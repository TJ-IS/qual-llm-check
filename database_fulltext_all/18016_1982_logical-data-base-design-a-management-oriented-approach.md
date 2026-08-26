---
otero_id: 18016
otero_key: "5YFBUN3C"
title: "Logical data base design: A management-oriented approach"
authors: "Arun Sen"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90040-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logical Data Base Design: A Management-Oriented Approach

Arun SEN \*

Pennsylvania State University, University Park, PA 16802, USA.

A logical data base consists of data definitions and data relationships. It is typically very large and complex even for a small organization, but it is generally designed in an ad hoc manner. However, several approaches have recently been proposed that allow for a systematic logical data base design.

To make a data base more useful to the managers, it is imperative to encourage and obtain their involvement in the initial phase of the logical data base design. "Surface semantic models" are used in the logical data base design process to increase this involvement. A special type of this, called a "hierarchical external view model", is proposed. It has been successfully used to develop a logical data base for the Department of Aging in Pennsylvania.

Keywords: Surface semantic model, data base management system, logical data base design, organizational hierarchy, external view, conceptual view, requirement analysis, view modeling, hierarchical views, managerial activities, managerial decisions.

## 1. Introduction

The past 15 years have witnessed a rapid growth in the area of Data Base Management Systems (DBMS). It is a software package responsible for accessing data efficiently and for maintaining its integrity as well as system security. The term “integrity” means ensuring – as much as can be ensured – that the data in the data base is accurate at all times; “security” means the protection of the data against unauthorized disclosure, alteration, or destruction.

The design of such a system involves two steps. The first step is logical data base design; i.e., the process of creating data structures that satisfy the users' needs. The second is physical design, which includes the design of storage structure, the acces mechanisms, the implementation of security, and the choice of hardware.

The physical design has received considerable attention for a long time. As a result, much research has been reported [4] and many commercial packages, like IMS, SYSTEM 2000, TOTAL, STAIRS and others, are available. However, logical data base design research is still somewhat ad hoc. In the commercial arena, logical data base design is just beginning to be recognized as a critical phase in the development of advanced information systems.

![](/api/attachments/5YFBUN3C/fulltext/images/aaf628e2eb15c445bac41561532ad91412304a1aabf40611f730b200be109fc7.jpg)

## 2. What is a Logical Data Base Design (LDBD)?

An organization contains many functional groups each of which needs data for its operations, making the total data base very large and complex. The design of a data base is generally bottom up. Designers begin with separate functions, putting the element descriptions into data dictionaries, generating cross-references or matrices in order to aid in developing “the design.” We suggest that there are harmful consequences to such an approach, particularly if the data base is designed to support managerial decisions. There is never one optimal design; there are many, each with its own strengths and weaknesses, flexibilities and complexities.

The goal of logical data base design is the production of a data base structure that satisfies organizational requirements. There are five considerations: first, information must be available; second, the time constraints must be met; third, the data base should be represented in a simple and easily comprehensible format; fourth, it should allow change to satisfy future requirements; and finally, it should be cost effective.

The common format must offer "a user's view" or "external view" of the data base. This external view should present data in a suitable format. The user's view (the external schema in the ANSI/SPARC model of data base management system architecture) is shown in Fig. 1.

A second level defines a global view of the data: this conceptual view is an abstract representation of the corporate data base. The external conceptual mapping defines the correspondence between an external and a conceptual view.

A third level of the architecture is the internal view, which allows tuning for efficient operations. The conceptual-internal mapping defines the correspondence between the conceptual view and the internal view of the data base.

According to Navathe and Scholnick [14], the

![](/api/attachments/5YFBUN3C/fulltext/images/194d7739c8bce1014495e74b68c2cabc53a01b67f5a783d3b5494ce1caae385d.jpg)  
Fig. 1. An Architecture of a Data Base Management System [1].

![](/api/attachments/5YFBUN3C/fulltext/images/7773aac70ab3ad411a2f17aa635a34b18f1d6967d98272b78ff42b0650125946.jpg)  
Fig. 2. Conceptual Framework for a Logical Data Base Design [14].

process of logical data base design comprises requirement analysis, view modeling, view integration, model optimization, and model mapping. These are shown in Fig. 2. Requirement analysis provides the input for all phases. The output consists of data specifications and processing requirements for the system users. View modeling provides the abstract representations that correspond to each user's view. View integration combines several sets of such views to provide the global views, which all provide the same information but in different manners. In model optimization, the designer analyzes the global views and selects the one which is most useful. Finally, in model mapping, the chosen global view is mapped onto the available data base management system software.

## 3. Management Involvement in the LDBD Process

An actual data base is a set of data stored on different devices; it is accessed on demand. The DBMS provides help to the user by shielding access and storage techniques from him. This is partly done by a logical data base which forms an interface to the actual data base.

In a “top-down” approach, the logical data base is designed first. This provides the necessary data structures and the interrelationships among data items. The data may then be collected and stored according to the demands of the DBMS package used. This type of planning tends to force the designers to be systematic. In contrast, in the “bottom-up” approach the data is not collected in an orderly manner. The design is geared toward some specific decisions. Such ad hoc procedures are generally effective on a small scale, where the managers are interested in a few decisions: the design environment is simple and its data base design is easy. However, retrofit later creates problems for large organizations with large and complex data bases.

The first two steps of the logical data base design process need heavy user (here, manager) involvement. In the requirement analysis step, the designer interacts with the managers to find out their needs. This is an interactive process and needs cooperation. At present, it is done ad hoc. However, an attempt has been made recently [3] to structure it. This paper discusses the view modeling step. Design analysis is made during this step, where different logical structures emerge as outputs. (These logical structures are referred to earlier as external views.) As the success of the logical design depends typically on how appropriately and effectively the external views are constructed, a management involvement and cooperation is very essential at this stage also.

## 4. A Management-Oriented View Modeling Approach

In a view modeling step, users may feel more comfortable with techniques that capture the way we speak and communicate verbally. This is because these techniques traditionally require less data management expertise. Chen's Enity-Relationship model [11,12], Smith and Smith's Generalization. Classification and Aggregation model [5,6] and Roussopoulos and Mylopoulos' Semantic Network model [10] are some examples of such techniques. Kerschberg et al. [8] call these techniques surface semantic models.

Although these models are successful in extracting information at the discourse level, they have one common shortcoming. All of them have ignored the management activities of the organization. In this section, we provide an approach which recognizes these managerial activities and their importance.

Any organization can be thought of as an information generating process, where the information is generated for the internal and external activities of the organization. The internal activities include, among others, production, marketing, and finance, whereas the external activities are labor relations, tax reporting, demand analysis and so on. Whatever the activities are, they are the sole reason why the users in an organization need data. So, the design of a logical data base requires an analysis of the user activities.

Following Anthony [13], the user activities in an organization can be classified as: strategic planning, managerial control and operational control. Strategic planning is the process of deciding upon the objectives of the organization, the resources to be used to attain these objectives, and the policies that govern the acquisition, use, and disposition of these resources. Thus, strategic planning is the process of formulating longrange plans and policies that determine the character of an organization. Management control is the process by which managers assure that resources are obtained and used efficiently in the accomplishment of the organizational objectives. And operational control is the process of assuring that tasks are carried out efficiently. This typology hints at the different information needs for different organizational levels. Strategic planning is concerned with setting broad policies and goals for the organization. This activity is vital since predictions about the future are most important. The information needed by the strategic planners is aggregate, and the scope and variety of the information vary extensively. By contrast, the information needs for operational control require detailed description of a well-defined and narrow scope. The information requirements for management control fall in magnitude between those of strategic planning and operational control.

The above classification makes it evident that the users at different levels will have different views. The views at the operational control level will have data with maximum detail; they become less detailed as they move from operational control to strategic planning, making the views hierarchical. An activity at any level may need several different views of data that can be interrelated. Also, activities at different levels can have views that may be interrelated. However, once these hierarchical external views are integrated, the resulting conceptual view is flat (or nonhierarchical). This is shown in Figure 3. The boxes at the external level represent the external views of the data base. It is, however, not necessary to use the three levels all the time. The notation “←→” shows the external-conceptual mapping and the notation “←→” shows the conceptual-internal mapping, while the notation “←··→” or “··→” shows the mappings (relationships) between the hierarchical external views.

Note that Figure 3 is the generalization of the widely accepted ANSI/SPARC data base architecture. The external level of this new architecture has at most three levels. Although the mappings between the views at the external level are shown explicitly in Figure 3, the users never see these mappings once the logical data base has been built.

Using the above architecture of hierarchical external views and a single conceptual view, we propose the following model.

The model is an extended directed graph [7] with five elements $(C, F, V, A, H)$ where

(1) $C \neq \phi$ is a finite set of nodes or concepts,

(2) $F$ is a finite set of arcs or modeling functions,

(3) $V \neq \phi$ is a finite set of views,

(4) $A \neq \phi$ is a finite set of activities, and

(5) $H \neq \phi$ is a finite set of hierarchies.

Let us now explain each element in detail.

Concept. A concept is defined to be an abstraction of something that can be identified by its properties or attributes. For example, an abstract data item SUPPLIER can be conceived by the user as a collection of such properties as supplier identifier, supplier address, supplier service and so on. That is,

![](/api/attachments/5YFBUN3C/fulltext/images/76bca0fd43bf604ba19bf90d9bb431fe59dc218233593160583f849539be10a1.jpg)  
Fig. 3. Data Base Architecture Based on Management Activities.

$$
C _ {i} = \left\{a _ {i, j} \right\}, \quad 1 \leqslant j \leqslant J,
$$

where $C_{i}$ is the ith concept, and $\{a_{i,j}\}$ is the set of attributes needed to define $C_{i}$ .

Modeling Function. The modeling functions are the semantic relationships among concepts either at the same level or at different levels of the organizational hierarchy, and are defined over subsets of $C^{n}$ (an n-ary Cartesian product set of C, where C is the set of all concepts). There are two major types of modeling functions: horizontal and vertical. The horizontal modeling functions act among concepts at the same level, whereas the vertical modeling functions connect concepts that are located at different levels. Because of the interdependence among concepts, each modeling functions is associated with a set of update rules to insert, delete or modify the occurrences (a tuple in the relational model) of the concepts. Eight modeling functions $^{1}$ have been formulated and explored elsewhere [9], alongwith their updating rules [2]. They will not be presented here for the sake of brevity.

View. A view is a logical structure (or a construct) which is used by a user (or a group of users) to model his data needs. That is, a view $V_{k}$ consists of data abstractions or concepts and modeling functions that are needed for a particular user's data needs. So,

$$
V _ {k} = \left\{C _ {k, l} \right\} \cup \left\{f _ {k, l, l ^ {\prime}} \right\}, \quad 1 \leqslant l, l ^ {\prime} \leqslant L, \quad l \neq l ^ {\prime},
$$

where $\{C_{k,l}\}$ is the set of concepts in the kth view, and $\{f_{k,l,l'}\}$ is the set of horizontal modeling functions among the concepts in the kth view. Also, $\{C_{k,l}\} \neq \phi$ for $V_k$ to exist.

For example, a user may identify "purchasing" as a view. The objective of this view is to model the data needs of the user for the purchase process. It may include concepts like ORDER, SUPPLIER, SUPPLY, etc., connected by various horizontal modeling functions.

Activity. An activity is defined as a type of job a user (or a group of users) performs. As explained before, we have three layers of activities. These hierarchical layers will be noted as levels 1, 2 and 3-with level 1 as operational control, level 2 as management control, and level 3 referring to strategic planning. Activities will be identified by the symbol $A_{i,j}$ 's, where $A_{i,j}$ denotes the jth activity of the i th level. The data needs for each activity are modeled by the user views. So,

$$
A _ {i, j} = \left\{V _ {i, j, k} \right\}, \quad 1 \leqslant k \leqslant K,
$$

where $\{V_{i,j,k}\}$ is the set of views present in $A_{ij}$ . Some examples of activities are cited below in the context of a hierarchy.

Hierarchy. A hierarchy is defined as a set of related activities, where each activity is at a different organizational level. Thus a hierarchy can at most have three activities in it, one from each of the three possible levels. For example, the activities “service planning,” “service monitoring,” and “service plan implementation” form a hierarchy with the “service planning” activity at the stratetic planning level, the “service monitoring” activity at the management control level and the “service plan implementation” activity at the operational control level. A hierarchy has the following properties:

(a) $\bigcap_{p=1}^{p} H_p = A$ where $H_p$ is the $p$ th hierarchy and $A$ is the set of all activities of the organization, and

(b) $H_{p} \cap H_{q}$ may not be null. This means two different hierarchies can share some activities.

## 5. Implications of the Hierarchical View to the Management

The concept of the hierarchical view should be extremely useful to managers. Since the external view is hierarchical, the managers can view their data needs exactly the way they want. This will make the data base much more meaningful to the management. Secondly, the hierarchical view notion will force the designer to consider the relationships among different views—both in the same level and between levels. This means, any required update (that is, insertion, deletion or modification) of the data in one view will force updates in the related views. This will be automatic and can be handled by the DBMS itself.

An illustration at this point is helpful. We have chosen the case of the Department of Aging (DoA) to explain this model. The Department is involved in providing social services (e.g., transportation, legal services, and meals-on-wheels) to the elderly people in Pennsylvania. Its responsibilities include, among others, implementing federal and state programs, developing future policies, and maintaining control over the area agencies. An area agency, located at each sector (which may include more than one county), measures the demand of the local elderly population, submits plans to the Department, and administers its social programs.

Clearly, a logical design of this data base will involve large numbers of activities. For the purpose of illustration we have chosen a set of related activities “service planning,” “service monitoring,” and “service plan implementation.” These three activities form a hierarchy $H_{1}$ with “service planning” activity at the strategic planning level, the “service monitoring” activity at the management control level and the “service plan implementation” activity at the operations level.

An analysis of these activities provides the data requirements of the managers. In case of “service planning”, the managers are interested in: (a) the types of complaints the Department receives from the elderly people regarding a service, (b) the need of a new service, (c) the demographic profile of the elderly people in the state, (d) the need to acquire resources, and so on. These needs are abstracted in different views as follows:

Table 1
A list List of Views and Their Component Concepts

<table><tr><td></td><td>View</td><td>Concepts</td></tr><tr><td> $V_{3,1,1}$ </td><td>Complaints</td><td>1. Complaints</td></tr><tr><td> $V_{3,1,2}$ </td><td>Resource acquisition</td><td>1. Clients service demand2. Resource acquire3. Agency Allotment4. Funds5. Payment</td></tr><tr><td> $V_{2,1,1}$ </td><td>Cohort agency comparison</td><td>1. Cohort agency2. Amount of service3. Elderly served</td></tr><tr><td> $V_{2,1,2}$ </td><td>Unit cost of service</td><td>1. Agency2. Cost of service3. Elderly served</td></tr><tr><td> $V_{1,1,1}$ </td><td>Client</td><td>1. Client characteristic</td></tr><tr><td> $V_{1,1,2}$ </td><td>Service</td><td>1. Agency served2. Supply of service3. Clients</td></tr><tr><td> $V_{1,1,3}$ </td><td>Funding budget</td><td>1. Federal funds2. State funds3. Local funds</td></tr></table>

$A_{3,1}$ (service planning) =

{complaints, demand for service, elderly

people, resource acquisition,...}

Similarly, for the other two activities, the following views are important.

$A_{2,1}$ (service monitoring) = {cohort agency comparison, unit cost of service, social statistic for benefit measurement,...}

$A_{1,1}$ (service plan implementation) =

{client, service. subcontractor, funding

budget,...}

For the sake of brevity, we will consider only the following views:

(i) $V_{3,1,1} = \text{complaints, and } V_{3,1,2} = \text{resource acquisition.}$

Table 2  
A partial list of modeling functions between related concepts

<table><tr><td> $C_1$ (“From” concept)</td><td> $C_1'$ (“To” concept)</td><td>Modeling Function</td></tr><tr><td>Complaint</td><td>Amount of service</td><td>Logical VIC</td></tr><tr><td>Cohort Agency</td><td>Amount of service</td><td>Type-I Causal HIC</td></tr><tr><td>Amount of service</td><td>Elderly served</td><td>Type-III Causal HIC</td></tr><tr><td>Agency served</td><td>Supply of service</td><td>Type-I Causal HIC</td></tr><tr><td>Supply of service</td><td>Client characteristics</td><td>Type-III Causal HIC</td></tr><tr><td>Agency served</td><td>Cohort Agency</td><td>Part-whole VMF</td></tr><tr><td>Complaint</td><td>Supply of service</td><td>Logical VIC</td></tr></table>

(ii) $V_{2,1,1} = \text{cohort agency comparison, and } V_{2,1,2} = \text{unit cost of service.}$

(iii) $V_{1,1,1} = \text{client}, V_{1,1,2} = \text{service}, \text{and} V_{1,1,3} = \text{funding budget}.$

Note that the notation $V_{k}$ has been modified to $V_{i,j,k}$ to represent the kth view of the jth activity at the ith level.

These views are further analyzed to obtain concepts and modeling functions. Table 1 lists the concepts needed for the above views. To explain the entries of the table, let us take the “resource acquisition” view as an example. The objective of this view is to obtain information needed to plan for different resource allocations. This objective can be met by answering questions such as: (i) What is the demand for a service?; (ii) How much resource does the Department presently have for this service?; (iii) What are the allotments of this resource?; (iv) How is the Department going to pay for the new acquisition? These questions are abstracted as concepts and are shown in Table 1 with the “resource acquisition” view. All other concepts in this table are collected are abstracted the same way. The modeling functions between related concepts are also derived. $^{2}$ A partial list of these functions is provided in Table 2. The concepts are then connected by the modeling functions to obtain a network. Figure 4 shows such a network for $V_{3,1,1}$ , $V_{2,1,1}$ and $V_{1,1,2}$ views.

![](/api/attachments/5YFBUN3C/fulltext/images/b06a894d9ed486b07c791b10c282c94cfa265f68e8b6ed975a7e25cc5bdb3782.jpg)  
Fig. 4. A Data Base Architecture for the Example.

Note that concepts such as “cohort agency,” and “agency served” are related by a common denominator, “agency.” But “agency” appears differently at each level. At the operational control level, it is described in more detail; at the management control level, the concept “cohort agency” is less detailed. Also, since “cohort agency” provides services, the “cohort agency” and “amount of service" concepts are related. Any update in "cohort agency" may require updates in "amount of service." But as each modeling function has its separate set of update rules, any update in a concept that is triggered by an update in a related concept can now be automatically handled by the DBMS.

## 6. Conclusions

This paper is concerned with the development of a new type of data base architecture that depends upon management activities. The logical data base so designed supports a large number of decisions of the organization [2]. Moreover, the data base is presented in such a way that the users do not get unnecessary details of the data. The approach is more suitable for larger data bases, which are slowly becoming a way of life as organizations and their data needs grow steadily.

This idea has been successfully utilized to develop a data base for the Department of Aging in Pennsylvania. A detailed description of that study can be found in [2].

## Acknowledgement

The author would like to acknowledge the help received from Dr. P. De of the College of Administrative Science, Ohio State University, during the revision process of this manuscript.

## References

[1] ANSI/SPARC, Study group on Data Base Management System Report, FDT Bullet n of ACM SIGMOD 7, No. 21, 1975.

[2] A. Sen, On the Theory of Logical Data Base Design for a Decision Support System, Ph.D. Thesis, Pennsylvania State University, 1979.

[3] A. Sen and P. De, "A Formal Procedure for Requirement Analysis in Data Base Design," Proceedings of the XIV Annual Hawaii International Conference on Systems Sciences, Honolulu, January 8-9, 1981.

[4] C. Mohan, "An Overview of Recent Data Base Research," DATA BASE, Vol. 10, No. 2, Fall 1978.

[5] J.M. Smith and D.C.P. Smith, "Database Abstractions: Aggregation and Generalization," ACM Transactions on Database Systems, Vol. 2, No. 2, pp. 105-133, June 1977.

[6] J.M. Smith and D.C.P. Smith, "Database Abstractions: Aggregation," Communications of the ACM, Vol. 20, No. 6, pp. 405-413, June 1977.

[7] Jurgen M. Janas and C.B. Schwind, "Extensional Semantic Networks: Their Representation, Application and Generation," in Associative Networks: Representation and Use of Knowledge by Computers, N.V. Findler (ed.), Academic Press, New York, 1979.

[8] L.A. Kerschberg, A. Klag and D. Tsichritzis, "A Taxonomy of Data Models," Tech. Report CSRG-70, Computer Science Research Group, University of Toronto, May 1976.

[9] P. De, A. Sen, and E. Gudes, "An Extended Entity Relationship Model with Milti-Level External View," Proceedings of the 2nd International Conference on the Entity-Relationship Approach, pp. 459–476, October 12–14, 1981.

[10] N. Roussopoulos and H. Mylopoulos, "Using Semantic Networks for Data Base Management," Proceedings of the V.L.D.B. Conference, Boston, September 1975.

[11] P.P.S. Chen, "The Entity-Relationship Model - Toward a Unified View of Data," ACM Transactions on Database Systems, Vol. 1, No. 1, pp. 9–36, March 1976.

[12] P.P.S. Chen, "Applications of the Entity-Relationship Model," Proceedings of the New York Symposium on Data Base Design, New York, pp. 25–33, May 17–18, 1978.

[13] R.N. Anthony, Planning and Control Systems: A Framework for Analysis, Boston: Harvard University, Graduate School of Business Administration, 1965.

[14] S.B. Navathe and M. Schkolnick, "View Representation in Logical Data base Design," ACM SIGMOD, June 1978, pp. 144-156.
