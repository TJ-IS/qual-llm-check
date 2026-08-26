---
otero_id: 25000
otero_key: "ADSCPVVA"
title: "Business Process Modeling with Group Support Systems"
authors: "Alan R. Dennis; Glenda S. Hayes; Robert M. Daniels"
year: "1999"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1999.11518224"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Business Process Modeling with Group Support Systems

Alan R. Dennis, Glenda S. Hayes & Robert M. Daniels Jr.

To cite this article: Alan R. Dennis, Glenda S. Hayes & Robert M. Daniels Jr. (1999) Business Process Modeling with Group Support Systems, Journal of Management Information Systems, 15:4, 115-142, DOI: 10.1080/07421222.1999.11518224

To link to this article: http://dx.doi.org/10.1080/07421222.1999.11518224

![](/api/attachments/ADSCPVVA/fulltext/images/dc1310c80f5f39f7350c490f52c9f96bf65ccad7d544ccbccc197c332ed7579b.jpg)

Published online: 07 Dec 2015.

![](/api/attachments/ADSCPVVA/fulltext/images/ee1c658d661ad7d56fbc90498661ce3459a31e27f2cfeffe75c1bd0949790143.jpg)

Submit your article to this journal ↗

![](/api/attachments/ADSCPVVA/fulltext/images/b4773b3c548b554b8077eb27faf5461fdca33f1d443365c8646c49fd83bd3dd3.jpg)

Article views: 9

![](/api/attachments/ADSCPVVA/fulltext/images/36be409b3670933138d3db573a9d1ad77413812115850311d76f44aa79cc794c.jpg)

View related articles ↗

![](/api/attachments/ADSCPVVA/fulltext/images/57bab51380c2248f5cf76cd2ed9236ee30e39b658da4a0b1bac80f92be882e0b.jpg)

Citing articles: 1 View citing articles ↗

# Business Process Modeling with Group Support Systems

ALAN R. DENNIS, GLENDA S. HAYES, AND ROBERT M. DANIELS, JR.

ALAN R. DENNIS is an Associate Professor of MIS in the Terry College of Business at the University of Georgia. He received his Ph.D. in management information systems from the University of Arizona in 1991. His research focuses on groupware and Internet technologies and has appeared in MIS Quarterly, Information Systems Research, Management Science, and Academy of Management Journal. His most recent book is Data Communications and Networking (6th ed.) with Jerry FitzGerald.

GLENDA S. HAYES is a Senior Information Systems Engineer in the Software Engineering Center of the MITRE Corporation. She received her Ph.D. in management information systems from the University of Arizona in 1991. Her research interests include collaborative environments, metacatalogs, ontologies, mediation, and database middleware. She is currently supporting the Defense Information Systems Agency in programs such as the Global Combat Support System (GCSS), the Advanced Technologies Office, and the Defense Information Infrastructure, Common Operating Environment (DII COE) Data Engineering Office.

ROBERT M. DANIELS, JR. is a Senior Information Systems Engineer in the Software Engineering Center of the MITRE Corporation. He received his Ph.D. in management information systems from the University of Arizona in 1991. His research interests include group modeling processes, metadata, and database middleware. His most recent work has included support for the Defense Information Systems Agency in programs such as the Global Combat Support System (GCSS) and the Data Engineering aspect of the Defense Information Infrastructure, Common Operating Environment (DII COE).

ABSTRACT: Much process modeling research has focused on the development of new modeling languages, but very little research has examined the process by which model information is collected from subject-matter experts. The goal of this research was to develop and evaluate an alternative process to the traditional sequence of interviews or the increasingly common use of JAD (Joint Application Design) meetings run by professional facilitators/modelers. We began by selecting one commonly used modeling technique (IDEF0) and adapting its traditional modeling process to use an enabling technology of a group support system (GSS). We developed a special-purpose GSS tool to support the process and tested it through a series of eight field trials over a sixteen-month period. We then compared the new GSS-based technique with the traditional JAD technique in an additional series of eighteen field studies (nine JAD, nine GSS) over a two-year period. The results indicate that the GSS technique reduced the time required to build models by about 75 percent. Models built using GSS and the traditional JAD approach had similar numbers of syntax errors. Project managers perceived the GSS models to be as good as or better than the traditional JAD models in accurately defining the business process.

KEY WORDS AND PHRASES: group support systems, GSS, JAD, process modeling, requirements analysis.

PROCESS MODELING IS A KEY COMPONENT IN MANY SYSTEMS ANALYSIS and design and business process reengineering projects because it is important to understand, measure, and document existing processes before designing replacement processes or information systems to support them $[11, 27, 52]$ . Process modeling has many applications $[8]$ , but its role in requirements analysis (gathering, “figuring out,” and communicating “what to build” $[30, p. 31]$ ) is arguably the most important. Process modeling is one of the most commonly used techniques in requirements analysis, often taking the form of data-flow diagrams $[3, 29, 47]$ . Requirements analysis in general—and process modeling in particular—suffers from a “distressing, perhaps even shocking” lack of empirical research evaluating different approaches $[3, p. 134]$ .

Many new techniques for process modeling have been developed over the past ten years (e.g., essential systems analysis [52]; object-oriented modeling [37]); also see [8] for a summary of techniques including a dozen different process modeling languages that can be used). While these techniques differ in important ways, they all have two common structures: a language for specifying the model and a process for collecting the model's information. Most research on process modeling has focused on the language, finding new and more sophisticated ways to represent model elements and the relationships among them: "A review of this brief literature [on process modeling] will indicate that currently the field is primarily focused on properties of languages for representing processes and on process-driven environments" [8, p. 84].

Little formal empirical research has examined the process by which model information is collected $[8]$ , yet obstacles in communicating information among participants, modelers, and analysts are well documented $[2, 3]$ . Most of the tools available today are more useful for reviewing and implementing models than for initially capturing model elements and organizing them into models $[48]$ .

In this paper we present the results of a series of eighteen field studies to evaluate the effectiveness of a different process-based approach to collecting requirements: the use of a group support system (GSS; see $[32]$ ). We studied nine GSS-based projects conducted by the U.S. Department of Defense, which we compare with nine traditional non-GSS projects previously conducted by these same project managers. This approach enables us to draw some comparisons between the two approaches, but, because we did not personally observe the traditional sessions, we are unable to draw direct conclusions to explain these differences.

## Capturing Process Information

THE ESSENCE OF PROCESS MODELING IS CAPTURING and representing information about business processes [50]. Yet the methods for capturing the information for use in process models has received virtually no research attention [8]. Two information-capturing methods are commonly used in industry: interviews and joint application design (JAD) [40] (see Table 1). The technique of interviewing individuals with expert knowledge of processes has been common, in both process modeling and information requirements determination [12]. With this approach, key subject-matter experts are interviewed independently by the modeler(s). The modeler takes detailed notes from each interview and uses the notes to build an initial model. This model is then distributed back to the experts for comments and additional refinement. The model is iteratively revised and redistributed to the experts until no further changes are identified.

The key problem with the interview approach is the integration of information from experts. Experts often have slightly different views, resulting in the use of different terminology and different structures of processes and information flows. Recognizing and resolving these inconsistencies is difficult when the modeler must constantly cycle between a set of experts $[33, 49]$ . Interviewing is good for small, simple, well-understood processes; it does not work well for those that are complex, uncertain, or cross-functional $[12, 40, 49]$ .

A more commonly used approach to collect the information for a process model is the JAD meeting $[5, 37, 49]$ . Groups of subject-matter experts meet in a conference room under the guidance of a modeler/facilitator. Information is contributed verbally by the experts; the modeler records it and integrates it in the model language using flip charts, overhead transparencies, or a software tool. In some cases, CASE tools are used to support JAD meetings by augmenting or replacing the flip charts and overhead projectors with computers and video projection systems $[5, 37]$ . Keil and Carmel $[33]$ reported that facilitated JAD teams were rated more effective by developers than interviews in the development of custom software packages.

JAD provides three advantages compared with interviewing. First, JAD integrates the collection of information and the resolution of differences among the experts into one step $[49]$ . Any discrepancies among the experts are recognized immediately and can be resolved by the subject-matter experts themselves, rather than forcing the modeler to perform the reconciliation during the revision cycle. This greatly increases the productivity of modeling. Several practitioner studies suggest a 20–40 percent productivity improvement over the interview method $[7, 24, 25, 49]$ .

Second, the direct interaction of the experts with each other often improves the quality of the resulting models $[49]$ . Individuals are often poor processors of information, leading to incomplete or incorrect information specification $[12]$ . Having people interact with others in a group setting can result in a more complete understanding of the task and a better-quality product $[44]$ .

Table 1. Characteristics of Interview, JAD, and GSS-Based Information Capturing Techniques

<table><tr><td>Interviews</td><td>JAD</td><td>GSS</td></tr><tr><td>Possible to schedule meetings with as many subject-matter experts as needed.</td><td>Group process requirements usually limit participation to 5–10 subject-matter experts</td><td>Group process requirements usually limit participation to 20–30 subject-matter experts.</td></tr><tr><td>Difficult to integrate information among subject-matter experts.</td><td>Easier to integrate information among subject-matter experts.</td><td>Easier to integrate information among subject-matter experts.</td></tr><tr><td>No interaction among subject-matter experts.</td><td>Interaction among experts improves model quality.</td><td>Interaction among experts improves model quality.</td></tr><tr><td>Modeler controls model.</td><td>Facilitator/modeler controls model under the direction of the subject-matter experts.</td><td>Subject-matter experts control model.</td></tr><tr><td>Independent interviews provide opportunity for equal participation.</td><td>Vocal subject-matter experts can dominate requirements.</td><td>GSS provides opportunity for equal participation and anonymous comments.</td></tr></table>

Third, the use of JAD meetings often helps improve relations between the experts and the modelers and increases the experts' sense of ownership of the resulting models $[43, 49]$ . With the interview approach, experts often do not feel fully involved in the modeling process. Because the modeler is their primary point of contact, experts may wrongly interpret any changes as coming from the modeler, not from other experts. In JAD meetings, the direct interaction among the experts ensures that the source of all changes is clear.

It is critical that the subject-matter experts be directly involved and share control of the model with the modeler $[30]$ , something that does not always occur. The meeting facilitator or modeler can be viewed as a bottleneck and a filter. Nothing gets into the model until is understood, translated, and/or categorized by the modeler. As long as the model is controlled by the modeler, participants may not feel the desired degree of model ownership.

The major problems with the JAD approach are those traditionally associated with meetings. A limited number of people can participate effectively before the meeting becomes inefficient; most researchers believe the maximum effective group size is five [44], which is far smaller than the usual number of participants in modeling and JAD sessions, which often involve ten to fifteen [8, 43, 49].

One of the reasons for assembling a group of experts is because no one expert usually has sufficient information and expertise to document business processes completely and accurately. It is important to draw information from all experts attending the meeting. However, another key problem in verbal meetings traditionally used for JAD is that only one person can speak at a time. Members must take turns speaking and those not speaking are blocked from contributing their ideas and information until they can find a break in conversation. This leads to several problems, as experts who are blocked from contributing their information and ideas as they occur may forget or suppress them because they seem less relevant or less original at a later time [19, 34]. Key information is omitted. Also, a few members often dominate, with others saying little [44]. This domination and inequality of participation and influence can lead to poor-quality models that favor the dominating participants [22].

## Group Support Systems

In recent years, computer technology designed to reduce these group interaction problems (group support systems, or GSS) has been adopted with moderate success by a number of organizations $[32]$ . In this paper, we focus on same-time, same-place GSS, in which group members use computers to interact and exchange ideas and information, instead of and in addition to discussing information verbally. This has also been called an electronic meeting system $[16]$ . A GSS provides at least three functions that may improve meetings: (1) parallel communication; (2) anonymity; and (3) group memory $[18, 38]$ .

In a verbal meeting, if ten experts participate equally in a one-hour meeting, each expert spends six minutes contributing information and fifty-four minutes listening (or at least not contributing). With GSS, all members can type information and ideas simultaneously, and the software shares them with all participants. This parallel communication reduces blocking, enabling participants to contribute simultaneously, so that information is collected faster $[45]$ .

Anonymity may improve meetings by separating personalities from the problem. Individuals, particularly low-status participants, may withhold ideas out of apprehension of a negative evaluation $[19, 34]$ . Participants may also feel a pressure to conform to the group majority or senior participants' views, whether intended or not $[26, 31]$ .

A group memory is provided by electronically recording all information so that participants can immediately see information entered by others. This should enable members to better integrate information and reduce problems that occur when they inaccurately remember issues previously discussed $[19, 31]$ . Participants can also decouple themselves from the group to pause, think, and then rejoin the “discussion.” By enabling participants to concentrate on the work of others, the opportunity for “process gains” from synergy and learning should increase $[28, 45]$ .

GSS may also introduce some negative effects into the meeting process. Electronic communication is often seen as less “rich” than face-to-face verbal interaction $[10]$ . While media richness appears to be unimportant for information exchange $[41]$ , it may be critical for reducing the equivocality that arises when there are multiple and conflicting interpretations of information $[9]$ . The implication is that, while the parallelism, anonymity, and group memory offered by the electronic communication found in GSS may be valuable for the generation of information, resolving differences among experts may be done best through verbal interaction.

A recent metaanalysis of GSS research concluded that, in general, GSS use may increase the quality of group work but often increases the time required to complete the task $[17]$ . Effects were found to depend greatly on the size of the group. For larger groups, GSS was found to produce greater gains in quality with few increases in the time required. Likewise, while the electronic communication provided by the GSS improved performance on idea-generation tasks (and by implication the generation of information for models), a combination of electronic and verbal communication was found to be the best for decision-making tasks that required participants to resolve differences of opinions.

There have been several studies of GSS use for JAD sessions. Dennis et al. [15] and Liou and Chen [35] present the results of two initial attempts to develop GSS designed to support JAD sessions. Both studies were pilot studies and, while their results are promising, they were too small to determine whether GSS use improved quality or productivity.

Two other field studies have compared GSS-based JAD approaches with more traditional JAD approaches. Both used samples that were too small to allow statistical conclusions about the effectiveness of GSS-based JAD. Carmel et al. [4] found few differences between the two approaches. Dean et al. [13] studied three GSS-based JAD projects and five traditional JAD projects and found that GSS projects were completed about 200 percent faster but contained slightly more errors. Both studies concluded that the use of GSS promoted more equality of participation and led participants to believe that they played a larger role in defining the system's needs (i.e., had greater ownership of the results). They also noted that coordination among participants and the resolution of conflicting opinions was not performed very well in some of the GSS sessions, a key weakness that has the potential to cause serious problems later on; after all, the main point of using JAD sessions is to resolve these conflicts early.

## Developing a GSS-Based Process Modeling Technique

In order to test the effects of GSS use on process modeling, we needed to develop a GSS-based approach and supporting GSS tool(s). The first task was to select a business process modeling language and technique. We wanted a well-established, standardized technique with a history of success and good prospects for continued use. We chose IDEF0 [1, 21], a successor to SADT [42], and the technique mandated for all process improvement and system development projects by the U.S. Department of Defense (DoD) [20]. IDEF0 is also one of the techniques studied in previous research [4, 13, 14, 50].

According to the Curtis et al. [8] classification, IDEF0 is both a functional technique (representing what process elements are performed and their information flows) and an organizational technique (representing where and by whom process elements are performed), with some elements of an informational technique (representing the structure of the information used). IDEF0 is also one of the few formal process modeling techniques to have been the focus of empirical research. Research comparing

IDEF0 with other process modeling techniques (e.g., data-flow diagrams) has found no significant differences [50]. This section examines the major components of the IDEF0 language and process.

## IDEF0 Language

The fundamental building block of an IDEF0 model is the activity, which may be decomposed into subactivities, sub-subactivities, and so on. Activities are decomposed into subactivities (also called “children”), which, in turn, are decomposed into sub-subactivities (“grandchildren”), and so on. Activity numbers show the decomposition. Activity A11 is the child of activity A1. Activity A111 is a child of A11, as is A112, and so on. A list of activities and children is called an “activity tree” because it looks like a genealogy, or “family,” tree. Under IDEF0 rules, any activity that is decomposed into children must have three to six children.

Each activity has a set of ICOMs: Inputs (information or physical things), Controls (rules or policies that guide how the activity is performed), Outputs (information or physical things), and Mechanisms (resources used to perform the activity such as people and information systems). ICOMs define how the activity interacts with other activities and entities outside the model and are conceptually similar to the data flows in data-flow diagrams (DFDs). ICOMs can be decomposed, so that ICOMs at parent activities are gradually decomposed into more detailed ICOMs as the children activities (e.g., Reports at A1 becomes Personnel Reports, and Finance Reports at A11). Space precludes a complete description of IDEF0; see $[1, 21]$ .

## IDEF0 Process

The IDEF0 standard formally specifies an interview-based process to collect information from the subject-matter experts $[21]$ . We conducted an informal survey of twenty-four members of the IDEF Users Group and discovered that not one used the process as defined by the standard. Almost all used JAD techniques. Pure JAD calls for a scribe selected from the group and allows programmer/analysts to observe but not participate. The JAD as practiced for IDEF0 usually has a trained modeler (possibly the facilitator) operating the IDEF0 tool used to record the model.

The JAD groups usually work together with all members focusing on the same part of the model at the same time. Groups usually work “top-down” through the model following a breadth-first search technique, so that the highest level of the model (i.e., A0) is developed completely. Then the next level with all of its activities and ICOMs is developed completely (A1, A2, A3, etc.), then the next (A11, A12, A13, A21, A22, etc.), and so on until the model is complete (see [21]). In practice, there is a lot of iteration, as developing lower-level activities (e.g., A11) in detail often identifies problems in the structure of the higher-level activities and their ICOMs, requiring that the higher-level activities be reworked. At the end of the JAD meeting, which typically lasts many weeks, the group has produced what is called a “working” model. This model is then revised and improved by the modeler, the project manager, and senior managers, before an “official” version is published.

## An IDEF0 GSS-Based Process

The first question was how to adapt the traditional JAD-based IDEF0 process to incorporate GSS. One of GSS's most important features is the parallelism offered by electronic communication. However, the integration of information and the resolution of different interpretations may be best done verbally [9]. Verbal discussions allow for a stable object of review while parallel electronic revisions may lead to vacillations between differing opinions in a “last one wins” cycle. We concluded that any approach had to be primarily parallel in nature, but with the opportunity for rich verbal interaction to resolve differences of opinion.

Anonymity is important for the delivery of criticism $[6]$ . Thus, we wanted to ensure that any critical feedback was provided anonymously. When all participants work together on the same task, particularly modeling, a group tool that immediately enables everyone to view the work of others is useful in ensuring consistency and easier integration of the parts of the model developed by different participants. Each participant should be able to review the shared model independently as well as to access the group memory (archived versions that have been replaced or deleted). Such a shared memory (or “repository”) is a common feature in CASE tools. Thus, the basic concept of the GSS-based process was: parallel development of the model by all participants using a group memory, anonymous critiquing of the model, and verbal resolution of conflicts.

The general process we developed for GSS-based IDEF0 process modeling has two principal phases, plus an introduction and a conclusion (see figure 1). The first principal phase is activity definition, during which all activities are developed and refined. The second principal phase is ICOM definition, during which all Inputs-Controls-Outputs-Mechanisms are defined. This figure also shows the typical time spent in each step for a five-day-long process.

## Activity Definition

After some initial training on activity modeling with IDEF0, the group as a whole discusses the overall business process (A0) and identifies a set of three to six high-level activities. This set of activities forms an overall map of the business process to be modeled that is well integrated and internally consistent, and every participant needs to understand it. Here, the goal is to develop a very short, unequivocal, well-understood list of activities. The potential contributions of parallelism provided by electronic communication (the rapid collection of a large volume of information) are outweighed by the need to reduce equivocality and ensure that all participants have a shared understanding. Therefore, this step uses a chauffeured process in which the group verbally discusses the activities and the facilitator records the key points using the GSS as an electronic blackboard $[38]$ .

Once these three to six high-level activities are defined and well understood, they are decomposed into subactivities. The goal here is the rapid and simultaneous definition of lower-level activities. Parallelism is key. At this point, the group of experts is divided into subgroups of three to five members, who are assigned to decompose one or more of the high-level activities into subactivities, sub-subactivities, and so on, and to write definitions for them. For example, one subgroup may work on activities A1 and A2, while another does A3, and so on. Subgroups are generally formed by the participants themselves, based on their areas of expertise, and usually remain intact for the duration of the project.

![](/api/attachments/ADSCPVVA/fulltext/images/7b0e106d1f10155a27e4a41685de89a252b273a385a023993e26b386999ad768.jpg)  
Figure 1. GSS-Based Process (and Supporting GSS Tools)

Subgroups usually follow the same approach followed with the high-level activities. They begin with a verbal discussion with only one member using the GSS. Once the major subactivities for their high-level activity(ies) have been identified and discussed, the subgroups often subdivide into smaller subgroups of one or two members each and work on the activities separately but with close coordination among subgroup members.

In this way, the three to six major activities are developed in parallel. Consistency is improved by enabling everyone to view the entire model. The use of subgroups helps resolve inconsistencies by having the experts resolve issues within their subgroup before they are entered into the model. The facilitator(s) acts as a coach, providing advice about IDEF0 syntax rules and monitoring the shape of the emerging model to encourage consistency and quality. Subgroups are encouraged to actively view the work of other subgroups to identify and resolve (by informal discussion among subgroups) potential inconsistencies before they develop into major issues.

The next stage is a model review. Once all the subgroups have completed the initial decomposition and definitions, the entire group reconvenes to discuss the initial model. The goal for this step is to generate ideas to improve the model, so each participant works individually to review all the activities and definitions, using a GSS brainstorming tool (which is likely to produce more ideas than discussing the model verbally [23]). Participants can anonymously raise issues, which can encourage reticent members to participate. The participants classify the comments as critical issues that the group as a whole needs to discuss and resolve, minor issues that need little discussion (e.g., spelling), or misunderstandings that can be dropped. Minor issues are organized by area, printed, and assigned to the subgroup responsible. Critical issues are discussed verbally by the entire group, one by one, with the facilitator chairing the discussion, until each issue is resolved or it is apparent that agreement will not be reached without additional information or outside intervention. The facilitator and the entire group take ownership of the issue, rather than forcing an individual to challenge a subgroup. This resolution of conflicting model interpretations is important to ensure quality [4, 15]. Then each subgroup revises its part of the model, based on the minor comments and the resolution of the critical issues.

## ICOM Definition

The basic process for the ICOMs is similar. After receiving training on ICOM modeling, the subgroups develop an initial definition of the ICOMs and their connections, which also often leads to refinements of activities. Experts are encouraged to work bottom-up: that is, they define the ICOMs at the lowest level in the model first, and then carry them up to higher levels. ICOMs are defined bottom-up because it is the information flows and mechanisms at the bottom of the model that represent “real” things (forms, memos, policies, people). ICOMs attached to higher-level activities are typically aggregations or abstractions of actual things. In our experience, experts with little prior IDEF0 modeling experience find it easier to provide ICOM details first and then abstract them to higher-level entities, rather than thinking in the abstract first.

Each subgroup creates and defines ICOMs for the activities it has been assigned. As ICOMs are added to the model by one subgroup, they can be immediately seen by other subgroups. For example, if the subgroup modeling activity A1 defines an output to A2, the subgroup modeling A2 immediately sees the ICOM as an input (or a control or mechanism). Subgroups whose activities exchange many ICOMs are encouraged to talk about them to better integrate the information, rather than just adding them into the model without discussion.

Once the initial definitions of each subgroup are complete, the overall model is again reviewed. This in turn is followed by a final stage with each subgroup refining its area of the model based on the group's feedback and then consolidating the lower-level ICOMs into higher-level ICOMs (e.g., income statement and balance sheet at the lower levels become financial statements at higher levels).

The final stage is an overall review of the model and final revisions. At this point the “working” model is complete, and usually subjected to additional model review by the management team before the model is officially published.

## Technique Validation

We developed a new GSS software tool to capture the IDEF0 model elements and display them graphically. The prototype group-IDEF0 tool provided parallelism, anonymity, and group memory. It was used in conjunction with other general-purpose GSS (either GroupSystems or VisionQuest) that were used during model reviews to collect participants' comments.

The GSS process and the supporting software (our tool and either GroupSystems or VisionQuest) were pilot tested and refined through a series of eight modeling projects with both the DoD and private-sector corporations over an eighteen-month period. After each project, we analyzed the results and made changes to the process and the software. The software underwent considerable changes over this period. The techniques by which we used the software (e.g., training, instructions to the participants) also changed, but only moderately. The fundamental process changed little. At the end of this pilot-test stage, we were convinced that the process and supporting software were ready for formal testing. Therefore, we developed the hypotheses below and conducted the empirical study described in the remainder of the paper. None of the eight projects from the pilot-test stage was included in the formal empirical tests of the hypotheses; we collected entirely new data for the hypothesis tests because the process and software used in the initial pilot tests were different from those that emerged from the last pilot tests.

## Hypotheses

There are at least two key aspects of process modeling: (1) productivity or efficiency (the amount of time and resources it takes to produce the model), and (2) quality or effectiveness (the ability to capture and present the process in an accurate and understandable form) [50].

## Productivity

First, the GSS-based process was designed to leverage the inherent parallelism associated with the cross-functional nature of the groups, so that different parts of the model would be developed simultaneously. Second, the use of a GSS, designed to permit many experts to participate simultaneously rather than taking turns to speak, during the building of the model and the model review stages, should reduce production blocking. Third, the access to a single model in a shared group memory should help participants better integrate their different model elements, thus reducing time and effort spent on integration. Previous case studies suggest that GSS use may improve productivity in some cases $[13]$ , but not in others $[4]$ . We hypothesized that the use of a GSS process should improve productivity; models should be built in less time:

H1: Groups using GSS-based processes and tools will build IDEF0 models more quickly than groups using traditional JAD processes and tools.

## Model Quality

There are two distinct aspects of process model quality: syntactic correctness and semantic correctness [50]. Syntactic correctness is the extent to which the model conforms to the syntax rules of the modeling language. Models that do not abide by language rules are more difficult to understand by those experienced in the language, and are more difficult to integrate with other models using that language. Semantic correctness is the extent to which the model accurately and completely defines the business process (i.e., is a useful depiction of the process). A model that is syntactically correct but not semantically correct is misleading, while a semantically correct model that is syntactically incorrect may be difficult to understand or present different meanings to different readers.

There is often a tradeoff between syntax and semantics. For example, an activity that has seven inputs violates the syntax rules but may be the most accurate representation of the current process. Model analysts and facilitators are typically more expert in the syntax of the modeling language, while the subject-matter experts are better versed in the semantics of the business process. In the traditional process, the model is built by the facilitator (the syntax expert), based on information from the subject-matter experts (the semantics experts). One could argue that this approach emphasizes syntax over semantics, or at least filters the semantics through a syntactic lens.

Furthermore, current IDEF0 modeling tools often reject entries that violate syntax rules.

With the GSS-based process, the experts themselves build the model, with coaching from the facilitators and analysts. In this case, the experts have greater control of the model contents; they no longer have to convince the facilitator to record what they say, but instead can directly interact with the model itself. This should improve the semantic correctness of the model, at least to the extent that the experts are truly expert in the topic area, as it removes one potential source of “noise” in the recording process. However, the subject-matter experts will generally have less experience in IDEF0 modeling. Their knowledge and use of the IDEF0 language will likely be poorer than those of expert IDEF0 modelers. Thus, prior research suggests that models built using GSS are lower in syntactic quality $[13]$ . Therefore, we hypothesized:

H2: Models built by groups using GSS-based processes and tools will exhibit lower syntactic quality than models built by groups using traditional JAD processes and tools.

H3: Models built by groups using GSS-based processes and tools will exhibit greater semantic quality than models built by groups using traditional JAD processes and tools.

## Method

GIVEN THE COMPLEXITY AND TIME REQUIRED TO BUILD IDEF0 models, we chose a field-based research strategy. We studied nine business process models developed using GSS-based processes and tools and nine models developed using traditional JAD processes and tools. These nine GSS models were a totally different set of models than those used in the validation process.

## Projects and Participants

In selecting the projects to study, we decided to focus solely on projects conducted within the U.S. Department of Defense. The DoD has a well-defined standard for IDEF0 modeling and has a lot of experience with IDEF0. The projects were selected deliberately, not randomly, as deliberate selection is preferred in this type of research $[51]$ . Table 2 summarizes the projects.

The GSS projects were identified by our DoD research sponsors to span a range of sizes and complexities. The traditional JAD projects were identified by asking the managers of the GSS projects to provide information on a recently completed IDEF0 project they had managed that they believed was similar to their GSS project in terms of scope and complexity. We believed that the project managers were the best judges of similarity since they were the subject-matter experts who had actively participated in both projects. The nine project managers identified a total of thirteen projects. Rather than include all thirteen, we selected a subset of nine projects to compare with the nine GSS projects. We deliberately chose to bias the sample to favor the traditional

Table 2. Project Summary

<table><tr><td rowspan="2"></td><td colspan="3">Number of</td></tr><tr><td>Days</td><td>People</td><td>Activities</td></tr><tr><td colspan="4">GSS projects</td></tr><tr><td>CoE Installation Management</td><td>4</td><td>15</td><td>165</td></tr><tr><td>CoE Real Estate Installation Management Planning</td><td>3</td><td>6</td><td>43</td></tr><tr><td>Army Installation Budget Preparation</td><td>5</td><td>22</td><td>109</td></tr><tr><td>Army and Marine Corps Battlefield Logistics</td><td>13</td><td>60</td><td>375</td></tr><tr><td>Joint Theater Combatant Logistics</td><td>14</td><td>75</td><td>224</td></tr><tr><td>Logistics*</td><td>5</td><td>12</td><td>173</td></tr><tr><td>Logistics*</td><td>5</td><td>8</td><td>108</td></tr><tr><td>Army*</td><td>3.5</td><td>18</td><td>108</td></tr><tr><td>Joint Test Assets Database</td><td>4.5</td><td>9</td><td>86</td></tr><tr><td colspan="4">Traditional projects</td></tr><tr><td>CoE Real Estate Installation Services</td><td>22</td><td>7</td><td>103</td></tr><tr><td>CoE Real Estate Overall Installation Management</td><td>20</td><td>6</td><td>65</td></tr><tr><td>CoE Real Estate Installation Property Recording</td><td>24</td><td>9</td><td>72</td></tr><tr><td>CoE Real Estate Installation Property Management</td><td>27</td><td>6</td><td>65</td></tr><tr><td>Army Installation Management</td><td>40</td><td>9</td><td>47</td></tr><tr><td>Army Battlefield Logistics</td><td>35</td><td>6</td><td>165</td></tr><tr><td>Army Corporate Logistics</td><td>100</td><td>17</td><td>385</td></tr><tr><td>Marine Corps Ground Maintenance Logistics</td><td>30</td><td>13</td><td>76</td></tr><tr><td>Army*</td><td>80</td><td>6</td><td>106</td></tr></table>

\* Identity is confidential.  
CoE = Corps of Engineers.

JAD approach by eliminating the four projects that had the lowest productivity and quality.

One key concern in field-based research of this type is to what extent the two samples are “similar.” The management teams responsible for both sets of projects believed they were similar—and we believe this is the single most important test of similarity. Furthermore, there were no statistically significant differences in the number of activities $t(17)=0.71, p<=ns$ , and both had a mix of large projects and small projects. Both had similar types of processes: installation management and logistics. Most participants were similar in rank (mostly majors [O4/GS13] and lieutenant colonels [O5/GS14], with a few higher and lower ranks). About 30 percent of the participants in the GSS groups and about 50 percent in the traditional groups had prior process modeling experience. Four of the GSS projects were interservice projects that involved participants from two or more services (e.g., Army, Navy, Marines, and Air Force). All of the traditional projects were single-service. Interservice projects are generally regarded as more complicated and problematic than single-service projects because there are more opportunities for cultural, political, and terminology differences among participants.

One difference was the number of participants. GSS projects involved significantly more participants, about three times as many as the traditional projects (means = 8.78, 25.00, t(17) = 2.37, p <= 0.030). The project managers in the GSS projects chose to increase the number of participants to gain a wider representation into the process. This has the potential to increase productivity because there were more people to work. It also has the potential to decrease productivity because more people must agree on the contents of the model. In either case, productivity measures that equalize for the different number of participants are required.

All of the traditional projects were facilitated by experienced professional IDEF0 facilitators hired from leading consulting firms with a practice specializing in IDEF0 modeling. The GSS projects were facilitated either by the research team (projects 1, 6, 7, 9), by Army personnel (projects 3, 8), or jointly by both (projects 2, 4, 5). It is difficult to assess the individual abilities of the facilitators, but, in general, the professional facilitators on the traditional projects and the research team facilitators on the GSS projects had similar levels of experience. The Army personnel who facilitated two GSS projects by themselves had far less experience; they had assisted in four prior projects under the supervision of a research team, but otherwise it was the first or second time they had facilitated a process modeling project.

In summary, there appears to be a reasonable degree of similarity in the size and type of processes modeled between the GSS and traditional projects, although the traditional models were selected to bias the sample in favor of the traditional models. Participants in the traditional projects had more experience with modeling, and were more likely to come from the same service, differences that could bias the results in favor of the traditional projects. Likewise, the facilitators in the traditional projects had slightly more experience, again biasing the study in favor of the traditional projects.

## Measures

Information was collected from two sources. First, for each project, the project manager and three to seven participants were interviewed. We used the interviews to collect background information, to understand participants' perceptions of the projects, and to better understand the differences between the GSS and traditional processes. Second, the project reports were examined. For the nine GSS projects, this was the "working" report completed immediately after the project meetings. No "working" reports were available for any of the traditional projects, so we used the "official" report completed after the "working" report had been reviewed, corrected for errors, and refined by the management team.

## Productivity

The measure for productivity was the amount of meeting time required to collect the model information from the group of subject-matter experts. The actual size of the business process model and the number of participants involved differed on a case-by-case basis. Therefore, to provide a standard productivity comparison across cases, we used two measures: the number of activities modeled per day and the number of activities modeled per person-day.

We counted the number of activities in each model and the number of days and person-days that the group of experts spent working on the project in the JAD or GSS meetings before the “working” report was completed. This included all work on the process model, plus all briefings, training sessions, and discussions related to process modeling. In some of the meetings, the groups performed activities other than process modeling (e.g., data modeling); this time spent on nonprocess modeling activities was not included in the measure.

## Quality

We used two measures of model quality. Syntactic quality, defined as the extent to which the model conformed to IDEF0 rules, was assessed using the rules for assessing model quality in the Air Force IDEF0 standard (see [1, § 6.1 and 6.2]). These rules included the number of subactivities per parent activity (minimum 3, maximum 6), the number of inputs per activity (maximum 6), the number of controls outputs, and mechanisms per activity (minimum 1, maximum 6), and the presence of definitions for all activities and ICOMs.

One rater assessed the syntactic quality of the models by counting the number of activities with errors, expressed as a percentage of the total number of activities. A second rater assessed the quality of six randomly selected models (three GSS; three traditional). Interrater reliability (alpha) was 0.93, indicating adequate agreement, so the first rater's assessment was used.

This measure was biased in favor of the traditional projects, because it compared the “working” project reports for the GSS projects with the “official” project reports for the traditional projects. These “official” reports had undergone further refinement and quality improvement processes not performed on the “working” GSS reports (this extra time spent on refinement was not included in the productivity measures).

The second measure was semantic quality, defined as the extent to which the model accurately and completely defined the business process. There are no generally accepted rules for assessing semantic quality. No DoD or FIPS document discusses it. However, we believe that semantic quality is at least as important as syntactic quality. Ideally, we would have used a questionnaire or a panel of experts to assess quality. However, we did not have access to participants in the traditional projects and no one person had knowledge of all systems and was therefore able to judge the extent to which the model accurately represented the process.

We therefore used a simple qualitative approach to measure semantic quality. Project managers were asked to assess whether the semantic quality of the GSS projects was the same as, better than, or worse than the semantic quality of previous traditional projects on which they had worked that were similar to the GSS project. We stressed the need not to provide what the respondent might see as the “socially desirable" answer that the GSS projects had higher quality. While this approach lacks the quantitative purity of a questionnaire or panel of judges, we believe it is adequate, provided the results are used with caution.

## Results

## Productivity

TABLE 3 PRESENTS A SUMMARY OF THE RESULTS. GSS projects required significantly less time to complete, using either the number of activities per day (t(17) = 7.35, p < 0.001) or number of activities per person-day (t(17) = 4.08, p < 0.001). GSS groups produced models about 8.5 times faster in terms of activities per day, or about 4.5 times faster in terms of activities per person-day. Hypothesis 1, that GSS modeling is faster than traditional approaches, is supported.

As an aside, we noted earlier that the traditional groups received much more training than did the GSS groups. This increased training might affect our measures of productivity, because time spent in training reduces the amount of time spent modeling. If we eliminate the time spent in training from the productivity calculations for the traditional groups, their productivity (measured in activities per person-day) increases from 0.39 to 0.48, but this is still statistically significantly below the 1.80 level of the GSS groups, even without eliminating the GSS groups' training time from the calculations $t(17)=3.78, p=0.001$ .

## Quality

The first measure was syntactic quality, the percentage of activities with errors. There were no statistically significant differences in the error rate between GSS and traditional projects $t(17)=0.35, p=\mathrm{ns}$ . Two models (one GSS, one traditional) had error rates over 50 percent. If we omit these potential outliers, error rates fall to 13 percent for the GSS models and 14 percent for the traditional models, with still no statistically significant differences $t(15)=0.28, p=\mathrm{ns}$ . Hypothesis 2, that syntactic quality would be higher in traditional JAD projects, is not supported.

Semantic quality was based on the perceptions of the GSS project managers. Six perceived the GSS models to be of higher quality; three perceived no differences in quality; none perceived the GSS models to be of lower quality. Based on this qualitative evidence, we conclude that hypothesis 3, that the GSS models would be higher in semantic quality, is partially supported.

## Discussion

WE THEORIZED THAT BY TAKING ADVANTAGE OF THE PARALLELISM, anonymity, and group memory offered by a GSS, a GSS-based process modeling process might enable groups to produce models faster than groups using traditional JAD processes. The results of this study are promising. Groups using GSS-based modeling processes and tools developed models about four and a half times faster than groups using traditional processes and tools. There were no significant differences in syntactic quality, the extent to which the models conformed to IDEF0 syntax rules. Project managers perceived the models from the GSS process to be at least as accurate in defining the processes (i.e., semantic quality). This is even more interesting when one considers that the project sample and measures were biased in favor of the traditional projects.

Table 3. Results

<table><tr><td rowspan="2">Measure</td><td colspan="2">Traditional</td><td colspan="2">GSS</td><td rowspan="2">t</td></tr><tr><td>Mean</td><td>Std</td><td>Mean</td><td>Std</td></tr><tr><td colspan="6">Productivity</td></tr><tr><td>Activities per day</td><td>2.99</td><td>1.29</td><td>25.38</td><td>9.05</td><td>7.35*</td></tr><tr><td>Activities per person-day</td><td>0.39</td><td>0.23</td><td>1.80</td><td>1.01</td><td>4.08*</td></tr><tr><td colspan="6">Syntactic quality</td></tr><tr><td>Error Percentage</td><td>17.56</td><td>15.80</td><td>20.39</td><td>19.17</td><td>0.35</td></tr><tr><td colspan="6">*p&lt;0.001.</td></tr></table>

These results show considerable promise for GSS-based process modeling. They are, of course, from only one study and thus suffer from the traditional limitations of field-based research of this kind. The major strength—and weakness—of this study, and of other field-based studies like it (e.g., [13, 14]), is that we studied real groups working on real projects. These groups were not subject to well-controlled laboratory conditions and were not randomly assigned to their projects or to the GSS or traditional JAD conditions under which they worked; controlled conditions and random assignment are not desirable for this type of field research [51].

As with all field research of this type, this lack of control raises the concern that the GSS projects may have differed in some meaningful way from the traditional JAD projects. While we believe that the two did not differ in any meaningful way (or, if they did, the difference favored the traditional JAD groups), the possibility remains that some unknown factor other than the use of GSS may account for the differences between the traditional projects and the GSS projects. Our results are similar to prior research (see $[13]$ ), but we caution readers to draw conclusions carefully. In the sections below, we consider the possible explanations for these effects, identify some of the problems we encountered, and draw implications for managers and researchers.

## Productivity Gains

On average, models built using the traditional JAD approach required just over eight weeks to complete (median six weeks), while models using GSS required just over one week (median one week). The time required depended on the complexity of the models. The largest of the traditional models (385 activities) required twenty weeks, while the largest GSS model (375 activities) required three weeks.

We attribute the majority of the increased productivity of the GSS groups to four factors. First, subsets of the model were developed concurrently. Rather than having all experts focus on the same part of the model and discuss it verbally, several subgroups developed three to six portions of the model in parallel. There were usually four subgroups working on the GSS projects, so this would suggest that GSS should produce models about four times faster, presuming, of course, that there were no productivity losses due to the need to integrate the different parts of the model. The actual productivity differences were about 8.5 times faster (using the improvement in the number of activities per day). This suggests that the use of subgroups working in parallel accounts for about half of the productivity improvements we observed (i.e., 4 times increase out of an observed 8.5 times increase). This use of subgroups to work on separate parts of the model can also be done without the use of GSS, something we discuss in more detail below.

Second, the GSS modeling software, which provided independent concurrent access to the model and a group memory, enabled participants and facilitators to better integrate the different model components among the subgroups. Everyone had access to the latest updates of others' work, which enabled participants and facilitators to identify potential problems quickly as they were beginning to occur, not after they were complete. It was not uncommon for members of one subgroup to discover a potential problem in the work of another subgroup, and for them to approach the other subgroup quickly and verbally discuss the issue to resolution, before either group had invested much time or ego in the problem. This early resolution of problems reduced the time required to complete the model.

Third, use of the general-purpose GSS proved invaluable in promoting discussion of the model, particularly open criticism. Parallelism gave everyone, even the most reticent member of the group, the same opportunity to propose changes to the emerging model. Anonymity encouraged participants to deliver criticism more directly (with “less sugar coating,” according to one participant). Thus, the use of parallelism and anonymity to raise issues made the verbal discussions of the issues more efficient and focused.

Fourth, verbal discussions focused only on major disagreements. The group did not waste time discussing issues on which they agreed. Likewise, the group's discussion time was not spent on minor issues, since these were captured electronically. The use of the GSS to capture the major issues of disagreement tended to focus discussion on the issues, again promoting less wasted time. There were few digressions and, when digressions began, the facilitator was able to bring the discussions back to task by referring to the electronic comments under discussion (e.g., “How do we change the model based on this comment?”).

In most cases, disagreements were resolved through verbal discussion, either by resolving differences in understanding or by identifying different requirements and incorporating both positions. In a very few cases, the groups resorted to using the GSS voting tools to settle issues, with the group majority opinion “winning.” In one of these cases, a Navy captain was outvoted, but refused to be swayed. He called his admiral, and the admiral made it clear that if the Navy did not win the point, the Navy would withdraw from the project. The group accepted the Navy position and carried on. So, while the GSS voting tools did help occasionally, major decisions were more likely to be made by verbal discussion and group consensus than strict democratic majority vote through the GSS.

## Quality

One of the major differences between GSS and traditional approaches was that the subject-matter experts themselves played a larger role in the specification of the model. The facilitator was no longer an intermediary between the experts and the model; rather than relying on the facilitator to express their thoughts in the model, the experts worked directly with the model.

## Syntactic Quality

There were no differences in syntactic quality, suggesting that the participants' initial lack of experience with the modeling language did not prove a major stumbling block. We attribute this lack of syntactic quality differences to three factors.

The first was the relative complexity of the traditional process compared with the GSS process. In all but one of the traditional projects in this study, participants received one week of IDEF0 training. They were taught all aspects of the language in some detail. When the group began modeling, they were expected to use all of the knowledge they had gained. They defined the first activity in detail, added its ICOMs, defined its ICOMs, decomposed that activity into its children activities, and decomposed the ICOMs into children ICOMs. This was then repeated for each activity. Thus, for each activity, five rather complex actions were performed.

In contrast, the GSS process separated activity definition and decomposition from ICOM definition and decomposition to minimize the cognitive effort and the learning required by the experts. Participants in the GSS projects received an initial overview of IDEF0 for about an hour, followed by a series of three ninety-minute just-in-time training sessions interspersed throughout the modeling process. Each of these just-in-time sessions covered the essentials of the imminent modeling phase. Thus, participants' IDEF0 knowledge was chunked to minimize the learning required, and the process was designed to minimize the number of concepts the experts had to use simultaneously.

The second factor was the coaching done by the facilitator. The IDEF0 training provided to members of the GSS groups did not cover all the syntactic and semantic rules in IDEF0, just the major ones. If some part of the model violated other rules, the facilitator would explain the rule and help the group or subgroup revise the model to accommodate it. The facilitator constantly monitored the process, the model, and the subject-matter experts to ensure that all was proceeding as planned. If participants experienced problems or needed to be reminded of or introduced to an IDEF0 rule, the facilitator coached the participants through the issues, helping them to find a solution and gain a better understanding of the language rules.

The third factor was the formal model review process. The model was formally reviewed by all participants at least three times for syntax and semantics. The facilitator regularly reviewed the model to ensure that any rule violations were corrected. Finally, in three projects, one member of the management team, an IDEF0 expert, was designated to review the model for syntactic and semantic errors every evening or every second evening, and to report any items to the group at the start of the next day.

## Semantic Quality

Project managers perceived the semantic quality of the GSS projects, the extent to which the models accurately defined the process, to be equal to or higher than the traditional projects. There are three possible reasons for this. First, the experts felt a strong ownership of and responsibility for the model. It was their model, not the facilitator's or the project manager's. They invested a good deal of energy in defining the model and ensuring its accuracy, including calling their offices and colleagues in other offices to validate their information.

Second, the structured review process enabled problems with the model's semantics to be raised quickly and discussed openly. Anonymity was crucial to the raising of these issues for discussion. Since the comments made during the review were almost entirely criticisms of others' work, participants were reluctant to be seen as a continual critic. Several participants mentioned that anonymity "freed me from having a quota" of criticism, so that they could now voice all of their concerns. By disassociating criticisms from their contributor, participants were encouraged to identify all the problems they saw, rather than limiting themselves to the major issues. The anonymous nature of the criticism also seemed to lessen its sting, since the group as a whole (or the subgroup whose work was being criticized) was more likely to focus on resolving the issues raised than to engage in debate with the person who made the criticism.

Finally, the GSS use enabled more experts to participate. All projects (GSS and traditional) were intercommand projects—that is, they were designed to improve processes and/or development information systems that would be put in place at many different installations (i.e., bases) in several different commands (e.g., commands responsible for executing military operations, such as the war in the Gulf [e.g., SOUTHCOM], as well as commands responsible for training [e.g., TRADOC]). While many of the processes under study were very similar between commands (because they were guided by the same regulations), there were important differences in all projects between commands. It was necessary to involve representatives from each of the affected commands to ensure that the new processes and systems adequately met the needs of each command. It was also politically expedient to ensure that each command had a representative contributing to the project who could act as an advocate for the project when he or she returned to his or her unit.

On average, eight experts participated in the traditional projects, compared with twenty-five in the GSS projects. For two of the GSS projects, more than sixty experts participated together in the modeling process, which, according to the project managers, would have been virtually impossible using traditional JAD techniques. The GSS projects therefore had a broader base of experts from which to draw knowledge, and this broader range of knowledge likely resulted in a more complete and accurate model. This ability to include more participants was an important advantage mentioned by all project leaders.

## Problems and Challenges

We encountered several problems with this GSS-based approach, some of which we believe can be overcome in future work, some of which we believe are fundamental to GSS-based approaches and will need to be continuously managed. We first address three problems we believe can be overcome. One difficulty encountered was that of identifying syntax errors in the model. The software we used had no syntax-checking capability, so all errors had to be identified manually by the facilitator(s) and participants. Since completion of this study, several GSS modeling tools have become commercially available, all of which provide some syntactic error checking capability. A second problem was response time. Most of the projects were conducted using 386- and 486-based computers running on 4-megabit local area networks, so response time can clearly be enhanced by moving to faster hardware and networks. Finally, integration between our IDEF0 tool and GroupSystems and VissionQuest was via a rather clumsy cut-and-paste process. Since very little information actually needed to be shared (mostly process names), this was not a major problem. However, a simpler data-exchange process would have made transfer smoother.

Three issues are more fundamental. The first is user training. While training of the subject-matter experts is important in the traditional approach, it is critical in GSS-based approaches. Without adequate training, participants can quickly define a poor-quality model. Activities or ICOMs can be ill defined; different ICOMs may have similar names or the same ICOMs may appear with different names in different parts of the model. Even with adequate training, the model can quickly become hopelessly complex if participants attempt to define too many levels of activities or adopt a poor structure to the model (see Coupling and Cohesion in [1]). It is critical that the facilitator closely monitor the development of the model to quickly identify and correct flaws in participants' understanding of the modeling language. It can be useful to draw on the knowledge of those participants with previous modeling experience and encourage them to assist in monitoring quality. We also recommend that participants pause regularly to discuss questions and review syntax errors.

The second issue is consistency and integration. With this GSS process, different parts of the model are developed simultaneously by different participants. Ensuring that the terminology and fundamental concepts are consistent, and that the various parts of the model integrate smoothly into one seamless whole, can be challenging. Different experts potentially have different semantic understandings of the process, different terminology, and different writing styles, all of which need to be integrated.

This can be successfully managed, but it requires more vigilance from facilitators and participants than do traditional techniques in which only the facilitator has access to the model. An early pause in the modeling process to review progress can help ensure a common semantic understanding that will produce a more easily integrated model.

A final fundamental concern is information overload. The volume of information produced in both GSS and traditional models was large, ranging from one hundred pages for small models to fifteen hundred pages for the largest model; three hundred to four hundred pages was more typical. It was extremely difficult for all participants to process this volume of information actively in the time available (typically one to two weeks). There was a tendency for participants to focus on “their” part of the model, leaving others to worry about the rest. This lack of a “global” view has the potential to reduce model quality significantly. Facilitators need to promote the active involvement of all participants, but there are clearly limits to individuals’ cognitive abilities.

## Implications and Conclusions

## Implications for Managers

While we do not presume to have completely addressed the limitations of this study, we can draw some tentative conclusions for managers. In this study, the use of GSS-based processes and tools significantly decreased the time required to build business process models. GSS models were typically built in one week, as opposed to six weeks for traditional models. The cost differences were substantial. The largest GSS project (375 activities) cost about \$300,000. The largest traditional project (385 activities) cost about \$3 million. One of the debates within the reengineering community is the cost/benefit of modeling. Given a cost of \$3 million and one year to complete, it is easy to see why some advocate little or no modeling. In contrast, we believe that the benefits from modeling clearly outweigh the costs when GSS is used.

An interesting side effect of this reduction in time is the quality of the subject-matter experts who may be assigned to the project. Several project managers mentioned the difficulty in obtaining experts with sufficient knowledge for the six weeks required by traditional approaches. In some cases, the experts assigned to do the modeling did not have sufficient expertise, because those with the expertise could not be spared for six weeks. The implication is, if one can do process modeling faster (say, in one week not six), one may be able to gain access more easily to the most experienced experts, and produce a better quality model.

The project managers in this study intentionally increased the size of the groups when using the GSS approach. This was done for both practical and political reasons. Many of the models were truly large in scope, involving elements from different services. These projects required many experts because the range of knowledge required for the models spanned many different functions and services. By including sixty or more participants, project managers hoped to reduce the amount of time spent revising and correcting the model once it was circulated for comments and approval beyond the team that built it. It was also politically expedient to increase the size of the team in hopes of ensuring that each command had a representative contributing to the project who could act as an advocate when he or she returned to his or her command. The implication is that increasing the size of the modeling team may improve quality and help during the approval process.

## Implications for Future Research

We are encouraged by the magnitude of the productivity differences between the two approaches. These differences have several messages for researchers. First and foremost, we believe it suggests a new direction for process modeling research. While we still need to develop and refine the languages used to specify models, more research effort needs to be given to the processes by which models are built. Given the rather scant research attention that has been focused on the process of modeling, we are confident that by devoting more research to the process and by identifying other process improvements, we can find significant new ways to improve the productivity and quality of modeling.

Second, this research examined only one process modeling language (IDEF0). More research is needed to determine how well the concepts presented here can apply to other languages and approaches. While we believe that other modeling approaches (e.g., object-oriented) can benefit from GSS support, the effects of doing so remain an empirical question.

Third, we need to assess the relative importance of the elements in transforming the traditional process to a GSS process. We believe that simply parallelizing the process, so that several subgroups work simultaneously on different parts of the model, was a major element in the increased productivity, while the formal and informal model reviews in the process improved quality. The parallelism inherent in the GSS software itself also increased the productivity of the entry of the experts' information into the model, and of the model reviews. The anonymity provided by the GSS during the model reviews was a key element in improving semantic quality. However, without the special-purpose GSS IDEF0 software that provided a shared group memory into which all information was placed (with a very fine granularity of locking), and that was organized in the IDEF0 language format, such a parallelized process and parallelized software would likely have led to significant integration problems.

Since this was an initial study, we did not attempt to measure which of these components (parallelized process, model reviews, or the parallelism, anonymity, and group memory of the GSS software) was the “most important” factor. We suspect that the relationships among them are multiplicative, not additive, so that employing any one factor without the others will have far less effect. Nonetheless, this suggests some interesting opportunities for future research. It would be possible to decompose the GSS-based process to identify which GSS aspects appear to have the greatest effects on productivity and quality. For example, one could conduct a laboratory experiment to test a parallelized GSS-based process to a parallelized manual process to a sequential manual process to see which produces the best models in the least about of time. Likewise, the value of anonymity and parallelism to model review could be examined through a series of experiments contrasting traditional manual model review to anonymous and nonanonymous GSS-based review processes to see which is best and fastest at uncovering syntax and semantic errors.

We cannot offer any conclusive evidence about the relative merits of the different components of the GSS-based process, but we can speculate on the basis of our experiences. We interviewed a project manager who had conducted one project using a parallelized process similar to the one used in this study, but without any supporting GSS. Each of the subgroups worked in separate rooms, with a single-workstation, nonnetworked IDEF0 tool. Participants spent the first half of each day working in four subgroups to define the model elements, and the second half of each day working together as one large group to integrate the work of the subgroups. In the evening, the modelers spent several hours physically transferring the information among the computers used by each of the subgroups.

This project averaged just over six activities modeled per day, which is about twice the productivity of the nonparallelized traditional approach, and one-quarter the productivity of the GSS approach. However, the manager reported difficulties in integrating the work of the subgroups to ensure consistency in terminology, structure, and especially the connection of ICOMs from activities in one subgroup to those in another. The “simple” physical transfer of data among the subgroups also proved time-consuming and bothersome. The modeling team worked an additional half-day each evening to integrate the models (this time was not counted in the productivity calculations).

Thus, simply parallelizing the process without GSS tools (into four parallel sessions for half of the day, with the other half of the day for review and integration—and the evenings for technical integration) doubled productivity. This suggests that parallelizing the process brings improvements in about the same ratio of the number of parallel sessions (i.e., four subgroups working in parallel should improve productivity by a factor of four). However, the parallel nature of the work could not be sustained for the entire day, because the subgroups need to meet to review and integrate their models. These integration and review sessions lasted a half-day for the manual groups, the same time it took to develop the models in the first place, producing a one-to-one ratio between development and integration. In our GSS process, the time for model review was significantly reduced, producing something closer to a four-to-one ratio between time in development versus integration. This time reduction was accomplished by using the GSS tools in GroupSystems and VisionQuest for the review sessions, and by enabling the experts to see each others' emerging models in the GSS IDEF0 tool and enabling them to be proactive in resolving integration problems early, rather than waiting for a formal review. The IDEF0 tool also automatically integrated the models, so, unlike in the manual sessions, the technical integration of the model (i.e., copying disks) was avoided, thus improving the technical teams' productivity (although these values are not included in our productivity measures).

So, we conclude that about half the productivity benefits arose from the parallelized process and about half from the use of the GSS tools. However, as noted from the experiences of the manual groups using the parallelized process, manual groups were unable to sustain the parallelized process for the entire project without GSS tools, and thus they only attained about half the possible improvement from a parallelized process.

Finally, this research was conducted in meeting rooms using a same-time, same-place form of GSS. The Internet and the Web have created many new opportunities for group work. It is now possible to include participants from many remote locations, so that, in theory, the size of the subject-matter expert group can become quite large, including participants from anywhere in the world. Indeed, it would be possible to conduct the entire modeling session over the Web without the need to meet in person. However, we are skeptical. One of the challenges in process modeling—and in GSS-based process modeling in particular—is ensuring the consistent integration of the model elements from different subject-matter experts. Verbal discussion was very important in resolving the differences of opinions among the experts and also helped ensure that all participants shared a common understanding of the process and the IDEF0 methodology.

Nonetheless, it may be possible to use the Internet selectively to involve a wider set of subject-matter experts at specific points in the process. We believe that using the Internet to bring in outside experts to assist in the review of the model for errors and omissions holds considerable promise (see $[39, 46]$ ). This has the potential to involve outside experts (and those who must ultimately approve the model) earlier in the modeling process to ensure that the subject-matter experts can benefit from a much broader range of opinions that, we hope, will better enable the earlier identification of problems.

In any event, we believe that this study has two messages for business process modeling: First, we recommend that managers begin to use GSS-based techniques for process modeling. Second, we encourage researchers to develop new techniques and software to support other approaches beyond the IDEF0 approach used in this study to determine the extent to which GSS-based techniques can be applied to other process modeling languages.

Acknowledgments: The authors thank Wesley Brown, Col. Wayne Byrd (ret.), Brice Marsh, Lawrence Massman, and Jim Gantt for their support and assistance in conducting this research. They also thank John Satzinger, Dale Goodhue, and the anonymous reviewers for helpful comments on earlier versions.

## REFERENCES

1. AFWAL-TR-81-4023. IDEF0 Function Modeling. Wright Aeronautical Laboratory, U.S. Air Force, 1981.

2. Bostrom, R.P. Successful application of communication techniques to improve the systems development process. Information and Management, 16 (1989), 279–295.

3. Byrd, T.A.; Cossick, K.L.; and Zmud, R.W. A synthesis of research on requirements analysis and knowledge acquisition techniques. MIS Quarterly, 16 (1992), 117–138.

4. Carmel, E.; George, J.F.; and Nunamaker, J.F. Supporting joint application development

(JAD) with electronic meeting systems. Proceedings of the Thirteenth International Conference on Information Systems, Dallas, 1992, pp. 223–232.

5. Carmel, E.; Whitaker, R.D.; and George, J.F. PD and joint application design: a transatlantic comparison. Communications of the ACM, 36, 4 (April 1993), 40–48.

6. Connolly, T.; Jessup, L.M.; and Valacich, J.S. Effects of anonymity and evaluative tone on idea generation in computer-mediated groups. Management Science, 36, 6 (June 1990), 689–703.

7. Cosby, B.A. Planning for success: the importance of JAD pre-work. In Proceedings of GUIDE61. Anaheim, Calif., March 1985, pp. 7–8.

8. Curtis, B.; Kellner, M.I.; and Over, J. Process modeling. Communications of the ACM, 35, 9 (September 1992), 75–90.

9. Daft, R.L., and Lengel, R.H. Organizational information requirements, media richness and structural design. Management Science, 32 (1986), 554-571.

10. Daft, R.; Lengel, R.; and Trevino, L. Message equivocality, media selection, and manager performance. MIS Quarterly, 11 (1987) 355–366.

11. Davenport, T., and Short, J.E. The new industrial engineering: information technology and business process redesign. Sloan Management Review (Summer 1990), 11–27.

12. Davis, G.B., and Olson, M.H. Management Information Systems: Conceptual Foundations, Structure, and Development, 2d ed. New York: McGraw-Hill, 1985.

13. Dean, D.L.; Lee, J.D.; Orwig, R.E.; and Vogel, D.R. Technological support for group process modeling. Journal of Management Information Systems, 11, 3 (1994), 43–63.

14. Dean, D.L.; Lee, J.D.; Pendergast, M.O.; Hickey, A.M.; and Nunamaker, J.F. Enabling the effective involvement of multiple users: methods and tools for collaborative software engineering. Journal of Management Information Systems, 14, 3 (1998), 179–222.

15. Dennis, A.R.; Daniels, R.M.; Hayes, G.S.; and Nunamaker, J.F., Jr. Methodology-driven use of automated support in business process reengineering. Journal of Management Information Systems, 10, 3 (1993), 117–138.

16. Dennis, A.R.; George, J.F.; Jessup, L.M.; Nunamaker, J.F., Jr.; and Vogel, D.R. Information technology to support electronic meetings. MIS Quarterly, 12, 4 (1988), 591–624.

17. Dennis, A.R.; Haley, B.J.; and Vandenberg, R.J. A meta-analysis of effectiveness, efficiency, and participant satisfaction in group support systems research. Proceedings of the Seventeenth International Conference on Information Systems, Cleveland, 1996, pp. 851–853.

18. DeSanctis, G., and B. Gallupe. A foundation for the study of group decision support systems. Management Science, 33 (1987), 589–609.

19. Diehl, M., and Stroebe W. Productivity loss in brainstorming groups: toward the solution of a riddle. Journal of Personality and Social Psychology, 53 (1987), 497–509.

20. DoD 8020.1-M. Functional Process Improvement. U.S. Department of Defense. 1992.

21. FIPS 183. Integration definition for function modeling (IDEF0). Federal Information Processing Standards Publications, U.S. Department of Commerce, 1993.

22. Franz, C.R., and Robey, D. An investigation of user-led system design: rational and political perspectives. Communications of the ACM, 27 (1984), 1202–1217.

23. Gallupe, R.B.; Dennis, A.R.; Cooper, W.H.; Valacich, J.S.; Nunamaker, J.F., Jr.; and Bastianutti, L. Electronic brainstorming and group size. Academy of Management Journal, 35 (1992), 350–369.

24. Gill, A. Setting up your own group design session. Datamation (November 15, 1987), 88–92.

25. Godfrey, L.E. Joint application design—a timesaver. Resource (March 1986), 28+.

26. Hackman, J.R., and Kaplan, R.E. Interventions into group process: an approach to improving the effectiveness of groups. Decision Sciences, 5, 3 (1974), 459–480.

27. Hammer, M., and Champy, J. Reengineering the Corporation. New York: Harper, 1993.

28. Hill, G.W. Group versus individual performance: are n+1 heads better than one? Psychological Bulletin, 91 (1982) 517–539.

29. Hoffer, J.A.; George, J.F.; and Valacich, J.S. Modern Systems Analysis and Design. Reading, MA: Benjamin/Cummings, 1996.

30. Holzblatt, K., and Beyer, H.R. Requirements gathering: the human factor. Communications of the ACM, 38, 5 (May 1995), 30–32.

31. Jablin, F.M., and Seibold, D.R. Implications for problem solving groups of empirical

research on “brainstorming”: a critical review of the literature. The Southern States Speech Communication Journal, 43 (1978), 327–356.

32. Jessup L.M., and Valacich J.S., eds. Group Support Systems: New Perspectives. New York: Macmillan, 1993.

33. Keil, M., and Carmel, E. Customer developer links in software development. Communications of the ACM, 38, 5 (May 1995), 33–44.

34. Lamm, H., and Trommsdorff, G. Group versus individual performance on tasks requiring ideational proficiency (brainstorming): a review. European Journal of Social Psychology (1973) 361–387.

35. Liou, Y.I., and Chen, M. Using group support systems and joint application development for requirements specification. Journal of Management Information Systems, 10, 3 (1993), 25–41.

36. Martin, J. Rapid Application Development. New York: Macmillan, 1991.

37. Monarchi, D.E., and Puhr, G.I. A research typology for object-oriented analysis and design. Communications of the ACM, 35, 9 (September 1992), 35–47.

38. Nunamaker, J.F., Jr.; Dennis, A.R.; Valacich, J.S.; Vogel, D.R.; and George, J.F. Electronic meeting systems to support group work. Communications of the ACM, 34, 7 (July 1991), 40–61.

39. Pendergast, M.O.; Dean, D.L.; Lee, J.D.; Nevstrujev, B.; and Katic, N. Current advances in group supported business process reengineering. In Proceedings of the Twenty-ninth Annual Hawaii International Conference on System Sciences, vol. 3, 1996, pp. 451–460.

40. Player, R.C. Engineering high quality, value-added IDEF0 models. Proceedings of the IDEF Users Group, Richmond, VA, 1994, pp. 33–47.

41. Rice, R. Task analyzability, use of new media, and effectiveness: a multi-site exploration of media richness. Organization Science, 3 (1992), 475–500.

42. Ross, D.T. Structured analysis (SA): a language for communicating ideas. IEEE Transactions on Software Engineering, SE-3, 1 (1977), 16–34.

43. Rush, G. A FAST way to define system requirements. Computerworld (October 7, 1985), 11–12.

44. Shaw, M. Group Dynamics: The Psychology of Small Group Behavior, 3d ed. New York: McGraw-Hill, 1981.

45. Valacich, J.S.; Dennis, A.R.; and Connolly, T. Group versus individual brainstorming: a new ending to an old story. Organizational Behavior and Human Decision Processes, 57 (1994), 448–467.

46. Van Genuchten, M.; Cornelissen, W.; and van Dijk, C. Supporting inspections with an electronic meeting system. Journal of Management Information Systems, 14, 3 (1998), 165–178.

47. Whitten, J.L., and Bentley, L.D. Systems Analysis and Design Methods, 4th ed. Boston: Irwin/McGraw-Hill, 1998.

48. Winograd, T. From programming environments to environments for designing. Communications of the ACM, 38, 6 (June 1995), 65–74.

49. Wood, J., and Silver D. Joint Application Design. New York: John Wiley and Sons. 1989.

50. Yadav, S.; Bravocco, R.R.; Chatfield, A.T.; and Rajkumar, T.M. Comparison of analysis techniques for information requirements determination. Communications of the ACM, 31 (1988), 1090–1097.

51. Yin, R.K. Case Study Research: Design and Methods, rev. ed. Newbury Park, CA: Sage, 1989.

52. Yourdon, E. Modern Structured Analysis. Englewood Cliffs, NJ: Yourdon Press, 1989.
