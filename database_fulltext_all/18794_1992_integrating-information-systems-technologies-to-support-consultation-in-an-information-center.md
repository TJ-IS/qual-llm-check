---
otero_id: 18794
otero_key: "V4ZX5S5J"
title: "Integrating information systems technologies to support consultation in an information center"
authors: "Sudha Ram; Stephen Hayne; David Carlson"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90015-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Integrating information systems technologies to support consultation in an information center \*

Sudha Ram

University of Arizona, Tucson AZ, USA

Stephen Hayne

University of Calgary, Calgary Alta., Canada

David Carlson

University of Colorado, Boulder CO, USA

This paper presents an approach for integrating different types of information systems technologies to support the functions of an information center (IC). A knowledge-based system, information center expert/help service (ICE/H), has

![](/api/attachments/V4ZX5S5J/fulltext/images/b536019b460233b610465a26836148084c33ea653803c6850e93bcc64b6bf096.jpg)

Sudha Ram is Associate Professor of Management Information Systems at the University of Arizona. She received a B.S. degree in mathematics, physics and chemistry from the University of Madras in 1979, PGDM from the Indian Institute of Management, Calcutta in 1981 and a Ph.D. from the University of Illinois at Urbana-Champaign, in 1985. Dr. Ram has published more than 20 refereed articles in journals such as Communications of the ACM, IEEE Expert, and

IEEE Transactions on Knowledge and Data Engineering. Her research interests are in the areas of database and knowledge based systems. She is currently working on research projects funded by IBM, NCR, US ARMY, National Institute of Standards and Technology (NIST) and the Marketing Science Institute. Dr. Ram serves as a member of the editorial board of the Journal of Database Administration. She was the Guest-editor for the December 1991 issue of IEEE Computer on "Heterogeneous Distributed Database Systems". She is a member of ACM, IEEE Computer Society and TIMS.

Correspondence to: Dr. Sudha Ram, Department of Management Information Systems, College of Business and Public Administration, University of Arizona, Tucson, AZ 85721, USA.

\* This research was supported in part by grant WG-488116 from IBM, Gaithersburg, MD.

been developed to provide support for the help services of an IC. A general process model to represent the consultation process in an IC is described. Based on this model, an architecture has been developed to support the consultation process. The architecture depicts the use of a knowledge management system, a data management system and a communication (e-mail) system to emulate the consultation process. The ICE/H system has been implemented using this architecture to support an IC with 5000 users.

Keywords: Expert system; Knowledge base system; Database system; Information center; Knowledge representation; Consultation process; Electronic mail

![](/api/attachments/V4ZX5S5J/fulltext/images/a8d571376fd661c6a16eda0470a22b0d793eeab7913afa03a83cd08013cb2fe0.jpg)

Stephen Hayne is an assistant professor in the Faculty of Management at the University of Calgary. He holds a Ph.D. in MIS from the University of Arizona. Dr. Hayne's interests involve distributed database design, group support systems, knowledge-based technology and software engineering. Much of his research is rooted in the desire to use innovative technology to solve real business problems. To this end he has implemented and studied the use of tools in graphical environments which assist groups in communication and decision-making, e.g. shared drawing, group brainstorming, concurrent issue surfacing and consolidation. He is also applying this technology to support decision making during crisis situations.

![](/api/attachments/V4ZX5S5J/fulltext/images/6ed2520a1774c47ca74f61f38b55b4e562ce07fd94eb45fe0b20c79ee115660b.jpg)

David A. Carlson is assistant professor of information systems at the University of Colorado at Boulder. He got his Ph.D. in management information systems at the University of Arizona in 1991. His current research interests include: Mental models of strategic management, especially TQM; knowledge-based systems to support managers' mental models; and distributed knowledge-based systems.

## 1. Introduction

Information centers (ICs) are organized to provide help to end users of computing resources. Typically, ICs provide guidance in software and hardware selection and distribution. They also assist users in solving problems associated with the use of software and hardware. The rapid proliferation of personal computers and mainframe-based tools for end users has, however, created an unmanageable burden for many ICs. It has been demonstrated that providing knowledge based support for ICs can go a long way in easing this burden on IC consultants $[11]$ . Past research has focused on providing knowledge-based support for the software selection function of an IC $[22]$ . Our objective is to extend this research by considering the help services of an IC. Users approach the IC with specific problems related to the use of hardware and software; the IC consultants provide them with trouble shooting expertise. This is regarded as the most important function of an IC $[3]$ . We have attempted to integrate different types of information systems technologies to support this function. Specifically, this research demonstrates the use of knowledge and database management integrated with communications technology to support the consultation process.

## 2. Justification for ICE/H

The information center expert (ICE) project is an on-going effort in the MIS department at the University of Arizona. Its overall intent is to provide knowledge-based support for ICs. Over the past several years, an information center expert for software consultation (ICE/C) has been designed and prototyped $[11,17]$ . Our current research focuses on a general process model, architecture, and implementation of a system to provide knowledge-based support for IC help services (ICE/H).

ICE/H is unique among expert systems in several ways. First, it effectively demonstrates the integrated use of a knowledge management system, a database management system, and an electronic mail facility to provide several advantages. The general architecture separates the static knowledge – rules for guiding the problem diagnosis – from the dynamic knowledge, in the form of text for the solutions to be presented to the user. This approach maximizes the flexibility and maintainability of the system. Second, the system can be used simultaneously by a large number of users. Each receives an answer suitable at his/her level of understanding. Third, a feedback mechanism in the architecture guarantees that the user receives an answer to his/her problem. The system provides a facility that can forward users' comments to consultants via electronic mail as required. This feature illustrates the use of electronic mail to provide communication similar to that between a consultant and user. This capability also supports a semi-automatic evolution of the system in response to changes in user needs and computing environment of the organization. More specifically, it often allows the system to be modified without requiring the services of a knowledge engineer. Fourth, user consultations are captured by the system along with their comments. This provides the IC with data on the performance of ICE/H and information that can be used to plan future enhancements. Finally, the system captures the expertise of multiple experts. Most other expert systems have been built using one or two experts [4]. In addition, knowledge acquisition for ICE/H was achieved by using group support tools [20].

As stated earlier, the help service (help desk/technical support) provided by ICs is considered its most important function. IC consultants are expected to assist end-users in solving problems associated with the use of hardware and software. Typically, they receive a high volume of calls, most of which deal with routine and repetitive problems. The need to be ‘on call’ at all times prevents them from effectively managing their time. Most ICs experience a high turnover rate, because, as their expertise increases, the consultants are sought out and hired by functional departments. Thus the IC is frequently faced with the problem of hiring and training new personnel. In many cases, it is very difficult to attract senior experts.

![](/api/attachments/V4ZX5S5J/fulltext/images/a61df5cba3ac118d4789f17196cb732f05d3196f02f15d4681577b1dafbc7e8e.jpg)  
Fig. 1. General consultation process.

An expert system can enhance the effectiveness of an IC in several ways. Routine questions are addressed by the system with minimal participation required by the staff. Unlike a consultant, the system is also available at all times. End users get immediate solutions to their problems, rather than waiting for a consultant to return their call. End users are furnished with a single source for help $[21]$ . In addition, consistent advice is supplied by the system; problems caused by turnover are alleviated. It essentially captures and preserves expertise and thus serves to train new consultants. Moreover, the system leaves the IC consultants more time to spend on non-routine tasks and to provide training and other services to end users.

## 3. Consultation process model

In order to develop a knowledge based system to support the help services of an IC it is necessary to understand the consultation process. A typical scenario of the interaction between an end user and a consultant is (see Figure 1):

(1) a user telephones the IC help number;

(2) a general consultant answers and tries to diagnose the problem and provide an answer;

(3) during the conversation, the consultant prompts the user with questions to discover: (a) the general problem area, and

(b) the user's level of expertise within that area;

(4) if the problem is within the scope of the consultant's area of expertise, and is fairly simple, the consultant answers it right away;

(5) for more complicated problems, the consultant may refer to software manuals. In some cases, the consultant may even discuss alternative solutions with other consultants to suggest the most suitable alternative(s);

(6) if the problem is beyond the ability of the general consultant the user is referred to another who normally deals with such problems;

(7) in some cases, no solution is available. May be the user tried out several alternatives and none worked. In such cases, the consultant learns from the user feedback and attempts to formulate alternative solutions;

(8) in all cases, the user is given the answer in terms that (s)he understands. For novice users, the consultation process is involved, since the consultant asks more questions to diagnose the problem. With expert users, it is easier to identify the problem with fewer questions and a succinct answer usually suffices;

![](/api/attachments/V4ZX5S5J/fulltext/images/517ce17af2aa8396ecbed5bd023992246eeae381e9106df6151d130d3f11886d.jpg)  
Fig. 2. System consultation process.

(9) in all cases the consultant may give the user an answer over the telephone, visit the office for a hands-on demonstration or notify the user through electronic mail when a solution has been found.

A knowledge-based system that emulates the consultants and supports the process must address several aspects. First, it must support different styles of dialog based on its ability to identify the expertise level of the user. Second, the user's profile must be stored, to be retrieved for future consultations. Third, the heuristics used by a consultant for matching problems with solutions must be replicated. Solutions that are readily available from the consultant's mind or manuals need to be represented. The ability to identify situations when a problem is beyond the scope of the system should be possible. Lastly, the communication during different stages of the consultation process needs to be effectively duplicated. This should assist the system in learning when a solution is found to be ineffective or incorrect.

## 4. Integrated architecture for consultation

A general architecture must define the system components needed to support the process model. It utilizes a knowledge-based system to control the consultation. A database management system is integrated to improve the maintainability of the system and to record factual data, and an electronic mail system is used to provide the communication links within the process model. Figure 2 shows the system consultation process model.

Expert systems are generally composed of a knowledge base and an inference engine. The knowledge base may be further subdivided into the decision heuristics used by the expert (frequently rules) and the factual data. Knowledge provides the controlling and general information; typically complex and relatively small in volume. Data represents the manipulated and factual information; typically regular but voluminous [23].

Knowledge relates to the general aspects of the data, but knowledge should not vary rapidly over short periods of time. Knowledge bases excel at managing unstructured information. Databases excel in their ability to insert, update, retrieve and delete the relatively dynamic data. Thus, this architecture uses a knowledge base for the static rules used by experts to deal with situations within a domain, and a database to provide an efficient means of maintaining the dynamic portion, i.e., specific solutions to particular problems.

Zobaidie and Grimson [24] describe a variety of ways in which an expert system might interact with a database system. In an intelligent database the deductive component is embedded into the database management system. In an enhanced expert system the inference engine is provided with direct access to a generalized database. In inter-system communication, an expert system and a database management system co-exist with inter-communication between them. ICE/H is an example of an expert system using inter-system communication.

In our architecture, the communication link is bidirectional. The database stores the factual data which is accessed during inferencing. The expert system also updates these facts and inserts new entries into the database to store a profile of new users and to log the session results. This log is accessed by the knowledge base and used for feedback in future consultations.

The electronic mail communication links in the system consultation process model are unidirectional. Messages are generated by the knowledge base during a consultation with an end user. The database supplies e-mail addresses for the sender and receiver of the message. These are inserted onto the communication network for delivery to either the end user or to a consultant. No electronic mail messages are received by the knowledge base in this design.

## 4.1. Knowledge base

A classification scheme is used to organize the domain knowledge within the knowledge base and to co-ordinate the interaction of the knowledge and data bases. The problem diagnosis step of the consultation process model attempts to classify the user's question within this classifica-

![](/api/attachments/V4ZX5S5J/fulltext/images/f0c63d7d44bb4efef00534ab9ad174dd921fddb75032395376f5593dfd9e402f.jpg)  
Fig. 3. ICE/H classification tree (excerpt).

tion hierarchy. Figure 3 shows an excerpt of a classification tree for ICE/H. It satisfies the notion of a class hierarchy (lattice) and its inheritance of properties. The class hierarchy captures the IS-A relationship between a class and its subclass (equivalently, a class and its superclass).

![](/api/attachments/V4ZX5S5J/fulltext/images/deba1dbee7385dd65f506ccfdbc35a45793c0a24665fbdc70fd99e9dba60dd27.jpg)  
Fig. 4. Database model for the general architecture.

Subclasses of a class not only inherit all properties defined for the class, but can have additional properties defined locally. For conceptual simplicity, 'similar' objects (problem/solution pairs) are grouped together into a class. This class tree can also be viewed as a decision tree and, in order to reach a problem/solution leaf node, the tree must be traversed.

A classification tree for this architecture may be represented using any of the accepted knowledge representation models. An object-oriented programming language may be particularly suitable for implementing this representation. Since most expert system development shells utilize them, we use a rule representation in the following. Once the knowledge has been acquired and a representation is defined, a method for traversing the knowledge must be chosen. Since our objective is to determine a solution to the classified problem, a key into the database of solutions must be generated. Backward chaining is the most appropriate inference mechanism for resolving the goal of generating the database key.

The problem classification key used to access the solution database is in three parts: A category, a subcategory, and a keyword string. The category and subcategory provide a definitive structure for the top two levels of the classification tree. The keyword string is accumulated as the remaining nodes of the class tree are traversed. Thus, in Figure 3, we may have a category of 'PROFS', a subcategory of 'Mail', and a keyword string of 'Notes/Send/Other Systems'. When designing the dialog for classifying the user's problem within the hierarchy, a serious attempt should be made to minimize the number of questions that must be answered. Similar to the process model, the system should be designed to diagnose the user's general problem domain and then focus the consultation dialog with more detailed questions. The current implementation of ICE/H contains four categories and an average of six subcategories within each. Thus, two menu selections within the system dialog can eliminate most problem classes, and further dialog is conducted to construct a meaningful keyword string in a single subcategory. This separation of the category and subcategory from the keyword string facilitates the integration of the knowledge base with the database in the ICE/H architecture.

## 4.2. Data base

The database component of the general architecture stores facts which are accessed by the knowledge base. Figure 4 displays an entity-relationship diagram showing the primary elements of the database design. In this, keys are underlined and only important attributes for each entity are shown. The database relations support the consultation process. The problem class represents an abstract entity that relates many of the other entities in the design. The problem class in the database model has attributes in common with the top two levels of the classification structure in the knowledge base representation, providing a link for integrating the knowledge and data base components of the architecture.

Each user has a profile that is divided into two parts: Personal data and domain specific expertise at the subcategory level. An entity, person, represents the personal data for each user of the system. The personal data, along with system-generated information about the problem diagnosis, is sent by the system to a consultant if the user is not satisfied with a solution. A similar personal data profile is stored for each consultant providing an electronic mail ID for forwarding users' unresolved problems.

A consultant expertise profile is defined to relate each consultant with one (or more) problem class(es) of expertise. Each consultant is also assigned a priority to show those most proficient in a certain domain and availability to indicate whether that consultant is currently able to receive messages. Similarly, a user expertise profile is defined to store the level of expertise of each user, in a given problem class.

The problem /solution entity contains specific instances of solution text for the classification key: Category, subcategory, and keyword string. These solutions are retrieved during the consultation as the user's problem is diagnosed, and the text is presented to the user. The context-sensitive help entity supports descriptive information available on demand during a session. By storing this help text in the database rather than embedded in the knowledge-base rules, IC consultants are able to customize term descriptions which clarify the dialog questions.

The session log entity is used to capture information about each user's consultation session and his/her satisfaction with the system. This information includes:

\- starting and ending date/time (duration);

\- classification (database key) of the solution presented;

\- outcome of the session (selected from: ‘none of the above’, no solution, solution understood, solution not understood, previous solution not understood);

\- user's remarks, if not satisfied;

\- employee ID of the consultant receiving the message from a dissatisfied user;

\- user comments from the end-of-session questionnaire.

These data elements may be analyzed later to ascertain user satisfaction with the system, to determine the problem areas which generate the most help queries, and to identify areas that are missing or poorly covered. This capability is a unique and valuable feature of this architecture.

A database maintenance tool, independent from the consultation knowledge base, must be provided for the information center staff.

## 4.3. Communication

The system consultation process model has four communication links to fulfill a user's request for help. A link required by all expert systems is a human-computer interface to conduct a dialog with the user. However, when the expert system is implemented in a broad domain such as an IC, communication support should extend beyond the usual system dialog. For IC help services, such support might include: Providing a copy of the expert solution to the end user, forwarding a user's comments to a human consultant, and initiating communication directly between the end user and the human expert whenever the user's problem is beyond the scope of the expert system. The architecture accommodates these through electronic mail in the integrated system.

Invariably there will be questions for which the system has no acceptable answers: The question may be outside the scope of the system, or the solution may not be specific enough. Then, the expert system facilitates replies to unanswered questions and prompts the human experts to enhance the solution. The system prompts a dissatisfied user for comments. These remarks, along with any problem classification accomplished by the system, are forwarded to an ‘appropriate’ consultant. The problem classification is used to select a consultant from a database table that maintains a list of available consultants and their individual domains of expertise. This consultant receives an electronic mail message and replies via electronic mail, telephone, or in person and then uses the database maintenance tool to enter an improved solution into the database, or considers the unresolved problem for an extension of the knowledge base. For problems not within the domain of the system, knowledge engineers are required, since support for automated extension of the knowledge base is not included in this architecture.

If a user did not understand the solution presented, a more detailed solution may be selected and presented. For example, if a user was originally classified as intermediate, then solutions for a novice will be retrieved. This process of displaying solutions having successively less assumed expertise simulates the actual consultation. In addition, the ICE/H system tailors the dialog questions to the user's level of expertise; novices may be asked additional questions to clarify the diagnosis. If the user does not understand the most detailed solution that is available, then (s)he is asked to enter a textual description of the unresolved problem. This problem description, along with the classification database key determined by the system, is forwarded to a consultant who replies with a solution and, if necessary, modifies the solution in the database.

The message built by the system should be inserted seamlessly as though the user had used the electronic mail system directly and actually sent the message, which should contain the appropriate origin and destination address, header information, and message body text. The addresses of both sender and receiver are retrieved from the database of user and consultant profiles. By tagging the message with the return address, the consultant can then correspond directly with the user through the electronic mail system and bypass the expert system. A short subject header for the message, which depends on the outcome of the consultation, is inferred by the system. The electronic mail facility should support messages to remote nodes on the network.

## 5. Implementation of ICE/H

ICE/H is implemented on an IBM 4381 mainframe. The system was built using three components. ESE/VM, an expert system development shell based on EMYCIN, uses rule-based inferencing as the basis for its knowledge representation. The shell provides developers with editors for maintaining the knowledge base and an interface to external routines and to SQL/DS an IBM relational database management system. These two features allow electronic mail messages to be generated and sent by the system and provides convenient access to the facts in the database. The PROFS (IBM 1988) integrated office system was used to support electronic mail.

The domain knowledge is represented as a classification tree. ESE uses focus control blocks (FCBs) to direct the flow of control for a given consultation. The concept of FCBs is similar to the ‘hypothesis’ of NEOMYCIN [8]. The FCBs in ESE/VM allow the tasks to be organized into a hierarchy which allows a convenient representation of the class tree in ICE/H. One of the properties of an FCB is that parameter/rules above a certain FCB are visible to the lower level FCBs, but the FCBs higher in the hierarchy cannot access the parameters/rules of the lower level FCB. This inheritance property is useful for reducing the number of parameter/rules that need to be resolved, yet still allow access to all applicable parameters/rules of the particular class.

The architecture of ICE/H is shown in Figure 5. Our objective was to incorporate features which would allow much of the system to be maintained by the domain experts without the support of a trained knowledge engineer. The static rules are contained in an ESE/VM knowledge base and the dynamic elements are stored in a SQL/DS database. In addition, a semi-automated feedback mechanism is incorporated; this notifies the domain experts, via PROFS electronic mail, when an ICE/H user does not receive a satisfactory solution to his/her problem. This feedback mechanism is also activated when a user's question is beyond the scope of the ICE/H knowledge base.

ICE/H Architecture  
![](/api/attachments/V4ZX5S5J/fulltext/images/f9064ebf255bab08a91a5cf41fee80647a2b4daff6e0d53628ab72b2ad59d4f0.jpg)  
Fig. 5. ICE/H architecture.

## 5.1. ICE / H consultation process

The ICE/H system has been implemented to support the users as well as the consultants of an IC. The system serves to train new consultants in the IC. A typical consultation with ICE/H is as follows:

(1) The user links to ICE/H and initiates a help session.

(2) The user's profile is brought into the inferencing environment from SQL. If this is the first time that the user has accessed the system for this particular problem domain, his proficiency is gathered by the system and stored in the database. (3) Since the database contains all previous consultations, the user may view them and comment on their success or failure. These comments are logged and a message is forwarded to a consultant.

Table 1
Evolution of ICE/H

<table><tr><td>Feature</td><td>Prototype ONE</td><td>Prototype TWO</td><td>Prototype THREE</td></tr><tr><td>Domain categories</td><td>• PROFS</td><td>• Other domains included such as file transfers, application system, printing, etc.</td><td>• Same as TWO - some domains reclassified</td></tr><tr><td>Dialog for problem diagnosis</td><td>• Dialog tailored to type of user: Novice, intermediate, expert</td><td>• Same as ONE</td><td>• Reduced to two levels of expertise: Novice, expert</td></tr><tr><td>User profile</td><td>• Overall measure of user expertise from proficiency in use of hardware/software</td><td>• User expertise determined according to domain category</td><td>• Users allowed to move down level of expertise if solution not understood• User expertise determined according to domain category and subcategory</td></tr><tr><td>Consultant profile</td><td>• Only one consultant designated to receive all user feedback</td><td>• Different consultants for each problem area receiving feedback</td><td>• More sophisticated algorithm to choose consultant (based on priority and availability)</td></tr><tr><td>Feedback mechanism</td><td>• Feedback mailed to consultant only if solution not found</td><td>• Users given the option of mailing solutions to themselves• User feedback sent to consultants if solution not understood• Feedback solicited on most recent previous consultation</td><td>• Seamless integration with PROFS electronic mail facility• Feedback solicited on all previous consultations</td></tr><tr><td>Miscellaneous</td><td>-</td><td>• Multiple consultations during the same session• Context-sensitive help built into knowledge base</td><td>• Complete record of consultations captured• Context-sensitive help enhanced by incorporating help text into database• Feedback on overall system solicited</td></tr></table>

(4) The system directs the dialog with the user to diagnose and classify the problem.

(5) A key to the solution database is generated and a query is made. If a solution is not found, the dialog is captured along with the user's textual description of the problem and forwarded to a consultant. Information on the domain of each consultant's expertise is maintained. This is used to select the appropriate consultant when forwarding the message.

(6) Solution(s) found are passed back to the inferencing environment for display to the user. If the user is not satisfied, (s)he may examine a solution appropriate for a lower level of expertise (the expanded text may address the dissatisfaction) or (s)he may send a message to a consultant. (7) The user exits the system. either satisfied with the solution, or awaiting the response of the consultant.

(8) When a consultant receives a message describing an unsolved problem or an unsatisfactory solution, (s)he replies (via electronic mail, phone or in person) and then updates the solution in the database by using the maintenance tool. This ensures that a current and understandable solution is returned whenever the same problem is encountered again. It also ensures that a user with an unresolved problem gets through to a consultant. The user and consultant may continue their dialogue through the electronic mail system.

The ICE/H prototype is being tested at an IC help desk which supports a base of 5000 end users, receives approximately 3000 calls per month, and is staffed by twelve consultants.

## 5.2. Prototype development process

A prototyping process $[2,15]$ was used to establish the detailed requirements and to validate and improve the knowledge-base rules and database solutions. In addition to the typical benefits derived from developing system prototypes (user interface design, clarification of original design requirements, etc.), we were able to define several of the architectural features.

A group decision support (GDSS) environment was used to assist in the process. Initially, it helped in determining the scope of the system and in eliciting the process model for consultation. This was then emulated using stepwise refinement. Three prototype systems were developed prior to the final implementation. Table 1 traces the evolution of these. The first column of the table represents the main features in the consultation process, such as problem diagnosis approach, the domain covered by each prototype, etc. The first was developed primarily to illustrate the architecture of the system and did not support all features. During the development, existing features were modified to incorporate the process model or new features were added to replicate the consultation process model. Most of the enhancements were essentially to incorporate different types of feedback. These features were aimed at building a semi-automatic learning feature. The final prototype incorporated all the types of feedback mechanisms using electronic mail.

Since ICE/H was designed for both end users and IC consultants, feedback from both sets of users was required during prototyping. The GDSS tools were particularly useful in resolving conflicts among the various users. For instance, one major issue causing conflict was the number of levels of expertise to be addressed by the system. This issue was resolved amicably using issue consolidation and voting tools $[1]$ . A permanent record of feedback was easily obtained using these tools; this further assisted development during the feedback process.

## 5.3. Knowledge acquisition

Most expert systems reflect the knowledge of one or, at most, a few experts. Even when several experts are used, one of them is usually the primary contributor, who resolves any conflicts that arise during knowledge acquisition $[9,19]$ . However, this approach is not suitable for developing a system such as ICE/H. The breadth of knowledge required by IC consultants presents a difficult problem in designing and maintaining a knowledge-based support tool. When an end user queries the IC help desk, she expects this single contact point to lead to a solution to her problem. But no single human expert possesses all of the knowledge required to answer the full range of end user problems. In practice, an individual with broad, but shallow, knowledge would answer the routine questions and forward more specialized questions to an expert. A knowledge-based system for an IC help desk, therefore, must represent knowledge from multiple experts.

Our current implementation of ICE/H utilized approximately 12 experts who were all located at one site in the organization. However, it is possible that the experts could be scattered nation wide. Acquiring knowledge from multiple experts involves the issue of interpreting alternative points of view and varying methods for problem solving. Chorafas [7] recommends using group discussions as one way to approach this issue. Since knowledge acquisition consumes approximately 50% of the total development time, efforts were made to facilitate this process. Accordingly, we used several GDSS tools to conduct the knowledge acquisition. The details of this process are summarized in another paper [20].

By using these tools, experts were able to work simultaneously, adding to each others comments while considering others' points of view. The major contribution of the GDSS tools was the reduction in total time taken for the entire process and the ease of conflict resolution.

## 6. Validation

Expert systems are evaluated primarily to test for program accuracy, completeness, and utility $[10,18]$ . Evaluations by domain experts help to determine the accuracy of the embedded knowledge and the accuracy of any advice or conclusions that the system provides. These experts can also determine the boundaries of system knowledge. Evaluations by users help to determine the utility of the system: Whether it produces useful results, the extent of its capabilities, its ease of interaction, the intelligibility and credibility of its results, and its speed, efficiency and reliability.

## 6.1. Knowledge accuracy

Both static and dynamic evaluations were performed by the experts:

\- Static evaluation. Each consultant was given a copy of all solutions in the database, along with a description of the path followed to reach the solution. By reviewing this information, the consultant was able to identify and correct inconsistent or incomplete solutions within his/her area of expertise.

\- Dynamic evaluation. Each consultant was required to travel down every single path of the decision tree. This allowed him to compare the system's line of reasoning with his own. Each consultant was also asked to use a number of 'real' cases to test the system. Suggestions were solicited to improve the knowledge base and the decision tree. These suggestions were gathered during the feedback sessions conducted in conjunction with the knowledge acquisition. A gripe facility was made available to the consultants. This allowed the comments from the consultants to be forwarded directly to the system designers via e-mail.

## 6.2. Problem domain completeness

Even though the scope of each problem category had been specified in the first knowledge acquisition session, it was necessary to ensure that the problems did indeed cover all problems within each category. Testing for this type of completeness of the problem domain is difficult. One method is to build a flow chart displaying the sequence of each condition and consequence. This method was followed in ICE/H.

## 6.3. System utility

We are currently in the process of validating the system more thoroughly. At the end of every consultation, users are required to fill out an electronic questionnaire. This information is included in the session log. Preliminary analysis has shown that users are satisfied with the automated consultation process. It also appears that users receive solutions to their problems in less time. This may be due to the fact that there is no “telephone tag”. Informal feedback from consultants indicates that they are less interrupt driven; they prefer electronic mail to the telephone.

## 7. Discussion and future research

We have justified the need for a knowledge based system to support the help services of an information center and discussed a general process model and generic architecture for such a system with a prototype that implements this model. We have demonstrated the use of an integrated environment to support one of the most important functions of an IC, i.e., help services. The system has been designed to provide maximum flexibility and to support the changing needs of end users and the IC. The development of the system followed the standard prototyping approach, however, the process was facilitated by using a group decision support environment.

Unlike most knowledge based systems, ICE/H captures the knowledge from more than ten experts. The static portion of this knowledge has been separated from the dynamic portion by integrating the knowledge base with a database systems. This allows for easy modification without the services of a trained knowledge engineer. Unlike the earlier ICE/C system, a relational database management system (DBMS) supports the representation of the dynamic knowledge. This enables ICE/H to be used simultaneously by multiple users. Issues of concurrency and recovery are managed by the DBMS. Use of a DBMS also allows context sensitive help to be provided to the user whenever required, tailored to the user's level of expertise. The DBMS allows logging of all user consultations, providing statistics and descriptive feedback on the usage of the system.

Most important of all, the system has effectively captured the communication process between the consultant and user using electronic mail. ICE/H also uses this facility to incorporate a semi-automatic learning feature by means of the immediate feedback to IC consultants regarding solutions. Although the system cannot automatically update solutions, it triggers the consultants to do so.

## 7.1. Distributed ICE / H

Frequently, organizations are forced to operate multiple IC facilities each with its own set of consultants to provide help service for different offices, branches, or regions. This support can now be provided by means of a system such as ICE/H implemented in a distributed environment. The system could be divided into a number of subsystems, each operating at one or more sites connected together by means of a communication network.

Issues that need to be addressed in such a design include techniques to integrate independent knowledge bases. While the issue of integrating independent databases has been examined in great detail in the past [6] integration of knowledge bases is currently being studied [5]. By developing a distributed ICE/H system, users from any site in an organization could be supported with little or no incremental cost. The system would automatically refer to the appropriate knowledge base after conducting a preliminary consultation with the user. The individual knowledge base would then be used to solve the user's problem, ensuring location transparency to the end user. Further, by integrating individual knowledge-based systems, we can achieve synergy in solving a problem that no single system can solve. Typically, smaller systems can be built faster and more easily and integrated to solve problems that are out of the scope of any one system. Such 'teamwork' is also followed by human IC consultants when they are faced with a complicated problem. In many cases, one expert is able to understand and solve a problem partially, and often refers the user to one or more other consultants for clarification.

The distributed approach can also be used to integrate the knowledge base system for software and hardware recommendation with ICE/H.

## 7.2. Brittleness of ICE / H

Most of today's knowledge-based systems cannot determine if the problems they are trying to solve are outside the scope of their expertise. This is referred to as the brittleness problem [16]. In addition, systems expect that the inputs are in a tightly defined environment and changes in syntax etc. can cause problems. Currently, most of the burden of determining whether the problem is within the scope of the system is on the end user, who is provided with context sensitive help to assist in deciding if the problem can be addressed by the system. If the user decides it is not, feedback is obtained and forwarded to an appropriate consultant.

Humans IC consultants can often solve problems using common sense or analogy. An important extension would involve capturing “analogous knowledge” for a subset of non-routine problems. By building “analogical reasoning”, the problem solving scope of the system could be extended, thereby addressing the brittleness issue.

## 7.3. Object-oriented design for ICE / H

While it was possible to build the decision tree using the ESE expert system shell, a truly object-oriented expert system shell would allow the problem class to be mirrored directly in the class hierarchy. These domains could be treated as discrete objects, referencing others only as needed. To add a new domain into the classification tree, one would merely instantiate an existing class. This abstraction mechanism would help the knowledge engineer capture more generic knowledge with higher reusability.

Further, it is necessary to decouple the control logic (order of execution of profile retrieval, message generation, etc.) from the problem diagnosis. Declarative and procedural knowledge, as well as the structure of a target domain, could be easily organized around objects. This would facilitate the modularity, modifiability, and maintainability of the knowledge based system.

## References

[1] Applegate, L.M., B.R. Konsynski and J.F. Nunamaker, "A Group Decision Support System for Idea Generation and Issue Analysis in Organizational Planning", in: Proceedings of the Conference on Computer-Supported Cooperative Work, 1986, pp. 16–34.

[2] Boehm, B.W., T. Gray and T. Seewaldt, “Prototyping vs. Specifying: A Multiproject Experiment”, IEEE Transactions on Software Engineering, December 1984, pp. 473–484.

[3] Brancheau, J.C., D. Vogel and J.C. Wetherbe, “An Investigation of the Information Center from the User’s Perspective”, Data Base, Fall 1985, pp. 4–17.

[4] Buchanan, B., D. Barstow, R. Bechtel, J. Bennett, W. Clancey, C. Kulikowski, T. Mitchell and D. Waterman, "Constructing an Expert System", in: Building Experts Systems, Addison-Wesley, Reading, MA, 1983, pp. 127-167.

[5] Carlson, D. and S. Ram, “An Object-oriented Design for Distributed Knowledge Based Systems”, in: Proceedings of the 22nd Hawaii International Conference on System Sciences, Kona, HI, January 1989, pp. 55–64.

[6] Ceri, S. and G. Pelagatti, Distributed Database: Principles and Systems, McGraw-Hill, New York, NY, 1984.

[7] Chorafas, D.N., Applying Expert Systems in Business, McGraw-Hill, New York, NY, 1987.

[8] Clancey, W.J., “Heuristic Classification”, in: Knowledge-based Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1983, pp. 1–67.

[9] Gaines, B. and J. Boose, Knowledge Acquisition for Knowledge based Systems, volume 1. Academic Press, San Diego, Ca, 1988.

[10] Gaschnig, J., P. Klahr, H. Pople, E. Shortliffe and A. Terry, “Evaluation of Expert Systems: Issues and Case Studies”, in: Building Experts Systems, Addison-Wesley, Reading, MA, 1983, pp. 241–280.

[11] Heltne, M., A.S. Vinze, B.R. Konsynski and J.F. Nunamaker, “ICE: Information Center Expert, A Consultation System for Resource Allocation”, Database, Summer 1988, pp. 1–16.

[12] IBM, Professional Office System, Reference Manual, Program Number 5848–439, 1986.

[13] IBM, Expert System Development/Consultation Environment/VM, Reference Manual, Program Number 5798-RWQ, 1988.

[14] IBM, SQL/DS Database Management System, Reference Manual, Program Number 5998-RXQ, 1988.

[15] Lantz Kenneth E., The Prototyping Approach, Prentice Hall, New York, NY, 1984.

[16] Lenat, D., “Overcoming the Brittleness Bottleneck”, in: Proceedings of the Third IEEE Conference on Artificial Intelligence Applications, February 1987, pp. 64–72.

[17] Nunamaker, J.F., B.R. Konsynski, M. Chen, A. Vinze, Y.I.L. Chen and M. Heltne, “Knowledge-based Systems Support for Information Centers”, Journal of Management Information Systems, 5, 1, Summer 1988, pp. 6–24.

[18] O'Leary, D., "Methods of Validating Expert Systems", Interfaces, 18, 6, Nov-Dec 1988, pp. 72-79.

[19] Prerau, D.S., “Selection of an Appropriate Domain for an Expert System”, AI Magazine, 6, Summer 1985, pp. 26–30.

[20] Ram, S., J. Nunamaker, I. Liou, D. Carlson and S. Hayne, “Using Group Decision Support Systems for Knowledge Acquisition: An Information Center Application”, in: Proceedings of the 9th International Conference on Decision Support Systems, June 1989, pp. 87–102.

[21] Rockart, J.F. and L.S. Flannery, “The Management of End-User Computing”, Communications of the ACM, 26, 10, October 1983, pp. 776–784.

[22] Vinze, A., Knowledge Based Support for Software Selection in Information Centers: Design Criteria, Development Issues and Empirical Evaluation, PhD thesis, Department of MIS, University of Arizona, Tucson, AZ, 1988.

[23] Wiederhold, G. and J. Milton, A Precis of Research on Knowledge-Based Management Systems, Working Paper, Department of Computer Science, Stanford University, June 1987.

[24] Zobaidie, A. and J.B. Grimson, “Expert Systems and Database Systems: How Can They Serve Each Other?”, Expert Systems, 4, 1, February 1987, pp. 241–280.
