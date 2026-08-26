---
otero_id: 2132
otero_key: "4DTJMSST"
title: "A Decision Support System for predictive police patrolling"
authors: "M. Camacho-Collados; F. Liberatore"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.04.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
M. Camacho-Collados <sup>a,b</sup>, F. Liberatore <sup>c,</sup>⁎

<sup>a</sup> Spanish National Police Corps, Madrid, Spain

<sup>b</sup> Statistics and Operations Research Department, University of Granada, Granada, Spain

<sup>c</sup> AIDA, Computer Science Department, Autonomous University of Madrid, Madrid, Spain

## a r t i c l e i n f o

Article history: Received 2 September 2014 Received in revised form 1 March 2015 Accepted 24 April 2015 Available online 4 May 2015

Keywords: Predictive policing Time series forecasting Police Districting Problem Multi-criteria decision-making Decision Support Systems

## a b s t r a c t

In the current economic climate, many police agencies have reduced resources, especially personnel, with a consequential increase in workload and deterioration in public safety. A Decision Support System (DSS) can help to optimize effective use of the scarce human resources available. In this paper we present a DSS that merges predictive policing capabilities with a patrolling districting model, for the design of predictive patrolling areas. The proposed DSS, developed in close collaboration with the Spanish National Police Corps (SNPC), defines partitions of the territory under the jurisdiction of a district that are efficient and balanced at the same time, according to the preferences of a decision maker. To analyze the crime records provided by the SNPC, a methodology for the description of spatially and temporally indeterminate crime events has been developed. The DSS has been tested with a case study in the Central District of Madrid. The results of the experiments show that the proposed DSS clearly outperforms the patrolling area definitions currently in use by the SNPC. To compare the solutions in terms of efficiency loss, we discuss how to build an operational envelope for the problem considered, which can be used to identify the range of performances associated with different patrolling strategies.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

In this paper, we propose a Decision Support System (DSS) for the implementation of a new paradigm of predictive police patrolling for the efficient distribution of police officers in a territory under the jurisdiction of a police department, with the aim of reducing the likelihood of criminal acts. This DSS, called the Predictive Police Patrolling DSS (P<sup>3</sup>-DSS), has been developed in collaboration with the Spanish National Police Corps (SNPC).

Intuition has always been a fundamental part of police work [39]. Knowledge in the field by experienced managers of public security has proven to be a useful weapon against crime. In most police departments, this experience-based system remains unchanged. However, police intuition may not be taking into account all the factors influencing the evolution of crime. Historically, criminology has shown great interest in the identification of areas with a higher rate of criminal activity [5]. It has been proven that studying historical data allows identifying places where crime tends to agglomerate. Therefore, making use of historical information is fundamental for decreasing crime, as we know that crime has greater chances of happening when there are no security measures and a motivated criminal encounters an appropriate objective [48,49]. Consequently, in the last decade, predictive policing measures have been developed, with different levels of sophistication, with the aim of providing an analysis of the evolution of crime in a territory. More recently, both academics and practitioners, such as the RAND corporation and the National Institute of Justice of the United States (NIJ), have recognized the need for taking a step forward and developing explicit DSS to provide help to decision makers in law enforcement agencies [38].

## 1.1. The Predictive Police Patrolling DSS $( P ^ { 3 } { - } D S S )$

In Spain, the security of towns is the responsibility of the SNPC, usually sharing a territory with other local security forces. The SNPC is an armed institution of a civil nature, dependent on the Spanish Ministry of Home Affairs. Among its duties are keeping and restoring order and public safety and preventing the commission of criminal acts. The SNPC is one of the country's most valued institutions, and is at the global forefront of the fight against crime, with the aim of constant innovation. Under the current system, the distribution of agents is determined by the inspectors that coordinate the service during a particular shift. Their experience, accompanied by preliminary information, such as a summary of the criminal activity of the last days, leads them to decide on the allocation of policemen in a whole district.

The socio-economic context in recent years in Spain is that of a severe crisis that has reduced the number of police officers available to the SNPC. Therefore, designing the distribution of agents in a territory has become a complex task, and the lack of personnel can result in a lowered level of security and, as a consequence, in an increased level of crime. In order to continue providing the same level of security to the citizens of Spanish cities, the SNPC is taking steps to increase its competitiveness, such as the development of a DSS to assist decisionmaking processes in matters of public security in Madrid, with the intention of applying this methodology to other cities. The seminal work of [47] showed that making use of optimization models results in a reduction of the level of subjectivity present in this kind of decision-making, an improvement in the quality of the decisions, and an increase in the level of satisfaction of the policemen involved.

This article has made the following contributions to the literature on DSS for public security management. First, we illustrate the pilot study that was undertaken in collaboration with the SNPC to develop a DSS for the implementation of a predictive police patrolling paradigm: the P<sup>3</sup>-DSS. This DSS provides predictive policing capabilities for forecasting the distribution of crime risk in a territory, as well as an optimization system that exploits this information to distribute agents in the best possible way, according to the preferences of the decision maker. To the best of the authors' knowledge, this is the first DSS for public security managers that combines predictive policing techniques to support the allocation of human resources. Furthermore, we present a methodology for the temporal and spatial description of crime events in which the time and the location of the incidents are indeterminate. In fact, the exact time and location of occurrence of an incident is often not known to the victim or the police. As an example, a victim of a pickpocket will often realize that he/she has been robbed after a certain time, therefore making it impossible to determine precisely when and where the crime occurred. Previous works on the subject have dealt exclusively with temporally indeterminate crimes [30] and, to the best of the authors' knowledge, no treatment for spatial uncertainty has been proposed in the literature. Moreover, we propose a novel algorithm to define the operational envelope for the specific shift under study. The operational envelope is a powerful tool for identifying the range of impacts of different patrolling strategies and to quantify possible efficiency losses of suboptimal plans. Finally, to test our DSS, we present a case study of the Central District of Madrid. This same methodology can be easily extended to any district. Additionally, we provide some insights into the patrolling strategies produced by the DSS and compare their performance to the current patrol sector configurations adopted by the SNPC.

The reminder of the article is organized as follows. In the next section we present the current state of the art of predictive policing. This part also examines the theoretical background and current research into the Police Districting Problem (PDP) and focuses on the existing DSS for efficient policing. In Section 3, the structure of the proposed DSS, called P<sup>3</sup>-DSS, is given. Next, in Section 4, we present the operational envelope, its application in the evaluation of patrolling configurations, and an algorithm for its computation. In Section 5 we apply the P<sup>3</sup>-DSS to a real case study of the Central District of Madrid. The article concludes with a summary of the main findings of this research and some possible future lines of research to be explored.

## 2. Related work

In this section, a review of the most relevant contributions to the literature is presented.

## 2.1. Predictive policing

The term predictive policing is relatively recent and refers to the application of quantitative techniques to foretell where crimes will take place in the short-term future. The National Institute of Justice (NIJ) defined it as taking data from disparate sources, analyzing them, and then using the results to anticipate, prevent, and respond more effectively to future crimes [36]. This technique is based upon advances in criminology, such as Hot Spot theories [43,54,53], and studies of the ecology of crime [7,8]. Statistics based methods have been used since the release of CompStat in 1994, but it was only a few years ago that complex mathematical algorithms have been developed to address this problem in the most profound way. CompStat combined Geographic Information System (GIS) and crime mapping techniques to identify areas of high crime intensity. The importance of measuring the occurrence of crimes in the police districts and keeping track of the actions of the police managers for decision-making was proven by Weisburd et al. [55]. This topic was opened to different approaches by the International Journal of Forecasting, which published a special issue on crime forecasting in 2003 [24].

Years later, researchers at UCLA started a new approach to the investigations of crime agglomerations, modeling the dynamics of crime hotspots and determining the parameter values that lead to the creation of stable hotspots [45]. In a subsequent study, they used amplitude equations to study the development of crime hotspot patterns [44] and self-exciting point processes [35]. Also, they mathematically proved that there were different types of hotspots, even though they seemed similar at first sight. This breakthrough was further developed using Levy Flight models by Chaturapruek et al. [14]. More recently, Zipkin et al. [58] introduced a police behavior component aiming at suppressing hotspots of criminal activity. In this model, the police deployment adapts dynamically to changing crime patterns, making criminals modify, to a certain degree, their awareness and their criminal actions.

Probably the most ambitious predictive policing project so far made use of the algorithms created by Brantingham and Mohler, along with LAPD Captain Sean Malinowski. With three years of data, and focusing on three types of crime in particular (i.e., burglary, automobile theft, and theft from automobiles), the algorithm points out areas of likely crime incidence. The first analyses have shown a reduction of property offenses where this methodology has been implemented, reporting considerable reductions in serious violence crimes in the treatment cities and areas relative to comparison cities and areas. Another experiment of predictive policing was implemented in Santa Cruz, where predictive maps based on risk percentages were given to security managers. The use of these maps resulted in a 19% drop in burglaries [21].

Another line of research that has been widely applied in practice has focused on Risk Terrain Modeling (RTM) [11]. According to its creators, RTM is “an approach to risk assessment in which separate map layers representing the influence and intensity of a crime risk factor at every place throughout a geography is created in a Geographic Information System (GIS). Then all map layers are combined to produce a composite “risk terrain” map with values that account for all risk factors at every place throughout the geography” [10]. RTM has also been proposed as a methodology for the identification of risk clusters and the distribution of police resources [30].

A number of models making use of methodologies other than hotspot and RTM have been presented in the academic literature. Xue and Brown [56] and Smith and Brown [46] developed a spatial choice model and represented criminal events as point processes combining discrete choice techniques and data mining. They used this approach to predict the spatial behavior of criminals, comparing it with existing hotspot analyses. Furtado et al. [22] model criminal behavior by using ant-inspired systems, trying to discover strategies for efficient police patrolling that take into account the dynamics of the criminals. Wang and Brown [51] used a spatiotemporal analysis for modeling criminal incidents, making use of a variety of data types, such as spatial, temporal, geographic, and demographic data. In a subsequent paper, Wang et al. [52] extended this prediction model to include information proceeding from social network posts. A similar approach is proposed by Gerber [23], finding that by combining historical crime records with Twitter data from users in a specific geographic area, the prediction performance improves for 19 of 25 crime types. Finally, Chen et al. [15] applied spatio-temporal analysis methods to investigate patterns of offenses against property.

## 2.2. The Police Districting Problem (PDP)

District design can be seen as the problem of grouping the elementary units of a given territory into larger districts, according to their relevant attributes. Depending on the problem faced, the attributes considered might belong to different contexts, including economic, demographic, geographic, and political contexts. In the last decades, the districting problem has been approached in a broad number of fields: e.g., electric power, schools, electoral areas, and police patrols. A unified territorial design model that allows the formulation and solution of districting problems in a variety of applications is the subject of Kalcsics and Schröeder [28], which also reviews the existing literature on territorial design, highlighting application fields, criteria, and solution methodologies for these types of problems.

The Police Districting Problem (PDP) concerns the optimal partitioning of a territory into patrol sectors. Optimizing the configuration of patrol sectors in the face of the expected crime activity in a particular shift or scenario provides a solid guideline for the effective deployment of the agents. Also, by concentrating the presence of police agents in the areas with the highest expected levels of criminal activity, it fosters a shift of paradigm from detention to prevention, thanks to the deterrent effect of a police presence. The first paper on PDP was by Mitchell [34], which proposes a clustering heuristic for the redesign of patrol beats in Anaheim, California. The author considers the total expected weighted distance to incidents, as well as a workload measure defined as the sum of the expected service time and the expected travel time. Bodily [6] adopts a utility theory model that incorporates the preferences of three interest groups, namely, the citizens, the administrators, and the service personnel. A simple local search algorithm swaps patrol beats from one sector to another to improve the value of the utility function. Benveniste [1] was the first author to include workload equalization in the optimization process, solving a non-linear stochastic model by means of an approximation algorithm. The model by D'Amico et al. [20] calculates sector workloads by calling an external software program, PCAM [12,13]. This external routine makes use of a queuing model to compute the statistics regarding a sector, including the optimal number of cars to be allocated. The simulated annealing algorithm devised by D'Amico et al. [20] iteratively calls PCAM as a subroutine. To enforce equity in terms of area, the ratio of the size of the largest and smallest sectors is bounded from above. Unlike the previous papers, Curtin et al. [19] apply a covering model to determine police patrol sectors, so as to maximize the number of incidents that are close to the centers of the sectors. In a subsequent article [18], the authors include backup coverage (e.g., multiple coverage of high priority locations). Zhang and Brown [57] propose a heuristic algorithm for the generation of districting, evaluated using an agent-based simulation model.

Contributions to the PDP have been extremely heterogeneous in terms of the objectives and methodologies adopted. As an example, a universal definition of workload has not been reached yet. A thorough review of all the research on the PDP, analyzing and comparing the different aspects of the models and approaches proposed, can be found in [9].

## 2.3. DSS for efficient policing

The application of DSS to police environment has a growing role in the literature. Some innovative strategies have been established to be effective and efficient when deciding on the best officer deployment and schedule. In the late 1980s, Taylor and Huxley [47] proposed a scheduling system driven by shift turnovers, based on years of calls data. This led to a declining response time compared to manual methods. However, in that study, different crime records were not considered. More recently, Xue and Brown [56] proposed a DSS in which criminal events were modeled as point processes. They intended to predict the spatial behavior of active criminals. By analyzing the offenders' decisions, law enforcement would be empowered with better planning and knowledge of the spatial patterns of crime. A few years later, anoth er intuitive method discussed by Li et al. [33] suggested a model based on a fuzzy self-organizing map, identifying the characteristic of several crime patterns, to determine a better duty deployment. However, recent research by Kuo et al. [32] criticized most programs for making use of a naive before–after evaluation method. The authors developed hotspot approaches that apply GIS to combine crime rates and crash rates for prediction, aiming to reduce dispatch time. The main characteristics of the articles reviewed here are summarized in Table 1.

The research presented in this article innovates in the field of DSS for public security in several ways. First, most of the methodologies developed so far assume that the crime incidents can be represented as points in time and space. As we elaborate in Section 3.1, this is not always the case, as most of the time the victims are not aware of the time or the location where the crime took place. Therefore we developed a methodology that allows us to represent crime records having an indeterminate time or location. Second, the proposed methodology makes use of classical time series models. Although not novel, these models have two advantages: they are very good at capturing the seasonal components of the crime data and they do not require any additional spatial information (e.g., population density, average income, distance to risky locations), which makes them extremely applicable. Finally, to the best of the authors' knowledge, the DSS presented in this paper is the first to combine Predictive Policing capabilities with an optimization model that explicitly provides efficient partitions of the territory into patrol sectors, rather than just a representation of the criminal hot spots.

## 3. Structure of the P<sup>3</sup>-DSS

The DSS that we propose is composed of three main elements that identify the predictive police patrolling strategies: Data Pre-Processing Unit (DPPU), Crime Risk Forecasting Unit (CRFU), and Patrol Sector Optimization Unit (PSOU).

Fig. 1 illustrates the main loop of the P<sup>3</sup>-DSS, which shows how the elements interact. Being a real-time system, the P<sup>3</sup>-DSS undertakes an infinite loop composed of two main parts. When a certain updating condition is met (e.g., when a significant number of records have been added to the crime reports database and a certain amount of time has passed since the last update), the system first calls the DPPU to update the internal data structures and the CRFU to update the forecasting models. These operations are carried out in the background, and are invisible to the user. Whenever a request for a patrolling configuration is sent by the user, the P<sup>3</sup>-DSS calls the PSOU and returns the resulting configuration. These units will be presented in detail in the following subsections.

## 3.1. Data Pre-Processing Unit (DPPU)

Most of the research in predictive policing assumes that the criminal incidents are associated with a determined point in time and space. Ratcliffe [41] presents a methodology for the temporal description of crime events where the time of incidence is indeterminate. However, many common crimes also have indeterminate spatial incidence, e.g., pickpocketing. We now present a novel methodology for the spatio-temporal description of crime events that can be indeterminate in both the temporal and the spatial dimensions.

The P<sup>3</sup>-DSS makes use of a three-dimensional data structure providing a discretized representation of the space (i.e., the territory under the jurisdiction of a district) and of time (i.e., the period of time considered in the historical data). In fact, we represent the territory under the jurisdiction of a district as a grid, G, having I rows and J columns. The size of the grid cells can be determined by taking advantage of the results of Gorr and Harries [24], which show that the average monthly crime counts need to be on the order of 30 or more to achieve good forecast accuracy. Time is discretized by considering the agents' shift as the time unit.<sup>1</sup> The total number of time steps, T, can be easily computed by calculating the number of shifts included in the period of time encompassed by the historical data available.

The main data structure used by the DSS is a three-dimensional array C, having dimension $I \times J \times T .$ The value of each element, $c _ { i , j , t } \in \mathbb { R } ,$ represents the number of crime reports associated with location $( i , j ) \in G$ at time step $t \in \{ 1 , . . . , T \}$ . The procedure executed by the DPPU to compute this value will be explained in the following.

Table 1  
References and structural characteristics of DSS for efficient policing.

<table><tr><td>Reference</td><td>Data</td><td>Objective(s)</td><td>Technology</td><td>Validated</td></tr><tr><td>Taylor and Huxley [47]</td><td>Provided by: San Francisco Police Department, CA. Historical calls for service, time spent by call type, percentage of calls requiring two or more police officers, and percentage of cars with two or more officers allocated.</td><td>Reduction of the cost of operations and increase of citizen safety and officer morale.</td><td>San Francisco Police Department Computer Aided (CAD) System</td><td>Yes</td></tr><tr><td>Xue and Brown [56]</td><td>Provided by: Richmond Police Department, VA. Criminal incidents between July 1, 1997 and October 31, 1997. Includes more than 1200 crime observations.</td><td>Crime reduction</td><td>Regional Crime Analysis Program (ReCAP)</td><td>No</td></tr><tr><td>Li et al. [33]</td><td>Provided by: National Police Agency of Taiwan. Data originated from 20 county police bureaus in Taiwan from 2003 to 2004. Fourteen criminal categories were collected.</td><td>Crime reduction</td><td>Unknown</td><td>No</td></tr><tr><td>Kuo et al. [32]</td><td>Provided by: College Station Police Department, TX. Crime and crash data, from January 2005 to September 2010. Includes 65,461 offense reports and 14,712 crash reports.</td><td>Reduction of dispatching time and number of crime and traffic events</td><td>ArcGIS, KDE, Google Maps</td><td>No</td></tr></table>

The array C is initialized to 0. Next, each crime report is proportionally accounted for in the elements of the array involved in the criminal event according to the following data included in the crime report database of the SNPC:

• Event time window: Range of dates and times in which an event occurred.

• Event location: Place where the crime was committed, i.e., its geographical location. This might be specified as an address or, more generally, as an area.

By “proportionally,” we mean that a crime is partially accounted for in all elements $c _ { i , j , t }$ referenced by the data. The following cases might occur:

• The time and location of the crime are known with certainty and are limited to a single grid cell and time step (e.g., a robbery). The location $( i , j )$ and time step t can be determined unambiguously. The value of $c _ { i , j , t }$ is increased by 1.

• The location of the crime is limited to a single grid cell and the time is expressed as a period of time covering more than one time step (e.g., a motor vehicle theft). In this case, the location (i, j) can be determined unambiguously but the time is expressed as a range $t , . . . , t + n .$ . Thus, the value of the $C _ { i , j , t } , . . . , C _ { i , j , t } + n$ is increased according to the proportional part of the crime time range that falls into each time step.

• The time of occurrence of the crime is contained in one time step but the location is not limited to a single grid cell (e.g., a breach of the peace). The time step t can be determined unequivocally but the location is expressed as a set of locations $\{ ( i _ { 1 } , j _ { 1 } ) , . . . , ( i _ { n } , j _ { n } ) \}$ . Therefore, the $C _ { i _ { 1 } , j _ { 1 } , t } , . . . , C _ { i _ { n } , j _ { n } , t }$ are increased according to the proportional part of the area considered by the reports that falls into each grid cell.

• The location is not limited to a single grid cell and the time of the crime is contained in more than one time step (e.g., a pickpocketing or evading a police car). In this case, first all the elements involved are identified, and then the value of each element is increased proportionally, as illustrated in the previous items.

Once C is built, we can use it to forecast the risk of crime in a specific shift.

## 3.2. Crime Risk Forecasting Unit (CRFU)

The array C can be looked at from two different perspectives. In fact, by selecting a specific time step, $\overline { { t } } \in \{ 1 , . . . , T \}$ , the bi-dimensional matrix $C _ { \bullet , \bullet , \overline { { t } } }$ <sup>f g</sup>represents the distribution of crimes reported in the territory for the selected shift. Similarly, by selecting a specific location $\left( \bar { i } , \bar { j } \right) \in { \cal G } ,$ the vector $C _ { \bar { i } , \bar { j } , }$ is the time series of the crime counts for the selected location. Since this number is an approximation to the real number of crimes committed, we can apply classical time series forecasting models to predict the risk of crime for each cell of the grid. For instance, exponential smoothing models assign progressively smaller weights (importance) to older data, whereas newer data is given progressively greater weight. The use of classical time series forecasting models has also been validated by previous research on the topic. In fact, Gorr [25] and Cohen [17] agree that exponential smoothing models are very accurate at forecasting crime series at the sub-district level. Following these results, the CRFU considers for each location $( i , j ) \in G$ an exponential smoothing state space model [27]. As shown in Section $5 ,$ although this methodology relies exclusively on crime location, the CRFU is capable of discerning the underlying pattern and producing good quality predictions.

## 3.3. Patrol Sector Optimization Unit (PSOU)

Forecasting the risk of crime in an area is just the first step toward the definition of sound patrolling sectors in a district. By optimizing the configuration of patrol areas, it is possible to focus resources on the most relevant locations, with a consequential improvement in the effectiveness of patrolling operations. After interviewing several service coordinators and a number of agents involved in public safety operations, several desirable characteristics were identified in order to find a “good” territory partition.

• Compact areas: a compact area allows for a better control of the territory by the agents, as travel times from one point to another within the area are minimal. Therefore, the more compact an area is, the faster the response of agents who are in the area to emergency calls.

![](/api/attachments/4DTJMSST/fulltext/images/1913eda4f2732e2e1ba6a37f25f351d3923488975d20ae9685cb9afc528a3e37.jpg)  
Fig. 1. The $\mathrm { P } ^ { 3 } .$ -DSS main loop.

• Homogeneity in terms of workload: generating patrol sectors that are similar in terms of workload is quite useful for two main reasons. First, it ensures a more efficient distribution of work and, therefore, a better service to the public. Second, greater equality in workload increases the satisfaction of the agents.

• Mutual support: It is desirable that agents be able to count on the support of agents assigned to other patrol sectors in case of need.

The mathematical optimization model proposed for the solution of this problem partitions the area under the jurisdiction of a police district into a defined number of patrolling sectors, in the most efficient way. The resulting districting problem, called the Multi-Criteria Police Districting Problem (MC-PDP), has been presented in [9] and a fast heuristic algorithm was proposed for its solution. Computational experiments showed that the MC-PDP rapidly generates patrolling configurations that are more efficient than those currently adopted by the SNPC. The main characteristics of the MC-PDP will be introduced in the following.

## 3.3.1. Input data and parameters

The PSOU requires the following input data:

• Let R be the bi-dimensional crime risk matrix for a future time step $t ^ { \prime } > T ,$ having dimension $I \times J .$ This matrix is computed by the CRFU by forecasting the crime risk level at each location $( i , j ) \in G .$ . Thus, the value of every element $r _ { i , j } \in R$ represents the predicted risk of crime at location $( i , j )$ and time step $t ^ { \prime } .$

• Let A be the bi-dimensional distance matrix, having dimension $I \times J .$ The elements $a _ { i , j } \in A$ are non-negative real numbers that represent the total length of the streets to be patrolled at location $( i , j ) \in G .$ This matrix can be computed using the information provided in a GIS.

• Let $p \in$ ℕ be the number of patrolling sectors to be defined. We assume $p > 1$

• Let $\mathbf { w } \in \mathbb { R } ^ { 4 }$ be the vector of weights expressing the decision maker's preference associated with each attribute (see Section 3.3.3).

• Let $\lambda \in \mathbb { R } , 0 \leq \lambda \leq 1$ be the coefficient expressing the decision maker's preference between optimization and workload balance (see Section 3.3.4).

## 3.3.2. Structure of a patrolling configuration

A feasible patrolling configuration is a partition P of the territory considered. Each subset s ∈ P represents a patrol sector and is expressed as a subset of locations, i.e., $s \subseteq G .$ From this point onward, the terms “patrol sector” and “partition subset” will refer to the same concept. The number of subsets in the partition must be exactly p. All partition subsets must be connected and convex.

## 3.3.3. Patrol sector attributes and workload

The MC-PDP evaluates the patrol sectors s ∈ P defined by a configuration P according to four main attributes: area, isolation, demand, and diameter. All the attributes, explained in the following, are expressed as dimensionless ratios, so as to be comparable.

• Area, $\alpha ^ { s } .$ . This attribute is a measure of the size of the territory that an agent should patrol. It is expressed as the ratio of the area encompassed by sector s, to the whole district area.

$$
\alpha^ {s} = \frac {\sum_ {(i , j) \in s} a _ {i j}}{\sum_ {(i , j) \in G} a _ {i j}}.\tag{1}
$$

• Isolation, $\beta ^ { s } .$ In the MC-PDP, two districts support each other if the distance between their geometric medians (i.e., the location in a sector that minimizes the sum of the distances to all the locations in the sector) is less than or equal to a defined constant, K. We recommend defining K as

$$
K = \left\lceil \frac {\max \{I , J \}}{\sqrt {p}} \right\rceil .\tag{2}
$$

The support received by a sector can be calculated by

$$
b ^ {s} = \left| \left\{s ^ {\prime} \in P \mid d i s t \left(o ^ {s}, o ^ {s ^ {\prime}}\right) \leq K, s \neq s ^ {\prime} \right\} \right|,\tag{3}
$$

where $o ^ { s }$ identifies the median location of sector s and dist is the distance between two locations.<sup>2</sup> The isolation of sector s is computed as

$$
\beta^ {s} = \frac {p - 1 - b ^ {s}}{p - 1}.\tag{4}
$$

• Risk, $\gamma ^ { s } .$ . This attribute is a measure of the total risk associated to the sector that an agent patrols. It is expressed as the ratio of the total risk of sector s, to the whole district risk.

$$
\gamma^ {s} = \frac {\sum_ {(i , j) \in s} r _ {i j}}{\sum_ {(i , j) \in G} r _ {i j}}.\tag{5}
$$

• Diameter, $\delta ^ { s } .$ . The diameter of a subset is defined as the maximum distance between any pair of locations belonging to that subset. It has been introduced in the MC-PDP as an efficiency measure. In fact, the diameter can be interpreted as the maximum distance that the agent associated to the district would have to travel in case of an emergency call. Therefore, a small diameter results in a low response time. The diameter measure used to evaluate a patrol sector is the ratio of the subset diameter to the maximum diameter possible.

$$
\delta^ {s} = \frac {\max _ {a , b \in s} \{d i s t (a , b) \}}{\max _ {a , b \in s} \{d i s t (a , b) \}}.\tag{6}
$$

By combining the attributes with the preference weights w defined by the decision maker, we can compute a measure of the workload $W ^ { s }$ of a sector s as

$$
W ^ {s} = w _ {\alpha} \cdot \alpha^ {s} + w _ {\beta} \cdot \beta^ {s} + w _ {\gamma} \cdot \gamma^ {s} + w _ {\delta} \cdot \delta^ {s}.\tag{7}
$$

## 3.3.4. Objective function

According to the guidelines provided by the professionals of the SNPC, the patrolling configurations should be as efficient as possible and, at the same time, they should distribute the workload homogeneously among the patrol sectors. Unfortunately, there might be a trade-off between these requirements. The objective function of the MC-PDP takes into consideration the preferences of the decision maker for these factors.

$$
\min o b j (P) = \lambda \cdot \max _ {s \in P} \left\{W ^ {s} \right\} + (1 - \lambda) \cdot \frac {\sum_ {s \in P} W ^ {s}}{p}.\tag{8}
$$

The term $m a x _ { s \in P } \{ W ^ { s } \}$ represents the worst workload, while the term $\frac { \sum _ { s \in P } W ^ { s } } { p }$ is the average workload. This objective function allows the decision maker to examine the trade-off between optimization and balance by a parametric analysis. In fact, by varying λ, the model gives a range from optimization $( \lambda = 0 )$ to balance $( \lambda = 1 )$ ).

![](/api/attachments/4DTJMSST/fulltext/images/79d11eca0607814541546bf181b11b3600dda3ee453ace60ed8958c65a6a6fd6.jpg)  
Fig. 2. Operational envelope. Workload of the system as a function of the number of patrolling sectors p.

## 3.3.5. Solving the MC-PDP

The MC-PDP is an extremely complex model that cannot easily be solved to optimality. In fact, not only does modeling the property of subset connectivity make the MC-PDP intractable in large problems, but also no linear formulation for the convexity condition has been presented in the literature. Given that computational time is critical—the user expects a solution within a reasonable time—the MC-PDP is solved by a Greedy Randomized Adaptive Search Procedure (GRASP) algorithm. This methodology, thoroughly described and tested in [9], is capable of generating in just one minute patrolling configurations that are more efficient than those currently adopted by the SNPC.

## 4. The operational envelope

The MC-PDP finds a good partition of the territory, according to different attributes. When considering suboptimal ways of subdividing a district, the basic question is what is the loss of efficiency involved in terms of workload. We can approximate this loss of efficiency by calculating the distance from the best solution value found. For a fixed number of patrolling sectors and weights, we can represent the increase in workload (or loss of system efficiency) as shown in Fig. 2.

The operational envelope presented refers to Saturday, 10/13/2012, night shift in the Central District of Madrid (see Section 5) and was computed using the real crime distribution in the district. However, we can obtain an approximate operational envelope by using the forecast crime distribution provided by the CRFU. In Fig. 2, the values on the x-axis represent the number of patrolling sectors. The values on the y-axis display the workload, computed as in Eq. (8). For this illustrative example, we assign to the weights and the balance coefficient the following values, $( w _ { \alpha } , w _ { \beta } , w _ { \gamma } , w _ { \delta } ) = ( 0 . 4 5 , 0 . 0 5 , 0 . 4 5 , 0 . 0 5 )$ and $\lambda =$ 0.1. As the number of patrolling sectors increases, the workload is consequently decreased. Fig. 2 has two trends: the upper trend displays the worst case workload (i.e., the workload obtained when the least effective patrolling plan is implemented) whereas the lower trend depicts the best case workload (i.e., the workload when implementing the best patrolling plan for different values of p). It can be easily seen that the two trends define a range of losses, from the best case to the worst case, that encompasses all the possible ways of protecting the district. This region is referred to as the operational envelope. Knowing the structure of the envelope can be helpful for patrol planning decisions. The lower curve represents a situation of complete control. Thus, the optimal patrolling strategy can be devised. On the other hand, the upper curve shows the effects of applying the worst possible patrolling scheme. The thickness of the envelope provides valuable information regarding the range of the impact of different partitioning strategies using the same amount of resources, and the extent to which the workload may be unnecessarily increased if suboptimal plans are implemented. Prior examples of depicting similar envelopes in other application settings can be found in [16,31,50].

## 4.1. Computing the operational envelope

An algorithm for the computation of the operational envelope is presented in Algorithm 4.1.

Algorithm 1. Algorithm for the computation of the operational envelope.

```csv
Require: R, A, w, λ
1: for p ∈ {2, ..., 10} do
2: ▷ Obtaining lower trend point
3: i ← 0
4: obj(Pp+) ← inf
5: while i < 10 do
6: solve obj(P) ← min MC-PDP(R, A, w, p, λ)
7: if obj(P) < obj(Pp+) then
8: obj(Pp+) ← obj(P)
9: i ← 0
10: else
11: i ← i + 1
12: end if
13: end while
14: ▷ Obtaining upper trend point
15: i ← 0
16: obj(Pp-) ← -inf
17: while i < 10 do
18: solve obj(P) ← max MC-PDP(R, A, w, p, λ)
19: if obj(P) > obj(Pp-) then
20: obj(Pp-) ← obj(P)
21: i ← 0
22: else
23: i ← i + 1
24: end if
25: end while
26: end for
27: return obj(Pp+) and obj(Pp-), ∀p = 2, ..., 10
```

Computing (or approximating) the operational envelope for a turn is computationally expensive. In fact, the lower trend points are the best solutions found by the MC-PDP, while the upper trend points are the greatest solutions found by a maximization version of the MC-PDP. For the determination of the operational envelope in Fig. 2, we ran the optimization algorithms for each value of p iteratively and stopped the execution when there was no improvement in the best solution for 10 consecutive iterations. This stopping criterion is often applied in exploration-based optimization algorithms such as Genetic Algorithms to ensure that the method has converged [29,42]. In terms of computational time, it took approximately two hours to compute the operational envelope presented in Fig. 2, which is quite time consuming. However, since the operational envelope is a strategical tool that needs to be calculated only once per shift, this computational time is reasonable.

## 4.2. Calculating the efficiency loss

The decision-maker can exploit the information provided by the operational envelope to compare alternative patrolling configurations and evaluate the potential benefits of corrective plans, such as changes in the number of patrolling sectors, or investments in the analysis of the system to acquire a better definition of the data and the parameters. In fact, the operational envelope can be used to compute the percentage efficiency loss associated to a certain partition $P ;$

$$
\text { Efficiency   loss } = 1 0 0 \frac {\operatorname{obj} (P) - \operatorname{obj} \left(P ^ {+}\right)}{\operatorname{obj} \left(P ^ {-}\right) - \operatorname{obj} \left(P ^ {+}\right)}\tag{9}
$$

where $P ^ { + }$ and is the best and $P ^ { - }$ the worst known partition for the set of attributes.

## 5. Case study: the Central District of Madrid

To test the $\mathrm { P } ^ { 3 } { \mathrm { - } } \mathrm { D } { \mathsf { S } } { \mathsf { S } } ,$ , we developed an initial version considering the thefts reported during the years 2008 to 2012 in the Central District of Madrid. The dataset includes exactly 105,755 incidents. This case study focuses on theft as it is the single most frequent type of crime committed in Spain and one of the main priorities for the SNPC is its reduction. However, extending the $\mathrm { P } ^ { 3 } { - } \mathrm { D } \mathsf { S } \mathsf { S }$ to other districts and to consider several types of crime is straightforward and can be accomplished with little change in the structure of the units and the models. Nevertheless, the final version of the P<sup>3</sup>-DSS will require dedicated hardware to be able to cover the whole national territory.

## 5.1. Overview of the Central District of Madrid

Madrid is the capital of Spain and the most populous city in the country. The total population of the city in 2013 was 3,215,633 people, and 6,369,162 people in the metropolitan area. The Central District of Madrid, on which we focus our research, has an area of more than 2 mile<sup>2</sup>, and is limited by the traffic circles of Segovia, Toledo, Valencia, and Atocha. It is composed of six neighborhoods: Palacio, Embajadores, Cortes, Justicia, Universidad, and Sol. Its population is approximately 150,000 people. The population of the Central District of Madrid is extremely heterogeneous; there is also a large transient population that increasingly commutes to this district for reasons of work, sightseeing, or leisure.

In Spain, the security of towns is the responsibility of the SNPC, usually sharing the territory with other local security forces. Currently, the inspector in charge of civil protection operations in a shift decides the distribution of agents in the district. This decision is normally taken considering mostly their personal experience, their intuition, and also some descriptive statistics, such as the summary of the criminal activity of the last days.

## 5.2. Implementation and integration of ${ \bf \dot { P } } ^ { 3 } .$ -DSS

The DPPU and the CRFU have been developed in R [40] and then embedded in C++. For their implementation, the following R packages have been used: sp [37,4], rgeos [3], maptools [2], and forecast [26]. The PSOU has been programmed entirely in C++.

The GIS currently in use by the SNPC (SNPC-GIS) is structured as shown in Fig. 3.

The SNPC-GIS is composed of the following elements:

• Map Database and Server: These units provide access to the updated road maps of Spain.

• Reports Database and ETL Module: These units provide access to

![](/api/attachments/4DTJMSST/fulltext/images/1df30571f1c861d4df3907545ad0dc452f39891a9bd7971101813e926848f186.jpg)  
Fig. 3. SNPC-GIS diagram. A line connecting two elements indicates bi-directional communication between them.

crime records.

• GIS: The GIS in use in the SNPC allows visualizing crime records on the map and representing the location of police vehicles in the territory.

The $\mathrm { P } ^ { 3 } .$ -DSS proposed in this paper is composed of three fundamental parts that interact naturally with the existing SNPC-IS, as illustrated in Fig. 4.

The DPPU interacts with the ETL Module to access the Reports DB, get the crime records data, and to combine this data with the geographical information returned by the Map Server to build the crime risk matrix C. This data is passed to the CRFU to forecast crime risk levels for future shifts. Both the DPPU and the CRFU need to regularly update their data structure and models so as to always have the best forecasting quality. The PSOU obtains the forecast crime risk levels from the CRFU, and the user's preferences from the GIS. Finally, the GIS is connected to the CRFU and the PSOU to make queries regarding the distribution of crime risk in a future shift and the recommended patrol sector configuration, respectively. The GIS has been updated to visualize the patrol configurations, while the forecast crime risk levels are represented using an existing feature for the display of heat maps.

## 5.3. Crime risk prediction quality

We now analyze the quality of the crime risk forecast given by the CRFU. The seasonality period-length was chosen according to preliminary experiments on the dataset that showed that the best performance is obtained when using a seasonality period-length of 21 shifts.

![](/api/attachments/4DTJMSST/fulltext/images/7a35393bb4c51d3afc7e0d1afc8df9d1f1565eef5619e189a9d5d5fc583f55b5.jpg)  
Fig. 4. P<sup>3</sup>-DSS integrated into the SNPC Information System. A line connecting two elements indicates bi-directional communication between them

Forecasting MSEs obtained by the CRFU and by the baseline. Table 2

<table><tr><td>Area</td><td>MSE</td><td>01/2012</td><td>02/2012</td><td>03/2012</td><td>04/2012</td><td>05/2012</td><td>06/2012</td><td>07/2012</td><td>08/2012</td><td>09/2012</td><td>10/2012</td><td>11/2012</td><td>12/2012</td></tr><tr><td colspan="14">(a) Forecasting MSEs obtained by the CRFU.</td></tr><tr><td rowspan="2">*Tribunal</td><td>Training</td><td>0.22168</td><td>0.22439</td><td>0.23043</td><td>0.23004</td><td>0.23365</td><td>0.23238</td><td>0.23144</td><td>0.23097</td><td>0.23081</td><td>0.23104</td><td>0.24023</td><td>0.24323</td></tr><tr><td>Validation</td><td>0.37128</td><td>0.53738</td><td>0.21372</td><td>0.41565</td><td>0.18121</td><td>0.21446</td><td>0.26313</td><td>0.23633</td><td>0.25698</td><td>1.04725</td><td>0.48787</td><td>0.64897</td></tr><tr><td rowspan="2">*Puerta del Sol</td><td>Training</td><td>5.5535</td><td>6.91950</td><td>6.78993</td><td>6.68529</td><td>6.60658</td><td>6.49690</td><td>6.39895</td><td>6.30892</td><td>6.21466</td><td>6.12261</td><td>6.04007</td><td>5.97210</td></tr><tr><td>Validation</td><td>69.19553</td><td>1.27499</td><td>1.25833</td><td>2.69727</td><td>1.52356</td><td>0.84760</td><td>1.56948</td><td>1.56276</td><td>1.16589</td><td>1.89223</td><td>1.54950</td><td>2.97830</td></tr><tr><td rowspan="2">*El Rastro</td><td>Training</td><td>0.10257</td><td>0.11009</td><td>0.10347</td><td>0.10295</td><td>0.10307</td><td>0.10293</td><td>0.10267</td><td>0.10296</td><td>0.10210</td><td>0.10124</td><td>0.10040</td><td>0.09919</td></tr><tr><td>Validation</td><td>0.03804</td><td>0.26832</td><td>0.07405</td><td>0.11660</td><td>0.08281</td><td>0.08519</td><td>0.134499</td><td>0.02678</td><td>0.04322</td><td>0.05627</td><td>0.02750</td><td>0.11087</td></tr><tr><td colspan="14">(b) Forecasting MSEs obtained using the baseline. The percentages are the ratios of the baseline MSEs to the CRFU MSEs.</td></tr><tr><td rowspan="2">*Tribunal</td><td>Validation</td><td>1.48378</td><td>2.07518</td><td>1.23134</td><td>1.16131</td><td>0.51028</td><td>0.56323</td><td>0.40318</td><td>0.40188</td><td>0.64585</td><td>2.16645</td><td>2.04720</td><td>1.53111</td></tr><tr><td>Ratio</td><td>399.64%</td><td>386.17%</td><td>576.15%</td><td>279.40%</td><td>281.60%</td><td>262.63%</td><td>153.22%</td><td>170.05%</td><td>251.32%</td><td>206.87%</td><td>419.62%</td><td>235.93%</td></tr><tr><td rowspan="2">*Puerta del Sol</td><td>Validation</td><td>134.45202</td><td>2.68679</td><td>2.74614</td><td>4.47852</td><td>2.79284</td><td>1.71924</td><td>3.00656</td><td>1.640898</td><td>1.71565</td><td>3.96208</td><td>3.81717</td><td>4.73182</td></tr><tr><td>Ratio</td><td>194.31%</td><td>210.73%</td><td>218.24%</td><td>166.04%</td><td>183.31%</td><td>202.84%</td><td>191.56%</td><td>100.05%</td><td>147.15%</td><td>209.39%</td><td>246.35%</td><td>158.88%</td></tr><tr><td rowspan="2">*El Rastro</td><td>Validation</td><td>0.18613</td><td>1.18519</td><td>0.50907</td><td>0.94083</td><td>0.41429</td><td>0.50386</td><td>0.56963</td><td>0.23759</td><td>0.45586</td><td>0.64930</td><td>0.33392</td><td>0.59623</td></tr><tr><td>Ratio</td><td>489.30%</td><td>441.71%</td><td>687.47%</td><td>806.89%</td><td>500.29%</td><td>591.45%</td><td>423.52%</td><td>887.19%</td><td>1054.74%</td><td>1153.90%</td><td>1214.25%</td><td>537.77%</td></tr></table>

## 5.3.1. Dataset

We assessed the quality of the CRFU forecasts by computing the forecasting Mean Square Error (MSE), considering all the months in 2012 and three areas of interest in the Central District of Madrid. For each validation period, we trained the forecasting model using all the criminal records prior to the period considered (e.g., for the January 2012 validation period, we trained the forecasting models using the historical data from January 2008 to December 2011). Next, we computed the validation MSE for the following areas of interest of the district:

• Tribunal. Located in the north of the district, Tribunal is a wellfrequented crossroad positioned right at the border between two areas that are very popular for nightlife: Malasaña and Chueca.

• Puerta del Sol. One of Madrid's main attractions and a prominent meeting place for citizens and tourists alike, Puerta del Sol is a square located in the center of the district.

• El Rastro. An area located in the south of the district that hosts a famous flea market every Sunday morning.

## 5.3.2. Performance analysis

The training and validation MSEs are given in Table 2a. Except for “January 2012/Puerta del Sol,” the CRFU performed extremely well in validation, with a maximum validation MSE of 2.98, corresponding to an average forecasting error of 1.73 thefts per shift. The “January 2012/Puerta del Sol” case can be easily explained by observing Fig. 5.

In fact, the plot has a peak of more than 80 thefts in the first shift. This observation, that statistically can be considered an outlier, is due to the fact that the first shift of January 2012 corresponds to New Year's Eve. It is traditional in Madrid to celebrate this event in the Puerta del Sol. Therefore, the high aggregation of people in the square and the festive atmosphere contributed to the extraordinarily high number of thefts.

## 5.3.3. Comparison with the baseline

To understand the quality of the predictions returned by the CRFU we compare the results obtained against a baseline. Table 2b presents the MSEs obtained by a baseline model that predicts tomorrow's crime rate to be the same as today's crime rate. In absolute terms, the baseline model performs fairly well, with relatively low values of validation MSE. We can conclude that, with the exception of the “January 2012/Puerta del Sol” case, the crime risk level is quite simple to forecast using only information on time and location, in the dataset considered. In the table, the percentages are the ratios of the MSEs obtained by the baseline model to those of the CRFU. These values confirm that the CRFU provides a much better prediction than the baseline model. In fact, the validation MSE of the baseline model is always larger than the MSE of the CRFU, especially in El Rastro, where it is always more than four times larger.

PUERTA DEL SOL, JANUARY 2012  
![](/api/attachments/4DTJMSST/fulltext/images/9f9f18adf3c17a1d1aba662ea97ba64e8a2de639ff485411962eb9992f569be5.jpg)  
Fig. 5. Crime distribution for January 2012.

(a) CONF2: the city is divided into two big sectors by the Gran Via, the main street in the district, and the agents are free to patrol the assigned area ad lib.

![](/api/attachments/4DTJMSST/fulltext/images/acb2b82e9db345e4ebdbeda434a5523c3a01d82a4373813dec41fd3ccb757a33.jpg)

(b) CONF6: the district is partitioned according to its neighborhoods.

![](/api/attachments/4DTJMSST/fulltext/images/4f8b1cd91ad9e4123c48233e568090cc6362ae0209638ca74932565cc35b744d.jpg)  
Fig. 6. Patrolling configurations currently adopted by the SNPC in the Central District of Madrid. Each sector is represented by a different color. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

## 5.4. Predictive police patrol configurations quality

Camacho-Collados et al. [9] extensively analyzed the performance of the MC-PDP in the presence of perfect information. We now assess the quality of the patrolling configurations generated by the P<sup>3</sup>-DSS based on the forecast crime risk.

## 5.4.1. Comparison with standard configurations

We now analyze the quality of the solutions found by the optimization algorithm by comparing them to the patrolling configurations currently adopted by the SNPC.

In the Central District of Madrid, on an “average day,” one of the following patrol sector configurations is applied:

• CONF6: The district is partitioned according to its six neighborhoods.

• CONF2: The district is split into two big sectors by the Gran Via, the main artery in the territory, and the agents are free to patrol the assigned areas ad lib. The northern sector includes two neighborhoods (viz., Universidad and Justicia) while the southern sector includes four neighborhoods (viz., Palacio, Sol, Embajadores, and Cortes).

To be able to compare the performance of these configurations with those determined by the optimization algorithm, we represented CONF6 and CONF2 using the same grid structure adopted by the optimization algorithm, as illustrated in Fig. 6. The cells of the grid shared by more than one sector have been assigned to the sector occupying most of its area. It should be noticed that both configurations have one sector that is not convex, i.e., the green sector in CONF6 and the light blue sector in CONF2. Therefore, the configurations currently adopted by the SNPC would be infeasible according to the optimization model proposed. This might result in better attribute values for these solutions than those achievable with a feasible solution by the MC-PDP

To assess the quality of the predictive patrol sector configurations, we ran an analysis composed of the following steps:

1. Generation of 1000 random test instances. Each instance is represented as a tuple $( w _ { \alpha } , w _ { \beta } , w _ { \gamma } , w _ { \delta } , \lambda$ , shift). For each sample, the attribute weights $\left( \boldsymbol { w _ { \alpha } } , \ \boldsymbol { w _ { \beta } } , \ \boldsymbol { w _ { \gamma } } , \ \boldsymbol { w _ { \delta } } \right)$ are sampled from a uniform (a) Prediction for SATT3: Saturday, 10/13/2011, night shift (10 PM-8 AM).

(a) SATT3: Saturday, 10/13/2011, night shift (10 PM-8 AM).  
![](/api/attachments/4DTJMSST/fulltext/images/6675a930c60348c1a2da4e1c5c8d7609ac22bd4a8273aa40c382c0641298dd1a.jpg)

(b) SUNT1: Sunday, 10/14/2011, morning shift (8 AM-3 PM).  
![](/api/attachments/4DTJMSST/fulltext/images/9b851c23aeb3482e8f6e852a64fac856b5b178702c98b0524ac1df6ba2410d7a.jpg)

(c) MONT2: Monday, 10/15/2011, afternoon shift (3 PM-10 PM).  
![](/api/attachments/4DTJMSST/fulltext/images/868e845e128a78a9126f96bf09961b533a8979913501f9b02489cec2eb5bbfb0.jpg)  
Fig. 7. Maps of the number of thefts reported in the Central District of Madrid. The red shade represents a high crime level while the white shade represents no criminal activity. (For interpretation of the references to color in this gure legend, the reader is referred to the web version of this article.)

<table><tr><td>Shift</td><td>Configuration</td><td>p</td><td>Obj (P)</td></tr><tr><td colspan="4">(a) Objective function values of the patrol sector configurations currently adopted by the SNPC.</td></tr><tr><td rowspan="2">*SATT3</td><td>CONF2</td><td>2</td><td>0.55086</td></tr><tr><td>CONF6</td><td>6</td><td>0.20655</td></tr><tr><td rowspan="2">*SUNT1</td><td>CONF2</td><td>2</td><td>0.56515</td></tr><tr><td>CONF6</td><td>6</td><td>0.21236</td></tr><tr><td rowspan="2">*MONT2</td><td>CONF2</td><td>2</td><td>0.55074</td></tr><tr><td>CONF6</td><td>6</td><td>0.20830</td></tr><tr><td>Dataset</td><td>p</td><td colspan="2">Obj (P) 95% CI</td></tr><tr><td colspan="4">(b) Objective function values of the patrol sector configurations obtained by  $P^{3}$ -DSS. 95% confidence intervals over 50 runs.</td></tr><tr><td rowspan="2">*SATT3</td><td>2</td><td colspan="2">[0.54560,0.54560]</td></tr><tr><td>6</td><td colspan="2">[0.19699,0.20061]</td></tr><tr><td rowspan="2">*SUNT1</td><td>2</td><td colspan="2">[0.54695,0.54695]</td></tr><tr><td>6</td><td colspan="2">[0.19703,0.19973]</td></tr><tr><td rowspan="2">*MONT2</td><td>2</td><td colspan="2">[0.54112,0.54112]</td></tr><tr><td>6</td><td colspan="2">[0.19399,0.19708]</td></tr></table>

Comparison of the objective function values.

(b) Prediction for SUNT1: Sunday, 10/14/2011, morning shift (8 AM-3 PM).

(c) Prediction for MONT2: Monday, 10/15/2011, afternoon shift (3 PM-10 PM).

![](/api/attachments/4DTJMSST/fulltext/images/818fb126596175bbe727f700c0b379604512d6fd711a44901f78f75e7c8ca985.jpg)  
Fig. 8. Maps of the forecast crime risk in the Central District of Madrid. The red shade represents a high crime risk level while the white shade represents no criminal risk. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

distribution (0,1) and normalized, the balance coefficient λ is sampled from a uniform distribution (0,1) and the shift is chosen ran-<sup>U</sup>domly from the set of all the shifts in 2012.

2. Forecasting of the crime risk distribution and extraction of the validation crime distribution for each of the test instances.

3. Generation of patrolling configurations based on the forecast crime risk by running the MC-PDP once, using 2 and 6 patrol sectors (p = {2, 6}). The optimization algorithm has been run for 60 s to simulate a real-time environment.

4. Evaluation of patrolling configurations generated by the P<sup>3</sup>-DSS using the validation data.

5. Evaluation of the standard patrolling configurations currently adopted by the SNPC (CONF2 and CONF6) using the validation data.

6. Statistical comparison of the objective function values obtained on the same test instances by the standard configurations and those generated by the P<sup>3</sup>-DSS.

The results of the statistical analysis will be presented in the following. First we tested the data for each group for normality using a Shapiro–Wilk Normality Test and found that they did not follow a normal distribution. Then, we applied a Friedman Test, a nonparametric test of nonindependent data from two or more groups that does not require the data to proceed from a normal distribution. The statistical difference is significant in both cases. In fact, the p-values are p = 2.56e − 12 for the 2 patrol sectors case, and p = 0.02781 for the 6 patrol sectors case. We can therefore state that, even in the face of uncertainty,

## Table 3

the P<sup>3</sup>-DSS produces patrolling configurations that dominate those currently adopted by the SNPC.

## 5.4.2. Comparing the loss of performance

It is difficult to understand what the real improvement is in terms of efficiency resulting from using the P<sup>3</sup>-DSS. That is because the objective function (Eq. (8)) includes both a balance term and a global performance term. Fortunately, we can use the operational envelope (see Section 4) to compare the patrolling configurations in terms of efficiency loss (Eq. (9)).

Given the computational time required to compute the operational envelope for each case, this analysis has been limited to three shifts and one configuration of the attributes. The shifts and the attributes have been identified with the help of a service coordinator in charge of the patrolling operations of the Central District of Madrid. In the course of many meetings, we asked the service coordinator to identify a small number of shifts that could be considered as typical scenarios and that presented very different crime activity patterns. The following shifts are considered:

• SATT3: Saturday, 10/13/2012, night shift (10 PM–8 AM).

• SUNT1: Sunday, 10/14/2012, morning shift (8 AM–3 PM).

• MONT2: Monday, 10/15/2012, afternoon shift (3 PM–10 PM).

These three shifts were chosen for their representativeness. Fig. 7 illustrates the distribution of thefts in these three shifts. SATT3 is characterized by a high level of nightlife, with people coming from other districts of Madrid as well as other cities. In the picture it can be seen that thefts are committed in almost all the territory, with the highest levels concentrated around Plaza Callao, a busy meeting place, Plaza Mayor, the central plaza of the city, and Lavapies, a difficult area. SUNT1 has a moderate level of criminality, mostly concentrated in the south of the district where the popular El Rastro flea market is held every Sunday morning. Finally, MONT2 presents the characteristics of a normal business day, with low levels of criminal activity, mostly concentrated in the commercial area.

Comparison of the patrol sector configurations obtained by P<sup>3</sup>-DSS with those currently adopted by the SNPC.

<table><tr><td>Dataset</td><td>Configuration</td><td>p</td><td>SNPC solutions efficiency loss (%)</td><td> $P^3$ -DSS solutions efficiency loss (%) 95% CI</td></tr><tr><td rowspan="2">*SATT3</td><td>CONF2</td><td>2</td><td>15.77</td><td>[0,0]</td></tr><tr><td>CONF6</td><td>6</td><td>20.01</td><td>[10.15,14.38]</td></tr><tr><td rowspan="2">*SUNT1</td><td>CONF2</td><td>2</td><td>82.75</td><td>[0,0]</td></tr><tr><td>CONF6</td><td>6</td><td>24.32</td><td>[8.81,12.04]</td></tr><tr><td rowspan="2">*MONT2</td><td>CONF2</td><td>2</td><td>24.14</td><td>[0,0]</td></tr><tr><td>CONF6</td><td>6</td><td>21.46</td><td>[7.12,10.74]</td></tr></table>

![](/api/attachments/4DTJMSST/fulltext/images/406da2011d0a157de9d1a658ea1bf5bbfeb3711b53d62a3c3baf745a48483ec5.jpg)  
Fig. 9. Best patrolling configurations identified by the $\mathrm { P } ^ { 3 } .$ -DSS for the shift SATT3 with 2 and 6 patrol sectors. Each sector is represented in a different color. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

Fig. 8 shows the forecast crime risk distribution obtained by the CRFU. Visually, the real and forecast crime distributions appear to be very close.

Concerning the weights and the balance coefficient, we explained the meaning of each attribute in the model to the service coordinator. Then we asked her to rate from 0 to 10 the importance of each attribute and her preference between patrolling efficiency and workload balance. The following values were obtained after normalizing and scaling the figures provided:

• Attribute weights, $( w _ { \alpha \circ } w _ { \beta } , w _ { \gamma } , w _ { \delta } ) = ( 0 . 4 5 , 0 . 0 5 , 0 . 4 5 , 0 . 0 5 )$

• Balance coefficient, $\lambda = 0 . 1$

The objective function values (Eq. (8)) of the standard patrolling configurations are provided in Table 3a.

The MC-PDP was run for 60 s using the parameters provided by the service coordinator. As the optimization algorithm is random in nature, we ran each configuration 50 times, using the forecast data. After that, we evaluated the solutions using the validation data. The 95% confidence intervals of the solution values using the real data are shown in

Table 3b. As expected, the confidence intervals are better (lower) than the objective function values of the corresponding SNPC configurations in all cases.

To understand the real improvement in terms of efficiency resulting from the adoption of the $\mathrm { P } ^ { 3 } \mathrm { - D } \bar { \mathsf { S } } \mathsf { S } ,$ we compute the efficiency loss for both types of patrolling configurations.

Table 4 provides the efficiency loss, computed according to Eq. (9), associated to the patrolling configurations currently adopted by the SNPC and the 95% confidence interval of the efficiency loss relative to the solutions identified by the $\mathrm { P } ^ { 3 } .$ -DSS. For this experiment the operational envelope was approximated by running the optimization algorithms on the validation data. The results in the table show that there is a significant improvement in terms of efficiency when implementing the configurations identified by the $\mathrm { P } ^ { 3 } .$ -DSS. These results confirm the usefulness of the $\mathrm { P } ^ { 3 } { - } \mathrm { D } \mathsf { S } \mathsf { S }$ as a policing DSS for the data and the parameters considered in the experiments.

Figs. 9–11 show the best patrolling configurations obtained by the $\mathrm { P } ^ { 3 } .$ -DSS for the three shifts considered. We can see that these patrol sectors have significant differences from those currently in use (Fig. 6). Some insights will be given in the following:

• SATT3: Police activity is focused on the Gran Via, the main artery of the city that runs from the top-left corner of the district to the center, and then goes toward the east. The reason for that is that the Gran Via and its surroundings are very popular nightlife areas.

(a)  
![](/api/attachments/4DTJMSST/fulltext/images/937d7b253b643f4810e189562425945e206aa9ce5b5c2fe195ce438eb50fa179.jpg)

(b)  
![](/api/attachments/4DTJMSST/fulltext/images/090746899548d7ae229f74e744f64743d22564ef3d6afe931f41537203f79168.jpg)  
Fig. 10. Best patrolling con gurations identi ed by the $\mathrm { P } ^ { 3 } .$ -DSS for the shift SUNT1 with 2 and 6 patrol sectors. Each sector is represented in a different color. (For interpretation of the references to color in this gure legend, the reader is referred to the web version of this article.)

![](/api/attachments/4DTJMSST/fulltext/images/fe35a4c1cd06203fa77926b8a0ee3ebebfb9635f6d3760a4f724413a93689913.jpg)  
Fig. 11. Best patrolling configurations identified by the P<sup>3</sup>-DSS for the shift MONT2 with 2 and 6 patrol sectors. Each sector is represented in a different color. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

• SUNT1: The patrolling configuration concentrates on the southern part of the district, where most of the crimes happen on Sunday morning because of the popular flea market.

• MONT2: The city is uniformly partitioned between north-east and south-west. The configuration with 6 patrol sectors assigns higher importance to the central-western part of the district, corresponding to the commercial area.

## 6. Conclusions

This study represents a first step toward a comprehensive system based on mathematical algorithms, providing an objective and effective approach to decision-making for public security police officers. Specifically, we made use of predictive techniques for controlling the variability of crime in sufficiently small spatial areas, to subsequently develop a tool to help in the management of a proper geographical distribution of the available patrols in a concrete police shift. To evaluate this new approach, we applied our models to predict property crimes in the Central District of Madrid. Based on our assessments with the real criminal incident data, our models can not only predict future incidents accurately but also determine a very efficient police distribution in a district. Other contributions made by this paper are a methodology for the temporal and spatial description of indeterminate crime events, and an algorithm for the computation of the operational envelope of the problem under analysis.

Despite the very promising results obtained, there is still room for improvement. In fact, the SNPC is currently enhancing the Reports DB to support the geolocation of the events, rather than relying on written descriptions. Also, the forecasting models in the CRFU might be extended to include additional variables such as weather conditions (e.g., amount of rain, temperature), special events (e.g., demonstrations, sport events, parades), and social network posts (e.g., Twitter, Instagram). The addition of these and other correlated variables should result in better crime risk predictions. Finally, the optimization model in the PSOU could be adapted to consider census districts instead of the grid structure. Apart from eliminating the issue of determining the size of the grid cells, this would simplify the exchange of information and data among public agencies.

This research represents a first step toward the implementation of a comprehensive DSS for police corps that provides support for all the operations carried out by police agencies. According to some agents in charge of public security in the SNPC, the most interesting features would be (1) the definition of a system for the objective evaluation of the effectiveness of an agent and (2) a model capable of determining the minimum number of agents required in a specific future shift.

We hope that this work will be a useful source of ideas for future research and will foster and encourage more collaborations between police agencies and researchers in the fields of computer science, operations research, mathematics, and statistics.

## Acknowledgments

The authors would like to thank the Spanish National Police Corps personnel of the SEYCO (Statistics and Operative Control Section), the CPD (Data Processing Center), the Sala 091 of Madrid (Police Emergency Call Center), the Central District of Madrid, and the Central District of Granada for their help and collaboration. The investigation of Camacho-Collados was partially financed by the Spanish Police Foundation research grant for civil servants of the Spanish National Police Corps and by the Fulbright Program. The research of Liberatore was supported by the Spanish Government, grant TIN2012-32482. All support is gratefully acknowledged.

## References

[1] R. Benveniste, Solving the combined zoning and location problem for several emergency units, Journal of the Operational Research Society 36 (5) (1985) 0433–0450.

[2] R. Bivand, N. Lewin-Koh, maptools: Tools for Reading and Handling Spatial ObjectsURL: http://CRAN.R-project.org/package=maptools,2014 (R package version 0.8–29).

[3] R. Bivand, C. Rundel, rgeos: Interface to Geometry Engine-Open Source (GEOS)URL: http://CRAN.R-project.org/package=rgeos,2014 (R package version 0.3–4)

[4] R.S. Bivand, E. Pebesma, V. Gomez-Rubio, Applied Spatial Data Analysis with R, Second edition Springer-Verlag, 2013. (URL: http://www.asdar-book.org/).

[5] R.L. Block, C.R. Block, Crime and Place, chapter “Space, Place and Crime: Hot Spot Areas and Hot Places of Liquor-Related Crime”, Criminal Justice Press/Willow Tree Press, 1995. 145–183.

[6] S. Bodily, Police sector design incorporating preferences of interest groups for equal ity and efficiency, Management Science 24 (12) (1978) 01301

[7] P.J. Brantingham, P. Brantingham, Patterns in Crime, Prentice-Hall, 1984.

[8] R.J. Bursik, H.G. Grasmick, Neighborhoods and crime: the dimensions of effective community control, Lexington Books, 1993.

[9] M. Camacho-Collados, F. Liberatore, J.M. Angulo, A multi-criteria police districting problem for the efficient and effective design of patrol sector, European Journal of Operations Research, (2015)http://dx.doi.org/10.1016/j.ejor.2015.05.023.

[10] J.M. Caplan, L.W. Kennedy, Risk Terrain Modeling Compendium, Rutgers Center on Public Security, 2011

[11] J.M. Caplan, L.W. Kennedy, J. Miller, Risk terrain modeling: brokering criminological theory and GIS methods for crime forecasting, Justice Quarterly 28 (2) (2011) 0360–0381.

[12] J. Chaiken, P. Dormont, A patrol car allocation model: background, Management Science 24 (12) (1978) 01280–01290

[13] J. Chaiken, P. Dormont, A patrol car allocation model: capabilities and algorithms, Management Science 24 (12) (1978) 01291–01300.

[14] S. Chaturapruek, J. Breslau, D. Yazdi, T. Kolokolnikov, S.G. McCalla, Crime modeling with Levy flights, SIAM Journal on Applied Mathematics 73 (4) (2013) 01703–01720.

[15] P. Chen, H. Yuan, D. Li, Space–time analysis of burglary in Beijing, Security Journal 26 (1) (2013) 1–15.

[16] R.L. Church, M.P. Scaparra, Analysis of facility systems reliability when subject to attack or a natural disaster, in: A.T. Murray, T.H. Grubesic (Eds.), Critical Infrastructure: Reliability and Vulnerability: Advances in Spatial Science, Springer-Verlag 2007, pp. 221–241.

[17] J. Cohen, Development of Crime Forecasting and Mapping Systems for Use by Police, Technical report, U.S. Department of Justice, 2006.

[18] K. Curtin, K. Hayslett-McCall, F. Qiu, Determining optimal police patrol areas with maximal covering and backup covering location models, Networks and Spatial Economics 10 (1) (2010) 125–145.

[19] K. Curtin, F. Qui, K. Hayslett-McCall, T. Bray, Geographic Information Systems and Crime Analysis, Chapter Integrating GIS and Maximal Coverage Models to Determine Optimal Police Patrol Areas, Idea Group Inc., 2005. 214–235.

[20] S. D'Amico, S. Wang, R. Batta, C. Rump, A simulated annealing approach to police district design, Computers & Operations Research 29 (6) (2002) 667–684.

[21] Z. Friend, Predictive policing: using technology to reduce crime, FBI Law Enforcement Bulletin (2013) URL: http://leb.fbi.gov/2013/april/predictive-policing-usingtechnology-to-reduce-crime.

[22] V. Furtado, A. Melo, A.L.V. Coelho, R. Menezes, R. Perrone, A bio-inspired crime simulation model, Decision Support Systems 48 (1) (2009) 282–292.

[23] M.S. Gerber, Predicting crime using Twitter and kernel density estimation, Decision Support Systems 61 (1) (2014) 115–125.

[24] W. Gorr, R. Harries, Introduction to crime forecasting, International Journal of Forecasting 19 (4) (2003) 551–555.

[25] W. Gorr, A. Olligschlaeger, Y. Thompson, Short-term forecasting of crime, International Journal of Forecasting 19 (4) (2003) 579–594.

[26] R.J. Hyndman, forecast: Forecasting Functions for Time Series and Linear Models URL: http://CRAN.R-project.org/package=forecast, 2014 (R package version 5.4).

[27] R.J. Hyndman, A.B. Koehler, J.K. Ord, R.D. Snyder, Forecasting with Exponential Smoothing: the State Space Approach, Springer-Verlag, 2008.

[28] J.N. Kalcsics, M. Schröeder, Towards a unified territorial design approach — applications, algorithms and GIS integration, TOP 13 (1) (2005) 1–74.

[29] N. Karma, C.Y. Suen, P.F. Guo, Palmprints: a novel co-evolutionary algorithm for clustering finger images, Genetic and Evolutionary Computation — GECCO 2003, volume 2723 of Lecture Notes in Computer Science, Springer-Verlag 2003, pp. 322–331.

[30] L.W. Kennedy, J.M. Caplan, E. Piza, Risk clusters, hotspots, and spatial intelligence: risk terrain modeling as an algorithm for police resource allocation strategies, Journal of Quantitative Criminology 27 (3) (2011) 339–362.

[31] H. Kim, M. O'Kelly, Survivability of commercial backbones with peering: a case study of Korean networks, in: A.T. Murray, T.H. Grubesic (Eds.), 51st Annual North American Meetings of the Regional Science Association International, Springer-Verlag 2004, pp. 107–128.

[32] P.F. Kuo, D. Lord, T.D. Walden, Using geographical information systems to organize police patrol routes effectively by grouping hotspots of crash and crime data, Journal of Transport Geography 30 (1) (2013) 138–148.

[33] S. Li S. Kuo E. Tsai An intelligent decision-support model using ESOM and rule extraction for crime prevention, Expert Systems with Applications 37 (10) (2010) 7108-7119.

[34] P.S. Mitchell, Optimal selection of police patrol beats, The Journal of Criminal Law, Criminology and Police Science 63 (4) (1972) 577.

[35] G. Mohler, M. Short, P. Brantingham, F. Schoenberg, G. Tita, Self-exciting point process modeling of crime, Journal of the American Statistical Association 106 (493) (2011) 100–108.

[36] NIJ, Predictive Policing, http://www.nij.gov/topics/law-enforcement/strategies/ predictive-policing/Pag es/welcome.aspx,2014.

[37] E.J. Pebesma, R.S. Bivand, Classes and methods for spatial data in R, R News 5 (2) (2005) (URL: http://cran.r-project.org/doc/Rnews/).

[38] W.L. Perry, B. McInnis, C.C. Price, S. Smith, J.S. Hollywood, Predictive Policing: The Role of Crime Forecasting in Law Enforcement Operations. Santa Monica, CA:

RAND Corporation (2013) http://www.rand.org/pubs/research\_reports/RR233. Also available in print form.

[39] A.J. Pinizzotto, E.F. Davis, C.E. Miller III., Emotional/Rational Decision Making in Law Enforcement Technical report, Federal Bureau of Investigation. 2004

[40] R. Core Team, R: a Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria, 2014. (URL: http:// www.R-project.org/).

[41] J.H. Ratcliffe, Aoristic signatures and the spatio-temporal analysis of high volume crime patterns, Journal of Quantitative Criminology 18 (1) (2002) 3–43.

[42] M. Safe, J. Carbadillo, I. Ponzoni, N. Brignole, On Stopping Criteria for Genetic Algorithms, in: A.L.C. Bazzan, S. Labidi (Eds.), Advances in Artificial Intelligence — SBIA 2004, volume 3171 of Lecture Notes in Computer Science, Springer-Verlag 2004, pp. 405–413.

[43] L.W. Sherman, P.R. Gartin, M.E. Buerger, Hot spots of predatory crime: routine activities and the criminology of place, Criminology 27 (1) (1989) 27–56.

[44] M.B. Short, A.L. Bertozzi, P.J. Brantingham, Nonlinear patterns in urban crime: hotspots, bifurcations, and suppression, SIAM Journal on Applied Dynamical Systems 9 (2) (2010) 462–483.

[45] M.B. Short, M.R. D'Orsogna, V.B. Pasour, G.E. Tita, P.J. Brantingham, A.L. Bertozzi, L.B. Chayes, A statistical model of criminal behavior, Mathematical Models and Methods in Applied Sciences 18 (Suppl.:0) (2008) 1249–1267.

[46] M.A. Smith, D.E. Brown, Application of discrete choice analysis to attack point patterns, Information Systems and e-Business Management 5 (3) (2007) 255–274.

[47] P.E. Taylor, S.J. Huxley, A break from tradition for the San Francisco Police: patrol officer scheduling using an optimization-based decision support system, Interfaces 19 (1) (1989) 4–24.

[48] G.E. Tita, J. Cohen, J. Engberg, An ecological study of the location of gang “set space”, Social Problems 52 (2) (2005) 272-299

[49] G.E. Tita, G. Ridgeway, The impact of gang formation on local patterns of crime, Journal of Research in Crime and Delinquency 44 (2) (2007) 208–237.

[50] D. Urban, T. Keitt, Landscape connectivity: a graph theoretic perspective, Ecology 82 (5) (2001) 1205–1218.

[51] X. Wang, D.E. Brown, The spatio-temporal modeling for criminal incidents, Security Informatics 1 (0 2) (2012).

[52] X. Wang, M.S. Gerber, D.E. Brown, “Social Computing, Behavioral — Cultural Modeling and Prediction”, chapter Automatic Crime Prediction Using Events Extracted from Twitter Posts, Springer-Verlag, 2012. 231–238.

[53] D. Weisburd, L. Green, Policing drug hot spots: the Jersey City drug market analysis experiment, Justice Quarterly 12 (4) (1995) 711–736.

[54] D. Weisburd, L. Maher, L. Sherman, Contrasting Crime General and Crime Specific Theory: The Case of Hot Spots of Crime, volume 4 of Advances in Criminological Theory, Transaction Press, 1992.

[55] D. Weisburd, S. Mastrofski, A.M. McNally, R. Greenspan, J. Willis, Reforming to preserve: Compstat and strategic problem solving in American policing, Criminology and, Public Policy 2 (3) (2003) 421–456.

[56] Y. Xue, D.E. Brown, Spatial analysis with preference specification of latent decision makers for criminal event prediction, Decision Support Systems 41 (3) (2006) 560–573.

[57] Y. Zhang, D.E. Brown, Police patrol districting method and simulation evaluation using agent-based model & GIS, Security Informatics 2 (7) (2013).

[58] LR. Zipkin M.B. Short, A.I. Bertozzi Cops on the dots in a mathematical model of urban crime and police response, 19 (5) (2014) 1479-1506

Miguel Camacho Collados is a mathematician, a police inspector of the Spanish National Police Corps, and a PhD candidate of the University of Granada. Currently he is a Fulbright Grant holder and he is visiting the Department of Mathematics of the UCLA as an exchange scholar under the supervision of Prof, Bertozzi.

Federico Liberatore received his PhD in Operational Research in 2010 from the University of Kent, UK. He is a Fulbright Grant holder. His research interests include location analysis, fortification/interdiction models in networks, humanitarian logistics, policing models, and artificial intelligence in games
