---
otero_id: 18848
otero_key: "WW7V3SGA"
title: "Expert systems for organizational and managerial tasks"
authors: "Franz Lehner"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90052-h"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Briefings

# Expert systems for organizational and managerial tasks

Franz Lehner

University of Linz, A-4040 Linz / Auhof, Austria

This paper provides an overview, based on a literature analysis, of such expert systems that are currently available or being developed. Furthermore, the state of the art, the goals, and the application opportunities for expert systems in organizational and managerial tasks are analyzed and their base in organizational theory is discussed. Due to the multitude and heterogeneity of tasks associated with an organization, we have structured this paper along the application areas documented in the literature: structural organization, process organization, office systems and administration, personnel management and leadership, and project management. Although some cases permit classification in more than one area, for the most part this classification is free of overlapping.

Keywords: Organizational and managerial task, Organizational structures, Process organization, Project management, Office automation, Personnel management, Leadership.

![](/api/attachments/WW7V3SGA/fulltext/images/e1bd87218dbc5c147f0f61e2cee34b8ddb87a17b471c655c803f6fefbd65effb.jpg)

Franz Lehner has been assistant at the Institute for Organizational Research at the University of Linz, Austria, since 1986. Before this he gathered experience in the field of EDP as head of the educational center at a software house and as an independent consultant. He specialises in the management of computer applications, the development of information strategies, and the effects of technological change on organisational structures.

Correspondence to: F. Lehner, Institut für Wirtschaftsinformatik und Organisationsforschung, University of Linz, A-4040 Linz/Auhof, Austria.

The tasks and activities of today's managers are supported in many ways by software and have even been modified or influenced by it. A uniform description of an organizer's responsibilities is neither available nor perhaps even capable of being gathered and recorded. We use the term organizing here in the sense of the creation of a goal-oriented enterprise or group implementing of technical or sociotechnical systems. An important responsibility of a managerial organizer is thus the formation of the organizational structure and of rules for the coordination of the individual organizational units and processes in order to establish a formal framework for the operation of the company toward the fulfillment of its tasks. This can include, e.g., guaranteeing or improving the efficiency or the effectiveness of the organizational units in terms of the goals. The primary responsibilities of a manager are often seen in the realm of administrative tasks, in office automation, and in the development of data processing (DP) systems. The organization of specialized processes (e.g., production, technical development, customer service, distribution) tend to be handled by other persons. Coordination among the managers and other responsible persons as an managerial or organizational task is either nonexistent or unsystematic, or it gradually becomes important with increasing integration as a result of DP [47].

On the basis of analysis of research approaches in the area of tasks and activities of managers, Rockart and DeLong established a need for managerial support in the development of models and improvement of the organizational system, especially planning and control, and of the efficiency of office systems $[37,49]$ . There is no mention of the application of information engineering in general and of software for the organizer specifically.

Meanwhile, in addition to conventional software, a number of expert systems have been developed for the support of organizational activities. Expert systems are generally considered to be application systems that incorporate programming methods from artificial intelligence. However, the definition of expert systems in the literature is neither consistent nor unambiguous. The most important criteria include the separation of knowledge-base and inference components and in the various definitions the presence of an explanatory component. From this perspective, expert systems serve as a new tool for DP task support. This paper does not make any evaluation about the relative value of expert systems technology over implementations with conventional programming techniques $[40,50,32,33,34]$ .

## Structural organization

The literature on and the available tools for the support of organizational tasks often limit themselves to the representation of general principles and the support of the presentation of existing organizational structures or systems $[36]$ . Although a certain amount of work has been done on the representation of organizational knowledge $[8,9,14]$ , it is unclear how the process of structuring and shaping organizational structures can be supported. Although the support of the dynamics of the organizational structuring process is an important goal of expert systems, efforts are still being concentrated on questions of representation of knowledge about organizations (i.e., the rules by which organizations function, including regulations, employment agreements, standing orders, company structure, protocol) as well as the possibilities for accessing this knowledge. The literature makes little mention of the actual structuring process or the evaluation of concrete organizational forms or alternatives $[c.f.18]$ .

Dinkelbach developed a tool in Prolog at the University of Cologne that, in addition to handling the representation of an organizational structure (applications, tasks, responsibilities and interrelationships among these), permits consistency checks, completeness tests, and simple evaluations. The evaluations consist primarily of conclusions concerning centralization and decentralization possibilities. The system is based on two structuring instruments: the Rockart method for centralization/decentralization of decisions and the ORIKOM method (German abbreviation for Organisatorisches Instrument zur Gestaltung von Informations- und Kommunikationssystemen, i.e. organizational instrument for design of information and communication systems), which supports the structuring of a company's information processing. Restrictions of its range of application result primarily from the state of development of the current program version (e.g., lack of consideration of location or specialized areas, no representation of decision authorization or authority relationships, application-specific task specifications only at the lowest hierarchy level) [11].

A GMD (Gesellschaft für Mathematik und Datenverarbeitung) project called “Assistent Computer” is intended to establish an organizational knowledge base containing information about the organization of the GMD. Currently knowledge about the organizational structure and the procedure flows (process structures) of the company is being recorded in an electronic organizational handbook using the example of an acquisition system. This knowledge base is accessed with the planning system VIPS, which also interactively supports the user in the planning of new procedures. The most important frame structures in this system are the hierarchy for the classification of the acquired objects, the structural organization, and the hierarchy for decomposing tasks into subtasks. The rules of the knowledge base have thus far only been described informally. Interactive functions and control mechanisms that support planning of office activities are described procedurally $[39,54]$ . The ORGWIS project (German abbreviation for Organisations Wissensbasis, i.e. organizational knowledge base) is undertaking the further development of the “Assistent Computer”, although the precise goals have not yet been formulated. Among the general goals are to provide organizational knowledge for a broad range of applications and to support the carrying out of large projects.

The ORGEN (ORganization GENerator) and ORSYS (Organizational Structuring System) assist attempting to isolate and classify the parameters of organizational structuring for data processing on the basis of a contingency approach. The dependence of the results of the structuring of attribute values of the parameters is represented as a control system. Sensitivity analyses of organizational structures can be carried out in future extensions for various combinations of attribute values, etc. The first version of the generator (ORSYS I) can structure a data processing department. This structuring process takes place in several partially recursive steps. From an organizational point of view, the determination of the optimal number of subordinates (span of control) and the job descriptions is particularly interesting [23,28]. However, development is not being continued on this expert system.

The systems treated so far were based, at least implicitly, on a situative organizational approach. Unseld implemented an organizational model, MOMo, that builds on a different theoretical foundation, subjective organizational theory, i.e., covering all the assumptions and evaluations that leaders make about organizations $[51]$ . The pilot model that was constructed with KEE and SimKit is based on a case study from the area of organizational psychology. The model encompasses a technical component (a quantitative description of the company) and a psycho-social component (attributes of organization members). The organization members are described by means of quantitative attributes such as age, educational level, and job description, and by means of qualitative attributes, such as interest, loyalty and motivation. The representation of the behavior of organization members is central. This takes place by “prototypical organization pictures”, i.e., predefined action and behavior patterns that consider the individual goals and value systems, as well as the current context of the situation. The expert system processes the information from the organizational model and returns directions for action based on available subjective organizational theories. The directions for action generated by the expert system are entered into the organizational model and measured over a time span to test their value in the context of the model. The effects of decisions that were made are observed and comparisons are made between intended and actual developments in the modelled organization. At this time, the applicability of the analysis is restricted because the studies of subjective organizational theories all emanate from a single person. The system cannot yet make conclusions on real organizational situations.

With the exception of MOMo, the above examples depict only a part of the total organizational structure. Those questions or tasks that are difficult or impossible to support with conventional means usually affect several organizational units or the total organization (e.g., integration, divisionalization, centralization/ decentralization). The profitable use of currently available expert systems remains impossible at the current state of development, even if an overall optimum is replaced by the principle of the “satisfying solution” from the organizational theory principle of March and Simon [38]. The main reason seems to be that knowledge in this area is very complex, incomplete, or not differentiated adequately. Thus on the one hand all the systems exhibit difficulties in knowledge acquisition and the associated learning components, and on the other hand only inadequate solutions seem to emerge from either their deductive approach or from pattern matching.

Generic knowledge bases could achieve particular importance here. These are knowledge bases that build on available basic knowledge (both specialized and general) rather than only on specific knowledge [c.f. 57]. Generic knowledge thus represents a core of knowledge that is needed in general for the solution to a specific category of problems but, because of its generality, must be complemented with problem and situation oriented information.

Another example of applications that use expert systems techniques to support structuring is the Organizational Consultant, for the examination of the purposefulness of organizational structures and for the design of optimal organizations $[2,7]$ . Similar goals were pursued (although without the use of expert systems techniques) by Wedekind in developing an interactive system for the structuring of organizations $[56]$ and by Böhling and Quint in a simulation model for the design of production organizations $[5]$ .

## Process organization, office systems and administration

Dynamic organization, office systems and management are combined because delineating the respective areas is neither possible nor purposeful and because most of the expert systems described here do not even permit an exclusive classification. Instead there are relatively large intersections and multiple classifications that also complicate the evaluation of their applicability. Expert systems that support production processes are explicitly excluded. Traditionally these are tasks that are handled by production specialists rather than by organizers. Examples and details can be found in the literature $[42,1,29]$ .

The VIPS planning support system is based on the GMD electronic organization handbook. This knowledge base is accessed interactively and supports the planning of new procedures. VIPS supports the planner or organizer who first wants to achieve an overview of the organizational system and use this information to modify the system. Within the synthesis phase the user specifies his problem by selecting a planning context. Starting with a skeletal frame, a series of detailed plans are designed that are graphically depicted in a Petri net. If information is already available in the knowledge base on the planned activity, then the system automatically suggests what the user needs to do (e.g. consider legal issues, compute consequential costs, check space requirements) in handling a particular procedure. In a successive simulation phase the generated plan can be analyzed and verified.

The GMD developed an office system simulator in Prolog that represents processing steps as switching steps in a Petri net. This permits, for example, the determination of new processing and throughput times in the event that conditions change $[58, 59]$ . After various further developments, the simulator is now being successfully used in various areas such as planning support, verification of communication protocol, and design and verification of conversation mediators. The simulator can be used as a modelling tool that facilitates the understanding of an unfamiliar system and as support in the development of new systems $[53]$ .

An expert system named SMARTX was developed by Boeing Computer Services Company to support the selection of hardware and software for office applications. This system is based on databases in which products from suitable suppliers are stored along with their attributes (functions, technical restrictions, etc.) [25]. The VIPS planning system mentioned above is also suitable for this sort of application, although the underlying approach is completely different. If we delete this particular application for office automation, then these systems can be classified in a broader context for general support of configuration activities as well as computer center or DP operations. Mertens and his coworkers mention several expert systems that provide support in the configuration or grouping of computer systems, in tuning operating systems, and in the assurance of operational readiness in the computer center. We should also mention a larger group of expert systems that are associated in a broader sense with databases. Such applications cover a spectrum from database design to information retrieval to knowledge-based generation of database queries. An example of this class of applications is the KONDOR system that was designed by the Bense AG and the GfD-Ingenieur- und Beratungsgesellschaft. Through a uniform dialog interface it supports qualified online queries in external databases [42].

Document and form processing provides a central basis for the organization of office and administration systems. The concept of knowledge-based form processing assumes that numerous kinds of administrative work can be handled by means of structured or partially structured forms. Expert systems can support the completion of such tasks with their knowledge about correct form processing. This support combines procedural knowledge about the execution of the steps of various processes and declarative knowledge about the contents of the forms $[61,42]$ . This actually does not involve a contribution to the support of organizational tasks, but suggests solutions for the tasks themselves.

The Office by Example approach by IBM provides the integration of word processing, access to databases, graphical processing, and electronic mail, all with a uniform user interface and based on the Query by Example database language $[64]$ . The ASPERA system was developed for public administration of the Piemont region (Italy) and serves to recognize processes that can be executed in parallel rather than sequentially. The system also provides information about where a particular file is currently located and what additional steps are still required. Its goal is better supervision and the acceleration of administrative processes [42]. Similar goals are reflected in an expert system developed by Florek et al.; its controlling and monitoring instrument for the area of administrative functions provides support for processing involving multiple workstations [15].

The application of expert systems in the office is often headlined with the buzz phrase “Office of the Future”, in which expert systems are supposed to support both administrative and management functions. The goal is the integration of a multitude of instruments in information and communication engineering by means of cooperative interfaces in such a way that the user sees them through a common and uniform user interface $[61,17,63]$ . Monitoring the user dialog makes it possible, for example, to detect misunderstandings on the part of the user, to advise the user of deficiencies without needing to request them, or to make suggestions. Aid, CONSUL and WISDOM are examples of such expert systems $[63]$ .

At this time, expert systems for intelligent word processing, such as EPISTLE or EPIKUR, concentrate on the special case of the administration of correspondence. This includes the evaluation of the contents of incoming mail, in which knowledge about the structure of correspondence is used to extract certain mail content such as the date, the return address, or the subject. In combination with content analysis methods, certain mailings (e.g., unimportant ones) can be filtered out $[42,48,63]$ . The Triumph-Adler AG company and the University of Erlangen-Nürnberg developed a prototype for the sorting of incoming mail according to the responsible employee or the required procedures. Mertens himself notes that practical application of the prototype would require that a significantly higher proportion of incoming mail be in some form that is readable by machine. This requirement could be fulfilled in the foreseeable future, however, since some companies with international activities have decided to handle all internal mail and communication in the area of middle management via electronic mail.

Other suggestions for the use of expert systems deal with the support of the generation and administration of documents: cataloging texts, filling out forms, etc. Expert systems assure uniformity of procedures and guarantee that all the necessary data is collected. An example of such an expert system is KOFIS (Knowledge-Based Office Information System), which supports the storage and retrieval of documents in the office.

## Personnel management and leadership

Expert systems for personnel management and personnel leadership tasks support the selection of applicants, evaluation of employees, personnel scheduling, and planning and decision processes as well as leadership tasks in a narrower sense. One quickly notices that there are few expert systems in this area that support operational tasks, which Mertens and his coworkers explain as being due to the fact that conventional DP systems already provide adequate support.

There is substantial demand for systems that support managers in the evaluation of their subordinates. For example, in some organizations engineers land management positions on the basis of their expert technical knowledge rather than any demonstrated leadership ability. Examples of expert systems that provide support are: Performance Mentor, an expert system that supports managers in the evaluation of performance; the Welder Qualification Test Selection System for the selection of an employment test for a specific task; JOBBES, an expert system for career counseling; and SESP, which supports a manager in the selection of personnel $[19,42]$ . An expert system for personnel scheduling was developed at the Technical University in Berlin especially for personnel agencies. In assigning personnel to jobs, personnel qualifications are optimally matched to the job requirements.

Expert systems are specially useful in planning and decision-making. Such processes often have the following characteristics: physical separation of group members, need for temporal coordination, procedure and flow control in the group process, and communication among the group members. Most traditional planning systems are based on the assumption that a planner can generate a solution to a problem algorithmically on the basis of the problem description. Such autonomous planning systems support, for example, processes like the formulation and evaluation of goals. If we assume that we need to provide consideration for unforeseen situations, interruptions of the planning process, changes in the organization, or divergent goals among the personnel, then there are typical reasons for the application of expert systems.

Initial attempts to establish the connection between existing approaches to decision support systems (DSS) and artificial intelligence technology were made by Elam/Henderson (1983), Ford (1985), Holsapple/Whinston (1985) and Pfeifer/Lüthi (1987). One well-known system is ODYSSEY, which supports the planning of business trips [39]. The TABS appointment planning system is intended to enable the planning and coordination of appointments, even with incompletely or unclearly formulated requirements, and to resolve schedule conflicts. The knowledge base manages data about persons involved, appointment scheduling, appointment calendar administration, and date computation [42].

The MPO (Managing Participation in Organizations) system supports the choice of management behavior on the basis of the normative models of Vroom/Yetton and Vroom/Jago as well as the analysis of management success. The basic management model, which is considered to be a contingency approach, consists of three elements: a taxonomy of the behavioral opportunities for the manager (decision strategies), diagnostic questions with which the manager analyzes the attributes of a given management situation (problem attributes), and normative recommendations (decision rules) that assure the quality and acceptance of the selected decision strategy. In addition to providing support in the decision for a particular management strategy, MPO, although it does not fulfill all the required attributes of today's expert systems, can be used for the training of managers and the analysis of the degree of success of management [55].

## Project management

To a great extent, the work of managers and organizers is distinguished by its effect on projects. The use of a computer can be valuable in reducing the administrative work involved in a project and updating information on the state of the respective projects. This also explains why there have been studies on the use of expert systems for tasks in the field of project management.

Most of the currently known systems, such as

ALERT, PROJECT MANAGEMENT ADVANTAGE, CALLISTO, DEVISER, and NONLIN, originated in the USA [62,46]. Meanwhile, however, systems have been developed and are available in German-speaking countries. The spectrum of applications ranges from the diagnosis of problems in software development projects (PROJCON) to searching a database for reusable project components (PROJECT ADVISOR) to general support in project planning and simulation (CPSS) [42]. Several examples for the support of core tasks in project management are discussed in more detail below, particularly cost assessment, time planning and network analysis.

Cocomo 1 is an expert system that supports the planning and allocation of resources in software design projects [19]. It was developed with Insight 2, a rule-based tool with back chaining, in the USA at NASA for the estimation of software costs on large projects. Cocomo 1 consists of four knowledge bases that were derived from the Cocomo software cost model developed by Boehm at TRW [4]. The system does not claim to outperform human experts. It is simply intended to support the correct use of the Cocomo model and to make it possible for people without experience in cost estimation to make reasonable predictions and schedules with this model. In order to support project planning, the system can be used in the following ways:

\- determination of which of the four knowledge bases is best suited to the current cost analysis problem;

\- reduction of costs for the adaptation of existing code to the current project;

\- preparation of detail planning and a cost estimate for the complete implementation of the new product;

\- preparation for the implementation of individual modules of the entire system.

An expert system for cost estimation of data processing projects was developed by Schering AG in Berlin in cooperation with the Technical University of Berlin $[31,42]$ . The system has since been used in a production setting. The most significant parameters in the estimation of project costs according to this model are the complexity, the application area, and the available infrastructure for the project. The rules for cost estimation are ordered according to the parameters and make up the major part of the knowledge base. The handling of uncertainties is an important problem, because significant cost-determining attributes of a project cannot be specified exactly at the early stage of cost estimation. The expert system shell KEE, with which the system was developed, affords no suitable method for handling uncertainty. For this reason the heuristics of cost estimation were augmented by a dynamically changing database of experience that provides a sufficiently accurate result. This expert system proved to be superior to the Function Point Method [42].

One particular emphasis in the application of expert systems for large projects is network analysis. Examples are NETEX and BEREX. While NETEX supports the choice of a standard network structure for multiproject management in the area of project planning, BEREX helps in adapting the project structure to the goals and restrictions of the specific project $[27]$ . The SCHEDULING ASSISTANT has different goals. It is based on use of a PERT network and the specification of up to eight risk factors and it can be used for the analysis of risks. Production rules draw their heuristic knowledge from the way in which the risk factors can affect the duration of individual project stages or the entire project $[62]$ . Expert systems can be used, for example, for risk analysis. In practice, expert systems are winning acceptance only very slowly.

## Comparison with conventional software for organizational tasks

Expert systems for organizational tasks can be compared to a consultant with whom problems can be discussed. Systems that provide an unambiguous solution for a given problem are the exception. The final decisions are made by humans; the expert systems only make a suggestion, but do not assume responsibility. The kind of tasks supported by expert systems are marked by high complexity, low structuring, and the lack of other suitable methodological support. Expert systems thus attempt to provide solutions to problems that could previously only be handled inadequately, if at all. Conventional software for organizational tasks, on the other hand, supports only an organizer's specific, defined subtasks.

The support of complex informational requirements in a company requires a modelling of the company and its activities. Organizational databases contain data that are relevant to the organizational structure as well as to tasks and activities of the company. The organizational informational system that is built thereon supports database management and queries regarding the objects and relations of the stored data $[39,20,21,22,35]$ . Performance attributes of programs currently on the market include: graphical representation of organigrams, position diagrams, substitute diagrams, hierarchy diagrams, proxies, job descriptions, overview of responsibilities, work instructions, work procedures, and control diagrams. Building on the organizational database in future phases permits the stored data to be analyzed and used to help identify organizational weaknesses. Periodic ideal-real comparison and planning of the structural organization and the procedure and information flows by means of simulations or what-if analyses are planned for inclusion in future projects. Among the goals are the improvement of the coordination in the company, the support of longitudinal and cross-sectional studies of organizational solutions, and the provision of an information system to support organizational work. The particular suitability of object-oriented programming languages, which are also used in the development of expert systems, for the representation of static structures could lead to a rapid decrease in the importance of conventional organizational information systems or the cancellation of further development of such systems.

A large number of (partially) software-supported methods are currently available to support tasks in the realm of analysis and structuring of office systems. There have been some efforts to establish a formal system of representation in terms of Office Specification Languages in order to be able to proceed with computer-aided processing. However, there is no evidence of a consistent or widespread application of computer-aided structuring of office systems. Usually the availability of such methodical support concentrates on activities and communications analysis and the clear representation of processes. A reduction mechanism is present in practically all known approaches. The goal is an optimization of such criteria as throughput time, information flow, data quantities and processing time. Several exemplary tools are now briefly introduced.

The DOMINO procedure system automates procedures in an organization that always take place uniformly according to certain rules. The DOMINO system provides the framework for the solution of a certain problem; this must be complemented to form a plan of action when the user decides on a particular action and executes it. This procedure corresponds to the method of planning on the basis of frameworks presented by Friedland. The company model and the work procedures are represented in the graphical modelling language GRAPES. The organizer receives support in the design of new procedural variants in the form of time evaluations, efficiency analyses, and the possibility to run simulations $[39]$ .

Communications Structure Analysis (or KSA in German) is a computer-aided method for improving the information and communication relationships in a company. The individual modules, which build primarily on an hierarchical decomposition of office activities, work with a database that contains a representation of the organizational structure. KSA attempts to attain powerful office systems by optimizing elementary tasks and restructuring the office activities. Computer support is available for input, accumulation and analysis of data. A simulator provides support for the generation of solutions.

ISS (Information System Study), known in German-speaking countries as KSS (Kommunikationssystem-Studie), is a method developed by IBM; it permits an analysis of the quality and the flow of information within an organization. The computation of a defined degree of satisfaction serves as an indicator of weak points in the information supply. In the realm of a simulation it can be determined how the efficiency of the information supply would change if optimal satisfaction could be assumed in certain areas. For processes that exchange a great deal of data, a reorganization in the formation of subsystems is recommended (data-oriented procedural integration). The combination into organizational units is supported with the help of the computed isolation and interaction factors. Statistics and simulations can be employed instead of the measure of the degree of satisfaction [52].

MOSAIK (Modular Organizational System for the Analysis and Implementation of Communications Technology) is a method for the collection and analysis of communications data in the office. It is also a tool in OECOS (Organisational Engineering for Communications and Organizational Systems) of the Siemens Company and follows a process-oriented approach for communications network analysis on multiple hierarchical levels in the organization being studied. It supports the selection among various different technical solutions.

When these conventional tools for organizational tasks are compared with expert systems, the former are distinguished by their having been tested in practice and by their availability. The required input data generally do not allow much flexibility. This poses possible problems in the flexibility of the methods, in the interpretation of results, and in the availability of tools for the automatic evaluation of data. Most of the expert systems are still being developed or at best in the early stages of testing. A significant advantage of expert systems in the future could be the fact that the diagnosis of organizational structures or procedures will not require extensive data collection efforts, as is the case with conventional tools. Knowledge-based systems will aid in the administration and application of organizational knowledge, that is widely distributed, fragmentary, and recorded in a multitude of different forms. We must also be aware that an extensive restructuring of an entire organization occurs only in the most unusual of cases. The knowledge base of existing expert systems approaches, however, is still much too tuned to individual cases.

The electronic organizational handbook of the GMD establishes a connection between knowledge-based system and the DOMINO procedure system. The expert system developed by Dinkelbach takes a similar approach with the ORIKOM method. This combinational approach seems to be the future way to develop and apply expert systems for managerial and organizational tasks. Its way of working out suggestions for improvement will primarily depend on the extent to which tools for simulation and graphical representation of results become available. At any rate, a really usable expert system for organizational diagnosis is not yet available. Clearly delineated planning tasks, on the other hand, are currently well supported. A detailed discussion of criteria that permit a decision between conventional support and the application of expert systems technology for an individual case can be found in the work of Krcmar [32,33].

## Summary

For almost all of the expert systems that were discussed, practical aspects of their use in organizations was the focus of interest. Only expert systems for establishing organizational structures strived to incorporate theoretical knowledge. An evaluation or comparison of these expert systems in terms of usability, user friendliness, quality of results, etc. is not practical or even possible currently.

It is particularly of note that, despite interesting individual developments in the area of structuring, there does not seem to have been any exchange of experience or synergy effect in this field, and most of the projects are being discontinued. This could be explained by the high complexity of the tasks and by the fact that representatives of classical organizational theory have only been involved to a limited extent in current information system developments. The potential of possible instrumental support has either not yet been recognized or considered unimportant. The theoretical foundation of the above systems is thus understandably unsatisfactory. This paper can perhaps make a contribution in the direction of building bridges among previously isolated approaches and developments.

The situation in other application areas is better. Here we find not only intensive cooperation between science and practice but also significant advances in the solving of problems that had previously been solved only inadequately, if at all. Expert systems in the area of networking offer support for model construction that is generally combined under the structural analysis of networks and for the evaluation of already existing models in the form of networks. Expert systems do not prescribe a procedure as is the case with standardized process diagrams, but can relieve the user by assuming structuring tasks that were previously done by humans.

Due to the high complexity of most problems in the area of office organization and automation, smaller systems with clearly delineated areas of application would seem to have the best chances of success. The development of expert systems for the office also needs to consider that this is not necessarily a translation of organizational knowledge that is hard to acquire, but that human planners tend to work with little efficiency. Knowledge based systems should thus also serve to improve the process by technical means.

A detailed study carried out by Krcmar showed that expert system projects tend to be successful if certain properties are given. The most important of these were the structurability of the problem, a limited and defined range for the problem (but it could nonetheless be complex), and no dominance of heuristic knowledge $[33]$ . These properties are often not given in organizational tasks; i.e., they are often not of a type that is considered solvable with expert systems. Thus a euphoric attitude is inappropriate, as can be seen by the reserved acceptance of this technology despite the surprisingly large number of available expert systems, for the usefulness of expert systems in organizational applications can only be proven in practice and over time.

## References

[1] Albayrak, S. Verteilte wissensbasierte Systeme in der Fertigung, In: Ehrenberg, D., Krallmann, H. and Rieger, B., 1990, pp. 73–94.

[2] Baligh, H.H., Burton, R.M. and Obel, B. Designing Organizational Structures: An Expert System Method, In: AFCET (Ed.), L'Économique et l'Intelligence Artificielle, Proceedings, Conférence Tutoriale, Aix-en-Provence 1986, pp. 177–181.

[3] Beulens, A.J.M. More powerful and user-friendly DSS by incorporating ES-technology, In: Ehrenberg, D., Krallmann, H. Rieger, B., 1990, pp. 95–112.

[4] Boehm, B.W. Software Engineering Economics, Englewood Cliffs, NJ, 1981.

[5] Böhling, II. and Quint, W. Simulation, von Unternehmensstrategien zum Entwurf von Produktionsorganisationen, In: Breitenecker, F., Troch, I. and Kopacek, P., Eds., Simulationstechnik, Braunschweig, 1990, pp. 50–61.

[6] Breitenecker, F., Troch, I. and Kopacek, P., Eds., Simulationstechnik, Braunschweig, 1990.

[7] Burton, R.M. and Obel, B. Evaluating Organizations Using an Expert System, In: Pau, L.F., Motiwalla, J., Pao, Y.N. and Teh, H.H. Eds., Expert Systems in Economics, Banking and Management, Amsterdam, 1989, pp. 319–328.

[8] Croft, W.B. Representing Office Work with Goals and Constraints, In: Proceedings of the IFIP WG 8.4, Workshop on Office Knowledge, Toronto, August 1987.

[9] Croft, W.B. and Lefkowitz, L.S. Task Support in an Office System, ACM Transactions on Office Information Systems, July 1984, pp. 197–212.

[10] Croft, W.B. and Lefkowitz, L.S. A Goal-Based Representation of Office Work, In: Lamerstorf, W., Ed., Office Knowledge: Representation, Management, and Utilization, North-Holland, 1988, pp. 99–124.

[11] Dinkelbach, W. Die Gestaltung der Aufbauorganisation des betrieblichen Informations- und Kommunikationssystems. Entwicklung eines computergestützten Gestaltungsverfahrens, Bergisch Gladbach/Köln, 1989.

[12] Ehrenberg, D., Krallmann, H. and Rieger, B., Eds., Wissensbasierte Systeme in der Betriebswirtschaft: Grundlagen, Entwicklung, Anwendungen, Berlin, 1990.

[13] Elam, J.J. and Henderson, J.C. Knowledge Engineering Concepts for Decision Support System Design and Implementation, Information & Management, 6, 1983, pp. 109–114.

[14] Ellis, C.A. Formal and Informal Models of Office Activity, In: Mason, R.E.A., Ed., Information Processing 83, North-Holland, Amsterdam, 1983, pp. 11–22.

[15] Florek, S. et al. An Approach for Representing Administration Processes: Experience from an Expert System Application, In: Brauer, W. and Wahlster, W., Eds., Wissensbasierte Systeme, Berlin, 1987, pp. 78–88.

[16] Ford, F.N. Decision Support Systems and Expert Systems: A Comparison, Information & Management, 8, 1985, pp. 21–26.

[17] Frank, U. Expertensysteme: neue Automatisierungspotentiale im Büro- und Verwaltungsbereich?, Wiesbaden, 1988.

[18] Frank, U. Zur Implementierung von Wissen über Organisationen, In: Kruse, H.-G. and Frank, U., Eds., Praxis der Expertensysteme, München/Wien, 1990, pp. 183–198.

[19] Harmon, P., Maus, R. and Morrisey, W. Expertensysteme. Werkzeuge und Anwendungen, München, 1989.

[20] Heilmann, H. Entwurfsentscheidungen bei der Gestaltung eines Organisationsinformationssystems, In: Kurbel, K. et al., Eds., Interaktive betriebswirtschaftliche Informations- und Steuerungssysteme, Berlin/New York, 1989, pp. 315–328.

[21] Heilmann, H. and Simon, M. Organisationsanalyse und -planung mit ODB/OIS. Integration mit bestehenden Anwendungssystemen im Unternehmen, In: Paul, M., Ed., Proceedings der 19. GI-Jahrestagung, Computergestützter Arbeitsplatz, Bd. 2, Berlin, 1989, pp. 190–203.

[22] Heilmann, H. et al. Organisationsdatenbank und Organisationsinformationssystem, In: Handbuch der modernen Datenverarbeitung (HMD), Heft 142, 1988, pp. 119–129.

[23] Heinzl, A. A Technique for Structuring Organizational Units Demonstrated on the Information Systems Department, Working Paper, WHU Koblenz, Haus d'Ester, Vallendar, 1989.

[24] Holsapple, C.W. and Whinston, A.B. Management Support through Artificial Intelligence, Human Systems Management, 5, 1985, pp. 163–171.

[25] Hoyer, R. Organisatorische Voraussetzungen der Büroautomation, Berlin, 1988.

[26] Jarke, M. Wissensbasierte Unterstützung verteilter Entscheidungen und Modellierungsprozesse, In: Scheer, A.-W., Ed., Betriebliche Expertensysteme II. Schriften zur

Unternehmensführung, Bd. 40, Wiesbaden, 1989, pp. 29–54.

[27] Klein, J., König, W. and Stiasni, Ch. Wissensbasierte Generierung von Projektplänen bei Dienstleistungsprojekten mit Kleinseriencharakter, In: Ehrenberg, D. et al, 1990, pp. 453–469.

[28] König, W. Informationsmanagement und Management von Informationssystemen, Hochschulnachrichten aus der Wissenschaftlichen Hochschule für Unternehmensführung, Hochschule für Unternehmensführung, Koblenz, 1989, pp. 5–6.

[29] König, W. and Hennicke, L. Das Produktionsplanungs-Expertensystem PROPEX-Entwicklung und Einsatzperspektiven, In: Wildemann, H., Ed., Expertensysteme in der Produktion, Passau, 1987.

[30] Krallmann, H. Expertensysteme in der Bürokommunikation, VDI-Berichte Nr. 663, Bürokommunikation '87 – Wege zum Erfolg in der Praxis, Düsseldorf, 1987, pp. 285–303.

[31] Krallmann, H. and Suhr, R. Einsatz wissensbasierter Systeme im DV-Projektcontrolling, In: State of the Art 3, Expertensysteme: Strategien und Erfahrungen, Oldenbourg Verlag, Juni 1986, pp. 53–60.

[32] Krcmar, H. Einsatzkriterien für erfolgreiche Expertensysteme, Arbeitsbericht Nr. 13, Lehrstuhl für Wirtschaftsinformatik, Universität Hohenheim, Stuttgart, Juli 1990.

[33] Krcmar, H. Die Bewertung von Einsatzkriterien für Expertensysteme, Ein Vergleich erfolgreicher und nicht erfolgreicher Expertensystemprojekte, In. Ehrenberg, D., Krallmann, H. and Rieger, B., 1990, pp. 337–351.

[34] Kurbel, L. Entwicklung und Einsatz von Expertensystemen, Berlin, 1989.

[35] Kurpicz, F.-J. Die Organisationsdatenbank strukturiert Unternehmen, In: Schönecker, H.G. and Nippa, M., Eds., Computerunterstützte Methoden für das Informationsmanagement, Baden-Baden, pp. 1990, pp. 289–308.

[36] Lehner, F. Software für Organisations- und Managementaufgaben, In: Informationstechnologie - Computer, Systeme, Anwendungen (it), 4, 1990, pp. 241–254.

[37] Lullies, V. Neue Bürotechnik und Management, ZfbF, 10, 1989, pp. 855–870.

[38] March, J.G., Simon, H.A. Organizations, New York, 1958.

[39] Martial, F. von and Victor, F. Das elektronische Organisationshandbuch. Anforderungen und Spezifikation, WISDOM Verbundprojekt, GMD Forschungsbericht FB-GMD-87-16, Gesellschaft für Mathematik und Datenverarbeitung, Bonn, 1987.

[40] Mertens, P. Expertisesysteme als Variante der Expertensysteme zur Führungsinformation, ZfbF 41, 10, 1989, pp. 835–845.

[41] Mertens, P. Betriebliche Expertensysteme in der Bundesrepublik, in Österreich und in der Schweiz, In: Ehrenberg, D., Krallmann, H. and Rieger, B., 1990, pp. 17–38.

[42] Mertens, P., Borkowski, V. and Geis, W. Betriebliche Expertensystem-Anwendungen, Eine Materialsammlung, 2nd ed., Berlin/Heidelberg, 1990.

[43] Ness, A.J. and Reim, F. Planungs- und Gestaltungswerkzeuge für verteilte Bürosysteme, Fraunhofer Institut für Arbeitswirtschaft und Organisation (IAO), 1987.

[44] Niemeier, J. Methoden zur Planung und Gestaltung von Bürokommunikationssystemen, In: Handbuch der modernen Datenverarbeitung (HMD), Heft 136, 1987, pp. 19–40.

[45] Pfeifer, R. and Lüthi H.-J. Decision Support Systems and Expert Systems: A Complementary Relationship?, In: Sol, H.G. et al., Eds., Expert Systems and Artificial Intelligence in Decision Support Systems, Reidel, 1987, pp. 41–51.

[46] Rüssel, L. and Herweg, R. Expertensysteme im Projektmanagement, Online, 6, 1988, pp. 54–55.

[47] Scheer, A.-W. EDV-orientierte Betriebswirtschaftslehre, 4th ed., Berlin, 1990.

[48] Schumann, M. Eingangspostbearbeitung in Bürokommunikationssystemen. Expertensystemansatz und Standardisierung, Berlin, 1987.

[49] Strunz, H. Anforderungen des Praktikers an den computergestützten Arbeitsplatz des Organisators-Ergebnisse einer qualitativen Marktuntersuchung, In: Paul, M., Ed., Computergestützter Arbeitsplatz. Proceedings der 19. GI-Jahrestagung, Berlin, 1989, Bd. 2, pp. 158–175.

[50] Thuy, N. and Schnupp, P. Wissensverarbeitung und Expertensysteme, München/Wien, 1989.

[51] Unseld, S.D. Wissensbasierte Simulation einer Organisation, Zürich, 1988.

[52] Vetter, M. Strategie der Anwendungssoftware-Entwicklung, Stuttgart, 1988.

[53] Victor, F. and Woetzel, G. Ein Prolog-Simulator für Prädikat/Transitions-Netze, In: Breitenecker, F., Troch, I. and Kopacek, P., Eds., Simulationstechnik, Braunschweig, 1990, pp. 284–289.

[54] Victor, F., Sommer, E. and Martial, F. von, Das Planungsunterstützungssystem VIPS: Synthese und Analyse von Vorgängen auf der Basis eines elektronischen Organisa-

tionshandbuchs, In: Paul, M., Ed., Computergestützter Arbeitsplatz. Proceedings der 19. GI-Jahrestagung, Berlin, 1989, pp. 464–475.

[55] Vroom, V.H. and Jago, A. The new Leadership. Managing Partizipation in Organizations, Englewood Cliffs, NJ, 1988.

[56] Wedekind, E.E. Informationsmanagement in der Organisationsplanung, Wiesbaden, 1988.

[57] Winand, U. Generische Wissensbasen: Werkzeuge zur Effektivierung und Ökonomisierung der Anwendung Vermittlung betriebswirtschaftlichen Wissens, In: Ehrenberg, D., Krallmann, H. and Rieger, B., 1990, pp. 267–281.

[58] Wisskirchen, P. et al., Eds., Informationstechnik und Bürosysteme, Stuttgart, 1983.

[59] Wisskirchen, P., Niehuis, S. and Victor, F. Ein rechnergestützter Bürosimulator auf der Basis von PrT-Netzen und Prolog, Angewandte Informatik, 5, 1984, pp. 181–188.

[60] Zelewski, S. Expertensysteme-Übersicht über Konzeptionen und betriebswirtschaftliche Anwendungsmöglichkeiten, Arbeitsbericht Nr. 17, Seminar für ABWL, Industriebetriebslehre und Produktionswirtschaft, Univeisität Köln, Köln, 1986.

[61] Zelewski, S. Expertensysteme im 'Büro der Zukunft', Arbeitsbericht Nr. 19, Seminar für ABWL, Industriebetriebslehre und Produktionswirtschaft, Universität Köln, Köln, 1987.

[62] Zelewski, S. Ansätze der Künstlichen-Intelligenz Forschung zur Unterstützung der Netzplantechnik, ZfbF, 12, 1988, pp. 1112–1129.

[63] Zelewski, S. Expertensysteme zur Unterstützung der Büroarbeit, Information Management, 2, 1989, pp. 18–25.

[64] Zloof, M.M. Office by Example, IBM Systems Journal, 21, 3, 1982, pp. 272–304.
