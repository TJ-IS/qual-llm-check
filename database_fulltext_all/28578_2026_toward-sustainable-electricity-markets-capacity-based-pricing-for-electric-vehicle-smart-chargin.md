---
otero_id: 28578
otero_key: "2VUSBQ36"
title: "Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging"
authors: "Konstantina Valogianni; Wolfgang Ketter; John Collins; Gediminas Adomavicius"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0078"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/2VUSBQ36/fulltext/images/f2b3dbc767bf9d010604ce7147deea84f73c46c4ca47c0e982fdef3dcf17c382.jpg)

# Toward Sustainable Electricity Markets: Capacity-Based Pricing for Electric Vehicle Smart Charging

Konstantina Valogianni,<sup>a,</sup>\* Wolfgang Ketter,<sup>b</sup> John Collins,<sup>c</sup> Gediminas Adomavicius<sup>d</sup>

<sup>a</sup> Department of Information Systems and Technology, IE Business School – IE University, 28006 Madrid, Spain; <sup>b</sup> Faculty of Management, Economics and Social Sciences, University of Cologne, 50923 Cologne, Germany; <sup>c</sup> Department of Computer Science, University of Minnesota Minneapolis, Minnesota 55455; <sup>d</sup> Department of Information and Decision Sciences, University of Minnesota, Minneapolis, Minnesota 55455 \*Corresponding author

Contact: Konstantina.Valogianni@ie.edu, https://orcid.org/0000-0001-6419-8675 (KV); ketter@wiso.uni-koeln.de,

https://orcid.org/0000-0001-9008-142X (WK); jcollins.cs@gmail.com (JC); gedas@umn.edu (GA)

Received: February 11, 2023

Revised: December 11, 2024

Accepted: May 12, 2025

Published Online in Articles in Advance: June 24, 2025

https://doi.org/10.1287/isre.2023.0078

Copyright: © 2025 The Author(s)

Abstract. We present a novel information systems (IS)-enabled pricing artifact for variablerate electric vehicle (EV) charging that can facilitate a sustainable EV introduction. EVs can significantly reduce carbon intensity in modern cities and address important sustainability challenges. However, large-scale EV introduction is expected to increase electricity demand peaks, threatening grid stability and reliability. Most proposed methods to coordinate EV charging have shortcomings, such as the inability to guarantee incentive alignment between grid and EV owner objectives, or avalanche effects, which might create new demand peaks as EV owners receive the same price signals and make similar charging decisions. To address this issue, we present a capacity-based pricing artifact that includes a dynamic, charging-rate-based price component and a set of price-setting methods based on analytical or computational heuristics. The proposed approach benefits from a variety of available information in the environment and allows rational EV agents to optimize their own costs through planning and scheduling in the presence of their individual charging needs and constraints, while at the same time rebalancing the total charging demand to mitigate avalanche effects in EV charging. The proposed artifact is highly effective in reducing demand volatility or, alternatively, in achieving a desired match between the output of renewable energy sources and overall charging demand. We demonstrate the benefits of the proposed approach empirically, by comparing it to traditional, currently used pricing benchmarks in several realistic scenarios. Our artifact supports grid operators in their effort to rebalance the overall EV charging demand across time. Furthermore, the proposed approach enables energy providers to maintain the overall revenues (i.e., to achieve rebalancing without changing the total charging cost for the same energy needs), while respecting marketimposed price constraints. Finally, energy market stakeholders can use our pricing scheme to induce demand profiles that follow renewable generation patterns, maximizing renewable usage and reducing inefficiencies in renewable energy utilization by the grid.

History: Gautam Pant, Senior Editor; Ning Nan, Associate Editor.

CO Open Access Statement: This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. You are free to download this work and share with others but cannot change in any way or use commercially without permission, and you must attribute thi work as “Information Systems Research. Copyright © 2025 The Author(s). https://doi.org/10.1287/ isre.2023.0078, used under a Creative Commons Attribution License: https://creativecommons.org licenses/by-nc-nd/4.0/.”

Funding: This work was supported by the Ramon Areces Foundation, Spain. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0078.

Keywords: Green IS • IS artifact • electric vehicles • sustainability • intelligent agents • energy informatics • smart markets • design science

## 1. Introduction

Modern cities are being transformed into smart environments where large volumes of data are being produced and transmitted (Ismagilova et al. 2019). One of the necessities in smart cities is to reduce carbon intensity and increase availability of transport to citizens (Brandt et al. 2018b). Electric vehicles (EVs) are becoming popular in smart cities because they have potential to significantly reduce carbon intensity in transportation systems (International Energy Agency 2017, Wu et al. 2019). The Paris Declaration on Electro-Mobility and Climate Change has set a target of 100 million EVs by 2030 (United Nations Framework Convention on Climate Change 2015), whereas the global number of EVs grew by 108% in 2021,<sup>1</sup> surpassing 11 million worldwide (International Energy Agency 2021). However, large-scale introduction of EVs into current electricity grids will pose important stability challenges that information systems (IS) research can address (Ketter et al. 2023).

Current electricity grids are not designed to support the load of large numbers of EVs charging their batteries during the early evening hours (Verzijlbergh et al. 2012), when electricity demand typically peaks because of energy-intensive household activities like cooking and cleaning (Ipakchi and Albuyeh 2009). EV chargers are the highest-power electrical load in most households, and they normally run for extended periods. Traditiona approaches to address this challenge are either investing in additional grid infrastructure (copper cables, etc.) to accommodate the extra peak demand coming from EVs (International Energy Agency 2017) or offering lower energy prices in exchange for allowing the grid operator to disable chargers during high-demand periods. Solving this problem through grid upgrades is very costly<sup>2</sup> and unsustainable (Watson et al. 2010), as the additional peak demand would almost certainly require installation of large numbers of new peak load generation units, such as low-efficiency fast-response gas turbines.

Current solutions to address the EV charging coordination challenge have shortcomings, mostly rooted in their inability to achieve incentive alignment between grid operators and electricity customers, often resulting in avalanche effects. An avalanche effect is the phenomenon of having similar customer responses to variable pricing schemes, creating congestion and new peaks in electricity demand during the low-price periods. This avalanche effect has been observed in the electricity pricing and EV charging literature (Gottwalt et al. 2011, Dallinger and Wietschel 2012, Krause et al. 2015, Akasiadis and Chalkiadakis 2016, Ensslen et al. 2018, Valogianni et al. 2020) as well as real-world pricing pilots (Schey et al. 2012), and can exacerbate demand peaks instead of alleviating them.

The advancement of technological solutions in electricity markets is converting electricity markets into smart markets where computational intelligence can support humans in making more informed decisions (Bichler et al. 2010). Leveraging this “smartness,” we respond to the calls in the IS literature for designing smart market decision support (Bichler et al. 2010, Ismagilova et al. 2019, Ketter et al. 2020) by introducing an IS-enabled pricing solution that can coordinate EV charging in a way that minimizes stress on the electrical grid and makes the best use of available renewable energy. The proposed pricing scheme leverages customer self-interest to induce desired demand profiles with low computational complexity, while meeting revenue targets and requiring only one-way communication of price parameters from energy supplier to participating EV chargers. The proposed approach does not put specific restrictions on the desired demand profiles; for example, they can be flat, matching a predicted energy generation pattern, etc.<sup>3</sup> In particular, we pro pose a pricing mechanism in which energy (kWh) prices have a component that is a function of charging rate or power (kW). This pricing mechanism lies at the core of the proposed solution. In the rest of this paper, we use the term capacity-based pricing (CBP) to refer to this charging-rate-based approach, because the rate at which an EV charger consumes electricity determines the grid capacity that will be utilized for this charging (Nicholas and Hall 2018). In other words, the EV charging rate is directly associated with the grid capacity, which is an important determinant in the grid stakeholders’ and policy makers’ efforts to prevent grid disruptions, such as blackouts (Leemput et al. 2015). Importantly, we use capacity-based pricing in combination with information available in smart electricity markets to propose a set of price-setting methods (based on analytical and compu tational heuristics) that satisfy stakeholder objectives, outperforming well-established benchmarks and induc ing near-optimal outcomes with low computational complexity. From the design science research perspective, our study can be considered as an example of the “Improvement” category, defined by Gregor and Hevner (2013) as contributions that develop new solutions for known problems. Our solution aims to overcome existing limitations, such as grid-balancing challenges due to avalanche effects exhibited by a number of benchmark approaches, advancing the solution maturity via novel designs and efficient computational, data-driven capabilities. We also provide an extensive evaluation of our artifact in a simulation environment calibrated with real-world data, measuring its impact based on predefined, domain-relevant metrics (Peffers et al. 2007, Venable et al. 2016).

The proposed approach offers several advantages to stakeholders. In particular, grid operators can benefit by reducing demand peaks and maintaining uninterrupted functionality of the grid. Most importantly, depending on the information available and the level of tempora granularity required, the proposed solution offers suitable options to satisfy grid operators’ objectives. At the same time, policy makers interested in sustainability may use our solution to shape demand to better match the output of renewable sources, so that their renewable capacity investment becomes more cost-effective (Hu et al. 2015). Consequently, our work can help increase societal sustainability in two ways. First, it can help facilitate large-scale adoption of EVs (Fridgen et al. 2014a), which is essential for reducing our collective carbon footprint as called for in the UN Paris Agreement (United Nations Framework Convention on Climate Change 2015). Second, it can reduce the need for additional grid capacity which is costly and unsustainable (Watson et al. 2010).

As a result, the contribution of this work, in addition to smart markets and smart cities literature (Bichler et al.

2010; Ketter et al. 2016a, 2020; Ismagilova et al. 2019), lies in Green IS, a growing area of IS that aims for sustainable environmental impact through the use of information systems (Melville 2010, Watson et al. 2010, Loock et al. 2013, Malhotra et al. 2013, Seidel et al. 2013, Ketter et al. 2016b, Loeser et al. 2017, Brendel et al. 2018). According to the main principles of Green IS, the use of information systems can lead to more efficient energy consumption, and IS researchers can be leaders in this effort (Watson et al. 2010). Aligning with this key Green IS objective, we design an artifact (a pricing scheme and price-setting heuristics) that benefits from information available to the stakeholders, and with minimal intervention and low computational complexity can induce EV charging behavior that is more favorable for the grid. Supporting the grid and facilitating renewable source integration lead to more efficient energy consumption and achieve a positive impact on the environment.

To illustrate this, we follow and adapt the Green IS framework proposed by Watson et al. (2010) to our specific problem setting, as shown in Figure 1. The figure summarizes how, in addition to the central piece—a novel capacity-based pricing scheme that is capable of providing the advantageous coordination between energy providers and consumers—the proposed solution is supported by two additional key IS-based elements. On the energy provision side, the proposed solution provides analytical as well as computational, data-driven price-setting heuristics, which strive to satisfy the eco-objectives of the grid stakeholders and are able to achieve near-optimal results with very low computational complexity. On the energy consumption side, the proposed solution relies on the presence and abilities of intelligent software agents that can facilitate the charging behavior that ensures the satisfaction of the consumer objectives and preferences.

## 2. Background

## 2.1. Green IS and Smart Sustainable Mobility

Green IS (Melville 2010, Watson et al. 2010, Loock et al. 2013, Malhotra et al. 2013, Seidel et al. 2013, Ketter et al. 2016b, Loeser et al. 2017) is a subfield of IS that deals with the role of IS in improving environmental sustainability. The Green IS research umbrella spans both theoretical and empirical studies, having as a common objective the use of information technology (IT) to improve societal sustainability or to establish sustainability as a core principle for firms and business processes (Dao et al. 2011). Our work responds to the call for designing smart sustainable mobility artifacts leveraging the unique position of the IS discipline at the intersection of the physical and digital layers of smart grids (Ketter et al. 2023). Following Ketter et al. (2023), the proposed approach addresses the research opportunity “Design of Mobility Demand Response Incentives and Nudging Strategies,” and our contribution falls into their specific research question “How should effective mobility demand response interventions be designed to steer user behavior in a system-beneficial manner (e.g., via time-shifting)?” Methodologically, we employ design science approaches to create incentives that are able to “elicit certain charging behaviors” in the context of EV charging. Following the research directions advocated by Melville (2010), the main affordances (Seidel et al. 2013) of our artifact relate to mitigating peak demand resulting from EV charging and, consequently, supporting grid stability and increasing sustainability levels, by reducing the need for additional infrastructure or increasing the use of renewable energy (Dedrick 2010). Similar IS artifacts have been proposed in other contexts such as microgrids (Brandt et al. 2014), smart homes (Brandt et al. 2013, Valogianni et al. 2014), carbon management systems (Corbett 2013), or energy demand side management (Gottwalt et al. 2011, Fridgen et al. 2014b).

Figure 1. Green IS Framework of This Study (Following Watson et al. 2010)  
![](/api/attachments/2VUSBQ36/fulltext/images/4f25d1a96034cace1a43250a517c935a8fea538982b0fb4d48f48ed53827746c.jpg)

In the context of EVs, Green IS research has examined different aspects of increasing sustainability levels, similarly to our work. For example, Brandt et al. (2018a) present an IS framework to discover synergies between EVs and renewable sources so that the grid benefits and sustainability levels increase. Another example is the work by Klo¨ r et al. (2018) that presents a decision support system (DSS) which facilitates repurposing of EV batteries, contributing to the conservation of raw materials—a crucial determinant of sustainability. A number of related issues have been explored in the Green IS literature with the goal of increasing sustainability (Benitez-Amado and Walczuch 2012; Seidel et al. 2013; Ketter et al. 2016b, 2018; Rieger et al. 2016; Loeser et al. 2017). Taking a more general perspective, vom Brocke et al. (2013) propose new directives for the IS discipline in establishing sustainability as the main principle in the way businesses operate. We respond to this call, demonstrating how the design of artifacts can contribute to solving sustainability problems (e.g., increasing the use of renewable sources and mitigating the need for additional grid infrastructure), outperforming current solutions and opening new paths for Green IS.

## 2.2. EV Charging Coordination

Our objective is a more flexible EV charging coordination mechanism that overcomes current shortcomings. EV charging coordination mechanisms can be categorized as centralized (top-down) or decentralized (bottomup). Top-down coordination mechanisms typically have a global objective, such as reducing overall demand peaks in the grid (Papadopoulos et al. 2013, Vandael et al. 2013, Hu et al. 2014). They might vary with respect to the type of the grid operator’s objective function and the means by which they exert control over individual charging units. One category of centralized mechanisms focuses on preventing grid congestion,<sup>4</sup> potentially compensating users for inconveniences caused (Papadopoulos et al. 2013, Vandael et al. 2013, Hu et al. 2014, Hajforoosh et al. 2015, Masoum et al. 2015, Jiang and Powell 2016). In general, preventing congestion is equivalent to managing peak demand within the capacity constraints of the grid or its segments. Another category of congestion prevention or reduction approaches is focused on providing incentives so that the overall demand peaks are reduced (Mocci et al. 2014, Zhang et al. 2015, Hafez and Bhattacharya 2016, Yao et al. 2017). Pricing mechanisms can be used as signals to electricity customers (Li 2007, Flath et al. 2013, Hu et al. 2016b, Kim and Giannakis 2016) to shape electricity demand. Auction mechanisms for EV charging (Gerding et al. 2011, De Craemer et al. 2014, Stein et al. 2017, Kahlen et al. 2018) are another type of centralized coordination. See Section 2.3 for a more detailed literature review on pricing mechanisms for EV charging.

Furthermore, centralized EV charging coordination has been proposed to regulate important grid stability and reliability parameters, such as the grid frequency and voltage (Wen et al. 2012, Gan et al. 2013, Zhong et al. 2014, Liu et al. 2016a, Tan and Wang 2016). A major ben efit of top-down coordination mechanisms is that they can easily satisfy the constraints imposed by the grid manager, leading to a balanced system. However, there are significant shortcomings. The most important challenge is that many of these approaches require the coordinator to exogenously control EV chargers (Hu et al. 2016a),<sup>5</sup> potentially violating the EV driver’s preferences and leading to inconvenience and loss of autonomy. In general, there is no reason to expect a global objective to align with the preferences of individual EV drivers. Furthermore, the majority of these mechanisms require direct control of EV chargers, which could also mean significant investment in communication and control infrastructure (Hu et al. 2016a).

Bottom-up mechanisms focus on individual customers, aiming to satisfy local objectives, such as minimizing electricity cost, and, if widely adopted, can affect the overall demand profile on the grid (Li 2007, Flath et al. 2013). These mechanisms typically do not violate individual preferences, but there is no guarantee that the individual objectives are aligned with the grid’s globa objective. One category of decentralized mechanisms is cooperative mechanisms, which assume that the EV customers are cooperating, trying to satisfy their own objectives but also to achieve an overall community objective (Akasiadis and Chalkiadakis 2016, Rieger et al. 2016, Robu et al. 2016). Other coordination mechanisms attempt to reduce peak load or offer regulation services (Beaude et al. 2013, Zhang et al. 2014, D’hulst et al. 2015). Grid operators may also attempt to use prices to influence EV charging decisions (Fridgen et al. 2014b), but because the same price signals are provided to all customers, their EV charging schedules are likely to be correlated. Specifi cally, if EV agents are cost-minimizers, they will shift their demand to the cheapest time periods, creating new peaks—that is, resulting in avalanche effects.

Such avalanche effects have been identified in the literature (Gottwalt et al. 2011, Dallinger and Wietschel 2012, Schey et al. 2012, Krause et al. 2015, Akasiadis and Chalkiadakis 2016, Ensslen et al. 2018, Wu et al. 2019, Valogianni et al. 2020), and there have been some attempts to mitigate them via blockchain architectures (Akasiadis and Chalkiadakis 2016) or via an intermediary between the grid and EV drivers that controls the charging (Ensslen et al. 2018). In addition, Wu et al. (2022) present an iterative smart charging method that aims at scheduling EV charging to meet an exogenous demand, while respecting private delay sensitivity constraints. Valogianni et al. (2020) present an adaptive pricing method that observes the EV driver reactions to broadcast prices and adjusts the prices accordingly.

However, these solutions are computationally more complex or require access to more information, compared with the approach we describe in this work. The proposed approach combines the decentralized decision making on the rational, self-interested EV owner side with a central coordination party that aims to induce a desired aggregate charging profile, mitigating the shortcomings that arise in purely centralized or purely decentralized mechanisms; for example, our artifact does not violate consumer preferences or constraints (neither attempts to change them) and at the same time is able to mitigate the avalanche effects. In addition, our approach—with its ability to perform well without many iterations—can adapt faster to rapidly changing, real-world environments.

## 2.3. Pricing Mechanisms for EV Charging

Pricing is one of the most popular methods used to coordinate EV charging toward certain objectives, such as grid balancing. Here, we provide an overview of different pricing mechanisms that are used for EV charging. We examine the advanced pricing mechanisms that aim to alleviate peaks in the demand, omitting the static time-of-use or flat pricing approaches. For an extensive review on pricing for EV charging, refer to the work by Limmer (2019).

First, we discuss the related work that assumes a form of iterative learning in order to adjust the EV prices advantageously for the grid and EV drivers. For example, Alizadeh et al. (2016) propose the use of conventional electricity prices (specified in monetary units/ kWh) adjusted with a “congestion factor” to coordinate EV charging. Their approach, while being effective, appears to be quite computationally intensive, requiring multiple iterations to achieve its full potential. In this stream of work, a popular approach is the use of traditional energy prices (monetary units/kWh) to coordinate EV charging, in combination with reinforcement learning methods or genetic algorithms (GAs) to better adapt these prices to the population they are targeting (Limmer and Rodemann 2019, Fang et al. 2020, Gong et al. 2020, Moghaddam et al. 2020, Rasheed et al. 2020, Li et al. 2023). Although such approaches can be effective, they, again, require a number of iterations for GAs to converge to the optimal policy. In a similar vein, several studies propose the adjustment of time-of-use prices using either GAs or other greedy heuristics (Tucker and Alizadeh 2018, Xu et al. 2020, Liang et al. 2023). Such heuristics might need between 20 and 100 days (iterations) to converge to the desired prices, making them more practically challenging. Lee and Choi (2021), Liu et al. (2021), and Wang et al. (2022) propose different deep reinforcement learning methods to learn and adjust real-time prices for EV charging scheduling. As before, such an approach requires substantial computational resources to be trained and converge to the desired outcome. Mrkos et al. (2018) and Huang et al. (2023) devise Markov Decision Processes (MDP)-based strategies to iteratively shape electricity prices so that grid and EV owner objectives are matched. Along the lines of the work discussed in this paragraph, these iterative processes increase computational complexity and do not allow for instantaneous decision making. For a more complete view of the use of different machine learning techniques to adjust EV charging prices, we direct the reader to the work by Fescioglu-Unver and Aktas¸ (2023).

Second, we discuss academic literature that makes assumptions about the EV owners’ price responsiveness in order to optimally set EV charging prices. For example, Soltani et al. (2015) assume the adjustment of electricity prices for EV charging based on the responsiveness of EV owners to the prices. As a result, such a pricing mechanism proposes an iterative learning component that can be computationally intensive. Lin et al. (2021) propose the use of a sigmoid function with adjustable parameters, as a proxy for price elasticity, combined with electricity prices to coordinate EV charging. However, similarly to previous approaches, it requires Particle Swarm Optimization methods to determine the optimal parameterization, leading once more to higher computational complexity. Yoon et al. (2015) and Dai et al. (2021) make some assumptions about the utility function of EV owners and, using iterative games, try to get to optimal electricity prices that satisfy grid and EV objectives at the same time. Zhang et al. (2020) propose a dynamic version of time-of-use pricing that gets adjusted based on an assumed degree of EV driver’s satisfaction. Santoyo et al. (2023) assume an impatience factor and other characteristics of user behavior in order to set prices for different levels of EV charging. However, in all cases, such prices are static and depend on the user behavior assumptions. In summary, we observe that this stream of literature requires some sub stantial specific assumptions about the way consumers respond, in addition to cost-minimization objectives.

Third, we examine the related work that deals with different types of pricing structures to coordinate EV charging. For instance, Yan et al. (2014) present a multitiered real-time pricing mechanism to coordinate EV charging. This method adjusts the prices during different times of the day based on the existing grid congestion. While being effective in mitigating peak demand, such a pricing method is not flexible enough to induce demand profiles of an arbitrary shape. In a similar way, Xiong et al. (2016) propose a congestion component added onto the existing electricity prices and, using game theory, they iteratively get to the optimal prices. Such an approach computes the prices faster, yet it still requires iterative processes to converge to the optimal outcome. Along similar lines, Zanvettor et al. (2022) present a pricing algorithm that adjusts the selling price of electricity for EV charging using an iterative algorithm.

This algorithm requires approximately 20 iterations to yield the optimal policy. Hu et al. (2016b) present a pricing mechanism to fill “valleys” in the electricity demand faced by the grid. This mechanism operates in an iterative fashion, but it is only suitable for flat demand profiles.

A special subcategory of pricing structures for EV charging is locational marginal pricing approaches. Such approaches are powerful in balancing the grid by setting prices depending on the grid congestion in each location. Different variations of locational marginal pricing have been proposed in the literature (Flath et al. 2013, Li et al. 2014, Liu et al. 2016b, Canizes et al. 2019), but their main objective is to induce flat demand profiles, without having the flexibility to induce profiles of an arbitrary shape with low computational complexity.

In summary, the existing literature has made progress on using conventional energy prices for grid-balancing objectives by restricting the problem/solution settings in the following ways: (a) relying on the presence of a substantial iterative/learning component that helps the prices converge to an optimum that satisfies grid objectives; (b) assuming certain behavioral characteristics of EV owners besides their rational, cost-minimization objectives; (c) assuming the desired demand profiles are flat or of certain (highly restricted) type. Our work addresses these challenges by offering a different pricing artifact that does not require numerous, timeconsuming learning iterations or extra knowledge about the reaction of EV owners to prices. As such, one of the key benefits of our approach is that it is able to adapt quickly to rapidly changing real-world environments. In addition, our artifact is able to induce any form of demand profile and balance the revenues associated with the broadcast prices. One core component of the proposed mechanism is the capacity-based pricing. We design our capacity-based pricing approach by building on general nonlinear pricing ideas introduced in the literature (Schweppe et al. 1988, Gottwalt 2015), and provide further contributions by systematically examining the theoretical properties and price-setting mechanisms of such an approach. In particular, we derive the conditions for inducing a desired profile and meeting revenue targets using the proposed pricing. As such, our work proposes a comprehensive IS-based artifact that (i) uses analytical price-setting heuristics derived by understanding certain theoretical properties of the proposed pricing mechanism; (ii) uses computational price-setting heuristics to leverage the observed charging behavior to further improve grid-balancing outcomes; and (iii) provides built-in revenue balancing capabilities, an important component that makes the proposed pricing scheme adaptable to various real-world economic environments. We extensively evaluate our mechanism in diverse scenarios using a simulation calibrated with real-world data. We demonstrate that our approach substantially outperforms a set of representative benchmarks from prior literature. The benefits of our mechanism rely on the highly advantageous price parameterization offered by our analytical and computational heuristics, which represent a key differentiating factor. We also show that our method retains its significant advantages even in scenarios with less “rational” (i.e., less planning-oriented) populations.

## 3. Proposed Approach: Capacity-Based Pricing

We adopt the viewpoint of a smart grid operator or energy provider who would like to reshape existing electricity demand over time toward a desired profile (e.g., to ensure grid reliability), such as a flat demand profile or a production pattern of a renewable source. This is known as load balancing (or grid balancing) and is a key goal of grid operators (Freitas and Brito 2019, Al-Ghussain et al. 2021). One common approach toward achieving this goal is for the grid operators to use price signals to communicate with EV owners and incentivize desired consumption behavior. We follow the pricingbased idea, and our problem setting involves two types of participants:

1. A smart grid operator who wants to manage capacity investment by redistributing peak demand or who wants to reshape existing demand over a specific time horizon (e.g., a day or a week) to follow the generation profile of renewable sources, while meeting a revenue target, and

2. EV owners who receive price signals and modify their EV charging to satisfy their preferences, including minimizing cost and the risk of running out of battery charge.

One of the key components of the proposed IS-enabled pricing solution is the presence of the intelligent agents (Wooldridge and Jennings 1995), which are software agents representing EV owners and to which EV charging-related tasks can be effectively and reliably delegated. Such agents can be installed on the user’s mobile device (similar to the ones presented by NewMo tion,<sup>6</sup> Enel,<sup>7</sup> or Eneco<sup>8</sup>) or even be part of the EV’s internal charging controller. Moreover, intelligent agents can help optimize EV charging based on EV owners’ preferences (Faruqui et al. 2011, Guo et al. 2014, Zhou et al. 2020, Das et al. 2021, Lagomarsino et al. 2022, Liu and Zhou 2022), such as expected driving needs/distances during the day as well as available times for charging. This input can be provided directly by the owner via some user interface or potentially learned by the agent directly from prior EV driving and charging activities.

## 3.1. Smart Grid Manager’s Objective

A grid operator or smart grid manager<sup>9</sup> desires to achieve a match between demand and supply and prevent blackouts. It acts by broadcasting price signals to

EV agents for a future horizon $T \in \mathbb { Z } ^ { + }$ (e.g., 24 h or 7 days), with $\mathbf { T } = \left\{ 1 , \ldots , T \right\}$ , to achieve a desired demand profile $\mathbf { D } = [ D _ { 1 } , \dots , D _ { T } ]$ . The time horizon T is discretized to time intervals t ∈ T that can have any size $\delta \neq 0$ (e.g., one hour) to meet the problem modeling needs (as small or large as required by the problem context).<sup>10</sup> Prices are broadcast to EV owners in the beginning of time horizon T and cover the whole planning horizon of the EV agent. At the end of the time horizon T, the prices can be adjusted by the grid operator and broadcast for the next horizon T.

The grid operator is represented by a control agent. Figure 2 provides an overview of the decision environment of the control agent (grid operator). The lightly shaded area indicates that the grid operator has no access to individual EV owner preferences or individual charging profiles. In other words, the grid operator is able to observe the EV agents’ aggregate demand $\mathbf { D ^ { 0 } } =$ $[ D _ { 1 } ^ { o } , \dots , D _ { T } ^ { o } ]$ as well as the overall EV charging need $\Phi =$ $\textstyle \sum _ { t = 1 } ^ { T } D _ { t } ^ { o }$ over time horizon T. The goal of the grid operator is to reshape this charging need Φ into the desired profile $\mathbf { D } = [ \bar { D _ { 1 } } , \dots , D _ { T } ]$ . Desired profile D can have any shape that satisfies the grid operator objectives, as long as it also satisfies $\begin{array} { r } { \Phi = \sum _ { t = 1 } ^ { T } D _ { t } } \end{array}$ . The latter formulation means that the same amount of electricity required by the EV agents is redistributed in a different way.

Figure 3 provides an overview of the decision environment of each individual EV agent, which receives price signals and decides about EV charging based on satisfying individual preferences and objectives. The lightly shaded areas in this figure indicate parts that EV owners do not have access to, such as the aggregate EV charging demand, which is only observed by the grid operator, or the individual charging demand profiles of other EV agents in the population. Online Appendix A presents a summary of the notation used throughout the paper. An exemplary outcome using this coordination mechanism is depicted in Online Appendix B.

## 3.2. Smart Grid Manager’s Price-Setting Approach

The grid manager’s agent (control agent) broadcasts prices for each time period t over some time horizon T to all EV agents, aiming at a desired demand profile. In other words, the broadcast prices are the same to the entire EV population (i.e., there is no price discrimination), although they can vary across time and, most importantly, they may also depend on the charging rate chosen by the consumer (e.g., EV agent). The chargingrate-based price component represents one of the key innovations of this study, as it allows mitigation of the avalanche effects (i.e., rational self-interested agents always charging the most when the traditional, static prices are lowest), as will be shown in Section 4. We propose the following formulation for electricity prices (in monetary units per kWh), which we call capacity-based pricing: 11

Figure 2. Grid Operator’s Decision Environment  
![](/api/attachments/2VUSBQ36/fulltext/images/d287732127f73ba722082e299ae517e7196b3a48b812f050928216951a2144dc.jpg)

$$
P _ {t} (r) = P _ {0, t} + \alpha_ {t} \cdot r,\tag{1}
$$

where $P _ { t } ( r )$ is the rate-dependent electricity price in monetary units per electricity unit $( \mathrm { e . g . , \ \$ 5 / k W h } )$ for time period t, and r is the EV agent’s chosen charging rate (power consumption). Parameter $P _ { 0 , t }$ represents a price component that is independent of the charging rate. We assume $P _ { 0 , t }$ to be specified exogenously. One possible value for $P _ { 0 , t }$ <sub>t</sub> is the wholesale electricity value at t. Another possible value for $P _ { 0 , t }$ <sub>t</sub> is a constant value $P _ { 0 }$ over time which ensures that the supply-side costs are always covered.

Term α · r is the variable component in our proposed pricing scheme and depends on the charging rate r that an EV agent selects based on her needs and preferences. The rate at which an EV agent is charging determines the grid capacity required to cover this load. Thus, we include a capacity charge in the pricing scheme (i.e., premium for charging rate used), transferring the cost of capacity to the EV customer who is using it. Grid managers are concerned about grid capacity, and this approach allows them to incentivize customers not to overload existing grid infrastructure. With our formulation, an EV agent that uses more grid capacity (i.e., charges at a higher rate) pays a higher price per electricity unit.

The parameter $\alpha _ { t }$ is the slope of the price curve with respect to charging rate. It is defined by the grid operator for each time interval t and serves as a steering parameter (decision variable), which allows the grid manager to induce a certain demand profile. The control agent’s goal is to determine the value $o f \alpha _ { t }$ for each interval $t ,$ that is, to determine the vector $\pmb { \alpha } = [ \alpha _ { 1 } , \ldots , \alpha _ { T } ]$ that will induce the desired aggregate demand profile. Naturally, the ability to calculate the optimal value of depends not only on the desired profile $\mathbf { D } = [ D _ { 1 } , \dots , D _ { T } ]$ but also requires some understanding of the EV population as well as how this population would respond to capacity-based pricing. Thus, for completeness, in the next subsection we briefly overview the key considerations of individual EV charging agents.

Figure 3. EV Agent’s Decision Environment  
![](/api/attachments/2VUSBQ36/fulltext/images/7a4c3e225740fe1e1a88d982dbd0b84356461db31db8ebd39aa38f249493fb6c.jpg)

## 3.3. EV Agents’ Decision Environment 9

Let $\mathbf { I } = \{ 1 , \ldots , I \}$ represent a set of self-interested EV agents (representing their owners’ preferences) that wish to minimize energy cost over time horizon $T \in \mathbb { Z } ^ { + } ,$ that is, I denotes EV agents in the grid operator’s portfolio. Each EV owner $i \in \mathbf { I }$ has a set of individual preferences $\theta ^ { i } = \{ \Delta ^ { i } , \Phi ^ { i } , \beta ^ { i } , E ^ { i } \} . ^ { 1 2 }$ This set includes tuple $\pmb { \Delta } ^ { i } = ( d _ { 1 } ^ { i } , \dots , \overline { { d _ { k } ^ { i } } } )$ of driving deadlines, which correspond to points in time $( d _ { n - 1 } ^ { i } < d _ { n } ^ { i } )$ over horizon T. Each deadline $d _ { n } ^ { i }$ coincides with the end of a time interval of duration $\delta .$ Before each deadline $d _ { n } ^ { i } ,$ the EV owner requires a minimum amount of energy $\varphi _ { n } ^ { i }$ from tuple $\mathbf { \Phi } ^ { i ^ { \widehat { } } } = ( \varphi _ { 1 } ^ { i } , \ldots , \varphi _ { k } ^ { i } )$ . These deadlines represent times that the EV owner needs to depart or certain times during the day that she requires at least this amount of charge. This energy $\varphi _ { n } ^ { i }$ is expected to be consumed on all $( \mathrm { i . e . , }$ planned and spontaneous) driving until the next deadline $d _ { n + 1 } ^ { i }$ . Thus, the amount of energy $\varphi _ { n } ^ { i }$ has to be equal to or greater than the amount spent on actual driving till the next deadline. The number of deadlines $( \mathrm { i . e . , } | \Delta ^ { i } | )$ as well as the timing of each deadline can vary across EV owners.

Furthermore, each EV owner has certain charging availability during time horizon T. This availability means that either she is close to a home plug or close to a charging pole (e.g., on work premises) and available for charging. We model this charging availability at any time interval $t \in \mathbf { T }$ as a binary variable $\beta _ { t } ^ { i } \in \{ 0 , 1 \}$ }. Thus, each EV owner i ∈ I has her own EV charging availability vector $\pmb { \beta } ^ { i } = [ \beta _ { 1 } ^ { i } , \dots , \beta _ { T } ^ { i } ]$ . Finally, each EV uses some energy while being driven. This expected driving might include spontaneous driving as well, which was not foreseen by the EV driver in advance. We denote as $E _ { t } ^ { i }$ the amount of energy actually spent during driving. The vector $\mathbf { E ^ { i } } = [ E _ { 1 } ^ { i } , \dots , E _ { T } ^ { i } ]$ contains nonzero values only when the EV owner is driving and, consequently, is not available for charging (i.e., $E _ { t } ^ { i } \neq 0$ only when $\beta _ { t } ^ { i } = 0 )$ . When the EV is available for charging $( \beta _ { t } ^ { i } = 1 )$ , the energy value $E _ { t } ^ { i }$ for this time t is zero.

A graphical illustration of the EV agent’s decision space over time is presented in Figure 4. Figure 4 shows that an EV agent i with charging requirements $\varphi _ { n - 1 } ^ { i }$ by deadline $d _ { n - 1 } ^ { i }$ and $\varphi _ { n } ^ { i }$ by deadline $d _ { n } ^ { i }$ spends electricity $E _ { 1 } ^ { i }$ during t � 1 and $E _ { 3 } ^ { i }$ during $t = 3$ for driving. During these times, the agent is not available for charging $( \beta _ { 1 } ^ { i } = 0$ and $\beta _ { 3 } ^ { i } = 0 )$ . Therefore, the agent needs to charge as much electricity as is needed to compensate for the amounts of energy spent for driving $E _ { 1 } ^ { i } , E _ { 3 } ^ { i }$ , so that by deadline $d _ { n - 1 } ^ { i } ,$ , the battery contains energy $\varphi _ { n - 1 } ^ { i } ,$ , and by $d _ { n } ^ { i } ,$ , it contains $\varphi _ { n } ^ { i }$

For each EV agent i, the energy cost over T (denoted as $C ^ { i } )$ is the sum of individual costs for each t:

$$
C ^ {i} = \sum_ {t = 1} ^ {T} c _ {t} ^ {i} = \sum_ {t = 1} ^ {T} e _ {t} ^ {i} \cdot P _ {t} (\cdot),\tag{2}
$$

where $c _ { t } ^ { i }$ is the cost of energy consumed during time $t , e _ { t } ^ { i }$ is the amount of energy consumed by each EV agent i during the interval $t ,$ and $P _ { t } ( \cdot )$ is the (possibly ratedependent) price of energy during this time. If we assume time intervals of equal duration $\delta \neq 0$ and charging at a constant power rate $r _ { t } ^ { i }$ in kW within time interval t, then $e _ { t } ^ { i } = r _ { t } ^ { i } \cdot \bar { \delta }$ . The objective of each EV agent $i \in \mathbf { I }$ is, then, to find the charging profile $\mathbf { r } ^ { i * } = [ r _ { 1 } ^ { i * } , . . . . , r _ { T } ^ { i * } ]$ that minimizes cost over T:

$$
\mathbf {r} ^ {i *} = \underset {r _ {1} ^ {i}, \dots , r _ {T} ^ {i}} {\arg \min} \sum_ {t = 1} ^ {T} r _ {t} ^ {i} \cdot \delta \cdot P _ {t} (\cdot)\tag{3}
$$

subject to two constraints. The first constraint is

$$
0 \leq r _ {t} ^ {i} \leq \beta_ {t} ^ {i} \cdot r _ {m a x} \quad \forall t \in \mathbf {T},\tag{4}
$$

where $r _ { m a x }$ is the highest allowable rate, which can vary depending on charging infrastructure. The rightmost inequality of (4) ensures that the EV can be charging only whenever it is available for charging (when $\beta _ { t } ^ { i } = 1 )$ Furthermore, the EV agent needs to ensure a minimum energy content $\varphi _ { n } ^ { i }$ before the EV owner unplugs the car for driving (before each deadline $d _ { n } ^ { i } )$ . We define as $S o C _ { n } ^ { i }$ the battery’s state of charge before each deadline $d _ { n } ^ { i } .$ This state of charge should be equal to or greater than the minimum energy content $\varphi _ { n } ^ { i } \colon \hat { S } o C _ { n } ^ { i } \geq \varphi _ { n } ^ { i } , \forall d _ { n } ^ { i } \in \Delta ^ { i }$

The state of charge before each deadline $d _ { n } ^ { i }$ is defined as $\begin{array} { r } { { S o C _ { n } ^ { i } = S o C _ { t = 0 } ^ { i } + \sum _ { t = 1 } ^ { d _ { n } ^ { i } } r _ { t } ^ { i } \cdot \delta - \sum _ { t = 1 } ^ { d _ { n } ^ { i } } E _ { t } ^ { i } } } \end{array}$ , where $S o C _ { t = 0 }$ is the battery’s state of charge before the time horizon starts (when $t = 0 )$ . This can be assumed zero (empty battery) or not. The term $\textstyle \sum _ { t = 1 } ^ { d _ { n } ^ { t } } E _ { t } ^ { i }$ denotes the amount of energy spent while the EV is driving till the deadline $d _ { n } ^ { i }$ The amount $\varphi _ { n } ^ { i }$ is expected to be consumed on planned or spontaneous driving till the deadline $d _ { n + 1 } ^ { i }$ . Thus, the second constraint is the minimum energy content constraint before each deadline:

Figure 4. EV Agent’s Decision Space  
![](/api/attachments/2VUSBQ36/fulltext/images/ef19054079a1d366339c15cddaf6e202b7948bf75e1559e8f28bf0ad6b90518f.jpg)

$$
S o C _ {t = 0} ^ {i} + \sum_ {t = 1} ^ {d _ {n} ^ {i}} r _ {t} ^ {i} \cdot \delta - \sum_ {t = 1} ^ {d _ {n} ^ {i}} E _ {t} ^ {i} \geq \varphi_ {n} ^ {i} \quad \forall d _ {n} ^ {i} \in \boldsymbol {\Delta} ^ {i}.\tag{5}
$$

A consequence of Equation (5) is that, at the end of the entire horizon T, the EV agent needs to charge

$$
S o C _ {t = 0} ^ {i} + \sum_ {t = 1} ^ {T} r _ {t} ^ {i} \cdot \delta = \varphi^ {i},\tag{6}
$$

with $\varphi ^ { i }$ being the summation of all required energy contents by each deadline: $\begin{array} { r } { \varphi ^ { i } = \sum _ { n = 1 } ^ { | \Delta ^ { i } | } \varphi _ { n } ^ { i } } \end{array}$ . It must satisfy $\textstyle \varphi ^ { i } \geq \sum _ { t = 1 } ^ { T } E _ { t } ^ { i }$ so that it covers all driving needs within horizon T. Also, we assume EV agents acquire the desired energy $\varphi ^ { i }$ sooner rather than later, all else being equal.

It is important to note that the above description represents the decision environment of highly capable EV agents. However, the proposed pricing approach is highly flexible and can be used with more myopic and less planning-oriented EV agents, for example, possessing some subset of the capabilities described above, as discussed in Online Appendix J.

## 3.4. Overview: Context and Scope of the Study

As mentioned earlier, our goal is to address the smart grid manager’s decision problem (i.e., grid balancing) via an innovative capacity-based pricing approach. Ideally, knowledge of the individual-level preferences of EV owners should help the grid manager make pricesetting decisions that achieve optimal outcomes (e.g., maximally balanced grid). However, the discussion of the EV agents’ decision environment in Section 3.3 points to two critical obstacles to the grid manager’s optimal decision making: (i) information availability and (ii) computational tractability. Specifically, considerations behind the charging decisions of individual EV agents are extremely complex (driving needs, deadlines, availability, etc.) and many of them are inherently private, that is, not available to (or measurable by) grid managers. In other words, grid managers are faced with an “incomplete information” problem. This is further compounded by the fact that, even if a substantial subset of this information was available to grid operators, at large scale (i.e., in settings with large EV populations) the precise optimization problem would be computationally intractable, because of the complex interplay between charging considerations, preferences, and needs. Thus, in order to address the smart grid manager’s decision problem in practical, realistic settings, we inevitably turn to heuristics (i.e., certain simplifications and approximations).

In Sections 4 and 5, we propose intelligent and high performing price-setting heuristics designed using both analytical and computational approaches. One baseline assumption is that the grid managers can always realistically expect the following data/information to be available (observable) to them: number of self-interested, rational EV agents $I ;$ EV agents’ aggregate demand $\mathbf { D ^ { 0 } } = [ D _ { 1 } ^ { o } , \dots D _ { T } ^ { \overline { { o } } } ] ;$ and the total energy $\begin{array} { r } { \Phi = \sum _ { i = 1 } ^ { I } \varphi ^ { i } = } \end{array}$ $\textstyle \sum _ { t = 1 } ^ { T } { \bar { D } } _ { t } ^ { o }$ consumed by all EV agents I across time horizon T. Also, our heuristics explore expanding information availability settings along an additional dimension: individual EV charging needs. In our study, we also make two additional assumptions about EV agent behavior, which are standard in the literature: EV agents are rational, that is, they are self-interested and they will choose their charging times and rates in a way that minimizes their cost, and, everything else being equal, they prefer to charge earlier than later.

Finally, it is important to note that, even though we propose heuristics to address the smart grid manager’s decision problem, in order to properly establish validity and measure performance of the proposed price-setting methods, we evaluate them in the most realistic scenario possible, that is, in a stochastic environment with highly heterogeneous EV agents (in terms of their driving behavior, charging needs, deadlines, etc.), and benchmark them against well-established pricing methods, as discussed in Sections 6 and 7.

## 4. Price-Setting Methods: Analytical Heuristics with No Charging Availability Constraints

In this section, we demonstrate several theoretical properties of the proposed capacity-based pricing approach, which provide key insights about its capabilities to miti gate potential avalanche effects. An important characteristic of the proposed approach (and one of the contributions of this study) is that the task of optimal price setting becomes directly analytically tractable in the situations where EV agents do not have charging availability constraints (i.e., EV agents are unconstrained). In other words, theoretical characteristics of the proposed approach directly lead to analytical heuristics for how grid operators can set capacity-based prices that induce the desired EV charging profile. Thus, these heuristics are optimal in unconstrained EV charging situations and also constitute a natural approach in situations where individual charging availability constraints are not observable by the grid operators.

Needless to say, this section does not constitute a complete theoretical analysis of the proposed capacity based pricing. Given the challenges of information availability and problem complexity in real-world environments, the focus is on deriving tractable analytical, closed-form heuristic solutions that can still offer effective and scalable price-setting methods meeting grid managers’ objectives. Also, it is important to reiterate that the performance evaluation and benchmarking for these heuristics are done in a full-fledged, stochastic, realistic simulation environment that reflects full complexity of individual EV agent behaviors.

To streamline the presentation of the theoretical results throughout this entire section, we will focus on the special case where $P _ { 0 , 1 } = \cdots = P _ { 0 , T } = : P _ { 0 }$ . However, the analogous theoretical results have been derived and are available for the general case, where $P _ { 0 , t }$ can have different values at different time periods t. All theorems for the general case and their respective proofs are presented in Online Appendix $C ,$ whereas the proofs of the theorems for $P _ { 0 , 1 } = \cdots = P _ { 0 , T } = : P _ { 0 }$ are presented in Online Appendix D.

## 4.1. Optimal EV Charging Under Capacity-Based Pricing

In order for the grid manager to induce the desired EV charging profile using capacity-based prices, it is important to understand how EV agents react to such a pricing mechanism. Thus, we first show how a rational (costminimizing) and unconstrained agent i with any arbitrary overall charging need $\varphi ^ { i }$ over $T$ will determine its optimal EV charging behavior over time horizon T $( { \mathrm { i . e . } }$ , best charging rate for each time interval) under capacity-based pricing.

Theorem 1. When electricity prices broadcast by grid operators are in the form of $P _ { t } ( r ) = P _ { 0 } + \alpha _ { t } \cdot r$ (capacitybased pricing), then the optimal $( i . e .$ , cost-minimizing) charging rate for each rational, unconstrained EV agent i is $\begin{array} { r } { r _ { t } ^ { i * } = \frac { \varphi ^ { i } } { \alpha _ { t } \cdot \delta \cdot ( \frac { 1 } { \alpha _ { 1 } } + \cdots + \frac { 1 } { \alpha _ { T } } ) } } \end{array}$ 7 $\forall t \in \mathbf { T } ,$ for a given amount of energy $\varphi ^ { i }$ to be charged over time horizon $T . ^ { 1 3 }$

Theorem 1 is also trivially extensible to situations when an EV driver has some periods of charging unavailability; that is, when charging availability vector $\pmb { \beta } ^ { i } = [ \beta _ { 1 } ^ { i } , \dots , \beta _ { T } ^ { i } ]$ includes zero elements. In this case, the optimal charging can be calculated as described by Theorem 1, but only including the available time periods as part of the calculation.

Figure 5 shows that, within each time interval $t ,$ each EV agent i can choose a charging rate that will result in an electricity price on the y-axis. Figure 6 shows an example of the optimal charging rates, given the price functions presented in Figure 5.

We observe that the optimal charging rate $r _ { t } ^ { i * } =$ $\frac { \varphi ^ { t } } { \alpha _ { t } { \cdot } \delta { \cdot } ( \frac { 1 } { \alpha _ { 1 } } + \cdots + \frac 1 { \alpha _ { T } } ) }$ depends on parameters $\alpha _ { t } ,$ , which are the charging-rate multipliers of pricing schemes in Figure 5. Consequently, by adjusting $\alpha _ { t } ,$ grid operators can change the shape of the demand displayed in Figure 6. The optimal values $\alpha _ { t }$ for inducing a desired charging profile will be discussed in Section 4.2. In Online Appendix $\scriptstyle \mathrm { E , }$

Figure 5. (Color online) Example Scenario for Capacity-Based Pricing $P _ { t } ( r ) = P _ { 0 } + \alpha _ { t } \cdot r , \forall t \in \mathbf { T }$  
![](/api/attachments/2VUSBQ36/fulltext/images/fe40ed847d33d2545bfad73831182a23d4fb1dfc1d7718ad891916d0c5cb78ca.jpg)  
we illustrate how the presented approach mitigates avalanche effects. The next subsection formalizes this expla nation by analytically deriving the optimal vector for the desired EV charging profile to be induced.

## 4.2. Optimality Conditions to Achieve a Desired Profile

We show how the $\alpha _ { t }$ parameters should be optimally set by the control agent representing a grid operator, so that the desired charging demand D is induced.

Theorem 2. To induce the desired charging profile $\mathbf { D = }$ $[ D _ { 1 } , \ldots , D _ { T } ]$ in a heterogeneous population of I rational, unconstrained agents using capacity-based prices of the form $\begin{array} { r } { P _ { t } ( r ) = P _ { 0 } + \alpha _ { t } \cdot r , } \end{array}$ , the values for parameters $\alpha _ { t }$ must be set so that they satisfy the condition $\begin{array} { r } { \frac { \dot { \alpha } _ { 1 } \cdot D _ { 1 } } { \delta } = \cdots = \frac { \alpha _ { T } \cdot D _ { T } } { \delta } , } \end{array}$

Theorem 2 offers an analytical heuristic (AH) that provides three important insights about the pricing scheme calibration for inducing a certain charging profile. First, there are multiple (theoretically infinitely many) optimal values for parameters $\alpha _ { t }$ yielding the same charging outcome, which is optimal for EV owners (ensures minimum cost under a given pricing scheme) and induces the profile desired by grid opera tors. We refer to this set of optimal $\pmb { \alpha }$ values as the D-inducing family of alphas. Second, the optimality condition does not require any knowledge (precise, distributional, etc.) of individual charging needs $\varphi ^ { i }$ . Thus, prices set according to Theorem 2 guarantee the desired charging profile for the grid operator in the presence of rational, unconstrained agents. Third, we can parameterize this family of optimal solutions with a single parameter (degree of freedom) $\begin{array} { r } { F = \frac { \alpha _ { 1 } \cdot D _ { 1 } } { \delta } = \cdots = \frac { \alpha _ { T } \cdot D _ { T } } { \delta } } \end{array}$ . The optimal vector is $\begin{array} { r } { \pmb { \alpha } = [ \frac { \delta \cdot \boldsymbol { F } } { D _ { 1 } } , \dots , \frac { \delta \cdot \boldsymbol { F } } { D _ { T } } ] } \end{array}$ for any $F \geq 0$ , so that $\alpha _ { t } \geq 0 , \forall t \in \mathbf { T }$ . Then, the optimal price for an EV agent i who chooses charging rate $r _ { t } ^ { i }$ is $P ( r _ { t } ^ { i } ) = P _ { 0 } + \alpha _ { t } \cdot r _ { t } ^ { i }$

Figure 6. (Color online) Optimal Charging Rate for Specific Prices Shown in Figure 5  
![](/api/attachments/2VUSBQ36/fulltext/images/e4cd2eb14ab4c5d34f1f5079a1f97c223892e213825e61be617a563e17b3efc6.jpg)

Please note that, even though the same pricing scheme is broadcast to all EV agents, each EV agent may pay a different price per kWh depending on their own charging needs. To see this, let $r _ { t } ^ { i }$ be the selected charging rate of EV agent i and the corresponding energy $\boldsymbol { r } _ { t } ^ { i } \cdot \delta$ a fraction of the overall demand $D _ { t }$ . Also, we denote $\epsilon ^ { i }$ ∈ [0, 1] as the fraction of total demand Φ corresponding to each individual EV agent $i ,$ that is, $\begin{array} { r } { \epsilon ^ { i } = \frac { \varphi ^ { i } } { \Phi } . } \end{array}$ For each time interval $t ,$ we have $\boldsymbol { \epsilon } ^ { i } \cdot \boldsymbol { D } _ { t } = \boldsymbol { r } _ { t } ^ { i } \cdot \boldsymbol { \delta }$ As a result, the optimal price is $\begin{array} { r } { P ( r _ { t } ^ { i } ) = P _ { 0 } + \alpha _ { t } \cdot \frac { \epsilon ^ { i } \cdot D _ { t } } { \delta } = P _ { 0 } + \epsilon ^ { i } \cdot F } \end{array}$ . The last formulation shows that, with the proposed pricing scheme which is uniform across EV agents, each EV agent i will pay a different price per kWh depending on their share of contribution $\epsilon ^ { i }$ to the overall demand $D _ { t }$ , which requires a corresponding charging rate.

## 4.3. Generating Target Revenue While Inducing a Desired Profile

As discussed in Section 4.2, the one degree of freedom produces the D-inducing family of alphas, that is, a theoretically infinite number of optimal charging vectors α that will induce the desired profile D. Each vector leads to a different pricing scheme which theoretically would bring different revenue to grid operators/energy providers. Naturally, not all pricing levels may make sense in a specific real-world economic situation. Thus, in addition to reshaping existing demand toward a desired profile via price signals, it is important to provide the energy suppliers or grid operators the ability to maintain the overall revenues established by the market $( \mathrm { i . e . }$ , to achieve rebalancing without changing the total charging cost for the same energy needs) or, more generally, the ability to collect a certain revenue or achieve revenue equivalence of the proposed capacity-based pricing scheme with some desired or government-regulated pricing scheme in the specific market environment (Reneses and Ortega 2014).

We show how the optimal solution space of vectors can be constrained to reflect the solution that will generate specific target revenue $\Psi ^ { * }$ , while at the same time inducing the desired demand profile $\mathbf { D } = [ D _ { 1 } , \dots , D _ { T } ]$ Also, recall that $\begin{array} { r } { \Phi = \sum _ { t = 1 } ^ { T } D _ { t } } \end{array}$ . In the next theorems, we use index $z \in \mathbf { T }$ to iterate over time slots for notational clarity in some of the expressions.

Theorem 3. To induce the desired charging profile $\mathbf { D = }$ $[ D _ { 1 } , \ldots , D _ { T } ]$ and generate the target revenue $\Psi ^ { * }$ in a heterogeneous population of I rational, unconstrained agents using capacity-based prices in the form of $\begin{array} { r } { P _ { z } ( r ) = P _ { 0 } + \alpha _ { z } \cdot r , } \end{array}$ parameters $\alpha _ { z }$ should be set as $\begin{array} { r } { \alpha _ { z } = \frac { \delta \cdot ( \Psi ^ { * } - P _ { 0 } \cdot \Phi ) } { D _ { z } \cdot \Phi \cdot \sum _ { i = 1 } ^ { I } \left( \epsilon ^ { i } \right) ^ { 2 } } , \forall z \in \mathbf { T } } \end{array}$

Simply put, Theorem 3 shows how to choose a specific value from the D-inducing family of alphas that is also able to generate target revenue $\mathrm { \bar { \Psi } } ^ { * }$ . In particular, because $\begin{array} { r } { \alpha _ { z } = \frac { \delta \cdot F } { D _ { z } } } \end{array}$ (as discussed in Section 4.2), the specific degree-of-freedom parameter value corresponding to this specific is $\begin{array} { r } { F = \frac { \Psi ^ { * } - P _ { 0 } \cdot \Phi } { \Phi \cdot \sum _ { i = 1 } ^ { I } \left( \epsilon ^ { i } \right) ^ { 2 } } . } \end{array}$ . And, the prices that the rational, unconstrained agent i will pay when it chooses the optimal charging rates $r _ { z } ^ { i * }$ are $P _ { z } ( r _ { z } ^ { i * } ) = P _ { 0 } + \epsilon ^ { i } .$ $\frac { \Psi ^ { * } - P _ { 0 } \cdot \Phi } { \Phi \cdot \sum _ { i = 1 } ^ { I } \left( \epsilon ^ { i } \right) ^ { 2 } } , \forall z \in \mathbf { T }$

It is important to note that Theorem 3 guarantees the precise induction of target revenue $\Psi ^ { * }$ with unconstrained EV agents only if we have accurate information about individual charging needs $\epsilon ^ { i } .$ . If no precise information on $\epsilon ^ { i }$ is available (as is the case in many real-world settings), the grid operator can still use Theorem 3 to achieve approximate induction of target revenue (while inducing the desired charging profile D) by using coarsegrained estimations of $\check { \epsilon ^ { i } }$ . For example, as a minimal amount of information, the population average $( \epsilon ^ { i } = \frac { 1 } { I } )$ could be used as a rough estimate; this scenario is repre sented as Corollary $\mathrm { A } . \bar { 5 }$ of Theorem 3 (and is provided in Online Appendix D because of space limitations). $\mathrm { A s }$ another example, if the distributional characteristics of $\epsilon ^ { i }$ are known (say, as part of domain knowledge), for example, $\epsilon ^ { i } \sim { \mathcal N } ( \textstyle { \frac { \dot { 1 } } { I } } , \bar { \sigma } ^ { 2 } )$ , then a more nuanced estimate could be obtained; this scenario is represented as Corollary $_ { \mathrm { A } . 6 }$ (also provided in Online Appendix D).

Furthermore, because of (private) individual preferences and constraints $\theta ^ { i } ( i \in \mathbf { I } )$ of EV agents, the desired charging profile D might not be achievable. In other words, charging profile $\mathbf { D ^ { 0 } }$ that the grid operator observes in reality can be different, leading to a different revenue as well. Let $\Psi ^ { o }$ be the observed revenue, as a result of $\mathbf { D ^ { 0 } }$ . An important benefit of the proposed pricing approach is that, given the observed actual charging profile $\mathbf { D ^ { 0 } }$ , it can help generate target revenue $\Psi ^ { * }$ even in the presence of hard and unobservable individual preference $\theta ^ { i }$ . The intuition behind this is as follows. Because preferences $\theta ^ { i }$ are imposing hard constraints $( \mathrm { e . g . , }$ representing actual driving and charging needs of individuals), no matter which $\pmb { \alpha }$ is selected from the D-inducing family of alphas (given by Theorem 2) by the grid operator, the observed profile will be $\mathbf { D ^ { 0 } }$ . Therefore, assuming that preferences $\theta ^ { i }$ do not change, the grid operator can adjust from to $\pmb { \alpha } ^ { \prime }$ (also chosen from the same D-inducing family) so that the observed reve nue comes closer to the desired $( \Psi ^ { * } )$ , as described by the following theorem.

Theorem 4. Let $\mathbf { D ^ { 0 } }$ be the actual charging observed in response to (due to private EV agent constraints), then the grid operator needs to adjust the broadcast values from $\begin{array} { r } { \alpha _ { z } \stackrel { \smile } { t o } \alpha _ { z } ^ { \prime } = \frac { \delta \cdot ( \Psi ^ { * } - P _ { 0 } \cdot \Phi ) } { - \hphantom { \eta } _ { z } \cdot \qquad \forall z \in \mathbf { T } } , } \end{array}$ , to generate target revenue $\begin{array} { r l } { \Psi ^ { * } . } & { { } D _ { z } . \sum _ { i = 1 } ^ { I } \sum _ { t = 1 } ^ { T } \epsilon _ { t } ^ { i ^ { 2 } } . \frac { D _ { t } ^ { o - } } { D _ { t } } } \end{array}$

Similarly to Theorem 3, Theorem 4 provides guarantees only if we have accurate and granular information about individual charging needs $\epsilon _ { t } ^ { \breve { i } } .$ . And, if no precise information is available, coarse-grained approximations can still be used. Two specific approximation scenarios— using population average and population distribution— are represented as Corollaries $\bar { \mathrm { A } } . \bar { 7 }$ and A.8, respectively, in Online Appendix D.

Next, we present price-setting methods that are based on computational heuristics and can take advantage of information that can be learned from smart electricity market environments.

## 5. Price-Setting Methods: A Computational Heuristic (CH) with Charging Availability Constraints

So far, we have presented price-setting methods that are based on analytical heuristics arising from fundamental information availability and problem tractability assumptions, primarily based on understanding of unconstrained EV agent behavior. In this section, we introduce a price-setting approach for more complex (and less analytically tractable) situations, where some (aggregate) indicators of EV agent charging availability constraints and preferences may be available. We develop an intelligent computational heuristic that is able to achieve near-optimal performance and outperform all other benchmarks, without requiring numerous iterations and high computational capacity. The differentiating factor between the analytical and computational heuristics is the ability of the latter to adjust crucial pricing parameters in an advantageous fashion after observing aggregate information readily available in the smart grid $( \mathrm { i . e . } ,$ , by learning from aggregate charging behavior data). The proposed computational pricesetting heuristic has two major steps: (1) initialization step and (2) learning-from-data step in response to the observed outcomes from initial prices. The second step has several substeps, and below we describe all the key steps of the proposed computational heuristic in more detail.

STEP 1. Initialization of capacity-based prices based on the analytical heuristic, that is, in the absence of knowledge about private charging availability constraints.

This is a straightforward initialization step that sets the initial capacity-based prices to an intelligent default value based on the derived theoretical results discussed in the previous section. To reiterate, Theorem 2 states that, for unconstrained EV agents, desired charging demand D can be induced by a family of alphas (parameterized by a single degree of freedom $\hat { F ) }$ , that is, the

D-inducing family of alphas. Choosing different parameterizations will always result in inducing the same desired demand D (from the same EV drivers), but will induce different revenue. We then use Theorem $3 -$ more specifically, its Corollary $_ { \mathrm { A . 5 } }$ (when minimal information is available about individual charging needs) or $_ { \mathrm { A } . 6 }$ (when distributional information is available about individual charging needs)—to pick a specific vector instance $\pmb { \alpha } ^ { 0 }$ from the D-inducing family of alphas that corresponds to desired charging revenue $\Psi ^ { * }$ . (For convenience, we denote the specific degree-of-freedom $F$ value that corresponds to $\pmb { \alpha } ^ { \hat { 0 } }$ as $F _ { i n i t } . )$

$\pmb { \alpha } ^ { 0 }$ ← choose $( F _ { i n i t } )$ from D-inducing alpha family based on $\Psi ^ { * }$ (using Theorem 3 corollaries)

STEP 2. Making data-driven adjustments by observing aggregate EV charging behavior (affected by private availability constraints of individual EV drivers) in response to the initial prices.

First, we assume that we can implement the initial capacity-based prices (based on $\pmb { \alpha } ^ { \theta }$ in Step 1 and a standard component $P _ { 0 } )$ and observe the resulting aggregate charging demand $\mathbf { D } ^ { o }$ and revenue $\Psi ^ { 0 }$

• Observation step:

$\begin{array} { l } { ( \mathbf { D } ^ { o } , \Psi ^ { 0 } ) } \\ { ( P _ { 0 } , \pmb { \alpha } ^ { 0 } ) } \end{array}$ ← observe outcomes based on capacity-based pricing

Typically, we will observe that $\mathbf { D } ^ { o } \neq \mathbf { D } ,$ , because of the private preferences and constraints of EV drivers. Thus, our first goal is to improve the observed demand $\mathbf { D } ^ { o }$ toward the desired value D.

• Step 2a. Adjusting capacity-based prices to better match the desired demand, based on the observed demand discrepancies due to the private charging availability constraints. As discussed in Section 4.1, the proposed capacity-based pricing approach has a desirable property that allows it to mitigate the potential avalanche effects; that is, at a given time period $t ,$ rational consumers will choose the charging rate $r _ { t }$ that is (inversely) proportional to the charging-rate price coefficient $\alpha _ { t } ,$ , thus, allowing the grid operator to induce desired charging behavior. That is, increasing or decreasing the $\alpha _ { t }$ value should correspondingly and proportionately affect the charging rate (and, hence, the charged energy amount) during time period $t ,$ subject to individual constraints and preferences. This observation gives rise to the following intuition: if we know some (even aggregate) charging availability information across different time periods, this information could be used to adjust the values accordingly. The following component of the computational heuristic exploits this intuition. The key idea is that the discrepancy between the observed and desired demand can be intuitively captured as $\mathbf { w } = \mathbf { D } ^ { o } / \mathbf { D }$ (or, more granularly, $w _ { t } = D _ { t } ^ { o } / D _ { t } )$ . Then, using the knowledge of this discrepancy, we can adjust the capacity-based prices accordingly: $\pmb { \alpha } ^ { 1 } = \pmb { \alpha } ^ { 0 }$ · w (or, more granularly, $\mathbf { \widehat { \alpha } } _ { t } ^ { 1 } = \boldsymbol { \alpha } _ { t } ^ { 0 } \cdot \boldsymbol { w } _ { t } )$

$\mathbf { w }  \mathbf { D } ^ { o } / \mathbf { D }$ // capture discrepancy between desired and observed charging profiles

${ \pmb { \alpha } } ^ { 1 }  { \pmb { \alpha } } ^ { 0 } \cdot { \bf w }$ // adjust capacity-based price component accordingly

As before, after implementing the adjusted capacitybased prices (based on $\pmb { \alpha } ^ { 1 }$ in Step 2a and a standard component $P _ { 0 } ) _ { . }$ , we can observe their effect on the aggregate charging demand D<sup>′</sup> and revenue $\Psi ^ { 1 }$

• Observation step:

$\begin{array} { l } { { ( { \bf D } ^ { \prime } , \Psi ^ { 1 } ) } } \\ { { ( P _ { 0 } , { \bf \Phi } \alpha ^ { 1 } ) } } \end{array}$ ← observe outcomes based on capacity-based pricing

It is important to highlight that the multiplicative adjustment $\pmb { \alpha _ { 1 } }$ of our analytically optimal prices $\pmb { \alpha } ^ { 0 }$ (i.e., ${ \pmb \alpha } ^ { 1 } = { \pmb \alpha } ^ { 0 } \cdot { \bf w } )$ exhibits some desirable properties. In particular, formally this $\pmb { \alpha } ^ { 1 }$ instance belongs to a different family of analytically optimal alphas, that is, the one that would induce desired demand D=w for unrestricted EV drivers (the D=w-inducing family of alphas).<sup>14</sup> Thus, all the additional properties of the analytically optimal prices hold for this alpha family as well, including Theorems 3 and 4. Also, it is important to reiterate that choosing different parameterizations of the same alpha family will always induce the same observed demand D<sup>′</sup> (from the same EV drivers), but will induce different revenues. Using the same $F _ { i n i t }$ parameter value (as above) on this family would result in precisely the $\pmb { \alpha } ^ { 1 }$ instance and would be guaranteed to induce the desired revenue $\Psi ^ { * }$ for unrestricted EV drivers. In summary, shifting from the D-inducing to the D=w-inducing family of alphas allows us to improve toward the desired demand $( \mathrm { i . e . } ,$ , from $\mathbf { D } ^ { o }$ to D<sup>′</sup>) when accounting for private EV driver preferences and restrictions. Thus, for the rest of the computational heuristic, we will operate within the D=w-inducing family of alphas, but we will attempt to find further adjustments toward desired revenue $\bar { \Psi } ^ { * }$ in the presence of private EV preferences. This is needed, because the initial value of $\Psi ^ { 1 }$ that was observed (in response to the default assumption of having unrestricted EV drivers) often may not accurately capture $\Psi ^ { * }$ . Thus, our second goal is to improve the latest observed revenue $\Psi ^ { 1 }$ toward the desired value $\Psi ^ { * }$

• Step 2b: Adjusting capacity-based prices to better match the desired revenue due to private charging availability constraints. As discussed above, the ability to select specific alpha instances systematically from the D=w-inducing family of alphas allows us to look for a different instance $\scriptstyle { \pmb { \alpha } } ^ { 2 }$ (essentially by finding another degree-of-freedom parameter value $F _ { a d j } )$ that is able to guarantee the same charging demand D<sup>′</sup> while adjusting from observed $\Psi ^ { 1 }$ toward $\Psi ^ { * }$ in the presence of observable aggregate charging behavior data, based on Theorem 4 (more specifically, its Corollary $_ { \mathrm { A . 7 } }$ or

A.8 in the Online Appendix in the settings with minimal versus distributional information about individual charging needs, respectively).

$\alpha ^ { 2 } \gets$ choose $( F _ { a d j } )$ from D=w-inducing alpha family based on $\Psi ^ { * }$ (using Theorem 4 corollaries)

After implementing this adjustment to capacitybased prices (based on $\mathbf { \bar { \alpha } } ( \alpha ^ { 2 } )$ , we can observe their effect.

• Observation step:

$\begin{array} { l } { ( \mathbf { D } ^ { \prime } , \Psi ^ { 2 } ) } \\ { ( P _ { 0 } , \pmb { \alpha } ^ { 2 } ) } \end{array}$ ← observe outcomes based on capacity-based pricing

Finally, $. \mathrm { i f } \Psi ^ { 2 }$ is not a sufficiently good approximation of $\Psi ^ { * }$ , we can rely on an additional learning step that can provide further revenue matching improvements.

• Step 2c: Adjusting capacity-based prices to better match the desired revenue due to private charging availability constraints, using a learning function. The last two observation steps provide two examples of the relationship between the D=w-inducing capacity based price vectors $\pmb { \alpha } ^ { 1 }$ and $ { \alpha } ^ { 2 }$ (represented by the corresponding degree-of-freedom values $F _ { i n i t }$ and $F _ { a d j } )$ and the resulting revenues $\Psi ^ { 1 }$ and $\Psi ^ { 2 }$ . Thus, we can use points $( \Psi ^ { 1 } , \stackrel { \smile } { F } _ { i n i t } )$ and $( \Psi ^ { 2 } , F _ { a d j } )$ to learn the best-fit line connecting them, that is, the line approximating the relationship between the induced revenue (in the presence of private constraints) and the degree-of-freedom parameter $F$ for the D=w-inducing family of alphas. In other words, the line describes the linear function $F = f ( \Psi )$ ). Then, we compute $F ^ { * } = f ( \Psi ^ { * } )$ , and use $F ^ { * }$ to select a specific instance $\pmb { \alpha } ^ { * }$ from the D=w-inducing family of alphas.

f ← compute a linear function $F = f ( \Psi )$ based on points $( \Psi ^ { 1 } ,$ $\dot { F } _ { i n i t } )$ and $( \Psi ^ { 2 } , F _ { a d j } )$

$F ^ { * } \gets f ( \Psi ^ { * } ) \qquad / /$ compute the improved estimate of degree-offreedom parameter for $\Psi ^ { * }$

$\alpha _ { t } ^ { * } = \delta \cdot F ^ { * } / ( D _ { t } / w _ { t } )$ ), ∀t // select alpha from D=w-inducing family based on $\check { F } ^ { * }$

return <sup>∗</sup> // return α<sup>∗</sup> as the result of the computational heuristic

## 6. Multiagent Simulation Testbed

To evaluate the proposed IS-enabled solution, we design a multiagent simulation which consists of rational EV agents and a smart grid manager (control agent) responsible for inducing a desired aggregate charging profile D while meeting revenue targets. Agent-based modeling has been used to explore the heterogeneous behavior of electricity consumers and, more specifically, EV drivers (Kang et al. 2013, Bustos-Turu et al. 2014, Ketter et al. 2016a, Sheppard et al. 2017, Chaudhari et al. 2018, Muratori 2018). Our simulation environment is built according to the “smart markets” paradigm (Bichler et al. 2010) based on the specifications of Power TAC (Ketter et al. 2016a), which has been used as a simulation testbed in numerous research studies (Peters et al. 2013, Hernandez-Leal et al. 2015, Ketter et al. 2016b, Ru´ bio et al. 2016, Natividad et al. 2017). In this simulation environment, we model realistic EV agents that have diverse needs, preferences, and constraints using the comprehensive preference structure described in Section 3.3 (initialized using real-world data on EV driving behavior). We use the analytical and computational heuristics proposed in Sections 4 and 5 using information that is realistically available to the grid operator, and we show that the results not only substantially outperform numerous commonly used benchmarks but also are very close to optimality.

## 6.1. Simulation Description

The general structure of our simulation is presented below. The parameters can be determined exogenously by the simulation designer. Each simulation run is described by Steps 1–6.

Parameters: Time horizon $T ,$ temporal granularity $\delta ,$ static price components $P _ { 0 , t }$

Step 1: The grid operator receives as inputs $( \mathrm { e . g . , }$ , from past observations) the size of EV population I and the overall energy consumption of the EV population $\Phi =$ $\textstyle \sum _ { i = 1 } ^ { I } \varphi ^ { i }$ across horizon $\acute { T } { . }$

Step 2: The grid operator decides on total desired charging demand profile across all EV agents D � $[ D _ { 1 } , \ldots , D _ { T } ]$ and target revenue $\Psi ^ { * }$ over time horizon T.

Step 3: Based on the inputs $I , \Phi , \mathbf { D } _ { }$ , and $\Psi ^ { * }$ from Steps 1 and $^ { 2 , }$ the control agent calculates the values for the capacity-based pricing vector ${ \pmb { \alpha } } = [ \alpha _ { 1 } , \ldots , \alpha _ { T } ]$ based on the configurations of analytical and computational price-setting heuristics, described in Section 6.5.

Step 4: Each EV agent i ∈ I has a set of stochastic preferences $\theta ^ { i }$ and receives α from Step 3. It finds the charging profile $\mathbf { r } ^ { i * } = [ r _ { 1 } ^ { i } , . . . . , r _ { T } ^ { i } ]$ that achieves minimum cost over $T$ based on $\mathbf { r } ^ { i * } = \mathrm { a r g }$ min $\begin{array} { r } { \quad \quad \boldsymbol { r } _ { 1 } ^ { i } , . . . . , \boldsymbol { r } _ { T } ^ { i } \sum _ { t = 1 } ^ { T } \boldsymbol { r } _ { t } ^ { i } \cdot \boldsymbol { \delta } \cdot ( \boldsymbol { P } _ { 0 , t } + \boldsymbol { \alpha } _ { t } \cdot \boldsymbol { r } _ { t } ^ { i } ) } \end{array}$ 1 subject to Constraints (4)–(6).

Step 5: The grid operator observes demand profile $\mathbf { D ^ { o } } = \left[ \bar { D } _ { 1 } ^ { o } , \ldots , \bar { D _ { T } ^ { o } } \right]$ and collects revenue from the EV population: $\begin{array} { r } { \Psi ^ { o } \stackrel { . . . } { = } \textstyle \sum _ { i = 1 } ^ { I } \sum _ { t = 1 } ^ { T } ( P _ { 0 , t } + \alpha _ { t } \cdot r _ { t } ^ { i ^ { o } } ) \cdot r _ { t } ^ { i ^ { o } } \cdot \delta , } \end{array}$

Step 6: The grid operator evaluates the observed outcomes $\mathbf { D ^ { 0 } }$ and $\Psi ^ { o }$ by comparing them with the desired outcomes D and $\bar { \Psi } ^ { * }$ using a set of evaluation metrics. For the computational heuristic, which performs datadriven adjustments based on the observed outcomes over a small number of iterations, return to Step 3 for the next iteration as needed (i.e., until the final step of the heuristic).

## 6.2. Evaluation Metrics

We use several evaluation metrics to assess the quality of the results induced by the proposed artifact.

First, we use root mean square error $\mathrm { ( R M S E ) \ = }$ $\sqrt { \sum _ { t = 1 } ^ { T } { ( D _ { t } ^ { o } - D _ { t } ) ^ { 2 } } }$ as a general-purpose metric to assess how close the actual charging is to the desired profile. It is measured in MWh, and a low RMSE indicates a good result.

Second, we use two domain-specific metrics: the absolute observed peak $D _ { p e a k } ^ { o }$ and the observed peak-toaverage power ratio (PAPR) that are only calculated when a flat electricity demand is desired. More specifically, we use these metrics when the desired EV charging profile is flat $o r$ when the combination of the household electricity demand and EV charging has to be flat. The absolute peak $D _ { p e a k } ^ { o } : = \mathrm { m a x } _ { t \in \mathbf { T } } { D _ { t } ^ { o } }$ is the maximum value of demand profile $\mathbf { D ^ { o } } = [ D _ { 1 } ^ { o } , \dots , D _ { T } ^ { o } ]$ and should be as low as possible. The PAPR metric $\begin{array} { r } { ( \mathrm { P A P R } { = } \frac { { ( D _ { p e a k } ^ { o } ) } ^ { 2 } } { ( D _ { r m s } ^ { o } ) ^ { 2 } } { = } \frac { \left( \mathrm { m a x } _ { t \in \mathrm { T } } D _ { t } ^ { o } \right) ^ { 2 } } { \frac { 1 } { T } { \sum } _ { t = 1 } ^ { T } { ( D _ { t } ^ { o } ) } ^ { 2 } } ) } \end{array}$ is also known as the square of the peak-to-average ratio or crest factor and measures the intensity of peaks in a curve; it is commonly used as a proxy for volatility in smart grids (Liu et al. 2014), and should be as close as possible to one.

## 6.3. Data Description

To calibrate the simulation, we use real-world data obtained from the Netherlands, as described below.

6.3.1. Individual Preferences of EV Agents. Arrival and departure preferences and their subsequent dead lines $d _ { n } ^ { \bar { i } }$ together with the charging requirements $\varphi _ { n } ^ { i }$ represent the main source of stochasticity in our simulation. They vary across EV drivers but also across times and days. To calibrate these parameters, we used data distributions obtained by the Central Bureau of Statis tics (CBS) in the Netherlands (Valogianni et al. 2020). This data $\mathrm { s e t } ^ { 1 5 }$ includes mobility preferences from population clusters (full- or part-time employees, students, retired persons, etc.) with a variety of habits and driving behaviors (business commuting, leisure time driving, vacation, visits to relatives, shopping, etc.). For every simulation run (Steps 1–6), EV agent instantiations are created, and their associated deadlines $\begin{array} { r } { \Delta ^ { i } = ( d _ { 1 } ^ { i } , \dots , } \end{array}$ $d _ { k } ^ { i } )$ together with the charging requirements $\mathbf { \Phi } ^ { \mathbf { j } } =$ $( \ddot { \varphi } _ { 1 } ^ { i } , \dots , \varphi _ { k } ^ { i } )$ are assigned to each agent. For each individ ual agent, we probabilistically draw a different driving profile with certain driving motivations per day (work, leisure, etc.) and driving demand for each activity, combined with arrival and departure times.<sup>16</sup> Therefore, these data calibrate the charging availability vector $\pmb { \beta } ^ { i } =$ $[ \beta _ { 1 } ^ { i } , \dots , \beta _ { T } ^ { i } ]$ as well as the driving demand vector $\boldsymbol { E } ^ { i } = [ E _ { 1 } ^ { i } , \ldots , E _ { T } ^ { i } ]$ , ∀i ∈ I. An example of such a randomly drawn profile is shown in Figure 7. This profile belongs to a full-time employee who drives to work in the morn ing, afterward drives to a business meeting, and then to a professional training. In midday, the person drives to lunch, in the afternoon to another business meeting, and in the evening s/he returns home. Using this profile, we calibrate the charging availability vector $\mathbf { \beta } ^ { \mathbf i } = [ \beta _ { 1 } ^ { i } , \dots , \beta _ { T } ^ { i } ]$ of this driver. Each of the driving motivations is associated with a driving distance in km. Following the EV manufacturers’ specifications for energy consumed per unit of distance driven, these driving distances are converted to energy consumed during driving and calibrate the driving demand vector $E ^ { i } = [ E _ { 1 } ^ { i } , \dots , E _ { T } ^ { i } ]$

Figure 7. Driving Profile Example: Full-Time Employee (Randomly Drawn) on a Random Day  
![](/api/attachments/2VUSBQ36/fulltext/images/db92ce60e949afef8b67a61a0d115a2f443be74d999f4f05a866e3d734d94745.jpg)

6.3.2. Energy Prices. We calibrate the price component $P _ { 0 , t }$ of the proposed capacity-based pricing scheme using a retail price constructed from the wholesale prices recorded by the European Power Exchange (EPEX) and adjusted to account for network fees, taxes, and value-added tax (VAT) for the Netherlands (44% of the retail price). Figure 8 shows three weeks of such retail prices.

6.3.3. Desired Profile. Desired demand profile D over time T is decided by the grid operator given the total EV agent needs and the grid capacity available. Here, we show some possible calibrations of this profile based on real-world scenarios. One possible calibration is for D to be entirely flat. Another possible calibration is a profile that will complement the existing household demand in the grid, so that the overall profile produced by EV charging and household demand is flat, as illustrated in Online Appendix B. To calibrate the household demand, we use real-world data collected from the Netherlands. Figure 9 displays the steady-state household electricity demand of our population, where it is shown that the household demand already has some peaks and valleys. Thus, the proposed pricing can be used to fill these valleys with EV charging demand and create a less volatile overall demand, as we show later in Figure 14. Finally, we also include a scenario where the EV charging demand needs to be shaped to follow very volatile energy generation profiles from renewable sources, such as solar or wind power. We also explore the sensitivity of our results when the desired demand might include some forecasting error, for example, due to the uncertainty of the renewable generation.

Figure 8. (Color online) Retail Prices $P _ { 0 , t } \left( \mathsf { \ E / k W h } \right)$ over Three Weeks  
![](/api/attachments/2VUSBQ36/fulltext/images/9a5869cff7c23296bb37c1bbc695210c7c92a174bba08a01ffa45fdf954e1d02.jpg)

## 6.4. Benchmarks

To evaluate the proposed artifact, we compare its efficacy against the following benchmarks.

6.4.1. Benchmark 1: Real-World Charging—Flat Pricing. First, we compare the outcome of the proposed artifact with real-world EV charging data obtained in collaboration with an EV charging infrastructure company in the Netherlands (Valogianni et al. 2020). The data set includes charging observations from 1,500 charging poles in the whole country (231,976 transactions with the grid; 10,462 EV owners). These transactions are completed under flat pricing; that is, EV drivers paid the same price per electricity unit irrespective of the time of day $\hat { ( P = P _ { 0 } ) }$ . The steady-state curve of these EV charging transactions, combined with the household demand, is presented in Figure 10, where we observe substantial charging during working and evening hours.

6.4.2. Benchmark 2: Rate-Independent Scenario— Variable Pricing. This benchmark assumes self-interested agents, minimizing their costs based on a given variable retail price signal, which does not depend on the charging rate $( \bar { \alpha } _ { t } = 0 , \bar { \forall } t \in \mathbf { T } )$ , similarly to Benchmark 1. However, in this benchmark, the electricity prices vary across time; that $\mathrm { i s } , P _ { 0 , t }$ is nonconstant over time. To optimally parameterize the prices $P _ { 0 , i }$ <sub>t</sub> for this benchmark, we use the available grid capacity (also known as residual grid capacity) as a determinant. Essentially, the desired demand D is assumed to be the residual capacity, and we set the prices $P _ { 0 , t }$ so that they reflect this capacity availability. To properly set the prices and avoid any dependence on absolute values, we first normalize the residual capacity (as shown by Freier and von Loessl (2022)). Specifically, the normalized residual capacity in this case is $\begin{array} { r } { \dot { \mathbf { D } } _ { \mathrm { n o m } } = \frac { \mathbf { D } - D _ { m i n } } { D _ { \underline { { m } } a x } - D _ { m i n } } , } \end{array}$ where $D _ { m i n }$ and $D _ { m a x }$ indicate the maximum and minimum values of the desired demand profile D. Next, we set the prices as $\mathbf { P _ { 0 } } = 1 - \mathbf { D _ { n o r m } }$ . In this way, we achieve a direct correspondence between desired demand and prices: when the normalized demand $D _ { n o r m , t }$ is low for time $t ,$ then the prices $P _ { 0 , t }$ will be high (as the normalized demand only gets values between zero and one). With this implementation, commonly used in the literature $( \mathrm { e . g . } ,$ Freier and von Loessl 2022), we build a benchmark that directly reflects the capacity availability on prices and can be used for any volatile desired demand profile D. Figure 11 shows the household demand combined with the EV charging as a result of this benchmark.

Figure 9. Steady-State Household Demand of the Population over a Four-Month Period  
![](/api/attachments/2VUSBQ36/fulltext/images/e708f0ed3381e3c41aed6948b3e3dc363304dbbe7a54117c93885ec1edbe4a22.jpg)

Figure 10. (Color online) Combination of EV Charging Under Flat Pricing and Household Demand  
![](/api/attachments/2VUSBQ36/fulltext/images/f2b584e37bb06d90bf4f1a15b54c35aa8376fc4d7eb7b578af748d6b4cfd8cd2.jpg)

We observe that, not surprisingly, all charging is concentrated in early morning hours because of the low prices, creating high peaks during that time and high overall volatility. As EV agents are cost-minimizers and solely driven by variations in prices, they consume a significant portion of the daily charging during the lowest-price periods (early morning), and do not charge at all when prices are high (noon and evening hours). We also observe avalanche effects. As discussed in Online Appendix F, this is because all agents get the same price signals and, aside from small differences in preferences, their charging coincides, creating new peaks during the low-price periods. This avalanche effect is exactly what our proposed pricing artifact aims to mitigate by adjusting the price signals using a capacity-based price component.

Figure 11. (Color online) Combination of EV Charging Under Variable Pricing and Household Demand  
![](/api/attachments/2VUSBQ36/fulltext/images/0f8add056b248d0d74269b8a44b87e073cae4877de64b4d2a211a048af9e0238.jpg)

6.4.3. Benchmark 3: Increasing-Block Pricing. Academic literature has also used nonlinear prices to redistribute and flatten the electricity demand (Borenstein 2012, Puller and West 2013, Ito 2014). Specifically, these nonlinear prices follow an increasing-block pattern with respect to certain baseline consumption over a billing time period. This baseline consumption is defined as a “minimal basic household electricity usage” (Borenstein 2012). In our case, because we are dealing with EV charging, we define as baseline consumption a fraction of EV charging that is essential for EV drivers to cover their daily driving needs. Calibrating this parameter for the population in the Netherlands—where all our data stem from—we assume as baseline consumption 25% of consumption, we then follow the pricing scheme proposed by Borenstein (2012, p. 66, table 2). This benchmark is expected to perform well in simulation scenarios where flat demand profile is desired, as by design it is meant to redistribute the demand toward a more flat outcome.

When the desired demand is volatile, we calibrate this benchmark to reflect this. Similarly to a situation described earlier, the desired demand serves as our residual capacity. Specifically, when the desired demand is volatile, we set as baseline consumption the minimum value of the desired demand $D _ { m i n } ,$ and we also set an intermediate variable $d = D _ { m a x } - D _ { m i n }$ . Then, the price values are set as proposed by Borenstein (2012), but the demand intervals are now dependent on the desired demand, $( D _ { m i n } , \ D _ { m i n } + 0 . 2 5 \cdot d ] , \ ( D _ { m i n } + 0 . 2 5 \cdot d ,$ $D _ { m i n } + 0 . 5 0 \cdot d ] , ~ ( D _ { m i n } + 0 . 5 0 \cdot d , D _ { m i n } + 0 . 7 5 \cdot d ] , ~ ( D _ { m i n } +$ $0 . 7 5 \cdot d , D _ { m a x } ]$ , and greater than $D _ { m a x }$ . In this way, we adapt this increased-block pricing scheme to the volatility of the desired demand profile and create counterincentives for consuming more than the desired demand.

## 6.5. Configurations of the Proposed Price-Setting Approaches

As shown in Figure 1, the proposed IS-enabled CBP arti fact can be configured with different price-setting methods depending on the data/information availability scenarios. In Table 1, we summarize the specific configurations used in our computational evaluation scenarios based on the AH and the CH. As mentioned in Section 3.4, in addition to the typical grid usage information that the grid managers can always realistically expect to be observable, our heuristics also explored some expanded information settings with individual EV charging needs. Specifically, in terms of the assumptions that are made about charging availability of EV users, we instantiate the proposed price-setting approaches as

Table 1. Configurations of the Proposed Capacity-Based Pricing Heuristics

<table><tr><td rowspan="2">Assumptions about charging availability</td><td colspan="2">Knowledge about individual EV charging needs</td></tr><tr><td>Minimal (population average)</td><td>Distributional (population distribution)</td></tr><tr><td>Unconstrained EV users (Analytical Heuristic: capacity-based prices with theoretically optimal grid-balancing performance)</td><td>CBP-AH</td><td>CBP-AH-Distrib</td></tr><tr><td>EV users with private constraints (Computational Heuristic: data-driven price adjustments based on aggregate indicators of actual charging behavior)</td><td>CBP-CH</td><td>CBP-CH-Distrib</td></tr></table>

• AH, which sets prices based on understanding of unconstrained EV agent behavior. This heuristic is based on the analytical results discussed in Section 4. It was also described as Step 1 of the overall approach presented in Section 5.

• CH, which uses the AH as the starting point and then makes data-driven adjustments based on (aggregate) indicators of charging behavior that are readily available in the smart grid. This heuristic was described as the overall process (including both Step 1 and Step 2) in Section 5.

In addition, for both AH and CH, we instantiate two versions of each heuristic based on what information about individual charging needs is available to the grid operator (e.g., as domain knowledge):

• Minimal: Only the most basic, default information about individual EV charging needs (i.e., the population average, no charging need distributions known) is used/assumed by both heuristics. This version uses Corollaries A.5 and $_ { \mathrm { A . 7 } }$ in the Online Appendix (of Theorems 3 and 4, respectively) for setting and adjusting capacity-based prices according to the desired revenue (for instance, in the CH configurations, these corollaries are used to set $\pmb { \alpha } ^ { 0 }$ and ${ \pmb { \alpha } } ^ { 2 }$ , respectively, as discussed in Section 5).

• Distributional (denoted as -Distrib): This version assumes some distributional information about the individual EV charging needs of the population, and uses Corollaries A.6 and A.8 in the Online Appendix (of Theorems 3 and $^ { 4 , }$ respectively) for setting and adjusting capacity-based prices according to the desired revenue (again, in the CH configurations, these corollaries are used for $\pmb { \alpha } ^ { 0 }$ and ${ \pmb { \alpha } } ^ { 2 }$ , respectively).

The aforementioned 2 × 2 set of configurations gives rise to four instantiations of capacity-based price-setting heuristics that we evaluate in our main experiments— CBP-AH, CBP-AH-Distrib, CBP-CH, and CBP-CH Distrib—as summarized in Table 1.

Note that incorporating distributional information of individual EV charging needs affects only the revenue generation performance. Thus, all “-Distrib” configurations will have the same grid-balancing performance as their non-distributional-information counterparts, and reporting of their performance on the grid-balancing metrics will be combined (i.e., as “CBP-AH [-Distrib]” and “CBP-CH [-Distrib]”).

## 7. Evaluation of the Proposed Approach

In this section, we present comprehensive evaluation results. We use the simulation testbed described in Section 6 and compare the performance of the proposed IS-enabled pricing solution to a number of benchmarks in realistic settings that explicitly consider heteroge neous EV populations, with individual driving and charging preferences taken into account. The time granularity and the time horizon of our evaluation results are assumed to be δ � 1h and T � 168h; however, the presented simulation testbed allows for configuration of these parameters according to the needs of the specific application setting. Such planning horizon (Kamankesh et al. 2016, McPherson et al. 2018, Pham et al. 2019, Mohseni et al. 2020) and time granularity values are commonly used in the literature (Gottwalt et al. 2011, Wolak 2011, Yoon et al. 2014, Ansarin et al. 2020, Fang et al. 2020, Fabra et al. 2021, Blaschke 2022, Freier and von Loessl 2022), and have also been used in practice in some parts of the world.<sup>18</sup>

We are interested in the impact of the proposed approach on the overall electricity demand the grid is facing as well as meeting revenue targets as a result of the proposed capacity-based pricing scheme. The peak demand of the aggregate electricity curve impacts the required grid capacity to a very large extent (International Energy Agency 2017). Another important factor is the demand volatility. Reduced demand volatility protects the grid from critical strains and unpredictability, which affect the grid’s quality of service (e.g., unpredictable demand peaks can create blackouts). Although inducing desired demand is crucial for the stability of the grid, the ability to meet revenue goals at the same time is also important for grid stakeholders, such as energy providers. Hence, the combination of demand and revenue goals allows for a comprehensive empirical evaluation of the proposed approach.

Next, we evaluate the performance of our approach in a series of distinct evaluation scenarios where the desired EV charging profiles are of different volatility levels, representing different grid objectives.

## 7.1. Inducing a Flat Charging Profile and Generating Target Revenue

First, we present a scenario in which the grid operator desires to induce a totally flat charging profile across the EV population. In this scenario, there are $I = 1 { , } 0 0 0$ EV owners with different preferences $\theta ^ { i }$ . The grid operator knows from past observations that the EV agent population desires to have overall Φ � 168 MWh charged in their EV batteries during time horizon T. Furthermore, we assume that $P _ { 0 , t } = \mathrm { \bar { } } P _ { 0 } = 0 . 0 5$ monetary units per kWh. The main grid-balancing performance results are summarized in Figure 12 and Table 2, which include the performance of proposed capacity-based pricing configurations (discussed in Section 6.5) and a subset of benchmark approaches (discussed in Section 6.4) that were designed for inducing flat profiles.

Figure 12 shows the average hourly charging across all EV agents, and Table 2 summarizes key gridbalancing performance metrics. Whereas all proposed capacity-based configurations outperform all benchmark approaches in terms of every grid-balancing metric, we observe near-optimal performance of the computational heuristic (i.e., the proposed CBP-CH [-Distrib] configurations) in terms of matching the desired profile, that is, yielding near-optimal RMSE (0.02), peak (1.03), and PAPR values (1.07). The difference between the proposed approach and the desired profile, although extremely small, results from the stochasticity of driving behavior $E _ { t } ^ { i }$ and charging availability $\bar { \beta } _ { t } ^ { i }$ across time $t \in \mathbf { T }$ and across agents $i \in \mathbf { I } ,$ as well as from different sets of deadlines $\Delta ^ { i }$ and charging requirements $\Phi ^ { i }$ across agents i ∈ I. The increasing-block pricing is also performing reasonably well in inducing a flat profile, as it is explicitly designed to serve this purpose. However, its performance is still below our proposed configurations according to all grid-balancing metrics (Table 2).

Figure 12. (Color online) Performance of Proposed Artifact and Benchmarks: Inducing a Flat Charging Profile of 1 MWh  
![](/api/attachments/2VUSBQ36/fulltext/images/71a66775f8019c4b1f994c1a45325f33970313c61a63ebb729e90d8bd0eb0ba3.jpg)

Table 2. Inducing a Flat Charging Profile of 1 MWh: RMSE, Peak-to-Average Power Ratio, and Energy Peak

<table><tr><td></td><td>RMSE (MWh)</td><td>PAPR</td><td>Peak (MWh)</td></tr><tr><td>Real-world charging—flat pricing</td><td>0.88</td><td>2.89</td><td>2.03</td></tr><tr><td>Increasing-block pricing benchmark</td><td>0.25</td><td>1.63</td><td>1.32</td></tr><tr><td>CBP-AH [-Distrib]</td><td>0.24</td><td>1.46</td><td>1.24</td></tr><tr><td>CBP-CH [-Distrib]</td><td>0.02</td><td>1.07</td><td>1.03</td></tr><tr><td>Desired profile</td><td>0</td><td>1</td><td>1</td></tr></table>

In addition to the fact that the proposed approach outperforms the benchmarks in terms of grid-balancing objectives, another key advantage is that it can do it while satisfying revenue equivalence objectives, which the benchmarks are not designed to satisfy. As Theorem 3 shows, each vector from the optimal solution space outlined by Theorem 2 yields a different revenue while inducing the same desired profile. To illustrate this relationship between values and target revenues in this specific setup, in Figure 13 we show values of $\alpha _ { t }$ that generate different target revenues Ψ<sup>∗</sup>, while inducing the same desired profile D in the population in question. Note that for $\alpha _ { t } = 0$ the generated revenue results from the price component $P _ { 0 , t }$ .

To see this in practice, assume that the target revenue in this population is equivalent to that generated by the flat pricing, that is, $\Psi ^ { * } = 1 7 , 8 7 8 . 6$ monetary units. Such a revenue equivalence requirement (e.g., with flat pricing) might get imposed by market regulators or other stakeholders. Table 3 shows the performance of the proposed price-setting configurations in meeting revenue targets. In the most conservative information availability scenario, configuration CBP-AH generates 18,361 monetary units (deviation of 2.70% from the desired). In case the grid operator has some domain knowledge of distributional characteristics of the EV population charging needs (CBP-AH-Distrib), the artifact generates revenue of 17,903 which deviates only by 0.14% from the target, while inducing the same charging behavior as CBP-AH. For the computational heuristic, we observe that the linear relationship derived in Theorem 3 and shown in Figure 13 continues to exist in the constrained agent population case, albeit with some noise resulting from stochastic individual preferences and deadlines. Therefore, our computational heuristic is still able to leverage the structural form of Theorem 3 (by using the results of the analytical heuristic as a starting point) to reduce computational complexity, while maintaining high accuracy. Running CBP-CH-Distrib yields revenues of 17,864.0 (0.08% difference) for the configuration. In summary, the proposed IS-enabled capacity-based pricing solution outperforms all benchmarks in inducing desired demand and, equally importantly, can generate revenues with minimal deviations from the target without high computational complexity.

Figure 13. Illustration of Theorem 3: Revenue Ψ<sup>∗</sup> for Different Values of α Inducing the Same Flat Profile  
![](/api/attachments/2VUSBQ36/fulltext/images/a9481804657f1a695808e546acc34d07b78b2fdde472bcca13bfead9e95c03d4.jpg)

Table 3. Generating Target Revenue Ψ<sup>∗</sup> While Inducing a Flat Charging Profile of 1 MWh

<table><tr><td></td><td>RMSE (MWh)</td><td>Revenue</td><td>% Diff. from the target  $\Psi^{*}$ </td></tr><tr><td>CBP-AH</td><td>0.24</td><td>18,361.0</td><td>2.70</td></tr><tr><td>CBP-AH-Distrib</td><td>0.24</td><td>17,903.0</td><td>0.14</td></tr><tr><td>CBP-CH</td><td>0.02</td><td>17,900.0</td><td>0.12</td></tr><tr><td>CBP-CH-Distrib</td><td>0.02</td><td>17,864.0</td><td>0.08</td></tr><tr><td>Target revenue  $\Psi^{*}$ </td><td>0</td><td>17,878.6</td><td>0</td></tr></table>

The performance of meeting revenue targets illustrates the additional advantages of the proposed approach. The target-revenue-generation results remain highly consistent for other evaluation scenarios (which will be discussed below) as well, and are presented in Online Appendix H because of space limitations.

## 7.2. Complementing Household Demand: Volatility Reduction

We extend the previous setting to a case in which the grid operator aims to distribute the EV charging on top of the household demand so that their combination creates an overall flat demand curve. This is more challenging, as the pricing schemes have to induce a somewhat volatile EV charging profile. As before, the grid operator is facing a population of I � 1,000 EV owners with different stochastic private preferences ${ \theta ^ { i } } , \forall i \in \mathbf { I } .$ . We assume the grid operator is aware from past data that the EV population charges an amount of 26 MWh in total per day for covering their driving needs and that $P _ { 0 , t } = P _ { 0 } = 0 . 0 5$ monetary units per kWh.

Figures 14 and 15 compare the performance of the proposed approach to the benchmarks. We again observe that our proposed price-setting configurations demonstrate performance that is closest (as compared to all benchmarks) to the desired profile. The regular time-variable pricing without a capacity-pricing component (rate-independent, $\alpha _ { t } = 0 )$ yields the worst result, because all EV agents charge during the low-price peri ods of the early morning, creating a high peak of approximately 8.5 MWh. The outcome from the traditional flat pricing scheme is less severe for the grid, because it is driven by customer convenience and not pricing. Finally, the increasing-block pricing benchmark still exhibits the best performance among all the benchmarks, as it is more flexible and adaptable to the desired demand. However, this benchmark is not as flexible for inducing a desired demand profile of an arbitrary shape as the capacity-based pricing, which allows for a much finer control of the induced demand. As a result, the proposed approach achieves the best distribution of EV charging to complement the given household demand in this realistic environment. We quantify these results in Table 4. The proposed capacity-based pricing configurations achieve the lowest peak, the lowest (and closes to one) PAPR, indicating reduced demand volatility, and demonstrate the best fit to the desired profile (with RMSE as low as 0.03 MWh).

Figure 14. (Color online) Distributing EV Charging over Household Demand Toward a Flat Profile  
![](/api/attachments/2VUSBQ36/fulltext/images/443e8606a66879ce1fecae0505c5c28848cff405fb994633baa282f24225fe51.jpg)

Furthermore, Table A.4 in Online Appendix H illustrates excellent ability of the proposed capacity-based pricing configurations to generate target revenue while inducing a nonflat desired profile. This evaluation scenario further confirms that the proposed approach, leveraging analytical or computational heuristics, outperforms all benchmarks and yields near-optimal results with low computational complexity.

Figure 15. (Color online) Distributing EV Charging over Household Demand vs. Benchmarks  
![](/api/attachments/2VUSBQ36/fulltext/images/05df2b7fd65519518af975de53307b6daa23471d98776be032bfece72f3ce686.jpg)

Table 4. Distributing EV Charging over Household Demand Toward a Flat Profile: RMSE, Peak-to-Average Power Ratio, and Energy Peak

<table><tr><td></td><td>RMSE (MWh)</td><td>PAPR</td><td>Peak (MWh)</td></tr><tr><td>Real-world—flat pricing</td><td>1.12</td><td>2.22</td><td>4.23</td></tr><tr><td>Rate-independent—variable pricing</td><td>2.17</td><td>6.22</td><td>8.42</td></tr><tr><td>Increasing-block pricing benchmark</td><td>0.48</td><td>1.74</td><td>3.39</td></tr><tr><td>CBP-AH [-Distrib]</td><td>0.29</td><td>1.37</td><td>3.07</td></tr><tr><td>CBP-CH [-Distrib]</td><td>0.03</td><td>1.06</td><td>2.69</td></tr><tr><td>Desired profile</td><td>0</td><td>1</td><td>2.61</td></tr></table>

## 7.3. Following the Production of Photovoltaic (PV) Arrays: Increasing Sustainability

Increasing societal sustainability levels by facilitating a smoother integration of renewable sources is another important affordance that the proposed approach is designed to satisfy. As part of our evaluation, we explicitly include a scenario where the EV charging demand needs to be shaped to follow production curves of renewable sources. When the energy generation profile is very volatile as a result of renewable sources (such as solar or wind power), the consumption of this renewable production can be maximized to reduce waste of electricity.

In this setting, we assume that the grid operator desires to cover the majority of EV charging through the production of PV arrays, that is, solar panels, in the local area. We compare the performance of the proposed capacity-based pricing configurations only, as the traditional benchmarks are not designed to induce volatile demand profiles and, therefore, perform significantly worse in such situations. In this simulation experiment, there are I � 1,000 EV owners with different stochastic private preferences $\theta ^ { i } ,$ and we calibrate the mechanism so that it consumes all electricity produced by the PV arrays $\Phi = 5 2 2 . 5 6 $ MWh over time horizon T. The PV data used in this scenario are obtained from PV installations in Hudson, WI, USA, collected during April 25 to June 23, 2015.

In Figure 16 and Table 5, we see that our approach demonstrates excellent performance in inducing a profile that is very close to the desired profile, with RMSE � 0.83 MWh for the analytical heuristic and RMSE � 0.21 MWh for the computational heuristic. As an illustration of the inapplicability of other benchmarks for the volatile demand profile scenarios, the increasing-block pricing benchmark, which was the second-best approach in the previous two experiments, had $\mathrm { R M S E } = 4 . 6 5$ MWh in this case.

As in previous experiments, the proposed pricing scheme enables the grid operator to set prices in accordance with a revenue target even with highly vola tile demand profiles (see Online Appendix H fo details).

Figure 16. (Color online) Incentivizing EV Charging to Match the Production of PV Arrays  
![](/api/attachments/2VUSBQ36/fulltext/images/7acb375be22abf82b719afa4e04dfe433f01ac7c0608a78083ee9dce8ae1b3c8.jpg)

As an important robustness check, Online Appendix I explores the sensitivity of results when the desired demand might include some forecasting error, mainly resulting from the uncertainty of the renewable generation that is integrated in modern grids. The results show that our approach maintains its superior grid-balancing performance when the desired demand that is used to calculate the prices deviates from the actually observed available grid capacity.

Overall, the results show that the proposed approach can successfully induce charging profiles of different kinds (flat, volatile, etc.) while satisfying revenue goals. One of the main challenges of renewable sources is their volatile production patterns, which do not match the stable household demand. The results underscore the power of this approach in shaping the charging demand to follow a specific production profile. This approach can be generalized to follow production patterns of wind turbines or any other renewable sources and con tribute significantly to societal sustainability.

## 7.4. Robustness Check: Sensitivity of Results to EV Agent Capabilities

As an important sensitivity analysis, we extended the evaluation of our proposed IS-enabled pricing solution to settings that allow for more myopic and less planning-oriented EV agent capabilities, as opposed to more nuanced, forward-looking ones (i.e., with longerterm planning horizons and more specific information provided on charging availability and intermediate charging deadlines) that were discussed in Section 3.3 and considered in the main results above. We evaluate the performance of our approach in this new setting using the same three evaluation scenarios where the desired EV charging profiles are of different volatility levels, discussed in the preceding three subsections. Because of space limitations, we refer the reader to Online Appendix J for the results. Importantly, the results show that our approach maintains its superior performance against all benchmarks.

Table 5. Incentivizing EV Charging to Match the Production Pattern of PV Arrays

<table><tr><td></td><td>RMSE (MWh)</td></tr><tr><td>CBP-AH [-Distrib]</td><td>0.83</td></tr><tr><td>CBP-CH [-Distrib]</td><td>0.21</td></tr><tr><td>Desired profile</td><td>0</td></tr></table>

## 8. Discussion and Conclusions

EV charging coordination is an important challenge that sustainable cities must address (Ismagilova et al. 2019). Existing coordination solutions have shortcomings, which mostly result from their inability to achieve incentive alignment between grid operators and EV owners. We describe a novel EV charging coordination artifact that overcomes this challenge. It combines the decentralized decision making on the rational, self-interested EV owner side with a central coordination party that aims to induce a desired aggregate charging demand profile. It develops a capacity-based pricing scheme that is a function of EV charging rates, and creates incentives for charging at different rates over time depending on the desired demand profile. Our study is particularly important for Green IS, because the proposed artifact is able to induce EV demand profiles able to match or complement the generation profiles of any shape, including matching the flat generation profile, complementing the preexisting demand toward the flat overall profile, following the more complex generation profiles of renewable sources, etc. Because real-world scenarios can exhibit highly varying energy generation profiles and/or preexisting demand profiles from other (non-EV) sources, such matching capabilities help utilize the existing grid infrastructure more efficiently and, thus, reduce the need for installing additional infrastructure (with all the corresponding effects, for example, significant savings on materials such as copper, etc.). Also, the ability to shape the demand to follow the generation of renewable sources is of high importance for Green IS, because it allows, with the use of information and technology, increasing the usage of renewable sources leading to higher sustainability levels and savings on conventiona energy. And, increasing renewable energy source utilization leads to carbon emission reduction, one of the major Green IS objectives. Following the terminology of Watson et al. (2010) and building on Figure 1, the proposed artifact helps satisfy eco-equity objectives (grid balancing), eco-effectiveness objectives (renewable integration), as well as the needs of environmentally aware drivers who desire to charge their EVs using renewable sources.

In addition to the aforementioned overarching contributions toward Green IS, our specific research contributions are as follows. (1) We describe a novel IS-enabled pricing artifact that prices energy based on capacity. This artifact includes a dynamic component (charging rate-based price) that can be taken into account by the EV owner when selecting charging rates. As a result, it allows grid stakeholders to price different charging rates based on their impact on the grid (e.g., higher grid capacity required to complete fast charging). (2) As part of the proposed solution, we develop analytical price setting heuristics derived by understanding theoretical properties of the proposed pricing mechanism. (3) Using the analytical heuristics as a starting point, we develop smart computational, data-driven price-setting heuristics with low computational complexity that leverage the observed charging behavior to further improve grid-balancing outcomes. (4) The proposed approach provides built-in revenue balancing capabili ties, a key component that makes the proposed pricing scheme adaptable to various real-world economic envir onments. (5) The proposed approach provides near optimal solutions to the problem of inducing any desired electricity demand profile in a stochastic EV charging environment. This is important in terms of increasing societal sustainability and contributing to Green IS (Watson et al. 2010), as such an approach can be used to induce a charging demand following the production profile of a photovoltaic panel, in which case the EV charging demand can be covered with renewable energy. (6) The proposed approach also moves the state-of-the-art beyond certain restrictions that are common in the EV charging pricing literature. For example, our pricing scheme is able to achieve near-optimal grid-balancing outcomes without requiring numerous time-consuming learning iterations (common in methods with iterative/learning components), specialized knowledge about the reaction of EV owners to prices (aside from their rational, self-interested objectives), or highly restrictive desired demand profiles. Thus, one major advantage of our approach is its ability to adapt quickly to changing real-world environments. (7) We provide a very extensive evaluation of the proposed approach in multiple realistic grid-balancing scenarios.

At the same time, this work has significant practical, societal, and managerial implications for smart city stakeholders, such as for smart grid operators, energy providers, and urban mobility planners (Xu et al. 2018), who can use our solutions to reshape existing EV charg ing demand. Grid operators strive to ensure a reliable grid through reducing unsustainable demand peaks. Energy providers can use these results to manage peak demand in their customer portfolios and, thereby, manage their capacity costs as well as the high cost of electricity during peak demand periods. Moreover, urban mobility planners can use our rapidly adaptable mecha nism as an incentive toward a sustainable EV adoption in high-density urban environments, ensuring lower carbon emissions and stability of the network. Also, utility companies can use our mechanism to maintain demand and revenue targets while complying with exogenous price constraints. Finally, EV drivers can benefit from grid balancing, as they are exposed to lower risks of blackouts, and from the ability to subscribe to sustainable electricity tariffs that consume renewable energy. The latter contributes to Green IS, as we offer a method to directly integrate renewable sources in current societies with the use of IT/IS-enabled solutions.

This work opens up a number of important avenues for future research, going beyond the specific settings of this study. For example, all presented results assume that the chosen capacity-based prices do not alter private driving needs and charging availability constraints of the EV users. Future studies could investigate the more extreme capacity-based pricing scenarios and their impact on consumer preferences and on the overall EV driving and charging behavior. In such a scenario, dynamic game-theoretic frameworks with a leader and followers could be examined. Also, in this work we assume that all EV owners are subscribed to the proposed pricing scheme. Future work could examine the effect of the proposed scheme in the presence of other tariffs available to the EV owners. Finally, an exciting future direction would be to enhance the current study with the inclusion of granular Internet-of-Things (IoT)- related information reflecting more nuanced agent constraints and preferences, which could lead to even more efficient outcomes.

## Acknowledgments

The authors thank Prof. Gautam Pant (senior editor), the associate editor, and the anonymous reviewers for the detailed and constructive reviews. Furthermore, the authors thank Prof. Ariana Polyviou and Dr. Nefeli Malamaki for the in-depth feedback.

## Endnotes

<sup>1</sup> See http://www.ev-volumes.com/.

<sup>2</sup> The European Network of Transmission System Operators for Electricity foresees the need for e150 billion of investments in grid infrastructure over a period of 10 years (ENTSO-E 2016).

<sup>3</sup> The focus of this paper is on reshaping the existing EV charging demand toward a desired profile. Changing—reducing or increasing—the overall magnitude of the EV charging demand, for example, by trying to alter fundamentally the population’s transportation needs and habits, is a very different research issue that is beyond the scope of this study.

<sup>4</sup> Congestion can have many causes—for example, consumers’ desire to charge at a certain time because it is convenient or avalanche effects, when the majority of consumers charge at low-price time periods—and can result in undesirable grid overload.

<sup>5</sup> For example, customers pay less for energy in exchange for having their chargers remotely cut off at times of the grid operator’s choosing.

<sup>6</sup> See https://newmotion.com/en/location-solutions/home-charging.

<sup>7</sup> See https://www.company.enelxway.com/en/app-electric-vehiclescharging.

<sup>8</sup> See https://www.teslarati.com/tesla-apps-dutch-developer-leveragesreal-time-electricity-rates-charging/.

<sup>9</sup> Both the terms grid operator and smart grid manager are used interchangeably to capture the variety in different entities managing the grid or segments of the grid in different parts of the world.

<sup>10</sup> Time appears as a subscript in all variables or parameters of interest.

<sup>11</sup> A preliminary version of this formulation was presented by Valogianni et al. (2015).

<sup>12</sup> Time t appears as a subscript and agent index i appears as a superscript in variables and parameters of interest.

<sup>13</sup> For expositional simplicity, this theorem assumes ${ \cal S } o { \cal C } _ { t = 0 } ^ { i } = 0 .$

<sup>14</sup> This is straightforward from Theorem 2, by using D=w (instead of D) as a desired charging profile.

<sup>15</sup> Available at https://opendata.cbs.nl/statline/#/CBS/nl/dataset/ 81124NED/table?fromstatweb.

<sup>16</sup> The exact arrival and departure times are not specified in the data set; hence, we probabilistically draw arrival and departure times depending on the driving motivation. For example, driving to work for most of the drivers takes place in the morning; however, in less frequent instances driving to work takes place at night. Such arrival and departure probabilities are included for all activities and all population clusters.

<sup>17</sup> See https://opendata.cbs.nl/statline/#/CBS/nl/dataset/81124NED/ table?fromstatweb.

<sup>18</sup> The “Octopus Energy Agile tariff” (https://octopus.energy/ smart/agile/) uses wholesale electricity data and is adjusted every hour or 30 minutes for the next 24 hours. The “Eneco Dynamisch” tariff (https://news.eneco.com/eneco-introduces-a-dynamic-energycontract/) is available in the Netherlands and presents retail electricity prices that vary per hour depending on the electricity market movements.

## References

Akasiadis C, Chalkiadakis G (2016) Decentralized large-scale electricity consumption shifting by prosumer cooperatives. Kaminka GA, Fox M, Bouquet P, Hu¨ llermeier E, Dignum V, eds. ECAI ‘16: Proc. 22nd Eur. Conf. Artificial Intelligence (IOS Press, Amster dam), 175–183.

Al-Ghussain L, Abubaker AM, Ahmad AD (2021) Superposition of renewable-energy supply from multiple sites maximizes demand-matching: Towards 100% renewable grids in 2050. Appl. Energy 284:116402.

Alizadeh M, Wai H-T, Chowdhury M, Goldsmith A, Scaglione A, Javidi T (2016) Optimal pricing to manage electric vehicles in coupled power and transportation networks. IEEE Trans. Con trol Network Sustems 4(4):863–875

Ansarin M, Ghiassi-Farrokhfal Y, Ketter W, Collins J (2020) The economic consequences of electricity tariff design in a renewable energy era. Appl. Energy 275:115317.

Beaude O, He Y, Hennebel M (2013) Introducing decentralized EV charging coordination for the voltage regulation. IEEE PES ISGT Europe 2013 (IEEE, New York), 1–5.

Benitez-Amado J, Walczuch RM (2012) Information technology, the organizational capability of proactive corporate environmental strategy and firm performance: A resource-based analysis. Eur J. Inform. Systems 21(6):664–679.

Bichler M, Gupta A, Ketter W (2010) Designing smart markets Inform. Systems Res. 21(4):688–699.

Blaschke MJ (2022) Dynamic pricing of electricity: Enabling demand response in domestic households. Energy Policy 164:112878.

Borenstein S (2012) The redistributional impact of nonlinear electric ity pricing. Amer. Econom. J. Econom. Policy 4(3):56–90.

Brandt T, Feuerriegel S, Neumann D (2013) Shaping a sustainable society: How information systems utilize hidden synergies between green technologies. Proc. 34th Internat. Conf. Inform. Systems (ICIS) (Association for Information Systems, Atlanta).

Brandt T, Feuerriegel S, Neumann D (2018a) Modeling interferences in information systems design for cyberphysical systems: Insights from a smart grid application. Eur. J. Inform. Systems 27(2):207–220.

Brandt T, DeForest N, Stadler M, Neumann D (2014) Power systems 2.0: Designing an energy information system for microgrid operation. Myers MD, Straub DW, eds. Proc. Internat. Conf. Inform. Systems Building Better World through Inform. Systems (ICIS) (Association for Information Systems, Atlanta), 163–180.

Brandt T, Ketter W, Kolbe LM, Neumann D, Watson RT (2018b) Smart cities and digitized urban management. Bus. Inform. Systems Engrg. 60(3):193–195.

Brendel AB, Zapadka P, Kolbe LM (2018) Design science research in green IS—Analyzing the past to guide future research. Bednar PM, Frank U, Kautz K, eds. 26th Eur. Conf. Inform. Systems Beyond Digitization Facets Socio-Tech. Change, ECIS 2018 (Portsmouth, UK), 115.

Bustos-Turu G, van Dam KH, Acha S, Shah N (2014) Estimating plug-in electric vehicle demand flexibility through an agent based simulation model. IEEE PES Innovative Smart Grid Tech. Eur. (IEEE, New York), 1–6.

Canizes B, Soares J, Vale Z, Corchado JM (2019) Optimal distribution grid operation using DLMP-based pricing for electric vehicle charging infrastructure in a smart city. Energies 12(4):686.

Chaudhari K, Kandasamy NK, Krishnan A, Ukil A, Gooi HB (2018) Agent-based aggregated behavior modeling for electric vehicle charging load. IEEE Trans. Indust. Informatics 15(2):856–868.

Corbett J (2013) Designing and using carbon management systems to promote ecologically responsible behaviors. J. Assoc. Inform. Systems 14(7):339–378.

Dai Y, Qi Y, Li L, Wang B, Gao H (2021) A dynamic pricing scheme for electric vehicle in photovoltaic charging station based on Stackelberg game considering user satisfaction. Comput. Indust. Engrg. 154:107117.

Dallinger D, Wietschel M (2012) Grid integration of intermittent renewable energy sources using price-responsive plug-in elec tric vehicles. Renewable Sustainable Energy Rev. 16(5):3370–3382.

Dao V, Langella I, Carbo J (2011) From green to sustainability: Infor mation technology and an integrated sustainability framework. J. Strategic Inform. Systems 20(1):63–79.

Das R, Wang Y, Busawon K, Putrus G, Neaimeh M (2021) Real-time multi-objective optimisation for electric vehicle charging management. J. Cleaner Production 292:126066.

De Craemer K, Vandael S, Claessens B, Deconinck G (2014) An event-driven dual coordination mechanism for demand side management of PHEVs. IEEE Trans. Smart Grid 5(2):751–760.

Dedrick J (2010) Green IS: Concepts and issues for information systems research. Comm. Assoc. Inform. Systems 27(1):11–18.

D’hulst R, De Ridder F, Claessens B, Knapen L, Janssens D (2015) Decentralized coordinated charging of electric vehicles consid ering locational and temporal flexibility. Internat. Trans. Electr. Energy Systems 25(10):2562–2575.

Ensslen A, Ringler P, Do¨rr L, Jochem P, Zimmermann F, Fichtner W (2018) Incentivizing smart charging: Modeling charging tariffs for electric vehicles in German and French electricity markets. Energy Res. Soc. Sci. 42:112–126.

ENTSO-E (2016) Ten-year network development plan 2016. European Network of Transmission System Operators for Electricity, Brussels.

Fabra N, Rapson D, Reguant M, Wang J (2021) Estimating the elasticity to real-time pricing: Evidence from the Spanish electricity market. AEA Papers Proc. 111:425–429.

Fang C, Lu H, Hong Y, Liu S, Chang J (2020) Dynamic pricing for electric vehicle extreme fast charging. IEEE Trans. Intelligent Transportation Systems 22(1):531–541.

Faruqui A, Hledik RM, Levy A, Madian AL (2011) Will smart price induce smart charging of electric vehicles? Preprint, submitted August 25, http://dx.doi.org/10.2139/ssrn.1915658.

Fescioglu-Unver N, Aktas¸ MY (2023) Electric vehicle charging service operations: A review of machine learning applications for infrastructure planning, control, pricing and routing. Renewable Sustainable Energy Rev. 188:113873.

Flath CM, Ilg JP, Gottwalt S, Schmeck H, Weinhardt C (2013) Improving electric vehicle charging coordination through area pricing. Transportation Sci. 48(4):619–634.

Freier J, von Loessl V (2022) Dynamic electricity tariffs: Designing reasonable pricing schemes for private households. Energy Econom. 112:106146.

Freitas S, Brito M (2019) Non-cumulative only solar photovoltaics for electricity load-matching. Renewable Sustainable Energy Rev. 109:271–283.

Fridgen G, Mette P, Thimmel M (2014a) The value of information exchange in electric vehicle charging. Proc. 35th Internat. Conf. Inform. Systems (ICIS) (Auckland, New Zealand).

Fridgen G, Ha¨fner L, Ko¨nig C, Sachs T (2014b) Toward real options analysis of IS-enabled flexibility in electricity demand. Proc. 35th Internat. Conf. Inform. Systems (ICIS) (Auckland, New Zealand).

Gan L, Topcu U, Low SH (2013) Optimal decentralized protocol for electric vehicle charging. IEEE Trans. Power Systems 28(2):940–951.

Gerding EH, Robu V, Stein S, Parkes DC, Rogers A, Jennings NR (2011) Online mechanism design for electric vehicle charging. 10th Internat. Conf. Autonomous Agents Multiagent Systems (AAA-MAS 2011), vol. 2 (International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC), 811–818.

Gong L, Cao W, Liu K, Zhao J (2020) Optimal charging strategy for electric vehicles in residential charging station under dynamic spike pricing policy. Sustainable Cities Soc. 63:102474.

Gottwalt S (2015) Managing flexible loads in residential areas. PhD thesis, Karlsruher Institut fu¨ r Technologie (KIT), Karlsruhe, Germany.

Gottwalt S, Ketter W, Block C, Collins J, Weinhardt C (2011) Demand side management—A simulation of household behavior under variable prices. Energy Policy 39(12):8163–8174.

Gregor S, Hevner AR (2013) Positioning and presenting design science research for maximum impact. MIS Quart. 37(2):337–355.

Guo Y, Liu X, Yan Y, Zhang N, Su W (2014) Economic analysis of plug-in electric vehicle parking deck with dynamic pricing. 2014 IEEE PES General Meeting Conf. Exposition (IEEE, New York), 1–5.

Hafez O, Bhattacharya K (2016) Integrating EV charging stations as smart loads for demand response provisions in distribution systems. IEEE Trans. Smart Grid 9(2):1096–1106.

Hajforoosh S, Masoum MA, Islam SM (2015) Real-time charging coordination of plug-in electric vehicles based on hybrid fuzzy discrete particle swarm optimization. Electric Power Systems Res. 128:19–29.

Hernandez-Leal P, Taylor ME, de Cote EM, Sucar LE (2015) Bidding in non-stationary energy markets. AAMAS’15: Internat. Conf. Autonomous Agents Multiagent Systems (Istanbul), 1709–1710.

Hu J, Morais H, Sousa T, Lind M (2016a) Electric vehicle fleet management in smart grids: A review of services, optimization and control aspects. Renewable Sustainable Energy Rev. 56:1207–1226.

Hu S, Souza GC, Ferguson ME, Wang W (2015) Capacity investment in renewable energy technology with supply intermittency: Data granularity matters! Manufacturing Service Oper Management 17(4):480–494.

Hu J, You S, Lind M, Ostergaard J (2014) Coordinated charging of electric vehicles for congestion prevention in the distribution grid. IEEE Trans. Smart Grid 5(2):703–711.

Hu Z, Zhan K, Zhang H, Song Y (2016b) Pricing mechanisms design for guiding electric vehicle charging to fill load valley. Appl. Energy 178:155–163.

Huang Q, Yang L, Zhou C, Luo L, Wang P (2023) Pricing and energy management of EV charging station with distributed renewable energy and storage. Energy Rep. 9(Suppl. 1):289–295.

International Energy Agency (2017) Global EV outlook. Organisa tion for Economic Co-operation and Development, Paris.

International Energy Agency (2021) Global EV outlook. Organisa tion for Economic Co-operation and Development, Paris.

Ipakchi A, Albuyeh F (2009) Grid of the future. IEEE Power Energy Magazine 7(2):52–62.

Ismagilova E, Hughes L, Dwivedi YK, Raman KR (2019) Smart cities: Advances in research—An information systems perspec tive. Internat. J. Inform. Management 47:88–100.

Ito K (2014) Do consumers respond to marginal or average price? Evidence from nonlinear electricity pricing. Amer. Econom. Rev. 104(2):537–563.

Jiang DR, Powell WB (2016) Practicality of nested risk measures for dynamic electric vehicle charging. Preprint, submitted May 10, https://arxiv.org/abs/1605.02848.

Kahlen MT, Ketter W, van Dalen J (2018) Electric vehicle virtual power plant dilemma: Grid balancing versus customer mobil ity. Production Oper. Management 27(11):2054–2070.

Kamankesh H, Agelidis VG, Kavousi-Fard A (2016) Optimal scheduling of renewable micro-grids considering plug-in hybrid elec tric vehicle charging demand. Energy 100:285–297.

Kang J, Duncan SJ, Mavris DN (2013) Real-time scheduling techni ques for electric vehicle charging in support of frequency regu lation. Procedia Comput. Sci. 16:767–775.

Ketter W, Schroer K, Valogianni K (2023) Information systems research for smart sustainable mobility: A framework and cal for action. Inform. Systems Res. 34(3):1045–1065.

Ketter W, Collins J, Saar-Tsechansky M, Marom O (2018) Information systems for a smart electricity grid: Emerging challenges and opportunities. ACM Trans. Management Inform. Systems 9(3):1–22.

Ketter W, Padmanabhan B, Pant G, Raghu T (2020) Addressing soci etal challenges through analytics: An ESG ICE framework and research agenda. J. Assoc. Inform. Systems 21(5):9.

Ketter W, Peters M, Collins J, Gupta A (2016a) Competitive benchmarking: An IS research approach to address wicked problems with big data and analytics. MIS Quart. 40(4):1057–1080.

Ketter W, Peters M, Collins J, Gupta A (2016b) A multiagent competitive gaming platform to address societal challenges. MIS Quart. 40(2):447–460.

Kim S-J, Giannakis GB (2016) An online convex optimization approach to real-time energy pricing for demand response. IEEE Trans. Smart Grid 8(6):2784–2793.

Klo¨r B, Monhof M, Beverungen D, Bra¨uer S (2018) Design and evaluation of a model-driven decision support system for repurposing electric vehicle batteries. Eur. J. Inform. Systems 27(2):171–188.

Krause SM, Bo¨rries S, Bornholdt S (2015) Econophysics of adaptive power markets: When a market does not dampen fluctuations but amplifies them. Phys. Rev. E 92:012815.

Lagomarsino M, van der Kam M, Parra D, Hahnel UJ (2022) Do I need to charge right now? Tailored choice architecture design can increase preferences for electric vehicle smart charging. Energy Policy 162:112818.

Lee S, Choi D-H (2021) Dynamic pricing and energy management for profit maximization in multiple smart electric vehicle charging stations: A privacy-preserving deep reinforcement learning approach. Appl. Energy 304:117754.

Leemput N, Geth F, Van Roy J, Olivella-Rosell P, Driesen J, Sumper A (2015) MV and LV residential grid impact of combined slow and fast charging of electric vehicles. Energies 8(3):1760–1783.

Li F (2007) Continuous locational marginal pricing (CLMP). IEEE Trans. Power Systems 22(4):1638–1646.

Li R, Wu Q, Oren SS (2014) Distribution locational marginal pricing for optimal electric vehicle charging management. IEEE Trans. Power Systems 29(1):203–211.

Li Y, Wang J, Wang W, Liu C, Li Y (2023) Dynamic pricing based electric vehicle charging station location strategy using reinforcement learning. Energy 281:128284.

Liang S, Zhu B, He J, He S, Ma M (2023) A pricing strategy for electric vehicle charging in residential areas considering the uncertainty of charging time and demand. Comput. Comm. 199:153–167.

Limmer S (2019) Dynamic pricing for electric vehicle charging – A literature review. Energies 12(18):3574.

Limmer S, Rodemann T (2019) Peak load reduction through dynamic pricing for electric vehicle charging. Internat. J. Electr. Power Energy Systems 113:117–128.

Lin J, Xiao B, Zhang H, Yang X, Zhao P (2021) A novel underfill-SOC based charging pricing for electric vehicles in smart grid. Sustainable Energy Grids Networks 28:100533.

Liu L, Zhou K (2022) Electric vehicle charging scheduling considering urgent demand under different charging modes. Energ 249:123714.

Liu D, Wang W, Wang L, Jia H, Shi M (2021) Dynamic pricing strategy of electric vehicle aggregators based on DDPG reinforcement learning algorithm. IEEE Access 9:21556.

Liu H, Qi J, Wang J, Li P, Li C, Wei H (2016a) EV dispatch control for supplementary frequency regulation considering the expectation of EV owners. IEEE Trans. Smart Grid 9(4):3763–3772.

Liu Z, Wu Q, Oren SS, Huang S, Li R, Cheng L (2016b) Distribution locational marginal pricing for optimal electric vehicle charging through chance constrained mixed-integer programming. IEEE Trans. Smart Grid 9(2):644–654.

Liu Y, Yuen C, Huang S, Hassan NU, Wang X, Xie S (2014) Peak-toaverage ratio constrained demand-side management with consumer’s preference in residential smart grid. IEEE J. Selected Topics Signal Processing 8(6):1084–1097.

Loeser F, Recker J, Brocke J. V, Molla A, Zarnekow R (2017) How IT executives create organizational benefits by translating environmental strategies into Green IS initiatives. Inform. Systems J. 27(4):503–553.

Loock C, Staake T, Thiesse F (2013) Motivating energy-efficient behavior with Green IS: An investigation of goal setting and the role of defaults. MIS Quart. 37(4):1313–1332.

Malhotra A, Melville NP, Watson RT (2013) Spurring impactful research on information systems for environmental sustainability. MIS Quart. 37(4):1265–1274.

Masoum AS, Deilami S, Abu-Siada A, Masoum MA (2015) Fuzzy approach for online coordination of plug-in electric vehicle charging in smart grid. IEEE Trans. Sustainable Energy 6(3): 1112–1121.

McPherson M, Ismail M, Hoornweg D, Metcalfe M (2018) Planning for variable renewable energy and electric vehicle integration under varying degrees of decentralization: A case study in Lusaka, Zambia. Energy 151:332–346.

Melville NP (2010) Information systems innovation for environmen tal sustainability. MIS Quart. 34(1):1–21.

Mocci S, Natale N, Pilo F, Ruggeri S (2014) Multi-agent control system to coordinate optimal electric vehicles charging and demand response actions in active distribution networks. 3rd Renewable Power Generation Conf. (RPG 2014) (IET, Stevenage UK), 3-1.

Moghaddam V, Yazdani A, Wang H, Parlevliet D, Shahnia F (2020) An online reinforcement learning approach for dynamic pricing of electric vehicle charging stations. IEEE Access 8:130305–130313.

Mohseni S, Brent AC, Burmester D (2020) Community resilienceoriented optimal micro-grid capacity expansion planning: The

case of Totarabank eco-village, New Zealand. Energies 13(15):3970.

Mrkos J, Komenda A, Jakob M (2018) Revenue maximization for electric vehicle charging service providers using sequential dynamic pricing. AAMAS ’18: Autonomous Agents MultiAgent Systems (Stockholm), 832–840.

Muratori M (2018) Impact of uncoordinated plug-in electric vehicle charging on residential power demand. Nature Energy 3(3):193–201.

Natividad F, Folk RY, Yeoh W, Cao H (2017) On the use of off-theshelf machine learning techniques to predict energy demands of power TAC consumers. Ceppi S, David E, Hajaj C, Robu V, Vetsikas IA, eds. Agent-Mediated Electronic Commerce. Designing Trading Strategies and Mechanisms for Electronic Markets (Springer, Cham, Switzerland), 112–126.

Nicholas M, Hall D (2018) Lessons learned on early electric vehicle fast-charging deployments. International Council on Clean Transportation, Washington, DC.

Papadopoulos P, Jenkins N, Cipcigan LM, Grau I, Zabala E (2013) Coordination of the charging of electric vehicles using a multiagent system. IEEE Trans. Smart Grid 4(4):1802–1809.

Peffers K, Tuunanen T, Rothenberger MA, Chatterjee S (2007) A design science research methodology for information systems research. J. Management Inform. Systems 24(3):45–77.

Peters M, Ketter W, Saar-Tsechansky M, Collins JE (2013) A reinforcement learning approach to autonomous decision-making in smart electricity markets. Machine Learn. 92:5–39.

Pham A, Jin T, Novoa C, Qin J (2019) A multi-site production and microgrid planning model for net-zero energy operations. Internat. J. Production Econom. 218:260–274.

Puller SL, West J (2013) Efficient retail pricing in electricity and nat ural gas markets. Amer. Econom. Rev. 103(3):350–355.

Rasheed MB, Awais M, Alquthami T, Khan I (2020) An optimal scheduling and distributed pricing mechanism for multi-region electric vehicle charging in smart grid. IEEE Access 8:40298–40312.

Reneses J, Ortega MPR (2014) Distribution pricing: Theoretical principles and practical approaches. IET Generation Transmission Distribution 8(10):1645–1655.

Rieger A, Thummert R, Fridgen G, Kahlen M, Ketter W (2016) Estimating the benefits of cooperation in a residential microgrid: A data-driven approach. Appl. Energy 180:130–141.

Robu V, Chalkiadakis G, Kota R, Rogers A, Jennings NR (2016) Rewarding cooperative virtual power plant formation using scoring rules. Energy 117:19–28.

Ru´ bio TR, Queiroz J, Cardoso HL, Rocha AP, Oliveira E (2016) TugaTAC broker: A fuzzy logic adaptive reasoning agent for energy trading. Rovatsos M, Vouros G, Julian V, eds. Multi-Agent Systems and Agreement Technologies. EUMAS 2015, AT 2015 (Springer, Cham, Switzerland), 188–202.

Santoyo C, Nilsson G, Coogan S (2023) Resource aware pricing for electric vehicle charging. Automatica 148:110733.

Schey S, Scoffield D, Smart J (2012) A first look at the impact of elec tric vehicle charging on the electric grid in the EV project. World Electric Vehicle J. 5(3):667–678.

Schweppe FC, Caramanis MC, Tabors RD, Bohn RE (1988) Spot Pric ing of Electricity (Springer Science & Business Media, New York).

Seidel S, Recker J, Vom Brocke J (2013) Sensemaking and sustainable practicing: Functional affordances of information systems in green transformations. MIS Quart. 37(4):1275–1299.

Sheppard C, Waraich R, Campbell A, Pozdnukov A, Gopal AR (2017) Modeling plug-in electric vehicle charging demand with BEAM: The framework for behavior energy autonomy mobility. Technical report, Lawrence Berkeley National Laboratory, Berkeley, CA.

Soltani NY, Kim S-J, Giannakis GB (2015) Real-time load elasticity tracking and pricing for electric vehicle charging. IEEE Trans. Smart Grid 6(3):1303–1313.

Stein S, Gerding EH, Nedea A, Rosenfeld A, Jennings NR (2017) Market interfaces for electric vehicle charging. J. Artificial Intelligence Res. 59:175–227.

Tan J, Wang L (2016) A game-theoretic framework for vehicle-togrid frequency regulation considering smart charging mecha nism. IEEE Trans. Smart Grid 8(5):2358–2369.

Tucker N, Alizadeh M (2018) Online pricing mechanisms for electric vehicle management at workplace charging facilities. 2018 56th Annual Allerton Conf. Comm. Control Comput. (IEEE Press, New York), 351–358.

United Nations Framework Convention on Climate Change (2015) Adoption of the Paris Agreement. United Nations Framework Convention on Climate Change, Paris.

Valogianni K, Ketter W, Collins J (2015) A multiagent approach to variable-rate electric vehicle charging coordination. AAMAS’15: Internat. Conf. Autonomous Agents Multiagent Systems (International Foundation for Autonomous Agents and Multiagent Sys tems, Richland, SC), 1131–1139.

Valogianni K, Ketter W, Collins J, Zhdanov D (2014) Enabling sustainable smart homes: An intelligent agent approach. 35th Internat. Conf. Inform. Systems (ICIS) (Auckland, New Zealand)

Valogianni K, Ketter W, Collins J, Zhdanov D (2020) Sustainabl electric vehicle charging using adaptive pricing. Production Oper. Management 29(6):1550–1572.

Vandael S, Claessens B, Hommelberg M, Holvoet T, Deconinck G (2013) A scalable three-step approach for demand side management of plug-in hybrid vehicles. IEEE Trans. Smart Grid 4(2):720–728.

Venable J, Pries-Heje J, Baskerville R (2016) FEDS: A framework for evaluation in design science research. Eur. J. Inform. Systems 25(1):77–89.

Verzijlbergh RA, Grond MO, Lukszo Z, Slootweg JG, Ilic MD (2012) Network impacts and cost savings of controlled EV charging IEEE Trans. Smart Grid 3(3):1203–1212.

vom Brocke J, Watson RT, Dwyer C, Elliot S, Melville N (2013) Green information systems: Directives for the IS. Comm. Assoc. Inform. Systems 33(1):509–520.

Wang K, Wang H, Yang J, Feng J, Li Y, Zhang S, Okoye MO (2022) Electric vehicle clusters scheduling strategy considering realtime electricity prices based on deep reinforcement learning. Energy Rep. 8(Suppl. 4):695–703.

Watson RT, Boudreau M-C, Chen A (2010) Information systems and environmentally sustainable development: Energy infor matics and new directions for the IS community. MIS Quart. 34(1):23–38.

Wen C-K, Chen J-C, Teng J-H, Ting P (2012) Decentralized plug-in electric vehicle charging selection algorithm in power systems. IEEE Trans. Smart Grid 3(4):1779–1789.

Wolak FA (2011) Do residential customers respond to hourly prices? Evidence from a dynamic pricing experiment. Amer. Econom. Rev. 101(3):83–87.

Wooldridge M, Jennings N (1995) Intelligent agents: Theory and practice. Knowledge Engrg. Rev. 10(2):115–152.

Wu OQ, Yu¨ cel S, Zhou Y (2022) Smart charging of electric vehicles: An innovative business model for utility firms. Manufacturing Service Oper. Management 24(5):2481–2499.

Wu X, Gong J, Greenwood BN, Song Y (2019) No longer riding dirty: The effect of electric vehicle subsidies on the diffusion of emerging technologies in automobile markets. Preprint, submit ted April 16, https://dx.doi.org/10.2139/ssrn.3373096.

Xiong Y, Gan J, An B, Miao C, Soh YC (2016) Optimal pricing for efficient electric vehicle charging station management. Thangarajah J, Tuyls K, Jonker C, Marsella S, eds. Proc. 15th Internat. Conf. Autonomous Agents Multiagent Systems (AAMAS 2016) (International Foundation for Autonomous Agents and Multiagent Systems, Richland, SC), 749–757.

Xu X, Niu D, Li Y, Sun L (2020) Optimal pricing strategy of electric vehicle charging station for promoting green behavior based on time and space dimensions. J. Adv. Transportation 2020(1):8890233.

Xu Y, C¸olak S, Kara EC, Moura SJ, Gonza´lez MC (2018) Planning for electric vehicle needs by coupling charging profiles with urban mobility. Nature Energy 3(6):484–493.

Yan Q, Manickam I, Kezunovic M, Xie L (2014) A multi-tiered real-time pricing algorithm for electric vehicle charging stations. 2014 IEEE Transportation Electrification Conf. Expo (ITEC ’14) (IEEE, New York), 1–6.

Yao L, Lim WH, Tsai TS (2017) A real-time charging scheme for demand response in electric vehicle parking station. IEEE Trans. Smart Grid 8(1):52–62.

Yoon JH, Bladick R, Novoselac A (2014) Demand response for residential buildings based on dynamic price of electricity. Energy Buildings 80:531–541.

Yoon S-G, Choi Y-J, Park J-K, Bahk S (2015) Stackelberg-game-based demand response for at-home electric vehicle charging. IEEE Trans. Vehicular Tech. 65(6):4172–4184.

Zanvettor GG, Casini M, Smith RS, Vicino A (2022) Stochastic energy pricing of an electric vehicle parking lot. IEEE Trans. Smart Grid 13(4):3069–3081.

Zhang N, Hu Z, Han X, Zhang J, Zhou Y (2015) A fuzzy chanceconstrained program for unit commitment problem considering demand response, electric vehicle and wind power. Internat. J. Electr. Power Energy Systems 65:201–209.

Zhang Q, Hu Y, Tan W, Li C, Ding Z (2020) Dynamic time-of-use pricing strategy for electric vehicle charging considering user satisfaction degree. Appl. Sci. 10(9):3247.

Zhang K, Xu L, Ouyang M, Wang H, Lu L, Li J, Li Z (2014) Optimal decentralized valley-filling charging strategy for electric vehicles. Energy Conversion Management 78: 537–550.

Zhong J, He L, Li C, Cao Y, Wang J, Fang B, Zeng L, Xiao G (2014) Coordinated control for large-scale EV charging facilities and energy storage devices participating in frequency regulation Appl. Energy 123:253–262.

Zhou K, Cheng L, Lu X, Wen L (2020) Scheduling model of electric vehicles charging considering inconvenience and dynamic electricity prices. Appl. Energy 276:115455.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
