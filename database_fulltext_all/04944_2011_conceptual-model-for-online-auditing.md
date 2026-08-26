---
otero_id: 4944
otero_key: "T2F2YKKY"
title: "Conceptual model for online auditing"
authors: "Wil van der Aalst; Kees van Hee; Jan Martijn van der Werf; Akhil Kumar; Marc Verdonk"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conceptual model for online auditing

Wil van der Aalst <sup>a,</sup>⁎, Kees van Hee <sup>a</sup>, Jan Martijn van der Werf <sup>a</sup>, Akhil Kumar <sup>b</sup>, Marc Verdonk <sup>c</sup>

<sup>a</sup> Department of Mathematics and Computer Science, Technische Universiteit Eindhoven, P.O. Box 513, 5600 MB Eindhoven, The Netherlands

<sup>b</sup> Smeal College of Business, Penn State University, University Park, State College, PA 16802, United States

<sup>c</sup> Deloitte, The Netherlands

## a r t i c l e i n f o

Available online 19 August 2010

Keywords: Information assurance Auditing Architecture Conceptual model Constraints Business rules Conformance checking

## a b s t r a c t

The independent veri<sup>fi</sup>cation of the right applications of business rules in an information system is a task for auditors. The increasing complexity of information systems, and the high risks associated with violations of business rules, have created the need for Online Auditing Tools. In this paper we sketch a conceptual design for such a tool. The components of the tool are described brie<sup>fl</sup>y. The focus is on the database and the conformance checker, which are described in detail. The approach is illustrated with an example and some preliminary case studies from industry.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Organizations are constantly executing business processes to achieve their goals [9,25]. These business processes need to be executed within certain boundaries. These boundaries are de<sup>fi</sup>ned by business rules coming from different sources. Some rules are enforced by law and the authorities, and others by the shareholders. But contracts with business partners like customers and suppliers also create boundaries. Moreover, the board of an organization itself de<sup>fi</sup>nes boundaries, e.g. in a code of conduct. Note that “staying within the boundaries” involves much more beyond avoiding fraud. So we consider fraud as an example of rule violation and therefore we do not treat it separately.

Information systems play a major role in executing the business processes, either in cooperation with employees or autonomously. This results in the need to implement business rules in both the information system and through operating instructions carried out by employees. As information systems become more and more complex, in many situations it gets very hard to manage the whole system. Since the management of an organization is responsible for the execution of the business processes, and accountable for staying within the boundaries, there is a need for checking whether the business rules are being followed on a continuous basis. Management has the prime responsibility to assess the operating effectiveness of “their” business rules, and must monitor the execution of the business processes closely. Independent veri<sup>fi</sup>cation is also needed. This is typically the job for auditors who provide assurance to stakeholders. Auditors can be either internal or external. An internal audit veri<sup>fi</sup>es adherence to both the internal and external boundaries (and can focus on both effectiveness and ef<sup>fi</sup>ciency of the processes and the business rules), whereas an external audit typically only focusses on the adherence to external boundaries and the effectiveness of processes and business rules. Of course, all auditors should be independent in their research approach and in their judgement.

For <sup>fi</sup>nancial statements a financial audit is performed by the CPAs (Certi<sup>fi</sup>ed Public Accountants). They verify if <sup>fi</sup>nancial statements of organizations are in accordance with external boundaries like the Generally Accepted Accounting Principles (GAAP) and Sarbanes Oxley (SOX) legislation. But business rules concern much more than the <sup>fi</sup>nancial reporting process and, therefore, there are numerous types of audits, e.g. ISO audits, food safety audits, Basel2 audits, information security audits, and operational audits. One aspect all audits have in common is that they often are very laborious and expensive. Moreover an audit always looks at a period in the past to determine if the business rules were adhered to in the period under review, while the management's main interest lies in the future.

In the ideal situation we would have a continuous auditing process that gives us real time insights into violations of business rules [13]. Clearly this is not feasible if done manually. Therefore, there is an urgent need for better techniques and software tools that make it possible to check arbitrary business rules automatically and in near real time. One of the approaches used today is to embed controls in the information system. A control is an automated task in the information system aimed at the prevention of violations of certain business rules. These controls are strongly related to the functions of the information system. Often business rules are generic, i.e. not bound to a speci<sup>fi</sup>c business context. An example is the “four-eyes”

principle that requires that “two tasks for the same case should be handled by different agents”.

It may seem paradoxical that another information system is needed to check the <sup>fi</sup>rst one. However, that is what we propose since the information systems themselves become too complex and thus require oversight. Our solution is not a type of theorem prover that veri<sup>fi</sup>es if the code of the information system correctly implements the business rules. Since people and organizations cannot be formally speci<sup>fi</sup>ed and may deviate at runtime, we envision a separate system that monitors the relevant activities of the information system and which independently checks if these activities conform to business rules. We call such a system an Online Auditing Tool or OLAT for short. Consequently, the information system should be equipped with a logging mechanism and the OLAT should be connected to the information system. The envisioned OLAT can work in two modes: it can report violations of business rules in the form of a report to the management of the organization, or it can send a message to the information system that can be used to exercise a control. Thus, the OLAT can also be considered as an external control mechanism for the information system. In the latter mode we have to be careful since it appears as if the OLAT becomes part of the information system, and therefore it could loose its independent status. However, the OLAT tool is only used to detect a (potential) violation and this information can be used in the information system to prevent the violation or to enact a compensation action. Although some techniques already exist to automate small parts of the audit process, a system integrating these techniques does not yet exist.

In this paper we sketch a “full blown” OLAT. This paper shows the possibilities and capabilities of such a tool, and gives insights into the architecture and functionality of such a system. Some components do not yet exist, and are ill-de<sup>fi</sup>ned, or even speculative. Although we call the tool set “online”, we do not mean they are all active in a real time mode. Only the conformance checking can be done in real time. However, the structure of the OLAT allows for reporting on a regular basis, thus providing near real time information.

At the outset it should be clari<sup>fi</sup>ed that, rather than focussing on modeling techniques for data and processes, instead we focus on the architecture of a system that can handle any business process. Considerable previous work has already looked at approaches for modeling business processes. Therefore, we place more emphasis on development of a meta model that encompasses process, business data and organizational aspects along with the runtime issues. In particular, we are interested in modeling those aspects of an organization that are relevant for the business rules to be monitored. However, we need certain techniques or approaches in order to express and check the business rules. Therefore, we present in Section 2 some basic techniques for data modeling, process modeling and the language to express business rules. In Section 3 we de<sup>fi</sup>ne the concepts that are related to auditing in an informal way. In Section 4 we give a high-level architecture of an OLAT, and also describe software components for which we do not have a concrete solution yet. In Section 5 we describe a conceptual data model for the OLAT. In Section 6 we study the business rules in detail. We have chosen to be as language independent as possible. Therefore we use standard predicate calculus to express these rules. Section 7 gives a concrete example to illustrate our approach. In Section 8 we describe practical experience with the business rule evaluation in some real life cases. Section 9 discusses related work and <sup>fi</sup>nally, the last section gives a conclusion and our plan for future work.

## 2. Preliminaries

Here we explain techniques for data modeling, process modeling and the predicate language to express rules. Although the focus of this paper is on the architecture and meta modeling of our OLAT tool, we need these techniques to illustrate the use of the tool. As we prefer to be as independent as possible from industry languages, we use plain predicate calculus for the business rules. Note that we do not intend to present a new modeling approach, rather we need a consistent combination of different modeling frameworks. For modeling approaches a large body of literature exists already, cf. [9,2].

## 2.1. Petri nets

For modeling of business processes we use Petri nets [2]. A Petri net consists of transitions (drawn as squares) which represent tasks that can be performed in a process, and places (drawn as circles), which de<sup>fi</sup>ne the conditions for a transition to be executed (or “<sup>fi</sup>red”). Places and transitions are connected by arcs. Places that have an arc to (from) a transition t are called the input (output) places of t. The state of a Petri net, also called a marking, is a distribution of objects, called tokens, over the places. A transition is enabled if in each of its input places there is at least one token. In that case it can fire which means that it consumes a token from each of its input places and produces a token in each of its output places. The behavior of a Petri net is characterized by the set (in fact graph) of markings that are reachable by transitions from an initial marking.

## 2.2. Data models

A database consists of entities, i.e., the elements or records stored in tables. All entities together form an instance of the database. The <sup>fi</sup>elds of a table are called the attributes of the entity, and are related by associations. On the schema level, entities belong to an entity type, associations belong to a relationship. The entity type also de<sup>fi</sup>nes the type of attributes of an entity. An Entity-Relationship diagram (ERD) [14] describes the type of various entities and the relationships between them. Entity types are drawn as rectangles. Inside the rectangle, the entity type is given, together with its attributes. Relationships between pairs of entities are drawn by arcs connecting them, with a diamond in the middle. We consider only binary relationships and most of them are functional relations.

A functional relationship can be represented as a function from one entity type to another. For functional relationships we drop the diamond, and represent them directly by an arc from the source entity type to the target entity type. We also distinguish between a total function and a partial function. A total function is one in which every element of a domain has a mapping, while in a partial function some elements are not mapped. For notation purposes, if at the arrow head a vertical bar is drawn, the function is total, i.e. for all instances in the entity, the function returns an instance of the associated entity. Otherwise, it is a partial function. A non-functional relation is a manyto-many relation, or a set-valued function. For non-functional relationships we use the standard diamond notation where the arrow indicates the direction of the relation. A relationship is uniquely identi<sup>fi</sup>ed by the source entity type and the name of the relationship. That is, names for the relationships are only unique for the source entity; from the context it is always clear which relationship is intended.

Consider the data model of Fig. 1. Here, there are three entity types: ‘Task’ with attribute ‘name’, ‘Process’ and ‘Transition’; two functional relationships: ‘h’ and ‘f’; and a non-functional relationship ‘tp’. The arrow on relation ‘tp’ indicates that tppTask × Process, i.e., ‘tp’ is a many-to-many relation between ‘Task’ and ‘Process’. The functional relation ‘h’ is partial, and it points from ‘Transition’ to ‘Task’, indicating that each entity of ‘Transition’ is connected to at most one entity of ‘Task’. The functional relation ‘f’ is total, i.e., every ‘Transition’ is connected to one ‘Process’.

![](/api/attachments/T2F2YKKY/fulltext/images/cf0173c8e30583cb589119c5cbfa264b137c70a65bb368b760744a1653b9dfef.jpg)  
Fig. 1. A simple data model.

If in a database instance two entities x,y are in a relationship r, we write $( x , y ) \in r .$ If r is a functional relationship from x to y, we write r $( x ) = y$ for $( x , y ) \in r$ . For example, we can formalize the constraint that states that if two entities of type ‘Transition’ have an association to the same entity of type ‘Task’ and to the same entity of type ‘Process’, these entities are identical to the following formula:

$$
\forall t _ {1}, t _ {2} \in \text { Transition }: (h (t _ {1}) = h (t _ {2}) \land f (t _ {1}) = f (t _ {2})) \Rightarrow t _ {1} = t _ {2}.
$$

Note that $h ( t _ { 1 } )$ indicates the unique entity that is related to t<sub>1</sub> by the functional relation h. So $h ( t _ { 1 } )$ is a term that can be used in a comparison operation, as in $h ( t _ { 1 } ) = h ( t _ { 2 } )$ above.

Most predicates can be translated into standard SQL (cf. [29]), all predicates can be checked using SQL augmented with stored procedures. In this case, the query would be: <sup>SELECT</sup> <sup>\*</sup> <sup>FROM</sup> Transition t1, Transition t2 WHERE t1.Task = t2.Task AND t1.Process = t2.Process AND t1.Id <sub>bN</sub> t2.Id<sub>. If the result of this</sub> query is empty, then the constraint holds. This provides a practical approach to implement a conformance checker for business rules: translate the rules into SQL queries and if they evaluate to the empty set, the rule holds.

## 3. Concepts

An auditor will look for assurance that the business processes have performed within the boundaries determined by the business rules, by either auditing the design, i.e., the implementation and effectiveness of controls, or by looking substantively at the data generated by the system. The last approach is considered as very costly if done in the traditional way. We propose a new and ef<sup>fi</sup>cient way for substantive data checking. Our proposal is to do it for speci<sup>fi</sup>c business rules only, in an automated way and in near real time.

Since the audit applies to a business process, we brie<sup>fl</sup>y review the basic process terminology (cf. [2]). A business process is a collection of tasks with (potentially complex) coordination requirements among them. A task represents a set of activities in the real world that is considered as one atomic action performed by an agent, or it is automated. A task is uniquely associated to a business form which is a collection of entities.<sup>1</sup> An instance of a business process is called a case. A case has its own case data associated with it and is stored in a database. When a task is executed for a speci<sup>fi</sup>c case, its case data is shown. In the business process a task can be any kind of activity, however in the information system the execution of a task is limited to reading, writing or updating these entities. As a task <sup>fi</sup>nishes, the coordination requirements determine the set of tasks that can be executed. Eventually, when no tasks are executable for a case, the case is closed. The modeling of business processes as Petri nets is very well understood and supported by tools (cf. [2]). Remember that we only model those aspects of business processes that are relevant for the business rules we are interested in.

Agents usually work in a certain role. A role is a generic identi<sup>fi</sup>er for a category of agents in an organization, e.g., a manager, director, vice-president, etc. are all generic roles. Thus, agents Joe and Mike might be managers, Sue a vice-president, and so on. We further assume that roles are organized in a hierarchy (i.e. a tree) in which the CEO is the top node, and each link between nodes represents a bossemployee relation. In general, every organization has a different hierarchy. There are different ways in which agents can be assigned to roles, but for now we will assume that an initial assignment of agents to roles is given. An agent a can grant a permission to agent a to perform (a) a speci<sup>fi</sup>c task, (b) all tasks belonging to a process, (c) all tasks belong to a case, or (d) a speci<sup>fi</sup>c task belonging to a speci<sup>fi</sup>c case. The agent is only allowed to grant a permission if it has the permission itself, either by its role, or through a permission obtained from another agent.

Certain tasks are used to detect or prevent violations of business rules. These tasks are called controls. There are different types of controls and many different ways of classifying them. For the purpose of this research we will classify them in the way they are used to respond to an exception that occurs on a business rule.

1. Detective: this type of control is only able to detect that a violation to the business rule has occurred. An example: an employee has just transferred \$ 1 million to his account.

2. Corrective: this type of control is like the detective control, but has the added functionality to (or attempt to) correct the violation to the business rule directly. An example: an employee has just transferred \$ 1 million to his account and the control is preparing to transfer it back.

3. Preventive: this type of control prevents business rules from being violated. An example: In the current payment run an amount of \$ 1 million is going to be transferred to the bank account of an employee, but the payment run will not be processed for this reason. A special case of preventive controls is a prospective control, which gives a warning if it is possible to break a business rule based on other actions performed.

We consider only two kinds of events: a task event and a permission event. The <sup>fi</sup>rst is the execution of a task, the second is the granting of a permission.

## 4. Top-level architecture

In Fig. 2 the top-level architecture of the OLAT is presented. We distinguish data sets (displayed by drums) and program modules (displayed by rectangles). Some of these modules already have an implementation in tools like ProM [6]. However, to our knowledge, no tool exists that integrates these techniques into a single information system for auditing purposes. Note that we have more modules in the architecture than we actually will describe in detail. In this paper we only focus on the conformance checker and the risk interpreter. For the other modules we only give a high-level speci<sup>fi</sup>cation.

The data sets form the database of the OLAT. The conceptual model of the database is presented in the next section. The database consists of three types of data: Run time data, de jure models, and de facto models. The run time data is collected from the monitored information system. The de jure models are the of<sup>fi</sup>cial models of the desired organization. In fact, the run time data should conform to the de jure models. Otherwise, it indicates a violation. The de facto models are derived from the run time data by discovery techniques and can differ from the de jure models.

## 4.1. Run time data

This data comes from the information system. All (relevant) events of the information system are recorded in the system log. So the run time data concerns the events in the business processes such as activities or tasks, and events in the authorization processes such as the granting of permissions. This data is needed to perform analysis by the conformance checker, difference analyzer and potential risk detector.

![](/api/attachments/T2F2YKKY/fulltext/images/96103c44650b2d55918540feb4b72fa04b70fdfe0732b5b71cceafe6cbc0035d.jpg)  
Fig. 2. A top-level architecture of an Online Auditing Tool.

## 4.2. De jure and de facto models

The de jure models describe the desired or of<sup>fi</sup>cial situation, whereas the de facto models are derived from the run time data, and thus describe the actually observed situation and behavior. The de jure models are made for the design of the information system. Both the de jure models and de facto models concern process models with tasks and their ordering, business data together with the forms data of the tasks, and the organizational data with the agents and their roles. Last, but not least, business rules are also a part of de jure and de facto models. Business rules are expressed in standard predicate logic. Except for the business rules, these other data sets are collected in one (relational) database as the de jure models describe the desired or of<sup>fi</sup>cial behavior, business rules in the de jure models should not be violated. On the other hand, business rules in the de facto models are discovered as will be discussed later. The de jure models are loaded from the information system, while the de facto models are obtained by discovery techniques. Hence, they may be less complete than the de jure models. The de facto and de jure models share the same database schema as presented in the next section (see Fig. 3).

## 4.3. Conformance checker

This module checks whether the run time data conforms to the de jure models, in particular the de jure business rules. This does not only include the control <sup>fl</sup>ow behavior, but also data <sup>fl</sup>ow, authorizations and business rules. Since the business rules are expressed in predicate logic, they can be translated into queries (cf. [29]). The queries run on the database (i.e. the de jure models plus the run time data). If the result of the query is the empty set, the rule is not violated. If a rule is violated, an exception report is generated based on the returned query containing the counter examples. This exception report needs to be analyzed by management and auditors, and can lead to either a remedial action, or to the conclusion that the situation should be allowed. In the latter case, the Rule Promoter can be used to add the newly discovered model to the de jure models. This conformance check, i.e. by executing the translated queries, can be run at any time, thus providing a way to continuously audit the system.

## 4.4. Discovery programs

In contrast to the conformance checker, discovery programs try to derive models out of the run time data. Many kinds of existing data mining and process mining techniques and tools can be used to discover not only the control <sup>fl</sup>ow, but also the authorization rules, business data models, organizational models and business rules [3,30,31]. In general, mining techniques try to deduce patterns and rules from facts. In our case the facts are stored as events in the run time data set. To discover a process model we look at the actual execution order of tasks for the cases, and from this we can infer a process structure (for example a Petri net) (cf. [5]). For the structure of business data we could look at data as business forms that are used in the events to derive entities and relationships. For organizational models, we can look at the permission events whereby an agent grants a permission to another agent. As these rules are derived from the run time data, the models obtained by discovery are de facto models. While detailed discussion of these techniques is beyond the scope of the current work, the kind of tools we have in mind is included in the well-known process mining toolset ProM [6].

## 4.5. Rule Promoter

This module represents functionality to convert a discovered de facto model into a de jure model, and in particular it concerns business rules. For this, it needs to be able to abstract from the speci<sup>fi</sup>c instance information. In the <sup>fi</sup>rst run, the module is used to tune the con<sup>fi</sup>guration of the de jure models to the actual situation. Later on it may be part of a continuous improvement process; e.g. when exceptions are discovered, analyzed and accepted, they are added to the de jure models, thus eliminating ‘false positives’ in the conformance checker.

![](/api/attachments/T2F2YKKY/fulltext/images/f0dc5bfaed1beef1c8f546171d175f3c1ba0da59ebf5652ed53a8735f8cc3aba.jpg)  
Fig. 3. Conceptual model for OLAT.

To the best of our knowledge, there are no methods or software for this task available today. Therefore, we assume this to be a human task.

## 4.6. Risk Interrupter

The Risk Interrupter takes input from the de jure models and the run time data in a way similar to the conformance checker. The difference is that this module interrupts the information system to prevent further processing of the case under consideration until issues are resolved and the risk is mitigated. Hence, it serves as an external guard for tasks in an information system. In fact, it can be seen as an external control based on the conformance checker.

## 4.7. Difference analyzer

The difference analyzer compares the de jure and de facto models. It also checks whether business rules, process models and organization structure are in con<sup>fl</sup>ict between the de jure and de facto models. This can be seen as a quality check for the models, and therefore a check for the functioning of the whole concept. Prototypes of such a tool have been designed [17].

## 4.8. Potential risk detector

This module is able to detect potential risks by analyzing the run time data, the de facto and the de jure models. For instance, if the de jure and de facto models differ, we could use it to see if a violation of a de jure business rule could occur. This information is considered as a warning. In the ProM toolset [6] several tools are available that could be used to realize this module.

## 4.9. Remarks on the implementation of the OLAT

We do not consider the implementation of the OLAT in detail in this paper. However we note that the heart of the OLAT is the database that contains all data. The conformance checker as well as the Risk Interrupter, can be based on a standard SQL engine. So the part of the system we focus on, can be realized using a standard database management system. Of course, the OLAT needs coupling with the information system to collect events from it, and also perhaps to send interrupts to it. It also needs a reporting facility. Since we aim at a generic OLAT we should be able to con<sup>fi</sup>gure the OLAT for speci<sup>fi</sup>c information systems, but this involves the construction of a standard data-intensive application. For the other modules, like the discovery programs, we might use existing tools that can query the database. Hence, the implementation is a serious engineering effort, but it does not require new scienti<sup>fi</sup>c insights.

## 5. Conceptual model

The heart of the OLAT is the database. This section describes a conceptual model for all the data sets needed for the OLAT. The conceptual model shown in Fig. 3 is actually a meta model in that it integrates the high-level modeling elements of the organization de<sup>fi</sup>nition, business data de<sup>fi</sup>nition and process de<sup>fi</sup>nition, along with a run time framework. These aspects are described at length next. In addition, there are consistency constraints that should hold for any organization. These constraints are explained in detail in Section 5.2. Note that if these constraints are violated, the database becomes inconsistent, which is not the same as a violation of a business rule. Conformance of business rules is then treated in Section 6.

## 5.1. Data model

Fig. 3 depicts the conceptual model. It is arranged into four components: the process de<sup>fi</sup>nition, the business data de<sup>fi</sup>nition, the organizational de<sup>fi</sup>nition and run time. We <sup>fi</sup>rst explain the conceptual model, and then show how, using predicate logic, all kinds of business rules can be formulated on this model. Remember that we do not distinguish between the de jure and de facto models here: they share the same data model. Also, note that we sometimes introduce transitive closures of relations $( \mathrm { i } . \mathrm { e } . , h ^ { \ast } , u ^ { \ast }$ and pred ). These transitive closures are assumed to be updated explicitly in the database, which is easy to perform. We use them to avoid recursive de<sup>fi</sup>nitions in constraints (i.e. queries), thus allowing us to implement the conformance checker with an SQL engine.

## 5.1.1. Business data definition

Processes involve business data, e.g., entities like invoices, products and customers. To describe the type of business data and the relationships between these data elements, we introduce the business data de<sup>fi</sup>nition. It stores the entity types of business data and the binary relationship between them. In fact, this component stores general data models as introduced in Section 2. However, we link them via form links to tasks.

## 5.1.2. Process definition

The process de<sup>fi</sup>nition component describes the processes monitored in OLAT. Note that we store the process models in the form of a data model. A process contains tasks that can be executed for that process. Processes are often hierarchical. Parts of the process are either reusable, or are re<sup>fi</sup>ned using subprocesses. In our conceptual model, this is modeled by relation u. If two processes x and y are related via u, then process x uses process y, i.e. y is a subprocess of x. To avoid recursion and to be able to use queries, we also store the irre<sup>fl</sup>exive transitive closure of u in a relation named $u ^ { * }$ . Tasks can be shared by different processes. As stated earlier, a task is identi<sup>fi</sup>ed with a form providing the necessary data to execute that task.

A task typically reads and writes entities. The entity FormLink models the relation of the entity types that are used in a form to perform a task. Its attribute type de<sup>fi</sup>nes whether the entity is read, written or both. To express conditions on the order in which tasks occur, we use labeled Petri nets. A transition is labeled with the process (relation f) and the task (relation h) it represents. The conceptual model allows that transitions which are connected via a place, do not need to be in the same (sub) process. However, we assume that all places connected to a transition belong to the same process. In this way, places can be shared by two or more processes, thus providing the possibility to de<sup>fi</sup>ne process composition, rather than only <sup>fl</sup>at processes. The initial tokens of a place are an attribute of the place. It should also be noted that although we use labeled Petri nets, any other process notation could be used to de<sup>fi</sup>ne the order in which tasks can occur. Moreover, we have no direct run time information of the <sup>fi</sup>ring of transitions or the marking of a place. However it is possible to derive this information if h is a bijection (see e.g. [30,31]).

## 5.1.3. Organizational definition

Tasks can be executed by different roles that are placed in a hierarchy. If a role is higher in the hierarchy, it means that this role can execute all the tasks of its subordinates. The hierarchy is expressed using relation h: if a and b are related by h (i.e. $( a , b ) \in h$ in the instance) then b is the supervisor of a. Again, we add the transitive and re<sup>fl</sup>exive closure of the hierarchy relation, h\* .

Agents are assigned to roles via an Assignment. This assignment can be for all processes or for a single process, which is depicted by the optional relation p. The entity Assignment has start and end attributes to indicate the interval in which this assignment holds.

## 5.1.4. Run time

The run time component stores all events and associated data from the information system. There are two types of events: events that indicate that something has been done for a speci<sup>fi</sup>c task (the entity Event in the model) and the granting of permissions by agents (the entity Permission). The data associated with an event is business data, i.e. the content of the forms <sup>fi</sup>lled in. The entities Entity and Association store the business data de<sup>fi</sup>nition. Each Entity belongs to an entity type. An Association associates two entities and belongs to some Relationship.

A Case is an instance of a process, and it proceeds through Events that are raised whenever a task is executed. An event is always executed by some agent for a task in a process. The event occurrences form a partial order represented by the relation prev. The relation pred is the transitive closure of relation prev, and is used for formulating business rules. Typically, an event for a task in a case also involves entities in the business data which are created or updated. This information is stored in UpdateEntity. Entity contains the latest version of the entity, UpdateEntity stores the changes.

If an agent A authorized another agent B to perform a part of its work, then agent B acquires a Permission from agent A to perform some work. A permission is always for a time interval and it can apply to a role, a process, a case, a task, or any combination of thereof. By obtaining a role permission, agent B can perform all tasks of that role, given that A has that role in the <sup>fi</sup>rst place. A permission can also apply to a speci<sup>fi</sup>c process or case, indicating that agent B can do anything A can do for that process or case. If the permission is for a task, agent B can execute that task as well. A permission is only allowed if agent A has the proper permissions for the work it delegates. Note that one cannot always detect in which role an agent executes a task, only whether it has the right authorization.

## 5.2. Constraints on the data model

There are two types of constraints that can be de<sup>fi</sup>ned on the process model: logical consistency constraints which do not depend on any business context, i.e. constraints to maintain the consistency of the data model, and conformance constraints which ensure the conformance of the data model within the business context. There is a simple distinction between the two: Consistency constraints do not use any speci<sup>fi</sup>c attribute value, while business rules do. The latter are described in the next section. For the business data, there are no separate constraints, as it is a general schema for an ERD. In the remainder of this section we explain some of the most important consistency constraints. We classify the constraints according to the component of the entity types they address.

## 5.2.1. Consistency constraints for the process definition

The conceptual model allows for subprocesses. Although a process can be nested arbitrarily deep, cycles in the process hierarchy are not allowed. This can be expressed using two constraints. First, the relation u should be irre<sup>fl</sup>exive, i.e. a process should not depend on itself. Secondly, as $u ^ { * }$ is the transitive closure of $u ,$ and we disallow cyclic references, $u ^ { * }$ needs to be irre<sup>fl</sup>exive as well. For the purpose of discovery algorithms, we require that the task and process uniquely identi<sup>fi</sup>es a transition. This gives rise to the following constraints:

p1: Relation u<sup>\*</sup> is the transitive closure of relation u.

p2: Relations u and u<sup>\*</sup> are irre<sup>fl</sup>exive.

p3: If a transition belongs to a certain process and represents a task, the task should also belong to that process.

p4: The combination of a task and a process uniquely identi<sup>fi</sup>es a transition.

For example, p4 is equivalent to stating: if, for two transitions $t _ { 1 }$ and $t _ { 2 } ,$ their related task and process are the same, the transitions are the same. Formally:

$$
\forall t _ {1}, t _ {2} \in \text { Transition }: (h (t _ {1}) = h (t _ {2}) \land f (t _ {1}) = f (t _ {2})) \Rightarrow t _ {1} = t _ {2}.
$$

## 5.2.2. Consistency constraints for the organizational definition

Consistency constraints for the organizational de<sup>fi</sup>nition are related to the de<sup>fi</sup>nition of the role hierarchy and the granting of permissions. A permission may be granted to an agent to act in a certain role, to perform a task, or to be involved in a process or case, or any combination thereof. An agent is only allowed to give a permission to another agent for a role if that agent has the proper authorization. The agent has this authorization if either it is allowed to assume that role, or it possesses the permission explicitly. This leads to the following (non-exhaustive) set of constraints.

O1: Relation $h ^ { * }$ is the re<sup>fl</sup>exive transitive closure of relation h.

O2: The start time of an assignment is strictly smaller than its end time.

O3: The start time of a permission is strictly smaller than its end time.

O4: An agent can only grant a permission for a role, if it is assigned to that role, or if it has a permission for that role itself.

O5: An agent can only raise an event for a task in a case, if it has a role assignment to execute that task, or it has a permission to execute it.

## 5.2.3. Consistency constraints for the run time

The main consistency constraints for the run time are concerned with the correctness of events: the events should happen in the right order, i.e. the timestamp of events in the relation prev should conform to the ordering. Also, the storage of business data should be according to the schema. This leads to the following set of constraints.

r1: The relation pred is the transitive closure of relation prev.

r2: If event y occurs after event x, then the timestamp of x should be at most the time stamp of y.

r3: The source and target entities an association relates to, should be of the correct type speci<sup>fi</sup>ed by the relationship the association belongs to.

r4: If an event in a case occurs, the task related to the event should be in the process of which the case is an instance.

r5: If an entity is updated by an event, it should be of an entity type that is in the form of the task the event is of.

r6: If a permission is both for a process and a case, the process of the case should be the same process as the permission is for.

r7: If an agent performs a task, and it is authorized by an assignment, this assignment is unique.

## 6. Business rules

In this section we present business rules. Since it is in principle impossible to list all possible business rules, we only consider some characteristic examples that occur frequently. Remember that a business rule is a constraint on the data model involving business data as parameters. Therefore, we are able to express business rules as parameterized constraints. Further, note that we can check them by query processing. So the implementation of the conformance checker could be based on a standard database engine. It is not only possible to express business rules for a single process or case, but it is also possible to express business rules involving several processes or cases.

In general, business rules concern the following aspects:

• ordering based, i.e. about the execution order of tasks in cases;

• agent based, i.e. about the involvement of a role or agent in cases and processes;

• value based, i.e. in forms belonging to a task.

In business rules these aspects may be combined. In this section, we show examples for each of the aspects. In some examples we need the set of attributes Λ and the set of values V. We use the notation $e . a { = } \nu$ to express that attribute a of entity e has value v.

## 6.1. Examples of ordering based rules

Ordering based rules express constraints concerning the ordering of events and tasks in processes. Below we refer to the conceptual model of Fig. 3 for the function names which denote the relationships between various entities.

O1: Task precedence. A task $t _ { 2 }$ should always be performed before task $t _ { 1 }$ in any case of process u.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
b 1 : TaskAlwaysBeforeTask(u : Process,  $t_{1}, t_{2}$  : Task) := 
:  $\forall x_{1} \in Event : (p(c(x_{1})) = u \land t(x_{1}) = t_{1}) \Rightarrow$ $\exists x_{2} \in Event : t(x_{2}) = t_{2} \land c(x_{1}) = c(x_{2}) \land (x_{2}, x_{1}) \in pred$
</div>

O2: Restrict update operation. After task u is performed in a case, no entity of type x can be updated anymore in that case. For example, an employee cannot change the travel expense form (or entity) after it has been approved.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
b2: RestrictUpdate(u : Task, x : EntityType) :=  
    $\forall e_{1}, e_{2} \in Event : c(e_{1}) = c(e_{2}) \land t(e_{1}) = u \land (e_{1}, e_{2})$ $\in pred \land \neg (\exists y \in UpdateEntity : p(y) = e_{2} \land t(e(y)) = x)$
</div>

O3: Maximum repetitions of a task in a case. In any case of process P task u cannot be executed more than n times.

$$
\begin{array}{l} b 3: \text { LimitNrOfTasks } (u: \text { Process }, z: \text { Task }) := \\ \quad \forall w \in \text { Case }: p (w) = u \Longrightarrow | \{x \in \text { Event }   | c (x) = w \land t (x) = z \} | \leq n \end{array}
$$

## 6.2. Examples of agent based rules

Role or agent based business rules express constraints about the involvement of roles and agents in processes.

A1: 4-eyes principle. Two tasks $t _ { 1 }$ and $t _ { 2 }$ in the same case should always be executed by different agents. Below execBy is a function that returns who performed an event.

$$
\begin{array}{c} b 4: 4 E y e s P r i n c i p l e (t _ {1}, t _ {2}: T a s k) := \\ \forall x, y \in E v e n t: (c (x) = c (y) \wedge t (x) = t _ {1} \wedge t (y) = t _ {2}) \Rightarrow \\ e x e c B y (x) \neq e x e c B y (y) \end{array}
$$

A2: Mutually exclusive agents. Two agents $a _ { 1 }$ and $a _ { 2 }$ should never appear together in a case.

$$
\begin{array}{c} b   5: \text {MutualExclusiveAgents} (a _ {1}, a _ {2}: \text {Agent}) := \\ \neg \exists u _ {1}, u _ {2} \in \text {Event}: u _ {1} \neq u _ {2} \land c (u _ {1}) = c (u _ {2}) \land \text {execBy} (u _ {1}) = a _ {1} \land \\ \text {execBy} (u _ {2}) = a _ {2} \end{array}
$$

A3: Maximum tasks by an agent. An agent a cannot do more than n tasks in any case of process u.

$$
\begin{array}{l} b 6: \text { TaskLimitOnAgent } (u: \text { Process }, a: \text { Agent }, n: \text { Nat}) := \\ \forall w \in \text { Case }: (p (w) = u) \Rightarrow \\ | \{x \in \text { Event } | c (x) = w \land \text { execBy } (x) = a \} | \leq n \end{array}
$$

```txt
e1: RestrictUpdate(t11,cust-account)
e2: MutualExclusiveAgents(agent-joe,agent-sue)
e3: TaskLimitOnAgent(agent-eric,4)
e4: 4EyesPrinciple(t7,t8a)
e5: 4EyesPrinciple(t7,t8b)
e3: 4EyesPrinciple(t10a,t10b).
```

A4: Forbid agent to write. An agent $a _ { 1 }$ is not allowed to update any entity in a process u.

```txt
b7 : ForbiddenToWrite(a : Agent, u : Process) := 
    ∀x ∈ Event : (execBy(x) = a ∧ p(c(x)) = u) ⇒ 
    ¬(∃y ∈ UpdateEntity : p(y) = x)
```

## 6.3. Examples of value based business rules

Value based business rules concern the values of business data. Typically, these constraints can have the following form:

• two values should be equal,

• one value should be larger than another value, or

• a value should be within some given set (i.e. within some limits).

V1: Restrict entity-attribute-value for an agent. An agent a is not allowed to write an entity of type b with value of attribute x larger than n.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
b8 : LimitEntAgent(a : Agent, b : EntityType, x :  $\Lambda$ , n : V) :=  $\forall z \in Event, y \in UpdateEntity$ 
:  $(p(y) = z \land t(e(y)) = b \land execBy(z) = a) \Rightarrow e(y).x \leq n$
</div>

V2: Restrict entity-attribute-value for a case. For each entity of type b written in case w, the value of attribute x is lower than n.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
b9 : LimitEntInCase(w : Case, b : EntityType, x :  $\Lambda$ , n : V) :=  $\forall y \in Event, z \in UpdateEntity$ 
:  $c(y) = w \wedge t(e(z)) = b \wedge p(z) = y \wedge e(z).x &lt; n$
</div>

V3: Agent approval limit. An agent a can only perform task u for a case, if for each entity of type b written in that cas, attribute x is less than n. E.g., a bank vice-president can approve a loan up to a limit of \$500,000.

```txt
b 10 : ApprLim(a : Agent, u : Task, b : EntityType, x : Λ, n : V) := ∀y ∈ Event
: (execBy(y) = a ∧ t(y) = u) ⇒ LimitEntinCase(c(y), b, x, n)
```

Note that LimitEntinCase is de<sup>fi</sup>ned above in rule b9.

V4: Three-way match. In each case of a process n, if task u is executed, then entities of types a, b and c belonging to the case should have the same value. E.g., the price of the invoice should match the price on the quotation and on the delivery notice.

```txt
b11 : ThreeWayMatch(n : Process, u : Task, a, b, c : EntityType) := 
    ∀w ∈ Case, v ∈ Event, x, y, z ∈ UpdateEntity
    : (c(w) = n ∧ t(v) = u ∧ c(p(x)) = c(p(y)) = c(p(z))
    = c(v) = w ∧ t(e(x)) = a ∧ t(e(y) = b ∧ t(e(z))
    = c) ⇒ e(x).value = e(y).value = e(z).value)
```

## 7. Example

Above we showed how parameterized business rules are expressed in predicate logic, and checked by further transforming predicate logic into queries and running them against a database. In this way, end users and process owners are not confronted with details of predicate logic.

As an example to illustrate the framework, Fig. 4 shows the Petri net for an Administer Account Transfer process. The process starts with a customer representative receiving an account transfer instruction (task t1) from a client, who records the transfer instruction (task t2). Next, a financial clerk validates the instructions (task t3). If the validation reveals a problem, communication details of the invalid instruction are extracted (task t5). Otherwise, a financial accountant checks the transaction limit of the transaction (task t4). If the transaction amount exceeds the limit for the customer, the process starts the Authorization subprocess consisting of tasks t7, t8a and t8b. If the limit is not reached, or the transaction is authorized, the banking specialist checks the available funds. If this check fails, communication details are derived from the account unit (task t9); if it passes, the Accounting Entry sub process is started, which applies the accounting entry and calculates a fee for it. In allcases, the results are collected in a report (task t15), and after it is approved (task t16), the customer is noti<sup>fi</sup>ed (task t18). If the report is not approved, it is reworked (task t17), and tasks t15 and t16 are repeated.

This process also involves the role of the senior financial manager, who supervises the financial manager, and heads a team also including a <sup>fi</sup>nancial accountant and a <sup>fi</sup>nancial clerk. Table 1 shows the assignment of roles to tasks. Note that based on the role hierarchy, the senior <sup>fi</sup>nancial manager inherits the permission to do everything her subordinate can do.

The organization has the following agents: agent-joe, agent-sue, agent-eric and agent-beth. These agents ful<sup>fi</sup>ll the roles within the organization. In this organization, we next de<sup>fi</sup>ne the business rules that must hold for the process. First, it is not allowed to update the entity cust-account after task t11 has been executed. Secondly, agent-joe and agent-sue are not allowed to work together in any case. Agent-eric is not allowed to execute more than 4 tasks. Last, tasks t7 and t8a in a case may not be executed by the same agents, and this also applies to tasks t7 and t8b, and for tasks t10a and t10b. To set up the conformance checker of OLAT, we need to implement these business rules in the system. Given the set of prede<sup>fi</sup>ned business rules in the previous section, the process owner only has to specify the following functions:

Most of these rules apply to all processes in the system; however, it is also possible to associate a process parameter with a rule in order to apply it to a speci<sup>fi</sup>c process or subprocess.

## 8. Practical experience with business rules

As computing prices fall and data analytics becomes more affordable, there are more applications of it in auditing. The Big Four audit <sup>fi</sup>rms are all venturing into this space and embedding their principles into the audit approach. In recent years we have seen a shift from introducing more controls in the information system towards substantive data analytics and validation of business rules. The main bene<sup>fi</sup>t of this type of audit is that there is a shift from identifying the risk from violation of a business rule towards detection of the violation. In practice we still see a combination of both: a control is tested; if it fails, then the whole population of data has to be validated against the business rules. While we have not yet developed a full blown OLAT, Deloitte Netherlands used a preliminary version of it in off-line mode for the validation of several business rules on large log <sup>fi</sup>les from real information systems. We mention one example in each of the rule classes we have identi<sup>fi</sup>ed. In all cases, we could feed the log to the application and execute the queries to check the business rules in a small amount of time, thus providing an ef<sup>fi</sup>cient approach to audit a complete business process. The outcome of these cases shows that it is feasible to check compliance on a regular basis without much effort.

## 8.1. Ordering based rule

A utility company introduced the rule that invoices could only be paid if there was a valid purchase order present in the system. This rule was applicable for 3 months and was con<sup>fi</sup>gured in their system as an automated control, which we veri<sup>fi</sup>ed to work correctly.

![](/api/attachments/T2F2YKKY/fulltext/images/813d3c94e1cb57d1c12df8774df55503793558a9ceae79f8a7368b3a58297d74.jpg)  
Fig. 4. Example of an account transfer process.

However in the process an invoice was registered in the system just before it was paid and the essence of the rule was that the company wanted to prevent placing orders that were not approved through the formal process. Therefore it was decided to run the task precedence business rule O1 in Section 6.1 (“Task t1 always precedes task t2”), with t1=“PO approval” and t2=“Invoice registration”, against the complete population of invoices of these 6 months. We found that in the <sup>fi</sup>rst 3 months, a signi<sup>fi</sup>cant number of invoices were paid without a PO approval being present at all. In the last 3 months we noted that for all invoices paid a PO had been approved, but that this approval in a signi<sup>fi</sup>cant number of cases occurred after registration of the invoice.

## 8.2. Agent based rule

At a large consumer products company we found that authorizations in their SAP system allowed for booking and approval of purchase orders across business units. This was against company policy and also posed a risk for the reliability of their <sup>fi</sup>nancial statements. Using an extension of the business rule A4 in Section 6.2, “Forbid agent to write”, to distinguish between processes in business units, we found that in the total population of 1892 purchase orders there were 140 agents involved in 5 business units. The business rule held for all but one agent that was involved in a process across two business units. Further inquiry about this exception with the agent con<sup>fi</sup>rmed that our assessment was correct, but that there was a plausible explanation for this fact.

Table 1 Task-role matrix.

<table><tr><td rowspan="2">task</td><td colspan="6">Roles</td></tr><tr><td>Customer representative</td><td>Banking specialist</td><td>Senior financial manager</td><td>Financial manager</td><td>Financial accountant</td><td>Financial clerk</td></tr><tr><td>Task t1</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Task t2</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Task t3</td><td></td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td>Task t4</td><td></td><td></td><td></td><td></td><td>√</td><td></td></tr><tr><td>Task t5</td><td></td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td>Task t6</td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Task t7</td><td></td><td></td><td></td><td></td><td>√</td><td></td></tr><tr><td>Task t8a</td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Task t8b</td><td></td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>Task t9</td><td></td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td>Task t10a</td><td></td><td></td><td></td><td></td><td>√</td><td></td></tr><tr><td>Task t10b</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Task t11</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Task t15</td><td></td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td>Task t16</td><td></td><td></td><td>√</td><td></td><td></td><td></td></tr><tr><td>Task t17</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Task t18</td><td>√</td><td></td><td></td><td></td><td></td><td></td></tr></table>

## 8.3. Value based rule

At a chemical company we found that the invoice veri<sup>fi</sup>cation option in SAP (which implements the 3-way match) was set to optional. A quick sample drawn on the population showed that indeed the option had been disabled for certain purchase orders that were in the selected sample. Overruling this option poses the risk that invoice amounts, goods received and goods ordered are not in accordance, but the actual impact of this risk is hard to quantify. We used the business rule “3-way match” to verify the whole population of purchase orders based on the amount and monetary value. In this way, we were able to assess the invoices that did not pass the 3-way match criteria. These invoices were followed up, some corrections were made and credit notes requested from suppliers.

## 9. Related literature

Most business process modeling tools do not provide adequate support for information assurance and this is often added in a piecemeal and rather ad hoc manner. To the best of our knowledge there are few efforts to develop a comprehensive architecture and conceptual model for online auditing, which is an important part of our contribution. A promising AI-based approach for detecting procurement fraud is presented in [13]. A work<sup>fl</sup>ow is described in terms of pre- and postconditions that must be satis<sup>fi</sup>ed, and a violation of post conditions raises a <sup>fl</sup>ag for further investigation. While the basic objectives are similar, our goals are more ambitious since the OLAT architecture also includes organizational and data models, as well as a more extensive discovery and corrective capability.

While there are few OLAT-like holistic architectures, there has been signi<sup>fi</sup>cant research interest focussed on various vocabularies and logicbased methods for expressing business rules in the modeling of processes. Since the mid-nineties several groups have been working on techniques for process mining, i.e., discovering process models based on observed events. In [3] an overview is given of the early work in this domain. The idea to apply process mining in the context of work<sup>fl</sup>ow management systems was introduced in [7]. The Alpha algorithm was the <sup>fi</sup>rst technique able to discover concurrency [4]. Process mining is not limited to discovery. For example, in the context of ProM [6] several approaches to conformance checking were realized. The best developed technique is the

Petri net-based conformance checking technique by Rozinat et al. [31]. Here an event log and a process model are compared and deviations are measured and highlighted in both the model and log. Metrics such as <sup>fi</sup>tness, appropriateness, etc. quantify conformance and the diagnostics allow for drilling down the problem.

Conformance checking is related to checking <sup>fi</sup>tness, and measuring the quality of a process mining technique. In [20] negative events are inserted to turn process mining into a classi<sup>fi</sup>cation problem, thus addressing problems related to appropriateness [31]. Also related is the work by Cook [16], where the event streams of a process model and a log are compared based on string distance metrics. Recently, several process mining techniques have been adapted to provide operational support, i.e., process mining is not done off-line but online. Examples are the recommendations provided in [34] and the predictions given in [1]. These papers illustrate that existing process mining techniques can be used in a real time setting. However, it is impossible to give a complete review of process mining techniques here, see http://www.processmining.org for more pointers to the literature.

Further related research is discussed in [18,19]. Here the authors have developed a declarative approach for process modeling using the SBVR (Structured Business Vocabulary and Rules) vocabulary and created a new framework. The vocabulary is supported by a model and allows process modeling and speci<sup>fi</sup>cation of access constraints in an English-like language. They also support defeasible logic [28] which is a non-monotonic logic and can work with a set of inconsistent constraints. Another approach for handling compliance inspired by defeasible logic and deontic logic [8] is discussed in [32]. These logics are more advanced than predicate logic, and are based on notions of permissions, obligations and prohibitions. They are applied in the context of the Business Contract Language (BCL) [21,26] where the focus is on how to proceed when one party fails to meet its obligations. In [5], the authors have used temporal logic expressions to check whether a log corresponds to constraints.

Prior research has looked at the issue of information security from various perspectives, e.g. at the network and operating system levels. However, our focus is on security at the application level, and the stream of security related research that is relevant here pertains to role based access control (RBAC) [33]. The notion of separation of duties [24,35], although it preexisted in accounting and control systems, also reemerged in the context of RBAC as the idea that if task 1 is performed by role A, then task 2 must be performed by role B, and membership of these roles must not intersect. This is a useful framework that has now been widely adopted in popular database management systems from IBM and Oracle.

Some related work on speci<sup>fi</sup>cation and enforcing role-based authorizations in work<sup>fl</sup>ow systems is discussed in [11]. The main focus of this work is on enforcement of constraints at run time. A formal model called W-RBAC for extending RBAC in the context of work<sup>fl</sup>ows using the notions of case and organizational unit is described in [36]. The approach in [12] is based on the notions of con<sup>fl</sup>icting roles, permissions, users and tasks. More sophisticated algorithms for enforcing separation of duties in work<sup>fl</sup>ows are developed in [27]. Finally, another stream of prior work that informs our research is the literature on basic <sup>fi</sup>nancial control principles, particularly as it relates to the recent Sarbanes–Oxley legislation [10,15,22,23].

## 10. Conclusion

Currently, the work of an auditor is mostly manual, and thus very laborious. Many existing tools that can be used for auditing only focus on a small part of the actual work of an auditor. In this paper, we argued for the need for online auditing of the business processes of an organization and proposed an Online Auditing Tool (OLAT). Suchan OLAT is connected to the organization's information system but is not a part of it. The assumption is made that all relevant events in the information system are passed to the OLAT. In this way, the OLAT can build an independent image of the state of the business processes and information systems executing day to day operations. Based on this image auditing processes can run continuously. Although some tools and techniques exist, these techniques are not well integrated into a single information system.

We presented a high-level architecture of such an OLAT and studied in more detail the database and the conformance checker. We also designed a conceptual data model with a set of consistency constraints in predicate logic. The business rules are designed to realize this part of the OLAT by a standard database management system in such a way that each business rule is translated in a straightforward way into a query that can be executed against the database. For the other components of the OLAT we have referred to process mining techniques and tools. We have performed some real-life case studies with the approach using a preliminary tool, although in an off-line mode. The studies performed so far demonstrate the realizability of the approach. Together with an auditor <sup>fi</sup>rm, we are building a prototype of such an OLAT tool by integrating the currently available off-the-shelf components.

There are several aspects of this work that need elaboration. First of all, we would like to build a prototype and perform online experiments with it. Secondly we should have the ability to insert business rules from a library of prede<sup>fi</sup>ned business rule like the ones given in Section 6. This would make it feasible for controllers and other business experts to add business rules for conformance checking without the help of computers scientists, by just <sup>fi</sup>lling in the parameters. Thirdly, we plan to re<sup>fi</sup>ne the conceptual model in order to make the delegation of roles easier. We also intend to extend the conceptual model to incorporate domain speci<sup>fi</sup>c knowledge, for, say, <sup>fi</sup>nancial departments or health care systems. Finally there are several unexplored components in the OLAT architecture, such as the Risk Interrupter, potential risk detector and difference analyzer. We have some rough ideas for them, but there are many open questions. However, the most urgent activity is experimentation with a prototype, because the proof of the pudding is in the eating.

## Acknowledgements

Some part of the work on this paper was done while Akhil Kumar was visiting the Information Systems Department at the Technical University of Eindhoven. He appreciates the hospitality of the hosts. His research was funded in part by the Smeal College of Business at Penn State.

## References

[1] W.M.P. van der Aalst, Using process mining to generate accurate and interactive business process maps, BIS 2009 Workshops, vol. 37 of LNBIP, Springer, 2009, pp. 1–14.

[2] W.M.P. van der Aalst, K.M. van Hee, Work<sup>fl</sup>ow Management: Models, Methods and Systems, The MIT press, Cambridge, Massachusetts, 2002.

[3] W.M.P. van der Aalst, B.F. van Dongen, J. Herbst, L. Maruster, G. Schimm, A.J.M.M. Weiiters. Workflow mining: a suryey of issues and approaches, Data & Knowledge Engineering 47 (2) (2003) 237–267.

[4] W.M.P. van der Aalst, A. Weijters, L. Maruster, Work<sup>fl</sup>ow mining: discovering process models from event logs, IEEE Transactions on Knowledge and Data Engineering 16 (9) (2004) 1128–1142.

[5] W.M.P. van der Aalst, H. Beer, B. Dongen, Process mining and veri<sup>fi</sup>cation of properties: an approach based on temporal logic, CoopIS 2005, No. 3760 in LNCS, Springer, 2005, pp. 130–147.

[6] W.M.P. van der Aalst, B.F. van Dongen, et al., ProM 4.0: comprehensive support for real process analysis, ICATPN 2007, vol. 4546 of LNCS, Springer, 2007, pp. 484–494.

[7] R. Agrawal, D. Gunopulos, F. Leymann, Mining process models from work<sup>fl</sup>ow logs, Sixth International Conference on Extending Database Technology, 1998, pp. 469–483.

[8] G. Antoniou, N. Dimaresis, G. Governatori, A system for modal and deontic defeasible reasoning, AI 2007: Advances in Arti<sup>fi</sup>cial Intelligence, No. 4830 in LNCS, Springer, 2007, pp. 609–613.

[9] A. Basu, R.W. Blanning, A formal approach to work<sup>fl</sup>ow analysis, Information System Research 11 (1) (2000) 17–36.

[10] D. Berg, Turning Sarbanes–Oxley projects into strategic business processes, Sarbanes–Oxley Compliance Journal (2004).

[11] E. Bertino, E. Ferrari, V. Atluri, The speci<sup>fi</sup>cation and enforcement of authorization constraints in work<sup>fl</sup>ow management systems, ACM Transactions on Information and System Security 2 (1) (1999) 65–104.

[12] R.A. Botha, J.H.P. Eloff, Separation of duties for access control enforcement in workflow environments IBM Systems Journal 40 (3)(2001) 666–682.

[13] K. Chari, J. Perols, An AI-based approach for procurement fraud detection, Proceedings of the Workshop on Information Technologies and Systems, 2005.

[14] P.P. Chen, The entity-relationship model: towards a uni<sup>fi</sup>ed view of data, ACM Transactions on Database Systems 1 (1976) 9–36.

[15] Committee of Sponsoring Organizations, Internal Control-Integrated FrameworkURL http://www.coso.org/publications/executivesummaryintegratedframework.htm.

[16] J.E. Cook, A.L. Wolf, Software process validation: quantitatively measuring the correspondence of a process to a model, ACM Transactions on Software Engineering and Methodology 8 (2) (1999) 147–176.

[17] B.F. van Dongen, R.M. Dijkman, J. Mendling, Measuring similarity between business process models, CAiSE, 2008, pp. 450–464.

[18] S. Goedertier, J. Vanthienen, Declarative process modeling with business vocabulary and business rules, OTM 2007 Workshops, No. 4805 in LNCS, Springer, 2007, pp. 603–612.

[19] S. Goedertier, C. Mues, J. Vanthienen, Specifying process-aware access control rules in SBVR, Advances in Rule Interchange and Applications, No. 4824 in LNCS, Springer, 2007, pp. 39–52.

[20] S. Goedertier, D. Martens, B. Baesens, R. Haesen, J. Vanthienen, Process mining as <sup>fi</sup>rst-order classi<sup>fi</sup>cation learning on logs with negative events, BPM 2007 Workshops, vol. 4928 of LNCS, Springer, 2008, pp. 42–53.

[21] G. Governatori, Z. Milosevic, A formal analysis of a business contract language, International Journal of Cooperative Information Systems 15 (4) (2006) 659–685.

[22] S. Green, Manager's Guide to the Sarbanes–Oxley Act: Improving Internal Controls to Prevent Fraud, Wiley, 2004.

[23] D.A. Haworth, L.R. Pietron, Sarbanes–Oxley: achieving compliance by starting with ISO 17799, Information Systems Management 23 (1) (2006) 73–87.

[24] D.R. Kuhn, Mutual exclusion of roles as a means of implementing separation of duty in role-based access control systems, RBAC 97, ACM, New York, NY, USA, 1997, pp. 23–30.

[25] A. Kumar, J.L. Zhao, Dynamic routing and operational controls in work<sup>fl</sup>ow management systems, Management Science 45 (2) (1999).

[26] P.F. Linington, Z. Milosevic, J. Cole, S. Gibson, S. Kulkarni, S. Neal, A uni<sup>fi</sup>ed behavioural model and a contract language for extended enterprise, Data & Knowledge Engineering 51 (1) (2004) 5–29.

[27] D.-R. Liu, M.-Y. Wu, S.-T. Lee, Role-based authorizations for work<sup>fl</sup>ow systems in support of task-based separation of duty, The Journal of Systems and Software 73 (3) (2004) 375–387.

[28] D. Nute, Defeasible logic, handbook of logic in arti<sup>fi</sup>cial intelligence and logic programming, Nonmonotonic Reasoning and Uncertain Reasoning, vol. 3, 1994, pp. 353–395.

[29] J. Paredaens, P. De Bra, M. Gyssens, D. van Gucht, The Structure of the Relational Database Model, Springer-Verlag New York, Inc., New York, NY, USA, 1989.

[30] A. Rozinat, W.M.P. van der Aalst, Conformance testing: measuring the <sup>fi</sup>t and appropriateness of event logs and process models, BPM 2005 Workshops, vol. 3812 of LNCS, Springer, 2006, pp. 163–176.

[31] A. Rozinat, W.M.P. van der Aalst, Conformance checking of processes based on monitoring real behavior, Information Systems 33 (1) (2008) 64–95.

[32] S. Sadiq, G. Governatori, K. Namiri, Modeling control objectives for business process compliance, Business Process Management, No. 4714 in LNCS, Springer, 2007, pp. 149–164.

[33] R. Sandhu, E. Coyne, H. Feinstein, C. Youman, Role-based access control models, IEEE Computer 29 (2) (1996) 38–47.

[34] H. Schonenberg, B. Weber, B.F. van Dongen, W.M.P. van der Aalst, Supporting flexible processes through recommendations based on history BPM 2008 vol 5240 of LNCS. Springer, 2008, pp. 51–66.

[35] R.T. Simon, M.E. Zurko, Separation of duty in role-based environments, Computer Security Foundations Workshop. 1997. Proceedings., 10th, 1997, pp. 183–194.

[36] J. Wainer, A. Kumar, P. Barthelmess, DW-RBAC: a formal security model of delegation and revocation in work<sup>fl</sup>ow systems, Information Systems 32 (3) (2007) 365–384

![](/api/attachments/T2F2YKKY/fulltext/images/a52ae4fe5c219057cfc050d6e4f15b4faeddddb881624c337a7fc79c0409b31c.jpg)  
Wil van der Aalst is a full professor of Information Systems at the Technische Universiteit Eindhoven (TU/e). Currentl he is also an adjunct professor at Queensland University of Technology (QUT) working within the BPM group there. His research interests include work<sup>fl</sup>ow management, process mining, Petri nets, business process management, process modeling, and process analysis. For more information about his work visit: http://www.work<sup>fl</sup>owpatterns com, http://www.work<sup>fl</sup>owcourse.com, http://www. processmining.org, http://www.yawl-system.com, or http://www.wvdaalst.com.

![](/api/attachments/T2F2YKKY/fulltext/images/da6c8ffb1326531f6ddc09b31df31046a1f10163750acb78a10b32d9739cd8a1.jpg)

Kees M. van Hee is a full professor of Information System at the Technische Universiteit Findhoven since 1984 He was 16 years managing director of several consultancy <sup>fi</sup>rms, including Deloitte. In 1999 he became partner at Deloitte as national director of consultancy until 2004. Since 2004 he is full professor again. He published over 120 articles on the following topics: Markov decision processes, applications of queuing theory, decision support systems, speci<sup>fi</sup>cation methods and tools, Petri nets, database systems and work<sup>fl</sup>ow management systems. He published <sup>fi</sup>ve books and he is the originator of the software tools ExSpect and Yasper. He conducted over 20 PhD-proiects and over 130 master thesis projects. Five of his PhD students became full professors. He presented over 150 lectures at conferences for scientists, practitioners or managers

![](/api/attachments/T2F2YKKY/fulltext/images/9d8a0f9ddc2f2e523a30ab95dfe2ed58b9f356c4cf424bc2641b187595f27ff6.jpg)

![](/api/attachments/T2F2YKKY/fulltext/images/1b06b631ed8e4c70a79b0fc402c66a368f2d99d92b05230e9858b7214b3f39ee.jpg)

Jan Martijn van der Werf is a PhD candidate in the Architecture of Information Systems group at the Technische Universiteit Eindhoven. He obtained his M.Sc. in Business Information Systems (2006) at the same university. His research interests include modeling and veri<sup>fi</sup>cation of information systems, their architectures, and the use of process mining in the monitoring of such systems.

Akhil Kumar is a professor of information systems at the Smeal College of Business at the Pennsylvania State University. He received his Ph.D. from the University of California at Berkeley, and has previously been on the faculties at Cornell University and University of Colorado. He has done pioneering work in data replication and XML based work<sup>fl</sup>ows. His research interests are in work<sup>fl</sup>ow systems, e-services, distributed information systems and intelligent systems. He has published more than 80 scienti<sup>fi</sup>c papers in academic journals and international conferences, and also held many editorial positions.

![](/api/attachments/T2F2YKKY/fulltext/images/ac26b59c2ed01b0de0d91bb22d55f74a2a2a2cee8b8a93c05c39bddfd893c794.jpg)

Marc Verdonk is a senior manager and IT auditor with Enterprise Risk Services at Deloitte Nederland as well as a PhD candidate in the AIS group at Technische Universiteit Eindhoven. He obtained his M.Sc. in Computer Science at Universiteit Utrecht and is both Certi<sup>fi</sup>ed Information System Auditor (CISA) as Certi<sup>fi</sup>ed Information System Security Professional (CISSP). His main interest is to make the audit profession future-proof by designing and applying technology-based approaches that makes auditing more ef<sup>fi</sup>cient, effective, value added and maybe even fun, for the auditee as well as the auditor.
