---
otero_id: 27097
otero_key: "5DYM2Y75"
title: "Intelligent Interface Design: An Empirical Assessment of Knowledge Presentation in Expert Systems1"
authors: "Donna M. Lamberti; William A. Wallace"
year: "1990"
journal: "MIS Quarterly"
doi: "10.2307/248891"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Intelligent Interface Design: An Empirical Assessment of Knowledge Presentation in Expert Systems

Author(s): Donna M. Lamberti and William A. Wallace

Source: MIS Quarterly, Vol. 14, No. 3 (Sep., 1990), pp. 279-311

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/248891

Accessed: 12-12-2015 15:05 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Intelligent Interface Design: An Empirical Assessment of Knowledge Presentation in Expert Systems $^{1}$

By: Donna M. Lamberti
AI/Information Systems Research Staff
IBM Cambridge Scientific Center
101 Main Street
Cambridge, Massachusetts 02142

William A. Wallace  
Decision Sciences and Engineering Systems  
Rensselaer Polytechnic Institute  
Troy, New York 12180

## Abstract

This research evaluates intelligent interface requirements for knowledge presentation in an expert system used for diagnostic problem solving. In a field study, interactions between employee expertise, knowledge presentation format (procedural vs. declarative), question type (requiring abstract vs. concrete knowledge organization), and task uncertainty are examined for employee problem-solving and decision-making performance (speed and accuracy). Also evaluated are confidence in system recommendations and lines-of-reasoning, as well as user satisfaction with the system interface. The study provides findings that are discussed within the context of intelligent interface requirements for organizational information systems. The results show that high-skill users perform significantly faster and more accurately when solving the problems and have self-reported confidence ratings that are higher than those of low-skill users. The expert system, however, has a greater impact on improving performance for low-skill users than for high-skill users. A relationship is found between skill level and task uncertainty indicating that different skill-level users require different presentation formats paralleling their conceptual representations of the problem. The interaction between skill level and knowledge organization is confirmed with results showing that low-skill users perform faster than high-skill users on questions requiring concrete knowledge organization; whereas high-skill users perform better when presented with questions requiring abstract knowledge organization.

Keywords: Expert systems, knowledge presentation, systems design, decision making, computer-human interface, human problem solving, cognitive models

ACM Categories: D.2.1, D.2.2, H.1.2, H.4.2, I.2.1, I.2.4, I.2.8, K.6.3

## Introduction

Since the mid-1960s, artificial intelligence (AI) has achieved some success in the development of expert systems (ES) or, more accurately, knowledge-based systems for business applications. ESs are commonly defined as special-purpose computer programs that use expert knowledge to attain high levels of performance in a narrow problem area (Hayes-Roth, et al., 1983). These systems use symbolic reasoning in conjunction with numerical processing to attain a level of competence that is likely to be better than a human with limited expertise in the particular problem area (Luconi, et al., 1986). ESs can operate as independent consultation systems, or they can be integrated with other, more traditional information systems (e.g., managing the selection of models used in problem solving or serving as an interface between the user and the model base). This research focuses on ESs as stand-alone systems.

Research on the use of ES can provide opportunities to understand human capabilities and limitations in the context of organizational decision making. In particular, research can help us learn how to match the ES and its knowledge base, developed from a specific representation scheme, with the user's information processing needs. This match can be achieved by relating the design requirements of ES interfaces to the user's problem-solving performance. While several research efforts have investigated the design of interface components (Alavi and Napier, 1986; Benbasat and Schroeder, 1977; Benbasat and Taylor, 1982; Coombs and Alty, 1980; Dos Santos and Bariff, 1988; Keller, 1985; Stohr and White, 1982), few of them have focused on the integration of these components.

Effective design of interfaces for intelligent systems requires an empirical understanding of the relationships between variables such as user expertise, knowledge presentation format, problem characteristics, and user decision procedures. This realization has resulted in considerable research in the management information systems (MIS) and decision support systems (DSS) literature (Bennett, 1976; DeSanctis, 1984; Ghani, 1981; Hurst, 1978; Lusk and Kersnick, 1979; Sharda, et al., 1988; Zmud, 1979). Yet most of this research focuses on studying these variables separately and often neglects the crucial aspect of interactions among the variables and their impact on the success of organizational information systems. Possible reasons for this situation include the lack of a theory for organizing, and accounting for, the variability in choosing design options.

In terms of ES, research investigating the impact of these variables on the design of user interfaces is essentially non-existent. ESs are unique in decision aid technology because they contain a knowledge base represented as facts, as well as heuristic procedures for how to solve problems; hence, by definition, they exhibit a more sophisticated reasoning capability. These systems dynamically draw conclusions and make recommendations similar to a human advisor.

In studying the ES problem-solving process as it impacts interface requirements (Turban and Watkins, 1986), it is clear that much of the research in MIS and DSS is not directly applicable. A primary feature that sets ES apart from DSS is a more powerful capability for explaining the lines-of-reasoning the system uses to solve a problem. Given the structure of ES, the way in which knowledge is represented internally determines the interface presentation of lines-of-reasoning. An effective explanation capability requires that ESs focus on cognitive processes underlying the notion of expertise. This focus adds another dimension to interface design. In contrast, MIS and DSS behavioral research have tended to concentrate more on user personality traits and abilities as they impact interface design. Empirical study is needed to clarify the important relationships that determine effective modes of communication between users and ES. Clearly, if an ES is to contribute to organizational productivity, users must have confidence in its reasoning strategies and knowledge base (i.e., its expertise).

The purpose of this research is to gain empirically a better understanding of interface requirements for ES as intelligent decision support tools. Given the emphasis placed on ES reasoning capabilities, we have decided to concentrate on the requirements for: (1) knowledge presentation in system dialogue and lines-of-reasoning; and (2) cognitive compatibility between the user and the ES as determined by varying levels of user expertise. Specifically, the research examines the impact of the following variables on ES users' diagnostic problem solving: user expertise, knowledge presentation format (procedural vs. declarative), question type (requiring abstract vs. concrete knowledge organization), level of problem uncertainty (task characteristics), and decision-making procedures on the diagnostic problem-solving of ES users. Selection of the variables for this study was prompted by the lack of empirical research in the ES area, as well as an acknowledgement that these variables have the most direct bearing on ES interface design given the architecture of these systems. To map the significant relationships between these variables, emphasis is placed on the link between internal knowledge representation and its external presentation in ES. The conceptual and empirical basis for selecting this set of variables is discussed in the following sections.

## User expertise in problem solving

A review of the literature in the MIS field shows that little attention has been paid to the user's expertise or skill level in problem solving when using an information system (DeSanctis, 1984). This situation, coupled with the fact that expert systems are being implemented on an increasingly wider scale within organizations, influenced the selection of skill level as a variable to be investigated in this study. For the purpose of this research, skill level is defined as the possession and organization of domain-specific knowledge and procedural skill that can be accessed and efficiently applied during problem solving (Vitalari and Schenk, 1989).

Research on skill acquisition shows that humans usually develop qualitatively different perceptions of a task and/or mode of decision making as their skill improves (Dreyfus and Dreyfus, 1986). In an organizational setting a system must be robust enough to support users with varying levels of expertise. It is crucial to understand differences between high- and low-skill employees' approaches to problem-solving in order to design a system that adequately supports their strategies.

This study was conducted using computer diagnostic programmers working for a large computer manufacturer. Although these programmers differed in skill level for diagnostic tasks, they were relatively homogeneous with respect to educational background, age, and length of company employment. Prior to beginning the study, a task analysis was performed to identify and evaluate differences in domain knowledge and procedural skill as applied to the type of problems shown in Figures 1 and 2. This analysis indicated skill level differences that were verified by the experimental results. A detailed discussion of the type of tasks performed is included in the methodology section.

## Knowledge presentation format

The various ways that knowledge can be represented within the ES knowledge base have been widely discussed in the literature (Bosman and Sol, 1985; Fox, 1985; Reddy and Newell, 1974; Schank and Abelson, 1977; Winograd, 1972). Despite the emphasis placed on internal representation of system knowledge, little attention has been given to how the same knowledge presented in the user interface affects ES users' performance. Yet the way knowledge is presented to users can have a direct bearing on their selection of problem-solving strategies (Jarvenpaa, 1988).

A controversy exists over the appropriate knowledge presentation format for system lines-of-reasoning. This issue is new to information systems research—the explanation of lines-of-reasoning is unique to knowledge-based systems technology. The user's ability to view lines-of-reasoning is a critical factor in system acceptance. Consequently, because it is key to fostering user confidence in ES, the design of accurate and comprehensible explanation facilities has received increasing attention. This research investigates procedural and declarative formats for knowledge presentation as it relates to designing effective user interfaces for expert systems.

The procedural presentation employs premise-action pairs represented in an IF...THEN production-rule format. Each rule embodies a single modular chunk of knowledge and states explicitly in the premise (IF) all necessary context. The action part (THEN) indicates one or more conclusions that can be drawn if the premises are satisfied. A production system usually requires a procedural control strategy that specifies the order in which the rules will be compared to a database and, consequently, be executed to specify the sequence of actions used to solve a problem.

The declarative presentation contains knowledge presented as a static collection of facts about objects, events, and situations. As Schor (1986) points out, “declarative knowledge can be characterized as knowledge lacking execution-sequence information” (p. 37). The declarative presentation, however, requires a computational method to be specified in order to carry out the solution to a problem for which the knowledge is applicable. In this sense, it is incomplete, lacking a built-in procedural interpretation of how to carry out the steps or when to apply the rules needed to solve a problem.

Examples of procedural and declarative lines-of-reasoning presented by the diagnostic ES investigated in this research are shown in Figures 1 and 2. The explanations were those shown to the ES users who participated in the study.

As Pylyshyn (1973) notes, a primary advantage of procedural presentation in interfaces is that using a bottom-up structure allows a small number of procedural rules to cover a wide domain of instances. Similarly, the literature on differences between experts and novices in concept categorization (Adelson, 1981; Anderson, 1982; Wiedenback, 1985) reveals that many things users know are best seen as procedures; it is difficult to describe this knowledge in a declarative way. Knowledge about interrelated facts is taken care of “automatically” in a procedural presentation because the system exerts control over the use of particular knowledge and deals explicitly with the interactions between the different operations.

![](/api/attachments/5DYM2Y75/fulltext/images/83209ec54e9a59999ce999977a2ded30364a669fc2096f16420a83a083670d83.jpg)  
Figure 1. System Abend Example

Perhaps the strongest advantage of procedural presentation is its support of heuristic reasoning. As Georgeff (1982) points out, the programs of complex ES in all domains have a large amount of their knowledge built into their procedures. Those programs that attempt to keep domain-specific knowledge in a non-procedural database do so at the expense of limiting themselves to simple goals. The obvious reason for this is that much of what we know about a domain is of the form, "If you're trying to deduce something under this particular set of conditions, follow this approach."

The primary argument generally made against a procedural presentation is that it requires a piece of knowledge be specified by saying how it is to be used. There may be more than one

Computer Error Condition
A user reported MSG8003 Abend 10 PGMID2657 LOCA61 or LOCAEA (not sure) when editing a DOSF document on a D/T8775. A Level 1 support representative spoke to the customer without resolving the problem. The customer states that he just installed FIX PACKAGE 40 plus some additional PTFS (unsure of numbers). The customer was not sure of what the user was doing at the time of the failure. He has printed the Abend dump and wants to pursue with Level 2. Requeuing to DOSF 104 for further problem determination.

Example Declarative Explanation of what the error means
The last Dataman return code indicates that a non-existent FCE referenced is the cause of the Abend. The error was detected at code point 1. The last data management function was GETWSFBN.
The following information concerning the status of workstore at the time of the Abend has been obtained from the Abend dump. This data can be used to assist the customer in obtaining the failing scenario. At the time of the Abend there was a document in working store. The operator who originally owned this document is in hexadecimal form at displacement X'86' of the same block.
The save stack has been backed out prior to the dump being taken, so it is not valid at this time. However, some residual information may be obtained for analysis of the data in the block.

Example Procedural Explanation of how to fix the error
Follow the procedure outlined to get the system up, minimizing time as well as loss of data.
If there is PGM DGADMRT,
then PGM DATMAN RC is substring (PGM DGADRMT, 8, 30), indicating a non-existent FCE referenced. Check the PABXV control block starting at displacement X'87' for the 15-character document name. Just prior to the Program Abend, the user had entered the GET command/key followed by the Screen Return command/key. At the start of BUF 5 you should see the last command from the operator and a document name. If not, try the PABXI at offset X'D1', where the editor saves the name if the operator did a 'GET' to permanent store.
If PGM STACKLCON = hex'00' and PGM DGASTACK has a value of Program Abend,
then the save stack has been backed out prior to the dump being taken, so it is not valid at this time. However, some residual information may be obtained by analysis of the data in that block. If the save stack pointer in the PABX1 is zero, then the contents of the stack are residual and not reliable.
If bits 5 to 5 in PGM DGBWSTAT is bin'1,'
then PGM WS STATUS has been assigned to module BRGQ7120. The last data management function was GETWSFBN. To analyze the Abend further, use the BRGQ7120 module listing, locate the error code point, and backtrack.

Figure 2. Program Abend Example

possible use, and it may not be possible to specify every use in advance. Also, it is not clear that production formalisms inherent in procedural knowledge are entirely adequate as explanatory tools for users. For example, Schor (1986) argues that traditional condition-action pairs of production are not compatible with the mental models first-line manufacturing managers use to diagnose symptoms of equipment malfunctioning.

The benefits of declarative presentation involve accessibility and communicability. Winograd (1972) has shown that much of what users know is most easily stated as a set of declaratives. Natural language is primarily declarative, and the usual way to communicate information is to break it into statements. This has implications for communicating knowledge content to system users who require knowledge presentation methods to be more understandable.

Thus, there are distinct advantages of both types of presentation resulting from different views of the purpose of knowledge presentation. The flexibility of declarative knowledge comes from its ability to decompose knowledge into definable independent axioms or facts. Procedural knowledge presentation, however, gives an immediate way of formulating the particular problem being solved. To address the lack of empirical research comparing these two forms of presentation, this study evaluated the effect of knowledge presentation on users' problem-solving methodology and decision performance.

## Knowledge organization

Considerable research attention has been directed toward understanding the differences in how experts and novices, in a particular domain, represent conceptual structures for problem solving (Adelson, 1981; 1984; Chase and Simon, 1973; Chi, et al., 1981; de Groot, 1965; Reitman, 1976). Various researchers (Chase and Simon, 1973; de Groot, 1965; Vessey, 1985) have shown that in a particular domain (e.g., chess, computer debugging) experts identify the functional relationships that exist between relevant pieces of information. They use these functional relationships to create internal representation for filtering information and constructing and executing internally consistent reasoning sequences.

Adelson (1981; 1984) has argued that the working representations of experts can be viewed as abstract conceptualizations of the original problem. In contrast, novices focus more on concrete, surface features of the problem. Although the terms abstract and concrete can be defined operationally in a number of different ways, they do appear to distinguish between the cognitions of experts and novices.

The distinction between abstract and concrete representations is central to this study and thus requires further explanation. In general, an abstract representation of a problem includes information on what a particular problem means given its symptoms, including how the particular problem relates to an overall class of problems. For example, the same solution can be reached using several different solution procedures. Effective causal reasoning and problem solving through alternative routes rely heavily on complete procedural knowledge.

Concrete representations focus on specific problem symptoms or surface details of a problem statement (i.e., details on the functioning of computer components). Because concrete representations employ a top-level structure, with incomplete procedural knowledge, they potentially suffer a reduced ability to construct and execute internally consistent reasoning sequences. The evolution of the representations used as novices slowly become experts can be considered as points along a concrete-abstract dimension.

Adelson (1981) finds that expert programmers use abstract, conceptually based representations when attempting to recall programming material, whereas novices use concrete, syntactically based representations. In Adelson's (1981) experiment, subjects were not told that lines of programming code could be organized either conceptually (abstractly) into three programs or syntactically (concretely) into five categories according to the control words they contained. Yet analyses of the order of recall for each group showed that the experts had indeed clustered the lines into complete programs while the novices had clustered the lines according to syntactic categories.

Chi, et al. (1977) elaborated the differences in mental representation for experts and novices. Their investigations conclude that, compared to expert representations, novice representations may be based on poorly formed or qualitatively different categories. Chi, et al. (1977) also note that in some cases, novices lack the knowledge to formulate categories of information that serve as the basis for expert representations. Both experts and novices form a schema that contains a description obtained from the surface features of the problem. However, the schema of the expert is based on the factual principles underlying the problem statement. The expert schema also contains information about how and when to use each of the principles present in the schema.

Most of the research described has focused on the problem solver's internal representation of a problem and to a lesser extent on his or her strategy for solution. In reviewing this literature, an important relationship emerges regarding a problem solver's cognitive representation of problems and the presentation of information required to solve a problem. As a result, questions arise as to how the format and organization of knowledge presented on an ES display affect experts' and novices' problem-solving performance.

In the case of diagnostic ES, the main source of knowledge displayed to users is in the form of questions. For the purpose of this research, the concepts of concrete and abstract knowledge organization were defined in terms of question type. Examples of the questions comprising the ES consultation are shown in Appendix A.

## Task characteristics

The characteristics of the problem-solving task are important to the design of ES because, in part, they determine the solution process for a problem. In decision making, processing strategies can vary with changes in task complexity, among other task characteristics. The information presented in an interface should complement task characteristics in order to support decision making. In an ES, a well-organized presentation of procedural/declarative explanations as well as abstract/concrete question types can be flexibly applied to changing task demands. In complex tasks, for example, a presentation scheme should emphasize meaningful patterns of information through a coherent organization of information representing the elements and relations contained in the problems. Thus, presentation format can be used to highlight information needed for solution procedures and their conditions of applicability.

Problems can be characterized according to numerous criteria. In this research, problem types lend themselves readily to classification according to degree of uncertainty. Task uncertainty is defined as the difference between the information required to solve the problem and the amount already possessed by the system user (Galbraith, 1977). According to this definition, the amount of information required to solve a problem is determined by the goal diversity (e.g., number of possible solutions, factors entering into the decision process, etc.), the number of internal factors about which information must be processed, and the level of goal performance (noting that higher performance levels require that more alternatives and variables be considered).

The task uncertainty in problem solving is usually measured by determining the degree of problem routinization. Routine problems (low uncertainty) can be dealt with by employing rules for solving them and standardized procedures. Nonroutine tasks (higher uncertainty), however, typically require “individual attention” and greater information processing because preplanning for their possible outcomes is either impractical (i.e., there are too many) or impossible (i.e., the information does not exist) (Daft and Macintosh, 1981; Tushman, 1978; 1979).

Several scales measuring routinization have been developed by Withey, et al. (1983), combining the features of several other scales (Daft and Macintosh, 1981; Sims, et al., 1976; Van de Ven and Delbecq, 1974). In this study, the task uncertainty dimension was measured using one of the Withey, et al. (1983) scales because it has a high reported degree of face validity and convergent validity.

## Decision making for diagnostics

Significant interest has emerged in the ES field concerning the development of systems to support diagnostic decision making (Clancey, et al., 1979; Shortliffe, 1976). Diagnosis is the process of determining and classifying the cause or value of an object, event, or situation in a system based on interpretation of potentially noisy data (Stefik, et al., 1982). Noisy data can result from incompleteness of information, questionable reliability of information, and the aggregation or summarization of information from multiple sources (Buchanan and Shortliffe, 1985).

We view the diagnostic situation as one in which the problem solver tries to ascertain the nature of the problem and recommends ways to alleviate it. This situation can be considered closer to “problem solving” than “decision making” (see Smith (1988) for a review of the conceptual distinctions between problem solving and decision making). However, we use the concepts of both problem solving and decision making to capture the complete procedure for addressing problems in the domain studied in this research. This procedure includes two phases: (1) problem solution based on diagnostic assessment; and (2) the decision for a final recommendation, referred to as an action plan, based on knowledge of the solution to the problem.

One of the basic principles that should be kept in mind when designing systems is that they should support or improve the decision making (Benbasat and Dexter, 1986). Understanding the decision process provides insight into what sort of aid to provide a decision maker to effectively improve his or her performance given information processing limitations. Interactions among user skill level, the degree of task uncertainty, and the type of decision for solving a problem directly affect the choice of knowledge presentation alternatives for system explanations.

The type of decision procedure employed is intricately tied to problem-solving task characteristics. Specifically, research (Galbraith, 1977) has pointed out that the degree of uncertainty associated with a task determines to a large extent the complexity of the decision process. The complexity of the decision process depends on whether the process is programmed or non-programmed (Simon, 1960).

A routine task with low uncertainty is solved most effectively using programmed decisions, which are repetitive and well-defined. Programmed decisions are well-structured; because the constraints of the problem are clear, a routine solution procedure is easily specified with relative certainty that the chosen solution will be successful. On the other hand, a non-routine task characterized by higher uncertainty is solved most effectively using a non-programmed decision that is novel and incompletely defined in terms of problem parameters and constraints.

In this study, the users of the ES were required to decide the appropriate action for fixing or circumventing a diagnostic problem. The users made their decisions as a final step, after having consulted the ES and considered its recommendation for solution. The experts involved in the study decided whether each final decision should be classified as either programmed or non-programmed.

## Research Questions

The objective of this research is to better understand the role of knowledge presentation in diagnostic ES. Problem-solving and decision-making performance are evaluated in an organizational setting to identify requirements for the design of system interfaces. The specific issues identified for study are as follows:

## Research issue 1

Do problem-solving tasks, characterized by high and low uncertainty, have a different impact on the information needed by ES users in a decision-making context?

## Hypotheses

H1: For both high- and low-skill employees using the ES, solution time and accuracy will be better for the low- versus high-uncertainty problem.

H2: For both high- and low-skill employees using the ES, decision time and accuracy will be better for the low- versus high-uncertainty problem.

H3: High- and low-skill employees will spend more time reviewing system lines-of-reasoning for the low- versus high-uncertainty problem.

## Research issue 2

What is the relationship between the format of knowledge presentation (procedural versus declarative) and users' performance with respect to problem solving and decision making?

## Hypotheses

H4: Problem-solving and decision-making accuracy will be higher for high-skill employees than for low-skill employees when procedural lines-of-reasoning are displayed.

H5: Accuracy will be higher for low-skill employees than for high-skill employees when declarative explanations are displayed.

H6: The higher the uncertainty associated with the problem task, the better the response time for high-skill employees versus low-skill employees when presented with procedural and declarative lines-of-reasoning.

## Research issue 3

What is the impact of knowledge organization (question type) on high- and low-skill users' performance?

## Hypotheses

H7: Low-skill users will perform faster and make fewer errors than high-skill users on system questions requiring a concrete representation of problem structures, relative to questions requiring an abstract representation.

H8: High-skill users will be faster on system questions requiring an abstract representation of the problem, relative to questions requiring only concrete knowledge.

H9: The accuracy of high-skill users' responses to questions requiring abstract as opposed to concrete knowledge organization will not differ significantly. $^{2}$

H10: High as well as low-skill users' response time and accuracy for questions will be better for the low- versus high-uncertainty problem when questions require either concrete or abstract knowledge organization. $^{3}$ The uncertainty variable may be especially important to lower-skill users, because they do not have at their disposal the rules and constraints for problem solution that higher-skill users do.

## Research issue 4

How do skill-level and problem-solving task uncertainty differences affect ES users' confidence and satisfaction ratings for recommendations, lines-of-reasoning, and decisions?

## Hypotheses

H11: High-skill employees' confidence ratings will be better than those of low-skill employees for system recommendations, lines-of-reasoning, and decisions. Also, overall confidence ratings will be better for the low- versus high-uncertainty problem with respect to system recommendations, lines-of-reasoning, and decisions for an action plan.

H12: Low-skill users will have higher satisfaction ratings for the declaratively formatted question explanations than will high-skill users, while high-skill users will have higher satisfaction ratings for procedurally formatted lines-of-reasoning than will low-skill users.

## Research Methodology Diagnostic expert system

The diagnostic ES evaluated in this study was developed using a rapid prototyping methodology. The system was built using an ES shell, Expert System Environment (ESE) (IBM Corporation, 1987). ESE consists of two complementary products, Expert System Consultation Environment (ESCE) and Expert System Development Environment (ESDE), which make up an ES preparation and execution facility. ESE is a forward- and backward-chaining rule-based system, which consists of a general-purpose family of products for developing and executing ES applications. It provides editing programs for knowledge definition, multiple inference techniques, explicit control specification, and a consultation interface for users.

## Field site and job description

The experiment, including the pilot study, was conducted over a two-year period. The field setting was a computer diagnostic support center within a large organization in the computer industry. The organization's support center aids customers by resolving computer system component problems. The ES was developed to support the functions of support center representatives and diagnostic programmers.

Based on knowledge of various computer system components, the programmer must provide customers the following assistance: (1) perform problem diagnosis; (2) perform database searches required to understand and develop a procedure for problem solution; (3) identify and recommend an “action plan” to resolve the problem; and (4) develop a bypass or circumvention to the problem (a necessary step only for “high-severity” situations). Prior to system implementation, the personnel performed these job tasks by using a computer terminal to monitor a queue of customer calls and to search an on line mainframe database for previously reported problem records.

## Problem-solving task description

Before beginning this research, a task analysis was performed to gain a thorough understanding of the work-setting factors that affect the diagnostic programmers' performance level. The analysis yielded descriptive information about the type of problem tasks encountered, the procedures employed by programmers when solving a problem task, and the decision environment within the organization.

There are several types of problem tasks in which the diagnostic programmers specialize. The general categories of problems includes System Abend $^{4}$ (hardware-related, e.g., system memory corrupted), Program Abend (software-related, e.g., null pointer in program not recognized), System Hang (e.g., system in a loop or a wait), user errors, incorrect output, and problems with documentation. Although the ES is designed to provide recommendations for each of these problem categories, System Abend and Program Abend problems were chosen to be representative of the overall nature of problem areas. The problems used in the study, as shown in Figures 1 and 2, were based on actual problems documented in a database.

## Diagnostic expert system purpose and capabilities

The ES consists of a question-answer dialogue. When a problem call is received from a customer, the diagnostic programmers use the ES to aid them in structuring a formulation of the problem and a pathway to its solution. Depending on the diagnostic programmer's responses, the consultation dialogue may take various paths until a recommendation is reached. In addition to asking specific questions, the user has the ability to use special commands for assistance during a consultation session. For example, the user may ask the system "WHY" it asked a particular question, or "HOW" it arrived at a specific recommendation. The system allows the user to make non-committal responses in the case of uncertain and/or incomplete information.

## Method

## Subjects

Ninety diagnostic programmers participated in the study. Each employee was randomly assigned to either the experimental or control condition. Descriptive statistics performed on responses to a demographics questionnaire showed that although the programmers worked on different products, they were relatively homogeneous in terms of education, time in job, and major job duties. Table 1 shows the demographic data for the programmers.

## Design

The study was quasi-experimental, employing a multi-factor, mixed design with repeated measures. The design has between-subject factors of employee skill level and using system versus not using system and within-subject factors of knowledge required for answering questions (abstract versus concrete), knowledge presentation format (procedural versus declarative), and task uncertainty (high versus low).

The dependent variables were: (1) problem-solving time and accuracy; (2) question-answer time and accuracy; (3) decision time and accuracy (for an action plan); (4) time spent to query question explanations and system lines-of-reasoning; (5) employee confidence in system recommendations, lines-of-reasoning, and action plan decisions; and (6) employee satisfaction with system capabilities.

## Procedure

## Skill level

A “general information” questionnaire was administered to determine the programmers’ proficiency in computer system diagnostics. The questionnaire used two criteria to judge skill level: (1) the different types of diagnostic problems; and (2) the number of different types of computer system components in which programmers specialize.

An overall skill-level score was obtained by taking a weighted average of the scale responses to questions for each of the aforementioned criteria and combining the computed skill-level scores for the two parts of the questionnaire. A median split was performed on these scores to form two groups, high-skill and low-skill. The distribution of skill-level scores ranged from 1,000 to 10,000, out of a possible range of 0 to 12,000 points, with the median split between 5,000 and 5,500. This indicates the representativeness of the subject sample with respect to varying skill level.

Table 1. Demographic Statistics

<table><tr><td></td><td>Total (n = 90)</td><td>Percent (100%)</td></tr><tr><td colspan="3">Job Title</td></tr><tr><td>Staff Programmer</td><td>12</td><td>13</td></tr><tr><td>Senior Assoc. Programmer</td><td>21</td><td>23</td></tr><tr><td>Associate Programmer</td><td>34</td><td>38</td></tr><tr><td>Programmer</td><td>23</td><td>26</td></tr><tr><td colspan="3">Major Job Duties*</td></tr><tr><td>Customer Contact</td><td>-</td><td>38</td></tr><tr><td>PMR Analysis</td><td>-</td><td>37</td></tr><tr><td>APAR Handling</td><td>-</td><td>20</td></tr><tr><td>Administrative</td><td>-</td><td>5</td></tr><tr><td colspan="3">Length of Time in Current Job</td></tr><tr><td>0-1 yr.</td><td>10</td><td>11</td></tr><tr><td>2-3 yrs.</td><td>35</td><td>39</td></tr><tr><td>4-5 yrs.</td><td>3</td><td>3</td></tr><tr><td>6-7 yrs.</td><td>35</td><td>39</td></tr><tr><td>8 or more yrs.</td><td>7</td><td>8</td></tr><tr><td colspan="3">Length of Time in Company</td></tr><tr><td>0-1 yr.</td><td>11</td><td>12</td></tr><tr><td>2-3 yrs.</td><td>18</td><td>20</td></tr><tr><td>4-5 yrs.</td><td>27</td><td>30</td></tr><tr><td>6-7 yrs.</td><td>19</td><td>21</td></tr><tr><td>8 or more yrs.</td><td>15</td><td>17</td></tr><tr><td colspan="3">Highest Degree</td></tr><tr><td>High School</td><td>1</td><td>1</td></tr><tr><td>Assoc. (2 yr.)</td><td>20</td><td>22</td></tr><tr><td>Bachelors</td><td>44</td><td>49</td></tr><tr><td>Masters</td><td>25</td><td>28</td></tr><tr><td>Ph.D.</td><td>-</td><td>-</td></tr><tr><td>Other</td><td>-</td><td>-</td></tr><tr><td colspan="3">Field of Study - Latest Degree</td></tr><tr><td>Computer Science</td><td>30</td><td>33</td></tr><tr><td>Applied Mathematics</td><td>24</td><td>27</td></tr><tr><td>Math Programming</td><td>6</td><td>7</td></tr><tr><td>Computer Systems</td><td>24</td><td>27</td></tr><tr><td>Data Processing</td><td>4</td><td>4</td></tr><tr><td>Technician</td><td>2</td><td>2</td></tr></table>

The employees were also asked to solve a short "warm up" problem task. The warm-up task was a documented Program Abend problem presented in a format similar to the System Abend and Program Abend problems used for the experimental session. The correlation between performance accuracy on this task and the scores on the questionnaire was computed to determine validity of the questionnaire. $^{4}$

## Knowledge presentation format

Knowledge presentation format is defined as whether the ES knowledge is presented in a procedural or declarative format. The ES was designed to incorporate both types of presentation formats in displaying declarative question explanations and procedural lines-of-reasoning for its recommendations. There were 20 explanations shown for the System Abend and another 20 for the Program Abend, with one explanation associated with each question. The recommendation lines-of-reasoning were shown to users at the end of the consultation.

## Knowledge organization

Knowledge organization, the second independent variable, refers to the type of knowledge requirements the ES questions placed on an employee. The ES was designed to incorporate a variety of different types of questions placed randomly throughout the consultation. Questions were classified as abstract (i.e., requiring the employee to possess knowledge of how specific computer components relate to one another in solving the problem) or concrete (i.e., requiring the employee to possess concrete, detailed knowledge about computer components).

Five experts, employed by the organization as diagnostic computer programmers, classified each question presented by the ES. Each expert was asked to rate each question on a five-point Likert-style scale indicating the degree to which high-level (abstract) or low-level (concrete) skills were needed to answer the question. For each question, an unweighted average of the ratings of the experts was taken. There was a total of ten concrete questions and ten abstract for each task. Examples of the experimental questions displayed during the consultation and their mean ratings are shown in Appendices A and B.

After the completion of the experimental session, each employee was also asked to rate the questions. The employees' ratings were compared with the experts' ratings to ensure that the employees perceived the questions in the same was as did the experts. The correlations between expert and employee ratings of questions are shown in Appendix B.

## Task uncertainty

To determine task uncertainty, a brief questionnaire incorporating a modified version of the Withey, et al. (1983) scale was given to the five experts. The questionnaire measured the degree of routinization and, hence, uncertainty associated with the System and Program Abend tasks by assessing dimensions of analyzability and number of exceptions. For each subject-matter expert, an unweighted average of the ratings given on the two dimensions was calculated and then averaged across the five experts to arrive at an overall task score. Based on the task scores, the Program Abend problem was classified as having higher uncertainty than the System Abend problem.

## Time

## Problem-Solving Time

The first dependent variable was problem-solving time. For the experimental group, total time for problem solution was defined as the time elapsed from when the consultation began (i.e., when the user hit the “enter” key) until the system recommendation was displayed. For the control group, problem-solving time was measured from the first step in the solution procedure until the subject gave a recommendation. The total time for problem solution was measured continuously in minutes, seconds, and 1/100ths of a second by an analog timer.

## Question-Answering Time

The second dependent variable was the time a programmer spent on each question. Question time was measured as the time from when a question was first displayed by the expert system until the user pressed the “enter” key to proceed to the next question. The amount of time spent on each question was clocked in seconds and 1/100ths of a second. A median response time was obtained for the set of abstract questions and for the set of concrete questions. Also, the total number of abstract and concrete questions that a user viewed was counted. If users made an error and the consultation proceeded down a question path irrelevant to solving the problem, questions displayed on this path were not taken into account for the data analysis.

## Decision Time

The third dependent variable was decision time. For both the experimental and control groups, decision time was defined as the time it took for a user to arrive at an action plan. For the experimental group, decision time was measured from the presentation of a system recommendation until the arrival of an action plan. Total decision time included the time a user spent querying the system to view the lines-of-reasoning. The total decision time was measured continuously, in minutes, seconds, and 1/100th of a second.

The System Abend problem took an average of 25 minutes to complete, compared to 38 minutes for the Program Abend problem. As part of the scenario, each user was asked to provide an action plan for problem solution to the customer.

## Accuracy

For the experimental group, problem-solving accuracy was defined as the number of errors made by a user when answering system questions. Typing errors were not included in the total error count. Total performance accuracy was comprised of accuracy on the individual questions for a consultation. If the ES or an associated software or hardware component failed during the testing session, the session was terminated. For each control group employee, performance accuracy was measured by taking an unweighted average of the number of decision errors as determined by the five subject-matter experts.

For both the experimental and control groups, decision accuracy was defined as the extent to which the employee's final action plan for problem solution was correct or incorrect. Documented action plans for two problem scenarios served as the criteria used by subject-matter experts to judge the accuracy of the employees' action plans. The two problem scenarios used in the study were modified versions of real diagnostic problems, and thus they possessed characteristics quite similar to the documented action plans implemented by customers and judged to be effective in solving the problem. For a problem task, a subject's decision accuracy was measured using a 7-point Likert-style scale with 1 indicating “no accuracy” and 7 a “great level of accuracy.” Total decision accuracy comprised the subject's decision accuracy for each problem task.

## Confidence ratings

After completing the task scenario, the programmers in the experimental group were asked to rate their level of confidence in the accuracy of the ES recommendations for problem solution, the lines-of-reasoning, and their final decision for an action plan. The scale used was 7-point Likert-style, with 1 indicating “no confidence” and 7 indicating “utmost confidence.”

## User satisfaction

The final dependent variable was user satisfaction with the ES. For the purpose of this study, a two-part satisfaction questionnaire was used. The first part was a modified version of the Schultz and Slevin (1975) questionnaire for user satisfaction, measuring the perceived effect of the ES on (1) the programmers' job performance and performance visibility; (2) change in the organizational structure and decision environment; and (3) the urgency for performance results even if costs are involved. The second part of the questionnaire measured user satisfaction with specific functions and capabilities of the ES.

## Data collection procedure

Sixty-six programmers participated using the ES. Twenty-four solved the same problems without the help of the ES. All employees participating in the study were given the skill level questionnaire and the warm-up problem task. The programmers in the experimental group were instructed to complete the System and Program Abend tasks using the ES. The researcher read aloud the problem tasks with the employees to ensure they understood them and that any questions the subject had were answered. The order of presentation of the two scenarios was reversed for every consecutive programmer. Programmers were told they were being timed, with emphasis placed on making minimal errors yet working with high efficiency.

A control group was also studied to serve as a baseline measure to ensure that the ES was effective. The programmers in the control group were asked to solve the problem tasks using their current procedures and methods of handling customer calls. They were using an online database and reference manuals to examine the problem symptoms and determine a solution plan.

The order of the System Abend and Program Abend problems was reversed for each employee in the control group. These scenarios were identical to the ones used with the experimental group. Once again, the researcher read aloud the problem tasks with the employees to ensure they understood them and that any questions the subject had were answered. Each scenario required the employee to arrive at an action plan for problem solution to be presented to the customer. A timer began when the employee took the first step in the procedure for problem solution.

## Results

Two different models of analysis of variance (ANOVA) were required to analyze the data from the study. One ANOVA included only the 66 subjects in the experimental group (i.e., those who had worked on the problems with the help of the ES). In the analyses performed on these data, skill level (experienced versus inexperienced) was a between-subject variable. Problem type (high versus low uncertainty), knowledge presentation format (procedural versus declarative), and type of question (abstract knowledge required versus concrete knowledge) were within-subject variables.

The second ANOVA model was used to examine the data from both the experimental group and the control group. Once again, skill level was a between-subject variable because both groups included experienced and inexperienced employees, and problem type was a within-subject variable. In addition, because the control group did not work on the ES, system use was a between-subject variable. Comparisons of the control and experimental groups did not include the knowledge presentation format and question-type variables because the control group was not presented with the ES questions and explanations. The significant main effects and interaction effects of the ANOVA analyses, along with the means for the timing and accuracy data, are summarized in Tables 2 and 3, respectively. In addition to the hypothesized effects, which are indicated by their respective numbers, several other significant findings are reported in the tables.

## User performance

## Impact of Task Uncertainty and Skill Level

A review of the literature indicates that experts in a particular area internalize more knowledge about problem characteristics and construct a more coherent representation of the structure underlying a task than lower-skill problem solvers (Bhaskar and Simon, 1977; Greeno, 1977; Karat, 1982). The results of this study support this contention and are similar to previous research findings (Chi, et al., 1981; Lewis, 1983) on expert-novice differences in problem representation. For example, the expert and novice computer programmers used in this study performed quite similarly to the expert-novice chess players studied by Chase and Simon (1973) and electronic technicians observed by Egan and Schwartz (1979). This similarity suggests that the programmers studied were not idiosyncratic and that applicability of the findings can be extended beyond the context of this study.

As postulated, high-skill employees, whether using the system or not, outperformed low-skill employees on the same task. This finding lends support to the belief that much of expert power lies in the expert's ability to establish correspondence quickly between externally presented information and internal models for this information (Chi, et al., 1981).

The research results show a significant relationship between level of expertise and problem-solving performance. Intricately tied to this relationship is task uncertainty. As postulated, when faced with tasks with varying levels of uncertainty associated with problem parameters, different-skill users required different knowledge presentation formats that paralleled their conceptual representation of the problem. The results showed that both high- and low-skill employees performed the lower uncertainty task, System Abend, faster and more accurately that the higher

Table 2a. Significant Main Effects for Impact of Task Uncertainty and Skill Level on Programmers' Performance

<table><tr><td>Independent Variable</td><td>Dependent Variable</td><td>Level of Significance</td><td>Results</td></tr><tr><td>Task Uncertainty (H3)</td><td>Time to Query System Lines-of-Reasoning</td><td>F(1,62)=35.19,p&lt;.0001</td><td>Employees spent more time querying the lines-of-reasoning for the Program Abend (M=6.24) than for the System Abend (M=5.18).</td></tr><tr><td>Skill Level</td><td>Problem Solution Time</td><td>F(1,86)=10.91,p&lt;.0012</td><td>High-skill users (M=25.81) solved the System Abend and Progam Abend faster than low-skill users (M=48.23).</td></tr><tr><td>Task Uncertainty</td><td>Problem Solution Time</td><td>F(1,86)=6.99,p&lt;.0273</td><td>Employees solved the System Abend (M=25.69) faster than the Program Abend (M=38.25).</td></tr><tr><td>Expert System Usage</td><td>Problem Solution Time</td><td>F(1,86)=219.11,p&lt;.0001</td><td>Employees solved the System Abend and Pro-gram Abend tasks faster using the system (M=27.88) than not using it (M=50.20).</td></tr><tr><td>Skill Level (H4)</td><td>Solution Accuracy</td><td>F(1,86)=45.34,p&lt;.0001</td><td>High-skill employees (M=4.17) made fewer errors in solving the System Abend and Program Abend tasks than did low-skill employees (M=7.02).</td></tr><tr><td>Expert System Usage</td><td>Solution Accuracy</td><td>F(1,86)=11.19,p&lt;.001</td><td>Employees solved the System Abend and Pro-gram Abend tasks more accurately using the system (M=4.28) than not using it (M=6.28).</td></tr><tr><td>Task Uncertainty</td><td>Solution Accuracy</td><td>F(1,86)=54.45,p&lt;.0001</td><td>Employees made fewer errors on the System Abend (M=4.04) compared to the Program Abend (M=7.09).</td></tr><tr><td>Skill Level</td><td>Decision Time</td><td>F(1,86)=133.71,p&lt;.0001</td><td>High-skill employees (M=6.25) had faster deci-sion times for the System Abend and Program Abend tasks than did low-skill employees (M=10.71).</td></tr><tr><td>Expert System Usage</td><td>Decision Time</td><td>F(1,86)=34.89,p&lt;.0001</td><td>Employees made faster decisions using the system (M=5.51) than not using it (M=8.19).</td></tr><tr><td>Skill Level (H4)</td><td>Decision Accuracy</td><td>F(1,86)=6.86,p&lt;.0110</td><td>High-skill employees (M=6.19) made more ac-curate decisions than did low-skill employees (M=5.53) for the System Abend and Program Abend tasks.</td></tr><tr><td>Expert System Usage</td><td>Decision Accuracy</td><td>F(1,86)=7.89,p&lt;.001</td><td>Employees made more accurate decisions for the System Abend and Program Abend using the system (M=5.88) than not using it (M=3.94).</td></tr></table>

1. Problem Solution Time and Decision Time are reported in minutes  
2. Time to Query System Lines-of-Reasoning is reported in minutes  
3. Question Response Time is reported in seconds  
4. Problem Solution Accuracy is measured by:
- Total number of errors made on concrete and abstract questions when using the system
- Number of incorrect steps in solving each task when not using the system  
5. Decision Accuracy is measured by expert ratings  
6. Question Response Accuracy is measured for each user by:  
- Total number of errors made for concrete questions  
• Total number of errors made for abstract questions

Table 2b. Significant Main Effects for Impact of Knowledge Presentation Format on Expert System Users' Performance

<table><tr><td>Independent Variable</td><td>Dependent Variable</td><td>Level of Significance</td><td>Results</td></tr><tr><td>Skill Level</td><td>Time to Query System Lines-of-Reasoning</td><td>F(1,62) = 19.45, p &lt; .0001</td><td>Hlgh-skill users (M = 5.31) spent less time querying procedurally formatted lines-of-reasoning for the System Abend and Pro-gam Abend tasks than did low-skill users (M = 6.82).</td></tr></table>

Table 2c. Significant Main Effects for Impact of Knowledge Organization on High- and Low-Skill Users' Performance

<table><tr><td>Independent Variable</td><td>Dependent Variable</td><td>Level of Significance</td><td>Results</td></tr><tr><td>Task Uncertainty (H10)</td><td>Question Response Time</td><td> $F(1,62)=49.24$ , p&lt;.0001</td><td>Employees answered System Abend questions (M=17.21) faster than Program Abend questions (M=25.16).</td></tr><tr><td>Skill Level</td><td>Question Response Time</td><td> $F(1,62)=47.71$ , p&lt;.0001</td><td>High-skill users (M=17.15) answered questions for the System Abend and Program Abend tasks faster than low-skill users (M=24.89).</td></tr><tr><td>Task Uncertainty (H10)</td><td>Question Accuracy</td><td> $F(1,62)=170.34$ , p&lt;.0001</td><td>Employees made fewer errors on the System Abend questions (M=1.72) than the Program Abend questions (M=3.49).</td></tr><tr><td>Skill Level</td><td>Question Accuracy</td><td> $F(1,62)=156.60$ , p&lt;.0001</td><td>High-skill users (M=1.69) made fewer errors on System Abend and Program Abend questions than did low-skill users (M=3.98).</td></tr></table>

uncertainty task, Program Abend. $^{6}$ In addition, high- and low-skill employees' decision time and accuracy were significantly better for the System Abend than for the Program Abend. $^{7}$ Tables 4 and 5 show examples of the raw timing and accuracy data collected for low- and high-skill users participating in the study.

Also, use of the system had a greater impact on low- than on high-skill employees' performance. For both problem tasks, problem solution and decision time decreased and accuracy increased a greater amount for low- than for high-skill users when using the ES. The system provided low-skill users with a structured route to procedurally solve a problem. However, these results alone do not address the question of why the ES aided problem-solving performance. Answers to this question were sought by examining performance differences in answering system questions.

Table 3a. Significant Interaction Effects for Impact of Task Uncertainty and Skill Level on Programmers' Performance

<table><tr><td>Independent Variable</td><td>Independent Variable</td><td>Dependent Variable</td><td>Level of Significance</td><td>Results</td></tr><tr><td>Task Uncertainty (H1)</td><td>Expert System Usage</td><td>Problem Solution Time</td><td> $F(1,86)=14.99$ ,  $p<.0110$ </td><td>Employees were faster at solving the System Abend ( $M=22.13$ ) than the Program Abend ( $M=33.63$ ) when using the system compared to not using it.</td></tr><tr><td>Skill Level</td><td>Expert System Usage</td><td>Problem Solution Time</td><td> $F(1,86)=3.90$ ,  $p<.0498$ </td><td>Low-skill employees&#x27; solution time ( $M=17.57$ ) decreased a greater amount than high-skill employees&#x27; time ( $M=9.98$ ) when using the system compared to not using it.</td></tr><tr><td>Task Uncertainty (H1)</td><td>Expert System Usage</td><td>Solution Accuracy</td><td> $F(1,86)=44.45$ ,  $p<.0001$ </td><td>Employees were more accurate in solving the System Abend ( $M=4.04$ ) than the Program Abend ( $M=7.09$ ) when using the system compared to not using it.</td></tr><tr><td>Task Uncertainty (H2)</td><td>Expert System Usage</td><td>Decision Time</td><td> $F(1,86)=99.89$ ,  $p<.0001$ </td><td>Employees made faster decisions for an action plan for the System Abend ( $M=5.63$ ) than the Program Abend ( $M=11.42$ ) when using the system compared to not using it.</td></tr><tr><td>Skill Level</td><td>Expert System Usage</td><td>Decision Time</td><td> $F(1,86)=34.89$ ,  $p<.0001$ </td><td>Low-skill employees&#x27; ( $M=6.70$ ) decision time decreased a greater amount than did high-skill employees&#x27; ( $M=2.87$ ) when using the system compared to not using it.</td></tr><tr><td>Task Uncertainty (H2)</td><td>Expert System Usage</td><td>Decision Accuracy</td><td> $F(1,86)=11.96$ ,  $p<.001$ </td><td>Employees had a higher accuracy rating for the System Abend ( $M=6.29$ ) than the Program Abend ( $M=5.02$ ) when using the system compared to not using it.</td></tr><tr><td>Skill Level</td><td>Expert System Usage</td><td>Decision Accuracy</td><td> $F(1,86)=71.96$ ,  $p<.0001$ </td><td>Low-skill employees&#x27; ( $M=1.58$ ) decision accuracy improved a greater amount than did high-skill employees&#x27; ( $M=1.16$ ) when using the system compared to not using it.</td></tr></table>

Table 3b. Significant Interaction Effects for Impact of Knowledge Presentation Format on Expert System Users' Performance

<table><tr><td>Independent Variable</td><td>Independent Variable</td><td>Dependent Variable</td><td>Level of Significance</td><td>Results</td></tr><tr><td>Skill Level (H5)</td><td>Knowledge Presentation Format</td><td>Question Accuracy</td><td> $F(1,62)=51.70$ , p&lt;.0001</td><td>Low-skill users (M=2.17) made fewer errors than did high-skill users (M=3.91) on declaratively formatted questions.</td></tr><tr><td>Skill Level (H6)</td><td>Knowledge Presentation Format</td><td>Question Response Time</td><td> $F(1,62)=131.28$ , p&lt;.0001</td><td>For the Program Abend, high-skill users (M=22.97) answered declaratively formatted questions faster than did low-skill users (M=46.74).</td></tr><tr><td>Skill Level (H6)</td><td>Knowledge Presentation Format</td><td>Question Response Time</td><td> $F(1,62)=2.03$ , p&lt;.0500</td><td>For the System Abend, low-skill users (M=27.77) answered declaratively formatted questions faster than did low-skill users (M=29.50).</td></tr></table>

Table 3c. Significant Interaction Effects for Impact of Knowledge Organization on High- and Low-Skill Users' Performance

<table><tr><td>Independent Variable</td><td>Independent Variable</td><td>Dependent Variable</td><td>Level of Significance</td><td>Results</td></tr><tr><td>Question Type (H7)</td><td>Skill Level</td><td>Question Response Time</td><td>F(1,62)=55.47,p&lt;.0001</td><td>Low-skill users answered concrete questions (M=11.91) faster than abstract questions (M=37.89).</td></tr><tr><td>Question Type (H8)</td><td>Skill Level</td><td>Question Response Time</td><td>F(1,62)=55.47,p&lt;.0001</td><td>High-skill users answered abstract questions (M=15.08) faster than concrete questions (M=19.22).</td></tr><tr><td>Question Type (H7)</td><td>Skill Level</td><td>Question Accuracy</td><td>F(1,86)=55.17,p&lt;.001</td><td>Low-skill users made more errors on abstract questions (M=5.26) than concrete questions (M=2.70).</td></tr><tr><td>Question Type (H9)</td><td>Skill Level</td><td>Question Accuracy</td><td>F(1,62)=2.17,p&lt;.0500</td><td>High-skill users tended to make more errors on concrete questions (M=1.83) than abstract questions (M=1.59).</td></tr></table>

Table 4. Example of Raw Data for System Abend

<table><tr><td rowspan="2"></td><td colspan="2">Timing</td></tr><tr><td>High Skill</td><td>Low Skill</td></tr><tr><td colspan="3">Question</td></tr><tr><td colspan="3">Concrete</td></tr><tr><td>1.</td><td>32.17 secs.</td><td>15.16 secs.</td></tr><tr><td>2.</td><td>37.19</td><td>22.00</td></tr><tr><td>3.</td><td>34.19</td><td>32.14</td></tr><tr><td>4.</td><td>41.18</td><td>20.17</td></tr><tr><td>5.</td><td>40.29</td><td>28.29</td></tr><tr><td>6.</td><td>39.18</td><td>31.15</td></tr><tr><td>7.</td><td>39.00</td><td>39.17</td></tr><tr><td>8.</td><td>41.16</td><td>22.18</td></tr><tr><td>9.</td><td>42.10</td><td>18.19</td></tr><tr><td>10.</td><td>38.06</td><td>22.14</td></tr><tr><td>Number of Errors</td><td>0</td><td>2</td></tr><tr><td colspan="3">Abstract</td></tr><tr><td>11.</td><td>10.00 secs.</td><td>41.21 secs.</td></tr><tr><td>12.</td><td>15.16</td><td>37.27</td></tr><tr><td>13.</td><td>13.10</td><td>42.18</td></tr><tr><td>14.</td><td>12.11</td><td>44.17</td></tr><tr><td>15.</td><td>15.17</td><td>34.38</td></tr><tr><td>16.</td><td>21.00</td><td>40.00</td></tr><tr><td>17.</td><td>11.00</td><td>35.02</td></tr><tr><td>18.</td><td>20.08</td><td>40.07</td></tr><tr><td>19.</td><td>17.18</td><td>44.15</td></tr><tr><td>20.</td><td>21.12</td><td>42.00</td></tr><tr><td>Number of Errors</td><td>1</td><td>4</td></tr><tr><td>System Lines-of-Reasoning/Recommendations</td><td>5.30 mins.</td><td>6.42 mins.</td></tr><tr><td>Total Consultation-System Abend</td><td>21.48 mins.</td><td>31.29 mins.</td></tr><tr><td>Decision</td><td>4.59 mins.</td><td>9.20 mins.</td></tr><tr><td>Decision Accuracy Rating (1-7)</td><td>7</td><td>5</td></tr><tr><td colspan="3">Note: The data reported here is just a sample of two subjects&#x27; timing and accuracy measurements for the System Abend problem.</td></tr></table>

Table 5. Example of Raw Data for Program Abend

<table><tr><td rowspan="2"></td><td colspan="2">Timing</td></tr><tr><td>High Skill</td><td>Low Skill</td></tr><tr><td colspan="3">Question</td></tr><tr><td colspan="3">Concrete</td></tr><tr><td>1.</td><td>42.11 secs.</td><td>35.01 secs.</td></tr><tr><td>2.</td><td>40.16</td><td>32.16</td></tr><tr><td>3.</td><td>41.54</td><td>43.17</td></tr><tr><td>4.</td><td>41.00</td><td>30.19</td></tr><tr><td>5.</td><td>39.48</td><td>31.11</td></tr><tr><td>6.</td><td>46.00</td><td>29.16</td></tr><tr><td>7.</td><td>43.10</td><td>43.14</td></tr><tr><td>8.</td><td>44.17</td><td>38.17</td></tr><tr><td>9.</td><td>44.26</td><td>31.25</td></tr><tr><td>10.</td><td>48.09</td><td>31.33</td></tr><tr><td>Number of Errors</td><td>2</td><td>4</td></tr><tr><td colspan="3">Abstract</td></tr><tr><td>11.</td><td>25.34 secs.</td><td>52.18 secs.</td></tr><tr><td>12.</td><td>21.17</td><td>46.07</td></tr><tr><td>13.</td><td>26.91</td><td>40.00</td></tr><tr><td>14.</td><td>20.24</td><td>59.12</td></tr><tr><td>15.</td><td>22.93</td><td>58.31</td></tr><tr><td>16.</td><td>26.66</td><td>54.16</td></tr><tr><td>17.</td><td>20.48</td><td>52.01</td></tr><tr><td>18.</td><td>26.17</td><td>56.00</td></tr><tr><td>19.</td><td>27.10</td><td>44.16</td></tr><tr><td>20.</td><td>20.16</td><td>45.71</td></tr><tr><td>Number of Errors</td><td>3</td><td>6</td></tr><tr><td>System Lines-of-Reasoning/Recommendations</td><td>6.25 mins.</td><td>8.45 mins.</td></tr><tr><td>Total Consultation-System Abend</td><td>30.48 mins.</td><td>45.59 mins.</td></tr><tr><td>Decision</td><td>6.49 mins.</td><td>11.02 mins.</td></tr><tr><td>Decision Accuracy Rating (1-7)</td><td>6.3</td><td>4</td></tr><tr><td colspan="3">Note: The data reported here is just a sample of two subjects&#x27; timing and accuracy measurements for the Program Abend problem.</td></tr></table>

## Impact of Procedural vs. Declarative Knowledge Presentation Format

Performance differences found to be related to the task uncertainty variable support the proposition that ES explanation facilities need to be designed to provide users with the necessary information processing support as required by task characteristics. Adding another level of complexity to design requirements is the finding that certain presentation formats may be more conducive to users with differing expertise. An ANOVA model also was used to compare question response time, accuracy, and query time as a function of skill level and task uncertainty for procedural versus declarative knowledge presentation formats. The results show that for the higher uncertainty task, response time and accuracy for questions with declaratively formatted explanations (as compared to procedural explanations) were better for high-skill users. However, for the lower uncertainty taks, low-skill users performed equally fast and more accurately than high-skill users when presented with declarative explanations to questions.

The results also show that high- and low-skill users queried the system longer and in greater depth for procedural lines-of-reasoning for the higher uncertainty task. Also, the results show that when presented with essentially the same amount and depth of knowledge, high- as well as low-skill users felt more confident with procedurally formatted lines-of-reasoning for the lower uncertainty task.

Procedurally formatted lines-of-reasoning seem to offer an advantage in explicitly presenting knowledge about processes used in strategies for problem solution. The procedural presentation provides users with a coherent linkage of the interrelationships among the problem elements. In solving a problem characterized by higher uncertainty, employees' knowledge about strategies may be limited to only a subset of the available strategies; whereas, a problem-task with lower uncertainty has fewer separate elements that need to be identified and fewer exceptions that have to be dealt with. Consequently, the ability of a procedural presentation to show explicitly how facts can be used to determine other facts in reasoning is more straightforward when there is less ambiguity. This condition provides employees with more aid for strategy selection.

## Impact of Abstract vs. Concrete Knowledge Organization

This research supports the conclusion that high- and low-skill employees organize their conceptual knowledge about a problem differently. The performance differences resulting in a cross-over interaction provide striking support for the apparent differences in the conceptual representations of employees varying in skill level. Low-skill employees performed significantly faster and more accurately when answering questions requiring concrete knowledge organization. High-skill employees performed faster, although not necessarily more accurately, when responding to questions requiring abstract versus concrete knowledge organization. $^{8}$ Tables 4 and 5 show examples of the raw timing data for the questions displayed during the System Abend and Program Abend consultations.

The main effect found for skill level would suggest that, overall, high-skill employees were both faster and more accurate than low-skill employees in answering concrete and abstract questions. However, as can be seen in Table 3, high-skill employees were not faster than low-skill employees on questions that required concrete knowledge. In fact, for both problem tasks, high-skill employees were slower in this condition than low-skill employees (t(65) = 10.11, p < .0001; t(65) = 11.12, p < .0001, respectively). Error rates for high- and low-skill employees were approximately the same for questions requiring concrete knowledge. The bulk of this main effect appears to be in the difference between the two skill levels in answering questions requiring abstract knowledge. There was no significant main effect for type of question. $^{9}$

These results are among the first in studying he impact of question type on user performance. Based on these findings, it appears that certain knowledge organization formats are more conducive to high- versus low-skill employees' performance. Also, the results indicate that for both high- and low-skill users, faster response times were not associated with a larger number of errors made on questions. Thus, there was no apparent trade-off between speed and accuracy (Pachella, 1974).

The results show that high-skill employees actually performed worse than low-skill employees when answering concrete questions. Only a few previous studies (e.g., Adelson, 1984) have obtained similar results with subjects engaged in programming tasks. The results of the study presented here extend Adelson's findings in the domain of diagnostic problem solving using information (i.e., questions) generated through the ES heuristics. It seems unlikely that the high-skill users forgot the problem-specific terminology or jargon that was represented in concrete questions because there was no significant difference in accuracy between question types. A more plausible explanation is that the high-skill users internalized knowledge about the underlying problem structure and were able to work more efficiently (i.e., faster) when presented with questions requiring abstract as compared to concrete information organization. This does not mean that they forgot the lower-level details of a problem. The verbal protocols collected during the task analysis indicated that the high-skill programmers extracted problem-specific details as accurately as did the low-skill ones (Lamberti, 1987). They proceeded to use these details as necessary cues to generate a correct problem solution plan.

## User confidence

An ANOVA was used to compare subject-reported confidence ratings in the ES recommendations, lines-of-reasoning, and question explanations as a function of skill level and task uncertainty. Overall, the ANOVA results, as shown in Table 6, confirmed hypothesis H11, indicating significant main effects for skill level and task uncertainty.

In addition, a Pearson product-moment correlation was performed to assess the relationship between employee confidence ratings in the recommendation, lines-of-reasoning, and the employees' final decision for an action plan and the time it took to make a final decision for the problem solution. As expected, the results show that confidence is tied to decision performance. The correlation coefficient showed a strong negative correlation between confidence ratings and decision speed. As the confidence ratings for a system recommendation, lines-of-reasoning, and final decision increased, final decision time for an action plan decreased. $^{10}$

## User satisfaction

In an effort to assess user satisfaction, subjects were asked to rate their general attitudes toward using an ES to assist with their work, as well as their satisfaction with interface features. As shown in Table 6, analysis of satisfaction ratings confirmed hypothesis H12, which states that low-skill users will have higher satisfaction ratings than high-skill users for the declaratively formatted questions.

Satisfaction with knowledge presentation format appears to be a critical factor affecting user confidence in decisions for problem solution. Ratings of satisfaction with procedural lines-of-reasoning were positively related to confidence ratings in a decision for an action plan. The more confident users were about their decision, the higher were their satisfaction ratings for procedural lines-of-reasoning. Overall, high-skill users were more satisfied and more confident in their decisions than low-skill users. Most of the previous empirical research has not found any significant relationships between confidence and user satisfaction. Yet the issue of confidence is critical to system usage (Lehner and Zirk, 1987; Swartout, 1981). Thus, there is a need for more extensive empirical research to further evaluate the impact of employee satisfaction with expert systems on their confidence in decisions aided by these systems.

Table 6. Confidence and Satisfaction Ratings in Expert System and Decision for Action Plan

<table><tr><td colspan="3">Significant Findings</td></tr><tr><td rowspan="2">Dependent Variables</td><td>Skill Level</td><td>Task Uncertainty</td></tr><tr><td>High Low</td><td>High Low</td></tr><tr><td rowspan="2">Recommendations</td><td>C/M = 5.70 C/M = 3.64F = 120.52 (p &lt; .0001)</td><td>C/M = 3.86 C/M = 5.47F = 194.35 (p &lt; .0001)</td></tr><tr><td>S/M = 3.79 S/M = 3.86F = .92 (p &lt; .714)</td><td>S/M = 1.82 S/M = 3.76F = 7.56 (p &lt; .0068)</td></tr><tr><td rowspan="2">Lines-of-Reasoning</td><td>C/M = 5.55 C/M = 3.36F = 210.08 (p &lt; .0001)</td><td>C/M = 3.62 C/M = 5.29F = 172.89 (p &lt; .0001)</td></tr><tr><td>S/M = 4.68 S/M = 2.16F = 681.07 (p &lt; .0001)</td><td>S/M = 3.79 S/M = 5.67F = 108.19 (p &lt; .0001)</td></tr><tr><td rowspan="2">Question Explanations</td><td>C/M = 2.00 C/M = 4.00F = 291.10 (p &lt; .0001)</td><td>C/M = 3.92 C/M = 5.28F = 72.10 (p &lt; .001)</td></tr><tr><td>S/M = 1.76 S/M = 4.52F = 498.10 (p &lt; .0001)</td><td>S/M = 2.72 S/M = 4.95F = 211.19 (p &lt; .0001)</td></tr><tr><td rowspan="2">Decision for Action Plan</td><td>C/M = 4.19 C/M = 2.16F = 576.12 (p &lt; .0001)</td><td>C/M = 4.39 C/M = 5.95F = 139.79 (p &lt; .0001)</td></tr><tr><td>- -</td><td>- -</td></tr><tr><td rowspan="2">Urgency of System Implementation</td><td>- -</td><td>- -</td></tr><tr><td>S/M = 2.36 S/M = 3.93F = 58.12 (p &lt; .001)</td><td>- -</td></tr><tr><td rowspan="2">Enhance Job Performance</td><td>- -</td><td>- -</td></tr><tr><td>S/M = 3.87 S/M = 4.13F = 3.34 (p &lt; .0524)</td><td>- -</td></tr><tr><td rowspan="2">System as Change Agent</td><td>- -</td><td>- -</td></tr><tr><td>S/M = 2.35 S/M = 3.86F = 62.94 (p &lt; .001)</td><td>- -</td></tr></table>

C/M = Mean Confidence Rating S/M = Mean Satisfaction Rating

A strong main effect for skill level was found for employee attitudes toward urgency of system implementation and the system as a change agent. Low-skill employees perceived that (1) there is a greater need (urgency) to implement the ES within the department; and (2) it will have a greater effect as a change agent on the organizational structure and decision environment. Also, there was a trend indicating a difference between high- and low-skill employees' attitudes with respect to the system's impact on job performance, with low-skill employees perceiving that the ES will have a more positive impact on their job performance and performance visibility. Overall, the low-skill users had more favorable attitudes toward the ES on all dimensions.

## Discussion

This study identified and empirically investigated the role of several variables in the design of interfaces for intelligent systems and their impact on users' decision performance. In doing so, it has helped alleviate the dearth of empirical research dealing with human-computer interaction issues as they relate to ES design.

One objective of this study was to examine whether performance improvements could be made when using an ES. Similarly, the impact of task uncertainty on performance was evaluated. In studying these issues, emphasis was placed on how the format and organization of information presented on an ES interface affected problem-solving performance. Although a good deal of insight has been gained providing theoretical and practical guidelines for the design of interfaces for intelligent systems, any conclusions are contingent on how generalizable the research results are. Thus, a few factors possibly influencing this study are discussed prior to the implications of the results.

## Generalizability

As a result of system design, the ordering of concrete/abstract questions was not randomized. Consequently, for both problem-tasks, the majority of the abstract questions were presented at the latter part of the consultation. However, this factor is not likely to totally explain employee performance. A strong cross-over interaction between skill level and question type was found, whereas question ordering is more likely to account for a main effect for question type. Yet, future research is needed to investigate the effects of varying abstract/concrete question ordering.

Due to the nature of the system design, the question explanations and lines-of-reasoning were not presented in both a procedural and a declarative format. Rather, all question explanations were presented declaratively because they highlighted knowledge about static facts. Multi-step reasoning strategies employed by the system, stated as lines-of-reasoning, were presented procedurally. In future work, the same information should be presented in both a declarative and a procedural format in order to gain more insight into how these presentation formats affect the performance of users with different skill levels. It can be speculated that, as expertise develops, repeated viewing of the same information item from two complementary formats would aid in controlling the development and evaluation of alternative lines-of-reasoning needed for complex problem solving.

Also, as noted in the literature review, the terms abstract/concrete may not be the best labels to use in capturing a user's conceptualization of a problem. The concept of abstract information needs to be tested by further research to determine how it can be better operationalized. However, the results of this study confirm conceptual differences in problem representation between high- and low-skill employees, causing a significant interaction between skill level and knowledge organization.

A question arises of whether there were hidden factors, other than skill level, that could possibly influence user performance on the ES. For example, perhaps there was an inherent difference between high- and low-skill employees based on general intelligence (I.Q.s). Such differences, although plausible, seem unlikely. Employees were trained in the same methods for problem determination and solution. As the demographic information indicates, the employees can be considered relatively homogeneous.

Although diagnostic programmers were used as subjects in this research, the findings do not seem to be idiosyncratic to this group. The programmers performed quite similarly to expert-novice subjects studied in the areas of chess, electronics, systems design, and medicine (Atwood, 1980; Chase and Simon, 1973; Egan and Schwartz, 1979; Johnson, et al., 1981). Also, the variables examined in this research are critical to the design of ES in any domain. Whether the ES is narrowly defined or more generalized, a user still faces a problem-solving situation. Differences may exist in the scope of problem- and decision-making boundaries. Yet attention still must be given to how to best match the format and organization of knowledge presented in ES with the qualitative and quantitative differences in users' problem representations and solution strategies. In consideration of these factors, it seems plausible to assume that the research questions and results of this study can be generalized beyond computer professionals using a specific ES implementation to other domains and user groups.

## Implications for intelligent interface requirements

Mere technological feasibility of ES applications must be augmented by empirical study of whether, and how, users will find this new technology useful. From an organizational perspective, it is pointless to build these systems without giving appropriate consideration to behavioral requirements for their usability.

Although it is difficult to make broad generalizations from a single study focusing on a particular field setting, the significant issues raised by this study can be synthesized with other research findings (e.g., Ghani, 1981; Lewis, 1983; Zmud, 1979) to arrive at an empirically based understanding of the key design variables. Several suggestions can be offered for enhancing the advisory capability of intelligent systems.

Although the ability to explain reasoning, referred to as an explanation facility, is usually considered one of the most powerful components of ES, it is an area that has not been adequately explored. As Carroll and McKendree (1987) state, “lack of empirical research carefully examining this issue increasingly is being identified as a key reason for the limited impact of ES technology” (p. 15). An explanation facility is useful on several levels: (1) the decision maker is aided in formulating problems and models for analysis; (2) it can assure the sophisticated user that the system’s knowledge and reasoning process is appropriate; and (3) it can instruct the novice user about the knowledge in the system as it is applied to solve a particular problem.

In developing explanation facilities, a question arises as to what constitutes knowledge requirements. What information does the explanation facility have to “know” about? How much information does it have to “know”? These issues need to be considered at the beginning of the system design process. They exemplify the potential impact of interface design on system construction. The findings of this research raise a number of general propositions for performance enhancement through knowledge presentation in ES:

\- Consideration must be given to human information processing limitations (Goslar, et al., 1986). The complexity of explanation structures (e.g., embedded lines-of-reasoning) must be geared to match these processing limitations. The explanation should present the appropriate level of structure of the problem by explicitly showing the implicit constraints and problem boundaries to better explain what the system is doing and why it is doing it.

\- When the user intervenes, the explanation presented should be tailored specifically to the conceptual representation required by the current question. Explanation facilities need to present information specific to abstract knowledge requirements in addition to concrete requirements.

\- Information presented for a specific question should be based on an evaluation of prior question explanations. The emphasis should be on integrating abstract and concrete details in related questions.

\- To increase user confidence in system reasoning, explanations of questions and recommendations should include reasons why alternative recommendations were not chosen. It is just as important to explain why certain problem solutions were not suggested as to explain why others were presented.

\- Questions should be presented in a way that helps explain causal relationships between multiple or associated problem types. The representation can reinforce the development of knowledge of common associations between specific problem types.

\- Critical cues associated with problem symptoms should be explicitly stated in questions in order to support the formalization of procedures required to solve a problem.

\- Interface design must consider a novice user's learning process, where he or she acquires more qualitative knowledge and gradually a more abstract working representation of problems. Thus, it may be more appropriate to design the system dialogue with a balance between concrete and abstract representations.

As Swartout (1981) states, once the content of an explanation has been determined, there is the question of how to convey this knowledge to the user. To achieve effective knowledge presentation, it is essential to use good rhetoric to make the explanation understandable (Aldag and Power, 1986). In evaluating system intelligibility, it is often claimed that representing more domain knowledge is a key to better explanation or advice-giving systems (Stevens, et al., 1982; Van Lehn, 1981). The question that must be addressed is what amount of knowledge, at how fine a grain of detail, can be adequately presented to support the problem solver's decision process when using the system? The answer to this question deals partly with the skill level of the problem solver. Also, task ambiguity places constraints and/or requirements on the need to present detailed knowledge in the knowledge base as well as in explanation facilities.

The results of this study indicate that when procedurally formatted lines-of-reasoning, presenting a finer grain of detail than declarative explanations, were presented to the users, there was a difference in high- versus low-skill user confidence, satisfaction, and the amount of time spend reviewing the lines-of-reasoning. The explanation facility must be able to present knowledge about questions at a variety of levels of detail for problems differing in uncertainty. For example, the explanations of broad questions about a fairly structured, high certainty problem should not be presented at the lowest level of detail. To make this possible, the code should reflect a top-down decomposition of the behavior of the system. This will make it possible for the explanation facility to select the appropriate level of decomposition to present explanations for each individual question. Clearly, more empirical research needs to look specifically at the impact of different depths of knowledge on users' performance. It should be noted that the ES investigated in this study has been successfully implemented. In an effort to obtain feedback on system usage and effectiveness, informal observation of users has been conducted. Results of these observations have been consistent with the findings reported in this study, i.e., speed and accuracy continue to improve over a range of problem types.

## Future research issues

The results of this study have practical implications for understanding the role of intelligent interfaces in knowledge-based systems. Undoubtedly, the technology needs to be designed taking the human problem solver into consideration. The way an individual solves a problem is influenced by the way knowledge about a problem is presented to him or her, as well as what problem-solving tools are made available. To explore more fully the role of ES as decision support tools, the following important research questions regarding ES design need to be tested in future work.

How can the user interface enhance a problem solver's ability to think about a problem and solve it? The concepts and images though which decision makers understand the environment are strongly conditioned by presentational schemes. Different presentational formats may impact ES users' performance, and, in fact, may cause changes in their approaches to problem solving. Identification and documentation of the effects of presentation schemes should be continuing goals of research. In considering cognitive compatibility between the user and the ES, researchers should focus on two related issues: (1) the best way to capture expertise and its abstractness for supporting skill development of novices; and (2) questions requiring concrete knowledge organization should be organized to create abstract representations in novice users.

Secondly, how can an ES exploit the user interface to communicate problem-solving knowledge to a user in order to influence decision outcomes? To effectively answer this question, more research is needed to develop models that validly and reliably capture expert reasoning processes. Researchers must ask questions about how and why ESs influence decision outcomes (Todd and Benbasat, 1987). The key is to understand the link between internal knowledge representation and its external presentation. If ESs are to be responsible for providing helpful advice, it is vital that there be compatibility between the representation and control structures employed by both the system and the user. Lehner and Zirk (1987) argue that the user must have a good mental model of ES problem solving. This does not mean that the system should follow a psychological model that exactly imitates a user's reasoning process. It does mean, however, that the presentation format chosen must be able to communicate the process that the ES follows in its problem-sovling activity. This argument emphasizes that an accurate mental model of system processing leads to improved user performance and higher confidence in the system's reasoning, even if there is a low degree of consistency between the user's problem-solving procedures and those of the system.

Similarly, can the incorporation of both procedural and declarative knowledge as one unified package improve user performance? One way to do this would be to present a set of declarative facts in one level of an explanation and then use embedded (procedural) explanations to structure facts in various configurations. In this way, less-skilled users could selectively view explanations at the appropriate level of detail, and higher-skilled users would be able to bypass the declarative explanations and focus on the procedural description if they desired to do so. Additional research should examine the impact of multiple representations of the same knowledge using procedural and declarative formatting.

Can the use of graphical displays to show conceptual relations that are interdependent (e.g., either in a network or hierarchy) among problem types improve user performance? In this interface, a problem initially can be viewed at an abstract level and then refined to successively lower levels of detail. An interface combining a question dialogue with a graphical presentation of paths of relations among problem parameters may be an effective technique to provide additional information about the structure of solution plans. User confidence in system recommendations may be enhanced by graphical links representing logical relationships between problem information, which better convey the structure of planning needed for problem solution, which may enhance user confidence in system recommendations. The use of direct manipulation graphics also permits the user to take a more active role in constructing a solution through the connection of icons and data, making the flow of control more explicit.

Finally, can rule-based systems use the same representation of knowledge in different ways (e.g., to solve problems, provide explanations, generate examples, offer advice)? An intelligent interface using the same set of rules to provide these capabilities is critical for integrating ES with decision support technology. This requirement raises the issue of interface independence—the extent to which the interface is immune from modifications to the internal knowledge-base representation and inferencing component. The concept is similar to that of data independence, which has become a cornerstone for database management applications. Decision support systems are capable of modifying not only the display of a problem but also its underlying structure. As Zachary (1986) points out, in more complex tasks a wide variety of model-based or knowledge-based inferences, predictions, and evaluations are possible. One interface should be able to access a variety of models within the system to provide support for problem solution across several domains. This type of design would enhance user performance by lessening the cognitive processing required to generate strategies for computationally intensive problem solving. It would also serve to increase interface flexibility, system efficiency, and maintainability.

The aforementioned research topics are by no means an exhaustive list. The need for innovative intelligent systems will continue to evolve, providing a challenge for researchers and designers to develop sophisticated and technologically feasible interfaces needed to support complex decision making. This study extends the findings of previous research and, in doing so, lays the ground work for future studies examining the effective utilization of ES.

## References

Adelson, B. “Problem Solving the the Development of Abstract Categories in Programming Languages,” Memory & Cognition (9:4), July 1981, pp. 422-433.

Adelson, B. “When Novices Surpass Experts: The Difficulty of a Task May Increase With Expertise,” Journal of Experimental Psychology:

Learning, Memory and Cognition (10:3), 1984, pp. 483-495.

Alavi, M. and Napier, H.A. “An Experiment in Applying the Adaptive Design Approach to DSS Development,” in Decision Support Systems: Putting Theory Into Practice, R.H. Sprague, Jr. and H.J. Watson (eds.), Prentice-Hall, Englewood Cliffs, NJ, 1986, pp. 65-75.

Aldag, R.J. and Power, D.J. “An Empirical Assessment of Computer-Assisted Decision Analysis,” Decision Sciences (17:4), Fall 1986, pp. 572-588.

Anderson, J.R. “Acquisition of Cognitive Skill,” Psychological Review (89:4), July 1982, pp. 369-406.

Atwood, M. Expert and Novice Systems Designers, SAI, Boulder, CO, 1980.

Benbasat, I. and Dexter, A.S. “An Investigation of the Effectiveness of Color and Graphical Information Presentation Under Varying Time Constraints,” MIS Quarterly (10:1), March 1986, pp. 59-83.

Benbasat, I. and Schroeder, R.G. “An Experimental Investigation of Some MIS Design Variables,” MIS Quarterly (1:1), March 1977, pp. 37-49.

Benbasat, I. and Taylor, R. "Behavioral Aspects of Information Processing for the Design of Management Information Systems," IEEE Journal of Systems, Man, and Cybernetics (12:4), July-August 1982, pp. 439-450.

Bennett, J.L. “Integrating Users and Decision Support Systems,” in Proceedings of the Sixth Annual Conference, Society for Management Information Systems, J.D. White (ed.), San Fransisco, CA, September 11-13, 1974, pp. 77-86.

Bhaskar, R. and Simon, H.A. "Problem Solving in Semantically Rich Domains," Cognitive Science (1:2), April 1977, pp. 193-215.

Bosman, A. and Sol, H.G. “Knowledge Representation and Information Systems Design,” in Knowledge Representation for Decision Support Systems, L.B. Methlie and R.H. Sprague, Jr. (eds.), North-Holland, Amsterdam, 1985, pp. 81-91.

Buchanan, B.G. and Shortliffe, E.H. Rule-Based Expert Systems - The MYCIN Experiments of the Stanford Heuristic Programming Project, Addison-Wesley, Reading, MA, 1985, pp. 83, 312.

Carroll, J.M. and McKendree, J. "Interface Design Issues for Advice-Giving Expert Systems," Communications of the ACM (30:1),

January 1987, pp. 14-31.

Chase, W.C. and Simon, H.A. “Perception in Chess,” Cognitive Psychology (4:1), January 1973, pp. 55-81.

Chi, M.T.H., Feltovich, P.J. and Glaser, R. "Categorization and Representation of Physics Problems by Experts and Novices," Cognitive Science (5:1), January-March 1981, pp. 121-152.

Clancey, W.J., Shortliffe, E.H. and Buchanan, B.G. “Intelligent Computer-Aided Instruction for Medical Diagnosis,” Proceedings of the Third Annual Symposium on Computer Applications in Medical Care, Washington, DC, October 14-17, 1979, pp. 175-183.

Coombs, M. and Alty, J. “Face-to-Face Guidance of University Computer Users-II: Characterizing Advisory Interactions,” International Journal of Man-Machine Studies (12:4), May 1980, pp. 407-429.

Daft, R.L. and Macintosh, N.S. “A Tentative Exploration into the Amount and Equivocality of Information Processing in Organizational Work Units,” Administrative Science Quarterly (26:2), June 1981, pp. 207-224.

de Groot, A.D. Thought and Choice in Chess, Mouton, Paris, 1965.

DeSanctis, G. "Computer Graphics as Decision Aids: Directions for Research," Decision Sciences (15:4), Fall 1984, pp. 463-487.

Dos Santos, B.L. and Bariff, M.L. "A Study of User Interface Aids for Model-Oriented Decision Support Systems," Management Science (34:4), 1988, pp. 461-468.

Dreyfus, H.L. and Dreyfus, S.E. Mind Over Machine - The Power of Human Intuition and Expertise in the Era of the Computer, The Free Press, New York, NY, 1986.

Egan, D.E. and Schwartz, B.J. “Chunking in Recall of Symbolic Drawings,” Memory & Cognition (7:2), March 1979, pp. 149-158.

Fox, M.S. “Knowledge Representation for Decision Support,” in Knowledge Representation for Decision Support Systems, L.B. Methlie and R.H. Sprague, Jr. (eds.), North-Holland, Amsterdam, 1985, pp. 3-26.

Galbraith, J.R. Organization Design, Addison-Wesley, Reading, MA, 1977, pp. 36-39.

Georgeff, M. "Procedural Control in Production Systems," Artificial Intelligence (18:2), March 1982, pp. 175-201.

Ghani, J.A. The Effects of Information Representation and Modification on Decision Performance, unpublished Ph.D. dissertation,

University of Pennsylvania, Philadelphia, PA, 1981.

Goslar, M.D., Green, G.I. and Hughes, T.H. "Decision Support Systems: An Empirical Assessment for Decision Making," Decision Sciences (17:1), Winter 1986, pp. 79-91.

Greeno, J.G. “Process of Understanding,” in Cognitive Theory—Volume 2, N.J. Castellan, D.B. Pisoni and G.R. Potts (eds.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1977, pp. 43-84.

Hayes-Roth, F., Waterman, D.A. and Lenat, D.B. Building Expert Systems, Addison-Wesley, Reading, MA, 1983.

Hurst, G.E. “The Role of Humans in Decision Support Systems,” working paper, 78-02-01, Department of Decision Sciences, University of Pennsylvania, Philadelphia, PA, 1978.

IBM Corporation. Expert System Consultation Environment/VM and Expert System Development Environment/VM, IPS Service Support Center, Irving, TX, 1987.

Jarvenpaa, S.L. “The Effect of Task Demands and Graphical Format on Information Processing Strategies,” Department of Management Science and Information Systems, College and Graduate School of Business Administration, University of Texas, Austin, TX, May 1988.

Johnson, P., Duran, A., Hassebrock, F., Moller, J. and Prietula, M. “Expertise and Error in Diagnostic Reasoning,” Cognitive Science (5:1), January-March 1981, pp. 235-283.

Karat, J. “A Model of Problem Solving with Incomplete Constraint Knowledge,” Cognitive Psychology (14:4), October 1982, pp. 538-559.

Keller, L.R. “Effects of Problem Representation on the Sure-Thing and Substitution Principles,” Management Science (31:6), June 1985, pp. 738-751.

Lamberti, D.M. Intelligent Systems Design: The Development of a Framework and Empirical Assessment of Knowledge Presentation and Reasoning in an Expert System Interface, unpublished doctoral dissertation, Rensselaer Polytechnic Institute, Troy, NY, 1987.

Lehner, P.E. and Zirk, D.A. “Cognitive Factors in User/Expert-System Interaction,” Human Factors (29:1), 1987, pp. 97-109.

Lewis, J.W. "An Effective Graphics User Interface for Rules and Inference Mechanisms," in Proceedings of CHI '83, Human Factors in Computing Systems, December 12-15, Boston, MA, 1983, pp. 139-143.

Luconi, F.L., Malone, T.W. and Scott Morton,

M.S. “Expert Systems: The Next Challenge for Managers,” Sloan Management Review (27:4), Summer 1986, pp. 7-14.

Lusk, E.J. and Kersnick, M. “Effects of Cognitive Style and Report Format on Task Performance: The MIS Design Consequences,” Management Science (25:8), August 1979, pp. 787-798.

Neter, J. and Wasserman, W. Applied Linear Statistical Models, Richard D. Irwin, Inc., Homewood, IL, 1974.

Newell, A. and Simon, H.A. Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

Pachella, R.G. “The Interpretation of Reaction Time in Information-Processing Research,” in Human Information Processing: Tutorials in Performance and Cognition, B. Kantowitz (ed.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1974, pp. 41-82.

Pylyshyn, Z.W. “What the Mind’s Eye Tells the Mind’s Brain: A Critique of Mental Imagery,” Psychological Bulletin (80:1), July 1973, pp. 1-24.

Reddy, R. and Newell, A. “Knowledge and Its Representation in a Speech Understanding System,” in Knowledge and Cognition, L.W. Gregg (ed.), Lawrence Erlbaum Associates, Hillsdale, NJ, 1974, pp. 253-285.

Reitman, J.S. “Skilled Perception in GO: Deducing Memory Structures from Inter-Response Times,” Cognitive Psychology (8:3), July 1976, pp. 336-356.

Schank, R.C. and Abelson, R.P. Scripts, Plans, Goals, and Understanding, Lawrence Erlbaum Associates, Hillsdale, NJ, 1977, pp. 150-174.

Schor, M. “Declarative Knowledge Programming: Better Than Procedural?” IEEE Expert (1:1), Spring 1986, pp. 36-43.

Schultz, R.L. and Slevin, D.P. (eds.) Implementing Operations Research/Management Science, American Elsevier Publishing Company, Inc., New York, NY, 1975, pp. 173-177.

Sharda, R., Barr, S.H. and McDonnell, J.C. "Decision Support System Effectiveness: A Review and an Empirical Test," Management Science (34:2), February 1988, pp. 139-159.

Shortliffe, E.H. Computer-Based Medical Consultation: MYCIN, American Elsevier Publishing Company, Inc., New York, NY, 1976, pp. 20-23.

Simon, H.A. The New Science of Management Decision, Harper Brothers, New York, NY, 1960.

Sims, H.P., Szilagyi, A.D. and Keller, R.T. "The Measurement of Job Characteristics," Academy of Management Journal (19:2), June 1976, pp. 195-212.

Smith, G.F. "Towards a Heuristic Theory of Problem Structuring," Management Science (34:12), December 1988, pp. 1489-1506.

Stefik, M., Aikins, J., Balzer, R., Benoit, J., Birnbaum, L., Hayes-Roth, R. and Sacerdoti, E. "The Organization of Expert Systems," Artificial Intelligence (18:2), March 1982, pp. 135-173.

Stevens, A., Collins, A. and Goldin, S.E. "Misconception in Students' Understanding," in Intelligent Tutoring Systems, D. Sleeman and J.S. Brown (eds.), Academic Press, New York, NY, 1982, pp. 13-24.

Stohr, E. and White, N. “User Interfaces to Decision Support Systems: An Overview,” International Journal of Policy Analysis and Information Systems (6:4), December 1982, pp. 393-423.

Swartout, W.R. “Explaining and Justifying Expert Consulting Programs,” Proceedings of the Seventh International Joint Conference on AI, Vancouver, British Columbia, August 24-28, 1981, pp. 815-822.

Todd, P. and Benbasat, I. “Process Tracing Methods in Decision Support Systems Research: Exploring the Black Box,” MIS Quarterly (11:4), December 1987, pp. 493-512.

Turban, E. and Watkins, P.R. “Integrating Expert Systems and Decision Support Systems,” MIS Quarterly (10:2), June 1986, pp. 121-136.

Tushman, N.L. “Task Uncertainty and Subunit Communication Structure,” Proceedings of the Academy of Management, August 1978, pp. 190-194.

Tushman, N.L. “Impacts of Perceived Environmental Variability on Patterns of Work Related Communications,” Academy of Management Journal (22:3), September 1979, pp. 482-500.

Van de Ven, A.H. and Delbecq, A.L. "A Task Contingent Model of Work-Unit Structure," Administrative Science Quarterly (19:2), June 1974, pp. 183-197,

Van Lehn, D. Bugs Are Not Enough: Empirical Studies of Bugs, Impasses, and Repairs in Procedural Skills, Xerox PARC Technical Report, Palo Alto, CA, 1981.

Vessey, I. "Expertise in Debugging Computer Programs: A Process Analysis," International Journal of Man-Machine Studies (23:5),

November 1985, pp. 459-494.

Vitalari, N. and Schenk, K. “An Examination of the Cognitive Limits of Novice Systems Analysts,” working paper, Graduate School of Management, University of California, Irvine, CA, 1989.

Wiedenbeck, S. “Novice/Expert Differences in Programming Skills,” International Journal of Man-Machine Studies (23:4), October 1985, pp. 383-390.

Winograd, T. Understanding Natural Language, Academic Press, New York, NY, 1972.

Withey, M., Daft, R.L. and Cooper, W.H. "Measures of Perrow's Work Unit Technology: An Empirical Assessment and a New Scale," Academy of Management Journal (26:1), March 1983, pp. 45-63.

Zachary, W. "A Cognitively Based Functional Taxonomy of Decision Support Techniques," Human-Computer Interaction (2), 1986, pp. 25-36.

Zmud, R.W. “Individual Differences and MIS Success: A Review of the Empirical Literature,” Management Science (25:10), October 1979, pp. 966-979.

## About the Authors

Donna M. Lamberti is a research staff member in AI and information systems at the IBM Cambridge Scientific Center, Cambridge, MA. She received a B.A. degree in experimental psychology from Vassar College, Poughkeepsie, NY, in 1982, and an M.S. degree in cognitive psychology, as well as a Ph.D. in management information systems/decision sciences from Rensselaer Polytechnic Institute, Troy, NY, in 1987. Her thesis research was on the development and empirical evaluation of an intelligent interface for a diagnostic expert system. This work was sponsored by an IBM Fellowship for research in information systems. Her current research interests include intelligent interface design for decision support technology, the design of AI-based advisory systems for organizations, and the implementation of decision support/knowledge-based systems.

William A. Wallace is professor of decision sciences and engineering systems at Rensselaer Polytechnic Institute. He received a B.Ch.E. from Illinois Institute of Technology and an M.S. and Ph.D. in management science from Rensselaer Polytechnic Institute. As a researcher and consultant in management science and information systems, Professor Wallace has over 15 years' experience in developing, implementing, and evaluating decision support systems for industry and government. He has authored or co-authored four books and over 90 articles and papers. He has held academic positions at Carnegie Mellon University and State University of New York at

Albany. He was a visiting faculty member at the National Center for Industrial Science and Technology Management Development in Dalian, People's Republic of China, and implemented the first micro computer-based educational facility in the country. He is currently engaged in research and development of computer-based decision aids using expert systems technology.

## Appendix A System Abend and Program Abend Questions

## Concrete Questions

S1. What features are installed with the base? (Choose any number of the following)  
\_\_\_\_ PSFK  
\_\_\_\_ DISSOS  
\_\_\_\_ BJK  
\_\_\_\_ HOST

S5. Communication attachments:
DPA (Local) \_\_\_\_ Yes \_\_\_\_ No
DAL (Loop) \_\_\_\_ Yes \_\_\_\_ No \_\_\_\_ How many?
DLA (Link) \_\_\_\_ Yes \_\_\_\_ No \_\_\_\_ How many?

S8. What type of dump is available?
(Choose any number of the following):
\_\_\_\_ SADUMP
\_\_\_\_ FP ABEND Dump

P3. Enter the number of the most recent fix package installed on a failing system. (e.g., Fix Package 39 = '39')

P7. It might also be helpful to know the previous fix package level (if we want to know which PTFs are actually new to the system). Enter that number if you have it.

P8. What documentation do you have available for working on this problem? (Choose any number of the following):
\_\_\_\_ SADUMP
\_\_\_\_ FP Abend Dump
\_\_\_\_ Traces
\_\_\_\_ Documents
\_\_\_\_ Data Management Services
\_\_\_\_ Configuration Services
\_\_\_\_ Hardware Diagnostic Output
\_\_\_\_ Program Listing
\_\_\_\_ Procedures
\_\_\_\_ Performance Monitor
\_\_\_\_ None of the above

## Abstract Questions

S11. What is the likelihood that the problem has occurred before? The likelihood of hardware errors causing a problem generally goes down as the number of failing systems increases.
\_\_\_\_ Systems(s)

S13. You were previously given a recommendation to do a maintenance IPL. Which of the following describes the results you encountered?

Logon device was up and user was at enter command

\_\_\_\_ IPL seemed to complete successfully but no devices came up

\_\_\_\_ User does not know loop/PND adapter/terminal/host address

\_\_\_\_ IPL was interrupted by a BOP message

S14. Identify and record any additional terminal messages associated with this problem. If you choose to pursue these messages, you must determine the weighting of each and enter the one with the highest weighting.

P.15 I can give you help with problems in the categories listed below. If you wish, you may select one of these major symptoms. Otherwise, if you are not sure, use the PF6 to bypass the selection, and I will try to figure it out. (Choose one of the following:)

Problem Determination

\_\_\_\_ System Abend

\_\_\_\_ Program Abend

\_\_\_\_ System Wait

\_\_\_\_ System Loop

P16. This is the Program Abend Processor. You have arrived here because of the Abend message. Before proceeding, be certain there were no I/O errors for the operator experiencing the Abend or affecting that operator's terminal communications. If so, you should use the appropriate problem determination techniques because I/O errors have probably caused the problem.

P20. Check your data. There is a discrepancy with regard to items reported in the message and supplied from the Abend dump.

Message Data ABEND Dump Data

If only the program locations differ, we will pursue the dump. Otherwise you will get to choose. If you want to change an entry, use the UNDO command (try PF1 for help with UNDO).

## Appendix B

## Mean Ratings and Correlations for System Abend and Program Abend Questions

Program Abend

<table><tr><td>Concrete Questions</td><td>Mean Expert Ratings</td><td>Mean User Ratings</td><td>Correlation</td></tr><tr><td>#P1</td><td>1.4</td><td>1.7</td><td>.83</td></tr><tr><td>#P2</td><td>1.6</td><td>1.3</td><td>.83</td></tr><tr><td>#P3</td><td>1.5</td><td>1.3</td><td>.86</td></tr><tr><td>#P4</td><td>1.0</td><td>1.6</td><td>.75</td></tr><tr><td>#P5</td><td>1.4</td><td>1.7</td><td>.83</td></tr><tr><td>#P6</td><td>1.0</td><td>1.6</td><td>.75</td></tr><tr><td>#P7</td><td>1.0</td><td>1.5</td><td>.78</td></tr><tr><td>#P8</td><td>1.6</td><td>1.0</td><td>.75</td></tr><tr><td>#P9</td><td>1.6</td><td>1.3</td><td>.83</td></tr><tr><td>#P10</td><td>1.8</td><td>1.5</td><td>.83</td></tr><tr><td>Abstract Questions</td><td>Mean Expert Ratings</td><td>Mean User Ratings</td><td>Correlation</td></tr><tr><td>#P11</td><td>4.2</td><td>4.7</td><td>.76</td></tr><tr><td>#P12</td><td>4.0</td><td>4.5</td><td>.77</td></tr><tr><td>#P13</td><td>4.0</td><td>4.3</td><td>.83</td></tr><tr><td>#P14</td><td>4.2</td><td>4.8</td><td>.75</td></tr><tr><td>#P15</td><td>4.6</td><td>4.3</td><td>.83</td></tr><tr><td>#P16</td><td>4.6</td><td>4.0</td><td>.75</td></tr><tr><td>#P17</td><td>4.4</td><td>4.0</td><td>.78</td></tr><tr><td>#P18</td><td>4.2</td><td>4.8</td><td>.75</td></tr><tr><td>#P19</td><td>4.2</td><td>4.7</td><td>.76</td></tr><tr><td>#P20</td><td>4.8</td><td>4.0</td><td>.60</td></tr></table>

System Abend

<table><tr><td>Concrete Questions</td><td>Mean Expert Ratings</td><td>Mean User Ratings</td><td>Correlation</td></tr><tr><td>#S1</td><td>1.4</td><td>1.7</td><td>.83</td></tr><tr><td>#S2</td><td>1.6</td><td>1.3</td><td>.83</td></tr><tr><td>#S3</td><td>1.5</td><td>1.3</td><td>.86</td></tr><tr><td>#S4</td><td>1.0</td><td>1.6</td><td>.75</td></tr><tr><td>#S5</td><td>1.4</td><td>1.7</td><td>.83</td></tr><tr><td>#S6</td><td>1.0</td><td>1.7</td><td>.65</td></tr><tr><td>#S7</td><td>1.0</td><td>1.3</td><td>.81</td></tr><tr><td>#S8</td><td>1.6</td><td>1.2</td><td>.78</td></tr><tr><td>#S9</td><td>2.0</td><td>1.6</td><td>.78</td></tr><tr><td>#S10</td><td>2.0</td><td>1.8</td><td>.86</td></tr><tr><td>Abstract Questions</td><td>Mean Expert Ratings</td><td>Mean User Ratings</td><td>Correlation</td></tr><tr><td>#S11</td><td>4.2</td><td>4.4</td><td>.86</td></tr><tr><td>#S12</td><td>4.0</td><td>4.0</td><td>1.00</td></tr><tr><td>#S13</td><td>4.0</td><td>4.2</td><td>.86</td></tr><tr><td>#S14</td><td>4.6</td><td>4.5</td><td>.92</td></tr><tr><td>#S15</td><td>4.4</td><td>4.3</td><td>.92</td></tr><tr><td>#S16</td><td>4.0</td><td>4.3</td><td>.83</td></tr><tr><td>#S17</td><td>4.2</td><td>4.8</td><td>.75</td></tr><tr><td>#S18</td><td>4.6</td><td>4.2</td><td>.78</td></tr><tr><td>#S19</td><td>4.6</td><td>4.4</td><td>.86</td></tr><tr><td>#S20</td><td>4.8</td><td>4.5</td><td>.83</td></tr></table>
