---
otero_id: 11964
otero_key: "DJ9PNAVD"
title: "Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Samaritan response"
authors: "Michael Khalemsky; David G. Schwartz"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.07.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Samaritan response

Michael Khalemsky, David G. Schwartz

Graduate School of Business Administration, Bar-Ilan University, Israel

## a r t i c l e i n f o

Article history: Received 25 December 2016 Received in revised form 11 May 2017 Accepted 12 July 2017 Available online xxxx

Keywords: Emergency response Community mHealth Simulation Healthcare policy EMS

## a b s t r a c t

Mobile emergency response applications involving location-based alerts and physical response of networked members increasingly appear on smartphones to address a variety of emergencies. EMS (Emergency Medical Services) administrators, policy makers, and other decision makers need to determine when such systems present an effective addition to traditional Emergency Medical Services. We developed a software tool, the Emergency Response Community Effectiveness Modeler (ERCEM) that accepts parameters and compares the potential smartphone-initiated Samaritan/member response to traditional EMS response for a specific medical condition in a given geographic area. This study uses EMS data from the National EMS Information System (NEMSIS) and analyses geographies based on Rural-Urban Commuting Area (RUCA) and Economic Research Service (ERS) urbanicity codes. To demonstrate ERCEM's capabilities, we input a full year of NEMSIS data documenting EMS response incidents across the USA. We conducted three experiments to explore anaphylaxis, hypoglycemia and opioid overdose events across different population density characteristics, with further permutations to consider a series of potential app adoption levels, Samaritan response behaviors, notification radii, etc. Our model emphasizes how medical condition, prescription adherence levels, community network membership, and population density are key factors in determining the effectiveness of Samaritan-based Emergency Response Communities (ERC). We show how the ef cacy of deploying mHealth apps for emergency response by volunteers can be modelled and studied in comparison to EMS. A decision maker can utilize ERCEM to generate a detailed simulation of different emergency response scenarios to assess the efficacy of smartphone-based Samaritan response applications in varying geographic regions for a series of different conditions and treatments.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

mHealth has been defined as “healthcare to anyone, anytime and anywhere by removing temporal and locational constraints while increasing both the coverage and the quality of healthcare” [1]. Developments in mHealth have led to a sharp increase in the availability of applications (apps) supporting medically motivated physical interaction between app users, leading to potentially significant changes in healthcare delivery [2,3]. Smartphone applications can support the connection of app users to real-world medical emergency events and are being studied in diverse situations such as the mapping and responseuse of AEDs (Automatic Electronic Defibrillators) [4–8], volunteer emergency response [9–14], the physical proximity of diabetes patients in need of glucose or monitors [15], and Emergency Response

Communities (ERC) for anaphylaxis events [16,17]. Such systems have the potential to enable a new form of emergency medical response in which the social network-based connection between individuals creates a lay-layer of support, which can augment or potentially modify current forms of EMS [16]. Many available emergency response apps are based on alerting available responders connected through smartphone social networks. Table 1 presents a few examples.

These apps fall into the category of “providing care” in Varshney's framework for emergency care and m-health enhancements [3]. Two important things that all such emergency support smartphone apps have in common are (a) a dependency on variables related to medical condition/treatment, individual user behavior, online community characteristics, and geographic region; and (b) their potential to improve on existing EMS response times.

Varshney discusses the importance of modeling the ways in which mobile technology can change the ways healthcare services are designed and delivered, emphasizing the “need to study how mobile technologies may affect the quality of healthcare in different scenarios”,

M. Khalemsky, D.G. Schwartz / Decision Support Systems xxx (2017) xxx–xxx

Table 1  
Examples of mHealth apps with an emergency alert component.

<table><tr><td>App name</td><td>Condition focus</td><td>Alert behavior</td><td>URL</td></tr><tr><td>Pulsepoint</td><td>Cardiac</td><td>Notify members with CPR training in vicinity.</td><td>http://www.pulsepoint.org</td></tr><tr><td>HelpAround Diabetes</td><td>Diabetes</td><td>Notify members with monitors, syringes or insulin in area.</td><td>http://helparound.co</td></tr><tr><td>SecuraFone Health</td><td>Stroke, Cardiac</td><td>Notify predefined social network including doctors and caregivers.</td><td>http://www.securafone.com/subpages/health.php</td></tr><tr><td>EpDetect</td><td>Epilepsy</td><td>Notify preset list of up to 3 caregivers</td><td>http://www.epdetect.com/</td></tr><tr><td>AllergyHero</td><td>Anaphylaxis</td><td>Social network of members in vicinity</td><td>http://www.allergyhero.com</td></tr></table>

including emergency care [18]. Decision makers tasked with adopting or promoting the community or regional use of apps as part of emergency response protocols, and possibly integrating the use of smartphonebased Samaritan response to enhance existing EMS infrastructures, have no decision tools designed to study the potential effects of these decisions prior to actual investment in adoption and integration. This presents a gap that we address in our research, taking a modeling approach.

## 1.1. EMS planning

There is substantial research on planning for Emergency Medical Services (EMS). This includes issues such as GIS models for ambulance positioning [19]; analytical tools for evaluating EMS system design changes [20]; DSS incorporating the role of centrality in ambulance dispatching [21]; addressing EMS response times in rural vs urban areas [22] and the use of simulation models to evaluate the performance of EMS [23]. These studies are important in the EMS field, yet have limited applicability for ERC effectiveness assessment for several reasons. EMS operates from fixed dispatch stations compared to ERC which is based on volunteers whose location is neither fixed nor predictable. EMS determines ambulance fleet size and their equipment based on budgetary constraints and resource allocation models, in contrast to the response of ERC volunteers that depends on multiple factors such as their location, location of the patient in distress, volunteer availability, possession of the required medication etc.

## 1.2. ERC planning

Modeling the potential efficacy of smartphone-based community response in emergencies has complexities that stem from the multiplicity of variables and scenarios that must be accounted for. These variables include those related to individual behaviors such as adherence, willingness to respond, community membership, and online availability, as well as macro level data related to population density, and prescription density within a population. Only once the former and latter are considered, meaningful assessments of the effectiveness of such app-based communities can be undertaken with comparisons to existing EMS response times.

The multitude of intervention apps being tested, recommended, and used today do not consider the performance of such apps in comparison to EMS, which is the consensus responder in emergency conditions. EMS administrators, policy makers, and other decision makers need to determine when such systems present an effective addition to traditional Emergency Medical Services [3,24]. This presents a significant gap that we begin to address in our research. Modeling all regions of a large healthcare system for multiple potential emergency response community apps becomes a daunting task requiring substantial time and effort. To make such tasks easier we developed the Emergency Response Community Effectiveness Modeler (ERCEM), which decision makers can use to simulate the effectiveness of smartphone-based emergency response community and assess its potential performance in comparison to EMS response addressing the same medical emergency need. We emphasize that the purpose of such assessment is not necessarily to replace EMS response but rather to see how it might be augmented through community action enabled by such apps. Such assessment is necessary for decision makers because of the costs and efforts of establishing an ERC, advertising and promoting it, integrating it into existing EMS processes and managing the community [25,26]. We illustrate the use of ERCEM by presenting an analysis of simulated Samaritan response to three different types of emergency event – anaphylaxis, hypoglycemia and opioid overdose, drawn from and compared to actual EMS calls and response times. We note that ERCEM is intended to be used at macro level - when making decision about establishment of an ERC in a given region - and not at micro level such a decision if ERC volunteers should be dispatched in a specific event.

## 2. Data and methods

In each of the example mHealth applications described above, help can come in the form of emergency medication, such as epinephrine, provided by a nearby patient with the same condition; or in the form of a procedure such as CPR performed by a trained individual irrespective of him/her sharing a medical condition. The parameters that influence potential community response will vary depending on the form of emergency intervention. In the former case, for example, prescription densities and adherence levels will be modelled whereas in the latter case this is replaced by the availability of trained individuals. Our presentation and methods focus on medication provision scenarios but can easily be modified to address procedure-based scenarios.

## 2.1. Measuring effectiveness

As we have already mentioned, the purpose of ERC is not to replace EMS but to augment the EMS response through faster first help by community members. Intervention by a professional is preferred and is expected to be more efficient than intervention by a lay person, but until an ambulance arrives, the help by a bystander is compared to no help and has been found to be effective [27–29]. This is particularly so when the patient himself is trained in administration of the medication and all that is lacking is supply. In the cases that we studied, the AAIs, glycogen kits, and naloxone kits are designed to be used by patients and their family members who often undergo recommended training [30–33]. In an emergency, these medications are provided by another patient or family member who themselves may have had similar training in use of the medication. Other forms of intervention, such AEDs increasingly come with accessible instructions to enable effective use by the untrained.

The actual measure of effectiveness in this research is delivery of the required intervention (e.g. medication or AED) to the scene of the emergency.

## 2.2. The emergency response community effectiveness model

The model enables estimation of the expected density of responders (ERC volunteers) based on demographic data in the specific region, prevalence of the medical condition, prescription adherence rates, assumptions of ERC adoption and mobile online availability. Having determined the expected number of responders, the model provides quantitative tools to compare the expected response times by ERC members to expected response times of EMS or to a medical outcomebased benchmark when EMS is deemed to be not available (i.e. in disaster scenarios).

The first step of the model estimates the expected density of responders (R) for each event, based on several parameters using Eq. (1):

$$
R = a \times b \times c \times d \times e \times f\tag{1}
$$

a – population density in a given geographic area.

b – percentage (of the general population) of diagnosed patients who are prescribed to carry their medication, relevant to the condition being modelled.

c – percentage of diagnosed patients that adhere and actually carry the required medication.

d – percentage of diagnosed patients that will join the community.

e – probability that a community member will be online at the relevant moment.

f – probability that a community member will agree to help when asked.

The number of the community members that are expected to respond within the radius of search (n) is calculated as

$$
\mathbf {n} = \mathbf {R} \times \boldsymbol {\pi} \times \mathbf {r} ^ {2}\tag{2}
$$

The second step of the model uses the Monte Carlo simulation to estimate the probability that the response by ERC will be faster than by EMS for each event. In each iteration of the simulation, the expected response time by ERC volunteers is compared to the expected response time by EMS based on actual historic response. Under circumstances in which there is no EMS service available, comparison can be made to a medical benchmark, similar to the 5-minute cutoff reported by Blackwell and Kaufman [24]. The results of all iterations of a specific event are aggregated to assess the aforementioned probability. The second step of the model uses the following additional parameters:

r – radius of search for volunteers.

n – number of the community members that are expected to respond to each event that was calculated in the first step of the model. ${ \bf d } _ { \mathrm { i } } { \mathrm { i } } = 1 , . . . , { \mathrm { n } }$ – distances of responding community members from the patient in distress. These distances are randomly generated by the Monte Carlo simulation for each iteration. The area of search is a circle with area of πr<sup>2</sup>. In order to predict the probability that a random point in the circle will be found at certain distance from the center, we use the cumulative distribution function presented in Eq. (3):

$$
\mathrm{CDF} = \frac {\pi \mathrm{d} ^ {2}}{\pi \mathrm{r} ^ {2}}\tag{3}
$$

## Fig. 1 depicts this approach graphically:

S – period of time required for the patient to ask for help.

$S _ { 2 } \cdot$ – period of time required for the ERC system to handle the event until the dispatch of the volunteers.

V – average pedestrian speed.

$\mathrm { t _ { i } i } = 1 , . . . , \mathrm { n }$ – estimated arrival times of responding community members to the patient in distress are calculated using Eq. (4):

$$
\mathrm{t} _ {\mathrm{i}} = \frac {\mathrm{d} _ {\mathrm{i}}}{\mathrm{V}} + S _ {1} + S _ {2}\tag{4}
$$

![](/api/attachments/DJ9PNAVD/fulltext/images/75de03250ed7b45a729e7f0a82e64ff1dd67d87b5e2a5b61d48b89a0abd908c1.jpg)  
Fig. 1. Distances of responding community members from the patient in distress

g – the probability that the volunteer will successfully deliver the intervention to the point of need. This factor is to compensate for potentially abandoning the task before completion which can occur for a variety of reasons, even after arrival of the volunteer to the point of need.

Estimated arrival times of volunteers whose intervention is expected to be successful, are compared to the expected response time of the EMS or to a medical benchmark. The probabilities estimated for each event are aggregated and presented for different situations, such as for urban areas vs rural areas.

The detailed simulation algorithm is presented in Appendix A. Here we present a brief description:

1. The simulation gets the dataset and the parameters.

2. Expected number of responders is calculated for each event using Eqs. (1) and (2).

3. For each row (event), the simulation performs multiple iterations. In each iteration, the expected arrival times of the volunteers are compared to the actual arrival time of the EMS or to a medical benchmark.

4. The number of the expected responders calculated in (2) is decimal. However, the number of responders in a specific iteration for a specific event must be integer. We recalculate n for each iteration, using its decimals as the probability that n will be n + 1.

5. If the expected number of responders is zero, the result of the iteration is “no responders found”.

6. If the expected number of responders is greater than zero, then we randomly create the distances for each responder using Eq. (3) and calculate the expected times of arrival (ETA) for each responder using Eq. (4).

7. If the ETA of the nearest responder is longer than the actual arrival time of the EMS or the medical benchmark, then the result is “the nearest responder was slower than the ambulance”.

8. If the nearest responder is faster than the ambulance, then we produce a random number and compare it to the “success” parameter (g). If the random number is smaller or equal to g, than we assume that the intervention by the volunteer was successful, therefore we calculate the time difference between the volunteer's ETA and the actual arrival time of the EMS and use it as the result of the iteration.

9. If the random number calculated in (8) is greater than g and there are no more responders available, than the result of the iteration is “the nearest responder was faster, but didn't help”.

10. If the random number calculated in (8) is greater than g and there are is another responder available, than steps 7–9 are repeated for the next responder until the maximum number of responders is reached or no more responders are available.

11. Steps 4–10 are performed for each iteration.

12. After the required number of iterations for a specific event is reached, the number of iterations in which the volunteers are expected to be faster than the EMS is calculated and used as the prob ability that ERC will be faster for the specific event.

13. Once all events are evaluated, additional aggregative calculations can be performed, such as average probability that ERC will be faster than EMS, expected time savings, distribution of successful interventions among the responders (e.g. the probability that help will be provided by the nearest responder vs the probability that help will be provided by the third responder) etc.

ERCEM was initially developed in VBA to work on excel spreadsheets, and following proof of concept, implemented in MATLAB for improved performance. SPSS was used to prepare the EMS events dataset for analysis. Easyfit<sup>1</sup> was used to determine the appropriate distribution of the results.

## 2.3. The EMS events data

We used the National EMS Information System<sup>2</sup> (NEMSIS) dataset for 2013 with 23,897,213 events which was imported into SPSS and analyzed. The dataset contains 574 data elements about each EMS event such as dates, times, location type, symptoms, medical conditions, medications used, procedures performed, different causes of delays and many more. Some data elements are publicly available while others, such as ZIP code or EMS agency, are restricted due to privacy and data sharing regulations. In this study, we used only the publicly available data.

To illustrate the use of ERCEM we conducted experiments on three different types of emergency event: anaphylaxis, hypoglycemia and opioid overdose (when naloxone was administered) across the United States. For anaphylaxis, relevant events were identified based on a specific condition code; hypoglycemia events were identified through a combination of condition code and EMS impression; and opioid overdose events identified based on medication used (naloxone). Certain events, such as cases that occurred in a health care facility or when ambulance arrival was delayed due to site safety concerns, were filtered out as irrelevant. Events with unreliable data or noisy data such as negative response time were filtered out.

Each dataset served as input to a distinct series of simulation experiments. Emergency provision of epinephrine auto-injectors was studied through a dataset of 14,366 anaphylaxis events; 33,424 hypoglycemia events were used to study emergency provision of glycogen kits; and 19,437 opioid overdose events were studied for the emergency provision of naloxone.

Our model can be used with different sources of EMS event data, such as the European Emergency Data Research Network.<sup>3</sup>

## 2.4. Population density metrics, RUCA and ERS urban influence codes

To determine the population density relevant for each event we used the ZIP Code level when possible and county level when ZIP

Code data was not available or not reliable. The population density data for ZCTAs (ZIP Code Tabulation Areas) and for counties was taken from the US Census AmericanFactFinder.<sup>4</sup> To convert it into ZIP Codes we used the crosswalk table from the UDS Mapper.<sup>5</sup>

Since EMS response times in rural areas tend to be much longer than in urban areas [22], it is important to check if the effectiveness of the ERC compared to the EMS response is different in urban areas versus rural areas. Rural-Urban Commuting Area (RUCA) Codes are a census tract-based classification scheme developed by Health Resources and Service Administration's Office of Rural Health Policy, the Department of Agriculture's Economic Research Service, and the WWAMI Rural Health Research Center. ZIP Code approximation was also developed [34]. United States Department of Agriculture Economic Research Service (ERS) Urban Influence Codes (UIC) are a classification scheme based on county level [35]. Several studies that address the issue of Rural-Urban Classification Systems for Public Health Assessment [36– 38], recommend the use of each coding system in different circumstances. We decided to use both the ZIP code-based RUCA codes and county-based ERS Urban Influence Codes to ensure a thorough analysis.

## 2.5. Prescription data modeling

For medication provision scenarios, such as anaphylaxis, an important input to ERCEM is the estimated per capita prescription density. This parameter determines the ratio of the potential medication carriers in the general population and together with adherence level predicts the number of the relevant medication doses within a given geographic area. It is necessary to externally determine this parameter for each medical condition being evaluated. For procedure-based scenarios such as CPR volunteers, this parameter should be replaced by the ratio of people that carry the relevant equipment, e.g. defibrillators or possess the relevant knowledge and training, e.g. CPR.

To model response to anaphylaxis events we followed Camargo et al. who provide the number of Adrenaline Auto-Injector (AAI) prescriptions per 1000 people for each US state [39].

To model response to hypoglycemia events we used prescriptions data from the 2012 Medical Expenditure Panel Survey by the Agency for Healthcare Research and Quality in the U.S. Department of Health & Human Services.<sup>6</sup>

To model response to opioid overdose events we used naloxone prescription data from a recent FDA report [40].

## 2.6. Scenarios approach

Estimating of the expected number of the responders requires several parameters that are unknown and difficult to predict. Testing multiple scenarios separately for each of these parameters would require a very large number of the simulation runs. Therefore, a scenarios approach was adopted. Following Schnaars [41], three scenarios were prepared - “worst case scenario” (all parameters are set to the most pessimistic values), “most-likely scenario” (all parameters are set to the most realistic values) and the “most optimistic scenario” (all parameters are set to the values expected under the best circumstances).

The scenarios were based on secondary data drawn from the medical literature. To illustrate the approach, we provide details of how parameters were determined for the anaphylaxis example. Similar work was done with hypoglycemia and opioid overdose, but is beyond the scope of this paper. Table 2 summarizes the scenarios and their parameters for each medical condition.

Table 2 Scenario parameters summary.

<table><tr><td rowspan="2">Parameter</td><td colspan="3">Anaphylaxis</td><td colspan="3">Hypoglycemia</td><td colspan="3">Opioid overdose</td></tr><tr><td>Worst</td><td>Likely</td><td>Best</td><td>Worst</td><td>Likely</td><td>Best</td><td>Worst</td><td>Likely</td><td>Best</td></tr><tr><td>c-adhere</td><td>25%</td><td>30%</td><td>60%</td><td>30%</td><td>50%</td><td>70%</td><td>25%</td><td>50%</td><td>75%</td></tr><tr><td>d-join the community</td><td>10%</td><td>20%</td><td>30%</td><td>10%</td><td>20%</td><td>30%</td><td>10%</td><td>20%</td><td>30%</td></tr><tr><td>e-online</td><td>50%</td><td>60%</td><td>80%</td><td>50%</td><td>60%</td><td>80%</td><td>50%</td><td>60%</td><td>80%</td></tr><tr><td>f-agree to help</td><td>30%</td><td>60%</td><td>80%</td><td>30%</td><td>60%</td><td>80%</td><td>99%</td><td>99%</td><td>99%</td></tr><tr><td>g-success</td><td>50%</td><td>60%</td><td>70%</td><td>50%</td><td>60%</td><td>70%</td><td>99%</td><td>99%</td><td>99%</td></tr></table>

The adhere parameter (c) was considered as follows: “worst case” scenario - adherence by 25% of patients, “most-likely scenario” - adherence by 30% of patients and “most optimistic scenario” - adherence by 60% of patients, based on studies by Song, Worm, & Lieberman that have found that under 30% of patients who have been prescribed Adrenaline Auto Injectors (AAIs) carry them at all times [42] and by Goldberg & Confino-Cohen that found that the percent of patients that carried an EpiPen™ at all times varied from 26% to 45% [43].

The join parameter (d) was considered as follows: “worst case” scenario - 10% of patients will join the community, “most likely scenario” - 20% of patients will join the community and the “most optimistic scenario” - 30% of patients will join the community, based on report by PatientsLikeMe that cover about 10% of ALS patients and consider it their “flagship” and The Pew Research Center reports that 72% of patients with chronic conditions use the Internet, 78% own a cellphone, 19% gone online to find others who might have health concerns similar to their own and 9% posted a health-related question online or shared their personal health experience online in any way [44]. According to another report by the Pew Research Center two-thirds of Americans own a smartphone (in rural areas only 52%) [45].

The online parameter (e) was considered as follows: “worst case” scenario – probability of 50% that a community member will be online when he is required to provide help, “most likely scenario” - probability of 60% that a community member will be online when he is required to provide help and “most optimistic scenario” – probability of 80% that a community member will be online when he is required to provide help, based on the Pew Research Center report [45] that about 21% of smartphone users have had to cancel or suspend service due to financial constraints and 35% of smartphone users frequently/ occasionally reach maximum data allowed on smartphone plan and on the IDC research made for Facebook, that found that 63% of smartphone users keep their phone with them for all but an hour of their working day and 79% keep it with them for all but 2 h of their day [46].

The agree to help parameter (f) was considered as follows: “worst case” scenario – probability of 30% that a community member will agree to provide help in a given event, “most likely scenario” – probability of 60% that a community member will agree to provide help in a given event and “most optimistic scenario” – probability of 80% that a community member will agree to provide help in a given event, based on the study by Marshall et al. that studied volunteers response times in public access defibrillation scheme in Northern Ireland and have found that only 45% of AEDs were collected by volunteers and any individual volunteer was only available to respond to around 30% of events [14]. In our model parameter (e) already addresses some of the potential causes of unavailability.

The success parameter (g) was considered as follows: “worst-case” scenario – probability of 50% that a community member will successfully provide help to the patient in distress, “most-likely” scenario – probability of 60% that a community member will successfully provide help to the patient in distress and “most optimistic” scenario – probability of 70% that a community member will successfully provide help to the patient in distress, based on the study by Marrs & Lack that have found that 20% of patients inject themselves [47] taking into account that we have already assumed that only 30% of patients actually carry their prescribed medicine.

The expected number of responders under each scenario was calculated by setting all parameters to the selected scenario values.

## 2.7. Monte Carlo simulation

We calculated the expected responders' density for each event and then we used Monte Carlo simulation to estimate the probability that the response by ERC volunteers will be faster than the response by EMS, and estimate expected time savings. The input parameters of the simulation are:

Global parameters (for the whole dataset):

r – radius of search. Prior to the simulation, we checked the maximum relevant radius of search (expected time of arrival of the community members = actual time of the EMS response) in the data to find that a radius of 1 km covers about 85% of events, 1449 m cover 95% of cases and 2346 m cover 99% of cases. In the current study, we examine arrival by foot only; therefore, this radius parameter is based on reasonable walking distance. We used two radius values in each experiment.

$S _ { 2 }$ – is the system processing overhead reflecting the period of time required for the ERC system to handle the alert until the dispatch of the volunteers. We assumed $S _ { 2 } = 0 . 5$ min. $\mathsf { S } _ { 1 }$ was set to zero because the same time would be required to call EMS.

V – pedestrian walking speed. Based on several studies [48–50], we set V = 1.38 m/s.

g – probability that the volunteer intervention will be effective upon reaching the scene of the emergency event under the evaluated scenario.

The maximum number of volunteers to be dispatched. We limit this number to three volunteers for several reasons (all findings refer to the anaphylaxis dataset):

✓ N3 volunteers are expected in only 8.1% of cases.

✓ The maximum expected probability of the result “Third responder didn't help and there are more volunteers” is 7%. The probability for this result is above 5% in only 125 cases (0.87%).

✓ In 86.324% of cases in which the ERC is expected to be faster than EMS, the nearest responder is expected to successfully provide help, in 11.392% it is the second responder (after the first responder fails) and in 2.283% it is the third responder (after the first two failed).

Parameters specific for each event in the simulation dataset:

n – the number of the expected responders calculated in the first step of the model and recalculated for each iteration as aforementioned.

z – actual response time by EMS (actual data from NEMSIS for each event).

2.8. Simulation robustness check

To ensure robustness and stability of the simulation we performed a robustness check. When we refer to the level of an individual event, we consider the widely used 5% of error as the maximum acceptable error. Under this assumption, about 7000 iterations are needed to get 100% of the simulation results within this range. In order to provide additional level of confidence we used a 10,000 iteration simulation. When we refer to the cumulative level, grouping the events by RUCA or ERS codes, the consistency of the results increases significantly. For the RUCA codes, the maximum error is 0.07%. For ERS codes, the maximum error is just 0.01%.

## 2.9. Calculating effectiveness

For each event, we count the percent of iterations in which the expected ERC response was faster than the EMS actual response time. This percent is the probability that ERC would have been faster for this event. The probabilities estimated for each event were aggregated and presented for different situations, such as for urban areas vs rural areas.

## 3. Results

## 3.1. Experiment results

The simulation results produced by ERCEM were used to generate a series of descriptive statistical reports. The following categories were studied:

1) correlation between EMS response times and the probability that ERC response time will be faster than EMS;

2) correlation between population density and the probability that ERC is faster than EMS;

3) probability that ERC is faster than EMS for each rural-urban classification (urbanicity);

In each of the above the results of multiple scenarios were generated and compared. We present below, a number of the more interesting findings.

## 3.2. ERC-EMS comparison by EMS response time

Fig. 2 presents the average probability that ERC will be faster than EMS for the events of anaphylaxis under the most-likely scenario with 1 km and with 2 km radius of search, for different EMS response times (note that the X axis is not linear), taking into account all relevant events recorded by NEMSIS which results in an averaging of rural and urban data:

This figure demonstrates that the probability that ERC will be faster rises as the EMS response times become longer. We can also observe that for lower EMS response times the effectiveness of ERC is similar for 1 km and 2 km radius of search, however for longer EMS response times, the 2 km radius of search provides higher effectiveness of the ERC.

3.3. ERC-EMS comparison by population density for different medical conditions

Fig. 3a and b present the average expected probability that ERC will be faster than EMS for different population density levels (people/km<sup>2</sup>) under the different scenarios (note the X axis is not linear):

Here we see that there are no significant differences between 1 and 2 km radius of search in any scenario. In areas with low population density, the effectiveness of ERC is low and the differences between the scenarios are small, however in highly populated areas, the effectiveness of ERC rises and the differences between the scenarios become more significant. For example, for population densities under 10 people/km<sup>2</sup> the differences are not visible, however for population densities about 150 people/km<sup>2</sup>, the “most likely” scenario predicts probability of 10% that ERC will be faster than EMS, while the “worst” scenario predicts near-zero probability.

Fig. 3a and b demonstrates how our model provides predictions for different medical conditions. For example, the “most-likely” scenario predicts 5% probability for population densities above 400 people/km<sup>2</sup> for anaphylaxis, and for population densities above 5500 people/km<sup>2</sup> for hypoglycemia. We can also see that in the most populated areas, the probability that ERC will be faster than EMS reaches 90% under the “most-likely” anaphylaxis scenario, compared to only 15% for the hypoglycemia scenario.

## 3.4. ERC-EMS comparison by rural-urban classification (urbanicity)

Table 3a presents the average probability that the ERC response to the events of anaphylaxis will be faster than the ambulance under the different scenarios. The data is grouped by RUCA codes.

![](/api/attachments/DJ9PNAVD/fulltext/images/5e40931b7cce3a7a69809ede24504de14ea5fea968f77bfff0b98ccd2efd7320.jpg)  
Fig. 2. Average probability ERC will be faster than EMS, most-likely Anaphylaxis scenario.

Please cite this article as: M. Khalemsky, D.G. Schwartz, Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Sa..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.07.003

![](/api/attachments/DJ9PNAVD/fulltext/images/20dc09cac85fee8c75de9112310c36ab8dcfd7b002c5d5ce5b2244bd559bc345.jpg)

![](/api/attachments/DJ9PNAVD/fulltext/images/bbdd03b629214c2a2c3fbccee382979258d6001a9ca7226b169418fb81a8bfe2.jpg)  
Fig. 3. a - Average expected probability ERC will be faster than EMS in anaphylaxis events for different population density levels. b - average expected probability ERC will be faster than EMS in hypoglycemia events for different population density levels.

Please cite this article as: M. Khalemsky, D.G. Schwartz, Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Sa..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.07.003

Table 3a  
Average probability ERC will be faster – Anaphylaxis events grouped by RUCA codes

<table><tr><td>RUCA Code</td><td>Worst 1 km</td><td>Worst 2 km</td><td>Most Likely 1 km</td><td>Most Likely 2 km</td><td>Optimistic 1 km</td><td>Optimistic 2 km</td><td>3 points estimate 1 km</td><td>3 points estimate 2 km</td></tr><tr><td>1 - Metropolitan area core</td><td>3.359%</td><td>3.861%</td><td>16.536%</td><td>16.753%</td><td>43.685%</td><td>42.811%</td><td>18.865%</td><td>18.947%</td></tr><tr><td>2 - Metropolitan area high commuting</td><td>0.169%</td><td>0.210%</td><td>1.066%</td><td>1.410%</td><td>6.235%</td><td>7.555%</td><td>1.778%</td><td>2.234%</td></tr><tr><td>3 - Metropolitan area low commuting</td><td>0.110%</td><td>0.170%</td><td>0.608%</td><td>1.128%</td><td>3.802%</td><td>6.579%</td><td>1.057%</td><td>1.877%</td></tr><tr><td>4 - Micropolitan area core</td><td>0.138%</td><td>0.188%</td><td>0.891%</td><td>1.091%</td><td>4.971%</td><td>5.843%</td><td>1.446%</td><td>1.733%</td></tr><tr><td>5 - Micropolitan high commuting</td><td>0.068%</td><td>0.072%</td><td>0.347%</td><td>0.465%</td><td>2.043%</td><td>2.789%</td><td>0.583%</td><td>0.787%</td></tr><tr><td>6 - Micropolitan low commuting</td><td>0.066%</td><td>0.094%</td><td>0.374%</td><td>0.562%</td><td>2.227%</td><td>3.450%</td><td>0.632%</td><td>0.965%</td></tr><tr><td>7 - Small town core</td><td>0.058%</td><td>0.071%</td><td>0.340%</td><td>0.465%</td><td>2.082%</td><td>2.831%</td><td>0.583%</td><td>0.794%</td></tr><tr><td>8 - Small town high commuting</td><td>0.042%</td><td>0.045%</td><td>0.188%</td><td>0.273%</td><td>1.078%</td><td>1.702%</td><td>0.312%</td><td>0.473%</td></tr><tr><td>9 - Small town low commuting</td><td>0.084%</td><td>0.090%</td><td>0.455%</td><td>0.602%</td><td>2.779%</td><td>3.644%</td><td>0.781%</td><td>1.024%</td></tr><tr><td>10 - Rural areas</td><td>0.047%</td><td>0.052%</td><td>0.201%</td><td>0.305%</td><td>1.197%</td><td>1.801%</td><td>0.341%</td><td>0.512%</td></tr><tr><td>For 68 events for which no RUCA code is available</td><td>5.423%</td><td>5.305%</td><td>14.320%</td><td>14.738%</td><td>30.564%</td><td>30.387%</td><td>15.545%</td><td>15.774%</td></tr><tr><td>Total</td><td>2.639%</td><td>3.032%</td><td>12.964%</td><td>13.182%</td><td>34.711%</td><td>34.255%</td><td>14.868%</td><td>15.003%</td></tr></table>

Table 3b shows the average probabilities that the ERC will be faster for different medical conditions under the most likely scenario with 1 km radius of search - grouped by RUCA codes:

Similar analysis was done using ERS Urban Influence codes. Results show no significant differences between the categorizations and indicate that the simulation performs consistently irrespective of the geographic coding method chosen.

## 3.5. Response patterns

For each study undertaken, ERCEM output enables analysis of response patterns. For example, the results of the simulation for anaphylaxis events under the most-likely scenario with 1 km of search are presented in Table 4 and depicted graphically in Figs. 4 and 5. Data is shown for both the complete dataset, and for heavily populated areas (PD N 6460) as elaborated in our discussion below.

The results presented in Fig. 4 provides us with some fascinating insights regarding the potential of Samaritan response given the input parameters, as well as the potential to improve that response by focusing on specific factors. First, it tells us that community response beats out EMS in 12.96% of events, and that this might be increased up to 14.6% by improving training so that more arriving responders will effectively administer their medication. Second, it provides indication that summoning of N3 responders for this medication would be ineffective as we see effectiveness in only 0.20% of cases.

In almost 62% of cases there was no response at all from an ERC Samaritan. This can be attributable to a series of factors: low membership in the region; low levels of connectivity; low levels of adherence; low levels of motivation to respond.

Again, it should be noted that the results presented in Fig. 4 represents the aggregate performance over all geographic areas and density zones. By focusing our analysis on specific population density areas, ERCEM can provide a picture of expected response improvements in a more well-defined environment. To illustrate, Fig. 5 shows expected response improvement when ERCEM is run for population density ≥ 6460 people/km<sup>2</sup> keeping all other parameters constant. Here we see that a volunteer response was elicited in every case and that first and second ERC responders precede EMS in over 55% of events.

## 3.6. Time savings in emergency response

For each study undertaken, ERCEM output enables analysis of time savings. For example, we analyzed the iterations in which the ERC was faster than the EMS for anaphylaxis events (about 12.96%). For the most-likely scenario with 1 km of search, the average saved time was 3.88 min across all geographic codes. In metropolitan areas (RUCA codes 1–3) the average saved time is 3.72 min. In micropolitan areas (RUCA codes 4–6) the average saved time is 4.04 min and in small towns and rural areas (RUCA codes 7–10) the average saved time is 5.55 min. When viewed alongside the success probability patterns, the time saving data show an important deviation. On the one hand, rural areas have a lower probability of success, yet on the other hand the time savings for successful interventions are up to 50% higher than for metropolitan areas. Conversely, in metropolitan areas where response success rates are relatively high, the expected time savings is lower.

## Table 3b

Analysis of the average probabilities that the ERC will be faster.

<table><tr><td>RUCA code</td><td>Anaphylaxis</td><td>Hypoglycemia</td><td>Opioid overdose</td></tr><tr><td>1 - Metropolitan area core</td><td>16.536%</td><td>1.49%</td><td>30.61%</td></tr><tr><td>2 - Metropolitan area high commuting</td><td>1.066%</td><td>0.26%</td><td>5.98%</td></tr><tr><td>3 - Metropolitan area low commuting</td><td>0.608%</td><td>0.11%</td><td>2.28%</td></tr><tr><td>4 - Micropolitan area core</td><td>0.891%</td><td>0.12%</td><td>4.01%</td></tr><tr><td>5 - Micropolitan high commuting</td><td>0.347%</td><td>0.07%</td><td>2.48%</td></tr><tr><td>6 - Micropolitan low commuting</td><td>0.374%</td><td>0.07%</td><td>2.45%</td></tr><tr><td>7 - Small town core</td><td>0.340%</td><td>0.05%</td><td>1.31%</td></tr><tr><td>8 - Small town high commuting</td><td>0.188%</td><td>0.06%</td><td>1.41%</td></tr><tr><td>9 - Small town low commuting</td><td>0.455%</td><td>0.09%</td><td>2.73%</td></tr><tr><td>10 - Rural areas</td><td>0.201%</td><td>0.05%</td><td>1.23%</td></tr><tr><td>No RUCA code is available</td><td>14.320%</td><td>0.14%</td><td>8.23%</td></tr><tr><td>Total</td><td>12.964%</td><td>1.15%</td><td>23.77%</td></tr></table>

Table 4  
Anaphylaxis response patterns.

<table><tr><td>Response</td><td>All regions</td><td>PD &gt; 6460</td></tr><tr><td>No response</td><td>61.90%</td><td>0%</td></tr><tr><td>All slower than EMS</td><td>19.40%</td><td>26.85%</td></tr><tr><td>First precedes EMS</td><td>11.20%</td><td>43.91%</td></tr><tr><td>First precedes EMS but ineffective</td><td>3.40%</td><td>0.04%</td></tr><tr><td>Second precedes EMS</td><td>1.50%</td><td>11.87%</td></tr><tr><td>Second slower than EMS</td><td>1.60%</td><td>9.43%</td></tr><tr><td>Second precedes EMS but ineffective</td><td>0.20%</td><td>0.04%</td></tr><tr><td>Third slower than EMS</td><td>0.30%</td><td>2.79%</td></tr><tr><td>Third precedes EMS</td><td>0.20%</td><td>3.06%</td></tr><tr><td>Third precedes EMS but ineffective</td><td>0.20%</td><td>2.01%</td></tr></table>

Please cite this article as: M. Khalemsky, D.G. Schwartz, Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Sa..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.07.003

![](/api/attachments/DJ9PNAVD/fulltext/images/30073b696ed0fa578b8bda6f0d76197923486a6baa257355678bba81f57aa20b.jpg)  
Fig. 4. Average expected probability that ERC will be faster than EMS for different population density levels – all cases of anaphylaxis.

![](/api/attachments/DJ9PNAVD/fulltext/images/9b75c06c975ffab2339bf545667032bd58800dace1d52d6cea2aec5cb7c649d8.jpg)  
Fig. 5. Average expected probability ERC will be faster than EMS for different population densities – anaphylaxis cases in areas with population density of 6460 people/km<sup>2</sup> and above.

Please cite this article as: M. Khalemsky, D.G. Schwartz, Emergency Response Community Effectiveness: A simulation modeler for comparing Emergency Medical Services with smartphone-based Sa..., Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.07.003

M. Khalemsky, D.G. Schwartz / Decision Support Systems xxx (2017) xxx–xxx

## 4. Discussion

Our study showed how ERCEM can analyze emergency response characteristics and potential improvements, based on actual EMS event data. By considering medical condition (proxied as preferred emergency treatment), prescription adherence levels, community network membership, and regional population density, the simulation generates results that can be used to assess the effectiveness of app-based Samaritan emergency response. We show how the potential community response can be modelled and studied in comparison to EMS. Our approach, grounded in real-world data, can be adopted to study a variety of community-based emergency response scenarios. Based on simulation and scenarios, ERCEM can help decision makers to assess the potential effectiveness of an ERC and to decide if such community should be created in a specific geographic area for a specific medical condition.

## 4.1. Helping decision makers

Without a comprehensive approach that considers different variables that affect the effectiveness of an ERC, it is easy to make wrong decisions. For example, an intuitive hypothesis can be “EMS response times are longer in rural areas, therefore the ERC will be more effective”. ERCEM simulation of multiple factors provides a different, counterintuitive prediction. There is a strong positive correlation (Spearman's correlation = 0.84 under the most likely scenario with 1 km radius of search) between the population density and the expected probability that ERC will be faster than the EMS. Under the most-likely scenario for anaphylaxis, the 5% average probability is reached between 547.62 and 649.27 people/km<sup>2</sup> (about 55% of cases occurred in areas with higher population density). As population density increases, the expected probability that ERC will be faster than the EMS rises. Under the most likely scenario for anaphylaxis with 1 km radius of search, the values of 50% and more are reached at population densities of 6460 people/km<sup>2</sup> (such densities are observed in major cities e.g. New York City, San Francisco).

Two factors are different for urban versus rural areas – population density and the ambulance arrival time, both positively correlated with the probability that ERC will be faster. In metropolitan areas population density is higher and EMS response times tend to be shorter. In our study, we used the EMS response data from the USA which is one of the most developed countries in the world [51]. There are differences in response times between urban and rural areas: the declared U.S. standard is to respond to 90% of calls within 8:59 min in urban areas versus 14:59 min in rural areas [22]. In the NEMSIS data for the 14,366 anaphylaxis events studied we found actual average response times of 9.82 min for urban areas and 14.21 for rural areas. At the same time, the population density varies significantly with averages of 1851 people/km<sup>2</sup> in urban areas versus 16.9 people/km<sup>2</sup> in rural areas. The effect of variations in population density is much more powerful (100×) than that of EMS response times (about 1.5×).

Scenario-based models can help decision makers assess the effectiveness of an ERC under different assumptions. “What-if” analysis can be performed both on a single variable level as shown with the radius of search and on multiple variables levels as shown with three scenarios.

## 4.2. Limitations

Participation by State EMS services in providing data to NEMSIS is voluntary. Therefore, the data may not be representative of the overall US population. The data that was used for this research is from the US only, but many countries have similar databases that can enable similar analysis, such as the European Emergency Data Research Network.

Samaritan help laws and regulations differ from country to country and should be taken into the account by policymakers when consider ing an establishment of an ERC.

We assumed that the responding community members reach the patient in distress by foot. This assumption is reasonable for relatively short distances in urban areas. However, for longer distances and in rural areas, driving and other means of transportation (e.g. bicycle) should be integrated into the model. In this case, differences in traffic conditions, time of day, and day of week should also be considered.

Calculated probabilities treated first response (ERC or EMS) equally irrespective of if one preceded the other by a mere second or by a span of many minutes. However, the model and the algorithm allow setting a threshold below which ERC time savings would be considered insignificant.

We ignored the differences in population density within the search area and assumed a uniform distribution of community members. However, some terrain conditions, like seashores, peninsulas or obstacles such as large areas closed for public, can significantly affect the accuracy of the model. Dealing with this issue requires geospatial analysis like the analysis used by Marshall et al. [14]. We further assumed static population densities despite the fact that population density may vary depending on the hours of the day and days of the week.

Further research is needed to assess the cost-effectiveness of ERC in terms of cost of Quality-adjusted life year (QALY) as was assessed for PAD (public access defibrillation) by Moran et al. [25]. The influence of ERC on EMS resilience or ability to deal with massive disasters should also be studied.

## 5. Conclusions

Developments in mHealth have led to a sharp increase in the availability of applications (apps) supporting medically motivated physical interaction between app users, including smartphone applications to connect users to real-world medical emergency events. Responding to the recognized need to study how mobile technologies affect healthcare in emergency situations [18], we focused on modeling the effectiveness of Emergency Response Communities in terms of faster first-aid provision. Multiple variables were used including those related to individual behaviors such as adherence, willingness to respond, community membership, and online availability, as well as macro level data related to population density, and prescription density within a population.

The Emergency Response Community Effectiveness Modeler (ERCEM) enables decision makers to simulate the effectiveness of smartphone-based emergency response communities and assess their potential performance in comparison to EMS response for delivery of specific interventions. We demonstrated the robustness of the simulation and illustrated the use of ERCEM by presenting an analysis of simulated Samaritan response to tens of thousands of anaphylaxis, hypoglycemia and opioid overdose events drawn from and compared to actual EMS calls and response times. The study of EMS calls related to these medical conditions provided a concrete example of the range of insights that ERCEM can provide decision makers.

## Acknowledgements

The authors thank N. Clay Mann, Principle Investigator of the NEMSIS Technical Assistance Center, University of Utah, for his support and assistance in preparing the dataset for our analysis. The NEMSIS National Dataset is supported by the National Highway Traffic Safety Administration, Office of Emergency Medical Services. We want to acknowledge and thank all the participating EMS providers, EMS agencies and state EMS offices who support and provide data to the NEMSIS National Dataset.

Appendix A. The ERCEM Algorithm

![](/api/attachments/DJ9PNAVD/fulltext/images/04af1976b094f13eb60704abfdfa6b0125e575b7e136ec62b3ba5b4a1a437bd5.jpg)

## References

[1] U. Varshney, Pervasive Healthcare Computing: EMR/EHR, Wireless and Health Monitoring, Springer Science & Business Media, 2009 https://www. google.com/books?hl=en&lr=&id=f5NoQDpVy8oC&oi=fnd&pg= PA1&dq=pervasive+healthcare+computing&ots=3gxy-ISfJL&sig= SL6iZ8WKU24kNs36IDymP1lUP0Y (accessed April 28, 2017).

[2] M. Swan, Emerging patient-driven health care models: an examination of health social networks, consumer personalized medicine and quantified self-tracking, Int. J. Environ. Res. Public Health 6 (2009) 492–525.

[3] U. Varshney, Mobile health: four emerging themes of research, Decis. Support. Syst. 66 (2014) 20–35, http://dx.doi.org/10.1016/j.dss.2014.06.001.

[4] T. Sakai, T. Iwami, T. Kitamura, C. Nishiyama, T. Kawamura, K. Kajino, H. Tanaka, S. Marukawa O. Tasaki T Shiozaki et al. Effectiveness of the new “Mobile AED Map" to find and retrieve an AED: a randomised controlled trial Resuscitation 82 (2011) 69–73

[5] T. Rea, J. Blackwood, S. Damon, R. Phelps, M. Eisenberg, A link between emergency dispatch and public access AFDs: potential implications for early defibrillation, Re suscitation 82 (2011) 995–998.

[6] R.M. Merchant, D.A. Asch, J.C. Hershey, H.M. Griffis, S. Hill, O. Saynisch, A.C. Leung, J.M. Asch, K. Lozada, L.D. Nadkarni, et al., A crowdsourcing innovation challenge to locate and map automated external defibrillators, Circ. Cardiovasc. Qual. Outcomes 6 (2013) 229–236.

[7] F. Folke, F.K. Lippert, S.L. Nielsen, G.H. Gislason, M.L. Hansen, T.K. Schramm, R. Sørensen, E.L. Fosbøl, S.S. Andersen, S. Rasmussen, et al., Location of cardiac arrest in a city center strategic placement of automated external defibrillators in public locations Circulation 120 (2009) 510–517

[8] M.A. Peberdy, L.V. Ottingham, W.J. Groh, J. Hedges, T.E. Terndrup, R.G. Pirrallo, N.C. Mann, R. Sehra, Adverse events associated with lay emergency response programs: the public access defibrillation trial experience. Resuscitation 70 (2006) 59–65. http://dx.doi.org/10.1016/j.resuscitation.2005.10.030.

[9] J. Elsner, P. Meisen, S. Thelen, D. Schilberg, S. Jeschke, EMuRgency–a basic concept for an AI driven volunteer notification system for integrating laypersons into emergency medical services, Int. J. Adv. Life Sci. 5 (2013) 223–236.

[10] J. Elsner, P. Meisen, D. Ewert, D. Schilberg, S. Jeschke, Prescient profiling–AI driven volunteer selection within a volunteer notification system, e℡EMED 2014, The Sixth International Conference on eHealth, Telemedicine, and Social Medicine 2014, pp. 94–98 http://www.thinkmind.org/index.php?view=article&articleid= etelemed\_2014\_5\_20\_40036 (accessed June 24, 2014).

[11] J. Elsner, M.-T. Schneiders, M. Haberstroh, D. Schilberg, S. Jeschke, An introduction to a transnational volunteer notification system providing cardiopulmonary resuscitation for victims suffering a sudden cardiac arrest, e℡EMED 2013, The Fifth International Conference on eHealth, Telemedicine, and Social Medicine 2013, pp. 59–64 http://www.thinkmind.org/index.php?view=article&articleid=etelemed\_2013\_3\_ 10\_40119 (accessed June 24, 2014).

[12] W.J. Groh, A. Birnbaum, A. Barry, A. Anton, N.C. Mann, M.A. Peberdy, K. Vijayaraghavan, J. Powell, V.N. Mosesso Jr., Characteristics of volunteers responding to emergencies in the Public Access Defibrillation Trial, Resuscitation 72 (2007) 193–199, http://dx.doi.org/10.1016/j.resuscitation.2006.06.036.

[13] R. Cappato, A. Curnis, P. Marzollo, G. Mascioli, T. Bordonali, S. Beretti, F. Scalfi, L. Bontempi, A. Carolei, G. Bardy, L.D. Ambroggi, L.D. Cas, Prospective assessment of integrating the existing emergency medical system with automated external defibrillators fully operated by volunteers and laypersons for out-of-hospital cardiac arrest: the Brescia Early Defibrillation Study (BEDS), Eur. Heart J. 27 (2006) 553–561, http://dx.doi.org/10.1093/eurheartj/ehi654.

[14] A.H. Marshall, K.J. Cairns, F. Kee, M.J. Moore, A.J. Hamilton, A. Adgey, A Monte Carlo simulation model to assess volunteer response times in a public access defibrillation scheme in Northern Ireland, Computer-based Medical Systems, 2006. CBMS 2006. 19th IEEE International Symposium on, IEEE 2006, pp. 783–788 http://ieeexplore.ieee.org. proxy1.athensams.net/xpls/abs\_all.jsp?arnumber=1647666 (accessed April 27, 2016).

[15] D. Johnson, DHF Partners With HelpAround in an Effort to Connect People Touched by Diabetes, Diabetes Hands Foundation, 2014 http://diabeteshandsfoundation.org/ dhf-and-helparound-work-together-to-bring-people-touched-by-diabetes-closer/ (accessed October 10, 2014).

[16] D.G. Schwartz, A. Bellou, L. Garcia-Castrillo, A. Muraro, N.G. Papadopoulos, Towards Chronic Emergency Response Communities for Anaphylaxis, 15th IEEE International Conference on Information Reuse and Integration, IEEE, San Francisco, 2014.

[17] D.G. Schwartz, A. Bellou, L. Garcia-Castrillo, A. Muraro, N.G. Papadopoulos, Exploring mHealth participation for emergency response communities, Australas. J. Inf. Syst. 21 (2017) http://dx.doiorg/10.3127/ajisv21i0.1378

[18] U. Varshney, A model for improving quality of decisions in mobile health, Decis. Support. Syst. 62 (2014) 66–77, http://dx.doi.org/10.1016/j.dss.2014.03.005.

[19] K. Peleg, J.S. Pliskin, A geographic information system simulation model of EMS: reducing ambulance response time, Am. J. Emerg. Med. 22 (2004) 164–170.

[20] B. Sund, Developing an analytical tool for evaluating EMS system design changes and their impact on cardiac arrest outcomes: combining geographic information systems with register data on survival rates, Scand. J. Trauma Resusc. Emerg. Med. (2013)http://dx.doi.org/10.1186/1757-7241-21-8.

[21] S. Lee, The role of centrality in ambulance dispatching, Decis. Support. Syst. 54 (2012) 282–291, http://dx.doi.org/10.1016/j.dss.2012.05.036.

[22] S. Chanta, M.E. Mayorga, L.A. McLay, Improving emergency service in rural areas: a bi-objective covering location model for EMS systems, Ann, Oper Res, 221 (2014) 133–159.

[23] Mohd Hafiz Azizan, Cheng Siong Lim, W.A. Lutfi, W.M. Hatta, Ting Loong Go, Soo Siang Teoh, Simulation of emergency medical services delivery performance based on real map. Int. I. Eng, Technol, 5 (3) (2013) 2620–2627.

[24] T.H. Blackwell, J.S. Kaufman, Response time effectiveness: comparison of response time and survival in an urban emergency medical services system, Acad. Emerg. Med. 9 (2002) 288 295.

[25] P.S. Moran, C. Teljeur, S. Masterson, M. O'Neill, P. Harrington, M. Ryan, Cost-effectiveness of a national public access de brillation programme, Resuscitation 91 (2015) 48–55, http://dx.doi.org/10.1016/j.resuscitation.2015.03.017.

[26] G. Nichol, E. Huszti, A. Birnbaum, B. Mahoney, M. Weisfeldt, A. Travers, J. Christenson, K. Kuntz, Cost-effectiveness of lay responder defibrillation for out-ofhospital cardiac arrest, Ann. Emerg. Med. 54 (2009) 226–235.e2, http://dx.doi.org/ 10.1016/j.annemergmed.2009.01.021.

[27] E.J. Gallagher, G. Lombardi, P. Gennis, Effectiveness of bystander cardiopulmonary resuscitation and survival following out-of-hospital cardiac, arrest, JAMA 274 (1995) 1922–1925.

[28] J. Herlitz, L. Svensson, S. Holmberg, K.-A. Ängquist, M. Young, Efficacy of bystander CPR: intervention by lay people and by health care professionals, Resuscitation 66 (2005) 291–295.

[29] T. Iwami, T. Kawamura, A. Hiraide, R.A. Berg, Y. Hayashi, T. Nishiuchi, K. Kajino, N. Yonemoto, H. Yukioka, H. Sugimoto, et al., Effectiveness of bystander-initiated cardiac-only resuscitation for patients with out-of-hospital cardiac arrest, Circulation 116 (2007) 2900–2907.

[30] F.M.G. Antiñolo, How incorrect is the use of adrenaline auto-injectors? Intern. Emerg. Med. 10 (2015) 887–888, http://dx.doi.org/10.1007/s11739-015-1290-9.

[31] G. Harris, A. Diment, M. Sulway, M. Wilkinson, Glucagon administration – underevaluated and undertaught Pract, Diabetes Int. 18 (2001) 22-25.

[32] K.F. Hawk, F.E. Vaca, G. D'Onofrio, Reducing fatal opioid overdose: prevention, treatment and harm reduction strategies, Yale J. Biol. Med. 88 (2015) 235–245.

[33] Nitil Kedia, Treatment of severe diabetic hypoglycemia with glucagon: an underutilized therapeutic approach, Diabetes Metab. Syndr. Obes. Targets Ther. (2011) 337–346, http://dx.doi.org/10.2147/DMSO.S20633.

[34] Rural Health Research Center, Rural-Urban Commuting Area Codes (RUCAs), http:// depts.washington.edu/uwruca/index.php (accessed June 12, 2016).

[35] United States Department of Agriculture Economic Research Service, ERS urban influence codes, http://www.ers.usda.gov/data-products/urban-influence-codes.aspx (accessed December 6, 2016).

[36] L. Gary Hart, Eric H. Larson, Denise M. Lishner, Rural definitions for health policy and research, Am. J. Public Health 95 (2005) 1149–1155, http://dx.doi.org/10.2105 AJPH.2004.042432.

[37] A.F. Coburn, A.C. MacKinney, T.D. McBride, K.J. Mueller, R.T. Slifkin, M.K. Wakefield, Choosing rural definitions: implications for health policy, Rural Policy Research Institute Health Panel, 2, 2007, pp. 1–8.

[38] A. Hailu, J. VanEenwyk, Guidelines for Using Rural-Urban Classification Systems for Public Health Assessment, Department of Health, Olympia, Washington, 2009.

[39] Carlos A. Camargo Jr., Sunday Clark, Michael S. Kaplan, Philip Lieberman, Robert A. Wood, Regional Differences in EpiPen Prescriptions in the United States: The Poten tial Role of Vitamin D, 2007 http://dx.doi.org/10.1016/j.jaci.2007.03.049.

[40] Matthew Rosenberg, Market Structure for Naloxone, FDA, 2015 https://www.fda. gov/downloads/Drugs/NewsEvents/UCM454757.pdf (accessed April 28. 2017)

[41] Steven P. Schnaars, How to develop and use scenarios, Long Range Plan. 20 (1987) 105–114.

[42] T.T. Song, M. Worm, P. Lieberman, Anaphylaxis treatment: current barriers to adrenaline auto-injector use, Allergy 69 (2014) 983–991.

[43] A. Goldberg, R. Confino-Cohen, Insect sting–inflicted systemic reactions: attitudes of patients with insect venom allergy regarding after-sting behavior and proper administration of epinephrine, J. Allergy Clin. Immunol. 106 (2000) 1184–1189.

[44] Pew Research Center, The Diagnosis Difference, 2013.

[45] Pew Research Center, The smartphone difference, http://www.pewinternet.org 2015/04/01/us-smartphone-use-in-2015/ 2015.

[46] IDC, IDC study: mobile and social = connectiveness, http://www.slideshare.net/jeffrufino/ idc-study-mobile-and-social-connectiveness 2013 (accessed September 3, 2015).

[47] T. Marrs, G. Lack, Why do few food-allergic adolescents treat anaphylaxis with adrenaline? – reviewing a pressing issue, Pediatr. Allergy Immunol. 24 (2012) 222–229, http://dx.doi.org/10.1111/pai.12013.

[48] Piotr Olszewski, Sony Wibowo, Using equivalent walking distance to assess pedestrian accessibility to transit stations in Singapore, Transp. Res. Rec. 1927 (2005) 38–45, http://dx.doi.org/10.3141/1927-05.

[49] R. Knoblauch, M. Pietrucha, M. Nitzburg, Field studies of pedestrian walking speed and start-up time, Transp. Res. Rec. (1996) 27–38.

[50] K.K. Finnis, D. Walton, Field observations to determine the influence of population size, location and individual factors on pedestrian walking speeds, Ergonomics 51 (2008) 827–842.

[51]. United Nations Development Programme, Human development index indicators by country 2014, https://data.undp.org/dataset/HDI-Indicators-By-Country-2014/5tucd2a9 2014 (accessed September 6, 2015).

![](/api/attachments/DJ9PNAVD/fulltext/images/b2a34be2e12608a752fcd2d21b481eec196460a27ced66e9c87df400da6fa627.jpg)

Michael Khalemsky – Michael is a PhD student in the Information Systems program of the Graduate School of Business Administration at Bar-Ilan University, Israel. His research fo cuses on the characteristics of Emergency Response Communities, modelling the behavior of crowds in constrained scenarios. Michael has presented his work at the INFORMS Annual Meeting (2016) and the World Allergy Association International Scientific Conference (WISC-2016). He holds a BA in Economics and Business, and MBA both from the Hebrew Uni versity of Jerusalem, and has PMI/PMP certification. He currently lectures at the Jerusalem College of Technology in the subjects of Systems Analysis, Project Management, and ERP. Michael's industry experience includes over 15 years of information technology project management in Government.

![](/api/attachments/DJ9PNAVD/fulltext/images/79bd54b104adacb22c8e1abc2dbc33fc63b2360c3d87016569fd067f1b8f046e.jpg)

David G. Schwartz - David is professor of information systems. and former vice-chairman, at the Graduate School of Business Administration of Bar-Ilan University, Israel, where he also founded and directs the Social Intelligence Lab (, www. socialintelligencelab.org). His research has appeared in publications such as Information Systems Research, IEEE Intelligent Systems, International Journal of Human-Computer Studies, JASIST, and the Journal of Organizational Behavior. His books include Cooperating Heterogeneous Systems: Internet-Based Knowledge Management and Organizational Memory; and the Encyclopedia of Knowledge Management, now in its second edition. David has been a visiting scholar at Columbia University, Department of Biomedical Informatics (2004) and Monash University Faculty of Information Technology (2007–8): and helo a Visiting Erskine Fellowship at Canterbury University, New Zealand for 2016. From 1998 to 2011 he served as editor of the journal Internet Research and is currently an Associate Editor of the European Journal of Information Systems. His main research interests are Cybersecurity mHealth, Knowledge Management, and Computer-mediated Communications.

David has served on the Board of Directors of multiple public companies including Psagot Investment House, Israel's leading investment house with over \$35B assets under management (Acquired by APAX Partners 2010): Cham Foods Ltd. (TASE) a multinational producer of ingredients for the food and nutriceutical industries; C.I. Systems (TASE) a producer of electrooptic systems for the military and semiconductor industries; and Copernic (NASDAQ: CNIC), an Internet search innovator (Acquired by DecisionPoint Systems/DPNI, 2010). Prof. Schwartz received his Ph.D, in Computer Science from Case Western Reserve University USA: MBA from McMaster University, Canada; and B.Sc. from the University of Toronto, Canada
