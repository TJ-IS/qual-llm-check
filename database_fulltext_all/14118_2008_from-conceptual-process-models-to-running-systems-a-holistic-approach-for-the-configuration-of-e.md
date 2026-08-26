---
otero_id: 14118
otero_key: "2W3CK94E"
title: "From conceptual process models to running systems: A holistic approach for the configuration of enterprise system processes"
authors: "Alexander Dreiling; Michael Rosemann; Wil M.P. van der Aalst; Wasim Sadiq"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.02.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# From conceptual process models to running systems: A holistic approach for the configuration of enterprise system processes <sup>☆</sup>

Alexander Dreiling <sup>a,d,⁎</sup>, Michael Rosemann <sup>b</sup>, Wil M.P. van der Aalst <sup>c</sup>, Wasim Sadiq <sup>d</sup>

<sup>a</sup> European Research Center for Information Systems, University of Münster, Leonardo-Campus 3, 48149 Münster, Germany <sup>b</sup> Faculty of Information Technology, Queensland University of Technology, Level 5/126 Margaret St., Brisbane QLD 4000, Australia <sup>c</sup> Department of Technology Management, Eindhoven University of Technology, PO Box 513, NL-5600 MB, Eindhoven, The Netherlands <sup>d</sup> SAP Research CEC Brisbane, SAP Australia Pty Ltd., Level 12/133 Mary St., Brisbane QLD 4000, Australia

Available online 23 February 2007

## Abstract

This paper proposes a method which aims at increasing the efficiency of enterprise system implementations. First, we argue that existing process modeling languages that feature different degrees of abstraction for different user groups exist and are used for different purposes which makes it necessary to integrate them. We describe how to do this using the meta models of the involved languages. Second, we argue that an integrated process model based on the integrated meta model needs to be configurable and elaborate on the enabling mechanisms. We introduce a business example using SAP modeling techniques to illustrate the proposed method.

© 2007 Elsevier B.V. All rights reserved.

Keywords: Information Modeling Concepts; Business Process Modeling; Reference modeling; Model configuration; System configuration

## 1. Introduction

The common presupposition of enterprise systems (ES) is that they support organizations in their operations and lead to significant efficiency gains. However, this is only true for well-implemented ES that support an organization's processes. The list of major ES project failures is long with famous examples such as FoxMeyer Drug which was allegedly driven into bankruptcy by the implementation of an ES and sued SAP for it [34]. Other examples include Mobil Europe and Dow Chemical both of which spent hundreds of millions of US\$ for their ES implementations [11].

The difficulties arise from the gap between the generic character of an ES and the non-generic, individual character of an organization. Within academia this development is reflected by a constantly growing body of literature on configuration [1,7,11,15,18,26,33] emphasizing that information systems are typically not implemented in an organizational context but adapted to organizational needs from ‘off-the-shelf’ packages. Major ES vendors similarly aim at tackling this problem by including an increasing amount of adaptation mechanisms into their packages in order to support the configuration process within organizations.

This paper introduces a method which targets increased usability of conceptual modeling for the purpose of ES configuration as conceptual modeling is underutilized in this context [38]. One of the reasons for this is that modeling is often seen to be a tool for documentation purposes only and as such not perceived as a valueadding tool within an ES project. Also, if modeling is used for requirements engineering purposes, usually the models do not automatically impact on the software configuration which again drives the perception that modeling is an overhead. Since modeling is underutilized the question arises as to how to create an improved value proposition related to conceptual modeling as part of an ES project. This paper's approach to achieve this goal features three different aspects:

• Various perspectives of modeling: managers and technical project members have a different perspective on a business process. To meet the requirements of different user groups, alternative modeling languages have evolved. Changing established modeling languages is time consuming and may result in resistance of project members to use modeling. We therefore propose to integrate existing process modeling languages.

• Model configuration: a set of predefined conceptual models needs to be adapted to the specific requirements of an organization.

• ES configuration by means of model configuration: usually, ES software needs to be adapted to the specific requirements of an organization. Graphical, intuitive means for configuring a system, i.e., system configuration by model configuration, are only rare as of today.

The model integration we propose differs from integration concepts underlying techniques such as UML or ARIS. We propose to integrate process modeling techniques which have evolved for different stakeholders such as management or technical analysts. The next section of the paper will elaborate on this topic. Second, we propose to make the integrated languages configurable which will be the concern of the remainder of our paper. Section 3 will discuss the vertical integration of process models subsequently followed by a discussion of process configuration in general in Section 4. Section 5 contains a business example that will provide a better understanding of our approach. Finally, a short outlook will be given and future prospects will be discussed.

## 2. Perspectives in process modeling

Within the fields of Information Systems and Computer Science, numerous process modeling languages have evolved. These techniques vary in their degree of comprehensibility to certain user groups, i.e., they are of different pragmatic quality [25]. Some process modeling languages depict business processes from a highlevel perspective with a focus on understanding key points of the process (for instance SAP's Collaborative Business Scenarios). In these cases an intuitive comprehensiveness for a large number of users with typically limited modeling experiences is more important than a high expressive power and detailed descriptions of a process. Other modeling techniques describe a business process with the purpose of executing the process automatically (workflow languages). Such techniques demand high rigor and express details, but are often only used by a limited number of experienced modelers.

We distinguish between the three perspectives: management, business process analyst, and technical analyst, and discuss them in more detail. This framework follows the commonly accepted distinction between managerial and non-managerial work on the one hand [47], and between business and IT on the other hand. Furthermore, this framework appropriately reflects the nature of ES projects, where the main involved parties are an organization's management, functional departments, its IT department, and external implementation partners. The management perspective allows for communicating process models as description of ES processes and functionality to management. The business process analyst perspective enables implementation partners and organizational actors from functional departments to communicate about the aspired functionality of the ES. Finally, the technical analyst perspective allows for specifying business processes in a format that can be processed by IT. These models can be used as a communication tool between IT departments and implementation partners. The remainder of this section will be concerned with discussing these three perspectives in more detail and motivating why they are important in the context of ES configuration.

## 2.1. Management perspective

The management perspective on a business process needs to provide a quick and intuitive overview of the business processes of an organization including related inter-organizational business processes. Management is responsible for many or even the entire set of business processes. Therefore, managers have to be aware of how business processes are executed within an organization, in detail. Nevertheless, due to the significant amount of business processes and their complexity, especially in large organizations, it is unavoidable to maintain a certain level of abstraction within the management perspective.

Business process frameworks as the highest level of an enterprise-wide model, provide a glance at the entire set of business processes within an organization. They provide an intuitive starting point for studying the entirety of an organization's business processes. Several of these frameworks have been developed as entry points into rich reference models. For instance, the CIM-Y framework developed by Scheer is comprised of business processes for manufacturers with the two main processes order management and product lifecycle management [31]. Retail-H, as another example, depicts the business processes involved in retailing [4,27]. The H-shaped framework includes all processes from procurement, over warehousing, to sales for operatively conducting retail. As a final example, the enhanced Telecom Operations Map (eTOM) is a business process framework of an ‘ideally operating’ telecommunication company [39].

Several ES software providers have included modeling techniques for process frameworks into their products. SAP, for example, currently provides so-called Solution Maps (SM) and Collaborative Business Scenarios (CBS) as reference models for their support of certain industries such as Automotive, Chemicals, or Retail or cross-industry concepts such as Customer Relationship Management, Supply Chain Management, or Enterprise Resource Planning.

## 2.2. Business process analyst perspective

The business process analyst perspective is located ‘between’ the rather high-level management perspective and the detailed perspective of a technical analyst. Unlike the two other perspectives, the business process analyst faces a variety of purposes when it comes to modeling. This includes business process documentation, process improvement, risk management, or knowledge management, as well as software selection, software configuration, system requirements specification, or process simulation. Consequently, this perspective demands rich and adaptable meta models. The notation of these models must be intuitively enough to support interaction with business users, who maybe modeling novices. At the same time, it must feature a degree of rigor, so that these models can form the starting point of a system or workflow development lifecycle. Several modeling languages have been developed to address the needs of this perspective. For instance, Event-driven Process Chains (EPCs) as an integrating modeling language of the process perspective within the Architecture of Integrated Information Systems (ARIS) approach [32] can be used to express business processes. EPCs have become common as software vendors such as SAP and Siebel have used them for their application-specific reference models.

## 2.3. Technical analyst perspective

The technical analyst perspective focuses on the IT support of business processes. Within this perspective, it is especially important to represent the parts of business processes that are supported by process-aware information systems such as workflow management systems.

Although workflow management (WFM) has been researched for a significant period now, with many software products available, there is no commonly accepted standard of a workflow language. Modeling standards such as Business Process Execution Language for Web Services (BPEL4WS) or Business Process Modeling Language (BPML) or notations such as Business Process Modeling Notation (BPMN) have been driven by the demand for solutions based on Web services. These standards, however, have a low level of maturity and still lack a significant uptake in practice. Recent publications and research on workflow management in general [2] or on workflow languages in particular [41] based on a rigorous analysis of workflow language requirements [43] suggest that this domain will change significantly over the next years.

Several organizations proposed workflow standards such as the WFMC (Workflow Management Coalition) [48], the RosettaNet Consortium [29], or the Supply Chain Council [37] towards workflow architectures, languages, or specific process schemas. One of the more advanced and influential workflow approaches is the so-called Yet Another Workflow Language (YAWL) approach [41,14], an open source workflow management system (www.yawl-system. com). This workflow language is based on the thoroughly researched Workflow Patterns [43]. Especially at an instance level, YAWL features several sophisticated modeling constructs to handle splits and synchronization of workflow branches.

## 3. Integration of perspectives

The existence of different process modeling languages in practice confronts an organization with two alternatives:

1. The organization can pursue the ‘conversion’ of all language users within the organization to one conceptual process modeling language.

2. The organization can accept the multiplicity of conceptual process modeling languages and build upon it.

We argue that the first option is not realistic for two main reasons: (1) it is impossible if the target language (i.e., the language to ‘convert’ to) is incapable of expressing constructs that some users have expressed in the past and that is necessary for them; (2) it is furthermore cumbersome or impracticable to achieve a single-language environment if entire language communities (such as product developers, or managers) must ‘convert,’ because they may simply resist these changes. It is plausible to assume that product developers cannot or are not willing to ‘convert’ from a rich workflow language to a high-level conceptual process modeling language that may simply be unsuitable for their purposes. It is furthermore not meaningful to confront managers having a broad area of responsibilities with detailed workflow models in order to inform them about internal processes. Hence, we propose to tolerate the co-existence of different languages and to integrate languages that express business processes at different levels of granularity. The question that arises is, of course, how this integration can be achieved?

In order to provide conceptual support for the implementation of process-aware information systems, language integration of the introduced perspectives needs to be achieved, which requires a mapping of language constructs within the perspectives as shown in Fig. 1. This framework will be populated in Section 5 of this paper when the actual integration of Collaborative Business Scenarios and Event-driven Process Chains will be explained in a business example.

Apart from the fact that all ES project members can continue to communicate with each other in the ways they are used to, one of the major advantages gained by an integration of languages of the three introduced perspectives is the impact of configuration decisions between the perspectives. If a top-down approach is chosen within an ES configuration project, e.g., switching-off an activity within the management perspective, then switching-off entire processes or process branches within the business process analyst perspective and entire workflow schemas or parts of workflow schemas within the technical analyst perspective can be done automatically. Bottom-up, integrated configuration allows for feedback mechanisms. If, e.g., a business process analyst discovers problems with the enactment of a business process after a certain process branch has been switched-off due to a configuration decision within the management perspective, he may feed back this information during the next milestone meeting to the management which potentially impacts on the original decision.

![](/api/attachments/2W3CK94E/fulltext/images/6804a0cbf4d17800c3a8ce0e51ba2cd7f4b3386b718cdf5d70b6e74ffef6aa54.jpg)  
Fig. 1. Generic language integration for the three perspectives management, business process analyst, and technical analyst.

Integrating languages featuring a different level of abstraction is naturally bound to losing information towards the more abstract information modeling languages. The difficulties of mapping constructs of languages that feature a different level of abstraction immediately become evident after an ontological examination of the languages. The Bunge–Wand–Weber (BWW) Ontology [45,46] provides a useful framework for such an ontological evaluation. Constructs from different languages belonging to the same ontological category (e.g., the BWW constructs Thing, Transformation, or State) can be mapped relatively easy at meta level. This task requires an examination of all language constructs of both languages towards their fit into the classes of the used ontology. If all constructs of both languages have been assigned exactly on ontological construct, pairs of constructs (mappings) of both languages within one class can be constructed. As an example the language construct Function of Eventdriven Process Chains (EPCs) can be mapped to the language construct Activity in a Collaborative Business Scenario (CBS) as both language constructs can be assigned to the BWW construct Transformation.

This mapping will usually lead to one-to-many relationships between the statements made in the languages rather than one-to-one relationships. In a detailed EPC model one CBS activity will usually be represented by many EPC Functions. Table 1 shows a simplified ontological analysis of SMs and CBSs within the management perspective, EPCs within the business process analyst perspective, and YAWL within the technical analyst perspective. This analysis depicts what ontological classes are supported by language constructs of the examined languages at the management, business process analyst, and technical analyst levels.

The ontological evaluation of the modeling languages is especially useful as it reveals the incapability of ‘high-level’ languages to make statements about aspects that can only be formulated with more complex languages (e.g., EPCs and YAWL). For example, the ontological concept State is not supported in the management perspective, if SMs and CBSs are used. The main reason for this ontological incompleteness is the deliberately limited meta model of those languages. If the more detailed modeling language features an ontological construct which is not supported in a less detailed modeling language the abstraction of the business process to the less detailed language will be at cost of losing expressive power. In these cases, mapping at a meta level allows for assigning a language construct of the ontological construct state to another one at management level as one-to-one or one-to-many. If, for instance, the Event within EPCs is mapped to a CBS activity at meta level, all Events within an EPC must be assigned to an Activity in a CBS. This is a clear change in the statement embedded within the EPC Events, but enables to switch-off EPC Functions and Events if a CBS activity is switched-off within the management perspective.

Evaluation of modeling languages with the base constructs of the Bunge–Wand–Weber Ontology [45]

<table><tr><td></td><td>SM, CBS</td><td>EPC $^a$ </td><td>YAWL</td></tr><tr><td>Thing</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Property</td><td>-</td><td>x</td><td>x</td></tr><tr><td>State</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Transformation</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Stable state</td><td>-</td><td>-</td><td>-</td></tr></table>

<sup>a</sup> A detailed ontological analysis of EPCs can be found in [16].

Apart from the difficulties that arise from mapping constructs which belong to different ontological classes, a closer examination of the constitutional part of processes – their control flow – and the capability of process modeling languages to depict various aspects of control flow reveals that integrating process modeling languages for different perspectives is a non-trivial task. An evaluation of the introduced languages towards their support of Workflow Patterns (Table 2) shows that more abstract process modeling languages insufficiently support control flow.

SAP's Solution Maps as the most abstract of the examined languages are completely incapable of expressing control flow. The purpose of this modeling technique is to provide a very coarse granular picture of what processes are to be supported by an ES. It is mainly used in the business blueprint phase of an ES project to decide which processes to support and for which processes no support is pursued. Control flow as a constitutional part of a process modeling language is not necessary within this language. Collaborative Business Scenarios include document flows rather than control flow. However, the document flow suggests that a function needs to have produced an output document serving as the input document for the next function, which somehow implies an order of activities. It can thus be argued that control flow is implicitly supported to a certain extend. Nevertheless, as shown in Table 2, the possibilities of CBS in terms of depicting control flow are limited. As in the case of Solution Maps, control flow is not necessarily the main focus of this modeling language.

At the business process analyst level, the possibilities of expressing control flow increase significantly. EPCs support ten of the twenty Workflow Patterns and hence six more than SMs and CBSs combined. This level of detail is required in order to communicate business processes from a business perspective. At this level, more than 1200 comparatively large EPCs used to describe the capabilities of $\mathrm { S A P ^ { \circ } s }$ product landscape up to SAP R/3 release 4.6c. This is certainly too much to serve as a tool for quickly providing an overview of $\mathrm { S A P ^ { \circ } s }$ capabilities, in a way that SMs or CBSs are intended to do. However, this level of detail is still not sufficient at the technical analyst level for two main reasons. First, in every case where any of the ten not supported Workflow Patterns is needed to describe the control flow of a certain business process, the expressional limits of EPCs are reached. Second, some of the constructs of EPCs are semantically difficult [40], which means that it remains unclear what they express. YAWL's capabilities transcend that of EPCs by supporting all Workflow Patterns with the intentional exception of one (Implicit Termination—a pattern which is typically not desirable while describing a workflow) and by being unambiguous about the meaning of its language constructs.

Table 2  
Evaluation of modelling languages with workflow patterns

<table><tr><td>Workflow pattern</td><td>SM, CBS</td><td>EPC*</td><td>YAWL*</td></tr><tr><td>Sequence</td><td>x/–**</td><td>x</td><td>x</td></tr><tr><td>Parallel split</td><td>x/–**</td><td>x</td><td>x</td></tr><tr><td>Synchronization</td><td>x/–**</td><td>x</td><td>x</td></tr><tr><td>Exclusive choice</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Simple merge</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Multi-choice</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Synchronizing merge</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Multi-merge</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Discriminator</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Arbitrary cycles</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Implicit termination</td><td>x/–**</td><td>x</td><td>-</td></tr><tr><td>Multiple instances without synchronization</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Multiple instances with a priori design time knowledge</td><td>-</td><td>x</td><td>x</td></tr><tr><td>Multiple instances with a priori runtime knowledge</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Multiple instances without a priori runtime knowledge</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Deferred choice</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Interleaved parallel routing</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Milestone</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Cancel activity</td><td>-</td><td>-</td><td>x</td></tr><tr><td>Cancel case</td><td>-</td><td>-</td><td>x</td></tr></table>

<sup>⁎</sup>Source: a detailed analysis of the supported workflow patterns of EPCs and YAWL can be found in [41]. <sup>⁎⁎</sup>Control flow in CBSs is rather depicted as document flow which technically means, that these workflow patterns are not supported. However, the document flow suggests that a function needs to have produced an output document serving as the input document for the next function, which somehow implies an order of activities.

The ontological class of each language construct and its corresponding Workflow Pattern determines which constructs can be mapped to each other while vertically integrating process modeling languages. Technically, SMs, CBSs, EPCs, and YAWL are integrated at meta level, since the meta models of the included languages are comprised of these language constructs and relationships between them.

Fig. 2 shows which models and modeling languages are assigned to what level of abstraction related to a segment of the ‘real world.’ If a model M1 expresses a part of the ‘real world’, meta model M2 is a model of language L1 that is used to express this part of the ‘real world’ [19–21,24,35]. This language-based meta model [35] is in itself expressed in a language L2. The example of Event-driven Process Chains depicts this relationship: a ‘real-world’ process (part of the ‘real world’) must be placed at the instance level. Its corresponding Eventdriven Process Chain diagram is an abstract model of this process (M1) and expressed in Event-driven Process Chain notation (L1). M2 is an abstract model of L1 and to be placed at meta level. We will use Chen's entityrelationship diagrams (ERD) [8] for expressing meta models such as M2, i.e., models of modeling languages. L2 will thus be a Chen-ERD. Whereas M1 contains the actual content of a process (e.g., functions such as ‘place order’ or events such as ‘order placed’), M2 contains modeling constructs (e.g., an entity type for ‘function and an entity type for ‘event’). Correspondingly, an instantiated metadata repository of the model M2 (language-based meta model of the actual business process) contains entities that represent functions, events, and other parts of EPCs. In other words, this metadata repository contains all information about process models. Implying that M2 contains an entity type function for expressing the EPC notation, the corresponding metadata repository contains a relation function that itself contains items such as ‘place order.’ A manipulation of this metadata repository can be conceived as one of several configuration mechanisms [5,6] and will be examined in more detail in the context of configuring vertically integrated process models below.

![](/api/attachments/2W3CK94E/fulltext/images/daf39f7e89ee228df46d0e57bdea6eb459dd8fdb7056f6986a7a09f5a6a25b1b.jpg)  
Fig. 2. Models and modeling languages on different levels of abstraction [19–21,24,35].

## 4. Process configuration

In order to continue this discussion we must make a few remarks on how we actually understand process configuration as the central topic of this contribution.

Configuration of software in order to meet requirements of organizations has been subject to academic discussion for a significant period of time as early examples suggest [15,26]. Davenport [11] describes the process of configuration as a methodology performed to allow a business to balance their IT functionality with the requirements of their business. More specifically, Soffer et al. [33] describe configuration as an alignment process of adapting the enterprise system to the needs of the enterprise. Especially, if an organization achieved competitive advantages in enacting a business process in a certain way, they usually will not wish to change this business process in order to fit into an enterprise system. In this case, the reference process within the enterprise system needs to be changed according to the ‘realworld’ business process. Soffer et al.'s approach [33] allows for implementing process variants based on the values of certain attributes. Enterprise system configuration involves setting all the usage options available in the package to reflect organizational features [11]. Brehm et al. [7] define nine different change options for enterprise systems from predefined alterations (e.g., by marking checkboxes) within the enterprise system to alterations of the program code. Holland and Light [18] argue that a critical success factor of enterprise system implementation is to avoid program code changes and wherever possible using predefined change options. Similarly, Sumner and Hamilton [36] argue that minimizing ES configuration significantly contributes to achieve turnarounds in escalated projects. This point clearly hints at insufficient means for ES configuration. In terms of model configuration Becker et al.'s approach is one of the most advanced [6]. It features several mechanisms for transforming a reference model into a build time model. Becker et al.'s approach is very generic and differs from our research in that we, first, seek generic patterns that arise during model configuration and, second, that we propose a configurable modeling language with the CEPC.

Configuration and customization are often used interchangeably. Merriam-Webster's Collegiate Dictionary [28] defines configuration as the “relative arrangement of parts or elements” whereas customizing is defined as “to build, fit, or alter according to individual specifications.” With these definitions in mind we can only perform reconfiguration (alteration of relative arrangement of parts or elements within enterprise systems) or customization (alteration of enterprise systems in order to meet the specification of the enterprise). The latter includes alterations of program code, which we do not pursue in our research. We are rather concerned with the configuration of ES and more specifically with that of ES processes. For the purpose of this paper, we define (re-)configuration of an enterprise system as the process of aligning business aspects such as functions, information, processes, or organization with generic enterprise systems in order to meet the business requirements of the enterprise in the most efficient way. For the sake of simplicity we use the term configuration instead of reconfiguration in this paper.

All of our configuration mechanisms are anchored at meta level. More specifically, we achieve configuration by manipulating a metadata repository that is an instantiation of the meta model M2 in Fig. 2. This metadata repository can easily be built as a relational database, because M2 is an entity-relationship diagram and therefore well-suited for this purpose. Using the example of Event-driven Process Chains, the metadata repository contains relations (tables in a relational database) for its language constructs such as Function or Event. Consequently, we are not deleting, e.g., a function within a process model but an entry within the ‘function’ table of a metadata repository. This configuration affects the type level (i.e., the model will be configured) because the information stored within the metadata repository is essentially information about the models. Thus, the basic configuration operators are the following:

• Accept: confirms a preconfigured model/part of the model (does not make changes to a specific part of the metadata repository)

• Delete: an object is removed from the reference model during configuration (an entity is removed from the metadata repository)

These basic operators allow for the construction of more complex operators, out of which we provide a few examples:

• Refine: deletes an object from a model and adds more than one object into which the original object is to be refined to the model (deletes an entry in the metadata repository and replaces it with several others)

• Unify: deletes a number of objects to be unified and adds one unified object to the model (deletes a set of entries in the metadata repository and replaces it with a new one)

• Change: deletes an object and adds another one to the model which represents an alternative to the original object (updates an entry in the metadata repository)

## 5. Business example

In order to illustrate the proposed configuration approach, we will now provide a short business example from the domain of Supply Chain Management (SCM). SCM focuses on design, operation, and maintenance of integrated value chains and aims at satisfying customer needs while simultaneously maximizing customer service [3,9,17]. Vendor Managed Inventory (VMI) has been recently discussed as a concept to increase supply chain efficiency and found especially useful in reacting to volatile changes in demand [13]. For our discussion we will use an SAP example outlined in Fig. 3.

The example includes an SAP Collaborative Business Scenario which is to be located within the management perspective. It shows in a very abstract way how SAP supports VMI by default. In this example the customer transfers inventory and sales data to respective vendors. In turn, vendors generate demand forecasts and plan supply and distribution of goods. They furthermore allocate trucks for deliveries and automatically generate sales orders. Customers respond with the automatic creation of corresponding purchase orders which triggers sales order processing on the vendor's side and delivery. The delivery is then received from the customer.

In our example, a company facing volatile demands wishes to engage in Vendor Managed Inventory. However, the demand forecast (CBS activity Generate Demand Forecast) should not be done by the vendor as described by SAP's reference model [30]. Rather, it shall be done in-house, because it is perceived as a competitive advantage by the company. The scenario requires for changing SAP's Collaborative Business Scenario (left side of Fig. 3) into a company-specific model (right side of Fig. 3).

The relevant segment from the vertically integrated meta model to capture the information about language aspects of Collaborative Business Scenarios is introduced in the ERM notation in Fig. 4. A CBS is comprised of (1 to n) CBS Objects (CBSO). Each object may occur in many CBSs. CBSO can be specialized disjoint and equivocally in Activity (A) and Organizational Unit (OU). Activities are performed by organizational units. Document flow connects two activities with each other denoting that an activity produces an output document which serves as an input document for the next activity.

![](/api/attachments/2W3CK94E/fulltext/images/1ba764dbda19f6be7e07f4807a6724b97bf533e408521fae6c9c14461950cdc4.jpg)  
Fig. 3. Configuration of SAP's collaborative business scenario “vendor managed inventory”. Source (left side): [30].

In order to perform configuration, as described above, we need to define relations for this segment of the meta model. These could be used to create a physical relational database schema. We use theoretically wellfounded [8,10] relational algebra expressions in order to depict how configuration can be achieved using an instantiated metadata repository. The following seven relations (R1–R7) can be defined according to the meta model segment from Fig. 4 (we have underlined key attributes and abstracted from attributes which would be necessary in a real setting such as time frame, cost, etc.). For each entity type we have to introduce one relation (R1, R2, R4, R5). Additionally, we have to introduce a relation for each relationship type (R3, R6, R7) as all relationship types represent n:m relationships.

R1: CBS = (cbsID, cbsName, cbsVersion)

R2: CBSO = (cbsoID, cbsoName, objecttype, cbsoVersion)

R3: CBScoCBSO = (cbscocbsoID, cbscocbsoName, cbscocbsoVersion)

R4: A = (aID, cbsoID, aName, aVersion)

R5: OU = (ouID, cbsID, ouName, ouVersion)

R6: AipbOU = (aipbouID, aID, ouID, aipbouName, aipbouVersion)

R7: DF = (dfID, previousAID, subsequentAID, dfName, document, dfVersion)

The configuration example introduced in Fig. 3 requires for updating the values of several elements that are included within these relations. We need to query the affected elements (Q1–Q3 expressed in relational algebra) and update the elements derived from these queries (U1–U3). In each query, we assume that a natural join will be done by attributes with exactly the same identifier.

Q1: Retrieve available information about the activities affected by the configuration: π<sub>aID,cbsoID,aName,</sub> (σ <sub>“ ”</sub>(A)⨝CBSO⨝ CBScoCBSO⨝σ<sub>cbsName=“Vendor Managed Inventory”</sub> (CBS))

![](/api/attachments/2W3CK94E/fulltext/images/417713767c1c46c876507a2a824700f14d0ffed0fadf73a916f30ee4f58de257.jpg)  
Fig. 4. Segment of the management perspective of the vertically integrated meta model.

U1: Update aVersion for the derived set of elements (changes the element from a reference element into a configured element)

Q2: Retrieve available information about the document flows affected by the configuration: π<sub>dfID,previousAID,</sub> <sub>subsequentAID,dfName,document,dfVersion</sub> (σ<sub>aName=“Generate</sub> (A)⨝DF⨝CBSO⨝CBScoCBSO⨝ σ<sub>cbsName=“Vendor Managed Inventory”</sub>(CBS))

U2: update document for the derived set of elements if necessary (changes the documents exchanged between the activities if the configuration requires it), update dfVersion for the derived set of elements (changes the element from a reference element into a configured element)

Q3: Retrieve available information about activity– organizational unit association (AipbOU): π <sub>cbsoID,aName,aVersion</sub> (σ<sub>aName=“Generate Demand Forecast”</sub> (A)⨝CBSO⨝CBScoCBSO⨝σ<sub>cbsName=“Vendor</sub> <sub>Managed Inventory”</sub>(CBS))

U3: Update ouID for the derived set of elements (changes the association from the activity “Create Demand Forecast” from the Organizational Unit “Customer/Retailer” to “Vendor”), update aipbou-Version for the derived set of elements (Changes the element from a reference element into a configured element)

The ‘version’ attributes in each relation are important to keep track of changes. Consequently, Q1–Q3 and

U1–U3 need to be extended by other queries and updating operations that change the ‘version’ attributes of the remaining four relations affected by the configuration if we assume that the right part of Fig. 3 is the final configuration result. Their construction is similar to Q1–Q3 and we omit their discussion here for simplicity reasons.

Configuration so far affected the management perspective only. Without vertical integration as proposed in the previous section the configuration steps would have to be performed again within the business process analyst perspective which quickly leads to a large overhead of modeling especially within large-scale requirements engineering projects. Moreover, the absence of vertical integration translates into an absence of model-inherent mechanisms to rigorously implement configuration decisions done at management level. The upper part of Fig. 5 thus depicts a segment of the populated framework from Fig. 1 integrating the management and business process analyst perspectives.

At management level, one CBS activity is concerned with generating the demand forecast (left upper part of Fig. 5). At business process analyst level a comparatively large Event-driven Process Chain corresponds to this activity only (right upper part of Fig. 5). It basically depicts what steps are necessary in order to transform the incoming documents for this activity into the necessary outgoing documents. In the discussion of our business example we already outlined the management decision to shift this activity to the customer side. If the models at management and business process analyst levels were integrated, then the configuration decision at management level can automatically translate into configuration decisions at business process analyst level. This is shown in the lower part of Fig. 5. At this stage, the changes at business process analyst level are changes in organizational responsibility only. This makes sense from a business process analyst perspective because the actual process is performed equivalently by another party. But we will see in the next integration step (between business process analyst and technical analyst) that these changes can as well be more far reaching.

![](/api/attachments/2W3CK94E/fulltext/images/839dc5fd457c392aab31bf030ffd193f3bf6e41a5c4b468726cdbd7fef6da775.jpg)  
Fig. 5. The configuration decision at management and business process analyst levels.

In order to retrieve the information that is affected at business process analyst level by the configuration decision at management level, we need to integrate both languages at meta level as discussed above. The right column of Fig. 6 therefore contains a possible meta model of Event-driven Process Chains.

Processes are comprised of Process Objects, which are specialized into Connectors, Events, Functions, and Organizational Units. Each specialized Process Object is linked to the others corresponding to the syntactic rules of EPCs. The middle column consists of a vertical integration layer, which links Collaborative Business Scenario to Process (i.e., an EPC). The many-to-manyrelationship accounts for the fact that a CBS will typically be refined by a set of EPCs, but that in turn some EPCs also transcend the processes outlined by a CBS. The CBS construct Activity is linked to the EPC construct Process Object. Again, the many-to-manyrelationship implies less rigor and allows for distinctively different views at the set of organizational activities by management and business process analysts. A third integration point consists of the link between the CBS construct Organizational Unit and the EPC construct Organizational Entity.

Given the introduced vertically integrated meta model, we can identify EPCs within the business process analyst perspective affected by the configuration within the management perspective (Q4). In order to perform Q4 we need two additional relations (R8, R9): P (Process) (entity type, part of the EPC meta model) and PCBSAs (P-CBS Association) (n:m relationship type, part of the integration layer between EPCs and CBS):

## R8: P=(pID, pName, pVersion)

![](/api/attachments/2W3CK94E/fulltext/images/434d18a01aeeb0117aabbcfece0e9733a41866a2b158833b885984cfd009b60f.jpg)  
Fig. 6. Segment of the management and business process analyst perspectives of the vertically integrated meta

R9: PCBSAs = (pcbsasID, cbsID, pID, pcbsasName, pcbsasVersion)

Q4: Retrieve available information about every EPC involved in the business process analyst perspective for “Vendor Managed Inventory”: π<sub>pID, pName,</sub> <sub>pVersion</sub> ( σ <sub>cbsName=“Vendor</sub> <sub>Managed</sub> <sub>Inventory”</sub> (CBS) ⨝PCBSAs⨝P)

The derived set of elements represents the set of EPCs which are affected by the configuration. In order to enable consistency between the configured CBS and the affected, not yet configured EPCs, we furthermore need to enquire about the affected set of EPC objects within these EPCs (Q5). Again, we need two new relations (R10, R11) in order to perform Q5: PO (Process Object) (entity type, part of the EPC meta model) and APOAs (A-PO Association) (n:m relationship type, part of the integration layer between EPCs and CBS):

R10: PO=(poID, poName, poVersion)

R11: APOAs=(apoasID, aID, poID, apoasName, apoasVersion)

Q5: Retrieve available information about every EPC object involved in the business process analyst perspective for the CBS activity “Generate Demand Forecast”: π<sub>poID,poName,</sub> <sub>poVersion</sub> ( σ <sub>cbsName=“Vendor Managed Inventory”</sub> ( CBS) ⨝ σ<sub>aName=“Generate Demand Forecast”</sub> (A)⨝CBSO⨝ CBScoCBSO⨝APOAs⨝PO)

Since functions are connected to organizational units in EPCs, we need the set of affected functions (according to the introduced meta model a subset of EPC objects). Assuming furthermore that a CBS organizational unit corresponds to exactly one EPC organizational entity, we can enquire about the set of EPC objects (functions connected to organizational units) which require for an update due to the configuration within the management perspective (Q6). We need four new relations to perform Q6: F (Function) (entity type, part of the EPC meta model), OE (Organizational Entity) (entity type, part of the EPC meta model), FOEAs (F-OE Association) (n:m relationship type, part of the EPC meta model) and OEOUAs (OE-OU Association) (n:m relationship type, part of the integration layer between EPCs and CBS):

R12: F = ( fID, poID, fName, fVersion)

R13: OE=(oeID, oeName, oeVersion)

R14: OEOUAs = (oeouasID, oeouasName, oeID, ouID, oeouasVersion)

R15: FOEAs = ( foeasID, fID, oeID, foeasName, foeas-Version)

Q6: Retrieve the set of EPC function–organizational entity relationships that are affected by the configuration within the management perspective: π<sub>foeasID,</sub> <sub>fID,</sub> <sub>oeID,</sub> <sub>foeasName,</sub> <sub>foeasVersion</sub> ( σ <sub>cbsName=“Vendor Managed Inventory”</sub> ( CBS) ⨝ CBScoCBSO⨝σ<sub>aName=“Generate Demand Forecast”</sub> (A)⨝CBSO⨝APOAs⨝PO⨝F⨝FOEAs⨝OE)

U6: Since U3 updated the organizational unit within the CBS after Q3, we can use the same information to update oeID for the derived set of elements (changes the association from every EPC function associated to the CBS activity “Create Demand Forecast” from the Organizational Entity “Customer/Retailer” to “Vendor”). Furthermore, update foeasVersion for the derived set of elements (changes the element from a reference element into a configured element)

After U6 we made sure that the configuration decision within the management perspective had an impact on the models within the business process analyst perspective. Similar to this example, other configuration scenarios can be specified and implemented. If, for instance, a CBS activity were to be deleted at management level, Q5 can be used to query which Functions (allegedly more than one) in an EPC correspond to this activity and these items can be marked for deletion as well.

We have described in our example so far how a business process model can be configured automatically as a result of a configuration decision at management level. Similarly, we wish to configure a model that serves as (an ideally machine understandable) technical description of a business process according to changes at business process analyst level. Fig. 7 depicts such a scenario as an extension of the already discussed example. The configuration of the initial VMI Collaborative Business Scenario and its impact on the business process analyst level has already been discussed (upper left and upper middle part of Fig. 7). In the original state, the process is handed before the CBS activity “generate demand forecast” from the customer/retailer to the vendor. At the business process analyst level this meant a change in organizational responsibility. However, at the technical analyst level, additional functionality must be provided for conditionally converting incoming business documents. Such conversion must be performed, if the documents created by the customer/ retailer cannot automatically be processed by the vendor's ES. After configuring the Collaborative Business Scenario as a result of a management decision and the corresponding configuration of the EPC at business process analyst level, an integrated YAWL diagram can also be adapted in order to account for the changes (lower right part of Fig. 7). After its automatic configuration the YAWL diagram will no longer include the initial document conversion step, because the process at this stage is no longer handed over before this part of the process from the customer/retailer to the vendor. However, at the end of the YAWL diagram corresponding to the CBS activity “generate demand forecast,” a conditional document conversion step must be included, because after configuration the process will be handed over from one party to another after the process has been executed according to the YAWL diagram.

![](/api/attachments/2W3CK94E/fulltext/images/44711b2aba2b988df4cf465ae4cd7c65bca62222f2f21be28dfaa60d2c051cfc.jpg)  
Fig. 7. The configuration decision at management, business process analyst, and technical analyst levels.

In a real-world ES project a preliminary business blueprint phase is concerned with decisions at management level (such as those which lead to CBS configuration). However, before the actual ES can be configured for using it to assist daily operations, a business analysis phase must be undertaken in order to determine the exact requirements that the ES must meet after it will ‘go live.’ As part of this phase the business process models describing ES capabilities will be configured if the generic description of the model does not fit the specific organizational requirements. With respect to the topic of this paper two major developments can be distinguished in this phase:

1. The business process models that were initially used to describe ES capabilities from a business process analyst perspective have been changed in patterns that were predefined by the ES vendor. Such configuration takes place if a vendor builds in choices that can be made at configuration time (e.g., which retail type must be supported, what type of warehouses is necessary, etc.). In this case an integration layer between the business process analyst and technical analyst perspectives that is built similarly to the one that we discussed above between the management and the business process analyst perspectives can take care of an automatic configuration of models at the technical analyst level as shown in Fig. 7.

2. The business process models that were initially used to describe ES capabilities from a business process analyst perspective have been changed to an extent that the integration layer between the business process analyst and technical analyst perspectives is not able to handle automatic configuration of models at technical analyst level anymore. Given the complexity of models at the business process analyst and technical analyst perspectives and, generically speaking, the variety of means of describing business processes from these perspectives, this is not unlikely to occur. In these cases we have included support for re-generating models from the technical analyst perspective in order to enable consistency between the layers.

Because the second case is realistic given the individuality of specific organizations and the generality of ES, it requires more attention. EPCs are useful for the purpose of communicating a process between business process analysts, but they are unsuitable as a description of a process from the technical analysis perspective. More specifically, EPCs cannot be used at the technical analyst level anymore as a result of their informal semantics [22]. It has been pointed out that many constructs are ambiguous [42,12,23]. In [23] an attempt is made to provide a suitable semantics to the so-called XOR and OR joins. Although this is possible, in real life applications humans tend to interpret EPCs in a less precise manner. Therefore, approaches such as the one in [12] have been proposed to migrate an informal EPC into an executable model.

However, before transforming a model at the business process analyst level (e.g., an EPC) to the technical analyst level, it is important to assess the correctness of the EPC. The so-called ProM framework is an open source tool that provides support for this task (www. processmining.org) and other tasks such as discovering processes based on event logs (e.g., the transaction logs or audit trails of an information system). The discovered model can be represented in a variety of languages (including EPCs) and consequently be exported to YAWL. ProM also allows for conformance checking, i.e., comparing a process model or process configuration with the actual behavior as registered by the information system. Clearly, these functionalities are very useful for the suggested transition of models at the business process analyst level to models at the technical analyst level in cases where configuration at the business process analyst level exceeds predefined configuration patterns. Fig. 8 shows a screenshot of ProM while analyzing the initial EPC (before configuration). As the figure shows, the EPC contains no errors. ProM uses an algorithm that is able to deal with multiple interpretations of an EPC [44]. However, in this case the model is unambiguous. Therefore, no further refinements are necessary.

ProM is also able to transform a correct EPC into a YAWL specification as shown in Fig. 9. Clearly, the mapping of EPCs onto YAWL does not add any information, i.e., technically related information needs to be added later. ProM only generates an initial model. However, this model can be executed immediately by the YAWL engine.

![](/api/attachments/2W3CK94E/fulltext/images/01141a2d843a9b4e1c449f0c1141911a93cff47c4497b9f81f96e329c38ce43a.jpg)  
Fig. 8. Screenshot of ProM while analyzing the EPC shown in Fig. 7.

Fig. 10 shows a screenshot of the YAWL work-list handler while executing three process instances (cases) according to the configured process model. Each of the three cases is in the state where the inventory and sales data have been transferred and the three subsequent steps are enabled (i.e., 9 work items are waiting to be processed).

In this section, we discussed a concrete example involving three modeling techniques each of which depicts a single business process from three different perspectives: management, business process analyst, and technical analyst. We suggested integrating these three languages by means of integrating their language constructs at meta level. We discussed how we can create impact of configuration decisions at one level on models at another level. We introduced relational algebra expressions that can be used to retrieve relevant constructs of models impacted by configuration decisions at another level. We also discussed that in cases where configuration escapes the suggested integration layer by means of metadata links other mechanisms are necessary such as the transformation of EPC models to a concrete workflow management system (YAWL) and showed that there is concrete tool support. ProM is able to generate a YAWL model based on an EPC and this model can immediately be executed in the YAWL environment. Note that in reality, however, more technical aspects need to be added (e.g., location of data, application integration, transactional properties, etc.).

## 6. Limitations of the approach

There are several factors that limit our approach and therefore need to be discussed. First and foremost, our propositions necessarily increase the modeling effort that typically is already large in ES projects. We do not target this issue directly in this paper but work on contributions to overcome this problem in related projects. It must be clear that our approach is only intended to be applicable in scenarios where conceptual models are bound to process execution of an ES. Only in these cases an increased modeling effort is justifiable. Furthermore, we investigate the problem of “modeling in the large” in a related project (funded by the Australian Government and SAP Research) in order to better understand the problems that result from large modeling projects and to deliver value propositions for managing such projects.

Another problem we need to address in further research is related to the integration layers between the management, business analyst, and technical analyst layers. The problem results from using established modeling languages and integrating them instead of

![](/api/attachments/2W3CK94E/fulltext/images/3bc4cf174dafd2dab5445a5bfd3bb1ca49d6228ae117eb43bd83874f4b73eb2d.jpg)  
Fig. 9. Screenshot of ProM while transforming the EPC into a YAWL model.

starting from the scratch with a one-language or integrated-language environment for ES projects. We typically map a language construct of one language with a similar language construct of another language at a different level with a many-to-many relationship. Again, this becomes necessary because the involved languages have been developed with different purposes in mind and for different user groups. They therefore depict entirely different parts of identical processes with entirely different semantics. Therefore, deleting an item in one model does not lead to an automatic deletion of corresponding items in a model on another level. Nevertheless, the approach helps in identifying items and marking them for deletion subject to discussion on another level. If deletion is impossible, then a feedback mechanism is gained which informs respective actors.

![](/api/attachments/2W3CK94E/fulltext/images/19e00f216b0624a8c26138212188e53898d3b2fea66e6f4e272c4dadd4bd89d5.jpg)  
Fig. 10. Screenshot of the YAWL work-list handler while executing the model depicted in Fig. 7 (YAWL model in lower right part) after the configuration decision.

A third limitation addresses the used modeling languages. We picked common and well-established languages for integrating them. Other languages on the introduced levels might be suited as well or even better suited for the task that we performed. We do not claim to have found the best possible integration scenario. We rather argued that such vertical integration is necessary and showed conceptually that it is possible and how it can be achieved.

## 7. Conclusions and outlook

Configuration is one of the most resource-consuming ES implementation phases, with considerable space for improvement. Our approach targets an increased efficiency of ES configuration by vertically integrating existing process modeling languages that have evolved for providing process information to different user groups. We argued that vertically integrated models need to be configurable and introduced an approach for such configurations. Both integration and configurability become necessary because configuration can be undertaken at management, business process analyst, and technical analyst levels and configuration should not be undertaken redundantly. We introduced a business example which outlines our approach. Together with the vision that comprehensive ES software fully acts according to specified process models, which is, for instance pursued with SAP's NetWeaver, our approach allows for efficiently configuring such software.

Our further work will mainly consist of two directions. First, we will work on a prototype which enables model configuration in the way we proposed it. Second, we will conduct empirical studies, for understanding which languages need to be integrated for configuring which ES packages most efficiently.

## References

[1] N. Bancroft, H. Seip, A. Sprengel, Implementing SAP R/3: How to introduce a Large System into a Large Organisation, 2nd ed., Manning Inc, Greenwich, 1998.

[2] A. Basu, A. Kumar, Research commentary: workflow management issues in e-Business, Information Systems Research 13 (1) (2002).

[3] C. Bechtel, J. Jayaram, Supply chain management: a strategic perspective, International Journal of Logistics Management 8 (1) (1997).

[4] J. Becker, R. Schütte, Handelsinformationssysteme, 2nd ed., Moderne Industrie, Landsberg (Lech), Germany, 2004.

[5] J. Becker, P. Delfmann, A. Dreiling, R. Knackstedt, D. Kuropka, Configurative process modeling — outlining an approach to increased business process model usability, 2004 IRMA International Conference, Idea Group Publishing, New Orleans, LA, 2004.

[6] J. Becker, P. Delfmann, R. Knackstedt, Konstruktion von Referenzmodellierungssprachen. Ein Ordnungsrahmen zur Spezifikation von Adaptionsmechanismen für Informationsmodelle, Wirtschaftsinformatik 46 (4) (2004).

[7] L. Brehm, A. Heinzl, M.L. Markus, Tailoring ERP systems: a spectrum of choices and their implications, 34th Hawaii Inter national Conference on System Sciences (HICSS), 2001, Hawaii.

[8] P.P. Chen, The entity-relationship model: towards a unified view of data, ACM Transactions on Database Systems 1 (1) (1976).

[9] M. Christopher, Logistics and supply chain management, Strategies for Reducing Cost and Improving Service, 2 ed., Financial Times Professional, London, 1998.

[10] E.F. Codd, A relational model of data for large shared data banks, Communications of ACM 13 (6) (1970).

[11] T.H. Davenport, Putting the enterprise into the enterprise system, Harvard Business Review 76 (4) (1998)

[12] J. Dehnert, W.M.P. van der Aalst, Bridging the gap between business models and workflow specifications, International Journal of Cooperative Information Systems 13 (3) (2004).

[13] S.M. Disney, D.R. Towill, The effect of vendor managed inventory (VMI) dynamics on the bullwhip effect in supply chains, International Journal of Production Economics 85 (2) (2003).

[14] M. Dumas, W.M.P. van der Aalst, A.H.M. ter Hofstede, Process-Aware Information Systems: Bridging People and Software through Process Technology, Wiley & Sons, New York, 2005.

[15] C.F. Gibson, C.J. Singer, A.A. Schnidman, T.H. Davenport, Strategies for making an information system fit your organization, Management Review 73 (1) (1984).

[16] P. Green, M. Rosemann, Integrated process modeling: an ontological evaluation, Information Systems 25 (3) (2000).

[17] F. Hewitt, Supply chain redesign, International Journal of Logistics Management 5 (2) (1994).

[18] C.P. Holland, B. Light, A critical success factors model for ERP implementation, IEEE Software 16 (3) (1999)

[19] R. Holten, Entwicklung von Führungsinformationssystemen. Ein methodenorientierter Ansatz, Gabler, Wiesbaden, Germany, 1999.

[20] R. Holten, Specification of management views in information warehouse projects, Information Systems 28 (7) (2003).

[21] R. Holten, A. Dreiling, J. Becker, Ontology-driven method engineering for information systems development, in: P. Green, M. Rosemann (Eds.), Business Systems Analysis with Ontologies, IDEA Group Publishing, Hershey, PA, 2005.

[22] G. Keller, M. Nüttgens, A.W. Scheer, Semantische Prozessmodellierung auf der Grundlage Ereignisgesteuerter Prozessketten (EPK), Veröffentlichungen des Instituts für Wirtschaftsinformatik, vol. 89, University of Saarland, Saarbrücken, 1992, (in German).

[23] E. Kindler, On the semantics of EPCs: a framework for resolving the vicious circle, Data and Knowledge Engineering 56 (1) (2006).

[24] A. Kleppe, J. Warmer, W. Bast, MDA Explained, Addison-Wesley, Boston, 2003.

[25] O.I. Lindland, G. Sindre, A. Sølvberg, Understanding quality in conceptual modelling, IEEE Software 11 (2) (1994).

[26] H.C. Lucas Jr., L.N. Stern, E.J. Walton, M.J. Ginzberg, Implementing packaged software, MIS Quarterly 12 (4) (1988).

[27] R. Luxem, The impact of trading digital products on retail information systems, 33rd Hawaii International Conference on System Sciences, 2000, Maui, HI.

[28] Merriam-Webster, Merriam-Webster's Collegiate Dictionary (online version available at http://www.m-w.com) (11th ed., Merriam-Webster, Springfield, MA, USA, 2003).

[29] RosettaNet, http://www.rosettanet.org (2004).

[30] SAP AG, Collaborative Business Scenario “Vendor Managed Inventory”, SAP AG, 2004.

[31] A.-W. Scheer, Wirtschaftsinformatik. Referenzmodelle für industrielle Geschäftsprozesse, 7 ed., Springer, Berlin, 1997.

[32] A.-W. Scheer, ARIS — Business Process Modeling, 3 ed., Springer, Berlin, 2000.

[33] P. Soffer, B. Golany, D. Dori, ERP modeling: a comprehensive approach, Information Systems 28 (6) (2003).

[34] T. Stein, SAP sued over R/3, InformationWeek 698 (1998).

[35] S. Strahringer, Metamodellierung als Instrument des Methodenvergleichs. Eine Evaluierung am Beispiel objektorientierter Analysemethoden, Shaker, Herzogenrath, Germany, 1996.

[36] M. Sumner, J. Hamilton, The turnaround ERP project: strategies and issues, 11th Annual Americas Conference on Information Systems (AMCIS), 2005, Omaha, NE.

[37] Supply Chain Council, Supply-Chain Operations Reference-Model. Overview of SCOR Version 5.0, Supply Chain Council, Pittsburgh, PA, 2001.

[38] H.M. Tan, The actual practice of modelling in SAP projects (Honors Thesis, Faculty of Information Technology, Queensland University of Technology, Brisbane, Australia 2004).

[39] TeleManagement Forum, NGOSS Technical Overview, Tele-Management Forum, Presentation TMFC1852, 2004.

[40] W.M.P. van der Aalst, Formalization and verification of eventdriven process chains, Information and Software Technology 41 (10) (1999).

[41] W.M.P. van der Aalst, A.H.M. ter Hofstede, YAWL: yet another workflow language, Information Systems 30 (4) (2005).

[42] W.M.P. van der Aalst, J. Desel, E. Kindler, On the semantics of EPCs: a vicious circle, in: M. Nüttgens, F.J. Rump (Eds.), Proceedings of the EPK 2002: Business Process Management using EPCs, Gesellschaft für Informatik, Trier, Germany, 2002.

[43] W.M.P. van der Aalst, A.H.M. ter Hofstede, B. Kiepuszewski, A.P. Barros, Workflow patterns, Distributed and Parallel Databases 14 (1) (2003).

[44] B.F. van Dongen, H.M.W. Verbeek, W.M.P. van der Aalst, Verification of EPCs: using reduction rules and Petri nets, Proceedings of the Conference on Advanced Information Systems Engineering (CAiSE 2005), volume 3520 of Lecture Notes in Computer Science, Springer, Berlin, 2005.

[45] Y. Wand, R. Weber, On the deep structure of information systems, Information Systems Journal 5 (3) (1995).

[46] R. Weber, Ontological Foundations of Information Systems, Coopers and Lybrand, Melbourne, Australia, 1997.

[47] R. Whitley, On the nature of managerial tasks and skills: their distinguishing characteristics and organization, Journal of Management Studies 26 (3) (1989).

[48] Workflow Management Coalition (WFMC), www.wfmc.org (2004).

![](/api/attachments/2W3CK94E/fulltext/images/4205d550bdeed005d5c77255617ebbc31c37b10e185393d9875bd88ebc81f0b4.jpg)

Dr. Alexander Dreiling is a Senior Researcher at SAP Research (CEC Brisbane, Australia). He received his MSc and PhD in Information Systems from the University of Münster in Germany. Prior to joining SAP Research he worked for the European Research Center for Information Systems in Münster, Germany and Queensland University of Technology in Brisbane, Australia. Alex is primarily

interested in conceptual modeling, in particular business process modeling, data warehousing, and business-related information systems research. His research so far led to more than 30 journal papers, conference papers, and book chapters.

![](/api/attachments/2W3CK94E/fulltext/images/8dedb365781c8d6557c7497fadb731ebec2ffee44b9be9f9157831f1acd1f953.jpg)

Dr. Michael Rosemann is a Professor for Information Systems and Co-Leader of the Business Process Management Group at Queensland University of Technology, Brisbane. His main areas of research are business process management, business process modeling, enterprise systems and ontologies. Besides more than 120 refereed papers including publications in journals such as Informa-

tion Systems, European Journal of Information Systems and IEEE Transactions on Knowledge and Data Engineering, he is the author and editor of five books. Michael is a member of the Editorial Board of six journals and a member of the ARC (Australian Research Council) College of Experts.

![](/api/attachments/2W3CK94E/fulltext/images/f85f4097f0fb9a91ebd0ae674656acf67aaa75e1829e754f8304e62759724d9e.jpg)

Dr. Wil van der Aalst is a Professor of Information Systems and head of the Information Systems department of the Technische Universiteit Eindhoven. He is also an Adjunct Professor at the Faculty of Information Technology of Queensland University of Technology. His research interests include Business Process Management, information systems, simulation, Petri nets, process models, workflow manage-

ment systems, process mining, verification techniques, enterprise resource planning systems, computer supported cooperative work, and interorganizational business processes. He published more than 200 books, journal papers, book chapters, conference papers, and reports on these topics.

![](/api/attachments/2W3CK94E/fulltext/images/e9737bda877f3580e78af0fe355e5596579de5392fe01ae492223642162bc512.jpg)

Dr. Wasim Sadiq is a Research Program Manager of Business Process Management and Semantic Interoperability (BPM and SI) research program at SAP Research (CEC Brisbane, Australia). His responsibilities include setting the research directions of SAP Research in business process management and applied semantics. He collaborates with SAP product groups and academic research partners

in exploring and investigating innovative research ideas. His main areas of research are business process modeling and simulation, business process execution infrastructures, and conceptual modeling. Wasim holds a PhD degree in Computer Science from University of Queensland, Brisbane, Australia.
