---
otero_id: 27334
otero_key: "PJKA67BC"
title: "Management of Large Software Development Efforts"
authors: "Robert W. Zmud"
year: "1980"
journal: "MIS Quarterly"
doi: "10.2307/249336"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Management of Large Software Development Efforts
Author(s): Robert W. Zmud
Source: MIS Quarterly, Vol. 4, No. 2 (Jun., 1980), pp. 45-55
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249336
Accessed: 26-08-2015 08:19 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# MANAGEMENT OF LARGE SOFTWARE DEVELOPMENT EFFORTS

By: Robert W. Zmud

## Abstract

The high development and maintenance costs, and the late delivery experienced by many organizations when developing large software systems is well documented. Modern software practices have evolved to overcome many of the technical difficulties associated with software development. To a large extent, however, the high costs and schedule slippages can be traced to management, not technical, deficiencies. This article develops an approach for managing the software development effort that exploits the benefits of modern software practices in staffing, planning, and controlling software development.

Keywords: Software development, software engineering, life cycle, project management
ACM Categories: 2.40, 2.41, 4.0

## Introduction

Apparently it is the exception rather than the rule for an organization to develop, within budget and according to schedule, a large software system that meets the sponsor's requirements $[5, 11]$ . Because of this phenomena, a number of programming and design methodologies have evolved over the last decade that resolve many of the technical problems experienced in software development $[1, 12, 15, 23, 26, 30]$ . A comparable evolution in management methodologies, however, has not occurred.

Practitioners have experimented and achieved a certain amount of success with various means of staffing, planning, and controlling the software development effort. The objective of this article is to synthesize these practical ideas to arrive at a managerial exploitation of modern software practices.

The focus of the article is on the development of large, application software rather than computer support software, such as compilers or operating systems. The development of large application software is particularly beset with managerial rather than technical problems $[25]$ . While no precise definition exists for “largeness,” a large software system is understood to be one that requires more than one management level to coordinate the development effort, and more than a six month development period $[3, 20, 25]$ .

## The Nature of Software

Software consists of abstract sets of rules that govern the creation, transfer, and transformation of data. Initially existing solely as an idea, it is iteratively refined, becoming visible at its completion. This invisibility is compounded for large software, for which logical complexity cannot be maintained in one person's mind, and for which development must be partitioned into a number of tasks assigned to different people. As task descriptions are only models of the intended abstraction, and as the individual performing a task interprets these descriptions through a unique world view, most software errors occur at the interfaces of modules written by different programmers [38].

This misinterpretation, or just incompleteness, of software requirements produces an environment where redirection of effort frequently occurs, resulting in a nullification of past work $[16]$ . It becomes advantageous to hide or postpone problems $[6, 32]$ , and the delivered software product often is not suited to the sponsor's needs. The later the need to modify or correct a software product is recognized, the higher the cost to implement the modification or correction $[5, 16]$ .

Given these attributes of software, it is not surprising that those responsible for developing a software product often demonstrate an inability to plan $[11, 31]$ , to revise plans $[3, 11, 16]$ , to monitor progress or change $[5]$ , and to present a clear leadership role $[31]$ . What result, again are late deliveries, high development costs, unsatisfied sponsors, and high maintenance costs.

## Key Management Considerations

An important insight to understanding the problems associated with managing software development is that most difficulties can be traced to the uncertainty that pervades software development. Software development is an information-intensive activity, and decision points are continually reached where the decision maker possesses inadequate information. Many decisions, hence, tend to be postponed in the hope that the needed information will appear later; many of the decisions that are made result in inappropriate actions.

This uncertainty emanates from numerous sources. First, many projects involve complex or state-of-the-art technologies. Thus, doubt arises in selecting the most appropriate hardware/software design, in estimating the resources to commit to the development effort, and in anticipating how the implemented product will perform. Second, innovative or unstructured software applications are increasing in number. It becomes difficult in such situations to state clear, concise, and complete requirements. Third, there is the influence of change — technological changes affect designs, environmental changes affect requirements, personnel changes affect development plans, and software introduction itself may change the organization, thus, possibly affecting requirements. Finally, the physical size of a large software product requires that development be accomplished through the combined efforts of many people. The more interdependent the assigned tasks, and the more differentiated are the individuals involved, the greater the uncertainty within a project.

Two means available for coping with uncertainty are reducing the absolute amount of uncertainty, and facilitating the flow of information to those individuals who must confront uncertainty. A number of guidelines have appeared, primarily in an anecdotal form, that provide for one or both of these means for dealing with the uncertainty inherent to the management of large software development efforts.

## Management guidelines

Task assignments should establish an accountability for results. Without the capability to associate the occurrence of some event to a specific individual, it becomes impossible to trace and resolve errors and delays.

As requirements relate to a dynamic world, large software products must continually evolve. To avoid disaster, the development effort must be change receptive, i.e., change must be anticipated, planned, and controlled.

The designer's intent must be captured and expressed as simply, unambiguously, and completely as possible. Without conceptual integrity [3, 24] it becomes extremely difficult to handle the mass of detail associated with large software development.

Continual validation [38] enables a redirection of effort without compromising objectives. What is desired is the capability to recognize errors early in development.

A common language is needed in order that all participants understand the intent of the designer and can express their reactions to the designer. The development of a continuity of thought also enables a project to survive participant turnover.

By imposing discipline upon participants, their contributions are exposed early in an understandable form. Correspondingly, participants need to be precisely informed as to the nature of their contribution.

If tasks are defined so as to minimize the need for participant interaction, the smaller the likelihood that misunderstanding between participants will occur. Thus, task independence, simplifies the development effort.

Individual tasks in a software development effort possess an inherent amount of uncertainty. If an implemented management methodology is not obtrusive, the additional obligations required of participants can only add to this uncertainty.

Finally, both the software product and the software development process must be made visible. Much uncertainty is reduced if sponsors can “see” their product, and if developers can assess project status.

## Modern software practices

The management of software development can benefit from recently introduced software methodologies in ways that are very similar to how software practices have been enhanced. Table 1 relates the more familiar of these methodologies to the above management guidelines.

Modularity [26] refers to the segmenting of a software product's functions into small, well defined, independent modules. Ideally, the only information any module requires of another is descriptions of what operation is performed, and what data need to be passed to and from the module. If modularity is successful, the software product should possess a clear, compelling design, and be easily modified. Also, modularity does provide a basis for assigning tasks and monitoring progress.

Stepwise refinement [12] involves the implementation of an abstract entity as a succession of more primitive entities. The objective is to develop a total design in a clear, natural manner to prevent those early design commitments that excessively constrain an evolving design. A byproduct of stepwise refinement is the capability to validate a design early in the design process.

Top down development [23] provides the practical means of incorporating modularity and stepwise refinement into the program implementation process. Program development proceeds incrementally, level by level, with testing and integration accomplished along with coding rather than afterward. As the primary control structures are defined and exercised early in program implementation, the software product becomes more visible and faulty designs are evidenced earlier.

Table 1. Benefits of Applying Modern Software Practices

<table><tr><td>Methodology</td><td>Guidelines Enhanced</td></tr><tr><td>Modularity</td><td>Accountability, Change Receptiveness, Conceptual Integrity, Task Independence, Visibility</td></tr><tr><td>Stepwise Refinement</td><td>Conceptual Integrity, Continual Validation, Continuity of Thought, Task Independence</td></tr><tr><td>Top Down Development</td><td>Change Receptiveness, Conceptual Integrity, Continual Validation, Continuity of Thought, Discipline, Unobtrusiveness, Visibility</td></tr><tr><td>Structured Design</td><td>Conceptual Integrity, Continual Validation, Continuity of Thought, Discipline</td></tr><tr><td>Structured Review</td><td>Accountability, Continual Validation, Continuity of Thought, Discipline, Unobtrusiveness, Visibility</td></tr><tr><td>Chief Programmer Team</td><td>Accountability, Conceptual Integrity, Continuity of Thought</td></tr></table>

Structured design [30] applies the concepts of modularity and stepwise refinement to the initial system design effort. By decomposing a software product into functional units at an early design stage, and formally describing the interfaces between units, validation of the design is facilitated, resulting in earlier recognition and correction of errors.

Structured review [15] involves a formal, team oriented critique of current development efforts, e.g., system design, program design, test plan, and code. If successfully applied, structured reviews can result in better designs, early error detection, and software visibility.

The chief programmer team [1] is an organizational means by which modern software practices and personnel specialization can be exploited. By having the chief programmer provide a total design and then assign implementation tasks to a number of specialists, the conceptual integrity of the software product and the accountability of participants are enhanced.

Modern software practices possess the potential to eliminate much uncertainty from large software development efforts by simultaneously providing a global and local awareness of the structure of a software product. A significant amount of uncertainty, however, will always be present in software development. In order to suggest possible means of coping with this remaining uncertainty, an information processing approach to organizational design will be introduced.

## Organizing for uncertainty

An increasingly popular perception of organizations holds that they are open systems which must deal with work related uncertainty $[14, 33, 34]$ . As the uncertainty facing an organizational unit increases, decision makers must process an increasing amount of information in order to achieve a given level of performance $[17]$ . Organizational designs, i.e., those patterns of resource allocations that link together the technology, tasks, and human components of an organization, thus must provide information processing capabilities appropriate for the level of uncertainty confronting each organizational unit.

Building upon Galbraith's [17] ideas, Van de Ven, et al. [35], identified three predominant coordination modes for providing information processing capabilities. The first is an impersonal mode, e.g., policies, plans, schedules, procedures, rule, and standards. The second is a personal mode, i.e., utilization of a liaison or boundary spanner linking role, and finally, a group mode, e.g., the mutual interaction between members of a task force. Coordination costs and information processing capacities both increase as one opts, respectively, for impersonal, personal, and finally, group modes of coordination.

## The Problem

The traditional approach for managing large software development efforts can generally be characterized by the acceptance of a discrete, sequential life cycle orientation, and the assignment of total development responsibility to a single project team, whose size varies depending upon manpower needs of each life cycle stage. However, adoption of such a management strategy, does not provide an effective means for coping with the uncertainty inherent to the development of large software systems. The discrete life cycle orientation precludes a full exploitation of modern software practices. Likewise, the single project organization ignores the reality that different life cycle activities are characterized by varying levels of uncertainty and hence require different organizational structures.

## A Solution: Evolutionary Development

Practitioners [7, 9] have noticed that the first implementation of any large software product is rarely successful. In fact, explicitly planning for at least one complete development iteration has resulted in more realistic development schedules.

The benefits from adopting an iterative approach to large software development have suggested a new perspective on the development life cycle. While appearing under a number of guises $[2, 18, 21, 24, 36, 37]$ , this means of applying modern software philosophies to the entire development cycle is most aptly termed evolutionary development. Simply, large development efforts are viewed as a succession of smaller development efforts, where an initial implementation provides only the most basic requirements, and succeeding implementations build upon one another until all requirements are provided in the final implementation.

Evolutionary development directly reduces the uncertainty associated with large software development in a number of ways. First, decomposing a large development effort into a collection of smaller development efforts reduces the complexity of individual project tasks. Second, sponsors are able to experiment with, and critique early implementations. Third, since succeeding implementations are developed only after prior implementations have been operationally evaluated by sponsors, the software maintenance function is brought into the development cycle. Fourth, the introduction of changes into succeeding implementation becomes a proactive, rather than reactive, activity. Fifth, major development difficulties typically arise in later stages when critical interfaces are enhanced. As these efforts will make up the latter implementations of evolutionary development, the degree of risk associated with early implementations is correspondingly reduced. Sixth, sponsors are better able to evaluate the worth of each requirement as the costs associated with satisfying individual requirements are more visible. Finally, this approach can be applied to the modification of an externally acquired software package, i.e., the package as received composes the initial implementation. Since externally acquired software is handled similarly as internally developed software, more consistent software policies should result.

Two more subtle benefits of adopting the evolutionary development perspective are of even greater importance. Evolutionary development enables a total exploitation of modern software practices, and an organizational design that more appropriately matches organizational information processing requirements to information processing capabilities is developed.

## Evolutionary life cycle

A pictorial representation of evolutionary development is shown in Figure 1. The development effort commences with requirements analysis.

After requirements analysis an initial, basic version of the software product is fully implemented. A succession of more refined versions follows, ending with a final version, i.e., an implementation that satisfies the full set of sponsor requirements.

## Requirements Analysis

Requirements analysis is the most crucial step in the development of a software product. If requirements are unsatisfactory, it becomes impossible to validate the software product and to manage the development effort.

A number of related tasks compose the requirements phase of evolutionary development. First, a clear, precise, and complete functional description of the software product must be derived. Second, this functional description needs to be validated. An apparently successful means of validating a functional description has been described by Berrisford and Wetherbe [4]. Their approach involves developing a prototype output system that can be experienced directly by project sponsors. Thus, any limitations of the functional description can be detected and corrected during requirements analysis. Third, agreement must be reached by the sponsor as to which requirements are to be satisfied with each incremental version of the software product. This agreement is formally expressed by establishing acceptance criteria for each version. Finally, the development schedule and budget are established.

In order to achieve the anticipated benefits of evolutionary development, software product versions should be characterized by relatively short time horizons. Richards [29] argues this time horizon should be no more than six months. Longer development periods result in sponsors losing touch with projects and, thus, becoming dissatisfied as well as unable to provide needed feedback information. Another argument for short version time horizons is to avoid the problems associated with technical staff or sponsor turnover [9].

## Version Development

As illustrated in Figure 1, version development consists of the sequential execution of system design, program implementation, acceptance testing, and quality control testing. Ample opportunities avail themselves for applying modern software practices—structured design for system design, top down development for program implementation, and structured review throughout. Additionally, the relatively small size of each version overcomes many of the staffing and coordination problems that have been experienced by organizations applying the chief programmer team concept.

![](/api/attachments/PJKA67BC/fulltext/images/412a4f39ed2f51355716a09ad5f0bce163ff7208ddc5e0dfba41f1478a551f08.jpg)  
Figure 1. Evolutionary Life Cycle

It is important that the distinction between acceptance testing and quality control testing be clear. Acceptance criteria focus on version implementation by enabling a validation of a version against stated requirements. Quality control testing, on the other hand, validates these stated requirements against current organizational realities. If it subsequently becomes apparent that the stated requirements must be changed, all further development efforts must be delayed until agreement is again reached on acceptance criteria for later versions, and on revisions to the project's schedule or budget.

It is also critical to underscore the importance of the first version of a software product. As all later versions should be viewed as enhancements to the preceding version, the control structure of the initial implementation must allow for a natural incorporation of the full set of requirements.

## Organizational design

Given the nature of evolutionary development, the need for at least three forms of organizational entities becomes apparent: a requirements analysis entity, a version development entity, and a project-version linkage entity. Table 2 provides a suggested organizational design for evolutionary development. The basis of this design is the amount of uncertainty inherent in the tasks to be accomplished by each entity.

Since requirements ultimately derive from constantly evolving organizational realities, the tasks associated with requirements analysis are characterized by high levels of uncertainty. A group coordination mode, where participants freely communicate with one another on a frequent and informal basis, is advocated. Representatives of the functional area(s) sponsoring a project should compose a majority of the participants, and the leader of the requirements analysis effort should be the functional manager who is immediately responsible for the sponsoring organization [29, 39]. System staff personnel would also participate as needed to provide particular skills or information.

Version development is characterized by moderate uncertainty levels where the amount of uncertainty to be confronted is determined by the degree of task independence achieved. A personal mode of coordination is consequently advocated, and the chief programmer team provides an ideal structure. The chief programmer is the individual who coordinates team activity.

Many organizations have experienced difficulties in implementing the chief programming team concept. The major difficulty appears to be the scarcity and salary demands of individuals who possess attributes required of a chief programmer [37]. Consequently, what is recommended is not necessarily a pure chief programmer team approach, but a modification of the concept that meets organizational constraints.

As long as quality control problems do not arise, little uncertainty should be expected in monitoring project progress through the sequence of version implementations. Coordination through an impersonal mode, i.e., compliance with version acceptance criteria and the project schedule and budget, should suffice. However, when crises do arise, the need for a personal coordination mode is felt. This role is the responsibility of the project coordinator.

The project coordinator is accountable for a software product after the requirements phase has been completed. It becomes the project coordinator's task to expedite the product through the successive version development efforts. Responsibility for the success of the software product, however, remains with the functional manager. Thus, the project coordinator, represents a true linking role, in which the incumbent represents neither the sponsoring organization nor the version development teams.

When significant problems arise during the development effort, the project coordinator first works with the affected organizational entity in resolving the problem. Next, agreement is obtained from a steering committee representing the project sponsor as to revisions in version acceptance criteria, and project schedules and budgets. It is just as important, however, that the project coordinator does not become intimately involved with the version development effort as long as the project proceeds as planned.

Table 2. An Organizational Design for Evolutionary Development

<table><tr><td>Entity</td><td>Coordination Mode</td><td>Leader</td><td>Participants</td></tr><tr><td>Requirements Analysis</td><td>Group</td><td>Functional Manager</td><td>Functional Representatives System Staff Representatives</td></tr><tr><td>Version Development</td><td>Personal</td><td>Chief Programmer</td><td>Chief Programmer Team</td></tr><tr><td>Project-Version Linkage</td><td>Impersonal (normal) Personal (crises)</td><td>None Project Coordinator</td><td>None Functional Steering Committee</td></tr></table>

## Planning

Modern software practices primarily achieve their benefits because of an increased attention to design. Likewise, an increased attention to planning, is a requirement of evolutionary development. The derivation of version acceptance criteria, and schedules and budgets forces more intensive planning during requirements analysis. The assignment of tasks among the members of a chief programmer team forces more intensive planning during version development. Thus, an increased attention to planning is a natural outgrowth of evolutionary development. Utilization of methodologies, such as PERT, that further enforce this attention to planning is recommended.

It has been suggested that the tasks assigned during version development should take no longer than two weeks to complete $[8, 22]$ . Short time horizons enable an earlier detection of problem situations. They also make it possible for development team members to savor the satisfactions associated with task closure more frequently, and require planning at a more detailed level. These horizons often result in less complex and interdependent tasks.

For planning to be effective, it is necessary to arrive at realistic time and cost estimates. Software estimation historically has been, and continues to be, a major difficulty associated with the management of large software development efforts $[7, 10, 19, 20, 27, 38]$ —intuition seems to work with small projects but not large projects, requirements and design details often remain ambiguous until a significant portion of development activities have transpired, productivity rates are highly variable, little data or experience is had with similar projects, little penalty is often associated with a poor estimate, and, little motivation often exists for realistic estimation because the individuals involved perceive that accurate estimates would result in a project not being approved. However, recent techniques have evolved that do provide for much improved estimates $[20, 27]$ . Additionally, as progress on a project is monitored, the gathered data can be used to refine initial estimates. Such data can also be maintained in an historical database for use in deriving standards for estimating the time and cost of future projects.

## Control

As with more traditional software management practices, project control is achieved through the specification and attainment of milestones. The difference with evolutionary development is that milestones, defined as the acceptance of each version, are tangible rather than intangible. Fewer but more critical milestones, whose significance to the software product is clearly evident to project sponsors, result.

Control of version development is more complex, with four mechanisms required. First, sponsor feedback regarding the system design must be obtained prior to the start of program implementation. Donelson [13] suggests that requiring the user manual to be developed parallel to system design, and that it be delivered to and accepted by the sponsor prior to program implementation, provides for this feedback. Second, the intensive use of structured reviews enables the chief programmer team to validate the system design against requirements, program designs against the system design, and coding and testing against program design. Third, an ability to track and control change is necessary. This can be accomplished by (1) maintaining the version schedule, budget, and acceptance criteria as a baseline document, (2) establishing the project librarian role through whom all designs, code, and test results must pass, and (3) requiring that all changes be approved by the chief programmer, the project coordinator, or the functional steering committee. Finally, it is important that the project coordinator be able to accurately assess the status of a version at any point in time. If task assignments possess short time horizons, and if the project librarian has knowledge of current task states, such a capability is provided.

## Documentation

The crucial element in managing large software development is project comprehension, i.e., the maintenance of a conceptual understanding of a software product, and an awareness of its state of development. While evolutionary development intrinsically provides a skeletal framework for comprehension, it is only through a strict adherence to documentation standards that project comprehension becomes a reality for all organizational participants involved in the development effort.

When all plans, designs, assignments, evaluations, explanations, results, and statuses are formally collected in a consistent fashion, communication between the diverse participants who must contribute to the development of a large software product is greatly facilitated. The use of graphical techniques is particularly advocated as they are concise, accurate, and easily understood [9].

The existence of a permanent, complete, correct, and accessible record of all communication regarding development additionally provides project independence from individual designers and programmers, thereby reducing vulnerability to personnel turnover or “blackmail” [9]. In this regard, fewer development problems tend to arise if all documentation for a project is maintained as a single volume under singular accountability. This volume, most commonly referred to as a unit development folder, may exist in an online or offline mode. With evolutionary development, unit development folders should be maintained for each version and for the entire project.

Nonetheless it is expected that documentation obligations under evolutionary development would be less than those experienced with more traditional management approaches. This should arise since a large portion of the needed documentation would naturally evolve through the use of modern software practices.

## Conclusion

This article has developed from the premise that most software development problems can be traced to the uncertainty inherent in such endeavors. The two most direct strategies for achieving more effective management of software development are to reduce the absolute amount of uncertainty within a project and to facilitate the information flow to decision makers confronted with uncertainty.

The developmental context established by adopting an evolutionary development perspective should result in less uncertainty through a conceptual simplification of the software product, and a capability to fully exploit modern software practices. Information flow is correspondingly enhanced through the early reception of feedback from project sponsors, and an organizational design that matches information processing requirements and capacities throughout the project life cycle.

A further advantage of this management perspective is its flexibility. Regardless of the size, source, or focus of a software development effort, a single management approach suffices with the only variation being the number of versions that compose the software product. All planning and control mechanisms can be applied to all projects resulting in consistent and understandable policies and procedures.

While this perspective is advocated for all organizations, existing policies and constraints of particular organizations may preclude full or even partial adoption. A number of organizations have realized success in an area where success is not common by following practices similar to those described. Obviously, success cannot be guaranteed. Any commitment of resources in implementing their practices bears a risk, but this risk must be contrasted with those costs currently traced to late, or otherwise unsatisfactory, software products.

## References

[1] Baker, F. T. "Chief Programmer Team Management of Production Programming," IBM Systems Journal, Volume 11, Number 1, 1972, pp. 56-73.

[2] Basili, V. R. and Turner, A. J. "Iterative Enhancement: A Practical Technique for Software Development," IEEE Transactions on Software Engineering, Volume 1, Number 4, 1975, pp. 390-396.

[3] Belady, L. A. and Lehman, M. M. “The Characteristics of Large Systems,” in Research Directions in Software Engineering by P. Wegner (ed.), MIT Press,

Cambridge, Massachusetts, 1979, pp. 106-138.

[4] Berrisford, T. and Wetherbe, J. "Heuristic Development: A Redesign of Systems Design," MIS Quarterly, Volume 3, Number 1, 1979, pp. 11-19.

[5] Boehm, B. W. “Software Engineering: R & D Trends and Defense Needs,” in Research Directions in Software Engineering by P. Wegner (ed.), MIT Press, Cambridge, Massachusetts, 1979, pp. 44-86.

[6] Brandon, D. H. “The Economics of Computer Programming,” in On the Management of Computer Programming by G. F. Weinwurm (ed.), Auerbach, Princeton, New Jersey, 1970, pp. 3-18.

[7] Brooks, F. P. The Mythical Man-Month, Addison-Wesley, Reading, Massachusetts, 1975.

[8] Connors, T. "Project Management," Proceedings, SMIS Annual Conference, Washington, D.C., 1978, pp. 169-176.

[9] Corbata, F. J. and Clingen, C. T. "A Managerial View of the Multics System Development," in Research Directions in Software Engineering by P. Wegner (ed.), MIT Press, Cambridge, Massachusetts, 1979, pp. 139-160.

[10] Daly, E. B., “Management of Software Development,” IEEE Transactions on Software Engineering, Volume 3, Number 3, 1977, pp. 230-242.

[11] DeRoze, B. C. and Nyman, T. H. "The Software Life Cycle — A Management and Technical Challenge in the Department of Defense," IEEE Transactions on Software Engineering, Volume 4, Number 4, 1978, pp. 309-318.

[12] Dijkstra, E. W. “Notes on Structured Programming,” in Structured Programming by O. J. Dahl, E. W. Dijkstra and C. A. R. Hoare, Academic Press, New York, New York, 1971, pp. 1-82.

[13] Donelson, W. S. “Project Planning and Control,” Datamation, Volume 22, Number 6, 1976, pp. 73-80.

[14] Duncan, R. B. “What is the Right Organization Structure? Decision Tree Analysis Provides the Answer,” Organizational Dynamics, Volume 7, Number 3, 1979, pp. 59-79.

[15] Fagen, M. E. “Design and Code Inspections to Reduce Errors in Program Development,” IBM Systems Journal, Volume 15, Number 3, 1976, pp. 182-211.

[16] Fink, R. C. “Major Issues Involving the Development of an Effective Management Control System for Software Maintenance,” Proceedings, IEEE Computer Software and Applications Conference, Chicago, Illinois, 1977, pp. 533-538.

[17] Galbraith, J. R. “Organizational Design: An Information Processing View,” Interfaces, Volume 4, Number 3, 1974, pp. 28-36.

[18] Gosden, J. A. “Some Cautions in Large-Scale System Design and Implementation,” Information and Management, Volume 2, Number 1, 1979, pp. 7-13.

[19] Jones, G. H. “Project Management: An Overview,” Proceedings, SMIS Conference, Washington, D.C., 1978, pp. 161-168.

[20] Kustanowitz, A. L. “System Life Cycle Estimation (SLICE): A New Approach to Estimating Resources for Application Program Development,” Proceedings, IEEE Computer Software and Applications Conference, Chicago, Illinois, 1977, pp. 226-232.

[21] McGowan, C. L. and McHenry, R. C. "Software Management," in Research Directions in Software Engineering by P. Wegner (ed.), MIT Press, Cambridge, Massachusetts, 1979, pp. 207-253.

[22] Metzger, P. W. Managing a Programming Project, Prentice-Hall, Englewood Cliffs, New Jersey, 1973.

[23] Mills, H. "Top Down Programming in Large Systems," in Debugging Techniques in Large Systems by R. Rustin (ed.), Prentice-Hall, Englewood Cliffs, New Jersey, 1971, pp. 41-55.

[24] Mills, H. “Software Development,” in Research Directions in Software Engineering by P. Wegner (ed.), MIT Press, Cambridge, Massachusetts, 1979, pp. 87-105.

[25] Moore, J. H. "A Framework for MIS Software Development Projects," MIS Quarterly, Volume 3, Number 1, 1979, pp. 29-38.

[26] Parnas, D. L. "A Technique for Software Module Specifications with Examples,"

Communications of the ACM, Volume 15, Number 5, 1972, pp. 330-336.

[27] Putnam, L. H. "A General Empirical Solution to the Macro Software Sizing and Estimating Problem," IEEE Transactions on Software Engineering, Volume 4, Number 4, 1978, pp. 345-361.

[28] Reynolds, C. H. "What's Wrong with Computer Programming Management," in On the Management of Computer Programming by G. F. Weinwurm (ed.), Auerbach, Princeton, New Jersey, 1970, pp. 35-44.

[29] Richards, N. L. “Organizing for Common Systems,” in Information System Methodology by G. Bracchi and P. C. Lockemann (eds.), Springer-Verlag, Berlin, 1978, pp. 120-141.

[30] Stevens, W. P., Myers, G. J. and Constantine, L. L. “Structured Design,” IBM Systems Journal, Volume 13, Number 2, 1974, pp. 115-139.

[31] Thayer, R. H. and Lehman, J. H. "Software Engineering Project Management: A Survey Concerning U. S. Aerospace Industry Management of Software Development Process," SM-ALCIALD, TR-77-02, Sacramento Air Logistics Center, USAF, Sacramento, California, 1977.

[32] Tsichritzis, D. "Project Management," in Advanced Course on Software Engineering by F. L. Bauer (ed.), Springer-Verlag, Berlin, 1973, pp. 374-384.

[33] Tushman, M. L. “Technical Communications in R & D Laboratories: The Impact of Project Work Characteristics,” Academy of Management Journal, Volume 21, Number 4, 1978, pp. 624-645.

[34] Tushman, M. L. and Nadler, D. A. "Information Processing as an Integrating Concept

in Organizational Design," Academy of Management Review, Volume 3, Number 3, 1978, pp. 613-624.

[35] Van de Ven, A. H., Delbecq, A. L. and Koenig, R., Jr. "Determinents of Coordination Modes in Organizational Design," American Sociological Review, Volume 41, Number 2, 1976, pp. 322-338.

[36] Weinberg, V. Structured Analysis, Yourdon, New York, New York, 1976.

[37] Yourdon, E. How to Manage Structured Programming, Yourdon, New York, New York, 1976.

[38] Zelkowitz, M. V. “Perspectives on Software Engineering,” Computing Surveys, Volume 10, Number 2, 1978, pp. 197-217.

[39] Zmud, R. W. and Cox, J. F. “The Implementation Process: A Change Approach,” MIS Quarterly, Volume 3, Number 2, 1979, pp. 35-43.

## About the Author

Robert W. Zmud is an Associate Professor in the Information Systems Department at the College of Business Administration at Georgia State University in Atlanta, Georgia. He received a B.A.E. at the University of Virginia, an M.S. at MIT, and a Ph.D. at the University of Arizona. His articles have appeared in a number of journals, including Management Science, Decision Sciences, and MIS Quarterly. His current research interests involve behavioral processes in the design, development, and implementation of MIS. He is a member of ACM, AIDS, SMIS, TIMS, and the Academy of Management.
