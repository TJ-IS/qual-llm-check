---
otero_id: 27232
otero_key: "K6ABJB2C"
title: "Information Technology to Support Electronic Meetings"
authors: "Alan R. Dennis; Joey F. George; Len Μ. Jessup; Jay F. Nunamaker; Douglas R. Vogel"
year: "1988"
journal: "MIS Quarterly"
doi: "10.2307/249135"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Information Technology to Support Electronic Meetings

Author(s): Alan R. Dennis, Joey F. George, Len M. Jessup, Jay F. Nunamaker, Jr. and Douglas R. Vogel

Source: MIS Quarterly, Vol. 12, No. 4 (Dec., 1988), pp. 591-624

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/249135

Accessed: 18-10-2015 04:05 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Information Technology to Support Electronic Meetings

By: Alan R. Dennis
Joey F. George
Len M. Jessup
Jay F. Nunamaker, Jr.
Douglas R. Vogel

Department of MIS
College of Business and Public Administration
The University of Arizona
Tucson, AZ 85721

## Abstract

As managers spend more of their time in meetings, the study of information technology to support meetings becomes increasingly important. Several unique systems to support meetings electronically have been developed in industry and universities. The PLEXSYS systems at the University of Arizona have been operational since 1985 and are now being implemented in industrial sites. This article proposes and defines a new term for information technology systems that support group meetings: electronic meeting systems (EMS). EMSs are more than group decision support systems (GDSS): they support more tasks than just decision making; they focus on communication. They move beyond the GDSS decision room, where groups must meet at the same time in the same place, to meetings that can be conducted across time and space. The article then presents a model of the EMS concept, which has three components: group process and outcomes; methods; and environment. Each of these components is explained in turn, and the implications derived from their study to date are discussed. Finally, the implementation of information technology for meeting support and its use in corporate settings will be addressed, as it has implications for productivity, meeting size, group member participation, and the role of the IS department.

Keywords: Electronic meeting systems, group decision support systems, group process and outcomes, methods, software, environments

ACM Categories: K.0, K.m, H.0, H.4.2, H.4.m

## Introduction

Managers and knowledge workers spend a significant proportion of their time working in groups. Estimates of this proportion range from 60-70% for information systems (IS) managers to 30-80% for general managers (Hymowitz, 1988; Ives and Olson, 1981; Mintzberg, 1983; Mosvick and Nelson, 1987). Unfortunately, most group meetings are not as productive as they could be (Goldhaber, 1974; Hymowitz, 1988; Mosvick and Nelson, 1987; Tubbs, 1984). One Fortune 500 company estimated that it lost \$71 million each year due to ineffectively managed meetings (Mosvick and Nelson, 1987). Yet, even though significant advances have been made to enhance individual productivity through the use of information technology (IT), comparatively little has been done to improve group productivity.

Recently, however, there has been rapidly growing interest in the use of IT to support meetings (Richman, 1987). While the concept has been discussed for several years (Huber, 1984; Keen and Scott Morton, 1978), most early efforts to develop systems to support meetings met with limited success (Kraemer and King, 1986). One of the most promising early efforts was led by G.R. Wagner at Execucom (Gibson and Ludl, 1988; Kull, 1982), although the system did not survive. The University of Arizona's first system to support meetings, developed as part of the ongoing PLEXSYS project, integrated some of Wagner's ideas in its design and implementation. The Arizona facility, which was also based on some of the work of Paul Gray (Gray, 1981; 1983), was fully operational in March, 1985. At this same time, researchers at the University of Minnesota also began to investigate the potential of systems to support meetings (DeSanctis and Gallupe, 1985).

Several other university and industry groups have developed IT-based systems to support meetings and group work (e.g., EDS, MCC, Xerox PARC, Claremont Graduate School).

Such systems can be grouped into two broad classes: group decision support systems (GDSS) and computer-based systems for cooperative work (CSCW) (Figure 1). The distinction between these two types of systems is in the primary type of group support they each were designed to provide. GDSSs are more task-oriented in that they provide a means for a group to work on and complete a task, such as reaching a decision, planning, or solving problems. CSCWs, on the other hand, are more driven by communication needs. They provide a means for small groups to communicate more efficiently, enabling them to jointly create or critique a document, for example. The distinctions between these two classes of systems are blurring. Some software tools developed as part of the PLEXSYS project exemplify the common area between GDSS and CSCW. In time, we believe, these two classes of systems will completely overlap, representing a single class of IT systems to support electronic meetings.

The purpose of this article is to propose a conceptual model of IT-based systems to support meetings, based on experiences in the PLEXSYS project. (See Appendix A for a brief history of the PLEXSYS project, and Appendix B for a description of the PLEXSYS environments). First, in light of the blurring of the distinctions between GDSS and CSCW, and in light of the changing technological focus from computers to IT in general, a new term is proposed and defined: information technology to support electronic meetings, or electronic meeting systems (EMS), for short. Then a model of the EMS concept is presented. The model is divided into three component parts: group process and outcomes; methods; and the EMS environment. Each of these components is then discussed separately, beginning with a conceptual model, moving to a discussion, and ending with implications. The article ends with a discussion of the broader implications that can be drawn from the discussion of the EMS concept.

![](/api/attachments/K6ABJB2C/fulltext/images/6e71be985144a176643a51ef51f0aa3005756fc8d1aa1d8acb18b6f31d597511.jpg)  
Figure 1. The Progression to EMS

## Definition of EMS

Webster defines a meeting as, “an act or process of coming together.” The definition does not imply that only one type of task is performed in a meeting (e.g., decision making), nor does it imply that the people participating in the meeting must come together in a central location at a specific time. It says only that they come together. Since the definition of a meeting is so broad, it makes sense to use a term that matches the definition to designate the information technology systems that support meetings. The term we propose is electronic meeting systems (EMS).

EMSs are systems that use information technology to support the group work that occurs in meetings. EMSs combine the task-orientation of GDSS and the communication-orientation of CSCW. GDSS has been defined as an integrated computer-based system to facilitate the solution of an unstructured or semi-structured task by a group that has joint responsibility for performing it (DeSanctis and Gallupe, 1985); EMS is that and more. It also enhances communication among group members (Bui, 1987; Bui and Jarke, 1984; DeSanctis and Gallupe, 1987; Huber, 1984; Kraemer and King, 1986; Loy, et al., 1987). EMS provides an additional communication channel; it enhances communication by adding structure, either implicitly or explicitly; and it can provide a complete recording of the group session to aid productivity in subsequent sessions (Karon, 1987). EMS also moves beyond the decision-making function implied in the term GDSS, since meetings involve more than just decision making; for example, they can also involve problem structuring, idea generation, idea organization, planning, creating, and even the elicitation of knowledge in the construction of expert systems (Nunamaker, et al., 1988b). In addition, EMS moves beyond the decision room, where groups must meet at the same time in the same place, to meetings that can be conducted across time and space. Group members can be located in different places and in different times, yet still work together to accomplish some common purpose.

## Therefore, we define EMS as:

An information technology-based environment that supports group meetings, which may be distributed geographically and temporally. The IT environment includes, but is not limited to, distributed facilities, computer hardware and software, audio and video technology, procedures, methodologies, facilitation, and applicable group data. Group tasks include, but are not limited to, communication, planning, idea generation, problem solving, issue discussion, negotiation, conflict resolution, systems analysis and design, and collaborative group activities such as document preparation and sharing.

## EMS Concept

There are three parts to the EMS concept: group process and outcomes, methods, and environment (Figure 2).

As a category, group process and outcomes encompasses several different constructs. These include the characteristics of the group itself, the characteristics of the task on which the group is working, the organizational context in which system use takes place, the process through which the group utilizes the system, and the outcomes resulting from system use. These elements of the larger concept can be grouped into a research model (Figure 3) that shows the relationships of these constructs to each other. Past GDSS and CSCW research has concentrated on these constructs, and the model is an attempt to synthesize past work as well as provide a model for future research within this area. The EMS concept goes beyond the constructs listed above; it must necessarily include methods and environments.

The second component of the larger concept is methods. On one level, methods are the software support provided in EMS, which can be thought of as the discrete tools provided for group support. Examples include electronic brainstorming, electronic notepads, and alternative ranking tools. Methods, however, are more than just the programs that the term software implies, because certain procedures, rules and methodologies are built into the software. Consider, for example, an electronic brainstorming tool in an EMS environment. The purpose of the tool is to allow group members to freely generate ideas. In order for the group to use the tool well, the procedures that promote idea generation and sharing must be built into the system. The methodology of manual brainstorming must be transferred to the EMS tool. In some systems, a human facilitator is also present to provide addi-

Environment

Methods

![](/api/attachments/K6ABJB2C/fulltext/images/0be1d7b82d9116b8ecafaa7a6cef194628e5faf24b11971c0e40ae2827d09b39.jpg)  
Figure 2. Conceptual Model

tional methodologies as needed. Where applicable, this human facilitation would also be a part of methods.

The third component of EMS is the environments in which the systems are used. Many people think of GDSS in terms of a room with networked workstations and public displays, where a single group can convene face-to-face to hold a meeting, but this is only one of many possible EMS environments (shown later in Figure 8). Groups can meet at the same time yet be physically dispersed, as is common in many CSCW systems. In addition, group members can work together from their own offices asynchronously. Other EMS environments can support several different groups, each distributed temporally and geographically. EMS moves beyond the limitations of the meeting room to support meetings across time and place. This is not to say that the GDSS room has outlived its usefulness; there will always be a need for such a facility, but EMSs facilitate group support in many different environments.

As Figure 2 indicates, there are areas of overlap between the three components. For example, some of the procedures and methodologies thought of as being part of methods might also be part of group process and outcomes. Structure beyond that provided by the software might be provided by group members as they work. Likewise, there might be overlaps between methods and environment, and between environment and group process and outcomes. These overlaps should be expected since it takes all three components to make an EMS; no such system is developed one component at a time. As each component is developed, it must necessarily take aspects of the other two components into consideration, and this produces the overlapping areas in Figure 2. The center of the diagram, where all three areas overlap, represents those parts of the overall EMS that are well-integrated, forming the heart of a well-designed EMS.

When any two of the three components has been specified, the third component is constrained by the limits of the other two. There is still some flexibility, but for the most part, the model has only two degrees of freedom. For example, if a particular group working on a particular task in a particular organizational context has decided to utilize the EMS approach, and it is further decided that the EMS environment to support them will allow them to work in their own offices asynchronously, then this group has little choice of the methods they will use. The methods will necessarily be devoid of active human facilitation, and the task, the group, and the physical and temporal dispersion of the group will necessitate the use of certain tools with certain built-in procedures. If this same group was to decide on the methods to use rather than the particular environment to work in, then the choice of environment would be limited. A more detailed discussion of each of these three components follows.

![](/api/attachments/K6ABJB2C/fulltext/images/3e28684f38cb86cad50b037c6018c0bacde12b44c7580a92b6e7300424f9691f.jpg)  
Figure 3. A Research Model

## Group Process and Outcome

The first part of the EMS concept is group process and outcome. As mentioned previously, this part of the concept has been dealt with most in the empirical GDSS literature to date. The methods and the environments have generally been perceived as givens, but they vary widely across many dimensions of methods and environments, as shall be seen in the following sections.

This section proposes a research model that can be used as a basis for empirical studies of EMS. The model is based on those variables and classes of relationships important to the group process and outcomes with EMS: group characteristics, task, context, environment, group process, and process outcomes. The relevant GDSS empirical literature is then reviewed. A full review of the empirical GDSS and CSCW literature is beyond the scope of this article, so it is confined to the GDSS literature. Since we see GDSS as a part of the larger EMS concept, the implications for group process and outcomes that can be drawn from a review of the relevant GDSS literature also apply to EMS in general.

## A Research Model

There is no commonly accepted causal model for studying group process and outcomes in GDSS, although several researchers have presented conceptual ideas based on theory and observation (DeSanctis and Gallupe, 1987; Huber, 1984; Kraemer and King, 1988). Many studies have used the work of McGrath (1984) on small groups as the beginning basis for such models (Gallupe, et al., 1988; Watson, et al., 1988; Zigurs, 1987). In general, each research study or research group has developed a micro model as the basis for one study or for a program of research.

Figure 3 displays an integration of many of the models used to conduct GDSS research. It is necessarily incomplete, as there are far more factors affecting meetings than can be represented in one diagram. However, it does present some of the variables and relationships considered in past research, as well as those that should be addressed in future research. The variables in the model are representative of those variables studied most often in past GDSS and computer-mediated communication research. The classes of variables are discussed first, followed by a discussion of the proposed relationships among them.

## Variables

The model has six basic sets of variables. First, the characteristics of the group, such as group size and group proximity (whether in one room or distributed in several remote locations), and past experience with the problem area, such as group process and tools, must be considered. The characteristics of the individual participants, group cohesiveness and motivation, past group history, and future relationships have also been shown as important in studies of meetings, so they should be considered in the study of EMS.

The exact type of task is very important to group performance (Poole, et al., 1985), so any study of performance must clearly define the nature of the task performed. The second class of variables, then, deals with the task faced by the group. One way to characterize the task is along the “rational/irrational” dimension. Also, task complexity can be measured by the number of issues and alternatives that must be considered and the time required to identify and assess the issues and alternatives (Hackman, 1968; Shaw, 1932; Shaw, 1973). But categorizing task type can be much more complex. McGrath (1984) has developed a taxonomy of eight group tasks, which provides a more precise method for analyzing and discussing tasks.

Third, the larger context in which the group meeting occurs (such as organizational or experimental situations) the larger environment, and individual incentive system are important (DeSanctis and Poole, 1987; Jessup, 1987).

Fourth, the presence or absence of an EMS, plus the specific characteristics of EMS design will have an impact on the group process and outcome. There are many different types of EMS and many different designs within each particular type; this variation may be important in explaining differences in reported outcomes.

Fifth, the nature of the group process, such as the presence or absence of a formal or informal group leader, the use of anonymity, the number of meeting sessions, the degree of structure in the group process, equality of participation, level of conflict, and the level of non-task (“uninhibited”) behavior must be considered.

Finally, there are many outcomes of a group meeting that may be measured. These include the decision / outcome quality, participant satisfaction with the outcomes and the process, participant confidence in the outcomes, process time required, level of group consensus, number of comments during the meeting, and the number of alternatives or issues considered.

## Relationships

Many early studies of GDSS used very simple models to study the effects of GDSS use on meetings. Independent variables such as GDSS use were hypothesized to directly affect dependent variables such as performance, with no intervening variables. These models are straightforward and easy to use, and represent a reasonable model of the underlying relationships. In Figure 3, these relationships are represented by the arrows running from the four left boxes to the outcome box.

More recently, researchers have begun using more complex models in an attempt to better understand the actual relationships involved. For example, DeSanctis and Poole (1987) propose a model of adaptive structuration, in which outcomes depend on the process in which the system is used. This process is in turn dependent to some extent on the group, task, context, and environment. This is incorporated into Figure 3 by the intervening position of the process box between the four left boxes and the outcome box.

Group process, then, can be either a dependent or independent variable, depending on the research design. For example, many system tools provide anonymity, while traditional manual techniques do not. Therefore, anonymity is a dependent variable since it is dependent on the presence or absence of the tool. In other cases, anonymity has been an independent variable, since non-anonymous system tools were compared to anonymous tools.

## Research Findings: Overview

It is tempting to analyze all past GDSS research dealing with group process and outcome as a single unified body of literature. Some may argue there is so little past empirical GDSS research that it makes little sense to do otherwise. However, after additional consideration, it becomes evident that there are several different but related streams of empirical research. This research has been conducted in both the laboratory and in the field, and it has involved two types of GDSS: Local Area Decision Nets (LADN) and Decision Rooms. LADNs are characterized by small group size, physically dispersed group members, and synchronous (or "real time") exchange (see Figure 8). Decision Rooms are characterized by small group size, having the group members together in the same room, and synchronous exchange.

Under the broader label of experimental research, at least four streams of research can be identified, as depicted in Figure 4. They compare: LADNs to Decision Rooms; LADNs to no computer support; Decision Rooms to no computer support; and two different configurations of the same Decision Room. The field research we reviewed has been confined to the use of Decision Rooms by real groups. In the next section, the four streams of experimental research, then the field work are discussed. Because work in this area is so recent, some of the work referred to is reported in working papers and not yet published.

## Experimental studies

## Local Area Decision Nets and Decision Rooms

Three studies have compared LADN and Decision Room GDSS (Bui, et al., 1987; Gallupe and McKeen, 1988; Jessup, et al., 1988) (Table 1). Each used a different GDSS system and slightly different experimental design. The Bui, et al. (1987) study compared the use of GDSS by proximate (face-to-face) and dispersed group members. Jessup, et al. (1988) started with the same design, but added the dimension of anonymity. Gallupe and McKeen (1988) compared two different systems — a GDSS and a computer-mediated conferencing (CMC) system — in proximate and dispersed settings. In these latter two studies, proximate groups were more satisfied with the group process than were dispersed groups.

## Local Area Decision Nets

There has been a substantial body of work on cross-media comparisons of computer conferencing (CC), led by researchers at the New Jersey Institute of Technology (Hiltz, et al., 1986; Turoff and Hiltz, 1982) and at Carnegie Mellon University (Kiesler, et al., 1984; Sprague, 1980).

![](/api/attachments/K6ABJB2C/fulltext/images/a93b4b1b3128a2c6e7ad5ebbd90c1bea1870a2edbc736972d582dea4cd04c83f.jpg)  
Figure 4. Current Research Streams

Computer conferencing fits nicely into the LADN categorization of GDSS, as shown by the groups using these systems in experiments at the above institutions: the groups were small, they worked at the same time, and each group member was isolated. Table 2 reports some of the findings for four of the five experiments reported in Hiltz, et al. (1986), Kiesler, et al. (1984), Siegel, et al. (1986), and Turoff and Hiltz (1982). These experiments do not constitute all the studies done in this area, but they are representative of this body of work. (Full consideration of this literature is, however, beyond the scope of this article.) In general, the results of such experiments suggest that groups using computer conferencing (or LADN), in comparison to conventional face-to-face groups (FTF), generate decisions of equal quality, are less likely to reach consensus, take longer to reach a group decision, are more likely to participate equally, and are more likely to engage in non-task behavior such as “flaming,” although Turoff and Hiltz (1982) found face-to-face groups more likely to engage in tension release behavior.

Table 1. Experimental GDSS Research: Decision Rooms and Dispersed Groups  
COMPARING GDSS DECISION ROOMS TO LOCAL AREA DECISION NETS

<table><tr><td colspan="5">COMPARING GDSS DECISION ROOMS TO LOCAL AREA DECISION NETS</td></tr><tr><td>Variables/Studies</td><td>Number of Solutions</td><td>Solution Quality</td><td>Decision Speed</td><td>Satisfaction</td></tr><tr><td>Bui, et al., 1987</td><td>no effect</td><td>dispersed groups better</td><td>dispersed groups faster</td><td>no effect</td></tr><tr><td>Jessup, et al., 1988</td><td>most in anonymous/dispersed; least in identified/proximate</td><td></td><td></td><td>proximate groups more satisfied; most satisfied groups in anonymous/dispersed and identified/proximate</td></tr><tr><td>Gallupe &amp; McKeen, 1988</td><td></td><td>no effect</td><td>GDSS took longer than CMC; dispersed took longer than proximate</td><td>no effect for GDSS; dispersed groups less satisfied</td></tr></table>

Table 2. Experimental GDSS Research: Local Area Decision Nets

<table><tr><td colspan="6">GDSS LOCAL AREA DECISION NETS VS. NO COMPUTER SUPPORT</td></tr><tr><td>Variables/ Studies</td><td>Decision Quality</td><td>Consensus</td><td>Time to Decision</td><td>Participation</td><td>Non-Task Behavior</td></tr><tr><td>Siegel, et al., 1986, exp. 1</td><td></td><td></td><td>CMC* groups took longer</td><td>CMC groups more equal</td><td>CMC groups less inhibited</td></tr><tr><td>Siegel, et al., 1986, exp. 3</td><td></td><td></td><td>CMC groups took longer</td><td>CMC groups more equal</td><td>CMC groups less inhibited; e-mail groups less so</td></tr><tr><td>Turoff and Hiltz, 1982, exp. 1</td><td>no effect</td><td>less likely in CC groups</td><td></td><td>no effect</td><td>more tension release in FTF*</td></tr><tr><td>Turoff and Hiltz, 1982, exp. 2</td><td>no report</td><td>leader alone or computer feedback alone more likely to lead to consensus</td><td></td><td></td><td></td></tr></table>

\*CMC = computer mediated communication; FTF = face-to-face.

## Decision Rooms Compared to No Computer Support

The largest body of GDSS research to date is concerned with comparing the use of a Decision Room to no computer support. In many of these studies, groups receiving no computer support either use the same structure as the GDSS groups, or they use no structured processes at all. The various studies, along with some of their findings, are listed in Table 3 and discussed below. The most obvious generalization that can be made from looking at Table 3 is that the results from these studies are inconsistent.

Table 3 illustrates the three most investigated dependent variables in these 10 studies: quality of decision, level of participation, and satisfaction with the group process. The findings for these variables are inconsistent across all 10 studies. Quality of decision was rated better in GDSS groups than in non-GDSS groups in five of the 10 studies, while four studies found GDSS group decisions to be at least as good as those made by non-GDSS groups. Use of the GDSS had no effect on the level of participation of group members in four of the seven studies that reported results about participation, but produced more even levels of participation in the other three studies. Four of the seven studies that measured satisfaction with the group process found that GDSS users were no more and no less satisfied with the process than were group members that did not use a GDSS. One of the studies found higher levels of satisfaction in GDSS groups and two found lower levels of satisfaction.

Table 3. Experimental GDSS Research: Decision Rooms  
GDSS DECISON ROOMS VS. NO COMPUTER SUPPORT

<table><tr><td>Variables/ Studies</td><td>Decision Quality</td><td>Consensus</td><td>Time to Decision</td><td>Participation</td><td>Inhibition</td><td>Satisfaction w/Process</td><td>Satisfaction w/Outcome</td></tr><tr><td>Steeb and Johnston, 1981</td><td>GDSS better</td><td></td><td>GDSS takes longer</td><td>no report</td><td></td><td>increased w/GDSS</td><td>increased w/GDSS</td></tr><tr><td>Lewis, 1982</td><td>GDSS better</td><td></td><td></td><td>GDSS reduces individual dominance</td><td></td><td>no effect</td><td></td></tr><tr><td>Ruble, 1984</td><td>no effect</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gallupe, et al., 1988</td><td>GDSS better</td><td></td><td>GDSS takes longer</td><td>no effect</td><td></td><td>reduced by GDSS</td><td>reduced by GDSS</td></tr><tr><td>Beauclair, 1987</td><td>no effect</td><td></td><td>no effect</td><td>no effect</td><td></td><td></td><td>no effect</td></tr><tr><td>Watson, et al., 1988</td><td>GDSS worse than manual; better than nothing</td><td>no effect</td><td></td><td></td><td></td><td>reduced by GDSS</td><td></td></tr><tr><td>Zigurs, 1987*</td><td>GDSS better</td><td></td><td></td><td>more even distribution of influence</td><td></td><td></td><td></td></tr><tr><td>A. Easton, 1988†</td><td>no effect</td><td></td><td>no effect</td><td>no effect</td><td></td><td>no effect</td><td>GDSS more satisfied</td></tr><tr><td>G. Easton, 1988</td><td>no effect</td><td>less likely in GDSS</td><td>faster in FTF</td><td>more equal in GDSS</td><td>no effect</td><td>no effect</td><td></td></tr><tr><td>Jarvenpaa, et al., 1988‡</td><td>EBB first, workstation 2nd and conv. last</td><td></td><td></td><td>no effect</td><td></td><td>no effect</td><td></td></tr></table>

\*This study, while a cross-media comparison, focused on process rather than outcomes.  
†In this study, structured approaches, whether automated or not, led to better quality decisions, which took longer to make, had higher user satisfaction with outcomes and processes, and had more equally distributed participation. ‡“EBB” stands for Electronic BlackBoard, with no other computer support. “Workstation” means a GDSS with networked workstations, with no other computer support. “Conv.” stands for conventional, meaning no computer support.

The other four dependent variables listed in the table have been investigated in half or fewer of the studies. Three of the five studies that looked at time to decision found that GDSS users took longer to reach a decision. The other two studies found no differences. The four studies that measured satisfaction with outcomes also had mixed results: two found higher levels of satisfaction, one found lower levels, and one found no differences. The two studies investigating consensus produced inconsistent findings as well: one found no effect and the other found consensus less likely among GDSS groups. And finally, the only study out of these 10 that investigated “flaming” found that there were no differences between GDSS and non-GDSS groups in the number of uninhibited comments they produced.

One area of possible research that has been neglected to date is a comparison of key attributes of different GDSS Decision Rooms. Decision Rooms differ across several attributes, such as architectural design, room configuration, public display capabilities, and system software. Using similar groups of subjects and a similar task, how would two different GDSS Decision Rooms compare on such outcome measures as decision quality and satisfaction with the process? This seems to be an overlooked area, which has a great deal of promise, but which would require cooperation among researchers operating distinctive Decision Rooms.

## Comparing Different Configurations of the Same Decision Room

The final stream of experimental GDSS research to be considered is concerned with the comparison of different configurations of the same Decision Room. These studies vary one or more features available in the Decision Room to further the understanding of when certain features are appropriate and when they are not. Only two such studies have been conducted (Connolly, et al., 1988; Jessup, et al., 1987), and they are listed with some of their findings in Table 4. Both studies used the University of Arizona's PLEXSYS system, and both studies varied the anonymous feature of PLEXSYS (see appendices). Some groups tagged all their comments with their names (identified) whereas other groups sent and received comments that were not tagged (anonymous). Both studies found that anonymous GDSS groups generated significantly more total comments, as well as more critical comments.

Anonymity is only one of the many features of PLEXSYS that could have been varied. Other systems likewise have many features that can be varied and tested in experimental situations. This is an area full of potential for GDSS researchers.

## Case studies and field studies

The primary methodology currently used to evaluate GDSS is experimental research. There have been a few studies, however, that have used the case study or field study methodology. For the purposes of this article, a GDSS case study involves a “real world” group using a GDSS at the GDSS site, away from their usual operating location. Generally, these GDSSs are located on the premises of a university, although some are commercial products. A field study, on the other hand, involves the study of a “real world” group using a GDSS at a GDSS site that is on the premises of their usual operating location. For clarity, we classified the Jarvenpaa, et al. (1988) study as an experiment, even though it was conducted in the field, and it will not be discussed further in this section.

Table 4. Experimental GDSS Research: Within Decision Rooms  
COMPARING DIFFERENT CONFIGURATIONS OF A SINGLE DECISION ROOM

<table><tr><td>Variables/Studies</td><td>Total Number of Comments</td><td>Number of Unique Solutions</td><td>Number of Critical Comments</td><td>Number of Supportive Comments</td><td>Overall Satisfaction</td></tr><tr><td>Jessup, et al., 1987</td><td>more with anonymity</td><td></td><td>more with anonymity</td><td>no effect</td><td></td></tr><tr><td>Connolly, et al., 1988</td><td>more with anonymity</td><td>more in critical groups</td><td>more with anonymity</td><td>more with anonymity</td><td>higher for supportive groups</td></tr></table>

Table 5 lists five studies that utilize the case and field study methodologies. The first four are case studies, as defined above, and the last is a field study. (Two other papers sometimes considered as reports on field studies actually are not: Kull (1982) reports on a GDSS simulation, and Kersten (1985) reports on the use of a GDSS in a course environment). With the exception of the first one, all of these studies were conducted in the PLEXSYS environment. The case studies were conducted at the University of Arizona, and the field studies were conducted on-site in a manufacturing plant.

All six studies report that “real world” users were extremely satisfied with GDSS use. This finding is not consistent with experimental findings on satisfaction, where some subjects were satisfied with GDSS use and others were not. One explanation for this may be the ability of real world users to compare GDSS use with conventional means of accomplishing the same tasks, an ability student subjects in experimental studies may lack. The other consistent finding, which varies only in particulars, is that real world participants also judge GDSS use to be extremely effective in helping them perform the tasks they are working on. Two of these studies (Nunamaker, et al., forthcoming 1989, Vogel and Nunamaker, 1988), for example, report vast time savings from GDSS use over conventional means. This finding also varies from experimental findings, where task performance varies widely. An explanation could lie in the fact that participants in case and field situations are working on solving their own problems instead of problems assigned to them by researchers. Also, tasks dealt with in the field are generally more complex than those dealt with in the laboratory, and, as such, are more illustrative of computer support benefits. Groups in the field tend to bring together different facets of domain knowledge that cumulatively yield a comprehensive picture of a complex area exceeding the capabilities of any individual group member.

## Implications From Group Process and Outcome

Two generalizations become readily apparent from reviewing the GDSS literature on group process and outcomes: (1) very little formal empirical work has been done in the area, and (2) many of the results from the work that has been done are inconsistent.

So little work has been done comparing LADNs to Decision Rooms that generalizations from the work are not very meaningful. The same is true of the work comparing different configurations of the same Decision Room. These are, however, very important areas that GDSS researchers should actively pursue. Considerably more research has been done on LADNs, but as these systems move beyond simple messaging systems (e.g., e-mail), opportunities arise for research into the effects of more sophisticated LADNs on groups.

As discussed earlier, very few generalizations can be made reliably from reviewing the experimental work that compared Decision Room use to no computer support for groups. At best GDSS use is associated with better quality decisions than no GDSS use (Gallupe, et al., 1988; Jarvenpaa, et al., 1988; Lewis, 1982; Steeb and Johnston, 1981; Zigurs, 1987), and at worse, there is no difference (Beauclair, 1987; Easton, A., 1988; Easton, G.K., 1988; Ruble, 1984). At best, GDSS use facilitates more even levels of participation among group members (Easton, G.K., 1988; Lewis, 1982; Zigurs, 1987), and at worst, there are no differences (Beauclair, 1987; Easton, A., 1988; Gallupe, et al., 1988; Jarvenpaa, et al., 1988). Findings on the other dependent variables are either inconsistent or are based on too few studies to mention.

It is important to observe, however, that the 10 studies that compared Decision Rooms to no computer support were conducted using seven different GDSSs. Each GDSS facility was designed based on a different philosophy, and the software used in each facility also varied widely. Different tasks, as well as different measures of the dependent variables, were used in the studies. There is so much variation across these studies that generalizations become problematic. A coherent body of knowledge concerning GDSS can be accumulated if researchers share software designs, experimental tasks, and variable measures in the future. In the meantime, it is important to the accumulation of knowledge about GDSS that researchers describe in detail the GDSS, task, procedures, and measures they use in their studies. This permits other researchers to better understand past work and to better plan future studies. The resulting accumulation of knowledge will apply to and aid in the development of EMS.

Table 5. GDSS Research: Case and Field Studies

<table><tr><td colspan="3">CASE AND FIELD STUDIES IN GDSS RESEARCH</td></tr><tr><td>Observations/Studies</td><td>Satisfaction</td><td>Effectiveness</td></tr><tr><td>Adelman, 1984</td><td>final design well supported by all participants</td><td>action taken within week after GDSS exercise</td></tr><tr><td>Nunamaker, et al., 1987</td><td>participants reported high levels</td><td>more equal participation</td></tr><tr><td>Vogel &amp; Nunamaker, 1988</td><td>participants reported high levels</td><td>participants said they did as much in one morning as would have normally taken two days</td></tr><tr><td>Dennis, et al., 1988</td><td>participants reported high levels</td><td>meetings rated extremely effective by management and participants</td></tr><tr><td>Nunamaker, et al., 1989</td><td>participants reported high levels</td><td>found manhour savings of 61% from GDSS use, compared to unsupported sessions</td></tr></table>

Research findings are much more consistent in the field studies reviewed in this article. “Real world” users are consistently satisfied with the group process, and they believe GDSS use to be very effective. The implication is that there are fundamental differences between how GDSSs are studied in the laboratory and applied in the field, and the effects they have on group processes and outcomes. Careful analysis is necessary to isolate and understand these differences.

One explanation for the rather mixed success of GDSS in experimental tests, as contrasted with its success in field studies, is the size of the groups and the complexity of the tasks. GDSS technology has some overhead cost. Previous experimental research focused on smaller groups (typically three or four members) and less complex tasks than those typically found in field settings (with groups of seven to ten or larger). In these cases, the overhead costs (or “process losses”) introduced by the specific GDSS system may simply have been higher than the marginal benefits provided to small groups addressing less complex tasks. GDSS may prove most appropriate in the support of large groups addressing complex tasks.

## Methods

Methods are a key component of the EMS concept. As discussed earlier, methods include software and the procedures and methodologies built into the software. Methods can also include the efforts of the human facilitator. The purpose of this section is to describe different types of methodological support that can be provided through EMS. First, a typology of EMS methods is described. Then the concept of an EMS toolkit is presented. The focus of this section is on characteristics of EMS methods that address the needs of groups responsible for complex decisions in which each member has a role and is an active participant in the group's discussions. Methods developed for computer conferencing or e-mail applications are not considered.

## EMS methods typology

Methods developed for EMS can be classified according to a number of different schemes. We have identified three dimensions where they vary: (1) whether support is provided for the facilitator only, for participants only, or for both; (2) whether group processing is sequential or parallel; and (3) whether the methods support single or multiple group sessions. The first two of these dimensions are represented in the matrix of Figure 5. For clarity, the third dimension, single or multiple session support, has been omitted from the figure. The primary difference between single or multiple session support is the use of a knowledge base and other technological support to facilitate integration and use of information across sessions and between groups.

Support for facilitators only can occur in either a sequential processing or parallel processing mode, but parallel processing for facilitators only is rare, and there may be few instances where such support would be useful. The facilitator is the only person receiving IT support, and parallel processing would imply having the facilitator run several processes simultaneously. Much more common is sequential processing support for facilitators. This type of support is the only kind available in single-workstation systems, where the facilitator enters comments and solutions that group members have generated through conventional means. Groups members generally follow the process through watching their comments appear on a public display. Such support is also available in multiple-workstation systems. In such systems, the facilitator guides the group through a complex process, such as consolidation of ideas generated during a brainstorming session. Group members may watch on a public display, or video switching may be used so they can watch on individual user screens.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Processing Mode</td></tr><tr><td>Sequential</td><td>Parallel</td></tr><tr><td rowspan="3">IT Support Provided For</td><td>Facilitator Only</td><td></td><td></td></tr><tr><td>Participant Only</td><td></td><td></td></tr><tr><td>Facilitator and Participant</td><td></td><td></td></tr></table>

Figure 5. EMS Methods Typology

Support for participants only requires a multiple-workstation EMS. Participants are allowed to work from their individual workstations, doing whatever they want when they want. No facilitator is required for them to use the EMS. They may work sequentially or they may work together simultaneously, in effect processing in parallel. In the first situation, the methodology can be designed so that users must take turns generating comments, which are displayed on a public screen. In the second situation, the methodology is designed so that all participants can enter comments at the same time. The methods determine the order in which comments will be displayed. While parallel processing is often more efficient, depending on the number of participants, the number and complexity of the comments may soon become overwhelming unless appropriate measures are taken to manage the process.

Support for both a facilitator and participants also requires a multiple-workstation EMS. Processing may be sequential or parallel. An example of sequential processing is a Nominal Group Technique tool. After each participant generates his or her own list of comments (which is actually parallel processing), the facilitator controls the process by which separate comments are presented to the group. Participant support allows each group member to choose which comment to present to the group at a given time.

An example of parallel processing is brainstorming. The facilitator support again provides a means to control the process, and participant support allows each group member to generate and distribute comments simultaneously.

Methods that support participants only, or both the facilitator and the participants, have been developed from two complementary but quite distinct perspectives or philosophies. The first, which underlies the designs of many CSCW systems, typically sees a group as a small number (e.g., three or four) of tightly knit co-workers with a common sense of purpose (e.g., Stefik, et al., 1987). Group members are seen as very cooperative (e.g., working together on a proposal or mutually authored document). Changes can be quickly made in terms of editing the work of others, and authorship is generally recognized. Essentially, there is a sense of member equality, with electronic interaction often accompanied by a high degree of verbal exchange.

The second perspective, which is how some GDSSs have been designed, views a group in a task force context. In this case, the group is larger (e.g., 12 to 24), often with subgroups. The group typically has a common sense of purpose and culture but members are not necessarily as cooperative and egalitarian as those in a small group of co-workers. The environment is often politically charged, with many personal opinions, agendas, and vested interests present. Tasks are complex, with the necessity to garner input from a variety of perspectives and member knowledge domains (e.g., for corporate resource allocation, planning, or negotiation). Anonymity may be important to draw out true feelings, voting is commonplace, and support for a facilitator as well as participants is likely to exist. In large groups, sequential processing can be less effective as either the opportunity for equal participation is removed or as each person has less time in which to contribute.

These perspectives are not mutually exclusive. In reality, groups, whether they are ongoing, discretionary coalitions, or formed for an explicit purpose, exhibit a variety of characteristics as a function of task and member characteristics. Further, an individual member's behavior may vary substantially from group to group or session to session or even within a session. Equifinality is likely to exist, i.e., there are a number of ways to support a particular group. Though methods developed from either perspective are often used for similar situations, the EMS approach seeks to flexibly capture aspects of both of these philosophical approaches.

All of the above method types can be used to support a single group in a single meeting. With the addition of a knowledge base and other types of technological support, the same types of software can provide support for multiple group sessions. Such methods are increasingly emerging to facilitate integration of information across multiple sessions and between groups. Comprehensive communications support is provided with a variable and dynamic degree of structure based on intra- as well as inter-session attributes. Support for integrating information across sessions and between groups includes knowledge bases with “intelligent” access through easy-to-use interfaces. Additional access is provided to organizational and external information resources to support dynamic integration of relevant information.

Particular attention should be given to seamless integration between multiple session support methods and other organizational information functions (e.g., teleconferencing, computer conferencing, scheduling, and e-mail). These are the types of things a focus on EMS makes possible. The methods increasingly support “decision rooms without walls” in which organizational members can be participating in group sessions without the need to be continuously present in a single room. Many of the capabilities described in this article are only beginning to surface in some GDSSs but will become standard in fully evolved EMS systems.

## EMS toolkit

Many early GDSSs were task-driven, as defined by Huber (1984). They were designed to meet the needs of one group performing one task, and therefore addressed one, and only one, application of meetings. As discussed in DSS literature, these systems were specific GDSS applications (Sprague, 1980). For example, one early GDSS was designed specifically to assist in labor-management negotiation and could not be used for any other task (Kersten, 1985).

More recently, the need to provide a toolkit, similar to the concept of a DSS model base or tool set (Sprague, 1980), has become apparent. Toolkits are collections of specific tools that address various parts of the meeting's process. In the same manner as hammers and wrenches are used for different tasks, so are the specific tools provided in the toolkit. A toolkit can conceivably include tools of each type described above. EMS environments using toolkits are activity driven (Huber, 1984), i.e., they have components to support specific group activities (such as idea generation and voting), rather than one indivisible system to support the entire process of one meeting application (such as decision making or negotiation).

The key advantage provided by toolkits is flexibility. This flexibility is important in three ways. First, each tool in the toolkit will have its own meeting dynamics. One tool in the toolkit may support a highly structured interchange of ideas, while another tool may provide very little structure. Groups can choose which tool they prefer. Second, groups use many processes to achieve their goals; they often do not proceed in a straightforward manner to reach their goals (Bahl and Hunt, 1984). The tools in the toolkits can easily be mixed and matched, and used in whatever order the group believes is most effective to achieve its goals. Finally, the toolkit is also sufficiently flexible to enable new tools to be easily added. The flexibility of the toolkit approach is illustrated in Figure 6, in which each tool or group of tools is represented as a node in a network. Users may begin at any node and move to any other node in any order. Some of the tools depicted in Figure 6 are described below.

Examples of tools in the PLEXSYS toolkit include:

\- Session director — guides the facilitator or group leader in selection of the tools to be used in a session and generates an agenda. Default times and output reports are listed and may be modified at the group's discretion.

\- Electronic brainstorming — supports idea generation, allowing group members to simultaneously and anonymously share comments on a specific question.

\- Issue analyzer — helps group members identify and consolidate key focus items resulting from idea generation. Support is also provided for integrating external information to support identified focus items.

\- Voting — provides a variety of prioritizing methods including Likert scales, rank ordering, and multiple choice. All group members cast private ballots. Accumulated results are displayed.

\- Topic commenter — supports idea solicitation and provision of additional detail in conjunction with a list of topics. Each topic may have subtopics. Participants enter, exchange, and review information on self-selected topics.

![](/api/attachments/K6ABJB2C/fulltext/images/70eb65820863ae935b70953e7344c2dff95dae56f13023dbf3dd9c8fae2a644e.jpg)  
Figure 6. Network of Tool Use

\- Policy formation — supports the group in developing a policy statement or mission through iteration and group consensus.

\- Organizational infrastructure — provides support for capturing characteristics of organizational data sets, information systems, and structure to provide a foundation for impact analysis.

\- Stakeholder identification and assumption surfacing — is used to systematically evaluate the implications of a proposed policy or plan. Stakeholder assumptions are identified, scaled, and graphically analyzed.

\- Alternative evaluator — provides multi-criteria decision-making support. Alternatives can be examined under flexibly weighted criteria to evaluate decision scenarios and tradeoffs.

The choice of tool will dramatically affect the meeting process and therefore the outcome of the meeting. Likewise, selecting the best combination of tools — the meeting agenda — is also crucial. For each stage in the process, the group can select one tool from a set of possible tools, depending on which specific group technique it wishes to use. One of the most important activities of any group process is the premeeting planning. Key tasks during this step are setting the objectives for the meeting, ensuring that participants understand these objectives and the roles they will play, and designing the agenda to meet these objectives. These activities can be supported by an agenda tool. The agenda tool may be a simple DSS, or an expert system could be built by using decision rules for setting meeting agendas. Alternately, setting the agenda could be sufficiently complex to require a separate planning meeting supported by EMS.

The organization of the tools to support group processes and tasks is facilitated in the system architecture illustrated in Figure 7. As the figure shows, the output from the tools serves as input to a knowledge base that provides a mechanism for representing and storing the planning knowledge using a variety of knowledge representation techniques that include semantic inheritance networks, frames, and production rules (Applegate, et al., 1987; McIntyre, et al., 1987). The knowledge base approach facilitates multiple planning and decision process representations. The representations can change dynamically as new knowledge is added to the system. The knowledge base acts as a “meeting memory” as groups return for additional sessions and new members or groups seek to build on the output from previous sessions.

![](/api/attachments/K6ABJB2C/fulltext/images/43a8f9c5f850f8e7c29402792504119950b9b5f374605a70080fa8c0e7a7c2d9.jpg)  
Figure 7. PLEXSYS

## Implications from methods

On one level, the EMS environment determines the methods that can be used. For example, if the environment involves a single workstation, then the methods will be limited to facilitation-only support (where one individual enters all pertinent information from the group session) or to specific models or sets of models that can be run with data collected from the group during its meeting. Once the environment expands beyond one workstation, to the point where each individual in the group has access to a workstation, then the methods that can be used change. Group members can now enter data and comments simultaneously, enabling the use of tools such as electronic brainstorming.

Methods and tool development are ongoing processes. Maintenance is critical to the success of any EMS, but maintenance is extremely labor intensive and therefore expensive. The development and continuing support of EMS methods represent a considerable investment of labor, time and capital.

## Environments

Several authors have presented alternative classifications of GDSS. DeSanctis and Gallupe (1985) originally presented a framework using the dispersion of group members and duration of the decision-making session, which was later revised (DeSanctis and Gallupe, 1987) to use group member proximity (i.e., dispersion) and group size. Kraemer and King (1986; 1988) developed a more detailed classification that examines the hardware, software, orgware, and people aspects of GDSS. Burns and colleagues (Burns, et al., 1987; Rathwell and Burns, 1985;

Thomas and Burns, 1982) introduced the concept of distributed decision making, where several groups interact and exchange information asynchronously. Hale and Haseman (1987) used a similar approach by categorizing GDSS on two dimensions: local vs. distributed, and length of the decision process, whether of limited duration or ongoing duration. Jelassi and Beauclair (1987) categorized GDSS for small groups on three dimensions: face-to-face vs. non-face-to-face, group member proximity, and synchronous-asynchronous.

The next section of this article presents a classification of EMS environments based on the taxonomies discussed above. Each EMS environment is then discussed individually, followed by a discussion of important practical considerations in EMS environment design. The section ends with a series of implications from EMS environments.

## Taxonomy of environments

There are three distinctive dimensions that can be integrated into a taxonomy of EMS environments: group size, participant location, and the timing of the “meeting” (whether it is one or more sessions, or a series of asynchronous group exchanges) (Figure 8).

Group size is a relative concept. Most researchers would probably agree that a group of three or four members is small, while a group of 20 or more is large. But, beyond this, general agreement on what is “large” and what is “small” or even “medium” is difficult. In this article, we consider small groups to have 10 members or less and large groups to have more than 10 members.

Group proximity refers to one “logical” group, in the sense that all participants address the same task. Not all participants need to be present in the same physical location (i.e., part of one physical group). Group proximity has three levels that relate to group geographic dispersion. With the first case — multiple individual sites — the individual members of the group are physically separate, working in their individual offices or workstations. In the second case — one group site — all members of the group are physically together in one room. In the last case — multiple group sites — members of the group meet in separate locations in subgroups, and then these multiple subgroup meetings are interconnected via EMS.

![](/api/attachments/K6ABJB2C/fulltext/images/cbf5b4384d019fa3134f9dc00459b7fc21c028c49fcb13a57944cab3a733ddd9.jpg)  
Figure 8. Taxonomy of Environments

Regarding time, groups may meet synchronously (i.e., at the same time) or asynchronously (i.e., at different times). With EMS, traditional meetings, in the sense that participants actually meet at the same place and time, are no longer the only choice. Electronic mail and computer conferencing are examples of information technologies that enable individuals to move beyond the traditional limitations of time and space, but since much present use of these ITs support individual work, they lie outside the EMS area and beyond the scope of this review (e.g., Hiltz and Turoff, 1981). Where these two ITs directly support meetings, they can be considered EMS.

Providing examples of asynchronous work in the group environment beyond those mentioned above is more difficult, since few such environments presently exist. Burns and colleagues (Burns, et al., 1987; Rathwell and Burns, 1985; Thomas and Burns, 1982) provide a few examples where geographically dispersed groups can meet at separate times (perhaps due to time zone requirements). Each group works as a unit and then transmits its results to the other groups for consideration in their subsequent sessions. Very little research has been done in the area of asynchronous group “meetings,” but there is potential for creative applications of this technology. In the following discussions of the EMS environments, the issue of asynchronous group work will not be addressed explicitly.

## EMS environments

There are six basic categories of EMS environments, which can be used synchronously or asynchronously.

![](/api/attachments/K6ABJB2C/fulltext/images/63fb2478aaf7bc2a639e4a7073f5e1efedd5d25b9c7823e257d00e2f6a75c0ef.jpg)  
Decision Room

Presently, the most common form of the organizational meeting is one where a small group of participants meets together in one place at one time. This type of meeting can be supported by a Decision Room environment. The Decision Room typically contains a series of networked computer workstations, plus wide screen computer video projection screen(s) for public viewing of group information. As the group meets face-to-face at the same place and time, verbal communication is available in addition to electronic communication.

![](/api/attachments/K6ABJB2C/fulltext/images/f27251e61da2eb8530be8c71089613185b0084cc408281edd5b2b78b9acda93d.jpg)  
Legislative Session

A legislative session differs from a Decision Room only in size; it accommodates a larger group. While verbal communication is still possible with a large group, it is less effective. Either the opportunity for equal participation of all group members is removed, or, if equal participation occurs, participants have far less time in which to communicate their ideas and opinions than they would in an equivalent small group meeting. Therefore, in a legislative session, electronic communication, and the methods to support it become more important.

![](/api/attachments/K6ABJB2C/fulltext/images/3ee75a5fa7f21b5ed730f5979567e06bd62396292f74722b3b0ab1e89548b227.jpg)  
EMS Teleconference

When a small group meets in several separate group sites at the same time, EMS teleconferencing facilities could be used. This is similar to non-EMS supported teleconferences, but with the addition of information technology to facilitate communication. At each site, the participants have the same technology as is available in a Decision Room, but with the addition of a network to support electronic, voice, and video communication between the different sites.

![](/api/attachments/K6ABJB2C/fulltext/images/cfb0440c046a731f090a2fea13580b9c2319d55b558f3f6bbc037f570a9d4195.jpg)  
EMS Teleconference/Broadcast

For a large group meeting at several sites, the EMS support is similar. However, the purpose of the meeting might be different. For example, organizations sometimes use teleconferencing facilities to broadcast courses or special presentations from leaders to geographically dispersed parts of the organization. With EMS, these broadcasts can be supplemented with an electronic communication channel to enable two-way communication between the multiple group sites.

![](/api/attachments/K6ABJB2C/fulltext/images/364d9b7fd32e219cef5c4d2c3a406781e7de6a31a22b32f0c575c08a61465157.jpg)  
Local Area Decision Net

A Local Area Decision Net is used to support a small group of dispersed individuals working at different sites (such as their offices). While equivalent facilities to EMS teleconferences can be provided to each individual, the cost may be prohibitive. More likely, video and voice communication channels would be omitted, leaving the group to rely on electronic communication.

![](/api/attachments/K6ABJB2C/fulltext/images/9bfa45518ec142e840aa69ab29b4778c9fb91874c65cc69bddd8737a5b57d053.jpg)  
Computer Conference

In the context of EMS, computer conferencing differs only in size from a Local Area Decision

Net. Unlike more traditional forms of computer conferencing using a bulletin board-style interface, EMS computer conferencing also includes synchronous communication among group members, where participants can simultaneously read and write messages. Because computer conferencing involves a large group, the methods used to manage the group interaction once again become very important.

## EMS environment design considerations

Most systems developed to support meetings exist in one of three environments: Local Area Decision Net, Decision Room, or legislative session. PLEXSYS is currently being used in the latter two (Appendix B). The lessons learned from the design and use of these environments are relevant to EMS design and are discussed in the next sections under the headings of floor plans, public information display, workstation design, ergonomics, and support issues (George, et al., 1988).

## Floor Plan

Floor plan considerations include group size, facilitation/leader focus, group member line of sight, and communication issues including recognition of verbal as well as electronic exchange. The setting should be multi-purpose and flexible to better meet the needs of different group sizes and task environments. Opportunities to work in dyads on workstations should be supported. Seating should be arranged to provide opportunity for face-to-face interchange among the participants as well as facilitation/leader focus. Group member line of sight should permit easy viewing of front screen images as well as communication with other group members. Recognizing the need for verbal and electronic communication in the room is an additional consideration particularly in terms of technology noise suppression.

## Public Information Display

Public information display issues include front screen type and number, information format (e.g., text or graphics) multi-media presentation support, teleconferencing concerns, and provision of an electronic podium. Presentation media should provide a wide range of support and should not restrict decision-maker communication. Front screen projection of individual workstation screens and consolidation group information, audio and video recording, optical disk technology, electronic blackboards, and overhead projection systems all play a role in providing a full measure of presentation media support. Particular attention should be given to aspects of presentation support that might adversely affect decision-maker comfort and participation (e.g., poor screen legibility). An electronic podium is especially useful to coordinate multi-media presentations through a user-friendly interface.

## Workstation Design

Workstation design issues include layout of microcomputer/screen, space for papers/other work, software distributed on each workstation hard disk, and local area net (LAN) handling of voice, video, and gateways. Providing an electronic interface for each group member encourages all group members to participate and enhances the efficiency of that participation. Relying on a single workstation for the whole group is not always appropriate. If multiple workstations are used, each should have a high degree of local intelligence and “in residence” software options that provide end-user help, data capturing, and communications support capabilities. As such, each group member can maintain some independence while contributing to the group as a whole through an interface that is flexible and individually supportive as well as integral to the networked system. A high bandwidth local area network (LAN) is necessary to maintain high levels of performance to accommodate network demands in transmitting text as well as screens between individual decision makers. Our experience has shown that users expect to receive subsecond response for all activities. Gateways provide group decision-making support for situations in which the decision makers are geographically dispersed.

## Ergonomics

Ergonomics issues include characteristics of the room, such as heat, sound, lighting conditions, and seating, where the group decision making takes place. Ignoring the impact of the setting may destroy the very nature of the fragile environment in which successful group decision making is facilitated. Aesthetics that provide a measure of executive appeal in terms of comfort and familiarity allow decision makers to better focus on issues at hand. Carpeting, wall coverings, and furniture appropriate to organizational conference rooms provide a setting where decision makers can comfortably relate to complex organizational questions.

## Support Issues

Support issues include breakout and conference rooms, high quality printers and copiers, gallery seating for observers, handicap access, security, redundancy in hardware and easy data recovery, observation rooms, and time stamping of voice and data in conjunction with video taping. Breakout rooms adjacent to the main conference area or other ways to logically partition a larger group into small discussion groups are particularly useful in some situations, as is a small conference room for preplanning or session staging purposes. Fast hardcopy printout capabilities provide additional user support. Gallery seating is useful for observers as well as facilitation helpers and executive support staff personnel. Security and reliability are constant concerns. Observation rooms and time stamping of audio, video, and data for subsequent playback and analysis assist researchers to better understand the implications of technology assisted groups.

## Implications from EMS environments

The design of the EMS environment can affect the process and outcomes of a group meeting. In the same way that simple design factors (such as color) have been shown to affect human information processing, complex design factors (such as workstation design or the design of the public information display) can be expected to affect meetings. While it is likely that several environment designs may be equally appropriate, the design of the EMS environment must be compatible with the methods with which it will be used. For example, the use of anonymity has been shown to have an impact on the process and outcome of meetings (Connolly, et al., 1988). While anonymity is a feature provided by EMS methods, it is rendered ineffective if participants can observe the workstation screen(s) of another participant(s).

In the design of EMS environments, the need to facilitate communication among group members is key. There are three communication channels that need to be effectively integrated, although not every channel will necessarily be provided in every environment. First, participants have access to the electronic communication channel via a computer workstation, which provides individual access to information. This access is used to enter and retrieve information to support the individual's contribution to the group. Public display of information in the electronic channel is also typical (either via a large screen projection system or an on-screen public window at the individual's workstation), which enables the group as a whole to focus on specific pieces of information.

Second, the environment may support verbal communication, either through face-to-face communication of group members in the same room, or via a microphone/speaker voice channel for groups members not in the same room. While the microphone/speaker channel at first appears to have the most critical design issues, it is important not to overlook the effects of workstation placement, for example, in a Decision Room environment. Providing a spacing between workstations of 2 feet as compared to 5 feet can affect the ease and manner of verbal communication in the group.

Third, provision for video or “sight” communication may also be useful. Once again, while the design issues for non-face-to-face environments may be technically challenging, it is important not to overlook those of face-to-face environments, especially legislative sessions. Participants should be able to easily see each other and any public information display.

In addition, certain design issues are extremely important to the development of a GDSS Decision Room that is useful to real world groups. As a minimum, the overall facility design, multiple public screens, central file servers, and communication network speed must be considered.

The overall facility design includes aesthetics, lighting and the physical organization of the Decision Room. The room must be physically organized for flexibility (to accommodate groups of various sizes) and to facilitate the use by group members of various communication channels, from electronic to verbal. The ability to show the screens of individual workstations on a large-screen projector is important, as is the presence of more than one public screen. In addition, knowledge bases and databases, handled by central file servers, facilitate coordination and management of input from individual group members and serve as “organizational” memory from one session to another.

One current challenge in EMS research is to move beyond Decision Rooms, legislative session environments, and Local Area Decision Nets into the development of EMS teleconferencing and computer conferencing environments, i.e., “Decision Rooms without walls.” Such environments have the potential to reduce the need for all participants to be physically present at the same place for meetings, and thus may substantially reduce travel time and costs for geographically dispersed groups.

## Implications

What are the implications of EMS technology for organizations? Since few organizations have implemented EMS to date, the answers to this question are still unknown. However, the implementation of PLEXSYS in a multinational corporation provides some evidence from which we can extrapolate and make predictions. The patterns that have started to emerge are addressed in the following three sections: organizational productivity, meeting size, and decision participation.

## Organizational productivity

One pattern that has emerged over the past year from our study of the day-to-day use of PLEXSYS in a major multi-national electronics firm (Nunamaker, et al., 1989) is that PLEXSYS-supported meetings are more productive than similar meetings not supported by PLEXSYS. More than 30 PLEXSYS-supported projects were tracked from initiation to completion. All projects required substantially fewer meetings and fewer person-hours than budgeted to complete. While these observations may be due to inaccurate a priori time budgeting or measurement error, this organization has a history of accurate forecasting and measurement. Conversely, the improvement may also be due to the Hawthorne effect; meetings were simply more productive because a change — any change — was introduced. However, since projects were observed over a one-year period, this too is less likely.

Huber (1988) suggests that with more productive meetings, fewer meetings are expected per project in an EMS supported organization environment. This may result in a decline in the total number of meetings in organizations, or, as meetings become more productive, an increase.

While these person-hour savings are dramatic, the elapsed times from project initiation to project completion were reduced even more substantially — from several months to several weeks in some cases. This has even greater implications for organizational productivity. By reducing the elapsed time from project identification to completion, organizations can be more responsive and more productive. Problems can be resolved faster, and market opportunities can be analyzed and acted on before competitors are aware of them.

## Meeting size

Some observers (e.g., Huber, 1988) have argued that the use of GDSS technology will decrease the number of people involved in future meetings. Previous non-GDSS supported research generally shows that small groups are more effective and more satisfying to belong to (Shaw, 1981), and, therefore, the increased productivity introduced by GDSS will increase the strength of the forces acting to promote smaller groups. In contrast, our experience with PLEXSYS shows that it supports and even promotes larger groups in meetings (Dennis, et al., 1988; Nunamaker, et al., forthcoming 1989).

There are three forces acting to increase the size of group meetings. First, one may presume that the issue to be addressed by the group is one that could benefit from the increased domain knowledge and skills provided by the members in the group; otherwise, why form a group? Huber (1984) points out that the business environment is becoming increasingly complex, which increases the need for specialized domain knowledge and skills, and thereby increases the desired size of the group.

Secondly, Ackoff (1981) argues that it is important for those charged with executing a plan or implementing a decision to understand why the plan or decision was made. The best way to do this is to include as many of these people as possible in the group, again increasing the desired group size.

Finally, there are political reasons for increasing the size of the group. By including additional participants in the decision-making group, their support is more likely to be gained for the decision — or at least the blame spread! Likewise, some organizational participants may insist on being present in meetings to ensure that their constituencies are represented (in resource allocation groups, for example).

Prior to the introduction of IT to support meetings, research — and experiences of managers — demonstrated the need to constrain the size of group meetings to increase productivity. However, since PLEXSYS has shown the potential to increase group productivity (Nunamaker, et al., forthcoming 1989), the size of group meetings can be expected to increase with EMS use.

## Decision participation

As the size of group meetings increases the meetings have the potential to span several hierarchical levels in the organization (Dennis, et al., 1988; Nunamaker, et al., forthcoming 1989). Indeed, this has been one of the factors in increasing productivity at the multinational firm described above. Bringing all hierarchical levels involved in the decision together in one meeting can have several advantages, from getting faster organizational approval for decisions to improving organizational communication (Huber, 1988).

Better organizational communication occurs because senior management is more aware of day-to-day issues, and employees and junior management are more aware of long term issues. As one CEO explained three months after a GDSS-supported strategic planning meeting: "A lot of education happened that previously hasn't happened during one of these things . . . People walked in with narrow perceptions of the company and walked out with a CEO's perception" (Dennis, et al., 1988, p. 16).

Since EMS can enable more organizational levels to be represented in group meetings, it is expected that more organizational levels will be involved in the decision-making process. As a result, organizational decision making could become more participative. However, this does not necessarily suggest that more decisions will be made by groups rather than by individuals; rather, individual decision makers might be more inclined to solicit information and opinions from a supporting group before making decisions.

## Conclusions

Information technology support for meetings is a relatively recent focus of study in the IS field, but it is an area of great potential and opportunity. The area is sufficiently broad to merit a label that encompasses all of its major aspects, and we have suggested electronic meeting systems (EMS) as that term. EMS as a concept is a combination of both GDSS and CSCW, stressing the role of information technology instead of just computers, the support of meetings across time and space instead of just in one room at one time, and the support of various tasks instead of just decision making.

The EMS concept has three components: group process and outcome, methods, and environments. In looking at group process and outcome, we presented a research model for investigating EMS. The model illustrated the variables important to group process and outcome and how they are related to each other. We also reviewed the studies of GDSS that are relevant to EMS and identified four streams of experimental research as well as a recent focus on field studies. There remains too much variation across studies to make many definitive statements, but using IT to support meetings does seem to lead to better quality decisions and more equal rates of participation among group members. More work needs to be done in this area, especially since some findings, such as those dealing with group satisfaction, consistently differ between experiments and field studies. In general, however, studies in this area do point to the potential usefulness of IT to improve meetings.

Our typology of EMS methods, which includes software as well as the methodologies and procedures built into the software, categorized methods according to the support they provided. Methods can be designed to support the meeting facilitator alone, the group alone, or both together. This support can allow sequential or parallel processing, and it can be used for a single session or across multiple sessions. Providing all of this support within a single EMS can be done through the toolkit concept, which provides maximum flexibility for supporting meetings. The more varied the tools in the toolkit, however, the greater the need for a premeeting planning session.

Finally, under EMS environments, we introduced a taxonomy of 12 different environments that differ in terms of group size, time, and the proximity of group members. Even though 12 environments are possible in this taxonomy, most current environments are limited to Decision Rooms, legislative sessions, or Local Area Decision Nets. From experience, we have found that important design considerations for the former two environments include floor plan, public information display, workstation design, ergonomics, and support issues. For any environment, the need to facilitate communication is key, and this can be done through providing support for three communication channels: electronic, verbal and visual.

It is difficult at this time to predict with any certainty how the implementation of EMS will affect organizations. Based on the implementation of PLEXSYS in a multinational corporation, however, we predict that EMS will be able to improve organization productivity by decreasing the number and duration of necessary meetings. At the same time, the number of individuals involved in a particular meeting can increase without affecting the productivity of the meeting since EMS can be designed to successfully support large groups. Finally, EMS makes it possible to broaden the scope of a meeting to include participants from various hierarchical levels, thereby improving organizational communication and facilitating faster approval for decisions.

## Acknowledgements

The PLEXSYS EMS has been developed over the past years with the dedicated efforts of Linda Applegate, David Chappell, T. Chen, Annette Easton, Kimlynn Gridley, Bruce Hemiter, Benn Konsynski, Simon Leung, Ben Martz, Mark Pendergast, Ed Roberts, Bill Saints, Joe Valacich, and Lee Walker. This research was partially supported by grants from the IBM Management Of Information Systems program, and the Social Sciences and Humanities Research Council of Canada.

## References

Ackoff, R.L. Creating the Corporate Future, John Wiley & Sons, New York, 1981.

Adelman, L. "Real Time Computer Support for Decision Analysis in a Group Setting: Another Class of Decision Support Systems," Inter-

faces (14:2), March-April 1984, pp. 75-83.

Applegate, L., Chen, T.C., Konsynski, B.R. and Nunamaker, J.F. Jr. “Knowledge Management in Planning,” Journal of Management Information Systems (3:4), Spring 1987, pp. 4-38.

Bahl, H.C. and Hunt, R.G. "Decision-Making Theory and DSS Design," Data Base (15:4), Summer 1984, pp. 10-14.

Beauclair, R.A. "An Experimental Study of the Effects of Specific GDSS Applications on Small Group Decision Making," working paper, University of Louisville, Louisville, KY, December 1987.

Blosser, P. An Automatic System for Application Software Generation and Portability, Ph.D. dissertation, Department of Computer Science, Purdue University, West Lafayette, IN, 1976.

Burns, A., Rathwell, M.A. and Thomas, R.C. "A Distributed Decision-Making System," Decision Support Systems (3), 1987, pp. 121-131.

Bui, T.X. “Co-op: A Group Decision Support System for Cooperative Multiple Criteria Decision Making,” Lecture Notes in Computer Science Series: 290, Springer-Verlag, Berlin, 1987.

Bui, T. and Jarke, M. "A DSS for Cooperative Multiple Criteria Group Decision Making," Proceedings of the 5th International Conference on Information Systems, Tucson, AZ, November 28-30, 1984, pp. 101-113.

Bui, T., Sivasankaran, T.R., Fijol, Y. and Woodburg, M.A. "Identifying Organizational Opportunities for GDSS Use: Some Experimental Evidence," Transactions of the Seventh International Conference on Decision Support Systems, San Francisco, CA, June 1987, pp. 68-75.

Connolly, T., Jessup, L.M. and Valacich, J.S. "Idea Generation in a GDSS: Effects of Anonymity and Evaluative Tone," working paper, University of Arizona, Tucson, AZ, 1988.

Dennis, A.R., Heminger, A.R., Nunamaker, J.F., Jr. and Vogel, D.R. "Bringing Automated Support to Large Groups: The Burr-Brown Experience," working paper, University of Arizona, Tucson, AZ, August 1988.

DeSanctis, G.L. and Gallupe, R.B. "Group Decision Support Systems: A New Frontier," Data Base (16:2), Winter 1985, pp. 3-9.

DeSanctis, G.L. and Gallupe, R.B. “A Foundation for the Study of Group Decision Support Systems,” Management Science (33:5), May 1987, pp. 589-609.

DeSanctis, G.L. and Poole, M.S. "Group Deci-

sion Making and Group Decision Support Systems: A Three Year Plan for the GDSS Research Project," MIS Research Center Working Paper WP-88-02, University of Minnesota, Minneapolis, MN, September 1987.

Easton, A. An Experimental Investigation of Automated versus Manual Support for Stakeholder Identification and Assumption Surfacing in Small Groups, unpublished doctoral dissertation, University of Arizona, Tucson, AZ, 1988.

Easton, G.K. Group Decision Support Systems vs. Face-to-Face Communication for Collaborative Group Work: An Experimental Investigation, unpublished doctoral dissertation, University of Arizona, Tucson, AZ, 1988.

Gallupe, R.B., DeSanctis, G.L. and Dickson, G.W. "Computer-Based Support for Group Problem Finding: An Experimental Investigation," MIS Quarterly (12:2), June 1988, pp. 277-296.

Gallupe, R.B. and McKeen, J.D. "Beyond Computer-Mediated Communication: An Experimental Study into the Use of a Group Decision Support System for Face-to-Face versus Remote Meetings," Proceedings of the ASAC 1988 Conference, Halifax, Nova Scotia, pp. 103-116.

George, J.F., Nunamaker, J.F. Jr. and Vogel, D.R. “Group Decision Support Systems and Their Implications for Designers and Managers: The Arizona Experience,” Transactions of the Eighth International Conference on Decision Support Systems, Boston, MA, June 1988, pp. 13-25.

Gibson, D.V. and Ludl, E.J. “Executive Group Decision Support Systems Considered at Three Levels of Analysis,” Transactions of the Eighth International Conference on Decision Support Systems, Boston, MA, June 1988, pp. 26-38.

Goldhaber, G. Organizational Communication, William C. Brown, Dubuque, Iowa, 1974.

Gray, P. "Initial Observations from the Decision Room Project," Transactions of the Third International Conference on Decision Support Systems, Boston, MA, June 1983, pp. 135-138.

Gray, P., Aronofsky, J.S., Berry, N., Helmer, O., Kane, G.R. and Perkins, T.E. "The SMU Decision Room Project," Proceedings of 2nd International Conference on Information Systems, Cambridge, MA, December 7-9, 1981, pp. 122-129.

Hackman, J.R. "Effects of Task Characteristics on Group Products," Journal of Experimental

Social Psychology (4), April 1968, pp. 162-187.

Hale, D.P. and Haseman, W.D. "EECS: A Prototype Distributed Executive Communication And Support System," Hawaii International Conference on System Sciences, Kona, HI, January 1987, pp. 557-565.

Hiltz, S.R., Johnson, K. and Turnoff, M. “Experiments in Group Decision Making Communication Process and Outcome in Face-to-Face Versus Computerized Conference,” Human Communication Research (13:2), Winter 1986, pp. 225-252.

Hiltz, S.R. and Turoff, M. “The Evolution of User Behavior in a Computerized Conferencing System,” Communications of the ACM (24:11), November 1981, pp. 739-751.

Huber, G.P. “Issues in the Design of Group Decision Support Systems,” MIS Quarterly (8:3), September 1984, pp. 195-204.

Huber, G.P. “Effects of Decision and Communication Support Technologies on Organizational Decision Processes and Structures,” Proceedings of IFIP WG 8.3 Working Conference on Organizational Decision Support Systems, North-Holland, Amsterdam, 1988, pp. 317-333.

Hymowitz, C. "A Survival Guide to the Office Meeting," Wall Street Journal, June 21, 1988, p. 35.

Ives, B. and Olson, M. "Manager or Technician? The Nature of the Information Systems Manager's Job," MIS Quarterly (5:4), December 1981, pp. 49-62.

Jarvenpaa, S.L., Rao, V.S. and Huber, G.P. "Computer Support for Meetings of Medium-Sized Groups Working on Unstructured Problems: A Field Experiment," working paper, University of Texas, Austin, TX, January 1988.

Jelassi, M.T. and Beauclair, R.A. “An Integrated Framework for Group Decision Support Systems Design,” Systems, Objectives, Solutions in Information and Management (13:4), April 1987, pp. 143-153.

Jessup, L.M. “Group Decision Support Systems: A Need for Behavioral Research,” International Journal of Small Group Research, September 1987, pp. 139-158.

Jessup, L.M., Connolly, T. and Galegher, J. "The Effects of Anonymity on Group Process in Automated Group Problem Solving," working paper, University of Arizona, Tucson, AZ, 1987.

Jessup, L.M., Tansik, D.A. and Laase, T.D. "Group Problem Solving in an Automated Environment: The Effects of Anonymity and Prox-

imity on Group Process and Outcome with a Group Decision Support System," Proceedings of the 1988 Annual Meeting of the Academy of Management, Anaheim, CA, August 1988.

Karon, P. "PCs Enter the Conference Room," PC Week, November 17, 1987, pp. 51, 60.

Keen, P.W. and Scott Morton, M. Decision Support Systems: An Organization Perspective, Addison-Wesley, Reading, MA, 1978.

Kersten, G.E. "NEGO-Group Decision Support System," Information and Management (8:5), May 1985, pp. 237-246.

Kiesler, S., Siegal, J. and McGuire, T.W. “Social Psychological Aspects of Computer Mediated Communication,” American Psychologist, October 1984, pp. 1123-1134.

Konsynski, B. A Model of Computer-Aided Definition and Analysis of Information System Requirements, Ph.D. dissertation, Department of Computer Science, Purdue University, West Lafayette, IN, 1976.

Konsynski, B. and Nunamaker, J.F. Jr. "PLEXSYS: A System Development System," reprinted in Advanced System Development/Feasibility Techniques, J.D. Couger, M.A. Colter and R.W. Knapp (eds.), John Wiley and Sons, New York, 1982.

Kraemer, K.L. and King, J.L. “Computer-Based Systems for Cooperative Work and Group Decision Making: Status of Use and Problems in Development,” Proceedings of the 1986 Conference on Computer Supported Collaborative Work, Austin, TX, December 1986, pp. 353-375.

Kraemer, K.L. and King, J.L. "Computer-Based Systems for Cooperative Work," Computing Surveys (20:2), June 1988, pp. 115-146.

Kull, D.J. “Group Decision: Can Computers Help?” Computer Decisions, May 1982, pp. 70+.

Lewis, F.L. Facilitator: A Micro Computer Decision Support Systems for Small Groups, unpublished doctoral dissertation, University of Louisville, Louisville, KY, 1982.

Loy, S.L., Pracht, W.E. and Courtney, J.F. Jr. "Effects of a Graphical Problem-Structuring Aid on Small Group Decision Making," Proceedings of the Twentieth Annual Hawaii International Conference on System Sciences, Kona, HI, January 1987, pp. 566-574.

McGrath, J.E. Groups: Interaction and Performance, Prentice-Hall, Englewood Cliffs, NJ, 1984.

McIntyre, S., Konsynski, B. and Nunamaker, J.F. Jr. "Automated Planning Environments: Knowl-

edge Integration and Model Scripting," Journal of Management Information Systems (2:4), 1987.

Mintzberg, H. The Nature of Managerial Work, Harper and Row, New York, 1983.

Mosvick, R.K. “Communication Practices of Managers and Technical Professionals in Four Large-Scale High Technology Industries,” presented at the National Convention of the Speech Communication Association, 1982.

Mosvick, R.K. and Nelson, R.B. We've Got to Start Meeting Like This, Scott Foresman and Co., New York, 1987.

Nunamaker, J.F. Jr. “A Methodology for the Design and Optimization of Information Processing Systems,” in Systems Analysis Techniques, J.D. Couger and R.W. Knapp (eds.), John Wiley and Sons, New York, 1974.

Nunamaker, J.F. Jr., Konsynski, B.R., Ho, T. and Singer, C. "Computer Aided Analysis and Design of Information Systems," Communications of the ACM, December 1976.

Nunamaker, J.F. Jr., Applegate, L.M. and Konsynski, B.R. "Facilitating Group Creativity with GDSS," Journal of Management Information Systems (3:4), Spring 1987, pp. 5-19.

Nunamaker, J.F. Jr., Applegate, L.M. and Konsynski, B.R. "Computer-Aided Deliberation: Model Management and Group Decision Support," Journal of Operations Research, November-December 1988a.

Nunamaker, J.F. Jr., Konsynski, B.R., Chen, M., Vinze, A.S., Chen, I.I. and Heltne, M.M. "Knowledge-based Systems Support for Information Centers, Journal of Management Information Systems (5:1), Summer 1988b, pp. 4-24.

Nunamaker, J.F. Jr., Grohowski, R., Heminger, A., Martz, B. and Vogel, D.R. “GDSS Experience at a Corporate Site,” forthcoming in Proceedings of the Twenty-Second Annual Hawaii International Conference on System Sciences, Kona-Kailua, HI, forthcoming January 1989.

Poole, M.S., Siebold, D.R. and McPhee, R.D. "Group Decision-Making as a Structural Process," Quarterly Journal of Speech (7:1), February 1985, pp. 74-102.

Rathwell, R.A. and Burns, A. “Information Systems Support for Group Planning and Decision-Making Activities,” MIS Quarterly (9:3), September 1985, pp. 255-271.

Richman, L.S. "Software Catches the Team Spirit," Fortune (115:12), June 8, 1987.

Ruble, M.R. An Empirical Test of a Decision Support System in a Group Decision Making Environment, unpublished doctoral dissertation,

Arizona State University, Tempe, AZ, 1984.

Shaw, M.E. “A Comparison of Individuals and Small Groups in the Rational Solution of Computer Problems,” American Journal of Psychology (44:3), July 1932, pp. 491-504.

Shaw, M.E. “Scaling Group Tasks: A Method for Dimensional Analysis,” JSAS Catalog of Selected Documents in Psychology (3:8), 1973.

Shaw, M.E. Group Dynamics: The Psychology of Small Group Behavior (3rd edition), McGraw-Hill, New York, 1981.

Siegel, J., Dubrovsky, V., Kiesler, S. and McGuire, T. "Group Processes in Computer Mediated Communication," Organizational Behavior and Human Decision Process (37:2), April 1986, pp. 157-187.

Sprague, R.H. "A Framework for the Development of Decision Support Systems," MIS Quarterly (4:4), December 1980, pp. 1-26.

Steeb, R. and Johnston, S.C. "A Computer-Based Interactive System for Group Decision-making," IEEE Transactions on Systems, Man, and Cybernetics (SMC-11:8), August 1981, pp. 544-552.

Stefik, M., Foster, G., Bobrow, D.G., Khan, K., Lanning, S. and Suchman, L. "Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings," Communications of the ACM (30:1), January 1987, pp. 33-47.

Teichroew, D. and Hershey, E.A. "PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems," in Advanced System Development/Feasibility Techniques, J.D. Couger, M.A. Colter and R.W. Knapp (eds.), John Wiley and Sons, New York, 1982.

Teichroew, D., Hershey, E.A. and Yamamoto, Y. "The PSL/PSA Approach to Computer-Aided Analysis and Documentation," in Advanced System Development/Feasibility Techniques, J.D. Couger, M.A. Colter and R.W. Knapp (eds.), John Wiley and Sons, New York, 1982.

Teichroew, D. and Sayani, H. "Automation of Sys-

tems Building," in Systems Analysis Techniques, J.D. Couger and R.W. Knapp (eds.), John Wiley and Sons, New York, 1974.

Thomas, R.C. and Burns, A. "A Case for Distributed Decision Making Systems, The Computer Journal (25:1), January 1982, pp. 148-152.

Tubbs, S.L. A Systems Approach to Small Group Interaction, Addison-Wesley, Reading, MA, 1984.

Turoff, M. and Hiltz, S.R. “Computer Support for Group Versus Individual Decisions,” IEEE Transactions on Communications (30:1), January 1982, pp. 82-91.

Vogel, D.R. “The Impact of ‘Messy’ Data on Group Decision Making,” Proceedings of the Twenty-First Annual Hawaii International Conference on Systems Science, Kona, HI, 1988.

Vogel, D.R. and Nunamaker, J.F. Jr. "Health Service Group Use of Automated Planning Support," Administrative Radiology, September 1988.

Vogel, D.R., Nunamaker, J.F. Jr., Applegate, L.M. and Konsynski, B.R. "Group Decision Support Systems: Determinants of Success," Transactions of the Seventh International Conference on Decision Support Systems, San Francisco, CA, June 1987, pp. 118-128.

Vogel, D.R., Nunamaker, J.F. Jr., George, J.F. and Dennis, A.R. "Group Decision Support Systems: Evolution and Status at the University of Arizona," Proceedings of IFIP WG 8.3 Working Conference on Organizational Decision Support Systems, North-Holland, Amsterdam, 1988, pp. 287-304.

Watson, R., DeSanctis, G. and Poole, M.S. "Using a GDSS to Facilitate Group Consensus: Some Intended and Unintended Consequences," MIS Quarterly (12:3), September 1988, pp. 463-478.

Zigurs, I. The Effect of Computer Based Support on Influence Attempts and Patterns in Small Group Decision-Making, unpublished doctoral dissertation, University of Minnesota, Minneapolis, MN, 1987.

## About the Authors

Alan R. Dennis is a doctoral student in MIS at the University of Arizona. He received a bachelor of computer science degree from Acadia University and an MBA from Queen's University in Kingston, Ontario, and was a winner of the AACSB National Doctoral Fellowship. Prior to entering the Arizona doctoral program, he spent three years as a faculty member of the Queen's University School of Business, and has published several articles and book chapters. His current research interests include electronic meeting systems, decision support systems, and business graphics.

Joey F. George is assistant professor of MIS at the University of Arizona. He earned his bachelor's degree at Stanford University in 1979 and his Ph.D. in management at the University of California at Irvine in 1986. His research focuses on how computing affects work. His current research investigates the effects of electronic meeting systems (EMS) use on the group work process and its outcomes, EMS use in non-American cultures, the effects of computing on decision authority in organizations, and the effects of extensive computerization in work groups.

Leonard M. Jessup is a doctoral candidate in organizational behavior at the University of Arizona, with a minor in management information systems. He is a member of the Academy of Management and the Institute of Management Sciences. He received his B.A. in information and communication studies, and his M.B.A. from California State University, Chico. He has worked as a community relations director in the health care industry and as a sales engineer in the electronics industry. His research interests include small group research, process analysis, and automated group problem solving.

Jay F. Nunamaker, Jr., is head of the Department of Management Information Systems and is a professor of management information systems (MIS) and computer science at the University of Arizona. He received a Ph.D. from Case Institute of Technology in systems engineering and operations research. He was an associate professor of computer science and industrial administration at Purdue University. Dr. Nunamaker joined the faculty of the University of Arizona in 1974 to develop the MIS program. Author of numerous papers on electronic meeting systems, the automation of software construction, performance evaluation of computer systems, and decision support systems for systems analysis and design, he has lectured throughout Europe, Russia, Asia, and South America. Dr. Nunamaker is chairman of the Association for Computing Machinery (ACM) Curriculum Committee on Information Systems.

Douglas R. Vogel is assistant professor of MIS at the University of Arizona. He received his M.S. in computer science from U.C.L.A. in 1972 and his Ph.D. in MIS from the University of Minnesota in 1986, where he was also research coordinator for the MIS Research Center. His current research interests bridge the business and academic communities in addressing questions of the impact of management information systems on aspects of interpersonal communication, group decision making, and organizational productivity.

# Appendix A The History of Information Technology to Support Meetings at the University of Arizona

## The Systems Development Process

Each information technology system that has been developed to support meetings grew out of a unique development project. An examination of each project would reveal different starting points for research. An understanding of the historical starting points helps users and developers better understand the system's current state and underlying design. The systems developed under the PLEXSYS project at the University of Arizona are no different. The purpose of this appendix is to provide the necessary background information on the PLEXSYS project.

The underlying concept for PLEXSYS had its beginning in 1965 with the development of Problem Statement Language/Problem Statement Analyzer (PSL/PSA) as part of the ISDOS (Information System Design and Optimization System) project at Case Institute of Technology (Teichroew and Hershey, 1982). Nunamaker was involved in the project that led to PSL/PSA from its inception. The PSL/PSA process started with the assumption that the requirements were known, or the individual or group responsible for the systems building project was capable of stating the requirements. There was no emphasis on developing an organizational consensus on the “correct” set of requirements, because at the time, it was assumed that the systems analyst was in charge and would be able to satisfactorily define the systems requirements. The emphasis on involving the user in requirements analysis was not to develop for another ten years.

The collective wisdom of the ISDOS project at that time decided that it was more important to develop methods to reduce the time to build a system, starting with “the assumption of correct requirements” as a given. The rationale was that the “correct requirements” are not constant; they change with changes in the organization. The users themselves change with respect to what they think they need to do their job. The basic objective was to reduce the time from the initial statement of requirements until the target system was operational. Automation or computer support was envisioned for each task in the systems life cycle.

From this conceptual framework, developed by five doctoral students under the direction of Professor Daniel Teichroew at Case Institute of Technology, evolved a number of software tools for automating the systems building process. This approach utilizing computer support for the systems building process resulted in PSL/PSA in 1965 (Teichroew and Hershey, 1982) and later in PLEXSYS $^{1}$ (Konsynski and Nunamaker, 1982). In 1965-1968, three activities shaped the development of PSL/PSA and eventually the development of PLEXSYS: (1) The first version of the problem statement language and problem statement analyzer was developed by Nunamaker (1974) as input to a computer-aided systems analysis and design software package called SODA (Systems Optimization and Design Algorithm); (2) the prototype for the problem statement language was developed by John Paul Tremblay; (3) the prototype for the problem statement analyzer was developed by Paul Stephan. These three developments led to the PSL/PSA version, which was used by well over 100 organizations for documenting and analyzing the set of requirements for an information system (Teichroew, et al., 1982).

PSL/PSA is a tool for describing requirements of a system, recording the descriptions in machine-processable form, and storing them in a database (Figure 1a). With the PSL/PSA approach, data is expressed in a formal language called PSL. As PSL statements are entered into the database, PSA analyzes the statements for correctness, completeness, and consistency with data and information already present in the database. PSA then produces a set of reports that represent the combined views of the many analysts or problem definers working on the requirements. These reports describe the inputs, outputs and system flow along with system structure, data structure, data derivation, size, volume and systems dynamics.

![](/api/attachments/K6ABJB2C/fulltext/images/20099feda223a848f8880237db48975136294dec0d62dd0f7b168828185bafa3.jpg)  
Figure 1a. PSL/PSA

Next, Pat Blosser (1976) and Benn Konsynski (1976), doctoral students at Purdue University in the early 1970s, added procedural definitions to PSL to facilitate automatic code generation from PSL/PSA. This served to facilitate code generation and moved the systems specification process further from the user.

Nunamaker and Konsynski moved on to Arizona in 1974. During the process of using SODA/PSL, SODA/PSA and ADS/PSA (Accurately Defined Systems) (early prototypes of PSL/PSA) on a large project for the U.S. Navy, a change took place in their thinking (Nunamaker, et al., 1976). There were problems in depending on end users to utilize a formal language for requirements specifications. The end users at the Navy would not write their specifications in a PSL/PSA-like system, so an accounting firm was hired to work with the end users and write the specifications in the language. Insights gained from the deficiencies in this solution led to the development of the PLEXSYS concept. The idea was to develop a phase that came before the use of PSL/PSA, i.e., develop software to assist the users with the determination of requirements (Konsynski, 1976; Nunamaker, et al., 1988a). This phase would help developers determine what was needed in addition to the software in order to develop systems that would be used by the end users of the information system.

In many of the organizations Nunamaker and Konsynski worked with, the user group was represented by a steering committee or task force consisting of 10-20 people. It became clear in 1979 that a special meeting room was needed for the task force to use, or for the user group to meet to address the information requirements of an organization. The function of the room would be to display the system flows, data structures and information requirements on a large screen projection system and permit each user seated at a workstation to interact with the set of requirements and the proposed design of the system. The PLEXSYS-84 system, which was an extension of the PSL/PSA/ISDOS project, was a workbench/workstation environment for the system development team. A collection of integrated tools, procedures, transformations, and models were available to the systems developer to analyze and design systems. It was expected that PLEXSYS would shorten the life cycle of development by facilitating a fast implementation of a prototype system. It was recognized that the design process could not be completely automated and that PLEXSYS would be a computer-aided support system with databases, knowledge bases, model management and inquiry facilities. $^{2}$

## Appendix B Arizona's Decision Room Facilities

## 1st Facility — PlexCenter

Construction of the first computer-assisted group meeting facility at the University of Arizona began in 1984. The facility, which opened in March 1985, was conceived as a meeting room for end users, systems analysts, systems designers and project leaders to review and analyze system specifications and designs. As usage of the system progressed over the first 18 months of operation we found that the software was valuable in planning efforts of all types, not just information systems planning. In fact, the usage of the room shifted from requirements and design review to initial discussion of issues and problems. The participants in each session became the group responsible for decision making regarding the organization's goals and objectives relative to the task. The system was built for one particular audience but was found to be useful in a broader context.

The first facility, called the PlexCenter, houses a large U-shaped conference table with 16 computer workstations (Figure 1b). Each workstation is recessed for line-of-sight considerations and to facilitate interaction among participants when appropriate. A BARCO large screen (10ft.) projection system can display screens of individual PCs. In addition, a video switcher facilitates the movement of screen images from PC to PC or downloads the public screen (facilitator's) display to each workstation. The facility includes four breakout rooms, also equipped with PCs, for small group discussion. PLEXSYS software consists of a large number of tools, including tools for brainstorming, issue analysis, voting, stakeholder identification, assumption surfacing, and recording what happens during a meeting. The facilitator's station provides access to and control over the group support tools. The facilitator helps the group get the most out of the GDSS process by both guiding the meeting and running the software. The interfaces have been set up so the user can understand the screens that appear even if they have not seen a particular screen previously. The system, written in Turbo PASCAL, uses pop-up menus, cursor selection from menus, and keyboard instructions to communicate with the user.

Based on insights gained from the operation of PlexCenter, it was decided to build a second facility. The success of using PLEXSYS in small and medium groups suggested that larger groups might benefit even more, so the second facility was designed to accommodate large groups. Over the first eighteen months of operation, it was observed that satisfaction of the group with the use of the system increased with group size. This led to the desire to build a larger facility to test the hypothesis that “satisfaction using the system increases with group size.” In addition, building a new facility provided an opportunity to improve the facility design, to develop a new systems architecture, and to take advantage of recent technological developments.

$^{2}$ As far as we know, based on the literature and usage of software tools, the first set of CASE (computer-aided software engineering) tools, namely PSL/PSA, came from Case Institute of Technology in 1965-68. At that time only Teichroew's group of Case, which later moved to the University of Michigan, was concerned with computer-aided support of the systems development process. It is ironic that 15 years after the development of PSL/PSA, this type of tool came to be known as CASE tools. Here, we recognize Teichroew as the originator of CASE tools.

![](/api/attachments/K6ABJB2C/fulltext/images/c4551333db2e545b2fbf07fb2b230fde14432e95831e5ef028d2214159b4cfa0.jpg)  
Figure 1b. PlexCenter

## 2nd Facility

The second Arizona facility designed to support group work with information technology was opened in November, 1987. The room was designed to accommodate 24 workstations with space for two people per workstation (Figure 2b). In addition, gallery seating for 18 observers was included in the back of the room. The room has a distinct legislative feel to it but it also facilitates talk across the room, if appropriate. The 24 workstations house IBM PS/2 model 50s with high resolution color monitors. The room is equipped with 38 audio pick-up microphones and six video cameras with stereo audio capability. In addition to the two large screen displays, a high resolution video projector with a remote control unit displays computer (analog and TTL) and NTSC video signals. This system permits display of laser disc, transparencies, videotapes, 35mm slides and Videoshow 160, a computer graphics presentation system with special effects.

A separate control room was built to house TV monitors, audio mixers, and video editing equipment for monitoring and processing session recordings. The capability exists to capture the computer inputs from all participants as well as audio and video recording of a session. Years later, a replay of a key corporate discussion or decision could be reproduced. This capability would provide tremendous insight for changes to corporate strategy, planning, etc., in the future.

## Future Plans

The result of our experiences (Nunamaker, et al., 1988a) has led us to consider the next phase in the development of information technology to support meetings, which is to distribute some of the functions of the collaborative meeting room to a participant's office. It is not necessary to bring everyone together in the electronic meeting room for each task. We are also planning to support groups distributed around the country and the world.

![](/api/attachments/K6ABJB2C/fulltext/images/67c051079cd91163cfbd6544d40fb837ad40cc4d787ff1cd6a26b12bffa635c4.jpg)  
Figure 2b. Decision Room for Larger Groups

In the near future, we will integrate PLEXSYS software tools with a videoconferencing system in order to test the concept of distributed meeting room facilities. The first step is to connect our two GDSS facilities with electronic and video links.

We envision a facility in which the scenarios are the same as those in our first and second rooms, but participants are located thousands of miles away. Imagine a facility in which your group is sitting in the center of a circular room. The walls of the room are covered with screens of the participants from around the world. Each local group would find themselves in the center of all participants.
