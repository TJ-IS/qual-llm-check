---
otero_id: 26434
otero_key: "TYAG39YN"
title: "Research Commentary: Workflow Management Issues in e-Business"
authors: "Amit Basu; Akhil Kumar"
year: "2002"
journal: "Information Systems Research"
doi: "10.1287/isre.13.1.1.94"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.248.155.225] On: 15 September 2016, At: 10:37 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

# Information Systems Research

![](/api/attachments/TYAG39YN/fulltext/images/f2e16507684bd8be5479b6f445e26eb2f49e097ed5cb5333cf8b6f2e2ec65bf4.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Commentary: Workflow Management Issues in e-Business

Amit Basu, Akhil Kumar,

## To cite this article:

Amit Basu, Akhil Kumar, (2002) Research Commentary: Workflow Management Issues in e-Business. Information Systems Research 13(1):1-14. http://dx.doi.org/10.1287/isre.13.1.1.94

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2002 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/TYAG39YN/fulltext/images/326671f6810533a407c662eb2095331e57be93c9c2edbc836e18366d2ec36204.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Commentary: Workflow Management Issues in e-Business

Amit Basu • Akhil Kumar<sup>1</sup>

Cox School of Business, Southern Methodist University, Dallas, Texas 75275 Bell Laboratories, 600 Mountain Avenue, 2A-406, Murray Hill, New Jersey 07974 abasu@mail.cox.smu.edu • akhil@acm.org

rends towards increased business process automation, e-commerce, and e-business have led to increasing interest in the field of workflow management. In this paper, we provide a perspective on the state of research in workflow management systems, and discuss possible future research directions in this area, with a particular emphasis on workflow systems in integrating interorganizational processes and enabling e-commerce solutions.

(Workflow Systems; e-Business; Workflow Specification; Workflow Modeling; B-to-B Exchange; e-Hubs; e-Services; Composition)

## 1. Introduction

Considerable progress in the field of information systems over the past 20 years has resulted from collaborative efforts among researchers from a variety of basic disciplines, ranging from computer science to social sciences. Over this same period, the economy has rapidly shifted from its traditional industrial base to a new, information-based economy. With the evolution of the commercial Internet and the use of the thinclient model of client-server systems in e-commerce and e-business, new types of digital products have augmented the service sector that has become such an important component of the economy. In this new environment, work has shifted from the creation of tangible goods to the flow of information through the value chain. Because these flows are critical to a firm’s business processes, they have triggered great interest in methods to define, analyze, and manage the flow of information-intensive work. The term “workflow management” is often used to characterize these tasks, and represents a broad, multidisciplinary body of research and development in this area.

The purpose of this paper is (1) to provide a perspective on the field of workflow management, and (2)

to identify promising directions for future research, focusing on the specification, analysis, and management of workflows in e-business environments.

Figure 1 gives a framework that also serves as a road map for this paper. Research in workflow systems can be viewed in terms of successive layers of complexity, and the framework shows how these layers have evolved. In Figure 1, the first layer pertains to issues that arise in intraorganizational workflows. The main ones are specification and modeling of workflows, performance, monitoring and control of workflows, and organizational metamodels of workflows. These are covered in §2 of this paper. Next, §3 discusses the next layer corresponding to interorganizational workflows. The issues that are relevant here are distributed architectures for combining workflows of business partners, and also ways to reconcile different workflow models. Then, §4 discusses the implications of workflow technologies in e-commerce settings, focusing on workflows for supply chains, design of e-hubs and composite e-services, and workflow standards to facilitate seamless e-commerce. Finally, we share some closing thoughts in §5.

Figure 1 A Framework for Workflow Systems Research

<table><tr><td colspan="3">e-Business Workflows(Supply Chains, e-Hubs, e-Services, Standards)</td></tr><tr><td colspan="3">Intraorganizational Workflows(Distributed Architectures, Heterogeneous Workflow Models)</td></tr><tr><td colspan="3">Intraorganizational Workflows</td></tr><tr><td>Workflow Specification</td><td>Organizational Metamodels</td><td>Workflow Analysis and Control</td></tr></table>

## 2. Intraorganizational Workflows

In this section, we review existing approaches to modeling workflows that occur within a single organization, and identify opportunities for additional work in this area. However, before discussing representation models, we first clarify exactly what is meant by the term “workflow,” since there are several interpretations in the literature.

## 2.1. Interpretations of Workflow Management

We identify three predominant views of workflows from the literature. In the first view, a process is viewed as a collection of tasks executed by various resources within a value system comprising one or more interacting organizations. Each process takes a specific set of inputs and transforms them into a specific set of outputs. Workflows associated with routine processes are called production workflows. On the other hand, a process may be nonroutine, resulting in possibly novel situations and ad hoc workflows. However, ideally, business processes should be designed to systematize the routine functions while also accommodating exceptional circumstances. Clearly, the specific tasks used to implement a business process may vary from one instance to another. Each such combination of tasks comprising an enactment of the business process then represents a workflow for this process (Basu and Blanning 2000).

A related view is represented by an industry standard proposed by the Workflow Management Coalition (WFMC www.wfmc.org-). According to the WFMC, a workflow is “the automation of a business process, in whole or in part, during which documents, information or tasks are passed from one participant to another for action, according to a set of procedural rules.” This view too assumes that each enactment of the process has a specific workflow, and uses the term “work case” to describe each instance. In fact, according to this standard, the terms “workflow management” and “case management” are synonymous. The key distinction of this view is that it focuses on automation of processes, and the implementation of workflow control through a software system called a “workflow engine.”

A third view of a workflow is as a particular type of process. For instance, Baresi et al. (1999) define a “workflowable” process as one with the following characteristics:

Predictability: the process is clearly defined and structured.

Repeatability: the process corresponds to a repeated situation.

Distributed: the process involves several organizational units.

Automation: the process can benefit from automated support.

Idling: the process contains idle periods that can be reduced by automatic checking and deadline management.

Opportunity: the process involves applications that can be easily implemented.

Although these three views are quite similar in spirit, they vary in specificity, the first being general and all-encompassing, while the third view is more specific in identifying the aspects of business processes that are especially suitable for automation through workflow technology.

## 2.2. Workflow Specification and Modeling

In this section, we examine different approaches to representing and reasoning about workflows.

2.2.1. Workflow Components. We start by reviewing basic workflow terminology, which includes terms such as process model, task, work case, resource, role, data elements, state information, and constraints. A process model represents the logic of a business process. It is a schema describing a collection of tasks that must be performed in accordance with various coordination requirements. For example, in a workflow associated with an order-processing application, the credit check and inventory check may occur in parallel, followed by manufacturing, shipping, delivery, and payment. A task (or activity) is an elemental process that represents a logical unit of work within the business process. A specific instance of a process model is called a work case. A work case often has an owner who is responsible for managing the case and resolving any problems. A resource is a human worker, machine, or even an organizational unit responsible for performing a task. In the case of human workers, the resource may be a specific individual, or alternatively, a generic role, such as a vice-president or a director, which represents a class of workers, any one of whom may perform a given task. A task may need input data and in turn produce output data or results that may be used by other tasks. For example, an order-processing task requires order data as input and produces a confirmation number and delivery date as output. The input and output data are called the data elements of a task. A task may also be in one of many states such as running, finished, suspended, etc. The activation, control, and evaluation of each task may be restricted by one or more constraints. Such constraints may be in the form of assumptions, decision rules, or triggers, and must be enforced by the workflow system.

2.2.2. Workflow Specification and Modeling Approaches. The key issues in workflow specification relate to task definition, task coordination, and correctness of execution requirements. The initial research in this area dates back to the Wharton Ph.D. thesis of Zisman (1977), who developed a Petri-net-based approach to specification and automation of office procedures. Subsequently, several researchers have used Petri nets as a workflow representation formalism (Murata 1989). Petri nets are particularly appealing because they have a formal structure that supports detailed analysis, and existing techniques for Petri net analysis can be applied to the analysis, validation, and verification of workflows (van der Aalst 1998, Desel and Esparaza 1995).

Another formalism that dates back to around the same time is the Information Control Nets (ICN) proposed by Ellis and Nutt at Xerox Parc (Ellis 1999, Ellis and Nutt 1980). The ICN is a simple but mathematically rigorous formalism designed to model office procedures. These nets consist of AND and OR nodes. The multiple tasks that emerge from an AND node are required to be done in parallel, while at an OR node any one of the several tasks is required to be done before the workflow can proceed. These nodes are used as building blocks to create a model of an office procedure. Other graph-theory-based models are discussed in (Luqi 1990).

A radically different approach is based on the ActionWorkflow formalism (Action Technologies, www.actiontech.com-). The underlying philosophy is the theory of speech acts, and has been discussed in the work of Winograd and Flores (1987). This paradigm states that all types of speech fall into just a few categories, and doing so facilitates meaningful interactions between various parties. Thus, a workflow is modeled as a series of conversations between customers and performers. There are four phases (akin to speech acts) in the conversations, namely, requests, agreement, performance, and satisfaction (or evaluation).

Another approach is to use an event-driven model for workflows. For example, the ECA (event conditions actions) was proposed by McCarthy and Dayal (1989) in the context of active databases. It lends itself well to a workflow implemented in a database environment, which supports events and triggers. The WIDE project has taken such an approach (Grefen et al. 1999). The EROCA approach (Kumar and Zhao 1999) adds roles and data objects to the ECA framework and suggests a possible direction for modeling workflow applications using an event-based paradigm.

A graph-theoretic approach that captures the M:N relationships represented by workflow tasks is based on metagraphs (Basu and Blanning 1994a and b). A metagraph contains directed edges that connect pairs of sets of elements. As shown in Basu and Blanning (2000), all the important components of workflows can be captured in a metagraph. Furthermore, multiple overlapping workflows can be represented in the same metagraph, which is a distinct feature of this approach. In addition to the visual representation of workflows as metagraphs, this approach also supports formal analysis of both the structure and performance of workflows. For instance, connectivity analysis can provide insights into process structure, such as whether there is an acceptable workflow in each relevant scenario, whether the workflow involves any cycles, whether there are situations where multiple redundant workflows can occur, and whether there are critical tasks that impact multiple workflows (or even multiple processes). Similarly, when attributes such as task durations (Basu and Blanning 2001), task costs, or resource costs are available, analysis of process schedules, timeliness, and cost effectiveness can also be done through formal procedures on the metagraph representation.

There are more than 200 products on the market that implement the various models. Some example products that exploit the technologies described above are ActionWorks www.actiontech.com-, Cosa www.cosa .de-, IBM MQSeries Workflow, formerly called FlowMark www.ibm.com/mqseries-, InConcert www.inconcert .com-, and Staffware (Staffware 1999). Some mail-based systems also have limited workflow capabilities, such as Information Lens (Malone et al. 1987) and Object Lens (Lai et al. 1988) from MIT, and newer products with more sophisticated features such as Lotus Notes and Microsoft Exchange. The Vortex system at Bell Labs is based on a declarative and rule-based approach to workflows (Hull et al. 1999). The workflow patterns home page (van der Aalst 2001) is a useful resource for the variety of workflow scenarios that can arise in real situations, and Leymann and Roller (2000) is a good resource for workflow systems concepts and implementation techniques.

One important issue that arises from the diversity of the above approaches to workflow modeling is the need for a unifying model. So far, no single approach has emerged as a standard. An approach towards workflow modeling similar to the one taken in the Unified Modeling Language (UML) (Fowler and Scott 1997) would be potentially quite promising. However, even within UML, a number of different modeling formalisms are supported, such as class diagrams, activity diagrams, and interaction diagrams, and a given application may use one or more of these formalisms resulting in very different models. Therefore, it is likely that several models will continue to coexist for some time. Translating between these models so that different workflow systems can interoperate is an interesting research problem which has not received much attention. This could lead to methods for integrating these heterogeneous models into a common framework.

## 2.3. Organizational Modeling of Workflows

The approaches described above are useful for modelling the control flow aspects of a workflow. Given that workflow systems operate in an organizational context, it is extremely important that they must be “organizationally aware” for the successful application of workflow technology. Moreover, it is crucial that there be a good fit between work practice and the models/mechanisms used by the workflow management system. Unfortunately, most of today’s workflow management systems focus on the process dimension (i.e., routing, control flow) and oversimplify the organizational dimension. Hence, the integration of workflow models with organizational models is an important area for future research, as we will see in this section.

An organization model reflects the organization structure of an organization. In the simplest form, it can be drawn as a tree or a directed graph. It represents a logical hierarchy of roles that are performed in the organization. Work in organizations is usually assigned to roles as opposed to specific named individuals. Therefore, in an insurance company, an important role is that of a claims director, and it is further specialized into roles of fire-claims, auto-claims, floodclaims, etc. inspectors. In each of these subcategories, there may be several individual workers who can perform these tasks. Companies have policies in place regarding who can perform what task. For instance, an auto-claims inspector would normally review an auto accident claim. However, if none of the auto-claims inspectors is available, the review could be assigned to a fire-damage claims inspector or even the claims director. This kind of flexibility is essential in all organizations. Therefore, a constraint specification language is required to specify such rules and policies in a convenient way.

There are also important policies regarding separation and binding of duties. Separation of duties means two tasks of a given workflow instance should not be performed by the same individual, e.g., an individual will not approve his or her own travel expenses. Another example of separation of duties is that “two different individuals must sign a check.” The need for binding of duties also arises in workflow systems. For instance, there may be a requirement that the same individual who made a sale to a customer should handle the repairs as well. However, the requirement for binding is often less stringent.

As an example of a complex constraint, consider the following from Bertino et al. (1999): “Task T2 must be executed by a role dominating the roles that execute tasks T1 and T4, unless T1, T2 and T4 are executed by the role general manager.” The approach of Bertino et al. (1999) to handling this kind of constraints is based on predicate logic. Other methods include the introduction of dynamic activation and revocation of privileges (Atluri et al. 1997) and an active-rule-based model (Castano and Fugini 1998). Moreover, Nyanchama and Osborn (1999) discuss conflicts of interest in terms of users/groups, roles, privileges, and their interrelationships. Simon and Zurko (1997) discuss separation-ofduty constraints (both static and dynamic), which are then implemented in Adage, a rule-based authorization system for distributed applications. In addition to further research on such security policies in an organization, it is also necessary to develop models for delegation of work so that a worker may perform impromptu delegation of tasks to coworkers based on their suitability and availability. At the same time, it is important that the security policies not be violated. Hence, work on delegation should be integrated with the work on security.

There is clearly a great need for better organizational models to make workflow management systems more “organizationally aware.” The work of zur Muhlen (1999a and b) is a step in this direction. The WFMC has also issued a metamodel recently (WFMC 1999). Naturally, it is also important to incorporate organizational constraints into such models, as they relate to resources, roles, tasks, policies, etc. There should be flexibility built into the constraints such that, in special situations, some constraints may be violated in order to complete the workflow gracefully. At a minimum, there must be a notion of hard/soft constraints, where hard constraints can never be violated, while the soft ones could.

2.4. Workflow Analysis, Monitoring, and Control Workflow systems require a variety of analyses, ranging from analysis of system design to analysis of system behaviour for monitoring and control purposes.

2.4.1. Structural Analysis. This includes methods to analyze the structure of processes and workflows during the design (or redesign) phase. The correctness, effectiveness, and efficiency of the business processes supported by the workflow management system are vital to any organization. A workflow process definition that contains errors may lead to angry customers, backlog, damage claims, and loss of goodwill. Flaws in the design of a workflow definition may also lead to high throughput times, low service levels, and a need for excess capacity. This is why it is important to analyze a workflow process definition before it is put into production.

There are three types of structural analyses:

Validation, i.e., testing for semantic completeness to ensure that the workflow behaves predictably in all scenarios.

Verification, i.e., establishing the syntactic correctness of a workflow and eliminating redundancies and deadlocks.

Data usage analysis, i.e., analyzing the pattern of data access by various tasks and preventing erroneous access patterns.

Validation can be done by interactive simulation: Fictitious cases are fed to the system to see whether they are handled well. For verification and performance analysis, more advanced analysis techniques are needed. Fortunately, many powerful analysis techniques have been developed for Petri nets (van der Aalst 1998). Linear algebraic techniques can be used to verify many properties, e.g., place invariants, transition invariants, and (non) reachability. Coverability graph analysis, model checking, and reduction techniques can be used to analyze the dynamic behavior of a Petri net. Some examples of tools are Woflan www.win.tue.nl/woflan/- and ExSpect www.exspect.com-.

Most workflow management systems do not support workflow verification. As a result, workflow process definitions become operational before they are thoroughly checked for correctness. This often results in runtime errors that need on-the-fly repair at high costs. There is clearly a need for analysis tools that take care of verification, particularly in the context of interorganizational workflows. Unfortunately, most vendors do not yet have the technology to build such tools.

Data usage analysis is required to prevent two concurrent tasks from writing to the same data object at the same time. Moreover, it is important to make sure that permissions to perform various data operations are assigned in a manner so as to prevent inadvertent errors. Because workflow systems are used to model the structure and behavior of processes in organizations, it is important to ensure that they maintain data integrity and recoverability in the same way that database applications do.

One way of doing so is to introduce a notion of transactions in workflow systems. However, the concept of transactions in the context of a workflow enactment is not clearly understood because a workflow describes a complex coordination of tasks and may run for a long time. Treating the entire workflow as one transaction could have harmful effects on concurrency. It is not clear how a failure of a partially completed workflow should be handled. Another respect in which workflow systems differ from database systems is that database systems can recover the data in a consistent manner, but they do not have a notion of state. In a workflow it is important to maintain the state of an enactment as well. For instance, the state of a workflow enactment would record information related to what tasks have been completed, what tasks are currently active, what paths were taken at OR nodes, how many times a loop was executed, etc. In case of failure, it should be possible to restore an enactment to its prefailure state. Therefore, transaction management approaches need to be modified suitably for workflow environments. A number of extended transaction models have been proposed, such as the ACTA framework (Chrysanthis and Ramamritham 1994), and the Contracts model (Wa¨chter and Reuter 1991). These need to be investigated further, to see how well they can be adapted into real workflow scenarios. The work described in (Rusinkiewicz and Sheth 1995) is a good start in this direction.

Related analyses may address the satisfactory allocation of resources to workflows, the nature of interactions among different resources and organizational units during each workflow, the scheduling of tasks to meet temporal constraints, and examination of costbenefit implications of specific workflows and processes. Some work on these problems has been done using metagraphs and Petri nets, but many problems still remain. Additional complexities arise in the design of distributed workflows, especially those spanning multiple organizations, as is commonplace in electronic commerce applications. Again, much more research is needed in these areas.

2.4.2. Performance Analysis. It is also very important to monitor and control ongoing processes. The processes must be evaluated with respect to performance indicators pertaining to service levels and resource utilization. Today’s workflow management systems provide limited support for performance analysis. Most provide a rudimentary simulator or a gateway to a simulation tool. Simulation and Markov Chain analysis (Kleinrock 1975, Ross 1990) can be used to estimate key performance indicators by experimenting with the specified workflow under the assumption of a specific behavior of the environment. Examples of key performance indicators are average throughput time of cases, average waiting time, occupation rates of resources, service levels, and the average number of pending cases. Computation of such metrics becomes harder because workflow transactions are typically long lived, involving interaction between manual and automated processing, and also between multiple resources. These problems only get further exacerbated when a workflow spans multiple organizations

There are two basic mechanisms for work distribution or allocation in a workflow system:

Push mechanism: A work item is pushed to a single resource.

Pull mechanism: A resource pulls work items from a view on a common pool of work items.

The push mechanism is a special case of the pull mechanism in that only one resource can see a given work item. It suffers from the drawback that if an item is “pushed” to a worker who is on vacation, this item could be sitting in the workbasket of this worker until she returns from her holiday. On the other hand, with a pull mechanism, multiple workers are “offered” this work item and chances are higher that one of them will be available to perform it. Therefore, current state-ofthe-art workflow systems (such as Staffware 1999, etc.) consider the pull mechanism as the basic paradigm for work distribution because this mechanism gives more flexibility.

For work distribution to workers to be effective, it should be based on explicit models of organizational structures and capabilities of workers, and this is being recognized, as reflected in recent work in this area (Jablonski and Bussler 1996, Lawrence 1997, zur Muhlen 1999a, Kumar et al. 2001b).

## 3. Distributed and Interorganizational Workflows

The focus of the discussion so far has been on workflows, or processes within a single organization, in the sense that a single workflow management system can be used to design, monitor, and control the workflow in the process. However, in practice and in general, this assumption must be relaxed in a number of ways:

(1) A single process may span multiple, geographically distributed locations. Centralized coordination of such processes not only imposes significant communication overhead, often over lower-bandwidth widearea networks, but also jeopardizes the process if the communication links are not wholly reliable.

(2) The workflow systems used for different subprocesses may be different, and may not support adequate interoperability.

(3) A process may span multiple organizational units, or even multiple cooperating partners in a value chain. Each entity may be motivated to control its own resources and activities, and may not accede control to its partners. See Lindert and Deiters (1999) and Kumar and Zhao (2001a) for examples of distributed architectures.

In terms of modeling such workflows, a number of additional problems are encountered which lead to interesting research questions. For example, when pieces of a workflow are partitioned across multiple firms, the interactions between activities that are at the organizational boundaries may have to be restructured. For example, in Figure 2a, if the workflow is partitioned so that Activity 1 is in one firm while Activities 2 and 3 are in another firm, then a mechanism must be introduced to transfer data across the boundary. As shown in Figure 2b, this may be accomplished by generating events that are sent via e-mail, HTTP, FTP, or using some other standard protocols. The second organization must also provide a mechanism to receive the event notification and resume the workflow. It may also be necessary to pass relevant data and state information across the organizations. Figure 2c shows a variant scenario in which the workflow may return to the first organization, thus creating an interorganizational loop or cycle. In such a case, it may be necessary to track the number of times such loops and cycles may occur to prevent indefinite iteration. Workflow models based on Petri nets can be adapted to model and implement such interorganizational workflows, as shown in van der Aalst and Kumar (forthcoming) and Lindert and Deiters (1999).

Figure 2a An Intraorganizational Workflow  
![](/api/attachments/TYAG39YN/fulltext/images/4d442aaae473b19e1ea5f87f545503b23a160127cfe08e0098cfcedd934ee927.jpg)  
Information Systems Research Vol. 13, No. 1, March 2002

The restructuring of workflows in distributed settings also raises a number of analytical questions. For example, in the case of outsourced activities, traditional control flow analyses are complicated by the fact that invocation of these tasks has to be structured as service requests (or API calls) to external coordinators, object resource brokers (ORBs), or transactionprocessing (TP) monitors. It is important to ensure that problems such as inconsistency and duplication of work do not arise due to the lack of transparency across the organizational boundaries. A more serious problem occurs when two workflows (say, of two partners) are integrated. Various kinds of integrity and validation problems can occur in trying to do this. For instance, two workflows that work well independently may deadlock when they are integrated. Some of these issues are addressed in van der Aalst (2000) using Petri nets as a modeling paradigm. However, the problem gets further exacerbated when the two partners use different workflow models altogether. While there is existing research in the area of mapping data models in the context of heterogeneous database systems (March et al. 2000), there is little work so far in the area of mapping disparate workflow models into one another, the metagraph approach (Basu and Blanning 2001) being one example of such work.

Figure 2b The Corresponding Interorganizational Workflow  
![](/api/attachments/TYAG39YN/fulltext/images/f2bbb2707869bf98d3eee440261be6f9b94bd3ca41bacfd3286e22e713675a7b.jpg)

Figure 2c A Re-entrant Workflow  
![](/api/attachments/TYAG39YN/fulltext/images/13a4611795a7a9e98d07ab670ad7fea6a038d1e4f9b293584e9f9d547199b11f.jpg)

In distributed workflows, an additional problem is the assignment of workflow or process fragments to servers and/or controllers, since centralized control may be infeasible. As discussed in Bauer and Dadam (1997) and Ceri et al. (1997), an intuitively appealing approach is to partition the workflow control so that tasks are controlled by the server that is nearest to the resources required for it. However, this may not always work well if a task is later delegated dynamically by a designated resource to a distant resource. Hence, dynamic allocation of tasks to servers when resources may migrate becomes a challenging optimization problem.

## 4. Workflow Issues in e-Business

In this section, we identify some promising areas for workflow research in the context of e-commerce and e-business. The methodological and conceptual bases for these research possibilities are those discussed in the previous sections, so we focus primarily on the application areas and issues.

## 4.1. Integrating ERP Applications with Supply Chains

A major area of process innovation through the use of Internet technologies is in the area of supply chain management. Adoption of EDI in various industries over the past two decades has facilitated relatively high levels of integration between manufacturers and their suppliers. However, although EDI is a very valuable technology, it does not offer the same flexibility as interaction over the Internet. One disadvantage of EDI is that it requires more set-up time, e.g., partners have to acquire and install special software, and subscribe to a VAN service before they can communicate. Moreover, the documents have to be formatted precisely according to specifications based on broad standards such as ANSI X.12 and EDIFACT. The Web overcomes these disadvantages while providing a secure means of communication through a browser. This increases flexibility and makes it easier to build (and reconfigure) supply chains quickly.

Workflow systems are key to the operation of supply chains, especially if they are to be tightly integrated. For instance, an online customer order for a new car is a workflow consisting of steps like selection of car features, placement of order, price and delivery date determination, confirmation of order, advance part payment, manufacturing, final payment, and delivery. This workflow consists of several subworkflows. For example, manufacturing may involve ordering materials and subassemblies, scheduling the final assembly, inspection, etc. Delivery may involve pick up at a factory, shipment by train or ship to an intermediate location, scheduling a delivery time with the customer, temporary storage, and then final shipment by a carcarrier to the customer premises, and handing over. The ability to query and view the status of this workflow and interact with it is important, particularly if it becomes necessary to consider changes to it, such as the impact of delays in parts shipments, transportation problems, etc.

There are two important problems here. The first involves the design and optimization of Internet-enabled supply chains. On the one hand, the open structure of the Internet allows companies to have more flexible supply chains that allow for more market-based (competitive) sourcing from multiple (or alternative) suppliers. On the other hand, the increased transparency offered by web-based systems often forces companies to move towards more tightly coupled supply chains. In such a situation, effective workflow management becomes crucial, since the resulting process is inherently distributed and interorganizational. One stream of research evolving in this area is the enhancement of workflow specification techniques based on graphtheoretic methods such as Petri nets and metagraphs (van der Aalst and Hofstede 2001, Basu and Blanning

2001). The use of these techniques enables the development of analytical tools for verification and validation of composite workflows. Another stream is the use of XML to build loosely coupled supply chains (van der Aalst and Kumar (forthcoming), Herring and Milosevic 2001, Lenz and Oberweis 2001).

The second problem is how to workflow-enable existing ERP (Enterprise Resource Planning) systems. ERP products are transaction driven, as opposed to processcentric, in their focus. Moreover, ERP systems manage structured data while workflows often involve handling unstructured documents. Therefore, workflow-enabling existing ERP systems requires bridging these different perspectives, and several companies like Oracle and SAP are involved in this effort. An example of work in this direction is Hartmann et al. (2001).

## 4.2. B-to-B Exchanges and e-Hubs

A B-to-B exchange is an electronic marketplace in which buyers and sellers meet to transact business. These marketplaces are also called e-hubs. These hubs are organized as vertical markets, and some wellknown examples are Covisint (for automobile companies) and Chemdex (for chemical products). The software for building such exchanges is provided by companies like Ariba, FreeMarkets, and Commerce One. These hubs are advantageous for both buyers and sellers because they reduce transaction costs. These exchanges can take two forms: public and private. Moreover, based on whether the exchanges are part of a vertical or horizontal market, and whether they are used for procurement of operating inputs or maintenance, repair and operation (MRO) inputs, they may be further classified into a 2 - 2 matrix of four categories (Kaplan and Sawhney 2000). There are C-to-C (consumer-to-consumer) e-hubs as well, well-known examples being e-Bay and Yahoo. These marketplaces allow consumers to carry out transactions among themselves.

Such marketplaces, though still in their infancy, will clearly play a major role in the near future and large amounts of business will be conducted through them. It is hard to predict what shape they will eventually take (see Wise and Morrison 2000 for some possible directions). However, these hubs are likely to play an important role in interorganizational workflows. These hubs can act as gateways that allow partner organizations (e.g., partners in a supply chain) to connect together and share supply chain data. This is the idea behind a promising new technology called CPFR (Collaborative Planning, Forecasting, and Replenishment). The goal of this next-generation supply chain technology is to allow the supply chain partners to exchange information instantaneously. Thus, as soon as a bag of potato chips is sold at a Wal-Mart store, this information would be transmitted to the e-hub, which would in turn pass it on to the distributor, manufacturer, the raw material suppliers, etc. This approach has several advantages. Rather than transmitting this information in a linear manner, it is transmitted via a hub. Moreover, the hub can reconcile differences between the data formats of multiple partners more easily, and repackage the data in a different form, perhaps even at a different level of aggregation. It does require a registration process whereby each partner would inform the server about the information that it will be sending to the hub, the identities of its partners, and, for each partner, what information it can access.

There are several important research issues here. The first one is the design of a distribution channel based on an e-hub. Instead of being linear it would perhaps be designed around a network model. This involves working out the details of information flows between various entities and the data structures for storing the information to be shared, along with the metainformation for sharing. The second is developing techniques for ensuring semantic integrity of the information and rules for mapping it correctly between any two partners, where the mapping or translation has to be done both for data and process information. The latter is clearly a rich area for further research. Yet another research area is how to build complex workflows using B-to-B exchanges. See Kaplan and Sawhney (2000) for an example of how a used-car auction application was redesigned. Clearly, more research is also needed in modelling and analyzing the performance and reliability aspects of e-hubs so that it should be possible to determine the value of metrics like how long a transaction will take and what the response time is.

## 4.3. e-Service Composition

Service quality is widely accepted as a key basis for competition in e-business and e-commerce. Because the underlying processes are enacted by multiple autonomous parties, without hierarchical or centralized control, effective workflow management and sharing of workflow information is crucial in such environments. We examine some aspects of e-business where these concerns lead to interesting research problems.

4.3.1. Plug-and-Play Services. In this section we discuss service composition where a user (a consumer or a business) is able to connect several services together from different vendors to create a new one-time service in a very short time. This kind of on-the-fly service composition is a new frontier in B-to-B commerce and relies heavily on the ability to quickly connect multiple workflows. An example of this could arise as follows: A user may buy components (such as motherboard, memory, disk drive, etc.) from different vendors; arrange to have a shipping company carry them to an assembler; give instructions to the shipping company to wait for all the components and then assemble the PC; and finally have the shipping company bring the product to the customer. This kind of designyour-own service is an example of a composite service, and it is difficult to implement because it requires intricate coordination among various vendors based on exchange of data and process information. For instance, the assembler must have a way to notify the component makers how to label their shipments so that all the arriving components can be properly routed within the assembler organization. Moreover, if, say, one component is delayed the component maker must inform the shipping company and the assembler about it so that they can adjust their schedules accordingly.

Such a composite service may run in a centralized architecture where the service composer acts like a hub (with a workflow engine and a data repository), or under a distributed architecture where each participant has its own workflow engine and a local database. In this architecture, the synchronization issues between the workflow engines can become complicated. More work is required to find suitable architectures that can scale well. In addition to the architecture, there are two major steps involved in building composite services. The first is to find a way to define the composition of the services. The second step is to make sure that the individual services can interact and coordinate with one another. Some initial work in the direction of the first step, using XML as a language to describe the composition, has been described in Christophides et al. (2001). Considerably more work is required in the second step.

4.3.2. Intelligent e-Services. As service composition gets more complex, other features need to be added. For instance, in the above example it might be possible to add a negotiation service that can negotiate with a vendor on behalf of the customer based on the customer profile. The area of negotiation in the context of e-services presents significant opportunities for methodological research. One very interesting approach that examines the representational implications of negotiated buyer-supplier relationships is that of Grefen et al. (2000), in which the model of a business contract is extended to include a process specification. This presents a specification of interacting processes and workflows as a part of the formal definition of a business relationship, and raises interesting questions such as whether economic parameters of contracts (e.g., costs, penalties, and rewards), can be captured in terms of the process specifications as well.

Customers may also require sophisticated querying abilities to find out the exact status of their order. Designing and running such queries in a heterogeneous environment can be difficult. When the same process is enacted using different partners over time, the ability to obtain consistent and meaningful data from queries about products, orders, and processes can be difficult. For example, service support for a defective part may depend upon which supplier provided the part, whether the manufacturer maintains inventory of the parts from that vendor (in case the vendor no longer makes the part), whether the vendor can directly replenish the customer’s defective part, and whether the part can be sourced from an alternative vendor. If the manufacturer has sourced the part from multiple suppliers, applicable workflows for each vendor case may be a critical determinant of service quality.

Another key area, which requires intelligence, is that of exception handling. Numerous kinds of exception situations can arise in a single e-service, let alone a composite one. Existing workflow systems tend to fall short whenever workflows have to accommodate exceptions to normal conditions. Usually it is the case that the designers anticipated exactly n exception scenarios but as soon as a new one comes up, human intervention is necessary. This problem is exacerbated when the workflow design deals with exceptions at the macro level $( \mathrm { i . e . , }$ alternative scenarios for the whole workflow), rather than using a constructive approach where each task could potentially terminate in multiple states, which results in a much larger state space. One way to alleviate this problem is by designing better metamodels and building interfaces with intelligent systems. Some initial research is reported in Strong (1992), Saastamoinen (1995), and Klein and Dellarocas (2000), but a lot more work is required.

## 4.4. Standards for e-Business

For interoperability to succeed, it is important that vendors agree on basic standards. Many XML-based standards are now beginning to emerge for e-commerce from recent developments in Internet technology and efforts of “electronic exchanges” such as Chem-Connect, Ariba, CommerceOne, Clarus, Staples.com, Granger.com, VerticalNet, and mySAP. The XML Common Business Library (xCBL) by CommerceOne, the Partner Interface Process (PIP) blueprints by Rosetta-Net, the Universal Description, Discovery and Integration (UDDI), the ElectronicBusiness XML (ebXML) initiative by UN/CEFACT and OASIS, the OpenBuying on the Internet (OBI) specification, the Open Application Group Integration Specification (OAGIS) are some proposed standards.

The Universal Description, Discovery and Integration (UDDI) specifications define a way to publish and discover information about web services. The term “web service” describes specific business functionality exposed by a company, usually through an Internet connection, for the purpose of providing a way for another company or software program to use the service. UDDI is intended to be an Internet standard for creating an online business registry. A variety of firmlevel initiatives such as Microsoft’s SOAP (Simple Object Access Protocol) Contract Language and IBM’s

NASSL (Network Accessible Service Specification Language) are being leveraged to develop the UDDI standard.

These standards primarily focus on the exchange of data and not on the control flow among organizations. Moreover, most of the standards provide DTDs (Data Type Definitions) or XML schemas for specific application domains or industries (e.g., procurement, automobile industry, etc.). Some initiatives that also address control flow are RosettaNet and BizTalk. The Partner Interface Process (PIP) blueprints in RosettaNet specify interactions using UML activity diagrams for the Business Operational View (BOV) and UML sequence diagrams for the Functional Service View (FSV) in addition to DTDs for data exchange. However, the PIP blueprints are not executable and need to be predefined. Moreover, like most of the standards, RosettaNet is primarily focusing on electronic markets with long-lasting prespecified relationships with one party (e.g., the market maker) imposing rigid business rules. For its part, Microsoft’s BizTalk www.Microsoft.com/biztalk- facilitates the creation of trading partner relationships by defining XML schemas using standard Internet transport and security technologies (Herring and Milosevic 2001). As with most situations where standards have been slow to evolve, a basic problem in standardization is the lack of a comprehensive model of e-business workflows. Development of such a model $\mathbf { o r } ,$ alternately, requirements specifications for e-business workflow management systems, represent significant opportunities for research today.

## 5. Conclusion

Workflow systems are becoming increasingly important because they are enablers of successful e-business solutions. This paper describes the relevant issues of workflow in the context of e-commerce and e-business applications. According to Sheth et al. (1999), process management is an organic component of any e-commerce solution, and processes will drive the network economy. Traditional information systems research has focused on problems such as application development and database management, which have gained significant maturity. On the other hand, the inherently hybrid (combination of automated and manual) nature of business process workflows, particularly when spread across multiple locations, resources, and organizational entities, present new challenges for IS researchers. In the volatile, dynamic context of e-business, these problems become not only more complex, but their solutions also become critical determinants of success.

In summary, this paper shows that workflow systems in the context of e-commerce represent a fertile area of research for IS professionals, with several interesting and challenging problems. The important issues that have been identified in particular as promising areas for further research are: specification of interorganizational workflows, design of better organizational metamodels, support for exceptions, and development of standards to facilitate interorganizational e-commerce.

## Acknowledgments

This paper benefited immensely from numerous discussions with several people, notably Wil van der Aalst, Paulo Barthelmess, Skip Ellis, Rick Hull, Jacques Wainer, and Leon Zhao, among others, over a period of time. These interactions have helped the authors to formulate their ideas for this paper. Of course, any errors are the sole responsibility of the authors.

## References

van der Aalst, W. M. P. 1998. The application of petri nets to workflow management. J. Circuits, Systems Computers 8(1) 21–66.

——. 2000. Loosely coupled inter-organizational workflows: Modeling and analyzing workflows crossing organizational boundaries. Inform. Management 37 67–75.

——. 2001. Workflow patterns. http://tmitwww.tm.tue.nl/research /patterns/-.

——, A. Kumar. XML-based schema definition for support of interorganizational workflow. Forthcoming, Inform. Systems Res.

——, A. H. M. Ter Hofstede. 2001. Verification of workflow task structures: A petri-net-based approach. Working paper, T.U. Eindhoven, The Netherlands.

——, J. Desel, A. Oberweis, eds. Business Process Management: Models, Techniques, and Empirical Studies, Lecture Notes in Computer Science, vol. 1806 Springer-Verlag, Berlin, Germany.

Ardhaldjian, R., M. Fahner. 1994. Using simulation in the business process reengineering effort. Indust. Engrg. 26(7) 60–61.

Atluri, V., Wei-kuang Huang. 1996. An extended petri net model for supporting workflows in a multilevel secure environment. DBSec 240–258.

——, ——, Elisa Bertino. 1997. An execution model for multilevel secure workflows. DBSec 151–165.

Baresi, L. et al. 1999. Workflow design methodology. Grefen, Pernici, and Sanchez, eds. Database Support for Workflow Management: The WIDE Project. Kluwer Academic Publishers 47–94.

Baskett, F., K. M. Chandy, R. R. Muntz, F. G. Palacios. 1975. Open,

closed and mixed networks of queues with different classes of customers. J. Assoc. Comput. Machinery 22(2) 248–260.

Basu, A., R. W. Blanning. 1994a. Model integration using metagraphs. Inform. Systems Res. 5(3) 195–218.

——, ——. 1994b. Metagraphs: A tool for modeling decision support systems. Management Sci. 40(12) 1579–1600.

—, ——. 2000. A formal approach to workflow analysis. Inform.Systems Res. 11(1) 17–36.

—, ——. 2001. Workflow analysis using attributed metagraphs. Proc. Hawaii Internat. Conf. System Sci. Maui, HI.

——, ——, A. Shtub. 1997. Metagraphs in hierarchical modeling. Management Sci. 43(5) 623–639.

Bauer, T., P. Dadam. 1997. A distributed execution environment for large-scale workflow management systems with subnets and server migration. Proc. 2nd IFCIS Conf. Cooperative Inform. Systems. Kiawah Island, SC.

Beaudouin-Lafon, M., ed. 1999. Computer Supported Cooperative Work: Trends in Software Series 7. John Wiley and Sons, Chichester, U.K.

Berge, C. 1989. Hypergraphs: Combinations of Finite Sets. North-Holland, Amsterdam, the Netherlands.

Bertino, E., Elena Ferrari, V. Atluri. 1999. The specification and enforcement of authorization constraints in workflow management systems. TISSEC 2(1) 65–104.

Bussler, C. 1999. Enterprise-wide workflow management. IEEE Concurrency 7(3) 32–43.

——, S. Jablonski. 1995. Policy resolution for workflow management. Proc. 28th Hawaii Internat. Conf. System Sci. Maui, HI.

Buzacott, J. A. 1996. Commonalities in reengineered business processes models and issues. Management Sci. 42(5) 768–782.

——, D. D. Yao. 1986. On queueing networks of flexible manufacturing systems. Queueing Systems 1 29–66.

Casonato, R. 1998. Production-class workflow: A view of the market. Gartner Group Research Note 00057684.

Castano, S., M. Fugini. 1999. Rules and patterns for security in workflow systems. DBSec Conf., Chalkidiki, Greece 59–74.

Ceri, S., P. Grefen, G. Sanchez. 1997. WIDE—A distributed architecture for workflow management. Proc. 7th Internat. Workshop on Res. Issues in Data Engrg. Birmingham, U.K.

Christophides, V., R. Hull, A. Kumar, J. Simeon. 2001. Workflow mediation using VorteXML. IEEE Data Engrg. Bull. 24(1) 40–45.

Chrysanthis, P., K. Ramamritham. 1994. Synthesis of extended transaction models using ACTA. ACM Trans. Database Systems 19(3) 450–491.

Desel, J., J. Esparaza. 1995. Free Choice Petri Nets, Volume 40: Cambridge Tracts in Theoretical Computer Science. Cambridge University Press, Cambridge, U.K.

van Dijk, N. M. 1993. Queueing Networks and Product Forms: A Systems Approach. John Wiley and Sons, Chichester, U.K.

Ellis, C. 1999. Workflow technology. M. Beaudouin-Lafon, ed. Computer Supported Cooperative Work, Trends in Software Series, vol. 7. John Wiley and Sons, Chichester, U.K. 29–54.

——, J. Huang. 1997. A comparison of workflow modeling formalisms. Proc. 35th ACM Southeast Conf. Apr. 11.

——, G. Nutt. 1980. Office information systems and computer science. ACM Comput. Surveys 12(1) 27–60.

Ferraiolo, D. F., D. R. Kuhn. 1992. Role-based access control. 15th Na tional Comput. Security Conf. NIST/NSA, 554–563.

——, J. Cugini, D. R. Kuhn. 1995. Role-based access control: Features and motivation. Annual Comput. Security Appl. Conf. IEEE Computer Society Press.

Fowler, M., K. Scott. 1997. UML Distilled. Addison-Wesley, New York. Gates, W. 1999. Business @ The Speed of Thought: Succeeding in the Digital Economy. Time-Warner Books, New York.

Grefen, P., B. Pernici, G. Sanchez, eds. 1999. Database Support for Workflow Management: The WIDE Project. Kluwer Academic Publishers, Twenti, The Netherlands.

——, K. Aberer, Y. Hoffner, H. Ludwig. 2000. CrossFlow: Crossorganizational workflow management in dynamic virtual enterprises. Internat. J. Comput. Systems Sci. Engrg. 15(5) 277–290.

Hammer, M., J. Champy. 1993. Reengineering the Corporation. Nicolas Brealey Publishing, London, U.K.

Hansen, G. A. 1997. Automated Business Process Reengineering: Using the Power of Visual Simulation Strategies to Improve Performance and Profit. Prentice-Hall, Englewood Cliffs, NJ.

Hartmann, P., R. Studt, T. Wewers. 2001. A framework for classifying interorganizational workflow-controlled business processes focusing on quality management. Proc. 34th Hawaii Internat. Conf. System Sci. Maui, Hawaii.

Herring, C., Z. Milosevic. 2001. Implementing B-2-B contracts using BizTalk. Proc. 34th Hawaii Internat. Conf. System Sci. Maui, Hawaii.

Hull, R. et al. 1999. Declarative workflows that support easy modification and dynamic browsing. Conf. Work Activities Coordination and Collaboration (WACC), San Francisco, CA 69–78.

Jablonski, S., C. Bussler. 1996. Workflow Management: Modeling Concepts, Architecture, and Implementation. International Thomson Computer Press, London, U.K.

Johansson, H. J., P. McHugh, A. J. Pendlebury, W. A. Wheeler. 1993. Business Process Reengineering: Breakpoint Strategies for Market Dominance. Wiley and Sons, New York.

Kaplan, S., M. Sawhney. 2000. e-Hubs: The new B-2-B marketplaces. Harvard Bus. Rev. 78(3) 97–103.

Kim, K. 1998. Architectures for very large scale workflow management systems. Ph. D. thesis, Department of Computer Science, University of Colorado, Boulder, CO.

Klein, M., C. Dellarocas. 2000. A knowledge-based approach to handling exceptions in workflow systems. Computer Supported Cooperative Work 9(3–4) 399–412.

Kleinrock, L. 1975. Queueing Systems, vol. 1: Theory. Wiley-Interscience, London, U.K.

Kumar, A., L. Zhao. 1999. Dynamic routing and operational controls in a workflow management system. Management Sci. 45(2).

——, ——. 2001. Workflow support for electronic commerce applications. Forthcoming, Decision Support Systems.

——, W. M. P. van der Aalst, H. M. W. Verbeek. Dynamic work distribution in workflow management systems: How to balance quality and performance? Forthcoming, J. Management Inform. Systems.

Lai, K. Y., T. W. Malone, K-C. Yu. 1988. Object lens: A “spreadsheet”

for cooperative work. ACM Trans. Office Inform. Systems 6(4) 332– 353.

Lawrence, P., ed. 1997. Workflow Handbook 1997. Workflow Management Coalition, John Wiley and Sons, New York.

Lenz, K., A. Oberweis. 2001. Modeling inter-organizational workflows with XML nets. Proc. 34th Hawaii Internat. Conf. System Sci. Maui, HI.

Leymann, F., D. Roller. 2000. Production Workflow, Concepts and Techniques. Prentice Hall, Upper Saddle River, NJ.

Lindert, F., W. Deiters. 1999. Modeling inter-organizational processes with process model fragments. Proc. Workshop on Enterprise-wide and Cross-Enterprise Workflow Management. Paderborn, Germany.

Luqi. 1990. A graph model for software evolution. IEEE Trans. Software Engrg. 16(8) 917–927.

Malone, T., K. Grant, F. Turbak, S. Brobst, M. Cohen. 1987. Intelligent information-sharing systems. Comm. ACM 30(5) 390–402.

Manganelli, R. L., M. K. Klein. 1996. The Reengineering Handbook: A Step by-Step Guide to Business Transformation, Amacom, New York.

March, S., A. Hevner, S. Ram. 2000. Research commentary: An agenda for information technology research in heterogeneous and distributed environments. Inform. Systems Res. 11(4) 327–341.

McCarthy, D. R., U. Dayal. 1989. The architecture of an active database system. Proc. ACM SIGMOD Conf. Management of Data, Portland, OR 215–224.

Morris, D., J. Brandon. 1993. Reengineering Your Business. McGraw-Hill, New York.

zur Mu¨hlen, M. 1999a. Resource modeling in workflow applications. Becker, Zur Mu¨hlen, Rosemann, eds. Proc. 1999 Workflow Management Conf. November 9th, Mu¨nster, Germany 137–153.

——. 1999b. Evaluation of workflow management systems using meta models. Proc. 32nd Hawaii Internat. Conf. on System Sciences, Maui, HI.

Murata, T. 1989. Petri nets: Properties, analysis and applications. Proc. IEEE 77(4) 541–580.

Nyanchama, M., S. L. Osborn. 1999. The role graph model and conflict of interest. ACM Trans. Inform. System Security 2(1) 3–33.

Poyssick, G., S. Hannaford. 1996. Workflow Reengineering. Adobe Press, Mountain View, CA.

Reichert, M., T. Bauer, P. Dadam. 1999. Enterprise-wide and crossenterprise workflow management: Challenges and research issues for adaptive workflows. Workshop Informatik ’99, Paderborn, Germany.

Reijers, H. A., W. M. P. van der Aalst. 1999. Short-term simulation: Bridging the gap between operational control and strategic decision making. Proc. IASTED Internat. Conf. on Modeling and Simulation. IASTED/Acta Press, Anaheim, CA 417–421.

Reisig, W., G. Rozenberg, eds. 1998. Lectures on Petri Nets I: Basic Models, vol. 1491 of Lecture Notes in Computer Science. Springer-Verlag, Berlin, Germany.

Ross, S. M. 1990. A Course in Simulation. Collier Macmillan, London, U.K.

Rusinkiewicz, M., A. Sheth. 1995. Specification and execution of transactional workflows. W. Kim, ed. Modern Database Systems: The Object Model Interoperability, and Beyond. ACM Press, Cambridge, MA 592–620.

Izak Benbasat, Senior Editor. This paper was received on November 12, 2000, and was with the authors 2 months for 1 revision.

Saastamoinen, H. 1995. On the handling of exceptions in information systems. Ph. D. thesis, University of Jyvaskyla, Finland.

Sandhu, R. S., V. Bhamidipati, Q. Manuawer. 1999. The ARBAC97 model for role-based administration of roles. ACM Trans. Inform. System Security 2(1) 105–135.

——, E. J. Coyne, H. L. Feinstein, C. E. Youman. 1996. Role-based access control models. IEEE Comput. 29(2) 38–47.

Sheth, A., W. van der Aalst, I. Arpinar. 1999. Processes driving the networked economy. IEEE Concurrency 7(3) 18–31.

Simon, R., Mary Ellen Zurko. 1997. Separation of duty in role-based environments. Proc. 10th Comput. Security Foundations Workshop (CSFW ‘97) Rockport, MA 183–194.

Staffware. 1999. Staffware GWD Procedure’s Guide, Version 8, Issue 2. Staff ware plc, Berkshire, U.K.

Strong, D. 1992. Decision support for exception handling and quality control in office operations. Decision Support Systems 8(3) 217–227.

SWAP Working Group. 1998. Requirements for simple workflow access protocol. Internet draft, SWAP Working Group, http:// www.ics.uci.edu/ietfswap-, November.

UDDI. 2000. UDDI technical white paper, available at uddi.org-, September.

Wa¨chter, H., A. Reuter. 1991. The ConTract model. A. Elmagarmid, ed. Database Transaction Models for Advanced Applications. Morgan-Kauffman, San Mateo.

WFMC. 1999. Interface 1: Process definition interchange process model, http://www.wfmc.org-.

Winograd, T., F. Flores. 1987. Understanding Computers and Cognition. Addison Wesley, Reading, MA.

Wirth, N. 1977. What can we do about the unnecessary diversity of notation for syntactic definitions. Comm. ACM 20(11) 822–823.

Wise, R., D. Morrison. 2000. Beyond the exchange: The future of B2B. Harvard Bus. Rev. 78(6) 86–96.

Wu, S., A. Sheth, J. Miller. 2000. Task and role combined access control model for workflow systems. Technical report, University of Georgia, Athens, GA.

Zapf, M., A. Heinzl. 2000. Evaluation of generic process design patterns: An experimental study. Business Process Management: Models, Techniques, and Empirical Studies, vol. 1806 of Lecture Notes in Computer Science. Springer-Verlag, Berlin, Germany 83–98.

Zisman, Michael D. 1977. Representation, specification, and automation of office procedures. Ph.D. thesis, The Wharton School, University of Pennsylvania, Philadelphia, PA.
