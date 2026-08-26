---
otero_id: 19244
otero_key: "8ETCJWA3"
title: "Object-oriented task analysis"
authors: "Shouhong Wang"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00036-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# Object-oriented task analysis

Shouhong Wang \*

Faculty of Business, University of New Brunswick, Saint John, New Brunswick, E2L 4L5 Canada

## Abstract

The object-oriented approach has recently received much attention in MIS development. However, as yet little research has been reported on task analysis in the object-oriented paradigm. This paper describes an object-oriented method for task analysis. Three fundamental types of objects (task, user, and interface) engaged in task analysis are described. The association between these objects is then built through identifying the messages between the objects. A practical application of this method shows that it is useful for the analysis and design of a human-computer interface.

Keywords: Task analysis; Human-computer interaction; Object-oriented approach

## 1. Introduction

The human-computer interaction (HCI) is becoming one of the most important issues in information systems development [11]. From the point of view of HCI, conventional systems analysis (SA) methods, such as the data flow diagram method [10,16], emphasize descriptions of functional and data requirements within the context of software engineering [29]. On the other hand, contemporary information systems design must be based on descriptions of human-computer interaction in order to make the systems more usable. The major analytic processes in specifying cognitive aspects of useability and the fit of task requirements to user populations are HCI or task analysis (TA) [22]. Although there are a variety of techniques [39], the theory of TA is still under development [12]. One of the problems in research in both HCI and SA communities is the failure to integrate TA with SA [2,6]. This lack of integration may cause difficulties in applying a uniform technique to analyze the global functional processes and the human-computer interface for specific tasks [21]. In this regard, Sutcliffe [30] has proposed a method of integrating the specification of the human-computer interface with the Jackson system development, and Sutcliffe and McDermott [32] have developed a method that integrated the descriptions of the human-computer interface with data flow diagrams. Their integrated methods covered task and user analyses, as well as functional descriptions. However, since the structured approach itself requires creative activities in systems design, the integration methods based on the structured approach do not warrant a smooth conversion from system analysis through system design to system implementation.

In recent years, the object-oriented approach has received attention from the computer and information systems communities $[3,33]$ . A recent information industry survey indicated that the adoption rate of object-oriented methods is dramatically increasing. Organizations that embraced the approach have experienced significant cost savings in the systems development area [25]. Nevertheless, little research into the integration of the development of the human-computer interface with the object-oriented method can be found.

## 2. Object-oriented systems analysis

The object-oriented approach $[23,26,36]$ has become popular in recent years; however, it is still in a period of development. Using the object-oriented approach, analysts model the system being investigated by identifying a set of objects in conjunction with the attributes and methods (i.e., internal operations and messages) that manipulate the object data or request services from other objects. Objects are grouped into classes, which have common properties. Classes are organized into hierarchies in which the subclasses inherit properties, including data definitions and methods. Interactions between objects are handled by means of message sending.

The dynamic relationships between object classes are built into the descriptions of the classes through the definition of message sending. All of the characteristics of object-oriented methods make the approach more effective than the traditional data flow diagram method in management information systems (MIS) development (see [20,24] for detailed discussion). More importantly, the model represented in the paradigm can be implemented by a computer based information system using object-oriented programming without the requirement of a creative system logical design phase [15].

Although the object-oriented approach has been recognized for many years, the methodology of OOA is far from mature. A serious criticism of current development work is the piecemeal fashion of object-oriented systems development. It is commonly accepted in the object-oriented field that the identification of object classes remains an art, given that it is highly dependent upon the problem domain. In fact, objects of a complex system are not “just there for the picking” [38]. Also, the genuine object-oriented methods often suffer due to difficulties in function refinement in IS analysis [26]. In other words, much functional refinement is needed once object classes are identified. For this reason, the development of a uniform paradigm that would merge functional, dynamic, and object-oriented methodologies as an exploratory analysis tool is crucial for object-oriented methodology [17,31,37].

There are a variety tools and techniques of OOA (see a recent survey in [13]). Coad-Yourdon's method [9] was selected as a base for this study because of its simplicity. A modification was, however, made to it: that cardinalities $(0, 1, N)$ between classes were omitted, because cardinalities are sometimes difficult to determine, and they are not always used in system implementation. The elements in OOA are:

![](/api/attachments/8ETCJWA3/fulltext/images/8b6ad7f4c6d451fdcdc8a35ae21dea497e1a6c94ef41234c06c97bcbc4a5429a.jpg)  
Inheritance  
Fig. 1. The diagram representing object class, inheritance and message sending

1. Attributes: Encapsulated data descriptions of the object class.

2. Operations: Processes that apply to the object class. There are two types of operations: method and message.

2.1. Method: An operation which manipulates the encapsulated data in the object.

2.2. Message: An operation procedure which requests service from other object(s). In the object-oriented paradigm, message sending from one object class to another makes dynamic connections between the object classes.

3. Inheritance: In a hierarchical relationship between object classes, subclasses inherit properties, including data definitions and operations, from their superclasses. Inheritance results in static connections between object classes.

These elements are shown in Fig. 1. They provide a generic instrument for object-oriented modeling. However, the instrument does not offer much help to the systems analyst in identifying object classes. This task is a function of the problem domain but is virtually the central issue in defining an OOA technique for a particular field.

OOA methods have been discussed extensively, however, they have not penetrated the HCI field. On the other hand, HCI methods need a tool that can help in general aspects of systems development, especially when TA is incorporated into SA.

## 3. Task analysis and object-oriented perspective

Superficially there is considerable overlap between TA and ordinary SA, as both attempt to define functions needed by the system. However, the difference between the two is significant. Ordinary SA addresses major functionalities within the entire organization. Two of its key concerns are information resources and products. On the other hand, TA addresses the tasks of individual users and human-computer interaction at their level. Personal information processing through the interface is the major interest of TA.

There are various TA methods, such as Task System Design [5], GOMS [8], and Task Analysis for Knowledge Description [18]. Their approaches are diverse due to their different assumptions. Nevertheless, there are similarities shared by the TA approaches: specification of human knowledge in terms of task structure and users' activities to accomplish the task though the human-computer interface. Accordingly, three types of formal descriptions are fundamental for task analysis: task, user, and interface descriptions.

![](/api/attachments/8ETCJWA3/fulltext/images/8474c90fe70338c3367495cacb39a8bf59170f04b9f8702c3612e74859b2d90a.jpg)  
Fig. 2. Task objects

Before object-oriented models for these are presented, our position of “analyst/designer’s view” must be clarified. In the HCI field, researchers often differentiate “user modeling” from “designer modeling”, however, for the purposes of system analysis and design, the user’s conceptual model of the system has to be acquired and transformed into a designer’s model. This concept is adopted here; i.e., all descriptions for TA in the object-oriented model are based on the analyst/designer’s view.

## 3.1. Task descriptions

A central part of TA is to provide task descriptions for an extant human-computer system. One of the most popular approaches to task descriptions is hierarchical task analysis (HTA), which was proposed originally by Annett and Duncan [1]. It was intended to be a general approach to task descriptions and has been applied to a wide range of solutions [19,27]. Using HTA, a task is formally described as a hierarchical structure, and a task can be represented by a tree of its subtasks. In human-computer interactive systems, a primitive subtask could be a computer subtask or human subtask, as shown in Fig. 2. A computer subtask is a computer procedure. A human subtask could be physical-motor operators, such as keystrokes and drawing, memory activities, such as recall, or a combination. In a highly interactive human-computer environment, it is often too tedious to separate a human subtask completely from computer tasks; e.g., when the user types a character, the computer will accept and record it, and when the user slides a cursor on a scroll bar to search for desired data, the computer must respond to move through and change the window on the file. For our purposes, typing and searching for data are defined as human tasks supported by computer procedures. This is illustrated in Fig. 2.

Research [35] has argued that TA should be based upon principles that have increased the utility of system specifications. Accordingly, if object-oriented system specifications are applied, a task or a subtask is an object, and a task structure is a type of assembly structure according to Coad and Yourdon. In our study, it is assumed that a task object can have more than one assembly structure to meet the requirements for designing a human-computer interface.

Two characteristics of object specifications make the representation of a task unique to others in TA. First, since a task (or subtask) is an object, it possesses its own operations (the set of computer procedures to accomplish it), while a human task object contains a set of human operators and computer support procedures. Second, a task object can send messages to trigger other objects; it can also be triggered by other objects. Consequently, in the object-oriented frame, the structure of a task is dynamic. Such a dynamic structure is different from the traditional static structure. Thus, the dynamic method makes the representation of a task structure more flexible than the traditional static method of designing the human-computer interface.

## 3.2. User descriptions

One of the major activities of TA is to analyze user characteristics in order to provide more information about the users for task design and strategic choice of interface. User description models are generally based on user classification $[7,14]$ . Many classification schemes use dimensions of skill and expertise (e.g., novices, experts, and intermittent users). However, there is little consensus about what characteristics should be described. On the other hand, cognitive models describe the human behavior during information processing. Among the human cognitive models, GOMS is one that is widely used. In this, the user's cognitive structure has four sets of components: goals, operators, methods for achieving the goals, and selection rules for choosing among competing methods for goals. A method is a conditional sequence of goals and operators, with conditional tests of the contents of the user's immediate memory and of the state of the task environment. Thus, method descriptions play a central role in this model; they are the core of user descriptions in TA. Because the term “method” has its own particular meaning in the object-oriented community, and to avoid confusion, “task solver” is used instead of “method” in the GOMS model in our study.

![](/api/attachments/8ETCJWA3/fulltext/images/57660fb018c9b2e5c166dc4e88d85ba9a987cb15e3d976c5f333c3be487cd732.jpg)  
Fig. 3. User objects

A task solver can be represented as an object. A major component of the attributes of a task solver object is a goal stack, which retains the step-by-step behavior of the user in reaching a top level goal. In the operation part, a task solver object is assumed to have a generic processor for goal stack processing.

![](/api/attachments/8ETCJWA3/fulltext/images/b6b180f3176abcb67f1941aa68c7e92b8cd1238223f1ac2a480904e7a83d0dab.jpg)  
Fig. 4. Human-computer interface objects

The operation part of each task solver object also contains a set of processes called “operators” in the GOMS model. From the point of view of OOA, those operational processes are messages to task objects. The operation part of a task solver object usually also contains a set of selection rules that control the user’s decision path, while accomplishing a top level goal. An example of task solver object corresponding to a goal of EXECUTE-UNIT-TASK is shown in Fig. 3(a), and an object-oriented frame for user descriptions in TA is shown in Fig. 3(b).

One user can have more than one task solver. This is because a user may have several goals in using a system or may ascertain several problem solving paths to reach a goal.

## 3.3. Interface descriptions

Interface descriptions specify the dialogue between user and computer. Presentation of information to the user and requests for input from the user are the two aspects of HCI from the computer side. There is a large literature on the elemental description of interface design in the HCI field (e.g., [4,28]). A set of primary interface elements are summarized in the appendix. In a contemporary computer programming language, the programming environment often provides high level interface implementation functions to allow easy development of a variety of interface formats for the user. In the present object-oriented context, interface descriptions for an IS are organized into a structure, as shown in Fig. 4. This structure is a type of classification structure. There are two subclasses of the general interface object of a particular IS, one is requests for input, and the other is information presentation. Each subclass in turn has its subclasses of interface objects; e.g., subclass requests for input from the user WINDOW has subclasses of MENU, SCROLL\_BAR, LIST, etc. An interface object possesses its own values of attributes and its event driven operations; e.g., a menu object may have bar-menu and a click on this menu item might trigger a computer task.

## 4. Synthesis of task, user, and interface descriptions for TA

The first step of a task analysis for a human-computer system generates three independent categories of object-oriented descriptions: task; user; and interface. The second step of a task analysis is to synthesize the three categories of descriptions.

A synthesis process for the three descriptions starts with user descriptions. The processor of the user's goal stack finds a goal. To represent its declaration, the user's task solver is assumed to send a message to an interface object; e.g., if the user clicks a menu item to express a goal, the click is a message to the menu object. There are three possible outcomes in response to an initial message:

1. The triggered interface object evokes another one; e.g., displays a submenu.

2. The interface object triggers (starts) a computer task, which might, in turn, evoke an interface object of information presentation to the user; e.g., printing a document after the user clicks a submenu item PRINT. The executed computer task may also trigger a human task.

3. The interface object triggers a human task. A consequence of this is to evoke an interface object of request for input from the user; e.g., after the user selects the EDIT command from the menu, the interface object EDIT triggers a human task of editing. The human then evokes the task object EDITING, which calls an interface object FORM, which allows the user to type.

In summary, a message from the user to declare a goal will cause the system to wait for the user to respond.

When the processor of the user's stack traces the step-by-step behavior further, it reaches either an operator or selection of rules. An operator performs a human task. A selection of rules will eventually trigger an interface object, which in turn evokes a computer task or human task. When a task is carried out, it will send a message to its parent task to indicate its completion. When a parent task is carried out, it will send a message to the user object, and then the active goal has been completed. A message from the task object will request the processor of the goal stack to delete the active goal. The synthesis process is successfully completed if the top goal of the user is accomplished, otherwise, the three types of objects for the system need to be redefined.

A simple example showing a synthesis process is given in Fig. 5, where the user ABC is to edit a manuscript using WordPerfect $^{™}$ . The task solver

defines the user's goal stack to accomplish three subgoals (WRITE, SPELLING-CHECK, and SAVE-FILE) in order to accomplish the top goal of EDIT-MANUSCRIPT. The task solver also defines the user's actions for accomplishing the goal. In the task descriptions, a task object is defined with three computer subtasks and one human subtask. In the interface descriptions, an interface structure and interface objects are outlined. A synthesis process starts with the user object. Message 1 represents the user's application of the WP command to declare the goal of editing a manuscript. The interface object DOS command then triggers the computer task to load WordPerfect (by sending message 2). The computer task object Load WP executes its operations and loads WordPerfect. It sends two messages, once the computer operations are completed: message 3.1 is sent to the interface object WP Main Menu to load a main menu, while message 3.2 is sent to its parent task object to report its completion. The system is now waiting for the user's action. In response to this, the user task solver sends its second message (message 4) to the human task object Typing. At this point, the user is supposed to type some text, using computer software WP. The synthesis process continues. Note that the numbers attached to messages indicate the step of the process. Thus, the final message (22) is sent from the task object to the user object, indicating that the word processing task is completed and the user's goal has been accomplished.

Several points need to be discussed further. First, this synthesis process serves to apply the object-oriented concept to a task analysis. In principle, the user objects do not need to be modeled in the form of computer software as do other objects. Yet, it is possible to model user objects in computer software objects resulting in simulation. Second, the process of synthesis of the three categories of descriptions actually builds the associations between objects (i.e., the components of the human-computer interactive system) by identifying the messages between them. It is also an elaboration process to check that the descriptions are complete in terms of accomplishing desired tasks. In this sense, a TA is an iteration: describing the three types of objects and then synthesizing them. This TA method is called object-oriented task analysis (OOTA).

![](/api/attachments/8ETCJWA3/fulltext/images/45ba06ddb4147d3a4f9f95b9a9c0d33d3b294fd308733206263799fac9ea0c93.jpg)  
Fig. 5. An example of synthesizing the three types of objects

## 5. A practical project using the OOTA method

In order to investigate the effectiveness of the proposed method, a human-computer interactive IS with a reasonable scale was analyzed and redesigned using the method. It is the Tariff System operating in the Planning Department of a telephone company in

Atlantic Canada. Tariffs are documents that define rules applied to individual categories of the customers of the telephone company. They are extensively used by a large group of people across the entire company for purposes including: planning, sales, customer service, and maintenance. There are hundreds of pages of these documents. A particular tariff document has to pass though several stages in its life cycle, including draft, proposal, and approval, before it actually applies to customers. All information regarding the current stage, the date of changes, relevant government regulations, and the user names is attached to the tariff documents. Traditionally, the tariff system was manual. It involved tons of paper per year. The tariff system was eventually computerized in Visual Basic [34], and installed on the company's LAN. This was a typical human-computer interactive system. Using it, the users were allowed to perform various operations on the tariffs, including editing, referencing, batch processing, updating, and printing. However, due to the poor human-computer interface, the users were not satisfied. Two major problems made the initial system unsuccessful.

![](/api/attachments/8ETCJWA3/fulltext/images/f654aeaa02313f6bc5066f98a8846a4cceb85f04dd2ee6efea87f7e472ff388f.jpg)  
Fig. 6. A procedure of object-oriented task analysis

First, the users had added many operation procedures for their own special purpose or based on their habits. The users often complained about the system. On the other hand, the designers felt that it was difficult to use a single frame of interface to accommodate the various needs of users. Second, the system was difficult to maintain. A change to an interface component often required a series of changes to the programs, but the programmers often failed to trace the effect of all the resultant changes. This was traced to poor documentation of tasks and interfaces.

The tariff system was reviewed and a work team was organized to revise the system. Since Visual Basic uses the object-oriented concept in providing the programmers with interface design facilities, the work team felt that an object-oriented task analysis tool was needed.

The OOTA method was used in analyzing and redesigning the tariff system. The entire analysis and redesign procedure is briefly summarized in Fig. 6. Eight typical users, who had experience with the tariff system and represented the major categories of users in the company, were systematically interviewed. As a result, 8 task solvers were modeled. After several revision iterations, 27 forms (i.e., parent interface objects in the Visual Basic term) were revised. About 250 computer tasks (computer program modules in this case) were revisited or modified accordingly. Using the synthesis process, these objects were successfully associated. Since implementation, the new tariff system has been better serving the users and the system is now well documented.

## 6. Summary

This paper recognizes the problem of a lack of techniques for the integration of human-computer interaction and traditional SA in the object-oriented paradigm. Assuming that the object-oriented systems development approach is superior and because more and more IS have been developed using the object-oriented paradigm, the object-oriented approach should be considered in facilitating analysis and design of the human-computer interfaces.

The proposed method has been applied on a practical project. It was found that there were many advantages. First, it facilitates communication in the course of IS development. It substantially reduces the requirement for artistic skills in human-computer interface design. Second, the technique integrates the three aspects (task, user and interface) of TA into a single object-oriented diagram, while providing measures to describe task and user objects in a static way and describing the dynamic supporting properties of the human-computer interactions by defining interface objects as well as messages between the object classes. Third, and more important, the object-oriented diagram could be specified in great detail. And these detailed analysis diagrams can be used for conversion into object-oriented programs directly. Thus, this would make it possible to integrate TA with software engineering. While the technique makes no claim to theoretical validity, it does offer a pragmatic synthesis of object-oriented approaches.

## Acknowledgements

The author wishes to thank Zhengjun Su for her work on parts of this study in the Tariff System. This research was supported by a grant from SSHRC(410930057) of Canada. The author is indebted to the Chairman of the Editorial Board and an anonymous referee for their valuable comments in revising this paper.

## Appendix A. Elements of the human-computer interface

## 1. Requests for input from the user:

<table><tr><td>Elemental Form:</td><td>Physical Device:</td></tr><tr><td>Command line</td><td>Keyboard</td></tr><tr><td>Menu</td><td>Direction Keys/Mouse</td></tr><tr><td>Form filling</td><td>Keyboard/Mouse</td></tr><tr><td>Icon/Button</td><td>Mouse/Finger</td></tr><tr><td>Tool bar (Menu + Icons)</td><td>Mouse</td></tr><tr><td>Graphics/Image/Picture</td><td>Mouse</td></tr><tr><td>Label</td><td>Keyboard</td></tr><tr><td>List</td><td>Mouse</td></tr><tr><td>Option/Checking</td><td>Mouse</td></tr><tr><td>Scroll bar</td><td>Mouse</td></tr><tr><td>Key/Function keys</td><td>Keyboard</td></tr><tr><td>Direct manipulation</td><td>Keyboard/Mouse/Graphic tablet</td></tr></table>

2. Information presentation from the computer:

Elemental Form: Physical Device:
Windows Screen/Printer
Text Screen/Printer
Graphics Screen/Printer
Color Screen/Printer
Sound Speaker

## References

[1] J. Annett and K.D. Duncan, “Task Analysis and Training Design,” Occupational Psychology, 41, 1967, pp. 211–221.

[2] Anonymous, “Two Communities, Two Languages,” Communications of the ACM, 36(4), 1993, pp. 113.

[3] J. Ang, “A Classification of Advanced Office Systems to Aid in Their Development,” Information & Management, 23(3), 1992, pp. 115–122.

[4] R.M. Baecker and W.A.S. Buxton, Readings in Human-Computer Interaction: A Multidisciplinary Approach, Morgan Kaufmann, San Mateo, CA, 1987, pp. 427–437.

[5] R.W. Bailey, Human Performance Engineering: A Guide to Systems Designers, Prentice Hall, Englewood Cliffs, NJ, 1982.

[6] D. Benyon, “The Role of Task Analysis in Systems Design,” Interacting with Computers, 4(1), 1992, pp. 102–123.

[7] C.M. Brown, Human-Computer Interface Design Guidelines, Ablex Publishing, Norwood, NJ, 1989.

[8] S.K. Card, T.P. Moran, and A. Newell, The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1983.

[9] P. Coad and E. Yourdon, Object-Oriented Analysis, Yourdon Press, Englewood Cliffs, NJ, 1991.

[10] T. DeMarco, Structured Systems Analysis and Design, Yourdon, New York, NY, 1978.

[11] D. Diaper, “The Discipline of HCI,” Interacting with Computers, 1(1), 1989, pp. 3–5.

[12] D. Diaper and M. Addison, “Task Analysis and Systems Analysis for Software Development,” Interacting with Computers, 4(1), 1992, pp. 124–139.

[13] G. Eckert and P. Golder, “Improving Object-Oriented Analysis,” Information and Software Technology, 36(2), 1994, pp. 67–86.

[14] E.A. Edmonds, “Adaptive Man-Computer Interface,” in M.J. Coombs and J.L. Alty (Eds.), Computing Skills and the User Interface, Academic Press, London, UK, 1981.

[15] R.G. Fichman and C.F. Kemerer, “Object-Oriented and Conventional Analysis and Design Methodologies,” IEEE Computers, 25(10), 1992, pp. 22–39.

[16] C. Gane and T. Sarson, Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Englewood Cliffs, NJ, 1979.

[17] B. Henderson-Sellers and L. L. Constantine, “Object-Oriented Development and Functional Decomposition,” Journal of Object-Oriented Programming, 3(1), 1991, pp. 11–16.

[18] P. Johnson, “Towards a Task Model of Messaging: An Example of the Application of TAKD to User Interface Design,” in P. Johnson and S. Cook (Eds.), People and Computers: Designing the Interface, Cambridge University Press, Cambridge, UK, 1985, pp. 46–62.

[19] M. Khalifa and D. Kira, “A Graphical Task Analysis Language (GTAL),” INFOR, 31(2), 1993, pp. 65–79.

[20] T. Korson and J.D. McGregor, “Understanding Object-Oriented: A Unifying Paradigm,” Communications of the ACM, 33(9), 1990, pp. 40–64.

[21] F.Y. Kuo, “A Cognitive Engineering-Based Approach to Designing Hypermedia Applications,” Information & Management, 25(5), 1993, pp. 253–263.

[22] J. Long, “Designing for Usability,” in M.D. Harrison and A.F. Monk (Eds.), People and Computers: Designing for Usability, Cambridge University Press, UK, 1986, pp. 3–23.

[23] J. Martin, Principles of Object-Oriented Analysis and Design, Prentice Hall, Englewood Cliffs, NJ, 1993.

[24] S.C. McIntyre and L.F. Higgins, “Object-Oriented Systems Analysis and Design: Methodology and Application,” Journal of Management Information Systems, 5(1), 1988, pp. 25–35.

[25] D. Pei and C. Cutone, “Object-Oriented Analysis and Design,” Information Systems Management, 12(1), 1995, pp. 54–60.

[26] J. Rumbaugh, M. Blaha, W. Premerlani, F. Eddy, and W. Lorensen, Object-Oriented Modelling and Design, Prentice Hall, Englewood Cliffs, NJ, 1991.

[27] A. Shepherd, “Analysis and Training in Information Technology Tasks,” in D. Diaper (Ed.), Task Analysis for Human-Computer Interaction, Ellis Horwood, Chichester, UK, 1989, pp. 15–54.

[28] B. Shneiderman, Designing the User Interface: Strategies for Effective Human-Computer Interaction, Addison-Wesley, Reading, MA, 1987.

[29] A. Sutcliffe, “Task Analysis, Systems Analysis and Design: Symbiosis or Synthesis?,” Interacting with Computers, 1(1), 1989, pp. 6–12.

[30] A.G. Sutcliffe, “Integrating Specification of Human-Computer Interface with Jackson System Development,” Information and Software Technology, 32(10), 1990, pp. 665–676.

[31] A.G. Sutcliffe, “Object-Oriented Systems Development: Survey of Structured Methods,” Information and Software Technology, 33(6), 1991, pp. 433–442.

[32] A.G. Sutcliffe and M. McDermott, “Integrating Methods of Human-Computer Interface Design with Structured Systems Development,” International Journal of Man-Machine Studies, 34(5), 1991, pp. 631–655.

[33] B. Thuraisingham, “Multilevel Security for Information Retrieval Systems – II,” Information & Management, 28(1), 1995, pp. 49–61.

[34] Visual Basic, Microsoft, Professional version, 1993.

[35] P. Walsh, “Analysis for Task Object Modelling (ATOM): Towards a Method of Integrating Task Analysis with Jackson System Development for User Interface Software Design,” in D. Diaper (Ed.), Task Analysis for Human-Computer

Interaction, Ellis Horwood, Chichester, UK, 1989, pp. 186-209.

[36] S. Wang, “Object-Oriented Systems Analysis: A Tool for MIS,” Data Resource Management, 3(4), 1992, pp. 12–21. Reprinted in Handbook of IS Management, Robert E. Umbaugh (Ed.), Auerbach Publications, Boston, MA, 1994, pp. 111–122.

[37] S. Wang, “Top-Down Methods in Object-Oriented Information Systems Analysis,” in Data Base Management, Section 26-01-23, Auerbach Publications, Warren, Gorham & Lamont, New York, NY, 1994, pp. 1–8.

[38] S. Wang and N. P. Archer, “Identifying Inheritance Structure in Object-Oriented Systems Analysis – A Pattern Matching Approach,” Journal of Object-Oriented Programming, 7(2), 1994, pp. 47–55.

[39] A. Whitefield and B. Hill, “Comparative Analysis of Task Analysis Products,” Interacting with Computers, 6(3), 1994, pp. 289–309.

Shouhong Wang is an associate professor of Management Information Systems at University of New Brunswick, Canada. He received his BEng and MBA from Tsinghua University, China, and his PhD in Information Systems from McMaster University, Canada. His experience includes working as a production senior manager, teaching in MIS and consulting as a chief information systems analyst of The State Economic Commission of China. His research interests include information systems analysis and design, artificial intelligence in management, and the human-computer interface. His papers have been published (or are forthcoming) in Journal of Management Information Systems, Decision Science, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems Management, IEEE Transactions on Patter Analysis and Machine Intelligence, Computers & Operations Research, INFOR, Fuzzy Sets and Systems, Computational Intelligence, Management Science, European Journal of Operational Research, Canadian Journal of Administrative Science, International Journal of Information Management, and others.
