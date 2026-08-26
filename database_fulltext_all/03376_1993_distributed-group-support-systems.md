---
otero_id: 3376
otero_key: "T7N8C4E2"
title: "Distributed Group Support Systems"
authors: "Murray Turoff; Starr Hiltz"
year: "1993"
journal: "MIS Quarterly"
doi: "10.2307/249585"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Distributed Group Support Systems

By: Murray Turoff
Department of Computer and Information Science
New Jersey Institute of Technology
Newark, New Jersey 07102 U.S.A.

Starr Roxanne Hiltz
Department of Computer and Information Science
New Jersey Institute of Technology
Newark, New Jersey 07102 U.S.A.

Ahmed N. F. Bahgat
Allied Consultants International
Khalifa El-Maamoon St.
Roxy Tower
Heliopolis, Egypt

Ajaz R. Rana
Department of Computer and Information Science
New Jersey Institute of Technology
Newark, New Jersey 07102 U.S.A.

## Abstract

Distributed group support systems are likely to be widely used in the future as a means for dispersed groups of people to work together through computer networks. They combine the characteristics of computer-mediated communication systems with the specialized tools and processes developed in the context of group decision support systems, to provide communications, a group memory, and tools and structures to coordinate the group process and analyze data. These tools and structures can take a wide variety of forms in order to best support computer-mediated interaction for different types of tasks and groups. This article summarizes five case studies of different distributed group support systems developed by the authors and their colleagues over the last decade to support different types of tasks and to accommodate fairly large numbers of participants (tens to hundreds). The case studies are placed within conceptual frameworks that aid in classifying and comparing such systems. The results of the case studies demonstrate that design requirements and the associated research issues for group support systems can be very different in the distributed environment as compared to the decision room approach.

Keywords: Group decision support systems, computer-mediated communications, computerized conferencing

ISRL Categories: HA0301, HA0302, HA0802

## Introduction

In the 1990s, informational networks are predicted to “help far-flung companies and entrepreneurs link up and work together from start to finish” (Business Week, cover). They will operate as “virtual corporations” (Business Week, 1993), formed for a specific project and then dissolved. The computer systems to support these often temporary and rapidly changing, geographically distributed task forces and partnerships will combine characteristics of computer-mediated communication systems (CMCS) and group decision support systems (GDSS) to create “distributed group support systems” (DGSS). Such computer facilities will need to support the full range of tasks involved in projects, including planning, budgeting, gathering information, resolving conflicts, and making decisions.

This article demonstrates the value of adding decision support tools to CMCS for a variety of case studies involving a range of task types. It also provides design and implementation guidelines and identifies research issues for DGSS. This section defines terms and provides historical perspective. The second section presents conceptual frameworks to organize the specific case studies, including a task typology. The third section summarizes five case studies representing five task types. The final section discusses the studies in terms of their implications for applications of and future research on DGSS.

A computer-mediated communication system is the use of the computer to structure, store, process, and distribute human communications (Hiltz and Turoff, 1985; Kerr and Hiltz, 1982). The most common forms are electronic mail, computerized conferencing, and bulletin board systems. A CMCS is frequently used for “asynchronous” text-based communication, meaning that the participants are distributed in time and space. It can also include graphics or digitized voice, as well as real-time (synchronous) exchanges.

A group decision support system (GDSS) is a computer-based “social technology,” the basic purpose of which is “to increase the effectiveness of decision groups by facilitating the interactive sharing and use of information among group members and also between the group and the computer” (Huber, 1984, p.186). It combines communication, computer, and decision support tools and processes to support problem formulation and solution (DeSanctis and Gallupe, 1987). For example, GDSSs include various kinds of voting tools and may support processes similar to “brainstorming,” “Nominal Group Technique,” or “stakeholder analysis.”

GDSS research usually brings people together in “decision rooms.” It is possible, and often desirable, to use these computer-based tools to structure interactions among people across different times and places (see, for example, Dennis, et al., 1988; Johansen, et al., 1991; Pinsonneault and Kraemer, 1990; Rice and Associates, 1984; Turoff and Hiltz, 1982). Figure 1 identifies five environmental contexts within which group support tools can enhance communication and decision making.

Over the last 15 years the New Jersey Institute of Technology (NJIT) has developed, applied, and assessed a variety of decision support software structures that have been incorporated into computer-mediated communication systems. This paper describes some case studies in terms of the group, the task or goal, the nature of the software features, and the outcomes. All of the case studies involved “real” groups of people with real problems. The systems were designed to support both these specific groups as well as other groups that might perform similar tasks in the future. In establishing this research program, we assumed that:

1. Prior GDSS research had focused on providing communication and decision support primarily for small groups meeting at the same time and in the same place (face-to-face synchronous meetings).

2. Prior CMCS research had focused on different time or place environments, where communication support is provided principally to large groups.

3. Both GDSS and CMCS are moving toward providing any time/any place systems with both communication and decision support for any size group.

A group support system is fundamentally a communication and coordination process that has strong roots in techniques for structuring group communication such as the Delphi method (Linstone and Turoff, 1975), “inquiry systems” (Churchman, 1971), and Nominal Group Techniques (Van de Ven and Delbecq, 1971). A DGSS can provide at least five distinct levels or types of communication support:

1. Alternative communication channels for the group. This permits a group to work more efficiently and/or more effectively with shared text, structured data, and graphics.

2. Process structuring for communication protocols and human roles. This includes the improvement of the group process by addressing such concerns as: (a) Software support for a leadership or facilitation role (e.g., special powers or privileges); (b) Participation equality (e.g., requiring inputs from each participant); (c) Encouraging free exchange of ideas and opinions (e.g., anonymity and Delphi techniques); and (d) Voting protocols to elicit the group's preference structure (e.g., one vote for preferred option, rating of each alternative, rank ordering of alternatives).

![](/api/attachments/T7N8C4E2/fulltext/images/7c3dba9d29a48d3c1d171d10062f4cf8dd524d48611455337816a4e2e99f334b.jpg)  
Figure 1. Modes of Group Support Systems (Adapted from Johansen, et al., 1991)

3. Support for data collection, organization, filtering, formatting, feedback, and retrieval. This includes any and all material (text, data, graphics) generated or required by the group to support its deliberations.

4. Availability of sophisticated decision aids in support of the group process (e.g., structural modeling, scaling methods, games and simulations, and statistical analysis and forecasting). These techniques are available for use because of the existence of a computer system as a participant in the communication process.

5. Synchronization of the communication process (e.g., who has read what, who has voted, when has a reasonable consensus been reached, when is there a new alternative to consider, where disagreement exists, when to open or close an activity in the problem-solving process, etc.). These are crucial for replacing the usual cues about the state of the group process that are available in the face-to-face synchronous environment.

Attempts to understand the computer-supported group process have tended to rely on face-to-face groups. However, in a DGSS, each participant can act as an individual problem solver and concentrate his or her attention on specific aspects of the problem. This requires that both individual and group problem solving processes and how they become coordinated in the asynchronous, distributed environment be considered. The designer must create appropriate communication structures and protocols that will bring the individual problem-solving process into synchronization with the group process, without restricting the individual's freedom to concentrate on aspects of the problem to which he or she can best contribute.

DGSS designs also need to make some provision for “group memory,” the ability to store the material generated in one session or phase for use in another (Valacich, et al., 1989). This has also been referred to as organizational, collaborative, or community memory (Hiltz and Turoff, 1978/1993).

Finally, group support software should employ one integrated system rather than many different systems to carry out a decision-making and implementation process. Participants are not likely to be satisfied with systems that require one set of technologies and procedures when they are working as dispersed individuals contributing to a group, and another when the group interacts simultaneously. Nor will users tolerate having to use different systems in different locations.

## Conceptual Frameworks

Conceptual frameworks help to organize case studies and point to their possible relevance for other specific examples of groups using DGSS.

Three categories of contingencies for the effects of GDSS have been proposed (DeSanctis and Gallupe, 1987). The first is communication condition or mode (Face-to-face or dispersed, as illustrated in Figure 1). The second dimension is group size. Whereas most studies, with the exception of those carried out in Arizona's large decision room (Dennis, et al., 1988), are with small groups, our field studies focus on larger groups using the system over a considerable period of time, rather than one or two short sessions.

The third dimension is task type. No existing classification scheme is, at the same time, mutually exclusive, comprehensive, theoretically logical, and concise enough to be useful for organizing and comparing research settings. However, by building upon earlier classifications by many group dynamics researchers, McGrath (1984) developed a typology that provides an initial step toward a task classification that satisfies these criteria. It distinguishes four categories of major activities or objectives, each with two subcategories of task types

## A. Generate

1. Planning tasks: Generating action-oriented plans.

2. Creativity tasks: Generating ideas (e.g., brainstorming).

## B. Choose

3. Intellective tasks: Solving problems that have correct or optimal answers.

4. Preference or decision making: Tasks for which the preferred or agreed-upon answer is the correct one and developing consensus is the goal.

## C. Negotiate

5. Cognitive conflict: Resolution of conflicting viewpoints, preference structures, or interpretation of information.

6. Mixed-motive: Resolving conflicts of motive/interest (e.g., bargaining, coalition formation).

D. Execute (carry out actions). These types of tasks are usually not included within the sphere of group decision support because they are “post-decision.”

Our purpose was to understand what happens when appropriate tools and communication structures to support each of these types of tasks are incorporated into a CMCS. The examples of distributed support systems discussed in this article span five of the six relevant task types listed above. A crisis management system called EMISARI was developed for a planning-type task. State legislative advisors and scientific experts used a “TOPICS Exchange” on intellective tasks (seeking scientific information that could improve laws related to technology regulation). A standards-setting group developed and used special support systems called TERMS and CHIPCHECK for their preference-type task. The use of hypertext structures within CMCS seems to have benefited groups involved in cognitive conflict tasks. A zero-based budgeting support system was constructed for a “mixed-motive”-type task. Each of these is described in this article.

Among the groups studied, none sought specific decision support software for asynchronous creativity tasks, but examples have occurred with the common forms of computer conferencing. Usually, anonymity or pseudonymity are significant tools for creative tasks.

In each of the five cases, the user group started with a task it needed to accomplish through asynchronous computer-mediated communication. The software was designed and implemented to support the type of task, not the specific problem instance. Each of the case studies is described briefly in this paper.

To understand the differences in the design of these distributed systems, it is useful to consider how they can coordinate the group activity. This is a second conceptual framework for the case studies. The “Summary and Discussion” section returns to this issue of coordination modes and summarizes the classification of the case studies on this dimension.

Our classification of coordination methods that groups use is derived from earlier classification of how organizational units coordinate their activity (Thompson, 1967). As adapted to DGSS, the four major coordination modes are:

1. Parallel: Each individual approaches the problem independently of the other members of the group.

2. Pooled: Same as parallel except that a structure or standard is utilized to formulate a group result (e.g., voting).

3. Sequential: The group imposes phases on the problem-solving process that must be undertaken in a sequential manner by all the members of the group (e.g., a step-by-step agenda).

4. Reciprocal: Changes made in one part of the problem by individuals can force reconsideration of other parts of the problem (e.g., consistency relations are imposed).

In the synchronous environment, the group usually relies on a self-imposed sequential strategy for the various segments of the problem. That is, an agenda is adopted, and the group systematically finishes one step or stage before moving on to consider the next task in the sequence. In the distributed environment, individuals have more freedom to work independently on different problem segments at the same time. It is therefore crucial that the computer system provide the tools and structure necessary for synchronization of the resulting group activity (Johnson-Lenz and Johnson-Lenz, 1991). This may range from simply providing information on what each individual has accomplished (i.e., parallel coordination), to forcing individuals to reconsider earlier activities of other members (i.e., reciprocal coordination).

The distinguishing aspects of this set of categories for group processes is further clarified in Table 1. Is there an imposed group view rather than the individual views of each member? Are the participants asynchronous or synchronous (face-to-face)? How does the effort of each individual influence the group results? Cumulative means that each individual's contribution can be a unique contribution (e.g., each person writing part of a report), and the result is usually the product of a unique problem-solving strategy. A synchronized result means that an individual contribution can force other individuals to rework their prior contributions as an explicit part of the strategy.

## Examples of Distributed Group Support Systems

This section describes a variety of DGSS tools that have been designed by the authors and their colleagues to enhance extended use of CMCS in an asynchronous mode. With the exception of the first system described below (EMISARI), the tools were created within the electronic information exchange system (EIES), and its successor, EIES 2.

EIES was put into operation at NJIT in 1976 and has served as both an R&D platform and a prototyping environment since then. The original EIES, which operated until 1991, used a single dedicated minicomputer and was a completely centralized system. EIES 2, in operation since 1990, is a full-screen mode and an object-oriented, fully distributed system that can operate over a network of computers. EIES and EIES 2 have been commercially available and accessible worldwide, and have served as “laboratories without walls.” For most of the case studies described below, the subjects consisted of user groups who were paying subscribers, who brought a task they needed to accomplish, and who had a budget for software additions to fit their needs. Both systems include a language for prototyping special communication structures and computer support and thus support an iterative process of design, application, and assessment of tools and processes for a distributed environment. (For more technical information on the systems, see Turoff, 1991; Turoff, et al., 1989.)

## EMISARI (emergency management information system and reference index)

## Group and Task

EMISARI was developed at the Office of Emergency Preparedness in the Executive Offices of the U. S. president in 1971 (Wilcox and Kupperman, 1972) to support planning and decision making during declared national emergencies. It supported messaging, conferencing, and data reporting in crisis management situations. First developed during the Wage-Price-Freeze as a crisis MIS, for over a decade it was used for a variety of declared federal crisis situations such as oil shortages and major strikes.

Table 1. Coordination Alternatives

<table><tr><td>Coordination Method</td><td>Group View</td><td>Individual Inputs</td><td>Group Results</td></tr><tr><td>Parallel Information Exchange</td><td>None imposed</td><td>Asynchronous</td><td>Summation</td></tr><tr><td>Pooled</td><td>Imposed</td><td>Asynchronous</td><td>Cumulative</td></tr><tr><td>Sequential</td><td>Imposed</td><td>Synchronized</td><td>Cumulative (usually)</td></tr><tr><td>Reciprocal</td><td>Imposed</td><td>Asynchronous</td><td>Synchronized</td></tr></table>

## Software Features

EMISARI gave 100-200 people scattered around the country the ability to track, interpret, and reorganize both qualitative and quantitative information associated with a rapidly changing and unpredictable situation, and to coordinate their actions. It had many significant features for collaborative group decision processes that have not yet appeared in any commercial system. The following are among the features that relate to DGSS:

\- The system monitor (a human role with software support) could establish a variety of data forms and then assign participants with the responsibility to fill in specific fields. The resulting database identified the individuals who provided the information and the date of updates.

\- People could append messages to the “data.” Anyone accessing the data could retrieve the associated discussion or contribute to it. Typically, comments interpreted the meaning of the data or its reliability.

\- One type of data table was a time-series collection that calculated a regression extrapolation each time a new entry was made and flagged values outside of prior expected predictions.

\- Public notebooks (bulletin boards) had separate membership roles for those entering data and those able to retrieve data. These were utilized for such purposes as announcing new policies and interpretations of policy. Tracking of key words searched in these notebooks determined what people were looking for but could not find. This information was then provided to the policy committees to aid in scheduling their deliberations.

\- Another specialized tracking data format facility enabled people to establish the sequence of steps a “case” would go through and who was responsible for determining the outcome of each step in the process. A case was typically a potential violation of a policy by an organization or a crisis-related incident requiring federal involvement. As steps were completed, the system alerted those involved in the next step to take over responsibility for the case.

\- A simplified integrated interface to a multi-regional input-output database allowed people to receive projections of the impacts of changes in industrial output in their area on related industries.

\- A directory showed who was responsible for what functions within the system (e.g., reporting particular entries in a table).

EMISARI was intended for a crisis environment. Therefore, the system monitor could make quick changes to any of the data formats and assigned responsibilities. It allowed participants to organize themselves into subgroups. In a crisis situation, it is impossible to predict the optimal composition of a group required to effectively address a particular issue, problem, or case. EMISARI provided all the necessary tracking and feedback communication structures to allow very large groups to exchange rapidly changing information in a very dynamic environment.

Approximately one-third of the software in EMISARI was devoted to supporting tools for specialized human roles (such as the system monitor and forms manager) that were an integral part of the design. Specific software support for human roles has been a common feature of computerized conferencing systems since that time.

The mode of coordination supported by these software features is “parallel” according to our classification. Everyone worked independently for the most part. The system merely served as a sophisticated means to keep everyone informed of policy decisions from the White House, what was happening in all the locations, and what actions each member of the crisis management team was taking.

## Results and Discussion

Though this system has been classified as supporting a “planning”-type task, it should be noted that it coordinated not only the policy making and planning, but also the monitoring of the execution of these policies and plans. In most cases of “real problems” in “real organizations,” a group’s complete task will combine two or more of McGrath’s (1984) task types.

There was no formal evaluation of EMISARI; in the crisis management environment, research is bypassed in favor of the heuristic of using whatever seems to work. The fact that the system continued to evolve and be used in crisis management for over a decade indicates that it was considered a “success” by the White House.

EMISARI demonstrates that attempts to limit the realm of GDSS to real-time systems are artificially restrictive. In a crisis, people adjust to the situation they are dealing with, and not to scheduled group meetings. Moreover, even though companies may not often face major crisis situations (e.g., oil spills, strikes, takeover bids, bombings, massive law suits), there are many situations (e.g., proposal bidding, product development delays, supply shortages, competitive announcements, cost overruns) that produce similar behavior and needs.

EMISARI provided the flexibility required for a variety of crisis monitoring and planning situations. It accomplished this by dealing with human roles, communication protocols and structures, data structures, and text item types and status. Nothing was built in that dealt with the content or specifics of a particular problem. While specific databases and models can be created around specific decision problems, group communication structures should focus on general classes of problems. This is counter to early decision support systems, where the tools were often structured for a given decision maker and his or her specific problem.

In a decision room GDSS, roles and communication protocols are left to the group process and to the skill of the trained moderator or facilitator. In systems like EMISARI and others described in this article, these aspects must be explicitly defined in the design of the system. Furthermore, large groups interacting over an extended period of time can generate a very large database. A three-month crisis activity using EMISARI could generate tens of thousands of items. This mandates careful attention to information organization and retrieval and requires further research. The design challenge is a function of group size, and very few examples of group support systems exist for working groups composed of hundreds of people.

## TOPICS for information exchange in large groups

## Group and Task

TOPICS was designed to support state legislative science advisors assigned to providing scientific information in a timely manner as input for prospective or pending legislation. $^{1}$ The purpose was to gather and evaluate the correctness of all available scientific and technical information so that legislators would reach correct conclusions about “the facts.” Thus, it has been classified as an intellective task. The initial TOPICS exchange was called “Legitech”; subsequently, the software underwent considerable evolution to support a more general information exchange function (Johnson-Lenz and Johnson-Lenz, 1980; 1981).

The TOPICS software supported information exchange, evaluation, and consolidation among a large group of experts. The approximately 80 participants in the original Legitech exchange included about 25 state legislative science advisors and 25 experts from scientific societies and government research laboratories. Participants needed to be able to obtain, accumulate, and organize relevant scientific information in a way that would not cause “information overload.” Topics could be as unpredictable as the weather and politics. If it happened to be a drought year, participants might need to know about farm subsidies, and if there were a big oil spill, they might need to know about environmental damage control.

## Software Features

Through work with the users, the following concepts and software structures evolved:

\- An INQUIRY was a pointed question, limited to three lines. All participants received the full text of all new inquiries. There were approximately 20 inquiries generated every week.

\- A RESPONSE could be entered to any inquiry by any member of the TOPICS exchange. Responses were to provide an answer or a lead to people or documents that had answers, or give an opinion or evaluation of a prior response. The first response usually was entered by the author of the inquiry, providing extensive background information and expansion on the question posed in the inquiry. Responses could be up to 300 lines long.

\- A user's SELECTIONS was the list of inquiry topics he or she was interested in and wished to follow over time. As each new inquiry was delivered, the user was asked whether that topic should be added to his or her selection list. On selecting an inquiry, the user would receive all prior responses and those subsequently entered in the future. Users could remove themselves from selected topics or add themselves to topics not initially selected.

\- An alphabetic Index of TOPICS provided rapid search and retrieval of topics by keyword.

When no more new responses were being added to a topic, a human editor created an "Inquiry-

Response Brief" and put the completed topic in a separate database. These Briefs were also made available by mail to offline participants.

Evolutionary changes made to TOPICS encouraged a social structure for the group that motivated and regulated participation. Initially, many people wanted to make inquiries and receive responses, but few took the time to respond to others. Software was added to automatically track how many responses were received and how many inquiries were made by each member. Members could see this scorecard, and billing procedures were implemented that gave credits for items contributed and debits for items received or inquiries made. Another enhancement was a “tallies” feature, an ongoing straw vote that could be attached to any topic. “Tallies” was a concise way of capturing disagreement among experts. Another feature added was “party,” software to support real-time sociable interchanges among members. Because the group was composed of individuals in different organizations, sociability was felt to contribute to the trust necessary for the free exchange of sensitive and controversial information.

TOPICS evolved from the active involvement of users in design discussions at all phases, from the first planning through the testing of prototypes to the construction of “wish lists” for the next release. The implementors (Johnson-Lenz and Johnson-Lenz, 1981) described this evolutionary process:

For a structure to be effective, it must meet the needs of the group using it. However, the perceived needs of a group may (and probably will) change over time. This means that as a group's needs change, either as it learns more about the medium or as its situation changes, the communications structure must evolve to match those needs (p.1).

## Results and Discussion

TOPICS proved to be a general purpose structure that could be used by other large groups engaged in information exchange. For example, the “growth topics exchange” supported the sharing of problems and solutions among a network of a half-dozen communities in the southwestern United States undergoing rapid growth. This group, which was smaller (about 30 participants), chose a different balance between information overload and the ambiguity that could be created by extreme conciseness. The group set the maximum length for inquiries to be five lines instead of three. (The software had been designed with length limits that could be changed at any time.)

TOPICS demonstrates the need to increase structure as a function of the size of the group. Twenty or so individuals can do “unpredictable information exchange” in an ordinary conference. However, when one is attempting it with a hundred or more individuals in one group, an expandable structure such as that provided by TOPICS becomes a necessity to avoid information overload.

## Standards setting: TERMS and CHIPCHECK

## Group and Task

The Joint Electron Device Engineering Council (JEDEC), under the aegis of the Electronic Industries Association, used EIES from 1978 to 1980 for “selected aspects of its work of promoting hardware and software standardization in microcomputer/large scale integration products” (Johnson-Lenz, et al., 1980). A total of 77 invited participants belonged to several standards committees with partially overlapping memberships. JEDEC’s standardization activities had been previously conducted only through quarterly face-to-face meetings, with additional communication via phone and mail. The standards under development required the unanimous approval of the members, i.e., the group had to first reach agreement on a set of terms and definitions that apply to a given standardization topic and then agree on the preferred set of standards to guide future product development. Because there was no “correct” answer as to what standards should be set, and the mission of the group was to reach consensus, the task was classified as a preference task.

## Software Features

A structured decision aid, TERMS, was programmed to support the process of developing and reaching agreement on such a standard set of terms and definitions. TERMS allowed any member to:

\- Add a proposed term;

\- Add a proposed definition or alternative definition to those made by others;

• Make a comment about a term or definition;

\- Vote on each proposed term and definition;

\- Revote at any time, based upon current votes and new alternatives.

Straw votes could be entered anonymously, and tallies of all votes on all proposed definitions were always available to members. The set of items contained in the TERMS subsystem for any specific standards effort was called a glossary and was maintained as a separately organized database, associated with the group's conference. The TERMS system was designed with the participation of interested project members.

In addition, the leader of one of the groups developed a decision support aid for his committee's work on memory chip carrier standardization. Called CHIPCHECK, it was used in evaluating various proposed memory chip carrier configurations. This routine recorded anonymous data only, since a possible configuration associated with a specific manufacturer might give away product development plans. The routine loaded a set of design rules based on multilayer package structures. The user then entered parameters for specific possible package design options. CHIPCHECK calculated and evaluated the parameters in light of the ground rules. All users could see the diagrams and different sets of parameters proposed and their evaluation against these common rules.

## Results and Discussion

During a final evaluation interview, those who had participated in any of the activities on EIES were asked how using the system affected the quality of decisions, the amount of information available, the speed of decision making, the amount of discussion, and the amount of participation. The following were among the commonly reported advantages of the system. It:

1. Accelerates exchange of ideas and opinions, thus speeding up the standards process;

2. Improves the quality of decisions;

3. Increases the amount of information available for decisions;

4. Makes for better, more effective face-to-face meetings;

5. Improves continuity between meetings;

6. Increases the amount of discussion.

It was felt, in contrast with face-to-face meetings, that fewer people participated more. In other words, there was intensive participation by a subgroup within the committees (Johnson-Lenz and Johnson-Lenz, 1981).

One of the important aspects of this application was the ability to make votes and anonymous or pen name comments. $^{2}$ This helped considerably in overcoming the concern of some members about giving away leads regarding R&D developments in the companies they were representing. While JEDEC committees were “collaborative” groups, they were not necessarily “cooperative” ones with respect to all the group objectives.

The JEDEC standardization project did encounter problems. For instance, only 58 of the invited 77 members ever signed online and participated; when asked why, the most frequent reason given by non-participants was “lack of time.” A major perceived shortcoming was the lack of any graphics except those that could be generated using the keys on the keyboard.

A large number of similar applications have occurred in the medical field. Twelve world-renowned researchers of hepatitis sought to arrive at an updated knowledge base for practitioners by requiring unanimous agreement on wordings taken from the research literature (Bernstein, et al., 1980). This group was examining all the recent research literature and regularly collaborating to reach agreement via computerized conferencing.

It is interesting to note that the TERMS software was also used in a counter-culture group devoted to discussing transformational experiences. The sorts of terms for which members of the group contributed definitions were “vision” and “love.” A well-designed group communication structure can serve a wide variety of specific applications within the same task type.

## A distributed system for zero-based budgeting

No decision activity in organizations is more common and pervasive at all management and professional levels than the allocation of resources through budgets. The achievement of every functional objective in the organization, as well as the personal success of every manager, depends on obtaining sufficient funds and resources to carry out plans. Because power and prestige are related to budget share, negotiations over this issue are a prototypical “mixed motive” task that involves conflicts of interest.

The most popular form of budgeting is the “line-item process” that starts with the prior budget and extrapolates trends. Particularly for organizations operating in a changing environment, and for new or “virtual” organizations, this process would not be satisfactory. One suggested budgeting alternative is zero-based budgeting (ZBB). ZBB starts every department at “zero” and requires that its budget be constructed based on its goals and programs and what is necessary to support them. The objective of ZBB is to involve managers at every level in making comparative judgments on the planned budgets (Pyhrr, 1970).

ZBB imposes a very large burden of added communication as managers review one another's projects, discuss them on a relative basis, and arrive at a group consensus on their relative importance to the organization. This burden can cut short its use or nullify its benefits (Wildavsky and Hammond, 1965). The premise of this case study, which was a Ph.D. dissertation (Bahgat, 1986), $^{3}$ was that an asynchronous communication process would make it feasible for decision makers to carry out the extensive iterative communications necessary for ZBB to have favorable outcomes.

## Group and Task

The case study was focused on a \$1.5 million equipment budget allocation for NJIT's 1987 fiscal year. The ZBB committee consisted of 28 individuals including deans, department chairpersons, research center directors, service unit directors, and the vice president for Academic Affairs.

It is quite common to discount case studies performed on captive subjects in university settings. However, given the autonomy of university departments run by tenured faculty, who generally have to be persuaded rather than ordered to do anything, there are many reasons why this can be considered a conservative and valid test of the feasibility of such a system. First, the funds at stake were the only source of money to support acquisition of equipment or other variable needs; the rest of the budget was allocated to fixed expenses. There were many more claimants than funds available. Second, organizational politics swirled around the imposition of the ZBB conferencing system, just as it would in any organization. For example, three units of the university totally boycotted any participation in the process for the first three months of the eight-month budget cycle. Their opposition to a new way of allocating capital funds was emotionally highly charged and expressed at all levels. Only after it was clear that the effort was moving ahead successfully, and the VP announced that no new equipment money would be given to any department that did not participate, did those three units join in the effort.

## Software Features

To create ZBB support software, a standard conference facility on EIES was augmented with a collaborative database of “decision packages” that users could fill in and update at any time. A decision package was a proposal that described requested items and the cost to support a new project or meaningfully expand or improve an existing project, including capital investment costs, yearly maintenance costs, technical staff, personnel development time, personnel operational time, and floor space requirements.

Among the special features added to facilitate the ZBB process were:

\- A ranking facility that allowed any participant to rank all the packages and, separately, just the packages in their unit. Members could modify their rankings at any time.

\- Standard summary reports that allowed anyone to see the detailed analyses at any time, including rankings and dollar amounts.

\- Change tracking that alerted members when a package or a rank order had been modified.

In addition, the standard conference facility on EIES existed for free discussion about the nature and merits of decision packages. At any point in time, any organizational unit could decide to make changes to its budget packages and thereby require a re-ranking by the other members. In that sense, it is one of the few examples of a fully “reciprocal” GDSS—the action of one group member sets off a polling of all members because of the change in the data recognized by the software tools. There was no human leadership to sequence the process and only a due date by which the final results had to be produced; the software features coordinated the group.

## Results and Discussion

The trial was instrumented with pre- and post-surveys, interviews, activity monitoring, and analyses of the discussion and behavioral patterns of those involved. This paper includes only an interpretive summary of selected findings.

During the eight months of the process, there was an initial face-to-face meeting to explain the system to be used. The remainder of the process took place online.

Positive outcomes were perceived by the vast majority of the participants. Over 90 percent felt that the information provided in the decision packages was useful. Over 73 percent believed that the process was desirable, and approximately 60 percent found the online process enjoyable and believed it improved the accuracy of the process.

Measures of mutual awareness and interrelationships among projects increased significantly between pre- and post-test. Furthermore, a great deal of communication occurred that consisted of individuals helping others to improve the estimates and specifications in their packages. There was also a strong correlation between the degree of participation in the communication process and the perceived benefits.

Responses on the post-process surveys and interviews indicated that the system reduced information overload and decreased the amount of communication time compared to the usual approach to ZBB. It also increased considerably the lateral exchange of information about capital investments. And there was considerable refinement of budget packages, negotiation between units, and new packages that cut across units for shared laboratories.

But a number of shortcomings were identified. The ranking of all decision packages on one dimension was found to be extremely difficult for most participants. There was general agreement that packages needed to be separately ranked for major missions such as research or education. Also, many people felt uncomfortable with ranking very large investment projects along with very small ones. A revised design would enable the group to develop separate dimensions along which the ranking procedure could be carried out.

This case study is highly significant because it is a clear-cut demonstration of a CMCS functioning as a DGSS, and the outcomes run counter to conventional management wisdom on the zero-based budgeting approach. While ZBB has largely been abandoned because of the communication demands when synchronous meetings are used, the use of an asynchronous group support system makes the approach feasible. Furthermore, it further demonstrates that implementing a process in a CMCS environment produces results and behavioral patterns different from those produced by the same process in a face-to-face environment.

## Hypertext: TOURS and QUESTION

In cognitive conflict tasks, there are several stages involved, including gathering and organizing all available information, making connections among different “pieces” of data, and then arriving at a collective understanding and evaluation of the issue. We have observed that tools that incorporate aspects of hypertext appear to be very useful in supporting such group efforts in arriving at a shared cognitive mapping of an area of knowledge.

Two examples of the use of hypertext tools embedded in a CMCS to support distributed group decision making provide the final examples in this section. Neither of these is as full a “case study” as the previous ones. Thus, the organization of this example of structures for DGSS is somewhat different than in the previous examples. First, some background is provided on what is meant by hypertext tools.

Among the fundamental elements of hypertext (Bieber and Kimbrough, 1992; Nelson, 1965) are the establishment of linkages among text fragments, the conditional handling of the linkages among fragments, and the idea that the fragments may be active programs rather than just passive pieces of text. In incorporating hypertext capabilities into CMCS, some additional elements come into play. The privilege of constructing new fragments and establishing linkages among them may be made dependent upon assigned roles within a group of people who have access to the collection of items. The items, whether text or programs, may ask questions of the readers and then incorporate the responses as changes in the original items. The content thus constantly changes and grows as a result of actions by members of a group who share access to the hypertext entity.

## TOURS: Group and Task

Developed by Peter and Trudy Johnson-Lenz (1982), TOURS enabled participants to explore and develop a range of alternative conditions and plans. The application was initially designed for government managers developing a long-term plan for the national forests. The system was intended to broaden their outlook and extend their planning horizon by enabling them to explore a number of scenarios and alternatives, and to try to reach agreement on their preference structure. Thus, it is an example of a “cognitive conflict” type of task.

## Software Features

TOURS allowed a complete network of “text items” but had some very unusual and interesting features not found in most other early examples of hypertext. The system utilized a metaphor of a “tour of the future,” in which the major nodes were called “stops.” A hypertext node in this system had a number of parts:

\- A text scenario about a particular aspect of the overall planning problem.

• A set of votable issues.

\- A set of comments made by everyone who stopped at this node during travels through the network.

\- Voting scales appropriate to the content of the node.

An artificial persona, a guide named Joan, presented possible stops that the “travelers” could make based upon where they had been, the factors the travelers were rating, and the conditions set up by the creator or “weaver” of the original network. The underlying tour network could be structured by the “weaver” to encourage divergence or convergence of views. At one extreme, the structure started travelers at a very specific focused position, and the network fanned out into many related topics. Alternatively, TOURS could be structured to guide users to a very focused decision-oriented issue after starting from diverse, loosely coupled aspects of the overall problem.

TOURS illustrates that the linking of items in a hypertext system is not a discrete binary choice (i.e., a link exists or it does not). The nature of a link can be “fuzzy” and the existence of a link can be influenced by both content variables and actions of the users on an individual and a group basis. For example, both the voting process and retrieval behavior (frequency of choice of “stops” by the other travelers) dynamically influenced the guidance process for exploring the resulting web. In this case, the probability that the link exists for a given user is determined by the above factors. Therefore, a qualified individual must establish the starting content of a tour and parameters of the network.

## TOURS Results

There is no published data on how well the strategic planning objective of the TOURS system was accomplished. TOURS was also utilized in an educational and recreational mode on EIES for a period, and positive impacts on students were observed. It appeared to increase their ability to deal with complex problems and to enjoy the associated learning process. Users continued to choose to enter the TOURS sub-system and to “travel” through the nodes until the EIES1 machine was turned off eight years later.

## QUESTION/Response Activities in the Virtual Classroom

TOURS led to a number of features for educational and training applications. QUESTION is such a feature, developed initially for the “Virtual Classroom”™ (Hiltz, 1986; 1993). This is an environment intended for collaborative learning within CMCS. It has been used by students and instructors in many courses, over the last seven years.

QUESTION utilizes a comment to pose a question and to provide answers that are attached to the question by a conditional link. Conference members are prevented from seeing the answers that have been generated as linked replies until they first supply an answer. This means that every student in the class is forced to think through and develop an answer. While this feature sounds like the question process used in a face-to-face class, in that environment the first few students to answer usually close out the participation by the rest of the class.

The QUESTION tool serves to illustrate a conditional structure for the delivery of new material to participants in a group. This same feature may be utilized to promote brainstorming and creativity in a group discussion. Most faculty members who have used the Virtual Classroom software tools have felt that this feature is one of the reasons why the Virtual Classroom has proven more effective in some ways than the face-to-face classroom. A similar structure may be used in any group process to encourage each member to develop ideas independent of the other members of the group.

## Hypertext Discussion

One problem with group hypertext, in which members can create and modify both nodes and links, is that users tend to be careless about observing and following the overall structure. They frequently make inappropriate links and ignore the use of keywords that can help others to see an overview of the total structure. Thus, a human moderator must have the power to “move” or change links, nodes, and keywords, in order to keep the hypertext organized.

Most current hypertext systems are highly tailored for specific applications, using a specific metaphor and a unique set of link types. Users will not be able to remember how to navigate completely different systems for every application. The future for hypertext thus lies in devising more powerful generalized theoretical models of the cognitive relationships that people use and raising the semantic level of tailoring linkages to the user and group level (Rao and Turoff, 1990).

In summary, a DGSS requires and can offer much more sophisticated and flexible software functionalities than those required to support face-to-face meetings, where limited training time is a serious limitation on functionality. Most GDSSs provide some specific forms of hypertext linking structure (e.g., criteria linked to the alternatives they evaluate). Thus, we believe that development of group hypertext features should be a priority research issue for the design of database support tools for DGSS.

## Summary and Discussion

Our case studies provide support for the DeSanctis and Gallupe (1987) premise that the nature of computer-based group support tools and structures that will be helpful is contingent on task type, communication mode, and group size. The cases presented in this article are data points chosen from dozens of groups that have used the systems over the years. They are all examples of “distributed” groups (different places/different times for interaction). They are also all fairly large groups; in our experience, groups of less than 10 usually do not fare well in the distributed environment; and if they do, they tend to manage with only a human moderator or leader in a discussion-oriented computer conference, and without any special decision support tools. Only “successful” applications were chosen where success is defined as use over a relatively long period of time. Roughly half of the groups that have made some attempt at using EIES systems have not been successful according to this criterion. (See Hiltz, 1984, and Hiltz and Johnson, 1989, for some comparisons of more and less successful online groups.) Each of these user groups participated to some extent in the development of special software tools to support their task. Thus, these are “naturally evolved” tools for the different task types that we chose to re-examine and compare. It is very likely that many different types of tools and processes than those evolved by the specific groups described would also have contributed to group success. However, it is also noteworthy that different types of tools did emerge to support the different task types represented.

There is much to learn about which tools and structures will be most helpful to provide coordination in the distributed mode, under various conditions. These “conditions” or contingencies are more complex than the three originally identified by DeSanctis and Gallupe (1987). In order to understand the range of contingencies along which to classify case studies of DGSS, some additional conceptual frameworks are presented.

Decision tasks are often characterized as being structured, semi-structured, unstructured, or wicked. Daft and Lengel (1986) make the useful distinction between uncertainty and equivocality. Uncertainty means a lack of information. Equivocality means ambiguity—the existence of multiple and conflicting interpretations about an organizational situation. The more unstructured the group task, the higher the “equivocality” of the needed information. Participants are not certain about what questions to ask, and if questions are posed, the situation is ill-defined to the point where a clear answer will not be forthcoming.

Distributed group support systems can be very suitable for problems involving ambiguity. For example, while the estimates of a proposed budget for a new project may be uncertain, any situation where the objective rationales for new projects are differently perceived in an organization or group is a situation of equivocal or ambiguous information. According to Daft and Lengel (1986):

Rich media facilitate equivocality reduction by enabling managers to overcome different frames of reference and by providing the capacity to process complex, subjective messages. Media of low richness process fewer cues and restrict feedback, and are less appropriate for resolving equivocal issues (p. 560).

Face-to-face meetings are a rich medium, while information systems and internal memos are not (Daft and Lengel, 1986). Obviously, if DGSSs are to play an important role in organizational communication, they must support “equivocality reduction.” On the basis of our work thus far, it appears that communication and decision support functions that allow group members to generate and process “complex subjective messages” can indeed be provided in the CMCS environment.

All the systems discussed in this paper were designed to handle situations with high equivocality of information. They do this successfully for a number of reasons:

\- They integrate free text discussion with computer-based data structures appropriate to the class of task, rather than the content of the task.

\- At least some of the participants were able to adapt to new writing styles that include paralinguistic cues (cues within text) that substitute for the non-verbal cues that convey emotion. (Such paralinguistic cues included using capitalization, punctuation, formatting, and slang to set off ideas and show emotion.)

\- The design of discussion-aid structures focuses not on the content of the decision as in classical DSS, but on the communication process and protocols.

\- The element of self-activation of participation by members in the group activity is desirable for encouraging reflective thinking about the task.

Three factor dimensions that are fundamental for examining the asynchronous GDSS environment are the degree of complexity of a task; the approach by which individuals and/or a group determines what is a “valid” result in examination of a problem; and the mode of coordination. The first dimension (task complexity) is based upon the classical DSS work on “problem structure” (Keen and Scott Morton, 1978; Scott Morton, 1971; Simon, 1960).

In the second section of this paper, four modes of coordination of group interaction were described. The right hand column of Table 2 reviews the classification of the systems mentioned in this paper according to this criterion. We have previously mentioned that EMISARI features facilitated “parallel” interaction and that the ZBB budgeting case included forms and algorithms that provided a “reciprocal” form of coordination. The other three cases are all examples of “pooled” coordination modes; another example of this mode would be iterative polling or voting tools.

Another key aspect of group problem solving is the approach whereby a group evaluates the validity of information about the task at hand: What is the nature of truth for the group process? A modified version of Churchman's (1971) inquiry system (Turoff and Rana, 1993), together with the dimensions of complexity and coordination, classifies the studies discussed in Table 2.

The concept of validation of the process for examination of a task comes from the philosophical foundations on the nature of “truth.” The categories of this dimension are taken from the work by Churchman (1971) and Merleau-Ponty and Heidegger (Kant, 1967). They are:

1. Deductive: A logical process or deductive procedure can be utilized to express truth.

2. Inductive: Agreement or consensus on interpretation of the data is the process whereby a group arrives at a truth.

3. Relative: It is assumed that there is no optimum or single truth to emerge. Truth must be found by comparing alternatives and picking the best.

4. Negotiated: A group "negotiates" what is to be considered true. Truth does not have to be tied to any external realities or observations.

5. Conflictual: Truth can only be derived from the strongest possible conflict between alternatives.

Together, these three dimensions appear to allow us to cover the scope of problem-solving situations in real organizations and the processes that groups use over prolonged periods of time. Most importantly, they provide a framework for considering the types of structures and tools that can be incorporated into a GDSS to support real-world group problem solving. They are drawn from prior sources dealing with both information systems and organizational behavior.

Table 2. Classification of Systems

<table><tr><td>System</td><td>Validation</td><td>Complexity</td><td>Coordination</td></tr><tr><td>EMISARI</td><td>Inductive</td><td>Unstructured</td><td>Parallel</td></tr><tr><td>TOPICS</td><td>Inductive</td><td>Semi-Structured</td><td>Pooled</td></tr><tr><td>TERMS</td><td>Relative</td><td>Semi-Structured</td><td>Pooled</td></tr><tr><td>TOURS</td><td>Negotiated</td><td>Semi-Structured</td><td>Pooled</td></tr><tr><td>CMC ZBB</td><td>Conflictual</td><td>Semi-Structured</td><td>Reciprocal</td></tr><tr><td>Decision Room GDSS</td><td>Inductive</td><td>Semi-Structured</td><td>Sequential</td></tr></table>

To date, very little has been done to develop systems for unstructured or wicked problems such as crisis management (EMISARI), nor has there been much work in the area of reciprocal systems (CMCS ZBB). In fact, most human groups try their very best to develop a strategy or problem-solving process that is sequential in nature and avoids reciprocal processes. They fail to grasp that with the computer as a communication facilitator, reciprocal processes can be almost as efficient as sequential ones, and might well lead to better problem-solving results. This is an area of research with considerable potential. Both unstructured problems and reciprocal systems require very general tool support that can be tailored to the needs of the groups as they carry out their activity.

Once a DGSS facility is in common use for carrying out everyday organizational communications, its capability can be extended to integrate all the manager's work. In order to accomplish this, the system's internal design must allow such extensions to be easily implemented. Most of the current message and conference systems on the market are isolated systems that do not allow easy interfacing with other computer resources. Many of the current generation of "Groupware" systems are really shared file facilities without adequate group communication protocols, human role support, or group facilities such as voting and filtering. As a result, widespread usage of such systems will be delayed until a new generation of CMCS systems is in place.

Distributed group support systems introduce a number of problems not usually faced in decision room GDSSs. The following problems should be of interest and concern to both researchers and practitioners:

1. The necessity to support larger decision groups than are typical in face-to-face meetings.

2. The increased likelihood of uncooperative subgroups, "non-rational actors," and lack of full participation. For example, voting procedures must deal with the best ways to determine a quorum and the dynamic feedback of voting results. Software support for detecting the emergence of polarization and aiding the facilitators is another example.

3. Dealing with “critical mass activity” phenomena associated with “negative feedback” if the participation rate is too low, and “information overload” if it is too high.

4. The need for better “meta-models” of the process that incorporate both individual and group problem-solving processes as a basis for making design choices.

5. Software support for leadership and facilitation roles as the group works together online.

6. The need for integration of general capabilities such as hypertext, database structures, form control, modeling capabilities, etc.

If there are some unique coordination problems in DGSS, there are also some unique opportunities for tools and processes to be incorporated into the supporting computer system. Our current work focuses on the development of a new generation of CMCS systems that allows the integration of group communication tools and processes with use of other computer resources within a single interface (Hiltz and Turoff, 1978/1993; Turoff, 1990; Turoff, et. al., 1989). A range of decision support tools and communication-structuring processes are being created as a “toolkit” from which those most appropriate for a specific group and task can be selected. A series of controlled experiments is being conducted to systematically study the best types of “matches” of coordination tools and strategies for different task types in the distributed environment. As the range of features expands and the results of field trials and laboratory experiments are published and become reflected in available commercial products, distributed group support systems can indeed become the central coordinating mechanism for the “virtual organizations” of the future.

## Acknowledgements

Among the sponsors of the research summarized in this article are the National Science Foundation, the Annenberg/CPB Project, the Alfred P. Sloan Foundation, the New Jersey Department of Higher Education, IBM, Hewlett Packard, Apple Computer, AT&T, and Computer Sciences Corporation. We are grateful to Peter and Trudy

Johnson-Lenz and the staff members of the Computerized Conferencing and Communications Center, who implemented and operated most of the systems described, and to the many faculty colleagues and students at NJIT who have participated in the projects. The opinions expressed are those of the authors and do not necessarily reflect those of our research sponsors and colleagues.

## Endnotes

$^{1}$ TOPICS was designed by Participation Systems Inc. and Peter and Trudy Johnson-Lenz. Funding for support of the state legislative science advisors was provided by the National Science Foundation. The structure of TOPICS became the foundation for a conferencing system developed by Participation Systems Inc. called PARTI, which is still available over a decade later.

$^{2}$ A number of GDSS efforts confirm early results on the value of anonymity in particular situations (Linstone and Turoff, 1975). In most situations where high status groups are examining alternatives, participants who have publicly committed their support to a specific choice are unlikely to change their views. Under anonymity conditions, however, people are much more likely to express changes of viewpoint. Most Delphi studies that tracked this measure report an average 30 percent change rate when votes are anonymous, and much less when they are not.

$^{3}$ The doctoral dissertation that resulted provides a very extensive set of findings (Bahgat, 1986).

## References

Bahgat, A. A Decision Support System for Zero-Base Capital Budgeting: A Case Study, unpublished Ph.D. dissertation, Rutgers Graduate School of Management, Newark, NJ, 1986.

Bernstein, L. M., Siegel, E. R., and Goldstein, C. M. "The Hepatitis Knowledge Base: A Prototype Information Transfer System," Annals of Internal Medicine (93:2), 1980, pp. 169-181.

Bieber, M.P. and Kimbrough, S.D. “On Generalizing the Concept of Hypertext,” MIS Quarterly (16:1), March 1992, pp. 77-93.

Business Week, February 8, 1993, pp. 98-103, cover.

Churchman, C.W. The Design of Inquiry Systems, Academic Press, New York, NY, 1971.

Daft, R. L. and Lengel, R. H. "Organizational Information Requirements, Media Richness and Structural Design," Management Science (32:5), May 1986, pp. 554-571.

Dennis, A., George, J., Jessup, L., Nunamaker, J., and Vogel, D. “Information Technology to Support Electronic Meetings,” MIS Quarterly (12:4), December 1988, pp. 591-624.

DeSanctis, G. L. and Gallupe, R. B. "A Foundation for the Study of Group Decision Support Systems," Management Science (33:5), May 1987, pp. 589-609.

Hiltz, S.R. Online Communities: A Case Study of the Office of the Future, Ablex, Norwood, NJ, 1984.

Hiltz, S.R. “The 'Virtual Classroom': Using Computer-Mediated Communication for University Teaching,” Journal of Communication (36:2), Spring 1986, pp. 95-104.

Hiltz, S.R. The Virtual Classroom: Learning Without Limits via Computer Networks, Ablex, Norwood, NJ, 1993, in press.

Hiltz, S.R. and Johnson, K. "User Satisfaction with Computer-Mediated Communication Systems," Management Science (36:6), June 1989, pp. 739-764.

Hiltz, S.R. and Turoff, M. The Network Nation: Human Communication via Computer, Addison-Wesley, Reading, MA, 1978. Revised edition, MIT Press, Cambridge, MA, 1993.

Hiltz, S.R. and Turoff, M. “Structuring Computer-Mediated Communications to Avoid Information Overload,” Communications of the ACM (28:7), July 1985, pp. 680-689.

Huber, G.P. "Issues in the Design of Group Decision Support Systems," MIS Quarterly (8:3), September 1984, pp. 195-204.

Johansen, R., Martin, A., Mittman, R., Saffo, P. I., Gibbet, D., and Benson, S. Leading Business Teams, Addison-Wesley, Reading, MA, 1991.

Johnson-Lenz, P. and Johnson-Lenz, T. "LegiTech/EIES: Information Exchange Among State Legislative Researchers," in Electronic Communication: Technology and Impacts, AAAS Selected Symposium 52, M. Henderson and J. MacNaughton (eds.), Westview Press, Boulder CO, 1980, pp. 103-111.

Johnson-Lenz, P. and Johnson-Lenz, T. "JEDEC/EIES Project—Use of Electronic Information Exchange in Developing Standards in the Electronics Industry," in Studies of Computer Mediated Communications Systems: A Synthesis of the Findings, Research Report Number 16, S.R. Hiltz and E.B. Kerr (eds.), Computerized Conferencing

and Communications Center, New Jersey Institute of Technology, Newark, NJ, 1981.

Johnson-Lenz, P. and Johnson-Lenz, T. "Groupware: The Process and Impacts of Design Choices," in Computer-Mediated Communication Systems: Status and Evaluation, E.B. Kerr and S.R. Hiltz (eds.), Academic Press, New York, NY, 1982, pp. 45-56.

Johnson-Lenz, P. and Johnson-Lenz, T. "Post-Mechanistic Groupware Primitives: Rhythms, Boundaries and Containers," International Journal of Man-Machine Studies (34), 1991, pp. 395-417.

Johnson-Lenz, P., Johnson-Lenz, T., and Hessman J.F. "JEDEC/EIES Computer Conferencing for Standardization Activities," in Electronic Communication: Technology and Impacts, AAAS Selected Symposium 52, M. Henderson and J. MacNaughton (eds.), Westview Press, Boulder, CO, 1980.

Kant, R.C. “Merleau-Ponty and Phenomenology,” in Phenomenology, Kockelmans (ed.), Doubleday, Garden City, NY, 1967.

Keen, P. G. W. and Scott Morton, M.S. Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

Kerr, E.B. and Hiltz, S.R. Computer-Mediated Communication Systems: Status and Evaluation, Academic Press, New York, NY, 1982.

Linstone, H. and Turoff, M. The Delphi Method: Techniques and Applications, Addison-Wesley, Reading, MA, 1975.

McGrath, J.E. Groups: Interaction and Performance, Prentice Hall, Englewood Cliffs, NJ, 1984.

Nelson, T. "A File Structure for the Complex, the Changing and the Intermediate," ACM 20th National Conference Proceedings, New York, NY, 1965, pp. 84-99.

Pinsonneault, A. and Kraemer, K.L. "The Effects of Electronic Meetings on Group Processes and Outcomes: An Assessment of the Empirical Research," European Journal of Operations Research (46), 1990, pp. 143-161.

Pyhrr, P.A. "Zero-Base Budgeting," Harvard Business Review (48), November-December, 1970, pp. 111-118.

Rao, U. and Turoff, M. “Hypertext Functionality: A Theoretical Framework,” International Journal of Human Computer Interaction (2:4), 1990, pp. 333-358.

Rice, R. and Associates. The New Media, Sage, Beverly Hills, CA, 1984.

Scott Morton, M.S. Management Decision Systems: Computer Based Support for Decision Making, Division of Research, Harvard University, Cambridge, MA, 1971.

Simon, H.A. The New Science of Management Decision, Harper and Row, New York, NY, 1960.

Thompson, J.D. "Organizations in Action," McGraw-Hill, New York, NY, 1967.

Turoff, M. "Computer Mediated Communication Requirements for Group Support," Journal of Organizational Computing (1:1), 1991, pp. 85-113.

Turoff, M. and Hiltz, S.R. "Computer Support for Group versus Individual Decisions," IEEE Transactions on Communications (Com-30:1), January 1982, pp. 82-90.

Turoff, M. and Rana, A.R. "A Task for Group Decision Support Systems," working paper, New Jersey Institute of Technology, Newark NJ. January 1993.

Turoff, M., Hiltz, S.R., Foster, J.F., and Ng, K. "Computer Mediated Communications and Tailorability," Proceedings of the Twenty-Second Annual Hawaii Conference on Systems Science (III), IEEE Computer Society, Washington, DC, January 1989, pp. 403-411.

Valacich, J.S., Vogel, D.R., and Nunamker, T. F., Jr. "Integrating Information Across Sessions and Between Groups in GDSS," Proceedings of the Twenty-Second Annual Hawaii International Conference on Systems Science (III), IEEE Computer Society, Washington, DC, 1989, pp. 291-299.

Van deVen, A. and Delbecq, A.L. "Nominal and Interacting Group Processes for Committee Decision Making Effectiveness," Academy of Management Journal (14:2), June 1971, pp. 203-212.

Wilcox, R.H. and Kupperman R. "An Online Management System in a Dynamic Environment," Proceedings of the First International Conference on Computer Communications, IEEE Computer Society, Washington, DC, 1972, pp. 117-120.

Wildavsky, A. and Hammond, A. "Comprehensive Versus Incremental Budgeting in the Department of Agriculture," Administrative Science Quarterly (10), 1965, pp. 321-346.

## About the Authors

Murray Turoff is a professor of computer science and a member of the School of Industrial Management at the New Jersey Institute of Technology, as well as a member of the Graduate School of Management at Rutgers University. He received his B.S. from the University of California at Berkeley and his Ph.D. from Brandeis. His research interests include the design of computer-mediated communication systems and decision support systems, and human-computer interaction.

Starr Roxanne Hiltz is a distinguished professor, computer and information science, NJIT, and a member of the faculty of the Graduate School of Business, Rutgers University. She received her B.A. from Vassar and her M.A. and Ph.D. from Columbia. Her research interests include the social impacts of computers, human-computer interaction, and computer support for group activities such as decision making and collaborative learning.

Ahmed N.F. Bahgat is a member of the faculty at Sadat Academy of Management Sciences, Cairo, an advisor to Egypt's Minister of Cabinet Affairs, and an entrepreneur. After completing his master's degree in accounting, he received a master's degree in computer science from the New Jersey Institute of Technology and a Ph.D. in management of information systems and accounting from the Graduate School of Management, Rutgers. His research interests include the implementation of information systems to improve the effectiveness of decision making, particularly in developing nations.

Ajaz R. Rana received his master's degree in computer science from the New Jersey Institute of Technology and is a current Ph.D. student in the joint Rutgers/ NJIT Ph.D. program in management of information systems. He is in the last stages of completing an experimental investigation of the use of GDSS tools and the CMCS environment to deal with peer review processing of journal articles. For 1993-94, he is a special lecturer in the CIS department at NJIT.
