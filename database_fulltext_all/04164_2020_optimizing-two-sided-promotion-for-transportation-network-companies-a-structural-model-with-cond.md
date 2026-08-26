---
otero_id: 4164
otero_key: "D6389UFV"
title: "Optimizing Two-Sided Promotion for Transportation Network Companies: A Structural Model with Conditional Bayesian Learning"
authors: "Jinyang Zheng; Fei Ren; Yong Tan; Xi Chen"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0908"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/D6389UFV/fulltext/images/f1aada34805e83fe0ffbcba847aeca7f22f41451e51e78d78cc848840b3dd7d5.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Optimizing Two-Sided Promotion for Transportation Network Companies: A Structural Model with Conditional Bayesian Learning

Jinyang Zheng, Fei Ren, Yong Tan, Xi Chen\*

To cite this article: Jinyang Zheng, Fei Ren, Yong Tan, Xi Chen\* (2020) Optimizing Two-Sided Promotion for Transportation Network Companies: A Structural Model with Conditional Bayesian Learning. Information Systems Research

Published online in Articles in Advance 30 Jul 2020

https://doi.org/10.1287/isre.2019.0908

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Optimizing Two-Sided Promotion for Transportation Network Companies: A Structural Model with Conditional Bayesian Learning

Jinyang Zheng,<sup>a</sup> Fei Ren,<sup>b</sup> Yong Tan,<sup>c</sup> Xi Chen<sup>d,</sup>\*

<sup>a</sup> Krannert School of Management, Purdue University, West Lafayette, Indiana 47907; <sup>b</sup> Guanghua School of Management, Peking University, 100871 Beijing, China; <sup>c</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>d</sup> Business School, Nanjing University, 210093 Nanjing, China

\*Corresponding author

Contact: zhengjy@purdue.edu, https://orcid.org/0000-0001-5028-4193 (JZ); fren@gsm.pku.edu.cn, https://orcid.org/0000-0002-2310-3972 (FR); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT); chenx@nju.edu.cn https://orcid.org/0000-0002-2634-8641 (XC)

Received: January 20, 2017 Revised: September 1, 2018; June 7, 2019 Accepted: September 24, 2019 Published Online in Articles in Advance: July 30, 2020

https://doi.org/10.1287/isre.2019.0908

Copyright: © 2020 INFORMS

Abstract. The mobile app of a transportation network company (TNC) has reshaped the taxi business model by providing new features and allowing the TNC platform to run a diverse two-sided sales promotion to help introduce those new features. We investigate the economic value of this app and how drivers build an initial preference for passenger matching, the cancellation feature, and online pay as well as how a two-sided sales promotion affects drivers’ willingness to use the TNC app. We estimate a structural model of drivers’ decisions to accept orders and to cancel generated orders and their perception of passengers’ willingness to utilize a sales promotion. Bayesian learning processes are introduced to account for drivers’ learning new features. We find evidence of the economic value of new features on a TNC app and drivers’ learning about the value of those features. Our results show that a platform subsidy and bids from passengers might signal low quality of service, and that platform cashback to passengers has a positive effect on drivers by increasing drivers’ chances of being rewarded. Our results further indicate that the substantial value of early promotion not only encourages current usage but also fosters learning that sustains drivers’ continued use of the app, and show how cashback for passengers affects the decisions of drivers. Finally, our policy simulations show improved performance with regard to drivers’ willingness to use the app as well as its cost effectiveness.

History: Raghu Santanam, Senior Editor; Mingfeng Lin, Associate Editor. Funding: This work was supported by the National Natural Science Foundation of China [Grants 71572004, 71831005, 71729001, 71490723, 71771118, and 71471083] and by the Ministry of Education Humanities and Social Sciences Foundation of China [Grant 18YICZH146] Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2019.0908

Keywords: transportation network companies • two-sided sales promotion • Bayesian learning • structural mode

## 1. Introduction

A transportation network company (TNC) is defined as “a service that does not own vehicles or employ drivers, and relies on software to connect passengers to rides” (California Public Utilities Commission 2013, p. 3). Early operators of transportation network apps include such well-funded firms as Uber, Lyft, Hailo, Ola Cabs, and Didi Dache. A TNC creates a two-sided market with two versions of its app, one for passengers to generate orders and the other for drivers to select orders. Both versions can be easily downloaded from major app platforms, including the App Store, Google Play, and Windows Phone Apps.

TNCs have drawn the attention of information systems and economics researchers due to the transformative and disruptive impact of their informationtechnology-enabled features on transportation systems. Those features, which are, in general, available in any TNC app, significantly reshape the business process and thus create economic value as follows. First, TNC apps typically provide internet-based matching, which expands the choice sets of both sides of users, passengers and drivers, beyond those of telephone reservation or roadside matching. Second, as the TNC is fundamentally a reservation-based business model, TNC apps brings more flexibility by allowing users to cancel orders or reservations, which is typically prohibited in the traditional reservationbased transportation model. With the cancellation function, users can easily react to updated information about the quality of orders and about other options, such as roadside hailing.

Third, most of the mainstream TNC apps enhance simplicity and flexibility in the transaction process by featuring “online pay,” which enables passengers to handle their payments automatically. Once a trip is completed, the TNC app digitally transfers the fare from the passenger to the driver’s online-pay account and immediately reports the fare, route, and time through email to passengers. Prior research has quantified the transformative impact of TNC at an aggregative level, such as the overall impact of TNC on a particular dimension, by treating TNC’s entry or exit as the finest grain (Greenwood and Wattal 2017, Gong et al. 2017, Park et al. 2017, Zhang and Li 2017, Burtch et al. 2018, Rhee et al. 2018). Scant research has quantified the transformative impact at a microlevel and identified its economic value at the attribute (feature) level, such as the value of matching, cancellation, or online pay.

Although TNC apps provide potentially valuable new features, a typical challenge, especially during the introductory period, faced by TNC platforms is to educate users to adopt the product and to overcome their unfamiliarity with the features. In particular, due to increasing demand, potential government regulation, and low exit cost for drivers, the bottleneck for a rapidly growing TNC is on the supply side. Because drivers do not have any long-term commitment to work for the TNC platform and the exit cost is low, how to accelerate drivers’ learning about the new features and maintaining their high app usage rate in a cost-effective way are crucial tasks for TNCs. Even though there has been a long-standing research stream on facilitating consumer learning and product usage (e.g., Erdem and Keane 1996, Erdem and Sun 2002, Ackerberg 2003, Chen et al. 2009), very little attention has been paid to the supply side.

A common approach to facilitate learning and product usage is a sales promotion. For example, during the introduction of their apps to drivers, Uber and Lyft paid drivers a 5% bonus for every ride based on the app. In 2016, Uber raised one billion U.S. dollars (USD) to promote the adoption of an Uber network in China, subsidizing new drivers as much as triple the regular fare per order during certain periods. Currently, Uber and Lyft still offer several forms of promotion, including a sign-up bonus and weekly promotion for their drivers. Other firms, such as Didi in China, have adopted similar strategies. Unlike PayPal’s one-time \$10 (throughout, \$ is for the amount in USD) bonus to open an account, these promotions typically last for a longer period for drivers, are repeated, or require several orders, depending on how fast the learning process can be accomplished.

Compared with how traditional taxis offer promotions, a TNC app makes the release, implementation, and adjustment of a promotion more flexible. The app allows the platform to target the learning of a specific feature of the app by making the promotion contingent on using that feature. In addition, given the two-sided nature of TNC apps, drivers and passengers might respond to promotions differently. A two-sided sales promotion can be designed for a TNC app such that the policies for passengers and drivers can be tailored separately for a more effective promotion. The literature has empirically documented the dynamics between empirical consumer learning and a traditional price promotion (e.g., spillover effects by a short-term price promotion for consumers (Erdem and Sun 2002) and a permanent price cut for consumers (Chen et al. 2009)). Limited research, however, has focused on the effectiveness of the mechanism of a two-sided promotion policy on learning and product usage.

The objectives of this study are twofold. First, we investigate the transformative impact of a TNC on taxi drivers at a microlevel. We focus on the driver side of the TNC platform because the market in our context as well as in many others is in demand due to regulation; this makes the supply side more important to platform performance. We are particularly interested in the economic value at the attribute (feature) level, such as the value of matching, cancellation, and online pay. Second, we quantify drivers’ learning of those attributes and further examine how a twosided sales promotion affects drivers’ learning dynamically and further affects drivers’ propensity to use a TNC app. In addition to the direct effect of instantly increased usage, a promotion can generate, in the long run, the indirect effect of drivers’ learn ing about the app through usage experience. A pro motion can accelerate usage experience and help reduce user uncertainty about and increase recognition of the true value of each attribute. We explicitly disentangle the indirect effect of sales promotions on drivers’ app usage through their learning from the direct effect of sales promotion. In addition, given that a two-sided promotion is provided, we examine whether the promotion on the passenger side also will incur an indirect effect on the driver side. Based on these findings, we help a TNC design better promotion schemes to accelerate drivers’ learning while maintaining cost effectiveness.

There are two major challenges to achieving these objectives. First, the remodeled business process, based on the use of the app, consists of sequential and interconnected decisions in each transaction, such as whether to accept an order, cancel that order, or use online pay for that order if finished. A sales promotion might have different effects on each transaction decision. The effect on one stage of a decision might indirectly affect another stage of the decision for a forward-looking driver. For example, one sales promotion policy in our data sample is that both drivers and passengers receive a cashback bonus when passengers use the online-pay function. Therefore, an order with higher potential for a cashback bonus will increase a forward-looking driver’s willingness to accept and fulfill the order. Without understanding a multiple decision-making process enabled by new features, however, it is impossible to quantify the effects of a sales promotion accurately. Therefore, we build a finite-horizon, forward-looking model, following Arcidiacono (2005), to explicitly recover the data-generation process of drivers’ sequential decisions in the presence of a sales promotion.

Second, because a sales promotion during the introductory period might have indirect effects due to diminishing uncertainty, our model needs to account for uncertainties about the new features embedded in different stages of decisions. A typical Bayesian learning model can handle this effectively; however, such a model is limited to the learning of one attribute associated with one decision. In our case, each usage experience consists of multiple attributes, with each attribute in one stage of a decision. Given that the stages of decisions are related to each other, the learning associated with different stages should be connected. We construct our structural model with Bayesian learning conditional on earlier-stage decisions to model the connected learning processes of a driver’s willingness to accept an app-generated order and to fulfill the order as well as the driver’s belief about the passenger’s willingness to use the onlinepay function.

Using data from a leading TNC in China, we quantify drivers’ learning how to use the app to accept orders and how to use the cancellation function as well as drivers’ beliefs about how passengers learn about the use of online pay. We identify, separately and economically, the cost associated with TNC matching, cost incurred by the canceled order, and cost of using online pay. The attribute values of the TNC matching, cancellation, and online-pay features are undervalued at the very beginning and, later on, are perceptually corrected by drivers’ learning through accumulated experiences at different learning rates. In particular, learning how to accept an order is the fastest, and learning the fulfilling/canceling feature is the slowest. We find that bids from passengers, subsidies from the app provider, and an online-paycontingent cashback bonus for passengers and for drivers all positively affect drivers’ decisions to accept and fulfill orders. This occurs through not only the direct impact on the latent utility of taxi drivers but also the indirect impact of drivers’ learning and looking forward in regard to passengers’ decisions to use online pay. In particular, bids from passengers and subsidies from the app provider exhibit a smaller magnitude of impact on drivers’ willingness to accept and fulfill an order than does the cashback bonus, as they potentially signal high risk and/or cost for that order. Our counterfactual analysis explicitly separates the learning-induced indirect effects of a sales promotion from the direct effects on usage increase. We also identify the forward-looking-induced indirect effects of a sales promotion for passengers on drivers’ decisions and provide managerial suggestions on how to accelerate driver learning while being cost effective.

The remainder of the paper is organized as follows. In Section 2, we briefly discuss the related literature and our contributions correspondingly. We describe the research context and our data set in Section 3. In Section 4, we present our model of drivers’ decisions to use the TNC app. In Section 5, we discuss our estimation strategy and report the estimation results. We simulate data to generate insights of our model and propose optimized sales promotion strategies in Section 6. Finally, we summarize our findings and conclude our research in Section 7.

## 2. Literature Review

## 2.1. The Transformative and Disruptive Impact of Information Technology in Transportation

Our paper seeks a microlevel understanding of the transformative and disruptive impact of the TNC app on drivers. The majority of prior research has quantified the economic value of TNC’s impact at a societal or an aggregative level, mainly in the format of social welfare (Buchholz 2015, Cohen et al. 2016, Frechette et al. 2019, Lam and Liu 2018). In addition, more particular dimensions of TNC’s impact (e.g., safety (Greenwood and Wattal 2017, Park et al. 2017), the structure and efficiency of transportation systems (Gong et al. 2017, Rhee et al. 2018), and consumption and business activity (Zhang and Li 2017, Burtch et al. 2018)) have been quantified by treating TNC’s entry or exit as the finest grain. An economic value quantification that is at the information technology (IT)– attribute level, such as the value of matching, cancellation, and online pay, warrants finer-grained investigation, such as a microlevel investigation of individual-level user behavior.

Recent studies apply individual-level structural models and counterfactual analysis to gauge the attribute-level impact of IT. For example, Lam and Liu (2018) find that 64% of welfare gains for passengers are from dynamic pricing. Buchholz (2015) shows that allowing tariffs to vary by time, location, or distance can enhance allocative efficiency, given the presence of search frictions. Our work contributes to this category of literature by further investigating the economic value of more IT-enabled features in the context of TNC. In particular, by building a structural model of the driver’s decision-making process, we identify the effectiveness and the mechanism of a twosided promotion; the attribute value; and the learning of matching, canceling, and online-pay features for drivers.

## 2.2. Learning and Finite-Horizon, Forward-Looking Structural Model

Our work applies a Bayesian learning framework to understand drivers’ decisions under uncertainty. Bayesian learning has been widely applied to study consumer learning. Erdem and Keane (1996) first identified consumer learning about product quality levels through experience and unobserved signals, such as advertising, by applying the Bayesian updating process. Due to the learning model’s applicability to consumers’ choices under uncertainty, the model has been extended to account for many formats of information, such as learning from observed signals (Erdem et al. 2008), from online reviews with different credibility (Zhao et al. 2013) and with different weights, and from their own preference for multiple attributes and variance of preference (Wu et al. 2015). Researchers have applied the learning model in a more complex context—for example, pharmaceutical treatment (Crawford and Shum 2005, Chan and Hamilton 2006) and addictive products, such as cigarettes (Chen et al. 2009). In information systems research, the learning model has been used to understand content generation and consumption on the mobile internet (Ghose and Han 2011), ideation on crowdsourcing (Huang et al. 2014), and online reviews (Ho et al. 2017). Prior studies of Bayesian learning focus on the consumer side. Recent twosided market-based business models, however, lead decision uncertainty to the supply side. Our work contributes to this literature by extending Bayesian learning to study the supply-side decision under uncertainty, shown as drivers’ decisions.

Another unique feature of drivers’ learning under our context is that a driver will learn multiple attributes associated with different but linked stages. To accommodate this feature, we follow Arcidiacono (2005) to develop a finite-horizon, forward-looking model and integrate it with Bayesian learning in each stage. To our knowledge, this is the first attempt to integrate the finite-horizon dynamic model with Bayesian learning to allow conditional learning on multiple stages.

## 2.3. Promotional Strategies

Our research is related to the literature on price promotion. A large quantity of industry anecdotes identify price promotion in the product introduction period as a strategy to enhance usage experiences and to foster consumer learning. However, in most research settings of experience goods with an adequate variation of prices, a sales promotion is limited in its direct effect and is considered equivalent to a temporary price cut. Consequently, very little attention has been paid to teasing out the indirect effects of a sales promotion from the direct price effect. There are a few exceptions; Erdem and Sun (2002), for example, find evidence of spillover effects of a sales promotion and advertising in umbrella branding of multiple products. Chen et al. (2009) examine another extreme case of a sales promotion as a permanent price cut for cigarettes and find the effectiveness of a permanent price cut when considering the indirect effects through forward-looking behavior, learning, and addiction. We contribute to this research stream by identifying the indirect effects of a short-term sales promotion for a new product/feature through learning and forward-looking.

In addition, we consider a two-sided promotion. Albuquerque et al. (2012) evaluate the effectiveness of promotion activities, including price promotion, in an online two-sided market of user-generated content, considering the network effects. In their setting, an individual user can play interchangeable roles in both sides of the market, and there is a “one-sided” promotion for a user in the two-sided market. Our work differs from the previously noted work by focusing on a two-sided promotion. In our context, the two sides, a driver and a passenger, cannot be one individual during a transaction, and the promotion policies for the two sides can be different. We focus on the indirect effects of a passenger’s promotion on a driver’s decision through the forward-looking behavior.

## 3. Research Context and Data 3.1. Research Context

Our data are from the leading mobile app–based TNC in China. We focus on its market when the app has been available for more than 15 months and in one of the first-tier cities in China, whose regulatory environment and industry characteristics of taxi service are very similar to those of the United States. The taxi service is highly fragmented, and there are 189 companies that are authorized to run the taxi business. Those companies will further lease their taxis to the taxi drivers, who pay the costs of leasing, gas, and insurance, and then collect all residual revenue as profit. As a result, drivers do not centrally coordinate their search behavior. Before the availability of TNCs, the majority of orders came from street hailing, and the rest came from prearranged rides. As a result, the traditional operation of taxis incurs a high searching cost, in the form of wasted time and fuel, to provide a match with a potential passenger.

Despite the decentralized operation, the taxi market is heavily regulated in the following ways. First, the pricing is regulated as a fixed two-part tariff fare that applies to all drivers. Therefore, even though the

TNC could subsidize drivers, the base fare is constant, no matter whether a driver takes an order online or offline. Second, a fixed-number medallion system is applied to control the supply size. As a result, the supply of taxis on our focal market is significantly lower than the demand. The statistics show a ratio of more than 500 people per taxi in this city. These statistics are consistent with the popularity of the app on the demand side; based on the usage pattern in our sample, orders arrive every few minutes. This renders the shortage of supply a crucial challenge for the TNC platform.

Different from Uber in the United States, none of the TNCs can operate their own vehicles in our focal market without a medallion. Our focal TNC operates its systems with existing taxis that have medallions and does not have any official or monopolistic power over the taxi drivers, especially during the period that we study. This helps to control for other effects, such as car characteristics and driver characteristics, leaving the introduction of the app and promotional activities as the only exogenous changes on IT attributes.

There are three types of sale promotion and subsidies provided during our observation. First, cashback to both driver and passenger is provided to encourage the adoption of online pay. Specifically, both the passenger and driver in one transaction will be rewarded with a fixed amount if the passenger pays the fare online instead of by cash. Similar to most marketing campaigns, the cashback plan for passengers is made public, but that for drivers is revealed to drivers only through the app right before its implementation. The cashback policy is not dynamic pricing and, thus, does not respond to an individual driver’s activities in a real-time manner. It is the same for all drivers, and its duration is unknown until it is updated. Figure 1 shows that each policy is stable and lasts for a long time relative to the duration of one order, and there is no pattern of spikes at the beginning/end of one specific policy period, perhaps due to the uncertain time for a policy announcement. As a result, we believe that there cannot be forwardlooking behavior for a promotion policy change.

Second, the platform provides subsidies that are not contingent on the usage of online pay. Notably, the subsidy provided at the initial stage is not an individual-level dynamic pricing scheme that is used to alleviate the spatial imbalance in a later stage of this app. In fact, the subsidy plan, such as a late-night/ rush-hour subsidy per order, applied to enrich the supply, is fixed and is available for all drivers. It is also revealed before a driver’s decision.

Third, the platform encourages passengers to subsidize drivers by paying bids. A bid is optional and order specific. A passenger could provide a bid when initializing a bid to compensate for the potential additional cost of a driver and, thus, increase the chance of being accepted by the driver. Further, subsidies and bids are provided independently because a passenger does not know the subsidies before bidding.

Figure 1. Sales Promotion Versus Outcome Variable Dynamics  
![](/api/attachments/D6389UFV/fulltext/images/0313e1f23841d216ba5ea2315663c07a75b82e6d8b923e38dce4afba3bb1175c.jpg)

![](/api/attachments/D6389UFV/fulltext/images/c68dbc442b108afe5a849abb3fab3e5f9feb84f19fc3c6d8188f5d4e2b1adea5.jpg)

![](/api/attachments/D6389UFV/fulltext/images/e7a229797076aeaeb992d5031a4ceef1059118d28d464f85cea8fb4c1267bdd9.jpg)

## 3.2. Data-Generation Process

We display the decision tree of a driver in Figure 2. From a driver’s perspective, each transaction involves three stages. Prior to Stage 1, the app provider announces a cashback offer to drivers and passengers. An order is then initiated by a passenger who needs a taxi and who inputs information on his or her current location (mandatorily) and destination (optionally). Usually, this step is automated by Global Positioning System (GPS) and voice messages, which are unobservable to econometricians. The platform subsidy for drivers will be added, and the passenger could additionally bid. Subsidies and bids are paid independently and added to cashback and the regular fare. The order, including the information on the bid, subsidy, and cashback, will be sent, upon the completion of the inputs, to all available and nearby drivers. A driver receives one order at a time.

In Stage 1, a driver will decide, given the previously noted information, whether to accept an order from the app. If a driver accepts an order from the app, he or she will receive the regular fare, the passenger’s bid, and a platform subsidy (if applicable); if the passenger pays online, the driver also will receive a cashback bonus. If the driver does not accept an order, no penalty will be imposed. He or she might take orders from other sources (e.g., roadside taxi hailers, the call center, or the next order from any source). In this regard, it should be noted that appbased orders are not necessarily superior to regular orders. Even though drivers can receive benefits, such as monetary rewards as well as ease of use due to the app’s functionality, they also incur extra cost for the app’s functions. For example, drivers need to use third-party financial services to process transactions, which reduces the instant gratification associated with cash. There are also some additional costs related to the use of the app, such as drivers’ efforts to install the app and to pay attention to notifications from the app as well as the idle time while driving to pick up passengers. A driver might be uncertain about the attribute value of using the app to match a passenger.

Figure 2. Decision Stages of Drivers

![](/api/attachments/D6389UFV/fulltext/images/907c248974bb46700290c3b7df216ca3b08a7496a15e3848a93676172d35a297.jpg)

After accepting an order, in Stage 2, a driver can decide whether to fulfill or cancel it. The cancellation feature in our observation is available only to drivers, as the TNC’s major objective is to maintain a lower cancellation rate by passengers and to make the platforms more attractive for the drivers due to the imbalanced demand and supply. Accordingly, a driver will not be penalized for canceling an order. A driver can cancel if he or she deems the order to be low quality or risky when additional information is generated after Stage 1 (e.g., updated traffic conditions/control, accidents on the way to pick up the passenger(s), difficulty in finding the pickup location, comes in or if a better alternative is available). In addition, as a new feature that does not exist in the traditiona taxi model, cancellation also might be triggered by the purpose of learning under uncertainty. A driver might be more likely to use the cancellation feature at the very beginning due to uncertainty about this feature. Given this expectation, a driver might be more willing to accept a low-quality order at the beginning so that he or she can try the cancellation feature later on.

Drivers receive payment after they complete the service. Stage 3 involves the decision by a passenger to pay online or in cash, conditional on the ride being completed. Note that paying online and in cash are the only two payment options in our context. Paying online incurs a positive attribute, such as convenience, as well as potential negative ones; for exam ple, the function may be difficult to use, be unstable, or have a high failure rate. Even though this is not the driver’s own decision, rational drivers will form a belief about this decision because they may benefit from it.

Rational drivers are both backward-looking and forward-looking when using a TNC app. Backwardlooking means that drivers learn to use the different functions associated with the different stages based on their usage experience. Each usage experience signals to the driver the attributes of functions such that he or she will be more certain when using the app. Forward-looking implies that drivers make decisions in earlier stages based on their belief about potential outcomes in later stages as a means to optimize their overall utility. This behavior connects the decisions made in different stages.

## 3.3. Data Description

We collect a panel of structured data from the TNC firm. We randomly sample 1,000 driver identifications (IDs) from all of the driver IDs in the database of the company and retrieve all of the transactional records that belong to those drivers. Note that the notion of learning is meaningful only when a user experiences the feature more than once (Huang et al. 2014). We exclude those drivers who never have any activity on the app, which results in a sample of 942 drivers.

We restrict our attention to the first 90 days of the data for the following two reasons. First, initial usage experience is required to identify the learning. Second, there are significant feature updates after that time period but no significant changes of features other than online pay as we examine the feature updates on the Apple and Android version history. In total, we have 198,689 transactional records. We observe the following seven variables: whether drivers accept the orders, whether transactions are fulfilled, whether online pay is used, cashback amount for passengers when using online pay, cashback amount for drivers when passengers use online pay, bids from passengers, and subsidies from the TNC platform. These data, in general, provide a record of the business process and sales promotion by the TNC platform. We show the summary statistics in Table 1.

We calculate the daily outcome variables that correspond to daily promotion policies, as Figure 1 shows. The daily average outcome variables are shown with solid, dashed, and dotted lines to represent the daily acceptance rate, daily fulfillment rate, and daily online-pay rate, respectively. In general, usage of online pay and fulfilled transactions are proportional to the accepted amounts, with a rising trend over time. The sales promotion policy chart shows that the cashback promotion policy also changed over time. For drivers, it started at 0 and had increased by day 10, an increase that, with some fluctuation, was maintained. For passengers, it also started at 0, went up from day 10 to day 80, and declined afterward. The other rewards chart shows a declining trend of bids from passengers and subsidies from the platform.

## 3.4. Model-Free Evidence

We provide some model-free evidence of the effects of a sales promotion and of learning through the following descriptive analysis. First, we compare the outcome variables with respect to a sales promotion policy in Figure 1, which shows an overall increase with a more intensive sales promotion, which indicates that a sales promotion stimulates acceptance, fulfillment, and online-pay rates. Interestingly, a comparison of the outcomes between day 10 and day

Table 1. Summary Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Min</td><td>Max</td></tr><tr><td>Acceptance</td><td>0.7622</td><td>0.4963</td><td>0</td><td>1</td></tr><tr><td>Fulfillment</td><td>0.6388</td><td>0.4803</td><td>0</td><td>1</td></tr><tr><td>Online pay</td><td>0.4394</td><td>0.4257</td><td>0</td><td>1</td></tr><tr><td>Cashback for driver $^{a}$ </td><td>1.4733</td><td>0.3625</td><td>0</td><td>1.5625</td></tr><tr><td>Cashback for passenger $^{a}$ </td><td>1.5843</td><td>0.6768</td><td>0</td><td>2.5000</td></tr><tr><td>Passenger bids $^{a}$ </td><td>0.0076</td><td>0.1531</td><td>0</td><td>7.8125</td></tr><tr><td>Platform subsidies $^{a}$ </td><td>0.0300</td><td>0.2149</td><td>0</td><td>15.6250</td></tr></table>

46 with those between day 65 and day 80 shows that, even though sales promotion policies for drivers and passengers are almost the same, and bids from passengers and subsidies from the platform are even higher during the earlier period, more orders are accepted and fulfilled with online pay after day 65. Quantitatively, a similar pattern can be observed by dividing the time horizon into three even periods and comparing the average outcomes, as shown in Table 2. A comparison of the middle 30 days with the last 30 days shows that all three outcome variables are improved, even with declining sales promotions and other rewards/subsidies.

A potential explanation for the improved outcome variables, after controlling for the sales promotion policies, is that the usage experience accumulated earlier led drivers to fully perceive the value of the app, converting them to frequent users, which we attribute to the learning effect. The descriptive analysis, however, is insufficient to identify the learning effects due to an alternative explanation, such as network growth; that is, the driver is more willing to use the app simply because he or she expects an increased number of passengers through its use. To fully reveal the learning effect and its interaction with sales promotions, we develop a structural model to identify the learning process with the network growth effect teased out.

## 4. Model

We present a structural model of the data-generation process of how a typical order on a TNC app is accepted, fulfilled, and completed following a request from a passenger. As discussed earlier, an order entails three stages of decisions:

Stage 1: The driver decides whether to accept the order.

Stage 2: The driver decides whether to cancel the accepted order.

Stage 3: The passenger decides whether to redeem the sales promotion by paying online.

Assume that the driver’s decision in Stage 1 is conditional on his or her belief in the decisions in Stages 2 and 3, and that the decision in Stage 2 is conditional on that in Stage 3. That is, the model needs to account for finite-horizon, forward-looking dynamics that incorporate the relationship among different stages with a decision-dependent state transition. We model these decisions in a forward way for easier interpretation but estimate the model by following typical backward induction. Specifically, we use a subscript a to represent the parameters associated with the decision to accept an order, subscript f to represent the parameters associated with fulfilling an accepted order, and subscript o to represent the parameters associated with redeeming a sales promotion

<sup>a</sup>Amount in USD.

Table 2. Change Over Time

<table><tr><td rowspan="2">Statistics</td><td colspan="4">Outcome</td><td colspan="4">Sales promotion and other rewards</td></tr><tr><td>No. orders</td><td>Accept</td><td>Fulfill/accept</td><td>Online pay/fulfill</td><td>Cashback for PSGRa</td><td>Cashback for drivera</td><td>Platform subsidya</td><td>PSGR bidsa</td></tr><tr><td>Overall</td><td>198,689</td><td>0.76</td><td>0.84</td><td>0.69</td><td>1.58</td><td>1.47</td><td>0.04</td><td>0.03</td></tr><tr><td>First 30 days</td><td>56,291</td><td>0.62</td><td>0.71</td><td>0.28</td><td>1.25</td><td>1.25</td><td>0.19</td><td>0.06</td></tr><tr><td>Mid 30 days</td><td>67,259</td><td>0.77</td><td>0.87</td><td>0.74</td><td>2.20</td><td>1.56</td><td>0.01</td><td>0.03</td></tr><tr><td>Last 30 days</td><td>704,430139</td><td>0.86</td><td>0.88</td><td>0.82</td><td>1.28</td><td>1.56</td><td>0</td><td>0.02</td></tr></table>

Note. PSGR, passenger.  
<sup>a</sup>Amount in USD.

to avoid potential confusion. We further define the arrival of each order as a one-time period.

## 4.1. Stage 1: Decision to Accept an Order

When an order arrives, the driver makes the decision about whether to use the TNC app to accept or to decline and chooses an alternative from traditional sources (e.g., telephone call, airport pickup, hotel pickup, passengers on the roadside). We assume that driver i at time t will receive a utility of $u _ { a i 1 t }$ if he or she accepts an order from the TNC app, and $u _ { a i 0 t }$ if not.

The utility of accepting an order, $u _ { a i 1 t } ,$ consists of two parts. The first part includes the utility value that will be received by a driver, regardless of what the driver does in later stages. This part considers the driver’s utility from the attribute of using the app to match with passenger(s), as it reduces the spatial imbalance of passengers. We use an attribute value, $A _ { a } ,$ to represent the intrinsic latent utility value of using the app to match with passenger(s) and term it an attribute value for matching. The utility of using the app to match also might depend on the available passengers on the app. Therefore, we also include the size of the passenger network, $N _ { t } .$ . Because we separate the passenger network size from the attribute value of matching to make the attribute value of matching not a function of the passenger network size, the attribute value of matching could be constant. A driver who accepts an order from the app will always benefit from using the app to match passengers and from a larger passenger network size regardless of whether the order is fulfilled or canceled later on because the matching has already occurred by that time. The first part, thus, does not depend on Stage 2.

The second part further considers two possible utility flows at Stage 2 after a driver accepts an order from the app. If the driver, later on, is committed to the accepted order, the transaction will be fulfilled, and the driver will gain utility $u _ { f i 1 t . }$ , including fare, bids, subsidy, and sales promotion, less the cost. In contrast, if the driver cancels the accepted order later on, he or she will gain utility $u _ { f i 0 t }$ . The rationality assumption indicates that drivers will always choose the best alternative in the later stage. Thus, this part is equal to the higher value between $u _ { f i 1 t }$ and $u _ { f i 0 t }$

We use an additive linear form with scalars for the first part and a maximum function to specify the utility of accepting an order as

$$
u _ {a i 1 t} = \beta_ {a i 1} A _ {a} + \beta_ {a i 2} N _ {t} + \max \left(u _ {f i 1 t}, u _ {f i 0 t}\right) + \varepsilon_ {a i 1 t},\tag{1}
$$

where $\beta _ { a i 1 }$ and $\beta _ { a i 2 }$ represent the weight of utility from the attribute value for matching and that from the passenger network size; and $\varepsilon _ { a i 1 t }$ captures unobserved information by econometricians, which is assumed to follow a type-I extreme value distribution.<sup>1</sup>

A driver could decide not to accept an order when he or she receives a higher utility from outside goods. We assume the utility of outside goods $u _ { a i 0 t }$ to be the summation of constant expected level $c _ { a i 0 }$ plus a stochastic error term that captures unobserved utilities:

$$
\mathcal {U} _ {a i 0 t} = c _ {a i 0} + \varepsilon_ {a i 0 t}.\tag{2}
$$

Given that the TNC platform has recently been introduced to the market, and that the cancellation and online-pay decisions happen after an acceptance, drivers are not initially fully certain about the latent utility. Therefore, before a driver makes the decision of whether to use the app to receive orders, he or she first forms an expectation of the utility from two alternatives, based on the information updated to period $t ,$ and chooses the alternative that maximizes his or her expected utility. The major source of information that drivers use to improve their perception of utility is their own usage experience, which provides more precise information than do other channels. We define information set $I _ { i t }$ as the cumulative usage experience and make the expectation of latent utility conditional on $I _ { i t }$ for the two alternatives:

$$
E (u _ {a i 1 t} | I _ {i t}) = \beta_ {a i 1} E (A _ {a} | I _ {i t}) + \beta_ {a i 2} E (N _ {t} | I _ {i t})
$$

$$
+ E \bigl (\max \bigl (u _ {f i 1 t}, u _ {f i 0 t} \bigr) | I _ {i t} \bigr) + \varepsilon_ {a i 1 t},\tag{3}
$$

$$
E (u _ {a i 0 t} | I _ {i t}) = c _ {a i 0} + \varepsilon_ {a i 0 t}.\tag{4}
$$

Because a driver does not have perfect information about the passenger network size, we use the number of orders received by a driver on the last day $x _ { i t } ^ { n s }$ to approximate the driver’s perceived network size $E ( N _ { t } | I _ { i t } )$ . A driver also is uncertain about the expected attribute value of matching $E ( A _ { a } | I _ { i t } )$ and the expected utility flow from Stage $2 \bar { E ( \operatorname* { m a x } ( u _ { f i 1 t } , u _ { f i 0 t } ) | I _ { i t } ) }$ For these two terms, we assume that drivers behave as Bayesian learners who update their expectations based on $I _ { i t }$ . Specifically, because drivers might get involved in three sequential decisions and receive usage experience from each, we let drivers update specific decisions based on the usage experience of a corresponding decision before time t. Therefore, $E ( \operatorname* { m a x } ( u _ { f i 1 t } ^ { - } , u _ { f i 0 t } ) \bar { | } _ { t _ { i t } } )$ is updated with Stage 2, which will be specified in later sections (Equation (16)). $E ( A _ { a } | I _ { i t } )$ is updated with the Stage 1 decision that drivers experience from the beginning to time t.

We explicitly explain how $E ( A _ { a } | I _ { i t } )$ is formed through a Bayesian learning process. We assume that, before starting to use the app to accept orders, drivers have prior information about the attribute of accepting orders from the app. We model the prior information, following $N ( \hat { A } _ { a 0 } , \sigma _ { a 0 } ^ { 2 } ) .$ , to accommodate a potentially biased prior belief $A _ { a 0 }$ and drivers’ uncertainty $\sigma _ { a 0 } ^ { 2 } .$ We assume that drivers make first-time decisions based on prior information only, such that first-time attribute $A _ { a }$ is drawn from a prior distribution $N ( A _ { a 0 } , \sigma _ { a 0 } ^ { 2 } )$ . By defining $\sigma _ { A _ { a } i 0 } ^ { 2 }$ as the variance of driver i’s perception of the mean attribute level at the very beginning, we have

$$
\begin{array}{c} E (A _ {a} | I _ {i 0}) = A _ {a 0}, \text { and } \\ \sigma_ {A _ {a} i 0} ^ {2} = \operatorname{Var} (A _ {a} | I _ {i 0}) = E \Big ((A _ {a} - A _ {a 0}) ^ {2} | I _ {i 0} \Big) = \sigma_ {a 0} ^ {2}. \end{array}\tag{5}
$$

We assume that drivers update their beliefs about attribute value and uncertainty when they receive signals, and that such signals, with some noise, are drivers’ own usage experience by which they can perceive the true attribute value of matching. The noise can be derived from the variability of the true attribute value itself or the variability associated with specific context in usage experience. To make the Bayesian update conjugate, we assume that the signal of the app’s true attribute value, denoted as $A _ { a i t } ^ { e } ,$ follows a normal distribution according to

$$
A _ {a i t} ^ {e} \sim N \left(A _ {a 1}, \sigma_ {a 1} ^ {2}\right),\tag{6}
$$

where $A _ { a 1 }$ is the mean of the signal that equals the true attribute value, and $\sigma _ { a 1 } ^ { 2 }$ captures the variance of the signal.

We assume that drivers update if they receive one more usage experience or, if not, stay with the initial perception.

Specifically, when drivers experience use the app to take an order at time t 1, they update their perception as a weighted average of the perception formed in the last time period $E ( A _ { a } | I _ { i ( t - 1 ) } )$ and the newly received signal $A _ { i a ( t - 1 ) } ^ { e }$ . To be consistent with the intuition that a more precise signal leads a driver’s perception to be closer to the true attribute value, we assume the weights as precision parameters, using the inverse of perception variance and that of the signal, according to

$$
\begin{array}{c} E (A _ {a} | I _ {i t}) = D _ {a i t} \times \frac {\frac {A _ {a i (t - 1)} ^ {e}}{\sigma_ {a 1} ^ {2}} + \frac {E (A _ {a} | I _ {i (t - 1)})}{\sigma_ {A _ {a} i (t - 1)} ^ {2}}}{\frac {1}{\sigma_ {a 1} ^ {2}} + \frac {1}{\sigma_ {A _ {a} i (t - 1)} ^ {2}}} \\ + (1 - D _ {a i t}) \times E (A _ {a} | I _ {i (t - 1)}), \end{array}\tag{7}
$$

$$
\sigma_ {A _ {a} i t} ^ {2} = D _ {a i t} \times \frac {1}{\frac {1}{\sigma_ {a 1} ^ {2}} + \frac {1}{\sigma_ {A _ {a} i (t - 1)} ^ {2}}} + (1 - D _ {a i t}) \times \sigma_ {A _ {a} i (t - 1)} ^ {2},\tag{8}
$$

where $D _ { a i t }$ is a dummy indicator function that in dicates whether the driver accepts an app order (= 1) or not $( = 0 )$ . Posterior uncertainty is updated as the inverse of the sum of the inverse of prior uncertainty and the inverse of signal variance if the signal is received. The Bayesian updating rule above (Equations (7) and (8)) exhibits diminishing uncertainty with gaining usage experience and increasingly diminishing uncertainty with gaining less noisy signals in usage experience.

When $E ( \operatorname* { m a x } ( u _ { f i 1 t } , u _ { f i 0 t } ) | I _ { i t } )$ is formed, and assuming that the error terms $\varepsilon _ { a i 0 t }$ and $\varepsilon _ { a i 1 t }$ are independently and identically distributed with type-I extreme distribution, we obtain the probability that a driver accepts an order from the TNC app conditional on information $I _ { i t }$ and the Stage 1 individual’s likelihood function as follows:

$$
\begin{array}{l} \operatorname * {P r} (D _ {a i t} | I _ {i t}) \\ = \frac {\exp \big (\beta_ {a i 1} E (A _ {a} | I _ {i t}) + \beta_ {a i 2} x _ {i t} ^ {n s} + E \big (\max \big (u _ {f i 1 t} , u _ {f i 0 t} \big) | I _ {i t} \big) \big)}{\exp \big (\beta_ {a i 1} E (A _ {a} | I _ {i t}) + \beta_ {a i 2} x _ {i t} ^ {n s} + E \big (\max \big (u _ {f i 1 t} , u _ {f i 0 t} \big) | I _ {i t} \big) \big)} \\ \qquad + \exp (c _ {a i 0}), \end{array}\tag{9}
$$

$$
L _ {a i} \Big (\beta_ {a i}, \beta_ {f i}, \beta_ {o i} \Big) = \prod_ {t = 1} ^ {T _ {i}} \Big (\operatorname * {P r} (D _ {a i t} | I _ {i t}) ^ {D _ {a i t}} \cdot (1 - \operatorname * {P r} (D _ {a i t} | I _ {i t})) ^ {1 - D _ {a i t}} \Big),\tag{10}
$$

$$
\mathrm{where} \beta_ {a i} = \{A _ {a 0}, \sigma_ {a 0} ^ {2}, A _ {a 1}, \sigma_ {a 1} ^ {2}, \log (\beta_ {a i 1}), \beta_ {a i 2}, c _ {a i 0} \}.
$$

4.2. Stage 2: Decision to Ful<sup>fi</sup>ll or Cancel an Order For an accepted order from the TNC app, a driver could further decide to cancel based on more information received after the accepting decision.

This decision is governed by the expectation of the latent utility if the driver fulfills the accepted order from the TNC app $u _ { f i 1 t } ,$ and that if the driver cancels the previously accepted order $u _ { f i 0 t }$

If a driver fulfills the accepted order from the TNC app, he or she would receive a cashback bonus $x _ { i t } ^ { c b }$ and costs associated with online pay $c _ { f i 1 }$ if the passenger uses online pay, such as the loss of instant gratification, passenger bids $x _ { i t } ^ { b i d } .$ , platform driver subsidy $x _ { i t } ^ { s u b } .$ , an initially uncertain attribute value of fulfilling (not canceling) $A _ { f } ,$ and a random utility value $\varepsilon _ { f i 1 t } .$ Otherwise, the driver would have a cost associated with canceling the order, including a deterministic average cost $c _ { f i 0 }$ and a random term $\varepsilon _ { f i 0 t }$ . Terms $\varepsilon _ { f i 1 t }$ and ε<sub>fi0t</sub> capture the additional unobserved information that occurs during the time lag between Stages 1 and 2 (e.g., road conditions/congestion, accidents on the way to pick up the passenger(s), difficulty in finding the pickup location, and/or an incoming high-value offline order). Using a linear additive form, we specify the latent utility of fulfilling or canceling the order after its acceptance as

$$
u _ {f i 1 t} = \beta_ {f i 1} A _ {s} + \beta_ {f i 2} x _ {i t} ^ {s u b} + \beta_ {s 3} x _ {i t} ^ {b i d}
$$

$$
+ D _ {o i t} \left(\beta_ {f i 4} x _ {i t} ^ {c b} + c _ {f i 1}\right) + \varepsilon_ {f i 1 t},\tag{11}
$$

$$
u _ {f i 0 t} = c _ {f i 0} + \varepsilon_ {f i 0 t},\tag{12}
$$

where $D _ { o i t }$ is an indicator function that indicates whether online pay is used (= 1) or not $( = 0 )$ . Only when online pay is used can the driver gain a cashback bonus from the platform while incurring a transaction cost. Terms $\beta _ { f i 1 } , \beta _ { f i 2 } , \beta _ { f i 3 } ,$ and $\beta _ { f i 4 }$ are the weights for the attribute value of fulfilling, a platform subsidy, a revealed bid from a passenger, and onlinepay-contingent cashback in the utility function, respectively. We give different weights to different formats of monetary rewards because we suspect that a revealed bid, as well as a subsidy, might play an additional role of signaling the quality of an order that might affect the cancellation decision. We conjecture that a high bid might convey extra information from a passenger, such as potential extra cost, because the bid might indicate that a sole flat rate netting of the cost is not as competitive as that in alternative orders for drivers. Similarly, an order-specific subsidy from the platform also might convey the information known by the platform, whereas such an effect does not exist for a cashback bonus.

Because the fulfilling/cancellation function has been recently introduced, drivers are uncertain about how this function works and are concerned that they might overact or underact in regard to canceling orders. To rationalize our model, we assume that a driver will form the expectation of latent utility conditional on the information up to time t to make the decision to fulfill or cancel an order. Given that monetary rewards are revealed precisely before the decision, all of the uncertainties in latent utility stem from $A _ { f } ,$ , as an attribute value of fulfilling (not canceling) an accepted order that is most likely to be uncertain for drivers, as well as $D _ { o i t }$ , which captures the uncertainty level associated with a next-stage decision. Accordingly, the expected utility conditional on information set $I _ { i t }$ is given by

$$
\begin{array}{r l} & E \big (u _ {f i 1 t} | I _ {i t} \big) = \beta_ {f i 1} E \big (A _ {f} | I _ {i t} \big) + \beta_ {f i 2} x _ {i t} ^ {s u b} + \beta_ {f i 3} x _ {i t} ^ {b i d} \\ & \qquad + \operatorname * {P r} (D _ {o i t} | I _ {i t}) \Big (\beta_ {f i 4} x _ {i t} ^ {c b} + c _ {f i 1} \Big) + \varepsilon_ {f i 1 t}, \end{array}
$$

$$
E \big (u _ {f i 0 t} | I _ {i t} \big) = c _ {f i 0} + \varepsilon_ {f i 0 t}.\tag{13}
$$

(14)

Drivers need to form beliefs about $A _ { f }$ through their experiences. Similar to the model of the perceived attribute value of accepting orders from the app, we assume that these learning processes follow the Bayesian updating rule, with the prior perceived value as following $N ( A _ { f 0 } , \sigma _ { f 0 } ^ { 2 } )$ and the signal as following $N ( A _ { f 1 } , \sigma _ { f 1 } ^ { 2 } )$ . We suppress the updating rules here for a concise interpretation and let $\bar { E ( A _ { f } , I _ { i t } ) }$ represent the Bayesian-updated driver’s belief of perceived attribute value for fulfilling an order at time t. In addition, drivers form beliefs about passengers willingness to use online pay as $\mathrm { P r } ( D _ { o i t } | I _ { i t } )$ , conditional on usage experience until time t by following the rule seen in Stage 3.

We assume that the error term follows type-I extreme value distribution, which results in a closedform logit formula for the probability of fulfilling an order and the expectation of the maximum of utility in Stage 2, conditional on the information set. We present the probability of fulfilling an order and the expectation of the maximum of utility in Stage 2 as follows:

$$
\operatorname * {P r} (D _ {o i t} | I _ {i t}) = \frac {\exp \left(\overline {{E (u _ {f i 1 t} | I _ {i t})}}\right)}{\exp \left(\overline {{E (u _ {f i 1 t} | I _ {i t})}}\right) + \exp \left(c _ {f i 0}\right)},\tag{15}
$$

$$
\begin{array}{c} E \bigl (\max (u _ {f i 1 t}, u _ {f i 0 t}) | I _ {i t} \bigr) = \gamma + \log \Bigl (\exp \Bigl (\overline {{E (u _ {f i 1 t} | I _ {i t})}} \Bigr) \\ + \exp \bigl (c _ {f i 0} \bigr) \Bigr), \end{array}\tag{16}
$$

where $\overline { { { E ( u _ { f i 1 t } | I _ { i t } ) } } } ~ = ~ \beta _ { f i 1 } E ( A _ { f } | I _ { i t } ) ~ + ~ \beta _ { f i 2 } x _ { i t } ^ { s u b } ~ + ~ \beta _ { f i 3 } x _ { i t } ^ { b i d } ~ + ~$ $\mathrm { P r } ( { \cal D } _ { o i t } | I _ { i t } ) ( \beta _ { f i 4 } x _ { i t } ^ { c b } ~ + ~ c _ { f i 1 } ^ { ' } )$ , and γ is the Euler-Mascheroni constant. The Stage 2 individual’s likelihood function is

$$
L _ {f i} \left(\beta_ {f i}, \beta_ {o i}\right) = \prod_ {t = 1} ^ {T _ {a i}} \left(\operatorname * {P r} \left(D _ {f i t} \mid I _ {i t}\right) ^ {D _ {f i t}} \cdot \left(1 - \operatorname * {P r} \left(D _ {f i t} \mid I _ {i t}\right)\right) ^ {1 - D _ {f i t}}\right),\tag{17}
$$

where $\beta _ { f i } = \{ A _ { f 0 } , A _ { f 1 } \log ( \sigma _ { f 0 } ^ { 2 } ) , \log ( \beta _ { f i 1 } ) , \beta _ { f i 2 } , \beta _ { f i 3 } , \beta _ { f i 4 } , c _ { f i 1 } , c _ { f i 0 } \}$

## 4.3. Stage 3: Passenger Decision to Use Online Pay and Redeem a Sales Promotion

Conditional on an order’s being fulfilled, the passenger makes the decision of whether to use online pay for taxi fare. Given that the online-pay function was recently introduced to passengers, the entire population of passengers can be considered Bayesian learners, especially from drivers’ perspectives. Similarly, through learning that is accelerated by the cashback policy, the perceived online-pay attribute value evolves dynamically and eventually converges to a stationary level from a biased starting value.

Given that online pay could potentially lead to a cashback bonus from the platform, drivers calculate their expected utilities in Stage 2 and, thus, Stage 1, with the expectation of the order being paid online. Different from learning from their own experiences of using a function of the app in Stages 1 and 2, in Stage 3, drivers form their beliefs about receiving an onlinepaid order through interactions with passengers. In other words, a driver’s perception of the probability of online pay reflects the aggregate usage pattern of all of his or her passengers. Following the literature on dynamic decision/choice in turbulent markets (Erdem and Keane 1996, Crawford and Shum 2005, Erdem et al. 2008, Chen et al. 2009, Huang et al. 2014), we assume that drivers could learn from their experience of passengers using online pay and, thus, form their beliefs about passengers’ decisions to use online pay.

To form his or her belief about the probability of online pay, a rational driver formulates a representative passenger’s decision problem. Because passengers will gain cashback if they use the onlinepay feature, it is known to the driver that the passenger’s decision of using online pay is governed by passenger-side sales promotion $x _ { i t } ^ { \bar { p } c b } .$ , the attribute value of using online-pay function $A _ { o } ,$ , and unobserved online-pay utility $\varepsilon _ { o i 1 t }$ . We assume that these components constitute a representative passenger’s latent utility function of using online pay, following a linear additive form, with $\beta _ { o i 1 }$ and $\beta _ { o i 2 }$ as the corresponding weights in driver $i ^ { \prime } \mathrm { s }$ belief. The utility from outside alternative payment methods, such as cash or a prepaid metro card, is specified as a driver’s expected average value $c _ { o i 0 }$ plus unobserved variation from the average $\varepsilon _ { o i 0 t }$ . Type-I extreme distributed error terms are assumed for $\varepsilon _ { o i 1 t }$ and $\varepsilon _ { o i 0 t }$ . Accordingly, the utility functions of taking online pay and alternative pay are given by

$$
u _ {o i 1 t} = \beta_ {o i 1} A _ {o} + \beta_ {o i 2} x _ {i t} ^ {p c b} + \varepsilon_ {o i 1 t},\tag{18}
$$

$$
u _ {o i 0 t} = c _ {o i 0} + \varepsilon_ {o i 0 t}.\tag{19}
$$

Similarly, the expected utility and, hence, a driver’s belief in the probability of receiving an online-paid order conditional on time information set $I _ { i t }$ are

$$
E (u _ {o i 1 t} | I _ {i t}) = \beta_ {o i 1} E (A _ {o} | I _ {i t}) + \beta_ {o i 2} x _ {i t} ^ {p c b} + \varepsilon_ {o i 1 t},\tag{20}
$$

$$
E (u _ {o i 0 t} | I _ {i t}) = c _ {o i 0} + \varepsilon_ {o i 0 t},\tag{21}
$$

$$
\operatorname * {P r} (D _ {o i t} | I _ {i t}) = \frac {\exp \left(\beta_ {o i 1} E (A _ {o} | I _ {i t}) + \beta_ {o i 2} x _ {i t} ^ {p c b}\right)}{\exp \left(\beta_ {o i 1} E (A _ {o} | I _ {i t}) + \beta_ {o i 2} x _ {i t} ^ {p c b}\right) + \exp (c _ {o i 0})}.\tag{22}
$$

The perceived attribute value of online pay, $A _ { o } ,$ is uncertain and needs to be learned by drivers. We model that drivers’ prior beliefs of the attribute follow $N ( A _ { o 0 } , \sigma _ { o 0 } ^ { 2 } )$ , and that the received signal about the attribute follows $N ( A _ { o 1 } , \sigma _ { o 1 } ^ { 2 } )$ . We assume that every time a driver fulfills an order and the passenger uses online pay for the fare, the driver’s perception of this attribute is updated following the Bayesian rule, similar to what is described for Stage 1. Given the assumption that drivers could form consistent beliefs about passengers using online pay based on their learning, we can maximize the following likelihood function to rationalize the parameters in driver i’s belief:

$$
L _ {o i} \big (\beta_ {o i} \big) = \prod_ {t = 1} ^ {T _ {f i}} \Bigl (\operatorname * {P r} (D _ {o i t} | I _ {i t}) ^ {D _ {o i t}} \cdot (1 - \operatorname * {P r} (D _ {o i t} | I _ {i t})) ^ {1 - D _ {o i t}} \Bigr),\tag{23}
$$

$$
\mathrm{where} \beta_ {o i} = \{A _ {o 0}, A _ {o 1}, \sigma_ {o 0} ^ {2}, \sigma_ {o 1} ^ {2}, \log (\beta_ {o i 1}), \beta_ {o i 2}, c _ {o i 0} \}.
$$

## 4.4. Stage Dependency and Heterogeneity

Throughout, the model is specified as though all of the errors in the various stages are independent of one another, and hence, each stage can be estimated separately. This assumption is relaxed through the use of the latent-class approach (Kamakura and Russel 1989), following Arcidiacono (2005), through which the parameters in different stages can now be correlated. The various stages are connected through an individual’s latent class, controlling for the dynamic selection that occurs in the model. These latent classes affect the parameters and intercepts in each stage of the estimation and the expectations on future utility (Arcidiacono 2005). For example, latent classes correlate the intercept in Stage 1 with that in Stage 2. A positive correlation, if identified, implies that an order that is more likely to be accepted will further be more likely to be fulfilled, whereas others are more likely to be canceled. Therefore, the latent-class approach further builds unobserved stage dependency by allowing the unobserved preference to be correlated over different stages, in addition to the observed stage dependency, by incorporating forward-looking behavior; that is, we expect $\mathrm { P r } ( { \bar { D } } _ { o i t } | I _ { i t } )$ in Stage 2 and $E ( \operatorname* { m a x } ( u _ { f i 1 t } , u _ { f i 0 t } ) | I _ { i t } )$ in Stage 1.

Notably, the latent-class approach also identifies and controls the unobserved heterogeneity of drivers. Even though other approaches (e.g., random coefficients) might control unobserved heterogeneity better, the advantage of relaxing the stage-independence assumption cannot be easily obtained by alternative methods. We therefore use latent class to control for unobserved stage dependency and heterogeneity. Specifically, we assume there are $m = 1 , 2 , \ldots , M$ latent classes, and that each individual driver i has a probability $0 \leq \pi ( m ) \leq 1$ of belonging to class m. Latent classes remain the same throughout all stages, individuals know their type, and preferences sensitivity $( \beta _ { a } , \beta _ { s } , \beta _ { p } )$ may vary across latent classes. The loglikelihood function for all of the observations then follows:

$$
\begin{array}{c} \operatorname{Log} L \left(\beta_ {a m}, \beta_ {f m}, \beta_ {o m}\right) = \sum_ {i = 1} ^ {I} \log \left(\sum_ {m = 1} ^ {M} \pi (m) \cdot L _ {o i} \left(\beta_ {o m}\right) \right. \\ \left. \cdot L _ {f i} \left(\beta_ {f m}, \beta_ {o m}\right) \cdot L _ {a i} \left(\beta_ {a m}, \beta_ {f m}, \beta_ {o m}\right)\right). \end{array}\tag{24}
$$

## 4.5. Identi<sup>fi</sup>cation and Endogeneity

We briefly discuss the identification of our model in two steps. In the first step, we explain the identification of a typical Bayesian learning process, following Crawford and Shum (2005). In the second step, we explain the identification of our full model.

There are three sets of parameters in a typical Bayesian learning model for discrete choice, with only one uncertain attribute value. The first and most intuitive one includes the coefficients associated with exogenous variables, such as coefficients for sales promotions in our study. These coefficients are identified by the variation of variables associated with them. The second set of variables includes true attribute value, prior attribute value, and constant terms in each Bayesian updating process, among which only two can be identified, as only the difference matters in a discrete-choice model. Our learning pattern allows identification of the difference between prior and true value from the difference of decisions between earlier and later stages. In other words, the variation of different decisions and variation along time allow us to identify two parameters. Because we are more interested in the difference between true and prior attribute value and whether the true attribute value is higher or lower than the constant value, we normalize the true attribute value to 0 and leave the prior attribute value and constant with freedom. This is also the most computationally effective way for minimization of an algorithm.

The third set of parameters includes prior variance and true variance of attributes for each Bayesian learning process, such as $\sigma _ { a 0 } ^ { 2 }$ and $\sigma _ { a 1 } ^ { 2 } , \sigma _ { f 0 } ^ { 2 }$ and $\sigma _ { f 1 } ^ { 2 } .$ , and $\sigma _ { o 0 } ^ { 2 }$ and $\hat { \sigma } _ { o 1 } ^ { 2 }$ . We are allowed to identify only one for prior variance and true variance in each Bayesian updating because only the relative difference between those two variance parameters matters. Given a fixed prior mean value as the starting point and a fixed true mean value as the converged end point, the latent utility still has freedom in the speed of con vergence as well as with regard to the time dimension. This convergence rate can be visualized as a curvature along the time series and identifies relative variance between prior variance and posterior variance. In our model, we normalize true value variance parameters as 1 and identify the prior variance parameters to investigate the uncertainty levels of attributes before any usage experience.

The identification for the full model is straightforward, following our discussion in the previous paragraph about identification for Bayesian learning. Given the observations of three sequential decisions as drivers’ decisions to accept orders, drivers’ decisions to fulfill orders, and passengers’ decisions to pay online in drivers’ perceptions, we can identify the Bayesian-updating-associated parameters $A _ { a 0 } , \sigma _ { a 1 } ^ { 2 } .$ $A _ { f 0 } , \ \sigma _ { f 1 } ^ { 2 } , \ A _ { o 0 } ,$ , and $\textstyle | \sigma _ { o 1 } ^ { 2 }$ from the difference of latent perceived attributes between earlier time points and later time points and the curvature of perceived attributes for each of the decisions.

Other parameters are components in a mixed generalized linear formula, which follows typical identification rules of latent-class discrete-choice models. The $c _ { f m 1 } \mathrm { c o u l d }$ be treated as the coefficient for $\mathrm { P r } ( D _ { o i t } | I _ { i t } )$ Because all of the variables, including $\mathrm { P r } ( D _ { o i t } | I _ { i t } ) .$ , have enough variation across individuals and across time periods within an individual, the associated parameters could be identified in a latent-class manner. Not that the Bayesian learning process has used $\sigma _ { a 0 } ^ { 2 } , \sigma _ { f 0 } ^ { 2 } ,$ and $\sigma _ { o 0 } ^ { 2 }$ to account for the heterogeneity of perceived attributes and their learning updates, and that the weights for attributes $\beta _ { a m 1 } , \ \beta _ { f m 1 } ,$ , and $\beta _ { o m 1 }$ must be positive to avoid “mirrored” estimates. We model the weights for attributes that are constant across latent classes and take a log transformation to enter the model as $\log ( \beta _ { a 1 } )$ , $\log ( \beta _ { f 1 } )$ , and $\log ( \beta _ { o 1 } )$

One potential concern about the identification is the endogeneity of $x _ { i t } ^ { b i d }$ , as a passenger might offer a bid due to the unobserved quality $\varepsilon _ { f i 1 t } \ ( \mathrm { e . g . } $ , the pickup location is far or difficult to reach). To address this concern, we follow Berry et al. (1995) to apply measures of isolation in product space as instrumental variables (IVs) to calculate the average bid amount received by other drivers on the same day. Note that, in a discrete context, the common factors that affect all of the choices (e.g., weather, time) would be canceled out, and only choice-specific factor(s) will remain in the associated error term. The IV, thus, is unlikely to be affected by/correlated with the unobserved quality of a specific order received by driver $I , \varepsilon _ { f i 1 t } ,$ , but shows a high degree of variation and correlation with $x _ { i t } ^ { b i d }$ Given the nonlinear nature of our model, we apply a control function approach (Heckman and Robb 1985) to estimate our model, which fundamentally adds an instrument-generated control variable in Equations (14) and (16) to correct the bias.

## 4.6. Estimation Speci<sup>fi</sup>cation

We follow Arcidiacono (2005) to use the expectationmaximization (EM) algorithm to recover parameters. In particular, we specify the expected log likelihood and the conditional probability of being the mth type as

$$
\begin{array}{l} \sum_ {i = 1} ^ {I} \sum_ {m = 1} ^ {M} P _ {i} (m) \cdot \left(\log \left(L _ {o i} (\beta_ {o m})\right) + \log \left(L _ {f i} (\beta_ {f m}, \beta_ {o m})\right) \right. \\ \left. + \log \left(L _ {a i} (\beta_ {a m}, \beta_ {f m}, \beta_ {o m})\right)\right), \\ P _ {i} (m) = \frac {\pi (m) \cdot L _ {o i} (\beta_ {o m}) \cdot L _ {f i} (\beta_ {f m} , \beta_ {o m}) \cdot L _ {a i} (\beta_ {a m} , \beta_ {f m} , \beta_ {o m})}{\sum_ {m = 1} ^ {M} \pi (m) \cdot L _ {o i} (\beta_ {o m}) \cdot L _ {f i} (\beta_ {f m} , \beta_ {o m}) \cdot L _ {a i} (\beta_ {a m} , \beta_ {f m} , \beta_ {o m})}. \end{array} \tag {25}\tag{26}
$$

At step E, we calculate the expected log-likelihood function and update $P _ { i } ( m )$ at the current parameter estimates. At step M, we maximize the expected loglikelihood function, holding $P _ { i } ( m )$ fixed. In particular, given the additive separability of the expected log likelihood, at step $M ,$ for each $m ,$ we (a) maximize $\Sigma _ { i } \log ( L _ { o i } ( \beta _ { o m } ) ) \hat { P _ { i } } ( m )$ to estimate $\beta _ { o m } , ~ ( \mathrm { b } )$ maximize $\Sigma _ { i } \log L _ { f i } ( \beta _ { f m } , \overleftrightarrow { \beta } _ { o m } ) P _ { i } ( m )$ with the given estimate of $\beta _ { o m }$ to estimate $\beta _ { f m } ,$ and (c) maximize $\Sigma _ { i } \log ( L _ { a i } ( \beta _ { a m } ,$ $\beta _ { f m } , \beta _ { o m } ) ) P _ { i } ( m )$ with the given estimates of $\beta _ { f m } , \beta _ { o m }$ to estimate $\beta _ { a m } .$ The updated $\log L _ { o i } ( \beta _ { o m } )$ $\log L _ { f i } ( \beta _ { f m } , \beta _ { o m } ) ,$ and $\log { L _ { a i } ( \bar { \beta } _ { a m } , \beta _ { f m } , \bar { \beta } _ { o m } ) }$ further update $P _ { i } ( \dot { m } )$ at step E of the next iteration. The π m is given by the average of $P _ { i } ( m )$

Step M (a) is similar to estimating a typical Bayesian learning model. We use the maximum simulated likelihood method proposed by Erdem and Keane (1996), with the attribute perception as simulated and the variance as integrated numerically; if an order is canceled, there will be no online pay or corresponding learning, so we only need the data for which the Stage 2 decision is to fulfill the order.

More challenges occur in step M (b) and (c). When forming the log likelihood, we need to update learning for not only the current stage attribute but also the later stage ones, as the later stage attributes are conditional on the current stage decision. For example, the decision to take outside goods in the current stage not only prohibits learning for the current stage attribute but also limits it for the next stage. This sequential and conditional decision and learning process naturally leads to a forward simulation-based method for drawing decisions sequentially to form the likelihood. In particular, note that, according to the backward induction in the EM specification, the parameters for later stage(s) are known when we estimate the parameters in step M (b) and (c). In each time period, we use the known parameters to simulate the later stage choice(s)/outcome(s), sequentially con ditional on the observed current stage choice, and update all stages’ perceived attribute values accordingly. The updated perceived attribute values, along with the known parameters, are used to simulate the choice(s)/outcome(s) in the next transaction/time period, conditional on that transaction’s observed current stage choice. We keep this loop through each time period. Similar to Erdem and Keane (1996), we numerically integrate perceived uncertainty by simulating many times for each individual and form a numerically integrated likelihood function.

## 5. Estimation Results

## 5.1. Model Fit and Comparison

In Table 3, we report and compare the model fit statistics. The first model is a myopic model that assumes that individuals make decisions of acceptance and cancellation independently, rather than sequentially with forwardlooking. Compared with the proposed model, this model ignores the expected learning and utility flow from Stage 2 at Stage 1. The second model adds forwardlooking of cancellation but no heterogeneous preference. The third model uses random parameters to substitute the latent-class parameters to control for heterogeneity. Compared with the proposed model, this model assumes Gaussian-distributed sensitivity parameters instead of a latent and discrete class distribution. In addition, it does not allow the unobserved stage dependency because the unobserved preference cannot be correlated over different stages. The fourth model is our proposed model. Because model-fitting statistics show that the two latent classes fit the data best for all four competing models, we report only the two-segment results for our proposed model. Our proposed model outperforms the three inferior models without forward-looking, unobserved heterogeneity, and/or unobserved stage dependency, which implies the importance of allowing for forwardlooking, unobserved heterogeneity, and unobserved stage dependency. The pseudo $R ^ { 2 }$ of our proposed model is in the range of 0.2–0.4, which is interpreted as excellent fit (McFadden 1978).

Table 3. Model Comparison

<table><tr><td rowspan="3"></td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td colspan="2">Model 4</td></tr><tr><td rowspan="2">Without forward-looking (2 seg)</td><td rowspan="2">Without unobserved heterogeneity (1 seg)</td><td rowspan="2">Random parameters</td><td colspan="2">Proposed model</td></tr><tr><td>2 seg</td><td>3 seg</td></tr><tr><td>-LL</td><td>182,396.9</td><td>182,852.9</td><td>181,829.7</td><td>181,489.3</td><td>181,435.7</td></tr><tr><td>BIC</td><td>182,573.2</td><td>182,976.2</td><td>182,012.8</td><td>181,678.9</td><td>181,690.7</td></tr></table>

Notes. seg, segment; -LL, log likelihood; BIC, Bayesian information criterion. Bold represents the minimal value of BIC.

To visualize the goodness of fit, we plot the average probability of decisions over different individuals for a specific cumulative number of transactions in Figure 3, where the grey dots indicate the nonparametric averages from our data, and the black ones represent predictive values from our parametric model. The y axes in the Figure 3 charts represent the probability that drivers accept orders, that orders are fulfilled, and that passengers pay online for fulfilled orders. The nonparametric results in our charts show general ascending and concave patterns for all of those probabilities, which indicate that individuals undervalue TNC app–associated features at the beginning but gradually learn and use them more frequently with the accumulation of usage experience. By checking the fitness of the black dots, we find that our mode recovers a learning pattern by a smooth concave and increasing function, which, in general, fits very well, except at the two tails, where the data are too sparse.

## 5.2. Estimation Results

In this section, we present the estimation results and insights associated with the estimates. We present the results in the same order as seen in our model, starting from the decisions of drivers and followed by the drivers’ beliefs about passengers’ decisions to use online pay. All point estimates as well as standard errors are presented in Table 4. In addition, we show the latent learning process by explicitly displaying the updated perceived attributes and updated perceived variance parameters of the three decisions to help to understand the learning process. The attribute values are simulated based on estimated parameters and are shown in Figure 4.

5.2.1. Stage 1. Note that in our forward-looking dynamic model, drivers’ expectations of Stage 2 utility affect their Stage 1 decision. Driver cashback, passenger cashback, passenger bids, and platform sub sidy thus could affect drivers’ Stage 1 decision indirectly through the expectation of Stage 2 utility functions. Given the model structure, the effect of driver cashback, passenger cashback, passenger bids, and platform subsidy on the Stage 1 decision should be consistent with that of Stage 2 qualitatively. Therefore, we omit the repeated qualitative interpretation, which is more extensively discussed in the Stage 2 results, and estimate only the promotion elasticities of a driver’s likelihood of accepting an order to highlight the quantitative findings. We show that a one-standarddeviation increase in driver cashback, platform subsidy, passenger bid, and passenger cashback, on average, would increase the probability of accepting an order by 6.7%, 2.9%, 2.2%, and 0.5%, respectively.

Figure 3. Fitness per a Comparison of Nonparametric Aggregate Estimation Versus Prediction from Our Model  
![](/api/attachments/D6389UFV/fulltext/images/1c5099f7f69f6989e16b12456d8b7e3176de40d182cbcce60e7e702fe20a5509.jpg)

![](/api/attachments/D6389UFV/fulltext/images/812705b68de399d18cd0b8753f8533c409eec9d5fb56a315efbf7684b253db29.jpg)

Fitness of Conditional Decision to Pav Online  
![](/api/attachments/D6389UFV/fulltext/images/7755b3337e278d2c11a121162a7c661152e0a1236d76ef6684a5b20b3a6f91f4.jpg)

We further find strong evidence of learning, as shown in Table 4 and Figure 4. The prior parameter for app attribute $A _ { a 0 }$ is <sup>−</sup>2.02, which is significantly lower than the normalized posterior parameter $\dot { A _ { a 1 } }$ (Z-score of <sup>−</sup>3.31). This difference indicates the undervaluation of the TNC app by drivers before they start to use it and suggests that learning can help to eliminate the perception bias gradually. We estimate $\log ( \sigma _ { a 1 } ^ { 2 } )$ to be 0.16, or the variance of signal $\sigma _ { a 1 } ^ { 2 }$ of 1.17, larger than the one-normalized experience variability parameter (Z-score of 2.01). This indicates that the signal is not quite clear and precise. Thus, drivers learning process in regard to the attribute of using the app to accept an order is slow. The smaller the variability parameter is, the greater the weight of the signal is from usage experience and the faster the learning process is. Combined with the estimation results in Stages 2 and 3, which show that the learning for using online pay and canceling orders is even slower, this result demonstrates why the TNC platform in our example uses a sales promotion associated with the online-pay function rather than per-use. We further show that drivers are more willing to use the app when their perceived passenger network size on the app is large.

Table 4. Estimation Results

<table><tr><td>Parameter</td><td colspan="2">Segment 1</td><td colspan="2">Segment 2</td></tr><tr><td colspan="5">Decision to accept an order</td></tr><tr><td> $A_{a0}$ </td><td>-2.02</td><td>(0.61)***</td><td></td><td></td></tr><tr><td> $A_{a1}$ </td><td>0</td><td>(fixed)</td><td></td><td></td></tr><tr><td> $\sigma_{a0}^{2}$ </td><td>1</td><td>(fixed)</td><td></td><td></td></tr><tr><td> $\log(\sigma_{a1}^{2})$ </td><td>0.16</td><td>(0.08)**</td><td></td><td></td></tr><tr><td> $\log(\beta_{a1})(attribute)$ </td><td>0.43</td><td>(0.02)***</td><td></td><td></td></tr><tr><td> $\beta_{am2}(network size)$ </td><td>0.20</td><td>(0.11)**</td><td>0.40</td><td>(0.17)***</td></tr><tr><td> $c_{am0}$ </td><td>0.07</td><td>(0.03)**</td><td>0.06</td><td>(0.05)</td></tr><tr><td colspan="5">Decision to fulfill an order</td></tr><tr><td> $A_{f0}$ </td><td>-2.62</td><td>(0.42)***</td><td></td><td></td></tr><tr><td> $A_{f1}$ </td><td>0</td><td>(fixed)</td><td></td><td></td></tr><tr><td> $\sigma_{f0}^{2}$ </td><td>1</td><td>(fixed)</td><td></td><td></td></tr><tr><td> $\log(\sigma_{f1}^{2})$ </td><td>5.37</td><td>(1.19)***</td><td></td><td></td></tr><tr><td> $\log(\beta_{f1})(attribute)$ </td><td>-1.42</td><td>(0.10)***</td><td></td><td></td></tr><tr><td> $\beta_{fm2}(platform subsidy)$ </td><td>1.08</td><td>(0.05)***</td><td>1.00</td><td>(0.02)***</td></tr><tr><td> $\beta_{fm3}(passenger bids)$ </td><td>1.18</td><td>(0.21)***</td><td>1.15</td><td>(0.15)***</td></tr><tr><td> $\beta_{fm4}(driver cashback)$ </td><td>5.36</td><td>(0.91)***</td><td>3.60</td><td>(0.40)***</td></tr><tr><td> $c_{fm1}(online-pay cost)$ </td><td>-6.44</td><td>(1.10)***</td><td>-4.14</td><td>(1.29)***</td></tr><tr><td> $c_{fm0}$ </td><td>-0.60</td><td>(0.12)***</td><td>-0.98</td><td>(0.33)***</td></tr><tr><td colspan="5">Decision to pay online</td></tr><tr><td> $A_{o0}$ </td><td>-8.13</td><td>(1.41)***</td><td></td><td></td></tr><tr><td> $A_{o1}$ </td><td>0</td><td>(fixed)</td><td></td><td></td></tr><tr><td> $\sigma_{o0}^{2}$ </td><td>1</td><td>(fixed)</td><td></td><td></td></tr><tr><td> $\log(\sigma_{o1}^{2})$ </td><td>1.21</td><td>(0.12)***</td><td></td><td></td></tr><tr><td> $\log(\beta_{o1})(attribute)$ </td><td>-0.76</td><td>(0.04)***</td><td></td><td></td></tr><tr><td> $\beta_{om2}(passenger cashback)$ </td><td>0.21</td><td>(0.05)***</td><td>0.28</td><td>(0.02)***</td></tr><tr><td> $c_{om0}$ </td><td>-1.02</td><td>(0.04)***</td><td>-1.54</td><td>(0.06)***</td></tr><tr><td colspan="5">Latent class</td></tr><tr><td> $\pi(m)$ </td><td>0.59</td><td>(0.14)***</td><td>0.31</td><td>—</td></tr><tr><td>Pseudo  $R^{2}$ </td><td>0.38</td><td></td><td></td><td></td></tr></table>

Note. We report standard errors in parentheses; — represents value with no estimates.  
\*\*Significance at 5%; \*\*\*significance at 1%.

The opportunity cost for outside goods $c _ { a m 0 }$ is insignificantly different from zero and slightly positive in the two latent classes, implying that outside goods, interestingly, generate equal or slightly higher attribute values when a driver uses the app but expects no passenger on the platform, no cancellation option, no monetary rewards for drivers, and/or no online-pay option. A possible explanation is that the usage complexity of the app (e.g., installation and setup) needs to be compensated. In regard to the effectiveness of sales promotion in the scenario in which uncertainty is eliminated, a simple calculation using our results from Stage 2 shows that a per-order compensation as low as \$0.02 is enough to cover the cost incurred by using the app to accept an order, which justifies the necessity of a subsidy for current TNC companies.

5.2.2. Stage 2. The positive and significant coefficient for cashback sales promotions for drivers indicates the effectiveness of the sales promotion in reducing drivers’ tendency to cancel an accepted order. Specifically, as the expected cashback also depends on drivers’ beliefs about passengers’ willingness to redeem the cashback (which is the same as the probability of using online pay), a positive coefficient suggests that drivers are less willing to cancel an order when they believe that passengers are highly likely to redeem a sales promotion and a large amount is promised in regard to the sales promotion. Note that, in Stage 3, we find that the belief about passengers willingness to redeem the cashback is a function of the sales promotion for passengers. The sales promotion strategy on the passenger side, thus, has an indirect and positive effect on drivers’ willingness to fulfill an accepted order. Quantitatively, we find that a onestandard-deviation increase in driver cashback and passenger cashback, on average, would increase the probability of fulfilling an order by 20.5% and 1.9%, respectively. From the platform’s perspective and conditional on the observed orders, \$1 more cashback for drivers would generate approximately \$1.98 in additional gross revenue.<sup>2</sup> On average, an active driver per day contributes \$2.55 additional gross revenue and the receipt of \$1.29 additional cashback. Assuming drivers take all of the revenue, a driver could earn \$3.84 extra per day.

Figure 4. Attribute Values and Uncertainties of Learning Processes  
![](/api/attachments/D6389UFV/fulltext/images/27fce3459484e0c8faa2f017b13b82ebeaf484bfeeaebeb9018b55649d507696.jpg)

![](/api/attachments/D6389UFV/fulltext/images/515ebc0efe1fc378897bd9dddafea3d71352bfc2aa8222c33a751788a7342275.jpg)

![](/api/attachments/D6389UFV/fulltext/images/35dc2db8c36b6bbab40b5df0ecbb5377c175e7b5a9deed4becb3dcf71b073588.jpg)

The coefficient of passenger bids and that of platform subsidy are also significantly positive but on a smaller scale compared with that of driver cashback. This supports our conjecture that, even though passenger bids and platform subsidy could lead to a higher utility level by providing a direct monetary incentive, they also might signal the poor quality of an order, such that passengers or the platform have to pay more to increase the probability that their orders could be taken, which consequently decreases drivers’ propensity to fulfill. One-standard-deviation increase in passenger bids and platform subsidy increases the probability of fulfilling an order by 5.8% and 7.1%, respectively. That is, \$1-greater passenger bids and platform subsidy could generate \$1.35 and \$1.18 additional revenue for the platform accordingly.

The attribute prior parameter, $A _ { s 0 . }$ , is estimated to be <sup>−</sup>2.62, much smaller than the normalized posterior parameter, $A _ { s 1 }$ (Z-score of <sup>−</sup>6.24), implying that drivers undervalue the perceived utility under uncertainty and, thus, overact by canceling existing orders. The experience variability parameter, $\log ( \sigma _ { s 1 } ^ { 2 } )$ is estimated to be 5.37. Compared with 1-normalized prior quality variance, it is much larger (Z-score of 4.51) and hence displays an extremely slow learning process. This learning pattern confirms our previous conjecture that the platform has to sustain the sales promotion for a certain length of time to ensure adequate learning.

We also identify two cost parameters associated with Stage 2. Given that the true attribute value is normalized to 0, the opportunity cost parameter associated with canceling the order, $c _ { f m 0 } .$ , in both latent classes is estimated to be negative (Z-scores of –5.02 and –2.97), equivalent to –\$0.20 and –\$0.33 when we adjust it with the cashback coefficient, showing an inferior expected utility for orders to be canceled. This is consistent with our intuition, as an accepted but later-on canceled order does not bring any revenue to the driver but, rather, costs time and gas potentially. The costs associated with using online pay for fulfilling an order, for both latent classes, are also negative and are adjusted to <sup>−</sup>\$1.20 and <sup>−</sup>\$1.15 using the cashback coefficient, showing a fixed cost for using online pay. Such a cost might result from the transaction cost of using online pay as well as the discounted utility due to delayed gratification.

![](/api/attachments/D6389UFV/fulltext/images/660a7068dba2d94b94cea788e17ecbae7e4d98bd825f7b4ddd05951e405c6b0e.jpg)

![](/api/attachments/D6389UFV/fulltext/images/92c7beb529fa4c776333b90ad5960533d9a0a5c82325b50d8c47fba3d6d225c9.jpg)

![](/api/attachments/D6389UFV/fulltext/images/39ebbffae49e8c1c0f3c3d320c8bbec927dda98cdbc206c3c09b6c196560a41c.jpg)

5.2.3. Stage 3. The coefficient of passenger cashback shows that, from the drivers’ perspective, passengers would be inclined to use online pay when the amount of cashback from the platform, as a bonus for using online pay, is high. This implies the effectiveness of the sales promotion on the passenger side.

With regard to learning, given that we fix the true attribute $\breve { A } _ { p 1 }$ at 0, the estimated negative prior attribute $A _ { p 0 }$ indicates the undervaluation of using online pay before drivers start to use and are informed about the quality of the app (Z-score of <sup>−</sup>5.77). In addition, to provide a comparison with the prior uncertainty of attribute $\sigma _ { p 0 } ^ { 2 }$ fixed at 1, we estimate lo $\phantom { } _ { ; } ( \sigma _ { p 1 } ^ { 2 } )$ to be 1.21; therefore, $\bar { \sigma } _ { p 1 } ^ { 2 }$ is much higher than $\overline { { \sigma _ { p 0 } ^ { 2 } } } ^ { r }$ (Z-score of 10.08), indicating a slow learning speed of the passenger population. The utility for outside goods is estimated to be <sup>−</sup>1.02 and <sup>−</sup>1.54 for the two latent classes. Thus, the online-pay function, in general, generates a positive utility for passengers compared with traditional cash transactions.

## 5.3. Extended Analysis and Robustness Check

We report the results of three extended analyses to check the robustness of our finding. First, we include the estimation results of Model 3 in the model comparison, which uses random parameters to substitute our latentclass parameters. Second, because our observation period includes a major holiday, a potential concern is whether seasonality would affect our results. Therefore, we include holiday/nonholiday as a variable that governs the utility of accepting an order online.

Given the complexity of our proposed model, especially the specification in Stages 1 and 2, we further estimate a simplified model that combines the two stages into one. In particular, we treat declining an order in Stage 1 the same as canceling in Stage 2, termed “not fulfill,” and as a result, there is only one stage of decision to fulfill or not. All of the independent variables in the utility functions of Stages 1 and 2 in our proposed model are included, except that this model has only one learning process for fulfilling an order, as only one type of signal for learning, driver’s experience of fulfilling orders, exists.

A more detailed specification and the results are reported in the Online Appendix. This detailed report shows that the random parameter approach and seasonality do not greatly affect the other parameters in our model, and that the qualitative interpretation of our main results is still robust. In addition, the simplified model results generate similar insights to the findings of the proposed model, which, once again, indicates the robustness of our analysis.

## 6. Policy Simulation

Our prior analysis qualitatively exhibits the learning effects, forward-looking behavior, and direct effects of sales promotions on drivers’ decisions as well as quantitatively measures the compound impact of a sales promotion policy, including the direct effect and the indirect ones through learning and forwardlooking. As the indirect effects are captured by the model structure, instead of directly by the parameters, the magnitude of indirect effects is absorbed by the compound effect and is difficult to identify separately by the estimated parameters. To highlight the importance of the mechanism of learning and forward-looking and their dynamic interactions with sales promotions, we apply simulations to explicitly quantify the indirect effects through learning and forward-looking on drivers’ decisions.

Other than the theoretical contribution, we further apply simulation methods to shed light on the practical side of our findings. We propose new cashback policies by leveraging the indirect effects through learning and forward-looking to improve the effectiveness of the sales promotion from the perspective of practitioners. Note that the focus of a growing company might not be profit optimization. Instead, our focal company is trying to increase its supply side and the adoption of online pay. Therefore, our policy aims at increasing acceptance, fulfillment, and online-pay rates by drivers while not being less cost effective for the platform. In particular, we set our outcome variables as fulfillment rate, which is the joint probability that an order is accepted and not canceled, and online-pay rate, which is the joint probability of acceptance, fulfillment, and online pay.

We use our parameter estimates to simulate a driver’s decision to accept an order, whether a transaction is fulfilled, and whether a driver receives a cashback bonus. Specifically, we first draw every driver’s type m based on π m . Given a policy, our model structure, and the parameter estimates for type m, in each loop of simulation, at t = 1, we first simulate the prior attribute values of matching, fulfilling, and online pay from their estimated prior distribution. We then reconstruct the expected utility function and simulate a driver’s decision to accept an order and fulfill it and whether the transaction is completed with online pay sequentially. The simulated decisions determine the updated perceived values of three attributes by using Bayesian learning in the next time period and, further, determine the next stage decisions. We keep this loop until the last time period for each individual and simulate each policy 1,000 times, taking the average as our result. Notably, due to data limitations, our simulation is based on the observed orders, and our findings are conditional on them. We focus on drivers’ decisions, conditional on an order arrival. Therefore, we present the simulation results as the fulfillment rate and online-pay rate, conditional on the cumulative transaction number. Although our policy change also might affect the order generation, we do not focus on this due to our research scope and data limitations.

## 6.1. Estimating Learning-Induced Indirect Effect of Sales Promotion

In the first set of policy simulations, we focus on the time dimension, in which we attempt to differentiate the learning-induced indirect effect from the salespromotion-induced direct effect on platform performance. We first simulate a baseline of drivers’ decisions across time periods, following the original promotion policy. Then, to display the direct effect of sales promotions, we find a benchmark time point in Figure 3 when the perceived value has converged to the true value from that point on, implying that learning is no longer updated, and an indirect effect through learning is no longer generated. We visualize the direct effect by simulating a case of \$0.15 cashback reduction in a sales promotion policy from the benchmark time point. Finally, we simulate the third case with a penalty before the benchmark point such that usage experience as well as learning are prohibited; then, we set promotion to again be \$0.15 less than the benchmark point. Because sales promotion is identical from the benchmark point such that the direct effect is the same, we visualize the indirect effect by presenting the difference between the second and third simulations, which is explained by the learning effect before the benchmark point only.

We aggregate the fulfillment rate and online-pay rate with respect to the cumulative transaction number and show our results in Figure 5. The baseline case is represented by the solid lines, which indicate the fulfillment rate and online-pay rate of the original policy accordingly. From Figure 3, we identify the cumulative transaction number (cumulative transaction number and time point are used interchangeably) 350 (on the x axis) as the benchmark point, as there is no more learning afterward. In the second case, we simulate the dashed line with a decrease of \$0.15 from time point 350. Because the promotion policies for dashed lines and solid lines are the same, and the learning has been fully finished before time point 350, the indirect effect through learning is the same at and after time point 350. As a result, the difference between the dashed line and baseline after time point 350 can be attributed solely to the direct effect of \$0.15 cashback reduction.

In the third case, we simulate the dotted line, which removes not only the direct effect of \$0.15 but also the learning-induced indirect effect from the sales promotion before time point 350. To achieve this, we impose a negative sales promotion of <sup>−</sup>\$3 before time point 350, which inhibits most of the order fulfillment and eliminates drivers’ learning through usage experience. From time point 350 to the end, we apply the same sales promotion strategy (\$0.15 cashback reduction), seen in the dotted line, to guarantee an identical direct effect of a sales promotion for the dotted and dashed cases. As a result, the difference between the dotted and dashed cases after the benchmark point will be explained by past learning, which is the only difference between these two cases. Because past learning is introduced by the past sales promotion policy, we can attribute the difference to the consequence of the indirect effect of sales promotions in the earlier time period. As we can observe, the dotted line still follows an increasing pattern, implying that drivers are still learning about the true value of the attributes of the app. This indirect effect will diminish with the accumulation of usage experience.

## 6.2. Estimating the Indirect Effect of Sales Promotion Through Forward-Looking

Our model estimation results show that a sales promotion on the passenger side has an indirect effect on outcome variables through the forward-looking behavior of drivers. However, the effect itself is not explicit, given the nonlinear structural model. We visualize this effect explicitly by adjusting passengerside sales promotion policy to simulate the outcome variables. In addition, we simulate the outcome variables with an identical adjustment to the driver-side sales promotion to comparatively illustrate the strength of a passenger-side sales promotion effect.

We first simulate the outcome variables of fulfillment rate and online-pay rate with the original sales promotion policy, shown as the solid line. Given a reduction of \$0.15 on the passenger-side cashback, we simulate the outcome variables represented by the dotted line. Further, we apply the same adjustment to the driver side, shown as the dashed line. The graph on the left in Figure 6 shows that, although present, the marginal effect of the passenger-side sales promotion is very limited in terms of the fulfillment rate compared with that of the driver-side sales promotion. With respect to online-pay rate (the graph on the right), as a sales promotion on the passenger side has a direct effect on the use of online pay, its overall marginal effect is more significant. Note that our online-pay rate is a joint probability that includes the effect of fulfillment rate, and thus, the promotion on the driver side has an impact on online-pay rate. If we consider the online-pay rate conditional on fulfillment, the driver-side promotion, as we model, should have no impact on online pay.

Further, we specify a more powerful adjustment toward a sales promotion to test whether similar results will be maintained. In our experiment, represented in Figure 7, we reduce the sales promotion by \$1 on either the passenger side or driver side. Compared with our findings in Figure 6, the marginal effects of sales promotion adjustment are more significant for both fulfillment rate and online-pay rate, and the conclusion that driver-side effect is more prominent still holds in the new experiment. Note that our research is conditional on fixing order generation due to data limitations; this observation leads to a managerial suggestion that, to optimize the overall supply conditional on the arrival of orders, the TNC should put more weight on the driver side.

## 6.3. Optimizing Sales Promotion

In this section, we apply model estimation results and earlier policy simulations to optimize the sales promotion strategy for the TNC supply shortage. Here, we do not attempt to manipulate the policies to achieve optimality, but rather, we show directive heuristic policy-making methods, which, by following, we can improve the platform performance. Our objective is to increase the fulfillment and online-pay rates while not being less cost effective for the platform

Figure 5. Direct and Learning-Induced Indirect Effects of Sales Promotion  
![](/api/attachments/D6389UFV/fulltext/images/550630889c905019fa4037bde95f9e8dcb3cb5b2ffd1e48ddb96090e04a2533d.jpg)

![](/api/attachments/D6389UFV/fulltext/images/f202cd49cb64357e836ac7df44912c559f40c2e3e211db5a62558601e26ca3d3.jpg)

The heuristic policy that we use is based on our findings of an indirect effect generated from learning and from forward-looking. Because a sales promotion of the passenger side shows a weaker effect on drivers’ fulfillment compared with that of the driver side, our first adjustment is to rebalance sales promotion between the two sides with more weight on the driver side. Further, we rebalance sales promotion with regard to time. Specifically, we use more sales promotion at the beginning of the product introduction period to achieve a more indirect effect. This is consistent with our claim that a sales promotion has a marginal indirect effect when learning happens.

Again, we start by simulating a baseline by following the original policy, shown as the solid line in Figure 8.

In this policy, a sales promotion exists for both sides, with an average of \$1.47 for the driver side and \$1.58 for the passenger side and an overall sales promotion cost of \$285,086 for 952 drivers. The first adjustment that we make is to remove all sales promotions on the passenger side and increase the sales promotions on the driver side by \$0.10, shown as the dashed line. The overall sales promotion cost decreases significantly to \$121,681, along with a significant loss of overall online-pay usage, shown as the space between the solid and dashed lines, due to inadequate learning. The fulfillment rate decreases at the very beginning due to the effect of forward-looking and learning. The online-pay rates of the solid and dashed lines converge to a similar level with the accumulation of usage experience, implying similar direct effects of these two sales promotion policies. The fulfillment rate is higher at the later periods for the new policy due to the similar effect of forward-looking and learning and the increased direct effect of \$0.10.

Figure 6. Decrease in Passenger-Side Sales Promotion by \$0.15  
![](/api/attachments/D6389UFV/fulltext/images/e483e4418acf07a1e527f2b28f32ca2d8d24f03b3ed3fc31f27a4cf97c240f5a.jpg)

![](/api/attachments/D6389UFV/fulltext/images/66f3139ef5ebd3cdfc031836bf38babfa6a52890364b02c938bb811bd9b7850f.jpg)

Figure 7. Decrease in Passenger-Side Sales Promotion by \$1  
![](/api/attachments/D6389UFV/fulltext/images/3f0ac1ec80b30ebf5371a0a519cef959df34fe8d9aa44795e4a50b5f2f676e2c.jpg)

![](/api/attachments/D6389UFV/fulltext/images/4681b486065b66cb7246e31cbde0df17bd3b6d0e5ea79c7a8c4f699ed6bc0601.jpg)

To alleviate the loss due to an inadequate earlierstage sales promotion, we increase sales promotion on the passenger side to \$4 during the first month after the app is released, reducing the overall cost to \$184,130. From the dotted line, we see that an intensive sales promotion works effectively to increase the overall fulfillment and online-pay rate by both direct and indirect effects, shown as the space between the dotted and dashed lines. The effects occur not only on the left-hand side of each figure, when the increased sales promotion is imposed, but also in the regions on the right-hand side, where an indirect effect through learning remains. The online-pay rate, however, still falls below the original solid line due to slower learning on online pay that results from insufficient incentivizing.

Our final policy is based on the dotted line, with a policy change of the sales promotion of \$3 for the first 50 orders on the driver side. The intensity of this short period promotion doubles the average in the original case. The reason that we offer only 50 orders with a doubled sales promotion is that a more intensive sales promotion will lead to an even faster learning process and, thus, more learning-induced indirect effects. The dot-dash lines in Figure 8 represent the overall performance of this policy, with the space between the dot-dash and dotted lines representing the marginal effect of an early sales promotion on the driver side. The figure also shows the indirect effect through the gap between the dotted and dot-dash lines after a cumulative transaction number of 50. Our final policy almost envelops the original one (solid line) regarding both fulfillment and online-pay rate, indicating an overall improvement with respect to app usage. In addition, the overall cost is \$247,399, much less than the \$285,086 in the original policy, and, consequently, results in a higher platform profit. This finding explains why many TNCs have an intensive sales promotion at the very beginning.

Figure 8. Fulfillment and Online-Pay Rates with Improved Sales Promotion Strategy  
![](/api/attachments/D6389UFV/fulltext/images/3ed664302e52e28f5f791f97dd05228bea7b1c98a1dd13bd95779f298d8dbffd.jpg)

![](/api/attachments/D6389UFV/fulltext/images/f976b1d9342356180942526e11b9ce8ee0e8214304004178b27124dad997390d.jpg)

It is worth noting that, even when learning is improved by imposing an intensive sales promotion, this does not necessarily imply that such a promotion should last until the learning finishes. In fact, none of our simulations lead to completed learning by the end of an intensive sales promotion. Although learning can lead to a higher perceived attribute value, its marginal effect diminishes with the accumulation of usage experience, and there will be a point where the marginal effect of learning is inadequate to cover the cost incurred by a sales promotion.

## 7. Conclusion and Implications

TNC app platforms are attempting to accelerate drivers’ learning about new features and maintain their high app-usage rates in a cost-effective way. By leveraging transaction-level data of drivers on a TNC app, we find a means to reduce their reliance on sales promotions by developing an understanding of the following mechanisms: (1) the economic value of TNC matching, cancellation, and online-pay features; (2) how new drivers learn those features and form their initial preference of TNC apps; and (3) how a two-sided sales promotion affects the formation of initial learning.

Our findings extend the understanding of the transformative and disruptive impact of IT in transportation to a finer-grained attribute/feature level. In particular, our results show the utility value/cost associated with matching an order, canceling an order, and paying online. Because those features are essential components of TNC apps, our work decomposes the economic value of TNC apps into finergrained components, which sheds light on the TNC app attributions and designs.

Our analysis also reveals drivers’ learning process of multiple features on TNC apps. We show that TNC app users underestimate the attribute values of matching and cancellation and the perceived value of passengers’ preference to use an online-pay function. As a result, drivers form a comparably lower willingness to use the app and higher willingness to cancel an order. These biased perceptions are corrected with accumulated usage experience, with accepting an order on TNC as learned most quickly and the fulfilling/ canceling feature as learned most slowly. Once the learning process is completed, drivers are more tolerant of accepting and fulfilling orders and are more optimistic about being rewarded with a cashback bonus. These results indicate the significant role of usage experience in alleviating bias from uncertainty and support the common industry practice of enhancing usage experience during product introduction.

We contribute to the promotional strategy literature by empirically examining how a two-sided promotion affects a driver’s app use and learning. Our results qualitatively and quantitatively show how bids from passengers, subsidies from the app provider, and an online-pay-contingent cashback bonus for passengers and for drivers affect drivers’ decisions through a direct effect of immediate impact on the latent utility level, an indirect effect of drivers’ learning, and another indirect effect of drivers’ forward-looking on passengers’ decisions to use online pay. Interestingly, we show that passenger bids and platform subsidy exhibit a smaller magnitude of impact on a driver’s willingness to accept and fulfill an order as compared with cashback for drivers. One potential explanation is that a bid or a subsidy might also signal high risk and/or low quality of that order.

We further explicitly display the existence and the magnitude of the two indirect effects. The indirect effect through learning indicates that a sales promotion is an effective tool for user learning, and thus, a sales promotion in the introductory period has more value than does a promotion that is launched later. An early sales promotion additionally affects decisions in later periods through early accumulated usage experience that corrects the attribute perception bias. This finding justifies the importance of an early sales promotion for a recently introduced product and explains why most TNC app platforms put forth enormous effort toward sales promotions in early stages.

In addition, the indirect effect through forwardlooking indicates a cross effect of a two-sided sales promotion. Sales promotions for passengers can influence the decisions of drivers when drivers are rationally forward-looking, and the decisions of passengers affect drivers’ earnings. This suggests the importance of the interdependency when designing a two-sided promotion for a two-sided market. Finally, to shed more light on the practical aspects of our findings, we propose revised promotion policies that take advantage of both indirect effects to help the TNC alleviate the supply shortage while controlling its cost.

Our paper has several limitations. First, the data available for researchers are limited. Our data limit us from investigating the order-generation process. In addition, the introductory period of the product might indicate incomprehensiveness of data maintenance. For each transaction, our data do not include such information as pickup locations, destinations, duration, or traffic routes, even though drivers might be able to partially obtain or infer such information.

Such a limitation restricts our investigation under the assumption of homogeneity of orders in terms of drivers’ learning process. Second, we take sales promotion as exogenous. Research that considers a strategic sales promotion could allow investigation of competition among different platforms and extend our learning framework to that of forwardlooking. Such research requires a data set with a sufficiently long period of variance of a sales promotion in equilibrium. Our data include only a period with several constant sales promotion amounts, each of which lasts for a long period. Individuals are well informed that, in the coming period, the sales promotion is the same for all orders. In addition, the short introductory period may not support the equilibrium assumption. Third, we do not account for network effects in our model. Network effects can be one component of learning signals such that they may have an impact on the speed of learning. Due to the sparsity of observation and limited information, however, it is very difficult for us to determine the “learning from network” mechanism and recover the network structure. All of these limitations can be addressed with additional data.

Despite the limitations, our paper makes the following contributions. First, it is the first study that econometrically models drivers’ decision processes in the use of a TNC app. Our model captures how drivers’ decisions are influenced by TNC monetary rewards as well as their perception of passengers decisions. In addition to the direct effect from a twosided sales promotion, we also depict drivers’ learning from their usage experience that indirectly contributes to their overall use of the app. Our results describe drivers’ learning of multiple attributes of the TNC app. Second, we run policy simulations to examine differential effects from different sets of marketing promotion designs. This generates managerial insights for the runners of newly introduced products in regard to designing a sales promotion in a more effective way. Our counterfactual analyses suggest that an early, intensive sales promotion policy not only enhances users’ willingness to use but also is cost effective.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their insightful comments and constructive suggestions.

## Endnotes

<sup>1</sup> Alternatively and equivalently, we could specify $u _ { a i 1 t } = \mathbf { m a x } ( u _ { f i 1 t } .$ $u _ { f i 0 t } ) + \varepsilon _ { a i 1 t }$ and have $\beta _ { a i 1 } A _ { a } + \beta _ { a i 2 } N _ { t }$ enter both $u _ { f i 1 t }$ and $u _ { f i 0 t }$ . The terms $\beta _ { a i 1 } A _ { a } + \beta _ { a i 2 } N _ { t }$ will still be canceled out in stage $^ { 2 , }$ because only difference matters.

<sup>2</sup> We use \$3.50 per order revenue for the calculation based on the company’s disclosure.

## References

Ackerberg DA (2003) Advertising, learning, and consumer choice in experience good markets: An empirical examination. Internat. Econom. Rev. 44(3):1007–1040.

Albuquerque P, Pavlidis P, Chatow U, Chen KY, Jamal Z (2012) Evaluating promotional activities in an online two-sided market of user-generated content. Marketing Sci. 31(3):406–432.

Arcidiacono P (2005) Affirmative action in higher education: How do admission and financial aid rules affect future earnings? Econ ometrica 73(5):1477–1524

Berry S, Levinsohn J, Pakes A (1995) Automobile prices in marke equilibrium. Econometrica 63(4):841–890.

Buchholz N (2015) Spatial equilibrium, search frictions and efficient regulation in the taxi industry. Technical report, University o Texas at Austin, Austin.

Burtch G, Carnahan S, Greenwood BM (2018) Can you gig it? An empirical examination of the gig economy and entrepreneurial activity. Management Sci. 64(12):5497–5520.

California Public Utilities Commission (2013) Decision adopting rules and regulations to protect public safety while allowing new entrants to the transportation industry. Accessed September 9, 2018, http:/ docs.cpuc.ca.gov/PublishedDocs/Published/G000/M077/K112/ 77112285.PDF.

Chan TY, Hamilton BH (2006) Learning, private information, and the economic evaluation of randomized experiments. J. Political Econom. 114(6):997–1040

Chen T, Sun B, Singh V (2009) An empirical investigation of the dynamic effect of Marlboro’s permanent pricing shift. Marketing Sci. 28(4):740–758.

Cohen P, Hahn R, Hall J, Levitt S, Metcalfe R (2016) Using big data to estimate consumer surplus: The case of Uber. NBER Working Paper No. 22627, National Bureau of Economic Research, Cambridge, MA.

Crawford GS, Shum M (2005) Uncertainty and learning in phar maceutical demand. Econometrica 73(4):1137–1173.

Erdem T, Keane MP (1996) Decision-making under uncertainty: Capturing dynamic brand choice processes in turbulent con sumer goods markets. Marketing Sci. 15(1):1–20.

Erdem T, Sun B (2002) An empirical investigation of the spillover effects of advertising and sales promotions in umbrella branding. J. Marketing Res. 39(4):408–420.

Erdem T, Keane MP, Sun B (2008) A dynamic model of brand choice when price and advertising signal product quality. Marketing Sci. 27(6):1111–1125.

Frechette GR, Lizzeri A, Salz T (2019) Frictions in a competitive, regulated market: Evidence from taxis. Amer. Econom. Rev. 109(8): 2954–2992.

Ghose A, Han SP (2011) An empirical analysis of user content gen eration and usage behavior on the mobile Internet. Management Sci. 57(9):1671–1691.

Gong J, Greenwood BN, Song Y (2017) Uber might buy me a Mercedes Benz: An empirical investigation of the sharing economy and durable goods purchase. Working paper, Temple Univer sity, Philadelphia.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride-sharing and alcohol related moto vehicle fatalities. MIS Ouart. 41(1):163–187

Heckman J, Robb R (1985) Alternative methods for evaluating the impact of interventions. J. Econom. 30(1–2):239–267.

Ho YC, Wu J, Tan Y (2017) Disconfirmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642.

Huang Y, Vir Singh P, Srinivasan K (2014) Crowdsourcing new product ideas under consumer learning. Management Sci. 60(9): 2138–2159.

Kamakura WA, Russel GJ (1989) A probabilistic choice model for market segmentation and elasticity structure. J. Marketing Res. 26(4):379–390.

Lam C, Liu M (2018) More than taxis with an app: How ride-hailing platforms promote market efficiency. Working paper, Clemson University, Clemson, SC.

McFadden D (1978) Quantitative methods for analyzing travel behavior of individuals: Some recent developments. Hensher D, Stopher P, eds. Behavioral Travel Modelling (Croom Helm London, London), 279–318.

Park J, Kim J, Pang MS, Lee B (2017) Offender or guardian? An empirical analysis of ride-sharing and sexual assault. Working paper, Korea Advanced Institute of Science and Technology, Daejeon, South Korea.

Rhee KM, Zheng J, Wang T, Tan Y (2018) Technology restriction and demand shifts in transportation dynamics: an empirical study. Working paper, University of Washington, Seattle.

Wu C, Che H, Chan TY, Lu X (2015) The economic value of online reviews. Marketing Sci. 34(5):739–754.

Zhang Z, Li B (2017) A quasi-experimental estimate of the impact of P2P transportation platforms on urban consumer patterns. Matwin S, Yu S, Farooq F, eds. Proc. 23rd ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Com puting Machinery, New York), 1683–1692.

Zhao Y, Yang S, Narayan V, Zhao Y (2013) Modeling consumer learning from online product reviews. Marketing Sci. 32(1): 153–169.
