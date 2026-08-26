---
otero_id: 3756
otero_key: "PDK8YDRM"
title: "TRANS-POL: A mediator between transportation models and decision makers' policies"
authors: "Dimitrios A. Tsamboulas; George K. Mikroudis"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.07.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# TRANS-POL: A mediator between transportation models and decision makers’ policies

Dimitrios A. Tsamboulas <sup>\*</sup>, George K. Mikroudis

Department of Transportation Planning and Engineering, National Technical University of Athens, 5, Iroon Polytechniou Street Zografou Campus, Zografou-Athens, GR-157 73, Greece

Received 29 February 2004; received in revised form 21 June 2005; accepted 8 July 2005 Available online 15 August 2005

## Abstract

TRANS-POL is a Decision Support System (DSS) specifically developed for the transport policy sector, which is capable of presenting the impacts from the implementation of transport policies and projects. It is developed to build intelligent translators between end users’ questions and sophisticated transport model outputs. Hence, it links Expert Systems (ES) and DSS with advanced transportation models so that functionality between them is achieved. TRANS-POL comprises a set of basic tools that facilitate navigation by transport and computer experts and policy makers through all the available system resources (databases, maps, transport models etc.) and complementary tools such as desktop mapping, GIS, database management and multicriteria evaluation for transportation infrastructure projects. TRANS-POL application to example cases has proven its functionality and use. The added value of TRANS-POL is that it provides a medium for bringing together all kinds of transport models and databases, making them available to a wider audience in a user friendly environment. © 2005 E1sevier B V. A11 righ

Keywords: Decision Support System; Expert system; Transportation models; Transportation decision makers; Transport policy

## 1. Introduction

With the progress of computer systems, a new kind of software tools is being developed to facilitate the decision-making process, namely the Decision Support systems (DSS), initially called support systems [9]. They aim at providing the requested information in a user friendly manner, through the application of models and/or the assistance of an expert system that satisfy the needs of the user. In this context, it is always important to remember that a Policy Support System is a kind of Decision Support System (DSS), which comprises a software system, under the direct control of decision makers. It assists them but it does not replace them in decision making. Therefore, the development of such a Decision Support System is addressed to people, and it is not another computerrelated advancement. Although computers and software play an integral role in the DSS world, the study of DSS related to transport policy issues is about how people think and make decisions. The definition and implementation of a DSS must integrate future users as much as possible, since for them, a DSS represents both a challenge and an opportunity to improve their working processes.

The literature on Decision Support Systems is quite rich, providing a sound basis for the methodologies employed and the mathematics involved [6,12]. There are numerous systems covering several disciplines, policy contexts and users’ needs for specific application environments [2,4,19]. The following are good examples of developed tools for policy issues: WATERSHEDSS (WATER, Soil, and Hydro-Environmental Decision Support System), which is designed to help watershed managers and land treatment personnel identify their water quality problems and select appropriate best management practices [18]; the Environmental Decision Support System (EDSS), which assists in solving environmental problems with the provision of an advanced modelling and analysis system for environmental scientists, engineers, policy makers, and educators [7]; the Spatial Decision Support System for Urban/Wild land Interface Fire Hazards, which assists planners and decision makers to better manage and formulate policy that would help reduce the risk of a firestorm [21]; the Integrated Planning Decision Support System (IPDSS), which is designed as a Decision Support System (DSS) to assist governments and communities in evaluation of geological hazards, vulnerability, and risk; in addition, it assists urban planners in organizing, analyzing, modifying, and re-evaluating existing or needed spatial information within land-use planning activities [10]. On the other hand, the development of spatial Decision Support Systems (SDSS) is now possible [4], as well as planning support systems (PSS), and thus, future developments are anticipated in decentralised decision making [13].

The paper presents TRANS-POL, a DSS specifically developed for the transport policy sector, to provide policy support information which can be generated in-house. This gained broad support from consultancy, academia and the European Commission itself. The research effort aims to improve information provision in a highly complex decision-making arena:

complex by its substance, its network of actors and the limited level of information available, despite the research efforts. TRANS-POL is developed as an integral part of the <sup>b</sup>BRIDGES,<sup>Q</sup> a research project funded by the European Commission’s 4th Framework Programme of Research and Development [23]. The final product of BRIDGES is a set of software tools and data formats designed to provide necessary backing for an ETIS (European Transport Policy Information System). ETIS is an information system of integrated policy tools to support policy analysis and policy making. When finalized, it will comprise four elements: a data element; an analytical modelling element; GIS and a final element interfacing users with the above elements [11]. On the other hand, BRIDGES was designed as a set of <sup>b</sup>open,<sup>Q</sup> highly interconnected tools: communication systems, data models and protocols, specialized transport routines, applications to build intelligent user interfaces, transport software routines and stand alone applications. The transformation of such an open <sup>b</sup>information and modelling<sup>Q</sup> system into a <sup>b</sup>Decision Support System<sup>Q</sup> requires intelligent intermediation between the system outputs and the end user requirements, which is to be provided by the elaborated TRANS-POL [22].

To summarize the problem statement: since there are all kinds of models, simple and complex, but rather sophisticated for a non-expert user to understand all their intricacies, the presented DSS provides a set of tools for making those models widely available, yet in a controlled manner. The added value of TRANS-POL is that it provides a medium for bringing together all kinds of transport models and databases, making them available to a wider audience in a user friendly environment.

In the following, the paper presents thoroughly the issues related to TRANS-POL architecture and implementation. Firstly, the TRANS-POL objectives and the areas chosen for the solution of the problem are presented. Then the overall architecture of the TRANS-POL system is explained. Furthermore, the building up of the DSS templates and their connection to data sources, knowledge sources, models and solvers is presented, as well as the contents of the <sup>b</sup>meta<sup>Q</sup> database used to guide the system through execution. Finally, the use of the system is described in an example case. Hence, the added value of the system for users and models’ developers in comparison with other DSS based approaches/models is highlighted.

## 2. Approach

## 2.1. Objectives

The objectives of on-going research in the area is the development of appropriate software modules for tools that will allow a user to formulate questions to any policy driven system, like ETIS, transform them into a series of calls to transport models and databases, and present the end results using either the ETIS Core Interface, or its own routines. TRANS-POL is placed within these research efforts. In addition, it could be used as an independent module. Consequently, special emphasis is placed on the development of direct access to database utilities and GIS mapping functions from within the DSS. Thus, such functions are either called directly when needed from the TRANS-POL code, or they are available as separate tools from the DSS menu (e.g., Visual Basic’s VisData tool for databases, and ESRI MapObject’s DSSview tool for maps).

A key element in the development and use of such policy tools is simplicity and ability to be used by the non computer specialists (e.g., decision makers, administrators, etc.), although it is a complex system. Thus, such systems (like ETIS) should provide the users with tailor-made data outputs and with certain predefined problems/scenarios in order to meet their needs. This is achieved by TRANS-POL, a DSS for making queries and interpreting results. The TRANS-POL menus direct the user requests, which may be concrete, simple, and immediate, such as <sup>b</sup>What are the flows for this specific network segment?<sup>Q</sup> or more abstract and complicated, such as <sup>b</sup>What is the best mode of transport for this specific corridor?<sup>Q</sup> Such requests are transformed into a series of calls to transport models and/or databases.

Note that since there is an infinite variety of models and data that could be used with the policy tools (like ETIS), TRANS-POL provides in an automatic way the tools for making the preparation of such menus and requests. By using the DSS tools, the model developer, who knows all the details of his/ her model, can prepare suitable questions that a nonexpert user may safely ask the model. This is particularly true for complex models, such as those built with VIA [17] and MEPLAN [15]. Typically, they need huge amounts of data (hundreds of Megabytes, or Gigabytes), which reside in various files, they require calling several sub-modules, making assumptions, and knowing which data to select for presentation under specific conditions, etc. The modeler, who knows or could assume with some degree of certainty, what are the valid questions the decision maker might ask, prepares for TRANS-POL a <sup>b</sup>template<sup>Q</sup> (an ASCII file) for each one of the questions. At the next step, he tests them, applying the relevant models, and then submits only the necessary data with the template to the DSS administrator of TRANS-POL. The DSS automatically parses the templates and it generates – based on them – simple menus containing the questions for the novice user. In cases of missing data or logical assumptions concerning the model execution, the modeler may prepare an additional knowledgebase file stating the preconditions for each assumption needed to run a model, or to select a model parameter.

As an example, for a specific question like <sup>b</sup>What are the flows on Spata airport bypass, during the airport construction?<sup>Q</sup> the answer may be obtained just through an SQL statement properly phrased in the template. The modeler knows in which tables the data are located, and under what names, he knows the SQL syntax (or the simpler template syntax), so he can write a template for the question. The DSS parses the template and shows on its menu the much simpler question <sup>b</sup>What are the flows... etc.<sup>Q</sup> When the novice user starts the DSS tool, he may find this, as well as other related questions, grouped under the <sup>b</sup>Spata airport construction<sup>Q</sup> category of models. By selecting the question, TRANS-POL fetches the results and displays them in the appropriate form (e.g., a listing, a graph, a map, etc.), as requested by the user.

## 2.2. DSS Users

From the above presentation, it is evident that three categories of possible DSS users exist:

a. Expert users (modelers, program developers, consultants, etc.) who have sophisticated data and models and want to make them accessible, in a controlled and limited manner to non experts.

b. Novice (non-expert) users that do not necessarily know all the intricacies of each and every model, but they want to ask specific questions within the range covered by one or more models.

c. A DSS administrator, who maintains a base of models, data, templates, knowledge files and other resources which are necessary to support the questions that the DSS can answer. He is indispensable when TRANS-POL is interactive over the Internet.

In the following, when we say <sup>b</sup>user(s),<sup>Q</sup> we collectively mean any one of the above users. Once a set of questions have been properly set up and tested, then a <sup>b</sup>user<sup>Q</sup> may go directly to the <sup>b</sup>Q and A<sup>Q</sup> menu of the DSS, browse through the available questions, select one, provide any additional values that may be needed (e.g., display ranges, desirable colors, etc.) and get the result.

## 3. System architecture

## 3.1. DSS components

Following its objectives, TRANS-POL will facilitate the following options: (1) database utilities for querying, updating, obtaining reports, etc., through an ETIS interface link; (2) comparative answers to users’ questions relating to alternative scenarios/options; (3) establishment of expert rules to estimate missing data; (4) initiation of transport models appropriate for the functionality requested by the user; and (5) evaluation of model results according to multicriteria models (e.g., Should I recommend this corridor vs. another?).

The concept <sup>b</sup>implementation of TRANS-POL<sup>Q</sup> is graphically shown in Fig. 1. A user may directly run/ execute a database method or load a template, parse it and execute it. A database method can be selected also with the help of the provided expert system rule base.

The results are presented directly in charts, or graphs, or viewed through the VisData or DSS view utilities. TRANS-POL is a combination of an objectoriented interface (OOI) and an expert system (ES). Options (1) and (2) can be handled directly by the OOI. Options (3), (4) and (5) can be provided through an expert system module that will <sup>b</sup>know,<sup>Q</sup> depending on the question, which data model to use, how to fill in data gaps and what kinds of results to display to the user. Interaction with the ES is also achieved through the OOI utilities. <sup>b</sup>Knowing<sup>Q</sup> means that a knowledgeable person has prepared in advance the necessary template or knowledge-base files and has provided the corresponding data, so that the template(s) can be parsed and executed correctly. The facilities offered by the DSS to support the above options are explained in the following.

![](/api/attachments/PDK8YDRM/fulltext/images/0ae9bc56e69d4cbb96aa7afac9a11ecf9d986be3d1adfb168244afe526105169.jpg)  
Fig. 1. Concept implementation of TRANS-POL.

## 3.2. The object-oriented interface (OOI)

The TRANS-POL provides an object-oriented interface for communicating with its users. The OOI comprises a set of menus, forms, dialog boxes, etc., which are either preset or generated during the execution of the program to facilitate the user dialogs. The preset part of the OOI guides the user through the standard options of calling a DSS module (data dictionary, template parser, expert system, etc.), or a utility (VisData, DSSview, etc.).

On the other hand, certain parts of the OOI are generated based on the information contained in the templates and knowledge-base files available during DSS execution. It comprises menus, list boxes, input boxes, maps, graphs, etc. that are generated either in order to prompt the user or to display the answers to user questions. Essentially, the DSS provides a shell for generating this part of the OOI. The expert user prepares templates which define the questions to be included in the OOI as well as the answers to be displayed. Thus, the run-time OOI of the DSS is actually <sup>b</sup>developed<sup>Q</sup> by the expert users that prepare and test their templates and then make them available, through the DSS to the novice users (to be referred as <sup>b</sup>users<sup>Q</sup>).

For a given model to be included in the TRANS-POL, the OOI development work starts by defining: What kinds of questions a user may ask; What kinds of problems are to be solved; What kind of information are accessible; Which models are used; Which databases are accessed; Which application programs are interfaced.

The starting point is the existing DSS interface with the sample models, data, maps, etc., which TRANS-POL already contains. However, using the DSS facilities, an expert user can extend this interface so that it can be connected to distributed databases, diverse software models, and even commercial packages. This follows an object-oriented approach, and, at this point, it has been programmed in the DSS using the ActiveX technology available through Visual Basic [14], Access [8], MapObjects [5] and Amzi Prolog [1].

At the user level, there is an effort to keep these implementation details of the DSS, invisible as much as possible. All systems peripheral to it are made accessible through this single interface in a uniform and simple manner. For this reason, two important utilities are included in the TRANS-POL:

a. The VisData program, which provides most of the MS Access functionality to the DSS users, without any royalties or additional costs. This way DSS users can examine and update all kinds of database files (Access, dBase, Excel, etc.) as well as files needed to run the DSS models.

b. The DSSview program, which is a simple GIS application using ESRI’s MapObjects. It also provides DSS users with basic GIS functions for viewing various kinds of GIS files (ARC/INFO, MapInfo, shapefiles, bitmaps, etc.), as well as basic editing and shapefile creation capabilities, free of charge.

In the future, additional utilities can be included, if needed, without any programming, just by modifying the DSS initialization (DSS.INI) file. A critical aspect of the approach is related to its ability to interconnect with various databases, models, etc. This becomes very complex in terms of knowing what to do and why. The user should not need to know what all the various databases and models are, but only what kind of questions the system can answer. Therefore, the OOI of the DSS was designed to comprise two layers: (i) a higher, user-oriented layer; and (ii) a lower, application-specific layer.

The user-oriented layer is the one which is visible to the user. The application-specific layer is not directly visible to the user, but it comprises the tools that make models, databases, GIS utilities, etc., available to the end user. The user layer of the objectoriented interface enables the user to supply the necessary information for the problem at hand and also allows the DSS to present the user with the available information, the problem formulation and the results. TRANS-POL, through the use of hierarchical menus, boxes with grouped input, standard models, etc. guides the user through a line of questions such as:

<sup>!</sup> Do you want specific flow/socio-economic/ landuse data?

<sup>!</sup> Do you want to run a specific transport model?

<sup>!</sup> What is the geographic area are that you want to evaluate?

<sup>!</sup> Which are the transport modes you want to use?

<sup>!</sup> Do you want to evaluate a single mode or multiple modes?

<sup>!</sup> Which socio-economic indicators do you want to use?

<sup>!</sup> Which land-use parameters do you want to consider?

<sup>!</sup> Set of questions for selected, often encountered scenarios/problems, such as evaluation of a combined transport corridor; planning of a transport project in a region covering more than one country; planning of a transport project in a specific country; local and regional views of trans-national networks; transport infrastructure for a selected region; demand-oriented indicators (flows, modal shares, etc.); supply-oriented indicators (density of infrastructures, etc.); infrastructure evolution in European Union countries; traffic flows for passengers and freight for a given area; socio-economic variables for a given area.

These are examples from an infinite number of questions that can be prepared through the DSS templates and knowledge-base files and presented in the above simple manner to the user, through the user layer of the OOI. The system applies the user choices in the above set of questions/options to build a formulation of the problem, select appropriate databases, query certain data from a given database, select the appropriate transport model and prepare the necessary input data set for running the model(s). Also, the DSS through the OOI may obtain from the user additional information on his/her preferences in order to derive the appropriate indicators and present the results in the most suitable format, e.g., which color, on what map, with graphs, charts, tables, etc.

The user may have the option to supply to TRANS-POL information on problem parameters, e.g., transport mode and network alternatives. Alternatively, the system may find/propose default values for a specific problem parameter, e.g., transport, socio-economic, land-use, etc. The user interface is menu/form driven. All model or standard query related information is grouped under a single menu path along with the necessary selection and data input boxes, command buttons, etc. Thus, the OOI serves as a graphical and textual tool for query input and result output. It is based on menus, browsers and graphers for result curves and so on, supplemented by a graphical interface for presentation of geographical data.

Furthermore, geographic interaction allows for (i) searching by graphic zooming and scrolling, feature identification, feature rendering, selection of areas and network elements by pointing at their graphic presentation, and (ii) results presentation by highlighting, etc. The above can be achieved by the MapObject’s geographic information system capabilities, which are embedded in the TRANS-POL.

## 3.3. Expert system (ES)

The main task of the expert system (ES) is to analyze user queries, decompose them into subqueries to pass to other modules, and combine results into a meaningful form for the user to understand. In doing so, the ES may apply default values, assumptions and rules to fill in any missing data required for running other modules.

The ES is a part of TRANS-POL and, thus, is accessible through the DSS interface. The user can formulate queries through the use of menus, displays, etc. of the TRANS-POL system, which is passed on to the ES for processing with full transparency. Since it is a part of the DSS, the ES uses directly the OOI modules, mentioned previously, and the template parser, or the Query processor, explained in the following. This modular approach allows using one or more modules when necessary, such as:

1. A template parser that interprets user queries (specified by means of the OOI). This is the same DSS module mentioned previously, which parses a template file.

2. A Query processor that executes SQL queries. It also calls the appropriate modules (e.g., DSS core, transport model, database) and/or inspects the corresponding parts of the ES’ knowledge-base.

3. An ES shell that applies rules in order to determine which modules to use under what conditions or to apply realistic assumptions for missing data. The ES shell processes rule files (or knowledge-base files). A rule file is an ASCII file containing simple rules to process the models.

4. A multicriteria evaluator that combines results from diverse sources (as the above) to be used in a multicriteria model.

These are TRANS-POL modules that can be called separately, or in combination to each other. Thus, the first two modules are called during template parsing and execution. The ES shell module is used specifically for processing rule files. The main module is the Query processor, which allows the user to form queries for the Query Manager subsystems. Its main task is to analyze and decompose user queries into subqueries and to pass the subqueries to other modules. Additionally, it is able to answer some kinds of queries, in particular those focusing on items already stored in the ETIS database, or that can be deduced by means of default values or current assumptions of the user. Before passing information to other modules, the Query Manager checks the consistency of data and results, keeps track of current assumptions of the user, and applies rules that may provide realistic assumptions for missing data.

TRANS-POL, when compared with other no model-based DSSs, exhibits a functionality that depends completely on the availability of models and data. If there are no data, there is nothing to process, and if there are no models, there is nothing intelligent for the DSS to do. For such cases, TRANS-

POL is applied using either simulated data, or sample sets of data from existing models.

## 3.4. Implementation details

The TRANS-POL Core Engine is a Windows Menu-driven Application, written in Visual Basic 5.0. The back-end database is ACCESS and the linking library is DAO 3.5. TRANS-POL Core Engine is also a Shell where independent programs–utilities have been incorporated. The DSS Administrators have the possibility of adding further independent programs into this Shell in future applications. On the other hand, the modelers can have a copy of TRANS-POL and test their model templates. So TRANS-POL can serve as a workbench for modelers where they can try many variations of methods just by writing a simple template file. This is much simpler than programming the execution sequence of those methods independently.

The ES modules (1), (2) and (4) have been developed in Visual Basic and the ES shell module (3) has been developed in Prolog, whereas all its screen I/O is passed to Visual Basic and handled by the DSS’ interface. All access to the above DSS/ES functionality is provided through the object-oriented interface (OOI) described previously. The end users (mainly non-experts) could use TRANS-POL and enjoy a rich set of Tools and Utilities all presented through a friendly user interface. They can put a question to the expert system, search for a specific method using keywords, browse database tables, and examine results in a digital map. Fig. 2 provides a graphical presentation of the DSS tool and its interactions with the other tools.

![](/api/attachments/PDK8YDRM/fulltext/images/cd7762054dc2b871e3b22541c12c41fcc6116740fe2a6a64282f49f11f40bf15.jpg)  
Fig. 2. DSS tool and external modules.

## 4. Transport models and their templates

## 4.1. Initiation of transportation models

While transport models exist in all varieties, simple and complex, they mostly require large amounts of data and sufficient time for their preparation, calibration, testing, running, and presentation of results. Once they are set up, considerable expertise is required to understand what they really do, and what answers they can safely provide to a user, who is not familiar with them.

However, in order to be useful to the users’ community outside the model developers’ group, models need customisation and careful design to control what the inexperienced user may do with them. TRANS-POL provides a solution to the above problem of model integration and results dissemination. By writing a set of templates, the modeler can control what kind of questions a user may safely ask using the tool. Also by providing the subset of data the modeler wants to distribute (ASCII files, database tables, maps etc.), he can provide a useful package for information retrieval and processing that can be highly valuable for administrators or other interested parties. This purpose is achieved in TRANS-POL in two ways: (i) preparation of templates, one for each type of function that the modeler wants to make available to end users; (ii) generation by the TRANS-POL of a Query path, after parsing templates, registered in the TRANS-POL database.

The process of template preparation involves the following steps: (1) selection of a data set (ASCII files, database files, GIS files) to be used along with the template; (2) writing the templates. For each question that a user might ask the model, a different method is written. Methods can be organised in one or more template files. Also, they are grouped for easier classification of menus and retrieval into the following clusters:

1) Testing–debugging each method. Using the TRANS-POL, the modeler can run each method separately and check whether it produces the desired results.

2) Submitting the templates to the TRANS-POL end user, or to a central TRANS-POL administrator. The TRANS-POL has the option of applying a password to restrict template use and of locking the template source file from unauthorised use, or tampering by non-expert users.

Once a template is available to the end user, all its methods appear as entries in a list table, where the user may select which methods to register for further use. When a method is registered, it is also placed automatically in a set of hierarchical menus that guide users through its execution. From then on, a user may just browse through these menus, select a method, specify further parameters that the method may need, provide display options, and view the results. This sequence of menu selections guides the user through the valid options to final completion of his request. Each path on the menu hierarchy constitutes a Query path, which is available to all TRANS-POL users.

Additionally, a modeler may prepare a rule file, which contains rules for selection of models under a set of conditions, for filling data gaps, for conditional execution of program files and other options. Each rule file is considered to be a knowledge-base of the ES shell. It is an ASCII file that contains a set of rules written in an <sup>b</sup>IF conditions THEN action<sup>Q</sup> format. It is checked–tested–debugged by the modeler in a similar manner to the template file. The result of processing the rule file is that the TRANS-POL may ask the user additional questions as these are encountered in the knowledge-base rules.

The implementation of <sup>b</sup>initiating transportation models<sup>Q</sup> in the TRANS-POL is as follows: (i) the OOI application layer handles the template and rule files; (ii) the OOI user layer generates and processes the Query paths; (iii) the TRANS-POL modules (template parser–Query processor–ES shell) are executed in sequence; (iv) depending on the output of each module the corresponding TRANS-POL (Core–Model–Database–Application) Manager system is called; finally, (v) the user may provide a Data Dictionary (DD) for all the parameters used in the above template and rule files. The DD is an access database file that contains the hierarchies, names, definitions, units, default values etc. of all the parameters of the model.

As a last remark, there is no limit on the classes of transportation models which are considered and can be used by TRANS-POL. Actually, there is no reason why the models under consideration have to be transportation models. The whole approach presented is generic and, although initially developed and tested within the transport framework, it is applicable to any type of policy decision making supported by models and data.

## 4.2. Templates

A template is an ASCII file that contains a model’s methods submitted by the modeler. Each method consists of reserved keywords that the TRANS-POL engine tries to parse, analyze and store. It guides the TRANS-POL engine on how to execute a specific method and act on the model’s data. Templates are a well-known solution that has been adopted by many commercial applications such as MS Word and MS Excel. The basic idea of a template is an ASCII file with commands, arguments and possibly some data. It is not a substitute for Macros or a Scripting language or a data file, it just <sup>b</sup>drives<sup>Q</sup> the application providing definitions and orders. The purpose of templates is to give the modelers a tool that allows them to make some of their model’s functions available to outside users in a controlled, yet user friendly manner.

As we have already mentioned, the modeler cannot normally submit the model itself, but just a set of data output results. TRANS-POL can further process the data in order to produce answers to certain specific questions anticipated to be posed by the users. But how can TRANS-POL act on those data? What rules and restrictions must TRANS-POL follow? If the modeler is always present, he/she would apply his/ her computer knowledge to produce good results. Unfortunately, this is not the usual case. The nonexpert user requires guidance. TRANS-POL includes a <sup>b</sup>driver<sup>Q</sup> that will guide him/her on how to act on those data. This <sup>b</sup>driver<sup>Q</sup> is the template. The modeler may also submit some independent programs along with a data set. Again it is necessary to know how to <sup>b</sup>call<sup>Q</sup> those programs in order to activate the model. Once more, such a <sup>b</sup>driver<sup>Q</sup> is again the template.

The template, as an ASCII file, can be written using any editor or word processor that supports the ASCII format. Because the file is in ASCII format, it can be exchanged between heterogeneous operating systems like Windows NT, UNIX, VAX VMS etc. without the intervention of any filter. This ASCII file will be read by the TRANS-POL application and parsed line by line. Each template file consists of one module and one or many methods. The module can represent an entire model and a method includes a procedure or function of a model. The TRANS-POL application could support many modules in one template, but this is not advisable for reasons of clarity. Each method consists of a set of predefined keywords and the associated arguments.

![](/api/attachments/PDK8YDRM/fulltext/images/0682e2b6c421ced3b14c1325ce3603824f4d2698efbf345c35257d1cb6834b47.jpg)  
Fig. 3. Template structure.

The template file follows a specific structure, as depicted in Fig. 3, and the logic in Fig. 4.

In a template, only a predefined set of keywords can be accepted and some of them in a specific order. For each keyword, there is the pair:

which denote that all the lines between them belong to the same keyword.

Templates support comments (’) and can contain many methods.

## 5. The <sup>b</sup>meta data base<sup>Q</sup> guiding the DSS execution

TRANS-POL is guided through execution of models, retrieval of data or presentation of results by a <sup>b</sup>meta<sup>Q</sup> database comprising rules, data, and a multicriteria evaluator. Expert rules are handled by the ES engine; data queries are handled by the database engine; multicriteria are entered and manipulated by a specialized database application.

## 5.1. Expert rules for missing data

Modelers, in certain cases, can make assumptions for missing data or provide alternate ways for estimating parameter values. TRANS-POL makes allowance for such options through its rule-based expert system shell. A modeler can write simple rules for missing data, conditional model execution and other items. At the next step, the DSS will process the rule (ASCII) file, prompting the user for selections and guiding him through the modeler’s logic. The objective for the DSS is to facilitate establishment of expert rules to estimate missing data. Thus, TRANS-POL provides a tool that facilitates estab-

Begin Keyword End Keyword

![](/api/attachments/PDK8YDRM/fulltext/images/d8bb8f002440378b83097fe7c2a50716baa81b9790b114278f80e1c86c09404d.jpg)  
Fig. 4. Template logic.

lishment and processing of expert rules. This is achieved through the well-known technique of rulebased (or knowledge-base) expert system shells. The modeler can write a set of logical or empirical rules that define constraints for model execution, parameter selection, etc., and the ES shell processes the rule file following first-order predicate logic. The rules are written in an ASCII file following a simple sentence-like format:

## IF<sup>b</sup>condition1<sup>N</sup>AND. . .<sup>b</sup>conditionN<sup>N</sup> THEN<sup>b</sup>action<sup>N</sup>

The author of the rule base can thus describe an infinite number of conditions for each possible action as clauses in the IF-part of the rules. In turn, each condition specified in the THEN-part of the rules can serve as a condition to other rules, and so on. This creates logical dependencies between the authordefined parameters. When parsing the rule base, the ES follows the reasoning of the IF-THEN clauses. Additional keywords in this file (ASKABLE, MENUASKABLE, etc.) specify which of the author-supplied names are keywords that a value needs to be supplied by the end user. This will constitute the reasoning to proceed. To accomplish it, TRANS-POL contains an ES shell developed in Amzi! Prolog, to handle the models’ rule bases.

## 5.2. Comparative answers to user queries

In most cases, a user may want to examine alternative scenarios and compare options in order to make a decision. TRANS-POL provides such facilities by displaying the results of queries back to the user, in a variety of forms (tables, graphs, charts, maps). Fig. 5 presents the template for a query and Fig. 6 the output, as generated by the tool.

## 5.3. Multicriteria evaluation (MCA)

There are several occasions that a user wants to make an evaluation of alternative options using a multicriteria model. TRANS-POL provides such a multicriteria evaluation module that allows a user to specify criteria, weights, and values and let the DSS perform the ranking/ presentations of his options. This is presented to demonstrate the capabilities of TRANS-POL of allowing a specific model (like the MCA) to be embedded.

![](/api/attachments/PDK8YDRM/fulltext/images/ba10db476b3b75b5c373d8102b8af9958d737feef2156663132b293a5a75cb66.jpg)

![](/api/attachments/PDK8YDRM/fulltext/images/4f71d826dbe98027f8af8e0c8c5b99a384666bfd2004be3d95f582462bcf5a50.jpg)  
Fig. 5. Templates for queries.

The objective here for the DSS is to facilitate evaluation of model results according to multicriteria models (e.g., should I recommend this road to be build this way?). The various multicriteria (MCA) assessment methods in general follow a certain methodological framework, consisting of four steps [3,20,24]:

1. Objectives—definition of basic problem and/or objective(s)

2. Criteria—description of the problem parameters and their corresponding index functions (indicators, cost functions, etc.)

3. Structure—definition of how the criteria are related and weighed to each other in the problem

4. Evaluation and ranking—definition of how to use the criteria and structure to meet the objectives

In a given decision situation, alternative projects can be evaluated following the above steps of the method and by receiving <sup>b</sup>values<sup>Q</sup> or <sup>b</sup>scores<sup>Q</sup> corresponding to the criteria employed by the method.

![](/api/attachments/PDK8YDRM/fulltext/images/9e4cda228bd19e1687ecd77db99ba91866d6bc55013a44ae0e280694889c0b31.jpg)  
Fig. 6. Output for comparative answers.

Dynamic effects can be treated by using scenarios at different time horizons. All values can be considered <sup>b</sup>frozen<sup>Q</sup> at the given time horizon where evaluation and comparison of projects take place. Fig. 7 presents a template where the criteria are listed, for which values have to be inserted.

![](/api/attachments/PDK8YDRM/fulltext/images/71806f82aa475c5192bfc2f132f61b029415d9fec3e5a164df08211bd120b455.jpg)  
Fig. 7. Multicriteria (MCA) application template.

A specific module has been constructed in TRANS-POL for MCA evaluation. It is an implementation of the above methodology in Visual Basic and Access, as described in the following. All the necessary elements of the methodology are kept in access tables for easy updating. The tables abide by the normalization rules of databases to facilitate the relational manipulation of each element. The MCA Tool evaluates the performance of various alternative scenarios (options), according to their performance score for the selected criteria, to which a specific importance value (weight) is assigned. Fig. 8 presents such an output.

The tool has been implemented with Microsoft Access using master tables, transaction tables and a combined dynamic queries. The user must supply most of the fields of those tables with initial values. For this purpose, a sequence of forms has been implemented and each one of them loads the next one and remembers which form was the previous one. With this process, the user is guided, through the tables, to supply initial values in the right order. This is very important because dynamic queries demand that certain tables be filled with data before they can carry on a calculation and proceed to the next logical step. The user is forced to choose values from Combo boxes in a clear and descriptive way, as each value is linked with a label that appears in the Combo box.

When calling the MCA utility, the user may either select from a predefined set of criteria–weights– values, which he may modify, or define his own set from the scratch. Once the MCA database of the above tables is completed, the user may select to run it. Then the system starts, completes the scoring of alternatives, and presents the results in tabular or graphical form.

## 6. Example cases of TRANS-POL

To demonstrate the use of the DSS tool and its components, several example cases are used. The first

![](/api/attachments/PDK8YDRM/fulltext/images/0d83fcec07fd86814756e0c0bf8bf746f90f6a36c64ec98fd3677bcb823c2f2d.jpg)  
Fig. 8. Multicriteria application output.

![](/api/attachments/PDK8YDRM/fulltext/images/32d3a0b28b0aa6808420de1944c0dac7434981291d577707626ec37aaf603a6b.jpg)  
Fig. 9. Sequential steps for DSS tool application.

group of example cases demonstrates the use of DSS templates and the overall functionality of the system. It is based on a study of transport-related impacts from the new Athens International Airport in Spata [16]. For reasons of confidentiality, data used are somewhat altered from the original values.

Two example queries are shown: One for air pollution levels in cities of the Messogia area surrounding the airport, and another for noise levels in neighboring cities.

For the queries related to air pollution, data are stored in an access database <sup>b</sup>SpataAirport.mdb<sup>Q</sup> and in several shapefiles that include both maps and data related to Spata airport. The sequential steps for the creation of templates and query results are presented in Fig. 9. Fig. 10 presents sample screen outputs regarding the air pollution levels.

The second example case is related to the expert system application, referring to Spata airport construction. It demonstrates some sample code for the expert system function of the DSS. The expert system decides about the use of a suitable model for air pollution assessment during the Spata airport construction, depending on the queries:

![](/api/attachments/PDK8YDRM/fulltext/images/7a0dfe647f4532fd450b616bcf52af19ce46bc0a7e4c4f7c13fd255bdb3d08b6.jpg)  
Fig. 10. Air pollution levels graphical outputs.

<sup>!</sup> the <sup>b</sup>Copert<sup>Q</sup> model for calculating road traffic emissions, and

<sup>!</sup> the <sup>b</sup>Hiway<sup>Q</sup> model for estimating air pollutant concentrations

Additionally, the sample code contains an example of how the system decides between examining available data and initiating a model run. In this example, the expert system presents a choice to the user to <sup>b</sup>recalculate<sup>Q</sup> or to use <sup>b</sup>calculated<sup>Q</sup> values, before applying the <sup>b</sup>Hiway<sup>Q</sup> model, which was chosen. Fig. 11 presents these outputs.

The third example case is related to the MCA application of TRANS-POL. To illustrate this, an evaluation problem has been examined, namely, transportation of construction materials through three different options: either through Spata (from Athens area), or through Markopoulo (from local quarries), or through Loutsa (from distant areas coming to Rafina port by lorries). The heavy truck traffic will create impacts to the natural environment and nuisance to inhabitants of those areas. The impacts will be both short-term and long-term, the first ones being the most important. Five criteria have been defined: Landscape, Air, Noise, Traffic, Accidents. The process of setting up and running the MCA function of

![](/api/attachments/PDK8YDRM/fulltext/images/2c306f892efdf37069087706e99841ec24b122850b829e032d3185e90c7dabfd.jpg)  
Fig. 11. Results of the expert system application.

TRANS-POL requires the application of the majority of TRANS-POL modules. The final options (alternative solutions) scores are presented in graphical form in Fig. 12, where the time dimension is included (the numerical output is presented in Fig. 8 of the previous section).

The fourth example case is related to the ability of TRANS-POL to incorporate data from outputs generated by transport models applications. For this a simulated MKmetric output data base for airport traffic is used. Actually, the data base structure is maintained, but data elements are simulated. Thus, based on the data elements, queries are generated, which are:

1. Passengers starting from an airport

2. Passengers starting from an airport to a domestic destination

3. Passengers starting from an airport to an international destination

4. Passengers starting from an airport to a specific destination

5. Passengers starting from an airport to destinations in a specific country /group of countries

6. Same as queries (1) to (5), but for passengers landing at an airport

7. Same as queries (1) to (5), but for starting and landing passengers

8. Same as queries (1) to (3), but for passengers changing plane at an airport

9. Same as queries (1) to (8), but for passengers when trip purpose is business

10. Same as queries (1) to (8), but for passengers when trip purpose is private

11. Same as queries (1) to (8), but for passengers when trip purpose is vacation

12. Same as queries (1) to (8), but for passengers mileage

13. Same as queries (1) to (5), but for number of flight movements for all or specific class of aircraft

14. Same as query (13) but for aircraft mileage

15. Same as queries (1) to (14), but for a specific flight routing / group of flight routings

16. Passengers to/from a specific traffic zone

17. Passengers to/from a specific traffic zone by trip purpose and / or mode

18. Same as queries (15) to (16), but for a specific airport / group of airports

![](/api/attachments/PDK8YDRM/fulltext/images/53d57f94a2d5627c636118019dc0b73c3a6ff09fb3e870ab80e2c13525697ecd.jpg)  
Fig. 12. MCA graphical output: alternatives scores over time.

19. Same as queries (15) to (16), but for market shares for a specific airport / group of airports in specific traffic zones

20. Same as queries (15) to (16), but for the weight of a traffic zone in the total airport catchment area

The database has to be recalculated for each scenario of each project concerning the air network. The total number of all the above combinations of questions is 120! (Permutations). These are questions only specific to the air network. Illustrative graphics can be constructed from query results, as in Fig. 13. These queries show the area of influence of an airport (e.g., Munich, MUC).

At the first step, a simple query was created. This query provides the number of passengers of every single traffic zone using the specific airport, e.g., of Munich (MUC). A map in a GIS, which uses From<sup>\_</sup> node<sup>\_</sup>number (translated into a NUTS number) as a key can be colored by the data from the field Pax<sup>\_</sup>total found in this query. At the second step, the percentage market shares, instead of absolute numbers were computed. Usually this can also be done directly in GIS, although the data in this application is simulated, since the example’ objective is demonstrating the amount of information and possible questions to MKmetric’s tools. Data are stored in the access database <sup>b</sup>Airports.mdb.<sup>Q</sup>

## 7. The value of TRANS-POL

The added value of TRANS-POL is that it provides a medium for bringing together all kinds of transport models and databases, making them available to a wider audience in a user friendly environment. In addition, it facilitates the structured analysis by the decision maker of relevant policy issues, not only considering each one separately, but also by combining them to form a coherent transport policy. It is evident that this is possible with the use of the developed DSS, the role of which is critical for such analysis. The transport policy analysis is concerned with national or multi-national issues. The latter for Europe are mainly the ones introduced by the European Union, such as sustainability, interoperability and intermodality, social cohesion, protection of the environment. In addition, national issues like the development of a specific region, the promotion of environmental friendly modes could be included in the analysis. Thus, depending on the project considered, the DDS could produce answers to queries related to these issues, as long as outputs from the models’ applications and data related to these issues are available.

![](/api/attachments/PDK8YDRM/fulltext/images/eed236df9a4fae6a8952a9d20498a7028efc7076b9ce814291cf202b2caec169.jpg)  
Fig. 13. Illustrative Outputs from TRANS-POL application for air traffic.

As for the functional specifications of the system, it is noted that the DSS for making queries and interpreting results processes user friendly characteristics. In case it has to be applied in the European context, it is programmed as an independent application properly linked to ETIS Core Interface and other ETIS elements. DSS menus allow the user to formulate specific questions and information requests and transform them into a series of calls to transport models and/or databases. The DSS is able to handle, through a combination of a database manager and an expert system, the following options: (1) initiation of transport models more appropriate for the functionality requested by the user; (2) database utilities to establish queries, updating, obtaining reports, etc.; (3) establishment of expert rules to estimate missing data; (4) comparative answers to user questions relating to alternative scenarios/options; and (5) evaluation of model results according to multicriteria models (e.g., should I recommend this road to be built in this way?).

Options (1), (3) and (5) are provided through an expert system module that depends on the question, which model data to use, how to fill in data gaps, and what kind of results to display to the user. The abovementioned have demonstrated the role and necessity of the various components of TRANS-POL.

The system is developed in such a manner to be able to accept inputs from other models’ applications, and as such, it is quite flexible, a property that is not so frequently encountered in other similar systems. This flexibility allows the user to develop the DSS parameters in a way that it is embedded in the examined policy context. Regarding the different European

Commission initiatives, like ETIS, the developed DSS being a prototype has demonstrated its ability to be connected with them, as it is the case with the models developed under BRIDGES research project, which was part of the ETIS initiative.

On the other hand, it is true that in most cases, the DSS user is not the decision maker himself, but a consultant searching for answers of queries put forward by the decision maker. The proposed DSS not being very sophisticated software does not require any formal training and, in most cases, can be used even by a novice user like an official at the European Commission. Needless to say that this is only a prototype that demonstrates the abilities for such software. In case a commercial application is introduced, then the TRANS-POL has to be adapted to fulfil the necessities of its potential buyers. Such a commercial application must envisage ways to maintain data and maps, safeguard the acquisition of necessary licenses for updates etc.

## 8. Conclusions

TRANS-POL provides a set of tools that facilitate the decision maker (regardless if he is the user of the system himself) to answer queries regarding the impacts from the implementation of transport policies. It allows selecting or formulating questions, transforms them into a series of calls to transport models and databases (either remotely or on-line), and displays the results through its own routines (as reports, tables, graphs, maps) or through other modules, like the ETIS initiative of the European Commission. In addition, TRANS-POL can be used also as an independent module, since it has its own expert system shell, a multicriteria analysis, database management capabilities, and GIS utilities.

From the end user point of view, TRANS-POL is a scalable multi-software system, uses a Windows compatible technology, able to integrate multiple and specialized software applications, in particular sophisticated transport models, database managers and GIS. It is an intelligent system, able to facilitate intermediation between policy questions and outputs resulting from scientific models. It is also regarded as a user friendly system since it makes use of specific options such as mapping tools, which are needed to develop powerful user interfaces.

From a system developer’s point of view, TRANS-POL has impacts on drastically reducing the time and cost by building up an advanced multi-software support system. TRANS-POL actually represents the first attempt to develop a methodology and, based on it, a software tool able to provide intelligent mediation between advanced models and end users (decision makers). Complex tasks, such as writing model templates to interpret model results and translate user queries to model’s parameters, can be carried out relatively easily by system developers.

Hence, all considered, TRANS-POL could be characterised as an innovative software technology in the following dimensions: it brings new capabilities (e.g., a system of tools to interface and drive many commercial applications without being dependent on any of them); it optimises and refines already existing software tools (e.g., mapping tools for transportation networks, fully personalised interfaces).

As with any system, the proposed TRANS-POL has operational constraints within which it could operate. They are mainly related to data availability and associated with quality/reliability, as well as the abilities of the selected models to produce the needed outputs. There are several opportunities for future research in terms of advanced analysis options (e.g., uncertainty analysis in scenario-building), use of semantic databases, ICT linking back and front office applications, group decision-making applications etc. However, all of them will require a more sophisticated DSS, which has to be related to commercial applications, provided that there is an interest for such system by the potential users.

Nevertheless, the definition and implementation of a second generation TRANS-POL must integrate future users as much as possible, since for them a DSS represents both a challenge and an opportunity to improve their working processes. In any case, a DSS will induce organizational changes, which cannot be successful unless they are clearly perceived and desired from the outset.

## Acknowledgment

The present paper is based on the research project BRIDGES, funded by the European Commission IVth framework Programme on Research and Development, during the period 1997–2000.The members of the Consortium that carried out the work are MCRIT (Spain), NTUA (Greece), DTU (Denmark), M.E. and P. (U.K.), MKmetric (Germany), SOFRES (France) and TRT (Italy).

## References

[1] Amzi! Inc. <sup>b</sup>Amzi! Prolog User’s Guide and Reference,<sup>Q</sup> 1998.

[2] M. Batty, P.J. Densham, Decision Support, GIS, and Urban Planning, Centre for Advanced Spatial Analysis, University College London, 1996.

[3] M. Beuthe, S. Grant-Muller, A. Pearman, D. Tsamboulas (corresponding author), Prioritising trans-European network transport initiatives, presented at the 8th World Conference on Transport Research, Antwerp, (July) 1998.

[4] P. Densham, Spatial Decision Support Systems, in: D.J. Maguire, M.F. Goodchild, D.W. Rhind (Eds.), Geographical Information Systems: Principles and Applications, Longman, London, 1991, pp. 403– 412.

[5] Environmental Systems Research Institute, Inc. <sup>b</sup>Building Applications with MapObjects,<sup>Q</sup> 1996.

[6] K. Fedra, R.F. Reitsma, Decision support and geographic information systems, in: H.J. Scholten, J.C.H. Stillwell (Eds.), Geographic Information Systems for Urban and Regional Planning, Kluwer Academic Publishers, The Netherlands, 1990, pp. 177 – 188.

[7] S.S. Fine, J. Ambrosiano, A.M. Eyth, D. Hils, W.T. Smith, S. Thorpe, D.H. Loughlin, The environmental Decision Support System: simulation support and information management in an integrated computational framework, Proceedings of Eco-Informa ’96: Global Networks for Environmental Information, vol. 11, 4–7 November, Lake Buena Vista, FL, Environmental Research Institute of Michigan, 1996, pp. 586 – 591.

[8] D. Gifford, et al., Access 97 Unleashed, Sams Publishing, 1997.

[9] M.J. Ginzberg, E.A. Stohr, Decision Support Systems: issues and perspectives, in: J. Ginzberg, G. Reitman, E.A. Stohr (Eds.), Decision Support Systems, Amsterdam, North-Holland, 1982.

[10] B. Harris, Planning theory and the design of planning support systems, Second International Conference on Computers in Planning and Management, Oxford, (6–8 July) 1991.

[11] http://www.etis-eu.org/etis.html.

[12] M. Makowski, Y. Sawaragi, Advances in Methodology and Applications of Decision Support Systems, International Institute for Applied Systems Analysis, 1991, http://www.iiasa.ac. at/publications, accessed June 17, 2000.

[13] M.L. Manheim, Creativity-support systems for planning, design and decision support, Microcomputers in Civil Engineering 1 (1986) 14 – 31.

[14] A.T. Mann, Visual Basic 5. Developer’s Guide, Sams Publishing, 1997.

[15] M.E.&P, software MEPLAN, EUNET research project of the 4th Framework Programme financed by the European Commission, 1999.

[16] G.K. Mikroudis, D.A. Tsamboulas, Spata DSS software, developed for the BRIDGES research project of the 4th Framework programme, financed by the European Commission, 1999.

[17] MkMetric, software VIA (in-house developed), www.mkm.de.

[18] D.L. Osmond, D.E. Line, J.A. Gale, R.W. Gannon, C.B. Knott, K.A. Bartenhagen, M.H. Turner, S.W. Coffey, J. Spooner, J. Wells, J.C. Walker, L.L. Hargrove, M.A. Foster, P.D. Robillard, D.W. Lehning, WATERSHEDSS: Water, Soil and Hydro-Environmental Decision Support System, North Carolina State University, 1995.

[19] C.V. Patton, D.S. Sawicki, Basic Methods of Policy Analysis and Planning, Prentice-Hall, Englewood Cliffs, 1986.

[20] A. Pearman, S. Watson, D. Tsamboulas, M. Beuthe, Developing appraisal procedures for trans-European networks. Proceedings of the 25th European Transport Forum Annual Meeting, organised by PTRC, Transportation Planning Methods, vol. P414/1, Brunel University, Uxbridge London, vol.1, (September) 1997.

[21] John Radke, A Spatial Decision Support System for Urban/ Wildland Interface Fire Hazards, University of California at Berkley, Federal Emergency Management Agency (FEMA), http//www.esri.com/library/userconf/pro95/to200/p175html, accessed July 21, 2000.

[22] D.A. Tsamboulas, G.K., Mikroudis, Decision Support System (DSS), BRIDGES Research project of the 4th Framework Programme, financed by the European Commission European Commission, 1999.

[23] A. Ulied, D. Tsamboulas, B. Mandel, O. Nielsen, C. Delavelle, I. Williams, A. Martino, Final Report, BRIDGES Research project, European Commission, (May) 2000, Brussels.

[24] I. Williams, P. Mackie, D. Tsamboulas, J. Larkinson, Assessing the socio economic and spatial impacts of transport initiatives: the eunet project, Presented at the 8th World Conference on Transport Research done in Antwerp, July, 1998.

Dr. Dimitrios Tsamboulas is an Associate Professor at the Department of Transportation Planning and Engineering, Faculty of Civil Engineering, at the National Technical University of Athens (NTUA).

He holds a Diploma of Civil Engineering of the National Technical University of Athens, Greece (1973), Master of Science (1975) and Civil Engineer’s Degree (1981) of the Massachusetts Institute of Technology, USA and also holds a Degree of Doctor of Philosophy (PhD) of University of Massachusetts, USA (1983). He speaks two languages fluently (English and French) and has basic knowledge of two more languages (Italian and German).

He is a member of many professional bodies (Technical Chamber of Greece, Association of Greek Professional Civil Engineers, Hellenic Institute of Transportation Engineer, etc.).

He is also Chairman or member to several international committees and groups of experts, as well as a member of scientific committees and reviewer of papers in scientific journals (Transportation Research Board of USA, Committee of the Scientific; the journal Innovation, The European Journal of Social Sciences;

Reviewer for the Transportation Research Record, European Journal of Operational Research, Scientific Journal Transportation Research Part C Emerging Technologies, <sup>b</sup>Technica Chronica<sup>Q</sup>/ Scientific Publication of the Technical Chamber of Greece, etc.).

He is the author of two books, co-editor in one book, and has more than 130 papers in scientific journals and presentations in conferences. He has more than 30 years of professional experience, in areas such as feasibility studies of transport infrastructure projects, transportation management, decision support systems, transport policies, modeling and forecasting, intermodality, new technologies and information systems for transport applications, cost-benefit and multi-criteria analysis, etc. He was project manager or participated in more than 50 research projects financed by the European Commission or other organizations and he was involved in more than 40 international and national consultancy studies in Greece, EU, Africa and in Phare countries, etc.

Dr. George Mikroudis is a Civil Engineering Consultant with a Professional Registration for Environmental and Transportation Studies.

He holds a Diploma of Civil Engineering of the National Technical University of Athens, Greece (1981), Master of Science (1984) and a Degree of Doctor of Philosophy (PhD) of Lehigh University of Bethlehem, PA, USA (1983). He is a native Greek, speaks fluently two languages (English and French) and has basic knowledge of one more language (German).

He is a member of many professional bodies (Technical Chamber of Greece, Association of Greek Professional Civil Engineers, Hellenic Institute of Transportation Engineers, Acoustics Society of Greece, Greek Sanitation Engineers, ASCE, IEEE, AAAS, Sigma Xi, etc.).

He is also the Managing Director of Twin Peak S.A., a Greek telecom company, and executive director of DAGM Developers Inc., a Greek construction company. He has been the CEO of Unitel Hellas S.A., a Greek satellite communications company, and an independent consultant for more than 25 years.

He has conducted more than 130 Environmental Impact Studies (EIS) of road projects, 30 EIS of railway projects, 35 EIS for airports, 20 EIS of harbours, 45 noise protection studies, 25 EIS of buildings and urban area projects, as well as development of over 15 commercial environmental, structural and geotechnical engineering software systems, such as EMoS by ODOS Logismiki, specifically for environmental impacts of road and railway projects, more than 20 structural designs of buildings and 2 road designs. Project examples include EISs for PATHE (Patras– Athens–Thessaloniki–Eidomeni Highway) motorway, EGNATIA motorway, IONIAN motorway, ATTIKI ODOS motorway, Olympic projects, Athens–Thessaloniki–Eidomeni high-speed railway, Port of Pireus, evaluation of 28 EIS of Greek ports, Eleftherios Venizelos, Thessaloniki, Heraklion airports, EIS of dams, industrial facilities, mines, urban projects, etc., environmental evaluation of 10 highway projects in Europe, environmental assessment of road projects in MEDA countries.

He is the author of one book and has more than 60 papers in scientific journals and presentations in conferences. He has more than 25 years of professional experience in areas such as environmental impact studies, air pollution, noise, visual intrusion, soil pollution, water pollution, environmental management, environmental policies, noise protection studies, feasibility studies of transport infrastructure projects, expert systems, artificial intelligence, decision support systems, databases, GIS, CAD, software development for environmental, structural and geotechnical engineering, modeling and forecasting, new technologies and information systems for engineering applications, multi-criteria analysis, structural analysis and design of buildings, earthquake engineering, telecommunications, satellite communications, etc. He was project manager or participated in more than 20 research projects financed by the European Commission or other organizations and he was involved in more than 250 international and national consultancy studies in Greece, EU, USA, Africa and in Phare countries, etc.
