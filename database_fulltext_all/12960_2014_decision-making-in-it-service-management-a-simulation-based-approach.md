---
otero_id: 12960
otero_key: "2DKY3E6G"
title: "Decision-making in IT service management: a simulation based approach"
authors: "Elena Orta; Mercedes Ruiz; Nuria Hurtado; David Gawn"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision-making in IT service management: a simulation based approach

Elena Orta ⁎, Mercedes Ruiz, Nuria Hurtado, David Gawn

Department of Computer Science and Engineering, University of Cadiz, C/Chile, 1, 11003 Cadiz, Spain

## a r t i c l e i n f o

Article history: Received 2 August 2013 Received in revised form 11 April 2014 Accepted 3 June 2014 Available online xxxx

Keywords: Decision support systems Simulation modeling IT services management ITIL Incident management Capacity management

## a b s t r a c t

Simulation modeling is widely used to support decision-making in different business areas and management tasks. Given the growing importance for real-world organizations to improve Information Technology Service Management (ITSM), this paper focuses on the application of these techniques to support decision-making in this <sup>fi</sup>eld. A review of published research articles that describe an application case has been conducted and it shows that different simulation approaches are extensively used to solve particular problems in the context of several processes. However, in these works there is no evidence of a systematic use of both ITSM frameworks and simulation model development methodologies. Given their importance to build valid simulation models, this paper proposes a novel decision-making framework whose main component is a speci<sup>fi</sup>c methodology to systematically build simulation models that help solve real-world organization problems applying ITIL recommendations. To illustrate the usefulness of this framework, two application cases in the context of the ITIL capacity management and incident management processes are summarized. The model simulations provide information about the process results, performance and behavior with different process configurations. Moreover, optimization experiments allow managers to determine the optimal process con<sup>fi</sup>guration that meets the established objectives.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Information Technology Service Management (ITSM) refers to the implementation and management of quality IT services that meet the needs of a business. ITSM is performed by IT service providers through an appropriate mix of people, processes and IT [41]. This discipline is focused on providing a framework to structure IT-related activities and the interactions of IT technical personnel with business customers and users. ITSM is generally concerned with operational issues of information technology management and not with technology development.

The growing importance for organizations to improve the management of their services has led to the emergence of international standards and frameworks such as ISO/IEC 20000 [43,44], ITIL [42] and CMMI-SVC [14], that provide process models and best practices for ITSM. ITIL (Information Technology Infrastructure Library), developed by the Of<sup>fi</sup>ce of Government Commerce (OGC), is nowadays one of the reference models most used in organizations. The empirical works realized by Marrone and Kolbe [61,62] show the operational and strategic bene<sup>fi</sup>ts that organizations gain with ITIL implementation.

Although ITSM frameworks provide important bene<sup>fi</sup>ts, their implementation in real organizations is a complex process and for this it is necessary to make very important and dif<sup>fi</sup>cult decisions [71–75]. Speci<sup>fi</sup>c examples of such decisions are as follows: a) What changes to make in process and service management strategy con<sup>fi</sup>gurations to improve process results, behavior and performance; and b) Determining the process con<sup>fi</sup>gurations that optimize the process results and meet the organization objectives, among others. Decision Support Systems (DSS) help managers make better decisions in this <sup>fi</sup>eld [12,17,23,48, 51,90,97].

Considering the dominant architectural component that provides the functionality to support decision-making, Power [81] differentiates communication-driven DSS, data-driven DSS, document-driven DSS, knowledge-driven DSS, and model-driven DSS. By de<sup>fi</sup>nition, one or more quantitative models are the dominant components of model-driven DSS [82]. This type of DSS emphasizes access to and manipulation of quantitative models, such us, algebraic, decision analytical, statistical, <sup>fi</sup>nancial, optimization or simulation models to provide decision support. They are designed so that users can manipulate model parameters to analyze the output sensitivity or to conduct a more ad hoc “what if?” analysis. Moreover, the model is accessible to a non-technical specialist, such as a manager, through an easy user interface. Power and Sharda present in [81] an overview of model-driven research and show the applicability and usefulness of simulation-driven DSS to support business and engineering decision-making. Simulation models are the main component of simulation-driven DSS. The authors of [55,56,65,83,92] emphasize the importance of using simulation model development methodologies to build valid and credible simulation models.

The goal of this paper is to explore the application of simulation modeling to support decision-making in the scope of ITSM. Its main contributions are as follows:

• A study of published research articles that apply simulation modeling in an ITSM context. The simulation approaches used, the processes modeled and the issues addressed in the selected articles have been identi<sup>fi</sup>ed.

• A decision-making framework to improve ITSM focused on simulation modeling. Its main components are a speci<sup>fi</sup>c methodology to develop simulation models in this context and the simulation models built.

• Two application cases of the proposed framework in the <sup>fi</sup>eld of the ITIL capacity management and incident management processes.

The rest of this paper is structured as follows. The next section presents the results of the study we conducted of published research articles that apply simulation modeling in an ITSM context. Section 3 describes the decision-making framework proposed for ITSM improvement. The two application cases of this framework are explained in Sections 4 and 5. Finally, Section 6 contains our conclusions and identi<sup>fi</sup>es further work to carry out in this area.

## 2. Simulation and IT service management: related work

The common goal of simulation models is to provide mechanisms for experimentation, system behavior prediction, the resolution of questions such as “What would occur if …?”, and learning more about the system represented. These models facilitate the experimentation of different decisions and observing the results in systems where the cost, time or risk of experimentation with the real system could be high [49]. They are usually built to understand how systems behave over time and to compare their performance under different conditions.

A very useful simulation technique is sensitivity analysis. This technique allows one to study the effects on model outcomes of varying the values of model input parameters over a range of values. Thus, it helps managers determine the likely range of results when there are uncertainties in the key input parameters, and identify which input parameters produce greater effects on model outcomes [49].

There are a variety of simulation approaches, such as state-based process models, discrete event simulation, system dynamics, agentbased simulation, Petri-net models, queuing models, Monte Carlo simulation, probabilistic simulation, and traditional mathematical simulation [81].

This section explores the use of simulation modeling to support decision-making in ITSM, looking speci<sup>fi</sup>cally into the processes and issues modeled. Moreover, the use of both ITSM frameworks or standards, and methodologies to build simulation models in this <sup>fi</sup>eld is also analyzed. We think that this study is appropriate for the following reasons:

• Simulation modeling is widely used to support decision-making in different business areas and management tasks. An extensive variety of practical questions can be addressed with simulation, such as strategic management, planning, control and operational management, process improvement and technology adoption [16,24,26,36,39,50, 82,95,108].

• The growing global diffusion of ITSM frameworks and standards due to the fact that organizations that implement them obtain important bene<sup>fi</sup>ts [15,61,62].

• The use of an adequate simulation model development methodology is one of the most in<sup>fl</sup>uential aspects in the building process to obtain valid and credible models. This is fundamental since a well-designed model signi<sup>fi</sup>cantly improves the probability of a successful outcome of a simulation study [55,56,65,83,92].

The study conducted focuses on a review of published research papers that describe an application case of simulation modeling in an

ITSM context. The intent is not to provide an exhaustive study but rather to offer an overview of the use of these techniques in this <sup>fi</sup>eld. We address the following three research questions:

• Q1: Is simulation modeling used to support decision-making in an ITSM context?

• Q2: Are ITSM frameworks used in the analyzed research papers?

• Q3: Are simulation model development methodologies used to build the models proposed?

The literature review undertaken follows three stages: 1) identifying the main issues addressed in the selected articles and associating these works with the most related ITIL process, 2) classifying the articles according to the issues addressed, and 3) studying the articles to see if they propose the use of ITSM frameworks and standards or simulation model development methodologies.

## 2.1. Identifying the issues addressed and associating the articles with ITIL processes

This section presents an overview of published research articles that describe an application case of simulation modeling in an ITSM context. For each article found a study of the issues addressed has been performed and it has been associated with the most relevant ITIL process. We have used ITIL since it is one of the ITSM frameworks most frequently adopted in organizations and provides important bene<sup>fi</sup>ts [15,61,62]. In addition, ITIL recommends using simulation to support decisionmaking in the continual improvement of processes [71].

ITIL structures service management processes in <sup>fi</sup>ve modules which correspond to the service lifecycle phases: Service Strategy [74], Service Design [72], Service Transition [75], Service Operation [73] and Continual Service Improvement [71]. In the following paragraphs, the articles found are referenced by process inside each of the service lifecycle phases. For each the issues addressed and the simulation approaches used are introduced. The simulation approach names have been abbreviated as follows: discrete event simulation (DES), system dynamics (SD), agent-based simulation (ABS), Petri-net models (PNM), queuing models (QM), Monte Carlo simulation (MCS), probabilistic simulation (PS), and traditional mathematical simulation (MS). In some situations simulation is used to validate conceptual or formal models. In this study we have introduced some works of this type and the simulation approach is named “other models simulation (OMS)”.

## a) Service strategy module

The purpose of service strategy is to design, develop and implement service management as an organizational capability and as a strategic asset [74]. The articles found by process for this module are as follows:

## a.1) Strategy management for IT services process

The goal of this process is to ensure that the service strategy is de<sup>fi</sup>ned and maintained, and achieves its purpose. This process is responsible for de<sup>fi</sup>ning the strategic goals and the appropriate strategies for compliance [74]. Table 1 summarizes the publications assigned to this process.

## a.2) Financial management for IT services process

The purpose of this process is to secure the appropriate level of <sup>fi</sup>nancing to design, develop and deliver services that meet the strategy of the organization [74]. The articles associated with this process are shown in Table 2.

## a.3) Demand management process

The purpose of this process is to understand, anticipate and in-<sup>fl</sup>uence customer demand for services. This process works with capacity management to ensure that the service provider has enough capacity to meet this demand [74].

The system dynamics model that Orta et al. [77] propose in the context of capacity management allows one to study if the

## Table 1

Simulation modeling in strategy management for IT service process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[47]</td><td>SD</td><td>Studying the interrelationships between the main elements of service management systems (business objectives, resources and processes).</td></tr><tr><td>[76]</td><td>SD</td><td>Analyzing strategic business rules and finding a good configuration for strategic business objectives and IT parameters.</td></tr><tr><td>[89]</td><td>SD</td><td>Exploring the role of SD research in making important progress with the following issue: “Why are some firms more profitable than others” (the study can be applied in the field of strategy for IT services).</td></tr><tr><td>[27]</td><td>SD</td><td>Evaluating different business objective strategies and determining the most adequate.</td></tr><tr><td>[91]</td><td>OMS</td><td>Examining performance measures, defining an IT investment strategy and selecting the optimal scenario for business and IT governance alignment.</td></tr></table>

## Table 2

Simulation modeling in <sup>fi</sup>nancial management for IT service process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[31]</td><td>SD</td><td>Identifying situations in which the cost of improving services exceeds the benefits. For this, the models allow to study service behavior, resource allocation, customer perception and reaction of competitors.</td></tr><tr><td>[99]</td><td>QM</td><td>Deciding the resource allocation that maximizes the benefits of service provider and minimizes the costs of service failures.</td></tr><tr><td>[1]</td><td>MS, QM</td><td>Analyzing the service cost based on penalties due to SLA violation and rewards received when the level targets are exceeded.</td></tr><tr><td>[57]</td><td>DES</td><td>Describing a framework for developing discrete-event simulation models which help estimate serviceability, costs, revenue, profit and quality of services.</td></tr><tr><td>[35]</td><td>MS</td><td>Analyzing the service cost considering alternative development teams and service providers, and determining the optimal cost service provider.</td></tr><tr><td>[80]</td><td>DES</td><td>Predicting the cost of services, analyzing the effects of business strategies, and defining both the IT infrastructure and the price of services.</td></tr><tr><td>[88]</td><td>PS</td><td>Analyzing the expected change-related costs.</td></tr><tr><td>[32]</td><td>MS</td><td>Discussing an analytical economic model of resource provision in a federated cloud. It also shows how to implement such federation among cloud providers for better performance.</td></tr><tr><td>[63]</td><td>MS</td><td>Supporting cloud service selection across multiple sources considering cost and risk (they are factors relevant to the decision scope).</td></tr><tr><td>[66]</td><td>MS</td><td>Proposing an analytical model of hybrid cloud costs in which the costs of computing and data communication are taken into account.</td></tr></table>

service capacity contracted by customers is enough to satisfy the service demand and meet the SLA.

## b) Service design module

Service design can be de<sup>fi</sup>ned as the design of appropriate and innovation IT services to meet current and future agreed business requirements [72]. The articles found by process in this area are referenced below:

## b.1) Service catalog management process

The objective of this process is to provide a consistent source of information for all agreed services and ensure that it is available [72].

In [102], the authors introduce an IT service catalog model to manage services. They also propose a method to solve the problem of service composition based on functions and levels of customer's requirements. The feasibility of the proposal is veri<sup>fi</sup>ed and evaluated by simulation experiments (OMS simulation approach).

## b.2) Service level management process

This process' aim is to negotiate for, agree on and document appropriate IT services. It also monitors and produces reports on delivery against the agreed service levels [72]. Table 3 presents the articles assigned to this process.

The models proposed in some of the articles associated with other ITIL processes also help analyze issues related to service level management, such as: a) how to allocate resources to meet SLAs [3,99]; b) impacts of threats on SLAs [45]; c) implications of an availability model in SLA management [28]; d) cost of services based on SLA compliance [1]; and e) effects of provider selection on SLA compliance [34].

## b.3) IT service continuity management process

The purpose of this process is to support the appropriate recovery capability within IT services to achieve the agreed business requirements [72]. The articles assigned to this process are summarized in Table 4.

## b.4) Availability management process

The aim of this process is to manage all IT service availabilityrelated issues, ensuring that availability targets are achieved in a cost-effective and timely manner [72]. Table 5 presents the papers associated with this process.

b.5) Capacity management process

## Table 3

Simulation modeling in service level management process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[96]</td><td>ABS</td><td>Examining a design-time assessment of an IT service architecture with respect to aspects of service level management.</td></tr><tr><td>[40]</td><td>QM, DES</td><td>Describing distributed transaction processing (DTP) systems which characterize the service industries, and comparing the predictive accuracy of different types of queuing and discrete event models.</td></tr><tr><td>[104]</td><td>MS</td><td>Proposing an optimization model of response in SaaS in order to optimize business profit.</td></tr><tr><td>[30]</td><td>MS, QM</td><td>Presenting an SLA based business-driven adaptive quality of service maintenance mechanism for multi-tier service in a virtualized IT environment.</td></tr></table>

## Table 4

Simulation modeling in IT service continuity management process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[100]</td><td>DES</td><td>Analyzing error impacts on IT services.</td></tr><tr><td>[101]</td><td>OMS</td><td>Presenting a model-driven framework that integrates business process modeling and IT management. It enables automatic consolidation of information from multiple data sources and various stakeholders.</td></tr></table>

## Table 5

Simulation modeling in availability management process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[85]</td><td>PNM</td><td>Improving service availability adding redundancy.</td></tr><tr><td>[28]</td><td>MS</td><td>Studying availability investment and discussing different availability strategies.</td></tr><tr><td>[60]</td><td>OMS</td><td>Assessing service risks focusing on two service availability metrics: a) the costs when the service is not available; and b) the probability that the service is available (calculated using attack graphs). Additionally, a model of an intrusion detection system is proposed.</td></tr></table>

## Table 6

Simulation modeling in capacity management process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[37]</td><td>SD</td><td>Studying the capacity requirements for BBC IT Storage Area Network to understand SAN capacity utilization trends and strategic acquisition planning decisions.</td></tr><tr><td>[1]</td><td>MS, QM</td><td>Presenting a dynamic capacity management framework based on an optimization model that links a cost model based on SLA contracts with an analytical queuing-based performance model.</td></tr><tr><td>[57]</td><td>DES</td><td>Proposing a framework that helps to build models for evaluating effectiveness of different resource management policies. The models also simulate interactions of demand planning activities for service engagements, human resource supply planning, resource attrition and termination, and execution of service orders to estimate business performance.</td></tr><tr><td>[76]</td><td>SD</td><td>Analyzing the consequences of under or over estimation of an outsourced service capacity on the application performance.</td></tr><tr><td>[70]</td><td>MS</td><td>Proposing algorithms of dynamic QoS optimization and adaptation of inter-dependent task sets in cooperative embedded systems.</td></tr><tr><td>[40]</td><td>QM, DES</td><td>Describing distributed transaction processing systems which characterize the service industries, and comparing the predictive accuracy of different types of queuing and discrete event models.</td></tr><tr><td>[2]</td><td>QM</td><td>Introducing a web service capacity planning methodology based on a workload model and a service behavior queuing model.</td></tr><tr><td>[79]</td><td>QM</td><td>Predicting the performance of composite web services with limited resources.</td></tr><tr><td>[99]</td><td>QM</td><td>Studying methods to provision an e-commerce service provider&#x27;s application-tier servers among a set of customer companies to maximize the provider&#x27;s profit.</td></tr><tr><td>[84]</td><td>MS</td><td>Presenting an energy-aware online provisioning approach based on simulations for high-performance computing applications on consolidated and virtualized computing platforms.</td></tr><tr><td>[54]</td><td>MS</td><td>Describing an enhanced Network Control Plane architecture operating over a virtual optical infrastructure to provide IT-aware and energy-efficient connectivity services between data centers.</td></tr><tr><td>[38]</td><td>MS</td><td>Introducing a new approach to perform dynamic resources management in virtualized data centers that proposes considering the non-stationary noise of the VMs&#x27; demand behavior.</td></tr><tr><td>[33]</td><td>MS</td><td>Introducing an algorithm for provisioning complex IT applications over optical networks and a discrete event simulator for cloud environments with under light-trail network.</td></tr><tr><td>[52]</td><td>MS</td><td>Examining two approaches and three types of metrics for quantifying the performance isolation on cloud-based systems.</td></tr></table>

The goal of this process is to ensure a cost-justi<sup>fi</sup>able IT capacity matched to the agreed business requirements [72]. The papers assigned to this process are shown in Table 6.

## b.6) IT security management process

The aim of this process is to align IT security with business security and ensure that the con<sup>fi</sup>dentiality, integrity and availability of the organization's assets, information, data and IT services always match the agreed business needs [72]. Table 7 introduces the articles assigned to this process.

## c) Service transition module

The role of service transition is to deliver services that are required by the business into operational use [75]. The following processes are grouped in this module:

## c.1) Transition planning & support process

The goals of this process are to plan and coordinate resources, and to manage the risks of failure and disruption across the transition activities [75]. The articles associated with this process are shown in Table 8.

## c.2) Change management process

The objective of this process is to ensure that standardized methods are used for the ef<sup>fi</sup>cient and prompt handling of all changes [75]. Table 9 summarizes the papers associated with this process.

## d) Service operation module

The purpose of service operation is to deliver services to agreed levels and to manage the applications, technology and infrastructure that support service delivery [73]. The processes for this module are as follows:

## d.1) Incident management process

The objective of this process is to manage and restore normal service operation after an interruption as rapidly as possible and with minimal impact on the business [73].

## Table 7

Simulation modeling in IT security management process

<table><tr><td>Ref</td><td>Approach</td><td>Issues</td></tr><tr><td>[86]</td><td>SD</td><td>Determining the optimal values of security management parameters and their interrelationships.</td></tr><tr><td>[60]</td><td>OMS</td><td>Studying network, attack and intrusion detection systems that can be applied in simulation experiments for networks with SOA architecture.</td></tr><tr><td>[64]</td><td>SD</td><td>Examining a theory of the development of insider-threat risks.</td></tr><tr><td>[68]</td><td>SD</td><td>Integrating change and access controls into their business process in the way that most effectively reduces security risk.</td></tr><tr><td>[69]</td><td></td><td></td></tr><tr><td>[29]</td><td>OMS</td><td>Estimating the improvements of the quality of CVSS-based (Common Vulnerability Scoring Systems) vulnerability prioritization.</td></tr><tr><td>[93]</td><td>MCS</td><td>Determining how the employees&#x27; use of social networks impacts their organization, and identifying how to mitigate potential risks.</td></tr><tr><td>[45]</td><td>OMS</td><td>Introducing a formal approach towards risk-aware service level analysis and planning.</td></tr><tr><td>[67]</td><td>MCS</td><td>Analyzing and handling security events/alerts and managing and remediating security incidents.</td></tr><tr><td>[63]</td><td>MS</td><td>Evaluating cloud service selection across multiple sources considering, mainly, cost and risk factors.</td></tr><tr><td>[105]</td><td>MS</td><td>Examining the protection of client privacy from malicious service providers and different noise generation strategies.</td></tr><tr><td>[106]</td><td></td><td></td></tr><tr><td>[107]</td><td></td><td></td></tr></table>

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

Table 8  
Simulation modeling in transition planning & support process

<table><tr><td>Ref</td><td>Approach</td><td>Issues</td></tr><tr><td>[19]</td><td>SD</td><td>Analyzing the interrelationships between specific KPIs and studying how planned behavior may lead to unintended outcomes.</td></tr><tr><td>[34]</td><td>OMS</td><td>Selecting the optimal cost service provider considering the process progress and service availability.</td></tr></table>

## Table 9

Simulation modeling in change management process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[68]</td><td>SD</td><td>Defining a process for integrating change and access controls into organization business processes.</td></tr><tr><td>[59]</td><td>QM</td><td>Selecting the optimal cost service provider considering both the process progress and the service availability.</td></tr><tr><td>[18]</td><td>OMS</td><td>Discovering change templates from historic traces recorded in provisioning systems. The change logs were generated by simulation of different RFC execution.</td></tr><tr><td>[87]</td><td>PS</td><td>Analyzing the business impact of changes in a network of services. Decision models to schedule service changes in a way to reduce total expected change-related costs have been developed.</td></tr><tr><td>[103]</td><td>OMS</td><td>Presenting a patch management framework based on SLA-driven patch applicability analysis that is better than the traditional ones.</td></tr></table>

Table 10 summarizes the articles associated with this process.

d.2) Request ful<sup>fi</sup>llment process

The aim of this process is to enable users to request services, and to source and deliver the services [73]. The papers associated with this process are shown in Table 11.

d.3) Access management process

The aim of this process is to provide the rights for users to be able to access services and prevent access to nonauthorized users [73].

The authors of [5] use simulation modeling to support decision policies in identity and access management (OMS). The authors focus on the provisioning process of user accounts on enterprise applications and services.

## 2.2. Classifying the referenced articles according to issues addressed

The results presented above identify the main issues addressed in the referenced articles. These issues can be grouped into the <sup>fi</sup>ve categories presented in Table 12.

## 2.3. Studying the use of ITSM frameworks and simulation model development methodologies

There isn't any evidence of the use of both ITSM frameworks and speci<sup>fi</sup>c simulation model development methodologies in the papers analyzed.

## 2.4. Study results

The <sup>fi</sup>rst research question asked whether simulation modeling is used to support decision-making in an ITSM context. The <sup>fi</sup>ndings indicate that these techniques are widely used in this <sup>fi</sup>eld. Most of the analyzed works use them in the scope of the following ITIL processes: strategy management for IT services, <sup>fi</sup>nancial management for IT services, service level management, availability management, capacity management, security management, change management, incident management and request ful<sup>fi</sup>llment. These works focus mainly on the study of service management strategies, process key performance indicators, service cost, service level objectives and process con<sup>fi</sup>guration. Additionally, the simulation approaches most frequently used are system dynamics, discrete event simulation, queuing models and traditional mathematical simulation.

The second and third research questions asked for the use of both ITSM frameworks and simulation model development methodologies. Though several works highlight their importance, evidences of a systematic use of them have not been found.

## 3. Decision-making framework for improving IT service management

The research article analysis conducted in the previous section shows that simulation modeling is extensively used to support decision-making in the <sup>fi</sup>eld of several ITSM processes. Though these papers address many issues and are suitable to solve particular problems, there is no evidence of a systematic use of ITSM frameworks and methodologies in the building process of the simulation models proposed. As a consequence, and given their importance to build credible simulation models that help to solve real-world organization problems, we consider it important to undertake a research effort in this <sup>fi</sup>eld.

Fig. 1 shows Simulation for ITSM (Sim4ITSM), a novel framework to support decision-making to improve ITSM focused on simulation modeling. Its main components are a speci<sup>fi</sup>c methodology to build

## Table 10

Simulation modeling in incident management process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[46]</td><td>SD</td><td>Assessing performance metrics of incident management and problem management processes.</td></tr><tr><td>[58]</td><td>MS</td><td>Analyzing the effects of the differences between support groups.</td></tr><tr><td>[53]</td><td>DES</td><td>Optimizing the number of Help Desk operators and their working time.</td></tr><tr><td>[7]</td><td>QM</td><td>Evaluating different support group reorganization strategies.</td></tr><tr><td>[11]</td><td>DES</td><td>Studying the effects of support group configuration on SLAs compliance.</td></tr><tr><td>[8]</td><td>QM</td><td>Estimating the cost of implementing different incident management strategies and analyzing the alignment of these strategies with the business objectives.</td></tr><tr><td>[9]</td><td>DES</td><td>Examining the dynamics of both the organization and the support groups.</td></tr><tr><td>[10]</td><td>DES</td><td>Introducing a web application developed using a Software-as-a-Service focus and a tiered architecture.</td></tr><tr><td>[25]</td><td>MS</td><td>Identifying key performance indicators of the incident management process.</td></tr><tr><td>[20]</td><td>MS</td><td>Demonstrating that the ticket allocation problem is an instance of the online scheduling problem on unrelated machines, and presenting auction based models for solving it.</td></tr><tr><td>[13]</td><td>OMS</td><td>Proposing an improved management process for cloud computing environments based on BDIM, and describing details about incident predication and prioritization algorithms.</td></tr></table>

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

Table 11  
Simulation modeling in request ful<sup>fi</sup>llment process.

<table><tr><td>Ref</td><td>Approach</td><td>Issues addressed</td></tr><tr><td>[78]</td><td>MS</td><td>Studying alternative dynamic assignment policies in an IT service delivery environment. A heuristic algorithm that assigns and describes the allocation index to each service request received is presented.</td></tr><tr><td>[21]</td><td>MS, DES</td><td>Providing recommended staffing levels in a complex service delivery system.</td></tr><tr><td>[22]</td><td>DES</td><td>Determining minimum staffing requirements while meeting contractual service quality commitments in a global service delivery system.</td></tr></table>

Table 12  
ITSM issues categories addressed.

<table><tr><td>Issue category</td><td>Issue category description and referenced articles</td></tr><tr><td>Service management strategies</td><td>Designing and examining service management strategies to improve the process performance, results and behavior. [2,7-10,13,20,27-29,33,34,37,38,54,57,58,63,64,67-70,76-78,80,84,85,89,91,93,99,102,105-107].</td></tr><tr><td>Key performance indicators (KPIs)</td><td>Defining and evaluating process performance metrics. [1,2,8,13,19,20,25,30,32,40,46,52,60,67-69,76,79,91,93,100,101].</td></tr><tr><td>Service cost</td><td>Analyzing service cost and designing management strategies to reduce service cost and obtain more benefits. [1,31,32,35,57,60,63,66,80,87,88,99].</td></tr><tr><td>Service level objectives (SLOs)</td><td>Determining optimal service level objectives and evaluating its compliance. [1,3,11,28,34,35,40,45,77,91,96,99,103,104].</td></tr><tr><td>Process configuration</td><td>Examining different process configurations and identifying optimal values of the process configuration parameters. [7,11,18,21,22,47,53,59,86].</td></tr></table>

simulation models in this context (SimMet), the simulation models built and model experimentation (model simulation and simulation optimization). SimMet allows us to systematically build correct and consistent simulation models [6,94] to address the issues identi<sup>fi</sup>ed in the literature review considering both ITIL recommendations and organization information. This methodology is the result of adapting other simulation model development methodologies [56,65,83,92] to the particular characteristics that these models present. Fig. 2 summarizes its main activities (A) and tasks (T): a) objective, b) inputs, c) outputs (O), and d) roles that perform it (SM: Service Manager; M: Modeler). In addition, it indicates the activities that use ITIL process recommendations and organization process information a) process description, b) management strategies and techniques, c) KPIs and d) SLOs.

![](/api/attachments/2DKY3E6G/fulltext/images/2606631469597403f8ff36973a1d06471696d0564fcce9f185e3f040d9a4509e.jpg)  
Fig. 1. Decision-making framework for improving ITSM (Sim4ITSM).

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

In the above section, the main issues that are usually addressed through simulation modeling are identi<sup>fi</sup>ed and presented in Table 12. In order to build simulation models that allow us to study these issues, SimMet proposes to model them as indicated in Fig. 2: a) model input parameters represent the process SLOs and the con<sup>fi</sup>guration parameters of both the process and the service management strategies; b) model output variables represent the process output variables (KPIs, results, behavior and cost) and the degree of SLOs compliance; and c) conceptual model represents the behavior of both the process and service management strategies.

Once the simulation models have been built, managers can perform model simulations manipulating the input parameter values

<table><tr><td colspan="2">SimMet Activities and Tasks</td><td>Role</td></tr><tr><td colspan="2">A1. Define organization process. (ITIL, OrgInf)</td><td rowspan="5">SM, M</td></tr><tr><td colspan="2">T1.1. Learn process. To obtain and analyze ITIL process information.</td></tr><tr><td>Inputs:• ITIL.</td><td>O1.1. ITIL process description: a) objectives, b) activity sequence, c) resources, d) inputs/outputs, e) KPIs, f) SLA, and g) strategies/techniques.</td></tr><tr><td colspan="2">T1.2. Adapt the process to the organization. To adapt ITIL process to the specific organization characteristics.</td></tr><tr><td>Inputs:• O1.1. ITIL process description.• Organization process information.</td><td>O1.2. Organization process description: a) objectives, b) activity sequence, c) resources, d) inputs/outputs, e) KPIs, f) SLA, and g) strategies/techniques.</td></tr><tr><td colspan="2">A2. Study process problems. To identify and analyze the main process problems. (ITIL, OrgInf)</td><td rowspan="2">SM,M</td></tr><tr><td>Inputs:• O1.2. Organization process description.• Process problems.</td><td>O2.1. Process problems list: a) code, b) brief description, c) severity, and d) urgency.</td></tr><tr><td colspan="2">A3. Evaluate the applicability of simulation modelling. To study the problems that can be solved through simulation modelling and prioritize them. (ITIL, OrgInf)</td><td rowspan="2">SM,M</td></tr><tr><td>Inputs:• O2.1. Process problems list.</td><td>O3.1. Simulation problems list (process problems that can be resolved using simulation modelling): a) code, b) brief description, and c) priority (calculated considering problem severity and urgency).</td></tr><tr><td colspan="2">A4. Describe the problem. To select and describe the problem to be resolved. (ITIL, OrgInf)</td><td rowspan="2">SM, M</td></tr><tr><td>Inputs:• O3.1. Simulation problems list.• O1.2. Organization process description</td><td>O4.1. Problem description: a) activity sequence, b) resources, c) inputs/ outputs, d) KPIs, e) SLA, and f) strategies/techniques related to the problem.</td></tr><tr><td colspan="2">A5. Select the simulation paradigm. To decide the simulation paradigm most appropriate to solve the problem.</td><td rowspan="2">M</td></tr><tr><td>Inputs:• O4.1. Problem description.</td><td>O5.1. Simulation modelling paradigm. Simulation paradigm chosen to build the model.</td></tr><tr><td colspan="2">A6. Model Conceptualization. (ITIL, OrgInf)</td><td rowspan="9">SM,M</td></tr><tr><td colspan="2">T6.1. Define model context and purpose.</td></tr><tr><td>Inputs:• O4.1. Problem description.</td><td>O6.1. Model context (ITSM process) and purpose (questions to resolve).</td></tr><tr><td colspan="2">T6.2. Define model input parameters (allow to define the simulation scenarios).</td></tr><tr><td>Inputs:• O4.1. Problem description.• O6.1. Model context and purpose.</td><td>O6.2. Model input parameters. They represent the process SLOs and the configuration parameters of both the management strategies and the process, These parameters are shown in the user interface.</td></tr><tr><td colspan="2">T6.3. Define model output variables (provide information about the model purpose)</td></tr><tr><td>Inputs:• O4.1. Problem description.• O6.1. Model context and purpose.</td><td>O6.3 Model output variables. They represent the process outputs variables (KPIs, results, behavior and cost) and the degree of SLOs compliance. These variables are shown in the user interface.</td></tr><tr><td colspan="2">T6.4. Process abstraction. To represent the main elements related to the model purpose and that most influence the output variables.</td></tr><tr><td>Inputs:• O4.1. Problem description.• O6.1. Model context and purpose.• O6.2. Input parameters• O6.3. Output variables</td><td>O6.4. Conceptual model. It represents the process and strategies behavior. The model elements depend on the model purpose (activities sequence, entities and flows, resources, feedback loops, decision points, structural dependences, management strategies, techniques). Different modeling techniques can be used, such as, causal diagram or activities diagram.</td></tr><tr><td colspan="2">A7. Formalize the model. To define the model using formal specification languages.</td><td rowspan="2">M</td></tr><tr><td>Inputs:• O6.4. Conceptual model.</td><td>O7.1 Formal model. The language used to formalize the model will depend on the simulation approach used, such as, Differential Equation Specified System, (DESS, system dynamics) or Discrete Event System Specification (DESS, discrete event simulation). Usually, these formalism are abstracted through graphical notation and the equations derived are the mathematical model that will be resolved through simulation.</td></tr><tr><td colspan="2">A8. Implement the model. To implement the model using a tool that support the simulation approach used.</td><td rowspan="2">M</td></tr><tr><td>Inputs:• O7.1. Formal model.</td><td>O8.1 Simulation model. Simulation model implemented.</td></tr></table>

Fig. 2. SimMet activities and tasks.

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

E. Orta et al. / Decision Support Systems xxx (2014) xxx–xxx

<table><tr><td colspan="2">A9. Verify and validate de model. To check that the model is correct and consistent, and that the structure and behaviour of the process is represented faithfully.</td><td rowspan="2">Role</td></tr><tr><td colspan="2">T9.1. Verify the model. To check that the model is correct and consistent.</td></tr><tr><td>Inputs:• O8.1. Simulation model.</td><td>O9.1. Model verification tests. Barlas and Sterman [6,94] propose the following tests:a) dimensional consistenceteststs (the variable dimensions are consistent and the units correct); b) syntactic validation tests (model equations do not have syntactic errors); andc) semantic validation tests (model equations do not have semantic errors).</td><td rowspan="3">SM, M</td></tr><tr><td colspan="2">T9.2. Validate the model. To check that the model faithfully represents the structure &amp; behaviour of the process.</td></tr><tr><td>Inputs:• O8.1. Simulation model.</td><td>O9.2. Model validation tests. The main tests [6,94] are as follows: a) structure confirmation tests (to compare the model equations with the real process element relations); b) parameter confirmation tests (to evaluate the input parameters with the process knowledge); c) extreme conditions tests (to assign extreme conditions to the input parameters and compare the results obtained with the real process behaviour); d) behavioural sensitivity tests (to determine the input parameters that most influence the output variables and analyze the real process sensitivity to these parameters); and e) behaviour patterns tests (to evaluate the model precision to represent the real process behaviour patterns.</td></tr></table>

Fig. 2 (continued).

Table 13  
SLA parameters (capacity management process).

<table><tr><td>Parameter type</td><td>Parameters</td></tr><tr><td>Service capacity</td><td>Contracted validation rate: credit validation service capacity contracted by the company.</td></tr><tr><td>Service response times (SLOs)</td><td>Expected response time (ERT): maximum service response time above which the provider is penalized.Maximum response time (MRT): maximum service response time above which the validation request is abandoned.</td></tr><tr><td>Service performance (SLOs)</td><td>Validated request rate: minimum percentage of service requests that must be validated within the ERT.Abandoned request rate: maximum percentage of service requests that are permitted to be abandoned.</td></tr><tr><td>Penalties</td><td>Maximum response time penalty: penalty for each service request validated above the expected response time.Abandonment penalty: penalty for each service request abandoned.</td></tr></table>

Table 14  
Model input parameters (capacity management process).

<table><tr><td>Category</td><td>Input parameter</td></tr><tr><td>Client configuration</td><td>Received request rate: trend of the received service requests.SLA parameters (see Table 13).</td></tr><tr><td>Service capacity configuration</td><td>Card validation rate (CVR): validation service capacity that the provider assigns to the company.CVR percentage: percentage of the CVR used to validate the service requests within the ERT. The remaining capacity is used to validate the service requests that awaiting answers within the MRT.Strategy selection: service capacity management strategy used by the service provider.</td></tr></table>

through the user interface. Model simulations provide information that enable managers to analyze the process outputs by varying the con<sup>fi</sup>guration of both the process and the management strategies. Thus, managers can identify the con<sup>fi</sup>guration parameters that produce the most effects on process outputs, and determine the con<sup>fi</sup>guration that meets the SLOs de<sup>fi</sup>ned in the organization. Additionally, optimization experiment results allow managers to determine the process con<sup>fi</sup>guration that meets the optimization objective established. Thus, model experimentation provides information that helps managers to make better decisions to improve processes and meet the business objectives.

The next sections present two application cases in the context of the ITIL capacity management and incident management processes. Not all the activities and tasks performed to build the simulation models are described, only the most relevant ones are summarized to demonstrate the usefulness and applicability of the framework.

Table 15  
Model output variables (capacity management process).

<table><tr><td>Category</td><td>Output variable</td></tr><tr><td>Service behavior</td><td>Requests received: number of service requests received.Requests validated ERT: number of service requests validated within ERT.Requests validated MRT: number of service requests validated within MRT.Requests abandoned: number of service requests abandoned because MRT is exceeded.</td></tr><tr><td>Service performance</td><td>Non-compliance ERT: deviation between the value of the SLA parameter Validated request rate and the rate of service requests validated within ERT.Abandonment non compliance: deviation between the rate of service requests abandoned and the value of the SLA parameter Abandoned Request Rate.Response time penalty: penalization for non-compliance with agreed response times.</td></tr></table>

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

![](/api/attachments/2DKY3E6G/fulltext/images/ce71beed33343a58eb12b376d7de3cdc9ff77c52efcf8de0f5de441d3995565a.jpg)  
Fig. 3. Validated requests ERT (Strategy A).

![](/api/attachments/2DKY3E6G/fulltext/images/2f0bca5d34d8a65e09c25b3a8449c5f332a97c9d0a45c316f2373b9ab62a3f5a.jpg)  
Fig. 5. Validated requests MRT (Strategy A).

## 4. Capacity management process simulation model

## 4.1. Activity A1. Define organization process

## 4.1.1. Task T1.1. Learn process

The purpose of the ITIL capacity management process is to provide the necessary capacity and to offer good quality IT services at a reasonable cost. This process comprises three sub-processes [72]: a) Business Capacity Management, b) Service Capacity Management, and c) Component Capacity Management. This paper focuses on the Service Capacity Management sub-process. The main aim of this sub-process is to manage the service capacity in order to comply with the SLAs that the providers sign with their clients. In this context, service providers can implement different service capacity management strategies which have different effects on the service performance and the degree of SLA compliance.

## 4.2. Activity A4. Describe the problem

For the model construction, a banking validation service provider and an e-commerce company that sells their products through its web portal have been considered. The banking validation service provider provides the company a credit validation service that validates credit card details, and veri<sup>fi</sup>es that the company's customers possess enough credit to realize the purchase. The conditions under which the service must be provided are documented in the SLA signed with the company.

## • SLA parameters

The SLA parameters are classi<sup>fi</sup>ed and described in Table 13 [72]:

• Service capacity management strategies

The service capacity management strategies determine the manner in which the service provider assigns the service capacity to perform the received credit validation service requests within the agreed response times (ERT and MRT). The following strategies are considered in the case study:

![](/api/attachments/2DKY3E6G/fulltext/images/9bf6148535e05c96ea23e01583e6344652dc6ffdfe6aabc868527f47d0e52bcf.jpg)  
Fig. 4. Validated requests ERT (Strategy B).

a) Strategy A: the service provider decides the service capacity percentages that will be used to validate the received service requests within the ERT and MRT, respectively. These percentages are constant and do not change over time.

b) Strategy B: initially, the service provider establishes the service capacity percentages that will be used to validate the service requests within the agreed response times. However, the service capacity assigned to validate service requests within the MRT that is not necessary to use because there are no service requests awaiting response, will be assigned to validate the new service requests received within the ERT. Therefore, the service capacity percentages depend on the received service request rate.

## 4.3. Activity A5. Select the simulation paradigm

The simulation paradigm chosen for building the simulation model is system dynamics.

## 4.4. Activity A6. Model conceptualization

4.4.1. Task T6.1. Define the model context and purpose

The simulation model has been built in the scope of the ITIL service capacity management sub-process [72]. Its purpose is to help service providers to make decisions to properly manage service capacities assigned to their clients, and ensure compliance with SLAs. Additionally, the model allows the study of penalties to be assumed by the provider for non-compliance with the agreed response times (ERT and MRT).

## 4.4.2. Task T6.2. Define model input parameters

The model input parameters are classi<sup>fi</sup>ed and described as Table 14 shows.

## 4.4.3. Task T6.3. Define model output variables

The main output variables can be classi<sup>fi</sup>ed and described as Table 15 summarizes.

![](/api/attachments/2DKY3E6G/fulltext/images/41b4efd07772291b04860c15c63ee6a5c0f1fc76399f449aa76d58e7c2b49b3b.jpg)  
Fig. 6. Validated requests MRT (Strategy B).

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

![](/api/attachments/2DKY3E6G/fulltext/images/cc60e1f39ea2938e8c4458797985ddf16d4370345b268bccdc74f3c5bb370616.jpg)  
Fig. 7. Abandoned requests (Strategy A).

## 4.5. Activity A8. Implement the model

The implementation and simulations of the model have been performed using the Vensim DSS® V.4.0 simulation tool [98].

## 4.6. Model experimentation

To show the usefulness of the simulation model, this section describes some sensitivity analysis experiments conducted to analyze the behavior and performance of the credit validation service. They also enable the study of the penalization for non-compliance with the SLA response time parameters. These experiments have been performed varying the values of the service capacity con<sup>fi</sup>guration parameters (model input parameters): a) service capacity assigned to the company; b) service capacity percentages assigned to validate the received service requests within the agreed response times (ERT and MRT); and c) service capacity management strategies (strategies A or B). The analysis of the simulation results helps the service provider to decide the values of the service capacity con<sup>fi</sup>guration parameters that improve the service behavior and meets the SLA. To illustrate these ideas the following paragraphs summarize some of the experiments performed.

• Experiment 1. The purpose of the sensitivity analysis performed in this experiment is to study the service behavior with the service capacity contracted by the company considered in the study case (4.395 requests/minute), and varying the service capacity strategy and the service capacity percentages. The results obtained show that the service behavior is as follows: a) the trend of the service requests validated within the expected response time (ERT) is very similar with both strategies, but with Strategy A more service requests are validated than with Strategy B (Figs. 3 and 4); b) with Strategy A more services requests are validated within the maximum response time (MRT) than with Strategy B, and these begin to be validated before (Figs. 5 and 6); c) with Strategy B fewer service requests are abandoned than with Strategy A, and these are abandoned later (Figs. 7 and 8); and d) if all the service capacity is used to validate the service requests within the ERT (CVR percentage is equal to 100%), with both strategies

![](/api/attachments/2DKY3E6G/fulltext/images/156ad5a73a43c89d49bf733872a6260ba5d64b9ba071ea2652ad38fc40da44ff.jpg)  
Fig. 8. Abandoned requests (Strategy B).

## Table 16

SLA parameters (incident management process).

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td>MaxResTime</td><td>Maximum incident resolution time.</td></tr><tr><td>IncReqMaxResTime</td><td>Minimum percentage of incidents that must be solved within the MaxResTime.</td></tr><tr><td>Penalization</td><td>Penalty for not meeting the parameter IncReqMaxResTime.</td></tr></table>

having the same number of service requests abandoned and these begin to be abandoned at the same time.

• Experiment 2. The aim of this sensitivity analysis is to determine the values of the service capacity management parameters that ensure SLA compliance. The results obtained indicate the following: a) the valid service capacity values are the same with both strategies (CVR N =4239 requests/minutes); and b) the valid service capacity percentage values vary depending on both the service capacity assigned to the company and the capacity management strategy adopted. So for example, with the service capacity contracted by the company considered in the case study (4.395 requests/minutes), SLAs are met with the following capacity management parameter values: a) Strategy A: CVR percentage N =96%; and b) Strategy B: CVR percentage N =0%.

• Experiment 3. This sensitivity analysis allows one to determine the lowest service capacity and the service capacity percentage values that ensure SLA compliance. In the case study, with both strategies the same results are obtained: a) the lowest valid service capacity is 4.239 requests/minute; and b) CVR percentage N =95%. Moreover, in the scenarios where SLAs are not met, it is observed that the degree of non-compliance is higher with Strategy A than with Strategy B. Besides, with Strategy A the SLAs are not met for longer than with Strategy B.

All these experiments also allow one to study the penalization that would have to be assumed by the provider for non-compliance with the agreed response times. For example, the results obtained in Experiment 1 show that the lowest penalization is obtained with Strategy B and CVR percentage ≤91%. Moreover, considering the smallest valid service capacity obtained in Experiment 2 (4.239 requests/minute), the lowest penalization is obtained with Strategy B and varying in time the value of CVR percentage. Initially, the optimal value of this percentage is 96%, but from a certain point in time (6.25 min) to the end of the simulation, this value changes to 100%. It is observed that the dynamic character of the model helps to decide when to change the CVR percentage value to ensure that the penalization is as low as possible during all of the simulation period.

## 5. Incident management process simulation model

## 5.1. Activity A1. Define organization process

## 5.1.1. Task T1.1 Learn process

The main aim of the ITIL incident management process is to manage and restore the normal service operation after an interruption as rapidly as possible, and with minimal impact on the business [73]. An incident is an unplanned interruption to an IT service or a reduction in the IT service quality [41].

IT support organizations usually consist of a network of support groups structured in several levels (typically 3 to 5). The support groups at lower levels perform generic tasks, while higher level groups perform more technical and speci<sup>fi</sup>c tasks. The technicians of the different support groups are specialized in certain incident categories (e.g., PC, server or network).

The incident management process begins when a client detects an incident and reports the service interruption to the organization. After,

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

Table 17  
Model input parameters (incident management process).

<table><tr><td>Category</td><td>Input parameter</td></tr><tr><td>Client configuration</td><td>ClientQuota:monthly quota for clients of the category i.IncReqRate:received incident trend.IncReqClosed:estimation of the incident percentage solved satisfactorily and closed.SLA parameters (see Table 16).</td></tr><tr><td>Support group configuration</td><td>For each support groupitheth following parameters are defined:SGNumberi:number of operators.SGShifti:active shift.Specialization:incident category in which the support group is specialized.MinTimeij, MedTimeij, MaxTimeij:estimations of the completion times of each process activity j.Efficiency:estimation of the percentage of incidents that the support group can solve without escalating the incidents.</td></tr><tr><td>Incident management strategy configuration</td><td>Parameters that allow the definition of the incident management strategies that the model simulates (a)SeverityStrategies (2), b)PriorityStrategies (2), c)AllocationStrategies (4), and d)Escalation Times (2))Parameters that allow the selection of the strategies that will be used in process simulations (SeverityStrategySel,PriorityStrategySel,Level1AllocStrategySel,Level2AllocStrategySel).</td></tr></table>

the incident is assigned to one of the idle analysts of the <sup>fi</sup>rst level support, who records and classi<sup>fi</sup>es the incident. The analyst also realizes an initial incident analysis to determine its severity and resolution priority. Depending on the incident category, severity and priority, the responsible assigned to resolve the incident could be: a) the analyst who realizes the initial analysis; or b) a technician of a support group specialized in the incident category. If the responsible assigned cannot solve the incident, it is escalated to a higher level support group. It is also possible that technicians of different support groups perform tasks that contribute to solve the incident. Thus, the incident may go through different stages and be treated by several support groups. Finally, the incident is closed if the client con<sup>fi</sup>rms that it has been resolved satisfactorily. Otherwise, the incident is reallocated again to a support group.

The incident management process has objectives that are speci<sup>fi</sup>c to the organization (SLOs), and are speci<sup>fi</sup>ed in the SLA that the organization and its clients sign. Many factors in<sup>fl</sup>uence the process outcomes and the SLA ful<sup>fi</sup>llment, such as the following: a) the organization structure; b) the received incident trend; c) the con<sup>fi</sup>guration and ef<sup>fi</sup>ciency of the support groups; d) the time required to perform the process activities; and e) the incident management strategies implemented in the organization. Therefore, the IT support organizations have to decide how to organize their internal structure and which incident management strategies should be adopted to achieve their SLA targets.

## 5.2. Activity A4. Describe the problem

For the model construction, an IT support organization that has two client categories (Gold and Non-Gold) is considered. The objectives of the incident management process are speci<sup>fi</sup>ed in the SLA that the organization agrees with its clients (Gold clients' SLA and Non-Gold clients SLA).

The SLA parameters, the internal structure of the organization and the incident management strategies considered in the case study are de<sup>fi</sup>ned using the following information as reference: a) the description and recommendations of ITIL Incident

Table 18  
Model output variables (incident management process).

<table><tr><td>Category</td><td>Output variable</td></tr><tr><td>Process behavior</td><td>·IncReqRec: incidents received.·IncReqSol: incidents resolved.</td></tr><tr><td>Process results</td><td>·IncReqSolMRT: incidents resolved within the agreed time limits.·Penalization: penalty for not meeting SLA targets.</td></tr><tr><td>Process performance</td><td>For each support group i the following indicators are obtained:·SGQueueSizei: queue size.·SGIdleAgenti: number of idle operators.·SGUtilizationi: average use.</td></tr></table>

Management process [73]; and b) information obtained from real IT support organizations [7,9].

## • SLA parameters

The SLA parameters considered in this study are shown in Table 16 [73]. The values of these parameters are different for each client category and incident priority. The most restrictive values correspond to higher priority incidents of Gold clients.

## • IT support organization structure

The IT support organization is structured in the following support levels: a) Support Level 0 or Service Desk (composed of six support groups: three groups of Analysts and three groups of Operators); b) Support Level 1 (comprised of ten support groups: GS1–GS10); and c) Support Level 2 (composed of <sup>fi</sup>ve support groups: GS11–GS15). Each support group is specialized in a concrete incident category and is active during one of the work shifts established in the organization (<sup>fi</sup>rst shift, second shift and third shift).

## • Incident management strategies

The organization applies the following incident management strategies:

a) Incident severity strategies. These strategies determine the incident severity based on the incident urgency and impact on the organization.

b) Incident priority strategies. These strategies determine the incident resolution priority according to the client category and the incident severity.

c) Support group allocation strategies. These strategies determine the support group to which the incident is allocated according to the following support group information: operator availability, workload, specialization and average incident resolution time.

d) Incident scaling strategies. These strategies determine the support group level to which the incident is allocated if either of the following occurs: a) the responsible assigned is unable to solve the incident; or b) the maximum waiting time established to solve the incident is exceeded. These strategies also determine the support group allocation strategy that will be applied if the incident is scaled.

The model allows one to simulate two incident severity strategies, two incident priority strategies, four support group allocation strategies and one scaling strategy.

## 5.3. Activity A5. Select the simulation paradigm

The simulation paradigm chosen for model building is discrete event simulation [73].

E. Orta et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/2DKY3E6G/fulltext/images/352db9665cc3d65a8366f9e5cc380979d2200dce0346547f4470afbfb625a89f.jpg)

![](/api/attachments/2DKY3E6G/fulltext/images/e5e9b786246c48b41f8074cb9fe0dc1662a6aac152cdee9eff56b9db3949b55c.jpg)  
Fig. 9. Resolved incidents grouped by client category and priority.

## 5.4. Activity A6. Model conceptualization

## 5.4.1. Task A6.1. Define model context and purpose

The model enables the prediction of process behavior, results and performance considering alternative process con<sup>fi</sup>gurations. Additionally, the model allows the determination of the process con<sup>fi</sup>guration that optimizes the results and meets SLA targets. The organization will comply with the SLA (Table 16) if the percentage of incidents solved within the maximum resolution time (speci<sup>fi</sup>ed in the parameter MaxResTime) is greater than or equal to the value of the parameter IncReqMaxResTime. Additionally, the model allows the analysis of the penalty for non-compliance to the SLA.

## 5.4.2. Task A6.2. Define model input parameters

Given the large number of the model input parameters, they are summarized and clustered into the categories shown in Table 17:

## 5.4.3. Task A6.3. Define model output variables

The main output variables are summarized and grouped in Table 18. The model calculates the total values for the process behavior and the result indicators, and aggregates them by different criteria (client, client category, incident priority, and client category & incident priority).

## 5.5. Activity A8. Implement the model

The implementation and experimentation of the model have been performed using the multiparadigm simulation tool AnyLogic<sup>TM</sup> [4].

## 5.6. Model experimentation

The objectives of the model experiments described in this section are as follows: a) analyzing the process results with an initial process con<sup>fi</sup>guration; and b) examining what changes can be made in the initial process con<sup>fi</sup>guration to improve the process results. Following these three experiments, two optimization experiments are also presented.

• Experiment 1. The purpose of this experiment is to study the process behavior, results and performance with the initial process con<sup>fi</sup>guration considered in the case study. The results obtained show the following process behavior: a) the process solves about 89% of the incidents of priority 1, 2 and 4; but only about 57% of the incidents of priority 3; b) 8.73% of the Gold clients' incidents and 85.61% of the Non-Gold clients' incidents are resolved within the agreed maximum resolution times (average percentage is equal to 59.98%); and c) 83.3% of the total penalty that the organization will have to assume is due to not meeting the Gold clients' SLA (16.7% is due to non-compliance with the Non-Gold clients' SLA). This data can also be studied at other levels of aggregation, such as client category and incident priority. So for example, Fig. 9 presents the resolved incident percentage (at a given time during the simulation) grouped by client category and incident priority. It shows that the most resolved incidents are the Gold clients' incidents of priority 4 (47.6%) and the Non-Gold clients' incidents of priority 4 (40%). Moreover, the least resolved incidents are the Gold clients' incidents of priority 3 (10%) and the Non-Gold clients' incidents of priority 1 (0%).

In addition, the process performance has been analyzed in terms of the sizes, number of busy operators and average use of the

![](/api/attachments/2DKY3E6G/fulltext/images/7553c55b855f970e9325473f845df262aee697cab7d18eda767f93bbe57acc97.jpg)  
Fig. 10. Average use of Level 1 support groups.

Please cite this article as: E. Orta, et al., Decision-making in IT service management: a simulation based approach, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.06.002

Table 19  
Issues addressed through capacity management and incident management.

<table><tr><td rowspan="2">Issues addressed</td><td colspan="2">Simulation models</td></tr><tr><td>Capacity management</td><td>Incident management</td></tr><tr><td>Service management strategies</td><td></td><td></td></tr><tr><td>Designing and examining service management strategies to improve the process performance, results and behavior.</td><td>X</td><td>X</td></tr><tr><td>Key performance indicators</td><td></td><td></td></tr><tr><td>Defining and evaluating process performance metrics.</td><td>X</td><td>X</td></tr><tr><td>Service cost</td><td></td><td></td></tr><tr><td>Analyzing service cost and designing management strategies to reduce service cost and obtain more benefits.</td><td>X</td><td>X</td></tr><tr><td>Service level objectives</td><td></td><td></td></tr><tr><td>Determining optimal service level objectives and evaluating its compliance.</td><td>X</td><td>X</td></tr><tr><td>Process configuration</td><td></td><td></td></tr><tr><td>Examining different process configurations and identifying optimal values of the process configuration parameters.</td><td></td><td>X</td></tr></table>

support groups. It is observed that while some support groups (e.g. GS1 and GS2) have a high average use and incidents in its queues, and all its operators are busy; others (e.g. GS3 and GS4) have lower average use, idle operators and no pending incidents. Fig. 10 shows the average use of Level 1 support groups at a given time during the simulation.

The results of this experiment show that the initial process con-<sup>fi</sup>guration considered in the case study is inadequate because 27% of the incidents are not resolved satisfactorily, the degree of non-compliance with Gold clients' SLA is very high (91.2 %), and the support groups' performance is bad and could be improved. To decide what changes to realize in the initial process con<sup>fi</sup>guration to improve the process results, Experiments 2 and 3 have been performed.

• Experiment 2. This sensitivity analysis has been con<sup>fi</sup>gured varying the values of the following model input parameters: a) Service Desk con<sup>fi</sup>guration; b) incident severity strategy selected; and c) incident priority strategy selected. Simulation results indicate that the best results are obtained with the following process con-<sup>fi</sup>guration: a) 4 analysts and 1 operator in the support groups active in the <sup>fi</sup>rst or second shift; b) incident severity strategy number two; and c) incident priority strategy number two. With this process con<sup>fi</sup>guration, the percentage of incidents resolved within the agreed time limits is equal to 81.12%. This percentage is 21.15% higher than the percentage obtained with the initial process con<sup>fi</sup>guration (59.98%). Therefore, the model is highly sensitive to changes in the con<sup>fi</sup>guration of the Service Desk, and the incident severity and priority strategies.

• Experiment 3. Another sensitivity analysis has been con<sup>fi</sup>gured varying the values of the incident scaling strategy con<sup>fi</sup>guration parameters. Simulation results show that the range of values obtained for the output variable that measures the average percentage of incidents resolved within the agreed times, is between 80% and 82.3%. The optimum value of this variable (82.3%) is only 1.18 % higher than the value obtained with the initial process con<sup>fi</sup>guration (81.12%). Therefore, the model is only slightly sensitive to changes in the con<sup>fi</sup>guration of the incident scaling strategy.

Finally, two optimization experiments performed using the metaheuristic techniques of the AnyLogic<sup>TM</sup> optimization engine OptQuest are presented.

• Optimization Experiment 1. This experiment allows the determination of the support group con<sup>fi</sup>guration and the values of the scaling parameters that maximize the percentage of incidents that the process can resolve without exceeding the time limits established in SLAs. In this experiment, restrictions to limit the maximum values of the personnel con<sup>fi</sup>guration parameters have been set. In the optimal process con<sup>fi</sup>guration obtained in the scenario simulated, the maximum percentage of incidents that can be resolved within the agreed times is equal to 83.07 %.

• Optimization Experiment 2. The purpose of this experiment is to determine the process con<sup>fi</sup>guration that meets a concrete optimization objective, and minimizes the deviation between the following data: a) the minimum percentage of incidents that must be resolved within the agreed times (value of the SLAs parameter IncReqMaxResTime); and b) the percentage of incidents that the process resolves within the agreed times. The optimization objective in the simulated scenario is the following: “The percentage of incidents resolved within the resolution times agreed in the SLAs must be greater or equal to 95% of the incidents received”. The optimal process con<sup>fi</sup>guration that meets the optimization objective enables the resolution of 97.58% of the incidents received within the SLA time targets.

## 6. Conclusions and further work

This paper focuses on the application of simulation modeling to support decision-making in the scope of ITSM. A study of published research articles that propose simulation models in this context has been presented. It shows that different simulation approaches have been used to address many issues in the context of several processes. These issues can be grouped and classi<sup>fi</sup>ed as follows: de<sup>fi</sup>ning appropriate service management strategies, analyzing process key performance indicators, studying and improving service cost, evaluating service level objective compliance and determining optimal process con<sup>fi</sup>guration.

However, in these works there is no evidence of a systematic use of both ITSM frameworks and simulation model development methodologies. As a consequence, and given their importance to build valid simulation models, this paper proposes a novel decision-making framework for improving ITSM based on simulation modeling (Sim4ITSM). The main component of Sim4ITSM is a simulation model development methodology (SimMet) that helps to systematically build simulation models applying ITIL recommendations to address the issues identi<sup>fi</sup>ed in the study of research articles conducted. The model simulations provide information about the model purpose and allow managers to experiment with different decisions, varying the model input parameter values via the user interface. Thus, the analysis of the model experimentation results helps managers to know the effects of changes before their implementation in the organization and to make better decisions.

To illustrate the usefulness and applicability of the framework proposed, two application cases in the context of the ITIL capacity management and incident management processes have been introduced. The purpose of the capacity management model is to help the service provider decide what service capacity management strategy to adopt to improve the service response times and ensure service level objective compliance. Further, the incident management process model allows managers to examine the process results with alternative process con-<sup>fi</sup>gurations, and determine the process con<sup>fi</sup>guration that optimizes the results and meets the SLOs. Table 19 summarizes the issues from Table 12 that can be addressed through experimentation with these models.

Finally, the main objectives of further work in this area are as follows:

• Extend the functionality of the simulation models presented in this work to solve more complex problems (different simulation approaches can be applied).

• Build simulation models in the context of other ITSM processes.

• Apply multi-objective optimization techniques to optimize simulation outputs.

• Integrate the models developed in a tool based on multiparadigm simulation that is currently under development (this tool will allow the simulation of interrelated ITSM processes within a common framework).

## Acknowledgments

This work has been partially supported by the Spanish Ministry of Science and Technology with ERDF funds under grants TIN2010- 20057-C03-03, and TIN2013-46928-C3-2-R.

## References

[1] B. Abrahao, V. Almeida, J. Almeida, A. Zhang, D. Beyer, F. Safai, Self-adaptive SLA-driven capacity management for internet services, 10th IEEE/IFIP Network Operations and Management Symposium, 2006. 557–568.

[2] V. Almeida, Capacity planning for web services, Techniques and Methodology, LNCS 2459, Performance Evaluation of Complex Systems: Techniques and Tools, Performance, Tutorial Lectures2002. 142-157.

[3] L. An, J. Jeng, Web services management using system dynamics, Proceedings of the IEEE International Conference on Web Services, 2005, pp. 347–354.

[4] AnyLogic®, http://www.anylogic.com (consulted in April of 2014).

[5] A. Baldwin, M. Mont, S. Shiu, Using modeling and simulation for policy decision support in identity management. Proceedings of the IEEE International Symposium Policies for Distributed Systems and Networks, 2009. pp. 17-24

[6] Y. Barlas, Formal aspects of model validity and validation in system dynamics, System Dynamics Review, 12(3), John Wiley & Sons, 1996, pp. 183–210.

[7] C. Bartolini, C. Stefanelli, M. Tortonesi, SYMIAN: a simulation tool for the optimization of the IT incident management process, Proceedings of the IFIP/IEEE International Workshop on Distributed Systems: Operations and Management: Managing Large-Scale Service Deployment, 2008, pp. 83–94.

[8] C. Bartolini, C. Stefanelli, M. Tortonesi, Business-impact analysis and simulation of critical incidents in IT service management, Proceedings of the International Conference on Symposium on Integrated Network Management, 2009, pp. 9–16.

[9] C. Bartolini, C. Stefanelli, M. Tostonesi, SYMIAN: analysis and performance improvement of the IT incident management process, IEEE Transactions on Network and Service Management 7 (3) (2010) 132–144 (2010).

[10] C. Bartolini, D. Stefanelli, D. Targa, M.A. Tortonesi, Web-based what-if scenario analysis tool for performance improvement of IT support organizations, Proceedings of the International Conference on Network and Service Management, 2011, pp. 1–5.

[11] C. Bartsch, M. Mevius, A. Oberweis, Simulation environment for IT service support processes, Proceedings of the International Conference on Information, Process and Knowledge Management, 2010, pp. 23–31.

[12] C. Bongsug, A complexity theory approach to IT-enabled services (IESs) and service innovation: business analytics as an illustration of IES, Decision Support Systems 57 (2014).1-10

[13] C. Cao, Z. Zhan, Incident management process for the cloud computing environments, Proceedings of the IEEE International Conference on Cloud Computing and Intelligence Systems. 2011, pp. 225–229

[14] Capability Maturity Model Integration (CMMI), http://www.sei.cmu.edu/cmmi/ (consulted in April of 2014).

[15] A. Cater-Steel, W.G. Tan, M. Toleman, Using institutionalism as a lens to examine ITIL adoption and diffusion, Proceedings of ACIS, 2009, (paper 73).

[16] D.C. Chat<sup>fi</sup>eld, T.P. Harrison, J.C. Hayya, SISCO: an object-oriented supply chain simulation system, Decision Support Systems 42 (2006) 422–434.

[17] S.W. Choua, C.H. Chiangb, Understanding the formation of software-as-a-service (SaaS) satisfaction from the perspective of service quality, Decision Support Systems 56 (2013) 148–155.

[18] W. Cordeiro, G. Machado, F. Andreis, J. Wickboldt, R. Lunardi, R.A. dos Santos, CHANGEMINER: a solution for discovering IT change templates from past execution traces, Proceedings of the IFIP/IEEE International Symposium on Integrated Network Management, 2009, pp. 97–104

[19] W. Currie, P. Joyce, P.G. Winch, Evaluating application service provisioning using system dynamics methodology, British Journal of Management 18 (2006) 172–191.

[20] H. Demirkan, D. Delen, Leveraging the capabilities of service-oriented decision sup port systems: putting analytics and big data in cloud, Decision Support Systems 55 (1) (2013) 412–421.

[21] P. Deshpande, D. Garg, N. Rama Suri, Auction based models for ticket allocation problem in IT service delivery industry, Proceedings of the IEEE International Conference on Services, Computing, 2008, pp. 111–118.

[22] Y. Diao, A. Heching, Staf<sup>fi</sup>ng optimization in complex service delivery systems, Proceedings of the 7th International Conference on Network and Service Management, 2011, pp. 1–9.

[23] Y. Diao, D. Nurthcutt, Modeling a complex global service delivery system, Proceedings of the Winter Simulation Conference, 2011, pp. 690–702.

[24] N.D. Domenica, G. Mitra, P. Valente, G. Birbilis, Stochastic programming and scenario generation within a simulation framework: an information systems perspective, Decision Support Systems 42 (2007) 2187–2218.

[25] D. Donko, I. Traljic, Performance estimation of organizational activity, Proceedings of the 2nd IEEE International Conference on Computer Science and Information Technology, 2009, pp. 284–288.

[26] S. Feng, X.L. Ling, Z.G. Duan, J.L. Zhang, Assessing the impacts of south-to-north water transfer project with decision support systems, Decision Support Systems 42 (2007) 1989–2003.

[27] A. Folgueras, F.J. Sáenz, M. de la Cámara Delgado, Técnicas de modelado de los costes variables aplicados al proceso de plani<sup>fi</sup>cación estratégica con <sup>fi</sup>losofía ciclo de vida de servicios TI, III Congreso Internacional itSMF España, Universidad Carlos III de Madrid, Madrid, 2008, (C. Fruhwirth, T. Mannisto, Improving CVSSbased vulnerability prioritization and response with context information, in: Proceedings of the 3rd International Symposium on Empirical Software Engineering and Measurement, 2009, pp. 535–544).

[28] U. Franke, Optimal IT service availability: shorter outages, or fewer? IEEE Transactions on Network and Service Management 9 (1) (2012) 22–33.

[29] C. Fruhwirth, T. Mannisto, Improving CVSS-based vulnerability prioritization and response with context information, Proceedings of the 3rd International Symposium on Empirical Software Engineering and Measurement, 2009, pp. 535–544.

[30] F. Gao, X. Qiu, L. Meng, SLA based business-driven adaptive QoS maintenance mechanism for multi-tier service in virtualized IT environment, Proceedings of the International Workshop on Management of Emerging Networks and Services, 2010, pp. 627–631.

[31] H. Gebauer, A dynamic theory of service management: implications for managing service improvements avoiding the “Service Jungle”, Proceedings of the XX International Conference System Dynamics Society 2002

[32] I. Goiri, J. Guitart, J. Torres, Economic model of a cloud provider operating in a federated cloud, Information System Frontiers 14 (2012) (2012) 827-843.

[33] P. Gokhale, R. Kumar, T. Das, A. Gumaste, Cloud computing over metropolitan area WDM networks: the light-trails approach, Proceedings of the IEEE Global Telecom munications Conference, 2010, pp. 1–6.

[34] G. Grabarnik, H. Ludwi, L. Schwartz, Management of service process QoS in a service provider–service supplier environment, Proceedings of the 9th IEEE International Conference on E-Commerce Technology and the 4th IEEE International Conference on Enterprise Computing, E-Commerce and E-Services, 2007, pp. 543–550.

[35] G. Grabarnik, H. Ludwig, L. Shwartz, Dynamic management of outsourced service processes' QoS in a service provider–service supplier environment, Proceedings of the 3rd IEEE/IFIP International Workshop on Business-driven IT Management 2008, pp. 81–88.

[36] A. Gregoriades, B. Karakostas, Unifying business objects and systems dynamics as a paradigm for developing decision support systems, Decision Support Systems 37 (2004) 307–3011.

[37] W. Hailegiorgis, D. Williams, Modelling capacity requirements for BBC IT storage area network: experience and research, Proceedings of the 22nd International Conference System Dynamics Society, 2004.

[38] M. Hoyer, D. Schlitt, Proactive dynamic resource management in virtualized data centers, Proceedings of the 2nd International Conferencia on Energy-Ef<sup>fi</sup>cient Computing and Networking, 2012, pp. 11–20.

[39] W. Hu, A. Almansoori, P.K. Kannan, S. Azarm, Z. Wang, Corporate dashboards for integrated business and engineering decisions in oil refineries: an agent-based approach Decision Support Systems 52 (2012 729-741

[40] O. Hühn, C. Markl, M. Bichler, On the predictive performance of queuing network models for large-scale distributed transaction processing systems, Information Technology and Management 10 (2–3) (2009) 135–149.

[41] ISO/IEC 20000-1, Information Technology — Service Management — Part 1: Service Management Systems Requirements. 2011.

[42] ISO/IEC 20000-2, Information Technology — Service Management — Part 2: Guidance on the Application of Service Management Systems, 2012.

[43] ITIL, http://www.itil-of<sup>fi</sup>cialsite.com/ 2011 (consulted in April of 2014).

[44] ITIL®, Glossary and Abbreviations, 2011.

[45] S. Jakoubi, S. Tjoa, S. Goluch, G. Kitzler, A formal approach towards risk-aware service level analysis and planning, International Conference on Availability, Reliability and Security, 2010, pp. 180–187.

[46] H.L. Jung, S.H. Young, K.Y.S. Chanchoon, C. Minju, J. Taikyeong, L.P. Gyung, H. Jun, IT service management case base & simulation analysis and design: systems dynamics approach, Proceedings of the International Conference on Convergence Information Technology, 2007, pp. 1559–1566.

[47] S. Karapetrovic, W. Willborn, Techniques connecting internal management systems in service organization, Managing Service Quality 8 (4) (1998) 256–271.

[48] M.I. Kellner, R.J. Madachy, D.M. Raffo, Software process simulation modeling: why? what? how? The Journal of Systems and Software 46 (2/3) (1999) 91–105.

[49] A.H. Khataie, A.A. Bilgat, J.J. Segovia, Activity-based costing and management applied in a hybrid decision support system for order management, Decision Support Systems 52 (2011) 142–156.

[50] J.Y. Kim, K. Altinkemer, A. Bisi, Yield management of workforce for IT service providers, Decision Support Systems 53 (1) (2012) 23–33.

[51] R. Krebs, C. Momm, S. Kounev, Metrics and techniques for quantifying performance isolation in cloud environments, Proceedings of the 8th International ACM SIGSOFT Conference on the Quality of Software Architectures, 2012, pp. 91–100.

[52] M. Kuncova, P. Wasserbauser, Discrete event simulation—HelpDesk model in SIMPROCESS, Proceedings of the European Conference on Modelling and Simula tion, 2007, pp. 105–110.

[53] G. Landi, N. Ciulli, J. Buyse, K. Georgakilas, M. Anastasopoulos, A. Tzanakaki, C. Develder, E. Escalona, D. Parniewicz, A. Binczewski, B. Belter, A network control plane architecture for on-demand co-provisioning of optical network and IT services, Proceedings of the Future Network & Mobile Summit Conference, 2012, pp. 1–8.

[54] A. Law, How to conduct a successful simulation study, Proceedings of the Winter Simulation Conference, 2003, pp. 66–70.

[55] A.M. Law, How to build valid and credible simulation models, Proceedings of the Winter Simulation Conference, 2009, pp. 24–33.

[56] Y. Lee, L. An, S. Bagchi, D. Connors, S. Kapoor, Discrete event simulation modelling of resource planning and service order execution for service business, Proceedings of the 2007 Winter Simulation Conference, 2007, 2007, pp. 2227–2233.

[57] T. Li, R.J. Kauffman, Adaptive learning in service operations, Decision Support Systems 53 (2) (2012) 306–319.

[58] X. Li, Z. Zhan, S. Guo, L. Zhang, IT incident assign algorithm based on the difference between support groups, Proceedings on the International Conference on Advanced Intelligence and Awareness Internet, 2010, pp. 319–323.

[59] X. Luo, K. Kar, S. Sahu, P. Pradhan, A. Shaikh, On improving change management process for enterprise IT services, Proceedings of the IEEE International Conference on Services, Computing, 2008, pp. 341–348.

[60] J. Magott, M. Woda, Evaluation of SOA security metrics using attack graphs, Proceedings of the Third International Conference on DepCos-RELCOMEX 2008 pp. 277–284.

[61] M. Marrone, L.M. Kolbe, Uncovering ITIL claims: IT executives' perception on benefits and Business-IT alignment. International Systems and E-business Management 9 (3) (2011) 363–380.

[62] M. Marrone, L.M. Kolbe, Impact of IT service management frameworks on the IT organization. An empirical study on bene<sup>fi</sup>ts, challenges and processes, Business & Information System Engineering 3 (1) (2011) 5–18.

[63] B. Martens, F. Teuteberg, Decision-making in cloud computing environments: a cost and risk based approach, Information Systems Frontiers 14 (4) (2012) 871-893.

[64] I.J. Martínez, G.P. Richardson, Best practices in system dynamics modeling, Proceedings of the 19th International Conference of the Systems Dynamics Society, 2001.

[65] I.J. Martinez-Moyano, E. Rich, S. Conrad, D.F. Andersen, T.R. Stewart, A behavioral theory of insider-threat risks: a system dynamics approach, Transactions on Modeling and Computer Simulation 18 (2) (2008) (article no. 7).

[66] O. Mazhelis, Tyrväinen, Economic aspects of hybrid cloud infrastructure: user organization perspective, Information System Frontiers 14 (4) (2012) 845–869.

[67] M. Mont, R. Brown, S. Arnell, N. Passingham, Security analytics: risk analysis for an organisation's incident management process, HP Laboratories, Technical Report HPL-2012-206 2012.

[68] A. Moore, A.R. Antao, Improving management of information technology: system dy namics analysis of IT controls in context, Proceedings of the 24th International Con: ference of the System Dynamics Society, 2006, (http://www.systemdynamics.org/ conferences/2006/proceed/papers/MOORE341.pdf).

[69] A. Moore, R. Antao, Modeling and analysis of information technology change and access controls in the business context, Technical Note CMU/SEI-2006-TN-040 Carnegie Mellon University 2007

[70] L. Nogueira, L.M. Pinho, Dynamic QoS adaptation of inter-dependent task sets in cooperative embedded systems, Proceedings of the 2nd International Conference on Autonomic Computing and Communication Systems, 2008, (article no. 34.).

[71] Of<sup>fi</sup>ce of Government Commerce (OGC), ITIL® Continual Service Improvement, 2011.

[72] Of<sup>fi</sup>ce of Government Commerce (OGC), ITIL® Service Design, 2011.

[73] Of<sup>fi</sup>ce of Government Commerce (OGC), ITIL® Service Operation, 2011.

[74] Of<sup>fi</sup>ce of Government Commerce (OGC), ITIL® Service Strategy, 2011.

[75] Of<sup>fi</sup>ce of Government Commerce (OGC), ITIL® Service Transaction, 2011.

[76] E. Orta, M. Ruiz, M. Toro, Analyzing strategic business rules through simulation modeling, Proceedings of the IFIP Conference on E-Business, E-Services and E-Society, 2009, pp. 357–368.

[77] E. Orta, M. Ruiz, M. Toro, A system dynamics approach to web service capacity management, Proceedings of the European Conference on Web Services, 2009, pp. 109–117.

[78] H. Parvin, A. Bose, M. Van Oyen, Priority-based routing with strict deadlines and server <sup>fl</sup>exibility under uncertainty, Proceedings of the Winter Simulation Conference, 2009, pp. 3181–3187

[79] D. Peng, Y. Yuan, X. Wang, A. Zhou, Capacity planning for composite web services using queuing network-based models, Proceedings of the 5th International Conference in Advances in Web-Age Information Management, LNCS, 3129, 2004, pp. 439–448.

[80] T. Popkov, Y. Karpov, Using simulation modeling for IT cost analysis, 10th HP Open View University Association Workshop, 2003.

[81] D.J. Power, Decision Support Systems: Concepts and Resources for Managers, Quorum Books, Westport, Conn, 2002.

[82] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (3) (2007) 1044–1061.

[83] S. Robinson, Conceptual modeling for simulation: issues and research requirements, Proceedings of the Winter Simulation Conference, 2006, pp. 792–800.

[84] I. Rodero, J. Jaramillo, A. Quiroz, M. Parashar, F. Guim, S. Poole, Energyef<sup>fi</sup>cient application-aware online provisioning for virtualized clouds and data centers, Proceedings of the International Green Computing Conference, 2010, pp. 31–45.

[85] F. Salfner, K. Wolter, A Petri model for service availability in redundant computing systems, Proceedings of the Winter Simulation Conference, 2009, pp. 819–826.

[86] J.M. Sarriegi, J. Santos, J.M. Torres, D. Imizcoz, A.L. Plandolit, Modeling security management of information systems: analysis of an ongoing practical case, Proceedings of the 24th International Conference of the System Dynamics Society, 2006, (http://www.systemdynamics.org/conferences/2006/proceed/ index.htm ).

[87] L. Schmid, J. Gallati, K. Hügel, M. Loher, Success dynamics - a concept for building system dynamics models as decision support within strategic management, the 30th International Conference of the System Dynamics Society, Tutorial Lectures 2008. http://www.systemdynamics.org/conferences/2012/proceed/papers/P1101. pdf .

[88] T. Setzer, K. Bhattacharya, H. Ludwig, Decision support for service transition management, Proceedings of the Network Operations and Management Symposium, 2008, pp. 200–207.

[89] T. Setzer, K. Bhattacharya, H. Ludwig, Change scheduling based on business impact analysis of change-related risk, IEEE Transactions on Network and Service Management 7 (1) (2010) 58–71.

[90] M. Shayne, M. Kunc, J. Morecroft, S. Rockart, System dynamics and strategy, System Dynamics Review, 24 (4), John Wiley & Sons, Ltd., 2009, pp. 407–429.

[91] A. Shrestha A. Cater-Steel M. Toleman W.G. Tan A decision support tool to define scope in IT service management process assessment and improvement. LNCS 7939 (2013) 308-323.

[92] E. Silva, E.Y. Chaix, Business and IT governance alignment simulation essay on a business process and IT service model, Proceedings of the 41st Annual Hawaii International Conference on Systems Science, 2008, pp. 434–445.

[93] A. Squicciarini, M. Casassa-Mont, S. Rajasekaran, Using modeling and simulation to evaluate enterprises' risk exposure to social networks, IEEE Computer 44 (1) (2011) 66–73.

[94] J.D. Sterman, Business Dynamics. Systems Thinking and Modeling for a Complex World, McGraw-Hill, 2000.

[95] A.A. Tako, S. Robinson, The application of discrete event simulation and system dynamics in the logistics and supply chain context, Decision Support Systems 52 (2012) 802–815.

[96] S. Thanheiser, L. Liu, H. Schmeck, SimSOA: an approach for agent-based simulation and design-time assessment of SOC-based IT systems, Proceedings of the Symposium on Applied Computing, 2009, pp. 2162–2169.

[97] T.M. Theresa, M. Edgington, T.S. Raghu, Ajay S. Vinze, Using process mining to identify coordination patterns in IT service management, Decision Support Systems 49 (2) (2010) 175–186.

[98] Vensim DSS®, http://www.vensim.com (consulted in April of 2014).

[99] D. Villela, Provisioning servers in the application tier for e-commerce systems, ACM Transactions on Internet Technology 7 (1) (2007) (article no. 7).

[100] L. Wang, A. Sahai, J. Pruyne, A model-based simulation approach to error analysis of IT services, Proceedings of the 10th IFIP/IEEE International Symposium on Integrated Network Management. 2007 pp. 805-808

[101] U. Winkler, M. Fritzsche, W. Gilani, A. Marshall, A model-driven framework for process-centric business continuity management, Proceedings of the Seventh International Conference on the Quality of Information and Communications Technology, 2010, pp. 248–252.

[102] D. Xu, Y. Wang, X. Li, X. Qiu, ICT service composition method based on service catalogue model, Proceedings of the International Conference on Advanced Intelligence and Awareness Internet, 2010, pp. 324–328.

[103] B. Yang, N. Aran, S. Zeng, R. Puri, SLA-driven applicability analysis for patch management, IFIP/IEEE International Symposium on Integrated Network Management, 2011, pp. 438–445.

[104] G. Zhang, Y. Yang, A historical probability based noise generation strategy for privacy protection in cloud computing, Journal of Computer and System Sciences 78 (5) (2012) 1374–1381.

[105] L. Zhang, Z. Zhan, X. Li, BDIM-based optimal design of response time SLO for SaaS, 3rd IEEE International Conference on Broadband Network and Multimedia Technology, 2010, pp. 228–232.

[106] G. Zhang, Y. Yang, X. Liu, J. Chen, A time-series pattern based noise generation strategy for privacy protection in cloud computing, Proceedings of the 12th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing, 2012, pp. 458–465.

[107] G. Zhang, Y. Yang, D. Yuan, J. Chen, A trust-based noise injection strategy for privacy protection in cloud, Software - Practice and Experience 42 (4) (2012) 431–445.

[108] H. Zhen, C.K.M. Lee, A decision support system for procurement risk management in the presence of sport market, Decision Support Systems 55 (1) (2013).67-78

Elena Orta holds a Computer Science degree from the University of Seville (Spain) and a PhD from the University of Cádiz (Spain). Nowadays, she is an Associate Professor at the University of Cadiz (Spain). She is a member of the Software Process Improvement & Formal Methods Research Group, and itSMF Spain. She is mainly interested in decisionmaking in IT Service Management and simulation modeling techniques. She is author or co-author of papers in international conferences and journals. Her email address is elena.orta@uca.es.

Mercedes Ruiz holds a PhD in Software Engineering from the University of Seville, Spain. She is currently an Associate Professor at the University of Cadiz, Spain, where she leads the Software Process Improvement and Formal Methods Research Group. Her research interests are: simulation-based decision support applied in Software and Services Engineering, as well as simulation-based learning and assessment. She is the author or co-author of numerous papers in international conferences and journals. She is a member of ACM and of the Spanish Chapter of the ACM-SIGCSE. Her email address is mercedes.ruiz@uca.es.

Nuria Hurtado has a Computer Science degree from the University of Granada (Spain) and a PhD from the University of Cádiz (Spain). She is a member of the Software Process Improvement and Formal Methods (SPI&FM) Research Group, and the AIPO Association (Human Computer Interaction Association). Her main research interest is the application of simulation modeling techniques to improve interactive system usability and teamwork. She is author or co-author of several book chapters and papers in journals and international conferences. Her email address is nuria.hurtado@uca.es.

David Gawn is a PhD student at the UCA. He has a BSc (honors) in Microelectronic Systems from the University of Ulster, N. Ireland. His <sup>fi</sup>elds of research are modeling and simulation applied to IT Service Management processes. He most recently worked as a Service Delivery Manager in IBM Global Services, Spain. Previously he performed a variety of software engineering roles in companies such as Visteon Corporation, Ford Motor Company, and British Telecom. His email address is david.gawn@mail.uca.es
