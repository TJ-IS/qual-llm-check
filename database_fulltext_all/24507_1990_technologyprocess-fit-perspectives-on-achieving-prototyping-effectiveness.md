---
otero_id: 24507
otero_key: "CTHU6GU6"
title: "Technology–Process Fit: Perspectives on Achieving Prototyping Effectiveness"
authors: "Jay G. Cooprider; John C. Henderson"
year: "1990"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1990.11517897"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Technology-Process Fit: Perspectives on Achieving Prototyping Effectiveness

Jay G. Cooprider & John C. Henderson

To cite this article: Jay G. Cooprider & John C. Henderson (1990) Technology-Process Fit: Perspectives on Achieving Prototyping Effectiveness, Journal of Management Information Systems, 7:3, 67-87, DOI: 10.1080/07421222.1990.11517897

To link to this article: http://dx.doi.org/10.1080/07421222.1990.11517897

![](/api/attachments/CTHU6GU6/fulltext/images/05705efb6eeb5cae87520b599f2707f9601ec3fea52ce88c201f2852917aa868.jpg)

Published online: 21 Dec 2015.

![](/api/attachments/CTHU6GU6/fulltext/images/e8945d7b632dd13b5d72118f70d812119d83eb48b1b724be3e58f215b1348e37.jpg)

Submit your article to this journal ↗

![](/api/attachments/CTHU6GU6/fulltext/images/7cd7b92e6a2ff96345884ee926709c4ca5057e361fe451d155f7cbbf4c0341d5.jpg)

View related articles ↗

![](/api/attachments/CTHU6GU6/fulltext/images/31fe58bd3e6316bb56d28f51deaaf2648aad3b6a535df4baed4f747e2ddebb99.jpg)

Citing articles: 7 View citing articles ↗

# Technology-Process Fit: Perspectives on Achieving Prototyping Effectiveness

JAY G. COOPRIDER and JOHN C. HENDERSON

JAY G. COOPRIDER is Assistant Professor of Information Systems at the University of Texas at Austin. He received his S.B. in computer science from the Massachusetts Institute of Technology, and his Ph.D. in management from the Sloan School of Management at MIT. His research interests include the impact of CASE technology on software design teams and the use of partnership as a strategy for managing organizational relationships.

JOHN C. HENDERSON is Professor of Management Information Systems at Boston University School of Management. He received his Ph.D., M.S., and B.S. degrees from the University of Texas at Austin. His early work focused on decision support systems and the more traditional management information systems. Presently his research is focused in three areas: the alignment of business and information technology strategies; the role of information technology in building and managing strategic partnerships; and the use of information technology to support software development teams. He has held faculty appointments at Florida State University and Ohio State University, as well as having served as staff director for the Joint Committee on Electronic Data Processing at the Florida legislature. Prior to coming to Boston University, he was on the faculty of the Sloan School of Management at MIT. His articles have appeared in many journals, including Management Science, Journal of Management Information Systems, MIS Quarterly, Information Systems Research, Sloan Management Review, Decision Sciences, and IEEE Transactions on Engineering Management.

ABSTRACT: Prototyping has received a great deal of attention as an important design methodology. Current support technologies for prototyping environments are typically intended to increase the efficiency of the individual system builder. We propose a broader perspective for assessing the impact of support technology on prototyping processes. In developing this perspective, we present frameworks for prototyping processes, support technologies, and development performance. Prototyping is characterized from the behavioral perspectives of individual, social, and organizational processes—each of which must be considered in assessing impacts. Support technology is characterized by production, coordination, and organizational dimensions, each affecting prototyping processes and performance in unique ways. To assess the impacts of the process–technology linkages, measures are suggested for evaluating prototyping processes and products from task, social, and business perspectives. It is

An earlier version of this paper was originally published in the Proceedings of the Twenty-Third Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1990).

proposed that the primary determinant of performance impact is the fit between the prototyping processes and the support technology used. By combining a functional model of support technology with behavioral perspectives of the prototyping process, a better understanding of the impacts of technology on prototyping effectiveness is obtained.

KEY WORDS AND PHRASES: prototyping, software development processes, computer-aided software engineering (CASE) technology, evaluation of information system performance.

## 1. Introduction

THE JOB OF THE INFORMATION SYSTEM (IS) BUILDER is becoming more difficult. IS developers must deal with more sophisticated end users, demands for increased productivity, and proposals for a wide range of new development methods, techniques, and technologies. Their environment is growing increasingly dynamic and turbulent as their organizations confront more intense competitive pressures (from both domestic and foreign sources), changing regulatory controls, shrinking product life cycles, shifting management and control strategies, and growing uncertainties about their rapidly evolving technology base. These factors are making it much harder for today's IS builder to meet the performance expectations of management and the user community.

Prototyping has received a great deal of attention as a design methodology capable of addressing many of these issues. No universal definition of prototyping exists and different terms are used for referring to it $[2, 30]$ . Naumann and Jenkins $[30]$ state that a “prototype system, intentionally incomplete, is to be modified, expanded, supplemented, or supplanted” (p. 30). In general, prototyping is viewed as being consistent with the systems development life cycle, but does not attempt to define requirements or the details of design exhaustively. Variations of prototyping include iterative design, evolutionary design, and adaptive design $[2]$ . In these types of design approaches, each step of the systems design life cycle is involved. However, the objective of prototyping and other similar approaches is to create an inexpensive, live test-bed with which to interact with customers and clients. In fact, prototyping is often differentiated from other methodologies because the resulting system is often discarded or thrown away $[3]$ .

It has been suggested that prototyping enables developers to build systems more quickly $[3, 28]$ ; increase user involvement, utility, and satisfaction $[2, 37]$ ; respond to changing environments and requirements $[36]$ ; decrease maintenance costs $[3, 37]$ ; lower technical risk levels $[3, 11]$ ; reduce the number of design defects $[22]$ ; and reduce the level of application uncertainty $[2, 36]$ . Many view prototyping as the methodology that represents the future of software development $[1, 11]$ .

Past researchers have proposed many factors as affecting the performance of prototyping projects. The skills of the IS builder [30], the strength of the project leader [34], the experience of the system builder [3], the characteristics of the application [3, 30], and top management support [7] have each been proposed as determinants of prototyping success. A major thread through much of the prototyping literature, however, is that the availability of appropriate tools and technologies can be a major enabler of success for a prototyping project $[3, 30, 36]$ .

The potential for technology to impact on the prototyping process is significant. However, as has been suggested throughout the systems design research literature $[6, 25, 27, 29]$ , the design process is a complex sociopolitical network of issues for which technology per se is not the answer. In fact, if poorly applied, the tools and technologies of prototyping could well have a negative effect. As Lipp states in his book on the prototyping approach to systems development:

Many DP organizations have approached problem resolution from a “tool-oriented” perspective, assuming that if enough sufficiently sophisticated tools are “thrown” at the problem it will be solved. . . . [This approach is] simply providing a better weapon with which to kill ourselves. [26, p. 147]

Technology can have a major impact on the performance of IS builders using prototyping, but the technology must complement the processes used by builders during the course of a project $[11]$ . There are many reasons why researchers have not found that supporting technology has a significant effect on development performance $[18]$ . A major reason for this lack of effect, however, is a mismatch between the capabilities of the technology used and the fundamental processes of the system builder. It is the premise of this paper that only when supporting technologies are properly matched with the fundamental processes of the system prototyper will major impacts on prototyping performance be possible. This proposed “match” between technology and process will be referred to as “fit.” In doing so, fit is regarded as a moderating relationship $[38]$ : technology “moderates” (or enhances) the relationship between process and performance.

Specifically, although prototyping processes and support technologies may both affect prototyping performance directly, the fit between process and technology will be the significant determinant of performance. This concept of fit is related to Drazin and Van de Ven's description of structural contingency theory's concept of technological fit [12]. They state that the task for researchers adopting a systems definition of fit is to identify the feasible set of processes and technology dimensions that are effective for different environments and to understand which patterns of process–technology linkages are internally consistent and effective. Figure 1 illustrates this relationship.

A closely related issue involves measuring the performance of prototyping projects. To assess the impact of support technology on the prototyping process, it is obviously necessary to be able to measure that impact. Yet traditional measures of IS development performance (such as number of lines of code produced for a given amount of effort) distort the overall performance picture and cause managers to overlook important productivity factors $[22]$ . To overcome this, we present a framework for measuring prototyping performance. This framework will match performance measures to the perspectives of the prototyping processes and support technologies that we establish.

The reasons why this paper focuses on prototyping processes to the exclusion of other design methodologies (although many of the concepts presented may be applicable to other methodologies) should be noted. First, as mentioned earlier, prototyping is an important design methodology, deserving particular attention. Second, and perhaps more significantly, in examining the fit between development processes and supporting technologies, it is important to understand the development processes in some depth. Goodman [15] presents a strong argument for the necessity of understanding the task as an integral part of any model of performance. Since the tasks (processes) of a development team using a particular methodology can be very different from those of a team using a different methodology, specific conclusions about the impact of technology on one methodology cannot necessarily be applied to another. Rather, it is important to investigate the impacts of support technology on a development process in some specificity. By focusing on prototyping, the performance impacts of the process–technology fit can be examined in greater detail than would be possible by discussing development methodologies in general.

![](/api/attachments/CTHU6GU6/fulltext/images/360e1897bb080fa2db86f8ade317e5d7ef128ed5eb013ba609bb6160dd8caadc.jpg)  
Figure 1. The Impact of Support Technology on Prototyping Performance

Section 2 of this paper examines the behaviors of IS builders during prototyping and establishes behavioral perspectives of the prototyping process that will be used as a basis for discussing the relationships between technology and performance. Section 3 characterizes support technologies for prototyping, identifying the dimensions of this technology that will benefit the system prototyper. Section 4 discusses the fit between prototyping processes and supporting technologies. Section 5 then builds a framework for evaluating the performance of prototyping projects. This section identifies key dimensions of IS performance, provides examples of useful measures, and discusses potential performance impacts of various dimensions of support technology on the different perspectives of the prototyping process. Finally, section 6 offers final conclusions and recommendations for further research.

## 2. Behavioral Perspectives of the Prototyping Process

MANY CHARACTERIZATIONS OF THE PROTOTYPING PROCESS appear in the literature. Naumann and Jenkins [30] characterize prototyping as a four-step procedure:

1. identify the user's basic information requirements;

2. develop a working prototype;

3. implement and use the prototype system;

4. revise and enhance the prototype system.

Many other authors have presented similar descriptions $[2, 34]$ . Typically, these characterizations of the prototyping process describe prototyping as a set of phases that are terminated by the existence of an artifact—milestones, in effect. As such, they share a fundamental problem with the traditional “waterfall” method of software development $[5]$ that they are trying to augment or replace. These “milestone” process descriptions do not provide insight into the actual design behaviors or the processes that actually determine the success of the prototyping effort $[11]$ . If a design process model only depicts idealized processes that do not accurately map to actual prototyping behavior, then the supporting technologies applied to these idealized processes will not match the way that prototypers really work. Applying technology in this way may actually impair prototyping performance rather than enhance it.

To determine the most effective ways to apply technology to the prototyping process, a deeper, behavioral model of prototyping must be used. In an attempt to build such a model for the development of large software products, Curtis et al. [11] conducted a field study of large software development projects. They found that behavioral processes in such projects can be analyzed from three perspectives: cognitive, social, and organizational. Similarly, research on information systems in general can be characterized in terms of its unit of analysis [10]. Adapting Curtis et al.'s perspectives to reflect the applicable levels of analysis more closely, the behavioral processes of prototyping can be characterized from three perspectives: individual, social, and organizational. Table 1 illustrates the use of these basic perspectives to characterize the IS prototyping process.

## 2.1. An Individual Perspective of the Prototyping Process

The talents, skills, and experience levels of the individual participants of a prototyping project have been described as important influences on the prototyping process. For example, Blum [3] states that the form the prototyping process takes can be greatly influenced by the experience level of the system builder, while Naumann and Jenkins [30] state that the set of critical skills and abilities required for the system builder using prototyping are significantly different from those required for traditional system developers.

During prototyping, the system builder constructs successive versions of a prototype system, resolving conflicts with the user (requirements) within technology and economic constraints for each successive version $[30]$ . The builder is, in effect, performing detailed design and program generation as he or she creates and modifies each version of the system prototype. From an individual perspective, the prototyping process focuses on producing new prototype versions as quickly as possible. This perspective is common in the prototyping literature. However, the builder must work closely with the user at each step of the process—responding to changing perceptions of need. This builder-user interaction has been discussed by several researchers in the field, and it serves as the foundation for the process perspective discussed in the next section: the social perspective.

<table><tr><td colspan="2">Table 1 Behavioral Perspectives of Prototyping Processes</td></tr><tr><td>Perspective</td><td>Concerns</td></tr><tr><td>Individual</td><td>Individual system builderTalents and skillsExperience</td></tr><tr><td>Social</td><td>Intra-team communicationsUser-builder involvementDesign convergenceProject managementExtra-team communicationsBoundary managementInnovation</td></tr><tr><td>Organizational</td><td>Organizational environmentCoordination of multiple teamsReaction to external environment</td></tr></table>

## 2.2. A Social Perspective of the Prototyping Process

There has been a fairly large amount of research on the impacts of group process on IS development [13]. For example, Mumford [29] and Bostrom and Heinen [6] have discussed strategies for managing the development of information systems that are grounded in participatory decision-making/problem-solving theory. This research has provided many insights into the performance impacts of group behavior on software development. Generally, however, it has been poorly grounded in theory and has not provided models for understanding the performance effects of possible changes in group process behavior [21].

Collaboration between the system builder and user is at the heart of prototyping $[39]$ . Prototyping stresses the interactions among the user, the builder, and the system $[30]$ . Additionally, the manager role is a significant one in prototyping $[2, 34]$ (as it is with software development in general), although it has been generally neglected in the prototyping literature $[24]$ . The relationships among builder, user, and manager highlight the fact that, at its core, prototyping is a group process. Almost by definition, a system builder cannot prototype alone—the essence of prototyping is in the dialogue between builder and user $[39]$ , within the resource constraints established by management $[30]$ .

It is very important for all three roles to participate fully in the prototyping process. The importance of the manager's role was mentioned above. Henderson's empirical results [17] stress the importance of both the user's and builder's roles in the design process. In studying the level of designer and user involvement in 18 design teams from 12 different organizations, he found that neither user-dominated teams nor builder-dominated teams are as high performing as teams with more balanced levels of influence. Both the user and builder have expertise that is necessary to the prototyping process. Such research suggests that the manager-user-builder relationships are critical to prototyping processes.

In addition to communication within the team (manager-user-builder), communication with non-team stakeholders is an important process for the successful prototyping team. Gladstein [14] found such boundary management to be a major determinant of group performance. Henderson [16] relates this to IS design teams, arguing that boundary management is required for the team to establish design validity, and Zmud [40] found that the innovativeness of a software development group is facilitated if appropriate channels are provided to link the group with relevant external information sources. Both inter- and extra-team communications are important group processes for the successful prototyping team.

An idealized model of the group prototyping process would begin with each member of the team holding his or her own mental model of the proposed system. The differences and conflicts in the various individuals' mental models would be resolved and compromised until a final prototype product is reached $[11]$ . In this idealized model, any conflicts would be resolved objectively, and the "best" design alternative would eventually be reached.

This ideal model, however, rarely matches the reality of actual prototyping projects. There is a danger in prototyping that the system builder and user will come to agreement on a design solution before they have fully evaluated all of the system design requirements. Because of this, they can converge on a solution that is less than optimal. Henderson and Ingraham [19] found that “a comparison with the information requirements generated by a structured group process indicated that prototyping is a convergent design method that may overlook important user information needs.” Thus, techniques to balance the rapid convergence of prototyping approaches may have significant performance impacts.

A final group issue involved in the social perspective of prototyping is overall project management. Scharer [34] states that the challenge of managing a prototyping project can be greater than that of managing a project undertaken with a conventional methodology. In fact, most of the gains in productivity and quality that prototyping offers are realized only if the process is skillfully managed. Alavi [2] found that, while the use of prototyping provides clearer and better communication between system developers and users during the design phase of a project, the management and control of the project is more difficult, since the explicit planning and control guidelines inherent in traditional life-cycle approaches are missing.

The successful prototyping project, from a social perspective, effectively utilizes communication among members of the team as well as with nonteam stakeholders. Additionally, it requires the examination of alternate designs and concepts to slow the rapid convergence of ideas. Finally, it requires strict project management control.

Together, these factors can greatly enhance the group processes inherent in prototyping. It must be remembered, however, that these processes take place within an organizational environment. This organizational perspective provides the focus for the next section.

## 2.3. An Organizational Perspective of the Prototyping Process

The prototyping of an information system is performed within an organizational context (as is any software development method). The significance of the organizational environment has long been recognized as an important factor for successful development of information systems. Markus [27] and Kling and Iacono [25], for example, emphasize the importance of organizational–political factors in managing information systems. Curtis et al. [11] cite “requirements volatility” as the fundamental organizational issue for software development, stating that system requirements typically change because of environmental changes. Certainly, reacting to environmental changes is an important concern for the system prototyper. Quick response to organizational changes has, in fact, been cited as a primary advantage of prototyping [36]. There are, however, additional organizational issues that must be addressed.

Bourke [7] describes a prototyping project that was technically successful but was canceled because of inadequate sponsorship by the organization, which he refers to as a lack of “prototyping infrastructure.” Bourke feels that a prototyping project is doomed to fail without this infrastructure. Nosek [31] suggests that decision makers can build an organizational prototyping infrastructure by choosing organizational structures, reward systems, information processes, and personnel skills to ensure the successful completion of prototyping projects. He provides two case examples of organizational approaches to prototyping. One firm took an ad hoc approach to prototype development with minimal changes to organization design, while the second demonstrated a full commitment to providing a fertile environment for building prototypes by making substantial changes in organization design. For example, the second organization created a resource center to provide developers with information about the use of prototyping tools.

The organization environment, then, greatly affects the prototyping process. Generally, the organizational perspective of the prototyping process has two main parts. The first process involves the coordination of multiple teams. The organization must have the ability to create and manage a variety of design teams (perhaps some using prototyping and some not) without a significant reduction in the performance of any single team. The key issues relating to this coordination are the overall control of the various teams and the management of the distributed knowledge inherent in them. Project control and knowledge management can each be maintained on either a centralized or distributed basis, and the choice will greatly impact on the technology used to support the project and the project performance.

The second process from an organizational perspective involves learning about and reacting to the external environment (competitors, regulations, etc.). This process is necessary for identifying important applications and keeping applications flexible. The ability to create prototyping products or components that can be leveraged to meet competitive demands quickly can be extremely important for an organization struggling to maintain or improve its competitive position in a turbulent environment.

The organizational perspective of the prototyping process provides a business-level view of the project. It requires intra-company coordination of teams and extra-company gathering of information. This perspective can be enhanced by adjusting organization design variables and by providing functionality to carry out the intra- and extra-company communication needed.

Having examined the process of prototyping from individual, social, and organizational perspectives, we will now characterize the support technology that can be used to aid the system prototyper. This characterization will then be used to describe the possible technology-process linkages necessary for performance impact.

## 3. Dimensions of Support Technology

AS DISCUSSED IN SECTION 1, THE AVAILABILITY OF SUPPORT TECHNOLOGY is widely held to be a primary determinant of high performance for prototyping. The supporting technologies probably mentioned most frequently in the literature are very high-level languages (also referred to as fourth-generation languages, end-user languages, etc.) [30]. However, such technology by itself is not enough to establish a successful prototyping environment. As Taylor and Standish [36] state: “we must have a multi-faceted technical approach to rapid prototyping if we are to address a broad range of prototyping applications successfully.” We maintain that the technology must not only be multifaceted, but must also fit the actual prototyping processes in use.

Henderson and Cooprider [18] present an empirically-derived functional model of IS planning and design technology. They list 98 specific functions identified by experts in the technology. These 98 functions were categorized into three general dimensions and seven specific technology components, and the dimensions were shown to be useful for characterizing the capabilities of commercially available planning and design technologies. They are also useful for characterizing the types of support technologies that are most important in a prototyping environment.

Henderson and Cooprider describe three general dimensions of IS planning and design technology: production, coordination, and organization. Production technology has a direct impact on the capacity of an individual to generate planning and design decisions and subsequent artifacts or products. Coordination technology enables or supports the interactions of multiple agents in the execution of a planning or design task. Organizational technologies are the functions and associated procedures that determine the environment in which production and coordination technology will be applied to the planning and design process. Table 2 describes these three dimensions of technology.

## 3.1. The Production Dimension of Technology

Within each general technology dimension, more specific components are used to characterize the technology. Production technology consists of three components: representation, analysis, and transformation. Representation technology enables the user to define, describe, or change a definition or description of an object, relationship, or process. Such capabilities are at the heart of traditional characterizations of prototyping technology. By its nature, prototyping is a representation or modeling process [33]. Naumann and Jenkins [30] explicitly list “modeling” as a required technology for prototyping. Any technology supporting prototyping must provide an array of representation functionality.

<table><tr><td colspan="2">Table 2 Dimensions of Support Technology</td></tr><tr><td>Dimension</td><td>Components</td></tr><tr><td>Production</td><td>RepresentationAnalysisTransformation</td></tr><tr><td>Coordination</td><td>ControlCooperative Functionality</td></tr><tr><td>Organizational</td><td>Learning / SupportInfrastructure</td></tr></table>

Analysis technology enables the user to explore, simulate, or evaluate alternate representations or models of objects, relationships, or processes. It is very similar to Riddle's “technology of evaluation” [33]. As was discussed in section 2.2, many authors have criticized prototyping for being a convergent design process. Analysis technology provides the functionality for encouraging the examination of design alternatives and implications.

Transformation technology executes a significant prototyping task, thereby replacing or substituting for a human system builder. This dimension reflects a straight capital/labor substitution—technology for human labor. This functionality has received a great deal of attention in the prototyping literature. Prototyping implies a need to do things quickly (e.g., “rapid” prototyping), and transformation technology can play a major role in producing a prototype quickly.

The transformation functionalities currently available in support technologies in the marketplace are generally focused relatively late in the software development life cycle $[18]$ . Code generation, for example, is a typical transformation technology, and it is frequently used only after much of the design work is completed. In contrast, prototyping often provides much of its value early in the design life cycle, during problem formulation and definition $[4]$ . The determination of the precise types of transformation technology that provide the most impact on the prototyping process is an important subject for future research.

## 3.2. The Coordination Dimension of Technology

Coordination stems from the activities and resources that are expended in tasks requiring multiple actors or agents. The general dimension of coordination technology consists of two more specific components: control and cooperative functionality. Control technology enables the user to plan for and enforce rules, policies, or priorities that will govern or restrict the activities of team members during the prototyping process. There are two types of control covered in this component: access control and resource management. Access control assumes that issues of security and access must be carefully managed. Resource management enables a manager to plan for, allocate, and monitor the use of design team resources.

Two control issues that are especially important for prototyping deserve special mention. As discussed in section 2.2, project management can be extremely difficult in a prototyping environment. The familiar checkpoints inherent in the traditional development life cycle are generally lacking in prototyping [1], and it can be difficult for managers to monitor and control team members in a prototyping environment. Project control functionality is thus critical—probably even more critical than in a traditionally managed development project. In addition to project control, software configuration management functions such as version control can be very important. Since prototyping is an iterative process (with a new prototype system being generated at each iteration), these tools can become very important for tracking and managing the process.

Cooperative functionality enables the user to exchange information with other individuals for the purpose of influencing (affecting) the concept, process, or product of the prototyping team. This dimension of support technology has been largely ignored in the prototyping literature. However, if one accepts the social perspective of prototyping, the importance of cooperative functionality becomes evident. The ability to exchange information among members of the team and between the team and outsiders can be a significant determinant of performance. The ability of coordination technology to function both as a communication channel and as a facilitation aid can be very important for the prototyping system builder. Examples of such technology can be found in research on group DSS and computer-supported cooperative work.

## 3.3. The Organizational Dimension of Technology

Finally, the organizational dimension consists of two specific components: learning/support and infrastructure. Learning/support technology helps an individual user understand and effectively use the available technology. Such functionality can help the individual system builder become productive more quickly in a new environment by making it easier for him or her to learn the tools at his or her disposal. Additionally, it can improve the builder-user relationship by allowing users to use available technologies to explore their own alternatives—thus making the user a more influential part of the design team. It also aids the organization by training all members across all teams to a minimum skill level—assisting communication and cooperation among the teams.

Infrastructure technology is defined as functionality standards that enable portability of skills, knowledge, procedures, or methods across planning or design processes. Infrastructure technology gives teams the ability to share models, code, documentation, etc. By allowing teams to communicate and coordinate through the use of standards, the performance of the entire IS organization (in addition to that of the individual teams) can be markedly improved. At present, the role of IS standards as performance enhancers is not well understood. Jeffery [21], for example, states that programming and documentation standards have been suggested as affecting IS development performance, but their specific productivity impacts have not been investigated.

## 4. Process–Technology Linkages

MOST OF THE SUPPORT TECHNOLOGY THAT HAS BEEN SUGGESTED in the literature for prototyping environments is production technology. Such technology enables the individual system builder to build and analyze prototype systems as rapidly as possible. However, this technology will only marginally increase the performance of IS development teams and organizations as long as it is used just to “do the same things faster.” If production technology enables system builders to “do different things,” then performance can increase by a much greater amount. Order of magnitude improvement can only be achieved when the technology changes the process of software development $[21]$ . For example, code generation is a typical transformation technology $[18]$ , and it is frequently suggested as a prototyping aid $[33]$ . However, “coding” typically accounts for only 15 percent of the software costs of large systems $[22]$ . Using code generation to double coding efficiency, therefore, will provide only a 7.5 percent productivity increase. But if code generation is used to generate successive prototype systems more quickly, and this leads to better design evaluation, design defects can be significantly reduced, and more accurate systems requirements can be established early in the development life cycle, greatly reducing total project costs $[22]$ .

Gains in overall performance can be further leveraged by using technologies that support the group and organizational perspectives of the prototyping process. Support technologies improve performance not only by providing the “individual-based” representation–analysis–transformation functionality of production technology, but also by aiding intra-team coordination and boundary management through the use of control and cooperative support functionalities. Additionally, organizational technology aids the establishment of an organizational infrastructure for inter-team coordination by providing learning/support functions and technology standards for the entire organization.

It is expected that direct performance impacts will result from applying production technology to the prototyping processes in the individual perspective, coordination technology to social perspective processes, and organizational technology to organizational perspective processes. If, however, the use of production technology by individuals allows them to function more effectively as a team, there may be a much larger performance impact. Similarly, coordination technology can directly impact the group processes of prototyping, but it will have a larger effect on performance if it is used by the organization to leverage its management of the entire development process. For example, such technology may allow the parallel operations of multiple teams through a technology infrastructure. Thus, direct performance impacts occur across corresponding levels (production–individual, coordination–social, organizational–organization), but the linkages across levels will frequently offer much greater impacts on prototyping performance.

To evaluate the range of possible performance impacts of applying supporting technologies to prototyping processes, a broad view of assessing the performance of prototyping projects is required. The next section proposes such a view, and discusses its applicability in assessing the impact of the prototyping process–technology fit.

## 5. Measuring the Performance of Prototyping Projects

PERFORMANCE MEASUREMENT IS A CENTRAL ISSUE for evaluating the impact of support technology on the prototyping process. Research attempting to evaluate IS performance has suggested a range of possible measures. Hirschheim and Smithson [20], however, state that IS evaluations have been misdirected toward tools and techniques for measurement and away from understanding. For example, many researchers have based their productivity measurements on the number of lines of source code produced for a given amount of effort. This approach has long been criticized because of many obvious problems. For example, each line of source code does not have the same value and does not require the same amount of time or effort to produce. Still, most software productivity researchers use lines of code as a primary focus [5]. While performance measures such as “source lines of code per month” are relatively easy to gather and use, their narrow focus may distort the overall productivity picture and cause managers to overlook promising avenues for performance improvements. The ultimate goal, of course, is to provide applications that benefit the organization and not to create lines of code. Measures such as lines of code do not address the issues of most concern to management—particularly senior management. A more comprehensive view of IS performance is required. Table 3 illustrates such a view of performance in assessing the impact of technology on the prototyping process.

As seen in Table 3, one major issue in measuring IS performance is reflecting both a product and a process dimension. Many researchers have suggested the usefulness of separate measures for the products and processes of IS development. For example, Agresti [1] uses an industrial engineering perspective to propose process and product measures of software development. Riddle [33] has discussed the value of this approach in a prototyping environment. Since a primary goal of performance measurement is to improve the production processes involved, not only must the final product of the prototyping effort be evaluated, but the processes used to obtain that product must also be considered. It is important to use both types of measures, because there is a potential conflict between the efficiency of the process and the quality of the product.

This process/product dimension reflects the more general tradition of measurement in organizational control theory. Ouchi [32], for example, categorizes control measures as either behavior (process) based or outcome (product) based. This measurement dimension can be viewed as an application of these ideas to the area of prototyping.

Table 3 Sample Measures of Prototyping Performance

<table><tr><td></td><td>Process</td><td>Product</td></tr><tr><td>Task</td><td>Efficiency(SLOC/WM)</td><td>Quality(Defects/Unit)</td></tr><tr><td>Social</td><td>Synergy(Commitment)(Dependability)</td><td>Validity(Stakeholder assessment of meeting needs)</td></tr><tr><td>Business</td><td>Flexibility(Time to break even)</td><td>Leverage(Market share)</td></tr></table>

There can be difficulties in applying this process/product perspective to prototyping, however. The product of the prototyping process is sometimes not available at the end of the development process. Many prototypers feel that once a prototype has served its purpose of defining user requirements, it can (and should) be “disposed of.” The debate of “expendable” vs. “evolutionary” prototyping has received much attention $[3]$ . For our purposes, this issue is somewhat moot. The critical issue is to include the effort to produce a product as only one of several measures.

The levels of analysis shown in Table 3 illustrate that different behavioral perspectives lead to different measurements. This reflects the view that the measurement of prototyping performance should be oriented toward management decision and action. Boehm [5] demonstrates that the perceptions of senior management, middle management, and programmers are very different concerning the factors that have the most leverage for affecting development productivity. These perceptions can be important motivational factors for affecting the prototyping process, and they should be reflected in any performance measurement system. For our performance measurement system, we use task, social, and business perspectives to reflect the conceptual levels of measurement. These three levels generally complement the process perspectives that were developed in section 2, and they correspond well to the technology linkages with those processes. The following three sections describe each of these perspectives of performance measurement.

## 5.1. Task Measures of Performance

The task perspective of performance measurement reflects a production view of prototyping. The task measures of Table 3 are indicators of the accomplishment of the builder's defined tasks—they are “individual oriented” and, from a management perspective, are concerned with “doing things right.” Task process measures are primarily used to evaluate the efficiency of production. Source lines of code or function points per work-month are typical measures of this perspective. Task product measures evaluate the output of the prototyping production process. These measures reflect the quality of the program product. Quality may be measured in terms of defects per unit output (e.g., errors per thousand lines of code). Alternatively, quality measures may reflect the product's general technical performance. Examples of this form of task product measure include run-time speed and object code size.

These task measures dominate the IS performance literature [20]. There are several problems, however, with focusing exclusively on these measures. Some specific complaints about these types of measures were described earlier. In general terms, they are measures of output (in an economic sense) rather than outcome (the total impact of the process). They are much more closely aligned with efficiency (how well input is converted to output) than with effectiveness (how the input is used to accomplish the goals of the organization). The addition of social and business perspectives provides a broader performance evaluation.

## 5.2. Social Measures of Performance

Hirschheim and Smithson [20] argue that both technical (task-oriented) and nontechnical (social) criteria must be included for IS evaluation to be meaningful. Social measures of performance generally evaluate how well the prototyping team performs as a whole—they are “group oriented” and, from a management perspective, are concerned with “doing the right things.” Social process measures indicate how well the development team functions together. We refer to these types of measures as “synergy” measures—evaluating the process gains or losses resulting from working as a group rather than as individuals [35]. Internal to the team, this is an issue of team maintenance [14]. Maintenance measures involve commitment, quality of work life, and satisfaction with the team. External to the team, the issue is the perceived dependability of the team—“trust.” Zucker [41] describes this as “process-based trust,” and states that such trust is largely a function of the group’s track record—its history of success or failure on past projects. Frequently used measures include the team’s ability to meet delivery schedules and financial commitments.

The social product measures evaluate design validity—is the team meeting project requirements and do those requirements satisfy a real business need? Support technology must provide the ability to test design validity. Ultimately, design validity can only be assessed by an agent external to the development team and the builder-user relationship [8], and the best source of these tests comes from communication with nonteam stakeholders [16]. The performance measures for this dimension include the user satisfaction assessments of these stakeholders and the rate of function change during maintenance over time (increasingly smaller amounts of change in the system—given the same system usage—imply a more accurate design solution). Similarly, system usage and the link between that usage and the behavior of the organization are sources of validity measurements. In essence, a valid design is one that affects an intended change in organizational behavior.

The problem of performance measurement occurs within an organizational context, and, hence, should include explicit evaluation from an organizational perspective. This is an example of a “systemic” level of measurement: placing a manager’s problem situation in a larger context. The next section looks at the manager's problem of performance measurement from a larger organizational perspective.

![](/api/attachments/CTHU6GU6/fulltext/images/1daec3d446be4290fba5a8abc876f6f04a1e618e78cf79bc4b47e914303e9776.jpg)  
Figure 2. The Impact of Support Technology on Prototyping Performance

## 5.3. Business Measures of Performance

Business measures of performance involve business success. At their core, these measures are concerned with how well the firm is using technology to innovate—they are “organization oriented” and are concerned with “doing things differently.” Business process measures are primarily concerned with organizational flexibility. The motivation for this view is the need to manage organizational resources in the face of significant environmental changes. They focus on the organizational resource of time. The main concern in this perspective is the speed with which the organization reacts to changes in the environment. A fundamental measure in this perspective is “time-to-break-even”: the length of time it takes an organization to convert an IS concept into a viable product that has earned back its development costs for the organization. This measure highlights the criticality of rapid response to environmental changes while directly incorporating aspects of quality and maintainability. It is rapidly becoming a key measure of IS performance.

The business product issue is fundamentally one of business leverage: can prototyping be used to leverage a position of competitive advantage for the organization? It reflects the importance of continually trying to do new things in a changing environment. Time will leave behind those organizations whose IS leaders are not willing to innovate—transforming the business. Measures in this perspective are drawn from competitive analysis and environmental scanning: market share over time, for example, or rate of new IS product introductions compared to the rates of competitors.

## 5.4. Performance Impacts

Figure 2 shows the completed framework for assessing the impacts of technology on IS prototyping. As suggested in the previous sections, the major linkage of production technology is with the individual processes of prototyping, and its direct performance impact will primarily be on the task level of performance. For example, transformation technology such as code generation is expected to increase programmer efficiency, and analysis technology such as consistency tests among alternate representations will improve the quality of the program product. Coordination technology's direct linkage will be with social process, and it will directly impact the social level of performance. For example, control technology can be used to implement flexible project management strategies, giving team members more autonomy and increasing their job satisfaction. Additionally, cooperative functionality such as dialogue management can be used to involve nonteam stakeholders in the prototyping process, thus increasing design validity [16]. Organizational technology will have its most direct linkages with the organizational processes of prototyping, and will directly impact the business measures of performance. For example, the use of standards provides common communication protocols and knowledge representations, allowing the time-sharing of knowledgeable members among teams. This gives more teams better access to project knowledge, leading to a more effective use of the organization's knowledge resources and more flexible prototyping processes. Additionally, learning/support technology such as libraries of reusable code modules can help prototypers leverage their efforts to produce new products more quickly—enabling their organizations to attain competitive advantage.

As was discussed in section 4, however, some of the largest effects on productivity—the order-of-magnitude changes—come from the potential to change the existing prototyping processes. For example, the potential for technology to empower a given (e.g., user) role can radically change the group dynamics of a design process. Representation and analysis technology can reduce the design knowledge required for users to participate effectively, and, as a result, the user role becomes much more active in the prototyping process.

Closely related to this research theme is the need for systematic analysis of the link between prototyping and performance. The performance framework proposed here provides a basis for investigating this issue. The issue is one of utilizing the measures of performance in a systematic and meaningful way. One approach for undertaking this analysis is to use a statistical technique to combine the measures into a single measure of general performance, or into single measures for each level of analysis. One such technique that has been used in the IS literature is data envelopment analysis (DEA), which calculates a single number rating the efficiency of each reporting unit in converting multiple input factors to multiple outputs [23]. Whatever method is used, the purpose of the analysis should be to provide diagnostic information to management concerning ways to improve the development process along each relevant dimension. This framework can serve as a useful guide for this process [9], but different specific measures might well be appropriate for different development and business environments.

## 6. Conclusions and Recommendations for Future Research

THIS PAPER HAS EXAMINED THE PERFORMANCE IMPACTS of support technology on the prototyping process. In doing this, the process was examined from three behavioral perspectives: individual, social, and organizational. Support technology was then characterized by the functional dimensions of production, coordination, and organizational technology. A performance measurement framework was then developed using the dimensions of process/product and levels of analysis (task, social, and business). This framework was then used to base discussions of examples of performance impacts.

Much research remains to be done in this area. Development of performance measures at each level through the use of applicable reference disciplines is an obvious first step. Just as industrial engineering may be used as a reference field for measuring IS productivity (e.g., process/product), one could envision using research in manufacturing, group processes, economics, organizational studies, etc., to derive new measurements for prototyping performance.

Perhaps the major research issue emerging from this paper is the criticality of the technology-process "fit" to prototyping performance. If a technology platform or environment is provided for a prototyping team, will that platform account for major performance impacts by itself, or must the technology also match the specific design methods used? In other words, should design processes be altered to match the technology in use (through training, etc.) or should technology be modified to match design processes? Would the cost of either alternative be justified by the performance impacts they would provide? In the final analysis, the question of the magnitude of the impact of the technology-process “fit” as compared to the impacts of either the direct process or technology effects alone is an empirical issue, and it must be tested as such in the future. Both Venkatraman [38] and Drazin and Van de Ven [12] give suggestions for methodologies to operationalize and test the concept of fit in this environment.

As was mentioned in section 1, it should be noted that many concepts presented in this paper might be applied to other development methodologies. Although the process–technology linkages and the performance impacts discussed were directly framed for prototyping so that they could be examined in some depth, the implications of the process–technology “fit” and the performance measurement framework should be generally applicable to a wide range of design methodologies. Applications to other methods should be made in the future.

We have presented perspectives on the measurement of prototyping project performance, and a way to assess technologies that are available for the prototyping environment. This paper highlights the importance of examining the performance impacts of support technology broadly, and suggests that such an examination can be performed in a systematic manner. Of course, the ability to measure process–technology linkages and to attribute performance impacts to support technology becomes increasingly difficult as one moves from the individual unit of analysis to the organization. However, the ability to characterize prototyping behaviors and support technologies along the presented dimensions suggests that these frameworks can lead to an increased level of understanding of performance determinants at all levels.

## REFERENCES

1. Agresti, W. (ed.) New Paradigms for Software Development. Washington, DC: IEEE Computer Society Press, 1986.

2. Alavi, M. An assessment of the prototyping approach to information systems development. Communications of the ACM, 27, 6 (June 1984), 556–563.

3. Blum, B. Application systems prototyping. In M. Lipp, ed., Prototyping: State of the Art Report. England: Pergamon Infotech Limited, 1986, 3–14.

4. Boehm, B. Verifying and validating software requirements and design specifications. IEEE Software, 1, 1 (January 1984), 75–88.

5. Boehm, B. Improving software productivity. IEEE Computer, 20, 9 (September 1987), 43–57.

6. Bostrom, R., and Heinen, J. MIS problems and failures: a socio-technical perspective. MIS Quarterly, 1, 1 and 4 (1977).

7. Bourke, M. Actual experiences in prototyping. In Prototyping: State of the Art Report, M. Lipp, ed. England: Pergamon Infotech Limited, 1986, 15–26.

8. Churchman, C. The Design of Inquiring Systems. New York: Basic Books, 1971.

9. Cooprider, J., and Henderson, J. A multi-dimensional approach to performance evalua-

tion for IS development. Center for Information Systems Research Working Paper No. 197, Sloan School of Management, M.I.T., Cambridge, MA, 1989.

10. Curley, K., and Henderson, J. Evaluating investments in information technology: a review of key models. Proceedings of the 1989 ACM SIGOIS Workshop on the Impact and Value of Information Systems. Minneapolis, MN (June 1989).

11. Curtis, B.; Krasner, H.; and Iscoe, N. A field study of the software design process for large systems. Communications of the ACM, 31, 11 (November 1988), 1268–1286.

12. Drazin, R., and Van de Ven, A. Alternative forms of fit in contingency theory. Administrative Science Quarterly, 30, 4 (December 1985), 514–539.

13. Elam, J. (panel chair). Studying design teams—contrasting approaches. Proceedings of the Eighth International Conference on Information Systems. Pittsburgh, PA (December 1987), 463–464.

14. Gladstein, D. Groups in context: a model of task group effectiveness. Administrative Science Quarterly, 29, 4 (December 1984), 499–517.

15. Goodman, P. Impact of task and technology on group performance. In Designing Effective Work Groups, P. Goodman, ed. San Francisco: Jossey Bass, 1986.

16. Henderson, J. Managing the IS design environment. Center for Information Systems Research Working Paper No. 158, Sloan School of Management, M.I.T., Cambridge, MA, 1987.

17. Henderson, J. Involvement as a predictor of performance in IS planning and design. Center for Information Systems Research Working Paper No. 175, Sloan School of Management, M.I.T., Cambridge, MA, July 1988.

18. Henderson, J., and Cooprider, J. Dimensions of IS planning and design aids: a functional model of CASE technology. Information Systems Research, 1, 3 (September 1990), 227–254.

19. Henderson, J., and Ingraham, R. Prototyping for DSS: a critical appraisal. In Decision Support Systems, M. Ginzberg, W. Reitmann, and E. Stohr, eds. Amsterdam: North Holland, 1982, 79–96.

20. Hirschheim, R., and Smithson, S. Information systems evaluation: myth and reality. In Information Analysis: Selected Readings, R. Galliers, ed. Sydney: Addison-Wesley, 1987, 367–380.

21. Jeffery, D. Software engineering productivity models for management information system development. In Critical Issues in Information Systems Research, R. Boland and R.

Hirschheim, eds. Chichester: John Wiley & Sons, 1987, 113–134.

22. Jones, T. Programming Productivity. New York: McGraw-Hill, 1986.

23. Kauffman, R., and Kriebel, C. Measuring and modeling the business value of IT. In Measuring Business Value of Information Technologies, ICIT Research Team #2. Washington DC: ICIT Press, 1988.

24. Kensing, F. Property determination by prototyping. In Approaches to Prototyping, R. Budde, K. Kuhlenkamp, L. Mathiassen, and H. Zullighoven, eds. Berlin: Springer-Verlag, 1984, 322–340.

25. Kling, R., and Iacono, S. The control of information systems development after implementation. Communications of the ACM, 27, 12 (December 1984), 1218–1226.

26. Lipp, M. (ed.) Prototyping: State of the Art Report. England: Pergamon Infotech Limited, 1986.

27. Markus, M. L. Power, politics, and MIS implementation. Communications of the AM, 26, 6 (June 1983), 430–444.

28. Mason, R. E. A., and Carey, T. Prototyping interactive information systems. Communications of the ACM, 26, 5 (May 1983), 347–354.

29. Mumford, E. Participative systems design: structure and method. Systems, Objectives, Solutions, 1, 1 (1981), 5–19.

30. Naumann, J., and Jenkins, A. Prototyping: the new paradigm for systems development. MIS Quarterly, 6, 3 (September 1982), 29–44.

31. Nosek, J. Organization design choices to facilitate evolutionary development of prototype information systems. In Approaches to Prototyping, R. Budde, K. Kuhlenkamp, L. Mathiassen, and H. Zullighoven, eds. Berlin: Springer-Verlag, 1984, 341–355.

35. Steiner, I. Group Process and Productivity. New York: Academic Press, 1972.

32. Ouchi, W. A conceptual framework for the design of organizational control mechanisms. Management Science, 25, 9 (September 1979), 833–848.

33. Riddle, W. Advancing the state of the art in software system prototyping. In

Approaches to Prototyping, R. Budde, K. Kuhlenkamp, L. Mathiassen, and H. Zullighoven, eds. Berlin: Springer-Verlag, 1984, 19–28.

34. Scharer, L. The prototyping alternative. In New Paradigms for Software Development, W. Agresti, ed. Washington, DC: IEEE Computer Society Press, 1986, 59–68.

36. Taylor, T., and Standish, T. Initial thoughts on rapid prototyping techniques. In New Paradigms for Software Development, W. Agresti, ed. Washington, DC: IEEE Computer Society Press, 1986, 38–47.

37. Tavolato, P., and Vincena, K. A prototyping methodology and its tool. In Approaches to Prototyping, R. Budde, K. Kuhlenkamp, L. Mathiassen, and H. Zullighoven, eds. Berlin: Springer-Verlag, 1984, 434–446.

38. Venkatraman, N. The concept of fit in strategy research: toward verbal and statistical correspondence. The Academy of Management Review, 14, 3 (July 1989), 423–444.

39. West, M. A taxonomy of prototyping—tools and methods for database, decision support and transaction systems. In Prototyping: State of the Art Report, M. Lipp, ed. England: Pergamon Infotech Limited, 1986, 105–122.

40. Zmud, R. The effectiveness of external information channels in facilitating innovation within software development groups. MIS Quarterly, 7, 2 (1983), 43–58.

41. Zucker, L. Production of trust: institutional sources of economic structure, 1840–1920. In Research in Organizational Behavior, 8 (JAI Press, 1986), 53–111.
