---
otero_id: 22102
otero_key: "T4ZGX45C"
title: "Improving information requirements determination: a cognitive perspective"
authors: "Glenn J. Browne; V. Ramesh"
year: "2002"
journal: "Information & Management"
doi: "10.1016/s0378-7206(02)00014-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving information requirements determination: a cognitive perspective

Glenn J. Browne $^{a,*}$ , V. Ramesh $^{b}$

$^{a}$ Information Systems and Quantitative Sciences, Rawls College of Business Administration,

Texas Tech University, Lubbock, TX 79423, USA

$^{b}$ Kelley School of Business, Indiana University, Bloomington, IN 47403, USA

Received 15 May 2000; received in revised form 8 April 2001; accepted 23 January 2002

## Abstract

Requirements determination is a critical phase of information systems development, but much evidence suggests that the process can and should be improved. Because the bulk of requirements determination occurs early in the development of a system, improvements can yield significant benefits for the entire systems development process. This paper first discusses a three-stage descriptive model of the requirements determination process. Four classes of difficulties in determining systems requirements are then used to organize and describe particular problems that occur within each stage of the process, together with the cognitive and behavioral theories that underlie them. The paper then describes techniques that can address the problems and presents theoretical considerations that analysts can use in applying the techniques to improve requirements determination. © 2002 Elsevier Science B.V. All rights reserved.

Keywords: Requirements determination; Information systems development; Knowledge elicitation; Representation techniques; Cognitive limitations

## 1. Introduction

It has been argued often and convincingly that information requirements determination (IRD) is the most critical phase of information system development. IRD is a set of activities used by a systems analyst when assessing the functionality required in a proposed system. Types of information gathered include goals for the system, business processes, data needs, design constraints, and behaviors of users $[21,26,100]$ . Such information is commonly sought from the eventual users of the system through interviews, surveys, or observation, or may be derived by studying the systems currently being used in the organization [28]. This assessment of user needs is one of the key determinants of the ultimate success of an information system. However, because understanding human and organizational needs is difficult and complex, requirements determination is, in general, ad hoc [96] and poorly understood [85,92]. Further, the large number of completed systems that do not meet user specifications and expectations suggests that the determination of such requirements can be improved [31,83,91]. Because formal requirements determination occurs early in the systems development lifecycle, improvements are likely to influence the overall quality of systems development efforts significantly and, therefore, have the potential to reduce development costs dramatically [9].

This paper seeks to improve requirements determination efforts by identifying cognitive and behavioral underpinnings of IRD problems and presenting techniques that can be used to overcome them. In particular, the paper discusses a three-phase descriptive model of the requirements determination process, identifies problems that occur in each of these phases, and then presents solutions to these problems. Although some of these issues have been discussed in prior research (e.g., [82,90]), no prior conceptualization has explicitly tied the problems and their cognitive and behavioral underpinnings directly to techniques for improvement.

## 2. A descriptive model of information requirements determination

All systems development projects of any size and importance rely on a methodology that specifies the stages that project team members should follow in completing the system. Many variations exist, but all share the essential phases of analysis of the business problem or process, and design and implementation of an IS. All methodologies require that analysts gather information about system requirements from various stakeholders, especially those people who will use the system once it is implemented. Although requirements determination occurs throughout much of the process, we are concerned here with IRD during the analysis phase, during which most of a system's required functionality is specified. Such specifications need to be made whether a company seeks to automate an existing system or is attempting to support new business processes that do not yet exist in the company [89].

The requirements determination process during the analysis phase can be divided into three stages, as shown in Fig. 1: information gathering, representation, and verification [51,92]. In the information gathering stage, the analyst uses his or her prior experience and knowledge to gather information about the functional, non-functional, and technical requirements for the proposed system. This may be accomplished in several ways, e.g., by asking and/or observing how people perform tasks that will be supported by the new system, by examining business documents and forms, and by the analyst's use of inference and imagination to envision user needs. The outputs of this stage vary, but generally take the form of notes, outlines, checklists, and informal diagrams prepared by the analyst (see, e.g., [73]). This information is used as input to the second stage, in which different representational techniques may be used to document the elicited requirements. The outputs of this stage may include informal diagrams, semi-formal diagrams (e.g., data-flow diagrams), and prototypes. These representations are then typically used to help verify that the requirements elicited are in fact correct. Users then sign a requirements document, and the diagrams representing the requirements are given to a systems designer.

![](/api/attachments/T4ZGX45C/fulltext/images/0ad75be553decc1a2f8045e937d7651f9b15d94c7137c06dbc5bb6d43a206fed.jpg)  
Fig. 1. Requirements determination process model.

Throughout the stages of IRD, feedback loops are included to signify the iterative nature of the process. At each stage, the analyst assesses the quality and completeness of the outputs, and, if necessary, repeats activities within or between stages of the process. When the analyst is satisfied with the requirements, he or she terminates the IRD process.

## 3. Problems in requirements determination

Despite the efforts of analysts and other parties involved in systems development, failures of requirements determination represent one of the leading causes of system failure $[66]$ . Davis $[28]$ lists four sources of difficulties. In essence, these are: (1) constraints on humans as information processors; (2) the variety and complexity of information requirements; (3) communication issues between analysts and users; and (4) the unwillingness of users to provide requirements. These difficulties are shown in Table 1, together with specific problematic behaviors drawn from studies in cognitive and social psychology. These difficulties are basic to human problem-solving, and are independent of the systems development methodology being used. Fig. 2 presents the stages of the IRD process in which the problems are most likely to occur.

Table 1  
Difficulties in requirements determination

<table><tr><td>Classes of difficulties</td></tr><tr><td>Constraints on humans as information processors</td></tr><tr><td>Cognitive biases</td></tr><tr><td>Satisficing</td></tr><tr><td>Faulty reasoning</td></tr><tr><td>Automaticity</td></tr><tr><td>Problems in recall</td></tr><tr><td>Variety and complexity of requirements</td></tr><tr><td>Communication problems</td></tr><tr><td>Unwillingness of users to provide requirements</td></tr><tr><td>Motivational biases</td></tr><tr><td>Hawthorne effect</td></tr></table>

## 3.1. Constraints on humans as information processors

Many problems in IRD can be traced to human cognitive constraints. Cognition is limited as a result both of the architecture of the brain and of the adaptation by humans to their environment. Central to all cognitive constraints are the limitations on working

## Information Gathering

Cognitive Biases
Satisficing
Faulty Reasoning
Automaticity
Problems in Recall
Variety and Complexity of Requirements
Communication Problems
Motivational Biases
Hawthorne Effect

## Representation

Cognitive Biases
Satisficing
Faulty Reasoning
Problems in Recall
Variety and Complexity of Requirements

Verification
Cognitive Biases
Satisficing
Communication Problems

Fig. 2. Difficulties in stages of the requirements determination process.

memory, which has limited capacity and generally processes information serially rather than in parallel [72]. Other important constraints operate through long-term memory.

## 3.1.1. Cognitive biases in judgment

A major difficulty in systems development generally and requirements determination in particular is cognitive bias, which arises because of the short-cuts, or “heuristics,” that people use to solve problems and perform tasks. Because they are short-cuts, heuristics nearly always result in biased performance $[88]$ . This can have a serious impact on systems development because biases often lead to seriously flawed decision making. Tversky and Kahneman $[88]$ identified several general judgmental heuristics that are applied in a wide variety of tasks. These heuristics and associated biases are summarized in Table 2.

Cognitive biases seem to be associated with nearly all human decision making and problem-solving under conditions of uncertainty $[40,88]$ . Hence, we hypothesize that cognitive biases exist in all three-stages of the IRD process. During information gathering, cognitive biases such as the ease of recall bias and overconfidence are likely to affect the responses users give to analysts' questions about system needs; e.g., overconfidence about his or her understanding of a user's needs is likely to cause an analyst to stop information gathering prematurely, resulting in underspecified system requirements. During representation, analysts are likely to be affected by insufficient anchor adjustment. For example, after an initial representation (such as a prototype) is constructed, an analyst who encounters conflicting information is likely to attempt to adjust the initial representation rather than construct an entirely new representation. If the initial representation was seriously flawed, the resulting adjustment is likely to be insufficient to capture conflicting information appropriately. Finally, during verification, overconfidence is likely to be a problem because analysts are likely to remain overly optimistic about their understanding of user needs. Further, if users suggest problems with an analyst's understanding, the analyst is likely to anchor on his or her present understanding and adjust (often insufficiently) rather than re-thinking and questioning initial premises.

## 3.1.2. Satisficing

The limits on human information processing and the heuristic nature of problem-solving can lead to a second type of cognitive problem: satisficing. Simon [78] used this term to describe the tendency of people to use heuristics and seek satisfactory rather than “optimal” solutions to problems. Satisficing behavior develops as a person adapts to a particular task environment and learns the short-cuts that produce satisfactory results. However, because building information systems that are merely “satisfactory” is probably not the goal of most company executives, use of a satisficing strategy by systems analysts likely should not be encouraged. Thus, understanding satisficing behavior in systems development and reducing its effects are important. One of the purposes of systems development methodologies is to reduce satisficing by prescribing well-defined processes for the analyst.

As is the case with cognitive biases, satisficing is present in nearly all human behavior. Research has shown that people terminate the knowledge gathering process too soon in a variety of problem-solving situations (e.g., [4,65]), including the requirements determination process. For example, Pitts [67] showed that analysts eliciting requirements elicited only a small fraction of the available information before terminating the process. We hypothesize that similar effects typically occur during all of IRD. During representation, satisficing may cause analysts to represent requirements in ways that seem to reflect the desired functionality in the system without investing the time to ensure that the representations are accurate and complete. During verification, both users and analysts are likely to acquiesce to requirements that have been previously stated.

## 3.1.3. Faulty reasoning

Problems in reasoning also contribute to difficulties in requirements determination. Some problems result from deficient mental models and consequent reasoning fallacies [65]. For example, a person's mental model of an application domain is often incomplete and, thus, the inferences he or she draws based on this incomplete knowledge are likely to be inaccurate. In fact, most reasoning problems in everyday situations are due to illogical or unnecessary extensions beyond the person's mental model of the situation [65].

Table 2  
Cognitive heuristics and biases in judgment

<table><tr><td>Heuristic</td><td>Bias</td><td>Description</td><td>Example</td></tr><tr><td rowspan="2">Availability</td><td></td><td>Assessing the likelihood of an event&#x27;s occurrence by how “available” that event is in memory</td><td>When asked to name the best-selling word processing application packages in the US, most people recall them correctly. This is due to advertising that makes these products “available” in people&#x27;s memories</td></tr><tr><td>Ease of recall</td><td>Events that are vivid, emotional, particularly salient, or happened recently to a person are usually easier to recall. However, these characteristics of events do not make them more likely to occur</td><td>When an analyst attempts to elicit the frequency with which certain types of errors occur, the ease of recall bias may cause a user to report errors that occurred most recently or that irritate him the most. Such errors may not in fact occur very often, however, despite the user&#x27;s assertions to the contrary</td></tr><tr><td rowspan="3">Representativeness</td><td></td><td>Assessing the likelihood of an event&#x27;s occurrence by how representative that event is of events in its class</td><td>A manager may forecast the likelihood of success of a new information system by comparing the new system to successful systems from the past</td></tr><tr><td>Insensitivity to sample size</td><td>Not considering the size of a sample of data when assessing likelihood</td><td>If a user is basing a judgment on a small sample of information, the analyst should be concerned about that judgment because it may not be representative of the population being analyzed</td></tr><tr><td>Insensitivity to base rates</td><td>Not considering the rate of occurrence of a phenomenon in the population of interest when forecasting its likelihood of occurrence</td><td>Suppose, a base rate (i.e. average number) of errors made by programmers is known to be 10 errors per 100 lines of code. If a new programmer is hired and is reputed to be a “great programmer,” a project manager is usually more accurate if he forecasts 10 errors per 100 lines of code rather than the conflicting, but unsubstantiated, evidence that the new programmer is extraordinary</td></tr><tr><td rowspan="3">Anchoring and adjustment</td><td></td><td>Designing or forecasting based on an initial, often arbitrary, value and then adjusting from that value</td><td>In forecasting next year&#x27;s anticipated information technology budget, a company&#x27;s CIO uses this year&#x27;s budget and then adjusts from that figure</td></tr><tr><td>Insufficient anchor adjustment</td><td>Using an initial anchor and then being too conservative in adjusting from it</td><td>An analyst designing a user interface relies on past interfaces he has designed, fails to adjust adequately to current user needs, and delivers an interface that is not functional</td></tr><tr><td>Overconfidence</td><td>A person&#x27;s confidence in an outcome is higher than external circumstances warrant</td><td>Analysts often believe they understand what users need too soon, and consequently spend too little time collecting requirements. Similarly, project managers are often overconfident in their time and resource estimates for projects, causing system development failures</td></tr></table>

Derived from [5,40,86-88].

A second type of reasoning problem occurs when inadequate arguments are made to support claims made by users [25]. $^{1}$ Although a variety of types of arguments can be made in forming beliefs or asserting viewpoints (e.g., arguments from sign, authority, similarity, analogy; see [25]), people rely strongly on causal arguments to form beliefs [77]. In complex situations, such reliance may be inappropriate. Furthermore, people often do not form enough arguments in support of their beliefs, resulting in beliefs that are shallow and flawed [65].

Understanding the problems due to faulty reasoning is potentially important in both the information gathering and representation stages of requirements determination. During information gathering, users are likely to make illogical inferences, particularly when they do not have enough information about a particular event or phenomenon, and are also unlikely to generate adequate arguments to support their beliefs. The same sorts of difficulties are likely to affect analysts during the representation stage: analysts may make unwarranted inferences in representing the information for the desired system.

## 3.1.4. Automaticity

Another characteristic of human cognition is automaticity. Nearly, all human task performance involves a combination of controlled (conscious) and automatic processing. With controlled processing, a person consciously deliberates actions in working memory. With automatic processing, a person performs actions without consciously thinking about them. As tasks are performed more often and become routine, many of the behaviors cease to involve controlled processing and begin to be performed automatically; at this point, a person loses conscious access to the behaviors in working memory $[79]$ . Therefore, someone asked about the steps he or she is taking to perform a routine task will have significant difficulty describing those steps because they are no longer considered consciously. Tasks ranging from tying a necktie to filling out routine forms to driving automobiles generally involve automated behaviors.

Automaticity is a particularly serious problem in determining information requirements, because task performance behavior of users quickly becomes automatic [53]. Thus, this problem is most likely to occur during the information gathering stage.

## 3.1.5. Problems in recall

Another significant difficulty encountered in requirements determination relates to the nature of recall from long-term memory. In storing information in long-term memory, people typically store only the “gist” of the information, not the details $[12]$ . When asked to recall an event, people may remember the gist, but must “fill in” the details of the event because those details were not stored $[2,74]$ . This can lead to problems because people may fill in details that did not actually occur, and because different people fill in different details. Also, people do not remember many elements of information, either because it was not stored carefully or because the analyst has not stimulated the proper memory trace.

Problems in recall are likely to affect both analysts and users in the information gathering and representation stages. During information gathering, systems analysts need to be aware that much information evoked by a user will simply be inaccurate, either due to faulty inferences about what “must have occurred” or outright fabrication resulting from social pressures. A second problem is that errors in recall are particularly common for routine events: memories are best for unusual events and are worst for one routine occurrence within a set of occurrences $[14]$ . Since analysts are interested in modeling what typically occurs in user task performance (i.e. routine events), it is likely that memory errors will interfere with accurate recollections of these events. A third problem is that an event as recalled is typically told as a coherent story, even though the original event may have been far from coherent. This may mislead the analyst into believing that there is less complexity in the environment than is the case.

During the representation stage, analysts can be similarly affected by recall problems. In particular, most analysts capture only the gist of the information elicited from users during the information gathering stage, and hence, must “fill in the gaps” later. Further, analysts also must reduce complexity in the environment when representing information, both to make the representations more logical and to reduce cognitive demands in understanding the diagrams. However, if a representation simplifies an environment too much, the result will be a system that does not capture enough functionality.

## 3.2. Variety and complexity of user requirements

Requirements elicited will often have high variability because of the varying heuristics that different people use to perform tasks. Further, users' preferences are generally not stable $[40]$ ; eliciting requirements from the same user at different times is likely to yield somewhat different needs. Thus, there is variation both between and within users. Additionally, user requirements often (legitimately) change during the course of development, necessitating adjustments or rework. Further, users often must adjust dynamically to changing external conditions $[98]$ . Complexity for the analyst is heightened by the fact that there is no single “correct” list of requirements. Instead, a superbly functional system may be achieved from several potential sets of user requirements.

Finally, the fact that a new system is being contemplated for the business process implies a problem or opportunity, and it is likely that the implications of the problem are not fully understood. This means that system requirements are not simply waiting to be discovered, or “mined” from the heads of the users [45]. This is especially true in the context of new businesses (e.g., an e-business) in which standardized processes often have not been established. Thus, analysts often have to rely on the “emergence” of requirements during their discussions with users. $^{3}$ Creative methods for eliciting requirements are often needed [24].

Problems in IRD resulting from high variability and complexity seem likely to occur during the information gathering and representation stages (Fig. 2). In information gathering, one problem is that users often do not know what the functionality of the new system should be [1,102]. A second issue is that a new system usually requires different functionality, and future needs must be projected [57,102].

In the representation stage, one problem results from the fact that people have difficulties with holistic evaluations of complex problems. The sheer volume of information can overwhelm working memory. The general reaction to such difficulties has been the creation of structured methodologies that include standard representational techniques $[36]$ . The structured methodologies aid in decomposing problems into manageable sub-problems, making solutions easier to visualize and attain $[37,80]$ . However, there is evidence that the representations utilized in the methodologies may be inadequate for communication between analysts and users. Further, the problems with variety and complexity have been reduced, but certainly not eliminated $[19]$ .

A second difficulty in the representation stage is in categorizing and organizing data appropriately. Categorization reduces human cognitive demands $[72]$ , and so is a major solution for variety and complexity problems. Heterogeneity and complexity require that discriminations be made between stated user needs, followed by categorization of the information in meaningful and useful ways $[26,84]$ .

There are potential difficulties in categorizing information, however, such as inappropriate perceptions of variability. In discriminating among requirements, analysts may perceive variability when there is none or perceive no variability when variation is in fact present $[16]$ . This can lead to meaningless features in an IS because an analyst believed that a distinct feature was necessary to perform a task, or to meaningful features being omitted because an analyst failed to capture an important distinction. Thus, there is a need for techniques that both reduce requirements complexity and aid analysts in organizing elicited information.

## 3.3. Communication issues

Problems in communication lead to difficulties in the information gathering and verification stages of the requirements determination process. These can occur in a one-on-one session with a user or in a joint application development (JAD) setting with one or more analysts and several users $[11,41]$ .

The principal communication difficulties arise from the differing backgrounds of the two types of people involved. Analysts have typically been trained in information systems and allied fields. Users may have formal training in a substantive domain, such as marketing or finance, or only in a specific area of operations, such as customer service. In any case, the differing training and backgrounds generally mean that analysts and users speak different “languages” [11,63,94]. This can lead to difficulties in interpreting terms and acronyms and to problems in understanding people’s mental models. For example, there is evidence that experts and novices use different basic-level categories in describing the same phenomenon [23]. Thus, in determining requirements for a decision support system to support a marketing function, for instance, a systems analyst (the novice) may aggregate many user behaviors into a category named “decisions.” However, the user (the expert) may regard particular behaviors as “judgments,” “reasoning,” and “choices.” Such differences can lead to mistakes in modeling and ultimately to problems in system functionality (see also [75]).

Another difficulty results from the differing goals of analysts and users. Users' mental models are driven by domain-specific objectives, while analysts' models are often driven by systems concepts. For example, users may focus on achieving maximum functionality and flexibility, while analysts focus on efficiency and ease-of-maintenance.

## 3.4. Unwillingness of users to provide requirements

User cooperation is obviously important to assessing requirements. Lack of cooperation can be intentional or unintentional.

## 3.4.1. Motivational biases

Users may be intentionally unwilling to provide requirements as a result of company politics or organizational incentive systems $[7,48,81]$ . Such problems affect primarily the information gathering stage. Incentives motivate users to bias their responses to analysts' questions for such reasons as personal political or financial gain, self-protection, self-preservation, or because their responses will be evaluated by others.

Further, politics (and related group norms) can have a chilling effect on a user's evocation of information for fear of offending someone or of harming a political position. In the extreme, political considerations can lead to self-censorship and a “getting along”

mentality that results in poor information search, an incomplete listing of alternatives, an illusion of unanimity, and other symptoms of “groupthink” [44].

## 3.4.2. Hawthorne effect

A problem with all observations of behavior is the well-known Hawthorne effect. People who know they are being watched will often act differently than they do when unobserved. In particular, people will do what they think they are supposed to do, reflecting idealized rather than typical behavior $[64]$ . Such behavior, however, amounts to an unconscious lack of cooperation by users. The Hawthorne effect is important for systems analysts, because understanding users' typical task performance (reflecting users' heuristics and procedural knowledge) is generally the goal of requirements gathering.

## 4. Techniques for improved requirements determination

## 4.1. Techniques to address cognitive problems

The techniques identified in this section can be termed “informal” $[27,29,34,35]$ , distinguishing them from semi-formal models, such as entity-relationship diagrams (ERDs) and data-flow diagrams (DFDs). It should be noted that these techniques are meant to be illustrative rather than exhaustive. A number of other tools have been proposed in previous research, including conceptual graph structures $[38]$ , event and value trees $[93]$ , cause maps $[54]$ , teachback interviewing $[47]$ , prototyping $[66,71]$ , and object system models $[56]$ (see also, e.g., $[58,99]$ for reviews of other elicitation and representation tools).

The techniques may be divided into three general categories: pre-elicitation conditioning, prompting techniques, and external representational techniques. Table 3 presents a summary of the primary functions of these techniques, the cognitive/behavioral problems they address, and the stages of IRD during which they should be applied.

## 4.2. Use of recommended techniques in IRD

This section is divided into four sub-sections. Each contains suggestions for how various types of techniques can be used in the IRD process.

Table 3  
Informal techniques: functions and problems addressed

<table><tr><td>Technique</td><td>Functions</td><td>Problems addressed</td><td>IRD phases</td></tr><tr><td>Pre-elicitation conditioning</td><td>Permits explanation of key terms, and allows analyst to create and/or influence incentive scheme for decision maker [7,81]. Also allows analyst to determine need for specific types of questions (e.g., counter-arguments) to reveal inconsistencies in decision maker&#x27;s answers, potentially reducing cognitive and motivational biases [7]</td><td>Motivational biases, Hawthorne effect, and most other problems</td><td>Information gathering</td></tr><tr><td>Directed questions</td><td>Stimulate user&#x27;s memory, causing associations to be made and causing user to think of things he otherwise may not [6,18]</td><td>Cognitive biases, satisficing, faulty reasoning</td><td>Information gathering</td></tr><tr><td>What-if analysis</td><td>Stimulates user&#x27;s imagination, resulting in solutions otherwise not thought of; can cause associations or connections to be made in memory [24]</td><td>Automaticity, variety and complexity problems</td><td>Information gathering</td></tr><tr><td>Scenario response</td><td>Causes reflection, resulting in knowledge being used rather than simply assumed [46,76]</td><td>Automaticity</td><td>Information gathering, representation</td></tr><tr><td>Devil&#x27;s advocacy</td><td>Causes users to question assumptions and generate counter-arguments, revealing knowledge that otherwise would not be evoked and improving the accuracy of reasoning and judgments [17,18,24,49,65,76]</td><td>Automaticity, recall problems, faulty reasoning</td><td>Information gathering, representation, verification</td></tr><tr><td>Flow chart</td><td>Represents event as a linear process, reducing working memory demands and allowing all parties to comment on correctness of flow [39]</td><td>Automaticity, recall problems, variety and complexity problems, communication problems</td><td>Information gathering, representation, verification</td></tr><tr><td>Evocative knowledge map</td><td>Represents knowledge and beliefs in a non-linear diagram, reducing working memory demands [18,42]</td><td>Variety and complexity problems, communication problems</td><td>Information gathering, representation, verification</td></tr><tr><td>Influence diagram</td><td>Represents influences on process steps or stages, reducing working memory demands and allowing agreement among all parties as to influences [55]</td><td>Recall problems, communication problems</td><td>Information gathering, representation, verification</td></tr><tr><td>Decision map</td><td>Captures decision maker&#x27;s mental model of a decision, task, or environment [3,43,58]. Reduces demands on working memory and allows discussion among all parties involved</td><td>Recall problems, communication problems</td><td>Information gathering, representation, verification</td></tr><tr><td>Affinity diagram</td><td>Organizes and categorizes information, beliefs, and/or arguments [13]</td><td>Variety and complexity problems, communication problems</td><td>Information gathering, representation</td></tr><tr><td>Note board</td><td>Organizes and categorizes information, beliefs, and/or arguments, with the added advantage that the individual pieces of information are portable [39]</td><td>Variety and complexity problems, communication problems</td><td>Information gathering</td></tr></table>

## 4.2.1. Pre-elicitation conditioning

Prior to eliciting requirements, the analyst and user should discuss the purposes of IRD, what the analyst will be asking the user, and what the user will need to provide. In addition to this general management of the user's expectations, analysts can anticipate and mitigate various problems that are likely to occur. Pre-elicitation conditioning has been used successfully in such domains as decision making [81].

Numerous benefits can result from engaging users in a dialogue before beginning requirements elicitation. For example, making users aware of potential biases is probably the best defense against their occurrence (although even such warnings are not particularly effective) [32]. Similarly, the analyst should point out potential reasoning fallacies to mitigate their use as well. Finally, the analyst and user should discuss terminology during this meeting to help overcome the problem of differing backgrounds and training.

The analyst should also counter possible motivational biases by explaining how the information elicited will benefit both the user and the organization as a whole. Political considerations should be minimized by stating that everyone's opinion is valued and that there will be no retribution for contributing dissenting or “non-party-line” ideas (if true). Additionally, assurances that the user's responses will be kept confidential (also only if true) and that the user's superiors and managers want the user to provide truthful answers can reduce possible motivational biases. Further, an explanation of the Hawthorne effect during pre-elicitation meetings and an assurance by the analyst that he or she is interested in actual task behavior may reduce or eliminate its effects.

## 4.2.2. Direct prompting techniques

Direct prompting techniques are used to elicit information from users in a straightforward manner. They are intended to improve the ad hoc questions used in many requirements elicitation sessions, in which analysts do not know what questions to ask and users are unclear about how to respond $[17,59]$ .

4.2.2.1. Directed questions. Directed questions attempt to elicit information through the use of schemes or checklists designed to cue information in the user's memory [6,33]. Two classes of directed questions are theoretically possible: context-independent and context-dependent [18]. Questions entirely independent of context can be used regardless of the type of system being designed. Efforts have been made to create such standardized question lists; typical are ends-means analysis, critical success factors, and business systems planning [20,97,99]. Such questions aim to elicit relevant substantive knowledge about the domain, and serve as a useful starting point for understanding system needs.

Another type of context-independent questioning scheme is based on an analysis of the requirements determination task $[17]$ . This method is designed to overcome obstacles to eliciting requirements, including cognitive biases, satisficing, and faulty reasoning. For example, Table 4 shows a set of directed questions designed to mitigate cognitive biases. The questions are independent of application context, and can be used in many IS development efforts. Browne and Rogich $[17]$ have demonstrated empirically that questions of this type help users evoke more information requirements than several other methods, including questions based on interrogatories (who, what, when, where, why, and how) $[24]$ . Further, Pitts $[67]$ has shown that directed questions designed to mitigate satisficing behavior elicit a higher quantity and quality of requirements from users.

Directed questions can be used to address faulty reasoning in users by providing argument-based questions. Such schemes attempt to elicit various kinds of arguments from users, such as analogies, similarity, or causal arguments. The use of these different argument types has been shown to lead to elicitation of more types of knowledge and more accurate knowledge $[17,18,49]$ .

A second type of directed question depends in part on the business context. For example, questions can be created that would be standardized within particular classes of tasks. Such questions are partially independent of context, because they are dependent only on a class of tasks. This possibility has been discussed in several disciplines, but not yet fully explored $[18,38,93]$ . Certain tasks recur both within and between organizations. For example, customer service representatives answering telephones is a common job function in organizations; other common jobs include machine operators, inventory controllers, and mobile workforce personnel. Many domain-specific jobs occur in large numbers as well, such as tellers and loan officers in banks. With experience, analysts may be able to create question lists that are standard for such organizational tasks. As with context-independent questioning methods, these partially context-dependent questioning schemes help address problems due to cognitive biases, satisficing, and faulty reasoning.

Table 4  
Directed questions for mitigating cognitive biases

<table><tr><td>Bias</td><td>Questions</td></tr><tr><td>Ease of recall</td><td>For each of the last four times this happened, what was the customer&#x27;s response?What is the most unusual response you have received to that question?</td></tr><tr><td>Insensitivity to sample size</td><td>How many people did you ask?Do you think if you asked other people about this problem that they would answer differently?</td></tr><tr><td>Insensitivity to base rates</td><td>Over the years, how often has this occurred?How many people does this usually affect?</td></tr><tr><td>Insufficient anchor adjustment</td><td>What is your starting point for estimating that duration? Why did you start there?What if I asked you to be 95% confident in your estimate of that duration; what interval would you give me so you were 95% confident that the correct duration would be in that range?</td></tr><tr><td>Overconfidence</td><td>What other kinds of solutions could you imagine?Play the devil&#x27;s advocate for a minute; can you think of any reasons why your solution may be wrong?Can you think of any ways in which your suggestion could be improved?</td></tr></table>

The principal advantage of questions partially dependent on context is the power of the questioning scheme. Questions driven by context have greater power than generalized ones (i.e. the answers to context-dependent questions are likely to address a problem more specifically) [60]. The chief draw back is that they are obviously not exportable to the same range of tasks as context-independent questions; therefore, sets of questions will have to be created for each specific context.

4.2.2.2. What-if analysis. With what-if analysis, the analyst prompts the user by asking him or her a question that usually begins “What if …?” The stimulus typically takes one of two forms: it is either a prompt to describe the way a certain task is performed or a prompt to respond to a hypothetical problem. What-if questions can help users imagine future tasks that will need to be performed by providing stimuli that encourage them to think about how tasks might be performed [22]. In this way, what-if questions can help the analyst overcome the limitations of automaticity by causing users to reflect on their task performance. Such analyses can also be used to help users deal with complexity. When the requirements are complex, analysts need to stimulate users to envision and describe possible future task performance imaginatively [10,102], as well as carefully think through the tasks they perform. What-if analyses can be used to accomplish both of these objectives. Several types of what-if stimuli have been shown to be useful in aiding problem-solving, including the use of mental imagery [102], making sense of current events by pretending to look back at them from a future time [10], looking forward into the future using “future analysis” [45], and simulating shifts in context, person, or information [11] (see also [68,94,101]).

## 4.2.3. Indirect prompting techniques

Indirect prompting techniques are means for eliciting knowledge that the user may have difficulty evoking, e.g., knowledge that is automated.

4.2.3.1. Scenario response tasks. Scenario response tasks require users to respond to scenarios that are designed to reveal procedural knowledge in routine task performance. The goal is to give an experienced user a task in his or her domain that will cause the conscious use of knowledge. To accomplish this, the task obviously cannot be entirely routine, since in such a case the user will rely on his or her automated knowledge, and thus there will be no description of task performance forthcoming (nor will the analyst be able to observe it). Rather, the task must be designed so that it is only partially routine. There are several ways of designing such tasks, but the common element is that the user is surprised by some aspect of the task. Surprise causes reflection $[76]$ , which reveals knowledge. One such task is termed a “garden path” task. This task is based on a language comprehension task in which ambiguity is purposefully introduced into sentences to test readers’ comprehension $[8,95]$ . A scenario (reflecting a task in the user’s domain being modeled) is constructed so that it appears to be a routine task (leading the user down the garden path), but later includes novel elements. Upon reaching the novel aspects of the task, the user will have to re-trace his or her reasoning process and change the reasoning to fit the situation (he or she cannot rely on automated processes, since the task is no longer routine). In so doing, aspects of task performance behavior should be revealed. This is one of the few techniques with empirical validation for uncovering automated procedural knowledge. Johnson et al. $[46]$ presented experienced auditors with an actual audit case containing deliberately embedded misrepresentations and “blind alleys” designed to mislead subjects. In solving the case, lines of reasoning employed by the auditors were uncovered.

4.2.3.2. Devil's advocacy. In this approach, the systems analyst constantly prompts the user to challenge assumptions, reverse the meaning of statements, and generate arguments counter to those already stated (for a similar technique, see [24]). In prompting the user to question or challenge what has already been said, the analyst causes the user to reflect on the process and reveal knowledge that the user otherwise is unlikely to evoke [76]. This is another technique that has empirical validation. Prompting people to generate counterarguments and question assumptions has been shown to increase the knowledge evoked (e.g., [17,18]) and to improve the accuracy of reasoning and judgments concerning knowledge [49,65]. The devil's advocacy technique is therefore useful for mitigating automaticity, recall, and faulty reasoning problems.

## 4.2.4. External representation techniques

External representations are models, diagrams, and charts used to display information in a physical form. Most of these representations are useful in all three stages of the IRD process. External representations are useful because they document the information that a user has evoked. Seeing the information in a physical form can help cue related information in the user's memory, leading to the evocation of further information. External representations can also address the problems of automaticity and recall of information from memory. For example, by examining a flow chart a user may recognize that he or she has inadvertently omitted steps in a process. External representations are also critical for mitigating problems of variety and complexity in requirements. Diagrams can be used to decompose complex tasks or processes and to organize and categorize information to reduce the cognitive effort of both users and analysts.

In addition to supporting the information gathering stage of IRD, external representational devices are the heart of the representation stage. Analysts have traditionally used semi-formal diagrams such as DFDs and ERDs to represent requirements. However, the need for informal diagrams results from at least five factors in IRD that are supported by prior research:

1. It is very difficult to construct semi-formal diagrams while eliciting requirements from users; in fact, analysts regularly use some sort of note-taking or other informal techniques [68]. Standardization of these techniques will increase their quality and make their use more widespread.

2. Because of the difficulty in constructing ERDs and DFDs, adequate records of verbal interactions with users may not be kept, resulting in lost information [94].

3. Users do not fully understand semi-formal diagrams [57], so the verification (user “sign-off”) of requirements documents is often unreliable.

4. ERDs and DFDs are poor devices for eliciting requirements from users [11].

5. ERDs do not support the modeling of all types of relationships in users' mental models of application environments [70].

The simplicity of these informal techniques (both in terms of the symbols used and in the ways in which information is represented) should facilitate the interaction between analysts and users, as well as help overcome background differences among them. The simplicity of the techniques should also make them more understandable. The problems in IRD that can be overcome by the various techniques are shown in Table 3.

4.2.4.1. Flow chart. One type of external representation tool is a flow chart. Flow charts are perhaps the most general and most common of the representation techniques. A flow chart is a means of capturing a progression of an attribute of interest, such as behaviors, cognitive processes, or data. For example, Fig. 3 shows a flow chart of the behavior process used by a hypothetical firm for hiring new employees.

4.2.4.2. Evocative knowledge map. A second tool for representing information is an evocative knowledge map [42]. Knowledge maps have been used successfully in disciplines ranging from decision making (e.g., [18]) to educational curriculum development (e.g., [62]). An evocative knowledge map captures information relevant to a particular event or attribute of interest, and can represent causation, influences, dependencies, or simple associations between factors. The factors represented can include arguments, judgments, facts, or data. The simplicity of evocative knowledge maps allows them to address the obstacles associated with potential differences in the backgrounds of the analysts and users. Thus, evocative knowledge maps are particularly useful early in the IRD process for brainstorming about information relevant to a task or process, and can be used by an analyst with a single user or in a JAD session. Fig. 4 shows an evocative knowledge map created for an employee hiring process. The goal was to determine factors relevant to attracting the best applicant(s) for the job, which was hypothesized to depend on supply and demand forces in the market and the company's reputation. In addition to primary relationships, secondary relationships are usually gathered, e.g., public perceptions helping determine the company's reputation.

4.2.4.3. Influence diagram. Another representational tool is an influence diagram, which is a general technique that has many possible uses [55,69]. An influence diagram is based on the notion that behaviors and ideas are influenced by various activities, goals, beliefs, or other factors. Understanding the factors that underlie behavior can help analysts determine how and why knowledge is used. Influence diagrams are particularly useful in analyzing workflows and decision processes. Fig. 5 represents influences on the workflow steps in a firm's employee hiring process. The influences provide the analyst with important clues about requirements for a decision support system (DSS) to aid in the process. For

![](/api/attachments/T4ZGX45C/fulltext/images/07d85d2d545aa9b94090a5635378832ad17e5a291275694bcdd29ca7f91a9a00.jpg)  
Fig. 3. Flow chart: employee hiring example.

![](/api/attachments/T4ZGX45C/fulltext/images/1fd20ea9fd90b409236443ce4da4b3a4fc0fb92ea52f67b876beef302bfab188.jpg)  
Fig. 4. Evocative knowledge map: employee hiring example.

example, screening applications requires that thresholds be set for each criterion deemed relevant. Such functionality should be built into the DSS.

4.2.4.4. Decision map. A decision map is a technique for understanding users' mental models of decision processes, tasks, or environments. It is one type of cognitive map; cognitive maps have been used to model hierarchical categories of objects, associations between objects, causal relationships, arguments, and decisions $[3,43,50,52,58]$ . Fig. 6 shows a decision map for the process of screening applications in the employee hiring process.

4.2.4.5. Affinity diagram. An affinity diagram is an organizing tool used to locate similar facts, arguments, or other information together (hence, the name “affinity”) [13]. By categorizing information according to higher-level abstract concepts, problems of variety and complexity are reduced. An example of the use of an affinity diagram appears in Figs. 7 and 8. Fig. 7 shows statements made by managers during a discussion of a firm’s hiring practices. Such narratives are common outputs from interactions between analysts and users. The difficulty subsequently facing the analyst is how to organize the information into a useful form. The affinity diagram in Fig. 8 shows one way that the stated information could be organized. Similar arguments are located together, with the analyst creating the category names in a bottom-up fashion based on the content of the arguments. In this manner, sense can be made of the group discussion.

![](/api/attachments/T4ZGX45C/fulltext/images/4d791a80fe21534034d9a18f49f3acf0f6f4fd465d69b632b33fbd7837d3d235.jpg)  
Fig. 5. Influence diagram: employee hiring example.

4.2.4.6. Note board. A note board may take several forms, but it is typically a board on an easel or wall onto which tacks, staples, or sticky notes can be attached.

Information is written on cards or paper, and these notes are then attached to the board. The information on the cards may be data or process information, functional or non-functional information, technical information, etc. Because of the method of attachment, the note cards are movable. The board helps analysts and users visualize information and arrange it in a useful or logical manner. A note board is especially useful for groups of users, as it provides a shared representation of the information for discussion [39]. $^{4}$

![](/api/attachments/T4ZGX45C/fulltext/images/87f1b6b28861a00d26184bfc720d108eb618e6373b1703c5c0bb2901192b0465.jpg)  
Fig. 6. Decision map: employee hiring example—screening applications received.

In summary, the techniques described earlier are hypothesized to be useful in all stages of the requirements determination process. The techniques can be used singly or in combination to improve the requirements for a system.

## 5. Conclusion

Requirements determination is central to the development of IS. Understanding user needs is an obvious prerequisite to building a functional system. However, such an understanding is inhibited by a variety of psychological and social limitations due to the people involved. This paper has described many of these limitations and has offered techniques for mitigating them. Improving the requirements determination

Person A: We'll want to have a comprehensive system that will help us make hiring decisions in a structured way.

Person B: But we don't want a system that makes decisions for us.

Person A: Right, but we need help in structuring the decisions.

Person C: Plus, I'd like to feel confident that there is consistency in our decisions, that we're applying our criteria consistently.

Person D: Can we have the system help us in selecting the criteria? I mean, if we tell the system the position, can we get some kind of optimal weighting of the criteria?

Person C: Well, we couldn't get that without building expertise into it, like an expert system.

Person E: I read somewhere that simple expert systems do a better job of making hiring decisions than managers do.

Person B: Oh, I don't know about that. I wouldn't trust a computer that makes those kinds of decisions.

Person A: Well, I know there are advantages to expert systems, especially the way that they apply criteria consistently. We need to do that both for the sake of fairness and to get the best people.

Person C: I think a system that structures the decisions for us but leaves the final choice to us is what we need. You know, a decision support system.

Person E: Well I'm not opposed to a decision support system, but I think we ought to let the computer do the computations. That article I read said that managers cannot even apply their own criteria consistently.

Person D: So we tell the system what the criteria are and then it tells us which candidate would be best?

Person E: That's right.

Person B: I just don't see that we need this system. It will be expensive, and I don't think it will improve our hiring. You just can't quantify a lot of the factors that go into hiring.

Person F: I agree. How can a computer help you assess an applicant's appearance, or facial expressions, or enthusiasm?

Person A: Simple. You assign ratings to those things.

Person C: And you don't let them carry too much weight. That's the problem with making ad hoc decisions about candidates. Just because you think an applicant looked at you with a stupid expression makes you reject him when he otherwise may be the best candidate. That's not rational.

Fig. 7. Arguments made in group discussion.

process will lead to better information systems and to improved outcomes for organizations in terms of revenues, costs, and customer satisfaction.

Because requirements determination involves assessing human needs for functionality in highly complex organizational systems, the process is inherently difficult. There are no magical ways of solving requirements determination problems because complexity is essential to the process [15]. Hence, improving the IRD process must be undertaken incrementally, by furthering our understanding of business tasks, of human cognition and behavior, and of the gathering, representation, and verification of knowledge.

![](/api/attachments/T4ZGX45C/fulltext/images/508f2e2b5a57606cbc6778bc4a826024e181f8b4019c6c28c8c54c4ce5c4c9b0.jpg)

## Acknowledgements

The authors thank Iris Vessey, Rosann Collins, Barbara Klein, the Editor-in-Chief, and three anonymous reviewers for their useful comments on previous versions of this paper.

## References

[1] R. Ackoff, Management misinformation systems, Management Science 14, 1967, pp. B147–B156.

[2] J.W. Alba, L. Hasher, Is memory schematic? Psychological Bulletin 93, 1983, pp. 203–231.

[3] R. Axelrod, The Structure of Decision, Princeton University Press, Princeton, NJ, 1976.

[4] J. Baron, J. Beattie, J.C. Hershey, Heuristics and biases in diagnostic reasoning: congruence information and certainty, Organizational Behavior and Human Decision Processes 42, 1988, pp. 88–110.

[5] M.H. Bazerman, Judgment in Managerial Decision Making, Wiley, New York, 1998.

[6] P.G. Benson, S.P. Curley, G.F. Smith, Belief assessment: an underdeveloped phase of probability elicitation, Management Science 41, 1995, pp. 1639–1653.

[7] P.G. Benson, M.L. Nichols, An investigation of motivational bias in subjective predictive probability distributions, Decision Sciences 13, 1982, pp. 225–239.

[8] T.G. Bever, The cognitive basis for linguistic structures, in: J.R. Hayes (Ed.), Cognition and the Development of Language, Wiley, New York, 1970.

[9] B.R. Boehm, Software Engineering Economics, Prentice-Hall, Englewood Cliffs, NJ, 1981.

[10] R.J. Boland, Sense-making of accounting data as a technique of organizational diagnosis, Management Science 30, 1984, pp. 868–882.

[11] R.P. Bostrom, Successful application of communication techniques to improve the systems development process, Information & Management 16, 1989, pp. 279–295.

[12] C.J. Brainerd, V.F. Reyna, Explaining memory free reasoning, Psychological Science 3, 1992, pp. 332–339.

[13] M. Brassard, The Memory Jogger Plus+, GOAL/QPC, Methuen, MA, 1989.

[14] W. Brewer, Memory for randomly sampled autobiographical events, in: U. Neisser, E.W. Winograd (Eds.), Remembering Reconsidered, Cambridge University Press, Cambridge, 1988.

[15] F.P. Brooks, No silver bullet: essence and accidents of software engineering, Computer 20, 1987, pp. 10–19.

[16] G.J. Browne, S.P. Curley, Processes of reasoning with category knowledge in probability forecasting: typicality and perceived variability effects, in: G. Wright, P. Goodwin (Eds.), Forecasting with Judgment, Wiley, Chichester, 1998.

[17] G.J. Browne, M.B. Rogich, An empirical investigation of user requirements elicitation: comparing the effectiveness of

prompting techniques, Journal of Management Information Systems 17, 2001, pp. 223–249.

[18] G.J. Browne, S.P. Curley, P.G. Benson, Evoking information in probability assessment: knowledge maps and reasoning-based directed questions, Management Science 43, 1997, pp. 1–14.

[19] G.J. Browne, V. Ramesh, M.G. Pitts, M.B. Rogich, Representing user requirements: an empirical investigation of formality in modeling tools, in: Proceedings of the Americas Conference on Information Systems, Indianapolis, 1997.

[20] C.R. Byers, D. Blume, Tying critical success factors to systems development, Information & Management 26, 1994, pp. 51–61.

[21] T.A. Byrd, K.L. Cossick, R.W. Zmud, A synthesis of research on requirements analysis and knowledge acquisition techniques, MIS Quarterly 16, 1992, pp. 117–138.

[22] J.M. Carroll, Scenario-Based Design: Envisioning Work and Technology in Systems Development, Wiley, New York, 1995

[23] J. Corter, M. Gluck, Explaining basic categories: feature predictability and information, Psychological Bulletin 111, 1992, pp. 291–303.

[24] J.D. Couger, Creativity and Innovation in Information Systems Organizations, Boyd & Fraser, Danvers, MA, 1996.

[25] S.P. Curley, G.J. Browne, G.F. Smith, P.G. Benson, Arguments in the practical reasoning underlying constructed probability responses, Journal of Behavioral Decision Making 8, 1995, pp. 1–20.

[26] N.P. Dalal, S.B. Yadav, The design of a knowledge-based decision support system to support the information analyst in determining requirements, Decision Sciences 23, 1992, pp. 1373–1388.

[27] S.A. Dart, R.J. Ellison, P.H. Feiler, A.N. Habermann, Software development environments, IEEE Computer 20, 1987, pp. 18–28.

[28] G.B. Davis, Strategies for information requirements determination, IBM Systems Journal 21, 1982, pp. 4–30.

[29] P.J. Denning, Beyond formalism, American Scientist 79, 1991, pp. 8–10.

[30] A.R. Dennis, J.F. George, L. Jessup, J.F. Nunamaker, D.R. Vogel, Information technology to support electronic meetings, MIS Quarterly 12, 1988, pp. 591–624.

[31] K. Ewusi-Mensah, Critical issues in abandoned information systems projects, Communications of the ACM 40, 1997, pp. 74–80.

[32] B. Fischhoff, Debiasing, in: D. Kahneman, P. Slovic, A. Tversky (Eds.), Judgment Under Uncertainty: Heuristics and Biases, Cambridge University Press, Cambridge, 1982.

[33] B. Fischhoff, M. Bar-Hillel, Focusing techniques: a shortcut to improving probability judgments, Organizational Behavior and Human Performance 34, 1984, pp. 175–194.

[34] M.D. Fraser, K. Kumar, V.K. Vaishnavi, Informal and formal requirements specification languages: bridging the gap, IEEE Transactions on Software Engineering 17, 1991, pp. 454–466.

[35] M.D. Fraser, K. Kumar, V.K. Vaishnavi, Strategies for incorporating formal specifications, Communications of the ACM 37, 1994, pp. 74–86.

[36] C. Gane, T. Sarson, Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Englewood Cliffs, NJ, 1979.

[37] V. Goel, P. Pirolli, Motivating the notion of generic design within information processing theory: the design problem space, AI Magazine 10, 1989, pp. 18–36.

[38] S.E. Gordon, R.T. Gill, Knowledge acquisition with question probes and conceptual graph structures, in: T.W. Lauer, E. Peacock, A.C. Graesser (Eds.), Questions and Information Systems, Lawrence Erlbaum, Hillsdale, NJ, 1992.

[39] J.T. Hackos, J.C. Redish, User and Task Analysis for Interface Design, Wiley, New York, 1998.

[40] R.M. Hogarth, Judgement and Choice, Wiley, Chichester, 1987.

[41] K. Holtzblatt, H.R. Beyer, Requirements gathering: the human factor, Communications of the ACM 38, 1995, pp. 31–32.

[42] R.A. Howard, Knowledge maps, Management Science 35, 1989, pp. 903–922.

[43] A.S. Huff, Mapping strategic thought, in: A.S. Huff (Ed.), Mapping Strategic Thought, Wiley, New York, 1990.

[44] I. Janis, Victims of Groupthink, Houghton Mifflin, Boston, 1972.

[45] H.J. Jeffrey, A.O. Putnam, Relationship definition and management: tools for requirements analysis, Journal of Systems and Software 24, 1994, pp. 277–294.

[46] P.E. Johnson, K. Jamal, R.G. Berryman, Effects of framing on auditor decisions, Organizational Behavior and Human Decision Processes 50, 1991, pp. 75–105.

[47] L. Johnson, N.E. Johnson, Knowledge elicitation involving teachback interviewing, in: A. Kidd (Ed.), Knowledge Elicitation for Expert Systems, Plenum Press, New York, 1987.

[48] P.G.W. Keen, Information systems and organizational change, Communications of the ACM 24, 1981, pp. 24–32.

[49] A. Koriat, S. Lichtenstein, B. Fischhoff, Reasons for confidence, Journal of Experimental Psychology: Human Learning and Memory 6, 1980, pp. 107–118.

[50] K.Y. Kwahk, Y.G. Kim, Supporting business process redesign using cognitive maps, Decision Support Systems 25, 1999, pp. 155–178.

[51] T.J. Larsen, J.D. Naumann, An experimental comparison of abstract and concrete representations in systems analysis, Information & Management 22, 1992, pp. 29–40.

[52] S. Lee, J.F. Courtney, R.M. O'Keefe, A system for organizational learning using cognitive maps, Omega 20, 1992, pp. 23–36.

[53] R. Leifer, S. Lee, J. Durgee, Deep structures: real information requirements determination, Information & Management 27, 1994, pp. 275–285.

[54] L. Markoczy, J. Goldberg, A method for eliciting and comparing causal maps, Journal of Management 21, 1995, pp. 305–333.

[55] M.W. Merkhofer, Using influence diagrams in multiattribute utility analysis—improving effectiveness through improving communication, in: R.M. Oliver, J.Q. Smith (Eds.), Influence Diagrams, Belief Nets and Decision Analysis, Wiley, New York, 1990.

[56] L.B. Methlie, Systems requirements analysis—methods and models, in: H. Lucas, et al. (Eds.), The Information Systems Environment, North-Holland, Amsterdam, 1980.

[57] R.T. Mittermeir, P. Hsia, R.T. Yeh, Alternatives to overcome the communication problem of formal requirements analysis, in: M. Ohno (Ed.), Requirements Engineering Environments, North-Holland, Amsterdam, 1982.

[58] A.R. Montazemi, D.W. Conrath, The use of cognitive mapping for information requirements analysis, MIS Quarterly 10, 1986, pp. 45–55.

[59] J.W. Moody, J.E. Blanton, P.H. Cheney, A theoretically grounded approach to assist memory recall during information requirements determination, Journal of Management Information Systems 15, 1998, pp. 79–98.

[60] A. Newell, H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[61] J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34, 1991, pp. 40–61.

[62] A. O'Donnell, Searching for information in knowledge maps and texts, Contemporary Educational Psychology 18, 1993, pp. 222–239.

[63] I. Oliver, H. Langford, Myths of demons and users, in: R. Galliers (Ed.), Information Analysis: Selected Readings, Addison-Wesley, Reading, MA, 1987.

[64] H.M. Parsons, Hawthorne: an early OBM experiment, Journal of Organizational Behavior Management 12, 1992, pp. 27–43.

[65] D.N. Perkins, R. Allen, J. Hafner, Difficulties in everyday reasoning, in: W. Maxwell (Ed.), Thinking: The Expanding Frontier, Franklin Institute Press, Philadelphia, 1983.

[66] S.L. Pfleeger, Software Engineering, Prentice-Hall, Englewood Cliffs, NJ, 2001.

[67] M.G. Pitts, The use of evaluative stopping rules in information requirements determination: an empirical investigation of systems analyst behavior, Doctoral Dissertation, Dissertation Abstracts International, Vol. 60-05A, 1376, University of Maryland, Baltimore, 1999.

[68] C. Potts, K. Takahashi, A.I. Anton, Inquiry-based requirements analysis, IEEE Software 11, 1994, pp. 21–32.

[69] A. Ramaprasad, E.A. Poon, A computerized interactive technique for mapping influence diagrams (MIND), Strategic Management Journal 6, 1985, pp. 377–392.

[70] V. Ramesh, G.J. Browne, Expressing causal relationships in conceptual database schemas, Journal of Systems and Software 45, 1998, pp. 225–232.

[71] D.J. Reifer, Web development: estimating quick-to-market software, IEEE Software 17, 2000, pp. 57–64.

[72] D. Reisberg, Cognition, W.W. Norton & Company, New York, 1997.

[73] S. Robertson, J. Robertson, Mastering the Requirements Process, ACM Press, Harlow, England, 1999.

[74] M. Ross, E. Buehler, Creative remembering, in: U. Neisser, R. Fivush (Eds.), The Remembered Self, Cambridge University Press, Cambridge, 1994.

[75] K.D. Schenk, N.P. Vitalari, K.S. Davis, Differences between novice and expert systems analysts: what do we know and what do we do? Journal of Management Information Systems 15, 1998, pp. 9–50.

[76] D.A. Schön, The Reflective Practitioner, Basic Books, New York, 1983.

[77] M. Schustack, Thinking about causality, in: R.J. Sternberg, E.E. Smith (Eds.), The Psychology of Human Thought, Cambridge University Press, Cambridge, 1988.

[78] H.A. Simon, Models of Man, Wiley, New York, 1957.

[79] H.A. Simon, Information processing models of cognition, Annual Review of Psychology 30, 1979, pp. 363–396.

[80] H.A. Simon, The Sciences of the Artificial, MIT Press, Cambridge, MA, 1981.

[81] C. Spetzler, C.-A. Stael von Holstein, Probability encoding in decision analysis, Management Science 22, 1975, pp. 340–358.

[82] W. Stacy, J. Macmillan, Cognitive bias in software engineering, Communications of the ACM 38, 1995, pp. 57–63.

[83] Standish Group, Chaos, Research Paper, The Standish Group International, Inc., 1996.

[84] V.C. Storey, C.B. Thompson, S. Ram, Understanding database design expertise, Data and Knowledge Engineering 16, 1995, pp. 97–124.

[85] J.A. Turner, A comparison of the process of knowledge elicitation with that of information-requirements determination, in: W.W. Cotterman, J.A. Senn (Eds.), Challenges and Strategies for Research in Systems Development, Wiley, New York, 1992.

[86] A. Tversky, D. Kahneman, Availability: a heuristic for judging frequency and probability, Cognitive Psychology 4, 1973, pp. 207–232.

[87] A. Tversky, D. Kahneman, On the psychology of prediction, Psychological Review 80, 1973, pp. 237–251.

[88] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185, 1974, pp. 1124–1131.

[89] J.S. Valacich, J.F. George, J.A. Hoffer, Essentials of Systems Analysis and Design, Prentice-Hall, Englewood Cliffs, NJ, 2001.

[90] J.R. Valusek, D.G. Fryback, Information requirements determination: obstacles within, among and between participants, in: R. Galliers (Ed.), Information Analysis: Selected Readings, Addison-Wesley, Reading, MA, 1987.

[91] I. Vessey, S. Conger, Requirements specification: learning object, process, and data methodologies, Communications of the ACM 37, 1994, pp. 102–113.

[92] N.P. Vitalari, Structuring the requirements analysis process for information systems: a propositional viewpoint, in: W.W. Cotterman, J.A. Senn (Eds.), Challenges and Strategies

for Research in Systems Development, Wiley, New York, 1992.

[93] D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge University Press, Cambridge, 1986.

[94] D.B. Walz, J.J. Elam, B. Curtis, Inside a software design team: knowledge acquisition, sharing, and integration, Communications of the ACM 36, 1993, pp. 63–77.

[95] G.S. Waters, D. Caplan, Processing resource capacity and the comprehension of garden path sentences, Memory and Cognition 24, 1996, pp. 342–355.

[96] H.J. Watson, M.N. Frolick, Determining information requirements for an EIS, MIS Quarterly 17, 1993, pp. 255–269.

[97] J.C. Wetherbe, Executive information requirements: getting it right, MIS Quarterly 15, 1991, pp. 51–65.

[98] R.E. Wood, Task complexity: definition of the construct, Organizational Behavior and Human Decision Processes 37, 1986, pp. 60–82.

[99] S.B. Yadav, Determining an organization's information requirements: a state of the art survey, Database (1983) 3–20.

[100] S.B. Yadav, R.R. Bravoco, A.T. Chatfield, T.M. Rajkumar, Comparison of analysis techniques for information requirement determination, Communications of the ACM 31, 1988, pp. 1090–1097.

[101] R.M. Young, P. Barnard, T. Simon, J. Whittington, How would your favorite user model cope with these scenarios? SIGCHI Bulletin 20, 1989, pp. 51–55.

[102] R.W. Zmud, W.P. Anthony, R. Stair, The use of mental imagery as a requirements analysis technique, in: W.W. Cotterman, J.A. Senn (Eds.), Challenges and Strategies for Research in Systems Development, Wiley, New York, 1992.

Glenn J. Browne is an Associate Professor of Information Systems and Director of the Institute for Internet Buyer Behavior at Texas Tech University. He received his PhD from the Carlson School of Management at the University of Minnesota. His research interests include information requirements determination, behavioral decision-making processes, and systems analysis and design considerations for e-business. His articles have appeared in Management Science, Organizational Behavior and Human Decision Processes, the Journal of Management Information Systems, the Journal of Systems and Software, and other journals.

V. Ramesh is an Assistant Professor of Information Systems and Ford Motor Company Teaching Fellow in the Department of Accounting and Information Systems at Kelley School of Business, Indiana University. He has published over 25 papers in leading journals, books and conferences. His areas of expertise are in database modeling and design, systems design and development, heterogeneous databases, and groupware systems.
