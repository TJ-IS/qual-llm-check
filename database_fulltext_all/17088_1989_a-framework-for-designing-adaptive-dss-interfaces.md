---
otero_id: 17088
otero_key: "XPCCQHZH"
title: "A framework for designing adaptive DSS interfaces"
authors: "Brian L. Dos Santos; Clyde W. Holsapple"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90024-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Framework for Designing Adaptive DSS Interfaces

Brian L. DOS SANTOS

Krannert Graduate School of Management, Purdue University, West Lafayette, IN 47907, USA

Clyde W. HOLSAPPLE

Department of Decision Science and Information Systems, College of Business and Economics, University of Kentucky, Lexington, KY 40506-0034, USA

In addition to customary problem domain knowledge, a decision support system could benefit from the accommodation of two other types of knowledge: user knowledge and self knowledge. Past DSS research has focused on domain knowledge in various guises including data, procedures, rules sets, text, forms, spreadsheets and so on. In introducing the two new knowledge system dimensions, we argue that they are crucial to thinking about what it means for a DSS to have adaptive, easy-to-use interfaces. Based on a human support system metaphor, the framework presented here is also an important step in the direction of designing, implementing and researching such interfaces.

Keywords: Decision Support Systems, User Interface, Adaptive Interface, Knowledge Management.

![](/api/attachments/XPCCQHZH/fulltext/images/c9184f7cb8a7acbea07bcd37f64dd8c9c8707897f98b0d8b9e4cc837f4f91ea9.jpg)

Brian L. Dos Santos is Assistant Professor of Management Information Systems at the Krannert Graduate School of Management, Purdue University. Prior to his current position, he was an Assistant Professor at the University of Wisconsin, Madison. His main fields of research are decision support systems, user interfaces, and management of information systems. His articles have appeared in journals such as Management Science, Information and Management, Omega, and

Management Decision. He has been a consultant to a number of organizations in both the Private and Public sectors and has lectured on information systems topics at the National and International meetings.

## 1. Introduction

The use of computer-based systems in support of management decision making has increased dramatically over the past decade. During the same period, there has been a great deal of research on decision support system (DSS) development. Although there has been significant progress, development of DSS user interfaces is a topic that has received relatively little research attention. To be sure, every DSS has a user interface, but they tend to be developed on an ad hoc basis, without the benefit of a formal framework for design. Their features are not so much a reflection of what is possible, as they are a pragmatic response to immediately sensed needs. Consequently, the interface is often one of the weakest aspects of a DSS in the sense of being unnecessarily restrictive and inflexible. What is suitable initially, becomes constraining as user needs change in the face of time and experience.

By user interface, we are referring to those attributes of a DSS that define the interaction between the user and the DSS. It has been argued that from the user's perspective, the interface is the system and is the most important element of a DSS [32]. Further, the interface can determine the impact a DSS has on decision making [1,32]. It follows that a general framework, which alerts developers to interface design possibilities that might otherwise be overlooked, is a valuable step in the direction of facile interfaces and better decision making. Here, we are not referring to recognition of alternative interface styles such as menus, command language or direct manipulation. Stylistic concerns are important, but do not get at the deeper issue of understanding adaptive interface design possibilities. By addressing the more fundamental issue in this paper, we do not preclude any style or combination of styles.

![](/api/attachments/XPCCQHZH/fulltext/images/932c93d0c2f4d598ef04c7ce92420b5156538ab4928770108b09c065b5bafe47.jpg)

The terms user friendly and easy-to-use are often used to describe good interfaces $[9,22]$ . However, the phenomenon of friendliness (or ease-of-use) is not well understood. An interface feature that seems “friendly” in one situation may be extremely “unfriendly” in another $[33]$ . For example, a feature that seems friendly to a novice user of a system may seem unfriendly to an experienced user of the system, and vice-versa $[9,13,25]$ . Over time, a novice user can become an experienced user of a DSS. Furthermore, a user can be experienced in the use of some DSS capabilities and, at the same time, a novice in the use of other capabilities. Consequently, an interface will be friendly (or continue to remain so) only if it can adapt itself, or be easily adapted, regardless of stylistic traits $[20]$ .

In addition to user characteristics, the literature suggests that the quality of an interface is dependent upon task characteristics $[1,9,22]$ . In a DSS context, the task involves the use of a computer system in support of decision making (i.e., a DSS). DSSs, however, are becoming increasingly complex. While early DSSs provided users with relatively few capabilities, providing limited support to users, current DSSs provide users with extensive functional capabilities. For example, early DSSs often provided users with access to a few models interfaced to appropriate data, allowing users to select a model and the data to perform analysis. Today, DSS software allows users to build new models, modify existing models, access data and models on different computer systems, and so forth. For the interface designer, providing an easy-to-use interface to a system that has extensive capabilities is a challenging problem $[9]$ .

There has been a good deal of research on man-machine interfaces for computer systems and many books [8,15,30] and periodicals $^{1}$ are devoted primarily to the subject. Much of the recent literature has dealt with interactive user-computer communication. Within this arena, the issue of self-adaptive interface systems is beginning to emerge. For a tutorial introduction, see [12]. Although user-DSS communication is interactive, the literature on DSS interfaces does not explicitly consider the overall interactive nature of DSS use. Instead, DSS researchers have focused on either the inputs or the outputs of a DSS. For example, researchers have focused on interface characteristics and language systems for specifying user requests [1,5,7] (i.e., the inputs), and the presentation of output to users [2,21,28]. The quality of a DSS interface, however, is determined by the quality of the user-DSS interaction.

If a DSS is to be used by many different users for different tasks, its interface must be easily adaptable. The development of DSS interfaces has been hindered by the absence of an adequate framework to guide DSS interface developers in the development of adaptive interfaces. In this paper, a framework is presented to aid in the development of adaptive interfaces. First, a model of user-DSS interaction is presented and this model is used to derive design objectives for easy-to-use interfaces. Then, a general framework is proposed to facilitate the development of adaptive interfaces that will meet the design objectives. Finally, impacts of the framework are discussed, namely, the types of knowledge and problem processing capabilities necessary to develop adaptive interfaces.

## 2. Related Research

A well known generic framework for DSS design suggests that a DSS should have three subsystems: a language system (LS), a knowledge system (KS), and a problem processing system (PPS) [6]. This framework is shown in fig. 1. The KS contains the DSS's body of knowledge about the problem domain. Included in the KS are data, models, rule sets, forms, templates, and so on. The PPS is a processor that is capable of accepting problems stated in the LS and manipulating knowledge in the KS to generate appropriate responses to support the decision making process. The LS in this framework includes all the linguistic facilities made available to a decision maker by a DSS. The LS is the means by which the decision maker communicates with the DSS. The responses from the PPS to the user are the means whereby the DSS communicates with the user and are collectively referred to as the presentation system (PS). Like the LS, the PS is a system of representation. Together, the LS and the PS characterize the user interface. This is made explicit in fig. 2.

![](/api/attachments/XPCCQHZH/fulltext/images/00a586add414e6cea6f637863e08ce43f3a666f7c7f65a9d99fcf93dce1a2c07.jpg)  
Fig. 1. A generic DSS (Source: Bonczek, Holsapple and Whinston (1980)).

Research on the user interface can be separated into research on communications from the user to the system (the LS) and communications from the system to the user (the PS). Prior research has focused on two aspects of the LS: (1) what needs to be specified by the user to communicate effectively with the DSS, and (2) how it is specified. Research on communication from the system to the user (the PS) also has focused on two aspects: (1) helping the user communicate with the system via help and diagnostic facilities, and (2) determining how to present system output to the user.

One focus of LS research has been on the development of easy to use languages to simplify specification by the user in communicating with the system [5,7]. These languages form a continuum between two extremes. One extreme requires the user to state the problem to be solved, leaving it to the system to determine how the problem is to be solved. In this research, the emphasis has been on the development of formal languages for problem specification. The other extreme requires the user to specify the processing necessary to solve a problem. It is generally believed that, from the user's perspective, languages requiring problem specification are preferable to those requiring process specification.

Another focus of LS research has been on making it easy for the user to state problems or processing (as required) that is necessary $[1,25]$ . Current DSS software provide different options for communication with the system, such as menus, commands, question and answer, graphics, or forms. The primary research focus has been on determining the circumstances under which each of the various options is preferable. In addition, the direct manipulation interface style $[19]$ is likely to have an increasing prominence in future DSS interfaces $[17]$ . With it, a user directly manipulates computer output in order to provide computer inputs. In DSS terms, this means that the LS is defined as legitimate manipulations on elements of the PS.

![](/api/attachments/XPCCQHZH/fulltext/images/a3073e57bf6ae8c873a42571077121204dd11453a4348fb1158d183add56dec8.jpg)  
Fig. 2. A modified generic DSS.

Research on help facilities has focused on improving a user's ability to send appropriate problem statements or processing specifications to the system [18,29]. Help facility research has focused on providing appropriate error messages in response to problem statement or processing specification errors, and the provision of online tutorials to help users learn to use system facilities [13,24].

A good deal of DSS research has focused on the presentation of output to users. The emphasis in this research has been on determining the superiority of one output type over another $[11,27,28]$ , or on matching output types to individual user characteristics $[2,21]$ . Although such research is useful in settings where a DSS developer has to decide between one output form and another when building a DSS, it is less useful when users can be provided access to many different forms of output at minimal cost. Currently available hardware and software provides DSS users with access to many different forms of output, allowing a choice of output forms with each use.

It is apparent from this brief review that each research effort has focused on some facets of a user interface to the exclusion of others. Since DSS use is interactive, aspects of both the LS and the PS affect interface quality. While past research helps DSS developers design specific individual characteristics or details of the interface, it fails to provide a style-independent, integrative framework to aid in the development of adaptive DSS interfaces. In the next section, a conceptual model of user-DSS interaction is presented and this model is used to derive design objectives for DSS interfaces.

## 3. Characteristics of DSS-User Interaction

## 3.1. Background

The best known DSS frameworks [7,32] focus on the components of a DSS and their interrelationships. While the latter [32] can be fairly characterized as a special case of the former [7], both frameworks consider the 'system' to be the computer-based aid used by the decision maker (user). The user is viewed as part of the system's environment (i.e., a 'black box'), providing inputs to and receiving outputs from the system, and vice-versa. Although it is generally recognized that users interact with a DSS, little attention has been paid to this interaction. One consequence of a 'black box' view of the user is that DSS interface designs are not easily customized to individual users. For example, DSS interfaces generally do not distinguish between novice and experienced users of the DSS, although different interfaces are necessary for users with different levels of experience [20,25].

Furthermore, in unstructured problem solving situations, the user is an adaptive system, learning from DSS interaction both about the decision problem and use of the DSS. Interestingly, user learning about the decision problem can result in changes to user interaction with the DSS. For example, after observing last month's sales data, a user may wish to build and use a Monte Carlo simulation model. As a consequence, use of a DSS may cause users to move from DSS interactions with which they are experienced (e.g., retrieval of historic data), to those with which they are novices (e.g., building and using a simulation model).

## 3.2. User Considerations

In order to provide an easy-to-use $^{2}$ interface to a DSS that provides extensive capabilities, interface design must consider both the user and the support system. It is useful to consider the decision system (DS) as a user-support system couple aimed at reaching a decision in response to a problem. The user is viewed as an active entity in this system. Within the decision system, problem solving is an interactive process between a user and a support system. The interaction is in the form of messages that are sent from one party to the other. Messages from a user to the support system are referred to as the input interface (i.e., the LS), while messages from the support system to the user are referred to as the output interface (i.e., the PS).

In this interactive environment, both the user and the support system possess problem domain knowledge (i.e., knowledge relevant to the current problem). In addition, meaningful communication between the user and the support system requires that the user possess support system knowledge (i.e., knowledge the user must bring to the session with the DSS in order to use it effectively [3]), and problem processing capabilities that allow the user to use that knowledge to send appropriate messages. Interaction within the decision system is shown in fig. 3.

![](/api/attachments/XPCCQHZH/fulltext/images/11b755680cdfd9468727b974d8b2fd61ac5ad3abba18d0b48004231c447604a7.jpg)  
Fig. 3. Interaction within the decision system.

Conceptually, interaction between a user and the support system can be viewed as a communication system with interaction occurring at two levels, each requiring the user to possess specific knowledge (fig. 4). At the upper level, the user's problem processing system (PPS) uses problem domain knowledge to identify the problem related goals that the support system may satisfy. At the lower level, the user's PPS uses support system knowledge to obtain information relevant to the problem related goals generated at the upper level.

For example, consider a sales manager faced with the problem of assigning sales targets for the Company's sales force. At the upper level, the manager's PPS may determine that last year's sales targets and actual sales information is desired (i.e., the problem related goals). In order to obtain this information, the problem related goals must be transformed by the manager's PPS into an appropriate request, using support system knowledge and/or obtaining support system help to do so. In order to send an appropriate message, user-DSS interaction may be necessary, even though the manager has the necessary support system knowledge. For instance, a series of commands may have to be sent, with the support system validating and accepting each command as it is sent. Diagnostic and help facilities may also be involved. Similarly, request specification may involve the use of a multi-level menu or a series of questions and answers. In each case, there will be some interaction. Thus, for a given problem-related goal generated at the upper level (e.g., determining last year's targets and actual sales), there generally is user-DSS interaction at the lower level (e.g., to get the DSS to provide the desired information).

![](/api/attachments/XPCCQHZH/fulltext/images/3623d7318a9ada2926e50dcc8145bd16c1e12adb0bf4718db7677ef1c4336442.jpg)  
Fig. 4. A model of user/support system interaction.

After studying last year's data, and prior to a decision on sales targets for the current year, the sales manager may wish to derive projections from a sales forecasting model. As before, this problem may require DSS interaction for the user to obtain the desired information. Thus, in terms of user-DSS interaction, there are two types of interaction: (1) problem-oriented interaction, and (2) support-oriented interaction. Problem-oriented interaction is directly related to the user's decision problem. In the above example, this interaction is related to the retrieval or generation of historic sales and target data, and the subsequent use of a sales forecasting model. Support-oriented interaction is initiated for each set of problem related goals, which often are the result of problem-oriented interaction. However, support-oriented interaction is not directly related to the user's decision problem. Instead, it includes the interaction necessary to satisfy problem-related goals. In the above example, the interaction necessary to retrieve sales data is of this type and so is the interaction necessary to obtain model results.

## 3.3. Interface Design Objectives

As the DSS realm becomes more complex (i.e., DSS capabilities and domain knowledge in the KS increases), the cost of acquiring support system knowledge increases. In addition, the cost of sending meaningful messages also tends to increase, because messages may get longer and possibly more complex. For example, for an interface that uses a hierarchical menu format, the breadth and/or depth of the menu system increases as capabilities are added. For a command driven interface, the commands required to state the problem or the processing desired become more numerous or take on added optional clauses.

User knowledge about the support system, while necessary to interact at the lower level, does not itself improve decision making. Similarly, the actual interaction at the lower level (to satisfy a problem related goal) does not improve decision making. It is the information provided by the support system that does. That is, it is the problem-oriented interaction that ultimately determines the value of a DSS. Consequently, an easy-to-use DSS interface will minimize the cost of interacting at the lower level.

There are two types of costs associated with interaction at the lower level: (1) the cost of acquiring support system knowledge, and (2) the cost associated with the actual interaction. Thus, the total cost of interacting at the lower level may be reduced by reducing either or both of these costs. It should be recognized that, for a particular interface, from both the user and designer perspectives, there is a tradeoff between these two types of costs. By incurring additional costs of obtaining/requiring a great deal of support system knowledge, actual interaction costs can be lowered. All else being equal, minimizing the cost of acquiring support system knowledge means that actual interaction costs can be expected to be higher.

It is useful to distinguish between two aspects of the messages transmitted across the interface: (1) what the message sender has to say (message content), and (2) how the message sender can say it (message form). Message content deals with message semantics, i.e., what the sender actually has to say for a message to be meaningful. Message form is related to the means whereby messages are conveyed. Message content and form are closely related in that message content requirements for a meaningful message will determine the forms that are appropriate (i.e., that can be used). For example, if a meaningful message is a procedure, pop-down menus are likely to be a less appropriate form of specification than a series of commands. Both content and form affect interaction costs.

For the input interface, if 'GET AVERAGE SALARY FROM EMPLOYEE TABLE' is a meaningful message that is interpreted by the support system as a request to compute and display the average salary for all employees from an Employee table, then it may be possible to send the content of that message in other ways. Rather than taking the form of a command, it may be sent using a menu, a question and answer format, icons, etc. How a message is conveyed is referred to as the message form. Similarly, for the output interface, requested sales data is the message content, while tabular or bar graph presentations are message forms. What we are calling the message form and content can equivalently be considered the message surface structure and deep structure, respectively [17].

For the output interface, message content requirements require the provision of appropriate responses to input messages. These responses include the provision of responses to input messages from a DSS's KS, as well as the provision of help to enable users to send meaningful messages. Message form also is important for the output interface, as evidenced by past DSS research on the output interface [2,21].

## 3.4. User Differences

Differences among users, and for a single user, differences over time, is the primary reason for designing adaptable interfaces. An important difference among users is their level of expertise in using a DSS. In an increasingly complex DSS realm, users may have only limited knowledge about alternative and/or complementary support system knowledge. A single user may be experienced in using some DSS capabilities and, at the same time, be a novice $^{3}$ in using other capabilities. The difference between novice and experienced users is in the levels of support system knowledge that users possess. Experienced users possess considerable support system knowledge, while novices possess very little knowledge. Consequently, experienced users are able to reduce interaction costs by requiring little help from the support system, sending error free messages, quickly interpreting diagnostics, and so forth.

In addition to user experience with a DSS, psychological differences and user experience with other computer-based systems affect user preferences and/or the impact of message content and form for both the input [1] and output [21,28] interfaces. In the next section, we present a framework that will facilitate the development of adaptive DSS interfaces.

## 4. A Framework for Adaptive Interface Design

It is becoming increasingly evident, that, for a particular task, ‘friendly’ interfaces are based upon ‘real world’ metaphors that are familiar to the user $[12,22,23]$ . For example, ‘friendly’ systems supporting office functions provide an interface that allows the user to view system functions as objects from the office environment (such as, a calculator, a calendar, waste basket, reference manuals, file folders, etc.) and use them as they would use corresponding objects in the office $[4]$ . DSS interface design can be improved by basing the design upon an appropriate real world metaphor. We contend that the appropriate metaphor for DSS interface design is a human support system, in that it will reduce support system knowledge requirements and make it easy to send meaningful messages. This approach is similar in spirit to the dialog partner model discussed by $[26]$ .

Consider a simple human decision support system (HDSS) consisting of a manager (user) and subordinates (support system). Each subordinate has certain knowledge (domain knowledge) that the manager may require during the decision making process. The manager uses knowledge about the problem domain and knowledge about a subordinate's domain knowledge and LS to determine how information is to be requested. A subordinate, on the other hand, uses knowledge about the manager (e.g., PS) and the problem being worked upon to interpret a manager's requests. Clearly, the relationship $LS_{subordinate} \cap PS_{manager} \neq \emptyset$ must be true.

For example, a subordinate will interpret a manager's request for 'year-end figures', as 'yearend production figures,' because a previous request required 'mid-year production figures.' Similarly, a subordinate will provide comparative sales data in the form of bar graphs (although it was not requested in that form), because, in the past, the manager has requested it in that form. In such an environment, the input interface is greatly simplified, because the support system uses knowledge about the user and the user's current problem, to interpret requests and present results. Similarly, the human support system will use self knowledge (i.e., knowledge about its own capabilities) to help the manager receive desired support.

Thus, in a HDSS environment, the subordinate uses problem domain knowledge, knowledge about the manager, and self-knowledge, to provide a friendly interface. By using these three types of knowledge, a HDSS provides an input interface that: (1) reduces support system knowledge requirements, (2) reduces message content requirements for a meaningful message, and (3) provides a form that makes it easy to send a message. Similarly, a HDSS presents an output interface that provides: (1) friendly help systems to aid users in determining message content requirements and to help in the correction of erroneous messages, thereby reducing support system knowledge requirements, and (2) responses to messages that are context and user specific, without requiring explicit specification via the input message, thereby reducing message content requirements.

Metaphorically, the objectives of DSS interface design can be met by having the computerized support system (i.e., DSS) maintain knowledge about the user, as well as knowledge about itself, in addition to domain knowledge. A framework for DSS interface design based upon a human support system metaphor is shown in fig. 5. This framework suggests that DSS interfaces can be improved if the KS in a DSS contains the same categories of knowledge that the user possesses. In addition to problem domain knowledge, the DSS should include two other types of knowledge: (1) user knowledge, and (2) self knowledge. Further, the PPS must be capable of using all three types of knowledge in order to be able to adapt itself. By maintaining these two additional types of knowledge, the DSS interface can be adapted to meet the needs of both experienced and novice users. In addition, it has a potential for adjusting to accommodate user preferences. In the next section, we elaborate on these two types of knowledge and indicate how the PPS can use this knowledge to provide an easy-to-use interface.

![](/api/attachments/XPCCQHZH/fulltext/images/d1481ca6f156b315b1b288729ff57038bc2c9631e8ad77354b64aabf4bb763e2.jpg)  
Fig. 5. A framework for adaptive interface design.

## 5. The DSS Knowledge System

The content and processing of problem domain knowledge is described by Bonczek et al. [7] and will not be discussed here. This discussion will be restricted to user knowledge and self-knowledge. Moreover, the trivariate knowledge taxonomy introduced here in no way conflicts with the functional taxonomy that has been used as a basis for designing integrated and artificially intelligent DSSs [16]. In fact the two taxonomies appear to be orthogonal. That is, for each of the user, self, and domain knowledge categories, it should be possible to distinguish and consider descriptive, procedural, presentation, linguistic, reasoning and other functional types of knowledge.

## 5.1. User Knowledge

As indicated in fig. 5, users of a DSS possess three types of knowledge: (1) problem domain knowledge, (2) support system knowledge, and (3) self-knowledge. A user uses this knowledge to interact with the DSS in the course of making decisions. In a HDSS context, the human support person stores knowledge about the problem the user (i.e., manager) is working on, knowledge about the user's knowledge of the support system, and knowledge about user preferences. The PPS in a HDSS uses this knowledge to interpret messages and determine an appropriate response as well as its form of presentation. Consequently, user knowledge in the KS should contain three types of knowledge: (1) knowledge related to the problem the user is working on $(\mathbf{K}_{\mathbb{P}})$ , (2) knowledge about the user's knowledge of the support system $(\mathbf{K}_{\mathsf{UKS}})$ , and (3) knowledge about user preferences $(\mathbf{K}_{\mathsf{UP}})$ .

$K_{P}$ should contain knowledge related to the specific decision problems being faced by the user. Thus, $K_{P}$ might consist of knowledge that is descriptive (e.g., stored as text or as records in a database), procedural (e.g., represented as programs or spreadsheets in a model base), for reasoning (e.g., stored as rule sets in a rule base), for presentation (e.g., stored as forms or templates), linguistic (e.g., represented as vocabularies, macros, or grammars), and so on. The existence of such knowledge in $K_{P}$ means that a user need not replicate it in messages that are sent. Instead, the user may refer to it explicitly, implicitly, or perhaps not at all. Thus, message content requirements can be reduced. Furthermore, messages to the support system will be similar to those sent in a HDSS, since they will be interpreted within the context of previous messages. For instance, the procedural portion of $K_{P}$ can have knowledge about sequences of tasks that a user generally performs, allowing the user to execute these sequences with minimum interaction effort (i.e., reducing message content requirements).

Reducing message content requirements in current systems is often achieved by its use of defaults and macros. Defaults in most current systems are 'static,' and are often set by the designers of DSS and system software, while macros generally are the responsibility of the user or DSS developer. While defaults often can be changed by the user, doing so requires additional support system knowledge. In a HDSS, however, defaults are dynamic in the sense that a human support person interprets messages in the context of previous messages, as discussed earlier. Thus, in a human decision system, the equivalent of macros are created dynamically by the human support system and their use is observed in message requests such as, 'do the same thing using these new figures.'

There are two categories of knowledge about the support system that a user possesses: (1) knowledge about the contents of the KS (i.e., the problem domain), and (2) knowledge pertaining to the use of the DSS's capabilities. Thus, $K_{UKS}$ should contain knowledge about user expertise in using different knowledge management capabilities provided by the DSS's PPS (e.g., data management, spreadsheet analysis, rule set consultation, program execution). It should also contain knowledge about a user's familiarity with $K_{P}$ contents. This knowledge, together with self knowledge (discussed later), can be used by the DSS to help the user work with a DSS's domain knowledge.

$K_{UKS}$ can be used by the PPS to provide an appropriate message form for user messages and to provide intelligent help to users, thereby reducing both message sending and support system knowledge acquisition costs. Most current systems provide a single message form for users to send messages to the system, while systems that provide multiple message forms, have a single default form for users. While a single message form (e.g., question and answer) may be appropriate for a few users of a system, it may prove frustrating for other users of the system. $K_{UKS}$ can be used to tailor the message form of an interface to the individual user. Help systems can vary widely, from detailed tutorial-like explanations, to brief descriptions that aid recall. Help should be provided based upon user expertise and need [24]. $K_{UKS}$ can be used to customize help to the individual needs of users.

$K_{UP}$ should contain knowledge about user preferences for DSS output as well as user preferences for sending messages. $K_{UP}$ can be used by the PPS to reduce message content requirements and to provide an appropriate message form. Most current systems require the user to choose the form used for message responses, such as tables, pre-defined reports, graphs, etc. For a given task context, individual users may have preferences for one form of output over another. By recording user choices, future DSS messages can be presented in light of $K_{P}$ without requiring users to specify the chosen form each time a request is received, thereby reducing message content requirements. Also, the message form provided for user messages can be user specific, providing one user with a question and answer format, while another user is allowed to use commands.

## 5.2. Self-Knowledge

In a HDSS, the decision support system possesses knowledge about itself (i.e., it knows what it knows). We refer to this knowledge as self-knowledge. Self-knowledge ( $K_{S}$ ) in a HDSS is used to interpret messages and to help the user obtain knowledge relevant to the problem. In a computer context, data dictionaries and model directories are forms of system self-knowledge. Currently, however, these forms of self-knowledge are viewed and designed with the technical user in mind. For example, this knowledge may be available via the use of software external to the DSS, such as through the operating system. Consequently, although it could be used to improve the user interface, this knowledge seldom is available for such a purpose.

Access to self-knowledge is extremely important for adaptive interface design. It would enable the PPS to know what knowledge is available so that appropriate help and suggestions can be provided to the user. For example, if a user of a DBMS references a piece of data that does not exist, the interface could provide a list of the available data from which the user can choose. In the case of a model base, access to semantic knowledge pertaining to existing models would be useful.

## 6. Conclusion

It is widely recognized that DSS use is interactive. However, the best known models that have guided DSS development and research tend not to address interaction explicitly and in detail. Consequently, research on and development of the DSS interface has not kept up with the other aspects of a DSS, such as the model base, the data base, the problem processing system, etc. In this paper we have presented framework to facilitate the understanding and development of adaptive, easy-to-use interfaces. This framework is based upon a human support system metaphor and specifies the types of knowledge necessary to develop easy-to-use interfaces for DSSs. This framework explicitly recognizes the interactive nature of DSS use and draws upon a conceptual model of user-DSS interaction. In addition, we have indicated how the knowledge system and the problem processing system in a DSS will have to be augmented in order to provide friendlier interfaces.

Further research is needed to operationalize the management of a DSS's user knowledge and self-knowledge. Corresponding problem processor implementations need to be considered. It should be apparent from the discussion that there are relationships between the three types of knowledge that exist in the knowledge system used by the DSS's problem processing system. Formal specification of the three different types of knowledge and their relationships, as well as the capabilities that will be necessary in a DSS's PPS to provide adaptive interfaces, should be the subject of future research.

## References

[1] I. Benbasat, A.S. Dexter and P.S. Masulis, "An Experimental Study of the Human/Computer Interface," Communications of the ACM, Vol. 24, No. 11 (1981) 752–762.

[2] I. Benbasat and A.S. Dexter, "An Experimental Evaluation of Graphical and Color-Enhanced Information Presentation," Management Science, Vol. 31, No. 11 (1985) 1348–1364.

[3] J. Bennett, "User-Oriented Graphics, Systems for Decision Support in Unstructured Tasks," in: User-Oriented Design of Interactive Graphics Systems, S. Treu (ed.), New York: Association for Computing Machinery, 1977, 3-11.

[4] W.L. Bewley, T.L. Roberts, D. Schroit and W.L. Verplank, "Human Factors Testing in the Design of Xerox's "Star" Office Workstation," in: A. Janda (ed.), Human Factors in Computing Systems, New York: Association for Computing Machinery, 1983, 72–77.

[5] R.W. Blanning, “Conversing with Management Information Systems in Natural Language,” Communications of the ACM, Vol. 27, No. 3 (1984) 201–207.

[6] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, "Future Directions for Developing Decision Support Systems," Decision Sciences, Vol. 11, No. 4, (1980) 616–631.

[7] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[8] S.K. Card, T.P. Moran and A. Newell, The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1983.

[9] T. Carey, "User Differences in Interface Design," IEEE Computer, November (1982) 14–20.

[10] A. Chang, C.W. Holsapple, and A.B. Whinston, "A Decision Support System Theory," Working paper, Krannert Graduate School of Management, Purdue University, West Lafayette, IN, June 1988.

[11] B.L. Dos Santos, and M.L. Bariff, "A Study of User Interface Aids for Model-Oriented Decision Support Systems," Management Science, Vol. 34, No. 4 (1988) 441–468.

[12] R. Eberts, "Human Computer Interaction," in: Human Factors Psychology, P.A. Hancock (ed.), Elsevier Science Publishers, North-Holland, 1987.

[13] K. Efe, "A Proposed Solution to the Problem of Levels in Error-Message Generation," Communications of the ACM, Vol. 30, No. 11 (1987) 948–955.

[14] G.W. Furnas, T.K. Landauer, L.M. Gomez and S.T. Dumais, "The Vocabulary Problem in Human-System Communications," Communications of the ACM, Vol. 30, No. 11 (1987) 964–971.

[15] P.A. Hancock, (ed.), Human Factors Psychology, Elsevier Science Publishers, North-Holland Publishing Company, The Netherlands, 1987.

[16] C.W. Holsapple, and A.B. Whinston, The Information Jungle, Dow Jones-Irwin, Homewood, IL, 1988.

[17] C.W. Holsapple, S. Park, and A.B. Whinston, "Developing User Interfaces for Decision Support Systems," Working paper, Krannert Graduate School of Management, Purdue University, West Lafayette, IN, March 1988.

[18] R.C. Houghton, Jr., “Online Help Systems: A Conspectus,” Communications of the ACM, Vol. 27, No. 2 (1984) 126.

[19] E.L. Hutchins, J.D. Hollan and D.A. Norman, "Direct Manipulation Interfaces," in: User Centered System Design, D.A. Norman and S.W. Draper (eds.), Lawrence Erlbaum Associates, Hillsdale, New Jersey, 1986, 87-124.

[20] P.R. Innocent. “Towards Self-Adaptive Interface Systems.” International Journal of Man-Machine Studies, Vol. 16 (1982) 287–299.

[21] H.C. Lucas, Jr. and N.R. Nielson, "The Impact of the Mode of Information Presentation on Learning and Performance," Management Science, Vol. 26, No. 10 (1980) 982–993.

[22] F. Lustman, P. Mercier and L. Gratton, "A Dialog-Based Architecture for Interactive Information Systems," Data Base, Vol. 16, No. 3 (1985) 18–24.

[23] T.W. Malone, “How do People Organize their Desks: Implications for Designing Office Information Systems,” ACM Transactions on Office Information Systems, Vol. 1 (1983) 99–112.

[24] J.P. Moily, T.J. Murray and R. Agarwal, "A Preliminary Specification of an On-Line Expert Help System," Information and Management, Vol. 30, No. 4 (1987) 191–196.

[25] H. Mozeico, "A Human/Computer Interface to Accommodate User Learning Stages," Communications of the ACM, Vol. 25, No. 2 (1982) 100–104.

[26] H. Oberquelle, I. Kupka and S. Maass, "A View of Human-Machine Communication and Co-operation," International Journal of Man-Machine Studies, Vol. 19, No. 4 (1983) 309-333.

[27] M. Power, C. Lashley, P. Sanchez, and B. Shneiderman, "An Experimental Comparison of Tabular and Graphic Data Presentation," International Journal of Man-Machine Studies, Vol. 20 (1984) 545–566.

[28] W. Remus, "An Empirical Investigation of the Impact of Graphical and Tabular Data Presentations on Decision Making," Management Science, Vol. 30, No. 5 (1984) 533–542.

[29] B. Shneiderman, "Designing Computer System Messages," Communication of the ACM, Vol. 25, No. 9 (1982) 610–611.

[30] B. Shneiderman, Software Psychology, Winthrop, Cambridge, Massachusetts, 1980.

[31] B.M. Slator, M.P. Anderson, and W. Conley, "Pygmalion at the Interface," Communications of the ACM, Vol. 29, No. 7 (1986) 599–604.

[32] R.H. Sprague, and E.D. Carlson, Building Effective Decision Supports Systems, Prentice-Hall, Englewood Cliffs, New Jersey, 1982.

[33] A. Thesen, and D. Beringer, "Goodness-of-fit in the User/Computer Interface: A Hierarchical Control Framework Related to Friendliness," Working Paper, Department of Industrial Engineering, University of Wisconsin, Madison, Wisconsin, September 1984.
