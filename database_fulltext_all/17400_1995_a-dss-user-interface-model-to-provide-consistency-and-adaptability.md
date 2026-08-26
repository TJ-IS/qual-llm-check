---
otero_id: 17400
otero_key: "JB9W3SX3"
title: "A DSS user interface model to provide consistency and adaptability"
authors: "Chetan S. Sankar; F. Nelson Ford; Michael Bauer"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0033-a"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A DSS user interface model to provide consistency and adaptability

Chetan S. Sankar \*, F. Nelson Ford and Michael Bauer

Department of Management, 415 West Magnolia Avenue, Auburn University, Auburn, AL 36849, USA

The cost of a DSS user interface can run as high as 60 to 70 percent of the total cost of building a DSS. It is important that the interface be adaptable to different users' needs and also communicate consistent commands to the internal components of the DSS. Many DSS interfaces have been developed to be either consistent or adaptable, but not both. A review of literature reveals that prior models of the DSS user interface are oriented largely toward programmers and systems designers rather than end-users. The focus has been on providing consistent, recognizable commands to the internal DSS components. However, another objective of a DSS is to respond to the unique requests of individual end-users and prior models are generally deficient in meeting this objective. We propose a DSS user interface model that provides an interface adaptable to the various styles and needs of different users yet consistent to internal DSS components. A precisioning procedure is suggested as the basis for implementing the proposed model. This procedure articulates user-adaptive terms and system-consistent terms to provide an interface with both adaptable and consistent characteristics. Two examples from a telecommunications DSS illustrate the utility of the proposed procedure.

Keywords: User interface; Decision support systems; Adaptability; Consistency; Model

![](/api/attachments/JB9W3SX3/fulltext/images/6f63846118aa56a30dab6661af5b73ced005cbb39f6e9c65dec9b597d717d995.jpg)

Chetan S. Sankar is an Associate Professor of MIS at the Auburn University's College of Business. He received his Ph.D. from the Wharton School, University of Pennsylvania in 1981. He has worked as an Assistant Professor at Temple University and as a Systems Engineer at AT&T-Bell Laboratories. His current research interests are user interfaces, global information technology management, and career progression of technologists and managers. He is a senior member of the IEEE and a member of TIMS, DSI, and IRMA. His papers have appeared in, among others, MIS Quarterly, Information Management Review, Management Science, IEEE Transactions on Professional Communications, IEEE Transactions on Engineering Management, Journal of Database Administration, and the Naval Logistics Quarterly. A paper he co-authored won the third place in the Society for Information Management 1990 Paper Award Competition.

## 1. Introduction

Until recently, the development of user interfaces for Decision Support Systems (DSSs) received relatively little attention [9]. For years, systems designers developed ad hoc user interfaces without the benefit of a formal framework for design. Rather, designers were more concerned with the programming of the internal architecture of the DSS. Much of the research on DSSs focused on data, procedures, rule sets, text, forms, and spreadsheets associated with the problem/decision area. Because of this focus the user interface was frequently ignored, resulting in interfaces difficult to learn and use. Indeed, Lustman, Mercier, and Gratton [27] found that many DSS user interfaces were rigid and difficult to use.

![](/api/attachments/JB9W3SX3/fulltext/images/dcc6aac594e55fe915d5cf9182844d36b1635cf6662b87974121b6a6fe10538d.jpg)

F. Nelson Ford is an Assistant Professor of Management Information Systems in the Department of Management at Auburn University. He received his Ph.D. from the University of Alabama and was on faculty at Murray State University before coming to Auburn. His teaching focus is at the graduate level in the areas of management of technology, expert systems (ES), and decision support systems (DSS). His primary research interests include ES, the integration of knowledge-based systems with other information systems (IS), DSS, and the management of IS technology. He has published in, among others, MIS Quarterly, the Journal of Management Information Systems, Information and Management, Interfaces, and Simulation.

![](/api/attachments/JB9W3SX3/fulltext/images/bbe387193eb80358d5b1e16cb118b08bc1596fcbc9e29783842f028f98eb3aed.jpg)

Michael J. Bauer is a computer programmer at Vanity Fair Mills in Monroeville, AL. He obtained his B.S. in accounting from the Pennsylvania State University and an M.B.A. with an emphasis in information systems from Auburn University. His research interests are in creating user-friendly information systems including decision support systems.

As DSS architectures have been refined and improved, researchers have realized the relationship between the user interface and the quality (i.e. usefulness and usability [2]) of the decision support system. A quality or friendly interface is simply one which is easy for the user to learn and to use. The user interface is the most expensive part of a DSS [2], [6], [29]. Costs of user interface can run as high as 60 to 70 percent of the total cost of building a DSS. In addition, much of the power, flexibility, and usability of a DSS are derived from the capabilities in the user interface ([41], [42]). Without a quality user interface the DSS may not support a manager's decisions. Poor quality user interfaces are a major reason why managers have not used computers and quantitative analysis to the extent that these technologies have been available [43].

Both consistency and adaptability are significant to enhancing the quality of the DSS user interface. It is important that the interface be adaptable to different users and be able to handle the various analytical tasks the DSS is designed to support $[41]$ . Simultaneously, the system needs to communicate consistent commands to the internals of the DSS so that the appropriate information is retrieved or the requested actions taken. A problem arises, however, when designers try to provide both adaptability in the interface and consistency in the internal commands.

## 2. Purpose of the paper

The purpose of this paper is to describe a DSS model that can provide an adaptable interface for the various users and, in parallel, consistency within the system. A current generic model for DSSs is described first and the need for consistency and adaptability in a DSS is established. Current models in use in User Interface Management Systems are then reviewed and their limitations are pointed out. A proposed DSS model is then described that can provide the user and the system the best of both adaptability and consistency. The functions to be performed by the modules of this model are then listed. A precisioning procedure is outlined that could implement the proposed model. Two examples illustrate the use of this procedure. After a discussion of the advantages and disadvantages of this procedure, future research issues are discussed.

## 3. A generic DSS model

The generic DSS model described here is taken from Dos Santos and Holsapple [9]. They depict a three-part DSS to fulfil the users' needs (see Figure 1): the user interface, problem processing system (PPS), and knowledge system (KS). The user interface is made up of the language system (LS) and the presentation system (PS). Together the LS and the PS facilitate communication between the user and the internals of a DSS. The internals of the DSS include the PPS and the KS.

Capturing users' requirements is important in developing an interface. Users are familiar with the system and with the problems or decisions being supported by the system [9], [40], [44]. The LS allows the user to communicate requests for action by the PPS. The options for the LS include command languages, menus, touch screens, mice, and voice input [40]. The internals of the DSS (PPS and KS) process the request for action and the PS displays the results of the analysis [9].

The PS and the LS together characterize and represent the user interface and influence substantially the quality of the DSS. Research on the LS has focused on what needs to be specified by the user to communicate effectively with the DSS and how it is specified. Research on the PS has helped users communicate with the DSS through help and diagnostic facilities and has produced improved outputs [9].

## A Generic DSS Model

![](/api/attachments/JB9W3SX3/fulltext/images/482f974b7c3c24a58dbe59ba91fd17cee792995d7cdff2eef1b56116d6d16dd9.jpg)  
Note: This figure is from "A Framework for Designing Adaptive DSS Interfaces" by B.L. Dos Santos and C.W. Holsappale, Decision Support Systems, 5(1), 1989, p. 3.  
Fig. 1. A generic DSS model.

As researchers change the focus of their efforts toward the DSS user interface, the importance of consistency throughout the system and adaptability toward the user has become important to the quality and success of LS and PS. In the following sections issues of consistency and adaptability are explained in greater detail.

## 3.1. Consistent DSS user interfaces

Consistency is the steadfast adherence to the same principles, course, or form. User interface consistency is the adherence to the same method of interaction between all potential users of a system or application and the computer system or application itself. Initial proponents of consistency ([23], [30]) emphasized internal consistency, i.e., consistency within the system. However, current directions by IBM, AT&T, and Apple [36] emphasize both internal and external consistency. The objective is to create standardized user interface software both within and across product lines, thereby creating a corporate user interface. The emphasis is on allowing end-users to use the same interaction concepts and techniques throughout many different applications and systems [24]. Such consistency of interaction concepts and techniques is helpful in providing the internal DSS with commands that the PPS and KS can recognize and process. However, to provide this consistency users are required to learn the specific language, icons or other conventions of the interface.

Methods of providing interface consistency can be categorized into two levels: (1) consistency between and within systems and (2) consistency within an application. Consistency between and within systems requires a user to be trained in a particular interface that is used throughout the corporation. For example, AT&T uses consistent commands to transmit and manage information between and within their operational support systems. Different computer based information systems within AT&T use the same user interface [11]. The advantage of a common user interface is that users do not have to learn a new interface when starting a new system and training users only once reduces costs [27]. Consistency within an application means that the same interface is provided for each user of a specific application. All use the same commands and the results are presented in the same format. Each individual user's experience, cognitive style, and other characteristics are not explicitly considered in designing the interface. Examples are the screens provided by popular microcomputer software such as Microsoft Windows, Lotus 1-2-3 and Wordperfect.

Although consistency is important, users may find it difficult to learn and use. A consistent interface may not allow users to complete a task or fulfil requirements as they would like. In a consistent system the command language of the interface is constant for all users and each application of the system. A user must be trained, formally or informally, in the command syntax of the LS/PS. Often the command languages are difficult to learn and use, and may not fulfil the needs of an individual user. A consistent interface also may impede performance of experienced and skilled users. An example is the problems a person well-versed in Wordperfect 5.1 faces when he/she migrates to Wordperfect 5.1 for Windows. Here, the user is forced to learn the new commands of Windows as a pre-condition for using Wordperfect 5.1. The introduction of another version of Windows might force the user to learn another version of the “consistent commands/icons.”

Developers of DSSs try to choose the most common terms to represent commands or actions, but these terms may not improve user friendliness or provide the flexibility needed in the DSS. Furnas, Landauer, Gomez, and Dumais [14] describe the ineffectiveness of choosing the most common term as the “vocabulary problem.” Users employ a variety of words to describe an action or an object. No single access word, however well chosen, can be expected to cover more than a small proportion of users’ attempts. These authors [14, p. 967] conclude, “Simply stated, the data tell us that there is no good access term for most objects. The idea of an ‘obvious,’ ‘self evident,’ or ‘natural’ term is a myth! Since even the best possible name is not very useful, it follows that there can exist no rules, guidelines or procedures for choosing a good name, in the sense of ‘accessible to the unfamiliar user’.”

Mapping the system architecture onto the user interface is very seductive, appealing to the designer's sense of consistency and simplicity [15]. The system architecture as defined by the PPS and the KS is external to the user and will not be familiar to many users. Grudin [15] argues that it is critical to centre the interface design on users and their tasks and not to impose the designer's sense of consistency on the user. The users of a consistent interface must adapt to the interface. The interface is static and cannot be adjusted to fit users' needs. A consistent interface may not provide the flexibility needed to satisfy the different users' cognitive styles, the users' experience levels, and the different decision approaches supported by the DSS. Thus, from the DSS end user's perspective, a consistent interface may not be an ideal user interface.

## 3.2. Adaptable DSS user interfaces

An adaptable user interface supports several different dialogue modes; allows the user to switch smoothly and naturally between dialogue modes at any time; and makes it easy for the user to learn the different dialogue modes [20].

In an adaptable interface, the inputs and outputs of a user's queries can be displayed on screen, printed in graphical or textual form, or perhaps even shown in full motion video. The choices presented in the PS and LS reflect the cognitive preferences of the user and the complexity of the task being performed [28]. In addition, familiarity with a system influences the user's preference for an interface [31]. Experienced users work better with a complex interface, but novices prefer a simple interface through which they can learn to use the system. The presentation format preferred may be influenced by the user's experience in a specific problem/decision area. Some users are experienced in some applications of the DSS but not in others. Because the cognitive styles of decision makers change with the type of task or decision being undertaken, different interfaces are preferred for different tasks [28].

Liang [26] suggests three ways to design an adaptive interface: 1) User-involved; 2) User-controlled; and 3) Self-adaptive.

According to Liang, in the user-involved design approach a single user helps the designer build an interface that will satisfy that user's needs. The system is designed to a specific user's experience level and cognitive style. The DSS is made flexible by adapting the system to the single user. Other users may find the system unfriendly and inflexible.

User-controlled interfaces give the users an opportunity to control the method of communication with the system (control of the LS), and the presentation of the results (control of the PS). Some methods to generate user-controlled interfaces are interface generation languages $[26]$ and programmable smart terminals $[18]$ .

A self-adaptive interface automatically adjusts to the users' preferences and tasks. In an example of a self-adaptive interface [26], the system compiles statistics about the types of inputs and outputs preferred by a user. Based on an analysis of these statistics, the interface documents the preferences of this user. These preferences are used to show subsequent inputs and outputs to that user. Such an adaptable interface could provide the flexibility needed for performing the tasks at the level of experience of each user.

However, adaptable user interfaces must be able to communicate the user's commands to the internals of the DSS (PPS and KS). It is important to convert the adaptable user's commands of the user interface into consistent internal commands that can be understood by the PPS and the KS. Most DSSs require that the internals of the DSS use consistent commands in order to retrieve the appropriate information, execute the appropriate model, etc.

The next section reviews the past efforts to model user interfaces and comments on their ability to address consistency and adaptability.

## 4. Past efforts to model user interfaces

Past literature on User Interface Management Systems (UIMSs) ([5], [7], [10], [17], [30], [34]) and DSSs ([21], [39]) proposed models through which the user interface can be separated from the PPS. Representative models from these are briefly reviewed in this section and their strengths and limitations are presented. Our focus is on the degree to which these models consider the unique requirements of the system user.

A working group on UIMSs [10, p. 51] reviewed many different prototypes currently in place to model user interfaces. Some working models that were compared by this group were prototypes such as IUICE, KHS, RAID, MO-SAIC, DICE, and PROMETHEUS. The group observed that these systems were able to separate user interfaces from the application systems, but were not customized for end-users since end-user opinions were not taken into account [10, p. 56]. Johnson, Drake, and Wilson [10, p.208] state that the UIMS prototypes do not ascertain whether the specified interface met the requirements of the users' tasks. They also state, "Apart from any limitations arising from their architecture, builders of UIMSs have discovered that their systems are not easy to use. The language based nature of many UIMSs is largely oriented toward programmers rather than human factors experts ..."

Task analysis methods have been used in the design of human-computer interactions. A Task-Action Grammar (TAG) [7] has been developed to model the mental representation of the interface language and to allow a formal specification of the language as perceived by the user. Another procedure called TAKD [7] has been used to analyze the data from the observation of relevant tasks and to redescribe them all within a single, consistent representational form. An acknowledged limitation of these procedures [7] is that they do not translate from the user- to system-centred representations easily. Easytalk is an example of a system that uses structured tools to translate a user's plain English requests to SQL. The SQL commands are used to navigate a database to find the most efficient response [25]. These methodologies work better when the users' requirements are well laid out using CASE and structured system design methods [7]. Many DSS users are executives and their queries are ad-hoc. As a result, they may find it difficult to use task analysis methods to structure their queries. Use of these methods may require employing a systems analyst to translate each query into structured languages.

An adaptive user interface was designed for an electronic mail system $[5]$ based on the Command Language Grammar notation $[21]$ . This grammar was found to be a useful interface design tool. Its main advantage was its ability to open up a system for scrutiny at a number of levels of abstraction. Nonetheless it was found to be lacking in a number of ways particular to the design of adaptive user interfaces $[5]$ . Especially, the language used was based on computer science concepts and did not translate into English well.

Jones [19] presented the concept of a Graph-Based Modelling System (GBMS) and discussed a prototype GBMS implementation which “facilitates the creation of computer graphics interfaces for models that can be represented as attributed graphs”[19, p.136]. A designer uses a GBMS component, the schema editor, to specify a class of attributed graphs. From this, the GBMS automatically generates a computer graphics interface which allows users to work with graphs of that class. Such an interface can provide significantly enhanced user performance [19]. However, the capabilities of the resulting interface are limited in modelling environments that can be represented by a graph.

Meador and Ness [21, p. 126] developed a DSS for financial planning called Projector. Its English-like dialogue concealed some complex tools, including multiple regression, exponential smoothing with trend and seasonal analysis, goal programming, and optimization algorithms. The user was pleased with this DSS, his time-effectiveness improved, and he enjoyed performing sensitivity analysis. His major complaints were that the interface was verbose and the terminal was noisy. Another DSS prototype, REGIMES [39] supports only two kinds of user interfaces – menu and query language – and is not designed to adapt to the individual needs of users.

These models in UIMSs and DSSs focus not on providing adaptability but on providing consistency in the user interface. These models, therefore, may be applicable in designing user interfaces for transaction processing or data processing systems. However, one objective of DSSs is to respond to the unique requests of an end-user and these models generally fall short of that objective. We propose a model in which the unique individual needs of end-users are modeled as a part of the DSS interface.

## 5. Proposed model

The proposed model allows an end-user to converse with the DSS using an adaptable interface and, in parallel, allows effective communication with the internal PPS and KS using consistent internal commands. This is accomplished by dividing each user interface component (LS and PS) into adaptive and consistent sections. The adaptive section adapts to the unique requirements of a user and the consistent section provides consistent commands to the internals of the DSS (Figure 2).

The model has two modules: an adaptive terminology module and a consistent terminology module. These are connected by an Adaptive/Consistent (A/C) Interface module (Figure 3). A user's dialogue with the system and the resulting presentation by the DSS is adapted to the unique characteristics of the user using the adaptive terminology module. The PPS and KS of the DSS are provided consistent terminologies by the consistent terminology module.

The appeal of this model lies in the complete separation of the unique interface of a user from the PPS and KS. The expected functions and features of each module are described next.

## 5.1. Adaptive terminology module:

This module is responsible for requesting the dialogue from the user in terms preferred by the user. It is also responsible for presenting output from the system to a user in a format comfortable to the user. From the user's point of view, the adaptive terminology module is responsible for clarifying the syntax and semantics of the words used by the system and the user. The expected features of this module are ([1], [5], [8], [16], [35]:

1. Ease of learning: This is frequently identified with user friendliness. It is accomplished when the interface is clear, displays conventions familiar to the user, and when the system is reliable and responsive. The way the system looks and works should be compatible with unique user conventions and expectations.

![](/api/attachments/JB9W3SX3/fulltext/images/47565be9cc0871d0aa2406adffb4ac9d01ea6aa9fffda3fbc844ddc719247801.jpg)  
Fig. 2. Proposed DSS model.

![](/api/attachments/JB9W3SX3/fulltext/images/44e9412fabe40f1ff613cd99529972ad7cfdc4be0719214c12ee0dc2eebacb23.jpg)  
Fig. 3. Generic description of proposed model.

2. Contextual adaptation: This allows users to gracefully navigate through tasks. Users should be given clear, informative feedback on where they are in the system, what actions they have taken, whether these actions have been successful, and what actions should be taken next. The way the system works should be clear to the user.

3. High level of guidance /feedback: This is determined by the adaptive system's predictions of required guidance. These predictions are made heuristically based on histories of user achievements and errors. Knowledge of similar systems may be identified when a user employs commands that would be appropriate to another system, thus leading to automatic acceptance of synonymous user commands and command structures.

4. User in Control: The user should feel in control of the system. Informative, easy-to-use and relevant guidance and support should be provided, both on the computer and in hard-copy form, to help the user understand and use the system. When help is provided, it should not become excessive, and should be provided in adequate formats corresponding to the user's level of expertise.

5. Support Unique Styles: It is critical to support different users with their own unique styles. Users vary in their expertise and could be classified as naive, competent, experienced, and expert [16]. An expert has a high level of experience and a high degree of comprehension of the system. An experienced person has high experience, but low comprehension of the system. A competent person has low experience, but high comprehension of the system. And a naive person has low experience and comprehension. For example, Apple Computers' Lisa provides two separate interfaces, one for office workers, and another for programmers. Since the purpose of DSSs is to support decision making of managers, it is critical that the user interface of the DSS support as many users as possible.

## 5.2. Consistent terminology module:

This module is responsible for providing requests to the PPS so that the terms are clear to the system. It is also responsible for obtaining responses from the system in terms that are clear and unambiguous. From the PPS's point of view, the consistent terminology module is responsible for providing instructions and obtaining responses in an unambiguous and clear manner across all users and applications. The expected features of this module are ([13], [33], [35], [36]):

1. Self Consistency: Similar actions within an application should lead to similar results. This is most readily achieved with a coherent internal model.

2. Consistency across applications: Similar consistent terms in different applications should lead to similar results. The syntax should consist of the same or analogous actions and the semantics should be similar.

3. Consistency over time: Applications should provide the same results for the same consistent queries over prior versions of the same application.

4. Consistency within and across platforms: The applications should be consistent with published user interface guidelines established for the hardware or system software platform. The responses of different applications across multiple platforms should be the same given the same consistent user query.

5. Consistent error information: The system should be designed to minimize the possibility of user error, with built-in facilities for detecting and handling those that do occur consistently. Users should be able to check their inputs and to correct errors, or potential error situations before the input is processed using similar consistent terms.

## 5.3. A / C interface module:

This module is responsible for converting the unique terminology of the user to consistent shared terms used by the PPS and KS. The A/C interface module helps end-users state requests in their own languages and translates them into consistent terms. The features of this module are ([3], [4], [22]):

1. Clarity: permit ambiguous statements from the end-user and help him/her to refine the statements.

2. Help: be interactive and easy to use.

3. Accommodate different input / output styles: use menus, graphs, form fill-in, or any other means suited to the user's preferences.

4. Support mathematical models: support quantitative questions and refine the user's queries to specific mathematical models and algorithms if needed.

5. End-user driven: support the end-user rather than the designer of the DSS.

6. Translate terms: be able to transform unique into consistent terms and vice versa. It is responsible for ensuring that the user's requests have been communicated accurately and the results match to the queries.

It is important to develop implementation procedures and prototypes based on this generic model so that the feasibility and technical validity of this model can be demonstrated. The implementation procedure is the subject of the next section.

## 6. Proposed precisioning procedure

A review of the literature did not reveal any procedures or prototypes that can be used to implement the proposed model. Therefore, a precisioning procedure was developed to implement the model. This procedure clarifies the terms used by the adaptive and consistent terminology modules. Executives have used this precisioning procedure to simplify the information presented in row and column reports and in describing job objectives ([32], [37]). The procedure clarified the words used to document statements of objectives, activities, and criteria. It was tested in a series of communications workshops with executives at JCPenney and Volvo. The results showed that the managers were better able to state their objectives after using the precisioning method. The success with these earlier experiments served as the justification to modify the procedure to precision the requests of DSS end-users. The modified procedure is still under development and is yet to be tested using actual DSS end-users.

This procedure precision the unique terms used in the adaptive terminology module to the consistent terms in the consistent terminology module based on the following steps:

(1) Syntactic Part: The system splits a user's DSS request into syntax headings.

(2) Semantic Part: Users interact with the system and identify synonymous terms under each heading and replace them with consistent terms.

They further clarify the terms. The system stores the preferences of the user (unique and consistent terms). It also helps the user identify synonymous terms.

(3) Refine Vocabulary: The system combines the preferred choices of the user in order to assemble the user's request in consistent terms.

Step 1 - Syntactic Part: The request of a user in a DSS is expressed as a query, menu selection, form fill-in or an icon in a user interface. The precisioning method categorizes this request using syntax headings of Verbs, Nouns, WH Questions/ Relations, and Remaining Words. These headings are chosen based upon the context and peculiarities of the system under study. When analyzing row-and-column forms, 11 headings were used [37], whereas 9 were used when analyzing objectives [32]. Since the analysis of DSS requests using this approach is at a preliminary state, only 4 syntax headings were chosen. The syntactic definitions of these headings are ([32], [37]):

Verb: denotes the important actions that indicate what to do.

Table 1
An example of using A/C interface module to clarify a query

<table><tr><td colspan="4">ORIGINAL QUERY OF A CIO: Generate a new route if high speed digital service fails.</td></tr><tr><td>VERB</td><td>NOUN</td><td>WHQUESTION/RELATION</td><td>REMAININGWORDS</td></tr><tr><td>ORIGINAL QUERY:</td><td></td><td></td><td></td></tr><tr><td rowspan="2">GENERATE</td><td>ROUTE</td><td rowspan="2">IF</td><td>A NEW</td></tr><tr><td>DIGITAL SERVICES</td><td>HIGH SPEED</td></tr><tr><td>FAIL.</td><td></td><td></td><td></td></tr><tr><td>CONSISTENT QUERY:</td><td></td><td></td><td></td></tr><tr><td rowspan="3">GENERATE USING</td><td>MODEL ABC</td><td rowspan="3">IF</td><td rowspan="2">ALTERNATE</td></tr><tr><td>ROUTES</td></tr><tr><td>DIGITAL SERVICES</td><td>ANY 1.54 MB/SAND ABOVE</td></tr><tr><td rowspan="2">FAIL</td><td></td><td></td><td rowspan="2">COMPLETELY</td></tr><tr><td>CUSTOMER XYZ.</td><td>FOR</td></tr></table>

CONSISTENT QUERY OF CIO: Generate using Model ABC alternate routes if any 1.54 Mb/s and above digital services fail completely for customer XYZ.

Noun: shows the subject or object on which the action is performed.

WH question and Relations: WH Question shows the need for response by the DSS using words such as what, where, when, what if, how, why. Relations include prepositions and conjunctions such as and, if, but, for, by.

Remaining words: shows the remaining words in the user's request.

As an example, Table 1 shows how a query of a Chief Information Officer can be clarified using this procedure. The Chief Information Officer (CIO) asks the telecommunications department to generate a new route if high speed digital services fail. He may be specifically referring to the cable cut that knocked out 1.54 mb/s and above digital services, causing blockage of 60 percent of AT&T's telephone traffic into and out of New York City and closing the Commodities Exchange market for a day [12]. The DSS has to understand and narrow the specific focus of the problem so that the request can be answered within a reasonable time. The top half of Table 1 splits this query into the syntax headings.

Step 2 - Semantic Part: After the user's request has been split into the syntax headings, the terms under each syntax heading are analyzed separately by the user and the system. This is when the semantic meanings of the terms are clarified and expanded. For example, as Table 1 shows, “generate” may mean “use a specific model ABC” to the CIO. The user’s term “a new” is changed to its consistent synonym “alternate” route by the system. When the CIO mentions “route,” the system will ask questions to clarify that the CIO wanted the results for routes with bandwidth above 1.54 mb/s. The term “fail” may mean a complete failure or partial failure of the routes. If the CIO wants to generate alternatives for partial failure, then the A/C interface module must broaden the solution range so that partial failures are monitored. Also the CIO has not clarified whether this request is for a specific customer (customer XYZ) or for all customers. As an end-user interacts with the A/C interface module to clarify the semantics, the unique and consistent terms used by this user are stored in a database for future retrieval.

Step 3 - Refine Vocabulary: Putting together all the chosen consistent terms, the unified query of this CIO reads, "Generate using model ABC alternate routes if any $1.54\mathrm{mb / s}$ and above digi tal services fail completely for customer XYZ." This query from the consistent terminology module is sent to the PPS and KS and an appropriate response from the DSS is obtained. The results of this request will be sent to the consistent terminology module.

Example of using A/C interface module to clarify the presentation required by a CIO

<table><tr><td colspan="4">ORIGINAL QUERY OF A CIO: Show the results using graphs.</td></tr><tr><td>VERB</td><td>NOUN</td><td>WHQUESTION/RELATION</td><td>REMAININGWORDS</td></tr><tr><td>ORIGINAL QUERY:</td><td></td><td></td><td></td></tr><tr><td>SHOW</td><td></td><td></td><td>THE</td></tr><tr><td></td><td>RESULTS</td><td></td><td></td></tr><tr><td>USING</td><td>GRAPHS.</td><td></td><td></td></tr><tr><td>CONSISTENT QUERY:</td><td></td><td></td><td></td></tr><tr><td>DISPLAY</td><td></td><td></td><td>THEALTERNATE</td></tr><tr><td></td><td>ROUTESCUSTOMERXYZ.</td><td>FOR</td><td></td></tr><tr><td>USE</td><td>SCHEMATICMAPS</td><td>SO THAT</td><td></td></tr><tr><td></td><td>ROUTESLOCATIONS</td><td>AND</td><td></td></tr><tr><td></td><td></td><td></td><td>ARECLEARLYVISIBLE.</td></tr></table>

CONSISTENT QUERY OF CIO: Display the alternate routes for customer XYZ. Use schematic maps so that routes and locations are clearly visible.

After the system develops a response, steps 1, 2, and 3 of the precisioning method are repeated so that the response is presented in an adaptable manner to the user. The A/C interface module may have information about the preferred presentation style of this CIO – whether the routes should be displayed in real maps drawn to scale, in schematic maps drawn so that locations and routes can be clearly seen, or in tables. The adaptive terminology module is responsible for presenting the results to the CIO. The A/C interface module performs the necessary conversions of the presentation from the consistent to the adaptive terminology module.

Table 2 precisions the unique request of the CIO, “Show the results using graphs.” The upper half of Table 2 shows how this request is syntactically split into the syntax headings. The semantic clarification of this request is shown in the bottom half of Table 2. The consistent term “display” has been used to substitute for the synonymous word “show.” The noun “results” was clarified when the CIO indicated that “the alternate routes for customer XYZ” is what should be displayed. The noun “graphs” was clarified to mean the consistent term “schematic maps.” The CIO further clarified that the schematic maps should be arranged so that the locations and the routes connecting them are clearly visible. Thus the unified request of the CIO reads, “Display the alternate routes for Customer XYZ. Use schematic maps so that routes and locations are clearly visible.”

## 7. Discussion and future research

These two examples show how the precisioning method clarifies syntactic and semantic ambiguities of the terms used by a CIO. The advantage of the precisioning method is that it is simple and can be understood by executives with minimal training time. The executives who used this method in other contexts ([32], [37], [38]) felt comfortable with the method and used it to clarify their requests. The procedure is easily adaptable to different contexts as the previous applications illustrate. The user controls the interactions with the A/C interface module and works with it to clarify his/her unique terms. Thus, the precisioning procedure is designed to support unique styles of users. The strength of the precisioning method is in providing good adaptive and A/C interface modules. The disadvantage of the precisioning method is that it supports the consistent terminology module to a lesser extent. In contrast, most of the prototypes in UIMS research and in industry have been developed from the applications side and therefore provide more support for consistent terminology modules. Hence, future research might investigate the use of the precisioning method as a front-end to existing UIMS prototypes and applications. In addition, its use in concert with artificial intelligence techniques in UIMS design may represent another fruitful research direction.

The precisioning procedure is under development and additional syntactic categories may be needed when it is tested with DSS end-users. The end-users should test the procedure using DSS queries, pull-down menus, icons, and other unique user interface techniques. Another research issue is to what degree it will be necessary to modify the precisioning procedure to handle these different user interface commands.

Extensive efforts are being made by companies such as AT&T, Apple, and Microsoft [36] to develop software to retrieve appropriate results from large internal databases given consistent commands and requests. Because the user interface is a major part of a DSS [2], it is critical that further research effort be focused on developing implementation prototypes of the proposed model. Without such implementations, the commands used in DSS interfaces will likely continue to be based on the DSS designers' terms and will not reflect the unique needs of end-users.

As prototypes are developed to implement the proposed model, it is important to develop measurable criteria to evaluate them. These criteria could be derived based on the expected features of the three modules. A related issue for future research is the operationalization of such criteria so that the results of testing different prototypes of similar DSS user interface models can be compared.

## 8. Conclusions

In the past providing both consistency and adaptability within a DSS has been considered to be in opposition. As consistency and adaptability are incorporated into a DSS, the quality and effectiveness of the system improves. Consistency can provide the internal system with commands that the PPS can understand, while adaptability can ensure that the system fits each user's cognitive style, experience, and specific problem objective. Many current models in UIMS focus on providing a consistent user interface. These models may be applicable in designing user interfaces for transaction processing or data processing systems. One objective of a DSS is to respond to the unique requests of an end-user and these models fail to consider that. That is where our model contributes to the field.

The proposed model focuses a DSS developer's task on generating adaptable user interfaces while at the same time providing consistent terms/commands to the PPS and KS. Implementing the proposed model could help make the DSS easy to use for any end-user. Thus, as the end-user gains more efficient and effective use of the system, the organization derives major strategic and operational benefits. In addition, the organization experiences more effective use of its resources as users share applications through better and easier interface to PPS and KS.

## References

[1] S.L. Alter, Decision Support Systems: Current Practices and Continuing Challenges, Addison-Wesley Publishing Company, Reading, MA, 1980.

[2] J.L. Bennett, Analysis and Design of the User Interface for Decision Support Systems, In Building Decision Support Systems, pp. 41–64, Edited by J.L. Bennett, Addison Wesley Publishing Company, Reading, MA, 1983.

[3] R.W. Blanning, The Functions of a Decision Support System, Information and Management, 2 (3), 1979.

[4] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, Inc., Orlando, FL, 1981.

[5] D.P. Browne, B.D. Sharratt and M.A. Norman, The Formal Specification of Adaptive User Interfaces Using Command Language Grammar, Human Factors in Computing Systems 1986 Conference Proceedings, The Association for Computing Machinery, NY, 1986.

[6] E.D. Carlson, Developing the User Interface for Decision Support Systems, In Building Decision Support Systems, pp. 65–88, Edited by J.L. Bennett. Addison-Wesley Publishing Company, Reading, MA, 1983.

[7] D. Diaper, Task Analysis for Human-Computer Interaction, Ellis Horwood Limited, Hartnolls, U.K., 1989.

[8] B.L. Dos Santos and M.L. Bariff, A Study of User Interface Aids For Model-Oriented Decision Support Systems, Management Science, 34(4), April 1988, pp. 461–468.

[9] B.L. Dos Santos and C.W. Holsapple, A Framework for Designing Adaptive DSS Interfaces, Decision Support Systems, 5(1), 1989, pp. 1–11.

[10] D.A. Duce, M.R. Gomes, F.R.A. Hopgood and J.R. Lee, Editors, User Interface Management and Design, Springer-Verlag, New York, NY, 1991.

[11] J.M. Farber, The AT&T User Interface Architecture, AT&T Technical Journal, 68(5), Sept/Oct. 1989, pp. 9–16.

[12] J. Foley, AT&T Cut Was Lesson Learned, Communications Week, Jan. 14, 1991, p. 35.

[13] D.M. Frohlich and P. Luff., Some Lessons From an Exercise in Specification, Human-Computer Interaction, 4(2), 1989, pp. 121–147.

[14] G.W. Furnas, T.K. Landauer, L.M. Gomez and S.T. Dumais, The Vocabulary Problem in Human-System Communication, Communications of the ACM, 30(11), Nov. 1987, pp. 964–971.

[15] J. Grudin, The Case Against User Interface Consistency, Communications of the ACM, 32(10), Oct. 1989, pp. 1164–1173.

[16] R. Hartson and D. Hix., Advances in Human-Computer Interaction, Ablex Publishing Corporation, Norwood, NJ, 1988.

[17] S.E. Hudson, UIMS Support for Direct Manipulation Interfaces, Computer Graphics, 21(2), 1987.

[18] P.R. Innocent, Towards Self-Adaptive Interfaces, International Journal of Man-Machine Studies, 16, 1982, pp. 287–299.

[19] C.V. Jones, An Introduction to Graph-Based Modeling Systems, Part I: An Overview, ORSA Journal on Computing, 2(2), Spring 1990, pp. 136–151.

[20] E. Kantorowitz and O. Sudarsky, The Adaptable User Interface, Communications of the ACM, 32(11), Nov. 1989, pp. 1352–1358.

[21] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[22] P.G.W. Keen and T.J. Gambino, Building a Decision Support System: The Mythical Man-Month Revisited, In Building Decision Support Systems, pp. 133–172. Edited by J.L. Bennett, Addison-Wesley Publishing Company, Reading, MA, 1983.

[23] W.A. Kellog, Conceptual Consistency in the User Interface: Effects on User Performance, in Proc. INTERACT'87 Conference on Human-Computer Interaction, Stuttgart, Sept. 1-4, 1987.

[24] I.H. Koritzinsky, New Ways to Consistent Interfaces, in Coordinating User Interfaces for Consistency, J. Nielsen, ed., Academic Press, Inc., San Diego, CA, 1989.

[25] D. Kull, Cutting through DBMS Complexity, Computer Decisions, April 1989.

[26] T. Liang, User Interface Design for Decision Support Systems: A Self Adaptive Approach, Information and Management, 12(4), April 1987, pp. 181–190.

[27] F. Lustman, P. Mercier and L. Gratton, A Dialogue-Based Architecture for Interactive Information Systems, Data Base, Spring 1985, pp. 18–24.

[28] R. Mann, H.J. Watson, P.H. Cheney and C.A. Gallagher, Accommodating Cognitive Style Through DSS Hardware and Software, Proceedings from the 19th Hawaii International Conference on Systems Sciences, 1986.

[29] R. Molich and J. Nielsen, Improving a Human-Computer Dialogue, Communications of the ACM, 33(3), March 1990, pp. 338–348.

[30] T.P. Moran, The Command Language Grammar: A Representation for the User Interface of Interactive Computer Systems, Int. J. Man-Machine Studies, 15, 1981, pp. 3–50

[31] H. Mozeico, A Human/Computer Interface to accommodate User Learning Stages, Communication of the ACM, 25(2), Feb. 1982, pp. 100–103.

[32] C. Newsom, Development of a Method for Improving Implementation Plans. Ph.D. Dissertation, The Wharton School, The University of Pennsylvania, Philadelphia, PA, 1985.

[33] J. Nielsen, Coordinating User Interfaces for Consistency, Academic Press, Inc., San Diego, CA, 1989.

[34] G.E. Pfaff, ed., User Interface Management Systems, Springer-Verlag, 1985.

[35] S. Ravden and G. Johnson, Evaluating Usability of Human-Computer Interfaces: A Practical Method, Ellis Horwood Limited, Chichester, U.K., 1989.

[36] D. Rosenburg, A Cost Benefit Analysis for Corporate User Interface Standards: What Price to Pay for Consistent “Look and Feel”?, in Coordinating User Interfaces for Consistency, J. Nielsen, ed., Academic Press, Inc., San Diego, CA, 1989.

[37] C.S. Sankar, Analysis of Names and Relationships among Data Elements, Management Science, 31(7), 1985, pp. 888–899.

[38] C.S. Sankar and N. Ford, The DSS User Interface Language: A Proposal, Proceedings, 1990 Decision Sciences Institute, pp. 330–332, November 1990.

[39] K.B.C. Saxena and M. Kaul, A Conceptual Architecture for DSS Generators, Information and Management, 10(1986), pp. 149–157.

[40] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly, 4(4), Dec. 1980.

[41] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, N.J., 1982.

[42] R.H. Sprague, Jr. and H.J. Watson, editors, Decision Support Systems: Putting Theory Into Practice, Prentice-Hall, Englewood Cliffs, N.J., 1986.

[43] E. Turban, Decision Support and Expert Systems: Management Support Systems, 2 ed., Macmillan Publishing Company, New York, 1990.

[44] H.J. Watson and R.H. Sprague Jr., The Components of an Architecture for a DSS, in Decision Support Systems: Putting Theory into Practice, pp. 107–117, edited by J.L. Bennett, Prentice-Hall, Englewood Cliffs, NJ, 1989.
