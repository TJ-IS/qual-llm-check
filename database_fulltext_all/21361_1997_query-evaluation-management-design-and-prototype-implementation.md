---
otero_id: 21361
otero_key: "W7AWNGE7"
title: "Query evaluation management design and prototype implementation"
authors: "Paulo B. Goes; Ram D. Gopal; Nai-Kuang Chen"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00047-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Query evaluation management Design and prototype implementation

Paulo B. Goes $^{*}$ , Ram D. Gopal, Nai-Kuang Chen

Operations and Information Management, School of Business Administration, University of Connecticut, Box U-41 IM, Storrs, CT 06269, USA

Received 9 October 1995; revised 15 April 1996; accepted 3 May 1996

## Abstract

The increasing customer orientation of information technology applications has resulted in a stronger emphasis on providing query evaluation services to the user community. Applications in electronic markets, data warehousing and decision support systems arenas function in highly dynamic environments serving users who demand increasing flexibility in their interactions with the systems. These characteristics limit a direct application of current query evaluation models. We propose the development of a query evaluation subsystem (QUEM) that is equipped with a knowledge base, a learning component and a decision support component to provide greater flexibility to the users and aid in managing system transitions. A prototype termed QUEST has been built and implemented in a quasi-real world setting. The experimental results validate the practical viability of the proposed architecture.

Keywords: Query evaluation; Query processing; Database management; Decision support systems; Knowledge bases

## 1. Introduction

Recent decades have witnessed a dramatic increase in the use of database systems for information storage and retrieval. As information becomes an important resource, corporations are placing increasing emphasis on the management of data. The evolution of database architectures has placed individual users as direct consumers of corporate information. With the capability of formulating their own on-line queries against corporate databases, users no longer need to rely on data processing departments for fulfilling their information needs. The relational architecture provides simplicity and data independence that obviate the need for a user to consider the physical details of data storage, data structure, and access methods in order to interact with the system.

Unfortunately, this ease of use has also led to a loss of control and a lack of knowledge on the underlying system details, especially on the part of non-expert users. While users are able to interact with the system to obtain the desired information, they have no a priori knowledge on important accompanying information such as query processing time, size of the resulting output, and of the transaction charge if query processing entails costs to the users. Providing information on such query evaluation metrics prior to query submission is an important component of user service, especially in a number of emerging information system applications. For example, as more companies realize the importance of information for decision making purposes, they have begun to make all the key information available to the decision makers. These decision support systems provide access to the information warehouses which store information relevant for decision making purposes [3,16]. Typically, decision makers submit ad hoc queries and the need for accurate estimates on the query execution time and the size of output is acute as the decision makers' time is expensive and there frequently exist time constraints on the decisions that rely on the responses to these queries.

## 1.1. Information markets and query evaluation

The need for providing query evaluation metrics to end-users is strongly underscored in information market applications. Information markets have arisen to satisfy the increasing need for companies to utilize information external to the company in planning important business decisions. The economies associated with the collection and management of up-to-date external information make purchasing of such information from external providers a more attractive option than internal creation and management. In recognition of this trend, a significant number of private organizations and government agencies have developed on-line databases and make them available to the consumers for a fee. For example, Dow Jones Information Service provides data on stock market and other financial market activities on all corporations listed on the New York and American

Stock Exchanges. Mead Data Corporation's Lexis data bank provides legal research information such as case law, court decisions, federal regulations, and legal articles. Knight-Ridder's KR Information OnDisc (formerly DIALOG's ONLINE) offers over 75 different data banks in agriculture, business, economics, etc. [21,22,25,27]. These markets are projected to significantly grow in the near future within the vast infrastructure of the internet. In this vein, database software companies such as Informix and Oracle have started to offer products which allow World Wide Web browsers to function as front ends to companies' relational databases. This will provide users with enormous flexibility in accessing external sources of data because they can formulate the queries in the form they find most useful, without the limitations imposed by the flat file structure of current data banks.

A number of researchers, including a team at University of Texas-Austin, have begun to lay the requisite theoretical foundations for these emerging electronic market mechanisms $[4,15,30]$ . Database queries in such markets can be seen as requests for the purchase of information products. In order to operate in such markets, suppliers need to provide services to the customers in the form of query evaluation metrics prior to the purchase (processing of the query).

## 1.2. Query evaluation metrics

Query evaluation metrics represent the consumption of system resources during the processing of the query transaction. The commonly utilized query evaluation metrics are the size of output [1,10,19,29], transaction response time [1,2,10,18,21,29] and the transaction charge to the user [2,17–19,21]. The three metrics are highly interdependent. The response time of a transaction depends on the volume of data processed and transferred to the user destination. Charging mechanisms typically employ a combination of response time and output size in their computing algorithms [2]. The underlying rationale is that the response time is indicative of the user waiting time and output size of the volume of the transaction. These metrics are often used collectively. In general, external and commercial applications focus on transaction response time and transaction charge, whereas internal and decision support applications emphasize size of output and transaction response time as relevant metrics. For example, Lexis/Nexis and other online data banks use response time and transaction charge [18,21]. The interdependencies among the evaluation metrics and their applicability to different environments are illustrated in Fig. 1.

![](/api/attachments/W7AWNGE7/fulltext/images/0fc9029481556427bb41dff4a2f360d57b8d9fcaf6964e22b3604f3ba4a1ce18.jpg)  
Fig. 1. Query evaluation metrics.

## 1.3. Query evaluation models

The development of query evaluation metrics requires a careful consideration of the mechanics involved in processing the query. Once a user submits a query, the Database Management System (DBMS) determines the set of tasks that need to be performed in order to respond to the query. The query evaluation metrics are thus a function of the types of system resources consumed in the execution of individual tasks, task management algorithms, and the overall staging of these tasks. As a result the query evaluation methodology needs to consider a myriad of factors such as:

\- query characteristics,

• data distribution and storage mechanisms,

\- hardware characteristics, such as CPU power, I/O bandwidth, communication capacities, and network topologies,

\- protocol mechanisms for recovery and concurrency,

\- query optimization algorithms, and

\- system utilization rates.

A number of query evaluation techniques have been proposed, most of which are based on analytical models [6-9,11-13,20,23,28,32,33] or simulations [26,31]. A good survey of such methods appear in [14]. To maintain tractability, the above studies limit the number of factors incorporated and make simplifying assumptions on the operational aspects of the system. As a result, most are applicable only for limited query types, processed in particular system environments. Furthermore, much of the focus in these models is on the overall performance of the system rather than providing precise evaluation metrics for ad hoc queries posed by individual users. From an application perspective, the above models are directly relevant for evaluating transaction processing systems, central to which are a limited set of queries that are repeatedly processed.

On the other hand, most emerging applications such as data warehousing, decision support systems and electronic markets, which require evaluation models function in environments where ad hoc queries frequently arise. A direct implementation of the current models is further limited due to the dynamic nature of these systems. Given that most current models function in specific system configurations, changes as a result of technological evolution, system upgrades, and usage patterns quickly render these models less useful. Current literature provides little insights on how to manage the evaluation models in the face of these system transitions. Model management strategies that translate the system-wide changes to specific impacts on evaluation models have not been developed. Further complications arise due to the lack of generality; strategies derived for a particular system configuration may not be relevant to other configurations as system changes may have varying impacts which are difficult to capture. The current literature provides limited insights to the Database Administration (DBA) for the management of the query evaluation process, especially in dynamic environments that provide users with greater flexibility in their interactions with the system.

## 1.4. Proposed research

In this research, we propose an architecture for the development of a DBMS subsystem termed Query Evaluation Manager (QUEM) whose primary responsibility is to provide query evaluation-related services to the user community. An important characteristic of QUEM is its ability to manage system changes to provide consistently satisfactory levels of service over the various operating environments the database system encounters throughout its life cycle. This is accomplished through the expert selection and utilization of evaluation models which are appropriate to each specific environment. To incorporate change management capabilities, QUEM is equipped with a knowledge base, a learning component that assimilates knowledge through change processes, and a decision support component which interacts with the DBA. The latter component is necessitated by the fact that the ultimate responsibilities for system management rest with the DBA, and the primary role of QUEM is to provide expert-level assistance.

The QUEM architecture is generic in that it is relevant to a spectrum of different operating environments. For example, internally oriented decision support systems and external commercial systems, systems that operate on intra- or inter-organization networks, and systems that are based on relational and non-relational platforms can all derive useful design principles for the construction of the query evaluation sub-system. The second phase of this research details the development of a prototype termed QUEST, under the QUEM design guidelines. The prototype is an instantiation of the architecture and is tailored for an internal relational database application. An empirical evaluation through an implementation of QUEST in a quasi-real world setting validates directly the prototype and in the process the key QUEM architectural features that address user flexibility and system dynamics.

The primary contributions of this research are two-fold. One, we present a blueprint for the development of a sub-system for providing query evaluation services in a user-empowered, dynamic environment, through the QUEM architecture. Two, we present the prototype QUEST specifically developed for internal, relational platforms. A unique feature of QUEST is that it houses neural network based models that have hitherto not been used in conjunction with query evaluation. The empirical study highlights the practical viability of QUEST in particular, and key features of QUEM in general.

The rest of the paper is organized as follows. Section 2 provides the architectural foundations of QUEM. Section 3 presents a prototype, termed

QUEST, which has been designed and built. Section 4 presents a limited validation of the QUEM architecture through an implementation study. Conclusions and future research directions are presented in Section 5.

## 2. QUEM architecture

In this section we develop QUEM, an architecture that provides guidelines to the design of a DBMS subsystem to provide query evaluation related services to the user community. The QUEM architecture is generic in that it permits the materialization of query evaluation subsystems for a wide variety of operating environments. Concomitantly, every feasible materialization exhibits all the key desirable features that are embedded within the generic architecture. We initially present the important objectives of the QUEM architecture prior to embarking on the discussion of the specific architectural components.

## 2.1. Key architectural objectives

QUEM-supported evaluation subsystems are designed to be used by the administrators of database systems where providing query evaluation metrics is a crucial component of the overall service to the user community. From the perspective of practical viability for emerging applications, it is essential for QUEM to incorporate the following features.

\- Speed. The estimation and the actual query processing occur in a linear succession as the user's decision to process the query depends on the particular values of the evaluation metrics. It is important to recognize that the time spent in the estimation of the query evaluation metrics is time lost as the actual query is not processed during this stage. Thus the speed of estimation is an important determinant of the success of the overall subsystem.

\- Versatility. Emerging database applications such as electronic commerce and data warehousing typically support a plethora of user information needs of the system. These user-empowered environments dictate that the evaluation subsystem be capable of processing a wide variety of queries, from pre-defined periodic transaction queries to ad hoc user-constructed queries.

\- Adaptability. Most database systems are dynamic in nature and constantly evolve. The evaluation subsystem should possess change management capabilities that assist the DBA in the transition from one system environment to the next. These desirable change management capabilities include: (i) recognition of the need to change the evaluation subsystem to respond to changes in the system environment, (ii) management of the process of transition to a new set of evaluation models, and (iii) seamless transition to minimize disruption of user services. These features ensure the usefulness of the evaluation subsystem throughout the life cycle of the overall system.

## 2.2. Intelligent decision support system (IDSS) architecture for QUEM

The proposed architecture outlines the design and management of QUEM. Fig. 2 illustrates the context view of the QUEM architecture. It consists of five distinct, inter-related modules. The evaluation module houses the current set of models and associated factors used for query evaluation. Its primary function is to provide query-related services to the user and act as a bridge to the database query processor. The user interface module and the DBA interface module provide front-end support to the users and the DBA, respectively. The adaptive control module monitors the performance of the evaluation module and supports its adaptive maintenance, in conjunction with the DBA. The meta knowledge base is a repository of both the generic evaluation-related and system-specific knowledge. A key aspect of this module is that new knowledge is constantly assimilated, through information derived from user transactions and information interchange with the DBA.

Consider the operation of a database system over an extended period of time. The total time of use can be divided into “time frames”, where in each time frame the system operates within a relatively stable operating environment. Hence, each time frame refers to a specific and stable environment for which the current evaluation module can adequately capture the underlying query dynamics. The transition from one time frame to the next involves: (i) identification of the need for change of the evaluation module, (ii) identification of the causes and the key factors that capture these changes, and (iii) regeneration of the evaluation module relevant for the new time frame. The adaptive control module in QUEM monitors the performance of the evaluation module. Performance

![](/api/attachments/W7AWNGE7/fulltext/images/4ebbabef9b8affae0c19f1d3c684a57aa5b1d776b6ed90030f5857306eb05ec7.jpg)  
Fig. 2. DSS architecture for QUEM: Context view.

degradations are analyzed and communicated to the DBA. This information includes a temporal analysis of performance deviations and their impacts on the performance of the evaluation module. Along with the meta knowledge base, this information is utilized to isolate the causes and identify the new model/factor set that captures important changes in the environment. For the new evaluation module generation, the meta knowledge base, which includes the knowledge built into QUEM and the knowledge that is assimilated by the learning mechanism through prior system phase changes, is employed. The key to the knowledge base is that it is domain-specific and thus directly relevant and useful for managing changes in the system environment. The DBA interface module makes this expertise available to the DBA to efficiently manage changes. Once the new module is implemented, the meta knowledge component analyzes the changes to derive useful information and updates the knowledge base. This stage constitutes the learning phase of QUEM. This cycle is a continuous process that occurs throughout the lifetime of the system. Thus, QUEM is an intelligent decision support system that can be employed by the database administration to provide valuable services to the user. A more detailed view of the modules and their interactions is depicted in Fig. 3 and is described below.

The evaluation module stores the current set of models and the factors incorporated within them. These models and factors are a subset of the models and factors in the meta knowledge base. The factors serve as explanatory variables that affect query performance. The models depict the fashion in which the factors affect query performance. The models provide estimates on various evaluative metrics such as transaction charge, response time, output size, which are conveyed to the user through the user interface module. The input values to the models (the factor values at the query evaluation time) come from both the query itself and the meta knowledge base. The evaluation module is designed to maintain a degree of logical independence from the rest of the system so that the models and the factor set can evolve to maintain relevance with the changing system dynamics.

![](/api/attachments/W7AWNGE7/fulltext/images/d1fa4a83f9d6a33d7ddac41c3be698893f771437dd8df33db5aabbe3a5aa661c.jpg)  
Fig. 3. IDSS architecture for QUEM: Component view.

Clearly, more sophisticated estimation models and a larger number of factors may only improve the accuracy of the estimation of the query evaluation metrics. However, the downside to the increasingly sophisticated models and larger factor sets is that they tend to require higher levels of systems resources which is directly reflected in longer times spent for the process of estimation. Thus, a point of diminishing returns will be reached where the benefits of more accurate evaluations are outweighted by higher estimation costs. To successfully balance this fundamental tradeoff, the DBA dictates performance goals in terms of accuracy levels of the evaluation metrics. The evaluation module is then generated to achieve these specified goals with a minimal set of factors and computationally efficient models. This guarantees that the key architectural objective of speed of estimation is successfully achieved. Note that this may entail the use of a multitude of model/factors combinations, with each tailored to specific query structures and system states. Thus only a relevant subset of models housed in the evaluation module may be automatically triggered depending on the particular query being processed and the present status of the system. For example, in relational systems queries on single relations are fundamentally different from multi-relation queries because of the JOIN operation. As a result, different models/factors may be relevant for these query types. In another example, multi-user network-enabled systems operate in two distinct states: congested and uncongested. The state of congestion dictates the use of more complex models/factors to capture the operating environment. Such knowledge on which models/factors to deploy is created from the meta knowledge base and is directly embedded in the evaluation module. It can be automatically triggered upon the arrival of a query through a simple if-then-else decision structure.

The user interface module provides front-end services to the user. Its two main functions include: (a) assisting users in building queries so as to satisfy the information needs and meet the price, time or other resource constraints, and (b) providing an estimate of relevant metrics so that a user can decide to process, redesign or cancel the query. A sample of this interface is shown in Fig. 4. Upon completion of a user transaction the user interface module transmits the transaction information to the meta knowledge base where it is used for control and redesign purposes.

![](/api/attachments/W7AWNGE7/fulltext/images/40b46b2ef903c0a202ea383a81e553a0b9837698960f7faabcecfbd5bc90c363.jpg)  
Fig. 4. Sample user interface screen.

The meta knowledge base is a repository of both generic and domain-specific knowledge. It consists of three components. The model-factor base houses the universal set of factors and models and all relevant knowledge on their implementation to specific environments. The evaluation module is an instantiation and is directly derived from the model-factor base. We can view the knowledge content of the model-factor base as a superset of that in the evaluation module.

The knowledge in the model-factor base is constantly evolving and comes from two sources: (a) knowledge that is built in by the system designer, and (b) knowledge that is “learnt”, assimilated and stored during system transitions. The built-in knowledge typically consists of a large set of factors and models that are known to be relevant to query evaluation, and generic knowledge on how to operationalize them under various operating conditions. For example, factors such as query characteristics, I/O channel capacities, CPU features that are known to be important are housed in the model-factor base. Similarly, modeling tools such as regression models are incorporated within the model-factor base by the system designer. It can also be updated by the DBA, if for example, new estimation techniques become available. Generic knowledge on the effective use of models/factors could, for example, take the form:

I/O transfer is an important factor in evaluating multi-relation queries in uncongested systems; I/O transfer and channel capacity are important factors in evaluating multi-relation queries in congested systems.

Another example of generic knowledge could include:

Memory size is an important factor in evaluating memory intensive queries;

Memory size is less important in evaluating I/O bound queries.

The second source of knowledge results from the interaction with the system users during query processing and with the DBA during system transitions. This knowledge pertains directly to the particular system, and this system-specific knowledge is highly relevant for managing change processes. For example, consider the following knowledge associated with one system transition:

Addition of a storage device may necessitate a revision of the current evaluation module.

The revision of the current evaluation module to address addition of a storage device only required the regeneration of a subset of the models.

This specific knowledge can be “learnt” and stored in the model-factor base for future use. A high-end learning system may automate the process through inductive and deductive learning capabilities. A low-end system might rely heavily on the DBA and simply provide a few automated routines for efficient storage and retrieval of textually-based knowledge.

The model-factor base is invoked by the adaptive control module when the current query evaluation module no longer provides adequate performance levels. The model-factor base is utilized to (a) help identify the causes of the performance degradation, and (b) assist in the creation of the new evaluation module that effectively endogenizes the external change. The QUEM architecture is generic and permits a wide range of operationalization schemes to perform the two tasks. A low-end (with high DBA involvement) implementation might only permit the storage of knowledge as a set of factoids that can be efficiently retrieved, modified and appended to the model-factor base by the DBA through a few pre-defined automated routines. A high-end system might automate much of these tasks. Such a system could incorporate fuzzy logic, conflict resolution schemes to resolve conflicting messages, other knowledge acquisition/representation aids as well as model management techniques [5] to automatically learn, assimilate, and efficiently manage the model-factor base.

The domain-specific knowledge stored includes a “snapshot” view of the current system and an audit trail of user transactions. The system-specific knowledge base provides input to the evaluation module about the current status of the system, which is then used to derive the performance metrics. It provides a quantitative description of the database and the overall system. Most current DBMSs already collect and provide such information. For example, data dictionaries such as IBM DB2’s Catalog contain information about the current structure of tables, indices, etc., and the RUNSTATS utility in DB2 provides a statistical profile on the distribution of the data in the relations. Therefore the explicit creation of the system-specific knowledge base for QUEM is typically not required, and the development of a simple interface with the existing database modules would make it operational.

The control data base maintains a log of recent user transactions. Information such as query descriptors, actual and estimated performance metrics that provide insights into the overall performance of the current query evaluation module is collected. The control data base is monitored by the adaptive control module to assess the overall performance of the system.

The adaptive control module is responsible for ensuring satisfactory levels of performance of the evaluation module. Its two components monitor the performance of the evaluation module and assist the DBA with the regeneration and/or fine tuning of the current implementation of the evaluation module. The performance monitor analyzes the control data base and reports to the DBA. Once the need for change has been recognized the change manager is activated.

The change manager initiates a session with the DBA and opens a channel to access the meta knowledge base. The session activities include:

(a) Identification of the trigger events that led to performance degradation. This is achieved by synthesizing the relevant information from the meta knowledge base and the information that is provided by the DBA.

(b) Update of the evaluation module to incorporate the trigger events and achieve the desired performance levels. This is achieved by consulting the meta knowledge base and the DBA to generate a new set of models and factors relevant to the new system environment. A number of models that incorporate the trigger events with varying degrees of complexity are generated from the model-factor base. These models are evaluated for adequacy in the new system environment. The change manager assists the DBA in the final choice of the models/factors to be embedded in the new evaluation module.

<table><tr><td>Current Model in Use</td><td colspan="2">Last 30 days</td><td colspan="2">Last 10 days</td><td colspan="2">Last 1 day</td></tr><tr><td></td><td>MPD</td><td>NQP</td><td>MPD</td><td>NQP</td><td>MPD</td><td>NQP</td></tr><tr><td>Model 1</td><td>23.1%</td><td>17233</td><td>22.2%</td><td>5723</td><td>22.8%</td><td>599</td></tr><tr><td>Model 2</td><td>26.3%</td><td>14345</td><td>24.7%</td><td>4719</td><td>24.6%</td><td>481</td></tr><tr><td>Model 3</td><td>24.9%</td><td>15091</td><td>23.0%</td><td>5009</td><td>23.7%</td><td>492</td></tr></table>

Fig. 5. Performance report.

(c) Assimilation and incorporation of the knowledge acquired during the current system transition into the meta knowledge base for future use. This is achieved through a thorough analysis of how the transition to the new evaluation module was successfully conducted. This, for example, could include the behavior of particular models and factors in the new and old environments.

Note that the above activities can be implemented through various degrees of automation. At the very least, the adaptive control module provides decision support and maintains a close interaction with the DBA, the authority that is ultimately responsible to initiate and implement changes. This feature underscores the trends that characterize the shifts in the management of task complexities. The database technologies have made the access to data very easy for the users and in the process have transferred most of the responsibilities for dealing with the underlying system complexities to the DBA. QUEM in turn is designed to transfer these complex tasks from the DBA to the system, which inherits the responsibilities for knowledge assimilation and storage.

The DBA interface permits the DBA to access performance reports and participate in the creation and update of the evaluation module. It also provides access to the meta knowledge base for the addition of new knowledge. Fig. 5 shows a sample of the performance report. Fig. 6 illustrates performance diagnostics and the process of knowledge creation. These figures are derived from the prototype discussed in Section 4.

A process view of QUEM that identifies the trigger events and principal change activities is shown in Fig. 7. The following section outlines a prototype based on the QUEM architecture which has been designed and implemented.

![](/api/attachments/W7AWNGE7/fulltext/images/87a06c59a44d7a53d1d0822ce6d4ae4dac7bd813cd7fec9d8388717479163891.jpg)  
Fig. 6. Performance diagnostics.

## 3. QUEST: A prototype

QUEST (Query Estimator) is a first level prototype limited in scope to evaluating query response time (and indirectly output size) for a relational DBMS implemented on a Local Area Network setting. The logical independence designed within the QUEM architecture facilitates easy additions to the features of each module. Thus QUEST is an evolutionary prototype whose scope can be iteratively expanded to incorporate charging algorithms, generate pricing schemes and support databases implemented over other network configurations.

## 3.1. Meta knowledge base

Model-factor base: Models are created based on the estimation methodologies of regression and neural networks. These are two widely used forecasting techniques with each having distinct advantages over the other. Regression methodology imposes little computational work, but does require an explicit function specification relating the set of factors to the response time. Furthermore, regression-based estimation procedures are limited to linear and a few non-linear function specifications. This methodology has been used for query response time estimation in some database settings [1,10]. Neural networks are based on artificial intelligence and can automatically detect and incorporate the inherent relationship between factors and response time. Since an explicit functional form need not be specified a priori, techniques based on neural networks place a lower cognitive burden on the DBA. While neural networks have been used for estimation purposes in a number of application areas, to the best of our knowledge, they have not been used for query evaluation. The down side to this methodology is the increased computational effort. Other evaluation techniques based on for example queuing methods and stochastic models can be adaptively included in the model base as the prototype evolves towards full functionality.

![](/api/attachments/W7AWNGE7/fulltext/images/a19002886313e0a0ed79b76cc5d0c69161d219185368bb9c39ff5ce9db49342c.jpg)  
Fig. 7. IDSS architecture for QUEM: Process view.

The models generated in QUEST are segmented according to whether the query refers to a single relation or multiple relations due to the wide discrepancy in typical response times of these two types of queries. The join queries that arise over multiple relations are generally at least an order of magnitude more expensive than single-relation queries in typical response times.

The set of factors incorporated in QUEST can be categorized into query characteristics, such as attributes involved and selectivity factors, hardware characteristics, such as CPU power, I/O bandwidth, DBMS structural characteristics, such as the file organizations, index structures, network characteristics, such as communication bandwidth, network topology, and overall system characteristics, such as the number of users and system load. New factors are appended to the factor base as the system undergoes changes and some of these cannot be captured and explained by the factor base.

The knowledge base includes expert-level rules on how to utilize the models and the factors. These rules are either built-in at the design time or created during the system transition phases. These rules are utilized by the system and the DBA in the change management process. The knowledge is stored as a series of factoids. The knowledge base is indexed and keyword searchable for efficient manipulation during system transitions.

Control data base: This component is operationalized as a simple audit trail that tracks query characteristics such as single/multiple relation query, attributes addressed, selectivity conditions, output size, system utilization ratio, number of users on line and actual and estimated response times. This information was deemed sufficient for the current implementation of the prototype.

## 3.2. Adaptive control module

Performance monitor: The performance monitor is designed to constantly monitor the control data base. The performance of each model is evaluated in terms of the following metrics: MAD (Mean Absolute Deviation), MPD (Mean Percentage Deviation)

and MSE (Mean Square Error). The performance monitor provides periodic and exception reports to the DBA on recent past, present and projected state of the system. The DBA sets acceptable performance deviations for each model in the current model set. Persistent deviations beyond these pre-set limits are conveyed to the DBA and provide impetus for change. What constitutes persistent deviations is defined by the DBA. For example, the QUEST prototype permits the DBA to define deviations within one unit of MAD as acceptable, and deviations beyond these limits for 20% or more of the latest 100 queries processed as constituting persistent degradation.

Change manager: QUEST's change manager is implemented as a set of automated routines to assist the DBA in managing system transitions. The change manager can act on any subset of the current set of models. It incorporates a set of benchmark queries, which is a set of test queries that are representative of the general queries posed by the users. The DBA actively participates in the creation and management of benchmark queries. The key phases involved in QUEST's change manager are as follows.

Diagnostics phase: Change Manager identifies the set of models requiring change. The Change Manager provides a performance analysis of each current evaluation module (Fig. 8 and Fig. 9). The DBA selects the models to change.

Factor set selection phase: The Change Manager isolates the time frame of performance degradation and presents an analysis to DBA. Change Manager provides user-friendly access to the meta knowledge base to help DBA isolate the trigger events that might have occurred around this time frame. DBA identifies the set of factors that aid to endogenize the events that led to performance degradation.

Model set selection phase: Change Manager runs benchmark queries in new environment to obtain performance benchmarks. The Change Manager generates a range of model/factor combinations; DBA selects a set for further evaluation. Change Manager evaluates each combination against benchmark queries in terms of the performance metrics MAD, MPD and MSE. Change Manager prompts DBA to analyze the results and select the new evaluation module.

Table 1  
Realization of key objectives

<table><tr><td></td><td>QUEM</td><td>QUEST</td></tr><tr><td colspan="3">Objectives:</td></tr><tr><td>Speed</td><td>Minimal set of factors, intelligent model selection</td><td>Minimal set of factors to advice DBA provided performance goalsIntelligent model selection through analysis of recent queries</td></tr><tr><td>Versatility</td><td>Accommodate a plethora of user needs of the system</td><td>Ability to evaluate any user constructed relational queries</td></tr><tr><td>Adaptability</td><td>Full range of change management capabilities to accommodate system transitions</td><td>System prompts need for changeNew evaluation model generation through system-DBA interchangeNew knowledge creation through system-DBA interchange</td></tr></table>

Knowledge creation phase: Change Manager conducts a comparative performance analysis of old and new models and presents the analysis to DBA. DBA fine tunes knowledge learnt and updates the meta knowledge base with information on how the new factor set and models have explained trigger events.

Tables 1 and 2 below present overviews of how QUEST materializes the key objectives, features and components of the QUEM architecture. An empirical study which details a particular implementation of the QUEST prototype is discussed in the next section.

## 4. Validation of QUEM: An empirical study

The purpose of conducting the empirical study is to provide a limited validation of the architecture through an implementation of the QUEST prototype, and to subject the prototype to a major system change and evaluate its adaptability and knowledge-creation capability during the course of this change.

Table 2  
Comparative view of the key features

<table><tr><td></td><td>QUEM</td><td>QUEST</td></tr><tr><td>Focus</td><td>Internal, external</td><td>Internal, relational DBMS</td></tr><tr><td>Performance metric</td><td>Transaction charge, response time, size of output</td><td>Response time, size of output (intermediate result)</td></tr><tr><td>Meta knowledge base</td><td rowspan="2">Generic models, generic factors</td><td rowspan="2">Models: regression, neural networkFactors: query, hardware, structural network, overall system</td></tr><tr><td>Model-factor base</td></tr><tr><td>Control data base</td><td>Query, user, performance, system descriptors</td><td>Query, user, performance, system descriptors</td></tr><tr><td>Decision support</td><td rowspan="2">Full range of front-end services for information extraction by users</td><td rowspan="2">Flexible relational query construction interfaceResponse time (output size) estimates prior to query executionGoal seeking capability to maximize informational output within resource constraints</td></tr><tr><td>User</td></tr><tr><td>DBA</td><td>Model/factor managementInterface support for knowledge creation and assimilation</td><td>Periodic and exception reporting on system statusProvide facilities for active DBA involvement in model/factor selection and modification during system transitionProvide facilities to examine previously acquired knowledge for relevance and fine tune knowledge acquired during system transitions before final assimilation</td></tr></table>

The study was motivated by a relational database system utilized by a county in a northeast state to track and monitor Driving While Intoxicated (DWI) cases. The system provides various services to the employees in the county office, the police departments, the courts, and the news media. An important concern for the end-users and the database administration has been the wide variability in the response times to users' queries. The response times varied from a few seconds to a few hours, and lack of this response time information was a cause for significant frustration among the users. The administration was interested in not only providing accurate estimates for the current system setup, but their needs were strongly underscored by the necessity to maintain adequate accuracy levels in the face of technical changes to the hardware/software environment and projected changes in the usage patterns.

The QUEST prototype was implemented in a laboratory setting that closely mimics the actual database environment. In this quasi-real world setting, we replicated the actual system in its hardware/software configuration and the usage patterns. The database itself was “transported” to the laboratory, with random changes in the values of data that was deemed confidential. To further maintain realism to the actual system, queries that were processed were mainly derived from the actual ones. This decision to conduct experimentation in the laboratory was made due to the obvious confidentiality reasons and a need to perform extensive testing prior to the actual implementation. More importantly, the laboratory setting permitted us to subject the system to a life cycle change to gauge the performance of the prototype. Such an analysis in the actual setting was viewed as an undesirable intrusion and negatively impacting the existing work patterns.

The DWI database consists of six relations, and its schema is depicted in Appendix A. To ensure adherence to the actual setting, three PCs with 386-based microprocessors were networked, with one machine designated as the server. The database and the DBMS software were housed on the server. Queries were submitted from the two clients.

Clearly, the system itself is comprised of hardware components (server CPU, client CPUs, I/O devices, etc.), software components (operating system, DBMS, etc.), and network components (operating system, topology, bandwidth, etc.). QUEST's model-factor base is sufficiently comprehensive to explicitly capture all the relevant factors in such a system and functionally represent them through sophisticated models. However, the initial factor and model set selection was driven by the objective of attaining the pre-set performance goals, concomitant with the QUEM objectives of speed and versatility. To achieve these objectives the DBA was asked to establish acceptable performance levels. A MAD level of three seconds for single-relation queries and two minutes for two-relation join queries were identified as desirable target levels. The following discussion presents the rationale underlying the initial model/factor selection.

Query processing involves three types of operations: I/O transfer, CPU processing and network transfer. The usage pattern of the DWI database was such that network congestion was rarely an issue. As a result of low network traffic, network transfer costs are mainly a function of the output data. Of the two remaining types of operations, I/O related costs are typically more predominant, and the amount of CPU processing is closely related to the amount of data which is input/output. These facts guided our choice of the initial factor set. This initial set, along with the rationale for inclusion of each element, is depicted in Table 3.

For model selection, both regression and neural networks techniques were employed. Multi-relation joins are typically processed as a sequence of two-relation joins and thus the results of the two-relation joins are directly transportable to the general case [24]. Consequently, only single-relation and two-relation queries were explicitly modeled. 160 single-relation queries and 87 two-relation queries were chosen as benchmark queries. These queries mainly represented the actual queries posed by the users. A few additional queries were included to ensure an equitable inclusion of all the relations in the database. For each set, one half of the randomly chosen queries was used for model parameter estimation and the rest to derive performance metrics.

Table 3  
Initial factor set

<table><tr><td>Factor</td><td>Explanation</td><td>Rationale</td></tr><tr><td colspan="3">Relation-based</td></tr><tr><td> $N_i$ </td><td># of tuples in relation i</td><td>Impacts input costs</td></tr><tr><td> $T_i$ </td><td>Size of tuple in relation i(in bytes)</td><td>Impacts input costs</td></tr><tr><td colspan="3">Query-based</td></tr><tr><td> $σ_Q$ </td><td>Selectivity factor for query Q</td><td>Impacts input and output costs</td></tr><tr><td> $S_Q$ </td><td>Size of tuple in query answer(in bytes)</td><td>Impacts output costs</td></tr></table>

<table><tr><td colspan="4">Table 4Initial regression results</td></tr><tr><td colspan="4">Dependent variable: Response time</td></tr><tr><td>Model</td><td>Independent variable</td><td>Estimated value</td><td>t statistic</td></tr><tr><td>Single-relation</td><td>Constant</td><td>6.63651</td><td>9.714*</td></tr><tr><td> $R^{2} = 0.663$ </td><td>Costinput</td><td>1.25104e-05</td><td>2.515**</td></tr><tr><td> $F = 64.894$ *</td><td>Costoutput</td><td>2.81996e-04</td><td>11.346*</td></tr><tr><td>Two-relation</td><td>Constant</td><td>-27.79745</td><td>-0.53</td></tr><tr><td> $R^{2} = 0.771$ </td><td>Costinput</td><td>3.92688e-04</td><td>2.045**</td></tr><tr><td> $F = 65.627$ *</td><td>Costoutput</td><td>0.00417</td><td>9.826*</td></tr></table>

Note: \* Significant at p-value < 0.0001; \*\* Significant at p-value < 0.05.

The regression technique requires an explicit specification of the estimation model. The following functional forms were used.

Single-relation queries:

$$
\text { Response   time } = \beta_ {0} + \beta_ {1} \text { Cost } _ {\text { input }} + \beta_ {2} \text { Cost } _ {\text { output }},
$$

where

$$
\operatorname{Cost} _ {\text { input }} = N _ {i} \times T _ {i}
$$

and

$$
\mathrm{Cost} _ {\text { output }} = N _ {i} \times \sigma_ {Q} \times S _ {Q}
$$

represent size of data input and output respectively.

Two-relation join queries:

$$
\text { Response   time } = \beta_ {0} + \beta_ {1} \text { Cost } _ {\text { input }} + \beta_ {2} \text { Cost } _ {\text { output }},
$$

where

$$
\operatorname{Cost} _ {\text { input }} = \left(N _ {i} \times T _ {i} + N _ {j} \times T _ {j}\right)
$$

and

$$
\mathrm{Cost} _ {\text { output }} = \left(N _ {j} \times \sigma_ {Q} \times S _ {Q}\right)
$$

represent the data input and output costs, respectively. Relation j is considered the largest of the two relations.

To estimate the regression model parameters, the Ordinary Least Square (OLS) technique was used. The data set satisfied the assumptions incorporated within the OLS technique and was thus a suitable estimation technique. The regression results are reported in Table 4.

For the neural networks technique, the factor set in Table 3 for each participating relation in the query is used as the input. Two neural networks setups, depicted as NN1 and NN2, were considered. NN1 was setup with one hidden layer with ten neurons and NN2 was setup with two hidden layers, with two-thirds the number of inputs as the number of neurons for the first layer and one-third as many for the second. For both setups, a standard sigmoid transfer function with a low saturation limit of 0 and a high saturation limit of 1 was used. The training tolerance was set at 0.1, which implies that the output value must be within 10% of the range of the training pattern to be considered correct. The networks were set up to continue training until all training facts meet the 0.1 tolerance rate.

Table 5  
Performance metrics

<table><tr><td rowspan="2">Metrics</td><td colspan="3">Single-relation models</td><td colspan="3">Two-relation models</td></tr><tr><td>Regression</td><td>NN1</td><td>NN2</td><td>Regression</td><td>NN1</td><td>NN2</td></tr><tr><td> $MAD^a$ </td><td>1.86</td><td>1.77</td><td>1.66</td><td>37.11</td><td>50.21</td><td>36.29</td></tr><tr><td>MPD</td><td>23.25%</td><td>18.15%</td><td>17.86%</td><td>31.16%</td><td>52.09%</td><td>37.69%</td></tr><tr><td> $MSE^a$ </td><td>5.31</td><td>9.71</td><td>6.93</td><td>3536.91</td><td>3737.87</td><td>2300.72</td></tr></table>

$^{a}$ Time unit in seconds.

(a)  
Single-relation Query Response Time (Regression Model)  
![](/api/attachments/W7AWNGE7/fulltext/images/5652a7d74dca32bccb1d3c533eb05c0174de5c907ff4ebc15a66c04fb6b7841a.jpg)

(b)  
Join Query Response Time (Regression Model)  
![](/api/attachments/W7AWNGE7/fulltext/images/9fbf6220f5bf3637d8352e189bcb3bacb51159805526dbecc8d6345ea787d8db.jpg)  
Fig. 8. (a) and (b): Performance of the evaluation module.

With the regression models derived and the neural nets trained and tested, a second batch of benchmark queries was used to obtain performance metrics. The results are reported in Table 5.

The MAD values for all the models considered were within the levels pre-set by the DBA. These results were presented to the DBA for model selection. Given that the performance of the regression models were reasonably close to the NN2 setup, which provided the lowest MAD levels, and given the lower cost of implementing the regression models, a decision was made to incorporate these into the evaluation module of the prototype. Fig. 8(a) and Fig. 8(b) portrays the performance of the evaluation module against user queries, posed to the database at various points in time.

To evaluate the adaptability of the prototype, the system was subject to an event change and the DBA was asked to interface with the prototype in order to update the evaluation module to capture the new system environment. An upgrade of the server machine to a 486-based microprocessor constituted the system change. This caused a significant performance degradation in the evaluation subsystem as shown in Fig. 9. The performance monitor prompted the DBA to re-evaluate the current evaluation module.

With the need for change clearly identified by the performance monitor, the Change Manager initiated a dialogue with the DBA which resulted in the following activities:

(1) The cause of change was identified by the DBA: server system upgrade.

(2) Change Manager performed a search of the meta knowledge base on server system upgrade. Note that since the meta knowledge base is implemented in a textual format, the Change Manager performed a keyword search for information retrieval.

(3) The meta knowledge base did not identify any new factors to include with this change.

(4) Since no explicit factor was identified, Change Manager's automated routine recommended a re-evaluation of the models with the same factor base.

(5) The DBA approved this recommendation and the Change Manager re-evaluated the models and presented performance metrics of the new models to the DBA. These are illustrated in Table 6.

Single-relation Query Response Time (Regression Model)  
![](/api/attachments/W7AWNGE7/fulltext/images/619f0c0012c1b4971da91d3042046f53ce3910ca04f2d5540d7a8947dc1bad82.jpg)  
Fig. 9. Server upgrade: Performance of the evaluation module for single-relation regression models.

Table 6  
Performance metrics

<table><tr><td rowspan="2">Metrics</td><td colspan="3">Single-relation models</td><td colspan="3">Two-relation models</td></tr><tr><td>Regression</td><td>NN1</td><td>NN2</td><td>Regression</td><td>NN1</td><td>NN2</td></tr><tr><td> $MAD^a$ </td><td>0.16</td><td>0.12</td><td>0.11</td><td>0.34</td><td>0.41</td><td>0.39</td></tr><tr><td>MPD</td><td>43.62%</td><td>29.09%</td><td>30.94%</td><td>10.65%</td><td>11.61%</td><td>11.08%</td></tr><tr><td> $MSE^a$ </td><td>0.03</td><td>0.03</td><td>0.03</td><td>0.20</td><td>0.32</td><td>0.30</td></tr></table>

$^{a}$ Time unit in seconds.

(6) The new models were deemed satisfactory by the DBA who selected the NN2 setup for single-relation queries and the regression model for two-relation queries for the evaluation module.

(7) The model-factor base in the meta knowledge base was updated with the new knowledge acquired during this phase change.

Learning by Change Manager: The learning by the Change Manager is a direct result of the comparative analysis of the old and new evaluation modules. The following factoids were derived and presented to the DBA:

(i) Server system upgrade did not necessitate the inclusion of new factors.

(ii) Server system upgrade impacts both single-relation and two-relation models.

(iii) A server system upgrade led to an improved performance of the models.

(iv) Neural networks models based on NN2 setup provide superior performance overall.

Learning by DBA: The DBA accepted the above with minor editorial changes and appended them to the model-factor base along with the following: (v) From the combined perspective of cost and accuracy, the regression-based models provide better performance for two-relation queries.

Comparative views of QUEST's objectives, features and components versus their actual implementation in the empirical study are summarized in Tables 7 and 8.

## 4.1. Lessons learned

A post-experimental interview with the DBA yielded several interesting perspectives on both the overall architectural design and the specific capabilities of the QUEST prototype. The significant appeal of the prototype stems from its ability for knowledge creation and assimilation, and its decision support capability. The prototype permits the responsibility for “learning from experience” to be transferred from the DBA to the system, and thus overcomes problems that arise due to human memory losses and personnel turnover. Further, the DBA noted the difficulties that arise in transforming generic knowledge to specific system environments. The fact that the meta knowledge base assimilates domain-specific knowledge was viewed as extremely important from a practical stand point. It was noted by the DBA that the knowledge represented in the system is a result of a series of events that have an impact on the system. As the meta knowledge base can provide valuable insights on how these events affect the system, this knowledge in turn can be used in planning system improvements.

Table 7  
Realization of key objectives

<table><tr><td></td><td>QUEST</td><td>Empirical study</td></tr><tr><td colspan="3">Objectives:</td></tr><tr><td>Speed</td><td>Minimal set of factors to advice DBA provided performance goals Intelligent model selection through analysis of recent queries</td><td>Minimal set of factors to achieve 3 sec., MAD level for single relation queries and 2 min. MAD level for join queries Priority to regression model due to lower computational effort</td></tr><tr><td>Versatility</td><td>Ability to evaluate any user constructed relational queries</td><td>Ability to evaluate any SELECT, PROJECT one-relation queries, and two-relation JOIN queries</td></tr><tr><td>Adaptability</td><td>System prompts need for changeNew evaluation model generation through system-DBA interchangeNew knowledge creation through system-DBA interchange</td><td>System prompts need for changeDBA/System isolate cause of change (CPU upgrade)New evaluation model generation through system-DBA interchange to achieve pre-specified performance level (neural network for single queries, regression for join queries)Knowledge creation: knowledge on CPU upgrade, its effects on performance,consequent generation of new models were assimilated into knowledge base for future use</td></tr></table>

The most significant shortcoming of the current prototype was identified as the long time delays between performance degradation and implementation of the new evaluation module. A careful scheduling of the activities involved in this transition period may substantially reduce the downtime. Also, the current set of models housed in the model-factor base may need to be expanded to accommodate increasing complexity as the current database system evolves. The second generation of the QUEST prototype will incorporate these recommendations.

As Tables 7 and 8 clearly indicate the empirical study validates the two key architectural features of speed and adaptability. The speed feature is validated by the Change Manager's automated routines that carefully generated minimal sets of factors and computationally efficient models which attained pre-specified performance levels. The adaptability feature is validated through the successful phase transition in response to server upgrade and the ensuing evaluation module generation and knowledge creation by the Change Manager/DBA tandem. As only one and two-relation queries were considered in the study, the versatility feature was evaluated only to a limited extent. Future research would validate this feature through a QUEST implementation in an environment that caters to users' eclectic information needs.

Table 8  
Comparative view of the key features

<table><tr><td></td><td>QUEST</td><td>Empirical study</td></tr><tr><td>Focus</td><td>Internal, relational DBMS</td><td>Internal, relational DBMS on LAN file server</td></tr><tr><td>Performance metric</td><td>Response time, size of output (intermediate result)</td><td>Response time, size of output (intermediate result)</td></tr><tr><td colspan="3">Meta knowledge base</td></tr><tr><td>Model-factor base</td><td>Models: regression, neural networkFactors: query, hardware, structural network, overall system</td><td>Models: regression, neural networkFactors: query, hardware</td></tr><tr><td>Control data base</td><td>Query, user, performance, system descriptors</td><td>Query, user, performance, system descriptors</td></tr><tr><td colspan="3">Decision Support</td></tr><tr><td>User</td><td>Flexible relational query construction interfaceResponse time (output size) estimates prior to query executionGoal seeking capability to maximize informational output within resource constraints</td><td>Response time estimation prior to query execution</td></tr><tr><td>DBA</td><td>Periodic and exception reporting on system statusProvide facilities for active DBA involvement in model/factor selection and modification during system transitionProvide facilities to examine previously acquired knowledge for relevance and fine tune knowledge acquired during system transitions before final assimilation</td><td>Daily reports on MAD levels of one- and two-relation queries, on current day, week and monthException report generated if at least 50% of previous 20 queries have deviations above one unit of MADInformation on system change provided by DBA (CPU upgrade)Search knowledge base on relevant information to generate models/factors that capture and endogenize system changeSelection by DBA of models/factors candidates through active system supportEvaluation of candidates against benchmark queries.Analysis of relative performanceComparative analysis by system of old/new models/factors and their performance (learning phase)DBA fine tunes acquired knowledge prior to final assimilation into knowledge base</td></tr></table>

## 5. Concluding remarks

Providing query evaluation services to users is becoming increasingly important in emerging information technology applications such as decision support systems, data warehousing, and electronic markets. The highly dynamic nature of the operating environments and the high frequency of ad hoc queries limit a direct application of current evaluation models. In this paper, we have proposed a DBMS subsystem which is designed to manage evaluation services and provide expert-level support to the database administration. The objective of the QUEM subsystem is to guarantee that the users will receive satisfactory levels of query evaluation services throughout the life cycle of the database system. To accomplish this, we designed a comprehensive architecture that incorporates a knowledge base, a learning component, and a decision support component.

In order to validate the conceptual design of QUEM we developed and implemented a prototype based on the proposed architecture. The prototype was extensively tested in a quasi-real world setting where it was subjected to significant life cycle changes. The prototype's learning component proved extremely useful in the process of assimilating environment-specific knowledge and explaining the impact of the specific changes on the performance of the evaluation models. The regeneration of new relevant models was successfully conducted, so that specified levels of evaluation performance were attained. The experimental evaluation demonstrated the practical viability of the proposed architecture.

A number of issues deserve further investigation. Our current efforts are directed at the second generation of the QUEST prototype which incorporates new modeling techniques and significantly reduces the time between the detection of performance degradation and new model generation. Also being addressed is the development of a rule-based system for the management of the meta knowledge base to avoid redundancies, incorporate deductive capabilities and resolve information conflicts.

The framework proposed for QUEM is generic; however, many of the implementation aspects in the prototype have focused on the relational model. Extensions to object-oriented, multi-media and textual database contexts will likely yield fruitful design guidelines. Another interesting issue to further investigate relates to the implementation of the QUEM architecture across a distributed communications network. A question that arises is how to build distributed intelligence into the network that facilitates knowledge sharing among different control sites. We are currently pursuing some of these issues.

## Acknowledgements

We would like to thank the associate editor and the referees for insightful comments and suggestions which considerably improved the paper. Helpful comments by Dr. Jim Marsden and Dr. George Scott on earlier drafts are also gratefully acknowledged.

## Appendix A. Relational schema of DWI database

## DRIVER

Number of records: 1500, Record size: 90 bytes
Attribute name Explanation
SSN \* Social Security Number
FNAME First Name
LNAME Last Name
DOB Date of Birth
SEX Gender
ADD Address
LICENSE Driver Has License (Y/N)
STATE State Driver License(Y/N)

## VEHICLE

<table><tr><td colspan="2">Number of records: 1500, Record size: 57 bytes</td></tr><tr><td>Attribute name</td><td>Explanation</td></tr><tr><td>VNO</td><td>Vehicle Registration Number</td></tr><tr><td>VIN</td><td>Vehicle Identification Number</td></tr><tr><td>MAKE</td><td>Make of The Vehicle</td></tr><tr><td>MODEL</td><td>Model of The Vehicle</td></tr><tr><td>YEAR</td><td>Year Manufactured</td></tr><tr><td>INSURED</td><td>Insured (Y/N)</td></tr><tr><td>REGISTER</td><td>Registered (Y/N)</td></tr><tr><td>STATE</td><td>Registered in State (Y/N)</td></tr></table>

## OCCURRENCE

<table><tr><td colspan="2">Number of records 1000, Record size: 115 bytes</td></tr><tr><td>Attribute name</td><td>Explanation</td></tr><tr><td>OCCN</td><td>Occurrence number</td></tr><tr><td>DATE</td><td>Date</td></tr><tr><td>TIME</td><td>Time</td></tr><tr><td>LOCATION</td><td>Location</td></tr><tr><td>AGENCY</td><td>Police Agency in Charge of The Accident</td></tr><tr><td>NHURT</td><td>Number of People Hurt in The Accident</td></tr><tr><td>NKILL</td><td>Number of People Killed in The Accident</td></tr><tr><td>COMMENTS</td><td>Note</td></tr></table>

## DWI

<table><tr><td colspan="2">Number of records: 695, Record size: 104 bytes</td></tr><tr><td>Attribute name</td><td>Explanation</td></tr><tr><td>OCCN</td><td>Occurrence Number</td></tr><tr><td>SSN</td><td>Social Security Number</td></tr><tr><td>BAC</td><td>Blood Alcohol Content</td></tr><tr><td>CHARGE</td><td>Police Charge</td></tr><tr><td>COMMENTS</td><td>Note</td></tr><tr><td>REFUSE</td><td>Driver Refused BAC Test (Y/N)</td></tr></table>

## ACCIDENT

Number of records 1178, Record size: 120 bytes
Attribute name Explanation
OCCN Occurrence Number
SSN Social Security Number
LEFT Driver Left The Scene (Y/N)

<table><tr><td>CHARGE</td><td>Police Charge</td></tr><tr><td>VIN</td><td>Vehicle Identification Number</td></tr><tr><td>COMMENTS</td><td>Note</td></tr></table>

COURT

<table><tr><td colspan="2">Number of records: 1574, Record size: 153 bytes</td></tr><tr><td>Attribute name</td><td>Explanation</td></tr><tr><td>SSN</td><td>Social Security Number</td></tr><tr><td>OCCN</td><td>Occurrence Number</td></tr><tr><td>DATEARR</td><td>Date Arranged</td></tr><tr><td>JUDGE</td><td>Judge</td></tr><tr><td>CLOC</td><td>Court Location</td></tr><tr><td>DATESEN</td><td>Date Sentenced</td></tr><tr><td>GUILTY</td><td>Guilty (Y/N)</td></tr><tr><td>FINE</td><td>Amount Fined</td></tr><tr><td>PTIME</td><td>Sentenced Prison Time</td></tr><tr><td>LCANCEL</td><td>Driver License Cancellation (Y/N)</td></tr><tr><td>EDUCATION</td><td>Driver Education Required (Y/N)</td></tr><tr><td>COMMENTS</td><td>Note</td></tr></table>

## References

[1] A.K. Aggarwal and A.B. Kahn, Managing Query Response Time: Regression Approach, Proceedings of the Decision Science Institute Conference, Miami, FL (1990) 803–805.

[2] Stephen E. Arnold, Online Pricing: Where It's at Today and Where It's Going Tomorrow, Online (March 1989) 6–9.

[3] L. Barney, Data Warehousing Tames a Cyclone of Information, Wall Street and Technology 12, No. 14, June (1995) 68–73.

[4] A. Barua, S. Ravindran and A. Whinston, Supplier Selection Strategies for the Smart Internet Shopper, Working Paper, Management Science and Information Systems, University of Texas at Austin (1994).

[5] A. Basu and R. Blanning, Metagraphs: A Tool for Modelling Decision Support Systems, Management Science 40, No. 12 (December 1994) 1579–1600.

[6] C.A. van den Berg and M.L. Kersten, Analysis of a Dynamic Query Optimization Technique For Multijoin Queries, Journal of Systems Software 27 (1994) 233–241.

[7] A.F. Cardenas, Analysis and Performance of Inverted Database Structures, Communications of the ACM 18, No. 5 (May 1975) 253–263.

[8] T. Cheung, A Statistical Model for Estimating the Number of Records in a Relational Database, Information Processing Letters 15, No. 3, 115–118.

[9] P. Chu, A Contingency Approach to Estimating Record Selectivities, IEEE Transactions on Software Engineering 17, No. 6 (June 1991) 544–552.

[10] J. Fedorowicz, Database Performance Evaluation in an Indexed File Environment, ACM Transactions on Database Systems 12, No. 1 (March 1987) 85–110.

[11] P. Goes, A Stochastic Model for Performance Evaluation of Main Memory Resident Database Systems, ORSA Journal on Computing 7, No. 3 (Summer 1995).

[12] R.D. Gopal, R. Ramesh and S. Zionts, Access Path Optimization in Relational Joins, ORSA Journal on Computing 7, No. 3 (Summer 1995).

[13] R.D. Gopal and R. Ramesh, The Query Clustering Problem: A Set Partitioning Approach, IEEE Transactions on Data and Knowledge Engineering 7, No. 6 (1995).

[14] G. Graefe, Query Evaluation Techniques for Large Databases, ACM Computing Surveys 25, No. 2 (June 1993) 73–170.

[15] A. Gupta, D. Stahl and A. Whinston, Pricing of Services on the Internet, Working Paper, Management Science and Information Systems, University of Texas at Austin (1994).

[16] R. Hackathorn, Data Warehousing Energizes Your Enterprise, Datamation 14, No. 2 (February 1995) 38–45.

[17] Donald T. Hawkins, In Search of Ideal Information Pricing, Online (March 1989) 15–30.

[18] Kalervo Jarvelin, A Methodology for User Charge Estimation in Numeric Online Databanks. Part I: A Review of Numeric Databanks and Charging Principles, Journal of Information Science 14 (1988) 3–16.

[19] Kalervo Jarvelin, A Methodology for User Charge Estimation in Numeric Online Databanks. Part II, Journal of Information Science 14 (1988) 77–92.

[20] Kalervo Jarvelin, An Approach to Query Cost Modeling in Numeric Databases, Journal of The American Society For Information Science (July 1989) 236–245.

[21] J.P. Lomio, The High Cost of NEXIS and What a Searcher Can Do About It, ONLINE (September 1985).

[22] J. Marcus, Mining for Full-Text Gold on a Deadline: Information Technology Subject to Coverage on the Three Major Services, Database 18, No. 2 (April–May 1995) 81–85.

[23] K. Mikkilineni and S.Y.W. Su, An Evaluation of Relational Join Algorithms in a Pipelined Query Processing Environment, IEEE Transactions on Software Engineering 14, No. 6 (June 1988) 838–848.

[24] P. Mishra and M. Eich, Join Processing in Relational Databases, ACM Computing Surveys (1992).

[25] M.A. Morrison, Computers – So Many Choices, So Little Time, Economic Development Review 13, No. 1 (Winter 1995) 8–10.

[26] H.C. Nguyen, A. Ockene, R. Revell and W.J. Skwish, The Role of Detailed Simulation in Capacity Planning, IBM Systems Journal 19, No. 1 (1980) 81–101.

[27] M. O'Leary, The Two Worlds of Online, ONLINE 19, No. 2 (March–April 1995) 49–50.

[28] P. Palvia and S. March, Approximate Block Accesses in Database Organizations, Information Processing Letters 19 (1984) 75–79.

[29] H.G. Perros, A Model for Predicting the Response Time of an On-Line System for Electronic Fund Transfer, Journal of Telecommunication Networks 4, No. 1 (1986) 73–83.

[30] S. Ravindran, A. Barua, B. Lee and A. Whinston, Strategies

for Smart Shopping in Cyberspace, Working Paper, Management Science and Information Systems, University of Texas at Austin (1994).

[31] H. Rubinovitz and B. Thuraisingham, Simulation of Join Query Processing Algorithms for a Trusted Distributed Database Management System, Information and Software Technology (May 1993).

[32] Susan V. Vrbsky and Jane W.S. Jane, Producing Approximate Answers to Set- and Single-Valued Queries, Journal of Systems Software 27 (1994) 243–251.

[33] S.B. Yao, An Attribute Based Model for Database Access Cost Analysis, ACM Transactions on Database Systems 2, No. 1 (1977) 45–67.

![](/api/attachments/W7AWNGE7/fulltext/images/098730cf602f7c6946ebcd566caa6ea9c5ed69dbfe9923c8fc5e2d12b6ef5cdf.jpg)

Paulo B. Goes is Associate Professor of Operations and Information Management at the University of Connecticut. He received a Ph.D. in Computers and Information Systems from the University of Rochester, an M.S. in Production Engineering from the Federal University of Rio de Janeiro, and a B.S. in Civil Engineering from the Federal University of Minas Gerais, Brazil. His research interests include the modeling, design and evaluation of database systems,

communication systems and decision support systems utilizing management science and artificial intelligence techniques.

![](/api/attachments/W7AWNGE7/fulltext/images/d482080db9d0c8b272e624ff59445e050b5f2e5a6738a548f9071d85c37bf43d.jpg)

Ram D. Gopal is Assistant Professor of Operations and Information Management at the University of Connecticut. He received his Ph.D. in Management Systems from S.U.N.Y. at Buffalo in 1993. His current research interests are in the areas of database security, software piracy, database design and IT performance issues. His articles have appeared in the ORSA Journal on Computing, IEEE Transactions on Knowledge and Data Engineering, and Proceedings of the International Conference on Information Systems.

![](/api/attachments/W7AWNGE7/fulltext/images/2a6fa593f6942aa1cefc74f5348bc3f0740d86d92cf2a7f9478e917166674719.jpg)

Nai-Kuang Andrew Chen is Ph.D. student of Operations and Information Management at the University of Connecticut. He received a Bachelor in Business Administration degree from the Soochow University, Taiwan, and a Master of Accountancy degree from the George Washington University. His current teaching and research interest is the management of decision support systems by combining techniques in the field of management information sys-

tems, financial analysis, artificial intelligence, software engineering, network administration, and database management.
