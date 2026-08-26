---
otero_id: 8514
otero_key: "PQ9HVTYF"
title: "Composite event monitoring in XML repositories using generic rule framework for providing reactive e-services"
authors: "S. Swamynathan; A. Kannan; T.V. Geetha"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.10.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Composite event monitoring in XML repositories using generic rule framework for providing reactive e-services

S. Swamynathan <sup>\*</sup>, A. Kannan, T.V. Geetha

School of Computer Science and Engineering College of Engineering, Anna University, Chennai 600025, India

Received 12 September 2003; received in revised form 4 October 2004; accepted 6 October 2004 Available online 5 November 2004

## Abstract

E-services are emerging as a new paradigm to build web applications. Extensible Markup Language (XML) is becoming a dominant standard for exchanging and storing information in XML-enabled repositories. With its increasing use in areas like ecommerce, there is a rapidly growing need for rule-based technology to support reactive functionality on XML repositories. Active (Event-Condition-Action, ECA) rules are used in the form of XML to implement reactive behavior in e-services. In such services, the reactive rules are used to monitor the event(s) of interest of various users and on the occurrence of the same if the conditions were satisfied then appropriate action would be taken. The event of interest of various users may be simple or complex. In e-service scenario, it becomes necessary to facilitate users to monitor complex events, which are associated with various application domains. These complex events include simple, temporal, and composite events. In this paper, a system is proposed that handles such complex events. For this purpose, the system used a specially designed language called Generic Composite Event Rule Markup Language (GCERML). Monitoring of complex events requires a complex logic and hence the system proposed in this paper uses an inference engine called Java Expert System Shell (JESS), to monitor the complex events in an easy and efficient manner.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Active rules; Composite event; Reactive services; JESS; Rule markup language

## 1. Introduction

Internet has brought in much revolution in B2B solutions [2]. With the development of the search engines, the problem of retrieving relevant information was solved to some extent provided it is available at the time of request. However, this implies that the user has to repeatedly poll for the required information, if it is not available at the information provider at the time of request. A solution to this problem is described [3] in which reactive services are provided to clients. In that system, a reactive mechanism is discussed in which requests are received from users and framed as rules. These rules are then sent to the remote servers that are suspected to contain useful and relevant information. If the required information is not available at the time of arrival of rule, then the rules are installed onto the servers. The rules get executed once the requirement is satisfied and then the rules get triggered, sending back notification to the client.

The reactive mechanism is feasible by using active database technology [16,21].wevent-based rule system. In this system on signaling of an event, a condition corresponding to the event is evaluated and based on the result of this evaluation an action is taken. In this work, Event-Condition-Action (ECA) format is used in which the event is monitored and the condition is evaluated once the event is triggered and the action part delivers the data to the user who puts on the request.

Active rules, which are basically ECA rules, can be represented using XML format and a rule markup language can be formulated [1,5,19]. Active rules for XML offer a natural way for the rapid development of innovative e-services [2] because the information associated with the information provider may be available as XML repositories. Reactive rules may be defined on these XML repositories with events and condition being associated with the XML elements.

Event monitoring is an important issue in most of the Decision Support Systems. Decision makers should be promptly informed about the important events that are associated with critical success factors [12]. An event is a happening of interest and it happens instantaneously at specific points in time. The events may be simple or complex. The work described in this paper enriches the event set with complex and temporal events. For the implementation of this event set, a Generic Composite Event Rule Markup Language (GCERML) is designed. GCERML is generic in the sense that it includes all kinds of events, namely simple, Composite and Temporal events. GCERML takes the advantages of XML standard such as ease of understanding, excellent expressiveness and web representation power. The simple events can be monitored using the parsing technique for XML called Document Object Model (DOM). Monitoring of complex events require a complex logic for which DOM is inadequate. Hence, in this paper, a system, which uses an inference engine called Java Expert System Shell (JESS) [6], is proposed to monitor the complex events in an easy and efficient manner.

The rest of the paper is organized as follows. Section 2 summarizes the literature study. Section 3 explains the architecture of the system. The Generic composite Event Rule Markup Language and event classification is described in Section 4. Section 5 explains the Composite Event Monitoring system. The implementation details are explained in Section 6. The conclusion and future enhancements are briefed in Section 7.

## 2. Literature review

The Internet and the World Wide Web (WWW) have changed the landscape of network computing and have become the de facto environment for electronic commerce. Therefore, many B2B and B2C solutions are offered by different enterprises. This revolution has let the researchers to work in different areas relating to Internet. Some of the promising areas include workflow, agent-based systems, mobile commerce, business models for knowledge management, web services and so on. Due to the influence of web-based systems, more intelligent software systems are expected to be available in order to satisfy the needy users. Open service architectures are being proposed for the interchange of models and data. Extensible Markup Language (XML) provides a framework for describing the syntax for creating and exchanging data structures. The explosive growth of XML-based proposals and standards points to its wide usage and in addition reflects the urgent requirements. An XML-based modeling language for the open interchange of decision models within the DSS community has been proposed [9]. XML-based languages allow applications and on-line analytic processing tools to be modeled from multiple sources without having to deal with individual differences between these sources. The need for workflow support in various interorganizational electronic commerce applications was felt and XML-based Extensible Routing Language (XRL) that enables routing of commercial documents over the Internet to create truly intelligent documents was suggested [10]. This routing language was simple, yet powerful enough to support flexible routing of documents in the Internet environment. For the effective implementation of an interorganizational supply chain on the Web, many optimization model agents need to be embedded in

the distributed software agents [15]. A case-based model modification scheme was proposed that can generate the required formulation from semantically specified requirements in the agent communication language using XML [4]. In order to implement a credit scoring decision support system for small business loans, an embedded scoring model in XML format was suggested [20]. A generative grammar formalism called a procedure constraint grammar (PCG) that defines entire families of related trade procedures to handle various situation-specific factors from multiple sources was described [11]. In Lee’s system, the usual grammar formalism was modified to take into account a variety of constraints. The above approaches to solving Internet-based applications point to the emerg ing role of XML-based standards in this area. Reactive Web service is another area which is influenced by XML-based standards. Pushing reactive services to XML repositories using active rules [3] describes the architecture through which rules can be installed on a remote system and the events associated with the XML repositories can be monitored. The Event-Condition Action (ECA) knowledge model adapted from active database methodology can be used to define these active rules in order to build an innovative e-service [2]. This led to the definition of the Active Rule Markup Language (ARML), designed for sharing information among active information management systems [5]. Most of the systems, which handle active rules for monitoring, focus only on simple events such as update, insert and delete. However, the nature of events that needs to be monitored in real time systems demand high complexity in event monitoring. Hence, need for studying and implementing composite events becomes a necessity. The work on composite event specification in active databases [8] formed a good basis on which a study on composite events could be made and the work provides a detailed view on certain possibilities of composite events along with event specification in object oriented databases [7]. However, these concepts are focused on active and object oriented databases and there is a need for viewing these aspects from an eservice perspective. The important contribution of this paper is in addressing the issue of building a specially designed Generic Composite Event Rule Markup Language for monitoring of composite events. ECA rule matching services for simpler development of reactive applications [13] proposes C Language Integrated Production System (CLIPS)-based architecture for manipulating CORBA-based events in a rule triggering system. Their work clearly reveals that an inference engine would be of great use for rule matching. However, in order to cater to applications like e-services, a more generic rule format and a platform independent language based inference engine becomes necessary. The core contribution of the work described in this paper is the design of a generic XMLbased rule format and the use of JESS, a platform independent inference engine to provide complex event monitoring facility.

## 3. Architecture

The architecture of the composite event monitoring system using generic rule framework for providing reactive e-services is shown in Fig. 1.

The architecture of the composite event monitoring system includes a set of XML servers, rule server and a web-based user interface for client’s access. The client submits a request to the rule server. Example requests may be related to purchasing a house at a particular location, buying stocks, matrimonial requests, etc. The rule server accepts the request and formulates a rule based on that request and installs it on the servers where the required data is expected to be available. Once the corresponding event occurs, the server where the event has occurred notifies the client. The rule server acts like an intermediary between the client and the server providing the service. The rule server contains the Document Type Definition (DTD) of all the XML repositories. Apart from this, it also has the GCERML DTD for the ECA rule to be generated. Using the client request and the DTD of the XML servers, the rule server generates a rule using the GCERML DTD. It stores the rule in the rule repository. The rule broker then identifies the list of XML servers that contain relevant information regarding the rule. The rule is then sent to the XML servers using a B2B interface that employs the SOAP Protocol [18] to encapsulate the rule submission message.

Service Suppliers are in the form of XML Servers that contain relevant data in the XML format. It can also contain components with services attached to them. The structure of a single XML server is shown in Fig. 2.

![](/api/attachments/PQ9HVTYF/fulltext/images/2fbf3c3b2d269867ba81df0191ec711ae18a2c5c8ca7a36d9cb144cc715c9d0a.jpg)  
Fig. 1. Architecture of composite event monitoring system.

Each XML server consists of two basic components namely XML repository and rule engine. The XML repository contains the database in XML format. The rule engine stores rules sent by the rule server. Further it also implements an event-monitoring scheme to check if the events specified in the rules occur. Rules are installed onto XML servers and these rules monitor the XML databases for specified events. If any such event occurs then the condition is checked and if it is true then the corresponding action is triggered. The action can modify the database or execute a method or can communicate back to the client. On the client side, there is an application dependant program that communicates with the client to get the client’s request and provide the reply from the server to the client.

![](/api/attachments/PQ9HVTYF/fulltext/images/e38016cca347aaf4efa6a5c9a9bd9eb0ed7f6ebe507c4985f9e1ca7f2670438a.jpg)  
Fig. 2. Single XML Server.

## 4. Generic composite event rule markup language

An XML-based modeling language is very much used in many decision support systems [9,20]. Designing the most generic DTD called Generic Composite Event Rule Markup Language (GCERML) that suits all kinds of business applications is one of the contributions of this paper. Aiming at a GCERML for the rule system involves a wide variety of events, conditions, actions and extra features like priority to rules, security features, etc. Composite event takes care of events that takes place one after another or replicates itself n number of times or occurs prior to another event, etc. Other kind of events includes basic time events (At,

<table><tr><td colspan="2">Composite-event = logical-event</td></tr><tr><td>|</td><td>(Composite-event)</td></tr><tr><td>|</td><td>Composite-event | composite-event</td></tr><tr><td>|</td><td>Composite-event</td></tr><tr><td>|</td><td>Relative (composite-event-list)</td></tr><tr><td>|</td><td>Relative+(composite-event)</td></tr><tr><td>|</td><td>Relative constant-integer-expression (composite - event)</td></tr><tr><td>|</td><td>Prior (composite-event-list)</td></tr><tr><td>|</td><td>Prior constant-integer-expression (composite-event)</td></tr><tr><td>|</td><td>Composite-event; composite-event</td></tr><tr><td>|</td><td>Sequence (composite-event-list)</td></tr><tr><td>|</td><td>Sequence constant-integer-expression (composite-event)</td></tr><tr><td>|</td><td>Choose constant-integer-expression (composite-event)</td></tr><tr><td>|</td><td>Every constant-integer-expression (composite-event)</td></tr><tr><td></td><td>Fig. 3. Composite event grammars.</td></tr></table>

Before, After, etc.), and temporal events (Meets, Overlap, Endsequal, etc.). Taking into considerations all these points, the GCERML has been designed.

## 4.1. Event classification

The events that can be specified by the client come under the following broad categories such as basic events, temporal events and composite events. The basic events consist of simple events, simple time events and component-based events.

The simple event consists of the events like on insertion, on update, on deletion. These kinds of simple events are taken care of in the XML document itself by building a DOM tree. Document Object Model (DOM) and Simple API for XML (SAX) [17] are XML parsers. After constructing the DOM tree, the XML server monitors various nodes of the tree. Simple time events are triggered by time changes.

In a distributed environment, the presence of components, which contains business logic, can lead to a more flexible environment [14]. It allows remote clients to execute the business logic present in the server. For example, consider an online cab agency containing a database of currently available cars. Since the consumer is a remote client, a method to hire a car may be used. As arguments, the client may provide some details about the required car. This logic may involve some database operations. Hence, normal manipulation of the database and manipulation using components needs to be monitored.

The temporal events consist of the meets, overlaps, during, startsequal, endsequal and equal operations. In temporal events, the temporal operations enclose composite events. The start time of a composite event is the time the first basic event of the composite event occurs. The end time of a composite event is the last basic event of the composite event that occurs.

Logical events can be combined to create composite events using logical operators and special event specification operators. A logical event is nothing but basic events along with a masking condition. Fig. 3 specifies the grammar for handling composite events.

Composite events define many new types of events like Relative, Prior, Choose, Every and so on. Prior (E, F) holds if E occurs before F (that is, if the last logical event of E occurs before the last logical event of F). The order in which the other events occur is immaterial. On the other hand, Relative (E, F) requires that the last logical event of E occur prior to the first logical event of F. Thus the event Prior (E, F) occurs at F2 when the event history is F1 E1 E2 F2 but the event Relative (E, F) does not occur. The composite event Sequence (E1,. . .En) specifies that the component event Ek occurs immediately after the component event Ek-1 event (2VkVn). Operator Choose is used for specifying which occurrence of an event is to be selected. The Every operator is used for specifying events that occur periodically.

## 5. Composite event monitoring

There are two methods of implementation to monitor for the occurrence of composite events in the XML servers. They are finite automata method and event correlation and aggregation using inference engine. Since composite events can be expressed as regular expressions, their occurrence can be detected using finite automata [7]. An automaton can be defined for each event, which reaches an accepting state exactly whenever the event occurs. The input to the automaton is the sequence of logical events constituting the event history for the object with which the automaton is associated. In a program, this concept of finite automata using a linked list and state variable can be implemented. The Finite Automata method to handle composite events has several disadvantages. Since each composite event forms a separate finite automaton, the number of finite automata to manipulate becomes high if the number of composite events increases. As a result, the performance of the entire system decreases. For an e-service application, the finite automaton method is not suitable. A fast method to detect composite event occurrences and perform the action associated with it is needed. As a result, an inference engine is used to solve the problem.

The XML server receives ECA rule subscriptions from rule server, maps them to JESS rules, and delegates the rule-based event correlation process to an embedded inference engine. Composite events occurring at the XML server are mapped into JESS facts. The service provider’s main capabilities are to enable composite event matching and event aggregation and to trigger a set of predefined and arbitrary actions as a consequence of a matched situation. This service highly simplifies the development of reactive applications by alleviating the programmer from the implementation of complex composite event handling mechanisms. The event matching operation done at the XML server is shown in Fig. 4.

The condition part of the GCERML is an XQuery [23] statement. Each XQuery query is expressed in the For–Let–Where–Return (FLWR) representation. XQuery uses XPath [22] statements in its FOR and WHERE clause. The action part of the generic rule “On Event Every (Insert on house and before 20/02/04) Condition location=Adyar Notify Broker"

![](/api/attachments/PQ9HVTYF/fulltext/images/0624a1148992c3d56f3112df39a0112472e67656b3f28317dfd699e36bcf513d.jpg)  
Fig. 4. Triggering of composite events using Java Expert System Shell.

denotes the client’s requested action. This can be of two types namely notification action and data modification action. For example, if a client requests a house in Area X with more than three rooms then the client is notified when the house in Area X with more than three rooms is inserted in the database.

Certain privileged clients can give requests such that when the event occurs and the condition is satisfied, action performing data modification in the XML documents can be issued. All clients cannot be given this power of modification of the database in order to prevent misuse. As a result, an authorization code attribute is present in the Generic Rule DTD. This is used to identify privileged clients. The action part of the Generic Rule is encapsulated using the Simple Object Access Protocol (SOAP).

![](/api/attachments/PQ9HVTYF/fulltext/images/d986909f83a999d3750c02e95e5beb4018cd55d9facaf6c80b2cd5c75cd00131.jpg)  
Fig. 7. XML rule to JESS rule.

The following example clearly illustrates the client’s request, the generated rule in the rule server and its corresponding JESS format. Fig. 5 illustrates client’s request.

At the Rule Broker, the client request shown in Fig. 5 is transformed into XML format as in Fig. 6.

At the XML server, the ECA rule given in XML format is mapped to JESS rule, as shown in Fig. 7, which is build upon predefined user constructs. The events that occur are also converted to JESS facts. The JESS inference engine constantly monitors the JESS rule and on the occurrence of a new fact, executes the

![](/api/attachments/PQ9HVTYF/fulltext/images/03eadc41d44928c783e3c82946b6de043aa9cfb631c121c3c03c05a2e30bab74.jpg)  
Fig. 6. An example: rule server generated XML format rule.

![](/api/attachments/PQ9HVTYF/fulltext/images/bf6f03a7f56bd845ded92ff0ea13e63240273ef2b68f340f301feb925988a6b9.jpg)  
Fig. 8. XML format of the rule.

JESS rule producing new JESS facts as the result. These JESS facts must later be converted into suitable action as requested by the client.

## 6. Implementation details

The sample domain considered for this implementation is book agency. This implementation consists of modules such as user interface, rule server implementation and XML server implementation. For the client’s user interface, an HTML page with an applet, which incorporates a tree structure for efficient and easy event entry, is used. This is hosted at the Rule Server. The root element of the tree structure is event. The user can then build any kind of composite event using this tree. A document object is defined, which stores the tree the user enters in DOM format. A function iterates through the tree created by the user and constructs the event in the DOM format in the document variable. For each leaf in the tree, a text node is created with that particular string name. If it is not a leaf node, a new element is created with that particular name and recursively calls the function on that particular element. This function finally returns the event in DOM format, which adds other details such as IP address of the rule server and client’s rule id. This document object is then sent through SOAP to the XML server.

The XML Server consists of two main portions namely, the XML repository and the rule execution engine, which monitors the rules to check if any rule is to be triggered. For this purpose, JESS is employed that forms, monitors and executes rules. XML repository relating to the application domain is built using Java bean. In connection with rules, classes are implemented, which receive and parse rules and store them in the JESS environment. Once a new rule arrives, the change is sensed and the new rule in the form of an XML file is parsed, and corresponding JESS rule is formed and asserted to the JESS inference engine.

For the Rule execution engine, JESS functionality is incorporated inside a class and the incoming rule is parsed using this functionality, and asserted as a JESS rule in the Rete engine (the JESS execution engine). Whenever an event occurs, it is converted into a JESS fact and asserted into the JESS Rete engine. Whenever all facts corresponding to a JESS rule occurs, the JESS rule gets activated, and as a result, a notification message is sent back to the user using the SOAP protocol. When any of the mutation events happen then XML file that consists of rules is parsed and the rule that corresponds to the event is triggered and that rule node is fetched. Then the XQuery in the condition tag is read and it is evaluated. If it is true then value of the action tag is read which is a SOAP call. Then the SOAP call is executed which delivers the data to the interested recipients.

```clojure
(defrule r1 (and(insert Book ?ft1 )) (and(delete Author ?ft2 )) =>(bind ?stmin0 (min ?ft1 ?ft2 )) (bind ?stmax0 (max ?ft1 ?ft2 )) (assert(st0 ?stmin0 ?stmax0)))
```  
Fig. 9. JESS rule <sup>d</sup>r1<sup>T</sup>

```verilog
(defrule r2 (and(insert Publisher ?ft3))(and(delete book ?ft4)) => (bind ?stmin1 (min ?ft3 ?ft4))(bind ?stmax1 (max ?ft3 ?ft4))(assert(st1 ?stmin1 ?stmax1)))
Fig. 10. JESS rule 'r2'.
```

## 6.1. Sample rule

Consider a client who submits the following request: if the time between the arrival of a new book and an author being completely sold out overlaps the time between the arrival of a new publisher and a book being completely sold out, then the user requests a notification. The condition is that the publisher should be Addison-Wesley. The XML format of the above rule will be as in Fig. 8.

The condition part of the rule is taken care in the XML server using the XQuery package. From the entire database, only those with publisher as Addison-Wesley are considered for the above operation. The above rule has the temporal event <sup>d</sup>overlap<sup>T</sup>. Two composite events are said to overlap each other if the time of occurrence of the first basic event of the first composite event is less than the time of occurrence of the first basic event of the second composite event and the time of occurrence of the last basic event of the first composite event is less than the time of occurrence of the last basic event of the second composite event.

Conversion of the above XML rule into JESS rule is as follows. The first Composite Event involves the <sup>d</sup>insert Book<sup>T</sup> and <sup>d</sup>delete Author<sup>T</sup> basic events. It gets converted as shown in Fig. 9.

The second Composite Event involves <sup>d</sup>insert Publisher<sup>T</sup> and <sup>d</sup>delete Book<sup>T</sup>. It gets converted as shown in Fig. 10. The final rule for Overlaps is shown in Fig. 11.

The temporary rules r1 and r2 corresponds to the two individual composite events. Rule r1 checks whether the basic events in the composite event, namely, <sup>d</sup>insert book 50<sup>T</sup> and <sup>d</sup>delete Author 75<sup>T</sup> occur. Then the minimum of the two times is found and asserted as ?stmin0. This forms the start time of the Composite event. Similarly, the maximum of the two times is found and asserted as ?stmax0. This forms the end time of the Composite event. Then these two times are asserted in the form of a fact with head st0. The same process is repeated for rules r2 that monitors the second composite event.

Rule r3 forms the original rule for overlap. Here, the intermediate facts namely st0 and st1 are checked whether they have been asserted. Then the start times and end times are compared to check whether the two composite events do indeed overlap. If so, the event is triggered and the notification is sent back to the client.

## 7. Conclusion

In this paper, a system that uses active rules to provide e-services for the requested users in a reactive manner is discussed. The Generic Composite Event Rule Markup Language (GCERML) that has been designed in this work is generic and can suit for any kind of application domain. GCERML has been designed to represent different kind of events, which includes basic events with simple time events, composite events, component events and temporal events. The Rule Server has been implemented to accept client rules, convert them to XML rules in GCERML format and send the rule to the XML server. The monitoring of basic events has been implemented using the DOM event handler. The monitoring of complex events like temporal and composite events has been implemented using the JESS inference engine. The condition checking has been implemented using XQuery. The action part of the rule is a SOAP call to the requested client.

```txt
(defrule rul0 (st0 ?stmin0 ?stmax0)(st1 ?stmin1 ?stmax1)(test(<?stmin0 ?stmin1))(test(< ?stmax0 ?stmax1))(test(> ?stmax0 ?stmin1)) => (notify http://localhost:8080/simple/receiver))
```  
Fig. 11. JESS final rule.

This work can be enhanced in such a way that each XML Server can have the DTDs of other servers in order to enable communication between them. This hints that one XML Server can trigger an event that can take place in another Server. Currently only one rule server exists. This rule server sends the rule it receives from the client to the appropriate XML server. An improvement over this could be to distribute the rule server. Thus there can be several rule servers, which function in parallel and submit the client’s rule to the appropriate XML servers. In this case, synchronization among the rule servers has to be taken care of.

## References

[1] James Bailey, Alexandra Poulovassilis, Peter Wood, An event-condition-action Language for XML, WWW, 2002, pp. 486– 495.

[2] A. Bonifati, S. Ceri, S. Paraboschi, Active rules for XML: a new paradigm for e-services, VLDB Journal 10 (1) (2001) 39– 47.

[3] A. Bonifati, S. Ceri, S. Paraboschi, Pushing reactive services to XML repositories using active rules, Computer Networks 39 (5) (2002) 645– 660.

[4] Yong Sik Chang, Jae Kyu Lee, Case-based modification for optimization agents: AGENT-OPT, Decision Support Systems 36 (4) (2004) 355– 370.

[5] Eunsuk Cho, Insuk Park, Soon J. Hyun, Myungchul Kim, ARML: an Active Rule Markup Language for Sharing Rules among Active Information Management Systems, First International Workshop on RuleML 2002.

[6] Ernest J. Friedman-Hill. JESS, The Expert System Shell for the Java Platform, http://herzberg.ca.sandia.gov/jess.

[7] N.H. Gehani, H.V. Jagadish, O. Shmueli, Event specification in object oriented databases, ACM-SIGMOD International Conf. on Management of Data 1992.

[8] N.H. Gehani, H.V. Jagadish, O. Shmueli, Composite event specification in active databases: model and implementation, 18th International Conf. on Very Large Databases 1999.

[9] HyoungDo Kim, An XML-based modeling language for the open interchange of decision models, Decision Support Systems 31 (4) (2001) 429–441.

[10] Akhil Kumar, J. Leon Zhao, Workflow support for electronic commerce applications, Decision Support Systems 32 (3) (2002) 265– 278.

[11] Ronald M. Lee, Automated generation of electronic procedures: procedure constraint grammars, Decision Support Systems 33 (3) (2002) 291–308.

[12] Rey-Long Liu, Yun-Ling Lu, Distributed agents for costeffective monitoring of critical success factors, Decision Support Systems 35 (3) (2003) 353 – 366.

[13] Diego Lopez De Ipina, An ECA rule-matching service for simpler development of reactive applications, Proc. of IFIP/ ACM Middleware 2001, Nov. 2001.

[14] Richard Monson-Haefel, Enterprise Java Beans, 2nd Ed., O’Reilly Publishers, 2000.

[15] Jae Heon Park, Sang Chan Park, Agent-based merchandise management in business-to-business electronic commerce, Decision Support Systems 35 (3) (2003) 311 – 333.

[16] Norman W. Patron, Active Rules in Database Systems, Springer-Verlag, New York, 1999.

[17] Abraham Silberschatz, Henry Korth, S. Sudarshan, Database System Concepts, 4th ed., McGraw Hill Publishers, 2002.

[18] Simple Object Access Protocol (SOAP), http://www.w3.org/ TR/SOAP.

[19] S. Swamynathan, A. Kannan, T.V. Geetha, Multi user rule categorization for intelligent web services using XML active rules, International Business Information Management Conference, Egypt, 2003, pp. 616– 623.

[20] Ray Tsaih, Yu-Jane Liu, Wenching Liu, Yu-Ling Lien, Credit scoring system for small business loans, Decision Support Systems 38 (1) (2004) 91– 99.

[21] J. Widom, S. Ceri (Eds.), Active Database Systems: Triggers and Rules for Advanced Database Processing, Morgan Kaufmann, 1996.

[22] XML Path Language (XPath), http://www.w3.org/TR/XPATH.

[23] XML Query Language (Xquery), http://www.w3.org/TR/ XQuery.

S. Swamynathan is working as a Senior lecturer in Department of Computer Science and Engineering. He is currently working for his PhD. His email address is swamyns@annauniv.edu.

A. Kannan received his PhD in Computer Science and Engineering. He is working as an Assistant Professor in Department of Computer Science and Engineering. He has published many articles in national and international journals. His research area includes Database Technology, Artificial Intelligence and Web Technology. His email address is kannan@annauniv.edu.

T.V. Geetha received her PhD in Computer Science and Engineering. She is a professor and currently the head of the Department of Computer Science and Engineering. She has published many articles in national and international journals and also handling many consultancy projects. Her research area includes Natural Language Processing and Web Technology. Her email address is rctamil@annauniv.edu.
