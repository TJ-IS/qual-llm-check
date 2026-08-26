---
otero_id: 17172
otero_key: "ZEBDZWSE"
title: "An integrated multicomputer DSS design for transport planning using embedded computer simulation and database tools"
authors: "Jeffery K. Cochran; Ming-Tsu Chen"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90048-g"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated multicomputer DSS design for transport planning using embedded computer simulation and database tools

Jeffery K. Cochran and Ming-Tsu Chen
Systems Simulation Laboratory, Industrial and Management Systems Engineering, Arizona State University, Tempe AZ 85287, USA

Goods movement is probably the most neglected issue in transport planning. What work has been done is largely restricted to urban goods movement. A major project funded by the Arizona Department of Transportation has resulted in a unique Decision Support System for transportation planners of highway goods movement. This paper presents the design of that system. Some of the system's unique features include: (1) use of both mainframe and microcomputers to form an integrated interface, (2) use of a database language to organize and preprocess mail survey data and topology data, and (3) use of a discrete-event computer simulation model to perform "what-if" scenarios in a statistically valid manner. All components of the system are accessed through a user-friendly menu structure which assists in both data manipulation and the translation of simulation experiment output into summaries of commodity type, weight distribution, capacity analysis, safety implications, and pavement maintenance. This DSS, named AFNA (Arizona Freight Network Analysis), is the first involving simultaneous embedded computer simulation and database tools. It is complete and now in use providing ADOT transportation engineers with new planning capabilities.

Keywords: Computer simulation, DSS design, Embedded software tools, Transport planning, Multicomputer DSS, Highway goods movement.

cial intelligence, expert systems, and decision support and analysis methodology. His industrial experience includes work at Battelle Northwest Laboratory, Los Alamos National Laboratory, and NASA's Laboratory for Application of Remote Sensing.

![](/api/attachments/ZEBDZWSE/fulltext/images/ef01ed4e19cd700541373790cd01ebba99793f9ad218b3aa3d8fb61a88c90256.jpg)

Highway networks serve as the most critical means of moving goods and people. Since most traditional transportation studies have focused on passenger car traffic flow and urban transportation planning activities, highway goods movement is probably the most neglected issue in transportation planning. With increasing passenger traffic and freight hauling on major Arizona highways resulting from the state's rapidly growing population, the Arizona Department of Transportation (ADOT) is now concerned with the preparation of statewide “master plans” to meet existing and future freight demands [9].

Jeffery K. Cochran is Associate Professor of Industrial & Management Systems Engineering at Arizona State University. He received a PhD in Industrial Engineering (Operations Research) from Purdue University in 1984. At ASU he is also a Director of the System Simulation Laboratory. Through this laboratory Dr. Cochran is pursuing research interests in applied operations research, simulation and stochastic system modeling, computer integrated systems design, artifi

Research background

To study the impacts of anticipated increases in freight flows in the Arizona highway system, the Transportation Planning Division of the ADOT awarded a contract to a multidisciplinary research team at Arizona State University (ASU) to develop a computer-simulated model of freight movement. This project is entitled Arizona Freight Network Analysis (AFNA). To create the AFNA model, the team conducted a state-wide survey of public and private freight carriers. The survey supplied information such as carrier type, commodity type, total weight, shipping date, origin-destination points for a large number of trips, and “via” routes. The survey data was then compiled into an information directory of all carriers, which serves as the basis for the AFNA project and is the driving force for the computer simulation model. Since ADOT did not have a DSS, and the management was unaware of exact DSS capabilities, the AFNA project was seen as a chance to introduce DSS techniques into ADOT for the first time.

![](/api/attachments/ZEBDZWSE/fulltext/images/336eae5e9652b2ae95b60503e85375a50ac689649003c79c868a852befcc5f37.jpg)  
Ming T. Chen is a Systems Engineer at Motorola, Inc., in Phoenix, Arizona, where he is responsible for networking, data communication, and database design and development. He has a Masters degree in Industrial and Management Systems Engineering from Arizona State University.

## Research Objective

The primary objective of this research is to design and develop a DSS for ADOT transportation planners dealing with goods movement on highways. The system incorporates a database and a simulation model as fundamental analysis tools. The prime consideration in developing the AFNA DSS is to create a program with DSS characteristics: user friendly, interactive, various solutions from a model library, and capable of accessing pertinent database information.

The computer simulation model developed in this research represents the core of the DSS to which additional front-end and back-end software modules have been added for specific application requirements. Our DSS framework emphasizes data, model, and dialog function integration to assist in decision-making. A menu-driven user-system interface is provided so that all the data and model operations are transparent to the user. The AFNA DSS is used in freight movement planning to provide the decision makers with information which is derived from the state highway network simulation model. The Arizona highway system studied in the project includes all major highway sections within the Arizona state boundary (204 links, 82 nodes).

An important feature of the AFNA DSS is the capability to conduct “what if” experiments, such as closed lanes and roads, by adjusting only the input data files without recompiling any software. As a result, AFNA provides an easy-to-use simulation-based decision support environment. Moreover, several built-in planning routines analyze the simulation outputs to help the user justify results and make better decisions.

Alavi [1] points out that the designer of a DSS should be cognizant of three specific guidelines: the decision maker should be involved in the design, development, and evaluation of the DSS; prototypes should be built before the full-scale system is built; and the DSS should support capabilities for complexity coping, conflict resolution, and uncertainty reduction. Alavi proposes an approach called “adaptive design” for DSS development, and applies it successfully in a case study [2].

Clearly, DSS requires a unique development approach. The words iterative, evolutionary, and adaptive design are all used to describe this approach in which needs analysis, design, development, and implementation are all combined into a single phase which is reiterated in a short period of time. The use of these concepts in designing the AFNA DSS is another research objective.

## Pertinent DSS Applications

Applications motivate Decision Support Systems research. Since the DSS concept was introduced and developed, many successes have been reported $[5,14,15,23,24]$ . As various DSS applications are studied, it becomes clear that they differ considerably. Some are mainframe-based, while others run on a PC. Some support ad hoc decision-making, while others are used for institutional decision support in an organization $[12]$ . However, most applications share the feature that they are intended to provide cost savings, better decisions, and better communication about decisions. In this section, several DSS applications related to transportation analysis are presented.

The train dispatching system used by the Norfolk Southern Railway is a highly successful DSS [20]. It is an on-line, real-time, operational DSS that is used daily by train dispatchers to route trains along a section of track for which they are responsible. The operations research staff developed specialized algorithms and models specifically for train dispatching and related decisions. The impact is to reduce resulting train delay time. While the system offers an optimal solution for each dispatching decision, the dispatcher retains the ability to override each path to reflect his experience and judgement.

Kornhauser [3,16] describes the analysis capabilities of the Princeton Transportation Network Model and Graphical Information System (PTNM/GIS). The PTNM/GIS is an integrated package of computer programs and databases for freight transport planning of operations, marketing, and strategy. Railroad, trucking, and intermodal issues are each analyzed using the programs, networks, and databases within the PTNM/GIS which can be regarded as a generalized DSS. It is specifically designed to help transportation industrial managers make better-informed decisions by using its powerful map operations (graphical capabilities). However, it does not contain statistical experimentation capabilities.

Daily [10] describes a DSS for trucking break-bulk operations. This DSS is designed and developed in conjunction with a large motor carrier. It uses a PC located at the break-bulk operation with a database maintained on a remote mainframe. The DSS, on a daily basis, determines the best allocation of men, equipment, and facilities for various costs and services. Moreover, it can be used to perform a weekly forecast of manpower required.

Gavish [13] presents a DSS for managing the transportation needs of a large corporation. The system uses analytical operations research based models for forecasting, load balancing, scheduling, and control. It supports decisions such as vehicle maintenance, fleet sizing, and depot location. Feedback mechanisms for updating the status of the system and for improving the decision support models are provided.

Each of these systems contains a piece of the puzzle for developing the AFNA DSS, but our design has several key differences. AFNA uses a discrete-event computer simulation model as the central scenario generator. Further, we use a simultaneous combination of mainframe and microcomputers to perform calculations. Finally, the problem of goods movement on highways is our focus. These features are unique and will be presented in some detail in the rest of this paper.

## Specific DSS Identification: ROMC Analysis

ROMC analysis, used to identify capabilities for any DSS, is a process-independent model for structuring DSS design which has proven to be very adaptable to user needs and iterative development [22]. This approach focuses on the user point of view to generate representations (R's) to help conceptualize and communicate the information, operations (O's) to analyze and manipulate the representations, memory aids (M's) to help the user link the representations and operations, and control mechanisms (C's) to operate the system. Listed below are the capabilities that we use in the AFNA DSS:

## Representations

Tables Freight carrier directory
Highway travel data
Highway static characteristics
Highway traffic characteristics
Highway city intersection
Accident records
Highway maintenance

Maps Arizona engineering districts and maintenance sections

Reports Simulation output

Graphs Histograms of traffic volumes

Operations Operations on tables
Operations on graphs
Operations on database
Operations on survey data
Extraction language
Control language

Memory Aids
Database for tables and graphs
Model output
Workspaces for each representation
Libraries
Hard copies

Control Mechanisms
Use menus to display operations
Use question-answer dialogue to input data
Provide special function keys
Provide on line help messages
Provide program instruction and user manual

The above specific sets of R's, O's, M's, and C's constitute the AFNA system capability requirements.

This approach is directly linked with the Bonczek dialog-data-model DSS framework [7]. The dialog component is used to build the R and C capabilities; the modeling component is used to build the O capabilities; and the database component is used to build the M capabilities. Thus, ROMC analysis not only identifies the specific DSS, but also provides the specifications of the capabilities that the DSS software must provide for building the specific DSS.

## Software Development Strategy: Microcomputer-Based and Modular Software Integration Approach

The decision-maker's role is being reshaped by the use of the PC along with the advanced technology developed in the area of microcomputers. With the expanded random access memory (RAM) capabilities brought about by 16-bit microprocessors (32-bit microprocessors are also available now), and the expanded storage capability made possible by the hard disk unit, the stage is set for rapid development of useful and powerful DSS software packages on PCs.

Five levels of DSS software have been identified [6]: specific DSS (SDSS), generalized DSS (GDSS), DSS generator (DSSG), DSS tools (DSST), and general purpose programming languages. Ultimately, all DSS software is built upon some general-purpose programming language, and any SDSS can be developed using only this type of software. However, directly using general-purpose languages to develop an SDSS application program is typically not practical in terms of time, effort, and technical skill requirements.

In a recent study [19], a number of PC software potentially useful for decision support are discussed. According to their functional capability, they are categorized into three groups: software for database management, software for model-base management, and software for integrated DBMS support. Although many packages exist for the first two groups, only a very limited number of contemporary software belong to the last category – the integrated package. Moreover, many integrated packages which combine only spreadsheet calculation, file management, and graphics capabilities tend to be less powerful and comprehensive than the type of single-function package (DSST) that is currently available [4]. This disadvantage, called the Swiss Army Knife Syndrome, raises a question regarding specific DSS software development strategy: do we use an existing integrated package (DSSG), or do we design procedures that will enable the rapid integration of disparate existing software products (DSST) into a package? The latter strategy, which can be called the “modular integration approach”, has been adopted in this research since the AFNA database has already been created by the dBASE III package (a DSST), and the simulation modeling capability requirement is found only in specialized simulation software.

DOS 3.0 ENVIRONMENT  
![](/api/attachments/ZEBDZWSE/fulltext/images/9120f73f9c0da7ab781c3c987c42b48444561f3f549dcd0cebda12f1baf99862.jpg)  
Fig. 1. Modular Software Integration Development.

The conceptual layout of this design procedure for the AFNA DSS is shown in fig. 1. BASIC language version 3.0 handles the DSS dialog interface and provides the means for system integration because of its comprehensive and powerful command set. The command “SHELL” is used to link all modular components within the mainline dialog program. The “SHELL” command allows control to exit from the BASIC program to the DOS environment, run a .COM, .EXE, or .BAT program, and return to the BASIC program at the line after the “SHELL” statement. This powerful mechanism facilitates the modular software integration process of combining two or more stand-alone programs into a single package, thereby allowing the user to use the data and the model between applications without turning off one application before using another.

There are many benefits to the modular system development approach. The whole system can be divided into several modules and linked by a mainline program which serves as a central interface. Individual modules can be written in any software language as long as it can be compiled into an .EXE file; that is, the software structure permits the components to be nonhomogeneous. The system can be expanded and maintained in an easy and flexible manner since individual modules are developed independently. System development time can be reduced as a result of functional decomposition. Thus, an individual module is a manageable size and this facilitates coding and debugging procedures. System portability is enhanced because the program is executable directly from the DOS prompt, which means complete independence from background software packages is attained. The newest available software products as well as previously developed programs can be conveniently adopted and tailored to the system in an integrated fashion.

## Modeling Approach: Data-Driven Discrete-Event Computer Simulation

The objective of the AFNA DSS is to enhance the transportation planning functions of ADOT through improved data and modeling of freight flow on the Arizona highway network. Network analysis views a complex system as being composed of sources, sinks, and interchange points. Two approaches can be taken to solve network transportation problems; closed-form mathematical solutions (equation or optimization models), or computer simulation (description or process models). The computer simulation approach is chosen here based on two key factors: our domain has problem statistics complexity, and we need to generate different scenarios for planning functions. Computer simulation has previously been used successfully in a few DSS studies $[8,11]$ . Ross $[18]$ lists some transportation simulation models and their main features. Ours is the first transportation DSS with embedded simulation.

The AFNA simulation model is driven by survey data (see fig. 2). There are six distinct stages comprising the survey data-driven simulation modeling technique:

(1) The real system is measured (in the AFNA case, this information is provided by ADOT highway ground count data),

(2) Raw data is collected by a multi-stage survey mailer.

(3) Raw survey data is refined by an analysis program until it is suitable as input,

(4) The refined surveys data is combined with network topological data,

(5) The combined data is used by the data-driven simulator to generate performance matrices, and

![](/api/attachments/ZEBDZWSE/fulltext/images/3451e88843c672eed368dafe534d9d41fddae6cc63b7d11e8ba5bf2156946409.jpg)  
Fig. 2. Survey Data-Driven Simulation.

(6) The survey data-driven simulation model results are validated by comparing the model response with the corresponding system response.

Many of the mathematical details of this process are presented in [9].

## The AFNA System Structure

The AFNA software environment contains five modules: the user-system interface module, the dBASE III database module, the model data preprocessor module, the SLAM II [17] Arizona highway simulation model module, and the transportation planning module.

The user-system interface module facilitates user interaction with the data and the model components of the AFNA by a menu-driven dialog. From the user's point of view, the dialog is the system. It provides the control and operation of the DSS, enabling the user to access information, supply data for the model, execute models, compare alternatives, and store results. Researchers have shown that a good design of the user-system interface can make a substantial difference in learning time, system performance, and user satisfaction [21]. Thus, the user-system interface module plays an important role in providing a user-friendly dialog and integrating the data/model components into the unified AFNA DSS environment.

![](/api/attachments/ZEBDZWSE/fulltext/images/bf128c499c3ba805196ec7d3c94d69a1b57306f7f9e154449c299d3fef6b14c0.jpg)  
Fig. 3. AFNA Multi-level Menu Structure.

![](/api/attachments/ZEBDZWSE/fulltext/images/5aa6a092270c1a39a6af414f56c5f1e58a97ec876b8c7698aaad1e83f8c6fd00.jpg)  
Fig. 4. AFNA Data Bases & Data Extraction Procedure.

AFNA SYSTEM  
![](/api/attachments/ZEBDZWSE/fulltext/images/42aefbb41a56583d8270b3b089be4feac4f2f6b905481ebf992d453fb3e3540a.jpg)  
Fig. 5. AFNA Model Structure & Library.

Menu selection systems are attractive because they can eliminate training and memorizing complex command sequences. When AFNA is initiated, a main menu appears from which the user can select a course of action. From the main menu, the system proceeds into another menu or into a question/answer dialog to determine the information or direct action desired. The multilevel menu structure in AFNA is shown in fig. 3. Based on functionality, the database operations, data preprocessor operations, simulation model operations, and planning module operations are grouped together into a menu tree structure. This menu organization is designed to reflect the AFNA DSS structure, as well as to match our users' tasks.

The microcomputer screen is the medium for supplying information to the user. A well-designed screen enhances the efficiency of operations and communications. It helps the user find the information necessary for desired operations, and interpret the output of programs. The extended ASCII characters for graphic symbols, color options in foreground and background display, and the on-line error checking routines are all implemented in the AFNA dialog screen design. The conceptual design of the data extraction procedures and databases in the AFNA system is presented in fig. 4. The database management functions are provided by the dBASE III package. The data-model link functions are performed by a data pre-processor.

## The Slam II Simulation Model Module

Fig. 5 reviews the conceptual layout of the AFNA model structure and library. The initial computer coding task concentrates on the full scale conditional branching simulation model.

The output from the simulation model is automatically converted into user-domain terms. Eight specially programmed options are provided for the AFNA DSS:

\- SURVEY freight data echo report - a file which is used to drive the conditional branching simulation model.

\- LINK summary report (STATISTIC) - the time-persistent statistics of an individual link which is specified by the user.

\- LINK summary report (HISTOGRAM) – the statistics in histogram form. Due to the array size limitation, it allows only for FREEWAY links at this time.

\- NODE summary report (STATISTICS) – all inbound and outbound link statistics for the city as specified by the user.

\- COMMODITY distribution summary (by LINK) – the truck commodity percentage distribution for all links.

\- WEIGHT distribution summary (by LINK) – the truck weight distribution for all links.

\- Average Daily Traffic (ADT) summary (by route) – the ADT result for the specific route (Interstate, Federal, and State highway) by user requirement.

\- Traffic congestion analysis (by LINK) - the simulated traffic volume/capacity ratio for each link.

All options show the results on the terminal screen in an interactive mode. Moreover, the user can provide an output file name to save the results of selected portions of a planning session in a disk file for later use in report generation.

The AFNA simulation model is currently running on the ASU EJS mainframe system instead of in an IBM PC environment. The primary reason for this is network size. An IBM PC is not capable of running the full scale (204 links) model due to the limited memory capacity of the SLAM PC version. In addition, the execution of a large scale discrete-event simulation on a PC is very slow (in some cases, a run may take a couple of days). As a consequence, it is more suitable for the AFNA simulation model to run on the ASU EJS mainframe system and be accessed through a modem from a PC environment.

The EJS system is running on an IBM 4381 super-minicomputer under the CMS (Conversational Monitor System) environment. CMS enables the user to create, update, and manipulate files, as well as compile, test, and execute the program in an interactive mode. The Engineering Computer Services (ECS) department fully supports this system at ASU. ADOT planners are in Phoenix and may easily access the system by modem.

![](/api/attachments/ZEBDZWSE/fulltext/images/68a99902cbadf31ab266662b41b5c78de0e28d3511d5a5d4f8a69f86f9335ba0.jpg)  
Fig. 6. AFNA PC-Mainframe Communication.

The ability to transfer information conveniently is crucial for the SLAM simulation model module. Fig. 6 illustrates the PC-mainframe communication design in the AFNA system. The input files can be prepared or updated in advance on the PC, and the simulation output can be analyzed in the PC environment, so that ADOT saves mainframe access time. Utility functions make uploading and downloading files easy.

## Summary and Conclusions

The Arizona Freight Network Analysis System was developed for the Arizona Department of Transportation to evaluate the current status and future condition of rural freight-movement systems in Arizona. The system, named AFNA, is a menu-driven interactive decision support environment which consists of five modules, namely: the user-system interface module, the dBASE III database module, the model data preprocessor module, the SLAM II simulation model module, and the transportation planning module. These modules are integrated in a state-of-the-art manner.

The user-system interface module plays an important role in communicating within and controlling movement through the whole system, as well as in providing a user-friendly dialog between the AFNA system and the user. The dBASE III database module contains two databases, namely: the freight carrier directory database, and the freight flow survey database. The model-data link requirement is accomplished by the model data preprocessor, whose function is to refine the survey freight flow data until it is suitable input to the simulation model. This refined freight flow data and the Arizona highway network topology and link data are used to drive the SLAM II simulation model. As a result, the model (which is based on a conditional branching approach) can be considered as a generic data-driven truck routing simulator. Finally, the planning module uses the simulation output data to perform various statistical analyses, including average daily truck traffic, commodity type and weight class distribution, congestion analysis, safety implications, and pavement maintenance planning.

The data-model-dialog paradigm for a decision support system design demonstrates itself to be a useful framework in this research study. Our modular software integration approach incorporates separate programs developed by the AFNA project team into a unified package. A mainline dialog generation and control program is the key for integration. It serves as a common interface between the various system modules and the user in the AFNA system.

To execute a large scale simulation model, a communication network between micro- and mainframe computers is needed. The AFNA simulation model runs on the mainframe, yet the model data preparation and output analysis and presentation are performed on the PC to take advantage of the microcomputer's excellent user interface and relative lack of expense.

The model developed for the AFNA system is a data-driven simulation model. Different from a traditional simulation model which tends to combine data, knowledge, and control in its programming, the data-driven modeling approach treats the data and control logic as distinct parts. Thus, the resultant model is a generic simulator which can be used in many different application scenarios without modifying the program.

The use of the decision support system design concept and data-driven simulation model in this project make the AFNA system flexible, useful, and effective. At this time, two significant planning efforts are under way at ADOT which use the AFNA DSS as a key component.

## Acknowledgement

We wish to acknowledge the assistance of the Center for Advanced Research in Transportation at Arizona State University for the use of its personnel and computer resources. We also wish to thank the Arizona Department of Transportation for funding this project under Grant No. 800815. Finally, we wish to thank the anonymous referees for their helpful suggestions.

## References

[1] M. Alavi, An Assessment of the Concept of Decision Support System as Viewed by Senior-Level Executives, MIS Quarterly, Dec. (1982).

[2] M. Alavi, and H.A. Napier, An Experiment in Applying the Adaptive Design Approach to DSS Development, Information & Management, 7, No. 1 (1984).

[3] ALK Associates, The Princeton Transportation Network Model and Graphic Information System, Princeton, New Jersey, April (1986).

[4] B.L. Alperson, The Fully Powered PC, Simon & Schuster, Inc. New York (1985).

[5] S.J. Andriole, ed., Microcomputer Decision Support Systems: Design, Implementation, and Evaluation, QED Information Sciences, Inc., Massachusetts (1986).

[6] G. Ariav and M.J. Ginzberg, DSS Design: A Systemic View of Decision Support, Communications of the ACM, Oct. (1985).

[7] Bonczek et al., The Foundations of Decision Support Systems, Academic Press, New York (1981).

[8] L. Brennan et al., The Development of an Interactive Simulation Model for Management Decision Making, Proceedings of the 1984 UKSC Conference on Computer Simulation, pp. 313–325, Sept. (1984).

[9] J.K. Cochran, and L. Lin, An Application of Computer Simulation to Freight Transport Systems, Journal of the Operational Research Society, 40, No. 5 (1989).

[10] M.M. Daily et al., Decision Support Systems for Trucking Break-Bulk Operations, TRB, Transportation Research Record 1038 (1985).

[11] Z.S. Dan, A Simulation Environment for Decision Support, ULTRATECH Conference Proceedings 1986, Vol. 2, pp. 85–96, Sept. (1986).

[12] C. Garnto and H.J. Watson, An Investigation of Database Requirements for Institutional and Ad Hoc DSS, Database, Summer (1985).

[13] B. Gavish, A Decision Support System for Managing the Transportation Needs of a Large Corporation, AIIE Trans, Vol. 13, No. 1 (1981).

[14] W.C. House, ed., Decision Support Systems: A Data-Based, Model-Oriented, User-Developed Discipline, Petrocelli Books, New Jersey (1983).

[15] P.G.W. Keen and M.S. Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Massachusetts (1978).

[16] A.L. Kornhauser and M. Bodden, Network Analysis of Highway and Intermodal Rail-Highway Freight Traffic, Transportation Research Record 920 (1983).

[17] A.A.B. Pritsker, Introduction to Simulation and SLAM II, 3rd Ed., Systems Publishing Corp., Indiana (1986).

[18] P. Ross and D. Gibson, Survey of Models for Simulating Traffic, An Overview of Simulation in Highway Transportation, Society for Computer Simulation (1977).

[19] A.P. Sage, An Overview of Contemporary Issues in the Design and Development of Microcomputer Decision Support Systems, in Microcomputer Decision Support Systems: Design, Implementation, and Evaluation, ed. by Stephen J. Andriole, QED Information Sciences, Inc., Massachusetts (1986).

[20] R.L. Sauder and W.M. Westerman, Computer Aided Train Dispatching: Decision Support Through Optimization, Interfaces, 13, No. 6 (1983).

[21] B. Shneiderman, Designing the User Interface: Strategy for Effective Human-Computer Interaction, Massachusetts, Addison-Wesley (1987).

[22] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly, 4, No. 4 (1980).

[23] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, New Jersey (1982).

[24] R.H. Sprague, Jr. and H.J. Watson, ed., Decision Support Systems: Putting Theory into Practice, Prentice-Hall, New Jersey (1986).
