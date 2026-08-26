---
otero_id: 18468
otero_key: "JAY69EPE"
title: "Integrated project support environments"
authors: "Alan W. Brown"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90068-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Integrated Project Support Environments

Alan W. Brown

Department of Computer Science, University of York, York YOI 5DD, England

In the last few years the rapidly expanding application of computer technology has brought the problems of software production increasingly to the fore, and it is widely accepted that current software development techniques are unable to produce high quality software at the required rate. To try to prove this imbalance, the field of Software Engineering is attempting to apply the formal methods of engineering to software design and implementation. One of the most promising areas is that of Integrated Project Support Environments (IPSE's), which attempt to spread the focus of attention during software development from the coding stage to embrace the whole development cycle, from initial requirements specification to operational maintenance. These environments hope to improve production efficiency and quality by providing a complete set of support tools to help with each stage of software development, and to supply the necessary tool integration to ensure a smooth transition between these tools. This paper analyses the motivation for integrated support in the production of software, reviews the history of environments for software development, and provides the context for describing current research trends.

Keywords: Software engineering, Integrated project support environment, Software process.

## 1. Introduction

When a software system is designed and implemented, automated support for the development process is required. Where the software can be written by one person in a few weeks, the required support may be minimal; individual tools for program editing, compiling, and debugging may be all that are required. However, the current trends in the use of computer technology are leading to the development of larger and more complex software systems, which typically require a large group of developers, and may take from months to years to complete. It is not uncommon for software systems development to involve more than a hundred people over a period of years and produce in excess of a million lines of source code [34,16]. With such a vast difference in scale, the following points may be noted:

\- no one person may be fully familiar with the complete system, so it is vital that the separate pools of knowledge can be integrated;

\- the finished product may not be a single definitive version, but a set of related versions to suit different user requirements;

![](/api/attachments/JAY69EPE/fulltext/images/cf12249653c808077a2230888603dad58d11c90a5bd1dcced15103bc2c07bbc4.jpg)

Alan Brown graduated in 1983 with a first class honours degree in Computer Science from the University of Hull. After working in industry for a year he joined the University of Newcastle upon Tyne as a Ph.D. student, and was soon recruited as a Research Associate for the Aspect project, one of the UK. Alvey-funded Software Engineering IPSE projects. In this capacity he was responsible for designing and building an abstraction mechanism to augment the database facilities which formed the heart of the Aspect IPSE. In 1988 Dr. Brown received a Ph.D. for his thesis entitled "A View Mechanism for an Integrated Project Support Environment". In the summer of 1988 Dr. Brown joined the University of York as a lecturer in the Department of Computer Science where his main research interests are in object-oriented database systems, IPSE technology, and in the application of IPSE ideas into other areas, in particular VLSI systems.

\- errors will be found in a large system, and hence maintenance of the running system is very likely to be an on-going problem;

\- it is not economically viable to throw away the system and re-implement when operating conditions, or user requirements change. Therefore, the software must evolve over time;

\- the management of a software project becomes much more difficult, in particular, control of the development and maintenance process and ensuring its continued progress.

Therefore, if we are to provide automated support for large scale software production, we must provide facilities to deal with the problems, and so support the complete software life-cycle, from requirements definition to operational maintenance, provide recognised paths of communication and co-ordination between the software developers involved in a project, and allow managers to exert control over the development and maintenance process and to monitor its progress. Systems which attempt to provide such support are known as Integrated Project Support Environments (IPSE's).

## 2. The Problems of a Traditional Environment

Research into software development techniques and methodologies has been followed by production tools which support a method by automating some aspect of the use or application of the method. The tools may provide different levels of support, from simple clerical assistance by recording and storing the information, to extensive checking of this information according to the rules of the method [28]. Hence, traditional support environments consist of a machine operating system and filing system, together with an ad hoc collection of development tools that cover some part of the life-cycle, supporting some set of preferred development methods. The tool may interface with the operating system or directly with the hardware.

The principle way in which tools interact is through some commonly understood communication protocols embedded within the tools themselves. However, as the tools are often written without knowledge of other tools with which they may need to interact, the use of individual tools within a larger development context can be difficult. The following problems are often experienced:

\- Different development tools often overlap in their roles, duplicating effort;

\- Tools designed to fit different development methods can often interfere with one anther, produce inconsistent results, or be totally incompatible;

\- The complex relationships and dependencies which exist between data items are often lost, or difficult to determine as properties are created within the tools and are unavailable outside the tool, being hidden internally or transformed before output;

\- There is no integrating structure which controls the ways in which a set of tools are allowed to interact with the data, and the tools which individuals users are allowed to invoke. As a result, maintaining data integrity is difficult;

\- Current practice relies heavily on manual co-operation and communication to ensure that project members can work independently and yet as a team.

## 2.1. An Example

To illustrate the problems which exist in traditional development environments, and the need for tools to be integrated in their use of data, consider how the UNIX tool MAKE [15] records information about inter-dependencies of program modules.

Figure 1 shows how a simple software system may have been constructed.

Here, a simple compiler is constructed by processing a parser grammer to produce a parser object module, and then compiling this module to produce a relocatable binary version. This is loaded with the binary produced by compiling a code generation module to produce a running program.

To record the dependencies the MAKE tool relies on a file called a "makefile" which holds these relationships in a special textual form. In Figure 2, we show how this may look.

It consists of a set of line pairs, where the first line of a pair defines a dependency (for example, that the module "program" is dependent on "lib1", "codegen.obj", and "parser.obj" modules) while the second line is a command that will generate the derived module from its constituent parts. For example, "program" is created by executing the command "load lib1 codegen.obj parser.obj". Hence, by reference to a makefile the

![](/api/attachments/JAY69EPE/fulltext/images/ed69e3b3acff44eb27aef6a2ff2ac5508dc1cf9412ebfbb5715536a3e16846b7.jpg)  
Fig. 1. Data Flow for a Simple Compiler.

MAKE tool can automatically generate derived modules from their constituent parts without the user needing to remember how each module was created.

In isolation, the MAKE tool can be used to great effect for program generation and maintenance. However, as part of a larger development environment to provide support for all phases of a software project, there are a number of problems with such a tool. Firstly, the relationships between modules are buried within a makefile in a form specific to the tool. If we now want to transfer that information to some other tool, for example to analyse the impact of changing a particular module, then this new tool would need to read in the makefile and decode the relationships which

Fig. 2. Makefile for Simple Compiler.

exist, before it could perform its function. No doubt the information it obtains will then be written out in some special file, and if we now wish to input this to a report generator then it would have to interpret the output data and convert it as necessary. This not only results in duplication of effort, with each tool having to reinterpret the structured information each time, it is also a major problem when changes to the data format must take place.

A second consequence is that maintenance of makefiles for large systems is particularly difficult. The complexity of the system is reflected in the complexity of the makefile, and thus it is difficult to assess how the makefile should be amended to reflect changes in the way a system is built. If the structures and relationships hidden within a makefile were to be held explicitly in some appropriate form, it would then be easier to alter it when changes are needed.

Finally, if we now wish to apply some form of constraint on how systems are built (for example, applying project standards for system building) with the makefile approach it would be particularly difficult, as it is not clear at when and where rules could be applied. This is because integrity checking of the data is carried out in an ad hoc manner within individual tools. If we could remove the task of data integrity maintenance from each of the separate tools, record the rules in an accessible form, and apply the checks to the data at a central point, then we would have a mechanism which gave us more confidence in the correctness of the data. $^{1}$

![](/api/attachments/JAY69EPE/fulltext/images/c08f55a966f8b0aee4487c46c7206c01f1d47dff03a2d376105e09320a732a21.jpg)  
Fig. 3. Grouping of Tools into Families.

## 2.2. Tool Families

A partial solution employed by many existing development systems is to tightly couple sets of tools into families (tool sets) which share a common pool of knowledge, as shown in Figure 3.

Recognising the need for co-operation and integration between tools, one approach has been to build families of tools that can work in concert to support some part of the development or maintenance process [34,13]. These tool families share common data format and operating conventions which allow them to interact in a meaningful way. A typical example is the set of UNIX tools which make up a documenter's workbench [2]. This allows a single document to contain tables, equations, and diagrams and to be processed by passing it through a sequence of tools which share the same formatting style and formatting conventions.

However, the conventions are still embedded within the tools. Thus, to add a new tool to the family would involve understanding the communication and data conventions with which new tool must interact. This could involve re-implementing the checks and structuring operations that already exist in the family.

## 3. The IPSE Approach

Having recognised the problems of integrating a set of individual tools to support the complete life-cycle of a large software project, researchers began to focus their attention on the means of integration within a support environment, rather than between individual tools. By providing integrated support for software development, it was hoped that much more control could be maintained over the development process, while easing the transition of a software product from one development phase to the next.

Integrated support has been provided by removing the data structuring and control facilities that are often duplicated in each tool and maintaining them at a central point. This allows them to be easily amended and consistently applied [6]. This is coupled with increased recognition that effective support of software development can only be achieved if the tools work together.

Figure 4 shows how the tools communicate by interacting at a higher abstract level than the operating system. The interface has been raised so that it is “closer” to the actual problem domain; it is concerned with project level objects, such as users, their roles within the software development process, and the tasks they carry out, rather than files and program processes. This project level interface has facilities and services which help control software development at the project level.

<table><tr><td>Tool</td><td>Tool</td></tr><tr><td>.</td><td>.</td></tr><tr><td>.</td><td>.</td></tr><tr><td colspan="2">Project Level Interface</td></tr><tr><td colspan="2">Operating System Interface</td></tr><tr><td colspan="2">Hardware Interface</td></tr></table>

Fig. 4. Tool Interaction in an IPSE.

Typically, the facilities record structured data using a database, and control the sharing of data between users at the level of documents and programs.

## 3.1. The Closed IPSE

In closed environments, steps towards integration have been taken by providing tools for supporting the life-cycle of a project within a particular model of the software development process. Typical of this approach is the Perspective IPSE [39]. In this, tools communicate via a database which records all relevant information about the software project throughout its life cycle. The database is structured in a way that allows meaningful relationships between data items to be retained; for example, the relationship between a specification and its implementation in a programming language. The tools form a fixed set supporting a single method of project development. In this case, a set of tools support the MASCOT design notation [3], with automatic translation of validated designs into an extended form of the Pascal programming language. Additional tools then allow compilation and debugging of programs written in this extended Pascal. Further facilities allow communication between project members while controlling the sharing of data between them, using versioned data items.

A large number of closed IPSE's have been built in the last decade, each supporting some preferred set of software development techniques. An early example was TOPD [19], which supported a top-down approach to program design that translated requirements into COBOL code. Later examples include TOOLPACK [32], which is specifically designed to support small-scale development of mathematical software implemented in FORTRAN, and ARCTURUS [35], which supports the use of Ada as a command, design, and programming language. Many more such systems are described in [18].

The important features of a closed IPSE are that, though tightly coupled, no mechanisms are available for the IPSE user to add new tools to support a different approach and very limited facilities are available to tailor the IPSE to suit particular needs. Consequently, a closed IPSE may provide excellent automated support if supported techniques closely mirror an organisation's existing development strategy and are well suited to the application system under development. Otherwise they may involve the organisation in a large amount of relearning, or may not be applicable to some systems. Similarly, as software development methods continue to evolve, support for new methods and techniques will be required. For many closed IPSE's it is not easy to add support without considerable re-implementation of the IPSE by its vendor. The additional project level services available in an IPSE, such as the improved data structuring facilities of the project database, are not accessible to the end users, who may wish to customise the IPSE to suit individual project needs.

## 3.2. The Open IPSE

Recognising the problems of inflexibility in closed IPSE's, some more recent work has led to the creation of open environments [36]. In this approach, the role of the IPSE is seen as the provision of an infrastructure into which tools can be embedded. It provides control of all data developed during the life-time of a project by providing facilities accessible through a structured interface. Thus, facilities at this interface may include support for the structuring and storing of information (eg. documents and program modules) for configuration and version control of data items, and for the sharing of this data among groups of users. As this provides the lowest level of IPSE services, and is the interface at which tools are written, it is known as the Public Tool Interface (PTI) [27]. The required openness is achieved by making the PTI extensible so that it can support new methods and tools, and configurable, so that a project can impose particular methods of working, if desired.

One of the first IPSE's to recognise the advantages of providing an open environment was CADES [30], which was specifically built to support the development of ICL's VME/B operating system. Although originally configured with a fixed set of tools, a form of PTI was made available to allow new tools to be integrated within a CADES system [33].

## 3.2.1. Basic Architecture

The architecture of an open IPSE was initially guided by work carried out to define requirements for an Ada Programming Support Environment (APSE), reported in the STONEMAN document [9]. Here, to support the development of large Ada programs, the need for automated support of the program development process led to the definition of a set of requirements which outline the basic architectural components of an APSE. To summarise, the basis of any APSE must be a database which records data items and their relationships in a structured and accessible form. The database provides the integrating factor for tools that communicate through this structured repository for data. A Kernel Ada Programming Support Environment (KAPSE) is then defined as the database together with communication and run-time support to allow a set of Ada programs to be executed. With the addition of a minimal set of tools to support the creation and maintenance of Ada programs, a Minimal Ada Programming Support Environment (MAPSE) results. Finally, an Ada Programming Support Environment (APSE) is constructed by extending the MAPSE to provide support for different programming methodologies and techniques. This architecture is illustrated in Figure 5.

![](/api/attachments/JAY69EPE/fulltext/images/dbc14c8bb640167b2ec6890defb9ab6fd94647b52c5a7d1f85ac6b3e50d0dfa7.jpg)  
Fig. 5. Basic Architecture of an APSE.

An important feature of the architecture is the interface between the KAPSE and MAPSE. Essentially, this interface provides access to the set of services provided by the KAPSE to the tools implemented as part of the MAPSE and APSE. In this sense it is equivalent to what we have called a PTI.

## 3.2.2. Further Developments

The approach advocated in STONEMAN has gained a wide measure of acceptance over the last few years, and a number of efforts have been made following similar principals.

In the United States, mainly funded by the Department of Defense (DOD), work has been concentrated on specification of APSE's and limited prototyping following the guidelines of STONEMAN. In Europe, and in particular the U.K., with funding from both the Alvey and ESPRIT programmes, IPSE work has been much more diverse. While the ESPRIT work has mainly concentrated on the tools needed to populate IPSES's and a single framework through which they can interact, the Alvey programme has funded three concurrent projects investigating IPSE design and construction.

The first of these is the Aspect project [17]. Following many of the principles established in STONEMAN, Aspect has been working for the past four years on research into, and prototype development of, however, extensible IPSE. The second project, ECLIPSE is more concerned with intercepting current proven technology and constructing a production-standard IPSE to support both Alvey and ESPRIT funded tool producers [1]. This is primarily a set of tools written to the interface provided by an implementation of the Portable Common Tool Environment (PCTE), which is a PTI defined within the ESPRIT programme as the interface to which all of its tool writers can work. The third, and much more ambitious project, called IPSE 2.5, is attempting to extrapolate from current technology to define the direction of future IPSE research [42]. In particular, it is concentrating on support for formal methods of software development. Its name comes from the Alvey definition of a set of existing tools linked by a file system as a first generation IPSE, those built on a database as second generation, and those built on knowledge-based techniques as third generation [31]. According to these definitions, while Aspect and ECLIPSE are second generation IPSE's, this project is attempting to establish a path between second and third generation systems. However, as the project was begun much more recently it is still very much in an exploratory phase.

Work in industry is similarly moving in the direction of open IPSE's, most notably perhaps with recent work at IBM aimed at defining the architecture of a software engineering support facility [21,20]. The proposed architecture emphasizes the need for a set of Common Tool

Services (CTS) accessed by tools through a Common Tool Interface (CTI), analogous to a PTI.

## 3.2.3. Standardisation on a PTI

Early work in this area was motivated by the United States Department of Defense (DOD), whose analysis of their massive spending on computer software determined that a great deal of their resources were being spent on re-writing software in different languages to suit different operating conditions. This led to the design and development of the Ada language, and the recognition that the environment in which Ada programs were developed would itself have to be defined. When a number of concurrent projects were underway to develop APSE systems along the lines suggested in the STONEMAN report, the US DOD realised that the problems experienced by implementing software in many different languages would soon exist for tool writers. Potentially, tool writers would spend much of their time porting tools to work in different APSE's. Hence, at the beginning of 1982, work began on defining a set of APSE standards for use within the US DOD to permit the sharing of tools and other software between US DOD supported APSE's. In 1985 a proposed Military Standard Common APSE Interface Set (CAIS) was released for evaluation [40]. Following this work, a set of requirements for a more advanced APSE interface set was developed [41], and work is currently underway to enhance the first version of the CAIS to meet these requirements.

Motivated by a similar need for a common tool interface, though for programs written in a variety of languages, the European ESPRIT programme has provided funds for the definition of a Portable Common Tool Environment (PCTE) to be used throughout the ESPRIT community [8]. All tool writers funded by the ESPRIT programme will write tools to this public interface, which will facilitate the integration of tools within a common framework. Implementations of the PCTE are now available, and many more are expected.

Hence, support for a standard PTI is divided between those who advocate the CAIS, and its enhancements to provide extended support, and those who support use of the PCTE. Both technical and political arguments abound, with many people desperate for standardisation, particularly developers trying to avoid unnecessary re-writing of their tools to suit different IPSE interfaces. However, many IPSE researchers favour a more cautious approach, recognising that experience of using IPSE systems is remarkably thin.

## 4. Support Environments for Non-Software Design Activities

The process of software development shares a number of characteristics with other development activities, notably Ver; Large Scale Integration (VLSI) circuit design, architectural design, and aerospace design. These activities can be grouped collectively under the title of "Engineering Design". It is interesting, then, to examine the approaches taken to provide computerised support in these related areas and compare them with IPSE technology.

Computer-Aided Design (CAD) systems have been available for a number of years, and it has been recognised that there have been more attempts to provide automated support in design activities such as VLSI circuit design than for software design [37]. However, the development history of support environments for non-software design activities has very closely followed that described for software. In particular, the abundance of individual tools supporting some part of a design method are now giving way to integrated tool sets supporting more of the design process [22]. Indeed, in parallel with the work in IPSE's for software development support, attention in non-software design activities is now turning from individual tools towards controlled tool interaction through the use of a design database [14,24,7].

Analysis of the characteristics of design data have revealed a number of problems with applying conventional database technology in the design environment. Similar analyses have been made for software engineering data $[4,5]$ , and it is interesting to note how closely the results equate to similar analyses of VLSI circuit design data.

Cross-fertilisation of ideas between different design activities is currently underway in some areas, most notably in the support for long-lived design transactions and complex data objects [25,23,26]. It is clear, however, that continued collaboration will be of benefit to all, with the result that the design process may be better understood and the designer's needs more adequately supported.

## 5. 4GL's and CASE Environments

In the field of commercial data processing pressure to improve the speed and quality of software production has been a driving force for many years. Initially improvements were made through the adoption of third generation languages $^{2}$ such as COBOL and PL/1. Later, the use of database systems in place of conventional file-based techniques provided a greater level of independence between the application programs and the physical data structures. In the latest attempts at providing more powerful application languages, the data definition and manipulation languages of relational database systems have been augmented with facilities to provide easier end-user application development. As these languages manipulate sets of tuples of relations rather than records within files, they are often classed as the next generation of programming language, fourth generation languages (4GL's) [29].

In effect a 4GL provides an application development environment consisting of a relational database and application development language. The main components of a 4GL appear to be:

\- A database query language. Usually some form of the SQL language [12] is provided to allow database definition and manipulation;

\- A procedural language. A third generation language (3GL), usually C, is often available for more complex data manipulation and arithmetic operations. Facilities exist to embed the database query language into the 3GL;

\- A report generator. A simple language exists which enables complex data retrievals to be made, and the format of the displayed results to be defined;

\- A screen generator. For fast generation of end-user applications, facilities exist to enable screen-based interfaces to the database to be created. Many of the complex screen-handling facilities are managed within the 4GL and need not be considered in the final application. This makes the applications smaller and easier to write.

Hence, 4GL's can be seen as a limited form of IPSE in that they provide integrated support for the fast development of data processing applications. While they are very effective for the creation of small-scale applications and prototypes, their lack of support for anything other than a small part of the software life-cycle limits their use.

For large-scale data-intensive application development, support systems which attempt to provide a more integrated set of facilities are often called Computer-Aided Software Engineering (CASE) environments [10]. There is no clear agreement as to the use of the term “CASE environment”. Systems which come under this heading seem to range from extensions of 4GL systems to cover an extended life-cycle through the addition of debugging tools, to complete integrated systems which are in broad terms equivalent to IPSE’s as described earlier. In the more extensive CASE environments, the only clear distinction between them and IPSE’s seems to be the application domains; while IPSE’s are primarily aimed at largescale, embedded real-time systems, typically for use in military or process control environments, CASE environments address commercial data processing applications. This often manifests itself in the choice of tools supported. In Index Technology’s Excellerator CASE system [11], for example, the tools and facilities available address the areas of:

\- Diagrammatic support for structured methods. For example, graphic-editing facilities for system specification in Jackson Structured Design [38];

\- Prototyping of end-user screens;

\- Analysis and consistency of designs;

\- Sophisticated desk-top publishing support for documentation production;

\- Project management, including cost estimation and load forecasting;

\- Automatic code-generation from designs, and the use of 4GLs.

The emergence of CASE environments in commercial data processing can be seen as a direct parallel to the use of IPSE's in real-time embedded systems. As both fields progress, it is likely that the distinction between them will become continually more blurred.

## 6. Summary

The need to provide automated support to aid the process of complex software systems design, implementation, and maintenance, led to the production of individual tools to support individual development methods and techniques. Integration of the various facilities has been necessary to ensure that the complete project life-cycle is supported in a convenient, flexible manner within a model of the development process. This paper has examined the motivation and objectives of this work, with particular emphasis on the key aims of openness and integration upon which an IPSE is founded. We have classified IPSE's as closed and open, depending on the exposure they provide to a Public Tool Interface (PT?), and consequently the ease with which new tools can be added to the IPSE. Through providing this analysis, we have been able to compare and contrast some of the current major research efforts.

## 7. Acknowledgements

This work was carried out as part of the Aspect project, which is a UK. IPSE project funded by SERC through the Alvey Software Engineering Directorate. Special thanks are due to Peter Hitchcock and Brian Randell for their comments on earlier drafts of this paper.

The form and content of this paper have also been enhanced through the detailed comments of the referees, particularly those of Prof. Sibley.

## References

[1] A. Alderson, M.F. Bott, and M.E. Falla, "An Overview of the Eclipse Project", pp. 100–113 in Integrated Project Support Environments, ed. J. McDermid, Peter Peregrinus (1985).

[2] AT&T, UNIX System V Documenter's Workbench Introduction and Reference Manual, April 1984.

[3] G. Bate, "Mascot3: An Informal Introductory Tutorial", Software Engineering Journal 1(3), pp. 95-102 (May 1986).

[4] M.L. Boerstra (ed.), Engineering Databases, Elsevier Press (1985).

[5] A.W. Brown, A.N. Earl, P. Hitchcock, R. Weedon, and R.P. Whittington, "The Use of Databases for Software Engineering", pp. 55–70 in Proceedings of the 5th British National Conference on Databases (BNCOD5), ed. E.A. Oxborrow, Cambridge University Press (14th–16th July 1986).

[6] A.W. Brown, "A View Mechanism for an Integrated Project Support Environment", in Proceedings of a Conference on Automating Systems Development, Leicester Polytechnic (April 1987).

[7] A.P. Buchmann, "Current Trends in CAD Databases", Computer-Aided Design 16 (May 1984).

[8] Bull, ICL, Nixdorf, Olivetti, and Siemens, PCTE: A Basis for a Portable Common Tool Environment - C Functional Specification, 1985.

[9] J.N. Buxton, Requirements for APSE - STONEMAN, US Department of Defence (February 1980).

[10] E.J. Chikofsky, "Software Technology People Can Really Use", IEEE Software, pp. 8-10 (March 1988).

[11] E.J. Chikofsky and B.L. Rubenstein, "CASE: Reliability Engineering for Information Systems", IEEE Software, pp. 11-16 (March 1988).

[12] CJ. Date, A Guide to the SQL Standard, Addison-Wesley (1987).

[13] D.A. Dolotta and J.R. Mashey, "An Introduction to the Programmer's Workbench", pp. 164–168 in Proceedings of 2nd International Conference on Software Engineering, San Francisco (October 1976).

[14] J. Encarnacao and F.L. Krause, File Structures and Databases for CAD, North-Holland (1982).

[15] S.I. Feldman, "Make - A program for Maintaining Computer Programs", Software Practice and Experience, Bell Laboratories 9, pp. 255-265 (April 1979).

[16] R.L. Glass, Modern Programming Practices - A Report from Industry, Prentice-Hall (1982).

[17] J.A. Hall, P. Hitchcock, and R. Took, "An overview of the ASPECT Architecture", pp. 86–99 in Integrated Project Support Environments, ed. J. McDermid, Peter Peregrinus Ltd. (1985).

[18] H-L. Hausen and M. Mullerburg, "Conspectus of Software Engineering Environments", pp. 462–476 in Tutorial: Software Development Environments, ed. A.I. Wasserman (1982).

[19] P. Henderson, "The TOPD System", Technical Report No. 77, University of Newcastle upon Tyne (September 1976).

[20] G.F. Hoffnagle and W.E. Beregi, "Automating the Software Development Process", IBM Systems Journal 24 (3), pp. 102-120 (1985).

[21] W.S. Humphrey, "The IBM Large-Systems Software Development Process: Objectives and Direction", IBM Systems Journal 24(2), pp. 76–78 (1985).

[22] R.H. Katz, "Managing the Chip Design Database", IEEE Computer, pp. 26-36 (December 1983).

[23] R.H. Katz, "Transaction Management in the Design Environment", in New Applications of Databases, ed. Garadin and Gelenbe, Academic Press (1984).

[24] M.A. Ketabchi and V. Berzins, "Modeling and Managing CAD Databases", IEEE Computer 20(2), pp. 93-102 (February 1987).

[25] W. Kim and D.S. Batory, "Modeling Concepts for VLSI

CAD Objects", ACM Transactions on Database Systems 10 (September 1985).

[26] R.A. Lorie, Issues in Databases for Design Applications, IBM Research Report (1981).

[27] T.G.L. Lyons, "The Public Tool Interface in Software Engineering Environments", Software Engineering Journal 1(6), pp. 254–258 (November 1986).

[28] J. McDermid and K. Ripken, Life-Cycle Support in the Ada Environment, Cambridge University Press (1984).

[29] F.R. McFadden and J.A. Hoffer, Database Management (Second Edition), Benjamin/Cummings (1988).

[30] R.W. McGuffin, A.E. Elliston, B.R. Tranter, and P.N. Westmacott, "CADES - Software Engineering in Practice", ICL Technical Journal 2(1), pp. 13-28 (May 1980).

[31] D. Morgan, “The Imminent IPSE”, Datamation 33(7), pp. 60–68 (April 1987).

[32] L. Osterweil and W.R. Cornell, "The Toolpack/IST Programming Environment", in IEEE Softfair (July 1983).

[34] B.R. Rowland and R.J. Welsch, "Software Development System", Bell Systems Technical Journal 62(1) (January 1983).

[33] D.S. Robinson, Private Communication, December 1987.

[35] T.A. Standish and R.N. Taylor, "Arcturus: A Prototype Advanced Ada Programming Environment", ACM SIGPLAN Notices 19(5), pp. 57–64 (May 1984).

[36] V. Stenning, "On the Role of an Environment", pp. 30–35 in Proceedings of the 9th International Conference on Software Engineering (March 1987).

[37] L.G. Stucki, "What about CAD/CAM for Software? - The ARGUS Concept", SOFT-FAIR '83, pp. 129–144, IEEE (1983).

[38] A. Sutcliffe, Jackson Systems Development, Prentice-Hall (1988).

[39] Systems\_Designers, DEC/1.X Perspective Technical Overview, November 1984.

[40] US.DOD, "Common APSE Interface Set (CAIS)", Proposed MIL-STD-CAIS (January 1985).

[41] US.DOD, Requirements and Design Criteria for the Common APSE Interface Set (RAC), September 1985.

[42] B.C. Warboys, "IPSE 2.5", pp. 221–230 in Proc. Joint IBM/University of Newcastle upon Tyne Seminar (2nd–5th September 1986).
