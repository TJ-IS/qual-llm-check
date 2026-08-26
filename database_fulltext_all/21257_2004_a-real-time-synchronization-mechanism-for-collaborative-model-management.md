---
otero_id: 21257
otero_key: "6Y2ERR2T"
title: "A real-time synchronization mechanism for collaborative model management"
authors: "Soon-Young Huh; Hyung-Min Kim"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00031-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A real-time synchronization mechanism for collaborative model management

Soon-Young Huh<sup>a,</sup>\*, Hyung-Min Kim<sup>b</sup>

<sup>a</sup> Graduate School of Management, Korea Advanced Institute of Science and Technology, 207-32 Cheongryangri-dong, Dongdaemun-gu, Seoul, South Korea

<sup>b</sup>IBM Business Consulting Services, 40F ASEM Tower, Samsung-dong, Kangnam-gu, Seoul, South Korea

Received 13 September 1999; accepted 12 February 2002

Available online 4 April 2003

## Abstract

As mathematical models are increasingly adopted for corporate decision-making, problems arise in departmental information sharing and collaboration around model management systems. When multiple departments are involved in decision-making problems, it is necessary to consider the individual conditions of the multiple departments as a whole from an entire organizational perspective. However, in functionally decentralized organizations, the operational data is usually dispersed in individual departments, thus, the departmental decisions are made separately on the basis of limited information and perspective. This paper proposes an object-oriented data model for developing a collaborative model management system that facilitates not only sharing mathematical models among multiple departments, but also coordinating and propagating ongoing changes in the models on a real-time basis. A prototype system is developed at KAIST on a commercial object-oriented database system called ObjectStore using C++ programming language. <sup>D</sup> 2003 Elsevier B.V. All rights reserved

Keywords: Departmental computing; Collaborative model management; Mathematical models; Model change notification; Object-oriented database management system

## 1. Introduction

As business environments become more competitive and rapidly change, precise and agile analysis is more important and, thus, mathematical models are increasingly adopted to support decision making. As a tool serving such decision-supporting tasks, model management systems (MMS) have been extensively researched on to build a corporate information repository capturing a variety of mathematical models, and to facilitate users to manipulate the models for solving their own departmental business problems [5,10,11,31,34].

Traditionally, model users in the functional departments such as marketing, manufacturing and logistics tend to solve problems and make decisions from their own autonomous department-centered perspectives due to the difficulties in considering the whole condition in an organization [9,27,28,45]. Recently, as global optimality and overall responsiveness at the corporate level are increasingly pursued, model information-sharing across an organization and agile collaborative decision-making are highly emphasized. Many studies in the literature have suggested jointly making corporate decisions to overcome the suboptimal performance of separate decision-making [8,24,45]. In these joint approaches, it is assumed that a centralized authority makes all the decisions simultaneously or jointly pursues the organizational global objectives. However, in reality, it is not easy for a centralized authority to gather all recent information scattered in and maintained by multiple departments. Furthermore, under today’s circumstances in which business rules and market demands are fast-changing, such a centralized decision-making approach is more unrealistic than in the past [28].

Therefore, it is more effective and efficient for multiple departments to individually feed the required information into the model, and then use the computational results collaboratively in making their own departmental decisions. In this situation, if the input dataset’s change initiated by a department does not propagate to the other related departments immediately, then the other departments may make a wrong decision with the old dataset and the incorrect model execution results. In other words, a real-time change notification mechanism is imperative functionality for model collaboration in departmental computing environments. In this paper, we suggest the necessity of model collaboration between multiple departments with a realistic example, and propose a unique departmental collaborative model management framework including a real-time change notification mechanism for supporting tasks requiring collaboration among multiple departments on an ongoing basis.

It is apparent from previous studies on the model management area that there is a rich compilation of research in the development of MMS in general [3,6,11,15,34,36], distributed model management in particular [32,33,38] and the design and management of multiple user interfaces architecture [12,18,39,30]. In particular, to store the represented models in a persistent storage device and support multi-user access to them, several database modeling methods have been developed: relational database [5,10] and object-oriented database (ODBMS) approaches [20,35]. In terms of model representation and storage, in this paper, we adopt generic model concepts [20,21] based on the ODBMS approach, which we proposed in previous studies since it can accommodate the diverse mathematical models in a uniform way and provide fullfledged model management operations, ranging from model storage to model execution. However, in our previous proposals [20,21], we could not encompass the model collaboration concepts and have no model change notification mechanisms.

With respect to the change notification mechanisms, much research has been done in a wide variety of disciplines, especially workgroup computing systems and the database management systems area. The model-view-controller (MVC) architecture [17] developed as a standard user interface in Smalltalk supports change management functionality on transient shared object. However, it cannot manage the changes on a persistent shared object and cannot support a multiuser environment [44], whereas the distributed, objectbased programming systems such as Argus [29], Emerald [23] and Guide [19] provide an environment in which programs consisting of a set of interacting autonomous objects may execute concurrently on multiple processes. However, these systems provide little change management and notification capability among processes and weak transaction management functionality for concurrent multi-user environments. Afterwards, to overcome such limitations, we proposed an object-oriented database model to support multiple users sharing common persistent objects in a client/server computing environment [22]. This paper stems from our previous object-oriented change management framework and uses its basic concepts and constructs. However, in our previous works, there were no constructs and mechanisms for managing models collaboratively between departments and no considerations about triggering necessary actions and storing their results within database systems when the stored data changes, which are imperative to implement collaborative model management functionalities.

In the literature, there have been diverse research efforts on change notification and reflection in the database systems area such as active database systems [14,47], deductive database systems [46] and distributed database systems [1,2]. Usually, the active database systems make use of the Event-Condition-Action rule architecture, in which an event triggers a rule and then related actions are performed if the condition is satisfied. Our proposed change notification mechanism could be considered as an effort to apply these active database concepts into the collaborative model management systems at the point that a modelbase reacts actively to the stored model’s change. However, so far, there have been no researches that apply these active database concepts to the model management area for supporting model collaboration. Therefore, the active database systems proposed in the literature have no change notification mechanisms for managing the dependency relationships between the shared model and the dependent user interfaces and, when the shared model changes, for executing the model again and propagating the changed results appropriately to the user interfaces. In addition, in the deductive database or distributed database systems area, change notification methods were proposed to compute derived data automatically or maintain consistency between stored data. However, these methods usually deal with the change notification mechanisms within database systems, not including the user interface part in the client systems which is main topic of this paper.

This paper is composed of six sections. Section 2 addresses departmental collaborative model management environments with an illustrative mathematical programming model. Section 3 reviews the nature of the generic model concepts which provide the theoretical basis for constructing an object-oriented modelbase. Section 4 presents the concrete object-oriented data model for automatic update of the distributed departmental user interfaces. Section 5 describes the detailed change notifying steps for maintaining consistency between shared models and their user interfaces, and presents a Petri-net model for discussing the properties of the proposed algorithm. Finally, Section 6 summarizes the contributions of this study and suggests further research areas.

## 2. Departmental collaborative model management

When one makes a decision on a business problem, it is necessary to consider the whole condition of the organization in order to seek a corporate global optimum. Along with the technological progress of network and database systems, it becomes increasingly possible that the information resources managed in an organization are utilized from the viewpoint of the entire organization. Since the individual decisionmaking tasks of the multiple departments are interdependent, MMS should be employed to support analyzing and solving business problems from the organizational perspective rather than an individual departmental perspective. For instance, sales forecasts on products by the marketing department serve as a basis for scheduling future production quantities at the manufacturing department. In turn, the capacity of the production facility at the manufacturing department affects the cost structure and, thus, the selling price for the marketing department. However, respective departments in an organization are usually functionally and geographically separated and, thus, the available information for departmental decision-making is restricted to the scope related to their own operations. To overcome such informational limitations, the models managed in MMS should be able to encompass all information factors dealt with by multiple departments, and respective departments should be able to share such models. Therefore, it is necessary for collaborative MMS to support multiple departments in sharing the large-scale mathematical models and cooperating collaboratively on an ongoing basis for agility by inputting business datasets into the common models and utilizing the computational results for their respective business decisions.

As an illustration of a mathematical model relating multiple departments such as manufacturing, marketing and logistics, Fig. 1 presents a single product and multiple periods production and sales scheduling model that is set up to minimize production and storage cost within the production capacity while satisfying the forecasted market demand.

In terms of model execution, since the model presented in Fig. 1 only specifies the general structure of the model, it needs to be instantiated with input datasets from several departments. Fig. 2 presents a collection of input datasets for an illustrative problem with three periods, and also shows the linear programming instantiated by these exemplified input datasets.

As shown in these two figures, the respective mathematical models stored and managed by MMS are comprised of two parts: model structure and model instance. Firstly, the model structure, also known as model schema, represents the general relationships of

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Minimize  $10Qty_{11} + 12Qty_{12} + 14Qty_{13} + 10Qty_{22} + 12Qty_{23} + 10Qty_{33}$ 

subject to  $Qty_{11} + Qty_{12} + Qty_{13} \leq 2000$ $Qty_{22} + Qty_{23} \leq 2000$ $Qty_{33} \leq 3000$ $Qty_{11} = 1500$ $Qty_{12} + Qty_{22} = 1000$ $Qty_{13} + Qty_{23} + Qty_{33} = 3500$ 

production capacity constraints

market demand constraints
</div>

Fig. 2. Model instance and linear programming of the model defined in Fig. 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1) Input Variables
    T : the number of production and sales periods
    ProdCost : production cost per unit product
    StorCost : storage cost per unit product
    ProdCapa $_{t1}$  t1 ∈ {1,..., T} : production capacity in period t1
    SalesFore $_{t2}$  t2 ∈ {1,..., T} : sales forecasts in period t2

2) Decision Variable
    Qty $_{t1\ t2}$  t1 ∈ {1,..., T}, t2 ∈ {1,..., T}, t2 ≥ t1
    : units of the product manufactured in period t1 and sold in period t2

3) Objective Function
    Minimize  $\sum_{t1 \in \{1,\ldots,T\}, t2 \in \{1,\ldots,T\}} (\text{ProdCost} + (t2 - t1) \text{StorCost}) \text{Qty}_{t1\ t2}$ 
    t2 ≥ t1 : total cost over all periods considering production and storage cost

4) Constraints
    $\sum_{t2 \in \{1,\ldots,T\}} \text{Qty}_{t1\ t2} &lt;= \text{ProdCapa}_{t1}$ 
    t1 ∈ {1,..., T}, t2 ≥ t1 : total units manufactured in period t1 must not exceed the production capacity of period t1
    $\sum_{t1 \in \{1,\ldots,T\}} \text{Qty}_{t1\ t2} = \text{SalesFore}_{t2}$ 
    t2 ∈ {1,..., T}, t2 ≥ t1 : total units sold in period t2 must be equal to the sales forecast of period t2
</div>

Fig. 1. Model structure of a production and sales scheduling problem.

elements composing a mathematical model and describes the business problems to be solved for decision supporting. Fig. 1 shows an example of the model structure and it should be stored in a corporate modelbase to be accessed and shared by multiple users in an organization. Secondly, the model instance represents the necessary datasets describing specific business conditions. Fig. 2 shows an illustration of the model instance and it enters into the model structure to obtain a solution of the specific business problem. Therefore, the model structure is explicitly separated from the model instance, and many kinds of model instances can be applied to the same model structure. Practically, if the business condition changes, the model instance should be evolved accordingly to reflect the change. Meanwhile, the executable model, the model structure instantiated by a model instance, can be solved or executed by some solver algorithms such as Simplex method.

As mentioned above, the business problems considering the whole condition and pursuing the global optimum in an organization require the information about multiple operational functions such as manufacturing, logistics and marketing, and in functionally

```txt
1) Input Datasets (Model-Instance)
• Number of Periods (T) = 3
• Production Cost (ProdCost) = 10
• Storage Cost (StorCost) = 2

• Production Capacity (ProdCapa) • Sales Forecasts (SalesFore)

period capacity period forecast
1 2000 1 1500
2 2000 2 1000
3 3000 3 3500
```

2) Linear Programming Model Instantiated by the Input Datasets decentralized organizations, the latest datasets are scattered into and maintained by respective departments. For instance, in the above example model, among the input variables, production cost (Prod-Cost) and production capacity (ProdCapa) can be delivered by the manufacturing department, while sales forecasts (SalesFore) and storage cost (Stor-Cost) can be offered by the marketing department. In terms of the computational results, the manufacturing department is more interested in the future production schedule, while the marketing department is concerned with the expected delivery and inventory amounts as well as the future sales schedule. Fig. 3 provides two exemplified departmental user interfaces that can be used independently in the manufacturing department and the marketing department with respect to the production and sales scheduling model defined in Fig. 1.

As shown in the figure, the manufacturing department, through its user interface (Fig. 3a), can provide the production cost and production capacity as input data to the model and can get the production schedule in the future as the results of the model execution. Moreover, the marketing department can offer the sales forecasts representing the expected market demand and storage cost as input data and obtain the expected delivery and sales schedule with its user interface (Fig. 3b). To be sure, these two departments access and execute the same model stored in a modelbase and the model has been built encompassing these two departments’ conditions. On the other hand, in such capacity, when a certain department alters a part of the model instance (input data), other departments that are interested in the model execution results have to be notified. For instance, when the production cost is lowered by the manufacturing department, the change has an effect not only on the production schedule used by the manufacturing department but also on the delivery and sales schedule used by the marketing department. Therefore, the changes in the model instance should be reflected in the departmental user interfaces such as those presented in Fig. 3.

![](/api/attachments/6Y2ERR2T/fulltext/images/e0803d26e13aaade137386d7c58ed55a83ad21f259ed74c7c9e1e645fac0de8e.jpg)  
(a) Manufacturing Department's User-Interface

![](/api/attachments/6Y2ERR2T/fulltext/images/addc4cbb8ac5a0a68caa9004cef819a8e57218a744064dc8984ed39d509a9306.jpg)  
(b) Marketing Department's User-Interface  
Fig. 3. Examples of departmental user interfaces of the production and sales scheduling model.

As such, to support the multiple departments in sharing a common model and doing their tasks cooperatively, several requirements can be highlighted. First, various mathematical models including model structure and model instance should be stored in a corporate modelbase server in a uniform way and scan be accessed by multiple departmental users concurrently. To do so, the constructs for building a modelbase should have a general structure for accommodating various mathematical models and they should provide full-fledged model management operations such as retrieval, update and execution capabilities. Second, respective departments should be able to have unique departmental user interfaces satisfying their own information needs on the shared model, and the altered input data by one department and the revised computational results should be delivered to other related departments with no time delay. Specifically, under the collaborative model management environments, when changes are made to a hared model, it can cause inconsistency between the model revised by a department and the user interfaces rendered to other departments that are derived from the original model. This seemingly inconsequential anomaly can do serious harm, including undermining the validity of their understanding of the problem, causing impaired communication among the participating departments and, ultimately, questioning the efficacy of the cooperative tasks among multiple departments. Thus, providing individual departments with consistent and synchronized user interfaces of the shared model becomes a key issue in order to accomplish the goal of collaborative MMS. In this study, we propose the collaborative model management framework satisfying such requirements, and we adopt an objectoriented database system as an implementation platform for combining the model management constructs and the change notification mechanisms in a single paradigm.

## 3. Review of the generic model concepts: modelbase construction using an object-oriented database system

In order to utilize the mathematical models as shared information resources in an organization, they should be stored in a modelbase and accessible to multiple departments concurrently. In general, the mathematical models maintained in a modelbase can be represented by hierarchical structures for systematic administration in MMS [4,13,16,42]. For instance, optimization models consist of multiple algebraic representations including objective function or constraints and, according to the problem at hand, these components might have subelements such as various specific parameters and decision variables. Therefore, a specific mathematical model can be described by a hierarchical tree structure and it is possible that respective nodes in the tree structure are represented by object-oriented concepts [20,26,35]. Along the object-oriented approach, in this study, we use generic model concepts [20,21] to accommodate diverse models in terms of a systems approach and, thus, the proposed modelbase stores a collection of models by breaking down the models into their lower level components on the basis of object-oriented database systems. Because the generic model concepts can provide object-oriented constructs for storing various mathematical models in a modelbase consistently, the useful mechanisms that object-oriented methodology generally offers such as inheritance, polymorphism and encapsulation [25] can be utilized in constructing a modelbase. The core constructs and concrete storing structure of the generic model concepts are described below and more detailed information can be found in our previous works [20,21].

In generic model concepts, a generic model characterized by a generic model type represents a mathematical model as an abstraction of a real world problem and consists of three kinds of ports: inports, outports and midports. Ports have a set of attributes and operations to describe the information pertaining to algebraic expressions and data values. The inport and outport admit input datasets and produce computational results, respectively, while the midport carries the rest of the model such as the model constraints and the model objective function. Ports are grouped into modules that are characterized by the module type. Modules can be integrated to form a generic model, which is at the highest level in generic model hierarchy. The core constructs making up a generic model and their relationships can be represented by a hierarchical structure as depicted in Fig. 4 using Object Modeling Technique (OMT) [43]. Here are brief descriptions of the OMT notations. The notations use boxes and lines to depict classes of objects and relationships between the objects, respectively. In a class box, there are three rows: the top row denotes the name of the class, the middle row displays the attributes of the class and the bottom row represents the operations. Among the relationships, inheritance relationship is denoted by a triangle on the line, and aggregation relationship is represented by a diamond shape. Multiplicity of association is pictorially represented as a black circle at the endpoint of a line depicting a relationship.

![](/api/attachments/6Y2ERR2T/fulltext/images/eac7030193cb4ccb13960763569cb075b6bef0eae2292aed4e8cdd0c35147854.jpg)  
Fig. 4. Object model of generic model concepts.

Regarding these concepts, the GenericModelType is viewed as the highest aggregation of a number of modules—the ModuleType. A module, in turn, consists of a set of ports—the PortType. Actually, the childModules attribute of the GenericModelType and the childPorts attribute of the ModuleType are objectvalued attributes (OVA) that point to the module type objects and the port type objects belonging to the generic model and the module, respectively. Among the operations in the GenericModelType, solve() operations are used for executing the specific instantiated model and obtaining a solution of the problem. Meanwhile, three port types, InportType, MidportType and OutportType, inherit the properties of the Port-Type and all components building a mathematical model, such as objective function, constraints and parameters, become belonging to one of these three port types in the lowest level. As mentioned above, the InportType and the OutportType store and manage input and output datasets, respectively, while the MidportType manages the rest of the model such as algebraic formulations representing the objective function and constraints.

Using such object-oriented constructs provided by the generic model concepts, the mathematical models shared by multiple users can be stored and managed in a modelbase based on object-oriented database systems. Fig. 5 shows an illustration of the objectoriented database structure storing the production and sales scheduling model presented in Figs. 1 and 2 using OMT’s instance diagram.

In the figure, the illustrated production and sales scheduling model consists of five modules: Index module, Parameter module, Constraint module, Objective module and Variable module. Among these, the index and parameter modules take the inports of the model as the child ports, which should be instantiated by departmental model users. In this example, all inports have been instantiated by the model instance presented in Fig. 2. On the other hand, the constraint and objective modules contain the midports as the child ports and the specific algebraic expressions are stored in the expression attribute in the MidportType. Lastly, the variable module is linked to the outport of this model and after the model execution, the computational results are stored in this outport. Then, these stored results are delivered to multiple departmental model users.

As mentioned above, the model instance stored in inports of a model can change due to the dynamic nature of the operating environment and the inherent uncertainty associated with the problems. Therefore, as the input datasets stored in the inports evolve, the output data maintained in the outports should be recalculated and the related model users scattered in multiple departments should be notified of the new computational results. In this study, we propose the mechanisms for automatic user interface update in collaborative modeling environments and the following sections describe the mechanisms in more detail.

![](/api/attachments/6Y2ERR2T/fulltext/images/3716856e68db9cf6269e7c9fc2f4521c099f69a0d1016bee501d17d903f187d3.jpg)  
Fig. 5. Instance diagram of the production and sales scheduling model based on the generic model concepts

## 4. Object-oriented model for automatic change notification to departmental user interfaces

The proposed automatic change notification mechanism provides the object-oriented constructs for (1) managing the dependency relationships between the shared models and their dependent departmental user interfaces and (2) performing change notification activities when some changes occur at the shared model. In this study, the collaborative model management framework is based on the following client/ server architecture, because it may seem to be a typical model management scenario: a corporate modelbase server stores the common models and the clients located in many departments access and manipulate the shared models concurrently. In this situation, those constructs performing change notification activities are designed generally independent of MMS and they are inherited to the model management constructs based on the generic model concepts explained above. Therefore, the two kinds of constructs (change management constructs and model management constructs) are separated structurally and the proposed change management constructs can be applied and extended easily to not only MMS but also the other application systems where the change notification functionality is needed. The core constructs for managing dependency relationships dynamically according to the creation and deletion of the user interfaces, and for maintaining those user interfaces reflecting an identical image of the shared model all the time, can be defined as follows.

. A supporter is a common object being shared concurrently by multiple users and usually stored in a persistent memory such as database systems. The production and sales scheduling model described in Fig. 5 is an example of a supporter and changes are made to such supporter object.

. An observer is an object providing visual representation of the supporter and is affected by the supporter’s change. Usually, it is created and managed in a transient memory such as the client’s cache memory, and the departmental user interfaces presented in Fig. 3 are the examples of the observer object.

. A dependency manager is an object for keeping dependency relationships between the supporters and their dependent observers (concretely between shared models and their departmental user interfaces in the model management context). Especially, in client/ server environments, to support the steps in change notification effectively, we divide the dependency relationship management mechanism into two levels. At the server level, the external dependency manager manages the dependency relationships between the supporter and the dependent clients containing observers, while, at the individual client level, the internal dependency manager controls the dependency relationships between the supporter and its specific observers created in the client. This two-level dependency management mechanism is explained in more detail below.

. A change container is an object for maintaining the contents of the change occurred in a supporter object. Because the supporter objects are stored in a database server, and accessed and modified by multiple users concurrently, the update operations to alter the supporter can be terminated unsuccessfully. Therefore, when some changes are made to a supporter, firstly, the contents of the change are registered to a change container object. Thereafter, only if the database transaction having the update operations is finished successfully, the contents of the change kept in a change container object are delivered to the dependent clients.

Fig. 6 shows the core constructs and their relationships for automatic user interface update using OMT [7,43]. In the figure, there are five classes which were described above and the model management constructs such as the classes for storing models using the generic model concepts and the classes for representing the departmental user interfaces inherit the properties of the Supporter class and the Observer class, respectively.

In the figure, the Supporter class represents the shared information resources such as mathematical models in an organization, while the Observer class expresses their visual representation such as the departmental user interfaces on the shared models. Therefore, when the contents of the supporter object change, then the observer objects should be able to reflect the supporter’s change because they are the

![](/api/attachments/6Y2ERR2T/fulltext/images/8cd93d6788a9a984162dcb0d351b86b847d2331a3b4ab2a0d79e801579766869.jpg)  
Fig. 6. Object model for automatic user interface update in MMS.

dependent objects of the supporter object. As the dedicated dependency-maintaining tools, there are two kinds of dependency relationship maintenance classes: the ExternalDependencyManager and the InternalDependencyManger. As mentioned above, at the server side, the ExternalDependencyManger class manages the dependency relationships between the supporter model and its dependent clients, and it has the supporter attribute as a key and the dependentClients attribute as its values. On the other hand, at the individual client side, the InternalDependency-Manager manages the dependency relationships between the supporter model and its specific observers created in the client itself, and it has the supporter attribute as a key and the dependentObservers attribute as its values. To illustrate this two-level dependency maintenance mechanism, Fig. 7 shows a situation where one modelbase server interacts with two departmental clients (CL1 for the manufacturing department and CL2 for the marketing department). Shaded elements such as the rectangle (A) and triangle (B) represent the models stored in a modelbase, whereas the transparent elements in an oval represent the user interfaces created in the clients. At the client level, in order to manage the dependency relationship between a supporter and its internally created user interfaces, each client contains an Internal Dependency Manager. At the server level, to handle the dependency relationship between a supporter model and its dependent clients, the modelbase server is equipped with an External Dependency Manager. In the figure, three observers for the supporter model A are created in CL1 (a1, a2) and CL2 (a3), while only one observer of model B is created in CL2 (b1). In addition, through these two Dependency Manager objects, the dependency relationships between the supporter models (A, B) and their observers (a1, a2, a3, b1) are managed at the server and client sides, respectively.

As such, by managing the dependency relationships between the stored model and departmental user interfaces using the two dependency managers, the server and clients are able to maintain their own information independently. In so doing, the network load needed for notifying changes can become significantly less than managing the whole dependency information on the server side only. Specifically, as the number of departmental clients and the number of model user interfaces created in each client increase, this two-level dependency management mechanism becomes beneficial.

![](/api/attachments/6Y2ERR2T/fulltext/images/a92fcd2a048a2f64ee14f93393c8780d29c630f511945271a1646f171fd9527d.jpg)  
Fig. 7. Internal and external dependency manager.

Such dependency relationships are generated when a new observer object is created in a client. More precisely, when a new departmental user interface is created, the registerObserver() operation of the Observer class depicted in Fig. 6 is invoked to register the new dependency relationships in the two kinds of dependency manager objects. Conversely, when the user interface is removed, the unregisterObserver() operation is invoked to delete the dependency relationships from the dependency manager objects. On the other hand, when some changes occur in a supporter object, the registerChange() operation of the Supporter class is invoked internally and the contents of the change are maintained in the aspects attribute of the ChangeContainer class chronologically. Then, the sendUpdate() operation is triggered to send an update request message to all the registered observers. Upon receiving the requests, the respective observer objects execute the updateObserver() operation of the Observer class to modify their status accordingly.

The proposed class definitions for Supporter and Observer are generically designed for managing the dependency relationships and the change notification so that they can be easily applied to the collaborative MMS using the inheritance mechanism. As shown in Fig. 6, the Supporter class can be used as a super-class of the generic model classes constructing a modelbase, while the Observer class can be used as a superclass of the departmental user interface. Both subclasses can be augmented with additional structural attributes and functional operations on top of those in the super-classes. Moreover, the operations in Supporter and Observer classes can be customized to suit collaborative model management functionality since most of the operations are declared as abstract forms. Consequently, the super-classes take care of the generic automatic user interface update tasks, while the subclasses focus on the collaborative model management tasks.

## 5. Change notifying steps in collaborative model management environments

In distributed client/server computing environments, in order to give notification of the changes that occurred in a modelbase server to clients dispersed in many departments automatically, some dedicated processes taking full charge of communication and change coordination tasks are necessary at both the server side and the client side. The Change Notification Server and the Change Notification Client come to play such roles and the two-level dependency relationship management mechanism is embodied in these two processes. The Change Notification Server is the change managing process on the server side, while the Change Notification Client represents the client side, and these two processes have operations to support communications between server and client. In the change notification steps, the Change Notification Server refers to the external dependency manager to find dependent clients containing user interfaces scattered in various departments, while the Change Notification Client uses its internal dependency manager to know what kind of user interfaces are created in the client itself.

With the elements of the mechanisms all laid out thus far, the following description shows how the Change Notification Server and the Change Notification Client interact with each other to play their respective roles when a new observer object is created or a model change is encountered. All steps can be presented in three phases. Phase I includes the steps for maintaining dependency relationships, while Phase II and III are change notification courses in a server side and in a client side, respectively. To describe the detailed sequence involving dependency management and change notification, we can depict all the steps using an event trace diagram [43] as shown in Fig. 8. The event trace diagram is effective in describing the sequence of events and the objects exchanging events. In the diagram, an individual participating object and event are represented by a vertical line and a horizontal arrow, respectively, and time goes downwards.

In Phase I, when a new observer (a departmental user interface) is created in a client, the communication connection between a modelbase server and its client is established and the contents of the model stored in a modelbase are delivered to the client to visually represent it on the observer. Then, the fact that a new observer was created is notified to its Change Notification Client in order to register the dependency relationship between the supporter model and a newly created dependent observer in the internal dependency manager of each client. Similarly, this fact is also notified to the Change Notification Server by the

![](/api/attachments/6Y2ERR2T/fulltext/images/d45218b9c50cb6467849e7dcc50647d73ffc82980673cd26c4b432e1cbcf1481.jpg)  
Fig. 8. An event trace diagram on change notifying steps.

Change Notification Client in order to register the dependency relationship between the supporter model and the dependent client containing the observer in the external dependency manager residing at a modelbase server.

Thereafter, if some departments modify the supporter model, Phase II and III are started automatically to notify the change to other related departments immediately. First, Phase II pertains to the change notification steps in a modelbase server. When a user changes a model instance through the observer in his or her client, the database transaction having an update operation modifies the model instance stored in a modelbase. Then, the contents of the change accumulate in a ChangeContainer object linked to the changed supporter model. After the update operations are ended, the model is executed again with the changed model instance. New model execution makes a change at the instance of the generic model’s outports (explained in Section 3). In addition, the change contents of the outports are added to the Change-Container object. Only if the whole model change and execution steps are terminated successfully will the changed supporter model send a message to the Change Notification Server to begin subsequent change notification steps. Receiving the message, the Change Notification Server refers to its external dependency manager to find the clients containing dependent observers on the changed model and gets the dependent clients as a result.

Second, Phase III is related to the change reflection steps in the client. As explained before, since many kinds of user interfaces can exist in various departments according to their information needs, the notified change contents should be reflected on the user interfaces appropriately depending on the form of the individual user interface. Actually, the detailed operations for change reflection on the individual departmental user interfaces are implemented in the subclasses derived from the Observer class according to their representational style as explained in Fig. 6. Therefore, each user interface is able to reflect the notified model changes suitably to satisfy its representational properties. In Phase III, if the client containing the dependent observers is notified of the model changes (including model execution results), the Change Notification Client uses its internal dependency manager to search for the specific observers existing in the client. Then, the found observers are updated adequately to reflect the changes of the model.

The proposed change notification algorithm for supporting collaborative model management can be represented with a Petri-net graph [40,41] for examining its properties as shown in Fig. 9. The Petri-net view of a system concentrates on two primitive concepts: events and conditions. Events are actions that take place in the system. The occurrence of these events is controlled by the states of the system described as a set of conditions. In the Petri-net graph, a condition is represented by a circle and an event by a bar between two conditions. In addition, a token is represented by a black dot in the circle, which used to define the execution of a Petri-net. Thus, the token’s position represents the execution state of a Petri-net and its position may change during the Petri-net’s execution.

With the Petri-net graph specified in Fig. 9, several properties of the proposed change notification algorithm can be discussed. To examine the properties of the Petri-net model, the reachability tree can be used for representing the reachability set of a Petri-net [37,40]. In the reachability tree, a marking is used for representing the state of a Petri-net graph, thus, it expresses an assignment of tokens to the conditions of a Petri-net graph. For example, marking (1, 0, 0, 1, 0) means the initial state of the Petri-net model drawn in

Fig. 9 that condition C1 and C4 have one token, respectively, and other conditions (condition C2, C3, C5) have no token. In addition, from the model management system’s perspective, it means that the modelbase server is waiting for a model instance change and at the same time the client system is waiting for any change notification from the server. At this state, when a model instance change occurs (the event E1 occurs), then the marking is translated into the other marking (0, 1, 0, 1, 0), because the token that resided in the condition C1 has moved to the condition C2. Through this method, the exhaustive reachability tree of the Petri-net model in Fig. 9 can be depicted as shown in Fig. 10.

The reachability tree depicted in Fig. 10 enumerates the whole cases of the conditions passed by at the change notification process. Thus, through the tree, reachability, boundedness and liveness of the proposed algorithm’s Petri-net model can be examined. Firstly, the reachability means all the proposed notification steps are realized as designed and it can be shown by the fact that a token pass by all conditions in the Petri-net graph. In Fig. 10, there are five markings (from M1 to M5), and among these markings condition 1 has a token in M1, condition 2 in M2, condition 3 and 4 in M3, and condition 5 in M4. Therefore, all conditions have a token in the tree and we can tell all conditions are reachable in the algorithm. Secondly, the boundedness means that the proposed algorithm is a finite state algorithm and it can be shown by the fact that all conditions have finite number of tokens in the reachability tree. As shown in the Fig. 10, the number of tokens in each condition is either 0 or 1, thus, it can be said that the Petri-net model is bounded and this algorithm has finite state cases in all times. Lastly, the liveness means the proposed mechanism has no deadlock situation and it can be shown by the fact that there exists no dead node (a node where any event cannot be occurred) in the reachability tree. As shown in the tree, all the leaf nodes are representing the initial condition again, and it means any transition sequence leads the state of the system to the initial condition. Therefore, it can be said that the proposed mechanism has no deadlock case, because there is no dead node in the graph.

![](/api/attachments/6Y2ERR2T/fulltext/images/5eee78cc2b28e1b3e4104e6063dd248069e6c463450a3ab0def027e3e72d2887.jpg)  
Fig. 9. Petri-net graph of the change notification algorithm.

![](/api/attachments/6Y2ERR2T/fulltext/images/3beecca7126f61d7a8e144f8d71a3f5c79ed2ddc29aba4d136011ea7e5af348d.jpg)  
Fig. 10. Reachability tree of the Petri-net model described in Fig. 9.

As explained thus far, through the proposed automatic user interface update mechanism, when some changes occur in the shared model, the contents of the changes and the revised model execution results can be conveyed to the related departments with no time delay. Consequently, all users located in many departments using the model concurrently are able to maintain their own user interfaces consistent with the shared model at all times.

## 6. Conclusion

In this paper, we proposed the collaborative model management framework that (1) enables multiple departments to share a large-scale mathematical model and (2) supports an automatic model change notification mechanism for synchronizing the various departmental user interfaces on a real-time basis.

As a decision-supporting tool, MMS can facilitate storing and manipulating mathematical models in an organization. As business environments become more complicated, these systems are increasingly in demand to obtain precise and quantitative analytical results. Moreover, in making decisions with regard to business problems, it is necessary to consider the whole condition of the various operational functions in an organization. In this sense, to support departmental decisionmaking from an entire organizational standpoint, respective departments need to utilize all information generated or maintained by various departments. However, in functionally decentralized organizations, since individual departments are dispersed in an organization and they have only limited information related to their tasks, they are inclined to make decisions from the viewpoint of their own departments. Therefore, to overcome such informational limitations of the respective departments and support collaboration among multiple departments on an ongoing basis, we suggested the framework based on object-oriented paradigm for sharing a common model and maintaining consistency between multiple departments.

The collaborative model management framework proposed in this study encompasses the following characteristics. First, generic model concepts are used to accommodate diverse mathematical models in a uniform way, and object-oriented database management systems (ODBMS) are adopted as an implementation platform. The ODBMS approach specifically ensures that the collaborative model management architecture is more reliable and secure under a multi-user computing environment than in a proprietary file system approach. Second, the models stored in a modelbase are concurrently accessed and manipulated by multiple departments through their departmental user interfaces, although the user interfaces are different. Depending on each department’s unique tasks and information needs, the datasets that respective departments can offer to the common model and the computational results that the departments want to obtain are different among each other. The proposed collaborative MMS are able to support the various departmental user interfaces with the same model and through these user interfaces the respective departments can use the shared model from their own perspectives pursuing organizational global optimum. Third, the changes of the model initiated by a certain department and the revised computational results followed by the changes are automatically and immediately propagated to the other related departments. In particular, since each department has its unique departmental user interface on the shared model, the notified changes are reflected in the user interfaces appropriately according to each representational style.

A prototype system for the proposed collaborative modeling environment, supporting the multiple departmental user interface presentation and change coordination, has been developed and tested on a Windows NT platform using an object-oriented database system called ObjectStore [25] and C++ programming language. There are two directions for future research. First, complicated and domain-specific rules for various user interface updating strategies such as selective updating or delayed updating can be encompassed in the proposed framework. Second, the mechanisms proposed in this paper can be extended and applied to virtual organization and supply chain management areas where multiple partner companies do their jobs collaboratively to achieve a common objective.

## References

[1] M. Ahamad, M.H. Ammar, S.Y. Cheung, Replicated Data Management in Distributed Systems, Readings in Distributed Computing Systems, IEEE Computer Society Press, California, 1994.

[2] B. Awerbuch, L.J. Schulman, The maintenance of common data in a distributed system, Journal of the Association for Computing Machinery 44 (1997) 86 – 103.

[3] H.K. Bhargava, R. Krishnan, Computer-aided model construction, Decision Support Systems 9 (1993) 91 – 111.

[4] J. Bisschop, A. Meeraus, On the development of a general algebraic modeling system in a strategic planning environment, Mathematical Programming Study 20 (1982) 1 – 29.

[5] R. Blanning, A relational framework for join implementation in model management, Decision Support Systems 1 (1985) 69 – 82.

[6] R. Blanning, Model management systems: an overview, Decision Support Systems 9 (1993) 9 – 18.

[7] G. Booch, J. Rumbaugh, I. Jacobson, The Unified Modeling Language, User Guide, Addison Wesley, New York, 1999.

[8] W.W. Damon, R.A. Schramm, Simultaneous decision model

for marketing, Production, and Finance, Management Science 19 (1972) 161– 172.

[9] X. de Groote, Flexibility and marketing/manufacturing coordination, International Journal of Production Economics 36 (1994) 153– 167.

[10] D. Dolk, Model management and structured modeling: the role of an information resource dictionary system, Communications on Association for Computing Machinery 31 (1988) 704–718.

[11] D. Dolk, An introduction to model integration and integrated modeling environments, Decision Support Systems 10 (1993) 247–254.

[12] E.F. Ellison, G. Mitra, UIMP: user interface for mathematical programming, Association for Computing Machinery Transactions on Mathematical Software 8 (1982) 229 – 255.

[13] R. Fourer, D. Gay, B. Kernighan, A mathematical programming language, Management Science 36 (1990) 519 – 554.

[14] E. Gamma, R. Helm, R. Johnson, J. Vlissides, Design Patterns: Elements of Reusable Object-Oriented Software, Addison Wesley, New York, 1994.

[15] A. Geoffrion, An introduction to structured modeling, Management Science 33 (1987) 547 – 588.

[16] A. Geoffrion, The SML language for structured modeling: level 1 and 2, Operations Research 40 (1992) 38 – 57.

[17] G. Grasner, S. Pope, Cookbook for using the model-viewcontroller user interface paradigm in smalltalk-80, Journal of Object-Oriented Programming 1 (1988) 26 – 49.

[18] H.J. Greenberg, F.H. Murphy, Views of mathematical programming models and their instances, Decision Support Systems 13 (1995) 3 –34.

[19] D. Hagimont, P.Y. Chevalier, A. Freyssinet, S. Krakowiak, S. Lacourte, J. Mossiere, X. Rousset, Persistent Shared Object Support in the Guide System: Evaluation and Related Work, Proceedings of OOPSLA, Oregon, USA (1984) 129– 144.

[20] S.Y. Huh, Modelbase construction with object-oriented constructs, Decision Sciences 24 (1993) 409 – 434.

[21] S.Y. Huh, Q.B. Chung, A model management framework for heterogeneous algebraic models: object-oriented database management systems approach, Omega 23 (1995) 235 – 256.

[22] S.Y. Huh, D.A. Rosenberg, Dependency maintenance for collaborative computing environment, Journal of Systems and Software 34 (1996) 231– 246.

[23] E. Jul, H. Levy, N. Hutchinson, A. Black, Fine-grained mobility in the emerald system, Association for Computing Machinery Transactions on Computer Systems 6 (1988) 109 – 133.

[24] D. Kim, W.J. Lee, Optimal joint pricing and lot sizing with fixed and variable capacity, European Journal of Operational Research 109 (1998) 212 – 227.

[25] C. Lamb, G. Landis, J. Orenstein, D. Weinreb, The objectstore database system, Communications of the Association for Computing Machinery 34 (1991) 50 – 63.

[26] B. Le Claire, R. Sharda, An Object-Oriented Architecture for Decision Support Systems, Proceedings of the International Society for Decision Support Systems Conference, Austin, TX (1990) 567– 586.

[27] W.J. Lee, D. Kim, Optimal and heuristic decision strategies for

integrated production and marketing planning, Decision Sciences 24 (1993) 1203– 1213.

[28] W.J. Lee, K.C. Lee, A meta decision support system approach to coordinating production/marketing decisions, Decision Support Systems 25 (1999) 239– 250.

[29] B. Liskov, Distributed programming in Argus, Communications on Association for Computing Machinery 31 (1988) 300– 312.

[30] P.C. Ma, F.H. Murphy, E.A. Stohr, A graphics interface for linear programming, Communications on Association for Computing Machinery 32 (1989) 996– 1012.

[31] M. Mannino, B. Greenberg, S. Hong, Model libraries: knowl edge representation and reasoning, ORSA Journal of Com puter 2 (1990) 287– 301.

[32] M.K. Mayer, Future trends in model management systems: parallel and distributed extension, Decision Support Systems 22 (1998) 325 – 335.

[33] W.A. Muhanna, Issues in Distributed Model Management Systems, Proceedings of the 11th Annual International Conference on Information Systems, ACH (1990) 231 – 242.

[34] W.A. Muhanna, SYMMS: a model management system that supports model reuse, sharing, and integration, European Jour nal of Operational Research 72 (1994) 1093– 1123.

[35] W.A. Muhanna, An object-oriented framework for model management and DSS development, Decision Support Systems (1995) 214– 243.

[36] W.A. Muhanna, R.A. Pick, Meta-modeling concepts and tools for model management: a systems approach, Management Science 40 (1994) 553–565.

[37] T. Murata, Petri Nets: properties, analysis and application, Proceedings of the IEEE 77 (1989) 541–580.

[38] I. Murphy, D. Ghosh, A. Moffett, Allocating modelling resources in distributed model management systems, Annals of Operation Research 38 (1992) 397– 419.

[39] F.H. Murphy, E.A. Stohr, A. Asthana, Representation schemes for mathematical programming models, Management Science 38 (1992) 964– 991.

[40] J.L. Peterson, Petri Net Theory and the Modeling of Systems, Prentice-Hall, New Jersey, 1981.

[41] C. Petri, Kommunikation mit Automaten, PhD dissertation, University of Bonn (1962).

[42] A. Roy, L. Lasdon, J. Lordman, Extending planning languages to include optimization capabilities, Management Science 32 (1986) 360– 373.

[43] J. Rumbaugh, M. Blaha, W. Premerlani, F. Eddy, W. Lorensen, Object-Oriented Modeling and Design, Prentice-Hall, New Jersey, 1991.

[44] Y.P. Shan, An Event-driven Model-View-Controller Framework for Smalltalk, Proceedings of OOPSLA, New Orleans, LA (1989) 347– 352.

[45] A.G. Sogomonian, C.A. Tang, Modeling framework for coordinating promotion and production decisions within a firm, Management Science 39 (1993) 191 – 203.

[46] J.D. Ullman, Principles of Database and Knowledge-Base Systems, Computer Science Press, Maryland, 1988.

[47] J. Widom, S. Ceri, Active Database Systems: Triggers and Rules for Advanced Database Processing, Morgan Kaufmann Publishers, California, 1996.

![](/api/attachments/6Y2ERR2T/fulltext/images/8a61df86285c48ba97e9f3aa6004382ec91955c1d69bed8af4b7c63e6f650615.jpg)

Soon-Young Huh is a Professor of Management Information Systems at the KAIST. He received his PhD from the University of California, Los Angeles. Dr. Huh has published articles in such journals as Decision Sciences, International Journal of Intelligent Systems in Accounting, Finance and Management, Omega, Journal of Systems and Software. His research deals with abstraction database application to business systems, model management, object-ori-

ented database approach to decision support systems and intelligent approaches in financial trading systems. His e-mail address is syhuh@kgsm.kaist.ac.kr.

![](/api/attachments/6Y2ERR2T/fulltext/images/b779c1eb43cee50766aa5a17698ebab1264333e611108b454a5cbec4541c3ad5.jpg)

Hyung-Min Kim is a principal consultant of IBM Business Consulting Services. He received his PhD from the KAIST, and has worked for business consulting service firms after completing his PhD study. His research interest is in the areas of model management systems, knowledge management systems, object-oriented database approach to decision support systems and customer relationship management systems. In particular, he has an interest in

practical application of such systems in the real business world. His e-mail address is hyungmin.kim@kr.ibm.com.
