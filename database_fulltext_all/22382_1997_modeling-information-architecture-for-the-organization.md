---
otero_id: 22382
otero_key: "6GCKBQZR"
title: "Modeling information architecture for the organization"
authors: "Shouhong Wang"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00025-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# Modeling information architecture for the organization

Shouhong Wang $^{*}$

Faculty of Business, University of New Brunswick, Saint John, NB E2L 4L5, Canada

Accepted 20 May 1997

## Abstract

The issue of information architecture (IA) for organizations has recently received considerable attention in IS development. However, as yet little research has been reported on modeling IA using a systematic approach. This paper describes an object-oriented method for modeling it. The proposed method extends the traditional concept of IS analysis into the context of contemporary information technology (IT), and is useful for planning IT-enabled business process reengineering for the organization. © 1997 Elsevier Science B.V.

Keywords: Information architecture; Information systems analysis and design; Object-oriented approach

## 1. Introduction

An information architecture (IA) is a high-level map of the information requirements of an organization [3]. IA (or information systems (IS) architecture) is becoming one of the most important issues in IS development [1]. This is due to the extraordinary rate of growth of information technology (IT) and the wave of business process reengineering. In the information era, traditional monolithic computer systems no longer support cross-functional business processes. Organizations are seeking opportunities to exploit new IT, such as office automation, imaging documentation, networks, and client-server technology to redesign business processes. The analysis and design of high-level architecture for the enterprises is important in assessing the business, technology, and information needs of the organization.

The analysis and design of an IA are the tasks of information specialists in the organization [30]. From the point of view of modeling IA, a natural language is universal, in the sense that it can describe anything important. Yet natural languages have potential ambiguities. Especially, in the system implementation stages, natural language descriptions do not provide measures to map the real world to the computer world. Conventional systems analysis methods, such as the data flow diagram method [8, 14], entity-relationship method [6] and the combination of these methods [25], emphasize descriptions of functional and data requirements within the context of monolithic computing systems. On the other hand, contemporary IS analysis must present many global system aspects including special techniques (e.g. imaging and EDI), locations of data and applications (company-wide and locally managed), and adopted system standards and rules. Although there have been many discussions about IA, there is no theory of its modeling. One of the problems of research in IS development is the failure to integrate the modeling of IA with systems analysis. This lack of integration may cause difficulties in applying a uniform technique to analyzing the global IA and the specific applications for a reengineered business process.

In recent years, the object-oriented approach has received attention from the IS communities $[2, 16, 32, 36]$ . A recent information industry survey indicated that the adoption rate of object-oriented methods is increasing dramatically. Organizations that embraced the approach have experienced significant cost savings in the systems development area $[27]$ . Nevertheless, little research into the integration of modeling IA with the object-oriented method can be found. This paper presents a framework for modeling IA for an organization.

Although IS architecture is related to information and business strategy, our research was limited to modeling IS architecture and should not be construed as presenting a strategic planning methodology. While the development of a strategy for organizations which could manifest itself in architectural expression is an important subject, it is outside this study.

## 2. Object-oriented approach in modeling IS

The object-oriented approach [23, 28, 37] has become popular in recent years; however, it is still in a period of development. Using the object-oriented approach, analysts model the system being investigated by identifying a set of objects in conjunction with their attributes (i.e. data) and methods (i.e. internal operations and messages) that manipulate the object data or request services from other objects. The encapsulation of the attributes and exclusive methods form the basis for treating the attributes and methods as a whole. Objects are grouped into classes which have common properties. Classes are organized into hierarchies in which the subclasses inherit properties, including data definitions and methods. Interactions between objects are handled by means of message sending. The dynamic relationships between objects are built into the descriptions of the classes through the definition of message sending. All of these characteristics make the object-oriented approach more effective than the traditional data flow diagram method in IS development (see [19, 26] for a more detailed discussion). More importantly, the model represented in the paradigm can be implemented by a computer-based IS using object-oriented programming without the requirement of a creative system logical design phase [13].

The methodology of object-oriented analysis is far from mature. A serious criticism of current work is the piecemeal fashion of object-oriented systems development. From the point of view of IA, research should investigate an extension of the object-oriented approach into modeling IA at a macro level.

There are a variety of tools and techniques for object-oriented analysis (see a survey in [10]). Coad-Yourdon's method [7] was selected as a base for this study because of its simplicity. Nevertheless, two significant modifications were made to it. First, cardinalities $(0, 1, N)$ between classes were omitted because they do not play an important role in modeling macro IA. The second modification was that data transmitted by messages between object classes were explicitly annotated. The concept of data flows passing in the object-oriented paradigm is quite different from data flows in the structured data flow diagram in that data flows must be associated with the messages between objects. The elements in object-oriented modeling are:

1. Attributes: Encapsulated data descriptions of the object class.

2. Operations: Processes that apply to the object class. There are two types of operations:

2.1. Method: An operation which manipulates the encapsulated data.

2.2. Message: An operation procedure which requests service from other object(s). In the object-oriented paradigm, message sending from one object class to another makes dynamic connections between the object classes.

3. Data flow: A group of data elements that are associated with a message and specify the communication between the objects.

4. Inheritance: In a hierarchical relationship between object classes, subclasses inherit properties, including data definitions and operations, from their superclasses. Inheritance results in static connections between object classes.

![](/api/attachments/6GCKBQZR/fulltext/images/56137d3eed0091d238c5d74fd7bdf70e6740a9ad519920a69dcd71247b67f8de.jpg)  
Fig. 1. The diagram representing object class, inheritance and message sending.

These elements are shown in Fig. 1. They provide a generic instrument for object-oriented modeling. However, the instrument does not offer much help to the systems modeler in identifying object classes. This task is a function of the problem domain but is virtually the central issue in defining an object-oriented technique for a particular field.

Object-oriented methods have been discussed extensively; however, they have not been adopted by the IA field. On the other hand, modeling IA needs a tool that can help in general aspects of systems development for the organization, especially when IA is incorporated into comprehensive IS analysis.

## 3. IA and the object-oriented perspective

The difference between ordinary systems analysis and modeling IA is significant. Ordinary systems analysis addresses major functionalities and data requirements within the organization. Its key concerns are data and processes. On the other hand, IA addresses the structure of the IS at the organizational level for the planning and management of information assets and resources. Architectural properties of the IS are the major focus for modeling IA.

Although the term IA has been used broadly in the IS community, it has no commonly used definition. From the point of view of systems modeling, the core part of Zachman's framework [38] is the description of data, process and network. His framework provides a taxonomy for relating the concepts that describe the real world to the concepts that describe the IS. However, it does not provide an integration of the descriptions. Sowa and Zachman [31] attempted to formalize the framework. They used symbolic logic to describe the concepts of IA. Such logical expressions, however, are too elegant for system planners to understand and too difficult for system developers to apply. Nevertheless, they extended the original framework by adding three descriptions: people, time, and motivation. According to the extended framework, an IA must therefore describe six concepts: what (data), how (process), where (network/location), who (actors/people), when (time), and why (motivation). Recent research indicated that, while the six-concept framework for IA is useful, there is a tremendous need for the integration of these descriptions into a unified paradigm and for the creation of computer-based tools (CASE tools) to support IA modeling [12].

There are also numerous other conceptual frameworks for IA (see a survey in [20] and [9, 18, 24, 29]). However, from the point of view of modeling IA, these structures could be derived from Zachman's framework. According to previous research [33, 34, 35], the object-oriented paradigm provides an effective environment for IS development, and such a uniform paradigm can merge functional (process), dynamic (time), and object (data) methodologies as an exploratory analysis approach for business process modeling. From the viewpoint of object-oriented modeling, descriptions of what (data), how (process), and when (time) in Zachman's framework can be integrated into one fundamental type of description of business processes. Descriptive representation of the motivation (why) of the enterprise characterizes the objectives (or goals) and strategies of the organization relating to its IS. Descriptions of motivation are also fundamental descriptions of an IA. Descriptions of actors (who) in the IS are important to extract the concept of people from the real-world enterprise because of the significance of the organizational structure and the human informational relationships in the enterprise. The organizational design challenge has to deal with the job design, the structure of authority, and responsibility. Hence, descriptions of actors are the third element in descriptions of an IA. The advent of workstation technology, client-server concepts, and distributed systems has shifted the attention of modeling IA from the traditional monolithic computer systems to network issues. Descriptions of network (where) are the fourth fundamental type of descriptions for an IA. Accordingly, four types of formal descriptions are fundamental for IA in the object-oriented paradigm: business process, actor, goal, and client-server descriptions.

Before object-oriented models for these are presented, the position-of ‘analyst/designer’s view’ must be clarified. In modeling IA, researchers often differentiate among ‘planner’s view,’ ‘designer’s view’ and ‘builder’s view;’ however, for the purposes of system analysis and design, the planner’s conceptual model of the system has to be acquired and transformed into a designer’s model. Furthermore, the builder’s perspective has to be materialized in the details of the designer’s model. Here all descriptions for IA in the object-oriented model are based on the analyst/designer’s view.

## 3.1. Business process descriptions

Essential perspectives in business process are readily represented using the object-oriented methodology. These essential perspectives are the same as those in Zachman's framework. Corresponding to Zachman's 'how' are functional perspectives which represent the process elements that are being performed, and the product flows that are relevant to these elements. Behavioral perspectives (when) represent when process elements are performed; and informational perspectives (what) represent the products (information) produced or manipulated by a process.

To integrate these three, a business process can be modeled by using three fundamental types of object classes: physiomorphic, event, and document.

Physiomorphic objects are physically existing entities of the agent (e.g. customer) and resource (e.g. machine). For an organization, one always can identify a hierarchy of physiomorphic object classes that is useful for a top-down system analysis.

Event objects represent events of routine operations, such as order processing, or decision making activities, such as credit approving. In the object-oriented paradigm of business process modeling, event objects explicitly describe the system timing dynamics. A special event object of a system is the calendar (or system clock) which specifies all of the important events of the system.

Document objects are information entities that enter the system (e.g. order applications), or that are produced by the system (e.g. business reports).

This object-oriented modeling method is effective for system analysis in the sense that it offers a structured approach for searching and creating object classes. Using this method, the business process model contains behavioral, functional, and informational perspectives of the system.

To demonstrate the usefulness of the object-oriented method in business process modeling and reengineering, we use an example that is a simplified version of the Ford Accounts Payable System [15]. The original processes are outlined as follows.

1. A copy of a purchase order from the purchasing department is sent to accounts payable.

2. After material control receives the goods, a copy of the receiving document is sent to accounts payable.

3. An invoice from the vendor is sent to accounts payable.

4. Accounts payable matches the purchase order against the receiving document and the invoice.

5. If all of the documents match, the payment is issued.

6. If there is any mismatch, an accounts payable clerk will investigate the discrepancy, and generate error reports.

From the verbal descriptions of the business process, the output document objects, PAYMENT and ERROR\_REPORT are first identified. Tracing backwards from the output document objects, the event objects are then found. They are MATCHING in the accounts payable department, and SHIPPING in the vendor. Tracing back further, the document objects, ORDER, RECEIPT, and INVOICE, are found. Physiomorphic objects such as INVENTORY are also revealed through the identification of information requirements for the events and document objects. Since this example focuses on business process modeling, only major descriptions of attributes, operations, messages, and data flows for the classes are presented. As a result of the application of the object-oriented business process modeling, the accounts payable system is modeled in Fig. 2.

![](/api/attachments/6GCKBQZR/fulltext/images/8604ea34ebdb8fde3da2423ecd022122aa23948e859e68afd2fd61d7e1be9a43.jpg)  
Fig. 2. An example of modeling business processes.

Similarly, a reengineered accounts payable system is modeled in Fig. 3. The difference between the two is significant. In the reengineered system, the central event of MATCHING in the accounts payable department does not apply to the INVOICE issued by vendors. Instead, the accounts payable department creates an ORDER based on requests from the purchasing department. This change eliminates errors in mismatching and make the process more efficient, and a significant amount of manpower is saved.

## 3.2. Goal descriptions

A central part of IA is the provision of goal descriptions for an extant IS. One of the simplest approaches for providing a goal description is the hierarchical model. A goal is formally described as a hierarchical structure and represented by a tree of its subgoals. In enterprise systems, a primitive subgoal could be an IS or business subgoal. An IS subgoal is directly related to its performance in the organization. A business subgoal describes an ordinary objective or critical factor of the business.

Modeling IA should be based upon principles that have increased the utility of system specifications. Therefore, if object-oriented specifications are applied, a goal or a subgoal is an object, and a goal structure is a type of assembly structure. In our study, it is assumed that a goal object can have more than one assembly structure to meet the requirements for modeling an IA. Since a goal (or subgoal) is an object, it possesses its own attributes and operations. Attributes of a goal object are strategies for achieving the goal and the operations of a goal object are evaluations of the performance of business processes and the system related to the goal. Fig. 4 shows a simplistic object model of goals constructed around a video tape store case study that has been used in a number of publications [5]. As shown in Fig. 4, the firm has two major goals to help it maximize profit: HIGH\_TURN\_RATE and HIGH\_FULFILLMENT. For each of these, there are a number of strategies, such as Stock\_high\_demand\_movies, Eliminate\_low\_demand\_movies, and Substitute\_in-stock\_for\_out-of-stock. Each goal has its own ways of evaluation, such as Turn\_rate and Fulfillment\_rate. The relationships between goal objects and other objects in IA are represented by a message linkage initiated by these operations. Individual goals can also have subgoals. For instance, HIGH\_TURN\_RATE has subgoals of ONE\_TURN\_PER\_2DAYS and NO\_MOVIES\_STAY\_7DAYS, and so on.

![](/api/attachments/6GCKBQZR/fulltext/images/b691941553300d4538ed926b8572fcbfa4d64173f37b59e63a88f19e23430d5e.jpg)  
Fig. 3. Reengineered business process for the example in Fig. 2.

## 3.3. Actor descriptions

One of the major functions of modeling IA is to analyze the system actors' characteristics in order to provide more information about the people of the organization for the purposes of strategic planning and human resource management. Actor is the fundamental type of object class describing people who act on the system.

Attributes of actors could be three-dimensional: organizational, technical and cognitive. In the dimension of the organizational infrastructure, authority of control and responsibility in business and/or information processes are the fundamental attributes. In the technical dimension, actors' descriptions are generally based on user classification of skill and expertise in information technology (i.e. novice, expert, and intermittent user) [4]. In the dimension of human cognition, actors' cognitive structure describes the human behavior in solving a problem using IT.

As an object, an actor can have operations that describe its actions on the system. Control, execution, and communication (formal or informal) are a few examples of these operations. Actors play multiple roles: they could be a trigger of events or a controller of business processes. For instance, a CEO member can initiate a group meeting to make a decision. Actors can also be information providers. Interactions between actors as well as between actors and the information system, can be expressed in communication terms, such as formal or informal, using message sending in the object-oriented paradigm.

![](/api/attachments/6GCKBQZR/fulltext/images/0eca41c044444b42b2b6edeaeb63384fc3e8099118c50089d788917d4c48250a.jpg)  
Fig. 4. An example of modeling goals and strategies.

Actor objects are different from physiomorphic objects with respect to people. Actor objects model people from the organizational view, while physiomorphic objects for people place more emphasis on data and information processing. In modeling IA, one must distinguish between these two different types of object classes. For instance, if EMPLOYEE is a physiomorphic object class in a bank IS, information is available about each of the employees for human resource information processing. On the other hand, if CLERK is an actor object class, it describes clerks' roles and responsibilities in the day-to-day operations.

In the information era, the traditional hierarchical organizational structure chart does not reflect the work relationships between people precisely. This is because the nature of the transaction in contemporary organizations is no longer product- or function-oriented. The organizational dynamics community often defines free structures of working relationships between people [21]. The object-oriented paradigm provides a rich semantic environment for describing such free structures.

Fig. 5 shows an example of actor object descriptions. This example is constructed around a case of a small sales company from [17], with hypothetic modifications of the information technology environment. There are five major actor object classes in this system: SALESPEOPLE, SALES\_MANAGER, PURCHASING\_SHIPPING\_MANAGER, ORDER\_PROCESSING\_MANAGER, and SERVICE\_MANAGER. Each actor has its Responsibility, Authority, and other IT-related attributes. The formal relations between actors are implemented through their interaction with business processes. For instance, the sales manager assigns sales tasks to the salespeople. On the other hand, the salespeople ask the order processing manager to order products. This example shows that the traditional organizational tree is insufficient to describe the organizational aspects of information exchange. The interaction between actors and other types of fundamental descriptions using the object-oriented scheme best describe the organizational dynamics.

![](/api/attachments/6GCKBQZR/fulltext/images/e1d52c59bb9f32b0aa56a0cce5842a7b69bd76c11fa4f01ab20c89a881bdfb41.jpg)  
\* Business processes are not modeled in this diagram

Fig. 5. An example of modeling actors.

## 3.4. Client-server descriptions

Client–server computing is becoming one of the most important issues in IS development [22]. Client–server computing refers to the automation of business processes through computing resources that are not confined to a single location [11]. The architecture of IS involving distributed processing is essentially a client–server issue. The model for the network-based IS must describe the relationship between clients and servers.

Client–server descriptions for IA address the allocation of tasks of front-end and back-end computers in the network. Fundamental types of object classes associated with client–server descriptions for an IA are client and server objects, genuine and virtual objects, and user interface objects.

The client is the front-end processor that is operated by the end user and is generally the originator of the computing process. Using the object-oriented methodology, a client can be described by its attributes, including its address, hardware, software, the corresponding servers' location in the network, and its network protocols. Intersystems communication functions, provided by the client-server development software, allow the client to communicate with the server. The server is the back-end processor that provides processing and/or information to the client. Similar to the client, a server can be described by its attributes, including the corresponding clients' location, hardware, software, and communication protocols.

In the broadest sense, client-server applications split a computing process into two parts. Client-server computing makes the entire system transparent for the user who perceives the part performed by the server as though it were performed by the local client platform. A way of specifying the division of computing tasks is to use virtual objects and genuine objects. A virtual object is an imaginary object perceived by the user who operates the client processor. Its corresponding factual object, the genuine object, must exist on the server processor. For instance, in an order entry system, the process of entering an order and checking for stock in inventory is divided between the PC located in the sales office and the midrange host located at the warehouse. The user would perceive the PRODUCT objects as though they reside on the PC, and obtain inventory information to prepare a shipping order for the customer. In fact, the PRODUCT objects, along with the operation programs, are stored on the server platform. In this case, PRODUCT is a virtual object class for the client, but a genuine object class for the server.

Typically, a virtual object and genuine object in a client–server application is a physiomorphic object. Conceptually, however, they could also be an event or document object class. If object-oriented specifications are applied, the virtual objects, the client, the genuine objects and the server can be organized into assembly structures. The relationship between the virtual and genuine objects is represented by messages and associated data flows. Using such specifications of IA, the division of client and server's tasks can be defined clearly, and information about the requirements in client–server computing could be provided for the detailed design and strategic choice of the interface.

An original consideration of client-server computing is that a PC or workstation is much more capable and economical for supporting a graphic user interface than a mainframe terminal. User interface descriptions specify the requirement of communication skills for the users and computer on the client side. The user interface is an indispensable part of the IS in a client-server application, and user interface object classes can be a type of fundamental object in IA modeling.

Consider a university exploring options to update its existing accounting IS. The reengineered registration procedure had exceeded the capabilities of its current accounting system on a large mainframe. The accounting IS was shared by two campuses and a number of departments at the university, each of which required access to information about students' financial status. It was decided that a client–server architecture was required to support the various applications, as well as to provide a central point of control for system data.

In analyzing this client-server application for the Business Office on a remote campus, the following object classes were identified:

Client: DOS/Microsoft Window PCs in the Business Office, attached to a Novell LAN.

Server: Host DB2 database on IBM 3090, located in the computing center 120 km away.

Genuine physiomorphic Student account. Its attributes include Student ID, Student name, Tuition balance, etc., stored on the central DB2. Virtual student account perceived by the local PCs.

Event: Tuition review on the fifth Friday of each new academic term.

Document: Tuition summary report for each category of students.

GUI: Window for input of student categories by the Business Office. Its frame is named Window-A.

The entire modeling of the accounting system is shown in Fig. 6.

Note that in our discussion we use ‘client–server’ as a general concept in modeling contemporary IA. For the simplest case of stand-alone PC or legacy batch processing system, client and server objects virtually degenerate to a single ‘server’ object.

## 4. Synthesis of business processes, goals, actors and client–server descriptions for IA

The first step in modeling an IA generates four independent categories of descriptions: business processes, goals, actors, and client-server computing. The second step is to synthesize these four which can be formalized into a structured procedure:

1. A synthesis process starts with business process descriptions.

2. Document and physiomorphic object classes in the business process take part in genuine and virtual object classes in the client–server descriptions.

3. Event object classes are triggered by actor object classes if they are not triggered automatically by the system calendar. The linkages of business process and actor descriptions are the messages sent by actors to evoke events. Such messages usually go through the user interface.

4. Document objects in business processes respond to the messages initiated by actors to retrieve or enter data through the user interfaces specified in the client–server descriptions.

![](/api/attachments/6GCKBQZR/fulltext/images/a43f967f302513388d1866480ef8f103c5120beca1efee0cb405f123ea1c0837.jpg)  
Fig. 6. An example of modeling client-server computing.

5. The associations between business processes and goals are assembled by messages from the business processes to the corresponding goals. Upon the completion of a business process cycle, the business process sends a message containing the required data to the goal object for evaluation of the business and system performance.

In principle, the synthesis process is successfully completed if the top goal of the organization is accomplished, otherwise, the four types of descriptions for the IA need to be redefined.

A simple example of a synthesis process for IA modeling is given in Fig. 7: an IA model for a small law firm planning its new computing system. The firm currently has 20 lawyers and 4 secretaries; the accounts receivable system is manual, and information about cases is not shared. Two goals are set: charge to the customer promptly and share information about cases. Two major business processes closely related to the IS are accounts receivable and case information on-line access. Actors participating in the system are LAWYER and SECRETARY. The client-server descriptions include objects on Novell LAN as well as GUI objects of the accounting software package ACCPAC and the e-mail system Pegasus. Message 1, which is sent by object class SECRETARY to the CHARGE event, represents the completion of a lawsuit. It triggers an accounts receivable process. Messages 1.1 and 1.2 represent messages sent by CHARGE event to carry out the accounts receivable process. Message 1.1.2.1 symbolizes the interaction between the interface of ACCPAC and actor SECRETARY. Message 2 from LAWYER indicates the case retrieval and search activities; it triggers the retrieval functions of the case files. Similarly, Message 2.1.2.1 symbolizes the interaction between the interface of DOS/Pegasus and actor LAWYER. Finally,

![](/api/attachments/6GCKBQZR/fulltext/images/5daf93377619a190f89902d5de7e5275307aeb2a92c174847f5d932819300d93.jpg)  
Fig. 7. An example of the synthesis process in modeling information architecture.

Messages 1.3, and 2.3, which are sent by business processes accounts receivable and case information respectively, request the recording of the system performance, thereby indicating that the goal has been accomplished.

This synthesis process applies the object-oriented concept to IA modeling. In principle, some objects (e.g. goal and actor objects) do not need to be modeled in the form of computer software as do others. Yet, it is possible to model these objects thus allowing simulation to be included in the IS planning and for end-user job training. Also, the process of synthesis of the four categories of descriptions actually builds the associations between objects (i.e. the components of the IA) by identifying the messages between them. It is also an elaboration process to check the completeness of modeling of the IS architecture. In this sense, the modeling is an iteration: describe the four types of objects and then synthesize them. We term this modeling method as object-oriented IA analysis. Finally, the proposed modeling method employs formal (scholastic) object-oriented modeling symbols. These symbols can be substituted with desirable icons (or clip-art images) for presentational purposes. From our point of view, any informal icons depicted in 'frameworks' in the literature can be described formally by the proposed modeling method.

## 5. Summary

This paper recognizes the problem of a lack of integrated modeling methods for IA. Assuming that the object-oriented systems development approach is superior and because more and more IS have been developed using the object-oriented paradigm, the object-oriented approach should be considered in facilitating modeling IAs.

The proposed object-oriented IA modeling method has many advantages. First, it employs a simple object-oriented modeling tool and facilitates communication in the course of IS development. Second, the technique integrates the four aspects (business process, goal, actor, and client–server) of IA into a single object-oriented diagram. At the same time it provides measures to describe who, what, why and how in a static way and describes the dynamic supporting properties (when and where) of IA by defining event, client and server objects as well as messages between the object classes. Third, the object-oriented diagram could be specified in great detail; these detailed diagrams can be used for system planning, system analysis, and implementation, as well as user training and system evaluation.

## Acknowledgements

This research was supported by a grant from Social Sciences and Humanities Research Council of Canada.

## References

[1] B.R. Allen and A.C. Boynton, “Information architecture: In search of efficient flexibility,” MIS Quarterly, 15(4) (1991), pp. 435–445.

[2] J. Ang, “A classification of advanced office systems to aid in their development,” Information and Management, 23(3) (1992), pp. 115–122.

[3] J.C. Brancheau and J.C. Wetherbe, “Information architectures: Methods and practice,” Information Processing and Management, 22(6) (1986), pp. 453–463.

[4] C.M. Brown, Human-Computer Interface Design Guidelines (Ablex Publishing, Norwood, NJ, 1989).

[5] T.A. Bruce, Designing Quality Data Bases (Dorset House, London, 1991).

[6] P. Chen, “The entity-relationship model – Toward a unified view of data,” ACM Transactions on Database Systems, 1(3) (1976), pp. 9–36.

[7] P. Coad and E. Yourdon, Object-Oriented Analysis (Yourdon Press, Englewood Cliffs, NJ, 1991).

[8] T. DeMarco, Structured Systems Analysis and Design (Yourdon, New York, 1978).

[9] B.A. Devlin and P.T. Murphy, “An architecture for a business and information system,” IBM Systems Journal, 27(1) (1988), pp. 60–80.

[10] G. Eckert and P. Golder, “Improving object-oriented analysis,” Information and Software Technology, 36(2) (1994), pp. 67–86.

[11] B. Elbert and B. Martyna, Client/Server Computing: Architecture, Applications, and Distributed Systems Management (Artech House, Boston, MA, 1994).

[12] R. Evernden, “The information framework,” IBM Systems Journal, 35(1) (1996), pp. 37–68.

[13] R.G. Fichman and C.F. Kemerer, "Object-oriented and conventional analysis and design methodologies," IEEE Computes, 25(10) (1992), pp. 22-39.

[14] C. Gane and T. Sarson, Structured Systems Analysis: Tools and Techniques (Prentice-Hall, Englewood Cliffs, NJ, 1979).

[15] M. Hammer, “Reengineering work: Don’t automate, obliterate,” Harvard Business Review, 68(4) (1990), pp. 104–112.

[16] T.J. Heintz, “An object-oriented approach to planning and managing software development projects,” Information and Management, 20(4) (1991), pp. 281–293.

[17] G.R. Jones, Organizational Theory (Addison-Wesley, Reading, MA, 1995).

[18] B.O. Kim, “Business process reengineering: Building a cross-functional information architecture,” Journal of Systems Management, 45(12) (1994), pp. 30–35.

[19] T. Korson and J.D. McGregor, “Understanding object-oriented: A unifying paradigm,” Communications Of The ACM, 33(9) (1990), pp. 40–64.

[20] C.H. Lesso, “Information systems architecture,” Records Management Quarterly, 23(3) (1989), pp. 24–28.

[21] T.W. Malone, J. Yates and R.I. Benjamin, “Electronic markets and electronic hierarchies,” Communications of the ACM, 30(6) (1987), pp. 484–497.

[22] W. Marion, Client/Server Strategies (McGraw-Hill, New York, 1994).

[23] J. Martin, Principles of Object-Oriented Analysis and Design (Prentice Hall, Englewood Cliffs, NJ, 1993).

[24] P. Marttin, K. Lyytinen, M. Rossi, V. Tahvanainen, K. Smolander and J. Tolvanen, “Modeling requirements for future CASE: Modeling issues and architectural consideration,” Information Resources Management Journal, 8(1) (1995), pp. 15–25.

[25] V.A. Mastro, “Three-dimensional system development enhances productivity,” Data Management, (1986), pp. 26–29.

[26] S.C. McIntyre and L.F. Higgins, “Object-oriented systems analysis and design: Methodology and application,” Journal of Management Information Systems, 5(1) (1988), pp. 25–35.

[27] D. Pei and C. Cutone, “Object-oriented analysis and design,” Information Systems Management, 12(1) (1995), pp. 54–60.

[28] J. Rumbaugh, M. Blaha, W. Premerlani, F. Eddy and W. Lorensen, Object-Oriented Modeling and Design (Prentice Hall, Englewood Cliffs, NJ, 1991).

[29] H. Ryan and J. Santucci, “Building an enterprise information architecture,” Infoworld, 15(12) (1993), pp. 57–60.

[30] E.H. Sibley, “The evolution of approaches to information systems design methodology,” in: Information Systems Design Methodologies: Improving the Practice, T.W. Olle, H.G. Sol and A.A. Berryn-Stuart (Eds.), Elsevier Science, North-Holland, 1986, Chapter 1.

[31] J.F. Sowa and J.A. Zachman, “Extending and formalizing the framework for information systems architecture,” IBM Systems Journal, 31(3) (1992), pp. 590–616.

[32] B. Thuraisingham, “Multilevel security for information retrieval systems – II,” Information and Management, 28(1) (1995), pp. 49–61.

[33] S. Wang, “Top-down methods in object-oriented information systems analysis,” in: Data Base Management, Section 26-01-23, (Auerbach Publications, Warren, Gorham and Lamont, New York, 1994), pp. 1–8.

[34] S. Wang, “Object-oriented modeling of business processes,” Information Systems Management, 11(2) (1994), pp. 36–43.

[35] S. Wang, “An object-oriented approach to work group support systems analysis,” International Journal of Information Management, 15(3) (1995), pp. 199–207.

[36] S. Wang, “Object-oriented task analysis,” Information and Management, 29(6) (1995), pp. 331–341.

[37] S. Wang, “Toward formalized object-oriented management information systems analysis,” Journal of Management Information Systems, 12(4) (1996), pp. 117–141.

[38] J.A. Zachman, “A framework for information systems architecture,” IBM Systems Journal, 26(3) (1987), pp. 276–292.

![](/api/attachments/6GCKBQZR/fulltext/images/1f1c852bb337dff560f7eb7f0bc14a8ccf8a8061744fe69d623e6502334e7043.jpg)

Shouhong Wang is a professor of Management Information Systems at University of New Brunswick, Canada. He received his B.Eng and MBA from Tsinghua University, China, and his Ph.D. in Information Systems from McMaster University, Canada. His experience includes working as a production senior manager, teaching in MIS and consulting as a chief information systems analyst of The State Economic

Commission of China. His research interests include information systems analysis and design, artificial intelligence in management, and the human-computer interface. His papers have been published in Information and Management, Journal of Management Information Systems, Information Systems Management, International Journal of Information Management, Information and Systems Engineering, Decision Sciences, IEEE Transactions on Systems, Man, and Cybernetics, IEEE Transactions on Patter Analysis and Machine Intelligence, Computers and Operations Research, INFOR, Fuzzy Sets and Systems, Computational Intelligence, Management Science, European Journal of Operational Research, Canadian Journal of Administrative Science, Journal of The Operational Research Society, INFORMS Journal on Computing, Computers and Industrial Engineering, Human Systems Management, and others.
