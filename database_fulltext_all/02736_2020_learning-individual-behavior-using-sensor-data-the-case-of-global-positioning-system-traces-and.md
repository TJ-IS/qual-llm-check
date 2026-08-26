---
otero_id: 2736
otero_key: "WYF5N7ZC"
title: "Learning Individual Behavior Using Sensor Data: The Case of Global Positioning System Traces and Taxi Drivers"
authors: "Yingjie Zhang; Beibei Li; Ramayya Krishnan"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0946"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Information Systems Research

![](/api/attachments/WYF5N7ZC/fulltext/images/f1fa05ed5194812dfa8e46eb012549d6de6ba7a3ad2c538aeef37b9cf81b3aed.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Learning Individual Behavior Using Sensor Data: The Case of Global Positioning System Traces and Taxi Drivers

Yingjie Zhang, Beibei Li, Ramayya Krishnan

Yingjie Zhang, Beibei Li, Ramayya Krishnan (2020) Learning Individual Behavior Using Sensor Data: The Case of Global Positioning System Traces and Taxi Drivers. Information Systems Research

Published online in Articles in Advance 05 Oct 2020

https://doi.org/10.1287/isre.2020.0946

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Learning Individual Behavior Using Sensor Data: The Case of Global Positioning System Traces and Taxi Drivers

Yingjie Zhang,<sup>a</sup> Beibei Li,<sup>b</sup> Ramayya Krishnan<sup>b</sup>

<sup>a</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080; <sup>b</sup> Heinz College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213

Contact: yingjie.zhang@utdallas.edu, https://orcid.org/0000-0003-0745-2563 (YZ); beibeili@andrew.cmu.edu, https://orcid.org/0000-0001-5466-7925 (BL); rk2x@cmu.edu, https://orcid.org/0000-0001-9935-2468 (RK)

Received: July 23, 2018 Revised: October 24, 2019; March 17, 2020 Accepted: May 12, 2020 Published Online in Articles in Advance: October 5, 2020

https://doi.org/10.1287/isre.2020.0946

Copyright: © 2020 INFORMS

Abstract. The ubiquitous deployment of mobile and sensor technologies enables observation and recording of human behavior in physical (off-line) settings in a manner similar to what has been possible to date in online settings. This provides researchers with a new lens through which to study and better understand previously unobservable individua decision-making processes. In this study, using a Bayesian learning model with a rich data set consisting of approximately two million fine-grained Global Positioning System (GPS) observations, we analyze the decision-making behavior of 2,467 single-shift taxi drivers in a large Asian city with the objective of understanding key factors that drive the supply side of urban mobility markets. The data set includes detailed taxi GPS trajectories, taxi occupancy data (i.e., whether the taxi is occupied or not), and taxi drivers’ daily incomes. This capacity to use data for which occupancy of the taxi is known is a distinctive feature of our data set and sets our work apart from prior work in the literature. The specific decisions we focus on pertain to actions drivers take to find new passengers after they have dropped of current passengers. In particular, we study the role of information derivable from GPS trace data (e.g., where passengers were dropped off, where they were picked up, longitudinal taxicab travel history with fine-grained time stamps) observable by or made available to drivers in enabling them to learn the distribution of demand for their services over space and time. We find significant differences between new and experienced drivers in both learning behavior and driving decisions. Drivers benefit significantly from their ability to learn from not only information directly observable in the local market but also aggregate information on demand flows across markets. Interestingly, our policy simulations indicate that information that is noisy at the individual level becomes valuable when ag gregated across relevant spatial and temporal dimensions. Moreover, we find that the value of information does not increase monotonically with the scale and frequency of information sharing. Our results also provide important evidence that efficient information sharing can lead to a welfare increase among drivers because of potential market expansion. Efficient information sharing can bring, within the taxi market, additiona income-generating opportunities that could be unfulfilled. Overall, this study not only explains driver decision-making behavior but also provides taxi companies with an implementable information-sharing strategy to improve overall market efficiency.

History: Yong Tan, Senior Editor; Wonseok Oh, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2020.0946.

Keywords: mobility analytics • GPS trajectory • Bayesian learning • taxi industry • driver heterogeneity • information sharing • driver welfare

## 1. Introduction

## 1.1. Taxi Industry

The taxi industry is a major component of the urban transportation infrastructure. According to a recent report by Brennan (2014), every year approximately 700 million passengers are transported by taxicabs in the United States, generating \$16 billion in revenues. However, inefficiency in the taxi markets has been well documented, leading to both low utilization of taxis and high wait times for customers (Buchholz 2015, Salz et al. 2019). For example, in New York City (NYC), the average taxi occupancy during weekday rush hours was only 56% in 2014.<sup>1</sup> Moreover, passengers have an especially difficult time hailing taxis during shift changes and in bad weather. This is not limited to NYC. For example, in Beijing, around 30% of people spent more than 20 minutes waiting for a taxi in 2015, and yet, a taxi’s average monthly empty-car distance was 2,400 km compared with an occupied distance of 5,088 km, which indicates that, on average, about onethird of total driving distance was allocated not to the serving of passengers but instead to the search for them.<sup>2</sup> More recently, as shown in Cramer and Krueger (2016), even after using the matching techniques, drivers’ occupancy rate is still low (i.e., although increased compared with the previous taxi market, unfortunately, still around only 55%–65%). This finding indicates that between one-third and even onehalf of drivers’ total working time is wasted idling between trips. This strongly indicates the potential inefficiency in the taxi market even after ridesharing or ride-hailing platforms started using automatic matching algorithms.

Such inefficiency in the taxi market has attracted both industry and academic attention. Recent work studying the matches made between drivers and passengers as revealed in taxi pickup and drop-off data has sought to explain market inefficiency prevailing under regulation. For example, Buchholz (2015) analyzes the same NYC taxi data to explore the dynamic equilibrium effects of regulations on spatial search frictions and welfare. He finds significant search frictions that lead to a welfare reduction of \$422 nillion, or 62% per year.

Going beyond the basic tasks of connecting a rider to a driver, ride-hailing platforms, such as Uber or Lyft, have tried to address the inefficiency on the supply side of the taxi market by sharing real-time demand information with drivers through mobile technologies. For example, the surge maps in the Uber driver app and the prime-time pricing provided by Lyft provide drivers with better knowledge about real-time demand (e.g., pickups) distributions in the city. These strategies, however, still have downsides. First, they ignore the potential opportunity cost for a driver to drive to a certain location. Considering, for example, the time needed to drive to a certain location or the potential traffic or competition encountered at that location, it may not be profitable for the driver to follow the surge. Second, providing an identical realtime heat map of pickups to all drivers may not be an effective solution (Chen and Sheldon 2016, Guda and Subramanian 2019). Drivers are heterogeneous in their preferences and abilities to use different types of information for decision making. For example, beyond real-time pickups, some drivers may find other types of information (e.g., drop-offs, waiting time, trip incomes) more valuable to infer the distributions of demand in the city. Unfortunately, existing platforms fail to leverage the variety and heterogeneous value of information to reduce driver search frictions in the taxi market. One challenge is that in a traditional off-line setting, individual drivers’ decision processes are often unobserved; that is, it is often unobserved what situation a driver encounters in real time or what information signals a driver receives on the road prior to or during the decision making. Therefore, very limited knowledge has been developed toward understanding how drivers make realtime decisions to increase their utilization and the role information plays in helping them learn about demand in the taxi market.

## 1.2. Overview

To address these issues, in this paper, we focus on examining the value of different types of information in helping drivers find customers when they are unoccupied. More specifically, the ubiquitous deployment of mobile and sensor technologies today has enabled the capacity to observe and record driver behavior, at large scale and fine grain, in physical (off-line) settings. This provides us with a new lens through which to understand previously unobservable individual decision-making processes. The specific driver decisions on which we focus in this paper are to which locations to go when the taxis are unoccupied. We aim to understand how taxi drivers learn about demand from different types of real-time temporal, spatial, and contextual information (e.g., popularity of a location, time of day), trip information (e.g., trip income, travel speed, waiting time), and social information (e.g., nearby taxi drivers’ pickups or drop-offs) We seek to understand both the major drivers of heterogeneity in individual behavior and the discrepancy in the observed outcomes. We also aim to study, from a policymaker’s perspective, how to le verage such knowledge to benefit all drivers and improve market efficiency.

Note that with the full Global Positioning System (GPS) sensor data of the taxis, we now are able to document the entire demand search process undertaken by each driver. In other words, we observe not only the matches made between drivers and passengers in the taxi market but also drivers’ complete search trajectories leading to those matches. This is a unique feature of our study, which distinguishes this work from other existing work. Based on a similar context, literature from urban analytics and machine learning has traditionally focused on predicting driver behavior from large-scale observational data, providing data-driven approaches to build rich models and relying on cross-validations as a powerful too for model evaluation (e.g., Ge et al. 2010, Yuan et al. 2013, Liu et al. 2017). Nevertheless, such predictionfocused models may vary in their fundamental hypotheses of what drives the observed outcomes. They may not apply when we wish to answer questions about the counterfactual impact of a change in policy, especially considering that the policy change has not necessarily been observed before or may have been partially observed only for a subset of the population (Athey 2015). This study, however, aims to understand the cause of a driver’s behavioral change when experiencing a policy change (e.g., when more demand or supply information in the market is provided to the driver in real time).

In this paper, our research questions include the following: (1) How do taxi drivers infer the distribution of demand in the city based on different information to which they are exposed at different locations and in different time periods? (2) How do different drivers respond to such information differently? (3) How can we leverage this knowledge to improve decision making for both individual drivers and platforms (e.g., how do we design effective information-sharing strategies)?

To address our research questions, we propose and estimate a structural learning model at the individualdriver level. Our structural econometric model approach builds on explicit economic theories, fully specifies the economic preferences of individuals under a behavioral model framework, and estimates the causal impacts of policies from data using statistical methods (Dubé et al. 2005, Reiss and Wolak 2007). Such a model allows us to examine the underlying mechanism of drivers’ behavioral changes.

We validate our study using a combination of three large and unique data sets containing complete information on approximately 2 million individual observations from 2,467 taxi drivers in a large Asian city for August and September 2009:<sup>3</sup> (1) the taxi’s GPS trajectory data (e.g., real-time geographic coordinates and time stamps at the minute level), (2) the taxi’s triprecord data (e.g., trip distance, geographic coordinates of pickup and drop-off locations, and incomes paid for the trip), and (3) geospatial map data (e.g., type and density of points of interest).

A summary list of findings from our empirical analyses is as follows. First, the results indicate strong heterogeneity in city demand across both spatial and temporal dimensions. Second, on average, new drivers are much more active in learning from information signals than experienced drivers. This result indicates that experienced drivers overall have more precise prior knowledge on demand and that, therefore, additional real-time information signals, on average, are less valuable to them than to new drivers.

Third, there exists significant heterogeneity in the impacts of information signals on drivers’ decisions. Specifically, we observe that new drivers are much better at learning from simple and straightforward signals (e.g., other taxi pickups or number of vacant taxis nearby, which implies a direct effect on currentperiod demand or supply), whereas experienced drivers tend to ignore these simple signals and instead focus more on learning from the more complicated signals (e.g., other taxi drop-offs, which imply an anticipated effect on future-period demand).

Fourth, our policy-simulation results show that by aggregating the information extracted from drivers GPS mobility traces on a large scale, we can significantly improve the quality of individual drivers decision making. Notably, we find that information that is noisy at the individual level can become more valuable after we aggregate it across various spatial and temporal dimensions.

Finally, our study provides important evidence that efficient information sharing can lead to a welfare increase among drivers because of potential market expansion. Efficient information sharing can bring, within the taxi market, additional income-generating and customer service opportunities that are left unfulfilled. Our work not only explains driver decisionmaking behavior but also provides taxi companies with an implementable information-sharing strategy to improve overall market efficiency.

## 1.3. Contribution

The key contributions of our study can be summarized as follows. First, we demonstrate the value of extracting behavioral patterns from large-scale, finegrained off-line mobility trace data to the understanding and improvement of human decision making. In particular, by collecting and analyzing this new source of information, we are able to extract knowledge that is often unavailable to individuals or organizations in the conventional setting.

Second, we develop a Bayesian learning framework to examine drivers’ city-demand learning process based on the various information to which they are exposed. One methodological innovation of this framework is that we model the information signals differently in accordance with their contexts. In our model, the learning process is contingent on each driver’s own experience, observed peer behavior, and accumulated knowledge of how to interpret different signals in different ways. This model allows us to jointly identify the heterogeneity in individual learning ability as well as in the value of different types of information in real-time decision making.

Third, this paper is, to the best of our knowledge, the first paper to combine spatiotemporal data mining with structural econometrics to study decision making in social-cyber-physical systems. Such an approach allows us to link individual behavior and economic outcome from a more explanatory perspective. We aim to provide insights into how and why drivers behave in certain ways and how observed and unobserved individual characteristics can explain those behaviors.

Fourth, the literature on the mobile transportation field (including both the traditional taxi industry and the emerging ridesharing platforms) demonstrates empirically the behavioral changes under different contexts. They mainly focus on the taxi labor supply with exogenous changes in factors such as weather and entry of ridesharing platforms. Recent papers (e.g., Haggag et al. 2017) analyze drivers’ behavioral changes with aggregated observations. Our proposed structural model and the corresponding empirical analyses incorporate multilevel signals/feedback as determinants of drivers’ choices. Specifically, in our proposed model, over time, drivers who experience differently (i.e., who are exposed to different types of signals) diverge regarding their uncertainty on the evaluation of different choices (i.e., pairs of locations and time slots). In this way, we consider our model and analyses as a great theoretical strength in explaining drivers’ heterogeneity from a behavioral modeling process rather than simply assuming a parametric heterogeneity in the utility function (Erdem and Keane 1996).

## 2. Theoretical Background 2.1. Literature Review

Our study draws from the streams of literature discussed here. First, our study is related to the literature on computational urban analytics. In particular, the availability of real-time GPS trace data has attracted many researchers from the computer science and transportation fields to the study of drivers’ behavior analytics using machine learning techniques. Existing studies can be divided mainly into two categories: exploratory and predictive analyses. The first category explores the behavioral patterns of taxi drivers (e.g., Liao et al. 2006; Liu et al. 2010a, b; Balafoutas et al. 2013). For example, Liu et al. (2010b) propose a mobility-based clustering method to identify the hot spots of moving vehicles in an urban area. The second category of studies focuses on predictive analysis based on historical behavior of drivers (Hunter et al. 2009; Ge et al. 2010; Phithakkitnukoon et al. 2010; Liu et al. 2013, 2017; Yuan et al. 2013). For example, Ge et al. (2010) develop a mobile recommender system that has the ability to recommend a sequence of pickup points for taxi drivers or a sequence of potential parking positions. Yuan et al. (2013) propose a system for computing the shortest-time driving routes using traffic information and driver behavior However, most previous studies focus on exploring how drivers behave or on predicting what future driving routes should be, whereas relatively few studies have explained how information signals ob served by drivers are used to learn demand and supply competition at locations, thereby leading to decisions about where to go. Pure machine learning– based models make statistical predictions but do not separate out the economic values of information signals. Our model, on the contrary, studies the roles of information with a utility-based approach, which allows us to examine the counterfactual impacts of different policy changes.

Second, our paper is related to the social and economic perspectives of the taxi (or, more generally speaking, the vehicle-for-hire) market (e.g., Camerer et al. 1997; Farber 2005, 2008, 2015; Crawford and Meng 2011; Greenwood and Wattal 2017; Hall et al. 2015; Wang et al. 2019; Zheng et al. 2020; Haggag et al. 2017). These studies focus mainly on the relationship between taxi drivers’ daily wage targets and the taxi labor supply. Our paper distinguishes itself from these existing studies in that we aim to understand, from a micro perspective, how individual drivers learn to use various information signals to infer taxi demand in the city and to make real-time driving decisions accordingly. We achieve this by analyzing large-scale and granular-level taxi GPS traces. Haggag et al. (2017) aimed to address similar questions by understanding taxi drivers’ learning behavior. Their trip-level data, however, only allowed them to compare the productivity improvement from the first to the 100th shift. Our unique GPS trace data, by contrast, provide us with a way to recover drivers’ search traces and understand from them how their own experience and peer behavior can help improve their knowledge. Moreover, our structural model accounts for various information signals for individual-level learning in real time. This also enables us to study the underlying mechanisms of driver decision making.

Three recent studies that are highly related to our paper are those by Salz et al. (2019), Buchholz (2015), and Buchholz et al. (2016). These papers focus on economic demand and individual-level driver decisionmaking problems in the taxicab industry. By analyz ing NYC Yellow Medallion taxi data, Salz et al. (2019) study the effect of regulations on aggregate city-level taxi service and demand; Buchholz (2015) explores the dynamic equilibrium effects of regulations on spatial search frictions and welfare; and Buchholz et al. (2016) analyze the dynamic labor supply in the NYC taxi industry. Our paper distinguishes itself from these three papers in that we focus on the individuallevel driver decision-making processes, and we aim to understand and reduce potential market inefficiency by accounting for heterogeneity among individual drivers. Moreover, we observe drivers’ complete search trajectories. Significantly in this respect, our unique data set provides us with a holistic view of drivers’ full decision-making processes.

Third, and finally, our paper also is related to literature on consumer Bayesian learning models, which have been widely applied to the analysis of consumers choices under uncertainty in the fields of marketing, information systems, and economics. One of the most influential papers is that by Erdem and Keane (1996), which proposes a structural model for estimation of learning signals from both purchase experience and advertisements. Since Erdem and Keane (1996), Bayesian learning models have been widely applied in various fields, including health technology adoption (Hao et al. 2018), crowdsourcing (Huang et al. 2014), and wireless-service adoption (Iyengar et al. 2007). Meanwhile, there are several recent studies in the economics and marketing literature that improve the Bayesian learning model by introducing forgetting and forward-looking components (Ackerberg 2003, Mehta et al. 2004) or by considering the individual heterogeneity (Iyengar et al. 2007, Zhao et al. 2013, Zhang et al. 2019). The main model of our paper follows Erdem and Keane (1996) and extracts novel information signals from off-line trace data.

## 2.2. Theoretical Implications

In general, our paper has at least three theoretical implications in the areas of (1) spatial-temporalcontextual information on human decision making, (2) value of information with aggregation benefits, and (3) theories of experience in worker productivity.

First, our work closely builds on previous theoretical implications of spatial-temporal-contextual information on human decision making. Physical location is one of the customer-environmental cues that mobile devices identify that influence behaviors and attitudes (Bargh and Chartrand 1999). Prior literature demonstrates the existence of a location effect in the mobile context and quantifies it on the basis of the effectiveness of location-based advertising (e.g., Ghose et al. 2019, Molitor et al. 2019). Temporal information, by contrast, as suggested by prior literature, activates different goals. Time of day or day of the week, for example, significantly influences consumer purchasing decisions (e.g., Ghose et al. 2019). The interaction between spatial and temporal dimensions meanwhile also has a significant impact on consumer behavior (Luo et al. 2013). In addition, prior literature suggests that consumers’ broader environmental contexts (beyond immediate location and time) affect their decision making (Choi et al. 2012, Andrews et al. 2015, Ghose et al. 2019). Our study extends previous theoretical understanding on the value of spatial-temporal-contextual information on human decision making in the context of taxi market.

Second, another important finding in our paper is observed from our policy simulations, in which we point out that noisy signals become valuable with aggregation. This supports the theory of aggregated value of information, especially from an information intermediate perspective (Bhargava and Choudhary 2004, Bakos and Katsamakas 2008). Previous studies put more emphasis on the online two-sided marketplaces. In particular, Bhargava and Choudhary (2004) point out the main factors to explain the aggregation benefits: network effects and value-added service. Our empirical study extends this related literature by analyzing the labor-supply side of the urban mobility market and by decomposing the information-aggregation benefits to compare the aggregated values across different types of information.

Third, our work also contributes to prior literature on worker experience and productivity. Prior literature demonstrates both empirically and theoretically the relationship between experience and productivity with the introduction of information systems (Francalanci and Galal 1998, Aral et al. 2012, Menon et al. 2020). The literature shows great effort in exploring how new information systems would help improve workers’ productivity, especially for skilled workers (Tambe and Hitt 2012, Tambe 2014). In our empirical analysis, we model and evaluate drivers learning rates with different experience levels. In this way, we take a further step by focusing on new entrants (i.e., the less experienced drivers). Specifically, we show that new drivers are good at learning from simple signals. More important, for information that contains more noise and from which it is more complicated for new drivers to extract valuable messages, we present an aggregation approach to help them better improve their knowledge. This is essentially valuable in emerging markets, such as ridesharing platforms.

## 3. Research Context

We use a combination of three large, unique data sets containing individual trip records from all taxi drivers in a large Asian city for August and September 2009. This section first introduces the background of the city on which our research focuses; then we describe the details of the three data sets.

## 3.1. Background

The large Asian city that is the source of our data had a population of approximately 10 million people in 2009 and a population of around 14,000 people per square mile. In 2017, the city announced a policy to restrict traffic availability during the rush hours from 7–9 a.m. and 5:30–7:30 p.m. In 2009, buses were the major source of public transportation in the city, and two new subway lines were just open to traffic within the urban area and between the airport and the urban area. Multiple taxi companies operated within the city. The taxi drivers were allowed to choose time slots, and they had to pay a fixed leasing fee per month back to the company and could keep the rest. There was no significant difference among companies in terms of leasing fee. There were no surcharges to the trip price either. The city policy prescribed that taxis with urban tags could operate within the downtown areas (including the airport), whereas taxis with suburban tags could operate only in suburban areas (outside the downtown area). When a taxi was empty, to figure out when and where passengers might be waiting for a taxi in real time, a taxi driver would often make driving decisions based on the driver’s own experiences (e.g., passenger pickups or drop-offs, waiting time, etc.) and observed peer behaviors (e.g., other drivers’ pickups, drop-offs, or drive-bys) on the road. More experienced drivers, who typically have been exposed to such demand signals over a longer period, might be able to more precisely pin down the locations that provide them with a higher probability of picking up their next passengers.

## 3.2. Data Description

We conduct an empirical analysis on a combination of three large data sets: (1) taxi drivers’ GPS-coordinate tracking data, (2) taxi trip-record data, and (3) geospatial map data. Note that our data sets cover all existing companies in the focal city, which allows us to infer the overall city demand from the individual taxi traces. Such coverage is one advantage of our crosscompany data because no single company data set can observe all the information signals each driver receives to recover the true spatial and temporal demand.<sup>6</sup>

3.2.1. Taxi Drivers’ GPS-Coordinate Tracking Data. Each taxi’s GPS-tracking record includes taxi ID, real-time geographic coordinate information (i.e., longitude and latitude), recorded time, taxi company ID, and taxi type ID. According to city policy, taxis are divided into three types: urban taxis that can drive only within the downtown area, suburban taxis that can drive only outside the downtown area, and other taxis that can drive anywhere in the city. The GPS-tracking data were recorded approximately every one minute.

3.2.2. Taxi Trip-Record Data. Each trip record includes taxi ID, geographic and temporal information on starting and ending points, trip income (i.e., total money paid by the passengers), and total distance, taxi company ID, and the taxi type indicator. Combining these data with the GPS-tracking data, we have full GPS trajectories (when taxis are both occupied with passengers and empty) of a total of approximately 2 million trip records from 2,467 single-shift taxi drivers in August and September 2009.<sup>7</sup> Note that the availability of taxi occupancy is an important feature of our data relative to most of the other publicly available data sets (e.g., the NYC Taxi and Limousine Commission open data<sup>8</sup>), which contain only trip-record data (i.e., when the cars have passengers).

3.2.3. Geospatial Map Data. This data set consists of two parts: points of interest (POIs) and road intersections. Each POI has its geographic location. Each road intersection, meanwhile, has its specific geographic coordinates. Figure 1 illustrates four sampled drivers’ trajectories on September 1, 2009.

Figure 1. (Color online) Data Visualization of Driving Trace Plot with City Map  
![](/api/attachments/WYF5N7ZC/fulltext/images/4afaf6d572dbd34266db5bdffa0519e9c6d8756b6287eb53ad6d454f4408b27f.jpg)  
Notes. The lines are the streets in the large Asian city. The dots are sample drivers’ GPS records.

## 4. Model

Following Erdem and Keane (1996), we develop a Bayesian learning framework to model how taxi drivers learn the taxi demand in the city. Such a structural econometric model helps us explicitly model the individual decision-making process through the utility function. It also helps us disentangle the role different information signals play during the individual decision process. A visualized framework is shown in Section A of the online appendix.

## 4.1. Utility Function

A taxi driver’s decision about where to go when the taxi is vacant depends on that driver’s evaluation of all reachable locations (i.e., the choice set). We conceptualize the locations that a driver considers to be organized into a grid. The evaluation of a location is built on the driver’s expectation/knowledge with respect to the inherent quality in each location. The quality captures the trade-off between potential benefits (e.g., from picking up a passenger) and costs (e.g., from peer competition or substantial expenses, such as gas cost) within the location. In addition to taxi drivers’ long-term knowledge, drivers adjust their evaluations according to some short-term factors, such as weather change. Based on this understanding we model that at time $t ,$ taxi driver i’s utility of each location–time set j l, τ (i.e., l is the spatial unit of the choice set, and τ is the temporal unit of the choice set) as

$$
\tilde {U} _ {i j t} = \alpha \tilde {Q} _ {i j t} + \beta \mathsf {L o c} _ {j} + \gamma T _ {t} + \delta \mathsf {L o c} _ {j} \cdot T _ {t} + \varepsilon_ {i j t},\tag{1}
$$

where $\tilde { Q _ { i j t } }$ is driver i’s knowledge of the quality of location–time set j at time t; Loc includes the static features of location $j ,$ such as numbers of POIs; $T _ { t }$ includes the time-varying factors, such as weather; $\varepsilon _ { i j t }$ captures any idiosyncratic shock, following the type I extreme value distribution. Note that t and τ are different time units: t denotes the time of decision making, and τ is the time dimension of our choice set. The intuition behind τ is that the quality varies across locations and with time-of-day slots. For example, the demand in an office area during rush hour is different from that in the same area at midnight. To define τ in the choice ${ \mathrm { s e t } } ,$ we divide one day into $N _ { T }$ time-of-day slots. And if we use $N _ { L }$ to denote the number of location grids, the total number of location–time sets is $N _ { T } \times N _ { L }$ . For identification, we do not include a constant term in the utility function. We assume that taxi drivers make decisions based on their expected utility value. Accordingly, this expected utility is $U _ { i j t } =$ $\alpha Q _ { i j t } + \beta \mathrm { L o c } _ { j } + \gamma \mathrm { T } _ { t } + \delta \mathrm { L o c } _ { j } \cdot \mathrm { T } _ { t } + \varepsilon _ { i j t }$ , where $Q _ { i j t } \dot { = } E ( \tilde { Q _ { i j t } } )$

## 4.2. Knowledge-Acquisition Process

When driving around the city, drivers might be able to update their expectations of quality through their own passenger pickup experiences or by observing peer behavior on the road, such as other taxis’ pickups and drop-offs and numbers of nearby vacant taxis. These types of information can help drivers reduce the uncertainty of their expectations with respect to unobserved quality information. To model this learning process, we follow a structural framework of Bayesian learning by assuming that drivers use information signals to update their beliefs in a Bayesian fashion (Erdem and Keane 1996). Mathematically, let $d _ { \tt S i g n a l , i j t }$ denote whether driver i receives a signal in location–time set j at time t. If $d _ { \tt S i g n a l } , i j t = 1$ , the driver receives this signal and updates his or her knowledge about quality. The quality message contained in a particular signal is measured by $\mathrm { M S i g n a l } _ { i j t } .$ . Note that drivers might not precisely evaluate the messages from signals. Thus, similar to previous studies (Erdem and Keane 1996, Huang et al. 2014), we assume that the content of the information from signals $( \mathrm { i . e . , M S i g n a l } _ { i j t } )$ follows a normal distribution around the true unobserved quality $Q _ { j } \colon ^ { 9 }$

$$
\mathrm{MSignal} _ {i j t} \sim N \left(Q _ {j}, \sigma_ {\text { Signal }} ^ {2}\right),\tag{2}
$$

where $\sigma _ { \mathrm { { s i g n a l } } } ^ { 2 }$ is the variance of quality information contained in the signal. In other words, this variance represents the precision of the information that can be parsed from the signal, a greater value of $\sigma _ { \mathrm { { s i g n a l } } } ^ { 2 }$ suggesting a less precise signal. In Section $5 . 3 ,$ we introduce in detail the signals we consider and how we extract them from our data.

## 4.3. Updating Procedure

$\mathrm { A t } ~ t _ { 0 } ,$ before receiving any information, taxi drivers start with some prior beliefs about the true unobserved quality of each location–time set, $Q _ { j } ,$ , respectively. As is consistent with the previous literature on Bayesian learning (e.g., Erdem and Keane 1996, Huang et al. 2014), prior beliefs are assumed to be normally distributed with mean $Q _ { 0 }$ and variance $\sigma _ { Q 0 } ^ { 2 }$ . Over time, drivers receive surrounding signals, according to which they update their beliefs. By using Bayes’ rule (DeGroot 2005), drivers update their posterior beliefs as conditional on prior beliefs and signals. Because prior beliefs at time $t _ { 0 }$ and all signals are assumed to be normally distributed, the posterior quality at any time period also follows a normal distribution, which is given by

$$
\tilde {Q _ {i j t}} \sim N \Big (Q _ {i j t}, \sigma_ {Q, i j t} ^ {2} \Big),\tag{3}
$$

where

$$
Q _ {i j t} = \left[ \frac {Q _ {i j , t - 1}}{\sigma_ {Q , i j , t - 1} ^ {2}} + \sum_ {\mathrm{Signal}} \frac {d _ {\mathrm{Signal} , i j t} \mathrm{MSignal} _ {i j t}}{\sigma_ {\mathrm{Signal}} ^ {2}} \right] \cdot \sigma_ {Q, i j t} ^ {2}\tag{4}
$$

and

$$
\sigma_ {Q, i j t} ^ {2} = \left[ \frac {1}{\sigma_ {Q , i j , t - 1} ^ {2}} + \sum_ {\mathrm{Signal}} \frac {d _ {\mathrm{Signal} , i j t}}{\sigma_ {\mathrm{Signal}} ^ {2}} \right] ^ {- 1}.\tag{5}
$$

## 4.4. Decision-Making Process

Individual drivers make decisions based on their expectation of the utility (McFadden 1974) as conditional on their information knowledge at time t (denoted as Info i, t ):

$$
\begin{array}{r l} & U _ {i j} | \mathrm{Info} (i, t) = E \big (U _ {i j t} \big) \\ & \qquad = \alpha Q _ {i j t} + \beta \mathrm{Loc} _ {j} + \gamma \mathrm{T} _ {t} + \delta \mathrm{Loc} _ {j} \cdot \mathrm{T} _ {t} + \varepsilon_ {i j t}. \end{array}\tag{6}
$$

We then define the choice set $J _ { j = ( l , \tau ) } = \{ k | k = ( l _ { k } , \tau _ { k } ) , \forall l _ { k } \} _ { }$ where $\tau _ { k }$ is the projected future arrival time at location $l _ { k }$ after accounting for the driving time from l to $l _ { k } .$ Note that by modeling the choice set as a combination between each potential location and its associated future arrival time (rather than the current time), we aim to account for the potential opportunity cost of driving to a destination in real-time decision making. Empirically, the size of a choice set is the same as the spatial dimension $N _ { L }$ , and the only difference is that in a choice set, we have to consider the corresponding driving time from the current location to any location defined in the spatial set. The outside option is defined as taxi drivers’ decisions about not driving at the given time stamp. Following the classic model for consumer choice (McFadden 1974) and normalizing the utility of the outside option to zero, we model drivers’ decision-making process as a multinomial logistic model with the following probability:

$$
\operatorname * {P r} (k | j) = \frac {e ^ {\alpha Q _ {i j t} + \beta \mathrm{Loc} _ {j} + \gamma T _ {t} + \delta \mathrm{Loc} _ {j} \cdot T _ {t}}}{1 + \sum_ {j ^ {\prime} \in J _ {j}} e ^ {\alpha Q _ {i j ^ {\prime} t} + \beta \mathrm{Loc} _ {j ^ {\prime}} + \gamma T _ {t} + \delta \mathrm{Loc} _ {j ^ {\prime}} \cdot T _ {t}}}.\tag{7}
$$

For better clarification, we provide a summary of all variables and notations in Table 1.

## 5. Data Processing

In this section, we discuss the details on how we process our large-scale raw GPS-trajectory data for extraction of important model-estimation variables.

## 5.1. Location–Time Set

In this study, our focal interest is urban taxi drivers who are eligible to drive within the urban area of the city.<sup>10</sup> We use Voronoi diagrams (Aurenhammer 1991) to partition the city plane (i.e., downtown and airport areas) into grids based on road intersections. In particular, each road intersection is assigned to a unique corresponding location grid. Any point within the grid is closer to the corresponding intersection than to other intersections (Okabe et al. 2009). We assume that drivers make decisions and update their knowledge of quality at the level of a location-grid unit. In total, we have 15 location grids. In the temporal dimension, for the purpose of computational feasibility, we classify each day, based on the general law of commuting in this city, into four time slots: midnight (12–7 a.m.), rush hour (7–9 a.m. and 5–7 p.m.), daytime (9 a.m.–5 p.m.), and evening (7 p.m.–12 a.m.).<sup>11</sup> According to the preceding discussion, the total number of location–time sets is 60.

Note that because of the location–time constraint, in reality, when a taxi driver makes decisions about where to go next, not all 60 location–time sets are considered. For example, when a taxi is empty at location A (in Figure 2) at 6 p.m. (i.e., the corresponding time slot is rush hour), the driver evaluates the driving time from location A to all of the potential 15 location grids. Take location E as an example: if the driving time from A to E is two hours, the alternative to E in the driver’s consideration set includes $\scriptstyle \mathrm { { E , } }$ evening only, because when the driver arrives at $\scriptstyle \mathrm { \mathrm { E } } ,$ it would be 8 p.m., the corresponding time slot of which is evening rather than rush hour. Notably, to account for the opportunity cost of driving to a certain location, the time considered in the location–time choice set for a driver is not the current decision-making time stamp but instead the projected arrival time if the driver were to drive to the corresponding location from the current location.

Table 1. Summary of Model Parameters

<table><tr><td>Notation</td><td>Explanation</td></tr><tr><td> $t$ </td><td>The time unit of a driver&#x27;s decision making</td></tr><tr><td> $j = (l, \tau)$ </td><td>Index of a location–time set with spatial and temporal units  $l$  and  $\tau$ </td></tr><tr><td> $N_{L}, N_{T}$ </td><td>Spatial and temporal dimensions in choice set definition</td></tr><tr><td> $Q_{j}$ </td><td>True quality of location–time set  $j$ </td></tr><tr><td> $Q0$ </td><td>Individual&#x27;s initial prior mean of quality</td></tr><tr><td> $\sigma^{2}_{Q0}$ </td><td>Individual&#x27;s initial prior variance of quality</td></tr><tr><td> $Q_{ijt}$ </td><td>Driver  $i'$ &#x27;s knowledge about quality in set  $j$  at time  $t$ </td></tr><tr><td> $\sigma^{2}_{Q,ijt}$ </td><td>Driver  $i'$ &#x27;s posterior variance of quality</td></tr><tr><td> $d_{\text{Signal},ijt}$ </td><td>Indicator of driver  $i'$ &#x27;s receiving signals of set  $j$  at time  $t$ </td></tr><tr><td> $\sigma^{2}_{\text{Signal}}$ </td><td>The variances of signals</td></tr><tr><td> $T_{t}$ </td><td>Time-varying factors at time  $t$ </td></tr><tr><td> $\alpha, \beta, \gamma, \delta$ </td><td>Weights to be estimated in utility function</td></tr></table>

Figure 2. (Color online) Geographic Distribution of Sampled Location Grids  
![](/api/attachments/WYF5N7ZC/fulltext/images/a0667272d99d081d186619971f3debe4ce08fc0b9ac70c06f273b58c277c8f7a.jpg)  
Note. The lines are streets; the points are the centers of the respective location grids.

In our empirical setting, we assume that taxi drivers make driving decisions if and only if their taxi is empty. In other words, when a taxi becomes empty, the driver needs to choose to which location grid to go. Without loss of generality, we assume that a driver makes this decision when a trip ends. Because we observe the actual location at which the driver picks up the next passenger, we use this observed information as the decision choice the driver makes when the taxi is empty.<sup>12</sup>

## 5.2. Heterogeneity in Driver Type

To better capture heterogeneity in driver experience, following prior literature (Haggag et al. 2017), we consider two types of drivers: new and experienced. Specifically, we assume a driver to be new when the driver has no record before August 20, 2009. In the Asian city, taxi drivers are mostly full-time drivers. Hence, if they had not worked for three weeks, they are likely to have entered the taxi workforce in Sep tember 2009 as new and inexperienced.<sup>13</sup> Considering that drivers with different levels of experience might behave very differently in their learning and decisionmaking processes, in our model, we allow for such heterogeneity and model the set of parameters to be driver type specific. Inspired by the method in Shin et al. (2012), we used driver behavior from the previous month to recover the prior value for experienced drivers (which distinguishes the experienced drivers from the new drivers). In particular, to impute the initial state of experienced drivers at the beginning of September 2009, we followed Erdem and Keane (1996) by preestimating drivers’ beliefs based on the common prior and average numbers of signals in August 2009. Then we used an individual’s imputed posterior mean and variance as the driver’s prior knowledge on September 1, 2009. In total, we have 263 new taxi drivers and 2,204 experienced drivers, which give a total of 172,515 observations from new drivers and 1,737,813 observations from experienced drivers for our empirical estimation.<sup>14</sup>

## 5.3. Signals

One advantage of our data set is that based on all the taxi traces, we are able to recover the off-line demand signals to which a driver is exposed while driving. Such off-line demand information allows us to better understand the overall decision process of a driver at a much finer level (i.e., minute or second level). Note that this granular off-line information usually goes unobserved in the conventional decision-analytics setting. For example, without the taxi GPS-trajectory data, documenting how many other taxis drove by or stopped to pick up or drop off a passenger while a taxi driver was driving and at what time and location would not be feasible. Understanding whether and how a taxi driver might use such observed information on the road for real-time decision making also would be difficult. Specifically, we consider seven information signals that carry benefit or cost information for a driver to evaluate the quality of a location–time choice. 15

## 5.3.1. Signal De<sup>fi</sup>nitions.

5.3.1.1. Pickup Signal. It is intuitive that if a location has more pickups within a given time period, it indicates higher demand from that location in that time period. Hence, a driver gains a higher benefit. Pickups in a given location–time set are generated by all drivers within that location during that time. With this understanding, we propose our first signal, the pickup signal, to which a taxi driver is exposed if the driver observes a pickup from other drivers or from the driver himself or herself.

5.3.1.2. Drop-Off Demand Signal. A previous drop-off can indicate a potential future pickup in the same location. For example, a consumer might go to a shopping mall at 7 p.m. and spend around three hours there. Thus, the drop-off at 7 p.m. might lead to future demand at 10 p.m. To capture such potential temporal correlation in demand distribution, we consider a second benefit-related signal, the drop-off demand signal. Specifically, suppose that driver i passes location l and observes drop-off(s) from others at time t (and the corresponding temporal unit of choice set is $\tau _ { 0 } )$

Driver i would update knowledge about quality in location–time set j, where $j = ( l , \tau )$ is a combination of the same location l and a future time slot τ. Here $\tau = \tau _ { 0 } + \Delta$ where Δ is the time gap between the current drop-off and the future pickup $\left( \mathrm { e . g . } , \Delta = 3 \right.$ hours as in the previous example between 7 and 10 p.m.). Note that in the real world, taxi drivers might not know exactly how each current drop-off will transform into a future pickup. However, we assume that a driver has some ex ante knowledge of the prob ability distribution of Δ. We use historical data to recover the empirical distribution of the future pickup probability conditional on the current drop-off.<sup>16</sup>

5.3.1.3. Trip-Income Signal. Every time a trip completes, taxi drivers have a new observation of trip income for a given location–time set j. They then need to decide whether this new observation is useful or not to their learning process. To model this informationupdating process, we allow each driver to use the new trip income as a signal to update knowledge if and only if this trip income is different from the driver’s prior expectation. In other words, we assume that the probability (denoted as $P _ { i , \mathrm { T I } } ( \mathrm { T I } _ { i j t } ) )$ of updating the quality prior to using the trip-income signal depends on the difference between the observed and expected trip income. The larger the difference, the higher is the probability.

5.3.1.4. Drop-Off Cost Signal. When a trip ends, the vacant taxi immediately becomes a competitor of nearby taxis. Hence, real-time drop-offs can be a supply-side indicator: more drop-offs in a location at the same time indicate more intense competition, which, in turn, can increase nearby drivers’ costs in searching for demand within the same location. Hence, we consider a drop-off cost signal, which helps drivers update their knowledge about the quality of a given location–time set.

5.3.1.5. Vacant-Taxi Signal. Observing a vacant taxi driving by or parking nearby can also be valuable to a taxi driver because from that observation, the driver can infer the intensity of competition nearby. In particular, drivers with vacant taxis nearby might cruise or park around the same area, trying to find passengers. Hence, this information is a quality indicator that reveals potential cost.

5.3.1.6. Waiting-Time Signal. We define the time gap between the end of the previous trip and the start of the current trip as a driver’s waiting time, which can help the driver to evaluate knowledge about cost in the given location–time set j. In our model, similar to the trip-income signal, we allow each driver to use the actual observed waiting time as a signal to update knowledge if and only if this value is different from the driver’s prior expectation. We use $P _ { i , \mathrm { W T } } ( \mathrm { W T } _ { i j t } )$ as the updating probability prior to using a waitingtime signal.

5.3.1.7. Speed Signal. Traffic conditions might also provide useful information to drivers’ evaluation of their knowledge about quality. A bad traffic condition (e.g., with traffic jams or accidents) might prolong a route and reduce the number of trips a driver can potentially make. To capture this information, drivers can use their real-time driving speed to evaluate the traffic conditions in a given location–time set. Similarly, we assume that each driver uses the actual observed speed as a signal to update knowledge if and only if this value is different from the driver’s prior expectation. Hence, the updating probability, denoted as $P _ { i , \mathtt { S P } } ( \mathtt { S P } _ { i j t } )$ , depends on the difference between the observed and expected driving speeds.

## 5.3.2. Signal Extraction

We use GPS-trajectory data to extract all the potential activities of a driver and of other peer drivers that could have been observed by the driver on the driving path. Note that although our empirical estimation focuses on the decisions from single-shift drivers only, we account for all taxis (both single shift and multishift) when extracting the information signals to recover the entire market activities in the city. We discuss the extraction details of these signals as follows.

Regarding pickup signal, vacant-taxi signal, drop-off cost signal, and drop-off demand signal, we extract them directly from the taxi GPS-trajectory data. We assume that when a driver observes any of these three activities (drop-off, pickup, vacant taxi drive-by) from any taxi driver (including the driver himself or herself) within the same location at the same time, the driver can gain some additional (but potentially noisy) knowledge about the quality in the local area during that time period. Specifically, we first extract a driver’s trajectory from the GPS-tracking data to summarize what location grid the driver drives by during each one-minute bin, which is the metaunit in our GPS trace data. Then, according to the definition of signals, a driver would only receive a signal if the corresponding activity occurs simultaneously. We define simultaneity here as the cooccurrence of activities within one minute of driving distance, which equals either a one-minute temporal gap or 500 m in spatial distance.<sup>17</sup> For example, we consider that the driver receives a pickup signal if he or she picks up a passenger or one or more pickup activities by other peer drivers occur simultaneously near the driver’s current location grid.

Note that, in reality, a driver might not always pay attention to activities on the road (e.g., because of neglect or cognitive limitation); hence, a driver might not always notice a peer activity nearby regardless of how precisely simultaneity is defined. Our model, however, is able to account for such a situation through signal variances $( \sigma _ { \mathrm { P i c k } } ^ { 2 } , \ \sigma _ { \mathrm { D D r o p } } ^ { 2 } , \ \sigma _ { \mathrm { T r i p } } ^ { 2 } , \ \sigma _ { \mathrm { C D r o p } } ^ { 2 } ,$ $\sigma _ { \mathrm { V a c a n t } } ^ { 2 } , \sigma _ { \mathrm { W a i t } } ^ { 2 } ,$ and $\sigma _ { \mathrm { S p e e d } } ^ { 2 } )$ . In this case, the corresponding estimated signal variance is large, suggesting that although the driver received the signal, the driver did not learn much from it.

Regarding trip-income signal, waiting-time signal, and speed signal, we extract them based on the following three steps. First, extract the observed actua value of the corresponding activities. Specifically, for the trip-income signal, we directly parse the trip income from our trip data every time a trip ends; for the waiting-time signal, we use the time gap between two consecutive trips as the waiting time; and for the speed signal, based on the trajectory information recorded in our GPS trace data, we derive the actual speed by dividing the travel distance by the travel time.<sup>18</sup> Second, compute the distribution of the difference between the expected and actual values. The expected value is measured based on the past average trip income, waiting time, and speed of each individual driver. Third, our data show that the distributions of the differences approximately follow a normal distribution (Figure 3). We then use the fitted normal distribution to derive the probability that drivers update their knowledge.<sup>19</sup>5.4. Extraction of Spatial and Temporal Variables

For each location, we extract two spatial features: airport indicator and POI density. The potential demand in the airport might be different from those in other areas. Hence, we aim to capture such heterogeneity using an airport indicator. The other variable we consider here is POI density. We count the number of POIs within each location grid and take a log transform to ensure that the value lies within a reasonable range. Additionally, we extract three temporal variables: weekend indicator, number of raining hours, and number of storms in a given day. These data were crawled from an online weather database (www.wunderground.com/). Table 2 presents our statistical summary.

## 6. Estimation and Identi<sup>fi</sup>cation

To estimate our model, we follow Erdem and Keane (1996) and apply the simulated maximum likelihood method. The Monte Carlo simulation draws random samples of signal value, which we use to apply the Bayesian updating rules to compute the utility and then to compute the simulated likelihood value. Note that in the model, we assume that signal value follows a normal distribution. Hence, in each iteration of our estimation, when calculating Equation (4), and in Section 5, we randomly draw a signal value for each signal from the corresponding distribution to get the value of information content MSigna $\boldsymbol { 1 } _ { i j t } .$ . This is a standard method for estimating a Bayesian learning model.

Figure 3. (Color online) Distributions of Differences Between Expected and Actual Value  
![](/api/attachments/WYF5N7ZC/fulltext/images/bd4358d725b2840c89fa31149c673c6047f9cd6ced7e8f156290f99fbb4745fb.jpg)  
Speed  
Notes. (a) Speed. (b) Waiting time.

The true value of unobserved quality $Q _ { j }$ is identified based on drivers’ steady-state behavior. In the Bayesian learning process, the beliefs $Q _ { i j t }$ evolve to the true value $Q _ { j } .$ . In the extreme case in which the state is stable, the belief is the true value. However, following the discussion in Ching et al. (2013), we cannot identify $Q$ and α simultaneously. To address this issue, we need to either fix $Q _ { j }$ for one alternative j (e.g., Erdem and Keane 1996) or fix the coefficient α (e.g., Hao et al. 2018). In this paper, we fix $Q _ { j }$ for one j. Based on Section $^ { 7 , }$ the sample likelihood function can be expressed as

![](/api/attachments/WYF5N7ZC/fulltext/images/5711e97973c3b16e9f8137bac455f4997943055dd2e0e2f3e8edfbf94d623792.jpg)  
Table 2. Statistical Summary  
Waiting Time

$$
\prod_ {k} \operatorname * {P r} (k | j) ^ {I \{Y _ {i t} = k \}},\tag{8}
$$

where $I \{ \}$ is an indicator function indicating whether the observed decision of individual i at time t is k or not.

As we discuss in Section 5, to control for driverlevel heterogeneity, we separate drivers into two types, experienced and new drivers, and assign to them different sets of parameters (i.e., utility weights and learning coefficients). The identification procedures for the two sets of parameters stay the same. Hence, we discuss parameter identification without referring to the specific driver type.

<table><tr><td>Variable</td><td>Definition</td><td>Mean</td><td>Standard error</td><td>Minimum</td><td>Maximum</td></tr><tr><td> $N_{PUa}$ </td><td>Number of pickup signals</td><td>4.6649</td><td>10.3182</td><td>0</td><td>1,777</td></tr><tr><td> $N_{CDO}$ </td><td>Number of drop-off cost signals</td><td>4.6732</td><td>10.3923</td><td>0</td><td>1,783</td></tr><tr><td> $N_{VT}$ </td><td>Number of vacant-taxi signals</td><td>5.2536</td><td>13.2245</td><td>0</td><td>2,378</td></tr><tr><td>POIDensity</td><td>(Log) Number of POIs within a location grid</td><td>4.3967</td><td>0.3745</td><td>3.5084</td><td>4.9140</td></tr><tr><td>TI</td><td>Trip income</td><td>30.4746</td><td>15.4434</td><td>12.5</td><td>210.3</td></tr><tr><td>WT</td><td>Waiting time, minutes</td><td>21.8925</td><td>13.7230</td><td>0</td><td>60</td></tr><tr><td>SP</td><td>Speed, km/h</td><td>20.5554</td><td>5.3205</td><td>0</td><td>81.4204</td></tr><tr><td>Weekend</td><td>Weekend indicator</td><td>0.2963</td><td>0.4653</td><td>0</td><td>1</td></tr><tr><td>Raining</td><td>Daily raining hours</td><td>1.3704</td><td>3.0778</td><td>0</td><td>14</td></tr><tr><td>Storms</td><td>Daily number of storms</td><td>0.1852</td><td>0.6225</td><td>0</td><td>3</td></tr></table>

Notes. In the estimation, we assume the same frequency of updating and decision making. In other words, every time a taxi becomes vacant, the driver updates knowledge first and then uses that new knowledge to make decisions. Therefore, we aggregate the number of signals received since the previous update.

The prior parameters $( Q _ { 0 }$ and $\sigma _ { 0 } ^ { 2 } )$ and signal variances $( \sigma _ { \mathrm { P i c k } } ^ { 2 } , \sigma _ { \mathrm { D D r o p } } ^ { 2 } , \sigma _ { \mathrm { T r i p } } ^ { 2 } , \sigma _ { \mathrm { C D r o p } } ^ { 2 } , \sigma _ { \mathrm { V a c a n t } } ^ { 2 } , \sigma _ { \mathrm { W a i t } } ^ { 2 } ,$ and $\sigma _ { \mathrm { S p e e d } } ^ { 2 } )$ capture how the arrival of signals changes the individual’s belief about the quality distributions $( \mathrm { i . e . } , \sigma _ { Q , i j t } ^ { 2 }$ and $Q _ { i j t } )$ . The preference parameter α captures the individual driver’s preferences in evaluating each location–time set. These two sets of parameters can be jointly identified because we observe the differences in individuals’ decisions as well as the differences in their decision changes over time. More specifically, individual preferences can be identified through variations in decisions from different drivers who had the same information set at a given time (i.e., same spatial and temporal features, same belief) but made different choices.

Additionally, for tractability in this study, we assume the prior mean and variance of the perceived distribution of the unobserved quality to be common across the same type of driver (i.e., new or experienced) and across locations. We identify them through the variations in the population-level average behavior change before and after receiving the signals. For example, if, after receiving a few pickup signals at a certain location and time, the driver’s probability of staying in this given location does not change significantly compared with the initial probability of staying before receiving any signal, then we can assume that the prior belief about quality is quite precise and that the prior variance is low. Moreover, we also observe variations in the average behavior change during early time periods when drivers might not receive any signal at all. This additional type of variation allows us to further pin down the prior variance. For example, if drivers’ behaviors change significantly even without being exposed to any information signal, the prior variance of their belief is likely quite high.

## 7. Empirical Results

In this section, we discuss our main empirical results. First, we discuss the parameter estimates in the utility function and in the learning process, respectively. Then we compare our model with other alternative models.

## 7.1. Estimation Results from Main Mode

Table 3 presents parameter estimates in the utility function (Section 1). Specifically, we have two spatial variables (i.e., POI density and airport indicator) and three temporal variables (i.e., weekend indicator, raining hours, and number of storms). We present the individual preferences of experienced and new drivers, respectively. We would like to highlight several interesting findings from this result table. First, POI density plays an important role in drivers evaluation of each location. POI density, to some degree, suggests the popularity of a given location. Hence, the positive estimate of $\beta _ { 1 }$ indicates that all drivers prefer seeking passengers in a popular location. Second, temporal factors, on average, do not have significant impacts on drivers’ evaluations of local quality. But when interacting with the airport indicator, the interaction effects become statistically significant. In particular, we find that compared with new drivers, experienced drivers are more likely to go to the airport and look for passengers during the weekend or on bad-weather days (e.g., rain or storms). In contrast, new drivers are more likely to drive to the airport during weekdays and less likely to do so in bad weather.

Next, Table 4 summarizes how different signals affect the learning processes of the two types of taxi drivers. First, the initial prior variance $\bar { \sigma } _ { 0 } ^ { 2 }$ shows a

Table 3. Parameter Estimates in Utility Function

<table><tr><td rowspan="2">Parameters</td><td colspan="2">Experienced drivers</td><td colspan="2">New drivers</td></tr><tr><td>Estimate</td><td>Standard error</td><td>Estimate</td><td>Standard error</td></tr><tr><td>Quality ( $\alpha$ )</td><td>0.1920</td><td>0.0830</td><td>0.1793</td><td>0.0023</td></tr><tr><td>POI density ( $\beta_1$ )</td><td>2.7062</td><td>0.0099</td><td>2.9873</td><td>0.0460</td></tr><tr><td>Airport indicator ( $\beta_2$ )</td><td>-0.0005</td><td>0.0450</td><td>1.1969</td><td>0.0678</td></tr><tr><td>Weekend indicator ( $\gamma_1$ )</td><td>-0.7751</td><td>5.2809</td><td>0.2578</td><td>3.8168</td></tr><tr><td>Raining hours ( $\gamma_2$ )</td><td>-0.2575</td><td>5.2810</td><td>-1.7732</td><td>2.2681</td></tr><tr><td>Number of storms ( $\gamma_3$ )</td><td>1.0240</td><td>5.1571</td><td>-0.1423</td><td>3.7344</td></tr><tr><td>Airport  $\times$  weekend ( $\delta_1$ )</td><td>0.2028</td><td>0.0715</td><td>-0.8887</td><td>0.0844</td></tr><tr><td>Airport  $\times$  raining ( $\delta_2$ )</td><td>0.0426</td><td>0.0087</td><td>0.0078</td><td>0.0082</td></tr><tr><td>Airport  $\times$  storms ( $\delta_3$ )</td><td>0.6762</td><td>0.0272</td><td>0.2370</td><td>0.0450</td></tr></table>

Note. Significant (95%) estimates are in bold.

Table 4. Parameter Estimates in Learning Process

<table><tr><td rowspan="2">Parameters</td><td colspan="2">Experienced drivers</td><td colspan="2">New drivers</td></tr><tr><td>Estimate</td><td>Standard error</td><td>Estimate</td><td>Standard error</td></tr><tr><td>Prior variance ( $\sigma_{0}^{2}$ )</td><td>0.0128</td><td>0.0102</td><td>1.0694</td><td>0.3989</td></tr><tr><td colspan="5">Signals with benefit information</td></tr><tr><td>Pick-up signal ( $\sigma_{\text{Pick}}^{2}$ )</td><td>1.0792</td><td>0.0032</td><td>0.7116</td><td>0.2378</td></tr><tr><td>Drop-off demand signal ( $\sigma_{\text{DDrop}}^{2}$ )</td><td>0.7075</td><td>0.0136</td><td>1.1073</td><td>0.4447</td></tr><tr><td>Trip-income signal ( $\sigma_{\text{Trip}}^{2}$ )</td><td>1.1738</td><td>0.0061</td><td>0.9583</td><td>0.0216</td></tr><tr><td colspan="5">Signals with cost information</td></tr><tr><td>Drop-off cost signal ( $\sigma_{\text{CDrop}}^{2}$ )</td><td>1.1025</td><td>0.0044</td><td>1.5003</td><td>0.5000</td></tr><tr><td>Vacant-taxi signal ( $\sigma_{\text{Vacant}}^{2}$ )</td><td>0.9198</td><td>0.0096</td><td>0.1457</td><td>0.0271</td></tr><tr><td>Waiting-time signal ( $\sigma_{\text{Wait}}^{2}$ )</td><td>0.5111</td><td>0.0341</td><td>0.4767</td><td>0.6976</td></tr><tr><td>Speed signal ( $\sigma_{\text{Cpeed}}^{2}$ )</td><td>0.8543</td><td>0.0059</td><td>0.9740</td><td>0.0347</td></tr></table>

Note. Significant (95%) estimates are in bold.

much lower estimate on experienced drivers than on new drivers. Because experienced drivers have been exposed to the taxi industry for a relatively longer time than new drivers, at the beginning of September 2009, experienced drivers were supposed to, on average, have a more precise knowledge about quality distributions than new drivers. Second, all of the information signals, on average, are more valuable to new drivers than to experienced drivers. In particular, our results show that the magnitudes of signal variances are closer to those of new drivers’ prior variance. Because, in Equations (4) and (5), all signal variances serve as denominators, a smaller value of variance would lead to a larger impact in the updating process. Hence, with everything else constant, if prior variance is much smaller than signal variance, signals are valuable to drivers’ learning processes and vice versa. Interestingly, we observe that new drivers are good at learning from simple signals (e.g., pickup signal, vacant-taxi signal), whereas experienced drivers do not seem to value simple information signals and, instead, are better at learning from the more complicated signals (e.g., drop-off demand signal). In terms of simple signals, drivers only need to observe how their peers behave and then directly infer quality information. On the contrary, with regard to complicated signals, such as the drop-off demand signal, drivers need to predict the correlation between current dropoff and future pickup, which requires more experience in signal processing.

As discussed in Section 5, we extracted 15 location grids and divided each day into four time slots. In total, then, we have 60 location–time sets. In Table 5, we first present the mean and variance of true value for each of the four time slots. For identification in our estimation, we normalize the quality of one grid to one as the baseline. Hence, all of the estimates’ values are relative to this baseline.<sup>20</sup> Overall, the estimated true value is consistent and appears valid because we observe the highest quality during rush hours and the lowest value around midnight. For example, a high average quality might come from two factors: one is the potentially high demand resulting from commuting needs (e.g., rush hours), and the other is the potentially low cost resulting from less competition (e.g., many scheduled shifts around 7 a.m. or 6 p.m., resulting in fewer available taxis) or better traffic conditions. Therefore, the average quality during rush hours is the highest because the demand is high when many taxis are doing the shift schedule, leading to a lower supply. To further illustrate the variation not only across time but also across locations, we also provide, in Table 5, the estimated true quality in two sample locations.

To further validate the robustness of our empirical findings, we conducted four additional empirical extensions, including the inclusion of risk factors, additional heterogeneous learning effects by temporal factors (i.e., weekend/weekday indicator and weather factors), an alternative choice set definition (i.e., considering smaller time slots as 15 minutes or one hour), and accounting for forward-looking behavior manners. All the results show consistency with our main findings. The details are provided in Section F of the online appendix.

## 7.2. Model Comparison

To examine whether includ-ing learning processes can better explain the drivers’ behavioral patterns we observe from the data, we first compare our full model with two alternative benchmark models that are widely used in similar scenarios to model individual choice: (1) a simple logit model without learn-ing signals and (2) a simple logit model with learning signals as input features. Furthermore, to evaluate the necessity of a Bayesian learning model, we compare our model with a two-stage decision-making model (i.e., selecting one of the four time slots as working hours and then choosing locations). We follow Lee et al. (2015) in estimating the two-stage model. In addition, we also consider two alternative learning models with different subsets of signals (i.e., benefit signals versus cost signals only). We compare the six models using the log-likelihood, Akaike information criterion (AIC) and the Bayesian information criterion (BIC), as shown in Table 6. We test for both in-sample and out-ofsample fits.<sup>21</sup> We find that our structural model with all information signals outperforms the other five alternative models. Not surprisingly, we also observe that including learning signals as model inputs improves model performance, which, in turn, illustrates the importance of real-time information signals in modeling driver decisions. Moreover, comparing with the two alternative learning models with subsets of signals, we demonstrate the value of both cost and benefit signals in modeling driver decisions. Detailed discussion and intuitions are provided in Section G of the online appendix.

Table 5. Estimates of True Quality Value

<table><tr><td>Time slots</td><td>Mean among locations</td><td>Standard deviation among locations</td><td>Location I</td><td>Location II</td></tr><tr><td>Midnight</td><td>-0.0790</td><td>4.0020</td><td>0.3813</td><td>1.0232</td></tr><tr><td>Rush hours</td><td>0.2129</td><td>1.6864</td><td>0.7267</td><td>0.9287</td></tr><tr><td>Regular daytime</td><td>-0.0784</td><td>3.6889</td><td>0.8127</td><td>1.3672</td></tr><tr><td>Evening</td><td>0.0333</td><td>2.8602</td><td>0.9156</td><td>-1.3188</td></tr></table>

## 8. Policy Simulations

We conduct several policy simulations to examine counterfactual effects. For each policy experiment, we simulate 1,000 iterations and calculate results by averaging across them. We discuss in detail each policy simulation in the following subsections.

The main outcome measure we considered in the simulation analyses is the model-predicted incomes for driver i in location–time set j at time t:

$$
\begin{array}{l} \text {Predicted\_Income} _ {i j t} \\ = \sum_ {k \in J (j)} \operatorname * {P r} (Y _ {i k t}) \times E (\text {Incomes} _ {k t}) \\ = \sum_ {k \in J (j)} \operatorname * {P r} (Y _ {i k t}) \times \operatorname * {P r} (\text {GetATrip}) _ {k} \\ \quad \times \text {AvgIncomePerTrip} _ {k t}, \end{array}\tag{9}
$$

where $\mathrm { P r } ( Y _ { i k t } )$ is the probability of moving to set $k ,$ which is the candidate set when drivers are at set j at time t. Note that in our counterfactual analyses, according to different information-sharing strategies, we changed the numbers of signals to which an in dividual is exposed. This leads to different simulated probability. To approximate $\operatorname* { P r } ( { \tt G e t A T r i p } )$ , we use TrueQuality , which represents the true quality in set k estimated from our model; AvgIncomePerTri $\cdot \mathrm { p } _ { j t }$ is the average per-trip income in location–time set j at time t and is observed from the data. Note that without loss of generality, we assume that the number of pickups in location–time set j at time t is linearly correlated with the local true quality. We compute the predicted driver incomes under information sharing. We then aggregate the predicted incomes over all drivers across location and time and compare the result with the observed total driver incomes at a daily level.

## 8.1. Information Sharing

In our model, we assume that drivers update their beliefs about the quality distribution only through the signals they observe on their own. However, because the taxi companies have access to drivers’ GPS traces, what would be the implications of taxi companies or sharing platforms (e.g., Uber and Lyft) broadcasting all information signals to everyone (so that the driv ers do not have to directly observe the signals by themselves)? Does this improve drivers’ decisionmaking efficiency? We run the simulations by allowing for information sharing with each of the signals separately. The results are shown in Figure 4.<sup>22</sup> In the four panels, the y-axis indicates the average daily model-predicted incomes (normalized to U.S. dollar values), and the x-axis indicates dates. In particular, Figure 4, (a) and (b), presents performance when broadcasting signals include cost information, and Figure 4, (c) and (d), shows results when broadcasting signals include benefit information. The dashed line in each plot denotes the base case without broadcasting. The four plots indicate that, on average, information sharing among drivers can increase driver income. For example, on average, we observe a 5.5% increase in

Table 6. Model Comparison

<table><tr><td rowspan="2"></td><td colspan="3">In-sample fit</td><td colspan="3">Out-of-sample fit</td><td rowspan="2">Number of parameters</td></tr><tr><td>-LL</td><td>AIC</td><td>BIC</td><td>-LL</td><td>AIC</td><td>BIC</td></tr><tr><td>Logit model without signals</td><td>431,775.38</td><td>431,791.38</td><td>431,827.03</td><td>446,372.82</td><td>446,388.82</td><td>446,424.47</td><td>8</td></tr><tr><td>Logit model with signals</td><td>374,785.03</td><td>374,815.03</td><td>374,881.87</td><td>386,951.28</td><td>386,981.28</td><td>387,048.12</td><td>15</td></tr><tr><td>Two-stage model</td><td>434,679.88</td><td>434,709.88</td><td>434,776.97</td><td>447,788.83</td><td>447,818.83</td><td>447,885.92</td><td>15</td></tr><tr><td>Cost signals only</td><td>239,676.58</td><td>239,850.58</td><td>240,238.24</td><td>241,187.81</td><td>241,361.81</td><td>241,749.47</td><td>87</td></tr><tr><td>Benefit signals only</td><td>227,127.32</td><td>227,297.32</td><td>227,676.06</td><td>229,670.40</td><td>229,840.40</td><td>230,219.14</td><td>85</td></tr><tr><td>Full model</td><td>223,127.42</td><td>223,313.42</td><td>223,727.81</td><td>225,855.80</td><td>226,041.80</td><td>226,456.19</td><td>93</td></tr></table>

Notes. LL, log likelihood; AIC, Akaike Information Criterion; BIC, Bayesian Information Criterion

(b)

Figure 4. (Color online) Broadcast Different Types of Information Signals  
(a)  
![](/api/attachments/WYF5N7ZC/fulltext/images/39e5406fb8812b3a3557c965c34acf5f8326c5188dbfb20a0dfc075865b300b7.jpg)  
Sharing of Cost Signals (I)

![](/api/attachments/WYF5N7ZC/fulltext/images/39f3cb13d0daceb222d8a6deeaacdf9f489df171a558e593eec2847d9ee6cb03.jpg)  
Sharing of Cost Signals (II)

(c)  
![](/api/attachments/WYF5N7ZC/fulltext/images/4e94bce3d316bb448f5699357446587fd75d774b02c3e6535a2d42713d3803b9.jpg)  
Sharing of Benefit Signals (i)

(d)  
![](/api/attachments/WYF5N7ZC/fulltext/images/a2ca20f9bb28f9de570fa0992eacb41e73c82b3c58f6c12da540fa91b3ce35e9.jpg)  
Sharing of Benefit Signals (II)  
Notes. (a) Sharing of cost signals (I). (b) Sharing of cost signals (II). (c) Sharing of benefit signals (I). (d) Sharing of benefit signals (II).

drivers’ daily income if we broadcast the drop-off demand signal among all taxi drivers. Moreover, the degree of increase varies among different information signals. Interestingly, a signal with a smaller value (i.e., a larger signal variance) at the individual level can be highly informative in improving drivers learning efficiency if we aggregate the signal volumes across all drivers. More specifically, first, Figure 4(a) shows that sharing the vacant-taxi signal is not so helpful, whereas sharing the drop-off cost signal can significantly increase drivers’ daily income by 4.17%. One reason for this finding is that a vacant taxi driving by or a vacant taxi parking nearby is a more frequent event than a taxi drop-off; hence, drivers are more likely to observe common signals, such as the vacanttaxi signal, by themselves even without receiving broadcast messages. In contrast, drivers would benefit much more from the broadcasting of signals that are initially rare and sparse, such as the drop-off cost signal. Second, Figure 4(b) shows that sharing the speed signal can lead to a 4.10% increase in driver income, whereas sharing the waiting-time signal is not so helpful.<sup>23</sup> Third, Figure 4, (c) and (d), also suggests that the drop-off demand signal is the most valuable to drivers among the three signals with demand information when broadcasting. Interestingly, we show in Table 4 that the value in the dropoff demand signal is smaller (i.e., with a higher estimated variance) than the other two demand signals at the individual level but that it becomes most valuable while being aggregated and shared among all drivers.

Overall, both Table 4 and Figure 4 suggest a consistent trend across signals: although an information signal might be noisy at the individual level, it can become highly informative after we aggregate it across individuals. Note that to reach these findings, we first need to know what exactly an individual driver truly observes in an off-line setting, which can only be inferred from a combination of both triprecord data and off-line trace data. This finding thereby reinforces one major advantage of our study that we are able to show the value of aggregating information—information that otherwise would have been unavailable within a traditional organizational setting—for improved decision making.

In addition, we take a further step by broadcasting different combinations of information signals. Our finding suggests that taxi drivers might not always benefit from a larger variety of information signals, especially when the noise of each signal is nonnegligible. The details are provided in Section H of the online appendix.

## 8.2. Effective Distance and Effective Frequency of Information Sharing

In the preceding subsection, we discussed the situations when broadcasting different information signals among drivers across all distance ranges. This strategy has the potential to significantly improve drivers’ predictions of taxi demand, but it might be costly in operation, and moreover, individual drivers are also unlikely to efficiently handle a large volume of information at once because of cognitive limitations. Thus, we conduct further policy simulations by exploring the effective distance and effect frequency of information sharing. We find that the value of information does not increase monotonically with the scale (distance) and frequency of information sharing. Also, we find that the optimal effective distance and optimal frequency of information sharing vary among different signals. Therefore, organizations and platforms must understand the incremental value of acquiring larger-scale information across spatial and temporal dimensions in order to better facilitate decision making. We provide detailed analyses and results in Sections I and J of the online appendix.

## 8.3. Welfare Implication

In previous subsections, we discussed the driver income improvement potentially obtainable by information sharing. In this section, we discuss the associated welfare implication.

It is clear that at the individual level, holding everything else constant, information sharing can potentially improve an individual driver’s income through improved decisions. For example, with better knowledge about the true unobserved quality (Q ), a driver now is likely to choose a location with a higher probability of picking up a passenger while accounting for the expected costs. However, at the population level, the mechanism of the overall driver income increase is not fully clear. In particular, from a welfare perspective, does the overall income increase come from a redistribution among different drivers (e.g., shifting highincome drivers’ incomes to low-income drivers or vice versa)? Or does it come from a potential expansion in the market size (i.e., with information-sharing drivers now able to capture previously unserved demand in the market)?

Theoretically, our model assumes, over time, that drivers learn the true unobserved quality Q of each location–time set. Importantly, the true unobserved quality, which is carried through various information signals, would cover both served and unserved demand information in the market. For example, some accidentally unserved demand on one day may likely be served on other day(s) if the same (or similar) demand is recurring over time.<sup>24</sup> Therefore, learning Q enables drivers to account for such unserved demand during the decision-making process. Besides, with better knowledge about the distribution of the true unobserved quality in the city, it is possible that some drivers who previously chose the outside option (i.e., did not pick any location and stopped working) now may choose the inside option instead. This means that the potential excess capacity of drivers, which did not get used previously to pick up pas sengers, now can be devoted to picking up the additional unserved demand. If this is the case, then we would expect an overall increase in driver welfare because of market expansion. Empirically, we would expect, after information sharing, a lower predicted share of outside options (higher total share of inside options) from all drivers.

To examine the welfare implication, we conduct an additional analysis. We compare the observed number of trips at each location and time with the number of drivers who are predicted to go to the corresponding location at that time based on the modelpredicted likelihood of picking up passengers under various information-sharing strategies. We then aggregate across all location–time sets (i.e., inside op tions) in the city to calculate the total observed and predicted market sizes.<sup>25</sup>

Table 7 shows the increases from the total observed market size to predicted market size when we broad cast each of the seven signals. As seen, with informationsharing strategies, approximately 2% more drivers choose to participate in the market (who previously chose the outside option), implying that the previously unserved demand will likely be served by this excess supply capacity, and the total welfare is improved.<sup>26</sup> Overall, our study provides important evidence that efficient information sharing can lead to a welfare increase among drivers resulting from potential market expansion. Efficient information sharing can generate, within the taxi market, additional income that otherwise could be missed.

## 8.4. Heterogeneity in Welfare Impact

To further examine whether the overall income increase comes from a redistribution among different drivers, we separately looked into two types of drivers based on their historical behavior: (1) highincome drivers, drivers with the top 20% highest hourly income, and (2) low-income drivers, drivers with the bottom 20% lowest hourly income.<sup>27</sup> Then we ran simulations by broadcasting each of the seven signals separately and predicted the average daily income per driver for the two types of drivers, respectively. The results are shown in Figure 5 (we plot the detailed trends Section K of in the online appendix).

Table 7. Welfare Impact Analysis

<table><tr><td>Broadcasting</td><td>Market size changes, %</td><td>Broadcasting</td><td>Market size changes, %</td></tr><tr><td>Pick-up signal</td><td>2.31</td><td>Drop-off cost signal</td><td>2.35</td></tr><tr><td>Drop-off demand signal</td><td>2.34</td><td>Vacant-taxi signal</td><td>2.27</td></tr><tr><td>Trip-income signal</td><td>2.28</td><td>Waiting-time signal</td><td>2.28</td></tr><tr><td>Optimal case(with precise knowledge)</td><td>2.40</td><td>Speed signal</td><td>2.28</td></tr></table>

Interestingly, our findings suggest that both highand low-income drivers would benefit, in the form of higher overall income, from information sharing. If we compare performance between the high- and lowincome drivers, among all seven signals, we find that low-income drivers can benefit slightly more from broadcasting than can high-income drivers. For example, when broadcasting the speed signal, highincome drivers, on average, can benefit from a 5.08% income increase, whereas low-income drivers receive only a 3.59% increase. And when broadcasting the tripincome signal, low-income drivers’ daily income increases by 3.77%, which is less than high-income drivers’ 5.03% increase. Moreover, as shown in Section I of the online appendix, we also find consistent evidence in the potential market expansion from both types of drivers. In particular, we find an increase for both types of drivers in the number of drivers who switch from the outside option to the inside option after information sharing. We also find that such an increase is higher for low- compared with high income drivers.

## 9. Conclusion and Discussion

The main goal of this paper was to understand human behavior and decision making by learning from largesale, fine-grained, digitalized off-line trace data. We instantiate our study by analyzing taxi trace data in order to understand drivers’ learning behavior for local demand and to recover the value of information signals extracted from the off-line traces. We propose and estimate a structural model for understanding of individual drivers’ heterogeneous learning behaviors. We validate our model using a combination of three large, unique data sets containing approximately 2 million fine-grained GPS observations from 2,467 single-shift taxi drivers driving in a large Asian city for August and September 2009.

Our empirical analyses indicate strong heterogeneity between new and experienced taxi drivers in both the value of information and individual drivers learning behavior based on this information. Interestingly, we find that straightforward information signals have little value for drivers seeking to gain competitive power. Instead, experienced drivers benefit largely from the ability to learn from more complex information. Our policy-simulation results show that by aggregating the information extracted from the off-line behavior traces on a large scale, individual drivers’ decision-making efficiency can be significantly improved. Interestingly, we find that information that is noisy at the individual level can become more valuable after it is aggregated across various spatial and temporal dimensions. We also find that the marginal value of aggregating larger-scale information varies among the different information types.

Figure 5. Comparison of High-Income with Low-Income Drivers  
![](/api/attachments/WYF5N7ZC/fulltext/images/451f61fa474fc8c60564018b703a8558204ecd9804c1c26ef7a79bdd28439bcd.jpg)

Our study demonstrates the value of extracting behavioral patterns from granular off-line trace data to the understanding and improvement of human decision making. In particular, by collecting and analyzing the new source of off-line behavior traces, we were able to leverage information that is often unavailable to individuals or organizations in the conventional setting. In the broader perspective, this work demonstrates the potential of combining largescale temporal and spatial data mining together with econometric structural models and Bayesian statistics for better understanding of human decision making. With the growing ubiquity of individual-level mobile and sensor technologies, more and more human behavioral information is digitalized and associated with location and time stamps. Certainly, our study can provide a foundation on which future studies can build. Our methodologies can be generalized to other types of vehicle-for-hire demand estimation (e.g., Uber/Lyft) or, more broadly, to other off-line settings beyond the taxi industry (e.g., sensor-generated data, Internet-of-Things).

Our paper provides several managerial implications. First, our model framework about drivers learning procedure and decision-making process can be generalized to the emerging mobile transportation fields, such as ridesharing platforms and autonomous vehicles. For example, our model and results suggest the effectiveness of different types of information signals along with a driver’s driving trajectory as well as efficient strategies about how to aggregate different types of information from a control center/ platform perspective. Such results would be helpful in improving ridesharing drivers’ decisions during idle time between trips. For example, the ridesharing platforms could use their mobile data to collect the corresponding signals and broadcast them (or the most effective ones) to individual drivers who might not be able to efficiently make decisions about where to go. This, in turn, would also help increase the platform revenue because the daily income gained by individuals has proved to increase significantly from our empirical results. Second, notable policy implications extend from our study. Our welfare analysis in the policy-simulation part suggests the effectiveness of information sharing across drivers, especially for low-income drivers. This finding is valuable for mobile transportation companies or related departments to offer corresponding information-sharing strategies so that it would better help less experienced or less incentived drivers (who potentially earn less) improve their working performance, which, in turn, increases the matching efficiency between passengers and drivers. Again, this finding also provides helpful insights for ridesharing platforms. Specifically, given the natural advantages in collecting aggregated-level driver behavior–related signals from their apps, the platforms can selectively broadcast signals to drivers with low experience or incentive levels to encourage them to make better decisions. Not only can this help drivers increase their daily income, but it also allows them to address the potential long waiting time in selected areas or time windows.

Our paper has several limitations that can serve as guidelines for future research. First, incorporating more individual driver-level characteristics, such as past driving experience, family background, and company resources, would be interesting. Second, in our analysis, we assumed independent driver decision mak ing and did not consider drivers’ strategic behavior (e.g., decisions based on expectations of what others might do). Liu and Whinston (2019) propose a new analytical framework to analyze such strategic behavior across autonomous vehicles. Unlike robots, human drivers have more heterogeneity in terms of preferences and abilities. Thus, future studies would be interesting in modeling human drivers’ strategic behavior under a game-theoretic framework. Third, our data cover a two-month period. Unfortunately, we do not have access to additional data (i.e., longer periods or other cities). We acknowledge that the current data set might not be most ideal, but re searchers have no ultimate control over corporate partners. Finally, looking into demand shocks in the market and examining how they might affect the tax industry at the individual-driver level would be interesting. For example, the introduction of Uber-type services and e-hail mobile apps has significantly affected taxi markets. Our insights and structural modeling framework have the potential to be applied in these settings as well.

## Acknowledgments

For helpful comments, the authors thank seminar participants at Carnegie Mellon University, New York University, The University of Texas at Dallas, and National University of Singapore for helpful comments. They also thank participants at 2015 ICIS conference, 2015 Workshop on Information Technology and Systems (WITS), 2016 SCECR conference (Statistical Challenges in Electronic Commerce Research), 2017 Conference on Information Systems and Technology, and 2017 Workshop on Information Systems and Econom ics (WISE).

## Endnotes

<sup>1</sup> This information is available at http://www.nyc.gov/html/tlc/ downloads/pdf/2016\_tlc\_factbook.pdf.

<sup>2</sup> This information is available at http://life.china.com.cn/2015-12/ 28/content\_37408261.htm.

<sup>3</sup> This is one limitation of our study because our data cover a twomonth period. Unfortunately, we do not have access to additional data (i.e., longer periods or other cities). We acknowledge that the current data set might not be most ideal, but researchers have no ultimate control over corporate partners.

<sup>4</sup> Note that our data came from 2009 when neither mobile hailing apps nor a calling system was used in the market. Thus, the pickup locations we observe from the data are the actual choice that the driver made rather than coming from the passengers’ request.

<sup>5</sup> Note that although taxi-hailing mobile apps are quite popular today, people rarely used them in 2009. Thus, they are not the focus of this paper. However, our methods and analyses have the potential to be generalized to the more recent taxi market as well. For example, our analyses could improve taxi-hailing services today by recommending better-personalized taxi demand information to individual drivers.

<sup>6</sup> One potential limitation of our data is that we do not observe the potential “unserved” demand. That is, if a customer wanted to hail a taxi but did not find one, we would not observe such demand in our data. We also do not observe the actual waiting time of passengers. Hence, we do not know exactly when and where a customer’s demand first initiated. Such data limitation is common across all the existing studies on the taxi market (e.g., Buchholz 2015, Salz et al. 2019). However, we are able to observe all the “served” demand; in other words, as long as customers did not switch to an alternative transportation mode (e.g., walking, bus), we would be able to observe their demand at a certain time (i.e., customers who wait longer are captured by demand at a slightly later time). Therefore, notwithstanding this potential limitation, our data provide us with a close approximation of the overall taxi demand in the city.

<sup>7</sup> In our empirical analysis, we focus on the decision-making behavior of single-shift drivers only. Our data also contain taxis with multiple drivers (multishift). We identify multishift versus single shift based on driver names associated with each taxi (which are available in the data). Note that although we do not focus on modeling the decision processes of the multishift taxi drivers, we account for market activities from all taxis in the market when extracting information signals such as pickups, drop-offs, or drive-bys to recover demand from the entire market. We further elaborate how we extract various information signals from GPS trajectories of all taxis in the market in Section 5.3.

<sup>8</sup> This information is available at http://www.nyc.gov/html/tlc/ html/about/trip\_record\_data.shtml.

<sup>9</sup> The normal distribution in modeling drivers’ prior and signal values is a typical assumption in prior literature (e.g., Erdem and Keane 1996, Ching et al. 2013, Huang et al. 2014, Hao et al. 2018) mostly for computational tractability while still preserving generalizability. In our paper, we build on prior literature in learning and follow the classical normal assumption in our model. There are several ad vantages about this assumption: first, the nature of Bayes’ rule allows us to easily connect drivers’ prior and posterior with their received signals; second, the normal distribution allows us to capture the potential noise and values contained in each signal.

<sup>10</sup> The reason we did not consider the suburban area is that only the taxis with urban tags can operate within the urban area. The taxis without urban tags were not allowed to enter the urban area because of some policy issues. And the pricing mechanisms were significantly different between the two types of taxis. To avoid any potential noise and confusion, we consider only the taxis with urban tags and analyze their behavior within the urban area, although our proposed model is applicable to any context with which a taxi driver is faced.

<sup>11</sup> This definition is based on the general commuting patterns within the Asian city. We also tried alternative definitions of time slots in modeling choice sets, and we found that our results stayed qualitatively consistent. The results are available from the authors upon request. We also illustrate the driving patterns among the 15 locations in Section B of the online appendix.

<sup>12</sup> From our GPS trace data, we cannot tell where the driver actually planned to go. We can only observe where the driver ended up picking up a passenger. We acknowledge this as a potential limitation of ou data. However, inferring behavioral preferences from observed choices is a common solution in all archival data analyses.

<sup>13</sup> We also tried other cutoff points, such as August 15 and 31, the results for which showed qualitative consistency.

<sup>14</sup> We provide some model-free evidence on the distribution of driver heterogeneous behavior in Section C of the online appendix.

<sup>15</sup> The selection of signals is based on an in-person interview with a random sample of taxi drivers. We also conducted a set of modelfree evidence and reduce-form analysis to ensure the validity of the signals. The details are provided in Sections D and E of the online appendix.

<sup>16</sup> In detail, given that the temporal dimension of our choice set is $N _ { T }$ (i.e., N is the number of time slots in the choice set), we create $N _ { T }$ pickup vectors and N drop-off vectors for each location. In the vectors, each element records the number of pickups/drop-offs within each location–time set in each day. Then, for each location, we compute the correlations between the drop-off vector in one time slot and the pickup vector in future time slots. Finally, we use these correlations to generate the distribution of future pickups conditional on the current number of drop-offs. We normalize each correlation b the aggregated correlation value in each location–time set.

<sup>17</sup> One minute is the finest grain of observation in our data. For a robustness check, we also tried different definitions of simultaneity, such as 5- or 10-minute driving radius. We find that our main results remain qualitatively consistent. Detailed estimation results are available from the authors upon request.

<sup>18</sup> The time window that we use to derive driving speed is the time gap between the starts of two consecutive trips.

<sup>19</sup> For example, if the fitted normal distribution is $N ( \mu , \sigma ^ { 2 } )$ and the actual difference is x, the approximate probability is given by $1 - 2 \times \mathrm { C D F } _ { N ( \mu , \sigma ^ { 2 } ) } ( - | \mathbf { x } - \mu | )$

<sup>20</sup> As Erdem and Keane (1996) point out, the statistically significant levels of these estimates are not a critical issue; rather, their relative scales are.

<sup>21</sup> Specifically, we randomly selected 500 drivers with a total of 810,000 observations to conduct the model comparison experiment. We randomly partitioned this sample by drivers into 50% training sample (observations from 250 drivers) and 50% testing sample (observations from the other 250 drivers). The in-sample fit was calculated based on the training sample, and the out-of-sample fit was calculated using the testing sample.

<sup>22</sup> As we discuss in Section 7, signals are more valuable to new drivers than to experienced drivers when compared with the latter’s prior knowledge. Hence, Figure 4 only shows the performance within the group of new drivers. We also test the performance among experienced drivers, but the results show that broadcasting signals does not have significant impacts on experienced drivers’ learning procedure.

<sup>23</sup> Compared with the actual speed, the actual waiting time a driver observes might be more subjective. For example, even within the same location grid during the same time slot, waiting time might significantly vary among drivers depending on driver experience (in which case, however, speed is less likely to vary significantly among drivers regardless of driver experience because of the relatively stable traffic condition). Therefore, when the information signal itself becomes highly subjective, the likelihood that drivers use it for updating their knowledge becomes less reliable, leading to a low value of broadcasting such signals.

<sup>24</sup> The stochastic randomness in drivers’ decision-making processes leads to the fact that drivers may make better decisions on some days than others. Hence, even consistent daily demand might be accidentally missed on some days.

<sup>25</sup> Note that the predicted total number of drivers who choose the inside option is a supply-side approximation of the predicted market size. The two are equal when all the supply capacity is fulfilled with demand. We acknowledge that because of data limitations, we do not observe the demand-side capacity $( \mathrm { i . e . , }$ how many customers are actually waiting to find a taxi). However, based on our model assumption, drivers choose to go to a location for a reason: because of the highest possibility of finding demand after accounting for the expected competition and cost. Therefore, it is likely that the supply is fulfilled. In particular, beyond the observed supply capacity that already matches with the currently observed (served) demand, the predicted excess supply capacity is likely to be fulfilled (or partially fulfilled) with the additional unserved demand. In a follow-up sensitivity analysis, we also tested scenarios in which only a proportion of the predicted excess supply capacity is fulfilled with de mand. In that case, we still find a consistent welfare implication. The results are available from the authors upon request.

<sup>26</sup> In Section I of the online appendix, as a robustness check, we also compared the changes of predicted market shares (instead of market size) before and after information sharing. The results are qualitatively consistent.

<sup>27</sup> We also considered different percentiles (30%, 40%, 50%) and found the results to be very consistent.

## References

Ackerberg DA (2003) Advertising, learning, and consumer choice in experience good markets: An empirical examination. Internat. Econom. Rev. 44(3):1007–1040.

Andrews M, Luo X, Fang Z, Ghose A (2015) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Aral S, Brynjolfsson E, Van Alstyne M (2012) Information, technology, and information worker productivity. Inform. Systems Res. 23(3, pt. 2):849–867.

Athey S (2015) Machine learning and causal inference for policy evaluation. Proc. 21st ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Computing Machinery, New York), 5–6.

Aurenhammer F (1991) Voronoi diagrams: A survey of a fundamental geometric data structure. ACM Comput. Surveys 23(3):345–405.

Bakos Y, Katsamakas E (2008) Design and ownership of two-sided networks: Implications for internet platforms. J. Management Inform. Systems 25(2):171–202.

Balafoutas L, Beck A, Kerschbamer R, Sutter M (2013) What drives taxi drivers? A field experiment on fraud in a market for credence goods. Rev. Econom. Stud. 80(3):876–891.

Bargh JA, Chartrand TL (1999) The unbearable automaticity of being. Amer. Psych. 54(7):462–479.

Bhargava HK, Choudhary V (2004) Economics of an information inter mediary with aggregation benefits. Inform. Systems Res. 15(1):22–36.

Brennan A (2014) Taxi & Limousine Services in the US. IBISWorld Industry Report 48533, IBIS World, Los Angeles. Available at https://www.ibisworld.com/united-states/market-research -reports/taxi-limousine-services-industry/.

Buchholz N (2015) Spatial equilibrium, search frictions and efficient regulation in the taxi industry. Working paper, The University of Texas at Austin, Austin.

Buchholz N, Shum M, Xu H (2016) Semiparametric estimation of dynamic discrete choice models. Working paper, The University of Texas at Austin, Austin.

Camerer C, Babcock L, Loewenstein G, Thaler R (1997) Labor supply of New York City cabdrivers: One day at a time. Quart. J. Econom. 112(2):407–441.

Chen MK, Sheldon M (2016) Dynamic pricing in a labor market: Surge pricing and flexible work on the Uber platform. Proc. 2016 ACM Conf. Econom. Comput. (EC ’16) (ACM, New York), 455.

Ching AT, Erdem T, Keane MP (2013) Invited paper: Learning models: An assessment of progress, challenges, and new de velopments. Marketing Sci. 32(6):913–938.

Choi J, Bell DR, Lodish LM (2012) Traditional and IS-enabled customer acquisition on the internet. Management Sci. 58(4): 754–769.

Cramer J, Krueger AB (2016) Disruptive change in the taxi business: The case of Uber. Amer. Econom. Rev. 106(5):177–182.

Crawford VP, Meng J (2011) New York City cab drivers’ labor supply revisited: Reference-dependent preferences with rational expectations targets for hours and income. Amer. Econom. Rev. 101(5):1912–1932.

DeGroot MH (2005) Optimal Statistical Decisions, vol. 82 (John Wiley & Sons, Hoboken, NJ).

Dubé JP, Sudhir K, Ching A, Crawford GS, Draganska M, Fox JT, Hartmann W, et al. (2005) Recent advances in structural econo metric modeling: Dynamics, product positioning and entry Marketing Lett. 16(3–4):209–224.

Erdem T, Keane MP (1996) Decision-making under uncertainty: Capturing dynamic brand choice processes in turbulent consumer goods markets. Marketing Sci. 15(1):1–20.

Farber HS (2005) Is tomorrow another day? The labor supply of New York City cabdrivers. J. Political Econom. 113(1):46–82.

Farber HS (2008) Reference-dependent preferences and labor supply: The case of New York City taxi drivers. Amer. Econom. Rev. 98(3):1069–1082.

Farber HS (2015) Why you can’t find a taxi in the rain and other labor supply lessons from cab drivers. Quart. J. Econom. 130(4): 1975–2026.

Francalanci C, Galal H (1998) Information technology and worke composition: Determinants of productivity in the life insurance industry. Management Inform. Systems Quart. 22(2):227–241.

Ge Y, Xiong H, Tuzhilin A, Xiao K, Gruteser M, Pazzani M (2010) An energy-efficient mobile recommender system. Proc. 16th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM) (Association for Computing Machinery, New York, NY, USA), 899–908.

Ghose A, Li B, Liu S (2019) Mobile targeting using customer trajectory patterns. Management Sci. 65(11):5027–5049.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride sharing and alcohol-related moto vehicle homicide. MIS Quart. 41(1):163–187.

Guda H, Subramanian U (2019) Your Uber is arriving: Managing ondemand workers through surge pricing, forecast communication, and worker incentives. Management Sci. 65(5):1995–2014.

Haggag K, McManus B, Paci G (2017) Learning by driving: Pro ductivity improvements by New York City taxi drivers. Amer. Econom. J. Appl. Econom. 9(1):70–95

Hall J, Kendrick C, Nosko C (2015) The effects of Uber’s surge pricing: A case study. Working paper, University of Chicago, Chicago.

Hao H, Padman R, Sun B, Telang R (2018) Quantifying the impact of social influence on the information technology implementation process by physicians: A hierarchical Bayesian learning ap proach. Inform. Systems Res. 29(1):25–41.

Huang Y, Singh PV, Srinivasan K (2014) Crowdsourcing new product ideas under consumer learning. Management Sci. 60(9): 2138–2159.

Hunter T, Herring R, Abbeel P, Bayen A (2009) Path and travel time inference from GPS probe vehicle data. NIPS Analyzing Networks Learning Graphs (NIPS, Whistler, BC) 12(1):2.

Iyengar R, Ansari A, Gupta S (2007) A model of consumer learning for service quality and usage. J. Marketing Res. 44(4):529–544.

Lee Y-J, Hosanagar K, Tan Y (2015) Do I follow my friends or the crowd? Information cascades in online movie ratings. Management Sci. 61(9):2241–2258.

Liao L, Patterson DJ, Fox D, Kautz H (2006) Building personal maps from GPS data. Ann. New York Acad. Sci. 1093(1):249–265.

Liu D, Di Weng YL, Bao J, Zheng Y, Qu H, Wu Y (2017) SmartadP: Visual analytics of large-scale taxi trajectories for selecting billboard locations. IEEE Trans. Visualization Comput. Graphics 23(1): 1–10.

Liu L, Andris C, Ratti C (2010a) Uncovering cabdrivers’ behavior patterns from their digital traces. Comput. Environ. Urban Systems 34(6):541–548.

Liu S, Liu Y, Ni LM, Fan J, Li M (2010b) Toward mobility-based clustering. Proc. 16th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM) (Association for Computing Machinery, New York, NY, USA), 919–928.

Liu S, Araujo M, Brunskill E, Rossetti R, Barros J, Krishnan R (2013) Understanding sequential decisions via inverse reinforcement learning. IEEE 14th Internat. Conf. Mobile Data Management (MDM), vol. 1 (IEEE, Piscataway, NJ), 177–186.

Liu Y, Whinston A (2019) Resolving Braess’s paradox through information design: Routing for heterogeneous autonomous vehicles. Inform. Econom. Policy 47:14–26.

Luo X, Andrews M, Fang Z, Phang CW (2013) Mobile targeting. Management Sci. 60(7):1738–1756.

McFadden D (1974) Conditional logit analysis of qualitative choices. Zarembka P, ed. Frontiers in Econometrics (Academic Press, Cambridge, MA), 105–142.

Mehta N, Rajiv S, Srinivasan K (2004) Role of forgetting in memorybased choice decisions: A structural model. Quant. Marketing Econom. 2(2):107–140.

Menon NM, Mishra A, Ye S (2020) Beyond related experience: Upstream vs. downstream experience in innovation contest platforms

with interdependent problem domains. Manufacturing Service Oper. Management. Forthcoming.

Molitor D, Reichhart P, Spann M, Ghose A (2019) Measuring the effectiveness of location-based advertising: A randomized field experiment. Working paper. Fordham University, New York.

Okabe A, Boots B, Sugihara K, Chiu SN (2009) Spatial Tessellations: Concepts and Applications of Voronoi Diagrams, vol. 501 (John Wiley & Sons, Hoboken, NJ).

Phithakkitnukoon S, Veloso M, Bento C, Biderman A, Ratti C (2010) Taxi-aware map: Identifying and predicting vacant taxis in the city. International Joint Conference on Ambient Intelligence (pp. 86-95). Springer, Berlin, Heidelberg.

Reiss PC, Wolak FA (2007) Structural econometric modeling: Rationales and examples from industrial organization. Heckman JJ, Leamer E, eds. Handbook of Econometrics, vol. 6(A) (Elsevier), 4277–4415.

Salz T, Lizzeri A, Frechette GR (2019) Frictions in a competitive, regulated market evidence from taxis. Amer. Econom. Rev. 109(8): 2954–2992.

Shin S, Misra S, Horsky D (2012) Disentangling preferences and learning in brand choice models. Marketing Sci. 31(1):115–137.

Tambe P (2014) Big data investment, skills, and firm value. Man agement Sci. 60(6):1452–1469.

Tambe P, Hitt LM (2012) The productivity of information technology investments: New evidence from IT labor data. Inform. System Res. 23(3 pt. 1):599–617.

Wang Y, Wu C, Zhu T (2019) Mobile hailing technology and tax driving behaviors. Marketing Sci. 8(5):734–755

Yuan J, Zheng Y, Xie X, Sun G (2013) T-drive: Enhancing driving directions with taxi drivers’ intelligence. IEEE Trans. Knowledge Data Engrg. 25(1):220–232.

Zhang S, Singh PV, Ghose A (2019) A structural analysis of the role of superstars in crowdsourcing contests. Inform. Systems Res. 30(1): 15–33.

Zhao Y, Yang S, Narayan V, Zhao Y (2013) Modeling consumer learning from online product reviews. Marketing Sci. 32(1):153–169.

Zheng J, Tan Y, Ren F, Chen X (2020) Optimizing two-sided pro motion for IS enabled transportation network: A conditional Bayesian learning model. Inform. Systems Res. Forthcoming
