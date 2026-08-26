---
otero_id: 6630
otero_key: "DYF7SDDS"
title: "A new collaborative system framework based on a multiple perspective approach: InteliTeam"
authors: "Ibrahim Cil; Oguzhan Alpturk; Harun R. Yazgan"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.03.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A new collaborative system framework based on a multiple perspective approach: InteliTeam

Ibrahim Cil\*, Oguzhan Alpturk, Harun R. Yazgan

Department of Industrial Engineering, Engineering Faculty, Sakarya University, Esentepe Campus, Adapazari 54040, Turkey

Available online 25 May 2004

## Abstract

This study develops a Web-based collaborative system framework based on a multiple perspective approach. This framework is a recent decision support system (DSS) paradigm proposed by Courtney [Decis. Support Syst. 31 (2001) 17] for knowledge management of and decision making about a special organizational problem. It consists of four main components. The first component is a group decision-making (GDM) approach in which many participants’ points of views are considered in the modeling of a specific problem. In the second component, many multiple criteria decision-making (MCDM) techniques are employed. The third component is an intelligent system. The fourth component is related to advanced communications that are supported by new technologies such as mobile tools, mobile e-service, and the wireless application protocol (WAP). A new software system called InteliTeam is developed based on the framework. InteliTeam can be accessed from application service providers (ASP), so installation of the software is not required. The software provides online mapping, online queries, and online analysis functions for users anywhere at any time. An example of the software as tested on many organizational problems is presented to illustrate its effectiveness.

Keywords: Multiple perspectives; Collaborative support system; Multiple criteria; Web-based decision support systems; ERP selection

## 1. Introduction

Organizational environments have become more complicated, interconnected, and global with the increasing use of web and communication technologies. The organizational problems in the future will be even much more complex than those of the past. Therefore, social, environmental, and economic concerns should be taken into account in a decision process. Mitroff and Linstone [53] propose that managers of organizations must consider cultural, organizational, personal, ethical and aesthetical factors in their decision approaches. Organizations and their decision support systems (DSS) have to tackle this complexity and go beyond the technical orientation of previous DSS. Courtney [22] follows Mitroff and Linstone’s approach and proposes that DSS researchers should embrace a much more comprehensive view of organizational decisions to develop DSS for the new century. Courtney suggests a new decision-making paradigm for organizational decision problems. The newly developed DSS should be capable of handling much broader areas than mathematical models and knowledge-based systems did in the past. The new DSS trend is an enormous challenge, but is imperative that the DSS remains a vital force in the future.

In this study, a new collaborative system, Inteli-Team, an abbreviation of ‘‘Intelligence of Team’’, is developed based on Courtney’s DSS paradigm. The InteliTeam consists of web technology, a group decision-making (GDM) process, a large number of multicriteria decision-making methods, and social choice functions. In addition, InteliTeam has both data-driven and model-driven supports for problem solving. It uses an object-oriented analysis and design method and Unified Modeling Language (UML). Web-based programming and an object-oriented design paradigm exist in the architecture of the software. These components provide persistence-mapping functions that integrate a relational database and an object-oriented code.

The environment of the developed system is discussed in the next section. The third section focuses on presenting and explaining the aim and physical, logical, and functional structures of the system. The last section provides an example and discusses the results.

## 2. An assessment of DSS environment

This section summarizes the technologies, approaches, and methodologies that are employed in InteliTeam.

## 2.1. Historical perspective

Decision support originated in the late 1960s, and the application of DSS appeared two decades later. The 1970s was the conceptual and technological development period of DSS. In the mid-1980s, group decision support was widely studied to support decision makers. In the early 1990s, a shift from a mainframe-based DSS to a client/server DSS occurred. In early 1995, the Web was recognized by a number of software developers and academics as a serious platform for implementing DSS, and corporate intranets were later developed to support information exchange and knowledge management. In 2000, ASPs began to host the application software and technical infrastructure that were necessary for decision support capabilities. In the late 2000, a number of frameworks for knowledge management were proposed and developed such as model-driven DSS, data-driven DSS, communication-driven DSS, and knowledge-driven DSS. Recently, the use of Web-based DSS as services has been explored, including the concept of offering decision computation technologies as services on the Web. Web-based decision computation will allow the development of DSS that combine multiple source components to deliver application-specific solution packages. Today, technologically advanced users also expect even more functionality than was once available in DSS technology [8,34,42,65].

## 2.2. A new decision-making paradigm in the DSS environment

In the early 1970s, Gorry and Scott Morton [31] clearly defined the original DSS concept by combining Anthony’s [2] categories of management activity and Simon’s [63] description of decision types. Simon’s decision approach became a conventional DSS decision-making process. The process consists of three phases: intelligence, design, and choice. Intelligence is used in the military sense to search the environment for problems, i.e., the need to make a decision. The design involves the development of alternative ways of solving the problem. The choice analyzes the alternatives and chooses one for implementation.

Courtney [22] recently put forward an alternative decision-making paradigm that uses a multiple perspective approach. The approach introduces many new factors into the picture for organizational knowledge management and decision making. Courtney’s paradigm is illustrated in Fig. 1. The primary difference between this decision model and previous decision models in a DSS context is that multiple and varied perspectives are developed during the problem formulation phase. The heart of the decision process is a mental model of stakeholders with various perspectives [53].

The mental model determines the perspectives that will be dealt with and the data that will be necessary. In contrast to Simon’s approach, the mental model is affected by the steps of a decision process. Courtney’s approach begins with problem recognition, and a number of perspectives are developed. The various perspectives provide much greater insight than normal into the nature of the problem and the possible solutions. They allow tools such as cognitive maps, influence diagrams, entity-relationship diagrams, and object diagrams to be of great value both in illustrating the associative elements and in surfacing assumptions in wicked systems.

![](/api/attachments/DYF7SDDS/fulltext/images/e9edeb6005d10a9ca3c4f69c85fce7bbc43c1882c3f4c88ec9c4d414ae99db5d.jpg)  
Fig. 1. Courtney’s [22] decision-making paradigm for DSS.

## 2.3. Group decision making, GDSS, and collaborative systems

Turban and Aronson [69] argued that the majority of real world decision-making problems involve multiple decision makers. As decision making moves from being an individual activity toward a group activity, many organizations are forming virtual teams of geographically distributed knowledge workers to collaborate on a variety of tasks [13,17,34,52,73]. At present, the need for GDM techniques and support is greater than ever before. This is due to the complexity of business relationships, the greater number of decision makers and organizations that are involved in the decision process, online access to multiple external information sources, and the decreasing in the time allowed for decision making.

## 2.3.1. Group decision-making processes

The GDM methodologies that are presented in the literature provide systematic approaches to how people and groups handle several dimensions of decision processes [3,14,18,36,38]. These include (i) Hwang and Lin’s [36] systems approach to expert judgments/ group participation, (ii) Thompson and Tuden’s [68] contingency model for GDM, (iii) the Vroom and Jago [72] model of participation, (iv) Stumpf et al.’s [67] contingency model for GDM, and (v) McGrath’s [51] typology of group tasks. InteliTeam follows the Hwang and Lin system approach. This allows one to implement Courtney’s decision paradigm in real life. The Hwang and Lin system approach focuses on decision making from a system viewpoint, regardless of the organizational, political, and social factors.

## 2.3.2. GDSS and collaborative systems

The incorporation of computational methods and techniques to help group activities to work concurrently and cooperatively was initiated nearly 15 years ago [55]. Following this idea, special attention has been paid to systems that are able to provide working groups with a set of computational tools that not only facilitate communication between members, but that also structure the decision making processes [1,19,25,26,30,41,48,57,58]. These systems are called group decision support systems (GDSS) and support a group working in unstructured problems. In general, these tools exploit advances in communications to support discussion-oriented tasks in group decision making. DSS technologies constitute an area that is generally referred to as ‘‘computer-supported cooperative work’’ or ‘‘collaborative systems’’, which are used to support unstructured problems. Specifically, collaborative systems enhance the communication-related activities of a team of individuals that is engaged in coordination activities such as computer-assisted communication and problem solving, and help in the evaluation of a decision process [5,34,42,48]. The main difference between GDSS and collaborative systems is that collaborative systems support group discourse tasks by structuring the argumentation, and also provide a formal documentation of the process that is used to arrive at a decision.

## 2.4. Web-based DSS

From the early 1990s, powerful tools such as data warehouses, online analytical processing, data mining, and the Web emerged for building DSS. The Web has attracted enormous interest in recent years, and it may have even a greater impact in the near future [62].

For the time being, the Web environment emerges is a very important DSS development. Web-based DSS reduce technological barriers and make it easier and cheaper to provide decision-relevant information. Web technologies can support group work in four ways [10]: structuring group processes, supporting communication, providing enhanced information processing, and providing modeling capabilities.

The Web allows decision makers to work together to solve a particular problem by applying novel methods, although they might neither be present at the same time in the same place nor constitute a permanent organization. It allows asynchronous interaction, thus improving communication within and between countries. Thus, decision makers can evaluate and rank alternatives, determine the implications of offers, maintain negotiation records, and concentrate on issues instead of personalities.

## 2.4.1. Asynchronous meetings and the Delphi technique

Asynchronous meetings have become common in organizations. Asynchronous meetings, which involve working together without being in the same place or at the same time, offer a potential solution to the organizational problems over the Web environment. The technology is used to overcome space and time constraints that burden face-to-face meetings, to increase the range and depth of information access, and to improve group task performance effectiveness, especially by overcoming process losses [53]. Such meetings rely heavily on documents that are exchanged among participants [5].

The Delphi technique is one of the most widely used structured group process. It is applied to complex and unstructured problems to develop the strongest pro and con arguments for a set of alternative solutions. The technique allows experts to deal systematically with a complex problem or a task. The essence of the technique is fairly straightforward. It comprises a series of questionnaires that are sent via the Web to a preselected group of experts. These questionnaires are designed to elicit and develop individual responses to the problems posed and to enable the experts to refine their views as the group’s work progresses in accordance with the assigned task.

## 2.5. Multiple criteria decision-aid DSS

Developments in multiple criteria decision-making (MCDM) methodology and the popular computerized MCDM methods have provided a set of multiple criteria decision support systems (MCDSS) that can be used in solving problems for a single or group of decision makers [33].

Several generations of MCDSS have been developed and used in real world case studies, taking advantage of the explosive progress of information technology and the improvements in MCDM [8,33,40,47,49]. The first MCDSS that provided a generic tool implements a specific approach to facilitate the exploration of a problem with a view to improving the understanding of the problem situation and to reaching a better informed decision. Some of the early developed DSS are summarized in the first column of Table 1.

The development of visual interactive systems began in the 1980s and continued into the 1990s. Most decision situations have to be tackled by a group of people rather than an individual decision maker. Recently, network systems have appeared for group decision support. Some GDSS are summarized in Table 1.

The latest generation of MCDSS that is based on the integration of Artificial Intelligence and MCDM approaches is called Intelligent MCDSS (Table 1). The present intelligent systems are based on expert systems technology. However, this is in the process of being replaced by a diversity of intelligent systems.

Despite the advances in theoretical and applied research in decision science and all kinds of DSS, decision-aid techniques and systems had only limited effects on decision-making practice and quality in the late 2000s [8,42,46,64].

<table><tr><td>Generic DSS</td><td>Group decision support systems</td><td>Intelligent CDSS</td></tr><tr><td>Decision Lab [39], Brans and Mareschal [11]</td><td>Team Expert Choice 2000, http://www.expertchoice.com</td><td>NEGOPLAN, Kersten et al. [44]</td></tr><tr><td>Expert Choice, Selly and Forman [61]</td><td>Web Hiper, http://www.100gen.fi/english/alkusivu.htm</td><td>ARIADNE, Sage and White [60]</td></tr><tr><td>Criterion Decision Plus, InfoHarvest [37]</td><td>Group V.I.S.A, Belton and Elder [7]</td><td>PLEXSYS, Dennis et al. [24]</td></tr><tr><td>Decision Explorer, Eden [27]</td><td>Group ELECTRE III, Carlos et al. [15]</td><td>MARKEX, Matsatsinis and Samaras [50]</td></tr><tr><td>ELECTRE, Roy [59]</td><td>JUDGES, Colson and Mareschal [21]</td><td>MATEX, Cil and Evren [20]</td></tr><tr><td>HIPRE, Olson [56]</td><td>Co-oP, Bui and Jarke [13]</td><td>FINEVA, Zopounidis and Doumpos [74]</td></tr><tr><td>TESS 6.0, http://www.arlingsoft.com</td><td>MEDIATOR, Jarke et al. [39]</td><td>MIIDAS, Siskos et al. [65]</td></tr><tr><td>MACBETH, Bana e Costa and Vansnick [6]</td><td>HIVIEW http://www.enterprise-lse.co.uk</td><td>FARSYS, Volberda and Rutges [71]</td></tr><tr><td>V.I.S.A, Belton and Vickers [9]</td><td>WINGDSS, Csaki et al. [23]</td><td>FINSIM, Karacapilidis and Pappis [42]</td></tr><tr><td>VIG, Lubich [48]</td><td>HERMES, Karacapilidis and Pappis [43]</td><td>OPTRANS Object, Klein and Grubbstrom [45]</td></tr><tr><td>MIIDAS, Siskos et al. [64]</td><td>Opinions-Online, http://www.opinions-online.com</td><td>RODOS, French et al. [29]</td></tr><tr><td>TELOS, Grigoroudis et al. [32]</td><td>Joint Gains, http://www.decisionarium.hut.fi</td><td>Babylon (http://www.gmd.de)</td></tr></table>

Although most of the DSS software packages in the literature have many new features, they have not adopted any fundamentally new techniques, and are not adequate to compensate for today’s organizational decision problems. We believe that radical changes are required to solve such problems, which is why we developed InteliTeam.

## 2.6. A comparison of DSS software

This section explains the summary of the comparison of DSS software packages that is given in Table 2. The comparison is carried out in terms of functionality, problem-solving method, data type, user type, web technology, brainstorming and surveying, intelligence features, and system requirements. These criteria are chosen by many researchers to compare software packages in the literature [5,6,42,44]. One of the most difficult tasks in this type of research is to decide which DSS should be included in the overview. We use 10 well-known software packages in the comparison.

The results of the comparison show us that InteliTeam is quite different from the other software packages:

1. One of the important differences is that most of the present tools have been developed based on MCDSS, GDSS, and Expert systems. In contrast,

InteliTeam is based on a collaborative system. The collaborative system consists of:

(i) asynchronization and collaboration, which are provided by the Web;

(ii) many MCDM methods and social choice functions;

(iii) visualizations and the accessibility of data and information;

(iv) sharing the data among participants; and

(v) screening, sifting, and filtering the data, information, and knowledge.

2. InteliTeam differs from existing DSS in terms of its decision-making process. The most popular traditional DSS are based on the decision-making processes that Simon defined. However, Inteli-Team was developed according to a multiple perspective approach.

3. InteliTeam has multiple functions, and the existing DSS have only one function. For example, Opinion-Online is only capable of voting and surveying; Decision Explorer can only structure problems with cognitive methods; and Expert Choice 2000 can only overcome hierarchically problematic structuring characters and use the wellknown AHP method. In addition, InteliTeam aims to integrate and exploit the best feature of these tools within an integrated collaborative system.

4. InteliTeam contains a large number of social choice functions and outranking and preference aggregation techniques. This is a very useful extension of the traditional stand-alone computerbased DSS or GDSS. To select a method from among many, a user can decide which intelligent system that they will use for a specific method choice.

T<sub>a</sub>bl<sub>e</sub> 2  
A C<sub>ompar</sub>i<sub>son o</sub>f <sub>we</sub>ll-k<sub>nown</sub> DS S <sub>so</sub>ft<sub>ware</sub>

<table><tr><td></td><td>Web-HIPRE</td><td>Criterion decision plus</td><td>Expert choice 2000</td><td>Opinions-Online</td><td>HIVIEW</td></tr><tr><td>Functions</td><td>Problem structuring, multicriteria evaluation and prioritization</td><td>Structuring and analyzing complex decisions</td><td>Hierarchical defining goals and criteria, building model, evaluating alternatives</td><td>Generating private and customized sites for voting and surveys</td><td>Constructing a model, scoring, setting preferences, analyzing the model</td></tr><tr><td>Problem solving methods</td><td>AHP, SMART, SWING, SMARTER</td><td>AHP, SMART</td><td>AHP</td><td>-</td><td>SMART</td></tr><tr><td>User</td><td>MultiUser</td><td>Single-user</td><td>Single/multiuser</td><td>Multiuser</td><td>Multiuser</td></tr><tr><td>Data/information</td><td>Hard data</td><td>Hard data</td><td>Hard data and soft information</td><td>Hard data and soft information</td><td>Hard data</td></tr><tr><td>Web technology</td><td>Java-applet</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Brainstorming and surveying</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Intelligence features</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>System requirements</td><td>Web-based</td><td>Windows 95/98/2000/NT/XP</td><td>Windows 95/98/2000/NT/XP</td><td>Web-based</td><td>Windows 95/98/2000/NT/XP</td></tr><tr><td>Website</td><td>http://www.100gen.fi/english/alkusivu.htm</td><td>http://www.infoharvest.com</td><td>http://www.expertchoice.com</td><td>http://www.opinions-online.com</td><td>http://www.enterprise-lse.co.uk</td></tr><tr><td></td><td>Logical decisions</td><td>Joint Gain</td><td>JUDGES</td><td>TESS 6.0</td><td>Decision explorer</td></tr><tr><td>Functions</td><td>Modeling problems hierarchically, analyzing and ranking</td><td>Negotiation</td><td>Collective selection and/ or ranking alternatives, hierarchical clustering</td><td>Collaborative decision- making, organizing priorities, analyzing results, creating what-if scenarios</td><td>Generating Cognitive Maps</td></tr><tr><td>Problem solving methods</td><td>SUF, AHP,</td><td>Method of Improving Directions</td><td>Electre I,II,III, Promethe I,II</td><td>Weighted Average Method/ Benefit based Decision method</td><td>Cognitive Mapping</td></tr><tr><td>User</td><td>Single user</td><td>Multiuser</td><td>Multiuser</td><td>Multiuser</td><td>Expert-participants</td></tr><tr><td>Data/information</td><td>Hard data and soft information</td><td>Hard data</td><td>Hard data</td><td>Hard data</td><td>Soft information</td></tr><tr><td>Web technology</td><td>No</td><td>Java-applet</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Brainstorming and surveying</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td></tr><tr><td>Intelligence features</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr><tr><td>System requirements</td><td>Windows 95/98/2000/NT/XP</td><td>Web-based</td><td>Windows 95/98/2000/NT/XP</td><td>Windows 95/98/2000/NT/XP</td><td>Windows 95/ 98/ 2000/ NT/ XP</td></tr><tr><td>Website</td><td>http://www.logicaldecisions.com</td><td>http://www.decisionarium.hut.fi</td><td>Email g.colson@ulg.ac.be</td><td>http://www.arlingsoft.com</td><td>http://www.banxia.com/</td></tr></table>

5. In contrast to the traditional DSS model-driven structure, the InteliTeam has both data-driven and model-driven supports for problem solving. After entering data and information into the systems, an intelligent system takes care of the screening, sifting, and filtering of data, information, and knowledge.

6. InteliTeam was developed based on Web technology, and it also supports mobile tools, mobile eservice, and WAP. Greater collaboration functions facilitate more interactive decision processes.

7. With InteliTeam, the decision maker or/and participants can define and enter their preferences as hard data, such as price, miles per gallon, and/ or soft information such attractiveness. In addition, information is also entered into the system with Delphi survey documents.

8. Many existing DSS appear to have been designed for ‘‘average’’ users. However, the technological proficiency levels of all knowledge managers and users continue to increase, and software should answer their needs. We think that InteliTeam is suitable for an advanced information technology user. A user type such as an analyst or an expert analyst, as defined by Belton and Hodgkin [8], was taken into consideration.

9. Many DSS software packages require installation processes before they can be used. For example, if Expert Choice 2000 is used, it has to be installed on both client and participant computers, and an Internet Information Server is necessary for this job. In addition, Java-applet technology is used by Web Hipre software. However, InteliTeam is available from ASP for the delivery of DSS functionality. Therefore, installation is not necessary. ASP hosts the decision support application and provides secure access over the Internet.

10. In terms of software cost, a modeler need not buy program to solve their specific problem if InteliTeam is chosen. Rent per use based on ASP is much more advantageous than buying the software.

## 3. A collaborative system: InteliTeam

The purpose of the collaborative system is to develop a web-based framework for a knowledge management and decision making on a special organizational problem. The framework contains four main components. The first component is a GDM approach whereby many participants’ points of view are taken into account in the modeling of a specific problem. The second component is related to employing many multicriteria decision-making techniques. In the third component, the framework is supported by an intelligent system. Advanced communication is supported by new technologies such as mobile tools, mobile e-service, and WAP in the fourth component.

The main problem areas are related to technological management (choosing an investment, technology selection), strategic management, environmental protection (waste management), and other applications. Online stores can be also considered. Particular problem types are dealt with by comparison, ranking, and/ or the choosing of alternatives.The InteliTeam:

(i) provides decision processing using a multiple perspective approach and expertise knowledge support; and

(ii) improves communication among individuals and groups.

The participant’s viewpoints are taken into account in the modeling of a specific problem in every stage of the decision process. Because the InteliTeam achieves a consensus among different perspectives, it can be effectively used to solve problems that involve multiple criteria, multiple perspectives, multiple stakeholders and multiple issues.

## 3.1. Physical structure of InteliTeam

## 3.1.1. Architecture

The software architecture contains fundament web based programming and object-oriented design paradigms. The entire system is designed in an objectoriented manner, and UML and its constituents can reside all over the Web by using ASP services.

The InteliTeam architecture consists of three classical layers: presentation, domain, and data access. In the first layer, a user interface package provides user interfaces for the decision maker, the participants/experts, and the system administrator. An Internet presentation framework provides access user interfaces.

In the second layer, business rules, computing algorithms, and mechanisms of the classes are established. This layer has four fundamental packages: the Delphi package, the intelligent system package, the methods package, and the system maintenance pack age. The Delphi package creates surveys and questionnaires, gathers responses from participants, and analyzes data and information. The intelligent system package has two functions: the first is related to the screening, sifting, and filtering of data, information, and knowledge; and the second is used for selecting a model that is consistent with the available data. The method package implements a large number of MCDM methods for preference aggregation and decision analysis. The system maintenance package provides continuity of system management functions.

In the last layer, the domain layer accesses the data in the database. The layer includes four main packages. The database management system package is used for data management (storing, updating, restoring and processing). The model base management system package is used for the model management. The knowledge base management package is used for knowledge management (storing, updating, restoring and processing). Furthermore, a framework provides the persistence mapping functions for integrating relational database and object oriented code (Fig. 2).

InteliTeam controls itself by Internet communication between the user and the application, and an additional web server is not required. A framework that exists at the presentation layer processes HTTP and WAP requests and provides the user with the results (Fig. 3). The InteliTeam codes were written with Borland Delphi 5. The program runs on Windows 98/NT/2000/XP. It is supported by Borland Paradox DBMS, and clients require at least Internet Explorer 5.0 or Netscape Navigator 4.5.

## 3.1.2. Deployment of the InteliTeam

There seems to be an increasing trend for using ASP services in web-based implementation. ASP services enable the dissemination of DSS applications at a reasonable cost. They are especially attractive for ready-made DSS applications. Therefore, we developed InteliTeam to be used with ASP. In this model, the server plays a central role. Although information and data are stored in the server, users can reach the server and compile their jobs by using PCs or mobile devices (Fig. 4).

## 3.2. Logical structure

InteliTeam consists of six basic logical components: decision maker, participant, survey, question-

![](/api/attachments/DYF7SDDS/fulltext/images/5000be4cd12f726607f6865dc60ad9dd0cb161f7bb1b289e79907ed35d789c0d.jpg)  
Fig. 2. IteliTeam UML architecture diagram.

![](/api/attachments/DYF7SDDS/fulltext/images/734df8eb4257a9e364bb701630a280f790c233cfd4411409a54205a7712829c4.jpg)  
Fig. 3. Physical structure of InteliTeam.

naire, problem, and model. Decision maker is the manager of the system and has the right to make decisions. It prepares surveys, questionnaires, problems, and questionnaire responses, and evaluates the results of the problem solving phases. Participants’ judgment and preferences are included during several phases of the decision-making process. The participants are generally experts at specific decision-making problem areas. The survey component is used to obtain information and data about the decision-making problem as a first concept. In making a survey, many questionnaires are sent to the participants and used in data collection processes. The outputs of the survey are the alternatives, criteria, and weights that are used to structure the decision problem. The problem represents a decision situation and contains ID, name, and parameters. A problem can be modeled with various methods. The chosen models represent the problem in different forms, depending on the methods used. A Class diagram of the system is given in Fig. 5.

## 3.3. Functional structure

The activities that are supported by InteliTeam in the entire decision modeling life cycle can be classified into four categories: idea generation, problem structuring, modeling, and choice. InteliTeam pro-

![](/api/attachments/DYF7SDDS/fulltext/images/17c316e1d4db237755bbc0e7c3a47bc9de17e6254c557cf414fdc4fbb8165970.jpg)  
Fig. 4. UML deployment of InteliTeam.

![](/api/attachments/DYF7SDDS/fulltext/images/b8215258c5c82fe057e92b5c03365b7150d74e85e033ad864a9f7670447fd5a4.jpg)  
Fig. 5. A Class diagram and partial logical structure of InteliTeam.

vides communication and decision support for idea stimulation, data gathering, issue clarification, prob lem structuring, and problem solving. The Web supplies considerable support for each of functions. InteliTeam is supported by the Web in four ways: in structuring group processes, in supporting communication, in providing enhanced information processing, and in providing modeling capabilities. By using asynchronous collaboration, the InteliTeam provides a framework for representing multiple viewpoints of a problem, aggregating the preferences of multiple decision makers according to various group norms, and organizing the decision process in the Web environment.

InteliTeam provides decision support based on perspective development and perspective synthesis in four stages: idea generation and knowledge elucidation; the structuring of the problem, preference articulation, modeling, and the aggregation of the preferences; and the choice of recommendations. Processing steps are affected and affect themselves (Fig. 6).

![](/api/attachments/DYF7SDDS/fulltext/images/88974410d1d85e70819182dad16bd282169ae9c1fe238752bd022c3e9477b017.jpg)  
Fig. 6. Recursive group decision-aid process.

InteliTeam integrates the structured idea of collaborative work by combining three types of methods with the modeling technologies that are employed in DSS: process-based methods for capturing the decision process in collaborative systems; decision structure-based methods for explicitly describing the questions addressed, the available options, and criteria for evaluating the options; and analysis methods for choosing alternatives to give an explicit decision structure.

## 3.3.1. Data gathering

This process identifies and defines the real problem, and decides what to do about it. How many criteria and alternatives to be considered and used are well conducted and documented? The activities carried out with the multiple perspective approach above are contributed by many participants. The decision process begins, of course, with the recognition of the problem to which it relates. The process consists of developing multiple perspectives and gathering information that provide much greater insights into the nature of the problem and its possible solutions.

With InteliTeam, the data gathering is conducted by the Delphi rounds or the Delphi surveys regardless of organizational, political, and social factors. The

InteliTeam system starts with the generation of ideas about the problem. The electronic version of the Delphi method, an asynchronous implementation of the Delphi technique, is used for this purpose. The essence of the system is fairly straightforward. It is comprised of a series of questionnaires that are sent via the Internet to a preselected group of experts. These questionnaires are designed to elucidate and develop individual responses to the problems introduced and to enable the experts to refine their views as the group’s work proceeds in accordance with the assigned task.

## 3.3.2. Problem structuring

In the problem-structuring phase of the decision support framework, three main steps are followed to define the problem framework, to identify the information requirements, and to identify alternatives, criteria, constraints, and stakeholders. Once an initial problem is defined, a better structure is needed before to the application of formal modeling techniques. There are several issues of concern. The first is the structuring policy, i.e., what key decision is to be made, and in what sequence? There are various alternative policies, depending on the criteria and measures of effectiveness, and each policy will result in a different set of models.

![](/api/attachments/DYF7SDDS/fulltext/images/4aedbdeb1b960c18079e56d86471848309168be2c4b462ee17d68e1f9c5ba3f9.jpg)  
Fig. 7. InteliTeam, first screen.

InteliTeam uses dynamic decision problem structuring for this purpose. The approach advocates a dynamic interaction between criteria and alternatives as a decision maker understands their references and expands the set of alternatives. Previous efforts at decision problem structuring, have addressed the generation of criteria and alternatives, and have presented arguments about their interrelationships in a static way. The dynamic approach recognizes the different starting points that are inherent in value-focused thinking and alternative-focused thinking [12]. More importantly, the approach reflects the interactive nature of criteria and alternatives, and suggests movement from one to any other. The interactive and dynamic approach to problem structuring implies that thinking about alternatives helps to generate criteria and vice versa. That is, these two structuring elements cannot be thought of as being independent of each other. Inteli-

Team shares the characteristics of the problem of GDM under multiple criteria, which are outlined in the following matrix [16,38,54].

$$
A ^ {k} = \left[ a _ {i j} \right] ^ {k} = \left[ \begin{array}{c c c c c} a _ {1 1} & \dots & a _ {i j} & \dots & a _ {1 p} \\ a _ {2 1} & \dots & a _ {2 j} & \dots & a _ {2 p} \\ \cdot & \dots & \cdot & \dots & \cdot \\ \cdot & \dots & \cdot & \dots & \cdot \\ \cdot & \dots & \cdot & \dots & \cdot \\ a _ {m 1} & \dots & a _ {2 j} & \dots & a _ {m p} \end{array} \right]
$$

where M is the number of alternatives $\scriptstyle m = 1 , \ldots . . , M ; N$ is the number of conflicting criteria, $\scriptstyle n = 1 , \ldots , N ; \ a _ { i j } ^ { k }$ is group member k’s value of alternative i evaluated by criterion $j ; ~ K$ is the number of group members $k { = } 1 , . . . , K ; ~ A _ { i } ^ { k } { = } [ a _ { i 1 } . . . a _ { i p } ] ^ { k }$ are the alternatives i that are being evaluated by criteria from 1 to N by group member k; and $A _ { j } ^ { k } { = } [ [ a _ { i 1 } . . . a _ { i p } ] ^ { k } ] ^ { \mathrm { T } }$ is criteria j that is being used by group member k to evaluate all alternatives from 1 to M.

![](/api/attachments/DYF7SDDS/fulltext/images/6f839e91bd456ef8963bd4cbd38ec6742604f05d75eb25158af9bfff05322ba2.jpg)  
Fig. 8. The Delphi survey and questionnaire-forming screen.

## 3.3.3. Method selection

The selection and use of a specific method is, however, inherently subjective and guided by the decision maker’s current understanding of the situation. It is often assumed that preferences remain stable, at least for the duration of the choice process, and that the selection of a support tool is compatible with these preferences. The choice of a method can be made in two ways with InteliTeam: either directly by users or by an expert system. The decision maker determines the problem solving methods according to the data handled. After specifying the method, the decision maker brings in new participants/experts so that it can determine the parameters and other information such as scoring, ranking, and rating.

InteliTeam has two methods. The first method is related to social choice functions such as BORDA, CONDORCET, and NANSON. The second method is related to outranking and preference aggregation techniques such as TOPSIS, SMART, AHP, SPAN, and ELECTRE III, and deals with the problems of sorting, ranking, and selecting the best alternative.

![](/api/attachments/DYF7SDDS/fulltext/images/777800f727742574f2542d547ca69595293750db8a3ff6b25dc3175b388c69d6.jpg)  
Fig. 9. The open-ended questionnaire for identifying strategic perspectives.

Furthermore, InteliTeam ensures a minimum of rank disagreements, absolute deviations, and Euclidean distances between the ranks and the prudent orders.

## 3.3.4. Recommendation

The final step is the recommendation of a solution for a specific problem. In this phase, the best or satisfactory decision is sought and found. After entering all of the data for a system, InteliTeam solves the model and presents the results to a decision maker. This process chooses a possible alternative or a ranking of decision alternatives according to group preferences. InteliTeam has a powerful sensitivity analysis function, so sensitivity analysis can also be performed when necessary.

## 4. An example: integrating multiple perspectives in ERP selection

Many firms around the world have shifted their IT strategies of developing information systems in-house to purchasing application software such as enterprise resource planning (ERP) systems. However, a large number of ERP implementations have failed to meet expectations [4,35,66,70]. Due to the high investment in and high risk of failure of ERP systems, and the magnitude of the problems that are involved in their implementation, misfits have been an important issue. Therefore, the selection of an appropriate system is a key factor in the eventual success of ERP system implementation. Due to the strategic, organizational, technological, and behavioral impacts of ERP, a broad perspective of the ERP system evaluation process is needed. Furthermore, the limitations of available resources and the diversity of alternatives make the selection of an ERP project a time-consuming task. Hence, a multidimensional and a multiple perspective approach to ERP system adoption and evaluation is needed.

Typically, ERP systems are software packages with several modules, such as human resources, sales, finance, and production, and provide cross-organizational integration of data through imbedded business processes [28]. ERP systems require a high level of alignment between business strategies, IT strategies, and organizational processes, which are all worthy of long-term planning.

![](/api/attachments/DYF7SDDS/fulltext/images/034fbfa609abdf0fa78b4040c8ee2141c18a4b17eba279420f1d36319d41ce4f.jpg)  
Fig. 10. Checklist questionnaire for eliciting detailed information.

This section explains an ERP selection on Intel-Team for a hypothetical firm. A software selection team was appointed to execute the ERP selection and evaluation process. Based on the results of the academic literature review and articles drawn from the Web and respected practitioner magazines, the team defined six essential perspectives to be considered for ERP selection:

1. Strategic Perspective.

2. Organizational Perspective.

3. Technical Perspective.

4. Vendor and Product Perspective.

5. Project Perspective.

6. User Perspective (external and internal).

The team developed an information gathering process based on a Delphi survey using InteliTeam. Once a user accesses InteliTeam, they see the screen that is shown in Fig. 7. The user is then asked to provide a previously assigned ID and password.

As part of its data gathering effort, the team developed and implemented a survey. In accessing InteliTeam on the Web, the first step was to create a survey for the generation of ideas and the gathering of information about the decision problem. Using the Delphi method, the ERP experts were surveyed to obtain the information that was necessary for ERP selection. The Delphi survey was undertaken over a 2- month period. The InteliTeam Delphi survey package uses two types of questionnaires: open ended and final score list. The initial questionnaire style is generally open ended, and the knowledge obtained is generally text based.

The survey was designed to determine the main perspectives, identify the software and vendors, and elicit information. The work of implementing the survey included designing and testing the first questionnaire; identifying, selecting, and contacting potential participants; distributing the first questionnaire; collecting and analyzing the responses to the first questionnaire; designing the second questionnaire; distributing the second questionnaire; and collecting and analyzing the responses to the second questionnaire.

![](/api/attachments/DYF7SDDS/fulltext/images/980a3cc16c3bd48ba4d1c25311a6647c3b7774be27d035a1f86f68fa63f15537.jpg)  
Fig. 11. The fundamental points of view on ERP software selection and cognitive map.

The purpose of the first questionnaire was to elicit information about participants’ points of view on the ERP selection process. Four questions were asked: two on evaluation perspectives and two questions on the selected software. These questions were repeated for six main perspectives (Fig. 8). The project evaluation team used questions that called for open-ended responses, as opposed to providing respondents with a selection of chosen answers. This was done to encourage productive thinking on the part of respondents and to ensure that the scope of survey responses was not limited to the team’s knowledge and thinking. Selected parts of the first questionnaire are shown in Fig. 9.

The first questionnaire was pilot tested on five individuals who were identified by team members as having suitable manufacturing experience, vision, and familiarity with the project, as well as the ability to complete and return the pilot questionnaires quickly. The results of the pilot questionnaires were incorporated into the instructions and questions in the first questionnaire.

Potential survey participants were then identified. Members of the team on ERP selection identified both potential participants and individuals who could suggest potential participants. The team believed that the survey should include both industry participants and academic experts in ERP.

The first questionnaire was sent out in batches via e-mail and participants were given approximately 2 weeks to respond. The responses varied in length and detail because of the open-ended nature of the questions. The open-coding technique was used to analyze the responses. With this technique, survey responses are read repeatedly, and codes or categories are inferred. When the coding was completed, the team used the codes or categories to extract a list of evaluation and selection perspectives that represented the ideas of the respondents. This list was then incorporated into the second questionnaire.

The Delphi method is an interactive process; that is, during the process, participants receive feedback on the responses of the group as a whole. In the ERP Delphi survey, the second questionnaire was used to provide participants with feedback on the results of the first questionnaire. As mentioned previously, the second questionnaire was a Final Score List questionnaire, which was used for scoring obtained knowledge. The lists of viewpoints and software that were generated by the first questionnaire were used to construct the first two questions of the second questionnaire, which asked the respondents to indicate the importance of their viewpoints. Additional questions asked the respondents to list detailed factors based on priority. A sample question of the second questionnaire is shown in Fig. 10.

![](/api/attachments/DYF7SDDS/fulltext/images/5a903ce2490c1364b60096a446fc7c121abea5b8ae7b905e28b4eeecf37dc3e7.jpg)  
Fig. 12. Method selection for the synthesizing mechanism.

The second questionnaire was sent via e-mail to the respondents of the first questionnaire. The responses from the second questionnaire were collected to determine the viewpoints and the software that the respondents thought were the most important.

The next stage described the structuring phase, where the most critical success or failure factors, i.e., fundamental points of view of the ERP selection, were identified. InteliTeam used the cognitive mapping technique to help the team to identify and structure their points of view. The team aimed at identifying the causal relationships between certain fundamental points of view in the selection process of ERP systems. This identification, represented by cognitive maps of ERP participants’ perceptions, could lead to improvements in the decision making process. The fundamental points of view affecting ERP software selection and adoption were identified from the responses to the second question of the first questionnaire (Fig. 11). By using a causal grid, i.e., a twodimensional matrix in which the fundamental points of view are listed in rows and columns, the cause and effect relationships between the fundamental points of view could be identified.

Thus, the perspectives, the ERP software packages, the preferences, the weights, and the cause and effect relationships were provided through expert judgment or group participation. After collecting all of the knowledge and information that was needed, the team passed to the problem-structuring phase. The team specified the viewpoints and the software from the results of the previous stages. In other words, criteria and decision alternatives were generated by group processes. After evaluating many ideas, the team selected the five software packages that best fulfilled expectations, and thus identified the viewpoints that were necessary to ascertain the priority software.

![](/api/attachments/DYF7SDDS/fulltext/images/f9a2f8e75f72a5655f8076d9dfc7d706173ec5efb20a31ca6b66a78aa61da16a.jpg)  
Fig. 13. The evaluation table for the TOPSIS method.

Identifying the viewpoints and the software added a new problem to the problem list. The software packages were selected from the survey results using check boxes. In the same manner, the perspectives were automatically entered into the evaluation table. After all of the inputs were entered into the evaluation table, an evaluation method was selected from the list that is shown in Fig. 12. These methods also provided the group preference aggregation function, whereby a synthesizing mechanism was used to derive a tentative collective decision, by absorbing, in some way, the individual opinions.

The team used the TOPSIS method according to the data handled. After specifying the method, the team determined the information, such as scoring and ranking, that was required for the method. At this stage, a Delphi round was again used for scoring the software packages. Fig. 13 shows the ratings. The results that were finally recommended are given in Fig. 14.

In this example, a set of evaluating criteria based on the extensive survey results was identified, then the environment and characteristics of ERP systems were taken into consideration. Once the knowledge and information were collected, an iterative approach of consultation with the consultant, suppliers, users, and managers was conducted to modify the evaluation perspectives. The results of this example provide practical guidelines for the selection of ERP systems.

![](/api/attachments/DYF7SDDS/fulltext/images/d94b3e3e516ddfd9232ff3519cc912b7410d21848ea11b50dba2793635bfd68f.jpg)  
Fig. 14. One of the final reports for the selection of ERP software.

## 5. Conclusions

Technological developments have continuously allowed the development of more effective DSS tools. The developed computer systems have enabled the use of spreadsheets, databases, and flexible modeling tools. Networks and communications have enabled the use of group support systems. Expert systems technology has enabled knowledge-based DSS.

Advances in Web technology have enabled interorganizational DSS, and have given rise to numerous new applications of existing technology and many new decision self-support technologies. Today’s fundamental question is whether GDM processes, various MCDM methods, intelligent system components, and Internet technologies that have support functions can be used as an integrated base within a collaborative framework.

All complex organizational problems involve a group of factors, various scientific/technical disciplines, and a diversity of individuals. In principle, each individual treats a problem differently and thus sees it from a distinct perspective. The objective of this study was to develop a serviceable tool to support collaboration and group processes. The study provided a framework for representing multiple viewpoints of a problem, aggregating the preferences of multiple decision makers according to various group norms, and organizing the decision process on the Web.

InteliTeam supports activities in the entire decision modeling life cycle by producing communication and decision support for knowledge gathering. It is a Web based collaborative system that provides online idea stimulation, issue clarification, problem structuring, and problem solving. The system is based on preference elucidation, aggregation, and decision analysis techniques.

Many DSS software packages have been developed and implemented for decision problems. We believe that the more that technology is developed, the more that existing software will affect the many exciting developments in DSS and knowledge management.

## Acknowledgements

We would like to thank the guest editors and the anonymous reviewers for their constructive comments and feedback on earlier versions of this manuscript.

## References

[1] M. Alavi, P.G.W. Keen, Business teams in an information age, The Information Society 6 (4) (1989) 179 – 195.

[2] R.N. Anthony, Planning and Control Systems: A Framework for Analysis, Harvard University Graduate School of Business Administration, Cambridge, MA, 1965.

[3] P. Antunes, J. Segovia, N. Guimaraes, J. Cardenosa, OR-CHESTRA: Negotiation Subsystem: integrating workflow with group decision techniques, ESPRIT Project No. 8749 (1994).

[4] E. Appleton, How to survive ERP, Datamation 43 (1997) 50 – 53.

[5] R.M. Baecker, Readings in Groupware and Computer-Supported Cooperative Work, Morgan Kaufmann, San Mateo, CA, 1993.

[6] C. Bana e Costa, J.C. Vansnick, Applications of the MAC-BETH approach in the framework of an additive aggregation model, Journal of Multi-Criteria Decision Analysis 6 (2) (1997) 107–114.

[7] V. Belton, M.D. Elder, Focusing discussion using Group VISA for multicriteria decision support, Working Paper Series in the Theory, Method and Practice of Management Science, University of Strathclyde (1998).

[8] V. Belton, J. Hodgkin, Facilitators, decision makers, D.I.Y. users: is intelligent multi-criteria decision support for all feasible or desirable? European Journal of Operational Research 113 (1997) 247–260.

[9] V. Belton, S.P. Vickers, VISA—VIM for MCDA, in: G. Lockett, G. Islei (Eds.), Improving Decision Making in Organisations, Springer, Berlin, 1989, pp. 287 – 304.

[10] R.P. Bostrom, R.T. Watson, S.T. Kinney (Eds.), Computer Augmented Teamwork: A Guided Tour, Van Nostrand-Reinhold, New York, 1992.

[11] J.P. Brans, B. Mareschal, PROMCALC and GAIA: a new decision support system for multicriteria decision aid, Decision Support Systems 12 (1994) 297 – 310.

[12] J. Buchanan, M. Henig, J. Corner, Comment on rethinking value elicitation for personal consequential decisions, by G. Wright and P., Goodwin, Journal of Multi-criteria Decision Analysis 8 (1).

[13] T.X. Bui, M. Jarke, Communications design for Co-oP: a

group decision support system, ACM Transactions on Office Information Systems 4 (2) (1986) 81– 103.

[14] J. Cardenosa, C. Juarez, G. Pastor, An intelligent system for problem analysis in organizations, Expert Systems with Applications 15 (1998) 223– 233.

[15] J. Carlos, L. Lopez, E. Fernandez-Gonzalez, A new method for group decision support based on ELECTRE III methodology, European Journal of Operational Research 148 (1) (2003) 14– 27.

[16] C. Chen, Extensions of the TOPSIS for Group Decision-Making under Fuzzy Environment Fuzzy Sets and Systems 114 (1) (2000) 1 – 9.

[17] L. Chidambaram, Relational development in computer-supported groups, Management Information Systems Quarterly 20 (2) (1996) 143 – 163.

[18] C.W. Churchman, The Design of Inquiring Systems: Basic Concepts of Systems and Organization, Basic Books, New York, NY, 1971.

[19] I. Cil, O. Alpturk, InteliTeam: a group decision support system, Proceeding of the 30th International Conference on Computers and Industrial Engineering, Tinos Island, Greece, June 28 – July 2.

[20] I. Cil, R. Evren, Linking of manufacturing strategy, market requirements and manufacturing attributes in technology choice: an expert system approaches, The Engineering Economist 43 (3) (1998) 183–202.

[21] G. Colson, B. Mareschal, JUDGES: a descriptive group decision support system for the ranking of the items, Decision Support Systems 12 (1994) 391–404.

[22] J.F. Courtney, Decision-making and knowledge management in inquiring organizations: toward a new decision-making paradigm for DSS, Decision Support Systems 31 (2001) 17 – 38.

[23] P. Csaki, T. Rapcsak, P. Turchanyi, M. Vermes, R & D for group decision aid in Hungary by WINGDSS, a Microsoft Windows based group decision support system, Decision Support Systems 14 (1995) 205 – 217.

[24] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker, D. Vogel, Information technology to support electronic meetings, Management Information Sytems Quarterly 12 (4) (1988) 591– 624.

[25] G. DeSanctis, B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (12) (1987) 1589 – 1609.

[26] J.S. Dhaliwal, L.L. Tung, Using group support systems for developing a knowledge-based explanation facility, International Journal of Information Management 20 (2000) 131–149.

[27] C. Eden, Strategy development and implementation: cognitive mapping for group support, in: Strategic Thinking: Leadership and the Management of Change, John Wiley & Sons, Ltd., 1993, chapter 5.

[28] J. Esteves, J. Pastor, An ERP Life-cycle-based Research Agenda, 1. International Workshop on Enterprise Management Resource and Planning Systems (EMRPS) (1999) 359 – 371, Venice, Italy.

[29] S. French, K.N. Papamichail, D.C. Ranyard, J.Q. Smith, Design of a decision support system for use in the event of a

radiation accident, Working Paper, University of Leeds, School of Computer Studies (1996).

[30] S. Galam, C.D. Zucker, From individual choice to group decision-making, Physica. A 287 (2000) 644 – 659.

[31] G.A. Gorry, M.S. Scott Morton, A framework for management information systems, Sloan Management Review 13 (1) (1971) 50– 70.

[32] E. Grigoroudis, Y. Siskos, O. Saurais, TELOS: a customer satisfaction evaluation software, Computers & Operations Research 27 (2000) 799– 817.

[33] S.J. Hammond, L.R. Keeney, H. Raiffa, Smart Choices: a Practical Guide to Making Better Decisions, Harvard Business School Press, Boston, 1999.

[34] R.T. Hightower, L. Sayeed, The impact of computer mediated communication systems on biased group discussion, Computers in Human Behavior 11 (1) (1995) 33– 44.

[35] K.K. Hong, Y.G. Kim, The critical success factors for ERP Implementation: an organizational fit perspective, Information and Management 40 (2002) 25–40.

[36] C.L. Hwang, M.J. Lin, Group Decision Making under Multiple Criteria: Methods and Applications, Springer-Verlag, Berlin, 1987.

[37] M.J. InfoHarvest, Criterium Decision Plus: User’s Guide, InfoHarvest, Seattle, WA, 1996.

[38] P. Iz, R.L. Gardiner, Analysis of multiple criteria decision support systems for cooperative groups, Group Decision and Negotiation 2 (1) (1993) 61 – 79.

[39] M. Jarke, M.T. Jelassi, M.F. Shakun, MEDIATOR: toward a negotiation support system, European Journal of Operational Research 31 (3) (1987) 314– 334.

[40] M. Jelassi, TMCDM: from ‘stand-alone’ methods to integrated and intelligent DSS, in: Y. Sawaragi, K. Inoue, H. Nakayama (Eds.), Toward Interactive and Intelligent Decision Support Systems vol. 2, Springer-Verlag, Heidelberg, Germany, 1987, pp. 90– 99.

[41] R. Johansen, Groupware: Computer Support for Business Teams, The Free Press, New York, 1988.

[42] N.I. Karacapilidis, C.S. Pappis, A framework for group decision support systems: combining AI tools and or techniques, European Journal of Operational Research, 103 (1997) 373 – 388.

[43] N.I. Karacapilidis, C. Pappis, Computer-supported collaborative argumentation and fuzzy similarity measures in multiple criteria decision making, Computers & Operations Research 27 (2000) 653–671.

[44] G.E. Kersten, W. Michalowski, S. Matwin, S. Szpakowicz, Rule-based modelling of negotiation strategies, Theory and Decision 25 (1988) 225– 257.

[45] M. Klein, R.W. Grubbstrom, Using OPTRANS as a KB-DSS development environment for designing DSS for production management, European Journal of Operational Research, Special Issue 109 (2) (1998) 264 – 285.

[46] M. Klein, L.B. Methlie, Knowledge-based DSS, Wiley, New York, 1995.

[47] P. Korhonen, H. Moskowitz, J. Wallenius, Multiple criteria decision support, European Journal of Operational Research 63 (1992) 361– 375.

[48] I. Cil, Internet-based CDSS for modern manufacturing processes selection and justification, Robotics and Computer Integrated Manufacturing 20 (3) (2004) 177 – 190.

[49] T.W. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 (1) (1994) 87 – 119.

[50] N.F. Matsatsinis, A.P. Samaras, MCDA and preference disaggregation in group decision support systems, European Jour nal of Operational Research 130 (2001) 414 – 429.

[51] J.E. McGrath, Groups: Interaction and Performance, Prentice-Hall, Englewood Cliffs, NJ, 1984.

[52] J.E. McGrath, A.B. Hollingshead, Groups Interacting with Technology: Ideas, Evidence, Issues and an Agenda, Sage Publications, London, 1994.

[53] I.I. Mitroff, H.A. Linstone, The Unbounded Mind: Breaking the Chains of Traditional Business Thinking, Oxford Univ. Press, New York, 1993.

[54] O.K. Ngwenyama, N. Bryson, Eliciting and mapping qualitative preferences to numeric rankings in group decision making, European Journal of Operational Research 116 (1999) 487– 497.

[55] J.F. Nunamaker, L. Applegate, B.R. Konsynki, Facilitating group creativity: experience with a group decision support system, Journal of Management Information Systems 3 (4) (1987 Spring) 5 – 19.

[56] D.L. Olson, Decision Aids for Selection Problems, Springer, New York, 1996.

[57] G.P. Pervan, A review of research in group support systems: leaders, approaches and directions, Decision Support Systems 23 (1998) 149– 159.

[58] D.J. Power, Decision Support Systems Glossary. DSS Resources, World Wide Web, http://www.DSSResources.com/ glossary (1999).

[59] B. Roy, The Outranking Approach and the Foundations of ELECTRE methods in Reding in Multiple Criteria Decision Aid, in: C.A. Bana e Costa (Ed.), Springer Verlag, Berlin, 1990, pp. 155 – 183.

[60] A.P. Sage, C.C. White, ARIADNE: a knowledge-based interactive system for planning and decision support, IEEE Transactions on Systems, Man, and Cybernetics 14 (1) (1984) 35– 47.

[61] M.A. Selly, E.H. Forman, Expert Choice. Decision Sup port Software, 4922 Ellsworth Ave. (Pittsburgh, PA, 1986).

[62] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present and future of decision support technology, Decision Support Systems 33 (2002) 111– 126.

[63] H.A. Simon, The New Science of Management Decision, Harper Brothers, New York, 1960.

[64] Y. Siskos, A. Spyridakos, Intelligent multicriteria decision support: overview and perspectives, European Journal of Operational Research 113 (1999) 236– 246.

[65] Y. Siskos, A. Spyridakos, D. Yannacopoulos, Using artificial intelligence and visual techniques into preference disaggregation analysis: the MIIDAS system, European Journal of Operational Research 113 (1999) 281–299.

[66] C.J. Stefanou, A framework for the ex-ante evaluation of ERP

software, European Journal of Information Systems 10 (2001) 204–215.

[67] S.A. Stumpf, R.D. Freedman, D.E. Zand, Judgmental decisions: a study of interactions among group membership, group functioning and the decision situation, Academy of Management Journal 22 (4) (1979) 765 – 781.

[68] J.D. Thompson, A. Tuden, Strategies, structures, and the process of organizational decision, in: J.D. Thompson, et al. (Eds.), Comparative Studies in Administration, Univ. of Pittsburgh Press, Pittsburgh, PA, 1959, pp. 195– 216.

[69] E. Turban, J. Aronson, Decision Support and Intelligent Systems, Fifth ed., Prentice-Hall, Upper Saddle River, New Jersey, 1998.

[70] J. Verville, A. Halingten, A six-stage model of the buying process for ERP software, Industrial Marketing Management 32 (2003) 585–594.

[71] H.W. Volberda, A. Rutges, FARSYS: a knowledge-based system for managing strategic change, Decision Support Systems 26 (1999) 99– 123.

[72] V.H. Vroom, A.G. Jago, The New Leadership, Managing Participation in Organizations, Prentice-Hall, Englewood Cliffs, NJ, 1988.

[73] M.E. Warkentin, L. Sayeed, R. Hightower, Virtual teams versus face-to-face teams: an exploratory study of a webbased conference system, Decision Sciences 28 (4) (1997) 975– 996.

[74] C. Zopounidis, M. Doumpos, PREFDIS: a multicriteria decision support system for sorting decision problems, Computers & Operations Research 27 (2000) 779– 797.

![](/api/attachments/DYF7SDDS/fulltext/images/862b25f1a27505be5b00ff8d35ae04387d7d0ef24e8a14be2d484859fa5260af.jpg)

Ibrahim Cil is an Assistant Professor in the Department of Industrial Engineering at Sakarya University, Turkey. He received his PhD in Industrial Engineering from Istanbul Technical University. His research interests include decision analysis, decision support systems, manufacturing strategies, manufacturing systems design and control, and the application of artificial intelligence to manufacturing. His papers have appeared in several jour-

nals, including Robotics and Computer Integrated Manufacturing, Int. J. Computer Integrated Manufacturing, and the Engineering Economist.

![](/api/attachments/DYF7SDDS/fulltext/images/e33e36630747c2557fe3e43e6d69653ea0bf1148821d9c4dc3939ced91b2212d.jpg)

Oguzhan Alpturk received his BS and MS degrees in Industrial Engineering from Sakarya University. He has since been working for business consulting service firms. His research interests are in the areas of knowledge management systems, object-oriented analysis and design, object-oriented database approaches to decision support systems and customers, and Web-based group decision support systems. He has a particular interest in the

practical application of such systems in the real business world.

![](/api/attachments/DYF7SDDS/fulltext/images/2551ed36bce9ce4961667a101f7497b2434a92e2c28dd62fbe322f2ba0dc1c0b.jpg)

Harun Resit Yazgan graduated from the BSc. Management Engineering program at the Department of Management, Istanbul Technical University, Istanbul in 1986. He completed his PhD at the University of London, UK, in 1994. He is now an Assistant Professor at the Industrial Engineering Department of Sakarya University. He is interested in neural networks, meta heuristic algorithms, optimization and planning, and control systems.
