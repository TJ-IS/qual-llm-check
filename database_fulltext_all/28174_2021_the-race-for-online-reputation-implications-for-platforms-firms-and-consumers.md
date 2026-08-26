---
otero_id: 28174
otero_key: "FJZE36Q3"
title: "The Race for Online Reputation: Implications for Platforms, Firms, and Consumers"
authors: "Mingwen Yang; Zhiqiang (Eric) Zheng; Vijay Mookerjee"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Race for Online Reputation: Implications for Platforms, Firms, and Consumers

Mingwen Yang,<sup>a</sup> Zhiqiang (Eric) Zheng,<sup>b</sup> Vijay Mookerjee<sup>b</sup>

<sup>a</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>b</sup> Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080

Contact: mingweny@uw.edu, https://orcid.org/0000-0002-4620-6149 (MY); ericz@utdallas.edu, https://orcid.org/0000-0001-8483-8713 (Z(E)Z); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM)

Received: March 4, 2019 Revised: March 29, 2020; September 9, 2020 Accepted: November 17, 2020 Published Online in Articles in Advance: September 7, 2021

https://doi.org/10.1287/isre.2021.1005

Copyright: © 2021 INFORMS

Abstract. Online reputation (as re<sup>fl</sup>ected in customer ratings) has become a key marketingmix variable in the digital economy. This paper models how <sup>fi</sup>rms compete by managing their online reputations. We consider a market consisting of competing <sup>fi</sup>rms that participate in a platform such as Expedia or Yelp. Each <sup>fi</sup>rm exerts effort to improve its rating but, in doing so, also in<sup>fl</sup>uences the mean market rating. The sales of a <sup>fi</sup>rm are in<sup>fl</sup>uenced by its own rating and the mean rating of the <sup>fi</sup>rms in the market. We formulate each <sup>fi</sup>rm’s decision as a stochastic control problem in which the objective is to maximize the discounted pro<sup>fi</sup>t over a planning horizon. These control problems are connected through a common market belief that represents the mean rating of the <sup>fi</sup>rms in the market. The joint actions of the <sup>fi</sup>rms generate a mean market rating in equilibrium. We prove that such an equilibrium exists and is unique, and we use a simple algorithm to compute its value. An equilibrium analysis of the mean market rating reveals several insights. A more heterogeneous market (one in which the parameters of the <sup>fi</sup>rms are very different) leads to a lower mean market rating and higher total pro<sup>fi</sup>t of the <sup>fi</sup>rms in the market. Our results can inform platforms to target certain <sup>fi</sup>rms to join: growing the middle of the market (<sup>fi</sup>rms with average ratings) is the best option considering the goals of the platform (increase the total pro<sup>fi</sup>t of the <sup>fi</sup>rms) and other stakeholders, namely the incumbents and the consumers. For <sup>fi</sup>rms, we <sup>fi</sup>nd that a <sup>fi</sup>rm’s pro<sup>fi</sup>t can increase from an adverse event (such as a reduction in sales margin or an increase in the cost of control) depending on how other <sup>fi</sup>rms in the market are affected by the event. Our <sup>fi</sup>ndings are particularly signi<sup>fi</sup>cant for platform owners to employ a strategic growth model for the platform.

History: Anindya Ghose, Senior Editor; Juan Feng, Associate Editor.

Funding: E. (Z). Zheng acknowledges his grant support from National Natural Science Foundation of China (NSFC) [Grant 71831006].

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2021.1005.

Keywords: online reputation competition equilibrium controlled diffusion process

## 1. Introduction

The internet has empowered consumers to garner product or service information from the experience of other consumers through online user opinions (customer reviews). It is reported that 88% of consumers read online reviews to evaluate the quality of a local business (Anderson 2014). Online reviews have been found to have a large impact on a <sup>fi</sup>rm’s online reputation and revenue. For example, a 1% improvement in reputation can result in up to a 1.42% increase in revenue (Anderson 2012), and <sup>fi</sup>rms making into the list of top 25 reviews generate 5% more payments compared with those that did not make it (Tadelis 2016). In response, <sup>fi</sup>rms spend millions of dollars annually to manage user opinions to build and maintain brand awareness (Forbes 2013). In TripAdvisor’s latest study, it is reported that 97% of business owners consider online reputation management to be important to their businesses (Erskine 2018). Thus, online reputation has become a pivotal marketing-mix variable for <sup>fi</sup>rms. For example, hotels have begun to redirect their advertising budget to appear in preferred AAA listings to manage their reputation and monitor guest comments (Manley 2017).

Firms can manage online reputation internally by dedicating manpower to monitor online reputation and act on it accordingly. Wikipedia (2020) lists some common tactics used to manage online reputation. Firms commonly use online reputation management (ORM) software to help support online reputation management tasks.<sup>1</sup> Firms can also outsource ORM to thirdparty companies or individual professionals. For example, Wadworth uses GuestRevu to constantly gather feedback from its guests and actively manage its online reputation (GuestRevu 2020). Another form of outsourcing is to use platforms such as Fiverr.com on which freelancers offer services for online reputation management.

A <sup>fi</sup>rm’s online reputation (as re<sup>fl</sup>ected in its ratings) <sup>fl</sup>uctuates and is not fully controllable. It is this fact that makes it valuable but realistic (Erskine 2018). Thus, although a <sup>fi</sup>rm’s mean rating can be in<sup>fl</sup>uenced by its control effort, there is usually a stochastic component that cannot be in<sup>fl</sup>uenced by the <sup>fi</sup>rm. The control effort can be understood as staf<sup>fi</sup>ng or budget assigned to manage online reputation. For example, if the <sup>fi</sup>rm manages reputation internally, the control effort can be thought as the manpower (e.g., total person hours) dedicated to ORM as well as the cost of using the ORM software. When the ORM task is outsourced, the control effort can be determined by the outsourcing budget.

A consumer’s purchasing decision on a platform depends not only on the ratings of the focal <sup>fi</sup>rm, but also on those of its competitors. As such, <sup>fi</sup>rms need to justify to customers why the customer should choose them over their competitors. To achieve this, <sup>fi</sup>rms often track social media key performance indicators (e.g., review ratings) about themselves as well as those of their competitors (Glassman 2011). Many social media analytics tools, such as RivalIQ and SproutSocial, provide services to help <sup>fi</sup>rms readily track their competitors social media activities and performance. Our research setting considers a group of <sup>fi</sup>rms in a platform (such as Yelp or Expedia) that compete for sales by managing their online reputation. These <sup>fi</sup>rms face the challenge of effectively managing online reputation in the presence of competing <sup>fi</sup>rms (Kent 2014). To this end, the literature has recently started examining the problem of reputation management through approaches such as <sup>fi</sup>rm response (Kumar et al. 2018, Yang et al. 2019) and review manipulation (Luca and Zervas 2016). There is also a stream of research that examines the impact of online reviews of competing <sup>fi</sup>rms on a focal <sup>fi</sup>rm’s sales (Jabr and Zheng 2014, Kwark et al. 2021).

From the perspective of platform owners, managers often assume that the key to success is to grow the number of <sup>fi</sup>rms and consumers as quickly as possible to reap the positive network effects, believing that the size leads to competitive advantage (Cennamo and Santalo´ 2013). However, a simple growth strategy, often referred to as “get big fast,” could lead to a platform trap because it ignores competitive forces that arise among the <sup>fi</sup>rms as a result of the growth strategy (Cennamo and Santalo´ 2015).

Given the importance of online reputation competition, there are several challenges <sup>fi</sup>rms and platforms continue to face:

How much effort should a <sup>fi</sup>rm exert to effectively manage online reputation (that evolves stochastically over time), and how does the effort level of competing <sup>fi</sup>rms affect this choice?

<sub>•</sub> From the platform’s perspective, how should it target a new <sup>fi</sup>rm to join without compromising the objectives of the incumbent <sup>fi</sup>rms and consumers?

For a given market size, how should the platform balance the different kinds of <sup>fi</sup>rms in the platform so as to maximize the platform goals?

Most previous models on advertising competition (that can be considered similar to online reputation competition) have considered a duopoly market when analyzing equilibrium outcomes. A notable exception is Naik et al. (2008) in which the competition among many <sup>fi</sup>rms is studied. However, unlike our study, Naik et al. (2008) consider a deterministic problem in which the state variable does not have a stochastic component. Besides, in online reputation competition, not only can consumers observe the customer reviews received by all the <sup>fi</sup>rms in the market, but <sup>fi</sup>rms can also observe all other <sup>fi</sup>rms’ customer reviews. Thus, in a competitive market, when all the <sup>fi</sup>rms in the market attempt to manage their online reputations, the equilibrium ratings in the market are dif<sup>fi</sup>cult to solve using a traditional stochastic differential game-theoretic model.

To address this dif<sup>fi</sup>culty, we derive the market equilibrium using the following process. Because the rating of each individual <sup>fi</sup>rm is stochastic, the market rating (average ratings across the <sup>fi</sup>rms) is also stochastic. However, in equilibrium, consumers and <sup>fi</sup>rms use the mean of the market rating as the basis for their actions. Each <sup>fi</sup>rm’s sales (another stochastic process) are driven by its current rating and this (mean) belief. This is analogous to the re<sup>fl</sup>ection problem identi<sup>fi</sup>ed in Manski (1993) in which the group behavior affects individual behavior, and the group behavior is the aggregation of individual behavior.

An analysis of the mean market equilibrium reveals several insights. The mechanism underlying these insights is that a particular <sup>fi</sup>rm’s actions not only directly affect its outcomes (such as rating or pro<sup>fi</sup>t), but also indirectly affect these outcomes via the equilibrium mean market rating. We list several results that impact the strategies of the platform and <sup>fi</sup>rms.

For a given number of <sup>fi</sup>rms in the platform, a more heterogeneous market (one in which the parameters of the <sup>fi</sup>rms are very different) leads to a lower mean market rating and a higher total pro<sup>fi</sup>t of the <sup>fi</sup>rms in the market. This <sup>fi</sup>nding can bene<sup>fi</sup>t platform owners to choose the right mix of <sup>fi</sup>rms in the platform. A heterogeneous market can increase the pro<sup>fi</sup>t of the <sup>fi</sup>rms and the platform but at the expense of the consumers.

Our results can also inform platform owners to develop a targeted growth strategy, that is, encourage certain kinds of <sup>fi</sup>rms to join the platform.

– Growing <sup>fi</sup>rms with average ratings (i.e., the middle of the market) is the safest option considering the goals of the platform (increasing the total pro<sup>fi</sup>t of all the <sup>fi</sup>rms) and other stakeholders, namely the incumbent <sup>fi</sup>rms and consumers.

– Growing <sup>fi</sup>rms with lower-than-average ratings (i.e., the market at the bottom) hurts the consumers but bene<sup>fi</sup>ts both the platform and the incumbent <sup>fi</sup>rms.

– Growing <sup>fi</sup>rms with higher-than-average ratings (i.e., the market at the top) bene<sup>fi</sup>ts the consumers but hurts the pro<sup>fi</sup>ts of the incumbent <sup>fi</sup>rms.

<sub>•</sub> In a competitive market, adversity can be a friend. A <sup>fi</sup>rm could get hurt from an increase in the cost of control effort (or a decrease in the sales margin). However, this result could <sup>fl</sup>ip if another <sup>fi</sup>rm experiences a higher increase in the cost of control effort (or a greater decrease in the sales margin).

Sometimes, the image of the platform can play an important role in attracting customers to the <sup>fi</sup>rms in the platform. In such situations, attracting low-rating <sup>fi</sup>rms could hurt all the stakeholders (the incumbent <sup>fi</sup>rms, the platform, and the consumers). Conversely, high-rating <sup>fi</sup>rms should be induced to stay with the platform. Therefore, we extend the base model by considering the impact of the mean market rating on the market demand. The intuition is that the mean market rating may change the platform’s image, which, in turn, could affect the market demand. We show that, when the impact of the platform’s image is suf<sup>fi</sup>ciently small, the consequences of the entry (exit) of a <sup>fi</sup>rm to the incumbent <sup>fi</sup>rms, the platform, and the consumers stay the same. However, these consequences change when the platform’s image plays a more substantial role.

The rest of the paper has the following structure. Section 2 summarizes the relevant literature. Our model is presented in Section 3. In Section 4, we study the equilibrium. Section 5 describes the results. We present an extension model in Section 6. Section 7 discusses the implications, and Section 8 concludes the paper.

## 2. Literature Review

In this section, we discuss the related literature and how this paper builds upon and extends various streams of related research.

## 2.1. Advertising Competition

Traditionally, in the advertising literature, many researchers have explored the optimal advertising strategy in monopoly or competitive markets (Bass et al. 2005, Naik et al. 2008, Rubel et al. 2011). In this literature, <sup>fi</sup>rms invest in advertising over multiple periods to maximize their total pro<sup>fi</sup>ts, and the advertising expenditure (effort) affects both present and future demands of the product. The effect of advertising persists beyond the current period but with diminishing returns (Liu et al. 2012), and the term goodwill is proposed to capture consumers’ awareness of the product formed through advertising. The competing brands seek to increase brand awareness to boost their sales. Hence, managers have to take into account the presence of multiple competitors in determining their best course of action. Each <sup>fi</sup>rm selects a level of advertising expenditure to maximize its discounted pro<sup>fi</sup>t <sup>fl</sup>ow over time, and <sup>fi</sup>rms compete among themselves for the goodwill. One well-known duopoly example is the strategic advertising competition between Coke and Pepsi, in which Chintagunta and Vilcassim (1992) empirically validate the classic Lanchester model (Little 1979) using the real data. When there are more than two rivals in the market, Naik et al. (2008) consider oligopolistic competition in which each <sup>fi</sup>rm solves an optimal advertising strategy to maximize its pro<sup>fi</sup>t in equilibrium. Instead of modeling deterministic sales– advertising dynamics by Naik et al. (2008), Prasad and Sethi (2004) adds a diffusion term capturing randomness in the evolution of sales in a duopoly setting.

Unlike previous studies, we consider a large number of <sup>fi</sup>rms in a market that compete for sales stochastically, each attempting to control its rating. To the best of our knowledge, this necessary combination of features, namely more than two <sup>fi</sup>rms, stochastic state variables, and the mechanism (control effort online reputation sales pro<sup>fi</sup>t) has not been studied earlier. We next discuss online review competition among <sup>fi</sup>rms.

## 2.2. Online Review Competition

Because online consumer reviews are observable to consumers and competing <sup>fi</sup>rms in the market, consumers are able to form informed beliefs about the review ratings of the competing <sup>fi</sup>rms in the market. These beliefs could act as an anchor when they make purchase decisions. Our paper contributes to a growing body of literature related to online review ratings competition, such as those examining the impact of review ratings on product sales (Chevalier and Mayzlin 2006, Duan et al. 2008, Zhu and Zhang 2010). Within this literature, a recent stream of studies examines the impact of the reviews received by the competitors. It has been well documented that consumers make their purchase decisions based on the review ratings of the focal product and competitors; there is a strong spillover effect from competitors’ ratings to the focal product’s sales (Jabr and Zheng 2014, Kwark et al. 2021). For example, Jabr and Zheng (2014) empirically demonstrate that product sales of a focal <sup>fi</sup>rm drop with the improvements in the reviews of its competitors. Using retail clickstream data, Kwark et al. (2021) show that the mean review rating of substitute products exerts a negative impact on the sales of the focal product.

Several analytical studies have attempted to unravel how the competition emanating from online reviews in<sup>fl</sup>uences a <sup>fi</sup>rm’s decisions (Mayzlin 2006, Li et al. 2011, Kwark et al. 2014). Mayzlin (2006) identi<sup>fi</sup>es a unique equilibrium in which online reviews are persuasive despite the promotional chat (e.g., review manipulation) activity of competitors. Contrary to the prior advertising literature, <sup>fi</sup>rms spend more resources promoting inferior products under such an equilibrium. Li et al. (2011) analyze the offsetting effects caused by competition for repeatedly purchased products, resulting in an “S-shaped” relationship between the quality of reviews and <sup>fi</sup>rm pro<sup>fi</sup>ts. Kwark et al. (2014) study the effect of online product reviews on upstream competition between manufacturers in a channel structure. The quality and <sup>fi</sup>t information provided by consumer reviews affect the upstream competition in different ways. There are some papers focusing on the strategic behaviors between <sup>fi</sup>rms and consumers in terms of online feedback by which agents can rate each other sequentially (Hui et al. 2016, Ye et al. 2014) or manipulating customer reviews in response to competition (Wu and Qiu 2016) in which they <sup>fi</sup>nd that, although forging customer reviews can improve the perceived quality, high-quality sellers do not do so because of higher marginal cost.

Different from prior studies, we investigate how the competition impacts a <sup>fi</sup>rm’s decision (control effort) to manage its customer reviews and further pro<sup>fi</sup>t dynamically in a competitive market. In addition, we also study the impact on the pro<sup>fi</sup>ts of incumbent <sup>fi</sup>rms and the total pro<sup>fi</sup>t of all the <sup>fi</sup>rms in the market, a measure that is in line with the goals of the platform.

## 2.3. Equilibrium Models with Many Players

Most previous analytical studies on online ratings competition have considered a few competing <sup>fi</sup>rms (often two <sup>fi</sup>rms in a duopoly setting). In this study, we consider a competitive market with a large number of <sup>fi</sup>rms that attempt to manage their online reputations. When the number of players is large, stochastic games become notoriously intractable. Lasry and Lions (2007) introduce mean <sup>fi</sup>eld games to study Nash equilibria when the number of players is large and the players interact symmetrically through the empirical distribution of the states of all the players. Given such a distribution, each player typically solves a control problem. One example is the question: “What time does the meeting start?” (Gueant et al.´ 2011), in which a meeting scheduled for a certain time very often starts several minutes after the scheduled time. The actual time when the meeting starts (T) depends on the dynamics of the arrivals of individual participants. Each agent decides the agent’s (intended) arrival time by minimizing the agent’s expected total cost (if the agent arrives earlier than T, the agent incurs a waiting time cost; otherwise, the agent suffers a cost of lateness because of the reputation loss) with the assumption that T is known. T is the mean <sup>fi</sup>eld, that is, the exhaustive summary for each agent of the behavior of the others, and a priori distribution can be treated as deterministic because of the law of large numbers. The equilibrium shows that the individual optimization behavior, supposing T is known, fully generates the realization of this time T.

Given the stochastic nature of our problem setting (both ratings and sales of each <sup>fi</sup>rm are stochastic processes), the equilibrium concept we use in this study has been inspired by the concept of a mean <sup>fi</sup>eld. However, we consider heterogeneous players rather than identical players. Our equilibrium is also similar to the rational expectations equilibrium (Muth 1961). Rational expectation is a concept and modeling technique that is used widely in many domains, for example, <sup>fi</sup>nance (Chari and Jagannathan 1988, Cao 1999, Veronesi 1999), online advertising (Aseri et al. 2020), macroeconomics (Frydman 1982), etc. In our paper, we borrow the spirit of a rational expectations equilibrium, but unlike many previous applications of this concept, we make necessary modi<sup>fi</sup>cations for the continuous and dynamic nature of our problem setting.

In the next section, we present the model and study its properties.

## 3. Model Description

We model a <sup>fi</sup>rm’s decision with regard to its control effort to manage its online reputation (review ratings or user opinions) assuming rational, pro<sup>fi</sup>t-maximizing behavior. Our discussion begins with a high-level, conceptual model to better understand its inner mechanism and key components.

## 3.1. Conceptual Model

We consider a market consisting of a relatively large number of retailers (N >> 2), closely competing with each other in a speci<sup>fi</sup>c market segment, for example, <sup>fi</sup>ve-star hotels within the same price range in the same neighborhood, moderately priced Italian restaurants within the same zip code, etc. Customers of a focal <sup>fi</sup>rm not only consider its rating, but also the ratings of the competing <sup>fi</sup>rms in the market. In theory, therefore, the equilibrium ratings in the market would be the outcome of an N N game, whose analysis would be intractable for most reasonable values of N. To address this problem, we consider a different equilibrium concept as follows.

In equilibrium, customers and <sup>fi</sup>rms have a common belief about the mean rating of all the <sup>fi</sup>rms in the market (market rating). This market rating is constructed from directly competing <sup>fi</sup>rms in the same market segment. Customers and <sup>fi</sup>rms believe that the market rating follows a stochastic process with some mean. This mean market rating is used by customers and <sup>fi</sup>rms as the basis for their decisions. A conceptual model representing our equilibrium concept is shown in Figure 1. The conceptual model shows that a focal <sup>fi</sup>rm’s sales depend not only on its own rating, but also on the mean market rating constructed from the ratings of all the <sup>fi</sup>rms in the market. In Figure 1, we depict each <sup>fi</sup>rm’s sales as driven by the mean market rating and the rating of the focal <sup>fi</sup>rm. Because the mean market rating affects the evolution of <sup>fi</sup>rms’ ratings, it must also be considered in the choice of the control effort. Finally, each <sup>fi</sup>rm’s rating affects the mean market rating in equilibrium.

Figure 1. Conceptual Model  
![](/api/attachments/FJZE36Q3/fulltext/images/cc38401efd10a427db6dd52541c728fb920d6c208f0dece79ae9871ce31ab85d.jpg)

The mean market rating plays a central role in our analysis. Firms could obtain the mean market rating either by inference or by observation as illustrated. Some leading platforms have started to display the mean market rating on the platform. For example, Figure 2 provides a screenshot from Taobao.com (the largest business-to-business e-commerce website in China). We can see that the platform lists the consumer ratings of a speci<sup>fi</sup>c retailer and its rank relative to the mean market rating. For the example depicted in Figure 2, this particular seller’s consumer rating with respect to the “product description consistency” is 3% higher than the mean market rating. Thus, <sup>fi</sup>rms and consumers can easily observe the mean market rating, and this mean market rating is the same for every <sup>fi</sup>rm in the market.

Admittedly, not all platforms directly display the mean market rating to the public. However, consumer ratings of <sup>fi</sup>rms are public, and most platforms make it convenient for users to <sup>fi</sup>lter out competitors. Thus, it does not take much effort for <sup>fi</sup>rms and consumers to infer the mean market rating. Figure 3 provides a screenshot from Yelp.com. After constraining Italian restaurants near downtown Dallas and the expense range (medium, \$\$), Yelp displays 33 restaurants with ratings for each. Firms and consumers can readily compute or infer the mean market rating based on this set of information. In addition, there is abundant evidence showing that <sup>fi</sup>rms track and react responsively to their competitors’ performance and market conditions (Jabr and Zheng 2014, Kwark et al. 2021).

Motivated by these examples, we use the mean market rating as an anchor to model consumer purchase behavior. From a mathematical perspective, the stochastic process underlying the market rating can be derived from the primitives of the model. This process has a steady-state mean. Thus, the idea that consumers can use the steady-state mean as an anchor is theoretically sound and agrees with the theoretical properties of the market rating process realized in equilibrium. The use of the steady-state mean as an anchor is also practically meaningful given that the market ratings are only updated periodically and not in real time. Finally, a process with a steady-state mean allows us to achieve a parsimonious, tractable model that yields useful insights.

## 3.2. Ratings Formation Process

The key feature of our model is that a <sup>fi</sup>rm’s control effort affects its online reputation (measured by consumer ratings), which, in turn, in<sup>fl</sup>uences sales.<sup>2</sup> The control effort can be understood as the personnel or budget assigned to manage online reputation. There are several speci<sup>fi</sup>c actions that <sup>fi</sup>rms (or their agents) can deploy for boosting online reputation. One approach could be soliciting positive reviews, for example, by sending emails to encourage positive customers to post reviews after transactions. Because recent reviews are often displayed <sup>fi</sup>rst and most customers only read the <sup>fi</sup>rst few pages of online reviews, negative reviews get crowded out quickly among a large number of positive ones (Yang et al. 2019). Some platforms allow <sup>fi</sup>rms to talk to customers off-line to resolve their complaints so that they may revise their negative opinions (Banjo 2012). Some <sup>fi</sup>rms manage their user opinions by publicly responding to consumer reviews (referred to as management response). A <sup>fi</sup>rm’s responses can affect future reviews in two ways. Customers are more likely to write negative reviews when their experience of a product is different (worse) from what they have experienced (Moe and Schweidel 2012, Ho et al. 2017). If customers were to voice a complaint on an issue that has already been raised and responded to, they would feel obliged to express their complaint differently—referred to as the “beg to differ” effect by Moe and Schweidel (2012). Responding to reviews is also likely to decrease the occurrence of future negative reviews because consumers feel that their reviews are closely scrutinized, which increases the “cost” of leaving a negative review, especially a <sup>fl</sup>aky or unfounded one (Yang et al. 2019).

Figure 2. (Color online) Illustration of the Mean Market Rating by Observation  
![](/api/attachments/FJZE36Q3/fulltext/images/0319b15aae5d56ad7977a3a9702d136f77887e271c1b3351436579b3170cdcf1.jpg)

## 3.3. Mathematical Preliminaries

We <sup>fi</sup>rst present a model of an individual <sup>fi</sup>rm in the platform that exerts effort to control its online reputation so as to maximize a pro<sup>fi</sup>t objective. This problem is solved for a given value of the mean market rating (μ). Later, this value is determined in equilibrium when we solve the N-<sup>fi</sup>rm model in the next section.

There are two continuous-state, continuous-time stochastic processes corresponding to the two state variables in the <sup>fi</sup>rm’s control problem: (1) online reputation x(t) and (2) sales rate S(t).<sup>3</sup> We <sup>fi</sup>rst describe how the <sup>fi</sup>rm’s online reputation evolves over time in reaction to its control. The change in the online reputation (dx(t)) in a small time interval from time t to t dt, is modeled as

$$
d x (t) = \Bigl (u \sqrt {b - x (t)} - \theta \mu x (t) \Bigr) d t + \zeta (x (t)) d W (t).\tag{1}
$$

The variable x(t) represents the online reputation of the <sup>fi</sup>rm at time t. As an illustration, x(t) could be operationalized using the last (most recent) n review ratings.<sup>4</sup> The variable u denotes the control effort (u is not necessarily constant, and we solve for u later) exerted by a <sup>fi</sup>rm to manage its online reputation. It is important to note that conventional marketing-mix variables (such as price or quality) are not represented in the control variable u. This is because we consider a speci<sup>fi</sup>c market segment in which conventional variables, such as price and quality, do not vary much across competitors. For example, with three-star downtown hotels, the quality and price are usually highly correlated and do not vary much. Each market segment has its de<sup>fi</sup>nition of what price and quality level to offer, which we reasonably assume is stable within a certain period of time. As long as these variables are relatively stable, they do not matter much in the stochastic optimal control model we develop.<sup>5</sup> Therefore, in this paper, we maintain a parsimonious model by focusing on online reputation competition.<sup>6</sup>

Figure 3. (Color online) Illustration of the Mean Market Rating by Inference  
![](/api/attachments/FJZE36Q3/fulltext/images/7e29f2de97becc603da3ebcf9ab06130ecc7682c610940e3aa5de6163caa1755.jpg)

The variable b is the upper bound of review ratings, for example, in many review platforms, this value is <sup>fi</sup>ve. The boosting impact of the control on the rating diminishes as the rating improves. This diminishing marginal effect, captured by the square root structure, has been used in many previous studies on the impact of advertising effort on sales or demand (Prasad and Sethi 2004, Bass et al. 2005). The square root form implies that it is relatively easier for <sup>fi</sup>rms to improve their ratings when they are low than when they are high.

The term θμx t represents a decay component to capture a commonly observed trend in the literature that consumer ratings tend to decline over time (Li and Hitt 2008, Moe and Schweidel 2012). If ratings did not decay, once a <sup>fi</sup>rm reached the maximum rating (e.g., <sup>fi</sup>ve on a one-to-<sup>fi</sup>ve scale), it would not need to do anything to maintain the maximum level. The phenomenon of natural decay (in the absence of any control effort) is prevalent and has been widely documented in the literature (e.g., Li and Hitt 2008, Moe and Schweidel 2012, Zheng et al. 2014). For example, a book typically receives the highest review rating when it is released. Over time, the book loses novelty gradually, and its review rating tends to decline. Thus, if the focal <sup>fi</sup>rm does not exert any effort, this natural decay phenomenon persists, and the rating falls gradually over time. The decay factor in our model is introduced to capture this phenomenon.

The decay in rating is proportional to the current rating (x(t)). That is, a high rating decays faster than a low rating. For a product or service that already has a low reputation in the eyes of consumers, another negative review will not diminish the reputation by as much. For example, when a discount airline (e.g., Spirit) receives another complaint about its poor service, it likely has less of an impact than when a premium airline (e.g., American Airlines) is reported to have a case of bad service. This is because consumers expect relatively poor service from a low-reputation <sup>fi</sup>rm. As seen in Equation (1), the decay in rating is also proportional to the mean market rating (μ). When the mean market rating is high (i.e., the overall online reputation in the market is high), consumers become more demanding of better service. Therefore, with higher mean market rating, the magnitude of decay increases. The parameter θ is the coef<sup>fi</sup>cient of decay.

The stochastic (diffusion) term captures all the randomness in<sup>fl</sup>uencing the ratings. The stochastic term is modeled as $\zeta ( x ( t ) ) d W ( t )$ , where $d W ( t )$ is the increment of a Wiener process following a normal distribution with mean zero and variance $d t ,$ and $\zeta ( x ( t ) )$ , a function of the state, is the magnitude of the stochastic component.

The change in the sales rate over a small time interval from time t to $t + d t$ , denoted by $d S ( t )$ , is described as follows:

$$
d S (t) = \big (\beta \big (x (t) - \mu \big) + \gamma - \tau S (t) \big) d t + \sigma (S (t)) d Z (t).\tag{2}
$$

This change is composed of a deterministic (drift) component and a stochastic (diffusion) component. The <sup>fi</sup>rst term of the deterministic component is proportional to the difference between the <sup>fi</sup>rm’s rating at time $t \ ( x ( t ) )$ and the mean market rating $( \mu )$ . The parameter $\beta$ represents the impact of ratings on the sales rate and can be interpreted as the customers’ sensitivity to ratings. The second term of the deterministic component is a trend parameter $( \gamma )$ that captures the impact of factors on the sales rate that are not related to ratings (e.g., the declining or increasing popularity of the cuisine served by a restaurant, a growing population of af<sup>fl</sup>uent customers of a tour operator, etc.).<sup>7</sup> The value of the trend parameter can be positive, negative, or zero. The third term in the drift component retards the growth of sales. The intuition is that it becomes dif<sup>fi</sup>cult to increase sales when the current sales are already high.

The stochastic term is modeled as $\sigma ( S ( t ) ) d Z ( t ) ,$ where $d Z ( t )$ is the increment of a Wiener process and follows a normal distribution with mean zero and variance $d t .$ The stochastic term captures all the randomness in-<sup>fl</sup>uencing the sales rate; $\sigma ( S ( t ) )$ , a function of the state, is the magnitude of the stochastic component. In both the rating and sales rate processes, the functional forms of the coef<sup>fi</sup>cients $\zeta ( x ( t ) )$ and $\sigma ( S ( t ) )$ are general and do not affect our analysis.

Before we proceed to formulate and solve the control problem for the <sup>fi</sup>rm, we summarize the key assumptions of our analysis.

Consumers use the mean market rating as an anchor to make their purchase decisions. Firms also use this anchor to make optimal decisions on their control efforts.

Firms make effort decisions assuming that the mean market rating is not in<sup>fl</sup>uenced by their efforts.

The rating of a <sup>fi</sup>rm decays at a rate proportional to the current rating of the <sup>fi</sup>rm and the mean market rating.

The impact of control effort on the rating exhibits diminishing returns.

## 3.4. Stochastic Optimal Control Problem

Equations (1) and (2) model how the focal <sup>fi</sup>rm’s control effort u in<sup>fl</sup>uences its rating and further sales rate over time. We consider a <sup>fi</sup>rm that wishes to maximize its total discounted pro<sup>fi</sup>t over a planning horizon. The cost of the control $( \mathrm { e . g . }$ , the cost of the effort to improve the online reputation) is assumed to be a convex and increasing function in the control effort: as the control effort increases, the marginal cost of control increases. We formulate a stochastic optimal control problem as follows:

Table 1. De<sup>fi</sup>nition of Variables and Parameters

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>S(t)</td><td>Sales rate at time t</td></tr><tr><td>x(t)</td><td>Online reputation (rating) at time t</td></tr><tr><td>u</td><td>Control effort</td></tr><tr><td>v</td><td>Steady-state mean rating</td></tr><tr><td>μ</td><td>Mean market rating</td></tr><tr><td>η</td><td>Sales margin</td></tr><tr><td>c</td><td>Cost of control effort</td></tr><tr><td>β</td><td>Customer sensitivity to ratings</td></tr><tr><td>τ</td><td>Sales rate retardation coefficient</td></tr><tr><td>γ</td><td>Sales rate trend parameter</td></tr><tr><td>θ</td><td>Ratings decay coefficient</td></tr><tr><td>ρ</td><td>Discount factor</td></tr><tr><td>σ(S(t))</td><td>Magnitude of volatility in sales rate</td></tr><tr><td>ζ(x(t))</td><td>Magnitude of volatility in ratings</td></tr></table>

$$
\begin{array}{l l} \max _ {u} & \mathbb {E} \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} (\eta S (t) - c u ^ {2}) d t \right] \\ \text {subject to} & d S (t) = (\beta (x (t) - \mu) + \gamma - \tau S (t)) d t + \sigma (S (t)) d Z (t) \\ & d x (t) = \Big (u \sqrt {b - x (t)} - \theta \mu x (t) \Big) d t + \zeta (x (t)) d W (t) \end{array}\tag{3}
$$

where $\eta$ denotes the sales margin, c denotes the cost of control effort, and $\rho$ represents the discount factor. In the objective, $( \eta \dot { S } ( t ) - c u ^ { 2 } )$ represents the <sup>fi</sup>rm’s pro<sup>fi</sup>t rate at time $t ; e ^ { - \rho t }$ is the continuous discount effect at time t. The total pro<sup>fi</sup>t is calculated by integrating the pro<sup>fi</sup>t rate from time 0 to . Because the sales rate S(t) evolves stochastically over time, we take expectation of the total pro<sup>fi</sup>t. Table 1 summarizes the parameters and variables of interest in the model.

We solve the stochastic optimal control problem in Equation (3) (See Online Appendix A) and obtain the $( u ^ { * } ) . ^ { \mathnormal \mathrm { \& } }$ 2 optimal control

Theorem 1. The optimal control effort depends on the firm’s current rating x(t) and various parameters as follows:

$$
\begin{array}{r} u ^ {*} = \alpha \sqrt {b - x (t)}, \\ w h e r e \alpha = \sqrt {(\rho + \theta \mu) ^ {2} + \frac {\eta \beta}{(\rho + \tau) c}} - (\rho + \theta \mu). \end{array}
$$

This control falls within the class of a feedback control; that is, the control depends on the current state. In our context, it is reasonable that the optimal effort exerted by the <sup>fi</sup>rm is higher when the current rating is lower. Also, for a given mean market rating, the control increases with the sales margin (η) and customer sensitivity parameter (β) but decreases with the cost of the control effort (c), sales rate retardation (τ), and decay coef<sup>fi</sup>cient (θ). This is also reasonable because the <sup>fi</sup>rm has a greater incentive to increase its rating when the sales margin or the customer sensitivity parameter is higher. On the other hand, there is less incentive to increase effort if the cost of control, the sales rate retardation, or the decay coef<sup>fi</sup>cient is bigger.

Substituting the optimal control $u ^ { * }$ back into Equation (3) and rewriting, we get the trajectories of two controlled diffusion processes that embed the optimal control strategy as follows:

$$
d S (t) = (\beta (x (t) - \mu) + \gamma - \tau S (t)) d t + \sigma (S (t)) d Z (t)\tag{4a}
$$

$$
d x (t) = \lambda (\nu - x (t)) d t + \zeta (x (t)) d W (t)\tag{4b}
$$

where $\begin{array} { r } { \nu = \frac { A - ( \rho + \theta \mu ) } { A - \rho } b , \lambda = A - \rho , } \end{array}$ , and $\begin{array} { r } { A = \sqrt { \left( \rho + \theta \mu \right) ^ { 2 } + \frac { \eta \beta } { ( \rho + \tau ) c } } . } \end{array}$

The controlled rating process, x(t), follows a mean reverting process in which it <sup>fl</sup>uctuates around its steadystate mean ν with λ being the speed of reversion. The mean-reverting property echoes the beg-to-differ effect by which customers prefer to express their complaints differently (Moe and Schweidel 2012, Ho et al. 2017). The <sup>fi</sup>rm’s steady-state mean rating (ν) decreases as the mean market rating (μ) increases. On the other hand, the sales rate process is a more complex process (the presence of the stochastic variable $x ( t )$ is in the deterministic term) and does not have a well-behaved form. However, we can obtain a closed-form expression for the expected sales rate at time $t , \mathbb { E } ( S ( t ) | S ( t _ { 0 } ) , x ( t _ { 0 } ) )$ , given the initial sales rate $S ( t _ { 0 } )$ , initial rating $x ( t _ { 0 } ) .$ , and various parameters (see Online Appendix J). The <sup>fi</sup>rm’s value function $V ( S ( t _ { 0 } ) , x ( t _ { 0 } ) )$ , that is, the total discounted pro<sup>fi</sup>t earned by adopting the optimal control, is presented in Theorem 2.

Theorem 2. The optimal value function depends on the firm’s initial sales rate $S ( t _ { 0 } )$ , the initial rating $x ( t _ { 0 } )$ , and various parameters, as follows:

$$
\begin{array}{l} V (S (t _ {0}), x (t _ {0})) = \frac {\eta}{(\rho + \tau)} S (t _ {0}) + 2 c (A - \rho - \theta \mu) x (t _ {0}) \\ \qquad - \frac {\eta \beta \mu}{\rho (\rho + \tau)} + \frac {\eta \gamma}{\rho (\rho + \tau)} \\ \qquad + \frac {b c}{\rho} \bigg (\frac {\eta \beta}{(\rho + \tau) c} - 2 (\rho + \theta \mu) A + 2 (\rho + \theta \mu) ^ {2} \bigg). \end{array}
$$

## 4. Equilibrium Analysis

We now introduce a stochastic differential game in which there are N <sup>fi</sup>rms engaged in the ratings competition. Each <sup>fi</sup>rm is represented with parameters: $\beta _ { i }$ (customer sensitivity to ratings for <sup>fi</sup>rm i), $\eta _ { i }$ (sales margin for <sup>fi</sup>rm $i ) , \gamma _ { i }$ (sales rate trend for <sup>fi</sup>rm $i ) , c _ { i }$ (cost of control for <sup>fi</sup>rm i), τ<sub>i</sub> (sales retardation coef<sup>fi</sup>- cient for <sup>fi</sup>rm $i ) _ { . }$ , and $\theta _ { i }$ (decay coef<sup>fi</sup>cient for <sup>fi</sup>rm $i )$ .

The parameters $\rho$ (discount factor) and b (upper bound of ratings) are considered common to all the <sup>fi</sup>rms in the market.

After solving <sup>fi</sup>rm $i ^ { \prime } \mathrm { s }$ stochastic optimal control problem (for a given μ), its optimal control effort is

$$
\begin{array}{c} {u _ {i} ^ {*} = \alpha_ {i} \sqrt {b - x _ {i} (t)},} \\ {\mathrm{e} \alpha_ {i} = \sqrt {(\rho + \theta_ {i} \mu) ^ {2} + \frac {\eta_ {i} \beta_ {i}}{(\rho + \tau_ {i}) c _ {i}}} - (\rho + \theta_ {i} \mu).} \end{array}
$$

Substituting the optimal control $\boldsymbol { u } _ { i } ^ { * }$ back into the state equations, we get the trajectories of two controlled diffusion processes for <sup>fi</sup>rm i as follows:

$$
\begin{array}{r} d S _ {i} (t) = (\beta_ {i} (x _ {i} (t) - \mu) + \gamma_ {i} - \tau_ {i} S _ {i} (t)) d t + \sigma_ {i} (S _ {i} (t)) d Z _ {i} (t) \\ d x _ {i} (t) = \lambda_ {i} (\nu_ {i} - x _ {i} (t)) d t + \zeta_ {i} (x _ {i} (t)) d W _ {i} (t) \end{array}
$$

where $\begin{array} { r } { \nu _ { i } = \frac { A _ { i } - ( \rho + \theta _ { i } \mu ) } { A _ { i } - \rho } b , \lambda _ { i } = A _ { i } - \rho , } \end{array}$ , and $\begin{array} { r } { A _ { i } = \sqrt { \left( \rho + \theta _ { i } \mu \right) ^ { 2 } + \frac { \eta _ { i } \beta _ { i } } { ( \rho + \tau _ { i } ) c _ { i } } } . } \end{array}$

The pro<sup>fi</sup>t of <sup>fi</sup>rm $i ,$ given the initial sales rate $S _ { i } ( t _ { 0 } )$ and the initial rating $x _ { i } ( t _ { 0 } ) .$ , is

$$
\begin{array}{r l} & V _ {i} (S _ {i} (t _ {0}), x _ {i} (t _ {0})) = \frac {\eta_ {i}}{(\rho + \tau_ {i})} S _ {i} (t _ {0}) + 2 c _ {i} (A _ {i} - \rho - \theta_ {i} \mu) x _ {i} (t _ {0}) \\ & \qquad - \frac {\eta_ {i} \beta_ {i} \mu}{\rho (\rho + \tau_ {i})} + \frac {\eta_ {i} \gamma_ {i}}{\rho (\rho + \tau_ {i})} + \frac {b c _ {i}}{\rho} \bigg (\frac {\eta_ {i} \beta_ {i}}{(\rho + \tau_ {i}) c _ {i}} \\ & \qquad - 2 (\rho + \theta_ {i} \mu) A _ {i} + 2 (\rho + \theta_ {i} \mu) ^ {2} \bigg). \end{array}
$$

Firm i’s steady-state mean rating is $\nu _ { i } .$ The market rating (z(t)) is a stochastic process de<sup>fi</sup>ned by $z ( t ) =$ $\begin{array} { r } { \Sigma _ { i = 1 } ^ { N } x _ { i } ( t ) / N . } \end{array}$ As the controlled diffusion process of $x _ { i } ( t )$ has a steady-state mean, it follows that z(t) also has a steady-state mean. In equilibrium, we have

$$
\frac {1}{N} \sum_ {i = 1} ^ {N} \nu_ {i} = \mu .
$$

Therefore, we have,

$$
\mu = b \frac {\sum_ {i = 1} ^ {N} \frac {A _ {i} - (\rho + \theta_ {i} \mu)}{A _ {i} - \rho}}{N}.\tag{5}
$$

The equilibrium mean market rating should satisfy Equation (5).

## 4.1. Equilibrium Mean Market Rating

Theorem 3. A unique equilibrium exists for the mean market rating.

Although we do not provide a closed-form expression for the mean market rating in equilibrium, we prove the existence and uniqueness of the mean market rating in equilibrium (see Online Appendix B). Furthermore, its value can easily be recovered using a simple search procedure. The mean market rating in equilibrium depends on the sales margin, cost of control, sales retardation, decay coef<sup>fi</sup>cient as well as the customer sensitivity parameter of each <sup>fi</sup>rm in the market, the total number of <sup>fi</sup>rms in the market, the discount factor, and the upper bound of ratings.

Intuitively speaking, the reason for the existence of an equilibrium is as follows. Assume that the equilibrium mean rating for a given market exists for $\mu = \mu ^ { \star }$ However, let us say we provide a value of $\mu ^ { \prime } > \mu ^ { \star }$ as a parameter for each <sup>fi</sup>rm to solve its stochastic control problem. Becuse the provided value is higher than the equilibrium value, each <sup>fi</sup>rm responds with a control effort that is lower than the one that it would choose at equilibrium $\begin{array} { r } { ( \frac { \partial u ^ { \star } } { \partial \mu } < 0 ) } \end{array}$ . This would, in turn, lower the mean rating of each <sup>fi</sup>rm so that the response from the <sup>fi</sup>rms would be such that the average of the ratings of the <sup>fi</sup>rms would be lower than $\mu ^ { \prime } .$ , say $\mu ^ { \prime \prime }$ . If $\mu ^ { \prime \prime } > \mu ^ { \star }$ then the process would repeat until the equilibrium value of $\mu ^ { \star }$ is reached. In a similar way, we can understand how the equilibrium value of $\mu ^ { \star }$ would be reached if the starting value of the market parameter was provided below the true equilibrium value. To summarize, the equilibrium can be reached by a sequence of adjustments, starting above or below the true value. This is because the responses of the <sup>fi</sup>rms are such that they naturally push the next term in the sequence closer to the true value: when the parameter for the mean is above the true value, the responses push this value down, and otherwise, the responses push this value up.

The intuition for uniqueness is a bit more technical than that for existence. Essentially, the main reason behind uniqueness is that, when the equilibrium value (μ) increases, <sup>fi</sup>rms have less incentive to exert effort to improve ratings. The reaction of each <sup>fi</sup>rm is strictly monotonic in $\mu ;$ hence, the uniqueness of the equilibrium. Technically, this idea translates into a unique solution of equation $\mu = h ( \mu )$ (see Online Appendix B). The left side of the equation increases with $\mu .$ The right side monotonically decreases with $\mu$ for the reasons explained earlier. Hence, we get a unique equilibrium.

## 4.2. Example

We illustrate the market equilibrium for a simple case of $N = 3$ <sup>fi</sup>rms in the market.<sup>9</sup> The market rating (z(t)) is stochastic over time and is calculated as the average of the ratings of these three <sup>fi</sup>rms as follows:

$$
z (t) = \frac {x _ {1} (t) + x _ {2} (t) + x _ {3} (t)}{3}
$$

Figure 4(a) and (b), illustrates each <sup>fi</sup>rm’s ratings and sales rates as they evolve over time. We see that both the ratings and sales rates <sup>fl</sup>uctuate over time. In the <sup>fi</sup>gure, we also plot the expected ratings and sales rates over time. The formulas of the expected sales rates and ratings are provided in Online Appendix J. In Figure 4(b), the sales rates have either a positive or a negative trend. The time length is not long enough for sales rates to get saturated. The saturated sales rates (as t goes to in<sup>fi</sup>nity) of <sup>fi</sup>rms 1–3 are 47.23, 1.47, and 0.66 (see the formula of saturated sales rate in Online Appendix J). The mean rating for each <sup>fi</sup>rm is $\nu _ { 1 } = 3 . 9 7 , \nu _ { 2 } = 3 . 4 1$ , and $\nu _ { 3 } = 3 . 4 6 .$ Figure 4(c) shows how the market rating is also stochastically evolving over time with a mean value $\mu = 3 . 6 1$ (the mean market rating). Firm 1’s (<sup>fi</sup>rm $2 ^ { \prime } { \mathrm { s } } )$ ratings on average are higher (lower) than the mean market rating, and therefore, the sales rate of <sup>fi</sup>rm 1 is higher than that of <sup>fi</sup>rm 2 on average. The control effort exerted by each <sup>fi</sup>rm is depicted in Figure 4(d), in which <sup>fi</sup>rm 1 exerts the most effort although its ratings are the highest. This is because the coef<sup>fi</sup>cient of control effort for <sup>fi</sup>rm 1 is the highest $( \alpha _ { 1 } = 2 3 . 0 3 )$ , owing to its highest value of sales margin and customer sensitivity.

Although the market rating is a stochastic process, in equilibrium, customers use the mean of this process (i.e., <sup>E</sup><sub>(</sub>z<sub>(</sub>t<sub>))</sub> or μ) as an anchor to make purchase decisions. Also, in equilibrium, the mean market rating is the mean of the ratings of all <sup>fi</sup>rms, that is, $3 . 6 1 =$ $( 3 . 9 7 + 3 . 4 1 + 3 . 4 6 ) / 3$ . Note that the equilibrium can be asymmetric, that is, ν ≠ ν ≠ ν . The pro<sup>fi</sup>ts of <sup>fi</sup>rms 1–3 are $V _ { 1 } = 2 0 6 . 3 8 , V _ { 2 } = 5 1 . 4 1$ , and $V _ { 3 } = 3 2 4 . 2 4$ . In addition, a <sup>fi</sup>rm in the market can have a mean rating below the market mean yet make positive pro<sup>fi</sup>t (e.g., $\nu _ { 2 } < \mu$ but $V _ { 2 } = 5 1 . 4 1 > 0 )$

## 5. Results

We present and discuss several results relating to the impact of different parameters on the mean market rating and the <sup>fi</sup>rm’s pro<sup>fi</sup>t in equilibrium. The impacts (on the mean market rating and the pro<sup>fi</sup>t in equilibrium) in which the parameters of more than one <sup>fi</sup>rm change are also studied. Finally, several results relating to the market structure (heterogeneity among <sup>fi</sup>rms, the entry and exit of a <sup>fi</sup>rm) are studied.

We begin with two propositions concerning the impact of various parameters on the mean market rating and the <sup>fi</sup>rm’s pro<sup>fi</sup>t in equilibrium.

Proposition 1. The mean market rating in equilibrium changes as the parameters of a firm change as follows:

i. The mean market rating increases as the sales margin increases $\begin{array} { r } { ( \frac { d \mu } { d \eta _ { i } } > 0 ) } \end{array}$

<sup>i</sup>ii. The mean market rating increases as customers become more sensitive to ratings $\begin{array} { r } { ( \frac { d \mu } { d \beta _ { z } } > 0 ) } \end{array}$

<sup>i</sup>iii. The mean market rating decreases as the cost of control effort increases $\begin{array} { r } { ( \frac { d \mu } { d c _ { i } } < 0 ) } \end{array}$

<sup>i</sup>iv. The mean market rating decreases as the sales rate retardation increases $\begin{array} { r } { ( \frac { d \mu } { d \tau _ { i } } < 0 ) } \end{array}$

v. The mean market rating decreases as the ratings decay coefficient increases $\begin{array} { r } { ( \frac { d \mu } { d \theta _ { i } } < 0 ) } \end{array}$

The proof of Proposition 1 is provided in Online Appendix C. In Proposition 1, we note that the impact of a parameter (such as the cost of control effort, sales margin, customer sensitivity, etc.) on the equilibrium mean market rating is intuitive. For example, if the cost of control effort (c ) for a particular <sup>fi</sup>rm increases, it discourages this <sup>fi</sup>rm to invest in effort to improve its rating. As a result, the rating of this <sup>fi</sup>rm falls, leading to a decrease in the equilibrium mean market rating. On the other hand, an increase in the sales margin (η ) or the customer sensitivity parameter (β ) provides a greater incentive for the <sup>fi</sup>rm to improve its rating. It does so by increasing the control effort, and hence, its rating increases. This leads to an increase in the mean market rating.

Figure 4. Numerical Illustration  
![](/api/attachments/FJZE36Q3/fulltext/images/9da2f221f52032eb57a416f488b1f60f8b2bcfbe3531b99e7eac31654b38ae16.jpg)

![](/api/attachments/FJZE36Q3/fulltext/images/865c721ac320d9b660be24bcef433d79e70ee2463f26c61c81dc3b3a0ec0a6e7.jpg)

Corollary 1. The impact of a firm’s parameter on its own mean rating (self-impact) is greater than the impact on the mean market rating (market-impact), that is, $\begin{array} { r } { | \frac { { \bf \dot { \Phi } } _ { d \nu _ { i } } } { d \phi _ { i } } | > | \frac { d \mu } { d \phi _ { i } } | } \end{array}$ where $\phi _ { i }$ can be $\eta _ { i } , \beta _ { i } , c _ { i } , \tau _ { i } , o r \theta _ { i } .$

This result follows from the de<sup>fi</sup>nition of the mean market rating, $N \mu = \Sigma _ { k = 1 } ^ { N } \nu _ { k }$ . Differentiating both sides with respect to $\phi _ { i ^ { \prime } }$ where $\phi _ { i }$ can be $\eta _ { i } , \beta _ { i } , c _ { i } ,$ $\tau _ { i } ,$ or $\theta _ { i } ,$ we get

![](/api/attachments/FJZE36Q3/fulltext/images/830aaab81648fc1cb1db07f25de83ecb2385fb599f4ac9d9624161424e621937.jpg)

![](/api/attachments/FJZE36Q3/fulltext/images/e874639df30f84b8d7d66d2bc62c4beb28b187cbc364c84c652805c645ec2ed2.jpg)

$$
\frac {d \nu_ {i}}{d \phi_ {i}} = N \frac {d \mu}{d \phi_ {i}} - \sum_ {k \neq i} ^ {N} \frac {d \nu_ {k}}{d \phi_ {i}}.
$$

In Online Appendix D, we prove that the magnitude of $\frac { d { \nu } _ { i } } { d { \phi } _ { i } }$ (self-impact) is greater than the magnitude of $\frac { d \mu } { d \phi _ { i } }$ (market-impact).

This corollary implies that the size of the market (N) dilutes the market impact of an event $( \mathrm { i . e . , }$ the change of a parameter) affecting a <sup>fi</sup>rm. This supports the equilibrium concept we use in this study, namely that each <sup>fi</sup>rm behaves (or optimizes) its own pro<sup>fi</sup>t, assuming that its actions have no impact on the mean market rating. However, at the end, the mean market rating is affected by the aggregate behavior of the <sup>fi</sup>rms.

Proposition 2. A firm’s profit in equilibrium changes as the parameters of the firm change, as summarized:

i. The profit increases with the sales margin if and only if $N - f _ { \eta _ { i } } ( \dot { N } ) > 0$

ii. The profit increases with the customer sensitivity to ratings if and only $i f N - f _ { \beta _ { i } } ( N ) > 0 .$

iii. The profit increases with the cost of control effort if and only $i f N - f _ { c _ { i } } ( N ) < 0$

iv. The profit increases with the sales rate retardation if and only $i f N - f _ { \tau _ { i } } ( N ) < 0 .$

v. The profit increases with the ratings decay coefficient if and only $i f N - f _ { \theta _ { i } } ( N ) < 0 .$

The expressions of $f _ { \eta _ { i } } ( N ) , f _ { \beta _ { i } } ( N ) , f _ { c _ { i } } ( N ) , f _ { \tau _ { i } } ( N )$ , and $f _ { \theta _ { i } } ( N )$ are provided in Online Appendix E.

The impact of a change in a parameter on the pro<sup>fi</sup>t in equilibrium is more subtle. For example, take the case of an increase in the sales margin of a particular <sup>fi</sup>rm. Proposition 2(i) asserts that this increase could have a positive or a negative impact on the pro<sup>fi</sup>t of this <sup>fi</sup>rm. In Proposition 1(i), we observe that an increase in the sales margin increases the mean market rating in equilibrium. Therefore, with an increase in the sales margin of a <sup>fi</sup>rm, there are two opposing forces: (1) a direct (positive) effect that must be positive (because, everything else held constant, a higher sales margin should lead to a higher pro<sup>fi</sup>t) and (2) an indirect (negative) effect that acts through the increase in the mean market rating. However, the net impact on pro<sup>fi</sup>t can be either positive or negative. This is because the (positive) direct effect can dominate the (negative) indirect effect when there is a suf<sup>fi</sup>ciently large number of competing <sup>fi</sup>rms in the platform. The reverse is true when the number of competing <sup>fi</sup>rms is relatively small. The impact of a cost increase can be explained in a similar way: as the cost of a <sup>fi</sup>rm increases, it has less incentive to invest in effort, implying that its rating decreases. However, because the mean market rating also decreases, the net impact on the pro<sup>fi</sup>t of the <sup>fi</sup>rm could be positive despite an increase in the cost.

In Proposition 2, we examine the pro<sup>fi</sup>t impact of a situation when only the focal <sup>fi</sup>rm is affected by an event. However, when another <sup>fi</sup>rm is also affected by the event, the effect on the focal <sup>fi</sup>rm could reverse.

We illustrate this possibility in Table 2, in which we observe that <sup>fi</sup>rm 1’s pro<sup>fi</sup>t decreases when only its control cost increases (scenario I). However, its pro<sup>fi</sup>t increases despite the same increase in its own cost when the cost associated with <sup>fi</sup>rm 2 also increases (scenario II). The implication of this <sup>fi</sup>nding is that, when an adverse event (such as an increase in the wage rate in a local area, leading to an increase in the control cost in that area) strikes two <sup>fi</sup>rms, the <sup>fi</sup>rm that manages this adverse event better (e.g., by changing its operations to better respond to the cost increase), can turn the adversity into an advantage. Although <sup>fi</sup>rm 3’s cost does not change $( c _ { 3 } , c _ { 3 } ^ { \prime } , c _ { 3 } ^ { \prime \prime } )$ , its pro<sup>fi</sup>t increases as <sup>fi</sup>rm 1’s cost increases or both <sup>fi</sup>rms 1 and 2’s costs increase. Firm 3’s pro<sup>fi</sup>t gets affected indirectly through the mean market rating in equilibrium even though its cost does not change.

Table 2. Illustration of the Impact of Cost on the Firms’ Pro<sup>fi</sup>ts

<table><tr><td rowspan="2">Firm</td><td rowspan="2"> $c_i$ </td><td rowspan="2"> $V_i$ </td><td colspan="2">Scenario I</td><td colspan="2">Scenario II</td></tr><tr><td> $c'_i$ </td><td> $V'_i$ </td><td> $c''_i$ </td><td> $V''_i$ </td></tr><tr><td>Firm 1</td><td>1</td><td>5,623.4</td><td>1.1</td><td>5,437.5</td><td>1.1</td><td>5,793.0</td></tr><tr><td>Firm 2</td><td>1</td><td>1,702.5</td><td>1</td><td>1,734.5</td><td>1.5</td><td>1,276.9</td></tr><tr><td>Firm 3</td><td>1.2</td><td>2,466.8</td><td>1.2</td><td>2,501.9</td><td>1.2</td><td>2,713.1</td></tr></table>

Note. $\beta _ { 1 } = 1 . 2 , \beta _ { 2 } = 1 . 3 , \beta _ { 3 } = 1 , \eta _ { 1 } = 1 0 0 , \eta _ { 2 } = 8 0 , \eta _ { 3 } = 9 0 , \tau _ { 1 } = 0 . 2 , \tau _ { 2 } = \tau _ { 2 } = 1$ $0 . 4 , \tau _ { 3 } = 0 . 3 , \theta _ { 1 } = 1 , \theta _ { 2 } = 1 , \theta _ { 3 } = 1 . 1 , S _ { 1 } ( 0 ) = S _ { 2 } ( 0 ) = S _ { 3 } ( 0 ) = 2 0 , x _ { 1 } ( 0 ) = 3 . 1 , S _ { 3 } ( 0 ) = 4 . 3 , S _ { 4 } ( 0 ) = 5 . 5 , S _ { 5 } ( 0 ) = 5 . 5 , S _ { 6 } ( 0 ) = 6 . 5 , S _ { 7 } ( 0 ) = 6 . 5 , S _ { 8 } ( 0 ) = 6 . 5 , S _ { 8 } ( 0 ) = 6 . 5 , S _ { 8 } ( 0 ) = 6 . 5 , S _ { 8 } ( 0 ) = 6 . 5 , S _ { 1 0 } ( 0 ) = 6 . 5 , S _ { 1 1 } ( 0 ) = 6 . 5 , S _ { 1 2 } ( 0 ) = 6 . 5 , S _ { 1 2 } ( 0 ) = 6 . 5 , S _ { 1 2 } ( 0 ) = 6 . 5 , S _ { 1 3 } ( 0 ) = 6 . 5 , S _ { 1 4 } ( 0 ) = 6 . 5 , S _ { 1 4 } ( 0 ) = 6 . 5 , S _ { 1 4 } ( 0 ) = 6 . 5 , S _ { 1 5 } ( 0 ) = 6 . 5 , S _ { 1 4 } ( 0 ) = 6 . 5 , S _ { 1 5 } ( 0 ) = 6 . 5 , S _ { 1 5 } ( 0 ) = 6 . 5 , S _ { 1 5 } ( 0 ) = 6 . 5 , S _ { 1 5 } ( 0 ) = 6 . 5 , S _ { 1 5 } ( 0 ) = 6 .$ x<sub>2</sub> 0  x<sub>3</sub> 0  4, γ 0:1, γ 0:1, γ 0:12, ρ  0:1, b  5.

Proposition 3. The entry of a new firm has the following consequences for the existing (incumbent) firms, the platform, and the consumers:

i. The entry of a low-rating firm increases the total profit of the market and the profits of the incumbent firms. Howev-$e r ,$ it lowers the mean market rating.

ii. The entry of a high-rating firm lowers the profits of the incumbent firms. However, it increases the mean market rating.

iii. The entry of an average-rating firm increases the total profit of the market. However, it leaves the profits of the incumbent firms and the mean market rating unaffected.

The proof of Proposition 3 is provided in Online Appendix F. In the preceding proposition, we are able to make certain analytical predictions when a <sup>fi</sup>rm joins a platform consisting of multiple incumbent <sup>fi</sup>rms. In equilibrium, there are two aggregate outcomes of interest to the consumers and the platform. The mean market rating can be considered to be a measure related to consumer welfare, whereas the total pro<sup>fi</sup>ts of all the <sup>fi</sup>rms in the market can be used as a measure of the platform’s goal. Platforms often charge a brokerage fee from <sup>fi</sup>rms. Thus, the higher the total pro<sup>fi</sup>ts of <sup>fi</sup>rms, the better it is for the platform. 10

The entry of a low-rating <sup>fi</sup>rm (with a rating lower than the mean market that consists of only the incumbent <sup>fi</sup>rms in equilibrium) can have two reinforcing effects.<sup>11</sup> If the ratings of other <sup>fi</sup>rms do not change, the market mean should clearly be lower. As a consequence, the other <sup>fi</sup>rms in the market could decrease their efforts when faced with a lowered market mean. Hence, the market mean should reduce even more in equilibrium. The analysis of the impact of a low-rating <sup>fi</sup>rm becomes more complex when the reaction of the incumbent <sup>fi</sup>rms in the market is considered. It can be shown that, even if the reaction of the incumbent <sup>fi</sup>rms is taken into account, the mean market rating in equilibrium decreases. This increases the pro<sup>fi</sup>ts of incumbent <sup>fi</sup>rms in the market though. The total pro<sup>fi</sup>t (including the new entrant) is clearly higher than the total pro<sup>fi</sup>t before the entry of the low-rating <sup>fi</sup>rm.

Table 3. Illustrating the Impact of Entry

<table><tr><td>Profit</td><td>Before entry</td><td>After entry Scenario (a)</td><td>After entry Scenario (b)</td></tr><tr><td>Firm 1</td><td>113.39</td><td>91.70</td><td>91.70</td></tr><tr><td>Firm 2</td><td>53.82</td><td>50.69</td><td>50.69</td></tr><tr><td>Firm 3</td><td>41.89</td><td>35.21</td><td>35.21</td></tr><tr><td>Firm 4 (entry)</td><td>-</td><td>24.27</td><td>64.27</td></tr><tr><td>Total profit</td><td>209.10</td><td>201.87</td><td>241.87</td></tr></table>

Note. $\rho ~ = ~ 1 , ~ b ~ = ~ 5 , ~ S _ { 1 } ( 0 ) = S _ { 2 } ( 0 ) = S _ { 3 } ( 0 ) = 5 , x _ { 1 } ( 0 ) = x _ { 2 } ( 0 ) = x _ { 3 } ( 0 ) = 0$ $x _ { 4 } ( 0 ) \stackrel { \cdot } { = } 4 , \beta _ { 1 } = 5 . 1 7 , \beta _ { 2 } = 1 , \beta _ { 3 } = 2 . 4 7 , \eta _ { 1 } = 1 7 . 2 , \eta _ { 2 } = 1 3 . 0 2 , \eta _ { 3 } = 1 0 . 9 2 , \eta _ { 4 } = 1 0 \cdot 2 0 . 7 2 , \eta _ { 5 } = 1 3 . 0 2 , \eta _ { 6 } = 1 0 \cdot 2 0 . 7 2 , \eta _ { 7 } = 1 0 \cdot 2 0 . 7 2 , \eta _ { 8 } = 1 0 . 9 2$ $c _ { 1 } = c _ { 2 } = c _ { 3 } = c _ { 4 } = 1 , \beta _ { 4 } = 1 0 , \eta _ { 4 } = 1 0 , \gamma _ { 1 } = \gamma _ { 2 } = \gamma _ { 3 } = \gamma _ { 4 } = 0 , \theta _ { 1 } = \theta _ { 2 } = \theta _ { 3 } = \left| \frac { 1 } { \sin \theta _ { 1 } } \right| = 0$ $\theta _ { 4 } = 1 , \tau _ { 1 } = \tau _ { 2 } = \tau _ { 3 } = \dot { \tau } _ { 4 } = 0 , \dot { S _ { 4 } } ( 0 ) = { \mathrm { 1 } } ( \mathrm { \dot { s c e n a r i o } \dot { a } ) } , \dot { S _ { 4 } } ( 0 ) = 5 ( \mathrm { s c e n a r i o b } ) .$

On the other hand, the entry of a high-rating <sup>fi</sup>rm has two opposing effects. If the incumbent <sup>fi</sup>rms do not react, the entry of a high-rating <sup>fi</sup>rm should result in an increase in the mean market rating. This reduces the pro<sup>fi</sup>ts of the incumbent <sup>fi</sup>rms in the market. Hence, the total pro<sup>fi</sup>t of the incumbent <sup>fi</sup>rms decreases from the level before the entry of the high-rating <sup>fi</sup>rm. It can be shown that the preceding conclusion holds even when we account for the fact that the incumbent <sup>fi</sup>rms react to the entry of the high-rating <sup>fi</sup>rm. However, if we include the pro<sup>fi</sup>t of the new entrant, the total pro<sup>fi</sup>t of the market can be either higher or lower.

Table 3 numerically illustrates the impact of a new entry <sup>fi</sup>rm on the incumbent <sup>fi</sup>rms and the total pro<sup>fi</sup>t of the market. Assume there are three <sup>fi</sup>rms (<sup>fi</sup>rms 1–3) originally in the platform (before the entry), and one <sup>fi</sup>rm (with high rating, <sup>fi</sup>rm 4) joins the platform. The mean market rating in equilibrium changes from 2.63 to 2.79 after the entry. In scenario a, the total pro<sup>fi</sup>t of the market decreases from 209.1 to 201.87 after the entry. In scenario b, the total pro<sup>fi</sup>t of the market increases from 209.1 to 241.87 after the entry. For the incumbent <sup>fi</sup>rms (<sup>fi</sup>rm 1–3), each pro<sup>fi</sup>t decreases after the entry.

Thus, the entry of a high-rating <sup>fi</sup>rm can be good or not so good for the platform (the total pro<sup>fi</sup>t increases or decreases), good for consumers (the mean market rating is higher), and not so good for the incumbent <sup>fi</sup>rms (each incumbent <sup>fi</sup>rm’s pro<sup>fi</sup>t reduces).

When a <sup>fi</sup>rm with an average rating (equal to the mean market rating) enters the market, there is no impact on the mean market rating. Hence, there is no impact on the incumbent <sup>fi</sup>rms in the market. However, the total pro<sup>fi</sup>t (including the new entrant) must be higher than what it was before the entry. The entry of an average-rating <sup>fi</sup>rm is good for the platform (the total pro<sup>fi</sup>t is higher), but the incumbent <sup>fi</sup>rms and consumers do not get affected.

Table 4 summarizes how a new entry in<sup>fl</sup>uences the mean market rating in equilibrium (related to consumer welfare), the pro<sup>fi</sup>ts of the incumbent <sup>fi</sup>rms in the platform, and the total pro<sup>fi</sup>t of the <sup>fi</sup>rms in the platform (related to the platform’s goal).

Corollary 2. The exit of a firm has the following consequences for the existing (incumbent) firms, the platform, and the consumers:

i. The exit of a low-rating firm increases the mean market rating. However, it lowers the profits of the incumbent firms and the total profit of the market.

ii. The exit of a high-rating firm lowers the mean market rating. However, it increases the profits of the incumbent firms.

iii. The exit of an average-rating firm leaves the mean market rating and the profits of the incumbent firms unaffected. However, it decreases the total profit of the market.

The proof of the preceding corollary is provided in Online Appendix G. The exit of a high-rating <sup>fi</sup>rm should decrease the mean market rating, ceteris paribus. Because the new mean market rating becomes lower, the remaining (incumbent) <sup>fi</sup>rms enjoy higher pro<sup>fi</sup>ts. However, this exit also decreases the number of <sup>fi</sup>rms in the market (from N to N – 1), and hence, it is not immediately clear whether the total pro<sup>fi</sup>t of the market must decrease as a result of the exit. The exit of a low-rating <sup>fi</sup>rm has the opposite effect: it increases the mean market rating and lowers the pro<sup>fi</sup>ts of incumbent <sup>fi</sup>rms. The total pro<sup>fi</sup>t of the market decreases. Finally, the exit of an average-rating <sup>fi</sup>rm leaves the mean market rating and the pro<sup>fi</sup>ts of the incumbent <sup>fi</sup>rms unchanged but lowers the total pro<sup>fi</sup>t of the market because the average-rating <sup>fi</sup>rm no longer contributes to the total pro<sup>fi</sup>t.

Proposition 4. A more heterogeneous market (one in which the parameters of the firms are very different) leads to a lower mean market rating in equilibrium.

We study the heterogeneity among <sup>fi</sup>rms using the following structure. De<sup>fi</sup>ne a composite parameter for each <sup>fi</sup>rm as

$$
\delta_ {i} = \frac {\eta_ {i} \beta_ {i}}{(\rho + \tau_ {i}) c _ {i}}.
$$

Let $\bar { \delta }$ be the mean value of the parameter for the <sup>fi</sup>rms in the market. Next, let each <sup>fi</sup>rm’s parameter differ by a factor y from the <sup>fi</sup>rm immediately above (or below) it. That is,

Table 4. Impact of a New Entry

<table><tr><td>New entry</td><td>Mean market rating</td><td>Profits of incumbent firms</td><td>Total profit of market</td></tr><tr><td>Low-rating firm</td><td>Decrease</td><td>Increase</td><td>Increase</td></tr><tr><td>High-rating firm</td><td>Increase</td><td>Decrease</td><td>Increase or decrease</td></tr><tr><td>Average-rating firm</td><td>Unaffected</td><td>Unaffected</td><td>Increase</td></tr></table>

$$
\delta_ {i} = \bar {\delta} + y \bigg (i - \frac {N + 1}{2} \bigg),
$$

where $i = 1 , 2 , . . . , N ,$ , and N is assumed to be odd. If N is even, we can add a virtual <sup>fi</sup>rm to represent the middle <sup>fi</sup>rm and ignore it for the purposes of calculating the mean market rating.

In the preceding, the <sup>fi</sup>rm in the middle has the mean parameter (<sup>¯</sup>δ), and the <sup>fi</sup>rms above (below) arithmetically increase (decrease) from the mean value by the value y. In this structure, the parameter y represents the level of heterogeneity in the market. As y increases, the market is more heterogeneous. The result in the preceding proposition states that a higher value of y leads to a reduction in the mean market rating in equilibrium. The proof of Proposition 4 is provided in Online Appendix H.

The main implication of this result is for the platform. As it targets <sup>fi</sup>rms with more diverse parameters (as opposed to niche <sup>fi</sup>rms with similar parameters), it reduces the competition among the <sup>fi</sup>rms in the platform. This lowers the mean market rating, implying that consumers receive a lower reputation of the product or service. In the next proposition, we consider the impact of the market heterogeneity on the pro<sup>fi</sup>ts of the <sup>fi</sup>rms.

Proposition 5. The total profit of the firms in the market increases with an increase in the extent of heterogeneity in the market.

To understand this result, we <sup>fi</sup>rst let the cause of the heterogeneity arise from the difference in the sales margin $( \eta _ { i } )$ . It is possible to show that, for $i >$ $\begin{array} { r } { \frac { N + 1 } { 2 } , \frac { d V _ { i } } { d y } > 0 } \end{array}$ (see the proof in Online Appendix I). That is, a <sup>fi</sup>rm with a higher-than-average sales margin earns more pro<sup>fi</sup>t as it becomes more heterogeneous (higher y). However, a <sup>fi</sup>rm with a lower-than-average sales margin could earn more or less pro<sup>fi</sup>t. Importantly, the total pro<sup>fi</sup>t of the market (sum of the pro<sup>fi</sup>ts of all the <sup>fi</sup>rms) is higher with more heterogeneity (see the proof in Online Appendix I). A similar argument can be made when the source of heterogeneity comes from other parameters.

These results can be interpreted in terms of the intensity of competition in the market. As the <sup>fi</sup>rms become more heterogeneous, the intensity of competition reduces, which results in a higher total pro<sup>fi</sup>t in equilibrium.

## 6. Extension: Incorporating Platform Reputation Effect

So far, we have not considered the impact of the overall market reputation (the mean market rating or the platform reputation) on consumer demand. However, it is possible that consumers prefer a platform that has a higher mean market rating. The mean market rating may change the platform’s image (reputation), which, in turn, could affect the market demand. In other words, a <sup>fi</sup>rm’s sales can bene<sup>fi</sup>t from higher mean market rating. Therefore, in this extension, we investigate the positive impact of the mean market rating on each <sup>fi</sup>rm’s sales and propose an extended model as follows. As before, for notation simplicity, we suppress the <sup>fi</sup>rm subscript i.

$$
\begin{array}{l l} \underset {u} {\max} & \mathbb {E} \bigg [ \int_ {0} ^ {\infty} e ^ {- \rho t} (\eta S (t) - c u ^ {2}) d t \bigg ] \\ \text { subject   to } & d S (t) = (\beta (x (t) - \mu) + \gamma - \tau S (t) + k \mu) d t \\ & \qquad + \sigma (S (t)) d Z (t) \\ & d x (t) = \Big (u \sqrt {b - x (t)} - \theta \mu x (t) \Big) d t \\ & \qquad + \zeta (x (t)) d W (t), \end{array}\tag{6}
$$

where k is the coef<sup>fi</sup>cient of platform (market) reputation. The de<sup>fi</sup>nitions of the other parameters are the same as those in the base model. We solve the stochastic optimal problem. The optimal control effort is

$$
u ^ {*} = \alpha \sqrt {b - x (t)},
$$

$$
\alpha = \sqrt {(\rho + \theta \mu) ^ {2} + \frac {\eta \beta}{(\rho + \tau) c}} - (\rho + \theta \mu).
$$

The optimal value function given the initial sales rate and the initial rating is

$$
\begin{array}{l} V (S (t _ {0}), x (t _ {0})) = \frac {\eta}{(\rho + \tau)} S (t _ {0}) + 2 c (A - \rho - \theta \mu) x (t _ {0}) \\ \qquad - \frac {\eta \beta \mu}{\rho (\rho + \tau)} + \frac {\eta (\gamma + k \mu)}{\rho (\rho + \tau)} + \frac {b c}{\rho} \bigg (\frac {\eta \beta}{(\rho + \tau) c} \\ \qquad - 2 (\rho + \theta \mu) A + 2 (\rho + \theta \mu) ^ {2} \bigg), \end{array}\tag{7}
$$

where $\begin{array} { r } { A = \sqrt { \left( \rho + \theta \mu \right) ^ { 2 } + \frac { \eta \beta } { \left( \rho + \tau \right) c } } } \end{array}$ . The proofs of the mathematical results are provided in Online Appendix K.

We see that, as the coef<sup>fi</sup>cient of market reputation (k) increases, the value function increases. In the base model, a larger mean market rating (μ) always hurts the value function (see the proof in Online Appendix E). However, because of the positive impact of the mean market rating on sales, as the mean market rating increases, it could either hurt or bene<sup>fi</sup>t the value function depending on the magnitude of the market reputation coef<sup>fi</sup>cient. Thus, the consequences of the entry of a new <sup>fi</sup>rm for the incumbent <sup>fi</sup>rms, the platform, and the consumers can change as the market reputation coef<sup>fi</sup>- cient changes. We propose Proposition 6 to summarize the new <sup>fi</sup>ndings. In this proposition, we only consider the case in which the market reputation coef<sup>fi</sup>cient is suf<sup>fi</sup>ciently large, that is, $k > g ( \mu )$ , where the expression for $g ( \mu )$ is provided in Online Appendix K. When the market reputation coef<sup>fi</sup>cient is relatively small, that is, $k \leq g ( \mu ) .$ , the outcomes speci<sup>fi</sup>ed in Proposition 3 continue to hold.

Table 5. Impact of a New Entry When the Market Reputation Coef<sup>fi</sup>cient Is Suf<sup>fi</sup>ciently High

<table><tr><td>New entry</td><td>Mean market rating</td><td>Profits of incumbent firms</td><td>Total profit of market</td></tr><tr><td>Low-rating firm</td><td>Decrease</td><td>Decrease</td><td>Increase or decrease</td></tr><tr><td>High-rating firm</td><td>Increase</td><td>Increase</td><td>Increase</td></tr><tr><td>Average-rating firm</td><td>Unaffected</td><td>Unaffected</td><td>Increase</td></tr></table>

Proposition 6. When the market reputation coefficient is sufficiently high $( i . e . , k > g ( \mu ) )$ , the entry of a new firm has the following consequences for the existing (incumbent) firms, the platform, and the consumers:

i. The entry of a low-rating firm lowers the mean market rating and the profits of incumbent firms.

ii. The entry of a high-rating firm increases the mean market rating, the profits of the incumbent firms, and the total profit of the market.

iii. The entry of an average-rating firm increases the total profit of the market. However, it leaves the profits of the incumbent firms and the mean market rating unaffected.

The expression of $g ( \mu )$ is provided in Online Appendix K. The proof of Proposition 6 is provided in Online Appendix K. Table 5 summarizes how a new entry in<sup>fl</sup>uences the mean market rating, the pro<sup>fi</sup>ts of incumbent <sup>fi</sup>rms, and the total pro<sup>fi</sup>t of the market.

The main message of the preceding proposition is for the platform owners. When encouraging a new <sup>fi</sup>rm to join the platform, it is crucial to pay attention to the impact on the overall reputation of the platform. This insight is particularly meaningful for the entry of a low-rating <sup>fi</sup>rm because the overall reputation of the platform suffers as a result of the entry. When the market reputation plays a signi<sup>fi</sup>cant role (the market reputation coef<sup>fi</sup>cient is relatively high), the pro<sup>fi</sup>t of each incumbent <sup>fi</sup>rm could decrease. At the same time, the total pro<sup>fi</sup>t of the <sup>fi</sup>rms in the market could also decrease, implying that the entry of a low-rating <sup>fi</sup>rm could hurt both the incumbent <sup>fi</sup>rms and the platform. Therefore, in such cases, a low-rating <sup>fi</sup>rm should not be encouraged to join because it hurts all stakeholders: incumbent <sup>fi</sup>rms (lower individual pro<sup>fi</sup>ts), platform (lower total pro<sup>fi</sup>t), and consumers (lower mean market rating).

Similarly, the exit of a <sup>fi</sup>rm could have different consequences for the incumbent <sup>fi</sup>rms, the platform, and the consumers compared with the base model. We propose Corollary 3 to summarize the new results. Again, we consider the case in which the market reputation coef<sup>fi</sup>cient is suf<sup>fi</sup>ciently high, that is, $k > g ( \mu )$ Otherwise, the outcomes speci<sup>fi</sup>ed in Corollary 2 continue to hold.

Corollary 3. When the market reputation coefficient is sufficiently high $( i . e . , \ k > g ( \mu ) )$ , the exit of a firm has the following consequences for the existing (incumbent) firms, the platform, and the consumers:

i. The exit of a low-rating firm increases mean market rating and the profits of incumbent firms.

ii. The exit of a high-rating firm lowers the mean market rating, the profits of the incumbent firms, and the total profit of the market.

iii. The exit of an average-rating firm decreases the total profit of the market. However, it leaves the profits of the incumbent firms and the mean market rating unaffected.

The expression of g μ is provided in Online Appendix K. The proof of Corollary 3 is provided in Online Appendix K. Concerning the preceding corollary, the pertinent case to focus upon is the exit of a highrating <sup>fi</sup>rm. This leads to a bad outcome for all stakeholders (lower individual pro<sup>fi</sup>ts of incumbent <sup>fi</sup>rms, lower total pro<sup>fi</sup>t, and lower mean market rating), and hence, to the extent possible, a high-rating <sup>fi</sup>rm should be provided incentives to stay in the platform.

## 7. Managerial Implications

Our study has three important takeaways for platform executives and participating <sup>fi</sup>rms: (1) aim for strategic growth, (2) diversity is key, and (3) outrun your competitor. We discuss them here.

## 7.1. Aim for Strategic Growth

Growth is often a core value in the business plan of any organization. Toward this end, many platforms have advocated a get-big-fast strategy to grow the platform (Cennamo and Santalo´ 2013), for example, by continually soliciting new <sup>fi</sup>rms to join the platform at all costs. However, the platform needs to be strategic about growth. Cennamo and Santalo (´ 2013) show that such a “growth at all costs” strategy can be perilous without carefully considering the potential con<sup>fl</sup>icts and disincentives of such a growth strategy, particularly among the <sup>fi</sup>rms on the platform. For example, we saw that the entry of a relatively low-rating <sup>fi</sup>rm may increase the total pro<sup>fi</sup>t of the market (i.e., sum of pro<sup>fi</sup>ts including the new entrant). However, the platform runs into a dilemma here. When a low-rating entrant joins, the incumbent <sup>fi</sup>rms bene<sup>fi</sup>t but the consumers experience a market with a lower mean market rating than before. On the other hand, when a new, high-rating <sup>fi</sup>rm enters, the mean market rating increases (bene<sup>fi</sup>cial for consumers), but the incumbent <sup>fi</sup>rms earn lower pro<sup>fi</sup>ts, and the total pro<sup>fi</sup>t (including the new entrant) may be either lower or higher.

Thus, the platform needs to balance its recruiting activities between low- and high-rating <sup>fi</sup>rms, referred to as the platform governance problem in the literature (Tiwana et al. 2010, Wareham et al. 2014, Huotari 2017, Rietveld et al. 2019). Even when the platform bene<sup>fi</sup>ts (higher total pro<sup>fi</sup>t), one of its stakeholders (incumbent <sup>fi</sup>rms or consumers) could be hurt as a result of the new entry. Encouraging average-rating <sup>fi</sup>rms to join could turn out to be most bene<sup>fi</sup>cial because it has no impact on the incumbent <sup>fi</sup>rms or consumers, but there is a limited extent to which the platform can <sup>fi</sup>nd such <sup>fi</sup>rms and encourage them to join. In such cases, as much as possible, the platform should attempt to grow at the middle rather than at the ends. Growing at the low end of the market is bene<sup>fi</sup>cial to incumbents, but the loss to consumers (resulting from a lower mean market rating) must be kept in check. In the view of such a trade-off, Apple, for example, stipulated strict quality standards for its app developers (Huotari 2017). Growing at the top end is good for consumers and sometimes for the platform, but the loss to incumbent <sup>fi</sup>rms must be weighed when attempting to grow at the high end of the market. This is echoed by Tadelis (2016), in which he points out that promoting seller quality may come at the expense of crowding out incumbents. Rietveld et al. (2019) also show that platform owners of games do not simply promote “best in class” games; rather, they strategically invest in underappreciated games with which there is a greater marginal value to be unlocked.

When the platform reputation plays an important role, it becomes even more important to selectively grow the platform (e.g., encouraging a low-rating <sup>fi</sup>rm to join could be harmful for all stakeholders). When the reputation effect is important, it also becomes important for the platform not to lose <sup>fi</sup>rms at the top, that is, a high-rating <sup>fi</sup>rm should be induced to stay in the platform.

## 7.2. Diversity Is Key

Platforms can bene<sup>fi</sup>t from our results concerning the heterogeneity of <sup>fi</sup>rms that participate in the platform. If a platform only targets similar <sup>fi</sup>rms (e.g., <sup>fi</sup>rms with similar costs, pro<sup>fi</sup>t margins, etc.), it could result in intense competition, leading to lower <sup>fi</sup>rm pro<sup>fi</sup>ts and the total pro<sup>fi</sup>t of the market. Our <sup>fi</sup>ndings show that diversity among <sup>fi</sup>rms is good for the platform and the <sup>fi</sup>rms in the platform. The caveat, however, is that the mean market rating decreases with more diversity. Thus, the platform needs to carefully balance the characteristics of <sup>fi</sup>rms with relatively high margins against those with relatively low margins. This <sup>fi</sup>nding is consistent with Cennamo and Santalo (´ 2019) and Wareham et al. (2014), in which they show the need to have heterogeneous <sup>fi</sup>rms to serve diverse consumers and to meet the evolving market demand. Nintendo in the 1990s, for instance, carefully curbed the number of competing video game titles by forbidding game developers to launch more than <sup>fi</sup>ve titles in a category (Williams 2002).

## 7.3. Don’t Try to Outrun the Bear, Outrun Your Competitor

Concerning <sup>fi</sup>rms, our results allow a <sup>fi</sup>rm to anticipate the impact of changes in various parameters on its pro<sup>fi</sup>t. For example, contrary to what one could expect, a <sup>fi</sup>rm could welcome an increase in the cost of control effort (for example, if the costs of certain inputs, such as labor or materials, increase) if it believes that it can control the cost increase better than its competitors. As Hass and Rigby (2004) succinctly put it, “The key to survival? Play the bear’s game while others become (the prey of) it.”<sup>12</sup> Winning competitors are often those who are able to scrutinize their supply chains, labor deployment, marketing programs, and overhead costs to eliminate wasted dollars to compete. Although consumers do not play a strategic role in this study, they are clearly an important stakeholder. To this end, we have provided several results with regard to the impact of various parameters on the mean market rating in equilibrium. As the mean market rating improves, it bene<sup>fi</sup>ts consumers because they receive a product or service with higher online reputation.

## 8. Conclusion

The ubiquity of online customer reviews is reshaping consumer perception on products or services that are being evaluated for purchase. According to a report from TripAdvisor, more than 90% of business representatives rated online reviews as one of the most important factors for their businesses (GuestRevu 2016). Given the importance of online reputation, we address the question of how the competition impacts a <sup>fi</sup>rm’s control effort to manage its online reputation and, hence, its pro<sup>fi</sup>t. The answer to this question has important implications for the governance of platforms; that constitutes the main focus of this study.

We consider a competitive setting in which all <sup>fi</sup>rms in a market attempt to manage their online reputations (measured by review ratings). Because <sup>fi</sup>nding a Nash equilibrium in our case is intractable, we invoke the notion similar to a mean <sup>fi</sup>eld equilibrium, in which consumers interpret a <sup>fi</sup>rm’s ratings in a relative sense, anchored around a belief about the mean market rating. Then, each <sup>fi</sup>rm’s sales are driven by its own rating and this mean-<sup>fi</sup>eld belief. We develop a controlled diffusion model in which a <sup>fi</sup>rm’s sales are driven by the common belief and its own ratings that are maneuvered by the control effort chosen to maximize its pro<sup>fi</sup>t. Thus, we derive a controlled diffusion model for the evolution of the ratings and sales of a <sup>fi</sup>rm. We prove the existence and uniqueness of the equilibrium mean market rating, which depends on each <sup>fi</sup>rm’s sales margin, cost of control effort, sales rate retardation, ratings decay coef<sup>fi</sup>cient, customer sensitivity to ratings, the total number of <sup>fi</sup>rms in the market, the discount factor, and the upper bound of ratings.

We <sup>fi</sup>nd that, when the customer sensitivity to ratings is high or when the sales margin is high, the <sup>fi</sup>rm exerts more effort (but at a diminishing rate) to boost its rating. It results in an increase in the mean market rating in equilibrium. This <sup>fi</sup>nding re<sup>fl</sup>ects a key structural result in this study that applies in several situations: a particular <sup>fi</sup>rm’s actions directly impact its outcomes (such as rating and pro<sup>fi</sup>t) but indirectly impact these outcomes by acting through the equilibrium mean market rating. Interestingly, the direct and indirect impacts pull in opposite directions. When the direct impact is positive (negative), the indirect impact is negative (positive). Another interesting <sup>fi</sup>nding is that, for a focal <sup>fi</sup>rm, the joint impact on the pro<sup>fi</sup>t if the parameters of multiple <sup>fi</sup>rms were to change can be different from the impact if the parameters of only the focal <sup>fi</sup>rm were to change. For example, if only the sales margin of one <sup>fi</sup>rm were to decrease, it could decrease its pro<sup>fi</sup>t. However, if the sales margin of a competing <sup>fi</sup>rm were to decrease more, then the focal <sup>fi</sup>rm’s pro<sup>fi</sup>t could increase despite a decrease in its sales margin. This somewhat unexpected result arises from the endogenous nature of the mean market rating.

We extend the base model by factoring in the potential impact of the mean market rating on the total demand attracted by the market. The intuition is that the mean market rating may change the platform’s image (reputation), which, in turn, affects the market demand. When the coef<sup>fi</sup>cient of market reputation is suf<sup>fi</sup>ciently small, the consequences of the entry (exit) of a <sup>fi</sup>rm on the incumbent <sup>fi</sup>rms, the platform, and the consumers stay the same with the base model. However, when the impact of the platform’s image is relatively high, the consequences of the entry (exit) may reverse.

We provide several insights concerning the properties of the mean market rating and the pro<sup>fi</sup>t in equilibrium. For example, a more heterogeneous market (one in which the parameters of the <sup>fi</sup>rms are very different) leads to a lower mean market rating and higher total pro<sup>fi</sup>t of the <sup>fi</sup>rms in the market. In addition, our results can inform platforms on how to target certain <sup>fi</sup>rms to join, depending on their ratings. Targeting <sup>fi</sup>rms with average ratings (i.e., the middle of the market) is the safest option considering the goals of the platform (increase the total pro<sup>fi</sup>t) and other stakeholders, namely the incumbent <sup>fi</sup>rms and the consumers. On the other hand, growing the market at the bottom hurts consumers (i.e., targeting <sup>fi</sup>rms with lower than average ratings) but bene<sup>fi</sup>ts both the platform and the incumbent <sup>fi</sup>rms. Finally, growing at the top is good for the platform and consumers but hurts the pro<sup>fi</sup>ts of incumbent <sup>fi</sup>rms.

This study is not without limitations. First, we consider some speci<sup>fi</sup>c functional forms for the drift terms in the state equations. Our results are obviously constrained by these choices. However, the functional forms used are not atypical and have support in previous work on differential games in advertising. Second, it is possible that some savvy customers may see through manipulative activities and act strategically. In this study, we implicitly assume that consumers are nonstrategic. However, strategic consumers are an interesting topic to explore in future work. Third, we consider a homogeneous market in which all <sup>fi</sup>rms compete with one another. Alternatively, we could consider a network-like structure in which the weight between two nodes (<sup>fi</sup>rms) represents the intensity of competition between the nodes. Fourth, in addition to intra market competition, there could be inter market competition. That is, beyond competing <sup>fi</sup>rms in one segment (market), there could be another layer of (possibly weaker) competition across segments. Fifth, we did not consider temporal effects and, instead, restricted ourselves to a steady-state analysis. Given the stochastic nature of the setting, future work could consider how <sup>fi</sup>rms jostle one another for competitive positions in the market and how the equilibrium outcomes (mean market rating, mean individual rating, control efforts, etc.) unfold over time. Finally, future research can also explore the issue of optimizing the number of competing <sup>fi</sup>rms to host in the platform or consider the repercussions of publicizing the mean marketing rating to some selected stakeholders.

## Acknowledgments

The authors gratefully acknowledge the feedback received from the senior editor, the associate editor, and anonymous reviewers. The authors thank the seminar participants at The University of Texas at Dallas as well as participants at the 2018 INFORMS Annual Meeting, 2018 Workshop on Information Technologies and Systems (WITS), and POMS 30th Annual Conference (2019).

## Endnotes

<sup>1</sup> ORM software has become a sizable industry. Webimax, REQ, and Net Reputation are some leading companies that provide special software and services to help firms manage online reputation (Clutch 2020).

Another possible influence chain is effort leading to change in demand leading to change in review volume leading to change in rating. The effort in this chain could involve manipulating traditional marketing-mix variables, such as price or quality, because these variables would clearly affect demand. Our focus in this study is not on traditional variables, such as price, quality, advertising effort, etc., which directly affect demand (Naik et al. 2008, Buell et al. 2016, Boleslavsky et al. 2017), but on the kind of effort that affects ratings (e.g., faster or better response to consumer issues, better management of consumer opinions via analytics, etc.) and, hence, indirectly affects demand (Gu and Ye 2014, Proserpio and Zervas 2017, Gunarathne et al. 2018). This distinguishes our work from the existing work on competition based on traditional variables.

<sup>3</sup> Because we are first presenting a model for an individual firm, we suppress a firm-specific subscript to avoid clutter.

<sup>4</sup> Using the last n ratings to construct x(t) is just one concrete example of how x(t) could be interpreted. It could, for example, be a richer variable that includes not only the numerical rating, but a reputation measure that also captures the text of the reviews. The model we develop is agnostic about how the reputation measure is derived and, as such, can adapt to any measure as long as Equation (1) holds well.

<sup>5</sup> Prior studies show that the price dispersion declines as an internet market matures and as more retailers join the platform (Venkatesan et al. 2007, Ghose and Yao 2011).

<sup>6</sup> Our approach is consistent with many past studies on advertising competition that exclude price as a variable so as to focus on the role of advertising as a strategic variable. As Erickson (1985) points out, other marketing-mix variables (such as price) are omitted so that advertising as one very important variable can be the focus of the study. Similarly, other studies (Erickson 1985, 1995, 2009; Sorger 1989; Fruchter and Kalish 1997; Fruchter 1999; Wang and Wu 2001; Prasad and Sethi 2004; Bass et al. 2005; Naik et al. 2008) investigate firms’ advertising decisions in competitive settings without considering other marketing-mix variables.

<sup>7</sup> Note that our inclusion of a trend term is structurally similar to that of the unobserved component model in time series analysis by which a time series is often decomposed into a trend component and other components (Pelagatti 2015).

<sup>8</sup> The proofs for all the mathematical results in this paper are provided in the online appendix.

<sup>9</sup> We choose $\eta _ { 1 } = 1 0 2 . 6 9 , \eta _ { 2 } = 1 0 1 . 3 9 , \eta _ { 3 } = 1 0 6 . 6 9 , \beta _ { 1 } = 8 . 4 9 , \beta _ { 2 } = 5 . 7 6 ,$ $\beta _ { 3 } = 2 . 3 4 , c _ { 1 } = 1 . 5 0 , c _ { 2 } = 1 . 3 6 , c _ { 3 } = 1 . 0 2 , \tau _ { 1 } = 0 . 0 6 , \tau _ { 2 } = 0 . 0 8 , \tau _ { 3 } = 0 . 0 6 , \theta _ { 1 } = 0 . 0 6 , \tau _ { 2 } = 1 . 0 2 , \tau _ { 3 } = 0 . 0 3 , \tau _ { 2 } = 1 . 0 2 , \tau _ { 1 } = 0 . 0 3 , \tau _ { 2 } = 1 . 0 2 , \tau _ { 2 } = 1 . 0 2 , \tau _ { 3 } = 0 . 0 3 , \tau _ { 2 } = 1 . 0 2$ $1 . 3 1 , \ \theta _ { 2 } = 1 . 7 8 , \ \theta _ { 3 } = 1 . 3 0 , \ \rho = 1 , \ b \ = \ 5 , \ \sigma _ { 1 } = 0 . 1 S _ { 1 } ( t ) , \ \sigma _ { 2 } = 0 . 1 S _ { 2 } ( t ) , \ \sigma _ { 3 } = 1 . 3 1 , \ \theta _ { 2 } = 0 . 1 3 , \ \theta _ { 3 } = 1 . 3 1 , \ \rho = 1 . 3 1 , \ \rho = 1 . 3 1$ $0 . 1 S _ { 3 } ( t ) , \zeta _ { 1 } = 0 . 2 \sqrt { b - x _ { 1 } ( t ) } , \zeta _ { 2 } = 0 . 2 \sqrt { b - x _ { 2 } ( t ) } , \zeta _ { 3 } = 0 . 2 \sqrt { b - x _ { 3 } ( t ) } , \gamma _ { 1 } = 0 ,$ $\gamma _ { 2 } = 1 . 2 7 , \gamma _ { 3 } = 0 . 4 0 , x _ { 1 } ( 0 ) = x _ { 2 } ( 0 ) = x _ { 3 } ( 0 ) = 3 , S _ { 1 } ( 0 ) = S _ { 2 } ( 0 ) = S _ { 3 } ( 0 ) = 5 , \Delta t = \mathrm { 1 2 } , \lambda = 3$ 0:01, and N 3.

<sup>10</sup> For example, commission rates at Expedia range from 20%–25% (Page 2018).

<sup>11</sup> We examine the effects of a firm entry into the platform in the sense of an existing firm joining the platform. That is, we consider what would happen if a firm (e.g., hotel, restaurant, etc.) with its own user base joins the platform.

<sup>12</sup> The bear game (a popular joke) is about two campers attempting to run away from a bear. One of them puts on his running shoes. Upon this, the other remarks that the shoes won’t help outrun the bear. The camper responds, “I don’t need to outrun the bear; I just need to outrun you.”

## References

Anderson KC (2012) The impact of social media on lodging performance. Cornell Hospitality Rep. 12(15):6–11.

Anderson M (2014) 88% of consumers trust online reviews as much as personal recommendations. Accessed December 25, 2017, https://searchengineland.com/88-consumers-trust-online-reviews -much-personal-recommendations-195803

Aseri M, Dawande M, Janakiraman G, Mookerjee V (2020) Ad-blockers: A blessing or a curse? Inform. Systems Res. 31(2):627–646.

Banjo S (2012) Firms take online reviews to heart. Accessed October 6, 2015, http://www.wsj.com/articles/SB10001424052702303292 204577517394043189230?cb=logged0.448628765065223.

Bass FM, Krishnamoorthy A, Prasad A, Sethi SP (2005) Building brand awareness in dynamic oligopoly markets. Marketing Sci. 24(4):556–568.

Boleslavsky R, Cotton CS, Gurnani H (2017) Demonstrations and price competition in new product release. Management Sci. 63 (6):2016–2026.

Buell RW, Campbell D, Frei FX (2016) How do customers respond to increased service quality competition? Manufacturing Service Oper. Management 18(4):585–607.

Cao HH (1999) The effect of derivative assets on information acquisition and price behavior in a rational expectations equilibrium. Rev. Financial Stud. 12(1):131–163.

Cennamo C, Santalo J (2013) Platform competition: Strategic´ trade-offs in platform markets. Strategic Management J. 34 (11):1331–1350.

Cennamo C, Santalo J (2015) How to avoid platform traps. ´ MIT Sloan Management Rev. 57(1):12–15.

Cennamo C, Santalo J (2019) Generativity tension and value creation ´ in platform-based technology ecosystems. Organ. Sci. 30(3): 617–641.

Chari VV, Jagannathan R (1988) Banking panics, information, and rational expectations equilibrium. J. Finance 43(3):749–761.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Vilcassim NJ (1992) An empirical investigation of advertising strategies in a dynamic duopoly. Management Sci. 38(9):1230–1244.

Clutch (2020) Top reputation management companies. Accessed March 24, 2020, https://clutch.co/pr-<sup>fi</sup>rms/reputation-management.

Duan W, Gu B, Whinston AB (2008) The dynamics of online wordof-mouth and product sales-an empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Erickson GM (1985) A model of advertising competition. J. Marketing Res. 22(3):297–304.

Erickson GM (1995) Advertising strategies in a dynamic oligopoly. J. Marketing Res. 32(2):233–237.

Erickson GM (2009) Advertising competition in a dynamic oligopoly with multiple brands. Oper. Res. 57(5):1106–1113.

Erskine R (2018) Study: 97% of business owners say online reputation management is important – here’s how to keep up. Accessed August 30, 2018, https://www.forbes.com/sites/ryaner skine/2018/07/30/study-97-of-business-owners-say-online -reputation-management-is-important-heres-how-to-keep-up/ #2e66bcc56c02.

Forbes (2013) Is online reputation management worth the money? Accessed April 2, 2018, https://www.forbes.com/sites/ learnvest/2013/07/26/is-online-reputation-management-worth -the-monev/#5bf667f839c9

Fruchter GE (1999) The many-player advertising game. Management Sci. 45(11):1609–1611.

Fruchter GE, Kalish S (1997) Closed-loop advertising strategies in a duopoly. Management Sci. 43(1):54–63.

Frydman R (1982) Toward an understanding of market processes: Individual expectations, learning, and convergence to rational expectations equilibrium. Amer. Econom. Rev. 72(4):652–668.

Ghose A, Yao Y (2011) Using transaction prices to re-examine price dispersion in electronic markets. Inform. Systems Res. 22(2):269– 288.

Glassman N (2011) What every social media marketer should know about revinate. Accessed September 22, 2016, http://www.adweek .com/digital/socialmedia-apps-revinate/.

Gu B, Ye Q (2014) First step in social media: Measuring the in<sup>fl</sup>uence of online management responses on customer satisfaction. Production Oper. Management 23(4):570–582.

Gueant O, Lasry J-M, Lions P-L (2011) Mean´ <sup>fi</sup>eld games and applications. Carmona RA, Cinlar E, Ekeland I, Jouini E, Scheinkman JA, Touzi N, eds. Paris-Princeton Lectures on Mathematical Finance 2010 (Springer, Berlin, Germany), 205–266.

GuestRevu (2016) Back to basics: What is online reputation management and why does it matter to hotels? Accessed January 17, 2017, http://blog.guestrevu.com/back-to-basics-what-is-online -reputation-management-and-why-does-it-matter-to-hotels.

GuestRevu (2020) Some of the world’s top hotels are part of the guestrevu family. Accessed March 24, 2020, https://www .guestrevu.com/clients.

Gunarathne P, Rui H, Seidmann A (2018) When social media delivers customer service: Differential customer treatment in the airline industry. Management Inform. Systems Quart. 42(2):489–520.

Hass D, Rigby DK (2004) Outsmarting walmart. Harvard Business Review Online (December), https://hbr.org/2004/12/outsmarting -wal-mart.

Ho YC, Wu J, Tan Y (2017) Discon<sup>fi</sup>rmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3): 626–642.

Hui X, Saeedi Ma, Shen Z, Sundaresan N (2016) Reputation and regulations: Evidence from eBay. Management Sci. 62(12): 3604–3616.

Huotari P (2017) Too big to fail? Overcrowding a multi-sided platform and sustained competitive advantage. Bui TX, ed. Proc. 50th Hawaii Internat. Conf. System Sci. (IEEE, Waikoloa Village, HI), 5275–5284.

Jabr W, Zheng Z (2014) Know yourself and know your enemy: An analysis of <sup>fi</sup>rm recommendations and consumer reviews in a competitive environment. Management Inform. Systems Quart. 38(3):635–654.

Kent K (2014) Catching up with the competition: How to get more online reviews from your customers. Accessed December 25, 2017, https://www.reviewtrackers.com/catching-competition -online-reviews-customers/.

Kumar N, Qiu L, Kumar S (2018) Exit, voice, and response in digital platforms: An empirical investigation of online management response strategies. Inform. Systems Res. 29(4):849–870.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Kwark Y, Lee GM, Pavlou PA, Qiu L (2021) On the spillover effects of online product reviews on purchases: Evidence from clickstream data. Inform. Systems Res. Forthcoming.

Lasry J-M, Lions P-L (2007) Mean <sup>fi</sup>eld games. Japanese J. Math. 2 (1):229–260.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Li X, Hitt LM, Zhang ZJ (2011) Product reviews and competition in markets for repeat purchase products. J. Management Inform. Systems 27(4):9–42.

Little JDC (1979) Aggregate advertising models: The state of the art. Oper. Res. 27(4):629–667.

Liu D, Kumar S, Mookerjee VS (2012) Advertising strategies in electronic retailing: A differential games approach. Inform. Systems Res. 23(3):903–917.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Sci. 62(12):3412– 3427.

Manley B (2017) Hoteliers strive for control in age of online ratings. Accessed September 2, 2018, http://www.hotelnewsnow .com/Articles/259581/Hoteliers-strive-for-control-in-age-of -online-ratings.

Manski CF (1993) Identi<sup>fi</sup>cation of endogenous social effects: The re-<sup>fl</sup>ection problem. Rev. Econom. Stud. 60(3):531–542.

Mayzlin D (2006) Promotional chat on the internet. Marketing Sci. 25(2):155–163.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Muth JF (1961) Rational expectations and the theory of price movements. Econometrica 29(3):315–335.

Naik PA, Prasad A, Sethi SP (2008) Building brand awareness in dynamic oligopoly markets. Management Sci. 54(1):129–138.

Page V (2018) How Expedia makes money. Accessed September 2, 2018, https://www.investopedia.com/articles/investing/080315/ how-expedia-makes-money.asp.

Pelagatti MM (2015) Time Series Modelling with Unobserved Components (CRC Press, Boca Raton, FL).

Prasad A, Sethi SP (2004) Competitive advertising under uncertainty: A stochastic differential game approach. J. Optim. Theory Appl. 123(1):163–185.

Proserpio D, Zervas G (2017) Online reputation management: Estimating the impact of management responses on consumer reviews. Marketing Sci. 36(5):645–665.

Rietveld J, Schilling MA, Bellavitis C (2019) Platform strategy: Managing ecosystem value through selective promotion of complements. Organ. Sci. 30(6):1232–1251.

Rubel O, Naik PA, Srinivasan S (2011) Optimal advertising when envisioning a product-harm crisis. Marketing Sci. 30(1):1048–1065.

Sorger G (1989) Competitive dynamic advertising: A modi<sup>fi</sup>cation of the case game. J. Econom. Dynamic Control 13(1):55–80.

Tadelis S (2016) Reputation and feedback systems in online platform markets. Annual Rev. Econom. 8:321–340.

Tiwana A, Konsynski B, Bush AA (2010) Research commentary-platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Inform. Systems Res. 21(4): 675–687.

Venkatesan R, Mehta K, Bapna R (2007) Do market characteristics impact the relationship between retailer characteristics and online prices? J. Retailing 83(3):309–324.

Veronesi P (1999) Stock market overreactions to bad news in good times: A rational expectations equilibrium model. Rev. Financial Stud. 12(5):975–1007.

Wang Q, Wu Z (2001) A duopolistic model of dynamic competitive advertising. Eur. J. Oper. Res. 128(1):213–226.

Wareham J, Fox PB, Cano Giner J (2014) Technology ecosystem governance. Organ. Sci. 25(4):1195–1215.

Wikipedia. Reputation management. Accessed March 24, 2020, https://en.wikipedia.org/wiki/Reputation\_management.

Williams D (2002) Structure and competition in the US home video game industry. Internat. J. Media Management 4(1):41–54.

Wu R, Qiu C (2016) Seller manipulation of consumer reviews under competition. Bui TX, Sprague RH, eds. Proc. 49th Hawaii Internat. Conf. System Sci. (IEEE, Koloa, HI), 3574–3582.

Yang M, Zheng Z, Mookerjee V (2019) Prescribing response strategies to manage customer opinions: A stochastic differential equation approach. Inform. Systems Res. 30(2):351–374.

Ye S, Gao G, Viswanathan S (2014) Strategic behavior in online reputation systems: Evidence from revoking on eBay. Management Inform. Systems Quart. 38(4):1033–1056.

Zheng Z, Pavlou AP, Gu B (2014) Latent growth modeling for information systems: Theoretical extensions and practical applications. Inform. Systems Res. 25(3):547–568.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
