---
otero_id: 21285
otero_key: "5DH4JN4V"
title: "A visual, hierarchical approach to implementing rule-based algorithms in classification of discrete, homogenous objects"
authors: "Roy Martin Richards"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00077-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A visual, hierarchical approach to implementing rule-based algorithms in classification of discrete, homogenous objects

Roy Martin Richards Jr.

College of Business Administration, Belmont University, 1900 Belmont Boulevard, Nashville, TN 37212-3757, USA

Received 1 November 2002; accepted 1 April 2003 Available online 14 June 2003

## Abstract

This research examines the graphical approach to implementing an expert system instead of the programming approach of the traditional ‘‘if then/else’’ construct. The rule base and knowledge base are built into the graphical model and only observation on the part of the user is needed for effective discrimination among choices. The application model is designed around a relational database management system with the user interface generated in Visual Basic and a rule base implemented through a hierarchy of mutually exclusive options presented to the user based on choices made as the user progresses through the various decision levels.

Decision factors are based on observation of the discriminatory aspects of the objects to be classified as exhibited by the objects and maintained in the knowledge base. Human control is established through explanation and real-time recording and tracking of all choices made for any object under consideration <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Expert systems; Graphical interface; Rule-based algorithm; Knowledge base; Database; Visual programming; Usability; Control

The assignment of discrete but homogeneous alternative objects into predefined groups is a problem of major interest both in practice and research. Referred to as classification for nominal objects, methodologies addressing the issue have been developed in many disciplines including artificial intelligence and operations research. This paper addresses the issue of classification by presenting a DSS/ES methodology that utilizes relational database technology and visual presentation of choices with explanatory information about objects and classes in a relatively simple computer application so that the unsophisticated user can successfully apply decision criteria leading to accurate classification of objects, despite a fairly complex set of object attributes. Expertise is built into the model in the rule base, which is executed through the hierarchy of mutually exclusive alternatives presented in the visual interface.

The hardware environment used for this model is the Personal Computer based on the Intel chipset running Microsoft Windows as the operating system. The application software is based on Microsoft Access with Visual Basic for access to design and implement the user interface. This hardware/software combination allows a wide variety of potential applications in virtually any field in which classification processes are employed. The PC environment is scalable and should be challenged only by the most complex of classification applications.

To place the classification model in an application context, the example of a vehicle classification system is employed. Many types of organizations are faced with this type of classification problem in their day-today activities including rental agencies, insurers, and dealerships. Topics such a managerial decision making, decision support systems, expert systems, and establishing competitive advantage using technology are of interest in any field of endeavor [1,11]. In the example used here, the operation of a car show is used. Vehicles are categorized by type, usage, modifications, model year, and other criteria. Awards are given by category or classification as determined by the classification criteria. The process of classification is subject to interpretation and understanding of the rules as established by the organizing body. The system is an ideal candidate for the application of a DSS/ES methodology.

## 1. The problem at hand

Perhaps the most primitive way to approach classification of a large number of objects is the manual method. The person or persons assigned the classification task would be given a set of discrete objects with attributes that either distinguish them from one another or establish similarities that would lead to their being classified in the same category. The classifier would be given a set of rules based on the attributes for given classes and would, through observation, attempt to discriminate among the objects based on those rules and attributes. In a very simple case, one in which the objects are very similar and there are only few rules and classes, the task is not extremely problematic.

However, when the task increases in complexity with increasing numbers of dissimilar objects and a complex set of attributes and rules, the problem can become unmanageable for all, except the expert who knows the rules and understands their application in the set of objects. The task will expand by a factor of the number of objects multiplied by the increase in the number of classifications times the number of rules for each classification, a non-linear increase in complexity. At some point, additional manpower is needed and the knowledge and expertise of the expert must be imparted to the additional manpower in some way requiring learning within the organization [8].

It is highly inefficient to just provide the novice classifiers with a list of classifications and a rulebook in such complex situations because the learning curve to proficiency is very steep at high levels of complexity. The increased complexity can also lead to an increase in the error rate in the process. In such a scenario, information technology can be applied to enhance the productivity and accuracy of the classifiers [2]. The decision support system or expert system has typically been the vehicle employed to address the classification problem [4,5].

For classification systems exhibiting medium to high levels of complexity, the cost of the process including detecting and correcting errors can be high. Manpower costs and the ramifications of misclassification can cripple an entire organization, especially when rental rates or premiums are involved. Information technology expenses can be much lower than the costs associated with a manual, error-prone system. Hence, the IT solution is frequently attractive to organizations facing even modest levels of complexity in their operations. Application of IT can reduce those costs as long as a system can be acquired that provides an accurate, easy to use solution to the problem.

Typical approaches to implementing DSS/ES applications have included several alternatives [7]. One of the most common of these methodologies employs the ‘‘if/then/else’’ programming construct in which a list of questions concerning object attributes is posed to the user who then responds with answers that are then subjected to a rule base which provides the discriminatory parameters to the data, resulting in a suggested classification for the object. The logic construct for such an application, especially in a complex application, can be enormously problematic—for the user and especially for the coder. Complex branching in the logic construct is difficult to define, even with the use of development tools and maintenance of the programs after implementation may also suffer. It is important to realize that things change over time whether they are the rules for classification or the attributes of the classes themselves. In developing an alternative methodology, both code complexity in the initial application and maintenance as the application matures are of critical importance [14]. Fortunately, the RDBMS with a graphical interface provides an attractive alternative since the logic of classification can be built into the user interface and the data can be collected and maintained for the knowledge base. The methodology presented here utilizes this approach.

## 2. The graphical model

The model described here can best be categorized as an expert system as opposed to a decision support system because it is built around the five components comprising an expert system. Those components are: (1) a knowledge base containing facts and rules, (2) an inference engine to interpret the rules, (3) an explanation subsystem to explain the sequence of logical inferences, (4) a knowledge acquisition subsystem, and (5) a user interface [12]. The knowledge of an expert in the process is incorporated in the decision criteria of the system.

The knowledge base contains data attributable to individual objects in the object set and is used to distinguish among them according to the rules that are embedded in the inference engine. The inference engine, rather than being a series of ‘‘if/then/else’’ statements, is contained in the hierarchy of mutually exclusive choices in the graphical model. For example, upon making the observation that an object belongs in a given major category, all options for the other major categories are hidden from the user’s view, allowing further choices to be made only from the subcategories associated with the major category chosen. The hierarchical structure of the decision matrix is implemented in this way.

The explanation subsystem is vital for the effective use of the model by the relatively unsophisticated user. Explanation is an important component of any automated or semi-automated system [13]. When incorporating explanation use during user interaction, it is important to consider appropriate techniques for both novices and experienced professionals due to qualitative and quantitative differences in the nature and extent of explanation use [10]. However, use of explanations can result in improved performance, more positive user perceptions, and long-term learning [3,6].

The explanation component of the model used here is comprised of both pre-choice information in the form of ‘‘hover boxes’’ explaining options and a ‘‘running history’’ of choices made leading to the current options displayed. This technique provides the user with both pre-choice information and postchoice feedback about the selections made leading to the recommended classification.

The knowledge acquisition subsystem is handled by the database software through the use of forms and queries. Data can be entered and updated for the individual objects in addition to the ability to redefine category attributes on an ad hoc basis. Manipulation of the various screens is required for updates of the rule base.

The user interface component is implemented through a series of screens that are presented as the user moves through the decision tree structure. Graphics including icons, action buttons, and other VB techniques are provided to register choices and store permanent and transient data in the database transparently to the user. The end result of the process is a recommended classification which will be reviewed for accuracy by the expert after the user has completed the logic process. This makes much more efficient use of the expert than having him perform the lower-level functions now accomplished by the additional, nonexpert manpower.

## 3. Structure of the model

Conceptualization of the task of classifying various vehicle types according to object characteristics is structurable and, with decomposition and characterization of the task, is subject to a knowledge-based system application [2]. The task is decomposed into a hierarchy structure that is then translated into screens in the user interface with screen components representing task events. Fig. 1 shows the highest level in the decision structure as applied to the vehicle classification system.

![](/api/attachments/5DH4JN4V/fulltext/images/e1fd292c6ecb485b9cfd818be9b14638c3abe1a09cfb45008baa41c29d53f33d.jpg)  
Fig. 1. Level one—major classification breaks.

![](/api/attachments/5DH4JN4V/fulltext/images/f8cb0f9caef915d3c4cb3d44c52c4d145d67715da6e6edddc3b16fb73537fbc7.jpg)  
Fig. 2. Automobile class

The level one categories are then broken down into the next level of the model. Figs. 2–4 show how the next level is organized.

The categories at level 2 break down farther by several attributes including the number of modifications, type of modifications, model year, and others, giving up to eight levels of hierarchy per class. The entire structure is too large to include here but these examples show how the task was decomposed and structured for implementation.

## 4. Implementation of the model

The graphical representation of the hierarchical model presented above is readily translatable into a structured implementation model in which data are stored in MS Access and a VB interface is used to input choices among alternative attributes for determination of the proper classification. The screens generated follow closely the diagrams represented in Figs. 1– 4. For example, the level 1 diagram presented in Fig. 1 gives rise to this screen in the implementation model (Fig. 5).

In addition to the three buttons corresponding to the events, ‘‘vehicle is an automobile’’, ‘‘vehicle is a truck’’, and ‘‘vehicle is other’’, data describing attributes of the given vehicle are presented from the database describing the vehicle under consideration. These data are collected by observation during the process of acquiring supplemental data in module four of the expert system model using the knowledge acquisition subsystem at some point before the classification process begins and are verified by the user during classification. The information on ‘‘Last Year’s Classification’’ is included if the vehicle was in the show during the previous year and is used as a crosscheck for verification purposes. If this year’s recommended class varies from last year’s class, a flag is set to indicate that there is a difference. The user can then check the attributes to determine if the discrepancy is justified.

Also included in this screen is a hover box for the ‘‘Other’’ category describing the types of vehicles that are included in that category (Competition, Bike, Boat, Special Interest, Go-cart, Experimental). All buttons have hover boxes describing the vehicles in that category as shown for the ‘‘Other’’ option.

The explanation component of the system, in addition to the hover boxes, contains online ‘‘Help’’ that the user can manually execute for more detailed information, but the hover boxes appear automatically when the pointer is moved over any given box. The next screens (Figs. 6 and 7) show a lower-level set of options to which the user can navigate by following the higher-level paths in the system.

Fig. 6 shows the screen that the user will see after indicating that the vehicle is a two-seat automobile and illustrates the further classification available for that type of vehicle. In this example, the vehicle has been modified from the original design so ‘‘Modified’’ is the next option that should be chosen.

![](/api/attachments/5DH4JN4V/fulltext/images/bd917e4add3853040037bc0badd45f36bbc3e7d710fc60e33ff52e83323f7c8d.jpg)  
Fig. 3. Truck class.

![](/api/attachments/5DH4JN4V/fulltext/images/b3efbad408607ab56eb2a11e1e5a7d6235fa37c261c21d431cd65842bb7ae9bf.jpg)  
Fig. 4. Other classes.

Once the user clicks on the option ‘‘Modified’’, the screen is dynamically repainted so that the other three options at this level are made invisible and the option chosen is ‘‘grayed-out.’’ This provides an audit trail as to the options chosen to this point. At the same time, the options in the next level of the process become visible. The arrow at the lower right of the screen enables the user to return to the next higher level of classification if the previous selection was in error.

To proceed to the classification of the vehicle, the user would click on one of the options in the active buttons. In this case, the number of modifications is the decision criterion for the classification. The identifying information for the vehicle is carried forward and is displayed at the top of the screen so that the user can verify that this is the proper vehicle. In this instance, the options are self-explanatory (0 to 3 mods, 4-6 mods., etc.) so hover boxes are not needed. The list of major and minor modifications is included in the information provided to the user for classification purposes and can be determined by observation.

Upon reaching the lowest level in the decision hierarchy, the recommended classification is presented to the user as shown in Fig. 8.

In addition to the recommended class (313 in this case), a description of the class is provided (Sports Car:Mild Sports:D:1981-DATE) for verification. If this agrees with the audit trail of choices taken by the user, he will click on the OK button to complete the classification process for this vehicle. The options taken are then stored in the database along with the recommended classification and the process is complete for this vehicle.

By implementing the rule-based algorithm using a hierarchy of screen choices, the logic inherent in the database software is used for classification determination rather than a series of if/the/else statements, greatly simplifying the construction of the logic model. The if/ then/else structure would look something like this:

![](/api/attachments/5DH4JN4V/fulltext/images/837d5da42d6877588e5fe9896b878eb6c90262f40092f9af5d8e3dcee8bafcb3.jpg)  
Fig. 5. Level one interactive screen.

![](/api/attachments/5DH4JN4V/fulltext/images/5ee82adf8135d50867f066be1016fe9aa4a3c4b5420dd66b26271bf2d88cb1d9.jpg)  
Fig. 6. Subordinate level screen.

## Level One logic.

if [major classification] = “Automobile" then . . .else

$$
\begin{array}{r l} & \text { if   [major   classification] = "Truck" then...else} \\ & \text { do   [major   classification] = "Other"} \end{array}
$$

end if;

end if;

end if.

## Level Two logic

if [level two classification] = "2-seat" then . . . else

$$
\text { do   [level   two   classification] } = \text {"4 - seat"}
$$

end if;

It is readily apparent that given up to eight levels of classifications and approximately 400 final classifications, the logic model would become cumbersome at best. Modification and maintenance of the code would become problematic.

However, using the built-in logic of the relational data base management system and graphical interface, both logic generation and data storage are greatly simplified. Many of the logic modules are built-in and modification and maintenance simply become a matter of manipulating the screens to reflect updates and changes. In addition to the ease of use of this system for users, the graphical, hierarchical model becomes very attractive to both developers and users alike.

## 5. Human control of the model

One of the major advantages of this model is that it is under human control at all times. Observation on the part of the user is required for the discretionary activities and the results of the process are verifiable at all levels of operation. The expert’s knowledge is built into the structure of the choice matrix through the presentation of options included in screens based on the previous selections made. Also, verification of the final classification is provided in cases exhibiting some level of conflict among different classifiers. Since more than one classifier is used for each vehicle, conflict can arise over the correct classification. The system seeks to lessen the chance of conflict. The complete audit trail of choices and the information gathered and stored about each object in the set support group activities such as negotiation and conflict resolution. The model supports communication, modeling and negotiation, and intelligent support [9].

![](/api/attachments/5DH4JN4V/fulltext/images/654bfbc682ae206275c18b803552dafad2361b4148d642e9314f8d319af63bac.jpg)  
Fig. 7. Subordinate level screen.

The hardware platform is also subject to a great deal of control. The system can be employed on a stand-alone PC or on a client/server network either wired or wireless. User nodes can be laptops or handheld PCs or even PDAs, creating a high degree of flexibility in implementation of the system. The system can be controlled as to configure and use through the choice of platforms. Since the system is scalable, more complex problems in classification can be addressed through modification of the platform capabilities to whatever the appropriate scale of any given application.

![](/api/attachments/5DH4JN4V/fulltext/images/e1addf8296e953ca9aaaa510e0ffd38cc1116d0ee82d1e4409b36a3b6471d1de.jpg)  
Fig. 8. Recommended classification.

## 6. Further application of the model

The graphical model with its many advantages over the traditional DSS/ES model may be attractive in many other applications involving classification of discrete objects that exhibit certain homogeneous characteristics. Aside from fields involving vehicles such as insurance underwriting and competitions of various types, the model may be applicable to inventory management systems or part classifications for assembly line applications. For example, assume an airplane manufacturer produces several different types of airplanes. One might be a business jet that operates at high speeds and altitudes while another model might be a propeller-driven model operating at lower speeds and altitudes. The components for each model would vary substantially as to application and specifications.

An expert system could be constructed using the model described here to classify parts for the two different models based on requirements of the airplanes and specifications of the characteristics of the parts. Those suitable or unsuitable for each model of the airplanes could be readily distinguished and classified.

There are also law enforcement applications of the model. In an incident involving hostage taking, a set of scenarios could be constructed based on the facts at hand. The high-level alternatives might involve questions such as, ‘‘Has a perimeter been established?’’ with appropriate options to be pursued based on the answer. The alternatives could be constructed into the graphical interface with logic paths leading to recommendations for action based on the facts and logic of an expert as built into the system.

These are only a few of the possible applications for such a model. In fact, virtually any DSS/ES application can be implemented using the graphical, hierarchical approach to implementing a rule-based algorithm for discriminating among choices.

The resulting model greatly simplifies the generation and maintenance of the logic component over the if/then/else structure and enhances usability. The rule base as constructed from the experience and knowledge of the expert is incorporated into the hierarchy of screens presented so that only observation by the user is required for execution of the classification process. The model is applicable to a wide variety of DSS/ES system problems and allows a much simpler logic structure in these types of applications thus reducing complexity of the systems and, therefore, system cost, both initially and throughout the life of the system.

## Acknowledgements

This study was partially funded by a summer research grant from Belmont University.

## 7. Conclusion

This study has presented an approach to implementing a rule-based algorithm as the basis for an expert system through the construction of a graphical, hierarchical database system that allows the user to discriminate among choices for the classification of discrete, homogenous objects. The application used to demonstrate the model is a vehicle competition during which vehicles are classified according to attributes associated with them according to rules governing assignment of vehicles to those classifications. Thus, similar object vehicles can be judged in a given classification rather than comparing vehicles that are dissimilar in attributes.

In operation, a user choice at higher levels leads to mutually exclusive options at lower levels, indicating a path through the logic that leads to one, and only one, recommended classification. Explanation of options is provided to the user both pre-choice through hover boxes, a feature of the RDBMS, and post-choice through documentation of the trail leading to the next choice set. The system also provides for review by the expert at the culmination of the classification process. All components of an expert system are used in the model providing a robust implementation.

## References

[1] A.M. Beckers, M.Z. Bsat, A DSS classification model for research in human resource information systems, Information Systems Management 19 (3) (2002 Summer) 41– 50.

[2] M. Benaroch, M. Tanniru, Conceptualizing structurable tasks in the development of knowledge-based systems, Decision Sciences 27 (3) (1996 Summer) 415 – 449.

[3] G.D. Bhatt, The enabling role of decision support systems in organizational learning, Decision Support Systems 32 (3) (2002 January) 297 – 309.

[4] C. Doumpos, Multicriteria classification and sorting methods: a literature review, European Journal of Operational Research 138 (2) (2002 April 16) 229 – 246.

[5] G. Elofson, Intelligent agents extend knowledge-based systems feasibility, IBM Systems Journal 34 (1) (1995) 78 – 95.

[6] S. Gregor, I. Benbasat, Explanations from intelligent systems: theoretical foundations and implications for practice, MIS Quarterly 23 (4) (1999 December) 497– 530.

[7] F. Hayes-Roth, N. Jacobstein, The state of knowledge-based systems, Association for Computing Machinery, Communications of the ACM 37 (3) (1994 March) 26–39.

[8] M.J. Hines, M. Goul, The design, development, and validation of a knowledge-based organizational learning support system, Journal of Management Information Systems 15 (2) (1998 Fall) 119– 152.

[9] T.-P. Liang, Model Management For Group Decision Support, MIS Quarterly 12 (4) (1988 December) 667– 680.

[10] J.-Y. Mao, I. Benbasat, The use of explanations in knowl-

edge-based systems: cognitive perspectives and a processtracing analysis, Journal of Management Information Systems 17 (2) (2000 Fall) 153 – 179.

[11] M.D. Mattei, Using ‘‘expert systems’’ for competitive advantage, Business and Economic Review 47 (3) (2001April – June) 17 – 20.

[12] S.D. Seilhamer, Current State of Decision Support System and Expert System, Journal of Systems Management 39 (8) (1988 August) 14 – 19.

[13] V.C. Storey, R.C. Goldstein, J. Ding, Common sense reasoning in automated database design: an empirical test, Journal of Database Management 13 (1) (2002 January – March) 3– 13.

[14] C. Wagner, End users as expert systems developers? Journal of End User Computing 12 (3) (2000 July – September) 3 – 13.

![](/api/attachments/5DH4JN4V/fulltext/images/90f0f63b647f5a4a2efc7fb5a3d69ff7e4fbedc431682f597ab1def08aa2ee7a.jpg)

Roy Martin Richards, Jr., PhD received his doctorate from the University of Georgia and his Master of Business Information Systems and Bachelor of Arts from Georgia State University. After serving more than 30 years on the faculties of University of North Texas in Denton, TX, University of Dallas in Dallas, TX, University of Montana in Missoula, MT, University of Georgia in Athens, GA, and Belmont University in Nashville, TN, he recently retired from

academia to pursue a career in criminal justice. His research is widely published and he serves as minitrack chair for the Topics in Organizational Systems and Technology at the Hawaiian International Conference on System Sciences.
