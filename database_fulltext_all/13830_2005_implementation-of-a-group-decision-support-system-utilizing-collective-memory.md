---
otero_id: 13830
otero_key: "MGEBTN39"
title: "Implementation of a group decision support system utilizing collective memory"
authors: "W.David Haseman; Derek L. Nazareth; Souren Paul"
year: "2005"
journal: "Information & Management"
doi: "10.1016/j.im.2004.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Implementation of a group decision support system utilizing collective memory

W. David Haseman<sup>a</sup>, Derek L. Nazareth<sup>a</sup>, Souren Paul<sup>b,\*</sup>

<sup>a</sup>School of Business Administration, University of Wisconsin, Milwaukee, WI 53201, USA <sup>b</sup>College of Business and Administration, Department of Management, Southern Illinois University at Carbondale, Carbondale, IL 62901-4627, USA

Received 30 January 2002; received in revised form 15 October 2003; accepted 2 April 2004 Available online 3 October 2004

## Abstract

Collective memory has been characterized as a socially articulated and maintained reality of the past—one form being organizational memory. The collective memory concept can also be specialized to a group level and used to support work groups engaged in repetitive decision-making activities. The advantages of capturing collective memory are many, including simplification of the process, codification of decision strategies, carryover of knowledge when group composition changes, etc. While there has been substantial research in group decision-making, the explicit use of collective memory to support repetitive decision-making has received less attention. This paper describes the development and implementation of a collective memory based environment for support of a multi-attribute, iterative decision process. The environment utilized hypermedia, groupware, and Intranet technologies. Results of its use are encouraging.

Keywords: Collective memory; Group memory; Organizational memory; Group decision support systems; Knowledge sharing systems; Multi-attribute decisions

## 1. Introduction

Many organizational decision-making processes involve groups of executives performing periodic and repetitive activities. At each session, new sets of data, information, and knowledge may be generated. The composition of the decision-making group, however, may change: group members may retire, resign, or be transferred. New members of the group need to learn how previous decisions were made.

While organizational policies and procedures will undoubtedly be of some use in this context, the intelligence and design activities from Simon’s characterization of decision-making [32] are likely to represent the richer knowledge that is useful in subsequent sessions. Therefore, mechanisms to capture the experiential knowledge of these groups can be of significant value to the organization in general, and the group in particular. The development of a shared repository that stores the knowledge of group members, retains the rules, policies, and standard procedures, and acquires relevant data and knowledge from the external environment will clearly assist these groups. The shared repository, together with the appropriate means for managing its content, represents an implementation of collective memory.

Zarecka [39] described collective memory as a socially articulated and maintained history. Pennebacker and Banasik [27] highlighted the dynamics that contribute to the issues associated with building and maintaining collective memories. Collective memory at the enterprise level, viz. organizational memory has emerged as an area of considerable research interest. At the workgroup level, collective memory is generally characterized as group memory. It can include the knowledge and experiences of the groups in the context of decision-making activities. Other cases where such memory will be of utility are multi-stage decisions and decisions that cannot be satisfactorily completed in a single session, creating a need to carry over intermediate findings to subsequent sessions.

This paper outlines the development and implementation of the prototype of a group decision-making environment that utilizes the work of prior groups stored in the collective memory. In an effort to enhance utility, the prototype was tested in a semistructured decision-making environment involving multiple attributes. Collective memory components were captured using a hypermedia framework, and the collective memory was leveraged through the use of Intranet technology interfaced to traditional group decision support systems (GDSS).

## 2. Collective memory, group memory, and group decision-making

Memory is the facility to retain, recall, and manipulate past or present information as well as expectations about the future. Although the primary focus of memory-related research is on individuals, Halbwachs et al. [9] proposed that there is memory at the collective level, a socially constructed notion. Members of different social groups and institutions (such as family and associations) draw on their current context to recreate the past. Organizational memory, defined as ‘‘the means by which knowledge from the past is brought to bear on present activities, thus resulting in higher or lower levels of organizational effectiveness’’ [33], has been variously characterized as: a function of people and artifacts [21]; dependent on the upper echelon of an organization [10]; an interpretative system [5]; and the organization itself [8]. Moorman and Miner [22] defined organizational memory as ‘‘collective beliefs, behavioral routines, or physical artifacts that vary in their content, level, dispersion, and accessibility.’’ Sandoe et al. [28] conceptualized organizational memory along two dimensions. Ontologically, the memory can have two forms: concrete or abstract. Epistemologically, the memory can represent reality or serve as means to interpret it. Accordingly, four different views exist:

1. Concrete-representation: such as data, documents, and formal knowledge.

2. Concrete-interpretation: such as organizational policies and operating procedures.

3. Abstract-representation: such as cognitive maps and frameworks.

4. Abstract-interpretation: such as culture and social structures.

A host of benefits attributable to organizational memory have been cited including increased organizational learning [11], lowered transaction costs, and lowered resistance to decisions [36]. A potential misuse of organizational memory can be the internalized learning of users, which may invoke routine responses to non-routine situations.

## 2.1. Group memory

Group memory is a form of collective memory at a workgroup level; it is useful in various types of group work such as meetings and projects. A model of transactive group memory was presented in Wegner [38]. Transactive memory consists of the information stored in each individual member’s memory and the awareness of the type of information held by other members of the group. The encoding, storage, and retrieval of transactive information is facilitated by communications and interactions among the group members. Models have predominantly centered on the use of rich communication media such as faceto-face or telephonic conversations [1] and are viewed as being different from group interactions supported by group support systems (GSS) that allow members to interact anonymously and asynchronously. GSS researchers have employed shared repositories such as knowledge bases and e-mail folders to store group level information and knowledge from group deliberations, interactions, or negotiations [24]. GSS literature has frequently used the term ‘‘group memory’’ for this shared repository and its tools. Such memory can support a group’s work within and across sessions. It can also provide uniform, consistent knowledge acquired from prior sessions and can be used ‘‘to bring new participants up to speed by browsing through knowledge about current session and former sessions’’ [12]. Due to ambiguity in the terminology, we employ the term collective memory instead of group memory in this research. Issues of knowledge creation and acquisition in GSS usage have received particular attention. Kwok and Khalifa [18] examined how the use of GSS can provide a higher level of knowledge acquisition. Parent et al. [26] described how face-to-face GSS can be used to enhance knowledge creation in focus groups. The integration of collective memory with GSS is thus an important but less explored area. Desired functional capabilities for such collective memory include [17]:

\- Access to information internal and external to the group.

\- Capturing, storage, and integration of information generated by group interaction.

\- Provision of common perspectives of organizational information (mission, goals, objectives, and basic policies).

\- Provision of session continuity through stored data on previous sessions.

\- Enlightenment of new group members on previous activities of the group.

\- Supporting works of groups distributed across time and space.

Prior implementations of collective memory for groups included the support for project [23,37] and meeting memory.

## 2.2. Decision-making using collective memory

Several types of group decisions can benefit from group level collective memory support. Repetitiveness of the decision-making situation presents an obvious case, but though it reinforces the decision-making practices, it does so at the expense of recall of less frequent policies and decisions. In such situations, collective memory may be bypassed for routine cases but will be instrumental in exceptional ones. Multistage decisions represent another compelling case. Depending on the time period between sessions and the level of activity in the intervening period, some loss of individual memory can be expected. Collective memory allows the team to resume deliberations at relatively little cost and no significant rework of prior material. Change in group membership also needs access to collective memory. New members must be initiated in the group process and existing members may take on additional or different roles. An iterative decision process, where decision makers work through multiple rounds to achieve consensus, could also benefit from collective memory. Some social choice processes, notably elections through repeated ballots, also demonstrate similar needs.

The contents of a collective memory can range considerably including, but not limited to, data sets used in decision-making, prior or partial decisions made, models for decision-making, traces of prior meetings, explanations, decision strategies, alternative courses of action, etc.

Table 1  
Collective memory usage by decision type

<table><tr><td>Group level collective memory support</td><td>Repetitive decisions</td><td>Multi-stage decisions</td><td>Group variability</td><td>Iterative decisions</td></tr><tr><td>Raw data sets</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Intermediate data</td><td></td><td>√</td><td></td><td></td></tr><tr><td>Candidate solutions</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Models for decision-making</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Model outputs</td><td></td><td>√</td><td></td><td></td></tr><tr><td>Decision strategies</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Decisions made</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Partial decisions made</td><td></td><td>√</td><td></td><td></td></tr><tr><td>Decision traces</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Decision explanations</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

The selection of collective memory contents and composition is critical for its effective use. Table 1 lists some collective memory options and their posited relevance for various types of decisions.

## 3. Group decisions utilizing collective memory

Our work elicited the use of collective memory in an iterative decision that closely resembles judgment tasks. Judgment tasks are cognitive-conflict ones and have outcome and solution scheme multiplicity with solution scheme/outcome uncertainty [20]. They are commonly found when some form of problem reduction (or structuring) is performed through the selection of an appropriate solution scheme and then is used to evaluate the outcome. Recruitment and personnel hiring are good examples—typically the first round involves the selection from a candidate pool, while the final selection is made from the smaller pool often using the evaluations from the earlier process.

The participants in cognitive-conflict tasks can benefit from a collective memory repository with preference structures of similar prior tasks. For each preference structure, the memory can store the different instances of its use and consequent outcomes. For example, a committee making decision on admission of students to a doctoral program can use a collective memory that contains information (such as GPA, test scores, etc.) used in the past, the decision rule employed (lexicographic, elimination by aspect, additive linear, etc.), values/weights of each criteria, and decision outcomes. By carefully analyzing the memory, participants can develop a better idea about the preference structures that have resolved cognitive conflicts in the past. This may help decision makers adopt less conflicting decision/judgment policy.

The decision situation considered here involves the selection and prioritization of the attributes of Master of Business Administration (MBA) programs. Various sources of information are available including US News and World Report, Peterson’s Guide, the Princeton Review, etc. An individual wishing to select an MBA program can also browse Web sites as well as employ a host of search engines that assist in finding alternatives. Based on some threshold values for various attributes of the school (e.g., location, desired majors), the search engines can produce a list of candidate schools. While it is possible that more elaborate models based on optimization and behavioral decision theory can be formulated for this decision, the selection process is typically characterized in terms of alternatives and attributes. Although the decision appears to be an individual one; in reality, many factors affect the decision including the influence of family, peer groups, and mentors. The need to simplify the decision is paramount. Selecting a set of meaningful attributes, rank ordering them, and eliminating unpromising ones are the strategies that can simplify the process. Many strategies involve external influences, and though their role may be primarily advisory, they are important nonetheless.

In an attempt to simplify the decision, an iterative approach was adopted. Possible attributes were identified prior to the first round. These were culled from a large set of available information and descriptors of various MBA programs. Groups of decision makers then allocated weights (constrained to sum to 100) for selected attributes. Decision makers were free to assign a zero weight to an attribute if they felt it was unimportant. In cases where attributes are subjective and their number and alternatives relatively small, it may be desirable to have decision makers rate each alternative for all relevant attributes. This approach is also preferred when decision makers employ non-linear utility functions. However, for decisions involving large numbers of attributes and/or alternatives, this approach proves time-consuming and cognitively difficult, particularly in maintaining consistency. For attributes with numeric values, a normalized score using a simple linear transformation may be used for comparability. Thus, if the minimum and maximum values for tuition fees are $x _ { i , \mathrm { m i n } }$ and $x _ { i , \operatorname* { m a x } } ,$ the normalized score for a school with a tuition fee of $x _ { i }$ is

$$
x _ {i} = \frac {1 - (x _ {i} - x _ {i , \mathrm{min}})}{x _ {i , \mathrm{max}} - x _ {i , \mathrm{min}}}.\tag{1}
$$

Normalized scores are dimensionless, enabling comparison of attributes on different dimensions. In addition, they eliminate any scale factor. If a simple linear transformation does not capture this rating, a piecewise continuous mapping to an ordinal scale may be employed. In this case, the tuition values can be broken down into several ranges, each of which maps to a predetermined ordinal scale—a technique often employed in decision analytic tools [30].

Based on the attribute weights, a rank-ordered list of alternative schools was generated using the ‘‘simple additive weighting’’ method [19,4,15]. The score $S _ { i }$ for alternative i was derived:

$$
S _ {i} = \sum_ {j} X _ {i j} W _ {j}\tag{2}
$$

where $X _ { i j }$ represents the normalized score for attribute $j$ of alternative i.

$W _ { j }$ represents the group’s weight for attribute j and

$$
\sum_ {j} W _ {j} = 1 0 0.\tag{3}
$$

Schools were ordered by their final scores. The list of schools produced is thus a consequence of the decision made on the attributes and their weights. By examining the combination of attribute weights and the rank-ordered list, group members can determine how schools are rated on various attributes. If the group is satisfied, the decision-making process can conclude; otherwise, attribute weights can be revised and a new rank-ordered list generated. The decision task chosen for this work is similar to the techniques followed in some multi-attribute decision-making. Turban and Aronson [35] also discuss similar group tasks.

## 4. A prototype system to support iterative group decision-making

Support for group decision-making necessitated the creation of an appropriate meeting environment. The need for individual group members to explore the solution set and reach consensus over multiple decision sessions prompted the development of an appropriate meeting environment. A modular architecture was employed, as depicted in Fig. 1.

Information relevant to the decision (e.g., attributes and their scores for individual programs) was stored in a separate module. Data was available to the decision makers through a hypermedia interface. This allowed individual decision makers to examine MBA programs as well as rank order them on any specific attribute. This was implemented using standard Web pages served over an Intranet. Collective memory information, including attributes selected by prior groups, the respective weights of each attribute, and rank-ordered lists of candidate schools was maintained in a separate module. Although this can be displayed automatically using a meeting databasedriven Web site, human intervention was deliberately introduced. Experts analyzed the meeting data to filter the relevant information generated in a meeting. This modular approach facilitated the ability to swap out the decision-related data and substitute a different set for collective memory support of a different decision.

![](/api/attachments/MGEBTN39/fulltext/images/42fab98cb266090cda8d389f7e6e3bc96b85988ce947d2f1eaf9956864cc265a.jpg)  
Fig. 1. Logical prototype architecture.

Table 2 VisionQuest support

<table><tr><td>VisionQuest tool</td><td>Generation</td><td>Organization</td><td>Evaluation</td><td>Selection</td></tr><tr><td>Brainwriting</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Commenting</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Categorizing</td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>Allocating</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Ranking</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Rating</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Multi-rating</td><td></td><td></td><td>√</td><td></td></tr><tr><td>Reducing</td><td></td><td></td><td></td><td>√</td></tr><tr><td>Voting</td><td></td><td></td><td></td><td>√</td></tr></table>

Management of the group decision process was accomplished through the use of a module that allowed decision makers to allocate weights to individual attributes and vote on final decisions. We selected Vision Quest based on its ease of use, ease of training, and simplicity of design. It can be used to generate, organize, and evaluate ideas, obtain consensus on them and plan actions based on them. It requires a skilled facilitator. The specific tools available in VisionQuest for support of various tasks in electronic meetings are depicted in Table 2. In addition, it permits the integration of external software as part of the meeting—a crucial feature, since most decisions involve external inputs and analyses. The physical architecture of the prototype system is presented in Fig. 2.

## 4.1. Information module—MBA program information

MBA program Web pages were assembled from publicly available data, e.g., the Graduate Management Admissions Council, Princeton Review, Peterson’s Guide, and information obtained directly from the universities. The sources held a large amount of information and were not entirely consistent in their presentation or content. A consistent format, with no missing data, and a relevant subset of both attributes and schools obviously was needed. After careful consideration, 18 attributes that characterized MBA

![](/api/attachments/MGEBTN39/fulltext/images/62e3218689a0b0de745553e0171bb08aae07b3a740d7b91c6a00108ad3aa670c.jpg)  
Fig. 2. Physical prototype architecture.

Table 4

<table><tr><td>Table 3Attributes selected for decision task</td></tr><tr><td>AACSB accreditationAverage age of incoming classAverage starting salaryProximity to city XExecutive MBA program availabilityMinimum months to degreeNon-tuition feesPart-time MBA programPhD program availabilityPercentage of applicants admittedPercentage of international studentsPercentage of minority studentsPercentage receiving aidPercentage of women studentsTuition feesTypical GMAT scoreTypical undergraduate GPATypical work experience</td></tr></table>

programs were selected. These are listed in Table 3. It is unlikely that decision makers will concurrently consider all 18 in the decision-making process. We expected that only a small subset would be weighted heavily. To preclude researcher bias, the final set was not restricted to those expected to play a significant role.

In a similar vein, it was decided to restrict the number of potential schools considered. This proved to be a little more challenging because a list of over 2000 programs needed to be reduced to a manageable subset. Clearly, a great deal of bias could be introduced here. After some deliberation, it was decided that the list be restricted to MBA programs of note, in the USA. A few additional programs were also included in this set, mostly local programs; see Table 4.

Data for these 24 programs was collected on the 18 relevant attributes and encoded in a consistent format in the program Web pages. The authors did not verify the accuracy of the data as it was deemed to have no significant impact on the outcome of the research.

## 4.2. Information module—collective memory

The collective memory segment included information that related to the group process and any implications of the decisions made. We decided that the collective memory module should contain data on attributes selected, weights assigned, and the resultant ranking of the programs. After careful review, more detailed data like the dispersion of attribute weights and participants’ comments were not included in the prototype. The specific items stored in the collective memory module are given in Table 5.

<table><tr><td>Carnegie Mellon University</td></tr><tr><td>DePaul University</td></tr><tr><td>Harvard University</td></tr><tr><td>Indiana University</td></tr><tr><td>Marquette University</td></tr><tr><td>Michigan State University</td></tr><tr><td>MIT, Sloan School of Management</td></tr><tr><td>New York University</td></tr><tr><td>Northwestern University</td></tr><tr><td>Purdue University</td></tr><tr><td>Saint Louis University</td></tr><tr><td>Southern Illinois University, Carbondale</td></tr><tr><td>Southern Illinois University, Edwardsville</td></tr><tr><td>University of California, Los Angeles</td></tr><tr><td>University of Chicago</td></tr><tr><td>University of Cincinnati</td></tr><tr><td>University of Illinois at Chicago</td></tr><tr><td>University of Michigan</td></tr><tr><td>University of Minnesota</td></tr><tr><td>University of Nebraska, Lincoln</td></tr><tr><td>University of Notre Dame</td></tr><tr><td>University of Pennsylvania, Wharton School</td></tr><tr><td>University of Wisconsin, Madison</td></tr><tr><td>University of Wisconsin, Milwaukee</td></tr></table>

In order to keep the interactions manageable and let decision makers focus on the task, the data in the collective memory module was also accessible in hypermedia format [2]. The navigation paths between the collective memory and MBA program pages are shown in Fig. 3, with collective memory depicted in shaded boxes. The navigation paths make it easy for decision makers to move between the data and collective memory in a seamless manner. Sample Web pages are depicted in Fig. 4.

<table><tr><td>Table 5Collective memory contents</td></tr><tr><td>Attributes selected by previous groupsPercentage of groups selecting an attributeAverage weight allocated to each attributeRank-ordered list of programs using the attribute subsets and weights from prior groups</td></tr></table>

![](/api/attachments/MGEBTN39/fulltext/images/5a6425b953956f14476dbaa27bdc282a834176adfb29ec56a7d8c1cb508879e7.jpg)  
Fig. 3. Navigation in hypermedia.

## 4.3. Data management

The source and nature of the data determined how it was managed and manipulated. VisionQuest was used to store meeting-related data such as session details, list of participants, allocation of weights by participants, and any votes taken by the decisionmaking group. This included both individual and group results. Data on individual MBA programs was stored in a Microsoft Access database. This included some descriptive data about each program, as well as the scores on each attribute of interest, normalized on a 0–1 scale to facilitate comparability. Continuous variables were normalized using the range of attribute values across all programs, and indicator variables were simply converted to 0 or 1. The group weights were used in conjunction with the normalized scores to arrive at an overall score for each program, which formed the basis for the program rankings. Although we used the simple additive weighting approach to compute the total score of the MBA programs, other multiple criteria decision-making techniques [34] could also be used. Data was stored for each iteration. In addition, data about individual Web pages accessed was captured as part of the log.

## 4.4. The meeting management module

The management of the sessions was performed through the use of allocation and voting tools. The allocating tool enabled participants to distribute a predetermined total of points to a set of alternatives. The software then averaged out the allocation by individual participants to arrive at the group allocation. It also displayed the range of points allocated to each alternative, providing the group the opportunity to examine any disparate allocations. The group could re-allocate the points to arrive at greater consensus. The voting tool allowed the group to take opinion polls on alternatives or outcomes. These results were reported as simple tallies, and a group could adopt any strategy (simple majority, two-thirds majority, approval voting, etc.) for final selection.

Each decision-making session was created as a meeting with an agenda and roster, the latter being the list of users participating in the meeting. The agenda consisted of the sequence of tasks to be performed, and it was implemented as a series of VisionQuest topics and activities. Groups were given a predefined agenda that provided for up to seven iterations, though the groups were informed that if consensus was reached, they could stop. Each iteration

comprised browsing the relevant Web pages (programs, attributes, etc.), allocating weights to individual attributes, computation of school rankings, and a review of the rank-ordered programs based on the group weights. A portion of the agenda is depicted in Fig. 5.

The subjects had to acquire information so that they could evaluate various MBA programs. Although

![](/api/attachments/MGEBTN39/fulltext/images/fbcea917d0fa972acb23ae9ea7040b5992c5291ef617218d0b64021511409788.jpg)  
(a)

<table><tr><td>Average Salary</td><td>Schools</td></tr><tr><td>77000</td><td>Massachusetts Institute of Technology</td></tr><tr><td>75000</td><td>Harvard University</td></tr><tr><td>72290</td><td>New York University</td></tr><tr><td>72200</td><td>University of Pennsylvania, Wharton School</td></tr><tr><td>69792</td><td>University of Michigan</td></tr><tr><td>68250</td><td>Northwestern University</td></tr><tr><td>66800</td><td>University of California, Los Angeles</td></tr><tr><td>65500</td><td>University of Chicago</td></tr><tr><td>62517</td><td>Carnegie Mellon University</td></tr><tr><td>57255</td><td>Indiana University</td></tr></table>

(b)  
Fig. 4. Web page: (a) individual program page; (b) programs ranked by attribute; and (c) attribute weights.

![](/api/attachments/MGEBTN39/fulltext/images/e980d223973840a4316241d515d131f72797108096aa0a781bde4738b6600dec.jpg)  
Fig. 4. (Continued ).

information can be acquired anytime during the decision-making process, it is the early acquisition of information that results in better decisions [29]. Thus, participants were allowed, at the start of each iteration, to browse the pages for individual MBA programs and program ranking by attributes. After a suitable period of browsing, the group moved to allocating weights to the attributes. All 18 attributes were displayed, and individual decision makers were required to allocate a total of 100 points to them. Upon submission of their

![](/api/attachments/MGEBTN39/fulltext/images/3e2a03e7582b2e968bf00c7d63dfdd9c0889a4d8fc04dad8cb902bcc406d17ce.jpg)  
Fig. 5. VisionQuest agenda.

![](/api/attachments/MGEBTN39/fulltext/images/7cd2e96ec014ddca1bcf55e60de4d14bce97695047f0f85c80b73890ff76e516.jpg)  
Fig. 6. Group results: allocation of weights.

allocations, the overall group allocations was made available. The group results were then used to compute the overall scores for each alternative and the rankordered list was presented. At this point, the decision makers could accept the outcome, or refine their decision on attribute weights by further iteration. The voting tool in VisionQuest was employed for this, with participants having the option to vote for or against the outcome. With a group size was of five members, it was decided that a simple majority could not serve as an appropriate stopping rule, as consensus could not be guaranteed. Accordingly, a rule requiring four positive votes in the group was adopted. Upon satisfactory termination, the participants were instructed to complete an exit questionnaire. The timestamp for completion of the experiment was recorded. A sample screen from the group activity process is presented in Fig. 6.

## 5. An experiment using the prototype

Our research sought to examine the effectiveness of collective memory on group decision support system usage. While a field research approach would undoubtedly provide a rich and representative source of data, difficulties in identifying a priori natural settings involving collective memory information systems use coupled with the paucity of subjects and potential lack of comparability among subjects rendered these approaches less appropriate. The majority of GDSS research has involved laboratory experiments using students as subjects, and has employed ad hoc rather than established groups. Laboratory experiments are easily replicable and are generally suitable for research on some decision-making processes. It is acknowledged that students are not ideal surrogates. However, the careful selection of a meaningful decision-making task with which students can readily identify can provide meaningful exploration of the question. After carefully weighing the pros and cons, this study settled on laboratory experiments using ad-hoc groups to explore the influence of collective memory on the performance of group work. Details of the experiment are presented by Paul et al. [25]. We attempted to test whether the use of collective memory in GDSS based meetings results in improvement in:

\- group consensus;

\- decision-making speed;

\- thoroughness of decision-making in terms of decision process scope;

\- thoroughness of decision-making in terms of decision process range;

\- decision quality as perceived by the group members.

## 5.1. Method

The experiment employed a randomized posttestonly control group design [3]. Given that several hundred subjects would be participating in the experiment over a period of several days, it was important to control the effects of history, maturation, and pretesting. Random assignment of subjects to treatment or control groups ensured comparability of groups. The control groups used a GDSS, and the treatment groups used a GDSS with collective memory.

## 5.2. Subjects

The experiments employed undergraduate business students at a large mid-western US university. As juniors and seniors, many of them were considering graduate programs, and motivation levels were high. A total of 270 students participated in this experiment in lieu of an assignment in a course. Each group had five members. The groups were evenly split between treatment and control groups. Subject to schedule availability of the students, participants were randomly assigned to experimental groups. Precautions were taken to address the shortcomings of previous studies reported by Fjermestad and Hiltz [7].

## 5.3. Treatment and procedures

The experiment was conducted in a decision room equipped with 20 workstations. Clusters of five workstations were formed for each group, with each participant assigned a separate workstation. Four decisionmaking groups could participate at any time. Since it was necessary for groups to proceed in an orderly fashion, a coordinator was appointed for each group. In addition to participating in the activities, the coordinator performed decision closure tasks including exporting group attribute weights to a database on the MBA programs, computing school ranking scores, and importing the ranked order list from the database using additional privileges at the group coordinator’s workstation.

The experiment started with the browsing of Web pages on MBA programs and their attributes. In addition, the treatment group participants browsed the pages on collective memory. In order to preclude the effects of history and testing, it was important to ensure that subjects had access to the browsing material only during their experiment. This was accomplished by using a limited-access Intranet to deploy the material. In addition, the use of the Intranet prevented browsing of external material. This was deemed necessary to constrain the time for decision-making as unfettered browsing would have confounded this measurement. Once the members became familiar with the situation, they allocated weights for 18 attributes. The group weights were then computed and a rank-ordered list generated. The participants then voted on their group decision and iterated until consensus was reached. At the end, each participant completed a questionnaire on the perceived decision quality.

## 5.4. Dependent variables

The dependent variables studied included: group consensus, decision-making speed, decision process scope, decision process range, and perceived decision quality. Group consensus was measured in terms of the number of votes cast in favor of the final decision (referred to as ‘‘for votes’’). Decision-making speed was measured as the elapsed time (in minutes) between the start and end of activities of each group. Decision process scope was operationalized as the total number of attributes considered by the group members. Decision process range was characterized by the total number of information pages browsed by group members. Perceived decision quality was measured using a questionnaire comprising several Likert scale items.

## 5.5. Results

A number of person-specific, demographic variables (age, gender, GPA, and Internet skill) were collected at the end of the experiment. These were

Table 6 Collective memory experimental results

<table><tr><td rowspan="2">Dependent variable</td><td colspan="2">Mean (standard deviation)</td></tr><tr><td>Control group (n = 27)</td><td>Treatment group (n = 27)</td></tr><tr><td>Group consensus</td><td>4.7 (0.5)</td><td>4.5 (0.5)</td></tr><tr><td>Decision-making speed**</td><td>37.0 (12.1)</td><td>30.9 (11.7)</td></tr><tr><td>Decision process scope***</td><td>15.2 (2.2)</td><td>13.2 (2.7)</td></tr><tr><td>Decision process range*</td><td>93.2 (32.2)</td><td>76.6 (41.5)</td></tr><tr><td>Perceived decision quality</td><td>3.58 (0.28)</td><td>3.62 (0.34)</td></tr></table>

$$
^ {*} P <   0. 1 0.
$$

$$
^ {* *} P <   0. 0 5.
$$

tested to ensure that the subjects were randomly distributed across the two sets of experimental groups, using chi-square tests for categorical variables and ttests for metric variables. The analyses revealed uneven distribution of GPA across control and treatment groups (mean GPA, 3.14 for control versus 2.98 for treatment groups; t ¼ 2:891, P < 0:001). There was no bias in the distribution of members by gender, age or Internet skill across the two groups. Subsequent data analyses used GPA as a covariate in the analysis of covariance (ANCOVA) tests.

The ANCOVA results indicated that the use of collective memory information helped study participants make faster decisions. However, the control groups surpassed the treatment groups in both scope and range of decision process. The use of collective memory did not have any significant effect on the group consensus nor did it seem to influence the decision quality perceived by the group members. Table 6 presents the basic statistics of these dependent variables.

Given the sample size, to ensure that the findings of parametric statistical tests were valid, we also conducted nonparametric tests. The results of these matched the findings in Table 6.

## 6. Discussion and limitations

The laboratory experiment revealed that the use of collective memory does speed up the decision-making process. The users of collective memory, however, browsed fewer information pages and considered fewer attributes in their work. The participants of the laboratory experiment were undergraduate business students who were presumed to be motivated to participate in the experiment—they received a waiver for an assignment in a course and were excited at the prospect of using electronic decision-room facility. However, as is the case with most laboratory research, there was no way to ensure that they put their best effort to arrive at the decision. As a further incentive, subjects were informed that an expert panel would assess the quality and performance of group work and that the grade of each student in this laboratory work would depend on this evaluation. Shirani et al. [31] found that group performance in GDSS based meetings improved when group-based incentives were offered.

We used hypermedia based information systems in this research. However, research by Huang [13] highlighted the possibility that the use of multimedia may cause decision makers to spend more time to obtain less information.

The collective memory discussed here is for small work groups. The use of GDSS for large groups has been discussed in the literature [6], with the general consensus that larger groups generate more quality ideas, and tend to reach better decisions at the expense of increased decision time [16]. We found that use of collective memory improves the speed of decisionmaking. The effectiveness of collective memory for large groups remains an open question, though we suspect that large group process losses may overshadow improvements in speed of decision-making.

The electronic meeting environment offers the possibility of conducting in-depth research on the information processing of group decision makers. The use of the Web server log file provides the opportunity for detailed analysis of participant information gathering patterns, particularly at the different phases (intelligence, design, and choice) of decision-making. The modular design of the prototype discussed here can be extended to other multi-attribute decision situations.

## 7. Conclusions

The results from the use of the prototype are encouraging. One of the objectives of using collective memory is to make group members aware of the group norms. Huang et al. [14] found that GSS groups engaged in preference tasks have attenuated normative influence; i.e., reduced level of desire to conform to the expectation of others. A reduced normative influence is likely to have negative effect on group decision outcomes. However, based on our findings, we expect that inclusion of collective memory in GSS-based meetings will help participants focus on the outcome of the other groups that were engaged in similar meetings and hence improve normative influence that is supported by the memory.

## References

[1] V. Anand, C.C. Manz, W.H. Glick, An organizational memory approach to information management, Academy of Management Review 23 (4), 1998, pp. 796–809.

[2] H. Bhargava, M. Bieber, S.O. Kimbrough, OONA, MAX and the WYWWYWI principle: generalized hypertext and model management in a symbolic programming environment, in: Proceedings of the Ninth International Conference on Information Systems, 1988, pp. 179–191.

[3] D.T. Campbell, J.C. Stanley, Experimental and Quasi-Experimental Designs for Research, Rand McNally & Company, Chicago, 1966.

[4] C.W. Churchman, R.L. Ackoff, An approximate measure of value, Journal of Operations Research Society of America 2 (2), 1954, pp. 172–187.

[5] R.L. Daft, K.E. Weik, Towards a model of organizations as interpretation systems, Academy of Management Review 9 (2), 1984, pp. 284–294.

[6] A.R. Dennis, A.R. Heminger, J.F. Nunamaker Jr., D.R. Vogel, Bringing automated support to large groups: the Burr–Brown experience, Information and Management 18 (3), 1990, pp. 111–121.

[7] J. Fjermestad, S.R. Hiltz, An assessment of group support systems experimental research: methodology and results,

Journal of Management Information Systems 15 (3), 1998-99, pp. 7–149.

[8] J.R. Galbraith, Organizational Design, Addison-Wesley, Reading, MA, 1977.

[9] M. Halbwachs, F.J. Ditter, V.Y. Ditter Trans, The Collective Memory, Harper Colophon Books, New York, 1950/1980.

[10] D.C. Hambrick, P.A. Mason, Upper echelons: the organization as a reflection of its top managers, Academy of Management Review 9 (2), 1984, pp. 193–206.

[11] B. Hedberg, How organizations learn and unlearn, in: P. Nystrom, W. Starbuck (Eds.), Handbook of Organizational Design, Oxford University Press, New York, 1981, pp. 1–27.

[12] C.W. Holsapple, A.B. Whinston, Decision Support Systems: A Knowledge-Based Approach, West Publishing, St. Paul, MN, 1996.

[13] A.H. Huang, Effects of multimedia on document browsing and navigation: an exploratory empirical investigation, Information and Management 41 (2), 2003, pp. 189–198.

[14] W. Huang, K.K. Wei, B.C.Y. Tan, Compensating effects of GSS on group performance, Information and Management 35, 1999, pp. 195–202.

[15] C. Hwang, K. Yoon, Multiple Attribute Decision-Making, Springer-Verlag, New York, 1981.

[16] H.G. Hwang, J. Guynes, The effect of group size on group performance in computer-supported decision-making, Information and Management 26 (4), 1994, pp. 189–198.

[17] L.M. Jessup, J.S. Valacich, Group Support Systems, Macmillan Publishing Company, New York, 1993.

[18] R.C.W. Kwok, M. Khalifa, Effect of GSS on knowledge acquisition, Information and Management 34 (6), 1998, pp. 307–315.

[19] K.R. MacCrimmon, Decision-Making Among Multiple-Attribute Alternatives: A Survey and Consolidated Approach, RAND Memorandum, RM-4823-ARPA, 1968.

[20] J.E. McGrath, Groups: Interaction and Performance, Prentice Hall, Englewood Cliffs, NJ, 1984.

[21] J.G. Miller, Living Systems, McGraw-Hill, New York, 1978.

[22] C. Moorman, A.S. Miner, The impact of organizational memory on new product performance and creativity, Journal of Marketing Research 34 (1), 1997, pp. 91–104.

[23] J. Morrison, Team memory: information support for business teams, in: Proceedings of the Twenty-Sixth Hawaii International Conference on System Sciences, 1993, pp. 122–131.

[24] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, Electronic meeting systems to support group work, Communications of the ACM 34 (7), 1991, pp. 40–61.

[25] S. Paul, W.D. Haseman, K.R. Ramamurthy, Collective memory and cognitive conflict group decision-making: an experimental investigation, Decision Support Systems 36 (3), 2004, pp. 261–281.

[26] M. Parent, R.B. Gallupe, W.D. Salisbury, J.M. Handelman, Knowledge creation in focus groups: can group technologies help? Information and Management 38 (1), 2000, pp. 47–58.

[27] J.W. Pennebaker, B.L. Banasik, On the creation and maintenance of collective memories: history as social psychology, in: J.W. Pennebaker, D. Paez, B. Rime (Eds.), Lawrence Erlbaum Associates, Publishers, New Jersey, 1997.

[28] K. Sandoe, L. Olfman, M. Mandviwalla, Meeting in time: recording workgroup conversation, in: Proceedings of the Twelfth International Conference on Information Systems, 1991, pp. 261–271.

[29] C. Saunders, S. Miranda, Information acquisition in group decision-making, Information and Management 34 (2), 1998, pp. 55–74.

[30] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[31] A. Shirani, M. Aiken, J.G.P. Paolillo, Group support systems and incentive structures, Information and Management 33, 1998, pp. 231–240.

[32] H. Simon, The New Science of Decision-Making, Harper and Row, New York, 1960.

[33] E.W. Stein, V. Zwass, Actualizing organizational memory with information systems, Information Systems Research 6 (2), 1995, pp. 85–117.

[34] O. Svenson, Process descriptions of decision-making, Organizational Behavior and Human Performance 23, 1979, pp. 86–112.

[35] E. Turban, J.E. Aronson, Decision Support Systems and Intelligent Systems, Prentice-Hall Inc., Upper Saddle River, New Jersey, 2001.

[36] J.P. Walsh, G.R. Ungson, Organizational memory, Academy of Management Review 16 (1), 1991, pp. 57–91.

[37] M. Weiser, J. Morrison, Project memory: information management for project teams, Journal of Management Information Systems 14 (4), 1998, pp. 149–166.

[38] D.M. Wegner, Transactive memory: a contemporary analysis of the group mind, in: B. Mullen, G.R. Goethals (Eds.), Theories of Group Behavior, Springer-Verlag, New York, 1986, pp. 185–208.

[39] I.I. Zarecka, Frames of Remembrance: The Dynamics of Collective Memory, Transaction Publishers, New Brunswick, 1994.

![](/api/attachments/MGEBTN39/fulltext/images/392ca518c1727ee55f53598932d3969f74f4ca8f68e1ce9bce4cb98fe34ea9fb.jpg)

William (Dave) Haseman is Wisconsin distinguished professor at the University of Wisconsin, Milwaukee. Dr. Haseman has a PhD in management information systems from Purdue University. He also has an MBA from the University of Wisconsin, Milwaukee. His undergraduate degree in electrical engineering is from Purdue University. Prior to joining the UWM faculty, he served on the

faculty at Carnegie-Mellon University.

Professor Haseman’s research interests are in the area of group decision-making, emerging technologies, eBusiness, Web services, and the use of the Internet for business applications. He has been the principal investigator of several major research grants from national funding agencies such as the National Science Foundation and the US Department of Commerce and has extensive consulting experience.

He currently serves as the Director of the Center for Technology Innovation, an applied research center that is actively involved in the Milwaukee area IT community. He has designed a number of custom professional education programs taught in Milwaukee area companies. He served as the conference chair for America’s Conference in Information Systems (AMCIS 1999).

He has published over 30 books, book chapters, and journal articles and has made over 50 conference presentations. His articles have appeared in Accounting Review, MIS-Q, Operations Research, Datamation, Management Datamatics, Journal of Computing and Operations Research, Journal of Socio-Economic Planning, The Computer Journal, Journal of Medical Systems, Information Systems, Information Processing and Management, Policy and Analysis and Information Systems, Database Management, International Journal of Human-Computer Studies, Information Resources Management Journal, Annual Review of Communications, and Decision Support Systems.

![](/api/attachments/MGEBTN39/fulltext/images/ba6c0ebdf9a1c9cf5acdc17fca2e9394b93d6c64135c1ec18ec47c4800a6e1e0.jpg)

Derek L. Nazareth is associate professor of management information systems at the University of Wisconsin, Milwaukee. He holds a PhD in management from Case Western Reserve University. His current research interests include application development using Web services, software reuse, data warehousing, machine learning, and knowledge base verification. His papers appear in Com-

munications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, Knowledge Acquisition, OMEGA, Information & Management among others. He is a member of AIS, ACM, and INFORMS, and was the Program Chair for AMCIS 1999.

![](/api/attachments/MGEBTN39/fulltext/images/e2c1d180dd89dbda86103dede2805357a31877137dde74eb438edde7b1ea4553.jpg)

Souren Paul is an assistant professor of management information systems at the College of Business and Administration at Southern Illinois University, Carbondale. He holds bachelor’s and master’s degrees in electronics and tele-communications engineering from Jadavpur University, India, and a PhD in management information systems from the University of Wisconsin, Milwaukee. He has published

research articles in Decision Support Systems, Information & Management, Journal of Information Systems Education, and Proceedings of Hawaii International Conference on System Sciences. His current research interests are in the areas of cognition and knowledge sharing in collaborative technology supported group work, virtual teams, and organizational knowledge management systems.
