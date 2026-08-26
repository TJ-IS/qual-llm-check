---
otero_id: 21581
otero_key: "4Z34DNZA"
title: "Migrating to the Web: a Web financial information system server"
authors: "Seng-cho T Chou"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00034-7"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Migrating to the Web: a Web financial information system server

Seng-cho T. Chou )

Department of Information Management, National Taiwan UniÕersity, 50 Lane 144 Keelung Road, Section 4, Taipei, Taiwan

## Abstract

As Intranets are getting more and more popular in business use, the needs for Web information systems are becoming obvious. This paper reports our efforts involved in the implementation of a Web DSS server, which is migrated from a stand-alone DSS server. We describe the various aspects of the system in detail, and propose a generalized Web information system architecture, which works as a reference architecture for a wide class of information systems over the Web, including DSS. The discussion also covers current technologies being used in this project including HTML, CGI, Java, and Web databases, and addresses open problems that require further research and development efforts. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Web information system; Information system architecture; Web database; DSS; Intranets; Network computing; Financia engineering

## 1. Introduction

There is no doubt that the World Wide Web <sup>w</sup> <sup>x</sup> 13,18 , otherwise known as the Web, has become one of the most exciting new-comers as an information dissemination media in recent years. It has attracted and affected people from all walks of life. The Web offers many advantages over traditional media, being inexpensive and widely used by industry for information sharing and product promotion. It is a rich and interactive media that is superior to its traditional counterpart, and offers many technical advantages due to its set of open standards. With appropriate tools, users can get information and services via the Web through any of the hardware and software platforms. It does not matter whether the machine is a personal computer PC , a Mac, or aŽ . workstation; neither does it matter whether it is running MS Windows, MacOS, or UNIX. Everyone can hook on to the Web and benefit from it.

As the Internet is getting more and more popular as the backbone of the global information infrastructure, the Web is no longer for information display only. In particular, for Intranet applications, information systems over the Web, or Web ISs, will be playing a key role in business 6 . For information<sup>w</sup> <sup>x</sup> workers, migrating into the Web is an unavoidable trend. The Web and Internet are definitely becoming the information infrastructure of the next generation information systems. Many questions pop up in our mind when we are getting ready to develop Web ISs. For instance, how is the Web environment different from the traditional IS environment? How should existing information systems be migrated to the Web world?

In an attempt to get some insight in this direction, this paper reports our efforts involved in the implementation of a Web decision support system DSSŽ . server, which is migrated from a stand-alone DSS server. We describe the various aspects of the system in detail along with the current technology being used in the project. We then propose a generalized Web IS architecture, which works as a reference architecture for a wide class of information systems over the Web, including DSS. We also report our experience and address open problems that require further research and development efforts.

## 2. The original system and its goals

Stock trading DSS based on various artificial intelligence AI technologies including neural net-Ž . work, genetic algorithms, and fuzzy expert systems, have been an active research area in financial engineering over the years 1,7,19,21 . Most of the sys-<sup>w</sup> <sup>x</sup> tems seen today are fixed in their software components; consequently, it is not easy to modify these systems to meet the changing needs of the environment. In order to deal with this problem, we have implemented a system, Flexible Intelligent Financial Engineering System FIFES 2 , which allows oneŽ . <sup>w</sup> <sup>x</sup> to generate specific DSSs according to one’s needs.

FIFES consists of three main subsystems, namely, a user-friendly graphical user-interface GUI sub-Ž . system, a model base subsystem, and a data management subsystem. The GUI supports a graphical enduser computing facility for users to set up their specific DSSs. The model base subsystem is responsible for the management of a variety of analytical modules, pre-processing modules, and postprocessing modules. The analytical modules are built upon AI technologies. Any specific DSS is made up of modules stored in the model base subsystem. The data management subsystem provides facilities for the storage and management of stock trading data for, and the results generated by, specific DSSs. To make a specific DSS or a project in FIFES, a user picks one or more of the needed pre-processing, analytical, and post-processing modules and indicates how they shall be connected through the GUI subsystem. FIFES is a stand-alone system which is designed for use by a single user but allows multiple specific DSSs to be generated.

The flexibility to allow users to generate any specific system according to their needs is the most important feature of FIFES. Since the market is changing constantly, any specific system tends to become obsolete after a short period of time. Investors often want to change their trading strategies from time to time. FIFES is aimed at making it possible for users to easily build financial engineering systems suited to their needs.

## 3. Migrating to the Web

It has been our goal to allow people outside of our research group to try out FIFES and to share and promote the use of AI technology in financial applications. Many alternatives for distributing FIFES are possible, but the Web is perhaps the easiest and least expensive way to make the research results available to a wide audience. For instance, instead of distributing demonstration disks, dealing with problems related to installation, version upgrade, and more importantly the daily update of financial data, not to mention the cost of making the disks and other distribution materials, an immediately available and constantly updated system on the Web would be void of all these problems.

With this in mind, the original stand-alone system would have to assume a new role. Our idea is to make it a server system under the Web. This server will then be accessed by any Web client with the standard Web setup—HyperText Markup Language Ž . HTML browser. Anyone who hooks onto the Web can then try out our system with very little overhead. The new system will be a client<sup>r</sup>server CŽ . <sup>r</sup>S system with the following characteristics: on the client side, it will be a front-end system to work with Web clients to get their service requests and to present results to them. The server, on the other hand, supports the construction of specific DSSs and the execution of any specific DSS. It needs to provide services for the management of specific DSSs, system components, and financial data management.

More importantly, it has to support concurrent access of the system. Data communication is through the Internet with standard communication protocols such as the Transmission Control Protocol<sup>r</sup>Internet Protocol TCPŽ . <sup>r</sup>IP 12 observed by both the client and<sup>w</sup> <sup>x</sup> server.

The new system configuration brings up a set of issues that were not considered in the original system. A description of these issues follows.

## 3.1. Front-end modules deÕelopment

A user-friendly front-end is often the emphasis of stand-alone systems such as FIFES. But when migrating to the Web, platform independence becomes more important. The front-end should be composed of platform independent modules for information display, service requests handling, and results presentation.

## 3.2. Client’s sharing of workload

One common characteristic of Web applications is that most of the work is done by the Web server. The client does nothing more than displaying the contents of HTML pages. This mode works fine for applications focusing on information display only. For applications that take up CPU cycles, the performance of these applications will get worse when the server needs to serve multiple clients. One way around this problem is to off-load some of the work from the server to the clients, whenever possible, allowing the server to work on a more important task—the service of more clients.

## 3.3. Remote access of serÕices

Service modules are the core of information systems. A Web IS server is loaded with service modules, which are invoked upon clients’ requests. In a client<sup>r</sup>server environment, this amounts to a remote service invocation as opposed to local sub-program invocation in a stand-alone system. One word about service modules is worth mentioning when switching to the Web world. Since these service modules often encapsulate much specific knowledge about the applications that the information system is designed for, reuse of these modules to the best possible extent is important to avoid expensive, time-consuming, error-prone total re-implementation.

It is also common for the client front-end to communicate with a database back-end for information retrieval and update when information will need to be shared back and forth between the front-end and the back-end. Such a service would need to be provided under the Web environment.

## 3.4. New source of data

There is no doubt that the Web is an informationrich environment. Information that used to be ‘offline’ can now be accessed through the Web. For instance, the daily financial data of the Taiwan stock market is now available on the Web. It is desirable to efficiently incorporate data from the Web with applications on hand as this results in a fast, accurate, and inexpensive way of data acquisition. Of course, data management cannot be neglected when more and more data become available. Allowing data to be stored in piles of files can lead to undesirable outcomes.

## 3.5. Concurrent access

When a system goes to the Web, it potentially opens up to many users. Many Web sites are currently for information display only and therefore concurrent access is not a problem. But when it comes to the type of servers we have in mind, concurrent data update conflicts become obvious and the exercise of concurrency control is necessary.

## 3.6. Multi-serÕer coordination

For the sake of performance and service provision, a single server might not be sufficient. In the former case, we might want to add multiple servers to boost up performance. In the latter case, services might be distributed among different servers. Therefore, the coordination of these servers is necessary to either balance the workload, to direct clients’ requests to the appropriate servers, or both.

## 4. The new system

In this section, we give an in-depth account of the proposed system, covering the functional view, the run-time architectural view of the system, and sample screen shots to show how the issues are being dealt with in the proposed system.

## 4.1. Functional Õiew of the system

We start with the functional view of the system. The functions supported by the new system are summarized in Fig. 1. A brief description of the major functional components follows.

From the user’s perspective, the functions supported by the system include login validation, project construction, project execution, and result presentation and status check. In addition, certain privileged functions, which can only be done at the server station, are also supported, including the addition of new project components, new financial data, user management, system maintenance, and database administration functions. Project construction provides facilities for the selection of project components, specification of their connections, and specialization of components; together they make up the definition of a project to be stored in the system’s database.

Project execution allows users to browse through the projects stored in the system database and to pick the one to be executed. Once the selection is made and the execution request is issued, the project will be executed at the server side. The status and the results of the execution can be obtained through the result presentation and status check function.

![](/api/attachments/4Z34DNZA/fulltext/images/d742da2d4f5a995475df186015eb01e0a6391fbbb1080b4a51277574d732bcd1.jpg)  
Fig. 1. Functional view of the system.

As promoted by the network computing model, the installation of new software modules and databases is all done at the server site such that all clients can take advantage of what is on the server without the need of worrying about installation, maintenance, upgrades, and other related problems.

## 4.2. Run-time architecture

The run-time architecture of the system is diagrammed in Fig. 2. The system is a client<sup>r</sup>server system on the Internet<sup>r</sup>Intranet environment. Clients can log into the system through any machine running the standard Java-enabled HTML browser. The server station is a Pentium 133 with 32 MB RAM and 1.2 GB hard-disk running Microsoft’s NT. The Web server is the public domain WebSite 20 . In what<sup>w</sup> <sup>x</sup> follows, we first talk about the front-end and Web database back-end of the new system. Then we describe how the original DSS server is modified to be coupled with the front-end and back-end components to make a Web information system server.

## 4.2.1. Front-end

As shown, the front-end module consists of several components including the user-interface, project management, and result presentation. The front-end module is responsible for user login and validation, project construction, project execution, information display, and result presentation. A client invokes the system by connecting to the homepage of the system through the standard HTTP protocol, which will cause those components to be loaded from the server to the client station.

The front-end is partially developed in HTML 4 , <sup>w</sup> <sup>x</sup> which can then be read by any HTML browser. HTML is a rich presentation language for the development of hypertext-based user-interface screen pages. HTML is platform independent and is fundamental in the Web environment, but is insufficient for the full functionality of the front-end module. For example, a windowing user-interface with pull-down

Web Browser

![](/api/attachments/4Z34DNZA/fulltext/images/c891d604ffeeb34d4091c9163f62fee98396e9844acf21caea507f2c0454c8a2.jpg)  
Fig. 2. Run-time system architecture.

menu support cannot be handled by HTML see Fig. Ž 3 for the sample screen shots. Java 16 from Sun- . <sup>w</sup> <sup>x</sup> Soft is by far the most important development language that can help make this happen. Java programs can be designed in such a way that they are loaded from the server and executed by the clients with a Java-enabled browser. The rest of the front-end module is therefore written in Java as Java applets attached in the homepage of the system.

By virtue of Java applets that are executed at the client side, the front-end module is also designed to share the workload of the system. For example, the graph plotting program of the result presentation component is written in Java and is to be executed solely at the client side.

We should also mention that the original system has a user-friendly graphical end-user computing facility for the construction of specific DSSs. This portion cannot currently be easily ported to the Web environment without involved development efforts. So, a fill-in-the-blank approach is taken in place of this graphical end-user computing interface.

## 4.2.2. Data management

The data management component is responsible for the management of the data for the system as

well as for individual DSSs. The former refers to the information about project components and definitions, and the latter refers to the data obtained from an external source through manual or automated processes and results generated by individual DSSs. Database support in the Web environment has re-

![](/api/attachments/4Z34DNZA/fulltext/images/64cf643f8fa1afb6c4ac57512564d629edba7ddd8eeb3b50053883686eba450c.jpg)

![](/api/attachments/4Z34DNZA/fulltext/images/c74413e92cd591c5a2eb042ad7a7763fcaf292f596d6be38bfce2cde32c58cdb.jpg)  
Fig. 3. Sample system screen shots: the specification of a the preprocess module, b the neural module, and c the postprocess module of Ž . Ž . Ž . some particular project; d the execution of the project on the WIN 32 environment at the server; and e and f two forms of resultŽ . Ž . Ž . presentation.

![](/api/attachments/4Z34DNZA/fulltext/images/69610507d325eeebb6312563533c888400530244108aa425804ac611cd163041.jpg)

![](/api/attachments/4Z34DNZA/fulltext/images/2645c5da8cd5ff305632d5511f12410243ddfd91998e0a9ae19feef264e5eabd.jpg)  
Fig. 3.

cently gained much attention from the database community 14,10 . To manipulate databases through the<sup>w</sup> <sup>x</sup> Web, a common approach is through the Common Gateway Interface CGI 4 . For example, a CGIŽ . <sup>w</sup> <sup>x</sup> program written in C <sup>q q</sup>, Visual Basic, or any appropriate language can manipulate databases through the Open Database Connectivity ODBCŽ . <sup>w</sup> <sup>x</sup> 11 protocol. Database vendors also have their own more efficient approach for their own databases. For instance, Web SQL 15 from Sybase can be used to work with the Sybase SQL Server or databases from other vendors. The Practical Extraction and Report Language PERL 5 is often used in this case.Ž . <sup>w</sup> <sup>x</sup> However, the need for parsing input parameters in a CGI program and the use of PERL with Web SQL for data access do add extra complexity to the development of these database applications.

(e)  
![](/api/attachments/4Z34DNZA/fulltext/images/5590555682bf8ea2dab7bf1ddfe0e14adf5a0acc0a1b9749fd7c05a340ee9520.jpg)

(f)  
![](/api/attachments/4Z34DNZA/fulltext/images/8249ed10a4070b478c0959d6e239399494d8d0449673e2a63f96f471f9d27e10.jpg)  
Fig. 3.

Java is again an important general purpose object-oriented language for the development of Web database applications. Through appropriate middleware supporting the standard protocols such as ODBC and JDBC 9 , most database systems available today <sup>w</sup> <sup>x</sup> can be accessed by programs written in Java using standard SQL 10 . The combination of Java and <sup>w</sup> <sup>x</sup>

SQL is also much cleaner when compared to the alternatives mentioned above.

In our system, the front-end module works with the underlying database using the JDBC and ODBC protocols through the help of a middleware Dataramp <sup>w x</sup> <sup>w x</sup> 3 and a JDBC-ODBC bridge by JavaSoft 8 . The underlying database can be any database server that honors the ODBC protocol. Our current implementation makes use of Sybase SQL Anywhere that comes with PowerBuilder 5.5.

Besides the storage and management of data for the system and individual DSSs, the underlying database management system also helps support concurrent user access to the system through its standard transaction management facility. For example, concurrent read<sup>r</sup>write access to the project definition table has to be coordinated.

## 4.2.3. DSS serÕice modules

With the front-end and back-end database being in place, the next step is to couple the original system with the new environment. We start with the front-end. A common straight-forward approach is to allow the front-end to invoke individual DSS through CGI. CGI sets up a way for clients to invoke server’s modules to be executed on the server side. The advantages of this approach are two-fold: it is simple, and, more importantly, it makes it possible to salvage existing program modules of the original system, in particular, when user interactions are not involved. Since the core of any specific DSS is its analytical AI modules that have little interaction with users, they are good candidates to be turned into CGI programs.

For reasons that we will address below, direct conversion of existing programs into CGI programs is not sufficient. A dispatcher daemon is therefore introduced as shown in Fig. 2. The dispatcher is written in C<sup>qq</sup> or any language that has the capability to fork off child processes. The sole responsibility of the dispatcher is to invoke individual DSSs to work. It does it by consulting the project definition table for the project specified by a CGI program originated from some particular client and then invokes the project accordingly. A CGI program carrying a client’s request for the execution of some specific project communicates with the dispatcher through a socket connection 12 , which will be<sup>w</sup> <sup>x</sup> further explained below. Since the server station is a Pentium PC running NT, the WIN 32 operating environment is chosen for the child processes. Such an arrangement makes salvage of existing DSSs possible. In fact, individual DSSs from the original system were directly reused with almost no change.

The salvage of DSS programs did save development time but the ramification, however, was that the data source for these programs could not be changed. The original program modules make use of files directly, while our new environment stores data in the database. So, data extraction programs were written to extract data from the database to form data files to be used by the program modules. With the appropriate setup of file directories, each DSS will have its own working space for each client such that a multi-user computing environment is supported.

So, through CGIs and a dispatcher daemon, we achieve the goal of integrating legacy DSSs into the Web environment, and the WIN 32 and local file directories provide an isolated working space for each running project in a multi-user computing environment.

The main reason for the setup of the socket connection between a client’s CGI program and the dispatcher daemon is for dealing with the auto-disconnection problem in the Web environment due to the invocation of long processes. Owing to the timeout feature and the connectionless nature of the Web, a Web link between a client and a server could be disconnected when there is no traffic between them. This could happen when the server is busy undertaking a long process for the client. When the link is terminated, the on-going long process will be canceled as well. One way around this problem is to have the server invoke a separate independent process for the client’s long process in such a way that the client and server can continue communicating without the need to wait idly for the termination of the long process. Not surprisingly, most of the DSSs in our system do take some time to run. We therefore make use of the socket connection and the dispatcher daemon for this purpose. We also provide the status check facility for clients to check the status of the execution of the projects; in particular to get to know when the projects are terminated. The result presentation facility allows a client to retrieve the result data produced from a project upon its successful completion.

For the sake of performance or integration of service, multiple servers might be involved. The coordination of these servers is necessary to either balance the workload, to direct clients’ requests to the appropriate servers, or both. The similar socket setup will also enable the dispatcher to get help from, and to coordinate the activities of, these cooperating servers.

The current architecture does not prevent us from developing new project components in languages other than C<sup>qq</sup>. We anticipate that new modules will be developed in Java as Java applications, and then the data in the database can be directly used without the need to go through the data extraction process.

## 4.3. Sample screen shots

Given in Fig. 3 are some of the major screen shots to show the I<sup>r</sup>O and run-time characteristics of the system. The client station is a SUN Classic running the Netscape 3.01 browser.

## 5. Reference architecture

The discussions above are not unique to the particular system proposed in this paper but are common to most information service servers in the Web environment. In this section, we present a generalized Web IS architecture, which works as a reference architecture for the design and development of a wide class of Web information systems including DSS.

Shown in Fig. 4 is a three-tier client server architecture with layered service supports. On the client side, the front-end module provides all the needed facilities and the user-friendly interface for the use of the system, whose facilities are at the disposal of the clients. Front-end modules in the Web environment are stored in the server and loaded at run-time to be executed at either the client or server sites depending on the nature of the services.

On the servers’ side, there are four layers of services with level 0 services provided by the data server and three others by the application server. Explanations follow.

## 5.1. LeÕel 0: data storage and management

The data server at level 0 provides the facilities to handle the data of the information system. The data may include those for the system and those for the applications. An example of the system data is the information about projects in our system such as the components information for the construction of specific projects and project definitions. The large amount of stock financial data is an example of the application data. The core of this module is typically a database management system. Note that the data server does not have to reside at the same machine as the Web server. If there are cooperating servers in the system, data could be distributed and<sup>r</sup>or replicated among these servers. Efficient integrated database services would therefore be a main topic of concern in this module.

![](/api/attachments/4Z34DNZA/fulltext/images/2d116b71ddd4ac4fea6135e6cc68e897982b2d61c918bb25cfea749b0698b82f.jpg)  
Fig. 4. Web IS reference architecture.

## 5.2. LeÕel 1: multi-user concurrent access control

An information system server on the Web oftenŽ . needs to deal with more than one client at the same time; therefore, the exercise of multi-user access control is needed to avoid conflicts due to concurrent updates on both system and application data, and other related problems. Along with the help of the database system at level 0, this module provides the necessary facilities to safe-guard the data for the system. Besides the database, our example system also takes advantage of the run-time operating environment and directories of local file systems to provide this level of service.

## 5.3. LeÕel 2: application-dependent serÕices

Every information system server provides someŽ . specific services. It is the module at this level that supports all these services. For instance, in the system we are building, this module provides many specific DSSs to be invoked by users. The construction of new DSSs are also supported. Consolidation of external data into the system database might also be part of the services supported by this module. Although services provided at this level are application-dependent, one thing in common is that this module often makes use of, and manipulates, data managed by the facility at level 0, the data storage and management module. This module also needs level 1 services, should it modify the stored data for multiple clients at the same time.

## 5.4. LeÕel 3: multi-serÕer coordination

Although a client on the Web communicates with the main server, nothing prevents us from having multiple servers to serve the clients. In this architecture, we refer to the other servers as cooperating servers. There are two main reasons for the need of cooperating servers. One is to distribute the work among multiple servers to relieve the workload of the main server for performance purpose. In this case, this module is responsible for load-balancing the servers involved. Another reason refers to the situation where specific services might be resided in a certain server but not in the others. In this case, this module needs to direct service requests to the appropriate servers.

## 6. Lessons learned

As Intranets are getting more and more popular, the idea of network computing with centralized management of software, but with distributed processing and accessing capability, is attractive to the users of an organization. Our system is constructed under the same philosophy. Most of our users are students in the financial engineering and data mining classes. They do enjoy the benefit of the facilities provided without the worry of system installation and maintenance. They can construct new projects, fine-tune projects or try out projects on different periods of data. They can even demonstrate their systems anywhere they desire. Such a Web IS setup is well-received. Before the completion of this experimental prototype, we previously had to port the whole system setup to another machine in order to install it for their use. The involved effort is substantial due to such problems as system installation, data collection, and update. The current setup is, however, still a bit limited in the sense that the incorporation of new modules and daily data still has to go through the main server workstation. It is also a bit slow as the prototype system is running on a basic Pentium PC with no cooperating servers, and Java is still in its infancy.

The three-tier reference architecture and the implementation framework, in particular the Web database facility and the Java computing environment, are useful references for the construction of other Intranet information systems. We are currently building a document workflow management system using the same architecture. Other Web information systems with similar server architectures and Intranet computing environments are being planned.

The software development environment for Web applications is changing very rapidly. This is most obvious in the setup of the Web database access environment. We have gone through CGI, Web SQL with PERL, and later Java with JDBC<sup>r</sup>ODBC in just half a year. The latest introduction of Java seems to ease these rapid changes as Java is potentially becoming the dominant language<sup>r</sup>environment for the development of Web applications.

Our experience also indicates that the DSS program modules of the original system are salvaged and directly incorporated into the new system. The rest such as the user-interface and the project construction modules are modified to a certain degree or totally re-constructed. Nevertheless, the savings in the development effort is still substantial enough for us to enjoy an early success in this Web information system prototyping project.

## 7. Concluding remarks

As Intranets are getting more and more popular in business use, the needs for Web information systems are becoming obvious. This paper has touched on the topics including Web IS architecture and system development, migration from existing traditional ISs to the Web environment, and Web database supports. While our prototype system is taking shape, the reference architecture has guided us through many issues involved in the development of information systems on the Web. This paper, while reporting our system migration experience, has brought up many issues that deserve further research and development efforts. Our list of future work includes such problems as integrated database environment for efficient data access and transaction management, parallel processing and load-balancing strategies with cooperating servers, and user management and protection. Many tools are on our wish list. We have seen some on the horizon 8,17 while others are still yet to<sup>w</sup> <sup>x</sup> come. These tools will relieve the efforts needed for the development of Web ISs.

## Acknowledgements

This research has been partly supported by the National Science Council under grant NSC 86-2416- H-002-008.

## References

1 S.-c.T. Chou, C.-C. Yang, C.-H. Chen, F. Lai, A Rule-based Neural Stock Trading Decision Support System, IEEE<sup>r</sup>IAFE

Conference on Computational Intelligence for Financial Engineering, New York, March 1996, pp. 148–154.

<sup>w</sup> <sup>x</sup> 2 S.-c.T. Chou, The Implementation of a Stock Trading Decision Support Systems Development Platform, TR:NSC-86- 2416-H-002-008, Department of Information Management, National Taiwan University, 1997.

<sup>w</sup> <sup>x</sup> 3 Dataramp, http:<sup>rr</sup>www.dataramp.com.

<sup>w</sup> <sup>x</sup> 4 I.S. Graham, HTML Source Book, 2nd edn., Wiley, 1996.

<sup>w</sup> <sup>x</sup> 5 A. Humphreys, M. Glover, PERL 5 How-to, Waite Group Press, 1996.

<sup>w</sup> <sup>x</sup> 6 Intranets Redefine Corporate Information Systems, http: <sup>rr</sup>home.netscape.com <sup>r</sup>comprod<sup>r</sup>at\_work<sup>r</sup>white\_paper<sup>r</sup>indepth.html, 1996.

<sup>w</sup> <sup>x</sup>7 G.-S. Jang, F. Lai, Intelligent Stock Market Prediction System Using Dual Adaptive-Structure Neural Network, Proceedings of Second International Conference on Artificial Intelligence Applications On Wall Street, New York, 1993, pp. 288–294.

<sup>w</sup> <sup>x</sup> 8 JavaSoft, http:<sup>rr</sup>splash.javasoft.com.

<sup>w</sup> <sup>x</sup> 9 JDBC, http:<sup>rr</sup>www.javasoft.com.

<sup>w</sup> <sup>x</sup> 10 B. Jepson, JAVA Database Programming, Wiley, 1997.

<sup>w</sup> <sup>x</sup> 11 Open Database Connectivity, Microsoft Press.

<sup>w</sup> <sup>x</sup> 12 W.R. Stevens, TCP<sup>r</sup>IP Illustrated, Vol. 3, Addison-Wesley, 1996.

<sup>w</sup> <sup>x</sup> 13 R. Stout, The World Wide Web Complete Reference, Mc-Graw-Hill, 1996.

<sup>w</sup> <sup>x</sup> 14 M. Swark, D. Kittel, WWW Databae Developer’s Guide, Sams.Net Publishing, 1996.

<sup>w</sup> <sup>x</sup> 15 Sybase Web.SQL Product Specification.

<sup>w</sup> <sup>x</sup> 16 A. van Hoff, S. Shaio, O. Starbuck, Hooked on Java, Addison-Wesley, 1996.

<sup>w</sup> <sup>x</sup> 17 S.E. Varney, Datawebs! Datamation, April 1996, pp. 38–47.

<sup>w</sup> <sup>x</sup> 18 W3 Consortium, http:<sup>rr</sup>www.w3.org.

<sup>w</sup> <sup>x</sup> 19 F. Wong, C. Tan, Hybrid Neural, Genetic, and Fuzzy System, Trading on the Edge, Wiley, 1994, pp. 243–261.

<sup>w</sup> <sup>x</sup> 20 WebSite Web server, http:<sup>rr</sup>website.ora.com.

<sup>w</sup> <sup>x</sup> 21 C.-C. Yang, S.-c.T. Chou, W.-H. Chu, F. Lai, Using AI in developing market predictions: a study of the pacific-basin capital markets, in: R.S. Freedman, R.A. Klein, J. Lederman Ž . Eds. , The Handbook of Financial Applications of Artificial Intelligence, Probus Publishing, 1994, pp. 139–157.

![](/api/attachments/4Z34DNZA/fulltext/images/d472232614b4e0cfb1abd200d44144ffade20f329d941e462b98185b1a080bc5.jpg)  
Seng-cho T. Chou is a Professor in the Department of Information Management at the National Taiwan University. He received his PhD in Computer Science from the University of Illinois at Urbana-Champaign in 1991. His research interests center around Web information systems including databases integration, information retrieval, document management, workflow, and security, and artificial intelligence in data mining and financial applications.
