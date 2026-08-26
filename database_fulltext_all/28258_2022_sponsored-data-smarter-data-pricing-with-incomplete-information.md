---
otero_id: 28258
otero_key: "7FVC344N"
title: "Sponsored Data: Smarter Data Pricing with Incomplete Information"
authors: "Xiaowei Mei; Hsing Kenneth Cheng; Subhajyoti Bandyopadhyay; Liangfei Qiu; Lai Wei"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1063"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sponsored Data: Smarter Data Pricing with Incomplete Information

Xiaowei Mei,<sup>a</sup> Hsing Kenneth Cheng,<sup>b</sup> Subhajyoti Bandyopadhyay,<sup>b</sup> Liangfei Qiu,<sup>b</sup> Lai Wei<sup>c,</sup>\*

<sup>a</sup>Department of Management and Marketing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong; <sup>b</sup>Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>c</sup> Anta College of Economics and Management, Shanghai Jiao Tong University, Shanghai 200030, China

Contact michael.mei@polyu.edu.hk, https://orcid.org/0000-0002-1719-7394 (XM); hkcheng@u<sup>fl</sup>.edu, <sup>:</sup>https://orcid.org/0000-0001-5787-0777 (HKC); shubho@u<sup>fl</sup>.edu, https://orcid.org/0000-0003-1962-6962 (SB); liangfei.qiu@warrington u<sup>fl</sup>.edu, https://orcid.org/0000-0002-8771-9389 (LQ); laiwei@sjtu.edu.cn, https://orcid.org/0000-0003-2083-1752 (LW)

Received : February 15, 2020<sub>Revised:</sub> Nove Accepted <sup>: August 10, 2021</sup>Published Online in Articles in Advance: November 11, 2021

https://doi.org/10.1287/isre.2021.1063

Copyright:

Abstract. With the upcoming next-generation 5G networks, mobile network operators (MNOs, such as AT&T, T-Mobile, and Verizon) are investigating new business models that encourage content providers (such as Net<sup>fl</sup>ix and Spotify) to sponsor data for consumers. Sponsored data allow customers to browse, stream, and enjoy content from their data sponsors without impacting their monthly data plan allowance. We analyze this recent phenomenon using an incomplete information game-theoretical model, where the MNO does not observe consumers’ types (personal valuation of mobile data) and provides multiple data plans to consumers. We <sup>fi</sup>nd that the impact of sponsored data on consumer surplus crucially depends on whether the MNO has complete information over consumer types: Under complete information, sponsored data do not improve consumer surplus. However, under incomplete information, sponsored data increase consumer surplus. Our analysis also show that under incomplete information, the MNO should allow sponsored data in a wider range of market conditions than those under complete information. Our study suggests that prior literature tends to underestimate both the long-run detrimental effect of sponsored data on content diversity and the short-run bene<sup>fi</sup>cial effect on consumer surplus. Our <sup>fi</sup>ndings offer important managerial implications for the MNO, who is interested in optimizing the data plans, and for policymakers who regulate the wireless internet market.

History: Yong Tan, Senior Editor; Zhengrui Jiang, Associate Editor.

Funding: X. Mei received <sup>fi</sup>nancial support from the Hong Kong Polytechnic University Start-up Fund [Project ID P0000234]. L. Wei received <sup>fi</sup>nancial support from the National Science Foundation of China [Grants 72122013, 71831006, and 71801151].

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2021.1063.

Keywords: sponsored data <sub>•</sub> wireless internet <sub>•</sub> game theory <sub>•</sub> incomplete information <sub>•</sub> consumer surplus

## 1. Introduction

Explosive growth in mobile data consumption has been witnessed with the development of dataintensive internet services during the last couple of years. According to Ericsson, the monthly data traf<sup>fi</sup>c on smartphones in North America has been increasing at the rate of almost 40% since the end of 2015, reaching 25 gigabytes per month per active smartphone by 2022, with other regions catching up.<sup>1</sup> Cisco’s Visual Network Indexing forecasts that smartphones will account for 44% of total web traf<sup>fi</sup>c by 2022, up from 18% in 2017 (Cisco 2019). Besides data-intensive content, factors that drive usage include an increase in Long Term Evolution subscriptions, improved device capabilities, and more attractive data plans. With the upcoming next-generation 5G networks that possess more capacity and are able to accommodate more people, our mobile phones will handle data even more massively.

Mobile network operators (MNOs), such as AT&T, T-Mobile, and Verizon, would like this trend to continue because they stand to bene<sup>fi</sup>t from high revenue due to high demand. More and more content is produced by innovative content providers (CPs), such as Net<sup>fl</sup>ix and Spotify, in creative ways (Li et al. 2020). Although enjoying various digital content provided by CPs, consumers, however, are becoming more conscious about their data consumption because their monthly caps of mobile data plans can be easily exhausted by digital content, such as high-de<sup>fi</sup>nition videos and virtual reality or augmented reality games. To resolve consumers’ anxiety of running out of data quotas, the MNOs have proposed a new business model to subsidize consumers by transferring at least part of the data bills from consumers to CPs. However, research into this area is in a nascent stage and many critical elements of this business model are not thoroughly examined. This work attempts to address this research gap.

## 1.1. Motivations

In their 2014 Developer Summit, the executives of AT&T introduced “Sponsored Data,” which allows customers to browse, stream, and enjoy content from their data sponsors without impacting their monthly data plan allowance. This new monetization mechanism was quickly embraced by the industry, with 10 companies signed up with AT&T one year after their proposal.<sup>2</sup> T-Mobile started offering its customers free streaming music from top providers, including Spotify, Pandora, and iTunes Radio, since 2014 (Gryta 2014). In November 2015, free streaming video was provided through a new service called “Binge On,” which cooperates with 42 providers—Net<sup>fl</sup>ix, Amazon, Hulu, HBO, among others (Gryta and Knutson 2015). In early 2016, Verizon introduced its sponsored data service FreeBee Data. A black-and-white bee appears next to sponsored content, so customers know that clicking on that content does not incur data charges.<sup>3</sup>

Although sponsored data are adopted as a new business model by most major U.S. carriers and applauded by consumers, such a business model has been criticized by advocators of net neutrality (Cheng et al. 2011, Economides and Hermalin 2012), who contend that small businesses and developers are put at a distinct disadvantage to their deeper-pocketed competitors who can make their content more easily accessible by paying to exempt their traf<sup>fi</sup>c from consumers’ monthly bills. They are also concerned that the mobile network operators could also pick winners and losers online using their position as a gatekeeper, which would distort competition and hurt innovations on the internet in the long run.

The mobile network operators, however, argue that this new business model does not violate the principle of net neutrality because sponsored data are transmitted without priority over nonsponsored data. Others claim that this new monetization mechanism by carriers like AT&T is actually double-dipping, or twosided billing, which places more burden on content providers because an additional cost is incurred just to get their content delivered to customers.<sup>4</sup> Another concern of this new business model is that people who rely on sponsored data may never have access to the “real” internet once they are satis<sup>fi</sup>ed with free access to a walled garden of chosen services.<sup>5</sup> One example of the reaction to this concern is India’s blockage of Facebook’s Free Basics Internet, which provides free content, such as selected local news and the BBC, to people who do not have access to the internet.<sup>6</sup>

We analyze this new business model of the telecommunication industry, whereby the MNO is encouraging CPs to subsidize consumers by providing sponsored data within an incomplete-information game theoretical framework. In particular, we focus on an incompleteinformation model in which the MNO does not observe consumers’ types (personal valuation of mobile data), which is a realistic scenario in practice and provides multiple data plans to consumers.

## 1.2. Contributions

We derive the optimal data plans for a monopolist MNO under different cases where one or both of the competing CPs are allowed to participate in sponsored data. We <sup>fi</sup>nd that the impact of sponsored data on consumer surplus crucially depends on whether the MNO can perfectly observe consumer types. When the MNO can perfectly observe consumer types (complete information), sponsored data does not improve consumer surplus. However, when the MNO cannot perfectly observe consumer types (incomplete information), sponsored data increases consumer surplus. Our analysis also shows that under incomplete information, the MNO should allow sponsored data in a wider range of market conditions than those under complete information.

The key intuition is that when information is complete, the MNO is able to extract the value of sponsored data fully. However, when information is incomplete, consumers can bene<sup>fi</sup>t from their information rent reinforced by sponsored data. This result sheds light on the recent policy debate on the impact of sponsored data on consumer surplus. The MNOs, such as AT&T, insisted that sponsored data bene<sup>fi</sup>t consumers because it allows users to consume data for free and help them save money: “AT&T’s sponsored data service is aimed solely at bene<sup>fi</sup>ting our customers.”<sup>7</sup> However, some digital rights groups claimed that sponsored data does not bene<sup>fi</sup>t consumers: “While sponsored data will be pitched as a way to save customers money, it’s really just double charging.”<sup>8</sup> Our analytical result provides a complete picture of the impact of data sponsorship on consumer surplus by reconciling these two different views in a uni<sup>fi</sup>ed framework: The effect of sponsored data on consumer surplus depends on whether the MNO has complete information over consumer types.

Our paper differs from prior literature on sponsored data (e.g., Joe-Wong et al. 2015, Cho et al. 2016, Cho et al. 2020) in the following four aspects. First, to the best of our knowledge, almost all prior models of sponsored data have focused exclusively on complete information games. The critical difference between the complete and incomplete information model is that in a complete information model, the MNO considers only the participation constraints (both types of consumers obtain nonnegative utilities) and completely ignores the incentive-compatibility constraints because the MNO perfectly observes consumer types. In contrast, in an incomplete information model, the MNO needs to design a menu of contracts that is both incentive compatible and individually rational. Our study relaxes the assumption of complete information and examines the difference between complete and incomplete information models.

Second, the previous studies (e.g., Joe-Wong et al. 2015) assume that CPs are not directly competing for consumers. However, in reality, some CPs could be in direct competition. For example, Spotify and Pandora are in <sup>fi</sup>erce competition: Pandora lost nearly eight million listeners in the <sup>fi</sup>rst three quarters of 2017.<sup>9</sup> Our model contributes to the literature on sponsored data by highlighting the impact of sponsored data on CP competition.

Third, the prior literature (e.g., Ma 2014, Zhang and Wang 2014, Joe-Wong et al. 2015) implicitly assumes that if a CP wants to sponsor data, he or she can sponsor data without the permission of the MNO. It may not be consistent with the current practice of sponsored data. In reality, the MNO decides whether to allow CPs to sponsor data. For example, T-Mobile has a sponsored data program called “Music Freedom.” According to Van Schewick (2016), although the program has grown from 7 to 40 providers, it still includes only a fraction of the more than 2,000 licensed online radio streaming CPs in the United States. Some smaller CPs had to wait 1.5 years to be included, whereas some never heard back from T-Mobile at all. So far, T-Mobile has, at least in part, focused on adding larger, more popular services <sup>fi</sup>rst. In our model, we explicitly consider that the MNO makes a decision on allowing which CPs to sponsor and the CPs choose their sponsoring level.

Finally, our study provides different and important policy implications in more realistic scenarios. Prior literature on sponsored data (e.g., Joe-Wong et al. 2015) tends to underestimate both the long-run detrimental effect of sponsored data on content diversity and the short-run bene<sup>fi</sup>cial effect on consumer surplus. Our research highlights a balanced and nuanced view on the policy implications of sponsored data: In the short run, sponsored data can increase consumer surplus. Nevertheless, in the long run, it raises an important anticompetitive concern: In the presence of sponsored data, a high-margin content provider may leverage his or her advantage in revenue generation capability to expand market share and gain monopoly power in digital content markets. The regulators and policymakers should pay close attention to the market conditions under which the introduction of sponsored data are more likely to reduce content diversity and to be anticompetitive.

## 2. Literature Review

Our research draws on two streams of literature. The <sup>fi</sup>rst research stream studies data sponsoring, that is, transferring at least part of the monthly mobile data bills from end consumers to the content providers, which is a business practice that can potentially bene <sup>fi</sup>t all parties involved. Having the data usage counted against their monthly quotas, end consumers will con sume more digital content and more revenue can be generated for the content provider and further ex tracted by the internet service provider. Andrews et al. (2013) view the interaction of end users with a content provider on an infrastructure platform built and maintained by an internet service provider as a two sided market. They <sup>fi</sup>nd that an optimal coordinating contract can be designed to maximize total system pro<sup>fi</sup>t and the additional pro<sup>fi</sup>t due to sponsoring data can be split between the content provider and the in ternet service provider in an arbitrary manner. Ma (2014) proposes to allow CPs to voluntarily subsidize the usage-based fees induced by data consumption for end users. They model the regulated subsidization competition among CPs and show that although sub sidization competition could increase the competitiveness and welfare of the internet content market, high access price might reduce the throughput of certain CPs and needs to be regulated. From CPs’ perspective, both small and large (or richer) CPs have an incentive to provide sponsored data only when the monopolis tic internet service provider cannot discriminate the charging price of CPs. The small CP may bene<sup>fi</sup>t more from the adoption of sponsored data for the short-run competition where the market shares are <sup>fi</sup>xed (Zhang and Wang 2014). From the perspective of the internet service provider, the optimal network management choice of data sponsorship crucially depends on mar ket conditions, such as the revenue rates of CPs and the <sup>fi</sup>t cost of consumers (Cho et al. 2016). Many of the previous studies (e.g., Ma 2014, Zhang and Wang 2014, Cho et al. 2016) assume a <sup>fi</sup>xed data consumption rate for all consumers. However, in our study, we capture the heterogeneous nature of users’ data con sumption rate through an incomplete information model, because the heterogeneity of data usage is widely regarded as one of the most important mobile user patterns in empirical studies (Jin et al. 2012).

The second research stream concerns uncertainty in economic transactions, particularly the information asymmetry literature in information systems (Dimoka et al. 2012, Hong et al. 2015, Lu et al. 2019, Qiu et al. 2019, Cheng et al. 2020). Many scholars have investigated decision making under uncertainty arising from asymmetric information, employing principle-agent theory (Ross 1973, Grossman and Hart 1983). Although the original form of principle-agent theory deals with the delegation of tasks by a principle to an agent, it has been applied to the context of economic transactions involving buyers and sellers for goods and services (Eisenhardt 1989). The intangible nature of online markets makes the effects of information asymmetry even more pronounced (Ghose 2009). Following this stream of research, there has been a rich body of literature focusing on two major sources of information asymmetry that consumers face in online markets: seller uncertainty and product uncertainty. Sellers typically possess more information about their products as well as their own characteristics and practices, which raises uncertainty for consumers because they cannot readily evaluate the products physically or fully monitor sellers’ behavior. Therefore, two information problems arise for consumers: adverse selection (hidden information) and moral hazard (hidden action) (Spence 1973, Arrow 1985, Milgrom and Roberts 1992). Research in online markets, thus, has been focused on reducing product uncertainty through information signals (Dimoka et al 2012, Qiu and Whinston 2017, Qiu et al. 2018, Khurana et al. 2019, Qiu et al. 2021), building trust in online sellers (Gefen et al. 2003, Pavlou 2003, Bapna et al. 2017), and moral hazard and adverse selection of sellers (Dewan and Hsu 2004, Dellarocas 2005, Ghose 2009). More recent work shows that seller and product uncertainty could be further reduced by online word of mouth through numerous review and feedback rating systems (Chen and Xie 2008, Mudambi and Schuff 2010, Kwark et al. 2014, Kwark et al. 2021, Wang et al. 2021). Extending the information asymmetry literature of information systems focusing on sellers and products, we propose consumer uncertainty (consumers’ valuation of the mobile data) as an essential element in the telecommunication market where nove business practices, such as sponsored data, have been conducted. Table 1 summarizes the comparison of previous literature with our work.

## 3. Incomplete Information Model of Sponsored Data

In our model, we assume a monopolist MNO, two competing CPs, and two types of consumers: $\Theta = \bar { \{ \theta _ { H } , \bar { \theta } _ { L } \} }$ , with $\theta _ { H } > \theta _ { L }$ , which indicates that type-H consumers have a higher valuation of mobile data than type-L consumers. The reason for assuming a monopolist MNO is due to the institutional contexts documented in Online Appendix D. First, the wireless service market in the United States is highly concentrated. The Federal Communications Commission’s (FCC) annual review of mobile industry competition found that the two largest carriers, Verizon and AT&T, controlled around 70% of the nationwide market share based on service revenues.<sup>10</sup> In many geographical markets, one cellular service provider may dominate and operate as a local monopoly. Second, al though in some geographical markets in the United States multiple MNOs exist (oligopolists), because of low churn rates, they are often de facto monopolies: the churn rate was just 0.91% for Verizon and 1.08% for $\mathrm { A T } \& \mathrm { T . } ^ { 1 1 }$ This assumption is also widely adopted in prior analytical models studying the telecommunication industry (Choi and Kim 2010; Guo et al. 2010, 2012, 2013; Cheng et al. 2011; Kramer and Wiewiorra¨ 2012; Joe-Wong et al. 2015, 2018; Guo and Easley 2016; Qiu et al. 2019). In our context, consumer types can be interpreted as the personal valuation of mobile data services. The proportion of type-L consumers is $\beta ,$ and the proportion of type-H consumers is $1 - \beta . ^ { 1 2 }$

The two CPs, G and B, create and distribute online content through the MNO’s internet facilities to consumers. To monetize their value creation activities, the CPs employ an indirect revenue model, that is, obtaining their revenue mainly from advertising and af<sup>fi</sup>liate marketing in which CPs are paid by third parties in exchange for access to consumers. The advertisement-assisted revenue model is widely adopted by CPs in reality (e.g., the basic service of YouTube, Pandora, Spotify, and Vimeo). Although the CPs could generate revenue directly from users subscriptions, licensing, usage-related fees, and con tent syndication (Gallaugher et al. 2001, Ha and Ganahl 2004), the lion’s share of their pro<sup>fi</sup>t still comes from the advertisement-assisted revenue. According to eMarketer, YouTube’s 2018 ad revenue was pegged at \$3.6 billion in the United States alone, an increase of 17.1% year-on-year, and worth around 11% of Google’s total U.S. ad revenue for the year (eMarketer 2018). In contrast, YouTube’s Premium revenue was estimated at a little under \$0.75 billion at the same time (Ramsey 2018). Following previous literature (Asdemir et al. 2012, Hu et al. 2015, Guo et al. 2019), we adopt the advertisement-assisted revenue model for the CPs. We use average revenue per user (ARPU) to measure the revenue CPs generate from per consumer following the convention from the industry. Let $r _ { G }$ and $r _ { B }$ denote the ARPU of CPs G and $B ,$ respectively. Without loss of generality, we assume $r _ { B } < r _ { G } ,$ which means that $\mathrm { C P } \ { \overset { \sim } { G } }$ (the high-margin CP) is better than CP B (the low-margin CP) in generating pro<sup>fi</sup>t. We do not explicitly model the contract between the MNO and CPs in our baseline model. The contract between the MNO and CPs is often accomplished on a case-by-case basis, and we assume that the CPs pay the same amount as an individual consumer when they sponsor data. We provide additional discussions on the possible extension of allowing the MNO to treat the CPs differently in our Online Appendix C. The results are consistent with the ones we <sup>fi</sup>nd in our baseline model.

Table 1. Comparison of Previous Literature with Our Work

<table><tr><td>Research stream</td><td>Previous literature</td><td>Our work</td></tr><tr><td rowspan="3">Sponsored data</td><td>Fixed data consumption rate for consumers (Andrews et al. 2013, Ma 2014, Zhang and Wang 2014, Cho et al. 2016)</td><td>Heterogeneous data consumption rate</td></tr><tr><td>CPs sponsor data without permission of MNO (Ma 2014, Zhang and Wang 2014, Joe-Wong et al. 2015)</td><td>MNO decides whether to allow CPs to sponsor data</td></tr><tr><td>CPs do not directly compete for consumers (Andrews et al. 2013, Joe-Wong et al. 2015)</td><td>CPs compete for consumers through sponsored data</td></tr><tr><td>Information asymmetry</td><td>Seller uncertainty and product uncertainty (Dimoka et al. 2012, Hong et al. 2015, Qiu et al. 2019)</td><td>Consumer uncertainty</td></tr></table>

The MNO is not able to observe consumer types directly. Hence, it offers a menu of contracts (two data plans) to consumers: $\{ ( q _ { H } , p _ { H } ) , ( q _ { L } , p _ { L } ) \}$ , where $q _ { H }$ and $q _ { L }$ are the data amount and $p _ { H }$ and $p _ { L }$ are the unit prices of the data plan for type-H and type-L consumers, respectively. If a consumer chooses a data plan, $( q _ { i } , p _ { i } )$ he or she can consume data amount $q _ { i }$ and needs to pay $q _ { i } \cdot p _ { i }$ in total, where $i \in \{ H , L \}$ . This setting is widely used in the literature (Hande et al. 2009, Joe-Wong et al. 2015, Cho et al. $2 0 1 6 ) . ^ { 1 3 }$ In the current practice, major MNOs, such as Verizon and AT&T, typically offer various mobile data plans for different data usage. Users can choose one of several data plans that charge different amounts. Ideally, the MNO wants to induce type-L consumers to choose plan $( q _ { L } , p _ { L } )$ and induce type-H consumers to choose plan $( q _ { H } , p _ { H } )$

Consumers’ utility over data consumption is given by $\theta _ { i } v ( q _ { i } ) - p _ { i } q _ { i }$ , where $i \in \{ H , L \}$ . Consumers’ valuation function of mobile data is denoted as v ; we assume it is strictly increasing and strictly concave, that is, $v ^ { \prime } ( \cdot ) > 0$ and $v ^ { \prime \prime } ( \cdot ) < 0$ . Notations used in our model are summarized in Table 2, and the timeline of the game is given as follows:

i. The MNO decides whether to allow CPs to sponsor consumers. There are four cases: (1) baseline case without sponsored data (the MNO does not allow either CP to sponsor); (2) only the high-margin CP G is allowed to sponsor data; (3) only the low-margin CP B is allowed to sponsor data; and (4) both CPs are allowed to sponsor data.

ii. The CPs determine the level of sponsored data, and the MNO sets a menu of contracts (data plans).

iii. Consumers decide whether to accept a data plan and which data plan they want to accept according to the utility function. They also choose one CP among the two.

Case 1. Neither of the CPs is allowed to sponsor data. In Case 1, consumers decide whether to accept a data plan and which data plan they want to accept according to the utility function: $\theta _ { i } v ( q _ { i } ) - p _ { i } q _ { i }$ . Each consumer’s taste on ${ \mathrm { C P s } } , \varepsilon ,$ is a random draw from a uniform distribution, $[ - \alpha , \alpha ]$ . The expected value of ε is zero. In the baseline case (Case 1), if $\varepsilon \ge 0$ , a consumer will choose high-margin $\mathrm { C P } \ G ; \mathrm { i f } \ \varepsilon < 0 ,$ , a consumer will choose low-margin CP B. Therefore, the market share of CP G is given by the probability (Prob) that a consumer chooses this CP, $\mathrm { i . e . , }$ Prob $\begin{array} { r } { [ \varepsilon \ge 0 ] = \frac { 1 } { \gamma } } \end{array}$ . Similarly, the market share of CP B is Prob $\begin{array} { r } { [ \varepsilon < 0 ] = \frac { 1 } { 2 } . } \end{array}$ . In other words, two content providers who provide content of the same quality share the market equally. We relax the assumption of full market coverage and CPs’ content quality being the same in the extension section.

The MNO needs to design a menu of contracts that is incentive compatible and individually rational.<sup>14</sup> A menu of contracts, $\{ ( q _ { L } , p _ { L } ) , ( q _ { H } , p _ { H } ) \}$ , is incentive compatible if a high-type consumer prefers $( q _ { H } , p _ { H } )$ to $( q _ { L } , p _ { L } )$ and a low-type consumer prefers $( q _ { L } , p _ { L } ) \mathrm { t o } ( q _ { H } , p _ { H } ) ;$

$$
\theta_ {H} v (q _ {H}) - p _ {H} q _ {H} \geq \theta_ {H} v (q _ {L}) - p _ {L} q _ {L},\tag{1}
$$

$$
\theta_ {L} v (q _ {L}) - p _ {L} q _ {L} \geq \theta_ {L} v (q _ {H}) - p _ {H} q _ {H}.\tag{2}
$$

A menu of contracts, $\{ ( q _ { L } , p _ { L } ) , ( q _ { H } , p _ { H } ) \}$ , is individually rational if both types of consumers obtain nonnegative utility (participation constraints):

$$
\theta_ {H} v (q _ {H}) - p _ {H} q _ {H} \geq 0,
$$

$$
\theta_ {L} v (q _ {L}) - p _ {L} q _ {L} \geq 0.\tag{3}
$$

(4)

The MNO’s optimization problem is to maximize his or her pro<sup>fi</sup>t subject to (s.t.) Constraints (1)–(4):

$$
\begin{array}{r l} & {\max _ {(q _ {L}, p _ {L}), (q _ {H}, p _ {H})} \beta [ p _ {L} q _ {L} - c q _ {L} ] + (1 - \beta) [ p _ {H} q _ {H} - c q _ {H} ]} \\ & {\quad \mathrm{s.t.} \theta_ {H} v (q _ {H}) - p _ {H} q _ {H} \geq \theta_ {H} v (q _ {L}) - p _ {L} q _ {L},} \\ & {\qquad \theta_ {L} v (q _ {L}) - p _ {L} q _ {L} \geq \theta_ {L} v (q _ {H}) - p _ {H} q _ {H},} \\ & {\qquad \theta_ {H} v (q _ {H}) - p _ {H} q _ {H} \geq 0,} \\ & {\qquad \theta_ {L} v (q _ {L}) - p _ {L} q _ {L} \geq 0,} \end{array}
$$

Table 2. Summary of Key Notations

<table><tr><td colspan="2">MNO&#x27;s decision variables</td></tr><tr><td> $p_{H}, p_{L}$ </td><td>Unit data prices charged to type-H and type-L consumers in MNO&#x27;s data plans</td></tr><tr><td> $q_{H}, q_{L}$ </td><td>Data amount offered to type-H and type-L consumers in MNO&#x27;s data plans</td></tr><tr><td colspan="2">Content provider&#x27;s decision variable</td></tr><tr><td> $s_{B}, s_{G}$ </td><td>Data sponsor rate chosen by low-margin CP B and high-margin CP G</td></tr><tr><td colspan="2">Other parameters</td></tr><tr><td> $\theta_{H}, \theta_{L}$ </td><td>Consumer types, type-H consumers have a higher valuation of mobile data than type-L ones, that is,  $\theta_{H} > \theta_{L}$ </td></tr><tr><td> $\beta$ </td><td>Proportion of type-L consumers</td></tr><tr><td> $\varepsilon$ </td><td>Consumer preference heterogeneity over CPs,  $\varepsilon \sim$  Uniform  $[-\alpha, \alpha]$ </td></tr><tr><td> $r_{B}, r_{G}$ </td><td>Average revenue per user for CP B and CP G,  $r_{B} < r_{G}$ </td></tr><tr><td> $v(\cdot)$ </td><td>Consumers&#x27; valuation of the content, strictly increasing and concave</td></tr><tr><td> $\phi(\cdot)$ </td><td>Inverse function of  $v'(\cdot), \phi(v'(x)) = x$ </td></tr><tr><td> $I_{G}$ </td><td>Indicator function which takes the value of one if a consumer chooses CP G and takes the value of zero if a consumer chooses CP B</td></tr><tr><td>c</td><td>Unit cost for the MNO to provide mobile data</td></tr></table>

where c is the unit cost of the MNO. In the following lemma, we show that in this optimization problem, Constraints (1) and (4) are binding and Constraints (2) and (3) are automatically satis<sup>fi</sup>ed if (1) and (4) are satis<sup>fi</sup>ed.

Lemma 1. In the MNO’s optimization problem, the incentive-compatibility constraint for low-type consumers (Constraint (2)) and the individual rationality constraint for high-type consumers (Constraint (3)) are redundant. The incentive-compatibility constraint for high-type consumers (Constraint (1)) and the individual rationality constraint for low-type consumers (Constraint (4)) are binding.

Proof. All the proofs can be found in Online Appendix A.

Therefore, the MNO’s pro<sup>fi</sup>t optimization problem reduces to

$$
\begin{array}{c} \max _ {(q _ {L}, p _ {L}), (q _ {H}, p _ {H})} \beta \big [ p _ {L} q _ {L} - c q _ {L} \big ] + (1 - \beta) \big [ p _ {H} q _ {H} - c q _ {H} \big ], \\ \text {s.t.} \theta_ {H} v (q _ {H}) - p _ {H} q _ {H} = \theta_ {H} v (q _ {L}) - p _ {L} q _ {L}, \\ \theta_ {L} v (q _ {L}) - p _ {L} q _ {L} = 0. \end{array}
$$

Substituting for the values of $p _ { H }$ and $p _ { L } .$ , the equilibrium values of $q _ { L }$ and $q _ { H }$ are determined by the following equations:

$$
\begin{array}{l} {v ^ {\prime} (q _ {H} ^ {*}) = \frac {c}{\theta_ {H}},} \\ {v ^ {\prime} (q _ {L} ^ {*}) = \frac {\beta c}{\theta_ {L} - (1 - \beta) \theta_ {H}}.} \end{array}
$$

We assume that $\phi ( \cdot )$ is the inverse function of $v ^ { \prime } ( \cdot ) \colon$ $\phi ( v ^ { \prime } ( x ) ) = x . ^ { 1 5 }$ Therefore, we can obtain the following proposition:

Proposition 1. In the baseline case of no sponsored data, the optimal menu of contracts is $\{ ( q _ { L } ^ { * } , \bar { p _ { L } } ^ { * } ) , ( q _ { H } ^ { * } , p _ { H } ^ { * } ) \}$ , where

$$
q _ {H} ^ {*} = \phi \bigg (\frac {c}{\theta_ {H}} \bigg),\tag{5}
$$

$$
q _ {L} ^ {*} = \phi \bigg (\frac {\beta c}{\theta_ {L} - (1 - \beta) \theta_ {H}} \bigg),\tag{6}
$$

and the equilibrium prices are

$$
p _ {L} ^ {*} = \frac {\theta_ {L} v (q _ {L} ^ {*})}{q _ {L} ^ {*}},\tag{7}
$$

$$
p _ {H} ^ {*} = \frac {\theta_ {H} v (q _ {H} ^ {*}) - \theta_ {H} v (q _ {L} ^ {*}) + \theta_ {L} v (q _ {L} ^ {*})}{q _ {H} ^ {*}}.\tag{8}
$$

Next, we consider consumer surplus. Because the individual rationality constraint for low-type consumers is binding, the surplus value for low-type consumers is zero. We need to consider only the positive surplus value (information rent) of high-type consumers. In the equilibrium, the surplus value of a high-type consumer is given as follows:

$$
\theta_ {H} v (q _ {H} ^ {*}) - p _ {H} ^ {*} q _ {H} ^ {*} = \theta_ {H} v (q _ {L} ^ {*}) - p _ {L} ^ {*} q _ {L} ^ {*} = \theta_ {H} v (q _ {L} ^ {*}) - \theta_ {L} v (q _ {L} ^ {*}).
$$

Therefore, in the baseline case, the consumer surplus is

$$
(1 - \beta) (\theta_ {H} - \theta_ {L}) v (q _ {L} ^ {*}).
$$

Case 2. Only high-margin CP G is allowed to sponsor data.

In the case where only CP G is allowed to sponsor data, the timeline of the game is the same as that in the baseline case without sponsored data. The MNO offers a menu of contracts to consumers: $\{ ( q _ { H } , p _ { H } ) _ { \cal A } ,$ $( q _ { L } , p _ { L } ) \}$ . Consumers that are sponsored by CP G face a price, $p _ { i } - s _ { G }$ , instead of $p _ { i } ,$ , where $s _ { G }$ is the sponsor rate chosen by CP G. If $s _ { G } = p _ { i } ,$ , it means the CP sponsors consumers fully: Consumers can consume the data for free. Note that this assumption of sponsoring data price is mathematically equivalent to that of sponsoring data quantity: In Joe-Wong et al. (2015), a CP sponsors a fraction of his or her content, $\sigma _ { G } ;$ after sponsoring data, consumers need to pay $( 1 - \sigma _ { G } ) p _ { i } q _ { i }$ if they choose CP G (before the introduction of sponsored data, consumers need to pay $p _ { i } q _ { i } )$ ). Under our assumption, consumers need to pay $( p _ { i } - s _ { G } ) q _ { i }$ if they choose CP G. It is straightforward to see that when $s _ { G } = p _ { i } \sigma _ { G }$ , consumers pay the same amount and the two formats of sponsoring data are equivalent.<sup>16</sup>

In Case 2, a consumer’s utility is

$$
\theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + s _ {G} q _ {i} \cdot \mathbf {I} _ {G},
$$

where $i \in \{ H , L \}$ and $\mathbf { I } _ { G }$ is an indicator function, which takes the value of one if a consumer chooses CP G and takes the value of zero if a consumer chooses CP B.

Similar to Case 1, consumers’ taste heterogeneity, $\varepsilon ,$ follows a uniform distribution, $[ - \alpha , \alpha ]$ . In the case of CP G sponsoring data, if $\varepsilon + s _ { G } \ge 0 ,$ , a consumer will choose CP G, if $\varepsilon + s _ { G } < 0 .$ , a consumer will choose CP B. A larger value of $s _ { G }$ makes $\varepsilon + s _ { G }$ more likely to be not less than zero. In other words, a higher level of sponsored data from $\mathrm { C P } \ G$ (a larger value of $s _ { G } )$ leads consumers more likely to choose CP G. Therefore, the probability that a consumer chooses $\mathrm { C P } G$ (the market share of CP G) is given by

$$
\operatorname{Prob} \left[ \varepsilon + s _ {G} \geq 0 \right] = \min \left\{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\}.
$$

When consumers choose their data plans, they do not know the value of ε but know that ε is a random draw from a uniform distribution $[ - \alpha , \alpha ]$ . Therefore, consumers decide which data plan they want to accept according to the following expected utility function:

$$
\begin{array}{l} \operatorname{Prob} [ \varepsilon + s _ {G} \geq 0 ] \big [ \theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + s _ {G} q _ {i} \big ] \\ \quad + \{1 - \operatorname{Prob} [ \varepsilon + s _ {G} \geq 0 ] \} \big [ \theta_ {i} v (q _ {i}) - p _ {i} q _ {i} \big ] \\ = \theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + \min \bigg \{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \bigg \} s _ {G} q _ {i}, \end{array}
$$

where $i \in \{ H , L \}$ . The MNO’s pro<sup>fi</sup>t optimization problem is

$$
\begin{array}{c} \max _ {(q _ {L}, p _ {L}), (q _ {H}, p _ {H})} \beta [ p _ {L} q _ {L} - c q _ {L} ] + (1 - \beta) [ p _ {H} q _ {H} - c q _ {H} ] \\ s. t. \theta_ {H} v (q _ {H}) - p _ {H} q _ {H} + \min \bigg \{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \bigg \} s _ {G} q _ {H} \\ = \theta_ {H} v (q _ {L}) - p _ {L} q _ {L} + \min \bigg \{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \bigg \} s _ {G} q _ {L}, \end{array}\tag{9}
$$

$$
\theta_ {L} v (q _ {L}) - p _ {L} q _ {L} + \min \left\{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\} s _ {G} q _ {L} = 0,\tag{10}
$$

where Equation (9) is the incentive-compatibility constraint for high-type consumers and Equation (10) is the individual rationality (participation) constraint for low-type consumers. Solving MNO’s pro<sup>fi</sup>t optimization problem, we can obtain the following proposition:

Proposition 2. In the case where only high-margin $C P G$ is allowed to sponsor data, the optimal menu of contracts is $\{ ( { q _ { L } } ^ { * } , { p _ { L } } ^ { * } ) , ( { q _ { H } ^ { * } } , { p _ { H } ^ { * } } ) \}$ , where

$$
q _ {H} ^ {*} = \phi \bigg (\frac {c - \min \left\{1 , \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\} s _ {G}}{\theta_ {H}} \bigg),\tag{11}
$$

$$
q _ {L} ^ {*} = \phi \bigg (\frac {\beta c - \min \left\{1 , \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\} \beta s _ {G}}{\theta_ {L} - (1 - \beta) \theta_ {H}} \bigg),\tag{12}
$$

and the equilibrium prices are

$$
p _ {H} ^ {*} = \frac {\theta_ {H} v (q _ {H} ^ {*}) - \theta_ {H} v (q _ {L} ^ {*}) + \theta_ {L} v (q _ {L} ^ {*}) + \min \left\{1 , \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\} s _ {G} q _ {H} ^ {*}}{q _ {H} ^ {*}},\tag{13}
$$

$$
p _ {L} ^ {*} = \frac {\theta_ {L} v (q _ {L} ^ {*}) + \min \left\{1 , \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\} s _ {G} q _ {L} ^ {*}}{q _ {L} ^ {*}}.\tag{14}
$$

The market share of CP G is Prob $\left[ \varepsilon + s _ { G } \ge 0 \right] =$ min $\left\{ 1 , { \frac { 1 } { 2 } } + { \frac { s _ { G } } { 2 \alpha } } \right\}$ . Therefore, the pro<sup>fi</sup>t optimization problem for $\mathrm { C P } G$ is given as follows:

$$
\begin{array}{c} S _ {G} ^ {*} \in \max _ {s _ {G}} r _ {G} \min \biggl \{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \biggr \} \\ - s _ {G} \bigl [ \beta q _ {L} ^ {*} + (1 - \beta) q _ {H} ^ {*} \bigr ] \min \biggl \{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \biggr \}, \end{array}
$$

where $r _ { G }$ min $\left\{ 1 , { \frac { 1 } { 2 } } + { \frac { s _ { G } } { 2 \alpha } } \right\}$ is the revenue and $s _ { G } \big [ \beta q _ { L } ^ { * } +$ $( 1 - \beta ) q _ { H } ^ { * } ] \mathrm { m i n } \left\{ 1 , { \textstyle \frac { 1 } { 2 } } + \frac { s _ { G } } { 2 \alpha } \right\}$ is the cost of sponsoring data.

In the next proposition, we compare $q _ { L } ^ { * }$ and $q _ { H } ^ { * }$ under the baseline case of no CPs sponsoring data (we denote it as case NN) with those under the case of CP G sponsoring data (we denote it as case SN).

Corollary 1. The equilibrium data consumption, $q _ { L } ^ { * }$ and $q _ { H } ^ { * } ,$ , under the case of high-margin $C P \ G$ sponsoring is greater than the data consumption under the baseline case of no CPs sponsoring data, that $i s ,$

$$
q _ {L, S N} ^ {*} > q _ {L, N N} ^ {*}, q _ {H, S N} ^ {*} > q _ {H, N N} ^ {*}.
$$

Corollary 1 implies that the introduction of data sponsorship increases equilibrium data consumption. $\mathrm { A s }$ one type of digital goods, mobile data exhibits a similar economic feature with other goods: when sponsored data exists, which is equivalent to data price drops for consumers, demand increases.

Next, we consider consumer surplus. When the high-margin $\operatorname { C P } G$ provides sponsored data, similar to Case 1 where no CPs sponsor consumers, the individual rationality constraint for low-type consumers is binding; we need to consider only the positive surplus value (information rent) of high-type consumers. In the equilibrium, the surplus value of the high-type consumers is given as follows:

$$
(1 - \beta) (\theta_ {H} - \theta_ {L}) v \Big (q _ {L, S N} ^ {*} \Big).
$$

Then, we also compare the consumer surplus under the baseline case of no CPs sponsoring data with that under the case of CP G sponsoring data and obtain the following proposition (full proof in Online Appendix A):

<sub>Proposition 3 (</sub>Consumer Surplus with Complete and <sup>Incomplete</sup> <sup>Information</sup>). With incomplete information, consumer surplus under the case where high-margin CP G is allowed to sponsor data is greater than that under the baseline case where no CP is allowed to sponsor data. With complete information, consumer surplus is equal under both cases.

At <sup>fi</sup>rst glance, the <sup>fi</sup>rst part of Proposition 3 seems straightforward: the consumer surplus is greater under Case 2 because CP G sponsors consumers’ data consumption. However, the consumer surplus may not necessarily increase. The reason is that the MNO endogenously determines the price of data plans: The MNO can increase the price of data plans to better extract consumer surplus after the introduction of sponsored data. If the value of sponsored data are fully extracted by the MNO, the consumer surplus will remain the same after CP G sponsors consumers’ data consumption. However, Proposition 3 implies that the MNO does not fully extract the value of sponsored data, and consumers bene<sup>fi</sup>t from the sponsored data of CP G.

When we dig deeper into why the MNO is not able to fully extract the value of data sponsorship, we <sup>fi</sup>nd that incomplete information is the key (the MNO is not able to observe consumer types directly). In the second part of Proposition 3, we show that under complete information (the MNO is able to differentiate between two types of consumers), the consumer surplus under the case where only $\mathrm { C P } \ G$ is allowed to sponsor data are equal to that in the baseline case of no CPs are allowed to sponsor data. This result holds for the other cases of sponsored data (Cases 3 and 4).

Proposition 3 highlights the importance of introducing incomplete information into the context of sponsored data. When information is complete (the MNO can differentiate between two types of consumers), the MNO is able to extract the value of sponsored data fully, and consumers will not bene<sup>fi</sup>t from sponsored data. However, when information is incomplete (the MNO cannot differentiate between two types of consumers), the MNO is not able to fully extract the value of sponsored data. Therefore, consumers can bene<sup>fi</sup>t from sponsored data because of their information rent. On the other hand, we notice that in the long run, sponsored data may be detrimental to consumer surplus if only one content provider is allowed to sponsor data, and content diversity is reduced. The high-margin content provider could leverage his or her advantage in revenue generation capability to expand market share and potentially drive the other content provider out of the market. To illustrate this, notice that the market share of CP G under Case 2 is Prob $\begin{array} { r } { [ \varepsilon + s _ { G } \ge 0 ] = \operatorname* { m i n } \left\{ 1 , \frac { 1 } { 2 } + \frac { s _ { G } } { 2 \alpha } \right\} } \end{array}$ . If the sponsor rate is high enough, for example, $s _ { G } = 2 \alpha$ , then the lowmargin CP B would be driven out of the market. Likewise, CP $G ^ { \prime } \mathrm { s }$ market share could be extracted when the low-margin CP B sponsors data at a high rate under Case 3. This raises anticompetitive concerns for policymakers because many network carriers are now trying to be content providers in addition to being internet service providers, which enables them to leverage their increased pricing power gained through integration and extract more surplus from consumers. For instance, in 2015, Verizon acquired AOL, a leader in digital content and advertising, with a \$4.4 billion deal that aims to create a major new player in the digital media business by combining one of the biggest mobile network providers with a leading CP (Rooney 2015). AT&T completed their acquisition of Time Warner Inc. in 2018, bringing together the content and creative talent at Warner Bros., HBO, and Turner with AT&T’s strengths in direct-toconsumer distribution to offer their customers a highquality, mobile-<sup>fi</sup>rst entertainment experience (AT&T 2018). Comcast also made a similar bid for 21st Century Fox. However, their prospects were called into question by the U.S. antitrust authorities.<sup>17</sup> Although the vertical integration of a service provider with a content provider may change the pricing incentives of upstream and downstream <sup>fi</sup>rms and reduce double marginalization, policymakers should also notice that the incentives behind the vertical integration to foreclose rivals and raise their costs could lead to welfare loss for consumers. In this regard, policymakers need to ensure that the MNO allows all content providers rather than only the ones acquired by the MNO to have opportunities to sponsor data for consumers. This is an important approach to alleviate anticompetitive concerns. On the other hand, to conduct a smooth vertical acquisition, the MNO should pay attention to government regulations about promoting online competition and openness on the internet, such as Net Neutrality<sup>18</sup> and Open Internet Order.<sup>19</sup>

Case 3. Only low-margin CP B is allowed to sponsor data.

Case 3 is symmetric with Case 2 and follows the same procedure. Detailed analysis is in Online Appendix A.

Case 4. Both CPs are allowed to sponsor data.

In this subsection, we consider the case that both the high-margin $\ \mathrm { C P } \ G$ and the low-margin CP B sponsor data. The MNO offers a menu of contracts to consumers: $\{ ( q _ { H } , p _ { H } ) , ( q _ { L } , p _ { L } ) \}$ . Consumers who are sponsored by $\boldsymbol { \mathrm { C P } } \boldsymbol { \mathrm { G } }$ or B will face a price $p _ { i } - s _ { G }$ or $p _ { i } - s _ { B } ,$ where $s _ { G }$ and $s _ { B }$ are the sponsor rate chosen by $\mathrm { C P s } \ G$ and $B ,$ respectively. In the case of both CPs sponsoring data, a consumer’s utility is

$$
\theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + s _ {G} q _ {i} \cdot \mathbf {I} _ {G} + s _ {B} q _ {i} \cdot \mathbf {I} _ {B},
$$

where $i \in \{ H , L \}$ and $\mathbf { I } _ { B }$ is an indicator function, which takes the value of one if a consumer chooses CP B.

The probability that a consumer chooses CP G is

$$
\operatorname{Prob} \left[ \varepsilon + s _ {G} - s _ {B} \geq 0 \right] = \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\}.
$$

Consumers decide which data plan they want to accept according to the expected utility function:

$$
\begin{array}{l} \text {Prob} [ \varepsilon + s _ {G} - s _ {B} \geq 0 ] \big [ \theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + s _ {G} q _ {i} \big ] \\ \quad + \{1 - \text {Prob} [ \varepsilon + s _ {G} - s _ {B} \geq 0 ] \} \big [ \theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + s _ {B} q _ {i} \big ] \\ \quad = \theta_ {i} v (q _ {i}) - p _ {i} q _ {i} + \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} q _ {i} \\ \quad + \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {B} q _ {i}, \qquad \text {where} \\ i \in \{H, L \}. \end{array}
$$

The MNO’s pro<sup>fi</sup>t optimization problem is

$$
\begin{array}{l} \max _ {(q _ {L}, p _ {L}), (q _ {H}, p _ {H})} \beta [ p _ {L} q _ {L} - c q _ {L} ] + (1 - \beta) [ p _ {H} q _ {H} - c q _ {H} ] \\ s. t. \theta_ {H} v (q _ {H}) - p _ {H} q _ {H} + \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} q _ {H} \\ \quad + \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {B} q _ {H} \\ \quad = \theta_ {H} v (q _ {L}) - p _ {L} q _ {L} + \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} q _ {L} \\ \quad + \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {B} q _ {L}, \\ \quad \theta_ {L} v (q _ {L}) - p _ {L} q _ {L} + \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} q _ {L} \\ \quad + \min \left\{\left(\frac {1}{2} - \frac {s g - s B}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {B} q _ {L} \\ \quad = 0. \end{array}
$$

The <sup>fi</sup>rst constraint is the incentive-compatibility constraint for high-type consumers: A high-type consumer has no incentive to choose the low-type contract, $\left( q _ { L } , p _ { L } \right)$ The second constraint is the individual rationality constraint (participation constraint) for low-type consumers: If a low-type consumer chooses the low-type contract, $\left( q _ { L } , p _ { L } \right)$ , the utility should be nonnegative. From our earlier discussion, we know that these two constraints should be binding at the optimum. Solving MNO’s pro<sup>fi</sup>t optimization problem, we obtain the following proposition:

Proposition 4. In the case where both CPs are allowed to sponsor data, the optimal menu of contracts is $\{ ( q _ { L } ^ { * } , { p _ { L } ^ { * } } )$ $( q _ { H } ^ { * } , p _ { H } ^ { * } ) \}$ , where

$$
q _ {H} ^ {*} = \phi \left(\frac {c - \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+} , 1 \right\} s _ {G} - \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+} , 1 \right\} s _ {B}}{\theta_ {H}}\right),\tag{15}
$$

$$
q _ {L} ^ {*} = \phi \left(\frac {\beta c - \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+} , 1 \right\} \beta s _ {G} - \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+} , 1 \right\} \beta s _ {B}}{\theta_ {L} - (1 - \beta) \theta_ {H}}\right),\tag{16}
$$

and the equilibrium prices are

$$
\begin{array}{c}\theta_ {H} v (q _ {H} ^ {*}) - \theta_ {H} v (q _ {L} ^ {*}) + \theta_ {L} v (q _ {L} ^ {*}) + \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\}\\p _ {H} ^ {*} = \frac {s _ {G} q _ {H} ^ {*} + \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+} , 1 \right\} s _ {B} q _ {H} ^ {*}}{q _ {H} ^ {*}},\\\theta_ {L} v (q _ {L} ^ {*}) + \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} q _ {L} ^ {*}\\p _ {L} ^ {*} = \frac {\left. \right. + \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+} , 1 \right\} s _ {B} q _ {L} ^ {*}}{q _ {L} ^ {*}}.\end{array}\tag {1}\tag{17}
$$

(18)

The market share of $\ \mathrm { C P } \ \mathrm { \Lambda } _ { G }$ is given by min $\left\{ \left( { \frac { 1 } { 2 } } + \right. \qquad \right.$ $\textstyle \frac { s _ { G } - s _ { B } } { 2 \alpha } ) ^ { + } , 1 \big \}$ , and the optimization problem for $\mathrm { C P } \ G$ is given as follows:

$$
\begin{array}{l} S _ {G} ^ {*} (s _ {B}) \in \max _ {s _ {G}} r _ {G} \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} \\ \qquad - s _ {G} \min \left\{\left(\frac {1}{2} + \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} [ \beta q _ {L} ^ {*} + (1 - \beta) q _ {H} ^ {*} ]. \end{array}
$$

Here, $S _ { G } ^ { * } ( s _ { B } )$ is the optimal reaction function: Given s , the optimal sponsoring amount for CP G is $S _ { G } ^ { * } ( s _ { B } )$

Similarly, the optimization problem for CP B is given as follows:

$$
\begin{array}{l} S _ {B} ^ {*} (s _ {G}) \in \max _ {s _ {B}} r _ {B} \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} \\ \qquad - s _ {B} \min \left\{\left(\frac {1}{2} - \frac {s _ {G} - s _ {B}}{2 \alpha}\right) ^ {+}, 1 \right\} [ \beta q _ {L} ^ {*} + (1 - \beta) q _ {H} ^ {*} ]. \end{array}
$$

Combining $S _ { G } ^ { * } ( s _ { B } )$ and $S _ { B } ^ { * } ( s _ { G } )$ , we can obtain $S _ { G } ^ { * }$ and $S _ { B } ^ { * }$

In the next proposition, we compare $q _ { L } ^ { * }$ and $q _ { H } ^ { * }$ under the baseline case of no CPs sponsoring data with those under the case of both CPs sponsoring data (we denote it as case SS)

Corollary 2. The equilibrium data consumption, $q _ { L } ^ { * }$ and $q _ { H } ^ { * } ,$ , under the case of both CPs sponsoring is greater than the data consumption under the baseline case of no CPs sponsoring data, that $i s ,$

$$
q _ {L, S S} ^ {*} > q _ {L, N N} ^ {*}, q _ {H, S S} ^ {*} > q _ {H, N N} ^ {*}.
$$

We conduct numerical analysis (details in Online Appendix B) to compare $q _ { L } ^ { * }$ and $q _ { H } ^ { * }$ under the case of both CPs sponsoring data with those under the case of only one CP sponsoring data because it is not analytically feasible to do so. Our result shows that the optimal data quantity is always larger when both CPs sponsor consumers than only one CP does so. This is intuitive because when both CPs compete to provide sponsored data, the MNO would sell more data to consumers to extract the surplus subsidized by the sponsoring CPs.

For consumer surplus, when both CPs provide sponsored data, the individual rationality constraint for low-type consumers is binding as well; and we need to consider only the positive surplus value (information rent) of high-type consumers. In the equilibrium, the surplus-value of the high-type consumers is given as follows:

$$
(1 - \beta) (\theta_ {H} - \theta_ {L}) v \Big (q _ {L, S S} ^ {*} \Big).
$$

Similarly, we also compare the consumer surplus under the baseline case of no CPs sponsoring data with that under the case of both CPs sponsoring data and obtain the following proposition (full proof in Online Appendix A):

Proposition 5. The consumer surplus under the case of both CPs sponsoring data is greater than that under the baseline case of no CPs sponsoring data.

Once again, our result in Proposition 5 highlights the importance of introducing incomplete information. The result seems straightforward: consumer surplus increases because both CPs provide sponsored data. However, this might not necessarily be true because the MNO endogenously determines the data price and could raise the price to better extract consumer surplus when both CPs provide sponsored data. Our analytical insights are robust: When information is incomplete, consumers can bene<sup>fi</sup>t from sponsored data. However, when information is complete, the MNO is able to extract the value of sponsored data fully, and consumer surplus will not be altered although both CPs sponsor data.

This result provides important managerial insights for policymakers. Although seller uncertainty and product uncertainty have been the two major sources of information asymmetry that has been well studied in the literature and understood in practice, consumer uncertainty (consumers’ heterogeneous valuation of the mobile data) is actually an essential element that ensures consumer surplus being augmented rather than fully extracted by the MNO when sponsored data are provided by CPs. Because of analytical intractability, we also conduct numerical analysis for the optimal consumer surplus under different market conditions. We reserve the details in Online Appendix B.

Next, we compare the MNO’s pro<sup>fi</sup>t under complete information with that under incomplete information for all four cases and obtain the following proposition (full proof in Online Appendix A):

Proposition 6. The MNO’s profit is higher under complete information than under incomplete information in all four cases.

Proposition 6 shows that with complete information, the MNO’s pro<sup>fi</sup>t increases. The intuition is that, under complete information, the MNO can separately set the price and quantity for two types of consumers. In contrast, under incomplete information, the MNO needs to prevent high-type consumers from choosing the package $\left( p _ { L } , q _ { L } \right)$ that is designed for low-type consumers. Therefore, the MNO is not able to effectively extract the surplus of high-type consumers.

## 4. Numerical Analysis

In this section, we adopt a speci<sup>fi</sup>c form of consumers value function v and conduct extensive numerical analyses to examine the optimal cases for the MNO and the content providers. In particular, we look at the following functional form: $v ( \cdot ) \equiv v _ { 0 } \ln { ( d + x ) }$ , where $v _ { 0 } = 1$ and $d = 1 .$ , which is an increasing and concave function. The main reason we adopt a logarithmic function is that this concave utility function form is widely used in the literature (Matsumoto 2006, C¸anakoglu and˘ Ozekici<sup>¨</sup> 2010, Ye and Yao 2010, Atamturk and G¨ omez´ 2017) to model the risk-averse behavior of humans. The concave form of a logarithmic function models the fact that as media consumption on mobile devices rises, marginally, consumers derive less pleasure and satisfaction. Then, the inverse function of $v ^ { \prime } ( \cdot )$ is $\begin{array} { r } { \phi ( x ) = \frac { 1 - x } { x } . } \end{array}$

## 4.1. Optimal Cases for the MNO

Our <sup>fi</sup>rst numerical analysis aims to determine the optimal case for the MNO under different market conditions. Figure 1 illustrates the result, which we summarize in the following observation.

Observation 1. The optimal case for the MNO is Case 1 (neither CP providing sponsored data) with high con sumer preference heterogeneity and low revenue rate of CPs; Case 2 (only the high-margin CP G sponsoring) with high consumer preference heterogeneity and high revenue rate of CPs; and Case 4 (both CPs sponsoring) with low consumer preference heterogeneity.

The underlying logic is as follows: Essentially, in our model, consumer preference heterogeneity on $\textstyle \mathrm { C P s , } \alpha ,$ is used to model horizontal service differentiation between CPs. If α is small, it means that the horizontal service differentiation is low and CPs compete more <sup>fi</sup>ercely. Sponsored data are an effective tool to stimulate consumers to switch from the nonsponsored CP to the sponsored CP under this scenario. Therefore, both CPs compete to provide sponsored data under Case 4 (the bottom area of Figure 1), which generates the most surplus for the MNO. In contrast, when consumer preference heterogeneity on CPs (α) is large, sponsored data are less effective because of a high level of horizontal differentiation (the degree of competition is low). Consequently, CPs cannot use sponsored data to expand their market share effectively. CP B with a lower margin drops out of the sponsoring program <sup>fi</sup>rst, leaving only CP G providing sponsored data on the market and Case 2 (the upper right area of Figure 1) becomes optimal in the equilibrium. However, if the revenue rate of the high-margin CP G is low, he or she cannot afford sponsored data either, and Case 1 (the upper left area of Figure 1) becomes the optimal case in the equilibrium. In Online Appendix B, we show that the patterns in Figure 1 are robust when we vary parameter values, which further con<sup>fi</sup>rms the underlying logic.

Our choice of parameter values is $\theta _ { H } = 1 . 5 , \ \theta _ { L } = 1 _ { \ L }$ $\beta = 0 . 6 , \mathrm { ~ c = 0 } . 6 ,$ , and $r _ { B } = 1$ . Note that these parameter values are meaningful in the relative sense. Here, $\begin{array} { r } { \frac { \theta _ { H } } { \theta _ { L } } = } \end{array}$ 1:5 means that high-type consumers value data 1.5 times as low-type consumers, and our numerical results are robust when we vary $\frac { \theta _ { H } } { \theta _ { L } } .$ In our numerical analysis, $\textstyle { \frac { r _ { G } } { r _ { B } } } \in [ 1 . 2 , 3 ]$ , which means CP G’s margin could be slightly higher $( \textstyle { \frac { r _ { G } } { r _ { B } } } = 1 . 2 )$ or signi<sup>fi</sup>cantly higher $\begin{array} { r } { ( \frac { r _ { G } } { r _ { B } } = 3 ) } \end{array}$ than CP B. The marginal cost of providing mobile data for the $\mathrm { M N O } , c = 0 . 6 ,$ , is smaller than other parameters. It captures the fact that the MNO is able to increase capacity at a low marginal cost. The cost of provisioning the marginal customer at large carriers today is less than $\$ 1,$ /month. We choose the proportion of low-type consumers $\beta$ to be 0.6, and our results are consistent when we vary $\beta .$

We also examine the optimal cases for the MNO to allow sponsored data under incomplete versus complete information. Figure 2 illustrates the result, which we summarize in the following observation.

Observation 2. Case 1 (neither CP providing sponsored data) is optimal for the MNO in a wider range of market conditions under complete information than under incomplete information.

Here the market conditions refer to horizontal service differentiation (the parameter α) as well as the revenue rate of two competing CPs (with CP $B ^ { \prime } \mathrm { s }$ revenue rate normalized to one). This result shows that sponsored data becomes more relevant under incomplete information, which is a more realistic scenario. In Online Appendix $\mathrm { B , }$ we conduct additional numerical analyses and show that this insight is robust when we vary parameter values. The intuition is that under complete information, the MNO could better differentiate consumers of different types, which enables him or her to better extract consumer surplus compared with that under incomplete information. Consequently, the CPs’ surplus gets extracted more by the MNO as well when the CPs provide sponsored data to consumers, which results in less willingness to sponsor consumers under complete information. Therefore, we observe a wider area of Case 1 under complete information (Figure 2) than incomplete information (Figure 1).

Speci<sup>fi</sup>cally, under incomplete information, the incentive-compatibility constraint of the high-type consumers $\theta _ { H } v ( q _ { H } ) - p _ { H } q _ { H } \geq \theta _ { H } v ( q _ { L } ) - p _ { L } q _ { L }$ requires that the optimal data quantity $q _ { L } ^ { * }$ cannot be too high compared with the scenario under complete information. Otherwise, the high-type consumers would prefer the data plan $( p _ { L } ^ { * } , q _ { L } ^ { \bar { * } } )$ designated for low-type consumers and the above incentive-compatibility constraint is violated. On the other hand, we can obtain that under incomplete information, the optimal data amount for high-type consumers is $\begin{array} { r } { q _ { H } ^ { * } = \phi \biggl ( \frac { c - \operatorname* { m i n } \big \{ 1 , \frac { 1 } { 2 } + \frac { s _ { G } } { 2 \alpha } \big \} s _ { G } } { \theta _ { H } } \biggr ) . } \end{array}$ , which is the same as that unde complete information. Therefore, when switching from incomplete information to complete information, the cost for CP G to provide sponsored data $( s _ { G } \big \lceil \beta q _ { L } ^ { * } +$ $( 1 - \beta ) q _ { H } ^ { * } ] \mathbf { m i n } \left\{ 1 , \frac { 1 } { 2 } + \overline { { \frac { s _ { G } } { 2 \alpha } } } \right\} )$ goes up with everything else equal, which results in less incentive for the content provider to sponsor data.

## 4.2. Optimal Cases for the Content Providers

Do the content providers always have an incentive to sponsor consumers for their data plans? In order to answer this question, we examine the optimal cases for CP G and CP B through numerical analysis. Figure 3 illustrates the result, and we summarize it in the following observation.

Figure 1. (Color online) Optimal Cases for the MNO to Allow Sponsored Data under Incomplete Information, Where $\theta _ { H } = \bar { 1 } . 5 , \theta _ { L } = 1 , \beta = 0 . 6 , { \bf c } = 0 . 6 ,$ and $r _ { B } = 1$  
![](/api/attachments/7FVC344N/fulltext/images/1b1719b76975dc516ad3887e113f11e0ac9851bf23a218c3e8edf0b5dcb6ae3f.jpg)

Figure 2. (Color online) Optimal Cases for the MNO to Allow Sponsored Data under Complete Information, Where $\theta _ { H } = \bar { 1 . 5 } , \theta _ { L } = 1 , \beta = 0 . 6 , { \bf c } = 0 . 6 ,$ , and r 1  
![](/api/attachments/7FVC344N/fulltext/images/2a4d5ee922164a1fe2a1354951dba6ce80207e3e4f5f3b67d2c3094365b81b25.jpg)  
Observation 3. Both CPs prefer to provide sponsored data alone (Case 2 for CP G and Case 3 for CP B) when consumer preference heterogeneity is low; CP B prefers no sponsored data for both CPs (Case 1) when consumer preference heterogeneity is high, whereas CP G does so only when his or her advantage of revenue rate over $\mathrm { C P } \overset { \cdot } { B }$ is not signi<sup>fi</sup>cant.

The intuition is that α models the horizontal differentiation between CPs. As we discussed above, sponsored data are an effective tool for CPs to seize market share from their competitors when the horizontal differentiation is small. In an extreme case, $\alpha = 0 ,$ which implies no horizontal content differentiation, and two CPs provide homogenous content: The degree of competition is the highest, and a slight increase in sponsored data can make all consumers switch to the sponsoring CP. Therefore, when α is small, both CPs have a strong incentive to provide sponsored data; they prefer to do so alone if possible. However, one thing that needs to be emphasized here is that our analysis in the previous subsection has demonstrated that Case 3 is never an optimal choice for the MNO who stands in a dominant market position in deciding whether to allow the CPs to provide sponsored data. Therefore, Case 3 never appears in the <sup>fi</sup>nal equilibrium.

When the horizontal service differentiation is large, sponsored data become a less effective tool for the content providers to capture market share; it is optimal for both CPs not to provide sponsored data (Case 1). However, when the revenue rate of CP G $( r _ { G } )$ is high, CP G becomes interested in providing sponsored data even if α is large. The underlying reason is that with a high revenue rate, CP G could afford sponsored data extensively, which captures the market share of CP B at a high cost (because α is large and consumers are not easy to switch). The market share of CP G under this case is Prob $\left[ \varepsilon + s _ { G } \ge 0 \right] =$ min $\left\{ 1 , { \frac { 1 } { 2 } } + { \frac { s _ { G } } { 2 \alpha } } \right\}$ , which could be close to one (CP B being driven out of the market) with suf<sup>fi</sup>ciently high s .

## 4.3. Optimal Sponsor Rate for the Content Providers

In this subsection, we investigate how CPs’ optimal sponsor rate varies with their revenue rate and consumer preference heterogeneity under the equilibrium cases of Case 2 (only the high-margin CP G provides sponsored data) and Case 4 (both CPs provide sponsored data). Figure 4 illustrates the result, which we summarize in the following two observations.

Observation 4a. When the high-margin CP G provides sponsored data alone under Case 2, the optimal sponsor rate monotonously increases in his or her revenue rate; however, it <sup>fi</sup>rst increases in consumer preference heterogeneity and then decreases.

For ${ \mathrm { C P ~ } } G ,$ the optimal sponsor rate increases in his or her revenue rate $r _ { G }$ under Case 2. This is intuitive because a higher revenue rate enables CP G to afford a higher sponsor rate in order to seize more market share from her competitor. When consumer preference heterogeneity α is relatively large, the optimal sponsor rate decreases in α. The reason is that large α indicates high horizontal service differentiation and low competition between CPs, which means it is less ef<sup>fi</sup>cient to make consumers switch from the nonsponsoring CP to the sponsoring CP through sponsored data. Therefore, $\mathrm { C \hat { P } }$ G’s incentive to provide sponsored data is not strong under this scenario; and it declines even more as consumer preference heterogeneity increases. However, when α is small, sponsored data become an effective tool to capture market share. Thus, CP G would like to provide more sponsored data to seize more market share from CP B. That is why the optimal sponsor rate of CP G increases in α when α is small.

Observation 4b. When both CPs provide sponsored data under Case 4, the high-margin CP G’s optimal sponsor rate monotonously increases in his or her revenue rate; however, it <sup>fi</sup>rst increases in consumer preference heterogeneity and then decreases; the low-margin CP B’s optimal sponsor rate decreases in both CP G’s revenue rate and consumer preference heterogeneity.

When both CPs compete to sponsor consumers (Case 4), unsurprisingly, CP G’s optimal sponsor rate increases in his or her revenue rate because a highe revenue rate enables CP G to sponsor consumers more intensively in order to capture more market share. This puts the low-margin CP B in a more inferior position with less market share. Consequently,

Figure 3. (Color online) Optimal Cases for the CPs Under Incomplete Information, Where $\theta _ { H } = 1 . 5 , \theta _ { L } = 1 , \beta = 0 . 6 , { \bf c } = 0 . 6 ,$ and $r _ { B } = 1$  
![](/api/attachments/7FVC344N/fulltext/images/cd76e2533348c706bd1a953ada96887fcdfd1e5416fadd00b51ffdfa3565d976.jpg)  
sponsored data becomes less affordable to him or her and his or her optimal sponsor rate decreases in CP G’s revenue rate. For the same reason as we have illustrated for Observation 4a, CP G’s optimal sponsor rate <sup>fi</sup>rst increases in α and then decreases. The lowmargin CP B reacts to CP G’s data sponsorship by also providing sponsored data in order to defend his or her market share. However, as consumer preference heterogeneity α increases, sponsored data becomes less effective in seizing market share and CP B reacts by sponsoring less. Therefore, CP B’s sponsor rate decreases in α under Case 4.

## 4.4. Optimal Profit for the Content Providers

We next investigate how CPs’ optimal pro<sup>fi</sup>t varies with their revenue rate and consumer preference heterogeneity under the equilibrium cases of Case 2 (only the high-margin CP G provides sponsored data) and Case 4 (both CPs provide sponsored data). Figure 5 illustrates the result, and we summarize it in the following two observations.

Observation 5a. When the high-margin CP G provides sponsored data alone under Case 2, his or her optimal pro<sup>fi</sup>t increases in his or her revenue rate and decreases in consumer preference heterogeneity.

Its intuitive that CP G’s revenue rate affects his or her pro<sup>fi</sup>t positively, either under Case 2 or Case 4. To understand the effect of consumer preference heterogeneity on CP G’s optimal pro<sup>fi</sup>t when he or she provides sponsored data alone under Case 2, recall that larger α indicates higher horizontal service differentiation between CPs and sponsored data become less effective for CP G to capture market share from CP B. Therefore, although CP G provides sponsored data alone under Case 2 without CP B competing to

![](/api/attachments/7FVC344N/fulltext/images/0fd2e9793a374790e7bdb1a519a578093321e9cc9d970cdfe805fc1450264170.jpg)  
sponsor consumers, CP G’s pro<sup>fi</sup>t decreases as consumer preference heterogeneity increases.

Observation 5b. When both CPs provide sponsored data under Case 4, the high-margin CP G’s optimal pro<sup>fi</sup>t increases in both his or her revenue rate and consumer preference heterogeneity; the low-margin CP B’s optimal pro<sup>fi</sup>t monotonously decreases in CP G’s revenue rate. However, it <sup>fi</sup>rst decreases in con sumer preference heterogeneity and then increases.

When both CPs compete to provide sponsored data under Case 4, their pro<sup>fi</sup>t increases in α under most circumstances. The underlying reason is that, as we have illustrated above, when α is small, the horizontal service differentiation is low and both CPs compete <sup>fi</sup>ercely by subsidizing consumers with sponsored data to defend their market share. When the horizontal service differentiation increases, the competition between two CPs to sponsor consumers becomes less <sup>fi</sup>erce, which results in higher pro<sup>fi</sup>t for both CPs. We also notice that the pro<sup>fi</sup>t of lowmargin CP B actually decreases in α when α is small. The reason is that the sponsor rate of the highmargin CP G increases in α within this region (as we see in Observation 4b), which results in a smaller market share and less pro<sup>fi</sup>t for CP B. CP B’s optimal pro<sup>fi</sup>t decreases in CP G’s revenue rate as well, because a higher revenue rate of CP G enables him or her to sponsor consumers more intensively, which results in more market share of CP B being extracted, thus, less pro<sup>fi</sup>t for CP B.

## 4.5. Optimal Cases for Social Welfare

We examine the optimal cases for social welfare in this subsection. Figure 6 illustrates the result, which we summarize in the following observation.

Figure 4. (Color online) Optimal Sponsor Rate for the CPs, Where $\theta _ { H } = 1 . 5 ,$ $\theta _ { L } = 1$ , β <sub>-</sub> 0:6, $\mathbf { c } = 0 . 6 ,$ and $r _ { B } = 1$  
![](/api/attachments/7FVC344N/fulltext/images/a408d544d27df308dd6c74b02344c6376ee59f30ccb53bd17cfcccf045f4673b.jpg)

![](/api/attachments/7FVC344N/fulltext/images/27cceccffa50de8d6337c417d109554046f055b38443271e51003df46a3093a4.jpg)  
Observation 6. Social welfare is optimal under Case 2, where only the high-margin CP G provides sponsored data under most market conditions; when consumer preference heterogeneity is high, and the revenue rate of CPs is low, social welfare is optimal under Case 1, where neither CP sponsors consumers.

The intuition is as follows. As Figure A.1 in Online Appendix A shows, there are three parties of players in our model, the MNO, the CPs, and consumers. From a social planner’s perspective, the MNO’s pricing policy is purely “wealth transfer” rather than “wealth creation.” In other words, both the consumers’ payment to the MNO for mobile data and the content providers’ subsidization of sponsored data for consumers are essentially internal wealth transfers within the system. No matter how much the MNO charges consumers for the mobile data and the CPs sponsor consumers, the wealth simply moves from one party to another with the total amount

![](/api/attachments/7FVC344N/fulltext/images/79bd38f825ef2c660e80225a3ce10a9bfbd9f18f61f692a560ed9e54b463ec66.jpg)  
unchanged. As far as the calculation of social welfare is concerned, the social planner cares only about the factors that can affect net “wealth creation,” more precisely, the net increase in social welfare. The only thing that impacts social welfare is the content providers’ revenue-generation capability. With the same market coverage, the higher CPs’ revenue-generation capability is, the more net social wealth they can create. Therefore, the social planner would like to see the market share of the high-margin CP to be larger because the high-margin CP could create more value than the low-margin CP with the same market share. Under Case 2, only the high-margin $\boldsymbol { \mathrm { C P } } \boldsymbol { \mathrm { G } }$ provides sponsored data and gains a larger market share than under Case 3 (only the low-margin CP B provides sponsored data) as well as Case 4 (both CPs provide sponsored data), which creates the most net increase in social welfare. Thus, the social welfare under Case 2 is higher than that under Cases 3 and 4. When CPs

The profit of CP G under Case 2

The profit of CP B under Case 4  
Figure 5. (Color online) Optimal Pro<sup>fi</sup>t for the $\mathrm { C P s , }$ Where $\theta _ { H } = 1 . 5 , \theta _ { L } = 1 , \beta = 0 . 6 , { \bf c } = 0 . 6 ,$ and $r _ { B } = 1$  
![](/api/attachments/7FVC344N/fulltext/images/ba0845ff958cc7881f55bf84f734786fd2338a0f6c8d24eeae26af7916484a8b.jpg)

The profit of CP G under Case 4  
![](/api/attachments/7FVC344N/fulltext/images/7f680febfa307e7f34d515ce944d3b7b19234ecd2094a620966c5293a252706d.jpg)  
revenue rates are low, and consumer preference heterogeneity on CPs (α) is large, social welfare is the highest under Case 1, where no CPs sponsor data. This is because sponsored data are not an effective tool to capture market share when there is a high level of horizontal differentiation between CPs, and both CPs are not well motivated to sponsor consumers because of their low revenue rates. Therefore, social welfare is actually maximized when neither CP provides sponsored data.

## 5. Extensions

## 5.1. Relaxing Full Market Coverage Assumption

Niculescu et al. (2018) show the distinction between partial market coverage and full market coverage. In our context, a full market coverage assumption means that the MNO serves both types of consumers. Under some conditions, it might be in the ${ \mathrm { M N O } } ^ { \prime } { \mathrm { s } }$ best interest to serve only high-type consumers (it is never optimal for the MNO to serve only low-type consumers). It is worth noting that almost all prior studies on

![](/api/attachments/7FVC344N/fulltext/images/433584ee91ed1d4ab0ee0e429471ff86b75ed978186e3581823d2f159ba9cdb3.jpg)  
incomplete information principal-agent models assume that the market is fully covered: both types of consumers are served $( \mathrm { e . g . }$ , Laffont and Martimort 2009). The reason is that if the market is not fully covered, then it becomes a case where the MNO targets only the high-type consumers and completely ignores the low-type consumers. In that case, the incentivecompatibility constraint will be ignored: The MNO does not need to make sure that a high-type consumer prefers $( q _ { H } , p _ { H } )$ to $\left( q _ { L } , p _ { L } \right)$ and a low-type consumer prefers $( q _ { L } , p _ { L } )$ to $( q _ { H } , p _ { H } )$ . The MNO only has to con sider the individual rationality constraint for the hightype consumers. In this section, we look at the log utility function, $v ( x ) = v _ { 0 } \ln { ( d + x ) }$ , where $v _ { 0 } = 1$ and $d = 1$ and characterize the conditions under which the MNO has an incentive to cover the market partially.

Under (i), the baseline case without sponsored data, the MNO will serve only high-type consumers if

$$
\theta_ {L} - (1 - \beta) \theta_ {H} \leq \beta c.\tag{19}
$$

Otherwise, the MNO will serve both types of consumers. Note that Condition (19) is more likely to be satis<sup>fi</sup>ed when $\theta _ { H }$ is larger or $\theta _ { L }$ is smaller. In other words, when the high-type consumers’ valuation of mobile data is higher, or the low-type consumers’ valuation is lower, the MNO is more likely to serve only high-type consumers. Under this case, the MNO’s pro<sup>fi</sup>t function is

$$
\pi_ {1} ^ {M N O} \bigg (q _ {H} ^ {*} = \frac {\theta_ {H}}{c} - 1, q _ {L} = 0 \bigg) = (1 - \beta) \bigg [ \theta_ {H} \mathrm{ln} \left(\frac {\theta_ {H}}{c}\right) - c \frac {\theta_ {H}}{c} + c \bigg ].
$$

Under (ii), the case where only $\mathrm { C P } \ G$ is allowed to sponsor, the MNO will serve only high-type consumers if

$$
\theta_ {L} - (1 - \beta) \theta_ {H} \leq \beta \bigg (c - \min \bigg \{\frac {1}{2} + \frac {s _ {G} ^ {*}}{2 \alpha}, 1 \bigg \} s _ {G} ^ {*} \bigg) ^ {+},\tag{20}
$$

where $s _ { G } ^ { * }$ is the equilibrium subsidization by $\ \mathrm { C P } \ G$ Under this case, the MNO’s pro<sup>fi</sup>t function is

$$
\begin{array}{r l} & {\pi_ {2} ^ {M N O} (q _ {H}, q _ {L} = 0) = (1 - \beta) \bigg [ \theta_ {H} \mathrm{ln} (1 + q _ {H})} \\ & {+ \min \bigg \{\frac {1}{2} + \frac {s _ {G} ^ {*}}{2 \alpha}, 1 \bigg \} s _ {G} ^ {*} q _ {H} - c q _ {H} \bigg ],} \\ & {q _ {H} ^ {*} (s _ {G} ^ {*}) = \max \Bigg \{0, \frac {\theta_ {H}}{c - \min \bigg \{\frac {1}{2} + \frac {s _ {G} ^ {*}}{2 a} , 1 \bigg \} s _ {G} ^ {*}} - 1 \Bigg \}.} \end{array}
$$

where

Under (iii), the case where only CP B is allowed to sponsor, the MNO will serve only high-type consumers if

$$
\theta_ {L} - (1 - \beta) \theta_ {H} \leq \beta \bigg (c - \min \bigg \{\frac {1}{2} + \frac {s _ {B} ^ {*}}{2 \alpha}, 1 \bigg \} s _ {B} ^ {*} \bigg) ^ {+},\tag{21}
$$

where $s _ { B } ^ { * }$ is the equilibrium subsidization by CP B. Under this case, the MNO’s pro<sup>fi</sup>t function is

Figure 6. (Color online) Optimal Cases for Social Welfare, Where $\theta _ { H } = 1 . 5 , \theta _ { L } = 1 , \bar { \beta = } 0 . 6 , { \bf c } = 0 . 6 ,$ , and $r _ { B } = 1$  
![](/api/attachments/7FVC344N/fulltext/images/669b99603b9b52241a856e423b57f1808dfba7e2d758402460fd6bc6983ff2c3.jpg)

$$
\begin{array}{r l} & {\pi_ {3} ^ {M N O} (q _ {H}, q _ {L} = 0) = (1 - \beta) \bigg [ \theta_ {H} \mathrm{ln} (1 + q _ {H})} \\ & {+ \min \left\{\frac {1}{2} + \frac {s _ {B} ^ {*}}{2 \alpha}, 1 \right\} s _ {B} ^ {*} q _ {H} - c q _ {H} \bigg ],} \\ & {q _ {H} ^ {*} (s _ {B} ^ {*}) = \max \left\{0, \frac {\theta_ {H}}{c - \mathrm{min} \left\{\frac {1}{2} + \frac {s _ {B} ^ {*}}{2 \alpha} , 1 \right\} s _ {B} ^ {*}} - 1 \right\}.} \end{array}
$$

where

Under (iv), the case where both CPs are allowed to sponsor, the MNO will serve only high-type consumers if

$$
\begin{array}{c} \theta_ {L} - (1 - \beta) \theta_ {H} \leq \beta \bigg (c - \min \left\{\left(\frac {1}{2} + \frac {s _ {G} ^ {*} - s _ {B} ^ {*}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} ^ {*} \\ - \min \left\{\left(\frac {1}{2} - \frac {s _ {G} ^ {*} - s _ {B} ^ {*}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {B} ^ {*} \bigg) ^ {+}. \end{array}\tag{22}
$$

Under this case, the MNO’s pro<sup>fi</sup>t function is

$$
\begin{array}{l} \pi_ {4} ^ {M N O} (q _ {H}, q _ {L} = 0) \\ = (1 - \beta) \left[ \begin{array}{c} \theta_ {H} \mathrm{ln} \left(1 + q _ {H}\right) + \mathrm{min} \left\{\left(\frac {1}{2} + \frac {s _ {G} ^ {*} - s _ {B} ^ {*}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {G} ^ {*} q _ {H} \\ + \mathrm{min} \left\{\left(\frac {1}{2} - \frac {s _ {G} ^ {*} - s _ {B} ^ {*}}{2 \alpha}\right) ^ {+}, 1 \right\} s _ {B} ^ {*} q _ {H} - c q _ {H} \end{array} \right], \\ \text {where} q _ {H} ^ {*} (s _ {G} ^ {*}, s _ {B} ^ {*}) = \max \Bigg \{0, \frac {\theta_ {H}}{c - \mathrm{min} \left\{\left(\frac {1}{2} + \frac {s _ {G} ^ {*} - s _ {B} ^ {*}}{2 \alpha}\right) ^ {+} , 1 \right\} s _ {G} ^ {*} - \mathrm{min} \left\{\left(\frac {1}{2} - \frac {s _ {G} ^ {*} - s _ {B} ^ {*}}{2 \alpha}\right) ^ {+} , 1 \right\} s _ {B} ^ {*}} - 1 \Bigg \}. \end{array}
$$

Comparing the equilibrium data consumption under different cases, we have the following result:

Corollary 3. The equilibrium data consumption under the case of high-margin $C P G ,$ , low-margin $C P B ,$ or both $C P s$ sponsoring is greater than that in the baseline case $o f$ no CPs sponsoring data, that $i s , \quad q _ { H , S N } ^ { * } > q _ { H , N N } ^ { * } , q _ { H } ^ { * }$ ,NS $> q _ { H , N N } ^ { * } , \ q _ { H , S S } ^ { * } > q _ { H , N N } ^ { * } ,$ when the market is not fully covered.

Therefore, the same result in the main model still holds when we relax the assumption of full market coverage.

## 5.2. Content Quality Difference

Following the model settings of prior studies (Choi and Kim 2010, Cheng et al. 2011), we assume that the two CPs provide the same content quality in our main analysis. It is a theoretical simpli<sup>fi</sup>cation so that we can focus on the main interest in our model. It is also a reasonable assumption in some real-world scenarios. For example, Spotify and Pandora are competing music content providers. Their content quality is similar because their music “libraries are very comparable, and there aren’t any notable artists who appear on one service and not the other.”<sup>20</sup>

In this subsection, we extend our model and consid er the scenario where the two CPs provide different content quality. In our main model, each consumer’s taste between CPs, $\varepsilon ,$ is a random draw from a uniform distribution, $[ - \alpha , \alpha ]$ . In the baseline case where neither of the CPs is allowed to sponsor data, if $\varepsilon \ge 0$ a consumer will choose CP G; if $\varepsilon < 0$ , a consumer will choose CP B. In other words, it implies that the two CPs provide the same content quality. If the highmargin CP G sponsors data, a consumer will choose CP G when $\varepsilon + s _ { G } \ge 0$ and CP B is chosen when $\varepsilon + s _ { G } < 0 .$ . In other words, consumers are more likely to choose CP G with a high level of sponsored data from CP G (a larger value of $s _ { G } )$ . Therefore, the market share of CP G is given by

$$
\mathrm{Prob} [ \varepsilon + s _ {G} \geq 0 ] = \min \left\{1, \frac {1}{2} + \frac {s _ {G}}{2 \alpha} \right\}.
$$

We can modify our model setting to re<sup>fl</sup>ect that CP B provides a higher level of content quality. In this extension, each consumer’s taste between ${ \mathrm { C P s } } , \ \varepsilon ,$ is a random draw from a uniform distribution, $[ - \omega , \alpha ]$ where $\omega > \alpha > 0 .$ . Therefore, in the baseline case where neither of the CPs is allowed to sponsor data, the market share of CP G is Prob $\begin{array} { r } { [ \varepsilon \ge 0 ] \stackrel {  } { = } \frac { \alpha } { \omega + \alpha } < \frac 1 2 } \end{array}$ and the market share of CP B is Prob $\begin{array} { r } { [ \varepsilon < 0 ] = \frac { \omega } { \omega + \alpha } > \frac { 1 } { 2 } . } \end{array}$ In other words, when CP B provides a higher level of content quality, the market share of CP B is larger than that of CP G. The quality difference between the two CPs’ content is captured by the difference between ω and α: If the difference between ω and α is larger, then the quality difference between the two CPs’ content is larger. In the case where only CP G is allowed to sponsor data, the market share of CP G is

$$
\mathrm{Prob} [ \varepsilon + s _ {G} \geq 0 ] = \min \left\{1, \frac {\alpha}{\omega + \alpha} + \frac {s _ {G}}{\omega + \alpha} \right\}.\tag{23}
$$

Suppose that CP B is a small innovative CP (providing a higher level of quality). Without sponsored data, the market share of CP B is Prob $\begin{array} { r } { \bar { \mathbf { \Theta } } \varepsilon < 0 ] = \frac { \omega } { \omega + \alpha } , } \end{array}$ which is larger than $1 / 2$ because of his or her high content quality. The market share of CP G is Prob $\left[ \varepsilon \geq 0 \right] =$ $\begin{array} { r } { \frac { \mathbf { \dot { \alpha } } _ { \alpha } } { \omega + \alpha } < \frac { \mathbf { \dot { 1 } } } { 2 } } \end{array}$ . However, from Equation (23), we can see that, with sponsored data, CPs with deep pockets, such as CP G (in our model, CP G has a higher revenue generation rate), may obtain a larger market share with sponsored data:

$$
\min \left\{1, \frac {\alpha}{\omega + \alpha} + \frac {s _ {G}}{\omega + \alpha} \right\} > \frac {\alpha}{\omega + \alpha}.
$$

When the level of sponsored data is suf<sup>fi</sup>ciently high, CP B might be driven entirely out of the market, although it provides a higher level of content quality. This result shows that a major content provider can leverage his or her advantage in revenue-generation capability to gain market power in digital content markets under some market conditions even if his or her quality of content is lower than his or her smaller but more in novative competitors.

To further understand how quality difference affects the MNO’s decision on sponsored data, we conduct another numerical analysis; the result is shown in Figure 7. When α is small, only the high-margin CP G providing sponsored data (Case 2) is the optimal case (the bottom area of Figure 7). The intuition is that the most market share $\dot { \mathrm { C P } } \ B$ could extract through providing sponsored data is $\mathrm { C P } \ G ^ { \prime } \mathrm { s }$ market share Prob $\begin{array} { r } { [ \varepsilon \ge 0 ] = \frac { \alpha } { \omega + \alpha } . } \end{array}$ . When α is small, the content quality of CP G is much lower than that of ${ \mathrm { C P } } ^ { - } B .$ . In other words, CP $B ^ { \prime } \mathrm { s }$ potential market gain is small and has no incentive to sponsor consumers extensively. With $\begin{array} { r } { s _ { B } = \alpha , } \end{array}$ , CP B’s market share would be Prob $\varepsilon + s _ { B } \le 0 ] =$ min $\begin{array} { r } { \left\{ 1 , \frac { \omega } { \omega + \alpha } + \frac { s _ { B } } { \omega + \alpha } \right\} = 1 } \end{array}$ Therefore, the MNO would rather prefer $\mathrm { C P } \ G$ to provide sponsored data (Case 2) more extensively to extract more surplus. Meanwhile, CP G possesses a strong incentive to expand his or her market share through sponsored data; Case 2 turns out to be the optimal case fo the MNO under this scenario.

When α is larger, the content quality of two CPs does not differ signi<sup>fi</sup>cantly; both CPs have incentives to provide sponsored data. However, because the revenue rate of CP G is higher than that of CP $B ,$ allowing only the high-margin CP G to provide sponsored data generates more surplus for the MNO. Thus, Case 2 (the upper right area of Figure 7) is optimal for the MNO under this scenario. If the revenue rate of CP G is not quite high, then CP G does not have much incentive to provide sponsored data either and Case 1 becomes the optimal case for the MNO (the upper left area of Figure 7).

Figure 7. (Color online) Optimal Cases for the MNO with Content Quality Difference Under Incomplete Information, Where $\theta _ { H } = 1 . { \dot { 5 , } } \theta _ { L } = 1 , \beta = 0 . 6 , { \bf c } = 0 . 6 , \omega = 2 . 6 , \mathrm { a n d } r _ { B } = 1$

![](/api/attachments/7FVC344N/fulltext/images/953440243685a600c170478b93e92296c8ba3232ee8a5baca2e7e6b65d68f4d1.jpg)

Figure 8. (Color online) Optimal Cases for the MNO with Content Quality Difference Under Complete Information, Where $\theta _ { H } = 1 . 5 , \theta _ { L } = 1 , \beta = 0 . 6 , \mathbf { c } = 0 . 6 , \omega = 2 . 6$ and r 1  
![](/api/attachments/7FVC344N/fulltext/images/37a108f7a7995a5cdb44a37879372068fe4bf3a3364b77eeff72e2ed03e6ffac.jpg)

When α is moderate, the market share of CP G is larger; this provides an incentive for CP B to sponsor consumers more extensively to seize market share. Because the market share of CP B is larger than that of CP G in the baseline case $\begin{array} { r } { ( \frac { \omega } { \omega + \alpha } > \frac { \alpha } { \omega + \alpha } ) } \end{array}$ , it turns out that the MNO bene<sup>fi</sup>ts more from CP B providing sponsored data rather than CP G; thus, Case 3 (the middle triangle area of Figure 7) is optimal. Notice that when the revenue rate of CP G increases under this scenario, Case 2 becomes the optimal case because the highmargin CP G could afford to sponsor consumers more extensively, which generates more surplus for the MNO than Case 3, where CP B sponsors consumers.

We also examine the optimal cases for the MNO to allow sponsored data with the content quality difference under complete information (Figure 8). Similar to our main model (the same content quality for both CPs), we <sup>fi</sup>nd that the MNO should adopt Case 1 (no CP provides sponsored data) in a wider range of market conditions under complete information than under incomplete information. This result veri<sup>fi</sup>es our intuition that sponsored data becomes more relevant under incomplete information, which is a more realistic scenario, even when considering the content quality difference for CPs.

## 6. Conclusions and Future Research Directions

We analyze an incomplete information game-theoretic model for a monopolist MNO and two competing CPs who might compensate consumers’ digital content consumption by providing sponsored data. We <sup>fi</sup>nd that the impact of sponsored data on consumer surplus crucially depends on whether the MNO has complete information over consumer types. In a more realistic scenario with incomplete information where the MNO cannot perfectly observe consumer types, sponsored data can improve consumer surplus. This result provides a complete picture of the impact of sponsored data on consumer surplus and reconciles the debate and con<sup>fl</sup>icting views between scholars, digital rights groups, and network carriers regarding this issue. Our result also shows that under incomplete information, the MNO should allow sponsored data in a wider range of market conditions than under complete information. This suggests that sponsored data are a more relevant business model under the more realistic scenario of incomplete information, which has been neglected by previous studies. Maintaining a customer database has long been a marketing activity conducted by many businesses. The digitalization of businesses and the technical progress have empowered the harvest of customer data more effortlessly and at a larger scale. Not only does the collection and processing of customer information enable price discrimination for <sup>fi</sup>rms, more than often, it leads to privacy concerns as well (Gal-Or et al. 2018, Montes et al. 2019, Johnson et al. 2020). Therefore, policymakers should devote more attention to the protection of consumer privacy and limit the data that can be collected by the <sup>fi</sup>rms, which then leads to incomplete information case and sustain consumer surplus.

We also <sup>fi</sup>nd that if the ARPU of one CP is signi<sup>fi</sup> cantly higher than the other, the MNO prefers the high-margin CP to provide sponsored data because more values can be generated by this CP than the low-margin CP out of the same market share and then extracted by the MNO. Consequently, the MNO could favor some content providers over others by acting as a gatekeeper to pick winners and losers. This requires attention from policymakers because promising startup content providers could be driven out of the market by their incumbent competitors with higher ARPU and deeper pockets, which could harm internet innovation in the long run. Previous studies tend to underestimate this long-run detrimental effect of sponsored data, that is, small players, not-for-pro<sup>fi</sup>t entities, and start-ups do not get an equal chance to compete on the market, which could bring an end to the era of “innovation without needing permission” (FCC 2010, p. 140.).

Our research has several limitations. First, the MNO has no capacity constraint in our model setting. As we show through our analysis, subsidization from content providers creates a surge for consumers’ data consumption, which could put the MNO’s infrastructure capacity under pressure and cause network congestion. The same problem is worth investigating by factoring in the ${ \mathrm { M N O } } ^ { \prime } { \mathrm { s } }$ capacity constraints. Second, we discuss in the extension the scenario where the two CPs provide different content quality; nevertheless, we assume that consumers single-home, that is, they only choose one of the two content providers throughout the analysis. In reality, however, consumers repeatedly switch from one content provider to another or stay tuned with multiple content providers. It would be interesting to examine consumers’ multihoming strategy as a future research direction. Third, we assume a monopolist MNO in our model settings. It would be interesting to examine the competition between MNOs. When only one MNO exists in the market, it can effectively extract CPs’ pro<sup>fi</sup>ts from a dominant position. The existence of multiple competing MNOs should make the CPs relatively better off. However, the impact of sponsored data on consumer surplus is unclear and needs to be further examined. Although we do not expect the overall dynamics of the model to change dramatically, the extent of competition in the MNO market can certainly affect consumers’ choices (Guo et al. 2017).

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their helpful and constructive suggestions throughout the review process. Professor H. K. Cheng gratefully acknowledges the generous research support from the John B. Higdon Eminent Scholar chair.

## Endnotes

<sup>1</sup> See https://www.ericsson.com/en/mobility-report/futuremobile-data-usage-and-traffic-growth (last accessed August 3, 2021).

<sup>2</sup> See http://arstechnica.com/business/2015/01/att-has-10-businessespaying-for-data-cap-exemptions-and-wants-more (last accessed August 3, 2021).

<sup>3</sup> See https://www.verizon.com/about/news/introducing-freebeedata-new-sponsored-data-service-verizon (last accessed August 3, 2021).

<sup>4</sup> See http://www.forbes.com/sites/ewanspence/2012/02/27/attlooking-to-double-dip-on-mobile-data-charges/#1800acc372f6 (last accessed August 3, 2021).

<sup>5</sup> See http://www.theverge.com/2014/1/6/5280566/att-sponsoreddata-bad-for-the-internet-the-economy-and-you (last accessed August 3, 2021).

<sup>6</sup> See http://www.thehindu.com/sci-tech/technology/internet/ trai-rules-in-favour-of-net-neutrality/article8209455.ece (last ac cessed August 3, 2021).

<sup>7</sup> See https://www.cnet.com/news/at-t-says-sponsored-data-doesnot-violate-net-neutrality/ (last accessed August 3, 2021).

<sup>8</sup> See https://www.wired.com/2014/01/att-sponsored-data/ (last accessed August 3, 2021).

<sup>9</sup> See https://www.forbes.com/sites/hughmcintyre/2017/11/03/ pandora-is-losing-850000-listeners-every-month/#b38b2a55a93f (last accessed August 3, 2021).

<sup>10</sup> See https://www.reuters.com/article/usa-wireless-fcc/top-fouru-s-wireless-carriers-increase-control-of-market-review-findsidUSL1N0U22PR20141219 (last accessed August 3, 2021).

<sup>11</sup> See https://www.wsj.com/articles/good-luck-leaving-yourwireless-phone-plan-1392056715 (last accessed August 3, 2021).

<sup>12</sup> To avoid trivial cases, we assume that $\theta _ { L } > ( 1 - \beta ) \theta _ { H }$ by following prior literature (Laffont and Martimort 2009).

<sup>13</sup> Joe-Wong et al. (2015, p. 3) explain that in this setting, “users can choose one of several data plans that charge different amounts for different monthly data caps.”

<sup>14</sup> We focus on the separating equilibrium and prove in Online Appendix A why a pooling equilibrium is not an optimal solution.

<sup>15</sup> Our assumption $\theta _ { L } > ( 1 - \beta ) \theta _ { H }$ at the beginning of Section 3 ensures that $\begin{array} { r } { v ^ { \prime } ( \bar { q } _ { L } ^ { \ * } ) = \frac { \beta c } { \theta _ { L } - ( 1 - \beta ) \theta _ { H } } > 0 } \end{array}$ . Because v <sub>·</sub> is strictly concave and increasing, $v ^ { \prime } ( \cdot )$ is a strictly decreasing function, and the invers function of v exists and is also decreasing.

<sup>16</sup> In our main model, we assume that the CPs pay the same amount as an individual consumer when they sponsor data. In Online Appendix C, we provide additional discussions on the possible exten sion of allowing the MNO to treat the CPs differently.

<sup>17</sup> See https://money.cnn.com/2018/07/13/media/att-timewarner-appeal-comcast-fox/index.html?iid=EL (last accessed August 3, 2021).

<sup>18</sup> See https://www.theverge.com/2021/7/9/22570567/biden-netneutrality-competition-eo (last accessed August 3, 2021).

<sup>19</sup> See https://www.fcc.gov/document/fcc-releases-open-internetorder (last accessed August 3, 2021).

<sup>20</sup> See https://www.digitaltrends.com/music/spotify-vs-pandora/ (last accessed August 3, 2021).

## References

Andrews M, Ozen U, Reiman MI, Wang Q (2013) Economic models of sponsored content in wireless networks with uncertain demand. 2013 IEEE Conf. Comput. Comm. Workshops (INFOCOM WKSHPS) (IEEE, Piscataway), 345–350.

Arrow KJ (1985) The economics of agency. Principals and Agents: The Structure of Business (Harvard Business School Press, Boston) 37–51.

Asdemir K, Kumar N, Jacob VS (2012) Pricing models for online advertising: CPM vs. CPC. Inform. Systems Res. 23(3-part-1): 804–822.

Atamturk A, G¨ omez A (2017) Maximizing a class of utility functions´ over the vertices of a polytope. Oper. Res. 65(2):433–445.

AT&T (2018) AT&T completes acquisition of Time Warner Inc. Accessed August 3, 2021, https://about.att.com/story/att\_ completes\_acquisition\_of\_time\_warner\_inc.html.

Bapna R, Qiu L, Rice S (2017) Repeated interactions versus social ties: Quantifying the economic value of trust, forgiveness, and reputation using a <sup>fi</sup>eld experiment. MIS Quart. 41(3):841–866.

C¸anakoglu E,˘ Ozekici S (2010) Portfolio selection in stochastic<sup>¨</sup> markets with HARA utility functions. Eur. J. Oper. Res. 201(2):520–536.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Scj, 54(3):477–491

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Cheng HK, Fan W, Guo P, Huang H, Qiu L (2020) Can “gold med al” online sellers earn gold? The impact of reputation badge on sales. J. Management Inform. Systems 37(4):1099–1127.

Cho S, Qiu L, Bandyopadhyay S (2016) Should online content providers be allowed to subsidize content?—An economic analysis. Inform. Systems Res. 27(3):580–595.

Cho S, Qiu L, Bandyopadhyay S (2020) Vertical integration and zerorating interplay: An economic analysis of ad-supported and ad-free digital content. J. Management Inform. Systems 37(4):988–1014.

Choi JP, Kim BC (2010) Net neutrality and investment incentives. RAND J. Econom. 41(3):446–471.

Cisco (2019) Cisco visual networking index: Forecast and methodology. Cisco 2014–2019 White Paper, Cisco Systems, San Jose, CA.

Dellarocas C (2005) Reputation mechanism design in online trading environments with pure moral hazard. Inform. Systems Res. 16(2):209–230.

Dewan S, Hsu V (2004) Adverse selection in electronic markets: Evi dence from online stamp auctions. J. Indust. Econom. 52(4):497–516

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 32(3):395–426.

eMarketer (2018) Video swells to 25% of US digital ad spending. Accessed August 3, 2021, https://www.emarketer.com/content/ video-swells-to-25-of-us-digital-ad-spending.

Economides N, Hermalin B (2012) The economics of network neutrality. RAND J. Econom. 43(4):602–629.

Eisenhardt KM (1989) Agency theory: An assessment and review. Acad. Management Rev. 14(1):57–74.

FCC (2010) Preserving the open internet. GN Docket No. 09-191, WC Docket No. 07-52, Report and Order, 25 FCC Rcd 17905, 17910, para.13.

Gallaugher JM, Auger P, BarNir A (2001) Revenue streams and digital content providers: An empirical investigation. Inform. Man agement 38(7):473–485.

Gal-Or E, Gal-Or R, Penmetsa N (2018) The role of user privacy concerns in shaping competition among platforms. Inform. Systems Res. 29(3):698–722.

Gefen D, Karahanna E, Straub DW (2003) Trust and TAM in online shopping: An integrated model. MIS Quart. 27(1):51–90.

Ghose A (2009) Internet exchanges for used goods: An empirica analysis of trade patterns and adverse selection. MIS Quart. 33(2):263–291.

Grossman S, Hart O (1983) An analysis of the principal-agent prob lem. Econometrica 51(1):7–45.

Gryta T (2014) T-Mobile will waive data fees for music services. Wall Street Journal (June 18), http://www.wsj.com/articles/tmobile-will-waive-data-fees-for-music-service-1403142678.

Gryta T, Knutson R (2015) T-Mobile to offer free video streaming. Wall Street Journal (November 11), http://www.wsj.com articles/t-mobile-to-offer-free-video-streaming-1447187527.

Guo H, Easley RF (2016) Network neutrality versus paid prioritization: Analyzing the impact on content innovation. Production Oper. Management 25(7):1261–1273.

Guo H, Cheng HK, Bandyopadhyay S (2012) Net neutrality, broadband market coverage, and innovation at the edge. Decision Sci. 43(1):141–172.

Guo H, Cheng HK, Bandyopadhyay S (2013) Broadband network management and the net neutrality debate. Production Oper. Management 22(5):1287–1298.

Guo H, Bandyopadhyay S, Cheng HK, Yang YC (2010) Net neutrali ty and vertical integration of content and broadband services. J. Management Inform. Systems 27(2):243–276.

Guo H, Zhao X, Hao L, Liu D (2019) Economic analysis of reward advertising. Production Oper. Management 28(10):2413–2430.

Guo H, Bandyopadhyay S, Lim A, Yang Y, Cheng HK (2017) Effects of competition among internet service providers and content providers on the net neutrality debate. MIS Quart. 41(2):353–370.

Ha L, Ganahl R (2004) Webcasting business models of clicks-andbricks and pure-play media: A comparative study of leading webcasters in South Korea and the United States. Internat. J. Media Management 6(1-2):74–87.

Hande P, Chiang M, Calderbank R, Rangan S (2009) Network pricing and rate allocation with content provider participation. IN-FOCOM, IEEE (IEEE, Piscataway, NJ), 990–998.

Hong Y, Wang C, Pavlou PA (2015) Comparing open and sealed bid auctions: Evidence from online labor markets. Inform. Systems Res. 27(1):49–69.

Hu Y, Shin J, Tang Z (2015) Incentive problems in performancebased online advertising pricing: Cost per click vs. cost per action. Management Sci. 62(7):2022–2038.

Jin Y, Duf<sup>fi</sup>eld N, Gerber A, Haffner P, Hsu WL, Jacobson G, Sen S, Venkataraman S, Zhang ZL (2012) Characterizing data usage patterns in a large cellular network. Proc. 2012 ACM SIGCOMM Workshop Cellular Networks: Operations, Challenges, Future Design (ACM, New York), 7–12.

Joe-Wong C, Ha S, Chiang M (2015) Sponsoring mobile data: An economic analysis of the impact on users and content providers. 2015 IEEE Conf. Comput. Comm. (INFOCOM) (IEEE, Piscataway, NJ), 1499–1507.

Joe-Wong C, Sen S, Ha S (2018) Sponsoring mobile data: Analyzing the impact on internet stakeholders. IEEE/ACM Trans. Network 26(3):1179–1192.

Johnson GA, Shriver SK, Du S (2020) Consumer privacy choice in online advertising: Who opts out and at what cost to industry? Marketing Sci. 39(1):33–51.

Khurana S, Qiu L, Kumar S (2019) When a doctor knows, it shows: An empirical analysis of doctors’ responses in a Q&A forum of an online healthcare portal. Inform. Systems Res. 30(3):872–891.

Kramer J, Wiewiorra L (2012) Network neutrality and congestion¨ sensitive content providers: Implications for content variety, broadband investment, and regulation. Inform. Systems Res. 23(4):1303–1321.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Kwark Y, Lee GM, Pavlou PA, Qiu L (2021) On the spillover effects of online product reviews on purchases: Evidence from click stream data. Inform. Systems Res. 32(3):895–913.

Laffont JJ, Martimort D (2009) The Theory of Incentives: The Principal-Agent Model (Princeton University Press, Princeton, NJ).

Li S, Luo Q, Qiu L, Bandyopadhyay S (2020) Optimal pricing model of digital music: Subscription, ownership or mixed? Production Oper. Management 29(3):688–704.

Lu Y, Gupta A, Ketter W, Van Heck E (2019) Information transparency in business-to-business auction markets: The role of winner identity disclosure. Management Sci. 65(9): 4261–4279.

Ma RT (2014) Subsidization competition: Vitalizing the neutral internet. Proc. 10th ACM Internat. Conf. Emerging Networking Experi ments Tech. (ACM, New York), 283–294.

Matsumoto K (2006) Optimal portfolio of low liquid assets with a log-utility function. Finance Stochastics 10(1):121–145.

Milgrom P, Roberts J (1992) Economics, Organization and Management (Prentice Hall, NJ).

Montes R, Sand-Zantman W, Valletti T (2019) The value of personal information in online markets with endogenous privacy. Management Sci. 65(3):1342–1362.

Mudambi SM, Schuff D (2010) What makes a helpful online review? A study of customer reviews on amazon.com. MIS Quart. 34(1): 185–200.

Niculescu MF, Wu DJ, Xu L (2018) Strategic intellectual property sharing: Competition on an open technology platform under network effects. Inform. Systems Res. 29(2):498–519.

Pavlou PA (2003) Consumer acceptance of electronic commerce: In tegrating trust and risk with the technology acceptance model. Internat. J. Electronic Commerce 7(3):101–134.

Qiu L, Whinston AB (2017) Pricing strategies under behavioral observational learning in social networks. Production Oper. Man agement 26(7):1249–1267.

Qiu L, Chhikara A, Vakharia A (2021) Multidimensional observational learning in social networks: Theory and experimental evidence. Inform. Systems Res. 32(3):876–894.

Qiu L, Rui H, Whinston A (2019) Optimal auction design for WiFi procurement. Inform. Systems Res. 30(1):1–14.

Qiu L, Shi Z, Whinston AB (2018) Learning from your friends check-ins: An empirical study of location-based social networks. Inform. Systems Res. 29(4):1044–1061.

Ramsey C (2018) YouTube <sup>fi</sup>ghts off competition with expanded Premium subs service. Accessed August 3, 2021, https://www. tvbeurope.com/business/youtube-<sup>fi</sup>ghts-off-competition-withexpanded-premium-subs-service.

Rooney B (2015) Verizon buys AOL for \$4.4 billion. Accessed August 3, 2021, https://money.cnn.com/2015/05/12/investing/ verizon-buys-aol/index.html.

Ross SA (1973) The economic theory of agency: The principal’s problem. Amer. Econom. Rev. 63(2):134–139.

Spence M (1973) Job market signaling. Quart. J. Econom. 87(3): 355–374.

Van Schewick B (2016) T-Mobile’s Binge On Violates Key Net Neutralit Principles (Stanford Law School, The Center for Internet and Soci ety, Stanford, CA).

Wang H, Du R, Shen W, Qiu L, Fan W (2021) Product reviews: A bene<sup>fi</sup>t, a burden, or a tri<sup>fl</sup>e? How seller reputation affects the role of product reviews. MIS Quart. Forthcoming.

Ye HQ, Yao DD (2010) Utility-maximizing resource control: Diffu sion limit and asymptotic optimality for a two-bottleneck mod el. Oper. Res. 58(3):613–623.

Zhang L, Wang D (2014) Sponsoring content: Motivation and pitfalls for content service providers. 2014 IEEE Conf. Comput. Comm Workshops (INFOCOM WKSHPS) (IEEE, Piscataway, NJ), 577–582.

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
