---
otero_id: 24935
otero_key: "ZGD4J8N8"
title: "Enabling the Effective Involvement of Multiple Users: Methods and Tools for Collaborative Software Engineering"
authors: "Douglas L. Dean; James D. Lee; Mark O. Pendergast; Ann M. Hickey; Jay F. Nunamaker"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518180"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Enabling the Effective Involvement of Multiple Users: Methods and Tools for Collaborative Software Engineering

Douglas L. Dean, James D. Lee, Mark O. Pendergast, Ann M. Hickey & Jay F. Nunamaker Jr.

To cite this article: Douglas L. Dean, James D. Lee, Mark O. Pendergast, Ann M. Hickey & Jay F. Nunamaker Jr. (1997) Enabling the Effective Involvement of Multiple Users: Methods and Tools for Collaborative Software Engineering, Journal of Management Information Systems, 14:3, 179-222, DOI: 10.1080/07421222.1997.11518180

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518180

![](/api/attachments/ZGD4J8N8/fulltext/images/95aa34cc7ba8bda144d91f6c28a96493e95c762a0883b80b91b102f4c5d0ec30.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/ZGD4J8N8/fulltext/images/d25bf996d517fd47e30e0828508ae7edb7eae75fc94217c91dd6de5258940813.jpg)

Submit your article to this journal ↗

![](/api/attachments/ZGD4J8N8/fulltext/images/7f8c152ae4dcd384ac90fcc639137b9ffb2ec4a0893acaee89c3eb259584b250.jpg)

View related articles ↗

![](/api/attachments/ZGD4J8N8/fulltext/images/15e15a627a51ce2bf639a0d32e86d367547af4314d65cfe8b2270d7d7e7a8647.jpg)

Citing articles: 11 View citing articles ↗

# Enabling the Effective Involvement of Multiple Users: Methods and Tools for Collaborative Software Engineering

DOUGLAS L. DEAN, JAMES D. LEE, MARK O. PENDERGAST, ANN M. HICKEY, AND JAY F. NUNAMAKER, JR.

DOUGLAS L. DEAN is a Research Scientist at the Center for Management Information at the University of Arizona. He received his Master of Accountancy with an emphasis in information systems from Brigham Young University in 1989 and his Ph.D. in MIS from the University of Arizona in 1995. His research interests include electronic meeting system support of modeling, business process improvement, and information systems requirements collection. He also facilitates meetings in these areas. His interests also include systems analysis and design methods. His work has been published in Management Science, Journal of Management Information Systems, Group Decision and Negotiation, IEEE Transactions on Systems, Man, and Cybernetics, ACM SIG Group Bulletin, and multiple conference proceedings.

JAMES D. LEE is a Research Scientist in the Center for the Management of Information at the University of Arizona. He received his B.S. in accounting and a Master of Accountancy degree with an emphasis in information systems from Brigham Young University in 1989, and a Ph.D. in MIS from the University of Arizona in 1995. His research interests include computer-aided business engineering, electronic meeting support for activity/data modeling, business process reengineering, systems analysis and design, database management, and activity-based costing. He has developed software prototypes to support activity and data modeling in an electronic meeting systems environment. His work has been published in the Journal of Management Information Systems and the ACM SIG GROUP Bulletin, and also in several conference proceedings.

MARK O. PENDERGAST is an Assistant Professor in the Management and Systems Department, College of Business and Economics, at Washington State University. He received his M.S. and Ph.D. degrees in MIS from the University of Arizona in 1982 and 1989, respectively, and a B.S. in electrical computer engineering from the University of Michigan in 1979. Prior to moving to WSU, Dr. Pendergast was on the faculty of the University of Florida and worked as a systems analyst and lead engineer for Control Data Corporation and Harris Corporation. Dr. Pendergast's research

Acknowledgments: We would like to recognize the following individuals and organizations for their vital roles in enterprise analysis research and for their contributions to this paper: Douglas R. Vogel, Richard E. Orwig, Boris Nevstrujev, Nina Katic, Bill Saints, Mark Bovelsky, Lynne Mikulich, Ventana Corporation, the U.S. Army Environmental Center, the DoD Environmental Security Corporate Information Management Program Management Office, and the U.S. Army Waterways Experimental Station. This research was sponsored by the Army Environmental Center.

interests are in electronic meetings systems, groupware, business process reengineering, and systems analysis. His work has been published in the Journal of Management Information Systems, IBM Systems Journal, Journal of Computer-Supported Cooperative Work, and ACM Computer Communications Review, as well as in several books and conference proceedings.

ANN M. HICKEY is a doctoral candidate in management information systems at the University of Arizona. She received her B.A. in mathematics from Dartmouth College in 1977 and her M.S. in management information systems from the University of Arizona in 1990. Prior to beginning her doctoral studies, Ms. Hickey worked seventeen years as a program manager and senior systems analyst for the Department of Defense. Her research interests include collaborative requirements elicitation, business process reengineering, systems analysis and design, and electronic meeting support for activity and scenario modeling.

JAY F. NUNAMAKER, JR. For biographical sketch, please see the Guest Editors' Introduction.

ABSTRACT: The paper presents results of ongoing research to support effective user involvement during systems development projects. The Collaborative Software Engineering Methodology is presented as a framework that contains mechanisms to support three layers of user involvement: selected user representatives, user groups, and the broader user community. Productivity and user participation of traditional group meetings have been limited by chauffeured facilitation and by support of single-user tools designed for analysts rather than users. The paper introduces electronic meeting systems (EMS) modeling tools designed to allow users to work in parallel to contribute directly during meetings. These tools are easy to use while containing support features traditionally associated with CASE tools. The methodology includes a sequence of requirements abstractions that users engage directly including activity models, data models, scenarios, system use cases, and prototypes. This methodology is designed to help organizations respond to today's rapidly changing information processing needs.

KEY WORDS AND PHRASES: activity modeling, data modeling, electronic meeting systems, enterprise analysis, group support systems, groupware, IDEF, information systems requirements, JAD, software engineering.

ALMOST WITHOUT EXCEPTION, PRODUCTS AND SERVICES TODAY depend on high-quality information systems. Information systems and electronic networks enable us to buy tickets on airplanes that rely on computers for navigation and air traffic control. Computer systems automatically deposit our paychecks, pay our mortgages and utility bills, and invest our money. One cannot use a telephone, cash a paycheck, heat leftovers, or enroll a child in school without interacting with a computer. Vital as information systems are to our everyday life, the process of creating systems has been plagued with excessive costs, delayed releases, and the production of faulty, bug-ridden products. Much of the blame for this has been placed on inaccurate, unstable specifications for projects with unreasonable budgets and time schedules. This is largely the result of systems developers' inability to effectively involve end users in the development of detailed, adequate specifications. As Boddie [4] aptly put it:

Most programs spring from truly wretched specifications, if, indeed, there are any specifications at all. Throughout the development process, users, programmers, and analysts are engaged in a ritual dance of successive approximation to the required product.

In recent years industry professionals and academic researchers have made progress toward ending this “ritual dance” by developing advanced systems analysis and design techniques that use formal modeling methods in an automated, collaborative environment. Methodologies such as joint application design (JAD), rapid application development (RAD), information engineering (IE), and object-oriented analysis have been shown to improve design quality and reduce project duration. These techniques have in common an effort to reduce costs and time requirements through automation, reliance on the effective use of teams, and the involvement of end users at various stages of the project life cycle. While these new methodologies have been successful in addressing symptoms of the overall problem, they have realized only limited progress in achieving these objectives.

The major challenge that remains is to discover a way to combine the best elements of these promising techniques into a single methodology. The initial success of using techniques such as JAD and RAD for the development of small systems demonstrates a clear need for an overall methodology that includes a sequence of requirement elicitation, validation, and prioritization events that can effectively support multiple users. What are key attributes of a collaborative software engineering methodology that will enable effective and efficient involvement of groups of users? Is it possible to create requirements abstractions that are user-centered and at the same time give developers what they need to understand requirements? What mix of user/analyst/developer/facilitator interaction techniques and software tools will best leverage work from single users, small groups, and large groups throughout all phases of systems development, especially for large, complex systems? These are important questions that must be answered in order to create a new collaborative methodology.

This paper presents results from an ongoing research project at the University of Arizona that is working to create collaborative groupware tools, procedures, and facilitation techniques that will enable groups of end users to participate effectively in all phases of the software engineering process. We first look back at significant advances in the systems development process and then propose a new methodology, the Collaborative Software Engineering Methodology, that combines advanced group collaboration techniques with the best elements of systematic reuse, data integration, and rapid prototyping methods in order to produce integrated and interoperable systems. This is followed by an in-depth discussion of how such integration was accomplished for activity-modeling and data-modeling phases. We conclude with a discussion of lessons learned from applying collaborative design techniques to real-world groups, a summary of the contributions of the Collaborative Software Engineering Methodology, and an overview of future research directions.

## The Search for a Solution

THE TRADITIONAL SYSTEMS DEVELOPMENT LIFECYCLE (SDLC) developed in the late 1960s has long been held up as the standard by which alternative software development methodologies are judged, and, despite its many flaws, the SDLC or one of its many variations remains the most widely used development methodology [60]. In his discussion of the SDLC, Yourdon points out many of the weaknesses of the methodology, the most important of which are:

\- Nothing is demonstrable until near the end of the cycle.

\- It depends on correct, stable requirements.

\- It delays detection of errors until implementation.

\- It does not promote software reuse.

\- It takes too long.

\- It is generally not practiced in a formal fashion.

In addition to the well-known shortcomings pointed out by Yourdon, the SDLC does not recognize an organization's information systems development as an ongoing activity. Instead, it is designed around a single project that has a defined beginning and end. This orientation involves end users only at the beginning and the end, does not promote integration with existing applications, inhibits data standardization, and does little to promote long-term business process or activity analysis.

Brooks [9] describes the typical software development project as a potential monster (or werewolf) waiting to be conquered by a magical “silver bullet”:

The familiar software project, at least as seen by the non-technical manager, has something of this character (werewolf); it is usually innocent and straightforward, but is capable of becoming a monster of missed schedules, blown budgets, and flawed products. So we hear desperate cries for a silver bullet—something to make software costs drop as rapidly as computer hardware costs do.

Over the years computer professionals have addressed these problems by means of a combination of alternate methodologies and software tools that automate portions of the methodology. While none of these alternatives has yet been shown to be the “silver bullet” that can solve all the ills of systems development, they are steps in the right direction. We will begin by looking at research that has defined formal constructs and automated software tools for systems development.

## Formalization and Automation

A stream of research that began with the development of the first computer-aided software engineering (CASE) tool, PSL/PSA [56], and later evolved into PLEXSYS [39] formalized systems development activities through a set of integrated software tools. PSL/PSA consists of computer-aided structured documentation and analysis techniques that were developed for requirements elicitation and the preparation of functional specifications for information systems. PSL, or Program Statement Language, was a syntactically analyzable specification language for describing systems.

PSA, or Problem Statement Analyzer, used the PSL scripts to generate summary and reference reports. PSL/PSA advanced the state of systems development by creating an environment where a system design could be stored and checked for completeness and consistency and strongly influenced later structured analysis methodologies such as Ross's [53] Systems Analysis and Design Technique (SADT). PSL/PSA enjoyed a large following in the federal government and had strong patches of support at IBM, AT&T, and many other Fortune 500 companies. However, by today's standards, creating the PSL scripts could be as involved as writing the final programs themselves and was too complex for typical users.

PLEXSYS advanced this work by creating an integrated development environment composed of both a complete and unified development methodology and a set of computer tools to support the use of the methodology, which consisted of four phases that roughly corresponded to the traditional SDLC. Unlike the waterfall SDLC, the PLEXSYS methodology provided for feedback from each phase to its predecessor and a continuous cycle from the last phase to the first, similar to the spiral models presented by Boehm $[5]$ and DeGrace $[24]$ . PLEXSYS never progressed beyond the academic prototype stage because, like many early CASE tool prototypes, it suffered from limitations in computer technology, particularly in processing power and graphical capabilities. The analytical power provided by PSL/PSA and the automated design tools of PLEXSYS would have required graphical user interfaces (GUIs) and easier-to-use graphical modeling techniques present in modern CASE tools.

Other researchers sought to make the analysis and design process in the SDLC more disciplined through the use of well-defined methodologies supported by graphical models. Of these attempts, structured analysis (SA) [25, 61], information engineering (IE) [43], and object-oriented analysis and design (OOAD) [6, 36] have had the greatest impact on software development. SA emphasizes a top-down analysis of processes using data flow diagrams, structure charts, and state-transition diagrams. IE, on the other hand, focuses on creating the organization of data required for ideal support of business processes. Proponents of this paradigm believe an organization's data model is more permanent than its processes and that optimizing the design of data will enable future applications to be added with little disruption to current applications. This is seen as a first step toward data standardization and a necessary part of systems integration [3, 32, 40, 46]. The value of data modeling and data integration is further underlined by a study conducted by the Gartner Group which indicated that the average large corporation required access to more than one trillion bytes of data in 1990, a number fifty times as large as data access requirements in 1985 [45]. Proponents of object-oriented programming (OOP) have developed a number of OO analysis and design methodologies, many of which are based on the fundamental concepts of information engineering [30]. Booch [6] presents one such OOAD methodology (which was later incorporated into the Rational Rose® CASE tool). What differentiates Booch's OOAD from IE and SA is the use of prototyping at the conceptualization phase, the use of scenarios and patterns during analysis, evolving the final system as a stream of executable releases, and the incorporation of the principles of reuse at each stage of the methodology. CASE technology used an integrated set of analyst and developer software tools to automate these methodologies. While CASE technology has been credited with a substantial increase in productivity $[2, 47]$ , studies such as $[38]$ have shown that, in the majority of instances (70 percent), use of CASE tools has been discontinued one year after adoption.

The refinement of systems development methodologies made it possible to verify the internal completeness and consistency of designs and provided a formal vernacular for communications between analysts and designers. Nonetheless, the output of these methodologies, and the CASE tools that automate them, has limited value in determining and validating user requirements. The complex syntax and technical nature of the artifacts produced by these methodologies make them often indecipherable to end users, a communication barrier that prevents end users from contributing in an active, meaningful manner during requirements elicitation. Users still must wait until the final system or a mature prototype has been produced to have an opportunity to provide feedback on the analysis process. The development of user-centered analysis techniques is an important step toward bridging this communications gap.

## Collaborative Requirements Definition

As stated earlier, one of the major problems confronting systems developers is obtaining a complete and stable set of requirements in a timely fashion. Requirements that surface during implementation/test phases are difficult to meet. Eliciting requirements from users has traditionally been a lengthy process relying on user interviews and surveys $[55]$ . Serial interviews with members of large user groups are very inefficient and do not provide an efficient mechanism for resolving conflicting requirements $[16]$ . Questionnaires can be used to survey large numbers of users, but inaccuracy and low response rates are problems, as is lack of a conflict-resolution mechanism $[16]$ .

Several streams of research, both academic and professional, address this problem by involving users more directly in the requirements determination and interface design processes. These techniques have in common the use of meetings attended by both analysts and users. Electronic meeting systems (EMS) supported meetings also have been used to elicit requirements from many users simultaneously and are excellent mechanisms for revealing and resolving conflicts $[48]$ . Structured meeting techniques such as joint application development (JAD) $[59]$ and other similar facilitated application specification techniques (FAST) $[52]$ have been developed to improve the productivity of group meetings and overcome the problems of other requirements elicitation techniques. The use of prototyping and methodologies such as rapid application development (RAD) $[44]$ enables users to become involved at the design stage, thereby allowing requirements that would have surfaced after deployment of a system to be uncovered early.

JAD centers on a structured workshop that brings together users and IS professionals to determine requirements, thereby overcoming several of the problems of traditional techniques such as slow communication, long feedback time, user-versus-IS conflicts, and the tendency toward a tunnel-vision-like focus on a single user or department. The

JAD session also promotes commitment, group cohesion, resolution of conflicting views, and productive group meetings $[59]$ . JAD workshops traditionally have been “low tech,” relying on tools such as flip charts and blackboards, but now they increasingly depend on single-user CASE tools or other computer support $[59]$ . Although JAD is effective for requirement elicitation and conflict resolution in a group meeting, it does not specify how individual meetings could be combined into a complete requirement elicitation methodology. Nor does it include many of the traits Davis $[18]$ identified as needed in a comprehensive technique.

Traditional general EMS (GEMS) [49] tools including electronic brainstorming, idea categorization, and group vote have proven extremely useful in supporting analysis teams but have been used with mixed results to support JAD sessions. Carmel [11, 12, 13] compared five electronically supported JAD sessions with five traditionally supported JAD sessions. GroupSystems (TM Ventana Corporation), a GEMS tool, was used to support the electronic JAD meetings. The study showed that GEMS allowed for greater and more equal participation, but at the cost of less discipline and less success in resolving conflicts. Wood and Silver [59] postulated that the problems were caused by lack of facilitation and planning, not the use of computer tools. They further concluded that, given the same level of planning and facilitator intervention, the traditional JAD sessions also would have fared poorly. Studies by Liou [42] and Chen [14] showed that GEMS can be used successfully to capture basic requirements information, but Chen [15] also pointed out that, while GEMS are helpful for many meeting needs, the generality of the tools imposes some limits on the capture of requirements information. GEMS lack modeling support for the capture of structured relationships, a repository based on modeling semantics, support for multiple levels of problem abstraction, information hiding, and complexity management. Comments contributed by users tend to be unstructured and difficult to segregate into semantically meaningful fields. Consequently, it is difficult to perform error checking, consistency checking, and completeness checking. A lack of disciplined structure also impedes easy import or export to CASE tools that embody a disciplined structure. Katic et al. [37] attempted to implement aspects of Booch's OOAD methodology using a combination of GEMS and group-enabled software for the creation of class/responsibilities/collaborators (CRC) methodology. Users in this study were able to create process scenarios and, with the help of facilitators, to construct CRC definitions, but they were not able to develop OO designs.

Rapid application development (RAD) was developed to help overcome some of the shortcomings of JAD. RAD, as defined by Martin [44], consists of a four-phase life cycle: requirements planning, user design, construction, and cutover. RAD's main advantage is speed. In some cases systems have been developed in one-fourth of the time required by traditional methodologies. The short development cycle leads to systems that more closely match current business needs, and users' participation in the design process and their ability to interact with the prototype increase commitment and chances that all requirements will be satisfied [44]. RAD is not without its problems, though. It does not include any provisions to promote code reuse or consistency across interfaces, programming, and data [8]. Large systems or components, which require extensive integration with existing systems, may not be supported well by the methodology or by the CASE tools used to support it [33]. These problems require input from more users and user organizations than the RAD methodology can support. In addition, systems analysts may not have all the skills needed for managing the dynamics of small group meetings, let alone large ones.

## Silver Bullets

"There is no one silver bullet," Yourdon [60] aptly wrote, "but there are a dozen or so that are worth exploring." Among Yourdon's list are JAD, RAD, prototyping, information engineering, software reusability, and object-oriented methodologies. Common to these techniques is the effort to reduce cost via automation and reuse and to schedule reduction through the effective use of teams and the involvement of end users at various stages of the project life cycle. This changes not only the composition of the project team but the artifacts that the team produces. Traditional SLDC methods demand that a series of requirements and design documents be produced, followed by development of software and integrated systems. This sequence has been replaced by organizational models (activities, processes, patterns, and scenarios), integrated data models (relational and object-oriented), and incrementally developed prototype systems. The major challenge that remains is to discover a way to combine the best elements of these promising techniques into a single methodology. One key will be how end users are integrated into the process. Both JAD and RAD involve groups of end users in both the analysis and design phases for the purpose of requirement elicitation and prototype evaluation. Systematic software reuse and OOAD methodologies rely on end-user input during domain and model analysis and could be improved by substituting analyst interviews with group-oriented techniques.

Merely assigning end users to design teams is not enough; a collaborative systems development methodology must elegantly identify and incorporate the needs of diverse users. It is difficult, however, to effectively obtain adequate user involvement $[59]$ . A primary difficulty stems from the fact that systems development methodologies have traditionally been designed around the needs and capabilities of analysts instead of users. Traditional CASE tools are far too complex for non-analyst users to use, and learning how to use CASE tools takes too long for first-time users, so group-enabling such tools to allow end-user involvement would not work. There is a need to adapt modeling techniques to enable direct contributions from non-analyst users. This can be achieved by the development of processes and representations that users understand and can use.

Structured intervention literature reflects that the application of appropriate structured procedures produces better results than normal group interaction $[7, 34]$ . Striking a balance between the use of analyst interviews, powerful CASE analysis tools, and group-enabled modeling tools requires accurately assessing the value and form of end-user input at each level of model abstraction. This necessitates the use of skilled facilitators orchestrating a mix of user/analyst/developer interaction techniques throughout all phases of systems development. Studies such as $[26, 50]$ underline the importance of facilitation in electronic meetings. George [31] argues that facilitation is more important with larger groups because larger groups have a greater need for structure and coordination. Successful facilitators know when it is more appropriate to use small rather than large groups. For example, one effective technique consists of analysts working with small groups of selected users to develop initial models that are then evaluated and enhanced during large group meetings.

The goal of the research described in the following sections is to respond to these challenges by developing a framework for rapid, integrated, incremental systems development that enables groups of users to contribute effectively and efficiently throughout the development process. The methodology described is designed to foster the best elements of systematic reuse, data integration, and collaborative work methods in order to produce integrated and interoperable systems.

## A Framework for Collaborative Software Engineering

EARLIER RESEARCH AT THE UNIVERSITY OF ARIZONA on general electronic meeting systems (GEMS) provided extensive information on how to improve the efficiency of user-group meetings. Similar research on EMS modeling tools focused on improving the effectiveness of user development of activity and data models. Although both areas are critical to the information systems development process, they do not by themselves provide a comprehensive systems development methodology. Current University of Arizona research has therefore been extended to integrate the strengths of general and modeling EMS tools with the best of the systems development practices described in the previous section. The resulting Collaborative Software Engineering Methodology provides a comprehensive framework that will guide related research toward the common goal of enabling participation of multiple users throughout the systems development process.

## The Collaborative Software Engineering Methodology

Because the goal of this research is to enable user participation, our Collaborative Software Engineering Life Cycle (figure 1) is portrayed with user/analyst/developer collaboration at its center. The planning, requirements, design, and implementation phases of the life cycle are shown loosely separated and as a continuous cycle to emphasize the iterative and ongoing nature of systems development in today's organizations. The primary outputs of each phase are displayed as links between successive phases.

Teamwork is essential to all successful information systems development efforts. This approach is incorporated in our methodology by representing the analyst/developer team at the core of the life-cycle model. Extending out from the core are three different levels of user participation: selected users, who represent the user groups; groups of users, who represent the user community; and the entire user community. This layering of user participation is required because the Collaborative Software Engineering Methodology is designed to be scalable to large, complex information systems supporting extensive and diverse user populations. For example, the Department of Defense is developing systems to support users at Army, Navy, Air Force, Marine, and Defense Logistics Agency installations around the world. Although it is possible to survey these users periodically to identify their needs or provide them with status reports (e.g., during the planning phase), it is virtually impossible to involve all users on a regular basis. Therefore, a representative group is drawn from the various constituencies through purposeful sampling. Group members, referred to as subject matter experts (SME), should be influential members of the user community and should be experts in their business areas. SME groups meet regularly to generate requirements (e.g., business scenarios), resolve conflicting viewpoints (e.g., varying business processes/scenarios), enhance proposed models (e.g., integrated data models) or prototypes, and validate key deliverables (e.g., prioritized requirements). Although such meetings are essential to ensure equitable representation of the diverse user community, it can be extremely expensive to bring thirty or more SMEs together for these group meetings. Therefore, between meetings, selected group members work with analysts and developers either individually or in small groups to answer questions and develop initial models (e.g., system use cases). These initial models can be provided as read-aheads to the user group, greatly increasing the productivity of the large group meetings.

![](/api/attachments/ZGD4J8N8/fulltext/images/35b76816542aa03db63822c931f2f949ae6f55de661655447b9f74a56675fa00.jpg)  
Figure 1. The Collaborative Software Engineering Life Cycle

The productivity of the large group meetings is also enhanced by the methodology's emphasis on the use of representations, software tools, and meeting processes that enable synchronous input by groups of non-analyst SMEs without requiring them to become methodology experts. Determining the best combination of CASE tools, GEMS, and EMS modeling tools is important for achieving this goal. GEMS support general meeting tasks and some development activities. They provide significant advantages in the areas of anonymity, parallel processing, and maintenance of an organizational memory. When EMS modeling tools that fit meeting needs exist, they are used. However, EMS modeling tools are not appropriate for all types of development activities. Furthermore, EMS modeling tools lack some features found in sophisticated CASE tools. Thus, information captured in group meetings is often moved to CASE tools after the meeting. Import/export capabilities between EMS modeling and commercial CASE tools help smooth this information transfer. Analysts then work with the CASE tools between meetings and, when required, use them as aids at meetings.

As powerful as these tools are, having the right tools is not enough. The methodology also emphasizes the need for skilled facilitators applying well-designed meeting methods to ensure effective mapping of the EMS to the group processes of elicitation, convergence, validation, and prioritization. Depending on the maturity of the group, the complexity of the task, and the specific development activity, these group processes may occur multiple times in a single group meeting or may be spread across several meetings. Skilled facilitators are needed to recognize differences and to guide the SME group toward efficient accomplishment of the its goals.

This layering of user participation, mix of user/analyst/developer interaction techniques, and use of EMS technology is unique to the Collaborative Software Engineering Methodology. The methodology builds on several participative development concepts by incorporating JAD's group meetings and RAD's user participation, but it also extends those concepts. It explicitly includes a mix of interaction techniques with guidelines for effectively supporting them by means of EMS technology during the different life-cycle phases and at different levels of user participation.

User interaction techniques and other critical collaborative processes of the methodology are implemented in each of the life-cycle phases described below. The presentation of the primary phases of the methodology has been simplified considerably for this paper. In the comprehensive version of the methodology, each phase is decomposed into more detailed activities/subactivities with flow, sequence, and feedback/iteration among the child activities explicitly defined to provide detailed guidance for those executing the methodology. For each of the primary phases, the methodology defines “what” activities should be accomplished, “when” they should be done, “how” the output of each step should be developed, and “who” is responsible for and participates in each step of this team-based process. The methodology also provides guidelines for tailoring to the needs of a specific information system. Examples of some of the key features of the methodology are included in the following overview of its primary life-cycle phases.

## Planning Phase

The purpose of the planning phase is to identify user needs and to map them into information system (IS) development plans. Planning is especially critical in the Collaborative Software Engineering Methodology because it is designed to support incremental system development (although it is also applicable to other development approaches). An incremental system development life cycle supporting timely fielding of information system increments/versions is used to rapidly satisfy customer requirements and to get real-world user feedback for future increments. Because of the need for rapid systems development, IS plans are established collaboratively by management and senior analysts/developers based on user input (e.g., surveys) instead of by a time-consuming strategic planning process such as IBM's Business Systems Planning [35]. IS plans and proposed schedules are provided to development teams and the user community. The plans are updated based on feedback from the users and as understanding of user needs increases with successive information systems increments.

## Requirements Phase

The purpose of the requirements phase is to guide the SMEs' transition from analysis of business needs to identification of systems requirements. The methodology accomplishes this goal through an iterative process of making the transition from high levels of abstraction to specific details which allows SMEs to bridge two gaps, the requirements and the artifact specificity gaps. The process begins with top-down decomposition of business activities followed by development of detailed business scenarios and data requirements for those activities. This process increases the specificity of requirements. The scenarios and data requirements are subsequently translated into alternative system use cases that are implemented in a physical artifact—the prototype. Research has shown that many users have great difficulty in articulating their requirements unless they see a physical artifact. Successful techniques such as RAD have proven that prototypes are an excellent mechanism for helping users overcome this barrier by providing a physical product they can evaluate. The development and evaluation of system use cases and prototypes therefore increase specificity of both the requirements and the artifact. This results in higher-quality requirements than those provided by the traditional waterfall model, which does not provide a demonstrable product until near the end of the entire life cycle.

## Design and Implementation Phases

The Collaborative Software Engineering Methodology seeks to improve the speed and quality of the design and implementation phases by continuing its emphasis on SME participation and prototype development and evaluation. The methodology implements a RAD-like approach, with analysts and developers working with the SME group and its representatives to refine user interfaces and define required design specifications. Because of their involvement throughout the development process, the SME groups are also ideal participants during the implementation's alpha testing. Beta testing generally expands outward to include additional members of the user community at large. Upon completion of the implementation phase, the new system, along with its associated models and requirements/design specifications, serve as inputs to the next iteration of the life cycle. In this manner, the systematic reuse of requirements, designs, and subsystems is specifically incorporated into the Collaborative Software Engineering Methodology, thereby also accruing the benefits of this effective development practice.

The above description of the methodology is intended as an introduction to our Collaborative Software Engineering Methodology. As stated previously, the methodology provides a framework to guide research related to expanded participation of multiple users throughout the systems development process. The remainder of the paper reports on research conducted to support the requirements phase of the methodology.

## The Collaborative Requirements Elicitation and Validation Phase

The primary focus of our research to date has been in the area of collaborative requirements elicitation and validation (CREV). The CREV phase of the Collaborative Software Engineering Methodology has been decomposed into six primary activities as shown in figure 2. A description of each of these activities follows the CREV diagram.

## Step 1. Identify Business Activities

The first step in the CREV phase is the identification of business activities. Both the SADT and IE methodologies require development of comprehensive business activity/function models. The CREV approach speeds the development by only requiring a simplified model of business activities. This model is essential to the effective initiation of an information systems development effort and serves the following purposes:

\- The model documents the business environment and helps the highly heterogeneous SME group develop a common understanding of the business.

\- SMEs can analyze the model to determine whether a complete business process reengineering (BPR) effort is warranted or whether they can directly incorporate some process improvements into the model quickly without a waiting for an extended BPR analysis.

\- SMEs then analyze the model to identify the activities having the greatest need or promising the greatest potential benefit from new or improved information systems support. These activities become the focus of more detailed analysis and begin to define the scope of the information system.

\- The activity model also provides a structure for more detailed analysis. For each of the activities having IS potential, the SME group continues top-down decomposition of activities into subactivities. SMEs explicitly prioritize their attentions as they focus their decomposition efforts on the activities having the greatest need for information system support.

![](/api/attachments/ZGD4J8N8/fulltext/images/1d8d009fcf87740a216fdbcd952c1789cb31c31f06f4f307ce549c8324d925d3.jpg)  
Figure 2. Overview of Primary Activities in CREV Phase

\- Finally, new incremental development efforts for the same business area can use the model to conduct detailed analysis of activities that not been included in previous increments.

While there are several possible ways of accomplishing this step, we use GroupSystems Group Outliner to support SME groups in creating informal activity hierarchies. When more formalism is warranted, we use the Activity Modeler collaborative modeling tool to develop structured activity models. The output of this step is a preliminary definition of the scope of the IS and a list of discrete business activities/processes within that scope for which business scenarios will be generated in the next step.

## Step 2. Generate Business Scenarios

The purpose of this step is to capture the dynamic view of business processing requirements through the generation of business scenarios. Use of scenarios is an effective concept extracted from many object-oriented development methodologies. In this context, business scenarios are defined as narrative descriptions of human work processes that specifically identify an ordered sequence of actions taken to accomplish some business goal. SME groups generate business scenarios for each of the discrete business activities with automation potential identified during step 1. These scenarios initially describe the current work processes. The group is led to converge on a common definition of work processes. Next, group members brainstorm on how the scenario might be improved and on how information systems might improve the process. In this way, improvements from business process changes and information systems enhancements can be identified. Data/objects required to support these scenarios are also identified so they can be incorporated into the data model developed in step 3. Upon completion of the initial integrated data model as described in the next step, the SME group evaluates potential impacts of the integrated data on the business, that is, how data integration would change the desired business scenarios. If these impacts are acceptable, the business scenarios are updated to reflect those changes. Otherwise, the SME group recommends revisions to the initial integrated data model that are acceptable from a business processing perspective. The outputs of this step are the data requirements input to step 3 and the integrated business scenarios used as input to step 4. These business scenarios, along with the data model developed in step 3, provide the systems analysts with key information about how an information system can support the business requirements. In addition, the business scenarios provide a rich context for evaluating the impacts of alternative information systems solutions on the business. Currently, we use GroupSystems Group Outliner to support scenario generation and evaluation by SME groups. Occasionally, we also use a single-user process modeling CASE tool in chauffeured mode to analyze complex scenarios.

## Step 3. Develop Data Model

SME groups participate in development of the data model used to capture the business data requirements and associated business rules. IE and other data-driven methodologies include development of the data model as the central focus of the requirements phase. In the CREV phase, it is developed in conjunction with the business scenarios. Existing systems and data models provide a rich source of information that the data modeler can use to develop an initial data model. SMEs then can use the business scenarios to identify additional data requirements. SMEs also provide the meta-data (data type, length, domain values, etc.) required to complete the data model. Data modelers work simultaneously with SMEs to identify potential data integration opportunities, which in turn are incorporated in the initial integrated data model. SME groups assess the impact of integration on the business, using scenarios as described in step 3. Feedback from this analysis is used to update the integrated data model which is validated by SMEs. We primarily use Group Data Modeler, as described later, to support collaborative capture of data model information, including meta-data. The graphical representation of the data model is captured in a CASE tool. The output of this activity is the integrated data model, a critical component of the requirements specification and a major input to the next two steps of the CREV phase.

## Step 4. Define System Use Cases

In this step the focus shifts from the business to the information system. Systems analysts, working with small groups of SMEs, use the integrated business scenarios and data model to define alternative system use cases. The system use case concept is drawn from Jacobson et al.'s [36] popular approach to object-oriented systems engineering. A system use case represents the sequences of actions performed by the system to yield an observable and valuable result to the user, so system use cases bridge both the requirements and artifact specificity gap. They bridge the requirements gap by providing specific descriptions of what the system must do to satisfy the users' business requirements. They also help to bridge the artifact specificity gap by including physical mockups of actual screen and report layouts. We do not use EMS tools to create system mockups, although EMS can be used to develop and evaluate narrative descriptions of system use cases. The output of this step is a set of alternative system use cases with proposed screens, menus, and reports that define the users' preliminary information systems requirements. This information is used during step 5 to develop the initial system prototypes for SME evaluation.

## Step 5. Evaluate Prototypes

To help SMEs identify and validate their requirements, a prototype based on the proposed system use cases is developed. As clearly demonstrated by the RAD approach, prototypes provide SMEs with a physical artifact that enables them to evaluate both the requirements and their implementation. A critical element of this step, which is missing from most RAD efforts, is a structured prototype evaluation process used to elicit and validate feedback from SMEs in a group environment. Specifically, we use GroupSystems Categorizer to collect open-ended feedback and GroupSystems Survey to collect responses to closed-ended evaluation questions. The feedback is used to update the business scenarios, data models, system use cases, and the prototype in an iterative development and evaluation process that increases the specificity of both the requirements and the artifact (i.e., the prototype). The outputs of this step are the feedback used to update the SME requirements, the prototype evaluation results, and the prototype, which then becomes a key component of the documentation step of the CREV phase.

## Step 6. Prioritize and Document Requirements

Unlike a monolithic requirements specification, which often takes so long to develop that it is outdated before it is even completed, the objective of the CREV phase is to define a streamlined process for identifying user requirements. The goal of this step, therefore, is to consolidate and prioritize requirements identified during SME group sessions. Documentation of these requirements in combination with the activity, data, and business scenario models, the system use cases, and the prototype provide a complete and useful requirements specification for the development team. The succinct documentation generated by this step is supplemented by the knowledge participants have gained from taking part in the process. This step is critical, because it summarizes the results of the entire requirements process and documents SME priorities and agreements.

## Implementing the Methodology

Although we have been both developing and using EMS technology to support requirements gathering activities for years, the preceding requirements-gathering steps were formalized within the overall Collaborative Software Engineering Methodology over the last year and a half.

The DoD Environmental Security Corporate Information Management (DESCIM) Program Management Office began implementation of the Collaborative Software Engineering Methodology in early 1997. The U.S. Army Waterways Experimental Station (WES) was in the process of implementing the methodology in mid-1997. We conducted a training session for DESCIM team leaders and key systems analysts and modelers to begin the implementation process. We also assisted DESCIM personnel in implementing the methodology by helping them schedule the key life-cycle activities for their current software development projects. Based on just these actions, DESCIM is already seeing many project management benefits. We have also facilitated meetings for each of the primary activities in the CREV phase of the methodology. A variety of GEMS have been used to support these meetings. We have also developed and used EMS modeling tools over the last several years to support activity and data modeling. These tools are called Activity Modeler and Group Data Modeler, respectively. In particular, Activity Modeler has proved extremely effective for identifying and analyzing business activities (CREV Step 1) as well as for business process reengineering. Group Data Modeler has been equally successful for eliciting essential data modeling information directly from SMEs (CREV Step 3). The detailed discussion of these collaborative tools in the next two sections shows how the principles of collaborative software engineering (i.e., integration of user-comprehensible representations into tools with associated meeting methods) have been successfully implemented in these EMS modeling tools.

## Collaborative Activity Modeling

ACTIVITY MODELING IS THE FIRST STEP IN THE CREV phase of the Collaborative Software Engineering Methodology. The activity model generated in this phase provides a basis for the analysis of business processes and defines the preliminary scope for further analysis and design activities. The collaborative activity modeling tool described in this section was designed as a specialized EMS modeling tool to support this first step.

## Activity Modeling Concepts

There are various methods for modeling business processes. The IDEF0 definition method is one commonly used by commercial and noncommercial organizations to develop and analyze business models. At one time, IDEF0 was designated by the U.S. Department of Defense (DoD) as the official method for Functional Process Improvement [28], and although it no longer retains this designation, it is still widely used as a powerful business analysis method. The methodology is used to define a functional or activity model of what an organization does. The IDEF0 method grew out of the Air Force Integrated Computer Aided Manufacturing project [57]. (The term “IDEF” comes from ICAM—Integrated Computer-Aided Manufacturing—DEFinition language.) An IDEF0 model consists of an activity hierarchy with its attendant constraints on the activities included at multiple levels of detail. Activities are bounded by inputs, controls, outputs, and mechanisms (referred to in aggregate as ICOMs). ICOMs show the information and physical objects that link activities. When viewed in diagrams, activities are represented as boxes and ICOMs are represented as arrows. Inputs enter from the left of activities, controls enter at the top, outputs exit from the right, and mechanisms enter from the bottom. IDEF0 is based largely on a well-established modeling language known as Structured Analysis and Design Technique (SADT) [53, 54].

Parent and child diagrams within the IDEF0 method should be balanced. That is, ICOM arrows that bound a particular activity (parent) should also bound its corresponding decomposition diagram (children). Logical classes of ICOM connections can be bundled together into more general ICOMs that enter or exit a decomposition, and therefore also enter or exit the parent. Bundling allows more generalized inputs, outputs, controls, and mechanisms to be shown on the parent diagram, which reduces the complexity of the more abstract parent view. Balancing, bundling, multiple levels of abstraction, and other provisions within the IDEF0 method represent structure that gives IDEF0 exposition power and rigor that is not available in many less-structured modeling methods.

The basic concepts of IDEF0 are simple enough to be grasped quickly by those who are not experts in modeling, who can use them for very simple models without a great deal of training. However, when developing nontrivial models that are well integrated and parsimonious, non-experts quickly flounder unless they have expert support. More complex modeling efforts require the support of someone who understands the modeling process and the nuances of IDEF0 principles.

## Traditional Model Development Approach

Current tool support for both activity and data model development is dominated by single-user, analyst-oriented tools. One reason for this is that activity and data model development requires considerable expertise. Since analysts have long used interviews to buffer subject matter experts (SMEs) from modeling complexity, tools have tended to be designed for analysts. Although such tools are valuable modeling aids, they do not provide the means whereby non-analyst SMEs can work in parallel to contribute and review model content. Thus, traditional technological support has prevented more than a handful of SMEs from conveniently and effectively participating in model development. In traditional model development, diagrams and definitions are typically constructed on whiteboards or transparencies. In many instances, a second shift of modelers works after hours to transcribe this information into a CASE tool so that transcription time does not cut into the group's active modeling and analysis time. In addition, SMEs must often attend three to five days of activity or data modeling training before participating in these modeling sessions.

One of the significant problems of the traditional approach is that filtering all input through a single analyst in a serial fashion significantly restricts direct, parallel input from participants. A productivity bottleneck results from only one person's being able to contribute at a time.

Also, filtering participants' verbal contributions through an analyst may reduce the amount of content that is considered and recorded during model development.

## The Activity Modeling Tool

To overcome the problems of the traditional activity model development approach, researchers at the University of Arizona developed a collaborative activity modeling tool. The iterative refinement and study of collaborative support features within the activity modeling tool revealed many features that proved important for support of collaborative activity model development. This section describes the development of the tool, its key functions, and successful facilitation strategies.

## Development History

The evolution of the collaborative IDEF0 modeling tool, now called “Activity Modeler” (hereafter referred to as AM) is described in detail in $[19, 20, 51]$ . The first prototype was developed at the University of Arizona in 1992. In its research phase, the tool went through four substantial prototype, test, and refinement cycles before being transferred to Ventana Corporation for development as a commercial product. Ventana rewrote the code, adding several additional enhancements before officially releasing it to the market. In its current form, the AM tool represents approximately seven person-years of development, testing, and refinement. It is the most sophisticated EMS modeling tool developed so far.

## Collaborative Modeling Interfaces

AM provides a textual and a graphical user interface, both of which are important in the collaborative activity modeling process. Our experience working with several groups of SMEs showed that, using the textual interface, the SMEs could quickly enter important data into the model, while the graphical interface helped them visualize certain modeling aspects such as how activities were related to each other and which ICOMs should be bundled together.

## Graphical Interface

The graphical interface of the tool is known as the AM Viewer. Graphical support is essential for conceptualization during model development and review. The human factors research that went into the development of the IDEF0 method emphasized the use of easy graphical metaphors that manage complexity. Our early attempts to capture data in a textual model editing interface and to capture graphics in a single-user IDEF0 CASE tool were unsuccessful because the model changed so rapidly that the analyst supporting the session could not keep up in the CASE tool. This graphical lag thwarted real-time visualization by SMEs. We eventually succeeded in developing capability that allowed SMEs to invoke various graphical views of the model rapidly on demand. Rather than burden SMEs with the task of positioning graphical objects, the viewer engine creates a graphical view based on model content that has been entered textually.

![](/api/attachments/ZGD4J8N8/fulltext/images/035efa6dca711a20aceced898cfed5e85c9f1f6a5f987e683cf66fed651661ce.jpg)  
Figure 3. Activity Modeler Viewer with Display in Tiled Mode

This reduces processing overhead and cognitive demands and permits SMEs to focus on editing model content rather than on how to lay out the diagrams. Figure 3 shows two ways of presenting graphical views of an IDEF0 model using the AM Viewer. On the left is the traditional sibling set view that shows how inputs, controls, outputs, and mechanisms interact and connect activities within a single decomposition. The window on the right shows the view of a single activity and its related ICOMs.

The arrows in the viewer tool bar allow for navigation between activities in a sibling set and among the different levels of the model. In addition to the tiled view shown above, a hierarchical tree view is available. SMEs can view each type of diagram individually or in tiled mode. Forms for the textual interface can be accessed from within the viewer to add or modify portions of the model. SMEs can also easily toggle back and forth between the graphical and the textual user interfaces of the tool.

## Textual Interface

In both graphical and textual modes, the AM software provides a shared work environment that includes concurrency control so that, although only one workstation can edit a specific activity or ICOM at a time, individuals can view all activities and ICOMs concurrently. The main screen of AM presents two windows to SMEs (see figure 4). On the left is the activity list, presented in hierarchical form. On the right is the ICOM list, presented in alphabetical order. Symbols on the screen represent whether activities and ICOMs have definitions (a sheet of paper) and improvement ideas (a light bulb).

<table><tr><td>A0 Conduct Environmental Planning
A1 Perform Initial Environmental Evaluation of Test Conc
A1.1 Coordinate with Environmental Office
A1.2 Determine Whether Additional Review is Require
A2 Conduct Environmental Review
A2.1 Complete Environmental Survey
A2.1.1 Obtain Technical Data on Test
A2.1.2 Review Test Request for Possible Impacts
A2.2 Acquire Needed Information
A2.2.1 Identify Environmental Data Requirements
A2.2.2 Review Information
A2.2.2.1 Review Range Baseline
A2.2.2.2 Review Proposed Test Information
A2.2.3 Obtain Missing Information
A2.2.3.1 Conduct Field Survey
A2.2.3.2 Conduct Literature Search
A2.2.3.3 Obtain Other Outside Information
A2.3 Identify and Resolve Environmental Compliance
A2.3.1 Conduct Regulatory Analysis
A2.3.2 Obtain Required Permits
A2.3.3 Conduct Necessary Consultation
A2.3.4 Complete Other Regulatory Requirements
A2.4 Conduct NEPA Environmental Analysis
A2.4.1 Define DOPAA working with customer
A2.4.2 Conduct Impact Analysis
A2.4.3 Coordinate NEPA Document
A2.4.3.1 Prepare Draft NEPA Document
A2.4.3.2 Prepare Final NEPA Document
A2.5 Generate Record of Environmental Consideration
A3 Receive Environmental Approval/Disapproval</td><td>Additional Information
Additional Information Request
Additional Test Information Request
Affected Environment Information
Budget
Categorical Exclusion
Consultation Constraint
Contractors
Customer Notifications
Database
Decision Maker
Decision Package
Designated Cognizant Authority
DOPAA Document
Draft NEPA Document
Environmental and Other Information
Environmental Constraints Notification
Environmental Models
Environmental Planner or Board
Environmental Planning Check List
Environmental Program Office
Environmental Test Constraint
Field Information
FONSI
Forwarding Letter
Funding
GIS
GPS
Impact Analysis Report
Information Needs Request
Information Request Resource</td></tr></table>

Figure 4. Activity Modeler Main Screen

From this main screen, SMEs may add activities and ICOMs. SMEs may also double click on an activity or ICOM to add/edit definitions or add improvement ideas. Only ICOMs that have been entered into the ICOM glossary can be attached as connections to activities. This enforcement helps reduce the tendency for individuals to enter ICOM homonyms and synonyms.

Figure 5 shows the Connections dialog that allows SMEs to add, delete, or modify ICOM connections associated with an activity. The SME selects whether to add an ICOM as an input, control, output, or mechanism.

When SMEs want to add a connection, they are presented with the Add Connection dialog where they can select ICOMs from a pick-list to attach to the activity. On the Add Connection dialog, the tool can show all existing ICOMs or just those ICOMs used by the parents, siblings, or children of a given activity. If the ICOM to be attached has not been added to the glossary, the Add ICOM dialog is displayed and the ICOM can be inserted into the glossary and then attached to the activity.

ICOMs can be bundled as appropriate and a simple, easy-to-use interface is available for SMEs to create ICOM bundles. These bundles are also reflected in the graphical view of the model. The model analysis function or the viewer can be invoked at any time to locate bundling and propagation errors. This helps eliminate hierarchical ICOM propagation problems.

![](/api/attachments/ZGD4J8N8/fulltext/images/d0ff67e5aa96f0738109b1817fef692fef6e185a1aba889e2625c2088bc2242f.jpg)  
Figure 5. Activity Modeler Connections Dialog

## Model Reconciliation and Semantic Correctness

In the process of developing our first activity models we realized an integrated semantic checker within AM was essential. During model development we found that modeling rule violations were easily overlooked by the SMEs unless they received immediate feedback. The error checking features that consequently were added to AM were powerful, but not too restrictive or intimidating to SMEs. Allowing a certain amount of freedom accommodates different facilitation styles (top-down, bottom-up, inside-out, etc.), while at the same time providing a mechanism to identify and correct model errors to insure compliance with standards. Error checking in AM is supported in two ways. First, through visual cues on the diagrams, violations of IDEF0 rules (errors) and model inconsistencies (warnings) are flagged with red dots (see the top two inputs in figure 3), which the SMEs can click on for an explanation of the error or warning. Second, within the textual view of AM is a model analysis function that checks for twenty-eight different errors and warnings. This feature has a help reference for each error that can take the SME to a dialog box where the error can be corrected. This immediate feedback helps the SMEs and the facilitator identify and fix modeling errors, inconsistencies, and omissions before they get out of control.

## Group Coordination and Group Access Management Mechanisms

AM has several features designed to support group coordination and to give the facilitator the ability to manage SMEs' access to the model. Coordination mechanisms include status indicators on the main displays, which tell the SMEs whether an activity or ICOM is being edited by another SME, if it has an improvement idea or a description, or if it has been marked for deletion.

AM provides the facilitator with the ability to set group access rights to different AM functions. Rights can be set for adding/deleting/modifying activities, ICOMs, and activity connections. The facilitator can also turn the SMEs' right to use the AM viewer off or on. In addition, certain activities and ICOMs can have locks placed on them to allow SMEs to view but not edit the locked items. Therefore, if there is a dispute regarding a particular activity or ICOM, its current state can be locked until the disagreement is resolved.

## Import/Export

An import/export feature was developed to allow the exchange of models between AM and a number of traditional single-user IDEF0 CASE tools, such as AI0 Win from KBSI and Design/IDEF from Meta Software. AM uses the interchange definition language (IDL), which was developed by a consortium of IDEF tool vendors, for model import and export. This feature allows models that have been developed in traditional single-user tools to be imported for group review and revision. It also allows models to be migrated to CASE tools after collaborative meetings.

## Facilitation Using AM

## Preliminary Preparation

When possible, it is preferable to perform some preliminary analysis before a meeting to educate the analyst and to develop a high-level list of candidate activities, rather than starting from scratch in the group meeting. It is easier for a group to fix and build upon a reasonable starter list of activities. This list can be developed by conducting SME interviews or by asking the SMEs to submit a high-level list of activities. The analyst then prepares the list of candidate activities based upon the SME input and enters it into the Group Outliner tool of GroupSystems (a tool used for collaboratively building hierarchical lists). It is also helpful if the analyst and the meeting owner can develop the model context, viewpoint, and purpose prior to the session.

## SME Training

Developing large, complex models of common business practices requires much more training than it is practical to provide to session participants. Rather than giving the SMEs three to five days of training, as is often done in traditional modeling meetings, SMEs are given thirty to sixty minutes of limited training and are then led through the model development process by a trained IDEF0 facilitator. This training is supplemented by short just-in-time training segments at various stages of the modeling process.

## Basic Facilitation Approach

The process of model development combines some aspects of traditional, top-down model development and yet allows participants to work in parallel to contribute textual model content. The first session task is to develop the model context, viewpoint, and purpose (or review these items with the group if they were developed prior to the session). Next, the entire group helps define the candidate activity hierarchy. If a candidate activity list has been generated prior to the session, the SMEs validate and enhance the list of activities. Otherwise, the SMEs brainstorm and enter candidate activities into Group Outliner. Next, a facilitator chauffeurs the group through the process of structuring these nodes into an initial, tentative activity tree hierarchy. The overall group is then divided into smaller subgroups. The activities in the hierarchy are allocated across the subgroups whose members generate definitions for them. After each subgroup enters initial definitions for their assigned activities, they review the other activity definitions within the entire model. Alternative descriptions, suggestions for description refinement, and questions regarding clarification are submitted into the tool as needed. Afterward, the facilitator leads the group through selection and refinement of a best definition. The group also works with the facilitator to address any changes to the node tree that have resulted from clarification of definitions that have arisen from the discussion.

After the initial hierarchy is constructed, the group defines and attaches the ICOMs in a top-down fashion, beginning with the first activity decomposition. Participants are asked to suggest ICOMs that bound and link the parent activities. An ICOM list is generated and reviewed by participants to identify candidate ICOMs associated with activities. For each decomposition, the primary border ICOMs that span main branches of the tree are identified and entered first. Only after these are attached to the activities and defined are the arrows internal to the decomposition considered. As new ICOMs are identified and attached, SMEs enter the definitions. Thus, the facilitator converses with group members about candidate ICOMs and records the attachments, while various SMEs help define the ICOMs through their individual workstations.

Activities are altered as necessary in light of the greater clarity made evident when the ICOM attachments are considered. Activities are also merged or split, promoted or demoted among levels, or deleted as necessary to improve the logical construction of the model.

## Model Analysis and Reconciliation

Throughout the development of the activity model, the analyst and facilitator review the model content to ensure that modeling rule violations are not overlooked by the SMEs. Warning dots are displayed on the model viewer to help the SMEs identify IDEF errors or model inconsistencies, but the SMEs often get so involved in entering new model content that they forget to review these errors or inconsistencies. The facilitator can prompt the SMEs to review certain modeling violations and then provide assistance in fixing the problems, as necessary.

Model reconciliation is a critical part of the collaborative development process. When SMEs are divided into subgroups to work on different parts of the model, it is necessary to bring the whole group together periodically to review each subgroup's portion of the model and how each portion may have impacts on the other parts of the model. AM's model analysis function can also be used to determine where certain problems might exist in the model. Performing this periodic model analysis and reconciliation keeps the model from getting too far out of sync and keeps the whole group informed of the modeling being performed by the individual subgroups. If the group keeps up with the model analysis and reconciliation throughout the session, the analyst's model cleanup time at the end of the session is greatly reduced.

## Collaborative Data Modeling

THE DEVELOPMENT OF AN ENTERPRISE-WIDE COMMON CONCEPTUAL data model is a critical step in the creation of information systems that can take advantage of today's rapidly advancing information technology $[3, 32, 40, 46]$ . The third step in the CREV phase of the Collaborative Software Engineering Methodology is the creation of an integrated data model. In CREV, data modeling is performed in conjunction with scenario building, so that data and objects identified during the construction of scenarios can be incorporated into the data model. The organization's activity model defined in the previous step is used as a basis for defining the scope of the scenarios and data model. An activity model can also aid in determining which legacy systems, if any, need to be considered in the resulting integrated data model. It is important to involve SMEs when attempting to develop a conceptual data model that must accommodate the needs of a wide variety of users. Involvement is especially important when various constituencies within the SME population have both common and unique data needs, but whose needs are currently supported by different legacy systems based on dissimilar data models. Legacy systems are often based upon physical models that are not generalized to support a more diverse community and frequently contain a variety of data structure problems that even their own SMEs have to work around. To support the input of a variety of SMEs, an effective modeling approach is required. This approach should help groups of non-analyst SMEs engage model content in terms that they understand, support negotiation of model content, and speed group contribution of structured model content. This section discusses the group data modeling tool and methods developed at the University of Arizona that support such an approach.

## Data Modeling Concepts

Modeling is an approach that is used in many disciplines to manage complex problems $[29]$ . When analysts want to identify and describe the objects and associations among the objects of an organization, most analysts will use a data model $[46]$ . The U.S. Department of Defense offers this detailed description of data models $[27]$ :

\- A data model is a graphical and textual representation of analysis that identifies the data needed by an organization to achieve its mission, functions, goals, objectives, and strategies and to manage and operate the organization. It describes the scope, boundaries, and types of data needed to support the functional activities at all levels of the organization.

\- The data model identifies what data are sharable across functional and organizational boundaries, and what data are redundant and unnecessary. It provides the top-down, organization-wide perspective needed for planning, designing, building, and maintaining future integrated information systems with a single point of entry for data and contains information about the business rules of the organization.

\- Data modeling techniques and tools help management and other personnel to accurately plan, identify, represent, relate, standardize, and store the data needed by the organization.

Creating the conceptual data model of an organization is a challenging task. Regardless of the approach or method used to model, four main steps are accomplished during the development of a conceptual data model. These steps are:

\- First, it is necessary to identify, name, and textually define entities within the business area about which information is stored. The selection of an appropriate name and the construction of a meaningful, unambiguous textual definition for each entity is important. Appropriate names and definitions allow an entity to be easily understood and differentiated from other entities in the model. It is important for groups of SMEs to identify, name, and textually define entities collaboratively so that they can be understood by the larger user community.

\- Second, attributes, the pieces of data that may be stored about each entity, must likewise be identified, named, and given textual definitions. The different views of various SMEs must be reconciled into the conceptual model [17].

\- Third, meta-data must be defined for each of the attributes. In the context of attribute definition, meta-data refers to information about the data. In addition to the textual attribute definitions discussed above, meta-data includes other information about each attribute such as data type, field width, and general and enumerated domain values. Meta-data provides useful information that gives the attribute meaning [10]. It also dictates the acceptable values that may exist for the attribute, known as its domain.

\- Fourth, the relationships or associations among the objects must be defined. The identification of valid relationships among the entities is critical during data design.

## Traditional Data Model Development Approach

As mentioned earlier, current tool support for data model development is dominated by single-user, analyst-oriented tools. With the help of an analyst, groups use flip charts, whiteboards, or pencil and paper to define entities, attributes, and meta-data $[1, 58]$ . When all information flows through a single person, the modeling process is hindered significantly. Contributions from SMEs may be limited as they tire of the process or forget contributions they would like to make because they have to wait their turn. Also, model content is subject to incorrect interpretation by the scribe. The collaborative data modeling tool was developed to address these issues.

## Group Data Modeler

## Development History

Over the past four years, researchers at the Center for Management Information at the University of Arizona have developed EMS modeling tools and methods to support data model development $[21, 40, 41]$ . An understanding of the issues involved in collaborative data modeling has been advanced through the development of a number of group data modeling prototype tools. Current development efforts have focused on tools and user interfaces that can support tasks that novice data modelers can be expected to perform. This collaborative modeling tool, named Group Data Modeler (GDM), is currently in its third major version.

## Collaborative Modeling Interface

The GDM tool includes several simple user interfaces to reduce complexity for non-analysts. The tool allows multiple participants to work in parallel to contribute and review model content. It supports parallel access at the entity level, attribute level, and meta-data level. Entities are presented as an indented list, with the number of attributes for each entity displayed to the left in parenthesis (see figure 6).

This easy-to-use interface provides the SMEs with the ability to build a hierarchical listing of entities in support of entity types or categories. Several persons can add entities in parallel, and participants can offer different entity definitions for the same entity at the same time.

GDM also provides an interface that allows participants to contribute different attributes for the same entity at the same time. The attribute entry and definition screen is shown in figure 7. From this screen the participants not only enter the names of the attributes, but also select the data type and designate whether the attribute is a keyfield. In selecting a data type, the SMEs select one of four simplified types: number, alpha-numeric, memo (free-flowing text), or date.

The final set of data entry screens within the GDM are for entering the meta-data specific to each attribute. The tool displays a different meta-data screen, depending on the data type selected for the attribute. Only the meta-data fields specific to the attribute's data type need to be entered by the SMEs (see figures 8 and 9).

## Group Coordination and Group Access Management Mechanisms

Like AM, GDM has several features designed to support group coordination and to enable the facilitator to manage SMEs' access to the data. GDM provides the facilitator with the ability to set group access rights to different GDM functions. Rights can be set for adding/deleting/modifying entities and attributes and their definitions. The facilitator can also turn off or on SMEs' right to access the meta-data for attributes. These rights can be assigned to the group as a whole, or selected rights can be assigned to individuals or subgroups as necessary.

![](/api/attachments/ZGD4J8N8/fulltext/images/828f800ce8cb61cae7b17ab4218dfd7c91e70e966cbd8452caeafc4a89d9375f.jpg)  
Figure 6. Entity List in the GDM

## Import/Export

It is often necessary to import data from another tool into GDM or to export data from GDM into a different tool. GDM currently supports import from and export to the ERWIN data modeling tool from LogicWorks. This feature facilitates using GDM for group review and validation of existing data models without having to rekey or cut/paste the data between tools. Future versions of the tool will support import/export to other data modeling tools, as required.

## Facilitation Using GDM

With the exception of a few preliminary items, the collaborative approach to data model development follows the same steps discussed previously in the section on data modeling concepts. The following sections describe in detail the collaborative approach.

## SME Training

Learning the complexities of data modeling requires considerable effort and experience. Goodhue et al. [32] questioned the practice of trying to provide extensive training in the data modeling process to participants. Some training, however, helps explain the basic concepts sufficiently to give SMEs a high-level overview of modeling constructs and how they will be asked to participate. About thirty minutes of initial training is provided to set the stage at the beginning of the meeting; then focused just-in-time training specific to each of the sequential modeling stages is provided at appropriate times. This makes the modeling constructs and tasks less intimidating and keeps the training directly relevant to each of the respective tasks in turn.

![](/api/attachments/ZGD4J8N8/fulltext/images/fc34b31a6078c9d419e77d0c00f2cafc752d21a10a69af09619471c557380d03.jpg)  
Figure 7. Attribute Definition and Simplified Data Type Selection Form in GDM

## Preliminary Preparation

When possible, it is preferable to perform preliminary analysis before the meeting to educate the analyst and to develop a draft model, rather than starting from scratch in a group meeting. It is easier for a group to fix and build upon a reasonable starter representation. This draft model may be developed using legacy systems and SME interviews.

Once the group meeting actually begins and the SMEs have had some data modeling training, the scope of the model is reviewed to establish the model boundaries. The group is then led through a review of the draft model so that they can identify what content is in the draft model—and what is not. This serves as the initial overview of the model and at the same time permits SMEs to make suggestions about obvious errors and omissions. The analysts use this input to make obviously needed changes to the model.

![](/api/attachments/ZGD4J8N8/fulltext/images/4b0a05e4bf9dba5186db7fb63bdf8c737b3af75abf4962416c8952c03a5d6ab7.jpg)  
Figure 8. Meta-Data Definition Form for a Numeric Data Type

## Identify, Name, and Textually Define Entities

After reviewing the draft model, the entity list is made available to all SMEs through the EMS modeling tool environment. At this point, the emphasis is on identifying, naming, and textually defining the entities. SMEs may suggest new entities that do not exist in the model and are also asked to review existing entity names and their corresponding textual definitions for appropriateness. The GDM allows SMEs to work in parallel, at their own pace, as they work through the entire entity list (see figure 6).

SMEs are asked to post questions and new or improved entity definitions into the GDM. Questions may be raised regarding what real-world objects are represented by entity abstractions and whether particular entities, including those in inheritance hierarchies, are appropriately differentiated from each other. Each group member may see the inquires and suggestions posted by the other members. SMEs and analysts can evaluate what is known, is unknown, or is unclear in a nonthreatening environment.

Next, the facilitator or analyst leads the group through a chauffeured review of the definitions and comments. Each of the definitions and comments is displayed on the public screen. SMEs can follow along on the public screen or on the screen at his or her individual workstation. During this review, suggested names and definitions are considered. More meaningful names may be identified. A candidate definition may be selected or parts of multiple candidate definitions may be merged to form the final definition. This chauffeured review is made more effective because SMEs have worked through the model and have documented ambiguities and suggestions in the GDM.

![](/api/attachments/ZGD4J8N8/fulltext/images/9031cf21172b71f2ec1a76401087eba7f4df3e489af1318782029adabb395d86.jpg)  
Figure 9. Meta-Data Definition Form for an Alpha-Numeric Data Type

Beyond the added model validity and clarity resulting from such a collaborative effort, another benefit is the comprehension that SMEs achieve about the entity abstractions. This understanding helps substantially in later modeling tasks.

## Identify, Name, and Textually Define Attributes

The fact that, so far, the group has been led through a careful review of the entities allows SMEs to identify attributes (referred to as “data elements” in some methods) in light of that understanding. The SMEs’ grasp of the entities allows them to work in parallel to identify, name, and define the attributes associated with those entities.

The approach is similar to the approach used to identify and define entities. SMEs first work in parallel to visit the respective entities. For each entity, they identify, name, and textually define attributes (see figure 7). Again, a chauffeured stage is used to evaluate the comments, to refine the names and definitions, and to facilitate the group's arrival at agreement.

This electronically supported approach differs from traditionally supported meetings. In traditional meetings, attribute identification and definition tend to be done in a completely chauffeured manner. With the GDM, SMEs can contribute attribute information to the same entity at the same time or work behind different entities. This allows each individual within the group to contribute and evaluate attributes at his or her own pace. In addition, individuals with expertise on certain entities may spend more of their time where they have the most expertise. Analysts can monitor the electronic discussion to review the group's contributions in a nonthreatening, rapid fashion. Then, the analyst helps the group evaluate and restructure the information during the chauffeured stage.

## Define Other Attribute Meta-Data

With a textual definition of each attribute agreed upon by the group, the stage is now set for the definition of the attribute meta-data. The biggest challenge of this task to SMEs is complexity. SMEs can easily be overloaded by complexity, so it is essential to provide an effective approach to obtaining meta-data information.

Meta-data can be very difficult to define. Our research has shown that when SMEs were asked to fill out a generic form displaying detailed meta-data dimensions, they were overwhelmed by the complexity of the meta-data definition task. However, when given forms displaying meta-data dimensions specific to simplified data types, SMEs were able to fill in those dimension much more easily (see figures 8 and 9).

The GDM displays meta-data dialog forms specific to each simplified data type. SMEs select the data type for an attribute with the help of the analyst. Then, when entering meta-data, the GDM automatically presents the appropriate meta-data form, based on the data type selected. In this way, SMEs can define meta-data in terms that they can understand. They are spared having to deal with the analyst-centered data standardization view of the conceptual data model.

The process used during this stage is similar to that at previous stages. SMEs work from attribute to attribute, posting appropriate meta-data. Questions and suggestions are also entered. Later, these are addressed by the group with the assistance of the analyst during a chauffeured review. The meta-data definition feature in the GDM allows groups efficiently to define information that previously was very difficult and time-consuming to obtain. Both parallelism and structure are provided. Without this type of support, we have observed that analysts often deemed it too difficult to capture some information. For example, when participants resisted taking the time in a meeting to obtain meaningful high and low limits for numeric attributes, we have seen an analyst fail to get a group to specify these carefully. As a result, the eventual domain implementation may not have been adequately restrictive.

## Identify the Relationships among the Objects

Defining relationships for a domain can be a formidable task. Participants have difficulty establishing and evaluating relationships without the help of a qualified analyst. Relationships are considered at various times throughout the overall meeting. Analysts often come to a meeting with questions about relationships that they ask at different times throughout the meeting. Some questions surface during the initial model overview at the beginning of the meeting. Others arise while the group is working on the entity and attribute definitions. Finally, some are asked during one or more focused relationship reviews. These reviews are much more effective when SMEs have gone through the stages of the modeling process, an experience that has helped them engage and comprehend aspects of the model.

The GDM does not support direct storage of relationships, although relationship or business rule information could be stored as a comment for the entities. Early prototypes of the GDM did support relationships, but it was found that analysts preferred to update the relationships in their own CASE tools $[40]$ . Moreover, textual representations of the relationships were not understood by SMEs without the assistance of an analyst.

## Results

WE HAVE USED VARIOUS VERSIONS OF AM, GDM, and GroupSystems with actual business personnel working on a multitude of complex problems. Many of our modeling meetings have been to collect and reconcile requirements from diverse groups who traditionally have had their own legacy systems that contained partially overlapping functionality. For example, we have worked with many groups comprised of representatives drawn from the U.S. Army, Navy, Air Force, Marines, Defense Logistics Agency (DLA), and other government organizations that are trying to define common requirements that will satisfy the larger user community. Often, we have had participants in our meetings who were users or developers of legacy systems and who would be affected by the decisions made in the meeting, underscoring the need to support negotiation and decision making for key stakeholders. Although use of EMS modeling tools are not limited to nontrivial systems, our work has dealt with larger, complex systems containing data shared across multiple business areas. Thus, we have had also to support data standardization and component integration. Working with small groups would have been overly restrictive since the tasks we were addressing required broad user involvement. At the same time, supporting larger groups with traditional single-user tools would have been painful at best. EMS modeling tools and GEMS technology have allowed us to support these larger groups.

A detailed comparison of groups supported by traditional single-user tools and groups supported by AM is available in $[19, 22, 23]$ . In brief, AM allows a model to be built considerably faster by a greater number of SME participants. For example, in our study of AM, models were built two to three times faster than models developed with the traditional approach. The AM-supported group size in our sample averaged double that of the traditionally supported groups. However, the average EMS-supported participant was 60 percent more productive than a person who participated in smaller, traditionally supported groups. In terms of model quality, models constructed with AM were of equal or superior quality to models developed with the traditional approach when supported by appropriate facilitation. Activity and ICOM descriptions tended to be longer and more descriptive, presumably because all content did not need to be filtered through the analyst or scribe.

We are currently completing a study evaluating modeling productivity and the quality of models developed with GDM. In this study we are comparing data models developed with GDM with those developed using single-user tools and those developed with GEMS. Our preliminary findings suggest that GDM-supported models are developed more quickly and with more detail than models developed with the other two approaches. Moreover, GDM is particularly easy for SMEs to use.

The simple-to-use, group-enabled collaborative interfaces of AM and GDM made content contribution possible for the typical non-analyst user in our studies. Users were able to navigate in models and add content, including content that has traditionally been collected only through serial interviews and chauffeured meetings.

AM and GDM overcame model access limitations imposed by traditional, single-user tools as SMEs were able to see and edit parts of the model in parallel. SMEs were able to pose questions and provide candidate definitions directly instead of having to work through a scribe. Rather than being limited to verbal contributions, SMEs typed in contributions and were also able to see contributions typed in by other SMEs.

Although the tools enabled parallelism, the best results were achieved when the meeting process was structured to achieve a combination of parallel contribution and chauffeured convergence reviews. By alternating parallel contribution with periodic chauffeured reviews, groups received the support necessary to achieve both agreement and closure. The groups worked best when they were guided through the scoping and decomposition of key parts of the models. However, as the process continued, parallel work had to be well orchestrated. Otherwise, model content became redundant and fragmented. Initially, SMEs best engaged the overall model development process in stages where their attention could be devoted to one abstraction framework at a time before moving to the next. As SMEs became more experienced with model semantics, they were able to move among the abstraction levels more easily.

SMEs did not need extensive premeeting training in the modeling methods to contribute productively during model development. When supported by facilitators who know how to conduct the group modeling process effectively, SMEs were able to work productively. A combination of a brief initial training, just-in-time training during the process, and ongoing support by the facilitator (and analysts as necessary) was sufficient to allow the groups to be productive.

## Discussion

WE BEGAN THIS PAPER BY ASKING THE QUESTION: What are the key attributes of a collaborative software engineering methodology that will enable effective and efficient involvement of groups of users? The first step toward answering this question was to define who the users should be. Most methodologies view users at the individual level, gathering their input during one-on-one analyst/user interviews. RAD views the users as selected user representatives who work directly with the development team to create models and system prototypes. JAD broadens user participation by involving a group of key users directly in its requirements determination and other design meetings. Because our methodology is designed to support complex systems supporting a large, heterogeneous user population, the Collaborative Software Engineering Methodology incorporates and extends these views of the user. As shown in figure 1, the methodology explicitly defines a three-layered view of users: selected user representatives, the user group (SMEs), and the entire user community.

The next step was to define when the users should be involved in the software engineering process. While traditional methodologies primarily involve users only in the early and very late phases of the life cycle, the Collaborative Software Engineering Methodology takes a RAD-like approach by explicitly involving users in all phases of development. However, unlike RAD, the methodology leverages on its layered view of user participation to maximize both the breadth and the efficiency of that involvement. Specifically, it interweaves involvement by individual user representatives for activities such as preliminary model development, by groups of SMEs for more diverse requirements gathering or model refinement/validation, and by the broader user community in initial needs surveys and wide-scale beta testing. Examples of these different levels of user involvement are provided in figure 1 and as part of the discussion of the Collaborative Software Engineering Methodology.

Given this framework for user involvement, the focus of our research then turned to ensuring the efficiency and effectiveness of that involvement. To accomplish this goal, we combined the power of today's best systems development practices with the efficiencies of collaborative technologies into a comprehensive Collaborative Software Engineering Methodology. The description of the Collaborative Requirements Elicitation and Validation (CREV) phase of the methodology provides many examples of how these best practices were integrated into the methodology. To identify business activities (CREV step 1), the methodology incorporates IDEF0's and information engineering's business activity modeling concepts, but streamlines the process by decomposing only activities with IS potential rather than decomposing all activities to create a comprehensive model. Information engineering and other data modeling concepts are implemented into CREV step 3, but with an emphasis on learning from business scenarios to speed data model development. Successful OO concepts such as scenarios and system use cases are also implemented in the methodology, but with a specific emphasis on the need to transition from a business scenario focus (CREV step 2) to a system use case focus (CREV step 4). Prototyping is explicitly incorporated in the requirements (CREV step 5) and development phases. The methodology also shows how these best practices can be linked. The activity model provides structuring to guide concurrent development of the business scenarios and data model, which are used to define system use cases. Data models and use cases are implemented in prototypes that are used to refine and validate all these components of the final requirements specification.

Integrating these best practices was not sufficient to ensure the efficiency and effectiveness of user group involvement. User group meetings are notoriously inefficient. JAD takes a first step toward improving the outcomes of requirements meetings by emphasizing meeting planning, a structured process, and the value of facilitation, but has not traditionally been supported by GEMS or EMS modeling tools. Use of collaborative technologies not only improves the efficiency of meetings, it also allows direct contributions by users because it eliminates the process and information losses of chauffeured meeting methodologies such as JAD. Use of general-purpose collaborative technologies is a first step toward eliminating these losses and is incorporated in the Collaborative Software Engineering Methodology. For example, GroupSystems Group Outliner is often used to define high-level business activities (CREV step 1) and generate business scenarios (CREV step 3). In addition, both GroupSystems Categorizer and Survey are used during structured prototype evaluations (CREV step 5). However, as supported by our experiences with AM and GDM, many life-cycle activities may be better supported by EMS modeling tools that have been specifically designed for requirements gathering from non-analysts. The complex tools used by analysts can overwhelm non-analyst users, so EMS modeling tools must be designed with simplified interfaces for non-analysts. Therefore, an essential element of our Collaborative Software Engineering Methodology is the development of requirements modeling abstractions that enable direct SME contributions but also give developers what they need to understand requirements. Making collaborative model development possible is the primary route to ensuring efficient and effective user involvement. The remainder of this section focuses on what is required to enable collaborative modeling.

Figure 10 reflects essential components of collaborative modeling support. First, collaborative modeling tools enable SMEs to interact directly with models while working in parallel. Such tools must contain a user-comprehensible interface, essential for complexity management. Modeling aids within collaborative modeling tools can also benefit model development, as can model access controls that help govern what parts of the model users can access and what operations they are allowed to perform.

Second, CASE tools serve as enablers to collaborative model development. The ability to import and export modeling information from CASE tools allows for migration of models among collaborative modeling tools and CASE tools. CASE tools may also be used to provide graphical and analytical support during meetings. Export to CASE is important because CASE tools are sometimes used to generate physical data bases, conduct further analysis, and generate code.

Third, appropriate group processes are required for effective use of collaborative modeling tools. Fourth, for best results, a facilitator and/or analyst who understand the method, the tools, and the meeting process should support the meeting.

## Collaborative Modeling Tools

To allow efficient participation by large groups of SMEs, collaborative modeling tools provide concurrent access that allows SMEs to work in parallel, thereby helping overcome a significant productivity bottleneck inherent in meetings supported by single-user tools. Users are not limited to seeing only a part of the model shown to them by the facilitator and can confidently type in content that is not subject to excessive initial filtering by the facilitator.

## User-Comprehensible Collaborative Interface

EMS modeling tools should provide ease of use for non-experts while retaining some functionality traditionally available only in CASE tools. Although ease of use is important to all software implementations, it is especially important in EMS modeling tools. Simplification is critical because SMEs should not be cognitively overloaded by the modeling tool interfaces. Rather, they should be able to learn to use the essential features of the tools very quickly, so they are free to focus on model content. To accomplish this, EMS modeling tools should manage complexity by presenting SMEs with views such as simple lists and graphics, but should also allow SMEs to obtain more detail. Users should be able to add and edit items easily. When graphics are supported in an EMS modeling tool, SMEs should be able to move easily among the various graphical views. One of the benefits of EMS modeling tools over GEMS is that relationships among objects may be captured explicitly, but information hiding is also important in reducing cognitive load. For example, in AM, SMEs may focus on activity and ICOM names and definitions, even though additional forms are available to capture ICOM connections, improvement ideas, and other information such as cost, duration, and frequency. Our experience suggests that skilled analysts move easily among the abstraction levels; novices do not. Allowing non-experts to focus at one level of information at a time reduces complexity. Beyond information hiding, simplification of the underlying conceptual model may also help reduce complexity. For example, our simplified presentation of data modeling semantics within GDM radically reduced complexity.

![](/api/attachments/ZGD4J8N8/fulltext/images/4f6fc9927da8fe7078d42006cbfc64177100c8175f759685cd1f6c7b0403ccf5.jpg)  
Figure 10. Collaborative Modeling Enablers

## Modeling Aids

Modeling aids offer essential collaborative support for some modeling methodologies. Their importance depends on the complexity of the modeling method semantics, as well as on how self-contained the definable objects are within the method—that is, how well SMEs can define objects with only a partial picture of other related objects and the relationships among the objects. For example, during data modeling, entities and attributes may often be defined initially without having a detailed understanding of all of the relationships among the entities. Users can often conceptualize entities and the attributes associated with them after just a preliminary view of the relationships obtained from draft models and verbal discussion. Because graphical views of the relationships may be done periodically with the aid of a single-user CASE tool, we did not include graphical support in GDM. Conversely, during the definition of IDEF0 models, graphical views of ICOM attachments are needed to conceptualize activities. Attempting to bring activities into focus without these graphical views is counterproductive. Moreover, being able to identify which ICOMs are not consistently used across related diagrams is very beneficial, so incorporation of these aids was essential to AM.

Modeling aids can be separated into two types: aids primarily used by SMEs during modeling and aids almost exclusively used by the facilitator. The second type assumes that the facilitator has more sophistication in the modeling method. AM has both classes of modeling aids. Errors and omissions are displayed on graphics for the benefit of both SMEs and the facilitator, whereas the more comprehensive analytical engine tends to be used periodically by the facilitator to identify modeling errors, inconsistencies, and omissions. Designers of EMS modeling tools should consider the potential benefit of each type of aid.

## Model Access Controls

It is helpful to have model access controls in EMS modeling tools. Both AM and GDM have features to support group coordination and to permit the facilitator to manage SMEs' access to models. Both tools let the facilitator start and stop participants from the leader station. Moreover, the facilitator can enable and disable SMEs' ability to edit items and relationships. This is especially useful for locking items that have been agreed upon or helping a group focus on specific aspects of the model.

## Case Tool Support and Access

Whether or not CASE tool support is required during collaborative modeling meetings depends on the sophistication of the collaborative modeling tools. For example, AM modeling aids are sufficiently complete to ensure that no CASE tool is required to support collaborative model development. Conversely, although GDM may be used without a CASE tool, CASE support is helpful when relationships among entities are many and complex. The ability to import and export modeling information among CASE and EMS modeling tools can be useful. Import from CASE tools to collaborative modeling tools allows models developed in single-user tools to be reviewed and edited in a collaborative environment. Being able to export from EMS modeling tools to CASE means that models can be easily moved to single-user tools. This is also useful when CASE tools offer features beyond those found in EMS modeling tools.

## Effective Group Process

Appropriate processes are essential to effective meetings and are valuable research contributions in and of themselves. Our research over the last five years has demonstrated that effective methods can only be developed through iterative action research. They must be developed through trial and refinement.

Parallel access allows people who are not modeling experts to contribute. Consequently, without proper process and facilitation orchestration, unreconciled, messy models result $[22, 23]$ . With chauffeured meetings conducted with single-user tools, the analyst has control at the point of initial insertion into the model and can therefore filter input at the point of origin. On the other hand, with collaborative modeling tools, content oversight must be provided without diminishing the benefits of parallel work. Our early attempts at conducting IDEF0 modeling with collaborative tools did not support enough convergence and therefore resulted in too many overlapping and unreconciled abstractions. We subsequently developed a group process that allowed parallel work, helped SMEs comprehend the model, achieved modeling efficiency gains, and produced high-quality models $[22, 23]$ .

When different individuals or subgroups work on a part of a model, they must develop contexts and frames for how the parts fit together. Unless this is done, overlapping and inconsistent abstractions result. Furthermore, SMEs must be led in frequent convergence exercises in which they cross-review and reconcile their respective preliminary contributions. Moreover, economy can be gained by letting SMEs cycle among different parts of the model to make candidate definitions, comments, and suggestions in the collaborative modeling tools before engaging in convergence exercises. Finally, it is important to break the modeling process into stages so that SMEs can focus on one abstraction framework at a time before moving to the next. For example, having SMEs name and define entities first, then define attributes, and then enter meta-data allows SMEs to stay primarily focused on a single abstraction framework at time. As they become more experienced in the modeling method, SMEs can develop the ability to move easily and rapidly among the different abstraction frames.

## Facilitator/Analyst Support

The facilitator works jointly with a systems analyst when planning and conducting requirements meetings. Synergy results when good analysts and good facilitators work together as a team. The systems analyst participates in all requirements activities prior to group meetings and is essential for maintaining continuity throughout the entire process, bringing to it a knowledge of what requirements information is already known and what needs to be obtained. Ideally, analysts should have looked at legacy systems, legacy data models, and other historical artifacts to develop initial concepts, straw models, and questions. They know how to untangle complicated requirements constructs and represent them in the modeling languages and CASE tools.

Facilitators are scarce but important enablers of the effective use of collaborative modeling tools and GEMS in a collaboration-based life cycle. Skilled facilitation is essential for the best outcomes. Facilitators help plan and conduct the group meetings. A facilitator's expertise should include: (1) a grasp of meeting planning and general facilitation principles such as meeting processes and group dynamics, (2) an understanding of how a specific meeting and requirements abstraction fits into the overall requirements gathering life cycle, (3) a knowledge of the requirements specification methodology used in the meeting (e.g., for data modeling meetings, the facilitator should understand data modeling semantics), and (4) a knowledge of how to use GEMS and collaborative modeling tools to facilitate requirements gathering meetings.

Some analysts are highly skilled technically but lack expertise on how to use GEMS and collaborative modeling tools to collect requirements. Furthermore, some facilitators can run general meetings but have not developed the skill to run requirements meetings. We have found that the latter facilitation skill is so rare that a few facilitators tend to work multiple projects, unlike analysts who tend to be dedicated to one or two projects because of their need to remain intimately involved with the content. It is helpful, however, if the same facilitator can continue to work on the same project in order to retain continuity from meeting to meeting.

## Conclusions and Future Research

THE COLLABORATIVE SOFTWARE ENGINEERING METHODOLOGY DEFINED IN THIS PAPER provides a framework for effective and efficient user involvement throughout the systems development process. This methodology includes mechanisms to support three layers of user involvement: selected user representatives, user groups (SMEs), and the entire user community. Specifically, it includes intimate involvement of individual user representatives for development of preliminary models and prototypes, groups of SMEs to refine, validate, and prioritize requirements, and the broader user community during initial needs surveys and wide-scale beta testing.

Participation of multiple SMEs is beneficial for both content and political reasons. Group meetings provide a useful mechanism to involve multiple SMEs. JAD takes a first step in improving the outcomes of requirements meetings by emphasizing meeting planning, a structured process, and the value of facilitation. However, traditional JAD meetings have been supported by single-user tools and processes that impose significant productivity and participation bottlenecks on meetings.

EMS modeling tools and GEMS can be powerful enablers of collaborative systems development meetings. Their use can provide a number of benefits. First, these tools appear to break a significant productivity bottleneck associated with the traditional approach. EMS support allows a model to be built considerably faster by a greater number of participants. Although users are working in a group, individual productivity is higher than for individuals working in small groups supported by the traditional chauffeured approach. Second, EMS support makes it easier for users to contribute directly. Thus, users can comprehend and feel ownership of the models and the decisions. Third, since more people may contribute, the likelihood that critical requirements will be missed is reduced. The ability of more people to engage the models effectively allows for contribution, resolution, and negotiation of requirements by key stakeholders. Involvement is focused during meetings rather than through a series of drawn out review-and-revision cycles that occur when serial interviews are used. Projects can therefore move forward to the next stage rather than being bogged down in analysis paralysis. Finally, the ability to speed requirements development makes it more likely that key personnel will participate. It also increases the likelihood that projects will be completed since management and user commitment tends to falter when systems development drags on seemingly forever.

The Collaborative Software Engineering Methodology also provides a framework for requirements abstractions that can be developed by SMEs in an effective order. Since it is impossible to produce useful monolithic requirements specifications at the beginning of a project, requirements need to be uncovered in stages and represented in multiple, internally consistent abstractions. It supports the statement of requirements in activity models, data models, scenarios, systems use cases, and prototypes. Together, these requirements abstractions provide the key information necessary for systems design.

Additional refinements to the Collaborative Software Engineering Methodology will be made as part of our future research. More EMS modeling tools are needed to enhance the methodology. For example, we have identified the need for a collaborative modeling tool to support business scenario modeling, though we have not yet developed this tool. Collaborative tools that can support other requirements representations may also be useful. The functionality of GDM will also be enhanced. Tools and methods to support distributed collaboration may also help during systems development projects. Finally, we will be conducting a longitudinal case study of the entire methodology to measure its benefits and to further refine it based on those results. The Department of Defense is continuing to fund our research to address these initiatives.

In conclusion, we believe that the Collaborative Software Engineering Methodology and the tools discussed in this paper represent a significant step forward in supporting user involvement during systems development projects. This methodology, with the above enhancements, can become the key to success in responding to the rapidly changing information processing needs of today's organizations.

## REFERENCES

1. August, J.H. Joint Application Design: The Group Session Approach to System Design. Englewood Cliffs, NJ: Yourdon Press, 1991.

2. Banker, R.D., and Kauffman, R.J. Reuse and productivity in integrated computer-aided software engineering: an empirical study. Management Information Systems Quarterly, 15, 3 (1991).

3. Bock, D.B.; Klepper, R.W.; and Sumner, M.R. Avoiding the pitfalls of implementing

enterprisewide modeling. Data Resource Management, 3 (Spring 1992), 13–21.

4. Boddie, J. Crunch Mode. Englewood Cliffs, NJ: Prentice-Hall, 1987.

5. Boehm, B. A spiral model of software development and enhancement. Proceedings of an International Workshop on the Software Process and Software Environments, Coto de Caza, CA, 1985.

6. Booch, G. Object-Oriented Analysis and Design, 2d ed. Redwood City, CA: Benjamin/Cummings, 1994.

7. Bostrom, R.P.; Anson, R.; and Clawson, V.K. Group facilitation and group support systems. In L.M. Jessup and J.S. Valacich (eds.), Group Support: New Perspectives. New York: Macmillan, 1993, pp. 146–168.

8. Bourne, K.C. Putting rigor back into RAD. Database Programming and Design, 7, 8 (1994).

9. Brooks, F. No silver bullets. IEEE Computer (April 1987).

10. Bruce, T.A. Designing Quality Databases with IDEF1X Information Models. New York: Dorset House, 1992.

11. Carmel, E. Supporting joint application development with electronic meeting systems: a field study. Ph.D. dissertation, University of Arizona, 1991.

12. Carmel, E.; George, J.F.; and Nunamaker, J.F., Jr. Supporting joint application development (JAD) and electronic meeting systems: moving the CASE concept into new areas of software development. Proceedings of the 25th Annual Hawaii International Conference on System Sciences, 1992.

13. Carmel, E.; George, J.F.; and Nunamaker, J.F., Jr. Examining the process of electronic-JAD. Journal of End User Computing, 7, 1 (1995), 13–22.

14. Chen, M., and Liou, Y.I. The design of integrated group support environments. Proceedings of the 24th Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1991, pp. 333–342.

15. Chen, M.; Nunamaker, J.F., Jr.; and Weber, E.S. Computer-aided software engineering: present status and future directions. DATABASE (Spring 1989), 7–13.

16. Conger, S. The New Software Engineering. Belmont, CA: Wadsworth, 1994.

17. Date, C.J. An Introduction to Database Systems, 5th ed., vol. 1. Reading, MA: Addison-Wesley, 1990.

18. Davis, R.J. Management Framework for Process Improvement. Washington, DC: Office of the Director of Defense Information, 1993.

19. Dean, D.L. Electronic meeting systems tools and methods to increase group participation and productivity during business process modeling. Ph.D. dissertation, Management Information Systems Department, University of Arizona, 1995.

20. Dean, D.L.; Lee, J.D.; Orwig, R.E.; and Vogel, D.R. Technological support for group process modeling. Journal of Management Information Systems, 11, 3 (Winter 1995–96), 43–64.

21. Dean, D.L.; Lee, J.D.; and Vogel, D.R. Group tools and methods to support data model development, standardization, and review. Thirtieth Annual Hawaii International Conference on the System Sciences. Maui, HI: IEEE Computer Society Press, 1997, pp. 386–395.

22. Dean, D.L.; Orwig, R.E.; and Vogel, D.R. Facilitation methods for use with EMS tools to enable rapid development of high quality business process models. Proceedings of the 29th Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1996, pp. 472–481.

23. Dean, D.L.; Orwig, R.E.; and Vogel, D.R. Meeting methods for use with EMS tools to enable rapid development of quality business process models. Group Decision and Negotiation, forthcoming.

24. DeGrace, P., and Stahl, L.H. Wicked Problems, Righteous Solutions: A Catalogue of Modern Software Engineering Paradigms. Englewood Cliffs, NJ: Yourdon Press, 1990.

25. DeMarco, T. Structured Analysis and System Specification. Englewood Cliffs, NJ: Prentice-Hall, 1979.

26. Dennis, A.R.; Heminger, A.R.; Nunamaker, J.F., Jr.; and Vogel, D.R. Bringing automated support to large groups: the Burr-Brown experience. Information and Management, 18, 3 (1990), 111–121.

27. Department of Defense. Data Administration. Washington, DC: U.S. Government Print-

ing Office, 1994.

28. Department of Defense. DoD 8020.1-M. Functional Process Improvement: Functional Management Process for Implementing the Information Management Program of the Department of Defense. Washington, DC: Director of Defense Information, Office of the Secretary of Defense, 1992.

29. Edwards, P. Models and analogy in science. In P. Edwards (ed.), Encyclopedia of Philosophy. New York: Free Press, 1967, pp. 354–359.

30. Fichman, R.G., and C.F.K. Object-oriented and conventional analysis and design methodologies: comparison and critique. Compute (October 1992).

31. George, J.F.; Dennis, A.R.; and Nunamaker, J.F., Jr. An experimental investigation of facilitation in an EMS decision room. Group Decision and Negotiation, 1 (1992), 57–70.

32. Goodhue, D.L.; Kirsch, L.J.; Quillard, J.A.; and Wybo, M.D. Strategic data planning: lessons from the field. MIS Quarterly, 16, 1 (March 1992), 11–34.

33. Gordon, V.S., and Bieman, J.M. Rapid prototyping: lessons learned. IEEE Software (January 1995), 85–95.

34. Hirokawa, R.Y., and Gouran, D.S. Facilitation of group communication. Management Communication Quarterly, 3, 1 (August 1989), 71–92.

35. IBM Corporation. Business Systems Planning—Information Systems Planning Guide. IBM, 1975.

36. Jacobson, I.; Christerson, M.; Jonnsson, P.; and Overgaard, G. Object-oriented software engineering—a use case driven approach. Reading, MA: Addison-Wesley, 1992.

37. Katic, N.; Nvstrujev, B.; Vogel, D.R.; and Pendergast, M.O. Bridging the gap between structured requirements and object-oriented analysis and design. Proceedings of the 29th Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1996, pp. 525–534.

38. Kemerer, C.F. How the learning curve affects CASE tool adoption. IEEE Software, 9, 3 (1992).

39. Konsynski, B.R.; Kotteman, J.E.; Nunamaker, J.F., Jr.; and Stott, J.W. PLEXSYS-84: an integrated development environment for information systems. Journal of Management Information Systems, 1, 3 (Winter 1984–85), 64–104.

40. Lee, J.D. Group data modeling support for business process reengineering. Ph.D. dissertation, Management Information Systems, University of Arizona, 1995.

41. Lee, J.D.; Dean, D.L.; and Vogel, D.R. Tools and methods for group data modeling: a key enabler of enterprise modeling. ACM SIG Group Bulletin, 18, 2 (August 1997), 59–62.

42. Liou, Y.I., and Chen, M. Using group support systems and joint application development for requirements specification. Journal of Management Information Systems, 10, 3 (Winter 1994–95), 25–41.

43. Martin, J. Information Engineering. Englewood Cliffs, NJ: Prentice-Hall, 1990.

44. Martin, J. Rapid Application Development. New York: Macmillan, 1991.

45. Mayer, R.J. IDEF1X Data Modeling. College Station, TX: Knowledge Based Systems, Inc., 1993.

46. Navathe, S.B. Evolution of data modeling for databases. Communications of the ACM, 35, 9 (September 1992), 112–123.

47. Norman, R.J., and Nunamaker, J.F. CASE productivity perceptions of software engineering professionals. Communications of the ACM, 32, 9 (1989).

48. Nunamaker, J.F., Jr.; Dennis, A.R.; Valacich, J.S.; and Vogel, D.R. Information technology for negotiating groups: generating options for mutual gain. Management Science, 37, 10 (October 1991), 1325–1346.

49. Nunamaker, J.F.; Dennis, A.R.; Valacich, J.S.; Vogel, D.R.; and George, J.F. Electronic meeting systems to support group work. Communications of the ACM, 34, 7 (July 1991), 40–61.

50. Nunamaker, J.F., Jr.; Vogel, D.R.; Heminger, A.; Martz, B.; Grohowski, R.; and McGoff, C. Experiences at IBM with group support systems: a field study. Decision Support Systems, 5, 2 (1989), 183–196.

51. Pendergast, M.O.; Dean, D.L.; Lee, J.D.; Nevstrujev, B.; and Katic, N. Current advances in group supported business process reengineering. Proceedings of the 29th Annual Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 1996, pp. 451–460.

52. Pressman, R.S. Software Engineering: A Practitioner's Approach, 4th ed. New York: McGraw-Hill, 1997.

53. Ross, D.T. Structured Analysis (SA). A language for communicating ideas. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 16–34.

54. Ross, D.T. Douglas Ross talks about Structured Analysis. Computer (July 1985), 80–88.

55. Schach, S.R. Classical and Object-Oriented Software Engineering, 3d ed. Chicago: Irwin, 1996.

56. Teichrow, D., and Hershey, E.A. PSL/PSA: a computer-aided technique for structured documentation and analysis of information processing systems. IEEE Transactions on Software Engineering, SE-3, 1 (January 1977), 41-48.

57. UM. Integrated Computer-Aided Manufacturing (ICAM) Function Modeling Manual (IDEF0). Materials Laboratory, Air Force Wright Aeronautical Laboratories, Air Force Systems Command, Wright-Patterson AFB, OH, 1981.

58. Wood, J., and Silver, D. Joint Application Design: How to Design Quality Systems in 40 Percent Less Time. New York: John Wiley, 1989.

59. Wood, J., and Silver, D. Joint Application Development, 2d ed. New York: John Wiley, 1995.

60. Yourdon, E. Decline and Fall of the American Programmer. Englewood Cliffs, NJ: Yourdon Press, 1992.

61. Yourdon, E., and Constantine, L.L. Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design. Englewood Cliffs, NJ: Prentice-Hall, 1979.
