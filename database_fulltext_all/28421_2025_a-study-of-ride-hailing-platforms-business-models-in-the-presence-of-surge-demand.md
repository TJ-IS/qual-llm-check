---
otero_id: 28421
otero_key: "E4K8NAW6"
title: "A Study of Ride-Hailing Platforms’ Business Models in the Presence of Surge Demand"
authors: "Haiyang Feng; Nan Feng; Ling Zhang; Zhengrui Jiang; Minqiang Li"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0695"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Study of Ride-Hailing Platforms’ Business Models in the Presence of Surge Demand

Haiyang Feng,<sup>a,</sup>\* Nan Feng,<sup>a</sup> Ling Zhang,<sup>b</sup> Zhengrui Jiang,<sup>c</sup> Minqiang Li<sup>a,d</sup>

<sup>a</sup> College of Management and Economics, Tianjin University, Tianjin 300072, China; <sup>b</sup> School of Management, Shijiazhuang Tiedao University, Hebei 050043, China; <sup>c</sup> School of Management and Economics, The Chinese University of Hong Kong, Shenzhen 518172, China; <sup>d</sup> Laboratory of Computation and Analytics of Complex Management Systems, Tianjin University, Tianjin 300072, China \*Corresponding author

Contact: hyfeng@tju.edu.cn, https://orcid.org/0000-0002-4301-001X (HF); fengnan@tju.edu.cn (NF); zhangling@stdu.edu.cn (LZ); zjiang@cuhk.edu.cn, https://orcid.org/0000-0002-8576-7643 (ZJ); mqli@tju.edu.cn, https://orcid.org/0000-0001-7929-3747 (ML)

Received: December 18, 2022 Revised: October 5, 2023; May 28, 2024; November 23, 2024; February 1, 2025 Accepted: February 16, 2025 Published Online in Articles in Advance: March 13, 2025

https://doi.org/10.1287/isre.2022.0695

Copyright: © 2025 INFORMS

Abstract. Booming demand in the ride-hailing market allows ride-hailing platforms to experiment with different business models. This study analyzes whether a ride-hailing platform should adopt a closed business model, that is, serving riders only with platformowned vehicles, or an open business model, that is, allowing private vehicles to utilize the platform to provide services. Special attention is paid to the impact of uneven demand during a day; thus, the game-theoretical model we develop features a two-period framework with normal and surge periods. Analytical results reveal that the open business model leads to more service supply (supply-augmenting effect) and a lower price increase (price discrimination–hindering effect) in the surge period, both benefiting riders. It also reduces the number of idle vehicles in the normal period, thus resulting in more efficient utilization of vehicle resources. These effects jointly lead to higher social welfare under the open business model. Interestingly, the platform does not always benefit from adopting the open business model, and a higher level of demand surge has nonmonotonic impacts on the optimality of this model. In sum, the open business model always benefits the riders, private drivers, and the society as a whole, but it may not be more profitable for the platform. This interesting result calls for policymakers to incentivize the platform so that it adopts the open business model instead of the closed one.

History: Ram Gopal, Senior Editor; Atanu Lahiri, Associate Editor. Funding: This work was supported by the National Natural Science Foundation of China [Grants 72231004, 72394373, and 72022012].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0695.

Keywords: ride-hailing platform • open/closed business model • normal/surge period • surge pricing

## 1. Introduction

Advances in mobile communication technologies have facilitated the development of ride-hailing platforms such as Uber, Lyft, and Didi. The global ride-hailing market size is estimated to rise at a compound annual growth rate of 14.36% from 2024 to 2030, reaching nearly US\$291.83 billion by 2030 (Maximize Market Research 2024). In China, the ride-hailing market has witnessed significant growth and development with an estimated revenue of US\$59.56 billion in 2024; the market volume is expected to reach US\$82.09 billion and the number of users is projected to hit 0.66 billion by 2029 (Statista Market Insights 2023).

One of the major challenges faced by these online ride-hailing platforms is the uneven distribution of demand during a day. There is typically a demand surge during rush hours in urban centers. Statistics show that the number of users opening the Uber app in the surge period is four times more than that in the normal period, but less than half of their demands can be fulfilled (Hall et al. 2015). To cope with the demand surge, ride-hailing platforms usually rely on two instruments. First, some platforms adopt an open business model and attract as many qualified private drivers to register as service providers as possible. Second, dynamic pricing is now widely adopted to better regulate supply with demand.

Whereas the open business model is prevalent in the ride-hailing market, adopted by dominant platforms such as DiDi, Uber, and Lyft, some major ride-hailing platforms, such as Caocao Chuxing and T3 Chuxing in China, took an opposite path, that is, keeping a closed business model under which the platform purchases its own vehicles and hires full-time drivers to serve its riders. Under this business model, the platform reaps all the revenues generated from serving riders. The drawback is that the platform also affords high fixed and variable costs under this asset-heavy business model, which could lead to a slower speed of expansion. Moreover, some platforms adopt a hybrid model to more effectively align with the markets they serve. For instance, Shenzhou Zhuanche, a major ride-hailing platform in China, not only maintains a large number of platform-owned vehicles but also embraces private drivers by providing them access to traffic, technology, and brand resources through its U+ open platform. As a result, Shenzhou Zhuanche has evolved into an open platform, characterized by a hybrid business model that incorporates both platform-owned and private vehicles.

In view of the diverse business models adopted by ride-hailing platforms, we aim to conduct a detailed comparison of the closed and open business models with special attention paid to the impact of demand surge on platforms’ optimal decisions. Figure 1 shows the three market structures considered in this study. A platform could serve all riders using its own vehicles, that is, adopting a closed business model (shown in Figure 1(a)). Alternatively, given the high cost of owning vehicles and hiring drivers, a platform may consider an open business model, which includes two possibilities: a pure-sharing open model (shown in Figure 1(b)) and a hybrid open model (shown in Figure 1(c)). Under a pure-sharing open model, only private drivers provide ride-hailing services on the platform. Under a hybrid open model, both the platform-owned and private vehicles are simultaneously made available to riders.

The closed business model enables a platform to generate revenues directly from providing ride-hailing services to riders. However, this heavy-asset model reduces flexibility in supply and increases operating cost, making it difficult to expand market share. Under the pure-sharing open model, a platform does not bear fixed costs and the supply is more flexible, but the platform only obtains a small proportion of revenues. Under the hybrid open model, a platform obtains revenue from its own vehicles as well as private vehicles. The participation of the private drivers increases the supply of ride-hailing services on the platform, thus easing up the scarcity of resources especially during the period of surge demand. However, accepting private drivers leads to internal competition on the platform. Although the platform charges them a commission fee, private drivers do split a proportion of orders and profits, which potentially reduces the platform’s net profit. Therefore, whether the platform should adopt the closed, pure-sharing open, or hybrid open business model is an important strategic question to be addressed. Motivated by the trade-off faced by a ride hailing firm in the presence of surge demand, we aim to answer the following research questions:

I. Should a ride-hailing platform adopt a closed or an open business model?

II. How does a change in business model impact the service price and the number of vehicles purchased by the ride-hailing platform?

III. How does demand surge in high traffic hours affect the ride-hailing platform’s optimal business model, pricing strategy, and profitability?

We build a two-period model, corresponding to normal and surge periods, to answer these questions. In this model, a ride-hailing firm first chooses its business model and makes vehicle purchase and pricing decisions, after which private drivers and riders make participation decisions. Several findings emerge from our analysis. First, compared with the closed business model, adopting the open business model leads to two important effects: the supply-augmenting effect, which increases the number of available vehicles on the platform, and the price discrimination–hindering effect, which results in a lower price increase in the surge period, both benefiting riders. In addition, the open business model leads to two desirable outcomes for ride-hailing firms: the platform can purchase fewer vehicles, and these vehicles are less likely to sit idle in the normal period, both because of the more efficient utilization of vehicle resources. Second, the open business model enables the platform to reduce the price gap between the normal and surge periods, which also benefits riders and helps reduce public criticisms toward surge pricing. Moreover, with a steeper demand surge, the open business model becomes more effective in reducing the price gap under a sufficiently high (or low) demand surge or a low price sensitivity of riders. Interestingly, despite the identified benefits, the open business model does not always dominate the closed business model in terms of profitability for the platform. Specifically, if the total potential demand is low, the open business model outperforms the closed model when the magnitude of the demand surge is moderate. In contrast, when the total potential demand is high, a small magnitude of demand surge also makes the open business model more likely to be profitable. Finally, the open business model always improves the social welfare within the ride-hailing system. In summary, the open business model benefits riders, private drivers, and society as a whole although it may not necessarily generate more profit for the platform—the party that actually decides the business model. This interesting finding calls for policymakers to incentivize the platform, for example, through providing tax subsidies, to ensure that adopting the open business model is more profitable for the platform as well.

Figure 1. Market Structure of the Closed/Open Business Model  
![](/api/attachments/E4K8NAW6/fulltext/images/85a9e08f58317b4f94b0472e8adbadd96233135aad76c8e5dce8fc692672f37d.jpg)  
Notes. (a) Closed business model. (b) Pure-sharing open model. (c) Hybrid open model.

The rest of the paper is organized as follows. In the next section, we review the related literature. Our model setup is provided in Section 3. The market equilibria under the closed and open business models are derived and compared in Sections 4 and 5. Section 6 summarizes model extensions. We conclude this study in Section 7 with a summary of findings and managerial implications.

## 2. Literature Review

In this section, we review three streams of related literature.

## 2.1. Literature on Platform Openness

The first stream of related literature is on the platform openness strategy. It is a consensus that a closed business model guarantees the firm’s controllability, whereas an open business model incentivizes complementors to join, thereby boosting the supply of resources. Hence, several prior studies focus on the trade-off between controllability and resource availability, deriving the optimal degree of platform openness that strikes a balance between the two. For instance, Economides and Katsamakas (2006) compare industry structures based on proprietary platforms with those based on open-source platforms. They find that, when users have a strong preference for application variety, the proprietary platform gains a higher profit than the open-source platform. Parker and Van Alstyne (2018) build an innovation model that characterizes the optimal degree of platform openness and find that the optimal degree declines with a rise in the intrinsic platform value but increases with developer value, sizes of developer and end-user pools, and level of resource reuse. Niculescu et al. (2018) study the strategic decision of an incumbent to open a proprietary technology platform and show that, when the network effects are of intermediate intensity, the incumbent should open its technology to the entrants with high absorptive capacity. Benzell et al. (2024) empirically examine how opening digital services to third parties fosters growth and find that the adoption of application programming interfaces has a significant and positive effect on economic growth.

Furthermore, some prior studies analyze whether a firm should operate as a platform and how first party and third party product/service providers compete on online platforms. Specifically, Hagiu et al. (2020) investigate whether a multiproduct firm should turn itself into an open platform by hosting competitors and conclude that an open platform can be unilaterally profit able for the multiproduct firm and jointly profitable for both firms. He et al. (2020) empirically investigate the impact of a platform owner’s entry on the demand of third party stores as well as their potential reactions. Song et al. (2021) develop a game-theoretic model to examine why an online retailer opens its platform to third party sellers and analyze the spillover effect of consumer awareness on the third party sellers’ and the retailer’s decisions. Chen and Guo (2022) develop a game-theoretical model to explore how new media advertising affects the openness of a retail platform and find that the availability of low-cost advertising through new media could enable a retailer to open its platform and cooperate with third party sellers. Cheng et al. (2023) explore the impact of a platform’s own brand on incumbent sellers and the effectiveness of protective policies. They conclude that, when the introduction of one’s own brand is banned under the sell-to contract, the incumbent sellers can be better off.

To the best of our knowledge, most previous research in this stream examines the openness strategies of either retailing or technology platforms, whereas our study focuses on a ride-hailing platform. There are several key differences between the prior studies and the present research. First, unlike other types of platforms, a key role played by ride-hailing platforms is to continuously match supply with demand in real time using modern information systems. Second, the market structure examined in our study is more complex than those considered in prior studies because private drivers joining the platform not only serve as service providers to riders but also as competitors to the platform, and the platform must dynamically adjust service price to balance demand with supply in both the normal and surge periods. Third, existing studies primarily focus on whether a platform should open to third parties, whereas this study further investigates the optimal amount of platform-owned resources.

## 2.2. Literature on Ride-Hailing Platforms

This study is also related to the growing literature on ride-hailing platforms. Over the past decade, the ridehailing industry has experienced substantial growth, garnering considerable attention from academia. In particular, the prior literature explores the pricing decisions and matching mechanisms of ride-hailing platforms. Regarding pricing decisions, previous research extensively investigates the impacts of various pricing strategies on the benefits for both sides of ride-hailing platforms. For instance, Cachon et al. (2017) study several pricing schemes that could be used by service platforms, including surge pricing, and find that all stakeholders could benefit from the use of surge pricing on a platform with self-scheduling capacity. Bimpikis et al. (2019) explore spatial price discrimination in the context of ride-sharing platforms and uncover the impact of demand patterns on the platform’s prices and profits as well as consumer surplus. Yang et al. (2020) propose a novel reward scheme integrated with surge pricing and uncover scenarios in which all three stakeholders (passengers, drivers, and platform) are better off under the reward scheme. He et al. (2021) empirically analyze the short-term wage elasticity of labor supply in a real-time ride-sharing market and find a negative labor supply elasticity for drivers. Hu et al. (2022) investigate surge pricing from a temporal perspective, highlighting the strategic behavior by riders and drivers, and they identify two types of equilibrium pricing strategies, which are skimming surge pricing and penetration surge pricing. Zhang et al. (2024) examine the coopetition between a ride-sharing platform and a car-rental firm and show that the supply-side cooperation intensifies the demand-side price competition and decreases the total revenue. Chen et al. (2024) analyze rental models in the sharing economy, showing that the optimal choice depends on the setup and transaction costs.

Meanwhile, other scholars devote themselves to the design and optimization of matching mechanisms on ride-hailing platforms. Specifically, Xu et al. (2020) construct a double-ended queuing model to explore ways for avoiding matching a requesting rider with an idle driver far away. Motivated by the potential benefits of delayed matching, Ke et al. (2020) develop a two-stage framework that incorporates combinatorial optimization and multiagent deep reinforcement learning methods to conduct bipartite matching and determine the delayed time. Experimental results verify that this framework can significantly improve the system efficiency by balancing the trade-offs among success rate, average pickup time, and average matching time. Zhu et al. (2021) propose a Markov decision process model to capture the dynamics in ride-sourcing markets with mixed agents. They demonstrate that the proposed model is effective in balancing the short-term objective of maximizing immediate revenue and the long-term objective of maximizing service rate. Afe\`che et al. (2023) explore how and why platform controls (demand-side admission control and supply-side repositioning control) impact the ride-hailing platform’s equilibrium performance and find that admission control significantly reduces the inefficiency in capacity allocation. Castillo et al. (2024) identify match failures in ride-hailing markets during high demand and prove that surge pricing is an effective solution.

Unlike previous studies in this research stream, the present research considers discriminatory pricing in the normal and surge periods, derives the platform’s optimal in-house service capacity, and examines how the uneven demand affects the platform’s optimal decisions on the business model. Even though demand surge significantly influences the participation deci sions of both service providers and consumers, very few studies explore the impact of it on the outcomes and decisions of ride-hailing platforms, and our study fills this gap. Moreover, this study identifies two crucial effects, namely, the supply-augmenting effect and price discrimination–hindering effect, and explores how they jointly influence the platform’s optimal decision making. To the best of our knowledge, no prior study has considered the joint impact of these two effects.

## 2.3. Literature on the Flexible Manufacturing Strategy

Our study is also closely related with the literature on the flexible manufacturing strategy, which explores the simultaneous use of proactive and reactive capacities to mitigate risks of demand uncertainty and maximize profit. To assess the impact of manufacturing flexibility on firm performance, many prior studies analyze the choice between investing in flexible capac ity versus dedicated capacity (e.g., Fine and Freund 1990, Bish and Wang 2004, Goyal and Netessine 2007, Boyabatlı et al. 2016, Chod et al. 2021). For instance, Goyal and Netessine (2007) evaluate the strategic value of manufacturing flexibility in an uncertain environment and explore the impact of competition on a firm’s choice of technology (product flexible or product dedi cated) and capacity investment decisions. They show that flexibility is not universally optimal. Boyabatlı et al. (2016) investigate how budget constraints affect the choice between flexible technology and dedicated technology. They identify a threshold on unit investment cost that determines the optimal technology choice. Chod et al. (2021) establish that flexible resources carry a learning benefit over nonflexible ones. They find that, when learning becomes valuable, the flexible system leads to a larger increase in profitability than does the nonflexible system as long as profit margins are not too high.

Meanwhile, as enterprises continuously improve supply chain resilience by contracting with multiple suppliers, some scholars study the role of supply flexibility in mitigating the risk of supply interruption (e.g., Kouvelis and Li 2008, Federgruen and Yang 2009, Simchi-Levi et al. 2018, Wang and Webster 2022). For example, Kouvelis and Li (2008) study the potential use of a flexible backup supplier as an emergency response and derive the optimal emergency response policy involving whether and how much to order from the flexible backup supplier. Simchi-Levi et al. (2018) provide an analytical expression for the optimal inventory solution and explore the effectiveness of different degrees of flexibilities. They find that firms should allocate more inventory to high-variability products when their level of flexibility is low. As flexibility improves, firms should allocate more inventory to low-variability products. Wang and Webster (2022) focus on the optimal flexibility configuration of a supply network that comprises both unreliable primary suppliers and reliable backup suppliers and uncover the conditions under which flexibility benefits.

This research differs significantly from these prior studies on flexible manufacturing in the following aspects. First, because of the unique spatial matching mechanism, unlike the firms considered in the prior literature, ride-hailing platforms cannot fully control the order assignment process. Second, a ride-hailing platform can match demand with supply through adjusting the service price. In contrast, few prior studies on flexible manufacturing take pricing decisions into account, and the reactive suppliers’ behaviors are typically managed through contracts. Third, the private drivers considered in this study are more proactive than the reactive suppliers considered in the prior literature. In particular, we divide a day into normal and surge periods, and the private drivers can independently determine whether to join the platform, acting as complementors in the surge periods and competitors in the normal periods. In contrast, prior studies do not model daily demand fluctuations; hence, it is neither possible nor necessary for the contracted suppliers to select the portions of market demand to satisfy.

In summary, the key differences between the present research and related previous studies mandate that we custom-build a theoretical model for the ridehailing market with demand surge considered. As a result, our model and analysis do not resemble those of the prior studies, and our key findings as well as their theoretical and practical implications also differ significantly from those in the prior literature.

## 3. Model Setup

We consider a monopoly ride-hailing platform providing ride-hailing services in a market with surge demand.

Facing the surge demand, the platform assesses the optimality of three different business models, that is, closed, pure-sharing open, and hybrid open. As shown in Figure 2(a), when the firm adopts the closed business model, only the platform-owned vehicles provide ridehailing service to riders, and the platform reaps all the service fees and pays fixed salaries to the drivers. As illustrated in Figure 2, (b) and (c), when it is open to private drivers, the platform could adopt either the puresharing or hybrid open model depending on whether it purchases platform-owned vehicles. The private drivers, serving riders with their private vehicles, obtain per-transaction payment and pay commissions to the platform.

Because of the uneven demand for ride-hailing service during a day, a two-period model, including a normal period and a surge period, is used to differentiate the low demand during the nonrush hours and the demand surge during rush hours. As shown in Figure $^ { 3 , }$ the length of the normal period is denoted by $t _ { N }$ and that of the surge period by $t _ { S } . ^ { 1 }$ Similarly, $a _ { N }$ and $a _ { S }$ denote the sizes of potential demand per unit time in the two periods. In both periods, given the service price set by the platform, some riders request rides. Without loss of generality, we assume that each rider requests one unit of service per unit of time. Following prior studies (e.g., Hu et al. 2022), if riders who request rides outnumber available drivers, each rider, regardless of the rider’s valuation, has the same likelihood of being served; if drivers outnumber ride requests, all rider requests are satisfied and some drivers are idle.

The sequence of events proceeds as follows.

I. The ride-hailing platform decides whether to accept private drivers.

II. The platform determines the number of wholly owned vehicles.<sup>2</sup>

III. The platform sets its service prices for the normal and surge periods.

Figure 2. Closed/Open Business Model  
![](/api/attachments/E4K8NAW6/fulltext/images/e881c1d9f7863f862870de57c821133a1cd2d611176ab8b217406a0d85170058.jpg)

Figure 3. Two-Period Mode  
![](/api/attachments/E4K8NAW6/fulltext/images/6455a7871ed0090079e7308403e2b3f11831294fa6f3595aeeb77b14ae755401.jpg)

IV. The riders and private drivers (if an open model is adopted) make participation decisions.

As illustrated in Figure 4, if the platform chooses not to accept private drivers, it adopts a closed business model and then decides the optimal number of wholly owned vehicles. If the platform chooses to accept private drivers, depending on whether it purchases vehicles or not in the second stage, its business model corresponds to the two types of open models.

## 3.1. Riders’ Decisions

Following the setting in Cachon et al. (2017) and Yang et al. (2020), given the service price, the number of riders requesting ride-hailing service per unit time in period j is

$$
M _ {j} ^ {i} = a _ {j} - b p _ {j} ^ {i},\tag{1}
$$

where $a _ { j }$ is the potential market size (per unit time) in period $j ,$ b captures the riders’ price sensitivity, and $p _ { j } ^ { i }$ denotes the service price in period j. The superscript i $( i \in \{ C , O \} )$ denotes the business model adopted by the platform, where $^ { \prime \prime } C ^ { \prime \prime }$ stands for closed business model and $^ { \prime \prime } O ^ { \prime \prime }$ for open business model. The subscript j $( j \in \{ N , S \} )$ denotes the service period, in which ${ \hat { \mathbf { \Omega } } } ^ { \prime \prime } { \hat { N } } ^ { \prime \prime }$ and $^ { \prime \prime } S ^ { \prime \prime }$ represent normal and surge periods, respectively. Because the potential market demand (per unit time) is higher in the surge period, we assume $a _ { S } > a _ { N }$ Further, we let the total demand for ride-hailing service in the two periods be a constant, denoted by M, such that

$$
a _ {N} t _ {N} + a _ {S} t _ {S} = M.\tag{2}
$$

## 3.2. Private Drivers’ Decisions

The numbers of platform-owned vehicles and private vehicles on the platform are denoted by $n _ { 1 }$ and $n _ { 2 j , }$ respectively. Under the closed business model, only the platform-owned vehicles provide service to riders; thus, $n _ { 2 j } = 0$ . Under the open business model, the private drivers’ participation decisions depend on the net profit derived per ride. Without loss of generality, we assume that each driver fulfills one ride request per unit of time. In addition to variable service cost (such as fuel cost and wear and tear of a vehicle), private drivers also incur opportunity cost. We use d to denote the private drivers’ opportunity cost per unit order. Deducting the commission, variable service cost, and opportunity cost from revenue, we obtain the private driver’s profit (per unit order) in period j:

$$
\pi_ {D j} = (1 - r) p _ {j} ^ {O} - c - d,\tag{3}
$$

where $r$ is the commission rate charged by the platform and c is the variable service cost per ride.

Because private drivers tend to differ in terms of financial well-being and valuation of time, they likely have heterogeneous opportunity costs. We denote the maximum number of private drivers by $N _ { 2 }$ and assume that their opportunity cost (d) follows a uniform distribution over $[ 0 , { \overline { { d } } } ]$ , where d denotes the maximal opportunity cost. A private driver joins the platform only when $\pi _ { D j } > 0 .$ Because outside options are beyond the scope of ride-sharing industries, a private driver’s opportunity cost is assumed to be identical in the normal and surge periods. Let $\hat { \boldsymbol { d } } _ { j }$ denote the opportunity cost of the marginal driver who is indifferent between joining and not joining the platform in period j. From $\pi _ { D j } > 0$ , we obtain $\hat { d } _ { j } = \hat { ( 1 - r ) } p _ { i } ^ { O } - c .$ Thus, the number of drivers joining the platform in period j is given by

$$
n _ {2 j} = \beta ((1 - r) p _ {j} ^ {O} - c).\tag{4}
$$

Here, $\begin{array} { r } { \beta = \frac { N _ { 2 } } { \overline { { d } } } . } \end{array}$ . Then, the total number of available vehicles on the platform in period j is

$$
N _ {j} ^ {i} = \left\{ \begin{array}{l l} n _ {1}, & i = C \\ n _ {1} + n _ {2 j}, & i = O. \end{array} \right.\tag{5}
$$

## 3.3. Fulfilled Demand and Platform Profit

Under the closed business model, following prior studies on ride-hailing service (e.g., Hu et al. 2022,

Figure 4. Ride-Hailing Platform’s Decision on Business Model  
![](/api/attachments/E4K8NAW6/fulltext/images/48ef3d83f6ec7b853ba36aa95586f5188e246667001e77abefe8cb1a709edd69.jpg)

Zhang et al. 2024), the number of riders being served (per unit time) in period j is

$$
D _ {j} ^ {C} = \min \{n _ {1}, M _ {j} ^ {C} \}.\tag{6}
$$

When serving the riders, the platform-owned vehicles also incur a variable service $\mathrm { c o s t } , { ^ { 3 } }$ denoted by c. Further, when not serving riders, that is, during the idle time, the platform-owned vehicles incur an idle cost of $c \times h$ . The idle cost (per unit time) should be smaller than the service cost because of savings in fuel, vehicle wear and tear, and other factors; hence, $0 < h < 1$ Under the closed business model, only platform-owned vehicles provide services on the platform. The platform’s profit gained per unit time in period j is then formulated as

$$
\pi_ {j} ^ {C} = D _ {j} ^ {C} (p _ {j} ^ {C} - c) - (n _ {1} - D _ {j} ^ {C}) c h.\tag{7}
$$

Note that, for analytical tractability and notational simplicity, here we abstract away the operational details, such as the revenue per rider and the distance per ride. These details can be incorporated into the model by reinterpreting $D _ { j } ^ { C }$ and/or $\overset { \bullet } { p } _ { j } ^ { C }$ and using expected values.

Under the open business model, it is not guaranteed that each private driver receives an order per unit time, especially in the normal period. In the normal period, whether a private driver receives an order depends on the overall supply and demand dynamics on the platform. Technically, the platform can prioritize its own vehicles when assigning orders. However, it may choose not to do so for reasons such as minimizing riders’ wait times or enticing private drivers. Because platformowned vehicles and private vehicles compete for orders in the normal period, negative same-side network effects exist on the supply side. Thus, drawing on model setups from the prior literature $( \mathrm { e . g . }$ , Yoo et al. 2002, Bhargava and Choudhary 2004), we assume that the numbers of orders fulfilled by the platform-owned vehicles $( D _ { 1 N } ^ { O } )$ and that by private vehicles $( D _ { 2 N } ^ { O } )$ in the normal period take the following forms:<sup>4</sup>

$$
\left\{ \begin{array}{l} D _ {1 N} ^ {O} = \min \{n _ {1}, M _ {N} ^ {O} - l n _ {2 N} \}, \\ D _ {2 N} ^ {O} = l n _ {2 N}. \end{array} \right.\tag{8}
$$

where l represents the competitiveness of private drivers, which depends on the private drivers’ ability to compete for orders and the platform’s tendency to assign orders to its own vehicles when both types of vehicles are available. However, in the surge period, we presume that all vehicles are running at full capacity.<sup>5</sup> Therefore, the numbers of orders fulfilled by the platform-owned vehicles $( D _ { 1 S } ^ { O } )$ and that by the private vehicles $( D _ { 2 S } ^ { O } )$ are

$$
\left\{ \begin{array}{l} D _ {1 S} ^ {O} = n _ {1}, \\ D _ {2 S} ^ {O} = n _ {2 S}. \end{array} \right.\tag{9}
$$

The total number of riders being served under the open business model in period j is $\overset { \smile } { D } _ { j } ^ { O } = D _ { 1 j } ^ { O } + D _ { 2 j } ^ { O }$

Under the hybrid open model, the platform profits from charging private drivers commissions and serving the riders with its own vehicles. Under the pure-sharing open model, the platform profits only from charging private drivers commissions. Thus, the platform’s profit gained per unit time in period j under the open business model, either hybrid or pure-sharing, equals

$$
\pi_ {j} ^ {O} = D _ {1 j} ^ {O} (p _ {j} ^ {O} - c) - (n _ {1} - D _ {1 j} ^ {O}) c h + D _ {2 j} ^ {O} p _ {j} ^ {O} r.\tag{10}
$$

Note that, under the pure-sharing open model, $D _ { 1 j } ^ { O } = 0$ With the normal and surge periods both considered, the platform’s total profit under the closed or open business model equals

$$
\Pi^ {i} = \pi_ {N} ^ {i} t _ {N} + \pi_ {S} ^ {i} t _ {S} - k n _ {1}, i \in \{C, O \}.\tag{11}
$$

Here, k is the fixed cost of owning a vehicle that is independent of car usage.<sup>6</sup> Table 1 summarizes the key notations.

## 4. Equilibrium Analysis

In this section, we first derive and analyze the plat form’s optimal service prices (in both periods), optimal number of platform-owned vehicles, and maximal profit under the closed and open business models. Then, we identify two effects resulting from the participation of private drivers.

## 4.1. Equilibrium Solutions

If the platform chooses the closed business model, only the vehicles owned by the platform provide services; thus, $n _ { 2 j } = 0 .$ . In this case, the platform’s optimal service price in period $j ~ ( j \in \{ N , S \} )$ can be obtained by maximizing its profit in this period $( \pi _ { j } ^ { C } )$

$$
\begin{array}{l} \max _ {p _ {j} ^ {C}} \pi_ {j} ^ {C} = D _ {j} ^ {C} (p _ {j} ^ {C} - c) - (n _ {1} - D _ {j} ^ {C}) c h, \\ \text {s.t.} p _ {j} ^ {C} > 0. \end{array}\tag{12}
$$

Solving Problem (12), we obtain the platform’s optimal service price:

$$
p _ {j} ^ {C} (n _ {1}) = \left\{ \begin{array}{l l} \frac {a _ {j} - n _ {1}}{b}, & n _ {1} \leq \frac {a _ {j} - b c (1 - h)}{2}, \\ \frac {a _ {j} + b c (1 - h)}{2 b}, & n _ {1} > \frac {a _ {j} - b c (1 - h)}{2}. \end{array} \right.\tag{13}
$$

After substituting the optimal price in Equation (13) into the platform’s total profit under the closed model (i.e., Equation (11)), the platform’s optimal number of purchased vehicles can be obtained by solving the following problem:

$$
\begin{array}{r l} & {\underset {n _ {1}} {\max} \Pi^ {C} = \pi_ {N} ^ {C} t _ {N} + \pi_ {S} ^ {C} t _ {S} - k n _ {1},} \\ & {\quad \mathrm{s.t.} n _ {1} > 0.} \end{array}\tag{14}
$$

Table 1. Summary of Key Notations

<table><tr><td>Notations</td><td>Descriptions</td></tr><tr><td> $p_{j}^{i}$ </td><td>Service price in period j when platform adopts business model i</td></tr><tr><td> $M_{j}^{i}$ </td><td>Number of requests (per unit time) in period j under model i</td></tr><tr><td> $N_{j}^{i}$ </td><td>Number of servicing vehicles on the platform in period j under model i</td></tr><tr><td> $D_{j}^{i}$ </td><td>Number of riders being served through the platform in period j under model i</td></tr><tr><td>M</td><td>Total potential demand for ride-hailing service in the two periods</td></tr><tr><td> $n_{1}$ </td><td>Number of platform-owned vehicles on the platform</td></tr><tr><td> $n_{2j}$ </td><td>Number of private drivers on the platform in period j</td></tr><tr><td> $N_{2}$ </td><td>Maximum number of private drivers</td></tr><tr><td> $t_{j}$ </td><td>Length of period j</td></tr><tr><td>c</td><td>Variable service cost per ride</td></tr><tr><td>h</td><td>Ratio of the platform&#x27;s idle cost to the service cost</td></tr><tr><td>k</td><td>Fixed cost of owning a vehicle</td></tr><tr><td>d</td><td>Private drivers&#x27; opportunity cost (per unit time), d ∈ [0, d̅]</td></tr><tr><td>l</td><td>Private drivers&#x27; level of competitiveness in the normal period</td></tr><tr><td> $a_{j}$ </td><td>Potential market size in period j</td></tr><tr><td>b</td><td>Coefficient of riders&#x27; price sensitivity</td></tr><tr><td>r</td><td>Commission rate charged by the platform to the private drivers</td></tr></table>

For this problem, the constraint $n _ { 1 } > 0$ requires $k < { \overline { { k } } } ,$ where $\begin{array} { r } { \overline { { k } } = \overline { { \frac { ( a _ { N } - b c ) t _ { N } + ( a _ { S } - b c ) t _ { S } } { b } } } } \end{array}$ . We find that a threshold $\begin{array} { r } { k _ { 1 } = \frac { ( a _ { S } - a _ { N } ) t _ { S } } { b } - h c ( t _ { N } + t _ { S } ) } \end{array}$ divides the feasible region $( 0 , { \overline { { k } } } )$ into two intervals, and the optimal solution to Problem (14) takes different forms depending on into which interval k falls. For ease of comparison, we summarize the solution, consisting of the optimal number of platform-owned vehicles, service prices, demands, and profits, in Table 2.

In the case that the open business model is adopted, some private drivers join the platform and provide ride-hailing services to riders. The platform maximizes its profit, $\breve { \Pi } ^ { O } .$ , by choosing its optimal service prices in the normal and surge periods and the optimal number of purchased vehicles. We next derive the platform’s profit-maximizing service price in period j:

$$
\begin{array}{l} \max _ {p _ {j} ^ {O}} \pi_ {j} ^ {O} = D _ {1 j} ^ {O} (p _ {j} ^ {O} - c) - (n _ {1} - D _ {1 j} ^ {O}) c h + D _ {2 j} ^ {O} p _ {j} ^ {O} r, \\ \text {s.t.} p _ {j} ^ {O} > 0. \end{array}\tag{15}
$$

Solving Problem (15), we obtain the optimal service price of the open platform in period $j ^ { \mathrm { ~ ~ } } ( p _ { j } ^ { O } ( n _ { 1 } ) )$ . The open platform maximizes its profit, $\Pi ^ { O }$ by deciding the optimal number of platform-owned vehicles:

Table 2. Optimal Solutions Under the Closed Business Model

<table><tr><td>Variables</td><td colspan="2">Optimal solutions</td></tr><tr><td>Number of purchased vehicles</td><td colspan="2"> $n_{1}^{C*} = \begin{cases} \dfrac{(a_S - bc)t_S - b(k + cht_N)}{2t_S}, & 0 < k < k_1, \\ \dfrac{(a_N t_N + a_S t_S) - b(k + c(t_N + t_S))}{2(t_N + t_S)}, & k_1 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Price</td><td> $p_{N}^{C*} = \begin{cases} \dfrac{bc(1 - h) + a_N}{2b}, & 0 < k < k_1, \\ \dfrac{a_N}{b} - \dfrac{(a_N t_N + a_S t_S) - b(k + c(t_N + t_S))}{2b(t_N + t_S)}, & k_1 \leq k < \overline{k}. \end{cases}$ </td><td> $p_{S}^{C*} = \begin{cases} \dfrac{a_S}{b} - \dfrac{a_S t_S - b(k + c(ht_N + t_S))}{2bt_S}, & 0 < k < k_1, \\ \dfrac{a_S}{b} - \dfrac{(a_N t_N + a_S t_S) - b(k + c(t_N + t_S))}{2b(t_N + t_S)}, & k_1 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Demand</td><td> $D_{N}^{C*} = \begin{cases} \dfrac{a_N - bc(1 - h)}{2}, & 0 < k < k_1, \\ \dfrac{(a_N t_N + a_S t_S) - b(k + c(t_N + t_S))}{2(t_N + t_S)}, & k_1 \leq k < \overline{k}. \end{cases}$ </td><td> $D_{S}^{C*} = \begin{cases} \dfrac{a_S t_S - b(k + c(ht_N + t_S))}{2t_S}, & 0 < k < k_1, \\ \dfrac{(a_N t_N + a_S t_S) - b(k + c(t_N + t_S))}{2(t_N + t_S)}, & k_1 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Profit</td><td colspan="2"> $\Pi^{C*} = \begin{cases} \dfrac{((a_S - bc(1 - h))t_S - b(k + hc(t_N + t_S)))^2}{4bt_S} + \dfrac{(a_N - bc(1 - h))^2t_N}{4b}, & 0 < k < k_1, \\ \dfrac{((a_N - bc(1 - h))t_N + (a_S - bc(1 - h))t_S - b(k + hc(t_N + t_S)))^2}{4b(t_N + t_S)}, & k_1 \leq k < \overline{k}. \end{cases}$ </td></tr></table>

intervals by<sup>7</sup>

$$
\begin{array}{l} \max _ {n _ {1}} \Pi^ {O} = \pi_ {N} ^ {O} t _ {N} + \pi_ {S} ^ {O} t _ {S} - k n _ {1}, \\ \text {s.t.} n _ {1} \geq 0. \end{array}\tag{16}
$$

From the first order condition, we derive the optimal solutions as summarized in Table 3. Note that, here, the feasible region (0, k) for k is divided into three

$$
\begin{array}{l} k _ {2} = \frac {t _ {S} G _ {S}}{B _ {S}} \left(\frac {a _ {S} A _ {S} - c (b E _ {S} - h B _ {S})}{G _ {S}} - \frac {a _ {N} A _ {N} - c (b E _ {N} - h B _ {N})}{G _ {N}}\right) \\ \quad - c h (t _ {N} + t _ {S}) \text {and} k _ {3} = \sum_ {j \in \{N, S \}} \frac {(a _ {j} A _ {j} - b c E _ {j}) t _ {j}}{B _ {j}}. \end{array}
$$

From the optimal number of platform-owned vehi cles shown in Table 3, we can conclude that the platform should adopt the pure-sharing open model rather than the hybrid open model when the fixed cost of owing vehicles (k) is higher than a threshold $\left( k _ { 3 } \right)$

Table 3. Optimal Solutions Under the Open Business Model

<table><tr><td>Variables</td><td colspan="2">Solutions</td></tr><tr><td>Number of platform-owned vehicles</td><td colspan="2"> $n_{1}^{O*} = \begin{cases} \dfrac{(a_S A_S - bc E_S)t_S - (k + cht_N)B_S}{2G_S t_S}, & 0 < k < k_2, \\ \dfrac{\left(\sum_{j \in \{N,S\}}((a_j A_j - bc E_j)t_j/B_j)\right) - k}{2\left(\sum_{j \in \{N,S\}}(G_j t_j/B_j)\right)}, & k_2 \leq k < k_3, \\ 0, & k_3 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Price (N)</td><td colspan="2"> $p_{N}^{O*} = \begin{cases} \dfrac{c(b(1-h) + l\beta(1-r)(2-h)) + a_N}{2(b + l\beta(1-r)^2)}, & 0 < k < k_2, \\ \dfrac{cl\beta + a_N}{b + l\beta(1-r)} - \dfrac{\left(\sum_{j \in \{N,S\}}((a_j A_j - bc E_j)t_j/B_j)\right) - k}{2(b + l\beta(1-r))\left(\sum_{j \in \{N,S\}}(G_j t_j/B_j)\right)}, & k_2 \leq k < k_3, \\ \dfrac{a_N + cl\beta}{b + l\beta(1-r)}, & k_3 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Price (S)</td><td colspan="2"> $p_{S}^{O*} = \begin{cases} \dfrac{c\beta + a_S}{b + \beta(1-r)} - \dfrac{(a_S A_S - bc E_S)t_S - (k + cht_N)B_S}{2(b + \beta(1-r))G_S t_S}, & 0 < k < k_2, \\ \dfrac{c\beta + a_S}{b + \beta(1-r)} - \dfrac{\left(\sum_{j \in \{N,S\}}((a_j A_j - bc E_j)t_j/B_j)\right) - k}{2(b + \beta(1-r))\left(\sum_{j \in \{N,S\}}(G_j t_j/B_j)\right)}, & k_2 \leq k < k_3, \\ \dfrac{a_S + c\beta}{b + \beta(1-r)}, & k_3 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Private drivers</td><td colspan="2"> $n_{2j}^* = \beta((1-r)p_{j}^{O*} - c), j \in \{N, S\}.$ </td></tr><tr><td>Demand (N)</td><td colspan="2"> $D_{N}^{O*} = \begin{cases} a_N - b\left(\dfrac{c(b(1-h) + l\beta(1-r)(2-h)) + a_N}{2(b + l\beta(1-r)^2)}\right), & 0 < k < k_2, \\ \dfrac{l\beta(1-r)(l\beta c + a_N)}{b + l\beta(1-r)} + \dfrac{b\left(\left(\sum_{j \in \{N,S\}}((a_j A_j - bc E_j)t_j/B_j)\right) - k\right)}{(b + l\beta(1-r))\left(\sum_{j \in \{N,S\}}(G_j t_j/B_j)\right)} - l_{N}\beta c, & k_2 \leq k < k_3, \\ \dfrac{l\beta((1-r)a_N - bc)}{b + l\beta(1-r)}, & k_3 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Demand (S)</td><td colspan="2"> $D_{S}^{O*} = \begin{cases} \dfrac{\beta(1-r)(c\beta + a_S)}{b + \beta(1-r)} + \dfrac{b((a_S A_S - bc E_S)t_S - (k + cht_N)B_S)}{2(b + \beta(1-r))G_S t_S} - \beta c, & 0 < k < k_2, \\ \dfrac{\beta(1-r)(c\beta + a_S)}{b + \beta(1-r)} + \dfrac{b\left(\left(\sum_{j \in \{N,S\}}((a_j A_j - bc E_j)t_N/B_j)\right) - k\right)}{(b + \beta(1-r))\left(\sum_{j \in \{N,S\}}(G_j t_j/B_j)\right)} - l_{S}\beta c, & k_2 \leq k < k_3, \\ \dfrac{\beta((1-r)a_S - bc)}{b + \beta(1-r)}, & k_3 \leq k < \overline{k}. \end{cases}$ </td></tr><tr><td>Profit</td><td colspan="2"> $\Pi^{O*} = \sum_{j \in \{N, S\}}((n_{2j}^*p_{j}^{O*}r + (D_{j}^{O*} - n_{2j}^*)(p_{j}^{O*} - c) - ch(n_1 - (D_{j}^{O*} - n_{2j}^ {*})))t_j) - kn_1^{O*}.$ </td></tr></table>

Given a fixed total market size (M), a larger $a _ { S }$ or, equivalently, a smaller $a _ { N }$ indicates more riders requesting service in the surge period; that is, the demand surge is steeper. Then, by analyzing the impact of the demand surge on the number of platform-owned vehicles under the closed and open business models, we find that, under the open business model, the platform should purchase fewer vehicles to cope with the increased demand surge when the fixed cost is relatively high $( \frac { \partial n _ { 1 } ^ { O * } } { \partial a _ { S } } < 0$ when $k _ { 2 } \leq k < k _ { 3 } )$ . The reason for this counterintuitive finding is as follows. With a steeper demand surge, each platform-owned vehicle, although it generates a higher profit (per ride) to the platform in the surge period, has a lower profitability in the normal period because of competition from private vehicles $( \frac { \hat { \partial } p _ { S } ^ { O * } } { \partial a _ { S } } > 0$ and $\frac { \partial p _ { N } ^ { O * } } { \partial a _ { S } } < 0 )$ . Further, the private drivers on the open platform can ease the supply shortage in the surge period. Hence, when the platform is open and the fixed cost is relatively high, it benefits from reducing its own service capacity as the demand surge becomes higher.

## 4.2. Supply-Augmenting Effect and Price Discrimination–Hindering Effect

After exploring the equilibrium solutions under the two business models, we identify two effects resulting from the participation of private drivers: the supplyaugmenting effect and price discrimination–hindering effect.

4.2.1. Supply-Augmenting Effect. First, we compare the number of platform-owned vehicles and total number of available vehicles under the two business models. We denote the difference between the numbers of platform-owned vehicles under the closed and open business models by $\Delta n _ { 1 } = n _ { 1 } ^ { C * } - n _ { 1 } ^ { O * }$ and derive Proposition 1. Because of its complexity, the threshold condition (c˜) used in this proposition is given in Online Appendix A.3.

Proposition 1. The open business model generates a supply-augmenting effect in the surge period, whereas such an effect may or may not exist in the normal period. Especially,

a. The platform owns fewer vehicles under the open business model than under the closed business model, that is, $\Delta n _ { 1 } > 0$

b. In the surge period, the platform’s total service capacity under the open business model is always higher than that under the closed business model.

c. In the normal period, if the variable service cost is sufficiently high, that is, $c > { \tilde { c } } ,$ , the total number of vehicles on the open platform is smaller than that on the closed platform;

otherwise, the total number of vehicles on the open platform is larger than that on the closed platform.

Proposition 1(a) indicates that the platform can purchase fewer vehicles by opening up to private drivers. Because private drivers augment the supply on the platform, it is not surprising that the platform would purchase fewer vehicles. For ride-hailing platforms, the open business model reduces the financial pres sure of an asset-heavy operation.

Proposition 1(b) reveals that the platform’s total service capacity under the open business model is always higher than that under the closed business model in the surge period. The reasoning behind this finding is as follows. The ride-hailing market faces a supply shortage in the surge period. In this case, although the optimal number of platform-owned vehicles decreases after opening the platform (as revealed in Proposition 1(a)), plenty of private vehicles join the platform, leading to the total service capacity under the open business model being higher than that under the closed business model. In other words, adopting the open business model can alleviate the difficulty of getting a taxi in rush hours. Taken jointly, Proposition 1, (a) and (b), suggests that private vehicles joining the platform not only reduce the number of vehicles purchased by the platform but also improves the platform’s total service capacity in the surge period. Therefore, the adoption of the open business model generates a supply-augmenting effect, effectively mitigating the scarcity of supply on the ride-hailing platform in the surge period and benefiting riders.

On the other hand, as stated in Proposition 1(c) and illustrated in Figure 5, in the normal period, when the variable service cost is high, the total number of vehicles on the open platform may be lower than that on the closed platform. That is, the supply-augmenting effect vanishes in the normal period. The reason behind this counterintuitive finding is as follows. In the surge period, there is a large number of ride requests. Hence, when the platform is closed to private vehicles, it must purchase a sufficiently large number of vehicles to ensure adequate service capacity in the surge period even though a portion of vehicles might become idle in the normal period. In contrast, when the open business model is adopted, because part of the demand during the surge period can be met by private vehicles, the platform can purchase significantly fewer vehicles. Furthermore, under a closed business model, all vehicles available during the surge period are also available during the normal period, whereas under the open model, private drivers can opt out during the (low demand) normal period. These two differences, coupled with the fact that, as the variable service cost becomes higher, the number of private vehicles decreases in the normal period $( \frac { \partial n _ { 2 N } ^ { * } } { \partial c } < 0 )$ , lead to the interesting result that the number of available vehicles on the platform in the normal period is lower under the open business model when the variable service cost is sufficiently high.

Figure 5. (Color online) Comparison of Service Capacity in the Normal Period  
![](/api/attachments/E4K8NAW6/fulltext/images/3e0ed03e0889f9a32fe8b02cc6e9aee22015bd02e60ab623074bedf98afb966c.jpg)  
Note. M � 1, a � 1:3, t � 0:3, t � 0:7, b � 0:9, β � 1, h � 0:1, r � 0:1.

Based on prior literature (e.g., Chen and Sheldon 2016), total service capacity in the surge period is a key metric of the overall efficiency of the ride-hailing platform. Therefore, from the perspective of alleviating the traffic pressure during rush hours, the open business model can improve overall efficiency. From the platform owner’s perspective, it is imperative to ensure consistently high service efficiency whether during the normal or surge period. A less-than-adequate service capacity not only fosters negative impressions among consumers but also disrupts their consumption habits. From a city manager’s perspective, although transit accessibility in the peak hours is a critical metric of city evaluation, ride-hailing service can lead to reductions in the utilization of public transit services as empirically revealed in the prior literature (Babar and Burtch 2020). Thus, in terms of improving the transit accessibility in the peak hours, the open platform model is more efficient. However, from the viewpoint of improving the utilization of public transportation in the normal period, a city manager may prefer that ride-hailing platforms maintain a low service capacity. Therefore, the most ideal outcome for the city manager is that the ride-hailing platform provides high service capacity in the surge period and low service capacity in the normal period, thereby balancing the overall utilization rate of public transportation and transit accessibility in the peak hours. As revealed in Proposition 1, this ideal outcome is achieved under the open business model when the service cost is sufficiently high. Proposition 1 offers practical guidelines for city managers to reorganize public transportation systems as ridehailing platforms transition from a closed to an open model.

4.2.2. Price Discrimination–Hindering Effect. Of particular interest to this study is the practice of surge pricing, which is frequently adopted by ride-hailing platforms. However, this practice is not without controversy as complaints and public criticism about this pricing mechanism are rising (Dholakia 2015). Fortunately, our analytical findings show that this issue can be alleviated by the adoption of the open business model.

Proposition 2. Opening the platform to private drivers always reduces the price gap between the normal and surge periods.

As stated in this proposition, the price gap between the surge and normal periods under the open business model is always smaller than that under the closed business model. This finding indicates that the open business model has a price discrimination–hindering effect. This effect has important practical implications. Note that surge pricing was originally proposed to address the mismatch between supply and demand in the surge period. With a significant increase in demand, the service price in the surge period can be significantly higher than that in the normal period. By adopting the open business model, the participation of private drivers can supplement the supply, mitigating the demand and supply mismatch and simultaneously reducing the price surge in the surge period, which represents another benefit to consumers.

From Proposition 2, we now understand that there is an additional benefit when adopting an open business model: it allows the platform to set a relatively low service price in the surge period, thus reducing the magnitude of price surge. This is especially helpful in addressing public complaints about surge pricing. Surge pricing has been criticized by the public as high-tech gouging (Lowrey 2014). Consumers’ complaints mainly originate from the price gap between the normal and surge periods; that is, the lower regular price makes the surge price seem exorbitant (Dholakia and Brown 2016). On the supply side, when facing the mechanism of surge pricing, private drivers are reported as colluding to trig ger surge prices (Hamilton 2019). In this regard, the hybrid open model considered in this study is also better than the pure-sharing model used by Uber because the platform can serve the riders with its own vehicles, thus making it hard for private drivers to engage in pricing collusion. However, from the perspective of profit maximization, the price discrimination–hindering effect may negatively impact the platform, which is further discussed in the next section.

Furthermore, we analyze the impact of demand surge on the open business model’s price discrimination–hindering effect and derive Corollary 1.

Corollary 1. When the demand surge is low or high $( a _ { S } \leq a _ { S 1 } o r a _ { S } > a _ { S 2 } ) .$ , the open business model becomes more effective in reducing the price gap as the demand surge increases. When the demand surge is moderate $( a _ { S 1 } < a _ { S }$ $\leq a _ { S 2 } )$ , if the rider’s price sensitivity is low $( b \leq \hat { b } )$ , the open business model’s role in reducing the price gap increases as the demand surge increases; however, if the rider’s price sensitivity is high $( b > \hat { b } )$ , the open business model’s role in reducing the price gap decreases with the magnitude of the demand surge.

As stated in Corollary 1, when the demand surge increases, the price discrimination–hindering effect becomes more pronounced unless the demand surge is moderate $( { a } _ { S 1 } < { a } _ { S } \le { a } _ { S 2 } )$ and the rider’s price sensitivity is high $( b > \hat { b } )$ . The reasoning behind this finding is as follows. The platform’s price discrimination capability primarily depends on two key factors: the riders willingness to pay a high service price in the surge period and the platform’s incentive to charge a high service price in the surge period. As the demand surge increases, the riders’ willingness to pay more in the surge period increases at the same rate under the two business models; however, the platform’s incentive to charge a high price evolves differently because the platform’s pricing decision under the open business model is intertwined with the private drivers’ participation decisions. Specifically, when the magnitude of demand surge is either low or high, the riders are either evenly distributed in the two periods or highly concentrated in the surge period,<sup>8</sup> indicating a relatively low demand fluctuation in the market; thus, the platform’s reliance on leveraging the supply-augmenting effect of private vehicles becomes minimal. Participation of private drivers splits a large portion of revenues from the platform-owned vehicles, and the participation decisions of the private drivers are mainly determined by the service price. Consequently, in comparison with the closed platform, to suppress the participation of private vehicles, the open platform is less incentivized to set a higher service price. As the demand surge intensifies, the closed platform has the incentive to impose a significantly higher price in the surge period, but the open platform’s pricing decision is greatly restricted by the competition resulting from the private drivers. Therefore, in this case, the price discrimination–hindering effect of the open business model is enhanced as the demand surge increases.

In the case of a moderate demand surge, according to the optimal solutions in Table $3 , ^ { 9 }$ as the demand surge increases, the number of platform-owned vehicles under the closed platform increases, whereas that of the open platform decreases. In this scenario, for the platform adopting the open business model, as the demand surge increases, the reduced number of platform-owned vehicles incentivizes the platform to set a significantly higher price in the surge period to leverage the supplyaugmenting effect, indicating an enhancement in its lowlevel price-discrimination capability. In contrast, for the platform operating under the closed business model, its high-level price-discrimination capability is hindered by the high price sensitivity of riders. Therefore, when the demand surge is moderate and the rider’s price sensitivity is high, the price discrimination–hindering effect resulting from the open business model diminishes as the demand surge increases.

## 5. Open Business Model vs. Closed Business Model

In this section, we first compare the equilibrium solutions associated with the closed and open business models and then derive the conditions under which the open business model outperforms the closed one for the ride-hailing platform.

## 5.1. Comparison of Idle Vehicles

The number of a platform’s idle vehicles serves as a crucial indicator of the overarching efficiency of the business model. Thus, we examine the conditions under which idle vehicles exist in the market and compare both the probability of existence and the number of idle vehicles under the two business models. The key findings are summarized in Lemma 1 and Proposition 3.

Lemma 1. Under both the closed and open business models, no vehicle is idle in the surge period; in the normal period, a portion of the platform-owned vehicles is idle if the fixed cost is low $( k < k _ { 1 }$ under the closed business model and $k < k _ { 2 }$ under the open business model). Further, the number of idle vehicles, if it exists, increases with the magnitude of the demand surge.

Lemma 1 reveals that, when the fixed cost is rela tively low, it is optimal for the platform to acquire some excess capacity—relative to the demand in the normal period—to meet the high demand in the surge period. Outside the surge period, however, a proportion of the platform-owned vehicles sit idle, indicating a waste of precious resources. Moreover, analytical results and Figure 6 show that, as the surge in demand from the normal period to the surge period increases, the number of idle vehicles also increases, further deteriorating the efficiency of the platform-owned vehicles. These findings hold under both closed and open business models.

Proposition 3. Compared with the closed business model, idle vehicles are less likely to exist and the number of idle vehicles is smaller when the platform adopts the open business model.

Compared with the closed business model, under the open business model, the platform purchases fewer vehicles (as shown in Proposition 1(a)) and the private drivers split a portion of orders. Whether opening the platform to private drivers leads to more idle vehicles or not hinges on two factors: the extent to which platform-owned vehicles are reduced and the intensity of market competition that ensues. It is worth noting that Proposition 3 and Figure 6 reveal that the number of idle vehicles under an open business model is strictly lower than that under a closed business model regardless of the fixed cost of platform-owned vehicles. By appropriately adjusting the service prices and the number of purchased vehicles, the platform could minimize the number of idle vehicles in the normal period even when the private drivers have the highest level of competitiveness $( \mathrm { i } . \mathrm { e } . , l = 1 )$ . This finding confirms that opening the platform to private drivers could help the platform reduce the downtime of its own vehicles, implying more efficient utilization of its vehicle resources. Essentially, what makes the difference under the open platform is that private vehicles can provide a flexible supply to riders, helping the platform meet the increased demand during the surge period. Consequently, the platform does not need to purchase an excessive number of vehicles to cope with the demand surge.

Figure 6. Number of Idle Vehicles Under Different Business Models  
![](/api/attachments/E4K8NAW6/fulltext/images/a86014a3aca78417efa4483e11562a2e711836bcb66583d32984dd77e4591dfe.jpg)  
Note. M � 1, t � 0:3, t � 0:7, b � 0:6, β � 0:8, l � 0:9, c � 0:1, k � 0:05, $h = 0 . 1 , r = 0 . 1$

It is well-known that the sharing platforms are facilitating improved use of underutilized assets owned by individuals. Proposition 3 reveals an insightful finding that, by embracing the open business model, a closed platform can also increase the usage rate of its own assets, leading to a win–win situation for all participants. Established firms are often reluctant to make drastic changes to business models because of path dependence, inertia to change, or low tolerance to risks. The findings in Lemma 1 and Proposition 3 provide strong support for the call that “companies must learn to overcome incumbent inertia and engage with the innovative models that the sharing economy has introduced to the world” (Enders et al. 2016).

5.2. Comparison of Service Prices and Demand We compare the equilibrium price and demand for the ride-hailing service under different business models. The findings are summarized in Proposition $^ { 4 , }$ and the threshold condition (cˇ) used in this proposition is provided in Online Appendix A.8.

Proposition 4. The equilibrium price and demand for the ride-hailing service always move in different directions afte adopting the open business model:

a. In the surge period, the optimal price (demand) of th open platform is always lower (higher) than that of the closed platform, that is, $p _ { S } ^ { O * } < p _ { S } ^ { C * }$ and $\tilde { D _ { S } ^ { O * } } > \tilde { D _ { S } ^ { C * } }$

b. In the normal period, if and only if both the fixed cost and variable service cost are relatively high $( k \geq k _ { 2 }$ and $c > { \check { c } } )$ the optimal price (demand) of the open platform is higher (lower) than that of the closed platform, that is, $p _ { N } ^ { O * } > p _ { N } ^ { C * }$ <sup>∗</sup> and $D _ { N } ^ { O * } < D _ { N } ^ { C * } ;$ otherwise, the optimal price (demand) of the open platform is lower (higher) than that of the closed platform.

Private vehicles can augment the ride-hailing supply, encouraging the open platform to reduce the service price to attract more riders. Hence, the optimal price (demand) under the open business model is always lower (higher) than that under the closed business model in the surge period, as shown in Proposition 4(a). Similar to the existence of the exceptional scenario described in Proposition 1(c) and Figure $5 ,$ it is interesting to note that the equilibrium service price (demand) in the normal period can be higher (lower) under the open business model than under the closed business model.

Whereas the impact of a higher variable cost is intuitive, the impact of a higher fixed cost on the equilibrium outcomes under the open and closed business models in the normal period is more complicated. An increase in fixed cost has no impact on the private drivers’ willingness to join the platform but significantly diminishes the platform’s incentive to purchase vehicles under the closed business model. Thus, one may expect that a higher fixed cost yields a larger reduction in the number of fulfilled orders during the normal period to the closed platform in comparison with the open platform. Nevertheless, Proposition 4(b) indicates that, during the normal period, a sufficiently high fixed cost $( k \geq k _ { 2 } )$ could surprisingly give the closed platform the advantage in fulfilled orders. More specifically, as depicted in Figure 7, under a relatively low fixed cost $( k _ { 2 } \leq k < k _ { 3 } )$ , an increase in it promotes the occurrence of the exceptional scenario $( \grave { p } _ { N } ^ { O * } > p _ { N } ^ { C * }$ and $D _ { N } ^ { O * } < D _ { N } ^ { C * } )$ The reason behind this counterintuitive finding is that, as suggested by the equilibrium solutions shown in Tables 2 and $^ { 3 , }$ the optimal number of platform-owned vehicles decreases at a faster rate under the open business model than under the closed one when the fixed cost falls within the region of $( 0 , k _ { 3 } ) .$ , i.e., $\frac { \partial n _ { 1 } ^ { O * } } { \partial k } < \frac { \partial n _ { 1 } ^ { C * } } { \partial k } < 0 .$ Therefore, when the fixed cost is relatively large, the open platform is compelled to set a higher price during the normal period, compared with the closed platform, to attract private drivers, but a higher price suppresses the number of riders’ requests. Moreover, as the fixed cost reaches a sufficiently high level $( k \geq k _ { 3 } ) .$ , a further increase in it discourages the occurrence of this exceptional scenario. The number of platform-owned vehicles reduces to zero under the open business model in this high fixed-cost region $( k \geq k _ { 3 } ) ;$ therefore, the change in fixed cost does not affect the pricing decision of the open platform, reducing the likelihood of occurrence of the exceptional scenario.

Figure 7. (Color online) Comparison of the Optimal Service Price and Demand in the Normal Period  
![](/api/attachments/E4K8NAW6/fulltext/images/581e5f0e89af989f7ad1536f7b8e2c50015ffb0351cb3388c4ac9fb86ebbe594.jpg)  
Note. M � 1, a � 1:3, t � 0:3, t � 0:7, b � 0:8, β � 1, l � 0:9, h � 0:1, $r = 0 . 1 \AA$

## 5.3. Comparison of Profit and Social Welfare

The platform’s choice of business model ultimately depends on its net profit. Theoretically, the puresharing open model is a special case of the hybrid open model; thus, we focus on comparing the platform’s net profits derived under the closed business model and the hybrid open model and analyze the impact of the demand surge on the platform’s decision.

Proposition 5. The open business model is not always more profitable for the platform, and the impact of the magnitude of demand surge on the profit gap between the open and closed business models $( \Pi ^ { O * } - \Pi ^ { \check { C } * } )$ is nonmonotonic.

Our analyses so far show that the open business model benefits private drivers with the opportunity to earn more revenue, benefits the riders with more supply of services and a lower price in the surge period, and leads to more efficient utilization of vehicle resources in the normal period, which has environmental and sustainability implications. Interestingly, Proposition 5 reveals that the open business model does not always lead to more profit for the platform.

This finding is somewhat counterintuitive because, whereas the passive participants always benefit from the open business model, the party that makes the decision on the business model may or may not benefit from it. As we elaborate later, this finding has implica tions for policymakers.

Corollary 2 follows immediately from Proposition 5 and uncovers how the magnitude of demand surge impacts the profit gap between the two business models. The result uses the following threshold value:

$$
\begin{array}{l} \overline {{M}} = \frac {k (t _ {N} + t _ {S}) (b ^ {2} (1 + 2 r) + b \beta (1 - r) (l + 1) + l \beta^ {2} (1 - 2 r) (1 - r) ^ {2})}{((b (1 - 2 r) + \beta (1 - r)) t _ {N} + (b (1 - 2 r) + l \beta (1 - r)) t _ {S})} \\ \qquad + \frac {b c (1 + r) (t _ {N} + t _ {S})}{(1 - r)}. \end{array}
$$

Corollary 2. As the magnitude of demand surge (a<sub>S</sub>) increases,

a. When the total market size in the two periods is small $( M \leq { \overline { { M } } } )$ , the profit gap $( \Pi ^ { O * } - \Pi ^ { C * } )$ first increases and then decreases.

b. When the total market size in the two periods is large $( M > \overline { { M } } )$ , the profit gap $( \Pi ^ { O * } - \Pi ^ { C * } )$ first decreases, then increases, and subsequently decreases again.

Proposition 5 and Corollary 2 describe how the magnitude of the demand surge affects the profit gap between the two business models. Figure 8 further illustrates the platform’s optimal business model under different values of $a _ { S } .$ . Whereas it is intuitive that a high fixed or variable cost incentivizes the platform to adopt the open business model, what is intriguing is the nonmonotonic impact of the magnitude of demand surge.

When choosing between open or closed business models, one may naturally expect that, under a higher demand surge, the platform is always more willing to open up to private drivers to mitigate the supply shortage in the surge period. Therefore, the nonmonotonic patterns are rather counterintuitive. The reasons behind the intriguing findings are as follows. As illustrated by Figure 9, a higher demand surge incentivizes the platform to purchase more vehicles and attract more private drivers to participate in the surge period (demand curve shifting upward). Under the open business model, the price elasticity of supply resulting from the participation of private drivers ensures a relatively larger increase in supply than that under the closed model; that is, the supply-augmenting effect of the open business model contributes to a larger increase in total revenue generated on the platform. Meanwhile, the increase in price under the closed business model is likely larger than that under the open business model because of the price discrimination–hindering effect resulting from the adoption of the open business model. Overall, the two driving forces, the supply-augmenting effect and pricing discrimination–hindering effect, jointly determine the optimality of the open business model under different levels of demand surge. The ride-hailing platform should strategically choose its optimal business model based on these two effects.

Figure 8. Optimal Business Model Under Different Values of $a _ { S }$ and k  
![](/api/attachments/E4K8NAW6/fulltext/images/fe9c9688c7200ae0e3ed073927c04d4a5cd759343301c6ab384c5cf1f555b48d.jpg)

![](/api/attachments/E4K8NAW6/fulltext/images/39d850684a7eb8a0fdf24e1a804608d0845244d007304746cb8f1c7bebd18625.jpg)  
Note. t � 0:3, t � 0:7, b � 0:25, β � 1:5, l � 0:2, c � 0:2, h � 0:1, r � 0:2.

Specifically, when the demand surge is moderate, because the demand fluctuation is high, the platform is incentivized to adopt the open business model to leverage the flexibility and cost-efficiency of private vehicles. Consequently, the supply-augmenting effect resulting from the open business model becomes the dominate driving force. Thus, the platform is more willing to adopt the open business model in this moderate-demand surge region compared with the low- or high-demand surge region. When the demand surge is high, because most of the riders congregate in the surge period, the demand fluctuation is actually low, lowering the platform’s incentive to harness the supply-augmenting effect resulting from the open business model. Furthermore, as revealed in Corollary 1(a), an increase in demand surge could increase the closed platform’s capability to implement price discrimination. Therefore, the closed business model is more likely to be adopted as the demand surge increases in this high-value region.

However, when the demand surge falls in a lowvalue interval, even though the demand fluctuation remains modest because of a relatively uniform distribution of riders, the impact of increased demand surge on the superiority of the open business model becomes contingent upon the total potential demand size. Specifically, in this low-demand surge region, compared with the closed business model, the platform’s incentive to adopt the open business model decreases (increases) as the demand surge increases when the total potential demand is high (low). In this case, a higher demand surge incentivizes the platform to adopt the open business model to leverage the supply-augmenting effect. However, it is worth noting that the open business model also reduces the platform’s ability to implement a high level of price discrimination (as suggested by Corollary 1(a)), and such a price discrimination–hindering effect is more pronounced when the potential demand is high. Therefore, as the demand surge increases, the price discrimination–hindering effect dominates in a market with high potential demand, and the open business model becomes less preferred by the platform. Conversely, in a market with low potential demand, the price discrimination–hindering effect is less significant, and the open model is more likely to surpass the closed one as the demand surge increases because the supply-augmenting effect dominates.

Figure 9. (Color online) Impact of Demand Surge (a ) on the Total Revenue Generated on the Platform  
(a)  
![](/api/attachments/E4K8NAW6/fulltext/images/8341f74ceb4d1e8a0541e472386f92c00140378ea216b11cb2f6d5aa95e7a0f1.jpg)  
Notes. (a) Closed platform. (b) Open platform.

(b)  
![](/api/attachments/E4K8NAW6/fulltext/images/574f9796cbd496d31f74ef43418bae3cd95449ec86bf5b4af37b4d0a53b13220.jpg)

To explore the overall efficiency of the open business model, we also numerically derive and compare the social welfare within the ride-hailing system under the two business models. The social welfare is composed of the platform’s profit (Equation (11)), the riders’ total consumer surplus (derived from Equation (1)), and the private drivers’ net profits (derived from Equation (3)). As shown in Figure 10, our numerical results reveal that adopting the open business model always yields a higher social welfare. Therefore, from the perspective of social welfare, opening up the ridehailing platform is always desirable.

Considering all findings, we can conclude that, with the possible exception of the platform, the open business model benefits all parties and the society as a whole. More specifically, the open business model leads to more service supply and a lower service price in the surge period, thus benefiting riders; reduces the number of idle vehicles in the normal period, thus resulting in more efficient utilization of vehicle resources; and helps private drivers earn extra revenue—three effects jointly leading to a higher social welfare—although, interestingly, the open business model may not always generate more profit to the platform. Because the open business model may be beneficial to everyone except the platform that actually decides whether it should be adopted, policymakers should provide incentives, such as tax subsidies, to ensure that the open business model is more profitable for the platform as well.

Figure 10. Social Welfare Comparison  
![](/api/attachments/E4K8NAW6/fulltext/images/e49fae9d8fd7922cfc35dce6e95b51115b4f598b69729ed2db9270bb9ed809db.jpg)  
Note. M � 1, a � 1:5, t � 0:3, t � 0:7, b � 0:25, β � 1:5, c � 0:2, $h = 0 . 1 , r = 0 . 2 .$

## 6. Extensions

We develop several extension models to examine the robustness of our main findings after relaxing several important assumptions. First, we extend the main model to examine the platform’s optimal business model by considering strategic rider behavior. Second, we build a recursive model for a competitive market, capturing direct competition between private and platform-owned vehicles using a likelihood-based order assignment function. Further details about these two extension models are provided in Online Appendix B. Additionally, we also explore the following important cases. First, the case with an endogenized commission rate is explored. In this case, the platform decides the number of purchased vehicles and the commission rate simultaneously. Because endogenizing the commission rate makes the model analytically intractable, numerical experiments are conducted to analyze the property of the optima commission rate and the robustness of the main findings. Second, the case with asymmetric price sensitivities in the two periods is examined. We assume that the rider’s price sensitivity in the normal period, denoted by $b _ { N } ,$ , is larger than that in the surge period, denoted by $b _ { S } ;$ that is, $b _ { S } < b _ { N }$ . And the demand function is reformulated as $M _ { j } ^ { i } = a _ { j } - b _ { j } p _ { j } ^ { i } , i \in \{ C , O \} , j \in \{ N , S \}$ . Finally, asymmetric service costs are taken into account. Specifically, we consider the variable service costs of platform-owned vehicles in the normal and surge periods as $^ { \prime \prime } c ^ { \prime \prime }$ and $^ { \prime \prime } c + \Delta c , ^ { \prime \prime }$ respectively. Additionally, for private vehicles, the variable service costs in the two periods are expressed as $^ { \prime \prime } \lambda \times c ^ { \prime \prime } \mathrm { a n d } ^ { \prime \prime } \lambda \times ( c + \Delta c ) . ^ { \prime }$

These extension models analytically or numerically verify that the main findings of this study are still valid. In particular, the results prove that accepting private drivers could reduce the number of idle vehicles in the normal period and narrow the price gap between the two periods. Furthermore, we numerically verify the finding that the platform has more incentive to adopt the open business model under low or moderate demand surge in these extension models.

## 7. Conclusions and Discussions

Motivated by the exploding growth of the ride-hailing market, we study whether a ride-hailing firm should adopt a closed business model in which only the plat form’s own vehicles are available or an open business model, opening up its platform to private vehicles. We build a two-period model to analyze this market, featuring a demand surge from the normal period to the surge period; examine how the equilibrium number of platform-owned vehicles, service prices, and market demands change as the platform switches from a closed business model to an open business model; and derive the conditions under which the closed or open business model is more profitable for the ride-hailing firm.

Our analytical results lead to several important findings. First, we find that adopting the open business model results in two important effects: the supplyaugmenting effect and price discrimination–hindering effect, both benefiting the riders especially in the surge period. Second, compared with the closed business model, the open business model enables the platform to purchase fewer vehicles, thus reducing the number or the downtime of idle vehicles in the normal period and leading to more efficient utilization of vehicle resources. Third, adopting the open business model can reduce the price gap between the surge and normal periods, alleviating public criticism toward surge pricing. Fourth, the aforementioned effects ensure that the open business model always leads to higher social welfare compared with the closed business model. Finally, and counterintuitively, we find that the open business model does not always lead to a higher profit for the platform. In sum, the open business model always benefits the riders, drivers, and society but may or may not be more profitable for the platform.

This study also has important practical implications for platform owners. First, it provides critical theoretical guidelines to help firms assess whether opening their platforms to private drivers is a profitable strategy. If it is indeed profitable, the equilibrium solutions and related findings could also be utilized to generate operational guidelines when a platform implements the open business model. For instance, one of our key findings is that, when the market potential is low, a moderate demand surge makes the open business model more attractive, whereas a low or high demand surge makes the open business model less appealing. In practice, some platforms may indeed be able to influence the magnitude of the demand surge. Then, the findings derived from this study can help guide a platform in jointly determining its business model and operational tactics to influence the demand surge. If taking actions to influence the demand surge incurs a significant cost, our analytical solutions can help a platform compare the costs and benefits of different actions and then decide the best course of action. Furthermore, our results show that the open business model has two merits (reducing the number of idle vehicles in the normal period and the magnitude of increase in price in the surge period) even when it is dominated by the closed business model in terms of profitability. This important finding can provide invaluable insights to platform owners at both the strategic and operational levels and help them build strong and sustainable competitive advantages over competitors or future market entrants.

Our findings also provide important insights for policymakers. The open business model benefits the riders with an increased supply of service and lower service price, leads to more efficient utilization of vehicle resources, and provides private drivers with an opportunity to earn extra revenue. These effects jointly lead to higher social welfare. Given these benefits, pol icymakers should facilitate the participation of private drivers by providing training or monetary incentives. Despite the proven benefits of the open business model, we find that it may not generate more profit for the platform. To maximize the overall benefit to society, policymakers should incentivize a platform to select the open business model by providing, for instance, tax subsidies to the platform to ensure that the open business model is more profitable to the platform.

This paper contributes to the literature on ride-hailing platforms by studying the impacts of different business models in the presence of demand surge. Although this study focuses specifically on ride-hailing platforms, we note that other on-demand service platforms also face the choice between open and closed business models. For instance, in the realm of on-demand delivery service, notable platforms such as Uber Eats, DoorDash, and Postmates operate under a pure-sharing open model. Meanwhile, platforms such as Meituan, Ele.me, Instacart, and Shyp opt for a hybrid open model. In contrast, Waitr, SF Tongcheng, SF Express, and UPS rely exclusively on hired delivery personnel. Similar divergence in business models is also observed in the on-demand labor service market. For instance, TaskRabbit facilitates the matching of freelance labor with demand, whereas Managed by Q adopts a closed business model by directly hiring employees to provide services. The model and analysis presented in this study can be adapted to help improve decision making for these other types of platforms. In fact, our findings could be applicable to a broader spectrum of on-demand service platforms if the following conditions are met: (a) the service providers can enter and leave the market freely, (b) the platform is the price maker and the pricing decision determines the number of participants on both sides of the market, and (c) there are distinct normal and surge demand periods in the market.

There exist several interesting directions for future research. For instance, this study considers a monopoly market with only one ride-hailing platform. Com petition among ride-hailing platforms plays a vital role in promoting an open platform. Private drivers can easily join an open platform—or even multiple platforms concurrently—thereby enhancing competitiveness through two-sided network effects. Hence, it would be interesting to investigate the optimal business models for competing platforms. Second, this study assumes identical service levels from the platform-owned vehicles and the private vehicles. Platform-owned vehicles are sometimes perceived as more professional and comfortable options compared with private vehicles. A future study could consider asymmetric service levels and explore how the gap in service quality between the two types of vehicles can impact the decisions of the platforms. Third, the present study focuses on ride-hailing platforms. In a future direction, one could examine how a traditional retailer can benefit from opening up its platform and how the cross- and same-side network effect, commission rate, or government subsidy affects the platform’s profitability. In addition, a private driver who owns a car may opt to use a platform-owned vehicle if the profits are more lucrative. Therefore, a future study could consider drivers’ decisions regarding whether to drive their own vehicle or use a platformowned vehicle.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for helpful and constructive suggestions throughout the review process. Haiyang Feng, Nan Feng, and Ling Zhang have made equal contributions and are co-first authors.

## Endnotes

<sup>1</sup> The two periods in our model can be perceived as the cumulation of all the normal or surge periods in the planning horizon. We use exogenous variables, t<sub>N</sub> and $t _ { S } ,$ to depict the lengths of the two periods instead of normalizing them to one.

<sup>2</sup> According to industry news and reports, the quantity of platformowned vehicles changes from year to year, rendering it an operational-level decision variable. Thus, it is reasonable to assume that the number of platform-owned vehicles is determined after the decision on platform openness.

<sup>3</sup> In this study, the service cost consists of not only fuel cost but also vehicle value depreciation caused by usage (e.g., wear and tear, mileage).

<sup>4</sup> In equilibrium, $n _ { 1 }$ is larger than or equal to $M _ { N } ^ { O } - l n _ { 2 N }$ because, otherwise, the platform raises the service price to lower the demand and improve the profit margin. The matching results of this model align with a likelihood-based model: $\begin{array} { r } { D _ { 1 N } ^ { O } = \frac { n _ { 1 } ^ { - } } { n _ { 1 } + l n _ { 2 N } } M _ { N } ^ { O } } \end{array}$ and $\begin{array} { r } { D _ { 2 N } ^ { O } = \frac { l n _ { 2 N } } { n _ { 1 } + l n _ { 2 N } } M _ { N } ^ { O } } \end{array}$ with a detailed comparison provided in Online Appendix B.

<sup>5</sup> This assumption is satisfied in our equilibrium outcomes.

<sup>6</sup> For notational simplicity, the fixed cost includes salary paid to drivers and insurance premiums during the service life of a vehicle as well as vehicle value depreciation caused by the passage of time.

<sup>7</sup> Expressions for $A _ { j } , B _ { j } , E _ { j } ,$ , and $G _ { j }$ are provided in Online Appendix A.2.

<sup>8</sup> When all riders congregate in the surge period, from the perspective of the ride-hailing platform, demand fluctuation vanishes.

<sup>9</sup> Moderate demand surge (a<sub>S1</sub> < a<sub>S</sub> ≤ a<sub>S2</sub>) corresponds to the case of $k _ { 2 } \leq k < k _ { 1 }$ in Table 3.

## References

Afe\`che P, Liu Z, Maglaras C (2023) Ride-hailing networks with strategic drivers: The impact of platform control capabilities on performance. Manufacturing Service Oper. Management 25(5): 1890–1908.

Babar Y, Burtch G (2020) Examining the heterogeneous impact of ride-hailing services on public transit use. Inform. Systems Res. 31(3):820–834.

Benzell SG, Hersh J, Van Alstyne M (2024) How APIs create growth by inverting the firm. Management Sci. 70(10):7120–7141.

Bhargava HK, Choudhary V (2004) Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1):22–36.

Bimpikis K, Candogan O, Saban D (2019) Spatial pricing in ride sharing networks. Oper. Res. 67(3):744–769.

Bish EK, Wang Q (2004) Optimal investment strategies for flexible resources, considering pricing and correlated demands. Oper. Res. 52(6):954–964.

Boyabatlı O, Leng T, Toktay LB (2016) The impact of budget con straints on flexible vs. dedicated technology choice. Management Sci. 62(1):225–244.

Cachon GP, Daniels KM, Lobel R (2017) The role of surge pricing on a service platform with self-scheduling capacity. Manufacturing Service Oper. Management 19(3):368–384.

Castillo JC, Knoepfle D, Weyl EG (2024) Matching and pricing in ride hailing: Wild goose chases and how to solve them. Management Sci., ePub ahead of print September 11, https://doi. org/10.1287/mnsc.2022.00096.

Chen J, Guo Z (2022) New-media advertising and retail platform openness. MIS Quart. 46(1):431–456.

Chen J, Feng N, Guo Z, Zhang W (2024) On-demand, long-term, or hybrid? An economic analysis of optimal rental models on sharing platforms. Inform. Systems Res., ePub ahead of print April 25, https://doi.org/10.1287/isre.2022.0441.

Chen MK, Sheldon M (2016) Dynamic pricing in a labor market: Surge pricing and flexible work on the uber platform. Working paper, University of California, Los Angeles.

Cheng HK, Jung KS, Kwark Y, Pu J (2023) Impact of own brand product introduction on optimal pricing models for platform and incumbent sellers. Inform. Systems Res. 34(3):1131–1147.

Chod J, Markakis MG, Trichakis N (2021) On the learning benefit of resource flexibility. Management Sci. 67(10):6513–6528

Dholakia UM (2015) Everyone hates Uber’s surge pricing—Here’s how to fix it. Harvard Business Review Online (December 21), https://hbr.org/2015/12/everyone-hates-ubers-surge-pricing heres-how-to-fix-it.

Dholakia UM, Brown GR (2016) Uber’s surge pricing: 4 reasons why everyone hates it. Government Technology Online (January 27), https://www.govtech.com/archive/ubers-surge-pricing-4- reasons-why-everyone-hates-it.html.

Economides N, Katsamakas E (2006) Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry. Management Sci. 52(7):1057–1071.

Enders A, Ko¨nig A, Grobe C (2016) The sharing economy: “Upending business as usual.” IMD. Accessed November 10, 2022, https://www.imd.org/research-knowledge/articles/the sharing-economy-upending-business-as-usual/.

Federgruen A, Yang N (2009) Optimal supply diversification under general supply risks. Oper. Res. 57(6):1451–1468.

Fine CH, Freund RM (1990) Optimal investment in product-flexible manufacturing capacity. Management Sci. 36(4):449–466.

Goyal M, Netessine S (2007) Strategic technology choice and capacity investment under demand uncertainty. Management Sci. 53(2):192–207.

Hagiu A, Jullien B, Wright J (2020) Creating platforms by hosting rivals. Management Sci. 66(7):3234–3248.

Hall J, Kendrick C, Nosko C (2015) The effects of Uber’s surge pric ing: A case study. Working paper, The University of Chicago Booth School of Business, IL.

Hamilton IA (2019) Uber drivers are reportedly colluding to trigger “surge” prices because they say the company is not paying them enough. Business Insider Online (January 14), https://www.

businessinsider.com/uber-drivers-artificially-triggering-surge-pricesreports-abc7-2019-6.

He S, Qiu L, Cheng X (2021) Surge pricing and short-term wage elasticity of labor supply in real-time ridesharing markets. MIS Quart. 46(1):193–228.

He S, Peng J, Li J, Xu L (2020) Impact of platform owner’s entry on third-party stores. Inform. Systems Res. 31(4):1467–1484.

Hu B, Hu M, Zhu H (2022) Surge pricing and two-sided temporal responses in ride hailing. Manufacturing Service Oper. Management 24(1):91–109.

Ke J, Xiao F, Yang H, Ye J (2020) Learning to delay in ride-sourcing systems: A multi-agent deep reinforcement learning framework. IEEE Trans. Knowledge Data Engrg. 34(5):2280–2292.

Kouvelis P, Li J (2008) Flexible backup supply and the management of lead-time uncertainty. Production Oper. Management 17(2): 184–199.

Lowrey A (2014) Is Uber’s surge-pricing an example of high-tech gouging? The New York Times Magazine Online (January 10), https://www.nytimes.com/2014/01/12/magazine/is-ubers-surgepricing-an-example-of-high-tech-gouging.html.

Maximize Market Research (2024) Ride-hailing market: Global analysis and forecast (2024–2030). Accessed February 15, 2025, https:// www.maximizemarketresearch.com/market-report/global-ridehailing-market/78559/.

Niculescu MF, Wu DJ, Xu L (2018) Strategic intellectual property sharing: Competition on an open technology platform under network effects. Inform. Systems Res. 29(2):498–519.

Parker GG, Van Alstyne M (2018) Innovation, openness, and plat form control. Management Sci. 64(7):3015–3032.

Simchi-Levi D, Wang H, Wei Y (2018) Increasing supply chain robustness through process flexibility and inventory. Production Oper. Management 27(8):1476–1491.

Song W, Chen J, Li W (2021) Spillover effect of consumer awareness on third parties’ selling strategies and retailers’ platforms open ness. Inform. Systems Res. 32(1):172–193.

Statista Market Insights (2023) Ride-hailing: Market data & analysis. Accessed December 20, 2023, https://www.statista.com/outlook mmo/shared-mobility/ride-hailing/china.

Wang Y, Webster S (2022) Product flexibility strategy under supply and demand risk. Manufacturing Service Oper. Management 24(3): 1779–1795.

Xu Z, Yin Y, Ye J (2020) On the supply curve of ride-hailing systems. Transportation Res. B Methodology 132:29–43.

Yang H, Shao C, Wang H, Ye J (2020) Integrated reward scheme and surge pricing in a ridesourcing market. Transportation Res. B Methodology 134:126–142

Yoo B, Choudhary V, Mukhopadhyay T (2002) A model of neutral B2B intermediaries. J. Management Inform. Systems 19(3):43–68.

Zhang C, Chen J, Raghunathan S (2024) When sharing economy meets traditional business: Coopetition between ride-sharing plat forms and car-rental firms. Inform. Systems Res. 35(3):1137–1153.

Zhu Z, Ke J, Wang H (2021) A mean-field Markov decision process model for spatial-temporal subsidies in ride-sourcing markets Transportation Res. B Methodology 150:540–565.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
