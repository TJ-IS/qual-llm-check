---
otero_id: 28358
otero_key: "85Q7GDAS"
title: "Blessing or Curse? Implications of Data Brokers for Publisher Competition"
authors: "Xin Zhang; Wei Thoo Yue; Ran (Alan) Zhang; Yugang Yu"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0227"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Blessing or Curse? Implications of Data Brokers for Publisher Competition

Xin Zhang,<sup>a</sup> Wei Thoo Yue,<sup>b,</sup>\* Ran (Alan) Zhang,<sup>c</sup> Yugang Yu<sup>a</sup>

<sup>a</sup> Anhui Province Key Laboratory of Contemporary Logistics and Supply Chain, International Institute of Finance, School of Management, University of Science and Technology of China, Hefei, Anhui 230026, China; <sup>b</sup> Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong; <sup>c</sup> Department of ISQS, Rawls College of Business, Texas Tech University, Lubbock, Texas 79409 \*Corresponding author

Contact: zx01@ustc.edu.cn, https://orcid.org/0000-0002-6582-9253 (XZ); wei.t.yue@cityu.edu.hk, https://orcid.org/0000-0002-1344-153X (WTY); ran.alan.zhang@ttu.edu, https://orcid.org/0009-0001-6233-1927 (R(A)Z); ygyu@ustc.edu.cn, https://orcid.org/0000-0003-2882-5584 (YY)

Received: April 3, 2022 Revised: January 26, 2023; October 8, 2023; February 28, 2024 Accepted: March 5, 2024 Published Online in Articles in Advance: April 1, 2024

https://doi.org/10.1287/isre.2022.0227

Copyright: © 2024 INFORMS

Abstract. The abundance of consumer data has given rise to a new data broker industry that plays a pivotal role in targeted advertising. Many publishers rely on data brokers to gain (i) individual insights drawn from their own data or (ii) collective insights drawn from both their data and those of their competitors, thus improving their targeting capabilities. As data brokers control large volumes of data, they can govern how data insights are sold to downstream publishers. Despite their importance, prior studies provide little insight into the strategic function of data brokers and their subsequent impact on downstream competition. To address this research gap, we build an analytical model to analyze the interactions among a data broker, two competing publishers, and advertisers. Our analysis yields several novel findings. First, we show that the data broker may strategically set prices in a manner that leads to the exclusive selling of collective insights to one publisher, as opposed to nonexclusive selling involving two publishers. This result implies that it may be advantageous for the data broker to pursue an exclusive strategy that makes data insights scarcer for some firms. Second, we illustrate that competition between publishers can be either facilitated or impeded by the data broker depending on the broker’s interests when selling the data insights. Finally, the data broker may induce both competition-mitigation and value-enhancing effects that affect aggregate welfare. Interestingly, although the data broker’s decision (i.e., exclusive selling) may reduce market competition, the aggregate welfare can still improve because collective insights allow publishers to increase their targeting value for advertisers more efficiently.

History: Giri Kumar Tayi, Senior Editor; Atanu Lahiri, Associate Editor

Funding: This work was supported by the National Natural Science Foundation of China [Grants 72301267, 71921001, 72091215/72091210]. This work was supported by Research Grants Council, University Grants Committee, Hong Kong [CityU 11502319]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0227.

Keywords: data broker • data analytics • data externality • publisher competition • targeted advertising

## 1. Introduction

The explosion of consumer data has created tremendous opportunities for interested parties to extract the data’s value. This is evident in the data broker industry, which plays a pivotal role in the circulation of data products in today’s digital economy. A recent media report estimates the worth of the data broker industry by 2030 at approximately \$382 billion (MMR 2023). Traditionally, data brokers have been recognized for their role in collecting consumer data and selling raw data. However, with the advancement of data analytics techniques, data brokers now possess the ability to derive high-value insights from the data they collect. For example, data brokers such as Oracle, Lotame, and OnAudience have collected data from various sources, to generate and sell valuable insights. In this study, we specifically direct attention to this evolving landscape, focusing on data brokers that specialize in selling insights rather than raw data.

Central to the operations of data brokers is the sale of insights, facilitated by advanced data analytics techniques and rich data collection. Data brokers can sell these insights to companies that use them for advertising and marketing. Many publishers (e.g., Forbes, New York Daily News) have purchased data insights from data brokers or data management platforms (e.g., Lotame and Oracle), to sell their ad inventory more effectively via direct ad sales and programmatic advertising channels. Interacting with multiple publishers, data brokers’ unique position as data aggregators enables them to offer various data-enabled market insights. Specifically, a data broker can offer (i) individual insights generated from a publisher’s own data and (ii) collective insights generated from a publisher’s own data and other publishers’ (i.e., competitors’) data. For instance, Oracle, a prominent data broker, may offer individual insights to Forbes by analyzing the publisher’s first-party data. Oracle can also provide Forbes with collective insights by integrating third-party (including other publishers’) data.<sup>1</sup> Regarding the pricing scheme, data brokers have been selling data insights with flat-fee pricing (e.g., a fixed subscription price) (Moore 2016, MMR 2023). For example, the data broker OnAudience discloses on its website that it collects publishers’ audience data to create audience segments and sells data insights at a fixed subscription price.<sup>2</sup> Further, OnAudience indicates that data brokers usually charge an additional price for the use of thirdparty data (e.g., other publishers’ data) to generate data insights.

Publishers have incentives to purchase individual insights that can help publishers better understand their users’ behaviors, trends, and intentions, empowering publishers to build consumer profiles and create targetable audience segments. In turn, these enable publishers to offer advertisers greater targeting value, allowing publishers to sell more ad impressions and earn greater ad revenue. A media report shows that buying data insights from Lotame increased New York Daily News direct ad sales revenue by 15%.<sup>3</sup>

Moreover, publishers also have incentives to purchase collective insights derived from various data sources. These richer insights furnish publishers with a more holistic view of consumer profiles and enhance their consumer-targeting capabilities (Gu et al. 2022). For instance, many companies find that combining browsing history with purchasing history offers a more comprehensive view of the targeted segments. This benefit is known as data externality or data synergy as it is achieved by integrating a variety of datasets (Weibl and Hess 2020, Ichihashi 2021). In practice, the strength of data externality determines the merged value of collective insights. Specifically, when data externality is high (low), the merged value of collective insights may be higher (lower) than the sum of the values of two individual insights, implying that the collective data are superadditive (subadditive) (Gu et al. 2022). Therefore, the extent to which a data broker may improve a publisher’s targeting precision is contingent on several crucial factors, including the strength of data externality and the data broker’s analytics capabilities. These factors affect the price that a data broker can charge for data insights.

While data have become an essential source of competitive advantage, the impact of data brokers on market competition is a topic of considerable debate. Advocates of data brokers assert that they can provide access to crucial data, thus leveling the playing field fo smaller firms (Katz 2019). Nevertheless, some policymakers worry that data brokers’ control of extensive data gives them market power that allows devising different pricing strategies that potentially favor larger firms and distort market dynamics (Bourreau et al. 2017). Despite this risk, few studies have examined data brokers’ impact on downstream market competition, especially considering the impact of data externality and data analytics capability.

To fill this gap in the literature, this study examines the competitive implications of data brokers operating in the market. We focus on the targeted advertising industry, where publishers such as Forbes and the New York Daily News stand to benefit from the insights that data brokers sell (Melendez and Pasternack 2019). These insights enable publishers to enhance their consumer targeting capabilities, incentivizing advertisers to purchase ad space on their websites. This study focuses on the strategic interactions between a data broker and competing publishers. Typically, a data broker provides a pricing menu for different types of data insights, and publishers select one. To maximize its profit, the data broker can devise a pricing menu that incentivizes only one publisher to purchase collective insights (exclusive selling) or entices both publish ers to buy collective insights (nonexclusive selling).

In this paper, we investigate the following research questions: (1) What are the competing publishers’ strategies for purchasing data insights? (2) What are the data broker’s optimal pricing and selling strategies for data insights? (3) How do a data broker’s strategies affect publishers’ competitive outcomes, advertiser surplus, and aggregate welfare? We address these questions by developing an analytical model comprising a data broker, two competing publishers associated with different amounts of consumer data, and a unit mass of advertisers. We define the publisher associated with more data as the large publisher, while the other is termed the small publisher.

The differentiation of large and small publishers allows us to examine whether the data broker’s strategies could lead to an uneven market playing field and to consider the policy implications. In our model, we assume that the data broker has collected the publishers’ consumer data through multiple channels and can either generate individual insights relevant to one pub lisher or collective insights that relate to both. We model the problem as a three-stage game. In Stage 1, the data broker, who is a market leader, determines the optimal pricing strategies for data insights. In Stage 2, the publishers decide their data insights purchasing strategies and ad pricing strategies. In Stage 3, advertisers make ad purchasing decisions between publishers.

Our analysis yields several novel results that reveal how data brokers may affect the downstream industry. Before determining the data brokers’ optimal pricing strategies, we first examine the publishers’ incentives to purchase data insights. A common misconception is that small publishers have a greater incentive to purchase collective insights because they can gain access to more external data that would significantly improve their targeting capabilities (i.e., value-enhancing effect). However, our results reveal that drawing insights from the large publisher may reduce the targeting differentiation between the publishers, intensifying competition and reducing the small publisher’s profit. Thus, the large publisher may have a greater incentive to buy collective insights, leading to greater targeting differentiation and weaker competition (i.e., competition-mitigation effect).

Second, our analysis sheds light on the interactive effects of data externality and data analytics capability on the data broker’s optimal pricing and selling strategies for data insights. Intuitively, when data externality is relatively high (e.g., data are considerably superadditive and the merged value of collective insights is high), one might think that the data broker would choose to sell collective insights to both publishers. However, our finding suggests that this intuition does not always hold. Indiscriminately selling collective insights to both publishers could actually intensify downstream competition between them, thereby reducing their willingness to pay (WTP) for collective insights. Instead, the data broker may achieve optimal profit by strategically setting prices such that only one publisher chooses to buy collective insights. This approach reduces market competition, allowing the broker to command a higher price for collective insights. Finally, when data externality and the data analytics capability of the data broker are moderate, it becomes advantageous for the data broker to offer prices that entice both publishers to purchase collective insights. In this case, both publishers have a relatively high WTP for collective insights as their acquisition does not significantly intensify competition, and collective insights enable publishers to enhance their targeting precision for advertisers.

From the perspective of public policy, our analysis suggests that the presence of a data broker can either increase or reduce market competition, depending on its strategies for selling data insights. When the data broker sells collective insights only to the small publisher or to both publishers, the small publisher can gain a greater competitive advantage. This will intensify competition between publishers, leading to a higher advertiser surplus and a leveling of the market playing field. However, having a stronger capability for data analytics may motivate the data broker to sell collective insights exclusively to the large publisher, which will soften competition and result in a lower advertiser surplus. Finally, whether the data broker improves or diminishes aggregate welfare depends on the competition-mitigation and value-enhancing effects created in the market. Aggregate welfare can still improve even though the data broker’s decision may reduce market competition because the data broker’s collective insights enable publishers to increase their targeting value for advertisers more efficiently.

The remainder of this study is organized as follows. In Section 2, we review the related literature. We then describe our model in Section 3 before analyzing it and reporting the results in Section 4. Next, Section 5 outlines several extensions to the main model. Finally, we conclude the study by discussing our contributions and the relevant managerial implications in Section 6.

## 2. Literature Review

This study is closely related to three streams of literature: (i) online data markets, (ii) data externality, and (iii) targeted advertising. In this section, we review relevant studies in each stream and highlight the research gaps.

## 2.1. Online Data Markets

In line with the growing importance of consumer data, there is an emerging body of literature on online data markets, where data brokers play the role of data suppli ers (Bergemann and Bonatti 2019, Acemoglu et al. 2022). Previous studies have examined data brokers’ optimal data-provisioning and pricing strategies under various contexts. For example, Braulin and Valletti (2016) and Montes et al. (2019) consider a scenario in which the data broker sells consumer preference information to downstream competitors for price-discriminating consumers. Both studies show that a data broker can benefit by providing information exclusively to one of the downstream firms because it can relax competition between the firms. Ray et al. (2020) explore how to nego tiate a suitable price for the data that is acceptable to both the seller and buyer. They find that providing a demonstration is beneficial to the data broker when the buyer is biased and underestimates the data’s value.

Other studies examine the data broker’s decisions about data quality. For instance, Bimpikis et al. (2019) show that when selling data for demand prediction, it may be optimal for the data broker to distort the data with noisy signals and provide data of an inferior quality to ease competition. Likewise, Zhang et al. (2019) investigate the data quality decisions of data brokers that also offer ad delivery services. They find that the data broker may choose to provide low-quality data to incentivize firms to use the data broker’s ad delivery service.

Although our study is similar to papers that examine the impact of data brokers on market competition, it differs from them in the following aspects. First, we delve into the role of data brokers in the new context of targeted advertising and incorporate strategic interactions among the data broker, publishers, and advertisers. In contrast to prior literature that only considers individual insights, we consider a setting in which the data broker offers a menu of data insights, including both individual and collective insights. Aggregating data from different firms creates a data externality effect that previous studies have not taken into account. Second, the prior literature does not consider the characteristics of the data broker, such as its data analytics capability. In this study, we explicitly model this factor and find that it has a significant impact on the data broker’s strategies for selling data insights.

## 2.2. Data Externality

Since today’s firms can collect an abundance of diverse data, scholars have paid increasing attention to how firms can generate insights from these data. Data externality implies that the collection of data about some consumers enables firms to infer information about others through advanced analytics techniques (Mac-Carthy 2010, Ichihashi 2021). Prior studies have considered the impact of data externality on consumers incentives to share their data with firms. For instance, Acemoglu et al. (2022) show that data externality leads consumers to share data excessively, compromising consumer privacy and hurting social welfare. Similarly, Choi et al. (2019) show that data externality motivates firms to collect excessive consumer data, reducing consumer surplus. In contrast to these studies, our study focuses on the impact of data externality from the perspective of the data broker rather than the consumers.

Our study is close to Gu et al. (2022), which also considers the impact of data externality and examines the impact of the merged value of two datasets on data brokers’ optimal data selling strategies. Specifically, Gu et al. (2022) consider a setting with three players: two competing data brokers and a downstream data buyer. They investigate whether and when two data brokers have incentives to cooperate or compete with each other. They find that the optimal strategy of data brokers depends on the nature of the merged datasets. If data are subadditive (i.e., the combined value is lower than the sum of the values of the two datasets), data brokers have incentives to cooperate and share their data. When data are superadditive (i.e., the combined value is equal to or greater than the sum of the two data sets), data brokers compete and sell their datasets independently.

Our paper differs from Gu et al. (2022) in several important ways. First, our model considers a more complex setting including four players in the context of targeted advertising: a monopoly data broker, two competing publishers, and advertisers. Second, Gu et al. (2022) examine the impact of the value of merged datasets on the optimal strategy of upstream competing data brokers, that is, whether to share data or not. In their paper, they focus on the competition between two data brokers. In contrast, our study focuses on a monopoly data broker’s data insights selling strategies, and their impact on the competition between two downstream publishers. Our result shows that when the collective data are superadditive, the data broker will choose to sell collective insights; however, it may not sell collective insights to both publishers, as doing so would intensify downstream competition between publishers and lead to a lower WTP from publishers. Thus, the data broker achieves better performance by setting prices such that only one publisher chooses to buy collective insights.

## 2.3. Targeted Advertising

There is an expanding body of literature on targeted advertising, in which consumer data play an important role in helping firms target relevant consumers (Athey and Gans 2010, Goldfarb and Tucker 2011). Some studies have shown that targeted advertising improves matching precision between ads and consumers, thus benefiting consumers by improving their purchases (Bergemann and Bonatti 2011). However, Todri et al. (2020) demonstrate that targeted advertising can annoy consumers when their personal information is used to improve advertising effectiveness. Other studies have examined how targeted advertising affects firms’ competitive landscape. For example, Chen and Stallaert (2014) investigate how behavioral targeting can intensify competition and reduce publishers’ revenue. Meanwhile, Chen et al. (2017) examine the competitive implications of mobile geo-targeting and find that it can mitigate interfirm price competition and enhance firms’ profits. Finally, Gal-Or et al. (2018) analyze the effect of consumer privacy concerns on competing publishers investment decisions related to targeting capability and the subsequent impact on publisher competition.

Our study extends prior studies in the targeted advertising setting, which have thus far omitted the data broker. Hence, the literature ignores the impact of data brokers on the availability of data insights to downstream publishers, which has a significant effect on the publishers’ competitive edge. By incorporating the data broker into our model, this paper advances the understanding of the strategic interactions between the major players in the online advertising ecosystem.

## 3. Baseline Model

In this section, we introduce our baseline model, con sisting of four players: a data broker, two competing publishers, and a unit mass of advertisers. We describe below each player’s strategic decisions.

## 3.1. Data Broker

The data broker collects consumer data from the two publishers and analyzes the data to generate market insights, which can enhance the targeting value that publishers offer to advertisers. We use α $( 0 < \alpha < 1 )$ to represent the data broker’s data analytics capability. As α is often constrained by the industrial technology level (Koh et al. 2017, Belleflamme et al. 2020), we assume that it is exogenous and its value is common knowledge.

The data broker offers a menu of data insights, including (i) individual insights derived from a publisher’s own data and (ii) collective insights derived from a publisher’s data and its competitor’s data. A publisher has incentives to purchase collective insights because its competitor’s data (e.g., third-party data) can complement the publisher’s own data, enabling it to build more precise consumer profiles and improve targeting precision for advertisers (Banaszczyk and Chmielewski 2023). Such benefits from external data are referred to as data externality. In one example of such benefits, an industrial report shows that several large publishers in Europe have pooled their data to improve the effectiveness of targeted advertising (Davies 2016).

As data have become a valuable asset, the data broker’s objective is to maximize its profit by developing an optimal pricing menu for different types of data insights. Industrial reports and real-world practices suggest that flat-fee pricing (or lump-sum pricing) is a common practice that has been widely adopted by data brokers (Moore 2016, Leetaru 2018, Maximize Market Research 2023). For example, OnAudience, a major data broker specializing in targeted advertising, adopts a straightforward flat-fee pricing model (e.g., a fixed subscription price) for their analyzed datasets, and it indicates that data brokers usually charge additional price for the use of third-party data.<sup>4</sup> As highlighted by Mehta et al. (2021), such a flat-fee pricing model is easy to comprehend and execute.

Following this practice, we denote the price of each analyzed data set as w. In this manner, the data broker sets a price w for individual insights because they are derived from one publisher’s data (i.e., one analyzed data set) and a price 2w for collective insights as they include both individual insights and insights derived from the competitor’s data (i.e., two analyzed datasets).<sup>5</sup> Given the complicated interactions between the data broker and publishers, this simplified pricing model serves as a starting point to understand the key dynamics of the data broker industry. In our model extension (Section 5.1), we investigate another pricing model in which the data broker sets the prices for individual insights and collective insights independently, denoted by w and $\phi ,$ , respectively. We also consider on-demand pricing in the Online Appendix B, where the price for each data set depends on its number of records. Our analysis shows that the main results remain qualitatively unchanged.

Given the pricing menu offered by the data broker, publishers select one type of insight to maximize their payoffs. As the market leader, the data broker optimally sets its prices such that publishers may purchase individual insights or collective insights in the way the data broker expects. Therefore, the data broker’s pricing decisions may lead to one of three purchasing scenarios: (i) both publishers purchase collective insights; (ii) one publisher purchases collective insights while the other purchases individual insights; or (iii) both publishers purchase individual insights.

Depending on the publishers’ purchasing decisions, the data broker’s profits (denoted by $\pi _ { b } )$ can be (i) $\pi _ { b } = 4 w ;$ (ii) $\pi _ { b } = 3 w ;$ or (iii) $\pi _ { b } = 2 w ,$ corresponding to the three abovementioned cases, respectively. The data broker determines the optimal price for its data insights to maximize its profit.

## 3.2. Publishers

We consider two competing publishers indexed by $i = 1 .$ , 2. Publishers have different amounts of daily web traffic due to their popularity. For instance, The New York Times has three times as many page views as For-$b e s . ^ { 6 }$ Therefore, the data broker can collect different amounts of consumer data from publishers’ websites. Without loss of generality, the total amount of consumer data associated with Publisher 1 is normalized to 1, while the total amount of consumer data related to Publisher 2 is denoted by $\beta ( \beta < 1 ) . \ l ^ { 7 }$ Hereafter, we refer to Publisher 1 as the large publisher and Publisher 2 as the small publisher.

To improve their data value and remain competitive in the digital advertising landscape, publishers can buy data insights from data brokers to improve ad targeting for advertisers. For example, Forbes has announced publicly that it has purchased data insights from Oracle to help advertisers improve their targeting precision (Kingham and Carbonell 2016). Specifically, each publisher may choose to purchase (i) individual insights (denoted by O) or (ii) collective insights (denoted by B). For expositional convenience, we use $s _ { i }$ to represent publisheri’s decisions, where $s _ { i } \in \{ O , B \}$ . Table 1 summarizes the publishers’ decision matrix.<sup>8</sup>

As mentioned above, the data broker charges a price $w$ for the individual data insights, which is the cost incurred by publishers. When choosing B, the publisher needs to pay an additional price w to the data broker to obtain additional insights drawn from its competitor’s data. Following prior literature (Gal-Or et al. $2 0 1 8 ,$ Chatterjee and Zhou 2021), we consider the scenario where publishers sell ad inventory directly to advertisers at a lump-sum price for a fixed number of impressions. Hence, publisher $i ^ { \prime } \mathrm { s }$ profit functions under different strategies $s _ { i }$ can be formulated as follows: (i) when $s _ { i } = O , \pi _ { i } = p _ { i } D _ { i } - w ;$ (ii) when $s _ { i } = B , \quad \pi _ { i } =$ $p _ { i } D _ { i } -$ 2w where $D _ { i }$ is the advertisers’ demand and $p _ { i }$ is the ad price that the publisher charges to advertisers for targeted ads.<sup>9</sup>

Table 1. Publishers’ Decision Matrix

<table><tr><td>Publisher 1/Publisher 2</td><td>O</td><td>B</td></tr><tr><td>O</td><td>OO</td><td>OB</td></tr><tr><td>B</td><td>BO</td><td>BB</td></tr></table>

## 3.3. Advertisers

We consider a unit mass of advertisers that seek to purchase targeted ads from two publishers. We assume that advertisers are heterogeneous in their valuation (v) for publishers’ daily traffic and that v follows a uniform distribution $( \mathrm { i . e . , } \ v \sim U [ 0 , 1 ] )$ . Depending on the publishers’ strategies for data insights purchasing, the advertisers obtain different amounts of utility when displaying ads on publishers’ websites. Typically, publishers can directly disclose to advertisers about their insights purchasing practice, including whether they purchase data insights from a data broker. For example, as discussed in a media report, Forbes communicates to its advertisers that it has purchased the data insights from the data management platform Krux to improve targeting for advertisers (Aquino 2014). The report also indicated that Forbes has long been transparent with advertisers about how it leverages the data broker’s advanced analytics capability to acquire consumer insights derived from its own data $( \mathrm { i . e . , }$ individual insights) and third-party data $( \mathrm { i . e . , }$ collective insights). In addition to the direct disclosure to advertisers, publishers may also publicly announce their partnerships with certain data brokers and their insights purchasing activities (Kingham and Carbonell 2016). Given the above practical evidence, we assume that publishers’ insights purchasing decision is a public information for advertisers.

Specifically, when publishers choose to purchase individual insights (denoted by O), the advertiser’s utility obtained from each publisher is given by $U _ { 1 } = v +$ $\alpha - p _ { 1 }$ and $U _ { 2 } = \beta v + \alpha \beta - p _ { 2 }$ , where v and $\beta v$ represent the value derived from the two publishers’ daily traffic, respectively. Note that the two publishers’ daily traffic (proxied as their total amount of consumer data) is asymmetric and denoted by 1 and $\beta ,$ respectively. The second terms α and αβ represent the value of individual insights for improving the publishers targeting precision, which increases advertisers’ utility. These insights allow publishers to target consumers more accurately, leading to a higher conversion rate. Therefore, advertisers can obtain additional value when advertising on the publisher’s websites. This multiplication form of the value implies that as the data analytics capability (α) or amount of data $( \mathrm { e . g . } ,$ 1 or $\beta )$ increases, the realized value of individual insights for advertisers increases. The two publishers decide the ad prices $p _ { 1 }$ and $_ { p _ { 2 } , }$ and advertisers will purchase targeted ads from the publisher that offers a higher utility.

When publishers choose to purchase collective insights (denoted by B), they can leverage their competitor’s data to obtain additional insights. The additiona value of collective insights depends on the extent to which the competitor’s data complements the publish $\mathrm { e r ^ { \prime } s }$ own data; we refer to this as the strength of data externality (denoted by $\gamma )$ . In practice, a publisher can directly communicate with advertisers and disclose the value of $\gamma$ by revealing the value of its competitor’s data $( \mathrm { i . e . }$ , third-party data), which can be measured by the number of data records or consumer attributes that complement the publisher’s own data. As mentioned previously, Forbes communicates to its advertisers and marketing partners that it has purchased third-party data from Krux to build more refined consumer seg ments and improve targeting precision for advertisers (Aquino 2014). Through such direct communication, advertisers can know the value of collective insights. Based on the anecdotal evidence discussed, we assume $\gamma$ is common knowledge to advertisers. To ensure there is competition between the two publishers in all four cases, we assume $\begin{array} { r } { \gamma < \operatorname* { m i n } \lbrace \frac { ( 2 + \alpha ) ( 1 - \beta ) } { \alpha } , \frac { ( 1 - \alpha ) ( 1 - \beta ) } { \alpha \beta } \rbrace } \end{array}$ ; Otherwise, one publisher will be driven out of the market.

A high γ corresponds to the case where two publishers’ data are highly complementary; in this case, collective insights generate high value. We denote the additional value that advertisers may obtain from collective insights (relative to individual insights) as $\alpha \beta \gamma$ and $\alpha \gamma$ when buying from the large and small publishers, respectively. Taken together, when publishers buy collective insights, the advertiser’s utility obtained from the large and the small publishers can be written as $U _ { 1 } = v + \alpha + \alpha \beta \gamma - p _ { 1 }$ and $U _ { 2 } = \beta v + \alpha \beta +$ $\alpha \gamma - p _ { 2 }$ . Based on this formulation, when $\gamma = 1$ , both publishers obtain the same value from collective insights $( \mathrm { i . e . , } \alpha + \alpha \beta \gamma = \alpha \beta + \alpha \gamma )$ . When $\gamma > 1 ,$ , the small publisher obtains more value from collective insights $( \mathrm { i . e . , ~ } \alpha + \alpha \beta \gamma < \alpha \beta + \alpha \gamma )$ ). When $\gamma < 1$ , the large publisher obtains more value from collective insights $( \mathrm { i . e . , }$ $\alpha + \alpha \beta \gamma > \alpha \beta + \alpha \gamma )$ ). Moreover, when $\gamma > 1$ , the value of collective insights is greater than the sum of the values of two individual insights $( \mathrm { i . e . , } \alpha + \alpha \beta \gamma > \alpha + \alpha \beta )$ while when $\gamma < 1$ , the value of collective insights is lower than the sum of the values of two individual insights $( \mathrm { i . e . , ~ } \alpha + \alpha \beta \gamma < \ \alpha + \alpha \beta )$ . Following Gu et al. (2022), we refer to the data structure as superadditive when $\gamma > 1$ and subadditive when $\gamma < 1$

Table 2. Advertiser Utility in Each Strategy Profile

<table><tr><td colspan="3">Advertiser utility</td></tr><tr><td>Strategy profiles ( $s_1s_2$ )</td><td>Buying from Publisher 1</td><td>Buying from Publisher 2</td></tr><tr><td>OO</td><td> $U_1 = v + \alpha - p_1$ </td><td> $U_2 = \beta v + \alpha \beta - p_2$ </td></tr><tr><td>OB</td><td> $U_1 = v + \alpha - p_1$ </td><td> $U_2 = \beta v + \alpha \beta + \alpha \gamma - p_2$ </td></tr><tr><td>BO</td><td> $U_1 = v + \alpha + \alpha \beta \gamma - p_1$ </td><td> $U_2 = \beta v + \alpha \beta - p_2$ </td></tr><tr><td>BB</td><td> $U_1 = v + \alpha + \alpha \beta \gamma - p_1$ </td><td> $U_2 = \beta v + \alpha \beta + \alpha \gamma - p_2$ </td></tr></table>

Since there are four strategy profiles for the two publishers, we have four different combinations of advertisers’ utility. We summarize the advertiser’s utility functions for each strategy profile in Table 2. The first (second) argument in each strategy profile represents Publisher 1’s (2’s) decisions about purchasing data insights.

The timeline of the model is illustrated in Figure 1. In Stage 1, the data broker determines its optimal price w. In Stage 2, each publisher i determines its strategy for purchasing data insights s<sub>i</sub>. In Stage 3, the two publishers determine the ad price p<sub>i</sub>. In Stage 4, advertisers purchase targeted ads from the publisher that offers a higher utility.

## 4. Analysis and Results

We use the backward induction approach to derive the subgame perfect equilibrium. For analytical tractability, we assume that the advertiser market is fully covered in the baseline model.<sup>10</sup> This assumption has been widely used in the literature to simplify exposition (Chen et al. 2009, Desai et al. 2016, Gal-Or et al. 2018). In the model extension (Section 5.3.1), we relax this assumption by considering the scenario in which the advertiser market is not fully covered. All proofs are presented in the Online Appendix.

## 4.1. Publishers’ Decisions About Purchasing Data Insights and Pricing Ads

For each subgame in Stage 4, by letting $U _ { 1 } = U _ { 2 } ,$ , we can derive the marginal advertiser (denoted by $v ^ { * } ) _ { \ r { \ r } }$ , which is indifferent to buying ads from Publisher 1 or Publisher 2.

Hence, the advertiser demand for Publisher 1 is given by $D _ { 1 } = 1 - v ^ { * } ,$ , and the advertiser demand for Publisher 2 is $D _ { 2 } = v ^ { * }$ . Taking advertisers’ demand into account, we can derive the competing publishers optimal ad prices.

Lemma 1. The publishers’ equilibrium prices for each sub game are summarized as follows:

(i) in subgame OO, $\begin{array} { r } { , p _ { 1 } ^ { * } = \frac { ( \alpha + 2 ) ( 1 - \beta ) } { 3 } , p _ { 2 } ^ { * } = \frac { ( 1 - \alpha ) ( 1 - \beta ) } { 3 } ; } \end{array}$

(ii) in subgame OB, $\begin{array} { r } { p _ { 1 } ^ { * } = \frac { 2 ( 1 - \beta ) + \alpha ( 1 - \beta - \gamma ) } { 3 } , \quad p _ { 2 } ^ { * } = } \end{array}$ $\scriptstyle { \frac { 1 - \beta - \alpha ( 1 - \beta - \gamma ) } { 3 } } ;$

(iii) in subgame BO, $\begin{array} { r } { p _ { 1 } ^ { * } = \frac { ( \alpha + 2 ) ( 1 - \beta ) + \alpha \beta \gamma } { 3 } , \quad p _ { 2 } ^ { * } = } \end{array}$ ${ \frac { ( 1 - \alpha ) ( 1 - \beta ) - \alpha \beta \gamma } { 3 } } ;$

(iv) in subgame BB $\begin{array} { r } { , p _ { 1 } ^ { * } = \frac { ( 1 - \beta ) ( 2 + \alpha ( 1 - \gamma ) } { 3 } , p _ { 2 } ^ { * } = \frac { ( 1 - \beta ) ( 1 - \alpha ( 1 - \gamma ) ) } { 3 } . } \end{array}$

Based on the publishers’ optimal prices and the data broker’s data insights price w, we can obtain the competing publishers’ optimal profits under each strategy. Given the rival’s decisions (i.e., O or B), we derive each publisher’s optimal responses by comparing the pub lisher’s profits under the two choices; these responses are affected by the magnitude of w. Specifically, each publisher’s optimal responses are summarized as follows: (i) given that Publisher 1 chooses O, Publisher 2 would choose B if $w < w _ { 1 } ;$ (ii) given that Publisher 2 chooses O, Publisher 1 would choose B if $w < w _ { 2 } ;$ (iii) given that Publisher 1 chooses B, Publisher 2 would choose B if w < w ; (iv) given that Publisher 2 chooses B, Publisher 1 would choose B if $w < w _ { 4 }$

The detailed expression for each threshold of w can be found in the Online Appendix. The above result shows that each of the two publishers responds differently to its rival’s decisions. The thresholds $w _ { 1 }$ to $w _ { 4 }$ are all functions of $\alpha , \beta , \gamma$ . This suggests that the data analytics capability, data externality, and the small publisher’s data size play an interactive role in publishers decisions. In particular, $w _ { 1 }$ and $w _ { 2 }$ increase with $\gamma ,$ implying that as data externality increases, publishers are more willing to buy collective insights if their competitor chooses to buy individual insights. In contrast, $w _ { 3 }$ and $w _ { 4 }$ change nonmonotonically with $\gamma .$ This means that when data externality increases, publishers’ incentives to buy collective insights may increase or decrease, depending on other market parameters.

Figure 1. The Sequence of Events

<table><tr><td>Stage 1</td><td>Stage 2</td><td>Stage 3</td><td>Stage 4</td></tr><tr><td>The data broker determines the optimal price w.</td><td>Each publisher i selects its strategy for purchasing data insights si.</td><td>Each publisher i determines the price pi for targeted ads.</td><td>The advertisers choose one of the publishers to deliver their targeted ads.</td></tr></table>

By comparing the magnitude of the four thresholds, we obtain publishers’ strategies for purchasing data insights when the data broker’s pricing decision w is exogenously given. To ensure that both publishers have incentives to purchase at least individual insights, there exists an upper bound of the data broker’s price (denoted by w).

Lemma 2. Depending on the data broker’s data price $w ,$ the competing publishers’ strategies for purchasing data insights are summarized as follows:

(i) When $\gamma > \gamma _ { 1 } , \ i f \ 0 < w < w _ { 4 } .$ , BB is the equilibrium outcome; $i f w _ { 4 } < w < w _ { 1 } ,$ , OB is the equilibrium outcome; if $w _ { 1 } < w < \overline { { w } } , O O$ is the equilibrium outcome.

(ii) When $\gamma < \gamma _ { 1 } , i f 0 < w < w _ { 3 } .$ , BB is the equilibrium outcome; $i f w _ { 3 } < w < w _ { 2 } , B O$ is the equilibrium outcome; if $w _ { 2 } < w < \overline { { w } }$ , OO is the equilibrium outcome, where $\gamma _ { 1 } =$ ${ \frac { 2 ( \alpha - 1 + ( \alpha + 2 ) \beta ) } { \alpha ( 1 + \beta ) } } .$

Lemma 2 shows that depending on the data insights price w and data externality $\gamma ,$ there are two types of equilibrium outcomes for publishers’ insights purchasing strategies (shown in Figure 2).

First, when data externality γ is high $( { \mathrm { i . e . , ~ } } \gamma > \gamma _ { 1 } ) ,$ $w _ { 4 } < w _ { 3 }$ and $w _ { 2 } < w _ { 1 }$ . The relationship $w _ { 4 } < w _ { 3 }$ implies that if the rival chooses B, the large publisher is less incentivized to choose B (i.e., collective insights) than the small publisher. Thus, both publishers would choose B only if the data broker’s price is lower than the large publisher’s WTP, that is, $w < w _ { 4 }$ . As the data broker’s price increases (i.e., $w _ { 4 } < w < w _ { 1 } )$ , the small publisher is still incentivized to choose B, while the large publisher chooses O (i.e., individual insights). This leads to asymmetric choices (i.e., OB) between the two publishers.<sup>11</sup> The reason for this result is that the large publisher has more data, so the value of buying collective insights is higher for the small publisher than for the large publisher. The high data externality further amplifies the relative advantage that the small publisher gains through buying collective insights. Finally, when the data broker’s price exceeds $w _ { 1 }$ , the cost of obtaining collective insights outweighs the benefits. In this case, both publishers choose to only buy individual insights (i.e., OO is the equilibrium).

Second, when data externality is low $( { \mathrm { i . e . , ~ } } \gamma < \gamma _ { 1 } ) .$ $w _ { 3 } < w _ { 4 }$ and $w _ { 1 } < w _ { 2 }$ . This implies that if the rival chooses $B ,$ the small publisher has relatively less incentive to choose B. In this case, both publishers would choose B only if the data broker’s price is lower than the small publisher’s WTP $\displaystyle \left( \mathrm { i . e . , ~ } w < w _ { 3 } \right)$ . However, unlike the prior case, as the data broker’s price increases $( \mathrm { i . e . , } w _ { 3 } < w < w _ { 2 } )$ , the large publisher still has an incentive to buy collective insights, while the small publisher chooses to buy individual insights. This leads to the emergence of asymmetric BO equilibrium. This result can be explained as follows. When data externality is lower, both the large and small publishers obtain less value from collective insights. However, the small publisher would lose more because the large publisher has more data. Thus, when w increases, the small publisher chooses not to buy collective insights, as the cost of the additional insights outweighs their benefits. In contrast, the large publisher still has the incentive to buy because its value loss is relatively lower. Moreover, buying additional insights allows the large publisher to improve its targeting value more than the small publisher; this can help the large publisher further differentiate itself from its competitor, thereby alleviating competition. Finally, when the data insights price is relatively high $( \mathrm { i . e . , ~ } w > w _ { 2 } )$ ), both publishers choose not to buy collective insights.

In summary, our result shows that when the data broker’s price is exogenous, the strength of data externality plays a critical role in publishers’ data insights purchasing strategies. Given the asymmetric nature of the amount of data associated with the two publishers, we might expect the small publisher to have a greater incentive to buy collective insights $( \mathrm { i . e . , }$ BO is dominated by OB). However, our analysis shows that this is not always the case, as the chosen strategy may intensify competition. Instead, when data externality is low, BO may occur in the equilibrium.

Figure 2. (Color online) Publishers’ Strategies for Purchasing Data Insights When w Is Exogenous

<table><tr><td>BB</td><td>OB</td><td>OO</td></tr><tr><td>0</td><td>w4</td><td>w1</td></tr><tr><td colspan="3"> $\overline{w}$ </td></tr><tr><td colspan="3"> $\gamma >\gamma_1$ </td></tr><tr><td> $BB$ </td><td>BO</td><td>OO</td></tr><tr><td>0</td><td>w3</td><td>w2</td></tr><tr><td colspan="3"> $\overline{w}$ </td></tr><tr><td colspan="3"> $\gamma <\gamma_1$ </td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(i) When $\gamma &lt; \gamma_{1}$, the data broker's profits are  
$\left\{ \begin{array}{ll}\pi_b = 4w_3 &amp; BB: if 0 &lt; w &lt; w_3\\ \pi_b = 3w_2 &amp; BO: if w_3 &lt; w &lt; w_2\\ \pi_b = 2\overline{w} &amp; OO: if w_2 &lt; w &lt; \overline{w} \end{array} \right.$  
(ii) When $\gamma &gt;\gamma_{1}$, the data broker's profits are  
$\left\{ \begin{array}{ll}\pi_b = 4w_4 &amp; BB: if 0 &lt; w &lt; w_4\\ \pi_b = 3w_1 &amp; OB: if w_4 &lt; w &lt; w_1\\ \pi_b = 2\overline{w} &amp; OO: if w_1 &lt; w &lt; \overline{w} \end{array} \right.$
</div>

## 4.2. Data Broker’s Optimal Strategies for Selling Data Insights

We now consider the scenario in which the data broker determines its optimal pricing decisions. Based upon the publishers’ decisions in Lemma 2, the data broker strategically determines its data insights price w to maximize its profits. Our analysis consists of two steps. First, we derive the data broker’s optimal price and profit under the four purchasing strategies of publishers, which serves as a locally optimal solution. Then, we compare the data broker’s optimal profits across the four strategies to determine the optimal pricing that generates the maximum profit for the data broker.

Given that the data broker’s profits increase monotonically with the insights price $w ,$ the data broker always sets the price w as high as possible in each strategy for which the demand is known. Thus, based on Lemma $^ { 2 , }$ the data broker’s optimal prices (denoted by w<sup>∗</sup>) in each strategy are summarized as follows: in the BB case where both publishers purchase collective insights, $w ^ { * } = w _ { 4 }$ or $w ^ { * } = w _ { 3 } ;$ ; in the BO case where only the large publisher purchases collective insights, $w ^ { * } = w _ { 2 } ;$ in the OB case where only the small publisher purchases collective insights, $w ^ { * } = w _ { 1 } ;$ and in the OO case where both publishers purchase individual insights, $\boldsymbol { w } ^ { * } = \overline { { \boldsymbol { w } } }$ . We refer to OB and BO as exclusive selling strategies and BB as a nonexclusive selling strategy. Thus, the data broker’s optimal profit in each case are as follows:

We can now compare the data broker’s profits across different strategies and examine the conditions under which a strategy would generate the highest profit.

Proposition 1. The data broker’s equilibrium strategies for selling data insights are as follows:

(i) When data externality is low, the data broker sets optimal prices so that both publishers buy individual insights, that is, OO strategy occurs under the condition where (a) $\gamma _ { 1 } < \gamma < m i n \{ \gamma _ { 5 } , \gamma _ { 7 } \} o r ( b ) \gamma < m i n \{ \gamma _ { 1 } , \gamma _ { 3 } , \gamma _ { 6 } \} ;$

(ii) When the small publisher’s data size is relatively large and data externality is relatively low, the data broker sets prices so that the small (large) publisher buys individual (collective) insights, that is, BO strategy occurs under the condition where (a) $\beta > { \frac { 2 } { 3 } } ( { \sqrt { 7 } } - 2 )$ and max $\{ \gamma _ { 6 } , \gamma _ { 2 } \} < \gamma < \gamma _ { 1 }$ or (b) $\beta < \frac { 2 } { 3 } ( \sqrt { 7 } - 2 )$ and $\gamma _ { 6 } < \gamma <$ min $\{ \gamma _ { 1 } , \gamma _ { 2 } \} ;$ 3

(iii) When the small publisher’s data size is relatively small and data externality is high, the data broker sets prices so that the large (small) publisher buys individual (collective)

insights, that is, OB strategy occurs under the condition where $\gamma > \operatorname* { m a x } \{ \gamma _ { 1 } , \gamma _ { 4 } , \gamma _ { 7 } \} ;$

(iv) When both the small publisher’s data size and data externality are moderate, the data broker sets prices so that both publishers buy collective insights, that $i s ,$ BB strategy occurs when (a) $\dot { 0 } < \beta < \frac { 2 } { 3 } ( \sqrt { 7 } - 2 )$ and max $\{ \gamma _ { 2 } , \gamma _ { 3 } \} <$ $\gamma < \gamma _ { 1 } o r ( b ) \frac { 2 } { 3 } ( \sqrt { 7 } - 2 ) < \bar { \beta }$ and $\gamma _ { 3 } < \gamma <$ < min $\left\{ \gamma _ { 1 , } \gamma _ { 2 } \right\} o r$ (c) max $\{ \gamma _ { 1 } , \gamma _ { 5 } \} < \gamma < \gamma _ { 4 } ;$

where the expressions of different γ thresholds are presented in the Online Appendix.

Proposition 1 characterizes the conditions under which each strategy can arise as an equilibrium. It highlights the nontrivial interplay among the strength of data externality (which reflects the merged value of collective insights), the data broker’s data analytics capability, and publisher competition. In general, the data broker must balance the demand for data insights (e.g., exclusive or nonexclusive selling) and the price of data insights, which is affected by the intensity of publisher competition. Although nonexclusive selling guarantees a higher demand (in which the data broker sets prices to induce both publishers to buy collective insights), it may reduce publisher differentiation and thus intensify competition, resulting in lower prices. Hence, the data broker’s equilibrium strategies should balance the holistic impact of different market parameters on publisher competition.

To illustrate Proposition 1, Figure 3 depicts a spectrum of equilibrium outcomes produced by the interactive effects of the small publisher’s data size $\beta$ and data externality γ. A higher γ corresponds to a higher merged value of collective insights. In particular, when $\gamma < 1 ,$ , it implies that the collective data are subadditive and the merged value of collective insights is lower than the sum of the values of two individual insights. In this case, the data from two publishers may include some overlapping information or correlated data points, leading to diminishing returns of data. We find that when $\gamma$ is low $( \mathrm { e . g . } , \gamma = 0 . 2 )$ , both publishers have a low incentive to buy collective insights due to the small gain, and thus OO strategy occurs in equilibrium (see OO region in Figure 3).

Figure 3. (Color online) Data Broker’s Equilibrium Strategies Under Different β and γ Values (α � 0:3)  
![](/api/attachments/85Q7GDAS/fulltext/images/b308f392c3af7f00ec2fa285747eda1eb46f8f776d78597ab1bd90f42074d427.jpg)

On the contrary, when $\gamma \geq 1 _ { \cdot }$ , it implies that the collective data are superadditive and the merged value of collective insights is greater than the sum of the values of two individual insights. In this case, data from the two publishers complement each other and create synergies. As γ increases, although both publishers benefit from purchasing collective insights, the small publisher benefits more since it obtains more insights from the large publisher’s data set. This, in turn, gives the small publisher a greater incentive to buy collective insights (B) when $\gamma$ is high $( \mathrm { e . g . } , \ \gamma = 1 . 5 )$ ). However, the two publishers’ incentives to purchase collective insights also depend on the difference between the publishers data sizes. When $\gamma$ is relatively high and $\beta$ is relatively small, the small publisher’s WTP for collective insights is much higher than that of the large publisher. Therefore, the data broker benefits most by offering prices that encourage only the small publisher to purchase collective insights, while the large publisher chooses to buy individual insights (see OB region in Figure 3).

As $\beta$ increases, the small publisher’s data size becomes larger, so the large publisher obtains more value by purchasing collective insights. In this case, the small publisher has little incentive to buy collective insights, as doing so reduces the value differentiation between the two publishers and thus intensifies competition. Therefore, the small publisher fares better by buying individual insights. In conclusion, when $\beta$ is relatively large and $\gamma$ is relatively high, it is optimal for the data broker to set prices so that only the large publisher chooses to buy collective insights (see BO region in Figure 3). Note that when $\beta$ and $\gamma$ are sufficiently high, the small publisher will be driven out the market, which is not the interest of this study (i.e., nonfeasible region in Figure 3).

When data externality is moderate $( \mathrm { e . g . } , \gamma = 0 . 6 )$ and the data are subadditive but the reduction in the merged value of collective insights is not substantial, the impact of $\beta$ on equilibrium outcomes is more nuanced. Specifically, as $\beta$ increases from small to large, the equilibrium strategy evolves along the following path (Figure 3, horizontal arrow): $O O \to { \bar { O B } } \to B B \to { \bar { B O } }$ . The rationale for this equilibrium evolution is as follows. First, when $\beta$ is small, the small publisher’s data size increases as $\beta$ increases, which incentivizes the small publisher to obtain more external insights to compete against the large publisher. Meanwhile, the large publisher has a weaker incentive to buy collective insights given that $\beta$ is small. Thus, it is optimal for the data broker to set prices so that only the small publisher buys collective insights (i.e., the equilibrium switches from OO to OB).

As $\beta$ continues to increase, the large publisher’s incentive to buy external insights strengthens. In this case, the data broker benefits more by offering prices to induce both publishers to purchase collective insights (i.e., the equilibrium switches from OB to BB). As Figure 3 illustrates, the BB equilibrium comprises two subregions, $B B _ { 1 }$ and $B B _ { 2 } ,$ where the two publishers incentives to purchase collective insights differ. In $B B _ { 1 } ,$ the large publisher has a relatively weak incentive to purchase collective insights because of a relatively small $\beta .$ Consequently, the data broker’s price is subject to the large publisher’s WTP $( \mathrm { i . e . , } w ^ { \ast } = w _ { 4 } )$ . In contrast, in $B B _ { 2 }$ , the small publisher has a weaker incentive to purchase collective insights because doing so could intensify the competition. Thus, the data broker’s price is subject to the small publisher’s WTP $\left( \mathrm { i . e . , } w ^ { \ast } = w _ { 3 } \right)$

Finally, when $\beta$ is large, the small publisher chooses not to buy collective insights (i.e., the equilibrium switches from BB to BO). This is because the large $\beta$ itself diminishes the value differentiation between the large and small publishers. If the small publisher continues to purchase external insights derived from the large publisher’s data, the publishers’ differentiation would be further reduced, and the level of competition would become very intense. However, the large $\beta$ gives the large publisher a strong incentive to buy collective insights, which can help the large publisher differentiate itself from the small publisher. Because of this, the data broker will choose to sell collective insights only to the large publisher at a higher price. This result implies that the data broker may intentionally soften the competition between the publishers, leading to an anticompetitive outcome.

To further analyze the impact of the data broker’s data analytics capability, we illustrate how the data broker’s selling strategies may change due to the joint effect of data externality and data analytics capability when $\beta = 0 . 3$ (illustrated by Figure 4). We observe the following results. First, when the data broker’s data analytics capability is low $( \mathrm { e . g . } , \alpha = 0 . 1 )$ , the value of collective insights is low. In this case, both publishers have low incentives to buy collective insights even though the collective data are superadditive $( \mathrm { i . e . , }$ $\gamma > 1 )$ ). Hence, when the broker’s analytics capability is low, regardless of the degree of data externality, we find that the OO strategy occurs in equilibrium (see OO region in Figure 4).

Second, when the data analytics capability is mod erate $( \mathrm { e . g . } , \alpha = 0 . 4 )$ , we find that BB strategy and OB strategy will occur in equilibrium if data from two sources are not extremely subadditive. Specifically, as γ increases, the equilibrium will switch from OO to BB, then from BB to OB. The reason is two-fold. When α increases, the value of collective insights increases, which enhances both publishers’ incentives to buy them if γ is not too low (i.e., BB). However, as γ increases, the small publisher obtains more additional value from collective insights than that of the larger publisher. Hence, when γ is greater than a certain threshold (wherein γ can be less than 1), the data broker is better off offering prices that encourage only the small publisher to buy collective insights (i.e., OB).

Figure 4. (Color online) Data Broker’s Equilibrium Strategies Under Different α and γ Values (β � 0:3)  
![](/api/attachments/85Q7GDAS/fulltext/images/46ad06b97cd72407bd81602fcec20b9b5c41bb9d21244af8f9ba1cd8dfa1600e.jpg)

Finally, when the data analytics capability is large $( \mathrm { e . g . } , \ \alpha = 0 . 8 )$ , we find that the BO strategy is more likely to occur in equilibrium, and BO can occur when data are subadditive $( \gamma \leq 1 )$ or superadditive $( \gamma > 1 )$ while the OB strategy occurs when data are superadditive $( \mathrm { i . e . , } \gamma > 1 )$ ). This is because when α becomes very large, the value of collective insights is high; this gives the large publisher stronger incentives to buy collective insights to better compete with the small publisher. At the same time, the small publisher has no incentive to buy collective insights if γ is not very high (even though γ is greater than 1) because doing so would render its value provision closer to that of the large publisher and thus intensify competition. This finding demonstrates that anticompetitive outcomes are likely to arise when the data broker possesses a superior data analytics capability, as there is a tendency for the data broker to make an exclusive deal with the large publisher. As we will show later, this reveals the potential downsides of big data analytics from the public policy perspective, suggesting that data brokers may harm advertiser surplus and aggregate welfare.

In summary, our results indicate that data external ity, data analytics capability, and asymmetry in the amount of data between publishers play intertwined roles in determining the equilibrium outcomes. We find that when data are considerably subadditive (e.g., when consumer attributes between two datasets overlap significantly), the data broker tends to sell individual insights to both publishers. When data are near additive (including slightly subadditive and slightly superadditive), along with moderate analytics capabil ity and differences in data size between publishers, the data broker may benefit more by setting prices so that both publishers buy collective insights. In this case, both publishers are incentivized to purchase collective insights to enhance their targeting value while not causing fierce competition. Intuitively, when data are considerably superadditive and the merged value of collective insights is high, one might think that the data broker may choose to sell collective insights to both publishers. However, we find that it may not be optimal for the data broker to sell collective insights to both publishers in this case, as doing so would intensify downstream competition between publishers. Instead, depending on the magnitude of data analytics capabil ity and the publisher’s data size, the data broker fares better by pricing the insights so that only one publisher is incentivized to purchase collective insights. In this vein, making the market less competitive allows the broker to charge a higher price for collective insights.

## 4.3. Comparative Statics

In this subsection, we use comparative analysis to examine the impact of data analytics capability (α) and data externality (γ) on the data broker’s price, and advertiser surplus. We also examine the impact of data externality on publisher profits.

Proposition 2. The impacts of data analytics capability and data externality on the data broker’s price have the following properties:

(i) (The impact of ) As the data analytics capability increases, the data broker’s price exhibits a discrete decrease when the equilibrium switches from OB to BB.

(ii) (The impact of ) As data externality increases, th data broker’s price exhibits a discrete decrease when the equilibrium switches from BO to BB.

Figure 5 illustrates the impact of the data analytics capability (α) and data externality (γ) on the data broker’s price (denoted by w<sup>∗</sup>) and profits (denoted by π<sup>∗</sup>). As shown in this numerical example, when α and γ increase, the data broker’s price and profit increase within each equilibrium case; this is because a higher data analytics capability or data externality enhances both publishers’ WTP for the data insights. However, as α increases, the equilibrium may switch from OB to BB, and the data broker would decrease the price discretely to incentivize both publishers to buy collective insights (i.e., increase demand). Likewise, as γ increases, when the data structure changes from very subadditive to slightly subadditive, the equilibrium may switch from BO to BB, and the data broker also decreases the price discretely so that both publishers buy collective insights. In contrast, when the equilibrium switches from BB to OB or BO, the data broker chooses to increase their price so that only one publisher purchases collective insights.

Figure 5. (Color online) The Impact of α and γ on the Data Broker’s Price and Profit  
(a)  
![](/api/attachments/85Q7GDAS/fulltext/images/c54a9c1320a30c0f4f56fa0f25d0dd39b60aa90f0b00e3bd793d2900c4af7340.jpg)

(b)  
![](/api/attachments/85Q7GDAS/fulltext/images/0d6ac322ca13c689ca4d8af59145ef76105147097d12772835becaeda35b7d3b.jpg)  
Note. Panel (a) is based on parameter values $\beta = 0 . 3 , \gamma = 0 . 6 5 ;$ Panel (b) is based on parameter values $\beta = 0 . 3 , \alpha = 0 . 5 .$

Proposition 3. The impacts of data analytics capability and data externality on advertiser surplus have the following properties:

(i) (The impact of ) As α increases, advertiser surplus (AS) increases in each equilibrium case and exhibits a discrete decrease when the equilibrium switches from BB to BO.

(ii) (The impact of ) As γ increases, advertiser surplus increases in the BO, BB, and OB cases, and exhibits a discrete decrease when the equilibrium switches from BB to OB.

Figure 6 illustrates the results of Proposition 3. Proposition 3(i) shows that as the data analytics capability α improves, advertiser surplus increases in each equilib rium scenario (see Figure 6(a)). This result holds because both publishers can increase advertiser utility by providing a higher targeting value (i.e., value-enhancing effect). When the equilibrium switches from OO to OB, the small publisher gains additional insights from the competitor’s data, allowing the small publisher to enhance the targeting value for advertisers. As a result, the differentiation between the publishers decreases, leading to intensified competition and a discrete increase in adver tiser surplus.

Nevertheless, as the level of data analytics continues to increase, advertiser surplus decreases discretely when the equilibrium switches from BB to BO (Figure 6(a)). The underlying mechanism is that high data analytics facilitate an exclusive sale of collective insights by the data broker to the large publisher, softening competition. Moreover, the advertiser utility decreases because the small publisher provides lower targeting value to advertisers. This finding reveals that advances in data analyt ics will not necessarily improve advertiser surplus.

Likewise, Proposition 3(ii) indicates that as data externality increases, advertiser surplus increases in all cases except OO, as data externality is irrelevant in this case (Figure 6(b)). We find that when the data structure changes from subadditive to superadditive, advertiser surplus may decrease. This occurs because when the collective data are superadditive $( \gamma > 1 )$ , the equilibrium may switch from BB to OB, where the data broker may choose to sell collective insights exclusively to the small publisher. As a result, the large publisher cannot enhance advertiser utility by leveraging collective insights, which negatively affects advertiser surplus.

Figure 6. (Color online) The Impact of α and γ on Advertiser Surplus  
(a)  
![](/api/attachments/85Q7GDAS/fulltext/images/d4f935f76ea1c8a5d4f1a691b9ea2248a5375868eb411f43453996530e1e7564.jpg)

(b)  
![](/api/attachments/85Q7GDAS/fulltext/images/7030cd76a0d91de82d8ffb12a51207e08d73c9f323eae4d1d598eba610dc0c47.jpg)  
Note. Panel (a) is based on parameter values $\beta = 0 . 3 , \gamma = 0 . 8 ;$ Panel (b) is based on parameter value $\beta = 0 . 3 , \alpha = 0 . 5$

Overall, we show that both data analytics capability and data externality have a nonmonotonic effect on advertiser surplus. Specifically, advertiser surplus may first increase and then undergo a discrete decrease as each market parameter changes. These changes occur because the data broker may adopt different pricing strategies that affect the competitive structure of the downstream publisher market. An important caveat is that advances in data analytics capability may lead to exclusive deals for collective insights between the data broker and one of the publishers, resulting in an anticompetitive outcome and harming advertiser surplus.

Proposition 4. The impacts of data externality on publisher profits have the following properties:

(i) As γ increases, the small publisher’s profit exhibits a discrete increase when the equilibrium switches from BO to BB;

(ii) As γ increases, the large publisher’s profit exhibits a discrete decrease when the equilibrium switches from BO to BB.

Figure 7 illustrates the result of Proposition 4, highlighting the impact of data externality γ on the two publishers’ profits. In this numerical example, when γ increases, we find that the small publisher’s profit $( \mathrm { i . e . , ~ } \pi _ { 2 } ^ { \ast } )$ decreases within each case. This happens because the data broker, as the market leader, will charge a higher data price for the data insights as γ increases. This price increase outweighs the value gained from the data insights for the small publisher. However, the small publisher’s profit increases discretely when the equilibrium switches from BO to BB. This is because the small publisher can gain more value when switching from buying individual insights to collective insights, which increases the small publisher’s competitiveness. Furthermore, to incentivize the small publisher to buy collective insights, the data broker reduces the price of collective insights at the threshold. Both forces lead to a discrete increase in the small publisher’s profit.

Figure 7. (Color online) The Impact of γ on Publishers’ Profits  
(a)  
![](/api/attachments/85Q7GDAS/fulltext/images/06f071e6fecc9b37e0d442a5c5116dbf9183ab467d74f169eb6cb05d2a9fb08b.jpg)  
Note. Both Panel (a) and Panel (b) are based on parameter values $\beta = 0 . 3 , \alpha = 0 . 5 .$

Likewise, when the equilibrium switches from BB to OB, the small publisher’s profit also exhibits a discrete increase. This is because a higher γ enables the small publisher to derive more value from collective insights than that of the large publisher. When γ is sufficiently high, it is more advantageous for the large publisher to buy only individual insights (i.e., shifting from B to O) to save costs and soften the competition with the small publisher. This finding implies that as γ becomes sufficiently large, the small publisher may fare better as it may gain a competitive advantage compared with the large publisher.

In terms of the large publisher, when γ increases, Figure 7 shows that the large publisher’s profit $( \mathrm { i . e . , } \pi _ { 1 } ^ { \ast } )$ decreases within each case. There are several forces at play. First, when γ increases, the data broker is able to charge a higher price for collective insights, which hurts the large publisher’s profit even in the BO case where only the large publisher buys collective insights. Second, in the BB case, the small publisher gains more value from buying collective insights, which weakens the large publisher’s competitive advantage. Hence, when the equilibrium switches from BO to BB, the large publisher’s profit suffers a discrete decrease. Finally, when γ becomes high, OB equilibrium occurs and only the small publisher buys collective insights. In this case, the increase in γ further causes the large publisher to lose its competitive advantage. As a result, the large publisher’s profit exhibits a discrete decrease when the equilibrium switches from BB to OB, and it decreases within the OB case.

(b)  
![](/api/attachments/85Q7GDAS/fulltext/images/6a1609e97097a0938322e3d72b4a2393c768b05a01e98683f44bd8237847caf4.jpg)

Overall, our results show that when γ increases, both publishers’ profits may decrease because the increase in γ changes the competition between the two publishers, and the data broker, who acts as a market leader, may charge a higher price for data insights. However, when γ increases, we find that the small publisher can fare better at certain thresholds when it starts to purchase collective insights or the large publisher no longer buys collective insights. This result provides support for the industrial point of view that the emergence of data brokers may level the playing field for smaller firms (Katz 2019).

## 4.4. The Welfare Implications of Data Sharing Between Publishers

In previous sections, we identified the conditions under which the data broker may choose to sell collective insights exclusively to one publisher, both publishers, or neither publisher through different pricing decisions. When the data broker sells collective insights, it essentially facilitates data sharing (exchange) between the two publishers, as each publisher can obtain additional insights from its competitor’s data. However, antitrust authorities are concerned that data sharing via data brokers may soften competition and facilitate collusive behavior, thus hurting consumer surplus and aggregate welfare (Richter and Slowinski 2019). Some policymakers have prevented data brokers from sharing data among competitors. For instance, the Finnish Competition and Consumer Authority recently terminated a data broker’s business of sharing data between two dominant retailers in Finland (Koski 2018).

In this section, we examine how prohibiting data brokers’ data-sharing practices affects advertiser surplus and the aggregate welfare comprised of advertiser surplus, publishers’ profits, and the data broker’s profit. Specifically, with regulation that prohibits sharing competing firms’ data, the data broker can only offer individual insights to each publisher. In the context of our model, this means that only OO is feasible for both publishers. Without such regulation, however, other scenarios where the data broker shares the competitor’s data to generate collective insights (including BB, OB, and BO) can occur in equilibrium. Therefore, we compare the equilibrium outcomes with and without datasharing regulation to examine its potential impact.

Proposition 5. When compared with a regulated environment that prohibits data sharing between publishers, the following can be observed in an unregulated environment:

(i) (Advertiser surplus) Advertiser surplus is higher in BB, BO, and OB;

(ii) (Aggregate welfare) Aggregate welfare is higher in BO, it is higher in OB $i f \gamma > \gamma _ { 1 } ^ { * }$ , and it is higher in BB if $\gamma > \gamma _ { 2 } ^ { * }$

Proposition 5(i) shows that regardless of whether the data broker shares the competing publisher’s data exclusively or nonexclusively, advertiser surplus is higher than the OO case in which data sharing is not feasible. This result is driven by two effects: the competition effect and the value-enhancing effect. Specifically, compared with the OO case, the small publisher in the OB case can enhance the targeting value for advertisers to a greater extent by purchasing collective insights. Thus, the advertiser’s utility for the small publisher becomes closer to its utility for the large pub lisher. As a result, the differentiation between the publishers decreases, leading to intensified competition and higher advertiser surplus. At the same time, due to the data externality effect, combining the two publishers’ data allows the small publisher to offer advertisers a higher targeting value, which also increases advertiser surplus. Hence, both the competition and value-enhancing effects contribute to increasing advertiser surplus. In the BO case, competition between publishers is softened because when the large publisher purchases collective insights, the value differentiation between publishers increases. The reduction in competition may result in higher ad prices, thus reducing the advertiser surplus. However, the valueenhancing effect still exists and improves advertiser surplus, as the large publisher offers a higher targeting value to advertisers. Our results show that the valueenhancing effect outweighs the negative competitionmitigation effect, leading to a net increase in advertiser surplus. Finally, in the BB case, the value-enhancing effect is more prominent, as both publishers can provide high targeting value to advertisers. The valueenhancing effect still plays the dominant role in this case, leading to a higher advertiser surplus.

Proposition 5(ii) reveals that data sharing yields higher aggregate welfare in BO case than in the OO case. This occurs because data externality enables publishers to offer higher targeting value, increasing aggregate welfare to a large extent. In contrast, while advertiser surplus increases in the OB and BO cases, publishers profits decrease significantly in these cases. Only if data externality is relatively high can the increase in advertiser surplus compensate for the publishers’ profits loss, leading to a net increase in aggregate welfare.

In summary, our results suggest that regulations that prohibit data sharing do not necessarily benefit advertiser surplus and aggregate welfare. We show that data sharing via data brokers may promote publisher competition by reducing the large publisher’s market dominance. Moreover, data sharing can create additional value through data externality. In contrast, the exclusive use of data may lead to the underutilization of data value. These findings echo the recent data strategy proposed by the European Commission,<sup>12</sup> which emphasizes the social value of data sharing and advocates data openness in a secure environment (Martens et al. 2020).

## 5. Extensions and Robustness

In this section, we relax some of the assumptions made in the baseline model to check the robustness of our key results and potentially extend them. We summarize the key insights below and delegate some of the detailed analysis to Online Appendix B.

## 5.1. Independent Pricing Decisions for Individual and Collective Insights

In the baseline model, we assume that the data broker adopts a simple flat-fee pricing model for its data insights (i.e., analyzed datasets). Specifically, the data broker charges w for individual insights and 2w for collective insights. While this pricing model serves as a starting point to understand the key dynamics of the data broker industry, in practice, data brokers may also decide the price for individual insights and collective insights independently. In this extension, we investigate the data broker’s optimal independent pricing decisions and examine whether this pricing model changes its strategies for selling data insights.

As in the baseline model, the data broker first announces a pricing menu for different types of insights. We denote the data broker’s price for individual insights and collective insights as w and $\phi ,$ respectively. Given this pricing menu, each publisher selects one type of data insights. Depending on publisher i’s insights purchasing decisions (i.e., $s _ { i } = O \mathrm { ~ o r ~ } s _ { i } = B )$ , publisher i’s profit (denoted by $\pi _ { i } )$ can be rewritten as follows: (i) when $s _ { i } = O ,$ $\pi _ { i } = p _ { i } D _ { i } - w$ or (ii) when $s _ { i } = B , \pi _ { i } = p _ { i } D _ { i } - \phi ,$ , where $D _ { i }$ is the advertisers’ demand and $p _ { i }$ is the ad price that the publisher charges for targeted ads.

The data broker’s profit can be rewritten as follows: (i) in the BB case, $\pi _ { b } ^ { \dot { B } B } = 2 \phi ;$ (ii) in the OB case or BO case, $\pi _ { b } ^ { O B } = w + \phi \mathrm { o r } \bar { \pi } _ { b } ^ { B O } = \mathrm { \dot { \boldsymbol { w } } } + \phi ;$ or (iii) in the OO case, $\pi _ { b } ^ { O O } = 2 w$ . Following the same approach as in the baseline model, we first derive the data broker’s optimal pricing and profit in each case, which serves as a local optimal solution. Then, we compare the data broker’s optimal profit across different cases to determine the optimal pricing that provides the maximum profit.

$$
\begin{array}{l l} & \max _ {w} \pi_ {b} ^ {O O} = 2 w \\ s. t. & \pi_ {1} ^ {O O} \geq \pi_ {1} ^ {B O} \quad \text {(IC constraint)} \\ & \pi_ {2} ^ {O O} \geq \pi_ {2} ^ {O B} \quad \text {(IC constraint)} \\ & \pi_ {1} ^ {O O} \geq 0 \quad \text {(IR constraint)} \\ & \pi_ {2} ^ {O O} \geq 0 \quad \text {(IR constraint)} \end{array}
$$

Next, we describe the data broker’s profit-maximizing problem in each case, which is subject to the constraints of publishers’ incentive compatibility (IC) and individual rationality (IR). The data broker’s optimization problem in the OO case can be formulated as follows:

The optimization problem in the OB case can be formulated as follows:

$$
\max _ {w, \phi} \pi_ {b} ^ {O B} = w + \phi
$$

$$
s. t. \qquad \pi_ {1} ^ {O B} \geq \pi_ {1} ^ {B B}
$$

$$
\pi_ {2} ^ {O B} \geq \pi_ {2} ^ {O O}
$$

(IC constraint)

(IC constraint)

$$
\pi_ {1} ^ {O B} \geq 0
$$

(IR constraint)

$$
\pi_ {2} ^ {O B} \geq 0
$$

(IR constraint)

The optimization problem in the BO case can be formulated as follows:

$$
\begin{array}{r l} & {\underset {w, \phi} {\max} \pi_ {b} ^ {B O} = w + \phi} \\ {s. t.} & {\pi_ {1} ^ {B O} \geq \pi_ {1} ^ {O O}} \\ & {\pi_ {2} ^ {B O} \geq \pi_ {2} ^ {B B}} \\ & {\pi_ {1} ^ {B O} \geq 0} \\ & {\pi_ {2} ^ {B O} \geq 0} \end{array}
$$

(IC constraint)

(IC constraint)

(IR constraint)

(IR constraint)

Finally, the optimization problem in the BB case can be formulated as follows:

$$
\begin{array}{r l} & {\underset {\phi} {\max} \pi_ {b} ^ {B B} = 2 \phi} \\ {s. t.} & {\pi_ {1} ^ {B B} \geq \pi_ {1} ^ {O B}} \\ & {\pi_ {2} ^ {B B} \geq \pi_ {2} ^ {B O}} \\ & {\pi_ {1} ^ {B B} \geq 0} \\ & {\pi_ {2} ^ {B B} \geq 0} \end{array}
$$

(IC constraint)

(IC constraint)

(IR constraint)

(IR constraint)

The IR constraints in each case ensure that each publisher obtains nonnegative profit from buying data insights from the data broker. The IC constraints ensure that each publisher prefers the chosen decision to the alternative option. By solving the above optimization problems, we can derive the data broker’s optimal pricing decisions in each case. The results are summarized in the following lemma.

Lemma 3. The data broker’s optimal pricing decisions in each case are as follows:

(i) in the OO case, $\begin{array} { r } { w ^ { \ast } = \frac { 1 } { 9 } ( 1 - \alpha ) ^ { 2 } ( 1 - \beta ) ; } \end{array}$

(ii) in the OB case, when $\begin{array} { r } { \gamma < \frac { ( 1 + 2 \alpha ) ( 1 - \beta ) } { \alpha ( 2 - \beta ) } , \quad w ^ { * } = } \end{array}$ $\frac { ( 1 - \beta + \alpha ( \beta + \gamma - 1 ) ) ^ { 2 } - \alpha \beta \gamma ( 2 ( 2 + \alpha ) ( 1 - \beta ) - \alpha ( 2 - \beta ) \gamma ) } { 9 ( 1 - \beta ) } , \quad \phi ^ { * } = \frac { ( 1 - \beta + \alpha ( \beta - 1 + \gamma ) ) ^ { 2 } } { 9 ( 1 - \beta ) } ;$ when $\begin{array} { r } { \frac { ( 1 + 2 \alpha ) ( 1 - \beta ) } { \alpha ( 2 - \beta ) } < \gamma < \frac { ( 1 + 2 \alpha ) ( 1 - \beta ) } { \alpha } , ~ w ^ { \ast } = \frac { ( ( \alpha + 2 ) ( \beta - 1 ) + \alpha \gamma ) ^ { 2 } } { 9 ( 1 - \beta ) } , } \end{array}$

$$
\begin{array}{l} \phi^ {*} = \frac {(1 - \beta + \alpha (\beta - 1 + \gamma)) ^ {2}}{9 (1 - \beta)}; w h e n \gamma > \frac {(1 + 2 \alpha) (1 - \beta)}{\alpha}, w ^ {*} = \frac {((\alpha + 2) (\beta - 1) + \alpha \gamma) ^ {2}}{9 (1 - \beta)}, \\ \phi^ {*} = \frac {\alpha \gamma (2 (1 - \alpha) (1 - \beta) + \alpha \gamma) + ((2 + \alpha) (\beta - 1) + \alpha \gamma) ^ {2}}{9 (1 - \beta)}; \end{array}
$$

$$
\begin{array}{c} \text {(iii) in the BO case, w^{*} = \frac {(1 - \alpha - \beta + \alpha\beta(1 - \gamma))^{2}}{9(1- \beta)}, \phi^{*} =} \\ \frac {(\alpha + \beta - 1 + \alpha\beta(\gamma - 1)) ^ {2} + \alpha\beta\gamma(2(2 + \alpha)(1 - \beta) + \alpha\beta\gamma)}{9 (1 - \beta)}; \end{array}
$$

$$
\begin{array}{c} \text {(iv) in the BB case, when \gamma > \frac {2\alpha + 1}{2\alpha}, \phi^ {*} = \frac {(\alpha + 2 - \alpha\gamma)^{2} (1 - \beta)}{9};} \\ w h e n \gamma <   \frac {2 \alpha + 1}{2 \alpha}, \phi^ {*} = \frac {(1 - \alpha + \alpha \gamma) ^ {2} (1 - \beta)}{9}. \end{array}
$$

Based on the optimal price in Lemma $^ { 3 , }$ we can derive the data broker’s optimal profits in each case. By comparing the profits across different cases, we can derive the data broker’s optimal pricing decisions under different market conditions. These pricing decisions made by the data broker will result in different purchasing strategies by the publishers. Figure 8 illustrates the impact of $\beta$ and $\gamma$ on equilibrium outcomes when the data broker adopts the independent pricing scheme for collective insights and individual insights.

Consistent with the baseline model, we find that when $\gamma$ is relatively high and $\beta$ is not sufficiently large, the data broker is better off setting prices to induce only the small publisher to buy collective insights, leading to OB equilibrium. The reason is that the small publisher obtains a relatively higher value from buying collective insights than the large publisher when $\gamma$ is high and $\beta$ is not large; thus, the data broker can charge a higher price from the small publisher.

However, in contrast with the baseline model, when $\gamma$ is relatively low, we find BO and BB always dominate OO, causing OO not to occur in equilibrium. The intuition that BO dominates OO is as follows. When $\gamma$ is relatively low, the small publisher’s WTP for collec tive insights is relatively low. To induce publishers to buy collective insights, the data broker must set a low price. In the baseline model, due to the correlated pricing scheme, this will also lead to a low price for individual insights. Consequently, when $\gamma$ is relatively low, both the prices for collective insights and individual insights are reduced significantly. As a result, the data broker’s profit from selling collective insights to the large publisher and individual insights to the small publisher $( \mathrm { i } . \mathbf { e } . , B O )$ is lower than that of selling individual insights to both publishers by charging a higher individual price (i.e., OO). Therefore, in the baseline model, OO arises as the equilibrium when γ is low (see Figure 3). In contrast, in the extension model, the prices for collective insights and individual insights are independent. Therefore, even though the data broker charges a lower price for collective insights, the price for individual insights does not need to be very low. This independent pricing model enables the data broker to extract more revenue from publishers, leading to a higher profit for the data broker in the BO case than in the OO case. As a result, BO dominates OO when independent pricing is adopted, causing OO not to occur when γ is low.

Figure 8. (Color online) Data Broker’s Equilibrium Strategies Under Different $\beta$ and γ Values When the Data Broker Adopts Independent Pricing (α � 0:5)  
![](/api/attachments/85Q7GDAS/fulltext/images/4fcf9c8d8dcc3ec64bfbb56cd12809ef6b6506ea52503e4d9ac813c93ea6d3bb.jpg)

We find that BB also dominates OO when $\gamma$ is low. This is because the data broker can charge a higher price for collective insights in this new pricing model than it can in the baseline model. In the baseline model, when $\gamma$ is low, if the data broker charges a high price for collective insights, publishers may instead choose individual insights, given that the external data value is low, and the price of individual insights is only half that of collective insights. Therefore, the data broker can only charge a relatively low price if they want to induce both publishers to buy collective insights, leading to a low profit. As a result, the data broker finds it better to sell individual insights to both publishers when $\gamma$ is low (i.e., the OO case arises as the equilibrium). However, in the extension model, given that the prices for collective insights and individual insights are independent, the data broker can charge a high price for collective insights, while charging a relatively high price for individual insights (e.g., more than half of the collective insights price). Such pricing discourages publishers from buy ing individual insights. Therefore, in the new pricing model, the data broker can obtain a higher profit in the BB case than in the OO case, causing OO not to occur in equilibrium.

Moreover, we find that the equilibrium regions for BB and BO depend on the small publisher’s data size $\beta .$ Specifically, when $\beta$ is relatively small, BB arises as the equilibrium, whereas when $\beta$ is relatively large, BO becomes the equilibrium. The underlying intuition is that when $\beta$ is relatively large, the large publisher’s

WTP for collective insights increases because the large publisher can now obtain a higher external data value from the small publisher; at the same time, the small publisher’s incentive to buy collective insights decreases because the external data value does not change and buying collective insights would intensify the competition. Thus, the data broker benefits more by setting a high price for collective insights so that only the large publisher buys collective insights (see BO region in Figure 8).

Figure 9 illustrates the impact of α and γ on equilibrium outcomes when the data broker adopts the independent pricing model for collective insights and individual insights. We find that when γ is relatively high, OB will become the equilibrium. This is because the small publisher obtains high external data value when data externality increases. Hence, when γ is relatively high, the data broker has incentives to set a higher price for collective insights so that only the small publisher chooses to buy collective insights.

In contrast with the baseline model, when γ is relatively small, we find BO and BB always dominate OO, causing OO not to occur in equilibrium. This is because, in this independent pricing model, the prices for collective insights and individual insights are independent. When γ is relatively small, even though the data broker charges a lower price for collective insights, the price for individual insights does not have to be excessively low. Thus, this independent pricing scheme enables the data broker to extract more profit from publishers, leading to a higher profit for the data broker in the BO case than in the OO case. In the BB case, compared with the baseline model, the data broker can charge a higher price for collective insights, and also a relatively higher price for individual insights, due to the independent pricing scheme. As a result, the broker can obtain higher profits in BB than in OO, causing OO not to occur in the equilibrium.

Figure 9. (Color online) Data Broker’s Equilibrium Strategies Under Different α and γ Values When the Data Broker Adopts Independent Pricing (β � 0:4)  
![](/api/attachments/85Q7GDAS/fulltext/images/75261985df495fa22ec3a85947642b9da1169f2c6d0e76c05331a5d50e4c3cd8.jpg)

Moreover, we find that the equilibrium regions for BB and BO depend on the data analytics level. Specifically, when α is relatively small, BB becomes the equi librium, while when α is relatively large, BO arises as the equilibrium. The intuition is that when α is relatively large, the large publisher’s WTP for collective insights is relatively high. Thus, the data broker benefits more by setting prices to induce the large publisher to buy collective insights, leading to BO equilibrium (see BO region in Figure 9). When α is relatively small, BB would become the equilibrium. In this case, the data broker is better off also inducing the small publisher to buy collective insights.

## 5.2. Heterogeneous Targeting Values

In our baseline model, we assume that data insights provide homogeneous targeting value to advertisers. In practice, given advertisers’ heterogeneity, the value of data insights for improving consumer targeting may also be heterogeneous to advertisers. For instance, advertisers who sell niche products may value data insights more than those who sell mass products. In this section, we consider the scenario in which the value derived from individual insights is heterogeneous to advertisers. In this case, we can rewrite the advertisers’ utility as shown in Table 3.

Using a backward induction approach, we can derive the subgame perfect equilibrium. The detailed analytical derivation is provided in the Online Appendix B. Our results show that the equilibrium outcomes when considering heterogeneous targeting value are qualitatively the same as those in our baseline model—that is, the interactive effects of different market parameters lead to four different equilibrium strategies. Figure 10 depicts the equilibrium region for each case.

Table 3. Advertisers’ Utility in Each Subgame with Heterogeneous Targeting Value

<table><tr><td colspan="3">Advertiser utility</td></tr><tr><td>Subgame  $s_{1}s_{2}$ </td><td>Buying from Publisher 1</td><td>Buying from Publisher 2</td></tr><tr><td>OO</td><td> $U_1 = v + \alpha v - p_1$ </td><td> $U_2 = \beta v + \alpha \beta v - p_2$ </td></tr><tr><td>OB</td><td> $U_1 = v + \alpha v - p_1$ </td><td> $U_2 = \beta v + \alpha \beta v + \alpha \gamma - p_2$ </td></tr><tr><td>BO</td><td> $U_1 = v + \alpha v + \alpha \beta \gamma - p_1$ </td><td> $U_2 = \beta v + \alpha \beta v - p_2$ </td></tr><tr><td>BB</td><td> $U_1 = v + \alpha v + \alpha \beta \gamma - p_1$ </td><td> $U_2 = \beta v + \alpha \beta v + \alpha \gamma - p_2$ </td></tr></table>

Figure 10. (Color online) Data Broker’s Equilibrium Strategies When Considering Heterogeneous Targeting Value (α �0.3)  
![](/api/attachments/85Q7GDAS/fulltext/images/9cfc27d0446969bad50ac5f16ebd859fa8d12bdae61f5fbdc7f14f009c64de64.jpg)

## 5.3. Non Fully Covered Market

In this section, we relax the assumption of full market coverage to check the robustness of our key results. We consider the case where the advertiser market is not fully covered (Section 5.3.1) and the case where the publisher may not buy data insights (Section 5.3.2).

5.3.1. The Advertiser Market Is Not Fully Covered. When not all advertisers choose to buy ad impressions online, there is a segment of advertisers that chooses an outside option. Without loss of generality, we normalize the utility of the outside option for advertisers as 0. In this setting, advertisers have three options to buy ad impressions: buy from Publisher 1, buy from Publisher $^ { 2 , }$ or choose not to buy. Let $v _ { 1 } ^ { * }$ denote the advertiser who is indifferent between buying ad impressions from Publisher 2 and not buying, and let $v _ { 2 } ^ { * }$ denote the advertiser who is indifferent between buying ad impressions from Publishers 1 and 2. The above indifferent advertisers can be derived by solving $U _ { 2 } = 0$ and $U _ { 2 } = U _ { 1 }$

The publishers’ advertiser demands are given by $D _ { 1 } = 1 \stackrel { - } { - } v _ { 2 } ^ { * }$ and $D _ { 2 } = v _ { 2 } ^ { * } - v _ { 1 } ^ { * }$ , respectively. Taking the advertisers’ demand into account, we can derive the competing publishers’ optimal ad prices.

Lemma 4. When the advertiser market is not fully covered, the publishers’ equilibrium prices for each subgame are summarized as follows:

(i) in subgame OO, $\begin{array} { r } { p _ { 1 } ^ { * } = \frac { 2 ( 1 + \alpha ) ( 1 - \beta ) } { 4 - \beta } , p _ { 2 } ^ { * } = \frac { ( 1 + \alpha ) ( 1 - \beta ) \beta } { 4 - \beta } ; } \end{array}$ (ii) in subgame OB, $\begin{array} { r } { p _ { 1 } ^ { * } = \frac { 2 ( 1 + \alpha ) ( 1 - \beta ) - \alpha \gamma } { 4 - \beta } , ~ p _ { 2 } ^ { * } = } \end{array}$ $\textstyle \frac { ( 1 + \alpha ) ( 1 - \beta ) \beta + \alpha ( 2 - \beta ) \gamma } { 4 - \beta } ;$

(iii) in subgame BO, $\begin{array} { r } { p _ { 1 } ^ { * } = \frac { 2 ( 1 + \alpha ) ( 1 - \beta ) + \alpha ( 2 - \beta ) \beta \gamma } { 4 - \beta } , ~ p _ { 2 } ^ { * } = } \end{array}$ $\frac { \beta ( 1 - \beta + \alpha ( 1 - \beta - \beta \gamma ) ) } { 4 - \beta } ;$

$$
\begin{array}{c} \text {(iv) in subgame} \quad B B, \quad p _ {1} ^ {*} = \frac {(1 - \beta) (2 + \alpha (2 + (\beta - 1) \gamma))}{4 - \beta}, \quad p _ {2} ^ {*} = \\ \frac {(1 - \beta) ((1 + \alpha) \beta + \alpha (2 + \beta) \gamma)}{4 - \beta}. \end{array}
$$

By substituting the publishers’ optimal prices into their profit functions, we can obtain the competing publishers’ optimal profits under each strategy. Following a similar approach as in the baseline model, we can first derive the publishers’ decisions about purchasing data insights by comparing their profits across different cases. Anticipating the competing publishers’ decisions, the data broker decides its optimal pricing and strategy for selling data insights (shown in Figure 11).

Figure 11 shows that the equilibrium regions for different cases are similar to those in our baseline model. We find that when data externality is relatively high and the small publisher’s data size is small, the OB case arises as the equilibrium, while the BO case becomes the equilibrium outcome when data externality is relatively low and the small publisher’s data size is relatively large. When data externality is moderate and the small publisher’s data size is relatively small, the data broker would set prices so that both publishers choose to buy collective insights $( \mathrm { i . e . , }$ BB is the equilibrium). Finally, it is optimal for the data broker to sell individual insights to both publishers when data externality is low (i.e., OO occurs in the equilibrium).

Figure 11. (Color online) Data Broker’s Equilibrium Strategies When the Advertiser Market Is Not Fully Covered (α � 0.3)  
![](/api/attachments/85Q7GDAS/fulltext/images/7d6163dc5d2496ca7ae2325c1be70941f3521a2f451179f87d85ba909ec41911.jpg)

Table 4. Publishers’ Decision Matrix with Three Choices (N, O, B)

<table><tr><td>Publisher 1/Publisher 2</td><td>N</td><td>O</td><td>B</td></tr><tr><td>N</td><td>NN</td><td>NO</td><td>NB</td></tr><tr><td>O</td><td>ON</td><td>OO</td><td>OB</td></tr><tr><td>B</td><td>BN</td><td>BO</td><td>BB</td></tr></table>

5.3.2. The Publisher May Not Buy Data Insights. In our baseline model, we implicitly assume that publishers always purchase the data broker’s individual insights but strategically determine whether to purchase collective insights drawn from its competitors’ data $( \mathrm { i . e . , }$ $s _ { i } \in ( O , B ) )$ . While this is a reasonable assumption given the prevalence of data analytics in targeted advertising, we relax this assumption to give the publisher the option of not buying any insights from the data broker (denoted by N). Thus, in this setting, each publisher has three choices in Stage $2 ( \mathrm { i . e . , ~ } s _ { i } \bar { \in } ( N , \bar { O , ~ } B ) )$ . Table 4 summarizes the publishers’ decision matrix. In total, there are nine possible strategy profiles.

We can derive the data broker’s optimal pricing using the same analytical procedure as in the baseline model. The analytical derivation is delegated to the Online Appendix B. Figure 12 shows the equilibrium regions for the different cases. When incorporating the publisher’s outside option (i.e., N), we show that the OO case is dominated by the ON case. This implies that the data broker should set prices so that only the large publisher buys individual insights while the small publisher does not buy any insights. This is because the large publisher has more data, which means that buying individual insights would provide the large publisher with more value relative to the small publisher. Consequently, selling only to the large publisher allows the data broker to charge a higher price, as the large publisher’s WTP is higher than that of the small publisher. This, in turn, results in a higher profit for the data broker, compared with selling individual insights to both publishers.

Figure 12. (Color online) Data Broker’s Equilibrium Strategies When the Publisher May Not Buy Data Insights (α � 0:2)  
![](/api/attachments/85Q7GDAS/fulltext/images/58c517c1db4cdeee43b5482e7a3354d8471dea019cff35672e0f2ac6e9d20d07.jpg)

In addition, compared with the baseline model, we find that when data externality $( \gamma )$ is sufficiently high, the NB case dominates the OB case. This suggests that the data broker sets its prices to encourage only the small publisher to buy collective insights, while the large publisher does not buy any insights (see NB region in Figure 12). If the data broker wants to induce the large publisher to buy individual insights and the small publisher to buy collective insights (i.e., OB), the data broker has to charge relatively low prices for individual insights and collective insights. This is because the large publisher has a relatively low WTP for individual insights when $\gamma$ is sufficiently high. The purchase of collective insights by the large publisher may reduce publisher differentiation and intensify competi tion, given that the publishers’ value differentiation is lower in the OB case than in the NB case. Therefore, OB would result in a lower profit for the data broker. As a result, compared with the OB case, the data broker is better off charging a high price for collective insights so that only the small publisher chooses to buy collective insights while the large publisher does not buy any insights.

Furthermore, our analysis shows that the BO case is dominated by BN when the small publisher’s data size $( \beta )$ is relatively large. The underlying intuition is that when $\beta$ is large, the value differentiation between pub lishers is low. Thus, the small publisher has less incentive to buy data insights from the data broker, as doing so would intensify the competition with the large publisher. Consequently, to induce the small publisher to buy data insights, the data broker has to set a low price for individual insights and a relatively low price for col lective insights. This is not optimal for the data broker. As a result, the data broker would choose to set its prices so that only the large publisher buys collective insights, and the small publisher chooses not to buy any insights (see BN region in Figure 12). Finally, similar to the baseline model, the BB case arises as the equilibrium when both the small publisher’s data size and data externality are moderate. In this case, the data broker sells collective insights to both publishers to meet their demand and enhance their values while charging a moderate price.

To summarize, when considering the scenario in which the publisher has an outside option, our baseline model’s key insight—that the data broker may not always want to sell collective insights to every interested party—still holds. More importantly, the underlying mechanisms that drive different equilibrium outcomes are similar to those of the baseline model. In particular, selling collective insights exclusively to one publisher, while making information scarcer for the other (i.e., selling no insights), may mitigate the downstream competition and significantly increase one publisher’s competitive advantage. As a result, the data broker can charge one publisher a higher price, thereby obtaining higher profits by reducing competition in the downstream market.

## 5.4. Advertiser Multihoming

In the baseline model, we follow the prior literature (Gal-Or et al. 2018, Chatterjee and Zhou 2021) and assume that advertisers choose to buy ad impressions from only one publisher (i.e., singlehoming). In this section, we consider the case where advertisers may choose to deliver ads through both publishers $( \mathrm { i . e . , }$ multihoming) and examine how such behavior may affect our key results.

When advertisers consider displaying ads through both publishers, they do not compare the utility that they gain from each publisher. Instead, they evaluate whether a given publisher can provide a positive utility, regardless of the utility offered by the competing publisher (Bakos and Halaburda 2020). This implies that publishers do not compete head-to-head to attract each advertiser. Therefore, advertisers choose to display ads on publisher i if $U _ { i } > 0 ,$ and choose to multihome when both $U _ { 1 } > 0$ and $U _ { 2 } > 0$ . Figure 13 illustrates advertisers’ homing decisions when multihoming is possible.

As shown by Figure 13, advertisers with $v \in \left[ \tilde { v _ { 2 } } , \tilde { v _ { 1 } } \right]$ choose to advertise only through Publisher 2, while advertisers with $v \in [ \tilde { v _ { 1 } } , 1 ]$ choose to multihome with both Publisher 1 and Publisher $^ { 2 , }$ where $\tilde { v _ { 2 } }$ is characterized by $U _ { 2 } = 0$ and $\tilde { v _ { 1 } }$ is characterized by $U _ { 1 } = 0 .$ . Note that when $\tilde { v _ { 1 } } > 0$ and $\tilde { v _ { 2 } } > 0$ , we can obtain the inner solution for the publishers’ optimal prices, in which each publisher only serves a portion of advertisers. When $\tilde { v _ { 2 } } \leq 0 \mathrm { o r } \tilde { v _ { 1 } } \leq 0 .$ , we can derive the corner solution for the publishers’ optimal prices, in which Publisher 2 or Publisher 1 sets prices so that all advertisers buy ads from them.

Based on the different advertiser market segmentations, we can derive the publishers’ equilibrium prices in each case. Specifically, following the same analytical procedure used in the baseline model, we first obtain the publishers’ optimal ad prices (including the inner solution and corner solution). Then, we derive the pub lishers’ purchasing decisions for data insights by comparing the profits that publishers gain from each case. Anticipating the competing publishers’ decisions, the data broker determines its optimal pricing decisions. The analytical derivation can be found in the Online Appendix B. Figure 14 illustrates the equilibrium outcomes for the data broker.

Figure 14. (Color online) Data Broker’s Equilibrium Strategies When Advertiser Can Multihome (α � 0.25)  
![](/api/attachments/85Q7GDAS/fulltext/images/00559814925609e04f2503db7691492f03d7f4c00f2cc622fd6cde1e86787076.jpg)

Our analysis shows that when data externality is relatively low, that is, $\begin{array} { r } { \gamma < \gamma _ { m } = \frac { ( 1 - \alpha ) \beta } { \alpha } . } \end{array}$ , both publishers set optimal prices so that the advertiser market is partially covered (i.e., only a portion of advertisers choose to buy ads from them). Otherwise, when γ is relatively high, in the OB, BB, and BO cases, publishers may set prices so that the advertiser market is fully covered (i.e., all advertisers buy ads from them). When γ is relatively high, advertisers can obtain a relatively high utility in the OB, BB, and BO cases because they can gain a high external data value when buying collective insights; this enables publishers to charge a relatively high ad price while serving all advertisers. We derive the publisher’s pricing and profit for the OB, BB, BO, and OO cases, respectively, by considering scenarios where the advertiser market is fully or partially covered. We then derive the data broker’s optimal selling strategy for the data insights.

Figure 13. (Color online) Advertisers’ Homing Decisions When Multihoming Is Possible

<table><tr><td>0</td><td> $\widetilde{v_2}$ </td><td> $\widetilde{v_1}$ </td><td>1</td></tr></table>

The result shows that when advertisers multihome, BO does not occur in equilibrium. This means that the data broker does not benefit by offering prices so that only the large publisher buys collective insights. In contrast, we find that the data broker has more incentive to offer prices that encourage only the small publisher to buy collective insights (see OB region in Figure 14). When $\gamma < \gamma _ { m } ,$ the advertiser market is partially served by two publishers, while when $\gamma > \gamma _ { m } ,$ the advertiser market is fully covered. Notably, OB equilibrium can occur in both scenarios.

When advertisers multihome, publishers no longer compete for advertisers (i.e., advertisers do not compare two publishers’ utilities). Hence, the competition effect shown in the baseline model disappears. This implies that each publisher’s WTP for data insights does not depend on their competitor’s choice; instead, it depends on how data insights can improve the publisher’s data value for targeting (i.e., value-enhancing effect). Given that the small publisher can obtain more additional value when buying collective insights, its WTP for collective insights is higher than that of the large publisher. Hence, the BO case where only the large publisher buys collective insights does not emerge as the equilibrium. In other words, it is more profitable for the data broker to sell collective insights to both publishers than to sell exclusively to the large publisher, that is, BB dominates BO.

Furthermore, when data externality (γ) is high and the small publisher’s data size (β) is large, we find that BB arises as the equilibrium outcome. This is because when β is large, the large publisher’s WTP for collective insights increases. Therefore, it is optimal for the data broker to charge a relatively high price while selling collective insights to both publishers. Finally, we show that when data externality is relatively low, OO arises as the equilibrium; in this case, because γ is low, both publishers have a weaker incentive to buy collective insights.

## 6. Discussion and Conclusion

In this study, we develop an analytical model to analyze the strategic interactions between a data broker, two competing publishers, and advertisers. We investigate the data broker’s data insights pricing strategies and their impact on downstream market competition.

## 6.1. Theoretical Contributions

Our study contributes to three main areas of the literature. First, with the increased availability of data, there is a growing body of literature on online data markets, which has primarily focused on data brokers’ optimal data pricing strategies (Bimpikis et al. 2019, Montes et al. 2019). However, this line of literature has not considered the characteristics of data brokers, such as their capabil ity to generate insights from the data and their ability to dictate how different types of data insights are sold to competing publishers. We explicitly model data brokers’ analytics capability. Specifically, we examine how this capability interacts with other factors, such as data externality, to influence the data broker’s optimal data strategies, and we evaluate their subsequent impact on downstream market competition. We show that as a data broker’s data analytics capabilities increase, the data broker may strategically sell collective insights exclusively to the dominant downstream firm, thereby softening downstream competition.

Second, we contribute to the literature on the economic impact of data analytics. Most studies on data analytics focus on its business value, and some have shown that firms can reap more benefits when data analytics capabilities increase (Tambe 2014, Muller¨ et al. 2018, Wu et al. 2020). However, we show that data analytics has a nonmonotonic impact on the data broker’s price and advertiser surplus, both of which may first increase and then decrease as the data analytics capability improves. The reason is that data analytics capability directly affects targeting value and indirectly affects publisher competition. As a data broker’s data analytics capability improves, the broker tends to sell exclusively to the large publisher, creating both value-enhancing and competition-mitigation effects. Our findings formalize the intuitions reported by the FTC (2016), which highlight both the potential efficiency gains (i.e., the targeting value considered in this study) and the possible downsides of big data analytics (i.e., the exclusive data deal considered in this study).

Finally, we contribute to the online advertising literature, which has mainly focused on the interactions between publishers and advertisers (Chen and Stallaert 2014, Gal-Or et al. 2018). This literature has largely ignored the role of data brokers in online advertising. We show that data brokers can strategically impact the competitive landscape of the downstream publisher market through their control of data insights. In addition, we demonstrate how the data broker may influence advertiser surplus and aggregate welfare outcomes in the online advertising ecosystem through different pricing decisions for data insights. Therefore, this study advances the understanding of the strategic impact of data in the targeted advertising industry.

## 6.2. Managerial and Policy Implications

Our results offer several practical implications for managers and policymakers. In particular, we shed light on the market conditions that influence data brokers’ optimal strategies for selling data insights. Our analysis reveals that the interplay of two key factors, which have the potential to influence brokers’ ability to generate insights from data, may result in opposite outcomes. A high data externality motivates the data broker to sell more insights to small firms, whereas a higher level of data analytics encourages the broker to sell more insights to large firms. Both encourage exclusive selling of collective insights, in which data brokers set prices so that only one publisher is incentivized to purchase collective insights.

These findings imply that when the data from two publishers are naturally synergistic or superadditive (i.e., high data externality), the sharing of data can significantly benefit the small firm, motivating the data broker to exploit its surplus. However, when the collective data are subadditive, a data broker with a strong data analytics capability can take advantage of the large firm’s data value. When the data broker cannot fully exploit the individual publisher—that is, when both data externality and the data analytics capability are at a moderate level—it is more advantageous for the data broker to sell collective insights nonexclusively to both downstream publishers. Finally, when the data analytics capability is low and the collective data are considerably subadditive, the data broker should sell individual insights to both publishers.

This study focuses on the interactions between data brokers and publishers in the context of targeted advertising. However, our findings also apply to similar business settings that involve interactions between data brokers and downstream firms. For instance, in e-commerce, retail platforms such as Amazon and Alibaba can be regarded as data brokers that collect a large amount of consumer data from sellers (Bergemann and Bonatti 2019). Our findings thus provide insights into how retail platforms should devise their data-provisioning strategies; in particular, platforms should consider competition intensity between sellers, the synergy of the data at hand, and their data analytics capability.

Finally, many digital companies, such as Facebook and Google, use consumer data exclusively to establish a competitive advantage and build market power; such practices create anticompetitive effects and a “data barrier to entry” (Campbell et al. 2015). Notably, our findings show that data brokers may reduce the market dominance of firms with large data repositories and may even level the playing field for other market participants (e.g., small publishers). From this perspective, our findings support the recommendation of Martens et al. (2020) that governments should create a more conducive policy environment for third-party data owners (e.g., data brokers) to operate in the data market. The findings also support the latest data strategy viewpoint put forward by the European Commission, which states that the value of data might not be realized when insufficient data are shared in the industry (Preez 2022). This scenario promotes an unfair playing field in the market, with a large amount of data available to only a limited number of participants (OECD 2019).

## 6.3. Limitations and Future Research

In this section, we discuss some limitations of our study and suggest several avenues for future research. First, in our setting, we consider a monopoly data broker that plays the role of market leader. This assumption is reasonable because the data broker has access to more data and can decide how to sell it optimally (Montes et al. 2019). Nevertheless, as the data broker industry evolves, more brokers are entering the market and competing for downstream publishers. Therefore, it would be interesting for future studies to explore how competition between data brokers affects the strategic interactions between publishers and advertisers. Second, we consider the data broker’s data analytics capabilities to be exogenous. This assumption is realistic since the level of data analytics is often constrained by the industrial technology level (Koh et al. 2017). However, due to the potential benefits of data analytics, firms are eager to invest in data analytics technology. Thus, it would be worthwhile to extend the current study to endogenize the data analytics capability and explore the data broker’s optimal investment level in this capability. By doing so, we could generate new insights into the interplay between data brokers’ data analytics investment decisions and data selling strategies, as well as these factors’ subsequent impact on downstream market competition.

## Acknowledgments

The authors thank the senior editor, associate editor, and anonymous reviewers for their constructive feedback throughout the review process. The authors also thank Lihong Cheng for her feedback and suggestions on the early version of the work.

## Endnotes

<sup>1</sup> See https://www.forbes.com/sites/forbespr/2016/08/04/forbesmedia-selects-oracle-marketing-cloud-to-increase-advertising-revenue/ ?sh=785767712be1.

<sup>2</sup> See https://onaudience.com/data-management-platform-pricingand-buyers-guide#DMPpricing.

<sup>3</sup> See https://www.lotame.com/dmp-case-study-new-york-dailynews/.

<sup>4</sup> See https://onaudience.com/data-management-platform-pricingand-buyers-guide#DMPcomparison.

<sup>5</sup> Here, collective insights can also be understood as a bundle of individual insights and competitive insights. We assume that the price for each type of insight is the same (i.e., w), so the price of collective insights equals 2w.

<sup>7</sup> We proxy the publishers’ daily traffic as the amount of data they have.

<sup>8</sup> In the baseline model, we assume publishers derive sufficient large value (e.g., v) from data insights such that they always choose to buy insights. In the model extension (Section 5.3.2), we consider the scenario where publishers may not buy insights from the data broker.

<sup>9</sup> Note that publishers charge different prices in different cases. To simplify the notation, we use a generic notation p to denote publish ers’ prices in different cases.

<sup>10</sup> To ensure complete market coverage, we assume advertisers obtain a sufficient large basic value (e.g., v) from publishers, so that all advertisers’ utility is nonnegative and they find it optimal to purchase ads.

<sup>11</sup> Note that in the case $w _ { 4 } < w _ { 3 } < w _ { 2 } < w _ { 1 }$ , both OB and BO can be the equilibrium when $w _ { 3 } < w < w _ { 2 } ;$ we select OB as the main equilibrium of interest for clarity in exposition. Likewise, in the case $w _ { 3 } < w _ { 4 } < w _ { 1 } < w _ { 2 } ,$ both $B \bar { O }$ and OB can be the equilibrium when $w _ { 4 } < w < w _ { 1 } ;$ we select BO as the main equilibrium of interest for clar ity in exposition.

<sup>12</sup> See https://www.europarl.europa.eu/news/en/headlines/society/ 20220331STO26411/boosting-data-sharing-in-the-eu-what-arethe-benefits.

## References

Acemoglu D, Makhdoumi A, Malekian A, Ozdaglar A (2022) Too much data: Prices and inefficiencies in data markets. Amer. Econom. J. Microeconomics 14(4):218–256.

Aquino J (2014) Forbes’ Mark Howard talks programmatic trends, native ads and why it’s business as usual. Accessed March 24, 2024, https://www.adexchanger.com/publishers/forbes-mark-howardtalks-programmatic-trends-native-ads-and-why-its-business-asusual/.

Athey S, Gans JS (2010) The impact of targeting technology on advertising markets and media competition. Amer. Econom. Rev. 100(2): 608–613.

Bakos Y, Halaburda H (2020) Platform competition with multihoming on both sides: Subsidize or not? Management Sci. 66(12):5599–5607.

Banaszczyk P, Chmielewski T (2023) Data management platforms (DMPs) and data usage. Accessed March 24, 2024, https:// adtechbook.clearcode.cc/dmp-and-data-usage/.

Belleflamme P, Lam WMW, Vergote W (2020) Competitive imperfect price discrimination and market power. Marketing Sci. 39(5): 996-1015.

Bergemann D, Bonatti A (2011) Targeting in advertising markets: Implications for offline versus online media. RAND J. Econom. 42(3):417-443.

Bergemann D, Bonatti A (2019) Markets for information: An introduc Annual Rev. Econom.

Bimpikis K, Crapis D, Tahbaz-Salehi A (2019) Information sale and competition. Management Sci. 65(6):2646–2664.

Bourreau M, De Streel A, Graef I (2017) Big data and competition pol icy: Market power, personalised pricing and advertising. Preprint, submitted February 16, https://dx.doi.org/10.2139/ssrn. 2920301.

Braulin FC, Valletti T (2016) Selling customer information to competing firms. Econom. Lett. 149:10–14.

Campbell J, Goldfarb A, Tucker C (2015) Privacy regulation and mar ket structure. J. Econom. Management Strategy 24(1):47–73.

Chatterjee P, Zhou B (2021) Sponsored content advertising in a two sided market. Management Sci. 67(12):7560–7574.

Chen J, Stallaert J (2014) An economic analysis of online advertising using behavioral targeting. MIS Quart. 38(2):429–449.

Chen Y, Li X, Sun M (2017) Competitive mobile geo targeting. Market ing Sci. 36(5):666–682.

Chen Y, Joshi YV, Raju JS, Zhang ZJ (2009) A theory of combativ advertising. Marketing Sci. 28(1):1–19.

Choi JP, Jeon DS, Kim BC (2019) Privacy and personal data collection with information externalities. J. Public Econom. 173:113–124

Davies J (2016) German publishers are pooling data to compete with Google and Facebook. Accessed March 24, 2024, https://digiday.com media/german-publishers-pool-data-compete-google-facebook/.

Desai PS, Purohit D, Zhou B (2016) The strategic role of exchange promotions. Marketing Sci. 35(1):93–112.

Federal Trade Commission (FTC) (2016) Big data: A tool for inclusion or exclusion? Understanding the issues. Report, FTC, Washington, DC.

Gal-Or E, Gal-Or R, Penmetsa N (2018) The role of user privacy concerns in shaping competition among platforms. Inform. Systems Res, 29(3):698–722

Goldfarb A, Tucker C (2011) Online display advertising: Targeting and obtrusiveness. Marketing Sci. 30(3):389–404.

Gu Y, Madio L, Reggiani C (2022) Data brokers co-opetition. Oxf. Econom. Pap. 74(3):820–839.

Ichihashi S (2021) The economics of data externalities. J. Econom. Theory 196:105316.

Katz ML (2019) Multisided platforms, big data, and a little antitrust policy. Rev. Ind. Organ. 54(4):695–716.

Kingham E, Carbonell M (2016) Forbes media selects oracle marketing cloud to increase advertising revenue. Accessed March 24, 2024, https://www.forbes.com/sites/forbespr/2016/08/04/forbesmedia-selects-oracle-marketing-cloud-to-increase-advertising revenue/?sh=a9edb4f2be13

Koh B, Raghunathan S, Nault BR (2017) Is voluntary profiling welfar enhancing? MIS Quart. 41(1):23–41.

Koski H (2018) How do competition policy and data brokers shape product market competition? ETLA Working Papers, No. 61, The Research Institute of the Finnish Economy (ETLA), Helsinki, Finland.

Leetaru K (2018) What does it mean for social media platforms to “sell” our data? Accessed March 24, 2024, https://www.forbes. com/sites/kalevleetaru/2018/12/15/what-does-it-mean-for social-media-platforms-to-sell-our-data/?sh=3f156342d6c4

MacCarthy M (2010) New directions in privacy: Disclosure, unfair ness and externalities. ISJLP 6:425.

Martens B, De Streel A, Graef I, Tombal T, Duch-Brown N (2020) Business-to-business data sharing: An economic and legal analysis. JRC Digital Economy Working Paper, No. 2020-05, European Commission, Joint Research Centre (JRC), Seville, Spain

Maximize Market Research (MMR) (2023) Data broker market: Global industry analysis and forecast (2024-2030). Accessed March 25, 2024, https://www.maximizemarketresearch.com/ market-report/global-data-broker-market/55670/.

Mehta S, Dawande M, Janakiraman G, Mookerjee V (2021) How to sell a data set? Pricing policies for data monetization. Inform. Systems Res. 32(4):1281–1297.

Melendez S, Pasternack A (2019) Here are data brokers quietly buying and selling your personal information. Accessed March 24, 2024 https://www.fastcompany.com/90310803/here-are-the-databrokers-quietly-buying-and-selling-your-personal-information.

Montes R, Sand-Zantman W, Valletti T (2019) The value of personal information in online markets with endogenous privacy. Management Sci. 65(3):1342–1362.

Moore S (2016) How to choose a data broker. Accessed March 23 2024, https://www.gartner.com/smarterwithgartner/howto-choose-a-data-broker

Mu¨ ller O, Fay M, Vom Brocke J (2018) The effect of big data and ana lytics on firm performance: An econometric analysis considering industry characteristics. J. Management Inform. Systems 35(2): 488–509.

OECD (2019) Enhancing Access to and Sharing of Data: Reconciling Risks and Benefits for Data Re-use across Societies (OECD Publishing, Paris).

Preez D (2022) EU Data Act – Unlocking the value of industrial data in Europe. Accessed March 24, 2024, https://diginomica.com/eu data-act-unlocking-value-industrial-data-europe.

Ray J, Menon S, Mookerjee V (2020) Bargaining over data: When does making the buyer more informed help? Inform. Systems Res. 31(1):1–15.

Richter H, Slowinski PR (2019) The data sharing economy: On the emergence of new intermediaries. IIC-Internat. Rev. Intellectual Property Competition Law 50(1):4–29.

Tambe P (2014) Big data investment, skills, and firm value. Manage ment Sci. 60(6):1452–1469.

Todri V, Ghose A, Singh PV (2020) Tradeoffs in online advertising: Advertising effectiveness and annoyance dynamics across the purchase funnel. Inform. Systems Res. 31(1):102–125.

Weibl J, Hess T (2020) Turning data into value–exploring the role of synergy in leveraging value among data. Inform. Systems Manage ment 37(3):227–239.

Wu L, Hitt L, Lou B (2020) Data analytics, innovation, and firm productivity. Management Sci. 66(5):2017–2039.

Zhang X, Zhang R, Yue WT, Yu Y (2019) What is your data strategy? The strategic interactions in data-driven advertising. Proc. 40th Internat. Conf. Inform. Systems (Association for Information Sys tems, Atlanta), 1–9.

C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pera</sub>ti<sub>ons</sub> R<sub>esearc</sub>h & th<sub>e</sub> M<sub>anagemen</sub>t S<sub>c</sub>i<sub>ences an</sub>d it<sub>s con</sub>t<sub>en</sub>t <sub>may no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or</sub> <sub>ema</sub>il<sub>e</sub>d t<sub>o</sub> <sub>mu</sub>lti<sub>p</sub>l<sub>e</sub> <sub>s</sub>it<sub>es</sub> <sub>or</sub> <sub>pos</sub>t<sub>e</sub>d t<sub>o</sub> <sub>a</sub> li<sub>s</sub>t<sub>serv</sub> <sub>w</sub>ith<sub>ou</sub>t th<sub>e</sub> <sub>copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup> <sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use.</sub>
