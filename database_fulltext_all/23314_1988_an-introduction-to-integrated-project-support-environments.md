---
otero_id: 23314
otero_key: "QB7Y9Q86"
title: "An Introduction to Integrated Project Support Environments"
authors: "Alan W Brown"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.35"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Introduction to Integrated Project Support Environments

Alan W. Brown, Department of Computer Science, University of York

Abstract: In the last few years the rapidly expanding application of computer technology has brought the problems of software production increasingly to the fore, and it is widely accepted that current software development techniques are unable to produce high quality software at the rate required to keep pace with this. To try to improve this imbalance, the field of software engineering has been advanced as a possible solution, attempting to apply the formal methods of an engineering discipline to software design and implementation. One of the most promising areas to be developed in this field is that of integrated project support environments (IPSEs), which attempt to spread the focus of attention during software development from the coding stage to embrace the whole development cycle, from initial requirements specification through to operational maintenance. These environments hope to improve production efficiency and quality by providing a complete set of support tools to help with each stage of software development, and to supply the necessary tool integration to ensure a smooth transition of use between these tools.

This paper provides an introduction to IPSEs through analysing the motivation for providing integrated support for the production of software, and describing something of the evolution of environments for software development. This provides the context for describing current and future research trends in this area.

## Introduction

When a software system is designed and implemented, automated support for the development process is required. Where the software can be written by one person in a few weeks, the amount of support required may be small. For example, individual tools for program editing, compiling, and debugging may be all that are required. However, the current trend is for the use of computer technology in increasingly diverse and complicated applications, leading to the development of larger and more complex software systems. These systems typically require a large group of people to develop them, and may take many months to complete. For example, it is not uncommon for software systems development to involve more than a hundred people over a period of a number of years and produce in excess of a million lines of source code. $^{1,2}$ With this vast difference in scale, at least the following points may be noted:

\- No one person may be fully familiar with the complete system, so it is vital that the separate pools of knowledge can be integrated.

\- The finished product may exist not as one single definitive version but as a set of related versions to suit different user requirements.

\- Errors will be found in a large system, and hence maintenance of the running system will be an ongoing problem.

\- It is no longer economically viable to throw away the system and re-implement when operating conditions, or user requirements, change. Therefore, the software must evolve over time.

\- The management of a software project becomes much more difficult. In particular a great deal of time and effort is required to control the development and maintenance process, and to ensure the project's continued progress.

Therefore, if we hope to provide automated support for large-scale software production, we must provide facilities to deal with these problems, and so support the complete software life-cycle, from requirements definition to operational maintenance, provide recognized paths of communication and co-ordination between the software developers involved in a project, and allow managers to exert control over the development and maintenance process and to accurately monitor its progress. Systems which attempt to provide such support are most often known as software engineering environments, or integrated project support environments (IPSEs).

## The problems in a non-IPSE environment

Research into different software development techniques and methodologies has been followed by the production of individual software tools which support a method by automating some aspect of the use or application of the method. The tools may provide different levels of support, from simple clerical assistance by recording information in a computer's file store, to extensive checking of this information according to the rules defined by the method. $^{3}$ Hence, traditional environments in which software is developed consist of a machine operating system and filing system, together with an ad hoc collection of development tools which cover some part of the development life-cycle, supporting some set of preferred development methods. A software product is progressed by application of the development tools to the data which is generated. This situation is summarized in Figure 1.

In Figure 1 tools access machine facilities through the operating system interface, recording data in the file store it maintains. The principal way in which tools are allowed to interact is through some commonly understood communication conventions embedded within the tools themselves. However, as the tools are often written without knowledge of the other tools with which they may interact, the use of individual tools within a larger development context can result in difficulties. The following problems are often experienced:

\- Different development tools overlap in their roles and duplicate effort.

\- Tools designed to fit different methods can often interfere with each other, produce inconsistent results, or be totally incompatible.

\- The complex relationships and dependencies which exist between data items are often lost or difficult to determine as these properties are created within the tools themselves and hidden within the data formats they produce as output.

\- There is no integrating structure which controls both the way in which tools are allowed to interact with the data, and the tools which individual users are given access to invoke. As a result, maintaining the integrity of the data is difficult.

\- Current practice relies heavily on manual cooperation and communication to ensure that project members can work independently and yet as a team. Such problems are compounded in large, distributed projects.

## An example

To illustrate the problems which exist in traditional development environments, and the need for tools to be integrated in their use of data, consider how the UNIX tool MAKE $^{4}$ records information about interdependencies of program modules.

Figure 2 represents diagramatically how a simple software system may have been constructed, using an example adapted from ref. 4.

![](/api/attachments/QB7Y9Q86/fulltext/images/68a293eef6f80983e305f8559c1b831e453ea5da39ddebe22dcceb61ae6bf36b.jpg)  
Figure 1. Typical connection of tools in traditional development environment

In Figure 2, a simple compiler is constructed by processing a parser grammar to produce a parser object module, and then compiling this module to produce a relocatable binary version of the parser. This is loaded with the binary produced by compiling a code generation module to produce a running program.

To record the dependencies shown in Figure 2, the MAKE tool relies on a file called a 'makefile' which holds these relationships in a special textual form. In Figure 3, we show how a makefile may look for this example.

![](/api/attachments/QB7Y9Q86/fulltext/images/a0c074e1b5261b5a8c7166845dfbf47fd49e8a11722ca0a2698fdebd91fe1e41.jpg)  
Figure 2. Data flow for a simple compiler

It consists of a set of pairs of lines where the first line of a pair defines a dependency, for example, that the module 'program' is dependent on 'lib1', 'codegen.obj', and 'parser.obj' modules, while the second line is a command which will generate the derived module from its constituent parts. For example, 'program' is created by executing the command 'load lib1 codegen.obj parser.obj'.

program: libl codegen.obj parser.obj
load libl codegen.obj parser.obj

codegen.obj: codegen.src defsl
compile defsl codegen.src

parser.obj: parser.src defsl
compile defsl parser.src

parser.src: parser.gram

parser-gen parser.gram

## Figure 3. Makefile for simple compiler

Hence, by reference to a makefile the MAKE tool can automatically generate derived modules from their constituent parts without a user having to remember how each module is created.

In isolation, the MAKE tool can be used to great effect for program generation and maintenance. However, as part of a larger development environment in which we would like to provide support for all phases of a software project, there are a number of problems with such a tool. First, the relationships between modules are buried within a makefile in a special form which is specific to the tool. If we now want to use that information within some other tool, for example if we want to analyse the impact of changing a particular module and had such a tool available, this new tool would need to read in the makefile and decode the relationships which exist, before it can perform its function. No doubt the information it obtains will again be written out in some special form to a file, and if we now wanted to run a report generator with that information, it too would have to interpret the data and convert it to a form it recognized. This not only results in duplication of effort within different tools, having to re-interpret the structured information each time, but is also a source of problems when changes to the data format take place. It is not now possible to make any changes to the way data is stored without changing all the tools which access the data.

A second consequence of this approach is that maintenance of makefiles for large systems is a particularly difficult task. This is because the complexity of the system is reflected in the complexity of the makefile, and as a result it is difficult to assess how the makefile should be amended to reflect changes in the way a system is built. If the structures and relationships hidden within a makefile were to be held explicitly in some appropriate form, it would then be easier to alter this information when changes are needed.

Finally, if we now wanted to apply some forms of constraint on how systems are built, for example to apply project standards for system building, we would find this particularly difficult to achieve with the makefile approach as it is not clear at what point such rules could be applied. This is because integrity checking of the data is carried out in an ad hoc manner within individual tools themselves. If we could remove the task of integrity maintenance of data from each of the separate tools, record the rule in an accessible form, and apply the checks to the data at a central point, we would then have a mechanism which gave us much more confidence in the correctness of the data.

## Tool families

A partial solution employed by many existing development systems is to tightly couple sets of tools into families which share a common pool of knowledge, as shown in Figure 4.

Recognizing the need for co-operation and integration between tools, one approach has been to build families of tools which can work in concert to support some part of the development or maintenance process. $^{1,5}$ These tool families share a common data format and operating conventions which allow them to interact in a meaningful way. A typical example is the set of UNIX tools which make up a documenter's workbench. $^{6}$ This allows, for example, a single document to contain tables, equations and diagrams, and to be processed by passing the document through a sequence of appropriate tools which share a formatting style and a set of formatting conventions.

However, the conventions on which a set of tools are based are still embedded within the tools themselves and, for example, to add a new tool to a development environment would involve understanding the communication and data conventions of the tool sets with which one would expect the new tool to interact. This would involve re-implementing all the checks and structuring operations which already exist within the other tools. Also, if it was attempted to use the new tool with tools built on different conventions, the results would not be as expected.

## The IPSE approach

Having recognized the problems of integrating a set of individual tools to support the complete lifecycle of a large software project, researchers then began to focus their attention on the means of integration within a support environment, rather than on the individual tools themselves. By providing integrated support for software development it was hoped that much more control could be maintained over the development process, while at the same time easing the transition of a software product from one development phase to the next.

![](/api/attachments/QB7Y9Q86/fulltext/images/487c2181a9df9d63834d54500e77e84ce49657c87c19d6821e9d5dd7b22a17ea.jpg)  
Figure 4. Grouping of tools into families

The basis of providing integrated support has been through attempting to remove from the individual tools many of the data structuring and control facilities which typically are duplicated in each tool, and to maintain them at a central point which allows them to be more easily amended and consistently applied. $^{7}$ This has been coupled with an increasing recognition that effective support for software development can only be achieved if the tools work together within an effective development process.

In Figure 5 we can see that the tools communicate by interacting at a higher abstract level than the operating system interface. The interface at which tools and users interact has been raised so that it is closer to the actual problem domain, being concerned with project level objects such as users, their roles within the software development process, and the tasks they carry out, rather than the operating system concepts of files and program processes. We can think of this more abstract level as a project level interface, as through this interface facilities and services are available which help control software development at the project level. Typically, the facilities offered are for recording structured data using a database, and for the controlled sharing of data between users at the level of documents and programs.

Examining environments which provide integrated support for software development, we can divide systems into two approaches based on the exposure given to the project level interface, and consequently the ease with which new tools can be added to the environment to support new methods and techniques.

## Closed IPSEs

In the first approach, which provides what we can call ‘closed’ environments, steps towards fully integrated environments have been taken by providing a set of tools for supporting the life-cycle of a project within a preferred model of the software development process. Typical of this approach is the Perspective IPSE. $^{8}$ In a Perspective environment, tools communicate mainly via a database, which records all relevant information about a software project throughout its life-cycle. The database is structured in a way which allows meaningful relationships between data items to be maintained, for example the relationship between a specification document and its implementation in a programming language. The tools provided form a fixed set supporting a single method of project development. In this case, a set of tools support the MASCOT design notation, $^{9}$ with automatic translation of validated MASCOT designs into an extended form of the Pascal programming language. Additional tools then allow compilation and debugging of programs written in this extended form of Pascal. Further facilities exist to allow communication between project members while controlling the sharing of data between them through the use of versioned data items.

A large number of closed IPSEs have been built in the last decade, each supporting some preferred set of software development techniques. An early example was TOPD, $^{10}$ which supported a top-down approach to program design which translated into COBOL code. Later examples include TOOLPACK, $^{11}$ which is specifically designed to support small-scale development of mathematical software implemented in FORTRAN, and ARCTURUS, $^{12}$ which supports the use of Ada as a command, design, and programming language. Many more such systems are described in ref. 13.

![](/api/attachments/QB7Y9Q86/fulltext/images/7816783a3079354badb3b33da405e4829622eecb0304e3033b930f7358c2ca7e.jpg)  
Figure 5. Tool interaction in an IPSE

The important features of a closed IPSE are that although tightly coupled support is provided by the IPSE for a designated development methodology, no mechanisms are available for the IPSE user to add new tools to support a different development approach, and very limited facilities to tailor the IPSE to suit a particular organization's needs. Consequently, a closed IPSE may provide excellent automated support if the development techniques supported mirror closely an organization's existing development strategy, and are well suited to the application system under development, but otherwise may involve the organization in a large amount of re-learning, or may not be directly applicable to some systems. Similarly, as ideas and opinions concerning software development continue to evolve, support for new methods and techniques will also be required. With many closed IPSEs it is not easy to add support for such techniques without a considerable amount of re-implementation of the IPSE itself by the IPSE vendor. The additional project level services which are available in an IPSE, such as the improved data structuring facilities of a project database, are not made accessible to the end users who may want to customize the IPSE to suit individual project needs.

## Open IPSEs

Recognizing the problems of inflexibility which are evident with closed IPSEs, some of the more recent work in IPSE development has led to the creation of what can be called 'open' environments. $^{14}$ In this approach the role of the IPSE is seen as the provision of an infrastructure into which tools can be embedded. The IPSE provides control of all data developed during the lifetime of a project by providing a set of facilities accessible through a more appropriately structured interface than is conventionally available in a simple tool and operating systems environment. So, for example, facilities available at this interface may include support for the structuring and storing of information such as documents and program modules, for configuration and version control of data items, and for the sharing of information between groups of users. As this provides the lowest level at which any of the IPSE services may be accessed, and is therefore the interface at which tools are written, this interface is known as the public tool interface (PTI) for the IPSE. $^{15}$ The required openness of the IPSE is achieved by making the PTI extensible in order to support new methods and tools, and configurable so that a project can impose particular methods of working if desired.

One of the first IPSEs to begin to recognize the advantages of providing an open environment was CADES $^{16}$ which was specifically built to support the development of ICL's VME/B operating system. Although originally configured with a fixed set of tools, a form of PTI was made available to allow new tools to be integrated within a CADES system. $^{17}$

## Basic architecture

The architecture of open IPSE systems has been initially guided by work carried out to define requirements for an Ada programming support environment (APSE), reported in the STONEMAN document. $^{18}$ Here, to support the development of large programs written in Ada, the need for automated support of the program development process led to the definition of a set of requirements which outline the basic architectural components of an APSE. To summarize the report, the basis of any APSE must be a database which records data items and their relationships in a structured and accessible form. The database provides the integrating factor for tools which communicate through this structured repository for data. A kernel Ada programming support environment (KAPSE) is then defined as the database together with communication and runtime support to allow a set of Ada programs to be executed. With the addition of a minimal set of tools to support the creation and maintenance of Ada programs, a minimal Ada programming support environment (MAPSE) is envisaged. Finally, an Ada programming support environment is constructed by extending the MAPSE to provide support for different programming methodologies and techniques. This architecture is summarized in Figure 6.

An important feature of the architecture shown in Figure 6 is the interface between the KAPSE and MAPSE facilities. Essentially, this interface provides access to the set of services provided by the KAPSE to the tools implemented as part of the MAPSE and APSE. In this way it is equivalent to what we have called a PTI.

## Further developments

The approach advocated in STONEMAN has gained a wide measure of acceptance over the last few years, and a number of efforts have been made following similar principles. Here we summarize briefly the direction of this work.

In the United States, mainly funded by Department of Defense (DOD), work has been concentrated on implementations of APSEs following the guidelines of STONEMAN. In Europe, and in particular the UK, with funding from both the Alvey and ESPRIT programmes, IPSE work has been much more diverse in nature. While the ESPRIT work has been concentrating mainly on the tools which will be needed to populate IPSEs and a single framework through which they can interact, the Alvey programme has funded three concurrent projects which are investigating IPSE design and construction. The first of these is the ASPECT project. $^{19}$ Following many of the principles established in STONEMAN, ASPECT has been working over the past three years on research into, and prototype development of, an open, extensible IPSE. The second project, ECLIPSE, is much more concerned with intercepting current proven technology and constructing a production-standard IPSE to support both Alvey- and ESPRIT-funded tool producers. $^{20}$ This is primarily a set of tools written to the interface provided by an implementation of the portable common tool environment (PCTE), which is a PTI defined within the ESPRIT programme as the interface to which all of its tool writers can work. The third, and much more ambitious project, called IPSE 2.5, is attempting to extrapolate from current technology to define the direction of future IPSE research in the next decade. $^{21}$ In particular, it is concentrating on support for formal methods of software development. Its name comes from the Alvey definition of a set of existing tools linked by a file system as a first generation IPSE, those built on a database as second generation, and those built on knowledge-based techniques as third generation. $^{22}$ According to these definitions, while ASPECT and ECLIPSE are second generation IPSEs, this project is attempting to establish a path between second and third generation systems. However, as the project was begun much more recently than the other two it is very much in an exploratory phase.

Work in industry is similarly moving in the direction of open IPSEs, most notably perhaps with recent work at IBM aimed at defining the architecture of a software engineering support facility. $^{23, 24}$ The architecture proposed emphasizes the need for a set of common tool services (CTSs) accessed by tools through a common tool interface (CTI), analogous to a PTI. It will be interesting to see how this work develops and how it influences other commercial IPSE builders.

## Standardization on a PTI

Early work in this area was motivated by the United States DOD, whose analysis of their massive spending on computer software determined that a great deal of their resources were being spent on re-writing software in different languages to suit different operating conditions. This led to the design and development of the Ada language, and the recognition that the environment in which Ada programs were developed would itself have to be defined. Initial observations and requirements for Ada programming support environments were outlined in the STONEMAN document. $^{18}$ When a number of concurrent projects were under way to develop APSE systems along the lines suggested in the STONEMAN report, the US DOD soon realized that the problems experienced by implementing software in many different languages would soon exist for tool writers who would not know which APSE interface to use when implementing tools. Potentially, tool writers would spend much of their time porting tools to work in different APSE systems. Hence, at the beginning of 1982, work began on defining a set of APSE standards for use within the US DOD which would permit the sharing of tools and other software between US DOD supported APSEs. In 1985 a proposed military standard common APSE interface set (CAIS) was released for evaluation. $^{25}$ Leading on from this work a set of requirements for a more advanced APSE interface set has been developed, $^{26}$ and work is currently under way to enhance the first version of the CAIS to meet those requirements.

![](/api/attachments/QB7Y9Q86/fulltext/images/d25f734f0c70af0d27092c27b4c432eafed6b1a02ec1404b1ee1997e92110920.jpg)  
Figure 6. Basic architecture of an APSE

Motivated by a similar need for a common interface for tools, though for programs written in a variety of languages and not just Ada, the European ESPRIT programme has provided funds for the definition of a portable common tool environment (PCTE) which can be used throughout the ESPRIT community. $^{27, 28}$ All tool writers funded by the ESPRIT programme will write tools to this public interface, which will facilitate the integration of tools within a common framework. Implementations of the PCTE are now available, and many more are expected in the near future.

Hence, at present, support for a standard PTI is divided between those who advocate the CAIS — in particular its enhancements to provide extended support – and those who support use of the PCTE. Both technical and political arguments abound in this debate, with many people desperate for standardization as soon as possible, including tool developers who are trying to avoid unnecessary rewriting of their tools to suit different IPSE interfaces. However, many IPSE researchers favour a more cautious approach to standardization, recognizing that experience of using IPSE system is remarkably thin on the ground. It remains to be seen how these arguments will develop.

## Support environments for non-software design activities

The process of software development shares a number of characteristics with other development activities, most notably very large scale integration (VLSI) circuit design, architectural design, and aerospace design. These activities can be grouped collectively under the title of 'engineering design'. It is interesting, then, to examine the approaches taken to provide computerized support in these related areas and compare them with the IPSE technology described above.

Computer-aided design (CAD) systems have been available for a number of years, and it has been recognized that in the past there have been more attempts to provide automated support in design activities such as VLSI circuit design than for software design. $^{29}$ What is interesting, however, is to note that the development history of support environments for non-software design activities has very closely followed that described above for software. In particular, the abundance of individual tools supporting some part of a particular design method are now giving way to integrated tool sets supporting more of the design process. $^{30}$ Indeed, in parallel with the work on IPSEs for software development support, attention in non-software design activities is now turning from individual tools towards controlled tool interaction through the use of a design database. $^{31, 32, 33}$

Analysis of the characteristics of design data have revealed a number of problems with applying conventional database technology in the design environment. $^{30}$ Similar analyses have been made for software engineering data, $^{34,35}$ and it is interesting to note how closely the results equate to similar analyses of VLSI circuit design data.

Cross-fertilization of ideas between different design activities is currently under way in some areas, most notably in the support for long-lived design transactions and complex data objects. $^{36, 37, 38}$ It is clear, however, that continued collaboration will be of benefit to all concerned with the result that the design process itself may be better understood, and the designer's needs more adequately supported.

## A personal view of future IPSE research trends

The field of IPSE research has been particularly active over the past few years, and there seems to be no indication that this interest will subside in the foreseeable future. It would be useful at this point to look at some of the major trends of this work. Clearly, future IPSE work will be affected by advances in other related areas of computer science. For example, the current interest in knowledge-based techniques to provide active support for controlling large amounts of data will be directly applicable to IPSE research. $^{39}$ In this section, however, we examine a few of the areas which we believe will be of significance specifically to future IPSE research, with particular comment on the issue of standardization within the IPSE field.

## Genericity

Support environments in the past have focused on providing fixed support for a preferred development methodology. However, recent work has been aimed at providing open environments which enable new tools to be added easily to an IPSE. This move towards open environments can be seen as a first step on the road to providing a more generic style of environment in which the IPSE is seen as a kit of parts that can be instantiated, or customized, to provide a tailored, usable IPSE to suit a particular organization or project.

For example, work in the ASPECT project $^{19}$ is aimed at research into, and prototype development of, a generic IPSE capability. This work has concentrated on analysing the basic components of an IPSE and attempting to define generic mechanisms which would be necessary within many particular IPSEs. For example, a generic model of version and configuration control is used which deals with the logical representation of a developing product and its physical realization. A customized ASPECT IPSE, however, would tailor these facilities to support a particular model of versions and configurations to suit the end-user organization's needs. The recognition and understanding of the process of IPSE customization will be an important area of further IPSE research as many open questions remain.

## Modelling the software process

An important progression in recent IPSE work has been a recognition that the controlled development of a software product is as much about controlling the software development process as the final end product of the process. From this view there must be facilities within the IPSE to represent and control the development process in a clear and effective way.

One way in which we could represent the software development process is shown in Figure 7.

While traditionally support has been provided for the creation of a software product, and the controlled generation and manipulation of components which make up the product, we can distinguish two equally important aspects of the development process.

First, the product is developed under the control of a project plan. The creation and amendment of the plan together with its relationships with the product, are vital components of the development process. To provide effective support for managing software development the project plan itself must be modelled and controlled.

![](/api/attachments/QB7Y9Q86/fulltext/images/caf960fc87aa81f6cdb088ae83a1532e4ab90d0a5179f82291223fe9a8b315ae.jpg)  
Figure 7. A view of the development process

Similarly, the project plan is developed and carried out within the constraints of a larger project organization. It is important that the various project members, the roles they perform, and the allocation of users to perform tasks within the project plan are all monitored and controlled within the IPSE.

IPSE support for the software process is currently poor, with the notable exception of ISTAR $^{40}$ which uses the notion of a software ‘contract’ to model the individual tasks within a project plan. There will undoubtedly be a great deal of future IPSE work on providing effective support in an IPSE for the software process.

## Multi-discipline design environments

Initial work on IPSEs such as the STONEMAN report $^{18}$ discussed the role of environments in terms of support for particular programming languages. In the case of STONEMAN it was Ada. However, just as the idea of confining support environments to specific languages has been questioned by many, so we might begin to question the need for separate environments to support different types of engineering design. In particular, the support environment requirements for both computer hardware and software development appear to be very similar. Indeed, with respect to the design of computer-based systems there would be undeniable advantages for environments which supported both hardware and software design, and which helped in the trade-offs which commonly exist between the two technologies. Recognition and analysis of these similarities is currently a topic for research, and early indications are that sufficient commonality exists to motivate further investigation and prototype development of environments to support both hardware and software design. This may be a very interesting field of research over the next few years.

## IPSE standardization

The efficient development of quality computer software is of prime interest to a number of large and powerful organizations throughout the world. Not only will improvement of software development support save many millions of pounds in development and maintenance costs, but also production of high-quality software is vital to a number of life-critical computer applications. In particular, military applications of computers are increasing rapidly, and both NATO in Europe and the DOD in the US, are major software producers and consumers. Hence, the military's preoccupations with standardization and uniformity have been imposed on its use and development of software, with the effect that the many software producers who develop military application software have been subject to this control. The development and use of the Ada programming language has been a prime example. Ada could never have progressed so quickly, nor been accepted so widely, had the US DOD not supported the language as its intended standard software implementation language.

Over the past few years the need for IPSEs within the military arena has been realized, particularly as many military applications have been large, complex systems, prone to development delays and operational inefficiency. This in turn has led to a determination to apply standardization within the IPSE field, with the justifiable goal of allowing tools and tool users to transfer easily between military projects without expensive reworking. However, there is a difference between standardization on the use of a programming language such as Ada, and the attempt to standardize on the use of an IPSE. The difference is basically one of maturity of the fields. While work on understanding, developing, and applying programming languages has taken place over many years, the IPSE field has little practical experience to look back on. And, while the problems of programming language development are now reasonably well understood, the same cannot be said for IPSE development.

Seen in this context, a great deal of care is needed in the present moves towards applying standardization within the IPSE field. There is the danger that any standards which seem currently to be useful will soon be outdated and unused in the near future. These fears have been expressed by a number of IPSE researchers over the attempted imposition of the portable common tool environment (PCTE) as a European standard public tool interface, and in the US there have been many criticisms directed at the DOD's proposed military standard common APSE interface set. In the latter case this has led to a revised standard being developed, informally known as CAIS-A.

In summary we can say that the motivation behind the attempts at establishing standard tool interfaces for IPSEs is well founded: the need for easy tool migration from one IPSE to another. However, with the immaturity of the IPSE area real concerns have been expressed as to the usefulness of such standards in a rapidly changing field. It is clear that this debate is still far from over.

## Summary

The need to provide automated support to aid the process of complex software systems design, implementation and maintenance, led to the production of individual tools to support individual development methods and techniques. Integration of the various facilities provided has been necessary to ensure that the complete project life-cycle is supported in a convenient, flexible manner within a model of the development process. This paper has examined the motivation and objectives of this work, with particular emphasis on the key aims of openness and integration upon which an IPSE is founded. We have classified IPSEs as ‘closed’ and 'open' depending on the exposure they provide to a PTI, and consequently the ease with which new tools can be added to the IPSE. Through providing this analysis, we have been able to compare and contrast some of the major research efforts currently taking place in this area.

## Acknowledgements

This work was carried out as part of the ASPECT project, which is a UK IPSE project funded by SERC through the Alvey Software Engineering Directorate. Special thanks are due to Peter Hitchcock and Brian Randell for their comments on earlier drafts of this paper.

## Notes

1. Rowland, B. R. and Welsch, R. J. (1983) Software development system, Bell Systems Technical Journal, 62, 1, January.

2. Glass, R. L. (1982) Modern Programming Practices - A Report from Industry, Prentice-Hall.

3. McDermid, J. and Ripken, K. (1984) Life-cycle Support in the Ada Environment, Cambridge University Press.

4. Feldman, S. I. (1979) Make - a program for maintaining computer programs, Software Practice and Experience, Bell Laboratories, 9, 255–265, April.

5. Dolotta, D. A. and Mashey, J. R. (1976) An introduction to the programmer's workbench In Proceedings of 2nd International Conference on Software Engineering San Francisco, pp.164–168, October.

6. AT&T (1984) UNIX System V Documenter's Workbench Introduction and Reference Manual. April.

7. Brown, A. W. (1987) A view mechanism for an integrated project support environment. In Proceedings of a Conference on Automating Systems Development. Leicester Polytechnic, April.

8. Systems Designers (1984) DEC/VAX Perspective Technical Overview. November.

9. Bate, G. (1986) Mascot3: an informal introductory tutorial. Software Engineering Journal, 1, 3, 95–102, May.

10. Henderson P. (1976) The TOPD system. Technical Report No. 77, University of Newcastle upon Tyne, September.

11. Osterweil, L. J. and Cornell W. R. (1983) The Toolpack/IST programming environment IEEE Softfair, July.

12. Standish, T. A. and Taylor R. N. (1984) Arcturus: a prototype advanced Ada programming environment. ACM SIGPLAN Notices, 19, 5, 57–64, May.

13. Hausen, H.-L. and Mullerburg, M. (1982)

Conspectus of software engineering environments. In A. I. Wasserman (ed.) Tutorial: Software Development Environments.

14. Stenning V. (1987) On the role of an environment. In Proceedings of the 9th International Conference on Software Engineering, 30–35, March.

15. Lyons T. G. L. (1986) The public tool interface in software engineering environments, Software Engineering Journal, 1, 6, 254–258, November.

16. McGuffin, R. W., Elliston, A. E., Tranter, B. R., and Westmacott, P. N. (1980) CADES - software engineering in practice. ICL Technical Journal, 2, 1, 13-28, May.

17. Robinson, D. S. (1987) Private Communication, December.

18. Buxton, J. N. (1980) Requirements for APSE - STONEMAN. US Department of Defence, February.

19. Hall, J. A., Hitchcock, P. and Took, R. (1985) An overview of the ASPECT Architecture. In J. McDermid (ed.) Integrated Project Support Environments. Peter Peregrinus.

20. Alderson, A., Bott, M. F. and Falla, M. E. (1985) An Overview of the Eclipse Project. In J. McDermid (ed.) Integrated Project Support Environments. Peter Peregrinus.

21. Warboys, B. C. (1986) IPSE 2.5. In Proceedings of Joint IBM/University of Newcastle upon Tyne Seminar, September.

22. Morgan, D. (1987) The imminent IPSE. Datamation, 33, 7, 60–68, April.

23. Humphrey, W. S. (1985) The IBM large-systems software development process: objectives and direction. IBM Systems Journal, 24, 2, 76-78.

24. Hoffnagle, G. F. and Beregi, W. E. (1985) Automating the software development process. IBM Systems Journal, 24, 3, 102–120.

25. US DOD (1985) Common APSE Interface Set (CAIS). Proposed MIL-STD-CAIS. January.

26. US DOD (1985) Requirements and Design Criteria for the Common APSE Interface Set (RAC). September.

27. Bull, ICL, Nixdorf, Olivetti, and Siemens (1985) PCTE: A Basis for a Portable Common Tool Environment - C Functional Specification.

28. Campbell, I. (1986) PCTE Proposal for a public common tool interface. In I. Sommerville (ed.) Software Engineering Environments. Peter Peregrinus.

29. Stucki, L. G. (1983) What about CAD/CAM for software? - the ARGUS concept. SOFTFAIR '83, IEEE. 129-144.

30. Katz, R. H. (1983) Managing the chip design database. IEEE Computer, 26–36, December.

31. Encarnacao, J. and Krause, F. L. (1982) File Structures and Databases for CAD. North-Holland.

32. Ketabchi, M. A. and Berzins, V. (1987) Modeling and managing CAD databases. IEEE Computer, 20, 2, 93–102, February.

33. Buchmann, A. P. (1984) Current trends in CAD databases. Computer-Aided Design, 16, May.

34. Boerstra, M. L. (ed.), Engineering Databases. Elsevier.

35. Brown, A. W., Earl, A. N., Hitchcock, P., Weedon, R. and Whittington, R. P. (1986) The use of databases for software engineering. In E. A. Oxborrow (ed.) Proceedings of the Fifth British National Conference on Databases (BNCOD5), July.

36. Kim, W. and Batory, D. S. (1985) Modeling concepts for VLSI CAD objects. ACM Transactions on Database Systems, 10, September.

37. Katz, R. H. (1984) Transaction management in the design environment. In Garadin and Gelenbe (eds.) New Applications of Databases. Academic Press.

38. Lorie, R. A. (1981) Issues in Databases for Design Applications. IBM Research Report.

39. Frost, R. (1986) Introduction to Knowledge Based Systems. Collins.

40. Stenning, V. (1986) An introduction to ISTAR. In I. Sommerville (ed.) Software Engineering Environments. Peter Peregrinus.

![](/api/attachments/QB7Y9Q86/fulltext/images/72b49984b927f6b6ad389ea4fec61b9083300778ea972bad90698322366feab5.jpg)

## Biographical notes

Alan Brown graduated in 1983 with a first class honours degree in Computer Science from the University of Hull. After working in industry for a year he joined the University of Newcastle upon Tyne as a PhD student and was soon recruited as a Research Associate for the ASPECT project, one of the UK Alvey-funded software engineering IPSE projects. In this capacity he was responsible for designing and building an abstraction mechanism to augment the database facilities which formed the heart of the ASPECT IPSE. In 1988 Dr Brown received a PhD for his thesis entitled 'A view mechanism for an integrated project support environment'.

In the summer of 1988 Dr Brown joined the University of York as a lecturer in the Department of Computer Science where his main research interests are in object-oriented database systems, IPSE technology, and in the application of IPSE ideas into other areas, in particular VLSI systems.

Address for correspondence: Department of Computer Science, University of York, Heslington, York Y01 5DD.
