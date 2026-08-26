---
otero_id: 16986
otero_key: "EHY5AN79"
title: "The use of expert system technology in DSS"
authors: "A.J.M. Beulens; J.A.E.E. Van Nunen"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90005-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Use of Expert System Technology in DSS

A.J.M. BEULENS and J.A.E.E. Van NUNEN
Rotterdam School of Management, Erasmus University Rotterdam, 3000 DR Rotterdam, The Netherlands

In this paper we discuss the challenges that are eminent for the implementation of Decision Support Systems (DSS) in decision making processes. Based on the experience with some DSS which we developed in the past and which are still used in practice we evaluate the possibilities of using expert systems technology to meet some of the shortcomings of DSS of a previous generation. We will give a description of the different classes of information systems and make comparisons in order to show differences and consequences for systems development methodologies. In addition, we will describe some specific examples in order to elucidate our point of view with respect to the challenging future of DSS and expert systems which are emerging.

![](/api/attachments/EHY5AN79/fulltext/images/69f8976d16f6bc16f005ca4ce7aad22bdf6af0111c22b86b7b4717bfbe3be3ee.jpg)  
companies and organizations.

Adrie J.M. Beulens is currently Dean of the Faculty of Informatics of the Haagse Hogeschool, The Hague, The Netherlands. His current research interest lies in the area of Decision Support Systems, Management Information Systems and Quantitative Methods. Prior to joining the faculty of Informatics, he taught at the Rotterdam School of Management, and worked as Senior Project Manager in the area of Information Systems. He has been an IS-consultant to various situations.

![](/api/attachments/EHY5AN79/fulltext/images/ac97e9e9112a5f9a7aa2817110fe83bc1b805bce482f93f2194c9d51de1295c8.jpg)

Jo A.E.E. van Nunen (42) graduated cum laude in Mathematics at Technical University in Eindhoven, The Netherlands. He has his PhD from the same University in 1976. The subject of this thesis was 'Contracting Markov Decision Processes'. From 1976 till 1984 he was working at the Graduate School of Management in Delft. In 1978 he was Visiting Professor at the North Carolina State University in Raleigh, N.C. Since 1984 he is Professor of Quantitative Methods and Information Sciences at the Rotterdam School of Management of the Erasmus University in Rotterdam. He is author of two books and many articles in professional journals on Operations Research and Information Sciences. He has been active in building Decisions Support Systems for different types of applications, ranging from support systems for distributions, inventory control, maintenance, production to manpower support systems. Many of these systems were developed in close cooperation with Governmental Organizations and Industry.

## 1. Introduction

Survey papers on Decision Support Systems in general give an overall overview on what has been established in the past. In this paper we will use a different approach. First, we will give an idea about the field of Decision Support Systems and the place of DSS within the class of Information Systems. We will focus on the differences with classical Information Systems, like transaction processing or operational information systems (OIS), operation research applications (MS/OR), management information and database systems (MIS) and expert systems (ES). It will be clear that the specific requirements of DSS also influence the way in which development methodologies should be realized. The approach that is followed for creating a theory on development methodologies for DSS is a bottom up approach. Based on a number of real life applications of DSS the process of realization of the system is analyzed. In this paper we reconsider some existing DSS and give some directions that show how expert system technology can be used to improve the quality of DSS. Such systems are now available for specific applications. Recent research shows that the demand for such systems is enormous. In addition, the new technological developments open various challenging opportunities. Section 2 is concerned with the classification of types of Information Systems. Section 3 describes problems with and opportunities in DSS building; section 4 indicates the possible use of ES technology in DSS followed by concluding remarks in section 5.

## 2. Definitions and Descriptions of Types of IS

In this section the class of information systems (IS) is divided into types of information systems such as OIS, MIS, MS/OR, DSS and ES. IS are systems that are meant to provide information to managers to manage and control purposeful activities of an organization. Anthony [2] distinguishes three types of management tasks; strategic planning, management- and operational control. For each type of task the functional and performance requirements of IS that support these tasks are different. Operational information systems conduct transaction processes, they keep track of, and transmit messages about, important activities, events and states of the object system (OS) of interest. They are mainly used on the operational level. MIS, mainly used on the management control level, is concerned with analysis of and reports about the states and events in the OS to support planning and control, based on operational information. MS/OR systems primarily address the analysis and solution of well structured problems on the operational or management control level using mathematical models of the object system of interest. DSS are systems that provide support for solving semi- and unstructured problems that managers are confronted with. They have to be used integrated in the decision making process and incorporate data and models of the OS. They are primarily meant to be used on the management control and strategic planning level. ES are systems that support users, at any level in an organization, to perform a task that requires the knowledge of the problem domain of an expert. It solves a problem instance using knowledge rules and facts about the OS via inference capabilities.

The global framework of IS presented here indicates that categories of information systems may be based on:

\- The management level for which it is primarily used.

\- The structure of the tasks to be performed by the managers.

\- The technologies applied in these systems.

As a consequence the categories are overlapping. In the remainder of this paragraph of the paper we will deal in more detail with some characteristics of types of information systems, and some problems currently associated with building, using and maintaining them.

## 2.1. Operational Information Systems

Operational Information Systems (OIS) are primarily concerned with the timely and accurate registration of an operational object system, which provides and transmits information about important events, activities and states of the operational process. Important properties ar characteristics of these systems are

\- they support operational control activities,

\- they register transactions, provide for standard reports, messages and inquiries,

\- they deal with the history and current state and event in the OS,

\- they support decision procedures that are well structured,

\- they operate in a stable environment with respect to the organization and procedures,

\- they have evolved from classical EDP applications.

Problems associated with building, using and maintaining such systems are extensively dealt with in literature about information systems management, developing information systems and information resource management. We may e.g. refer to Alloway [1], Davis and Olson [7], Thierauf [16]. Sprague and McNurlin [15]. Some current problems with OIS are

\- they often do not sufficiently satisfy basic functional and performance requirements,

\- they are not dynamically robust,

\- they often do not properly interface with other types of IS,

\- they are frequently not based on current DB, Teleprocessing, and computer technology,

\- they are frequently not developed and maintained effectively and efficiently,

currently many OIS are not yet based on integrated corporate data bases and modern technology.

## 2.2. Management Information Systems

MIS are primarily concerned with recording information about the OS of interest and with providing information to managers on the management control level. Important properties and characteristics of these systems are:

\- they support management control activities,

\- they aggregate summarized historic data derived from large operational internal and external databases. E.g. sales figures per month are derived from sales-order files contained in the operational sales information system,

\- they provide data on planned and actual performance, analyze variances and suggest courses of action. E.g. standard sales reports compared with planned sales,

\- that operating procedures are not frequently subject to change. In general there is a class of standard operating procedures to be performed at regular intervals and adhoc queries,

\- they contain models for statistical analysis and reporting that are well structured and understood. E.g. statistical sales-analysis per product per region etc.,

\- they have developed over time in response to changing user requirements and technology.

The problems associated with OIS, mentioned in the previous section also hold to a large extent for MIS. Additional problems associated with MIS that need to be mentioned are:

\- poor interfaces with internal and external databases. This may be caused by technical problems or different types of data models,

\- frequently there are limited capabilities for ad hoc-queries. Often these capabilities are only accessible for expert users,

\- poor flexibility. It is in practice difficult to rapidly adapt a MIS with respect to changing management requirements. This may be caused by a variety of technical reasons, for example insufficient maintenance capacity might be a reason.

## 2.3. MS / OR Systems

Management Science or Operational Research systems exist for many decades. They are, mostly built by MS/OR departments, used to solve structured problems that managers are faced with. Important properties and characteristics of these systems are:

\- they support well structured decision making problems,

\- they are based on a set of models describing (part) of the OS of interest. They enable the generation and evaluation of a set of decision alternatives to find an optimal or feasible solution, based mainly on quantitative criteria. E.g. an MS/OR System may be used in an inventory control system to decide upon replenishment orders for certain articles if a minimum stock level of an article is reached,

\- they are meant to replace to some extent decision makers,

\- they are part of, or integrated with OIS or MIS. E.g. stock movements and registration in the order- and inventory processing system,

\- etc.

Problems associated with these kind of systems have been well phrased by Geoffrion [9]. The problems mentioned refer to e.g.

\- poor managerial acceptance,

\- poor development productivity,

\- poor usage of new technologies. This includes: user friendly system interfaces, representation capabilities, interfaces with OIS and MIS, etc., - etc.

## 2.4. Decision Support Systems

DSS are systems that enable managers, to use data and models related to an OS of interest, to solve semi- and unstructured problems they are faced with. Important properties and characteristics of these systems are:

\- they support decision making in dynamic environments,

\- they are used to solve semi- and unstructured problems on different management levels. Mainly on the strategic planning level. E.g. evaluation of personnel policies, investment decisions etc.,

\- they focus on effective support rather than automatic decision making or control,

\- they are meant to support decision processes in which qualitative as well as quantitative aspects play an important role,

\- they are meant to support one or more phases of a decision making process. The required information is provided by (mathematical) models and data that describe the OS of interest in order to help identify problems, or to generate, evaluate, and compare decision alternatives,

\- they are mainly future oriented. In DSS we use historical data and models to generate and evaluate forecasts and decision alternatives,

\- they may need to be concerned with the comparison of decision alternatives based on data stored in scenario databases,

\- they must be used integrated in the decision making process. The implementation of DSS heavily affects the organization of decision making processes,

\- they must be user friendly and user controlled. This is important in case of frequent and infrequent or fragmented usage. In many cases there are no standard operating procedures for these types of systems,

\- they must be flexible and adaptable to changes in the decision making process.

The functional and performance requirements just specified lead to characteristics with respect to the technical-architecture and functions of DSS. Some of these are:

\- DSS systems have an architecture comprising database components such as master-, scenario-, and model databases, software components comprising a database management system (DBMS) capable of handling the databases, a model base management system (MBMS) to handle the model base, a process control and management system (PCMS) and a user system interface. This architecture is depicted in fig. 1. For a more elaborate description we refer to Beulens [5],

\- DSS need a large array of data management and representation functions for the different databases as well as the model base,

\- they need a large array of user functions to be able to generate/evaluate the decision scenarios,

\- they are dependent on multiple internal and external data sources provided by OIS and MIS and scenario databases for the storage of decision alternatives,

![](/api/attachments/EHY5AN79/fulltext/images/bc0123af4fdb6ac34b7337ce16a11c8d0f6fda645f85880c6d66ac9d24aadfa7.jpg)  
Fig. 1. A conceptual model of a DSS.

\- DSS must be based on a DSS generator or a set of DSS-tools that allow for building and maintaining adaptable DSS.

If we compare MS/OR and DSS we find a number of similarities and differences that relate to model building and model usage in these systems. Important differences are that in DSS

\- we require a class of models rather than just one. This is due to the fact that we assume that in a semi-structured situation only part of the problem can be captured by a model and that alternative ones can be used,

\- decision alternatives must be judged by several quantitative and qualitative criteria. One looks for satisfactory not ‘optimal’ solutions,

\- one has to be able to evaluate the consequences of ‘own’ alternatives and ‘what-if’ questions,

\- one needs ‘goal-seeking’, e.g. decision alternatives have to be found that satisfy certain criteria,

\- the evaluation of decision scenarios requires the comparison of them,

\- one needs ample capabilities for sensitivity analysis with respect to parameters as well as models,

\- we require more efficient solution procedures to be able to generate necessary decision alternatives and to perform sensitivity analysis,

\- the user-system interface should enable model-and report generation,

\- model building is more difficult for semi- and unstructured problems and requires a lot of expertise,

\- one has to be able to support hierarchical related decisions.

The problems currently associated with building and using DSS are partly similar to the ones mentioned in the previous section for MS/OR and MIS. Problems of specific importance to DSS that need to be mentioned are

\- insufficient access capabilities to external databases from IS external to the DSS. This may be due to technical problems such as unknown data models, data models of different types or bad interfacing capabilities. It may also be caused by badly designed data models of these systems where information needs for systems to be interfaced with have not been taken into account,

\- DSS generators are still restricted to specific classes of models, e.g. financial planning models. In many cases DSS tools must be built and used to be able to capture certain types of models in DSS.

The increased complexity associated with building, using and maintaining these adaptable systems even aggravate these problems. However, new technological developments like 4th generation languages, model generators, simulation languages etc. open new perspectives.

## 2.5. Expert Systems

ES are systems that support users by performing a task that requires expert knowledge and facts about a problem domain. Important properties of ES are:

\- they aim to support a user to solve a particular problem instance. A user consults an ES e.g. for a diagnosis. An ES guides the user through the consultation process and is therefore system controlled. It is now widely accepted that not all relevant knowledged about the OS can be captured by an ES. Thus it can only act as an intelligent assistant,

\- they use expert knowledge in the knowledge base, facts and rules about the problem domain,

\- they are based on heuristics rather than mathematical models. Decision making procedures included in ES are often modelled after the cognition processes by which decision makers arrive at their decision.

\- they contain an inference engine that, once invoked via the user system interface, solves the question asked via logical analysis,

\- they contain a knowledge base of a limited problem domain. This contains knowledge about both the decision making process of expert users and about the OS of interest,

\- they are built using expert system shells or tools,

\- they focus on problem solving just as DSS do,

\- they are capable of explaining how a particular problem has been solved,

\- that some of them are very user-friendly due to the fact that they are system controlled and due to the sophisticated user-system interface. For example with (limited) natural language capabilities (Intellect e.g. [16]).

Part of these properties, if included in DSS, could improve the richness of the functionality of DSS and make them more user friendly on one hand and improve the functionality on the other hand.

At the moment there are several Expert Systems or Knowledge Based Systems used in practice. Very often they are developed for applications where it is relatively simple to capture the knowledge of the experts. Nowadays there are realizations where optimizing procedures are included in Expert Systems. However these possibilities are not yet offered in commercially available expert systems shells.

Practical applications of ES and problems currently associated with building and using ES are e.g. reported in publications of Silverman [14], Harmon and King [10], and Harmon, Maus and Morrissey [11]. Important to mention here is

\- the difficulty of knowledge engineering.

\- the performance of expert systems. Currently, for a reasonable performance, ES need a lot of computer resources,

\- the limited scope of expert systems,

\- the restricted ability to interface ES with data banks from other applications such as OIS and MIS,

\- the limited availability of ES-tools and shells on general purpose-computers.

## 3. Problems and Opportunities Facing DSS Builders

In the previous section we have dealt with problems associated with building, implementing, using and maintaining different types of IS. In this section we will deal with some problems that we have experienced with building and implementing practical MIS and DSS. We start however with important challenges and opportunities facing the DSS community. See e.g. Alloway [1]. First of all the circumstances in many organizations are now more favorable to develop and implement effective DSS. This may be reflected by

\- a growing management interest in and need for DSS next to MIS,

\- better and more mature OIS and MIS have been developed and implemented that provide for databases containing data to be used in DSS.

Secondly, there have been tremendously important technological developments. Some examples which facilitate the development of DSS are

\- the availability of computer networks with possibilities for distributed processing and distributed databases,

\- improved capabilities and speed of (desk-top) computers that allow for the development of applications previously impossible,

\- the availability of low-priced powerful micro-computers and workstations,

\- the improvement of fourth generation languages and DSS tools and generators,

\- available ES-technology with interfaces to current technology.

Moreover, there are developments with respect to DSS and modeling development. Some examples are

\- the growing theoretical knowledge with respect to methods for designing, building and maintaining DSS and the incorporated models,

\- software support-tools for designing systems and models.

In the past we have been involved in the development and implementation of several practical DSS. For example we developed DSS for location-allocation problems, production planning, financial planning, personnel planning, forecasting and an Economic Advisory System. These systems are being used and adapted in response to changing user requirements and changing problems. For two of these systems we will briefly describe the developments over time. After that we will give some problems encountered during the development, implementation and use of these systems.

The first group of DSS, that we have built, are concerned with a variety of location-allocation problems (see [5], [6] and [12]). This problem is depicted in fig. 2. We assume that there are a number of factories with production lines (L) that produce products (P), to be stored in a number of warehouses (W) and to be distributed to a number of buyers (B). Products are produced on the lines and thereafter directly transported from the factories to warehouses. The buyers must be supplied for all products by the same warehouse. We assume that we know

\- the demand per product per buyer,

\- the production and handling costs,

\- the available capacities,

\- the efficiency differences between depots,

\- the efficiency differences between factories,

\- the distribution costs per ton product. These costs may depend on the product, on the type of transport and on the distance(class).

A simplified formulation of this distribution problem as a mixed-integer LP-problem is: Which warehouses out of a possible set of them should be used. How should the available buyers be allocated to these warehouses, such that, within capacity constraints, the distribution and production costs are minimal. From a managerial point of view this information is far too restrictive.

The first DSS developed, the location-allocation DSS, that incorporates the LP-model previously mentioned, is being used by a brewery and an oil company to generate and evaluate different distribution scenarios. The extended location-allocation DSS, the ELA-DSS, which was derived from the previous one, is concerned with distribution structures in which the production is split up into phases and where there are interfactory shipments of unfinished products. The ELA-DSS is based on a revised mixed-integer-linear programming model. The DSS enables the user to generate a variety of distribution scenarios and to evaluate a variety of management questions related to them.

The third DSS is called the Location Allocation Routing DSS (LAR-DSS). It addresses another set of location-allocation problems where especially the feasibility of routing and service level constraints is to be evaluated for distribution structures. The LAR-DSS comprises a heuristic in which a vehicle routing package is incorporated. It enables users, currently consultants, to generate

Factories / lines (1)

Warehouses (w)

Buyers (b)

![](/api/attachments/EHY5AN79/fulltext/images/668f531b3cc6c07c5a7c21f0ddc0072615f3f385a38ae4259a61c3fe3bfe7910.jpg)  
Fig. 2. Simplified distribution network.

distribution scenarios and evaluate possible consequences of these. See [5], [6] and [12] for more elaborate descriptions.

Also in the area of personnel planning we have been involved in the development and implementation in different organizations of a DSS named FORMASY which stand for FOrecasting and Recruitment in MAnpower SYstems for personnel planning. A simplified personnel planning problem can be described as follows. We assume that there are a number of personnel categories and a number of time periods. Further, we assume that we know

\- the initial staff per category,

\- the required staff per category at a certain time period. Both quantitatively and qualitatively,

\- recruitment policies and constraints,

\- estimates of the percentage of the people that leave the company per year,

\- retirement schemes,

\- education schemes,

\- etc.

The personnel planning problems is now to determine personnel plans which include recruitment, retirement, promotions, education etc., which ensure that the required staff levels will be available in time with the right qualifications. The Formasy DSS, based on Markov and Cohort Models, has developed over time, and is used in a variety of companies to generate and evaluate the consequences of personnel plans. For a description of the DSS we refer to [13].

Our experiences with these systems, which are frequently used, show they can be improved with respect to:

1 The functionality and the user system interface. They do not completely satisfy functional- and performance requirements. There are difficulties in using the system, especially for non-experienced users.

2 The flexibility in a dynamic environment. The development productivity for our DSS appeared to be too low. Some possible causes for this are

\- the number of (data) model representations being used by modelers, users and software. This may cause communication and interface problems. For DSS in which Linear Programming (LP) models are used we have described this problem and solution in detail in Beulens [5],

\- the limitation of modeling software to one type of models, e.g. only LP- or financial models,

\- the lack of system support during all phases of designing, building and implementing components of DSS, including the models incorporated in it. This means that there are not sufficient modelling capabilities in the MBMS,

\- software tools which currently have inadequate capabilities for a.o. interfaces.

We have also experienced that DSS may be hard to implement in some organizations. This may be attributed to the problems previously mentioned. We have experienced differences with implementing and using the same DSS in different organizations or even in different departments/divisions of an organization.

In our research in the area of DSS we have addressed the opportunities and problems previously mentioned in a number of ways. Some research topics are

\- the generation of a generalized structure for our LP based DSS, as depicted in fig. 1, and the development of a DSS generator for these applications,

\- how to use ES technology to improve the functionality of our DSS as well as to make them more user friendly.

In the remained of this paper we will pay attention to the applicability of ES technology in DSS.

## 4. Possible Use of ES-Technology in DSS

In the previous sections we have discussed that there are ample problems and opportunities facing the DSS community. From the characteristics and properties connected with current types of IS we may derive that the use of different technologies may lead to complementary capabilities that, if incorporated in one system, may lead to DSS that are more user friendly, provide better functionality and can be used more efficiently and effectively. If we talk about ES-technology we refer to the principles, methods, knowledge representation and software tools employed in current ES. (See e.g. [10], [11]). In the remainder of this section we will deal with some examples of the use of ES technology in DSS for improving user-system interfaces, and for improving the functionality of components of specific DSS or a DSS generator.

## 4.1. Improving the User System Interface and Scenario Integrity

Many users of DSS have experienced that it may be rather difficult to learn how to use a system properly and effectively. We have found that there are a number of possible reasons that cause the complexity of system usage. Some of these are

\- the procedures to be used in the system have too little in common with procedures or systems that users are familiar with,

\- it is difficult to know the interdependencies of the functions provided by the system,

\- it is difficult to keep track of the consequences of function usage with respect to one decision scenario, for example on the integrity of the database; this is certainly valid in case of fragmented use over time,

\- there are applications that require extensive knowledge of a specific problem domain or technical knowledge. Examples can be found in the area of linear programming or forecasting models (see e.g. Van Dissel [8]),

\- users have to deal with several databases and models, each with different data models and resulting translation problems,

\- users may have to work on more decision scenarios at the same time. As a consequence they have to keep track of what they have done for each of them.

In some of our DSS we have encountered these problems and solved part of them by the functions provided by the PCMS as depicted in fig. 1. The PCMS controls the access of a user to the functions of the other components of the DSS. Together with the user system interface it determines a.o. whether the system is user friendly or not. We feel that the use of expert systems technology in the PCMS will make our DSS more efficient and user friendly. In a prototype system for financial planning we have tested this idea as follows. In the model base we have one or more process models. A process model describes on the user level the system functions and the relationships between them. System functions that need to be performed by the user and/or the machine to generate a correct scenario data base. For a correct and successful generation of a decision scenario a user is required to select one process model after which the functions described in it may be invoked and used. This must be done in an allowed sequence and each function must be executed correctly by both user and machine. In our test DSS we have built the PCMS using expert system technology, a knowledge base containing information about the process models and a meta-db in which data about the scenarios in process are stored. The system thus keeps track of the status of each scenario and of the integrity of the scenario database with respect to the process models (model or scenario data base integrity).

The results obtained with the system clearly indicate that the approach is technically feasible. Moreover, each of the possible causes of the complexity mentioned above is being addressed. The system has improved help facilities; it clarifies to the user for example the status of a current decision scenario, what has been done, what may be done, what the consequences of certain user actions/functions on the integrity of the scenario data base are etc.

## 4.2. The Use of Expert System Technology in our Location-Allocation DSS

In our location-allocation DSS applications we are investigating the applicability of ES-technology in order to make these DSS more effective, efficient and user friendly. At present we are in the process to establish a new development environment for DSS and to redesign and rebuild part of our location-allocation DSS [12] in which ES-technology will be used.

In the new version of this system we have planned to incorporate ES-technology for

\- improving the functionality of the PCMS as described in section 4.1. It will make the system more user friendly and maintain the integrity of scenario databases with respect to their process model and data model,

\- certain database validation functions. These functions will be invoked and evaluated by the PCMS before elaborate numerical analysis by an LP-package are performed. E.g. there is an extensive set of input variables of which the completeness and correctness can be checked. This must be done for capacities for warehouses and production lines, indices for transportation-, production- and handling costs, growth indices for different products, etc. Knowledge-rules can be used to represent these integrity constraints in a knowledge base,

\- improving the comparison of alternative decision scenarios by also incorporating qualitative arguments (in a meta-knowledge base),

\- a heuristic for the determination of a feasible integer solution for the location-allocation problem. Currently a feasible integer solution to the location-allocation problem is obtained starting from an LP-solution of an LP-relaxation of that problem. If the LP-solution is not an all-integer solution for the assignment of buyers to warehouses, which may happen for a limited number of buyers as described in [4], a simple heuristic is used to assign each buyer to just one warehouse. This procedure however may not lead to a feasible integer solution. Expert users evaluate these solutions by looking a.o. at what constraints are violated and to what degree. Based on this analysis constraints are relaxed and/or assignments are changed such that practically feasible integer solutions are found. Also for this problem we have planned an ES-subsystem that contains the knowledge of an expert with respect to the procedures to obtain a practically feasible integer solution. The knowledge incorporated contains a number of rules with respect to the possibility to relax certain types of constraints, relative priorities between constraints, priorities of assignment, etc. The ES-subsystem will help non-expert users to efficiently derive the necessary solutions,

\- improving the trial and error search procedures for better satisfying solutions. The process of obtaining feasible and satisfying distribution scenarios is often an iterating process in which via trial and error new scenarios are generated until a satisfying one is obtained. An expert-user compares the results of a certain decision scenario with preset objectives and analyses the reasons for the differences. For the location-allocation model these differences may a.o. be caused by capacity limitations of lines and warehouses, cost-figures and allocations etc.

Based on this analysis an expert user derives a new decision scenario in which the set of decisions, regarding possible factories and lines, associated capacities and production-, storage-, handling- and transport costs are changed compared to previous scenarios. By incorporating this expert knowledge into the ES subsystem we may help users of the DSS to suggest changes to scenarios such that they can find a satisfying solution as fast as possible. An ES-subsystem as just described may reduce the knowledge base of a user that is required to be able to effectively use the DSS,

\- obtaining automatic translations of algebraic data models into relational data models when incorporating new models into the model base (see also Beulens [5]).

## 4.3. The Use of ES-Technology in Other Applications / Components of DSS

In other DSS applications we have experienced problems more or less similar to the ones dealt with in previous sections. For some of these applications we have planned or are in the process to incorporate ES-technology in order to improve their functionality and user friendliness and to reduce the knowledge base of the user. Some research in progress encompasses the use of ES-technology in

\- a DSS for personnel planning, where based on experience with derived personnel plans, users get advise on how to find alternative plans that better satisfy preset staffing objectives. This includes e.g. feasible recruitment and promotion policies. For this DSS it also holds that users need a lot of expertise to be able to find good personnel plans efficiently. The solution to this problem is analogous to the procedure described for finding satisfying solutions for the location-allocation problems. New scenarios comprise decisions about the recruitment per category per time period, retirement schemes and promotion schemes. The knowledge of an expert user with respect to finding alternative plans based on derived plans and preset objective is captured in an ES-subsystem. This ES-subsystem can then be used to help non-expert users to find good personnel plans efficiently.

\- a DSS for Box-Jenkins time series analysis and forecasting. It is well known that a user who wants to make use of the Box-Jenkins technique needs a lot of statistical and technical knowledge of the Box-Jenkins method, technical knowledge of the software package and knowledge of the application domain. Part of the time series analysis and evaluation of time series models is performed by an Expert System. This encompasses regeneration of possible time series models, the estimation of parameters and the evaluation of them, followed by the selection and presentation of the best of them based on best fit. This decreases the technical knowledge of time series models required from the user substantially. Further, it is also planned to enhance the user system interface with ES capabilities as previously explained to make it more user friendly.

\- etc.

## 5. Concluding Remarks

In the previous sections we have dealt with a number of problems, opportunities and challenges facing the DSS, MS/OR and ES community. A lot of research, both theoretical and practical, is necessary in order to help us find solutions for these problems and to help us meet the challenge to provide good DSS for our users. The increasing maturity of information systems in organizations and the rapid technological developments offer the possibilities to do so. We do our research by building concrete practical DSS. DSS in which we make use of our experiences and the tools/techniques and methods previously developed. Ultimately these experiences should help us to contribute to formulate a theory on the design, development and implementation of DSS in which ES technology plays an important role.

## References

[1] Alloway, R.M. and J.A. Quillard, User Managers' Systems Needs, MIS Quarterly 7:2, June 83, pp 27–41.

[2] Anthony, R.N. Planning and Control Systems: A Framework for Analysis, Harvard University Press, 1965.

[3] Ariav, G., Clifford, J., eds, New Directions for Database Systems, Ablex, 1986.

[4] Benders, J.F., and Nunen, J.A.E.E. van, A. Property of Assignment Type Mixed Inter Linear Programming Problems, OR-letters pp. 47–52, 1983.

[5] Beulens, A.J.M., Transforming Algebraic Data Structures into Relational Data Structures in DSS. In conference report: Multi-attribute Decision Making via OR based Expert Systems. Eds. R.L. Keeney, R.H. Mohring, H. Otway, F.J. Radermacher, M.M. Richter, Universitat Passau, 1986.

[6] Beulens, A.J.M., Kolen, A.W.J., Niekamp, E.G., A Decision Support System for a Location-Allocation-Routing Problem, Working Paper Rotterdam School of Management, September 1987.

[7] Davis, G.B., and M.H. Olson, Management Information Systems: Conceptual Foundations, Structure, and Development, 1985.

[8] Dissel, H.G., Beulens, A.J.M., and Gels, M.C., The DSS approach for the Design and Use of a Box & Jenkins Time-series Analysis and forecasting System (in Dutch). Informatie, year 20, nr. 6, 1984.

[9] Geoffrion, A.M., An Introduction to Structured Modelling, working paper 338, Western Management Science Institute, UCLA, June 1986.

[10] Harmon, P., King, D., Expert Systems, Artificial Intelligence in Business, Wiley 1985.

[11] Harmon, P., Maus, R., Morrissey, W., Expert Systems: Tools & Applications, Wiley, 1988.

[12] Nunen, J. van, Benders, J.F., Decision Support for Location and Allocation Problems within a Brewery, Operations Research Proceedings 1981, Springer Verlag Berlin, 1982.

[13] Nunen, J. van, Wessels, J., A Decision Support System for Personnel Planning. In: Quantitative Methods in Management, Edited by C.B. Tilanus, O.B. de Gans, J.K. Lenstra.

[14] Silverman, B.G., Editor, Expert Systems for Business, Addison Wesley, 1987.

[15] Sprague, R.H., McNurlin, B.C., Information systems Management in Practice, Prentice Hall, 1986.

[16] Thierauf, R.J., Effective Management Information Systems, Merril, 1987.
