---
otero_id: 914
otero_key: "2JWV5NBQ"
title: "Simulation modeling for pandemic decision making: A case study with bi-criteria analysis on school closures"
authors: "Ozgur M. Araz; Tim Lant; John W. Fowler; Megan Jehn"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Simulation modeling for pandemic decision making: A case study with bi-criteria analysis on school closures

Ozgur M. Araz <sup>a,</sup>⁎, Tim Lant <sup>b</sup>, John W. Fowler <sup>c,d</sup>, Megan Jehn <sup>e</sup>

<sup>a</sup> Health Promotion, Social & Behavioral Health Department, College of Public Health, University of Nebraska Medical Center, Omaha, NE, USA <sup>b</sup> Decision Theater, Arizona State University, Tempe, AZ, USA

<sup>c</sup> Supply Chain Management Department, W.P. Carey School of Business, Arizona State University, Tempe, AZ, USA

<sup>d</sup> Industrial and Systems Engineering Department, Arizona State University, Tempe, AZ, USA

<sup>e</sup> School of Health Policy and Management, W.P. Carey School of Business, Arizona State University, Tempe, AZ, USA

## a r t i c l e i n f o

Available online 6 October 2012

Keywords: Pandemic in<sup>fl</sup>uenza preparedness School closure Simulation-modeling Decision analysis

## a b s t r a c t

Pandemic in<sup>fl</sup>uenza continues to be a national and international public health concern, and has received signi<sup>fi</sup>cant attention worldwide with the A/H1N1 in<sup>fl</sup>uenza outbreak in 2009. Many countries, including the United States, have developed preparedness plans for an in<sup>fl</sup>uenza pandemic. Preparedness plans are falling under renewed scrutiny as decision-makers apply new <sup>fi</sup>ndings and seek key leverage points for more effective preparedness and response. School closure has been recommended by the World Health Organization as one of the best ways to protect children and other susceptible individuals at the early stages of the pandemic. However, school closure is a dif<sup>fi</sup>cult mitigation policy to implement from both strategic and operational points of view. Challenges include impacts on alternative education delivery services, such as student meals and after-school oversight, as well as direct and indirect economic outfalls. To help public health decision makers address these issues, we developed an epidemiological simulation tool for pandemic in<sup>fl</sup>uenza which enables users to make decisions during a simulated pandemic. We then designed a school closure tabletop exercise using our simulation model as a decision-support tool for evaluating the effectiveness of school closure as a community mitigation strategy for pandemic influenza. We conducted two exercises in February 2009 for the Arizona Department of Health and Human Services including high-ranking health and education administrators from across the state. The purpose of these exercises was to test the state's pandemic preparedness plans with respect to school closure timing and impact. The exercises required participants to make (hypothetical) strategic and operational decisions to mitigate the impacts of pandemic in<sup>fl</sup>uenza at the state and local levels. Our simulation and decision analysis tool was used to assess the impact of key decisions in the exercises. This paper presents the technical details involved in the design and evaluation of this pandemic decision-support tool. Based on the decisions made in the exercises, we present a bi-criteria decision analysis framework to evaluate analytical results obtained from the simulation model. Our analyses show that sequential school closure and re-opening strategy with a speci<sup>fi</sup>c decision rule gives the best compromised solution in terms of minimizing the total number of infections and providing minimal educational discontinuity.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In 2009, the in<sup>fl</sup>uenza A/H1N1 virus quickly escalated to a global pandemic with sustained human-to-human transmission worldwide [13,41]. This recent in<sup>fl</sup>uenza outbreak highlighted the importance of preparedness activities for all countries in today's global world. Current preparedness efforts for pandemic in<sup>fl</sup>uenza focus on establishing ef<sup>fi</sup>- cient mitigation strategies for communities and planning for delivery of necessary medical services during an outbreak. School closure is a non-pharmaceutical in<sup>fl</sup>uenza mitigation strategy and has been included in the federal guidelines for the Community Strategy for Pandemic In<sup>fl</sup>uenza Mitigation [8]. During the 2009 A/H1N1 in<sup>fl</sup>uenza outbreak, local authorities across the United States closed schools in an effort to decrease in<sup>fl</sup>uenza transmission rates. However, there is limited quantitative and scienti<sup>fi</sup>c evidence available to support the ef<sup>fi</sup>cacy of this in-<sup>fl</sup>uenza mitigation measure, which has profound legal, economic, and social implications.

Tabletop exercises are used by many agencies and organizations in preparation for various disasters. A tabletop exercise is an informed discussion by responsible authorities for testing the theoretical and hypothetical capabilities in response to a disaster, such as pandemic in<sup>fl</sup>uenza [3]. These exercises are bounded by a scenario or set of scenarios and include public health professionals and policy-makers responding to prompted discussion questions. Although tabletop exercises for pandemic in<sup>fl</sup>uenza preparedness have not typically included computer-based simulation models, decision support systems or multi-media enabled narrative and real-time feedback systems [7,36], these tools are becoming increasingly important for public health managers for surveillance, prediction and decision analysis [44]. Previous work by Yoon et al. has shown that computer based virtual systems can signi<sup>fi</sup>cantly improve the ability of trainees to respond to dynamic and chaotic environments interactively and collaboratively [43].

In an attempt to test existing in<sup>fl</sup>uenza preparedness plans in Arizona, the Arizona Department of Health and Human Services (ADHS) hosted two tabletop exercises at the Arizona State University Decision Theater on February 12 and February 19, 2009. The Decision Theater is a visualization center where a collaborative decisionmaking environment is supported with various technological tools such as stereo sources, geospatial visualizations and dynamic simulation models. The participants of these exercises included key individuals who are involved in school closure decisions in Arizona (the director of the largest county health department in Arizona, several school superintendents, and Arizona Department of Education representatives). Participants also included school nurses, <sup>fi</sup>rst responders and state, county, and local health of<sup>fi</sup>cials as well as members of Parent Teacher Associations, large community businesses, and policy makers and planners at the K–12 and university levels.

The 2009 in<sup>fl</sup>uenza tabletop exercises at the Decision Theater focused primarily on school closure decisions for pandemic mitigation. These exercises integrated traditional elements of a tabletop design with a computer-based epidemiological simulation model, science-based narratives using mock news videos, a web-based participant collaboration and discussion-feedback tool, and facilitated group discussion. Participants of the exercises were prompted to make critical decisions (i.e. when to close schools, how long to close and when to re-open them), which impacted the results of the model.

State health of<sup>fi</sup>cials bene<sup>fi</sup>ted from the simulation model by de-<sup>fi</sup>ning and testing key epidemiological metrics for school closure identi<sup>fi</sup>ed in preparedness plans. The simulation model allowed decision makers to evaluate alternative strategies for making school closure decisions (including duration of closure, timing of closure and number of schools closed) which helped prepare them for making critical school closure decisions during the A/H1N1 outbreak just a few months later. In this paper, we outline the organizational design of the school closure exercises, and explain the technical speci<sup>fi</sup>cations of the supporting simulation–visualization tool. We then present the results generated by the simulation model and analyze them in a bi-criteria evaluation framework. In addition, this paper outlines a case in which a simulation–visualization based decision support tool can be effectively used for practicing policy decision making processes.

## 2. Literature review

Previous research in the <sup>fi</sup>eld of pandemic in<sup>fl</sup>uenza modeling is quite extensive and can be broadly categorized as: 1) modeling the spread of pandemic in a community [4,6], and building geospatial and temporal simulation models to estimate the global path of the pandemic spread [11,17,26,30], 2) evaluating possible non-pharmaceutical and pharmaceutical interventions at the global and local levels [10,14,42] and recently, 3) logistical issues related to the community response and preparedness activities [9].

Agent based models are widely used to analyze the behavioral patterns and its effects on the spread of diseases. Many have used agent-based simulations to model the spread of in<sup>fl</sup>uenza with social contact networks in an individual based modeling framework [9,10,14,20,42]. On the other hand, mathematical insights can be easily obtained with compartmental models, e.g. [16,17,30,31]. In [4] an age-structured, differential equation based disease model is used and in [6] a differential equation based mathematical disease spread model of the 1918 pandemic is presented. In this paper, we also present an age structured, differential equation based disease spread model for pandemic in<sup>fl</sup>uenza. We chose to use a deterministic compartmental model because of the computational dif<sup>fi</sup>culties that may arise in a real-time scenario-based exercise. The differences between stochastic agent based simulation modeling of disease spread with deterministic compartmental models and the convenience of these different modeling types in real time preparedness and planning exercises have been reviewed previously [2].

In addition to the papers listed above on modeling techniques, there is a substantial body of literature on the quantitative analysis of the effectiveness and cost effectiveness of school closure strategies under possible pandemic scenarios. Several studies have investigated the impact of school closures on cumulative in<sup>fl</sup>uenza attack rates; however, they do not present any of the social and economic costs of school closures [22,25,34,35]. Other studies have demonstrated that school closures can have a signi<sup>fi</sup>cant impact on the basic reproduction number and spread of disease [15,18–20]. Economic costs of school closures are also investigated but these studies do not simultaneously evaluate the epidemiological impact of school closures [23,32]. In a study by Sander et al. [33] the authors analyzed the cost effectiveness of 26 weeks of school closure in conjunction with other policies. However, this duration of school closure is likely to be viewed as impractical when there are uncertainties about the virulence of the epidemic. In another recent study evaluating various in<sup>fl</sup>uenza mitigation policies and including a single school closure policy option, the authors conclude that for a moderately severe pandemic, school closures can be a cost effective intervention [28]. Finally, multidisciplinary and system approaches have been suggested to evaluate school closure policies for pandemic in<sup>fl</sup>uenza because of its complex epidemiological effects as well as the impact on multiple dimensions of social and business life [5]. In a previous analysis of Arizona in<sup>fl</sup>uenza cases, we evaluated the effect of scheduled winter break school closures on the occurrence of in<sup>fl</sup>uenza among children and demonstrated that school closures may prevent or delay as much as 42% of potential in<sup>fl</sup>uenza cases among school-age children [40]. Here, we use our epidemiological model to simulate the spread of pandemic in<sup>fl</sup>uenza in multiple communities to answer several questions about the timing and methods of school closures by integrating decision analytics and disease spread modeling.

## 3. System design and integration for dynamic decision making

For pandemic preparedness exercises, we have taken a systems approach and <sup>fi</sup>rst developed a geospatial and age structured simulation model of in<sup>fl</sup>uenza spread in Powersim, a system dynamics modeling and simulation software [29]. This model is fed with several parameters which are statically stored in an excel spreadsheet. The simulation model is also connected to a central database where several inputs and resulting outputs from the model are kept in different forms (spreadsheets, raster etc.). Through the simulation model– database integration, as presented in Fig. 1, we transfer the outputs generated by the model to this database for generating visualizations. These visualizations are generated for the decision makers in different platforms such as Google Earth and Quantum GIS, an open source geographic information system, where participants can visualize the geographic and temporal spread of in<sup>fl</sup>uenza. Examples of some visualizations generated in one of the exercises are presented in Appendix D.

In a dynamic decision making environment, visual tools (i.e. graphs, maps etc.) can help decision makers, who are responsible for implementing appropriate policies for multiple communities in a wide geography, to better understand the risks about an ongoing public health crisis. After visualizing the situation through geo-special maps and tables/<sup>fi</sup>gures with epidemiologic parameters (number of cases, attack rate, etc.), decision makers can implement policies to minimize the impact of the outbreak in their communities. In the next section, we present the mathematical details of the developed simulation model.

![](/api/attachments/2JWV5NBQ/fulltext/images/825e0b9a0e2558c1956020222dee5e8a5bf078010d01da04d6c855e030c1b00c.jpg)  
Fig. 1. System integration for simulation–visualization during public health exercises.

## 3.1. Simulation model

The disease simulation model is a compartmental and deterministic susceptible (S)–exposed (E)–infected (I)–removed (R) model based on a set of differential equations [1]. In our model we have counties of the state as the communities and each county is divided into <sup>fi</sup>ve age groups (preschool, elementary, middle, high school children and adults). The counties are connected to each other through a travel network in which working adults are assumed to be traveling from one county to another and in this way the geographical spread of the disease is formulized. The transfer of the disease from one county to another is shown in Fig. 2 with the mixing structure in counties [27]. To formulate our geospatial disease spread model we de<sup>fi</sup>ned a set I, as I = set of counties, $i { \in } I = \{ 1 , . . . , 1 5 \}$ and set J, j∈J={PS,ES,MS,HS,adults} as the set of age groups.

Let K be the set of links in a transportation network with the daily commuting of working adults as the <sup>fl</sup>ow in the network. We used US census data of commuting workers for the traveling individuals between the counties [38]. Based on this data source for the travel network, our model has the characteristics of a fully connected network [38]. Let $T = \left( t _ { i , l } \right)$ be a symmetric transport matrix where $t _ { i , l }$ equals the total number of individuals in county i traveling to county l. Each county i has model variables for susceptible, S (t), exposed, $E _ { i }$ (t), infected, I (t) and recovered, R (t). The variable D (t) represents those who do not recover (i.e. die). Let Ω : $R ^ { I } {  } R ^ { I }$ be the transport operator de<sup>fi</sup>ned on the susceptible and exposed compartments as given in Eqs. (1) and (2). The transport operator adjusts the total number of susceptible and exposed adults in each county at each simulation time as it was introduced by Rvachev and Longini in [30]. We assume that infected individuals are not commuting during their infection period (i.e. they are either staying at home or hospitalized), therefore the transport operator is not applied to this compartment for daily commute adjustments [12,16,30].

$$
[ \Omega (S _ {i} (t)) ] = S _ {i} (t) + \sum_ {\{l | (l, i) \in K \}} \left(t _ {l, i} \frac {S _ {l} (t)}{N _ {l}}\right) - \sum_ {\{l | (i, l) \in K \}} \left(t _ {i, l} \frac {S _ {i} (t)}{N _ {i}}\right)\tag{1}
$$

$$
[ \Omega (E _ {i} (t)) ] = E _ {i} (t) + \sum_ {\{l | (l, i) \in K \}} \left(t _ {l, i} \frac {E _ {l} (t)}{N _ {l}}\right) - \sum_ {\{l | (i, l) \in K \}} \left(t _ {i, l} \frac {E _ {i} (t)}{N _ {i}}\right)\tag{2}
$$

Because Ω $R ^ { I } \to R ^ { I }$ is a linear operator we can use it in our differential equation based SEIR model described below. In Table 1 we present the notation for the parameters used in our model, values and also the references for these parameter values.

![](/api/attachments/2JWV5NBQ/fulltext/images/dd65012385f3ec6fe637f4280f0ce7d99621b16a92c7bc17bed0ff09997e8b0b.jpg)  
Fig. 2. Transfer of the disease from one county to another and the mixing structure (PS: preschool, ES: elementary school, MS: middle school, HS: high school children)

Notation for the model parameters.

<table><tr><td>Parameter symbol</td><td>Definition</td><td>Values</td><td>References</td></tr><tr><td> $\beta_{ij}$ </td><td>Contact rate of age group j in county i</td><td>See Table 2</td><td>[39]</td></tr><tr><td> $\alpha_j$ </td><td>Age specific infection rate</td><td>See Appendix A</td><td>[24]</td></tr><tr><td> $\mu$ </td><td>Infectious mortality rate (case fatality rate)</td><td>2%</td><td>[26]</td></tr><tr><td> $\gamma$ </td><td>Recovery rate for infected people</td><td>0.285(3.5 days of infectious period)</td><td>[6]</td></tr><tr><td> $\sigma$ </td><td>Rate of progression from exposed to infected</td><td>0.5(2 days of latent period)</td><td>[6]</td></tr><tr><td> $N_{ij}$ </td><td>Number of people in county i age group j</td><td>See Appendix B</td><td>[38]</td></tr></table>

## 3.2. The disease spread model

The sets of equations for modeling the in<sup>fl</sup>uenza dynamics are presented as:

$$
\frac {d S _ {i j} (t)}{d t} = - \alpha_ {j} \Omega \left(S _ {i j} (t)\right) \left[ \sum_ {k \in J} \beta_ {i k} \left(\frac {\left(\Omega \left(E _ {i k} (t)\right) + I _ {i k} (t)\right)}{N _ {i k}}\right) \right]\tag{3}
$$

$$
\frac {d E _ {i j} (t)}{d t} = \alpha_ {j} \Omega \left(S _ {i j} (t)\right) \left[ \sum_ {k \in J} \beta_ {i k} \left(\frac {\left(\Omega \left(E _ {i k} (t)\right) + I _ {i k} (t)\right)}{N _ {i k}}\right) \right] - \sigma \Omega \left(E _ {i j} (t)\right)\tag{4}
$$

$$
\frac {d I _ {i j} (t)}{d t} = \sigma \Omega \Big (E _ {i j} (t) \Big) - \mu I _ {i j} (t) - \gamma I _ {i j} (t)\tag{5}
$$

$$
\frac {d R _ {i j} (t)}{d t} = \gamma I _ {i j} (t)\tag{6}
$$

$$
\frac {d D _ {i j} (t)}{d t} = \mu I _ {i j} (t).\tag{7}
$$

The contact rate $( \beta _ { i j } )$ captures the mixing in each age group (i) with the mixing between the other age groups of any county (j). The values that we use in our simulation model for mixing rates, i.e. average daily contacts of individuals between the age groups and within their own age groups are presented in Appendix A and are based on [39]. These numbers are obtained after calibration studies to achieve age speci<sup>fi</sup>c attack rates presented in [24]. Because each individual, except the index case, is assumed to be susceptible at the beginning of the simulations, the decrement in the susceptible compartment of an age group in a county is formulated with an adjustment on the number of susceptible individuals traveling in and out of each county, as given in Eq. (3). The decrement in the susceptible compartment of an age group is added to the exposed compartment at each simulation time and the rate of decrement by time in the exposed compartment is given with the latent period $( \sigma ^ { - 1 } )$ as in Eq. (4). Because of the natural history of in<sup>fl</sup>uenza, the individuals who are exposed to the disease progress to the infectious stage after the latency period and they are accumulated in the infectious compartment of the model as given in Eq. (5). After the infectious period, the individuals either recover with a given rate as in Eq. (6) or die as given in Eq. (7). See Appendix C for the schematic representation of the model. These disease dynamics are assumed to be valid for any age group in any county with the appropriate parameter values.

In the Case study section, we present the analysis and results obtained from the simulation model based on different strategies during the hypothetical in<sup>fl</sup>uenza pandemic. These results were obtained with a severe pandemic scenario that has the basic reproductive ratio $\left( R _ { 0 } \right)$ of 2.1 as an initial condition in the model; and $R _ { 0 }$ is calculated as a function of the mean contact rate, infectious period and infection rate. This ratio is speci<sup>fi</sup>cally important for epidemiologists to quantify the transmissibility of the disease and it is de<sup>fi</sup>ned as the expected number of secondary infections arising from a single individual during the entire infectious period, in a totally susceptible population [6,21]. Any change in the contact rate caused by the implementation of a social distancing policy decreases the value of the reproductive ratio and this helps in mitigating the effects of pandemic in<sup>fl</sup>uenza. Since it is very dif<sup>fi</sup>cult to estimate the exact value of $R _ { 0 }$ for pandemic in<sup>fl</sup>uenza, Longini et al. discussed the stochastic modeling of $R _ { 0 }$ to capture more realistic social context and behavioral patterns in pandemic modeling [24] (see Appendix E, for the analysis of the $R _ { 0 }$ value on the peak of infections and the timing of the peak in the student population).

## 3.3. Decision-making environment and exercising pandemic preparedness plans

In order to create a dynamic decision-making environment that re<sup>fl</sup>ected real-world contexts and constraints, the pandemic preparedness exercises included a set of scenario based tabletop questions supported by an interactive simulation model. The model was developed speci<sup>fi</sup>cally for the exercise as a tool to provide realistic and timely constraints for school closure decision-making. It generated outcomes based on speci<sup>fi</sup>c decisions made during the exercises. Primary decisions involved when to close schools and in which counties to close schools. Because we assumed that none of the pharmaceutical interventions can be in use at the early stages of the pandemic, (caused by a novel in<sup>fl</sup>uenza virus) the impact of the mitigation policy (i.e. school closure) implemented at any county or in the whole state is assumed to be limited on changing the contact rate of individuals in the geographic area. The changes in the contact rate of individuals due to school closure policies are presented in Table 2. The school policies can include canceling all school activities, i.e. closing schools, or limiting activities while the schools are open, e.g. eliminating social and sportive gatherings. If decision makers decide to cancel all school activities, we assume that the school age population will have contacts limited to their households [39]. On the other hand, if school activities are limited (e.g. no after school activities) we assume that their contacts are reduced to half of their contacts during normal school days [39].

The numbers of infections at each county were reported throughout the exercises. Key questions and responses were organized, facilitated and recorded using group collaborative tools [37]. The decision making environment and supporting tools in pandemic preparedness exercises were designed to test speci<sup>fi</sup>c capabilities of responsible agencies. The main objectives of these exercises were: 1) to evaluate the communication pathways and mechanisms between schools and community stakeholders (e.g. parents, employees, families and community groups); between school districts; between districts and county agencies; between county, state, and federal agencies; 2) to prepare schools, school districts, health of<sup>fi</sup>cials, and other interested stakeholders for the impact of pandemic in<sup>fl</sup>uenza related school closure on families, employees, community events, physical plants, emergency operations, distance learning, <sup>fi</sup>nancing, and support services; 3) to cover planning gaps associated with the inter-pandemic period including school re-opening and re-closure; and 4) to clarify and delineate the roles of various entities involved in a pandemic in<sup>fl</sup>uenza-related school closure (schools, districts, counties, state, federal, etc.).

Changes in contacts by school closure policies.

<table><tr><td>Daily contacts (people/day)</td><td>Normal</td><td>Activities limited</td><td>Schools closed</td></tr><tr><td>Elementary schools</td><td>20</td><td>10</td><td>5</td></tr><tr><td>Middle schools</td><td>30</td><td>15</td><td>5</td></tr><tr><td>High schools</td><td>40</td><td>20</td><td>5</td></tr></table>

![](/api/attachments/2JWV5NBQ/fulltext/images/e1ad01ba383b4142a6cf85d0ac905f3b0c32a4d2bd36df2c79dfcf1163d9fa46.jpg)  
Fig. 3. Map of Arizona counties presented with their populations [38].

## 4. Case study

This section explains the details of the exercises that took place in February 2009 at the Decision Theater of Arizona State University. The developed simulation–visualization tool was used to facilitate and coordinate these exercises for the Arizona Department of Health Services (ADHS). The exercise participants tested their pandemic preparedness plans with respect to school closure timing and impacts.

## 4.1. The exercise scenario

Both of the exercises were initiated with the same scenario based on an in<sup>fl</sup>uenza pandemic caused by H5N1 (avian) virus, originating in Thailand, subsequently spreading to the United States, and then to Arizona where the <sup>fi</sup>rst case appeared in Yuma County on February 25th (see Fig. 3). At this point in the scenario, participants were informed that hundreds of cases have been detected in the US, and the decision makers were asked to make decisions regarding school closure and re-opening. A summary of the scenario is presented in Table 3.

Summary of the exercise scenario.

<table><tr><td>Date</td><td>Scenario summary</td></tr><tr><td>Jan 1</td><td>• Cases of pandemic influenza are reported in Thailand• Strain is confirmed to be H5N1 and transmission is person to person</td></tr><tr><td>Jan 12</td><td>• Beginning stages of worldwide pandemic• Cases of H5N1 in Germany, UK, China, and Indonesia• Several health ministries in European countries have issued advisories regarding local and international travel• Pandemic virus is likely to reach the United States in 4-6 weeks</td></tr><tr><td>Feb 10</td><td>• First case of H5N1 confirmed in the US• Major cities throughout the United States are reporting suspected cases of the same virus. There is currently no virus detected in Arizona</td></tr><tr><td>Feb 15</td><td>• First confirmed cases of H5N1 in California and New Mexico• The World Health Organization (WHO) has now declared that we are at level 5 of the pandemic alert• No federal/state declaration of emergency has been made at this time</td></tr><tr><td>Feb 25</td><td>• The H5N1 outbreak reaches Arizona, an elementary school student in Yuma is the first confirmed case• The WHO declares that we are in phase 6 – the pandemic phase – and there are confirmed cases in the United States• Hundreds of cases have been detected across the US</td></tr><tr><td>March 15</td><td>• A Yuma elementary student dies – the first H5N1 fatality in Arizona• Additional H5N1 cases are reported in several middle and high schools in Yuma</td></tr><tr><td>March 19</td><td>• Emergency rooms filled to capacity• Hospitals are reporting supply shortages</td></tr><tr><td>March 21</td><td>• Governor declares a state of emergency.• The number of cases in Arizona continues to increase</td></tr><tr><td>April 20</td><td>• Highways, malls, grocery stores, movie theaters and other public places remain empty• Businesses are struggling• Economy is down</td></tr><tr><td>April 30</td><td>• The Governor rescinds her order for school closure• Schools begin the process to re-open and resume activities• Business is returning to normal</td></tr><tr><td>June 6</td><td>• Arizona influenza cases are steadily declining.• Florida and California are reporting an increase in new influenza cases• A second wave of the pandemic appears likely to hit the US in the coming months</td></tr></table>

![](/api/attachments/2JWV5NBQ/fulltext/images/fd4b86a5a4c5bde348525685c0b21c401caa176e74755c284dddeb288fd0b233.jpg)  
Fig. 4. Key decision points for the exercise on Feb 12th, 2009.

## 4.2. The scenario decisions

As the exercise progressed, the participants were asked to make several decisions about closing schools after having the <sup>fi</sup>rst con<sup>fi</sup>rmed case in the state. In Arizona, county health of<sup>fi</sup>cers ultimately have the authority to close schools in their jurisdiction. Interestingly, the school closure decision making process, and triggers for closing, generated a substantial amount of discussion and confusion among participants.

Given the interactive simulation component of the exercise, participants were given the option of initiating school closure at any point during the scenario. The school closure could be implemented on an individual county level or statewide. Similarly, participants were also allowed to decide when and how to re-open schools after the closure. Participants were asked to determine whether schools should be re-opened statewide or separately by county, and whether the re-opening should be unconditional or limited to restricted activities (e.g. no sporting events, group works, etc.). The duration of school closure had a substantial impact on the health outcomes of the modeled pandemic throughout the state. In the exercise, Figs. 4 and 5 summarize the group decisions for each of the exercises against key scenario events.

## 4.3. Quantitative analysis and results

In this section, we analyze several decision pathways, including the ones generated in the actual exercise, via the simulation model. The decision pathways analyzed in this section are: 1) no interventions; 2) Exercise 1 results; 3) Exercise 2 results; 4) early school closure/ limited re-opening; and 5) sequential closure/re-opening. These decision pathways are compared and evaluated in terms of several epidemiological metrics. The epidemiological metrics are: 1) percentage of total population infected or cumulative attack rate (CAR); 2) mortality rate (percent of the population who have died from H5N1); 3) peak percent of infections (percentage of the population who have been infected at the peak) and 4) peak date (the day when infections have reached the peak value). We also de<sup>fi</sup>ne the educational loss to be the total number of student school days lost due to closure and calculate it with Eq. (8). TEL is the total educational loss (students∗day), S is the total number of students in county i, and TSC is the total days of school closure in county i. The results for each set of decision pathways are discussed below and summarized in Table 4.

$$
T E L = \sum_ {i \in I} S _ {i} T S C _ {i}\tag{8}
$$

## 4.3.1. No intervention (base run)

In this scenario, we ran the simulation without applying any nonpharmaceutical or pharmaceutical interventions. Without implementing any mitigation policies, a cumulative infection rate of 51.70% in the whole state population and of 55.03% in the student population were obtained, respectively. In addition, mortality rates were 1.36% and 1.65% in the overall and student populations, respectively. These results are important in terms of measuring the effectiveness of social distancing policies and school closures. The peak percentage of infections (10%) was observed 57 days after the day when the <sup>fi</sup>rst infectious case was introduced in the community (on April 21st). In Fig. 6, we present the total student infections in the state, student infections of Yuma County (where the <sup>fi</sup>rst case was introduced) and the student infection curves of the two most populated counties in the state, Maricopa and Pima Counties, respectively. As illustrated in Fig. 6, the pandemic only has one peak and it is very severe if no intervention strategy is applied. Note that the scale of the y-axis is different in Figs. 6, 7, 8 and 9.

![](/api/attachments/2JWV5NBQ/fulltext/images/a0508b787eca2d9913e69f2535377bef14040c285ff8ca2dac963e61889e8d07.jpg)  
Fig. 5. Key decision points for the exercise on Feb 19th, 2009.

Table 4  
Comparison of different scenarios.

<table><tr><td>Comparison metrics</td><td>No intervention</td><td>Exercise result 1</td><td>Exercise result 2</td><td>Early closure/limited re-opening</td><td>Sequential closure/re-opening</td></tr><tr><td>Total infected population</td><td>3,073,305</td><td>2,681,579</td><td>2,501,459</td><td>2,679,016</td><td>2,641,158</td></tr><tr><td>Infected population (%)</td><td>51.70</td><td>45.12</td><td>42.08</td><td>45.07</td><td>44.43</td></tr><tr><td>Total students infected</td><td>653,752</td><td>232,087</td><td>37,917</td><td>229,133</td><td>188,362</td></tr><tr><td>Students infected (%)</td><td>55.03</td><td>20.50</td><td>3.35</td><td>20.24</td><td>16.64</td></tr><tr><td>Total deaths in population</td><td>81,017</td><td>68,969</td><td>63,427</td><td>68,882</td><td>67,707</td></tr><tr><td>Deaths in population (%)</td><td>1.36</td><td>1.16</td><td>1.07</td><td>1.15</td><td>1.14</td></tr><tr><td>Total student deaths</td><td>18,672</td><td>6623</td><td>1083</td><td>6538</td><td>5363</td></tr><tr><td>Student deaths (%)</td><td>1.65</td><td>0.59</td><td>0.10</td><td>0.58</td><td>0.47</td></tr><tr><td>Peak student infections (%)</td><td>10.00</td><td>1.33</td><td>1.57</td><td>1.31</td><td>3.72</td></tr><tr><td>Peak day</td><td>61</td><td>174</td><td>27</td><td>173</td><td>40</td></tr><tr><td>Number of days closed</td><td>0</td><td>56</td><td>285</td><td>42</td><td>Varies by county</td></tr><tr><td>Students day missed</td><td>0</td><td>61,592,768</td><td>340,965,880</td><td>49,695,880</td><td>49,695,880</td></tr></table>

## 4.3.2. Exercise 1 (2/12/09) results

During Exercise 1, participants chose to close schools in Yuma County following the <sup>fi</sup>rst reported pandemic case in Arizona (on Feb 25th). After the <sup>fi</sup>rst reported death in Arizona (on March 5th), participants chose to close all schools across the state. Schools remained closed for 56 days and were re-opened after the Governor rescinded her order for school closure (April 30th). These decisions resulted in an overall statewide infection rate of 45.12%, student infection rate of 20.50% and a mortality rate of 0.59% in the student population. As shown in Fig. 7, the majority of these infections and mortalities were concentrated in Maricopa County due to the large population in this county. Also of note is that the decision to re-open schools resulted in an increase in student infections and deaths during a second wave of the pandemic which began at the end of July.

## 4.3.3. Exercise 2(2/19/09) results

During Exercise 2, participants chose to close schools in Yuma following the <sup>fi</sup>rst pandemic death in Arizona. A statewide school closure was then implemented after the Governor declared a state of emergency for Arizona. Participants elected not to re-open schools during this exercise for fear of a second pandemic wave. These decisions resulted in an overall statewide infection rate of 42.08%, student infection rate of 3.35% and a total mortality rate of 0.10% in the student population. From an epidemiologic perspective, an interesting result from this exercise was the apparent elimination of a second pandemic wave. As shown in Fig. 8, the pandemic peaked in March; however, prolonged school closure decreased contact rates and resulted in a pandemic which quickly died out.

![](/api/attachments/2JWV5NBQ/fulltext/images/505fb06ff49863755e876063860c5212c157673f68eed0daaadc3057cd884567.jpg)  
Fig. 6. Estimated infections with no interventions

## 4.3.4. Early closure/limited re-opening

In this section, we ran the simulation with a statewide school clo sure decision on February 25th (the detection of the <sup>fi</sup>rst H5N1 case in Yuma County) and with a limited re-opening decision after 6 weeks of closure. In the limited re-opening decision the schools were open for the essential educational activities only, i.e. the extracurricular and sport activities were restricted. The results of this scenario were very close to the results obtained in the <sup>fi</sup>rst exercise in terms of infections and mortalities in both the student and total population.

## 4.3.5. Sequential closure/re-opening scenario

To gain additional insights on the effects of the school closure and re-opening decisions during a pandemic in<sup>fl</sup>uenza outbreak, we ran an additional scenario in which we closed the schools for 6 weeks duration in each county whenever the number of infections reached a threshold value (4%). In this case, the simulation model generated an infection rate 44.43% for the total state population and 16.64% for the student population. We observed a mortality rate of 1.14% for the state population and 0.047% for the student population. However, as seen in Fig. 9, these set-up decisions did not decrease the peak number of student infections signi<sup>fi</sup>cantly (42,170) or the timing of the peak (40 days from the time the index case was introduced).

![](/api/attachments/2JWV5NBQ/fulltext/images/76e61372f39ca099e44587922ccc04f2e56a0da6794a05bc661ae3812d52f784.jpg)  
Fig. 7. Simulated results of Exercise 1.

![](/api/attachments/2JWV5NBQ/fulltext/images/0ffad6110e8248d593137ba41b5a76ba42ae31027c02382e5c56fe66002beab5.jpg)  
Fig. 8. Estimated infections of Exercise 2.

4.4. Bi-criteria analysis of school closure decisions: health vs. educational loss trade-offs

In Table 3, we present a comparative analysis of the scenarios described above. For Exercise 1, the results from the group decisions were very close to early closure/limited re-opening in terms of the number of infections and mortalities. Delaying school closures did not appear to substantially increase the percentage of the total population that became infected. For Exercise 2, the group results were signi<sup>fi</sup>cantly better than the early closure/limited re-opening and the no intervention scenarios. The decision about not to re-open schools, signi<sup>fi</sup>cantly reduced the total infection rates and total mortality rates, however due to the educational loss and costs this strategy may not be a practical one.

Obviously, an important question about the school closure in the state is about the economic and educational loss that may be caused in the course of a pandemic. Thus, in Fig. 10 we evaluate the alternative school closure and re-opening strategies in terms of two metrics, number of infections and the total educational loss, which are likely to be two key decision elements in pandemic policy making. In this bi-criteria evaluation graphic we have plotted the results for the <sup>fi</sup>ve scenarios in the previous section. The no interventions, sequential closure, and Exercise 2 scenarios are ef<sup>fi</sup>cient solutions and the decision makers will need to decide which of these is best depending on the relative importance of the number of student infections and the number of student school days lost. Clearly, the sequential closure scenario provides the solution that best balances the two objectives.

![](/api/attachments/2JWV5NBQ/fulltext/images/f90c12e2cbdbe30f35bf36b1f057c90199d1909c004469905cd3e1df0ef93b1e.jpg)  
Fig. 9. Estimated infections of sequential closure scenario

Bi-criteria Comparison of Different School Closure Strategies  
![](/api/attachments/2JWV5NBQ/fulltext/images/0b5b7f60e3dfa5201f4cbf58a21f99fb2a672bd25cb17f900d50575430a971ab.jpg)  
Fig. 10. Bi-criteria evaluation of considered scenarios.

The early closure/limited re-opening and Exercise 1 scenarios also give results that are close to the sequential closure scenario but they are dominated by the sequential closure scenario.

## 5. Conclusions

As we have seen with the recent H1N1 outbreak, the education system could be severely strained during a pandemic. Planning at all levels of response from the federal level down to individual schools is required to meet public health challenges faced by a pandemic. Additionally, roles and responsibilities for all responders and stakeholders must be clearly delineated in response plans, and coordinated exercises must be conducted to prepare our communities, schools, and children for a prolonged school closure.

The Arizona Pandemic In<sup>fl</sup>uenza School Closure Exercises provided a valuable forum for school and health of<sup>fi</sup>cials to collaborate on a comprehensive strategy for closing schools in the event of an in<sup>fl</sup>uenza pandemic. Key strengths identi<sup>fi</sup>ed during this exercise are as follows:

1. All exercise participants agreed that the ultimate authority to close schools within Arizona resides with County Health Of<sup>fi</sup>cers, and that individual district superintendents can also close their schools at will.

2. All participants agreed that early school closure is best; waiting too long results in unnecessary infections and fatalities. Additionally, issues such as distance learning, school meal programs, the challenges of closing and reopening schools during multiple pandemic waves and determining the authority to close schools were raised as important problems to be addressed.

3. The exercises reinforced the importance of collaboration between school districts, public health, and the medical community when deciding to close schools as a community mitigation strategy against a pandemic.

4. The supporting simulation model increased awareness about the possible social and economic impacts of a pandemic by generating outcomes based on various school closure policies. These simulated outcomes helped facilitate discussions among state of<sup>fi</sup>cials to identify the best possible school closure and re-opening policy and ultimately helped state of<sup>fi</sup>cials to practice decision making for future pandemics (which was observed during the H1N1 outbreak just following the completion of these exercises).

From our analysis of the modeling and simulation results, we concluded that mathematical modeling and simulations can inform policy makers by predicting disease spread patterns under multiple scenarios. In addition, these public health exercises brought together public policy makers, emergency preparedness planners and mathematical modelers in real time to improve decision-making around pandemic school closures.

The developed simulation–visualization model which reacts to school closure and re-opening decisions enabled decision makers to test several policies and identify the best strategy in terms of minimizing the total number of infections in schools while minimizing discontinuity in education. The presented bi-criteria evaluation framework for pandemic decision-making contributes to literature by presenting a method for comparing different strategies based on multiple decision making parameters. In addition, this framework helps public health of<sup>fi</sup>cials to analyze multiple scenarios and develop better preparedness strategies. In our analysis, the sequential closure and re-opening with a speci<sup>fi</sup>c decision rule gave the best compromised solution in terms of minimizing the total number of infections and providing minimal educational discontinuity. School closure policies were shown to reduce the peak of infections signi<sup>fi</sup>cantly during the pandemic which has tremendous public health implications. Delaying the peak of the outbreak affords the medical community valuable time to prepare for a surge in the demand for treatment and ensure that medical services can continue. In summary, we believe that our simulation model and exercise program can help public health professionals prepare for various disasters by evaluating the potential impacts of common public health interventions.

## Acknowledgments

We are thankful to the Arizona Department of Health and Human Services and the Public Health Department of Maricopa County for their support and collaboration on the design of the presented exercises and sharing their pandemic preparedness plans with us. We also acknowledge the valuable comments from Dr. Bob England, Director of Public Health Department in Maricopa County during and after the exercises. We acknowledge the help from Dr. Robert Pahle of Decision Theater for his help to generate some visualizations. Finally, we thank two anonymous referees for their insightful comments and suggestions.

## Appendix A. Age speci<sup>fi</sup>c infection rate

<table><tr><td></td><td>Elementary school</td><td>Middle school</td><td>High school</td></tr><tr><td>Age specific infection rates</td><td>0.0145</td><td>0.0125</td><td>0.0105</td></tr></table>

## Appendix B. Number of students in each county in Arizona by age group [38]

<table><tr><td>County</td><td>Total population</td><td>Preschool</td><td>Elementary S.</td><td>Middle S.</td><td>High school</td></tr><tr><td>Apache</td><td>69,343</td><td>140</td><td>5743</td><td>3230</td><td>4259</td></tr><tr><td>Cochise</td><td>126,106</td><td>324</td><td>9166</td><td>4745</td><td>8414</td></tr><tr><td>Coconino</td><td>128,925</td><td>257</td><td>8518</td><td>4219</td><td>8562</td></tr><tr><td>Gila</td><td>51,663</td><td>181</td><td>3742</td><td>1851</td><td>2627</td></tr><tr><td>Graham</td><td>33,073</td><td>94</td><td>3010</td><td>1356</td><td>3262</td></tr><tr><td>Greenlee</td><td>7251</td><td>11</td><td>836</td><td>439</td><td>492</td></tr><tr><td>La Paz</td><td>20,238</td><td>55</td><td>1208</td><td>620</td><td>808</td></tr><tr><td>Maricopa</td><td>3,635,528</td><td>10,030</td><td>326,803</td><td>155,846</td><td>239,412</td></tr><tr><td>Mohave</td><td>187,200</td><td>348</td><td>12,548</td><td>6510</td><td>8101</td></tr><tr><td>Navajo</td><td>108,432</td><td>258</td><td>8902</td><td>4602</td><td>14,125</td></tr><tr><td>Pima</td><td>924,786</td><td>1978</td><td>69,996</td><td>34,975</td><td>45,835</td></tr><tr><td>Pinal</td><td>229,549</td><td>842</td><td>24,407</td><td>11,254</td><td>14,180</td></tr><tr><td>Santa Cruz</td><td>42,009</td><td>111</td><td>4803</td><td>2459</td><td>3415</td></tr><tr><td>Yavapai</td><td>198,701</td><td>327</td><td>12,816</td><td>6858</td><td>9581</td></tr><tr><td>Yuma</td><td>181,277</td><td>529</td><td>16,606</td><td>9104</td><td>11,634</td></tr><tr><td>Arizona total</td><td>5,944,081</td><td>15,485</td><td>509,104</td><td>248,068</td><td>374,707</td></tr></table>

Appendix C. Simple SEIR model with the geospatial and age speci<sup>fi</sup>c dynamics  
![](/api/attachments/2JWV5NBQ/fulltext/images/e7b3d543f3dea8b991bd78e709c75c84b42f3cf0e608a58fb05f1788926eb185.jpg)

Appendix D. Display of the geographic and timely spread of pandemic in<sup>fl</sup>uenza in the state of Arizona

1stof March Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/6fd08794cf8dd0b02bfdda4dcb41eed534f4d4269cae7f09d635fa96b9f27f7b.jpg)

${ } ^ { 2 0 ^ { \mathfrak { h } } }$ of March Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/0af41c410d9ee86c9742870ed225b9acfcdfebe4c995d616e0d4d8858c013e96.jpg)

$2 0 ^ { \mathfrak { t h } }$ of April Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/06e4d6063790c732c5cde84b240fadbf91d944f2d9ed056e7611ea95a2c773c4.jpg)

$3 0 ^ { \mathsf { s t } }$ of April Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/1278b489503f2f710822417c362a27dbedabc3162bd061c94c05ed10e79b3f6d.jpg)

$1 5 ^ { m }$ of May Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/a4d2627c0b4ce6bc49a387d2a0053b9be03e453a6c439764287b6c2e9fd8498f.jpg)

${ 3 0 ^ { \mathfrak { n } } }$ of May Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/1acf47dc6cf1b802f9267c5bd9b126d3e5a9584ef244b18bf2658ff70e8f415b.jpg)

${ } _ { 3 0 ^ { \mathfrak { n } } }$ of June Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/eab7e6521b931e922438ef04e259fe95dc129a3d93177bc97624c0a1bdab641f.jpg)

${ 3 0 ^ { \mathrm { t h } } }$ of July Number of Infections  
![](/api/attachments/2JWV5NBQ/fulltext/images/55f14423df63ea8eb72a2e4119d3524814c4735863f4e4c942be1c0ed291b3a1.jpg)  
Note. This is a snapshot of one scenario and generated maps.

Appendix E. Peak of infections and peak time by $\mathbf { R _ { 0 } }$ for student population

![](/api/attachments/2JWV5NBQ/fulltext/images/6beeda41f797cd84708008c1b1222d7bf804ead513d770c48051977c464dca1a.jpg)  
Note: The affect of the basis reproductive ratio on the peak of infections and the timing of the peak (it is varied from 1.2 to 2.1). In the <sup>fi</sup>gure it can be seen that, as $R _ { 0 }$ increases the spread of the disease becomes faster in school age populations and the peak of infections increases dramatically.

## References

[1] R.M. Anderson, R.M. May, Infectious Diseases of Humans: Dynamics and Control, Oxford University Press, New York, 1991.

[2] O.M. Araz, T. Lant, J.W. Fowler, M. Jehn, A simulation model for policy decision analysis: a case of pandemic in<sup>fl</sup>uenza on a university campus, Journal of Simulation 5 (2011) 89–100.

[3] R. Beaton, A. Stergachis, J. Thompson, C. Osaki, C. Johnson, S.J. Charvat, N. Marsden-Haug, Pandemic policy and planning considerations for universities: <sup>fi</sup>ndings from a tabletop exercise, Biodefense Strategy, Practice and Science 5 (2007) 327–334.

[4] C. Castillo-Chavez, H. Hethcote, V. Andreasen, S.A. Levin, W.M. Liu, Epidemiological models with age structure, proportionate mixing and cross immunity, Journal of Mathematical Biology 89 (1989) 233–258 5J

[5] S. Cauchemez, N.M. Ferguson, C. Wachtel, A. Tegnell, G. Saour, B. Duncan, Nicoll, Closure of school during an in<sup>fl</sup>uenza pandemic, The Lancet Infectious Diseases 9 (8) (2009) 473–481.

[6] G. Chowell, C.E. Ammon, N.W. Hengartner, J.M. Hyman, Transmission dynamics of the great in<sup>fl</sup>uenza pandemic of 1918 in Geneva, Switzerland: assessing the effects of the hypothetical interventions, Journal of Theoretical Biology 241 (2006) 193–204.

[7] D.J. Dausey, J.W. Buehler, N. Lurie, Designing and conducting tabletop exercises to assess public health preparedness for manmade and naturally occurring biologi cal threats, BMC Public Health 7 (2007) 92.

[8] Department of Health and Human Services (US), Community strategy for pandemic in<sup>fl</sup>uenza mitigation. February 2007. [Cited 2011 May 11]. Available from: URL: http://www.pandemic<sup>fl</sup>u.gov/plan/community/mitigation html.

[9] A. Ekici, P. Keskinocak, J. Swann, Pandemic in<sup>fl</sup>uenza response, in: Proceedings of the 2008 Winter Simulation Conference, 1592–1600, Miami, FL, December 2008, 2008.

[10] N.M. Ferguson, D.A. Cummings, S. Cauchemez, C. Fraser, S. Riley, A. Meeyai, S. Iamsirithaworn, D.S. Burke, Strategies for containing an emerging in<sup>fl</sup>uenza pan demic in Southeast Asia, Nature 437 (2005) 209–214.

[11] N.M. Ferguson, D.A.T. Cummings, C. Fraser, J.C. Cajka, P.C. Cooley, D.S. Burke, Strategies for mitigating an in<sup>fl</sup>uenza pandemic, Nature 442 (2006) 448–452.

[12] A. Flahault, S. Degue, A. Valleron, A mathematical model for the European spread of in<sup>fl</sup>uenza, European Journal of Epidemiology 10 (4) (1994) 471–474.

[13] C. Fraser, C.A. Donnelly, S. Cauchemez, W.P. Hanage, M.D. Van Kerkhove, T.D. Hollingsworth L Griffin R E Baggaley H E Jenkins E L Ivons T Jombart W R Hinsley, N.C. Grassly, F. Balloux, A.C. Ghani, N.M. Ferguson, A. Rambaut, O.G. Pybus, H. Lopez-Gatell, C.M. Alpuche-Aranda, I. Chapela, E.P. Zavala, D.M.E. Guevara, F. Checchi, E. Garcia, S. Hugonnet, C. Roth, The WHO Rapid Pandemic Assessment Collaboration, Pandemic potential of a strain of in<sup>fl</sup>uenza A (H1N1): early findings, Science 234 (2009) 1557.

[14] T.C. Germann, K. Kadau, I.M. Longini, C.A. Macken, Mitigation strategies for pandemic in<sup>fl</sup>uenza in the United States, Proceedings of the National Academy of Sciences 101 (16) (2006) 6146–6151.

[15] M.Z. Gojovic, B. Sander, D. Fisman, M.D. Krahn, C.T. Bauch, Modeling mitigation strategies for pandemic (H1N1) 2009, CMAI 181 (10) (2009) 673-677.

[16] R.F. Grais, I.H. Ellis, G.E. Glass, Assessing the impact of airline travel on the geographic spread of pandemic influenza, European Journal of Epidemiology 18 (11) (2003) 1065-1072.

[17] R.F. Grais, J.H. Ellis, A. Kress, G.E. Glass, Modeling the spread of annual in<sup>fl</sup>uenza epidemics in the US: the potential role of the air travel, Healthcare Management Science 7 (2004) 127–134.

[18] N. Halder, J.K. Kelso, G.J. Milne, Developing guidelines for school closure interventions to be used during a future in<sup>fl</sup>uenza pandemic, BMC Infectious Diseases 10 (2010) 221.

[19] N. Hens, G.M. Ayele, N. Goeyvaerts, M. Aerts, J. Mossong, J.W. Edmunds, P. Beutels, Estimating the impact of school closure on social mixing behavior and the transmission of close contact infections in eight European countries, BMC Infectious Diseases 9 (2009) 187.

[20] J.K. Kelso, G.J. Milne, H. Kelly, Simulation suggests that rapid activation of social distancing can arrest epidemic development due to a novel strain of in<sup>fl</sup>uenza, BMC Public Health 9 (2009) 117.

[21] R. Larson, Revisiting R , basic reproductive number for pandemic in<sup>fl</sup>uenza, in: MIT Working Paper Series ESD-WP-2008-10, 2008.

[22] B.Y. Lee, S.T. Brown, P. Cooley, M.A. Potter, W.D. Wheaton, R.E. Voorhees, S. Stebbins, J.J. Grefenstette, S.M. Zimmer, R.K. Zimmerman, T.M. Assi, R.R. Bailey, D.K. Wagener, D.S. Burke, Simulating school closure strategies to mitigate an in-<sup>fl</sup>uenza epidemic, Journal of Public Health Management and Practice 16 (3) (May–Jun. 2010) 252–261.

[23] H. Lempel, R.A. Hammond, J.M. Epstein, Economic cost and health care workforce effects of school closures in the US, PLoS Current In<sup>fl</sup>uenza (October 5 2009) RRN1051.

[24] I.M. Longini, M.E. Halloran, A. Nizam, Y. Yang, Containing pandemic in<sup>fl</sup>uenza with antiviral agents, American Journal of Epidemiology 159 (2004) 623–633.

[25] G.J. Milne, J.K. Kelso, H.A. Kelly, S.T. Huband, J. McVernon, A small community model for the transmission of infectious diseases: comparison of school closure as an intervention in individual-based models of an in<sup>fl</sup>uenza pandemic, PLoS One 3 (12) (2008) e4005, http://dx.doi.org/10.1371/journal.pone.000 4005.

[26] S.M. Mniszewski, S.Y. Del Valle, P.D. Stroud, J.M. Riese, S.J. Sydoriak, Pandemic simulation of antivirals+school closures: buying time until strain-speci<sup>fi</sup>c vaccine is available, Comput Math Organ Theory 14 (2008) 209–221.

[27] K.R. Nigmatulina, R.C. Larson, Living with in<sup>fl</sup>uenza: impacts of government imposed and voluntarily selected interventions, European Journal of Operational Research 195 (2009) 613–627.

[28] D.J. Perlroth, R.J. Glass, V.J. Davey, D. Cannon, A.M. Garber, D.K. Owens, Health outcomes and cost of community mitigation strategies for an in<sup>fl</sup>uenza pandemic in the United States, Clinical Infectious Diseases 50 (2) (2010) 165–174.

[29] Powersim Software AS, http://www.powersim.com2003.

[30] L. Rvachev, I.M. Longini, A mathematical model for the global spread of in<sup>fl</sup>uenza, Mathematical Biosciences 75 (1985) 3-22

[31] I.M. Longini, A mathematical model for predicting the geographic spread of new infectious agents, Mathematical Biosciences 90 (1988) 367–383.

[32] M.Z. Sadique, E.J. Adams, W.J. Edmunds, Estimating the costs of school closure for mitigating an in<sup>fl</sup>uenza pandemic, BMC Public Health 8 (2008) 15.

[33] B. Sander, M.B.A. MecDev, A. Nizam, L.P. Garisson, M.J. Postma, M.E. Halloran, I.M. Longini, Economic evaluation of in<sup>fl</sup>uenza pandemic mitigation strategies in the United States using a stochastic microsimulation transmission model, Value in Health 12 (2009) 226–233.

[34] A. Sasaki, A. Gatewood Hoen, A. Ozonoff, H. Suzuki, N. Tanabe, N. Seki, R. Saito, J.S. Brownstein, Evidence-based tool for triggering school closures during in<sup>fl</sup>uenza outbreaks, Japan, Emerging Infect Disease 15 (2009) 1841–1843.

[35] R.D. Smith, M.R. Keogh-Brown, T. Barnett, J. Tait, The economy-wide impact of pandemic in<sup>fl</sup>uenza on the UK: a computable general equilibrium modelling experiment, BMJ 339 (2009) b4571.

[36] J.L. Taylor, B.J. Roup, D. Blythe, G.K. Reed, T.A. Tate, K.A. Moore, Pandemic in<sup>fl</sup>uenza preparedness in Maryland: improving readiness through a tabletop exercise, Biosecurity and Bioterrorism: Biodefense Strategy, Practice and Science 3 (2005) 61–69.

[37] ThinkTank, GroupSystems, http://www.groupsystems.com/2009.

[38] U.S. Census Data, www.census.gov/main/www/cen2000.html2000.

[39] J. Wallinga, P. Teunis, M. Kretzschmar, Using data on social contacts to estimate age speci<sup>fi</sup>c transmission parameters for respiratory-spread infectious agents American Journal of Epidemiology 164 (2006) 936–944.

[40] C. Wheeler, L. Erhart, M.L. Jehn, In<sup>fl</sup>uence of school closure on the incidence of in-<sup>fl</sup>uenza among school-age children in Arizona, Public Health Report 125 (6) (2010) 851–859.

[41] World Health Organization, Pandemic In<sup>fl</sup>uenza Preparedness and Response, 2009.

[42] J.T. Wu, S. Riley, C. Fraser, G.M. Leung, Reducing the impact of the next in<sup>fl</sup>uenza pandemic using the household-based public interventions, PLoS Medicine 3 (9) (2006) 1532–1540.

[43] S.W. Yoon, J.D. Velasquez, B.K. Partridge, S.Y. Nof, Transportation security decision support system for emergency response: a training prototype, Decision Support Systems 46 (2008) 139–148.

[44] Y. Zhang, Y. Dang, H. Chen, M. Thurmond, C. Larson, Automatic online news monitoring and classi<sup>fi</sup>cation for syndromic surveillance, Decision Support Systems 47 (2009) 508–517.

Ozgur Araz is an assistant professor in the College of Public Health at the University of Nebraska Medical Center. His primary research interests are complex systems thinking, modeling and simulation, modeling chronic and infectious diseases, stochastic optimization, healthcare operations management and sustainable development. He has his Ph.D. in Industrial Engineering from the Arizona State University. His email addres is ozgur.araz@unmc.edu.

Tim Lant is an assistant research professor at the ASU Decision Theater. His research interests are on public health emergency preparedness for emerging pandemics and bioterrorism, public health policy-making, decision-support, analytics, visualization, and simulated emergency preparedness exercises. He earned his Ph.D. in applied mathematics with specialization in mathematical biology at Arizona State University. His email address is lant@asuedu

John Fowler is the Motorola Professor of International Business and Chair of the Supply Chain Management Department in the WP Carey School of Business at Arizona State University (ASU) and a professor of industrial engineering in the School of Computing, Informatics, and Decision Systems Engineering at ASU. His research interests include modeling, analysis, and control of manufacturing and service systems. Dr. Fowler is the founding editor of the IIE Transactions on Healthcare Systems Engineering and is a joint editor of the Journal of Simulation. His email address is john,fowler@asu,edu

Megan Jehn is an associate professor in the School of Health Management and Policy at Arizona State University. Her research interests are public health emergency preparedness and health policy. She has her Ph.D. in epidemiology from the Johns Hopkins Bloomberg School of Public Health. Her email address is megan.jehn@asu.edu.
