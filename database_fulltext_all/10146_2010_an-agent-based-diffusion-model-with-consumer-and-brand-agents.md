---
otero_id: 10146
otero_key: "QATXQ82H"
title: "An agent-based diffusion model with consumer and brand agents"
authors: "Mary E. Schramm; Kevin J. Trainor; Murali Shanker; Michael Y. Hu"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An agent-based diffusion model with consumer and brand agents

Mary E. Schramm <sup>a,</sup>⁎, Kevin J. Trainor <sup>b</sup>, Murali Shanker <sup>a</sup>, Michael Y. Hu <sup>a</sup>

<sup>a</sup> Kent State University, Kent, OH, United States <sup>b</sup> Canisius College, Buffalo, NY, United States

## a r t i c l e i n f o

Article history: Received 7 September 2009 Received in revised form 20 May 2010 Accepted 8 August 2010 Available online 12 August 2010

Keywords: Adoption Diffusion Innovation Agent-based modeling Brand Product

## a b s t r a c t

Market members interact within a complex, adaptive system to effect adoption decisions and the resulting diffusion of innovations. Agent-based modeling (ABM) is a methodology well suited for simulating this system. It complements and extends econometric approaches by incorporating interactions among system members, and adaptation in the system, revealing emergent results. Since ABM allows study at the individual unit level, heterogeneity among system members is re<sup>fl</sup>ected and modeling at the brand level is possible. Here an ABM with consumer and brand agents is described. The brand and product diffusion curve output allows study of diffusion at micro and macro levels, respectively

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

The diffusion of innovations by consumers is a topic of ongoing interest to researchers and marketing managers. Diffusion of innovations in the social system re<sup>fl</sup>ects adoption decisions made by individual consumers. These decisions are made in a complex, adaptive system and result from the interactions among individual's personal characteristics, perceived characteristics of the innovation, and social in<sup>fl</sup>uence [12].

There are two broad approaches to modeling diffusion: econometric and explanatory. Econometric approaches, such as the Bass [1] model, “describe and forecast the diffusion of an innovation in a social system” [21, p. 1]. Econometric approaches forecast growth within a product category by modeling the timing of <sup>fi</sup>rst-purchases of the innovation by consumers [21]. Econometric modeling is most applicable when market growth rate and market size are of primary interest [28].

Explanatory models, such as the “consumer diffusion paradigm” proposed by Gatignon and Robertson [12], establish that the diffusion of a product in a de<sup>fi</sup>ned market is equivalent to the aggregation of individual consumer adoption decisions. Adoption is primarily a function of three sets of consumer-related factors: personal characteristics, perceived innovation characteristics, and the consumer's exposure to social in<sup>fl</sup>uence [12,30]. The explanatory modeling approach is most applicable when developing marketing strategies such as segmentation, targeting, and product positioning [21]. This type of model does not support diffusion curve development.

Although established models have provided a strong basis for diffusion research, they do have limitations. ABM has the potential to complement these approaches since it addresses many of their limitations. However, since outputs differ among the models, ABM does not replace econometric or explanatory models [10,36]. In established models, the ability to re<sup>fl</sup>ect real-world dynamics is limited since they do not incorporate the effect of interactions that occur among members of the social system (i.e., market segment) and brands during the diffusion process [10]. Their predictive power is especially poor in cases where the consumer population is very diverse or social in<sup>fl</sup>uence has a signi<sup>fi</sup>cant effect on the diffusion process [16]. Further, since the unit of study in econometric models is at the aggregate rather than individual unit level, differences among brands, such as marketing mix characteristics, cannot be explicitly incorporated in the model. As a result, one cannot study the effect of marketing mix strategies on diffusion at the brand level. The ability to see this effect is of particular interest to the brand manager who is charged with understanding outcomes at this level in order to make strategic decisions.

The goal of this study is to address the limitations of current diffusion models by developing an agent-based diffusion model with consumer and brand agents. Utilizing this methodology allows characteristics of the consumers and brands in the market to be incorporated in the model. Agent-based modeling (ABM) also allows interactions and emergent behaviors in the simulated market to be studied. Modeling diffusion at the brand rather than product-category level offers insights of interest from both research and management standpoints. This approach to modeling reveals the diverse set of brand-level diffusion curves that result from differences among brands. These brand-level diffusion curves aggregate to form the product-category level curve.

Agent-based modeling is an emerging methodology well suited for studying complex, adaptive systems, such as those seen in diffusion studies. Brand-level diffusion models are especially complex since there are: multiple brands; many and diverse factors de<sup>fi</sup>ne each brand; “order-of-entry effects” [2]; and consumers and brands that may adapt to changing market conditions [11]. In a real-world system, for example, such adaptation might occur as a consumer is in<sup>fl</sup>uenced by an opinion leader. ABM overcomes the limitations of econometric models in three ways. First, members of the market can be de<sup>fi</sup>ned in terms of their attributes. Consumers, for example, can be de<sup>fi</sup>ned in terms of factors such as their personal characteristics while brands can be de<sup>fi</sup>ned in terms of their marketing mix characteristics and entry timing. Second, interactions among agents may be de<sup>fi</sup>ned and simulated. Third, the agent adaptations that occur as the result of interactions can be modeled further adding to the simulation's ability to model real-world phenomenon [35].

Perhaps because of the widespread use of agent-based models in sociology, many of the current applications of ABM in diffusion research focus on the effect of the social network on adoption [10]. As a result of the network focus, factors at the consumer and product level that directly affect diffusion are not explicitly incorporated in these models. The ABM developed in this study clearly departs from others' emphasis on social network in<sup>fl</sup>uence. This model incorporates a comprehensive set of consumer and brand attributes to develop brand-level diffusion curves then aggregates them to develop a product-category diffusion curve.

Little diffusion research incorporating the effect of complex adaptive systems is found in the innovation literature [35]. The current research contributes to the <sup>fi</sup>eld by developing a complex, adaptive model that simulates key factors and interactions that occur in the market during the diffusion process. Further, since this approach incorporates consumer and brand characteristics, it may be used as a decision tool to compare the outcomes of different strategic choices during the marketing strategy development process.

The remainder of this paper will discuss diffusion theory, provide an overview of ABM, describe the agent-based diffusion model used in this study, review the simulation results, and end with conclusions.

## 2. Theory

The diffusion literature includes two major streams: econometric models and explanatory models. Econometric models vary in terms of the factors and algorithms they use to model purchases by customers in order to forecast product-category growth. These models typically re<sup>fl</sup>ect only <sup>fi</sup>rst-time purchases [21]. The Bass [1] model, upon which much diffusion research is based, forecasts the probability of individuals adopting at a given point of time as the innovation diffuses based on whether they are innovators or imitators. Extensions of the Bass model incorporate factors such as heterogeneous populations [5], price [29], advertising [15], and introduction of brands [19]. Mahajan et al. [21] provide a comprehensive review of econometric diffusion models.

Gatignon and Robertson's [12] “consumer diffusion paradigm” is an example of an explanatory model. In this framework (see Fig. 1), personal characteristics, perceived innovation characteristics, personal in<sup>fl</sup>uence, and external in<sup>fl</sup>uences directly affect the adoption process. In turn, the “distribution of individual adoption decisions” results in the diffusion at the social system (or market segment) level [12, p. 850]. Innovativeness is a key personal characteristic that affects adoption decisions. Although the de<sup>fi</sup>nition of innovativeness varies in the literature, it may be concluded that this factor plays a key role in an individual's decision to adopt an innovation and the time to adoption [e.g., 23,30].

Social in<sup>fl</sup>uence affects adoption decisions by reducing decision anxiety and by simplifying information search since the adopter can make a decision based on the experience of peers. Further, social in<sup>fl</sup>uence provides the potential adopter with a social context for the acceptability of the consumption decision [13]. The <sup>fi</sup>nal factor affecting adoption decisions is external in<sup>fl</sup>uence. External in<sup>fl</sup>uence refers to communication about the innovation from outside the individual's social in<sup>fl</sup>uence network [30].

The innovation's perceived characteristics affect adoption decisions at two levels. When an individual becomes aware of an innovation, perceived innovation characteristics will be assessed at the category level <sup>fi</sup>rst. If the individual decides to adopt, perceived innovation characteristics will be assessed at the brand level next, which will in<sup>fl</sup>uence the actual purchase decision [19]. The factors the individual will consider when making an adoption decision vary depending on whether the assessment is at the category or brand level. At the category level, characteristics that broadly de<sup>fi</sup>ne the innovation, such as relative advantage, compatibility, trialability, observability, and perceived risk, will be considered [30]. The second part of the consumer adoption decision, or the brand-level decision, is in<sup>fl</sup>uenced by marketing mix elements such as the innovation's price, promotion level, and distribution strategy [4].

At the brand management level, strategy should re<sup>fl</sup>ect both marketing mix decisions and entry timing considerations since market response to these brand-level strategies will be affected by the order in which the brand has entered the market [2], and the product-category's life cycle phase [22]. Late entrants may have a negative impact on the pioneer's position by successfully differentiating themselves in the market in terms of their attributes [32,38] although their success in doing so will be moderated by the strength of the incumbent brand [3]. Late entrants may also fuel market expansion through the differentiated products they offer [22].

## 3. Agent-based modeling

## 3.1. Overview

ABM is a methodology for modeling complex systems. It has been applied in many disciplines including engineering, economics, sociology, and the natural sciences; its acceptance in the management sciences is emerging [10,39]. Compared to other simulation methods, ABM offers several advantages especially in terms of modeling complex systems. For instance, in other models, the unit of study is the population. In ABM, the unit of study is the individual or agent. De<sup>fi</sup>nitions of individual system members (i.e., agents) may be grounded in theory (e.g., innovativeness, satisfaction) or be based on agent attributes (e.g., psychodemographics, product characteristics). The ability to de<sup>fi</sup>ne multiple agent types representing entities with different roles in the system allows system heterogeneity to be incorporated in the model [10].

Another key feature of ABM is its ability to simulate interaction among agents as de<sup>fi</sup>ned by the researcher. The researcher may also specify how the agents will adapt as a result to stimuli from the system. Members of a real-world system often interact and these interactions will result in members taking speci<sup>fi</sup>c actions. Members may also change, or adapt, as a result of these interactions. ABM easily mirrors these real-world conditions since the researcher can specify interactions among agents and then de<sup>fi</sup>ne the outcomes of the interactions based on the agents' characteristics. Since these adaptive, or emergent results, may not be anticipated by studying individual system elements, they represent another key feature of ABM [10,36].

ABM's greatest utility resides in applications where there is an interest in studying effects at micro and macro levels, when adaptation among agents occurs in the system, when the population is heterogeneous, and where emergent results are possible [10]. ABM's role in research is not to replace causal models, but rather to build upon their theoretical basis by providing insights related to interactions within the system and emergent results [10].

![](/api/attachments/QATXQ82H/fulltext/images/e946ecc66d7d81eca271622622770f94cb226c08d87f38978b3e9b7a0d604ecf.jpg)  
Fig. 1. Consumer diffusion paradigm.

A <sup>fi</sup>nal advantage of ABMs is their relatively easy implementation when compared to other modeling methodologies. ABM software is freely available (e.g., SWARM [34], NetLogo [37]). Although basic programming skills are helpful when constructing models, ABMs are easier to develop than other analytical models. Software, such as NetLogo, incorporates screen sliders, text boxes, and buttons on the computer screen to facilitate running and changing the model. More sophisticated approaches, such as neural networks or evolutionary algorithms, may also be utilized [10].

## 3.2. Agent-based diffusion models

Based on the congruence of ABM's application strengths and characteristics of many diffusion environments, it has great potential to advance diffusion research. In diffusion research, micro and macro level analyses are of interest (i.e., adoption and diffusion, respectively). Adaptation may occur as consumers, for example, are in<sup>fl</sup>uenced by opinion leaders. Consumers with varying levels of innovativeness create a heterogeneous population. Finally unexpected, emergent results may occur as the result of interactions among consumer and brand agents.

Studying diffusion of innovations in social networks has been the most prevalent application of ABM within the marketing literature. These studies have shown the strength of ABM in modeling these systems, especially as they become more heterogeneous. They also have demonstrated the impact of network structure on the diffusion rate [10]. Delre et al. [9] compared the effect of social in<sup>fl</sup>uence and word-of-mouth processes on diffusion across different network structures. The simulation showed that innovations diffuse more quickly in clustered networks than in random networks because individuals in clustered networks are exposed to more social in<sup>fl</sup>uence that may result in a shorter time to adoption. Diffusion occurs more slowly in large networks since in this case more adopters are necessary to in<sup>fl</sup>uence the individual. It also was found that the speed of diffusion is quicker in more heterogeneous networks. In heterogeneous networks, more individuals adopt early which accelerates the diffusion process sooner [9].

Janssen and Jager [17] studied green product introduction using producer agents and consumer agents. In the model, producer agents adapted their product offerings in response to their performance in terms of meeting business targets. Consumer agents were de<sup>fi</sup>ned in terms of environmental consciousness based on their social and personal needs. Differences in diffusion rates as a function of changes in product offerings and consumer agents' social and personal need de<sup>fi</sup>nitions provided numerous insights for targeting strategy.

Delre et al. [8] used ABM to study the effect of advertisingcampaign timing on the diffusion curves of different categories of durable products. Consumer agents were de<sup>fi</sup>ned in terms of their individual preference and social in<sup>fl</sup>uence of their network. The model revealed the relative effects of social contagion and mass media campaigns (in terms of quality and timing) on the diffusion rate and also showed how these effects impacted the diffusion of different durable product categories.

The Customer Behavior Simulator (CUBES) project incorporates ABM's ability to not only model interactions among agents, but also to facilitate agents' adaptive behavior in response to changing market conditions [31]. The model's strong consumer behavior focus simulates consumers' behavioral attitudes, consumption resulting from the attitudes, brand-level responses to market conditions, and the effect of brand-level responses on consumer attitudes. Consumer agents are de<sup>fi</sup>ned in terms of their behavioral attitudes and socioeconomic pro<sup>fi</sup>les. These attitudes affect their opinion about different brand agents and may change based on interactions with other system agents. The model's output includes diffusion curves, evolution of behavioral attitudes, and evolution of brands' market shares [31].

## 4. Agent-based diffusion model with consumer and brand agents

## 4.1. Model overview

The primary objective in developing the ABM for this study is to demonstrate the feasibility and advantage of using such a model to understand the complex interactions that occur at the brand level during the diffusion process for a durable product. Durable product diffusion models are distinct since these products, compared to nondurable products, are purchased once or infrequently [1]. Similar to the approach used by Delre et al. [9], the agents in this ABM reside in a <sup>fi</sup>xed network with a structure allowing interactions among consumers and among consumers and brands. ABM's ability to model at the individual unit level makes it feasible to de<sup>fi</sup>ne the product being studied at the brand rather than product-category level. Productcategory modeling is typically implemented in traditional diffusion models [e.g., 1,5]. Since this model allows diffusion to be studied at the brand level, understanding of diffusion is gained not only at the brand level, but also at the product-category level.

For the purpose of this research, the decision to adopt corresponds to a purchase decision. The individual decisions yield brand-level diffusion curves. Then, the model combines brand-level diffusion curves to form a product-category diffusion curve. This feature results in disaggregate (brand) and aggregate (product) diffusion curve outputs from one model. Traditional diffusion models deliver only an aggregate or disaggregate diffusion curve [27]. Therefore, this model allows study of diffusion at the micro (brand) and macro (productcategory) levels.

The theoretical basis for this agent-based diffusion model is the “consumer diffusion paradigm” [12]. ABM makes it possible to build upon this framework by de<sup>fi</sup>ning agents so that interactions between personal characteristics, personal in<sup>fl</sup>uence, and perceived innovation characteristics are simulated. ABM also allows consumer agents to adapt as they respond to changes in the market in terms of product offerings, promotion, and social in<sup>fl</sup>uence. The late entrant literature [2,22,32] is referenced to de<sup>fi</sup>ne brand agents and frame the simulations.

In addition to our assumption of a <sup>fi</sup>xed network structure, two other assumptions are made in this model. First, we assume that each consumer agent will adopt a maximum of one brand. Second, we assume that there will not be interactions among brands in terms of competitive responses to others' offerings.

## 4.2. Model design

NetLogo 4.0.3 [37] is used to program the agent-based simulation model described in the current study. NetLogo is a freely downloadable, agent-based software package that was created at the Center for Connected Learning and Computer-Based Modeling (CCL), directed by Uri Wilensky, at Northwestern University. NetLogo utilizes a simple programming language and a convenient user interface allowing models like ours to be easily simulated and evaluated. The software application is designed to be easy to use yet is broadly utilized by academics in the social, computer, and “hard” sciences [33].

NetLogo is extremely <sup>fl</sup>exible. Interactions not only among autonomous agents, but also between agents and the simulated environment, can be speci<sup>fi</sup>ed. As shown in Fig. 2, the simulation model used in this study requires input parameters for three entities: the simulation environment, consumer agents, and brand agents. Each set of parameters can be independently modi<sup>fi</sup>ed to approximate the unique context and problem domain that is being examined. As such, the input parameters at all three levels approximate the consumer, brand, and market conditions pertinent to the study's context.

## 4.3. Environmental parameters

The concept of time is modeled in NetLogo as an arbitrary unit (referred to as a “tick”) that is left to the model developer to de<sup>fi</sup>ne. In our model, a tick is recorded after every consumer agent makes a random “walk” within the simulated environment. These consumer movements are what enable interactions with other consumers or brands. The total number of time units per iteration, as well as how many units represent a single year, can be modi<sup>fi</sup>ed by the user to best represent a speci<sup>fi</sup>c study context.

Operationalizing the concept of population is also left to the model developer. In the case of this study, the consumer population is de<sup>fi</sup>ned as a collection of independent and individually-modeled consumer agents. In this model, the user can specify the total number of consumer agents for each simulation iteration.

The <sup>fi</sup>nal environmental parameter is called the adoption threshold. This parameter represents the value at which a consumer will adopt a brand after each consumer agent's individual adoption threshold has been calculated. If the consumer agent's threshold value exceeds this environmental parameter, adoption will occur. This threshold value is speci<sup>fi</sup>ed for the entire population and higher values yield lower adoption rates. This value can be modi<sup>fi</sup>ed by the user to match a speci<sup>fi</sup>c consumer adoption context as this is likely to change from situation to situation.

![](/api/attachments/QATXQ82H/fulltext/images/e635a8ddac9f58cb3b9e20432ab08376d3acaf78586246e88f3dab31989248c1.jpg)  
Fig. 2. Input parameters.

## 4.4. Consumer parameters

Rogers [30] classi<sup>fi</sup>ed groups of consumers, representing the target market for a given product, into <sup>fi</sup>ve categories (innovators, early adopters, early majority, late majority, and laggards). For simplicity, three groups of consumers based on the adopter groups de<sup>fi</sup>ned by Rogers [30] are included in this model. The model's adopter groups are categorized as innovators, early, and late adopters. Consumers within each group are homogenous in terms of their personal characteristics. To introduce additional heterogeneity into the consumer population, a distribution of consumers is generated within each adopter group. The number of consumers within each group is based on proportions de<sup>fi</sup>ned by Rogers [30]. The relative size of these adopter groups can be easily modi<sup>fi</sup>ed by the user to represent the consumer distribution for the product category under investigation.

To operationalize personal characteristics, a high, medium, or low level of innovativeness is assigned to the innovator, early adopter, and late adopter groups, respectively. Based on the assigned innovativeness level, each adopter group is de<sup>fi</sup>ned in terms of its sensitivity to features, price, promotion, and social in<sup>fl</sup>uence. At the extremes of the three consumer groups, an innovator is most innovative implying less sensitivity to features, price, and social in<sup>fl</sup>uence and more sensitivity to promotion while a late adopter is least innovative, and therefore, more sensitive to features, price, and social in<sup>fl</sup>uence, and less sensitive to promotion [1,18,30]. It is important to note that while sensitivity to product features, price, promotion, and social in<sup>fl</sup>uence are speci<sup>fi</sup>ed at the adopter group level, adoption decisions are made at the individual consumer agent level. The sensitivity value speci<sup>fi</sup>ed for each adopter group, therefore, represents the mean of a uniform distribution of values for each adopter category's consumer agent members. This approach results in homogeneous adopter groups that are comprised of unique consumer agents.

De<sup>fi</sup>ning consumer agents in terms of their sensitivity to brand attributes (i.e., features, price, and promotion) establishes the basis for interactions with brand agents. For instance, since the innovator will adopt earlier in the product life cycle, it is implied that the innovator will accept brands with fewer features and a higher price, typical of <sup>fi</sup>rst generation products [18]. At the other extreme, the late adopter will only accept a brand with relatively more features (representing later generation products) and a lower price. Therefore, the consumer agent makes brand-level decisions based on the match between its personal characteristics, the brand agent's characteristics, and the proportion of adopters in the system.

The simulation model interface allows the user to input both the relative size of the adopter group and the individual sensitivities to marketing and social in<sup>fl</sup>uence for each group. Again, these values can be modi<sup>fi</sup>ed to match the unique context under investigation. Since brand-level adoption and diffusion is being modeled in this study, it is assumed that the consumer agent has already adopted the product at the category level and is now making brand-level decisions [19].

## 4.5. Brand parameters

The simulation interface allows the user to specify both the individual characteristics of brand agents and the time each agent is introduced during the simulation. Characteristics for each brand are operationalized in terms of features, price, promotion level, and brand density (in terms of channel presence). A high value for the feature parameter indicates that consumer agents will perceive that the brand has a rich set of features. Similarly, a high price parameter indicates that consumer agents will perceive the price of the brand to be high. The promotion parameter is an indicator of promotional intensity and higher values indicate greater intensity. The brand density parameter is an indicator of distribution channel intensity. Higher values indicate greater intensity which means that the brand will be more visible to consumers. In this ABM, greater intensity translates into to a higher probability that consumer agents will interact with a given brand agent. The characteristics of each brand are context-speci<sup>fi</sup>c and should be adjusted by the user to approximate the brand strategies for the competing brands for the product category that is being modeled.

## 4.6. Adoption decision

As described earlier, in this simulation consumer and brand agents interact with each other and the decision to adopt is triggered during these interactions. The decision to adopt a brand by a consumer agent depends on the consumer's brand expectations (as a function of adopter category membership), the brand's characteristics, and the interaction between them. For example, an innovator consumer agent is more likely to adopt a brand introduced earlier in the productcategory life cycle since it will accept fewer product features and is less sensitive to price. In addition to brand characteristics, a consumer agent's decision to adopt is in<sup>fl</sup>uenced by the proportion of adopters in the system as a function of its personal characteristics. A consumer agent in the innovator group, for example, is less in<sup>fl</sup>uenced by social in<sup>fl</sup>uence (in the form of the proportion of adopters) and more in<sup>fl</sup>uenced by promotion. In contrast, a late adopter is swayed more by social in<sup>fl</sup>uence and less by promotion.

As shown in Fig. 3, each time a consumer agent interacts with a brand agent, the model calculates four index values representing the outcome of brand and consumer agent interactions in terms of features, price, promotion, and social in<sup>fl</sup>uence. In calculating the index for social in<sup>fl</sup>uence and brand promotion we account for both the number of interactions between the consumer and the brand, and also for the number of other consumers who have adopted a brand. Thus, the social in<sup>fl</sup>uence index increases as more consumers adopt this brand. Similarly, with greater brand density, and therefore greater interactions between the consumer and this brand, the value of brand promotion increases in this function calculation.

Relatively high index values indicate a match between the consumer agent's expectations and the brand's characteristics. The four calculated index values yield the consumer's adoption threshold (CAT). In essence, the CAT represents a composite measure of the impact of the interaction between the consumer agent's expectations and the brand's characteristics; higher values suggest a greater likelihood of adoption by the consumer agent:

CAT = f Feature Index; Price Index; Promotion Index; Social Influence Index

ð<sup>1</sup>Þ

A CAT is generated each time a consumer and brand agent interacts.

The Feature Index represents the impact of brand features on the adoption decision and is the product of the brand's features and the consumer agent's sensitivity to brand features. The impact of price on the adoption decision is represented by the Price Index and is calculated by multiplying the consumer agent's sensitivity to price by one minus the brand agent's price value; this calculation incorporates the positive adoption response to a lower price. The in<sup>fl</sup>uence of a brand's promotional intensity on the adoption decision is represented by the Promotion Index. The Promotion Index is calculated by <sup>fi</sup>rst multiplying consumer agent sensitivity to promotional activity by the brand agent's promotion intensity. This result is then multiplied by a value representing the previous interactions that have occurred between a given brand and consumer agent pair. The Social Influence Index represents the effect of the social in<sup>fl</sup>uence on the adoption decision. This value is calculated by multiplying the consumer agent's sensitivity to social in<sup>fl</sup>uence by the total proportion of consumer agents that have adopted the brand. The brand agent adopts the brand when the CAT exceeds the adoption threshold value (speci<sup>fi</sup>ed as an environmental parameter by the user).

![](/api/attachments/QATXQ82H/fulltext/images/980a36a87a7f61197b16274483054736c3477e68eeb33d7e07ee17686af3436f.jpg)  
Fig. 3. Consumer adoption threshold determination.

## 5. Simulation overview

For this study, we use the digital camera market as an illustration of how consumer and brand interaction in<sup>fl</sup>uences adoption decisions. This example illustrates how ABM supports the development of scenarios to understand the effect of changing brands' marketing mix variables on diffusion at the brand and product-category levels. First, a model representing the baseline market is developed. Then, model parameters are adjusted to investigate the effects of changes in marketing mix factors on brand and product-category diffusion. Details for the consumer agent and environmental parameters used for the simulations are found in Table 1.

The baseline scenario for this model references the consumer digital camera market from 1995 through 2002. Secondary data from freely available marketing reports are utilized in the simulations [6,14,20,24,25]. The time period referenced frames the digital camera's introduction through the takeoff of its diffusion curve. At the time, the market consisted of four dominant competitors; minor competitors in the market are not included in the model. Digital cameras offered by each competitor were very similar in terms of features and price. The primary difference among competitors was market entrance timing which is incorporated in the model.

Brand agents are de<sup>fi</sup>ned in terms of key characteristics described in marketing reports [7,24,25]. Four brand agents, representing the aggregate of models offered by each competitor, are incorporated in our baseline model re<sup>fl</sup>ecting the four key competitors that dominated the consumer digital camera market. In the baseline simulation (Simulation 1), brand agents are modeled with similar features and prices and differ only in terms of market entry timing to re<sup>fl</sup>ect the fact that digital camera brands introduced after the pioneer were noninnovative late entrants. A second brand is introduced at the end of Year 2 and two brands enter the market in Year 3, which is consistent with the historical data. Consumer agents are modeled as de<sup>fi</sup>ned above. Since marketing research [24] indicated that the key factors in<sup>fl</sup>uencing consumer decisions were price, resolution, and ease-of-use (i.e., features), these factors are studied in the second and third simulations in order to model how the late entrants' manipulation of these factors affects individual adoption decisions and the resulting diffusion curves. We assume that the magnitude of the response to lower prices will be greater to the response to more features. In the second simulation, market timing entry for Brands A through D is unchanged from Simulation 1. However, Brand B enters with enhanced features; Brands C and D follow Brand B by entering the market with features comparable to Brand B's features. In the third simulation, the factors from Simulation 2 are amended such that Brands C and D are introduced at a lower price than Brands A and B. Brand D's price is slightly lower than Brand C's price. An overview of brand agent de<sup>fi</sup>nitions for Simulations 2 and 3 is found in Table 2.

Consumer agent characteristics.

<table><tr><td rowspan="2">Group</td><td rowspan="2">Innovativeness</td><td colspan="4">Sensitivity to</td></tr><tr><td>Features</td><td>Price</td><td>Promotion</td><td>Social Influence</td></tr><tr><td>Innovator</td><td>High</td><td>Low</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td>Early adopter</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Medium</td></tr><tr><td>Late adopter</td><td>Low</td><td>High</td><td>High</td><td>Low</td><td>High</td></tr></table>

## 6. Simulation results

In Simulation 2, Brand Agents B, C, and D are altered to re<sup>fl</sup>ect enhanced features while leaving all other factors unchanged. By comparing the output details generated for the product-category level diffusion curves from the baseline or Simulation 1 (Fig. 4) and Simulation 2 (Fig. 5), it is seen that by Year 8, the result of introducing enhanced features into the market in Years 2 and 3 increases the number of adopters by 66% relative to the baseline. Thus, Simulation 2 demonstrates the potential to increase the market by introducing enhanced features earlier. A comparison of category level diffusion curves from Simulations 1 and 2 reveals that enhancing features sooner also increases the rate of diffusion. This result mirrors information from marketing research reports (incorporated in the model) indicating that consumers desire more features in digital camera offerings [24]. A second result from Simulation 2 demonstrates ABM's ability to reveal emergent results. In Simulation 2, Brand B enters at Year 2 with enhanced features; Brands C and D enter with the same enhanced features in Year 3. By comparing the curves shown in Fig. 5, it is seen that only Brand B is able to overtake Brand A (the pioneer) by enhancing its features. Based on the simulation results, we can conclude that features and entry timing are important to secure market leadership.

Table 2 Brand agent de<sup>fi</sup>nitions.

<table><tr><td rowspan="2"></td><td rowspan="2">Market entry (Year)</td><td colspan="2">Change from baseline</td></tr><tr><td>Features</td><td>Price</td></tr><tr><td colspan="4">Simulation 2</td></tr><tr><td>Brand A</td><td>1</td><td>No change</td><td>No change</td></tr><tr><td>Brand B</td><td>2</td><td>Enhanced</td><td>No change</td></tr><tr><td>Brand C</td><td>3</td><td>Enhanced</td><td>No change</td></tr><tr><td>Brand D</td><td>3</td><td>Enhanced</td><td>No change</td></tr><tr><td colspan="4">Simulation 3</td></tr><tr><td>Brand A</td><td>1</td><td>No change</td><td>No change</td></tr><tr><td>Brand B</td><td>2</td><td>Enhanced</td><td>No change</td></tr><tr><td>Brand C</td><td>3</td><td>Enhanced</td><td>Reduced</td></tr><tr><td>Brand D</td><td>3</td><td>Enhanced</td><td>Reduced further $^{a}$ </td></tr></table>

a Brand D is less expensive than Brand C.

<table><tr><td></td><td>Year 1</td><td>Year 2</td><td>Year 3</td><td>Year 4</td><td>Year 5</td><td>Year 6</td><td>Year 7</td><td>Year 8</td></tr><tr><td>Historic Digital Camera Data</td><td>2</td><td>6</td><td>13</td><td>25</td><td>47</td><td>92</td><td>162</td><td>256</td></tr><tr><td>Baseline Simulation Max</td><td>5.00</td><td>8.00</td><td>15.00</td><td>43.00</td><td>71.00</td><td>100.00</td><td>184.00</td><td>296.00</td></tr><tr><td>Baseline Simulation Min</td><td>2.00</td><td>3.00</td><td>5.00</td><td>18.00</td><td>40.00</td><td>65.00</td><td>131.00</td><td>219.00</td></tr></table>

Fig. 4. Simulation 1 (baseline) results.

In Simulation 3 (Fig. 6), price factors for Brand Agents C and D are altered in Year 3 to re<sup>fl</sup>ect a drop in price. The output details for Simulation 3 reveal that the number of adopters at the category level increases 44% in this scenario and the market diffusion rate increases relative to Simulation 2. This change is driven by Brand Agents C and D's low-price entrance in this scenario. As anticipated from our price response assumption, the number adopting Brand D surpasses that of Brand C since Brand D's price was slightly lower than Brand C's. Since both Brands C and D overtook Brands A (the pioneer) and B, this simulation reveals that reducing price, compared to increasing features, is able to overcome the market's lack of response to later entrants (as seen in Simulation 2). The simulated market's response to price reductions is expected since the model was programmed to re<sup>fl</sup>ect a greater effect of a price change, than a feature change, on the consumer agents' adoption decisions based on our assumption that consumers would respond more favorably to a drop in price than to enhanced features for purposes of the simulation.

![](/api/attachments/QATXQ82H/fulltext/images/eed6e3c837bccf7fff29dc68e60d4680ebd2f38811d90d99095c8a5c878f327c.jpg)  
Fig. 5. Simulation 2 results: Brands B, C, and D introduced with enhanced features

The difference between the results of Simulations 2 and 3 is summarized graphically in Fig. 7. This view yields additional emergent results at the brand level that signi<sup>fi</sup>cantly enhance information gained from market-level results. The effect of lower-priced, late entrants affects the diffusion curves for Brands C and D (the lowerpriced brands) immediately and continues to accelerate the curves through Year 8 (the end of the simulation). The diffusion rate for Brands A and B (the higher-priced brands) begins to decline immediately, however, their rate of decline is markedly less than the rate of acceleration for Brands C and D.

To summarize, results of these simulations reveal the affect of the changed parameters in terms of the product category and among brands. This ABM clearly allows the effect of interactions among brands and consumers to be demonstrated based on their reaction to strategic changes made by each brand agent. The ability to compare diffusion at the brand level provides greater insight than would have been provided by studying product-category diffusion information alone.

![](/api/attachments/QATXQ82H/fulltext/images/45360d40fbaeffb96f28ea5952aa9a2673f4bd81298329449110b9dcd1d9dd5b.jpg)  
Fig. 6. Simulation 3 results: Brand B introduced with enhanced features; Brands C and D introduced with enhanced features and reduced prices

![](/api/attachments/QATXQ82H/fulltext/images/61fcd93b65413d47d8c6c1ed019c19eb90643ce195775d4da286c05b6f81cb51.jpg)  
Fig. 7. Simulation 2 vs. Simulation 3: differences in number of adopters.

## 7. Limitations and future research

Several assumptions were made in the current simulation that represent limitations to be addressed in future research. First, the current simulation only considers interactions among consumers and between consumers and brands. Additional development incorporating interactions among brands would further advance this research by incorporating the effect of brand agents on one another in terms of strategy adaptation and entry/exit behavior. Such a simulation would also allow managers to better understand the competitive responses to marketing decisions. Next, we chose to develop this model with a <sup>fi</sup>xed network structure following Delre et al.'s approach [8]. Since it has been shown that network structure does affect diffusion dynamics, manipulating network structure in future research would enhance our model [9]. We also assumed that each consumer agent would purchase only one camera during the course of the simulation. Further research will incorporate multiple unit purchases, as well as the potential for consumer agents to switch brands, to more accurately re<sup>fl</sup>ect actual market behavior. Finally, in this model we set feature-preference parameters based on qualitative marketing research data. Extending this research by collecting primary data from consumers would re<sup>fl</sup>ect relative feature preferences among consumers and allow sensitivity analysis of the brand attributes incorporated in the model.

## 8. Conclusion

ABM represents a new methodology with the potential to advance the study of diffusion of innovative products. It builds on extant econometric and exploratory diffusion models by advancing understanding of interactions among agents in the system and by incorporating adaptive responses by agents to system changes [10]. Further, interactions that occur during ABM simulation runs can reveal emergent results which may not be evident when studying system elements individually [36]. The ability to de<sup>fi</sup>ne individual agents further adds to ABM's advantages since it allows multiple factors and heterogeneity among agents to be incorporated in the simulation [10]. ABM also supports managerial decision-making by allowing managers to predict the effect of marketing mix changes on diffusion rates.

This agent-based diffusion model con<sup>fi</sup>rms ABM's ability to demonstrate the role decisions by consumer agents have at the product category and brand levels. Simulation of diffusion at the brand level has signi<sup>fi</sup>cant managerial implications since it provides insights for brand managers in terms of their primary focus — the brand. By modeling brand-level diffusion curves, and then aggregating them to develop a product-category diffusion curve, the effect of agent actions and interactions can be understood at micro and macro levels. ABM can incorporate not only marketing mix factors, but also the important effect of social in<sup>fl</sup>uence on the market's response to changes in marketing strategy. ABM output allows focus on phases of the diffusion curve, such as the initial, or takeoff, phase. Thus, the manager can gain an understanding of the relative effect of marketing mix variables on driving takeoff as a function of the brand's market entry point [26]. Likewise, managers of brands that enter after the takeoff period can use ABM to understand their potential for penetrating the established market. In this model it becomes apparent that during takeoff, the late entrant brand introducing enhanced features <sup>fi</sup>rst bene<sup>fi</sup>ts the most in terms of increasing its volume. This action also accelerates the diffusion curve at the product-category level. Further, the simulation allows the manager to see the additive effect of changing multiple elements of the marketing mix. In this research, when the two late entrants (i.e., Brands C and D) are introduced with enhanced features and reduced prices, they both are able to overcome the higher-priced brands (i.e., Brands A and B) while further accelerating the diffusion curve. In addition to informing understanding of the brand and market-level reactions to changes in marketing mix strategy, the output from this simulation can be utilized for <sup>fi</sup>nancial analysis to further explore the outcomes of different strategies further adding to ABM's potential for contributing to diffusion research.

## References

[1] F.M. Bass, A new product growth model for consumer durables, Management Science 15 (5) (1969) 215–227.

[2] D. Bowman, H. Gatignon, Order of entry as a moderator of the effect of the marketing mix on market share, Marketing Science 15 (3) (1996) 222–242.

[3] G.S. Carpenter, K. Nakamoto, Competitive strategies for late entry into a market with a dominant brand, Management Science 36 (10) (1990) 1268–1278.

[4] R. Chatterjee, J. Eliasberg, V.R. Rao, Dynamic models incorporating competition, in: V. Mahajan, E. Muller, Y. Wind (Eds.), New-Product Diffusion Models, Kluwer Academic Publishers, Boston, 2000.

[5] R. Chatterjee, J. Eliashberg, The innovation diffusion process in a heterogeneous population: a micromodeling approach, Management Science 36 (9) (1990) 1057–1079.

[6] Consumer Electronics Association, Digital America 2006 — Overview, http:// www.ce.org/Press/CEA\_Pubs/1995.asp

[7] Simpler and Cheaper, Consumer Reports, May (2004) 20–21

[8] S.A. Delre, W. Jager, T.H.A. Bijmolt, M.A. Janssen, Targeting and timing promotional activities: an agent-based model for the takeoff of new products, Journal of Business Research 60 (2007) 826–835.

[9] S.A. Delre, W. Jager, M.A. Janssen, Diffusion dynamics in small-world networks with heterogeneous consumers, Computational & Mathematical Organization Theory 13 (2) (2007) 185–202.

[10] R. Garcia, Uses of agent-based modeling in innovation/new product development research, Journal of Product Innovation Management 22 (5) (2005) 380–398.

[11] H. Gatignon, E. Anderson, K. Helsen, Competitive reactions to market entry: explaining inter<sup>fi</sup>rm differences, Journal of Marketing Research 26 (1) (1989) 44–55.

[12] H. Gatignon, T.S. Robertson, A propositional inventory for new diffusion research, Journal of Consumer Research 11 (4) (1985) 849–867

[13] H. Gatignon, T.S. Robertson, Innovative decision processes, in: T.S. Robertson, H.H. Kassarjian (Eds.), Handbook of Consumer Behavior, Prentice-Hall, Inc, Englewood Cliffs, 1991.

[14] G. Gavetti, R. Henderson, S. Giorgi, Kodak (A) — Case 9-703-503, Harvard Business School, Boston, 2004.

[15] D. Horsky, L.S. Simon, Advertising and the diffusion of new products, Marketing Science 2 (1) (1983) 1–17.

[16] W. Jager, The four P's in social simulation, a perspective on how marketing could bene<sup>fi</sup>t from the use of social simulation, Journal of Business Research 60 (2007) 868–875.

[17] M.A. Janssen, W. Jager, Stimulating diffusion of green products, Journal of Evolutionary Economics 12 (3) (2002) 283–306.

[18] N. Kim, E. Bridges, R.K. Srivastava, A simultaneous model for innovative product category sales diffusion and competitive dynamics, International Journal of Research in Marketing 16 (1999) 95–111

[19] T.V. Krishnan, F.M. Bass, V. Kumar, Impact of a late entrant on the diffusion of a new product/service, Journal of Marketing Research 37 (May 2000) 269–278.

[20] R.S. Lazich (Ed.), Market Share Reporter, Gale Group, Detroit, 2001–2008

[21] V. Mahajan, E. Muller, F.M. Bass, New product diffusion models in marketing: a review and directions for research, Journal of Marketing 54 (January 1990) 1-26

[22] V. Mahajan, S. Sharma, R.D. Buzzell, Assessing the impact of competitive entry on market expansion and incumbent sales, Journal of Marketing 57 (3) (1993) 39–52.

[23] D.F. Midgley, G.R. Dowling, Innovativeness: the concept and its measurement, Journal of Consumer Research 4 (March 1978) 229–242

[24] Mintel, Digital Cameras — United States, March (2006).

[25] Mintel, Digital Still Cameras and Videocameras — United States, March (2008).

[26] E. Muller, R. Peres, V. Mahajan, Innovation Diffusion and New Product Growth, Marketing Science Institute, Cambridge, 2009.

[27] J.H. Roberts, J.M. Lattin, Disaggregate-level diffusion models, in: V. Mahajan, E. Muller Y. Wind (Eds.) New-Product Diffusion Models Kluver Academic Publishers, Boston, 2000.

[28] J.H. Roberts, G.L. Urban, Modeling multiattribute utility, risk, and belief dynamics for new consumer durable brand choice, Management Science 34 (2) (1988) 167–185.

[29] B. Robinson, C. Lakhani, Dynamic price models for new product planning, Management Science 10 (June 1975) 1113–1122.

[30] E.M. Rogers, Diffusion of Innovations, Free Press, New York, 2003.

[31] L.B. Said, T. Bouron, A. Drogoul, Agent-Based Interaction Analysis of Consumer Behavior, International Conference on Autonomous Agents, Bologna, Italy, 2002.

[32] V. Shankar, G.S. Carpenter, L. Krishnamurthi, Late mover advantage: how innovative late entrants outsell pioneers, Journal of Marketing Research 35 (February 1998) 54–70.

[33] E. Sklar, Software review: NetLogo, a multi-agent simulation environment, Arti<sup>fi</sup>cial Life 13 (3) (2007) 303–311.

[34] Swarm Development Group, www.swarm.org (1999).

[35] O. Toubia, J. Goldenberg, R. Garcia, A New Approach to Modeling the Adoption of New Products: Aggregated Diffusion Models, MSI Reports 08-001, 2008, pp. 65–81.

[36] J. Wang, K. Gwebu, M. Shanker, M.D. Troutt, An application of agent-based simulation to knowledge sharing, Decision Support Systems 46 (2) (2009) 532-541.

[37] U. Wilensky, NetLogo, http://ccl.northwestern.edu/NetLogo (1999).

![](/api/attachments/QATXQ82H/fulltext/images/1c11fe4f95a2605f7b54baa4a7b00c908f4cf32d521f93613caad3b804b0b0f0.jpg)

[38] S. Zhang, A.B. Markman, Overcoming the early entrant advantage: the role of alignable and nonalignable differences, Journal of Marketing Research 35 (4) (1998) 413–426.

![](/api/attachments/QATXQ82H/fulltext/images/8089a7d308540841b82c39329f9a3d0051a4bc0ba80ed174bb0dab5ba6b5aa6c.jpg)

[39] T. Zhang, D. Zhang, Agent-based simulation of consumer purchase decision-making and the decoy effect, Journal of Business Research 60 (2007) 912–922.

![](/api/attachments/QATXQ82H/fulltext/images/1c30078a1a40c1bbbac552c174d0685aaacb5002e385ae974e14c7ade5f34830.jpg)  
Mary E. Schramm received her MBA from the University of Wisconsin-Oshkosh. She is currently a Ph.D. candidate in Marketing at Kent State University. Her research interests include product innovation, diffusion, new product development, and healthcare marketing. Her industry experience includes product marketing and new product development in industrial and healthcare markets.

![](/api/attachments/QATXQ82H/fulltext/images/9821a163132ed8b136424fa0e1db535e940e4df3d5c41976fbb341cb318fec12.jpg)

Kevin J. Trainor is an Assistant Professor of Marketing in the Richard J. Wehle School of Business at Canisius College. He holds a Ph.D. in Marketing from Kent State University. His research interests include new product development, product innovation, and the interface between marketing and R&D. His research is published or forthcoming in Journal of Business Research, Journal of Business and Industrial Marketing, and Journal of International Management Studies. His industry experience includes roles in software development and product management.

Murali Shanker is a Professor in the Department of Management & Information Systems, Kent State University. He holds a Ph.D. from the University of Minnesota. Hi research is published in INFORMS Journal on Computer, IIE Transactions, Journal of the Operational Research Society, Decision Support Systems, and Decision Sciences. Hi research interests lie in Distance Learning, Distributed Computing, Open Source, Simulation, and Neural-Network Modeling.

Michael Y. Hu has a Ph.D. from the University of Minnesota in management science/marketing. Currently he holds the Bridgestone Chair in International Business and is a Professo of Marketing at Kent State University. He has published over a hundred and thirty academic articles in the areas of applications of marketing, international business and arti<sup>fi</sup>cial neura networks. His research has appeared in Journal of Marketing Research, Marketing Letters, International Journal of Research in Marketing, Decision Sciences, European Journal of Operational Research and many others. He won the University Distinguished Teaching Award in 1994 and the University Distinguished Scholar Award in 2006 at Kent State University
