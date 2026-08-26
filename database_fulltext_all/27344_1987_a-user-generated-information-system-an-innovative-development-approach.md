---
otero_id: 27344
otero_key: "AZHUCN3R"
title: "A User Generated Information System: An Innovative Development Approach"
authors: "Kenneth A. Kozar; John Μ. Mahlum"
year: "1987"
journal: "MIS Quarterly"
doi: "10.2307/249358"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A User Generated Information System: An Innovative Development Approach
Author(s): Kenneth A. Kozar and John M. Mahlum
Source: MIS Quarterly, Vol. 11, No. 2 (Jun., 1987), pp. 163-174
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249358
Accessed: 28-12-2015 05:37 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A User Generated Information System: An Innovative Development Approach

By: Kenneth A. Kozar
University of Colorado/Boulder
College of Business/MSIS
P.O. Box 419
Boulder, Colorado 80301

By: John M. Mahlum
Mahlum and Associates
8821 Penn/Lake Circle
Minneapolis, MN 55431

## Abstract

This article details a project which used a non-classical approach to developing information systems. A critical but backlogged information management project, representing \$13 million in payments due to clients, is described. Up-to-date payment processing would provide information valuable to generating increased organization revenues. The backlogged project was given life by having the users, with tutoring and guidance, perform tasks usually assigned to systems analysts. These tasks included the building of an information system about the system. The article presents the project scenario, describes the development approach used, evaluates the approach and why it worked, and suggests why other organizations could benefit from using the approach.

Keywords: Structured systems analysis, information requirements, user developed systems

ACM Categories: D.2.2, J.1, K.6.1

## Introduction

The 3M Company Health Care Products Division is one of the companys' 40 divisions. Each of the divisions is run as a near autonomous business. National Accounts, a part of Health Care Products, is responsible for promoting the sale of health care products to hospitals who are members of purchasing groups. These groups give member hospitals special considerations, including rebates on certain products or for quantity purchases. This approach helped 3M survive increasing competitive pressures. While this business strategy of using rebates increases sales and gives a competitive advantage, it brings with it special information processing needs.

The growth in Health Care Products sales and rebates was substantial. The business success caused tremendous rebate processing overloads. There also were increased demands for information from the rebate data. The existing rebate processing/sales reporting system quickly grew, resulting in fragmented processing done in several physical locations. This included both internal processing and use of a service bureau. Computing costs alone were running thousands of dollars a month.

The existing system was in need of attention. The five persons doing rebate processing entry could not keep up. The organization owed their product dealers \$13 million dollars for contracted rebates. The dealers were even starting to deduct unprocessed rebates due to them from payments to Health Care Products.

The existing system was very inefficient. Poor inputs meant many manual lookups in outdated tables that contained inconsistent and redundant data. The stages of computer processing were divided between three different computer systems and used two different programming languages. Interfaces between the systems caused many headaches since hard storage media, rather than telecommunications, was used to exchange data. There was a need for streamlining and consolidation of the actual processing.

Besides the processing deficiencies, the system allowed no real query capabilities or expedient means for report generation. Report generation by the service bureau was done by “cannibalizing” existing programs. The set of programs were added to as needed to get an information request satisfied. Attempts to focus sales efforts suffered because of untimely or nonexistent information. The lateness of the processing meant generated reports were history, not stimuli for action.

There was little overall system structure or coherence recorded except in the minds of the users. They had a good “picture” of the structure of the system. This mental documentation went home each night. Other documentation was scattered, considered personal, or non-existent.

The National Accounts Manager was confronted with the problem. He felt there was a need to study the existing system to consolidate the scattered portions and at the same time use newer technology. Security concerns worried him due to all the physical data movement and processing by different groups. Productivity was suffering and many of the workers felt “there had to be a better way.” But before we can describe the solution there is a need to understand the problem and opportunity.

## The Project Scenario

The next sections describe the needed systems project, classical alternatives for completing the project, and the non-classical, innovative approach chosen.

## The system-problem and opportunity

The Rebate/Sales Reporting System is not a typical system found in most organizations. It is meant to support a particular business strategy that is appropriate for some industries and markets. Figure 1, a context diagram created by users during system development, will aid in understanding the system. The diagram exhibits the links with other systems and sources/destinations of data. The lines with arrows indicate data flows between entities, shown as squares on the diagram. The following process was diagrammed:

Purchasing groups of hospitals were formed to allow hospitals to increase purchasing power. 3M's purpose in negotiating purchasing agreements with the purchasing group was to provide incentives to hospitals to buy health care products. The incentives were in the form of discounts the hospitals received from selected dealers as a result of being a member of a purchasing group. Discounts were received on specific products, for volume sales, for agreeing to commit to a 3M product (standardization), and for just being a member of a purchasing group.

3M agreed to protect dealers from losing money from the company's action in negotiating the purchasing agreement. This price protection was offered through rebate credits made to dealers by the company.

The dealers made rebate requests to 3M National Accounts. The dealers provided proof to National Accounts of discounts given to hospitals with documents indicating sales of products to individual hospitals. This proof was verified by National Accounts, and if approved, a rebate credit request was made to 3M credit/billing who issued rebate credit notices.

In some cases, dealers made payments to credit/billing which deducted the expected rebate. In this case, credit/billing issued a payment shortage notice. National Accounts verified these payment shortage notices, and ensured the rebate credit request from dealers included the deduction already taken.

Hospitals also made direct orders to a 3M sales branch, rather than through a dealer. National Accounts had to be aware of these direct orders since they contributed to sales volume which affected discounts.

3M marketing notified the system if any price or product changes took place. The system provided information to national accounts management, purchasing groups, dealers, and the sales branch. An important type of reporting was a sales recap which specified sale dollars of health care products for each hospital. Another report was the hospital net price report which indicated whether dealers were abiding by the purchasing agreements.

Thus, the National Accounts' Price Protection/Rebate/Sales Reporting System was critical to maintain a competitive advantage and to provide timely information to focus revenue generating efforts by sales personnel. Without the information from rebate processing, the company would not really know which hospitals were buying its products since most purchases were made through dealers.

![](/api/attachments/AZHUCN3R/fulltext/images/6359483ee0abd9d7837a844941612aff8c1e5b5e5b358451a4edcd160f1b440f.jpg)  
Figure 1. Context Diagram of Rebate Processing/Sales Reporting System

The question was how to proceed with bringing this system up-to-date, to handle growing volumes of rebates, and to provide the information needed to focus sales efforts. To answer this question, the project sponsor began by examining the classical alternatives.

## Classical alternatives

Neither the project sponsor nor the user group had any preconceived notions as to how systems should be developed. Several classical approaches were considered once the project was made a priority. Possibilities included:

1. Classical Life Cycle Development—The user who was the project sponsor approached the centralized systems development group with a project proposal. This group works under the marketing philosophy of satisfying the wants and needs of their customers. But, as is often the case in the information systems field, resources were too limited and demand for services so great that the project had to wait for resources to free up. The sponsor was disappointed with this response, but the needed systems development resources did not exist within the organization. It became clear that the classical life cycle with traditional roles played by systems developers and users was not possible due to the backlog problem.

2. Packaged Software—Investigations were done of user associations and vendors. The problem was unique enough that there were no general packages that could be adapted to provide a solution.

3. Classic User Developed—The users had no desire to become technically involved, nor was this determined to be a good use of existing strengths.

4. Prototyping—This approach requires existing data resources to be in order and to have skilled users of fourth generation languages [7]. This was not the case in this situation.

5. Outside Developers—It was possible to bring in an outside consultant, but having the entire systems development effort completed by an outside group was much too expensive and would set an unacceptable precedent.

Upon examining these approaches the users decided they needed guidance in dealing with the problem. They felt there may be another way to proceed.

## An Innovative Approach

With outside help and sanction of the information processing group, an innovative approach was attempted. It used a chief developer team based on the chief programmer team approach [1]. Most of the team members were not trained systems persons. They were knowledgeable members of the user group, tutored to define and document the existing system and its deficiencies.

There was no initial emphasis on building the physical system. In fact, this consideration was delayed as long as was feasible. With the quickly changing technological environment, no emphasis was put on selecting hardware, building or acquiring software, or acquiring a physical site or facilities. The emphasis was on recognizing and defining the problem/opportunity, not on solving the problem.

## New roles for

## development participants

This redefinition of the typical systems development effort led to new role definition for development participants. The systems unit would focus on the physical design only after the problem was defined. The users would, with help, build models of the existing system and of new requirements. The requirements would be stated in common business terms emphasizing profit motives (see Figure 2).

The backgrounds of the user participants included no training in computer technology or systems development. They were trained in their functional areas, and had no real interest in being “systems people.” Each of the participant groups will be described.

![](/api/attachments/AZHUCN3R/fulltext/images/88bc448e015ce3468c64ee76acb48fc527a5c5eb00321aaf94a98f4d03588c11.jpg)  
Figure 2. Roles and Results of Key Development Team Members

The user developer responsible for developing the models of what the system did and must do was a supervisor who understood the entire system. She quickly learned structured development techniques and was able to assist in developing and evaluating the models of the system. She was the primary liaison with the technology experts.

The primary sponsor of the project was the National Accounts manager who assured that resources were available to accomplish the project. He understood the business reasons for the system and was invaluable in developing the models of business requirements for the system. He had no background in systems or technical matters, but believed that technology could improve system performance that would aid workers in performing business tactics.

Two user managers with some systems background were invaluable in an advisory and organizing capacity. They set up and assisted in much of the requirements definition.

After the project proceeded for four months with only advisory and review assistance from the technical systems group, a systems professional was assigned to the project. This person had considerable experience in systems development and programming. He was brought up-to-speed with the developed documentation and assumed increasing responsibility for the project as the consultant who served as “chief developer” was phased out. Physical design of the system and programming proceeded and versions of the system were developed and implemented. The entire project spanned a period of about eighteen months.

A new role was that of chief developer. This person was an outside consultant who performed the following activities:

\- coordinated the systems development process,

\- “catalyzed” role players to build a team, - trained users in techniques of building non-physical models,

\- tutored and consulted with users to build actual models,

\- focused on linkage between business strategy and information system strategy.

The chief developer DID NOT DO:

\- computer programming,

\- hardware/systems software selection,

\- user manual or screen layout development,

\- training in use of the system.

The first two items above were done by the corporation's systems professionals and the last two were done by the users. This aligns with Rivard and Huff's belief that:

"With respect to user developed applications, the role of DP changes from providing the core development expertise to providing assistance, education, access to development tools, to computing resources, to data, etc. That is, the DP department becomes a system facilitator instead of a system developer," [10, p. 90].

The chief developer spent less than fifteen total days on the project, periodically doing training, tutoring, giving direction and aiding in reviews.

The chief developer gave specific assignments to the users. Once the users had constructive feedback from the systems people and the confidence that they were making distinct progress and contributions, the project perpetuated itself through the user efforts. The systems unit was kept informed of progress, and aided in defining the system requirements and in making contacts to link to the other organization members. A description of the activities follows.

## Building the information system

One of the critical tasks of the user group was to build a systems development database (known to many as documentation), providing information for systems professionals to make decisions on system design and implementation.

The users, with the help of the chief developer, built a database which included:

• WHO was involved with the system
Organizational Units
Organizational Positions

![](/api/attachments/AZHUCN3R/fulltext/images/4afc174f3b70a8f6d8667b93e7ebb3e96f4f0a978182ec76d4ce83fe1051c445.jpg)  
Figure 3. Activities and Results of Development Team

External Entities - WHAT the system did
Processes/Subprocesses
Data Stores
Data Flows

• WHAT data was required
Data Structures
Data Elements

\- WHAT the users could not do that they would have liked to do and the information needed to do it
Business Tactics
System Objectives

\- WHY this was needed in "bottom line" business terms.

Business Objectives

New and evolving subsystem modeling techniques were used. The following sections will detail how these models provided data which linked the entities that are listed above.

Figure 3 shows the sequence of the model building and the results that were stored in the systems development data store. This was systems development documentation being created as a by-product of the systems development activities. This project had no development activity formally called “documenting.”

## The Context Model

An organizational and environmental context model detailed who was involved with the system. The relationships among the different units were specified and formally reviewed. This information served as a directory of who should be interviewed, trained, part of a review team, etc.

The diagram that served as a critical part of describing this subsystem is the context diagram shown in Figure 1. As well, an organization chart showing organization units and positions within the system was developed.

## The Logical Flow Models

Logical models in the form of data flow diagrams and data dictionaries detailing what data were developed by the users with the aid of the chief developer who acted as a tutor on systems development techniques. Once developed, the models were presented to and reviewed by several levels of managers in different functional areas.

The techniques used, such as data flow diagrams and formal data “encyclopedias,” did not evolve until the late 1970’s, preventing this approach from previously being feasible.

The techniques are becoming more accepted today and even are supported by automated systems development workbenches. The reason the approach is feasible for users is that no knowledge of technology or programming is needed. Graphic approaches, like system flowcharts, focus on physical representations and are composed of “visual jargon” that users cannot identify with. (See $[2, 4]$ for more details on these techniques.)

Data flow diagrams were a key portion of the models. They served as the index to any existing or developed system documentation. A portion of one of the user developed diagrams is shown in Figure 4.

Four basic symbol types are represented: a square representing a source or destination of data to or from the system: a rounded-corner rectangle representing the processing of data; an elongated rectangle representing the storage of data; and a line representing the flow of data with an arrowhead indicating direction of flow.

The diagram was created and owned by the user group. They understood it and could use it to explain the system. These were not documents to be used only by professional systems analysts.

The data dictionary was more than an element description and directory. It was more of an encyclopedia about the sytem. It expanded on the data/processes/persons-positions-units denoted in the data flow and context diagram. This led to standardization of names and identification of aliases (same things called by different names).

## The Requirements Models

Requirements models detailing why the system was needed were developed by the users. A requirements dialogue technique, and what the organization called “wishing sessions,” were the methods used.

![](/api/attachments/AZHUCN3R/fulltext/images/92e06649a701989032fed709d3e80dc3856ea1c0617ed2293980bb4cd7f99277.jpg)  
Figure 4. A Data Flow Diagram Segment

The requirements models linked:

Business Objectives—desired business accomplishments expressed in terms of reduced costs or increased revenues.

Business Tactics—business actions done in order to accomplish the business objectives.

System Objectives—system achievements (reports/screens) to support the business persons in performing the business tactics.

These requirements would allow a systems person to specify potential system tactics to allow the system to achieve its objectives.

The following is an example of the relationships between these factors:

Business Objective—Increase sales revenue of Health Care Products by 5% from Purchasing Groups not fulfilling current Purchasing Agreements.

Business Tactic—Identify hospitals not purchasing specific 3M products as agreed, and contact them regarding these deficiencies.

System Objective—Produce a quarterly sales recap, identifying hospital purchases of each health care product within 30 days after end of the quarter.

## Review

It becomes clear from the above statements what the system must accomplish (system objective), and why it must do it (to support business tactics, allowing achievement of business objectives). Note that the objectives are stated in measurable terms making it possible to know when a business or system objective is reached.

Sets of these types of relationships were established for all the organizational units and positions concerned with the system, including credit, billing, sales, and marketing units. All of this work was within the capabilities of the users.

The “wishing sessions” were group brainstorming sessions where the participants “ideal” results from the potential system were described and recorded. These free thinking sessions promoted system acceptance and needs identification that enhanced final system quality.

The systems professionals were part of the review teams that examined the completed models. The models that were developed were to serve as their information system, allowing them to design system tactics which would meet system objectives.

Project management and audit activities were done informally by keeping a chronology of significant events and reviewing it as the project progressed. This allowed learning from past problems and avoided potential delays in getting future tasks done.

## Design and Implementation

Once the users built the three models that described who/what/why, the systems professionals built the fourth model that included how the system would be implemented. They could do this because they had a database about the existing system and its deficiencies. The new systems design was done with excellent information. This approach drew on the thinking of Howden who supports the building of a systems development database rather than the linking of systems development tools. Howden states:

"The database provides an integrating and unifying medium for interfacing tools without forcing them into a complex structure of interrelationships. Tools obtain their information from the database and return their results to it without having to interface directly with other tools" [5, p. 326].

Once the database was completed and a basic design specified, a fourth generation language was used to program the system. But, the programming was not done by the users. The software was written predominantly by systems professionals, in conjunction with the users.

At this point, the systems professional primarily responsible for the development effort took over the continued development of the system. He became the manager of the group responsible for processing rebates. The team of user/developers was so cohesive that this move was well accepted. The systems professional understood the business functions as a result of the information created and shared by the user groups. The users felt comfortable with the systems person since they had "trained him." This is in line with 3M's personnel policies where a new product's creator can become the department's manager. The company's former CEO and chairman Lewis Lehr called this "individual entrepreneurship." This may well be adaptable to solving the often stifling career path of the systems professional who is seen as a technician and not allowed a role in the business [see 8, p. 85].

The developed system is currently in place. Through streamlining of the old system as an interim solution/version, the several month rebate processing backlog has been eliminated. This version was not intended to be the final solution, but an interim solution/prototype that would be replaced with an enhanced system version. The “final” solution has increased machine activities that would assume the tasks done by humans in earlier versions.

## Impact/Results

Managers have been impressed by the efforts. A comment was made that it was “unbelievable that the systems team had unraveled in weeks what it had taken years to patch together.” System versions have allowed an elimination of the rebate processing backlog and improved decision making performance. This has resulted in increased sales revenues.

This success story demonstrates that systems work can be done by users. The users not only accomplished the task, but it is believed that they did it very efficiently. One reason for this was the reduced need to pass information about the system from the minds of users to the minds of developers. Much of the communication took place on paper with the models the users had built. This is more than just “substitution” of persons having analysis skills. It includes a superior means of representing systems by those persons who understand their business functions.

The development approach used has had an impact on several groups. Persons involved with the effort have reviewed the process and circumstances that led to success of the development. Other systems development teams have viewed the successful effort to determine why it worked so well. The approach has been reviewed by several other organizations where users have encountered similar problems.

Since the system has just recently been implemented, it is too early to have explicit, quantitative results. It is expected that the system slowly will have an influence on sales management's business tactics which will affect the bottom-line business objectives. Progress is apparent in the following areas:

1. Customer satisfaction

2. Cash flow improvement

3. Data analysis

4. Managerial decision making

5. Personnel productivity.

Further details, however, are confidential.

## Why did the innovative approach work?

This is a case of users taking a committed role in the information systems development process. They had no preconceived notions about the proper way to develop systems or about technology. Their concern was threefold:

1. An accurate definition of the problem

2. A viable solution

3. An effective implementation of a solution.

The users' thorough and accurate problem definition clearly documented the system needs and the link to the business objectives and tactics. This linking approach gave users the opportunity to concentrate on their strengths and contribute to project success. Following is some discussion of why the innovative approach worked.

Problem first, then the solution—The users had no preconceived notions about technology. This resulted in no solutions looking for a problem, but a thorough and complete problem definition. There were no “pet” solutions advocated by technical persons or vendors.

System ownership—Because the users had done all of the work to document the existing system and new needs, they were not going to abandon the project. They knew they had to stay involved, but also knew a team effort was required for success.

Everyone wins—The business and system objectives identified in the project included both potential cost savings through efficient operation of the system and, more critically, increased revenues that would result from better information. The sales persons would be rewarded with increased commissions and the systems persons could feel they contributed to the company's success.

The critical success factors of the revenue producers (sales force) were addressed (see $[12]$ for a summary of critical success factors). The sales staff critical success factors included determining to whom they should be selling, what products they should be promoting, gaining credibility by having information on what was sold, and knowing what sales volume agreements were not being met. Intuitive models of sales potentials were documented, developed, and implemented.

The critical success factors of the systems personnel involved with the project were also considered (see [9]). These included having systems development successes, enhancing human resource development, and the need to support the relationship with users and their objectives. An overall project goal was to make everyone a winner.

Using the strengths of unlike groups—The approach of using the system users to document the system—build an information system about the system—is using the strengths of the user groups. They are not programmers, but are systems people in the sense that they understand their system. What they need are some tools and techniques to record their systems views so that those views can be shared with persons who have more technical knowledge.

Likewise, the systems developers were not experts on the existing system and its deficiencies. But they could propose alternative designs using modern technology, once they understood the problem and its environment.

Allowing personal growth—The users of the system had no real desire to be current on state of the art computing technology. But the systems developers did have this desire. They wanted to know about the capabilities of the newest releases of hardware/software/communications. The innovative approach allowed this since the systems developers had to examine available technology to propose system tactics.

The users had a real need to know what the health care product competition was doing. They were much more concerned with their business than the business of computing. Again, this drew on the strengths and interests and critical success factors of each of the unlike groups. This is a clear case of letting people do what they like to do and can do best.

## "Reapplicability"-will the approach work elsewhere?

This concept of having users build the information base needed for systems developers to develop the technical components of an information system has wide applicability. Users can contribute to the process if they know what to do and what questions must be answered. The process is not performed in a cookbook fashion. Different users may end up using different processes but will end up with the same final product—information documentation. This will help the systems professional to use his/her technical strengths to complete the project.

To allow users to build the models of the system, there is a need to commit to the structured approach of systems development and to create a comprehensive system dictionary. Users may have to be trained, or if persons exist who understand structured methodologies, tutored to allow creation of flow models. An organization may find new organizational roles will be needed. Chief developers who can lead development efforts and systems development database librarians (dictionary builders), may be needed to manage the information being collected, especially if automated storage is used.

This approach has widespread applicability for other organizations. No major expenditures are needed, only a dismissal of ritual (see $[11]$ ) and a change in beliefs and attitudes. It requires using the strengths of users to perform roles not typically assigned to them. Adopters of the approach must believe that users understand their own system and can develop documentation of value for the systems professionals.

## Conclusion

Many of the key information systems management issues from an SIM sponsored research project are addressed by use of this approach $[3]$ . Information system (IS) planning through linking IS/corporate strategies, end-user system developing, improved software development and quality, improved IS productivity, organizational learning about computing, and wise use of IS human resources are “top ten issues” from the above study that this approach addresses.

More time should be spent teaching user groups how to define problems or to describe the environment of the problem than in applying technology to the problem. Developing subsystem models with the aid of a chief developer is one means of accomplishing this. But commitment must be made to supporting the chief developer concept. This person would ideally fit in an information center environment, and could be viewed as an internal consultant. This may be an ideal place to position MBA-MIS majors who are not technicians, but clearly understand information capabilities and how they can support business strategies. Educators might think about this focus when designing or revising curriculum.

The user role in this was not end-user computing, but was end-user developing $[13]$ . Users do not have to be programmers. They do need to clearly define their problems/opportunities. User involvement has been widely suggested. Building a series of models that would provide information for systems developers is a means of accomplishing this end. This is possible due to the evolution of the modeling techniques. Building the models will result in systems that help achieve business goals.

## Acknowledgements

The authors would like to thank Jody Janski for her special attention and devotion to the project and Don Kilberg for his persistence in seeing the project through to completion.

## References

[1] Baker, F.T. and Mills, H.D. "Chief Programmer Teams," Datamation, Volume 19, Number 12, December 1973, pp. 58–61.

[2] De Marco, T. Structured Analysis and Systems Specification, Yourdon Press, New York, New York, 1979.

[3] Dickson, G.W., Leitheiser, R.L., Wetherbe, J.C., and Nechis, M. "Key Information Systems Issues for the 1980's," MIS Quarterly, Volume 8, Number 3, September 1984, pp. 135–159.

[4] Gane, C. and Sarson, T. Structured Systems Analysis, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1979.

[5] Howden, W.E. "Contemporary Software Development Environments," Communications of the ACM, Volume 25, Number 5, May 1982, pp. 318–329.

[6] Janski, J.A. "User Model Number 1," Internal 3M Document, 1984.

[7] Jenkins, A.M. "Prototyping: A Methodology for the Design and Development of Application Systems," SIM Spectrum, Volume 2, Number 2, April 1985.

[8] Marth, D. "Keeping All the Lines Open," Nation's Business, Volume 72, Number 10, October 1984, pp. 85–86.

[9] Martin, E.W. "Critical Success Factors of Chief MIS/DP Executives," MIS Quarterly, Volume 6, Number 2, June 1982, pp. 1–9.

[10] Rivard, S. and Huff, S.L. "An Empirical Study of Users as Applications Developers," Information and Management, Volume 8, Number 2, February 1985, pp. 89–102.

[11] Robey, D. and Markus, M.L. "Rituals in Information System Design," MIS Quarterly, Volume 8, Number 1, March 1984, pp. 5–15.

[12] Rockart, J.F. "Chief Executives Define Their Own Data Needs," Harvard Business Review, Volume 49, Number 2, March–April 1979, pp. 115–126.

[13] Rockart, J.F. and Flannery, L.S. "The Management of End User Computing," Communications of the ACM, Volume 26, Number 10, October 1983, pp. 776–784.

## About the Authors

Kenneth A. Kozar is an Associate Professor of Information Systems at the University of Colorado/Boulder. He has held practitioner positions in information systems as well as being on the faculties of several universities. His research interests include innovations in systems analysis and design and communication between members of development teams.

John M. Mahlum is President of Mahlum and Associates, a consulting company specializing in strategic management. He served with the 3M Company for 38 years, including the position of National Accounts Manager for Health Care Products, before founding his own company.
