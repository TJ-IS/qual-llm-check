---
otero_id: 23019
otero_key: "7TME3AQJ"
title: "Towards the construction of workflow‐suitable conceptual modelling techniques"
authors: "A. P. Barros; A. H. M. Ter Hofstede"
year: "1998"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.1998.00042.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards the construction of workflow- suitable conceptual modelling techniques

A. P. Barros & A. H. M. ter Hofstede\*

Department of Computer Science and Electrical Engineering, The University of Queensland, Brisbane Qld 4072, Australia, email: barros@cs.uq.oz.au, and \*Cooperative Information Systems Research Centre, Queensland University of Technology, GPO Box 2434, Brisbane Qld 4001, Australia

Abstract. Despite their high-level and graphical nature, workflow specifications require a significant amount of implementation detail — for example application programming interface, database access and programming mechanisms for information flow — for a more comprehensive validation than is currently possible. This is currently recognized as a deficiency in workflow conceptualization. Although conceptual modelling techniques are available which are expressive, comprehensive and precise enough, we believe, their concepts and features are not specialized enough for workflow domains. In this paper, we offer a comparative insight into techniques which characterize different aspects and approaches of workflow specifications. These are: structured process modelling, object-oriented modelling, behavioural process modelling and business-oriented modelling. In particular, we determine gaps for workflows capturing operational business transaction processing, for example those of insurance claims, bank loans and government-related registration. For technique construction, we describe five workflow suitability principles.

Keywords: Business modelling, conceptual modelling, object-oriented analysis, workflow.

## INTRODUCTION

## Problem area

A workflow (see survey of concepts and products in the ButlerBloor Report; Makey, 1996) is an implementation model aimed at minimizing, if not eliminating altogether, the gap between business processing and computerized information systems (IS) processing. Under traditional implementation models, applications are partitioned into discrete units of functionality, with (typically) operational procedures used to describe how human and computerized actions of business processes combine to deliver certain functionalities. Over and above these, workflows allow coordinative and collaborative aspects of enterprises to be explicitly specified, thereby making it possible to integrate not only the information from multiple business processes but also the inherent information flow. Ultimately, multiorganizational value chains are facilitated through workflows.

Given the diversity of business processing and workflow types (see Georgakopoulos et al., 1995) it is not surprising that a large number of workflow specification techniques and languages, embodying different paradigms, have been proposed. In a process-centric paradigm, adopted in the most widely used Workflow Management System (WFMS) product, FlowMark (IBM), tasks form the focal points of workflow model cognition with execution constraints expressed both within tasks, for example pre- and postconditions, and across tasks, typically control flows. A document-centric paradigm, adopted in Lotus Notes (IBM) and LinkWorks (DEC), routes documents between actors. A state-centric paradigm, adopted in InConcert (XSoft), objectifies processes where workflow coordination is implicit in the process state life cycles. A speech-centric paradigm, adopted in Action Workflow (Action Technologies Inc.), structures workflows based on communication undertaken between actors.

A crucial step for the implementation of a workflow, as in traditional IS development, is its conceptual design. In accordance with the well-known Conceptualization Principle an essential understanding of a workflow should be imparted, independent of implementation (physical-structure) or representation (surface-structure) concerns. The benefit of validating conceptual specifications and detecting errors, prior to the much greater cost of doing so at the implementation level, is nowadays accepted without question. Indeed, in recognition that workflow specifications can be large and complex, accommodating the requirements of many stakeholders, support for conceptual design and validation through enactment is required as part of WFMS functionality. This is now endorsed by the Workflow Management Coalition through the process definition standard (in Interface 1). (See http://www.aiai.ed.ac.uk/WfMC/index.html for more details.)

Yet despite the availability of a plethora of conceptual modelling techniques (for an earlier collection see Olle et al., 1988), the quality of workflow conceptual modelling is still considered weak (Mohan, 1996). Certainly the field of conceptual modelling is quite mature, and the requirements for techniques are now well understood, if variously articulated. In addition to conceptualization, techniques should provide a sufficient expressive power so that a full conceptualization is in fact possible, they should be comprehensible to facilitate communication, and they should have a formal foundation which grounds their meaning. Importantly too, since a 'silver bullet' for all types of domains is considered unrealistic, techniques should be suitable for their problem domains, meaning their modelling concepts and features should reflect closely those required by the domain.

In our view, it is in the last of these aspects where the biggest deficiency in workflow conceptualization lies. The significant work which has been undertaken to improve the organizational embedding of conceptual modelling through the use of enterprise models as contexts and socio-technical frameworks (e.g. Avison & Wood-Harper, 1991) has served to improve requirements acquisition and the flexibility of analysis for different situations. Little has changed, fundamentally, in techniques still being used, such as Data Flow Diagrams, Petri net-based approaches, Statecharts and State Transition Diagrams.

## Approach

In this paper, we offer insight into areas which improve the workflow suitability of conceptual modelling techniques. Our approach is practical rather than philosophical, and it is similar in style to other efforts undertaken for conceptual modelling extensions (Wand & Weber, 1990; Mylopoulos, 1997). Against a ‘silver bullet’, our construction is aimed at the particular domain of coordinative workflows — or in more practical terminology, operational business transactions. In particular, we observe a number of properties of operational business transactions, and determine how effectively a sample set of conceptual modelling techniques appropriate for workflow specifications capture these properties.

The properties are anchored into general system properties. We state these as follows. As organizational systems or subsystems, operational business transactions work within a context, i.e. capturing their intent. Or put in a business sense, they are accountable, and are therefore grounded in organizational structure. Moreover, the vast amount of dynamic modelling experience suggests that their execution structure requires both control and data flow, and modularization (as an executable artefact as opposed to something which is used for purely presentation purposes). At the same time, they do not operate without constraint observed through quality controls such as temporal constraints, exception handling and contingency planning in their operation. And their actions are not merely internal to their domain but rather through interactions with a variety of external stakeholders such as customers, suppliers and collaborators we observe that they have an external interaction.

## Results

As a result of the analysis, we identify five workflow suitability principles. Towards static business transaction context, the Organizational Embedding Principle ‘right-orders’ the dependency between workflow and organizational models, while for a dynamic context the Scenario Validation Principle requires scenarios as units of interpretation for workflows. The Service Information Hiding Principle motivates the encapsulation of workflows into services, thereby conceptualizing external interaction with workflows. The Cognitive Sufficiency Principle requires fundamental details of execution structure and constraint to be imparted collectively by specifications. As we observe, the partial treatments of messaging, temporal constraints and human-to-computer interaction points by current techniques can be costly due to assumptions and waterfalls in specifications. The Execution Resilience Principle provides a special treatment of execution constraint, namely that related to workflow recovery.

Through this albeit incomplete and open-ended construction we provide an improved insight for the development and assessment of workflow modelling techniques. In Barros et al. (1997) and Barros & ter Hofstede (1997) we have provided empirical evidence that the principles lead to useful concepts for real-scale workflow modelling. In these papers, a real-life case study involving the land administration of road closures in Queensland is given.

The paper is organized as follows: first a survey of techniques is presented, then the workflow suitability principles are defined, and finally the paper is concluded.

## A SURVEY OF INTEGRATED CONCEPTUAL MODELLING TECHNIQUES

In this section, an insight into the capabilities of techniques to support a sound conceptualization of business transactions for workflow specifications is sought. The techniques are indicative of (i) structured process modelling, (ii) object-oriented modelling, (iii) behavioural process modelling, and (iv) business-oriented modelling.

## Structured process modelling

Structured process modelling, for example Structured Analysis and the Information Systems Analysis and Change method (ISAC), have had widespread use, providing both top-down process analysis and software design mapping. With the prevalence of database technology a number of extensions have been proposed (e.g. Yourdon, 1989; Shoval, 1991) to incorporate data modelling techniques. In particular, the data repositories identified through process modelling are used for the development of data models. We describe this as a process-centric integration strategy.

Data Flow Diagrams (DFDs), associated with Structured Analysis, are a popular — arguably the most popular — structured process modelling technique. Not surprisingly, DFD perspectives are offered by WFMS products, for example ENTIRE/Workflow (Software AG) and FloWare (Plexus) described in the ButlerBloor Report, for the higher levels of workflow analysis.

Figure 1 illustrates a process-centric integration of process and data models for a Library domain using Yourdon (1989); Entity Relationship Modelling (ERM) is used for the data modelling. The DFD models the processing of Loan Requests and Orders, viz Borrowers (an external entity) send Loan Requests (data flow) for Items to LOAN (process). A Loan (an update) is issued in Items (data store) and the Item is passed to the Borrower. When the Loaned Item is returned to LOAN, a Return is issued to the Items data store to indicate that the Item is available for loaning again. Borrowers also make Purchase Requests to the ORDER process. For this, Order Details are stored in Orders, and Item Details are stored in Items. An Order is sent to a Publisher who supplies the Ordered Item. Once supplied, the Item is updated to be Available.

DFDs are essentially static structures, expressing all possible data flow and data store interactions of processes. The aspects of process control which are important to workflows are captured through detailed process specifications. Process specifications refer to data dictionary elements which are linked to DFD and ERM components, and which provide syntactic correspondence between both. The informal nature of DFDs means that this integration is based on 'rules-of-thumb'. For example, a syntactic correspondence is required between data stores and entity types, indicated by alphabets in Fig. 1. Correspondence of relationship types, unless they are aggregated, is intuitive — for example, processes, data flows and data stores indicate relationship types as indicated by (a) and (b). The difficulty arises from the fact that DFDs, and with them their data flows and data stores, are abstract and decomposable. A given data store or data flow may have several and complex object types which are not easily corresponded with 'flat' ERM models. Some techniques such as those of Batini et al. (1992) alleviate this situation by providing mutually influential decompositions of process and data models.

Level 1 DFD  
![](/api/attachments/7TME3AQJ/fulltext/images/ebb62ebd770fc5cc87a44a294070eb82a2887f22fbd1de636bcb043c1e649de5.jpg)  
Figure 1. Process and data model integration for the Library domain in Structured Analysis.

The strength of a DFD lies in its simple and general concepts. Together with the decomposition feature, this allows an effective comprehensibility, which is useful for the early phases of analysis where the broader functionality of a system is still being determined. Simplicity and generality are particularly conducive for alignment with organizational definitions as discussed by Bansler & Bodker (1993), i.e. although DFDs lack context, they are context configurable.

For workflow modelling, however, DFDs are inadequate. As we saw, process control is implicit in detailed process specifications meaning that execution structure is hidden in pseudocode. The absence of formal semantics — an omission widely observed in most DFD techniques (see, for example, Opdahl & Sindre, 1993) — allows ambiguities and inconsistencies, thereby precluding the precision that workflow specifications require. Moreover, the expressive power of Structured English is restricted by, among other things, the loose coupling of its underlying models. This can restrict the degree to which task pre- and postconditions, typical in workflows, can be expressed. For execution constraint, temporal aspects, exception handling and process contingencies have to be ‘hard-coded’ into process specifications. DFDs permit process interaction with its environment, hence incorporating some treatment of external interaction. This only includes external event triggering with normal data flow analysis. In other words, the internal and external interactions of DFDs are very similar. As a feature of comprehensibility, more than anything else, Structured Analysis permits DFD partitioning by external events. This assists the validation of large and cumbersome DFDs.

## Object-oriented modelling

A number of WFMS products, for example LinkWorks (DEC) and InConcert (XSoft), provide a form of object-orientation for workflow specifications. One of the main advantages claimed is that objects provide a closer semblance with reality and are less prone to change than pure function-orientation. Along with static properties, objects include in their classification dynamic properties — operations, implemented as methods on classes. In keeping with tightly coupled object models, conventional Object Oriented Analysis/Design (OOA/D) techniques (Booch, 1991; Rumbaugh et al., 1991; Jacobson et al., 1992) and composed object-oriented techniques such as Universal Modeling Language (UML) advocate principally a state-centric integration of conceptual models. That is to say, object states are fundamental to the definition of object behaviour, and therefore to process (method) definition. (UML combines the techniques of Booch, Jacobson and Rumbaugh; refer to http://www.rational.com/uml for more details.)

Applied to workflows, objects can be used to model workflow resources such as documents, processes and actors. In the Integrated Object Oriented Method (IOOM) (De Antonellis & Pernici, 1995), for example, a purely state-centric approach is proposed using the office modelling concepts from the European Strategic Program for Research in Information Technology (ESPRIT) project OSSAD (Office Systems Analysis and Design Method). Object types are defined for business resources (actors, data or documents) and business processes, and roles define their permissible states and constraints. Overall workflow coordination is derived from the specification of intra-object dynamics. Clearly, in domains where object interaction is high, a higher modelling context is necessary. Process modelling and hence a process-centric integration can be useful for this. For example, DFDs are used in many OOA/D techniques, for example Shumate (1991), despite the paradigmal differences which are sometimes regarded as incompatible (Embley et al., 1995). Alternatively, other mechanisms, for example use cases (Jacobson et al., 1992), have been developed to preserve a high-level state-centric context.

A popular OOA/D technique, Object Modelling Technique (OMT) (Rumbaugh et al., 1991), incorporates both a state- and a process-centric integration strategy. It accommodates the data, process and behaviour perspectives through an object model (ERM), a function model (DFD) and a dynamic model (FSM which includes nesting), respectively. Figure 2 illustrates a state-centric model integration for the Library domain. In the object model, attributes are listed in the middle portion of the object class diagrams and methods are listed in the lower portion. Each object type has a dynamic model associated with it. The dynamic model contains a set of behaviour states as nodes. States are defined by ‘exclusive’ predicates and are orthogonal to the object type specializations (a structural classification). The edges represent state transi-

Object Model  
![](/api/attachments/7TME3AQJ/fulltext/images/38986f80c681cc4e09adb8ffdbd88312fd529e9fb53f52ad705c4cdd7e579aa5.jpg)

Dynamic Model (for item)  
![](/api/attachments/7TME3AQJ/fulltext/images/15f29e5b502e287ebd2355ddf38550858d5754ebb616d6d81dba227b26bda11b.jpg)  
Figure 2. Object and dynamic model integration for the Library domain in OMT.

© 1998 Blackwell Science Ltd, Information Systems Journal 8, 313–337 tions. A state transition embodies an event which triggers an action if a condition (optional) is satisfied.

Figure 3 illustrates a process-centric integration of the function and object models for the Library domain. For consistency, the function model's leaf processes and object class methods should correspond. This is not straightforward since a single leaf process may involve more than one object type. Clearly the principal object type referred to in OMT as the target needs to be identified. Targets are contained in data flows, data stores and actors (represented by a DFD's external entity symbol). OMT suggests as a guideline that a target be identified by determining a 'client–server' relationship between the object types. That is, an object type is a target if it invokes requests from other object types for some purpose related to none other of those object types. Hence the (lettered) correspondences in Fig. 3; a loosely coupled integration structure.

For business transaction workflow suitability, the generality of the object concept allows different sorts of organizational concepts to be captured (i.e. to be objectified). Furthermore, object abstractions such as specializations and generalizations allow multiple perspectives on objects. This enhances contextualization (Mylopoulos & Motschnig-Pitrik, 1995). For execution structure, we observe that object life cycles, of themselves, are useful in capturing single-document workflows and workflow (document) messaging. In this regard, the declarative nature of state transition rules, prolific also in event-condition-action (ECA) rule-based languages, represents an improvement over the imperative process specifications of structured process modelling techniques. However, as we saw through OMT, additional techniques are required to model multiple-document workflows. The addition of broader-level dynamics, however, can complicate the overall meaning of the technique. This seems true of OMT which imposes a particular intuition in its adaptation of DFDs, without an underlying formal semantics. For execution constraint, specifications for temporal aspects, exception handling and process contingencies require ‘hard-coding’, although UML offers some temporal treatment in its messaging (e.g. for ‘timeouts’). Through the separation of external triggers and messaging, it can seen that a declarative treatment of external interaction is provided for; in OMT, DFD actors are objectified, allowing an object’s interaction with its environment to be modelled.

## Behavioural process modelling

The obvious deficiency for business transaction workflow suitability in the techniques observed so far is the partial or implicit specification of execution structure. Towards imparting a sufficient cognition of business transactions, the execution order of workflow tasks needs to be clear, and triggering should allow sequence, repetition, choice, parallelism and synchronization.

In conceptual modelling, Petri net formalisms have provided a formal and expressive base from which behavioural aspects of process models can be captured precisely. Through Petri nets, a precise integration of data and process models has been possible, for example IML Inscribed Petri nets (Richter & Durchholz, 1982). High-level Petri nets such as Predicate/Transition nets (PrT-nets) and Coloured Petri nets have been proposed to improve suitability and the formal interpretation of classical Petri nets. This is seen through Activity–Behaviour

Function Model  
![](/api/attachments/7TME3AQJ/fulltext/images/040ebb2744ab3f6db5299d0f20c738d7ecfed768eb32d41d0164a0b4a6992dea.jpg)  
Figure 3. Function and object model integration for the Library domain in OMT.

Modelling (Solvberg & Kung, 1986) (PrT-nets) and the executable specifications of tools such as ExSpect (van Hee et al., 1989) (hierarchical CP-nets) and Income/Star (Jaeschke et al., 1993) (Fuzzy nets). Currently, a number of WFMS products make use of high-level Petri nets (e.g. van der Aalst, 1996).

Despite their improvements, combining both state-centric and process-centric construct into the same model poses comprehensibility problems for even basic specifications. We cite two developments in behavioural process modelling which have been aimed at alleviating this.

The Behaviour Network Model (BNM) (Kung, 1993) transfers behavioural aspects from higher levels of abstraction into the lowest level. DFDs are used at higher levels, and at the lowest level each process is transformed into a PrT-net which is tightly coupled with an ER schema. Thus PrT-net specifications replace traditional Structured English. At all levels of abstraction, model integration is process centric. As an example, Fig. 4 illustrates a DFD, PrT-net and ERM integration for the CHECK BORROWER process.

The DFD specifies that the conjunction (black dot) of Loan Request and Borrower Status are required by CHECK BORROWER so that a disjunction (white dot) of either Loan Request or Rejected Request is produced. (This data flow has been introduced to allow for model execution.) Data flows are message carriers which may be associated with ERM object types. In a PrT-net, input flows, in this case Loan Request, connect to places (i.e. u, v and Z) which in turn connect to transitions (i.e. BCI and BC2). Individual (element-of sign) or sets (equality sign) of instances of ERM entity types are linked to PrT-nets via places. Transitions, representing elementary actions, use entity and data flow instances as operands in pre- and postcondition rules.

![](/api/attachments/7TME3AQJ/fulltext/images/e6a971ddf0e67b395d08790201ca7887fe9a6731e8a7218056a54a9ce6efa258.jpg)  
Figure 4. Data, process and behaviour model integration for the Library domain in BNM.

Task Structures are purely process centric, resembling process-centric workflow specifications used in a number of commercial workflow products, for example FlowMark (IBM). In Hydra, a refined version of Task Structures (ter Hofstede & Nieuwland, 1993) is integrated with the data modelling technique PSM (Predicator Set Modelling) (an Object–Role modelling variant).

Figure 5 illustrates a decomposed Task Structure for CHECK BORROWER. The contrast with the BNM model (Fig. 4) is striking. The omission of state-based concerns simplifies considerably the process model. At the same time, triggers (arrows), decisions (circles) and synchronizations (not illustrated) provide the same expressive power as Petri net-based approaches (in ter Hofstede et al. (1998) a translation from Petri nets to Task Structures is provided). The formal semantics for Task Structures is described in Process Algebra (ter Hofstede & Nieuwland, 1993). Of course, more complicated Task Structures are possible than the one borne out by Fig. 5.

A conceptual specification language LISA-D (ter Hofstede et al., 1993) is used to express detailed process specifications and database constraints. A form of data flow between tasks is available through the use of buffers, essentially first-in, last-out (FILO) queues. For complex data (like documents), variables can be of object types (which may be schema types). The only complication is that all such object types have to belong to the schema associated with the Task Structure. This means the database schema also contains types associated with other information resources. Another restriction is that only single databases may be assigned to a Task Structure, which does not reflect the multi-database access typical in real-world business transactions.

## Business-oriented modelling

As the name suggests, business-orientation does not displace the essential nature of conceptual modelling, but rather that conceptual modelling is oriented towards an increased conceptualization of business aspects.

![](/api/attachments/7TME3AQJ/fulltext/images/8ef915efaf49199fe113cb3b486967a52fd972d3326023d0c37c5dd28cf1481e.jpg)  
Figure 5. A task structure for CHECK BORROWER.

Earlier attempts at business-orientation focused on providing some aspects of organizational processing structure, so that some organizational suitability was available. Comparatively recently, enterprise (or business) models have been proposed as contexts for IS conceptual models. As contexts, they provide a particular world-view which can improve fuzzy areas of analysis and design, for example requirements acquisition.

Of course, enterprise models themselves are abstractions of business detail. By and large, such detail is captured in organizational business plans. Business plans typically describe an organization's operational and strategic structure through qualitative descriptions which include mission, goals, objectives, critical success factors, market sectors, and competitive and quality management strategies. By contrast, enterprise models are more precise, describing the core of concepts in business plans (see, for example, Scheer & Hars, 1992).

Ramackers (1994) illustrates how detailed workflow models (as IS models) may be integrated into an executable specification framework with enterprise models. Business processing is hierarchically structured as activities, tasks and elementary actions, involving information resources and undertaken by actors. Figure 6 illustrates a part of an (operational) enterprise model for the Library domain's Loans task.

The process modelling is CP-net based. Fundamentally, each action is triggered when the precondition of all the input resources (actors and objects) being in the right state and a business rule (optional) is satisfied, the postcondition of resources being moved into the required states results. Create Loan is a composition for two exclusive actions which accept or reject the Loan. A rule language augments action specifications although it is not as expressive as LISA-D in Hydra. In the example, for instance, it is not possible to de-reference objects, Items, within complex objects, Loan.

Figure 6. Operational enterprise modelling for Library example in Ramackers (1994).  
![](/api/attachments/7TME3AQJ/fulltext/images/c6a3298e1ffc810d5bdd571dce3a78410b70498ff6034d8c141dad5991bf8e74.jpg)  
© 1998 Blackwell Science Ltd, Information Systems Journal 8, 313–337

The IS level is object based and therefore adopts state-centric integration. Those object types which are selected to be computerized are refined at the IS level (associated actions having a computerized co-actor are defined as methods). The behavioural aspects of object types are defined through event precedences which trigger state transitions or perform retrievals. Event processing is also CP-net based with an ECA language.

Clearly, much onus is placed on the enterprise model to actually deliver a sound workflow context, an issue which is at best determined empirically. In this regard we see two deficiencies in the operational enterprise model. First, while the object interaction of tasks and actions can be used to model data flows, the expressive power of the technique is limited with respect to data flow behaviour, i.e. messaging, on business transaction execution structure. In particular, a differentiation of both asynchronous and synchronous messaging (Hubbers & ter Hofstede, 1997) is absent. Moreover, no data buffering mechanism is provided. Secondly, only a basic treatment of an organization's interaction with its external environment is provided. That is, the interaction with the clients and other organizations is understood through the internal execution of tasks. Tasks form the only context from which actions are triggered. Events, including external events, are modelled at the IS level only.

Another business modelling approach which is pertinent for workflow specifications, as notably adopted by Action Workflow (Action Technologies Inc.), derives execution structure from the actor communication intent rather than organizational processing structure. This characterizes a new class of techniques, sometimes referred to as communication-based techniques. Communication-based techniques originate from the work of Flores & Ludlow (1980) based on the speech-act theory. The Actor–Bank–Channel (ABC) communication modelling technique (Dietz, 1994) of the DEMO method is one such example.

In ABC, the pattern of performative (state-changing) conversations between actors is used to derive interaction structures for communication units known as essential transactions. (In DEMO the term essential qualifies non-computerizable processing despite the possibility of computerized support.) That is, the request for something, say a business service, results in an actagenic (or an action planning) conversation; followed by an essential action; and finally a factagenic (or fact-generating) conversation, stating the results of the action. The actor initiating the actagenic conversation, i.e. initiator, is the same as the one terminating the factagenic conversation, i.e. executor. Conversely, the actor terminating the actagenic conversation is the same as the one initiating the factagenic conversation. For the execution of essential actions, actors generate plans involving communicative (e.g. information retrieval) actions from other actors in order to fulfil the essential action.

The same interaction structure applies to external transaction types, i.e. the initiator and the executor are external actors (in the environment), internal transaction types, i.e. the initiator and the executor are internal actors (in the business domain), and interface transaction types, i.e. the initiator is an external actor and the executor is an internal actor. A communication model is developed by building different transaction types into an interaction structure and including interstriction details (external data sources). A behaviour model is developed through the definition of execution and communication rules for performative conversations carried out by each actor. Significantly, different behaviour specifications may apply to different actors for the same object types.

Regardless of the effective value, which we believe requires further empirical assessment, speech acts provide an otherwise missing context for the triggering events and their causal chains. In other words, speech acts provide business transaction execution structure with an intensional closure. We believe this especially benefits the design of transactions which involves ‘fuzzy’ business processing where the execution paths are uncertain. Another benefit is the specialized treatment for a business transaction’s external interaction with the environment; this, as we have noted in previous techniques, has been insufficiently dealt with.

## WORKFLOW SUITABILITY PRINCIPLES FOR CONCEPTUAL MODELLING

Following the survey of conceptual modelling techniques and our observations of their suitability for capturing business transaction workflows, we now propose ways in which they may be extended. These are expressed through five workflow suitability principles. The principles are (i) organizational embedding, (ii) scenario validation, (iii) service information hiding, (iv) cognitive sufficiency, and (v) execution resilience.

## Organizational embedding

In reality, all concepts used in a workflow model are related to organizational concepts. This is because workflows, as indeed IS systems in general, are organizational systems or sub-systems. In other words, workflows have an organizational embedding.

We saw through business-oriented techniques that a business world-view, whether it be through organizational processing structure in enterprise models or through organizational communication in a theory of speech acts, provides a context which grounds the intent of a workflow. At the same time, it was apparent that such higher-level enterprise modelling contexts serve ends other than IS design, for example group planning and business service design. In other words, enterprise and workflow modelling have distinct, if interrelated and overlapping, concerns. Overloading one with the other's function can lead to an overloaded technique. In terms of our suitability synthesis, the issue for workflow modelling is therefore to focus its concern on execution structure, execution constraint and external interaction, while at the same time allowing it to contain a sufficient 'interface' to enterprise models.

It is in the refinement strategy from enterprise models to workflow models that we recognize a potential problem. This can be seen in the technique of Ramackers (1994). Recall that its refinement strategy is hierarchical, i.e. IS object methods are refined hierarchically from business-task actions. The problem lies in the fact that some workflow components need to be refined from a composition of enterprise components. This would certainly be the case when a workflow domain (note, not its environment) incorporates multiple organizations. Hierarchical refinement does not permit this. Instead it necessitates for such a workflow component, as illustrated in Fig. 7, that the related enterprise components are composed in order for the refinement to occur.

![](/api/attachments/7TME3AQJ/fulltext/images/459b75c5b26659aac05171a6c086e27276cf10ce74c584a4b970da71f4a38c05.jpg)  
Figure 7. A violation of conceptualization in enterprise to IS model refinement.

In fact, we contend that this type of composition (of an artificial component) is a violation of the Conceptualization Principle. In general, we require that, as dependent as workflows are on organizational contexts (of whatever sorts), in no way should this dependence lead to unnatural definitions. This is realized through the following principle:

## Principle — Organizational Embedding

A technique should embed all concepts in a conceptual model, directly or indirectly, but without redundancy, into organizational concepts.

The principle requires the dependence of workflow concepts on organizational concepts, without at the same time prescribing what form the organizational context should be, or indeed how the dependence should be constructed. Applied to the example, we can see that the hierarchical refinement of IS models to enterprise models would have to be replaced by a networking refinement to fulfil the principle. More than just a structural nicety, the principle endorses the autonomy of specifications, however interdependent, at both levels.

## Scenario validation

Through the Organizational Embedding Principle we have described the need for a structural context from which a workflow can be validated. As we have observed, organizational processing structures such as organizational units, business processes, business services and actors as individual concepts, and business transactions which we have proposed as an aggregate concept, all serve to ground the design of workflows.

Of course, the validation of workflows means more than the alignment of its concepts with concepts in the domain. It means the tracing of execution sequences, and the interaction involving actors, databases and the domain's environment. The same workflow structure can result in different execution sequences, given the different events and conditions which can influence the different parts of workflow execution. What is required therefore is a dynamic context for workflow execution.

We observed that different techniques provide different mechanisms for a ‘run-time’ validation of workflows, for example hand-traced execution resulting from external events in DFDs, event-based model enactment in Petri net-based techniques, scenarios and use cases in OOA/D techniques and speech-act traces in communication-oriented techniques.

We generalize the mechanisms of workflow validation as being those associated with discrete points in workflow execution which serve to activate or re-activate workflow execution. Indeed, triggering events like external or temporal events, or actor interactions, all occur at discrete points. From our Library domain example, the arrival of a Purchase Request is an example of an event which activates the workflow and results in a continuous execution sequence until an Order is forwarded to a Publisher. The arrival of an Ordered Item re-activates the workflow, and the update of the Item Details into the database marks the completion of the workflow. Although the example is rather simple, we can see the general pattern of workflow execution — a set of continuous execution sequences associated with triggering events which activate and re-activate the workflow.

We prefer the term scenarios for a set of descriptors which define the activation or reactivation of workflow execution, all the way to the final event which suspends or terminates a workflow. And we require that workflow modelling techniques provide explicit workflow validation through the following principle:

Principle — Scenario Validation

A technique should provide an explicit notion of scenario for model validation.

## Service information hiding

Following from this discussion, we turn to the most common problem area that we observed from the survey. This is the arbitrary treatment of a business transaction's external interaction. Again, from the Library example, workflows interact with stakeholders in their environments, e.g. Borrowers and Publishers, in a way which serves to validate workflow execution; as we have just described, external events activate and re-activate workflow execution. Through most techniques, as indeed in most workflow specification languages currently deployed, we observe that there is no modelling distinction between a workflow's external interaction (with its environment) and the internal interaction (between its tasks). Rather, events simply trigger different parts of a workflow, regardless of where they emanate from.

The problem here is that the external interaction with the environment is direct. More specifically, the environment's triggering of a workflow is direct, meaning that the environment is required to have knowledge of how a workflow is structured and which business process should be triggered. Under organizational service-orientation, a paradigm widely utilized for business delivery, the way an organization structures its processing should be insulated from its customer interaction. This is therefore true of workflows too: an external stakeholder interacting directly or indirectly with a workflow should not need to know about its internal structure. The implication is that when processes are re-engineered, the actual request is not affected.

As we discussed previously, events, particularly external events, are associated with an intent. In a dynamic sense, we have seen that events may be associated with communication intents. Of course, in a structural sense events are associated with organizational processing structures. In fact, under the service-orientation of organizational processing, business services are the units by which organizations deploy functionality. In other words, an organization reacts to the events of business service requests in undertaking its workflows. For the formulation of business service requests, we propose the following principle:

## Principle — Service Information Hiding

A technique should allow the formulation of service requests to be independent of their actual processing.

It may be recognized that the name of the principle reflects the well-known Information Hiding Principle in software design. Our principle, in fact, applies Information Hiding for business transaction processing, where business services are the interface to business processes, and where business processing structure is hidden from business service requests.

Figure 8 illustrates one major advantage of such workflow service-orientation, namely workflow integration across organizational boundaries. Three organizations — a client, a server and a supplier (to the server) — are depicted with their set of services (small boxes) as interfaces to their processes (ellipses). The ordered set of arcs depicts messages to/from services carrying requests and responses. Within the services (somehow), the appropriate workflows are activated. Direct process-to-process triggering is depicted to occur when the processes lie within the same service context.

The use of object-orientation for services has the advantage of providing declarative specifications for service behaviour. In particular this enables external interactions to be captured through ECA specifications. The encapsulation feature could allow a set of workflows to be hidden within and coordinated by a service. Also, the inheritance property allows for reuse of services within services, providing an additional layer of workflow modularization, over and above process/object decomposition.

In stating this, we are not convinced about the singular use of object-orientation for all workflow components. While the reactive nature of services lends itself to objectification, we feel that process-orientation best captures the highly interactive and imperative functionality of business processes. We therefore recommend that entire process triggering structures, for example Petri nets or Task Structures, be encapsulated into service objects.

A major advantage of this modelling duality is that (widely used) process-centric workflow specifications can be deployed and integrated using service objects in open distributed architectures, for example a Trader facility (Bearman, 1993). This goes a significant way towards the development of interorganizational workflows.

![](/api/attachments/7TME3AQJ/fulltext/images/ea4664952ea083610fc90053617899376566e83a82fe252552df453282586e27.jpg)  
Figure 8. Operational business modelling for Library example in Ramackers (1994).

## Cognitive sufficiency

In the previous principles we have dealt with workflow context and external interaction. We now turn our attention to the heart of workflow specifications, namely their execution structure and constraint.

In the survey, we saw that there are a number of aspects in a workflow specification, for example data and control flow, and choice, parallelism and synchronization in task execution. And there are a number of ways in which the same underlying model can be presented, for example data-flow and control-flow 'views'. Yet conceptual models, in general, are required to convey a certain amount of information which should not be split up, if the model is to be effective. For example, certain types of constraints (e.g. uniqueness and mandatory role constraints) in a data model are presented together, in order to preserve the intended understanding from being deflected. For our present purposes, we will use the term cognition to describe this.

In this section, we identify certain areas of workflow specifications which the survey suggests are treated variously. We argue that these areas should be included in a workflow model in order to enhance its cognition for business transactions. We generalize our motivation through the following principle:

## Principle — Cognitive Sufficiency

A technique should provide a sufficient cognition of a model such that the need for fundamental business process execution assumptions is eliminated.

Areas of business transaction execution structure and constraint which we believe would enhance the cognition of workflow models are described in the remaining section.

## Data and control flow combined

Although workflow technology has had separate origins of business process coordination (control-flow orientation) and document management (data-flow orientation), this separation does not cater for a large class of business transactions which requires both. Not surprisingly, a number of workflow vendors are now integrating process triggering and document messaging. IBM's integration of FlowMark and Lotus Notes and InConcert (Xerox), ENTIRE/Workflow (Software AG) and Computron Workflow (Computron), all described in the ButlerBloor Report, are examples.

While the end functionalities differ, a core commonality of triggering and messaging is apparent. Triggering structures invariably capture process execution order through sequence, choice, iteration, parallelism and synchronization. Messaging allows different modes of data flow with respect to processes: i.e. synchronous, where a process sends a message to another process and waits for a return message; and asynchronous, where a process sends a message to another process, without waiting for a return message. Messages may also be stored transiently, i.e. buffered, in containers where other processes can retrieve them. A base process-centric model on which messaging is defined permits multiple-document flow which is characteristic of a large proportion of business transactions.

The survey suggests that, despite the need for their integration, techniques are strong in data flows or control flows, but not both. BNM, Hydra and the approach of Ramackers (1994) all have elements of data flow and control flow. In BNM, DFDs and PrT-nets are used at different levels of abstraction, meaning that at one level data flows are prominent, while at the other control flows are prominent. In Hydra, a particular form of data stores is available through buffers, but since buffers store only data values, no rich data-flow mechanism is available. In Ramackers (1994), a form of data flow is captured through object integration with task and action CP-nets, but no data store construct is present.

## Human-computer interaction

Another area which seems lacking in full conceptual treatment, and which is pertinent to the workflow execution structure, is workflow interactions. Recall that interactions occur at discrete points of workflow execution which serve to activate and re-activate workflow execution. We encountered their importance in the construction of scenarios for workflow validation. Over and above the notion of procedure calls, interactions involve a dialogue between actors, e.g. between a customer and a salesperson (human–human interaction, HHI), and between a customer and a data entry form (human-computer interaction, HCI) and a protocol involving a file transfer between two computers (computer-computer interaction, CCI).

We saw that support for interactions ranged from some form of HCI, e.g. external object design in Ramackers (1994), to full HHI, e.g. speech acts in Dietz (1994). For workflow specifications, we envisage the extension of conceptual specification languages, such as Hydra's LISA-D, to capture dialogue specifications for HCI points. This should allow a greater interactivity than external object design (which involves the data entry of object attributes). Also, it should be related to higher forms of dialogue analysis like speech acts so that HCI may be viewed as a specialized form of HHI. Finally, certain details about CCI can be conceptualized, since they relate ultimately to user requirements. This aspect requires further research in the context of dialogue modelling.

## Temporal aspects

A workflow's execution is not constraint free, and we observed that task pre- and postconditions play a fundamental role in ensuring workflow quality control. An important feature of execution constraint is the temporal aspect. After all, temporal constraints are observable in a large proportion of business transaction processing. In courts of law, for example, matters are scheduled and adjourned at designated times, and in doing so the availability of required documentation is requested (to outside parties) within a certain duration of the court's hearing. Part of the acquisition of information involves searching a number of sources, where if one source does not yield information within a time duration then another source is canvassed — an example of a ‘time-out’.

Support for time in current workflow products is not widespread. Some functionality for workflow timing can be identified in Georgakopoulos et al. (1994). Although not widespread, some conceptual modelling support is available. The most common type of temporal constraint supported relates to process preconditions, where time functions allow time points and intervals to be specified. This is exemplified in TEMPORA (which specialized in time functionality) (Theodoulidis et al., 1990). UML, the object-oriented technique combining the efforts of Rumbaugh, Booch and Jacobsen, provides 'time-outs' during synchronous messaging, for example an object sends a message to another object and if a return message has not been received by a certain duration the messaging is aborted. This embodies time duration. Techniques based on time adaptations of Petri nets — timed Petri nets — have a sufficient expressive power to capture time points, intervals and durations.

Of course, the issue is the suitability of time functions so that workflow model cognition is sufficient. The variability of time functionality in workflow specification languages and conceptual modelling techniques suggests that this is open. Other features which are included in time ontologies (see, for example, Theodoulidis & Loucopoulos, 1991) are the relativity of time (absolute or relative) and multiplicity of execution within an interval. Indeed, further research, particularly empirical insight, into the application of these features for workflow specifications, for example in messaging and workflow interactions (including dialogue specifications), is required. Moreover, it should be remembered that the temporal aspect of software specifications is not new when one considers the developments in specification languages like Real-Time Process Algebra and Petri net-based approaches. All of these address temporal aspects in process specifications and, as such, offer further insight for timed workflow specifications.

## Execution resilience

An important aspect of execution constraint relates to exception handling. Needless to say, this too preserves the integrity of workflow execution. Of course, the natural place for exception handling is in detailed specifications of workflow tasks, for example in pre- and postconditions and action specifications. In this section, we focus on two aspects of exception handling which relate to the specialized area of workflow recovery. One is the backwards execution of a workflow due to the occurrence of an exception, for example when an Order has been terminated after the Library has issued it. The other is the running of process contingencies when their associated processes cannot run, for example a process at a site crashes.

We cite as a common motivation the execution resilience of a workflow in the presence of these abnormal exceptions. Through provisions of recovery, for example as in FlowMark (IBM), workflows can achieve execution resilience. In turn, we require workflow model execution resilience through the following principle:

## Principle — Execution Resilience

A technique should support the handling of exceptions, so that the execution resulting from a specification can be validated as being resilient.

Although traditional process modelling techniques do not deal with this aspect, a recently proposed workflow modelling technique, for example Casati et al. (1995), provides basic mechanisms for exception handling.

Through the survey, we saw that none of the techniques provided a treatment for workflow recovery. Hence business transaction quality controls like contingency planning can only be captured in detailed specifications, where possible. The main impetus for workflow recovery has occurred at the implementation level of workflows, specifically through transactional workflows (for a general survey, see Kim (1994), pp. 596–598). In particular, the database transaction model with its ACID properties (atomicity, consistency, isolation and durability) has been extended for (run-time) workflow execution properties.

Ordinarily, when exceptions occur, an undo of changes made by started but uncommitted tasks is applied. However, the long-lived nature of workflows means that committed tasks can be interleaved with uncommitted tasks. For example, subtasks are allowed to commit prior to the supertask committing. To rollback committed tasks, advanced transaction models use instead compensations. Examples of compensations in a workflow could include the following: the logical reverse of an update; sending abort messages to remote services for notification; triggering transitions to erroneous service states.

For crash situations, we recommend a rollforward strategy, where the WFMS will ensure consistency by performing a physical rollback of the current atomic unit, followed by restarting its first task. Again, the normal transaction behaviour, in this case redo is not enough. Since workflows could have tasks located on different nodes of a network, we envisage the use of contingencies as adopted in distributed transaction management. Here, a contingency represents an alternative task which can be run if the normal task cannot start up. We propose the use of a range of contingencies which can be run for failure under various conditions, for example numbers of failure and/or temporal constraints. This not only enhances the robustness of contingency but also captures problem escalation which is typical in business transaction processing. It also allows for the forcibility of a task, which as a requirement for distributed transaction management means that the task has to succeed eventually.

## CONCLUSION

Our approach in this paper was twofold. First, we surveyed techniques whose concepts and features may be observed in existing workflow specification formalisms. For presentation purposes, we classed these into structured process modelling, object-oriented modelling, behavioural process modelling and business-oriented modelling. We used key features of business transactions, namely the way their (organizational) context is established, the way their execution structure is portrayed, relatedly the mechanisms of their execution constraint, and finally, and what we believe is not salient enough, the modelling attention given to their environment interaction, i.e. their external interaction. Secondly, we elicited, from common and striking problems in the survey, principles which provide the conceptual foundations for extensions which address the workflow suitability of techniques. Also a form of contingency is incorporated through alternative execution of tasks. We do not believe that workflow products as yet provide a full and coherent treatment for workflow recovery. Nor is it apparent that techniques have incorporated workflow recovery.

While the synthesis was open-ended and sometimes arbitrary in feel, we argue that the proof of its value lies in the principles. These serve not only to redress conceptual modelling for the modern-day application of workflows, but also to highlight significant areas of workflow extension. In doing so, we have also offered new ways in which techniques may be assessed for workflow modelling.

The greatest ramification for workflow specifications lies in our proposals for workflow service-orientation. Included with a richer validation which can now incorporate a workflow's environment, we believe a benefit lies in the use of service objects to deploy workflows in current open distributed architectures. This would permit global access and integration of multi-organizational workflows.

This work has extended beyond these developments of conceptual foundation. To date, we have applied extensions to Task Structures which accord to the principles and we have empirically tested out the technique in a real-world case study. Future work will focus on mapping workflow conceptual models to product-specific specifications.

## ACKNOWLEDGEMENTS

Part of this work was funded by CITEC, a business unit of the Queensland Government's Department of Public Work and Housing.

Suggestions by the referees for improvement of an earlier version of this paper are gratefully acknowledged.

## REFERENCES

van der Aalst, W. (1996) Petri-net based workflow management software. In: Proceedings of the NSF Workshop on Workflow and Process Automation in Information Systems: State of the Art and Future Directions, pp. 114–118. University of Georgia, Athens, Georgia.

Avison, D.E. & Wood-Harper, A.T. (1991) Information systems development research: an exploration of ideas in practice. The Computer Journal, 34, 98–112.

Bansler, J.P. & Bodker, K. (1993) A reappraisal of Structured Analysis: design in an organizational context. ACM Transactions on Information Systems, 11, 165–193.

Barros, A.P. & ter Hofstede, A.H.M. (1997) Realizing the full potential of workflow modeling: a practical perspective. Journal of Information Technology, 3, 59–86.

Barros, A.P., ter Hofstede, A.H.M. & Proper, H.A. (1997) Towards real-scale business transaction workflow modelling. In: Proceedings of the Ninth International Conference CAiSE'97 on Advanced Information Systems Engineering, Olivé, A. & Pastor, J.A. (eds). Lecture Notes in Computer Science, 1250, 437–450.

Batini, C., Ceri, S. & Navathe, S.B. (1992) Conceptual Database Design — An Entity-Relationship Approach. Benjamin Cummings, Redwood City, CA.

Bearman, M.Y. (1993) ODP — Trader. Open Distributed Processing, 2, 37–51.

Booch, G. (1991) Object-Oriented Design with Applications. Benjamin Cummings, Redwood City, CA.

Casati, F., Ceri, S., Pernici, B. & Pozzi, G. (1995) Conceptual modeling of workflows. In: Proceedings of the OOER'95, 14th International Object-Oriented and Entity-Relationship Modelling Conference, Papazoglou, M. (ed.). Lecture Notes in Computer Science, 1021, 341–354.

De Antonellis, V. & Pernici, B. (1995) Reusing specifications through refinement levels. Data and Knowledge Engineering, 15, 109–133.

Dietz, J. (1994) Business modelling for business redesign. In: Proceedings of the 27th International Conference on System Sciences, pp. 723–732. Honolulu, Hawaii.

Embley, D.W., Jackson, R.B. & Woodfield, S.N. (1995) OO Systems analysis: is it or isn't it? IEEE Software, 12, 19–33.

Flores, F. & Ludlow, J.J. (1980) Doing and speaking in the office. In: Decision Support Systems: Issues and Challenges. pp. 95–118. Pergamon, New York, NY.

Georgakopoulos, D., Hornick, M. & Sheth, A. (1995) An overview of workflow management: from process modelling to workflow automation infrastructure. Distributed and Parallel Databases, 3, 119–153.

Georgakopoulos, D., Rusinkiewicz, M. & Litwin, W. (1994) Chronological scheduling of transactions with temporal dependencies. VLDB Journal, 3, 1–28.

van Hee, K.M., Somers, L.J. & Voorhoeve, M. (1989) Executable specifications for distributed information systems. In: Information System Concepts: An In-depth Analysis, Falkenberg, E.D. & Lindgreen, P. (eds), pp. 139–156. North-Holland/IFIP, Amsterdam, the Netherlands.

ter Hofstede, A.H.M. & Nieuwland, E.R. (1993) Task structure semantics through process algebra. Software Engineering Journal, 8, 14–20.

ter Hofstede, A.H.M., Orlowska, M.E. & Rajapakse, J. (1998) Verification problems in conceptual workflow specifications. Data and Knowledge Engineering, 24, 239–256.

ter Hofstede, A.H.M., Proper, H.A. & van der Weide, Th.P. (1993) Formal definition of a conceptual language for the description and manipulation of information models. Information Systems, 18, 489–523.

Hubbers, J.W.G.M. & ter Hofstede, A.H.M. (1997) Formalization of communication and behaviour in object-oriented analysis. Data and Knowledge Engineering, 23, 147–184.

Jacobson, I., Christerson, M., Jonsson, M. & van Overgaard, P. (1992) OO Software Engineering: A Use Case Driven Approach. Addison-Wesley, Reading, MA.

Jaeschke, P., Oberweis, A. & Stucky, W. (1993) Deriving complex structured object types for business process modelling. In: Proceedings of the 13th International

Conference on the Entity-Relationship Approach, Loucopoulos, P. (ed.), pp. 28–45. Springer-Verlag, Manchester, UK.

Kim, W. (ed.) (1994) Modern Database Systems: The Object Model, Interoperability and Beyond. Addison-Wesley, Reading, MA.

Kung, D.C. (1993) The behaviour network model for conceptual information modelling. Information Systems, 18, 1–21.

Makey, P. (ed.) (1996) Workflow: Integrating the Enterprise. Report of the Butler Group, Hessle, UK.

Mohan, C. (1996) State of the art in workflow management system research and products. In: Proceedings of ACM SIGMOD/PODS 96 Joint Conference, New York. ACM Tutorial presentation.

Mylopoulos, J. (1997) Information modeling in a time of revolution (Keynote address). In: Proceedings of the Ninth International Conference CAiSE'97 on Advanced Information Systems Engineering, Olivé, A. & Pastor, J.A. (eds). Lecture Notes in Computer Science, 1250.

Mylopoulos, J. & Motschnig-Pitrik, R. (1995) Partitioning an information base through contexts. In: Proceedings of the Third International Conference on Cooperative Information Systems (CoopIS'95), Vienna, Austria, pp. 44–55.

Olle, T.W., Hagelstein, J., Macdonald, I.G., Rolland, C., Sol, H.G., van Assche, F.J.M. & Verrijn-Stuart, A.A. (1988) Information Systems Methodologies: A Framework for Understanding. Addison-Wesley, Reading, MA. Opdahl, A.L. & Sindre, G. (1993) A taxonomy for real-world modelling concepts. Information Systems, 19, 229–241.

Ramackers, G.J. (1994) Integrated Object Modelling: An Executable Specification Framework for Business Analysis and Information System Design. PhD thesis, University of Leiden, Leiden, the Netherlands.

Richter, G. & Durchholz, R. (1982) IML-inscribed high-level Petri nets. In: Information Systems Design Methodologies: A Comparative Review, Olle, T.W., Sol, H.G. & Verrijn-Stuart, A.A. (eds), pp. 335–368. North-Holland/IFIP, Amsterdam, the Netherlands.

Rumbaugh, J., Blaha, M., Premerlani, W., Eddy, F. & Lorenson, W. (1991) Object-Oriented Modeling and Design. Prentice-Hall, Englewood Cliffs, NJ.

Scheer, A. & Hars, A. (1992) Extending data modeling to cover the whole enterprise. Communications of the ACM, 35, 166–172.

Shoval, P. (1991) An integrated methodology for functional analysis, process design and database design. Information Systems, 16, 49–64.

Shumate, K. (1991) Structured analysis and object-oriented design are compatible. ACM Ada Letters, 9, 78–90.

Solvberg, A. & Kung, C.H. (1986) On structural and behavioural modelling of reality. In: Database Semantics (DS-1), Steel Jr, T.B. & Meersman, R. (eds), pp. 145–171. North-Holland/IFIP, Amsterdam, the Netherlands.

Theodoulidis, C.I. & Loucopoulos, P. (1991) The time dimension in conceptual modelling. Information Systems, 16, 273–300.

Theodoulidis, C.I., Loucopoulos, P. & Wangler, B. (1990) Requirements specification in TEMPORA. In: Proceedings of the Second Nordic Conference CAiSE '90 on Advanced Information Systems Engineering, Steinholtz, B., Søluberg, A. & Bergman, L. (eds). Lecture Notes in Computer Science, 436, 264–282.

Wand, Y. & Weber, R. (1990) An ontological model of an information system. IEEE Transactions on Software Engineering, 16, 1282–1292.

Yourdon, E. (1989) Modern Structured Analysis. Prentice-Hall, Englewood Cliffs, NJ.

## Biographies

Alistair Barros graduated with Honours in Computer Science at the Department of Computer Science, University of Queensland in 1987. Since 1986, he has worked for the leading IT service provider in Queensland, CITEC, where he worked in the roles of analyst/programmer, project manager, consultant, and for four years in technical support as the chief database manager with Unix/Ingres databases. From 1995, he returned to the University of Queensland to undertake a PhD in the area of conceptual modelling and workflows, and his thesis was submitted for examination at the start of 1998. Currently he is working at the Distributed Systems Technology Centre (DSTC) as research scientist, which includes system integration consultancy roles involving Boeing Australia and CITEC.

Arthur ter Hofstede received his Masters degree (1989) and his PhD degree (1993) from the University of Nijmegen in the Netherlands. He worked for four years at the Software Engineering Research Centre (SERC) in Utrecht, where his research focused on meta-CASE technology and foundations of conceptual modelling. After working as a Lecturer at the University of Nijmegen in the Netherlands and the University of Queensland in Australia, he is currently a Lecturer at Queensland University of Technology in Australia and Deputy Director of its Cooperative Information Systems Research Centre. Arthur ter Hofstede has published in many journals and conference proceedings in the fields of information systems, software engineering and theoretical computer science. His research interests include conceptual data modelling, conceptual query languages, OO analysis, formalization, and workflow specification languages.
