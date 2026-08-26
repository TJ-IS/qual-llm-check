---
otero_id: 20513
otero_key: "KNV3VKX5"
title: "scenario modeling for government big data governance decision-making: Chinese experience with public safety services"
authors: "Zhao-ge LIU; Xiang-yang LI; Xiao-han ZHU"
year: "2022"
journal: "Information & Management"
doi: "10.1016/j.im.2022.103622"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# scenario modeling for government big data governance decision-making: Chinese experience with public safety services

![](/api/attachments/KNV3VKX5/fulltext/images/27f53daa608338bdcfbeba2fe9e06b762a520457134a6cb58cfdddc41d1235c5.jpg)

Zhao-ge LIU <sup>a,b,\*</sup>, Xiang-yang LI <sup>a</sup>, Xiao-han ZHU <sup>a,c</sup>

<sup>a</sup> No. 13, Fayuan Street, School of Management, Harbin Institute of Technology, Harbin 150001, China

<sup>b</sup> No. 422, Siming South Rd, School of Public Affairs, Xiamen University, Xiamen, 361005, China

<sup>c</sup> No. 777, Gaoxin Avenue, Government Service and Big Data Management Bureau of Wuhan Optics Valley District, Wuhan 430075, China

## A R T I C L E I N F O

Keywords: Government big data governance Scenario-based decision-making Scenario modeling Model-driven Data link network Public safety services

## A B S T R A C T

In the public safety service context, government big data governance (GBDG) is a challenging decision-making problem that encompasses uncertainties in the arenas of big data and its complex links. Modeling and collab orating the key scenario information required for GBDG decision-making can minimize system uncertainties. However, existing scenario-building methods are limited by their rigidity as they are employed in various application contexts and the associated high costs of modeling. In this paper, using a design science paradigm, a model-driven scenario modeling approach is proposed to achieve flexible scenario modeling for various appli cations through the transfer of generic domain knowledge. The key component of the proposed approach is a scenario meta-model that is built from existing literatures and practices by integrating qualitative, quantitative, and meta-modeling analysis. An instantiation mechanism of the scenario meta-model is also proposed to generate customized scenarios under Antecedent-Behavior-Consequence (ABC) theory. Two real-world safety service cases in Wuhan, China were evaluated to find that the proposed approach reduces GBDG decision-making un certainties significantly by providing key information for GBDG problem identification, solution design, and solution value perception. This scenario-building approach can be further used to develop other GBDG systems for public safety services with reduced uncertainties and complete decision-making functions.

## 1. Introduction

## 1.1. Background

Government public safety departments increasingly collect and use various big data to improve public safety services (e.g., infectious dis ease transmission analysis, building fire risk prediction, and water logging response), which results in the increasing use of Big Data Algorithmic Systems (BDAS) [[15], [21]]. However, the BDAS of public safety services relies heavily on the use of data combined from various sources, some owned by other government departments, others controlled by non-governmental organizations, yet others controlled by citizens. Without control over the ownership, quality and compliance of these data, BDAS would be too risky to be ensured with effective deci sion support for public safety services. Hence, public safety departments have increasingly turned to government big data governance (GBDG) as a means to exercise control over the ownership and quality of such data and over compliance with legal and ethical requirements to maximize value and minimize risk. This has helped improve the effects of public safety service BDAS [[18], [41]]. Decision-making is the key to effective GBDG as this directly determines if reasonable solutions will resolve noteworthy problems related to a specific service (e.g., data rights, data protection, business process problems) [[9], [24]].

Previously, safety services did not generally involve many large data items and GBDG decision-making tended to center on specific types of data such as geospatial or social media text data [10]. Meanwhile, various GBDG solutions (e.g., data sharing mechanisms, organizational structures, legal procedures, and data processing techniques) have been proposed for the effective use of these big data [[39], [11]]. With the rapid development of the smart city, an increasing number of big data items have been developed for implementation of more precise and efficient public safety services. Smart waterlogging risk analysis in Wuhan city, China, for example, currently involves both common geo spatial data (e.g., roads, buildings, and water systems) and novel big data items such as travel data, social media posts, and base station data, as well as the derived items of these base data [49]. This vast array of interlinked data items impacts GBDG decision-making due to inherent, complex uncertainties such as GBDG problems, environmental con straints (at organizational, regulatory, infrastructure, and device levels) and service-related features such as processes, input/outputs, data owners, and goals [4]. By contrast, scenario-based analysis is a reason able alternative, because it can help reduce the decision-making un certainties by systematically modeling and communicating real GBDG scenarios [26]. Herein, a scenario represents a comprehensive descrip tion of the status of various information elements (e.g., services, prob lems, environments, and solution effects) that can affect decision-making outcomes [[47], [31]]. The benefits of scenario-based decision-making are discussed in 2.1.

![](/api/attachments/KNV3VKX5/fulltext/images/9a18ba766cf211c415276559bc27f9783d0e35d07bbd08c9f99e6093282fa131.jpg)  
Fig. 1. Scenario framework for GBDG decision-making in public safety services. Four kinds of scenario elements are incorporated, i.e. public safety services and DLN, GBDG problems, solutions, and environment. The dotted arrows indicate that GBDG problems, solutions and environment influence safety service effects through their associations with DLN. The thick arrows represent the order of recognizing the elements, e.g., the identification of GBDG problems is based on the recognition of services and environment.

An important research question addressed in this study is how to effectively represent GBDG scenarios to minimize complex GBDG decision-making uncertainties in public safety services. Scenario models that are built using traditional approaches (e.g., framework-based or ontology-based modeling) are context-dependent rather than dynami cally adaptive to novel application contexts [[48], [12]]. As GBDG scenarios are generally composed of a variety of dynamic scenario ele ments and inter-element associations, the rebuilding of scenario models in a new context will dramatically increase the costs of modeling and relevant decision system development [[2], [30]]. By contrast, a more flexible approach is to build scenario models from generic domain knowledge. According to model-driven architecture, this can be ach ieved by constructing a domain meta-model that can incorporate various disparate and partial domain models, and by designing a mechanism to instantiate the meta-model in various real contexts [[14], [32]]. A key objective of this study is to design a flexible model-driven scenario modeling scheme for the GBDG decision-making of public safety services.

## 1.2. Design science as a research method

This study was conducted within the design science research (DSR) paradigm, which has been widely used for developing and evaluating IT artifacts in the public administration context [43]. Generally, DSR methodology includes: identifying problem and motivation, defining objectives of a solution, design and development, demonstration, eval uation, and communication [[37], [36]]. The design objective of this study was to craft a model-driven GBDG scenario-building scheme by constructing a scenario meta-model incorporating generic scenario el ements and their associations, and by providing an instantiation mechanism of the meta-model. First, the meta-model was built using four classes of generic elements (that are related to services, environ ment, problems, and solutions) that were extracted from the current literature and practices. Next, four associated components were deter mined to specify the instantiation process of the meta-model, and included: (1) inputting service and environment details, (2) identifying GBDG problems, (3) designing GBDG solutions, and (4) selecting and evaluating a solution. Finally, the proposed scheme was evaluated rigorously based on two real public safety service cases in China. The case studies allowed development of other GBDG systems for public safety services with reduced uncertainties and complete decision-making functions.

This study makes several important theoretical contributions. This study presents a novel scenario-building approach for GBDG decisionmaking in public safety services. The key component of this approach is a scenario meta-model that was built using a model-driven method to represent, transfer, and store the generic domain knowledge of scenariobuilding. The meta-model was accompanied by an instantiation mech anism for generating specific scenarios in various real contexts, addressing the difficulty of effective scenario representation under massive decision-making uncertainties. The evaluation using two case studies validated the scenario-building applicability, indicating that the method design benefits of a DSR approach. This study has important practical implications. The meta-model can be used as a representation of the generic domain knowledge offering solutions and reducing the costs of rebuilding scenario models in various application contexts. In addition, the analysis of the case studies makes practitioners aware of some important issues associated with scenario-building for effective GBDG problem identification, solution design, and solution value evaluation.

The remainder of this paper is organized according to DSR [36]. First, a review of extant research on scenario-based analysis and model-driven approaches is given. The GBDG scenario framework of public safety service is then defined, followed by the design of the model-driven scenario modeling approach around the key components. A thorough evaluation of the proposed approach is presented, followed by a brief discussion and conclusions.

## 2. Related work

## 2.1. Scenario-based GBDG decision-making

Scenario-based analysis has been increasingly applied to decisionmaking processes in uncertain environments [[26], [25], [44]]. A sce nario model can be designed to incorporate key information elements (scenario elements) in the decision-making process and the structural associations between them [27]. Here, the scenario elements and their associations are extracted from domain knowledge [29]. The model can be then instantiated to describe real scenarios with increased informa tion support and reduced uncertainties, which benefits clear and effec tive decision-making. The model can also be shared among relevant organizations for collective decision-making [44]. Scenario-based analysis has been used to facilitate decision-making for various public safety services including earthquake preparedness, fire hazard identifi cation, and waterlogging responses [[27], [42], [34]].

Scenario-based decision-making has been preliminarily discussed in terms of GBDG, with a particular focus on the selection of key scenario elements. For example, Soares [40] proposed that GBDG solutions should be developed per applicable scenarios to make full use of their advantages, and defined three common scenario elements: big data types (e.g., social media and geospatial data), GBDG problems (e.g., data quality and data protection), and applicable domains (e.g., healthcare and disaster management). Abraham et al [1]. extended this work by incorporating the environment constraints (e.g., organizational, regu latory, infrastructure-related) with the performance effects and risk management of GBDG solutions. Janssen et al [19]. further argued that GBDG should center not solely on the data, but on the data link network (DLNs) and links between them. It can be seen that the scenario elements provided by existing studies are too fragmented to comprehensively describe a GBDG scenario; key scenario elements are likely to be missing in real contexts.

In this study, GBDG scenario elements are systematically extracted from domain knowledge according to the necessary information for major GBDG decision-making processes. They are divided into four classes: public safety services and their DLN. environment characteristics, GBDG problems, and GBDG solutions, which are then illustrated in Fig. 1. The identification of problems within these classes requires a clear understanding of real-world safety services and their DLN condi tions, as well as environmental characteristics [1]. The GBDG solution design relies on problem elements and must satisfy specific environment constraints [[20], [5]]. The GBDG solution selection centers on potential improvements to service effects and the reduced cost of designed solu tions [23].

## 2.2. Model-driven solution to flexible scenario modeling

By developing a meta-model for a specific domain, the scenarios of that domain in different application contexts can be modeled flexibly. This is the key concept behind model-driven approaches [[14], [32]]. Model-driven methods were first proposed for software engineering, where meta-models (i.e.. generic models that represent domain knowl. edge) have been employed to configure extensive tools, processes, and content to swiftly develop software systems [6]. The meta-models pro vided by model-driven approaches can help clarify generic scenario el ements and their associations to map various scenario models for developing decision-making support systems [28]. Representative sce nario meta-model construction methods include Unified Modeling Language (UML), Common Warehouse Meta-model (CWM), and Meta-Object Facility (MOF).

Othman and Beydoun [34] developed a scenario meta-model for disaster management based on a four-layer MOF framework including numerous instantiation layers. Yu et al [45]. employed UML to construct a general platform independent model (PLM) for enterprise Web ser vices to support the use of scenario meta-models and decision-support systems in different organizations. Model-driven methods have been adopted in decision-making across various other domains, including IT outsourcing and the development of Internet Applications [[38], [16]]. Based on their abovementioned advantages, a model-driven method is adopted in this study for flexible GBDG scenario-modeling. A four-layer meta-model MOF framework is used to model scenarios with various degrees of instantiation.

Traditional model-driven approaches assume that instances of sce nario elements (e.g., DLNs and environmental details) can be directly obtained from the real world [[17], [34]]. However, due to the complexity of GBDG scenarios, certain instances can only be generated through associations with other scenario elements. For example, the identification of GBDG problems is based on DLN conditions and related organizations, infrastructures, and regulations. The GBDG solutions are designed according to identified GBDG problems and are under the constraints of both DLN conditions and environmental factors [35]. In such a situation, the lack of an effective instantiation mechanism of scenario elements is likely to produce missing data which would affect the performance of GBDG scenario models. Antecedent-Behavior-Consequence (ABC) theory explains scenario recognition process in an orderly way by dividing it into three sequential stages, i.e., antecedent input, behavior design, and consequence analysis. Herein, antecedents refer to the factors that affect behaviors, behaviors indicate the focused decisions (i.e., the GBDG solutions in this paper), and consequences of the behaviors are presented to facilitate the decision-making (Nickols et al., 2021; [46]). By applying ABC theory, the relationships between different kinds of scenario elements can be clarified, and thus reasonable and orderly instantiation of scenario models can be achieved. Hence, an instantiation mechanism was designed in this study based on ABC theory [46] and GBDG decision-making framework [1], and the instantiation process was divided into three stages: antecedent input, solution design, and solution effect analysis.

## 3. Scenario framework for GBDG decision-making in public safety services

A scenario is a comprehensive description of the status of various information elements (called scenario elements) that affect decisionmaking outcomes [[47], [31]]. In the GBDG domain, scenario ele ments can be divided into four key classes according to their functions in major decision-making processes: problem identification, solution design, and solution selection [[18], [18], [1]].

## Public safety services and their DLN

During GBDG decision-making, problem identification relies on the details of public safety services and their DLN. For example, the iden tification of data-quality-related problems centers on the data status (e. g., data precision and fault-tolerance) in the DLN; process redundancy is associated with the DLN structure. Moreover, service effects (e.g., disaster prediction precision and service time length) are often key in dicators of problem consequences.

## The GBDG environment

Both GBDG problem identification and solution design in the public safety service context are constrained by various environmental char acteristics such as regulations, organizational structures, infrastructures, and budget restrictions. For example, General Data Protection Regula tion (GDPR) [13] has explicit requirements regarding data rights (e.g., data queries and usage) in terms of citizens’ personal data; these re quirements must be considered during GBDG solution design to ensure that solutions are applicable in European countries.

![](/api/attachments/KNV3VKX5/fulltext/images/16f76e72287a29c300efb3a0a07356d894a63869643f82d04796d8ce3be31609.jpg)  
Fig. 2. Model-driven scenario modeling architecture for GBDG decision-making in public safety services. In the process of scenario meta-modeling, a meta-mode that contains the generic domain knowledge is developed, which is context-independent. The meta-model is then instantiated in real application contexts to provide the key scenario information for reducing the uncertainties in GBDG decision-making and thus improving decision-making efficiency.

## GBDG problems

GBDG solution design manages identified problems, so the problems must be fully and precisely understood. For example, in terms of process redundancy, the focus of GBDG solution design should be the adjustment of service processes and corresponding DLN structures. For data-rightsrelated problems, organizational activities such as authorizations may be involved.

## GBDG solutions

A thorough recognition of available GBDG solutions is necessary for solution evaluation and selection. Unlike decision-making in other do mains. GBDG decision-makers often find it difficult to perceive the value of GBDG solutions in terms of service improvement [7]. They are also sensitive to potential costs such as cross-department coordination dif ficulties or authorization anxiety [23]. Scenario elements related to GBDG solutions should be highlighted throughout the GBDG decision-making process.

Based on the abovementioned scenario elements and their relation ships, the scenario framework for GBDG decision-making is constructed in Fig. 1. The GBDG “scenario” concept is defined as follows:

A GBDG scenario is a carefully constructed and systematic snapshot of information elements that influence GBDG decision-making, i.e. public safety services (and their DLN), GBDG problem details, environment constraints (e. g., organizations, infrastructures, and regulations) and GBDG solutions and their associations. Scenario recognition minimizes uncertainties in GBDG decision-making (problem identification, solution design, and solution se lection) with the support of continuous, comprehensive, and precise scenario related information.

## 4. Designing a model-driven scenario modeling scheme to GBDG decision-making

It is difficult but necessary for GBDG practitioners of public safety services to deal with the various decision-making uncertainties across large sets of data and their complex links. Under massive uncertainties, an organized presentation of targeting scenarios is crucial in GBDG or ganization decision-making, especially when the organization lacks domain knowledge. Considering the different scenario elements in various application contexts, a model-driven scenario-building scheme that can flexibly generate scenario models using generic domain knowledge may produce greater efficiency and control costs [[14], [32]]. To design the model-driven scenario modeling approach, a sce nario meta-model was constructed that incorporated the generic domain knowledge, and then an operational process was designed employing the meta-model to generate the key scenarios in real contexts based on the ABC theory and GBDG decision-making framework. The overall process of the proposed approach is shown in Fig. 2.

## 4.1. GBDG scenario meta-modeling

For the purpose of this research, a GBDG scenario meta-model was developed to provide generic knowledge for scenario modeling. Agent Modeling Language (AML) was used to develop the scenario meta-model [[34], [8]]. This process involved first extracting the general scenario elements that were relevant to all available GBDG scenario models (or other relevant models that contain scenario elements, including GBDG influencing factor models, GBDG evaluation models, and GBDG decision-making framework). Next, the candidate scenario elements were short-listed. The differences between the scenario elements at hand were reconciled. Finally, the associations between the scenario elements were identified. A preliminary step was taken in this case to identify existing GBDG scenario models and other relevant models that were deemed influential. The influences of a reference model were estimated in terms of model acceptance (indicated by citations of the model), publisher influence (indicated by the impact factor of the publisher), and model applicability (as indicated by the number of main contexts in which the model is applicable).

Based on the identified models, the scenario elements were encoded using the framework analysis function provided by NVivo software [33]. In this process, only general scenario elements were shortlisted for in clusion into the scenario meta-model. Moreover, a reconciliation process between the scenario elements from the different source models was employed to produce the scenario meta-model shown here. Specifically, for each element, a hybrid definition was given when there were mul tiple definitions from different sources. For example, the “regulation' has been defined as data-level rules such as data right ownership in Liu and Li [26] and as multi-level rules such as organizations and metadata stan dards in Abraham et al [1].. The modeling definition is ‘the data governance rules of different levels including organization and data management’, which is a hybrid definition that encompasses both in terpretations. In other words, the scenario elements of the meta-model were based on finding a consensus between various expert opinions that were encapsulated in the models. The associations between the identified scenario elements were finally extracted in a similar manner.

![](/api/attachments/KNV3VKX5/fulltext/images/12742a1a5b687d3b6a656c89ba7b773ae7c06bf9253d3c44d372844f66a201a7.jpg)  
Fig. 3. Service scenario meta-model: A basic representation. Core element class is marked in orange. This model is composed of the key generic service elements in GBDG decision-making. (Extended service meta-model is shown in Appendix A.).

![](/api/attachments/KNV3VKX5/fulltext/images/3308998d79aa2801cfbe2237f90610414407aec73eea8130da5b18de899e74ba.jpg)  
Fig. 4. Environment scenario meta-model: A basic representation. Core element class is marked in orange. This model consists of the key generic environment elements in GBDG decision-making. (Extended environment meta model is shown in Appendix B.).

Due to the complexity of scenario elements and their associations, the GBDG scenario model was developed from parts to the whole. Specif ically, the four components that describe partial scenarios (e.g., services and DLN, GBDG environment, problems and solutions) were developed, and then integrated as the scenario model was instantiated for GBDG decision-making. (The process is discussed in detail in SubSection 4.2.)

## Scenario meta-model component 1: service

As shown in Fig. 3, the core class in the service scenario meta-model is DataLink, which defines the data link where service scenario elements are operationalized. All the key scenario elements describing public safety services and their DLN are aggregated within DataLink element and include DataLinkGoal, DataLinkTask, Channel, PrecedenceDataLink, EstimatedTime and ServiceEffect. DataLinkTask represents the collections of tasks (e.g., data collection, sharing and analysis) implemented by Organization to realize DataLinkGoal. Channel defines the ways available (e.g., information platforms, phone calls and social media) to complete DataLinkTask. EstimatedTime describes the general time spent to com plete DataLinkTask and is an important indicator of service effects. ServiceEffect defines safety service performance indicators that reveal the consequences of GBDG problems and the value of GBDG solutions.

The service scenario meta-model shown in Fig. 3 is a basic model that only presents key, generic service information relevant to GBDG decision-making. In practical applications, other elements (e.g., data input/outputs, meta-data standards, data quality, data protection mea sures) may be supplemented according to context at hand. A reference to the extended service scenario meta-model is presented in Appendix A.

## Scenario meta-model component 2: environment

As shown in Fig. 4, the core class in environment scenario metamodel is Environment, which represents the overall environment sta tus. Specifically, GBDG environment is composed of organizational environment, regulation environment, and infrastructure environment, which are described by OrganizationalEnvironment, Regulations, and In frastructures in the meta-model. respectively. The organizational environment is further divided into safety service organization and data right division. In the environment meta-model, ServiceOrganization represents the leading party of a public safety service and determines whether GBDG solutions should be adopted to improve the service ef fects. DataGovernanceTeam defines the governmental GBDG team and is responsible for identifying GBDG problems and providing Service Organization with reasonable GBDG solutions for decision-making. DataRightDivision describes how the relevant data rights in a safety service are allocated among organizations, which follows specific rules (defined by Regulations) and organizational structures (defined by ServiceOrganization). Infrastructures are divided into hard infrastructures (data collection devices, data use platforms, and data processing tech niques) and soft (data standards) categories.

## Scenario meta-model component 3: problem

The elements and their associations in the meta-model vary ac cording to the problem to-be-solved, so typical GBDG problems were extracted before developing the proposed meta-model. Seven general problems and 21 detailed problems concerning safety service GBDG decision-making were finally extracted and presented in Table 1. We focus here on two typical GBDG problems, “data rights non-availability” and “process redundancy”; the corresponding meta-models are shown in Fig. 5(a) and Fig. 5(b), respectively. It can be seen that the core class in the problem scenario meta-model is the elements that exist the problem, e.g., the UnavailableDataRight of data rights non-availability problem and the RedundantProcess of process redundancy problem. Problem Definition identifies whether the problem exists. AssociatedDataLink de fines the data links that are associated with the problem. These data links also belong to the DataLink class that has been defined in the ser vice meta-model.

GBDG problem identification relies on information regarding services and environments. so there are associations between relevant meta-model components (Fig. 6). Specifically, the GBDG problem is identified based on the features of DLN structures (See the details in Appendix D). The indicators of problem consequences should be consistent with those of safety service effects to fully reflect their impact. On the contrary, environment constraints should be considered in problem identification. For example, DataRightDivision supports the recognition of the data rights non-availability by providing detailed features (e.g., the owners of unavailable data rights). The safety service organization generally characterizes the demand side for unavailable data rights.

Table 1  
GBDG problems and potential influences on public safety services.

<table><tr><td>General problem categories</td><td>Detailed problems</td><td>Potential influences on public safety services</td></tr><tr><td rowspan="3">GBDG organization</td><td>Data right non-availability</td><td>Process redundancy; time waste; inaccurate decision-making...</td></tr><tr><td>Excessive data rights</td><td>Data security threats; non-compliance with regulations...</td></tr><tr><td>Organization missing</td><td>Process inefficiency; coordination difficulties...</td></tr><tr><td rowspan="3">Service process</td><td>Process redundancy</td><td>Time waste; resource waste; decision-making failure...</td></tr><tr><td>Process missing</td><td>Inaccurate decision-making; process inefficiency...</td></tr><tr><td>Process inefficiency</td><td>Time waste; resource waste; inaccurate decision-making...</td></tr><tr><td rowspan="3">Data quality</td><td>Weak data precision</td><td>Decision-making biases; insufficient capacity for realizing precise services...</td></tr><tr><td>Weak fault-tolerance</td><td>Service interruption; time waste...</td></tr><tr><td>Weak fitness (to process)</td><td>Resource waste; data storage waste; inaccurate decision-making...</td></tr><tr><td rowspan="3">Meta-data standard</td><td>Standard missing</td><td>Data sharing difficulties; decision-making biases...</td></tr><tr><td>Excessive standards</td><td>Coordination difficulties; excessive investment...</td></tr><tr><td>Compliance check missing</td><td>Data management monitoring difficulties; data quality problems...</td></tr><tr><td rowspan="3">Data security</td><td>Regulation missing</td><td>Data leakage; (data protection) technique missing; service interruption caused by external invasion...</td></tr><tr><td>Excessive regulations</td><td>Process redundancy; process inefficiency; time waste...</td></tr><tr><td>Technique missing</td><td>Insufficient capacity for preventing external invasion and data leakage behaviors...</td></tr><tr><td rowspan="2">Data lifecycle</td><td>Delayed data updating</td><td>Decision-making failure; inaccurate decision-making...</td></tr><tr><td>Data destruction missing</td><td>Insufficient data storage; resource waste...</td></tr><tr><td rowspan="4">Data storage and infrastructure</td><td>Insufficient data storage</td><td>Insufficient capacity for decision-making based on large scale data; Insufficient capacity for long-term analysis...</td></tr><tr><td>Lack of data processing technique</td><td>Data integration difficulties; data quality problems...</td></tr><tr><td>Lack of data collection devices</td><td>Restricted data types; process inefficiency; time waste...</td></tr><tr><td>Lack of data use platforms</td><td>Process inefficiency; insufficient capacity for identifying data values...</td></tr></table>

Note: The 7 general GBDG problems and 21 detailed problems concerning safety service GBDG decision-making were extracted from: Benfeldt et al., [7]; Janssen et al., [18]: Abraham et al., [1]: Al-Ruithe et al., [5]: Alhassan et al.. [4]: Liu et al., [25]; Silva et al., [39]; and Alhassan et al., [3].

## Scenario meta-model component 4: solution

The scenario elements and their associations in the solution metamodel are identified according to specific problems (in this case, data rights non-availability and process redundancy), as shown in Figs. 7(a) and 7(b), respectively. The core element is the adopted solutions of dealing with targeting GBDG problems, e.g., the DataRightChange of data rights non-availability problem, and the ProcessChange of process redundancy problem. DataLinkChange defines the possible DLN struc tures after adopting the solution. LeadingParty represents the main party implementing the solution, and Cooperator represents other organiza tions cooperating with the leading party. SolutionEffect and Cost define the safety service effects and the costs (e.g., financial costs and time costs) of the adopted solution, respectively.

## 4.2. Scenario model instantiation for GBDG decision-making

An instantiation mechanism of the GBDG scenario model is proposed here based on ABC theory [46] and the GBDG decision-making frame work [1]. The instantiation process is divided into three stages: input ting antecedents (services, problems, and environment), solution design, and solution effect analysis (Fig. 8). The operation includes four basic steps: 1) inputting service and environment details, 2) identifying GBDG problems, 3) designing GBDG solutions, and 4) selecting and evaluating a solution.

## Step 1. Input of service and environment

Both GBDG problem identification and solution design require in formation regarding the targeted service and related environment. The scenario model instantiation thus begins with the service meta-model and environment meta-model. Public safety service processes are con verted into DLN form (Fig. 1), then status data of the scenario elements describing the DLN (e.g., data link tasks) and relevant environment are collected.

## Step 2. GBDG problem identification

The aim of this process is to instantiate the problem meta-model by identifying GBDG problems with instantiated service and environment meta-models. The key to problem identification is the ProblemDefinition element embedded in the problem meta-model, which reveals whether a GBDG problem exists according to service-related and environmental information. The mechanisms for identifying data rights nonavailability and process redundancy problems are discussed in Subsec tion 4.1.3.

## Step 3. GBDG solution design

GBDG solutions must be designed with scenario information related to GBDG problems as well as the relevant services and environment. The other three meta-models should be instantiated before the solution meta-model. To design applicable solutions, we gathered the possible DLN changing plans and relevant details (e.g., organizational support of both the leading party and cooperators, as well as their tasks).

## Step 4. Solution evaluation and selection

When there are multiple candidate GBDG solutions, decision-makers can evaluate the value of each according to their estimated effects and costs, then isolate the one most likely to improve the safety service. Supported by the instantiated solution meta-model, decision-makers, and cooperating parties can comprehensively understand the selected solution(s) for effective implementation.

## 5. Evaluation: GBDG scenario modeling in real-world publi safety services

The scenario meta-model developed in this study is generic and in cludes various scenario elements that can be refined according to the public safety services at hand. We anticipate that the various scenario elements in GBDG, their associations, and different types of instantiated models can provide comprehensive and precise decision support as per the instantiation mechanism of the scenario meta-model. To test this approach, we use two real-world public safety decision-making cases in Wuhan, China: a daily safety service (fire hazard identification) demonstrative of the data rights non-availability problem and an emergency service (waterlogging risk analysis) demonstrative of the process redundancy problem, where data rights division are constrained by regional regulations.

![](/api/attachments/KNV3VKX5/fulltext/images/a54243c2a9b84307933bdd13ee71bfb25b4ed79a9a0c7f6d0991e5536e001fb3.jpg)  
a) Data right non-availability

![](/api/attachments/KNV3VKX5/fulltext/images/3875f75fe3e27cde50f12aa41770d7e5d9cd3deafae42d8900f216de0105c8c8.jpg)  
b) Process Redundancy

Fig. 5. Problem scenario meta-model: A basic representation. Core element classes are marked in orange. This model is composed of the key generic problem el ements in GBDG decision-making and focuses on two typical GBDG problems, i.e. “data rights non-availability” and “process redundancy”. (Extended problem meta model is shown in Appendix C.).  
![](/api/attachments/KNV3VKX5/fulltext/images/5cfac1e176c78b7ee6bcc3604b641ea1adb29be5ef8804dde9670b12610b9798.jpg)  
Fig. 6. Key associations between problem meta-model and other meta-model components. The elements in problem meta-model that are associated with those in other meta-models are marked in light red.

## 5.1. Key indicators for evaluating the scenario-based decision-making scheme

The proposed scenario modeling approach is expected to provide informational support for major decision-making functions, i.e., GBDG problem identification, solution design, and solution value perception. Key indicators of the proposed method’s performance are as follows.

## Problem identification function

Traditional GBDG decision-making centers on the development of GBDG solutions rather than the identification of problems [[26], [22]].

Here, problem identification is incorporated into the indictors used to evaluate our approach: (1) speed and (2) detailed presentation of problems and their impacts on services.

## Solution design guidance

Generally, a series of potential solutions is designed to manage identified problems. Users lacking experience with solution design may obtain a reference solution to guide them through the process. More over, for the developed solutions, an analysis about whether the solu tions are applicable in the application contexts should be presented to avoid negative results, e.g., invalid solution implementation and con flicts with regional regulations. In addition, the details of each solution should be shown to stakeholders as well to facilitate implementation.

![](/api/attachments/KNV3VKX5/fulltext/images/1656247e1eb33bfd241ee84b74b8eeef5e6cd1eb6bca7e4083b99accc9896c4e.jpg)  
a) Solution to data right non-availability

![](/api/attachments/KNV3VKX5/fulltext/images/2b250d545559008220aa1e51da60024616793a7d17604713a8574653b2cf9e7f.jpg)  
b) Solution to process redundancy

Fig. 7. Solution scenario meta-model: A basic representation. Core element classes are marked in orange. Key, generic solution elements approach two typical GBDG problems, data rights non-availability and process redundancy. (Extended solution meta-model is shown in Appendix E.).  
![](/api/attachments/KNV3VKX5/fulltext/images/43543b953b3d561a93afca09ee7dc72f82894af8d9b305f511f2991be9ba7e49.jpg)  
Fig. 8. Instantiation mechanism of GBDG scenario model based on ABC theory and GBDG decision-making framework. The aim of this mechanism is to achieve the reasonable and orderly instantiation of scenario models because a number of instances can only be generated through the associations with other scenario elements.

## Solution value perception

According to previous studies [7], one of the main factors that impede GBDG solutions from implementation is the difficulty of expressing their potential value as real-world services. Their value can be defined according to improvement to services and the attached costs. This information also helps to select the optimal solutions. Accordingly, a clear presentation of these specific values is incorporated into our evaluation.

## 5.2. Use case 1: fire hazard identification in wuhan (Daily safety service)

Daily fire hazard identification plays a critical role in reducing the occurrence of fire incidents. In 2017, the National Fire Department of China published a document that required prefecture-level and above cities to realize preliminary smart fire risk management before 2018. Since then, Chinese city governments have successively established their own big data platforms for analyzing regional fire risk.

In Wuhan, urban fire hazards are typically defined in three ways: (1) dangerous buildings, which are identified by type, usage time, and fire prevention devices installed; (2) risky buildings that overuse electricity as per the power department’s regular reports; and (3) community fire hazards such as damaged fire safety facilities, illegal construction of buildings, and occupied fire exits from textual reports provided by cit izens through social media. The fire department can use these identifi cations to prevent fire incidents. The detailed process of this service and its DLN are shown in Fig. 9.

Unstructured interviews were used to elucidate the issues related to GBDG efforts in this safety service, especially the scenario-building

![](/api/attachments/KNV3VKX5/fulltext/images/7da6bb14bdba92b3b478c5bf5a130f9a3649ed5809c640bf1ee6bd3466f08b23.jpg)  
Fig. 9. Service process and DLN of daily fire hazard identification in Wuhan. Focused urban fire hazards include dangerous buildings, buildings with risky human behaviors, and various community fire hazards reported by citizens. Some steps are simplified due to limited space. Arrows represent data links; black dots represent data inputs and data outputs.

![](/api/attachments/KNV3VKX5/fulltext/images/1f69bad9b054ae7309b029e239cef23b6746c5d3de5e5d43fe1ccf556fab838e.jpg)  
Fig. 10. Instantiated service meta-model and environment meta-model of daily fire hazard identification in Wuhan. \*Service time refers to the estimated time required for completing the service.  
\*Accuracy refers to the percentage of fire hazards that have been correctly identified.

effects. Interviews were conducted four times from June 2019 to January 2020, with the first focusing on the information collection for the service and environment scenario elements, the second focusing on the problem identification effects, the third focusing on the service ef fects after adopting the GBDG solution, and the fourth focusing on the improvement of the scenario modeling scheme. Respondents included government officials and data governance experts. Four researchers took part in the interviews, with two leading the questions, and the others preparing additional discussions. The interviews were recorded and then transcribed.

![](/api/attachments/KNV3VKX5/fulltext/images/1c578e15256e47e0308cffcc1ea8b24ebcf8d334415173907bbfca82f0196a28.jpg)  
Fig. 11. Instantiated problem meta-model and solution meta-model of the fire hazard identification in Wuhan. This use case focused on Data right non-availability problem and the accompanied Process redundancy problem. The solution deals with the problems by coordinating with relevant departments for sharing data query rights and then reducing redundant data links for optimizing the DLN structure.

This safety service involves data sharing between multiple de partments, which is mostly accomplished manually and thus is generally inefficient. A direct solution to this inefficiency is to empower the fire department to query relevant data (dangerous buildings, risky behav iors) to minimize data-sharing time. However, the empowerment of data rights is an organizational problem constrained by relevant regulations; the GBDG decision-making requires a comprehensive understanding of various scenario elements and their associations. The proposed scenario model was applied to support GBDG decision-making for this service. First, an instantiated service meta-model and environment meta-model were generated according to the service process, corresponding DLN, and relevant environment details as shown in Fig. 10.

The instantiated models provide a clear description of the scenario elements in this case regarding the DLN and environmental features. For example, in the service scenario meta-model, service time length and accuracy (i.e., the percentage of fire hazards correctly identified) can be used as performance indicators according to ServiceEffect. Another element instantiation sample centers on regulations and infrastructures, where data-sharing tasks must follow requirements defined in Wuhan Government Data Management Regulation. Supported by the scenario in formation, scenario-modeling for GBDG decision-making functions can be conducted as shown below.

## Result 1. : GBDG problem identification

The GBDG problem in this service was identified based on the in formation provided by the instantiated service and environment metamodels. An instantiated problem meta-model that presents the prob lem details was generated as shown in Fig. 11. The data rights nonavailability problem can be identified directly from the service and DLN features based on the mechanisms listed in Appendix E. The un available data rights are the query rights of dangerous building records (owned by the construction bureau) and the records of buildings with risky behaviors (owned by the power department). The crossdepartment sharing of these data significantly increases the service time of fire hazard identification and is likely to delay the treatment of fire hazards. After empowering the fire department with query rights, new possible data links corresponding to service processes are produced. The accompanying process redundancy should be addressed. In this process, the optimal DLN can be selected according to service time and accuracy.

## Result 2. : GBDG solution design

A reference solution to the aforementioned problems was designed based on the key information provided by the instantiated problem and environment meta-models. An instantiated solution meta-model solu tion details was generated as shown in Fig. 11. This reference solution improves service effects via coordination among relevant governmental departments to share data query rights with the Wuhan fire department, followed by a reduction in redundant data links to optimize the DLN structure. The applicability of the solution was verified by checking for compliance with Wuhan Government Data Management Regulation, which is supported by element associations between the instantiated solution and environment models. Details of the designed solution (e.g., leading party, cooperators, and data link changes) were comprehensively incorporated with the instantiated solution scenario elements.

## Results 3. : GBDG solution evaluation and selection

According to the instantiated solution scenario elements, a report of service effect improvements and potential costs of the designed solution was generated. As shown in Fig. 12, sharing related data query rights allows the hazard identification accuracy to remain unchanged while reducing service time for the Wuhan fire department from 190 min to 20 min. In this case, fire hazard identification can be updated every 20 min. Accordingly, the number of identification result updates is increased from 7 to 72 per day. This GBDG solution does not increase any financial or temporal costs; it only requires the coordination of Wuhan fire department with other departments to share data query rights. Based on key information provided by the solution scenario elements, decisionmakers and stakeholders can communicate effectively to implement solutions. As the director of Wuhan fire department said, the solution presents high value of facilitating smart fire risk management.

![](/api/attachments/KNV3VKX5/fulltext/images/a5ad30e2e8f14235c70d02739c85a447c8d71e14760e4460c396a31015d4f578.jpg)  
Fig. 12. Fire hazard identification service performance in Wuhan before versus after GBDG solution adoption. Left and middle panels show service process and DLN of fire hazard identification after solution implementation. Right panel shows effects and costs of the solution.

![](/api/attachments/KNV3VKX5/fulltext/images/0d31aa15c4b2d70132cefaa7d0e7852c84e44137fa6c63b0c7e30cf0bcb7559b.jpg)  
Fig. 13. Service process and DLN of waterlogging risk analysis in Wuhan, including risk of pedestrians being trapped and risk of vehicles being trapped. Five de partments provide various big data for precise analysis. Arrows represent data links; black dots represent data inputs and data outputs.

## 5.3. Use case 2: waterlogging risk analysis in wuhan (Emergency service)

Dynamic analysis of city-wide waterlogging risk is a prerequisite for timely and effective waterlogging response measures. Due to rapid ur banization and industrial development, all kinds of impermeable land surface $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ as construction land) in Wuhan have expanded quickly, which heavily increases the risk of waterlogging. To improve water logging response capability, the Wuhan East Lake High-Tech Develop ment Zone has established an emergency response center (ERC) and big data platform for waterlogging risk analysis. The platform allows for comprehensive analysis of waterlogging risk by aggregating the big data from various sources, e.g., the meteorological department, water department, traffic administrator, and telecommunication sector.

This process includes (1) analyzing the risk of pedestrians being trapped based on rainfall, drainage systems, geological data, population heat maps, and other relevant data and (2) analyzing the risk of vehicles being trapped based on traffic flow and the waterlogging situation on individual roads. The ERC publishes key waterlogging risk information in a timely manner to guide citizens to adjust their travel plans as needed. This public safety service and its DLN are illustrated in Fig. 13.

Similarly, unstructured interviews were conducted three times from January to June 2019 to define the effects of scenario-building on GBDG decision-making. The first interview dealt with assembling service and environment information, the second interview focused on the effects of problem identification, and the third interview dealt with collecting feedback about the effects of the GBDG solution. The scenario modeling scheme was improved based on the first use case (see details in Section 5.4), and thus this case focused more on the evaluation of the scheme. Specifically, respondents included the officials of the involved sectors (e. g., ERC, water department, and telecommunication sector), and the experts in data governance. Three researchers took part in the interview. The problems of the proposed scenario modeling scheme were also recorded and discussed for continuous improvement.

First, instantiated service and environment meta-models of the safety service were generated by identifying the statuses of relevant scenario elements, as shown in Fig. 14. The DLN of this public safety service also involves data interaction between multiple departments. The ideal GBDG solution secures the most efficient possible use of time by adjusting data rights division and optimizing the DLN structure. How ever, the solution in this case is constrained by the regulatory environ ment. Specifically, Wuhan Government Data Management Regulation stipulates three data-sharing rules: open to the public, conditionally shared, or not shared. Drainage-pipe-related data falls under the “not shared” rule, so links L3-L5 can only be realized by Wuhan water department via its affairs information platform. Telecommunications, social media, and traffic flow data are all “conditionally shared". The sharing of telecommunications and social media data requires an ano nymization process (represented by links L9 and L11), whereas traffic flow data can only be shared at the emergency response stage. Rainfall data is “open to the public” and can be freely obtained online without permission from the meteorological department. Under these regula tions, the division of data rights apart from rainfall queries is basically fixed; to this effect, it is difficult to significantly improve service effects through data rights adjustment.

## Result 1. : GBDG problem identification

Process redundancy in the Wuhan waterlogging risk analysis case was identified based on the DLN-related information provided by the instantiated service and environment meta-models. The corresponding problem meta-model was instantiated as shown in Fig. 15. Process redundancy problems in this service include the following. First, the rainfall data is “open to the public” and can be queried by the water department directly. Currently, however, it is queried by the meteoro logical department and then shared with the water department, which wastes service time. Second, the data anonymization of telecommuni cation and social media data before data sharing is irrelevant to waterlogging risk analysis and further wastes service time.

## Result 2. : GBDG solution design

A reference solution was designed for the two process redundancy problems as shown in Fig. 15. First, rainfall data is directly collected by the water department rather than shared from the meteorological department. Second, the population heat map and road waterlogging situation analyses are implemented in the telecommunication sector, then shared with the ERC. Population heat map and road waterlogging situation items do not contain personal information and thus do not need to be anonymized, which can conserve service time. In this case, regu latory constraints of regulations have already been considered based on the scenario information provided by the instantiated environment meta-model.

## Results 3. : GBDG solution evaluation and selection

The effects and costs of the solution supporting decision-making were determined based on information provided by the instantiated solution meta-model. As shown in Fig. 16, reengineering the safety service process brings the average waterlogging risk analysis time from 30 min down to 20 min (a 33.3% reduction). As every minute is crucial in the waterlogging disaster response, the designed solution greatly enhances efficiency and has significant GBDG value. The implementa tion of this GBDG solution only involves rainfall data interface con struction and a small adjustment to the service process, which are relatively inexpensive. Redundant data links in DLN (i.e., the sharing of rainfall data and the anonymization of telecommunications and social media data) are deleted, which conserves financial and communication costs as well.

## 5.4. An improved meta-model of model-driven GBDG scenario-building

The original model-driven GBDG scenario-building scheme was validated by the case studies, with the exception of the final component. The continuous improvement function of the final component is under development. The case studies appear to show that the solution to a GBDG problem such as the unavailability of data rights can also cause other GBDG problems, such as process redundancy. In the case studies, the solution to data right non-availability was shown in use case 1, and process redundancy was illustrated in use case 2. The findings indicated that modifications of the original scenario meta-model were needed so it better meets the requirements of continuous improvement.

GBDG is a kind of complex system engineering that involves imple mentation of various associated GBDG problems (see Table 1 for de tails). The scenario meta-model of a specific problem can be viewed as a sub-model. For example, one sub-model could target at unavailable data rights and another sub-model could deal with the associated process redundancy. The potential associations between sub-models should be constantly explored, which facilitates the continuous improvement of GBDG decision-making and the construction of an interconnected sce nario meta-model based on the updating of the problem definition element Fig. 17. shows an improved scenario meta-model of modeldriven GBDG scenario-building.

## 6. Discussion

## 6.1. Applicability of the proposed scenario modeling approach

Various GBDG decision-making uncertainties are introduced by big data items in public safety services. The proposed approach yields contextual GBDG scenario models that embed various elements (service, problem, environment, and solution) and their associations, which re veals key GBDG decision-making processes.

## Decision-making process 1: GBDG problem identification

The problem meta-model is embedded with problem definition ele ments that reveal whether specific problems exist in services based on the DLN features (provided by the instantiated problem meta-model) and GBDG environment (provided by the instantiated environment meta-model). A comprehensive description of the identified problems is generated for decision-making based on the scenario elements of the instantiated problem meta-model. We focus here on the identification mechanism of two typical GBDG problems, data rights non-availability, and process redundancy. By updating the problem definition elements, the proposed approach can be used to characterize complex GBDG

![](/api/attachments/KNV3VKX5/fulltext/images/8ed1348dfbeb5f256bac159457bb01038fe13bb88e8c2780751e89ebd0a52115.jpg)  
Fig. 14. Instantiated service meta-model and environment meta-model of waterlogging risk analysis in Wuhan. \*Service time refers to the estimated time required for completing the service  
\*Accuracy refers to the percentage of the area where waterlogging risk has been correctly predicted.

![](/api/attachments/KNV3VKX5/fulltext/images/004dd83bf65192c08fde2e0189786c72f60911a21eea6a847b23639ca30f5205.jpg)  
Fig. 15. Instantiated problem meta-model and solution meta-model of the waterlogging risk analysis in Wuhan. This use case focused on Process redundancy problems as data right division was constrained by governmental regulations. The solution deals with the problems by reducing redundant data links for optimizing the DLN structure.

![](/api/attachments/KNV3VKX5/fulltext/images/2aeafcf147ae2d04959d4b8ad8e062da32e3f937201b128cb8b218579dceb11a.jpg)  
Fig. 16. Performance of waterlogging risk analysis service in Wuhan before versus after adopting GBDG solution. Left and middle panels show service process and DLN of waterlogging risk analysis after implementing the solution. Right panel reports effects and costs of the solution.

![](/api/attachments/KNV3VKX5/fulltext/images/26d23a915f2e1e7b08ffa6eab658847ce9c2fdaa44a7e3995595a1cefb5ef354.jpg)  
Fig. 17. An improved meta-model of model-driven GBDG scenario-building.

problems.

Decision-making process 2: GBDG solution design

For typical GBDG problems, the solution meta-model can be embedded with various generic solution elements (e.g., possible tasks, leading party and cooperators, and data link adjustments) and their associations as extracted from existing GBDG research. According to the instantiated problem meta-model, generic solution elements can be instantiated to provide informational support for GBDG solution design. The instantiated service and environment elements encompass constraints on the solution design, which can prevent problematic sce narios such as non-compliance with existing regulations or imple mentation difficulties.

## Decision-making process 3: GBDG solution selection

The scenario elements of the effects and costs of designed solutions are also described in the solution meta-model and provide key evidence of the optimal solution. Customized indicators of solution effects (e.g., service time and accuracy) and solution costs (e.g., financial, commu nication, and time), and their associations with the DLN, are defined in the solution sub-model. The instantiated effects and costs of the designed solution can be generated according to the DLN related sce nario elements after adopting the solution. The adjusted safety service process, DLN, and a report (Figs. 13 and 17) of the effects and costs of the solution are also generated to help decision-makers to clearly recognize its principle and value.

## 6.2. Key strengths of the proposed approach

Our case study shows that the proposed scenario-based method re alizes multiple GBDG decision-making processes under complex un certainties by presenting the required scenario information. Decisionmakers not only can identify GBDG problems according to the DLN and environment features, but also analyze the effects and costs of a safety service before and after adopting a GBDG solution. This reveals the consequences of GBDG problems and the value of GBDG solutions. Previous GBDG studies have tended to center on GBDG solutions (including the overall decision-making framework and detailed solu tions to data rights division, process improvements, and multi-source data integration); few have considered the problem identification and solution selection processes necessary for effective solution design. This may lead to unclear and even incorrect understanding of the conse quences of potential GBDG problems and the effects of designed solu tions, which significantly affects GBDG decision-making outcomes [[26], [23]].

The proposed approach also has high flexibility and generality due to its model-driven architecture, which extracts generic scenario elements and their associations from existing GBDG scenario models and other relevant models (e.g., GBDG decision-making frameworks and GBDG influencing factor models). We construct a GBDG scenario meta-model that can be flexibly instantiated in different application contexts at a reasonable cost. More importantly, using a generic scenario meta-model as the key component in decision-making system design minimizes any repeat definitions of scenario elements and their associations to swiftly establish decision-support systems. Traditional scenario modeling methods such as framework-based and ontology-based modeling are generally developed for specific service contexts, so their scenario models are difficult to deploy in novel contexts [[44]. [12]].

The GBDG decision-making processes progresses through recogni tion of the DLN and environment, GBDG problem identification, solution design, and solution selection. An instantiation mechanism for the sce nario meta-model is incorporated in the proposed approach to achieve the reasonable and orderly generation of scenario instances, which effectively retains all key scenario elements. The proposed method drives GBDG problem identification based on the problem definition element embedded in the scenario meta-model, which encompasses the rules for identifying specific GBDG problems according to the DLN features.

## 7. Conclusions and future work

A flexible GBGD scenario modeling scheme is developed in this study to minimize complex uncertainties in GBDG decision-making by securing the required scenario information. The key component is a scenario meta-model that is established via a model-driven approach. This model provides a generic representational layer and unified view of common scenario elements in the GBDG decision-making process for various safety services. A consensus developed from existing GBDG scenario models and literature is the basis of the knowledge encapsu lated in the scenario elements that constitute the scenario meta-model. The proposed model is embedded with an instantiation mechanism based on ABC theory and the GBDG decision-making framework for reasonable, orderly generation of scenario instances in different appli cation contexts as per the decision-making sequence. Daily fire hazard identification and emergency waterlogging risk analysis in Wuhan were chosen as case studies to test the proposed method. We showed that key scenario information in the GBDG decision-making process (i.e., prob lem identification, solution design, and solution evaluation and selec tion) can be effectively modeled and instantiated to minimize uncertainties and improve decision-making efficiency.

This work contributes to the scenario analysis literature by empiri cally showing the effectiveness of modeling and communicating required scenario information in the GBDG decision-making of typical public safety services. A comprehensive presentation of scenario infor mation is essential for public safety service GBDG decision-making to minimize the complex uncertainties involved in big data items and their links. From the scenario recognition perspective, the proposed approach supports the rapid identification of GBDG problems in a given safety service and reveals optimal GBDG solutions accordingly.

A scenario meta-model that contains generic domain knowledge is also developed that can be instantiated flexibly in various application contexts, which is a further extension of existing scenario modeling approaches. The proposed approach is compatible with emerging GBDG solutions and can continuously support GBDG decision-making. For countries and regions with successful GBDG cases in public safety ser vices, the proposed approach can be applied to describe and share the experience contained therein as guidance for other regions to solve similar problems. We believe that this work may lead to more efficient and adaptive GBDG decision-making schemes even in worst-case con ditions such as scenario information incompleteness, noisy data, or invalid information.

This work is not without its limitations. The first limitation is that both the case studies were conducted in Wuhan. Wuhan has better big data governance than many others because of its powerful data support and mature data governance organization, with two typical GBDG problems existing. Future work should include other types of public safety services or different cities with different problem scenarios to provide a more comprehensive approach to understanding the contri butions of multiple components. Hence, extensive research is encour aged on other GBDG problem scenarios, such as data quality, data security, and their combinations, using the proposed scenario modeling approach and the decision-making processes outlined herein. The effects of the GBDG problem identification in the proposed method is also partially dependent on the comprehensiveness of the problem definition elements in the scenario meta-model. Future researchers are encouraged to investigate the identification mechanisms of various GBDG problems and their combinations to build corresponding problem definition elements.

We would like to offer some policy recommendations. First, practi tioners should consider conducting scenario analysis prior to making GBDG decisions for public safety services, as this helps to communicate the key information necessary for clear decision-making. Second, prac titioners should prioritize GBDG problem identification during GBDG decision-making as it determines the evaluation and selection of corre sponding solutions, and thus affects the performance of those solutions. Details regarding the DLN and environment constraints should be taken into account. Third, service effect improvements and potential costs attached to a GBDG solution should be carefully analyzed as they determine whether the solution is applicable. Finally, GBDG projects should be given careful attention as big data becomes an inextricable part of public safety services.

## Author biography

## Author 1: zhaoge liu

Zhaoge Liu is an Assistant Professor in the School of Public Affairs at Xiamen University in China. His-research interests are governmental data governance, public safety services and emergency management. He has published in some international journals, such as Knowledge-based Systems, Food Control, Fire Technology, Operational Research, and Natural Hazards Review.

Author 2: xiangyang li

Xiangyang Li is a Professor in the School of Management at Harbin Institute of Technology. His-research interests are digital government, data governance and emergency management. He has over 100 journal publications in a number of international journals including Expert Systems with Applications, Knowledge-based Systems, Safety Science, Operational Research and others.

## Author 3: xiaohan zhu

Xiaohan Zhu is currently the head of Government Service and Big Data Management Bureau in the Optics Valley District of Wuhan, China. He is also a PhD student at Harbin Institute of Technology. His-research interests are digital government, urban governance and emergency management. He has published in some international journals, such as Natural Haz ards Review and Geomatics and Information Science of Wuhan University.

## Author statement

The detailed description of authors’ diverse contributions is illus trated as follows.;Zhao-ge LIU: Conceptualization, Methodology, Soft ware, Validation.; Xiang-yang LI: Supervision, Writing - Reviewing and

Editing, Funding acquisition.; Xiao-han ZHU: Data Curation, Validation.

## CRediT authorship contribution statement

Zhao-ge LIU: Conceptualization, Methodology, Software, Valida tion. Xiang-yang LI: Supervision, Writing – review & editing, Funding acquisition. Xiao-han ZHU: Data curation, Validation.

## Declaration of Competing Interest

None.

## Acknowledgments

This work is supported by the Major Research Project of Nation Natural Science Foundation of China named “Big data Driven Manage ment and Decision-making Research” (No. 91746207), the General Program of Nation Natural Science Foundation of China (No. 71774043), the Emergency Management Major Research Project of Nation Natural Science Foundation of China (No. 91024028) and the General Program of Social Science Foundation of Hubei Province (No. 2019051).

## Appendix A. Extended representation of the service scenario meta-model

Extended representation of the service scenario meta-model is shown in Fig. 18

![](/api/attachments/KNV3VKX5/fulltext/images/7bbebb8027fdd6986f03e0981f9132ef7de450c981a4323ee12ca82d6cb2db84.jpg)  
Fig. 18. Service scenario meta-model: An extended representation. This model is an extension of the basic model shown in Fig. 3, with more detailed service el ements presented.

Appendix B. Extended representation of the environment scenario meta-model

Extended representation of the environment scenario meta-model is shown in Fig. 19

![](/api/attachments/KNV3VKX5/fulltext/images/60dd56af721c0730fb9abfec1896ca5c06186bab94fe2b201b27a997207aae84.jpg)  
Fig. 19. Environment scenario meta-model: An extended representation. This model is an extension of the basic model shown in Fig. 4, with more detailed envi ronment elements presented.

## Appendix C. Extended representation of the problem scenario meta-model

Extended representation of the problem scenario meta-model is shown in Fig. 20

![](/api/attachments/KNV3VKX5/fulltext/images/020c15676c4a52e2ffcdecabe9296165a256dc0eb2c94e9362ef32b254fd2c17.jpg)  
Fig. 20. Problem scenario meta-model: An extended representation. This model is an extension of the basic model shown in Fig. 5, with more detailed problem elements presented. Similarly, this model focuses on the two typical GBDG problems, i.e. Data right non-availability and Process redundancy.

Appendix D. The DLN structures and explanations of typical GBDG problems

<table><tr><td>Problem type</td><td>DLN structure</td><td>Explanation</td><td>Instance</td></tr><tr><td rowspan="3">Data right non-availability</td><td>O1 O2a t1 &gt; Th(a)</td><td>The cross-organization data sharing (of a) takes much more time (i.e. t1) than expected (i.e. Th), which affects the efficiency of public safety services.</td><td>Citizens have to go to different departments for corresponding services as the data is not well shared, which wastes a lot of time.</td></tr><tr><td>(a)</td><td>There is more than one time of data sharing, which means the communication between the organizations takes a lot of time and leads to the inefficiency of government service.</td><td>A service requires coordination of other organizations because the data rights are not available, e.g., healthcare departments may have to consult home office (in UK) about whether a foreigner has the qualification for getting healthcare services, as they do not have access to the relevant data.</td></tr><tr><td>(b)</td><td>More than one way exists between two same data items (i.e. a and b) with each way completed by one or multiple data links, which will cause a waste of resources.</td><td>Repetitive analysis of the fire hazards of a region using different methods, e.g.,1) City government analyzes city-wide fire hazards and deliver the results to the regional government.2) Regional government analyzes the fire hazards within the region.</td></tr><tr><td rowspan="3">Process redundancy</td><td>(a)</td><td>There is more than one way for obtaining b with each way completed by several data links, and the ways are independent with each other.</td><td>Governments have several ways for analyzing waterlogging risk during a rainstorm, e.g.,1) Deducing possible scenarios through Naïve Bayes method;2) Obtaining real-time conditions from social media platforms (such as Weibo).</td></tr><tr><td>(c)</td><td></td><td></td></tr><tr><td>(d)</td><td></td><td></td></tr></table>

Appendix E. Extended representation of the solution scenario meta-model

Extended representation of the solution scenario meta-model is shown in Fig. 21  
![](/api/attachments/KNV3VKX5/fulltext/images/350807ef0013c56a6a72ddce95407b026570b21f4186f096857b5233fbc7469d.jpg)  
Fig. 21. Solution scenario meta-model: An extended representation. This model is an extension of the basic model shown in Fig. 7, with more detailed problem elements presented. This model also focuses on the solutions to two typical GBDG problems, i.e. Data right non-availability and Process redundancy. 18

## References

[1] R. Abraham, J. Schneider, J. vom Brocke, Data governance: a conceptual framework, structured review, and research agenda, Int J Inf Manage 49 (2019) 424-438.

[2] P.A. Akiki, P.A. Akiki, A.K. Bandara, Y.J. Yu, EUD-MARS: end-user development of model-driven adaptive robotics software systems, Sci Comput Program 200 (2020), 102534, https://doi.org/10.1016/j.scico.2020.

[3] I. Alhassan, D. Sammon, M. Daly, Data governance activities: an analysis of the literature, Journal of Decision Systems 25 (2015) 64–75.

[4] I. Alhassan, D. Sammon, M. Daly, Data governance activities: a comparison between scientific and practice-oriented literature, Journal of Enterprise Information Management 31 (2018) 300–316.

[5] M. Al-Ruithe, E. Benkhelifa, K. Hameed, A systematic literature review of data governance and cloud data governance, Pers Ubiquitous Comput 23 (2019) 839–859.

[6] E. Bagheri, A.A. Ghorbani, UML-CI: a reference model for profiling critica infrastructure systems, Information Systems Frontiers 12 (2010) 115–139.

[7] O. Benfeldt, J.S. Persson, S. Madsen, Data governance as a collective action problem. Information Systems Frontiers 22 (2020) 299–313.

[8] B. Beydoun, G. Low, H. Mouratidis, B. Henderson-Sellers, A security-aware metamodel for multi-agent systems (MAS), Inf Softw Technol 51 (2009) 832–845.

[9] P. Brous, M. Janssen, Trusted decision-making: data Governance for creating trust in data science decision outcomes, Adm Sci 10 (2020), https://doi.org/10.3390/ admsci10040081.

[10] N. Clark, F. Guiffault, Seeing through the clouds: processes and challenges for sharing geospatial data for disaster management in Haiti, International Journal of Disaster Risk Reduction 28 (2018) 258–270

[11] B.A. Cumbie, C.S. Sankar, Choice of governance mechanisms to promote information sharing via boundary objects in the disaster recovery process, Information Systems Frontiers 14 (2012) 1079–1094.

[12] J. Du, H. Jing, K.R. Choo, V. Sugumaran, D. Castro-Lacouture, An ontology and multi-Agent based decision support framework for prefabricated component supply chain, Information Systems Frontiers (2019), https://doi.org/10.1007/s10796- 019-09941-x.

[13] European Union, New European Interoperability Framework – Promoting Seamless Services and Data Flows For European public administrations. Resource document. European Union, Luxembourg, 2017. https://ec.europa.eu/isa2/sites/isa/files/eif\_ brochure\_final.pdf. Accessed 25 August 2020.

[14] J. Evora, J.J. Hernandez, M. Hernandez, Advantages of Model Driven Engineering for studying complex systems, Nat Comput 14 (2015) 129–144.

[15] A. Hassan Zadeh, H.M. Zolbanin, R. Sharda, et al., Social media for nowcasting flu activity: spatio-temporal big data analysis, Information Systems Frontiers 21 (2019) 743–760.

[16] J.N. Hermida, S. Hermida, A. Montoyo, J. Gomez, ´ Applying model-driven engineering to the development of Rich Internet Applications for Business Intelligence, Information Systems Frontiers 15 (2013) 411–431.

[17] G.I. Hernandez, A.A.J. Fuente, J.E. Labra-Gayo, et al., Knowledge-based public service transactions: an intelligent model-driven approach in co-learning contexts, Comput Human Behav 51 (2015) 1032–1041.

[18] M. Janssen, H. van der Voort, Agile and adaptive governance in crisis response: lessons from the COVID-19 pandemic, Int J Inf Manage (2020), https://doi.org/ 10.1016/j.ijinfomgt.2020.102180.

[19] M. Janssen, P. Brous, E. Estevez, et al., Data governance: organizing data for trustworthy Artificial Intelligence, Gov Inf Q (2020), https://doi.org/10.1016/j giq.2020.101493.

[20] M. Janssen, Y. Charalabidis, A. Zuiderwijk, Benefits, adoption barriers and myths of open data and open government, Information Systems Management 29 (2012) 258-268.

[21] M. Janssen, D. Konopnicki, J.L. Snowdon, et al., Driving public sector innovation using big and open linked data (BOLD). Information Systems Frontiers 19 (2017) 189-195.

[22] M. Janssen, J. van den Hoven, Big and open linked data (BOLD) in government: a challenge to transparency and privacy? Goy Inf Q 32 (2015) 363–368.

[23] B. Klievink, B.J. Romijn, S. Cunningham, H. de Bruijn, Big data in the public sector: uncertainties and readiness, Information Systems Frontiers 19 (2017) 267–283

[24] T. Koltay, Data governance, data literacy and the management of data quality, IFLA Journal 42 (2016) 303–312.

[25] C. Liu, J. Qian, D. Guo, Y. Liu, A spatio-temporal scenario model for emergency

[26] Z. Liu, X. Li, Full view scenario model of big data governance in community safety service, in: in Proceedings of the 8th International Conference on Information Communication and Management - ICICM ’18, ACM Press, Edinburgh, 2018, pp. 44–49.

[27] Z. Liu, X. Li, X. Zhu, Joint risk assessment of the secondary disasters of rainstorms based on multi-source spatial data in Wuhan. China. Natural Hazards Review (2020), https://doi.org/10.1061/(ASCE)NH.1527-6996.0000403.

[28] M. Lycett, E. Marcos, V. Storey, Model-driven systems development: an introduction. European Journal of Information Systems 16 (2007) 346–348.

[29] X.Y. Ma, Y.Z. Sun, H.L. Fang, Y. Tian, Scenario-based multiobjective decisionmaking of optimal access point for wind power transmission corridor in the load centers. JEEE Transactions on Sustainable Energy 4 (2013) 229–239.

[30] J. Malý, M. Neˇcaský, Model-driven approach to modeling and validating integrity constraints for XML, with OCL, and Schematron. Information Systems Frontiers 12 (2015) 917–946.

[31] A. Martelli, Scenarios in decision-making, in: A. Martelli (Ed.), Models of Scenario building and Planning, Springer, New York, 2014, pp. 202–223.

[32] I. Mundi, M.M.E. Alemany, A. Boza, R. Poler, A model-driven decision support system for the master planning of ceramic supply chains with non-uniformity of finished goods, Studies in Informatics and Control 22 (2013) 153–162.

[33] NVivo (Non-numerical unstructured data indexing searching & theorizing), Qualitative Data Analysis Program, QSR International Pty Ltd, Melbourne, Australia, 2012. Version 10.0.

[34] S.H. Othman, G. Beydoun, Model-driven disaster management, Information & Management 50 (2013) 218–228.

[35] K. Paskaleva, J. Evans, C. Martin, Data governance in the sustainable smart city, Informatics 4 (2017) 1–19.

[36] K. Peffers, T. Tuunanen, M.A. Rothenberger, S. Chatterjee, A design science research methodology for Information Systems Research, Journal of Management Information Systems 24 (2007) 45–77.

[37] G. Piccoli, M.Ł. Bartosiak, B. Palese, J. Rodriguez, Designing scalability in required in-class introductory college courses, Information & Management 57 (2020) https://doi.org/10.1016/j.im.2019.103263.

[38] M.M. Rajaeian, A. Cater-Steel, M. Lane, A systematic literature review and critical assessment of model-driven decision support for IT outsourcing, Decis Support Syst 102 (2017) 42–56.

[39] M.M. Silva, T. Poleto, L.C.E. Silva, et al., A grey theory based approach to big data risk management using FMEA, Mathematical Problems in Engineering 2016 (2016) 1–15.

[40] S. Soares, Big Data governance: An emerging Imperative, MC Press, Boise, 2012.

[41] N. Thompson, R. Ravindran, S. Nicosia, Government data does not mean data governance: lessons learned from a public sector application audit, Gov Inf Q 32 (2015) 316–322.

[42] P. Xin, F. Khan, S. Ahmed, Dynamic hazard identification and scenario mapping using Bavesian network. Process Safety and Environmental Protection 105 (2017) 143-155.

[43] X. Xu, H. Qian, G. Ge, Z. Lin, Industry classification with online resume big data: a design science approach, Information & Management 57 (2020), https://doi.org 10.1016/i.im.2019.103182.

[44] F. Yu, X. Li, X. Han, Risk response for urban water supply network using case-based reasoning during a natural disaster, Saf Sci 106 (2018) 121–139

[45] X. Yu, Y. Zhang, T. Zhang, L. Wang, J. Hu, et al., A model-driven development framework for enterprise Web services, Information Systems Frontiers 9 (2007) 394-409.

[46] B.S. Zhang, X.Y. Li, J. Li, Research on emergency case ontology model based on ABC ontology, in: in Proceedings of the 20th International Conference on Management Science and Engineering - JCMSE ’13 JEFE Harbin 2013 pp. 227–233.

[47] D.Q. Zhang, S.W. Wallace, Z.X. Guo, Y.C. Dong, M. Kaut, On scenario construction for stochastic shortest path problems in real road networks. Transportation Research Part E: Logistics and Transportation Review 152 (2021). ttps://doi. org/10.1016/j.tre.2021.102410.

[48] K. Zhang, N. Luo, Y. Li, STGA-CBR: a case-based reasoning method based on spatiotemporal trajectory similarity assessment, IEEE Access 8 (2020) 22378-22385

[49] X. Zhu, X. Li, Z. Liu, Constructing Scenario Dimension Model of City Waterlogging Under Big Data Environ-Ment. 45. Geomatics and Information Science of Wuhan University, 2020, pp. 1818–1828.
