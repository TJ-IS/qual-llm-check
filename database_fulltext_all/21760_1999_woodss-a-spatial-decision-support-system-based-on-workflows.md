---
otero_id: 21760
otero_key: "ED728FNT"
title: "woodss — a spatial decision support system based on workflows"
authors: "Laura A Seffino; Claudia Bauzer Medeiros; Jansle V Rocha; Bei Yi"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00039-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# WOODSS — a spatial decision support system based on workflows

Laura A. Seffino <sup>1</sup>, Claudia Bauzer Medeiros <sup>)</sup>, Jansle V. Rocha <sup>2</sup>, Bei Yi <sup>3</sup>

IC and FEAGRI-UNICAMP-CP 6176, 13081-970 Campinas, SP, Brazil

## Abstract

Environmental planning takes advantage of geographic information systems GIS to manage geographic data. GIS are, Ž . however, tools which require a great deal of training and programming expertise and, furthermore, have little support for decision makers during their planning activities. This paper presents WOrkflOw-based spatial Decision Support System Ž . WOODSS — a software developed at the University of Campinas, Brazil, to be used in conjunction with a GIS in order to provide spatial decision support involving environmental data. WOODSS was implemented on top of a commercial GIS and tested in the context of agri-environmental planning activities. WOODSS is centered on dynamically capturing user interactions with a GIS in real time and documenting them by means of scientific workflows. It keeps track of decision procedures, models applied and the choice of parameters in running these models. WOODSS’s workflows can be updated on the fly, allowing testing and comparison of alternative planning strategies. They can, furthermore, be used as building blocks for the construction of complex decision procedures, supporting a divide-and-conquer problem solution style. These workflows interact directly with the GIS, sparing environmental planners and decision makers the burden of low-level programming. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Geographic information systems; Scientific workflows; Spatial decision support systems; Environmental planning

## 1. Introduction

Spatial decision support systems Ž . SDSS are decision support systems where the spatial properties of the data to be analyzed play a major role in decision making. Usually, these properties refer to the data’s location on the Earth’s surface — the so-called georeferenced data. The term refers to data about geographic phenomena associated with its location, spatially referenced to the Earth 6 .<sup>w</sup> <sup>x</sup>

Spatial decision support is one of the facilities that must be offered by environmental management information systems EMIS 18 . These are systemsŽ . <sup>w</sup> <sup>x</sup> which are conceived to help users administer environmental information within an enterprise. One of the most important activities that must be supported by EMIS is enÕironmental planning. This term encompasses a large set of planning and policy enforcement activities that have to deal with two Ž . sometimes conflicting objectives: exploitation of existing resources, to maximize profit; and preservation of these resources, to protect the environment.

This type of planning is usually conducted collaboratively by groups of experts in different fields Že.g., earth and environmental sciences, agriculture, remote sensing, operations research and may cover. the entire life cycle of a given decision chain. For instance, in an agriculture context, it involves determining what to plant where Ž . and when , how to prepare the soil, irrigation and fertilization policies, harvest and distribution logistics. The combination of  4  4 what, when and how to where constitutes the core of spatial decision support, which must take into account the fact that solutions are valid for a specific temporal and spatial frame.

A major tool in the framework of EMIS is provided by geographic information systems GIS . A Ž . GIS is a software that provides mechanisms to store, analyze, manipulate and visualize georeferenced data. GIS are used to help decision makers in identifying geographic regions that satisfy one or more criteria, exploring spatial and temporal relations among georeferenced data and providing data for analysis and simulation models 40 .<sup>w</sup> <sup>x</sup>

GIS are increasingly used to improve decision processes in environmental, urban and socio-economical applications. Even though the importance of GIS in spatial decision making is recognized, the capability of such systems is limited e.g., Ref. 28 .Ž <sup>w</sup> <sup>x</sup>. They are, above all, pieces of software that provide a wide variety of analysis functions over georeferenced data, and offer advanced cartographic visualŽ . presentation. However, they do not provide any means for helping users select the appropriate func tions to apply or to guide them in interpreting results.

GIS can only be considered as SDSS insofar as they provide tools to generate different types of maps, from which EMIS users identify solution alternatives. Each map reflects the choice of a given set of models and decision procedures. The spatial decision process goes through two stages: 1 map gener-Ž . ation using a GIS and 2 critical analysis of these Ž . maps. These stages can be iterated e.g., critical Ž analysis leads to generation of new maps , until. planners are satisfied. Since environmental planning is a very recent activity, these stages are performed in an ad hoc manner, with insufficient documentation and very little support for interchange of expertise among groups of planners. Thus, a considerable amount of time is spent in reinventing solutions to problems, and much money is wasted in not profiting from past experience.

The role of GIS within an EMIS and in spatial decision support is discussed in several contexts Že.g., Refs. 9,18,39 . There is, however, consensus <sup>w</sup> <sup>x</sup>.

that more powerful tools have to be provided in order to help decision makers.

This paper presents a computational tool which was developed with this objective in mind. This system, named WOODSS ŽWOrkflOw-based spatial Decision Support System , was developed in the . Institute of Computing of UNICAMP. It is based on combining the concept of GIS as spatial decision support tools within an EMIS to the notion of scientific workflows 48 . The latter are a special kind of<sup>w</sup> <sup>x</sup> workflow suited to documenting and specifying scientific experimental activities within a laboratory.

WOODSS captures planners’ interactions with a GIS in real time during their decision process, and has three main goals.

<sup>Ø</sup> Documentation. Users’ interactions with GIS are monitored and transformed into an intermediate representation — scientific workflows. These are stored in a database called WorkflowBase to docu-Ž . ment previous solutions to similar spatial decision problems. This allows faster comparison between different methods for data analysis, promoting better conditions for participatory planning. As shown subsequently, this documentation format has the advantage to be easier to use and understand than standard GIS programming or interaction modes.

<sup>Ø</sup> Support for decision making. This is ensured by the kinds of operations allowed by WOODSS. Indeed, workflows are not just yet another means of documenting planning activities, but also serve as executable specifications of these activities. This supports reproducibility of steps leading to a decision an important asset in decision support systems . Ž . Furthermore, WOODSS allows interactive updating of workflows thereby generating alternative decisionŽ procedures , their re-use as partial solutions to larger. problems again, fundamental in decision makingŽ . and their validation against predefined criteria Žequivalent to validation of steps leading to a decision ..

<sup>Ø</sup> Modelbase construction. Scientific workflows present a concise notation for simulation models in environmental planning. Thus, at the same time that it allows documentation of user decision procedures, WOODSS also supports progressive construction of the Modelbase of the decision support system Ž . DSS .

WOODSS was developed using the object oriented language Javae, and works in conjunction with IDRISI <sup>w</sup> <sup>x</sup> 14 , a GIS widely used in the environmental area. It is now being used by researchers and students of the Agriculture Engineering Faculty in UNICAMP, to document and speed up planning for agri-environ mental problems.

The rest of this paper is organized as follows. Sections 2 and 3 introduce SDSS, and the application of scientific workflows to spatial decision support within EMIS. Section 4 presents the WOODSS system architecture and Section 5 mentions some implementation aspects and a case study. Finally, Section 6 presents related work and Section 7 presents conclusions and future work.

## 2. Spatial decision support

## 2.1. Main issues

A DSS is a computer-based system designed to improve decision maker effectivity, by providing mechanisms to facilitate user interaction with data <sup>w</sup> <sup>x</sup> <sup>4</sup> and analysis models 21,45 .

A SDSS is a DSS in which the spatial dimension of the data is fundamental to the analysis of decisions. Spatial decision support relies heavily on maps, which form the backbone upon which plans and policies are defined. Problems can roughly be classified into siting Ži.e., WHERE to place some given object — e.g., a dam, a house, a park and. spatial allocation Ži.e., for a predefined location, WHAT is the best object among a class of objects to place there e.g., a crop or building type . In the first case,Ž . the main issue is determining the location, whereas in spatial allocation the unknown is the object itself. Some problems may require combination of both characteristics e.g., in routing or urban expansion Ž planning . Environmental planning, furthermore, in- . volves studies of risk<sup>r</sup>impact assessment, and contingency planning, which combine WHAT and WHERE to WHEN and HOW.

Spatial decision making has traditionally been associated with the use of GIS. However, as stressed in Refs. 10,28 , GIS do not adequately support the <sup>w</sup> <sup>x</sup> spatial decision process because they lack the appropriate modeling capabilities and do not accommodate variations in context or process.

If, on one hand, GIS lack support for spatial decision making, on the other hand current decision support systems do not provide adequate tools to solve spatial problems, especially those concerning environmental issues, which are fuzzier in nature than urban spatial problems.

Indeed, traditional DSS Že.g., Refs. 34,45 lack<sup>w</sup> <sup>x</sup>. the cartographic presentation facilities essential to spatial decision making. Furthermore, traditional DSS are frequently based on models which consider only one criterion, e.g., distance or cost functions to be optimized. In the spatial context, more complex realities must be considered, which must be analyzed through the combination of multiple criteria. Multiple criteria decision making techniques e.g., Refs. Ž <sup>w</sup> <sup>x</sup> 20,24,29,47 allow users to select a satisfactory. solution among alternative solutions, based on analysis of multiple criteria with different priorities. For example, erosion forecasts must consider factors such as land use, climate, slope, aspect and digital elevation model.

## 2.2. The spatial decision process

The spatial decision process within an EMIS can be described as the repeated iteration of four steps, which are based on the methodology in Ref. 37 for<sup>w</sup> <sup>x</sup> the development of environmental planning applications. These steps, which have an immediate correspondence to the non-spatial decision steps de-Ž . scribed in Ref. 11 are:<sup>w</sup> <sup>x</sup>

1. Planning. This is a group decision making process and involves the definition of the objectives, the geographic area and the data and models to be applied.

2. InÕentory<sup>r</sup> gathering of data. It consists in determining the relevant data and in collecting these data through, for example, air photos and satellite images.

3. DeÕelopment. It corresponds to the implementation in a GIS of the models, using the data defined by the previous step. Models are implemented by constructing programs which invoke GIS functions.

4. Assessment. It involves impact assessment, inter-

pretation of results and specification of policies. The first three steps correspond to the generation of a set of maps, whereas assessment consists in analyzing the maps to take decisions and calibrate the models employed. From a DSS perspective, each map is the result of the execution of a model. Each map in the set may reflect an alternative solution scenario for a given problem, or the map set may describe complementary actions to be taken in a given situation.

The entire process is complicated by the fact that data are very heterogeneous e.g., collected by dif-Ž ferent devices, for distinct geographic scales and non-homogeneous spatial and temporal units and . that models vary according to the geographic region to which the problem applies. Thus, whereas map production for cartographic purposes is relatively straightforward e.g., produce a map of the State of Ž Parana in Southern Brazil, or the state of Bahia in NE Brazil , map production for spatial decision sup-. port is very complex. For instance, the models and simulations necessary to produce an erosion map for the State of Parana are very different from those applied to the State of Bahia, due to enormous differences in soil, climate, vegetation, relief and land use management. Data and models are furthermore temporally sensitive e.g., seasonal changesŽ . and subject to socioeconomical constraints.

Assessment — map interpretation — is again dependent on the goals and expertise of the analysts, and on legislation and cultural issues. Thus, given one specific problem in environmental planning — e.g., define a schedule for sugar cane crop rotation for a specific region in Brazil — a multitude of map sets may be generated and, subsequently, multiple Ž . and even conflicting policies may be devised based on the maps.

WOODSS provides support to the creation of maps, i.e., steps 1 through 3 of the decision process.

## 3. Workflows

WOODSS is based on the concept of scientific workflows. A workflow denotes the controlled execution of multiple tasks in an environment of distributed processing elements 41 . It can be defined a<sup>w</sup> <sup>x</sup> set of tasks involved in a procedure along with their interdependencies, inputs and outputs. Each task is called an actiÕity, and can be executed by one or more agents, in a given role — it is a unit of work. An agent is a person or software component able to execute one or more activities.

Workflows are gaining increasing acceptance in the business world as a means of documenting and organizing procedures, as well as helping the coordination of groups. Workflows were conceived as a means for describing procedures in business environments which can be repeated over and over again.

The goal of a workflow management system Ž . WFMS is to provide facilities to specify and execute workflows 8 . Traditionally, these systems dis-<sup>w</sup> <sup>x</sup> tinguish between workflow modeling and execution. The modeling phase consists in creating a workflow specification, which is a description of activities, dependencies and agents. Activities may be automatic executed by a software component or manual Ž . Ž . performed by a person . Dependencies describe constraints among activities and can be data, temporal and execution dependencies 41 . The execution<sup>w</sup> <sup>x</sup> phase consists in running executing a given work-Ž . flow specification.

## 3.1. Scientific workflows

The term scientific workflow <sup>w</sup> <sup>x</sup>43,48 was coined to denote a specific kind of workflow which can be used to document and control the execution of scientific experiments and procedures — e.g., in DNA sequencing 33 or in geoprocessing 4,32 . Scientific<sup>w x</sup> <sup>w</sup> <sup>x</sup> work is characterized by a great degree of flexibility and presents a much higher amount of uncertainty and exceptions than business work. Thus, standard workflow mechanisms are insufficient to describe this kind of work.

In business applications, the main motivation for introducing workflow management is the desire to ‘‘re-engineer’’ work to enhance efficiency. The motivation for workflow management in scientific applications, however, is less to enhance efficiency, but to control experiments, and to make available to scientific users the information on how experiments were conducted.

Intuitively, scientific workflows differ from standard business workflows in two senses: a activitiesŽ . are experiment-oriented as opposed to business-ori-Ž ented ; and b the ‘‘flow of the work’’ being mod- . Ž .

eled and the interactions among activities must support the trial-and-error and ad hocness of scientific experimentation. More precisely, scientific workflows are defined as extending traditional workflow functionality to support the following aspects <sup>w</sup> <sup>x</sup> 2,43,48 .

<sup>Ø</sup> Ad hocness and incompleteness. Scientific workflows can be executed even when incomplete. being progressively built during their execution. Modeling and execution phases are interleaved — it is only upon the completion of an activity that subsequent activities may be specified. Traditional workflows, on the other hand, must be totally specified before being executed.

<sup>Ø</sup> Partial re-use. Scientific workflows differ from the traditional ones in the sense that they are considered to be building blocks for experiment specification. Thus, one can re-use partial workflows to specify new ones.

<sup>Ø</sup> Abandon<sup>r</sup>rewind and dynamic modification. Scientific workflows allow not only re-executing an activity but also rewinding to a previous one, reestablishing its context and continuing the execution through another course of action, which corresponds to specifying a new workflow on the fly.

<sup>Ø</sup> Tracing of inÕalid processes. In the scientific domain, decision processes are based in a trial and error mechanism learning from mistakes . Hence,Ž . unlike business workflows, scientific workflows serve as a means to document both successful and unsuccessful processes. The latter should be, moreover, amenable to re-execution.

<sup>Ø</sup> Specification from case. Traditional workflows are specifications that are expected to be executed frequently. Each such execution is called a case. Scientific workflows, on the other hand, may be executed only once e.g., for unsuccessful trials . Ž . Furthermore, since they may be specified on the fly, their specification may be prompted by the case — i.e., the case defines the workflow, instead of the specification guiding the case.

## 3.2. Using scientific workflows to document enÕironmental decision making

We recall that map production is an important stage in spatial decision support. Users interact with GIS during their decision process to generate maps over which decisions are based.

Some types of spatial decision procedures, especially in network-related problems, are already well understood e.g., Ref. 36 . Environmental decisionŽ <sup>w</sup> <sup>x</sup>. making is however still in its infancy, in part due to our yet incomplete knowledge of natural phenomena. Among the particularities of environmental decision processes, Mann 31 mentions: <sup>w</sup> <sup>x</sup>

<sup>Ø</sup> The lack of precision in goal definition e.g., no Ž standard definition for ‘‘sustainability’’ or ‘‘biodiversity’’ ;.

<sup>Ø</sup> The complexity and dynamicity of the natural environment, where feedback paths entail evolution and continuous change;

<sup>Ø</sup> The dependency of problems on the geographic scale, and the fact that the decision making process straddles many different approaches, reflecting planners’ varying views of natural phenomena;

<sup>Ø</sup> Finally, several problems are new, sometimes one-of-a-kind, and do not occur frequently enough to warrant generalization of solutions or rigorous mathematical treatment.

Environmental decision making has thus a strong component of empirical experimentation, with a long cycle of successive approximations through trial and error. It can thus be naturally expressed as a scientific experiment, in which the goal is to produce a map which will indicate how to solve a problem. WOODSS takes advantage of this analogy and uses scientific workflows to document and support spatial decision procedures for environmental problems.

Environmental decision making through a GIS corresponds to defining and calibrating a model by using the GIS’ functions to construct a set of maps. Map generation is a partially ordered sequence of activities, which are related by data and control links. These activities intermingle direct interaction with the GIS with the mouse and coding of macrosŽ . Ž or programs . This can be appropriately modeled by. scientific workflows in the following aspects.

<sup>Ø</sup> Ad hocness. Map generation in environmental planning has a strong empirical component, not being specified in advance but being determined during the decision process according to the GIS being used and the participants in the decision process.

<sup>Ø</sup> Partial re-use. In spatial decision making, Ž . parts of maps can be combined to produce more complex maps.

<sup>Ø</sup> Abandon<sup>r</sup>rewind and dynamic modification. The map sequences built during environmental planning are often discarded when users detect a trend that is not of interest. Map construction parameters can furthermore be dynamically modified by invoking distinct GIS modules to perform one given function. Decisions on which module to choose are data and context-sensitive — i.e., according to the way intermediate<sup>r</sup>partial maps look.

<sup>Ø</sup> Tracing of inÕalid processes. Environmental planners often need to reproduce unsuccessful map generation procedures in order to identify error sources.

<sup>Ø</sup> Specification from case. Many models are constructed while creating a map, rather than being specified in advance. This is a consequence of the fact that environmental planning involves many unknowns, and that often models have to be experimentally built from scratch.

## 4. The WOODSS system

WOODSS is a system based on scientific workflows whose goal is to support spatial decision processes. WOODSS supports all characteristics of these workflows as defined in Section 3. Scientific workflows are used by WOODSS in three roles: i as a means forŽ . documenting a decision process; ii as high-levelŽ . specifications of an environmental simulation model; and iii as executable parametrized specifications ofŽ . decision procedures, which can be re-used and adapted for similar situations. Workflows stored in WOODSS can be queried to give a global vision of the work developed to solve a problem or to guide the resolution of similar problems. Furthermore, they can be launched to automatically re-execute analogous activities with different parameters.

## 4.1. WOODSS from a DSS perspectiÕe

A traditional DSS architecture considers the interaction of three components: Interface, Database and Modelbase 11 . The interface interacts with a <sup>w</sup> <sup>x</sup> database management system DBMS , which ma-Ž . nipulates data, and a modelbase management system Ž . MBMS , which manipulates models to be applied on these data. Fig. 1, adapted from Ref. 22 , illus-<sup>w</sup> <sup>x</sup> trates the architecture of WOODSS in this context. <sup>5</sup>

## 4.1.1. Database

A DSS must manipulate internal application andŽ . external for example, national and international Ž policies data, and user’s estimatives. Data may be . queried by users or provided as the input to models. The DBMS must allow the combination and visualization of heterogeneous data and the manipulation of subjective data. In WOODSS, the Database encapsulates two kinds of data: georeferenced data used in the planning process, and which is manipulated by the GIS; and a WorkflowBase, which stores scientific workflow specifications and which use the other data to describe the map generation process in GIS. Both bases are stored in a relational database system.

## 4.1.2. Modelbase

Models provide analysis capabilities to the DSS. There are different kinds of models, depending of their purpose, the use of random parameters, their generality and their structure. The Modelbase of WOODSS consists of spatial analysis models specifiedŽ in terms of combination of GIS functions and deci-. sion techniques employed by the users. The decision process for environmental planning often combines four types of models 18 : transport model migration<sup>w</sup> <sup>x</sup> Ž of substances in air, water or ground , process model . Žsimulation of interactions of economical and natural agents , resource utilization model, and ecosystem. model. The heterogeneity of issues encountered is exemplified by the variety of analytical and probabilistic models proposed e.g., see Ref. 16 , whereasŽ <sup>w</sup> <sup>x</sup>. Ref. 35 presents over 100 methodologies for imple- <sup>w</sup> <sup>x</sup> menting models in environmental planning.

Each model, in environmental decision making, can be specified in terms of its inputs data files andŽ parameter values , outputs materialized in maps . Ž . and states 39 . Inputs, states and outputs can assume <sup>w</sup> <sup>x</sup> different values during a given simulation<sup>r</sup>experiment. The workflows of WOODSS document the execution of models, for specific parameters and inputs.

![](/api/attachments/ED728FNT/fulltext/images/8f203dd835268d561704f1df6f37cc5a770ccd728db0e11e5af86b0a8b1f1e4d.jpg)  
Fig. 1. WOODSS from a DSS perspective. The GIS is responsible for handling georeferenced data and providing functions to execute the spatial analysis models.

They can, however, be re-executed with distinct parameters and inputs, thus, constituting a high-level specification of a set of simulation models. The Modelbase of WOODSS is geared towards process models, resource utilization models and some types of ecosystem models for medium and small geo-Ž graphic scales . Transport models and ecosystem . models for large scales would require the use of a more versatile DBMS, with active and object-oriented capabilities.

## 4.1.3. Interface

The interface allows users to interact with models and data. This component requires a great part of the effort of system development. In WOODSS, the interface is coupled to a monitoring layer which intercepts user interactions, translating them into workflows stored in the WorkflowBase.

## 4.2. Architecture

The architecture of WOODSS — illustrated in Fig. 2 — consists of five modules: Interface, Monitor, Update, Query and Workflow Manager. The Monitor module captures users’ interactions with the GIS, informing them to the Workflow Manager. The latter is responsible for managing the WorkflowBase. The Interface module allows users to graphically visualize and create planning processes and models in terms of workflows. It mediates user requests for browsing Query module and update Update mod-Ž . Ž ule the WorkflowBase. .

Workflows, models and data are encapsulated in a database, managed by a relational DBMS. Spatial models are specified as workflows and executed within the GIS.

This architecture isolates users from internal data storage details — scientific workflows can be stored in a standard database, and thus take advantage of standard DBMS functions such as query optimization and indexing. Furthermore, the architecture can be coupled to several GIS, since the Monitor is the only module that interacts with the GIS. Thus, coupling WOODSS to a GIS requires only customizing the Monitor.

![](/api/attachments/ED728FNT/fulltext/images/eca257e6594837364bf187d50b0976b20c88baae11567258fad69ecbe3ca6829.jpg)  
Fig. 2. WOODSS architecture. Coupling to the GIS is achieved by means of the Monitor module, which ensures adaptability of WOODSS to several GIS.

## 4.2.1. WorkflowBase

The WorkflowBase is a relational database. It consists of set of scientific workflows and related metadata, stored in database relations Ž . i.e., tables . Each workflow is specified in terms of activities, data, dependencies and agents, translated into a set of relation tuples Ž . i.e., table rows .

Metadata have a very important role in supporting browsing and data transfer in environmental information systems, serving as additional online documentation for automated tools and human users 8 . In<sup>w</sup> <sup>x</sup> WOODSS, metadata are used to document facts related to a workflow and to the associated decision making process. Each workflow is linked to a metadata record. This record contains information about the objectives of a decision process and the geographic area considered, both being necessary to identify the nature of the environmental planning problem being handled 37 . The metadata record may include, fur-<sup>w</sup> <sup>x</sup> thermore, information about the author of the workflow and other additional data considered relevant Ž . e.g., quality of data used .

## 4.2.2. Interface

The Interface is the only module visible to the user, and transforms user query and update requests into appropriate sequences of commands to the other modules. It allows two types of interaction modes:

<sup>Ø</sup> Textual — The user fills in parameters in predefined query and update forms.

<sup>Ø</sup> Direct Manipulation — The user uses the mouse to manipulate workflow elements or click on some interface button.

The first type of interaction is employed to browse the WorkflowBase — retrieving all workflows that satisfy a given set of conditions e.g., concern a Ž specific region . The second type of interaction typi- . cally occurs when the user has already retrieved the workflows of interest and either wants to examine or update them, or to select sub-workflows for execution or re-use.

Both interaction modes hide from the user the fact that the storage and data management system is a relational DBMS. The interface just forwards user requests to the Update and Query modules, which interact with the Workflow Manager to transform these requests into SQL commands to the databaseŽ . or GIS macro programs to the GIS . All the userŽ . ever sees are workflows e.g., Fig. 3 or query Ž . <sup>r</sup>update forms e.g., Fig. 4 .Ž .

## 4.2.3. Query module

The Query module handles querying and navigation in the WorkflowBase. Users can request access to a specific workflow by name or sets of work- Ž . flows by keywords . Other typical queries are as Ž . follows.

<sup>Ø</sup> Area-based queries. Users search for decision processes and<sup>r</sup>or models executed involving a specific geographic area. This allows finding out, for instance, all studies conducted in a given region. One example would be to find out if there is a crop yield forecast model for the area in question.

![](/api/attachments/ED728FNT/fulltext/images/f0d576d485c39259e9fa69bec8eb1c310f57ab65f1da88e4e3b6cc05edbb0348.jpg)  
Fig. 3. WOODSS main interface.

![](/api/attachments/ED728FNT/fulltext/images/0499cae69565a652c8701b5ebfed3468d93b7296ec18071136ca7e1011416299.jpg)  
Fig. 4. Result of querying ‘‘slope calculation’’ activity.

<sup>Ø</sup> Problem-based queries. Users look for decision processes developed to solve problems with similar objectives, to take advantage of experience gotten in the resolution of the same problem over other geographic areas. For instance, a given erosion modeling procedure in one region may be adopted for other areas with similar characteristics.

<sup>Ø</sup> Process-based queries. Users request to see the sequence of activities that originated a given map set. This could help determining the quality or precision of the set and, indirectly, of the decisions taken based on the data.

## 4.2.4. Update module

The Update module mediates creation, removal or modification of workflows. A workflow can be updated in two ways.

<sup>Ø</sup> Component modification — The user requests insertion<sup>r</sup>deletion<sup>r</sup>modification of any workflow component individual activities, data files, depen- Ž dencies and agents . Metadata records can only be. created by invocation of the Update module equiv- Ž alent to writing annotations on sets of activities ..

<sup>Ø</sup> Workflow creation — The user requests combination of existing workflows e.g., by concatenat- Ž ing them . Commonly, experts approach a decision . problem by solving sub-problems and combining the solutions. This type of update contemplates this approach to decision taking. Workflow creation is also performed by the Monitor module.

## 4.2.5. Workflow Manager

The Workflow Manager is responsible for managing the WorkflowBase, handling the communication between the other modules and the DBMS, by translating the stored relations into workflows and viceversa. Basically, it manages workflows according to two main functionalities:

<sup>Ø</sup> Query<sup>r</sup>browse — retrieves workflows from the WorkflowBase. A user’s request via the Interface is transformed by the Query module into a set of SQL commands to the underlying database. The tuples retrieved are graphically presented to the user as workflows. These queries act both on metadata and on the workflows themselves.

<sup>Ø</sup> Update — creates, deletes and modifies workflows by requesting updates on the corresponding relations stored in the WorkflowBase. Updates may be requested either by the Update module user- Ž originated or the Monitor during workflow genera- . Ž tion ..

## 4.3. Interaction User–GIS–WOODSS

WOODSS caters to three kinds of user interaction modes see Fig. 2 . These modes support the aspects Ž . of scientific workflows defined in Section 3.

Ž . 1 User–GIS. Users ignore WOODSS and interact with the GIS, to generate maps according to some model, which is translated into executing sequences of GIS functions. WOODSS monitors this interaction in real time and generates the corresponding scientific workflow specification specifying workflows fromŽ the case ..

Ž . 2 User–WOODSS. Users interact only with WOODSS, querying and updating the WorkflowBase. Typically, this occurs when decision makers want to find out about previous solutions to a similar problem. WOODSS stores both successful and unsuccessful workflows, which allows not only re-use of past experiences partial re-use , but also learning fromŽ . past mistakes tracing invalid processes , a very im- Ž . portant factor in decision making.

Ž . 3 User–GIS–WOODSS. This mode of interaction combines the previous ones. Users alternate between WOODSS and the GIS, using the information in the WorkflowBase to continue their decision process. This allows creating alternative scenarios and designing new decision strategies. In practice, this corresponds to querying the WorkflowBase to find the workflows of interest, selecting and combining parts of these workflows to create a new workflow, and having the GIS execute this new workflow ad hoc-Ž ness and dynamic modification ..

## 5. Implementation

WOODSS was implemented on a PC platform, and the target GIS was IDRISI for Windows version 2.0. The implementation was developed with the object oriented language Javae. The WorkflowBase is implemented as relations in a relational database, which is connected to Java through the JDBC interface. This section gives a brief description of the implementation. For more details, the reader is referred to Ref. 42 .<sup>w</sup> <sup>x</sup>

## 5.1. IDRISI and WOODSS

IDRISI is a GIS developed to be used in microcomputers. It is widely used in environmental monitoring and natural resources management. IDRISI records user interactions in a sequential log file, which was used as input to the Monitor module of WOODSS. User interactions activities withŽ . IDRISI to generate maps are of three kinds: clicking at maps and invoking functions from a set of menus; typing commands; and running programs Ž . macro files .

Lines in the log file correspond to the execution of an IDRISI function, or to an error or warning message. In the first case, the line contains the name of the function and its parameters, which vary according to the function and, possibly, a option in it. For instance, the log record ‘‘c: idrisiw OÕerlay w421 1 image1 image2 image21’’ indicates that function oÕerlay was executed with option 1, using as input images stored in files image1 and image2, and producing as output image stored in image21. An image overlay corresponds roughly to adding the contents of the images to obtain a third image — e.g., an overlay of a soil and a vegetation maps will result in a composite map. This operation may be weighted — e.g., attributing weights to different values of soil and vegetation may result in a map indicating areas where conditions are good for planting a given type of crop.

The Monitor module was implemented to read the log of IDRISI in real time while it is being updated with user operations. It performs a syntactic analysis of the log file, identifying activities actually executed Ž . which did not generate errors , disregarding messages and identifying activities that were not executed because of errors. The log analysis also allows detecting data dependencies among activities. Other types of dependencies cannot be derived from the log and must be provided by the user directly via the Update module.

## 5.2. WorkflowBase

WOODSS WorkflowBase is implemented in the relational DBMS Visual FoxProe, version 5.0. Each workflow corresponds to a set of tuples stored in five relations: Activities, Data, Workflow, Metadata and Dependencies. The Metadata relation contains information about authors, objectives, geographic area and relevant comments. The Workflow relation maintains a record of the workflows in the WorkflowBase.

Each activity corresponds to a tuple in the relation Activities. It contains an internal WOODSS identifier, a name descriptor, an indication if it is a manual activity or if it was executed in IDRISI, pointers i.e., Ž in relational database terminology, foreign keys to. its input and output files, and activity-dependent parameters. Input and output files are used by the Workflow Manager to derive data dependencies between activities.

The Data relation records all data files used and produced in a given decision process. Each file corresponds to a relation tuple, containing a WOODSS internal identifier and other parameters e.g., fileŽ name ..

The Dependencies relation maintains data dependencies, as well as a restricted set of temporal and execution dependencies. Each tuple in this relation associates an activity precedent to another activityŽ . Ž . subsequent through pairs of internal identifiers Ž . foreign keys . Furthermore, each tuple contains additional information which depends on the type of dependency being stored. For data dependencies, the tuple stores the file identifiers of files which are produced by one activity and used as input by another. Execution dependencies are represented in a similar way, signalling when the beginning of an activity depends on the successful termination of other s . Temporal dependencies allow synchroniz-Ž . ing activities. In WOODSS, they are specified only for documentation purposes, since their enforcement would require modification of the transaction mechanism of the underlying DBMS e.g., Ref. 41 .Ž <sup>w</sup> <sup>x</sup>.

## 5.3. Workflow Manager

The Workflow Manager does not use a commercial WFMS. Rather, it is implemented within WOODSS to manage scientific workflows. Each log entry corresponding to an activity executed in IDRISI is transformed in a tuple in the relation Activities. The Workflow Manager inserts a tuple in the Data relation each time a new file is referenced. It inserts a tuple in the relation Dependencies each time it determines that an activity uses a file generated by a previous activity in the workflow. This requires that the Monitor keeps track of all files mentioned in a log until the end of a given decision process either Ž successfully or unsuccessfully . Manual activities. Ž . e.g., command editing and temporal and execution dependencies must be directly provided by the user through the Update module.

## 5.4. Query and Update modules

Query and Update modules are responsible for the access to the WorkflowBase. Once a workflow is selected, users can query and update information about activities, data, dependencies and metadata. Query and update requests are forwarded by the Interface to the Workflow Manager, which translates them into SQL query and update INSERT, DELETE, Ž UPDATE commands to the five relations within the. WorkflowBase. The result of these operations is returned to the Workflow Manager, and shown graphically to the user by the Interface module.

## 5.5. Interface

The interface is responsible for the communication of users with the Query and Update modules. Fig. 3 illustrates the main interface of WOODSS. It depicts a partial workflow which is part of the case study discussed in Section 5.7. It consists of a set of buttons for user interaction and a workflow display window. Each rectangle represents an activity, and each arrow a dependency, which is labeled by file names data dependency or conditions temporal orŽ . Ž execution dependencies . Each activity is labeled. with its name and, if executed in IDRISI, the IDRISI function is used.

For instance, in the figure, activity Slope Calculation is linked to UserDefined Classification via the Slopes file, which is produced as output by the former and used as input by the latter. This means that there is a data dependency from Slope Calculation to UserDefined Classification. Slope Calculation is an activity performed by invoking IDRISI function surface.

Users can access the current workflow by clicking on the Current Workflow button the third interac-Ž tion mode , and navigate through the WorkflowBase . clicking the WorkflowBase button. Once a workflow is shown in the workflow display window, users can query or modify its metadata record through the Metadata button, insert manual activities or dependencies through New ActiÕity and New Dependency, respectively, or update workflow components. Finally, Begin Selection and End Selection buttons let users select a partial workflow.

Activities and dependencies can be queried by clicking on the corresponding workflow graphical elements. Parameters displayed on the window are activity-dependent. Fig. 4 shows the result of querying the contents of the Slope Calculation activity. The Modify button, in the figure, is the one that allows update of activity details.

## 5.6. Re-execution and definition of new decision processes

WOODSS provides the facility of re-executing sequences of activities performed in IDRISI and that were documented through workflows. This way, users need not repeat their manual interaction with IDRISI, which is time consuming and error-prone. If a workflow is updated for re-execution, it is considered to be a new workflow — akin to defining a new<sup>r</sup>alternative decision process for a given problem.

Ideally, workflow launching would invoke a GIS directly. Unfortunately, because IDRISI is a proprietary software, this is not possible. So, WOODSS automatically creates a macro file from the workflow. This file is made available to users, who can execute it on IDRISI.

This is a powerful feature of WOODSS, since it is equivalent to programming applications directly in a GIS using a workflow notation. It is a means of ensuring reproducibility of a sequence of steps in a decision process. Re-execution has two roles in a decision support process: a independent observersŽ . can analyze past procedures, to audit or validate them; b at the same time, similar problems can be Ž . approached in an analogous way.

Users can select activities to be updated or re-executed. Fig. 5 illustrates the re-execution window after selection of four activities from the workflow in Fig. 3. The possibility of updating existing workflows is another plus offered by WOODSS. When the updates performed are just the change of input files or of parameters, without changing activities, this is tantamount to parameter tuning in DSS. The most complex update is building new workflows from partial workflows. It corresponds to constructing the solution of a problem by combining solutions of its parts.

## 5.7. Example of enÕironmental planning using WOODSS

We now give an example of an environmental decision making process using WOODSS. The workflow of Fig. 3 represents part of the solution for a siting problem described in Ref. 14 , and which was<sup>w</sup> <sup>x</sup> adapted to Brazilian agri-environmental data.

Given a certain region in the state of Sao Paulo,˜ planners must identify areas which are appropriate for planting sugar cane. The main constraints are that these areas are characterized by a little or noŽ . declivity to allow mechanical harvesting proce- Ž dures , b close to waterways for irrigation pur-. Ž . Ž poses , while at the same time keeping a certain. minimum distance from c natural reserves and dŽ . Ž . forest areas, to avoid environmental degradation. Finally, they must be e close to highways, to Ž . ensure appropriate transportation of the cane to the mills, and f respect urban distance constraints to Ž . Ž avoid increasing urban air pollution ..

## 5.7.1. Beginning a planning session

The user initially activates WOODSS and browses the WorkflowBase to check if there have been similar planning activities already performed for the same area combination of area-based query and problem-Ž based query . Browsing is initiated by clicking on. the WorkflowBase button see Fig. 3 . The user isŽ . next presented with a query form, with the options of indicating a specific workflow by name or filling inŽ . one or more fields. Suppose the user enters data in form fields Area — entering region coordinates — and Keywords — typing ‘‘sugar cane’’. Query form parameters are checked by WOODSS against the Metadata relation, to retrieve all workflows that obey the conditions.

![](/api/attachments/ED728FNT/fulltext/images/16d9ff10128cdd2df4d386ff0f19d6a7d875ae24316e7b501d1708eb02da4952.jpg)  
Fig. 5. New workflow created from partial selection and update of workflow of Fig. 3.

## 5.7.2. Situation 1 — a preÕious solution for the solution for the problem exists

Assume first that WOODSS finds a workflow that answers the request. It is then presented to the user, who can either re-execute it on IDRISI, or update it and execute the new updated version. Updating includes, among others, changing input files e.g., Ž running the workflow for the new region , changing . parameters e.g., tuning , modifying workflow de- Ž . pendencies and attributes or creating new dependencies and activities by clicking onŽ New ActiÕity and New Dependency interface buttons . Workflow . Ž . re execution corresponds to asking WOODSS to translate the workflow into IDRISI executable code. Fig. 6, for instance, corresponds to the IDRISI code generated by WOODSS for the partial workflow of Fig. 3.

## 5.7.3. Situation 2 — no preÕious solution exists

Suppose, on the other hand, that WOODSS does not find any workflow to satisfy the request. In this situation, the user must start a new decision procedure by interacting directly with IDRISI. As soon as the user switches to IDRISI, WOODSS initializes a new Ž . empty workflow called Current Workflow, and the Monitor module will start capturing into it user interactions in real time.

According to the user’s decision strategy, the first constraints to be checked will be those concerning declivity a and forestŽ . Ž . <sup>r</sup>reserve c, d constraints. The actual interaction with IDRISI is as follows. First, the user invokes the IDRISI Surface operation on relief data, to obtain a declivity map, and then classifies the areas in this map according to the gradient e.g., feeble, medium, high using aŽ . Reclass operation. Next, the user finds out which areas are under environmental protection by identifying re-Ž serves and forests in a land use map , and pinpoints. regions according to distance from the reserves Ž Distance operation , again reclassifying the result into. distance zones. The user then combines all these maps into an intermediate map by applying successive OÕerlay operations. The result is an intermediate map that indicates areas where sugar cane can be planted as far as a declivity, c forest and dŽ . Ž . Ž . reserves constraints are concerned.

There still remains to further restrict these areas according to b irrigation, e transportation and fŽ . Ž . Ž . urban constraints. Suppose however the user wants to interrupt this decision procedure, to check the steps taken so far. In order to do this, the user can switch to WOODSS main interface window and click on the Current Workflow button. Immediately, the user will see the current execution state displayed on Fig. 3. Internally, this is handled as an SQL query Ž . Query module to the WorkflowBase, asking for the Current Workflow.

Once the user examines the current workflow, there are three options to choose to continue the spatial decision process: i to go back toŽ . IDRISI, in which case the current workflow will continue being constructed in real time by WOODSS Žthe user is happy with what has been done so far ; ii to select. Ž . just part of this workflow, optionally editing it by adding activities and dependencies, and having it executed as the beginning of a new decision procedure just some of the steps taken were appropriateŽ . — see Fig. 5; or iii to abandon the current execu-Ž . tion and start a new one. In the last two cases, the user can indicate whether the abandoned current workflow should be stored in the WorkflowBase as an incomplete<sup>r</sup>erroneous solution. Also, at any time, the user can enter metadata and update and query information on the WorkflowBase.

After several such interactions, the user comes up with the final map which indicates the regions suitable for sugar cane plantation. This map must be examined in a context which involves other related information, which does not concern this paper. Fig. 7 shows a partial screen copy of this map, in the area of the county of Campinas. The corresponding full workflow will not be shown here, for readability reasons.

![](/api/attachments/ED728FNT/fulltext/images/1647162676c81ecab199e98d1660267f358f44bdea5e67765a8463a3bd967aae.jpg)  
Woodland Sugar Cane Urban Areas Water Main Roads  
Fig. 7. Regions suitable for planting sugar cane.

## 5.7.4. Situation 3 — participatory planning

Even though the example describes the work of a single user, it can also concern several users cooperating to develop a solution using the workflows as a communication means. For instance, one user can develop the first part Fig. 3 , and some other user Ž . can develop another part, and the final result is obtained by combining the workflows and executing this composite workflow. Or groups of users can develop partial or alternative solutions at different times, and keep track of what everyone is doing by looking at the respective workflows.

## 6. Related work

The work presented in this paper is related to two research fields: use of scientific workflows for experimental activities in a laboratory, and use of GIS in spatial decision support, within an EMIS. This paper reports the first attempt to link both contexts and implement them into a single tool.

Scientific workflows are a relatively new concept in the area of workflow management, and their use is still a matter of research. They have been reported as a means of documenting and keeping track of activities in a scientific environment. Research in the area is related to their use in specific domains, varying from their capacity to support collaborative scientific task execution e.g., Ref. 2 , long transaction capa- Ž <sup>w</sup> <sup>x</sup>.

bility 43 and, more specifically, their suitableness<sup>w</sup> <sup>x</sup> for documenting geoprocessing tasks 4,50 . The em-<sup>w</sup> <sup>x</sup> phasis, however, is on task execution and documentation, and not their role in decision support. Furthermore, unlike WOODSS, there is no implementation which allows direct linking to a GIS.

On the other hand, there are many proposals for extending GIS to provide spatial decision support. These proposals can be roughly classified into aŽ . case study presentation, b model implementation Ž . and c architecture and system design. Approaches Ž . vary between considering a GIS as the spatial DSS itself, to building or proposing a DSS which will take advantage of data stored within a GIS.

Case study presentations are centered on showing how the use of a GIS’ functions and cartographic display improves decision making in specific problems. The examples in Ref. 23 show how environ- <sup>w</sup> <sup>x</sup> mental problems often fall into a multi-criteria multi-objective situation, complicating the decision process. Other examples of case studies solved by extending GIS are found in Refs. 13 evaluation of<sup>w</sup> <sup>x</sup> Ž health risk awareness and assessment in the Philippines , 7 use in environmental study support , or . <sup>w</sup> <sup>x</sup> Ž . <sup>w</sup> <sup>x</sup> 49 role in strategic policy analysis concerning the Ž environment ..

Model implementation studies concern the building of tools that help spatial analysis studies within or in parallel to a GIS. This approach consists in ‘‘hardwiring’’ a set of models into a GIS for a given problem domain. As remarked by Ref. 28 , the GIS<sup>w</sup> <sup>x</sup> will provide the database and interface component of the DSS and the added module will contain the models. Examples are Refs. 46 tools which apply <sup>w</sup> <sup>x</sup> Ž probabilistic Bayesian networks to combine geographic information , 15 application of expert sys- . <sup>w</sup> <sup>x</sup> Ž tems to environmental planning , 24,30 application . <sup>w</sup> <sup>x</sup> Ž of multi-criteria techniques to GIS tools for decision support , 12 facility location in an urban environ- . <sup>w</sup> <sup>x</sup> Ž ment , 36 transportation planning and 47 in- . <sup>w</sup> <sup>x</sup> Ž . <sup>w</sup> <sup>x</sup> Ž dustrial siting . The three last studies are also exam-. ples of the growing work which integrates GIS and operations research for decision support.

Even though helpful in understanding the variety of issues involved in spatial decision processes, these studies do not help the more general problem, namely, how to construct SDSS. WOODSS can be placed within this category. Examples of this type of research are the work of Refs. 1,5 both of which<sup>w</sup> <sup>x</sup> Ž propose a general architecture for environmental decision support , 27 which provides an analysis of. <sup>w</sup> <sup>x</sup> Ž the multiple roles of GIS in spatial decision support ,. <sup>w</sup> <sup>x</sup> 25 environment for group work and 26 forŽ . <sup>w</sup> <sup>x</sup> Ž collaborative environmental planning on the www .. Except for this last work, which actually implemented a documentation and mediation system on the Web, the others present architectures without implementation. This is not to say that implementations do not exist. However, they are of limited scope, and usually do not take advantage of combining GIS facilities to decision support capabilities. The emphasis in Ref. 26 , as opposed to<sup>w</sup> <sup>x</sup> WOODSS, is in the collaborative discussion issues involved inŽ . environmental planning, rather than on the modeling itself.

From a functionality point of view, WOODSS approaches the work in Ref. 17 . The latter is based on<sup>w</sup> <sup>x</sup> the fact that modeling is one of the key activities necessary to solve a complex problem, and that therefore a system which supports modeling will enhance decision making activities. Their system is based on allowing users to define and simulate several types of models, and storing these models in a model base. The system is geared towards users who are able to understand equations, motivated by environmental modeling. A similar system is described in Ref. 44 , in the context of environmental process<sup>w</sup> <sup>x</sup> modeling. The paper describes a computational environment for characterizing scientific modeling methods, in order to support representation, manipulation and evaluation of scientific concepts. Models are constructed in terms of R-structures Žrepresentation structures , which are abstract representations of a. concept similar to the concept of abstract data types .Ž . The dynamics of real world processes are modeled through sequences of R-structure instance transformations. These ideas were applied to building a computational modeling environment — Amazonia — which supports large scale hydrologic research. Finally, the work in Ref. 39 concentrates on build- <sup>w</sup> <sup>x</sup> ing an object-oriented modelbase for environmental systems. This allows flexible model construction and enhances the possibility of smooth modelbase expansion.

WOODSS, though based on the same premises as Refs. 17,39,44 i.e., considering model definition<sup>w</sup> <sup>x</sup> Ž and documentation as central to a spatial DSS., generalizes them by the following.

<sup>Ø</sup> It is not restricted to users who understand mathematical models or a specific GIS program-Ž ming language , but also directed towards managers,. planners and environmental scientists.

<sup>Ø</sup> Its use of scientific workflows unifies activities of model specification and execution. Indeed, due to their nature, workflows act both as a documentation media similar to the R-structures in Ref. 44 and as Ž <sup>w</sup> <sup>x</sup>. executable entities as in the models in Ref. 39 .Ž <sup>w</sup> <sup>x</sup>.

<sup>Ø</sup> Rather than demanding that users always specify a model, it allows the construction of the model by capturing user interactionswith a GIS. Thus, it can both be used in a spatial DSS sense when Ž pre-existing models are selected for execution as. well as a model construction tool as in Ref. 39 .Ž <sup>w</sup> <sup>x</sup>.

<sup>Ø</sup> Unlike all other approaches, it is integrated within a GIS context. Therefore, users can simulate their models directly on the GIS.

Furthermore, WOODSS is loosely coupled to the GIS via the Monitor module. Thus, it can be used in other GIS environments, contingent on coding the interface between the GIS and the Monitor module.

## 7. Concluding remarks

This paper presented WOODSS — an SDSS for an EMIS, whose goal is to help experts in the environmental area to solve their decision problems. WOODSS is centered on dynamically monitoring user activities in a GIS and documenting them using scientific workflows.

Besides documenting decision processes on the fly, these workflows also constitute a means of progressively enriching the modelbase. They can be used to guide experts in solving analogous problems, or as partial solutions to a bigger problem, allowing a global view of the current state of a decision process, and helping to justify decisions. This is especially important in environmental planning, which involves a large volume of activities and data, and where decision making is primordially multi-participant.

WOODSS was tested with real environmental data and applications for agri-environmental planning, for the state of Sao Paulo, Brazil. More specifically, it˜ was used in constructing alternatives for implementing a soil erosion model, in a study of land suitability for sugar cane plantations superficially described inŽ Section 5 and in delimitation of conservation areas. for sustainable agriculture. Some of the users involved in these applications did not know how to use the GIS, but adapted easily to the workflow representation.

Among the basic characteristics that DSS should satisfy, and which are contemplated by WOODSS, we can cite:

<sup>Ø</sup> To help users who have different kinds of knowledge and expertise.

<sup>Ø</sup> To adapt to changes in computational environment and decision styles.

<sup>Ø</sup> To offer an interactive user-friendly interface.

<sup>Ø</sup> To support non linear executions, allowing users to give up or re-consider solution scenarios.

<sup>Ø</sup> To facilitate the dynamic addition of new knowledge obtained from previous expertise.

<sup>Ø</sup> To document decision and decision processes to justify decisions or re-use them in other processes.

Ongoing work involves extensions to the implementation and extensions to the architecture of WOODSS. From an implementation point of view, extensions being explored involve building a Monitor module for another GIS and generalizing the WorkflowBase to accommodate dynamic constraints. The WorkflowBase must also be ported to a more sophisticated DBMS, in order to handle large data sets.

From a theoretical point of view, the notion of metadata must be extended to accommodate geographic metadata standards e.g., Ref. 19 and en-Ž <sup>w</sup> <sup>x</sup>. hance metadata indexing. Another important issue will be analyzing the use of WOODSS in other spatial decision support contexts e.g., utility managementŽ or transportation . A possible extension would be to . add an intelligent learning module to the monitor, to help detect work patterns and identifying, from user interactions with the GIS, already stored workflows. This will be approached using case-based reasoning.

## Acknowledgements

This work was developed within the SAI project — Advanced Information Systems — of PRONEX II-MCT, with financial support from CNPQ GEO- Ž

TEC project in PROTEM-CC and FAPESP. The. authors thank the anonymous reviewers for their insightful comments and suggestions.

## References

<sup>w</sup> <sup>x</sup> 1 D. Abel, S. Yap, R. Ackland, M. Cameron, D. Smith, G. Walker, Environmental decision support system project: an exploration of alternative architectures for geographical information systems, Int. J. Geogr. Inf. Syst. 6 3 1992Ž . Ž . 193–204.

<sup>w</sup> <sup>x</sup> 2 A. Ailamaki, Y. Ioannidis, M. Livny, Scientific workflow management by database management, in: Proc. 10th IEEE International Conference on Scientific and Statistical Database Management, 1998, pp. 190–201.

<sup>w</sup> <sup>x</sup> 3 M. Alavi, H. Napier, An Experiment in Applying the Adaptive Design Approach to DSS Development, Chap. 5, 2nd edn., 1989, pp. 82–92.

<sup>w</sup> <sup>x</sup> 4 G. Alonso, C. Hagen, Geo-Opera: workflow concepts for spatial processes, in: Proc. Intl. Symp. Spatial Databases — SSD, 1997, pp. 238–257.

<sup>w</sup> <sup>x</sup> 5 M. Armstrong, P. Densham, Towards the development of a conceptual framework for GIS-based collaborative spatial decision making, in: Proc. 3rd ACM International Workshop in GIS, 1994, pp. 4–8.

<sup>w</sup> <sup>x</sup> 6 J. Carter, Fundamentals of geographic information systems: a compendium, Chapter on Defining the Geographic Information System, American Society for Photogrammetry and Remote Sensing, 1989, pp. 3–8.

<sup>w</sup> <sup>x</sup> 7 S. Carver, I. Heywood, S. Cornelius, D. Sear, Evaluating field-based GIS for environmental characterization, modelling and decision support, Int. J. Geogr. Inf. Syst. 9 4Ž . Ž . 1995 475–486.

<sup>w</sup> <sup>x</sup> 8 Workflow Management Coalition, Terminology and glossary, Technical Report WFMC-TC-1011, Workflow Management Coalition, June 1996.

<sup>w</sup> <sup>x</sup> 9 M. Crossland, B. Wynne, W. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14 1995 219–235.Ž .

<sup>w</sup> <sup>x</sup> 10 P. Densham, Geographical Information Systems, Vol. I, Chapter Spatial Decision Support Systems, Wiley, 1991, pp. 403–411.

<sup>w</sup> <sup>x</sup> 11 P.J. Densham, M.F. Goodchild, Research initiative six, spatial decision support systems, Scientific Report for the Specialist Meeting, Technical Report 90-5, NCGIA National Center for Geographic Information and Analysis, March 1990.

<sup>w</sup> <sup>x</sup> 12 Y. Ding, A. Baveja, R. Batta, Implementing Larson and Sadiq’s location model in a geographic information system, Comput. Ops Res. 21 4 1994 447–454.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 M. Eanache, GIS-ready decision support system, in: Proc. Intl. Conference Urban and Regional Information Association, 1994, pp. 206–218.

<sup>w</sup> <sup>x</sup> 14 J.R. Eastman, IDRISI for Windows, Tutorial Exercises, January 1997.

<sup>w</sup> <sup>x</sup> 15 F. Geraghty, Environmental assessment and the application of expert systems: an overview, J. Environ. Manage. 39 Ž . 1993 27–38.

<sup>w</sup> <sup>x</sup> 16 M. Goodchild, B. Parks, L. Steyaert Eds. , EnvironmentalŽ . Modelling with GIS, Oxford Univ. Press, 1993.

<sup>w</sup> <sup>x</sup> 17 G. Guariso, M. Hitz, H. Werthner, An integrated simulation and optimization modeling environment for decision support, Decision Support Systems 16 1996 103–117.Ž .

<sup>w</sup> <sup>x</sup> 18 O. Gunther, Environmental Information Systems, Springer-Verlag, 1998.

<sup>w</sup> <sup>x</sup> 19 O. Gunther, A. Voisard, Metadata in geographic and environmental data management, in: W. Klas, A. Shet Eds. , Man-Ž . aging Multimedia Data: Using Metadata to Integrate and Apply Digital Data, McGraw-Hill, 1998.

<sup>w</sup> <sup>x</sup> 20 I. Heywood, J. Oliver, S. Tomlinson, Building and exploratory multi-criteria modelling environment for spatial decision support, in: Proc. of the Fifth European Conference and Exhibition on Geographic Information Systems, EGIS ’94, Vol. 1, 1994, pp. 632–641.

<sup>w</sup> <sup>x</sup> 21 J.T. Hogue, A Framework for the Examination of Management Involvement in Decision Support Systems, Chap. 3, 2nd edn., 1989, pp. 49–56.

<sup>w</sup> <sup>x</sup> 22 H. Watson, R. Sprague Jr., The Components of an Architecture for DSS, Chap. 7, 2nd edn., 1989, pp. 107–117.

<sup>w</sup> <sup>x</sup> 23 J. Toledano, J. Eastman, P. Kyem, W. Jin, GIS and Decision Making, Vol. 4 of Explorations in Geographic Information Systems Technology, United Nations Institute for Training and Research, 1993.

<sup>w</sup> <sup>x</sup> 24 P. Jankowski, Integrating geographical information systems and multiple criteria decision making methods, Int. J. Geogr. Inf. Syst. 9 3 1995 251–273.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 P. Jankowski, T. Nyerges, A. Smith, T. Moore, E. Horvath, Spatial group choice: a SDSS tool for collaborative spatial decision-making, Int. J. Geogr. Inf. Syst. 11 6 1997Ž . Ž . 577–602.

<sup>w</sup> <sup>x</sup> 26 N. Karacapilidis, D. Papadias, T. Gordon, H. Voss, Collaborative environmental planning with GeoMed, Eur. J. Oper. Res. 102 2 1997 335–346.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 P. Keenan, Using a GIS as a DSS generator, White Paper MIS95-9, University College, Dublin, 1996.

<sup>w</sup> <sup>x</sup> 28 P. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems 22 1998 65–71.Ž .

<sup>w</sup> <sup>x</sup> 29 A. Laaribi, J.J. Chevallier, J.M. Martel, A spatial decision aid: a multi-criterion evaluation approach, Document de Travail 96-45, L’Universite Laval, 1996.´

<sup>w</sup> <sup>x</sup> 30 J. Malczewski, A GIS-based approach to multiple criteria group decision-making, Int. J. Geogr. Inf. Syst. 10 8 1996 Ž . Ž . 955–971.

<sup>w</sup> <sup>x</sup> 31 S. Mann, Spatial process modelling for regional environmental decision making, in: Proc. 8th Annual Colloquium of Systems Information Research Centre, New Zealand, 1996, pp. 126–135.

<sup>w</sup> <sup>x</sup> 32 C.B. Medeiros, G. Vossen, M. Weske, GEO-WASA — combining GIS technology and workflow management, in: Proc. of the 7th Israeli Conference on Computer-Based Systems and Software Engineering, 1996, pp. 122–139.

<sup>w</sup> <sup>x</sup> 33 J. Meidanis, G. Vossen, M. Weske, Using workflow management in DNA sequencing, in: Proc. 1st IFCIS Conference on Cooperative Information Systems, 1996.

<sup>w</sup> <sup>x</sup> 34 S. Mittra, Decision Support Systems: Tools and Techniques, Wiley, 1986.

<sup>w</sup> <sup>x</sup> 35 I. Moreira, Environmental monitoring, Chapter Origin and Synthesis of the Main Methods of Environmental Impact Risk Assessment, PIAB, 1992 In Portuguese .Ž .

<sup>w</sup> <sup>x</sup> 36 O. Nielsen, Using GIS in Denmark for traffic planning and decision support, J. Adv. Transp. 29 3 1996 335–354.Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 F. Pires, An automated environment for modelling geographic applications, PhD thesis, IC-UNICAMP, December 1997 In Portuguese .Ž .

<sup>w</sup> <sup>x</sup> 38 R.H. Sprague Jr., H.J. Watson, Decision Support Systems: Putting Theory into Practice, 2nd edn., Prentice-Hall, 1989.

<sup>w</sup> <sup>x</sup>39 A. Rizzoli, J. Richard Davis, D. Abel, Model and data integration end re-use in environmental decision support systems, Decision Support Systems 24 1998 127–144.Ž .

<sup>w</sup> <sup>x</sup> 40 H.O. Rocha, Geoprocessing applications in the evaluation of land agriculture suitability, in: GIS BRASIL 94, Curitiba, Parana, Brasil, October 1994 In Portuguese .Ž .

<sup>w</sup> <sup>x</sup> 41 M. Rusinkiewicz, A. Sheth, Specification and execution of transactional workflows, in: W. Kim Ed. , Modern DatabaseŽ . Systems. The Object Model, Interoperability and Beyond, ACM Press, 1995, pp. 592–620.

<sup>w</sup> <sup>x</sup> 42 L. Seffino, WOODSS — a spatial decision support system based on scientific workflows, Master’s thesis, UNICAMP, July 1998 In Portuguese .Ž .

<sup>w</sup> <sup>x</sup> 43 M. Singh, M. Vouk, Scientific computing meets transactional workflows, in: NSF Workshop on Workflow and Process Automation Information Systems, 1996.

<sup>w</sup> <sup>x</sup> 44 T. Smith, J. Su, A. El Abbadi, D. Agrawal, G. Alonso, A. Saran, Computational modeling systems, Inf. Syst. 20 2Ž . Ž . 1995 127–153.

<sup>w</sup> <sup>x</sup> 45 R. Sprague, H. Watson Eds. , Decision Support Systems — Ž . Putting Theory into Practice, 2nd edn., Prentice-Hall, Englewood Cliffs, NJ, 1989.

<sup>w</sup> <sup>x</sup> 46 A. Stassopoulou, M. Petrou, J. Kittler, Fusion of Information and reasoning in a GIS-based decision making system using a Pearl Bayes Network, in: Proc. 3rd ACM International Workshop in GIS, 1994, pp. 128–135.

<sup>w</sup> <sup>x</sup> 47 I. Mendes, V. Maniezzo, M. Paruccini, Decision support for siting problems, Decision Support Systems 23 1998 273–Ž . 284.

<sup>w</sup> <sup>x</sup>48 J. Wainer, M. Weske, G. Vossen, C.B. Medeiros, Scientific workflow systems, in: Proc. of the NSF Workshop on Workflow and Process Automation Information Systems, 1996.

<sup>w</sup> <sup>x</sup> 49 P. Walker, M. Young, Using integrated economic and ecological information to improve government policy, Int. J. Geogr. Inf. Syst. 11 7 1997 619–632.Ž . Ž .

<sup>w</sup> <sup>x</sup> 50 M. Weske, G. Vossen, C.B. Medeiros, F. Pires, Workflow management in geoprocessing applications, in: Proc. 6th ACM International Symposium Geographic Information Systems — ACMGIS98, 1998, pp. 88–93.

![](/api/attachments/ED728FNT/fulltext/images/53db3d209c2c8b368f3dc3767ae4cda213aa27c4d63a3ee46ae5ca05083e2867.jpg)  
Laura A. Sefino did her undergraduate work in Computer Science in Argentina and her MSc degree in Computer Science in UNICAMP, Brazil, in 1988. Her areas of interest are database systems and workflows.

![](/api/attachments/ED728FNT/fulltext/images/26bb864b214c6544aa2401bd2ee984d210cf9d52cca410f3b6869f7686e2bff1.jpg)

Claudia Bauzer Medeiros PhD’85, University of Waterloo, is an associate professor at the Institute of Computing, University of Campinas UNICAMP ,Ž . Brazil. She is the head of the Database Research Group in UNICAMP and is the leader of a major research project on developing GIS tools and techniques for urban and environmental issues. Presently she is the Editor of the Journal of the Brazilian Computer Science Society. Her areas of interest include active databases, integrity control, digital libraries and geographic database systems.

![](/api/attachments/ED728FNT/fulltext/images/4e80ef7ba0902c7b1c91c69622b2ae5198d2b1e32cb9e5df2accb98efc4979d2.jpg)

Jansle V. Rocha, PhD’88 in Remote Sensing, Cranfield Institute of Technology, Silsoe College, England, is an assistant professor at the Faculty of Agricultural Engineering, UNICAMP. He has research and operational experience in land resource surveying for many types of application, including land use planning and simulation and modeling using remote sensing and GIS. He is the head of GEO - Geoprocessing Study Group, a multidisciplinary group of researchers

who work with Remote sensing<sup>r</sup>GIS<sup>r</sup>GPS<sup>r</sup>Precision farming<sup>r</sup> Environmental Planning. His areas of interest are remote sensing, geographic information systems GIS , global positioning systemsŽ . Ž . GPS , precision agriculture and environmental planning.

![](/api/attachments/ED728FNT/fulltext/images/371f507de45da4abbfe1a74a1cddb61fb4b19396818f0f0ced70fb53d0a9e978.jpg)

Bei Yi is an undergraduate student in Computer Engineering, at the University of Campinas, Brazil.
