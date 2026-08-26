---
otero_id: 4014
otero_key: "XQDR7VCZ"
title: "Workflow simulation for operational decision support using event graph through process mining"
authors: "Ying Liu; Hui Zhang; Chunping Li; Roger Jianxin Jiao"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Work<sup>fl</sup>ow simulation for operational decision support using event graph through process mining

Ying Liu <sup>a,</sup>⁎, Hui Zhang <sup>b</sup>, Chunping Li <sup>b</sup>, Roger Jianxin Jiao <sup>c</sup>

<sup>a</sup> Department of Mechanical Engineering, National University of Singapore, Singapore 117576, Singapore

<sup>b</sup> School of Software, Tsinghua University, Beijing 100084, China

<sup>c</sup> The G.W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, USA

## a r t i c l e i n f o

Article history: Received 8 July 2010 Received in revised form 24 September 2011 Accepted 3 November 2011 Available online 10 November 2011

Keywords: Business process management Business process simulation Event graph Process mining

## a b s t r a c t

It is increasingly common to see computer-based simulation being used as a vehicle to model and analyze business processes in relation to process management and improvement. While there are a number of business process management (BPM) and business process simulation (BPS) methodologies, approaches and tools available, it is more desirable to have a systemic BPS approach for operational decision support, from constructing process models based on historical data to simulating processes for typical and common problems. In this paper, we have proposed a generic approach of BPS for operational decision support which includes business processes modeling and work<sup>fl</sup>ow simulation with the models generated. Processes are modeled with event graphs through process mining from work<sup>fl</sup>ow logs that have integrated comprehensive information about the control-<sup>fl</sup>ow, data and resource aspects of a business process. A case study of a credit card application is presented to illustrate the steps involved in constructing an event graph. The evaluation detail is also given in terms of precision, generalization and robustness. Based on the event graph model constructed, we simulate the process under different scenarios and analyze the simulation logs for three generic problems in the case study: 1) suitable resource allocation plan for different case arrival rates; 2) teamwork performance under different case arrival rates; and 3) evaluation and prediction for personal performances. Our experimental results show that the proposed approach is able to model business processes using event graphs and simulate the processes for common operational decision support which collectively play an important role in process management and improvement.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Business process management (BPM) has been attracting attention for more than a decade now, and its attention is now shifting from the enactment of business processes towards improving business processes [14]. The <sup>fi</sup>eld of BPM now supports the design, enactment, control and analysis of business processes [41]. An important part of the evaluation of designed and redesigned business processes is business process simulation (BPS). It enables the analysis of business process models with respect to some performance characteristics such as throughput time, cost or resource utilization. In business process analysis and management, it is possible to have multiple change possibilities concerning the process. Therefore, design and redesign of business process play an important role in process performance improvement. Simulation is mentioned as one of the techniques suitable for the support of redesign [18]. After the simulation of a redesigned process, the simulation result is analyzed to provide a quantitative estimate of the impact that the redesign is likely to have on the process performance. The redesigned processes are compared with the current process helping us to make decisions on the best design.

There are a number of BPM and BPS methodologies, approaches and tools available for different applications. However, different model formalisms have different limitations, which make the simulation results deviate from real-world processes. Petri net is a prevailing formalism for process models. However, it is a non-trivial task to mine the relations between activities, such as choice and parallelism, in Petri net. Some tools can deal with loops, but each of them imposes restrictions on the structure of these loops. Although work<sup>fl</sup>ow logs contain rich information, e.g. timestamps, organizer and other process related data, they have not been made full use in the majority of existing modeling formalisms. Therefore, it is necessary to research a better formalism which integrates all the aspects of processes in the model so as to express processes more comprehensively. In the meantime, a generic and systemic approach of BPS is lacking for operational decision support, from constructing process models based on historical data to simulating processes for typical and common problems. Enterprises are increasingly using modern software tools such as work<sup>fl</sup>ow management systems and enterprise resource planning systems in BPM. As a result, these systems contain rich knowledge of business process in the form as historical data, which can be used to discover underlying process models. Based on these models, BPS can be carried out to estimate the impact on process and support operational decision-making when different design possibilities are considered to be implemented. Current research about BPS is primarily concerned with developing simulation theories, methods and software tools that will directly address the problem of process-based organizational design, but it lacks a generic BPS approach for decision support in general applications.

In our attempt to tackle these problems, we propose an approach of work<sup>fl</sup>ow simulation for operational decision support using event graphs, which are constructed from log <sup>fi</sup>les through process mining [22,43] to model business processes and is able to integrate various kinds of process-related information with their different elements. In BPM, we usually need to focus on these problems, i.e. <sup>fi</sup>nding a suitable resource allocation plan to help enterprises to economize on resources and reduce cost, judging whether the coming case arrival rate is under control with a speci<sup>fi</sup>c resource allocation plan to adjust resources <sup>fl</sup>exibly, and analyzing and evaluating personal performances. As a result, we simulate the process based on the generated event graph model under different scenarios and analyze the simulation logs for these three problems: 1) suitable resource allocation plan for a speci<sup>fi</sup>c case arrival rate; 2) teamwork performance under different case arrival rates with a speci<sup>fi</sup>c resource allocation plan; and 3) evaluation and prediction from personal performances. All these three problems play an important role in supporting operational decisions to optimize the process.

The rest of this paper is organized as follows. Section 2 reviews related work on BPS, event graph and process mining. Our approach for work<sup>fl</sup>ow simulation with event graphs through process mining is brie<sup>fl</sup>y outlined in Section 3. Section 4 elaborates the approach of deriving an event graph through process mining and its evaluation plans with a case study of a credit card application. The work<sup>fl</sup>ow simulation for operational decision support based on the generated event graph model is presented in Section 5. We discuss its comparison with Petri nets and our further considerations about event graph in Section 6. Section 7 concludes.

## 2. Related work

## 2.1. Business process simulation

## 2.1.1. State of the art of BPS

The idea of BPS is not new and there are many tutorials, reviews and surveys on it. Paul et al. [26] reviewed the current status of the BPM and BPS domains, discussed some pertinent issues for their successful deployment, and suggested a number of research directions for organizational modeling. Barber et al. [3] reviewed the diverse literature on different BPM and BPS methodologies, approaches and tools available in relation to manufacturing management. Evidence from the literature indicated that few tools are available for supporting manufacturing business process management and that, except for a few small-scale processes, BPS implementations in manufacturing have had limited success. They identi<sup>fi</sup>ed the reasons for this and suggested a practical way forward until hardware and software limitations were overcome. Melão and Pidd [23] surveyed the usage of simulation in the design, modi<sup>fi</sup>cation and improvement of business processes. Hlupic and Vreede [10] investigated the potential of simulation to be used for business process modeling for evaluating alternative business process arrangements, future trends and challenges in BPS. They also discussed business process modeling methods and tools and main challenges and opportunities.

## 2.1.2. Applications of BPS

In modern enterprises, business processes are increasingly recognized as the key to competitive survival. Hence, BPS is used as an important and effective tool to improve the performance of processes. There have been many successful applications reported on different topics, i.e. process management, process improvement and change management.

Aguilar et al. [2] presented to show how simulation was used successfully to support the building of process centered management in a banking environment. Tan [39] proposed an approach of BPS to predict the potential business impacts of introducing an information system. Liu et al. [20] proposed Petri nets extended with time and color as a formalism for supply chain event management.

In process improvement, Simon et al. [38] gave an example to discuss the use of Value Stream Analysis (VSA) to identify inef<sup>fi</sup>ciencies in business processes, how simulation was used to evaluate improvement plans/develop future business scenarios derived from this, and how simulation was used to match available resources to workloads. Jain and Ervin [13] described an effort utilizing modeling and simulation for evaluating the improvements in business processes and systems including a move towards e-business for a logistics and distribution supply chain.

Finally, for change management, Aguilar et al. [2] indicated how BPS could provide support in a process centered management approach to change. Greasley [8] presented a case study of the use of business process simulation within the context of a business-processreengineering approach to change. Greasley [9] used BPS to evaluate the effect of the redesign of a police road traf<sup>fi</sup>c accident reporting system. The simulation method was demonstrated in the context of assisting process change enabled by the use of information systems in an organization in which there had been a historically mixed pattern of success in this activity. Zhang et al. [51] proposed an approach of simulating processes for runtime change management with event graphs.

## 2.1.3. Modeling formalisms for BPS

Due to different process modeling formalisms, the theoretical basis and implementation solution of BPS are also different from each other. We observe that there are three main formalisms, i.e. Petri net, IDEF and UML.

In process mining and modeling, Petri net is a prevailing formalism so there has been a lot of research about business process modeling and simulation with it. For example, Jörg and Thomas [16] simulated business processes with Petri net models by generating partially ordered runs and they also showed how these runs could then be used for performance analysis of important key indicators such as throughput time. With work<sup>fl</sup>ow technology, Petri net theory and simulation technology, a work<sup>fl</sup>ow engine independent business process analyzing system was realized to provide Petri net-based business process analysis [45]. Great work on BPS based on Petri net has been done by the Architecture of Information Systems (AIS) group. Reijers and ver dan Aalst [27] introduced short-term simulation by showing the relations and differences between strategic simulation and operational control. The data that might be used for this kind of decision was outlined and a simulation architecture applied in practice was also presented. Although simulation was used to analyze business processes at some stage, it was not used in a structured and effective manner, ver dan Aalst et al. [44] argued that there were also several additional and more fundamental problems. For example, the focus was mainly on design, not for operational decision-making. There was limited support for using existing artifacts such as historical data and work-<sup>fl</sup>ow schemas. The behavior of resources was modeled in a rather naive manner. Focusing on the latter problem, it proposed a new way of characterizing resource availability. Experiments using CPN Tools showed that it was indeed possible to capture human behavior in business processes in a better way. Wynn et al. [30,48] investigated the requirements for a process simulation environment that allowed simulation experiments to start from an intermediate execution state, instead of an empty execution state. They proposed an architecture addressing these requirements and demonstrated it through a case study conducted using the YAWL work-<sup>fl</sup>ow engine and CPN simulation tools.

IDEF is a method intended to capture the knowledge about how a particular system works. Ning et al. [24] introduced an IDEF3-based simulation modeling method and the relevant software tool, Easy IDEF3TM, to collect the necessary simulation information and describe it in a formalized way based on the communication-oriented IDEFS method. Based on the extended IDEF3 method, a hierarchical business process simulation modeling method was proposed, which inherited the hierarchical description capability of the IDEF3 method and supported integrative modeling of different objects (i.e. activity, entity, resource and role) with multiple abstraction levels [25].

For UML, De Cesare and Serrano [7] proposed a collaborative model using UML and business process simulation by mapping the constructs used in information system models to those used in business process models. Xie [49] enhanced the UML activity diagram's ability of describing process and added some information which the simulation needed. After that, the principles and methods used to translate the extended activity diagram into the GPSS model, were proposed to realize the integration of the static model and the dynamic model.

Besides these formalisms above, there have been other interesting methods for business process modeling and BPS, such as algebra event regular expression [32], DEMO [17] and so on.

Through our literature review in relation to BPS, we found that there have been many modeling formalisms and methods of BPS for different applications. However, there lacks a general approach for the entire process of BPS, from building the process models automatically to simulating the processes systematically for operational decision support. Besides, we aimed to discover a modeling formalism to integrate all the aspects of processes and make the BPS come nearer the truth so that the simulation results are more convincing. All these motivated us to simulate business processes using a different formalism.

## 2.2. Event graph

Event graphs were <sup>fi</sup>rst presented by Schruben [35] to develop simulations of discrete event systems. The system dynamics are characterized by events that change the state of the system and the logical and temporal relationships among events (See Fig. 1). Later in 1988, Schruben and Yucesan [37] presented a simulation graph as the mathematical formalization and extension of event graphs. A simulation graph is an ordered quadruple $\mathrm { G } = ( \nu ( \mathrm { G } ) , \mathfrak { E } _ { s } ( \mathrm { G } ) , \mathfrak { E } _ { \mathrm { c } } ( \mathrm { G } ) , \Psi ( \mathrm { G } ) )$ where $\nu ( G )$ is the vertex set of ${ \sf G } , \ { \sf \varepsilon _ { s } } ( { \sf G } )$ is the set of scheduling edges of ${ \sf G } , \varepsilon _ { \sf c } ( { \sf G } )$ is the set of canceling edges of G and $\Psi ( \mathbf G )$ is the incidence function. Based on the simulation graph, they formally de-<sup>fi</sup>ned the simulation model in that paper. Collectively, <sup>fi</sup>ve key elements play an important role in our simulation graph model, i.e. event vertex, state variable, edge condition, transition function and time delay. In simulation graphs, every vertex stands for an event and it must be regarded as instantaneous. State variable is used to integrate enterprise information in the models. Edge condition helps control the process <sup>fl</sup>ow so that it is relatively easy to build the activity processes. In this case, we need not be concerned about different logical relationships (e.g. choice, parallelism) between activities except the causality relation. Transition function re<sup>fl</sup>ects changes of state variables made at event vertexes. Time delay plays a signi<sup>fi</sup>cant role in analyzing the temporal information of different tasks and the whole process.

![](/api/attachments/XQDR7VCZ/fulltext/images/1299eb5fb93e94348a25d606e74c56b3abe9345519abf57975b00f01fecc3e17.jpg)  
Fig. 1. A fundamental event graph. The occurrence of event A causes event B to be scheduled after a time delay t, providing condition S>0 is true (after the state transition for event A has been made, where S is the state variable).

After the proposal of simulation graphs, researchers in the community actually did not make any distinction between event graphs and simulation graphs. The modeling power of event graphs was demonstrated by presenting a model simulating a Turing machine. Therefore, according to Church's thesis, event graph models are able to model any system that can be implemented on a modern computer [34]. Because of its simplicity and modeling power, some researchers began to model and simulate processes with event graphs. Sargent [33] modeled a simple manufacturing system using event graphs to illustrate its modeling and analysis. Buss [4] demonstrated the ability of event graphs to leverage simple models into more complex ones with very few additional features. A simulation modeling methodology was developed and implemented, combining discrete event simulation with qualitative simulation. It implemented the temporal interval speci<sup>fi</sup>cations in the discrete event model and constructed a temporal interval clock for the qualitative simulation model [12]. Lara [19] presented an extension to the classical event graphs formalism oriented towards the speci<sup>fi</sup>cation of component-based models.

In the existing works about event graphs, we note that they possess different elements which can be utilized to model various aspects of business processes. Besides, there have been successful applications of modeling and simulating processes with event graphs. Therefore, we aim to explore the possibility for BPS using event graphs.

## 2.3. Process mining

Process mining was <sup>fi</sup>rst introduced by Agrawal et al. [1]. This work was built up based on the work<sup>fl</sup>ow graphs and it de<sup>fi</sup>ned two problems, i.e. <sup>fi</sup>nding a conformal process model generating events appearing in a given work<sup>fl</sup>ow log and <sup>fi</sup>nding the de<sup>fi</sup>nition of edge conditions. A concrete algorithm was given to tackle the <sup>fi</sup>rst problem. Cook and Wolf [6] investigated process discovery in the context of software engineering processes. They described three methods for process discovery: one using neural networks, one using a purely algorithmic approach and one using the Markovian approach. The latter two were considered the most promising approaches. An important branch of studies in process mining is centered on the algorithms based on Petri nets [46]. The classic α-algorithm [42] is able to construct a corresponding Petri net based on event logs. Later, various algorithms based on α-algorithm were reported. For instance, a synchronization-based model to deal with the invisible tasks and short-loops [50], a novel approach for process mining to explicitly detect parallelism [47]. However, there are some dif<sup>fi</sup>culties for α- algorithm, such as mining duplicated tasks, hidden tasks and loops. At the same time, Petri nets do not make full use of the process information readily available. As a result, we aim to <sup>fi</sup>nd a better solution to these problems using event graphs.

Compared with existing work about BPS, event graphs and process mining, our work is characterized by the focus on a general approach of BPS for operational decision support. We mine business processes from work<sup>fl</sup>ow logs through process mining and express them with event graphs, which integrate the control-<sup>fl</sup>ow aspect, data aspect and resource aspect of processes. Based on the generated model, we proceed with BPS for three typical problems mentioned in Section 1 to help decision makers achieve process improvement and optimization.

## 3. A work<sup>fl</sup>ow simulation framework based on event graphs

The focus of our research is to present a generic and systematic approach for operational decision support with event graphs, which includes two parts, i.e. deriving event graph models from logs through process mining and simulating constructed models for operational decision support. The proposed work<sup>fl</sup>ow simulation approach based on event graphs is shown in Fig. 2. Any information system using transactional systems such as enterprise resource planning, customer relationship management or work<sup>fl</sup>ow management systems will provide work<sup>fl</sup>ow information in some form and to some extent, such as tasks available, their events and the details of these events like starting/ending timestamp. A work<sup>fl</sup>ow log is often a consistent XML document containing such information [40]. In our study, we <sup>fi</sup>rst aim to extract information from such logs and derive an event graph through process mining. In order to make full use of the rich information in logs, we build event graph models via <sup>fi</sup>ve main steps, constructing activity process, extracting state variables, mining edge conditions, establishing transition functions and dealing with time delays. By this means, we pull together various aspects of processes with different elements of event graphs so as to make the models more comprehensive. Later, we plan to look into representative problems for operational decision support. Based on the model discovered, we simulate the processes under different scenarios and obtain the simulation logs. The analytical results of simulation logs can be used to make operational decisions so as to optimize business processes and improve enterprise competitiveness. On the basis of the proposed approach shown in Fig. 2, Section 4 elaborates the approach of deriving an event graph using process mining and its evaluation plans through a case study. Section 5 presents the work<sup>fl</sup>ow simulation towards operational decision support based on the event graph model generated.

## 4. Deriving an event graph: a case study

In this section, we demonstrate the crucial steps in deriving an event graph through process mining using event logs. Since one of the main purposes in this paper is to validate the feasibility of the proposed approach, we are using simulation logs. In the way, the underlying process model is made known and we can steadily evaluate the performance of the proposed approach when the model derived is compared with the known one. However, we envision that the power of the proposed approach is actually with the process where the classic approaches can hardly deliver sound results largely because the underlying true model is too complicated or too dif<sup>fi</sup>cult to be discovered or restored. This applies to many scenarios like online ecommerce, social networks, logistics environment using RFID, and so on. This is also the key reason why we are motivated to pursue this research.

![](/api/attachments/XQDR7VCZ/fulltext/images/ddc5b7224f55f894f94c80323ba092bf41dedc49712030b768b272d4c8d2ead1.jpg)  
Fig. 2. A work<sup>fl</sup>ow simulation approach based on event graphs.

## 4.1. Experimental setup

We obtain event log <sup>fi</sup>les through simulation by using a credit card application process as a case study [30]. This case, being expressed as a YAWL<sup>1</sup> work<sup>fl</sup>ow model, is shown in Fig. 3. The process starts when an applicant submits an application. Upon receiving an application, a credit clerk checks whether it is complete. If not, the clerk requests additional information and waits until this information is received before proceeding. For a complete application, the clerk performs further checks to validate the applicant's income and credit history. Different checks are performed depending on whether the requested loan is large (e.g. greater than \$500) or small. The validated application is then passed on to a manager to decide whether to accept or reject the application. In the case of acceptance, the applicant is noti<sup>fi</sup>ed of the decision and a credit card is produced and delivered to the applicant. For a rejected application, the applicant is noti<sup>fi</sup>ed of the decision and the process ends.

According to that paper, we can generate simulation models from the (1) extracted work<sup>fl</sup>ow speci<sup>fi</sup>cation, (2) the newly extracted organizational model, and (3) the event log <sup>fi</sup>le. We downloaded these three <sup>fi</sup>les from the website.<sup>2</sup> As the event log <sup>fi</sup>le of YAWL lacks realistic timing behavior and we need to look into the temporal information, we make some changes on the timestamps in the <sup>fi</sup>le to better <sup>fi</sup>t our requirement. Under the guidelines of that paper, we generated the event logs for this case study via the following steps: 1) import the work<sup>fl</sup>ow and organizational model and the event log from YAWL and analyze them in ProM<sup>3</sup>; 2) integrate simulation-relevant information from the organizational model and log analysis into the YAWL model via ProM; 3) convert the YAWL model into a Petri net model via ProM; 4) export the integrated and converted model as a Coloured Petri Net model via ProM; 5) simulate the Coloured Petri Net [15] model in CPN Tools and get partial MXML log <sup>fi</sup>les; and 6) aggregate the partial MXML log <sup>fi</sup>les to the <sup>fi</sup>nal MXML log <sup>fi</sup>le.

After these steps, we obtain the MXML log <sup>fi</sup>le of the credit application, part of which is shown in Fig. 4. It consists of 17,900 events in total, 1050 cases with 12 different tasks.

## 4.2. Constructing the event graph through process mining

In our research, we view business process as a combination of different activities with a structure describing their logical order and dependency. At <sup>fi</sup>rst, we aim to model a process by constructing an event graph where the graph itself is discovered through process mining. The event graph formed helps us to simulate the process under different scenarios for operational decision support. Besides the control-<sup>fl</sup>ow aspect, in addition, event graphs combine other enterprise information such as data aspect and resource aspect. In this case, the approach for constructing event graphs through process mining consists of several steps for different components. Based on our previous study [52], we summarize the <sup>fi</sup>ve main steps of our approach shown in Fig. 2.

![](/api/attachments/XQDR7VCZ/fulltext/images/de5d3cf0e562c2d7e6649284d4189ab19d86508162612ecb2a5542ec351aca67.jpg)  
Fig. 3. A credit card application process modeled in YAWL.

![](/api/attachments/XQDR7VCZ/fulltext/images/38307a510e6d6dd6a73b0ec26116a0739b81a9c0e0588bf1c50269e3faa51b30.jpg)  
Fig. 4. Part of an example log <sup>fi</sup>le of the credit card application process.

## 4.2.1. Constructing activity process

Unlike the Petri net, event graphs do not need to concern themselves with different types of logical relations such as choice and parallelism. We only need to construct the causality relations, because the <sup>fl</sup>ow control relies on the edge conditions. Therefore, activity processes with causality relations form the crucial architecture of an event graph. We de<sup>fi</sup>ne the directly-follow-relation and the causality relation between activities as:

De<sup>fi</sup>nition 1. A>B: event A is directly followed by another event B in a trace in the logs.

De<sup>fi</sup>nition 2. A→B: event A causes event B to happen in the process.

De<sup>fi</sup>nition 3. $F ( \mathsf { A } \to \mathsf { B } ) { = } ( \sum V ( \mathsf { A } > \mathsf { B } ) ) / ( \# \mathsf { A } ) { : } V ( \mathsf { A } > \mathsf { B } )$ is the directlyfollow-relation counter for A>B. When A is directly followed by B in a trace, the counter is increased by 1. F(A→B) is to indicate the relation for A causing B. It equals the directly-follow-relation counter divided by the overall frequency of event A (#A).

Noted from the logs, since each task has two records in every case for its start and completion respectively (See Fig. 4), it is mapped into a starting vertex and an ending vertex and the time between these two vertexes can be taken as the duration of this task. We name each event as its initial task name together with its state shown in Table 1. Event vertexes are regarded as instantaneous.

Based on the proposal of instantaneous events, we construct an activity process like this. For event A, we aim to calculate all F(A→B) for every other event B covering all the traces by summing directly-follow-relation counter and dividing it by the overall frequency of event A (#A). After we shift other events for A and repeat this process, we can get the <sup>fi</sup>nal causality matrix. Note that tasks are not nested, which means if a task starts, it will not schedule another task before it completes. In this case, for each starting event vertex (it indicates the starting of a task), one vertex, and only one, that is the corresponding ending vertex, is its subsequence. For each ending vertex, we need only consider all the other starting vertexes as candidates of its subsequences. By this means, we obtain the causality metric from ending vertexes to starting vertexes. Based on causality metric, for every row, we consider the values larger than λ. Here the parameter λ is set for extracting the correct causality relations from noises. For every value larger than λ, the corresponding events are regarded as subsequent events. Here we set λ to 0.005. That is to say, when A occurs 1000 times and A is directly followed by B less than 5 times, it is impossible for A→B. Finally, we obtain the causality relations from ending vertexes to starting vertexes in Table 2 and <sup>fi</sup>nally construct the activity process in Fig. 5.

## 4.2.2. Extracting state variables

The state variables are crucial in event graphs and are usually mapped from the enterprise information. In this way, it is able to combine both data structure and behavior in a single entity. We need to extract all the information in the work<sup>fl</sup>ow logs and determine how they could be mapped into state variables. We consider two types of state variables, non-resource variables and resource variables. The former are usually process related information such as amount of products, cost or Boolean values for decisions. The latter are staff in charge of different tasks.

For the non-resource variables, after getting raw data from the logs, we <sup>fi</sup>rst carry out in-depth statistical analysis using Weka<sup>4</sup> — a well-known open source data mining platform [11]. Based on the statistical results, we determine which data features should be mapped into the state variables and what their types and ranges are. As for resource variables, we extract all the originators of all the events and calculate the total number of resources and numbers of resources in charge of different events. Based on these data, we map the resources into different state variables according to their different roles and initialize them with their amounts. If the organizational <sup>fi</sup>les about processes are available, it will help us to handle role mapping. Alternatively, expert veri<sup>fi</sup>cation is an option.

Table 1  
Event name table of the credit card application.

<table><tr><td>Event</td><td>Event name</td><td>Event</td><td>Event name</td></tr><tr><td> $e_1$ </td><td>receive_application_start</td><td> $e_2$ </td><td>receive_application_complete</td></tr><tr><td> $e_3$ </td><td>check_for_completeness_start</td><td> $e_4$ </td><td>check_for_completeness_complete</td></tr><tr><td> $e_5$ </td><td>get_more_info_start</td><td> $e_6$ </td><td>get_more_info_complete</td></tr><tr><td> $e_7$ </td><td>check_loan_amount_start</td><td> $e_8$ </td><td>check_loan_amount_complete</td></tr><tr><td> $e_9$ </td><td>perform_checks_for_large_amount_start</td><td> $e_{10}$ </td><td>perform_checks_for_large_amount_complete</td></tr><tr><td> $e_{11}$ </td><td>perform_checks_for_small_amount_start</td><td> $e_{12}$ </td><td>perform_checks_for_small_amount_complete</td></tr><tr><td> $e_{13}$ </td><td>make_decision_start</td><td> $e_{14}$ </td><td>make_decision_complete</td></tr><tr><td> $e_{15}$ </td><td>start_approval_start</td><td> $e_{16}$ </td><td>start_approval_complete</td></tr><tr><td> $e_{17}$ </td><td>notify_acceptance_start</td><td> $e_{18}$ </td><td>notify_acceptance_complete</td></tr><tr><td> $e_{19}$ </td><td>deliver_credit_card_start</td><td> $e_{20}$ </td><td>deliver_credit_card_complete</td></tr><tr><td> $e_{21}$ </td><td>complete_approval_start</td><td> $e_{22}$ </td><td>complete_approval_complete</td></tr><tr><td> $e_{23}$ </td><td>notify_rejection_start</td><td> $e_{24}$ </td><td>notify_rejection_complete</td></tr></table>

In this log <sup>fi</sup>le of credit card application, we consider two types of data with the tags “Attribute” and “Originator” for non-resource and resource state variables respectively. For the data in the “Attribute” tag, we extract them from the log <sup>fi</sup>les, transform them into the training <sup>fi</sup>le and analyze them in Weka. Based on the statistical results, we obtain the type and range of these data. As for the “Originator” tag, we count operators for different events, through which we can see that there are <sup>fi</sup>ve clerks and three managers. Managers are in charge of events ${ \tt e } _ { 1 0 }$ and ${ \mathsf { e } } _ { 1 4 }$ and clerks are in charge of the others. Finally, we obtain the state variables in Table 3.

## 4.2.3. Mining edge conditions

Edge condition is an important component of event graphs, because it plays an important role in controlling the process <sup>fl</sup>ows so that it is not necessary to pay much attention to the logical relations between activities. State variables are included in edge conditions. As a result, there are two types of edge conditions due to different state variables.

Edge conditions with non-resource state variables should be considered when an event has two or more subsequent events. Thus, we extract all these events, their subsequent events and all the interrelated state variables. The state variables are kept as attributes and the names of subsequent events are kept as class labels. By this means, all the information is extracted and transformed into training data for classi<sup>fi</sup>cation in Weka by which a set of classi<sup>fi</sup>cation rules are generated. We then take the rules generated as edge conditions. Such rules can surely be veri<sup>fi</sup>ed by human experts later on. In this case study, after extracting the events $\mathsf { e } _ { 4 } , \mathsf { e } _ { 8 }$ and $\mathsf { e } _ { 1 4 } ,$ their subsequent events and all the interrelated state variables as training data, we apply the RandomTree (with parameters $- \mathbf { k } \ : 1 - \mathbf { M } \ : 1 . 0 - \mathsf { S } 1 )$ for classi<sup>fi</sup>cation in Weka. We then generate the rules with non-resource state variables in Table 4. For edges conditions including resource state variables, when starting a task, we add an edge condition that the number of the corresponding role of this task is larger than zero. Finally, the conjunctions of these two kinds of edge conditions are placed along the corresponding edges.

Causality metric of the credit card application. Events $\mathsf { e } _ { 1 }$ to ${ \sf e } _ { 2 4 }$ are events in Table 1. Every cell denotes the causality value between two events and three decimal places are kept. For example, the value 1.0 in row 2 and column 3 means that the causality value for $\mathsf { e } _ { 2 } \to \mathsf { e } _ { 3 }$ is 1.0. Grids with $\cdot ^ { * } - \ "$ denote 0.

<table><tr><td></td><td> $e_1$ </td><td> $e_3$ </td><td> $e_5$ </td><td> $e_7$ </td><td> $e_9$ </td><td> $e_{11}$ </td><td> $e_{13}$ </td><td> $e_{15}$ </td><td> $e_{17}$ </td><td> $e_{19}$ </td><td> $e_{21}$ </td><td> $e_{23}$ </td></tr><tr><td> $e_2$ </td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_4$ </td><td>-</td><td>-</td><td>0.26</td><td>0.740</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_6$ </td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_8$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.972</td><td>0.028</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_{10}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_{12}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_{14}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.608</td><td>-</td><td>-</td><td>-</td><td>0.392</td></tr><tr><td> $e_{16}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.5</td><td>0.5</td><td>-</td><td>-</td></tr><tr><td> $e_{18}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.003</td><td>0.925</td><td>-</td></tr><tr><td> $e_{20}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>0.002</td><td>-</td><td>0.075</td><td>-</td></tr><tr><td> $e_{22}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $e_{24}$ </td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

## 4.2.4. Establishing transition functions

Transition functions represent how event vertexes affect state variables and it is not so easy to mine them automatically. This is actually because enterprise information is complex due to numerous names, different types, complex relations, and so on. Just the same as edge conditions, there are also two types of transition functions because of two different state variables.

For transition functions with non-resource state variables, we consider two situations. The <sup>fi</sup>rst is when a state variable shows up for the <sup>fi</sup>rst time at an event vertex. In this case, we consider that the event vertex will alter the state variable from its default value (for example, zero for numeric) to a random value but still in the corresponding range. The second is when the state variables do not appear for the <sup>fi</sup>rst time they are changed. In this case, we have made a simple assumption that all the state variables, before and after a certain event, are basically located in the same semantic layer and are in the same order so that the transition function can be realized through some simple mathematic formation like addition and subtraction. Therefore, we can deal with the transition functions for the latter situation with multi-linear <sup>fi</sup>tting, where the coef<sup>fi</sup>cients in the multi-linear equations are 0, 1 or −1. For example, the state variable A changes after an event $\mathrm { e _ { i \cdot } }$ There are other states variables B, C and D before the occurrence of $\mathsf { e } _ { \mathrm { i } } .$ So the problem is to <sup>fi</sup>nd the <sup>fi</sup>tting coef<sup>fi</sup>cients for Eq. (1):

$$
A _ {1} = a \cdot A _ {0} + b \cdot B + c \cdot C + d \cdot D\tag{1}
$$

where $\mathsf { A } _ { 0 }$ and $\mathsf { A } _ { 1 }$ are the values of state variable A before and after the occurrence of $\mathsf { e } _ { \mathrm { i } }$ respectively. Coef<sup>fi</sup>cients a, b, c and d are any of 0, 1 $0 \mathrm { r } - 1$ . In this case study, we only have the <sup>fi</sup>rst one in that a state variable shows up for the <sup>fi</sup>rst time. So we consider that the event vertex will alter the state variable from its default value to a random value but still in the corresponding range. Based on the statistical results of these state varibles, we obtain the transition functions in Table 5. Beside these transition functions about non-resource state varibles, we then set the number of the corresponding role decreased by one at a starting vertex and increased by one at an ending vertex. By this means, the transition functions with resource state variables C and M are added to the model.

![](/api/attachments/XQDR7VCZ/fulltext/images/a29e16351dfb4492d84b6c1916c13ad0e29a1560ad67958defe308faad09ab9c.jpg)  
Fig. 5. Activity process of the credit card application. Events $\mathsf { e } _ { 1 }$ to ${ \tt e } _ { 2 4 }$ are events in Table 1.

Table 3  
Table of state variables. C and M are resource state variables, while loanAmt, comple teApp and decideApp are non-resource state variables.

<table><tr><td>Name</td><td>Type</td><td>Values</td><td>Notes</td></tr><tr><td>C</td><td>Integer</td><td>[0, 5]</td><td>The number of Clerks.</td></tr><tr><td>M</td><td>Integer</td><td>[0, 3]</td><td>The number of Managers.</td></tr><tr><td>loanAmt</td><td>Integer</td><td>[272, 7972]</td><td>The amount of money in the credit application.</td></tr><tr><td>completeApp</td><td>Boolean</td><td>{true, false}</td><td>Indicates whether the application is complete.</td></tr><tr><td>decideApp</td><td>Boolean</td><td>{true, false}</td><td>Indicates whether the application is approved.</td></tr></table>

## 4.2.5. Dealing with time delays

Temporal information is also a signi<sup>fi</sup>cant factor for business process. However, it has not been made full use of in the majority of existing studies. Event graphs contain time delays on edges and through which it obtains a global clock in simulation. It is also useful for other in-depth studies, e.g. mining important information, evaluating process performance and so on. In event graphs, every event vertex is regarded as instantaneous and time delays are expressed on edges. We have chosen to map every task into two vertexes each with a starting vertex and an ending vertex. Therefore, the time delay between them is taken as the duration of the event. Meanwhile, we note that tasks in this case study are unseamed. That is to say there is no time gap between the ending vertex of one task and the starting vertex of another task. After extracting timestamps from log <sup>fi</sup>les, we calculate the time gaps between events with a causality relation and analyze them with the help of Weka. Finally, we determine the time delays in Table 6.

## 4.3. Event graph model formed

After the <sup>fi</sup>ve steps above, we have identi<sup>fi</sup>ed activity process, state variables, edge conditions, transition functions and time delays. Now we are able to construct the event graph model of the credit card application. Fig. 6 presents a full view of the event graph model constructed with the model characteristics listed below the activity process for better visualization.

## 4.4. Evaluation of the constructed event graph model

It has been pointed out that although there has been a lot of progress in developing progress mining algorithms in recent years, no effort has been invested in developing a common means to assess the quality of the models discovered [29]. Combining existing evaluation strategies for process and our own ideas, we aim to evaluate our approach of deriving an event graph through process mining by measuring precision, generalization and robustness.

Table of edge conditions. Note that only edges conditions with non-resource state variables are listed.

<table><tr><td>Starting</td><td>Ending</td><td>State variables</td><td>Classified rules</td><td>Verified rules</td></tr><tr><td rowspan="2"> $e_{4}$ </td><td> $e_{5}$ </td><td rowspan="2">completeApp</td><td>completeApp = false</td><td>completeApp = false</td></tr><tr><td> $e_{7}$ </td><td>completeApp = true</td><td>completeApp = true</td></tr><tr><td rowspan="2"> $e_{8}$ </td><td> $e_{9}$ </td><td rowspan="2">loanAmt</td><td>loanAmt &gt; = 506</td><td>loanAmt &gt; = 500</td></tr><tr><td> $e_{11}$ </td><td>loanAmt &lt; 506</td><td>loanAmt &lt; 500</td></tr><tr><td rowspan="2"> $e_{14}$ </td><td> $e_{15}$ </td><td rowspan="2">decideApp</td><td>decideApp = true</td><td>decideApp = true</td></tr><tr><td> $e_{23}$ </td><td>decideApp = false</td><td>decideApp = false</td></tr></table>

Table 5  
Table of transition functions. Note that only transition functions with non-resource state variables are listed.

<table><tr><td>Event</td><td>State Varibale</td><td>Values</td><td>Transition functions</td></tr><tr><td> $e_{2}$ </td><td>loanAmt</td><td>[272, 7972]</td><td>loanAmt = [272, 7972]</td></tr><tr><td> $e_{4}$ </td><td>completeApp</td><td>{true, false}</td><td>completeApp = {x|x=true or x=false}</td></tr><tr><td> $e_{14}$ </td><td>decideApp</td><td>{true, false}</td><td>decideApp = {x|x=true or x=false}</td></tr></table>

Firstly, we compare our model with the benchmark baseline, i.e. the prede<sup>fi</sup>ned YAWL model. After our careful and comprehensive examination, we found that the basic activity process in our event graph is well aligned with the origin model. It counts for the correctness of the crucial architecture of our model. Next, we aim to measure how well the event logs and constructed process models match. One approach is to generate all execution sequences allowed by the model and then compare them with the log traces [28]. We simulate the event graph model and obtain epoches as new logs $\left( \mathrm { L } _ { \mathrm { n } } \right)$ and compare it with the origin logs $\left( \mathrm { L } _ { \mathrm { o } } \right)$ . We are able to measure the precision and generalization de<sup>fi</sup>ned as follows and the results in Table 7 show that our approach has gained good precision and acceptable generalization.

Precision: $\begin{array} { r } { p = \frac { | \mathrm { L } _ { \mathrm { n } } \cap \mathrm { L } _ { 0 } | } { | \mathrm { L } _ { \mathrm { n } } | } } \end{array}$ calculates how many new traces are included in the origin traces;

Generalization: $\begin{array} { r } { g = \frac { | \mathrm { L } _ { \mathrm { n } } \cap \mathrm { L } _ { 0 } | } { | \mathrm { L } _ { 0 } | } } \end{array}$ calculates how many origin log traces are included in the new traces generated by simulating event graph models.

Besides the precision and generalization, we also expect to evaluate the robustness of our approach. In our study, the crucial part is the step to construct activity process. Therefore, we assess the performance of this step with different datasets which contain noisy logs. For comparison, we create the noisy logs by three manners: adding events, deleting events and disordering events from normal logs and mix them with the normal logs. The percentage of noise in new logs is 3%, 5%, 10%, 12% and 15% respectively. Then we apply our approach of constructing activity process based on different percentages of noise respectively and see whether our approach can still obtain the correct causality relations in the presence of noises. The results are shown in Table 8. Through Table 8 it can be seen that our approach can obtain the correct causality relations under different noisy conditions. In this case, we can construct the right activity processes of event graphs. So it has good robustness to deal with noise.

Table 6  
Table of time delays. Events $\mathsf { e } _ { 1 }$ to ${ \tt e } _ { 2 4 }$ are events in Table 1.

<table><tr><td colspan="2">Starting</td><td> $e_1$ </td><td> $e_3$ </td><td> $e_5$ </td><td> $e_7$ </td><td> $e_9$ </td><td> $e_{11}$ </td><td> $e_{13}$ </td><td> $e_{15}$ </td><td> $e_{17}$ </td><td> $e_{19}$ </td><td> $e_{21}$ </td><td> $e_{23}$ </td></tr><tr><td colspan="2">Ending</td><td> $e_2$ </td><td> $e_4$ </td><td> $e_6$ </td><td> $e_8$ </td><td> $e_{10}$ </td><td> $e_{12}$ </td><td> $e_{14}$ </td><td> $e_{16}$ </td><td> $e_{18}$ </td><td> $e_{20}$ </td><td> $e_{22}$ </td><td> $e_{24}$ </td></tr><tr><td rowspan="2">Time (minutes)</td><td>Min</td><td>1</td><td>10</td><td>50</td><td>2</td><td>25</td><td>15</td><td>10</td><td>1</td><td>5</td><td>10</td><td>1</td><td>2</td></tr><tr><td>Max</td><td>3</td><td>15</td><td>100</td><td>5</td><td>35</td><td>20</td><td>15</td><td>3</td><td>8</td><td>15</td><td>3</td><td>5</td></tr></table>

![](/api/attachments/XQDR7VCZ/fulltext/images/4590b83b37b06e37026ed3c1002683074c7bd29d4e5d26136652a75b874313f9.jpg)

![](/api/attachments/XQDR7VCZ/fulltext/images/26e207575ae332d3878ca40b799d0cf0399af7f868207c57df77e05f943da2e0.jpg)  
Fig. 6. Event graph model of a credit card application. The <sup>fi</sup>rst vertex named Start is a starting vertex of this event graph. Events e<sub>1</sub> to e<sub>24</sub> are events in Table 1. The notations with RND along with the edges denote time delays. RND is a Sigma function for random numbers. For example, 1+2 RND denotes random numbers between 1 and 3.

Table 7  
Comparison of LogA and LogB. NoC is the number of traces. NoT is the number of event names. NoE is the number of total events in the log. NoIT is the number of traces of one log included in the other log. Ratio denotes what percentage of traces in one log is included in the other log.

<table><tr><td>Logs</td><td>NoC</td><td>NoT</td><td>NoE</td><td>NoIT</td><td>Ratio</td></tr><tr><td>LogA</td><td>1050</td><td>24</td><td>17,900</td><td>771</td><td>73.43%</td></tr><tr><td>LogB</td><td>1050</td><td>24</td><td>17,868</td><td>1049</td><td>99.9%</td></tr></table>

## 5. Work<sup>fl</sup>ow simulation for operational decision support based on event graphs

Through process mining, we construct the event graph model of the credit card application. Based on the generated model, we simulate the process and analyze the simulation logs in order to support operational decisions. Although there is a software environment, Sigma,<sup>5</sup> for discrete event simulation, it has some limitations with regard to its simulation power. The most important one is that the case arrival rate cannot be con<sup>fi</sup>gured so that we are not able to simulate the process under some speci<sup>fi</sup>c scenarios that we need. In this case, we wrote a program for simulating the event graph model ourselves. The architecture for simulating the event graph model with our program is shown in Fig. 7. At <sup>fi</sup>rst, we con<sup>fi</sup>gure the total case number, the case arrival rate, and the number of clerks and managers. When executing the simulation, it initializes the program through reading the con<sup>fi</sup>gure <sup>fi</sup>le, creating a case distributor thread and the corresponding numbers of clerk thread and manager thread. Case distributor thread launches cases according to the con<sup>fi</sup>gured rate and generates tasks in the task queue. Clerk threads and manager threads process their tasks and keep communicating with the task queue. During the execution, logs are recorded for the whole process, which are analyzed for exploring different problems for operational decision support.

In BPM, we usually need to focus on problems which can help en terprises economize on resources, reduce cost and improve competitiveness, such as resource allocations, performance evaluation and prediction. As a result, based on our event graph model, we simulate the process for three typical and common problems:

• Problem 1: Suitable resource allocation. If the case arrival rate is unchanged, what is the suitable resource allocation plan? Is the proportion of different roles appropriate?

• Problem 2: Teamwork Performance Estimation. If the resource allocation is unchanged, how about the process performance under the situations of different case arrival rate? Are they under the control of the current speci<sup>fi</sup>c resource plan?

• Problem 3: Personal Performance Estimation. How about individual performances during the process? What can we learn from these personal performances?

## 5.1. Resource allocation planning

In this subsection, we aim to discover the suitable resource allocation through work<sup>fl</sup>ow simulation and check out whether the proportion of different roles is appropriate. In this way it helps enterprises to reallocate resources so that they can save costs and improve work ef-<sup>fi</sup>ciency. For the <sup>fi</sup>rst problem, one direct method is to simulate the process with different resource allocations while the case arrival rate remains unchanged. In this case study, we assume that there are 5 to 10 cases arriving randomly in every 20 to 30 min and we simulate the process to obtain 1000 cases each for four resource allocation plans:

• Plan (1): eight people with <sup>fi</sup>ve clerks and three managers;

• Plan (2): thirteen people with eight clerks and <sup>fi</sup>ve managers;

• Plan (3): sixteen people with ten clerks and six managers;

• Plan (4): nineteen people with twelve clerks and seven managers.

## Table 8

Testing results for constructing activity process with different noisy logs. NP is the percentage of noise. NoC is the number of traces in the log. NoT is the number of even names. NoE is the number of total events in the log. NoCRE is the number of causality relation edges discovered. IsCorrect indicates whether all the causality relation edges are correctly discovered in the logs.

<table><tr><td></td><td>Log1</td><td>Log2</td><td>Log3</td><td>Log4</td><td>Log5</td><td>Log6</td></tr><tr><td>NP</td><td>0%</td><td>3%</td><td>5%</td><td>10%</td><td>12%</td><td>15%</td></tr><tr><td>NoC</td><td>1050</td><td>1082</td><td>1105</td><td>1166</td><td>1192</td><td>1236</td></tr><tr><td>NoT</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td></tr><tr><td>NoE</td><td>17,900</td><td>18,448</td><td>18,854</td><td>19,944</td><td>20,368</td><td>21,089</td></tr><tr><td>NoCRE</td><td>26</td><td>26</td><td>26</td><td>26</td><td>26</td><td>26</td></tr><tr><td>IsCorrect</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

![](/api/attachments/XQDR7VCZ/fulltext/images/9d59ad95c2d981c4b37aa1771b21de323264eb4bb35ac0a2cb7a81ce990dc019.jpg)  
Fig. 7. Work<sup>fl</sup>ow simulation of event graph for operational decision support.

After obtaining the simulation logs, we compare the process performance via analyzing the simulation logs. The numbers of completed cases are tracked very four hours, shown in Fig. 8. Under Plan (1) with <sup>fi</sup>ve clerks and three managers, the process proceeds very slowly and the number of accumulated cases at every time point is relatively small. When there are three more clerks and two more managers in Plan (2), the process performance is much improved. After adding resources again in Plan (3), the performance is also improved but not that obviously. However, when there are nineteen people in Plan (4), the number of completed cases in every time slot is much alike Plan (3), without much performance improvement. After the comparison, it is easy to see that the suitable resource allocation plan for this case arrival rate is Plan (3) with sixteen people, ten clerks and six managers. Meanwhile, Plan (2) is also relatively acceptable.

From the last simulation, we can obtain the suitable plan of the resources for a speci<sup>fi</sup>c case arrival rate. Now we aim to <sup>fi</sup>nd out whether the proportion of different roles, clerk and manager in this example, is appropriate. Take Plan (1) mentioned above for example: we track the working state of two clerks and two managers, and compute the engagement rates every 2 h as shown in Fig. 9. If the staff is busy for 90 min in 2 h, the engagement rate is 75% in this time slot. We can see that the two clerks' work capacities are relatively saturated, keeping steadily around 80%. However, the two managers' engagement rates change dramatically and most of the time they are fairly low. Hence, we can draw the conclusion that the proportion of clerks to managers does not <sup>fi</sup>t and there needs to be a reduction in managers as their work has become unsaturated for most of the time under this case arrival rate.

![](/api/attachments/XQDR7VCZ/fulltext/images/787e2b6f8d943403bda68aae95ed7175aa42ce3d839ac7306be9da5e02c4ee66.jpg)  
Fig. 8. Comparison of completed cases for four resource allocation plans.

## 5.2. Teamwork performance estimation

In this section, we aim to understand teamwork performance under different case arrival rates. In this case, we can have a basic understanding of the appropriate task distribution for a speci<sup>fi</sup>c resource allocation plan and judge whether a case arrival rate is under control or not for such a team. So we simulated the credit card application under four different task distributions when there are <sup>fi</sup>ve clerks and three managers and obtain 1000 cases for each situation. In a time slot of 20 to 30 min, the four task distributions generated cases as follows:

• Distribution (1): generate one to two cases randomly;

• Distribution (2): generate two to four cases randomly;

• Distribution (3): generate four to six cases randomly;

• Distribution (4): generate six to eight cases randomly.

After obtaining the simulation logs, we tracked the average process durations every ten cases for each task distribution in Fig. 10. We can see that the process durations for Distribution (1) and Distribution (2) are almost the same, ranging from 70 to 90 min for each case. When cases arrive faster in Distribution (3), the process duration increases obviously and the average time of all the cases is 1286 min, which is relatively long. However, in Distribution (4), the process duration is prolonged and much longer than the former three distributions. Therefore, we understand the process performances under different case arrival rates and what case arrival rate is under control for our speci<sup>fi</sup>c resource allocation plan if we set the maximal acceptable process duration. When case arrival rate is beyond our control, we need to increase resources so as to make sure the process durations are acceptable.

## 5.3. Personal performance estimation

Besides predicting the teamwork performance through work<sup>fl</sup>ow simulation, it is also possible to evaluate personal performances. Here we used the engagement rate in Section 6.1 again as an evaluating indicator for personal performances. Tasking the case arrival rate and resource allocation Plan (1) in Section 6.1 for instance, we track the average engagement rate in every slot of two hours each for six staffs: three clerks and three managers. At the same time, we compute the average engagement rate of different roles, clerks and managers, for every time slot and for the whole respectively.

![](/api/attachments/XQDR7VCZ/fulltext/images/5c4c18597223e0d8894eafde6bfe7429ae132b49f592e46f3de99d51361cb95a.jpg)

![](/api/attachments/XQDR7VCZ/fulltext/images/fc1b08c9411e2f9b7978e70bad1356353370858bb9bfa58854e7392f2ae8e9d4.jpg)  
Fig. 9. Comparison of engagement rate between clerks and managers: (a) ClerkA vs ManagerA; (b) ClerkB vs ManagerB.

![](/api/attachments/XQDR7VCZ/fulltext/images/da7ab2767ae327fdef612a36f36c6649254e4d19b2be139b9c431a10fb250acc.jpg)  
Fig. 10. Comparison of process durations for four task distributions.  
(b)

Through the statistical data in Fig. 11, we can obtain information for the following questions:

• How busy is the staff? Through Fig. 11(a) we can see that most of the clerks' engagement rates range from 75% to 90%. Moreover, we can go deep into the data and calculate a staff member's average engagement rate on the whole. For instance, the maximal and minimal engagement rates of Clerk A are 90.83% and 72.5% respectively and the average engagement rate is 79.47% on the whole.

• How steady is the staff's work? The engagement rate <sup>fi</sup>gure gives us a qualitative understanding of whether a staff member's work state is steady or not. Here the stability means how a staff member's engagement rate <sup>fl</sup>uctuates. We can see that clerks' work is relatively steady but managers' work <sup>fl</sup>uctuates much more.

• When will the staff be fully engaged or not occupied? We can also observe that when the average engagement rate of all staff is at its highest or lowest. For example, in Fig. 11(b), the average engagement rate is relatively high at B and C, and low at A and D. Through such analysis and statistics, we can predict when the peak hours will be and allocate resource accordingly in order to reach an optimal process performance.

So far, we have simulated the event graph model of the credit card application for three representative problems of business process. Simulating the process under different resource allocation plans with a speci<sup>fi</sup>c case arrival rate helps to <sup>fi</sup>nd the suitable plan so that enterprises can economize on resources and reduce costs. Through work<sup>fl</sup>ow simulation, we judge whether a coming case arrival rate is under control with a speci<sup>fi</sup>c resource allocation plan in order to adjust resources <sup>fl</sup>exibly. Moreover, it is also able to analyze and evaluate personal performances through simulation. All these contribute to supporting common operational decisions in business processes and improving enterprise competitiveness.

(a)  
![](/api/attachments/XQDR7VCZ/fulltext/images/56317db78be5bf7c0fbe23c745c0bc398fa5772d95372172ecfa1b0b7b728dd2.jpg)

![](/api/attachments/XQDR7VCZ/fulltext/images/d0227c48bbc10c615769ef5ee488aa169ad3d2feae91d0c47258723ada1e1862.jpg)  
Fig. 11. Personal engagement rates for (a) clerks and (b) managers. The line named “Average” with dotted symbols denotes the average engagement rates of the three clerks (managers) in every time unit of 2 h. The horizontal line without symbols denotes the tota average engagement rate of the three clerks (managers) during the whole process

Table 9  
Conceptual comparison of event graph and Petri net.

<table><tr><td></td><td>Event graph</td><td>Petri net</td></tr><tr><td>Simplicity</td><td>The simplest and most natural way to represent discrete event models</td><td>Possessing complex icons for different elements</td></tr><tr><td>Expressibility</td><td>Integrating various aspects of processes</td><td>Focusing on control-flow aspect of processes</td></tr><tr><td>Complexity</td><td>Only the causality relations need to be considered when building models</td><td>Quite an effort to discover logical relations</td></tr><tr><td>Flexibility</td><td>Flexible to arrange the control flow with the help of edge conditions</td><td>Inflexible to arrange the control flow with fixed logical relationships</td></tr><tr><td>Dynamism</td><td>Easy to handle changes</td><td>Difficult to handle changes</td></tr></table>

## 6. Discussion

In this paper, we present an approach of work<sup>fl</sup>ow simulation for operational decision support with event graphs, which can be constructed from log <sup>fi</sup>les through process mining. Event graph concisely organize the elements of a discrete event simulation. The approach is feasible, as demonstrated by the case study. Meanwhile, we would like to discuss the comparison of event graphs with Petri nets and address three further considerations about event graphs.

## 6.1. Conceptual comparison with Petri nets

An event graph is a combination of graph-based formalism and rulebased formalism [21], with its visual appeal of being intuitive and explicit for graph-based formalism and a good presentation for rule-based formalism. Here we summarize the merits of event graphs compared to Petri nets, a prevailing formalism in process mining, as in Table 9:

Taking an example for simplicity, different icons for transitions in Fig. 3 denote the different logical relationships. You need to have some professional background to understand such a Petri net. It is pointed out that traditional work<sup>fl</sup>ow systems focus on providing support for the control-<sup>fl</sup>ow perspective of a business process [31], while event graphs pull together the various aspects of enterprise activities, with their different elements, in a concise manner so that it is able to track and analyze the process performance. For complexity, event graphs possess edge conditions to deal with the logical relationships between activities, so that only the causality relations need to be considered in constructing activity processes. But in Petri net, it is quite an effort to discover logical relations such as parallelism and choice. Besides, it is <sup>fl</sup>exible to arrange the control <sup>fl</sup>ow with the help of edge conditions in event graphs, which is explained further in the example of Fig. 12. Dynamic changes can be implemented by only modifying edge conditions or event priorities instead of rescheduling. However, this is dif<sup>fi</sup>cult for Petri nets to handle as it has to reschedule the activities and this often affects the whole process. In this experiment, we can recon<sup>fi</sup>gure the resources by simply modifying the state variables of clerk and manager.

In order to better illustrate the merits of event graphs, we give another example. Fig. 12 is an event graph model of a service system. Firstly, it is more <sup>fl</sup>exible to express logical relations between activities because event graphs possess edge conditions for <sup>fl</sup>ow control. In this example, “CheckType” has both a XOR split and an AND split to “StartService1” and “StartService2”. Also “EndService1” and “EndService2” comprise both a XOR join and an AND join to “Leave”. Such complex logical relations are very dif<sup>fi</sup>cult to express in Petri nets. Secondly, event graphs are able to pull together the various aspects of processes with their different elements in a concise manner. This example contains rich information such as the number of different idle servers and customers waiting in line, and durations of important events, which can be used to track and analyze the process performance.

## 6.2. Further considerations about event graphs

Through conceptual comparison with Petri nets, we see the merits of modeling and simulating processes with event graphs. Here we discuss three further considerations about event graphs, i.e. time gap, loop and simulation power.

In most of the process simulations, only the durations of tasks are under consideration and the time gaps between different tasks are ignored. But in fact these time gaps really exist and they also have an important impact on the whole duration of the process. So it is more realistic for us to take these time gaps into account when simulating the process. As we can see that in event graph models, we have explicit boundary division for tasks and it is very easy to add the time gaps into the model, putting time delays on the edges from the ending vertex of one task to the starting vertex of the subsequent.

Loop is an open problem when mining and modeling processes. van der Aalst et al. [40] mentioned two types of loops, basic loops and arbitrary loops. It points out that all the four work<sup>fl</sup>ow tools discussed in that paper impose restrictions on the structure of these loops in order to guarantee the correctness of the discovered model. Moreover, none of these tools support arbitrary loops. As mentioned before, we need not consider different logical relations but the causality relation between events because of edges conditions in event graphs. In this case, if we can detect the causality relation and edges conditions correctly, the loops will be constructed naturally. It is also possible to construct arbitrary loops, where the edge conditions are more complex for counteraction. Also, vertexes in event graphs can possess edges to themselves so that short loops are supported in this formalism. We aim to explore the capability of our approach to building business processes with loops in future works.

![](/api/attachments/XQDR7VCZ/fulltext/images/70403b9f422ea813cc09d08cfd333ea1d1ac93ce055891a00728c3d3c3451cb0.jpg)  
Fig, 12, An event graph model of a service system, The “Run" vertex simply initializes the model. S1 and S2 are the number of idle servers for two different kinds of services, O is the number of customers waiting for service. A is a calling population of customers. There are three kinds of customer requirements denoted by Type. Customers with Type equalling 1 or 2 only require service1 or service2 respectively, while customers with Type equalling 3 require both of these two services. E is a state variable for controlling the flow.

For a process modeling formalism, it is important to possess tools to visualize the models explicitly and simulate the processes powerfully. Simkit, an open source package, is based on event graph view and can be used to create discrete event simulation models [5]. But it is not graphic so that it lacks good visualization and is dif<sup>fi</sup>cult to use. We mentioned a software environment called Sigma for discrete event simulation before, which is the only graph tool of event graphs as far as we know. There are tutorials that simulate event graphs with Sigma [36]. However, there are some limitations in the simulation power of Sigma. For example, case arrival rate cannot be con<sup>fi</sup>gured so that we are not able to obtain the simulation data under some speci<sup>fi</sup>c scenarios. The initial states of event graph models are all empty so it is impossible to carry out non-empty state simulation. After the simulation, it lacks tools to analyze simulation logs and present statistical results. So it is necessary to develop a new tool for event graph simulation if we need to improve the simulation functions.

Based on our approaches presented, we expect to polish our method of modeling business processes with event graphs, integrating the applications of time gap and loop. Further improvement for simulating processes with event graphs, such as loading current states and visualizing simulation results, will also be further pursued. We have also come to realize that the true power of our proposed method lies in the situations where an underlying model is hardly to be formulated using conventional business process modeling formalisms. Scenarios like these include, for example, e-commerce, online shopping, logistic warehousing, etc. We are actively looking into some of these scenarios to further test and validate our proposal.

## 7. Conclusion

BPS plays a signi<sup>fi</sup>cant role in process management and improvement. In this paper, we have proposed an approach of work<sup>fl</sup>ow simulation for operational decision support with event graphs. Our model is constructed from log <sup>fi</sup>les through process mining and evaluations of deriving event graphs are given in terms of precision, generalization and robustness. Based on the generated model, we proceeded with work<sup>fl</sup>ow simulation under different scenarios for three typical problems during BPM with a case study of a credit card application. Based on the simulation logs, we are able to <sup>fi</sup>nd the suitable resource allocation plan for different case arrival rates, judge whether the coming case arrival rate is under control with a speci<sup>fi</sup>c resource allocation plan and evaluate personal performance. The analysis results of simulations enable enterprises to make operational decisions, which are critical for business process management and improvement.

## Acknowledgment

The work described in this paper was supported by a research grant from the National University of Singapore (Grant No: R265- 000-362-133).

## References

[1] R. Agrawal, D. Gunopulos, F. Leymann, Mining process models from work<sup>fl</sup>ow logs, Proceedings of the 6th International Conference on Extending Database Technology: Advances in Database Technology, 1998, pp. 469–483, Valencia Spain.

[2] M. Aguilar, T. Rautert, A.J.G. Pater, Business process simulation: a fundamental step supporting process centered management, 1999 Winter Simulation Conference Proceedings, 1999, pp. 1383–1392, Phoenix, AZ, USA.

[3] K.D. Barber, F.W. Dewhurst, R.L.D.H. Burns, J.B.B. Rogers, Business-process modelling and simulation for manufacturing management: a practical way forward, Business Process Management Journal 9 (4) (2003) 527–542.

[4] A.H. Buss, Modeling with event graphs, Proceedings of the 28th Conference on Winter Simulation, 1996, pp. 153–160, Coronado, California, USA.

[5] A.H. Buss, Component based simulation modeling with Simkit, 2002 Winter Simulation Conference, 2002, pp. 243–249, San Diego, CA.

[6] J.E. Cook, A.L. Wolf, Discovering models of software processes from event-based data, Journal ACM Transactions on Software Engineering and Methodology 7 (3) (1998) 215–249.

[7] S. De Cesare, A. Serrano, Collaborative modeling using UML and business process simulation, Proceedings of the 39th Annual Hawaii International Conference on System Sciences, 2006, p. 10b, Kauai, HI

[8] A. Greasley, Using business-process simulation within a business-process reengineering approach, Business Process Management Journal 9 (4) (2003) 408–420.

[9] A. Greasley, A redesign of a road traf<sup>fi</sup>c accident reporting system using business process simulation, Business Process Management Journal 10 (6) (2004) 635–644.

[10] V. Hlupic, G.-J.D. Vreede, Business process modelling using discrete-event simulation: current opportunities and future challenges, International Journal of Simula tion and Process Modelling 1 (1/2) (2005) 72–81.

[11] G. Holmes, A. Donkin, I.H. Witten, WEKA: a machine learning workbench, Proceedings of the 1994 Second Australian and New Zealand Conference on Intelli gent Information Systems, 1994, pp. 357–361, Brisbane, Australia.

[12] R.G. Ingalls, D.J. Morrice, A.B. Whinston, The implementation of temporal intervals in qualitative simulation graphs, Journal of ACM Transactions on Modeling and Computer Simulation 10 (3) (2000) 215–240.

[13] S. Jain, E. Ervin, Evaluation of supply chain business process improvements using simulation, Journal of Simulation and Process Modelling 1 (3/4) (2005) 138–149.

[14] M. Jansen-Vullers, M. Netjes, Business Process Simulation—A Tool Survey, Workshop and Tutorial on Practical Use of Coloured Petri Nets and the CPN Tools, 2006, p. 20b, Aarhus, Denmark.

[15] K. Jensen, Coloured Petri Nets: Basic Concepts, Analysis Methods and Practical Use, Springer-Verlag, Berlin, 1997.

[16] D. Jörg, E. Thomas, Modeling, simulation and analysis of business processes, Business Process Management, 2000, pp. 247–288.

[17] B. Joseph, A business process modeling and simulation method using DEMO, Enterprise Information Systems, 2008, pp. 254–265.

[18] W.J. Kettinger, J.T.C. Teng, S. Guha, Business process change: a study of methodologies, techniques, and tools, MIS Quarterly 21 (1) (1997) 55–80.

[19] J.d. Lara, Distributed event graphs: formalizing component-based modelling and simulation, Journal of Electronic Notes in Theoretical Computer Science 127 (4) (2005) 145–162.

[20] R. Liu, A. Kumar, W. van der Aalst, A formal modeling approach for supply chain event management, Decision Support Systems 43 (3) (2007) 761–778.

[21] R. Lu, S. Sadiq, A survey of comparative business process modeling approaches, the 10th International Conference on Business Information Systems, 2007, pp. 82–94, Poznan, Poland.

[22] L. Maruster, A.J.M.M.T. Weijters, W.M.P. van der Aalst, A.v.d. Bosch, Process mining: discovering direct successors in process logs, Lecture Notes in Computer Science: Discovery Science, Springer Berlin, Heidelberg, 2009, pp. 364–373.

[23] N. Melão, M. Pidd, Use of business process simulation: a survey of practitioners, Journal of the Operational Research Society 54 (1) (2003) 2–10.

[24] K. Ning, D. Niu, Q. Li, H. Shen, Y.-l. Chen, IDEF3-based business process simulation modeling, Computer Integrated Manufacture System 9 (5) (2003) 351–356.

[26] R.I. Paul, G.M. Giaglis, V. Hlupic, Simulation of business processes, American Behavioral Scientist 42 (10) (1999) 1551–1576

[27] H.A. Reijers, W.M.P. van der Aalst, Short-term simulation: bridging the gap between operational control and strategic decision making, Proceedings of the IASTED International Conference on Modelling and Simualtion, 1999, pp. 417–421, Anaheim, USA.

[28] A. Rozinat, Conformance testing: measuring the <sup>fi</sup>t and appropriateness of event logs and process models, Third International Conference on Business Process Management, 2005, pp. 163–176, Nancy, France.

[29] A. Rozinat, A.K.A.d. Medeiros, C.W. Günther, A.J.M.M. Weijters, W.M.P. van der Aalst, Towards an evaluation framework for process mining algorithms, BPM Center Report BPM-07-06, 2007.

[30] A. Rozinat, M.T. Wynn, W.M.P. van der Aalst, A.H.M.t. Hofstede, C.J. Fidge, Work-<sup>fl</sup>ow simulation for operational decision support, Data & Knowledge Engineering 68 (9) (2009) 834–850.

[31] N.C. Russell, W.M.P. van der Aalst, A.H.M.t. Hofstede, Designing a work<sup>fl</sup>ow system using coloured Petri nets, Lecture Notes in Computer Science, Transactions on Petri Nets and Other Models of Concurrency III 5800, 2009, pp. 1–24.

[32] S.A. Salaimeh, K. Batiha, Business process simulation with algebra event regular expression, Information Technology Journal 5 (3) (2006) 583–589.

[33] R.G. Sargent, Event graph modelling for simulation with an application to <sup>fl</sup>exible manufacturing systems, Journal of Management Science 34 (10) (1988) 1231–1251.

[34] E.L. Savage, L.W. Schruben, E. Yucesan, On the generality of event-graph models, INFORMS Journal on Computing 17 (1) (2005) 3–9.

[35] L.W. Schruben, Simulation modeling with event graphs, Journal of Communications of ACM 26 (11) (1983) 957–963.

[36] L.W. Schruben, Graphical Simulation Modeling and Analysis: using SIGMA for Windows, Boyd & Fraser, Danvers, MA, 1995.

[37] L.W. Schruben, E. Yucesan, Simulation graphs, Proceedings of the 20th Conference on Winter Simulation, 1988, pp. 504–508, San Diego, California, USA.

[38] D. Simon, K. Ben, H. Martin, R. Stewart, Applications of business process simulation and lean techniques in British Telecommunications PLC, 2000 Winter Simulation Proceedings, 2000, pp. 2015–2021, Orlando, FL, USA.

[39] Y. Tan, Simulation analysis on the performance of the sales and distribution process with enhanced information systems, Proceedings 2009 IEEE 16th International Conference on Industrial Engineering and Engineering Management, 2009, pp. 1852–1855, Beijing, China.

[40] W.M.P. van der Aalst, B.F.v. Dongen, J. Herbst, L. Maruster, G. Schimm, A.J.M.M. Weijters, Work<sup>fl</sup>ow mining: a survey of issues and approaches, Journal of Data & Knowledge Engineering 47 (2) (2003) 237–267.

[41] W.M.P. van der Aalst, A.H.M. ter Hofstede, M. Weske, Business process management: a survey, Lecture Notes in Computer Science 2678 (2003) 1–12.

[42] W.M.P. van der Aalst, A.J.M.M. Weijters, L. Maruster, Work<sup>fl</sup>ow mining: discovering process models from event logs, Journal of IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[43] W.M.P. van der Aalst, H.A. Reijers, A.J.M.M. Weijters, B.F.v.v. Dongen, A.K.A.d. Medeiros, M. Song, H.M.W. Verbeek, Business process mining: an industrial application, Information Systems 32 (5) (2007) 713–732.

[44] W.M.P. van der Aalst, J. Nakatumba, A. Rozinat, N.C. Russell, Business process simulation: how to get it right, BPM Center Report BPM-08-07, 2008.

[45] H. Wang, S. Sun, J. Xu, F. Shi, N. Zou, Petri net based business process simulation and analysis technology, Proceedings of the International Conference on Information Management, 2008, pp. 148–152, Taipei.

[46] A.J.M.M. Weijters, W.M.P. van der Aalst, Work<sup>fl</sup>ow mining: discovering work<sup>fl</sup>ow models from event-based data, Proceedings of the ECAI Workshop on Knowledge Discovery and Spatial Data, 2002, pp. 78–84, Lyon, France

[47] L. Wen, J. Wang, W.M.P. van der Aalst, B. Huang, J. Sun, A novel approach for process mining based on event types, Journal of Intelligent Information Systems 32 (2) (2009) 163–190.

[48] M.T. Wynn, M. Dumas, C.J. Fidge, A.H.M. ter Hofstede, W.M.P. van der Aalst, Business process simulation for operational decision support, The 3rd International Workshop on Business Process Intelligence (BPI 07) in Conjunction with Business Process Management Conference, 2007 Brisbane, Australia.

[49] Y. Xie, Process modeling and simulation based on extended UML activity and GPSS, IEEE International Conference on Automation and Logistics (ICAL 2008), 2008, pp. 2931–2935, Qingdao, China.

[50] X. Huang, L. Wang, W. Zhao, S. Zhang, C. Yuan, A work<sup>fl</sup>ow process mining algorithm based on Synchro-net, Journal of Computer Science and Technology 21 (1) (2006) 66–72.

[51] H. Zhang, Y. Liu, C. Li, R. Jiao, Deriving event graphs through process mining for runtime change management, The 1st International Conference on Modelling and Management of Engineering Processes, 2010, pp. 12p, Cambridge, UK.

[52] H. Zhang, Y. Liu, C. Li, R. Jiao, A Novel Approach of Process Mining with Event Graph, The 14th International Conference on Knowledge-Based and Intelligent Information & Engineering Systems, 2010, pp. 10p, Cardiff, Wales, UK.

Ying Liu is presently an Assistant Professor with the Department of Mechanical Engineering at the National University of Singapore. His current research interests focus on design informatics, data mining and text mining, intelligent information processing and management, machine learning, and their joint research and applications in engineering design, manufacturing and medical and healthcare industry for knowledge discovery and management purpose. He is the lead editor for the book “Advances of Computational Intelligence in Industrial Systems” Springer 2008 and he has served as lead Guest Editor for several special issues with the Journal of Intelligent Manufacturing, Information Systems Frontiers and Advanced Engineering Informatics. He is a member with ACM, ASME and the Design Society.

Hui Zhang is a Master degree student with the School of Software at Tsinghua University. Her research focus is centered on machine learning, data mining and process mining.

Chunping Li is an Associate Professor with the School of Software at Tsinghua University. He has been conducting extensive research in machine learning, data\text mining and formal knowledge representation and knowledge reasoning. He has developed an approach on deriving formal speci<sup>fi</sup>cation for the semantics of processes in logical paradigm, and its inference mechanism especially applied in the process control and management. Currently, Dr. Li is supervising several research projects (Principal Investigator) funded by NSF China and Volkswagen Research Germany, where he and his research group are investigating the techniques of software system design for prediction detection, system model representation, program complexity measurement, and performance evaluation, etc.

Roger Jianxin Jiao is an Associate Professor with the G.W. Woodruff School of Mechanical Engineering at Georgia Institute of Technology. Dr. Jiao has been conducting extensive research in engineering design and product development, engineering management, operation research, enterprise information system and management. Dr. Jiao is one of the leading academics in proposing the basic concept of mass customization and product family design and advancing the research frontier. Currently, Dr. Jiao is supervising several research projects (Principal Investigator) funded by European Commission, A\*STAR Singapore and Nanyang Technological University (his former af<sup>fi</sup>liation), through which he and his research group are investigating the computerized technology in mass customization recon<sup>fi</sup>guration system and the impact of ambient intelligence in human factor design.
