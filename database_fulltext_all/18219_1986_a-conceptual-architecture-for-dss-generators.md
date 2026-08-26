---
otero_id: 18219
otero_key: "26SE7U5E"
title: "A conceptual architecture for DSS generators"
authors: "K.B.C. Saxena; Mohan Kaul"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90024-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Conceptual Architecture for DSS Generators

K.B.C. Saxena

Department of Computing Studies, Hong Kong Polytechnic, Hung Hom, Kowloon, Hong Kong

and

Mohan Kaul

Indian Institute of Management, Ahmedabad, India \*

The development of DSS generators is a complicated task. No existing DSS generator has been reported as a generalised, powerful and “user friendly” system, which provides full-range of capabilities for easily building specific DSS in any application area. In order to integrate a variety of decision support and data management capabilities into a well-designed, orderly whole, a conceptual design model must be created as a foundation for developing such software systems. Sprague’s DSS model provides a basis for the creation of a foundation for DSS generator development. This paper proposes a comprehensive conceptual design model which is an in-depth augmentation of Sprague’s original model. This model not merely provides a basis for developing DSS generators; it also proposes a fundamental architecture of DSS generators which removes some of the responsibilities of DSS design from the user. Further, the conceptual model has been technically validated by implementing an experimental DSS generator REGIMES on a microcomputer. This implementation also demonstrates the feasibility of implementing a powerful DSS generator on cost-effective hardware.

Keywords: Decision support systems, DSS generators, DSS software, DSS architecture, DSS design

## 1. Introduction

Sprague has described a conceptual model of DSS [11]. A generalised DSS in his conceptual model is a DSS generator and includes three major components – a Data Base Management Software (DBMS), a Model Base Management Software (MBMS), and a user-system interface called the Dialogue Generation and Management Software (DGMS). The development of a DSS generator such as this is a complicated task. A DSS generator should not be developed by simply patching together a group of stand-alone software compo-

![](/api/attachments/26SE7U5E/fulltext/images/b83741c966074944c67d4b2fc57ad784ff1796aa183eccd9f54ece9192bc8cf5.jpg)

K.B.C. Saxena is a Senior Lecturer in the Department of Computing Studies, Hong Kong Polytechnic, Hong Kong. He received his B.Sc. (1961) and M.Sc. (1968) from Lucknow University, India and has recently submitted his dissertation for Ph.D. in Management to Gujarat University, Ahmedabad, India. Author of over forty articles and papers, his current research interests are directed toward the areas of decision support systems, end user computing, human factors in

computer systems, and software engineering. He is a member of the Institute of Data Processing Management, U.K., Association for Computing Machinery, Society for Information Management, IEEE Computer Society, Hong Kong Computer Society, Hong Kong Management Association, and Computer Society of India.  
![](/api/attachments/26SE7U5E/fulltext/images/b47e44f0ae098abedf8186f0a2b6f649fd9533e467fd3ebc4c221bcfa7ff3651.jpg)

Mohan Kaul is Director of Management Development Programme at the Commonwealth Secretariat, London, U.K. He has worked as Expert Advisor, Management Information Systems, United Nations Development Programme, Malaysia and Professor and Dean (Planning) at the Indian Institute of Management, Ahmedabad, India prior to his present assignment. He received his Ph.D. (1970) in Computer Science from University of Paris. Dr. Kaul's research and consulting in terests include Management Information Systems, Decision Support Systems and Software Systems.

nents. Neither should it be just an extension of another software package adding some decision support features. Users of a DSS generator have different problems and interests, and view the DSS generator from different perspectives. Furthermore, both data base management and model base management subsystems of the DSS generator are large, complex entities in themselves. Consequently, in order to achieve an efficient, workable system, concepts from DBMS and MBMS must be cleverly integrated into a well-designed, orderly whole. In essence, a conceptual design model must be created as a foundation for developing DSS generators. Of late, Wang and Courtney have presented a conceptual model of DSS generators based on Sprague's model [13]. However, this model has not taken into account the important characteristics of DSS users and their needs for multiple user interfaces and multiple representation of information. Such a user-oriented model is formulated in this paper, which conveys five essential components of a DSS generator (Fig. 1):
a. A User Interface Manager (UIM)
b. A Representation Manager (RM)
c. An Analysis Manager (AM)
d. A System Manager (SM)
e. A Data Extraction Manager (DEM)
It also conveys four essential types of libraries or bases:
a. A DSS data base
b. A working or views data base
c. An analysis base
d. A graphics base

![](/api/attachments/26SE7U5E/fulltext/images/48e44071aadb9cf4038f08054da96fa53c8f8a27cf6f69e4ad9235f35614f166.jpg)  
Fig. 1. A Conceptual Design Model for DSS Generators

These libraries or bases are managed with the help of three dictionaries: a data dictionary, an analysis dictionary, and a graphics dictionary.

## 2. The User Interface Manager

The diversity of situations in which a DSS generator may be used makes it difficult to prescribe a universal set of objectives for the user interface. DSS users are discretionary users with a wide range of experience, problems, skills, and expectations. In order to be both “usable” and “useful”, the human aspects of its users cannot be ignored. The need for “user friendly” systems has been felt for quite some time and many software systems have realised this by providing easy-to-use but single interfaces. However, “user friendliness” is a relative concept which depends on several factors related to the user; e.g., training and frequency of use. Therefore, an interface which could be “user friendly” to one category of users may be “user unfriendly” to another.

The ease of use of a DSS generator depends on the user's training and experience of working with interactive computer systems and his/her frequency of use. A menu based user interface is more suitable for trained but casual users. However, experienced users may prefer to work with a command language and untrained casual users may prefer a natural language question-and-answer interface. Thus we propose the interface requirement matrix of table 1 on the basis of user and user interface characteristics

Thus, a DSS generator should provide all the three major types of interfaces: menus, command language, and natural language questions/answers. Further, the DSS generator should provide the capability to shift from one interface to the other at the user's choice [12]. It should also provide the capability of presenting responses with a variety of formats and output devices, such as alphanumeric screens, graphic screens, printer/plotter hard copy, etc.

Table 1

<table><tr><td></td><td>Casual User</td><td>Regular User</td></tr><tr><td>Trained User</td><td>MenuCommand Language</td><td>Command Language</td></tr><tr><td>Untrained User</td><td>Natural LanguageQ/A</td><td>Menu</td></tr></table>

A DSS generator, therefore, must have a subsystem called the User Interface Manager (UIM) to provide support to a variety of dialogue styles and responses. It must have dialogue processors (DP) to process different dialogue styles; such as a menu processor (MP) to process menu-type dialogues, a command language processor (CLP) to process command language dialogues, and a natural language processor (NLP) to process natural language dialogues. It must also have various response processors (RP) to provide responses on a variety of devices; such as a display processor (DIP) to provide responses on alphanumeric display screen, a hard copy processor (HCP) to provide responses on printer/plotters, and a graphics processor (GP) to provide responses on a graphic display screen. Further, it must have an interface monitor (IM) to monitor commands from user and interfacing them with the appropriate processor, to switchover from one dialogue processor to another at the user's choice, to monitor responses on appropriate devices as demanded by the user, and to communicate with other software subsystems of the DSS generator. The interface monitor must also support adaptive design of a specific DSS by permitting extensibility, i.e. addition of new commands, in the various dialogue/response processors.

## 3. The Representation Manager

Any activity in a decision making process takes place in the context of some conceptualisation of the information used in the activity. The conceptualisation may be mental, but in most cases it is physically represented on paper, display screen, etc. This is particularly important when the decision maker wants to communicate some aspect of the decision to another person. These representations could be a table, graphics (such as a bar chart or a piechart), or a defined procedure. They provide a context in which users can interpret DSS outputs and invoke DSS operations [2]. Also, decision makers have trouble describing a decision making process, but they do seem to rely on representations when making or explaining a decision [3]. Therefore a DSS generator should not require that decision makers be able to describe the decision making process before the specific DSS is built, but it should help decision makers conceptualise a problem through the representation most familiar to them. As decision makers learn more about their decision making process, they develop preferences for certain representations. Therefore, a DSS generator must support multiple representations.

Tables are well-known to many non-technical users as the simplest representation for data. Therefore, a DSS generator must use a DBMS to help in managing the DSS data base which matches this user's model of data. The relational data model is suitable as the conceptual data model for DSS data base management. Relations have structural similarities with matrices, which are the data structure used in several statistical, MS/OR modelling techniques. Also; relations can be implemented using a variety of simple to complex storage structures such as direct-access files, B-trees, multipaging, etc. Within the relational data model, in managing the DSS data base, the task of data base management reduces to table management. Thus, the DBMS of a DSS generator is software called the Table Manager (TM).

Graphics provides another familiar set of representations to DSS users, especially when decision making involves large amount of data and detailed reports or tables may inundate decision makers with information overload. Graphics helps DSS users in identification of problems and opportunities that require user action, and in lending credence to management presentations. In fact, graphics representations have become a requirement for an effective DSS. A DSS generator, therefore, should encompass the usual data analysis and business presentation graphics as well as allow the specific DSS builders to develop their own specialised graphics. It must have Graphics Manager (GM) software to support graphics representations, such as bar charts, histograms, line charts, scatterplots, piecharts, etc.

Decision makers may have to make similar decisions regularly with a recurring problem, but each time the conditions may be so different that no structured rules can be specified and they may have to use a DSS to support their decision making. In such a situation, DSS users may be able to use the DSS successfully through its command language interface and may conceptualise the sequence of these commands as a procedure which could be used to support decision making for the specific problem. Thus, successful command procedures are another representation which DSS users find valuable in their decision making tasks. A DSS generator, therefore, should provide the capability for storing and retrieving these command procedures as and when required by DSS users. It must, therefore, support a library of command procedures, or a command procedure base (CP base) and a command procedure dictionary (CP dictionary), which is a catalogue of these procedures, to manage command procedures in the CP base.

## 4. The Analysis Manager

Modelling in a DSS environment involves writing and executing instructions in the modelling sublanguage of the user interface; this may involve both data manipulation and mathematical modelling. In some cases, modelling may involve only the retrieval and display of a set of desired data achieved by a composite query; this may be defined as a command procedure and stored in the command procedure base. In the case of data manipulation and mathematical modelling, the set of instructions could be viewed as analysis subroutines which could be invoked by the DSS user. Therefore, in this conceptual model, the Model Base Management Software is referred to as the Analysis Manager (AM) subsystem. It performs a function similar to that of the DBMS (a counterpart of the Table Manager). It provides a flexible way to define (store), invoke (use) and delete analysis routines in the analysis base (the counterpart of the data base). In addition, it provides facilities to catalogue and access analysis routines; this is achieved by an Analysis Dictionary, a counterpart of Data Dictionary.

## 5. The System Manager

A DSS generator must accommodate decisions that are made by groups or in parts by several people in sequence. The DSS generator, therefore, should permit sharing of the DSS data base between different decision makers. Further, the decision makers must have confidence in the decisions supported by the DSS generator, which will depend on the integrity of the data analysis and data used to support it. Therefore, a DSS generator should have a software component called System Administrator, which should permit sharing of the DSS data base between different users and at the same time maintain its integrity and security. It performs the system administration function by maintaining data about authorised users and their authorisation for accessing and sharing the tables and analysis routines. This data is maintained in a set of tables called the Access Tables.

A DSS generator should provide control aids which help decision makers exercise direct, personal control. One type of control aids facilitate the mechanics of using the DSS generator, such as function keys, etc. Another type of control aids includes aids to support training and explanations for using the DSS generator [2]. These control aids include natural language error messages and a training method for using the system. A DSS generator, therefore, should have a software component called the System Trainer to provide user training. In its simplest form, this training could be provided by HELP command, in which the System Trainer can help the user by extracting appropriate descriptions, formats, examples of command usage, etc. from a set of HELP files.

A DSS is an adaptive system and the final system must emerge through an evolutionary process of design and usage. In this context, DSS designer/builder, DSS user and the DSS itself should be able to influence and learn from one another [5]. A DSS generator should, therefore, provide the DSS designer/builder feedback on efficiency/effectiveness of the specific DSS. It should also provide feedback to DSS users for them to evaluate their use of the DSS, and feedback to the designers of DSS generator to evaluate the usage and performance of the DSS generator for technical improvement. Therefore, there must be a Performance Monitor, which may gather performance data in the form of Performance Tables. The Performance Monitor may collect information on commonly used sequences of commands, relative frequency of command usage, response times for various commands, capacity of the system in terms of cost and response for DSS data bases of various size, and statistics of user errors. It may also permit users to record their comments on feature additions/modifications for future versions of a specific DSS and/or the DSS generator. It may also indicate the weaknesses in the design and implementation of the DSS generator itself by collecting statistics to indicate excessive modularity, excessive hash searching, high paging rate, high cost of data conversion, and expensive sorting. Thus the performance tables in a DSS generator may serve the role of the “black box” kept in the cockpit of aircrafts and will help in finding the causes of crashes in usage as well as design and implementation efficiency and effectiveness!

System administration, system training, and performance monitoring are the basic system management functions for any DSS generator. They constitute the System Manager (SM). As these functions need to be administered by a human being, the DSS generator should be managed by a “super-user”, who makes extensive use of these facilities in order to provide good support to users.

## 6. The Data Extraction Manager

Various levels of management use different types of data to support their characteristic decision making activities. Operations data are detailed, specific and precise. The data are aggregated and summarised to support middle management's tactical and control activities. These data are further aggregated and summarised, and are integrated with data from external sources to support top management's strategic and planning activities. Therefore, the DSS data base should be a front-end database, i.e. rather than using these data directly, they should be filtered or extracted into the DSS data base from the corporate and external data bases [4,6]. The Data Extraction Manager (DEM) subsystem is needed to load the DSS data base with external data and data generated internally into a corporate data base.

## 7. The Data and Other Dictionaries

The data base management function of a DSS generator needs a Data Dictionary to provide generalised access to its data base. It is a valuable catalogue of data [1]. It facilitates understanding and communication about the relationship between system applications and system data usage, and it assists in achieving data independence by permitting users to access data without knowledge of the location or storage characteristics of the data in the system.

The analysis base is a data base of analysis routines; therefore the Analysis Manager also needs access to an Analysis Dictionary for maintaining analysis routines in the analysis base. Similarly, the Graphics Manager needs a Graphics Dictionary. It shows the names of graphics stored in the graphics base, their types and entry points.

## 8. Working Data Base or Views

The DSS data base has several tables, often with different formats and possibly stored on different media. DSS users operate on the DSS data base to transform many of its tables into a form which is easy to analyse and used in decision support activities. The DSS users, using the data subsetting and aggregation operations, can select subsets of DSS data base, compute new columns (or attributes) using the subsets, and store subsets or new data in a working data base. This provides the user's view of the DSS data base. DSS users will often want to view the results of aggregation and subsetting operations without repeating these operations. The DSS generator, therefore, should facilitate creation and maintenance of the working data base for its users.

## 9. Language Systems

A DSS generator must provide a variety of sublanguages for different DSS functions. The language system should include:

a. a general access sublanguage

b. an analysis routine handling sublanguage

c. an analysis or modelling sublanguage

d. a data base sublanguage, and

e. a graphics sublanguage.

The general access sublanguage is used to handle user-system interaction. The analysis routine handling sublanguage is used in defining, storing and deleting analysis routines, invoking stored analysis routines, and specifying parameters for these routines. The analysis sublanguage is mainly used for modelling/data analysis and would be more algebra-like than command oriented. The data base sublanguage provides facilities for data definition and manipulation. Besides fundamental operational commands, it should also provide query-based commands for users to access the data base. The graphics sublanguage provides facilities for creating graphics, their storage and retrieval.

## 10. Implementation of a Prototype DSS Generator Based on the Conceptual Model

REGIMES (an acronym for RElational Generalised Information ManagEment System) is a prototype DSS generator whose system design is based on the conceptual design model formulated above. This prototype has been designed and implemented to demonstrate the technical validity and feasibility of the conceptual model. It has been implemented on the Sharp MZ-80B microcomputer using the Sharp BASIC language. Sharp MZ-80B is a Z-80A processor based system having two diskette drives (of 248KB each; the maximum possible number of drives is 4) and a dot matrix printer/plotter. Some of the features of the conceptual model, such as natural language question/answer interface, command procedure base and dictionary, Data Extraction Manager, and Performance Monitor, have been dropped in the prototype because of hardware limitations, and because the purpose was to demonstrate the feasibility of the model and not to develop a commercial product.

The User Interface Manager of REGIMES is called the Command Processor. It supports two types of user interface - menu and a query language based. There are two dialogue processors -

menu and query language, the two user interfaces. The query language supported by REGIMES is an English-like language called RELENG [9]. In addition, the Command Processor also supports a Display Interface for processing responses on the display screen, a Hard Copy Interface for processing responses on the printer/plotter, and a Graphics Interface for processing graphic responses both on display and printer/plotter. The Interface Monitor of REGIMES is called the Menu/QL Analyser as its main function is to analyse the type of command – whether it is menu or query language based, and submit it to the appropriate dialogue processor.

The Representation Manager supports tables and graphics. The command procedure representation is supported by REGIMES, as a user can define a command procedure. However, there is no facility in the prototype to generate a command procedure base because of hardware limitations. The Table Manager is called the Table Handler; it manages tabular representations. A table is a normalised relation. The Graphics Manager is called the Graphics Handler and supports bar-chart, histogram, line-chart, scatterplot, and piechart.

![](/api/attachments/26SE7U5E/fulltext/images/9f84bf1e7890ff1cf0e8ca274d2b46ca55115b2e87d83295f1d846fde3ec2283.jpg)  
Fig. 2. Architecture of REGIMES

The Analysis Manager is called the Data Analysis Handler. The prototype supports data analysis by providing basic statistical functions and regression analysis. Additional data analysis may be performed by adding new analysis routines to the analysis base of REGIMES.

The System Manager has the System Administrator and the System Trainer components. The Performance Monitor has not been implemented in the prototype, because of the hardware limitations.

The prototype has three dictionaries - data dictionary, a graphics dictionary, and an analysis dictionary, as described in the conceptual model. These are used for managing the DSS and working data bases, the graphics base, and the analysis base.

The Data Extraction Manager has not been implemented because the prototype was implemented on a stand-alone microcomputer which has no facility to communicate with other large machines supporting storage of large corporate and external data bases.

The architecture of REGIMES is shown in Fig. 2. It has been described in detail in [10]. REGIMES supports the adaptive design strategy, i.e. it permits the “final” specific DSS to evolve through usage and learning. Specifically, it permits additions/modifications of new commands and procedures through a “PERFORM procedure-name” command. This command enables the user to test the utility of a new command initially as a special procedure, which can be later added to the command list by entering it into the command table of the Menu/QL Analyser and adding processing routine to the menu and query language processors.

The implementation of REGIMES also demonstrates the fact that microcomputers provide a suitable and cost-effective system for implementing powerful DSS generators. Most DSS data bases are small in size and could be stored on the diskette drives available with the micros. Even if the data base is larger in size, it can still be stored on small capacity hard disk drives available with most micros. The implementation itself in a high level and popular language such as BASIC enhances the portability of the system to other micros.

Another advantage of using a microcomputer is that micros may be used individually by a single user or a group of users for implementing a specific DSS, thereby providing more direct control to the user.

Micros can also be linked as an intelligent node to other computers in a local area network, thereby providing access to large corporate and external data bases as well as special software packages. There are now a variety of software tools for transferring data between micros and mainframes $[7]$ ; this may facilitate implementation of a Data Extraction Manager for DSS generators.

## 11. Conclusion

This paper described a comprehensive conceptual design model for developing DSS generators. The model conveys a concept of multiple user interfaces and multiple representation of information. It also conveys a concept of shared data bases to enhance organisational communication and support group decision making. The model stresses consideration of the DSS data base as a front-end data base and the use of a data extraction manager to build DSS data base from internal corporate and external data bases. The technical validity and feasibility of the model has been demonstrated by implementing a prototype DSS generator (REGIMES) based on the conceptual model. The conceptual model and its prototype attempt to advance software technology in DSS field towards an independent architecture of DSS generators which could be used virtually in any application area.

## References

[1] F.W. Allen, M.E.S. Loomis, and M.V. Mannino, “The Integrated Dictionary/Directory System”, Computing Surveys, Vol. 14, No. 2 (June 1982), pp. 245–286..

[2] E.D. Carlson, “An Approach for Designing Decision Support Systems”, Data Base, Vol. 10, No. 3 (Winter 1979), pp. 3–15.

[3] E.D. Carlson, B.F. Grace, and J.A. Sutton, "Case Studies of End User Requirements for Interactive Problem Solving". MIS Quarterly, Vol. 1, No. 1 (March 1977). pp. 51-63.

[4] M.H. Ginzberg and E.A. Stohr, “Decision Support Systems: Issues and Perspectives”, in Decision Support Systems, M.J. Ginzberg et al (eds.), North-Holland, Amsterdam, 1982, pp. 9–31.

[5] P.G.W. Keen, “Adaptive Design for Decision Support Systems”, Data Base, Vol. 12, Nos. 1–2 (Fall 1980), pp. 15–25.

[6] M.E.S. Loomis, “The Nature of Database Management for Effective Decision Support Systems”, in Data Base Management: Theory and Applications, C.W. Holsapple and A.B. Whinston (eds.), D. Reidel, Dordrecht, 1983, pp. 155–174.

[7] B. Nash, “Micro-Mainframe Integration”, Proc. South East Asia Regional Computer Conf., SEARCC'84, September 24–28, 1984, Hong Kong, pp. 14.1–14.11.

[8] K.B.C. Saxena, “Design of a Computer-Based Management Decision Support System”, Unpublished Ph. D. dissertation, Gujarat University, Ahmedabad, India, 1985.

[9] K.B.C. Saxena, “Relational English – A Query Language Based on a Relational View of Data”, Proc. Sixteenth

Annual Convention of Computer Society of India, CSI-81, New Delhi, March 1–4, 1981.

[10] K.B.C. Saxena, D.V. Gulati, and M. Kaul, “Architecture of a Microcomputer Based DSS Generator”, Hong Kong Computer Journal, Vol. 1, No. 5 (May 1985), pp. 8–18.

[11] R.H. Sprague, “A Framework for the Development of Decision Support Systems”, MIS Quarterly, Vol. 4, No. 4 (December 1980), pp. 1–26.

[12] R.H. Sprague and E.D. Carlson, "Building Effective Decision Support Systems", Prentice-Hall, Englewood Cliffs, N.J., 1982.

[13] M.S.Y. Wang and J.F. Courtney, “Design and Implementation of the MAGIC/ROC Decision Support System Generator”, Proc. Second Int. Conf. on Decision Support Systems, DSS-82, June 14–16, 1982, San Francisco, pp. 37–49.
