---
otero_id: 8070
otero_key: "E2W3EXCA"
title: "Ensemble machine learning models for aviation incident risk prediction"
authors: "Xiaoge Zhang; Sankaran Mahadevan"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Ensemble machine learning models for aviation incident risk prediction

Xiaoge Zhang, Sankaran Mahadevan

![](/api/attachments/E2W3EXCA/fulltext/images/0a3d4fc421c43e437fe714692226ca461b72f3ebeee4cfd24138f8fb90372efe.jpg)

PII: S0167-9236(18)30166-0

DOI: https://doi.org/10.1016/j.dss.2018.10.009

Reference:

DECSUP 13001

To appear in: Decision Support Systems

Received date: 22 May 2018

Revised date: 6 September 2018

Accepted date: 17 October 2018

Please cite this article as: Xiaoge Zhang, Sankaran Mahadevan , Ensemble machine learning models for aviation incident risk prediction. Decsup (2018), https://doi.org/ 10.1016/j.dss.2018.10.009

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Ensemble machine learning models for aviation incident risk prediction

Xiaoge Zhang<sup>a</sup>, Sankaran Mahadevan<sup>a,∗</sup>

<sup>a</sup>Department of Civil and Environmental Engineering, Vanderbilt University, Nashville, TN 37235, USA.

## Abstract

With the spectacular growth of air trafic demand expected over the next two decades, the safety of the air transportation system is of increasing concern. In this paper, we facilitate the “proactive safety” paradigm to increase system safety with a focus on predicting the severity of abnormal aviation events in terms of their risk levels. To accomplish this goal, a predictive model needs to be developed to examine a wide variety of possible cases and quantify the risk associated with the possible outcome. By utilizing the incident reports available in the Aviation Safety Reporting System (ASRS), we build a hybrid model consisting of support vector machine and an ensemble of deep neural networks to quantify the risk associated with the consequence of each hazardous cause. The proposed methodology is developed in four steps. First, we categorize all the events, based on the level of risk associated with the event consequence, into five groups: high risk, moderately high risk, medium risk, moderately medium risk, and low risk. Secondly, a support vector machine model is used to discover the relationships between the event synopsis in text format and event consequence. In parallel, an ensemble of deep neural networks is trained to model the intricate associations between event contextual features and event outcomes. Thirdly, an innovative fusion rule is developed to blend the prediction results from the two types of trained machine learning models, thereby improving the prediction. Finally, the prediction on risk level categorization is extended to event-level outcomes through a probabilistic decision tree. By comparing the performance of the developed hybrid model against another three individual models with ten-fold cross-validation and statistical tests, we demonstrate the efectiveness of hybrid model in quantifying the risk related to the consequences of hazardous events.

Keywords: Air transportation, Deep learning, Support vector machine, System safety, Risk assessment

## 1. Introduction

The International Air Transport Association (IATA) forecasts that the air trafic demand will grow at a 3.7% annual Compound Average Growth Rate (CAGR), and there will be 7.2 billion air travelers in 2035 [1, 2]. Thus, compared to the 3.8 billion air travelers in 2016, the air travel demand will nearly double over the next two decades. The rapid growth in air trafic demand will put pressure on the

# ACCEPTED MANUSCRIPT

air transportation system, which is already struggling to cope with the current demand. System-wide departure delays and en-route congestion will deteriorate due to the massive increase in the number of aircraft within the limited airspace. Such consequences further contribute to an increased number of conflicts in the air trafic, which might escalate to collisions or evolve into other hazardous events [3, 4, 5]. The rapid increase of air trafic demand also puts tremendous pressure on air trafic operators in maintaining the system safety at the same level as before. All the aforementioned factors could increase the occurrence rate of air trafic incidents.

Since air trafic accidents usually have severe consequences, the safety of the air transportation system has received great attention [6, 7, 8]. Over the past decades, numerous eforts have been dedicated to the development on comprehensive safety metrics as well as qualitative/quantitative approaches to detect anomalous behavior, assess the safety, and quantify the risk associated with one subsystem (i.e., airport ground operations, flight tracking, or taxiway and runway system) or a mixture of subsystems in the air transportation system [9]. For example, Netjasov and Janic [10] performed a comprehensive review of four state-of-the-art methods, namely causal models, collision risk models, human error models, and thirdparty risk models, for the assessment of risk and safety in civil aviation. McCallie et al. [11] described a taxonomy of possible attacks on one of the most critical technical upgrades – Automatic Dependent Surveillance Broadcast (ADS-B) system – in the Next Generation (NextGen) Air Transportation System; they examined the risks inherent in the ADS-B implementation and their potential impact, thereby supporting risk mitigation and management. Margellos and Lygeros [12] used Monte Carlo Simulation (MCS) to assess the probability of flights meeting the Target Windows (TWs) constraints and the probability of aircraft having conflicts in the 4-D Trajectory-Based Operations (TBO). Landry et al. [13] developed a conflict detection and resolution (CD&R) decision support system for the airport surface operations, and illustrated this with an example from the Hartsfield Atlanta International Airport. Di Ciccio et al. [14] proposed a model to automatically detect flight trajectory anomalies by using semi-publicly available data for the sake of alerting the receiving parties to take responsive actions in a timely manner. Sankararaman et al. [15] investigated the vulnerability of Trajectory-Based Operations (TBO) to technology disruption, and evaluated the degradation of four key performance indicators (KPI) subject to the technological impairment.

In general, there are two principal strategies to enhance the air transportation system safety: (I) increase system/subsystem reliability, i.e., reduce the probability of operators making mistakes or systems having malfunctions; and (II) improve the operators’ preparedness. When a hazardous event occurs, the operator is able to take appropriate safety measures to reduce the cost of the consequence caused by the hazardous event in a timely manner [16, 17, 18]. Although tremendous progress has been made over the past decades for enhancing the air transportation system safety, most of the studies emphasize identifying the accident precursors and initiating corrective actions to prevent future errors, which can be grouped into the first strategy. Among the existing studies, much of the efort has been devoted to

# ACCEPTED MANUSCRIPT

investigating human factors induced accidents and constructing causal models [10, 19]. For example, Wiegmann and Shappell [20] described the Human Factors Analysis and Classification System (HFACS) and provided aviation case studies on human factor analysis with HFACS. However, air transportation is a complex system of systems involving many varied but yet interlinking distributed networks of human operators, technical/technological procedures and systems, and organizations/stakeholders. The scarcity in the operational data and the involvement of a variety of human operators are major challenges that severely afect the prediction of erroneous operation, and challenge the assessment and improvement of the system reliability. In view of this, it would be beneficial to leverage the second strategy and emphasize the “proactive safety” paradigm [21], focused on strengthening the capability and eficiency of the operators in response to the abnormal events with appropriate actions, thereby mitigating the consequence or severity of hazardous events. In this connection, a large number of incident/accident reports have been filed over the past half century together. A few machine learning studies have been carried out to analyze these reports. For example, Oza et al. [22] developed two algorithms – Mariana and nonnegative matrix factorization-based algorithm – to perform multi-label classification for the reports of Aviation Safety Reporting System (ASRS). Budalakoti et al. [23] presented a set of algorithms to detect and characterize anomalies in discrete symbol sequences arising from recordings of switch sensors in the cockpits of commercial airliners. These studies have not explored the intricate relationships between abnormal event characteristics and the induced consequences. In this paper, we are motivated to fill this gap by quantifying the risk associated with the consequence of hazardous events through a hybrid machine learning model. This type of analysis will help to develop a decision support system that can learn the patterns in the data and help the analyst examine incidents/accidents quickly and systematically, thus assisting the risk manager in risk quantification, priority setting, resource allocation and decision making in support of the implementation of proactive safety paradigm.

To do this, we have utilized the Aviation Safety Reporting System (ASRS), which is a database of incident reports that provides a plethora of incidents/accidents that occur over the course of the past several decades. The incident reports are submitted by pilots, air trafic controllers, dispatchers, cabin crew, maintenance technicians, and others, and describe both unsafe occurrences and hazardous situations [24]. ASRS covers almost all the domains of aircraft operations that could go wrong. However, it is a non-trivial task to build a model from the ASRS data for the prediction of risk associated with the consequence of hazardous events due to the following challenges:

1. High-dimensional data. Each incident record consists of more than 50 items ranging from the operational context (weather, visibility, flight phase, and flight conditions) to the characteristics of the anomalous operation (aircraft equipment, malfunction type, and event synopsis). The url https://asrs.arc.nasa.gov/docs/dbol/ASRS CodingTaxonomy.pdf gives a detailed description of each item. Besides, air trafic operation is a complex system composed of a number of programs

# ACCEPTED MANUSCRIPT

and personnel. It is likely for the incident to occur at any phase and location due to a variety of factors (i.e., operation violation, visibility, human factors etc.), which makes it hard for the machine learning algorithm to predict the exact level of risk associated with each event outcome.

2. Primarily categorical data. Over 99% of the items in the ASRS database are categorical, and only one attribute (crew size) is numerical in each record. Although the categorical information ofers a high-level description of the context of each incident, very limited information specific to each abnormal event can be derived from such categorical information, e.g., how did the incident happen, how did the incident evolve over time in the system, what operation the pilot took to resolve the issue, etc. Since the categorical features are not informative, how to blend the predictions of the model trained by the categorical features and the predictions from the model trained by other informative indicators (e.g., event synopsis) without compromising the model performance is an issue worthy of investigation.

3. Unstructured data. One important unstructured attribute is event synopsis, which is a concise summary of the incident/accident in the form of text. Mining causal relationships from the unstructured text data is a daunting task [25]. A common characteristic in handling text data is to transform it into numerical data in the representation of term frequency of each individual document. Along this direction, researchers have developed numerous techniques to elicit useful knowledge from the text data, e.g., support vector machine [26], latent Dirichlet allocation-based topic mining [27, 28, 29], Na¨ıve Bayes-based document classification [30], k-nearest-neighbor (k-NN) classification [31], and others [32, 33]. Among them, support vector machine [34] has demonstrated good performance in text categorization because it overcomes over-fitting and local minima, thereby achieving good generalization to applications [35, 36].

4. Imbalanced class distribution. In the ASRS, the number of records in one class (i.e., possible utcome) is significantly larger than that of the others. The distribution of the outcomes for all the hazardous events reported between January 2006 and December 2017 is illustrated in Fig. 1. As can be observed, the number of records across diferent classes is highly imbalanced. Such imbalanced class distribution has posed a serious challenge to machine learning algorithms which assume a relatively well-balanced distribution [37].

Since ASRS consists of a variety of heterogeneous data (e.g., text data, categorical data, and numerical data), it is challenging to develop one single model to learn from the entire dataset for predicting the risk associated with the consequence of hazardous events. In this paper, we adopt the “divide and conquer” strategy to split the data into two parts: structured and unstructured, and develop a hybrid model to handle the two types of data, respectively. By doing this, we are able to leverage the strengths of each model in processing certain type of data. Compared with building a single model, the dimension of the problem is reduced significantly. With respect to categorical data, considering its high-dimensiona feature space, deep learning might be a good candidate to discover the highly intricate relationship between event contextual characteristics and event consequence due to its powerful ability in establishing a dense representation of the feature space, which makes it efective in learning high-order features from the raw data [38, 39]. As a result, a deep learning model is developed to process the categorical data for the purpose of learning the associations between event contextual features and event outcomes. In parallel, a support vector machine model is trained to identify the relationships between text-based event synopsis and the risk level associated with the consequence of each incident. Afterwards, the predictions from the two machine learning models are fused together for quantifying the risk associated with the consequence of each incident. Finally, the prediction on risk level categorization is extended to event-level outcomes through a probabilistic decision tree. Compared to the current state of the art in machine learning for aviation safety, we make the following contributions:

![](/api/attachments/E2W3EXCA/fulltext/images/092ace74e9ac0f28243005601cdd68948d7bbaeec0f23e6d58df549ea5e48ef4.jpg)  
Figure 1: Distribution of outcomes for all incidents/accidents between January 2006 and December 2017.

1. We have developed a machine learning methodology to learn the relationships between abnormal event characteristics and their consequences. We focus on the data set that has a large number of outcomes and imbalance of available data regarding these outcomes. This challenge is overcome by grouping the event outcomes into five risk categories and by up-sampling the minority classes.

2. A probabilistic fusion rule is developed to blend the predictions of multiple machine learning models that are built on diferent segments of the available data. Specifically, a hybrid model blending SVM prediction on unstructured data and deep neural network ensemble on structured data is developed to quantify the risk of the consequence of hazardous events, in which the record-level prediction probabilities, class-level prediction accuracy in each respective model, and the proportion of each class in the records with disagreeing predictions are considered in model fusion.

The rest of the paper is structured as follows. In Section 2, we provide a brief introduction to the ASRS database, and describe the principal elements in each record. In Section 3, we develop a hybrid model to learn the complex relationships between event characteristics and event outcomes. In Section 4, we evaluate the performance of the trained machine learning model on a test dataset. In Section 5, we provide concluding remarks and discuss future research directions.

## 2. Aviation Safety Reporting System

The Aviation Safety Reporting System (ASRS) is a program operated by the National Aeronautics and Space Administration (NASA) with the ultimate goal of increasing aviation system safety by discovering system safety hazards hidden in the multitude of air trafic operations. Over the past few decades, ASRS has become one of the world’s largest sources of information on aviation safety and human factors [24]. As one of its primary tasks, ASRS collects, processes, and analyzes voluntarily submitted aviation incident/situation reports from pilots, flight attendants, air trafic controllers, dispatchers, cabin crew, ground workers, maintenance technicians, and others involved in aviation operations.

Reports submitted to ASRS include both unsafe occurrences and hazardous situations. Each sub mitted report is first screened by two analysts to provide the initial categorization and to determine the triage of processing. During this process, ASRS analysts identify hazardous situations from the reports, and issue an alert message to persons in a position to correct them. Based on the initial categorization, ASRS analysts might aggregate multiple reports on the same event to form one database “record”. If any information needs to be further clarified, ASRS analysts might choose to call a reporter over the telephone to gather more information. After all the necessary information is collected, the reports are codified using the ASRS taxonomy and recorded in the database. Next, some critical information in each record is de-identified; then ASRS distributes the incident/accident records gathered from these reports to all the stakeholders in positions of authority for future evaluation and potential corrective action development.

Table 1 presents a sample situation record extracted from the ASRS database. As can be observed, each record has more than 20 fields ranging from event occurrence location to event characteristics. Here, we briefly introduce several primary attributes in each record:

1. Time and location of the abnormal event: The incident in Table 1 occurred on February 2017 at the BUR airport in USA. Here, BUR is the International Air Transport Association (IATA) code of the airport, and it refers to the Hollywood Burbank Airport located in Los Angeles County, California. Besides, the record also provides the basic altitude above Mean Sea Level (MSL). In this case, the hazardous event occurred when the flight was at an altitude of 2500 feet.

2. Environment: This describes the surrounding conditions encompassing the aircraft operations. Examples are: flight conditions (VMC, IMC, marginal, or mixed), and weather elements such as visibility, light, and ceiling. Here, VMC refers to visual meteorological condition (VMC) under visual flight rules (VFR) flight. In VMC, pilots have suficient visibility to fly the aircraft maintaining visual separation from the terrain and other aircraft. Diferent from VMC, instrument meteorologi cal condition (IMC) represents the category that describes weather conditions that require pilots to fly primarily by reference to instruments under instrument flight rules (IFR). Visibility and cloud ceiling are two key factors in determining whether the weather condition is VMC or IMC, and the boundary between IMC and VMC is known as VMC minima. “Marginal VMC” refers to conditions above but close to one VMC minima or more.

Table 1: A sample incident/accident record extracted from ASRS

<table><tr><td>Attribute</td><td>Content</td></tr><tr><td>Time / Day</td><td>Date : 201702Local Time Of Day : 0601-1200</td></tr><tr><td>Place</td><td>Locale Reference.Airport : BUR.AirportState Reference : CAAltitude.MSL.Single Value : 2500</td></tr><tr><td>Environment</td><td>Flight Conditions : VMCWeather Elements / Visibility.Visibility : 10Light: DaylightCeiling.Single Value : 12000</td></tr><tr><td>Aircraft</td><td>Reference : XATC / Advisory.Center : BURAircraft Operator : PersonalMake Model Name : PA-28R Cherokee Arrow All SeriesCrew Size.Number Of Crew : 1Operating Under FAR Part : Part 91Flight Plan : VFRMission : PersonalFlight Phase : Initial ApproachRoute In Use : Visual ApproachAirspace.Class D : VNY</td></tr><tr><td>Component</td><td>Aircraft Component : Engine AirProblem : Malfunctioning</td></tr><tr><td>Person</td><td>Reference : 1Location Of Person : XLocation In Aircraft : Flight DeckReporter Organization : PersonalFunction.Flight Crew : Single PilotQualification.Flight Crew : PrivateExperience.Flight Crew.Total : 175Experience.Flight Crew.Last 90 Days : 30Experience.Flight Crew.Type : 175ASRS Report Number.Accession Number : 1428684Human Factors : Confusion</td></tr><tr><td>Events</td><td>Anomaly.Deviation - Altitude : Excursion From Assigned AltitudeAnomaly.Deviation - Track / Heading : All TypesAnomaly.Deviation - Procedural : ClearanceAnomaly.Inflight Event / Encounter : Unstabilized ApproachDetector.Person : Air Traffic ControlWhen Detected : In-flightResult.Flight Crew : Returned To ClearanceResult.Flight Crew : Became ReorientedResult.Air Traffic Control : Issued New ClearanceResult.Air Traffic Control : Issued Advisory / Alert</td></tr><tr><td>Assessments</td><td>Contributing Factors / Situations : Airspace StructureContributing Factors / Situations : Human FactorsPrimary Problem : Human Factors</td></tr><tr><td>Synopsis</td><td>PA28R pilot reported becoming confused during a VFR flight to BUR and lined up on VNY. BUR Tower detected the error and issued a new heading and climb back to assigned altitude.</td></tr></table>

3. Aircraft: This attribute reports the basic aircraft and flight information, including the aircraft make and model, flight type (personal or commercial), the number of crew onboard, flight plan, flight mission, flight phase, and the airspace class the flight is in. Such information details the specific flight phase in which the hazardous event occurs. The basic aircraft information also enables us to have an understanding of the scale of the possible event consequence.

4. Component: If there is any mechanical failure in the aircraft, the record will have the component field, and it describes which aircraft component is faulty (i.e., engine, nosewheel, transponder etc.) and the type of the problem as well (i.e., malfunctioning, improperly operated, or others). This field might be empty if there is no component malfunction.

5. Person: Person describes the fundamental information of the personnel that reports the problem. For example, the location of the person, his/her location in the aircraft, the reporter organization, the qualification of the reporter, and the contributing human factor (e.g., fatigue, distraction, confusion, and time pressure).

6. Events: This attribute provides the basic characteristics of anomalous behavior and its consequence. In this record, BUR Tower detected the excursion of the flight from the assigned altitude and issued course correction to avoid the trafic. After taking course correction to avoid trafic, the pilot did not maintain the same course heading to Burbank while ATC assumed that the pilot was on correct heading. As a result, the BUR Tower recognized the error and issued a new heading and commanded the pilot to climb back to the assigned altitude to perform landing from the very start.

7. Assessments: Assessments provide evaluation of the root cause and other factors that contribute to the occurrence of the abnormal event.

8. Synopsis: All the above fields are categorical except the crew size. The last row of Table 1 and Table 2 provide several sample event synopses elicited from the ASRS database. As can be observed, event synopses gives a brief summary of the cause of the problem, and how the abnormal event evolves over time. Such information is helpful for us to assess the severity of the hazardous event and analyze possible consequences.

Table 2: Two examples of event synopsis in ASRS

<table><tr><td>Date</td><td>Event Synopsis</td></tr><tr><td>February, 2017</td><td>A319 Flight Attendant reported smoke in the cabin near the overwing exits during climb.</td></tr><tr><td>January, 2017</td><td>A319 flight crew reported fumes in the flight deck. After a short time they began to experience problems concentrating and the onset of incapacitation.</td></tr></table>

The above descriptions provide a brief introduction to the physical meanings of some important fields in each record. In ASRS, other records might difer from the above sample records in certain fields or they might have additional fields which are absent in the sample record due to the diference in the type and characteristics of the abnormal event.

## 3. Proposed Method

In this section, we develop a hybrid method to estimate the risk of the event consequence with the consideration of operational conditions and event characteristics. To build the hybrid model, we investigate the incidents/accidents that occurred from January 2006 to December 2017. The detailed proposed framework is outlined in Fig. 2, which shows a four-step procedure. In the first step, we perform a risk-based event outcome categorization. That is we employ the level of risk as a quantitative metric to measure the severity of the event outcome and collapse all the possible event outcomes into five categories: high risk, moderately high risk, medium risk, moderately medium risk, and low risk. Given the restructured categories, two models are developed in the second step to process the unstructured data (text data) and structured data (categorical and numerical information). Specifically, a support vector machine (SVM) model is developed to represent the relationship between event synopsis and the risk pertaining to the event outcome, and an ensemble of deep neural networks (DNN) is trained to predict the level of risk based on contextual features of each abnormal event. In the third step, we develop an innovative fusion rule to blend the prediction results from the SVM and DNN models. Finally, the risk-level prediction is further expanded to event-level outcome analysis in through a probabilistic tree.

## 3.1. Risk-based Event Outcome Categorization

As shown in Fig. 1, there are 36 unique event outcomes among the incident reports. Because almost all of the contextual features are categorical, they are uninformative indicators of the event outcome considering that one contextual condition might correspond to a large number of event outcomes that belong to diferent risk levels. For example, if we are only given the weather visibility, it is challenging to predict what might happen because the information is too limited. In other words, there exist too many possible scenarios given the weather visibility. From this perspective, event synopsis is the only attribute left that can help us to diferentiate the event outcome. Since the event synopsis embodies the complex event evolution process, it is dificult to use the current state-of-the-art text mining techniques to understand the semantics, discover the causal relationships, mine the event sequences, and associate with the event consequence from such a short and condensed report. Considering that there are 36 unique event outcomes, the machine learning algorithm is challenged by the lack of significant predictors in the ASRS records that can be used to distinguish the event outcomes.

![](/api/attachments/E2W3EXCA/fulltext/images/2c8bbf4568be13339b9794e1c1c5f233341e38326c7e95595e7de329d858471d.jpg)  
Figure 2: Hybrid machine learning framework for risk prediction.

Another challenge is that the class distribution is severely imbalanced. In such circumstances, the standard classification algorithms are often biased toward the majority class, leading to a high misclassi fication rate for the minority class [40, 41, 42]. To overcome this problem, one popular way is to generate additional samples by randomly duplicating observations from the existing records in the minority class with replacement (referred to as up-sampling in the rest of the paper) so as to balance the number of records for the majority and minority classes. Since the ratio between the majority class 1 and minority class 36 is larger than 1000, a large number of samples needs to be generated to increase the number of records for the minority class. As can be observed from Fig. 1, this is also true for many other minority classes. Therefore, some additional operations need to be considered to reduce the number of samples that need to be generated. Also, the prediction model built with the upsampled data needs to account for the upsampling.

The last issue is that one abnormal event might result in multiple outcomes. For example, as shown in the eighth row of Table 1, there are four diferent types of outcomes (as underlined in Table 1) for this sample record. It is impossible to train four individual machine learning models with each model being used to predict a particular event outcome. Besides, accident/incident records with multiple consequences are not rare in the ASRS database, and occupy almost 50% of the entire data.

To address the above three challenges, we develop a risk-based event outcome categorization, where each event outcome is associated with a specific risk indicator out of five categories: high risk, moder ately high risk, medium risk, moderately medium risk, and low risk. According to the severity of event consequence, each event is assigned to a particular risk group based on expert opinion. Table 3 reports the five risk categories and the set of outcomes belonging to that risk category. By doing this, we collapse the original 36 unique event outcomes into five groups, and project the event outcome to one of the five risk groups. Now, even if an event has multiple consequences, we can identify the highest risk group corresponding to the outcomes of that event, and use it to indicate the amount of risk related to that abnormal event. Another benefit is that the number of samples that need to be generated to balance the majority and minority classes is reduced by a large factor. Fig. 3 illustrates the class distribution after the collapse operation. It can be noticed that the class distribution is in better shape compared to the distribution of the original 36 classes. The ratio between the class with the most number of records and the class with the least number of records is reduced from 1000 to 2.1. The decrease in the number of samples that need to be generated also mitigates the computational efort for the machine learning models constructed in the next section.

Table 3: Mapping between risk levels and event outcomes

<table><tr><td>Risk Level</td><td>Event Outcome</td></tr><tr><td>High risk</td><td>General Declared EmergencyGeneral Physical Injury / IncapacitationFlight Crew Inflight ShutdownAir Traffic Control Separated TrafficAircraft Damaged</td></tr><tr><td>Moderately high risk</td><td>General EvacuatedFlight Crew Regained Aircraft ControlAir Traffic Control Issued Advisory / AlertFlight Crew Landed in Emergency Condition</td></tr><tr><td>Medium risk</td><td>General Work RefusedFlight Crew Became ReorientedFlight Crew DivertedFlight Crew Executed Go Around Missed ApproachFlight Crew Overcame Equipment ProblemFlight Crew Rejected TakeoffFlight Crew Took Evasive ActionAir Traffic Control Issued New Clearance</td></tr><tr><td>Moderately medium risk</td><td>General Maintenance ActionGeneral Flight Cancelled DelayedGeneral Release Refused Aircraft Not AcceptedFlight Crew Overrode AutomationFlight Crew FLC Overrode AutomationFlight Crew Exited Penetrated AirspaceFlight Crew Requested ATC Assistance ClarificationFlight Crew Landed As PrecautionFlight Crew Returned To ClearanceFlight Crew Returned To Departure AirportAircraft Automation Overrode Flight Crew</td></tr><tr><td>Low risk</td><td>General Police Security InvolvedFlight Crew Returned To GateAircraft Equipment Problem DissipatedAir Traffic Control Provided AssistanceGeneral None Reported TakenFlight Crew FLC complied w Automation Advisory</td></tr></table>

![](/api/attachments/E2W3EXCA/fulltext/images/01148b7a821c88444e095e937e9ff80ba4f51de25f18f325936be746bb4988af.jpg)  
Figure 3: Distribution of risk outcomes after recategorization of incidents/accidents from January 2006 to December 2017.

## 3.2. Model Construction

The ASRS data can be classified into two groups: structured data and unstructured data. In particular, structured data include numerical data (e.g., crew size) and categorical data (e.g., flight phase, weather visibility, flight conditions etc.). In ASRS, event synopsis is the only unstructured data, and it is used to describe how the accident/incident occurred.

Before developing the two machine learning approaches, we up-sample the minority classes in the restructured risk domain. Basically, up-sampling is the process of randomly duplicating observations from the minority class to reinforce its signal. With respect to the reorganized risk categories, we perform resampling with replacement for the three minority classes, namely: high risk, moderately high risk and moderately medium risk, so that the number of records for them matches with the majority class (medium risk). After the up-sampling operation, we develop two individual models to handle the structured and unstructured data, separately. The flowchart of the developed method is illustrated in Algorithm 1.

## 3.2.1. Support Vector Machine for Text-based Classification

Regarding the text data, our objective is to automatically categorize the abnormal event into the correct risk category based on the content of the event synopsis. In the past decades, a large number of statistical and computational methods have been developed for classification based on text data [33, 43],

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 : Hybrid model development
Input: Two already trained models: support vector machine $M_1$ and ensemble deep neural networks $M_2$, and a test dataset $D = \{(\mathbf{x}_1, y_1), (\mathbf{x}_2, y_2), \ldots, (\mathbf{x}_m, y_m)\}$
Process:
1: for $t = 1$ to $m$ do
2:    if $M_1(\mathbf{x}_t) = M_2(\mathbf{x}_t)$ then
3:    Output the prediction
4:    else if $M_1(\mathbf{x}_t) \neq M_2(\mathbf{x}_t)$ then
5:    Calculate the proportion of each class in the records with disagreeing predictions
$p(j) = \frac{N_j - \lambda_j \times N_j^c}{\sum_{k=1}^{5} (N_k - \lambda_k \times N_k^c)}$,    for $j = 1, 2, \ldots, 5$
6:    Compute record-level prediction probabilities for $\mathbf{x}_t$ in the two trained models $M_1$ and $M_2$
7:    Compute the model predictions for record $\mathbf{x}_i$ $p(Y_{\mathbf{x}_t}^s = i) \propto \sum_{j=1}^{5} \left[ p(\mathbf{Y} = i | \hat{\mathbf{Y}}^s = j) \times p(\hat{Y}_{\mathbf{x}_t}^s = j) \times \frac{N_j - \lambda_j \times N_j^c}{\sum_{k=1}^{5} (N_k - \lambda_k \times N_k^c)} \right]$ $p(Y_{\mathbf{x}_t}^d = i) \propto \sum_{j=1}^{5} \left[ p(\mathbf{Y} = i | \hat{\mathbf{Y}}^d = j) \times p(\hat{Y}_{\mathbf{x}_t}^d = j) \times \frac{N_j - \lambda_j \times N_j^c}{\sum_{k=1}^{5} (N_k - \lambda_k \times N_k^c)} \right]$
8:    Return the label with the highest prediction probability from $p(\mathbf{Y}_{\mathbf{x}_t}^s)$ and $p(\mathbf{Y}_{\mathbf{x}_t}^d)$
9:    end if
10:    end for
Output: hybrid model prediction
for example, Naïve Bayes [44, 45], support vector machine [46], maximum entropy [47], and others [48]. The support vector machine (SVM) has been found to provide a higher prediction accuracy than most other techniques [49]. Different from other classifiers, SVM implements a structural risk minimization function, which entails finding an optimal hyperplane to separate the different classes with the maximum margin. The introduction of the structural risk minimization (regularization term) function also enables SVM to have a good generalization characteristic, thereby guaranteeing the lower classification error on unseen instances.
The first essential step in applying SVM for text classification is to transform the text data into numerical feature vectors; this is referred to as text representation. Since the text descriptions of the incidents/accidents appear in the form of long sentences in different records, we employ the bag-of-words
</div>

# ACCEPTED MANUSCRIPT

(BoW) representation to transform the text data into numerical features. Specifically, we utilize the tokenizer in the natural language processing toolbox to split raw text into sentences, words and punctu ation [50]. Afterwards, all the stop words and punctuation are eliminated from the BoW representation, and we extract distinct words from all the event synopsis records, assign a fixed integer id to each term present in any event synopsis, and represent the content of a document as a vector in the term space, which is also referred to as a vector space model. However, in many cases, term frequency alone might not be adequate in diferentiating the documents. For example, since the word ‘the’ is a very common term that appears in every document, the term frequency method will tend to incorrectly emphasize documents with the usage of frequent terms (such as, ‘the’, ‘a’) but carrying very little information about the contents of the document, while more meaningful terms might be shadowed. As developed by Sp¨arck Jones [51], the term frequency-inverse document frequency (TF-IDF) method overcomes this drawback by determining the relative frequency of a word in a document compared to the inverse proportion of that word across all the documents, which is defined as:

$$
\operatorname{tf-idf} (t, d) = \operatorname{tf} (t, d) \times \left(1 + \log \frac {1 + n _ {d}}{1 + \operatorname{df} (d , t)}\right)\tag{1}
$$

where tf $( \mathrm { t } , \mathrm { d } )$ is the number of occurrences of term t in document d, $n _ { d }$ is the total number of documents, and df (d, t) is the number of documents that contain the term t.

By performing this operation, we can increase the term’s discriminating ability and make the weight of terms suitable to be used by the classifier. Given the TF-IDF vector representation of each event synopsis, we feed it into a support vector machine model in order to identify a hyperplane that separates the diferent classes with the maximum margin. In the next section, we will discuss the details on how to tune the model parameters in the support vector machine model.

## 3.2.2. Ensemble of Deep Neural Networks

With respect to the structured data, there are 29 diferent data items after removing the attributes which are empty in 80% of the records. As shown in Fig. 2, the structured data can be further classified into three groups: flight conditions, event characteristics, and operations. The flight conditions primarily depict the basic operational condition for each flight, including the weather condition, airport visibility, aircraft characteristics (i.e., model, flight mission, and flight plan), the persons involved (i.e., location of person, reporter organization), and other contributing factors (i.e., ATC equipment, human factors, and communication ambiguity). The flight conditions specify the context in which the accident/incident occurs. Next, the event characteristics describe the important features pertaining to the accident/incident, including the severity of the aircraft equipment problem (less severe or critical), the type of the event (illness, smoke, fire, procedural deviation, or airspace violation), whether passengers were involved in the event, the detecting person, as well as the time when event is detected (routine inspection, maintenance, or in-flight). The event characteristics enable us to have a better resolution in understanding a variety of aspects of the incident, for example, what is the cause of the event, when it happened, and the severity of the problem. Third, when the pilot or other operator is faced with the problem, they take certain measures to resolve the issue (e.g., flight crew took evasive action, or flight crew executed an emergency landing as precaution). All the event outcomes are displayed in the dashed box in the diagram at the bottom right of Fig. 2.

Considering the dimension of the input variables, we leverage the deep neural network (DNN, also referred to as deep learning) to learn the associations between the contextual features and event outcomes. Over the last five years, DNN has been proven to be very good at discovering intricate structures in high-dimensional data [52, 53], and has dramatically improved the performance of the state-of-the-art in image classification [54], speech recognition [55], and natural language understanding [56]. The key advantage of deep learning over the classical learning algorithms is that it is able to learn appropriate representations from the raw data with multiple levels of abstraction in an automatic manner that are needed for detection or classification. Typically, conventional machine learning algorithms require manually designed rigorous feature extractor to elicit informative features from raw data (e.g., image) that usually needs careful engineering and a considerable amount of domain expertise, from which the classifier is able to learn and diferentiate patterns revealed in the extracted features. Whereas, deep learning is able to extract features embodied in massive raw data with multiple levels of representation (e.g., orientation, location, motifs, and their combinations in images) from the training data automatically. As a result, it frees us from the design of a hand-engineered feature extractor to transform the raw data into a suitable representation or feature vector. Since deep learning requires very little engineering by hand, it can be updated by additional collection of abnormal event records in the ASRS database. Leveraging the powerful capabilities of deep learning, we have developed an ensemble of feed-forward deep neural networks in which each network consists of two hidden layers with each hidden layer having 24 and 12 neurons. The construction and performance of the ensemble of deep neural networks will be discussed in the next section.

## 3.3. Model Fusion

As described above, we develop two models: one for the unstructured data, and the other one for the structured data. How to fuse the prediction results of the two trained models is the next challenge. Many approaches have been developed to address this issue, including majority voting schemes (unanimous voting, simple majority, and majority voting), weighted sum, and support function fusion based on the ranking of each predicted class in terms of the estimated likelihood in each individual classifier [57]. Several challenges arise when we attempt to fuse the predictions from the two models by using these strategies. First of all, since there are only two models here, majority voting is not possible when the two models have diferent predictions. Secondly, as there are five classes in the risk-based event outcome categorization, weighted sum is inappropriate to be implemented in this circumstance. For example, suppose the support vector machine and the deep neural network ensemble have 60% and 80% overall prediction accuracy, respectively. Now they are given a new test record (not used in training), and suppose the predictions from the SVM and DNN models are classes 1 and 5, respectively. In this case, the model prediction after we perform a simple weighted sum operation will be $\textstyle { \frac { 0 . 6 } { 0 . 6 + 0 . 8 } } \times 1 + { \frac { 0 . 8 } { 0 . 6 + 0 . 8 } } \times 5 = 3 . 2 8$ , which does not make any sense. Note also that the fused prediction result needs to be an integer. Even if we take certain operations (e.g., rounding, flooring) to transform the decimal into an integer, the model prediction (3) after the transformation might be the least probable prediction in the two models. Consequently, the weighted sum operation is inappropriate to be implemented in this problem.

![](/api/attachments/E2W3EXCA/fulltext/images/eb3a10f268f29c6b17f0d4243abf72ffede015fd8e261b354665214ffb67975c.jpg)  
Figure 4: Proposed fusion rule to integrate the two models.

We develop a probabilistic fusion rule to blend the predictions from the two models. The framework of the proposed fusion rule is demonstrated in Fig. 4. In the first place, if the two models have the same prediction (prediction 1 = prediction 2), then the prediction result is easy to be determined. If the two models have diferent predictions, then we calculate the probability of the test record belonging to each class among the five risk categories in each model. To illustrate the proposed method, Table 4 reports the performance metrics of the two models on a validation dataset. The validation dataset consists of $N _ { 1 } , N _ { 2 }$ 2 $N _ { 3 } , N _ { 4 }$ , and $N _ { 5 }$ records in the five respective classes, where $A _ { i , j } ^ { s }$ and $A _ { i , j } ^ { d }$ represents the number of records that actually belong to class i but are labelled as class j in the support vector machine and DNN ensemble, respectively. The third to the seventh columns present the confusion matrix of the trained support vector machine on the validation dataset, while the confusion matrix of the deep learning ensemble is reported

# ACCEPTED MANUSCRIPT

in the thirteenth to seventeenth column. The ninth column of Table 4 reports the number of consistent predictions between the two trained models on the validation dataset, while the tenth column reports the accuracy of the correctly labeled records among the consistent predictions of the two models in the validation dataset.

When the two models have disagreeing predictions, one important underlying mechanism when devel oping the fusion strategy is: since no model is perfect, each model is expected to have misclassifications or make erroneous predictions. However, the valuable information embodied in the misclassifications should be further utilized to correct the model predictions on the subsequent unseen test dataset in a way that makes up the class that the observation should belong to if we know how often the model mislabels the class as other classes. Considering the various types of misclassifications that the trained model is prone to make, one way to achieve this objective is to increase the probability of labeling the observation as the correct class, while reducing the probability of labeling the record as the predicted class given by the model. Fortunately, such information can be derived from the confusion matrix. In fact, a confusion matrix not only provides class-level model prediction accuracy, but also the probability of mislabeling a record as other classes. Next, we will utilize the model misclassification probability to correct the mode prediction on new test records. Suppose the two models have diferent predictions on a new test record a; there are three important considerations in determining the probability of the new test record a belonging to each of the five classes i in the two models:

1. Record-level prediction probabilities: As mentioned earlier, two models have been trained: support vector machine and a deep neural network ensemble. The record-level probability $p ( \widehat { Y } _ { a } = i )$ measures the probability that the trained model assigns the test record a to a given class i. To be specific, with respect to the DNN ensemble, the record-level prediction probabilities can be measured as the ratio of the most frequent prediction to the total number of model predictions (which is 10, in this case). For example, if the most frequent prediction of the ten models is class 5, and it appears six times out of the ten model predictions, then the model prediction probability for this particular record belonging to class 5 is $6 / 1 0$ (0.6). Regarding the support vector machine, since samples far away from the separating hyperplane are presumably more likely to be classified correctly, we can use the distance from the hyperplane as a measure of record-level prediction probability following the method introduced in Ref. [58].

2. Proportion of each class in the records with disagreeing predictions: When the two models are trained, there are the same number of records belonging to each class in the training dataset. In other words, the data is balanced for each class in the training dataset. However, when we use the trained models to make predictions on test records, we only need decisions when the two trained models have inconsistent predictions. With respect to the set of disagreeing predictions, the actual proportion of records belonging to each class might be diferent (imbalanced) from the training dataset (balanced). The use of the model trained by the balanced class distribution will result in a biased estimator if it is directly utilized for making predictions on the set of records with inconsistent model predictions.

To address this issue, we introduce a weight factor to correct the trained model to fit the class distribution in the set of records with disagreeing model predictions, thereby ensuring that the updated estimator is unbiased. The number of records with consistent model predictions in each class is complementary to the amount of records with inconsistent model predictions in that class. In general, the more records the two classifiers agree on, the less the number of records the two classifiers disagree on. As a result, we formulate the following equation to represent the total number of records with inconsistent model predictions across all the classes considered:

$$
T = \sum_ {i = 1} ^ {5} (N _ {i} - \lambda_ {i} \times N _ {i} ^ {c})\tag{2}
$$

where i is the class label, $N _ { i }$ denotes the actual number of records that should have been labeled as class i, $N _ { i } ^ { c }$ represents the number of consistent predictions between the two models on all the records, and $\lambda _ { i }$ is the model accuracy with respect to the consistent predictions.

Considering the total number of disagreeing predictions across all the classes, the proportion w.r.t. class j is:

$$
p (j) = \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{T}\tag{3}
$$

Given the already correctly labeled samples by the two trained models, the probability of a new test record a that results in disagreeing predictions between the two models belonging to class j is $p \left( j \right)$

3. Class-level accuracy: This measures the degree of consistency between model predictions and actual observations. Mathematically, it can be represented as: $p \left( { Y = i } | { \widehat { Y } } = j \right)$ , where ${ \widehat { \pmb Y } } = j$ represents the samples with model predictions being class $j ,$ and $p \left( \mathbf { Y } = i | \widehat { \mathbf { Y } } = j \right) ( j \neq i )$ quantifies the proportion of samples with model predictions being class j that should have been labeled as class i. In particular, when j = i, then $p \left( { Y = i } | { \widehat { Y } } = i \right)$ measures the ratio of samples actually belonging to class i to the number of samples with model predictions being class $i ,$ which can also be referred to as a likelihood function. In other words, the likelihood function measures the probability of observing the data given the prediction. Such a quantitative metric $p \left( { Y = i } | { \widehat { Y } } = i \right)$ measures the accuracy of the trained model in making predictions with respect to class i.

If we only consider the special case $( i = j )$ , then the Bayes factor (or likelihood ratio) can be used to help decide which model supports our observation better from the two trained models, thereby assisting the model selection [59]. However, the Bayes factor does not consider the information embodied in the model misclassifications. Therefore, we propose an equation below to handle all the possible situations existing in the five-class classification problem by utilizing the information contained in the term $p \left( { Y = i } | { \widehat { Y } } = j \right)$ . The quantitative metric $p \left( { Y = i } | { \widehat { Y } } = j \right)$ is equivalent to the confusion matrix used in the performance evaluation on the validation dataset. By utilizing the metric $p \left( { Y = i } | { \widehat { Y } = j } \right)$ , we relate the model predictions to the actual observations, from which we compute the probability of a test record a actually belonging to a given class i in the subsequent sections.

For a given new test record $^ { a , }$ the proposed fusion rule based on the above three considerations is:

$$
p \left(Y _ {a} = i\right) = \sum_ {j = 1} ^ {5} \left[ p (\mathbf {Y} = \mathbf {i} | \widehat {\mathbf {Y}} = \mathbf {j}) p (\widehat {Y} _ {a} = j) \times \frac {p (j)}{\widetilde {p} (j)} \right]\tag{4}
$$

where $p \left( \mathbf { Y } = i | \widehat { \mathbf { Y } } = j \right) ( j \neq i )$ is the model misclassification rate, in which the model prediction is class $j$ while the actual observation is class $i ;$ when $j = i$ , then $p \left( { Y = i | \widehat { Y } = i } \right)$ denotes the model prediction precision with respect to class $i , p \left( j \right)$ is the proportion of class j in the set of inconsistent model predictions, $\widetilde { p } ( j )$ represents the proportion of class j in the training dataset, and $j$ $p \left( \widehat { Y } _ { a } = j \right)$ represents the confidence of the model in classifying the test record a as class $j$ .

By substituting Eq. (3) into Eq. (4), we have:

$$
p \left(Y _ {a} = i\right) = \sum_ {j = 1} ^ {5} \left[ p \left(\mathbf {Y} = \mathbf {i} | \widehat {\mathbf {Y}} = \mathbf {j}\right) p \left(\widehat {Y} _ {a} = j\right) \times \frac {1}{\widetilde {p} (j)} \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{T} \right]\tag{5}
$$

Since all the five classes are evenly distributed in the training dataset, $\widetilde { p } ( j )$ is a constant, which can be ignored, then we have:

$$
p \left(Y _ {a} = i\right) \propto \sum_ {j = 1} ^ {5} \left[ p (\mathbf {Y} = \mathbf {i} | \widehat {\mathbf {Y}} = \mathbf {j}) p (\widehat {Y} _ {a} = j) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{T} \right]\tag{6}
$$

Next, we perform the normalization operation following Eq. (7) such that the sum of the probability over the five classes in each model is 1.

$$
p \left(Y _ {a} = i\right) = \frac {\sum_ {j = 1} ^ {5} \left[ p (\mathbf {Y} = i | \widehat {\mathbf {Y}} = \mathbf {j}) p (\widehat {Y} _ {a} = j) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{T} \right]}{\sum_ {i = 1} ^ {5} \sum_ {j = 1} ^ {5} \left[ p (\mathbf {Y} = \mathbf {i} | \widehat {\mathbf {Y}} = \mathbf {j}) p (\widehat {Y} _ {a} = j) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{T} \right]}\tag{7}
$$

With respect to the support vector machine, the likelihood function $p \left( { Y = i } | { \widehat { Y } } = j \right)$ is calculated as:

$$
p \left(\boldsymbol {Y} = \boldsymbol {i} | \widehat {\boldsymbol {Y}} ^ {s} = \boldsymbol {j}\right) = \frac {A _ {i , j} ^ {s}}{\sum_ {i = 1} ^ {5} A _ {i , j} ^ {s}}\tag{8}
$$

where $A _ { i , j } ^ { s }$ denotes the number of samples with model predictions being class $j ,$ , but actually belonging to class i in the validation dataset.

<sub>records</sub> <sub>in</sub> <sub>the</sub> <sub>consistent</sub> m<sup>odel</sup> <sup>predictions</sup> <sup>that</sup> <sup>are</sup> <sup>cor</sup> <sub>represents</sub> <sub>the</sub> <sub>number</sub> <sub>of</sub> <sub>consistent</sub> <sub>predic</sub><sup>tions</sup> <sup>between</sup> <sup>the</sup> <sup>two</sup> <sup>models</sup> <sup>for</sup> <sup>each</sup> <sup>class,</sup> <sup>and</sup> <sup>consistent</sup> <sup>pred</sup> <sub>cs</sub> <sub>for</sub> <sub>the</sub> <sub>two</sub> <sub>trained</sub> <sub>models</sub>. <sub>Here,</sub> <sub>the</sub> <sub>support</sub> <sub>colu</sub>m<sup>n</sup> <sup>denotes</sup> <sup>the</sup> <sup>number</sup> <sup>of</sup> <sup>occurrences</sup> <sup>of</sup> <sup>each</sup> <sup>class</sup> <sup>in</sup>

<table><tr><td colspan="7">Support Vector Machine</td><td colspan="3">Shared Attributes</td><td colspan="7">Deep Learning Ensemble</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="5">Predicted Label</td><td rowspan="2">Support</td><td rowspan="2">Consistent Prediction</td><td rowspan="2">Consistent Prediction Accuracy</td><td rowspan="2"></td><td></td><td colspan="5">Predicted Label</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="5">True Label</td><td>1</td><td> $A_{1,1}^{s}$ </td><td> $A_{1,2}^{s}$ </td><td> $A_{1,3}^{s}$ </td><td> $A_{1,4}^{s}$ </td><td> $A_{1,5}^{s}$ </td><td> $N_1$ </td><td> $N_1^c$ </td><td> $λ_1$ </td><td rowspan="5">True Label</td><td>1</td><td> $A_{1,1}^{d}$ </td><td> $A_{1,2}^{d}$ </td><td> $A_{1,3}^{d}$ </td><td> $A_{1,4}^{d}$ </td><td> $A_{1,5}^{d}$ </td></tr><tr><td>2</td><td> $A_{2,1}^{s}$ </td><td> $A_{2,2}^{s}$ </td><td> $A_{2,3}^{s}$ </td><td> $A_{2,4}^{s}$ </td><td> $A_{2,5}^{s}$ </td><td> $N_2$ </td><td> $N_2^c$ </td><td> $λ_2$ </td><td>2</td><td> $A_{2,1}^{d}$ </td><td> $A_{2,2}^{d}$ </td><td> $A_{2,3}^{d}$ </td><td> $A_{2,4}^{d}$ </td><td> $A_{2,5}^{d}$ </td></tr><tr><td>3</td><td> $A_{3,1}^{s}$ </td><td> $A_{3,2}^{s}$ </td><td> $A_{3,3}^{s}$ </td><td> $A_{3,4}^{s}$ </td><td> $A_{3,5}^{s}$ </td><td> $N_3$ </td><td> $N_3^c$ </td><td> $λ_3$ </td><td>3</td><td> $A_{3,1}^{d}$ </td><td> $A_{3,2}^{d}$ </td><td> $A_{3,3}^{d}$ </td><td> $A_{3,4}^{d}$ </td><td> $A_{3,5}^{d}$ </td></tr><tr><td>4</td><td> $A_{4,1}^{s}$ </td><td> $A_{4,2}^{s}$ </td><td> $A_{4,3}^{s}$ </td><td> $A_{4,4}^{s}$ </td><td> $A_{4,5}^{s}$ </td><td> $N_4$ </td><td> $N_4^c$ </td><td> $λ_4$ </td><td>4</td><td> $A_{4,1}^{d}$ </td><td> $A_{4,2}^{d}$ </td><td> $A_{4,3}^{d}$ </td><td> $A_{4,4}^{d}$ </td><td> $A_{4,5}^{d}$ </td></tr><tr><td>5</td><td> $A_{5,1}^{s}$ </td><td> $A_{5,2}^{s}$ </td><td> $A_{5,3}^{s}$ </td><td> $A_{5,4}^{s}$ </td><td> $A_{5,5}^{s}$ </td><td> $N_5$ </td><td> $N_5^c$ </td><td> $λ_5$ </td><td>5</td><td> $A_{5,1}^{d}$ </td><td> $A_{5,2}^{d}$ </td><td> $A_{5,3}^{d}$ </td><td> $A_{5,4}^{d}$ </td><td> $A_{5,5}^{d}$ </td></tr></table>

In a similar way, the metric $p \left( { Y = i } | { \widehat { Y } = j } \right)$ in the DNN ensemble is computed accordingly. Given the model classification performance $p \left( { Y = i } | { \widehat { Y } } = j \right)$ , the probability of test record a belonging to each class in each model is computed as below:

$$
\begin{array}{r l} & p \left(Y _ {a} ^ {s} = i\right) \propto \sum_ {j = 1} ^ {5} \left[ p \left(\mathbf {Y} = \mathbf {i} | \widehat {\mathbf {Y}} ^ {s} = \mathbf {j}\right) \times p \left(\widehat {Y} _ {a} ^ {s} = j\right) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{\sum_ {k = 1} ^ {5} \left(N _ {k} - \lambda_ {k} \times N _ {k} ^ {c}\right)} \right] \\ & \quad \propto \sum_ {j = 1} ^ {5} \left[ \frac {A _ {i , j} ^ {s}}{\sum_ {i = 1} ^ {5} A _ {i , j} ^ {s}} \times p \left(\widehat {Y} _ {a} ^ {s} = j\right) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{\sum_ {k = 1} ^ {5} \left(N _ {k} - \lambda_ {k} \times N _ {k} ^ {c}\right)} \right] \\ & p \left(Y _ {a} ^ {d} = i\right) \propto \sum_ {j = 1} ^ {5} \left[ p \left(\mathbf {Y} = \mathbf {i} | \widehat {\mathbf {Y}} ^ {\mathbf {d}} = \mathbf {j}\right) \times p \left(\widehat {Y} _ {a} ^ {d} = j\right) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{\sum_ {k = 1} ^ {5} \left(N _ {k} - \lambda_ {k} \times N _ {k} ^ {c}\right)} \right] \\ & \quad \propto \sum_ {j = 1} ^ {5} \left\lbrack \frac {A _ {i , j} ^ {d}}{\sum_ {i = 1} ^ {5} A _ {i , j} ^ {d}} \times p \left(\widehat {Y} _ {a} ^ {d} = j\right) \times \frac {N _ {j} - \lambda_ {j} \times N _ {j} ^ {c}}{\sum_ {k = 1} ^ {5} \left(N _ {k} - \lambda_ {k} \times N _ {k} ^ {c}\right)} \right] \end{array}\tag{9}
$$

where $p \left( Y _ { a } ^ { s } = i \right)$ and $p \left( Y _ { a } ^ { d } = i \right)$ represent the probability of support vector machine and deep learning models in labeling the test record as class $i ,$ the term $\frac { N _ { j } - \lambda _ { j } \times N _ { j } ^ { c } } { \displaystyle { \sum _ { k = 1 } ^ { 5 } } N _ { k } - \lambda _ { k } \times N _ { k } ^ { c } }$ in Eq. (9) denotes the proportion of records belonging to class $j$ in the set of inconsistent model predictions; the terms $A _ { i , j } ^ { s }$ and $A _ { i , j } ^ { d }$ represent the samples belonging to class i but labeled as class j in the two respective models, and $p \left( \widehat { Y } _ { a } ^ { s } = j \right)$ and $p \left( \widehat { Y } _ { a } ^ { d } = j \right)$ are the prediction confidence of the two respective models to classify the test record a as class $j$

After normalizing the probability of the test record a belonging to each class in each model, we select the predicted class with the maximum probability from the two models as the hybrid model prediction. By considering the three factors, the proposed method successfully adjusts the trained model to suit the classification with respect to the records within the inconsistent model predictions. After we obtain the probability of the test record belonging to each class in each model, then we assign the test record to the class with the maximum probability.

## 3.4. Event-level Outcome Analysis

After the risk-level category that the test record should belong to is probabilistically determined, then event-level outcome can be derived by measuring the event synopsis similarity between the test record a and other records belonging to the same risk category. One popular way to measure document similarity is based on the content overlap between two documents [60] as represented in Eq. (10).

$$
\mathrm{sim} \left(d _ {i}, d _ {j}\right) = \frac {\sum_ {m = 1} ^ {k} w _ {m , i} \times w _ {m , j}}{\sqrt {\sum_ {m = 1} ^ {k} \left(w _ {m , i}\right) ^ {2}} \times \sqrt {\sum_ {m = 1} ^ {k} \left(w _ {m , j}\right) ^ {2}}}\tag{10}
$$

where $d _ { i }$ and $d _ { j }$ denote two documents, $w _ { m , i } \left( w _ { m , j } \right)$ is the frequency of object (words, or terms) $o _ { m }$ present in document $d _ { i } \ ( d _ { j } )$ , and k is the number of unique objects across all the documents.

The similarity metric defined in $\operatorname { E q . }$ (10) measures the cosine of the angle between vector-based representations of the two documents. Since there are multiple documents belonging to the same risk category as the test record a, we formulate the following equation to address such issues:

$$
p \left(e = k | Y _ {a} = j\right) = \frac {1}{c _ {k}} \sum_ {v = 1} ^ {c _ {k}} \mathrm{sim} \left(d _ {a}, d _ {I (v)}\right)\tag{11}
$$

where $c _ { k }$ denotes the number of records having event outcome k in the training dataset, and I(v) denotes the index of the v-th record having event outcome k in the training dataset.

Afterwards, a normalization operation can be performed by taking into account all the possible event outcomes in the j-th risk category.

$$
p \left(e = k \mid Y _ {a} = j\right) = \frac {p \left(e = k \mid Y _ {a} = j\right)}{\sum_ {k = 1} ^ {K} p \left(e = k \mid Y _ {a} = j\right)}\tag{12}
$$

where K represents the number of possible event consequences in the j-th risk category.

By considering the event outcomes in the corresponding risk category, a decision tree can be constructed to demonstrate the probability of each event to occur. In this way, the risk-level category can be mapped to event-level outcome.

## 3.5. Summary

The methodology developed in this section tackles the problem of risk quantification regarding the consequences of abnormal events in the national airspace system with a four-step procedure (see Fig. 2):

1. We reorganize all the incidents/accidents based on the risk associated with the consequence of each hazardous event. The risk-based event outcome categorization enables us to collapse the original 36 unique event outcomes into five groups, and project the event outcome to the dimension of risk quantification in the representation of five risk groups: high risk, moderately high risk, medium risk, moderately medium risk, and low risk. Considering the five risk groups, up-sampling is performed to balance the number of records between minority classes and majority classes.

2. Two models are developed to process the structured data and unstructured data, respectively. To handle the structured data in high dimension, an ensemble of deep neural networks are trained to associate the event contextual features with the event outcomes. A support vector machine model is used to discover the relationships between event synopsis and event consequence.

3. A probabilistic fusion decision rule is developed to blend the predictions by the two machine learning models. When the prediction results are inconsistent, a quantitative metric is proposed to compute the likelihood that the test record belongs to each predicted class, from which we can determine the class the test record should be assigned to.

4. Once the test record is assigned to a specific risk category, we map the risk-level category to eventlevel outcomes through a probabilistic tree, in which all the possible event outcomes in the corresponding risk category are considered.

## 4. Numerical Results

Table 5: The number of records belonging to each risk category

<table><tr><td>Class</td><td>High</td><td>Moderately high</td><td>Medium</td><td>Moderately medium</td><td>Low</td></tr><tr><td>Number of records</td><td>12327</td><td>8261</td><td>18841</td><td>8636</td><td>16508</td></tr></table>

## 4.1. Data Description

We collected 12 years of incident reports (from January 2006 to December 2017) from ASRS, thus obtaining 64,573 records. The number of records belonging to each risk class is shown in Table 5. To address the imbalance, we up-sample the three minority classes (high, moderately high, and moderately medium) with replacement to get the same amount of data as in the majority class to form a balanced dataset. After up-sampling, the dataset contains 18,841 records for the high, moderately high, medium, and moderately medium risk classes respectively, and 16,508 number of records in the low risk category. After the up-sampling operation, there are 91,872 number of records in total.

![](/api/attachments/E2W3EXCA/fulltext/images/b7897e908dd92addb29efc5c17255b200c6ff82f7ea0a696f332b42ef44df944.jpg)  
Figure 5: Datasets and model inputs.

All the input variables are summarized in Fig. 5, and they are grouped into two categories: unstructured data and structured data. The structured data includes 29 diferent variables ranging from aircraft information to event characteristics, while the unstructured (text) data only includes event synopsis. With the 29 structured variables and one unstructured variable, we train the SVM and DNN models.

Table 6: Confusion matrix

<table><tr><td></td><td>Predicted as positive</td><td>Predicted as negative</td></tr><tr><td>Actually positive</td><td>True Positives (TP)</td><td>False Negative (FN)</td></tr><tr><td>Actually negative</td><td>False Positives (FP)</td><td>True Negative (TN)</td></tr></table>

Given a trained classifier and a test dataset, the relationship between model predictions and true observations can be represented as a confusion matrix, as illustrated in Table 6. To assess the performance of every machine learning model, we adopt three most commonly used performance metrics.

1. Precision: Mathematically, Precision $\left( { \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F P } } } \right)$ is the ratio of correctly predicted positive observations to the total predicted positive observations, and high precision typically corresponds to low false positive predictions.

2. Recall: Recall is defined as Recall $\displaystyle \bigl ( \frac { \mathrm { T P } } { \mathrm { T P } + \mathrm { F N } } \bigr )$ quantifies the ratio of correctly labeled positive observations to all the positive observations in the actual class. It measures the ability of the trained model in identifying positive observations from all the samples that should have been labeled as positive.

3. The F1 score is the weighted average of precision and recall, which is mathematically described as F1 = 2 × precision+recall precision∗recall . In the F1 score, the relative contribution of precision and recall is the same. In other words, the F1-measure is the harmonic mean of precision and recall.

## 4.2. Experimental Analysis

We split the 91,872 records into three parts: training set (85%), validation set (5%), and test set (10%). The training set is used to guide the machine learning algorithms to optimize the relevant parameters so as to minimize prediction error; the validation set is utilized to develop the performance metrics for an unseen dataset (i.e., prediction accuracy). With the performance metrics obtained from the validation dataset, we then blend the predictions from the two trained models for the test dataset.

Regarding the SVM estimator for text classification, we leverage grid search to optimize the relevant hyperparameters. Specifically, we optimize the loss function (hinge, log, perceptron, squared loss, etc.), the regularization function (l1, l2, or elasticnet), the coeficient of regularization function $( \left[ 1 0 ^ { - 2 } , 1 0 ^ { - 5 } \right] )$ ), and the range of N-gram (N-gram is a contiguous sequence of n items from a given sample of text). The grid search exhaustively generates candidates from the set of parameter values, and evaluates all the possible combinations of parameter values on the training dataset and selects the best combination. After the optimal hyperparameters are identified, we run the trained support vector machine algorithm

# ACCEPTED MANUSCRIPT

on the validation data to obtain its performance metrics. The left part of Table 7 reports the performance metrics of the trained support vector machine model on the validation dataset.

In the DNN model, all the categorical features are encoded using one hot encoding. We randomly select 85% records from the training dataset to train a deep neural network, then we repeat the same procedure ten times to obtain an ensemble of deep neural networks. Every DNN has the same structure – 8 hidden layers and 40 neurons per layer. We choose an Adam Optimizer [61] with a learning rate of 0.001 to perform backward propagation in adjusting the weight variables with the objective of minimizing the categorical cross entropy as defined in Eq. (13).

$$
L \left(\mathbf {Y}, \widehat {\mathbf {Y}} ^ {d}\right) = - \frac {1}{n} \sum_ {i = 1} ^ {n} \left[ Y _ {i} \log \widehat {Y} _ {i} ^ {d} \right]\tag{13}
$$

where n is the number of training samples, Y<sub>i</sub> is a one-hot-encoding representation of the actual observation with the corresponding class label being 1 and the values of other classes being zero, and $\widehat { Y } _ { i } ^ { d }$ is the probabilistic estimation of ensemble deep learning models on the record i.

After the ten deep neural networks are trained, we use them to make predictions on the validation dataset, and the results are reported in Table 7. It is observed that the DNN ensemble does not perform as well as the SVM model in terms of precision and recall for classes 2, 3, and 5 due to the low level of information contained in the categorical features. As shown in the ninth column of Table 7, the two trained models agree on 491, 988, 448, 936, and 961 predictions with respect to the five classes. Among the consistent predictions of the two models, 401, 922, 339, 897, and 804 predictions with respect to the five classes are correctly classified, from which we can compute the ratio of consistent predictions that are correctly labeled in the validation dataset. Next, we utilize the two trained models to make predictions on the test dataset. With the performance metrics acquired on the validation dataset, we blend the predictions of the two models. Suppose the two models have probabilistic classifications on the test record a as shown in Table 8; each cell represents the probability that the test example a is a member of the class. Regarding the test record a, the SVM model supports class 5 the most, whereas the DNN ensemble assigns the highest probability to class 2.

Following the method introduced before, the total number of inconsistent model predictions is $T =$ $( 9 4 7 - 4 0 1 ) + ( 1 0 1 7 - 9 2 2 ) + ( 9 8 8 - 3 3 9 ) + ( 1 0 3 4 - 8 9 7 ) + ( 9 7 6 - 8 0 4 ) = 1 5 9 9$ . Then the proportion of each class in the disagreeing records is calculated as:

$$
\boldsymbol {p} = \left[ \begin{array}{l l l l l} 0. 3 4 & 0. 0 6 & 0. 4 0 & 0. 0 9 & 0. 1 1 \end{array} \right]
$$

<sub>records</sub> <sub>in</sub> <sub>the</sub> <sub>consistent</sub> m<sup>odel</sup> <sup>predictions</sup> <sup>that</sup> <sup>are</sup> <sup>cor</sup> <sub>represents</sub> <sub>the</sub> <sub>number</sub> <sub>of</sub> <sub>consistent</sub> <sub>predic</sub><sup>tions</sup> <sup>between</sup> <sup>the</sup> <sup>two</sup> <sup>models</sup> <sup>for</sup> <sup>each</sup> <sup>class,</sup> <sup>and</sup> <sup>consistent</sup> <sup>pred</sup> <sub>mn</sub> <sub>denote</sub><sup>s</sup> <sup>the</sup> <sup>number</sup> <sup>of</sup> <sup>occurrences</sup> <sup>of</sup> <sup>each</sup> <sup>class</sup> <sup>in</sup> <sup>the</sup> <sup>actual</sup> <sub>rformance</sub> m<sup>etrics</sup> <sup>for</sup> <sup>the</sup> <sup>two</sup> <sup>trained</sup> <sup>mod</sup>

<table><tr><td colspan="7">Support Vector Machine</td><td colspan="3">Shared Attributes</td><td colspan="7">Deep Neural Networks</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="5">Predicted Label</td><td rowspan="2">Support</td><td rowspan="2">Consistent Prediction</td><td rowspan="2">Consistent Prediction Accuracy</td><td rowspan="2"></td><td></td><td colspan="5">Predicted Label</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td rowspan="5">True Label</td><td>1</td><td>550</td><td>82</td><td>205</td><td>69</td><td>41</td><td>947</td><td>491</td><td>0.82</td><td rowspan="5">True Label</td><td>1</td><td>567</td><td>74</td><td>204</td><td>46</td><td>56</td></tr><tr><td>2</td><td>14</td><td>951</td><td>27</td><td>13</td><td>12</td><td>1017</td><td>988</td><td>0.93</td><td>2</td><td>25</td><td>931</td><td>28</td><td>5</td><td>28</td></tr><tr><td>3</td><td>153</td><td>65</td><td>592</td><td>119</td><td>59</td><td>988</td><td>448</td><td>0.76</td><td>3</td><td>208</td><td>72</td><td>495</td><td>97</td><td>116</td></tr><tr><td>4</td><td>16</td><td>7</td><td>43</td><td>943</td><td>25</td><td>1034</td><td>936</td><td>0.96</td><td>4</td><td>19</td><td>11</td><td>48</td><td>927</td><td>29</td></tr><tr><td>5</td><td>20</td><td>17</td><td>34</td><td>22</td><td>883</td><td>976</td><td>861</td><td>0.93</td><td>5</td><td>38</td><td>27</td><td>45</td><td>28</td><td>838</td></tr></table>

Table 8: Model predictions with respect to test record a

<table><tr><td>Model</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>SVM</td><td>0.10</td><td>0.20</td><td>0.20</td><td>0.20</td><td>0.30</td></tr><tr><td>DNN</td><td>0.20</td><td>0.40</td><td>0.10</td><td>0.02</td><td>0.28</td></tr></table>

Then the probability of assigning the test record a to class 1 in the SVM model is computed as:

$$
\begin{array}{l} p \left(Y _ {a} ^ {s} = 1\right) \propto \sum_ {j = 1} ^ {5} \left[ p (Y = 1 | \widehat {Y} ^ {s} = j) \times p (\widehat {Y} ^ {s} = j) \times p (j) \right] \\ = \frac {5 5 0}{5 5 0 + 1 4 + 1 5 3 + 1 6 + 2 0} \times 0. 1 \times 0. 3 4 + \frac {8 2}{8 2 + 9 5 1 + 6 5 + 7 + 1 7} \times 0. 2 \times 0. 0 6 \\ + \frac {2 0 5}{2 0 5 + 2 7 + 5 9 2 + 4 3 + 3 4} \times 0. 2 \times 0. 4 + \frac {6 9}{6 9 + 1 3 + 1 1 9 + 9 4 3 + 2 2} \times 0. 2 \times 0. 0 9 \\ + \frac {4 1}{4 1 + 1 2 + 5 9 + 2 5 + 8 8 3} \times 0. 3 \times 0. 1 1 \\ = \mathbf {0 . 0 4 6 8} \end{array}
$$

In a similar way, the probabilities of labeling the test record a as other classes in the SVM model is calculated:

$$
\begin{array}{r} p (Y _ {a} ^ {s} = 2) \propto 0. 0 1 3 7, p (Y _ {a} ^ {s} = 3) \propto 0. 0 6 4 6 \\ p (Y _ {a} ^ {s} = 4) \propto 0. 0 1 9 3, p (Y _ {a} ^ {s} = 5) \propto 0. 0 3 2 4 \end{array}
$$

After normalization, the probability of the test record belonging to each class in the SVM model is:

$$
\begin{array}{l} {p (Y _ {a} ^ {s} = 1) = 0. 2 6, p (Y _ {a} ^ {s} = 2) = 0. 0 8, p (Y _ {a} ^ {s} = 3) = 0. 3 7,} \\ {p (Y _ {a} ^ {s} = 4) = 0. 1 1, p (Y _ {a} ^ {s} = 5) = 0. 1 8.} \end{array}
$$

Likewise, with the DNN ensemble, the probabilities of the test record a belonging to class 1 to 5 are calculated as:

$$
\begin{array}{l} p \left(Y _ {a} ^ {d} = 1\right) = 0. 3 5, p \left(Y _ {a} ^ {d} = 2\right) = 0. 1 5, p \left(Y _ {a} ^ {d} = 3\right) = 0. 2 8, \\ p \left(Y _ {a} ^ {d} = 4\right) = 0. 0 4, p \left(Y _ {a} ^ {d} = 5\right) = 0. 1 8. \end{array}
$$

From the above computational results, test record a has the highest probability (0.37) of being labeled as class 3 in the SVM model. As a result, this test record a is assigned to class 3 in the hybrid model. For the remaining test records, we blend the two model predictions in a similar manner.

To compare the performance of all the investigated models, we randomly split the original dataset into ten equal sized groups to perform ten-fold cross-validation. The procedure presented in Algorithm 1 is repeated over the ten equal sized groups. Fig. 6 shows the proportions of five risk categories in the records with disagreeing predictions. Among the five risk categories, the medium risk class has the largest proportion of records with disagreeing predictions, followed by low risk and high risk classes. The proportion of each class with disagreeing prediction is relatively stable with a small variability. Due to the imbalanced class distribution in the records with disagreeing predictions, the adjustment factor introduced in Eq. (4) plays an essential role in embodying such information in the subsequent hybrid model predictions.

![](/api/attachments/E2W3EXCA/fulltext/images/f05b8e0a43cd9d3c6dd599da8324617cf559800b859e27aa7eb8342651a8d682.jpg)  
Figure 6: Proportion of each class in the records with disagreeing predictions

In addition, we implement ordinal logistic regression (OLR) for the purpose of comparing its performance with the DNN ensemble on the structured data [62, 63]. The computational result of ten-fold cross-validation for the four models is demonstrated as a boxplot in Fig. 7. It is worth noting that we shift the values of the three performance indicators of ordinal logistic regression by +0.4 for the sake of demonstrating the four models’ performance deviation clearly. As can be observed, the hybrid mode outperforms SVM, DNN ensemble, and OLR in terms of precision, recall and F1 score. More importantly, the hybrid model has a much smaller deviation for all the performance metrics when compared to all the other three models. In other words, it has the most stable prediction capability, thereby making it the best candidate for quantifying the risk of abnormal events. Since OLR is inferior to the other three models, we do not analyze its performance any further. From a quantitative viewpoint, based on the cross-validation results, the proposed hybrid model yields a better performance in precision, with an average score of 0.81, 3% higher than the scores of SVM and 6% higher than DNN ensemble models. The proposed hybrid model also outperforms the other two models regarding the recall rate. In other words, the hybrid model has a better performance in correctly identifying the records that actually belong to each class. Besides, the F1 score of the hybrid model is 3% higher than the support vector machine and 6% higher than deep neural networks on average. Regarding the predictions on the structured data, ordinal logistic regression performs much worse than deep learning ensemble. In summary, the proposed decision rule to fuse the predictions from the two models is efective in enhancing the hybrid model performance.

In addition to the boxplot illustrated in Fig 7, statistical t-test is also used to check whether there is a significant diference in the prediction performance of the four models [64]. Specifically, we make a null hypothesis that the means of population from hybrid model and any other individual model are the same, and rejection of this hypothesis indicates that there is suficient evidence that the means of the populations are significantly diferent, while failing to reject this hypothesis reveals that the distributions are identical. The t-test rejected the null hypothesis for all three aforementioned performance indicators, thus implying that there is a statistically significant improvement in the performance of the hybrid model compared to the SVM, DNN ensemble and OLR models.

![](/api/attachments/E2W3EXCA/fulltext/images/87f3fb823bf9e10b656b7806ee5c4c5e55a9eac03676d71e8ccebc75c31ac054.jpg)

![](/api/attachments/E2W3EXCA/fulltext/images/c4009d2d8081660df6e749620a5939bbb384cc4e4dd7230b2fd3e20d7cf39216.jpg)

![](/api/attachments/E2W3EXCA/fulltext/images/b32f02d3c575d1b60449966edefac31b1aeab27872d409aa61ed8a148f119ecf.jpg)  
Figure 7: The performance of hybrid model versus support vector machine (SVM), ensemble of deep neural networks (DNN), and ordinal logistic regression (OLR)

![](/api/attachments/E2W3EXCA/fulltext/images/b25d9d13e2951d1e8d046a611b8fdfc066b818914a7a700b0702e2acfb085b0e.jpg)  
(a)

![](/api/attachments/E2W3EXCA/fulltext/images/c601d06cbfed49fdcac6cf47d96f9eb33a8389f77cf6743188c1e535a7d56495.jpg)  
(b)

![](/api/attachments/E2W3EXCA/fulltext/images/e48ad050e156171f3747b919075ab3ea025dab092fdc1e55f4d4360dc77801af.jpg)  
(c)  
Figure 8: Confusion matrix. (a) the hybrid method, (b) support vector machine, (c) deep neural networks. The entry in the i-th row and j-th column corresponds to the percentage of samples from class i that were classified as class j. 1: low, 2: moderately medium, 3: medium, 4: moderately high, 5: high.

Fig. 8 shows the confusion matrices of the three trained models for the five considered classes in one test case. It can be observed that the hybrid method significantly increases the number of correct predictions for class 1 and class 3, while maintaining the prediction accuracy for the remaining three classes almost at the same level as the other two algorithms. The confusion matrices in Fig. 8 provide comprehensive information in terms of the number of correctly identified observations in each class. Across the five risk groups, the hybrid model correctly identifies 200 more observations than the SVM model. Besides, confusion matrices also embody the misclassification information. As illustrated in Fig. 8, it is most probable for all the three models to misclassify the records in class 1 as class 3, and vice versa. Such information can be utilized to guide the further refinement of the hybrid model.

Table 9: Event synopsis of test record a

<table><tr><td>Date</td><td>Event Synopsis</td></tr><tr><td>March, 2017</td><td>After initiating descent on a visual approach with glideslope out of service; an A319 Flight Crew initiated a go-around when flight director caused airspeed increase and climb to intercept altitude set for ILS to previously assigned runway.</td></tr></table>

Considering that the test record a is labeled as class 3 (medium risk), and the event synopsis of the test record a is shown in Table 9, then a tree is built to demonstrate the likelihood of the occurrence of every event outcome in the medium risk category. By measuring the similarity between the event synopsis of test record a and that of other records in the medium risk category, the probability for test record a having each outcome is obtained, and the result is illustrated in Fig. 9. The red filled node is a chance node used to identify the event in a decision tree where a degree of uncertainty exists. In this case, since the hybrid model does not have the capability to make event-level outcome prediction, we expand the risk-level prediction to event-level outcome prediction by considering all the possible event outcomes under the corresponding risk category. Along each line is shown the probability of each event to occur. As can be seen, it is most probable for the test record a to have event outcome “Flight Crew Executed Go Around Missed Approach”, followed by “Flight Crew Became Reoriented” and “Air Trafic Control Issued New Clearance”. With respect to other risk categories, similar diagrams can be constructed to represent event-level outcomes. Such event-level outcomes enable to connect the root cause (i.e., malfunction) and the consequence of the incident at the event outcome level.

![](/api/attachments/E2W3EXCA/fulltext/images/c0059c05d2f6bbd9eeba18f7bb0ff27983a7a50bb69c877a477aff433b532222.jpg)  
Figure 9: The probabilistic event outcomes for test record a

## 5. Conclusion

This paper developed a hybrid model by blending support vector machine and an ensemble of deep neural networks to quantify the risk pertaining to the consequence of hazardous events in the air transportation system. The SVM model is trained using the event synopsis, while the DNN ensemble is trained using categorical and numerical data. By merging the predictions from the two models, we formulate a hybrid model to assess the severity of abnormal event outcomes in terms of their risk levels using 64,573 reports on incidents/accidents that were reported between January 2006 and December 2017.

Several contributions have been made in this paper. First, we develop a risk-based event outcome categorization strategy to project the event outcomes in the space of risk quantification by collapsing the original 36 unique event outcomes into five risk groups. Secondly, this paper proposes a support vector machine and deep learning-based hybrid model to make prediction on the risk level associated with the event outcome by analyzing the event contextual features and event description in an integrated way. Thirdly, an innovative fusion rule is developed to blend the predictions from the two trained machine learning algorithms. Finally, a probabilistic tree is constructed to map the risk-level prediction to eventlevel outcomes. The results demonstrate that the developed hybrid model outperforms the individua models in terms of precision, recall and F1 score.

Future work can be carried out in the following directions. If the actions taken by the pilot or other operators involved in the response to abnormal events are available, it will be useful to extend the developed hybrid model to account for such important information. The inclusion of such information helps us to identify risk mitigation actions for unforeseen events in the future by learning from the

# ACCEPTED MANUSCRIPT

actions that have been taken in past. Another direction worthy of investigation is to leverage data mining and pattern recognition techniques to discover the intricate event sequences by incorporating more comprehensive reports on severe accidents available in National Transportation Safety Board (NTSB). Since many events interact with each other and tend to exhibit certain patterns, it is helpful to identify such interactions from the available records in ASRS, and characterize them in a rigorous manner. The modeling of such interactions can facilitate our understanding of the evolution of abnormal events, and help to develop corrective strategies. Last but not the least, root cause analysis needs to be performed to identify the major contributing factors and variables that lead to the occurrence of incidents with high risk consequences. Along this direction, appropriate permutation-based significance measures or other alternative methods need to be utilized to recognize the important incident contributing factors. The identification of crucial contributing variables enables risk-informed decision making, thereby aiding the implementation of a proactive safety paradigm in the future.

## Acknowledgement

The research reported in this paper was supported by funds from NASA University Leadership Initiative program (Grant No. NNX17AJ86A, Project Technical Monitor: Dr. Kai Goebel) through subcontract to Arizona State University (Principal Investigator: Dr. Yongming Liu). The support is gratefully acknowledged.

## References

[1] IATA forecasts passenger demand to double over 20 years, http://www.iata.org/pressroom/pr/ Pages/2016-10-18-02.aspx, Accessed: 2017-12-28.

[2] X. Zhang, S. Mahadevan, Aircraft re-routing optimization and performance assessment under uncertainty, Decision Support Systems 96 (2017) 67–82.

[3] The Next Generation Air Transportation System (NextGen), https://www.nasa.gov/sites/default/ files/atoms/files/nextgen whitepaper 06 26 07.pdf, Accessed: 2018-02-08.

[4] P. Fleurquin, J. J. Ramasco, V. M. Eguiluz, Systemic delay propagation in the US airport network, Scientific Reports 3 (2013) 1159.

[5] N. B. Sarter, H. M. Alexander, Error types and related error detection mechanisms in the aviation domain: An analysis of aviation safety reporting system incident reports, The International Journal of Aviation Psychology 10 (2) (2000) 189–206.

[6] I. Hwang, C. E. Seah, Intent-based probabilistic conflict detection for the next generation air transportation system, Proceedings of the IEEE 96 (12) (2008) 2040–2059.

## ACCEPTED MANUSCRIPT

[7] C. Barnhart, D. Fearing, V. Vaze, Modeling passenger travel and delays in the national air transportation system, Operations Research 62 (3) (2014) 580–601.

[8] K. Ng, C. Lee, F. Chan, A robust optimisation approach to the aircraft sequencing and scheduling problem with runway configuration planning, in: Industrial Engineering and Engineering Management (IEEM), 2017 IEEE International Conference on, IEEE, 40–44, 2017.

[9] L. F. Vismari, J. B. C. Junior, A safety assessment methodology applied to CNS/ATM-based air trafic control system, Reliability Engineering & System Safety 96 (7) (2011) 727–738.

[10] F. Netjasov, M. Janic, A review of research on risk and safety modelling in civil aviation, Journal of Air Transport Management 14 (4) (2008) 213–220.

[11] D. McCallie, J. Butts, R. Mills, Security analysis of the ADS-B implementation in the next generation air transportation system, International Journal of Critical Infrastructure Protection 4 (2) (2011) 78– 87.

[12] K. Margellos, J. Lygeros, Toward 4-D trajectory management in air trafic control: A study based on Monte Carlo simulation and reachability analysis, IEEE Transactions on Control Systems Technology 21 (5) (2013) 1820–1833.

[13] S. J. Landry, X. W. Chen, S. Y. Nof, A decision support methodology for dynamic taxiway and runway conflict prevention, Decision Support Systems 55 (1) (2013) 165–174.

[14] C. Di Ciccio, H. Van der Aa, C. Cabanillas, J. Mendling, J. Prescher, Detecting flight trajectory anomalies and predicting diversions in freight transportation, Decision Support Systems 88 (2016) 1–17.

[15] S. Sankararaman, I. Roychoudhury, X. Zhang, K. Goebel, Preliminary Investigation of Impact of Technological Impairment on Trajectory-Based Operations, in: 17th AIAA Aviation Technology, Integration, and Operations Conference, AIAA Aviation Forum, Denver, Colorado, United States, 2017.

[16] H.-J. Shyur, A quantitative model for aviation safety risk assessment, Computers & Industrial Engineering 54 (1) (2008) 34–44.

[17] X. Chen, I. Bose, A. C. M. Leung, C. Guo, Assessing the severity of phishing attacks: A hybrid data mining approach, Decision Support Systems 50 (4) (2011) 662–672.

[18] K. Barker, J. E. Ramirez-Marquez, C. M. Rocco, Resilience-based network component importance measures, Reliability Engineering & System Safety 117 (2013) 89–97.

[19] A. Roelen, R. Wever, A. Hale, L. Goossens, R. Cooke, R. Lopuha¨a, M. Simons, P. Valk, Causal modeling for integrated safety at airports, in: Proceedings of ESREL, 1321–1327, 2003.

[20] D. A. Wiegmann, S. A. Shappell, A human error approach to aviation accident analysis: The human factors analysis and classification system, Routledge, 2017.

[21] K. L. McFadden, E. R. Towell, Aviation human factors: a framework for the new millennium, Journal of Air Transport Management 5 (4) (1999) 177–184.

[22] N. Oza, J. P. Castle, J. Stutz, Classification of aeronautics system health and safety documents, IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 39 (6) (2009) 670–680.

[23] S. Budalakoti, A. N. Srivastava, M. E. Otey, Anomaly detection and diagnosis algorithms for discrete symbol sequences with applications to airline safety, IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews) 39 (1) (2009) 101–113.

[24] ASRS Program Briefing, https://asrs.arc.nasa.gov/docs/ASRS ProgramBriefing2016.pdf, Accessed: 2017-12-28.

[25] Y. Liu, C. Jiang, H. Zhao, Using contextual features and multi-view ensemble learning in product defect identification from online discussion forums, Decision Support Systems 105 (2018) 1–12.

[26] T. Joachims, Text categorization with support vector machines: Learning with many relevant features, in: European Conference on Machine Learning, Springer, 137–142, 1998.

[27] Y. Wang, W. Xu, Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud, Decision Support Systems 105 (2018) 87–95.

[28] F. Wang, T. Xu, T. Tang, M. Zhou, H. Wang, Bilevel feature extraction-based text mining for fault diagnosis of railway systems, IEEE Transactions on Intelligent Transportation Systems 18 (1) (2017) 49–58.

[29] R. Chen, Y. Zheng, W. Xu, M. Liu, J. Wang, Secondhand seller reputation in online markets: A text analytics framework, Decision Support Systems 108 (2018) 96–106.

[30] A. S. Abrahams, W. Fan, G. A. Wang, Z. J. Zhang, J. Jiao, An integrated text analytic framework for product defect discovery, Production and Operations Management 24 (6) (2015) 975–990.

[31] G. Guo, H. Wang, D. Bell, Y. Bi, K. Greer, Using kNN model for automatic text categorization, Soft Computing 10 (5) (2006) 423–430.

## ACCEPTED MANUSCRIPT

[32] M.-L. Zhang, Z.-H. Zhou, Multilabel neural networks with applications to functional genomics and text categorization, IEEE Transactions on Knowledge and Data Engineering 18 (10) (2006) 1338– 1351.

[33] M. Lan, C. L. Tan, J. Su, Y. Lu, Supervised and traditional term weighting methods for automatic text categorization, IEEE Transactions on Pattern Analysis and Machine Intelligence 31 (4) (2009) 721–735.

[34] S. Tong, D. Koller, Support vector machine active learning with applications to text classification, Journal of Machine Learning Research 2 (Nov) (2001) 45–66.

[35] V. Vapnik, Statistical learning theory, Wiley, New York, 1998.

[36] N. Li, D. D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems 48 (2) (2010) 354–368.

[37] Y. Tang, Y.-Q. Zhang, N. V. Chawla, S. Krasser, SVMs modeling for highly imbalanced classification, IEEE Transactions on Systems, Man, and Cybernetics, Part B 39 (1) (2009) 281–288.

[38] W. Zhang, T. Du, J. Wang, Deep learning over multi-field categorical data, in: European Conference

[39] Y. Shen, X. He, J. Gao, L. Deng, G. Mesnil, A latent semantic model with convolutional-pooling structure for information retrieval, in: Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management, ACM, 101–110, 2014.

[40] V. L´opez, A. Fern´andez, S. Garc´ıa, V. Palade, F. Herrera, An insight into classification with imbalanced data: Empirical results and current trends on using data intrinsic characteristics, Information Sciences 250 (2013) 113–141.

[41] J. F. D´ıez-Pastor, J. J. Rodr´ıguez, C. Garc´ıa-Osorio, L. I. Kuncheva, Random balance: ensembles of variable priors classifiers for imbalanced data, Knowledge-Based Systems 85 (2015) 96–111.

[42] N. V. Chawla, K. W. Bowyer, L. O. Hall, W. P. Kegelmeyer, SMOTE: synthetic minority oversampling technique, Journal of Artificial Intelligence Research 16 (2002) 321–357.

[43] S. Tan, Y. Li, H. Sun, Z. Guan, X. Yan, J. Bu, C. Chen, X. He, Interpreting the public sentiment variations on Twitter, IEEE Transactions on Knowledge and Data Engineering 26 (5) (2014) 1158– 1170.

[44] A. McCallum, K. Nigam, et al., A comparison of event models for Na¨ıve Bayes text classification, in: AAAI-98 workshop on learning for text categorization, vol. 752, Citeseer, 41–48, 1998.

[45] X. Zhang, S. Mahadevan, X. Deng, Reliability analysis with linguistic data: An evidential network approach, Reliability Engineering & System Safety 162 (2017) 111–121.

[46] J. Lilleberg, Y. Zhu, Y. Zhang, Support vector machines and word2vec for text classification with semantic features, in: Cognitive Informatics & Cognitive Computing (ICCI\* CC), 2015 IEEE 14th International Conference on, IEEE, 136–140, 2015.

[47] S. Zhu, X. Ji, W. Xu, Y. Gong, Multi-labelled classification using maximum entropy method, in: Proceedings of the 28th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 274–281, 2005.

[48] D. Isa, L. H. Lee, V. Kallimani, R. Rajkumar, Text document preprocessing with the Bayes formula for classification using the support vector machine, IEEE Transactions on Knowledge and Data Engineering 20 (9) (2008) 1264–1272.

[49] S. Chakrabarti, S. Roy, M. V. Soundalgekar, Fast and accurate text classification via multiple linear discriminant projections, The VLDB Journal 12 (2) (2003) 170–185.

[50] Natural Language Toolbox, https://www.nltk.org/, Accessed: 2018-04-02.

[51] K. Sp¨arck Jones, IDF term weighting and IR research lessons, Journal of Documentation 60 (5) (2004) 521–523.

[52] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (7553) (2015) 436–444.

[53] J. Evermann, J.-R. Rehse, P. Fettke, Predicting process behaviour using deep learning, Decision Support Systems 100 (2017) 129–140.

[54] A. Krizhevsky, I. Sutskever, G. E. Hinton, Imagenet classification with deep convolutional neural networks, in: Advances in Neural Information Processing Systems, 1097–1105, 2012.

[55] G. Hinton, L. Deng, D. Yu, G. E. Dahl, A.-r. Mohamed, N. Jaitly, A. Senior, V. Vanhoucke, P. Nguyen, T. N. Sainath, et al., Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups, IEEE Signal Processing Magazine 29 (6) (2012) 82–97.

[56] R. Collobert, J. Weston, L. Bottou, M. Karlen, K. Kavukcuoglu, P. Kuksa, Natural language processing (almost) from scratch, Journal of Machine Learning Research 12 (2011) 2493–2537.

[57] M. Wo´zniak, M. Gra˜na, E. Corchado, A survey of multiple classifier systems as hybrid systems, Information Fusion 16 (2014) 3–17.

## ACCEPTED MANUSCRIPT

[58] B. Zadrozny, C. Elkan, Transforming classifier scores into accurate multiclass probability estimates, in: Proceedings of the Eighth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 694–699, 2002.

[59] S. Sankararaman, S. Mahadevan, Model validation under epistemic uncertainty, Reliability Engineering & System Safety 96 (9) (2011) 1232–1241.

[60] P. Ahlgren, C. Colliander, Document–document similarity approaches and science mapping: Experimental comparison of five approaches, Journal of Informetrics 3 (1) (2009) 49–63.

[61] D. P. Kingma, J. Ba, Adam: A method for stochastic optimization, in: International Conference on Learning Representation, ACM, 1–13, 2015.

[62] J. D. Rennie, N. Srebro, Loss functions for preference levels: Regression with discrete ordered labels, in: Proceedings of the IJCAI multidisciplinary workshop on advances in preference handling, Kluwer Norwell, MA, 180–186, 2005.

[63] F. Pedregosa-Izquierdo, Feature extraction and supervised learning on fMRI: from practice to theory, Ph.D. thesis, Universit´e Pierre et Marie Curie-Paris VI, 2015.

[64] Z.-H. Zhou, Ensemble methods: foundations and algorithms, Chapman and Hall/CRC, 2012.

# ACCEPTED MANUSCRIPT

## Biographical Notes

Xiaoge Zhang received his B.S. degree from Chongqing University of Posts and Telecommunications in 2011, and the M.S. degree from Southwest University in 2014, both in Chongqing, China. Currently, he is pursuing his Ph.D. degree in Vanderbilt University, and is expected to graduate in early 2019. From August to December in 2016, he interned at the National Aeronautics and Space Administration (NASA) Ames Research Center (ARC), Moffett Field, CA, working at the Prognostics Center of Excellence (PCoE) led by Dr. Kai Goebel. He was a recipient of the Chinese Government Award for Outstanding Self-financed Students Abroad in 2017. He has published more than 30 research papers in peer-reviewed journals, such as IEEE Transactions on Cybernetics, IEEE Transactions on Reliability, Decision Support Systems, Information Sciences, Safety Science, Annals of Operations Research, Reliability Engineering and System Safety, and International Journal of Production Research, among others. Four of his publications are included in the Essential Science Indicators (ESI) highly cited papers. His current research interests include uncertainty quantification, reliability assessment, risk analysis, network optimization, and data analytics. He is a student member of IEEE, INFORMS, and SIAM.

Sankaran Mahadevan is John R. Murray Sr. Professor of Engineering, and Professor of Civil and Environmental Engineering at Vanderbilt University, Nashville, Tennessee, where he has served since 1988. His research interests are in the areas of uncertainty quantification, model verification and validation, reliability and risk analysis, design optimization, and system health monitoring, with applications to civil, mechanical and aerospace systems. His research has been extensively funded by NSF, NASA, FAA, DOE, DOD, DOT, NIST, GE, GM, Chrysler, Union Pacific, American Railroad Association, and Sandia, Idaho, Los Alamos and Oak Ridge National Laboratories. His research contributions are documented in more than 600 publications, including two textbooks on reliability methods and 280 journal papers. He has directed 42 Ph.D. dissertations and 24 M. S. theses, and has taught several industry short courses on reliability and risk analysis methods. He is a Fellow of AIAA and EMI (ASCE). His awards include the NASA Next Generation Design Tools award (NASA), the SAE Distinguished Probabilistic Methods Educator Award, SEC Faculty Award, and best paper awards in the MORS Journal and the SDM and IMAC conferences. Professor Mahadevan obtained his B.S. from Indian Institute of Technology, Kanpur, M.S. from Rensselaer Polytechnic Institute, Troy, NY, and Ph.D. from Georgia Institute of Technology, Atlanta, GA.

## Highlights

• A hybrid model blending SVM and DNN ensemble predictions is developed to quantify the risk level of abnormal aviation events

• An innovative probabilistic fusion rule is proposed to blend the two model predictions

Cross-validation and statistical tests are used to demonstrate the prediction performance of the developed hybrid model

![](/api/attachments/E2W3EXCA/fulltext/images/20fccc9282212906d76b4326b8106886e11223ece838fb82518beebffbb80a3a.jpg)  
Figure 1

![](/api/attachments/E2W3EXCA/fulltext/images/cff79079c97cbae5caabae4bb0a3aceb1666ce70c92b39b494a490e83808694d.jpg)

![](/api/attachments/E2W3EXCA/fulltext/images/1309e61ad56367f634060afd5b0ec18303365898545851c49009763f3203fd59.jpg)  
Figure 3

![](/api/attachments/E2W3EXCA/fulltext/images/254b4242c2f593e9af3365aae21a35f06b75d41edbf626f5b0384f1b8a1d6886.jpg)  
Figure 4

![](/api/attachments/E2W3EXCA/fulltext/images/fdb7a8abebd1e62a3f5b710a81773076b7fef6483a422d7bae46b9405cdd96e5.jpg)  
Figure 5

![](/api/attachments/E2W3EXCA/fulltext/images/ecffb8b9ab68e746d6d3fa435eafb22b35e56080c6d2c9b5a72d25de82b65f96.jpg)  
Figure 6

![](/api/attachments/E2W3EXCA/fulltext/images/d779f4287819c3b4a823b5836af72aa7f3b212a6a3120f81e0e86ec72cd75202.jpg)

![](/api/attachments/E2W3EXCA/fulltext/images/4c4f37d1dade8a984689cb2890a402b39aa2920a20877f63099f0b80969fe002.jpg)  
Figure 7

![](/api/attachments/E2W3EXCA/fulltext/images/21206ffc2b972d36732265b264aff127a76e51dae63af1f9797096ebaefb88b1.jpg)

![](/api/attachments/E2W3EXCA/fulltext/images/365303214a57ea4f758b590032fac01917d83ed2d6e7b9396824405b91177863.jpg)  
(a)

![](/api/attachments/E2W3EXCA/fulltext/images/b0bc952934aa7128d823a56b54abc37c2910a9f68471c28a9d490974c910b6ed.jpg)  
(b)  
Figure 8

![](/api/attachments/E2W3EXCA/fulltext/images/ffa6961de16e0b156175ca9e94b4152a80b3f18ca1128b7cd6a2c3deb13849ff.jpg)  
(c)

![](/api/attachments/E2W3EXCA/fulltext/images/430dd8abf5d576bb577b22644ee06baada11de4396eb7b373657b05f5b364512.jpg)  
Figure 9
