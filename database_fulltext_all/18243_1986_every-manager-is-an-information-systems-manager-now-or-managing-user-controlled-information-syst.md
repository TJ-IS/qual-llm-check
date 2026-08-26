---
otero_id: 18243
otero_key: "P68C6Q2D"
title: "Every manager is an information systems manager now, or, managing user-controlled information systems"
authors: "Gerald M. Hoffman"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90043-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Every Manager is an Information Systems Manager Now, or, Managing User-Controlled Information Systems

Gerald M. Hoffman

The Gerald Hoffman Company, 212 E. Ontario Street, Chicago, IL 60611, USA; teleph.: (312) 664-8039

There are many examples of microcomputer based information systems built and operated by people in the departments using the systems – people who are not information systems professionals. When such “user-controlled systems” are used for departmental (as distinguished from individual) purposes, they are in effect miniature Information Systems Departments (ISDs), with all of the managerial and technical problems of such departments. The manager of the user department is, willy-nilly, an information systems manager, with all of the problems of the manager of the main ISD, and with little or no technical support staff. These problems require solutions in the microcomputer environment which are often different from the standard mainframe solutions, and in many cases the ISD staff has not developed appropriate microcomputer solutions. This paper reviews the relevant literature, most of which takes the Information Services Department point of view, gives examples of microcomputer-specific solutions to common information systems problems, and suggests ways in which the ISD can provide better support to managers of user-controlled departmental information systems.

Keywords: Management, microcomputers, user management, information systems, personal computers, end-user computing, policy.

The Parable Of The Purchasing Manager And The Nerd

Once upon a time, not so long ago and in a place not so far away, there was a Purchasing Manager for a Great Company. The Company was so Great that Purchasing Manager had a staff of 22 people, for Great Company spent much money. Among their tasks was analysis of the choice between leasing and purchasing expensive capital equipment. One of the people assigned to lease/purchase analysis was Nerd, a financial analyst by training and a closet computerphile.

As interest rates increased, lease/purchase analysis became more important and more frequent; a backlog developed and Purchasing Manager told Nerd that she was planning to hire another analyst to help him. Nerd suggested that

![](/api/attachments/P68C6Q2D/fulltext/images/7bd2e850def23a979228a61180a2d29363f0c9008da1b5529953329ca8b80634.jpg)

Gerald M. Hoffman was, until recently, Managing Director of Lodestar Corporation, a software and consulting firm specializing in the use of information systems and management science to increase business profits. He has managed and executed assignments in all areas of business, including general management, information systems, production and distribution operations, marketing, human resources management, and strategic and tactical planning.

Dr. Hoffman is Adjunct Professor of Industrial Engineering and Management Science at Northwestern University, and Adjunct Director for Research at the Center for the Study of Data Processing of Washington University in St. Louis. He teaches in executive programs in the United States and in Europe, including those at Columbia University and at Washington University.

He has been Executive Vice President and General Manager of Amoco Computer Services Company, Manager of Operations Research for Amoco Corporation, and President of Panoramic Builders, Inc.

instead of increasing staff, Purchasing Manager authorize Nerd to acquire a microcomputer. Nerd would select the machine and write programs to do the analysis. Then he, Nerd, would be able to handle the entire lease/purchase workload, and eliminate the backlog as well.

Although she was somewhat dubious, Purchasing Manager agreed, and Nerd bought the microcomputer. He wrote the programs and did the analysis. The results were spectacular: the backlog disappeared, and response time for requests for new analyses dropped dramatically. The department was running so smoothly that Purchasing Manger was able to take a long-delayed vacation. She went to Acapulco for two weeks.

After he completed the backlog, Nerd had time on his hands. He decided to use his microcomputer to keep track of his open orders – purchase orders which had been issued but not yet filled by vendors. He wrote the program in two days, and spent another day entering data. Nerd was very proud as he showed his work to his colleagues, and they were mightily impressed. During coffee break the next morning, Eve, another member of the purchasing department, asked Nerd if his computer were powerful enough to keep track of her open orders as well as his. Nerd said said that of course it was, and they proceeded to enter her data.

Thus it came to pass that on the fourth day of her vacation, even as she lay basking in the Mexican sun, Purchasing Manager became an information systems manager as well. And she didn't even know it! (Nor did Vice President for MIS of Great Company.) The microcomputer, which had been purchased as a tool to help one person do his job more efficiently, had become a system serving more than one person, and performing an activity vital to the mission of her department. She was now responsible for technical information systems activities of whose existence she was not even aware: data integrity, disaster recovery, hardware service, et cetera, et cetera, et cetera. There was to be a day of reckoning....

## 1. Introduction

The purchasing manager in the parable above is by no means unique. Lehman [5] makes the distinction between “personal computing … use by an individual to carry out his or her job" and "organizational computing ... creation of information ... utilities ... for use by the organization as a whole". In the parable, the microcomputer was acquired to do a personal computing task: help one person do lease/buy analyses; the potential for trouble began when it was thoughtlessly used for organizational computing: tracking of open orders. Recent studies have shown that there is significant use of microcomputers for organizational computing. Benson [2, page 39] discovered that $29\%$ of initial applications of microcomputers were for data capture. Lee [4, page 316] found $28.8\%$ of users using data base applications and $13.8\%$ using mainframe connections. It is likely that most of these applications, plus some in other categories, represent organizational computing.

The MIS literature on end-user computing has mainly focused on new managerial problems of information systems professionals, problems which have been generated by the proliferation of micro-computers in the hands of users. The issues addressed are mostly systems issues (hardware and software compatibility, micro-mainframe connections, choice of tools, methods of providing support to users, etc.) and organizational issues $[1,3,6,8,10]$ . Most of the papers deal with personal rather than organizational computing. Recommendations to Information Systems Department (ISD) managers fall into two main categories. The first is that ISD take an active role in controlling end-user computing. The second is that ISD provide support to end users, often by means of information centers.

Only in a few instances is it acknowledged that the end-use computing requires management in the user department. The very term ‘microcomputer manager’ or “personal computer manager” has been defined as a member of the Information Systems Department who assists and/or controls users; see Shoor [10]. McFarlan and McKenney [8, page 95] recognized in 1983 the difficulties of orderly management of user controlled information systems, pointing out that the larger professional staff of a central department was better equipped to control complex IS activities than the typical staff supporting minicomputers. The problems of managing microcomputer based systems are the same, and they often have no professional support whatsoever. Leitheiser and Wetherbe [6] speak of “managing end-user computing”; but their discussion deals with how responsibilities for computing should be divided between ISD and end-user departments, how ISD should manage that division of responsibilities and how ISD should support the users.

Benson [2, page 40] and Lucas [7, page 42] recognize explicitly the problem addressed in this paper: how a manager in an end-user department should manage the information systems activities under his jurisdiction. Benson lists a number of common shortcomings in user-controlled systems. Lucas says, “In today’s processing environment, divisional and middle managers are confronted with making to the delegated to computer professionals.” He then provides a list of questions to which these managers must respond, and a list of recommendations for action. The questions are important and the recommendations are sound. However, neither Benson nor Lucas deals with the overall task of managing the divisional information systems activity.

## 2. The Miniature Information Services Department

Any business unit which has at least one user-controlled information system which is an organizational system (by Lehman's definition, quoted in the first paragraph of the introduction) has almost all of the functions and problems of a large mainframe-based information services department. However, the execution of these functions and the solution of these problems are different for the user-controlled activity, because (1) the hardware and software is smaller and less complex, (2) the user-controlled systems must fit (in many senses of the word) into the larger structure of the enterprise's information systems, and (3) the user-controlled function typically has little or no information systems expertise in its own staff.

It is the thesis of this paper that the information systems issues facing managers of departments with user-controlled systems can be best understood by viewing the user department as having its own management information systems activity, small but complete. (This is not to suggest that there should be a dedicated organizational unit; it is more likely that most of the activities will be part time assignments.)

The goal of this paper is to encourage the information systems profession to provide the managers of user-controlled systems with tools and method appropriate to their jobs, rather than to demand that the users employ tools appropriate to the tasks of the IS professional. (An instance of the neglected of ordinary ISD procedures by microcomputer users is reported by Raimondi [9] in a news article in Computerworld, which describes the success of a disaster backup plan when a major fire occurred. The entire execution of the plan was a success, except: “The only hitch … was that IBM PC users had no off-site backup, so their data was lost.”)

## 3. Managing The Miniature Information Services Department

This analysis takes the point of view of the manager of a department with a user-controlled organizational information system, describing some of the information systems problems facing that manager and suggesting solutions. It is assumed that there is a central Information Systems Department responsible for overall coordination of information systems in the organization, and that this department will provide technical support as requested.

A comprehensive treatment of these issues is far beyond the scope of this article. Rather, emphasis is placed on differences between the micro and the mainframe environments, and on issues often overlooked. The actions proposed are designed to be evocative rather than comprehensive or universally applicable. Many of the ideas suggested are elementary and well-known to information systems profession; this is by design, because it makes them potentially more useful to user managers than the more complex tools necessary to operate a large IS organization.

## 3.1. Systems Development

## 3.1.1. Selection and justification of new systems

The selection and justification of the first user-controlled system in a department usually appears to be self-evident: there is an obvious departmental need, and the hardware and software for the proposed microcomputer solution appears to cost substantially less than the amount estimated by ISD for a mainframe solution. For many types of systems, micro solutions are indeed less expensive.

However, the manager should be alert for three kinds of hidden costs. First is the cost (direct cost and opportunity cost) of departmental personnel doing information systems work, both during development and during operation. The second hidden cost is the cost of poor quality. This can take a variety of forms, including inadequate documentation, insufficient testing, etc. The third hidden cost is the opportunity cost resulting from departmental personnel not being acquainted with all of the information system possibilities available to them.

When any new system is proposed, the manager should:

be sure that all costs are included in the economic analysis which justifies the system.

make certain that there is some consultation with information systems professionals to determine whether there are any known pitfalls or missed opportunities in the proposal.

be sure that s/he is willing to divert the required resources, particularly people, to information systems activities.

## 3.1.2. System acquisition strategy

One of the common reasons that applications systems cost so much money is that users insist that the systems be exactly what the users want. This inevitably means that the system must be built from scratch, rather than being purchased off the shelf, which is nearly always less expensive. The preferred methods of acquisition for user-controlled systems are, in order of preference:

1. Purchase of a turnkey system. Such systems often provide for a significant degree of customization for each user. No modification should be permitted beyond those provided for by the vendor.

2. Purchase of an application development shell, such as a spreadsheet or a database package, and development of the application by the user group. The system should be built using the basic facilities of the package; use of associated programming languages should be avoided where possible, and otherwise kept to an absolute minimum. Extensive requirements for external programming should be taken as a sign that a choice of the package was wrong.

3. Acquisition of a custom system through the ISD, either built by ISD or acquired by ISD for the user group. Under no circumstances should a system requiring programming in a third generation language be undertaken by a user group. The necessary skills are unlikely to be available, and even if they were, the diversion of effort from the unit's primary mission would be too great.

## 3.1.3. System development requirements

According to these criteria, the only type of systems developed by user departments will be those using development shells. These shells are designed to let non-programmers create useful applications in a matter of days, rather than the months required for conventional systems. Because they are so quick and easy to use, they permit the development process to take place interactively: pieces of the system are built and tested, revised, retested, etc., until the entire system is complete. While there are advantages to this approach, there are also dangers.

1. It is so easy to make modifications that the system may never be finished. If use of the system begins before modifications are complete, there may be data errors and/or analytic inconsistency. The manager should make sure that the end of development is clearly defined, and that thereafter modifications be handled in a controlled way.

2. For similar reasons, complete system testing may never be done. This should mark the end of the development phase.

Protection must be provided against accidental destruction of data. The backup procedures which protect mainframe users must be provided by the programmer. The solution may be as simple as providing for frequent backup on disks which can be stored in another room, or even taken home.

Security is required for data and programs. In the mainframe environment, security is provided by passwords, security codes, a security officer, etc. For microcomputer systems, it often suffices to remove disks and lock them in a desk drawer. With a hard disk system, the door to the computer room can be locked. However security is achieved, it should be designed when the rest of the system is designed, not grafed on later.

Documentation is probably the most neglected aspect of user-developed systems. The correct amount is usually much more than the users create but much less than ISD typically requires. The following is a reasonable set for most applications:

● a copy of the package documentation, or at least a record of name, version number, release date, etc.

\- a listing of the source code for the application.
- a set of operational procedures, including data entry, backup, etc.

Maintenance decisions should be made jointly by all users of the system. Maintenance procedures should be established at the time the system is put into operation, and rigorously enforced. These should include, at a minimum, parallel testing and complete documentation of each change including the date introduced.

The issue of connectivity (to other information systems) should be addressed at the time the system is planned. It is likely that any system of importance will sooner or later be connected to other systems. The planning may be as simple as choosing a package which has data interchange facilities. The most important aspect of this planning is to coordinate with central ISD.

## 3.2. Operations

The most significant difference between operations in an ISD and operations of a user-controlled system is that ISD recognizes that operations takes resources and management, and users often do not. A common view is that the operation of a microcomputer is such a small task that it can be a part-time task which requires no management attention after it has been assigned. User management must budget manpower for operations, and be prepared to manage the activity.

This management includes organizing for and enforcing the decisions made during the design of the system regarding system security, backup, and maintenance. It is worthwhile to repeat this commonplace assertion because while the information services professionals understand its importance and difficulty, most user managers do not. Until the first data loss or vandalism, it may all seem like technological overkill.

In addition to application system security, hardware security must be considered and managed. Security of a microcomputer may seem like a small thing compared to guarding a large mainframe installation; on the other hand, microcomputers are regularly stolen from offices, while there are at yet no reported instances of theft of IBM 3090s. The solution is simple once the problem is identified: lock the door, and make some one person responsible for access to the computer.

Operations continuity is much more important than most users realize. Again, the problems are easy to solve for micros, once they are recognized. Electric power sources can be filtered and uninterruptable power supplies are not expensive. Hardware maintenance can be hired on a contract basis, but there may be a much more straightforward answer: 100% equipment redundancy. With the hardware costs of many systems under \$10,000 duplicating equipment for critical systems may be very cost effective. Backup for disaster is also straightforward: copies of programs, data, and documentation must be made and stored off site; arrangements should be made in advance for immediate access to replacement equipment; and procedures for restarting the system should be organized and documented.

## 3.3. Telecommunications

Telecommunications can affect user-controlled systems in two ways: communications to mainframes, and local area networks joining parts of the user-controlled system. Micro to mainframe communication is necessarily handled by a central group. The user manager need only be concerned that system design decisions do not make it unnecessarily difficult.

On the other hand, local area networks (LANs) are often installed and operated by a user department. Typically, the user contracts with a vendor to design and install the network, and user management assumes that once the LAN is operating, no further attention is required. Experience proves otherwise. An operating LAN requires an administrator within the user department to assign addresses, admit new users to the system, manage a file server, etc. It also needs some engineering support to find and correct network problems; some of these are software and others are hardware. Providing this support is usually far beyond the technical competence to be found in a user department; it is usually best supplied by a central ISD or by an outside contractor. Either way, some internal effort will be required to interact with the support staff.

## 3.4. Technical support

These activities would be sufficient for acquisition and operation of a user-controlled information tion system, provided the system were completely stable: if requirements did not change radically, if volumes were constant, if no additional demands were placed on the hardware, etc. In fact, all of these things change over time, sometimes drastically. The user department requires technical support in the areas of capacity planning, hardware and software standards, and hardware and software migration planning. All of this support can best be provided by the central ISD, with one caveat: the user department must have at least one person on its own staff who is technically qualified to carry on a dialog with ISD on these topics and evaluate ISD's recommendations from a departmental perspective.

## 3.5. Personnel management

Recruiting departmental people into the information systems task should not be difficult. Most commonly, the initiative comes from the employee himself, as from Nerd in the parable. Otherwise, a call for volunteers usually uncovers someone eager to learn about computing. If no suitable candidate appears, help can be sought from ISD.

Training is readily available: from ISD, from outside vendors of training, and from outside vendors of hardware and software. As a result of prior experience, information systems professionals know how to learn a new system quickly and use it efficiently. User personnel do not have this skill. The most important thing for the departmental manager to do (beyond insisting on adequate training) is to make certain that those who are to build and operate the system be trained on the exact configuration, software and hardware, which will be used for the operational system. Changes in a new release of software are usually only a minor nuisance for a professional programmer; for a first-time user of computers, they may cause a major setback.

The management of the people who work on user-controlled systems is a knotty problem: although these people are doing work of importance to the department, they are out of the main line of the department's activities. They develop specialized computer skills, even as their departmental skills deteriorate. The better they become at the information systems task, the more their future careers are in doubt. This issue must be addressed in the early stages of the development of the first user-controlled system, or that system and all figure systems will suffer.

There are three possibilities. The first, and by far the best, is to staff the information systems activities with user department people, and make assignment to these activities a normal (perhaps a required) part of progression through the department. The second possibility is to recruit information systems professionals to perform these functions as a part of their information systems careers. If this option is chosen, they should be transferred to the user department for a predetermined period of time and then transferred back to ISD. The third possibility is the least desirable and, of course, is the most likely to occur without strong management direction. It is to assign departmental employees permanently to the departmental information systems activity. This creates the very serious risk that the information systems activity will become second rate, for it will be in the hands of people who are not longer departmental professionals and who never have been information services professionals. There are instances where this strategy meets the needs of both the department and the employee, but they are rare.

## 4. Conclusions and Recommendations

The idea of viewing user-controlled information systems as miniature information services departments provides a framework for analysis of the managerial issues involved in the building and operation of such systems. This analysis yields some important insights:

The building and operation of user-controlled information systems is a complex activity, despite an appearance of simplicity. This activity requires active and thoughtful management.

User-controlled systems are structurally similar to ISD systems, and their success requires dealing with the same problems. Although the problems are the same, the solutions are often quite different.

The information systems profession has focused its attention on the problems user-controlled systems create for the information systems professionals, and has not effectively addressed the problems of user-managers in managing their information systems activities.

These insights lead to recommendations:

1. The information systems profession should develop management methods and procedures tailored to the problems of user-controlled systems: systems which are small, and which are built and/or operated by non-professionals.

2. The information systems profession should take an active role in teaching these methods and procedures to the user community in general and to user managers in particular.

3. User managers should recognize that user-controlled information systems require management and should allocate the necessary time and resources to provide it.

## References

[1] Maryam Alavi, “End-User Computing: The MIS Managers’ Perspective”, Information & Management, Vol. 8, No. 3 (March, 1985) page 171.

[2] David H. Benson, “A Field Study of End User Computing: Findings and Issues”, MIS Quarterly, Vol. 7, No. 4 (Dec., 1983, page 35.

[3] J. Daniel Couger, “E Pluribus Computum”, Harvard Business Review, Vol. 86, No. 5 (Sept.-Oct., 1986) page 86.

[4] Dennis M.S. Lee, “Usage Pattern and Sources of Assistance For Personal Computer Users”, MIS Quarterly Vol. 10, No. 4 (DEc., 1986) page 313.

[5] John A. Lehman, “Personal Computing vs. Personal Computers”, Information & Management, Vol. 9, No. 5 (Dec., 1985) page 253.

[6] Robert L. Leitheiser and James C. Wetherbe, “Service Support Levels: An Organized Approach to End-User Computing”, MIS Quarterly, Vol. 10, No. 4 (Dec., 1986), page 337.

[7] Henry C. Lucas, Jr., “Utilizing Information Technology: Guidelines for Managers”, Sloan Management Review, (Fall, 1986) page 39.

[8] F. Warren McFarlan and James L. McKenney, “The Information Archipelago - Governing the New World”, Harvard Business Review, vol. 83, No. 4 (July–Aug., 1983) page 91.

[9] Donna Raimondi, “Hot Sites: Disaster Plan Douses Flames”, Computerworld, Vol. XX, No. 46 (Nov. 17, 1986) page 1.

[10] Rita Shoor, “MicroManagers: New Skills & Problems”, Infosystems, Vol. 33, No. 1 (Jan., 1986) page 48.
