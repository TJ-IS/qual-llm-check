---
otero_id: 6100
otero_key: "SR8VH6A5"
title: "Plural: A decentralized business process modeling method"
authors: "Oktay Turetken; Onur Demirors"
year: "2011"
journal: "Information & Management"
doi: "10.1016/j.im.2011.06.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Plural: A decentralized business process modeling method

Oktay Turetken <sup>a,</sup>\*, Onur Demirors <sup>b</sup>

<sup>a</sup> European Research Institute in Service Science (ERISS), Tilburg University, Warandelaan 2 K729, 5000 LE, Tilburg, The Netherlands <sup>b</sup> Informatics Institute, Middle East Technical University, 06531 Ankara, Turkey

## A R T I C L E I N F O

Article history: Received 23 November 2009 Received in revised form 21 June 2010 Accepted 23 May 2011 Available online 13 June 201

Keywords: Business process modeling Decentralized process modeling Process improvement Process owner User involvement

## A B S T R A C T

Top-down and centralized approaches prevail in the design and improvement of business processes. However, centralized structures pose difficulties for organizations in adapting to a rapidly changing business environment. Here we present the Plural method which can be used to guide organizations in performing process modeling in a decentralized way. Instead of a centralized group of people understanding, modeling and improving processes, our method allows individuals to model and improve their own processes to help in fulfilling their roles in the organization. An individual model depicts a set of activities performed by a role, which together result in a cohesive service within the organization. These individual models are then integrated as necessary to show the way the organization works. We applied the Plural method in a case study of a small-size software organization. We describe the method and its underlying principles and then discuss the findings of our case study, lessons learned, and limitations. The study thus provided evidence of Plural’s utility and showed how an organization might exploit its strengths.

\- 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizations uses process models to understand, analyze, and communicate organizational knowledge as well as a steppingstone in automating their processing. We use process modeling in establishing quality manuals, assessing and identifying added value, establishing control mechanisms, and automating workflow. Consequently, process models are considered to be one of the most valuable assets of an organization.

Process modeling is traditionally performed as a top-down centralized approach. That is, a group of experts (systems or process engineering groups), work with groups of individuals system users) in different roles to identify and record the business processes. As the degree of the involvement of the process performers in the modeling effort increases, the likelihood that the model reflects the actual processes as well as the likelihood that the group enjoys using the model increases. Therefore, the degree of their involvement is most critical in determining the success of their efforts. We hypothesize that the full advantage of involvement is obtained when the individuals model their own processes.

The cycle times of top-down centralized organizational process modeling projects can be in the order of months or years, or even decades for very large systems. Furthermore, once process definitions are considered stable it is often difficult to change them. However, to respond to the demand of markets, organizations should be able to change their way of working. Thus we need to reduce the cycle time for modeling and improvement to the order of days or weeks. Process infrastructure should be able to incorporate changes rapidly. We believe that this goal could be achieved by a decentralized modeling approach.

Decentralized process modeling presumes each individual can define and maintain his or her own activities. If people model their own processes, they identify and resolve inconsistencies among their definitions. Such partial definitions, which are also maintained in a decentralized manner, can then be integrated to show the overall business processes and the organization’s process network at a point in time. One of the significant challenges of this approach is that the resultant partial models possess any inconsistencies due to different people’s concept of the overall process. However, we consider this an opportunity to allow an organization to identify points where improvements are possible in the overall process. This suggests that inconsistency resolution can be performed by the process performers rather than a central group who do not necessarily understand the problems or by an automated task executed by the IS. Shifting the responsibility to the knowledge workers improves the communication between them and uncovers implicit assumptions about the way the processes are carried out.

Decentralization in process modeling also allows process change to be performed by the process users on their own (individual) model rather than a central group maintaining organization’s overall system. This helps by increasing employee involvement, which fosters problem solving and process improvement. Participation and commitment allow employees to make decisions and this makes it possible to reorganize rapidly to change, creating an environment of ownership [3]. This aligns with the shift from command-and-control to coordinate-and-cultivate with decentralized structures of loose hierarchies and democracies centered around enduring human values.

We developed a method, Plural, which provides a guideline for organizations to perform business process modeling in a decentralized way; it allows each process owner to take the responsibility of describing and improving his or her own process without any central control structure, but builds and maintains the organization’s process-base.

During the development of the Plural method, we performed a number of pilot studies and applied case scenarios to explore the applicability of the method and enhance its structure. The intent was to answer the research question:

‘‘What benefits can organizations gain from applying the Plural method of modeling their processes in a decentralized manner?’’

Using the Plural method, diagrams depicting process dependencies and role dependencies were generated in order to provide insight into the way the organization works and can be improved.

## 2. Related work

Most of the business process management approaches assume central specification and enactment of processes (e.g., [2,11,14]). In general, such a structure provides functionality for process modeling and a software engine runs the models, records execution, and supports task automation and tool integration as necessary. The same assumption also prevailing in process redesign/improvement approaches. However, a centralized framework entails difficulties in knowledge-based organizations. It limits the degree of involvement of the process owners in the modeling and improvement efforts and makes it more difficult for them to own and maintain the definition.

Having recognized the importance of the involvement of the system users in process modeling, approaches urge organizations to motivate and encourage their employees in taking part in their definition and improvement projects [1]. Process modeling thus becomes a necessary skill for people in order for them to have a better understanding of the models and know how to evaluate alternatives. However, there is a lack of mechanisms and methods to help achieve process modeling in a decentralized manner. Studies on capturing process knowledge from different perspectives (e.g., a view-based approach for process elicitation [5]) support process model definitions at individual levels but assume a central structure in charge of eliciting and modeling processes, identifying and resolving inconsistencies between partial models, and integrating them.

Methods grounded on role-based modeling (e.g., Riva method and role activity diagrams, or formal enterprise modeling based on roles [9]) provideaconceptualdescriptionofasystem.Thesemethodsofferproven approaches for specifying processes and systems in terms of roles and theirinteraction,providingamechanismtocaptureindividuals’behavior in the organization. With extensions, these notations can be utilized for decentralized process modeling. A decentralized structure should be in placenotonlyfortheelicitationandmodelingphasesbutalsoforallother phases.

Singh et al. [15] proposed a commitment-based SOA that represents each participant as an agent that interacts and carries out a (business) service function through creating and manipulating commitments to one another. It offers flexibility to the participant in their local behavior provided that their interaction protocols are not violated. This approach dealt with the execution aspects of business processes rather than their elicitation, analysis, and modeling, which involve executable processes or components (as opposed to a conceptual model).

## 3. The Plural method

## 3.1. Core concepts

The decentralized approach allows each participant in the organization to define a (partial) model of his or her domain. These models are integrated as necessary to define the overall organizational processes. The complete representation is derived by joining the individual models that were (independently) described. However, the effort is more effective if, at the start of the definition, the goal, objectives and scope of what is to be modeled is communicated and accepted by all parties. This sets the goal and boundaries without directing what is to be done locally by each participant (agent). Thus each employee is given full responsibility to define the services/operations he or she is responsible to provide and how it interacts with others (communicating and negotiating with them).

The relationships between agents and processes depend on the agents’ roles. The operations to be fulfilled by the roles, when composed with other operations, make up the process. Fig. 1 shows the conceptual relationship between processes, roles, operations, and agents.

Although most businesses work in an ad hoc manner where work is completed with no high-level knowledge of how, an agent is provided with (or gathers) necessary resources and inputs needed to perform the activities and produce outputs. The Plural method captures and articulates this knowledge by requiring each agent to state his or her inputs and necessary resources. They must also define the outputs and their roles in obtaining the inputs and forwarding the outputs to another agent. As these expectations are defined by all agents they will be either fulfilled or renounced and all information passing through the interfaces is collected and analyzed. This therefore defines the interaction protocol between roles and defines their commitments.

The Plural method presumes that a dependency is a precondition for an activity to be performed. Thus an agent will be notified whether a precondition is or is not satisfied. The message can also include a notification about the state of a business object in the environment. Thus, an agent can receive a message indicating that a report is ready or it can receive the report itself.

Fig. 2 shows an abstract example of an individual process description of a role (role A). It displays how an agent’s role represents the activities it performs within the scope of a specific service it provides and its expectations from others.

To use the Plural method, an organization goes through three phases that establish its process-base. Fig. 3 shows these phases and the information flow between them.

![](/api/attachments/SR8VH6A5/fulltext/images/468f066ef12c073424b3fb50ddb127252cb6a7a13262ed793d2949a9a0dad9a8.jpg)  
Fig. 1. Relationship between processes, roles, operations, and agents

![](/api/attachments/SR8VH6A5/fulltext/images/5c92b7ddbacadae34bc96851ebd5cf3db38d854a117c5e8607b68f2df9ece2b4.jpg)  
Fig. 2. . Roles and expectations

![](/api/attachments/SR8VH6A5/fulltext/images/ab080c32ccb92f1faf35b39e6797b78e52442cff33df33995585bf08c08bef0e.jpg)  
Fig. 3. The Plural phases

In the context definition phase, all process owners define the purpose and scope of the modeling process by identifying the processes to be covered and the roles that participate in the processes. In the description and conflict resolution phase, development agents define the activities they perform and their expectations about their roles. They also identify and resolve inconsistencies and conflicts between their definitions and others. Role-based definitions are then verified by coordinators and validated by peer agents. In the integration and change phase, complete and consistent models are merged as necessary and new models are generated and analyzed for improvement opportunities. Based on its type, a change request triggers the first or second phase and the cycle repeats until the change is incorporated and the processes reach their next consistent and complete state.

## 3.2. Context definition

This first phase provides a structural frame as a high-level process network consisting of participating roles, agents, and their structural relationships. This entails:

\- Determining the purpose of the initiative.

\- Establishing the coordination team.

\- Identifying the processes that will be covered.

\- Identifying the roles and their relationships.

\- Assigning agents to roles.

\- Planning the execution of the method.

The organization initiates the process with a meeting that brings together all related process owners and stakeholders. The moderator introduces the method and presents a brief overview of the participants’ responsibilities. The participants then identify the firm’s processes in the long and short-term.

Before the scope of the initiative is defined, the group establishes the coordination team – that facilitates the execution of the method. The coordinators monitor and facilitate the definition process, guide agents in modeling and maintaining the process network, verify individual role process models, envisage the top view of processes as a whole, explain and analyze it, and identify problems and capture high-level improvements.

Depending on the scope, the group might decide to arrange follow-up meetings with the group members, stakeholders and the coordinators to perform the subsequent activities, including determining its scope and the roles that participate in these processes. Guiding resources, such as the process definitions, procedures, and standards provide valuable inputs for these meetings.

The coordination team depicts the coverage on a scope diagram. Fig. 4 shows an example of this. A connection between roles and processes implies that the role is participating in the process by offering one or more operations to serve the process goal. The include relationship between processes represents a reusable process that is unconditionally incorporated into the execution of another process. The extend relationship, on the other hand, is the incorporation of the reusable processes that depend on given conditions.

At this stage, the group can benefit from several resources including: existing process definitions and procedures; documents explaining the organizational structure, roles, and responsibilities; resources representing organization’s vision, goals, and strategies; and quality standards, handbooks, etc.

Since the method is based on a role-based approach, the roles of the participants and their relationships must be specified. The structural relationships are depicted in a role diagram. Similar to the class concept in UML, the relationships can be of type association, aggregation or generalization. Fig. 5 gives an example of a role diagram. There, the configuration manager and trainer are both project team members – a more general role (these two roles inherit all of the responsibilities of the project team member). Review team is an example of an aggregate role.

The roles in a role diagram can be either:

\- Active – modeled by an agent, where each active role has its own individual role-process model describing a particular operation as a set of the activities it performs for a specific process. Each active role, in turn, is assigned to one or more agents in the organization. Or,

\- Inactive – external to the organization (e.g., customer) or outside its scope because of the processes covered (e.g., internal customer). They interact with active roles but they do not have process descriptions.

After establishing the consensus on the scope and role definitions, each agent takes over some (active) roles as one of their responsibilities in the organization. Agents can be assigned to multiple roles or may be taken over by several agents. The coordination team ensures that no active role is left unassigned.

![](/api/attachments/SR8VH6A5/fulltext/images/1db9e06f368699058d9e4433bed772cc8522db01bef83889f4514c2886e84f5a.jpg)  
Fig. 4. A scope diagram.

There are two types of responsibilities for process definition:

\- Development agents – assigned to active roles and responsible for modeling that portion of the processes in which their roles participate. They develop measurements of the processes and communicate the results by identifying conflicts and inefficiencies with peers and coordinators.

\- Peer agents – validate the process definitions of the development agents, for whom they are assigned active roles and thus are proxies for the development agents.

The coordination team documents the execution plan. The plan and its diagrams provide a framework that describes the responsibilities and the scope of the individual process modeling activity that must be performed. The plan must then be approved by all participating agents and stakeholders.

## 3.3. Description and conflict resolution

The goal in this phase is to design a complete and consistent set of role-process descriptions. If necessary, the coordination team provides orientation sessions for agents who can then start modeling any of the processes and the roles to which they are assigned. All development agents start their description by identifying the operations of the roles for each process in which they participate. Fig. 6 gives examples of operations provided by roles in connection to their processes.

Conceptually, there is a hierarchical relationship between processes, operations, and activities representing a different abstraction level in the context of the process. It contains a set of role operations, which have atomic activities describing how that role performs the operation.

In addition to data dependency relationships, there are structural relationships between roles (e.g., aggregation or generalization). Fig. 7 gives the operations of the author role and two other roles that inherit its operations. For example, based on this definition, the change manager role, in any of its processes, may perform the initiate review operation, which is inherited from the author role.

For each of its operations, the role has a description of the behavior of the operation in an individual role-process diagram. In particular, an agent describes; the activities performed by its role, the information items it requires while performing the activities, and its outputs. This forms the role’s context. In addition, agents provide the sources of the inputs and destinations of the outputs, if any. The sources might be other roles or items, such as project repositories, folders, software tools, or other operations of the same role. Agents also represent the activities their roles perform with other roles.

![](/api/attachments/SR8VH6A5/fulltext/images/96be4ea0ebfd9809e2952d4ffca3884c6f710d6d4169e2e8c2a7a1f77ce98e67.jpg)  
Fig. 5. An excerpt from a role diagram.

In Plural, the notation used for describing the behavioral aspects is based on Event-driven Process Chain (EPC) technique, which is semi-formal and used in capturing and understanding processes for discussing business requirements and process improvement initiatives with process owners [13]. Its main constructs are functions and events. An event can trigger a function or a function can produce an event, and combinations of events and functions in sequence produce event-process chains. To represent control relationship between triggering events and functions, logical operators are used. Aspects regarding processed data and organizational structures are also represented in EPCs.

![](/api/attachments/SR8VH6A5/fulltext/images/c382e7520273dbe244d6f6a653f4090eb92ff5160e0cea31ca6924e514544a21.jpg)  
Fig. 6. Examples of role operations.

Fig. 8 shows an example of an individual role-process diagram constructed in one of our case studies. The example shows the prepare review operation of review team leader role in the review process. The diagram has swim-lanes (columns) and the role has a primary swim-lane in which the activities performed by that role are shown.

Such models are consistent with a role’s expectations if, in the models of the other roles, the expectations are acknowledged and shown at the expected interface. For example, the review team leader expects to receive the review request, the partly filled review record (review record – 1st section filled) and the product to be reviewed from the author role as inputs in order to service the operation. This expectation is considered ‘satisfied’ if the author role, in any of its operation model, declares that it sends these items to the review team leader. Otherwise, there is an inconsistency between the expectations of these two roles.

![](/api/attachments/SR8VH6A5/fulltext/images/8a7ad17930bb6444f5df16f8bd5f741a59bfc82811cbb8a74e222f9c133e1f6a.jpg)  
Fig. 7. Role operations and inheritance relationship between roles.

![](/api/attachments/SR8VH6A5/fulltext/images/95b07e7a4e0a0ce6af97d98a95f56ba5708771f4dc5dc4369bd510808106b614.jpg)  
Fig. 8. An individual role-process diagram for the prepare review operation of the review team leader role.

Plural allows participants to develop and maintain their own ontology or data dictionary by aligning their terms with those used in the external environment. This is made possible by using UML class diagrams for presenting generalization and aggregation relationships between items available in the domain.

An inconsistency in this approach represents a contradictory expectation that may exist between individual role-process diagrams. These models are inter-consistent if all interacting roles fulfill their mutual expectations. Thus, an inconsistency is an unsatisfied expectation and we presume that there is an inconsistency between two individual process models if the interaction modeled by one role is different from that modeled by another. Unlike most approaches, Plural performs consistency identification and resolution concurrently during the description of the processes. Furthermore, development agents can check expectations of other roles from their roles before they start modeling their parts. The aim is towards avoiding inconsistencies before they are created by the agents and, in turn, saving time for rework and consistency resolution.

In general, agents try to uncover the primary rationale of the others in defining a specific expectation or why the expectation is not being fulfilled by others. These interactions are one of the primary ways for agents to uncover concealed assumptions and share a common understanding. If both sides insist on their position, they must negotiate and resolve conflicts. With an agreement, agents change or re-model their activities in order to reflect the solution and provide consistent expectations in the individual models. Resolution is the agents’ responsibility.

Inter-consistent and complete individual descriptions are validated by peer agents and verified by the coordination team. Peers ensure that role’s process descriptions represent role’s responsibilities correctly and completely, and satisfy the role’s goals. Verification mainly involves checking models against a set of syntactic and semantic rules.

## 3.4. Integration and change

Based on the individual role-process diagrams, several diagrams that present process knowledge at higher abstraction levels can be generated. Each involves a query to the process-base that visualizes a portion of the processes from a specific perspective. A generated model is valid until a change is made to its underlying models. When a change is performed, the model has to be regenerated in order to reflect the change.

An activity-level process diagram integrates individual roleprocess models to depict all activities performed in that process at the lowest level. This requires all individual role-process model in the process to be placed side-by-side and joined by all messages that the roles exchange and the activities they jointly perform.

Operation-level process diagrams are synthesized activity-level diagrams depicting the role operations and the data dependency between them for a specific process. Fig. 9 depicts one such diagram for the review process. For example, the role operation prepare review is represented in the diagram with its inputs and outputs and its relationship with other entities within the scope of the review process.

Process-level diagrams are context diagrams at the highest level of abstraction depicting the data exchange between a specific process, roles, application systems and information stores as well as processes that extend the process or are included into it.

Dependency diagrams address the interactions. Role dependency diagrams present a set of roles and their relationship in terms of the information they exchange between them and other entities, such as application systems and information stores. Fig. 10 gives an example depicting the role dependencies for the review process covered in our case study. Process dependency diagrams depict the message exchange between processes as well as the interface to external roles and other entities. They help the organization to understand the interdependencies existing between organizational entities and the effect of changing the relationships, and to identify and compare alternatives.

During the description and inconsistency identification and resolution phase, agents can recognize deficiencies or problems due to the context. If a change is related to scope and context (i.e., the roles participate in processes and their relationships, or the processes covered and their internal relationships), agents can propose changes of context. The process group decides whether to accept or reject the changes. If accepted, the change is implemented by the coordination team. Depending on the scope and impact of the change, the process description may have to be paused and the process returned to the context definition phase.

Changes related to individual role definitions are made by the agents who are acting for that role and then it is reviewed by a peer agent and the coordinators. If a change does not affect the interface of the role, it is an alteration in role’s context and does not affect the interaction between the roles and the way they perform their tasks. If an update modifies the role’s interface (and thus its expectations), the change should either be incorporated in all related models or it should be revoked after negotiation between parties. Such cases manifest themselves as inconsistencies between expectations and resolved in the relevant models.

## 4. Research method

The utility of a design artifact must be rigorously demonstrated [6]. This involves its integration within the business environment. Observational methods, such as case and field studies, provide an analysis of the artifact within the technical infrastructure of the business environment. We considered the case study to be an appropriate strategy to investigate the application of the Plural method in an organizational setting, and to examine its utility and the implications on individuals and the organization.

First, we applied the Plural in multiple pilot case studies in order to explore its applicability, examine its drawbacks, and enhance its structure and components. We were able to apply the method in different business domains such as a university graduate school and a small-scale web design and development company. We identified several improvement opportunities as a result of these settings and components were improved. Second, we performed a case study that emphasized the utility of the Plural method on the modeling and improvement process rather than trying to measure its cost/benefit trade-off.

## 5. The case study

## 5.1. Site selection

The decentralized process modeling approach is more suitable for knowledge-oriented organizations since knowledge in such organizations is highly distributed among workers. In a knowledge-oriented organization, each worker has a specialty in which he or she maintains leading edge knowledge. Software developing organizations are examples of this type of organization. Furthermore software engineers are typically familiar with process modeling and related practices. Therefore, we assumed a decentralized approach in a software organization would be promising and performed our case study in a small software development and consultancy company.

![](/api/attachments/SR8VH6A5/fulltext/images/f876fa0896900da1746ed9f1eed7ff1733cc574c924790a46f9ba27c672402b1.jpg)  
Fig. 9. An operation-level process diagram for the review process.

The organization was established in 1999 and has currently 12 knowledge workers, 8 of whom work full-time. Their established quality system was certified as ISO 9000 compliant in 2000. Workers have graduate degrees in computer science, plus 4–12 years of field experience in software development and process improvement.

Our study group consisted of four employees all of whom participated as development agents. One of the participants also acted as the coordinator. Development agents were responsible for the role-based process description and validation of other individual models as peer agents where necessary. Except the coordinator, the participants were not familiar with the toolset and the notation used for the study, but they had a general knowledge of process modeling and related concepts.

The organization already had guidelines for process execution; these had not been formatted but were written in natural language. This made it easier to compare the original process definitions and ones developed through the Plural method. Agents participating in the case study were not involved in the definitions of the original process descriptions but as process performers they had been using these processes for more than four years based on their natural language descriptions.

![](/api/attachments/SR8VH6A5/fulltext/images/30cf69f28bee011be8c24213d0d242c61f021033fdb85beb3aaac8f930fa4dbb.jpg)  
Fig. 10. A generated role dependency diagram for the review process.

## 5.2. Data gathering

We observed the process followed by the participants for our case study. In particular, we watched and noted their activities, the difficulties they faced in following our method, and their interaction with other participants (their reaction to inconsistency and conflict). Also, during this time, all participants were asked to record a set of measures related to their work including the time spent for specific activities, such as role identification and individual modeling. After applying the Plural method, participants were interviewed to find any further benefit or difficulty observed. During the interview, they were asked to complete a questionnaire (containing 43 questions) to augment the discussion and to provide further feedback. The questionnaire was organized into four sections. The first focused on the participant’s knowledge of process modeling and the context in which the case study was conducted. The second section focused on the feelings of the agent on the effectiveness and efficiency of the method and its possible impact at the individual and organizational level. The third and fourth were designed to gather thorough feedback on their use of the Plural method and its notation, respectively. Participants filled out the questionnaire interactively, and were asked to comment on the rationale for each answer.

## 5.3. The tools used for the case study

Individual role-process models were designed using a commercial tool via a web-based environment, where the diagrams and process elements were stored in and retrieved from a central database. The tool was extended to adapt it to the specific needs of the approach. The add-on connected to the central database and analyzed the process repository to detect and present inconsistencies between individual process models. It also provided input for the integration of the models.

## 5.4. Execution of the case study

## 5.4.1. Context definition

Our study started with a meeting assembling all agents and stakeholders. After a brief orientation, the goal and objectives of the study were determined. The focus was on defining process models that facilitates human understanding and communication, particularly as a means to communicate and guide possible current and future performers. During this meeting, the study group determined the high level processes that would be covered in the study. The group then identified the processes performed in at least one type of project carried out in the organization. The training life cycle was selected; in this the company provides a set of specific courses to its customers by providing training, project management, review, configuration management and change management processes. Each process has a key behavior of the organization and expresses a goal that the organization wishes to achieve. For example, the organization performs the review process in order to decrease rework cost and increase the quality of its products.

During the next meeting the team identified the primary roles that participate in these processes and their relationship. The group focused on defining groups of tasks or functions for a particular aspect of related process rather than defining work titles or positions. The results provided a skeleton for all participants on their responsibilities and the scope of their individual process modeling activity.

The coordinator agent depicted this coverage on a scope diagram. Based on the processes covered and the roles that participate in these processes, the relationships between roles are depicted on a role diagram. Both diagrams were subjected to change during the study, specifically during the process definition. However, the minor changes did not significantly affect the scope. Each active role was then assigned to an agent in the organization. The coordinator documented and distributed a plan for the further phases of the study.

## 5.4.2. Description and conflict resolution

Before individual process modeling started, the coordinator initiated orientation meetings on the method to be followed, the toolset and the notation to be used, for all development agents. These sessions ranged a half to one hour. After this, the development agents were assigned to one or more active roles and started modeling the activities of their roles for the processes covered. For example, a development agent A (with review team leader and quality representative roles) began identifying the operations to be provided. Then, for each of these operations, agents depicted the behavior of the operation in an individual roleprocess model. Modeling started concurrently but sometimes continued asynchronously.

Each agent checked whether other roles’ expectations from his or her role had been satisfied. This check was also performed for his or her expectations from others. Fig. 11 gives a section of the list of expectations from the review team leader role.

If there was an inconsistency, such as that shown in Fig. 11, the agent either changed the description to match the other agent’s expectations or insisted on the position being enforced and communicated this with others requesting that they help solve the problem. For roles for which there was an unfulfilled expectation, the two agents discussed the underlying rationale to decide whether the expectation should or should not be changed. The coordinator moderated such interactions until all inconsistencies were resolved. Resolution was the agents’ responsibility.

We did not encounter any conflict that could not been resolved by participating agents. Significant conflicts were debated by all participants on two occasions. For these cases, agents involved in the discussion communicated, discussed the problem, and raised the issue to other agents in the organization if necessary. To justify their cases, they explored sources and shared their findings with others. For the inconsistencies caused by spelling mistakes or different naming practices, agents simply updated their definition. This was also true for items that were overlooked by agents and identified in inconsistency analysis.

Once individual diagrams were declared complete, they were validated by the peer agents and then subjected to verification by the coordinator.

![](/api/attachments/SR8VH6A5/fulltext/images/7fbc1a267791ea0ccfb31523e24f840f003078e756adb91fcc7acf0e1f65c7a1.jpg)  
Fig. 11. Analyzing expectations.

## 5.4.3. Integration and change

In this phase, the team generated diagrams depicting different aspects of the way the organization operates, thereby identifying any major flaws and helping understand the individual’s objectives and the way they communicate with others to achieve them. Diagrams were based mainly on consistent individual models and they were partially automated by the tool. The first type of diagram generated was at the activity-level, depicting the process at the lowest level of detail. In interviews, the activity-level diagram was found useful for the representation of the processes. However, agents also considered some integrated models to be too complex to follow and requested models that presented the process information in an aggregated fashion. Operation-level process diagrams served this purpose. Higher-level process diagrams depicting the process and its message interface were also generated. These revealed relationships between processes and other entities and helped agents to examine implications of making changes. This also allowed agents to note any interacting parties or information items that could be removed. Fig. 12 gives an example of such a diagram for the review process.

Other types of diagrams that presented process and role dependencies in terms of information exchange were also generated. These aggregated the information into more focused and filtered forms and helped agents see and understand the processes from several perspectives, in particular information exchanged through processes and roles. Role diagrams also make use of the aggregation relationship between roles. For example, the dependency of the review team was the combination of the dependencies of the roles of employees that constituted that team.

The application of the method was suspended in the integration and change phase, and the first modeling cycle was considered complete after all agents had agreed that the process models were complete, consistent, and stable. In a short meeting with all participants, the first cycle was announced as completed and participants’ experiences and comments were shared. At this point we interviewed participants using a structured questionnaire, which collected their observations and experience on the use of the method. We asked questions about the notation and toolset used, and whether the participants considered that the method had helped them express their knowledge about their processes.

![](/api/attachments/SR8VH6A5/fulltext/images/f14ab24eeb0d02cd53d855af038da87864c8c1968978be515d6fec083cbf697a.jpg)  
Fig. 12. An integrated process-level process diagram for the review process.

## 5.5. Findings

We had a chance to make on-site observations during and after the case study. We analyzed them to examine the way the definition evolved and the way the explicit declaration of expectations contributed to the completeness of the model.

During process description, development agents started modeling the ‘as-is’ processes. They also referred to existing narrative process descriptions. However, as they defined their expectations from others and examine other roles’ expectations, they started to identify problems stemming from ambiguous and incomplete process definitions as well as its implicit assumptions. For example, in the review process, the author, project leader and the review team leader had different expectations and understandings of the review initiation activity. Existing process descriptions also lacked the level of detail needed to guide its execution.

Another example of a conflict occurred in the review process was related to the author’s attendance at the review meeting. The author had expected to attend the to justify the case and to counter reviewers’ comments but the review team leader and review team members refused this, insisting that the meeting be performed internal to the review team.

The execution of the processes as described by them involved their tacit knowledge, which allowed them to handle ambiguities or fill gaps. By following the Plural method, they were able to reflect on how they actually performed their responsibilities. As they started uncovering and resolving such issues, and adapting their processes from others’ viewpoints, the process definitions turned into a ‘to-be’ model.

After the modeling was complete, responses to the questionnaire showed that agents strongly agreed that the modeling process gave them a better understanding of their role in the organization and that explicit modeling of their interfaces provided valuable information. They all agreed that modeling the activities they perform in the processes they participate drove them to think about the processes in greater detail. Although they noted that our method required additional effort; they found it beneficial and essential to model the exchange of information items between roles. Particularly for process guidance, role-based modeling was considered valuable and helpful, since it clearly presented the interactions and responsibilities for each role.

Agents were enthusiastic about checking their definitions against other’s expectations, analyzing inconsistencies and rapidly taking actions for its solution.

By encapsulation, information about the internal workings of a role is hidden to outside world, yet its interface is visible as expectations. Any change of internal behavior appears as an alteration to its interface. This is visible instantly and must be solved by the agent acting for this role and might require further changes to other descriptions.

During the case study, changes to the scope such as changes to role definitions were discussed and approved by the entire study group and changes were required to be made to the affected models by the coordinator.

Table 1 summarizes the effort spent in carrying out our study. In total, it took 40 person-hours of effort. The context definition phase consisted of two meetings and the work by the coordinator for modeling and documentation (10 person-hours). Process definition and conflict resolution involved 25 person-hours. Since each agent defined different portions of the processes, the effort required to model their sections was different. Agent 1’s section covered more activities, resulting in the highest value of effort committed to definition. The integration phase took considerable time (5 person-hours), but this could be reduced if the model generation and integration had been fully automated.

Table 1  
Efforts utilized and the duration of the study.

<table><tr><td># of high level processes</td><td>5</td></tr><tr><td># of development agents</td><td>4</td></tr><tr><td># of roles</td><td>18 (15 active/3 inactive)</td></tr><tr><td># of distinct role operations</td><td>48</td></tr><tr><td colspan="2">Effort (person-hour)</td></tr><tr><td>Context definition:</td><td>10</td></tr><tr><td>Definition and conflict resolution:</td><td>25</td></tr><tr><td>Agent 1</td><td>9.0</td></tr><tr><td>Agent 2</td><td>5.0</td></tr><tr><td>Agent 3</td><td>2.5</td></tr><tr><td>Agent 4</td><td>2.5</td></tr><tr><td>Coordinator</td><td>6.0</td></tr><tr><td>Integration</td><td>5</td></tr><tr><td>Total</td><td>40</td></tr><tr><td colspan="2">Duration (h)</td></tr><tr><td>Context definition:</td><td>4</td></tr><tr><td>Definition and conflict resolution:</td><td>9</td></tr><tr><td>Integration</td><td>5</td></tr><tr><td>Total</td><td>18</td></tr></table>

Based on the settings and effort utilized, it took 4 h to complete the context definition phase, 9 h for the description and conflict resolution phase and 5 h for the integration, totaling 18 h for the entire project to complete its first cycle.

We expected the Plural method to decrease in the total time for process modeling. During the conduct of the case study, we had the chance to observe development agents modeling their processes, discussing and resolving inconsistencies in parallel and autonomously. By maintaining a role based modeling approach, where role expectations are explicitly revealed; concurrency in modeling was achieved.

During process description, we observed that it is a good practice for the coordinator agents to monitor the development not only for verification purposes but also for observing any reusable process components that can be generalized. For example, each agent had a particular structure of initiating a change request in the organization. For this case, the coordinator agent proposed a generalized change request (CR) initiation procedure, based on the definitions of the development agents, to be performed by a particular role; the CR originator. The study group accepted this modification and each role initiating a change request inherited this responsibility from the CR originator role. This example also points to a dilemma on whether to let each agent to maintain its way of doing that set of activities or to establish a standard generalized way of reaching that process’ goal.

According to the answers given in the questionnaire and interviews, participants did not encounter any significant difficulties in following the method and found the notation relatively easy to learn and use. However, this response can be evaluated as being partial, given that participants were skilled in process modeling and related concepts.

## 5.6. Limitations of the plural method

The case study exposed some limitations of the method. The expected benefits were not fully realized if the processes being defined were not performed or not effectively established in the organization. For the change management process, for instance, there was a definition but the process itself was never attempted. Therefore, the agents had some difficulty and needed more guidance on their responsibilities and their goals in performing such work. The coordinator and the study group referred to existing process definition, code of practices and standards, and presented this additional information as the basis for the definition of the process by identifying primary inputs and outputs and making a brief description of what was expected from each role. For such cases, we observed that pair modeling for process definition (i.e., development agents modeling with peer agents and/or the coordinator) was an effective and a useful practice.

The organization that performed the case study had a high maturity level; both in its process stability as well as the way it considers process improvement. Our interviews revealed that the organization provided a degree of empowerment and motivated individuals to continuously improve themselves. This eased the way the approach was adopted in the organization.

The diagrams used in the Plural method have some cognitive limitations also. In essence, the trade-off between information and cognitive complexity is inherent in most visual representations. Additional information can be represented with the sacrifice of ease of perception. For some of the processes, an individual role model for an operation was too large to fit on a regular sheet of paper, revealing its complexity. The situation was complex for the some of the integrated and generated models. Similarly, a complete role dependency diagram for the organization was too complex and needed other representational techniques.

## 6. Conclusions

Use of the Plural method allows organizations to capture the perspectives of multiple agents who hold a partial knowledge of their organization’s processes. Capturing and representing process information from multiple viewpoints enables organization to capture wider and more accurate process information [4]. Studies of business process modeling and redesign suggest that the process models that are perceived as more accurate are also perceived as enabling a greater degree of redesign success than models that are less accurate [8].

Plural ensures that a role’s expectations (in the form of information flow) are explicitly defined and visible to the organization. This helps in discovering communication points and conflicts, and provides an explicit representation of unfulfilled expectations where process-level and individual objectives are not being achieved sufficiently.

By delegating the responsibility of modeling and improving processes to process owners, Plural can help to empower people and stimulate thinking about the way the processes are performed and the way they can be improved. It fosters an environment to reveal and discuss problems and establish a shared vocabulary, while allowing each individual to represent his or her own. For process improvement and redesign, it is important to make sure that employees have a roadmap of others’ positions [10]. Shared perspectives of agents, including goals and interdependencies, help organization to succeed in process definition and improvement.

Plural helps the organization to create a process-base that shows who is responsible for which activities, what information is processed by whom, and which organizational entities interact with each other. The process-base caters for the generation of various representations depicting the processes with different abstraction levels and perspectives. Such an environment allows the organization to establish a knowledge-friendly culture with openness, an innovative atmosphere, and willingness to share [7].

Plural builds a business process architecture in terms of a set of interacting and loosely coupled components, which represent the service operations of people acting for roles. Such an architecture helps to bridge the gap between business requirements and the IT infrastructure, and paves the way for translating requirements into flexible, reusable and autonomous software artifacts implemented as software services [12].

## 6.1. Limitations of the study

Our case study was performed in a relatively small size organization with a limited number of participants. Working with a small team of people co-located in the same office eased communication among team members and helped in expediting the effort. Although team members were not initially familiar with the notation and tools utilized, they had the necessary knowledge and skills to adopt the method of process modeling and this had a positive influence on the effort. In addition, the high maturity profile of the organization had a substantial impact on the success of the work. However, we have no proof yet that the approach will scale-up to be used in larger organizations with hundreds of knowledge workers spanning many large processes across the organization. This therefore results in a limitation on it generalizability.

The toolset used for the case study did not provide adequate support to the method and the add-on we have developed has its own limitations. The real benefits would be gained with a tool addressing the unique requirements of the method.

In brief, the evidence suggests that Plural method was successful in enabling decentralized business process modeling. Plural was developed as an initial method addressing the main features of our decentralized approach. Other methods built upon these characteristics can also be constructed, but currently there is no evidence that the potential benefits of decentralization will result from their use. We believe that our Plural method and its application in a particular organizational setting is an initial step towards its deployment and acceptance.

## Acknowledgements

The authors are indebted to three anonymous reviewers for their valuable and constructive comments, and to the Chairman of the Editorial Board, Professor Edgar H. Sibley, for his major editorial help. The authors would also like to thank all colleagues and friends who participated in the case studies and contributed to this work.

## References

[1] N. Baddoo, T. Hall, Practitioner roles in software process improvement: an analysis using grid technique, Software Process Improvement and Practice 7, 2002, pp. 17–31.

[2] J. Barjis, The importance of business process modeling in software systems design, Science of Computer Programming 71, 2008, pp. 73–87.

[3] L. Chang, P. Powell, Towards a framework for business process re-engineering in small and medium-sized enterprises, Information Systems Journal 8 (3), 2002, pp. 199–215.

[4] P. Darke, G. Shanks, User viewpoint modelling: understanding and representing user viewpoints during requirements definition, Information Systems Journal 7 (3), 2008, pp. 213–219.

[5] R.M. Dijkman, D.A.C. Quartel, M.J. van Sinderen, Consistency in multi-viewpoint design of enterprise information systems, Information and Software Technology 50 (7–8), 2008, pp. 737–752.

[6] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, Mis Quarterly 28 (1), 2004, pp. 75–105.

[7] B.v.d. Hooff, M. Huysman, Managing knowledge sharing: emergent and engineering approaches, Information and Management 46, 2009, pp. 1–8.

[8] N. Kock, J. Verville, A. Danesh-Pajou, D. DeLuca, Communication flow orientation in business process modeling and its effect on redesign success: results from a field study, Decision Support Systems 46 (2), 2009, pp. 562–575.

[9] M. Koubarakis, D. Plexousakis, A formal framework for business process modelling and design, Information Systems Journal 27 (5), 2002, pp. 299–319.

[10] S.C. Misra, U. Kumar, V. Kumar, Modelling strategic actor relationships for risk management in organizations undergoing business process reengineering due to information systems adoption, Business Process Management Journal 14 (1), 2008, pp. 65–84.

[11] M.P. Papazoglou, W.J. van den Heuvel, Business process development life cycle methodology, Communications of the ACM 50 (10), 2007, pp. 79–85.

[12] M.P. Papazoglou, P. Traverso, S. Dustdar, F. Leymann, Service-oriented computing: a research roadmap, International Journal of Cooperative Information Systems 17 (2), 2008, pp. 223–255.

[13] J. Recker, M. Rosemann, M. Indulska, P. Green, Business process modeling – a comparative analysis, Journal of the Association for Information Systems 10 (4), 2009, pp. 333–363.

[14] W.N. Robinson, S. Purao, Specifying and monitoring interactions and commit ments in open business processes, IEEE Software 26 (2), 2009, pp. 72–79.

[15] M.P. Singh, A.K. Chopra, N. Desai, Commitment-based service-oriented architecture, Computer 42 (11), 2009, pp. 72–79.

![](/api/attachments/SR8VH6A5/fulltext/images/7c64683dfa11bd728ecb7ecafbc54527b2d10a3e0adc8e8ac8d9973d7ea26fee.jpg)  
Oktay Turetken is currently a researcher at the European Research Institute in Service Science (ERISS) Tilburg University. He holds a Ph.D. in Information Systems from Middle East Technical University. Hi research focuses mainly on business process design analysis, and compliance, software project management, and software measurement.

![](/api/attachments/SR8VH6A5/fulltext/images/44c1688bd7f1f1c740181ef35ab513c9f7fbcce1c120bb74848c02dd8f20129e.jpg)

Onur Demirors has been working in the domain of software engineering as an academician, researcher and consultant for the last 20 years. He has Ph.D. and M.Sc. degrees in Computer Science from Southern Methodist University. His work focuses on software process improvement, software measurement and prediction, software project management, software engineering standards, and business process management. He is the director of the Software Management program at Middle East Technical University and the strategy director of Bilgi Group (www.bg.com.tr).
