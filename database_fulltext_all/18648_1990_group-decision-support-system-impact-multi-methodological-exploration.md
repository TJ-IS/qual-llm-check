---
otero_id: 18648
otero_key: "96URYXBV"
title: "Group Decision Support System impact: Multi-methodological exploration"
authors: "Doug Vogel; Jay Nunamaker"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90060-u"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Jay. F. Nunamaker, Jr. is Head of the Department of Management Information Systems and is a Professor of Management Information Systems (MIS) and Computer Science at the University of Arizona. He received a PhD from Case Institute of Technology in systems engineering and operations research. He was an Associate Professor of Computer Science and Industrial Administration at Purdue University. Dr. Nunamaker joined the faculty at the University of Arizona in

# Group Decision Support System Impact: Multi-Methodological Exploration

Doug Vogel and Jay Nunamaker

College of Business and Public Administration, University of Arizona, Tucson, Arizona 85721, USA

This paper documents multi-methodological exploration of the impact of Group Decision Support Systems. Examples of our studies are used to illustrate the use of six methodologies: mathematical simulation, software engineering, case, survey, field study, lab experiment, and conceptual (subjective/argumentative) based on an established taxonomy of MIS research methods. Examples of syncrgism attained through use of a multi-methodological approach are provided.

Keywords: Group decision support systems, GDSS, MIS research methodologies.

![](/api/attachments/96URYXBV/fulltext/images/ad605df53f69a2ba24f10a497e9ac7778568ef3ac893d8f20d890d5ba97a376a.jpg)  
Douglas R. Vogel is an Assistant Professor of MIS. He has been involved with computers and computer systems in various capacities for over 20 years. He received his M.S. in Computer Science from U.C.L.A. in 1972 and his PhD in Business Administration from the University of Minnesota in 1986 where he was also research coordinator for the MIS Research Center. His current research interests bridge the business and academic communities in addressing questions of the impact of

management information systems on aspects of interpersonal communication, group decision making, and organizational productivity. Dr. Vogel is also responsible for coordinating University of Arizona electronic meeting system research activities.

## Introduction

The study of Group Decision Support Systems (GDSS) has broadened considerably over the past years. Seven years ago, discussion was focused on “decision rooms” (e.g., Gray, 1981) and suggestions of the impact that group decision support systems could make (e.g., Huber, 1982). Huber (1984) noted that a GDSS consists of a set of software, hardware, and language components and procedures that support a group of people engaged in a decision-related meeting. DeSanctis and Gallupe (1985) defined GDSS as integrated computer-based systems which facilitate solution of semi- or unstructured problems by a group that has joint responsibility for making the decision.

More recent GDSS research and experience has recognized a much broader application and role of automated support for groups. Kraemer and King (1986) note that “GDSS’s have expanded in scope considerably in recent years to include other group activities besides decision making. Chief among these are communication and information processing.” Paul Gray (1986) suggested that the term Group Deliberation Support Systems might be more appropriate than Group Decision Support Systems recognizing the expanded functions that GDSS encompass. Wagner (1988) has suggested the name Group Process Support System. Vogel, Nunamaker, and Konsynski (1988) have suggested simply using the name Group Support Systems without any qualifiers. A National Science Foundation workgroup defined GDSS as the application of information technology to support the work of groups with a focus on improving group performance and organizational effectiveness.

![](/api/attachments/96URYXBV/fulltext/images/a25d1739ec7a600444824291b14aeabc2ed59f3da38062a5e2e85bce8aa17de2.jpg)  
1974 to develop the MIS program. He has authored numerous papers on group decision support systems, the automation of systems, decision support systems for systems analysis and design, and has lectured throughout Europe, Russia, Asia, and South America. Dr. Nunamaker is Chairman of the Association for Computing Machinery (ACM) Curriculum Committee on Information Systems.

Overall, GDSS are now recognized as supported searching for alternatives, communication, deliberation, planning, problem solving, negotiation, consensus building, and vision sharing, as well as decision making for group members not necessarily in the same place or at the same time. The question then becomes: what, if anything, differentiates GDSS from automated support for cooperative work? GDSS seem very much in concert with automated support for cooperative work with some distinguishing features. Foremost among these is that GDSS are often applied in larger group situations, where group members are not necessarily cooperative; e.g., for negotiation and in situations where hidden agendas exist or where certain members seem overly dominant and there is an unwillingness of members to publicly share certain information.

This need to deal with larger collaborative (but not necessarily cooperative) groups should influence the design of GDSS. Features such as anonymity and inability to alter or delete other member input are sometimes advocated. Private voting is promoted and supported in several ways. Dominance of a group by a single member or coalition is diffused through participation of all members. Facilitation support is provided. Inclusion and integration of information external to the group is supported. Attention is given to information integration within and across group sessions (Martz, Nunamaker, and Vogel, 1987).

This paper documents a multi-methodological exploration of the impact of GDSS. Examples of studies at the University of Arizona GDSS facilities are used to illustrate the use of six methodologies: mathematical simulation, software engineering, case, survey, field study, lab experiment, and conceptual (subjective/argumentative) based on a taxonomy of MIS research methods. Synergism from application of multiple methodologies are discussed. The multimethodological approach is advocated to facilitate study of the complex nature of GDSS impact.

## Abbreviated History of GDSS Research

The focus of this history of GDSS research is on electronic meeting room environments with multiple workstations. Research addressing single workstation environments (e.g., Shakum, 1987, Bui, et al., 1987) or computer conferencing oriented (e.g., Hiltz and Turoff, 1981) is not included. GDSS research in electronic meeting environments with multiple workstations includes five overlapping perspectives: (1) the domain and applicability of GDSS, (2) facility development, (3) research agenda, (4) GDSS evaluation and experimental results, and (5) operationalized use of GDSS. Each provides focus on particular aspects of GDSS and feedback that impacts the other perspectives.

## GDSS Domain and Applicability

Early papers described opportunities for applying technology to address group needs. For example, the SMU Decision Room Project (Gray, et al., 1981) attempted to determine how to integrate new information technologies into group decision making by senior executives. Attention was given to the nature of group decision making is business and how technology might be provided, physically arranged, and supported to be effective. Subsequent efforts have been carried out at the Claremont Graduate School (Gray, 1986) with additional attention to software and communication issues. Issues of group dynamics were particularly addressed. Huber (1982) has noted that:

Actual Group Effectiveness

= Potential Group Effectiveness

\- Group Process Losses

\+ Group Process Grains

Potential Group Effectiveness occurs when the problem solving group accomplishes its tasks with the members generally satisfied and without impairing capacity of the group to function in the future. Group Process Losses involve loss in quality because some members are not encouraged to contribute their knowledge. This can result from domination by other members, group pressures for conformity, mis-communication, and/or failure to explore alternative generation steps in the decision process. Losses can also occur because of conflicting environmental factors, inadequate technological support, and ineffective group leadership. Group Process Gains include the better decision quality because members think of new and useful ideas through the contribution of other members. Automated support for group decision making strives to offset process loss through group process gains.

Much research has focused on the development of group techniques designed to overcome dysfunctional problem solving behavior. Three methods – brainstorming, the Delphi technique, and the Nominal Group Technique – have been used to stimulate the problem-solving capabilities of group (Huber, 1980). Other techniques have been offered that present a variation, or combination, of these three methods. All exhibit structure that, in part, can be (and has been) supported with computer technology. Each is designed to address problem solving process deficiencies. Efforts have extended to prescribing GDSS characteristics and applicability from an organizational perspective (Huber, 1984). Huber and McDaniel (1986) have suggested a “decision-making paradigm of organizational design” where decision making includes the sensing, exploration, and definition of problems or opportunities, as well as the generation, evaluation, and selection of solutions.

## Facility Development

Facility development includes issues pertinent to the GDSS setting: hardware, software, and "orgware". The setting for group decision making, in terms of room furnishings, lighting, group member arrangement, and general atmosphere, has been assumed to impact group processes (Brembeck and Howell, 1976; Gray, 1981; Vogel, 1986). Hardware and software are vital components of any GDSS. A number of authors (e.g., Huber, 1984; DeSanctis and Gallupe, 1985, DeSanctis and Gallupe, 1987; Nunamaker, Applegate, and Konsynski, 1987) have noted interrelationships between facilities and group processes. The term "orgware" has been used by Kraemer and King (1986) to include “the organizational data, group processes for decision-making, and management procedures for collaborative group work.” It is increasingly moving from the domain of the facilitator to that of the system and facility as GDSS structure, robustness, and application of artificial intelligence increase.

Numerous configurations have been described (e.g., Gray, 1981, 1986; Kull, 1982; Vogel, et al., 1986). Martz, Nunamaker, and Vogel (1987) have taken a systems theory perspective. One example is in automated support for stakeholder identification and assumption surfacing (Applegate, 1986), based on the work of Mason and Mitroff (1981) focusing on dialectical inquiry and impact analysis in conjunction with assumption surfacing and testing. Their work, in turn, reflects some of Churchman's considerations for the meaning of a system (Churchman, 1968). Issues of requisite variety are of particular concern. Additional systems modelling focus is exemplified is research on semantic inheritance networks, frames, and production rules. (Kottemann and Konsynski, 1984; McIntyre, Konsynski, and Nunamaker, 1987).

## Research Agenda

Kraemer and King (1986) provide an overview of the kinds of systems configured to meet the needs of groups. They identify six types of GDSS: electronic boardroom, information center, teleconferencing facility, decision conference, local area group net, and collaboration laboratory. They also elaborate elements of hardware, software, organization ware, and people for each type of GDSS. More recently, Straub and Beauclair (1988) conducted a survey of 135 organizations and suggested that GDSS are gradually being incorporated into information system portfolios. In particular, they noted that GDSS application seems to fall into three major categories: planning, administrative, and data analysis tasks each with a different form of GDSS. They concluded that organizations are increasing their commitment to GDSS, especially in situations where opportunities exist for integration of computer conferencing and electronic mail.

Research agenda have been suggested by many authors. DeSanctis and Gallupe (1987) have called for GDSS research in six areas: (1) GDSS design, (2) patterns of information exchange, (3) the mediating effects of participation, (4) the effects on perceived physical proximity, interpersonal attraction, and group cohesion, (5) the effects on power and influence, and (6) the performance/satisfaction tradeoff. They identify major constructs for study in each area, and add that more clearly defined constructs and hypotheses are needed. Jessup (1987) proposed a behavioral research agenda for GDSS focusing on three levels: individual, group, and situational. He called for research into the effects of individual characteristics, anonymity, different decision making strategies and social contexts, and different task and incentive systems. Vogel, Nunamaker, and Konsynski (1988) have suggested particular focus on the nature and impact of the interaction of user profiles, task characteristics, and technological capability.

## GDSS Evaluation and Experimental Results

GDSS environments supported by a single workstation for the whole group and situations where manual activities have been computer supported to some extent have preceded the current multi-workstation GDSS emphasis. In particular, Warfield (e.g., 1973, 1976) has provided a sound foundation. His work on societal systems and complexity apply a systems approach to societal problems that includes several different analysis methods, e.g., interaction matrices and impact structures. Warfield's (1976) Idea Management incorporates the subprocesses of Idea Generation and Idea Structuring. The focus of this section, however, will be on evaluation and experimental results associated with multi-workstation GDSS environments in which the participants are individually supported with technology which is interconnected to provide opportunities for electronic exchange and accumulation of information.

Empirical studies have tended to be controlled laboratory experiments with student subjects making up inexperienced groups. Research tasks typically have qualitative text-oriented aspects that require group member judgement and interpersonal communication to arrive at a conclusion. For example, Lewis (1982) concluded that GDSS support was superior to no support and structured paper-and-pencil support in terms of producing higher quality decisions, generating more alternatives, and reducing domination by single group members. Gallupe (1985) found that GDSS supported groups produced a higher quality decision, particularly in high-difficulty tasks but that confidence in the decision and satisfaction in the process are reduced when a GDSS is used regardless of the task difficulty. The GDSS was rather primitive, though, by contemporary standards and there may have been confusion on the part of the subjects with the appropriate use and role of the technology. Watson (1987) examined the impact of group size (3 or 4) and GDSS structure (none, manual structure, automated structured support) on aspects of decision maker confidence, member dominance, and satisfaction with a resource allocation task. He concluded that the GDSS did not significantly increase group consensus, perceived decision quality, equality of influence, or satisfaction with the solution. Zigurs (1987) analyzed the effect of computer based (versus structured manual) support on influence attempts and patterns in small group (3 and 4 person) decision making. She concluding that there was no significant difference in the total amount of influence behavior between GDSS and non-supported groups but that the distribution of influence was more even in the GDSS groups. Whether these results would hold for larger groups (e.g. 8 person and up) under varying “political” conditions remains a research question.

Overall, evaluative studies of GDSS impact have addressed many quantitative and qualitative measures, as illustrated in Table 1 for some GDSS dissertations.

Table 1

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td># of Alternatives</td><td>x</td><td>x</td><td></td><td></td><td></td><td>x</td></tr><tr><td>Participation</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Decision Speed/Time</td><td></td><td>x</td><td>x</td><td></td><td></td><td></td></tr><tr><td>Influence Behavior</td><td>x</td><td></td><td>x</td><td>x</td><td>x</td><td></td></tr><tr><td>Consensus</td><td></td><td>x</td><td></td><td>x</td><td></td><td></td></tr><tr><td>Decision Confidence</td><td></td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>Decision Quality</td><td></td><td>x</td><td>x</td><td>x</td><td></td><td>x</td></tr><tr><td>Behavioral Inhibitions</td><td></td><td></td><td>x</td><td></td><td></td><td></td></tr><tr><td>Process Satisfaction</td><td></td><td>x</td><td>x</td><td>x</td><td></td><td>x</td></tr><tr><td>Outcome Satisfaction</td><td></td><td>x</td><td>x</td><td>x</td><td></td><td>x</td></tr></table>

$\mathbf{A} = \mathbf{Lewis}$ (1982)

F = Easton (1988)

$\mathbf{D} = \mathbf{W}$ atson (1987)

Many different results occur due, in part, to differences in technology, task, group size, leadership, and other potentially interacting variables. A caveat also exists in terms of degree of experimental rigor, measurement sophistication, and accountability for confounding effects. In total, however, this represents a first step towards a better understanding of the impact of GDSS. We are still a long way, however, from understanding the implications of GDSS on group process and outcomes.

## Operationalized Use of GDSS

Increasingly, GDSS have extended beyond laboratory environments and are seeing operational use in business and community groups. For example, University of Arizona GDSS software has been used by hundreds of groups, domestic and international, at a variety of sites. Vogel, Nunamaker, Applegate, and Konsynski (1987) have presented determinants of success based upon extended use of an operational GDSS. They suggest that the key rests in an appreciation of the need for (1) facilities that provide a professional setting in which sophisticated software and hardware is well organized and effectively supported, (2) ability to accommodate groups of varying size, composition, and experience that address tasks are “real” and complex by nature, and (3) facilitation that demonstrates technical competence in combination with an appreciation of group dynamics and an orientation that encompasses a multidisciplinary approach. They conclude that failure to capture and implement facets of these three areas or recognize their inter-relationships can easily have adverse effects on GDSS effectiveness, efficiency, and user satisfaction.

Demonstrations of GDSS efficiency and effectiveness with groups that have little history of working together represents only one facet of GDSS impact. Operational use in a multi-national corporation, however, represents a large step towards GDSS maturity and acceptance in corporate settings. University or Arizona software is currently in day to day use at a 6,000 employee site of a major multi-national corporation. A room was built, software installed, and facilitators trained. Users have ranged from shop floor personnel to top executive levels. Experienced as well as ad hoc groups have used the facility in single and multiple sessions for a variety of tasks. Preliminary finding reflect significant savings in terms of number of meetings and group member time necessary to address complex questions (Martz, 1989).

## Discussion

Early papers describing the domain and applicability of GDSS have strongly influenced facility development. Survey papers and research agenda have helped guide use of the facilities in systematically evaluating GDSS impact. This has provided a foundation for successful operationalized use in corporate settings, providing experience and additional insight into the domain and applicability of GDSS. Thus the interaction of the areas influences the direction that GDSS are taking.

## University of Arizona Facilities

Our GDSS activities have involved software and facilities development to provide a strong foundation for empirical research. One example (Figure 1) has been operational since March 1985. It uses a large U-shaped table equipped with up to 16 networked microcomputers to facilitate interaction among participants. A microcomputer attached to a large screen projection system is also on the network; this permits display of material from individual workstations or aggregated information from the group. Break-out rooms are equipped with microcomputers networked to those at the conference table. Executives, managers, and professional staff use the facility for organizational planning and to address complex, unstructured problems. The facility has received considerable national and international attention. Fortune Magazine (June 8, 1987) noted that “managers like the candor the process allows, and the groups have been uniformly enthusiastic.”

A second facility (operational on November 7, 1987) capable of seating 60 participants is equipped with 26 networked microcomputers accompanied by a wide variety of audio/visual support. This facility, illustrated in Fig. 2, has extensive presentation support capability, including two large screen projectors that provide feedback to the group during sessions. The facility is organized in two raised tiers of workstations which can be “logically” subdivided; they use token-ring technology to support a single group or several smaller groups. The facility has a control room to integrate audio-visual and workstation activities, as well as the recording and time stamping of audio, video, and data for re-creation of sessions.

![](/api/attachments/96URYXBV/fulltext/images/dfa3284e3ed403ba9b897d68126ea1e743ca85bc3125e22dcff9d07843dd6974.jpg)  
Fig. 1.

Both facilities are used extensively for experimental data collection. In either facility, participants interact with a variety of automated tools to support individual and group planning, deliberation, and problem-solving. Examples of the tool kit capability include:

A Session Director tool to guide the facilitator or group leader in selection of the software to be used in a session and agenda generation. Default times and output reports are listed. These may be modified at the group's discretion.

An Electronic Brainstorming tool to support idea generation, allowing group members simultaneously and anonymously to share comments.

An Issue Analyzer tool to help group member identify and consolidate key focus items resulting from idea generation. Support is provided for integrating external information for consideration in focus items.

A Voting tool to provide a variety of prioritizing methods, including Likert scales, rank ordering, and multiple choice. All group members cast private ballots. Accumulated results are displayed in graphical and tabular format.

A Policy Formation tool to support the group in developing a policy statement or mission through iteration and group consensus.

A Stakeholder Identification and Assumption Surfacing tool to support systematic evaluation of the implications of a proposed policy or plan. Stakeholders' assumptions are identified, scaled, and graphically analyzed.

Additional tools support Delphi and Nominal Group techniques as well as alternative evaluation with multiple criteria and hierarchical topic decomposition. Integration with other software is supported. The tools can be arranged in a variety of patterns to meet the needs of user groups. The output serves as input to a knowledge base that provides a mechanism for representing and storing the planning knowledge using several knowledge representation techniques, including semantic inheritance networks, frames, and production rules (Kottemann and Konsynski, 1983; McIntyre, Konsynski, and Nunamaker, 1987). The knowledge base approach facilitates multiple planning and decision process representations. The representations can change dynamically as new knowledge is added to the system. The knowledge base acts as an “organization memory” as groups return for additional sessions and new members or groups seek to build upon the output from previous sessions.

![](/api/attachments/96URYXBV/fulltext/images/0a7845bc325b3a7ec6750fd2037556f3ba6da084e1ff8cf623f77492d71763bb.jpg)  
Fig. 2.

## Methodology Taxonomy and Examples

Our taxonomy is based on the work of Vogel and Wetherbe (1984), who evaluated a number of candidate categories and taxonomies before proposing a taxonomy of: theorem proof, engineering, empirical (with subparts case study, survey, field test, and experiment), and subjective/argumentative. The selection was based on criteria of comprehensiveness in coverage of MIS research, parsimony in proposing only four reasonably non-overlapping primary categories, and usefulness.

A more detailed list of methodologies has been proposed by Jenkins (1985) who suggested that it be categorized in terms of decreased strength of the methodology in hypothesis testing. His categories are math modeling, experimental simulation, laboratory experiment, free simulation, field experiment, adaptive experiment, field study, group feedback analysis, opinion research, participative (action) research, case study, archival research, and philosophical research. Galliers and Land (1987) have kept the Vogel and Wetherbe taxonomy as a core, but have suggested additional categories to promote increased attention to contextual considerations and interpretations beyond empirical or observational approaches. Their eleven categories are theorem proof, laboratory experiment, field experiment, case study, survey, forecasting, simulation, game/role playing, subjective/argumentative, descriptive/interpretive, and action research.

## Mathematical Simulation

Many opportunities exist for aiding GDSS operation in group environments. For example, electronic brainstorming involves the interchange of “n + 1” files, where “n” is the number of group members. (A file in this sense is equivalent to a sheet of paper that a group member accesses to append his or her comment to those of other members.) The extra file is provided to allow each group member to work at his or her own speed and still have work waiting as a group member finishes a comment. A statistical profile and distribution of file use is available in terms of time spend by group members.

Experience with use of electronic brainstorming, including monitoring of file use, suggests that periods of extreme non-randomness can occur in file interchange between group members. As such, a group member may not see all of the files during a session and/or may see a small group of files an abnormally high percentage of the time. The question then becomes whether inclusion of additional files beyond the “n + 1” or revision of the exchange protocol based on frequency of access by group member would tend to better randomize access of groups members as a whole to all the files in the group session. It would be helpful to have a mathematical model of electronic brainstorming that would examine alternative file dynamics, which could be examined in live groups.

Additional opportunities could address system integration aspects in the context of knowledge base use. Technological characteristics, including network bandwidth, can be modeled and investigated with respect to integration of external information as well as use of the network to transmit screen images among participants. This is particularly important when communication extends beyond the decision room to include members in remote geophysical locations.

## Software Engineering

Considerable research has taken a software engineering perspective. For example, Applegate (1986) utilized prototyping to design, implement, and evaluate technical feasibility of automated support for electronic brainstorming. Model management systems have been proposed to facilitate the management of organizational planning models in a manner similar to the management or organizational data (Konsynski and Dolk, 1982). Attention extends from support for strategic planning down though automated supported for information systems developments to meet strategic planning and other organizational needs. A Planning System designed to meet the need for providing information systems support throughout the planning process draws on the Plexsys knowledge base design described by Konsynski, Kottemann, Nunamaker, and Stott (1984).

More recent work has focused on the development of semantic guided interfaces to assist end users in accessing information for group deliberations (Valacich, Vogel, and Nunamaker, 1988). These interfaces provide a visual framework that supports directed perusal of knowledge base information. A graphics system is under development to create, examine, and modify knowledge base models. It employs a familiar financial spreadsheet user interface and displays knowledge base objects in a higher resolution graphic format. Additional software engineering research is focusing on the integration of multi-criteria decision making models with existing software (Hong, Vogel, and Nunamaker, 1987).

Overall, these efforts have been organized using a systems approach with attention to adaptivity, memory, feedback control loops, levels of abstraction, information aggregation, storage, and retrieval (Martz, Nunamaker, and Vogel, 1987). Feedback control loops have three primary functions: (1) Information to be stored is monitored to maintain internal consistency and prevent erosion of knowledge base integrity and credibility. (2) Operation of the system is monitored to record group member contribution and voting. (3) Accumulated group information is presented in various methods or views for group member reflection. An enterprise model comprising aspects of organization mission, environment, and internal structure is used to provide an integrated focus on relevant organizational information.

## Case studies

Case studies provide an opportunity to evaluate GDSS capabilities when used to address complex questions in organizational settings with groups of experienced decision-makers. Studies can be longitudinal as well as single session, with opportunities to capture impact on project productivity and the organization. Accumulated case studies provide a rich source of qualitative and quantitative information in the domain of applicability of GDSS as a function of task and organizational characteristics. Two examples are described here.

A health care group used our facilities to address planning needs in the face of increasing health care industry turbulence (Vogel and Nunamaker, 1987). Thirteen key members of the management and administrative group (including the CEO) addressed them in two sessions lasting 3 1/2 hours each. Tool use included Electronic Brainstorming, Issue Analyzer, Voting, and Stakeholder Identification and Assumption Surfacing. The first session focussed on identification and prioritization of key health care issues. The second focused on how a fixed amount of resources might be allocated over projects that the group had identified in the first session. Measurements included time of tool use, as well as participant feedback on the process and outcome. A followup was conducted four months later to ascertain what ideas had actually been implemented.

It was observed that the use of GDSS increased satisfaction and productivity in a work group setting by altering group communication patterns. Participants perceived that they were able to generate more ideas, be more creative, and better able to reach consensus when using the GDSS versus manual approaches. Comments from the group were that they had accomplished as much in 1 morning as they would normally accomplish in 2 days. Much of the process gains were attributed to anonymity, allowing ideas to be expressed freely and clearly. In the four month followup, it was noted that several ideas had been immediately acted upon and put in place.

A second case study involved a Fortune 1000 electronics corporation. The CEO and 30 members of his executive team and support staff used GDSS facilities for 3 days with audio visual presentations in conjunction with electronic brainstorming sessions, issue identification, and rank ordering of alternatives. Topics addressed included establishment or corporate performance expectations, critiques of divisional plans and budgets, consensus formation on how objectives were to be accomplished, and product and associated resource allocation decisions. The group concluded that the computer supported sessions were particularly helpful in establishing a stronger sense of understanding and agreement among a larger group of participants than had historically been achieved manually.

## Surveys

Surveys can be particularly helpful in ascertaining opportunities for GDSS application and penetration into corporate settings. As previously noted, Straub and Beauclair conducted a survey of organizations and determined that GDSS are gradually being incorporated into information system portfolios. In particular, they noted that these application seems to fall into three categories: planning, administrative, and data analysis tasks. They concluded that organizations are increasing their commitment to GDSS, especially in situations where opportunities for integration of computer conferencing and electronic mail exist.

A survey has focused on management of software projects to identify opportunities for effective application of group planning and DSS. Topics addressed include: (1) general characteristics of software project development, (2) characteristics of problems/opportunities in definition of projects, (3) characteristics of project planning and control, (4) staffing and management of human resources, (5) the effect of user feedback on project design and development, (6) reasons for cost overruns, (7) attribution for project delays, (8) use of project management tools/techniques, (9) actions taken to handle delayed projects, and (10) strategies employed to coordinate and control resources. Data has been collected and is being analyzed.

## Field Studies

As previously noted, software has been installed at one site of a large multinational corporation in a room specially constructed for evaluative purposes. Group facilitators and maintenance personnel have been trained. Internal procedures have been established for session pre-planning and reporting. The software is used for a variety of planning purposes including handling of shop orders, production control, product strategies, advancement opportunities, and internal systems. Group size is typically ten members, ranging from top level executives to plant foremen and line personnel. Measurements include on-line pre- and post-session questionnaires comparing the automated process to the manual process as well as systematic recording of perceptions of time saved in terms of project duration, number of meetings, and person-hours.

The efficiency and effectiveness of these methods have proved to be overwhelmingly positive. Project calendar days have been reduced by orders of magnitude. The number of meetings have been reduced accordingly. Person-hours expended have been dramatically reduced, with an average savings of 55% based on experience with comparable unsupported groups. Comments have praised the fairness and comprehensiveness of the process and a desire to use the facility in the future. Satisfaction measures have been especially positive. Group members consistently feel that the computer-aided process is better than the manual one in terms of ideas generated, goal achievement, commitment generation, fairness, and efficiency. The facility has never been advertised, yet is now fully booked with groups based on word-of-mouth of successful use.

Efforts are currently underway to standardize instruments to capture data that can be systematically evaluated across studies at five other GDSS sites. A “data collection and analysis” module has been developed to address four areas: (1) group member data, (2) session dynamics, (3) researcher analysis, and (4) longitudinal (multi-session) support. The support module consists of a flexible loosely coupled set of automated procedures that can be included or not at researchers discretion. Group member data collected with the module captures the range of perceptual and demographic information associated with GDSS studies. Collection of session dynamics data complements group member data in tracking information flows to facilitate determination of process impact during group sessions. Analysis support goes beyond capturing data for the researcher; longitudinal (multi-session) support provides a “research memory” component that allows comparisons and acts as a resource for meta-analysis as well as provides a basis for organizational justification for GDSS.

## Lab Experiments

Lab experiments include comparison of manual and automated support as well as studies of the impact of various characteristics of automated support. One study (Easton, 1988) has investigated the impact of the Stakeholder Identification and Assumption Surfacing tool based on the work of Mason and Mitroff (1981). Four person groups of students subjects were faced with the task of evaluating the implications of a campus policy advocating purchase of computers by business school students prior to enrollment at the University.

Another experiment examines the effects of anonymity and the evaluative context on group process and outcome when using a GDSS (Jessup, Galegher, and Connolly, 1987). Using students as subjects and a $2 \times 2$ factorial design, researchers manipulated anonymity (group member contributions were either identified or not) and the group's evaluative context (group members either focused on the positive or negative aspects). Preliminary results suggest that group members working under anonymous conditions tended to be more probing and critical of each other's ideas and that these actions generated more comments: apparently the GDSS acted as a buffer between group members, detaching them from their comments, thus enabling them to be critical of each other in a non-threatening way. Subjects reported in debriefing sessions that they liked the system because they felt criticism was addressed at ideas and not to them personally.

A related experiment using students was conducted to examine effects of anonymity and proximity Jessup, Tansik, and Laase, 1987). This was intended to understand the effects of the identifiability of group member contributions and the proximity of group members (either together in a decision room or dispersed) on group process and outcome. Preliminary results suggest that people working in a decision room tended to be more satisfied and likely to focus on positive aspects of other's ideas. Anonymous conditions had a higher level of perceived system effectiveness. Group members working under anonymity were also more likely to report their session production. Groups working in separate rooms, and to a lesser extent those working anonymously, generated more comments. Groups working anonymous-dispersed generated the most and shortest comments. These latter worked in a mode much like traditional brainstorming. Groups working under identified face-to-face conditions generated the least and longest comments: a mode more like natural discussion, with well-formulated comments.

## Conceptual

Two areas of conceptual (subjective/argumentative) research involve (1) the use of expert systems to apply captured facilitation expertise and (2) broadening task functionality and applicability. The first involves a threefold challenge: how to capture facilitation expertise, how to validate it, and how to integrate it into a system to be used by less experienced facilitators. Capture of expertise is complicated by a need to consider phases of GDSS support, involving pre-planning of sessions and monitoring of feedback that often involves visual clues to group dynamics. Validation of captured expertise is a problem in any expert system implementation. Providing real-time delivery of expertise to assist a less experienced facilitator without adversely affecting the group process presents a particularly interesting challenge.

Multi-criteria decision-making models are particularly relevant to extended GDSS. Group members have a broad spectrum of factors that are important when arriving at a final decision. Choice categories can be compensatory or noncompensatory (Minch and Sanders, 1986), reflecting the level of cognitive processing demanded by the decision maker. Additive and additive-difference models illustrate compensatory choice strategies (Wright and Barbour, 1977) where all available information is used and the search in exhaustive. Conjunctive, disjunctive, lexicographic ordering, and elimination-by-aspects models illustrate noncompensatory choice strategies where heuristics for selecting alternatives are used without having to process all of the available dimensional information (Tversky, 1972).

Our activities are interested in the nature of the user interface in providing a communications interface and interactive ability for individuals to contribute, share, and deliberate with a textual, qualitative focus in the context of multi-criteria decision making (Hong, Vogel, and Nunamaker, 1987). Interfaces may use only single workstation through which the group's input is achieved as opposed to having a workstation for each individual in the group. However, opportunities are missed in conjunction with failure to let the group of users become an active aspect of model assumption selection and weighting to reflect a particular organizational context.

## Methodology Synergism

Session results are systematically entered into a knowledge base to facilitate multi-session comparison and analysis. As such, group data can be integrated across a number of sessions and/or studied to provide a better understanding of the overall impact of automated support on groups. Ability to view the knowledge base information from multiple perspectives complements the richness of typical group data. Support for examining data from multiple sessions across multiple studies and accumulation of a knowledge base provides an opportunity to better understand the impact of automated support on groups. The knowledge base becomes a resource complementing personal analysis activities; it is supported through user-friendly semantic guided interfaces. Observation of problems in organizing the output of electronic brainstorming sessions led to software engineering efforts that resulted in the Issue Analyzer tool. This in turn has been used extensively to assist groups in planning and decision making tasks, as well as in experimental studies evaluating the impact of integration of external information into the context of group deliberations (Vogel, 1988). This, in turn, has prompted the development of additional software engineering support of better user interfaces and more comprehensive integration of knowledge base capabilities (Valacich, Vogel, and Nunamaker, 1987).

## What We Have Learned

Over the past three years, hundreds of group sessions, from four to 48 in size and covering a variety of tasks, have been conducted. Tasks have included strategic planning, mission formulation, idea generation, issue organization, decision making, negotiation, and information system specification. Groups have included variations of homogeneous, heterogeneous, naive, experienced, cohesive, seasoned, and demographic background. Our experience suggests that:

… Efficiency and effectiveness consideration of automated support become increasingly apparent as group size increases. As group size increases above four, automated support enhanced group efficiency by facilitating input from all group members in a relatively simultaneous fashion; i.e., human parallel processing. Members need not “wait their turn” to contribute to the question or problem before the group. For larger groups, effectiveness of automated support becomes particularly apparently in eliciting and organizing large numbers of issues associated with a complex question. Without structured automated support, larger groups tend to “falter” and fail to work efficiently or effectively.

... Anonymity varies in importance with the group and task characteristics. Anonymity is important when sensitive issues that can be confounded with personalities in the group are being discussed. For groups of differing organizational levels, of course, anonymity provides a sense of equality and encouragement for participation.

... Periods of face-to-face discussion focused around front screen displays are an important complement to individual workstation interaction. Groups in which the members are at similar levels, even if from different organizations, tend to keep discussion on a common 'level of abstraction. Groups in which the members differ widely in organizational level leads to discussion at multiple levels of abstraction in terms of detail within a given problem domain. Either may be appropriate depending on the nature of the decisions to be made.

... Tool use should be matched to the task at hand and be responsive to group characteristics and dynamics. The GDSS should not impose a rigid structure. Groups with common domain knowledge may wish to start with issue organization as opposed to idea generation. Many occasions exist in which voting is not appropriate or necessary for successful conclusion. When it is warranted, the group (in conjunction with the leader or facilitator) should be able to select member weighting and issue scaling appropriate to the question or problem. ... Problems of “group-think,” pressures for conformity, and dominance of the group by strong personalities or particularly forceful speakers are minimized. Members can contribute without the anxiety associated with being the focus of attention due to a particular comment or issue. Lack of keyboarding skills is not a deterrent.

... Member satisfaction with the group process is enhanced when the groups are larger. For larger groups, the effective and efficient reduction of equivocality on issues is more readily apparent. Larger groups appreciate the structuring of automated support that keeps the group from becoming “bogged down” and the efficiency of simultaneous human and machine processing. Members tend to “buy-in” and support the group solution with enhanced confidence that issues have been sufficiently explored.

… Use of a GDSS tends to heighten and diffuse conflict within the group. On the one hand, conflict is heightened as members tend to become more blunt and assertive: to express themselves more forcefully and not politely. On the other hand, the ability to consider the comments of others through a screen interface is less volatile than face-to-face encounter, is less threatening, and promotes a higher sense of appreciation for multiple perspectives.

## Conclusion

This paper has documented a multi-methodological exploration of the impact of Group Decision Support Systems. Examples of studies at the University of Arizona facilities have been used to illustrate the use of six methodologies: mathematical simulation, software engineering (including prototyping), case, survey, field study, lab experiment, and conceptual (subjective/argumentative) based on an established taxonomy of MIS research methods. The authors feel that the multi-methodological approach has been effective in dealing with the complex nature of the development and evaluation of GDSS. Through continued use of a multi-methodological approach, it is hoped that we can make better use of the best that humans and technology jointly have to offer in addressing complex questions.

## References

Applegate, L. "Idea Management in Organization Planning," Unpublished Doctoral Dissertation, University of Arizona, 1986.

Brembeck, W. and Howell, W. Persuasion: a Means of Social Influence, Englewood Cliffs, New Jersey; Prentice Hall, 1976.

Bui, T. et al. "Identifying Organizational Opportunities for GDSS Use: Some Experimental Evidence," Proceedings of the 7th International Conference on Decision Support Systems, June 8–11, 1987.

Churchman, C.W. The Systems Approach, Deli: New York, 1968.

DeSanctis, G. and Gallupe, B. "Group Decision Support Systems: A New Frontier," DATA BASE, Winter, 1985, pp. 3–10.

DeSanctis, G. and Gallupe, B. "A Foundation for the Study of Group Decision Support Systems," Management Science, 33(5), May, 1987, pp. 589–609.

Easton, A. “An Experimental Study of the Effectiveness of a GDSS for Strategic Planning Impact Analysis,” Unpublished Doctoral Dissertation, University of Arizona, 1988.

Galliers, R. and Land, F. “Choosing Appropriate Information Systems Research Methodologies,” Communications of the ACM, 30(11), November, 1987.

Gallupe, B. "The Impact of Task Difficulty on the Use of a Group Decision Support System", Unpublished Doctoral Dissertation, University of Minnesota, 1985.

Gray, P. et al. "The SMU Decision Room Project," Transactions of the First International Conference on Decision Support Systems, Atlanta, Ga., June, 1981, pp. 122–129.

Gray, P. “Group Decision Support Systems,” in Decision Support Systems: A Decade in Perspective, E.R. McLean, H.G. Sol (editors), Elsevier Science Publishers B.V.: North Holland, 1986.

Hiltz, S. and Turoff, M. "The Evolution of User Behavior in a Computerized Conferencing System," Communications of the ACM, 24(11): 739, 1981.

Hong, I.; Vogel, D. and Nunamaker, J. "A Knowledge-Based DSS for Supporting Multiple Criteria Decisions," University of Arizona Working Paper, 1988.

Huber, G.P. Managerial Decision Making, Glenview, I11. Scott, Foresman, 1980.

Huber, G. “Group Decision Support Systems as Aids in the Use of Structured Group Management Techniques,” DSS-82 Conference Proceedings, 1982, pp. 96–108.

Huber, G. "Issues in the Design of Group Decision Support Systems," MIS Quarterly, September, 1984.

Huber, G. and McDaniel, R. “The Decision-Making Paradigm of Organizational Design,” Management Science, 32(5), May, 1986, pp. 572–589.

Jenkins, M. “Research Methodologies and MIS Research,” in Research Methods in Information Systems, E. Mumford, et al. (editors). Elsevier Science Publishers B.V.: North Holland, 1985.

Jessup, L. “Group Decision Support Systems: A Need for Behavioral Research,” International Journal of Small Group Research, 3(2), September, 1987, pp 139–160.

Jessup, L.M., Galegher, J., & Connolly, T. "Group decision support systems: The effects of anonymity and the evaluative context on group process and outcome in an automated collaborative environment," University of Arizona Working Paper, 1987.

Jessup, L.M., Tansik, D., & Laase, T.D. "Group problem solving in an automated environment: The effects of anonymity and proximity on group process and outcome with a group decision support system," Proceedings of the Academy of Management 1988 Annual Meeting, Anaheim, CA, August, 1987.

Konsynski, B. and Dolk, D. "Knowledge Abstractions in Model Management," DSS-82 Transactions, 1982.

Konsynski, B., Kottemann, J., Nunamaker, J., Stott, J. "Plexsys-84: An Integrated Development Environment for Information Systems," Journal of Management Information Systems, 1(3), 1984.

Kottemann, J. and Konsynski, B. “Information Systems Planning and Development: Strategic Postures and Methodologies,” Journal of Management Information Systems, 8(3):195, 1983.

Kraemer, K. and King, J. "Computer-Based Systems for Group Decision Support: Status of Use and Problems in Development," Proceedings of the Conference on Computer-supported Cooperative Work, October, 1986, pp. 353–375.

Kull, D. "Group Decisions: Can a Computer Help?" Computer Decisions, 14, 1982.

Lewis, F. “Facilitator: A Microcomputer Decision Support Systems for Small Groups,” Unpublished Doctoral Dissertation, University of Louisville, 1982.

Martz, B., "Information Systems Infrastructure for Manufacturing Planning Systems," Unpublished Doctoral Dissertation, University of Arizona, 1988.

Martz, B.; Nunamaker, J.; and Vogel, D. “Group Decision Support Systems: An Engineering Management Perspective” U. of Arizona Working Paper, 1987.

Mason, R. and Mitroff, I. Challenging Strategic Planning Assumptions, New York: John Wiley and Sons, 1981.

McIntyre, S., konsynski, B., Nunamaker, J., “Automated Planning Environments: Knowledge Integration and Model Scripting,” Journal of Management Information Systems, forthcoming.

Minch, P. and Sanders, G. “Computerized Information Systems Supporting Multi-criteria Decision-making,” Decision Sciences, Summer, 1986, pp. 395–413.

Nunamaker, J.; Applegate, L. and Konsynski, B. “Facilitating Group Creativity: Experience with a Group Decision Support System,” Journal of Management Information Systems, 3(4), 1987.

Shakum, M. Evolutionary Systems Design: Policy Making Under Complexity and Group Decision Support Systems, Holden-Day, Inc.: Oakland, Ca., 1987.

Straub, D. and Beauclair, R. "GDSS Technology in Practice," MISRC Working Paper 88-03, University of Minnesota, September, 1987.

Tversky, A. “Elimination by Aspects: A Theory of Choice,” Psychological Review, 79, 1972, pp. 281–299.

Valacich, J.; Vogel, D.; and Nunamaker, J. "A Semantic Guided Interface for Knowledge Base Supported GDSS," Proceedings of DSS-88, June, 1988.

Vogel, D. "An Experimental Investigation of the Persuasive Impact of Computer Generated Presentation Graphics", Unpublished Doctoral Dissertation, University of Minnesota, 1986.

Vogel, D. "The Impact of "Messy" Data on Group Decision Making," Proceedings of the 21st Annual Hawaii International Conference on System Sciences, January 5–8, 1988.

Vogel, D. and Nunamaker, J. "Health Service Group Use of Automated Planning Support," Administrative Radiology, Sept., 1988.

Vogel, D. and Nunamaker, J. "Group Decision Support Systems: Evolution and Status," IFIPS Working Group 8.3 Conference on Organizational Decision Support Systems, June, 1988.

Vogel, D.; Nunamaker, J.; and Konsynski, B. "Group, Task, and Technology Interaction in a Group Support System Environment," forthcoming in the DSS Journal, 1989.

Vogel, D.; Nunamaker, J.; Applegate, L. and Konsynski, B. "Group Decision Support Systems: Determinants of

Success," Proceedings of the 7th International Conference on Decision Support Systems, June 8–11, 1987.

Vogel, D. and Wetherbe, J. “MIS Research: A Profile of Leading Journals and Universities,” DATABASE, Fall, 1984.

Vogel, D. and Wetherbe, J. "Profile of MIS Research: Methodology and Journal Preference," The Journal of Data Education, Spring, 1985.

Wagner, G. and Nagasundaram, M. "Meeting Process Augmentation: The Real Substance of GDSS," IFIPS Working Group 8.3 Conference on Organizational Decision Support Systems, June, 1988.

Warfield, J. "An Assault on Complexity," Battelle Monographs, 1973.

Warfield, J. "Societal Systems, John Wiley and Sons, 1976.

Watson, R. "A Study of Group Decision Support System Use in Three and Four-person Groups for a Preference Allocation Decision," Unpublished Doctoral Dissertation, University of Minnesota, 1987.

Wright, P. and Barbour, F. “Phased Decision Strategies: Sequels to an Initial Screening,” TIMS Studies in the Management Sciences, 6, 2977, pp. 91–109.

Zigurs, 1. “The Impact of Computer-Based support on Influence Attempts and Patterns in small Group Decision Making,” Unpublished Doctoral Dissertation, University of Minnesota, 1987.
