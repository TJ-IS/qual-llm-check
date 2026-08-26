---
otero_id: 18975
otero_key: "9CVKGQ5H"
title: "An investigation into knowledge acquisition using a group decision support system"
authors: "Yihwa Irene Liou; Jay F. Nunamaker"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90061-w"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# An investigation into knowledge acquisition using a group decision support system \*

Yihwa Irene Liou

University of Baltimore, Baltimore, MD, USA

Jay F. Nunamaker, Jr.

University of Arizona, Tucson, AZ, USA

Group Decision Support Systems (GDSS) previously have been used to facilitate a variety of group activities. This study explores the use of a GDSS to facilitate knowledge acquisition from multiple experts to build a help-service expert system for an information center. Observations from this study indicate that a GDSS can facilitate knowledge acquisition from a group of experts by documenting knowledge electronically, supporting parallel knowledge extraction from several experts, offering a structured process, and providing a collaborative atmosphere which facilitates group interactions, resolves conflicts, and enriches the domain of expertise. The findings show that structured analysis techniques are useful in planning for knowledge acquisition, the participation of end users is important, and that a designated primary expert is helpful when multiple experts are involved.

Keywords: Group decision support systems; Knowledge acquisition techniques; Knowledge acquisition from multiple experts.

## Introduction

Knowledge acquisition in the context of expert systems development can be broadly defined as the process of extracting, structuring, and organizing knowledge from human experts so that the problem-solving expertise can be captured and employed in a computer program. It is the most important task in the expert system development process because the power of an expert system derives from the knowledge it possesses, not from the particular formalism and inference schemes it employs $[14]$ .

Studies have shown that expert systems developed based on discussion with a single expert do not emulate most real-life decision making, while expert systems that are based on inputs from several experts may reflect multiple lines of reasoning [21]. These multiple views may enable the expert system to function more effectively than could any one of the individual domain experts who contributed expertise. Furthermore, knowledge acquisition from multiple experts is necessary when diverse subsets of knowledge are required and no single expert has complete knowledge of the domain.

This paper reports findings of an exploratory investigation into knowledge acquisition from multiple experts using a Group Decision Support System (GDSS) to build an information center help-service expert system.

## Prior research

Difficulties of the interviewing technique

Interviewing is the most commonly used knowledge acquisition technique. Its basic form involves question-answer sessions between the knowledge engineer and the expert. Such unstructured interviews are usually started by asking "How do you solve this problem?" Follow-up questions usually reflect further explanation or clarification of some of these expert's points. A

![](/api/attachments/9CVKGQ5H/fulltext/images/4048a491f690e213ef95e63981c5f85780b9b15fe02450fdb14abf01d00a449a.jpg)

Jay F. Nunamaker is Professor of Management Information Systems and Computer Science and Director of the Center for Management Information at the University of Arizona. His degrees include a B.S. from Carnegie Institute of Technology, a B.S. and M.S. from the University of Pittsburgh, and a Ph.D. in Operations Research and Systems Engineering from Case Institute of Technology. in 1969, as a professor at Purdue University, he became involved in developing a new program in Management Information Systems, which led to the opportunity to direct and build an MIS program at the University of Arizona in 1974. Today the MIS program at Arizona is regarded as a leader in the field. Professor Nunamaker is recognized for innovative research related to the automation of systems development, data bases, expert systems, systems analysis and design, strategic planning and group decision support systems. He has published more than 70 refereed papers and two books dealing with these subjects and has presented lectures and papers throughout the United States and in Europe, South America and Asia. Dr. Nunamaker's research has led to several major breakthroughs in automated systems analysis and design. With colleagues at Case Institute of Technology and later at the University of Michigan, Dr. Nunamaker was a member of the team that in 1965 outlined and clarified the concepts on which computer-aided information systems are designed. From his work on requirements definition, the importance of involving high-level executives in the process led to the development of GPLAN in 1972; a Decision Support System and PLEXSYS in 1980; a Group Decision Support System that assists decision makers, systems analysts, systems designers and users in the planning process. The developments provided the basis for two facilities that were built at the University of Arizona in 1985 and 1987. The GDSS software and facilities are now being used by a number of organizations on a daily basis for idea generation, issue identification, issue analysis, assumption surfacing, communication and consensus building.

![](/api/attachments/9CVKGQ5H/fulltext/images/e41044bdcb4d120d71abf79c8e6eb3341b7bf586e6d368ade83d913c10483640.jpg)

Yihwa Irene Liou is an Assistant Professor of MIS at the University of Baltimore. She holds a B.A. in philosophy from the National Taiwan University, an M.L.S. from the University of Southern Mississippi, and an M.S. and a Ph.D. from the University of Arizona in Management Information Systems. Her current research interests include the impact of group support systems on organizations, facilitation of team activities, Joint Appli cation Design, Computer-Aided Software Engineering, business applications of expert systems, and knowledge acquisition techniques. Her published work has appeared in Journal of Management Information Systems, Knowledge Acquisition, Journal of Organizational Computing, Expert Systems with Applications, and Data Base. She is a member of the AAAI, ACM, IEEE, TIMS, and DSI.

distinct advantage of free-form interviews is that knowledge engineers can follow unforeseen paths.

However, there are difficulties in this technique. First, as people become more experienced at performing their tasks, they become less aware of the cognitive processes. Second, there are certain biases and fallibilities in human reasoning [9]. People tend to anchor on items that occur early in a sequence when reasoning about the whole sequence. When asked to describe their reasoning processes and problem solving methods, experts tend to provide reconstructed versions of their reasoning and omit components which seemed obvious and explicit to them, but may have been important to solve the problem (e.g., [3], [19]).

Most traditional knowledge acquisition techniques such as interviewing, questionnaires, observations, and protocol analysis have been designed and applied to acquiring knowledge from a single expert (e.g., [16], [24]). A review of these knowledge acquisition techniques can be found in [27]. Some of these techniques can be adapted and used for acquiring knowledge from multiple experts: e.g., a group of experts may be interviewed individually and interview sessions tape-recorded and transcribed for further analysis (protocol or discourse analysis) [1]. However, both the task and the process become more complicated when multiple experts are involved. When there is only one knowledge engineer, the knowledge acquisition process must be sequential (i.e., interviews with various experts are done on a one-on-one basis). When conflicting views exist between experts the need for several iterations of interviews makes this process very time-consuming.

Multiple knowledge engineers can conduct parallel interviews but coordination among them becomes important and time-consuming. Furthermore, the knowledge engineers may not be equally skilled in employing interviewing techniques. Conflicts can arise between the experts, between knowledge engineers' understanding of the problem domain, or the same expert may even have different opinions at different times and places. Such conflicts must be recognized through transcripts compilation and analyses. The conflicts must be resolved by individual experts and not knowledge engineers.

Although Expertise Transfer System (ETS) [4] and AQUINAS [5], knowledge acquisition tools based on the Personal Construct Theory [20] developed at the Boeing Company, do address knowledge acquisition from multiple experts, they are still in an experimental stage and are limited to laboratory use. The appropriateness and effectiveness of using Personal Construct Theory for multiple experts has yet to be tested.

## Using a GDSS for knowledge acquisition from multiple experts

Another way to acquire knowledge from multiple experts is to facilitate expert interaction that creates synergy and resolves conflicting views and problem-solving strategies. A GDSS is an integrated computer-based system that facilitates the solution of an unstructured or semi-structured task by a group of people $[12]$ . An effective GDSS is designed to increase the efficiency and effectiveness of group activities and aims to improve the group process by removing common communication barriers, and directing the pattern, timing, or content of discussion (e.g., $[17]$ ). Using a GDSS should contribute to the overall quality and quantity of results making them superior to the sum of each individual's contribution.

Research findings on the impacts of GDSS shown that their use increases the depth of analysis, the task-oriented communication (e.g., [15], [33], [35]), the quality of decision, and the confidence and group members' satisfaction (e.g., [2], [11], [18]). A detailed review can be found in [29].

It appears that a GDSS may facilitate knowledge acquisition from multiple experts by providing a collaborative atmosphere, by improving communications, by documenting acquired knowledge electronically, and by facilitating conflict resolution. When a GDSS is used for knowledge acquisition from multiple experts: computer workstations are used to collect inputs electronically; a public screen displays inputs from individual experts; conflicts are identified during the session and resolved immediately.

## Research methodology

## Research questions

The primary research problem is to explore “how” a GDSS can aid the knowledge acquisition process when multiple experts are involved. This is further decomposed into six specific questions:

![](/api/attachments/9CVKGQ5H/fulltext/images/91eed4877384c0fb90092c081a979d9f1c347a3ec8eff55ce3d3abb9530d05d3.jpg)  
Fig. 1. A research framework.

(1) What existing knowledge acquisition techniques can be applied to the GDSS environment? (2) What are the various phases of the acquisition process in these conditions? (3) What components should be incorporated in the environment to facilitate the acquisition of knowledge? (4) What types of support tools are needed to facilitate the generating, extracting, analyzing, and structuring of knowledge? (5) What process models can be used to extract, analyze, and verify knowledge? and (6) What is the methodology of acquiring knowledge in a GDSS environment?

## A research framework

To address these questions, a research framework, shown in Figure 1, was developed based on previous research for expert systems and GDSS. The acquisition process and techniques required to elicit knowledge from a group were identified from the literature on expert systems. Components of a GDSS and interrelationships among its components were identified from the literature. Finally these tools, techniques, and processes were integrated into models.

Knowledge acquisition techniques appropriate to the group environment were identified by review of group techniques used in small group research. These include brainstorming $[28]$ , Delphi technique $[22,31]$ , Nominal Group Technique $[36]$ , and Social Judgment Analysis $[32]$ . Protocol analysis $[26]$ may also be applied to analyze the electronic output from the group process.

The overall knowledge acquisition process can be decomposed into four phases: planning, extraction, analysis, and verification of knowledge. A methodology for knowledge acquisition in a GDSS environment, containing four phases with fourteen steps was developed and discussed in detail in [23]. These are summarized in Table 1.

The six necessary components of a GDSS are hardware, software, facility, procedures, facilitation, and people. People include facilitators and experts. Procedures are enforced by people who set up the agenda.

Tools appropriate for knowledge acquisition were uncovered through a microlevel study of the software component. Those at the University of Arizona Department of Management Information Systems have been used for a variety of research activities [10]. A three-dimensional analysis scheme focusing on the process capabilities, format of output, and interactions among participants was used to identify the appropriate tools for the knowledge acquisition task.

Table 1
Knowledge acquisition phases and steps.

<table><tr><td>KA stages</td><td>Steps</td></tr><tr><td>Planning for KA</td><td>Understanding the domainDefining the problem scopeIdentifying the type of applicationDeveloping process modelsIdentifying participantsPlanning knowledge acquisition sessions</td></tr><tr><td>Knowledge extraction</td><td>Explaining the KADiscussing the objectives of KA sessionsConducting KA sessionsDebriefing the expert team</td></tr><tr><td>Knowledge analysis</td><td>Analyzing session outputsTransforming knowledge into representations</td></tr><tr><td>Knowledge verification</td><td>Developing test scenariosVerifying knowledge with a panel of experts</td></tr></table>

Five process models were developed for conducting knowledge acquisition sessions. They were designed to support planning, identification, classification, repertory grid analysis, and verification. The models were generic processes that were independent of applications. Planning included activities to identify objectives and prepare the sessions. Identification involved determining and defining the problem scope. Verification included collection of feedback on the results. The classification and repertory grid analysis models were specifically designed for the knowledge acquisition task. The classification model provided an iterative process to identify and classify problems; it structured the knowledge acquisition activities in order to develop a hierarchical classification scheme at the end of the sessions. The repertory grid analysis model included activities to identify entities and traits which differentiate entities; a grid was developed by evaluating entities against traits. Further analysis could result in production rules. Due to the nature of the application problem domain (i.e., the information center help-service), the repertory grid analysis was not utilized in the actual knowledge acquisition sessions.

Planning for knowledge acquisition using structured techniques

Structured techniques, such as task and job analysis $[25]$ , can be used to identify knowledge acquisition needs and to structure the process. Because the analysis process serves to identify and delimit major sections of the domain, it provides a focus for development and can be used as a planning tool. It identifies goals of the expert system (ES) and major functions or tasks for which the ES will be responsible. It helps the knowledge engineer identify specific areas and appropriate experts for knowledge acquisition, thereby reducing knowledge acquisition time and making it easier to plan and schedule sessions. And finally, the sessions can be managed more effectively, because they are guided by explicit goals from the planning process.

The task analysis was employed to decompose the knowledge acquisition task. The sub-tasks included identifying major problem areas, sub-problem areas, and sub-sub-problem areas and problem instances. The nature of the information center help-service is a kind of classification problem. The classification model was employed to acquire a hierarchical classification scheme from experts.

## Knowledge acquisition using group systems: a case study

The case study was part of an effort to develop an expert system to support help-service in an information center.

## The application domain

Help-service (i.e., help desk and technical support) provided by information center (IC) consultants is perceived by users as the most important function of ICs [6]. Questions raised are diverse and may be related to both hardware and software. One common practice is to implement a telephone “hot line” [7]. Experts in the problem area must be “on call” to provide timely help. This is not always possible and is becoming increasingly difficult, as ICs are asked to support more users. An expert system that can determine specific needs and make suitable recommendations would therefore be valuable. The system would need to answer questions most commonly directed to the center. It would not replace personnel but would provide first-level screening.

The information center was part of a major computer manufacturing company. It was staffed with twelve internal consultants and served about five thousand end users, who were located in seven adjacent buildings. The end user support functions were divided into three areas: the help desk, the productivity center, and the main information center. The first dealt with both hardware and software problems. Problems dealing with personal computer (PC) applications were handled by the second. “How to” questions were addressed by the last.

An expert system for help-service appeared to be useful to this IC. First, the heavy workload would be reduced. Second, users would receive immediate on-line help on most of their questions instead of waiting on a busy hot line. The four primary problem areas identified by IC consultants were the use of the Professional Office System (PROFS), the use of Application System (AS, a fourth generation language), transferring files among computer systems, and printing files from different hardware.

## The GDSS

A conference room equipped with hardware and software was used to support group activities. Fourteen workstations, each installed with an IBM Personal Computer/AT, were placed in a U configuration around the room. An IBM Personal System 2/Model 80, at the open end of the U, was the facilitator's workstation. Workstations were networked using an IBM token-ring local area network. An IBM PC/AT, used as a server, and a laser printer were located in the control room, which had a large observation window overlooking the conference room. A BARCO system was used to project the facilitator's workstation screen to the large front screen. The room was also equipped with an overhead projector and two white boards. The room is similar to GDSS rooms used to support other group activities.

The software was GroupSystems, developed by the University of Arizona Department of Management Information Systems. Tools used in the knowledge acquisition sessions include: Electronic Brainstorming (an idea generation tool), Issue Analysis (a tool facilitating analysis and idea consolidation), Voting (a rank ordering tool), and Topic Commenter (a tool allowing group discussion of multiple topics). Detailed descriptions of these can be found in [10].

All IC consultants attended the knowledge acquisition sessions, using PROFS. Three were specialists in this and two were specialists in AS. Two of them handled most of the file transfer problems and two others were specialists in printing files using various hardware and software; two others performed administrative support for the center. One consultant who knows all these areas was the supervisor and acted as the primary expert coordinating the activities.

The expert system development team consisted of a group leader (the main contact with the organization), a knowledge engineer, and two programmers. End users of the PROFS and AS also participated in several sessions.

## The knowledge acquisition effort

Three site visits were made to conduct sessions. Table 2 summarizes these.

Table 2  
Summary of site visits and knowledge acquisition sessions.

<table><tr><td>Visit</td><td>KA stage</td><td>KA sessions</td></tr><tr><td>I</td><td>Planning for knowledge acquisition</td><td>Problem scopeProblem characteristicConsultation processCharacteristics of user</td></tr><tr><td>II</td><td>Knowledge extraction</td><td>Problem categorizationProblems and solutions</td></tr><tr><td>III</td><td>Knowledge verification</td><td>Feedback, extensions, term descriptions</td></tr></table>

## Planning for knowledge acquisition: Site visit I

Four sessions were conducted during the first visit (e.g., Table 3). Electronic Brainstorming was used to identify common problem areas and Issue Analysis was used to analyze the comments generated. Two additional brainstorming sessions were conducted to elicit information about the consultation process and user characteristics. In addition, one-on-one personal interviews were used to gain insights into the problem solving process and its problem domain.

The major objective was to identify common problem areas using the stimulus: “What general kinds of questions on software problems come to you?” The results of this brainstorming session were the input to Session II. The Issue Analysis consisted of two phases: Issue Identification and Issue Consolidation. The first of these was used to help consultants identify a list of common problems; e.g., PROFS was identified as an area in which users had the most questions. The second helped to condense the list of problem areas by grouping items with the same level of complexity. Subsets were identified and appended to each general area: e.g., PROFS mail and PROFS notes both were related to the PROFS system; printing notes from PROFS and from a PC file were both related to printing files.

Table 3  
Planning for knowledge acquisition-site visit I.

<table><tr><td>Session</td><td>I</td><td>II</td><td>III</td><td>IV</td></tr><tr><td>Objectives</td><td>Elicit general problem areas</td><td>Identify and consolidate problem areas</td><td>Elicit typical consultation process</td><td>Extract characteristics of users</td></tr><tr><td>Tools</td><td>Electronic Brainstorming</td><td>Issue Analysis</td><td>Electronic Brainstorming</td><td>Electronic Brainstorming</td></tr><tr><td>Topics</td><td>What are the general kinds of questions on software problems that come to you?</td><td>Output from session I</td><td>Describe the steps in a consultation session</td><td>What characteristics of your client are important?</td></tr><tr><td>Participants</td><td>9</td><td>9</td><td>10</td><td>7</td></tr><tr><td>Duration</td><td>45 minutes</td><td>60 minutes</td><td>25 minutes</td><td>20 minutes</td></tr><tr><td>Results</td><td>200 comments</td><td>30 items</td><td>60 comments</td><td>40 items</td></tr></table>

Both Session III and IV were brainstorming sessions: to elicit a snapshot of a typical consultation process and to extract characteristics of users. The problem scope had been defined during the first visit. Consultants with specialties in PROFS, AS, Printing, and File Transferring were identified as-domain experts for the development of the help service ES. One approach was to develop a classification scheme so that the system could classify a user's problem and suggest a solution.

## Knowledge extraction: Site visit II

The primary task here was to extract the expertise required to build the system. Six sessions were conducted, as summarized in Table 4, to extract a hierarchical structure that classifies problem areas into categories, subcategories, and instances with a specific problem statement and solution. Topic Commenter and Issue Analysis were used to develop detailed categorization of the four problem areas. Ten consultants who had the required expertise attended these sessions.

In the first session, consultants used the Topic Commenter tool to state what they knew about the problem areas and listed questions that were frequently asked. The result of this session, a set of common questions characterized into four areas, was used as input to the Issue Analysis session. In the Issue Identification phase, consultants worked individually to group common problems into categories. A list of categories was collected at the facilitator's workstation and projected to the public screen. In the Issue Consolidation phase, the facilitator and consultants worked together on the original list of 80 items and consolidated them into 18 subcategories.

During the consolidation phase, the GDSS helped resolve conflicts. Most of these related to classifying problem areas; they were identified from the system but resolved by discussion among consultants. These subcategories were then used as topics for another set of sessions using Topic

Knowledge extraction sessions-site visit II.

<table><tr><td>Session</td><td>I</td><td>II</td><td>III–VI</td></tr><tr><td>Objectives</td><td>Elicit subsets of common problems within each of the four main areas: PROFS, AS, File transfer, Printing</td><td>Identify and consolidate problem categories within each of the main areas</td><td>Extract problems and solutions within each of the subcategories of the four main areas</td></tr><tr><td>Tools</td><td>Topic Commenter</td><td>Issue Analysis</td><td>Topic Commenter</td></tr><tr><td>Topics</td><td>PROFS, AS, File transfer, Printing</td><td>Output from session I</td><td>Subcategories in PROFS, AS, File transfer, and Printing for Session III, IV, V, VI respectively</td></tr><tr><td>Participants</td><td>10</td><td>10</td><td>8, 2, 6, 6 for Session III, IV, V, VI respectively</td></tr><tr><td>Duration</td><td>40 minutes</td><td>120 minutes</td><td>20-40 minutes</td></tr><tr><td>Results</td><td>500 lines</td><td>18 items</td><td>Approximately 2000 lines in total</td></tr></table>

Commenter to further decompose the subcategories. Specific instances of problems and solutions were extracted during Sessions III to VI.

Although most sessions were only attended by consultants with expertise in a particular area, some sessions were attended by people having general knowledge in using a product. Consultants with general knowledge in any of the problem areas were also invited to attend, but they acted more as end users than as experts. The final results from these sessions were lists of specific problems and associated solutions. Hard copies of outputs were distributed to consultants to verify the knowledge extracted.

## Knowledge analysis

This phase dealt primarily with analyzing outputs from the knowledge acquisition sessions in the extraction phase and was not conducted at the field site. Outputs from knowledge acquisition sessions were analyzed and consolidated. The help-service is a type of classification $[8]$ , for which a heuristic classification structure was used. The sessions in the extraction phase were designed to develop such a structure and to provide instances of problems and solutions. The analysis was very straightforward. Categories and subcategories (i.e., problem areas) were taken from topics emerging from Topic Commenter sessions (Sessions I–VI). Instances (i.e., specific problems and associated solutions) were taken from Topic Commenter sessions (Sessions III–VI).

The classification structure was the foundation of the knowledge base. It was submitted to the IC consultants for evaluation before implementation. A set of primitive rules generated from the classification structure was also provided. Together, the classification structure and primitive rules provided the two programmers material from which to generate rules.

## Knowledge verification: Site visit III

It was next necessary to have experts confirm the classification structure, including categorization of problem areas and specific problems with their solutions.

A first-level verification was performed after the knowledge acquisition sessions during the 2nd visit. Results were reviewed by IC consultants. Verification focused on the terms and descriptors used. Minor changes were made. These had been suggested and considered before session outputs from the knowledge extraction phase were analyzed.

Knowledge verification sessions-site visit III

<table><tr><td>Session</td><td>I</td><td>II</td><td>III</td><td>IV</td></tr><tr><td>Objectives</td><td>Elicit feedback on the prototype system</td><td>Elicit feedback on the database management tool</td><td>Extract term descriptions</td><td>Extract suggestions on possible extensions</td></tr><tr><td>Tool</td><td>Topic Commenter</td><td>Topic Commenter</td><td>Topic Commenter</td><td>Topic Commenter</td></tr><tr><td>Topics</td><td>Dialog, screen design, user&#x27;s computing experience, tracking loop, user&#x27;s remarks, miscellaneous.</td><td>Screen design, functions management reports, maintenance reports, miscellaneous.</td><td>Terms used in the prototype as problem categories, subcategories, and PROFS and AS.</td><td>Methods to determine user&#x27;s computing experience, classification schemes of the four areas: PROFS, AS File transfer, Printing</td></tr><tr><td>Participants</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>Duration</td><td>30 minutes</td><td>30 minutes</td><td>30 minutes</td><td>30 minutes</td></tr><tr><td>Results</td><td>170 lines</td><td>120 lines</td><td>60 lines</td><td>250 lines</td></tr></table>

A third visit, summarized in Table 5, was made to complete the verification. The second-level verification primarily involved a thorough explanation of the classification structure and an overall review of the system architecture, followed by a demonstration of the prototype system to allow users and consultants to evaluate system solutions. The third-level verification focused on using real problems and scenarios to check for an appropriate solution. Feedback collected from the third visit was mainly concerned with implementation details and a maintenance tool. Some minor modifications to the classification structure and definitions of terms were provided to refine the system.

## Observations

A GDSS facilitated the acquisition of knowledge from a group of experts by documenting knowledge electronically, supporting knowledge extraction from individual experts in a parallel fashion, offering a structured process and possibilities to resolve conflicts during the knowledge extraction phase, and providing a collaborative atmosphere to facilitate group interactions that enrich the domain of expertise. In addition, we found that structured analysis techniques were useful in planning for knowledge acquisition, the participation of end users was important, and that a designated primary expert was helpful when multiple experts were involved. A post-session survey revealed features that experts liked including speed and thoroughness of assembling data, producing many ideas using brainstorming, parallel processing using Topic Commenter, screen design, immediate feedback, by responding to other people's input, and concentrated effort on a "memory dump" by several people at once. Features that they disliked about GDSS-facilitated knowledge acquisition included mental burnout due to intensity, a tedious consolidation process, and reducing creativity due to the structured format.

## Electronic documentation of knowledge

One of the primary advantages of using computer support to facilitate the acquisition of knowledge is that knowledge is documented electronically. There is no need to tape-record the interview process or to transcribe audio or video tapes. However, the Issue Analysis tool was not implemented to support automatic consolidation of issues at the time of the study and oral discussion was the primary communication channel. Video tapes could be used to reveal how conflicts were identified and then resolved.

## Parallel knowledge extraction

Another advantage of using a GDSS is that the acquisition process can be performed in parallel. If domain experts act individually, the acquisition is time-consuming and difficult. Conflicting views or strategies cannot be identified during the extraction process and must be resolved through several iterations of individual knowledge elicitation. Since individual knowledge engineers cannot be equally capable of performing the knowledge acquisition task, results from individual knowledge elicitation vary. Furthermore, the integration of knowledge into group knowledge should be done by experts rather than knowledge engineers.

If domain experts act as a team (i.e., knowledge acquisition activities involve the expert team so that group knowledge results), knowledge engineers can take advantage of such techniques as group interviewing, group discussion, and brainstorming. Knowledge extraction may be performed in parallel; experts contribute their knowledge together so that duplications can be eliminated by reviewing others entries and conflicts can be identified and resolved. Experience from the study suggests that using the parallel process saves time.

Awareness of other participants' presence and the ability to interact with them is important. Multiple user interfaces for parallel input is the key to achieve this. Moreover, the system should provide a public view of the group work, as well as feedback. This would allow each participant to interact with a specific, a subset, or other participants. This design feature is a departure from multiple user systems where a locking mechanism is the way to avoid conflict among users of shared resources.

## Conflicts addressed during knowledge extraction

In a GDSS environment, conflicting views can be addressed during the knowledge extraction phase. They mainly arise during extraction of heuristics to solve problems. Providing individual participant access to the group view identifies discrepancies. Some conflicts may be resolved through verbal debate, some may never be resolved, but a final consensus may be reached. Discussions are encouraged, whether or not electronic media are used. Observations indicate that although the current implementation of the consolidation tool (i.e., Issue Analysis) did not facilitate the consolidation process efficiently, verbal discussion could be used to resolve conflicts.

## Interaction resulting in enlarged and enriched domain of expertise

Interaction among experts is encouraged: it results in an enlarged and enriched domain of expertise. Since experts were acting both as “experts” and as “users,” they provided both problem descriptions and solutions. It was observed, during knowledge acquisition sessions, that when some consultants brought up frequently-asked questions for which they did not know the answers, other consultants were able to provide detailed solutions. Furthermore, a piece of information entered by one expert often stimulated another’s thoughts on a different matter. For example, one expert’s statement of problems related to printing a file induced another expert to suggest several ways of printing various files using different systems. Experience suggests that tools must encourage interactions among participants by providing various communication channels. Knowledge acquisition sessions should be held with computer support, since discussions can be captured by the system and no videotaping will be necessary.

## Roles of participants

Participants involved in the knowledge acquisition process using a GDSS included a designated primary expert and experts, a knowledge engineer, a facilitator, end users, and management.

## A designated primary expert

Having the right person as a primary expert was critical to the success of the project. In this study, one particular individual was of tremendous help in identifying experts, scheduling knowledge acquisition sessions, gathering experts, explaining the objectives of each session, helping resolve conflicts, and assisting in refining the knowledge base. This observation supports Prerau's [30] and Sviokla's [34] recommendations for a primary expert.

## The knowledge engineer

In the planning phase, the knowledge engineer defined the scope and process models. Her primary concern was the technical feasibility of developing an effective system. In the extraction phase, the knowledge engineer monitored the knowledge acquisition activities and the acquired knowledge so that it could be represented in a computer-understandable form in the analysis stage. In the verification phase, the knowledge engineer identified acquired knowledge and ways of validating the system components.

## The facilitator

The facilitator during knowledge acquisition sessions could be a group leader, guiding the group to achieve objectives of particular sessions, a chauffeur, who serves as the intermediary between the group and the GDSS software, and/or an assistant in the use of computer technology. One important characteristic of a good facilitator was technical competence (assisting experts' use of software, directing the system, and controlling the working environment). Being able to work with people was another needed characteristic [13], with communication skills and mastery of group techniques. During knowledge acquisition sessions, professional facilitators were desirable, but knowledge engineers with extensive experience working with groups and group environments were also acceptable.

## The users and the management

End users provided a broad perspective of how the expert system might be able to help them. Those with expertise in specific problem domain areas were also included in the knowledge extraction phase, so that interactions among experts and end users created a synergy to enrich the domain of expertise. Managers were involved in order to provide strategic guidelines as to what should and should not be included.

## Contributions and limitations

This exploratory study on the use of a GDSS for knowledge acquisition contributed to three research areas. It advanced expert systems development by establishing and applying a methodology for knowledge acquisition from multiple experts. Second, it expanded the study of GDSS to a new application. Last, it contributed to theoretical foundations by developing process models.

This study had three major strengths. First, it was an attempt to conduct an interdisciplinary investigation between knowledge acquisition for expert systems and the use of GDSS. This broadened the scope of GDSS applications. Second, the study was conducted in a real world application where the GDSS was successfully used to acquire knowledge for use in improving an information center's help service. Finally, no tool was customized. Tools were designed to be general purposes. Only the process models were designed to structure the knowledge acquisition activities.

There were some limitations. One consultant felt that the structured process reduced or limited creative thinking during the knowledge acquisition session. Another was concerned that intensity during the knowledge acquisition sessions could potentially cause mental burnout, that could result in useless results. Frequent breaks during sessions were encouraged to reduce problems that might be caused by this intensity. Gaining top management's commitment to release experts temporally from their daily responsibilities is also crucial.

## Implications and conclusions

Using a GDSS for knowledge acquisition opens the possibilities of extracting knowledge from multiple experts via teleconferencing technology in a distributed GDSS environment. Also, having both experts with diverse specialties and end users in the knowledge acquisition session, a knowledge engineer could gather various viewpoints from both experts and end users. This interaction creates a synergy to enrich the domain of expertise, making it more comprehensive than that would be acquired from “pure” experts.

Knowledge acquisition is the most important task in the development of expert systems. Knowledge acquisition from multiple experts can be performed in two ways or a combination of both: elicit knowledge from each expert individually or from experts as a group. Based on observations in this study, a group approach to acquiring knowledge from multiple experts using a GDSS has proved useful. The evaluation of the efficiency and effectiveness of the group approach, the relative merits of manual and computer-supported environments for knowledge acquisition, and of various designs for a GDSS to support such tasks require further investigation.

## References

[1] A.H. Abdul-Gader and K.A. Kozar, “Discourse Analysis for Knowledge Acquisition,” Journal of Management Information Systems, (6:4), Spring 1990, pp. 61–82.

[2] L.M. Applegate, B.R. Konsynski, and J.F. Nunamaker, Jr., “A Group Decision Support System for Idea Generation and Issue Analysis in Organization Planning,” Proceedings of 1986 Conference on Computer Supported Collaborative Work, Austin, TX, 1986, pp. 16–34.

[3] D.C. Berry, “The Problem of Implicit Knowledge,” Expert Systems, (4:3), August 1987, 144–150.

[4] J.H. Boose, “Rapid Acquisition and Combination of Knowledge from Multiple Experts in the Same Domain,” Future Computing Systems, (1:2), 1986, pp. 191–216.

[5] J.H. Boose and J.M. Bradshaw, “Expertise Transfer and Complex Problems: Using AQUINAS as a Knowledge Acquisition Workbench for Knowledge-Based Systems,” International Journal of Man–Machine Studies, (26), 1987, pp. 3–28.

[6] J.C. Brancheau, D. Vogel, and J.C. Wetherbe, “An Investigation of the Information Center from the User’s Perspective,” Data Base, Fall 1985, pp. 4–17.

[7] R.G. Canning, "Supporting End User Programmer," EDP Analyzer, (19:6), June 1981.

[8] W.J. Clancey, “Heuristic Classification,” Artificial Intelligence, (27), 1985, pp. 289–350.

[9] G.B. Davis and M.H. Olson, “Humans as Information Processors,” in Management Information Systems: Conceptual Foundations, Structure, and Development, McGraw-Hill, New York, 235–268.

[10] A.R. Dennis, J.F. George, L.M. Jessup, J.F. Nunamaker, and D.R. Vogel, “Information Technology to Support Electronic Meetings,” MIS Quarterly, 1988.

[11] A.R. Dennis, A.R. Heminger, J.F. Nunamaker, and D.R. Vogel, “Bringing Automated Support to Large Groups: The Burr-Brown Experience,” Information & Management, (18), pp. 111–121, 1990.

[12] G. DeSanctis and B. Gallupe, “A Foundation for the Study of Group Decision Support Systems,” Management Science, (33:5), 1987, pp. 586–609.

[13] M. Doyle and D. Straus, How to Make Meetings Work, Jove Books, New York, 1976.

[14] E.A. Feigenbaum, “The Art of Artificial Intelligence: Themes and Case Studies of Knowledge Engineering,” International Joint Conference on Artificial Intelligence 5, 1977, pp. 1014–1029.

[15] R.B. Gallupe, G. DeSanctis, and G. Dickson, “Computer-based Support for Group Problem Finding: An Experimental Investigation,” MIS Quarterly, (12:2), 1988, pp. 277–296.

[16] A. Hart, Knowledge Acquisition for Expert Systems, Kogan Page Ltd., London, 1986.

[17] G.P. Huber, “Issues in the Design of Group Decision Support Systems,” MIS Quarterly, (8:3), 1984, pp. 195–204.

[18] L.M. Jessup, D.A. Tansik, and T.L. Laase, “Group Problem Solving in an Automated Environment: The Effects of Anonymity and Proximity on Group Process and Outcome with a Group Decision Support System,” Proceedings of the Academy of Management, Anaheim, CA, August 1988.

[19] P.E. Johnson, “What Kink of Expert Should a System Be?” The Journal of Medicine and Philosophy, 8, 77–97.

[20] G. Kelly, The Psychology of Personal Constructs, Norton, New York, 1955.

[21] S.R. LeClair, A Multiexpert Knowledge System Architecture for Manufacturing Decision Analysis, Ph.D. dissertation, Arizona State University, May 1985.

[22] H.A. Linstone, and M. Turoff (Eds.), The Delphi Method: Techniques and Applications, Reading, MA: Addison-Wesley, 1975.

[23] Y.I. Liou, E.S. Weber, and J.F. Nunamaker, Jr., “A Methodology for Knowledge Acquisition in a Group Decision Support System Environment,” Knowledge Acquisition, (2), 129–144, 1990.

[24] Liou, Y.I., “Knowledge Acquisition: Issues, Techniques, and Methodology,” Data Base, (23:1), Winter 1992, 59–64.

[25] K.L. McGraw and K. Harbison-Briggs, Knowledge Acquisition: Principles and Guidelines, Prentice Hall, Englewood Cliffs, NJ, 1989.

[26] A. Newell and H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[27] J. Olson and J.H. Rueter, “Extracting Expertise from Experts: Methods for Knowledge Acquisition,” Expert Systems, (4:3), August 1987, pp. 152–168.

[28] A. Osborn, Applied Imagination, Scribner's, New York, 1957.

[29] A. Pinsonneault and K.L. Kraemer, “The Impact of Technological Support on Groups: An Assessment of the Empirical Research,” Decision Support Systems, (5), 1989, pp. 197–216.

[30] D.S. Prerau, “Selection of an Appropriate Domain for an Expert System,” The AI Magazine, (6), Summer 1985, pp. 26–30.

[31] D.S. Prerau, Developing and Managing Expert Systems, Addison-Wesley, Reading, MA, 1990.

[32] J. Rohrbaugh, “Improving the Quality of Group Judgment: Social Judgment Analysis and the Nominal Group Technique,” Organizational Behavior and Human Performance, (28), 1981, pp. 272–288.

[33] J. Siegel, V. Dubrovsky, S. Kiesler, and T. McGuire, "Group Processes in Computer-Mediated Communication," Organizational Behavior and Human Decision Processes, (37), 1986, pp. 157–187.

[34] J.J. Sviokla, “Business Implications of Knowledge-Based Systems,” Parts I and II, Data Base, (17), Summer 1986, pp. 5–19; (18), Fall 1986, pp. 5–16.

[35] M. Turoff and S.R. Hiltz, “Computer Support for Group Versus Individual Decisions,” IEEE Transactions on Communications, (30), January 1982, pp. 82–91.

[36] A. Van de Ven and A. Delbecq, “Nominal Versus Interacting Group Processes for Committee Decision Making,” Academy of Management Journal, (14), pp. 203–213, 1971.

## Acknowledgment

The authors thank Drs. Sudha Ram, David Carlson, and Stephen Hayne for their involvement in the ICE-H project. We appreciate Dr. Gerald DeSanctis for her comments on an earlier version of this article. Our special thanks go to Dr. Edgar Sibley and anonymous referees for their helpful comments.
