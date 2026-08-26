---
otero_id: 26944
otero_key: "PW6RTS6U"
title: "Project Management Considerations for Distributed Processing Applications"
authors: "Robert G. Felix; William L. Harrison"
year: "1984"
journal: "MIS Quarterly"
doi: "10.2307/248663"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Project Management Considerations for Distributed Processing Applications
Author(s): Robert G. Felix and William L. Harrison
Source: MIS Quarterly, Vol. 8, No. 3 (Sep., 1984), pp. 161-170
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/248663

Accessed: 08/05/2014 20:13

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Project Management Considerations for Distributed Processing Applications

By: Robert G. Felix
Fletcher-Challenge Ltd.
Private Bag
Auckland, New Zealand

By: William L. Harrison
College of Business
Oregon State University
Corvallis, Oregon 97331

## Abstract

Many distributed information processing systems will fail because of people and organizational problems — not technical problems. These problems can be addressed by careful skill and organizational planning, by added attention to training, and by an enhanced project management methodology. This methodology must be amended to include a strong requirement for technical architecture at the start, and for thorough systems testing at the finish.

Distributed systems are more complex and, to be successful, will require more work and expertise in the central systems staff, not less. Economies of scale will keep most of the work and expertise within the central staff.

Keywords: Project management, information systems design, distributed processing

ACM Categories: K.6, K.6.1

## Introduction

Project management concerns itself with planning, organizing, directing, and controlling the efforts of an applications development team to bring to life a computer application that is both efficient to use and cost effective to build. Project management techniques have been utilized for many years to develop centralized applications within the constraints of budgets and time. Distributed processing systems typically present additional difficulties for the project management staff that standard techniques do not address.

Much of the information systems literature addresses the technical problems inherent in developing a distributed system, or alternatively, the problems that systems managers may face in a “distributed” environment. This article assumes that the organization is committed to a distributed system and builds on that to establish managerial concepts about the development of the system. These are project management concepts that must be put in place before the project begins; in most cases they cannot be implemented effectively after the project is underway.

Information systems, whether distributed or not, are developed to address a basic business process. The process could be the taking of orders, the control of inventory, the fiscal management of independent agencies, or any one of a number of other business functions. While combination of functions to be performed will vary, depending upon the type of organization served and whether it is in the private or public sector, the basic theme remains — an information system is a capability developed to serve a specific purpose, and the effectiveness of that service becomes their rationale and the measure of their success.

A review of the literature, and years of observation, would suggest that most systems failures result from organizational and personnel problems, not technical problems. Technical problems can usually be detected and repaired before the system is put in jeopardy. The cost may be high in terms of either budget or schedule, but the repair can be made. Organizational and personnel problems often cannot be redressed, and continue to jeopardize the success of the system itself.

The project management issues discussed here are not startling, new ideas. For the most part, they represent issues which have been part of project management for the development of centralized applications. The nature of distributed processing does, however, dictate an increased emphasis on some aspects of the problem of project management [2].

## Developing a Distributed Data Processing Perspective

In order to develop a common perspective for later discussions it is important to establish a definition of distributed data processing (DDP) and to identify the factors within a firm which prompt managers to move to that environment. An informal definition is provided here:

"Distributed data processing is defined as the implementation of a related set of programs across two or more data processing centers or nodes. The programs are related in that they share or pass data between them. Each node is generally capable of performing data processing applications independently, and thus would normally have data storage and program execution facilities [10]." (For another definition see [5].)

By extending the notion of two or more data processing centers into business terms we may picture many geographically dispersed business units, each of which has local data processing needs and each of which has the need to coordinate activities with the other units or with corporate headquarters. Many of the data processing activities of any single business unit may be similar to many of the data processing activities of the other units. Numerous examples of such organizations exist — sales organizations with regional, district, and local sales offices provide one such example. The National Forest System within the USDA provides another. In both cases the activities of each of the distributed units are very similar.

The distributed data processing environment has been made possible by the exponential improvements in computer price/performance ratios. Managers of organizational units have been motivated to move into that environment by unresponsive centralized computing facilities. Benjamin [1] makes an interesting case for the increasing importance of distributed systems. McLean [9] points out that long delays in the development of applications had become commonplace. Kaiser and King [7] indicate that managers frequently were asked to work with a collection of programmer/analyst intermediaries over which they had no real control. In addition, unit managers have never been satisfied with algorithms which chargeout computing center costs nor with the increasingly bureaucratic responses which seem to accompany large scale computing centers. The distributed data processing environment appears to offer increased reliability and availability to be more in tune with the units' needs, and to be under local control.

There are other incentives to prompt organizations to move to a distributed environment. These reasons have a degree of rationality associated with them which data processing managers may be unwilling to concede to the previous motivating forces. In particular, the centralized computing facility may not be able to provide the ever-increasing capacity necessary to adequately provide for the local organization's data processing needs. Major upgrades in capacity often have a longer cycle time than the organization's need for computing capacity. New equipment becomes overloaded before newer equipment can be specified, tested, and installed. Smaller, distributed systems may provide a life cycle flexible enough to relieve these capacity problems.

Another rational motivation is a function of the difference in the rate of change of computing and communications costs. Computing (mainly hardware) costs are declining at a much faster rate than communication costs. In many circumstances this means that data may be processed and stored locally in order to forego potentially excessive communication costs which might otherwise be incurred [10].

Withington made an excellent case for something he called “distributed responsibility.” Withington [11] and Buchanan and Linowes [3], have provided very complete, descriptive treatment to help managers identify their own organization’s profile with respect to controlling the development and operation of applications in a distributed data processing environment. This article is intended to be more normative than the Buchanan and Linowes article, and more specific than the Withington article. It is intended to provide the manager with a set of operable project management recommendations to assist in the development of distributed applications within an organization which has predominantly been centralized.

A few comments about the “success” or “failure” of a system are in order before going further. The success of a system is measured here by the way it satisfies the purpose originally set forth. The system fails if it does not achieve its goals. An alternate view might be that the system fails if the manager responsible for the process perceives the system to have been a poor investment. Two ideas are important here; the concept of the system as an investment, and the concept of a subjective, perceptual measure of success or failure. (For another view of the evaluation of information systems see $[4, 6, 8]$ .)

If a system costs too much, takes too long, or is clumsy and unfriendly to use it may not seem to be a good investment even if administrative savings are realized. In fact, if a system is too clumsy additional people may be needed after the system is installed in order to manage it. In spite of substantial shortcomings, a system that allows greater management control or more efficient processing of transactions might be viewed as a success, despite its failure to achieve the planned economic goal. Because of the complex and interlocking purposes that information systems often serve, a subjective measure of success or failure becomes the only realistic approach.

A system should be judged by the responsible manager, weighing many factors to yield a subjective conclusion. This conclusion is based on the perceived balance between the effort required, the cost, and the benefits and consequences produced. One possible measure of success could be whether the project management team is invited back for another mission, or the circumstances under which it is invited back.

## The special nature of distributed processing systems

If a distributed data processing approach is taken to solve the needs of a business process, there are certain general differences between it and a centralized system which must be recognized. By its nature, the technical design of a distributed system is more complex since the DDP environment requires the use of telecommunications, decisions about which process will be performed at which location, rules for database usage, and so on. There are, therefore, many more technical choices and many more chances to err in the design.

The computers used will probably be minicomputers, at least at the nodes (the dispersed locations) if not at the host (the central site). For all their advantages, minicomputers offer a more limited, constrained technology. They are easier to overload than a large mainframe. The choices for solving an overload are more complex and more subject to error. Minicomputer operating software lacks some of the design features commonly available on large-scale machines, making application software harder to develop. This adds to the design complexity of a distributed system. A centralized system, or even one with a remote job entry capacity, has many pitfalls, but the design choices and opportunities are fundamentally less complex than with a distributed system.

There are social differences as well. If a centralized system is developed and perceived to be a failure, only one site, one organization, one set of managers is disgruntled. With some effort they can often be convinced to try again. In a distributed setting, if the system does not work very well at one site, the “well” may be “poisoned” for all the sites. A problem from which a single site might have recovered will multiply out of proportion as word spreads through the grapevine. Recovery will involve more people and more sites and will therefore be more complex, more time consuming, and more expensive. Since the system involves many sites, the project manager cannot personally visit each site informally to assess progress and identify troublesome issues. Visits are most often scheduled and formal, thus the communications about problems becomes imperfect and inadequate.

Furthermore, at a local site, possibly a branch or regional office, the main order of business is the day-to-day work. The main business is not experimenting with the use of computers. If a distributed system is brought in, local people assume it will work. The tolerance for what the system staff feel to be small problems is much less than at a headquarters site. People at central sites generally have a greater willingness to experiment and take risks. They usually take a longer term view, as they appropriately should. The local site has neither the charter nor the staff to allow this luxury. The end result is that the distributed system, when delivered to the local site, is under great pressure to deliver the advertised results in an environment that is not very forgiving. Small problems may then set the installation of the system back substantially at sites not yet visited.

Because of these issues of both technical and social complexity, distributed processing systems have certain requirements that are different from those of a centralized system from a project management sense. The additional requirements of distributed data processing are in four categories:

1. Skill requirements and organization structure,

2. Personnel training and development requirements,

3. Program management requirements, and

4. Technical policy requirements.

## Skill Requirements and Organizational Structure

Two kinds of skills are particularly important in distributed situations and must be available at the start of the development effort. The first skill is technical expertise in the hardware, operating system, applications software, and database technology to be used. Centralized systems, developed on an existing mainframe, tend to emphasize language skills — COBOL, MARK IV, or whatever. Distributed systems, on the other hand, require more comprehensive or unified skills. These systems are effective because of the integrated use of several technologies. For example, a distributed order entry system could be adequately programmed and well-supported by an efficient database management system but still fail because of poor network communications. Integration across the full range of technologies is essential.

The second skill lies in business process or procedural expertise. In a distributed environment the likelihood that all the decentralized offices or plants will use exactly the same procedures is very small. Enforcing an arbitrary set of procedures system-wide would make little sense and might generate undue resistance. The traditional approach of having a systems analyst understand the procedure to be automated can be very dangerous in a distributed system. The analyst's second-hand understanding can never be fully responsive to the subtle differences of procedure at each site. There are too many details and ambiguities. A first-hand understanding is needed to weigh the procedures, to shape the system to be installed, and to adapt the local procedures to that shape.

There are many examples of attempts to design systems which would support the same basic activity in many different locations. Typically, these systems have been specified by a cross section of user representatives to make sure everyone's particular interests are considered. Far too often the result is a compromise which fails to fit even a single unit well.

Consider, for example, a system of small mills within a wood products company. Although each mill performs the same basic task of converting timber into marketable wood products, the activities within these mills are varied according to the type of timber utilized, the “generation” of mill equipment used, and the market segment within which the mill’s products are sold. These local differences present the analyst with a much more complex design environment. Thus the need for business procedural skills to shape the system.

A distributed system is created to improve a business process; it serves a specific need. Organization and management of the project should be focused at a central point — the agency headquarters, the division office, or whatever. This central management does not, however, need to be the data processing authority. If the central data processing organization is wedded to a technological concept, a program management philosophy, or a skill level that would be antithetical to the proposed distributed system, then it is better to set up a special organization to implement the system.

It is likely that the technical systems development staff and overall program management should be centralized. To support the required technical expertise — to attract, reward, and develop the technical professional — a centralized organization is almost a necessity. Add to this the usual reasons of economies of scale, management control, and critical mass in a professional group, and the pressure for centralized development is substantial. But it is important that the management of the effort be centralized.

Central management is required for the user organization as well. All the problems with differing procedures at local sites, finding people experienced in the procedures, shifting the power-base (no matter how subtle), and managing the overall training and installation require a strong central control on the user side. The likelihood of achieving success without effective central user management is as small as without central project management. Research efforts or experimental systems have been known to succeed without this central focus, but not a systems effort as envisioned here.

As an example, consider the development of a distributed information retrieval system designed to support scientific inquiry throughout a large chemical products company. The corporate data processing staff was dedicated to the maintenance of a single, centralized system. Project management for the development effort was assigned to a project management team drawn from the research and development division. User representatives from three divisions were selected and assigned to the team under the supervision of an executive vice president. Thus, both centralized system and user management were involved.

Another organizational concept of systems management for distributed processing is the idea of “second level” management. There will inevitably be occasions when the professional development staff is not in agreement with the experts or representatives from the user organization. This can substantially impede a project of moderate complexity. It can be fatal in a very complex or ambitious project because of the delays and misjudgements it engenders. A simple way to resolve such difficulties is to maintain an active dialogue between managers two levels removed from the actual professionals doing the work.

Why two levels? The first level, the supervisory or project management level, is too likely to defend its own position. It does not have the objectivity required to resolve conflicts in program requirements and objectives. However, managers two levels removed can take a larger view without feeling the necessity to support parochial interests. Third level managers, if the organization is deep enough to afford them, are often so removed from the specifics that any resolution of issues tends to be more arbitrary than informed.

After the system is in operation it will be advisable to maintain central control and operational support. Changes, improvements, and enhancements all require the maintenance of a central authority, both to execute the change and to preserve the original goals of the system. Since there will be many sites involved, each running a miniature data processing function, a central support group is needed to answer operational questions and to sponsor ongoing training. These technicians must be available to resolve the many different things that can impact a network and distributed processing capability. As new people join the user organization, they must be introduced and trained on the system. As temporary people replace permanent users for holidays or sickness, they must be supported. If the equipment malfunctions, a system-wide log is needed to identify trends or major deficiencies. If the system involves financial data subject to audit, a central group is important to orient the auditors, to maintain audit discipline, and to provide a record and control of changes. None of this happens without a central support organization; all of it is possible with one.

To obtain the technical expertise necessary for implementing a distributed system, the organization must commit to a level of overhead that might not be otherwise justified. In addition, the organization must develop a career concept that is attractive. The likely career path for a technical expert can be viewed in three phases: development of the expertise on a selected hardware and software system, work on the program that uses the system, and then general research into some other new technology. A full cycle might take four or five years and should prove satisfactory to the individual and productive for the organization.

User expertise is perhaps more difficult to effect. At best, the user organization commits to a program to develop expertise in a few select individuals who are then targeted to be principals in the emerging distributed system. Rarely is much lead time required — six months to a year is adequate in most cases. As it turns out, large distributed systems may take this long or longer to gain management commitment.

A move by the Forest Service to change from a centralized to a distributed environment, for example, has taken several years. Training efforts began in the late 1970s. An early pilot project at Mount Hood National Forest provided guidance for later efforts which will culminate in a distributed processing network throughout the entire National Forest System in 1984-85.

This time factor can often be accommodated with aggressive planning. Time, however, is often less critical than is the commitment of the user organization. The users may balk at setting aside the people and resources necessary to achieve their development. In some situations, a clear career path for the user experts can help solidify their commitment. The assigned user experts may participate in the management and operation of the new system, or they may gain an increased visibility in the user organization that puts them in line for other important responsibilities.

## Personnel Training and Development Requirements

The previous section on organization and skills has already suggested several of the personnel development requirements important to distributed systems. The technical expertise in hardware, operating systems, applications software, database, and telecommunications must be available before the architectural design is begun. Expertise, in this sense, means more than an understanding of how to use the systems technology. It includes the experience to judge the limits and tolerances of the technology, to understand the features that are safe versus those untried, and to recognize the source of errors and problems. An aggressive training program is required, not a laissez faire one. Six months would be a minimum amount of time to spend in a personnel development program.

Procedural expertise on the user side is equally important, and harder to achieve. Ideally, it would include residency at several of the user locations in an administrative or management position to permit a broad view of the business process to be served. This may be impossible from either a career or logistical perspective, so alternative strategies may be needed. As an example, establishing “management” conferences to discuss improvements to the common business processes of all the locations might achieve some of the cross fertilization, visibility, and personal confidence needed. Special projects and consulting assignments across the sites can provide another avenue.

As the system moves toward the installation phase, the user community must be trained in the actual use of the system. There are two special rules for user training in distributed systems. The first rule is to recognize that the management group at each location must be trained as effectively as the staff using the system. (This does not mean the same materials or approach — only the same emphasis.) This training can be acquired from outside sources or developed within the organization. Data General's contract to provide distributed processing systems to the Forest Service contained provisions for different training sessions for system administrators, users, and managers.

The second rule is that five percent of the project budget is barely enough to produce the training materials. That does not include the direct costs of doing the training; it only includes preparing the materials. If this seems excessive, recall the formidable barriers to success we have discussed previously. It is a pocr trade-off to risk several hundred thousand dollars of investment (for a medium-sized distributed systems), only to fail at educating its users.

The users must be trained in both hardware and software. The system hardware should arrive at each site and be tested for use well ahead of scheduled user training sessions. The users should be encouraged to experiment with the system using computer games to develop a hardware and operating software familiarity. In earlier training efforts to introduce managers in the Forest Service to computing, games played an important role in overcoming the reluctance to operating a computer terminal.

To train in the use of the application systems and the database, a condensed, simplified model of the real system should be used. This involves just small data files, a limited number of procedures and, presumably, a very fast response. (The fast response, although helpful for training, may become a problem by setting user expectations higher than the limits achievable with the real system. This has not proven to cause any real dissatisfaction in the long run. Users understand that the actual system does more work, and so can be expected to take longer to do it.)

Training must emphasize how to deal with errors and problems, as well as the basics of running the system. The training should neither explain the structure of the system, nor how it works. Only what it does. Because the local site is not a computer center, and likely does not intend to become one, it will not have a resident programmer or operations staff. The local administrative staff must be able to attend to the small problems that come up in any computer operation. With the back-up of a central operations support staff this should pose no real problem, but it does extend the scope, duration, and intensity of the training.

One way to improve the training is to allow user personnel from the pilot project site to participate in training presentations at other sites. A large wood products firm developing a distributed system for sawmill operations would, for example, make use of operators and other users from the pilot site to develop and present training to other operators and users.

## Program Management Requirements

There are some particular skills needed for the systems program management itself. A large distributed system may take a year to gain acceptance of the concept, two years to design and build, and a year to install; overall, a significant piece of a career. Because of this length of time, as well as the complexity of the systems from a technical view, a special program management approach is needed. Essentially, it is a two level approach. The senior manager, designated the program manager, is assigned overall responsibility for effecting a successful system. As such, the program manager is deeply involved in the initial concept discussions and takes an active management role to analyze the requirements and develop the overall technical architecture.

At this point, a junior manager can become involved in the system to be responsible for the detailed design, development, and testing of the system, and to help in its installation and user training. It would be likely that this person, called a system development manager, would be in line for overall program management responsibilities down the line. The program manager then takes a more distant role, monitoring overall progress. This dual approach allows both a reasonable career path over a multi-year effort, and the application of adequate managerial competence to help assure success. The program manager's talents are used to best advantage and the user is assured continuity of management throughout the project.

The standard project management and system development techniques that are used for centralized systems can be applied to distributed systems as well, but there are additional steps that must be included. The usual system development methodology has four general phases: analysis, design, development, and installation. Many system development methodologies divide each of these four steps into smaller steps, usually to provide better direction to the work. A distributed system requires special emphasis on four areas that may be only lightly considered in a centralized environment. These areas are concept development, technical architecture, testing, and maintenance.

Concept development actually precedes the formal development of the system. It is the period when the systems manager and management in the user organization explore ideas and search for the critical facets of the business that would benefit from the use of computing technology. It is an unstructured period, but not an informal one. While this concept development stage is similar to a systems planning period, it lacks the overt goal of developing a computer system. It focuses instead on improving the business process — a slight, but important shift of emphasis.

The overall technical design, designated as the technical architecture, also requires particular emphasis in distributed situations. A large distributed system will improve and alter a business process through the use of its technology. An efficient distributed system for order entry may, for example, significantly change the behavior patterns of the sales force.

The variety of technologies available today allows a definite trade-off between the computing technology used and the system capabilities, costs, and development schedules. The technical architecture provides a basis to evaluate major technical trade-offs, including those that affect user requirements. Technical architecture is analogous to the architectural drawing for a building; the future course of efforts is shaped at this time.

Because users at the local site may present a less forgiving work force than could be expected at a headquarters office, testing is a critical area of project management. The system must be seen to work perfectly — or very close to it.

There can be no user-debugging period; there can be no excuses for functions agreed to, but not implemented. This requires that users, as well as system developers, clearly understand what capabilities will be delivered. It also requires exhaustive testing to guarantee a quality product. Particularly in a complex environment like a distributed system, it is essential that testing be done early and comprehensively.. As such, testing deserves a project management phase of its own.

There are four levels of testing, and each should be considered separately. Program testing checks the execution and functions of individual programs or modules. (The system presumably is built in a modular structure.)

System testing tests the system for execution, response times, and technical features. A continuing problem in the design of distributed systems is the trade-off between response time, equipment capability, and technical design. The system test is the first time this trade-off can be quantitatively evaluated; it becomes the first test of the technical architecture.

Functional testing is the exhaustive checking of the system's features and functions using "real" data. Every function, error code, and default loop must be carefully evaluated to be sure that it is there, it works, and to compare it to the original specifications. Whereas the system test works against the technical architecture, the functional test works against the user requirements.

Last, there is the acceptance test, preferably at a local site. The system may be perfect in all regards, but it still must be usable by the local people who will work with it. This is an entirely subjective measure, just as the success of the system is subjective. The equipment chosen may be cumbersome or it may even be the wrong color; it makes no difference. It is better to find and fix it during acceptance testing than to install the system and have it poison the well at many other sites. This four level test concept deserves a separate program management step to emphasize its importance, and to assure its execution.

One other project management step should be noted — maintenance. After the system is installed and is in normal operation there will be requests for changes, both as the users grow in their ability and as occasional problems develop in the system. This phase of the project should be planned as carefully as any other, and just as far in advance.

The appropriate way to deal with changes in a distributed system is with the “system release” concept. Changes are gathered together and accepted by representatives of the users and systems management. Then, at intervals of several months, new releases of the system, embodying new application software or new equipment, are presented to the users. This is the only method that maintains the control and discipline needed to support the original goals and the quality of the system. It should be provided as part of the original project management methodology to assure its acceptance and funding.

## Technical Policy Requirements

There are five policies for systems management that are particularly relevant to distributed systems. These are general policies not directed at a particular system project. They must be in place before a project begins.

1. In a distributed system environment, the users may maintain a local database on their processor. It is tempting to allow the headquarters access to this database for reports, perhaps even an unannounced “inspection” of the user’s business operations. The policy must be quite clear, however, that no access is permitted without the local user’s consent. The best method to do this is to establish a special file for access by the headquarters — a file quite separate from the local database. If the local site does not want to pass any data along, the file can be left blank. Whatever data are required by headquarters are placed in this file by the local user at their own discretion and timing. This is a form of the privacy issue, and an important policy to assure that local users maintain and feel a sense of ownership for their part of the system.

2. If the system contains financial data, it will be subject to audit. The policy must be that the users are entirely responsible for the audit of the system. The central system support organization can provide a detailed record of changes to the system process and logic, but that is all. The using organization must be responsible for local procedures, data security, and other audit issues.

3. In order to be assured that the system is useful and satisfies its original concept, the actual use of the system should be tracked. Although this is not a complex task in itself, it requires a policy statement to be sure it happens. The simplest method is to build a few routines into the software that track usage of particular functions or features; this should be provided during the initial design. It adds a little overhead to the cost of the system but is invaluable in evaluating the effectiveness of the system and in providing direction during its operating life.

4. The system should include a language capability that is sufficient to build new reports and change old ones at the local site. Changes in the database structure and fundamental logic are reserved for the corporate support group, but many local questions can be handled by changes in report structures. Few acceptable languages exist to provide this capability but, like user friendliness, it is a goal to be built into the technical architecture. If not stated as a policy goal, then competing requirements may compromise this capability.

5. Last is the policy on decentralization; there should not be one. It should be the result of the system concept and the technical architecture. Some systems are best centralized; some are best decentralized or distributed.

## Conclusions

This litany of issues might suggest that distributed systems are a poor response to organizations' needs; too complex, too difficult to manage, and too subject to risk and failure. On the contrary, the advantages outweigh the disadvantages in most cases. A distributed system is more robust — it is not dependent on a single processor, a single manager, or organization. The system is more natural. Local functions are handled locally, rather than transferring great amounts of work to a central site with the consequent loss of local ownership and control. A well-designed distributed system epitomizes the concept of “power to the people,” removing the arbitrary barriers that centralized data processing organizations tend to create. And a distributed system can be simpler in operation, and technically more resilient, than a centralized system. The simplicity fosters better understanding, better management, and better control. On balance, the distributed system can hold many advantages, but it does require different approaches to skills, organization, training, personnel development, and project management.

Distributed systems are an exciting and challenging way to improve a business process and assure effective ownership by the users. But their greater design complexity and the unforgiving pressure of the local environment create special problems in terms of project management. Different and stronger skills are needed than might be true in a centralized environment and greater attention must be paid to planning for both the program phases and the people involved and their organization. Central system staffs are not going to fade away in a world of distributed processing; they are going to have to work harder.

## References

[1] Benjamin, R.I. “Information Technology in the 1980’s: A Long Range Planning Scenario,” MIS Quarterly, Volume 6, Number 2, June 1981, pp. 11-31.

[2] Brookes, C.H.P., Phillip J., Grouse, D., Ross J., and Lawrence, M.J. Information System Design, Prentice-Hall of Australia, Sydney, Australia, 1982.

[3] Buchanan, J.R. and Linowes, R.G. "Understanding Distributed Data Processing," Harvard Business Review, Volume 58, Number 4, July-August 1980, pp. 143-153.

[4] Chandler, J.S. "A Multiple Criteria Approach for Evaluating Information Systems," MIS Quarterly, Volume 6, Number 1, March 1982, pp. 61-74.

[5] Enslow, P.H., Jr. "What is a 'Distributed' Data Processing System" in Management Information Systems, 2nd ed., by M.J. Riley (ed.), Holden-Day, Inc., San Francisco, California, 1981.

[6] Ives, B., Olson M.H. and Baroudi, J.J., "The Measurement of User Information Satisfaction," Communications of the ACM, Volume 26, Number 10, October 1983, pp. 785-793.

[7] Kaiser, K.M. and King, W.R., “The Manager-Analyst Interface in Systems Development,” MIS Quarterly, Volume 6, Number 1, March 1982, pp. 49-59

[8] McKeen, J.D. “Successful Development Strategies for Business Applications Systems,” MIS Quarterly, Volume 7, Number 3, September 1983, pp. 47-65.

[9] McLean, E.R. "End Users as Application Developers," MIS Quarterly, Volume 3, Number 4, December 1979, pp. 37-46.

[10] Scherr, A.L. "Distributed Data Processing," IBM Systems Journal, Volume 17, Number 4, November 4, 1978, pp. 324-343.

[11] Withington, F.G. "Coping with Computer Proliferation," Harvard Business Review, Volume 58, Number 3, May-June 1980, pp. 152-164.

## About the Authors

Robert Felix is a Financial Manager at Fletcher-Challenge Ltd. in Auckland, New Zealand. His previous experience includes consulting in the field of computer systems and corporate planning and several years as Manager of Business Systems for the Weyerhaeuser Company.

William Harrison is Associate Professor of Management Science in the College of Business at Oregon State University. His previous work experience includes two years as Director of Administration for Berkeley Computer Corporation and ten years in manufacturing management.
