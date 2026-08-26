---
otero_id: 18292
otero_key: "KX3C7NQH"
title: "End-user computing environments — Finding a balance between productivity and control"
authors: "Dale J. O'Donnell; Salvatore T. March"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90012-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# End-User Computing Environments – Finding a Balance Between Productivity and Control

Dale J. O'Donnell

Hewlett-Packard, 3000 Hanover Street, Palo Alto, CA 94303, USA

Salvatore T. March

Department of Management Sciences, University of Minnesota, Minneapolis, MN 55455, USA

Finding a proper balance between productivity and control is critical for maintaining an effective end-user computing environment. This paper surveys problems associated with productivity in end-user computing environments including their causes and organizational impacts. Controls are recommended to overcome the problems and thereby enhance productivity.

Keywords: End-user computing, Information center, Managing end-user computing, User developed systems, Productivity and control in end-user computing environments.

## 1. Introduction

An end-user in the Finance Department ponders the following questions: “Should I develop my own computer model and database in a fourth generation language, have my secretary key in the data, and immediately use the model for decision support, or should I have someone from the MIS Department build the model and database, then have someone from Internal Auditing validate the model and data and crosscheck the results before I adopt the system?” On the one hand, by developing the model and database himself and bypassing the validation and crosschecking the system would be implemented more quickly, thereby enhancing productivity. On the other hand, if the model makes inappropriate assumptions or the data is inaccurate, poor decisions may result.

While end-user computing has the potential to dramatically improve the decision making capabilities of management, it also has the potential to quickly generate very poor results. The adage, "To err is human ... but to really mess up, you need a computer" is particularly appropriate for end-user computing.

![](/api/attachments/KX3C7NQH/fulltext/images/0ac5eebf750d0f12717a2a1df533851ec6c6c6786a84a3c89d78404b0e8c9e63.jpg)  
Dale J. O'Donnell is a Systems Analyst in the Financial Services area of Hewlett-Packard Company in Palo Alto, California. He received his BS degree from Iowa State University and his MBA degree in Management Information Systems from the University of Minnesota. Mr. O'Donnell is active in software development, analysis of software tools, and establishment of personal computer strategies.

![](/api/attachments/KX3C7NQH/fulltext/images/ec77650214ac688056c73f8b386a6b4c8fa70e37c32a26e0d2b40081f2acbf78.jpg)  
Systems, The Journal of MIS, and Management Science. He is currently the Editor-in-Chief of ACM Computing Surveys.

The above scenario depicts a growing concern in end-user computing (EUC) environments. As organizations become more cost conscious and user oriented, computer tools proliferate, and the impetus is toward direct application of information technology by managers to improve their productivity. However, a counterbalancing set of computing controls must be administered to maintain the integrity of the solutions. Finding the appropriate fulcrum between productivity and control within the EUC environment is a challenge.

Productivity and management of EUC are getting the attention of many information systems (IS) professionals. In a recent survey of key IS management issues [5], facilitation and management of EUC ranked second only to improved IS planning. Productivity improvement and measurement ranked fifth. The EUC productivity/control issue is not exclusively an IS concern. Rather, since EUC transcends the whole organization, it is a concern of the entire enterprise. And this concern is magnified due to a lack of understanding of computing issues within the organization.

The central advantage of EUC is the increased potential for white-collar productivity. Because end-users understand their business problems better than IS professionals, they can often quickly create their own computing solutions. This has the complementary impact on IS of relieving the backlog and opening windows for more long-term project development.

However, the proliferation of EUC must have some controls. Uncontrolled EUC environments lead to disproportionate resource utilization, animosity and dysfunctional behavior between IS and EUC, and loss of business position resulting from ill-computed problem solutions [1]. An intriguing situation develops. On the one hand, it is important for the organization to take a proactive position vis-a-vis EUC and to encourage end-users to take advantage of the information technology [17]. On the other hand, it is important to control the EUC environment so that runaway budgets, inaccurate problem solutions, and negative internal relations do not occur.

This paper therefore discusses the issue of EUC productivity and the associated control necessary to maintain a balance between the two.

## 2. General Definitions

The term, “productivity” carries a variety of meanings. These are particularly confusing in EUC environments. Webster’s generic meaning is, “to yield or furnish results, benefits, or profits [18]” – a good basic definition for EUC. EUC productivity can further be partitioned into personal productivity of the end-user, project productivity, and enterprise productivity. Components of EUC productivity include measurements based on speed, cost, or yield [10].

The term, “control,” in the context of an EUC environment, has a straightforward meaning. It does not mean impeding EUC, rather it means guiding, directing, and encouraging its effective use [1]. Controls can be either general or specific in nature. A general control may evaluate the concentration of potentially conflicting functions within the EUC environment, whereas specific controls address a specific stage in development (e.g. testing) and detail the appropriate actions to be taken [19].

It is imperative to establish the meaning of the term, “end-user.” There are numerous taxonomies in the literature. Often, however, the categories are either loosely defined and overlapping so that categorization is difficult, or too specific, leaving some classes undefined. This classification road-block is further complicated by the constant change within end-user environments.

For purposes of analyzing the productivity/control issue, a composite of two taxonomies is used. Martin [13] simply breaks end-users into three categories:

1. Indirect end-users - people who use computers through other people, e.g. an airline passenger making flight arrangements through a travel agent.

2. Direct off-line users – people who specify business information for reports they ultimately receive, e.g. marketing managers.

3. Direct on-line users - people who actually use terminals, hands on, to gain information.

The productivity/control dilemma within most organizations centers primarily on the “direct online” users. Rockart and Flannery [15] further categorize Martin’s “direct on-line” group into six sub-groups:

1. Non-programming end-users - only access information through software provided by others - they do no programming or report generation and live totally in a menu-driven environment.

2. Command level users - access data on their own terms; they perform simple inquiries, calculations, and generate reports; they learn enough about databases to do their daily work.

3. End-user programmers - use command and procedural languages to develop their own applications, some of which are used by other end-users.

4. Functional support personnel - sophisticated programmers supporting end-users within their particular functional areas. They informally provide system design and programming expertise but are not viewed as DP professionals.

5. End-user computing support personnel – located in a central support organization, such as an Information Center. They are fluent in end-user languages and develop either application or "support" software.

6. DP programmers - similar to traditional programmers except they program in end-user languages.

The productivity/control issue, for this paper, is directed at Rockart's categories 1–4; i.e. those end-users typically not a part of the formal MIS/DP functional area. As easier-to-use software continues to develop, workstations offer more effective personal computing/host mainframe access, and computing needs expand within each functional area, this group poses the largest threat to a misbalanced productivity/control environment. Relative to traditional MIS/DP, this group will grow in size, yielding an even larger threat.

## 3. Key EUC Problems and their Impacts on Productivity

We now discuss some key productivity problems in EUC environments.

## 3.1 Problem: Lack of a Concrete Corporate Strategy Relative to EUC [6]

Organizations have allowed their EUC environment to evolve without an overall corporate strategy. There are several results from the lack of a well-conceived corporate strategy. These include:

1. A global “information architecture” is not developed. This has profound impact on the future of EUC. An information architecture lays the foundation for well-designed data structures and application portfolio. Absence of these components leads to confusion about the information capability of the organization. Hence, end-users do not know what information is available or how their requirements fit with those of other organizational units or functional areas.

2. A rational, optimal allocation of EUC resources is absent. Without a plan, users are likely to develop incompatible tools or purchase incompatible hardware. End-users, like IS personnel, are prone to buy hardware because it is “new and fast” and not because it fits the application or the environment. However, as communications and integrated databases become more common, incompatible equipment and applications become the Achilles heel.

3. Application and database development priorities are not established. Lack of these lead to scheduling conflicts, redundancies, and unshareable data. Without an overall plan, end-users develop their personal agendas for development of applications and their own criteria for data integrity and security. These may not coincide with the real needs of the company or organization. The results are inappropriate solutions to organizational problems, redundant applications, and inconsistent data. Additionally, end-users may casually develop a crucial system without concern for the needs of other “stakeholders.”

## 3.2 Problem: Lack of Organizational Fit Between EUC, Top Management, the DP/MIS Function, and Other Functional Units [15]

Although not a separate function, EUC may be out-of-synchronization with the DP/MIS function and other functional units. Organizational fit, in this context, means position within the hierarchy of an organization, implying job responsibility and reporting relationships.

Organizations have a difficult time properly positioning EUC. This is not surprising, considering the difficulty organizations have in positioning the more traditional DP/MIS function. Typically DP/MIS began within Accounting or

Finance [8]. In some organizations it remains within one of those functions [6] while in others a separate DP/MIS function has been established. Expansion of EUC into all areas of the organization further complicates this situation. If, for example, DP/MIS is within Finance, should EUC report to Finance? If so, will other functions view EUC as only supporting Finance? Finally, it is not uncommon for general management to have an aversion to computing, and to be unconcerned about EUC positioning, thereby increasing the probability for improper EUC fit.

Some of the impacts of poor organizational fit of EUC are:

1. Dysfunctional behavior and animosity can develop between DP/MIS and EUC, between end-users across functional units, and between users within the same unit [12]. Often the “keepers” or “developers” of a system feel possessive and afraid of losing their “edge.” Therefore, they have an incentive not to communicate the value of their computing tools. Even an information center, if not properly positioned with the organization, cannot overcome the personal and political problems that may arise.

2. Without an identifiable organizational fit, reporting responsibilities become clouded. When an application strongly enhances productivity, many units are groping to accept the credit. However, when an application fails, massive "finger pointing" results. Clearly, it is important to define the chains of command.

3. Even with an identifiable organizational fit, inappropriate criteria for performance appraisal can lead to disincentives relative to EUC. Given a commitment on the part of upper level management to organization-wide use of information technology in decision making, performance appraisals must consider not only the actual results of EUC for a particular decision, but also the technical skill development of the manager [14]. Furthermore, a model or database developed for one problem may be of use for others. Therefore, evaluating the performance of a manager involved in EUC completely on the basis of current results may be counterproductive.

## 3.3 Problem: Lack of a Systematic Software Design Process in the EUC Environment [1]

Many organizations have either not developed standards and policies relative to the software design process in the EUC environment, or have not communicated them. This problem surfaces in the EUC environments where end-users are developing applications (Rockart categories 3 and 4, and, to a lesser extent, category 2).

Multiple reasons exist for this obvious lack of systematic design. The reasons include:

1. A systematic design process may never have been established as a part of traditional DP/MIS – therefore, it is hard to conceive of a systematic approach to EUC.

2. Management of the functional unit establishes such rigorous demands on the EUC environments, that even if end-users knew the principles of software design, time would not allow their proper application.

3. End-users within the EUC environment do not fully understand the power of computers and their own skill limitations. Consequently, many end-users do not appreciate the need for a formal design methodology.

The lack of a systematic software design process can have profound impacts on the entire organization, especially in terms of EUC productivity. These include:

1. Conceptual design risks – often, user developed systems are not “designed,” they are developed “on the fly.” Without a formal statement of what the system is to do, there is little opportunity to select the appropriate implementation approach. What might appear to be a spreadsheet oriented problem could, on further analysis, turn out to be a database oriented problem. The results are inappropriate problem representations and the use of inappropriate implementation tools.

2. Documentation risks - end-users do not document their systems. They consider the effort to be a "waste of time." They fail to realize the difficulty others will have in understanding their system when called upon to make changes.

3. Testing risks - partially because most end-users have not come through the ranks of DP/MIS, there is a lack of emphasis on testing. Even rigorous testing cannot prove that software is error-free, but failure to do even minimal testing leaves the company at great risk (from a quality assurance perspective).

4. Maintenance - many end-users have a limited time horizon for the use of the newly developed system. Frequently, they view the computer solution as having applicability only for their immediate problem. Implementation decisions are made that decrease the development time even if their ultimate effect is to make system maintenance more difficult. The net result is that maintenance of these systems is often very expensive in both time and money [1].

5. Computer usage - most end-users view computer time as free, especially in an EUC environment. Very few understand the impact that their applications can have on response time and overall costs for the organization.

## 3.4 Problem: Lack of Quality Perspective [4]

Many user developed systems fail to genuinely incorporate “quality” into the software developed and the data manipulated. Quality, in this context, means reliability and accuracy.

A quality perspective can be lost in many parts of the organization. Top management should create a culture in which “quality counts.” Without this atmosphere it is unlikely that quality will evolve. However, the best orientation communicated from upper management will not overcome a lack of communication and practice within each EUC organizational unit.

The lack of a quality perspective can have a profound effect. As is the case with “audit” types of functions, many end-users hate to follow the rules necessary to insure quality. The effects of a lack of quality perspective include:

1. EUC solutions are not always correct. One can argue that users are no more at risk with computers than without, but, considering the size and complexity of problems that computers can handle and the assumption that "if it came from a computer it must be right," it is a stronger argument that use of the computer significantly increases the risk of flawed solutions.

2. EUC creates data security and integrity risks, thereby directly affecting the quality of the products [9]. The expanded use of DBMSS increases the probability of erroneous updates, violations of privacy and security rules, and of other criminal acts.

## 4. Controls and Measurement Mechanisms

Several practices can be incorporated into the EUC environment to insure that these problems reduce productivity.

## 4.1 Overcoming the Lack of a Corporate Strategy

Obviously, the most effective approach is to develop an EUC strategy. However, this is not a straightforward task. It is imperative that EUC become a part of the corporate strategy process rather than an afterthought [11]; i.e. the EUC plan must evolve concurrently with corporate plans. Initial EUC planning by the DP/MIS function in conjunction with other functional units prior to the production of an overall corporate strategy improves the chance of adoption of EUC plans throughout the enterprise.

A staged process [6] similar to that proposed for MIS planning can be used. The major sequential steps are:

1. Assess organizational objectives and strategies – analyze the current strategic organizational plan. Identify the major dominant groups and their objectives.

2. Set EUC mission by establishing an EUC charter.

3. Assess the EUC environment – identify the current EUC capabilities, new opportunities, the business environment, future technologies, current EUC applications portfolio, the EUC image, stage of EUC maturity, and personnel skills.

4. Set EUC policies, objectives and strategies - establish the organizational function, technology focus, resource allocation mechanism, and functional capability objectives.

5. Assess the organizational information requirements – develop an information architecture by analyzing organizational functions and activities and their information needs.

6. Assemble a master development plan for EUC - identify the needs, assign a priority ranking, and generate a proposed schedule to accomplish these. Needs assessment should include areas such as organizational learning, availability of technology, and accessibility of information.

7. Develop a resource plan - define hardware, software, training, and space needs and incorporate them into the EUC facilities and financial plan.

8. Design a cost/benefit evaluation system for EUC projects. This includes establishing project evaluation criteria, as well as criteria for assigning project to functional units (or to the MIS Department).

## 4.2 Overcoming the Lack of Organizational Fit

Trying to develop absolute rules for fitting EUC into an organization is not possible; they are specific to each enterprise. However, general conceptual frameworks are useful and may provide a format for placement of EUC.

The dysfunctional behavior and animosity that develop in EUC can often be traced to a lack of proper communication. An information center (IC) may help to bridge the communication barrier by providing a liaison among users and DP/MIS professionals. Ics typically act as consulting and service facilities that help end-users access their data [2]. Appropriately positioned, Ics can do much to enhance productivity in an EUC environment.

If the IC is placed under the control of the DP/MIS manager, then it is viewed (and used) as a tool of DP/MIS and not of EUC. This hampers the IC in developing the appropriate level of communication with its users. On the other hand, if the IC is placed under the control of a functional area manager, it is often seen as only belonging to that functional unit. The optimal placement of the IC is at the level of the development managers, as an independent organizational entity, so that everyone using the IC has equal status [9].

Responsibility for some aspects of the EUC environment belongs in the IC while others must rest with user management. For centralized functions, such as education and training, the IC is the logical locus of responsibility. Similarly, the IC is responsible for interfacing with DP/MIS (and Data Administration) for obtaining access to production data and for determining the level at which user developed systems should be integrated with existing production systems.

Responsibility for application selection and for the actual system development, however, lies with the functional unit [16]. End-user management must develop performance appraisals for EUC. A Management by Objectives (MBO) approach can be used. Such an approach assigns weights to each task (objective) to be performed. Performance is evaluated by combining the objectives accomplished and the weight of that objective. To attain status with other jobs, EUC must also be evaluated. Therefore, for end-users heavily involved in development, there should be a separate MBO weight that gauges their performances relative to EUC.

## 4.3 Overcoming the Lack of a Detailed Design Process

The lack of a detailed design process implies the need for a well enforced “standards and policies” program. Such a program must begin with a well-publicized and vigorously supported standards and policies manual. The manual should outline the responsibilities of all parties, describe alternative methods of implementation, and provide criteria for selecting an implementation method. It must argue for the benefits to the end-user of such a program. The program must be in place long before the first user signs onto the system. It establishes a cultural norm, making the user feel unnatural when trying any activities outside the boundaries. Such policies help to define the environment and identify out-of-control situations.

Education and standards relative to conceptual modeling are necessary to develop a productive EUC environment. Rather than initially imposing physical limitations and application methods on end-users, it is better to use a “problem solving approach.” Conceptual design is taught as a means of solving the problem rather than as a set of rules to be followed. Logical data modeling is one such conceptual tool $[3]$ . Standards relative to the correct modeling procedure should be taught. However, the benefits to the user of developing a logical data model must be stressed. These include: better understanding of the system under development, enhanced ability to use application development tools, lower likelihood of errors in the implementation, and increased ability to communicate with DP/MIS to determine if access to a production database is appropriate for this application.

Design policies and standards for application generation (end-user categories 3 and 4) include: 1. Formatting procedures so that the writing style reflects the function performed.

2. Requiring that the scope and relatedness of applications be specified.

3. Naming conventions that clearly identify the data used and activities done.

4. Documentation standards detailing the degree and type of documentation needed. At least author's name, creation date, summary of purpose, and modification history should be included.

5. Testing standards requiring a description of the test plan, the predicted results, and ultimately the actual results. Recording the number of test iterations encourages good test planning [4].

6. Maintenance standards to scope the range of maintenance activity and record the frequency and type of maintenance activity on the system.

## 4.4 Overcoming the Lack of a Quality Perspective

A key first step in insuring quality in an EUC environment is to provide a basic understanding of the components of quality. Provision of EUC quality [4] requires:

1. Integrity - the data contained in a system must be correct, timely, and meaningful. Tight controls on input and validation routines and data redundancy must be implemented.

2. Dependability - application products must demonstrate consistency and stability. The user must believe that a process or procedure will produce the same accurate results each time it is performed.

3. Ease of use - applications developed by end-users must be useable by end-users. End-users who become "expert" in a tool must avoid using "shortcuts" that make the system difficult for other managers to use.

The data integrity and security issue is critical for effective application development and computer processing in all of the EUC environment. Some of the crucial security issues include [9]:

1. Responsibility for confidentiality of passwords and sign-ons.

2. Frequency of and responsibility for password changes.

3. Length of a session, i.e. the time horizon of sign-on without rejustification.

4. Criteria for access to a production database (this is definitely not for beginners).

5. Sharing of data among applications.

Data integrity and dependability, as components of EUC quality, typically involve establishment of validation principles. Validation occurs on many levels including: data item, record, batch, and the database. The validation process will not produce error free data, but with concrete criteria in mind, an end-user can check (manually or within the software) much of the input, and output data [7]. Further, it is important to integrate a compliance audit into many of the EUC systems. This will aid in predicting the reliability of a system. Since each computer abuse has an average impact of \$500,000 [19], EUC audit controls are clearly needed. This is particularly important since many systems are chained (i.e. a sales transaction may generate a credit check, and updates to billing, inventory, and receivables data). Two of the controls in an EUC audit are:

1. Verification that controls exist in the software and that these have been appropriately tested, are working as specified, and cannot be overridden without appropriate documentation being produced.

2. Verification that the software processes input transactions consistently, including appropriate error messages.

## 5. Evaluation of the Productivity versus Control Issue

Finding the optimal balance between productivity and control is critical to the success of any EUC environment. An unrestrained EUC environment can lead to inconsistent, incoherent systems that inhibit rather than enhance effective management. Too restrictive an EUC environment can lead to limited computer use because of the perception that there are “too many rules.” Appropriate controls can actually enhance productivity.

We argue that control is essentially a component of productivity. To be productive in developing computer applications, specific controls must be in place. Too often emphasis is placed on simply solving the problem without concern for its relationship to corporate goals, the organizational fit, a systematic design process, or quality-issues directly related to control.

The control activities can be categorized as addressing environmental or process issues. The lack of corporate plan and improper organizational fit are environmental issues. They relate to control at the organizational level. The lack of detailed design process and quality assurance are process issues. They relate to control at the development level. The environmental issues are subjective in nature, they require policy development by upper management. The process issues are more objective, they can be addressed by training and development controls at the level of the individual. The net effect is the need for a flexible managerial approach including both global plans and policies to address the environmental issues and specific guidelines and training activities to address the process issues.

Finally, as is often the case with MIS-related issues, communication is the cornerstone of a well-managed EUC environment. The outlined problems are typically magnified if a breakdown in communication occurs. Global plans and policies control must be clearly communicated before managers become heavily involved in EUC. Managers must understand the established EUC environment. Similarly, the specific guidelines for developing applications and using the EUC environment must also be communicated. These require well developed training programs and technical support. The Information Center is the logical vehicle for facilitating this level of control.

## References

[1] Alavi, M., and Wiess, I.R.: “Managing the Risks Associated with End-User Computing,” Journal of Management Information Systems, Winter 1985–86, Vol. II, No. 3; pp. 5–20.

[2] Atre, S.: “The Information Center and Productivity Tools: Working in Harmony,” Computerworld, September 18, 1985, Vol. 19, No. 37A.

[3] Chen, P.P.: “The Entity-Relationship Model – Toward a Unified View of Data,” ACM Transactions on Database Systems, Vol. 1, No. 1, March 1976; pp. 9–36.

[4] Christoff, K.A.: “Building a Fourth generation Environment,” Datamation, September 15, 1985; pp. 118–24.

[5] Dickson, G.W., Leitheiser, R.L., and Wetherbe, J.C.: “Key Information Systems Issues of the 1980s,” MIS Quarterly, September 1984; pp. 135–59.

[6] Dickson, G.W. and Wetherbe, J.C.: The Management of Information Systems, McGraw-Hill, 1985; pp. 26–31, 124–128.

[7] Everest, G.C.: Database Management Objectives, System Functions, and Administration, McGraw-Hill, 1986; pp. 454–574.

[8] Gibson, C. and Nolan, R.L.: “Managing the Four Stages of EDP Growth,” Harvard Business Review, Vol. 52, No. 1, January-february 1974; pp. 76–88.

[9] Hammond, L.W.: “Management Considerations for an Information Center,” IBM Systems Journal, Vol. 21, No. 2, 1982; pp. 130–61.

[10] Jones, C.: “How Not to Measure Programming Productivity,” Computerworld, January 13, 1986; pp. 65–76.

[11] King, J.L.: “Strategic Planning for Management Information Systems,” MIS Quarterly, March 1978.

[12] Kutnick, P.: “Information Center Success Hinges on 10 Important Axioms,” Data Management, November 1985; pp. 15–7.

[13] Martin, J.: Application Development Without Programmers, Prentice-Hall Inc., 1982; pp. 100–04.

[14] Nolan, R.L.: “Managing the Crisis in EDP,” Harvard Business Review, Vol. 57, March-April, 1979; pp. 115–126.

[15] Rockart, J.F. and Flannery, L.S.: “The Management of End User Computing,” Communications of the ACM, October 1983, Vol. 26, No. 10; pp. 776–84.

[16] Thurston, P.H.: “Who Should Control Information Systems?” Harvard Business Review. January-February 1962; pp. 135–9.

[17] Vacca, J.R.: “The Information Center’s Critical Post-Start-Up Phase,” Journal of Management Information Systems, Spring 1985; pp. 50–55.

[18] Webster, N.: Webster's New Collegiate Dictionary, G. & C. Merriam Company, 1979; pp. 918.

[19] Weiss, I.R.: "Auditability of Software: A Survey of Techniques and Costs," MIS Quarterly, Vol. 5, No. 4; pp. 39–49. SIM/MISRC; December 1980.
