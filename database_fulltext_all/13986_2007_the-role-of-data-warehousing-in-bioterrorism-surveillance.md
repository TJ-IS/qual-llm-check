---
otero_id: 13986
otero_key: "9DKUUJET"
title: "The role of data warehousing in bioterrorism surveillance"
authors: "Donald J. Berndt; John W. Fisher; Jamie Griffiths Craighead; Alan R. Hevner; Stephen Luther; James Studnicki"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.04.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The role of data warehousing in bioterrorism surveillance

Donald J. Berndt <sup>a</sup>, John W. Fisher <sup>a</sup>, Jamie Griffiths Craighead <sup>a</sup>, Alan R. Hevner a,⁎ Stephen Luther <sup>b</sup>, James Studnicki <sup>b</sup>

<sup>a</sup> Information Systems and Decision Sciences, College of Business Administration, University of South Florida, Tampa, FL 33620, United States <sup>b</sup> College of Public Health, University of South Florida, Tampa, FL 33620, United States

Available online 9 June 2006

## Abstract

The development of an effective bioterrorism surveillance system requires effective solutions to several critical challenges. The system must support multidimensional historical data, provide real-time surveillance of sensor data, have the capability for pattern recognition to quickly identify abnormal situations, and provide an analytic environment that accelerates investigations by epidemiologists and other responders. The use of real-time or flash data warehousing provides the essential ability to compare unfolding health events with historical patterns of key surveillance indicators. To explore the role of data warehousing in surveillance systems, we study naturally occurring incidents, Florida wildfires from 1996 through 2001, as reasonable facsimiles of bioterrorism attacks. Hospital admissions data on respiratory illnesses during that period are analyzed to uncover patterns that might resemble an airborne biochemical attack. A principal contribution of this research is the adroit use of online analytic processing (OLAP) techniques, along with spatial and statistical analyses, to study the adverse effects of this natural phenomenon. These techniques will provide important capabilities for epidemiologist-in-the-loop surveillance systems, enabling the rapid exploration of unusual situations and guidance for follow-up investigations.

Keywords: Bioterrorism; Bioterrorism surveillance system; Data warehousing; Data analytics; Online analytic processing (OLAP); Spatial analytics

## 1. The threat of bioterrorism

The threat of a premeditated biological attack on civilian populations is of real concern to all nations. Recent events, such as the Sarin gas attack in Japan and the anthrax contamination of letters in the U.S. postal service, demonstrate the devastating consequences of bioterrorism both physically and psychologically [1].

Biological weapons can be based on a number of different biological agents with many forms of distribution, making the detection and response to biological attacks very difficult to prepare for [21]. Public anxiety is at an all-time high, and national, state, and local governments are being tasked to protect citizens from these threats to community health—now, not later. Surveillance systems to assist in the detection and prevention of such bio-threats must be rapidly developed. Unfortunately, the data necessary to fuel such systems reside in a multitude of disparate, distributed data sources among hospitals, clinics, pharmacies, water treatment facilities, labs, emergency rooms, etc., and we cannot wait for solutions with long development and implementation times.

How can a community, a county, a state, or a nation determine that it is being attacked by terrorists who are using biological or chemical agents as weapons within a time period short enough to prevent or at least ameliorate major negative health consequences? In the U.S., the Center for Disease Control and Prevention (CDC), in its public health response performance plan, emphasizes the ability of local and state health departments to respond to terrorist attacks. Central to this initiative is the establishment of sentinel networks that not only have the capacity to respond to an act of terrorism, but also to have the infrastructure to anticipate and potentially prevent threats from being realized, or, at least, to minimize their epidemiological impact through early detection [16]. Important components of these networks are an information system and dedicated data warehouse with the primary objectives of detecting and analyzing ongoing biochemical exposures and evaluating the consequences affecting the population health status.

At the University of South Florida, we have an active research program focused on healthcare data warehousing. This paper explores the use of this data warehouse in the context of bioterrorism surveillance, including the investigation of abnormal patterns of diseases related to biological or chemical agents [7]. Fundamentally, there are four major challenges required for such a system to be effective [8]:

1. It must be multidimensional. In other words, it must include a range of appropriate indicators and sources of information in order to monitor as many types of threats and health effects as possible.

2. It must accelerate the transmission of findings and data to closely approximate real time surveillance so as to provide timely attack warnings and responses.

3. It must have the capability for pattern recognition that will quickly identify a specific alarm or alert threshold value, raising the issue for further investigation or possible intervention.

4. It must provide a data analytic environment that will allow epidemiologists to rapidly investigate unfolding events in a historical context, effectively present the information to other decision-makers, and assist in any response.

Based on these objectives, we explore the role of data warehousing in bioterrorism surveillance efforts using an existing Florida healthcare data warehouse. The data warehouse provides the historical context in which to analyze unfolding events and associated realtime data feeds. Using the data warehouse, we investigate analytic methods that support the rapid exploration of complex, multidimensional data relevant to biochemical threats. However, such research is made difficult by the limited availability of data from the few actual terrorism incidents that have involved chemical or biological agents, as well as the difficulty of designing and executing simulated bioterrorism attacks for study.

There are two available strategies for developing realistic bio-attack scenarios. Synthetic data can be injected into available healthcare data to simulate a bioterrorism attack. Alternatively, naturally occurring incidents can serve as reasonable facsimiles of terrorist attacks. This latter strategy is applied in this paper, specifically focusing on wildfires and respiratory conditions.

We have selected six years of wildfires that occurred in Florida from 1996 through 2001 as the focus of our study. Wildfires typically begin as point source events and have reasonably localized effects that are known to be hazardous to people with respiratory problems. We analyze hospital admissions during this time period for respiratory diseases to determine if abnormal or elevated patterns of respiratory illnesses are apparent. The principal contribution of this research is the adroit use of online analytic processing (OLAP) techniques along with spatial and statistical analyses to study the adverse effects of this natural phenomenon. These techniques can accelerate the investigative processes that characterize human-in-the-loop (or more appropriately epidemiologist-in-the-loop) efforts to understand and respond to critical events. Other contributions include the overall data warehouse architecture and the discussion of our preliminary research on real-time data warehousing. Research implications are discussed for our on-going development of more effective bioterrorism surveillance systems.

## 2. The application of data warehousing to bioterrorism surveillance

The effective development and implementation of a bioterrorism surveillance system must address many technical issues related to the four challenges outlined above. A data warehouse infrastructure provides an appropriate foundation for much of this work. Clearly, data warehouses have, in large part, been defined by the goal of integrating diverse collections of multidimensional data. More recently, data warehouse researchers and practitioners have focused on real-time data warehousing based on continuous or “trickle” data loading techniques [2]. Application of appropriate realtime capabilities to public health surveillance systems will support timely identification and reaction to bioterrorism incidents.

Data warehousing is almost always the precursor to long-term data mining efforts. There is a substantial amount of research focusing on the application of statistical and machine learning techniques to the task of pattern recognition for biochemical terrorism [25]. A data warehouse can directly support epidemiologists in the performance of such data analytic tasks. These decision makers must be able to rapidly investigate suspect health data patterns at varying levels of aggregation, drill down to reveal details, and effectively present their findings.

While all of these challenges are important in designing a bioterrorism surveillance system, this paper focuses on our research in a few specific areas. The current healthcare data warehouse, as an ongoing project since 1997, has certainly provided considerable experience in data staging and cleansing a wide variety of multidimensional healthcare indicators [6]. The main focus of this paper is the exploration of OLAP technology and other data analytic techniques for rapid investigations using a naturally occurring phenomenon based on Florida wildfire data.

## 2.1. Multidimensional indicators

The multiple health effects of biological, chemical, or other types of agents or hazards require the specification and monitoring of many different information sources. Among the more obvious information sources are hospital emergency rooms, physician offices, primary care clinics, pharmacies, and clinical laboratories. The data taken from these sources can provide timely information about the nature of the threat, its health consequences, and the areas and populations affected. For example, there have been significant developments in the electronic reporting of laboratory results for notifiable conditions [5,18].

Recognition of the need for more timely surveillance has been demonstrated for diarrheal disease, emergency department-based emerging infections, influenza epidemics, nosocomial infections, salmonella, meningitis, tuberculosis, and various clinical event monitors [15]. There has been increasing attention paid to rapid laboratory testing, handheld and field-deployable devices, as well as clinical decision support systems [9]. In addition, there has been growing interest in systems that support syndromic surveillance (www. syndromic.org), and even an open source initiative to foster widespread adoption [25].

Among the many types of information sources that have received much less attention as part of an early detection system are physical monitors which are capable of detecting hazards affecting the water supply, the air supply, or the food supply. Each of these groups of indicators, or domains, would be specified as part of an integrated, comprehensive early warning system.

## 2.2. Real-time information

Timely detection is a key requirement to avoid the most serious negative consequences of any future terrorist attack involving biological or chemical agents. Timeliness, as measured by the time interval separating the event from its detection, is always a critical factor for an early warning system, but has been infrequently studied in the context of more rigorous evaluations [9]. An assessment of timeliness requirements for inhalation anthrax, with scenarios ranging from treatment starting on the first of 6 days to no treatment at all, suggests detection after 3 days is nearly useless and the cost accumulation during the steepest part of the curve (between day 2 and 3) is \$200 million per hour [11]! A CDC study of tularemia suggests that starting treatment on the day after the attack reduces the mortality rate by two-thirds, but treatment has no effect if started as late as the fifth day.

Current systems for reporting and notification often involve the reporting of data from the local level, to the state level, and on to the federal level. This highly centralized process batches the data at several levels and ‘timely’ reporting can actually take from a few weeks to more than a year to traverse these organizational boundaries. Serving as an additional barrier to the development of comprehensive surveillance systems is the fact that necessary data elements reside in a multitude of disparate, distributed data sources, complicating a timely implementation cycle. Many of the indicators that could be used in the system are not even identified, nor collected, and the logistical problems of capturing this information can be considerable for source organizations. Finally, the data discovery and categorization methods necessary for securing access to disparate, distributed data sources in real time requires unique and powerful technologies for identification, collection, integration, quality control, querying, reporting, and dissemination.

## 2.3. Pattern recognition and alarm thresholds

While the transmission of data elements in real time is a necessary capability of an effective bioterrorism system, it is in itself insufficient without the means to determine when the signal received actually represents the existence of an adverse event. These alarm values, or alert thresholds, must be determined on the basis of historical pattern recognition that will enable researchers to determine both the existence and nature of the damaging event. Hospital admissions initiated in the emergency room, for example, vary from hospital to hospital, seasonally, and by diagnostic composition. These existing patterns must be analyzed before an alert threshold can be determined.

![](/api/attachments/9DKUUJET/fulltext/images/c499fc4856570d10c5a4577c7122da633d0adbba7957066fa4af67b2f6e6d922.jpg)  
Fig. 1. High rate of hospitalizations from emergency room admissions at hospital 1.

For example, Fig. 1 shows a high number of hospitalizations resulting from emergency room admissions for a hospital near many of the Florida theme parks and tourist destinations. Using quarterly aggregations, the data show that the ER admission rate holds steady around 70%. However, Fig. 2 depicts the much lower percentages that characterize a large, urban hospital. For this hospital, the quarterly data show a steady ER admission rate of approximately 20%. This demonstrates the importance of having historical baseline data at fine-grained levels, such as individual hospitals, for comparison before sounding a bioterrorism alert, as well as, the wide variation in even the simplest indicators.

Various marker admissions can also be historically monitored such as infectious and parasitic diseases, diseases of the respiratory system (e.g., those due to external agents such as chemical fumes or vapors), nonspecific abnormal findings, poisonings by antibiotics, or the toxic effects of substances such as carbon monoxide or chlorine. Even the nature of the alarm threshold itself may vary. The actual level of the indicator value at a single hospital may serve as the alert; for example, any hospital that exceeds its own expected number of respiratory disease admissions by one standard deviation or more in any two-hour period. Similarly, an alarm threshold might be reached when a smaller increase in specified admissions is achieved (e.g., 20%) but at some number (e.g., 3 or more) of hospitals in the same area. These patterns and the determination of valid alert levels can only be accurately generated with the creation of a healthcare data warehouse that integrates the many disparate data elements. This warehouse can then support the use of sophisticated browsing tools for either explanatory or confirmatory purposes.

![](/api/attachments/9DKUUJET/fulltext/images/fb33eedfd2d5a6272d259084e1e3c06a13def179f9d77be04a2198d4f64ae58a.jpg)  
Fig. 2. Lower rate of hospitalizations from emergency room admissions at hospital 2.

## 2.4. A data analytic environment

A final challenge is to provide a data analytic environment that will allow an epidemiologist to rapidly investigate unfolding events and any alerts generated by more automated pattern recognition techniques. While the focus of this paper is primarily online analytic processing (OLAP) technologies that are commonly associated with data warehouses, other technologies from data visualization and geographic information systems (GIS) to traditional statistical tools can add capabilities to the analytic environment. In fact, new interface technologies being used with our healthcare data warehouse integrate OLAP capabilities with selected visualization techniques and geographical presentations. OLAP technologies allow users to navigate between levels of aggregation, considering patterns at somewhat higher levels of abstraction, yet still providing the capability to drill into underlying details. It is the ability to quickly move to appropriate levels of detail, while drawing upon an integrated collection of data elements, that provides a rich query environment.

## 3. The decision making context

The decision whether an unfolding epidemiological situation is in fact an act of bioterrorism is clearly a very daunting task, full of uncertainty. There has been much research regarding decision-making under ambiguous and confusing circumstances. For instance, signal detection theory has been widely applied in practice and research. Signal detection theory assumes that most decision-making tasks occur under conditions of uncertainty. The basic framework proposes four outcomes for such tasks: a “hit” corresponds to a correctly identified event (such as a bioterrorism attack) from the signals or available information, a “miss” is when a decision maker fails to identify such an event, a “false alarm” when an event is incorrectly identified, and finally a “correct rejection” when no event has occurred. This reasoning echoes the concepts of Type I and Type II errors in statistics, where the convention is to structure the hypotheses to minimize the risk of costly Type I errors, while using sample size and other design factors to control Type II errors.

The related concepts of sensitivity, specificity, and timeliness also describe important characteristics of the decision-making model, especially in the context of bioterrorism and disease surveillance [26]. Sensitivity relates to the level required to trigger an alarm or threshold, while specificity characterizes the accuracy or ability to correctly discriminate between outcomes. In medical testing terms, sensitivity is the probability that a screening test is positive given that a person has the disease (i.e., true positive). Specificity then is the probability that a screening test is negative given that a person does not have the disease (i.e., true negative). Associated with these measures, but reversing the logic, are positive predictive value and negative predictive value that focus on the probability a person does (PPV) or does not (NPV) have the disease given a positive or negative test. Typically, these parameters form the basis for a tradeoff, where increased sensitivity comes at the cost of reduced specificity. Bravata et al. [9] review many health surveillance systems (focusing on laboratory testing, field testing, and clinical decision support systems) and find relatively few rigorous evaluations using such metrics.

Timeliness is another critical issue that can often be improved by increasing sensitivity, again at the cost of other criteria. Timeliness is especially critical in the domain of disease outbreaks and bioterrorism early warning systems. Excessive delays can render effective interventions useless and dramatically reduce alternative courses of action [11]. Since many disease or biochemical agents have unique temporal trajectories, research into the profiles of these threats is a high priority.

Many investigators have theorized and experimented in the area of decision making under uncertain and risky conditions. Shapira offers a model of risk in managerial decision-making that further refines the relationship between possible outcomes [23]. This model has been recast for the study of “strategic surprises” [13]. While the model is more often used to characterize strategic surprises between business partners, several wartime events are used to illustrate the model, making the model very relevant for biochemical attacks. In particular, both the attack on Pearl Harbor and the Yom Kippur War provide examples where costly false alarms resulted in the upward adjustment of alarm thresholds and the resulting “surprise” attacks, despite very good intelligence. The authors suggest that it is tempting to cite an “information gap” due to less than ideal intelligence gathering activities. However, there is always incomplete information and uncertainty in such circumstances. Perfect information is usually too expensive and often simply unattainable.

These decision-making frameworks serve to highlight some important aspects of the biochemical threat detection challenge. The cost of false alarms in early warning systems for biochemical threats is extreme in terms of monetary expenditures and psychological burdens. Therefore, subsequent upward adjustments of alarm thresholds would be expected, reducing the sensitivity, timeliness, and ultimate usefulness of the system. In addition, biochemical attacks are (thankfully) exceedingly rare, providing few examples on which to refine and calibrate predictive models. Lastly, it may never be possible to definitively answer some questions regarding the origins of a particular attack, or even whether it was an intentional act or natural outbreak. In the face of such challenges, it is unlikely that a highly automated early warning system can be constructed, at least in the short term. A more appropriate goal would be to provide thorough, easily accessible, and sophisticated analytic capabilities for accelerating further investigations once early indications of a threat are identified. These types of human-in-the-loop, or more appropriately, epidemiologist-in-the-loop systems can be supported in part by available data warehousing, data mining, and information visualization technologies. The hope would be to accelerate and enhance the epidemiological investigative processes to improve timeliness, while still controlling the specificity and associated risks of false alarms.

The bioterrorism system architecture presented in the next section is designed with this decision context in mind. Our goal is to develop a system to provide rapid, verifiable information to support the ultimate human decision-maker who is responsible for balancing the trade-offs of sensitivity, timeliness, and the welfare of the affected population.

## 4. The CATCH data warehouse

Data warehousing technologies are a natural fit for many surveillance system requirements. In particular, the requirement for archiving both historical and realtime data is best accomplished using a data warehouse. In addition, any pattern recognition or data mining approach to threat detection will require a data warehouse infrastructure. Our interdisciplinary team has amassed considerable experience in using data warehousing and data mining technologies for community health status assessment [6,7]. This experience has centered on supporting the Comprehensive Assessment for Tracking Community Health (CATCH) methodology with advanced data warehousing components and procedures.

The current CATCH data warehouse supports population-based health status assessments throughout Florida. The data warehouse serves as a historical repository of fined-grained data, such as individual births, deaths, and hospital admissions, which are used to form aggregate indicators of health status. We also use a number of effective techniques to provide adequate levels of quality assurance [6]. Reconstructing and analyzing historical patterns are tasks well suited to data warehousing technologies. However, new tasks such as surveillance systems for bioterrorism require more timely data and real-time data warehousing approaches. With these requirements in mind, we propose the bioterrorism surveillance system architecture found in Fig. 3.

## 4.1. Real-time (flash) data warehousing

Clearly the major challenge in bioterrorism surveillance lies in coupling historical perspectives with realtime data warehousing approaches [12]. The existing CATCH data warehouse provides the historical information against which any new data can be compared. The new components in our prototype bioterrorism surveillance system are the real-time data feeds and associated flash data warehouse components. These innovative data warehouse components are used to store partially available real-time data. The components act as persistent memory for incomplete real-time data that are preprocessed for comparative queries against the archival data warehouse components, and possibly overwritten as new data become available. The flash components share common metadata with the archival data warehouse, making the important data items useful for cross queries. It is these common data items that serve as input to decision support systems and pattern recognition algorithms that will support the identification of potentially abnormal events.

The success of any bioterrorism surveillance system also requires real-time data collection from a wide variety of sources. While this is a difficult task, it can be approached in an incremental fashion. In addition, the Internet and rapidly developing wireless networking infrastructures provide expanding opportunities to use off-the-shelf technologies for real-time data entry. Data from many organizations can contribute to an effective surveillance system. Most database systems now incorporate many features for constructing distributed systems, thereby linking physically remote data sources.

![](/api/attachments/9DKUUJET/fulltext/images/edca79c265a4053f8ed5f9c35c4e3c058f5e04f456596bb8af3af8b36a6821a9.jpg)  
Fig. 3. A data warehouse architecture for bioterrorism surveillance.

Many of the interoperability concerns have been reduced since most organizations now rely on one of the few dominant relational database engines. There are also developing data model standards such as the Public Health Conceptual Data Model, developed as part of the NEDSS project [17]. The NEDSS Base System is being used to collect ‘notifiable’ conditions in several states. These types of systems are akin to operational systems in a business context, providing the infrastructure for capturing day-to-day transactions, and are the source systems for healthcare data warehouses.

In order to support real-time data collection, our architecture is compatible with several existing projects in Florida. The Florida Department of Health has a number of important real-time data collection systems in place. These are multi-stakeholder efforts involving the standardization and reporting of laboratory tests, based on medical industry standards (e.g., NEDSS, HL7, LOINC, and SNOMED) [17]. Two existing state systems are Merlin and EpiCom. Merlin is a webbased system for mandatory communicable disease reporting. The EpiCom system provides information exchange as well as communication between key public health decision-makers.

## 4.2. Hospital discharges and emergency room visits

The hospital discharge data contained in the CATCH data warehouse are used to support the OLAP analyses performed in this study. Florida hospital discharge transactions are collected by the Agency for Health Care Administration (AHCA) from the more than 200 shortterm acute care hospitals in the state. These hospitals report every discharge transaction, regardless of payer, throughout the state. Of course, we recognize that hospital discharge data may be of limited utility in the context of bioterrorism surveillance since it requires an admission and at least an overnight (24 h) stay in the hospital. Emergency room data or even physician office data would be a more appropriate dataset for this realtime surveillance challenge. Uncommon patterns in healthcare utilization are much more likely, especially in the early stages of an event, to surface in the emergency room rather than more routine hospital admissions. Currently, efforts are underway to collect emergency room data through the same statewide reporting mechanisms used for hospital discharges. The expected volume of this data is some two to three times the number of hospital discharges and will provide a complementary perspective on many issues related to bioterrorism surveillance.

To support this point, Table 1 summarizes an interesting analysis by the Volusia County Health Department in conjunction with the Florida Department of Health [24]. The authors note “several large wildfires occurred in Florida during June–July 1998, many involving both rural and urban areas in Brevard, Flagler, Orange, Putnam, Seminole, and Volusia counties.” Public health alerts advising people with “pre-existing pulmonary or cardiovascular conditions to avoid outdoor air in the vicinity of the fires” were issued, along with a subsequent analysis of the health impacts. The frequency of emergency room department visits and hospital visits for selected conditions during two 6-day periods, June 1–July 6, 1997 and June 1–July 6, 1998, were compared. As can be seen in Table 1, emergency department visits increased for asthma (91%), bronchitis with acute exacerbation (132%), chest pain (37%), conjunctivitis (32%), and shortness of breath/wheezing (32%). Hospital admissions also increased for asthma (46%) and chest pain (24%), though less dramatically.

Emergency room and hospital admissions, Volusia and Flagler Counties (from [24])

<table><tr><td rowspan="2">Diagnosis (ICD-9-CM codesa)</td><td colspan="3">Emergency department visits</td><td colspan="3">Hospital admissions</td></tr><tr><td>1997</td><td>1998</td><td>% change</td><td>1997</td><td>1998</td><td>% change</td></tr><tr><td>Asthma (493–493.91)</td><td>77</td><td>147</td><td>91</td><td>13</td><td>19</td><td>46</td></tr><tr><td>Acute bronchitis (466.0-466.19)</td><td>134</td><td>107</td><td>-20</td><td>5</td><td>4</td><td>-20</td></tr><tr><td>Bronchitis with acute exacerbation (491.21)</td><td>28</td><td>65</td><td>132</td><td>56</td><td>56</td><td>-</td></tr><tr><td>Carbon monoxide poisoning (986)</td><td>2</td><td>2</td><td>-</td><td>9</td><td>0</td><td>-100</td></tr><tr><td>Chest pain (786.50–766.59)</td><td>218</td><td>299</td><td>37</td><td>63</td><td>78</td><td>24</td></tr><tr><td>Conjunctivitis (372.30–372.39)</td><td>59</td><td>79</td><td>34</td><td>0</td><td>0</td><td>-100</td></tr><tr><td>Emphysema (492.0–492.8)</td><td>0</td><td>1</td><td>-</td><td>2</td><td>0</td><td>-100</td></tr><tr><td>Chronic obstructive pulmonary disease (496)</td><td>17</td><td>17</td><td>-</td><td>11</td><td>11</td><td>-</td></tr><tr><td>Heat exhaustion (992.3-992.5)</td><td>7</td><td>19</td><td>171</td><td>2</td><td>1</td><td>-50</td></tr><tr><td>Painful respiration (786.52)</td><td>74</td><td>54</td><td>-27</td><td>7</td><td>3</td><td>-57</td></tr><tr><td>Palpitations (785.1)</td><td>19</td><td>15</td><td>-21</td><td>0</td><td>1</td><td>-</td></tr><tr><td>Shortness of breath/wheezing (786.09)</td><td>68</td><td>90</td><td>32</td><td>1</td><td>1</td><td>-</td></tr><tr><td>Sinusitis (461.8–461.9)</td><td>46</td><td>55</td><td>20</td><td>0</td><td>0</td><td>-</td></tr><tr><td>Total</td><td>749</td><td>950</td><td>27</td><td>169</td><td>174</td><td>3</td></tr></table>

Frequency of emergency department visits and hospital admissions for selected conditions and percentage change — Volusia and Flagler counties<sup>b</sup>, Florida, June 1–July 6, 1997 and June 1–July 6, 1998.  
<sup>a</sup> Internal classification of diseases, Ninth Revision, Clinical Modification.  
b Seven hospitals in Volusia Country and one in Flagler Country.

![](/api/attachments/9DKUUJET/fulltext/images/ea980a320c7dcf3d9ebeee3d7e1c0a4daee0dc98e268b739ff9b6e71b1d0a6fd.jpg)  
Fig. 4. Aggregate data cube for bioterrorism surveillance.

These data demonstrate the potential of naturally occurring events as surrogates for biochemical attacks and the importance of collecting emergency room data. But the data also show that the effects may be detected in hospitalizations as well.

## 4.3. Aggregate data cubes for surveillance

In order to facilitate OLAP studies, an aggregate data cube is formed from the underlying hospital discharge data. This aggregate structure provides much improved performance for the roll-ups and drill-downs that characterize OLAP-style navigation. Of course, the true event-level data is still available for unanticipated queries, but many operations can be run against such pre-computed aggregates. Fig. 4 depicts one such aggregate with hospital admissions organized by several dimensions, including specific hospitals, ICD (International Classification of Disease) diagnostic codes, dates, and patient age categories. As part of this study, admissions with diagnoses from threats specifically related to respiratory and infectious illnesses were aggregated for OLAP analysis [22]. (Table 2 contains the ICD codes used for the study.) Support for OLAP analysis would provide the epidemiologist with powerful techniques to rapidly investigate current events in a historical context. These same data warehouse design and analysis techniques can also be applied to the emergency room data when it is available in the future.

Table 2  
Diseases (ICD codes) used in this study

<table><tr><td>Threat indicators</td><td>ICD codes</td><td>Comments</td></tr><tr><td colspan="3">Diseases of the respiratory system (ICD 460–519)</td></tr><tr><td>Acute respiratory infections</td><td>460–466</td><td></td></tr><tr><td>Pneumonia and influenza</td><td>480–487</td><td></td></tr><tr><td>Pneumoconiosis and other lung diseases due to external agents</td><td>500–508</td><td>Respiratory conditions due to chemical fumes and vapors (506)</td></tr><tr><td>Asthma</td><td>493</td><td></td></tr><tr><td colspan="3">Infectious and parasitic diseases (ICD 001–139)</td></tr><tr><td>Intestinal infectious diseases</td><td>001–009</td><td>Cholera, typhoid, Salmonella, Shigellosis, E. Coli</td></tr><tr><td>Zoonotic bacterial diseases</td><td>020–027</td><td>Plague, Anthrax</td></tr><tr><td>Viral diseases accompanied by exanthim</td><td>050–057</td><td>Smallpox, measles, rubella</td></tr><tr><td>Other diseases due to viruses and chlamydiae</td><td>070–079</td><td>Viral hepatitis, infectious mononucleosis</td></tr></table>

## 5. Florida wildfires

Several years of data on naturally occurring wildfires that resemble point source bio-attacks are used to provide a realistic study environment in which to investigate OLAP and other data navigation and presentation techniques. Data on more than 100,000 wildfires spanning more than two decades have been loaded into the CATCH data warehouse. Florida wildfires show considerable variation from year to year as depicted in Fig. 5. For instance, several years of drought conditions led to a record number of wildfires throughout Florida during the first six months of 2001. The majority of these fires were caused by lightening strikes on parched grass and wood. Over 3600 individual fires consumed nearly 320,000 acres of woodlands. Major transportation corridors, such as I-95 in the east, I-75 in the west, and I-4 across the state, were intermittently closed due to the lack of visibility from smoke and haze.

Total Acres Burned by Wildfires in Florida 1981-2000  
![](/api/attachments/9DKUUJET/fulltext/images/5071ecdd2ef085749034e14e7ace5d587126a83a91e2ae2c9a3e2d499a5fbb53.jpg)  
Fig. 5. Yearly acres burned by wildfires in Florida (1981–2000).

Another year of concentrated wildfires was 1998, when a string of fires burned along the Atlantic coastline. Again, the wildfires resulted in major highway closings and the widespread destruction of property. For instance, a 48-mile section of I-95, connecting Jacksonville to Cocoa Beach, was closed as a result of smoke and events such as the NASCAR Pepsi 400 in Daytona Beach were rescheduled. Fig. 6 provides a geographic visualization of the individual fires in 1998 and 1999 along with size information in number of acres burned. In 1999, we find that roughly half the acreage was burned and wildfires were spread more evenly across the state than in years 1998 and 2001.

Relevant to our study, the wildfires combined with the regular mix of air pollutants found in the air of urban areas, create a dangerous condition for individuals with respiratory illnesses. In the Tampa Bay area alone, the American Lung Association estimated the presence of approximately 350,000 respiratory patients who could have been affected by wildfires during the spring and summer of 2001. Over the Memorial Day weekend of 2001, the Florida Department of Environmental Protection issued air pollution alerts for all of the counties in the I-4 corridor from Tampa Bay in the west to Daytona Beach in the east, including the Orlando area. Persons with respiratory problems were advised to stay inside during the long holiday weekend [19].

These health emergencies due to natural causes hold great similarities to a potential biological or chemical attack via airborne agents. In a similar fashion, other researchers have used wildfires to learn valuable lessons on emergency response. For instance, the study of recent California wildfires highlighted both successes and problems, such as incompatible communication systems and business continuity challenges [4]. However, in this research we are using the wildfires as a context for understanding potential threats to human health. We explore the data on hospital admissions due to respiratory illness during the time period encompassing these fires. As a preliminary investigation, we use a healthcare data warehouse and associated query tools to ‘slice and dice’ data to investigate patterns of elevated respiratory illnesses that might have resulted from hazardous agents in the environment. A retrospective study such as this, where we know the cause of the illnesses, can inform the development of bioterrorism surveillance systems as we monitor real-time data for abnormal illness patterns and investigate any alerts or notifications that arise from automated detection systems.

a  
1998Florida Wildfires Greater Than 250 Acres  
![](/api/attachments/9DKUUJET/fulltext/images/083558ec3eba0af212b555c5f0a95e3350ab1ffe6c8f5383f11d85e8ce32e703.jpg)

![](/api/attachments/9DKUUJET/fulltext/images/92a08b3abed707630c832871a8ce57e05db99a09cefd82b2c8dd8211743f474d.jpg)  
Fig. 6. Comparing 1998 and 1999 Florida wildfires.

## 6. Online analytic processing (OLAP) on Florida wildfire data

In citing his experiences as the chief health officer for the District of Columbia, Dr. Walks notes that “the key to a successful response is the ability to communicate and share information quickly and fluidly with the appropriate people at the right time in order to make the critical decisions the situation demands” [27]. We consider data warehousing and OLAP technologies to be important methods for quickly analyzing and sharing information in support of critical decision-making activities. Surveillance personnel, such as epidemiologists and other healthcare professionals, can use integrated data warehousing technologies to rapidly analyze situations in ways that are currently very time consuming or simply not possible. Due to the sensitive nature of the data and potential costs of false alarms, fully automated pattern detection and alert mechanisms are unlikely to be implemented. Rather, systems that enable and accelerate analysis, feeding alerts to trained surveillance experts seem more feasible and likely to be implemented.

This section presents our exploratory application of online analytic processing (OLAP) to the hospital discharge data and Florida wildfire data from the years 1998 and 2001.

## 6.1. Applying OLAP to 1998 wildfire events

We begin by using OLAP techniques on the wildfire data from the year 1998. As noted above, a particularly concentrated group of wildfires burned near the city of Daytona, causing highway closures and significant property damage. Fig. 7 combines an actual satellite view of the burning wildfires with an illustration of the location and size of the wildfires. The smoke plumes are clearly visible, resembling a point attack, with the particulate matter a potential threat to health.

Fig. 8 is the result of an OLAP query, presenting detailed information for individual fires, including attributes such as the fuel type, size in acres, and cause. This information is presented at the ZIP code level, with roughly 25,000 fires reported. Fig. 9 aggregates the fire data at the ZIP code level, presenting the volume of hospitalizations due to the three respiratory diseases (see Table 2) by quarters of a year. No clear pattern emerges, except a slight elevation in respiratory illnesses during the first and fourth quarters (the winter), when there are more people in Florida.

In order to explore patterns at different levels of aggregation, dimension hierarchies are integrated with the wildfire data. Fig. 10 presents a roll-up on fire size using three rough categories: fire size > 10,000 acres, 1000 to 10,000 acres, and <1000 acres. Again, volumes and rates for the three respiratory diseases are

b  
![](/api/attachments/9DKUUJET/fulltext/images/612c0382489134b1cdac333a9d477875c5b680be6dea170fecb02880920b6645.jpg)

![](/api/attachments/9DKUUJET/fulltext/images/64f12d9c7e149e7b60c7fcd552efa96c4f28570a27e42cc8138e283cce737f18.jpg)  
Fig. 7. NOAA satellite image, 2 July 1998 (a), and corresponding wildfire map (b).

considered. While there are no clear patterns, it is interesting to note that the largest fires are associated with the lowest hospital discharge rates (per 100,000 people) across the board. This seems somewhat counterintuitive, but may be due to the rural nature and low population concentration of the areas in which the largest fires are likely to occur, later analyses correct for such factors.

![](/api/attachments/9DKUUJET/fulltext/images/f0bc956ebc361ee4c617fdf2a1414f346d8b36cb7260961a309b6eab3077d993.jpg)  
For Help, press F1

Fig. 8. Details on 1998 Florida wildfire data.  
![](/api/attachments/9DKUUJET/fulltext/images/15174dac4437efd75c3338496a1933c264e78581c47c8be4e194fb6a79b36d3b.jpg)  
For Help, press F1

Fig. 9. 1998 Respiratory illness volume and wildfire acreage burned by quarter.

![](/api/attachments/9DKUUJET/fulltext/images/a08991a418220619e7600d1e9c6d7248938fa99a5a0f50efee1ba11e263f9c46.jpg)  
Fig. 10. A roll-up on fire size.

## 6.2. OLAP drill down on 2001 Florida healthcare data

Public reports of the 2001 Florida wildfires provide the time and location of the fires for a more extensive OLAP analysis. During 2001 Governor Jeb Bush proclaimed a State of Emergency in accordance with Federal Emergency Management Agency (FEMA) guidelines for a collection of distinct areas from the middle of February through June of 2001. As illustrated in the Division of Forestry map (Fig. 11), some of these wildfires were near heavily populated areas and threatened major highways. Therefore, we select a specific set of wildfires that offers the opportunity to study realistic bio-threat scenarios. In particular, a State of Emergency was declared for Brevard, Orange, Osceola, and Seminole counties (within the Division of Forestry, Orlando Fire District) from April 16th through June 26th of 2001. These wildfires will serve as the subject for several OLAP queries that allow us to ‘drill down’ into the data to explore illness patterns related to air pollution caused by the wildfires.

![](/api/attachments/9DKUUJET/fulltext/images/93684508c41789d232e74c83853fd200eac4517f35dc2e69c67cf0ff62a55d5f.jpg)  
Fig. 11. 2001 Florida wildfires.

![](/api/attachments/9DKUUJET/fulltext/images/aad51606502a46ee7a350efe4cbbe7467866db81a5ef875731c0bfca192ca82c.jpg)  
Fig. 12. Diseases by quarter for 2000 and 2001.

Fig. 12 takes a regional perspective, showing the admissions associated with the potential threats (based on ICD codes) described in Table 2. This view rolls up several counties to form central Florida summaries. A few patterns do emerge from this coarse-grained overview. First, you can clearly see the seasonality in categories such as acute respiratory infections with the first and fourth quarters (the fall/winter) showing much higher numbers of cases. Secondly, the second quarter of 2001 has a somewhat higher rate of lung diseases due to external agents, as well as pneumonia and influenza. While this could simply be due to a nasty ‘flu’ season, further investigation is needed and we will continue to drill-down to finer levels of granularity as part of our example. In fact, drilling across to other regions reveals a similar pattern of slightly higher volumes of respiratory illnesses, making it less likely that wildfires were the only cause of the increased illness. Rather, natural variations for these years in weather, as well as general air quality could also be relevant factors.

The State of Emergency was declared for the Orlando Fire District, which includes Orange County. Fig. 13 drills down to the county level, again contrasting year 2000 with 2001, but by month. The latter year (2001) is compared with a three-year moving average in order to smooth out year-to-year variations. Additional values, such as expected values from regression equations or other predictive models are incorporated into the data warehouse surveillance components for further analysis. At the county level, the pattern of somewhat higher rates remains for pneumonia and influenza, as well as acute infections for April through June.

![](/api/attachments/9DKUUJET/fulltext/images/e1eb3c0d2ce2e821f7480cb2158e8a41c13dc0d7363bb147f4857ede405d6f9b.jpg)  
Fig. 13. Orange County disease moving average data by month.

![](/api/attachments/9DKUUJET/fulltext/images/367fbbeaf719f705ec4c1f29aca95245e698315fda163a97edbc141f35b57489.jpg)  
Fig. 14. Florida hospital disease data.  
For Help, press F1

![](/api/attachments/9DKUUJET/fulltext/images/ebe89b00c2c992b4dcf603d819f1f466d70819bda67c22fdecdee555a997a6e5.jpg)  
Fig. 15. Data analysis of respiratory diseases.

Within individual counties, it is possible to select specific hospitals. Florida Hospital is one of the major hospitals in Orange County and one of the largest healthcare institutions in the state. Fig. 14 shows quarterly disease data from 2000 and 2001. Even at this finer level of detail, the somewhat elevated second (and possibly third) quarter data remains evident. The graphical capabilities of the OLAP tool are also used to present trend lines for visual analysis.

Finally, in Fig. 15, we incorporate another year and additional dimensions such as age into the query mix, explicitly selecting a county, hospital, and threat group. The age ranges are shown along the righthand axis. Overall, the first and second quarters of 2001 have slightly higher incidences, with most of the difference due to acute respiratory infections in the very young. While it would require further detailed analyses beyond our current study to prove that such problems are directly related to the wildfires, the analytic process demonstrates how easily one can investigate patterns using OLAP technologies in this domain. We believe that OLAP technologies have great potential to be used to rapidly uncover potential issues, prepare for further investigations, and plan for possible responses, all very important tasks for any surveillance system.

## 7. Preliminary spatial and statistical analyses

A data warehouse infrastructure also provides the opportunity to couple statistical and spatial analyses with OLAP presentations. The data can be pivoted or reformatted within the data warehouse to suit multiple analytic approaches.

## 7.1. Spatial analysis of 1998 Florida wildfires

We performed a preliminary spatial analysis by selecting the ten largest burn scars from the 1998 wildfires along with the intersecting ZIP codes. Fig. 16 displays the locations of the selected ZIP codes used for this study. The purpose of this analysis is to see if ZIP codes in close proximity to large wildfires have increased levels of a specific respiratory illness (in this case, asthma). The selected ZIP codes are compared with the non-selected ZIP codes. The findings from the preliminary analysis are promising.

![](/api/attachments/9DKUUJET/fulltext/images/495b7502c308d663b431e994a55eab3c2aacf874616e0277eddda1aa52fe431e.jpg)  
Fig. 16. Selected ZIP codes for spatial analysis.

As noted earlier, respiratory illnesses data have strong seasonality with more admissions in the winter months than in the summer. Therefore, respiratory illnesses are compared from quarter-to-quarter and year-to-year. To account for population growth, respiratory illness rates per 100,000 people are calculated based upon the populations of the particular years. In addition, since this is a retrospective analysis, 1999 is compared to 1998 to eliminate changes simply due to increases in population. If there are higher respiratory admissions in 1998 then this is potentially due to wildfires, not simply population growth. Comparing 1999 to 1998 is also more conservative since there were some moderate size wildfires in 1999 in the proximity of the selected 1998 wildfire ZIP codes. A comparison of means of the difference in asthma-related respiratory illness per 100,000 people between the years 1999 and 1998 for selected ZIP codes (those that intersect the 10 largest burn scars, 21 ZIP codes) and unselected ZIP codes (834 ZIP codes) reveals a statistically significant difference at a 99% confidence level. As can be seen in Table 3, fireaffected ZIP codes have a higher mean asthma rate in 1998 than the non-fire-affected ZIP codes. It is interesting to note that the opposite is true in subsequent years when fires were not as prevalent.

## 7.2. Statistical analysis of 2001 Florida wildfire data

To further assess the accuracy of the trends found in the data warehouse OLAP analysis, the wildfire data are also analyzed using traditional statistical methods. The rigor of these statistical methods makes them somewhat unsuitable for real-time threat detection. There are also considerable, and well-documented, difficulties in isolating the health affects of transient events such as wildfires [20].

Table 3  
Mean asthma rates per 100,000 people

<table><tr><td></td><td>1998</td><td>1999</td><td>2000</td></tr><tr><td>Fire-affected ZIP codes</td><td>152.7</td><td>122.9</td><td>118.8</td></tr><tr><td>Non-fire-Affected ZIP codes</td><td>120.2</td><td>140.2</td><td>135.5</td></tr></table>

These difficulties not withstanding we develop a preliminary model based on traditional statistical techniques. A generalized linear (regression) model is developed with the rate of hospitalizations for asthma for two vulnerable age groups: children less than 4 years of age and older adults aged 65 or older. Data for each quarter of a three-year period (1998– 2000) are analyzed. Standard statistical procedures with nested/repeated data will likely lead to biased standard errors and test statistics [10]. To adjust for potential bias introduced by utilizing nested/repeated data we apply generalized estimating equations (GEE) to the model. GEE provides a convenient, flexible way to solve problems presented with this type of data [3].

The unit of analysis for the model is ZIP code. The dependent variable is the rate of discharges for asthma within each age group. The independent variable of interest is the extent of the wildfires with four levels defined as no fires, <1000 acres burned, 1000–10,000 acres burned, and >10,000 acres burned. The models are adjusted for the following covariates that have previously been shown to impact rates of hospitalizations at the ZIP code level: 1) percent of the population over the age of 65; 2) percent black population; 3) percent female; 4) percent Hispanic; 5) the total acreage burned; and 6) percent of household with income of \$15,000 or less. No statistically significant differences were found in the model using discharges for patients age 4 or younger. In models restricted to those over the age of 65, however, ZIP codes with fires had statistically higher rates of hospital discharges for asthma than those with no fires. ZIP codes with <1000 acres burned report approximately 9% increase in discharges for asthma $( p { = } 0 . 0 0 0 7 )$ ), those with 1000–10,000 acres burned report approximately 13% increased discharges for asthma $( p = 0 . 0 2 8 7 )$ , and those with greater than 10K acres burned report an approximately 32% increase in discharges for asthma $\scriptstyle ( p = 0 . 0 1 6 9 )$

These findings suggest that traditional statistical models, particularly those that allow for modeling of complex relationships may provide a framework for interpreting results for bioterrorism surveillance. In addition, these analyses show that Florida wildfire data, coupled with detailed health status indicators, could be useful as a naturally occurring surrogate for biochemical attacks. Wildfires are akin to point source attacks, the effect sizes are realistic and detectable, and there is a considerable amount of data available. Our efforts should be seen as an initial effort to develop statistical models to support bioterrorism surveillance. As the surveillance systems evolve and more precise spatial information becomes available more precise statistical models will be possible [14].

## 8. Research contributions and future directions

The urgent public need for effective bioterrorism surveillance systems has led our research team to extend the CATCH data warehouse with a focus on detecting and investigating abnormal illness patterns. The important research contribution of this paper is the adroit application of data warehouse OLAP query tools for identifying and exploring patterns of illness that might indicate the presence of a biological or chemical agent in the environment. OLAP tools are readily available and fairly easy to use yet still provide powerful query capabilities in a defined data warehouse environment. These techniques can accelerate the investigative processes that characterize human-in-the-loop efforts to understand and respond to critical events. In addition, the coupling of Florida wildfire data with detailed health status indicators provides a laboratory for investigating bioterrorism surveillance techniques. Other research contributions include a proposed data warehouse architecture for surveillance and our preliminary research ideas on real-time data warehousing.

We report two distinct sets of analyses that are performed using Florida wildfire data sets from years 1998 and 2001. An OLAP analysis of the 1998 wildfires demonstrates the ability to group data by ZIP code and fire size to study the occurrence of respiratory illnesses across these data dimensions. A retrospective analysis of the hospital admissions data surrounding the 2001 Florida wildfires illustrates the OLAP query techniques for drilling down into hospital admissions data to identify disease patterns. We demonstrate the ability to rapidly and effectively use OLAP queries on the data warehouse to identify and analyze illness patterns. We are able to easily slice the data along dimensions of time (from days to years), illness (ICD codes for respiratory and infectious illnesses), geography (Orange County), hospital (Florida Hospital), and age. Finally, we also demonstrate the extension of wildfire analyses to spatial and statistical methods. The data warehouse provides an excellent infrastructure for both exploratory and confirmatory analyses, providing the tools to re-organize the data for particular analytic methods. Indeed, the OLAP analyses, as well as spatial and statistical approaches, demonstrate the utility of the Florida wildfire data as a realistic focus for further experiments with bioterrorism surveillance methods.

Our future research directions on bioterrorism surveillance systems include three main activities.

➢ Coupling the data warehousing approaches and historical data with efforts in syndromic surveillance, including pattern recognition techniques that will automatically generate alerts. The most promising results will come from using both real-time data and well designed historical repositories.

➢ Using the data warehouse as an infrastructure for experimenting with pattern recognition algorithms that signal potentially abnormal events based on the selected threat indicators. Developing and evaluating statistical and machine learning techniques requires significant volumes of data.

➢ Lastly, the wildfire data provide a very interesting natural case study for work in bioterrorism surveillance. We hope to use the data to construct simulations for training, as well as for a research infrastructure. While much of the current data is based on hospital discharge events, future research will also include data from emergency room visits throughout Florida.

## Acknowledgements

We gratefully acknowledge the efforts of many colleagues and students who have contributed to the development of the CATCH data warehouse during its history. In particular, Sunil Bhat assisted us with many of the OLAP analyses shown in the paper.

## References

[1] J. Ackelsberg, S. Balter, et al., Syndromic surveillance for bioterrorism following the attacks on the WTC-NYC, 2001, Morbidity & Mortality Weekly Report, Center for Disease Control and Prevention, 2002 (September 19).

[2] L. Agosta, K. Gile, Real-Time Data Warehousing: the Hype and the Reality, White Paper, Forrester Research, Inc,, 2004 (December).

[3] P. Allison, Logistic Regression Using the SAS System: Theory and Application, SAS Institute Inc., Cary, NC, 1999.

[4] J. Ballman, Case study: when the smoke cleared, Disaster Recovery Journal 17 (1) (2004) 16–20.

[5] E. Barthell, W. Cordell, et al., The Frontlines of Medicine Project: a proposal for the standardized communication of emergency department data for public health uses including syndromic surveillance for biological and chemical terrorism, Annals of Emergency Medicine 39 (4) (2002 (April)) 422–429.

[6] D. Berndt, J. Fisher, A. Hevner, J. Studnicki, Healthcare data warehousing and quality assurance, IEEE Computer 34 (12) (2001 (December)) 33–42.

[7] D. Berndt, A. Hevner, J. Studnicki, The CATCH data warehouse: support for community health care decision making, Decision Support Systems 35 (2003) 36–384.

[8] D. Berndt, A. Hevner, J. Studnicki, Bioterrorism surveillance with real-time data warehousing, Proceedings of First NSF/NIJ Symposium on Intelligence and Security Informatics (ISI 2003), Lecture Notes in Computer Science, LNCS, vol. 2665, Springer-Verlag, June 2003, pp. 322–335.

[9] D.M. Bravata, et al., Evaluating detection and diagnostic support systems for bioterrorism response, Emerging Infectious Diseases 10 (1) (January 2004) 100–108 (www.cdc.gov/eid).

[10] P. Diggle, P. Heagerty, K. Liang, S. Zeger, Analysis of Longitudinal Data, Second editionOxford University Press, 2002.

[11] Kaufmann, et al., The economic impact of a bioterrorist attack: are prevention and postattack intervention programs justifiable? Emerging Infectious Diseases 3 (1997) 83–94.

[12] R. Kimball, Realtime partitions, Intelligent Enterprise 5 (3) (2002 (February 1)).

[13] J. Lampel, Z. Shapira, Judgmental errors, interactive norms, and the difficulty of detecting strategic surprises, Organization Science 12 (5) (2001 (September–October)) 599–611.

[14] A. Lawson, Statistical Methods in Spatial Epidemiology, John Wiley & Sons Ltd, New York, 2001.

[15] R. Lazarus, K. Kleinman, et al., Use of automated ambulatorycare encounter records for detection of acute illness clusters, including potential bioterrorism events, Emerging Infectious Diseases 8 (8) (2002 (August)) 753–760.

[16] W. Lober, B. Karras, et al., Roundtable on bioterrorism detection: information system-based surveillance, Journal of the American Medical Informatics Association 9 (2) (2002 (March–April)) 105–115.

[17] NEDSS Working Group, National electronic disease surveillance system (NEDSS): a standards-based approach to connect public health and clinical medicine, Journal of Public Health Management and Practice 7 (6) (2001 (November)) 43–50.

[18] Overhage, et al., Electronic laboratory reporting: barriers, solutions and findings, Journal of Public Health Management and Practice 7 (6) (2001 (November)) 60–66.

[19] C. Pittman, A breath of fresh air hard to come by here, St. Petersburg Times (2001 (May 26)) 1A.

[20] R. Puett, A. Lawson, A. Clark, T. Aldrich, D. Porter, C. Feigley, J. Hebert, Scale and shape issues in focused cluster power fo count data, International Journal of Health Geographics 4 (8) (2005).

[21] D. Relman, J. Olson, Bioterrorism preparedness: what practi tioners need to know, Infectious Medicine 18 (11) (2001 (November)) 497–515.

[22] L. Rotz, A. Khan, et al., Public health assessment of potential biological terrorism agents, Emerging Infectious Diseases 8 (2) (2002 (February)).

[23] Z. Shapira, Risk Taking: a Managerial Perspective, Russell Sage Foundation, New York, 1995.

[24] B. Sorenson, M. Fuss, Z. Mulla, W. Bigler, S. Wiersma, R. Hopkins, Surveillance of morbidity during wildfires—central Florida, 1998, Morbidity & Mortality Weekly Report, Center for Disease Control and Prevention, 1999 (February 5).

[25] F. Tsui, J. Espino, V. Dato, P. Gesteland, J. Hutman, M. Wagner, Technical description of RODS: a realtime public health surveillance system, Journal of the American Medical Informatics Association (JAMIA) 10 (5) (2003 (September)) 399–408.

[26] Wagner, et al., The emerging science of very early detection of disease outbreaks, Journal of Public Health Management and Practice 7 (6) (2001 (November)) 51–59.

[27] I. Walks, Preparing your organization for a terrorist attack, Disaster Recovery Journal 16 (3) (2003) 34–38.

![](/api/attachments/9DKUUJET/fulltext/images/02b864b072d98c36b18a8f89b789695de6795f24545b10535fe076a6dab539bd.jpg)

Donald J. Berndt is an Associate Professor in the Information Systems and Decision Sciences Department in the College of Business Administration at the University of South Florida. His research interests include database systems, data warehousing, data mining, and medical informatics. Dr. Berndt received a PhD in Information Systems from the Stern School of Business at New York University and a MS in Computer Science from the State University of New York at Stony Brook. He is

a member of Beta Gamma Sigma, ACM, AIS, and INFORMS.

John W. Fisher is Vice President and Chief Operating Officer of Medegy, a healthcare data warehousing company in Tampa, Florida. His research interests include data warehousing, the effect of electronic memory aids on expertise development, and data quality issues. Dr. Fisher received a PhD in Business Administration from the Information Systems and Decision Sciences Department in the College of Business Administration at the University of South Florida.

![](/api/attachments/9DKUUJET/fulltext/images/34ebf9d7f5b7ea1d06aee58d321b4d13e6ca36ec435b8995e03b9cbf5cea2cf6.jpg)

Jamie Griffiths Craighead is a doctoral student in the Information Systems and Decision Sciences Department in the College of Business Administration at the University of South Florida. Her research interests include geographic information systems, knowledge discovery, data mining, decision support systems, medical informatics, economics of information systems, and applications of information systems in healthcare. She has worked and studied in various countries and

has a background in economics, international studies, and geographic information systems.

![](/api/attachments/9DKUUJET/fulltext/images/6b8c98f2e5fe33a779bb70e3709b258a172f92f44365ebdf4e26a6941d4f1b8e.jpg)

Alan R. Hevner is an Eminent Scholar and Professor in the Information Systems and Decision Sciences Department at the University of South Florida, where he holds the Citigroup/Hidden River Chair of Distributed Technology. Dr. Hevner's areas of research interest include information systems development, software engineering, distributed database systems, health care information systems and telecommunications. He has published more than one hundred and twenty research

papers on these topics and has consulted for several Fortune 500 companies. Dr. Hevner has a Ph.D. in Computer Science from Purdue University. He has held faculty positions at the University of Maryland and the University of Minnesota. Dr. Hevner is a member of ACM, IEEE, AIS and INFORMS.

Stephen Luther is the Associate Director for Research Methods and Evaluation for the Patient Safety Center of Inquiry at the James A. Haley Veterans Administration Hospital and is an Affiliate Associate Professor in the Department of Health Policy and Management at the University Of South Florida College Of Public Health. Dr. Luther has a Ph.D. in measurement and evaluation with an emphasis on the measurement of health outcomes from the University of South Florida. His research interests include the use of both primary and secondary data to study health systems and outcomes.

![](/api/attachments/9DKUUJET/fulltext/images/37cb789bb1fb5c5473d98b204f376e3bdef2de5f16bc02f20869c241470d51af.jpg)  
James Studnicki is a Professor of Health Policy and Management at the University of South Florida’s College of Public Health. His research interests include measuring the health status of communities, evaluating alternative treatment outcomes, and studying the influence of managed care penetration on the utilization and quality of health services. Dr. Studnicki received a Sc.D. from Johns Hopkins University.
