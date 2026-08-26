---
otero_id: 10556
otero_key: "TVXWTWMN"
title: "A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time"
authors: "Audrey Fertier; Anne-Marie Barthe-Delanoë; Aurélie Montarnal; Sébastien Truptil; Frédérick Bénaben"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113260"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

![](/api/attachments/TVXWTWMN/fulltext/images/669a1125b91ba17611d51f4db5369a413d850e9efba818918dd888a00ad7a49d.jpg)

Audrey Fertier<sup>a,∗</sup>, Anne-Marie Barthe-Delanoë<sup>b</sup>, Aurélie Montarnal<sup>a</sup>, Sébastien Truptil<sup>a</sup>, Frédérick Bénaben<sup>a</sup>

<sup>a</sup> Centre Génie Industriel, Université de Toulouse, IMT Mines Albi, France

<sup>b</sup> Laboratoire de Génie Chimique, Université de Toulouse, CNRS, INPT, UPS, Toulouse, France

## A R T I C L E I N F O

Keywords: Information system Emergency decision support system Complex event processing Big Data Situation awareness Crisis management

## A B S T R A C T

This paper studies, designs and implements a new type of emergency decision support system that aims to improve the decision-making of emergency managers in crisis situations by connecting them to new, multiple data sources. The system combines event-driven and model-driven architectures and is dedicated to crisis cells. After its implementation, the system is evaluated using a realistic crisis scenario, in terms of its user interfaces, its ability to interpret data in real time and its ability to manage the 4Vs of Big Data. The input events correspond to trafic measurements, water levels, water flows, water predictions and flow predictions made available by French oficial services. The main contributions of this study are: (i) the connection between a complex event processing engine and a graph database containing the model of the crisis situation and (ii) the continuous updating of a common operational picture for the benefit of emergency managers. This study could be used as a framework for future research works on decision support systems facing complex, evolving situations

## 1. Introduction

William Wallace and Franck De Balogh [1] were among the first to recognise four phases in crisis management: prevention, preparation, response and recovery. Crisis cells are activated during the response phase. These cells are composed of emergency service managers, local authority representatives, etc. They initiate, coordinate and monitor the execution of all the measures intended to deal with the crisis and its efects. Crisis cells are informed by stakeholders, who also receive di rections from their crisis cells.

## ‘The trick is to be ready for a surprise’ — Patrick Lagadec [2]

Daniela Fogli and Giovanni Guida [3] underline the importance of structured and coordinated crisis response management, underpinned by a decision support system that is capable of: (i) sharing information with citizens, (ii) interacting with other information systems, (iii) coordinating heterogeneous and autonomous stakeholders, (iv) antici pating the consequences of decisions made. In their view, the usability of the system relies on a clear selection of concepts and on its ability to model any kind of crisis situation.

The use of an ontology or metamodel, as defined by Bézivin [4], enables interoperability ((ii)). The other requirements put forward by

Fogli and Guida [3] complement the approach proposed by Mica Endsley [5] to support decision-makers facing complex evolving situations, through the enhancement of their situation awareness. This approach depends on three steps: the perception of some of the elements composing the environment, the comprehension of the ongoing situation and the projection of the situation into the near future. A cognition process proposed by Giuseppe D’Aniello et al. [6] supports these three steps. This process includes the following actions: define objectives, gather data, identify the situation, apply rules, take action, learn and evolve.

First, to automate the perception and gathering steps, a system needs to access data that is continuously emitted by numerous, heterogeneous, known and unknown sources. This situation is referred as the 4Vs of Big Data. As defined in Ref. [7], it is a large, massive Volume of data, continuously generated and needing to be processed to support real time decision-making. The second of the 4Vs relates to Velocity, due to the dynamicity of the environment that causes out-of-date content. In addition, the data are generated in a Variety of formats and types by numerous heterogeneous sources that challenge interoperability between systems [8]. Finally, the last V refers to the Veracity of the available data, in other words their uncertainty [7], their objectivity and their credibility. To go further, once the 4Vs have been controlled, what matters is the value [7], security, and life cycle of both the ob tained information and the processed data.

Then, a system such as the one described by D’Aniello et al. [6] needs to interpret these data in order to identify the ongoing situation. A model of the current crisis situation can then be updated with this new information. It will need to suit the level of abstraction and aggregation required by the emergency managers. This can be achieved through the use of a Common operational picture, defined by Wolbers and Boersma [9] as a display of relevant information shared by, and for more than one person to achieve situational awareness.

In addition, Aysu Sagun et al. [10] point out that the model of the crisis situation could be used to further support decision-making by ofering a process by which stakeholders can coordinate actions during the whole response phase.

To sum up, the data available to the crisis cells can be used to enhance the situation awareness of the stakeholders. Yet, the emergency managers do not have the time to collect and interpret this information, especially given the crisis situation and the issues linked to the 4Vs of Big Data. The goal therefore is to provide a decision support environment, delivering an up-to-date common operational picture in every crisis cell without requiring additional eforts from the emergency managers. The issue can be summarized as follows:

How to collect, interpret and contextualise streams of raw data to automatically detect and model the consequences of a crisis threatening a given territory, while managing the 4Vs of Big Data?

Section 2 presents a four-fold literature review. Each part of the review ends with a presentation of the research works related to the Research Issue. Section 3 describes the methodology we followed, the scope of the research work, as well as the data and information avail able for the case study. Section 4 describes the design and implementation of a new emergency decision support system. Finally, Section 5 proposes a qualitative and a quantitative evaluation of the system, while taking into account the limits of its use in a given context.

## 2. Related works

This section aims to find existing emergency decision support systems able to (i) sustain the situation awareness of their users, (ii) pro cess data to perceive and comprehend ongoing situations, or (iii) manage the 4Vs of Big Data.

The following four parts are based on the methodology of the Systematic Literature Review described in Ref. [11]. First, the problem is stated. Here, it is our research issue. Then, a database and keywords are selected to design proper queries. All the literature reviews were run on the Web of Science<sup>1</sup> database.

## 2.1. Situation awareness and emergency decision support systems

Are there emergency decision support systems aiming to improve the situation awareness of emergency managers through automatic collection and interpretation of raw data?

The first literature review aims to present emergency decision support systems able to enhance the situation awareness of their users (perception, comprehension, projection of complex situations). The query ‘("situation awareness" OR "situational awareness") AND (emergency OR disaster OR crisis OR emergencies OR disasters OR crises) AND ("decision support system" OR "decision support systems")’ returned thirteen articles. Among them, eight were selected. They aim to support situation awareness in the following contexts: early warnings for tsunamis [12], landslides [13] fires [14-16], on-board fire emergencies [17], quick disconnect processes on sub-sea wells [18] or protection of World Heritage Sites [19]. They ofer to improve (i) connection to the real world through interpretation [13, 15, 17–19] or communication [14] of events, (ii) the provision of a structured information set to support decision-making [16] and (iii) the design of specific graphical user interfaces [12]. Some may take the shape of a common operational picture [15]. Only the ones able to collect, interpret or contextualise data are presented in Table 1. Because of the complexity and heterogeneity of the information needed to describe a crisis situation, the articles are evaluated for the variety of their input data (0 to n), the complexity of the interpreted information (0 to m attributes of 0 to p concepts), the speed of their interpretation process, the contextualisation of their user interface and, finally, their ability to use forecasts.

For example, the emergency decision support system proposed by Bukhtiar Mohsin et al. [15] recovers data sent by their drone to detect toxic substances or injured victims. Their systems could answer most of the requirements of our research issue. Yet, their automatic data collection is custom-made for their own system. As crises are unpredictable, there is still a need to access multiple known or unknown sources emitting on as many various topics as possible.

## 2.2. Event processing and emergency decision support systems

Are there emergency decision support systems able to process data or events, in real time, by means of easy subscription to new sources?

The second part of the literature review aims to present emergency decision support systems that are able to access and process multiple streams of events. As defined by Wasserkrug et al. [20], events are data emitted by people or devices that are associated with the occurrence of ‘real’ events: what happened, is happening or could happen. Flouris et al. [21] use complex event processing to detect temporal, spatial and semantic patterns. An event-driven architecture that respects the OASIS standard (available at www.oasis-open.org) also enables publish/subscribe mechanisms. This will allow a system to subscribe to topics and access both known and unknown sources. In this context, the query ‘("complex event processing" OR "data processing") AND (emergency OR disaster OR crisis OR emergencies OR disasters OR crises) AND ("decision support system" OR "decision support systems")’ on computer science, information systems and artificial intelligence, returned seventy-six articles. Among them, only four were selected because they met more than 3 of the criteria linked to the use of complex event processing or crisis management: (i) the use of an ontology or a metamodel to model complex situations, (ii) the connection to new sources to adapt quickly to complications, (iii) the use of time windows to support complex reasoning, (iv) the evaluation of the trustworthiness of deduced information and (v) the management of the variety and (vi) volume of input events.

First, Lauras et al. [22] propose a system that analyses events (radioactivity measurements, wind forecasts) and issues an alarm if they match their emergency rules. Mijović et al. [23] propose a system that integrates existing supervision systems, such as fire and smoke detectors. It analyses the events to issue a suitable alert level given the incident severity. It uses models to ofer a visualisation of the available sensors and actuators. Itria et al. [19] propose a system that processes events such as people detection and vibration detection to detect anomalies. It refers to a dedicated event ontology and performs event trust analysis: it runs an anomaly detection algorithm on the location of complex (output) events. Finally, Kovalchuk et al. [24] simulate queues of patients to predict mortality rates and support planning decisions in hospitals. They also analyse streams of ECG events to trigger an alert if a threshold is exceeded. All these systems are presented in Table 2.

Although these works ensure the management of the event volume and the temporal dimension, none of them seem to comply with all the criteria imposed by a complex crisis situation, except perhaps fo

Table 3  
Table 4  
Emergency decision support systems aiming to enhance situation awareness. The attributes marked with ! are Boolean. Abbreviations: Y. Yes N. No, U.I. User interface, G.U.I. Graphical User Interface, N/A Not Available.

<table><tr><td>Ref.</td><td>Input variety</td><td>Output complexity</td><td>Real time</td><td>UI</td><td>Forecast</td></tr><tr><td>[12]</td><td>1 (wave range)</td><td>1 of 1 (!warning)</td><td>Y</td><td>GUI</td><td>Y</td></tr><tr><td>[17]</td><td>n (sensors)</td><td>n of 1 (action list)</td><td>Y</td><td>GUI</td><td>N</td></tr><tr><td>[13]</td><td>1 (rainfalls)</td><td>n of 1 (landslide risk)</td><td>Y</td><td>GUI</td><td>Y</td></tr><tr><td>[15]</td><td>n (sensors &amp; videos)</td><td>n of n (fire emergency)</td><td>Y</td><td>GUI</td><td>N</td></tr><tr><td>[19]</td><td>n (tweets &amp; sensors)</td><td>1 of 1 (!gathering)</td><td>Y</td><td>N/A</td><td>N</td></tr><tr><td>[18]</td><td>n (sensors)</td><td>1 of n (!event)</td><td>Y</td><td>N/A</td><td>Y</td></tr></table>

Complex event processing for emergency decision support system. Abbreviations: N No, Y Yes.

<table><tr><td>Ref.</td><td>Ontology feeding</td><td>Easy subscriptions</td><td>Temporal patterns</td><td>Event veracity</td><td>Event variety</td><td>Event volume</td></tr><tr><td>[19]</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>[22]</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td></tr><tr><td>[23]</td><td>N</td><td>N</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>[24]</td><td>N</td><td>Y</td><td>Y</td><td>N</td><td>Y</td><td>Y</td></tr></table>

Complex event processing for emergency decision support system. Abbreviations: N No, Y Yes, (n of 1) n attributes of 1 concept.

<table><tr><td>Ref.</td><td>Ontology feeding</td><td>Easy subscriptions</td><td>Temporal patterns</td><td>Event veracity</td><td>Event variety</td><td>Event volume</td></tr><tr><td>[25]</td><td>(n of 1)</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr></table>

Barthe-Delanoë et al. [25], which followed the work of Lauras et al. [22]. This particular study is evaluated in Table 3. The authors used four diferent data sources to monitor the response to a nuclear incident. They were able to instantiate a risk (composed of several attributes). Like Mijović et al. [23], they used the emergence/nonemergence of some events to verify the trustworthiness of past ones.

The complex event processing paradigm makes it possible to follow the velocity of input data streams, through the use of temporal patterns, regardless of the volume or variety to be managed. In addition, the complex event processing rules can ensure the veracity of complex event outputs. However, this paradigm alone does not manage the volume or variety of these outputs.

## 2.3. Big Data and emergency decision support systems

Are there emergency decision support systems able to manage the issues linked to Big data?

The third literature review aimed to present emergency decision support systems able to manage the issues linked to the 4Vs of Big Data, while collecting, interpreting and contextualising raw data to enhance the situation awareness of their users. Real time data available to the emergency managers can come from social media, sensors coming from the Internet Of Things, or specific applications dedicated to recovering volunteered geographic information. The query ‘("social media" OR microblog\* OR "internet of things" OR sensor\* OR "volunteered geographic information") AND (emergency OR hazard OR disaster OR crisis OR emergencies OR hazards OR disasters OR crises) AND ("big data" OR (volume AND variety)) AND ("decision support system" OR "decision support systems")’ returned two reviews and one article. But none of them propose solutions to manage the 4Vs of Big Data while inferring new information to improve the situation awareness of emergency managers.

## 2.4. Modelling of a crisis situation in real time from raw data

Are there systems able to process heterogeneous data to update the model of a complex situation in real time?

This section broadens the scope of research and tries to find all the information systems that try to process data to update a model of a complex situation in real time. The query ‘(situation AND model AND (ontology OR metamodel) AND data)’ gave 314 results. 91 articles were selected by title and, among them, 24 by abstract, based on their links with the research issue: only the ones which proposed collecting, interpreting and contextualising data in real time were selected. The eight articles selected were evaluated on the variety and volume of input data (0, 1 or p), the complexity of the output set (0, 1 or n attributes of 0, 1 or m concepts), the velocity of the interpretation process and the veracity control of the output information. The results are presented in Table 4. For each row, when one of the result was not suficient for the evaluation, another paper by the same authors was added to the review.

These systems focus on getting a particular piece of information and none of them automatically instantiate more than one concept. The system proposed by Alexopoulos et al. [36] could provide answers to most aspects of our research issue. It uses rules to interpret location sensors, a weather station and energy sensors on machines to detect a worker in predefined zones and automatically assign a suited set of tasks. Yet, their system relies on the data coming from their own devices and focuses on adapting a process to the current availability of resources.

## 2.5. The gaps to be filled by emergency decision support systems

To sum up, no emergency decision support system was found to cover all the needs of an information system able to enhance the situation awareness of its users confronted with a complex situation by connecting to multiple data sources. All the requirements are summed up by the research question presented below. It enriches the research issue stated in the introduction with the results of the literature reviews. The transversal management of the 4Vs of Big Data appears in parenthesis.

How to (i) receive event streams emitted from known and unknown sources (data volume & velocity & variety), (ii) interpret them in realtime, (iii) automatically detect the various consequences of the crisis (information variety & velocity), (iv) automatically update the model of an on-going crisis situation by instantiating a metamodel common to all kinds of crisis situations (information variety), (v) display the corresponding common operational picture to support the decision-making of the emergency managers and (vi) allow the emergency managers to manually edit available information (information veracity)?

Information system able to interpret evolving data to model complex situations. The attributes marked with ! are Boolean. Abbreviations: Y. Yes, N. No.

<table><tr><td>Ref.</td><td>Input variety</td><td>Output complexity</td><td>Real time</td><td>Veracity</td></tr><tr><td>[26, 27]</td><td>4 (light, noise, temperature, !door)</td><td>1 of 1 (!room)</td><td>Y</td><td>Y</td></tr><tr><td>[28]</td><td>3 (sensors of an underwater vehicle)</td><td>n of 1 (fault)</td><td>Y</td><td>N</td></tr><tr><td>[29]</td><td>n (traffic data)</td><td>n of 1 (road)</td><td>Y</td><td>N</td></tr><tr><td>[30]</td><td>2 (speed, location of vessels)</td><td>n of 1 (threat)</td><td>Y</td><td>N</td></tr><tr><td>[31, 32]</td><td>3 (time, position, role)</td><td>n of 1 (anomaly)</td><td>Y</td><td>N</td></tr><tr><td>[33]</td><td>4 (!door, time, presence, light)</td><td>1 of 1 (!room)</td><td>Y</td><td>N</td></tr><tr><td>[34, 35]</td><td>4 (time, location, weather, company)</td><td>1 of 1 (!trip)</td><td>Y</td><td>N</td></tr><tr><td>[36]</td><td>3 (weather, energy, location)</td><td>n of 1 (task)</td><td>Y</td><td>N</td></tr></table>

## 3. Methodology, scope of work and input data

As part of a French research project, an expert interviewed several French practitioners familiar with crisis management. The expert, Mme. Dolidon, is part of the CEREMA (the French Centre for Studies and Expertise on Risks, the Environment, Mobility and Development) which is a public institution under the dual supervision of the French Ministry of Ecological and Inclusive Transition and the French Ministry of Territorial Cohesion and Relations with Local Authorities. The expert used the interviews to highlight the current dificulties of French emergency managers that are due to the complexity of a crisis situation: (i) the lack of experience regarding the unpredictable nature of the crisis situations, (ii) the integration of private actors, (iii) dispersed information that can lead to communication issues, (iv) the anticipation of the near future, (v) the implementation of operational services in the field, (vi) decision-making under uncertainties, (vii) the analysis of potential issues depending on the interconnection of networks, (viii) the quantity and variety of information to be shared, (ix) the diversity of computer tools or websites to be consulted to obtain the required information and (x) the diversity and complexity of use of existing contingency plans.

The response to our research question will meet their requirements. The processing, interpretation and modelling of event streams partly automates the perception step of situation awareness ((ix)). It also enables the identification of cascading efects due to the interconnection of networks ((vii)). The updated common operational picture mitigates the issue of a relative comprehension of the crisis situation ((iii)). It facilitates the understanding of the crisis situation and therefore sup ports anticipation and decision-making under uncertainties ((iv, vi)). The use of a metamodel limits the variety of information to be shared ((viii)).

In addition, an open source prototype, R-IOSUITE (https://r-iosuite. com) can use the updated model of the crisis situation to deduce a feasible response process, using the information contained in existing contingency plans ((x)). The process can then be orchestrated between the stakeholders ((v)). This facilitates the integration of private actors, or volunteers, as long as their capabilities are known ((ii)).

We propose answering our research question by transforming R-IOSUITE into an emergency decision support system able to meet nine of the ten requirements retrieved from the interviews with French emergency managers. We propose the design and implementation of the AIC information system: the (A)cquisition of events to perceive the current crisis situation; the (I)nterpretation of the collected events thanks to actual, in use, business rules to model the crisis situation that instantiates a given metamodel; and the (C)ontextualisation of the interpreted instances to infer new information. As a result, a common operational picture is updated and displayed on a map. This aims to automate the perception step of situation awareness, while leaving the decisions to the emergency managers.

For evaluation purposes, we propose a realistic case study. It simulates a flood of the French Loire River, between two main tributaries, with a return period of one hundred years. The hydrological part of the scenario was modelled by two oficial French flood forecast centres. They provided the water flows and water levels predicted on nine measuring stations for 56 h, over ten days of flooding, with a low (10%), medium (50%) and high probability (90%) of occurrence. In addition, the oficial French road services provided us with real trafic data emitted for one day between 1 am and 12 pm. Each data point gives the number of vehicles and trucks spotted between two cities. Because of the publish/subscribe requirement, every data set available in the case study has been turned into event streams. Each event was sent on a topic, with an id, a date of emission, a location and a description.

## 4. Result: the AIC information system

This section presents the design and implementation of the AIC information system. It answers the research question and, therefore, the research issue. It also addresses the practical requirements of the French emergency managers who were interviewed.

## 4.1. The design of the AIC information system

The design of the AIC information system begins with the setting-up of a metamodel dedicated to representing crisis situations. The complex event processing engine is then introduced to interpret and con textualise events. Finally, the mechanisms chosen to "acquire" events are presented.

## 4.1.1. A metamodel to enable interoperability

The AIC information system follows the model-driven interoperability method [37] with a unified approach of interoperability [38]. This is done to enable information sharing with other information systems. A unified approach includes the use of a common metamode or ontology: an ‘explicit specification of conceptualisation’ [39] depending on the user's point of view, the desired scope of study and the desired level of abstraction [40].

To represent a complex, evolving crisis situation, a metamodel must enable complex reasoning and cover all the information needed by the crisis cells to take decisions. A search was made on the Web of Science database with the query ((ontology OR ontologies OR meta-model\* OR metamodel\*) AND ("natural disaster" OR "natural disasters")). None of the results was able to (i) model complex relations between concepts and (ii) describe all the types of information needed by the emergency managers and (iii) adapt to the ongoing crisis, whatever its nature. In contrast, the metamodel presented in Ref. [41] and implemented in R-IOSUITE can represent complex relationships, information on the available stakeholders (Partners), the risks and incidents to be dealt with (Objectives) and the locations of assets at stake (Context) whatever the nature of the crisis or the level of detail needed (goods, roads, highways, …).

Fig. 1 presents this metamodel. For the research work presented in this paper, three concepts have been added to the original metamodel from Lauras et al. [41] to fit the requirement of our business issue: the ‘Data sources’, ‘Critical infrastructure’ and ‘Sensitive building’ concepts. This augmented metamodel is described below.

A "Partner" is an organisation. A "Collaboration" groups partners who agree on common objectives. An "Objective" concerns an "Opportunity" or a Threat to the collaboration. An "Environment component" can be anything which constitutes the environment a long as the collaboration uses or values it. A "Characteristic" of the environment can generate opportunities or threats. An "Event" materialises an opportunity or a threat. A "Capability" is the ability of one partner to do something for the benefit of the collaboration. The collaboration can reach its objectives by coordinating the capability of its partners. The resulting process is called "Behaviour". A behaviour consists of activities. An "Activity" invokes a capability. A "Procedure" is a set of activities prepared to face specific objectives. Finally, a "Data source" is a web service which publishes data.

The core of the metamodel is specific to the modelling of a collaboration of organisations, while the concepts at the top of Fig. 1 are specific to the modelling of crisis situations.

![](/api/attachments/TVXWTWMN/fulltext/images/5e0276ae9614711691d2c8a71956c64908351c6be9e16d697cb02c0e004e97eb.jpg)  
Fig. 1. Metamodel adapted from Ref. [41] to fit our goals and needs. It was modelled following the unified modelling language (UML) class diagram. (For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)

During a crisis situation, an environment component can be a "Territory", a "Person", a critical infrastructure or a sensitive building threaten by the ongoing crisis. As defined in [42], a "Critical Infrastructure" is needed for the generation or supply of energy, food, health or public order. A "Sensitive building" is a building that is not a critical infrastructure. A "Community", as defined in [43], gathers people sharing the same blood, place or spirit. A "Danger" is a characteristic threatening a territory. A "Risk" is a threat. An "Incident" materialises a risk.

The rest of this paper uses this metamodel to structure the information within the proposed decision support system. Of course, any other metamodel describing a crisis situation could be used. Besides, model transformation rules can be used to enable the use of information structured by other metamodels.

## 4.1.2. The interpretation and contextualisation of events to model collaborative situations

To save time during the crisis response, a part of the crisis situation model can be modelled in the preparation phase, before the emergence of a crisis. This concerns the partners and the critical infrastructure of a given territory. The AIC information system is especially helpful to model the information that must be retrieved during a crisis situation and cannot be retrieved beforehand: the emerging risks and incidents due to the crisis. Like Barthe-Delanoë et al. [25], we use complex event processing to detect critical events and manage the 4Vs at the data level (see Table 3).

One of our main contributions enables our complex event processing rules to refer to the information contained in the situation model. It does so by sending queries based on the concepts described in the metamodel. The rules are therefore divided into two categories: (i) the ones that need to query the content of the current crisis situation model and (ii) the others. The former are interpretation rules. They aim to update the situation model with new Dangers after the reception of events exceeding predefined thresholds. This group of rules is similar to the ones used in Refs. [23] or [25]. For example, the threshold can correspond to the safety level of a dyke, which, if exceeded, will trigger a Danger of Flooding to be added to the model of the crisis situation. The rules correspond to actual business rules that are currently followed by emergency managers. As a contribution, the second group, which we called contextualisation rules, aims to detect the Risks threatening the vulnerable assets located inside the detected danger zones. This type of rule can be represented by Eq. (1): an asset that coexists (\*) with a danger generates (=) a risk.

$$
\text { Risk } = \text { Danger*Vulnerable   asset }\tag{1}
$$

In addition, these rules can be (i) generalised to monitor complex collaborations of organisations, or (ii) tailored to monitor a specific crisis response, thanks to the layered structure of our metamodel. For example, Eq. (2) generalised Eq. (1) to any kind of collaboration. Eq. (3) makes it specific to dealing with a road crisis situation.

$$
\text { Opportunity / Threat } = \text { Characteristic*Environment   component }\tag{2}
$$

$$
\text { Congestion   Risk } = \text { Danger   of   snow*Highway }\tag{3}
$$

## 4.1.3. The acquisition of events in real time

To feed our complex event processing rules in real time, the AIC information system follows the recommendations of the OASIS standard. To be able to receive events from both known and unknown sources, it uses a publish/subscribe environment, as described in Ref. [44], with events described in extensible markup language (XML) and event types described in an XML schema definition (XSD).

## 4.2. The implementation of the AIC information system

Fig. 2 presents the architecture of the AIC information system on the left and the R-IOSUITE information system on the right. This archi tecture makes it possible to answer nine of the ten requirements of the French emergency managers presented in Section 3. All its components are based on the metamodel, the interpretation, contextualisation and acquisition of events described above. They are described in more depth in the next paragraphs. In the figure, the dotted lines represent event streams and the solid lines represent HTTP/SOAP exchanges.

## 4.2.1. The graph database to record the model of the crisis situation

R-IOSUITE hosts the model of the crisis situation in a graph-oriented database called Neo4J, available at https://neo4j.com/. It can be queried using a dedicated language called Cypher. Neo4J provides an easy way to match patterns of nodes and relationships within the model.

## 4.2.2. The metamodel structuring the information inside the decision support system

The metamodel presented in Fig. 1 is implemented in R-IOSUITE. It is described in an XML. The XML is structured by an XSD (XML schema definition), that can be seen as a meta-metamodel. The former describes all the markups used in the metamodel (a node, a property, a relationship …). The graph database has been augmented with a dedicated API to ensure that the model of the crisis situation matches the implemented metamodel.

EMERGENCY DECISION SUPPORT SYSTEM  
![](/api/attachments/TVXWTWMN/fulltext/images/43f313dbf450a4ea5c89c0aaab5df6bd77c84b5f9849e5b202d1d84c0ece2228.jpg)  
Fig. 2. The architecture defined and implemented to (A)cquire data of several types, from several sources, (I)nterpret and (C)ontextualise them into a model suited to represent a complex situation. (For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)

An example of instantiation is given in Fig. 3. The top of each box indicates which concept is instantiated. The instances are represented by an icon along with their name. In this example, the emergency managers face an incoming flood on their territory. Two partners are considered: the local administration (Prefecture 45) and the road services (DDT 45). Here, they have to coordinate three of their capabilities to prevent the risk of victims on their territory.

As part of the Middle Loire area case study, this metamodel was used to model 15,569 environment components. This evaluation validates the possibility to represent all the information describing a French territory that is needed by the French emergency managers. It takes into account the airports, railway stations, water stations, prisons, summer camps, hospitals, schools, sensitive industrial sites, dykes and buildings dedicated to crisis management.

4.2.3. The complex event processing engine to interpret and contextualise events

The complex event processing engine has been developed in Java. The complex event processing rules are described in a dedicated query language called SIDDHI, available at https://docs.wso2.com. It can process event streams and detect patterns. The main advantage of this language resides in the functions that can be described and added manually to the complex event processing rules. For example, we developed the function that enables our first contribution: the query to the Neo4J database to ask for the suppression, addition or update of an instance on the situation model with the Cypher language. Each rule is described in an XML file that specifies on which topics to subscribe and notify events, and which types of events (polygon of one colour in Fig. 2) to process.

In Fig. 2, the complex event processing engine refers to three rules listening to the events of the water event type, the addNode event type and the weather event type. In the figure, it first receives a water event that triggers a complex event asking for the addition of a node on the model of the crisis situation (a Danger represented with a pink star). This addition triggers another rule that asks for the addition of three other nodes (three Risks represented with a red, green and orange stars in the top left of the figure).

![](/api/attachments/TVXWTWMN/fulltext/images/b3dd04355e5352db93f523e07756a12a07f3dbbce931d047031891a6df2aa05d.jpg)  
Fig. 3. One example of model representing a crisis situation, dedicated to the emergency managers of the French city of Orleans.

As part of the Middle Loire case study, eleven complex event processing rules were tested to detect four dangers, six risks and one incident. All the rules are presented below. Very few rules are needed to cover one use-case. The first line indicates the event topic and event type listened to by their event processing agent. Eqs. (4), (5) and (8) are the interpretation rules which directly translate actual business rule recovered from the interviews of experts. Eq. (6) is a contextualisation rule which infers the risks threatening each territory. The parts in grey represent the data contained in the input water of trafic events. For the rules Eqs. (4) and (5), the thresholds correspond to the security levels of the dykes protecting the two cities. If the forecast water level exceeds them, a Danger is added to the model of the crisis situation. Then, for each Danger received, the rule Eq. (6) generates a risk of submersion for each road, water station, retirement home and dyke present in the model. The rule Eq.(6) is implemented by means of four SIDDHI QL rules, one for each node type to be retrieved with a query to the Neo4J graph database. For example, Eq. (7) is the query dedicated to retrieving all the retirement homes. The pink variables are automatically assigned by the SIDDHI QL homemade function given the description of the input event. The rule Eq. (8) generates a danger for the whole Middle Loire area if the flow resulting from both the River Loire and River Allier exceeds 3500 m<sup>3</sup>/s. Finally, the last implemented rule (Eq. (9)) adds an incident to the model when no evacuation from the city of Orleans is detected. tv2 is the number of vehicles coming from Orleans.

Event topic:Water, Event type:ForecastedWaterLevel

=If stationName Orleans and waterLevel 5

Thenadd new Danger flood likely in stationName

(4)

Event topic:Water, Event type:ForecastedWaterLevel

=If stationName Blois and waterLevel 4.5

Thenadd new Danger flood likely in stationName

(5)

Event topic:AddNode, Event type:AddUpdateDeleteNode =If node0. role Danger and node0. name contains flood likely =For allnode1. type (Road, Water station, Retirement home or Dyke), Addnew Risk submersion of node1.name

(6)

=Match (node: sensitiveBuilding) Where node. type Retirement home With point(latitude: var0, longitude: var1 ) As pDanger, point(latitude:node.latitude, longitude:node.longitude) As pSB <Where distance(pDanger, pSB) var2 Return node

(7)

Event topic:Water, Event type:ForecastedFlowLevel =If stationName Givry and waterFlow 3500 Thenaddnew Danger high probability of flood

(8)

Event topic:Traffic, Event type:TrafficMeasures =If stationName StHilaire and tv2 500 Thenadd new Incident no evacuationby road from Orleans

(9)

## 4.2.4. The message broker managing events inside the system

The Message broker has been developed in Java. It can subscribe to any kind of event publishers. When an event is received, it forwards it to the diferent services of the system. The complex event processing rules all subscribe to the Message broker and the message broker sub scribes to all the topics needed by the complex event processing rules. The message broker also notifies the API of the Neo4J database when the model of the crisis situation has to be updated.

In Fig. 2, the message broker has subscribed to three topics: A (addNode), B (weather) and C (water). It is notified of a forecastedWaterLevel event. It transmits it to the complex event processing engine, receives in turn the complex event emitted under the topic addNode, and pushes it to both the complex event processing engine and the graph database API.

## 4.2.5. The simulation of events from a crisis situation

The data available for each case study are simulated by a specific tool, R-IOSEMIT, which is part of R-IOSUITE, developed in Java and Typescript (for the Web user interface). It is dedicated to the simulation of events described in XML files. The frequency and topics are specified in two other XML files called the configuration file and the topic set file.

In Fig. 2, R-IOSEMIT simulates two event streams on two topics: the water topic and the weather topic.

As part of the Middle Loire case study, two types of events were simulated: trafic measurements, and water flow and water level forecasts. For example, Fig. 4 represents an event, along with its type, that communicates on the state of the trafic for the last hour between two cities. This occurrence shows that 10 vehicles were going in the direction of the French city of Orléans and 14 were heading the opposite way.

## 4.2.6. The visualisation and modification of the crisis situation mode

To enhance the value of the information processed by the emergency decision support system, the emergency managers can visualise the model of the crisis situation in a modeller (R-IODA) and a geographical information system (R-IOPLAY). R-IOPLAY ofers a common operational picture that can adapt to the needs of its users by means of layers: they can choose to see only the stakeholders involved or the critical infrastructure at stake for their level of command and control. A common operational picture is shown at the top right of Fig. 2. Every instance of concept of the R-IOSUITE metamodel has a geolocation that takes the shape of a point (as a critical infrastructure), a polyline (as a road) or a polygon (as an administrative area).

![](/api/attachments/TVXWTWMN/fulltext/images/a6cc0043d377c9ed9cc0248a69300c379bb71ceb63ddf14554e2f3440ffd485e.jpg)  
Fig. 4. An event described in a extensible markup language (XML) file and its type described in an XML schema definition (XSD).

![](/api/attachments/TVXWTWMN/fulltext/images/e2cdc88389d9dd3484e928f26814c67cc4bb514a6c78700ff5f322b3a65ea06e.jpg)  
Fig. 5. The user interfaces of the implemented information system. (For interpretation of the references to colour in this figure, the reader is referred to the web version of this article.)

## 4.2.7. The deduction and monitoring of a crisis response process

The modeler, R-IODA, and the geographical information system, R-IOPLAY, can also be used to automatically deduce a feasible response process. It inherits from the work of Wenxin Mu et al. [45, 46]. As such, it uses a strategy of deduction developed in Java. If needed, the emergency managers can modify it or ask for another deduction.

Then, R-IOWA can orchestrate the validated response process between the different stakeholders involved in it. This inherits from the work of Nicolas Boissel-Dallier et al. [47]. The response process is described in XML files and it instantiates a set of concepts that are close to the BPMN standard (available at http://www.bpmn.org/).

During the orchestration, R-IOTA detects when the situation expected from the execution of the response process difers too much from the observable situation. This inherits from the work of Anne-Marie Barthe-Delanoë et al. [25, 48]. It is carried out using a Java-based strategy of detection.

## 5. Evaluation on a realistic case study

## 5.1. The events and information available for the evaluation

The implemented emergency decision support system was tested on the Middle Loire flooding scenario. This includes 155 flood forecast events, emitted simultaneously by three sources, three interpretation rules to detect dangers, five contextualisation rules to detect risks and 1122 objects of interest.

## 5.2. Qualitative evaluation of the emergency decision support system

All the implemented user interfaces are presented in Fig. 5. From top left to bottom, the applications are described below.

R-IOSEMIT launches the simulation of event streams. R-IOPLAY is the common operational picture. Emergency managers can add new instances by dragging the icons from the left menu to the map. The red areas represent the afected areas. R-IODA is a modeller which clarifies the visualisation of complex modelling. Emergency managers can, for example, model the available stakeholders, their capabilities and the links between them. R-IOWA shows the orchestration of the response process. Finally, R-IOTA monitors the ongoing process. It shows un expected information with dotted lines or flashing tags.

R-IOPLAY, R-IODA and R-IOTA are now automatically updated with new dangers, risks and incidents interpreted from raw data and contextualised with regard to the ongoing crisis situation. This is accomplished by means of our contribution to R-IOSUITE: the AIC information system.

For practical evaluation of the emergency decision support system, a demonstration took place each year, between 2015 and 2018, in front of experienced emergency managers, from diferent levels of the French chain of command and control. In addition, in 2019, Mme. Dolidon, the expert from the CEREMA, and our research team presented the proposed emergency decision support system to the risk management department of two French cities: Orleans and Nantes. The latter was interested in the possibility to (i) recover information from their own geographical information system, (ii) send tasks to organisations that do not have access to the emergency decision support system, (iii) modify manually the model describing the crisis situation, (iv) adapt the response process to unexpected events, (v) adapt the algorithm of deduction to time constraints such as weekends or opening hours or (vi) to the available resources on the territory, (vii) customise the shape of a danger zone, (viii) prioritise the threats before the deduction of a response process.

Five points ((i, iii, iv, vii, viii)) are already available in the system and ((ii, v, vi)) have already been made possible. On demand, the system retrieves information from an external, open, geographical information system called OpenStreetMap ((i)). The system's components are loosely coupled and can easily be replaced by alternative, external implementations. This was, for example, tested with a to-do list mobile application ((ii)). The information contained in the common operational picture can be updated manually ((iii)). R-IOTA detects and adapts the ongoing response process to unexpected events ((vi)). The algorithm of deduction can adapt to any kind of constraints, as long as they correspond to modelled attributes ((v)). Another implemented algorithm of deduction, presented in Ref. [49], is dedicated to supply chain collaborations. It enables a response process to be deduced given the availability of resources and could be adapted to crisis situations ((vi)). A predefined shape of a danger can be specified within the interpretation rules ((vii)). Finally, the incidents and risks can be prioritised manually before the deduction of the response process ((viii)).

## 5.3. Quantified evaluation of the AIC information system

This section evaluates the ability of the proposed emergency deci sion support system to acquire, interpret, contextualise and communicate events in near real time. To this end, the interpretation and contextualisation times were measured, three times, on five diferent scenarios<sup>2</sup>. Table 5 presents, for each scenario, the number of events simulated, the frequency of emission, the number of activated rules and, among them, the number of contextualisation rules required to query the Neo4J graph database. These rules may, in fact, take longer to activate.

The time needed to interpret, contextualise and visualise the events received from R-IOSEMIT are presented in Table 6. The interpretation rules always interpreted raw events in under a second. The contextualisation rules, which query the situation model to detect all the environment components at stake in a danger zone, interpreted complex events in less than 3 s. All the complex events were then received and displayed on the common operational picture in less than a second. This evaluation thus confirms the AIC information system's ability to interpret and contextualise events to acquire several types of information, in near real time. In addition, all the events were correctly interpreted and correctly contextualised given the current crisis situa tion model.

Table 5  
The five scenarios that were used to test the implemented information system. Abbreviation: eyt. event. ctx. contextualisation

<table><tr><td></td><td>Events</td><td>Frequency</td><td>Rules</td><td>Ctx. rules</td></tr><tr><td>1</td><td>57</td><td>1 evt./ms</td><td>1</td><td>-</td></tr><tr><td>2</td><td>114</td><td>2 evt./ms</td><td>2</td><td>-</td></tr><tr><td>3</td><td>155</td><td>3 evt./ms</td><td>3</td><td>-</td></tr><tr><td>4</td><td>57</td><td>1 evt./ms</td><td>6</td><td>5</td></tr><tr><td>5</td><td>155</td><td>3 evt./ms</td><td>11</td><td>5</td></tr></table>

Table 6

The five scenarios that were used to test the implemented information system. Abbreviation: evt. event, ctx. contextualisation, int. interpretation.

<table><tr><td>Scenario:</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td colspan="6">Interpretation time delay (s)</td></tr><tr><td>Int. rules:</td><td>0.12</td><td>0.53</td><td>0.64</td><td>0.91</td><td>0.64</td></tr><tr><td>Ctx. rules:</td><td>-</td><td>-</td><td>-</td><td>2.25</td><td>1.83</td></tr><tr><td colspan="6">Visualisation time delay (s)</td></tr><tr><td>Int. rules:</td><td>0.06</td><td>0.20</td><td>0.39</td><td>0.72</td><td>0.28</td></tr><tr><td>Ctx. rules:</td><td>-</td><td>-</td><td>-</td><td>0.13</td><td>0.03</td></tr></table>

## 5.4. Results on the 4Vs of Big Data

All the components of the emergency decision support system architecture play a role in managing the 4Vs of Big Data. Table 7 sums up the efects of each component on the data and information that they processed. This concerns the metamodel (MM), the complex event processing (CEP) engine, the message broker (MB) and the common operational picture (COP).

On the first line of the results in Table 7, the metamodel makes it possible to control the variety and volume of information communicated to the emergency managers inside the crisis cells. The variety is limited by the finite number of concepts to be instantiated. The volume is limited by both the point of view and the perimeter applied during the modelling of the crisis situation. For example, a city will not obtain the same model as a state during a crisis response.

On the second line, the complex event processing engine succeeds in reducing, with each event processing agent, the volume and velocity of the event streams available on the ongoing crisis. As used in Refs. [23] and [25], the occurrence of one event can be used to improve the trustworthiness of another. All the complex event processing rules im plemented in the AIC information system are dictated by experts accustomed to crisis management in France. This ensures the veracity of the complex events, and, therefore, of the information added to the model of the crisis situation. Regarding the velocity on the information level, the complex event processing engine enables a near real time update of the common operational picture. This functionality was evaluated in the previous section.

On the third line, the message broker makes it possible to access a large variety and volume of event sources: this enhances the potential veracity of the information interpreted from them.

On the fourth line, the common operational picture enables the emergency managers to add, delete or update any information contained in the model of the crisis situation. This enhances the veracity of the information processed by the system. In addition, the volume and variety of the visible information can be adapted by the selection of layers.

To sum up, all the 4Vs of Big Data are managed by at least one of the components of the proposed architecture, on both the data level and the information level.

Table 7  
The role of the architecture components with regard to the 4Vs of Big Data.

<table><tr><td rowspan="2"></td><td colspan="4">Data</td><td colspan="4">Information</td></tr><tr><td>Volume</td><td>Variety</td><td>Velocity</td><td>Veracity</td><td>Volume</td><td>Variety</td><td>Velocity</td><td>Veracity</td></tr><tr><td>MM</td><td>-</td><td>-</td><td>-</td><td>-</td><td>x</td><td>x</td><td>-</td><td>-</td></tr><tr><td>CEP</td><td>x</td><td>-</td><td>x</td><td>x</td><td>-</td><td>-</td><td>x</td><td>x</td></tr><tr><td>MB</td><td>x</td><td>x</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>x</td></tr><tr><td>COP</td><td>-</td><td>-</td><td>-</td><td>-</td><td>x</td><td>x</td><td>-</td><td>x</td></tr><tr><td>Total</td><td>xx</td><td>x</td><td>x</td><td>x</td><td>xx</td><td>xx</td><td>x</td><td>xxx</td></tr></table>

## 5.5. Limits of the emergency decision support system

This paper introduces an emergency decision support system able to answer the research question, the business issue and the requirements of the French emergency managers presented in the Methodology section.

For the three levels of situation awareness (perception, comprehension and understanding), the system still lacks the ability to project the model of the current crisis situation into the near future. A new component could use (i) available forecasts and (ii) the events coming from the orchestration of the response process to obtain a model of the crisis situation which could be expected in the near future. In addition, a user interface could ofer emergency managers the possibility of testing ‘what-if’ scenarios. The projection of these models will generate models of the crisis situation that would be expected in the near future, if these events happened. The goal would be to use the same inter pretation and contextualisation rules.

## 6. Conclusion

During a crisis response, emergency managers need to take decisions. They need information and aim to coordinate heterogeneous and autonomous stakeholders. To help them, the research work presented in this paper aims to connect to the multiple data sources available to the crisis cells. The result is an emergency decision support system prototype. It merges an existing prototype, R-IOSUITE, with the AIC information system. Unlike existing literature, the AIC information system first enables R-IOSUITE to connect to topics in order to receive events from several heterogeneous sources. Then. it analyses the events with interpretation and contextualisation rules. The interpretation rules correspond to actual business rules. As a first contribution, the contextualisation rules query the graph database containing the model of the current crisis situation. This makes it possible to identify, from raw events, an area threatened by a danger and all the assets at risk in this area. New information is displayed in a common operational picture representing the crisis situation. In this way, the perception step of the emergency managers' situation awareness is supported in real time, as shown in our second contribution. In addition, the components of the proposed emergency decision support system manage at least one of the issues linked to the connection to new data sources. They control the volume, variety, velocity and veracity on both the data level (the events) and the information level (the model of the crisis situation).

The proposed system gives decision support systems the opportunity to enhance their users' situation awareness in real time, regardless of the complexity of their situation. The model-oriented approach avoids overloading them with too much information. For researchers working on other complex collaborations, such as logistics or healthcare, the layers of the implemented metamodel already enable them to add new interpretation and contextualisation rules to the system. For other researchers, all the XML files containing the metamodel, the deduction strategy, detection strategy, interpretation rules and contextualisation rules can easily be updated inside the system.

Finally, the emergency decision support system source code is available at http://r-iosuite.com/. It combines the AIC information system and the R-IOSUITE prototype. It is released with new func tionalities every 6 months.

## CRediT authorship contribution statement

Audrey Fertier: Writing - original draft, Software, Validation. Anne-Marie Barthe-Delanoë: Writing - review & editing, Supervision. Aurélie Montarnal: Writing - review & editing, Supervision. Sébastien Truptil: Writing - review & editing, Supervision. Frédérick Bénaben: Writing - review & editing, Supervision.

The three engineers (Nicolas Salatgé, Sébastien Rebière Pouyade and Julien Lesbegueries) of the industrial centre of IMT Mines Albi implemented the software. Guillaume Martin of the industrial center of IMT Mines Albi reviewed the paper. Andy Meehan of ALS-Immersion proofread the paper.

## Acknowledgments

We would like to thank the researchers and engineers from both our laboratories, along with our partners in the GéNéPi project.

## Funding sources

This work was supported by the French National Research Agency, through the GéNéPi funding project (program: Resilience and crisis management [DS0903] 2014) [grant number: ANR-14-CE28-0029].

## References

[1] W.A. Wallace, F. De Balogh, Decision support systems for disaster management, Public Administration Review 45 (1985) 134–146, https://doi.org/10.2307/ 3135008

[2] P. Lagadec, Learning processes for crisis management in complex organizations, Journal of Contingencies and Crisis Management 5 (1) (1997) 24–31, https://doi. org/10.1111/1468-5973.00034.

[3] D. Fogli, G. Guida, Knowledge-centered design of decision support systems for emergency management, Decision Support Systems 55 (1) (2013) 336–347, https:/ doi.org/10.1016/j.dss.2013.01.022.

[4] J. Bézivin, On the unification power of models, Software & Systems Modeling 4 (2) (2005) 171–188, https://doi.org/10.1007/s10270-005-0079-0

[5] M.R. Endsley, Toward a theory of situation awareness in dynamic systems, Human Factors: The Journal of the Human Factors and Ergonomics Society 37 (1) (1995) 32–64, https://doi.org/10.1518/001872095779049543

[6] G. D’Aniello, A. Gaeta, M. Gaeta, M. Lepore, F. Orciuoli, O. Troisi, A new DSS based on situation awareness for smart commerce environments, Journal of Ambient Intelligence and Humanized Computing 7 (1) (2016) 47–61, https://doi,org/10 1007/s12652-015-0300-0

[7] W. Boulila, I.R. Farah, A. Hussain, A novel decision support system for the interpretation of remote sensing big data, Earth Science Informatics 11 (1) (2018) 31–45, https://doi.org/10.1007/s12145-017-0313-7.

[8] G. Harerimana, B. Jang, J.W. Kim, H.K. Park, Health Big Data analytics: a technology survey, IEEE Access 6 (2018) 65661–65678, https://doi.org/10.1109 ACCESS.2018.2878254

[9] J. Wolbers, K. Boersma, The common operational picture as collective sensemaking, Journal of Contingencies and Crisis Management 21 (4) (2013) 186–199, https:/ doi.org/10.1111/1468-5973.12027

[10] A. Sagun, D. Bouchlaghem, C.J. Anumba, A scenario-based study on information flow and collaboration patterns in disaster management, Disasters 33 (2) (2009) 214–238. https://doi.org/10.1111/i.1467-7717.2008.01071.x

[11] P. Brereton, B.A. Kitchenham, D. Budgen, M. Turner, M. Khalil, Lessons from ap plving the systematic literature review process within the software engineering domain, Journal of Systems and Software 80 (4) (2007) 571–583, https://doi.org

10.1016/j.jss.2006.07.009.

[12] T. Steinmetz, U. Raape, S. Teßmann, C. Strobl, M. Friedemann, T. Kukofka, T. Riedlinger, E. Mikusch, S. Dech, Tsunami early warning and decision support, Natural Hazards and Earth System Sciences 10 (9) (2010) 1839–1850, https://doi. org/10.5194/nhess-10-1839-2010.

[13] D.B. Kirschbaum, T. Stanley, J. Simmons, A dynamic landslide hazard assessment system for Central America and Hispaniola, Natural Hazards and Earth System Sciences 15 (10) (2015) 2257–2272, https://doi.org/10.5194/nhess-15-2257-2015.

[14] A. Kassab, S. Liang, Y. Gao, Real-time notification and improved situational awareness in fire emergencies using geospatial-based Publish/Subscribe, International Journal of Applied Earth Observation and Geoinformation 12 (6) (2010) 431–438, https://doi.org/10.1016/j.jag.2010.04.001.

[15] B. Mohsin, F. Steinhäusler, P. Madl, M. Kiefel, An innovative system to enhance situational awareness in disaster response, Journal of Homeland Security and Emergency Management 13 (3) (2016) 301–327, https://doi.org/10.1515/jhsem-2015-0079.

[16] L.S. Santos, M.-A. Sicilia, E. Garcia-Barriocanal, Ontology-based modeling of efectbased knowledge in disaster response, International Journal on Semantic Web and Information Systems (LJSWIS) 15 (1) (2019) 102–118. https://doi,org/10.4018/ IJSWIS.2019010105.

[17] F. Calabrese, A. Corallo, A. Margherita, A.A. Zizzari, A knowledge-based decision support system for shipboard damage control, Expert Systems with Applications 39 (9) (2012) 8204–8211, https://doi.org/10.1016/j.eswa.2012.01.146.

[18] I. Marius, F. Kristin, K. Marianne, N. Salman, The level of automation in emergency quick disconnect decision making, Journal of Marine Science and Engineering 6 (1) (2018)17, https://doi.org/10.3390/imse6010017.

[19] M.L. Itria, M. Kocsis-Magyar, A. Ceccarelli, P. Lollini, G. Giunta, A. Bondavalli, Identification of critical situations via event processing and event trust analysis, Knowledge and Information Systems 52 (1) (2017) 147–178, https://doi.org/10. 1007/s10115-016-1009-x

[20] S. Wasserkrug, A. Gal, O. Etzion, Y. Turchin, Eficient processing of uncertain events in rule-based systems, IEEE Transactions on Knowledge and Data Engineering 24 (1) (2012) 45–58, https://doi.org/10.1109/TKDE.2010.204.

[21] I. Flouris, N. Giatrakos, A. Deligiannakis, M. Garofalakis, M. Kamp, M. Mock, Issues in complex event processing: status and prospects in the Big Data era, Journal of Systems and Software 127 (2017) 217–236, https://doi.org/10.1016/jjss.2016.06. 011 wOS:000397689000015.

[22] M. Lauras, F. Benaben, S. Truptil, A. Charles, Event-cloud platform to support de cision-making in emergency management, Information Systems Frontiers 17 (4) (2015) 857–869, https://doi.org/10.1007/s10796-013-9475-0.

[23] V. Mijović, N. Tomašević, V. Janev, M. Stanojević, S. Vraneš, Emergency manage ment in critical infrastructures: a complex-event-processing paradigm, Journal of Systems Science and Systems Engineering 28 (1) (2019) 37–62, https://doi.org/10. 1007/s11518-018-5393-5.

[24] S.V. Kovalchuk, E. Krotov, P.A. Smirnov, D.A. Nasonov, A.N. Yakovlev, Distributed data-driven platform for urgent decision making in cardiological ambulance control, Future Generation Computer Systems 79 (2018) 144–154, https://doi.org/10. 1016/j.future.2016.09.017.

[25] A.-M. Barthe-Delanoë, A. Montarnal, S. Truptil, F. Bénaben, H. Pingaud, Towards the agility of collaborative workflows through an event driven approach — application to crisis management. International Journal of Disaster Risk Reduction 28 (2018) 214–224. https://doi.org/10.1016/i.jidrr.2018.02.029

[26] Kwang-Eun Ko. Kwee-Bo Sim. Development of context aware system based on Bavesian network driven context reasoning method and ontology context modeling 2008 International Conference on Control, Automation and Systems, 2008, pp. 2309–2313.. https://doi.org/10.1109/ICCAS.2008.4694191.

[27] K.-E. Ko, K.-B. Sim, Context aware system based on Bayesian network driven context reasoning and ontology context modeling, International Journal of Fuzzy Logic and Intelligent Systems 8 (4) (2008) 254–259. https://doi,org/10.5391/LJFIS.2008 8.4.254.

[28] E. Miguelanez, P. Patron, K.E. Brown, Y.R. Petillot, D.M. Lane, Semantic knowledge-based framework to improve the situation awareness of autonomous underwater vehicles, IEEE Transactions on Knowledge and Data Engineering 23 (5) (2011) 759–773. https://doi.org/10.1109/TKDE,2010.46.

[29] N. Baumgartner, S. Mitsch, A. Müller, W. Retschitzegger, A. Salfinger, W. Schwinger, A tour of BeAware — a situation awareness framework for contro centers, Information Fusion 20 (2014) 155–173, https://doi.org/10.1016/j.infus. 2014.01.008.

[30] J. Gómez-Romero, M.A. Serrano, J. García, J.M. Molina, G. Rogova, Context-based multi-level information fusion for harbor surveillance, Information Fusion 21

(2015) 173–186, https://doi.org/10.1016/j.infus.2014.01.011

[31] N. Sanchez-Pi, L. Martí, J.M. Molina, A.C. Bicharra García, Information fusion for improving decision-making in Big Data applications, in: F. Pop, J. Kołodziej, B. Di Martino (Eds.), Resource Management for Big Data Platforms: Algorithms, Modelling, and High-Performance Computing Techniques, Computer Communications and Networks, Springer International Publishing, Cham, 2016, pp. 171–188, , https://doi.org/10.1007/978-3-319-44881-7\_9.

[32] N. Sanchez-Pi, L. Martí, J.M. Molina, A.C.B. Garcia, Ontology definition and cognitive analysis in Occupational Health and Security (OHS) environments, Proceedings of the 30th Annual ACM Symposium on Applied Computing, SAC ’15, ACM, New York, NY, USA, 2015, pp. 201–206, , https://doi.org/10.1145/2695664. 2695891.

[33] R. Pearson, M.P. Donnelly, J. Liu, L. Galway, Generic application driven situation awareness via ontological situation recognition, 2016 IEEE International Multi Disciplinary Conference on Cognitive Methods in Situation Awareness and Decision Support (CogSIMA), 2016, pp. 131–137, , https://doi.org/10.1109/COGSIMA. 2016.7497800.

[34] A.V. Smirnov, A.M. Kashevnik, A. Ponomarev, Context-based infomobility system for cultural heritage recommendation: tourist assistant — TAIS. Personal and Ubiquitous Computing 21 (2) (2017) 297–311, https://doi.org/10.1007/s00779- 016-0990-0.

[35] A. Smimov, A. Kashevnik, T. Levashova, M. Pashkin, N. Shilov, Situation modeling in decision support systems, 2007 International Conference on Integration of Knowledge Intensive Multi-Agent Systems, 2007, pp. 34–39, , https://doi.org/10. 1109/KIMAS.2007.369781.

[36] K. Alexopoulos, K. Sipsas, E. Xanthakis, S. Makris, D. Mourtzis, An industrial Internet of Things based platform for context-aware information services in man: ufacturing, International Journal of Computer Integrated Manufacturing 31 (11) (2018) 1111–1123. https://doi,org/10.1080/0951192X,2018.1500716.

[37] P. Grace, B. Pickering, M. Surridge, Model-driven interoperability: engineering heterogeneous IoT systems, Annals of Telecommunications 71 (3) (2016) 141–150, https://doi.org/10.1007/s12243-015-0487-2.

[38] D. Chen, G. Doumeingts, F. Vernadat, Architectures for enterprise integration and interoperability: past, present and future, Computers in Industry 59 (7) (2008) 647–659, https://doi.org/10.1016/j.compind.2007.12.016.

[39] T.R. Gruber, A translation approach to portable ontology specifications, Knowledg Acquisition 5 (2) (1993) 199–220, https://doi.org/10.1006/knac.1993.1008.

[40] A. Gómez-Pérez, Evaluation of ontologies, International Journal of Intelligent Systems 16 (3) (2001) 391–409, https://doi,org/10.1002/1098-111X(200103) 16:3≤391::AID-INT1014>3.0.CO:2-2

[41] M. Lauras, S. Truptil, F. Bénaben, Towards a better management of complex emergencies through crisis management meta-modelling, Disasters 39 (4) (2015) 687–714, https://doi.org/10.1111/disa.12122.

[42] A. Boin, A. McConnell, Preparing for critical infrastructure breakdowns: the limits of crisis management and the need for resilience, Journal of Contingencies and Crisis Management 15 (1) (2007) 50–59, https://doi.org/10.1111/j.1468-5973. 2007.00504.x.

[43] F. Tonnies, C.P. Loomis, C.P. Loomis, Community and Society, Routledge, 2017, https://doi.org/10.4324/9781315080871.

[44] P.T. Eugster, P.A. Felber, R. Guerraoui, A.-M. Kermarrec, The many faces of Publish/Subscribe. ACM Computing Surveys 35 (2) (2003) 114–131, https://doj org/10.1145/857076.857078.

[45] W. Mu, F. Bénaben, H. Pingaud, Collaborative process cartography deduction based on collaborative ontology and model transformation. Information Sciences 334-335 (2016) 83–102, https://doi,org/10.1016/i,ins.2015.11.033

[46] W. Mu, F. Benaben, H. Pingaud, An ontology-based collaborative business service selection: contributing to automatic building of collaborative business process, Service Oriented Computing and Applications 12 (1) (2018) 59–72. https://doj org/10.1007/s11761-018-0229-1.

[47] N. Boissel-Dallier, F. Benaben, J.-P. Lorré, H. Pingaud, Mediation information system engineering based on hybrid service composition mechanism, Journal of Systems and Software 108 (2015) 39–59. https://doi,org/10.1016/i,iss,2015.05 064.

[48] A.-M. Barthe-Delanoë, S. Truptil. F. Bénaben, H. Pingaud. Event-driven agility of interoperability during the run-time of collaborative processes, Decision Support Systems 59 (2014) 171–179, https://doi.org/10.1016/i.dss.2013.11.005

[49] R. Oger, F. Bénaben, M. Lauras, B. Montreuil, Towards decision support automation for supply chain risk management among logistics network stakeholders, IFAC-PapersOnLine 51 (11) (2018) 1505–1510, https://doi.org/10.1016/j.ifacol.2018. 08.287.
