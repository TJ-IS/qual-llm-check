---
otero_id: 16888
otero_key: "EWTYA6TE"
title: "An environment for development of decision support systems"
authors: "Nasir Ghiaseddin"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90028-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Environment for Development of Decision Support Systems

Nasir GHIASEDDIN

University of Notre Dame, Notre Dame, IN 46556, USA

As decision support systems gain widespread acceptance among decision makers, the demand for such systems is accelerated. The changing nature of DSS calls for a speedy development. However, the traditional system development techniques do not support the rapid development of such systems. This paper describes an environment for development of decision support systems. This environment offers a set of automatic and semi-automatic tools through which the speedy development of a high-quality DSS is greatly facilitated.

Keywords: Decision Support Systems, DSS, DSS Development, Prototyping, Development Language, Systems Analysis and Design, Module Management, Module Dependencies, Module Management Language.

![](/api/attachments/EWTYA6TE/fulltext/images/27440730fd87a45b96915c2df6f659330f3cd2cb54d49d9d5cb4bcedfa9ce953.jpg)  
intelligence.

Nasir Ghiaseddin is Assistant Professor of Management Information Systems at the University of Notre Dame. He received his B.S. degree in Mechanical Engineering from Arya-Mehr University of Technology, Tehran, Iran, his M.S. in Computer Science and his Ph.D. in Management Information Systems from Purdue University. His research and teaching interests are in the area of data base management, decision support systems, expert systems, and artificial

## 1. Introduction

Decision making by human beings involves highly complex processes. Understanding of human decision making behavior has been the subject of many studies by psychologists, decision scientists, and scientists in the field of artificial intelligence. Simon [15] proposes a three-stage model for the human decision making process: intelligence, design, and choice. The aim of Decision Support Systems (DSS) is to support the decision maker throughout the various stages of the decision making process through exploitation of a computerized information system. Decisions are classified by Simon as structured (programmable) or unstructured (nonprogrammable) depending on whether or not the decision making process can be described in detail before making the decision. A decision may be unstructured because of novelty, time constraints, lack of knowledge, large search space, need for nonquantifiable data and so on [5]. Until recently almost all existing computer support for decision making was for structured decisions, and little progress had been made in supporting semi-structured or unstructured decisions. It has been argued [9] that it is the semi-structured and unstructured decisions which are the greatest concern to decision makers. Therefore, Decision Support Systems must be capable of supporting the decision maker in his/her semi-structured or unstructured decision making activities. Donovan [6] describes the characteristics of problems to be solved through the use of a DSS as follows: (1) the problem is continuously changing, (2) the answers are needed quickly, (3) data are continuously changing and come from a variety of sources, (4) data must be processed into different kinds of data representations, and (5) when computer support is required, one is more concerned with rapid implementations than with long-term efficiency.

Decision Support Systems have shown to improve the productivity of the decision makers in their decision making activities, as well as increasing the quality of the decisions. Improvement in the quality of the decisions is possible because the decision maker can consider more alternatives before making a decision and also scientific models can be used in the formulation of various alternatives. It has been documented [18] that small improvement in decision making can result in high added profit. Such potential benefits, plus the continuous decline in computer costs have created an ever-increasing need for decision support systems. This need has accelerated the efforts in building more and more such systems. As potential benefits of decision support systems are being realized by more decision makers in various fields, the need for such systems will increase further.

This paper discusses the design of an environment for the development of decision support systems. We call this environment ‘The DSS Development System’ or DSSDS. In order to create an environment which supports the development of a successful DSS, we first study approaches which result in higher productivity in software development. The need for finding more productivity approaches in software development is currently a serious concern in software engineering. The reason for the seriousness of the software productivity problem is that in the past thirty years the cost of computer hardware has been steadily decreasing, while the cost of software development has been steadily increasing. Our interest in highly productive ways of software development is not only because of the economical gains, but also because the changing nature of DSS demands a speedy development process.

This paper discusses an environment for a D&S development process which enables the developer to develop high quality decision support systems of moderate cost within a relatively short period of time.

## 2. DSS Development Process

Development of a decision support system requires all phases of a system's life cycle; however, the iterations between various phases of the life cycle are happening at a much faster rate. In other words, since the problem space for a DSS is continually changing, modifications and extensions of a DSS should be regarded as a norm rather than as an exception. This certainly imposes a serious constraint upon the development process of a DSS. To deal with this problem we propose the following characteristics as essential features of any DSS development system (DSSDS) which is intended for the production of successful decision support systems.

(1) The DSSDS should support quick production of decision support systems.

(2) The decision support systems should be produced with inherent features of modifiability as well as extensibility.

(3) The DSSDS should support rapid modification and production of extensions to the DSS.

The imposition of the first requirement upon the DSSDS stems from a more profound reason than just the productivity gains. Since the problem itself and the user's conception and/or perception of the problem is continually changing, the DSS should be produced rather quickly. Otherwise, it will be obsolete as soon as the development process is finished. The second requirement simply states that the DSS should be built in such a way that it could be expanded (ideally indefinitely). The third requirement states that the rate of implementation of modification and extensions should be faster than the rate of generation of needs for new modification. Otherwise, the system will never keep up with the needs of its users and become obsolete very soon.

It is obvious that these requirements cannot be satisfied through the traditional system development process. There is a serious need for a more powerful facility to help satisfy these requirements. The design of such a facility will be discussed in later sections, but before that, another very important issue in the system development process must be discussed which is prototyping.

## 3. Prototyping

The key to the development of a successful system is the correct understanding of the problem by the developer. The understanding of the problem takes place in the analysis phase of the system's life cycle. At the end of this phase a formal writing of requirements specification is prepared by the analyst which must be reviewed and approved by the client before the design can begin. The importance of the requirements specification stems from the fact that experience has shown that errors in requirements specification are usually the last to be detected and the most costly to correct [2], [8]. The importance of this stage in the system's life cycle has been well understood from the early years in the field of systems analysis and design. To overcome the problems in requirements specification, various methods and tools have been developed to assist the developer in this stage of the development. The system specification tools such as Problem Statement Language (PSL) [17] and Requirements Specification Language (RSL) [1] will help the analyst in checking the consistency and unambiguity of the specification.

The main problem with these techniques is that they rely heavily on the user to verify the accuracy and completeness of the problems specification by looking at the formal specification of the requirements. It is often very hard for the users to visualize that what they see on paper will indeed solve their problems. Besides, many users, especially the DSS users, do not have a clear understanding of their true needs prior to actual utilization of the system.

A second group of tools realizing the potential difficulty of the users in verifying a printed specification of the requirements on paper provide graphical means to satisfy this purpose. Among these are Structured Analysis and Design Technique (SADT) [13], and SAMM [16]. Graphical representations are usually better understood by the user and provide a better picture of the system the way it has been understood by the developer and enhances productive feedbacks. However, the user never becomes certain whether a system will satisfy his/her true needs until he or she actually starts using it.

The understanding of the true needs of the user by the developer and the user him/herself can be greatly enhanced through the development of a prototype of the proposed system. With a prototype the user can more accurately examine whether the right problem is being solved and also if he/she has been understood correctly by the developer. Therefore, the answer to the two vital questions to the success of the system is provided with the most possible accuracy. By exercising the prototype, the user can provide vital feedback to the developer. This feedback could be used by the developer to finalize the requirements specification. By developing a prototype the developer also will experience the difficulties and potential problems in the development process.

Thus, it is clear that a prototype is a valuable learning vehicle both to the user and to the developer. However, in practice, prototypes are not built very often because of their high development cost and also because of the additional time required for their development.

These problems of prototyping could be overcome through utilization of a set of powerful tools which would facilitate a relatively cheap and speedy development of a prototype.

The DSS Development System to be discussed in the next section will, in fact, among other things, provide such tools. Note that the emphasis in prototyping should not be in producing a very efficient system; rather, the emphasis should be on rapid production of a prototype which accurately reflects the requirements of the proposed system in the manner perceived by the developer. A word of caution concerning the development of prototypes is in order: it is often necessary to make changes in the prototype in order to observe the user's reactions to modified versions. These changes should be stopped the moment no new knowledge can be learned from modification, or the cost of modification outweighs the benefits gained from it. In any event, the temptation to carry on the development of the prototype in order to turn it into the delivered system should be strongly resisted.

Prototyping in no way conflicts with the use of other systems analysis tools and techniques. In fact, we propose that tools should be provided to the developer to help capture pertinent information from the user. This information should be stored in an organized way in a data base. Automatic checking of the consistency and completeness should be performed on the data, and finally, tools should be provided to the designer so he/she can retrieve the pertinent data for each operation both quickly and in a convenient format. The developer can use this information to build a prototype with an acceptable level of accuracy for examination by the user. The requirements specification is finalized when the user is convinced the proposed system will indeed satisfy his/her needs.

## 4. The DSS Development System

The DSS Development System (DSSDS) is an environment for the development of decision support systems. The environment consists of a collection of highly specialized tools to be used by the DSS developer throughout the development process in order to facilitate the development of a successful system. The DSSDS will increase the productivity of the developer and help him/her to produce a DSS based on the true needs of the user at a moderate cost. The philosophy of the DSSDS is based on two very simple, but also very important concepts: (1) the use of highly automated tools throughout the development process and (2) the use of prefabricated pieces in the manufacturing of a whole piece whenever it is possible. The first concept increases the productivity of the developer in the same way an electric saw improves the productivity of a carpenter over a hand saw. The second concept increases the productivity of the developer analogous to the way a prefabricated wall increases the productivity of the carpenter in building a house.

Although many of the tools that DSSDS provides could be used in the development of any application system, our emphasis would be towards tools which are helpful especially in the development of a DSS. By specialization we expect to gain efficiency in the development process on the grounds that there will be a real need for the development of many decision support systems in the future. Design of any large system for the first time is a major task. In order to insure the success of the system, it is not recommended to design a gigantic system at the start in the expectation of supporting the development of every detail of the system. Rather, in the design of a DSSDS we follow the evolving characteristic. Namely, we think that a nucleus DSSDS should be first designed and developed to support the essential needs of the developer. However, the system should be extensible so other features could be added to the system when the need for them becomes apparent. Nevertheless, the DSSDS should have the following characteristics:

(1) The DSSDS should support the development of a successful DSS.

(2) The DSSDS should support the development process throughout the entire life cycle of the system, that is, it should support capturing of the requirements from the user, development of the prototypes, design and implementation of the delivered system, testing, and finally the maintenance of the DSS.

(3) The DSSDS should support the development of different decision support systems in different programming languages and possibly for different target computers.

(4) Various tools of the DSSDS should be relatively easy to use and independently available.

(5) The DSSDS should be capable of evolving over time.

The independence of various tools in this context implies only the functional independency; however, coordination of various tools is essential. The evolving feature of DSSDS here means that the system should allow new tools to be added to the system as well as allowing old tools to be improved or replaced by more advanced tools.

## 5. An Overview of DSSDS Environment

The DSSDS environment could be thought of as a workshop with many tools and prefabricated parts that the developer can use throughout the process of building a new DSS or to upgrade or repair an existing DSS. The environment of the DSSDS is shown in fig. 1. The developer is provided with a Development Language (DL) which is basically a powerful command language. Modules can be written in command language or any other programming languages such as FORTRAN, COBOL, PASCAL, etc. By module in this context we mean any set of executable lines of code which has a name, and is written to do a certain job. A module can be used independently, or it could be used in conjunction with other modules to build a more complex module. A module can do computation, perform read and write operations, transform data, or perform any other computer operations in order to achieve a certain objective.

In addition to the development language, a number of other facilities are available to the developer. These are Systems Analysis and Design Facility (SADF), a Module Management Language (MML), a Screen Management Language (SML), a Source Code Manager (SCM), a Report

![](/api/attachments/EWTYA6TE/fulltext/images/6a9715aeb5014c3e1ca3deeb05145c6f7123e6cf0a7ccac6d0a401956d7f7953.jpg)  
Fig. 1. An Overview of the DSS Development System (DSSDS).

Generator (RG), a Graphics Generator (GG), and a Request Handler (RH). Each of these facilities could be used through the command language or independently.

## 5.1. The Development Language (DL)

The Development Language is a command language. Its function is to provide a host to other facilities, as well as providing a collection of useful functions to be used by the developer. Individual commands or procedures written in MML, RG, GG, etc. can be invoked from the DL. The command language provides an interface between modules written in various facility languages (i.e., MML, RG, GG, etc.) as well as modules written in programming languages such as FORTRAN, COBOL, PASCAL, etc. In this way the developer can write a program in which its components are written in different programming languages and/or use various development facilities. For example, to create a plot of the predicted sale for years YR1 to YR2, the following program can be written:

RETRIEVE (SALE, YR, R10)
CALL REGRESS (SALE, YR, COEF)
CR FYR (10) = YR1 TO YR2
CALL FORECAST (COEF, FSALE, FYR)
GG. PLOT (FSALE, FYR)

The first line is intended to retrieve the sale values with the corresponding year values (YR) for ten most recent years (R10). The second line will run a regression on sale as a dependent variable against YR. Then, variable FYR is defined to be an array with values YR1 to YR2. The fourth line runs a forecasting model using the coefficients produced in line two. Finally, line five invokes the command PLOT from the Graphics Generator (GG) to plot the predicted sale against the future years.

By being able to create a program in which its components are written in different languages, we benefit in two ways: first, each component can exist in its most efficient form. That is, each module can be written in a language which is most suitable to its function. Second, more productivity can be gained by using many existing modules which are currently available in different programming languages. The purpose of this paper is not to discuss the syntax or semantics of the command language. Rather, it is to present the concept of such language. A sample of some other commands is shown in table 1.

Note: although many features of the Development Language (DL) resemble those of a functional language [10], DL is not a true functional language. One important feature of DL is that it will allow for the components of a new module to be written in different programming languages. In other words none of the components need to be a functional program.

## 5.2. Systems Analysis and Design Facility (SADF)

Development of a DSS, like any other system, starts with analysis. The aim of the system analysis phase is to gather enough information about the needs and operations of the system so that any qualified data processing professional, by reviewing this information, will be able to understand what the needs and requirements of the new system are and what it is supposed to do. The purpose of the Systems Analysis and Design Facility (SADF) is to help in the soliciting of pertinent information from the user, to store and organize this information in a data base, to check the consistency of the information and to make it available to the developer in a useable form.

Table 1
A Sample of Features of the Development Language.

<table><tr><td>CREATE x</td><td>Create a file and call it x; if x is not present, a working file is created.</td></tr><tr><td>STORE x</td><td>Store file x. The system will prompt for the location of the file and security feature. The default for x is the current working file.</td></tr><tr><td>SAVE</td><td>The system will save the entire work of the session, as it is, so it can be continued at a later time.</td></tr><tr><td>RECREATE</td><td>The system will recreate the working environment as it was left off in the last session.</td></tr><tr><td>EXECUTE x, (C = comp, I = data, 0 = y)</td><td>The system will send module x to computer ‘comp’ to be executed using file ‘data’ as input file, and sending the output to file y. Defaults are the main frame computer and terminal input/output, respectively</td></tr><tr><td>EXTRACT x, y, type</td><td>Extract file x and place it on file y. Type can assume values M or D for module and data. If system is unable to find the location of x, prompts for help.</td></tr><tr><td>RETRIEVE (x, y, z,..., pi)</td><td>Retrieve i instances of variables x, y, z, etc. P = R (recent), F (first), or A (all).</td></tr><tr><td>CR x(m) = i, j, k...</td><td>Create a vector of length m and initialize its values to i, j, k, etc.</td></tr><tr><td>CR x(m) = i to j</td><td>Create a vector of length m and initialize its elements to values from i to j.</td></tr><tr><td>CR x(m, n) = i11, i12,...,iθσ</td><td>Create a table and initialize its values row by row to i11,...,iθσ. If no values are given, the table is created but is not initialized.</td></tr><tr><td>IF (exp) command</td><td>Conditional execution of a command.</td></tr><tr><td>DO WHILE (exp)</td><td>Looping while ‘exp’ is true.</td></tr><tr><td>⋮</td><td></td></tr><tr><td>end</td><td></td></tr><tr><td>DO FOR i = j, k</td><td>Looping</td></tr><tr><td>⋮</td><td></td></tr><tr><td>end</td><td></td></tr></table>

Development of any nontrivial information system generally requires the participation of many people. One problem facing the development of such systems is to document the important communications among these participants so that at each point in time it is clear what decisions have been made in the handling of each component of the system. SADF will store these communications in a network data base and will relate them to the originator of the comment as well as to the component for which the comment is issued [fig. 2]. This information is available to all participants in the development process and it could be accessed by simple commands or queries.

In the course of system development, although some of the necessary information for the formulation of system requirements can be captured from existing systems or existing documents, the ultimate source of the information is the user.

![](/api/attachments/EWTYA6TE/fulltext/images/1d122dd4d75c608514d11a62ab155eaeb8913cb225453395bef0d9c9106ba115.jpg)  
Fig. 2. Extended Network Logical Structure of SADF Data Base.

However, different users have different needs and viewpoints which sometimes are in conflict. In any case, all viewpoints should be heard and all reasonable needs should be accounted for according to some priority list. SADF stores this information in an extended network data base [4] along with other information pertaining to analysis and design of the DSS.

A part of the requirements will be obtained from the user by a program which will interview the user in a conversational mode through an interactive terminal. This could be easily accomplished by a questionnaire designed especially for solicitation of information from the user. However, instead of a human interviewer, the computer will conduct the interview through an interactive terminal. Questions will be presented to the user, and answers obtained and stored in a data base. After interviewing all users, a summary report will be produced and the results stored internally so they can be viewed by the analysts, designers, programmers, etc. An automated interview usually is not enough for capturing all requirements, however, it can help the analyst by revealing the problem areas for more extensive study. In any event, all obtained information will be stored in an extended network data base [fig. 2]. This manner of storing the information facilitates effective use of the information as well as providing an excellent means of documentation [7].

The DSS Development System allows simultaneous development of several projects by one or more developers. Each project is assumed to consist of one or more subsystems [fig. 2]. During the analysis phase, each subsystem is divided into several components. Each component, in turn, can embody other components, and this hierarchy can continue as many levels deep as necessary. This association among various components is represented by the set 'Embed' in fig. 2. This arrangement provides an excellent means for structured analysis, as well as providing a convenient way of storing the obtained information during the analysis phase. Each component is associated with many occurrences of the record type 'DETAIL', which is arranged according to the level of detail. The 'USER' record type represents the user in its broad sense. That is, the user can be an individual, a department, the government, etc. Each user can demand some requirements or may impose some constraints on each component. Since requirements and constraints sometimes are not very rigid, it is important to know who demands a particular requirement or imposes a given constraint. Thus, by negotiating with the involved users, a compromise among conflicting demands could be achieved. Fig. 2 captures this information as an inherent part of the data structure. The record type 'COMPONENT' is associated with record type 'DATA ITEM' through two sets. Set 'Get' relates each component with its input data item types. This is a M:N relationship. Set 'Give' relates each component to its outputs. This is a 1:N relationship on the grounds that there should not be any redundancy in data production. Note that this arrangement captures the situation where a data item could be the output of one component and the input of another component. The record type 'DATA ITEM' is associated with 'INPUT SOURCE' to document the origination source of a given data item. The input source is, in turn, associated with the user who provides it. The record type 'DATA ITEM' is also associated with the record type 'OUTPUT REPORT' to show in which output report(s) a given data item type appears. The occurrence of each output report is associated to its potential users through the set 'Use', and to the module which produces it through the set 'Generate'.

The record type ‘DEVELOPER’ represents all the members of the development task force, that is, the project manager (is related to project through set ‘Manager’), the supervisor of a subsystem (is related to subsystem through set ‘Supervise’), the analyst in charge of component (is linked to component through set ‘Analyze’), or the person responsible for the development of a module (is related to the record type ‘MODULE’ through the set ‘Implement’).

During the course of a system development, task-related communication is often oral or is written on a piece of paper which will disappear after its usefulness is diminished. However, it is important to document important communications so that the rationale for a particular way of handling a case or the reason for the departure from the norms may be understood by the person who will maintain the system in the future. These communications could also be stored in the SADF data base and are related to both the originator of the comment and the subsystem and/or component in question.

Record type 'COMPONENT' through its recursive set 'Embed', provides an effective structure for storage of information during a structured analysis process. The structure represented by record type 'COMPONENT' is the conceptual structure of the problem the way it has been seen by the analyst during the analysis phase. However, the structure of the designed system is very likely to be different. The structure of the designed system will be stored in the data base with 'MODULE' representation. Here each subsystem can branch into several modules, and each module can in turn contain other modules, and this process can recursively continue as many levels deep as necessary. This recursive association of modules is represented through the use of $M: N$ set 'Contain'. Note that here the association is many to many because each module may contain many modules, and each module may be contained in many higher level modules. This arrangement provides an excellent means for representation of structured designs and storage of information about individual modules and their association with other modules as well as identification of their input/output data elements. Each module is related to its input data elements through set 'Receive'. This is an $M: N$ association meaning that each input element may be used by many modules, and each module may use many data elements as input. Set 'Produce' relates each module to its output elements. Here again, the case that some data elements may be output from one module and input to other modules is effectively handled. Treatment of input/output data elements in this way provides the precedence association among modules quite naturally because this information is implicitly stored in the data base.

For example, in fig. 3 modules x, y, and z at first seem to be independent because none of them is a module of others. However, investigation of input/output dependencies reveals that there is a precedence relationship among these modules. That is, module x should be executed first, y second, and z third [fig. 4]. This is because x uses data elements a, b, and c as input and produces d, e, and f as output. Module y uses d (an output of x), g and h as input, and produces i, j, k, and l as output, and finally, module z uses f (an output of x) and l (an output of y) as its input to produce m and n as its output.

The relationships of data items with components, modules, input sources, output reports, and data base record types can be used by SADF to check the completeness and consistency of the data. To check the completeness, all the components (at the end of the analysis phase) and all the modules (at the end of the design phase) must have inputs which come from an input source, from the data base, or from a preceding component/module. This can be easily done by drawing a precedence diagram using the following algorithm:

![](/api/attachments/EWTYA6TE/fulltext/images/b8397737c1b6daf468bcb1de3fb48dd21649f6bce182c0b9a262330990c043d3.jpg)  
Fig. 3. Implicit Precedence Relationship Between Modules x, y, and z Imposed by Input/Output Data Items.

Step 1. Find all modules whose inputs come from either an input source or from the data base.

Step 2. Find all modules whose inputs come from an input source, from the data base, or modules which were explored in previous steps. If no such module can be found, go to Step 4.

Step 3. Go back to Step 2.

Step 4. If all modules are accounted for, identify all data items which were not used by any module as unused data. If some modules are left untouched, identify them as the ones with an unknown source of inputs.

![](/api/attachments/EWTYA6TE/fulltext/images/80d4cf45bc43375189c1056bc549682ff01a02cfec21b73b0883e0303a7424e0.jpg)  
Fig. 4. Precedence Relationship Between Modules x, y and z.

The association of components and modules with data should be consistent. The consistency of this association could be checked by SADF. For example, in fig. 5, module (or component) x uses data items a, b, c and i (an output of module y) as its input to produce d, e, and f as its output. Module y, on the other hand, needs d (an output of x), g and h as its input to produce i, j, and k as its output. If no additional information is given, this is an inconsistency because x needs the output of y to work, and y needs the output of x to work. However, if it was meant for i to be the output of y from the previous cycle, then this conflict could be resolved by specifying the data base to be the origin of the input variable i (which is initialized to some value at the beginning), and by giving a different name (i.e., $i_{1}$ ) to the new value of this variable as an output of y [fig. 6]. Note that this treatment is necessary to resolve the conflict because i and $i_{1}$ are not really the same variable; $i_{1}$ is the new version of i.

![](/api/attachments/EWTYA6TE/fulltext/images/36e284c1b75768a3bb44dbecfb23408e7328c4d1d465adca1a35295d5dfdc3e4.jpg)  
Fig. 5. Deadlock in Precedence Association Between Modulus x and y.

Discussion of the make-up of each record type is outside the scope of the present discussion. However, for the sake of example let us consider the contents of record type 'MODULE'. This record type consists of the following information:

Module name
Purpose (what does it do)
Major technique to be used
Implementation status (finished, tested, etc.)
Date implementation started

![](/api/attachments/EWTYA6TE/fulltext/images/3f9db9b2214b3aa8f996fe61f4003d341dbfbaba9b004b554d96eca42dc1c3f1.jpg)  
Fig. 6. Resolution of Deadlock in Precedence Association Between Modules x and y.

Data expected to be finished
If delayed, reason for delay
Programming language to be used
Performance requirement
Which machine it should be built for
How often it would be used
:
etc.

Some of the informational content of the data base can be used for project management. Namely, since the information about 'Who is responsible for what', plus the information about the development status and major problems encountered are all stored in the data base, the project manager can use this information for the purpose of monitoring the progress of the development process. Of course, it is obvious that any change in the status and other informational content of the data base should be reflected in the data base by the individual member of the development team who causes the change, or the person who notices the change first.

After completion of the development process the information in the data base can serve as the documentation of the system and can be moved to a history data base or dumped on a tape. This tape can be reloaded whenever needed for the purpose of modification or other maintenance activities.

By having a network data base management system as a mechanism for information organization, the implementation of SADF is greatly facilitated. Moreover, the facility can easily evolve over time. A set of basic commands for a nucleus SADF are identified in Table 2. Note that many of these commands could be implemented using the data manipulation language (DML) of the Data Base Management System (DBMS) in some host language. The user can also use the query language of the DBMS to retrieve the information or manipulate the data within the data base. However, if the user feels that he needs to do certain data manipulation activities over and over again, he can create macro commands and add them to the system's library or his/her own personalized library. Therefore, the system can both evolve and become personalized over time.

The language of SADF is intended to be interactive and conversational. For example, if the user types the command 'ADD PROJECT', the system starts to ask about the informational content of record type 'PROJECT' (i.e., the name of the project, the client, etc.). Then the system continues to ask about who the project manager is, what the individual subsystems are, etc. There is no need for the user to give all the information at once. The progression of the conversation could be stopped at any point and unknown information be added later when it becomes available. Note that since we have a fixed structure for the data base, a conversational language could be effectively implemented. This is true because all the alternatives are known and enumerable. The system can resolve ambiguity and directs its path-finding activities by asking questions from the user.

Table 2
Basic Commands for SADF.

<table><tr><td>ADD</td><td>to add a new project, a new developer, a new module, etc.</td></tr><tr><td>DELETE</td><td>to delete a project, a subsystem, a constraint, etc.</td></tr><tr><td>CHANGE</td><td>to change data items within a particular record occurrence of a given record type of SADF data base.</td></tr><tr><td>PRINT</td><td>to print selected data elements from a given occurrence of a given record type.</td></tr><tr><td>PRINT ALL</td><td>to print all data elements from a given occurrence of a given record type.</td></tr><tr><td>LIST</td><td>to list selected elements of all members of a given owner of a particular set.</td></tr><tr><td>LIST ALL</td><td>to list all elements of all members of a given owner of a particular set.</td></tr><tr><td>TEST COMPLETENESS</td><td>to test if all data needed by modules (or components) have so source for providing them.</td></tr><tr><td>CHECK CONSISTENCY</td><td>to check if the precedence relationship creates no deadlocks.</td></tr><tr><td>PROGRESS REPORT</td><td>to create a progress report for a project, subsystem, or a major module.</td></tr></table>

## 5.3. Module Management

One way to achieve high productivity in the process of software development is to use prefabricated pieces in the construction of a new system. The use of preprogrammed modules in the manufacturing of a new system not only increases the productivity of the software development process, but also increases the opportunity for producing a higher quality software. Production of higher quality software is possible in two ways: First, the frequently used modules can be fine-tuned to perform very efficiently. That is, these modules can be written in assembly language or they can be written by highly skilled programmers. Second, since preprogrammed modules presumably have been in use in other systems and environments they have been perfected. Also, the performance of these modules in actual practice has been observed; thus, their strengths and weaknesses are better known. Therefore, the developer is building his/her system with a better known material, so it is expected that a better system will be produced. However, in practice, the use of prefabricated pieces in the development of a new system is negligible, unless the same person is developing a similar system. The main reasons for not using the product of previous efforts in the development of a new system can be classified under the following categories:

(1) Inflexible design. The module does not directly fit the current need, and inflexible design does not permit easy modification of the module.

(2) Different programming language. The module is written in a different programming language with no interface to the language used for the system development.

(3) Machine dependence. The module is written for a particular machine and cannot be used on other machines.

(4) No organized information about the existence of the module exists. The modules are scattered in various places (e.g., files, tapes, computer cards, etc.). No one knows about their existence or there is no convenient way of getting information about them.

(5) Lack of documentation. The existence of the module is known, but there is lack of documentation. The author is either unknown or no longer with the organization; therefore, no one is sure how to use the module.

(6) Lack of information about reliability of the module. The developer simply cannot trust someone else's product without having some evidence about the reliability of the product.

(7) Lack of performance data about the module. There is no evidence which would indicate how the module performs in a practical situation.

(8) Lack of information about the implicit assumptions under which the module will operate properly.

If we are able to find a solution to the above problems then we can expect to produce quality software with high efficiency and with reasonable cost.

The first problem calls for flexible design. Flexible design under the DSSDS is possible. Modification of a module through Source Code Manager (SCM) is also greatly facilitated. The second problem is solved under the DSSDS development language (DL) since DL provides an interface to several programming languages and any program written in DL can call modules of different programming languages. The third problem is less severe because most programs written in high-level languages are portable. However, there are several ways to solve this problem. If there is a complete program it could be routed to the right machine to be executed and the results transmitted to the originator of the problem. If the number of machine-dependent modules is considerable, a virtual machine (a simulation of another machine on an existing machine) could be developed to run these modules. Translators could also be written to translate programs of a given machine to another. The first solution is supported by DSSDS. The others could be designed and added to DSSDS if economically justifiable.

In the following sections we present a solution to problems no. 4 through no. 8. In order to solve these problems we will create a centralized information base containing all necessary information about all modules available to the software development center. This centralized information base could be used by individual members of the development team in order to select the appropriate modules to be incorporated in the development of the new systems.

To centralize all pertinent information about various modules, we have designed an extended network [4] data base system called 'The Library of Modules' (LOM). We will show how this library can be used to assist the developer in the task of module selection, as well as providing him/her with pertinent information in each problem area.

Our interest in preprogrammed modules is not stimulated solely by productivity gains and production of quality software. In the development of a DSS we need to supply the DSS with a collection of modules to be used by an automatic problem processing system as defined in $[3]$ and/or the decision maker for model building activities. Therefore, we consider the Library of Modules to be an essential part of our DSSDS.

## 5.3.1. The Library of Modules (LOM)

The Library of Modules stores all desirable information about available modules in a centralized fashion. The developer, after designing his/her system, can turn to the module library to see which of the existing modules could be used in the development of the new system. If none of the modules can be used directly, the developer may then investigate whether or not any of the modules can be used with minor modification. If the module library is large enough, it is reasonable to assume that some modules will be useful in the development of a new system. This will help a speedy development of a new system which we consider an essential requirement for the development of decision support systems. This approach also provides an opportunity for developing high quality software with reasonable cost.

The logical structure of an extended network data base along with a proposed list of data items is shown in fig. 7. Modules are categorized by the problems they solve and problems themselves are categorized by subject area. There may be more than one module for solving a given problem and a given module may solve more than one problem (N: M relationship). Information about the name of the module, module number (similar to the call number for books), the purpose (what does it do?), technique used and origin (where did it come from?) is stored for each module. The record type 'THEORY' is intended to represent the scientific basis for the technique used in the development of the module. The developer can check to see if there is a sound scientific basis for the technique,

![](/api/attachments/EWTYA6TE/fulltext/images/4a11d61d37e3c9cdb83b83c105ffda3596947ebaeb273f7bc33304c9d00bbc05.jpg)  
Fig. 7. An Extended Network Structure for Library of Modules.

and if so, can educate him/herself and learn about the conditions under which the technique is valid. In other words, it does the job of a handbook. This can be very helpful since the developer is not necessarily knowledgeable in all problem areas. For each 'THEORY' a number of references are also given in case they are needed. Each module may have many variations (e.g., different versions for different computers). Each record occurrence of the 'MODULE VARIATION' record type contains the properties of a specific variation [fig. 7]. Some explanations of these properties are in order: 'Major Difference' is an explanation of the major difference between this version and the original version of that module. Memory requirement gives the size of the program in bytes and it is especially helpful when there is a memory restriction. Reliability and performance data essentially tell how reliable the module has been and how fast it runs. The other information includes restrictions of that variation, where it can be found, how it should be accessed and what the calling procedure is. The record occurrence of each particular variation is associated with the system project(s) in which it has been used. For each project the name of the project manager and client as well as the name of the project and date of development are given. Therefore, if the developer wants additional information about the development process or practical results he/she can contact the appropriate person. Each occurrence of record type 'LANGUAGE' is related to all modules which are written in that particular language. Thus, it is possible to find out in what language a particular module is written and to scan through all modules written in a given language. Some variations of a module may be written for a particular computer so the record type 'COMPUTER' is related to record type 'MODULE VARIATION' through the many-to-many set 'Written for'. Each module variation is linked to its input/output through the set 'I/O'. Properties of each I/O variable are stored in an occurrence of 'I/O VARIABLE'. The I/O codes of I, O, or B correspond to input variables, output variables, and both, respectively. Other data items of I/O variables are shown in fig. 7. Each module is linked to its programmer and each variation is linked to the programmer who did the modification. For each programmer the name, phone number and address are given so that additional information can be obtained from the programmer if necessary.

Thus, the Library of Modules (LOM) directly or indirectly (through references, addresses, etc.) includes all the information that the developer would like to know about a particular module. Another interesting feature of LOM is the set relationship ‘Needs’ which will be discussed in the following section.

## 5.3.2. Module Dependencies

Within a system it often happens that the output of a module is used as input by another module, therefore creating a dependency between the two modules. We call this dependency between two modules a 'context-sensitive association' or a 'weak dependency' because the association is the result of input/output needs rather than the result of a direct need of one module to another. The dependency is context-sensitive because it very much depends on the context. For example, module x in a given system needs the output of module y in order to work. However, in a different context (i.e., a different system) this may not be the case, because the input of x may be provided in another way (e.g., be simply read in).

In contrast to this dependency there is another kind of dependency which we call 'strong dependency' or 'context-free association'. A strong dependency is the result of one module calling or invoking another module. For example, if module $z$ calls for the service of module $y$ in its procedure, then we say $z$ has a strong dependency to $y$ because $z$ cannot function unless $y$ is present; $y$ in turn may have strong dependency to another model. In fig. 8, module $z$ has strong dependency to $w$ , $x$ , and $y$ ; $w$ in turn has a strong dependency to $q$ and $r$ ; $x$ is strongly dependent on $s$ , $t$ , and $u$ , and $s$ in turn has strong dependency to $p$ ; and finally, $y$ is strongly dependent on $v$ . These dependencies are context-free because no matter in which system we use model $z$ , it needs modules $w$ , $x$ , and $y$ in order to operate. Modules $w$ , $x$ , and $y$ in turn need the service of their own modules. This hierarchy continues until all the new modules stand alone and are self-sufficient.

![](/api/attachments/EWTYA6TE/fulltext/images/d9740bf4b3589d26c3651e6543d862a4da517e2e05aece608263d22178f9bfde.jpg)  
Fig. 8. Strong Dependencies Between Modules.

This strong dependency of a module to other modules is effectively captured by the recursive relation 'Needs'. This is a M:N relationship because each module may need the service of several other modules, and also each module may give service to many modules. Treatment of module dependencies in this way greatly facilitates the development of new systems as well as modeling activities. Notice that if module z is selected to be included in a new system, all the modules which z is depending upon for their service in a direct or indirect way should go with module z.

The linkage through set ‘Needs’ provides valuable information to the developer. For example, if a module like z is a candidate for selection the developer can scan through all other modules which are directly or indirectly needed by z and examine their properties such as performance data, reliability measures, the language they are written in, hardware dependencies (if any), etc. Examination of this information is important because it may reveal some undesirable properties by one or more modules in the collection. This may require the rewriting of those modules or selection of an alternative module. Another valuable benefit of this approach is that through this linkage the developer can find out which modules use the service of a given module in a direct or indirect way. Therefore, should that module be altered, it would be very easy to find out which modules will be affected and, thus, appropriate measures could be taken if necessary.

A third advantage of this approach is that it eliminates redundancy in the storage of modules.

In other words, each module is stored only once, no matter how many other modules use its service.

Other consequences of this approach are that the system can evolve and/or become personalized. The evolution is possible because new independent or dependent modules could be added to the system with no difficulty. The developer could also use the original primitive modules and build upon them a collection of modules which would be used by him/herself on a personalized basis.

The system can also display a learning behavior. Observe that the set of modules which is directly needed by a module such as z could be considered as a precondition to z, because without it, z cannot be executed. However, existence of a module in the data base of the LOM automatically means that the preconditions are satisfiable and in fact the linkage paths represent the solution paths to satisfy the preconditions. Any time a new problem is solved, that is, a new module is formulated with or without the use of existing modules, this new information is added to the system. This problem need not be solved again because the solution path to this problem already exists in the data base. Thus, the system displays a learning behavior. Moreover these new skills are acquired in the area where the system has been used and, presumably, are needed the most. In other words, the system learns the right things. A final comment on the learning feature is in order: If the original collection of the primitive modules is considerably large, chances are that most of the new modules can be created through the use of the existing modules. It is the job of a human or computerized problem-solver to combine the right ingredients to create a module which would deliver the desired results for a given task. It is expected that most new modules would be the result of combining the existing modules or using some parts from the existing modules rather than being created completely from scratch. Different schemes should result in different environments which are best suited to different lines of development.

## 5.3.3. Module Management Language (MML)

The Library of Modules contains information about any module which is accessible through the development environment. The source code of these modules may be stored in source code files under the Source Code Manager (SCM), or stored in other files, even under other computer systems. No matter where the location of the module is, all the information about its properties, location and the procedure for accessing it is stored in LOM. To use this information the developer needs a collection of tools so he/she can easily scan through the information in the library and select the desired modules. After the selection of the modules the developer wants to copy the module itself plus its supporting modules to an appropriate place to be included in the new system with or without some modifications.

The use of a network data base management system for the Library of Modules automatically provides the developer with a powerful tool for retrieval and manipulation of information in the LOM. The user can use the query language of DBMS, question the informational content of the data base and/or manipulate the data. The developer can also develop a set of macro commands that he/she will use repeatedly. Nevertheless, the existence of a Module Management Language (MML) will greatly facilitate the job of the developer. A set of basic commands are shown in table 3. Additional commands in the form of macros can be designed by the developer on a personalized basis and be added to the system. The MML is intended to be conversational in the sense that any ambiguities may be resolved through conversation with the user.

## 5.4. Other Development Facilities

In the design of the foundation of DSSDS we implicitly assumed that a data base management system exists. Moreover, we based our design on a network data base system. Although it is possible to design a DSSDS without a data base management system, existence of a DBMS greatly facilitates the design and implementation process. Besides, since the DSSDS normally would be used in a development center, existence of a DBMS in such a center is unquestionable. We also assumed a query language does exist which would work with the data base system.

In fig. 1 the existence of a Report Generator (RG), a Graphics Generator (GG) and a Screen Management Language is recognized. We do not intend to discuss these facilities on the grounds that these facilities do exist in a variety of forms.

Table 3  
A Set of Commands for Module Management Language.

<table><tr><td>ADD $\langle rt \rangle$ </td><td>to add a new occurrence of record type ‘ $rt$ ’ in the data base</td></tr><tr><td>DELETE $\langle rt \rangle$ </td><td>to delete an occurrence of record type ‘ $rt$ ’ from the data base</td></tr><tr><td>CHANGE $\langle rt \rangle$ </td><td>to change data item(s) within record type ‘ $rt$ ’. (The system prompts for additional information.)</td></tr><tr><td>DISPLAY $\langle rt \rangle$  $\langle x \rangle$ </td><td>to display the informational content of occurrence  $x$  of ‘ $rt$ ’</td></tr><tr><td>DISPLAY $\langle rt \rangle$ . $\langle y \rangle$ , $\langle st \rangle$ </td><td>to display the informational content of record type ‘ $rt$ ’ for all members (or owners) of owner (or member)  $y$  of set  $st$ </td></tr><tr><td>DISPLAY $\langle rt \rangle$ </td><td>to display all occurrences of  $rt$ . (“SYSTEM” is assumed to be the owner, otherwise, system prompts for the owner.)</td></tr><tr><td>DISPLAY OWNER $\langle rt \rangle$  $\langle x \rangle$ . $\langle st \rangle$ </td><td>to display owner(s) of occurrence  $x$  of record type  $rt$  through set  $st$ </td></tr><tr><td>DISPLAY MEMBER $\langle rt \rangle$  $\langle x \rangle$ . $\langle st \rangle$ </td><td>to display all members of occurrence  $x$  of record type  $rt$  through set  $st$ </td></tr><tr><td>DISPLAY SUB-MODULE $\langle x \rangle$ . $\langle it \rangle$ </td><td>to display the value of item type ‘ $it$ ’ for all submodules directly needed by  $x$ . if ‘ $it$ ’ is missing all items will be displayed</td></tr><tr><td>DISPLAY ALL SUBMODULES $\langle x \rangle$ . $\langle it \rangle$ </td><td>to display the values of item type ‘ $it$ ’ for all direct or indirect submodules of  $x$ </td></tr><tr><td>DISPLAY SUPER MODULE $\langle x \rangle$ </td><td>to display modules that directly use the service of module  $x$ </td></tr><tr><td>DISPLAY ALL SUPER MODULES $\langle x \rangle$ </td><td>to display all modules that directly or indirectly use the service of module  $x$ </td></tr><tr><td>COPY $\langle x \rangle$ , $\langle y \rangle$ </td><td>to copy module  $x$  to file  $y$ </td></tr><tr><td>COPY ALL $\langle x \rangle$ , $\langle y \rangle$ </td><td>to copy  $x$  and all modules needed by  $x$  (directly or indirectly) to file  $y$ </td></tr></table>

The Report Generator and Graphics Generator that we have in mind should have features similar to those of Knowledge Man [12]. For Screen

Management Language we would like to have display facilities similar to those of SPF [11] and Screen Master [14]. The Source Code Manager (SCM) is a tool which would facilitate the generation of new modules or the alteration of existing modules. A detailed discussion of SCM appears in [7].

## 5.5. Request Handler (RH)

The Request Handler (RH) is intended to be used for maintenance purposes while the DSS is in operation. The purpose of the RH is to provide a communication link between the DSS and the DSSDS. The RH performs a number of important functions. First, suppose that while the DSS is in operation a bug is found in one of the modules. The user will send a request through RH explaining the problem. The user does not necessarily know which programmer was involved in the development of that module. The RH, by looking at the LOM, can route the message to the right programmer. In case the programmer is unknown or is no longer with the organization, then RH will route the problem to the person in charge or the least busy person in charge of such problems.

A second situation is that the user wants some extensions. That is, the user needs a new model which is not found in the DSS and cannot be formulated through existing modules in the DSS by PPS or by the user him/herself. The RH will look at the LOM. If the module is found in LOM, the RH will access the module and route it to the DSS automatically. Otherwise, it will place a message in the mail box of the least busy developer or the developer with the right qualifications for that job. In case the DSS user has some questions and needs some help, he/she can send a help request to the RH. The Request Handler starts a dialogue with the user and gathers information about the subject and the nature of the question and then routes the message to an appropriate developer.

Through RH, the communication link between the DSSDS and the DSS will remain open throughout the system's life cycle. Through this link the news about the availability of new modules, new versions of existing modules, or new facilities can be sent to the DSS to be placed in the mail box of interested parties. RH provides a valuable facility for supporting the product during the operation phase of its life cycle.

## 6. DSS Development

The DSSDS satisfies all the requirements we stated earlier for a DSS development system: the DSSDS supports a speedy development of a DSS; it also supports the DSS in its entire life cycle; various decision support systems can be developed through the DSSDS for different needs; the tools of the DSSDS are available independently; and the DSSDS is capable of evolving over time.

With the initiation of a DSS project, systems analysis begins. SADF helps the developer in gathering information and storing it in an organized way in SADF data base. Through SADF all members of the development team can use the same data and share their thoughts. When the developer believes he/she has understood the problem correctly, the development of the prototype begins. In the prototyping the emphasis is on speedy development of a system which reasonably represents the proposed system. Through DSSDS a speedy development of a prototype is possible because the LOM can provide considerable pre-programmed modules. In addition, the modification of existing modules is greatly facilitated under the SCM. The Report Generator, the Graphics Generator and the query language are excellent facilities for prototyping since efficiency is not an immediate concern in prototyping. For example, if a special report has to be prepared, it is very likely that the report could be provided through RG quite easily. However, if and when the report proved to be necessary or needed on a recurring basis, then a new module should be written to create this report very efficiently for the final system.

## 7. Summary

The need for many decision support systems in the near future stimulated our interest in finding a convenient way for developing such systems. The changing nature of DSS required us to find a way for speedy development and fast modification of DSS. Our study resulted in a proposal for a DSS Development System (DSSDS). The DSSDS facilitates both the development and maintenance of a DSS. The philosophy of the DSSDS is based on two concepts: the use of highly automated tools throughout the development process and the use of prefabricated pieces in the manufacturing of a whole piece. The environment of the DSSDS consists of a Development Language (DL), a Systems Analysis and Design Facility (SADF), a Module Management Language (MML), a Source Code Manager (SCM), a Report Generator (RG), a Graphics Generator (GG), and a Request Handler (RH).

The DSSDS provides an environment in which the developer can create high-quality decision support systems with moderate cost and within a relatively short period of time.

## References

[1] Bell, T., D. Bixler and M. Dyer, An Extendable Approach to Computer Aided Software Requirements Engineering, IEEE Transactions on Software Engineering (1977).

[2] Boehm, R., Software Engineering, R and D Trend and Defense Needs, in: Research Directions in Software Technology, MIT Press, Boston, MA (1978).

[3] Bonczek, R., C. Holsapple and A. Whinston, Foundation of Decision Support Systems, Academic Press, New York (1981).

[4] Bonczek, R., C. Holsapple and A. Whinston, Micro Database Management Practical Techniques for Application Development, Academic Press, New York (1984).

[5] Carlson, E., An Approach for Designing Decision Support Systems, Data Base (1979) 3–15.

[6] Donovan, J., Database System Approach to Management Decision Support, ACM Transactions on Database Systems 1, no. 4 (1976).

[7] Ghiaseddin, N., Framework for a DSS Development System, Ph.D. dissertation, Purdue University, West Lafayette, IN (1982).

[8] Gomaa, H. and D. Scott, Prototyping as a Tool in the Specification of User Requirements, Proceedings of 5th International Conference on Software Engineering (1981).

[9] Gorry, G. and S. Morton, A Framework for Management Information Systems, Sloan Management Review 13 (1971) 55–70.

[10] Henderson, P., Functional Programming - Application and Implementation, Prentice-Hall, Englewood Cliffs, NJ (1980).

[11] Joslin, P., System Productivity Facility, IBM System Journal 20, no. 4 (1981).

[12] Knowledge Manager Reference Manual, Micro Data Base Systems, Lafayette, IN (1983).

[13] Ross, D. and W. Schomaman, Structured Analysis for Requirements Definition, IEEE Transactions on Software Engineering (1977).

[14] Screen Master Reference Manual, Micro Data Base Systems, Lafayette, IN (1982).

[15] Simon, H., The New Science of Management Decisions, Harper, New York (1960).

[16] Stephens, S. and L. Tripp, Requirements Expression and

Verification Aid, Proceedings of the 3rd International Conference on Software Engineering (1978).

[17] Teichrow, D. and E. Hershey, PSL/PSA: A Computer Aided Technique for Structured Documentation and Analysis of Information Processing Systems, IEEE Transactions on Software Engineering (1977).

[18] Time Sharing Information Services, Inc., American Airlines Information Management System: Development, History, and Return on Investment. Time Sharing Today 3, 4, and 5 (1972) 1–15.
