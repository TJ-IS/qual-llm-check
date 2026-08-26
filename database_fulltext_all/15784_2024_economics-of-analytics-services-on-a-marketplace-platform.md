---
otero_id: 15784
otero_key: "UWDJ7PMR"
title: "Economics of Analytics Services on a Marketplace Platform"
authors: "Zhe Wang; Hong Guo; Dengpan Liu"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/16452"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ECONOMICS OF ANALYTICS SERVICES ON A MARKETPLACE PLATFORM<sup>1</sup>

Zhe Wang Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong SAR, CHINA {zhe.wang@cityu.edu.hk}

Hong Guo Department of Information Systems, W. P. Carey School of Business, Arizona State University, Tempe, AZ, U.S.A {hguo@asu.edu}

Dengpan Liu Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, Beijing, CHINA {liudp@sem.tsinghua.edu.cn}

Analytics services provided by marketplace platforms have become increasingly important for sellers seeking market insights. In this paper, we examine a scenario in which an analytics service plays a vital role in enhancing sellers’ understanding of market size and improving their decision-making. Using a game-theoretic model, we analyze the pricing strategies of the platform and the adoption strategies of sellers for the analytics service. Our study identifies two distinct effects of analytics services: the competition effect and the accuracy effect. Specifically, the competition effect manifests in opposing ways across different market scenarios, with a competition-intensifying effect in lowdemand markets and a competition-weakening effect in high-demand markets. Consequently, sellers using an analytics service command lower prices in low-demand markets and higher prices in highdemand markets. More interestingly, our results reveal that offering an analytics service could potentially hurt the total market demand, subsequently impacting the platform’s revenue from the marketplace service and potentially leaving the platform worse off. Additionally, driven by both the accuracy and competition effects, adopting an analytics service may adversely affect seller profitability and consumer surplus without necessarily improving overall welfare. Moreover, the transaction fee for the marketplace service plays a crucial role in the interplay between the analytics and marketplace services. Specifically, in low-demand (high-demand) markets, as the transaction fee increases, platforms should consider reducing (increasing) the subscription fee to encourage more (fewer) sellers to adopt the analytics service, thereby enhancing overall market demand and increasing revenue from the marketplace service. Our findings also suggest that platforms should refrain from offering analytics services in high-demand markets when the transaction fee is relatively high. Furthermore, policymakers (sellers) should be mindful of the potential negative consequences associated with the adoption of analytics services in high-demand (low-demand) markets.

Keywords: Analytics services, marketplace platform, platform pricing, seller competition, consumer surplus, social welfare

## Introduction

In recent years, online marketplaces have been growing rapidly, especially during the COVID-19 pandemic. According to a report by the United Nations Conference on Trade and Development (UNCTAD, 2022), online marketplace sales reached an impressive \$2.9 trillion globally in 2021. At the same time, sellers on marketplace platforms are facing unprecedentedly intense competition (Li et al., 2019). It has become increasingly apparent that these sellers need to develop effective marketing strategies (e.g., pricing strategies) to succeed. To address this growing need, some marketplace platforms have started to provide analytics tools to assist sellers in making informed decisions (Li et al., 2019). In particular, analytics services (e.g., Terapeak of eBay, BusinessAdvisor of Taobao, and BusinessIntel of JD <sup>2</sup> ) have gradually gained popularity among online sellers (Go, 2020; eBay, 2023). They may include descriptive analytics such as market trends analysis (e.g., eBay, 2023), predictive analytics such as sales forecasts (e.g., Villarica, 2017), and prescriptive analytics such as product category recommendations (e.g., Godin, 2018). By adopting analytics services, sellers can gain valuable business insights (Go, 2020), which enables them to make better decisions (e.g., pricing decisions) and remain competitive in the online marketplace.

In this paper, we focus on a specific subset of analytics services that address market size uncertainty for sellers. Market size is typically defined as the total number of potential sales for a particular product category (Melendez, 2019; Nasrudin, 2022), which can be inferred from the total number of products sold (Melendez, 2019). By subscribing to analytics services, sellers can enhance their understanding of the market size. Next, we provide some examples of market-size-related features and metrics provided by analytics services.

On eBay, sellers subscribing to Terapeak gain valuable insights into market size by utilizing features like Market Trends Research and metrics such as Total Sold (eBay, 2023; Terry, 2023). By taking real-time transaction and historical sales data as inputs, Market Trends Research utilizes visualization tools to generate market trend data as outputs (Terry, 2023), helping sellers better understand sales and demands. Total Sold measures the total number of products sold in a specified time period, giving sellers a clear understanding of their consumer market size (Roggio, 2021). Figure 1 illustrates an example of the Total Sold metric in

Terapeak research results. By leveraging the enhanced market-size-related insights provided by their Terapeak subscription, sellers can make informed decisions regarding pricing and other key business strategies (eBay, 2023). It is worth noting that other marketplace platforms also offer analytics services with similar metrics and features. For example, Taobao’s BusinessAdvisor provides a data module called Market Trends that enables sellers to improve their knowledge of consumer market size (Xiao, 2020).

As discussed above, subscribing to analytics services provides sellers with crucial market-size-related information, enabling them to gain valuable insights into their pricing structure. Consistent with those practices, in this paper, we examine a scenario in which an analytics service is vital for enhancing sellers’ understanding of market size and improving their decision-making. Consequently, the question naturally arises: How do analytics services affect sellers’ pricing decisions? Moreover, since the online marketplace is a highly interactive ecosystem that typically consists of sellers, consumers, and the platform, the effects of analytics services extend beyond the profits of sellers to include those of the platform and consumer surplus. Thus, another important question arises: How do analytics services affect the payoffs of sellers, consumers, and the platform? Additionally, from policymakers’ perspective, we investigate the research question: How do analytics services affect social welfare?

Figure 2 depicts the market structure and payment flows of a typical marketplace platform ecosystem with analytics services. As shown in the figure, sellers charge consumers product prices, and the platform generates revenue from two sources: The marketplace transaction fee (hereafter referred to as marketplace revenue) and the subscription fee of the analytics service (hereafter referred to as analytics revenue). However, these two revenue sources may conflict with each other, requiring the platform to delicately balance them when setting the optimal subscription fee. Therefore, the following research question arises: How can the platform strike a balance between marketplace revenue and analytics revenue while pricing the analytics service? Our findings suggest that the transaction fee plays a critical role in this trade-off and affects the platform’s subscription fee decision, ultimately impacting sellers’ adoption decisions. Thus, we further investigate the research question: How does the transaction fee impact market outcomes when analytics services are present?

![](/api/attachments/UWDJ7PMR/fulltext/images/aee9dc7822deca964665366126b7006524e2de1f72ae58bfbbb6609c956fb0f5.jpg)  
Figure 1. An Example of Terapeak Research Results

![](/api/attachments/UWDJ7PMR/fulltext/images/64424080c5a9eb018778e7df58e2f891d879ffb833abe95ac27eff45a1fcaafd.jpg)  
Figure 2. Payment Flows of a Marketplace Platform Ecosystem with Analytics Services

To explore the research questions outlined earlier, we develop a game-theoretic model in which two sellers compete on a marketplace platform that provides analytics services. To start with, we analyze the platform’s pricing strategies for the analytics service, as well as the sellers’ strategies for pricing their products and adopting the service. As previously discussed, analytics services can help sellers gain more knowledge about the size of the consumer market, leading to better decision-making (hereafter referred to as the accuracy effect). In addition, adopting the analytics service can potentially impact sellers’ competitive behavior (hereafter referred to as the competition effect). Interestingly, our findings suggest that the competition effect manifests in opposing ways across different market scenarios—a competition-intensifying effect in low-demand markets (where the consumer market is small) and a competition-weakening effect in high-demand markets (where the consumer market is large). Specifically, the competition among sellers is intensified in low-demand markets but is weakened in high-demand markets.

Our analysis indicates that adopting an analytics service has varying impacts on sellers’ pricing decisions depending on the market scenario. Specifically, based on the market information provided by the analytics service, sellers tend to lower their prices in low-demand markets but raise them in high-demand markets. We also find that the impact of the analytics service on sellers’ profits is dependent on the market scenario. In particular, sellers would be better (worse) off adopting the analytics service in high-demand (low-demand) markets due to the dominant impact of the accuracy (competition-intensifying) effect on sellers’ profits in such market scenarios. Furthermore, with the combined influence of the accuracy effect and the competition effect of the analytics service, we find that implementing the service would lead to a higher consumer surplus in lowdemand markets but a lower consumer surplus in highdemand markets, compared to not implementing the service. Lastly, it is important to note that analytics services may not always be beneficial from the perspective of policymakers seeking to maximize social welfare. More specifically, in high-demand markets, while the provision of an analytics service may benefit sellers and the platform, its impact on consumers will be relatively detrimental, ultimately resulting in a decrease in overall social welfare.

Several interesting findings also emerge from the analysis of the interplay between the platform’s two revenue sources— the analytics revenue and marketplace revenue. Specifically, in high-demand markets, when determining the subscription fee for the analytics service, the platform must strike a delicate balance between marketplace revenue and analytics revenue, as the incentives for managing these two revenue sources may potentially conflict. The reason for this is that in high-demand markets, the adoption of the analytics service by sellers results in increased analytics revenue for the platform. Moreover, through the adoption of the service, sellers realize that the market size is larger than anticipated, and the accuracy effect leads them to raise their prices to capture the larger market potential. Furthermore, the competition-weakening effect comes into play, reducing the intensity of competition between sellers in larger consumer markets. Both the accuracy effect and the competitionweakening effect contribute to elevated product prices, leading to a decrease in total market demand and consequently impacting marketplace revenue negatively. As a result, while encouraging sellers to adopt the service enhances the analytics revenue, it adversely affects the marketplace revenue in high-demand markets. However, in low-demand markets, these two revenue sources align with each other. Specifically, when sellers adopt an analytics service, the analytics revenue increases; at the same time, both the accuracy effect and the competition-weakening effect contribute to increased market demand and higher marketplace revenue. Additionally, our results demonstrate the critical role of the transaction fee in shaping the interplay between the two revenue sources. In high-demand (lowdemand) markets, as the transaction fee increases, the platform has incentives to charge a higher (lower) subscription fee to induce less (more) adoption from sellers, thereby increasing the total demand and hence the marketplace revenue. Interestingly, sellers may lower their product prices due to intensified competition when the platform charges them more for the marketplace service.

Our study makes several contributions. First, to the best of our knowledge, this work represents a pioneering study in formally examining analytics services offered by marketplace platforms—an important new business model in the platform economy. In this paper, we highlight the unique feature of this new business model: By offering both marketplace and analytics services, the platform serves the dual role of marketplace facilitator and market information provider, thereby facing a trade-off between analytics revenue and marketplace revenue. By studying this unique trade-off, we contribute to the literature on market information services and demand information sharing, which has primarily focused on how market information providers can maximize their revenue through information sharing (e.g., Vives, 1984), often overlooking the trade-off we highlight in this research. Second, this paper employs a distinct research methodology (i.e., analytical modeling) compared to prior studies within the broader research context of business intelligence and analytics, which allows us to go beyond the literature to investigate the economic implications of business intelligence and analytics on market outcomes such as social welfare. More specifically, the existing literature on business intelligence and analytics predominantly consists of technical and empirical studies that aim to enhance algorithmic performance (e.g., Moon & Russell, 2008) and investigate the impact of business intelligence on firm performance (e.g., Božič & Dimovski, 2019). However, the existing literature often lacks discussions regarding the impact of these tools on the strategic interactions among stakeholders in the platform ecosystem, as well as their effects on consumer surplus and social welfare. By adopting an analytical modeling approach, we can delve into these aspects and gain a deeper understanding of how these services influence various economic outcomes, including consumer surplus and social welfare.

Third, our research contributes to the existing literature on platform-based functions by examining the role of analytics services, a novel function that has received limited attention thus far. Unlike traditional platform-based functions, the analytics service does not directly provide added value to sellers. Instead, as explicitly modeled in this study, the service benefits sellers by providing them with valuable market information, which in turn enables them to make more informed decisions. When exploring the determinants of the impacts of platform-based functions, we go beyond the existing literature that mainly focuses on the characteristics of various stakeholders, including sellers (e.g., Li et al., 2019), consumers (e.g., Li et al., 2009), and platforms (e.g., Chen et al., 2016). Specifically, we also explore how the market scenario (high- or low-demand market) influences the impact of the analytics service as a platform-based function, considering the unique feature of the analytics service that provides sellers with marketsize-related information. Consequently, our findings reveal that the value of analytics services and their impacts on the platform ecosystem are contingent upon the underlying market scenarios. For example, we find that analytics services intensify seller competition in low-demand markets but weaken seller competition in high-demand markets. We also contribute to this stream of literature by studying the pricing of the platformbased function and investigating the unique trade-off faced by platforms between analytics revenue and marketplace revenue, which has seldom been investigated in the literature.

The rest of the paper is organized as follows. The following section provides a comprehensive review of the related literature. The Modeling Framework section proposes a gametheoretic model to investigate a marketplace platform ecosystem with analytics services under two distinct market scenarios. The Analysis of Sellers’ Pricing Decisions section derives sellers’ pricing decisions given their updated beliefs about market size. The Adoption and Pricing of Analytics Service section discusses the sellers’ adoption of the analytics service and the platform’s equilibrium pricing strategy. We conclude the paper with discussions about theoretical contributions and managerial implications.

## Literature Review

Our study is mainly related to four streams of research: market information services, demand information sharing, platformbased functions, and business intelligence and analytics. This section reviews the relevant studies and highlights our contributions to the existing literature.

## Market Information Services

There is extensive literature on the market information services provided by third-party consultants. For example, Chang and Lee (1994) discussed how a monopoly consultant should price the consulting service for two competitive firms to help reduce market uncertainty. Arora and Fosfuri (2005) extended this study in the context of investment consulting services, where firms could distinguish good projects from bad projects by using such a service. More recently, Bergemann and Bonatti (2015) and Kastl et al. (2018) found that a monopolistic information provider may provide imprecise information to competitive firms because more accurate information can lead to more intense competition and hence decrease firms’ willingness to pay for the information.

There also exists a large body of literature on self-provided or rival-provided market information. For example, Kwark et al. (2018) studied the impact of user-generated content serving as market information, which could help firms predict consumers’ preferences more precisely. Zhao and Xue (2012) studied consumer data trading between competing firms, where consumer data could help firms target individual consumers more accurately. They found that firms may be better off selling consumer information to rivals.

Unlike the above studies on market information services, this paper investigates analytics services offered by a two-sided marketplace platform. In this context, the platform serves the unique dual role of marketplace facilitator and market information provider. Consequently, the platform may face a trade-off between marketplace revenue and analytics revenue. To the best of our knowledge, this study is among the first attempts to formally investigate this important trade-off.

## Demand Information Sharing

Our work is also related to the literature on demand information sharing (Gal-Or, 1986; Darrough, 1993; Raith, 1996; Zhang, 2002; Ha et al., 2011; Jain et al., 2011; Gümüş, 2014; Tsunoda & Zennyo, 2021). Under a duopoly competition structure, Vives (1984), Gal-Or (1986), and Darrough (1993) examined firms incentives to disclose their private information under both the Cournot and Bertrand competition models. Furthermore, Raith (1996) developed a more general model to investigate oligopolists’ incentives to share their private information on stochastic demand or stochastic costs. Zhang (2002) investigated the vertical information exchange in a supply chain with duopoly retailers and found that no information was shared with the manufacturer on a voluntary basis. Additionally, in the context of supply chain competition, Ha et al. (2011) found that under Bertrand competition, manufacturers may be worse off if they receive information from retailers, unlike the case under Cournot competition. In the same context, Jain et al. (2011) found that when all retailers are given the same wholesale price, retailers will not truthfully share demand information in equilibrium. Gümüş (2014) investigated when and how credible demand forecast sharing can be sustainable in a supply chain. In a similar context, Tsunoda and Zennyo (2021) investigated a platform’s information-sharing policy under demand uncertainty with a supplier selling products on an online platform and an offline retailer.

While there is a growing body of literature on demand information sharing, the unique context of the two-sided marketplace platform remains relatively unexplored. In this context, it is essential for the platform to carefully assess the impact of information sharing on its marketplace and to determine the price for sharing demand information with key market participants (e.g., sellers). As a result, the platform must weigh the marketplace revenue generated from the marketplace service against the analytics revenue generated from information sharing. To our knowledge, our study represents one of the first attempts to examine this trade-off and to analyze information sharing with sellers in the context of a two-sided marketplace platform.

## Platform-Based Functions

Our work is also related to the literature on seller tools provided by the platform (also known as platform-based functions). For example, Li et al. (2009) studied how a platform buy-it-now feature used as a quality indicator affected consumers’ participation and bidding decisions. Walia and Zahedi (2013) found that the platform’s buy-it-now feature negatively affected sales performance. Chen et al. (2016) studied the revenue implication of the sponsored searching service offered by the platform, finding that in certain circumstances, the platform’s revenue under an advertising model (where the platform charges for a sponsored searching service) may be higher than that under a brokerage model (where the platform charges for each transaction). Li et al. (2019) uncovered several theoretical relationships between various structural characteristics of the platform-based function repertoire and sales performance at different levels of seller reputation.

The above studies, most of which were conducted empirically, focus on how the functions or tools provided by the platform influence sellers’ sales performance. Unlike conventional platform-based functions or tools, analytics services do not simply provide added value to sellers; instead, analytics services benefit sellers by providing them with market information that can help sellers make more informed decisions, which is explicitly modeled in this paper. Our study also contributes to this literature by analytically examining the strategic interactions between the platform and the competing sellers and the impact of analytics services on such interactions.

## Business Intelligence and Analytics

Our work is also related to the literature on business intelligence and analytics. As mentioned by Chen et al. (2012), firms can access large volumes of real-time consumer behavioral data in the big data era, which can further help them make better decisions. Currently, firms use structural data (e.g., consumer transaction data, sales performance data) and unstructured data (e.g., consumer search logs, consumer click logs, usergenerated content) to generate more business insights. For example, consumers’ transactional data can be used to predict product purchases (Moon & Russell, 2008), understand consumers’ online behavior (Zhang et al., 2006), and improve the accuracy of a recommendation system (Dzyabura & Hauser, 2019). Moreover, user-generated content can also be used to predict sales performance (Song et al., 2019) and help sellers better design and price their goods (Kwark et al., 2018).

This literature on business intelligence and analytics investigates how to use the big data generated in the digital era for business insights. However, the economic impacts of analytics services as an important tool to help sellers gain business insights have not been well-studied in this stream of literature. Our work aims to fill this gap in the literature on business intelligence and analytics by studying the pricing and adoption of analytics services and their implications for seller competition and social welfare.

## Modeling Framework

We consider two competing sellers <sup>3</sup> on a marketplace platform that offers a subscription-based analytics service. Following the existing literature on price competition among sellers with differentiated goods (e.g., Singh & Vives, 1984; Vives, 1984; Häckner, 2000; Symeonidis, 2003; Choi & Coughlan, 2006; Wang et al., 2016), we use a linear demand Bertrand competition model framework to capture the competition between the two sellers. Specifically, in this paper, seller ??’s demand is calculated as

$$
d _ {i} = \mu_ {i} a - p _ {i} + \lambda p _ {- i}.
$$

Here, $d _ { i }$ and $p _ { i }$ denote the demand and the price of seller $i \in$ {1,2}, respectively, $p _ { - i }$ denotes the price of her rival, and ?? denotes the market size. As shown in the formula of $d _ { i } ,$ each seller’s demand decreases in her own price but increases in her rival’s price. Additionally, $\lambda \in ( 0 , 1 ]$ denotes the substitution level, which characterizes the substitution effect between the competing products provided by the two sellers. As ?? increases, the two products are more substitutable for each other. In the special case of $\lambda = 1$ , the two products are perfectly substitutable. Moreover, $\mu _ { i } \in ( 0 , 1 )$ , where $\mu _ { i } +$ $\mu _ { - i } = 1$ , characterizes seller ??’s popularity among consumers. Without loss of generality, we consider seller 1 is the more popular seller in the market $( \mathrm { i . e . , } \mu _ { 1 } \geq \mu _ { 2 } )$

Sellers face uncertainty regarding the size of the market (??), which can take on either $a _ { H }$ or $a _ { L } ( { \mathrm { i . e . , } } a \in \{ a _ { H } , a _ { L } \} )$ , where $a _ { H } > a _ { L }$ . The probability of ?? taking the value $a _ { H } \mathrm { o r } a _ { L }$ is ${ } ^ { 1 / 2 }$ If $a = a _ { H } \left( a = a _ { L } \right)$ , the market is considered a high-demand (low-demand) market. Sellers are aware of the two possible values of the market size, but they cannot determine whether $a _ { H }$ or $a _ { L }$ is the true value without adopting the analytics service. Following prior studies (e.g., Jaynes, 2003), we assume that before adopting the analytics service, sellers hold unbiased prior beliefs about the market size, with $\operatorname* { P r } [ a = a _ { H } ] =$ $\mathrm { P r } [ a = a _ { L } ] = 1 / 2$ . In this model, we characterize the role of the analytics service as improving sellers’ understanding of the size of the market where they are competing. Correspondingly, we assume that sellers will know the true value of ?? once they adopt the service. Furthermore, in reality, the platform has access to information such as transaction volume over a specific period, which enables it to learn the market size (Melendez, 2019); thus, we assume that the platform has knowledge of the true market size. A list of notations used in this paper is provided in Table 1.

The timing of the game is depicted in Figure 3: In Stage 1, the platform decides on the subscription fee ?? for the analytics service. In Stage 2, sellers simultaneously decide whether to adopt the analytics service. If a seller adopts, the seller will learn about the true market size ( ?? ). In Stage 3, sellers simultaneously choose their prices ${ { p } _ { i } } . ^ { 4 }$ In Stage 4, consumer demands are realized. In the following, we discuss the players’ moves in each stage in detail.

Anticipating the sellers’ moves in Stages 2 and 3, the platform decides on the subscription fee for the analytics service in Stage 1. The platform has two revenue sources: The revenue generated from the transaction fee for the marketplace service<sup>5</sup> (termed marketplace revenue), and the revenue generated from the subscription fee for the analytics service (termed analytics revenue). In this paper, we denote the transaction fee charged by the platform for the marketplace service by $f ,$ which is considered to be exogenously given.<sup>6</sup> We denote seller $i \ ' _ { \mathbf { S } }$ demand by $d _ { i } ;$ thus, the marketplace revenue is $f ( d _ { 1 } + d _ { 2 } )$ . Moreover, the analytics revenue of the platform is $s ( I _ { 1 } + I _ { 2 } )$ , where ?? is the subscription fee for the analytics service, and $I _ { i }$ is the indicator variable for whether seller ?? adopts the service $( I _ { i } = 1$ in case of adoption, and $I _ { i } =$ 0 otherwise). Here, $I _ { 1 } + I _ { 2 }$ computes the total number of sellers adopting the service. The platform determines the subscription fee for the analytics service to maximize its profit $( \pi _ { p } ) .$ . Thus, the platform’s problem in Stage 1 is:

$$
\max _ {s} \pi_ {p} = f (d _ {1} + d _ {2}) + s (I _ {1} + I _ {2}).
$$

In Stage 2, anticipating the potential benefit of adopting the analytics service, sellers decide whether to adopt the analytics service. Here, it is important to note that the realized profits of sellers (and hence the actual benefit of the analytics service) critically depend on the market scenario (whether the market size is high or low, i.e., $a = a _ { H } \operatorname { o r } a = a _ { L } )$ . As a result, since neither seller knows the true market size before adopting the analytics service, they can only make their adoption decisions based on the expected payoffs $E [ \pi _ { i } ]$ . Specifically, the sellers calculate their expected profits $( E [ \pi _ { i } ] )$ based on their prior beliefs about the market size (i.e., $\operatorname* { P r } [ a = a _ { H } ] = \operatorname* { P r } [ a =$ $a _ { L } ] = 1 / 2 )$ . Consequently, the sellers make their adoption decisions to maximize $E [ \pi _ { i } ( I _ { i } , I _ { - i } ) ]$ in Stage 2:

$$
\max _ {I _ {i}} E [ \pi_ {i} (I _ {i}, I _ {- i}) ] = \frac {\pi_ {i} (I _ {i} , I _ {- i} , a _ {H}) + \pi_ {i} (I _ {i} , I _ {- i} , a _ {L})}{2}.
$$

<table><tr><td colspan="2">Table 1. List of Notations</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td> $p_i$ </td><td>Seller i&#x27;s price,  $i \in \{1,2\}$ </td></tr><tr><td> $I_i$ </td><td>Indicator variable for whether seller i adopts the analytics service:  $I_i = 1$  in case of adoption, and  $I_i = 0$  otherwise</td></tr><tr><td>s</td><td>Subscription fee for analytics services charged by the platform</td></tr><tr><td colspan="2">Parameters and other variables</td></tr><tr><td>a</td><td>True market size,  $a \in \{a_H, a_L\}$ </td></tr><tr><td>λ</td><td>Substitution level, λ ∈ (0,1]</td></tr><tr><td>μi</td><td>Seller i&#x27;s popularity among consumers, μi ∈ (0,1)</td></tr><tr><td>di</td><td>Seller i&#x27;s demand</td></tr><tr><td>πi</td><td>Seller i&#x27;s profit</td></tr><tr><td>πp</td><td>Platform&#x27;s profit</td></tr><tr><td>f</td><td>Transaction fee for marketplace services charged by the platform</td></tr></table>

<sup>6</sup> In reality, the transaction fee of the marketplace service is determined by many factors beyond the scope of this paper (Rochet & Tirole, 2003; Armstrong, 2006; Chen et al., 2016). For example, the platform may have the incentive to lower the transaction fee to attract more sellers to join the platform. Since the determination of the transaction fee is not the focus of the paper, we assume that the transaction fee is exogenously given.

![](/api/attachments/UWDJ7PMR/fulltext/images/ed6038b2cff9e8bb9335fc66d31db20f6e61a300b8b5f684e43ddb3f7e1cf0c8.jpg)

In the formula of $\pi _ { i } ( I _ { i } , I _ { - i } , a )$ , conditional on the sellers’ adoption decisions and the true market size (??), which can be $a _ { H }$ or $a _ { L }$ , seller $i \ \mathrm { ^ { \circ } s }$ resulting profit is: $\pi _ { i } ( I _ { i } , I _ { - i } , a ) = ( p _ { i } -$ $f ) E [ d _ { i } ( I _ { i } , I _ { - i } , a ) ] - I _ { i } s$ . Here, $I _ { i }$ is the indicator variable for whether seller ?? adopts the service, and $E [ d _ { i } ( I _ { i } , I _ { - i } , a ) ]$ , which depends on the sellers’ adoption decisions and the true market size (??), is seller ??’s expected demand (which will be introduced in the next paragraph), and ?? is the subscription fee of the analytics service.

In Stage 3, based on their updated beliefs about the true market size, the sellers simultaneously make their respective pricing decisions to maximize their own profits. Recall that we characterize the role of the analytics service as improving sellers’ knowledge about the market size. More specifically, we assume that if seller ?? adopts the analytics service, she knows the true market size (??); and if seller ?? does not adopt the service, then her prior belief is not updated and she still believes that ?? takes values $a _ { H }$ or $a _ { L }$ with equal probability (i.e., $\mathrm { P r } [ a = a _ { H } ] =$ $\mathrm { P r } [ a = a _ { L } ] = 1 / 2 )$ . Based on such updated beliefs, sellers simultaneously decide their prices $p _ { i }$ to maximize their expected profits. That is, seller ?? solves the problem:

$$
\max _ {p _ {i}} (p _ {i} - f) E [ d _ {i} (I _ {i}, I _ {- i}, a) ],
$$

where

$$
\begin{array}{r l} & E [ d _ {i} (I _ {i}, I _ {- i}, a) ] \\ & = \left\{ \begin{array}{c} \mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i}, \mathrm{if} I _ {i} = 1, a = a _ {H}; \\ \mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i}, \mathrm{if} I _ {i} = 1, a = a _ {L}; \\ \mu_ {i} (a _ {H} + a _ {L}) / 2 - p _ {i} + \lambda p _ {- i}, \mathrm{if} I _ {i} = 0, a = a _ {H} \mathrm{or} a _ {L} \end{array} \right. \end{array}
$$

is seller ??’s expected demand and ?? is the transaction fee the platform charges for the marketplace service. Note that since the adoption decisions are made in Stage 2, they are sunk costs for sellers in Stage 3 and hence are omitted in the seller’s maximization problem.

In Stage 4, consumer demands are realized. In the following two sections, using backward induction, we first analyze sellers’ pricing decisions in Stage 3 and then analyze sellers adoption decisions in Stage 2 and the platform’s subscription fee decision in Stage 1.

## Analysis of Sellers’ Pricing Decisions

In this section, we analyze sellers’ pricing decisions in Stage 3. Given their respective adoption decisions, sellers set their prices simultaneously to maximize profits, i.e., $\operatorname* { m a x } _ { p _ { i } } ( p _ { i } -$ $f ) E [ d _ { i } ( I _ { i } , I _ { - i } , a ) ]$ . Here, seller ?? ’s expected demand $E [ d _ { i } ( I _ { i } , I _ { - i } , a ) ]$ depends on her updated belief about the market size, which is in turn determined by sellers’ adoption decisions and the true market size ?? . Below, we examine sellers’ pricing decisions and summarize the results in Lemma 1. All the proofs of lemmas and propositions are relegated to Appendix G.

Lemma 1 (sellers’ pricing decisions): Given the true market size (??) and the sellers’ adoption decisions $a _ { i }$ and $I _ { - i } ) ,$ seller ?? makes her pricing decision $p _ { i }$ as follows in Table 2 below.

<table><tr><td colspan="4">Table 2. Lemma 1 Pricing Decision</td></tr><tr><td></td><td> $I_i = 0, I_{-i} = 1$ or  $I_i = I_{-i} = 0$ (Equivalently,  $I_i = 0$ )</td><td> $I_i = I_{-i} = 1$ </td><td> $I_i = 1, I_{-i} = 0$ </td></tr><tr><td> $a = a_H$ </td><td> $p_i = \frac{(a_H + a_L)(2\mu_i + \lambda\mu_{-i})}{2(4 - \lambda^2)} + \frac{f}{2 - \lambda}$ </td><td> $p_i = \frac{f(2 + \lambda) + a_H(2\mu_i + \lambda\mu_{-i})}{4 - \lambda^2}$ </td><td> $p_i = \frac{(a_H + a_L)(2\mu_i + \lambda\mu_{-i}) + 2f(2 + \lambda)}{2(4 - \lambda^2)} + \frac{\mu_i(a_H - a_L)}{4}$ </td></tr><tr><td> $a = a_L$ </td><td> $p_i = \frac{(a_H + a_L)(2\mu_i + \lambda\mu_{-i})}{2(4 - \lambda^2)} + \frac{f}{2 - \lambda}$ </td><td> $p_i = \frac{f(2 + \lambda) + a_L(2\mu_i + \lambda\mu_{-i})}{4 - \lambda^2}$ </td><td> $p_i = \frac{(a_H + a_L)(2\mu_i + \lambda\mu_{-i}) + 2f(2 + \lambda)}{2(4 - \lambda^2)} - \frac{\mu_i(a_H - a_L)}{4}$ </td></tr></table>

Note: Figure generated based on parameter values $a _ { L } = 2 , a _ { H } = 3 , \mu _ { 1 } = 1 / 2 , \mu _ { 2 } = 1 / 2 ,$ and $\lambda = 0 . 2 .$ . Figures generated based on alternative parameter values exhibit similar qualitative characteristics.

![](/api/attachments/UWDJ7PMR/fulltext/images/475b5ae614dd1830717328db841fae91da118790361a5b31e18a3a2b97674256.jpg)  
a. Low-demand market $( a = a _ { L } )$

![](/api/attachments/UWDJ7PMR/fulltext/images/384bb947e2d8e131755260a83777d0249d1115f0505a04b04e5c68513fb5d913.jpg)  
b. High-demand market $( { \pmb a } = { \pmb a } _ { H } )$

Figure 4. Seller i’s Pricing Decision

Note that the case where $I _ { i } = I _ { - i } = 0$ is equivalent to the regime without the analytics service. To illustrate the results in Lemma 1, we use Figure 4 to depict the results of how seller ?? makes her pricing decision based on the sellers’ adoption decisions and the market scenario.

As indicated by Lemma 1 and Figure 4, a seller’s pricing strategy may depend on the true market size and sellers’ analytics service adoption decisions. As shown in the last two columns of Table 2, compared to the regime without the analytics service, in the high-demand market, the adopting seller (i.e., the seller who adopts the analytics service) sets a higher price to take advantage of the strong demand; however, in the low-demand market, the seller sets a lower price to compete for the limited demand. Furthermore, the adopting seller’s pricing strategy also depends on their competitor’s adoption strategy. As shown in Figure 4, in the low-demand (high-demand) market, the adopting seller charges a lower (higher) price if their competitor changes from not adopting to adopting. Additionally, as shown in the first column of Table 2, the price of the nonadopting seller (i.e., the seller who does not adopt the analytics service) is the same as that under the regime without the analytics service and is independent of the other seller’s adoption decision and the true market size.

## Adoption and Pricing of Analytics Service

This section investigates how sellers make adoption decisions in Stage 2 and how the platform sets the subscription fee for the analytics service in Stage 1. To focus on the key effects of the service, we begin by studying the symmetric case, where sellers have the same popularity (i.e., $\mu _ { \mathrm { i } } = 1 / 2 )$ . For a comprehensive analysis, we extend the analysis to asymmetric sellers in Appendix C.

## Equilibrium Analysis

In Stage 2, the sellers decide whether to adopt the analytics service to maximize their respective expected profits. We investigate the adoption decisions of the sellers under different values of subscription fees and summarize the findings in Lemma 2.

Lemma 2 (sellers’ adoption of the analytics service): If the subscription fee ?? for the analytics service is relatively low $( i . e . , s \leq \tilde { s } )$ , both sellers adopt the service; otherwise, neither seller adopts the service. Note that $\begin{array} { r } { \tilde { s } = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } . } \end{array}$

Lemma 2 indicates that as the subscription fee (??) charged by the platform increases, fewer sellers adopt the analytics service. Specifically, both sellers will adopt the service when the subscription fee is lower than a threshold; however, when the subscription fee is higher than a threshold, they will be priced out of the analytics service. Whether a seller adopts the analytics service critically depends on the comparison between the subscription fee (??) charged by the platform and the potential benefit that the seller could derive from the subscription (i.e., ??̃ ). Interestingly, we find that when the value of $a _ { H } - a _ { L }$ increases, sellers are more incentivized to adopt the analytics service. The reason for this is that in such a case, sellers face higher market size uncertainty and thus can derive a higher potential benefit from adoption. Next, we examine the platform’s subscription fee decision, sellers adoption decisions, and the impact of the service on the platform’s profit in Lemma 3.

Lemma 3 (platform’s subscription fee, sellers’ adoption of the analytics service, and the impact of the service on the platform’s profit):

(a) If the market size is high $( a = a _ { H } )$ and the transaction fee is relatively high $( f > { \tilde { f } } ) ,$ the platform will set a high subscription fee $( s ^ { * } > \tilde { s } )$ such that neither seller adopts. Consequently, compared to the case where the analytics service is unavailable, the platform’s profit remains unchanged.

(b) Otherwise, the platform will set a low subscription fee (??<sup>∗</sup> = ??̃) to induce the adoption of both sellers. Consequently, compared to the case where the analytics service is unavailable, the platform’s profit is higher.

The expression of ??<sup>̃</sup> can be found in the proof of Lemma 3 in Appendix G.

According to Lemma 3, in the low-demand market, the platform is always incentivized to induce the adoption from sellers by setting a low subscription fee. In contrast, in the high-demand market, inducing seller adoption may not be the best strategy. The reasons for the differing outcomes in the two market scenarios are explained below.

In the low-demand market, sellers command lower prices once they adopt the service (as indicated in Lemma 1). This leads to more transactions and, consequently, higher marketplace revenue. Thus, in such a market, the platform always sets prices in a way that both sellers adopt the service, which increases both marketplace and analytics revenue.

In contrast, in the high-demand market, sellers command higher prices once they adopt the service (as indicated in Lemma 1). However, this increase in price leads to fewer transactions, resulting in lower marketplace revenue. Therefore, in such a market, the platform faces a trade-off between analytics revenue and marketplace revenue. In some cases, the platform may not have the incentive to induce the adoption by any seller, particularly if the transaction fee (??) is relatively high. We will delve deeper into how ?? impacts the platform’s trade-off between its two revenue sources in the section entitled Impact of Transaction Fee f.

It is worth noting that when compared to the regime without the analytics service, the platform’s profit will never decrease under the regime with the service. This is because the platform can always set a relatively high subscription fee for the service, which would prevent sellers from adopting it; as a result, the platform can at least earn the same profit as it would under the regime without the analytics service.

## Impact of Analytics Service

In order to examine the impact of the analytics service, we compare the equilibrium outcomes with those under the regime without the analytics service and summarize the findings below.

Proposition 1 (impact of analytics service on sellers’ prices): <sup>7</sup> Compared to the regime without the analytics service, under the regime with the service, (a) in the lowdemand market, sellers command lower prices, and (b) in the high-demand market, sellers command higher prices.

The above proposition states that the analytics service has opposite impacts on sellers’ prices under different market scenarios. The intuition is the following. Adopting the analytics service has two main effects on sellers’ incentives for setting prices. First, with the adoption of analytics services, sellers learn about the true market size, which enables them to make better pricing decisions. We refer to this effect as the accuracy effect. Second, with the updated beliefs about the market size, sellers may adjust their prices, which may in turn change sellers’ competitive behavior. We refer to this effect as the competition effect. The competition effect manifests in opposing ways across different market scenarios, with a competition-intensifying effect in the low-demand market and a competition-weakening effect in the high-demand market.

In the low-demand market, the analytics service has two effects: The accuracy effect and the competition-intensifying effect, both of which lead to sellers commanding lower prices. First, driven by the accuracy effect, sellers adopting the analytics service realize that the market size is smaller than previously expected. Thus, the expected marginal benefit from increasing the price is also lower than previously expected. Therefore, equipped with the improved knowledge of the consumer market, sellers have an incentive to reduce their prices after adopting the analytics service. Second, driven by the competition-intensifying effect, the adopting sellers realize a lower market size and compete for a smaller consumer market than previously expected. Consequently, under competitive pressure, the sellers become more aggressive in their pricing strategies. Both of the aforementioned two effects cause sellers to command lower prices in the low-demand market.

In the high-demand market, as in the low-demand market, the accuracy effect exists. Due to the accuracy effect, sellers gain a better understanding of the consumer market, leading them to realize that the market size is larger than previously expected. Consequently, they expect higher marginal benefits from increasing product prices, which incentivizes them to raise their prices. However, in the high-demand market, unlike in the low-demand market, sellers enjoy a competitionweakening effect. As such, with a larger consumer market and less competitive pressure, sellers become less aggressive in pricing. These two effects lead to higher prices commanded in the high-demand market. Next, we investigate the impact of the analytics service on seller profitability and summarize the results in the proposition below.

Proposition 2 (impact of analytics service on sellers profits): Compared to the regime without the analytics service, under the regime with the service, (a) in the lowdemand market, sellers are worse off, and (b) in the highdemand market, sellers are better off.

Proposition 2 reveals that sellers may not necessarily benefit from the analytics service. In the low-demand market, the accuracy and competition-intensifying effects of the analytics service have opposing impacts on sellers’ profits. Specifically, an adopting seller benefits from the accuracy effect. However, in the meantime, the sellers suffer from the competitionintensifying effect of the analytics service while also bearing the burden of paying the subscription fee. As a result, the combined impact of the subscription fee and the competitionintensifying effect on sellers’ profitability dominates that of the accuracy effect, leading to reduced profits for sellers in the low-demand market. Note that although sellers are worse off in the low-demand market, they still have an incentive to adopt the service because when making the adoption decision, sellers do not know the true market size, and they expect a higher revenue if they adopt the service. In the high-demand market, sellers benefit from the analytics service because both the accuracy and the competition-weakening effects positively impact sellers’ profits.

Next, we examine the impact of the analytics service on consumer surplus. We calculate the consumer surplus, denoted by ????, as:

$$
\begin{array}{r} C S = \sum_ {i = 1} ^ {2} \left(\frac {a (\mu_ {i} + \lambda \mu_ {- i})}{1 - \lambda^ {2}} d _ {i}\right) - \frac {d _ {1} ^ {2} + 2 \lambda d _ {1} d _ {2} + d _ {2} ^ {2}}{2 (1 - \lambda^ {2})} - p _ {1} d _ {1} \\ - p _ {2} d _ {2}. \end{array}
$$

In the expression of ????, the first term calculates the direct benefit of consuming products, the second term calculates the diminishing return of consuming products, and the last two terms calculate the total payment made by consumers. A detailed explanation of how we derive the expression for ???? is provided in Appendix H. We summarize the results regarding the impact of the analytics service on consumer surplus in Proposition 3.

Proposition 3 (impact of analytics service on consumer surplus): Compared to the regime without the analytics service, under the regime with the service, (a) in the lowdemand market, consumer surplus is higher, and (b) in the high-demand market, consumer surplus is lower.

As indicated in Proposition 3, under the regime with the analytics service, consumers are better off in the low-demand market but are worse off in the high-demand market. As discussed after Proposition 1, the analytics service has two effects: the accuracy effect and the competition effect. The competition effect operates in opposite directions under different market scenarios. In the low-demand market, the analytics service intensifies competition among sellers (i.e., competition-intensifying effect). Conversely, in the highdemand market, the analytics service weakens competition among sellers (i.e., competition-weakening effect). As for consumers, while they benefit from the effects of the analytics service that result in reduced product prices, they are also adversely affected by the effects that contribute to the escalation of product prices. As a result, consumers are better off in the low-demand market, where both the accuracy effect and the competition-intensifying effect of the analytics service incentivize sellers to reduce product prices. Conversely, in the high-demand market, they are worse off, as both the accuracy effect and the competition-weakening effect incentivize sellers to increase product prices.

Next, we examine the impact of analytics services on social welfare. We calculate social welfare, denoted by ????, as:

$$
\begin{array}{r l} S W = C S + \pi_ {1} + \pi_ {2} + \pi_ {p} & \\ & = \sum_ {I = 1} ^ {2} \left(\frac {a (\mu_ {i} + \lambda \mu_ {- i})}{1 - \lambda^ {2}} d _ {i}\right) \\ & - \frac {d _ {1} ^ {2} + 2 \lambda d _ {1} d _ {2} + d _ {2} ^ {2}}{2 (1 - \lambda^ {2})}. \end{array}
$$

Note that the subscription fee (??) of the analytics service, the transaction fee (??) of the marketplace service, and the price (??<sub>??</sub>) do not appear in ???? as they are transfer payments among the stakeholders. We summarize the results of social welfare in Proposition 4.

Proposition 4 (impact of analytics service on social welfare): Compared to the regime without the analytics service, under the regime with the service, (a) in the lowdemand market, social welfare is higher, and (b) in the highdemand market, social welfare is lower.

As shown in Proposition 4, social welfare under the regime with the analytics service is higher in the low-demand market but lower in the high-demand market. As shown in the formula of ????, social welfare equals the consumers’ aggregate gross value (i.e., the first two terms in the expression of ????) since all transfer payments cancel each other out. Furthermore, the consumers’ aggregate gross value increases with the number of products consumed (i.e., total market demand). As a result, in the presence of the analytics service, social welfare is enhanced when the effects of the analytics service drive higher total market demand. As discussed after Proposition 1, in the low-demand (highdemand) market, the accuracy effect and the competitionintensifying effect (the competition-weakening effect) of the service result in lower (higher) product prices, thereby driving higher (lower) total market demand and ultimately leading to higher (lower) social welfare.

## Impact of Transaction Fee ??

The transaction fee (??) plays a critical role in the platform’s trade-off between marketplace and analytics revenue. In this subsection, we investigate the impact of ?? on the equilibrium subscription fee of the analytics service and other equilibrium outcomes. First, we investigate the impact of ?? on the subscription fee and the analytics service adoption decisions. The results are summarized in Proposition 5 and illustrated in Figure 5.

Proposition 5 (impact of transaction fee ?? on subscription fee and service adoption): As the transaction fee for the marketplace service (?? ) increases, (a) in the low-demand market, the equilibrium subscription fee ??<sup>∗</sup> for the analytics service remains unchanged, and the equilibrium outcome that both sellers adopt remains unchanged, and (b) in the highdemand market, the equilibrium subscription fee ??<sup>∗</sup> may increase, and the equilibrium outcome may change from both sellers adopting to neither seller adopting.

In the low-demand market, as shown in Figure 5, the platform always sets a subscription fee that induces both sellers to adopt the service regardless of the transaction fee because, according to Lemma 3, the analytics revenue and marketplace revenue align with each other. Specifically, inducing sellers to adopt the analytics service increases both the analytics revenue and the marketplace revenue since the adopting seller will command a lower price, boosting the total market demand and hence increasing the marketplace revenue. As a result, the best strategy for the platform in the low-demand market is to choose the maximum subscription fee that induces both sellers to adopt the analytics service (i.e., ?? = ??̃ ), which is independent of ??, to maximize both the analytics revenue and the marketplace revenue.

However, in the high-demand market, as shown in Figure 5, the platform may set a higher subscription fee to induce fewer sellers to adopt the service as ?? increases. Unlike the lowdemand market, in the high-demand market, the analytics revenue and marketplace revenue sometimes conflict with each other. Specifically, inducing sellers to adopt the analytics service increases the analytics revenue but decreases the marketplace revenue since the adopting seller will command a higher price, which hurts the total market demand and hence the marketplace revenue. Thus, when ?? is relatively large, the platform focuses on the marketplace revenue by inducing less adoption from sellers. In contrast, when ?? is relatively small, the platform focuses on the analytics revenue by setting a lower subscription fee to induce more adoption from sellers.

![](/api/attachments/UWDJ7PMR/fulltext/images/eaa2fa0023afe8124d5938b7eb648481368ff202add0088195d064464bf81548.jpg)

![](/api/attachments/UWDJ7PMR/fulltext/images/97b636f36d7a3ad313fe062ae0c4236dd9562371ae4771a63144efc0a81d2c78.jpg)  
Note: Figure generated based on parameter values $a _ { L } = 2$ and $a _ { H } = 3 .$ Figures generated based on alternative parameter values exhibit qualitatively similar characteristics.  
Figure 5. Impact of ?? on Subscription Fee and Service Adoption

![](/api/attachments/UWDJ7PMR/fulltext/images/d563ba618a66cf48fd4a543ed4742c7ab1a11dd72fd839015082c39f95dc24c9.jpg)  
a. Low-demand market

![](/api/attachments/UWDJ7PMR/fulltext/images/0e93efb93f54fe8a167e8d11093e72b59cdb09fad1dce46df706241ba1bafcc3.jpg)  
b. High-demand market  
Note: Figure generated based on parameter values $a _ { L } = 2 , a _ { H } = 3 ,$ and ?? = 0.2. Figures generated based on alternative parameter values exhibit similar qualitative characteristics.  
Figure 6. Impact of ?? on Sellers’ Prices

Next, taking into consideration the impact of the transaction fee (??) on the platform’s subscription fee and the subsequent adoption decisions of sellers, we investigate the impact of ?? on sellers’ prices and profits in Proposition 6. Furthermore, Figure 6 depicts how ?? affects sellers’ prices.

Proposition 6 (impact of transaction fee ?? on sellers’ prices and profits): As the transaction fee for the marketplace service (??) increases, (a) sellers always raise their prices in the low-demand market but may reduce their prices in the high-demand market, and (b) sellers attain lower profits in both low-demand and high-demand markets.

In the low-demand market, as discussed following Proposition 5, the transaction fee (?? ) affects neither the platform’s subscription fee decision nor sellers’ adoption decisions. From the perspective of sellers, ?? only affects the cost of selling their products on the marketplace platform. More specifically, as ?? increases, sellers have to pay more to the platform for the marketplace service, hence attaining lower profits. In response, sellers partially pass this increased fee to consumers through higher product prices.

Interestingly, in the high-demand market, we find that an increase in ?? may lead to lower product prices. As depicted in Figure 6b, as ?? increases, seller ??’s price first increases and then plunges to a lower point before increasing again. The explanation is as follows: In the high-demand market, the increase in transaction fee ?? can change the platform’s subscription fee decision and hence sellers’ adoption decisions. As shown in Proposition 5, the increase in ?? may lead to the adoption outcome switching from both sellers adopting to neither adopting, which happens when the value for ?? crosses the threshold ??<sup>̃</sup> (as illustrated in Figure 6b). When such a switch occurs, as indicated by Propositions 1 and 2, the competition between sellers intensifies, leading to lower prices and profits for sellers. Note that when the increase in ?? does not lead to any change in the adoption outcomes, the impact of ?? on sellers is the same as that in the low-demand market, i.e., a higher ?? leads to higher prices and lower profits. We next investigate the impact of ?? on consumer surplus and social welfare and summarize the results in Proposition 7.

Proposition 7 (impact of transaction fee ?? on consumer surplus and social welfare): As the transaction fee for the marketplace service (??) increases, (a) in the low-demand market, consumer surplus and social welfare always decrease, and (b) in the high-demand market, consumer surplus and social welfare may increase.

In the low-demand market, as discussed following Proposition 5, the transaction fee (?? ) affects neither the platform’s subscription fee nor sellers’ adoption decisions, and as ?? increases, sellers increase their product prices to partially pass this increased fee to consumers. In response to the higher product price, the consumers consume fewer products, leading consumer surplus to decrease. Additionally, for social welfare, as mentioned in the discussion of Proposition 4, less consumption leads to a lower aggregate gross value for consumers and hence lower social welfare.

Interestingly, in the high-demand market, unlike the lowdemand market, a higher transaction fee may lead to higher consumer surplus and social welfare. In the high-demand market, the increase in the transaction fee (??) can change the platform’s subscription fee decision and hence sellers’ adoption decisions. As shown in Proposition 5, the increase in ?? may lead to the adoption outcome switching from both sellers adopting to neither adopting. When such a switch occurs in the high-demand market, the competition between sellers becomes more intense, leading to higher consumer surplus and social welfare (as indicated by Propositions 3 and 4).

## Conclusion

In this paper, we examine the economics of analytics services offered by a marketplace platform by using a game-theoretic model where sellers on the platform have inaccurate estimations of the market size. With the analytics service, sellers obtain a more accurate estimation of the market size and can further make better decisions (the accuracy effect). However, adopting the analytics service may also affect the competitive behavior of sellers (the competition effect). We investigate the impact of the analytics service in a lowdemand and a high-demand market. Table 3 summarizes the key impacts of the analytics service.

As shown in Table 3, the analytics service intensifies competition (resulting in the sellers charging lower prices) in the low-demand market but weakens competition (resulting in the sellers charging higher prices) in the high-demand market. Furthermore, we show that in the low-demand market, consumers are better off while sellers are worse off; however, the opposite holds true in the high-demand market. Additionally, we explore the important interplay between the platform’s two revenue sources: the analytics revenue from the subscription fee for the analytics service and the marketplace revenue from the transaction fee for the marketplace service. We find that depending on the market scenario, the platform’s incentives for managing the two revenue sources can align or conflict with each other. More specifically, in the high-demand market, encouraging sellers to adopt the analytics service enables the platform to enjoy higher analytics revenue. However, this comes at the expense of lower marketplace revenue. The reason for this is that in the high-demand market, both the accuracy effect and the competition-weakening effect lead to elevated product prices, resulting in a decrease in total market demand and subsequently reducing marketplace revenue. Thus, in the high-demand market, the analytics revenue and the marketplace revenue are in conflict with each other. Conversely, in the low-demand market, these two revenue sources align with each other. Specifically, the adoption of the service leads to an increase in analytics revenue. Concurrently, the accuracy effect and the competitionintensifying effect work in tandem, driving higher total market demand and generating increased marketplace revenue. Consequently, depending on the specific market scenario, the platform may need to carefully strike a delicate balance between these two revenue sources. Moreover, in the highdemand market, the adoption of the analytics service leads to a reduction in consumer surplus that outweighs the gains in the platform’s revenue and sellers’ profits, resulting in a decline in social welfare. In contrast, the adoption of the service in the low-demand market contributes positively to social welfare. In the following, we discuss our study’s theoretical contributions and managerial implications.

<table><tr><td colspan="4">Table 3. Impact of Analytics Service</td></tr><tr><td>Players</td><td>Outcomes</td><td>Low-demand market</td><td>High-demand market</td></tr><tr><td rowspan="2">Sellers</td><td>Prices</td><td>decrease</td><td>increase</td></tr><tr><td>Profit</td><td>decrease</td><td>increase</td></tr><tr><td>Consumer</td><td>Consumer surplus</td><td>increase</td><td>decrease</td></tr><tr><td rowspan="2">Platform</td><td>Analytics revenue</td><td>increase</td><td>increase</td></tr><tr><td>Marketplace revenue</td><td>increase</td><td>decrease</td></tr><tr><td>Social planner</td><td>Social welfare</td><td>increase</td><td>decrease</td></tr></table>

## Theoretical Contributions and Implications

Our research makes several theoretical contributions to the literature. First, to our knowledge, we are the first to formally investigate the impacts of analytics services on a marketplace platform. In this paper, we systematically characterize the unique feature of this new business model. More specifically, unlike the previous studies on market information services and demand information sharing (e.g., Gal-Or, 1986; Chang and Lee, 1994; Arora and Fosfuri, 2005), this paper investigates analytics services offered by a marketplace platform. In this context, the platform serves the unique dual role of marketplace facilitator and market information provider and may hence face a trade-off between marketplace and analytics revenue. To the best of our knowledge, the study is among the first attempts to formally study this important trade-off. Accordingly, we find that platforms (as an information brokerage) may not benefit from providing market information to sellers. Specifically, in high-demand markets, platforms can generate higher analytics revenue by serving as market information providers; however, this may come at the cost of lower marketplace revenue related to their role as marketplace facilitators due to decreased total market demand. When the transaction fee is relatively high, the loss in marketplace revenue outweighs the gain in analytics revenue, leaving the platform worse off providing market information through the analytics service. To the best of our knowledge, this outcome has rarely been documented in the existing literature on market information services and demand information sharing (e.g., Vives, 1984; Bergemann & Bonatti, 2015; Kastl et al., 2018; Tsunoda and Zennyo, 2021). Second, this paper employs a distinct research methodology, setting it apart from previous studies in the broader field of business intelligence and analytics (e.g., Moon & Russell, 2008; Chen et al., 2012; Božič & Dimovski, 2019; Dzyabura & Hauser, 2019). Existing literature in this area primarily focuses on empirical and technical investigations, aiming to enhance algorithm performance and explore the influence of business intelligence and analytics tools on firm performance. However, due to the prevailing research methods, the discussions regarding the effects of these tools on strategic interactions among stakeholders in the platform ecosystem, as well as their impact on consumer surplus and social welfare, have been limited. By adopting an analytical modeling approach, this paper aims to delve into the impact of analytics services on such strategic interactions and gain a more comprehensive understanding of their implications for various economic outcomes, including consumer surplus and social welfare. Third, our research adds to the literature on platform-based functions (e.g., Li et al., 2009; Walia & Zahedi, 2013; Chen et al., 2016; Li et al., 2019) by studying analytics services, a novel platform-based function that has not yet been studied. Unlike conventional platform-based functions, this novel function does not directly provide added value to sellers; instead, as explicitly modeled in this paper, it benefits sellers by providing them with valuable market information, which in turn helps them make more informed decisions. As a result, when exploring the determinants of the impacts of platform-based functions, we go beyond the existing literature by exploring how the market scenario (high- or low-demand market) influences the impact of the analytics service as a platform-based function. Consequently, our findings demonstrate that the impacts of the analytics service critically depend on the underlying market scenarios. For example, we find that the analytics service intensifies seller competition in a low-demand market but weakens it in a high-demand market. Furthermore, we contribute to this stream of literature by investigating the pricing of the analytics service as a platform-based function, an aspect overlooked in previous studies.

As the first attempt to model the analytics service, this theoretical framework helps set the agenda for more research in this area. Based on the proposed theoretical framework, there are many promising future directions that are worth exploring. Regarding market structure, future work could expand upon the current setting and examine the impact of analytics services in a setting where multiple platforms compete with each other. Since analytics services have an impact on both seller profitability and consumer surplus, they could be leveraged to attract sellers and consumers and may thus play an important role in the competition among platforms.

Considering platforms’ revenue models, future studies could investigate the impact of analytics services under revenue models beyond the transaction fee and commission fee revenue models examined in this paper. Considering platforms’ strategic decisions, a potential avenue for future research would be to incorporate the transaction fee for the marketplace service as an endogenous variable. Our results (e.g., Proposition 5) highlight the significant role that the transaction fee plays in the interplay between analytics and marketplace revenue; thus, it would also be intriguing to investigate how the presence of the analytics service in turn impacts the transaction fee.

Additionally, in terms of the platform’s knowledge of market size, to focus on the key trade-off, we assume that the platform possesses accurate knowledge of consumer market size. However, future research could extend our findings by exploring scenarios in which the platform lacks accurate information on the true market size and investigating how the quality of the information available to the platform impacts our current conclusions.

## Managerial Implications

Our research has several managerial implications. First, since the transaction fee impacts the interplay between the two revenue sources, platforms should take the transaction fee into account when setting subscription fees for the analytics service. If the transaction fee increases, platforms should focus more on marketplace revenue by inducing fewer (more) sellers to adopt the analytics service in a high-demand (low-demand) market to increase the total demand. On the other hand, if the transaction fee decreases, platforms should focus more on the analytics revenue.

More importantly, when deciding on the subscription fee for analytics services, platforms should carefully evaluate the market scenarios of the marketplace (i.e., whether the market is a low-demand or high-demand market). In practice, platforms could find out the true market size based on, for example, the information on transaction volume over a certain period (Melendez, 2019). Consequently, when setting the optimal subscription fee, depending on the market scenario, the platform may need to consider the aforementioned tradeoff between the analytics revenue and the marketplace revenue to maximize its profit.

Moreover, this paper provides important implications for sellers. Although the analytics service serves as a tool to help sellers gain more knowledge about the consumer market, interestingly, we find that sellers do not necessarily benefit from such a service. The analytics service actually hurts sellers in a low-demand market since adopting the analytics service drives fierce seller competition. Sellers should be aware of such a potential downside of the analytics service when deciding whether to adopt the service. In addition, sellers should carefully assess their popularity when deciding whether to adopt the service.

This paper also generates some meaningful implications for consumers. Our results reveal that the impact of analytics services on consumers depends on market scenarios. In a lowdemand market, adopting an analytics service leads sellers to lower their prices to better cater to the market, which benefits consumers in the market. In contrast, in a high-demand market, adopting the service leads sellers to raise their prices, leaving consumers in the market worse off. Consumers should be aware of this potential downside of analytics services. Additionally, policymakers should devise appropriate policies to protect consumers’ interests in the presence of analytics services, especially in high-demand markets. Furthermore, according to our study, policymakers should consider the potential negative impact of analytics services on social welfare. Our findings suggest that analytics services can only increase social welfare in low-demand markets. Thus, policymakers should carefully evaluate the market conditions and restrict the adoption of analytics services in high-demand markets.

## Acknowledgments

Dengpan Liu’s research was supported in part by the National Natural Science Foundation of China [Grant NSFC-72071118] and WU Jiapei Award for Information Economics in 2019 [Grant M19100295]. Dengpan Liu is the corresponding author of this paper.

## References

Armstrong, M. (2006). Competition in two-sided markets. RAND Journal of Economics, 37(3), 668-691. https://doi.org/ 10.1111/j.1756-2171.2006.tb00037.x

Arora, A., & Fosfuri, A. (2005). Pricing diagnostic information. Management Science, 51(7), 1092-1100. https://doi.org/ 10.1287/mnsc.1050.0362

Bergemann, D., & Bonatti, A. (2015). Selling cookies. American Economic Journal, 7(3), 259-294. https://doi.org/ 10.1257/mic.20140155

Božič, K., & Dimovski, V. (2019). Business intelligence and analytics use, innovation ambidexterity, and firm performance: A dynamic capabilities perspective. The Journal of Strategic Information Systems, 28(4), Article 101578. https://doi.org/ 10.1016/j.jsis.2019.101578

Chang, C. H., & Lee, C. W. J. (1994). Optimal pricing strategy in marketing research consulting. International Economic Review, 35(2), 463-478. https://doi.org/10.2307/2527064

Chen, F. Y., Yan, H., & Yao, L. (2004). A newsvendor pricing game. IEEE Transactions on Systems, Man, and Cybernetics-Part A: Systems and Humans, 34(4), 450-456. https://doi.org/ 10.1109/TSMCA.2004.826290

Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business intelligence and analytics: From big data to big impact. MIS Quarterly, 36(4), 1165-1188. https://doi.org/10.2307/41703503

Chen, J., Ming, F., & Li, M. (2016). Advertising versus brokerage model for online trading platforms. MIS Quarterly, 40(3), 575- 596. https://doi.org/10.25300/MISQ/2016/40.3.03

Cho, I. K., & Kreps, D. M. (1987). Signaling games and stable equilibria. The Quarterly Journal of Economics, 102(2), 179- 221. https://doi.org/10.2307/1885060

Choi, S. C., & Coughlan, A. T. (2006). Private label positioning: Quality versus feature differentiation from the national brand. Journal of Retailing, 82(2), 79-93. https://doi.org/10.1016/ j.jretai.2006.02.005

Darrough, M. N. (1993). Disclosure policy and competition: Cournot vs. Bertrand. The Accounting Review, 68(3), 534-561.

Dzyabura, D., & Hauser, J. R. (2019). Recommending products when consumers learn their preference weights. Marketing Science, 38(3), 417-441. https://doi.org/10.1287/mksc.2018. 1144

eBay. (2023). What are eBay research tools. https://pages.ebay. com/seller-center/listing-and-marketing/terapeak.html

Gal-Or, E. (1986). Information transmission: Cournot and Bertrand equilibria. The Review of Economic Studies, 53(1), 85-92. https://doi.org/10.2307/2297593

Go, R. (2020). How to source products on eBay using Terapeak. Deliverr. https://deliverr.com/blog/source-ebay-products-terapeak/

Godin, M. (2018). How we used eBay analytics to increase sales. Crazylister. https://crazylister.com/blog/ebay-analytics-increasesales/

Gümüş, M. (2014). With or without forecast sharing: Competition and credibility under information asymmetry. Production and Operations Management, 23(10), 1732-1747. https://doi.org/ 10.1111/poms.12192

Ha, A. Y., Tong, S., & Zhang, H. (2011). Sharing demand information in competing supply chains with production diseconomies. Management Science, 57(3), 566-581. https://doi.org/10.1287/mnsc.1100.1295

Häckner, J. (2000). A note on price and quantity competition in differentiated oligopolies. Journal of Economic Theory, 93(2), 233-239. https://doi.org/10.1006/jeth.2000.2654

Jain, A., Seshadri, S., & Sohoni, M. (2011). Differential pricing for information sharing under competition. Production and Operations Management, 20(2), 235-252. https://doi.org/ 10.1111/j.1937-5956.2010.01161.x

Jaynes, E. (2003). Probability theory: The logic of science. Cambridge University Press.

Kastl, J., Pagnozzi, M., & Piccolo, S. (2018). Selling information to competitive firms. Rand Journal of Economics, 49(1), 254- 282. https://doi.org/10.1111/1756-2171.12226

Kwark, Y., Chen, J., & Raghunathan, S. (2018). User-generated content and competing firms’ product design. Management Science, 64(10), 4608-4628. https://doi.org/10.1287/mnsc. 2017.2839

Li, H., Fang, Y., Lim, K. H., & Wang, Y. (2019). Platform-based function repertoire, reputation, and sales performance of emarketplace sellers. MIS Quarterly, 43(1), 207-236. https://doi.org/10.25300/MISQ/2019/14201

Li, S., Srinivasan, K., & Sun, B. (2009). Internet auction features as quality signals. Journal of Marketing, 73(1), 75-92. https://doi.org/10.1509/jmkg.73.1.075

Melendez, S. (2019). What is the definition of market size? Chron. https://smallbusiness.chron.com/definition-market-size-65724.html

Moon, S., & Russell, G. J. (2008). Predicting product purchase from inferred customer similarity: An autologistic model approach. Management Science, 54(1), 71-82. https://doi.org/ 10.1287/mnsc.1070.0760

Nasrudin, A. (2022). Market size: How to calculate, types, importance. Peboin. https://penpoin.com/market-size/

Raith, M. (1996). A general model of information sharing in oligopoly. Journal of Economic Theory, 71(1), 260-288. https://doi.org/10.1006/jeth.1996.0117

Rochet, J., & Tirole, J. (2003). Platform competition in two-sided markets. Journal of the European Economic Association, 1(4), 990-1029. https://doi.org/10.1162/154247603322493212

Roggio, A. (2021). How to use Terapeak for eBay 2021. PracticalEcommerce. https://www.practicalecommerce.com/ how-to-use-terapeak-for-ebay-2021

Singh, N., & Vives, X. (1984). Price and quantity competition in a differentiated duopoly. The Rand Journal of Economics, 15(4), 546-554. https://doi.org/10.2307/2555525

Song, T., Huang, J., Tan, Y., & Yu, Y. (2019). Using user-and marketer-generated content for box office revenue prediction: Differences between microblogging and third-party platforms. Information Systems Research, 30(1), 191-203. https://doi.org/ 10.1287/isre.2018.0797

Symeonidis, G. (2003). Comparing Cournot and Bertrand equilibria in a differentiated duopoly with product R&D. International Journal of Industrial Organization, 21(1), 39-55. https://doi.org/10.1016/S0167-7187(02)00052-8

Terry, E. (2023, September 24). Terapeak review 2022: Is this tool worth spending. Bloggersideas. https://www.bloggersideas. com/terapeak-review/

Tsunoda, Y., & Zennyo, Y. (2021). Platform information transparency and effects on third‐party suppliers and offline retailers. Production and Operations Management, 30(11), 4219-4235. https://doi.org/10.1111/poms.13518

UNCTAD. (2022). COVID-19 boost to e-commerce sustained into 2021, new UNCTAD figures show. https://unctad.org/ news/covid-19-boost-e-commerce-sustained-2021-newunctad-figures-show

Villarica, G. (2017). Terapeak forecasts eBay sales for Shopify sellers. Medium. https://medium.com/@grace3vil/terapeakforecasts-ebay-sales-for-shopify-sellers-24715b3092c8

Vives, X. (1984). Duopoly information equilibrium: Cournot and Bertrand. Journal of Economic Theory, 34(1), 71-94. https://doi.org/10.1016/0022-0531(84)90162-5

Walia, N., & Zahedi, F. M. (2013). Success strategies and web elements in online marketplaces: A moderated-mediation analysis of seller types on eBay. IEEE Transactions on Engineering Management, 60(4), 763-776. https://doi.org/ 10.1109/TEM.2013.2272194

Wang, H., Gurnani, H., & Erkoc, M. (2016). Entry deterrence of capacitated competition using price and non‐price strategies. Production and Operations Management, 25(4), 719-735. https://doi.org/10.1111/poms.12500

Xiao, Q. (2020). The BusinessAdvisor Market competition function helps shops break through barriers. Yubaibai. http://www. yubaibai.com.cn/article/5596838.html

Zhang, H. (2002). Vertical information exchange in a supply chain with duopoly retailers. Production and Operations Management, 11(4), 531-546. https://doi.org/10.1111/j.1937- 5956.2002.tb00476.x

Zhang, J., Fang, X., & Sheng, O. L. (2006). Online consumer search depth: Theories and new findings. Journal of Management Information Systems, 23(3), 71-95. https://doi.org/10.2753/ MIS0742-1222230304

Zhao, X., & Xue, L. (2012). Competitive target advertising and consumer data sharing. Journal of Management Information Systems, 29(3), 189-222. https://doi.org/10.2753/MIS0742- 1222290306

## Author Biographies

Zhe Wang is an assistant professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. from the School of Economics and Management at Tsinghua University. His primary research interests lie in the area of the economics of information systems, with a particular focus on fairness regulation, digital healthcare, and digital platforms. Zhe mainly employs the analytical modeling approach in his research.

Hong Guo is a professor of information systems at the W. P. Carey School of Business, Arizona State University. Hong studies emerging IT phenomena by characterizing their key design features, examining firms’ corresponding strategies, and analyzing the impacts of related IT policies. Her areas of expertise include digital platforms, business data visualization, digital games, algorithmic interpretability, net neutrality, etc. She teaches business data visualization to graduate students at ASU.

Dengpan Liu is a full professor with tenure in the Department of Management Science and Engineering at the School of Economics and Management, Tsinghua University. He received his Ph.D. in management science with a concentration in information systems from the University of Texas at Dallas in 2006. His research interests lie primarily in the area of economics of information systems, with a particular focus on digital platforms and e-commerce. He has published in journals such as Management Science, Information Systems Research, and MIS Quarterly. He currently serves as a senior editor of Production and Operations Management.

## Appendix A

## Model Extension with Inventory Decision: A Newsvendor Modeling Approach

In this appendix, we extend our analysis in the main model to a case where the sellers make both inventory and pricing decisions in Stage 3. With the other modeling components remaining unchanged, we follow Chen et al. (2004) to calculate seller ??’s realized demand and profit as follows:

$$
d _ {i} = \min \{q _ {i}, \mu_ {i} a - p _ {i} + \lambda p _ {- i} \} \mathrm{and}
$$

$$
\pi_ {i} = (p _ {i} - f) d _ {i} - r \max \{0, q _ {i} - (\mu_ {i} a - p _ {i} + \lambda p _ {- i}) \} - I _ {i} s,
$$

respectively, where $q _ { i }$ is the inventory decision of seller ?? and ?? is the holding cost of unit inventory. Note that when $r = 0 ,$ , the model in this extension reduces to the main model. Due to the sellers’ uncertainty about the market size (??), they face a typical trade-off when making inventory decisions. Specifically, they must balance maintaining a high inventory level (i.e., setting a high $q _ { i } ) .$ , which may result in a relatively high inventory holding cost, with maintaining a low inventory level (i.e., setting a low $q _ { i } ) .$ , which potentially leads to lost sales. Similar to the main model, we use backward induction to analyze the sellers’ pricing and inventory decisions in Stage 3, and then the sellers’ adoption decisions in Stage 2, followed by the platform’s subscription fee decision in Stage 1. In this model extension, we focus on the key effects of analytics services and study the symmetric case where the sellers have the same popularity $( \mathrm { i . e . , } \mu _ { 1 } = \mu _ { 2 } = 1 / 2 )$

Lemma A1 below summarizes the platform’s subscription fee decision and the sellers’ decisions on analytics service adoption. All the proofs of lemmas and propositions in this appendix are provided in Appendix G.

Lemma A1 (platform’s subscription fee and sellers’ adoption of the analytics service): (a) If the market size is large $( a = a _ { H } ) ,$ the inventory holding cost is relatively low $( r \leq \tilde { r } ) ,$ , and the transaction fee is relatively high $( f > \tilde { f } ^ { \prime \prime } ) ,$ then the platform sets a high subscription fee $( s ^ { * } > \tilde { s } ^ { \prime } )$ such that neither seller adopts; (b) otherwise, the platform sets a low subscription fee $( s ^ { * } = \tilde { s } ^ { \prime } )$ to induce the adoption by both sellers.

The expressions of ??̃<sup>′</sup>, ??̃ and $\tilde { f } ^ { \prime \prime } c a n$ be found in the proof of Lemma A1.

The structure of the equilibrium subscription fee remains the same as that in the main model. More specifically, the platform is always incentivized to induce the adoption from sellers in the low-demand market by setting a low subscription fee, whereas sometimes, it may not want any seller to adopt the service in the high-demand market. Additionally, we can analytically show that the threshold ${ \tilde { s } } ^ { \prime }$ increases with the inventory holding cost (??). The intuition is that a higher inventory holding cost makes the market uncertainty more harmful to the sellers. As a result, as an effective tool to reduce market uncertainty, the analytics service benefits the sellers more as ?? increases. Accordingly, the sellers’ willingness to pay for the analytics service increases, leading to an increased ${ \tilde { s } } ^ { \prime } .$

The lemma below presents the sellers’ equilibrium pricing and inventory decisions.

Lemma A2 (the sellers’ pricing and inventory decisions): (a) if the market size is large $( a = a _ { H } ) ,$ the transaction $f e e$ is relatively high $( f > \tilde { f } ^ { \prime \prime } )$ , and the inventory holding cost is relatively low $( r \leq \tilde { r } )$ , then the pricing and inventory decisions of the sellers are $\begin{array} { r } { p _ { i } = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } } \end{array}$ and $\begin{array} { r } { q _ { i } = \frac { a _ { H } ( 3 - \lambda ) - ( a _ { L } + 4 f ) ( 1 - \lambda ) } { 4 ( 2 - \lambda ) } } \end{array}$ , respectively; (b) otherwise, the pricing and inventory decisions of the sellers are $\begin{array} { r } { p _ { i } = \frac { a _ { H } + 2 f } { 4 - 2 \lambda } a n d q _ { i } = } \end{array}$ $\frac { a _ { H } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } ,$ , respectively, in the high-demand market, and $\begin{array} { r } { p _ { i } = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } a n d q _ { i } = \frac { a _ { L } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } , } \end{array}$ , respectively, in the low-demand market.

The expressions of ??̃ can be found in the proof of Lemma A2.

Here, we would like to note that, based on Lemma A1, in case (a) of Lemma A2, neither seller adopts the service, while in case (b), both sellers adopt the service. In the following, based on the results of Lemmas A1 and $\mathbf { A } 2 ,$ , we discuss the impact of the analytics service on sellers’ pricing and inventory decisions.

Proposition A1 (impact of analytics service on sellers’ pricing decisions): Compared to the regime without the analytics service, under the regime with the service, (a) in the low-demand market, the sellers command lower prices, and (b) in the high-demand market, the sellers command higher prices.

According to Proposition A1, with the analytics service, the accuracy effect and the competition-intensifying effect (competition-weakening effect) lead sellers to command lower (higher) prices in the low-demand (high-demand) market. Such a result is the same as that in the main model (see Proposition 1). In the following proposition, we study the impact of the analytics service on sellers’ inventory decisions.

Proposition A2 (impact of analytics service on sellers’ inventory decisions): Compared to the regime without the analytics service, under the regime with the service, (a) in the low-demand market, the sellers make the same inventory decision if the holding cost is relatively high $( r > \tilde { r } )$ , and choose a lower inventory level; otherwise, (b) in the high-demand market, the sellers choose a higher inventory level if the holding cost is relatively high $( r > \tilde { r } )$ , and choose a lower inventory level otherwise.

In the low-demand market, we find that when the inventory holding cost is relatively high $( r \geq \tilde { r } ) $ , adopting the analytics service does not impact the sellers’ inventory decisions. When the inventory holding cost (??) is high, in the absence of analytics services, to avoid the potential overstock cost, the sellers will maintain a low inventory level that can only meet the consumers’ demand in the low-demand market. With the analytics service, the seller becomes aware that the market demand is low and thus maintains an inventory level to meet this low demand. As a result, the sellers’ inventory decisions remain unchanged regardless of their adoption of the analytics service.

In the high-demand market, we find that when the inventory holding cost is relatively low $( r < \tilde { r } )$ , the sellers actually maintain a lower inventory with the analytics service. The reason is that, without the analytics service, when ?? is low, the sellers are willing to bear the potential overstock cost to keep an inventory level that can always meet consumers’ demand to avoid the potential risk of lost sales. With the analytics service, the more informed sellers also maintain an inventory level that can satisfy the demand in the high-demand market. However, the analytics service adoption in the high-demand market weakens the competition, leading to higher product prices. As the prices increase, sellers’ demand decreases, leading the sellers to choose a lower inventory level to satisfy consumers’ demand.

## Appendix B

## Model Extension with ?? Symmetric Sellers

In this appendix, we extend the sellers’ competition structure from two competing sellers (as analyzed in the main model) to ?? $( n \geq 2 )$ competing sellers. Specifically, we assume ?? sellers with equal popularity, denoted as $\mu _ { i } = 1 / n$ , where $i = 1 , 2 , \dots , n$ . Following backward induction, we first analyze the sellers’ pricing decisions in Stage 3, then their adoption decisions in Stage 2, and finally the platform’s subscription fee decision in Stage 1.

First, we examine sellers’ pricing decisions in Stage 3 and summarize the results in Lemma B1 below. All the proofs of lemmas and propositions are relegated to Appendix G.

Lemma B1 (sellers’ pricing decisions with ?? symmetric sellers): Given that the true market size is ??, ?? sellers adopt the service, and seller ??’s own adoption decision is $I _ { i } ,$ seller ?? makes the pricing decision $\pmb { p } _ { i }$ as follows:

<table><tr><td></td><td> $I_i = 1$ </td><td> $I_i = 0$ </td></tr><tr><td> $a = a_H$ </td><td> $p_i = \frac{a_H + a_L + 2fn}{4n + 2n\lambda - 2n^2\lambda} + \frac{a_H - a_L}{4n + 2n\lambda - 2nm\lambda}$ </td><td> $p_i = \frac{a_H + a_L + 2fn}{4n + 2n\lambda - 2n^2\lambda}$ </td></tr><tr><td> $a = a_L$ </td><td> $p_i = \frac{a_H + a_L + 2fn}{4n + 2n\lambda - 2n^2\lambda} - \frac{a_H - a_L}{4n + 2n\lambda - 2nm\lambda}$ </td><td> $p_i = \frac{a_H + a_L + 2fn}{4n + 2n\lambda - 2n^2\lambda}$ </td></tr></table>

To illustrate the results in Lemma B1, we use Figure B1 to depict how seller ?? makes her pricing decision based on the adoption decisions and the market scenario.

![](/api/attachments/UWDJ7PMR/fulltext/images/adb39f1f05450f1e9f6dd6a11b2f7b09a6adcaf6eba4fb50809f5805b519b99f.jpg)

![](/api/attachments/UWDJ7PMR/fulltext/images/9a7dda531bec8533a6e60024f5bb35a4e9ca0a8456bdd292d4fb7450cd9103a9.jpg)  
Note: Figure B1 is generated based on parameters values $a _ { L } = 2 , a _ { H } = 3 , \lambda = 0 . 2$ , and $n = 4 .$ . The figures generated based on alternative parameter values exhibit similar qualitative characteristics.

As indicated by Lemma B1, the pricing strategy of nonadopting sellers remains the same as in the regime without the analytics service, unaffected by other sellers’ adoption decisions and the true market size. For adopting sellers, they set higher prices in the high-demand market but lower prices in the low-demand market. Furthermore, unlike nonadopting sellers, an adopting seller’s pricing strategy also depends on the adoption decisions of other sellers. As shown in Figure B1, in the low-demand (high-demand) market, the adopting seller charges lower (higher) prices as more sellers adopt the service.

Next, we investigate how the sellers should make the adoption decisions in Stage 2. Lemma B2 summarizes the sellers’ adoption decisions in Stage 2 under varying subscription fee values.

Lemma B2 (sellers’ adoption of the analytics service with ?? symmetric sellers): If the subscription fee (??) for the analytics service is relatively low $\begin{array} { r } { ( s \leq \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } ) . } \end{array}$ , all sellers adopt the service; otherwise, none of the sellers adopts the service.

Similar to the sellers’ adoption decisions in the main model, as indicated by Lemma B2, all sellers opt to adopt the service if the subscription fee is relatively low, while none of them choose to adopt the service otherwise. Furthermore, we find that the maximum subscription fee that sellers are willing to pay $\begin{array} { r } { ( \mathrm { i . e . , } \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } ) } \end{array}$ decreases as the total number of sellers increases. The reason is that a more crowded market leads to lower potential revenue for each seller, reducing their potential benefits from the analytics service. Therefore, the sellers’ willingness to pay for the service decreases with ??.

Finally, we examine how the platform should set the equilibrium subscription fee for the analytics service in Stage 1, and the results are summarized in Lemma B3.

Lemma B3 (platform’s equilibrium subscription fee with ?? symmetric sellers): (a) If the market is a high-demand market $( { \pmb a } = { \pmb a } _ { H } )$ and the transaction fee is relatively high $( f > \tilde { f } ^ { \prime \prime \prime } )$ , the platform sets a high subscription fee $\begin{array} { r } { ( \pmb { S } ^ { * } > \frac { ( \pmb { a } _ { H } - \pmb { a } _ { L } ) ^ { 2 } } { 4 \pmb { n } ^ { 2 } ( 2 + \lambda - \pmb { n } \lambda ) ^ { 2 } } ) } \end{array}$ to price the sellers out of the adoption; (b) otherwise, the platform sets a low subscription fee $\begin{array} { r } { ( \pmb { S } ^ { * } = \frac { ( \pmb { a } _ { H } - \pmb { a } _ { L } ) ^ { 2 } } { 4 \pmb { n } ^ { 2 } ( 2 + \lambda - \pmb { n } \lambda ) ^ { 2 } } ) } \end{array}$ to induce the adoption of all sellers.

The structure of the equilibrium subscription fee is the same as in the main model. That is, the platform is always incentivized to induce adoption by sellers in the low-demand market by setting a low subscription fee, whereas sometimes, the platform may prefer no seller to adopt the service in the high-demand market.

Interestingly, in this extension, we find that the platform’s total analytics revenue, generated from inducing all sellers to adopt, actually decreases with the number of sellers (??). The reason is that while a higher ?? enables the platform to charge more sellers for the analytics service, it also reduces the sellers’ willingness to pay for the analytics service and hence lowers the subscription fee the platform can charge from each seller. The latter effect is found to dominate the former effect. As a result, the platform’s total analytics revenue from inducing all sellers to adopt decreases as the market becomes more crowded

Next, we examine the impact of the total number of sellers (??) on the platform’s equilibrium subscription fee.

Proposition B1 (impact of ?? on the platform’s equilibrium subscription fee): As the total number of ?? increases, (a) in the low-demand market, the equilibrium subscription fee decreases, and (b) in the high-demand market, the equilibrium subscription fee may increase.

As shown in Proposition B1, in the low-demand market, the equilibrium subscription fee decreases as ?? increases. The reason is that the platform always encourages all sellers to adopt the analytics service in the low-demand market and hence sets the subscription fee to sellers willingness to pay, which decreases with ??. Interestingly, we find that in the high-demand market, the equilibrium subscription fee may increase with ??. The reason is that in the high-demand market, the platform faces a trade-off between the marketplace revenue and the analytics revenue when determining the subscription fee. This trade-off is further impacted by the total number of sellers (??). More specifically, by inducing sellers to adopt the service, the platform gains in analytics revenue but experiences losses in marketplace revenue; as n increases, the gains in analytics revenue decrease, whereas the losses in marketplace revenue may increase. Thus, as ?? increases, the platform may shift from inducing all sellers to adopt to inducing none. Figure B2 below illustrates how the total number of sellers (??) impacts the sellers’ adoption outcomes in equilibrium.

![](/api/attachments/UWDJ7PMR/fulltext/images/aa746b8e63c33094f11f824520855ff5ad4380e459d23c00e7b143094e8c0e33.jpg)  
Note: Figure B2 is generated based on parameters values $a _ { L } = 2$ and $a _ { H } = 3 .$ . The figures generated based on alternative parameter values exhibit similar qualitative characteristics.

## Figure B2. Sellers’ Adoption Outcomes with ?? Symmetric Sellers

As shown in Figure B2, all sellers adopt the service in the upper-left region, while no seller adopts the service in the lower-right region, with the boundary between the two regions changing with ??. For example, in the shaded area in Figure B2, no seller adopts the service when ?? = 5, but all sellers adopt the service when ?? = 2 and ?? = 10. As illustrated in this example, the impact of ?? on the adoption outcome in equilibrium is non-monotonic. Thus, an increase in ?? can either lead to the platform increasing the subscription fee to the point where none of the sellers adopts the service or decreasing the subscription fee so that all sellers adopt the service.

## Appendix C

## Model Extension with Asymmetric Sellers in Popularity

In reality, the popularity of sellers on the platform, as measured by $\mu _ { i } ,$ can vary. In this section, to investigate the impacts of such heterogeneity in sellers’ popularity, we study an asymmetric setting where the sellers on the platform have different levels of popularity. Without loss of generality, we assume that seller 1’s product is more popular than seller $2 ^ { \circ } \mathrm { s } \left( \mathrm { i . e . , } \mu _ { 1 } \geq \mu _ { 2 } \right)$ . We hereafter refer to sellers 1 and 2 as the more popular and less popular sellers, respectively. For ease of notation, we let $\mu _ { 1 } = \mu$ and $\mu _ { 2 } = 1 - \mu$ (recall that $\mu _ { 1 } + \mu _ { 2 } = 1 )$ , with $1 / 2 \leq \mu <$ 1; hence, a higher value of ?? indicates a higher heterogeneity in sellers’ popularity.

## Equilibrium Analysis with Asymmetric Sellers

In this subsection, we first summarize sellers’ adoption decisions regarding the analytics service based on the subscription fee, and then we present the subscription fee charged by the platform in equilibrium. The lemma below summarizes sellers’ adoption decisions when the subscription fee of the analytics service is given.

Lemma C1 (sellers’ adoption of the analytics service with asymmetric sellers):

(a) If the two sellers are highly differentiated $( i . e . , \mu > \tilde { \mu } )                .$

(a1) when the subscription fee is high (i.e., $s > \tilde { s } _ { H } ) ,$ , neither seller adopts the service;

(a2) when the subscription fee is medium $( i . e . , \tilde { s } _ { L } < s \leq \tilde { s } _ { H } ) ,$ , only the more popular seller adopts the service;

(a3) when the subscription fee is low $( i . e . , s \leq \tilde { s } _ { L } ) ,$ , both sellers adopt the service.

(b) If the two sellers are not highly differentiated (i.e., $\mu \leq \tilde { \mu } ) .$

(b1) when the subscription fee is high $( i . e . , s > \tilde { s } _ { L } ) ,$ , neither seller adopts the service;

(b2) when the subscription fee is low $( i . e . , s \leq \tilde { s } _ { L } ) ,$ , both sellers adopt the service.

Note that the expressions of ??̃, $\tilde { s } _ { L } ,$ , and $\tilde { s } _ { H }$ can be found in the proof of Lemma C1.

As indicated by Lemma C1, unlike the case of symmetric sellers (see the Adoption and Pricing of Analytics Service section), when the sellers have asymmetric popularity, it is possible that only one seller adopts the service. When this asymmetric adoption outcome occurs in the case with asymmetric sellers, it is always the more popular one who adopts the service. The reason is as follows. Compared to the less popular one, the more popular seller holds a larger market share and can thus derive greater benefits from the service. Therefore, the more popular seller may still be willing to pay for the service even when the less popular seller is not. More specifically, when the two sellers are highly differentiated $( \mu > \tilde { \mu } )$ , the discrepancy in benefits derived from the analytics service becomes substantial enough to drive the asymmetric adoption outcome; otherwise, only symmetric adoption outcomes (both adopting or neither adopting) are possible.

Next, we summarize our findings concerning the platform’s equilibrium subscription fee and the corresponding adoption decisions of sellers under the asymmetric setting in the following lemma.

Lemma C2 (platform’s subscription fee and sellers’ adoption of the analytics service with asymmetric sellers): In equilibrium, the platform’s subscription fee and the sellers’ adoption decisions are:

(a) $s ^ { * } > \tilde { s } _ { H }$ and neither seller adopts the service, if the market size is high $( i . e . , a = a _ { H } )$ , and the transaction fee is relatively large $( i . e . ,$ $f > \tilde { f } ^ { \prime } ) ,$

(b) $s ^ { * } = \tilde { s } _ { H }$ and only the more popular seller adopts the analytics service if two sellers are highly differentiated (i.e., $\mu \geq \widetilde { \mu } ^ { \prime } ) ;$

(c) $s ^ { * } = \tilde { s } _ { L }$ and both sellers adopt the service otherwise.

Note that the expressions of ??̃<sup>′</sup> and ??<sup>̃′</sup> can be found in the proof of Lemma C2.

For illustrative purposes, we depict the equilibrium adoption outcomes in Figure C1.

Figure C1. Sellers’ Equilibrium Adoption Outcomes  
![](/api/attachments/UWDJ7PMR/fulltext/images/38c96f1dcd50b50b69bdddaca88a1ace799a1a0ddcc4c0d64398f01ac6e3f34e.jpg)

![](/api/attachments/UWDJ7PMR/fulltext/images/69554793d5b8b6b1c874a5f546037adeaf058a33f051f6c0da836e46786af091.jpg)  
Note: Figure C1 is generated based on parameters values $a _ { L } = 2 , a _ { H } = 3 ,$ and $\lambda = 0 . 2 .$ The figures generated based on alternative parameter values exhibit similar qualitative characteristics.

In the low-demand market, compared to not inducing any adoption by the sellers, the platform benefits from inducing at least one seller to adop the analytics service, leading to higher analytics and marketplace revenues. Furthermore, with asymmetric sellers, the platform may face a trade off between inducing adoption solely by the more popular seller to achieve higher analytics revenue and inducing adoption by both sellers to attain higher marketplace revenue. Specifically, as sellers become more differentiated from each other (i.e., as ?? increases), the platform can achieve higher analytics revenue by inducing adoption solely from the more popular seller. Thus, as shown in Figure C1a, if ?? exceeds a certain threshold, the platform induces adoption solely by the more popular seller; otherwise, it induces adoption by both sellers.

In the high-demand market, compared to not inducing any adoption from the sellers, the platform experiences higher analytics revenue but suffers from lower marketplace revenue when it induces at least one seller to adopt the analytics service. As the transaction fee ?? increases, the marketplace revenue becomes more critical to the platform. Consequently, as shown in Figure C1b, when the transaction fee ?? is relatively large, the platform prioritizes marketplace revenue and charges a high subscription fee, preventing either seller from adopting the analytics service. When the transaction fee is relatively small, the platform focuses on analytics revenue, inducing at least one seller to adopt the service; more specifically, the platform only induces adoption by the more popular seller when the sellers are highly differentiated, and it induces adoption by both sellers otherwise.

## Impact of the Degree of Heterogeneity in Sellers’ Popularity

Recall that the parameter ?? measures the degree of heterogeneity in sellers’ popularity, with a higher ?? indicating more heterogeneous sellers. Apparently, the sellers’ popularity can impact the potential benefits they derive from the analytics service, subsequently affecting their adoption and pricing decisions. The impact of ?? on the sellers’ adoption has been discussed in the previous subsection (see Lemmas 4 and 5). In the following, we examine the impact of ?? on the sellers’ pricing decisions and summarize the results in the proposition below.

Proposition C1 (impacts of ?? on the prices of asymmetric sellers): As the heterogeneity in sellers’ popularity increases (i.e., as ?? increases), (a) if the increase of ?? does not lead to a switch in the adoption outcome, the more popular seller commands a higher price, and the less popular seller commands a lower price, and (b) if the increase of ?? does lead the adoption outcome to switch from both sellers adopting to only the more popular seller adopting, the sellers command higher prices in the low-demand market but lower prices in the high demand market.

To illustrate the results in Proposition C1, we depict the relationship between the heterogeneity of sellers’ popularity and their equilibrium prices in Figure C2.

![](/api/attachments/UWDJ7PMR/fulltext/images/6359ce0813d55341c3908e5210c8bd4699a145c23d96d2f5777a89d6fd3fc420.jpg)

![](/api/attachments/UWDJ7PMR/fulltext/images/efc83c52ec2a9a3be0dfe0a2b4b32aeae5cb7fe82cb22a54b5b9b207348de9c3.jpg)

$$
a _ {L} = 2, a _ {H} = 3, \lambda = 0. 2,
$$

$$
f = 0. 1
$$

Figure C2. Impact of ?? on Sellers’ Equilibrium Prices

As shown in Figure C2, the increase in ?? may or may not result in a switch in the adoption outcome, transitioning from both sellers adopting to only the more popular seller adopting. When the increase in ?? does not lead to the switch, the more (less) popular seller’s price increases (decreases) with ??. This occurs because, as ?? increases, the more (less) popular seller experiences an increase (a decrease) in market power and thus charges a higher (lower) price.

In the low-demand market (high-demand market), when the increase in ?? results in a switch in the adoption outcome, the accuracy effect and the competition-intensifying effect (competition-weakening effect) diminish, ultimately leading to a rise (fall) in the product prices set by the sellers. Thus, as shown in Proposition C1(b), as ?? increases, the more popular seller may charge a lower price in the high-demand market, whereas the less popular seller may charge a higher price in the low-demand market.

## Appendix D

## Model Extension with the Commission-Fee-Revenue Model

In the main model, we assume that the platform adopts a transaction fee revenue model for its marketplace service, whereby the platform charges a fee for each transaction that takes place on it; thus, its marketplace revenue is calculated as $f ( d _ { 1 } + d _ { 2 } )$ , where ?? is the transaction fee charged and $d _ { 1 } + d _ { 2 }$ represents the total market demand. In this extension, we study a scenario wherein the platform adopts the commission-fee-revenue model for its marketplace service. More specifically, under this revenue model, the platform charges a marketplace service fee (i.e., commission fee) that is proportional to the sellers’ prices. Consequently, its marketplace revenue is calculated as $\alpha ( p _ { 1 } d _ { 1 }$ + $p _ { 2 } d _ { 2 } )$ , where ?? is the commission rate charged and $p _ { 1 } d _ { 1 } + p _ { 2 } d _ { 2 }$ is the total sales revenue generated by the sellers. Note that, in this extension, to focus on the main trade-off, we assume that the sellers have the same popularity (i.e., $\mu _ { 1 } = \mu _ { 2 } = 1 / 2 )$ . To start with, we investigate the platform’s subscription fee decision and the sellers’ adoption decision in equilibrium and summarize our findings in the lemma below.

Lemma D1 (platform’s subscription fee and sellers’ adoption of the analytics service under the commission-fee-revenue model): (a) If the market size is low $( \pmb { a } = \pmb { a } _ { L } )$ and the commission rate is relatively high $( { \pmb { \alpha } } > \widetilde { { \pmb { \alpha } } } ) ,$ , then the platform sets a high subscription fee $( \pmb { s } ^ { * } >$ $\frac { ( 1 - \alpha ) ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } )$ such that neither seller adopts; (b) otherwise, the platform sets a low subscription fee $\begin{array} { r } { ( { \pmb S } ^ { * } = \frac { ( 1 - \alpha ) ( a _ { H } - { \pmb a } _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ ) to induce adoption by both sellers. The expression of ??̃ can be found in the proof of Lemma D1.

According to Lemma D1, the sellers will not adopt the analytics service if the subscription fee exceeds a certain threshold $\begin{array} { r } { ( \mathrm { i . e . , } \frac { ( 1 - \alpha ) ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ and will adopt the service otherwise. Interestingly, this threshold decreases as the commission rate ?? increases. This is because as the commission rate increases, the sellers stand to benefit less from potential improvements in their decision-making and hence their sales revenue due to the adoption, which reduces their willingness to pay for the analytics service.

In addition, as suggested by Lemma D1, in the high-demand market, the platform is always better off incentivizing the sellers to adopt by setting a low subscription fee. In contrast, in the low-demand market, the platform is sometimes better off not incentivizing any seller to adopt. The reason is that the analytics service has a competition-intensifying effect, which can lead to a decrease in the sellers’ sales revenue in the low-demand market. Consequently, with the adoption of the analytics service by the sellers, the platform’s marketplace revenue may also decrease. Therefore, when deciding on the optimal subscription fee, the platform needs to balance the potential gain in the analytics revenue against the potential loss in the marketplace revenue. By contrast, in the high-demand market, both the accuracy effect and the competition-weakening effect have a positive impact on the sales revenue of the sellers. Accordingly, the platform benefits from higher analytics revenue and marketplace revenue by inducing the adoption from both sellers. Therefore, the best strategy for the platform is to set a subscription fee that incentivizes adoption by both sellers.

Next, we investigate the impacts of the analytics service on key market outcomes under the commission-fee-revenue model and summarize the findings in Proposition D1.

Proposition D1 (impact of analytics service on key market outcomes under the commission-fee-revenue model): Compared to the regime without the analytics service, under the regime with the service, (a) in the low-demand market, the sellers are worse off, commanding lower prices, while consumer surplus and social welfare are both higher, and (b) in the high-demand market, the sellers are better off, commanding higher prices, while consumer surplus and social welfare are both lower.

Proposition D1 highlights the contrasting impacts of the analytics service on market outcomes in low-demand and high-demand market scenarios. More specifically, in the low-demand market, the analytics service impacts the market outcomes through the accuracy effect and the competitionintensifying effect. This leads to lower prices set by sellers, resulting in increased total market demand, consumer surplus, and social welfare, but reduced profitability for sellers. By contrast, in the high-demand market, the analytics service impacts the market outcomes through the accuracy effect and the competition-weakening effect. This leads to higher prices set by sellers, resulting in reduced total market demand, consume surplus, and social welfare, but increased profitability for sellers. The rationale behind Proposition D1 is aligned with the discussions following Propositions 1-4. In the following, we further explore the impact of the commission rate ?? on the subscription fee charged by the platform and the service adoption decisions of the sellers and summarize our findings in the proposition below.

Proposition D2 (impact of commission rate ?? on subscription fee and service adoption under the commission-fee-revenue model): As the commission rate for the marketplace service ?? increases, (a) in the low-demand market, the equilibrium subscription fee ??<sup>∗</sup> for the analytics service may increase, and the equilibrium outcome may change from both sellers adopting to neither seller adopting, and (b) in the high-demand market, the equilibrium subscription fee ??<sup>∗</sup> for the analytics service decreases, and the equilibrium outcome of both sellers adopting remains unchanged.

As indicated by Proposition D2 (b), in the high-demand market, the platform always sets a subscription fee that incentivizes both sellers to adopt the service, regardless of the commission rate. The reason is that, as discussed following Lemma D1, in the high-demand market, analytics revenue and marketplace revenue are aligned. Thus, the best strategy for the platform in the high-demand market is to choose the maximum subscription fee that induces both sellers to adopt the analytics service $\begin{array} { r } { \mathrm { i . e . , } s ^ { * } = \frac { ( 1 - \alpha ) ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ . This subscription fee decreases with the commission rate ??, maximizing both the analytics revenue and the marketplace revenue.

In the low-demand market, unlike the high-demand market, the analytics revenue and marketplace revenue sometimes conflict with each other. As discussed following Lemma D1, inducing the sellers to adopt the analytics service increases the analytics revenue but may decrease the marketplace revenue (as the total sales revenue may decline). As a result, when the commission rate ?? is relatively high, the platform focuses on the marketplace revenue by setting a higher subscription fee to induce fewer sellers to adopt in order to avoid the loss in the marketplace revenue that would otherwise incur. In contrast, when the commission rate ?? is relatively low, the platform prioritizes analytics revenue by setting a lower subscription fee to induce more sellers to adopt in order to generate higher analytics revenue. Thus, an increase in the commission rate ?? can incentivize the platform to increases the equilibrium subscription fee $s ^ { * }$ , such that the adoption outcome changes from both sellers adopting to neither seller adopting.

To conclude, under the commission-fee-revenue model, our key findings derived in the main model remain qualitatively unchanged (see Proposition D1). Additionally, we have obtained new insights regarding the impact of the commission rate ?? (see Proposition D2).

## Appendix E

## Model Extension with Strategic Sellers Who Can Infer the True Market Size from the Subscription Fee of the Analytics Service

In the main model, we implicitly assume that sellers cannot strategically deduce the true market size from the subscription fee of the analytic service. However, in this extension, we relax this assumption and assume that if the platform charges different subscription fees for market of different sizes, the sellers can infer the true market size based on subscription fees. In this analysis, to focus on the main trade-off, we assume that the sellers have the same popularity $( \mathrm { i . e . , } \mu _ { 1 } = \mu _ { 2 } = 1 / 2 )$ . To begin with, we examine the platform’s subscription fee decision and sellers’ adoption decisions and summarize the results in the following lemma. Note that we use the terminology from the literature on dynamic games with incomplete information (e.g., Cho and Kreps 1987), where a pooling equilibrium refers to the equilibrium where the platform sets the same subscription fee for the analytics service regardless of the true market size, and a separating equilibrium refers to th equilibrium where the platform sets different subscription fees under different market sizes.

Lemma E1 (platform’s subscription fee and sellers’ adoption of the analytics service): While no separating equilibrium exists, there exist two types of pooling equilibria: (a) the adopting equilibrium, where the platform sets the subscription fee $\begin{array} { r } { \pmb { s } ^ { * } \le \frac { ( \pmb { a } _ { H } - \pmb { a } _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } , } \end{array}$ and both sellers adopt the service, and (b) the non-adopting equilibrium, where the platform sets the subscription fee $\begin{array} { r } { \pmb { S } ^ { * } > \frac { ( \pmb { a } _ { H } - \pmb { a } _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } , } \end{array}$ and neither seller adopts the service. The corresponding sellers’ beliefs can be found in the proof of Lemma E1.

Lemma E1 indicates that no separating equilibrium exists. This means that if the sellers are strategic enough to infer the true market size from the platform’s subscription fee decision, then the platform will not set different subscription fees for markets of different sizes. The reason is that if the platform were to do so, the sellers would immediately deduce the true market size, rendering the analytics service useles to them. Consequently, neither seller would adopt the service, and the platform would not generate any analytics revenue. Additionally, as for the marketplace revenue, it is better for the platform to induce the sellers to lower their product prices, which can lead to an overall increase in market demand and higher marketplace revenue. Thus, given that the analytics revenue is always zero in a separating equilibrium, the platform would prefer to convince the sellers that the market is a low-demand market to maximize its total revenue by obtaining higher marketplace revenue. Consequently, when the market size is high, the platform always has the incentive to mimic the platform's strategy in a low-demand market. As a result, any separating equilibrium cannot sustain.

In addition, as shown in Lemma E1, the sellers’ decisions to adopt the analytics service are qualitatively the same as those in the main model. That is, if the subscription fee is below a certain threshold, both sellers adopt the service, but if the fee exceeds the threshold, neither seller chooses to adopt the service.

Next, we investigate the impacts of the analytics service on key market outcomes under this model extension and summarize the results in the proposition below.

Proposition E1 (impact of analytics service on key market outcomes): Compared to the regime without the analytics service, under the regime with the service, (a) in the low-demand market, the sellers can be worse off, commanding lower prices, while both consumer surplus and social welfare are higher, and (b) in the high-demand market, the sellers are better off, commanding higher prices, while both consumer surplus and social welfare are lower.

Upon comparing the findings in Proposition E1 to those of the main model, it is evident that our key findings remain qualitatively unchanged The intuitions behind these results are also similar. More specifically, in the low-demand market, the analytics service impacts the market outcomes through the accuracy effect and the competition-intensifying effect. Due to those two effects, with the adoption of the service, the sellers will set a lower price and potentially obtain a lower profit (especially when the equilibrium subscription fee surpasses a threshold), resulting in higher total market demand, consumer surplus, and social welfare. By contrast, in the high-demand market, the service impacts the market outcomes through the accuracy effect and the competition-weakening effect. Due to those two effects, upon adopting the analytics service, the sellers will set a higher price and obtain a higher profit, leading to lower total market demand, consumer surplus, and socia welfare.

## Appendix F

## Expected Impact of Analytics Service on Key Market Outcomes

The main model investigates how the analytics service impacts market outcomes in a specific market scenario, such as a high-demand or low-demand market. In this analysis, we explore the expected impact of the analytics service on market outcomes. To start with, we use the consumer surplus as an example to demonstrate the contrast between the two analyses. The main model investigates how the analytics service impacts consumer surplus in a specific market scenario, such as a high-demand or low-demand market. For example, in the high-demand market, we investigate the impact of the service on consumer surplus by comparing consumer surplus with the analytics service $\scriptstyle C S | _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { H } }$ to that without the service $\left. C S \right| _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { H } }$ , both under the market with a high market size $a = a _ { H }$ . In contrast, in this analysis, we compare the expected consumer surplus with the service $E { \big ( } C S | _ { I _ { 1 } = 1 , I _ { 2 } = 1 } { \big ) }$ to that without the service $E { \big ( } C S | _ { I _ { 1 } = 0 , I _ { 2 } = 0 } { \big ) }$ , taking the expectation over ??.

In the following, we examine the expected impact of the analytics service and summarize the results in the proposition below.

Proposition F1 (expected impact of analytics service on key market outcomes): Compared to the regime without the analytics service, under the regime with the service, (a) the platform’s expected profit is higher, (b) the sellers’ expected prices and profits remain the same, and (c) the expected consumer surplus and social welfare become lower.

As indicated by Proposition 1, the analytics service has opposing impacts on product prices. Specifically, it leads to higher product prices in the high-demand market but lower product prices in the low-demand market. The results in Proposition F1 show that, despite these opposing impacts, the sellers’ expected prices remain unchanged because the opposing impacts are equally present in both market scenarios. Moreover, adopting the service results in increased revenue for the sellers by helping them make more informed decisions. However, this increased seller revenue is fully extracted by the platform, resulting in a higher profit for the platform and the same profit for the sellers.

Interestingly, we also find that the adoption of the analytics service results in lower consumer surplus. As previously discussed, the analytics service impacts the product prices in those two market scenarios to the same extent; however, the degree of impact on consumer surplus differs between these scenarios. Specifically, due to the larger consumer base in the high-demand market, the price changes have a greater impact on consumer surplus than in the low-demand market. Consequently, the negative impact of the analytics service on consumer surplus through product prices in the high-demand market outweighs its positive impact in the low-demand market. Thus, adopting the analytics service results in a decrease in expected consumer surplus. Similarly, the negative impact of the service on consumers’ aggregate gross value in the high-demand market outweighs its positive impact in the low-demand market, leading to an overall decrease in expected social welfare.

## Appendix G

## Proofs of Propositions and Lemmas

In this appendix, we assume that $4 f < 3 a _ { L } - a _ { H }$ . This assumption is made to exclude the uninteresting equilibrium outcomes where sellers have no demand.

## Proof of Lemma 1

Since this subgame of pricing decision is an incomplete information game (due to market size uncertainty), following the convention of solving Bayesian Nash equilibrium, we first propose each firm’s rational strategies in equilibrium and verify that neither player will deviate from such proposed strategies (Kwark et al. 2018).

Suppose, in equilibrium, seller $i \ ' \mathbf { s }$ price is (1) $p _ { i } ^ { a _ { H } } ( I _ { i } , I _ { - i } )$ when sellers’ adoption decisions are $I _ { i }$ and $I _ { - i }$ and the market is a high-demand market; $( 2 ) p _ { i } ^ { a _ { L } } ( I _ { i } , I _ { - i } )$ when sellers’ adoption decisions are $I _ { i }$ and $I _ { - i }$ and the market is a low-demand market. Given the other seller’s equilibrium pricing strategy and sellers’ adoption decisions $I _ { i }$ and $I _ { - i }$ , seller ??’s expected profit functions are

$$
\max _ {p _ {i}} (p _ {i} - f) E [ d _ {i} (I _ {i}, I _ {- i}, a) ] - I _ {i} s,
$$

where

$$
E [ d _ {i} (I _ {i}, I _ {- i}, a) ] = \left\{ \begin{array}{c} \mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i}, \text {if} I _ {i} = 1, a = a _ {H}; \\ \mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i}, \text {if} I _ {i} = 1, a = a _ {L}; \\ \mu_ {i} (a _ {H} + a _ {L}) / 2 - p _ {i} + \lambda p _ {- i}, \text {if} I _ {i} = 0, a = a _ {H} \text {or} a _ {L}. \end{array} \right.
$$

Specifically,

(1) When $I _ { i } = 1 , I _ { - i } = 1$ and the market is a high-demand market:

$$
\pi_ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1) = (p _ {i} - f) \big (\mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1) \big) - s
$$

(2) When $I _ { i } = 1 , I _ { - i } = 1$ and the market is a low-demand market:

$$
\pi_ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1) = (p _ {i} - f) \big (\mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1) \big) - s
$$

(3) When $I _ { i } = 1 , I _ { - i } = 0$ and the market is a high-demand market:

$$
\pi_ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 0) = (p _ {i} - f) \big (\mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 0) \big) - s
$$

(4) When $I _ { i } = 1 , I _ { - i } = 0$ and the market is a low-demand market:

$$
\pi_ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 0) = (p _ {i} - f) \big (\mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 0) \big) - s
$$

(5) When $I _ { i } = 0 , I _ { - i } = 1$ and the market is a high-demand market:

$$
\pi_ {i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 1) = \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 1)) + \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 1))
$$

(6) When $I _ { i } = 0 , I _ { - i } = 1$ and the market is a low-demand market:

$$
\pi_ {i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 1) = \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 1)) + \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 1))
$$

(7) When $I _ { i } = 0 , I _ { - i } = 0$ and the market is a high-demand market:

$$
\pi_ {i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 0) = \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 0)) + \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 0))
$$

(8) When $I _ { i } = 0 , I _ { - i } = 0$ and the market is a low-demand market:

$$
\pi_ {i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 0) = \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {H} - p _ {i} + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 0)) + \frac {1}{2} (p _ {i} - f) (\mu_ {i} a _ {L} - p _ {i} + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 0)
$$

The above profit functions are shown to be concave (i.e., $\frac { d ^ { 2 } \pi _ { i } ^ { a } } { d p _ { i } ^ { 2 } } < 0 )$ . Thus, in order for the proposed prices to be the equilibrium ones, they need to satisfy the following conditions:

$$
p _ {i} ^ {a _ {H}} (I _ {i}, I _ {- i}) = \left\{p _ {i} \bigg | \frac {d \pi_ {i} ^ {a _ {H}} (I _ {i} , I _ {- i})}{d p _ {i}} = 0 \right\}, p _ {i} ^ {a _ {L}} (I _ {i}, I _ {- i}) = \left\{p _ {i} \bigg | \frac {d \pi_ {i} ^ {a _ {L}} (I _ {i} , I _ {- i})}{d p _ {i}} = 0 \right\}, i \in \{1, 2 \}, I _ {i} \in \{0, 1 \}
$$

Solving the above equations, we get:

$$
p _ {i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 0) = p _ {i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 1) = p _ {i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 0) = p _ {i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 1) = \frac {(a _ {H} + a _ {L}) (2 \mu_ {i} + \lambda \mu_ {- i})}{2 (4 - \lambda^ {2})} + \frac {f}{2 - \lambda}
$$

$$
p _ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1) = \frac {f (2 + \lambda) + a _ {H} (2 \mu_ {i} + \lambda \mu_ {- i})}{4 - \lambda^ {2}}
$$

$$
p _ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1) = \frac {f (2 + \lambda) + a _ {L} (2 \mu_ {i} + \lambda \mu_ {- i})}{4 - \lambda^ {2}}
$$

$$
p _ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 0) = \frac {(a _ {H} + a _ {L}) (2 \mu_ {i} + \lambda \mu_ {- i}) + 2 f (2 + \lambda)}{2 (4 - \lambda^ {2})} + \frac {\mu_ {i} (a _ {H} - a _ {L})}{4}
$$

$$
p _ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 0) = \frac {(a _ {H} + a _ {L}) (2 \mu_ {i} + \lambda \mu_ {- i}) + 2 f (2 + \lambda)}{2 (4 - \lambda^ {2})} - \frac {\mu_ {i} (a _ {H} - a _ {L})}{4}.
$$

## Proofs of Lemmas 2 and 3

As discussed in the main text, specifically in the section entitled Adoption and Pricing of Analytics Service (including Lemmas 2-3 and Propositions 1-7), we assume that $\mu _ { 1 } = \mu _ { 2 } = 1 / 2$ . Lemmas 2 and 3 discuss the platform’s equilibrium subscription fee and the sellers equilibrium decisions when the inventory holding cost ?? is implicitly assumed to be 0 (the inventory holding cost ?? is introduced in Appendix A). Lemma A1 addresses the same issues in a more general setting, where the inventory holding cost is non-negative $( r \geq 0 )$ . Hence, we only provide the proof for Lemma A1, based on which Lemmas 2 and 3 follow immediately. Note that in Lemma 3, $\begin{array} { r } { \tilde { f } = \frac { a _ { H } - a _ { L } } { 8 - 1 2 \lambda + 4 \lambda ^ { 2 } } . } \end{array}$

## Proof of Proposition 1

Note that in the proofs of Propositions 1-4, our focus is on comparing the outcomes of the equilibrium in which sellers adopt the service with the scenario in which the analytics service is unavailable. This is because it is evident that all outcomes of the equilibrium where sellers do not adopt the service are the same as in the scenario where the analytics service is unavailable.

## The low-demand market case:

Seller ?? ’s price without the analytics service is $\begin{array} { r } { p _ { i } ^ { a _ { L } } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } } \end{array}$ . Seller ?? ’s price with the analytics service under the equilibrium outcome $\begin{array} { r } { I _ { 1 } = I _ { 2 } = 1 \mathrm { i s } p _ { i } ^ { a _ { L } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } } \end{array}$ . By comparison, we have $p _ { i } ^ { a _ { L } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) < p _ { i } ^ { a _ { L } } ( I _ { 1 } = 0 , I _ { 2 } = 0 )$

## The high-demand market case:

Seller ?? ’s price without the analytics service is $\begin{array} { r } { p _ { i } ^ { a _ { H } } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } } \end{array}$ . Seller ?? ’s price with the analytics service under the equilibrium outcome $\begin{array} { r } { I _ { 1 } = I _ { 2 } = 1 \mathrm { i s } p _ { i } ^ { a _ { H } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) = \frac { a _ { H } + 2 f } { 4 - 2 \lambda } } \end{array}$ .We have $p _ { i } ^ { a _ { H } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) > p _ { i } ^ { a _ { H } } ( I _ { 1 } = 0 , I _ { 2 } = 0 )$

## Proof of Proposition 2

## The low-demand market case:

We first provide a general formula of seller ??’s realized profit in the low-demand market case:

$$
\pi_ {i} ^ {r} = (p _ {i} - f) \left(\frac {a _ {L}}{2} - p _ {i} + \lambda p _ {- i}\right) - I _ {i} s ^ {*},
$$

where the superscript ?? in $\pi _ { i } ^ { r }$ stands for “realized.” Note that according to Lemma 3, $\begin{array} { r } { s ^ { * } = \tilde { s } = { \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } } } \end{array}$ when $I _ { 1 } = I _ { 2 } = 1$ in equilibrium.

Seller ??’s realized profit without the analytics service is

$$
\begin{array}{r l} & {\pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = \pi_ {i} ^ {r} \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), I _ {1} = 0, I _ {2} = 0 \big)} \\ & {\qquad = \frac {(a _ {H} + a _ {L} + 4 f (- 1 + \lambda)) (- a _ {L} (- 3 + \lambda) + a _ {H} (- 1 + \lambda) + 4 f (- 1 + \lambda))}{1 6 (2 - \lambda) ^ {2}}.} \end{array}
$$

Seller ??’s price with the analytics service under the equilibrium outcome $I _ { 1 } = I _ { 2 } = 1$ is

$$
\begin{array}{c} \pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} = \pi_ {i} ^ {r} \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), I _ {1} = 1, I _ {2} = 1 \big) \\ = \frac {(3 a _ {L} - a _ {H} - 4 f (1 - \lambda)) (a _ {H} + a _ {L} - 4 f (1 - \lambda))}{1 6 (2 - \lambda) ^ {2}}. \end{array}
$$

Under our technical assumption $4 f < 3 a _ { L } - a _ { H }$ , we have:

$$
\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} - \pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = - \frac {(a _ {H} - a _ {L}) (a _ {H} + a _ {L} + 4 f (- 1 + \lambda)) \lambda}{1 6 (2 - \lambda) ^ {2}} <   0.
$$

## The high-demand market case:

Similar to the proof for the low-demand market case, in the high-demand market, under our technical assumption $4 f < 3 a _ { L } - a _ { H }$ , we have:

$$
\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {H}} - \pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {H}} = \frac {(a _ {H} - a _ {L}) (a _ {H} + a _ {L} + 4 f (- 1 + \lambda)) \lambda}{1 6 (2 - \lambda) ^ {2}} > 0.
$$

## Proof of Proposition 3

Consumer surplus is calculated as:

$$
C S = \sum_ {i = 1} ^ {2} \left(\frac {a (\mu_ {i} + \lambda \mu_ {- i})}{1 - \lambda^ {2}} d _ {i}\right) - \frac {d _ {1} ^ {2} + 2 \lambda d _ {1} d _ {2} + d _ {2} ^ {2}}{2 (1 - \lambda^ {2})} - p _ {1} d _ {1} - p _ {2} d _ {2},
$$

where $d _ { i } = \mu _ { i } a - p _ { i } + \lambda p _ { - i }$ and $\mu _ { i } = 1 / 2$

## The low-demand market case:

Consumer surplus without the analytics service is:

$$
C S | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = C S \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), I _ {1} = 0, I _ {2} = 0 \big).
$$

Consumer surplus with the analytics service under the equilibrium outcome $I _ { 1 } = I _ { 2 } = 1$ is

$$
C S | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} = C S \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), I _ {1} = 1, I _ {2} = 1 \big).
$$

Under our technical assumption $4 f < 3 a _ { L } - a _ { H }$ , we have:

$$
C S | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} - C S | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = \frac {(a _ {H} - a _ {L}) (a _ {L} (5 - \lambda) - (a _ {H} + 8 f) (1 - \lambda))}{1 6 (- 2 + \lambda) ^ {2}} > 0.
$$

## The high-demand market case:

Similar to the proof for the low-demand market case, in the high-demand market, under our technical assumption $4 f < 3 a _ { L } - a _ { H }$ , we have:

$$
C S | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {H}} - C S | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {H}} = \frac {(a _ {H} - a _ {L}) (a _ {H} (\lambda - 5) + (a _ {L} + 8 f) (1 - \lambda))}{1 6 (- 2 + \lambda) ^ {2}} <   0.
$$

## Proof of Proposition 4

Social welfare is calculated as:

$$
S W = \sum_ {i = 1} ^ {2} \left(\frac {a (\mu_ {i} + \lambda \mu_ {- i})}{1 - \lambda^ {2}} d _ {i}\right) - \frac {d _ {1} ^ {2} + 2 \lambda d _ {1} d _ {2} + d _ {2} ^ {2}}{2 (1 - \lambda^ {2})},
$$

where $d _ { i } = \mu _ { i } a - p _ { i } + \lambda p _ { - i }$ and $\mu _ { i } = 1 / 2 , i \in \{ 1 , 2 \}$

## The low-demand market case:

Social welfare without the analytics service is:

$$
S W | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = S W \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), I _ {1} = 0, I _ {2} = 0 \big).
$$

Social welfare with the analytics service under the equilibrium outcome $I _ { 1 } = I _ { 2 } = 1$ is:

$$
S W | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} = S W \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), I _ {1} = 1, I _ {2} = 1 \big).
$$

Under our technical assumption $4 f < 3 a _ { L } - a _ { H }$ , we have

$$
S W | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} - S W | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = \frac {(a _ {H} - a _ {L}) (a _ {H} + 3 a _ {L} + 8 f) (1 - \lambda)}{1 6 (2 - \lambda) ^ {2}} > 0.
$$

## The high-demand market case:

Similar to the proof for the low-demand market case, in the high-demand market, under our technical assumption $4 f < 3 a _ { L } - a _ { H }$ , we have:

$$
S W | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {H}} - S W | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {H}} = - \frac {(a _ {H} - a _ {L}) (3 a _ {H} + a _ {L} + 8 f) (1 - \lambda)}{1 6 (2 - \lambda) ^ {2}} <   0.
$$

## Proof of Proposition 5

According to Lemma 3, in the low-demand market, the platform always sets a low subscription fee $\begin{array} { r } { ( \mathrm { i . e . , } s ^ { \ast } = \tilde { s } = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ to induce the adoption of both sellers. Thus, we conclude that, as the transaction fee (??) increases, in the low-demand market, the equilibrium subscription fee (s<sup>∗</sup>) for the analytics service remains unchanged. On the other hand, in the high-demand market, when the transaction fee is relatively high $( \mathrm { i } . \mathrm { e } . , f > \tilde { f } )$ , the platform sets a high subscription fee $\begin{array} { r } { ( \mathrm { i } . \mathrm { e } . , s ^ { \ast } > \tilde { s } ) } \end{array}$ to prevent either seller from adopting; otherwise, the platform sets a low subscription fee $( \mathrm { i } . \mathbf { e } . , s ^ { * } = \tilde { s } )$ to induce the adoption of both sellers. Thus, as the transaction fee (??) increases, in the high-demand market, the equilibrium subscription fee (s<sup>∗</sup>) for the analytics service either remains unchanged or increases.

## Proof of Proposition 6

For the prices listed in Lemma 1, we have $\begin{array} { r } { \frac { \partial p _ { i } } { \partial f } > 0 } \end{array}$ . Additionally, for the sellers’ profits $\pi _ { i } ^ { r } ( I _ { 1 } , I _ { 2 } )$ calculated in the proof of Proposition 2, we have $\frac { \partial \pi _ { i } ^ { r } ( I _ { 1 } , I _ { 2 } ) } { \partial f } < 0$ . That is, given the adoption decisions of the sellers, their prices increase with the transaction fee $f ,$ and their profits decrease with $f .$ . Since the change in ?? does not lead to a change in the sellers’ adoption decisions in the low-demand market (see Proposition $5 ) ,$ we conclude that as $f$ increases, the sellers raise their prices in the low-demand market and attain lower profits. Moreover, in the highdemand market, an increase in $f$ may lead to a switch in the adoption outcome, transitioning from both sellers adopting to neither adopting. This transition occurs when the value of $f$ crosses the threshold $\tilde { f }$ (see Proposition 5). When such a switch occurs, as indicated by Propositions 1 and $^ { 2 , }$ the sellers lower their prices and attain reduced profits.

## Proof of Proposition 7

For consumer surplus $C S ( I _ { 1 } , I _ { 2 } )$ and social welfare $S W ( I _ { 1 } , I _ { 2 } )$ calculated in the proof of Propositions 3 and 4, we have $\frac { \partial C S ( I _ { 1 } , I _ { 2 } ) } { \partial f } < 0$ and $\frac { \partial S W ( I _ { 1 } , I _ { 2 } ) } { \partial f } < 0$ . That is, given the adoption decisions of the sellers, consumer surplus and social welfare decrease with $f .$ Since the change in $f$ does not lead to the change in the sellers’ adoption decisions in the low-demand market (see Proposition 5), we conclude that in the lowdemand market, as ?? increases, consumer surplus and social welfare decrease. Moreover, in the high-demand market, the increase in ?? may lead to the adoption outcome switching from both sellers adopting to neither adopting, which happens when the value of $f$ crosses the threshold ??<sup>̃</sup> (see Proposition 5). When such a switch occurs, as indicated by Propositions 3 and $^ { 4 , }$ we conclude that consumer surplus and social welfare increase.

## Proof of Lemma A1

In this extension, we still make the assumption that $4 f < 3 a _ { L } - a _ { H }$ to exclude the uninteresting equilibrium outcomes where sellers have no demand. Following the convention of backward induction, we split the proof of Lemma A1 into three parts. In the first part, we analyze the sellers’ pricing and inventory decisions given their adoption decisions and the platform’s subscription fee decision; in the second part, we analyze the sellers’ adoption decisions given the platform’s subscription fee decision; in the third part, we analyze the platform’s subscription fee decision.

Part 1: Sellers’ pricing and inventory decisions.

We divide this part into four cases based on the sellers’ adoption decisions.

Case 1: Neither seller adopts the analytics service

Seller ??’s expected payoff is:

$$
\begin{array}{r} \pi_ {i} ^ {a} (I _ {i} = 0, I _ {- i} = 0) = \frac {1}{2} \bigg ((p _ {i} - f) \min \left\{q _ {i}, \frac {a _ {H}}{2} - p _ {i} + \lambda p _ {- i} \right\} - r \max \{0, q _ {i} - (\frac {a _ {H}}{2} - p _ {i} + \lambda p _ {- i}) \} \bigg) \\ + \frac {1}{2} \bigg ((p _ {i} - f) \min \left\{q _ {i}, \frac {a _ {L}}{2} - p _ {i} + \lambda p _ {- i} \right\} - r \max \{0, q _ {i} - (\frac {a _ {L}}{2} - p _ {i} + \lambda p _ {- i}) \} \bigg) \end{array}
$$

Thus, if $\begin{array} { r } { q _ { i } \le \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } } \end{array}$ , we have $\begin{array} { r } { \pi _ { i } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = ( p _ { i } - f ) q _ { i } , \mathrm { a n d } \frac { d \pi _ { i } } { d q _ { i } } > 0 ; \mathrm { i f } \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } < q _ { i } \leq \frac { a _ { H } } { 2 } - p _ { i } + \lambda p _ { - i } } \end{array}$ , we have $\begin{array} { r } { \pi _ { i } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { 1 } { 2 } ( p _ { i } - f ) q _ { i } + \frac { 1 } { 2 } \bigg ( ( p _ { i } - f ) \left( \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } \right) - r \left( q _ { i } - ( \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } ) \right) } \end{array}$ , and the sign $\operatorname { o f } { \frac { d \pi _ { i } } { d q _ { i } } }$ depends on the value of ?? ; if $q _ { i } > \frac { a _ { H } } { 2 } - p _ { i } + \lambda p _ { - i }$ , we have $\begin{array} { r } { \pi _ { i } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { 1 } { 2 } \Big ( ( p _ { i } - f ) ( \frac { a _ { H } } { 2 } - p _ { i } + \lambda p _ { - i } ) - r ( q _ { i } - ( \frac { a _ { H } } { 2 } - p _ { i } + \lambda p _ { - i } ) ) \Big ) + \frac { 1 } { 2 } \Big ( ( p _ { i } - f ) ( \frac { a _ { L } } { 2 } - p _ { i } ) - r ( \frac { a _ { H } } { 2 } - p _ { i } ) \Big ) . } \end{array}$ $\begin{array} { r } { p _ { i } + \lambda p _ { - i } ) - r ( q _ { i } - ( \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } ) ) \bigg ) , \mathrm { a n d } \frac { d \pi _ { i } } { d q _ { i } } < 0 . } \end{array}$

As can easily be seen above, $\pi _ { i }$ is always linear in $q _ { i } ;$ thus, we conclude that the dominant strategy of seller ?? is setting either $\begin{array} { r } { q _ { i } = \frac { a _ { H } } { 2 } - p _ { i } + } \end{array}$ $\begin{array} { r } { \lambda p _ { - i } \mathrm { o r } q _ { i } = \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } } \end{array}$ . Subsequently, we analyze which combinations of dominant strategies can be the equilibrium.

$$
q _ {1} = \frac {a _ {L}}{2} - p _ {1} + \lambda p _ {2} \text { and } q _ {2} = \frac {a _ {L}}{2} - p _ {2} + \lambda p _ {1} \tag {1}
$$

Substituting $q _ { 1 }$ and $q _ { 2 }$ into $\pi _ { i }$ and solving $\begin{array} { r } { \frac { \partial \pi _ { 1 } } { \partial p _ { 1 } } = 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial \pi _ { 2 } } { \partial p _ { 2 } } = 0 } \end{array}$ simultaneously, we have $\begin{array} { r } { p _ { i } = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } } \end{array}$ . Accordingly, we have $q _ { i } =$ $\frac { a _ { L } + 2 f ( - 1 + \lambda ) } { 4 - 2 \lambda }$ and $\begin{array} { r } { \pi _ { i } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { ( a _ { L } + 2 f ( - 1 + \lambda ) ) ^ { 2 } } { 4 ( - 2 + \lambda ) ^ { 2 } } } \end{array}$ . If seller ?? deviates and chooses $\begin{array} { r } { q _ { i } = \frac { a _ { H } } { 2 } - p _ { i } + \lambda p _ { - i } , } \end{array}$ then we have

$$
\pi_ {i} ^ {a} (I _ {1} = 0, I _ {2} = 0) = \frac {a _ {H} ^ {2} (2 - \lambda) ^ {2} + 6 4 f ^ {2} (1 - \lambda) ^ {2} + a _ {L} ^ {2} (2 + \lambda) ^ {2} + 2 a _ {H} (2 - \lambda) (8 (f + r) \lambda - 8 (f + 2 r) + a _ {L} (2 + \lambda)) + 1 6 a _ {L} (r (2 - \lambda) ^ {2} + f (- 2 + \lambda + \lambda^ {2}))}{6 4 (2 - \lambda) ^ {2}}.
$$

Accordingly, the necessary and sufficient condition for seller 1 not to deviate is:

$$
r > \frac {2 a _ {H} + 6 a _ {L} - 1 6 f - a _ {H} \lambda + a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda}.
$$

Thus, when $\begin{array} { r } { r > \frac { 2 a _ { H } + 6 a _ { L } - 1 6 f - a _ { H } \lambda + a _ { L } \lambda + 1 6 f \lambda } { 3 2 - 1 6 \lambda } , } \end{array}$ , we have $\begin{array} { r } { p _ { i } = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } } \end{array}$ and $\begin{array} { r } { q _ { i } = \frac { a _ { L } + 2 f ( - 1 + \lambda ) } { 4 - 2 \lambda } } \end{array}$ in equilibrium.

$$
q _ {1} = \frac {a _ {H}}{2} - p _ {1} + \lambda p _ {2} \text {and} q _ {2} = \frac {a _ {L}}{2} - p _ {2} + \lambda p _ {1}, \text {or} q _ {1} = \frac {a _ {L}}{2} - p _ {1} + \lambda p _ {2} \text {and} q _ {2} = \frac {a _ {H}}{2} - p _ {2} + \lambda p _ {1}
$$

Following the same logic as in (1), in order for (2) to be an equilibrium, we need to ensure the following two inequalities hold simultaneously:

$$
r <   \frac {2 a _ {H} + 6 a _ {L} - 1 6 f - a _ {H} \lambda + a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda} \mathrm{and}
$$

$$
r > \frac {2 a _ {H} + 6 a _ {L} - 1 6 f + a _ {H} \lambda - a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda}.
$$

Since the above two conditions cannot hold simultaneously, we conclude that (2) cannot be an equilibrium.

$$
q _ {1} = \frac {a _ {H}}{2} - p _ {1} + \lambda p _ {2} \text { and } q _ {2} = \frac {a _ {H}}{2} - p _ {2} + \lambda p _ {1}
$$

Following the same logic as in (1), in order for (3) to be an equilibrium, we need to ensure that the following inequality holds:

$$
r <   \frac {2 a _ {H} + 6 a _ {L} - 1 6 f + a _ {H} \lambda - a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda}
$$

Accordingly, in equilibrium, we have $\begin{array} { r } { p _ { i } = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } \mathrm { a n d } q _ { i } = \frac { a _ { H } ( 3 - \lambda ) - ( a _ { L } + 4 f ) ( 1 - \lambda ) } { 4 ( 2 - \lambda ) } . } \end{array}$

Note that when $\begin{array} { r } { \frac { 2 a _ { H } + 6 a _ { L } - 1 6 f - a _ { H } \lambda + a _ { L } \lambda + 1 6 f \lambda } { 3 2 - 1 6 \lambda } < r < \frac { 2 a _ { H } + 6 a _ { L } - 1 6 f + a _ { H } \lambda - a _ { L } \lambda + 1 6 f \lambda } { 3 2 - 1 6 \lambda } . } \end{array}$ , both (1) and (3) can be the equilibrium, and we use the Pretodominant defining rule to choose (3) as the equilibrium. Thus, to sum up, $\begin{array} { r } { \mathrm { i f } \ r < \frac { 2 a _ { H } + 6 a _ { L } - 1 6 f + a _ { H } \lambda - a _ { L } \lambda + 1 6 f \lambda } { 3 2 - 1 6 \lambda } } \end{array}$ , the equilibrium is $\ ( p _ { i } ^ { a } ( I _ { 1 } =$ $\begin{array} { r } { 0 , I _ { 2 } = 0 ) = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } , q _ { i } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { a _ { H } ( 3 - \lambda ) - ( a _ { L } + 4 f ) ( 1 - \lambda ) } { 4 ( 2 - \lambda ) } ) } \end{array}$ ; otherwise, the equilibrium is $\begin{array} { r } { ( p _ { i } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 0 ) = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } , q _ { i } ^ { a } ( I _ { 1 } = } \end{array}$ $\begin{array} { r } { 0 , I _ { 2 } = 0 ) = \frac { a _ { L } + 2 f ( - 1 + \lambda ) } { 4 - 2 \lambda } ) } \end{array}$

## Case 2: Only seller 2 adopts the analytics service

Seller 1’s expected payoff is the same as that in Case 1. Since seller 2 knows the true market size, seller $2 \mathit { \ ' } _ { \mathbf { S } }$ expected payoff depends on the true market size, and seller 2 can make decisions depending on the true market size. More specifically, when $a = a _ { H }$

$$
\pi_ {2} ^ {a _ {H}} (I _ {1} = 0, I _ {2} = 1) = (p _ {2} - f) \mathrm{min} \left\{q _ {2}, \frac {a _ {H}}{2} - p _ {2} + \lambda p _ {1} \right\} - r \mathrm{max} \{q _ {2} - \left(\frac {a _ {H}}{2} - p _ {2} + \lambda p _ {1}\right), 0 \} - s;
$$

when $a = a _ { L }$

$$
\pi_ {2} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 1) = (p _ {2} - f) \min \left\{q _ {2}, \frac {a _ {L}}{2} - p _ {2} + \lambda p _ {1} \right\} - r \max \left\{q _ {2} - \left(\frac {a _ {L}}{2} - p _ {2} + \lambda p _ {1}\right), 0 \right\} - s.
$$

Accordingly, following the same proof structure as in Case 1, the equilibrium results are as follows.

(1) when $\begin{array} { r } { r > \frac { 4 a _ { H } + 1 2 a _ { L } - 3 2 f + 3 2 f \lambda + a _ { H } \lambda ^ { 2 } - a _ { L } \lambda ^ { 2 } } { 6 4 - 3 2 \lambda } \ ; } \end{array}$

The equilibrium strategy of seller 1 is $\begin{array} { r } { ( p _ { 1 } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } , q _ { 1 } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { L } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } ) } \end{array}$ . The equilibrium strategy of seller 2 is $\begin{array} { r } { ( \rho _ { 2 } ^ { a a _ { \prime } } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { \mathrm { r } } + 2 f } { 4 - 2 \lambda } , q _ { 2 } ^ { a a _ { \prime } } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { \mathrm { r } } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } ) \mathrm { i f } a = a _ { \mathrm { r } } , \mathrm { a n d } ( \rho _ { 2 } ^ { a b } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { 2 a _ { \mathrm { r } } + 4 f - a _ { \mathrm { r } } \lambda ^ { 2 } + a _ { \mathrm { r } } \lambda } { 8 - 4 \lambda } , q _ { 2 } ^ { a a _ { \prime } } ( I _ { 1 } = 0 , I _ { 2 } = } \end{array}$ $\begin{array} { r } { 1 ) = \frac { a _ { H } ( 2 - \lambda ) - 4 f ( 1 - \lambda ) + a _ { L } \lambda } { 8 - 4 \lambda } ) \mathrm { ~ i f ~ } a = a _ { H } , } \end{array}$

(2) when $\begin{array} { r } { r \leq \frac { 4 a _ { H } + 1 2 a _ { L } - 3 2 f + 3 2 f \lambda + a _ { H } \lambda ^ { 2 } - a _ { L } \lambda ^ { 2 } } { 6 4 - 3 2 \lambda } \ ; } \end{array}$

The equilibrium strategy of seller 1 is $\begin{array} { r } { ( p _ { 1 } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } , q _ { 1 } ^ { a } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { H } ( 6 - \lambda ^ { 2 } ) - 8 f ( 1 - \lambda ) - a _ { L } ( 2 - \lambda ^ { 2 } ) } { 8 ( 2 - \lambda ) } ) } \end{array}$ . The equilibrium strategy of seller 2 is $\begin{array} { r } { ( p _ { 2 } ^ { a _ { L } } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { 4 a _ { L } + 8 f + a _ { H } \lambda - a _ { L } \lambda } { 1 6 - 8 \lambda } , q _ { 2 } ^ { a _ { L } } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { L } ( 4 - \lambda ) + ( a _ { H } + 8 f ) \lambda - 8 f } { 8 ( 2 - \lambda ) } ) } \end{array}$ if the market is of low-demand, and $\begin{array} { r } { p _ { 2 } ^ { a _ { H } } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { 4 a _ { H } + 8 f - a _ { H } \lambda + a _ { L } \lambda } { 1 6 - 8 \lambda } , q _ { 2 } ^ { a _ { H } } ( I _ { 1 } = 0 , I _ { 2 } = 1 ) = \frac { a _ { H } ( 4 - \lambda ) + ( a _ { L } + 8 f ) \lambda - 8 f } { 8 ( 2 - \lambda ) } } \end{array}$ if the market is a high-demand market.

## Case 3: Only seller 1 adopts the analytics service

This case is symmetric to Case 2.

Case 4: Both sellers adopt the analytics service

Seller ??’s expected payoff is as follows. When $a = a _ { H }$

$$
\pi_ {i} ^ {a _ {H}} (I _ {1} = 1, I _ {2} = 1) = (p _ {i} - f) \min \left\{q _ {i}, \frac {a _ {H}}{2} - p _ {i} + \lambda p _ {- i} \right\} - r \max \{0, q _ {i} - \left(\frac {a _ {H}}{2} - p _ {i} + \lambda p _ {- i}\right) \} - s;
$$

when $a = a _ { L } ;$

$$
\pi_ {i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1) = (p _ {i} - f) \min \left\{q _ {i}, \frac {a _ {L}}{2} - p _ {i} + \lambda p _ {- i} \right\} - r \max \{0, q _ {i} - \left(\frac {a _ {L}}{2} - p _ {i} + \lambda p _ {- i}\right) \} - s.
$$

Accordingly, following the same proof structure as in Case 1, the equilibrium results are as follows. If the market is a low-demand market, then the equilibrium is $\begin{array} { r } { p _ { i } ^ { a _ { L } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } } \end{array}$ and $\begin{array} { r } { q _ { i } ^ { a _ { L } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) = \frac { a _ { L } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } } \end{array}$ ; if the market is a high-demand market, then the equilibrium is $\begin{array} { r } { p _ { i } ^ { a _ { H } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) = \frac { a _ { H } + 2 f } { 4 - 2 \lambda } } \end{array}$ and $\begin{array} { r } { q _ { i } ^ { a _ { H } } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) = \frac { a _ { H } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } . } \end{array}$

## Part 2: Sellers’ adoption decisions.

Based on the results in Part 1, we derive sellers’ expected payoffs under different adoption decisions when the value of ?? falls within a specific range.

(1) when $\begin{array} { r } { r \leq \frac { 4 a _ { H } + 1 2 a _ { L } - 3 2 f + 3 2 f \lambda + a _ { H } \lambda ^ { 2 } - a _ { L } \lambda ^ { 2 } } { 6 4 - 3 2 \lambda } \colon } \end{array}$

$$
E [ \pi_ {i} (I _ {i} = 1, I _ {- i} = 1) ] = \frac {a _ {H} ^ {2} + a _ {L} ^ {2} + 4 a _ {H} f (- 1 + \lambda) + 4 f (a _ {L} + 2 f (- 1 + \lambda)) (- 1 + \lambda)}{8 (2 - \lambda) ^ {2}} - s,
$$

$$
E [ \pi_ {i} (I _ {i} = 1, I _ {- i} = 0) ] = \frac {3 2 a _ {L} f (- 1 + \lambda) + 6 4 f ^ {2} (- 1 + \lambda) ^ {2} + a _ {H} ^ {2} (8 + (- 4 + \lambda) \lambda) + a _ {L} ^ {2} (8 + (- 4 + \lambda) \lambda) + a _ {H} (3 2 f (- 1 + \lambda) - 2 a _ {L} (- 4 + \lambda) \lambda)}{6 4 (2 - \lambda) ^ {2}} - s,
$$

$$
E [ \pi_ {i} (I _ {i} = 0, I _ {- i} = 1) ] = \frac {a _ {H} ^ {2} + a _ {L} ^ {2} + 8 a _ {L} f (- 1 + \lambda) + 1 6 f ^ {2} (- 1 + \lambda) ^ {2} + 2 a _ {L} r (- 2 + \lambda) ^ {2} (2 + \lambda) + 2 a _ {H} (a _ {L} + 4 f (- 1 + \lambda) - r (- 2 + \lambda) ^ {2} (2 + \lambda))}{1 6 (2 - \lambda) ^ {2}},
$$

$$
E [ \pi_ {i} (I _ {i} = 0, I _ {- i} = 0) ] = \frac {a _ {H} ^ {2} + a _ {L} ^ {2} + 2 a _ {H} (a _ {L} - 2 r (- 2 + \lambda) ^ {2} + 4 f (- 1 + \lambda)) + 4 a _ {L} r (- 2 + \lambda) ^ {2} + 8 a _ {L} f (- 1 + \lambda) + 1 6 f ^ {2} (- 1 + \lambda) ^ {2}}{1 6 (2 - \lambda) ^ {2}}.
$$

Comparing the payoffs above and applying the Pareto-dominant Rule to define the equilibrium, we conclude that in this case, both sellers adopt the service if:

$$
s <   \tilde {s} ^ {\prime} = \frac {1}{1 6} (a _ {H} - a _ {L}) (4 r + \frac {a _ {H} - a _ {L}}{(2 - \lambda) ^ {2}}),
$$

and neither seller adopts the service otherwise.

$$
(2) \mathrm{when} \frac {4 a _ {H} + 1 2 a _ {L} - 3 2 f + 3 2 f \lambda + a _ {H} \lambda^ {2} - a _ {L} \lambda^ {2}}{6 4 - 3 2 \lambda} <   r \leq \frac {2 a _ {H} + 6 a _ {L} - 1 6 f + a _ {H} \lambda - a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda}:
$$

$$
E [ \pi_ {i} (I _ {i} = 1, I _ {- i} = 1) ] = \frac {a _ {H} ^ {2} + a _ {L} ^ {2} + 4 a _ {H} f (- 1 + \lambda) + 4 f (a _ {L} + 2 f (- 1 + \lambda)) (- 1 + \lambda)}{8 (2 - \lambda) ^ {2}} - s,
$$

$$
E [ \pi_ {i} (I _ {i} = 1, I _ {- i} = 0) ] = \frac {a _ {H} ^ {2} (- 2 + \lambda) ^ {2} + 3 2 f ^ {2} (- 1 + \lambda) ^ {2} - 2 a _ {H} (- 2 + \lambda) (4 f (- 1 + \lambda) + a _ {L} \lambda) + a _ {L} ^ {2} (4 + \lambda^ {2}) + 8 a _ {L} f (- 2 + \lambda + \lambda^ {2})}{3 2 (2 - \lambda) ^ {2}} - s,
$$

$$
E [ \pi_ {i} (I _ {i} = 0, I _ {- i} = 1) ] = \frac {(a _ {L} - 2 f (1 - \lambda)) ^ {2}}{4 (2 - \lambda) ^ {2}},
$$

$$
E [ \pi_ {i} (I _ {i} = 0, I _ {- i} = 0) ] = \frac {a _ {H} ^ {2} + a _ {L} ^ {2} + 2 a _ {H} (a _ {L} - 2 r (- 2 + \lambda) ^ {2} + 4 f (- 1 + \lambda)) + 4 a _ {L} r (- 2 + \lambda) ^ {2} + 8 a _ {L} f (- 1 + \lambda) + 1 6 f ^ {2} (- 1 + \lambda) ^ {2}}{1 6 (2 - \lambda) ^ {2}}.
$$

Comparing the payoffs above and applying the Pareto-dominant rule to define the equilibrium, we conclude that in this case, both sellers adopt the service if:

$$
s <   \tilde {s} ^ {\prime} = \frac {1}{1 6} (a _ {H} - a _ {L}) (4 r + \frac {a _ {H} - a _ {L}}{(2 - \lambda) ^ {2}}),
$$

and neither seller adopts the service otherwise.

(3) when $\begin{array} { r } { r > \frac { 2 a _ { H } + 6 a _ { L } - 1 6 f + a _ { H } \lambda - a _ { L } \lambda + 1 6 f \lambda } { 3 2 - 1 6 \lambda } \mathrm { . } } \end{array}$

$$
E [ \pi_ {i} (I _ {i} = 1, I _ {- i} = 1) ] = \frac {a _ {H} ^ {2} + a _ {L} ^ {2} + 4 a _ {H} f (- 1 + \lambda) + 4 f (a _ {L} + 2 f (- 1 + \lambda)) (- 1 + \lambda)}{8 (2 - \lambda) ^ {2}} - s,
$$

$$
E [ \pi_ {i} (I _ {i} = 1, I _ {- i} = 0) ] = \frac {a _ {H} ^ {2} (- 2 + \lambda) ^ {2} + 3 2 f ^ {2} (- 1 + \lambda) ^ {2} - 2 a _ {H} (- 2 + \lambda) (4 f (- 1 + \lambda) + a _ {L} \lambda) + a _ {L} ^ {2} (4 + \lambda^ {2}) + 8 a _ {L} f (- 2 + \lambda + \lambda^ {2})}{3 2 (2 - \lambda) ^ {2}} - s,
$$

$$
E [ \pi_ {i} (I _ {i} = 0, I _ {- i} = 1) ] = \frac {(a _ {L} - 2 f (1 - \lambda)) ^ {2}}{4 (2 - \lambda) ^ {2}},
$$

$$
E [ \pi_ {i} (I _ {i} = 0, I _ {- i} = 0) ] = \frac {(a _ {L} - 2 f (1 - \lambda)) ^ {2}}{4 (2 - \lambda) ^ {2}}.
$$

Comparing the payoffs above and applying the Pareto-dominant rule to define the equilibrium, we conclude that in this case, both sellers adopt the service if

$$
s <   \tilde {s} ^ {\prime} = \frac {(a _ {H} - a _ {L}) (a _ {H} + a _ {L} - 4 f (1 - \lambda))}{8 (2 - \lambda) ^ {2}},
$$

and neither seller adopts the service otherwise. To sum up, the sellers adopt the service if $s \leq \tilde { s } ^ { \prime }$ , and neither seller adopts the service otherwise, where

$$
\tilde {r} = \frac {2 a _ {H} + 6 a _ {L} - 1 6 f + a _ {H} \lambda - a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda}
$$

$$
\tilde {s} ^ {\prime} = \left\{ \begin{array}{l l} \frac {1}{1 6} (a _ {H} - a _ {L}) (4 r + \frac {a _ {H} - a _ {L}}{(2 - \lambda) ^ {2}}), i f r \leq \tilde {r} \\ \frac {(a _ {H} - a _ {L}) (a _ {H} + a _ {L} - 4 f (1 - \lambda))}{8 (2 - \lambda) ^ {2}}, o. w. \end{array} \right.
$$

## Part 3: The platform’s subscription fee decision.

Based on the results derived in Part 1 and Part 2, we derive the platform’s profit under different subscription fee decisions when the value of ?? falls within a specific range. Here

$$
\pi_ {P} ^ {a} (I _ {1}, I _ {2}) = f \sum_ {i = 1} ^ {2} \min \{q _ {i} ^ {a} (I _ {i}, I _ {- i}), \frac {a}{2} - p _ {i} ^ {a} (I _ {i}, I _ {- i}) + \lambda p _ {- i} ^ {a} (I _ {i}, I _ {- i}) \} + (I _ {1} + I _ {2}) \tilde {s} ^ {\prime},
$$

where $p _ { i } ^ { a } ( I _ { i } , I _ { - i } ) , q _ { i } ^ { a } ( I _ { i } , I _ { - i } )$ and ${ \tilde { s } } ^ { \prime }$ can be obtained from Part 1 and Part 2.

$$
(1) r \leq \tilde {r}
$$

## a. The low-demand market.

By comparison, we have:

$$
\pi_ {P} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1) > \pi_ {P} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 0).
$$

That is, the platform sets $s = \tilde { s } ^ { \prime }$ such that both sellers adopt the service in the low-demand market.

## b. The high-demand market.

The sufficient and necessary condition for the platform to induce both sellers to adopt the service is

$$
\pi_ {P} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1) \geq \pi_ {P} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 0),
$$

from which we have $\begin{array} { r } { f \le \tilde { f } ^ { \prime \prime } = \frac { a _ { H } - a _ { L } + 4 r ( 2 - \lambda ) ^ { 2 } } { 4 ( 2 - \lambda ) ( 1 - \lambda ) } } \end{array}$ . That is, the platform sets $s = \tilde { s } ^ { \prime }$ such that both sellers adopt the service if and only if $f \leq \tilde { f } ^ { \prime \prime }$

(2) $r > \tilde { r }$

## a. The low-demand market.

By comparison, we have: $\pi _ { \cal P } ^ { a _ { L } } ( I _ { i } = 1 , I _ { - i } = 1 ) > \pi _ { \cal P } ^ { a _ { L } } ( I _ { i } = 0 , I _ { - i } = 0 )$ . That is, the platform sets $s = \tilde { s } ^ { \prime }$ such that both sellers adopt the service in the low-demand market.

## b. The high-demand market.

By comparison, we have: $\pi _ { P } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) > \pi _ { P } ^ { a _ { H } } ( I _ { i } = 0 , I _ { - i } = 0 )$ . That is, the platform sets $s = \tilde { s } ^ { \prime }$ such that both sellers adopt the service in the high-demand market.

In Lemma A $\begin{array} { r } { \iota , \tilde { s } ^ { \prime } = \left\{ \begin{array} { l l } { \frac { 1 } { 1 6 } ( a _ { H } - a _ { L } ) ( 4 r + \frac { a _ { H } - a _ { L } } { ( 2 - \lambda ) ^ { 2 } } ) , i f r \leq \tilde { r } } \\ { \quad \frac { ( a _ { H } - a _ { L } ) ( a _ { H } + a _ { L } - 4 f ( 1 - \lambda ) ) } { 8 ( 2 - \lambda ) ^ { 2 } } , o . w . } \end{array} \right. \mathrm { ~ a n d ~ } \tilde { f } ^ { \prime \prime } = \frac { a _ { H } - a _ { L } + 4 r ( 2 - \lambda ) ^ { 2 } } { 4 ( 2 - \lambda ) ( 1 - \lambda ) } \mathrm { . } } \end{array}$

## Proof of Lemma A2

The proof of Lemma A2 directly follows from the proof of Lemma A1. More specifically, based on the market conditions, we identify th platform’s subscription fee decision and the sellers’ adoption decisions based on parts 1 and 2 in the proof of Lemma A1; accordingly, we

$$
\tilde {r} = \frac {2 a _ {H} + 6 a _ {L} - 1 6 f + a _ {H} \lambda - a _ {L} \lambda + 1 6 f \lambda}{3 2 - 1 6 \lambda}.
$$

## Proofs of Propositions A1 and A2

We divide this proof into two cases based on the value of the inventory holding cost ??.

Case $\mathbf { \xi } _ { l \cdot } r \leq \tilde { r }$

Without the analytics service, we have $\begin{array} { r } { p _ { i } = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } a n d q _ { i } = \frac { a _ { H } ( 3 - \lambda ) - ( a _ { L } + 4 f ) ( 1 - \lambda ) } { 4 ( 2 - \lambda ) } . } \end{array}$

With the analytics service, in the high-demand market, we have $\begin{array} { r } { p _ { i } = \frac { a _ { H } + 2 f } { 4 - 2 \lambda } \mathrm { a n d } q _ { i } = \frac { a _ { H } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } \mathrm { i f } f \le \tilde { f } ^ { \prime \prime } } \end{array}$ , and $\begin{array} { r } { p _ { i } = \frac { a _ { H } + a _ { L } + 4 f } { 8 - 4 \lambda } \mathrm { a n d } \ q _ { i } = } \end{array}$ $\frac { a _ { H } ( 3 - \lambda ) - ( a _ { L } + 4 f ) ( 1 - \lambda ) } { 4 ( 2 - \lambda ) }$ otherwise; in the low-demand market, we have $\begin{array} { r } { p _ { i } = \frac { { \bf \bar { \alpha } } _ { a _ { L } + 2 f } } { 4 - 2 \lambda } \mathrm { a n d } q _ { i } = \frac { a _ { L } { \bf \bar { \alpha } } - 2 { \bf \bar { \alpha } } ( 1 - \lambda ) } { 4 - 2 \lambda } . } \end{array}$ . Thus, compared to the regime without the analytics service, under the regime with the analytics service, in the high-demand market, the sellers command higher prices and choose a lower inventory level, whereas, in the low-demand market, the sellers command lower prices and choose a lower inventory level.

Case $2 , r > \tilde { r }$

Without the analytics service, seller ??’s pricing and quantity decisions are $\begin{array} { r } { p _ { i } = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } a n d q _ { i } = \frac { a _ { L } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } . } \end{array}$ . With the analytics service, in the high-demand market, we have $\begin{array} { r } { p _ { i } = \frac { a _ { H } + 2 f } { 4 - 2 \lambda } \mathrm { ~ a n d ~ } q _ { i } = \frac { a _ { H } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } } \end{array}$ ; in the low-demand market, we have $\begin{array} { r } { p _ { i } = \frac { a _ { L } + 2 f } { 4 - 2 \lambda } \operatorname { a n d } q _ { i } = \frac { a _ { L } - 2 f ( 1 - \lambda ) } { 4 - 2 \lambda } } \end{array}$ Compared to the regime without the analytics service, under the regime with the analytics service, in the high-demand market, the sellers command higher prices and choose a higher inventory level, whereas, in the low-demand market, the sellers command the same prices and choose the same inventory level.

## Proof of Lemma B1

Under this extension, we make additional technical assumptions $\begin{array} { r } { 2 \leq n < 1 + \frac { 1 } { \lambda } \mathrm { a n d } 0 < f < \frac { a _ { H } } { n ( 1 + \lambda - n \lambda ) } } \end{array}$ to ensure that each seller has positive demand. Following the convention of solving Bayesian equilibrium (the same approach as in the proof of Lemma 1) and using the symmetry property of the sellers, given that there are ?? sellers adopting the service (?? − ?? sellers not adopting the service), we propose the equilibrium strategies of sellers as follows: if seller ?? adopts the analytics service and the market is a high-demand market, then $p _ { i } = p ^ { a _ { H } } ; $ ; if seller ?? adopts the analytics service and the market is a low-demand market, then $p _ { i } = p ^ { a _ { L } } ;$ ; if seller ?? does not adopt the analytics service, then $p _ { i } = p ^ { N }$ Subsequently,

(1) Given the market is a high-demand market, ?? sellers adopting the service (?? − ?? sellers not adopting the service), and seller ?? adopts the analytics service, seller $i \ ' _ { \mathrm { s } }$ expected revenue is $\begin{array} { r } { \pi _ { i } = ( p _ { i } - f ) \left( \frac { a _ { H } } { n } - p _ { i } + \lambda \big ( ( m - 1 ) p ^ { a _ { H } } + ( n - m ) p ^ { N } \big ) \right) } \end{array}$ . This function is concave $\mathrm { ( i . e . , } \frac { d ^ { 2 } \pi _ { i } } { d p _ { i } ^ { 2 } } < 0 \mathrm { ) }$ and by solving $\begin{array} { r } { \frac { d \pi _ { i } } { d p _ { i } } = 0 } \end{array}$ , we derive $p _ { i } ^ { * }$ in this case as $p ^ { a _ { H } } = { \textstyle { \frac { 1 } { 2 } } } ( f + ( m - 1 ) p ^ { a _ { H } } \lambda + ( n - m ) p ^ { N } \lambda + { \textstyle { \frac { a _ { H } } { n } } } ) \cdots \cdots \cdots ( B I )$

(2) Given the market is a low-demand market, ?? sellers adopting the service (?? − ?? sellers not adopting the service), and seller ?? adopts the analytics service, seller ??’s expected revenue is $\begin{array} { r } { \pi _ { i } = ( p _ { i } - f ) \left( \frac { a _ { L } } { n } - p _ { i } + \lambda \big ( ( m - 1 ) p ^ { a _ { L } } + ( n - m ) p ^ { N } \big ) \right) } \end{array}$ .This function is concave $\mathrm { ( i . e . , } \frac { d ^ { 2 } \pi _ { i } } { d p _ { i } ^ { 2 } } < 0 \mathrm { ) }$ and by solving $\begin{array} { r } { \frac { d \pi _ { i } } { d p _ { i } } = 0 } \end{array}$ , we derive $p _ { i } ^ { * }$ in this case as $p ^ { a _ { L } } = { \textstyle { \frac { 1 } { 2 } } } ( f + ( m - 1 ) p ^ { a _ { L } } \lambda + ( n - m ) p ^ { N } \lambda + { \textstyle { \frac { a _ { L } } { n } } } ) \cdots \cdots \cdots ( B 2 ) .$

(3) Given ?? sellers adopting the service (?? − ?? sellers not adopting the service), and seller ?? does not adopt the analytics service, seller $i \ ' _ { \mathbf { S } }$ expected revenue is $\begin{array} { r } { \pi _ { i } = ( p _ { i } - f ) \big ( \frac { 1 } { 2 } ( \frac { \alpha _ { H } } { n } - p _ { i } + \lambda ( m p ^ { \alpha _ { H } } + ( n - m - 1 ) p ^ { N } ) ) + \frac { 1 } { 2 } ( \frac { \alpha _ { L } } { n } - p _ { i } + \lambda ( m p ^ { \alpha _ { L } } + ( n - m - 1 ) p ^ { N } ) ) \big ) } \end{array}$ . This function is concave $\begin{array} { r } { ( \mathrm { i . e . , } \frac { d ^ { 2 } \pi _ { i } } { d p _ { i } ^ { 2 } } < 0 ) } \end{array}$ and by solving $\begin{array} { r } { \frac { d \pi _ { i } } { d p _ { i } } = 0 } \end{array}$ , we derive $p _ { i } ^ { * }$ in this case as: $p ^ { N } = { \textstyle { \frac { 1 } { 4 } } } ( 2 f + m ( p ^ { a _ { H } } + p ^ { a _ { L } } ) \lambda + 2 ( n - m -$ $\begin{array} { r } { 1 ) p ^ { N } \lambda + \frac { a _ { H } + a _ { L } } { n } ) \cdots \cdots \cdots ( B 3 ) } \end{array}$

Solving Equations (B1), (B2), and (B3) simultaneously, we $\begin{array} { r } { \mathsf { g e t } p ^ { a _ { H } } = \frac { a _ { H } + a _ { L } + 2 f n } { 4 n + 2 n \lambda - 2 n ^ { 2 } \lambda } + \frac { a _ { H } - a _ { L } } { 4 n + 2 n \lambda - 2 n m \lambda } , p ^ { a _ { L } } = \frac { a _ { H } + a _ { L } + 2 f n } { 4 n + 2 n \lambda - 2 n ^ { 2 } \lambda } - \frac { a _ { H } - a _ { L } } { 4 n + 2 n \lambda - 2 n m \lambda } , } \end{array}$ and $\begin{array} { r } { p ^ { N } = \frac { a _ { H } + a _ { L } + 2 f n } { 4 n + 2 n \lambda - 2 n ^ { 2 } \lambda } . } \end{array}$

## Proof of Lemma B2

Given that there are ?? sellers adopting the service (?? − ?? sellers not adopting the service), if seller ?? does not adopt the analytics service (and thus their beliefs about the market size are $\mathrm { P r } [ a = a _ { H } ] = \mathrm { P r } [ a = a _ { L } ] = 1 / 2 )$ , then seller ??’s expected profit is:

$$
E [ \pi_ {i} (I _ {i} = 0) ] = (p ^ {N} - f) \left(\frac {1}{2} \Big (\frac {a _ {H}}{n} - p ^ {N} + \lambda (m p ^ {a _ {H}} + (n - m - 1) p ^ {N}) \Big) + \frac {1}{2} \Big (\frac {a _ {L}}{n} - p ^ {N} + \lambda (m p ^ {a _ {L}} + (n - m - 1) p ^ {N}) \Big)\right);
$$

if seller ?? adopts the analytics service, then seller ??’s expected profit is:

$$
E \left[ \pi_ {i} (I _ {i} = 1) \right] = \frac {1}{2} \Bigg ((p ^ {a _ {H}} - f) \left(\left(\frac {a _ {H}}{n} - p ^ {a _ {H}} + \lambda ((m - 1) p ^ {a _ {H}} + (n - m) p ^ {N})\right)\right) \Bigg) + \frac {1}{2} \Bigg ((p ^ {a _ {L}} - f) \left(\frac {a _ {L}}{n} - p ^ {a _ {L}} + \lambda ((m - 1) p ^ {a _ {L}} + (n - m) p ^ {N})\right) \Bigg).
$$

$$
(n - m) p ^ {N}) \biggr) \biggr) - s.
$$

Based on the sellers’ adoption decisions, we divide this proof into the following three cases.

Case 1: All sellers adopting the analytics service is the equilibrium:

In this case, the following condition needs to hold.

$$
E [ \pi_ {i} (I _ {i} = 1) | _ {m = n} ] \geq E [ \pi_ {i} (I _ {i} = 0) | _ {m = n - 1} ]
$$

By solving this inequality, we have $\begin{array} { r } { s \leq \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } . } \end{array}$

Case 2: No sellers adopting the analytics service is the equilibrium:

In this case, the following condition needs to hold.

$$
E [ \pi_ {i} (I _ {i} = 1) | _ {m = 1} ] <   E [ \pi_ {i} (I _ {i} = 0) | _ {m = 0} ]
$$

By solving this inequality, we have $\begin{array} { r } { s > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 n ^ { 2 } } . } \end{array}$

Case 3: ?? $( 1 \leq m ^ { \prime } \leq n - 1 )$ sellers adopting the analytics service is the equilibrium:

In this case, the following conditions need to hold: $E [ \pi _ { i } ( I _ { i } = 1 ) | _ { m = m ^ { \prime } } ] > E [ \pi _ { i } ( I _ { i } = 0 ) | _ { m = m ^ { \prime } - 1 } ] \mathrm { ~ a n d ~ } E [ \pi _ { i } ( I _ { i } = 0 ) | _ { m = m ^ { \prime } } ] >$ $E [ \pi _ { i } ( I _ { i } = 1 ) | _ { m = m ^ { \prime } + 1 } ]$

By solving this inequality, we have:

$$
\frac {(a _ {H} - a _ {L}) ^ {2}}{4 n ^ {2} (m ^ {\prime} \lambda - 2) ^ {2}} <   s <   \frac {(a _ {H} - a _ {L}) ^ {2}}{4 n ^ {2} (2 + \lambda - m ^ {\prime} \lambda) ^ {2}}.
$$

However, since $\begin{array} { r } { \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - m ^ { \prime } \lambda ) ^ { 2 } } < \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( m ^ { \prime } \lambda - 2 ) ^ { 2 } } } \end{array}$ under our assumption $\begin{array} { r } { 2 \leq m \leq n < 1 + \frac { 1 } { \lambda } } \end{array}$ , such a case is impossible. Note that when $\begin{array} { r } { \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 n ^ { 2 } } < s \le \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } , } \end{array}$ , all sellers adopting the service and no seller adopting the service can be the equilibrium, and the former is the Pareto dominant equilibrium. Applying the refining rule of Pareto dominant, we assume that the equilibrium is that all sellers adopt the service when $\begin{array} { r } { \frac { ( a _ { H } - \hat { a _ { L } } ) ^ { 2 } } { 1 6 n ^ { 2 } } < s \le \frac { ( \hat { a _ { H } } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ . Thus, we conclude that if the subscription fee ?? for the analytics service is relatively low $( s \leq$ $\frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } )$ , all sellers adopt the service; otherwise, none of the sellers adopts the service.

## Proof of Lemma B3

We split this proof into the high-demand and low-demand market cases

The low-demand market case:

If the platform sets a high subscription fee $\begin{array} { r } { s > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ and no seller adopts the service, then its profit is $\begin{array} { r } { \pi _ { p } = n f \left( \frac { a _ { L } } { n } - p ^ { N } + \right. } \end{array}$ $\lambda ( n - 1 ) p ^ { N } \ O \Big )$ . If the platform sets a subscription fee $\begin{array} { r } { s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ and all sellers adopt the service, then its profit is $\pi _ { p } =$ $\begin{array} { r } { n f \left( \frac { a _ { L } } { n } - p ^ { a _ { L } } + \lambda ( n - 1 ) p ^ { a _ { L } } \right) + n \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ . Under our technical assumptions mentioned in the Proof of Lemma B1, we always have $\begin{array} { r } { n f \left( \frac { a _ { L } } { n } - p ^ { N } + \lambda ( n - 1 ) p ^ { N } \right) < n f \left( \frac { a _ { L } } { n } - p ^ { a _ { L } } + \lambda ( n - 1 ) p ^ { a _ { L } } \right) + n \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ . Thus, in the low-demand market, the platform always sets a low subscription fee $\begin{array} { r } { ( s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } ) } \end{array}$ to induce the adoption from all sellers.

## The high-demand market case:

If the platform sets a high subscription fee $\begin{array} { r } { s > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ and no seller adopts the service, then its profit is $\begin{array} { r } { \pi _ { p } = n f \left( \frac { a _ { H } } { n } - p ^ { N } + \right. } \end{array}$ $\lambda ( n - 1 ) p ^ { N } \Big )$ . If the platform sets a subscription fee $\begin{array} { r } { s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ and all sellers adopt the service, then its profit is $\pi _ { p } =$ $\begin{array} { r } { n f \left( \frac { a _ { H } } { n } - p ^ { a _ { H } } + \lambda ( n - 1 ) p ^ { a _ { H } } \right) + n \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } . } \end{array}$ The sufficient and necessary condition for the platform not to induce any adoption i $\begin{array} { r } { n f \left( \frac { a _ { H } } { n } - p ^ { N } + \lambda ( n - 1 ) p ^ { N } \right) > n f \left( \frac { a _ { H } } { n } - p ^ { a _ { H } } + \lambda ( n - 1 ) p ^ { a _ { H } } \right) + n \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } } \end{array}$ . From the above inequality, we have $f > \tilde { f } ^ { \prime \prime \prime } =$ $\frac { a _ { H } - a _ { L } } { 2 n ( 2 + ( n - 1 ) \lambda ( ( n - 1 ) \lambda - 3 ) ) }$ Note that $f > \tilde { f } ^ { \prime \prime \prime }$ does not conflict with our technical assumptions mentioned in the proof of Lemma B1

## Proof of Proposition B1

In the low-demand market, the platform always sets the subscription fee $\begin{array} { r } { s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } } { 4 n ^ { 2 } ( 2 + \lambda - n \lambda ) ^ { 2 } } , } \end{array}$ , and we have: $\begin{array} { r } { \frac { d \frac { \left( a _ { H } - a _ { L } \right) ^ { 2 } } { 4 n ^ { 2 } \left( 2 + \lambda - n \lambda \right) ^ { 2 } } } { d n } < } \end{array}$ 0 under our technical assumptions mentioned in the proof of Lemma B1, which means that the subscription fee decreases with ??. In the high-demand market, when the equilibrium adoption outcome is all sellers adopting the service and the increase of ?? does not impact the equilibrium adoption outcome, the subscription fee decrease with ??, the reason of which is the same as what we have discussed for the results in the low-demand market. However, when $\begin{array} { r } { 3 n + \sqrt { \frac { 3 + \lambda ( 3 + \lambda ) } { \lambda ^ { 2 } } } < 2 + \frac { 3 } { \lambda } , } \end{array}$ we have $\begin{array} { r } { \frac { d \tilde { f } ^ { \prime } } { d n } < 0 } \end{array}$ , which indicates that the increases of ?? may induce the platform to increase the subscription fee to switch the adoption outcome from all sellers adopting to no seller adopting (as also indicated in Lemma B3). Thus, we conclude that, as ?? increases, the platform may increase the subscription fee.

## Proof of Lemma C1

Lemma C1 can be proved with the same logic as in the proof of Part 2 of Lemma A1. The values of thresholds in Lemma C1 are provided as follows: $\begin{array} { r } { \tilde { \mu } = \frac { 4 } { 8 - 2 \lambda - \lambda ^ { 2 } } , \tilde { s } _ { H } = \frac { 1 } { 1 6 } ( a _ { H } - a _ { L } ) ^ { 2 } \mu ^ { 2 } \mathrm { ~ a n d ~ } \tilde { s } _ { L } = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 2 - ( 2 - \lambda ) \mu ) ^ { 2 } } { 4 ( 4 - \lambda ^ { 2 } ) ^ { 2 } } } \end{array}$

## Proof of Lemma C2

Lemma C2 can be proved with the same logic as in the proof of Part 3 of Lemma A1. In Lemma C2, $\tilde { f } ^ { \prime } = \left\{ \begin{array} { c } { { \frac { ( a _ { H } - a _ { L } ) ( 2 - ( 2 - \lambda ) \mu ) ^ { 2 } } { ( 2 + \lambda ) ^ { 2 } ( 2 - 3 \lambda + \lambda ^ { 2 } ) } , \mu < \tilde { \mu } } } \\ { { \frac { ( a _ { H } - a _ { L } ) \mu } { 4 ( 1 - \lambda ) } , \mu \geq \tilde { \mu } } } \end{array} \right.$ . Let $\hat { \mu } _ { 1 }$ be the solution of $\mu$ that satisfies the following equation $\begin{array} { r } { f = \frac { ( a _ { H } - a _ { L } ) ( 3 2 + ( - 2 + \lambda ) \mu ( 3 2 - ( - 2 + \lambda ) ( - 4 + \lambda ( 4 + \lambda ) ) \mu ) ) } { 4 ( 2 - \lambda ) ( 1 - \lambda ) ( 2 + \lambda ) ^ { 2 } ( 2 - ( 2 - \lambda ) \mu ) } } \end{array}$ and falls within the range $[ 1 / 2 , 1 ]$ . And let $\hat { \mu } _ { 2 }$ be the solution of $\mu$ that satisfies the following equation $\begin{array} { r } { f = \frac { ( a _ { H } - a _ { L } ) ( - 3 2 + ( - 2 + \lambda ) \mu ( - 3 2 + ( - 2 + \lambda ) ( - 4 + \lambda ( 4 + \lambda ) ) \mu ) ) } { 4 ( - 2 + \lambda ) ( - 1 + \lambda ) ( 2 + \lambda ) ^ { 2 } ( 2 + ( - 2 + \lambda ) \mu ) } } \end{array}$ and falls $\tilde { \mu } ^ { \prime } = \left\{ \begin{array} { r } { \operatorname* { m a x } \left\{ \tilde { \mu } , \frac { 4 f \left( 1 - \lambda \right) } { a _ { H } - a _ { L } } , \hat { \mu } _ { 1 } \right\} } \\ { \operatorname* { m a x } \left\{ \tilde { \mu } , \hat { \mu } _ { 2 } \right\} , \mathrm { w h } } \end{array} \right.$ , when $a = a _ { H }$ within the range $[ 1 / 2 , 1 ]$ . Then, we have en $a = a _ { L }$

## Proof of Proposition C1

Substituting $\mu _ { 1 } = \mu$ and $\mu _ { 2 } = 1 - \mu$ into the prices listed in Lemma 1 and taking the derivative with respect to $\mu ,$ we have $\begin{array} { r } { \frac { \partial p _ { 1 } } { \partial \mu } > 0 \mathrm { a n d } \frac { \partial p _ { 2 } } { \partial \mu } < } \end{array}$ 0. That is, given the adoption decisions of the sellers, as ?? increases, the more popular seller (i.e., seller 1) commands a higher price, and the less popular seller (i.e., seller 2) commands a lower price. Additionally, given ??, we have $p _ { i } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) < p _ { i } ( I _ { 1 } = 1 , I _ { 2 } = 0 )$ in the lowdemand market and have $p _ { i } ( I _ { 1 } = 1 , I _ { 2 } = 1 ) > p _ { i } ( I _ { 1 } = 1 , I _ { 2 } = 0 )$ in the high-demand market. Thus, if the increase of ?? does lead the adoption outcome to switch from both sellers adopting to only the more popular seller adopting, the sellers command higher prices in the low-demand market but lower prices in the high-demand market.

## Proof of Lemma D1

Following the convention of backward induction, in this proof, we first derive the sellers’ pricing decision in Stage 3, then we derive the sellers’ adoption decision in Stage 2, and last, we derive the platform’s subscription fee decision in Stage 1. In this model extension, we make the assumption $3 a _ { L } - a _ { H } > 0$ to rule out the uninteresting equilibrium outcomes where sellers have zero demand in equilibrium.

## The sellers pricing decisions

This proof follows the same structure as that of Lemma 1. Here, we do not repeat the proof but provide the sellers’ pricing decisions under different adoption decisions and market scenarios.

$$
\begin{array}{r l} & p _ {i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 0) = p _ {i} ^ {a _ {H}} (I _ {i} = 0, I _ {- i} = 1) = p _ {i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 0) = p _ {i} ^ {a _ {L}} (I _ {i} = 0, I _ {- i} = 1) = \frac {a _ {H} + a _ {L}}{8 - 4 \lambda}, p _ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1) = \\ & \frac {a _ {H}}{4 - 2 \lambda}, p _ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1) = \frac {a _ {L}}{4 - 2 \lambda}, p _ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 0) = \frac {4 a _ {H} - a _ {H} \lambda + a _ {L} \lambda}{1 6 - 8 \lambda}, p _ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 0) = \frac {4 a _ {L} + a _ {H} \lambda - a _ {L} \lambda}{1 6 - 8 \lambda}. \end{array}
$$

## The sellers’ adoption decisions

The sellers’ adoption decisions are as follows: If the subscription fee s for the analytics service is relatively low $\begin{array} { r } { ( \mathrm { i . e . , } s \leq \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ , both sellers adopt the service; otherwise, neither seller adopts the service. This proof follows the same structure as that of Part 2 in the proof of Lemma A1.

## The platform’s subscription fee decision

## When the market is a low-demand market,

if the platform sets the subscription fee $\begin{array} { r } { S = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ such that both sellers adopt the service, then the platform’s profit is: $\begin{array} { r } { \pi _ { p } \left( s = \frac { ( a _ { N } - a _ { i } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { L } \right) = \alpha \sum _ { i = 1 } ^ { 2 } p _ { i } ^ { a _ { i } } ( l _ { i } = 1 , L _ { - i } = 1 ) \left( \frac { a _ { L } } { 2 } - p _ { i } ^ { a _ { i } } ( l _ { i } = 1 , L _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { i } } ( l _ { i } = 1 , L _ { - i } = 1 ) \right) + 2 \frac { ( a _ { N } - a _ { i } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ ; if the platform sets the subscription fee $\begin{array} { r } { s > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ such that neither seller adopts the service, then the platform’s profit is: $\begin{array} { r } { \pi _ { p } \left( s > \frac { ( a _ { k } - a _ { l } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { L } \right) = \alpha \sum _ { i = 1 } ^ { 2 } p _ { i } ^ { a _ { L } } ( I _ { i } = 0 , I _ { - i } = 0 ) \cdot \left( \frac { a _ { L } } { 2 } - p _ { i } ^ { a _ { L } } ( I _ { i } = 0 , I _ { - i } = 0 ) + \lambda p \frac { a _ { L } } { - i } ( I _ { i } = 0 , I _ { - i } = 0 ) \right) } \end{array}$ . The sufficient and necessary condition for the platform to induce neither seller to adopt the service is $\begin{array} { r } { \pi _ { p } \left( s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { L } \right) < \pi _ { p } \left( s > \right. } \end{array}$ $\begin{array} { r } { \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { L } \Big ) } \end{array}$ , from which we have $\begin{array} { r } { \alpha > \tilde { \alpha } = \frac { a _ { H } - a _ { L } } { a _ { H } \lambda + a _ { L } \lambda } . } \end{array}$ That is, in the low-demand market, the platform sets $\begin{array} { r } { s > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ such that neither seller adopts the service if and only if $\alpha > \tilde { \alpha }$

## When the market is a high-demand market,

if the platform sets the subscription fee $\begin{array} { r } { s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ such that both sellers adopt the service, then the platform’s profit is: $\begin{array} { r } { \pi _ { p } \left( s = \frac { ( a _ { H } - a _ { l } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { H } \right) = \alpha \sum _ { i = 1 } ^ { 2 } p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \cdot \left( \frac { a _ { H } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) + } \end{array}$ $\begin{array} { r } { 2 \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } ; } \end{array}$ if the platform sets the subscription fee ?? $\begin{array} { r } { > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ such that neither seller adopts the service, then the platform’s profit is: $\begin{array} { r } { \pi _ { p } \left( s > \frac { ( a _ { H } - a _ { i } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { H } \right) = \alpha \sum _ { i = 1 } ^ { 2 } p _ { i } ^ { a _ { H } } ( I _ { i } = 0 , I _ { - i } = 0 ) \cdot \left( \frac { a _ { H } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 0 , I _ { - i } = 0 ) + \lambda p \frac { a _ { H } } { - i } ( I _ { i } = 0 , I _ { - i } = 0 ) \right) } \end{array}$ . By comparison, we $\begin{array} { r } { \mathrm { g e t } { \cdot } \pi _ { p } \left( s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { H } \right) > \pi _ { p } \left( s > \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } , a = a _ { L } \right) } \end{array}$ . That is, the platform sets $\begin{array} { r } { s = \frac { ( a _ { H } - a _ { L } ) ^ { 2 } ( 1 - \alpha ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ such that both sellers adopt the service in the high-demand market.

## Proof of Proposition D1

In Proposition D1, the proof of the results related to sellers’ profitability, prices, consumer surplus and social welfare follows the same structure as that of Proposition 1, 2, 3 and 4, respectively. Here, we do not repeat the proof but provide the difference value between the value of those market outcomes under different sellers’ adoption decision. Note that all of the following comparisons are made under the technical assumption $3 a _ { L } - a _ { H } > 0$ . For sellers’ profits, in the low-demand market, $\begin{array} { r } { \pi _ { i } ^ { r } | _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { L } } - \pi _ { i } ^ { r } | _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { L } } = - \frac { ( a _ { H } - a _ { L } ) ( a _ { H } + a _ { L } ) ( 1 - \alpha ) \lambda } { 1 6 ( 2 - \lambda ) ^ { 2 } } < 0 , } \end{array}$

where the superscript ?? in ??<sup>??</sup> stands for “realized”; in the high-demand market, $\begin{array} { r } { \pi _ { i } ^ { r } | _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { H } } - \pi _ { i } ^ { r } | _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { H } } = \frac { ( a _ { H } - a _ { L } ) ( a _ { H } + a _ { L } ) ( 1 - \alpha ) \lambda } { 1 6 ( 2 - \lambda ) ^ { 2 } } > 0 } \end{array}$ . For sellers’ prices, in the low-demand market, $\begin{array} { r } { p _ { i } ^ { a _ { L } } ( I _ { i } = 1 , I _ { - i } = 1 ) - p _ { i } ^ { a _ { L } } ( I _ { i } = 0 , I _ { - i } = 0 ) = - \frac { a _ { H } - a _ { L } } { 8 - 4 \lambda } < 0 } \end{array}$ ; in the high-demand market, $\begin{array} { r } { p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) - p _ { i } ^ { a _ { H } } ( I _ { i } = 0 , I _ { - i } = 0 ) = \frac { a _ { H } - a _ { L } } { 8 - 4 \lambda } > 0 } \end{array}$ . For consumer surplus, in the low-demand market, $\begin{array} { r } { \left. C S \right| _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { L } } - \left. C S \right| _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { L } } = } \end{array}$ $\begin{array} { r } { \frac { ( a _ { H } - a _ { L } ) \left( a _ { L } ( 5 - \lambda ) + a _ { H } ( - 1 + \lambda ) \right) } { 1 6 ( 2 - \lambda ) ^ { 2 } } > 0 , } \end{array}$ ; in the high-demand market, under our assumption $3 a _ { L } - a _ { H } > 0$ mentioned in the proof of Lemma D1, we have $\begin{array} { r } { C S | _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { H } } - C S | _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { H } } = \frac { ( a _ { H } - a _ { L } ) ( a _ { L } + a _ { H } ( - 5 + \lambda ) - a _ { L } \lambda ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } < 0 } \end{array}$ . For social welfare, in the low-demand market, under our assumption $\begin{array} { r } { 3 a _ { L } - a _ { H } > 0 \ , \ S W | _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { L } } - S W | _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { L } } = \frac { ( a _ { H } - a _ { L } ) \left( a _ { H } ( 1 - 2 \alpha ) ( 1 - \lambda ) + a _ { L } \left( 3 - 3 \lambda + 2 \alpha ( 1 + \lambda ) \right) \right) } { 1 6 ( - 2 + \lambda ) ^ { 2 } } > 0 ; } \end{array}$ in the high-demand market, $\scriptstyle S W \mid _ { I _ { 1 } = 1 , I _ { 2 } = 1 } ^ { a = a _ { H } } -$ $\begin{array} { r } { { S W | } _ { I _ { 1 } = 0 , I _ { 2 } = 0 } ^ { a = a _ { H } } = - \frac { ( a _ { H } - a _ { L } ) ( a _ { L } ( 1 - 2 \alpha ) ( 1 - \lambda ) + a _ { H } ( 3 - 3 \lambda + 2 \alpha ( 1 + \lambda ) ) ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } < 0 } \end{array}$

## Proof of Proposition D2

According to Lemma D1, in the high-demand market, the platform always sets a low subscription fee (i.e., $\begin{array} { r } { s ^ { * } = { \frac { ( 1 - \alpha ) ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } } ) } \end{array}$ to induce the adoption of both sellers. Thus, we conclude that, as the commission rate ?? increases, in the high-demand market, the equilibrium subscription fee $s ^ { * }$ for the analytics service decreases. On the other hand, in the low-demand market, when the commission rate is relatively high (i.e., $\alpha > \tilde { \alpha } )$ , the platform sets a high subscription fee $\begin{array} { r } { ( \mathrm { i . e . , } s ^ { \ast } > \frac { ( 1 - \alpha ) ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ ) such that neither seller adopts the service; otherwise, the platform sets a low subscription fee $\begin{array} { r } { ( \mathrm { i . e . , } s ^ { * } = \frac { ( 1 - \alpha ) ( a _ { H } - a _ { L } ) ^ { 2 } } { 1 6 ( 2 - \lambda ) ^ { 2 } } ) } \end{array}$ to induce the adoption of both sellers. Thus, we conclude that, as the commission rate ?? increases, in the low-demand market, the equilibrium subscription fee $\boldsymbol { s } ^ { * }$ for the analytics service either increases (when the increase in ?? changes the adoption outcome from both sellers adopt the service to neither seller adopts the service) or decreases (when the increases in ?? does not change the adoption outcome).

## Proof of Lemma E1

In Lemma E1, the sellers’ on-equilibrium-path beliefs are $P r [ a = a _ { H } ] = P r [ a = a _ { L } ] = 1 / 2$ , and their off-equilibrium-path beliefs are $P r [ a = a _ { H } ] = 1$ . Note that, here, the on-equilibrium-path (off-equilibrium-path) refers to the cases wherein the platform sets subscription fee $s = s ^ { * } \left( s \neq s ^ { * } \right)$ . Following the convention of backward induction, in this proof, we first derive the sellers’ pricing decision in Stage 3, then we derive the sellers’ adoption decision in Stage 2, and finally, we derive the platform’s subscription fee decision in Stage 1. Similar to the main model, we make the assumption $4 f < 3 a _ { L } - a _ { H }$ to rule out the uninteresting equilibrium outcomes where sellers have zero demand.

## The sellers pricing decisions

In this modeling extension, in Stage 3, the sellers either become fully aware of the true market size or hold their prior beliefs about the market size $( \mathrm { i . e . , P r } [ a = a _ { H } ] = \operatorname* { P r } [ a = a _ { L } ] = 1 / 2 )$ . More specifically, if the platform commands different subscription fee under different market sizes or seller ?? adopts the analytics service, then seller ?? becomes fully aware of the true market size; if the platform commands the same subscription fee regardless of the true market size and seller ?? does not adopt the service, then seller ?? holds the prior belief $\Pr [ a = a _ { H } ] = \operatorname* { P r } [ a = a _ { L } ] = 1 / 2$ That is, the platform’s commanding different subscription fees under different market sizes and seller ??’s adopting the service have the same impact on seller ??’s belief. Thus, the sellers’ pricing decisions under all possible sellers’ beliefs can be found in Lemma 1.

## The sellers’ adoption of the analytics service

If the platform commands different subscription fees under different market sizes, then, as we have discussed before, the sellers become fully aware of the true market size. Accordingly, the analytics service becomes no value to the sellers and the sellers would not adopt the analytics service. If the platform commands the same subscription fee regardless of the true market size, then the sellers hold their prior beliefs about the market size (i.e., $\mathrm { P r } [ a = a _ { H } ] = \mathrm { P r } [ a = a _ { L } ] = \bar { 1 / 2 } )$ . Thus, the corresponding adoption decisions of sellers are summarized in Lemma 2.

## The platform’s subscription fee decision

Firstly, we prove that no separating equilibrium exists. That is, the platform would not command different subscription fees under different market sizes. We prove this by contradiction. Suppose that in the equilibrium, the platform sets the subscription fee $s = s _ { H }$ in the highdemand market and $s = s _ { L }$ in the low-demand market $( s _ { H } \neq s _ { L } ) ;$ then, the corresponding reasonable belief of the sellers would be the market is a high-demand market when seeing $s = s _ { H }$ and the market is a low-demand market when seeing $s = s _ { L }$ . When the sellers believe that the market is a high-demand market, according to Lemma 1, their pricing decisions are $\begin{array} { r } { p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) = \frac { f ( 2 + \lambda ) + a _ { H } ( 2 \mu _ { i } + \lambda \mu _ { - i } ) } { a - \lambda ^ { 2 } } } \end{array}$ ; when the sellers believe that the market is a low-demand market, their pricing decisions are $\begin{array} { r } { p _ { i } ^ { a _ { L } } ( I _ { i } = 1 , I _ { - i } = 1 ) = \frac { f ( 2 + \lambda ) + a _ { L } ( 2 \mu _ { i } + \lambda \mu _ { - i } ) } { 4 - \lambda ^ { 2 } } \iota } \end{array}$ , where $\mu _ { i } =$ $\mu _ { - i } = 1 / 2$ . Accordingly, in the high-demand market, if the platform sets a subscription fee $s = s _ { H }$ , then its profit (which equals its marketplace revenue as neither seller adopts the service in a separating equilibrium) is

$$
\pi_ {p} (s = s _ {H}, a = a _ {H}) = \sum_ {i = 1} ^ {2} f \left(\frac {a _ {H}}{2} - p _ {i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1) + \lambda p _ {- i} ^ {a _ {H}} (I _ {i} = 1, I _ {- i} = 1)\right);
$$

if the platform sets a subscription fee $s = s _ { L }$ , then its profit is

$$
\pi_ {p} (s = s _ {L}, a = a _ {H}) = \sum_ {i = 1} ^ {2} f \left(\frac {a _ {H}}{2} - p _ {i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1) + \lambda p _ {- i} ^ {a _ {L}} (I _ {i} = 1, I _ {- i} = 1)\right).
$$

As $p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) > p _ { i } ^ { a _ { L } } ( I _ { i } = 1 , I _ { - i } = 1 )$ , we have $\pi _ { p } ( s = s _ { H } , a = a _ { H } ) < \pi _ { p } ( s = s _ { L } , a = a _ { H } )$ . Thus, in the high-demand market, the platform always has incentive to mimic the platform’s behavior in the low-demand market. Accordingly, no separating equilibrium can be sustained.

Secondly, we verify the validity of the pooling equilibrium summarized in Lemma E1. As the game is a dynamic game with incomplete information, the solution concept is weak Perfect Bayesian Equilibrium. Thus, to verify the equilibrium summarized in Lemma 1, we need to verify whether the sellers’ beliefs (as specified at the beginning of this proof) are consistent with the platform’s strategy. The verification is conducted in the following two steps.

## Step 1. Given the platform’s strategy, the sellers’ beliefs are reasonable.

On the equilibrium path, given that the platform’s strategy (that setting the subscription fee $s = s ^ { * }$ in the equilibrium regardless of the market size), it is reasonable for the sellers to not update their beliefs. Note that any off-path belief is reasonable for weak PBE.

## Step 2. Given the beliefs, the platform’s strategy is optimal.

Given the sellers’ on-path (when $s = s ^ { * } )$ beliefs $P r [ a = a _ { H } ] = P r [ a = a _ { L } ] = 1 / 2$ and the sellers’ off-path (when $s \neq s ^ { * } )$ beliefs $P r [ a = a _ { H } ] = 1$ , the platform’s strategy is optimal. More specifically,

(1) when $s ^ { * } \leq \tilde { s }$ and the equilibrium is an adopting equilibrium,

\- in the low-demand market, if the platform sets $s = s ^ { * }$ , both sellers adopt the service and the platform’s profit is: $\begin{array} { r } { \pi _ { p } ( s = s ^ { * } , a = a _ { L } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { L } } { 2 } - p _ { i } ^ { a _ { L } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { L } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) + 2 s ^ { * } ; } \end{array}$ if the platform sets $s \neq s ^ { * }$ , both sellers believe that the market is a high-demand market and hence do not adopt the service, and accordingly, the platform’s profit i $\begin{array} { r } { \because \pi _ { p } ( s \neq s ^ { * } , a = a _ { L } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { L } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) } \end{array}$ . Accordingly, we have $\pi _ { p } ( s = s ^ { * } , a = a _ { L } ) >$ $\pi _ { p } ( s \neq s ^ { * } , a = a _ { L } )$ ; that is, setting $s = s ^ { * }$ is the best strategy of the platform in this case.

in the high-demand market, if the platform sets $s = s ^ { * }$ , both sellers adopt the service and the platform’s profit $\begin{array} { r } { \mathfrak { s } \colon \pi _ { p } ( s = s ^ { * } , a = a _ { H } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { H } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) + 2 s ^ { * } ; \mathrm { i } } \end{array}$ the platform sets $s \neq s ^ { * } ,$ , both sellers believe that the market is a high-demand market and hence do not adopt the service, and accordingly, the platform’s profit is: $\begin{array} { r } { \pi _ { p } ( s \neq s ^ { * } , a = a _ { H } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { H } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) } \end{array}$ . Accordingly, we have $\pi _ { p } ( s = s ^ { * } , a =$ $a _ { H } ) > \pi _ { p } ( s \ne s ^ { * } , a = a _ { H } )$ ; that is, setting $s = s ^ { * }$ is the best strategy of the platform in this case.

(2) when $s ^ { * } > \tilde { s }$ and the equilibrium is a non-adopting equilibrium,

in the low-demand market, if the platform sets $s = s ^ { * }$ , neither seller adopts the service and the platform’s profit is $\begin{array} { r } { \cdot \pi _ { p } ( s = s ^ { * } , a = a _ { L } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { L } } { 2 } - p _ { i } ^ { a _ { L } } ( I _ { i } = 0 , I _ { - i } = 0 ) + \lambda p _ { - i } ^ { a _ { L } } ( I _ { i } = 0 , I _ { - i } = 0 ) \right) } \end{array}$ ;if the platform sets $s \neq s ^ { * }$ , both sellers believe that the market is a high-demand market and hence do not adopt the service, and accordingly, the platform’s profit is: $\begin{array} { r } { \cdot \pi _ { p } ( s \neq s ^ { * } , a = a _ { L } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { L } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) } \end{array}$ . Accordingly, we have $\pi _ { p } ( s = s ^ { * } , a = a _ { L } ) >$ $\pi _ { p } ( s \neq s ^ { * } , a = a _ { L } )$ ; that is, setting $s = s ^ { * }$ is the best strategy of the platform in this case.

in the high-demand market, if the platform sets $s = s ^ { * }$ , neither seller adopts the service and the platform’s profit is: $\begin{array} { r } { \pi _ { p } ( s = s ^ { * } , a = a _ { H } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { H } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 0 , I _ { - i } = 0 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 0 , I _ { - i } = 0 ) \right) } \end{array}$ ; if the platform sets $s \neq s ^ { * }$ , both sellers believe that the market is a high-demand market and hence do not adopt the service, and accordingly, the platform’s profit is: $\begin{array} { r } { \pi _ { p } ( s \neq s ^ { * } , a = a _ { H } ) = \sum _ { i = 1 } ^ { 2 } f \left( \frac { a _ { H } } { 2 } - p _ { i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) + \lambda p _ { - i } ^ { a _ { H } } ( I _ { i } = 1 , I _ { - i } = 1 ) \right) } \end{array}$ . Accordingly, we have $\pi _ { p } ( s = s ^ { * } , a = a _ { H } ) >$ $\pi _ { p } ( s \neq s ^ { * } , a = a _ { H } )$ ; that is, setting $s = s ^ { * }$ is the best strategy of the platform in this case.

## Proof of Proposition E1

The proofs for the impact of the analytics service on sellers’ prices, consumer surplus and social welfare directly follow the proofs for Proposition 1, Proposition 3 and Proposition 4. In this proof, we focus on the impact of the analytics service on the sellers’ profitability.

## The low-demand market case:

We first provide a general formula of seller ??’s realized profit in the low-demand market case: $\begin{array} { r } { \pi _ { i } ^ { r } = ( p _ { i } - f ) \left( \frac { a _ { L } } { 2 } - p _ { i } + \lambda p _ { - i } \right) - I _ { i } s ^ { * } } \end{array}$ , where the superscript ?? in $\pi _ { i } ^ { r }$ stands for “realized.” Seller ??’s realized profit without the analytics service is

$$
\pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = \pi_ {i} ^ {r} \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 0, I _ {2} = 0), I _ {1} = 0, I _ {2} = 0 \big).
$$

Seller ??’s price with the analytics service under the equilibrium outcome $I _ { 1 } = I _ { 2 } = 1$ is

$$
\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} = \pi_ {i} ^ {r} \big (p _ {i} = p _ {i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), p _ {- i} = p _ {- i} ^ {a _ {L}} (I _ {1} = 1, I _ {2} = 1), I _ {1} = 1, I _ {2} = 1 \big).
$$

We have

$$
\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {L}} - \pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {L}} = \frac {(a _ {H} - a _ {L}) (a _ {H} (1 - \lambda) - a _ {L} - (a _ {L} - 4 f (1 - \lambda)) \lambda)}{1 6 (2 - \lambda) ^ {2}} - s ^ {*},
$$

which is positive when $\begin{array} { r } { s ^ { \ast } < \frac { ( a _ { H } - a _ { L } ) ( a _ { H } ( 1 - \lambda ) - a _ { L } - ( a _ { L } - 4 f ( 1 - \lambda ) ) \lambda ) } { 1 6 ( 2 - \lambda ) ^ { 2 } } } \end{array}$ and negative otherwise. Thus, with the analytics service, in the low-demand market, the sellers can be worse off.

## The high-demand market case:

Similar to the proof for the low-demand market case, in the high-demand market, as $s ^ { * } < \tilde { s }$ when the sellers adopt the service, we have:

$$
\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} ^ {a = a _ {H}} - \pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} ^ {a = a _ {H}} = \frac {(a _ {H} - a _ {L}) (a _ {H} (1 + \lambda) + (- 1 + \lambda) (a _ {L} + 4 f \lambda))}{1 6 (2 - \lambda) ^ {2}} - s ^ {*} > \frac {(a _ {H} - a _ {L}) (a _ {H} (1 + \lambda) + (- 1 + \lambda) (a _ {L} + 4 f \lambda))}{1 6 (2 - \lambda) ^ {2}} - \tilde {s} = \frac {(a _ {H} - a _ {L}) (a _ {H} + a _ {L} + 4 f (- 1 + \lambda)) \lambda}{1 6 (2 - \lambda) ^ {2}} > 0.
$$

Thus, we conclude that, with the analytics service, in the high-demand market, the sellers are better off.

## Proof of Proposition F1

We would first like to clarify that all of the following comparisons are made under the technical assumption $3 a _ { L } - a _ { H } > 4 f$

• Sellers’ prices:

The expected sellers’ prices with the analytics service:

$$
E \big (p _ {i} (I _ {i} = 1, I _ {- i} = 1) \big) = \frac {p _ {i} ^ {a _ {H}} (I _ {i} = 1 , I _ {- i} = 1) + p _ {i} ^ {a _ {L}} (I _ {i} = 1 , I _ {- i} = 1)}{2}.
$$

The expected sellers’ prices without the analytics service:

$$
E \big (p _ {i} (I _ {i} = 0, I _ {- i} = 0) \big) = \frac {p _ {i} ^ {a _ {H}} (I _ {i} = 0 , I _ {- i} = 0) + p _ {i} ^ {a _ {L}} (I _ {i} = 0 , I _ {- i} = 0)}{2}.
$$

Comparison:

$$
E \big (p _ {i} (I _ {i} = 1, I _ {- i} = 1) \big) - E \big (p _ {i} (I _ {i} = 0, I _ {- i} = 0) \big) = 0.
$$

• Sellers’ profits:

The expected sellers’ profits with the analytics service:

$$
E \left(\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1}\right) = \frac {\pi_ {i} ^ {r} | _ {I _ {1} = 1 , I _ {2} = 1} ^ {a = a _ {H}} + \pi_ {i} ^ {r} | _ {I _ {1} = 1 , I _ {2} = 1} ^ {a = a _ {L}}}{2},
$$

where the superscript ?? in $\pi _ { i } ^ { r }$ stands for “realized.”

The expected sellers’ prices without the analytics service:

$$
E \big (\pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} \big) = \frac {\pi_ {i} ^ {r} | _ {I _ {1} = 0 , I _ {2} = 0} ^ {a = a _ {H}} + \pi_ {i} ^ {r} | _ {I _ {1} = 0 , I _ {2} = 0} ^ {a = a _ {L}}}{2}.
$$

Comparison:

$$
E \big (\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} \big) - E \big (\pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} \big) = 0.
$$

• Consumer surplus:

The expected consumer surplus with the analytics service:

$$
E \big (C S | _ {I _ {1} = 1, I _ {2} = 1} \big) = \frac {C S | _ {I _ {1} = 1 , I _ {2} = 1} ^ {a = a _ {H}} + C S | _ {I _ {1} = 1 , I _ {2} = 1} ^ {a = a _ {L}}}{2}.
$$

The expected consumer surplus without the analytics service:

$$
E \big (C S | _ {I _ {1} = 0, I _ {2} = 0} \big) = \frac {C S | _ {I _ {1} = 0 , I _ {2} = 0} ^ {a = a _ {H}} + C S | _ {I _ {1} = 0 , I _ {2} = 0} ^ {a = a _ {L}}}{2}.
$$

Comparison:

$$
E \big (\pi_ {i} ^ {r} | _ {I _ {1} = 1, I _ {2} = 1} \big) - E \big (\pi_ {i} ^ {r} | _ {I _ {1} = 0, I _ {2} = 0} \big) = - \frac {(a _ {H} - a _ {L}) ^ {2} (3 - \lambda)}{1 6 (2 - \lambda) ^ {2}} <   0
$$

• Social welfare:

The expected social welfare with the analytics service:

$$
E \big (S W | _ {I _ {1} = 1, I _ {2} = 1} \big) = \frac {S W | _ {I _ {1} = 1 , I _ {2} = 1} ^ {a = a _ {H}} + S W | _ {I _ {1} = 1 , I _ {2} = 1} ^ {a = a _ {L}}}{2}.
$$

The expected social welfare without the analytics service:

$$
E \big (S W | _ {I _ {1} = 0, I _ {2} = 0} \big) = \frac {S W | _ {I _ {1} = 0 , I _ {2} = 0} ^ {a = a _ {H}} + S W | _ {I _ {1} = 0 , I _ {2} = 0} ^ {a = a _ {L}}}{2}.
$$

Comparison:

$$
E \big (S W | _ {I _ {1} = 1, I _ {2} = 1} \big) - E \big (S W | _ {I _ {1} = 0, I _ {2} = 0} \big) = - \frac {(a _ {H} - a _ {L}) ^ {2} (1 - \lambda)}{1 6 (2 - \lambda) ^ {2}} <   0.
$$

## Appendix H

## Derivation of the Expression for Consumer Surplus

Our model is based on Singh and Vives’ (1984) analysis of two firms competing for consumers with differentiated products. By choosing the purchasing quantity from seller ?? (denoted by $d _ { i } )$ , the consumers as a whole are (equivalently, a representative consumer is) maximizing the utility function:

$$
U _ {c} (d _ {1}, d _ {2}) = \alpha_ {1} d _ {1} + \alpha_ {2} d _ {2} - \frac {\beta_ {1} d _ {1} ^ {2} + 2 \gamma d _ {1} d _ {2} + \beta_ {2} d _ {2} ^ {2}}{2} - p _ {1} d _ {1} - p _ {2} d _ {2}.
$$

By simultaneously solving for the partial derivatives $\partial U _ { c } / \partial d _ { 1 } = 0$ and $\partial U _ { c } / \partial d _ { 2 } = 0$ , as shown in Singh and Vives (1984), the demand functions of the sellers are as follow:

$$
d _ {1} = \frac {\alpha_ {1} \beta_ {2} - \alpha_ {2} \gamma - p _ {1} \beta_ {2} + p _ {2} \gamma}{\beta_ {1} \beta_ {2} - \gamma^ {2}}, d _ {2} = \frac {\alpha_ {2} \beta_ {1} - \alpha_ {1} \gamma - p _ {2} \beta_ {1} + p _ {1} \gamma}{\beta_ {1} \beta_ {2} - \gamma^ {2}},
$$

where $\beta _ { 1 } \beta _ { 2 } - \gamma ^ { 2 } > 0$ . It is worth mentioning that Häckner (2000) provides a more generalized analysis in which $n ( n \geq 2 )$ sellers compete against each other.

Recall that in our model, we have defined the sellers’ demand function as follows:

$$
d _ {1} = \mu_ {1} a - p _ {1} + \lambda p _ {2}, d _ {2} = \mu_ {2} a - p _ {2} + \lambda p _ {1}.
$$

Following the same logic as Singh and Vives (1984) and Häckner (2000), we can obtain the consumers’ utility (i.e., consumer surplus) in our paper through reverse induction. Specifically, we can calculate the consumer surplus using the equation:

$$
C S = U _ {c} = \sum_ {i = 1} ^ {2} \left(\frac {a (\mu_ {i} + \lambda \mu_ {- i})}{1 - \lambda^ {2}} d _ {i}\right) - \frac {d _ {1} ^ {2} + 2 \lambda d _ {1} d _ {2} + d _ {2} ^ {2}}{2 (1 - \lambda^ {2})} - p _ {1} d _ {1} - p _ {2} d _ {2}.
$$

This consumer utility function yields the demand function used in our study. Specifically, by simultaneously solving $\partial U _ { c } / \partial d _ { 1 } = 0$ and $\partial U _ { c } / \partial d _ { 2 } = 0$ , we can obtain the demand function (i.e., $d _ { i } = \mu _ { i } a - p _ { i } + \lambda p _ { - i } )$ adopted in the paper.
