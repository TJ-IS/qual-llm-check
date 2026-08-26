---
otero_id: 28401
otero_key: "T33ZDCX6"
title: "Mergers Between On-Demand Service Platforms: The Impact on Consumer Surplus and Labor Welfare"
authors: "Xiaogang Lin; Tao Lu; Xin Wang; Gang Kou"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0553"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/T33ZDCX6/fulltext/images/4287225aee72e882ef3099f57a3934a0582dd366609401da30056a49653605f6.jpg)

# Mergers Between On-Demand Service Platforms: The Impact on Consumer Surplus and Labor Welfare

Xiaogang Lin,<sup>a</sup> Tao Lu,<sup>b</sup> Xin Wang,<sup>c,d,</sup>\* Gang Kou<sup>c,d,e</sup>

<sup>a</sup> School of Management, Guangdong University of Technology, Guangzhou, Guangdong 510520, China; <sup>b</sup> School of Business, University of Connecticut, Storrs, Connecticut 06269; <sup>c</sup> School of Business Administration, Southwestern University of Finance and Economics, Chengdu 611130, China; <sup>d</sup> Big Data Laboratory on Financial Security and Behavior, Southwestern University of Finance and Economics, Chengdu 610074, China; <sup>e</sup> Xiangjiang Laboratory, Changsha 410205, China \*Corresponding author

Contact: xglin1010@hotmail.com (XL); tao.lu@uconn.edu, https://orcid.org/0000-0001-6373-3285 (TL); wxin@swufe.edu.cn, https://orcid.org/0000-0001-6354-7810 (XW); kougang@swufe.edu.cn, https://orcid.org/0000-0002-9220-8647 (GK)

Received: October 3, 2022 Revised: October 5, 2023; May 16, 2024 Accepted: June 16, 2024 Published Online in Articles in Advance: January 31, 2025

https://doi.org/10.1287/isre.2022.0553

Copyright: © 2025 The Author(s)

Abstract. On-demand service platforms connect customers with independent service providers (agents) by competitively setting service prices and wages. Mergers between on-demand service platforms have recently become prevalent, resulting in antitrust debates. A merger, although reducing competition, enables the agents on previously separate platforms to serve all the customers. In this paper, we develop a game-theoretical model to analyze the impact of a merger between two platforms. The two platforms compete on prices and wages before the merger, but are managed by a single firm after the merger. We show that a merger not only creates pooling benefits, but also enhances the cross-side network effect (i.e., customers benefit from more agents and vice versa). As a result, it can lead to a win-win-win outcome, where the platforms’ profits, consumer surplus, and labor welfare all improve after a merger. The win-win-win outcome is more probable if the premerger market is less saturated or if the market is more differentiated on the customer/agent side. Interestingly, a stronger within-side congestion effect may either strengthen or weaken a merger’s potential to benefit customers. Additionally, we show that a merger is less likely to improve consumer surplus and labor welfare if there are more multihoming agents in the market and that it is more likely to benefit labor welfare if there is less cross-side price transparency. Our results provide guidelines for antitrust policymakers to evaluate the impact of a merger between on-demand service platforms.

History: Giri Kumar Tayi, Senior Editor; Jianqing Chen, Associate Editor. 55

Open Access Statement: This work is licensed under a Creative Commons Attribution-NoDerivatives 4.0 International License. You are free to download this work and share with others commercially or noncommercially, but cannot change in any way, and you must attribute this work as “Information Systems Research. Copyright © 2025 The Author(s). https://doi.org/10.1287/isre.2022.0553, used under a Creative Commons Attribution License: https://creativecommons.org/licenses/by-nd/4.0/.”

Funding: X. Lin received financial support from the National Natural Science Foundation of China [Grants 72471063 and 72001048], the Guangdong Basic and Applied Basic Research Foundation [Grant 2023A1515010857], and the Guangzhou Science and Technology Programme [Grant 2024A04J2557]. X. Wang received financial support from the National Natural Science Foundation of China [Grant 72495125], the Guanghua Talent Project of the Southwestern University of Finance and Economics, and the Research Grants Council of the Hong Kong Special Administrative Region, China [Grant 16210720]. G. Kou received financial support from the National Natural Science Foundation of China [Grants 72495125 and 71910107002].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0553.

Keywords: mergers and acquisitions • platform competition • consumer surplus • labor welfare • sharing economy

## 1. Introduction

Mergers and acquisitions are becoming a critical business strategy for companies looking to expand into new markets, increase their competitiveness, and reduce costs. Of the different types of mergers, horizontal mergers, involving two firms competing in the same market, are often of concern to antitrust agencies because they may lessen competition substantially and harm consumers (U.S. Federal Trade Commission, Guide to Antitrust Laws, https://www.ftc.gov/advice-guidance/competition-guid ance/guide-antitrust-laws). Extant research has focused on horizontal mergers in conventional industries (see Whinston 2007 for a comprehensive review). However, the current research lacks several key elements needed to analyze increasingly common horizontal mergers in the rapidly developing sharing economies.

On-demand service platforms, a major type of sharing-economy platform, connect customers in need of a service with independent service providers (agents) who self-schedule their supply. These platforms exhibit two main features: (i) the services provided are often time-sensitive; and (ii) the platforms set both service prices and wages to attract customers and agents, respectively, and earn revenue when a customer and an agent are matched (see Zhang et al. 2022 for a comprehensive summary of platforms setting both prices and wages). For example, food delivery platforms (e.g., DoorDash and Uber Eats) connect independent food couriers with customers; ride-hailing platforms (e.g., Lyft and Uber) match drivers and riders; and carsharing platforms (e.g., GetAround and Turo) connect car owners and car renters.<sup>1</sup> In recent years, mergers between on-demand service platforms have become prevalent. Examples are abundant. For food delivery services, two major companies in the United States, Postmates and Uber Eats, merged in 2020 (Gandotra 2020), and Delivery Hero sold its operations in Germany to its Dutch competitor Takeaway.com in 2018 (Dealroom 2018); car-sharing platforms GetAround and HyreCar joined together in 2023 (PYMNTS 2023); and in ridehailing markets, Didi Chuxing and Grab have acquired Uber’s operations in China and Southeast Asia, respectively (Abkowitz and Carew 2016, Russell 2018).

Debates have arisen regarding the impact of mergers between on-demand service platforms. On the one hand, mergers reduce market competition, raising antitrust concerns such as potential increases in service prices. On the other hand, merged firms typically enable agents to serve all the customers from previously separate platforms, thereby gaining an advantage from resource pooling. For example, after the Postmates-Uber Eats merger, Postmates drivers’ accounts were linked with Uber Eats, such that “instead of pulling orders from one platform, they may now accept orders from either” (Helling 2023). As such, agents have more opportunities to make money, and customers have access to more agents to fill their demand in a timely manner. As Helling (2023) commented, “some sources argue that the customer suffers from the merger … .A lawsuit [was] filed that claimed customers are paying artificially inflated prices for food. However, not much attention has been drawn to any divergence in customer service now compared to customer service before the merger. Those that use the delivery apps report satisfactory levels of customer service.”

To analyze the impact of mergers between on-demand service platforms, several key features of these platforms need to be considered. First, because services are timesensitive, customers care about waiting time when choosing which platform to use. With all else equal, a customer will wait less and obtain a higher utility from a platform if more agents are available on the platform; on the other hand, the customer will wait longer if more other customers are requesting services, resulting in greater congestion on the platform. We refer to the above features as a positive cross-side network effect and a negative within-side congestion effect, respectively. Second, selfscheduling agents, unlike full-time employees in traditional firms, get paid only when they fulfill a customer order, and so agents care about work opportunities on a platform. Similar to the two effects on the customer side, agents will expect more work opportunities and, thus, more earnings from a platform if there are more customer orders or fewer competing agents on the platform. Last but not least, as mentioned above, the postmerger firm usually enables agents to serve customers on previously separate platforms. This merger-enabled resource pooling has a crucial impact on the aforementioned network effects because after a merger, customers may have access to more agents, and agents have more work opportunities.

In this paper, we develop a game-theoretical model that captures all the above features. In the premerger market, two platforms compete on prices and wages. Customers decide which platforms to use, taking into account their preferences, prices, and network externality, and agents decide which platforms to work for based on their prefer ences, wages, and the probabilities of getting jobs—that is, utilization rates. After a merger, the two platforms are cen trally managed by a postmerger firm, and, moreover, agents are pooled together to serve the customers on both platforms. By comparing the equilibrium solutions in the premerger and postmerger scenarios, we find that a merger, although reducing competition, may improve consumer surplus and labor welfare because of the post merger resource pooling and the cross-side network effect.

The contributions of our work are summarized as follows. First, to our knowledge, this is the first paper that highlights the welfare implications of platform mergers with a postmerger pooling effect. The extant literature has established that in a single-sided market, a merger can improve consumer surplus if it leads to an exogenous and sufficiently high cost synergy (e.g., Farrell and Shapiro 1990, Whinston 2007).<sup>2</sup> However, in our setting, the “cost synergy” arises endogenously from resource pooling and the dynamics of the agent-side market. We provide conditions under which this endogenized synergy is sufficient for a merger to result in a win-win-win outcome, where the platform profits, consumer surplus, and labor welfare are all improved. In particular, the win-win-win outcome is more probable if the premerger market is less saturated or if the market is more differentiated on the customer/agent side.

More interestingly, with a stronger within-side congestion effect, the impact of a merger on consumer surplus may vary due to two competing forces. First, a stronger congestion effect reduces the premerger market saturation, making the merger more likely to improve consumer surplus. On the other hand, an increase in price leads to less congestion, which partially counteracts the negative impact on customer utility. This stronger congestion effect results in customers being less sensitive to price, enabling the merged firm to extract consumer surplus more effectively. Consequently, a stronger congestion effect may either amplify or attenuate a merger’s potential to benefit customers.

Furthermore, as a merger reduces competition on both sides, one might expect prices to increase and wages to decrease after a merger. However, we show that, although the price increases after the merger, the merged firm may offer a higher wage in some cases because a higher wage attracts more agents and helps expand the postmerger market.

Additionally, with several model extensions, we find that a merger is more likely to be welfare-improving if fewer agents are multihoming in the premerger market; if prices and wages are not observable to agents and customers, respectively; or if more customers or agents are loyal to each platform.

The rest of the paper is organized as follows. In Section 2, we review related literature. We introduce our model settings in Section 3. In Section 4, we present our analysis and results. In Section 5, we discuss several extensions of our base model. We conclude our paper in Section 6. Proofs are presented in the Online Appendix.

## 2. Literature Review

There has been a growing literature on the implications of sharing-economy platforms, such as the impact of ride-hailing platforms on traditional transportation services (Yu et al. 2020), the economic and societal impact of home-sharing platforms (Zervas et al. 2017, Han et al. 2022), the welfare implications of peer-to-peer rental markets (Abhishek et al. 2021), and the co-opetition between ride-sharing platforms and car rental businesses (Zhang et al. 2024). Numerous papers have developed analytical models to examine various pricing and operations strategies from a monopolistic platform’s perspective, such as surge pricing (e.g., Cachon et al. 2017, Hu et al. 2021), spatial pricing (Bimpikis et al. 2019), flat commissions (Chen and Hu 2020), dynamic payout ratios (Bai et al. 2019), and allocation mechanisms (Lu et al. 2023). Other works examine the impacts of various relevant factors, such as delay sensitivity (Taylor 2018), forward-looking behavior (Chen and Hu 2020), matching mechanisms (Feng et al. 2021), labor pool size (Benjaafar et al. 2021), etc. Unlike the aforementioned studies focused on a monopoly platform, our paper studies two competing platforms and highlights the impact of a merger between platforms on consumer surplus and labor welfare.

More relevant to our paper is the literature considering price and wage competition between on-demand service platforms. Cohen and Zhang (2022) analyze the impact of introducing a new joint service between two competing platforms and show the existence of a profitsharing contract that benefits both platforms. Bai and

Tang (2022) study a case in which two on-demand platforms engage in Bertrand competition for customers and single-homing agents who possess a homogeneous preference for both platforms. In their model, only one platform can sustain profitability, and the other firm earns zero profit in equilibrium. Wu et al. (2020) further add a sequential subgame between customers and agents and propose useful refinement rules for multiple equilibria. They also find that only one platform can have a positive market share in equilibrium. Different from these papers, we consider two platforms that engage in price and wage competition for customers and agents with heterogeneous preferences for the platforms. In our model, both platforms can earn positive profits in the premerger competition. More importantly, our analysis is focused on how the platform profits, consumer surplus, and labor welfare change as two platforms merge; the implications of mergers are not discussed in the above papers.

Among the works that study competition of on-demand service platforms, our work is most relevant to a subgroup of papers that analyze consumer surplus and labor welfare. Nikzad (2020) considers a model where two platforms competitively determine the service price and wage rate for customers and agents, respectively, and compares the monopoly and duopoly settings. In his model, agents have homogeneous preferences for the two competing platforms and are multihoming. Benjaafar et al. (2020) analyze a similar case in which customers have heterogeneous preferences for the two platforms, whereas agents are indifferent between the two plat forms and choose to multihome. Our work, developed in parallel to and independently of these two papers, analyzes a setting in which both customers and agents possess heterogeneous preferences for two platforms. We also consider settings with single-homing and multihoming agents. More importantly, our analysis and results underscore two countervailing forces of a merger tha drive its welfare implications—that is, a competition reduction effect and an advantage of resource pooling. As mentioned earlier, the tension between these two forces is in line with the antitrust debates in practice, but it is not captured in the above two papers. Bernstein et al. (2021) analyze a model on the competition on the customer side, while assuming that agents are not choosing between platforms,<sup>3</sup> and their focus is to analyze the impacts of surge pricing and drivers’ multihoming incentives on customers and agents, rather than the impact of mergers. More recently, Zhang et al. (2022) consider a setting in which both customers and agents have heterogeneous preferences for two platforms, like ours. However, their focus is on the impact of different wage schemes on platform profits and consumer and worker surplus. They show that, depending on the market characteristics, such as substitutability on the demand and supply sides, each of the three wage schemes (i.e., fixed commission rate, dynamic commission rate, and fixed wage) can be the best for consumers and workers. They also factor in cross-side network effects, asymmetric demand/supply functions, and wage choices in the analysis. Compared with Zhang et al. (2022), our model, instead of examining different wage schemes, is focused on comparing the customer surplus and labor welfare before and after a merger, while taking into account the merger-enabled resource pooling. Additionally, our model captures not only a positive cross-side network effect, but also a negative within-side congestion effect.

In the economics and operations literature, some papers have studied horizontal mergers in traditional production settings. Stigler (1950) uses a Cournot competition model to show that the formation of a cartel tends to reduce competition and increase prices. Williamson (1968) considers the cost synergies generated from economies of scale in mergers. He shows that cost synergies may reduce prices and benefit consumers. This trade-off between reduced competition and cost synergies has been the focus of many subsequent papers, such as Perry and Porter (1985), Farrell and Shapiro (1990), Whinston (2007), and Catala˜o-Lopes and Brito (2021). In the field of operations management, several studies examine the implications of mergers with focuses on operational factors, such as the supply chain structure (Cho 2013), contract unobservability (Li and Liu 2020), inventory aggregation (Cho and Wang 2017), etc. The above papers focus on production firms and examine the impact of mergers on consumer surplus, whereas labor welfare is not considered. In contrast, our paper considers on-demand service platforms that involve both customers and independent agents, and so we analyze both the consumer surplus and labor welfare. Moreover, a typical assumption in the above literature is that a merger results in an exogenous reduction in marginal production cost, also known as a cost synergy, which drives the welfare implications of the merger. Nevertheless, our model does not presume any cost synergy, but in some sense, a “cost synergy” arises endogenously from the postmerger pooling effect.

Finally, another relevant stream of literature to our paper is on economics of two-sided platforms (Caillaud and Jullien 2003; Rochet and Tirole 2003, 2006; Hagiu 2006, 2009; Armstrong and Wright 2007; Hao et al. 2017); see a comprehensive survey by Rysman (2009). This literature typically considers platforms deciding on the fees charged to two groups of users (e.g., consumers and content providers). Several papers have analyzed competition and mergers in this setting. For example, Armstrong (2006) studies pricing strategies in three models of twosided markets: monopoly, competing platforms with single-homing agents, and competing platforms with multihoming agents. Chandra and Collard-Wexler (2009) study a merger of two newspaper publishers with single-homing customers and advertisers. Correia-da Silva et al. (2019) use a quantity competition model to examine horizontal mergers of two-sided platforms. On-demand service platforms considered in our paper differ vastly from the platforms in the above literature. First, on-demand service platforms pay wages to the agent side, instead of charging fees. Moreover, besides the cross-side network effect, on-demand service platforms also feature a negative within-side congestion effect.

## 3. The Model

## 3.1. Premerger Scenario

Consider two competing platforms, indexed by $i = 1 , 2 ,$ that recruit independent agents $( \mathrm { e . g . }$ , drivers for food delivery platforms) to provide on-demand services to customers. We consider a two-sided market consisting of a population of potential customers and a population of potential agents. Note that we focus on a relatively short period of time, during which the potential demand and supply are stationary. Denote by N the maximum customer arrival rate and K the size of agent populations within the time period. Denote by $\mu$ the average service rate $( \mathrm { i . e . }$ , the number of services that an agent performs, on average, within a unit time period). We focus on a case in which the maximum arrival rate is smaller than the maximum possible service rate of the system $( \mathrm { i . e . , }$ $N < K \mu )$ , such that the system is not overly crowded if customers and agents all use one platform. In the premerger scenario, the two platforms compete by choosing a service price $p _ { i }$ charged to customers for using a service and a wage level $w _ { i }$ offered to agents for completing a service. The prices and wages $( p _ { i } , w _ { i } ) ^ { \prime } \mathbf { s }$ will, in turn. determine the fraction of customers (agents) actually using platform i, denoted by $n _ { i } \left( k _ { i } \right)$ , as will be detailed below.

3.1.1. Customers. Each customer demands a service and has a valuation v for the service. Platforms in practice usually provide different mobile app features and loyalty programs. To capture customers’ heterogeneous preferences for each platform, we adopt a Hotelling model (Hotelling 1929), which is common in the platform economics literature $( \mathrm { e . g . , }$ Armstrong 2006, Bernstein et al. 2021, Zhang et al. 2022). Specifically, we assume customers to be infinitesimal with a “location” parameter x uniformly distributed over [0, 1]. Platforms 1 and 2 are located at the two endpoints 0 and 1 of the Hotelling line. The location of a customer represents her taste for each platform. A customer with location parameter x will incur a disutility of $t x \left[ t ( 1 - x ) \right]$ if using platform 1 [platform 2], where $t > 0$ is a unit cost of misfit. As such, a smaller x represents a stronger affinity toward platform 1 versus platform 2.

As an important feature of on-demand service platforms, a customer’s utility from using a platform is influenced by the actual demand and supply on the platform. For example, a customer will wait longer if there are fewer available agents or more requests from other customers on the platform, because a smalle number of agents or a larger number of other customers will make it more difficult for the customer to match with a suitable agent. To incorporate these network effects while keeping the model tractable, we introduce a network externality term $\varphi _ { i }$ in the customer utility function for each platform $i ,$ defined as a linear function $\varphi _ { i } = k _ { i } K \mu - \theta n _ { i } N$ . The first term of $\varphi _ { i }$ represents the effective amount of supply, whereas the second term is the amount of demand on platform i multiplied by a factor $\theta \in [ 0 , 1 ]$ . When $\theta = 0 , \varphi _ { i }$ reduces to the cross-side network externality, as commonly adopted in the platform literature (e.g., Rochet and Tirole 2003, 2006; Zhang et al. 2022); it captures the positive cross-side network effect—that is, customers benefiting from more supply. When $\theta > 0 , \varphi _ { i }$ further incorporates a withinside congestion effect—that ${ \mathrm { i } } \mathbf { s } ,$ as more customers request services while the number of available agents is fixed, the platform is more congested, and so each customer will incur a disutility due to longer waiting time. The greater the $\theta ,$ the stronger the within-side congestion effect. Additionally, $\varphi _ { i }$ also captures economies of scale for platforms in the sense that even if $k _ { i }$ and $n _ { i }$ increase by the same proportion, the network externality $\varphi _ { i }$ will be larger. This captures the reality that matching a customer and an agent is easier when the numbers of customers and agents are both larger.

In summary, a customer’s utility from using platform $i ,$ denoted by $U _ { i } ^ { c } ,$ , depends on (i) her valuation of the service $v ,$ (ii) her location parameter $x ,$ (iii) service price $p _ { i } ,$ and (iv) network externality $\varphi _ { i }$ . Therefore, we have

$$
\begin{array}{l} U _ {1} ^ {c} = v - t x - p _ {1} + b \varphi_ {1}, \text {and} \\ U _ {2} ^ {c} = v - t (1 - x) - p _ {2} + b \varphi_ {2}, \end{array}\tag{1}
$$

where $b > 0$ represents the customers’ sensitivity to network externality. Customers maximize their utility by choosing among three options: platform 1, platform $^ { 2 , }$ and an outside option (e.g., cooking at home instead of ordering on a food delivery platform), of which the valuation is normalized to zero. Note that each customer will make a service request via at most one platform because customers are required to pay a cancellation fee if they withdraw an order that has been accepted.<sup>4</sup> We assume that the value of network externality parameter b cannot be too large—that is, $b < \overline { { b } } = \operatorname* { m i n } \{ 2 v / K \mu ,$ $t / ( K \mu - N \theta ) , ( l \theta + \sqrt { l ( l \theta ^ { 2 } + ( K \mu ^ { 2 } t / N ) ) } ) / K \mu ^ { 2 } \}$ }. Similar assumptions have been commonly adopted in the literature on two-sided markets (see, e.g., Armstrong 2006, p. 674). The assumption implies that the network externality cannot carry an exceedingly large weight in a customer’s utility function compared with the service valuation and fit, such that at least some customers can receive a positive utility without network externality. If this assumption is violated, the platforms’ profit functions will not be well-behaved, and so a premerger equilibrium may not even exist.

3.1.2. Agents. Similar to the customer side, we assume that agents are infinitesimal, each with a location parameter y uniformly distributed over a Hotelling line [0, 1]. The value of $y$ reflects an agent’s preference for plat forms. Let $l > 0$ be the agent side unit misfit cost. Then, an agent with location parameter y will incur disutility of ly $\left[ l ( 1 - y ) \right]$ if working on platform 1 [platform 2]. In practice, there are nonearning differences between platforms that influence agent preferences. For example, food delivery platforms have different payment processes and vehicle requirements. DoorDash drivers can cash out for free with a prepaid debit card, DasherDir $\operatorname { e c t } ,$ whereas Uber Eats drivers use Uber Pro Cards. Moreover, the two cards have different cashback reward programs (Campbell 2023). When picking up an order at restaurants, Uber Eats drivers do not need to pay, whereas Postmates drivers pay with a special prepaid “PEX” card. To be a food courier on Uber Eats, one must have a vehicle, whereas Postmates allows on-foot couriers (Doyle 2023). Because of these differences, agents may have heterogeneous preferences for plat forms, which is represented by the misfit cost l in our model. We also note that the assumption of heteroge neous agents has been adopted in the sharing economy literature $( \mathrm { e . g . }$ , Zhang et al. 2022). In Online Appendix I, we show that if agents have homogeneous preferences for platforms, there may not exist any pure strategy Nash equilibrium in the platform competition unde our setting.

An agent’s actual earning on platform i depends on both wage rate $w _ { i }$ and how much time the agent is occupied. As in Bai et al. (2019) and Bernstein et al. (2021), we assume that each agent on a platform has an equal probability of being assigned orders, and the agent utilization rate (or the probability of an agent receiving an order) on platform i is given by $\rho _ { i } = ( n _ { i } N ) / ( k _ { i } K \mu )$

An agent’s utility from offering service on platform i depends on (i) wage level $w _ { i } ,$ (ii) utilization rate $\rho _ { i } ,$ and (iii) his location parameter $y .$ The expected utility of an agent operating on platform $i ,$ denoted by $U _ { i } ^ { a } ,$ , is as follows:

$$
U _ {1} ^ {a} = w _ {1} \mu \rho_ {1} - l y, \mathrm{and} U _ {2} ^ {a} = w _ {2} \mu \rho_ {2} - l (1 - y).\tag{2}
$$

Agents maximize their expected utility by choosing to operate on platform 1, platform 2, or neither. If an agent chooses not to offer service at all, the agent will receive a zero utility. As such, we will focus on the case in which agents are single-homing—that is, being an available agent on at most one platform.<sup>5</sup> Nevertheless, we will extend our analysis to allow multihoming agents in Section 5.1.

Note that although only customers directly enjoy the service valuation v, as v increases and more customers join the platform, agents on this platform also become better off because of the higher probability of getting a job. On the other hand, as more agents become available, customers will benefit through increased network externality as well. This reflects a cross-side network effect in our problem.

3.1.3. Platforms. The two platforms anticipate that customers and agents make choices to maximize utility as described above, and they simultaneously determine their prices $p _ { i } ^ { \prime } \mathbf { s }$ and wages w<sub>i</sub>’s to maximize the following profit function:<sup>6</sup>

$$
\Pi_ {i} (p _ {i}, w _ {i} \mid p _ {j}, w _ {j}) = (p _ {i} - w _ {i}) \mathrm{min} \{n _ {i} N, k _ {i} K \mu \},\tag{3}
$$

where subscript j represents the rival of platform i $( i = 1 , 2 , j = 3 - i )$ . Note that a transaction is realized only when a customer is matched with an agent, and so the number of transactions is equal to the minimum of supply and demand $( \mathrm { i . e . , ~ m i n } \{ n _ { i } N , k _ { i } K \mu \} ) .$ ; see Zhang et al. (2022) for a similar modeling approach. It is worth noting that the fraction of customers using each platform $n _ { i }$ is influenced by not only prices $p _ { 1 }$ and $_ { p _ { 2 } , }$ but also the fraction of agents on each platform $k _ { 1 }$ and $k _ { 2 }$ through network externality $\varphi _ { i } ,$ whereas the fraction of agents $k _ { i }$ is influenced by not only wages $w _ { 1 }$ and $w _ { 2 } ,$ but also the fraction of customers on each platform $n _ { 1 }$ and $n _ { 2 }$ through utilization rates $\rho _ { i } .$ As such, the demand and supply on each platform, or equivalently $n _ { i }$ and $k _ { i } ,$ are jointly determined by $( p _ { 1 } , p _ { 2 } , w _ { 1 } , w _ { 2 } ) ;$ we will express $( n _ { i } , k _ { i } )$ as implicit functions in Section 4.1. We can show that the price and wage selected by platform i must satisfy $n _ { i } N \le k _ { i } K \mu$ and $\varphi _ { i } \geq 0$ in any equilibrium (see Online Appendix C for the proof). Therefore, the profit function in (3) is demand constrained in equilibrium.

## 3.2. Postmerger Scenario

In the postmerger scenario, the two platforms are managed by a central planner, which is referred to as the merged firm and denoted by m. After a merger, platforms usually maintain their brands and mobile apps separately, while allowing agents to accept customer orders from both platforms. For example, Postmates and Uber Eats merged in 2020, but still run separately; customers can still order through either the Postmates or the Uber Eats delivery app (Doyle 2023). Consistent with this practice, in the main paper, we focus on a setting in which the merged firm retains two platforms located at endpoints 0 and 1 as before.<sup>7</sup> In the long term, platforms might be able to rebrand themselves and migrate all the customers and agents to a single platform. In Online Appendix D, we examine the case where two platforms after the merger can reposition as a single brand and show that our main results continue to hold.

The merged firm controls the prices and wages for both platforms. Without loss of optimality, we consider the symmetric solution with a service price $p _ { m }$ and a wage $w _ { m }$ on both platforms (i.e., $p _ { 1 } = p _ { 2 } = p _ { m }$ and $w _ { 1 } = w _ { 2 } = w _ { m } ) ,$ ; the optimality of symmetric solution is formally proved in Online Appendix J. In contrast to the premerger scenario, the merged firm pools agents to ful fill demand streams on both platforms 1 and 2. That is, an agent on each platform can be assigned to the customers on both platforms 1 and 2. Thus, customers (agents) experience a common network externality (utilization rate), regardless of which platform they use. Let $n _ { m } = n _ { 1 } + n _ { 2 }$ and $k _ { m } = k _ { 1 } + k _ { 2 }$ be the total fractions of active customers and agents, respectively, where $n _ { i }$ and $k _ { i }$ can be obtained similarly, as in the premerger model. We denote the postmerger network externality and agent utilization by $\varphi _ { 1 } = \stackrel { \textstyle \cdot } { \varphi } _ { 2 } = \varphi _ { m } = k _ { m } K \mu - \theta n _ { m } \dot { N }$ and $\rho _ { 1 } = \rho _ { 2 } = \rho _ { m } = n _ { m } N / k _ { m } K \mu$

This merged firm m determines its service price $p _ { m }$ and wage $w _ { m }$ to maximize the following profit:

$$
\Pi_ {m} (p _ {m}, w _ {m}) = (p _ {m} - w _ {m}) \mathrm{min} \{n _ {m} N, k _ {m} K \mu \}.\tag{4}
$$

Similar to the premerger model, we also confirm that the optimal price and wage must satisfy $\rho _ { m } \leq 1$ and $\varphi _ { m } \geq 0$ (see Online Appendix C for the proof)

## 4. Results

Our focus is to investigate the impact of a merger on customer surplus (CS) and labor welfare (LW). We will first solve for the equilibria in the premerger and postmerger scenarios, respectively, and then compare the equilibrium outcomes in these two scenarios.

## 4.1. Demand and Supply Functions

We will derive demand and supply functions in this section. We say that the customer (agent) market is fully covered if none of the customers (agents) choose the outside option; otherwise, we say that the market is par tially covered. Depending on the prices and wages, the customer or the agent market may or may not be fully covered. We will use the symbol $\therefore \mathrm { F ^ { \prime \prime } \left( ^ { \prime \prime } P ^ { \prime \prime } \right) }$ to represent full (partial) coverage of a market. In general, there are four cases, depending on the market coverage of the customer and agent markets: full coverage of both mar kets (case FF), partial coverage of the customer market with full coverage of the agent market (case PF), ful coverage of the customer market with partial coverage of the agent market (case FP), and partial coverage of both markets (case PP).

From Equations (1) and (2), we can derive the frac tions of customers and agents on platform i in the premerger scenario as the following implicit functions:

$$
(n _ {i}, k _ {i}) = \left\{ \begin{array}{l} \left(\frac {1}{2} - \frac {p _ {i} - p _ {j} - b (\varphi_ {i} - \varphi_ {j})}{2 t}, \frac {1}{2} + \frac {w _ {i} \mu \rho_ {i} - w _ {j} \mu \rho_ {j}}{2 l}\right) \\ \qquad \text {if} \Sigma_ {i = 1} ^ {2} (v - p _ {i} + b \varphi_ {i}) \geq t, \\ \qquad \Sigma_ {i = 1} ^ {2} w _ {i} \mu \rho_ {i} \geq l [ \mathrm{FF} ], \\ \left(\frac {v - p _ {i} + b \varphi_ {i}}{t}, \frac {1}{2} + \frac {w _ {i} \mu \rho_ {i} - w _ {j} \mu \rho_ {j}}{2 l}\right) \\ \qquad \text {if} \Sigma_ {i = 1} ^ {2} (v - p _ {i} + b \varphi_ {i}) \\ <   t, \Sigma_ {i = 1} ^ {2} w _ {i} \mu \rho_ {i} \geq l [ \mathrm{PF} ], \\ \left(\frac {1}{2} - \frac {p _ {i} - p _ {j} - b (\varphi_ {i} - \varphi_ {j})}{2 t}, \frac {w _ {i} \mu \rho_ {i}}{l}\right) \\ \qquad \text {if} \Sigma_ {i = 1} ^ {2} (v - p _ {i} + b \varphi_ {i}) \\ \geq t, \Sigma_ {i = 1} ^ {2} w _ {i} \mu \rho_ {i} <   l [ \mathrm{FP} ], \\ \left(\frac {v - p _ {i} + b \varphi_ {i}}{t}, \frac {w _ {i} \mu \rho_ {i}}{l}\right) \\ <   t, \Sigma_ {i = 1} ^ {2} w _ {i} \mu \rho_ {i} <   l [ \mathrm{PP} ], \end{array} \right.\tag{5}
$$

where $i = 1 , 2 ,$ and $j = 3 - i .$ . The demand and supply on platform i are $n _ { i } N$ and $k _ { i } K \mu$ , respectively. Similarly, we can derive the fractions of customers and agents on each separate platform in the postmerger scenario as the following implicit functions:

$$
(n _ {i}, k _ {i}) = \left\{ \begin{array}{l l} \left(\frac {1}{2}, \frac {1}{2}\right) & \text {if} 2 (v - p _ {m} + b \varphi_ {m}) \geq t, \\ & 2 w _ {m} \mu \rho_ {m} \geq l [ \mathrm{FF} ], \\ \left(\frac {v - p _ {m} + b \varphi_ {m}}{t}, \frac {1}{2}\right) & \text {if} 2 (v - p _ {m} + b \varphi_ {m}) <   t, \\ & 2 w _ {m} \mu \rho_ {m} \geq l [ \mathrm{PF} ], \\ \left(\frac {1}{2}, \frac {w _ {m} \mu \rho_ {m}}{l}\right) & \text {if} 2 (v - p _ {m} + b \varphi_ {m}) \geq t, \\ & 2 w _ {m} \mu \rho_ {m} <   l [ \mathrm{FP} ], \\ \left(\frac {v - p _ {m} + b \varphi_ {m}}{t}, \frac {w _ {m} \mu \rho_ {m}}{l}\right) & \text {if} 2 (v - p _ {m} + b \varphi_ {m}) \\ & <   t, 2 w _ {m} \mu \rho_ {m} <   l [ \mathrm{PP} ]. \end{array} \right.\tag{6}
$$

Thus, the total demand and supply on platform m are $n _ { m } N = ( n _ { 1 } + n _ { 2 } ) N$ and $k _ { m } K \mu = ( k _ { 1 } + k _ { 2 } ) K \mu$ , respectively. Notice that both sides of Equation (5) or (6) are functions of $n _ { i }$ and $k _ { i } .$ Given any prices and wages $( { p _ { i } } , { w _ { i } } )$ and $( p _ { m } ,$ $w _ { m } )$ , we can always solve for $( n _ { i } , \ k _ { i } )$ from (5) or (6), although their closed-form expressions cannot be obtained. Thus, the supply and demand functions are well-defined when platforms optimize over price and wage.

It is noteworthy that platform i’s demand $n _ { i }$ and supply $k _ { i } ,$ defined by the implicit functions in (5), cause the profit function in (3) to be nonconcave in either $p _ { i }$ or $w _ { i } ,$ posing challenges for finding an equilibrium. Nevertheless, when $( p _ { j } , w _ { j } )$ is fixed, we can optimize over $( n _ { i } , k _ { i } )$ to determine the optimal price and wage $( p _ { i } , w _ { i } )$ , and vice versa. The profit function in (3) is concave in $n _ { i }$ and $k _ { i }$ if $b < { \overline { { b } } }$ . These properties will be used to find the equilibrium prices and wages in the premerger scenario.

## 4.2. Equilibrium Characterization

In the main body, we will focus on the case where $l < b N \mu / 2$ , which implies that the misfit cost for agents is relatively small. As a result, case FP, which corre sponds to a fully covered customer market and a partially covered agent market, will not occur in equilib rium. This is in line with the fact that, compared with customers, agents care much more about their earnings than the distinct features of platforms. We believe that this is also consistent with what we observe in practice. In Online Appendix $G ,$ we will relax this assumption and examine the case where $l \ge b N \mu / 2$

In the following sections, we will use superscripts pre and post to denote the equilibrium solutions in the premerger and postmerger scenarios, respectively. We will focus on the symmetric equilibrium in the premerger model, and so the subscript i will be omitted for brevity. In Online Appendix H, we will extend our analysis to the case of asymmetric equilibrium and demonstrate the robustness of our main results. The following lemma presents closedform solutions for the equilibrium price and wage, as well as the conditions for different market coverage.

Lemma 1 (Premerger Equilibrium). A unique symmetric equilibrium exists in the premerger scenario. The equilibrium symmetric price and wage $( p _ { 1 } ^ { p r e } = p _ { 2 } ^ { p r e } = p ^ { p r e }$ and $\dot { w } _ { 1 } ^ { p r e } = w _ { 2 } ^ { p r e }$ $\dot { = } w ^ { p r e } )$ are given in Table 1.

As shown in Lemma 1, in the premerger scenario, three different cases of market coverage, FF, PF, and PP, may happen in equilibrium. See Figure 1(a) for a graphic illustration.

• In case FF, where the service valuation v is rela tively high, the competing platforms fully cover the customer and agent markets $\bar { ( \mathrm { i . e . , ~ } n ^ { p r e } = 1 / 2 , k ^ { p r e } = 1 / 2 ) }$ There are three subcases in which the equilibrium price and wage have different expressions, depending on whether the customer/agent indifferent between two platforms obtains strictly positive utility. In FF(1), both the indifferent customer and agent receive positive utility, as valuation v is sufficiently high. In FF(2), the indifferent customer receives zero utility, but the indifferent agent obtains positive utility. In FF(3), both the indiffer ent customer and agent end up with zero utility.

• In case PF, where v is moderate, the platforms partially cover the customer market while fully covering the agent market $( \mathrm { i . e . , \ } n ^ { p r e } < 1 / 2$ and $k ^ { p r e } = 1 / 2 )$ . Similarly, two subcases may arise: in PF(1), the utility of the agent indifferent between choosing two platforms is strictly positive, whereas in PF(2), the utility of that agent is zero.

Table 1. Symmetric Equilibrium in the Premerger Model

<table><tr><td>Coverage</td><td>Condition</td><td>Equilibrium price and wage (ppre, wpre)</td></tr><tr><td>FF(1)</td><td> $v \geq \frac{3N(bN\theta+t)-K(2bN\mu-l)}{2N}$ </td><td> $\left( bN\theta + t - \frac{K(bN\mu-l)}{2N}, \frac{K(bN\mu-l)}{2N} \right)$ </td></tr><tr><td>FF(2)</td><td> $\max \left\{ \overline{v}, \frac{2(bN\theta+t)-bK\mu}{2} \right\} \leq v < \frac{3N(bN\theta+t)-K(2bN\mu-l)}{2N}$ </td><td> $\left( \frac{2v-(bN\theta+t)+bK\mu}{2}, \frac{K[bN\mu(2v+bK\mu)-(bN\theta+t)(2l+bN\mu)]}{2N[2(bN\theta+t)-bK\mu]} \right)$ </td></tr><tr><td>FF(3)</td><td> $\frac{2(bN\theta+t)-bK\mu}{2} \leq v < \max \left\{ \overline{v}, \frac{2(bN\theta+t)-bK\mu}{2} \right\}$ </td><td> $\left( \frac{2v-(bN\theta+t)+bK\mu}{2}, \frac{Kl}{2N} \right)$ </td></tr><tr><td>PF(1)</td><td> $\min \left\{ \underline{v}, \frac{2(bN\theta+t)-bK\mu}{2} \right\} \leq v < \frac{2(bN\theta+t)-bK\mu}{2}$ </td><td> $\left( \frac{2v+bK\mu}{4}, \frac{K[bN\mu(2v+bK\mu)-4l(bN\theta+t)]}{8Nv} \right)$ </td></tr><tr><td>PF(2)</td><td> $\frac{2l(bN\theta+t)}{bN\mu} - \frac{bK\mu}{2} \leq v < \min \left\{ \underline{v}, \frac{2(bN\theta+t)-bK\mu}{2} \right\}$ </td><td> $\left( \frac{2v+bK\mu}{4}, \frac{Kl(bN\theta+t)}{N(2v+bK\mu)} \right)$ </td></tr><tr><td>PP</td><td> $v < \frac{2l(bN\theta+t)}{bN\mu} - \frac{bK\mu}{2}$ </td><td> $\left( \frac{2lv(bN\theta+t)}{4l(bN\theta+t)-b^2K\mu^2N}, \frac{b^2K\mu^2Nv}{2[4l(bN\theta+t)-b^2K\mu^2N]} \right)$ </td></tr><tr><td colspan="3">Note.  $\overline{v} = \frac{4l(bN\theta+t)-b^2K\mu^2N+b\mu[(bN\theta+t)N-Kl]}{2bN\mu}$  and  $\underline{v} = \frac{4l(bN\theta+t)-b^2K\mu^2N+2\sqrt{l(bN\theta+t)[4l(bN\theta+t)-b^2K\mu^2N]}}{2bN\mu}.$ </td></tr></table>

• In case PP, where v is relatively small, the platforms partially cover both the customer and agent markets $\bar { ( \mathrm { i . e . , } n ^ { p r e } < 1 / 2 }$ and $k ^ { p r e } < 1 / 2 )$ , leaving some customers and agents choosing the outside option.

Next, we characterize the optimal price and wage along with the market coverage in the postmerger scenario, as shown in Lemma 2.

Lemma 2 (Postmerger Optimal Solution). The optimal price and wage $( p _ { m } ^ { p o s t } , w _ { m } ^ { p o s t } )$ in the postmerger scenario are given in Table 2.

Similar to the premerger scenario, Lemma 2 shows that, depending on valuation v, platform m sets the price and wage to fully cover both markets (FF), partially cover the customer market but fully cover the agent market (PF), or partially cover both markets (PP).

The equilibria in Lemmas 1 and 2 are quite different. There are no subcases within each coverage case in the postmerger equilibrium, and the pricing strategies are also different. These changes are caused by three effects induced by a merger.

First, the two platforms are managed by a central planner $( \mathrm { i . e . , }$ the merged firm m), who determines the price and wage, and, thus, there is no competition. As shown in Table 1, there are three subcases within the FF case, depending on whether a customer or agent indif ferent between joining the two platforms receives positive or zero utility. However, in the postmerger scenario, the platform has no incentive to offer additional surplus to a boundary customer or agent. Even if the markets are fully covered, a customer or agent on the boundary always receives zero utility. Therefore, there is only one possible scenario in the FF case. Similarly, there are no subcases in the PF case.

Second, the merged firm pools customers and agents together, creating a resource-pooling effect. The network externality becomes $\varphi _ { { } _ { m } } = k _ { m } K \mu - \theta n _ { m } N$ after a merger, as opposed to $\varphi _ { i } = k _ { i } K \mu - \theta n _ { i } N$ on each individual platform i $( i = 1 , 2 )$ before the merger. Because a common pool of agents are serving all the customers, the network externality also becomes larger. As discussed in Section 3.1, when the postmerger agent and customer densities both increase after a merger, it becomes easier to match a customer with an agent, as reflected in the increased externality.

Figure 1. Schematic Diagrams of (a) the Premerger Equilibrium and (b) the Postmerger Solution  
(a)  
![](/api/attachments/T33ZDCX6/fulltext/images/0b0c60f00fadafb96202f3c4b2449acc287c4097ac355c611e29d95589f4a367.jpg)

(b)  
![](/api/attachments/T33ZDCX6/fulltext/images/0d77dc5142bb0f6f6107bf70a67725c4ff536a0781669c4295b124c3666b1a13.jpg)  
Notes. This figure adopts the following parameter values: $\theta = 0 . 8 , N = 2 5 , K = 7 , \mu = 4 , t = 3 6 ,$ and l � 8. (a) Premerger. (b) Postmerger.

Table 2. Optimal Price and Wage in the Postmerger Scenario

<table><tr><td>Coverage</td><td>Condition</td><td>Optimal price and wage ( $p_{m}^{post}$ , $w_{m}^{post}$ )</td></tr><tr><td>FF</td><td> $v \geq 2bN\theta + t - bK\mu$ </td><td> $\left(\frac{2v - (2bN\theta + t) + 2bK\mu}{2}, \frac{KL}{2N}\right)$ </td></tr><tr><td>PF</td><td> $\frac{l(2bN\theta + t)}{bN\mu} - bK\mu \leq v < 2bN\theta + t - bK\mu$ </td><td> $\left(\frac{v + bK\mu}{2}, \frac{KL(2bN\theta + t)}{2N(v + bK\mu)}\right)$ </td></tr><tr><td>PP</td><td> $v < \frac{l(2bN\theta + t)}{bN\mu} - bK\mu$ </td><td> $\left(\frac{lv(2bN\theta + t)}{2[l(2bN\theta + t) - b^{2}K\mu^{2}N]}, \frac{b^{2}K\mu^{2}Nv}{2[l(2bN\theta + t) - b^{2}K\mu^{2}N]}\right)$ </td></tr></table>

Finally, after the merger, the cross-side network effect plays a more critical role in customers’ price sensitivity. The price sensitivity of customers on platform i can be represented by the derivative of the fraction of active customers on this platform with respect to the price $p _ { i } ,$ which are characterized in the following lemma.

## Lemma 3.

a. In the premerger scenario, the following result holds:

$$
\begin{array}{l} \left(\frac {\partial n _ {i}}{\partial p _ {i} ^ {+}}, \frac {\partial n _ {i}}{\partial p _ {i} ^ {-}}\right) \\ = \left\{ \begin{array}{l} (s _ {f}, s _ {f}) \text {if the coverage case is FF and} \\ \sum_ {i = 1} ^ {2} (v - p _ {i} + b \varphi_ {i}) > t, \\ (s _ {p}, s _ {f}) \text {if the coverage case is FF and} \\ \sum_ {i = 1} ^ {2} (v - p _ {i} + b \varphi_ {i}) = t, \\ (s _ {p}, s _ {p}) \text {if the coverage case is PF or P} \end{array} \right. \end{array}\tag{7}
$$

(8)

$$
P P,\tag{9}
$$

where $s _ { f } = - ( 2 t + 2 b \theta N - 2 b K \mu ( \partial k _ { i } / \partial n _ { i } ) ) ^ { - 1 } , s _ { p } = - ( t + b \theta N$ $- b K \mu ( { \partial k _ { i } } / { \partial n _ { i } } ) ) ^ { - 1 }$ , and $\partial n _ { i } / \partial p _ { i } ^ { + }$ and ${ { \partial } n _ { i } } / { { \partial } p _ { i } ^ { - } }$ are the right and left derivatives of n<sub>i</sub> with respect to $p _ { i } ,$ respectively.

b. In the postmerger scenario, the following result holds:

$$
\left(\frac {\partial n _ {m}}{\partial p _ {m} ^ {+}}, \frac {\partial n _ {m}}{\partial p _ {m} ^ {-}}\right)
$$

$$
(0, 0) \text {   if   the   coverage   case   is   FF   and   } 2 (v - p _ {m} + b \varphi_ {m}) > t,\tag{10}
$$

$$
2 (v - p _ {m} + b \varphi_ {m}) = t,\tag{11}
$$

$$
\left\lfloor \left(s _ {m}, s _ {m}\right) \text {   if   the   coverage   case   is   PF   or   PP }, \right.\tag{12}
$$

where $s _ { m } = - ( t / 2 + b \theta N - b K \mu ( \partial k _ { m } / \partial n _ { m } ) ) ^ { - 1 }$ , and $\partial n _ { m } /$ ${ \partial p _ { m } ^ { + } }$ and $\partial n _ { m } / \partial p _ { m } ^ { - }$ are the right and left derivatives of $n _ { m }$ with respect to $p _ { m } ,$ respectively.

Note that in Lemma $^ { 3 , }$ the left and right derivatives may not be equal because increasing or decreasing the price at the boundary point can result in different coverage of the customer market. Although the expressions of customers’ price sensitivity differ slightly for different coverage, the structures are the same. Take the partial coverage case in the premerger scenarios as an example. The price sensitivity $\partial n _ { i } / \partial p _ { i }$ is equal to $s _ { p } = - ( t + \bar { b } \theta N - b \hat { K \mu } \partial k _ { i } / \partial n _ { i } ) ^ { - 1 }$ . The first term, t, represents the direct loss from a higher price. The second term, bθN, accounts for the impact of the congestion on the customer side. The third term, $b K \mu \partial k _ { i } / \partial n _ { i } ,$ reflects the influence of the cross-side network effect. The third term, which increases with $\partial k _ { i } / \partial n _ { i } ,$ amplifies the magnitude of customers’ price sensitivity, meaning that the cross-side network effect causes customers to be more sensitive to price. This is because a price increase can reduce the number of active customers, which, in turn, reduces agents. The reduction in agents further decreases customers’ utility, causing more customers to leave. Given the expressions of the price sensitivity in Lemma 3, we next analyze how a merger affects the price sensitivity in the following proposition.

Proposition 1. A merger increases the weights of the crossside network effect and the congestion effect in customers price sensitivity.

Proposition 1 reveals that a merger enhances the role of the cross-side network effect and the congestion effect in customers’ price sensitivity. In the postmerger scenario, the boundary customer or agent always receives zero utility. As a result, the case specified in (10) does not appear in equilibrium. We only need to compare $s _ { p }$ and $s _ { f }$ in the premerger scenario with $s _ { m }$ in the postmerger scenario to analyze the change in the weight of the cross-side network effect. Because the weight of the cross-side network effect is the same in $s _ { p }$ and $s _ { f }$ (note that the coefficient of each term in $s _ { f }$ is twice of that in $s _ { p } )$ , it suffices to compare $s _ { p }$ and $s _ { m } .$ . By comparing the expressions of $s _ { p }$ and $s _ { m }$ in Lemma 1, we can see that the weight of the direct impact of a higher price (the first term) becomes smaller in the postmerger scenario, and, effectively, the weight of the cross-side network effect becomes greater. This is because the merged firm monopolizes the market and gets customers along the entire Hotelling line, instead of from only one endpoint, as in the premerger scenario, increasing the weight of the cross-side network effect. For a similar reason, the weight of the congestion effect in customers’ price sensi tivity is also increased after a merger. In the next section, we will show that this enhancement substantially impacts the merged firm’s pricing decision and the welfare implications of the merger.

## 4.3. Welfare and Profit Implications

Now, we proceed to investigate how consumer surplus and labor welfare change as the two platforms merge. The expressions of surplus and labor welfare under the premerger and postmerger scenarios are given below, which depend on whether the corresponding market is fully or partially covered.

In the premerger model, denote by x and x (y and y) the location parameters of the customer (agent) who is indifferent between using platform 1 and the outside option and between using platform 2 and the outside option at the symmetric equilibrium, respectively, where $\underline { { x } } = ( v - p ^ { p r e } + b \varphi ^ { p r e } ) / t , \overline { { x } } = 1 - ( v - p ^ { p r e } + b \varphi ^ { p r e } ) / t ,$ $\underline { { y } } = ( w ^ { p r e } \mu \rho ^ { p r e } ) / l , \mathrm { a n d } \bar { y } = 1 - ( w ^ { p r e } \mu \rho ^ { p r e } ) / l .$ . Then, we have

$$
C S ^ {p r e} = \left\{ \begin{array}{l} N \left(\int_ {0} ^ {\underline {{x}}} U _ {1} ^ {c} d x + \int_ {\bar {x}} ^ {1} U _ {2} ^ {c} d x\right) = N \cdot \frac {(v - p ^ {p r e} + b \varphi^ {p r e}) ^ {2}}{t} \\ N \left(\int_ {0} ^ {\frac {1}{2}} U _ {1} ^ {c} d x + \int_ {\frac {1}{2}} ^ {1} U _ {2} ^ {c} d x\right) = N \cdot \left(v - p ^ {p r e} + b \varphi^ {p r e} - \frac {t}{4}\right) \end{array} \right.\tag{[Case P],}
$$

[Case F];

$$
L W ^ {p r e} = \left\{ \begin{array}{l} K \left(\int_ {0} ^ {y} U _ {1} ^ {a} d y + \int_ {\overline {{y}}} ^ {1} U _ {2} ^ {a} d y\right) = K \cdot \frac {(w ^ {p r e} \mu \rho^ {p r e}) ^ {2}}{l} \\ K \left(\int_ {0} ^ {\frac {1}{2}} U _ {1} ^ {a} d y + \int_ {\frac {1}{2}} ^ {1} U _ {2} ^ {a} d y\right) = K \cdot \left(w ^ {p r e} \mu \rho^ {p r e} - \frac {l}{4}\right) \end{array} \right.\tag{[Case P],}
$$

[Case F]:

Similar to the premerger model, the expressions of consumer surplus and labor welfare in the postmerger model are

$$
C S ^ {p o s t} = \left\{ \begin{array}{l} N \cdot \frac {(v - p _ {m} ^ {p o s t} + b \varphi_ {m} ^ {p o s t}) ^ {2}}{t} \\ N \cdot \left(v - p _ {m} ^ {p o s t} + b \varphi_ {m} ^ {p o s t} - \frac {t}{4}\right) \end{array} \right.\tag{[Case P],}
$$

[Case F];

$$
L W ^ {p o s t} = \left\{ \begin{array}{l} K \cdot \frac {(w _ {m} ^ {p o s t} \mu \rho_ {m} ^ {p o s t}) ^ {2}}{l} \\ K \cdot \left(w _ {m} ^ {p o s t} \mu \rho_ {m} ^ {p o s t} - \frac {l}{4}\right) \end{array} \right.\tag{[Case P],}
$$

[Case F]:

The impacts of a merger on customers and agents are not straightforward. By pooling customers and agents together, a merger can generate additional utility for them. The interaction between competition and the crossside network effect determines how the additional utility is distributed among platforms, customers, and agents. In the following analysis, we will show that, depending on the specific circumstances of the market, a merger may or may not benefit customers and/or agents.

## Theorem 1.

a. The postmerger consumer surplus is higher than the premerger consumer surplus $( i . e . , C \dot { S } ^ { p o s t } > C \check { S } ^ { p r e } )$ if and only if v < min $\{ t - ( b ( K \mu - 2 N \theta ) ) / 2 ,$ , max $\{ t K \mu / 2 N \theta , ( K \mu [ { \dot { 4 } } l$ $\dot { ( } b N \theta + t ) - b ^ { 2 } K \mu ^ { 2 } \dot { N ] } ) / N ( 4 l \theta + b K \mu ^ { 2 } ) \} \}$

b. The postmerger labor welfare is higher than the premerger labor welfare $( i . e . , L W ^ { p o s i } > L W ^ { p r e } )$ if and only if $v <$ $( 2 l ( b N \theta + t ) ) / b N \mu - b K \mu / 2$

Theorem 1 analyzes how consumer surplus and labor welfare are affected by a merger. Figure 2 illustrates the comparison before and after a merger. Figure 3 illustrates the corresponding market coverage in the premerger and postmerger scenarios. As discussed in Section $4 . 2 ,$ a merger reduces competition, generates a pooling effect, and enhances the role of the cross-side network effect in customers’ price sensitivity. These three factors jointly affect consumer surplus and labor welfare.

If the premerger case is FF, the effect of competition reduction is so high that the merged firm extracts more utility than what is generated from the pooling effect, leaving customers worse off.

If the premerger case is PE. the effect of competition reduction is moderate. The enhanced cross-side net work effect, together with reduced competition, jointly determines whether the merged firm can extract all the additional utility generated from the pooling effect. When the number of active customers on a platform is small, the enhanced cross-side network effect makes customers highly sensitive to price. Customers’ high price sensitivity effectively limits the merged firm’s pric ing power and makes customers benefit from the merger. To see this, notice that, as discussed in Proposi tion 1, the magnitude of $\partial n _ { 1 } / \partial p _ { 1 }$ increases with $\partial k _ { 1 } / \partial n _ { 1 }$ because of the cross-side network effect. Furthermore, we can show that $\partial k _ { 1 } / \partial n _ { 1 }$ decreases with $n _ { 1 } ,$ , indicating that one additional customer has a diminishing benefit in attracting agents to the platform. This diminishing bene fit is caused by the utilization in agents’ utility function: When $n _ { 1 }$ increases, more agents join the platform in response, and an additional customer has a smaller impact on the utilization. Therefore, customers’ price sensitivity decreases with the number of active custo mers. When there are a small number of active custo mers, the impact of the cross-side network effect on customers’ price sensitivity is large. After a merger, the enhanced role of the cross-side network effect makes customers become even more sensitive to price. As a result, the merged firm cannot price too aggressively, leaving customers some utility generated from the pool ing effect. When there are a large number of active cus tomers, the diminishing benefit of an additional customer causes customers’ price sensitivity to be low. Even though the role of the cross-side network effect is enhanced by a merger, its impact on customers’ price sensitivity is still limited. The merged firm can aggressively set the price and extract all the utility generated from the pooling effect, leaving customers worse off. Because of the enhanced cross-side network effect and the diminishing benefit of an additional customer to agents, a merger benefits customers when the number of active customers is small. In the PF case, the active proportion of customers on platform i is given by $\bar { n } _ { i } = \bar { ( } v - p _ { i } + b \varphi _ { i } ) / t$ . As the service value v decreases, even though the platform tries to reduce its price to compensate for the negative impact of lower service value, customers’ utility of joining platform i still decreases with v, causing more customers to choose the outside option. Therefore, for small service value v, the number of active customers is small. In this case, a merger is more likely to benefit customers.

Figure 2. (Color online) The Effect of the Merger on (a) Consumer Surplus and (b) Labor Welfare  
![](/api/attachments/T33ZDCX6/fulltext/images/58d68f6c825235dc312d924f949ccbffc2fb1b0263e9c6761ba010ad43266780.jpg)

(b)  
![](/api/attachments/T33ZDCX6/fulltext/images/c1504d4871388b13fab510861307b1671622b300be32768e34561e3e2f2165f4.jpg)  
Notes. Parameter values are the same as in Figure 1. (a) Consumer surplus comparison. (b) Labor welfare comparison.

Figure 3. (Color online) Market Coverage Before and After the Merger  
![](/api/attachments/T33ZDCX6/fulltext/images/9c8f453b0c2db55ce495a2d27bf68163b726c3eba7da16d2a7db678b5354f78b.jpg)  
Note. Parameter values are the same as in Figure 1.

If the premerger case is PP, because there is a minimum impact of reduced competition, a merger is more likely to benefit customers. As shown in Figure 3, the region in which a merger improves consumer surplus is larger than that in the PF case.

The change in labor welfare after a merger is also heavily influenced by the cross-side network effect. The cross-side network effect encourages a platform to hire more agents and offer customers positive network externality, which can help the platform raise prices and earn more profit. Because a merger enhances the role of the cross-side network effect, the merged firm has an incentive to take advantage of this more effective cross-side network effect by hiring more agents and offering customers higher network externality. When v is small, such that the premerger agent market is partially covered, it is possible for the merged firm to hire more agents after a merger, and, thus, agents are better off. However, if the premerger agent market is already fully covered, the merged firm cannot hire more agents. Furthermore, the merged firm faces reduced competition and can afford to cut wages and hire the same number of agents. As a result, agents are worse off.

In summary, Theorem 1 shows that if service valuation v is small, such that the premerger market is not sat urated, a merger can improve consumer surplus and labor welfare while increasing the total profit of plat forms, thus achieving a win-win-win outcome.

To gain more insights into how a merger influences the market dynamics, it is worth comparing the equilibrium prices, wages, and profits before and after the merger.

Proposition 2. The premerger and postmerger prices, wages, and profits satisfy the following properties: (a)

Figure 4. (Color online) Numerical Illustration of the Impact of a Merger  
![](/api/attachments/T33ZDCX6/fulltext/images/016b61d1fa52c078c5c4037263be3d9df8b53dd38f869bb706520fd0b63c3df4.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/6ae73fcc6b6f483937342d05d1ac3e6238927ea1b376e3ce35b5d4bf2d3677e2.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/98b89f8808755cf7152e5eb13a42bc93e360e93f6d8a489047212df0bff6ca6c.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/ef0754abb30b59fa938d4002de52c9d805808559cefd48bca1aa809e56200709.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/7a30e0cebf1d4817578257cb8d5e439dea8ec8c9df1a5b9f97557c97eccda202.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/e90700f52057a0e123039fdab05a1993c2e2d012804c8f2107d6317de836c4aa.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/1d02bdcf2ce45cc5ed5d11e5c991f12a2849bb27ff4fb31a0e07143fe031ee55.jpg)  
Note. This figure adopts the following parameter values: θ � 0:8, b � 0.3, N � 25, K � 7, µ � 4, t � 36, and l � 8.

$\Pi _ { m } ^ { p o s t } > 2 \Pi ^ { p r e } ; \left( b \right) p _ { m } ^ { p o s t } > p ^ { p r e } ;$ ; and (c) $w _ { m } ^ { p o s t } > w ^ { p r e }$ if and only if one of the following conditions holds:

i. v < min{max{v , (l[4l(bNθ + t � b<sup>2</sup>Kµ<sup>2</sup>N)])=b<sup>2</sup>N<sup>2</sup>µ<sup>2</sup>}, (2l(bNθ + t))=bNµ � bKµ=2};

ii. max $\left\{ t K \mu / 2 \theta N , ( 2 l ( b N \theta + t ) ) / b N \mu - b K \mu / 2 \right\} < v <$ min $\left\{ v _ { w 2 } , v _ { w 3 } , t - b \left( K \mu - 2 N \theta \right) \right\}$ 8

Proposition 2 formally proves that after a merger, the platforms’ profits and service price increase, whereas the wage may either increase or decrease. Figure 4 presents a numerical example that further demonstrates how a merger changes the price and wage, along with the network externality, consumer surplus, agent utilization, labor welfare, and platform profit.

As shown in the three panels at the top of Figure 4, a merger always leads to a higher price because the market competition is reduced. Nevertheless, after the merger, customers also receive higher network externality because the merger enables resource pooling and enhances the role of the cross-side network effect, such that the merged firm has a greater incentive to take advantage of the cross-side network effect. The changes in price and network externality jointly determine the consumer surplus. When valuation v is small, the benefit of increased externality outweighs the effect of increased price, and so the merger improves the consumer surplus. We note that these observations echo the anecdotal evidence cited earlier that people are concerned with inflated prices, while acknowledging the improved customer services after the Postmates-Uber Eats merger (Helling 2023).

The effect of a merger on wages is more nuanced because the agent utility depends on the multiplication of wage and utilization. In other words, the wage and agent utilization are substitutable. As shown in the middle three panels of Figure 4, for a small $v ,$ the merged firm will substantially increase the wage to attract more agents, so as to leverage the network externality. However, for a moderate v, the pooling effect after a merger can also improve agent utilization such that it becomes less necessary for the merged firm to raise the wage, leading to the nuanced effects on wages. For a sufficiently large $v ,$ the premerger markets have been saturated, and, thus, the merger will not influence agent utilization or incentivize the firm to further expand the market; consequently, competition reduction on the supply side becomes a dominant force, and the merger results in a lower wage. Overall, the labor welfare, jointly influenced by the wage and agent utilization, can be improved by the merger when v is small enough.

Finally, the bottom panel of Figure 4 plots the premerger and postmerger profits. Clearly, the merger increases the total profit, as the merged firm can centrally optimize the price and wage. Furthermore, we observe that the magnitude of profit increase is larger with a smaller v (i.e., in a less saturated market).

Next, we analyze the impacts of several market parameters on the welfare implications of a merger. Recall that the parameter θ measures the strength of the congestion effect within the consumer side, which reflects an important feature of on-demand service platforms. Misfit costs t and l capture the levels of market differentiation on the customer and agent sides, respectively. Propositions 3 and 4 below examine if a merger will more likely improve consumer surplus and labor welfare as the within-side congestion effect (θ) and the levels of market differentiation (t and l) vary, respectively. These propositions provide insight into when antitrust agencies should consider being lenient toward mergers between on-demand service platforms.

## Proposition 3.

a. $I f N K \ge 2 t l / b ^ { 2 } \mu ^ { 2 }$ or $\theta < K \mu / 2 N$ , then as θ increases, $C S ^ { p o s t }$ is more likely to be larger than $C S ^ { p r e } ;$ however, if $N K < 2 t l / b ^ { 2 } \mu ^ { 2 }$ and $\theta \geq K \mu / 2 N ,$ then as θ increases, $C S ^ { p o s t }$ is more likely to be smaller than $C S ^ { p r e } .$

b. As θ increases, $L W ^ { p o s t }$ becomes more likely to be larger than $L W ^ { p r e }$

Proposition 3(a) indicates that as the within-side congestion effect becomes stronger $( \mathrm { i . e . , ~ } \theta$ is larger), a merger may either increase or decrease the consumer surplus. On the one hand, a larger θ implies a higher congestion cost from customers’ perspective and, thus, makes it more difficult for a platform to attract customers. Consequently, the premerger customer market is less saturated such that a merger more likely benefits customers. On the other hand, θ reduces the price sensitivity of customers for both premerger and postmerger scenarios. Intuitively, this occurs because an increase in price discourages customers from using the service, but, meanwhile, each customer anticipates less congestion, which partially offsets the negative impact of the increased price on customer utility. Proposition 1 shows that a merger enhances the role of congestion effect θ in customers’ price sensitivity because the merged firm attracts and pools customers from the entire market.<sup>10</sup> Therefore, with a higher $\theta ,$ customers are even less sen sitive to price after the merger, which enables the merged firm to price more aggressively and better extract consumer surplus. The first force related to market saturation is dominant when the potential market size is large enough $( N K \ge 2 t l / b ^ { 2 } \mu ^ { 2 } )$ , such that an increase in $\theta$ always makes the merger more likely to benefit customers. However, when the potential market size is small $( N K < 2 t l / b ^ { 2 } \mu ^ { 2 } )$ , the latter force as to custo mers’ price sensitivity may dominate the former, such that an increase in θ can make the merger less likely to benefit customers. See the nonmonotone threshold, as illustrated in Figure 5(a). Our result suggests that for small-sized markets, a merger may have the most poten tial to improve consumer surplus when there is a moderate level of congestion effect.

Proposition 3(b) indicates that a stronger congestion effect (a larger θ) always makes the merger more likely to benefit agents, as illustrated in Figure 5(b). With a larger θ, premerger platforms are more likely to serve fewer customers and, hence, hire fewer agents. A merger can thus induce the firm to hire more agents, thus improving the labor welfare.

Proposition 4. As t or l increases, $C S ^ { p o s t }$ and $L W ^ { p o s t }$ are more likely to be larger than $C S ^ { p r e }$ and $L W ^ { p r e }$ , respectively.

Proposition 4 shows that when the market becomes more differentiated on the customer or agent side (t or l increases), a merger is more likely to improve consumer surplus and labor welfare. A more differentiated market indicates that competition is less intense in the premerger scenario, and, thus, the impact of competition reduction caused by a merger becomes smaller. Therefore, a merger is more likely to benefit customers and agents.

In summary, our analysis shows that, although a merger reduces competition and increases prices, it can still benefit customers and agents because of the pooling benefit and the enhanced role of the cross-side network effect. This socially beneficial outcome can emerge when customers’ valuation for the service is not very high or the customer or agent side is more differentiated. Interestingly, this outcome is most likely when customers have a moderate sensitivity to congestion; both very high and very low levels of congestion sensitivity can undermine the merger’s potential to benefit customers. Our results provide new insights to antitrust agencies. When evaluating potential mergers of on-demand service platforms, antitrust agencies should consider not

(a)

Figure 5. (Color online) The Effect of the Congestion on the Change in (a) Consumer Surplus and (b) Labor Welfare  
![](/api/attachments/T33ZDCX6/fulltext/images/934dc189271d7c1e1f671f8917f1e2a2efaf8f2cc0d04cd12e423e47f64a140a.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/85127f1aba0b64eba24fc70e1229730376c3869c9a7b5b5a31f0e889abe25385.jpg)  
Notes. This figure adopts the following parameter values: b � 0.3, N � 25, K � 7, µ � 4, t � 36, and l � 8 such that $\begin{array} { r } { N K < \frac { 2 t l } { b ^ { 2 } \mu ^ { 2 } } , } \end{array}$ . (a) Consumer surplus change. (b) Labor welfare change.

only the possible changes in prices and wages, but also the aforementioned factors that influence the interplay among reduced competition, cross-side network effects, and pooling benefits.

## 5. Extensions

Our base model can be extended in various directions. In this section, we provide a summary of these model extensions, whereas the detailed analyses can be found in the online supplement of the paper. In Section 5.1, we discuss an extension where some agents are multihoming. In Section 5.2, we consider a case where the prices and wages are unobservable to agents and customers, respectively. In Section 5.3, we discuss other extensions to examine the robustness of our results.

## 5.1. Multihoming Agents

In the base model, we have assumed that all the agents could work for only one platform. In practice, there are cases in which some agents can multihome—that is, they can be simultaneously available on both platforms. In this subsection, we consider a more general setting, in which, among the K potential agents, an η proportion of the agents is multihoming, whereas the 1 � η proportion is single-homing. We assume that the multihoming agents choose between working for both platforms and getting the outside option (i.e., not working at all). When they choose to work, they wait on both platforms and will accept jobs from either platform. On the other hand, single-homing agents remain the same as in our base model—that is, they choose to work for either platform 1 or platform 2, or opt for the outside option. For tractability, we assume the proportion η to be a given parameter. It is a reasonable assumption because agents choice between single-homing and multihoming is a long-term decision driven primarily by personal nature. 11

Because of the complexity of the problem, we first analyze an extreme case where all the agents are multihoming—that is, $\eta = 1$ . We can show that in the premerger scenario, multiple Nash equilibria exist, but there is a unique symmetric Pareto-optimal equilibrium. We focus on this unique symmetric Pareto-optimal equilibrium when comparing the premerger and postmerger scenarios. The detailed analysis can be found in Online Appendix E.

Proposition 5. When all the potential agents can multihome (i.e., η � 1), if v is sufficiently large and $N > K \mu / 2$ , then th following results hold:<sup>12</sup>

a. In the premerger scenario, there exists a unique symmetric Pareto-optimal equilibrium in which $p ^ { p r e } = \stackrel { \cdot } { t } + \stackrel { \cdot }  ( l ( 4 N -$ $K \mu ) ) / 2 K \mu ^ { 2 }$ and $w ^ { p r e } = l / 2 \mu$

b. In the postmerger scenario, the optimal price and wage are given by $p _ { m } ^ { p o s t } = ( 2 v - ( 2 b N \theta + t ) + 2 b K \mu ) / 2$ and $w _ { m } ^ { p o s t } =$ $K l / 2 N$

c. The postmerger profit is higher than the total premerger profit $( i . e . , \Pi _ { m } ^ { p o s t } > 2 \dot { \Pi } ^ { p r \acute { e } } ) ;$ the postmerger consumer surplus is lower than the premerger one $( i . e . , C S ^ { p o s t } < C S ^ { p r e } ) ;$ ; both the postmerger and premerger labor welfare are zero $( i . e . ,$ $L W ^ { \dot { p } o s t } = L \dot { W } ^ { p r e } = 0 )$

Proposition 5 indicates that when all the agents multihome, a merger hurts customers, but does not affect agents. Before the merger, multihoming agents already work for two platforms simultaneously, and customers already achieve the maximum possible network externality because agents are already “pooled” together. A merger merely reduces competition in the customer market without generating additional value from the pooling effect. Thus, customers are generally worse off as a merger takes place. On the agent side, because multihoming agents are not choosing between platforms, they are, in effect, homogenous when deciding whether to work (on both platforms) or not. Consequently, in both premerger and postmerger markets, platforms can extract all the labor welfare in equilibrium, implying that $L W ^ { p o s t } = L W ^ { p r e } = 0$

For general cases when $\eta < 1$ , the problem becomes intractable, and so we resort to numerical simulations. Specifically, to solve the premerger model, we adopt a best-response dynamics process to compute the most reasonable equilibrium (if any). In the best-response dynamics, players take turns to update their strategies based on the best responses; if the process converges to a stable strategy profile, then this strategy profile is a Nash equilibrium (Kleinberg and Tardos 2005, p. 692). A detailed description of our algorithm and numerical study can be found in Online Appendix E. We present our main findings in a representative example shown in Figure 6.

As depicted in Figure 6, the postmerger profit is higher than the total premerger profit. More importantly, as the proportion of multihoming agents (η) increases, it is less likely for a merger to benefit customers and agents. As mentioned earlier, the existence of multihoming agents reduces the pooling benefit from a merger because the benefit has been utilized before the merger and also makes it easier for platforms to extract labor welfare. We highlight this main finding below.

Observation 1. As the proportion of multihoming agents becomes larger, a merger will be less likely to improve consumer surplus and labor welfare.

Our findings suggest that antitrust agencies should be cautious about platform mergers if a large proportion of agents in the market is multihoming.

## 5.2. Customers (Agents) Do Not Observe Wages (Prices)

In the base model, we have implicitly assumed that customers can observe agents’ wages, and agents can also observe customers’ prices, because it is a common assumption adopted in the literature. However, in some practical situations, prices and wages may not be observable to agents and customers, respectively. We thus consider this alternative setting in this subsection.

Because customers (agents) cannot observe wages (prices), our model becomes a game of imperfect information. To analyze this game, the out-of-equilibrium beliefs must be treated with caution. In this analysis, we adopt passive beliefs, a commonly used equilibrium-refinement criterion in the literature $( \mathrm { e . g . } ,$ , Hart et al. 1990, McAfee and Schwartz 1994, Segal 1999, Gavazza and Lizzeri 2009). Under passive beliefs, customers’ and agents beliefs do not change when an out-of-equilibrium offer is observed.

Given the incomplete information, platform i’s profit function in the premerger scenario is not jointly concave either in $( p _ { i } , w _ { i } )$ or in $( n _ { i } , k _ { i } )$ for any given price $p _ { j }$ and wage $w _ { j }$ of platform $j ,$ and it becomes intractable to establish analytical results about the equilibrium. Nevertheless, by utilizing necessary optimality conditions, we can derive the closed-form expressions for the prices and wages under each possible equilibrium case and then leverage these expressions to develop a numerical approach to solve the model. By examining a wide range of parameter values, we are able to find a symmetric premerger equilibrium and an optimal postmerger solution in all the instances. A detailed description of our numerical study can be found in Online Appen dix F. Below we report our main findings.

Observation 2. When prices and wages are not observed by agents and customers, respectively, we observe the following results: (a) The profit of the merged firm is always higher than the total profit of the premerger platforms $( \mathrm { i . e . , } \Pi _ { m } ^ { p o s t } > 2 \Pi ^ { p r e } ) ;$ (b) the postmerger consumer surplus is higher than the premerger consumer surplus $( \mathrm { i . e . , } C S ^ { p o s t } > C S ^ { p r e } )$ if and only if v is relatively small; and (c) the postmerger labor welfare is not smaller than the premerger one $( \mathrm { i . e . , } L W ^ { p o s t } \geq L W ^ { p r e } )$

Our main results from the base model continue to hold when wages and prices are not observable to customers and agents, respectively. A merger can result in a win-win-win outcome if the service valuation v is relatively small. The impact on labor welfare is slightly different: in the base model where wages and prices are observable, a merger can reduce labor welfare when v is large, whereas in the case of unobservable wages and prices, labor welfare does not decrease after a merger. When wages are observable to customers, premerger platforms may competitively offer high wages, because such high wages can attract not only agents, but also customers who would anticipate more agents by observing higher wages. However, when wages are unobservable to customers, premerger platforms have less incentive to offer high wages because wages cannot directly influence customers. As a result, with observable wages, the premerger competition in the agent market is more intense, and thus a merger has a stronger competition-reduction effect and is more likely to hurt agents, compared with the case of unobservable wages. Additionally, we also compare the merger-induced changes in consumer surplus and labor welfare with and without price and wage transparency and find that in most cases, a merger generates more benefits for consumers and agents with unobservable prices and wages. See Online Appendix F for more details.

Figure 6. (Color online) The Effect of a Merger as η (the Proportion of Multihoming Agents) Varies  
![](/api/attachments/T33ZDCX6/fulltext/images/f1b0fde7353238dede226aa55a85307e89af1e06e0440eafef0a1b74e406d21e.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/6f462d8085745878f7c3ca551b955dc18d9fa18c747728d7f6b6a5f1a5e31a2c.jpg)

![](/api/attachments/T33ZDCX6/fulltext/images/c564e77313ed251e9e60a48e6277d7cfe98223d68d34de733e662fc8b6252957.jpg)  
Notes. This figure adopts the following parameter values: $v = 1 4 , \theta = 0 . 8 , b = 0 . 3 , N = 2 5 , K = 7 , \mu = 4 , t = 3 6 ,$ and l � 8. The premerger equilibrium was determined by the best-response dynamics procedure in Online Appendix E

## 5.3. Other Extensions

In addition to the extensions discussed in Sections 5.1 and 5.2, we have also analyzed other extensions, which are summarized in the following. The details of the analysis can be found in the Online Appendix.

5.3.1. Loyal Segments of Customers and Agents. In the base model, we have focused on the case where all the customers and agents choose between the two platforms and the outside option. In practice, some customers and agents may be loyal to a certain platform, and they do not choose the other platform (Zhang et al. 2022). In Online Appendix K, we consider a case where there are additional segments of loyal customers and agents to each platform. We find that in the presence of loyal customers and agents, even when the nonloyal segment is fully covered in the premerger market, a merger can simultaneously benefit the platforms, customers, and agents, resulting in a win-win-win outcome. In addition, a merger is more likely to benefit all parties if the size of loyal customers or agents increases. Therefore, our main intuition from the base model continues to hold.

5.3.2. Quadratic Congestion Function. For tractability, we have assumed the congestion level on the consumer side to be a linear function of demand. In a more realistic setting, the congestion level can take a nonlinear form. In Online Appendix L, we consider an alternative network externality term where the within-side congestion effect is an increasing quadratic function of the agent utilization rate (Bernstein et al. 2021). We numerically verified that our main findings are robust when the congestion effect takes a nonlinear form.

5.3.3. Large Misfit Cost for Agents. So far, we have focused on the case where $l < b N \mu / 2 $ —that is, the misfit cost for an agent is relatively small. This assumption rules out a type of equilibria in which the customer market is fully covered, whereas the agent side is partially covered. For completeness, in Online Appendix $G ,$ we relax this assumption and examine the case where $l \ge b N \mu / 2$ . We find that, as in the base model, a merger can result in a win-win-win outcome when the service valuation v is relatively small.

5.3.4. The Postmerger Firm Repositions as a Single Brand. In the main body of the paper, we have focused on a situation where the two platforms remain as two separate brands after a merger. This is true for many merger events in practice (e.g., the merger between Postmates and Uber Eats). However, in some cases, the postmerger firm may transform the two platforms into one with a new brand. In Online Appendix D, we show that all our results continue to hold in a setting where there is a single postmerger platform that can optimally reposition on the Hotelling line, whereas the two premerger platforms, as in our base model, are located at points 0 and 1, respectively.

5.3.5. Asymmetric Equilibria. Our analysis has focused on symmetric equilibria in the analysis. In Online Appendix H, we develop a numerical approach to compute asymmetric equilibria (if any) and show that our main results are robust if an asymmetric equilibrium is played out.

## 6. Conclusions

Motivated by the horizontal mergers that have recently become prevalent in the on-demand economy, we built a game-theoretical model to analyze the impacts on consumer surplus and labor welfare of a merger between two on-demand service platforms. We established that although a merger reduces competition, it may benefit both customers and agents because of a merger-enabled pooling benefit, along with a positive cross-side network effect. Our results provide important managerial implications, as summarized below.

First, our analysis uncovers two countervailing forces, a competition-reduction effect and a merger-enabled pooling benefit, that jointly determine the welfare implications of a merger between on-demand service platforms. This echoes the debates mentioned earlier regarding the Postmates-Uber Eats merger (Helling 2023). When assessing the potential consequences of a merger, antitrust regulators should not only focus on the impact on service prices, but also evaluate whether the merger enables platforms to pool resources, leading to potential improvements in service quality (e.g., reduction in waiting times).

Moreover, we characterize the conditions under which a merger will be more likely to improve consumer surplus and labor welfare. These conditions provide practical guidelines for antitrust agencies to evaluate the impact of platform mergers. In particular, our findings indicate that a merger is more likely to be welfare-improving if the premerger market is less saturated. For example, the Postmates-Uber Eats merger took place when there was significant growth in demand for food delivery services, and by acquiring Postmates, Uber Eats aimed to expand its food delivery business (Gandotra 2020). Because of increased demand, the food delivery market appeared not saturated at that time, and our results suggest that a merger in such a situation has the potential to achieve a win-win-win outcome where consumer surplus, labor welfare, and the platform profitability are all improved. Additionally, we show that a win-win-win outcome is more probable if the customer/agent market is more differentiated. Our results suggest that antitrust agencies consider being more lenient toward a merger if the market has room to grow or if the two merging platforms have differentiated features.

One might jump to a conclusion that, due to resource pooling, a merger would benefit customers when the services are highly time-sensitive. Nevertheless, we find that the congestion effect on the customer side has an indeterminate impact. A win-win-win outcome is most likely to occur when customers have a moderate level of sensitivity to congestion. In other words, both very high and very low levels of congestion sensitivity can undermine the merger’s potential to benefit customers. Thus, caution should be taken regarding a merger between platforms offering highly time-sensitive services.

Furthermore, we demonstrate that a merger always leads to a price increase, but it can result in either a wage increase or decrease. Our findings imply that the firm may choose to raise wages voluntarily following a merger, even without regulatory intervention. In such cases, from the perspectives of policymakers, regulating service prices charged to customers may be more effective than regulating wages offered to agents.

Finally, our model extensions reveal additional factors relevant to the impact of a merger. A merger is less likely to be socially beneficial if more agents are multihoming in the premerger market. Our result suggests that strict antitrust policies should be imposed on markets where multihoming agents are prevalent. Moreover, a merger has greater potential to benefit consumers and agents, and hence should be granted more leniency when wages and prices are less transparent to customers and agents, respectively, or when the market contains larger segments of loyal customers and agents.

Our model has limitations that deserve discussion and future research. Our stylized model has not incorporated concrete spatial features that are particularly important to ride-hailing platforms. A more compli cated model framework is required to study spatial pricing and competition. Future research can incorporate concrete spatial features to quantify the benefit of the pooling effect using operational and geographical data, potentially enriching the findings. Throughout the analysis, we allow platforms to choose any prices and wages to maximize profits. In practice, platforms may adopt a certain pricing scheme such as a fixed commission rate or a fixed wage level. A valuable direction for future research would be to explore the implications of a merger when platforms adhere to these pricing schemes. In addition, consistent with most observations, we consider two competing platforms in the premerger market. In this case, a merger will lead to a monopoly in the postmerger market. There exist scenarios in which there are two or more service platforms after a merger. Future research can explore a market setting where a merged company may still compete with other platforms. We believe that this area presents many interesting questions for future research.

## Acknowledgments

The authors sincerely appreciate the constructive guidance, comments, and suggestions from the senior editor Giri Kumar Tayi, the associate editor Jianqing Chen, and the three anonymous reviewers throughout the review process.

## Endnotes

<sup>1</sup> However, peer-to-peer rental platforms (e.g., Airbnb), crowdsourcing platforms (e.g., CrowdSpring and 99design), and traditional consumer-to-consumer platforms (e.g., Taobao and eBay) are beyond the scope of our research, because for these platforms, prices or wages are not typically set by platform operators and matching does not necessarily need to be fast.

<sup>2</sup> A few papers consider the merger between two-sided platforms that charge fees to users on both sides (e.g., Chandra and Collard-Wexler 2009, Correia-da Silva et al. 2019). However, on-demand service platforms charge prices for customers, but pay wages to agents, and feature a within-side congestion effect.

<sup>3</sup> More specifically, in their single-homing setting, each agent is dedicated to a certain platform; in the multihoming setting, all agents serve on both platforms. Hence, in both cases, platforms are not competing for agents.

<sup>4</sup> See, e.g., https://www.businessinsider.com/guides/tech/how-tocancel-postmates-order (accessed September 30, 2023). Recall that we focus on a short time frame. So, in the long term, customers can be multihoming in the sense that they are free to register on both platforms, but in the short term, they can make only one request fo service due to cancellation fees.

5 Agents are restricted to single-homing for many practical reasons. For example, in Singapore, agents are constrained by exclusivity arrangements, such that they can only provide service on one ride hailing platform (Iwamoto 2018). On-demand food delivery platforms in China require agents (i.e., “drivers”) to work exclusively for one platform (see, e.g., Hersey 2018). Besides, platforms often run loyalty programs to make agents better off working for one platform continuously (Gridwise 2021).

<sup>6</sup> Ride-hailing platforms in practice often set a commission rate instead of explicitly setting a wage rate. In our model, having $p _ { i }$ and w as decision variables is equivalent to letting platforms determine a service price p along with a commission rate $( p _ { i } - w _ { i } ) / p _ { i }$

<sup>7</sup> An alternative interpretation of the two-location postmerger model is that the postmerger firm combines two apps as one, but continues to offer the features previously available in both apps. In this case, although only one app exists after a merger, customers and agents will still enjoy the features that best suit their preference—that is, choose either zero or one on the Hotelling line that maximizes their utility. For instance, agents will opt for their preferred payment methods if both payment options, previously offered by the two plat forms, remain available after a merger.

<sup>8</sup> The expressions of $v _ { w 1 } , v _ { w 2 } ,$ , and $v _ { w 3 }$ are provided in Online Appendix A.

<sup>9</sup> We say A is more likely to be larger (smaller) than B if the parameter range in which $A > B \left( A \leq B \right)$ becomes larger.

<sup>10</sup> Per the expressions of customer price sensitivity in Lemma $^ { 3 , }$ $s _ { f } = - ( 2 t + 2 \bar { b \theta } N - 2 b K \mu \partial k _ { i } / \partial n _ { i } ) ^ { - 1 } , s _ { p } = - ( t + b \theta N - b K \mu \partial k _ { i } / \partial n _ { i } ) ^ { - 1 } ,$ and $s _ { m } = - \left( \frac { t } { 2 } + b \theta N - b K \mu \partial k _ { m } / \partial n _ { m } \right) ^ { - 1 }$ are all increasing in θ, imply ing that demand becomes less sensitive to an increase in price. Moreover, the congestion effect (i.e., the term with θ) carries a greater weight relative to the direct pricing effect $( \mathrm { i . e . }$ , the first term with t) in the postmerger price sensitivity $s _ { m }$ than that in the premerger counterparts s<sub>f</sub> and $s _ { p } .$

<sup>11</sup> For example, one can think of the η proportion of agents as techsavvy agents that always opt for simultaneously using two mobile apps to serve on both platforms, whereas the 1 � η proportion of agents always focus on one platform due to a prohibitively high hassle cost.

<sup>12</sup> The regularity conditions (v is sufficiently large and $N > K \mu / 2 )$ are required to ensure the platforms’ payoff functions are well behaved.

## References

Abhishek V, Guajardo JA, Zhang Z (2021) Business models in the shar ing economy: Manufacturing durable goods in the presence of peer-to-peer rental markets. Inform. Systems Res. 32(4):1450–1469.

Abkowitz A, Carew R (2016) Uber sells China operations to Didi Chuxing. Wall Street J. (August 1), https://www.wsj.com/articles/ china-s-didi-chuxing-to-acquire-rival-uber-s-chinese-operations 1470024403.

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Armstrong M, Wright J (2007) Two-sided markets, competitive bot tlenecks and exclusive contracts. Econom. Theory 32(2):353–380.

Bai J, Tang CS (2022) Can two competing on-demand service plat forms be profitable? Internat. J. Production Econom. 250:108672.

Bai J, So KC, Tang CS, Chen XM, Wang H (2019) Coordinating supply and demand on an on-demand service platform with impatient customers. Manufacturing Service Oper. Management 21(3): 556–570.

Benjaafar S, Xiao S, Yang X (2020) Do workers and customers benefit from competition between on-demand service platforms? Working paper, University of Minnesota, Minneapolis.

Benjaafar S, Ding JY, Kong G, Taylor T (2021) Labor welfare in on-demand service platforms. Manufacturing Service Oper. Man agement 24(1):110–124.

Bernstein F, DeCroix GA, Keskin NB (2021) Competition between two-sided platforms under demand and supply congestion effects. Manufacturing Service Oper. Management 23(5):1043–1061.

Bimpikis K, Candogan O, Saban D (2019) Spatial pricing in ride sharing networks. Oper. Res. 67(3):744–769.

Cachon GP, Daniels KM, Lobel R (2017) The role of surge pricing on a service platform with self-scheduling capacity. Manufactur ing Service Oper. Management 19(3):368–384.

Caillaud B, Jullien B (2003) Chicken & egg: Competition among intermediation service providers. RAND J. Econom. 34(2):309–328.

Campbell H (2023) DoorDash vs Uber Eats: Which app is better for drivers? Accessed September 30, 2023, https://therideshareguy. com/doordash-vs-uber-eats.

Catala˜o-Lopes M, Brito D (2021) Post-merger internal organization in multitier decentralized supply chains. J. Econom. 132(3): 251–289.

Chandra A, Collard-Wexler A (2009) Mergers in two-sided markets: An application to the Canadian newspaper industry. J. Econom. Management Strategy 18(4):1045–1070.

Chen Y, Hu M (2020) Pricing and matching with forward-looking buyers and sellers. Manufacturing Service Oper. Management 22(4):717–734.

Cho SH (2013) Horizontal mergers in multitier decentralized supply chains. Management Sci. 60(2):356–379.

Cho SH, Wang X (2017) Newsvendor mergers. Management Sci 63(2):298–316.

Cohen MC, Zhang R (2022) Competition and coopetition for twosided platforms. Production Oper. Management 31(5):1997–2014.

Correia-da Silva J, Jullien B, Lefouili Y, Pinho J (2019) Horizontal mergers between multisided platforms: Insights from Cournot competition. J. Econom. Management Strategy 28(1):109–124.

Dealroom (2018) Takeaway.com acquires Delivery Hero Germany: A closer look. Accessed September 30, 2023, https://dealroom. co/blog/after-delivery-hero-takeaway-com-deal-whats-next-in food-delivery-tech.

Doyle R (2023) Uber Eats vs. Postmates: Comparison for users and drivers. Accessed September 30, 2023, https://apporbit.com ubereats-vs-postmates-comparison.

Farrell J, Shapiro C (1990) Horizontal mergers: An equilibrium anal ysis. Amer. Econom. Rev. 80(1):107–126.

Feng G, Kong G, Wang Z (2021) We are on the way: Analysis of on-demand ride-hailing systems. Manufacturing Service Oper. Management 23(5):1237–1256.

Gandotra S (2020) Here’s what Uber acquisition over Postmates means to entrepreneurs. Accessed September 30, 2023, https:// www.code-brew.com/heres-what-uber-acquisition-over-postmates means-to-entrepreneurs/.

Gavazza A, Lizzeri A (2009) Transparency and economic policy. Rev. Econom. Stud. 76(3):1023–1048.

Gridwise (2021) Uber vs. Lyft: Which is better for rideshare drivers? Accessed September 30, 2023, https://gridwise.io/uber-vs-lyft which-is-better-for-rideshare-drivers.

Hagiu A (2006) Pricing and commitment by two-sided platforms RAND J. Econom. 37(3):720–737.

Hagiu A (2009) Two-sided platforms: Product variety and pricing structures. J. Econom. Management Strategy 18(4):1011–1043.

Han W, Wang X, Ahsen ME, Wattal S (2022) The societal impact of sharing economy platform self-regulations—An empirical investigation. Inform. Systems Res. 33(4):1303–1323.

Hao L, Guo H, Easley RF (2017) A mobile platform’s in-app advertising contract under agency pricing for app sales. Production Oper. Management 26(2):189–202.

Hart O, Tirole J, Carlton DW, Williamson OE (1990) Vertical integration and market foreclosure. Brookings Pap. Econom. Act. Microeconom. 1990:205–286.

Helling B (2023) Postmates Uber Eats merger: Bringing two giants together. Accessed September 30, 2023, https://www.ridester. com/postmates-uber-eats/.

Hersey F (2018) Didi Waimai claims to have become Wuxi’s top food delivery service on first official day. TechNode (April 11), https://technode.com/2018/04/11/didi-wuxi/.

Hotelling H (1929) Stability in competition. Econom. J. 39(153):41–57.

Hu B, Hu M, Zhu H (2021) Surge pricing and two-sided temporal responses in ride hailing. Manufacturing Service Oper. Manage ment 24(1):91–109.

Iwamoto K (2018) Singapore allows Uber’s exit with antimonopoly measures. Nikkei (April 13), https://asia.nikkei.com/Business/ Companies/Singapore-allows-Uber-s-exit-with-antimonopolymeasures.

Kleinberg J, Tardos E (2005) Algorithm Design (Pearson, London).

Li X, Liu Q (2020) Contract unobservability and downstream competi tion. Manufacturing Service Oper. Management 23(6):1468–1482.

Lu T, Zheng Z, Zhong Y (2023) Maximizing the benefits of an on-demand workforce: Fill rate-based allocation and coordination mechanisms. Manufacturing Service Oper. Management 25(6):2216–2232.

McAfee RP, Schwartz M (1994) Opportunism in multilateral vertical contracting: Nondiscrimination, exclusivity, and uniformity. Amer. Econom. Rev. 84(1):210–230.

Nikzad A (2020) Thickness and competition in on-demand service platforms. Working paper, University of Southern California, Los Angeles.

Perry MK, Porter RH (1985) Oligopoly and the incentive for hori zontal merger. Amer. Econom. Rev. 75(1):219–227.

PYMNTS (2023) Getaround acquires HyreCar to strengthen carsharing business. PYMNTS (May 15), https://www.pymnts.com acquisitions/2023/getaround-acquires-hyrecar-to-strengthencarsharing-business/.

Rochet JC, Tirole J (2003) Platform competition in two-sided mar kets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rochet JC, Tirole J (2006) Two-sided markets: A progress report. RAND J. Econom. 37(3):645–667.

Russell J (2018) It’s official: Uber sells Southeast Asia business to Grab. Techcrunch (March 25), https://techcrunch.com/2018/03/ 25/gruber-official/.

Rysman M (2009) The economics of two-sided markets. J. Econom. Perspect. 23(3):125–143.

Segal I (1999) Contracting with externalities. Quart. J. Econom. 114(2):337–388.

Stigler GJ (1950) Monopoly and oligopoly by merger. Amer. Econom. Rev. 40(2):23–34.

Taylor TA (2018) On-demand service platforms. Manufacturing Ser vice Oper. Management 20(4):704–720.

Whinston MD (2007) Antitrust policy toward horizontal mergers. Armstrong M, Porter R, eds. Handbook of Industrial Organization, vol. 3 (Elsevier, Amsterdam), 2369–2440.

Williamson OE (1968) Economies as an antitrust defense: The wel fare tradeoffs. Amer. Econom. Rev. 58(1):18–36.

Wu S, Xiao S, Benjaafar S (2020) Two-sided competition between on-demand service platforms. Working paper, Hong Kong Polytechnic University, Hong Kong.

Yu JJ, Tang CS, Max Shen ZJ, Chen XM (2020) A balancing act of regulat ing on-demand ride services. Management Sci. 66(7): 2975–2992

Zervas G, Proserpio D, Byers JW (2017) The rise of the sharing economy: Estimating the impact of Airbnb on the hotel industry. J. Marketing Res. 54(5):687–705.

Zhang C, Chen J, Raghunathan S (2022) Two-sided platform competition in a sharing economy. Management Sci. 68(12):8909–8932.

Zhang C, Chen J, Raghunathan S (2024) When sharing economy meets traditional business: Coopetition between ride-sharing platforms and car-rental firms. Inform. Systems Res. 35(3):1137–1153.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
