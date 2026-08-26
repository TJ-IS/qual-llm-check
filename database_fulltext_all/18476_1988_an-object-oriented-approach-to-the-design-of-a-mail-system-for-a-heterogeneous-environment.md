---
otero_id: 18476
otero_key: "R8QQGUW5"
title: "An object-oriented approach to the design of a mail system for a heterogeneous environment"
authors: "Feng-Yang Kuo"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90072-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Object-Oriented Approach to the Design of a Mail System for a Heterogeneous Environment

Feng-Yang Kuo \*

Information Systems, College of Business University of Colorado, Denver, CO 80202-2219, USA

The design of an electronic mail system, MASH, is presented in this paper. The system, to be used in a heterogeneous environment, provides common user interfaces that allow the use of several diverse workstations. It also allows message transmission through different networks. An object-oriented approach is adopted to model the handling of the user interface and communication. This approach results in procedural transparency to users when using the system.

Keywords: Communication management, Electronic mail system, Heterogeneous environment, Layered software, Mail host, MASH, Network, Object oriented approach, User interface management, Workstation.

![](/api/attachments/R8QQGUW5/fulltext/images/15974d24cfd59f2021659d712b0312157c894ffefb4edd87ccc5fb6fb2423001.jpg)

Feng-Yang Kuo is Assistant Professor in the Information Systems Division, University of Colorado at Denver. He received his B.S. degree in Management Science from Chiao-Tung University, Taiwan; M.S. degree from Clarkson University, Postdam, New York; and Ph.D. degree from University of Arizona. Dr. Kuo's current research interests include user interface design, database management, and office automation.

\* The author thanks Professor Benn Konsynski of University of Arizona for the opportunity to work in this project. He also thanks R. Chen and A. Chang for their outstanding effort when the project was in progress. The research was sponsored in part by a grant from the U.S. Army Information Systems Command.

## 1. Introduction

In today's automated office, man-computer and computer-computer communication occurs in a heterogeneous environment. The man-computer communication environment consist of microcomputers of different architectures from different vendors; the computer-computer communication environment includes many alternative local area and long haul networks that may be incompatible with each other.

This heterogeneous environment can create serious problems for an electronic mail system user who must rely on several incompatible workstations and networks for communicating with various locations. The user may have trouble learning to use those different workstations, mail systems, and networks efficiently.

This paper presents the development of a user-friendly electronic mail system designed for use in a heterogeneous environment (Fig. 1). The system, called MASH (Mail Access Supporting Heterogeneity), provides common user-system interfaces across workstations and it hides the complexities of the network from the user. The concepts involved are applicable to large, multi-site organizations where personnel are required to use many incompatible workstations and networks. The benefits of the system include ease in training personnel to cope with environmental complexity and increased personnel productivity yielded by common user interfaces.

## 2. Electronic Mail Systems and the MASH Architecture

There are several types of mail systems available for electronic message exchanges in offices.

The first is a mainframe- or mini-computer based mail system, such as VMS MAIL or UNIX MAIL, which allows users of the same computer or of the same computer-cluster to exchange messages with one another. The system also allows messages to be sent to people in remote locations if the computer is connected to a long haul network.

These mainframe- or mini-computer based systems are difficult to use in a heterogeneous environment because they require the user workstation, normally an intelligent microcomputer, to become a dumb terminal. The user must know how to use a communication software for terminal emulation and for local area network connection; s/he must also learn to use the mail system for local or long distance mail exchange. The problem becomes worse when several local area networks, and/or computer mail systems, are involved. Then, an office worker not familiar with computers may not be able to learn all the technical details of the several systems in use.

The second type is a mail system that is a part of an integrated software package for office automation, like ALL-IN-ONE [1]. It allows the user to work with the integrated package at the workstation without knowing the technical details of both the network and the mainframe- or mini-computer to which the workstation is connected. Such integrated software packages are usually computer vendor and/or network specific. In a heterogeneous environment where many different computers and networks are employed, a user still must learn mail systems from several different packages.

The third type, a standalone workstation mail system, is designed for use in a distributed environment. A prototype is discussed in [13]. This system consists of two main components: a user agent that resides in a workstation and a message agent that resides in a back end office processor, i.e., computer. A user interacts wi#. the user agent to create and to retrieve messages. The message agent of the office processor is responsible for transmitting messages among office processors that are connected to the network. In still another prototype system [12], a User Interface Program and a Message Processing Module are used to facilitate mail exchange. This type of system is particularly useful for multimedia, e.g., text, voice, graphics, etc., mail exchange.

![](/api/attachments/R8QQGUW5/fulltext/images/54a68c1501239cc664f17884e847413c89418170579732abb01687e557af3ec5.jpg)  
Fig. 1. The MASH environment.

The MASH system architecture presented in this paper resembles that of the third type of mail system. It has three components: the user interface component which allows a user to create and to read mail messages; a data management component which facilitates storage and retrieval of messages; a communication management component which facilitates transmission of messages through various networks.

A major difference between MASH and the third type of mail system is that with MASH more than one mail host, analogous to the message agent, can be connected to a workstation (Fig. 1). As a result, communication management functions must be handled by both the workstations and the mail hosts. In addition, because a MASH user is not limited to a workstation, s/he must can use any available workstation, at any location, to transmit messages. For this reason, standard dialogues must be provided to facilitate user learning of the MASH user interface across workstations. The challenge of the MASH design is to develop a software architecture supporting these heterogeneous workstations, networks, and mail hosts. To do so, an object-oriented approach [8] is adopted to model the handling of user interface, data, and communication for the system.

An object is an abstraction of a real world entity; it is described by a set of data attributes and operations that it can perform. There are several advantages associated with an object-oriented approach. First, when a system is described by a set of interrelated objects, the system is modular: information and operations of one object are hidden from other objects. Second, objects are classified into different classes; instances of the same object class can be created with the same data and operational characteristics. Third, there can be object subclasses. These inherit all data attributes and operations of the parent object class.

![](/api/attachments/R8QQGUW5/fulltext/images/9a69e4bae8e048d924c59b6cd5fed2921c8d6bde9805547d042102af5d1fab30.jpg)  
Fig. 2. MASH' architecture from the object perspective.

Conceptually, the MASH system can be described as a set of interdependent objects. Examples of these objects are mail boxes and mail messages (Fig. 2). A MASH object is defined by its user interface, its data, and its communication attributes. Also associated with the object are its operations for user interface, data, and communication. Those operations are facilitated by a set of software utilities provided to implement the system on various workstations (Fig. 3).

An important distinction between the object-oriented approach to modeling and to implementation must be made here. The MASH sytem is modeled with an object-oriented approach but is not implemented with an object-oriented programming language such as SMALLTALK 80 [4]. Instead, the PASCAL language is used for implementation because of its availability for different workstation environments. What is said here, therefore, must not be confused with object-oriented implementation of MASH. Because MASH data operations include relatively simple retrieval and storage functions, they will not be discussed in detail in this paper.

## 3. MASH User Interface

The MASH user interface component accepts and interprets user inputs and it presents the results to the user. The traditional approach to implementing the user interface would be to include user interface functions in the MASH software. The drawback to this approach is that the software is less amenable to modifications and it is more difficult to transport the software to different workstations.

![](/api/attachments/R8QQGUW5/fulltext/images/0e46c65b6703f0eea83a49af11caf874c8a0b72526e7c843443d51e6e2b3fa5f.jpg)  
Fig. 3. The MASH software facilities overview.

Unlike the traditional approach, the MASH user interface is designed based on the concept of dialogue independence $[3,7,14]$ . This concept emphasizes the separation of the user interface from the MASH software and of the user interface definition from its manipulation. As a result, the MASH user interface is portable and flexible and its overall design and implementation costs are reduced.

## 3.1. MASH User Interface Attributes

The entire dialogue process of the MASH system consists of a set of hierarchically interrelated objects. At the lower level of the user interface hierarchy are data-oriented objects, like mail messages and mail boxes. At the higher level, are control-oriented objects which facilitate user monitoring of the dialogue process. This design is based on research [11] which suggests that the computer system's representation should be hierarchically structured in order to take advantage of human cognitive power. As later summarized [6], this user interface organization can support both low-level, human information processing which deals mainly with a set of interacting objects, and high-level processing which employs formal rules for aggregating objects to accomplish a task.

MASH objects are classified according to both their uses and their human factor characteristics. A MASH object may be used in one of three ways: as a command, to facilitate control; as data, for creating and modifying mail messages; or as feedback that helps user learning and error correction. In terms of human factor design, a MASH object's interaction requirement can be user

Table 1  
MASH Dialogue Objects.

<table><tr><td>Type code</td><td>Type descriptions</td><td>MASH Objects Names and Descriptions</td></tr><tr><td>a</td><td>Forced command choice type, such as menu and scroll menu</td><td>MAIN: the MASH main menuCREATE/SEND: the menu for creating and sending mailREAD: the menu for reading mail</td></tr><tr><td>b</td><td>Free choice language type, such as a command languages</td><td></td></tr><tr><td>c</td><td>Forced choice data object, such as a menu of data items</td><td></td></tr><tr><td>d</td><td>Free response data object, such as a data form</td><td>HEAD: the form for creating and modifying mail</td></tr><tr><td>e</td><td>Free response data object, such as a table of data</td><td>MBC BOX: the created-mail tableMBS BOX: the send-mail tableMBI BOX: the received-mail tableMBR BOX: the read-mail table</td></tr><tr><td>f</td><td>Free data entry data objects, such as an unformatted document</td><td>EDIT: the form for entering the message</td></tr><tr><td>g</td><td>Combinations of system prompts and the user&#x27;s answers</td><td></td></tr><tr><td>h</td><td>Many levels of help messages</td><td>HELP: showing multiple levels of help messages</td></tr><tr><td>i</td><td>Error/Status/Currency</td><td>MBC: current created-mailMBS: current sent-mailMBI: current received-mailMBR: current read-mailERROR: showing error messagesMAIL-OP: current operation status</td></tr></table>

![](/api/attachments/R8QQGUW5/fulltext/images/d727aca07bd0c9baf2a51fa458151c7ce3e9d077798892bede82ae405b76042d.jpg)  
Fig. 4. The dialogue dependency for creating mail messages.

guided, system guided, user free response, or user forced choice [9]. Thus, the classification of MASH objects is based on two dimensions: purpose and human factor requirements (Table 1).

The hierarchical structure of the MASH user interface is defined by object dependencies. These are preceding or succeeding relationships among objects; each of the relationships is associated with conditions which must be met if the relationship is to be activated. A notation similar to State Transition Diagrams (STD) [5,10,14] is used to show object dependencies. For examples, in the STD used to create a mail message (Fig. 4), a node represents a MASH object. A labeled, directed arc is a conditional transition; the label specifies the transition condition. An unlabeled, directed arc is an unconditional transition. A node may represent still another level of STD, i.e., cluster of objects. In short, the overall MASH user interface can be viewed as a hierarchy of STDs, or clusters of MASH objects (Fig. 5).

The type of a MASH object and its dependency information constitute the primary user interface attributes. However, additional attributes are necessary to complete the user interface description of a MASH object.

A name is assigned to an object as the logical reference to it. Spatial information, i.e., the location and the size of the object, and lexical elements, e.g., menu options, error messages, etc., are also required to convey "what," "how," and "why" that the user needs to supply. Finally, video attributes can be specified to highlight a certain part of an object in order to keep the user's attention. Those attributes, i.e., type, dependency, etc., are encoded in a computer readable format (Fig. 6) and they are converted to the format required for different workstations.

## 3.2. MASH User Interface Operations

A MASH object's operations are defined by its object type. Those operations associated with an object include accepting and interpreting user input; responding to the user action, i.e., selection, insertion, and deletion; handling feedback operations; and maintaining the overall image of the object. An object is activated according to its dependency attributes.

The architecture of the MASH software which facilitates objects' user interface operations in a heterogeneous environment is of interest. This software can be characterized as portable, reusable, and consistent. To achieve portability, the MASH software is layered (Fig. 7). The lower-layer software is hardware dependent so it can handle primitive user interface operations. The higher-layer software, built on top of the lower-layer software, provides functions necessary to perform a series of operations on a MASH object. When transported to a different workstation, only the lower-level software has to be modified; thus the portability of MASH software is increased.

Both lower- and higher-level MASH software are reused. To facilitate the operations of MASH objects, a higher-level software function is created for each type of object. This software function invokes necessary lower-level software routines. In addition, higherlevel software functions are used to support screen utilization by different clusters of objects.

In the MASH implementation, each object has its own view port and each cluster has its logical display area. Both use the same physical display device. The higher-level software functions (1) initialize the logical area and view ports to be used, (2) activate objects, (3) deactivate objects, and (4) resume and erase the logical area and view ports.

![](/api/attachments/R8QQGUW5/fulltext/images/da7e78cff01119071e228e6b1b85def04e1bac42616b6bb0cba83cc94799e865.jpg)  
Fig. 5. MASH objects and their dependency overview.

As a result of this, the task of developing the MASH user interface is reduced significantly.

User keystroke interactions invoking MASH object operations are consistent because a common set of lower-level software routines is provided to handle the keystroke interactions for different types of objects. As a result, the keystrokes for "selection" of an object or an item within an object, insertion and deletion of a user entry, and execution or abortion of a user operation are standardized for all types of objects. Higher-level software functions also keep track of the information about current and suspended user operations. This information includes the state of

## (a) Notations

R: Row
C: Column
UL: Upper left
LR: Lower right
at - specify the location of an option or item
is - specify the syntax of an option or an item
to - specify the transition to another dialogue object
/\* \*/ - comments

## (b)

NODE NAME: Main
TYPE: 'a'
SIZE: UL (R1 C2) LR (R9 C18)
IMAGE:

## VISIBILITY: 1

OPTION 1: at R+2 C+2    /\* location relative to the UL position\*/
    is "MAIN"    /\* the syntax is MAIN \*/
    to    /\* no transition performed \*/
OPTION 2: at R+3 C+2    /\* location relative to the UL position\*/
    is "CREATE/SEND"    /\* the syntax is CREATE/SEND \*/
    to CREATE/SEND    /\* transition to the node CREATE/SEND \*/
OPTION 3: at R+4 C+2    /\* location relative to the UL position\*/
    is "READ"    /\* the syntax is READ \*/
    to READ    /\* transition to the node READ \*/
OPTION 4: at R+6 C+2    /\* location relative to the UL position\*/
    is "PROFILE"    /\* the syntax is PROFILE \*/
    to PROFILE    /\* transition to the node PROFILE \*/
OPTION 5: at R+7 C+2    /\* location relative to the UL position\*/
    is "LOCAL LIST"    /\* the syntax is LOCAL LIST\*/
    to LIST    /\* transition to the node LIST \*/

Fig. 6. The readable format of a MASH object's definition.

user actions and the status of MASH operations. Thus, complexity for the user to navigate between different clusters of objects is reduced.

![](/api/attachments/R8QQGUW5/fulltext/images/c07d01196feebedcdf1209fc826af07b0571aa96e8b59133acabf2e1837fb1e6.jpg)  
Fig. 7. The layered dialogue execution software.

## 4. MASH Communication

MASH's communication media include several incompatible local area network alternatives, such as SYTEK and ETHERNET and the long haul network DDN (Defense Data Network). In addition, many mail systems of different host computers are used as mail hosts for a user workstation. Complexity emerges when the various mail hosts and network alternatives involved require substantially different protocols for sending and receiving messages. If not transparent, the different protocols may overwhelm nontechnical users and hamper their productivity.

<table><tr><td>Message object</td><td>Mail Host Script Object</td><td>Resulting SCS for sending a VAX MAIL message</td></tr><tr><td>Mailbox</td><td>USERNAME</td><td>INITIATE ibmxt-1 I/O PORT</td></tr><tr><td>Time Created</td><td>PASSWORD, T60, P$</td><td>MEDIA IS sytek, CALL IS call</td></tr><tr><td>Keywords</td><td>[ READMAIL</td><td>NUMBER IS ?11,</td></tr><tr><td>Subject</td><td>ACKNOWLEDGE STATUS ]</td><td>TIMEOUT IS 50</td></tr><tr><td>From</td><td>[ SENDMAIL</td><td>HOST IS VAX, NAME IS Smith,</td></tr><tr><td>To</td><td>Mailbox</td><td>PASSWORD IS htims</td></tr><tr><td>Folder/File</td><td>Subject/Keywords</td><td>TIMEOUT IS 60</td></tr><tr><td>Rec-Status</td><td>To</td><td>PROMPT IS $</td></tr><tr><td></td><td>WAIT STATUS ]</td><td>[ SENDMAIL</td></tr><tr><td></td><td>[ MAIL DIRECTORY</td><td>Mailbox</td></tr><tr><td></td><td>ACKNOWLEDGE STATUS ]</td><td>(Time Created)</td></tr><tr><td></td><td></td><td>Subject/Keywords</td></tr><tr><td>Destination Object</td><td>Network Script Object</td><td>(From)</td></tr><tr><td></td><td></td><td>To</td></tr><tr><td></td><td></td><td>(Folder/File)</td></tr><tr><td>Name</td><td>SESSION</td><td>STATUS ]</td></tr><tr><td>Mailhost</td><td>[call NUMBER T50]</td><td>HOST LOGOUT using logout/nohandup</td></tr><tr><td>Network</td><td>TERMINATE SESSION done</td><td>MEDIA LOGOUT USING done</td></tr></table>

Fig. 8. An example of SCS construction. Note that the environment consists of IBM PCs, a SYTEK local area network, and a VAX computer with the VMS MAIL.

This problem is solved by introducing objects which carry communication attributes defining what to do with different mail systems, host computers, and network alternatives. These attributes deal mainly with the upper three layers of the ISO O!S model: the session, the presentation, and the application layers. Specifically, communication attributes define the session establishment protocols for the MASH system to connect to various mail hosts, presentation format, and commands to invoke and execute the requested host's mail system. A command language interpreter is used to interpret the attributes and to transmit a message accordingly.

The MASH system relies on existing mail hosts and networks to support the communication operations of a message object. The MASH system is responsible only for creating a message object with its user interface component and for adding communication attributes to its communication component. Once the message object is created and leaves the user workstation, it "flows" in the network until it reaches its destination.

## 4.1. MASH Communication Attributes

A message object is produced by aggregating the HEAD and the EDIT objects generated by the user in the MASH user interface component. It consists of the attributes: TIME-CREATED, KEYWORDS, SUBJECT, FROM, TO, CC, FOLDER-FILE, and REC-STATUS. FOLDER-FILE refers to the main archive file of the mail host; REC-STATUS is used to indicate if the message has been received. Three additional types of objects are used for defining communication attributes: Destination, Mail Host Script, and Network Script.

A Destination object has attributes that describe a person who may receive any message sent by the user: NAME, MAIL HOST, and NETWORK. Instances of this object type are created by querying the user. They are stored in the Destination database. The Mail Host Script object contains protocol definitions used for establishing a session with a mail host and for invoking the desired mail system when many mail systems are available on a given host computer. The Network object contains protocol definitions of a network. Instances of both types of objects are stored in the Mail Host script database and the Network Script database respectively.

Message, Destination, Mail Host Script, and Network Script objects as well as the user's profile are used to generate Service Communication Scripts (SCS) by a tool called the Communication Packaging Manager (CPM). CPM consists of data to be transmitted and a series of language statements used for both transmission and function invocation. Fig. 8 depicts the construction of SCS for sending messages in an environment consisting of IBM PC workstations, a SYTEK local area network, and a VAX computer with VMS MAIL function [2]. Information specific to a user, such as NUMBER, NAME, and PASSWORD, is obtained from a user's profile. The user's profile includes attributes such as user names and passwords for various available mail hosts. The additional items, "Time," "From," and "Folder-File," are put in parentheses because the VMS MAIL software does not require "Folder-File" and it issues its own "From" and "Time Created" values; a part of the CPM's function is to ensure that SCS do not include attributes conflicting with those of the selected mail host.

## 4.2. MASH Communication Operations

MASH communication operations are facilitated by a command language interpreter. Fig. 9 shows the commands available. A detailed discussion of SCS language can be found in Chang [2].

The command interpreter software separates program functions from the definitions of the media and the host environments. To do this, a library of general software modules and protocol definitions of network alternatives are provided for each protocol layer. The command interpreter invokes only those communication software modules required to execute the SCS. Consequently, it allows a workstation to communicate flexibly in multi-host, multi-network environments without requiring a separate communication program for each environment. This separation of communication software from protocol definitions is termed communication independence in the MASH project.

## 5. Summary

In summary, the MASH system architecture consists of a set of hierarchically dependent objects, each of which is defined by user interface, data, and communication attributes. Software is provided to facilitate operations for user interface, data, and communication according to the object definitions. Both the definitions and the software which supports operations of objects are relatively portable. As a result, the MASH system provides a user with standard dialogues that work in many different workstations while they hide the complexities involved with using various network alternatives.

```txt
1. INITIATE [ ] I/O PORT;
2. MEDIA IS [ ], CALL IS [ ], NUMBER IS [ ], AND TIMEOUT IS [ ], UNTIL [ ];
3. USING [ ] UNTIL [ ];
4. LOOP;
5. LOOPING [ ] TIMES, UNTIL [ ];
6. HOST IS [ ], NAME IS [ ], PASSWORD IS [ ], AND EXTRA NAME IS [ ], EXTRA PASSWORD IS [ ], AND TIMEOUT IS [ ], PROMPT IS [ ];
7. INVOKE [ ], TIMEOUT IS [ ], UNTIL [ ];
8. HOST LOGOUT USING [ ], UNTIL [ ];
9. MEDIA LOGOUT USING [ ], UNTIL [ ];
10. BREAK;
11. EXIT.
12. READMAIL;
13. SENDMAIL;
Fig. 9. The MASH's communication interpreter's commands.
```

Although no formal survey has evaluated user satisfaction with the MASH system, experience with the system suggests that users enjoy the user interface because of its flexibility and its procedural transparency for using different networks. One common complaint is that although MASH dialogues are consistent across workstations, they are not compatible with typical office systems like work processing and database management systems. This problem is difficult to solve unless dialogue standards are established for all applications. However, recent research has reported the use of user interface management tools to facilitate user interface operations. Such tools can be responsible for enforcing the standards for all office systems.

The MASH system can easily adapt to multiple networks because of its communication interpreter. However, this approach has a costly drawback: slower communication speed due to the overhead in determining the invocation of software modules. Future research is needed to evaluate network utilization of alternative approaches.

Finally, research is needed to study decision rules as attributes of MASH objects. Experience shows the MASH system is too active currently. For example, in urgent, real-world situations, a message system, i.e., phone and/or face-face, is actually used to relay the emergency message from one person to another until the message reaches its intended destination or an acceptable substitute. The MASH system in its present form still relies on its users to relay messages; messages are not automatically routed.

A possible solution to the problem is to incorporate routing rules in the MASH message objects. These rules, generated by examining organizational and individual policies, would determine appropriate message routing and destinations. Message objects, characterized by user assigned KEYWORD and PRIORITY attributes, would activate object rules to deal with special circumstances now requiring human involvement. This would allow the system to become a more responsive tool for group decision making.

## References

[1] All-IN-1 Application Programmer's Reference Manual, Digital Equipment Corporation, 1982.

[2] Chang, H. Communication Scripts for the Computer Based Message Systems, Technical report, University of Arizona, Tucson, Arizona, 1985.

[3] Coutaz, J. Abstractions for User Interface Design, Computer 19, No. 9, 1985, pp. 21–38.

[4] Goldberg, A and Robson, D. Smalltalk 80: the Language and its Implementation, Addison-Wesley, 1983.

[5] Jacob, R. Using Formal Specifications in the Design of a Human-Computer Interface, Communication of the ACM, April, 1983, pp. 259–264.

[6] Jagodzinski, A.P. A Theoretical Basis for the Representation of On-line Computer Systems to Naive Users, Int. J. Man-Machine Studies 18, 1983, pp. 215–252.

[7] Kuo, F. and Konsynski, B. Dialogue Management: Support for Dialogue Independence, MIS Quarterly 12, No. 3, 1988, pp. 481–499.

[8] Lipkie, D., Star Graphics: An Object-Oriented Implementation, Computer Graphics, pp. 115–123, July 1982.

[9] Miller L. and Thomas, J., Behavioral Issues in the use of Interactive Systems, Int. J. Man-Machine Interfaces 9, 1977, pp. 509–436.

[10] Parnas, D. On the Use of Transition Diagrams in the Design of a User Interface for an Interactive Computer System, Proc. 24th Natl. ACM Conference, 1969, pp. 379–385.

[11] Rasmussen, J. The Human as a System's Component, Human Interaction with Computers, Academic Press, London, 1980.

[12] Reynolds, J.K., Postel, J.B., Katz, A.R. Finn, G.G. and DeSchon, A.L., The DARPA Experimental Multimedia Mail System, Computer, October, 1985, pp. 82–89.

[13] Sakata, S. and Ueda, T, A Distributed Interoffice Mail System, Computer, October, 1985, pp. 106–119.

[14] Wasserman, A.I. Percher, P., Shewmake, D. and Kersten, M., Developing Interactive Information Systems with the User Software Engineering Methodology, IEEE Tans. Software Engineering, Vol. SE-12, No. 2, 1986, pp. 326–345.
