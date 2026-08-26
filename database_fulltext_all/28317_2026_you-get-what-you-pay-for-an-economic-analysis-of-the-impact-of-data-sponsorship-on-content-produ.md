---
otero_id: 28317
otero_key: "A9VSG8GW"
title: "You Get What You Pay For! An Economic Analysis of the Impact of Data Sponsorship on Content Production"
authors: "Xin Wang; Chong (Alex) Wang; Liangfei Qiu; Xi Weng"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# You Get What You Pay For! An Economic Analysis of the Impact of Data Sponsorship on Content Production

Xin Wang,<sup>a</sup> Chong (Alex) Wang,<sup>b</sup> Liangfei Qiu,<sup>c</sup> Xi Weng<sup>a,</sup>\*

<sup>a</sup> Guanghua School of Management, Peking University, Beijing 100871, China; <sup>b</sup> Department of Information Systems, The College of Business, City University of Hong Kong, Hong Kong; <sup>c</sup>Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, Florida 32611

\*Corresponding author

Contact: 1901110926@pku.edu.cn, https://orcid.org/0000-0001-8083-1151 (XW); alex.wang@cityu.edu.hk, https://orcid.org/0000-0001-6243-7062 (C(A)W); liangfei.qiu@warrington.ufl.edu, https://orcid.org/0000-0002-8771-9389 (LQ); wengxi125@gsm.pku.edu.cn, https://orcid.org/0000-0001-8383-0461 (XW)

Received: January 4, 2022 Revised: October 12, 2022; August 6, 2023; July 26, 2024; December 16, 2024; February 4, 2025; May 7, 2025 Accepted: May 18, 2025 Published Online in Articles in Advance: June 10, 2025

https://doi.org/10.1287/isre.2022.0002

Copyright: © 2025 INFORMS

Abstract. The mechanism for data traffic pricing critically impacts the content provision decisions of data-intensive applications. We analyze the implications of sponsored data services on content quality, the profits of content providers (CPs) and Internet service providers (ISPs), consumer surplus, and social welfare using a game-theoretical model. By endogenizing CPs’ content quality decisions, our study reveals the critical role of content production efficiency in determining the optimal mechanism for ISPs’ data traffic pricing. When content production efficiency is low, allowing sponsored data services increases an ISP’s profit but adversely affects CPs by intensifying competition to subsidize consumers, consistent with prior studies. When content production efficiency is high, data sponsorship reduces the ISP’s profit but benefits CPs by dampening the intensity of competition in content production. Regarding consumer surplus and social welfare, when content production efficiency is sufficiently high, allowing only one CP to sponsor consumers maximizes consumer surplus and social welfare compared with scenarios with no data sponsorship or with both CPs allowed to sponsor consumers. As technology such as generative artificial intelligence tools enhances content production, ISPs and governments should re-evaluate data sponsorship programs.

Funding: This work was supported by National Natural Science Foundation of China [Grants 72131001, 72192843, 72192844, 72225001].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0002.

Keywords: data sponsorship • content quality • data traffic pricing • internet service provider • sponsored data services

## 1. Introduction

The data traffic of Internet service providers (ISPs) primarily comprises digital content, including streaming, video, and gaming applications. As ISPs deploy new generations of mobile network technologies, such as 5G, to open new frontiers for data-intensive services, they innovate data traffic pricing mechanisms to increase revenue (Qiu et al. 2019). One widely adopted mechanism is sponsored data services, first introduced in January 2014 by AT&T in the United States (Kumar and Qiu 2022). Sponsored data services allow content providers (CPs) to pay for the data traffic their users incur while consuming content. Data sponsorship effectively lowers the cost of content consumption, leading some to consider it a win for the millions of consumers who are reaping the benefits of services made available through free data programs. However, permitting CPs to subsidize user data traffic also alters the competition structure and incentives for content production, and whether sponsored data services are in the public interest remains a highly debated topic.

Previous theoretical analyses of sponsored data services primarily focus on their implications for data traffic regarding net neutrality.<sup>1</sup> These studies treat content quality as exogenous and focus on horizontal differentiation (e.g., Cho et al. 2016, Qiu et al. 2017, Cho et al. 2020, Mei et al. 2022). However, the dynamic and intense competition in the digital content market underscores the paramount importance of content quality differentiation. In video streaming services, high-quality, platform-generated content can, for instance, attract substantial user traffic while significantly boosting advertising revenue. Platforms are therefore compelled to invest heavily in content production. In 2022, global investment in digital content surged to \$238 billion (Ampere Analysis 2023), with Netflix dedicating a staggering \$14 billion budget to licensed and original content (Netflix 2022). The competition for exclusive, high-quality content is equally fierce among Chinese platforms such as Tencent and iQIYI (Xin 2021). These CPs’ strategic content provision decisions are critical to their competitiveness and directly influence ISPs’ pricing strategies. This illustrates the importance of considering investments in content quality alongside data sponsorship when evaluating the impact of sponsored data services.

This paper thus aims to comprehensively examine the interaction between data sponsorship and content creation within the digital content ecosystem. By endogenizing content creation decisions, this study represents a critical extension to previous theoretical analyses of sponsored data services. We base our analysis on Cho et al. (2016) while considering CPs’ content provision decisions as endogenous to ensure we remain conversant with the literature. As in Cho et al. (2016), our model adopts a Hotelling competition framework (Hotelling 1929) involving a monopolist ISP, two competing CPs, and a unit mass of consumers. In this framework, we define content quality as the value that content offers consumers (Fan et al. 2007, Johar et al. 2012, Berman and Katona 2020). CPs invest in content production to improve content quality, with more efficient production processes enabling CPs to produce digital content of a given quality at a lower cost.<sup>2</sup>

Our findings highlight the critical role of CPs’ content production efficiency in net neutrality discussions. Consistent with models assuming exogenous content quality (e.g., Cho et al. 2016), our model shows that when content production efficiency is low, one $\mathrm { C P ^ { \prime } s }$ data sponsorship adversely affects the market share and profit of another CP by intensifying competition to subsidize consumers. Conversely, a novel insight of our model is that when content production efficiency is high, one CP’s data sponsorship increases the profits of both CPs and the market share of the other CP, regardless of whether the other CP engages in data sponsoring. This outcome arises because sponsored data services shift the sponsoring CP’s focus (i.e., a CP sponsoring consumers’ data usage) from competing in content production to competing in data sponsorship, causing it to dramatically reduce its investment in content. Although the sponsoring CP loses market share due to diminished content quality, both CPs benefit from reduced competition intensity in content production at a high level of content production efficiency. Therefore, net neutrality policies that prohibit sponsored data services benefit nonsponsoring CPs (i.e., CPs not sponsoring consumers data usage) only when content production efficiency is low. As content production efficiency improves, these policies are increasingly perceived as less beneficial by nonsponsoring CPs due to the intensifying competition in content production.

Furthermore, our model suggests that the ISP’s optimal network management decision regarding whether to permit CPs’ data sponsorship depends on CPs’ content production efficiency. When efficiency is high, the ISP’s optimal choice is to not introduce sponsored data services. When efficiency is low, allowing both CPs to subsidize consumers maximizes the $\mathrm { I S P } ^ { \prime } \mathrm { s }$ profit. Although sponsored data services may appear beneficial for ISPs due to the additional revenue generated from charging $\mathrm { C P s , }$ our model indicates these services could reduce the ISP’s revenue by reducing consumer willingness to pay and diminishing content quality, particularly when content production efficiency is high. In such scenarios, the ISP is adversely affected by the CPs data sponsorship, as the reduction in revenue from consumers outweighs the additional revenue from CPs.

Additionally, our model investigates the impacts of sponsored data services on consumer surplus and social welfare. Compared with scenarios without data sponsorship, our findings reveal that allowing only one CP to subsidize consumers’ data usage leads to an increase in consumer surplus. However, when both CPs offer subsidies, consumer surplus remains unchanged because the ISP adjusts the data usage price to capture all the consumer benefits gained from data sponsorship. Thus, we propose that social planners adopt non-netneutral sponsored data services (i.e., allowing only one CP to sponsor consumers’ data usage) to maximize consumer surplus by restricting ISPs’ ability to extract these benefits. Second, we compare social welfare (the sum of consumer surplus and the profits of the two CPs and the ISP) across different cases. Our results show that, compared with a case without data sponsorship, allowing one CP to sponsor data improves social welfare only when content production efficiency is high, whereas allowing data sponsorship for both CPs always improves social welfare. Consistent with our findings on the profits of CPs, we find that when their content production efficiency is high, non-net-neutral sponsored data services maximize social welfare.

This research extends the theoretical literature on sponsored data services in several ways. First, our model delivers a comprehensive understanding of the interplay between quality investment and data sponsorship in sponsored data services by simultaneously considering CPs’ decisions on content provision and data sponsorship. The analysis reveals findings that contradict previous studies and highlights the crucial role of content production efficiency in reshaping competition among CPs and altering the welfare implications of sponsored data services when content production decisions are endogenized. Our study also extends the traditional literature on price–quality competition (Banker et al. 1998, Biglaiser and Ma 2003) by considering the context of the digital content market, where consumers pay for data traffic and ISPs govern the market by offering innovative pricing mechanisms. Finally, by analyzing the impacts of removing a pricing instrument (data sponsorship), we contribute to the literature on the competition between price and quality by revealing that these impacts depend on CPs’ content production efficiency.

While contextualized to the ISP-supported digital content market, our model analysis generates insights that apply broadly to IT ecosystems of interconnected technologies, services, and stakeholders collaborating to deliver digital products (Rausch et al. 2012). These ecosystems revolve around three key roles: infrastructure providers, service providers, and end users. Infrastructure providers, such as cloud platforms (e.g., AWS, Azure, Google Cloud) and telecom companies, supply foundational resources like storage, computing, and connectivity. Service providers, including SaaS platforms, software developers, and content providers (e.g., Netflix, Spotify), leverage this infrastructure to create and deliver digital services. End users, from individual consumers to enterprises, rely on these services for applications, platforms, and cloud-based solutions. In these ecosystems, infrastructure providers empower service providers to offer services that are essential for engaging and retaining users in today’s data-intensive digital landscape. Our model examines the interplay between data traffic pricing and data sponsorship, highlighting the critical role of content quality differentiation in sustaining user engagement within dataintensive ecosystems.

The remainder of this paper is arranged as follows. Section 2 reviews the literature that prompted our research. Section 3 details the model setup. Section 4 analyzes the equilibria of our model and discusses an ISP’s optimal network management choices. Section 5 assesses the impacts of sponsored data services on CP profits, consumer surplus, and social welfare. To illustrate the role of CPs’ endogenous content provision decisions, Section 6 compares our model predictions with those of Cho et al. (2016). Finally, Section 7 presents the conclusions from the results of our model and suggests future research directions.

## 2. Literature Review

Academic discourse on sponsored data services is rooted in the literature on net neutrality, a policy principle regarding the nondiscriminatory provision of Internet traffic (Wu 2003, Go´mez-Barroso and Feijo´o 2011). Initially, the literature focused on packet discrimination in ISP network management, where ISPs charge CPs for prioritizing data packet delivery, alongside the economic implications of net neutrality policies. Cheng et al. (2011) employed Hotelling’s (1929) competition framework to compare packet discrimination and net neutrality. In their model, two competing CPs provide horizontally differentiated content, which is delivered to consumers by a monopolist ISP. They found that packet discrimination always increases the ISP’s profit but also renders the CPs worse off than under a net neutrality scenario. Furthermore, Guo et al. (2010) found that an ISP vertically integrated with a CP always has an incentive to deviate from net neutrality. However, this does not necessarily degrade the packet delivery of the CP unaffiliated with the ISP. The net neutrality literature widely adopts the construct of a monopolist ISP (e.g., Choi and Kim 2010, Guo et al. 2010, Cheng et al. 2011, Kra¨mer and Wiewiorra 2012), with other studies examining the effects of ISP competition yielding results similar to those in monopoly models (e.g., Hermalin and Katz 2007, Economides and Ta˚ g 2012, Guo et al. 2017). For a broader review of this literature, see Schuett (2010), Faulhaber (2011), Kra¨mer et al. (2013), and Easley et al. (2018).

Stemming from the net neutrality discussion, theoretical discussions on sponsored data services focus on the economic implications of net neutrality requirements. Cho et al. (2016) pioneered this discussion by adopting the analysis framework of Cheng et al. (2011). They studied the impacts of sponsored data services and found that an ISP’s optimal network management choice regarding data sponsorship is contingent on the advertising revenue rates of CPs and the fit costs of consumers. In Cho et al.’s (2016) model, sponsored data services force competition among CPs to subsidize consumers’ data usage; without the resources to support consumers, the CP loses market share to its rival and experiences reduced revenue. Several studies extended this analysis. Qiu et al. (2017) considered a nonlinear data usage pricing scheme with data caps and found that an ISP always benefits from sponsored data services under such a scheme, regardless of market conditions. Cho et al. (2020) examined the simultaneous impacts of vertical integration and data sponsorship, showing that the consumer valuation of ad-free content significantly affects how an ISP maximizes its profit. According to Mei et al.’s (2022) analysis, the impact of sponsored data services on consumer surplus crucially depends on whether the ISP has complete information on consumer types. Other recent studies have further examined the optimal strategies of ISPs for providing sponsored data services in various contexts (Jullien and Sand-Zantman 2018, Inceoglu and Liu 2019, Gautier and Somogyi 2020, Hoernig and Monteiro 2020, Wang et al. 2021).

Previous studies on data sponsorship focus on the competition for traffic between CPs through consumers data usage subsidization, without a focus on quality and treating content provision decisions as exogenous (e.g., Cho et al. 2016, Qiu et al. 2017, Cho et al. 2020, Gautier and Somogyi 2020, Wang et al. 2021, Mei et al. 2022). Since CP decisions on data sponsorship and service quality are crucial to market competition, we model sponsorship and quality competition simultaneously.

This allows our analysis to reveal novel insights into ISPs’ optimal network management choices and social planners’ potential regulatory strategies. Comparing our model predictions with those of Cho et al. (2016) reveals the importance of CPs’ endogenous content provision decisions in the theoretical analysis of data sponsorship (see Section 6). Although the results of our model mirror those of Cho et al. (2016) when CP content production efficiency is low, they diverge significantly when content production efficiency is high.

This study also contributes to the academic literature on price–quality competition (e.g., Ma and Burgess 1993, Biglaiser and Ma 2003, Laine and Ma 2017, Pu et al. 2022) by considering content quality competition as a factor in the market implications of sponsored data services. Spence (1975) demonstrated that a profitmaximizing firm should determine its quality level based on its impact on the marginal consumer’s willingness to pay. Subsequent studies have examined the interplay between quality and price competition, showing that high quality is often associated with high prices (Moorthy 1988, Barua et al. 1991). Moreover, quality differentiation can increase profits by mitigating price competition (Shaked and Sutton 1982, 1983; Matsubayashi 2007). Our study extends this classical discussion to a new context, where data sponsorship can be regarded as regulated price competition. In the digital content market, the profit of a CP primarily depends on traffic (market share) rather than direct payment from consumers, while its pricing power is regulated by the ISP, which determines the Internet access fee and whether sponsorship is allowed. We find that allowing CPs to compete on sponsorship can reduce the intensity of their quality competition, aligning with key insights from price–quality competition research. Our results also demonstrate that content production efficiency is crucial in determining ISPs’ optimal strategies.

## 3. Model Setup

To understand the impact of sponsored data services on the competition among CPs, we analyze a multistage game-theoretical model and derive its subgame perfect Nash equilibrium (SPNE) via backward induction. The model consists of three player types: (1) a monopolist ISP that delivers content from CPs to consumers by providing Internet access, (2) two competing CPs that provide consumers with free content services and generate revenue from advertising, and (3) a unit mass of consumers who use CP content services through the Internet access provided by the ISP.

The literature on sponsored data services (Cho et al. 2016, 2020) widely adopts the monopolistic ISP assumption, which aligns with the institutional context of the United States, where the wireless services market is highly concentrated. By the end of 2016, AT&T and

Verizon controlled approximately 70% of the US market, with very low quarterly churn rates of 1.7% and 1.3%, respectively (Federal Communications Commission 2017). Accordingly, many regional markets in the United States are dominated by a single ISP, and even where multiple ISPs exist, they often operate as local monopolies due to low churn (Mei et al. 2022). Similarly, the US cable service market is dominated by large ISPs (e.g., Comcast, Charter, and AT&T), and in 2019, over 83.3 million Americans could only access broadband through a single ISP (Mitchell and Kienbaum 2020).

Table 1 lists the notations in our model. The remainder of this section describes the consumers, CPs, ISP, and the game sequence employed in this model.

## 3.1. Consumers

Our model incorporates a unit mass of consumers who are heterogeneous in their content preferences. Following Hotelling (1929), consumers are uniformly distributed in the interval [0; 1], with consumer locations representing their ideal content. The two competing CPs, A and B, are located at 0 and 1, respectively. Each consumer consumes digital content from either of the CPs and incurs a fit cost proportional to the distance between their ideal content and the chosen CP. Let t denote the unit fit cost. A consumer located at x ∈ [0; 1] incurs a fit cost of xt from consuming CP A’s content and (1 � x)t from consuming CP B’s content. For analytical tractability, we assume single-homing consumption of one CP for each consumer (Guo et al. 2010, Kra¨mer and Wiewiorra 2012, Guo et al. 2017, Mei et al. 2022).

Consumers pay the ISP to access digital content via the Internet. We assume that the ISP charges a usagebased per-packet price p to consumers (Choi and Kim 2010, Kra¨mer and Wiewiorra 2012, Cho et al. 2016). Each consumer uses 1 unit of data packets and pays an Internet access fee p to the ISP. The assumption of a fixed amount of data usage is reasonable in certain scenarios. For example, the time spent and data traffic consumption for watching a movie do not vary based on quality. In other scenarios, consumers can decide their data usage endogenously by directing it to the consumption of higher-quality content. For instance, the data usage of users of an online gaming platform increases with content quality (i.e., they spend more time playing a highquality game than a low-quality one). In Online Appendix C, we relax the assumption of fixed data usage and consider the case where consumers can endogenously choose their data usage. In the equilibrium of this exten sion, consumers’ data usage with a CP increases with the CP’s content quality and data sponsorship, while it decreases with the ISP’s data usage price. Most model predictions from the main model remain robust under this extension, according to the numerical analysis.

The ISP may offer a sponsored data service, allowing the CPs to pay for part of the data traffic consumers incur when accessing their content. To track whether the ISP allows CP i (i � A or B) to subsidize consumers data usage, we introduce an indicator function, $I _ { \mathrm { i } } ,$ which is set to 1 if the ISP allows CP i to sponsor consumers and 0 otherwise. Under a sponsored data service $( I _ { \mathrm { i } } = 1 )$ , CP i chooses an amount of data sponsorship $s _ { \mathrm { i } }$ such that a consumer’s Internet access fee within this amount (incurred using CP i’s content services) is charged to CP i. Consequently, the Internet access fee charged to each of CP i’s customers falls by $I _ { \mathrm { i } } s _ { \mathrm { i } }$ . Additionally, we allow $s _ { \mathrm { i } } > p ,$ meaning that CPs can offer consumers benefits beyond reimbursing Internet access fees.

Table 1. Notations

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>ISP</td><td>Internet service provider</td></tr><tr><td>p</td><td>The usage-based price per packet charged to consumers</td></tr><tr><td> $\pi_{\text{ISP}}$ </td><td>The ISP&#x27;s profit</td></tr><tr><td>CP</td><td>Content provider: there are two competing content providers, A and B, each located at one end of the interval [0,1]</td></tr><tr><td> $\pi_i$ </td><td>CP i&#x27;s profit, i = A or B</td></tr><tr><td> $I_i$ </td><td>A function that indicates whether the ISP allows CP i to sponsor consumers</td></tr><tr><td> $s_i$ </td><td>Amount of data sponsorship paid by CP i</td></tr><tr><td> $D_i$ </td><td>Demand for CP i</td></tr><tr><td> $V_i$ </td><td>Content quality: the gross value of CP i&#x27;s online content</td></tr><tr><td>C(V)</td><td>Cost of producing content services with quality V</td></tr><tr><td>t</td><td>Unit fit cost</td></tr><tr><td> $\phi$ </td><td>A parameter that characterizes CPs&#x27; content production efficiency</td></tr><tr><td>r</td><td>CPs&#x27; marginal revenue from a unit of data traffic</td></tr><tr><td>x ∈ [0,1]</td><td>Consumer preference: consumer x receives a utility  $V_A - xt$  from CP A&#x27;s content (located at 0) or  $V_B - (1 - x)t$  from CP B&#x27;s content (located at 1)</td></tr><tr><td> $x_m$ </td><td>The preference of a marginal consumer who is indifferent between CPs A and B</td></tr><tr><td>CS</td><td>Consumer surplus</td></tr><tr><td>SW</td><td>Social welfare</td></tr></table>

Note. Parametric assumptions: $\begin{array} { r } { r \in \left[ 2 \phi t ^ { 2 } , 4 \phi t ^ { 2 } \right] , \phi > \frac { 1 } { 4 t } . } \end{array}$

From CP i’s content services, a consumer can obtain a gross value, V<sub>i</sub> $( i = \mathrm { A } \ \mathrm { o r } \ \mathrm { B } ) .$ , that reflects the quality of these services (Fan et al. 2007, Johar et al. 2012, Berman and Katona 2020). Consumers decide which content to consume based on the utility they derive, consisting of four parts: the gross value of the consumed content, the fit cost incurred from the difference between the consumer’s ideal and consumed content, the Internet access fee, and the data sponsorship. Formally, the utility derived by a consumer at location $x \in [ 0 , 1 ]$ from retrieving content from CPs A and B is represented as follows:

$$
U _ {\mathrm{A}} (x) = V _ {\mathrm{A}} - t x - p + I _ {\mathrm{A}} s _ {\mathrm{A}},\tag{1}
$$

$$
U _ {\mathrm{B}} (x) = V _ {\mathrm{B}} - t (1 - x) - p + I _ {\mathrm{B}} s _ {\mathrm{B}}.\tag{2}
$$

## 3.2. Content Providers

The two competing CPs offer free-to-access, horizontally differentiated content of quality $V _ { \mathrm { { A } } }$ and $V _ { \mathrm { { B } } }$ to consumers. A CP’s profit consists of three parts: advertising revenue, the cost of content production, and the cost of data sponsorship.

First, the advertising revenue model is prevalent among CPs—such as YouTube, HBO Max, and iQIYI.

Following prior literature, the CPs earn advertising revenue proportional to the data traffic generated by their consumers (Choi and Kim 2010, Guo et al. 2010, Cheng et al. 2011, Kra¨mer and Wiewiorra 2012, Cho et al. 2016, Guo et al. 2017, Qiu et al. 2017, Cho et al. 2020, Mei et al. 2022). Let r denote the CPs’ advertising revenue rate per data packet.

Second, CPs invest in content quality. Producing content services of quality V incurs the production cost $C ( V ) = { \frac { \phi } { 2 } } V ^ { 2 }$ . φ characterizes content production effi ciency, where a lower $\phi$ implies a more efficient produc tion process that allows CPs to produce digital content of a given quality at a lower cost. The quadratic cost function of content production captures the fact that quality improvement becomes more costly as quality increases—a commonly adopted assumption in the literature (Moorthy 1988, Barua et al. 1991, Moorthy and Png 1992, Thatcher and Pingry 2004). To avoid the trivial case where CPs over-invest in content production and produce content of infinitely high quality, we assume that $\begin{array} { r } { \phi > \frac { 1 } { 4 t } } \end{array}$ (please refer to footnote 4).

Third, if the ISP allows CP i (i �A or B) to subsidize consumers’ data usage $( I _ { \mathrm { i } } = 1 )$ , then CP i determines the amount of data sponsorship, $s _ { \mathrm { i } } ,$ , per consumer, paying the same per-packet price, $p ,$ to the ISP as consumers pay (Cho et al. 2016, Qiu et al. 2017, Cho et al. 2020, Mei et al. 2022).

Given the per-packet price $p$ for data traffic and the ISP’s choice of $I _ { \mathrm { i } } ,$ CP i’s profit function is thus formu lated as follows:

$$
\pi_ {\mathrm{i}} = r D _ {\mathrm{i}} - \frac {\phi}{2} V _ {\mathrm{i}} ^ {2} - I _ {\mathrm{i}} s _ {\mathrm{i}} D _ {\mathrm{i}},\tag{3}
$$

where $D _ { \mathrm { i } }$ is the demand for CP i. We assume that $r \leq$ $4 \phi t ^ { 2 }$ to ensure that CPs receive nonnegative profits in equilibrium (please refer to footnote 3).

## 3.3. Internet Service Provider

The ISP decides on (1) whether to allow CPs to subsidize consumers’ data usage (i.e., the values of $I _ { \mathrm { A } }$ and I ) and (2) the per-packet price p for data traffic. We assume that the ISP covers the entire market and delivers content to consumers at a negligible cost (Cheng et al. 2011, Cho et al. 2016). Under this assumption, the ISP’s profit is $\pi _ { \mathrm { I S P } } = p$ . The full market coverage assumptions are widely used in research employing the Hotelling model (Armstrong 2006, Nasser and Turcic 2015, Kourandi et al. 2016). Under this assumption, consumers’ choices are represented by a cutoff rule: a consumer located in $[ 0 , x _ { \mathrm { m } } ]$ chooses CP A, while one in $[ x _ { \mathrm { m } } , 1 ]$ chooses CP B, where $x _ { \mathrm { m } }$ is the location of the marginal consumer indifferent about choosing between CPs A and B. Hence, the demands for CPs A and B in Equation (3) are $D _ { \mathrm { { A } } } = x _ { \mathrm { { m } } }$ and $D _ { \mathrm { B } } = 1 - x _ { \mathrm { m . } }$ , respectively.

Since the marginal consumer $x _ { \mathrm { m } }$ receives the lowest utility among all consumers, the sufficient and necessary condition for full market coverage is $U _ { \mathrm { A } } ( x _ { \mathrm { m } } ) =$ $U _ { \mathrm { B } } ( x _ { \mathrm { m } } ) \geq 0$ . Hence, the $\mathrm { I S P ^ { \prime } s }$ profit maximization problem can be formulated as follows:

$$
\max _ {p, I _ {\mathrm{A}}, I _ {\mathrm{B}}} \pi_ {\mathrm{ISP}} = p\tag{4}
$$

$$
s. t. U _ {\mathrm{A}} (x _ {\mathrm{m}}) = U _ {\mathrm{B}} (x _ {\mathrm{m}}) \geq 0.\tag{5}
$$

To ensure that the ISP’s optimal strategy is to cover the entire market in equilibrium, we assume $r \geq 2 \phi t ^ { 2 }$ (please refer to footnote 3). This assumption requires the marginal advertising revenue is not too low compared with content production and fit costs. In Online Appendix D, we relax this assumption and discuss an extension in which ISP covers the market partially. The main model’s major predictions remain consistent.

To assess and assure the robustness of the model predictions, we have analyzed various extensions to the main model, including multihoming consumers, consumer annoyance from advertisements, network effect, heterogeneity in content production efficiency, consumers’ vertical heterogeneity, subscription-based revenue models, and ISP’s price discrimination. The detailed analysis and results of these other extensions are available upon request.

## 3.4. Game Sequence

In this model, the ISP, CPs A and B, and consumers make decisions independently to maximize utility or profits in the following sequence:

• In stage 1, the ISP chooses a network management option, among three alternative scenarios: allowing no CP to sponsor consumers, allowing either CP A or B to sponsor consumers, or allowing both CPs to sponsor consumers.

• In stage 2, depending on the ISP’s network management choice in stage 1, the ISP announces the perpacket price p to the end consumers, while CPs A and

B decide the quality of their content services $( V _ { A }$ and $V _ { B } )$ and the amount of data sponsorship per consumer $( s _ { \mathrm { A } }$ and s ).

• In stage 3, each consumer chooses to consume content from either CP A or CP B.

As shown in Figure 1, this sequence describes a multistage game with perfect information. We obtain the SPNE of this game via backward induction, as described in the following section.

## 4. Equilibrium Analysis

In this section, we employ backward induction to determine the SPNE of our model, with detailed proofs provided in Online Appendix A. The $\mathrm { I S P } ^ { \prime } \mathrm { s }$ network management choices in stage 1 yield the following three subgames:

Subgame N: Neither CP is allowed to sponsor data traffic.

Subgame S: Only one CP is allowed to sponsor data traffic.

Subgame SS: Both CPs are allowed to sponsor data traffic.

In Sections 4.1–4.3, we analyze the equilibria under different subgames, respectively. In Section 4.4, we compare the ISP’s profits across the derived equilibria of different subgames to determine the SPNE.

## 4.1. No Data Sponsorship (Subgame N)

Lemma 1 summarizes the equilibrium of subgame N, where no CP is permitted to subsidize consumer data usage $( I _ { \mathrm { A } } = I _ { \mathrm { B } } = 0 )$

Lemma 1 (Equilibrium of Subgame N). In the equilibrium without data sponsorship, the optimal per-packet price set by the ISP is $\begin{array} { r } { p ^ { * } = \frac { r } { 2 \phi t } - \frac { \dot { t } } { 2 } ; } \end{array}$ the CPs’ optimal content quality decisions are $\begin{array} { r } { V _ { A } ^ { * } = \dot { V } _ { B } ^ { * } = \frac { r } { 2 \phi t } , } \end{array}$ , and the equilibrium marginal consumer is $\begin{array} { r } { x _ { m } ^ { * } = \frac { 1 } { 2 } . } \end{array}$

Lemma 1 demonstrates that the optimal content quality decision for a CP that does not provide data sponsorship is $\begin{array} { r } { V ^ { \ast } = \frac { r } { 2 \phi t } . } \end{array}$ . At the optimal content quality $\ h ^ { * }$ , the marginal revenue of content production ( <sup>r</sup> ) equals to the marginal production cost $( \frac { d C ( V ^ { * } ) } { d V } = \phi V ^ { * } )$ ). V<sup>∗</sup> increases with the advertising revenue rate r and decreases with content production efficiency φ. When the advertising revenue rate r is higher, an increase in market share yields greater profits for CPs, motivating them to produce higher-quality content to compete for market share. Meanwhile, a low level of efficiency in content production (i.e., a higher φ) discourages a CP from increasing the quality of its content.<sup>3</sup>

## 4.2. Only One CP Sponsors Consumers (Subgame S)

We analyze the equilibrium of subgame S, where only one CP is allowed to sponsor data traffic. Without loss of generality, suppose that only CP A can sponsor consumers $( I _ { \mathrm { A } } { \overset { \cdot } { = } } 1$ and $I _ { \mathrm { B } } = 0 )$ . Under the assumption that $2 \phi t ^ { 2 } \le r \le 4 \phi t ^ { 2 }$ and $\begin{array} { r } { \phi > \frac { 1 } { 4 t } , } \end{array}$ , Lemmas 2 and 3 characterize CP A’s optimal content quality decision and optimal data sponsorship decision, respectively.<sup>4</sup>

Figure 1. Game Sequence  
![](/api/attachments/A9VSG8GW/fulltext/images/060f1c8b70f455b2d1535d7a09cdf115b648304c62932001d44d6351c36fec28.jpg)

Lemma 2. In the equilibrium of subgame $S ,$ given the amount of data sponsorship per consumer s from CP A, CP A’s optimal content quality decision is $\begin{array} { r } { V _ { A } ^ { * } = \frac { r - s _ { A } } { 2 \phi t } } \end{array}$ , and CP B’s optimal content quality decision is $\begin{array} { r } { V _ { B } ^ { * } = \frac { r } { 2 \phi t } . } \end{array}$

Lemma 2 demonstrates that sponsored data services incentivize CP A (the sponsoring CP) to reduce its investment in content quality and that a larger amount of data sponsorship (i.e., a higher $s _ { \mathrm { A } } )$ leads to lowerquality content services. Since sponsored data services use a proportion of CP A’s advertising revenue to subsidize consumers’ data usage, an increase in market share reduces profitability for CP A compared with subgame N. Therefore, CP A reduces its content quality to obtain a lower marginal production cost after engaging in sponsored data services. If $s _ { \mathrm { A } } = 0 ,$ , we derive CPs’ optimal content quality decisions $\begin{array} { r } { V _ { \mathrm { A } } ^ { * } = V _ { B } ^ { * } = \frac { r } { 2 \phi t } } \end{array}$ from Lemma 2, consistent with Lemma 1.

Lemma 3. In the equilibrium of subgame S, CP A’s optimal data sponsorship decision $( i . { \dot { e } } . , s _ { A } ^ { * } )$ is as follows:

1. When $r \leq t ,$ the CP ignores the sponsoring option such that $s _ { A } ^ { * } = 0 ;$

2. When $r > t ,$ the CP subsidizes consumers’ data usage such that $s _ { A } ^ { * } > 0$

Lemma 3 demonstrates that $\mathrm { a C P ^ { \prime } s }$ decision to subsidize consumers depends on the advertising revenue rate r. When this rate is low $( \mathrm { i } . \mathrm { e } . , r \le t )$ , an increase in market share from data sponsorship does not generate sufficient revenue to cover the cost of such sponsorship, hence CP A ignores the sponsoring option. In this case, the equilibrium reverts to that of subgame N. Therefore,

CP A sponsors its consumers only when the advertising revenue rate is sufficiently high $( \mathrm { i } . \mathrm { e } . , r > t )$

Based on Lemmas 2 and 3, Lemma 4 summarizes the equilibrium of subgame S.

Lemma 4 (Equilibrium of Subgame S). Table 2 summarize the equilibrium of subgame S, where only CP A can sponsor consumers’ data usage.

By comparing CP A’s equilibrium market share $x _ { \mathrm { m } } ^ { \ast }$ in subgame S with that in subgame N, we arrive at a counterintuitive finding: subsidizing consumer data usage does not necessarily increase CP A’s market share—it could even decrease it. We characterize this result in Lemma 5.

Lemma 5. In the equilibrium of subgame S, subsidizing consumer data usage decreases CP A’s market share if its content production efficiency is high $\begin{array} { r } { ( i . e . , \phi < \frac { 1 } { 2 t } ) ; } \end{array}$ otherwise (when $\begin{array} { r } { \phi \geq \frac { 1 } { 2 t } ) } \end{array}$ , it increases CP A’s market share

Although subsidizing consumers’ data usage appears to increase a sponsoring CP’s market share—as consumers prefer sponsored over unsponsored content— Lemma 5 demonstrates that the opposite result can occur under certain conditions. Figures 2 and 3 illustrate the rationale behind Lemma $5 . ^ { 5 }$ Lemmas 1 and 2 hold that CP A decreases its content quality, $V _ { \mathrm { A } } ,$ , by $\frac { s _ { \mathrm { A } } } { 2 \phi t }$ according to the amount of data sponsorship $s _ { \mathrm { A } }$ and that this decrease is negatively associated with φ. When content production efficiency is high $\begin{array} { r } { ( \mathrm { i . e . , } \phi < \frac { 1 } { 2 t } ) . } \end{array}$ , competition in content production is intense.<sup>6</sup> The data sponsorship option thus redirects CP A’s focus to competition over consumer subsidization, reducing investments to improve content quality. Since the fall in CP $\mathrm { A } ^ { \prime } \mathrm { s }$ content quality (i.e., $\begin{array} { r } { V _ { \mathrm { A } } ^ { \mathrm { \Delta V } } - V _ { \mathrm { A } } ^ { \bar { \mathrm { S } } } = \frac { s _ { \mathrm { A } } } { 2 \phi t } ) } \end{array}$ is greater than the value of its data sponsorship $( \mathrm { i } . \mathrm { e } . , s _ { \mathrm { A } } )$ , it loses market share to CP $\mathsf { B } ( \mathrm { i . e . , } x _ { \mathrm { m } } ^ { \bar { S } } \leq x _ { \mathrm { m } } ^ { \mathrm { N } } )$ . In contrast, when content production efficiency is low $\begin{array} { r } { ( \mathrm { i . e . , ~ } \phi \geq \frac { 1 } { 2 t } ) } \end{array}$ , this content

max $\{ V _ { \mathrm { A } } + s _ { \mathrm { A } } - t x , V _ { \mathrm { B } } + s _ { \mathrm { B } } - t ( 1 - x ) \}$

Table 2. Equilibrium of Subgame S

<table><tr><td>Assumptions</td><td colspan="5"> $2\phi t^{2} \leq r \leq 4\phi t^{2}$  and  $\phi > \frac{1}{4t}$ </td></tr><tr><td>Market conditions</td><td>Per-packet price  $p^{*}$ </td><td>CP A&#x27;s content quality decision  $V_{A}^{*}$ </td><td>CP A&#x27;s data sponsorship decision  $s_{A}^{*}$ </td><td>CP B&#x27;s content quality decision  $V_{B}^{*}$ </td><td>Marginal consumer  $x_{m}^{*}$ </td></tr><tr><td> $r \leq t$ </td><td> $\frac{r}{2\phi t} - \frac{t}{2}$ </td><td> $\frac{r}{2\phi t}$ </td><td>0</td><td> $\frac{r}{2\phi t}$ </td><td> $\frac{1}{2}$ </td></tr><tr><td> $r > t$ </td><td> $\frac{-3\phi t^{2} + t + \phi tr + \frac{3}{2}r - \frac{r}{2t\phi}}{4\phi t - 1}$ </td><td> $\frac{r + t - \frac{r}{2\phi t}}{4\phi t - 1}$ </td><td> $\frac{2\phi t(r - t)}{4\phi t - 1}$ </td><td> $\frac{r}{2\phi t}$ </td><td> $\frac{-r + 2\phi tr + 2\phi t^{2}}{2t(4\phi t - 1)}$ </td></tr></table>

production competition is less intense. Data sponsorship thus leads CP A to compete more intensely for market share.<sup>7</sup> CP A in subgame S thus provides sufficient data sponsorship to offset the decrease in its content quality (i.e., $\begin{array} { r } { s _ { \mathrm { A } } \overset { \mathrm { ^ { \circ } } } { \geq } V _ { \mathrm { A } } ^ { \mathrm { N } } - V _ { \mathrm { A } } ^ { \mathrm { S } } = \frac { s _ { \mathrm { A } } } { 2 \phi t } ) } \end{array}$ , enabling it to expand its market share $( \mathrm { i . e . , } x _ { \mathrm { m } } ^ { \mathrm { S } } \geq x _ { \mathrm { m } } ^ { \mathrm { N } } )$

Lemma 6 (Equilibrium of Subgame SS). Table 3 summarizes the equilibrium of subgame SS, where both CPs can subsidize consumers’ data usage.

## 4.3. Both CPs Sponsor Consumers (Subgame SS)

In the equilibrium of subgame SS summarized in Lemma $^ { 6 , }$ since the CPs are homogeneous in their advertising revenue rate r and content production efficiency $\phi ,$ they make symmetrical decisions about content quality and data sponsorship. Consistent with Lemmas 2 and $^ { 3 , }$ both CPs sponsor their consumers only when $r > t ;$ and data sponsorship $s _ { \mathrm { i } } ^ { * }$ reduces CP i’s content quality from $\frac { r } { 2 { \phi } t }$ to $V _ { \mathrm { i } } ^ { * } = \frac { r - s _ { \mathrm { i } } ^ { * } } { 2 \phi t }$ compared with subgame N. To reveal the impact of CP B’s data sponsorship on market competition under the condition $r > t ,$ , we compare CP A’s equilibrium decisions $( s _ { \mathrm { A } } ^ { \ast }$ and $V _ { \mathrm { A } } ^ { * } )$ in subgame SS to those in subgame S. When content production efficiency is low $\begin{array} { r } { ( \mathrm { i . e . , } \phi \geq \frac { 1 } { 2 t } ) } \end{array}$ , allowing CP B to sponsor consumers causes CP A to rely more heavily on data sponsorship. Compared with subgame S, CP A provides more data sponsorship $( \mathrm { i . e . } , s _ { \mathrm { A } } ^ { \mathrm { S S } } \geq s _ { \mathrm { A } } ^ { \mathrm { S } } )$ and reduces its content quality $( \mathrm { i . e . , }$ $V _ { \mathrm { A } } ^ { \mathrm { S S } } \leq V _ { \mathrm { A } } ^ { \mathrm { S } } )$ ). Conversely, when content production efficiency is high $\begin{array} { r } { ( \mathrm { i . e . , } \phi < \frac { 1 } { 2 t } ) } \end{array}$ , allowing CP B to sponsor consumers incentivizes CP A to allocate more resources to content production. In this case, compared with subgame S, CP A increases its content quality (i.e., $V _ { \mathrm { A } } ^ { \mathrm { S S } } \geq V _ { \mathrm { A } } ^ { \mathrm { S } } )$ ) and provides less data sponsorship $( \mathrm { i . e . } , s _ { \mathrm { A } } ^ { \mathrm { S S } } \leq s _ { \mathrm { A } } ^ { \mathrm { S } } )$

Figure 2. (Color online) Comparison of CP A’s Equilibrium Market Shares $( x _ { \mathrm { m } } ^ { \ast } )$ in Subgames N and S When $\phi \overset { - } { \leq } \frac { 1 } { 2 t }$  
![](/api/attachments/A9VSG8GW/fulltext/images/7569246418d87a4c80526a47087ead3f7da314bb91a0656c3b0ff116a3743351.jpg)  
Figure 3. (Color online) Comparison of CP A’s Equilibrium Market Shares $( x _ { \mathrm { m } } ^ { \ast } )$ in Subgames N and S When φ $> \frac { 1 } { 2 t }$  
max $\{ V _ { \mathrm { A } } + s _ { \mathrm { A } } - t x , V _ { \mathrm { B } } + s _ { \mathrm { B } } - t ( 1 - x ) \}$

## 4.4. Subgame Perfect Nash Equilibrium

In this section, we determine the ISP’s optimal network management choice to characterize the SPNE, building on the derived equilibria conditional on the $\mathrm { I S P ^ { \prime } s }$ network management choices. We impose the assumption $2 \phi t ^ { 2 } \le r \le 4 \phi t ^ { 2 }$ and $\begin{array} { r } { \phi > \frac { 1 } { 4 t } } \end{array}$ to guarantee fully-covered equilibrium existence and avoid trivial cases in all three subgames. According to Lemma $^ { 3 , }$ when $r \leq t ,$ the low revenue rate r encourages CPs to ignore the sponsoring options, making the decision of whether to allow data sponsorship irrelevant to the equilibrium results. To avoid this trivial case, we focus on the scenario where $r > t$ in subsequent analyses. We then compare the ISP’s equilibrium profits under different network management choices to derive the SPNE, which is summarized in Proposition 1.

![](/api/attachments/A9VSG8GW/fulltext/images/34be30b66059a5e8e98f5c05774806ef61b7e4628adaa5447541164cd696a869.jpg)

Table 3. Equilibrium of Subgame SS

<table><tr><td>Assumptions</td><td colspan="4"> $2\phi t^{2} \leq r \leq 4\phi t^{2}$  and  $\phi > \frac{1}{4t}$ </td></tr><tr><td>Market conditions</td><td>Per-packet price  $p^{*}$ </td><td>CPs&#x27; content quality decisions  $V_{\mathrm{A}}^{*}(=V_{\mathrm{B}}^{*})$ </td><td>CPs&#x27; data sponsorship decisions  $s_{\mathrm{A}}^{*}(=s_{\mathrm{B}}^{*})$ </td><td>Marginal consumer  $x_{\mathrm{m}}^{*}$ </td></tr><tr><td> $r \leq t$ </td><td> $\frac{r}{2\phi t}-\frac{t}{2}$ </td><td> $\frac{r}{2\phi t}$ </td><td>0</td><td> $\frac{1}{2}$ </td></tr><tr><td> $r > t$ </td><td> $\frac{1}{2\phi}+r-\frac{3t}{2}$ </td><td> $\frac{1}{2\phi}$ </td><td> $r-t$ </td><td> $\frac{1}{2}$ </td></tr></table>

Proposition 1 (ISP’s Optimal Network Management Choice). In the SPNE,

1. When CPs’ content production efficiency is high (i.e., $\begin{array} { r } { \phi < \frac { 1 } { 2 t } ) . } \end{array}$ , the ISP suffers from the CPs’ data sponsorship, and its optimal network management choice is to not introduce sponsored data services $( i . e . , \pi _ { I S P } ^ { N } > \pi _ { I S P } ^ { S }$ and $\pi _ { I S P } ^ { N } > \pi _ { I S P } ^ { S S } ) ,$ ;

2. When CPs’ content production efficiency is low $( i . e . ,$ $\begin{array} { r } { \phi > \frac { 1 } { 2 t } ) . } \end{array}$ , the ISP benefits from the $C P s ^ { \prime }$ data sponsorship, and its optimal network management choice is to allow both CPs to subsidize consumers’ data usage $( i . e . , \pi _ { I S P } ^ { N } < \pi _ { I S P } ^ { S } < \pi _ { I S P } ^ { S S } )$

Figures 2 and 3 illustrate the rationale behind Proposition 1, which is explained by analyzing whether the ISP should allow CP A to sponsor consumers in comparison with subgame N. Under the assumption of full market coverage, the ISP’s profit π<sub>ISP</sub> equals the data usage price p. Meanwhile, the optimal price $p ^ { * }$ (i.e., the highest p) should allow the marginal consumer to obtain zero utility $( { \mathrm { i . e . , ~ } } p ^ { \ast } = V _ { \mathrm { A } } + s _ { \mathrm { A } } - t { \overset { \sim } { x } } { \mathrm { m } } = V _ { \mathrm { B } } + s _ { \mathrm { B } } - t ( 1 - x _ { \mathrm { m } } ) )$ . In a scenario with more intense competition between the CPs $( \mathrm { i . e . , } V _ { \mathrm { i } } + s _ { \mathrm { i } }$ is higher, i � A or B), the ISP raises p<sup>∗</sup> to extract more consumer surplus.

When CPs’ content production efficiency is high $\begin{array} { r } { ( \mathrm { i . e . , } \phi < \frac { 1 } { 2 t } ) } \end{array}$ competition in content production is intense. Consequently, introducing sponsored data services shifts CP A’s focus to competing by subsidizing consumers while dramatically reducing its investment in content quality. This reduction in quality (i.e., $\begin{array} { r } { V _ { \mathrm { A } } ^ { \mathrm { N } } - V _ { \mathrm { A } } ^ { \mathrm { S } } = \frac { s _ { \mathrm { A } } } { 2 \phi t } , } \end{array}$ , see Lemmas 1 and 2) is thus larger than the value of its data sponsorship $( \mathrm { i } . \mathrm { e } . , s _ { \mathrm { A } } ) .$ , thereby reducing competition between the CPs (i.e., lowering $\bar { V _ { \mathrm { A } } } + s _ { \mathrm { A } } )$ and forcing the ISP to lower p<sup>∗</sup>. By contrast, when content production efficiency is low $\begin{array} { r } { ( \mathrm { i . e . , } \phi > \frac { 1 } { 2 t } ) } \end{array}$ there is less competition in content production, and sponsored data services thus encourage CP A to be more forceful in competing for market share. Thus, CP A in subgame S provides sufficient data sponsorship to offset its decreased content quality (i.e., $s _ { \mathrm { A } } > V _ { \mathrm { A } } ^ { \bar { \mathrm { N } } }$ $\begin{array} { r } { - V _ { \mathrm { A } } ^ { \mathrm { S } } = \frac { s _ { \mathrm { A } } } { 2 \phi t } ) } \end{array}$ , thereby intensifying the competition between the CPs (i.e., increasing ${ V _ { \mathrm { A } } + s _ { \mathrm { A } } } )$ and enabling the ISP to raise $p ^ { * }$ . Therefore, the ISP should allow CP A to sponsor consumers only when content production efficiency is low; the same applies to CP B.

Proposition 1 reveals the crucial role of CPs’ content production efficiency in determining the ISP’s optimal network management choice. It suggests that the ISP should introduce sponsored data services only when CPs’ content production efficiency is low. Although sponsored data services can generate additional revenue for the ISP by charging CPs, they can also reduce revenue generated from charging consumers. When content production efficiency is high, the competition in content production becomes intense, encouraging the sponsoring CPs to prioritize competing for data sponsorship, leading them to dramatically reduce their investment in content production. This reduction reduces the appeal of Internet access to consumers, forcing the ISP to lower its data usage price. In such a scenario, the reduction in revenue—generated from charging consumers—outweighs the additional revenue generated from charging CPs. Hence, the ISP does not benefit from sponsored data services.

By analyzing the trade-off between the ISP’s benefit from CPs’ data sponsorship competition and its loss from their competition in content production, our model yields valuable insights into an ISP’s network management choices.

## 5. Welfare Analysis

As noted in the introduction, there is significant debate over whether sponsored data services are in the public interest. Proponents argue that sponsored data services benefit consumers by providing “free” data traffic, while critics claim they are discriminatory and violate the net neutrality principle. In this section, we examine these arguments by comparing CPs’ profits, consumer surplus, and social welfare across subgames N, S, and SS under the assumptions of $r > t$ (the condition under which sponsoring is attractive to CPs). Our findings provide useful guidance for social planners considering regulations on sponsored data services.

We begin by exploring how sponsored data services affect CPs’ profits, addressing: (a) whether a CP can benefit from subsidizing consumers’ data usage compared with a baseline scenario without data sponsorship (subgame N), as outlined in Proposition $2 ;$ and (b) whether a CP would suffer lower profits due to its rival’s data sponsorship, as outlined in Proposition 3.

Proposition 2 (Implication of Subsidizing Consumers). Considering CP A, which is allowed to sponsor in subgame S:

1. When content production efficiency is high $\begin{array} { r } { ( i . e . , \phi < \frac { 1 } { 2 t } ) . } \end{array}$ CP A benefits from subsidizing consumers’ data usage regardless of whether the other $\bar { C P }$ sponsors consumers, and it achieves maximal profit in subgame SS, where both CPs are allowed to sponsor consumers $( i . e . , \pi _ { A } ^ { N } < \pi _ { A } ^ { S } < \pi _ { A } ^ { S S } )$ ;

2. When content production efficiency is low $\begin{array} { r } { ( i . e . , \phi > \frac { 1 } { 2 t } ) . } \end{array}$ CP A achieves maximal profit in subgame S, where it sponsors consumers alone $( i . { \dot { e } } . , { \dot { \pi } } _ { A } ^ { S } > \pi _ { A } ^ { N }$ and $\pi _ { A } ^ { S } > \pi _ { A } ^ { S S } ) ,$ , and it achieves a lower profit in subgame SS than in subgame N $( i . e . , \pi _ { A } ^ { S S } < \pi _ { A } ^ { N } )$ if the advertising revenue rate is sufficiently low $( i . { \ddot { e } } . , r < { \bar { 4 } } \phi t ^ { 2 } - t )$

Proposition 2 indicates that whether a CP benefits from sponsoring consumers largely depends on its content production efficiency. When content production efficiency is high $( \mathrm { i . e . , } \ \phi < \frac { 1 } { 2 t } )$ the $\mathrm { C P } ^ { \mathrm { i } }$ benefits from subsidizing consumers, as the competition to produce content is intense. With “content wars” becoming increasingly fierce in recent years (Ampere Analysis 2023), CPs have heavily invested in content production. Netflix, for example, spent \$3 billion in 2018 producing original content, causing its negative free cash flow to rise to \$1.3 billion (Egan 2019). Sponsored data services can reduce the intensity of this competition by shifting the focus of the sponsoring CPs to competing in data sponsorship, causing them to reduce their investment in content production and benefit from less intense competition in content compared with subgame N. Conversely, when content production efficiency is low $\begin{array} { r } { ( \mathrm { i . e . , } \phi > \frac { 1 } { 2 t } ) . } \end{array}$ , the sponsoring CPs may suffer from the competition in data sponsorship. In this scenario, allowing only one CP to sponsor consumers can increase that CP’s profits by expanding its market share. However, allowing both CPs to sponsor consumers may trap the CPs in a “prisoner’s dilemma.” In other words, allowing both CPs to sponsor data when their advertising revenue rate is low $\overline { { ( } } \mathrm { i . e . , } r < 4 \phi t ^ { 2 } - t )$ forces them into a competition to subsidize consumers, even though expanding their market shares via this route is unprofitable for both of them.

Next, we explore whether a CP suffers due to its rival’s data sponsorship.

Proposition 3 (Impact of the Rival’s Data Sponsorship). Compared with the scenario in which the rival has no sponsoring option:

1. When content production efficiency is high $\begin{array} { r } { ( i . e . , \phi < \frac { 1 } { 2 t } ) , } \end{array}$ a CP always benefits from its rival’s data sponsorship through higher profits, regardless of whether it has the option to sponsor.

2. When content production efficiency is low $\begin{array} { r } { ( i . e . , \phi > \frac { 1 } { 2 t } ) . } \end{array}$ a CP always suffers from its rival’s data sponsorship, regardless of whether it has the option to sponsor.

Proposition 3 reveals how one CP’s data sponsorship impacts the other CP. Specifically, the data sponsorship of one CP has two effects on the competition between

CPs: it intensifies the competition to subsidize consumers, which adversely affects the other CP; and it incen tivizes the sponsoring CP to reduce its investment in content (see Lemma 2), which decreases the intensity of the competition in content production, benefitting the other CP. Due to these two opposing effects, the impact of one $\mathrm { C P ^ { \prime } s }$ data sponsorship on the other CP ultimately depends on content production efficiency. When content production efficiency is high $\begin{array} { r } { ( \mathrm { i . e . , } \phi < \frac { 1 } { 2 t } ) } \end{array}$ , competi tion in content production becomes highly intense, encouraging the sponsoring CP to shift its focus to competing in data sponsorship while dramatically reducing its content investment. In this case, the effect of a $\mathrm { C P ^ { \prime } s }$ data sponsorship on the competition in content production dominates its effect on the competition in data sponsorship. Consequently, the data sponsorship of one CP decreases the intensity of the competition for content, increasing the other $\mathrm { C P ^ { \prime } s }$ market share (see Lemma 5) and profits. Conversely, when content production efficiency is low $\begin{array} { r } { ( \mathrm { i . e . , } \phi > \frac { 1 } { 2 t } ) } \end{array}$ , the effect of one CP’s data sponsorship on the competition to subsidize consumers outweighs its effect on the competition to produce content. Since this sponsorship intensifies the competition to subsidize consumers, it reduces the other CP’s market share (see Lemma 5) and profits.

Proposition 3 further explores whether a social planner should prohibit sponsored data services to safeguard nonsponsoring CPs’ interests. While proponents of net neutrality have argued that sponsored data services are discriminatory and disadvantageous to nonsponsoring CPs (Fried 2014), Proposition 3 illustrates that banning these services does not necessarily benefit nonsponsoring CPs. The impact of such a ban depends on the level of content production efficiency. Compared with the scenario where only one CP (CP A) has the option to sponsor (subgame S), when content production efficiency is low $\begin{array} { r } { ( \mathrm { i . e . , ~ } \phi > \frac { 1 } { 2 t } ) } \end{array}$ , a nonsponsoring CP (CP B) benefits from banning sponsored data services $\mathrm { ( i . e . , } \pi _ { \mathrm { B } } ^ { \mathrm { N } } > \pi _ { \mathrm { B } } ^ { \mathrm { S } } \mathrm { ) }$ because the competition to subsidize con sumers ends. However, when it is high $\begin{array} { r } { ( \mathrm { i . e . , } \phi < \frac { 1 } { 2 t } ) . } \end{array}$ , a nonsponsoring CP suffers from this ban $( \mathrm { i . e . , } \bar { \pi } _ { \mathrm { B } } ^ { \mathrm { N } } < \bar { \pi } _ { \mathrm { B } } ^ { \mathrm { S } } )$ due to the intense competition to produce content.

We now assess whether consumers benefit from data sponsorship by comparing consumer surpluses under different network management choices. Consumer surplus is the sum of consumers’ utility and is calculated as $\begin{array} { r } { \dot { C } S = \int _ { 0 } ^ { x _ { \mathrm { m } } } U _ { \mathrm { A } } ( x ) d x + \int _ { x _ { \mathrm { m } } } ^ { 1 } U _ { \mathrm { B } } ( x ) d x . } \end{array}$

Proposition 4 (Consumer Surplus). Compared with the baseline scenario without data sponsorship (subgame N), (1) allowing both CPs to sponsor consumers does not change consumer surplus, whereas (2) allowing only one $C P$ to sponsor consumers always increases consumer surplus.

Proposition 4 shows that compared with subgame N, consumer surplus increases when only one CP is allowed to subsidize data usage. When both CPs sponsor consumers, the consumer surplus is unchanged, as the ISP extracts it via its data usage pricing decision. Varying according to the CPs’ content quality and data sponsorship, the $\mathrm { I S P ^ { \prime } s }$ optimal data usage price $p ^ { * }$ always provides the marginal consumer $x _ { \mathrm { m } } ^ { \ast }$ zero utility; due to the low fit cost, the further from the marginal consumer, the higher the utility. In Figure 4, the consumer surplus is represented by the shaded area and equals $\begin{array} { r } { C S = t ( x _ { \mathrm { m } } ^ { \ast } - \frac { 1 } { 2 } ) ^ { 2 } + \frac { t } { 4 } . } \end{array}$ . The formula implies that consumer surplus directly depends on the marginal consumer’s location $x _ { \mathrm { m } } ^ { \ast }$ and increases as $x _ { \mathrm { m } } ^ { \ast }$ deviates from ${ \scriptstyle { \frac { 1 } { 2 } } } .$ When both CPs subsidize consumers’ data usage, the marginal consumer does not move their location, staying at $\begin{array} { r } { x = \frac { 1 } { 2 } } \end{array}$ compared with subgame N. In such cases, the CPs’ data sponsorship does not increase consumer surplus, and the ISP extracts all the benefits that consumers derive from the data sponsorship. However, when only one CP sponsors consumers, such as in the example in Figure 4, the marginal consumer $x _ { \mathrm { m } } ^ { \ast }$ deviates from ${ \scriptstyle { \frac { 1 } { 2 } } , }$ moving closer to CP B’s location x � 1 compared with subgame N. Accordingly, sponsored data services increase the surplus of CP A’s consumers while decreasing that of CP B’s consumers. Given that, in this scenario, CP A has a larger market share than CP B, sponsored data services benefit most consumers and thus increase total consumer surplus. The rationale behind Proposition 4 implies that the imbalance in the CPs’ market shares can benefit consumers by constraining the ISP from extracting consumer surplus.

Proposition 4 indicates how a social planner could regulate sponsored data services to benefit consumers. Departing from the above-described net neutrality argument that supports banning data sponsorship, Proposition 4 implies that a ban would not make consumers better off and could even reduce consumer surplus. Based on this implication, we advise that social planners encourage ISPs to allow only one CP—among a set of two CPs—to subsidize consumers, as this maxi mizes consumer surplus. Net neutrality proponents generally critique the provision of data sponsorship via only one CP, which can be detrimental to nonsponsoring CPs. In contrast to this position, we propose that allowing exclusive data sponsorship can benefit consumers by constraining the ISP from extracting the consumer surplus. Social planners should account for this when regulating sponsored data services.

Figure 4. Illustration of Consumer Surplus  
![](/api/attachments/A9VSG8GW/fulltext/images/769c619b0d92dfc6293c41b7d6bfebcbb82bd80836ad85b89d5cbacf86aead3d.jpg)

Finally, we analyze the influence of sponsored data services on social welfare $( \mathrm { i . e . , }$ , the sum of the $\mathrm { I S P ^ { \prime } s }$ profit, the CPs’ profits, and consumer surplus) to obtain Proposition 5.

Proposition 5 (Social Welfare). There are two cutoff $\underline { { \boldsymbol { \phi } } }$ and $\mathbf { \bar { \phi } }$ with $\begin{array} { r } { \frac { 1 } { 4 t } < \underline { { \phi } } < \overline { { \phi } } } \end{array}$ such that<sup>8</sup>

1. When CPs’ content production efficiency is extremely high $( i . e . , \ \frac { 1 } { 4 t } < \phi < \phi )$ , allowing only one CP to sponsor consumers maximizes social welfare while no data sponsor ship minimizes social welfare (i.e., $S W ^ { \mathrm { S } } > S W ^ { \mathrm { S S } } > S \dot { W } ^ { \mathrm { N } } )$ ;

2. When CPs’ content production efficiency is intermediate $( i . e . , \phi < \phi < \overline { { \phi } } )$ , allowing both CPs to sponsor consumers maximizes social welfare while no data sponsorship minimizes social welfare $( i . e . , S W ^ { \mathrm { S S } } > S W ^ { \mathrm { S } } > S W ^ { \mathrm { N } } ) .$ ;

3. When CPs’ content production efficiency is extremely low $( i . e . , \overline { { \phi } } < \phi )$ , allowing both CPs to sponsor consumers maximizes social welfare while allowing only one CP to sponsor consumers minimizes social welfare $\overline { { ( i . e . , \ S W ^ { { S S } } } } >$ $\dot { S } W ^ { \mathrm { { N } } } > S W ^ { \mathrm { { S } } } )$ ).

Proposition 5 suggests that the impact of sponsored data services on social welfare depends on the ISP’s network management choice and CPs’ content production efficiency. Regarding the ISP’s network management choice, Proposition 5 involves the pairwise comparison of three subgames: subgame N, subgame S, and subgame SS.

First, the welfare comparison between subgame N and subgame SS is straightforward. Since the CPs make symmetrical decisions in both subgames, social welfare is determined by $V - 2 C ( V ) - t / \check { 4 } ,$ which denotes the consumers’ value from content minus production and fit costs. The CPs’ equilibrium content quality decision in subgame $\begin{array} { r } { \mathrm { S S } , \frac { 1 } { 2 \phi } , } \end{array}$ is naturally the optimal investment level, as it maximizes $V - 2 \dot { C } ( V )$ . By contrast, in subgame N, the CPs over-invest in content production compared with the optimal investment level $\Bigl ( \frac { r } { 2 \phi t } > \frac { 1 } { 2 \phi }$ when $r > t )$ . Thus, compared with the baseline scenario without data sponsorship (subgame N), allowing both CPs to sponsor consumers enhances social welfare. Specifically, the CPs allocate resources to data sponsorship and are incentivized to reduce their investments in content production without increasing consumers’ fit costs (see Lemma 2).

Second, the welfare comparison between subgame N and subgame S is ambiguous. On the one hand, com pared with subgame ${ \bar { \mathrm { N } } } ,$ allowing only one CP to sponsor consumers improves social welfare by reducing CPs’ investments in content production, as in the welfare comparison between subgame N and subgame SS. On the other hand, allowing only one CP to sponsor consumers leads to a reduction in social welfare, as it increases consumers’ fit costs by causing some consumers to abandon their preferred services for data sponsorship. As $\phi$ increases, its effect on preventing content overinvestment (i.e., $\begin{array} { r } { V _ { \mathrm { A } } ^ { \mathrm { N } } - V _ { \mathrm { A } } ^ { \mathrm { S } } = \frac { r - t } { 4 \phi t - 1 } ) } \end{array}$ diminishes and is eventually outweighed by its effect on increasing fit costs, leading to a reduction in social welfare when the content production efficiency is extremely low $( \mathrm { i . e . , } \phi > \overline { { \phi } } )$

Finally, the welfare comparison between subgame S and subgame SS is also ambiguous. The logic is similar to that of the welfare comparison between subgame N and subgame S. Compared with subgame SS, allowing only one CP to sponsor consumers increases consumers fit costs and may lead to a greater reduction in content quality. Specifically, the nonsponsoring CP always over-invests in content quality $( V _ { \mathrm { B } } ^ { \mathrm { S } } = \frac { r } { 2 \phi t } > \frac { 1 } { 2 \phi }$ when $r > t )$ , while the sponsoring CP decreases its investment when the content production efficiency is high $( V _ { \mathrm { { A } } } ^ { S } =$ $\frac { r + t - \frac { r } { 2 \phi t } } { 4 \phi t - 1 } < \frac { 1 } { 2 \phi }$ when $\begin{array} { r } { \phi < \frac { 1 } { 2 t } ) } \end{array}$ . Therefore, the content production efficiency must be extremely high $( \mathrm { i . e . , } \phi < \phi )$ for the reduction in $V _ { \mathrm { A } } ^ { \mathrm { S } }$ to outweigh the increase in both $V _ { \mathrm { ~ B ~ } } ^ { S }$ and the fit costs. Under such conditions, allowing only one CP to sponsor consumers maximizes social welfare, as it dominates both subgame N and subgame SS.

Based on these findings, social planners can develop policies that allow non-net-neutral service (i.e., subgame S) when content production efficiency is extremely high and enforce net-neutral data sponsorship (i.e., subgame SS) otherwise.

## 6. Comparison with the Exogeneous

Content Quality Case—(Cho et al. 2016) This study provides a critical extension to existing research on sponsored data (e.g., Cheng et al. 2011, Cho et al. 2016). By endogenizing CPs’ content provision decisions, it addresses a crucial knowledge gap regarding the impacts of an ISP’s network management choice on the interplay between CPs’ quality investment and consumer subsidy decisions.

The analysis reveals new insights that deviate from the predictions of prior studies. To illustrate the importance of endogenizing CPs’ content production deci sions in analyzing the impact of sponsored data service, we compare our model predictions on mostly preferred subgames to those of Cho et al. (2016) in Table 4. Their model assumes exogenously fixed content service quality and can be considered a special case of the current model. We include a detailed analysis of this special case in Online Appendix B.

Table 4. Comparison of Model Predictions on Mostly Preferred Subgames: Endogenous vs. Fixed Content Quality

<table><tr><td></td><td>Main model (endogenous content quality)</td><td>Extension (fixed content quality)</td><td>Discussion</td></tr><tr><td>ISP</td><td>Subgame N when CPs&#x27; content production efficiency is high (i.e.,  $\phi < \frac{1}{2i}$ ) and subgame SS otherwise.</td><td>Always subgame SS.</td><td>Different from the fixed content quality model, the ISP may suffer from the sponsored data service in the endogenous content quality model, as this service may make Internet access less appealing to consumers by reducing the CP&#x27;s content investment. When content production efficiency is high, the reduction in content quality is most severe, hence the ISP would prefer subgame N.</td></tr><tr><td>Sponsoring CP</td><td>Subgame SS when CPs&#x27; content production efficiency is high and subgame S otherwise.</td><td>Always subgame S.</td><td>Different from the fixed content quality model, a sponsoring CP prefers the other CP to have the sponsoring option too when content production efficiency is high, as this option reduces the intensity of quality competition by shifting the other CP&#x27;s focus from competing to produce high-quality content to competing to subsidize consumers.</td></tr><tr><td>Nonsponsoring CP</td><td>Subgame N when CPs&#x27; content production efficiency is low and subgame S otherwise.</td><td>Always subgame N.</td><td>Different from the fixed content quality model, a nonsponsoring CP suffers from banning data sponsorship when content production efficiency is high, as this ban intensifies competition from the other CP, thereby negatively impacting the nonsponsoring CP.</td></tr><tr><td>Consumer surplus</td><td>Always subgame S.</td><td>Always subgame S.</td><td>Consumer surplus always achieves its maximum in subgame S for both models, as the imbalance in the CPs&#x27; market shares could benefit consumers by constraining the ISP from extracting consumer surplus.</td></tr><tr><td>Social welfare</td><td>Subgame S when CPs&#x27; content production efficiency is high and subgame SS otherwise.</td><td>Subgame SS or subgame N, and subgame S is strictly worse.</td><td>In the fixed content quality model, subgame SS and subgame N achieve the same social welfare, as data sponsorship by both CPs merely redistributes (rather than generates new) welfare. In the endogenous content quality model, data sponsorship enhances social welfare by preventing CPs from over-investing in content production.</td></tr></table>

Table 4 presents the most preferred network management choice from the perspectives of the ISP, the sponsoring CP, the nonsponsoring CP, the consumer surplus, and the total welfare. The comparison highlights the critical role of content production efficiency. Specifically, predictions regarding net neutrality implications and the ISP’s profitability based on models with exogenously fixed content quality hold only when content production efficiency is low (Propositions 1–3). Furthermore, without accounting for endogenous content production decisions, sponsored data services never increase social welfare (Proposition 5).

When CPs jointly determine content production and sponsorship, the implications of allowing data sponsorship critically depend on CPs’ content production efficiency. As information technologies continue to enhance digital content production, ISPs and governments must re-evaluate the impact of data sponsorship programs.

## 7. Conclusion

In recent years, the rapid development of artificial intelligence (AI) has profoundly enhanced and transformed content production, as producers use generative AI tools to generate and improve video content.<sup>9</sup> Social media platforms such as TikTok invest heavily in AI tools that enable users to produce high-quality videos (Pogla 2023). According to AIContentfy (2023), which offers AI content production services, AI tools can analyze user data to generate high-quality, engaging content tailored to individual preferences at a low cost. Our paper adopts the stance that: (1) the development of generative AI will fundamentally transform the digital content market landscape by making content production more accessible and efficient; and (2) the impact of sponsored data services should be re-examined by simultaneously considering investment in the production of high-quality content and data sponsorship decisions. Understanding how sponsored data services influence content-related investments is crucial to understanding the market implications of transformative AI technologies. Conducting this analysis not only contributes to the net neutrality discussion but also provides insights into how to foster an ecosystem of highquality content that benefits both CPs and consumers.

In the digital content market, CPs compete for data traffic by subsidizing consumers and investing in highquality content. Previous studies on data sponsorship have treated CPs’ content provision decisions as exogenous, an approach that offered limited insights into the trade-off between data sponsorship and content production, and an incomplete understanding of the impact of sponsored data services. Generative AI is slated to fundamentally transform the content production process, necessitating a re-examination of how network management policy is optimized, particularly as existing theories cannot offer useful guidance without considering endogenous content production decisions. By incorporating CPs’ endogenous content provision decisions and their content production efficiency, our study extends Cho et al.’s (2016) framework to offer a more nuanced understanding of the impacts of sponsored data services and net neutrality policies on various industry stakeholders. Our results emphasize the importance of endogenous content provision decisions in theoretical analysis and highlight the critical role of content production efficiency in determining the impacts of sponsored data services. These impacts can fundamentally shift due to increased content production efficiency, which is particularly relevant given the technological advancements in AI.

Our model provides valuable insights into competition among CPs and the strategies adopted by ISPs. When CPs’ content production efficiency is low, the data sponsorship of one CP increases an ISP’s profit but adversely affects the other CP by intensifying competi tion to subsidize consumers. This finding aligns with previous studies. However, when CPs’ content production efficiency is high, our model diverges from previ ous findings, showing that the data sponsorship of one CP reduces the ISP’s profit while benefiting both CPs by alleviating the intensity of competition in content production. Due to the projected rapid improvement in content production efficiency driven by generative AI, we predict that the impact of sponsored data services on CPs’ competition will evolve to a point where ISPs can no longer profit from these services.

Furthermore, the findings from our model offer valu able guidance for social planners in regulating sponsored data services. First, they indicate that the benefits of net neutrality policies (i.e., banning data sponsorship) for a nonsponsoring CP critically depend on content production efficiency. In cases of high content production efficiency, non-net-neutral sponsored data services—where only one CP sponsors consumer data—prove more advantageous for nonsponsoring CPs, as they reduce competition among CPs relative to the dynamics observed in subgame N. Moreover, our analysis reveals that, compared with net neutrality (i.e., no data sponsorship or allowing both CPs to sponsor consumer data usage), non-net-neutral sponsored data services yield greater benefits for consumers by constraining the ISP’s ability to extract consumer surplus. Lastly, our results show that sponsored data services can enhance social welfare by preventing over-investment in content production by sponsoring CPs. Specifically, when CPs’ content production efficiency is high, allowing only one CP to sponsor consumers maximizes social welfare, whereas allowing both CPs to sponsor consumers does so when content production efficiency is low. Therefore, from the perspectives of nonsponsoring CPs, consumer surplus, social welfare, and the rapid advancements in AI-driven content production efficiency, social planners should encourage ISPs to provide non-net-neutral sponsored data services.

Our work can be extended in several ways. First, while our model focuses on monopolistic ISP decisions, future research could examine CPs’ strategies for content provision and data sponsorship in markets with multiple competing ISPs. Second, researchers could explore other contexts where an ISP charges CPs for practices that deviate from net neutrality, such as packet blocking or delivery priority (Easley et al. 2018). One insight we draw from our research is that charging CPs for data traffic can incentivize reduced content investment, potentially reducing ISPs’ revenue from charging consumers. Future studies could explore the applicability of this insight in other net neutrality scenarios. Third, future research could empirically examine the impacts of sponsored data services and government regulations. For instance, we have observed suggestive evidence from the Chinese streaming video provider Tencent, whose growth rates in content investments have slowed after it initiated a sponsored data program.<sup>10</sup> This is consistent with our finding that sponsored data services incentivize CPs to reduce investment in content (Lemma 2). However, we cautiously note that multiple factors may explain this suggestive evidence, and the sponsored data service may be only one contributing factor. We thus recommend that future studies analyze the role of data sponsorship in such cases and empirically validate our findings in real-world contexts.

## Endnotes

<sup>1</sup> Net neutrality supporters argue that sponsored data services violate the principle of net neutrality and disadvantage CPs that lack the resources to subsidize consumers, as consumers generally prefer sponsored content over unsponsored content (Knutason and Gryta 2014, Kravets 2014, Cho et al. 2016, Qiu et al. 2017).

<sup>2</sup> Efficiency is a critical factor in content production. For example, Netflix employs an “efficiency” metric to measure the viewership of digital content relative to its cost (Shaw 2021).

<sup>3</sup> In the equilibrium of subgame N, CPs offer the same content quality service $( V _ { A } ^ { * } = V _ { B } ^ { * } )$ and have equal shares of the market; at the optimal ISP price $p ^ { * } ,$ , the utility of marginal consumer (located at <sup>1</sup>) is zero. In Online Appendix $\scriptstyle \mathrm { A , }$ we show that the assumption $r \geq$ $2 \phi t ^ { 2 }$ ensures that $p ^ { * }$ is non-negative, and CPs and ISP have incentive to fully cover the market. We also show that when $r > 4 \phi t ^ { 2 } ,$ , the competition becomes too intense such that both CPs experience negative equilibrium profits. We thus adopt an additional assump tion that $r \dot { \leq } 4 \phi t ^ { 2 }$

<sup>4</sup> Other than the assumption that $2 \phi t ^ { 2 } \leq r \leq 4 \phi t ^ { 2 }$ specified in the previous footnote, we further require that $\begin{array} { r } { \phi > \frac { 1 } { 4 t } , } \end{array}$ which ensures that CP A’s sponsored data decision $s _ { A } ^ { * }$ is positive. Without this assump tion, CP A’s profit function is convex and hence will produce con tent of infinitely high quality, as shown by Online Appendix A.

<sup>5</sup> Figures 2 and 3 characterize the value that consumers derive from CPs’ services (i.e., max $\left\{ V _ { A } + s _ { A } - t x , V _ { B } + s _ { B } - t ( 1 - x ) \right\} )$ ). The consu: mers located in $[ 0 , x _ { m } ]$ choose CP A and obtain the value $V _ { A } + s _ { A }$ � tx; and those in $[ x _ { m } , 1 ]$ choose CP B and obtain the value

$V _ { B } + s _ { B } - t ( 1 - x )$ . The $\mathrm { I S P ^ { \prime } s }$ optimal pricing $p ^ { * }$ equals the value that the marginal consumer derives from CPs’ services $( \mathrm { i . e . , } p ^ { * } = V _ { A } + s _ { A }$ $t x _ { m } = V _ { B } + s _ { B } - t ( 1 - x _ { m } ) )$

<sup>6</sup> The intensity of competition in content production can be quantified by the equilibrium value of $V _ { \mathrm { i } } .$ . As content production efficiency improves, represented by a decrease in φ (the cost parameter for content production), CPs respond by increasing their content investments. This results in a higher $V _ { \mathrm { i } } ,$ reflecting heightened competition in content production.

<sup>7</sup> The intensity of competition for market share encompasses both content production and data sponsorship, and can be measured by the total value $V _ { \mathrm { i } } + s _ { \mathrm { i } }$ that CP i delivers to its consumers. This metric captures the combined efforts in creating compelling content and offering data sponsorship to enhance consumer utility. Specifically, when $\dot { \phi } \geq \frac { 1 } { 2 t } , \dot { V _ { A } ^ { S } } + s _ { A } ^ { S } \geq \dot { V _ { A } ^ { N } }$ , the value $\left( V _ { \mathrm { i } } + s _ { \mathrm { i } } \right)$ delivered by CP A in subgame S exceeds that in subgame N, indicating a more intense competitive stance in subgame S.

$^ { 8 } \phi$ is the unique root larger than $\textstyle { \frac { 1 } { 4 t } }$ produced by solving $S W ^ { S S } -$ $S \overline { { W } } ^ { S } = 0$ and its approximate value is $\begin{array} { r } { \phi \approx \frac { 0 . 3 7 8 5 } { t } , } \end{array}$ , while $\overline { { \phi } }$ is the unique root larger than $\textstyle { \frac { 1 } { 4 t } }$ produced by solving $S W ^ { S } - S W ^ { N } = 0$ and its exact value is $\begin{array} { r } { \overline { { \phi } } = \frac { 3 + \sqrt { 5 } } { 4 t } . } \end{array}$

<sup>9</sup> For example, “The Frost” is a 12-minute movie in which every shot was generated by the AI image-generation tool DALL-E; and “Sunspring” is a short sci-fi movie with a script entirely written by an AI system named “Benjamin” (Raj 2024).

<sup>10</sup> Tencent has provided a sponsored data program, the Tencent King Card Service, since 2016 (https://www.sohu.com/a/ 119356937\_513433, accessed July 1, 2022). Tencent’s annual content investment growth rates were 37.43% in 2014, 55.92% in 2015, 30.61% in 2016, and 26.30% in 2017 (https://www.tencent.com/zhcn/investors.html, accessed July 1, 2022).

## References

AIContentfy (2023) The role of AI in content personalization. AIContentfy (November 6), https://aicontentfy.com/en/blog role-of-ai-in-content-personalization.

Ampere Analysis (2023) Growth in content investment will slump in 2023. Report, London.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Banker R, Khosla I, Sinha K (1998) Quality and competition. Man agement Sci. 44(9):1179–1192.

Barua A, Kriebel CH, Mukhopadhyay T (1991) An economic analysis of strategic information technology investments. MIS Quart. 15(3):312–330.

Berman R, Katona Z (2020) Curation algorithms and filter bubbles in social networks. Marketing Sci. 39(2):296–316.

Biglaiser G, Ma C (2003) Price and quality competition under adverse selection: Market organization and efficiency. RAND J. Econom. 34(2):266–286.

Cheng HK, Bandyopadhyay S, Guo H (2011) The debate on net neutrality: A policy perspective. Inform. Systems Res. 22(1):60–82.

Cho S, Qiu L, Bandyopadhyay S (2016) Should online content providers be allowed to subsidize content?—An economic analysis. Inform. Systems Res. 27(3):580–595.

Cho S, Qiu L, Bandyopadhyay S (2020) Vertical integration and zero-rating interplay: An economic analysis of ad-supported and ad free digital content. J. Management Inform. Systems 37(4): 988–1014.

Choi JP, Kim B (2010) Net neutrality and investment incentives RAND J. Econom. 41(3):446–471.

Easley RF, Guo H, Kra¨mer J (2018) Research commentary—From net neutrality to data neutrality: A techno-economic framework and research agenda. Inform. Systems Res. 29(2):253–272.

Economides N, Ta˚ g J (2012) Net neutrality on the Internet: A twosided market analysis. Inform. Econom. Policy 24(2):91–104.

Egan M (2019) Netflix is burning through cash. This can’t last forever. CNN Business (January 18), https://www.cnn.com/2019/ 01/18/investing/netflix-cash-burn-stock/.

Fan M, Kumar S, Whinston A (2007) Selling or advertising: Strate gies for providing digital media online. J. Management Inform. Systems 24(3):143–166.

Faulhaber GR (2011) Economics of net neutrality: A review. Comm. Convergence Rev. 3(1):53–64.

Federal Communications Commission (2017) Twentieth mobile wireless competition report. Report, Federal Communications Commission, Washington, DC.

Fried I (2014) FCC chairman says AT&T sponsored data plans warrant watching. Vox (January 9), https://www.vox.com/2014/1/ 9/11622180/fcc-chairman-says-att-sponsored-data-plans-worthmonitoring.

Gautier A, Somogyi R (2020) Prioritization vs zero-rating: Discrimi nation on the Internet. Internat. J. Indust. Organ. 73:1–25.

Go´mez-Barroso JL, Feijo´o C (2011) Asymmetries and shortages of the network neutrality principle. Commun. ACM 54(4):36–37.

Guo H, Bandyopadhyay S, Cheng HK, Yang YC (2010) Net neutrality and vertical integration of content and broadband services. J. Management Inform. Systems 27(2):243–276.

Guo H, Bandyopadhyay S, Lim A, Yang YC, et al. (2017) Effects of competition among internet service providers and content providers on the net neutrality debate. MIS Quart. 41(2):353–370.

Hermalin BE, Katz ML (2007) The economics of product-line restric tions with an application to the network neutrality debate. Inform. Econom. Policy 19(2):215–248.

Hotelling H (1929) Stability in competition. Econom. J. 39(153):41–57.

Hoernig S, Monteiro F (2020) Zero-rating and network effects. Econom. Lett. 186:1-4.

Inceoglu F, Liu X (2019) Multiproduct price discrimination with quan tity limits: An application to zero-rating. Econom. Lett. 180:41–45.

Johar M, Kumar N, Mookerjee V (2012) Content provision strategies in the presence of content piracy. Inform. Systems Res. 23(3):960–975.

Jullien B, Sand-Zantman W (2018) Internet regulation, two-sided pricing, and sponsored data. Internat. J. Indust. Organ. 58:31–62.

Knutason R, Gryta T (2014) AT&T to let content companies subsi dize users’ data costs. Wall Street Journal (January 6), http:// online.wsj.com/news/articles/SB100014240527023048871045793 04451794540152.

Kourandi F, Kra¨mer J, Valletti T (2016) Net neutrality, exclusivity contracts, and Internet fragmentation. Inform. Systems Res. 26(2):320–338.

Kra¨mer J, Wiewiorra L (2012) Network neutrality and congestion sensitive content providers: Implications for content variety, broadband investment, and regulation. Inform. Systems Res. 23(4):1303–1321.

Kra¨mer J, Wiewiorra L, Weinhardt C (2013) Net neutrality: A progress report. Telecomm. Policy 37(9):794–813.

Kravets D (2014) AT&T thumbs nose at net neutrality with “sponsored” bandwidth scheme. Wired (January 6), http:// www.wired.com/2014/01/att-sponsored-data/.

Kumar S, Qiu L (2022) Social Media Analytics and Practical Applications: The Change to the Competition Landscape (CRC Press, Boca Raton, FL).

Laine LT, Ma CA (2017) Quality and competition between public and private firms. J. Econom. Behav. Organ. 140:336–353.

Ma C, Burgess J (1993) Quality competition, welfare, and regulation. Zeitschr, f Nationalökonomie 58(2):153–173

Matsubayashi N (2007) Price and quality competition: The effect of differentiation and vertical integration. Eur. J. Oper. Res. 180(2):907–921.

Mei X, Cheng HK, Bandyopadhyay S, Qiu L, Wei L (2022) Sponsored data: Smarter data pricing with incomplete information. Inform. Systems Res. 33(1):362–382.

Mitchell C, Kienbaum K (2020) Report: Most Americans have no real choice in internet providers. Institute for Local Self-Reliance (August 12), https://ilsr.org/report-most-americans-have-no-realchoice-in-internet-providers/.

Moorthy K (1988) Product and price competition in a duopoly model. Marketing Sci. 7(2):141–168.

Moorthy K, Png I (1992) Market segmentation, cannibalization, and the timing of product introductions. Management Sci. 38(3):345–359.

Nasser S, Turcic D (2015) To commit or not to commit: Revisiting quantity vs. price competition in a differentiated industry. Management Sci. 62(6):1533–1841.

Netflix (2022) Annual report pursuant to section 13 or 15(d) of the securities exchange act of 1934. Report, 121 Albright Way, Lo Gatos, CA.

Pogla M (2023) TikTok’s \$1 billion GPU investment: An in-depth look. AutoGPT (June 21), https://autogpt.net/tiktoks-1-billiongpu-investment-an-in-depth-look/.

Pu J, Nian T, Qiu L, Cheng HK (2022) Platform policies and sellers competition in agency selling in the presence of online quality misrepresentation. J. Management Inform. Systems 39(1):159–186.

Qiu L, Wang C, Jia J (2017) Sponsored data services and consumer welfare on mobile broadband. Proc. 38th Internat. Conf. Inform. Systems. 2017 (Association for Information Systems, Coex Seoul, South Korea), 10–13.

Qiu L, Rui H, Whinston A (2019) Optimal auction design for Wi-Fi procurement. Inform. Systems Res. 30(1):1–14.

Raj A (2024) AI in the film industry: Still a long way to go. Techwire (January 17), https://techwireasia.com/01/2024/ai-in-the-filmindustry/.

Rausch A, Mu¨ ller JP, Niebuhr D, Herold S, Goltz U (2012) IT ecosys tems: A new paradigm for engineering complex adaptive software systems. Proc. 6th IEEE Internat. Conf. Digital Ecosystems Technol. 2012 (IEEE, Piscataway, NJ), 1–6.

Schuett F (2010) Network neutrality: A survey of the economic literature. Rev. Network Econom. 9(2):1–13.

Shaked A, Sutton J (1982) Relaxing price competition through prod uct differentiation. Rev. Econom. Stud. 49(1):3–13.

Shaked A, Sutton J (1983) Natural oligopolies. Econometrica 51(5): 1469–1483.

Shaw L (2021) Netflix estimates “Squid Game” will be worth almost \$900 million. Bloomberg (October 17), https://www.bloomberg. com/news/articles/2021-10-17/squid-game-season-2-series-worth 900-million-to-netflix-so-far.

Spence AM (1975) Monopoly, quality, and regulation. Bell J. Econom. 6(2):417–429.

Thatcher ME, Pingry DE (2004) An economic model of product quality and IT value. Inform. Systems Res. 15(3):268–286.

Wang C, Li M, Feng H, Feng N (2021) Should subscription-revenue internet content providers adopt sponsored data plans by mobile telecom carriers in duopoly market? Electronic Commerce Res. Appl. 50:101106.

Wu T (2003) Network neutrality, broadband discrimination. J. Telecomm. High Tech. Law 2(1):141–179.

Xin X (2021) A brief analysis of the popularity of domestic IP suspense drama in the all-media era. Art Performance Lett. 2(5):76–79.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
