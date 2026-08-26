---
otero_id: 12662
otero_key: "69EUHTCX"
title: "Building and evaluating ESET: A tool for assessing the support given by an enterprise system to supply chain management"
authors: "K. Dharini Amitha Peiris; Jin Jung; R. Brent Gallupe"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.05.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building and evaluating ESET: A tool for assessing the support given by an enterprise system to supply chain management

K. Dharini Amitha Peiris <sup>a,</sup>⁎, Jin Jung <sup>a</sup>, R. Brent Gallupe

<sup>a</sup> Department of Information Systems, Business School, University of Auckland, New Zealand <sup>b</sup> School of Business, Queen's University, Kingston, Ontario Canada

## a r t i c l e i n f o

Article history: Received 6 June 2013 Received in revised form 16 April 201 Accepted 7 May 2015 Available online 16 May 2015

Keywords: Impact of Enterprise Systems on Supply Chain Management Systems Evaluation Qualitative Evaluation of Decision Support Systems Enterprise Systems Supply Chain Management Systems

## a b s t r a c t

Modern organisations must effectively manage their supply chains, to exist and grow. Supply chains draw information extensively from enterprise systems (ESs) of participating businesses. Despite that supply chains frequently depend on information from ES to succeed, not much research on measuring the effectiveness of information transfers between these systems has been published. This paper describes the building and evaluation of a flexible decision support tool that evaluates the impact an ES has on supply chain management (SCM), thereby filling a gap in the SCM assessment portfolio of tools. The main purpose of the Enterprise System Evaluating Tool (ESET), is to measure the support given by ES to SCM and identify process points at which such support fails. Thus ESET empowers organisations with knowledge to improve their supply chain performance by modifying and/or enhancing the ES. A case study based approach was used to evaluate ESET to ascertain its utility by applying it in two Fortune 100 organisations within one industry. In future research, ESET will be applied across many industries, to quantitatively evaluate ESET and refine it further. Analytics on data gathered from these organisations may then enlighten researchers and practitioners on the current state of support given by ES to SCM.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

After many years of improving the effectiveness of internal operations, organisations are now focusing on improving processes across supply chains [2,78]. The number of organisations consciously participating in supply chains has grown dramatically in the last decade [27,83]. Successful supply chain management (SCM) often depends on the extent of support provided by organisation-wide information systems (ISs) such as enterprise systems (ESs) [2,12,22,57,59,71,81,91]. Recognising this ES–SCM interdependence, vendors strive to develop ES to better support SCM processes [2,12,22,37,83]. Delone and Mclean state that it is critical to measure IS performance in order to better understand the value and efficacy of management actions and IS investments. The practical problem that motivated this study is that, despite significant investments being made in ES and in SCM, knowledge of how well an ES supports SCM is sparse [81,91]. Support given by ES to SCM is not often measured and therefore not optimised [2,11,29,70, 91]. We could not find any suitable non-intrusive, customisable and easy to use tool available that enabled comprehensive measurement of such support, whilst providing diagnostics to inform which process points in an ES must be strengthened.

ES are organisation-wide IS that are integrated across organisational functions [1,2,20]. These systems have evolved from isolated transaction processing systems, to systems that automate routine processes, share information across business functions, and generate business analytics [1,2,20]. An ES impacts performance at process, organisation and supply chain levels, benefitting the focal organisation and supply chain partners. Organisations are increasingly aware that ES are critical to achieve cost reductions and efficiencies that lead to competitive advantage [29,36,53,58,69]. They have become vastly complex systems that support many groups of people who work together with vast amounts of resources, under pressures of time, facing many challenges and across organisations. Not surprisingly, many ES implementations turn out to be less successful than originally intended [1,20,55]. However, most ESs are also considered to be cost-effective enablers of B2B (business to business), B2C (business to consumer) and B2E (business to employee) information transfers [7,9,54]. In this paper we refer to all types of enterprise-wide information systems, as ES.

A supply chain (SC) is typically defined as a group of organisations linked by flows of products, services, finances, and information from a supplier's supplier (upstream) to a customer's customer (downstream) [19,32,50]. SCM is the management of these flows from upstream production through to downstream distribution of products and/or services to reach customers, ideally just in time, to satisfy their needs [3,12,29, 31,32,86]. Many types of supply chains exist [18]. The tool we developed can be applied in all types of supply chains. It focuses on measuring the effectiveness of information sharing between an organisation's internal and SCM processes. Many researchers consider that effective collaboration and efficient transfer of information to be critical between supply chain partners [12,22,53,91]. Indeed, this research is related to research streams such as Collaborative Planning Forecasting and Replenishment systems (CPFRS) that focus on networking organisations through their ES [35]. Although in some environments ESs of supply chain partners allow collaboration, in other situations communication between organisations happens mainly through specialised automated or semiautomated software, known as supply chain management systems (SCMSs) [3,12,22]. Currently most vendors attempt to align ES with SCM processes, particularly to reduce inventory and working capital, and to forge closer relationships with customers and suppliers [10,22]. In this paper, we refer to any collaborative software components dedicated to SCM as SCMS. SCMS can either be integrated or synchronised with existing ES [15].

## 1.1. Organisation of the paper

Firstly the need for organisations to evaluate the support that an ES provides their SCM is established. As we could not find any decision support system (DSS) that does this, we identified requirements for such a DSS. We next investigated techniques and models used to evaluate IS, ES and information sharing in SCM, and studied how the performance of ES support given to SCM can be improved. We discuss the design, building and evaluation of this DSS which we named, the Enterprise System Evaluating Tool (ESET). Multi-methodological [60] and design science research approaches [33] were used in this research. The lessons learnt developing a tool using an explorative IS research artefact development methodology is the contribution of the current study. Qualitative methodologies are proven as a valid methodology to evaluate IS [40,85]. We conclude this paper describing contributions made to DSS by building ESET, stating implications of this study for researchers and practitioners of ES and SCM, and explaining our goals for future research, which will include a quantitative evaluation of ESET [40,47].

## 2. Is effective information transfer needed from ES for efficient SCM?

The motivation of this research is the practical problem identified in our on-field observations and literature reviewed, which indicate that the support an ES provides SCM is critical to enable each supply chain partner not only to perform adequately but strive to be optimised for competitive advantage of the whole value chain [2,12,22,57,59,71,81, 84,91]. Relatively little research has been conducted on the ES–SCM interdependence [2,12,91], although the performance of SCM is well researched [4,8,11,15,24,30,34,43,82,83] as is the performance of ES [1,2,5,22,25,46,57,59,64,71]. To better understand the process of information transfer between ES and SCM, we first describe the structure of an ES using Møller's conceptual framework [54], discuss a few different types of relationships observed between ES and SCM/SCMS and then investigate the need for ES to support SCM.

Møller elucidates that the conceptual framework of an ES (referred to as Enterprise Resource Planning — ERP systems) has four layers [54]. The foundation layer comprises a central data repository that allows information flows to and from various organisational functions [22]. The process layer provides integrated information with personalised visualisations to stakeholders [22,54]. The business analytics layer provides business intelligence to each stakeholder and facilitates decision support by aligning with SCMS and other software. As the need for organisations to share information by allowing integration and synchronisation of ES and SCM processes have become critical, later versions of ES have advanced capabilities to enable external information flows [7,54]. Hence, in many current ESs a portal layer is equipped with strong inter-organisational information transferring capabilities [10,22]. This outline allows us to visualise not only the basic structure of an organisation-wide IS designed to facilitate collaboration with external organisations but also the evolution of an ES with layer by layer additions over time.

The relationship between ES and SCM/SCMS varies from one supply chain micro-environment to another [12,19,22,53,91]. Initially organisations depended on organisation-wide information systems (such as MRP, MRPII, ERP) to generate and share information needed to manage supply chains. However with time, organisations have realised that collaborating with supply chain partners requires different configurations of information infrastructures. Therefore modern information systems catering to both organisational and SCM needs have ended with numerous configurations [22,52,53]. In some, ES and SCMS are highly “integrated”, meaning systems are combined as an integral whole. This is seen in modern vendor offerings of ES, where an SCMS component is embedded as a separate module [18,22,53]. In other configurations, ES processes are totally separate from SCMS and SCM processes. In such situations systems are said to be “synchronised”, allowing two or more systems to operate separately but share information to varying degrees harmoniously [53]. Therefore the relationships that exist between ES and SCM/SCMS to facilitate collaborative activities through business-to-business (B2B) communications are varied, needing complex information sharing solutions.

Whatever format an ES–SCM configuration takes within an organisation, these systems must effectively transfer and share needed information for the focal organisation and its participating supply chains to succeed [2,12,91]. Notwithstanding the diversity of these systems, it can be reasoned therefore that each supply chain partner will benefit by being able to measure the effectiveness of its ES in supporting SCM especially when a supply chain is first established or when the ‘information-flow equilibrium’ of a supply chain is disturbed. We consider a supply chain to be in information-flow equilibrium, if the information needed throughout the supply chain is obtained to a high degree of satisfaction of its partners, although the efficiency and effectiveness of this process may not be optimised. The information-flow equilibrium of a supply chain is absent or in a state of turbulence at many points of an organisation's life cycle: when a supply chain is first established or at the start of an organisation itself, when the strategic business focus of SCM changes within one or more organisations in the chain, when the membership of the supply chain changes, when new products or services are introduced along the supply chain, when upgrades or changes occur to a partner's ES (or other communicating information system), or when the activity level of the supply chain alters significantly due to natural or man-made reasons. Furthermore, when organisations merge, ES support for SCM should be strengthened to avoid a weaklink in the supply chain [18,28,32,78]. The above mentioned is not a comprehensive list of such situations. It is important to measure the impact of an ES on SCM before implementing an ES, during maintenance, and when an ES needs to tune-in with changing business or system environments. A tool used for this purpose therefore should not be intrusive and should be easy to use.

2.1. The quality of support given by an ES to SCM should be a criterion for software selection

The purchase of a suitable ES is vital not only for the success of an organisation but also for its SCM as it would impact on the whole supply chain [2,21,22,34,37,81,91]. Benefits of an ES that supports SCM well include, real-time collaborations; effective sharing of vast amounts of SCM relevant information that empower managers to implement timely, pre-emptive, and competitive business initiatives [81]; better facilitation of SCM processes such as scheduling, inventory control and transportation modal planning to increase distribution productivity [34]; and reduced cycle time, fast transactions and effective collaboration for internal and external business management [22,57,70,91]. Conversely, poorly selected, implemented, or used, ES can cause bottlenecks within supply chains [34,81,91]. To avoid such bottlenecks a systematic and comprehensive study to identify ES–SCM process points which share information if known, prior to the purchase of an ES, will therefore be useful.

Making a mistake in buying ES can be fatal for an organisation [67] and its supply chain [83], especially due to the huge costs involved. For example, in large Fortune 500 companies, it is estimated that ES expenditure would exceed US\$100 million and in medium sized organisation between US\$10 and US\$20 million [55]. Costs of implementing ES are mainly attributed to the cost of infrastructure, customization, time taken to implement, and consultancy costs [10,27,55]. Despite this, the benefits of ES are perceived to outweigh its costs [10,17,28,89]. We reason that a tool to assess an ES, and its ability to support SCM, prior to purchase can be therefore critical.

As most vendors develop ES following perceived best practices of a specific industry, there is an expectation for individual organisations to change business processes to suit the software [21]. Research shows that such organisational changes occur slowly [42,55] highlighting even more, the need for an assessment of an ES, and specifically its ability to support SCM practices before it is purchased [28,81,91]. Implementation of an ES is complicated as these are complex systems comprising many modules. SCMSs are even more complex and span over different platforms using many protocols. Problems are therefore magnified when integrating or synchronising inter-organisational software such as ES and SCMS [21]. As these systems co-exist in modern organisations their collaborations need to be continuously evaluated in detail [21]. Such an evaluation will also give clearer directions for customisation.

## 2.2. A tool to assess the support an ES gives SCM will be useful for the organisation during its operations

We reason that planned assessment of support given by an ES to SCM whilst it is active will ensure that operational mishaps are minimised. Although an ES may be selected carefully, various other factors can still cause ES to malfunction or fail. Such factors include, errors in configuration; demand of ES–SCMS for a broader set of skills; and attempts to minimise operational costs (for example, by employing unskilled staff) [1,14,41,61]. It is also important to manage staff buy-in and staff skill. Negative attitudes of staff can be due to possible changes to existing job role definitions, increasing task interdependencies [41], restrictions in job tasks [61], and low job satisfaction [14]. Appropriately skilled and motivated staff may be hard to find and expensive. Using a tool such as ESET, a systematic study of ES–SCM process points that share information can highlight problems which occur during operations and give management an insight to take remedial measures. Incorporating a learning module in ESET can support upskilling staff thereby motivating them to use most features.

## 2.3. A tool to assess the support an ES gives SCM will be useful when organisational changes occur

Structural business changes to business (merges, downsizing etc.), changes to the technical environment (technical upgrades, introducing new technologies etc.), and changes to economic and social environments can impact on existing IS configurations and create a state of turbulence needing systems to be re-configured, re-integrated and/or re-synchronised [18]. A re-assessment of the ES's capability to support new SCM needs will then have to be done. Supply chain participants need to continuously and dynamically adapt to sharing, transforming and communicating needed information [12,22,53,91] as missing (or slow to obtain) information will be a hindrance to business. To frequently assess an ES's support given to SCM, with a tool such as ESET, with the least intrusion possible will be very valuable in these circumstances.

We infer therefore, that effective information transfer between ES and SCMS is needed at an appropriate granularity for effective and efficient SCM. The effectiveness of information transfer should be assessed prior to purchasing an ES, whilst an organisation is in operation, and when changes occur to the supply chain equilibrium. Identifying these requirements motivated us to build an instrument to evaluate the support given from ES to SCM. We noted that this evaluation must be carried out with minimal intrusion. To design such a system we explored past literature on evaluation of IS, ES and SCM/SCMS.

## 3. Learning from evaluation of IS, ES and SCM to build ESET

Evaluation of IS has been well researched [23], and a variety of instruments developed [23,39,86]. DeLone and McLean's updated “IS Success Model” was of special interest as, in their synthesis of research on evaluating IS they updated their original model to include “service quality” [23,63], “information quality”, and “systems quality”. These contribute to “intention to use a systems and use”, and “user satisfaction”. All of these factors then lead the newly defined key performance measure, “net benefits” [23]. Net benefits (defined as benefits less costs) are regarded as an important criterion for evaluating IS-impact beyond the immediate user and occurs at the work group level, inter-organisational and industry levels, and societal level. DeLone and McLean state that it is impossible to define “net benefits” without first defining the frame of reference. Hence, it is important to decide whether net benefits are being measured from the view of the individual, organisation, industry or in a national sense. The IS Success Model is valuable in directing us to set the high level objectives of ESET.

Evaluation of an ES also involves identifying improvements that must be made to such systems to enhance the quality of decisions made, besides giving a measurement of organisational fit and net benefits that accrue from using the system [7,25]. Net benefits of ES have been measured at strategic, managerial and organisational levels [23, 70]. ES benefits can be measured in terms of the primary value-drivers identified as informate, integrate and optimise [22]. ES have also been evaluated from both financial and non-financial perspectives to capture value derived from both aspects [17,23,64,68,79]. For example, some ES evaluation models used a balanced scorecard approach [17,51,64,68] whilst others used a critical success factor approach [36,49,56,88].

Evaluation models used for SCM and SCMS also include, measuring SCM performance at strategic, tactical and operational levels [28,30] and from financial and non-financial perspectives [16]. Many SCM/ SCMS evaluation models have used various combinations of approaches, techniques and performance perspectives, such as the balanced scorecard approach combined with an analytical hierarchy process approach, at the three management levels [72].

Evaluation methods used in IS, ES and SCM were investigated, through various perspectives and at different granularity levels. These various models, although contributing in many ways, needed to be defined with more granularity for ESET. Hence, to provide this granularity we turned to the Supply Chain Council's SCOR (Supply Chain Operations Reference) Model, currently being used to evaluate SCM in many organisations [82,83].

SCOR spans from establishing an SCM strategy for the individual organisation to dealing with the more granular performance metrics and their corresponding SCM processes [11,82,83]. This detail is what is required for ESET. It is recognised that SCOR is only a guideline, that it is not comprehensive, and that it must be selectively applied to suit an organisation [82,83]. We found SCOR to comprise a fairly robust set of customisable SCM processes, performance attributes, and metrics at a granularity level suitable for the intents of ESET, yet to be used with awareness of its limitations.

It was useful to investigate the implications of using different methods to measure ES and SCM performance. However, we found that evaluating the performance of an ES in supporting SCM, was less well researched [20,81,91]. The frame of reference of the IS measurement as specified by Delone and McLean, needs to be set at the organisational level in ESET [23]. ESET's performance indicators if defined using SCOR at the operations level and aggregated to get the organisational level measurement, can address the six success factors defined by the Delone and McLean's model as well as both financial and non-financial dimensions [17,23].

## 4. Design and development of ESET

Building and evaluating IS artefacts have been carried out for many years in IS research [6,26,33,44,60,74,75,77,90]. Two well-known methodologies using this approach are the multi-methodological information systems (MMIS) research [60] and the design science research (DSR) methodologies [6,33,90]. Key objectives of this type of research are to solve complex organisational and managerial problems through designing and building IS artefacts for “utility” [6,33,60,74,90] and/or, to explore and define “truths” about IS, its frameworks or their development processes.

Building and evaluating artefacts in IS research is rooted in natural science [74,75,90], unlike the quantitative and qualitative approaches in IS research, which are based on social science research. Although theory building is not the main aim of such IS research methodologies, incorporating proven theories or frameworks in the artefact's design is considered important [90]. The evaluation methodology used must justify the utility of an artefact built for a pre-defined purpose. Hence, methods involving explorative evaluation are often preferred over quantitative methods in evaluating a newly built IS artefact [40,82]. Guided by these principles, and using the General Systems Theory (GST) as a basis [13], we built ESET for the key purpose of evaluating support given by an ES to SCM, and validated the artefact further by using a qualitative approach. GST was used in ESET, to identify the inputs, generate outputs and feedback.

Considering the requirements elucidated above from past literature and field observations carried out in six organisations, we derived the high level requirements of ESET (Table 1 — key objectives). The focus of ESET is to identify the organisation's SCM strategy first, and then methodically explore existing, and non-existing but required, links between SCM and ES processes. Measuring how well such support is given at each process point and then aggregating a composite highlevel measure of how well an organisation's ES supports its SCM should be provided by ESET. Generating business analytics to explain and diagnose weak process support points, will enable management to select ES software or take remedial measures to enhance an ES in order to better support SCM.

ESET was designed, after investigating many versions of DSS frameworks. The first DSS framework presented by Sprague Jnr had a database management system, a model management system and a dialogue management system [66,76]. Next, Sprague and Carlson's DSS framework [77] and the extended knowledge base decision support system (KBDSS) frameworks by Klein and Methlie [44] were investigated. DSS is defined as highly interactive, computer-based information systems that use interfaces, models and solvers together with robust databases, and knowledge bases, and a knowledge engine to solve unstructured and complex problems faced by stakeholders [44]. Currently KBDSS is designed with knowledge bases that evolve with use to support users with dynamic personalised recommendations in different situations, giving content-based and collaborative user-filtering based (filtered out and filtered in) recommendations [62,65]. The foundation of ESET was based on this recommender-driven DSS framework [62]. ESET's components therefore are Users, Model/Solver base, Visualisation base, Interface, and the Data/Knowledge base (Table 2). Although the basic components still correspond to the traditional DSS frameworks described over thirty years ago, current DSS requirements and functionalities are far more advanced, in keeping with advances in technology. Therefore we have extended the traditional DSS and included a business analytics module as well as a learning module in ESET's design (Fig. 1).

Table 1  
Summarised requirements of ESET.  
(Requirements supported by literature are cited; FO — Field Observations; new concepts are requirements derived in this study).

<table><tr><td></td><td>Requirements Identified</td><td>Description</td></tr><tr><td>1</td><td>Key objectives of ESET</td><td>To facilitate capturing the SCM strategy of an organisation [82,83]To provide a composite high-level measure of ES support given to SCM [81,91]To facilitate methodically exploring links that exist between SCM and ES [82,83]To provide business analytics to diagnose weak process points in ES-SCM [FO]To design ESET for business executives&#x27; ease of use [FO]To provide diagnostics to enhance support given from ES to SCM [FO]</td></tr><tr><td>2</td><td>Key visualisation requirements</td><td>To allow management to articulate the SCM strategy [82,83, FO]To identify SCM processes needing support from ES [81,91, FO]To identify persons responsible for SCM processes needing support from ES [FO]To include an intelligent visualisation / recommendation base [87, FO]</td></tr><tr><td>3</td><td>A robust data repository is required</td><td>To store all general and organisation-specific information on, [82,83, FO]O SCM performance strategiesO SCM measurement metricsO Organisational processes that support those selected SCM strategiesO Persons responsible for specific processesAbility to store, retrieve, share and manage very large amounts of data [44,77,87]To allow an application to mine and display information proactively [65,87]</td></tr><tr><td>4</td><td>Key solvers designed to support key objectives</td><td>To calculate a high level measure for the degree of support given to SCM by an ES [81,91]To recommend SCM performance metrics corresponding to the organisation&#x27;s SCM strategies. These metrics are selected from the default knowledge base (or user-defined metrics, also included in the knowledge base) [82,83, FO]To recommend enterprise processes corresponding to SCM metrics specified in the previous section. These processes are selected from the default knowledge base (or user-defined processes in the knowledge base) [82,83, FO]To calculate the level of ES support for each SCM Metric. Input from staff is also used to calculate this measure. An aggregation of values obtained will allow the high level measure for the degree of support given to SCM by an ES to be calculated [82,83, FO]</td></tr><tr><td>5</td><td>Recommender-base is closely tied to the solver-base</td><td>A knowledge-base is needed in ESET along with corresponding solvers [new concept]To comprehensively match enterprise processes with specified SCM metricsTo give SCM-ES process specific information.To give system specific user assistance;To give content specific user assistance that supports cognitive understandingTo give recommendation for using ESET: to carry out the task at hand</td></tr><tr><td>6</td><td>User requirements</td><td>ESET needs to be an interactive, easy to use system that is also least disruptive to users. It generates appropriate visualisations and recommendations for staff carrying out diverse ESET related tasks [44,65,77,87]</td></tr><tr><td>7</td><td>Learning component</td><td>The learning component is an important module for any decision support system to minimise staff problems: incorporating a learning module in ESET can support upskilling staff and thereby motivating them to use most features [new concept, 62]</td></tr><tr><td>8</td><td>Synchronised framework</td><td>As ESET needs all these components to be synchronised to provide stakeholders with dynamic recommendations, analysed and customised for user-defined situations, we believe a Decision Support System (DSS) [43,60,73,74]-Recommender System (RS)[63,65,87] framework will provide an appropriate foundation.</td></tr></table>

## 5. Building a default knowledge base for ESET

A default knowledge base was included in ESET (Table 2), to avoid a cold start problem common in recommender systems [65]. Whilst an ES primarily deals with information management internal to the organisation, SCMS focuses on information sharing between organisations in the supply chain [15]. In our search for generalised knowledge repositories with ES–SCM linkages, we found many studies exploring information sharing between ES and SCM/SCMS at different degrees of depth [18, 28,32,78,82,83]. Of the frameworks studied, we found that the Supply Chain Operations Reference Model (SCOR) was well suited for our purposes as it had rigorous detail (Fig. 2).

SCOR is developed by the Supply Chain Council (SCC), having more than 800 members from organisations and educational institutions [80,82,83]. SCC has attempted to standardise SCM performance metrics and processes within the SCOR framework [21,38,45,48]. SCOR links four SCM factors, used in ESET: SCM processes, performance attributes of those processes, diagnostic metrics to evaluate performance attributes, and enterprise processes that impact on performance metrics [48,82,83]. The processes, performance-attributes and metrics are hierarchically organised and address both financial and non-financial perspectives [83]. Organisations participating in SCM may find it useful to adopt SCOR if they are seeking to adhere to standardised SCM processes and performance measurements that synchronise with their SCM partners [21,38].

SCM requires the management of six key business processes: plan, source, make, deliver, enable, and return, as recognised in the SCOR framework (Fig. 2) [8,82,83]. The plan process addresses issues such as balancing resources with requirements, and aligning supply chain and business plans. The source process deals with identifying suppliers, scheduling deliveries, and managing inventories. The make process handles production scheduling, quality and performance evaluations, and managing work-in-progress. The deliver process addresses selection of carriers, routing of shipments, managing warehouses, and invoicing customers. The return process is about authorising, scheduling and receiving returns, and issuing return credits. SCOR version 11.0 [83], has identified a sixth process known as enable. The enable process supports the governance of planning and execution of SCM processes [83]. It deals with establishing, maintaining and monitoring information, relationships, resources, assets, business rules, compliance and contracts of supply chain. Each key SCM process is decomposed in SCOR to level 2 and level 3 sub-processes defining tasks at detailed levels. These sub-processes deal with lower level tasks that ultimately contribute to a key SCM process. Organisations strive to achieve continuous exchange of information from the most granular low level processes by integrating or synchronising ES with SCMS.

Together with processes, the SCOR model provides a basis for documenting performance attributes of a supply chain and metrics to measure SCM performance [21,52,82,83]. These performance attributes are reliability, responsiveness, and agility (customer focused) and costs and asset management efficiency (finance and cost focused). Organisations use these key performance attributes to define and develop strategies to improve SCM effectiveness. Hence one organisation may select the strategy of becoming a low cost provider by concentrating on controlling costs and improving asset management efficiencies, whilst another may choose to compete on the basis of being reliable, responsive and agile. Therefore the importance given to each performance attribute and SCM process will vary from organisation to organisation [83].

In order to evaluate the performance of a supply chain, SCOR provides performance metrics at three levels. Each of the five performance attributes is decomposed into these three levels of diagnostic metrics to evaluate and improve supply chain performance. Level 1 metrics are known as the strategic metrics or key performance indicators (KPI). These diagnose the overall health of a supply chain. Level 2 metrics serve as diagnostics for level 1 metrics, and can be used to identify the performance and gaps in performance of a specific level 1 metric. SCOR 11.0 provides 42 level 2 metrics to effectively evaluate the management of a specific supply chain. SCC recommends that performance evaluation is done in a balanced manner by including at least one metric for each performance measure. The six main processes of SCOR and the five main performance attributes do not however match one to one. Several different sub-processes at levels 2 and 3 may contribute to one performance metric of SCOR. To understand the metric hierarchy, we have provided an example of the performance attribute reliability in Fig. 3.

The foundation of ESET was designed by extending the Sprague and Carlson (1982) framework [77] — to build a DSS framework more appropriate for today.

<table><tr><td>DSS Component</td><td>Conceptual framework of ESET</td></tr><tr><td>Users</td><td>Many stakeholders carrying out diverse tasks are catered for in ESET, with required recommendations and business analytics.</td></tr><tr><td>Model base/Solver base</td><td>The solver/model base of ESET has three meta-solver modules incorporating data mining and business analytics. A number of minor solvers assist the following three main solver modules:The Learning Module assists users to learn about ESET or relevant ES-SCM/SCMS tasks.The Recommender Module, incorporating a content-based recommender component and collaborative filtered-in and filtered-out recommender component, allows dynamic stakeholder-support to be generated when using ESET.The Business Analytics Module generates predetermined and ad-hoc business analytics</td></tr><tr><td>Visualisation base</td><td>The visualisation base of ESET contains a meta-visualisation base, with one module for each major task: customising, evaluating and providing diagnostics.Using the customising module senior managers are enabled to specify SCM business strategies and related performance attributes relevant and unique to their organisation, by selecting from the knowledge base or defining new. They will identify other junior staff who will systematically select and record all lower level SCM metrics and processes that support the SCM business strategy specific to the organisation.Using the evaluating module designated employees will rate the quality of information supplied by the ES to SCM at each process point. ESET gives guidance for such ratings to be given by identifying the data required for each SCM process. All ratings of performance metrics given by employees and all communications are recorded in the OLTP database of ESET.The diagnostics module triggers four solvers. The first solver calculates a composite high-level measure to indicate how well the ES of an organisation supports its SCM whilst the others provide further analysis. The second solver generates business analytics to identify SCM strategies and sub-goals well-supported or not well-supported by the ES. The third solver identifies business processes from which the ES effectively extracts and presents information relevant to SCM, and those that do not. The fourth solver processes ad-hoc queries.</td></tr><tr><td>Interface</td><td>Key objective of the interface design was ease of use. Using a web-server and client architecture, the interface was designed for desktop / laptop use, but can be extended to include mobile devices in the future.</td></tr><tr><td>Data/knowledge base</td><td>The extended DSS structure of ESET has a Domain Knowledge Module that stores SCM strategies, SCM metrics and related ES business processes that support SCM. Organisation specific information is also stored in this module. Information on user responsibilities and ownerships are also recorded. The Domain Knowledge Module includes a data warehouse and a knowledge base that support recommender and business analytics generation.</td></tr></table>

![](/api/attachments/69EUHTCX/fulltext/images/eeeb505bfe9249b83852b65b60049c82dcbce74f8e5039b6fc032e67a4ad2d99.jpg)  
Fig. 1. ESET was based on Sprague and Carlson's DSS framework [77], enhanced to give business recommendations and educate users.

The associations between metrics and processes are updated by the supply chain council with each revision of SCOR. This framework shows that a vast number of integral processes need to be managed in a supply chain. As the focus of ESET is to evaluate how well an ES supports SCM, the granularity provided by SCOR is well-suited for the task.

SCOR has some limitations. Although the processes may be detailed up to 4 levels, it may not cover the broad spectrum of business processes in every organisation. The detailed specifications in SCOR can be difficult for organisations to comprehend, conform with, and implement. Adapting to SCOR revisions can be expensive, complex and labour intensive. Despite these limitations, by selecting processes and performance measures as required, organisations can use the SCOR model as a guide to articulate SCM strategies and measure SCM performance [82,83].

## 5.1. Application of SCOR to ESET

Our research is motivated by the need to have a computer-aided tool to measure the support given by an ES to SCM, before, during and after implementation of ES and SCMS. In order to identify where improvements can be made, organisations must define their own SCM strategies, performance metrics and process links in ESET. The tool should also provide KPI-by-KPI analysis of the support given, thus identifying business processes and data-points from which information flows to the SCM can be improved. The SCOR model comprises a detailed analysis of the ES–SCM linkages and provides a robust set of customisable SCM processes, performance attributes, and metrics that can be utilised as a “start-up” knowledge-base in ESET. Using SCOR allows ESET to evaluate systems quality, information quality, service quality and net benefits provided by an ES to SCM conforming to DeLone and McLean's model [23] whilst providing performance measurements from many perspectives.

![](/api/attachments/69EUHTCX/fulltext/images/429dd971ca420ce910ff6a98813e1116686bbe3fed49b15c8259ef39e2a18ece.jpg)  
Fig. 2. The SCOR framework (from SCOR version 11 [83]).

Eight step procedure used by ESET.  
![](/api/attachments/69EUHTCX/fulltext/images/16bb1200ab92cd5a13f41c9982b68c91626f5accb78c4631fd6ad4bece075951.jpg)  
Fig. 3. An abstraction of a metrics hierarchy adapted from the SCOR model [83].

## 6. The implementation of ESET

The evolving prototype of ESET was built using a centralised Oracle database, an HTTP server and the 4GL “Application Express”. The default knowledge base uses data from SCOR but is customisable. An eight step procedure has been developed to apply ESET (Table 3). In steps 1 to 6 using the Customising Module, senior managers identify the organisation's SCM strategies, SCM performance attributes, key performance indicators (level 1 metrics) as well as lower level metrics and their related processes. In Step 7, when using the Evaluation Module, a questionnaire interface customised for each process is generated by ESET to facilitate the evaluation (Fig. 4).

## 7. Case study based evaluation of ESET

Two similar organisations from the same industry were selected to evaluate ESET. Both organisations, ‘ElectraHC’ and ‘EarthChem’, are very large global Fortune 100 companies engaged in ‘engineer-to-order’ in a South-East Asian country (names of the organisations were disguised conforming to ethics agreements). Although different in size, they had similar SCM strategies, SCM processes, with well-established enterprise systems from two leading vendors — SAP and Oracle corporations. The profiles of these two organisations are given in Table 4.

<table><tr><td>Step</td><td>Objective of step</td><td>Responsibility</td><td>ESET functionality</td></tr><tr><td>Step 1</td><td>To define and quantify the SCM strategy:The CEO describes the SCM organisational strategy and then relates this to SCM performance attributes. Each performance attribute is given as a percentage weighting.</td><td>CEO/Senior management team</td><td>Customising module:SCOR performance attributes from which to select and instructions to rate the attributes are displayed. The user is also prompted to specify user-defined performance attributes as required.</td></tr><tr><td>Step 2</td><td>To select KPI or level 1 SCM performance metrics:Senior management selects from 10 KPI specified in SCOR (version 10.0) adding user-defined KPI as needed.</td><td>Senior management</td><td>Customising module:Descriptions of the KPIs and instructions to select the KPIs are given. The user is also prompted to specify user-defined KPIs as required.</td></tr><tr><td>Step 3</td><td>To select level 2 SCM performance metrics:Senior management selects from 42 level 2 metrics specified in SCOR 10.0 adding user-defined level 2 metrics as needed.</td><td>Senior management</td><td>Customising module:Descriptions of the level 2 metrics and instructions to select the level 2 metrics are given. The user is also prompted to specify user-defined level 2 metrics as required.</td></tr><tr><td>Step 4</td><td>To select level 3 SCM performance metrics:Senior management selects from level 3 metrics specified in SCOR adding user-defined level 3 metrics as needed.</td><td>Senior management</td><td>Customising module:Descriptions of the level 3 metrics and instructions to select the level 3 metrics are given. The user is also prompted to specify user-defined level 3 metrics as required.</td></tr><tr><td>Step 5</td><td>To identify relevant SCM processes of the organisation:Senior management assisted by ESET identifies SCM processes.</td><td>Senior management</td><td>Customising Module:ESET will provide detailed descriptions of the 5 key SCM processes – plan, source, make, deliver and return – as well as their sub-processes.</td></tr><tr><td>Step 6</td><td>To identify personnel responsible for evaluating the ES:Persons with knowledge of SCM processes are identified.</td><td>Senior management</td><td>Customising module:ESET will prompt and assist the identification of persons responsible for each process.</td></tr><tr><td>Step 7</td><td>To rate the quality of information provided by the ES at each of the process points:The level of support provided is expressed as a percentage (where the ideal level is 100%). Accuracy of information, granularity, format and timeliness are considered.</td><td>Relevant operational staff/ES experts</td><td>Evaluating module:ESET assists operational staff by displaying a profile of each process with a description. The information inputs and outputs of the process is also given. The performance attributes it contributes to and instruction on how to rate the performance is provided.</td></tr><tr><td>Step 8</td><td>To provide an overall measure of support given by the ES to SCM:Solvers provide various business analytics.</td><td>Diagnostic module</td><td>Diagnostic Module:Uses the solvers to calculate the required results. Drill down/consolidation features are provided in ESET.</td></tr><tr><td colspan="4">Evaluating ES support for Supply Chain Process sS3.5: Verify product</td></tr><tr><td colspan="4">SC process sS3.5 determines whether the product delivered by a supplier confirms to requirements.</td></tr><tr><td colspan="4">Performance attributes affected: (Please note: you may add or remove Performance Attributes as required)</td></tr><tr><td>Performance Attribute</td><td>Metric</td><td>Recommendations</td><td></td></tr><tr><td>Supply Chain Reliability (RL)</td><td>% Order/lines received with correct content % Orders/ lines received defect free</td><td>Calculate please - support given below</td><td rowspan="5">According to SCOR version 10.0 this process affects three performance attributes</td></tr><tr><td>Supply Chain Responsiveness (RS)</td><td>Verify product life cycle time</td><td>Calculate please - support given below</td></tr><tr><td>Supply Chain Agility (AG)</td><td>Not Applicable</td><td>You may add this if needed</td></tr><tr><td>Supply Chain Costs (CO)</td><td>Cost to verify product</td><td>Calculate please - support given below</td></tr><tr><td>Supply Chain Asset Management (AM)</td><td>Not Applicable</td><td>You may add this if needed</td></tr><tr><td colspan="4">Evaluating Instructions: (Please note: you may add or remove rating criteria as required)</td></tr><tr><td colspan="4">Rate the support given by the ES to each of the Performance Attributes on a scale of 1 to 10 by considering the rating criteriagiven below (0 indicates no support from the ES and 10 indicates perfect support)</td></tr><tr><td>Performance Attribute</td><td>Rating Criteria Recommendation: You may add or remove rating criteria for each performance attribute evaluated, as needed.</td><td>Rating Scale: 0 (Low) to 10 (High)</td><td></td></tr><tr><td>RL</td><td>Does the ES inform you what items and quantities each consignment should contain? Does the ES provide you with instructions on how to check the quality of the items? (for example: inspection logic; test sample size etc.). Does the ES allow you to record the results of the inspection and the quantities that were defective? Add other criteria if needed...</td><td></td><td></td></tr><tr><td>RS</td><td>Does the ES inform you when to expect consignments from suppliers? Is the ES integrated with the suppliers' information systems to enable deliveries to be planned? (for example, to minimize queries at the inspection location) Add other criteria if needed...</td><td></td><td></td></tr><tr><td>CO</td><td>Does the ES provide information to plan inspections? (for example, testing equipment, facilities, materials and staffing to minimize inspection-time) Does the ES allow use of time saving technologies? (for example, RFID or bar coding)</td><td></td><td></td></tr></table>

Fig. 4. Sample ESET screen to evaluate ES support for SCM processes

## 7.1. A pilot evaluation using a case-based approach

Continuous evaluation and adaptation of an artefact must be done iteratively in DSR [33]. The objective of this pilot study was therefore to identify possible enhancements needed in ESET. It was important to use two organisations having similar processes to carry out this study, to establish a strong foundation for the tool. A quantitative evaluation, can later follow by applying it in many organisations.

The SCM processes of both organisations are similar. These are, plan: process customer orders, prepare project plans; source: order raw materials, order technician supplies, and manage raw materials; make: manage production and execute product inspections; and deliver: ship items and install. Neither organisation considered returns as a valuable SCM process. They were confident that guarantees given will be safe and will not incur any costs as returns were a rare exception, rather than a rule. Enable was not recognised as an SCM process at the time of this study.

## Table 4

Profiles of ElectraHC and EarthChem in 2009.

<table><tr><td></td><td>ElectraHC</td><td>EarthChem</td></tr><tr><td>Industry</td><td>Engineering, Procurement and Construction</td><td>Engineering, Procurement and Construction</td></tr><tr><td>Main products</td><td>Hydrocarbon and industrial infrastructure such as refineries, petro chemical and power plants.</td><td>Chemical processing equipment such as bio chemical plants, pressure columns, heat exchanges and reactors, industrial robotics and machining centres.</td></tr><tr><td>Revenue</td><td>3.6 trillion (US)</td><td>2 billion (US)</td></tr><tr><td>Profit</td><td>550 billion (US)</td><td>46 million (US)</td></tr><tr><td>Total approximation of full time employees</td><td>6,000</td><td>700</td></tr><tr><td>ES vendor</td><td>SAP</td><td>Oracle</td></tr><tr><td>ES implementation</td><td>August 2003</td><td>January 2008</td></tr><tr><td>ES-SCMS configuration</td><td>Synchronised</td><td>Integrated</td></tr><tr><td>ES-SCMS performance</td><td>Stable</td><td>Stable</td></tr></table>

## Results and lessons learnt

The pilot study at ElectraHC was done after we had built and populated the default database using information available from SCOR. It was possible therefore to check whether the default database was acceptable to the organisation and how well they could customise ESET for application.

• The customising process commenced with a senior manager defining the SCM business strategy. ESET assisted the manager by providing step-by-step instructions and SCOR's definitions of SCM performance attributes. In order of importance, Reliability, Cost, Asset Management, and Responsiveness were selected. Agility was not considered important.

• Once the SCM strategy was clear, the KPIs of SCM, also known in SCOR as level 1 metrics, were identified by a team of senior managers.

• ESET next guided the team to specify the key SCM subprocesses of the business and to identify staff responsible for those processes. 21 sub processes at level 3 were selected and the staff responsible for each of these processes were identified.

Thus ElectraHC found the default database acceptable, and also made the following two suggestions:

• ElectraHC observed that having to select only from SCOR metrics and processes was too restrictive, and recommended that ESET should allow defining their own. As a result ESET now has more flexibility and allows user-defined metrics and processes, not available in the default database (from SCOR), to be incorporated with ease.

• As managers using ESET during the pilot study needed guidance from the researchers, the process has been streamlined by introducing a clearly defined eight step procedure with system enabled recommendations (Table 3).

Thus the pilot study at ElectraHC contributed to the enhancement of the design and application of ESET, in keeping with expectations of DSR.

## 7.2. A case-study based evaluation of ESET at EarthChem

The enhanced version of ESET was evaluated in detail at EarthChem. We investigated EarthChem's ES and SCMS through observations, analysis of company documents, and interviews with senior management to get a better understanding of how ESET performed.

## 7.2.1. The ES of EarthChem has four subsystems

The sales and operations subsystem gives computerised support for customer management, customer order management, and order fulfilment. Having a data warehouse as its backend, it provides users with access to aggregated operational data integrated from many sources to assist with tasks. The finance and accounting subsystem supports accounting, financial control, and financial analysis functions. Comprehensive and systematic financial reports are generated by integrating business performance data. The procurement and inventory management subsystem controls purchase order management, supplier management, and warehouse management. The production management subsystem supports planning, scheduling, manufacturing and quality control (Fig. 5).

The ES has improved EarthChem's internal operations and over time, information sharing has been extended to external systems augmenting SCM processes, most of which corresponded to processes available in the default database of ESET. The SCMS generates inbound orders based on purchase orders and outbound orders based on customer orders, automatically releasing them by gathering and analysing relevant data in the ES

## 7.3. Management perceptions of the quality and usefulness of its ES

During the evaluation of ESET at EarthChem, a number of senior managers were interviewed and many anecdotal perceptions on support given by EarthChem's ES to its SCM were noted. The qualitative data thus gathered was useful and helped senior management to take a fresh look at their ES–SCM strategies. Some examples of management perceptions were:

• On supply chain reliability: “After the implementation, management felt more confident with clients as they could be provided with much richer, accurate and effective information integrated and analysed by the ES.” — Manager, Operational Excellence Team

• On supply chain responsiveness: “It would be impossible to give a service or a purchase order on-time without the new ES.” — Manager, IT Services Team

• On supply chain agility: “When data is entered in the ES instead of in spread sheets, transparency is ensured and it is automatically shared between permitted internal users and external supply chain partners, allowing everyone to react and adapt faster to any changes in the supply chain.” — Senior Executive, Customer Relationships Team

• On supply chain costs: “It is hard to say that the ES–SCM implementation provides direct financial benefits to the organisation” — Executive Cost Management Team.

• On supply chain asset management efficiency: “Inventory cannot be managed at all without the ES.” — Executive, Purchasing and Inventory Management

![](/api/attachments/69EUHTCX/fulltext/images/f9e491bd8a8cad31d7be6c7cfa54296f875ba2957c16a68d92158888142bebfc.jpg)  
Fig. 5. ES/ERP at EarthChem.

Table 5  
SCM strategy of EarthChem — applying step 1 of ESET.

<table><tr><td>Key SCM performance attributes of EarthChem</td><td>EarthChem&#x27;s % weightings for each performance attribute</td></tr><tr><td>Supply chain reliability</td><td>28</td></tr><tr><td>Supply chain responsiveness</td><td>27</td></tr><tr><td>Supply chain agility</td><td>9</td></tr><tr><td>Supply chain costs</td><td>17</td></tr><tr><td>Supply chain asset management efficiency</td><td>19</td></tr><tr><td></td><td>100</td></tr></table>

## 7.4. Application of ESET in EarthChem

EarthChem had never developed, had access to, or used any tool to quantify and evaluate the impact ES had on SCM performance, although many agreed on the importance of such an evaluation. ESET was applied with the commitment of top management, once they understood the workings of ESET and realised that ESET could, within a short timeframe, generate measurements beneficial to the organisation.

In applying ESET at EarthChem the eight step procedure (see Table 3) was followed. In step 1, the senior executives defined the SCM strategy of the organisation using only the performance attributes available in ESET (from the default knowledge base). Supply chain reliability and responsiveness were the most important attributes reflecting management's perceptions (see Table 5).

In the next three steps (2, 3, and 4) senior managers selected level 1 metrics (KPIs) and their associated level 2 and 3 metrics. This selection process was facilitated by ESET displaying the hierarchically arranged performance metrics for the three levels, sourced from the default knowledge base.

Making use of a feature of ESET that allows the addition of userdefined metrics, the managers added customer satisfaction as a KPI, a user-defined level two metric (UDRL.2.1). They also specified submetrics of UDRL.2.1 and identified the relationship of each specified sub-metric with relevant SCM sub-processes. In step 5, the management team identified SCM processes at levels 1, 2, and 3. A total of 19 processes at level 3 were considered important (Fig. 6). The team also identified operational staff with the best knowledge of the information inputs and outputs at each of these process-points (Step 6).

In step 7 operational staff selected in the previous step, rated the quality of information supplied by the ES at each identified process-points. SCM processes affect performance attributes in different ways. For example, the evaluation screen presented by ESET for sS3.5 (Fig. 4) “verify product/execute quality inspection” shows that this process affects only three of the five performance attributes: reliability, responsiveness, and cost. Lower level metrics supported by sS3.5 for reliability are “% Orders/ lines received with correct content” and “% Orders/lines received defect free”; for responsiveness it is, “Verify product cycle time”; and for costs it is, “Cost to verify product”.

The lower section of the screen (in Fig. 7) prompts the evaluator to consider whether the ES gives sufficient information at the process point to support these lower level supply chain metrics. The “rating criteria” column displayed on the screen informs the evaluator of what metrics must be considered by displaying this information in an easy to comprehend question format. The evaluator is thus enabled to rate the ES support given to specified SCM performance attributes at each process point. If the quality of information provided by the ES at a process point was helpful to SCM, a high rating was given by the evaluators. Once all the data is gathered ESET produces the business analytics required.

![](/api/attachments/69EUHTCX/fulltext/images/23aa44306cccea75ba407a22d2fdf256f1d4bb3e4958dfa4eb32387298f7a597.jpg)  
Fig. 6. SCM processes of EarthChem.

## 7.5. Diagnostics provided by ESET in EarthChem

The most important measurement provided by ESET is the overall indicator of ES support given to SCM. In the study done at EarthChem this was 61.68%. This means that the ES supports SCM to a reasonable degree but can be improved. Had the ES supported the SCM perfectly, this indicator would have been 100%. Next, an analysis of ES support given to SCM by performance attribute was displayed on request. A solver in ESET analysed the level of support given by EarthChem's ES to SCM by aggregating the ratings given for each performance attribute across all process points (Table 6). Asset management efficiency and reliability were the two performance attributes best supported by the ES. None of the key processes selected by the senior managers had any effect on agility. This is consistent with the SCM strategy of the senior management as reflected by a weighting of only 9% given to agility (Table 5).

Finally, a process-wise analysis of support given by the ES to SCM was displayed on request by ESET (Table 7). This information is vital to improve the overall quality of support given by an ES to SCM. Whilst only two processes received a score of 80% or higher, there were two processes that scored below 45%.

## 8. Discussion

The development and implementation of ESET, and its case study based evaluation at two Fortune 100 companies indicate that such a tool has the potential to provide managers with useful information regarding the degree of support their ES gives SCM processes. This case study based approach was especially suitable to validate the product before implementing in more organisations.

Five main learning points resulted from the evaluation of ESET. First, ESET needed to be easy to implement using the eight step procedure. This was true for the EarthChem implementation where it took approximately 10 h of staff time spread over three days to use ESET. A manager of the cost and project management team in EarthChem affirmed that “the procedures of ESET's evaluation methodology were simple and fast. It was easier to follow than most complex IS evaluation models, and the disruptions to the firm's operations minimal”. As ESET was new to the organisation, a lot of time was spent explaining “how to use ESET”. In future this can be done through a workshop supplemented by a video clip to key persons using the learning component of ESET.

Table 7  
Analysis of ES support to SCM by SCM processes in EarthChem

<table><tr><td>Process</td><td></td><td>Score</td></tr><tr><td>D 3.1</td><td>Prepare quotation for client</td><td>70.0%</td></tr><tr><td>P 2.3</td><td>Prepare project plan after client has accepted quotation</td><td>55.0%</td></tr><tr><td>D 3.3</td><td>Generate project order, commit resources</td><td>64.0%</td></tr><tr><td>S 3.1</td><td>Identify sources of raw material supplies</td><td>72.5%</td></tr><tr><td>S 3.2</td><td>Select supplier, request quote, negotiate supply terms</td><td>65.0%</td></tr><tr><td>S 3.3</td><td>Create purchase order, schedule purchase deliveries</td><td>56.7%</td></tr><tr><td>S 3.4</td><td>Receive raw materials from supplier</td><td>73.3%</td></tr><tr><td>S 3.5</td><td>Verify raw material quality</td><td>36.7%</td></tr><tr><td>S 3.6</td><td>Store raw materials</td><td>67.5%</td></tr><tr><td>M 3.1</td><td>Supply materials to production line</td><td>66.7%</td></tr><tr><td>M 3.4</td><td>Receive finished products and conduct quality control</td><td>72.5%</td></tr><tr><td>M 3.6</td><td>Store finished products</td><td>80.0%</td></tr><tr><td>D 3.4</td><td>Schedule installation</td><td>65.0%</td></tr><tr><td>D 3.6</td><td>Route shipments</td><td>60.0%</td></tr><tr><td>D 3.9</td><td>Pick products</td><td>75.0%</td></tr><tr><td>D 3.10</td><td>Pack products</td><td>80.0%</td></tr><tr><td>D 3.12</td><td>Ship products</td><td>53.3%</td></tr><tr><td>D 3.13</td><td>Receive and verify product by customer</td><td>73.3%</td></tr><tr><td>D 3.14</td><td>Install product</td><td>43.3%</td></tr></table>

Second, we observed in Step 1 of the eight step procedure that senior managers were able to define their supply chain strategy and quantify it in a meaningful manner. This confirmed that this key step in the process gave direction and provided a solid basis for the procedure.

Third, senior management of both organisations decided that one of them should be responsible for overseeing the complete evaluation process. This person ensured quality control by collecting evidence to support ratings given. The researchers have noted this as a worthy future enhancement.

Fourth, EarthChem appreciated the flexibility of ESET. The procurement manager stated that “today's organisations are varied in their form of operations and management. Thus, a fixed evaluation methodology used for every organisation may not work properly. This tool's strength is that it is flexible and we can apply it our way”. Based on these initial evaluations of the tool, it will need to be even more flexible so that new criteria can be selected/added to, in this process of evaluation at each data point.

Fifth, the business analytics provided were useful. The composite indicator of 61.68% showed that the ES had room for improvement. The drill-down diagnostics provided by ESET were particularly useful. For example, consider EarthChem's rating for process S3.5 Verify raw material quality (Table 5). A 36.7% score for S3.5 came as a surprise to management who expected a much higher score. On closer examination of the rating, managers discovered that the ES did not support any cost saving measures at quality control nor provided information to assist staff to plan raw material inspections.

## 8.1. Implications for researchers and future directions

The implications for researchers is that a tool based on accepted SCM principles can be designed, developed, and implemented to assess the impact of ES on SCM. Future research can examine other models and measures for assessing this impact. More sophisticated analytics could possibly be developed to provide fine-grained measures for ES–SCM evaluation criteria. Implementation and evaluation processes can also be investigated further to refine the Eight Step Procedure, perhaps adding more flexibility to the use of ESET and building on its strengths.

Analysis of ES support to SCM by performance attribute for EarthChem.

<table><tr><td>Performance attribute</td><td>Result</td><td>Comment</td></tr><tr><td>Reliability</td><td>73.8%</td><td>13 SCM processes contributed to this performance attribute. Before weighting with the SCM performance attribute ratings, seven processes scored 80% or higher indicating that the ES provided information of high quality at these points. Three processes scored less than 30% indicating room for improvement.</td></tr><tr><td>Responsiveness</td><td>58.0%</td><td>All SCM processes contributed to this result. Six processes scored 80% or higher whilst eight had scores of 50% or lower.</td></tr><tr><td>Agility</td><td>0.0%</td><td>None of the SCM processes identified by EarthChem contributed to agility.</td></tr><tr><td>Cost</td><td>62.0%</td><td>Results were somewhat similar to those for responsiveness. All SCM processes contributed to this result. Seven processes scored 80% or higher, whilst eight had scores of 50% or lower.</td></tr><tr><td>Asset management</td><td>78.0%</td><td>Only five of the SCM processes identified by EarthChem had any effect on this performance attribute. All processes scored between 60 and 80%.</td></tr></table>

Although qualitative assessments of ESET are useful, quantitative assessments are also needed to provide a more comprehensive evaluation of the system. A quantitative evaluation of ESET could be conducted by surveying users of ESET using previously developed instruments similar to that used by Lin and Shao [47], or by developing survey questions specific to ESET. Quantitative measures could be taken of the usefulness of the performance indicators provided by ESET. Other criteria that could be quantitatively measured are the perceived ease-of-use of ESET, and users' perceptions of how flexible and adaptable ESET is. If a quantitative analysis of these and other measures resulted in values below a threshold of say 50%, on their respective scales, then ESET could be considered ineffective.

Finally, use of ESET in a number of organisations in various industries will allow three main streams of research: to improve the development and use of ESET; to improve the ability of ES to support SCM; and to learn which configurations of ES–SCM, are most appropriate in given different situations. This will also allow data analytics on the current state of support provided by an ES to SCM, using varying criteria such as different vendor offerings and different demographics of organisations.

## 8.2. Implications for Management

The main implication for management is that ESET, in initial tests, has been useful in assessing the impact of an organisation's ES support for SCM processes. This extends the knowledge that management has at its disposal to improve the performance of its supply chain. More work needs to be done regarding some aspects of the tool to improve usability, flexibility, and ease-of application, but initial results indicate that ESET has the potential to be another tool that will help managers improve their SCM, by making information transfers from ES to SCM more effective.

## 8.3. Limitations of the research

ESET has so far been evaluated in two large well established Fortune 100 organisations. However, evaluations in a number of organisations of varying sizes and types will be needed to improve the generalizability of the tool and the usefulness of its knowledge bases. It may be possible, in future for the default knowledge base (built using the SCOR framework) to be replaced by a knowledge base that evolves in ESET with use.

## 9. Conclusions

This paper has described the design, development, implementation, and evaluation of a decision support tool (ESET) to assess the impact of an organisation's ES on its supply chain management processes. The design is based on the widely accepted DSS framework which was enhanced to incorporate a learning and a business intelligence component within its solver module. A prototype of the tool was developed with the requirements to be flexible to changing environments and needs of SCM. It was also designed to be easy to use and implement, and useful to different levels of management. ESET was implemented and evaluated in two large Fortune 100 companies. The initial evidence is that the tool and the procedures to implement the tool were useful for management in making assessments about the effectiveness of their ES in supporting SCM, and that it could be applied in practice with minimum disruptions to operations. This ease of application use is beneficial as ESET can then be applied at different points in the lifecycle of such systems. The tool was designed to measure performance at the most granular level feasible of an organisation's ES–SCM interactive points. These points of interaction can be decided flexibly in accordance with the SCM strategy specified by the organisation's senior managers. There is more work to be done in ESET. For example, useful business intelligence derived by ESET can be enhanced in future versions of the tool. It is hoped that this paper will be a catalyst for further development and research into tools such as ESET, which facilitate evaluation of other systems. There is additional work to do, but we believe this research adds value for practitioners. It may signal the beginnings of a new research stream for DSS researchers — DSS used to assess the impact of one system on another, and enhancing DSS frameworks in the future with a learning module and a BI component within its solver base.

## References

[1] H.A. Akkermans, K. van Helden, Vicious and virtuous cycles in ERP implementation: a case study of interrelations between critical success factors, European Journal of Information Systems 11 (2002) 35–46.

[2] H.A. Akkermans, P. Bogerd, E. Yücesan, L.N. van Wassenhove, The impact of ERP on supply chain management: exploratory findings from a European Delphi study, European Journal of Operational Research 146 (2) (2003) 284 301.

[3] D. Ang, T. Grifiin, J. Goodson, J. Ho, Enterprise systems education through supply chain management, Contemporary Management Research 6 (1) (2010) 3–10.

[4] B.J. Angerhofer, M.C. Angelides, A model and a performance measurement system for collaborative supply chains, Decision Support Systems 42 (2006) 283–301.

[5] A. Ansarinejad, M. Amalnick, M. Ghadamyari, S. Ansarinejad, L. Hatami-Shirkouhi, Evaluating the critical success factors in ERP implementation using fuzzy AHP approach, International Journal of Academic research 3 (1) (2011) 65–80.

[6] R. Baskerville, What design science is not, European Journal of Information Systems 17 (2008) 441–443.

[7] E.W.N. Bernroider, An analysis of ERP decision making practice and consequences for subsequent system life cycle stages, Decision Support for Global Enterprise 2 (2007) 195–206.

[8] L. Berrah, V. Clivillè, Towards an aggregation performance measurement system model in a supply chain context, Computers in Industry 58 (2007) 709–719.

[9] V. Bhardwaj, M. Eickman, R.C. Runyan, A case study on the internationalization process of a ‘born-global’ fashion retailer, The International Review of Retail, Distribution and Consumer Research 21 (3) (2011) 293–301

[10] P.J. Bhattacharya, P.B. Seddon, Role of enterprise systems in business transformations: a management perspective, Proceedings of the 10th Australasian Conference on Information Systems (ACIS) Melbourne 2009, pp. 278–289.

[11] P. Bolstorff, “How does SCOR measure up” Supply Chain Technology News, March 2002.

[12] I. Bose R. Pal A. Ye ERP and SCM systems integration: the case of a valve manufacturer in China, Information & Management 45 (2008) 233–241.

[13] K. Boulding, General systems theory — the skeleton of science, Management Science 2 (3) (1956) 197–208.

[14] B.S. Butler, P.H. Gray, Reliability, mindfulness, and information systems, MIS Quarterly 30 (2)(2006) 211–224.

[15] P. Buxmann, A. von Ahsen, L.M. Díaz, K. Wolf, Usage and evaluation of supply chain management software — results of an empirical study in the European automotive industry, Information Systems Journal 14 (2004) 295–309.

[16] F.T.S. Chan, H.J. Qi, An innovative performance measurement method for supply chain management, Supply Chain Management 8 (3) (2003) 209–223.

[17] D. Chand, G. Hachey, J. Hunton, V. Owhoso, S. Vasudevan, A balanced scorecard based framework for assessing the strategic impacts of ERP systems, Computers in Industry 56 (2005) 558–572

[18] C. Chandra, S. Kumar, Enterprise architectural framework for supply-chain integration, Industrial Management & Data Systems 101 (6) (2001) 290–304.

[19] H.P. Choi, Information sharing in supply chain management: a literature review on analytical research, California Journal of Operations Management 8 (1) (2010) 110–116.

[20] T.H. Davenport, Mission Critical: Realizing the Promise of Enterprise Resource Planning Systems, Harvard Business School Press, Boston, 2000.

[21] T.H. Davenport, The coming commoditization of processes, The Harvard Business Review 83 (6) (2005) 100–108

[22] T.H. Davenport, J.D. Brooks, Enterprise systems and the supply chain, Journal of Enterprise Information Management 17 (1) (2004) 8–19.

[23] W.H. DeLone, E.R. McLean, The DeLone and McLean model of information systems success: a ten-year update, Journal of Management Information Systems 19 (4) (2003) 60–95.

[24] J.H. Foggin, J.T. Mentzer, C.L. Monroe, A supply chain diagnostic tool, International Journal of Physical Distribution & Logistics Management 34 (10) (2004) 827–855.

[25] G.G. Gable, D. Sedara, T. Chan, Enterprise systems success: a measurement model, 24th International Conference on Information Systems, Seattle, Washington 2003, pp. 576–591.

[26] R.B. Gallupe, G. DeSanctis, G.W. Dickson, The impact of computer support on group problem finding: an experimental approach, MIS Quarterly 12 (2) (1988) 276–296.

[27] Gartner, User Survey Analysis: Application Software spending 2010–2011Retrieved on 25th January 2011, from http://www.gartner.com/DisplayDocument?ref= clientFriendlyUrlandid=1528818

[28] A. Gunasekaran E.W.T. Ngai Information systems in supply chain integration and management, European Journal of Operational Research 159 (2004) 269–295.

[29] A. Gunasekaran, C. Patel, R.E. McGaughey, A framework for supply chain performance measurement, International Journal of Production Economics 87 (3) (2004) 333–347.

[30] A. Gunasekaran, C. Patel, E. Tirtiroglu, Performance measures and metrics in a supply chain environment, International Journal of Operations and Production Management 21 (1/2) (2001) 71–87.

[31] G. Gunnarsson, S. Jonsson, Charge the relationships and gain loyalty effects: turning the supply link alert to IT opportunities, European Journal of Operational Research 144 (2003) 257–269.

[32] J.E. Hernández, A.C. Lyons, R. Poler, J. Mula, J. Goncalvez, A reference architecture for the collaborative planning modelling process in multi-tier supply chain networks: a Zachman-based approach, Production Planning and Control, Special Issue (2013) 1–17.

[33] A.R. Hevner, S.T. March, J. Park, Design science in information systems research, MIS Quarterly 28 (1) (2004) 75–105.

[34] C. Ho, Measuring system performance of an ERP-based supply chain, 45(6)2007. 1255–1277.

[35] D.K.Y. Ho, T.M. Choi, Collaborative planning forecasting replenishment schemes in apparel supply chain systems: cases and research opportunities, Intelligent fashion forecasting systems: models and applications, Springer-Verlag, Heidelberg, ISBN: 978-3-642-39868-1 2014, pp. 29–40.

[36] C.P. Holland, B. Light, Critical success factors model for ERP implementation, IEEE Software 16 (3) (1999) 30–36.

[37] C.C. Hsu, K.C. Tan, V.R. Kannan, G. Keong Leong, Supply chain management practices as a mediator of the relationship between operations capability and firm performance, International Journal of Production Research 47 (3) (2009) 835–855.

[38] S.H. Huan, S.K. Sheoran, G. Wang, A review and analysis of supply chain operations reference (SCOR) model, Supply Chain Management 9 (1) (2004) 23–29.

[39] J.J. Jiang, G. Klein, Risks to different aspects of system success, Information and Management 36 (1999) 263–272.

[40] B. Kaplan, J.A. Maxwell, Qualitative research methods for evaluating computer information systems, Evaluating the organizational impact of healthcare information systems, Springer, New York 2005, pp. 30–55.

[41] D. Kang, R. Santhanam, A longitudinal field study of training practices in a collaborative application environment, Journal of Management Information Systems 20 (3) (2003) 257–281.

[42] B. Keating, T. Coltman, M. Katina, V. Baker, Unpacking the ERP investment decision: an empirical assessment of the benefits and risks, 17th European Conference on Information Systems, Verona, 2009.

[43] K.K. Kim, N.S. Umanath, B.H. Kim, An assessment of electronic information transfer in B2B supply-channel relationships Journal of Management Information Systems 22 (3) (2005) 293–320.

[44] M. Klein, L. Methlie, Knowledge-Based Decision Support System with Applications in Business, John Wiley & Sons, New York, 1995.

[45] B. Kocaoğlu, B. Gülsün, M. Tanyaş, A SCOR based approach for measuring a benchmarkable supply chain performance, Journal of Intelligent Manufacturing 24 (1) (2013) 113–132.

[46] S.A. Kronbichler, H. Ostermann, R. Staudinger, A comparison of ERP-success measurement approaches, Journal of Information Systems and Technology Management 7 (2) (2010) 281–310.

[47] W.T. Lin. B.B.M. Shao. The relationship between user participation and system success: a simultaneous contingency approach, Information and Management 37 (6) (2000) 283–295.

[48] A. Lockamy III, K. McCormack, Linking SCOR planning practices to supply chain performance: an exploratory study, International Journal of Operations and Production Management 24 (12) (2004) 1192–1218.

[49] X. Lu, L. Huang, M.S.H. Heng, Critical success factors of inter-organisational information systems — a case study of Cisco and Xiao Tong in China, Information and Management 43 (3) (2006) 395–408.

[50] J.T. Mentzer, W. DeWitt, J.S. Keebler, S. Min, N.W. Nix, C.D. Smith, Defining supply chain management, Journal of Business Logistics 22 (2) (2001) 1–25.

[51] J. Michalska, The usage of the balanced scorecard for the estimation of the enterprise's effectiveness, Journal of Materials Processing Technology (2005) 751–758 (162–163:SPEC. ISS.).

[52] P. Millet, P. Schmitt, V. Botta-Genoulaz, The SCOR model for the alignment of business processes and information systems, Enterprise Information Systems 3 (4) (2009) 393–407.

[53] V. Misra, M.I. Khan, U.K. Singh, Supply chain management systems: architecture, design and vision, Journal of Strategic Innovation and Sustainability 6 (4) (2010) 102–108.

[54] C. Møller, ERPII: a conceptual framework for next-generation enterprise systems? Journal of Enterprise Information Management 18 (4) (2005) 483–497.

[55] E.F. Monk, B.J. Wagner, Concepts in Enterprise Resource Planning, 4th ed. Thomson Course Technology, Boston, 2013.

[56] J. Motwani, R. Subramanian, P. Gopalakrishna, Critical factors for successful ERP implementation: exploratory findings from four case studies, Computers in Industry 56 (6)(2005)529–544

[57] K.E. Murphy, S.J. Simon, Intangible benefits valuation in ERP projects, Information Systems Journal 12 (4) (2002) 301-320

[58] R. Narasimhan, S.W. Kim, Effect of supply chain integration on the relationship between diversification and performance: evidence from Japanese and Korean firms, Journal of Operations Management 20 (3) (2002) 303–323.

[59] A.I. Nicolaou, Firm performance effects in relation to the implementation and use of enterprise resource planning systems, Journal of Information Systems 18 (2) (2004) 79–105.

[60] J.F. Nunamaker, M. Chen, T.D.M. Purdin, System development in information systems research, Journal of Management Information Systems 7 (3) (1990) 89–106.

[61] K. Park, A. Kusiak, Enterprise resource planning (ERP) operations support system for maintaining process integration, International Journal of Production Research 43 (19) (2005) 3959–3982.

[62] K.D.A. Peiris, R.B. Gallupe, A conceptual framework for evolving, recommender online learning systems, Decision Sciences Journal of Innovative Education 10 (3) (2012) 389–412.

[63] L.F. Pitt, R.T. Watson, C.B. Kavan, Service quality: a measure of information systems effectiveness, Management Information Systems Quarterly 19 (2) (1995) 173–187.

[64] M. Rosemann, J. Wiese, Measuring the performance of ERP software: a balanced scorecard approach, Proceedings of the 10th Australasian Conference on Information Systems 1999, pp. 773–784 (Dec.).

[65] J.B. Schafer, J. Konstan, J. Riedl, Recommender systems in e-commerce, 1st ACM Conference on Electronic Commerce, Denver, Colorado, United States 1999, pp. 03–05 (Nov ).

[66] D. Schuff, D. Paradice, F. Burnstein, D. Power, R. Sharda, Decision support (an examination of the DSS discipline), Annals of Information Systems, Springer, London, 2011, ISBN 978-1-4419-6180-8.

[67] J.E. Scott, The FoxMeyer Drugs' Bankruptcy: Was it a Failure of ERP? Americas Conference on Information Systems, 1999. 80 (August)

[68] D. Sedera, G. Gable, R. Rosemann, A balanced scorecard approach to enterprise systems performance measurement, Proceedings of the 12th Australasian Conference on Information Systems, 2001 (Dec.).

[69] D. Sedera, S. Rangaswami, P. Mallavaram, A critical evaluation of the enterprise systems success measurement models, managing modern organizations through information technology, Proceedings of the Information Resources Management Association International Conference 2005, pp. 655–659.

[70] S. Shang, P.B. Seddon, A comprehensive framework for classifying the benefits of ERP systems, Proceedings of the Americas Conference on Information Systems, AMCIS 2000, pp. 1005–1014.

[71] S. Shang, P.B. Seddon, Assessing and managing the benefits of enterprise systems: the business manager's perspective, Information Systems Journal (12) (2002) 271–299.

[72] M.K. Sharma, R. Bhagwat, An integrated BSC-AHP approach for supply chain management evaluation, Measuring Business Excellence 11 (3) (2007) 57–68.

[73] B. Shore, A.R. Venkatachalam, Evaluating the information sharing capabilities of supply chain partners, a fuzzy logic model, International Journal of Physical Distribution and Logistics Management 33 (9) (2003) 804–824.

[74] H.A. Simon, The New Science of Management Decision, Englewood Cliffs, Prentice Hall, New Jersey, 1977.

[75] H.A. Simon, The Sciences of the Artificial, 3rd ed. MIT Press, London, 1996.

[76] R.H. Sprague Jr., A framework for the development of decision support systems, Management Information Systems Quarterly 4 (4) (1980) 1–26.

[77] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[78] H. Stadtler, Supply chain management and advanced planning — basics, overview and challenges, European Journal of Operational Research 163 (3) (2005) 575-588

[79] C.I. Stefanou. A framework for the ex-ante evaluation of ERP software. European Journal of Information Systems 10 (4) (2001) 204–215

[80] G. Stewart, Supply-chain operations reference model (SCOR): the first crossindustry framework for integrated supply-chain management, Logistics Information Management 10 (2) (1997) 62–67.

[81] Y. Su, C. Yang, Why are enterprise resource planning systems indispensable to supply chain management? European Journal of Operations Research 203 (1) (2010) 81–94.

[82] Supply Chain Council, SCOR version 10.0 (2010)available at http://supply-chain.org/ f/SCOR-Overview-Web.pdf.

[83] Supply Chain Council, SCOR version 11.0 (2013)available at http://supply-chain.org/ news-scor-11-release.

[84] J.M. Tarn, D.C. Yen, M. Beaumont, Exploring the rationales of ERP and SCM integration, Industrial Management and Data Systems 102 (1) (2002) 26–34.

[85] M. Themistocleous, Z. Irani, P. Love, Evaluating the integration of supply chain information systems: a case study, European Journal of Operational Research 159 (2) (2004) 393–405.

[86] G. Torkzadeh, W.J. Doll, The development of a tool for measuring the perceived impact of information technology on work, Omega 27 (3) (1999) 327–339.

[87] T. Tran, Designing recommender systems for e-commerce: an integration approach, Proceedings of the 8th international conference on electronic commerce: the new e-commerce: innovations for conquering current barriers, obstacles and limitations to conducting successful business on the internet, Canada August ACM 2006

[88] E.J. Umble, R.R. Haft, M.M. Umble, Enterprise resource planning: implementation procedures and critical success factors, European Journal of Operational Research 146 (2)(2003) 241-257

[89] O. Velcu, Exploring the effects of ERP systems on organizational performance: evidence from Finnish companies, Industrial Management and Data Systems 107 (9)(2007)1316-1334

[90] R. Winter, Design science research in Europe, European Journal of Information Systems 17 (2008) 470–475.

[91] C. Yang, Y. Su, The relationship between benefits of ERP systems implementation and its impacts on firm performance of SCM, Journal of Enterprise Information Management 22 (6) (2009) 722–752.

K. Dharini Amitha Peiris is a lecturer at the University of Auckland. Her current research interests are in decision support systems, recommender systems, evaluation of IS, ERP and SCM systems, design science research in IS and online learning systems. She received her PhD and MPhil from the University of Auckland, NZ and her BSc (Hons) from Kingston University, Surrey, UK. She has over 15 years' experience in designing courses and lecturing in database systems, business intelligence and data mining at all levels from undergraduate stage one to executive programmes.

K. Dharini Amitha Peiris

The University of Auckland, Business School, Owen G Glenn Building, 12 Grafton Road, Auckland, New Zealand. 1142

R. Brent Gallupe is Professor of Information Systems, Director of the Queen's Executive Decision Center, and Associate Dean — Faculty at the School of Business, Queen's University at Kingston, Canada. He also holds an on-going Adjunct Visiting Professor appointment at the University of Auckland, New Zealand. His current research interests are in computer support for groups and teams, knowledge management systems, and online learning systems. His work has been published in such journals as Management Science, MIS Quarterly, Information Systems Research, Academy of Management Journal, Sloan Management Review, and Journal of Applied Psychology R. Brent Gallupe B.Math. MBA, PhD, CMA, ISP, FLMI School of Business, Goodes Hall, 346, Queen's University, Kingston, Ontario Canada K7L 3 N6 e-mail: bgallupe@business.queensu.ca

Jin Jung is a PhD candidate in the Department of Information Systems and Operations Management at the University of Auckland, New Zealand, where she received her BCom and MCom. Her current research is in the area of evaluation of IS, ERP and SCM systems, decision support systems, recommender systems and implementation methodologies. She has experiences in implementing of ERP at worldwide organisations in Europe and South-East Asia
