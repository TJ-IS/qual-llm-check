---
otero_id: 22442
otero_key: "5R643YGN"
title: "A graph-based approach for rule integrity and maintainability in expert system maintenance"
authors: "Kunihiko Higa; Ho Geun Lee"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00037-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A graph-based approach for rule integrity and maintainability in expert system maintenance

Kunihiko Higa $^{a,*}$ , Ho Geun Lee $^{1,b}$

$^{a}$ Department of Industrial Engineering and Management, Tokyo Institute of Technology, O-okayama, Meguro-ku, Tokyo 152-8552, Japan $^{b}$ Department of Business Administration, Yonsei University, Seoul, South Korea

Received 27 January 1997; accepted 21 December 1997

## Abstract

Just as conventional software systems have maintenance costs far exceeding development costs, so too do rule-based expert systems. They are frequently developed by an incremental and iterative method, where knowledge and decision rules are extracted and added to the system in a piecemeal manner throughout system evolution. Thus, ensuring the correctness and consistency of the rule base (RB) becomes an important, though challenging task. However, most research work in expert systems has focused on building and validating rule bases, leaving the maintenance issue unexplored. We propose a graph-based approach, called the object classification model (OCM), as a methodology for RB maintenance. An experiment was conducted to compare the OCM with traditional RB maintenance methods. The results show that the OCM helps knowledge engineers retain rule-base integrity and, thus, increase rule-base maintainability. © 1998 Elsevier Science B.V. All rights reserved

Keywords: Rule base; Knowledge base maintenance; Rule integrity; Rule maintainability; Graph-based method

## 1. Introduction

Software maintenance has become an important task because it accounts for a considerable amount of the time spent and life-cycle cost of a software system. For traditional software systems, maintenance costs exceed the development costs by a factor of between two and four $[6, 18]$ . There is no reason to assume that this should be any different for rule-based expert systems, provided that they have a reasonable operational life. Most expert-system developers adopt an evolutionary approach, where knowledge bases evolve in an iterative fashion through interactions between knowledge engineers and experts. Although there is merit to this approach (prototyping is an appropriate mechanism for extracting ill-specified and non-formalized expert knowledge), the inherently ad-hoc nature of this evolutionary approach can lead to unanticipated maintenance problems after the system is put into operation.

Evolutionary development implies that knowledge and decision rules are extracted and added to the system in a piecemeal manner throughout the system evolution. Thus, ensuring the correctness and consistency of the rule base (RB) becomes a challenging task. The difficulty is further magnified if expert systems are maintained by people who did not develop the initial system. Poor maintenance can result in a rule base that becomes too complex to manage. Based on an extensive survey of early expert systems, Gill [11] found that the high cost of on-going maintenance is one of the major factors that results in expert system failure.

Surprisingly, the problem of the maintenance of the RB is not well understood, although it has long been an issue. As the RB evolves, effort and resources have to be devoted to updating the system in order to keep the rules consistent and manageable. Unfortunately, there is no widely accepted methodology for the maintenance of RBs, thus making knowledge updates a challenging task. We propose a graph-based approach called the object classification model (OCM) as a methodology for maintaining RBs. This method uses graphical structures to provide visualization for interpreting information structure in the rule hierarchy. This paper reports on an experiment that compares RB maintenance using a traditional method with the use of OCM. Our hypothesis is that the OCM facilitates updates of knowledge by increasing consistency and maintainability of RBs.

## 2. Maintenance of the rule base

If expert systems deal with problems whose subject knowledge is destined to evolve, modifications to the knowledge base are inevitable during the life cycle of the system $[17, 20]$ . When the knowledge domain is volatile, the system designer may not, at least initially, possess an overall global picture of the knowledge that the system must contain and how it eventually will be structured in the RB. Several examples show that the cost of on-going maintenance of the RB often becomes too high and results in system failure. In Hewlett–Packard's IPT and Honeywell's PRESS, for example, the growth and dynamics of the task domain have made their on-going maintenance too costly to continue their services.

Digital's XCON configuration system also demonstrates the challenging nature of RB maintenance [3]. Since the system was put into operation in 1980, ca.

40% of its rules have changed each year. Digital offers several hundred major new products each year. Configuration information about them must be included in the rule base. Sometimes rules dealing with the configuration of existing products must be changed to incorporate additions. Also, existing products are repackaged, as directed by engineering, marketing, and government regulation. Once the XCON was viewed as a successful business support tool, users generated new requirements that enlarged its function and significantly changed the rules. As a result, the knowledge base of XCON had grown from 850 rules in 1980 to over 10 000 rules in 1988 [4].

Why is the maintenance of RB a non-trivial task? Updating it consists of rule additions, rule deletions, and rule modifications. When new knowledge is added, it will result in a new branch of the rule hierarchy. The antecedents and consequences of the new rule must be tied into the rest of the rules by establishing correct relations between them. Removal of a rule in the middle of a chain in the rule-base hierarchy necessitates knitting together the existing rules. All the rules that are supposed to call or be called by the removed rule must be examined to avoid undesired effects. Similarly, modification or replacement of existing rules, as a result of new conditions or relationships being created, requires significant examinations of its impact on the existing rule hierarchy, since the modification of a rule can be viewed as the process of removing one rule and introducing a new one.

## 3. Rule-base integrity and maintainability

A change in the existing knowledge base often leads to unanticipated rule anomalies. The maintenance operation may result in an inconsistency, as well as unstructured rules.

## 3.1. Integrity

Advice provided by an expert system should be consistent in the sense that the same states of the world must lead to the same set of inferences being made by the system. Conflicts, Dead-end-IF, and missing rules are addressed here as sources of the integrity problem.

## 3.1.1. Conflicting rules

If two (or more) rules have logically equivalent antecedents (or one subsumes the other) but conclude differently, they are in conflict. Situations where the same antecedent conditions lead to different conclusions have been variously labeled as logical conflict, ambiguity and so on [8]. Consider, for example, the following two rules:

$$
\begin{array}{l l} \text {Rule 1:} & \text {IF c_{1} AND c_{2} THEN g_{1}} \\ \text {Rule 2:} & \text {IF c_{1} AND c_{2} THEN g_{2}} \end{array}
$$

If the outcome $g_{1}$ and $g_{2}$ are mutually exclusive, then these two rules are clearly in conflict.

## 3.1.2. Dead-end-if

This rule type is defined as one that does not connect to a goal. A rule $R_{i}$ becomes Dead-end-IF when its conclusion $g_{i}$ is not used as a condition by any other rules although $g_{i}$ is not a final goal. Consider, for example, the following RB with three rules (only $g_{1}$ is a final goal):

$$
\begin{array}{l l} \text {Rule 1:} & \text {IF a_{1} THEN g_{1}} \\ \text {Rule 2:} & \text {IF c_{1} THEN a_{1}} \\ \text {Rule 3:} & \text {IF c_{2} THEN b_{1}} \end{array}
$$

Unlike Rule 2, whose consequent value is used to check the condition for the final goal, Rule 3 does not contribute to the goal $g_{1}$ ; thus, it is a Dead-end-IF.

## 3.1.3. Missing rules

A missing rule exists when an antecedent contains a literal, that is neither obtainable from a fact nor inferable from any other rule. Consider, for example, the rule:

$$
\text { Rule: } \quad c _ {1} \text {   AND   } c _ {2} \text {   THEN   } g _ {1}
$$

If the truth value of $c_{1}$ or $c_{2}$ (or both) cannot be determined from external sources (such as a database or user input), then the RB has at least one missing rule, whose consequence provides the antecedents $c_{1}$ and $c_{2}$ .

The presence of conflicting rules results in inconsistency of the RB, while the Dead-end-IF and the missing rules make the RB incomplete [2]. Gaps or inconsistency in the knowledge base can seriously impair system performance. It is obvious that conflicting rules might yield contradictory advice and, thus, must be avoided in the RB. If it is incomplete, there are certain legal combinations of parameters that are not contained in the antecedent of an existing rule (in the case of missing rules), or there are certain legal consequent values that are not linked to any final advice (in the case of Dead-end-IF). With an incomplete RB, expert systems will be unable to provide a satisfactory response, since the consultation with the system might result in ‘no conclusion.’

## 3.2. Maintainability

The maintainability of the RB is affected by any redundancy and instability of the rules. In contrast to integrity, such rules are logically sound but increase the potential of inconsistency in future. Thus, the RB maintainability problem can be tested by checking the existence of such rules. Redundancy in an RB is typically caused by the presence of subsumption or duplication of rules. An RB is unstable when a simple change to one rule increases the possibility of inconsistency in other rules.

## 3.2.1. Duplication

A rule $R_{i}$ is a duplicate of a rule $R_{j}$ , if $R_{i}$ has a logically equivalent antecedent part with $R_{j}$ and shares a common consequent value with $R_{j}$ . The duplicate rule can be removed without changing the set of conclusions asserted by the RB for any valid input. Duplication is a special case of subsumption.

## 3.2.2. Subsumption

Subsumption occurs when two rules have identical conclusions and the antecedent of one rule is a subset of that of the other rule. Consider, as an example, the following two rules:

$$
\begin{array}{l l} \text {Rule 1:} & \text {IF c_{1} AND c_{2} AND c_{3} THEN g_{1}} \\ \text {Rule 2:} & \text {IF c_{1} AND c_{2} THEN g_{1}} \end{array}
$$

Rule 2 subsumes the Rule 1, since the antecedents of the Rule 2 ( $c_{1}$ and $c_{2}$ ) logically dominate the antecedents of the Rule 1 ( $c_{1}$ , $c_{2}$ and $c_{3}$ ), and both rules share a common consequent value $g_{1}$ . Obviously, when the more restrictive Rule 1 succeeds, the general Rule 2 is also satisfied.

## 3.2.3. Adjacency

A rule $R_{i}$ is adjacent to a rule $R_{j}$ , if the antecedents of both rules are mutually exclusive and exhaustive, and both rules share a common consequent value. Consider the following two rules:

$$
\begin{array}{l l} \text {Rule 1:} & \text {IF a_{1} AND (c_{1} OR c_{2}) THEN g_{1}} \\ \text {Rule 2:} & \text {IF a_{1} AND (c_{3} OR c_{4}) THEN g_{1}} \end{array}
$$

If the union of the antecedents of the two rules $(c_{1}, c_{2}, c_{3}, c_{4})$ has no gap, that is, covers all the possible values of ‘C’ between $c_{1}$ and $c_{4}$ , these two rules are adjacent to each other. (Note: the “unnecessary IF condition” discussed in [23] is one type of adjacency).

Duplication, subsumption and adjacency do not normally affect the operation of an RB, unless the system estimates the level of confidence in its conclusions $[7]$ . While they may not necessarily provide logically incorrect advice, their presence will affect the performance of the system (its efficiency) $[19]$ . Such rule inconsistency can also result in update anomalies if one instant of a redundant rule is removed and another is not, or when one rule is altered while the other is left alone. Since their existence will complicate the maintenance of RB, it is generally desirable to remove them.

## 4. Related work

The rule-based system development process typically includes knowledge acquisition, representation, implementation, validation and maintenance. RB maintenance is not independent of other phases of the life cycle. It is highly dependent on the quality of the representation: good ones make RB much easier to understand and maintain. Knowledge maintenance also has obvious parallels with knowledge validation, since the defects that may result from maintenance can result from the initial construction of the rule base. However, validation addresses the entire rule base (the degree of correspondence between the expert advice and the system recommendation), while error checking associated with maintenance activities need only impinge on a part of the RB (internal verification such as logical correctness of the rules).

Several approaches to the verification of knowledge encapsulated in an expert system have been suggested. These approaches are designed to detect inconsistency, redundancy, missing rules, and conflicts in RBs. Completeness and consistency checking of a rule base have been addressed by Suwa et al. [24, [25] in their rule-checking program associated with the ONCOCIN expert system. The rule checker aids by automatically identifying redundancies, subsumptions, inconsistency at a local level, and missing rules. Nguyen [21] and Nguyen et al. [22] describe an automated rule verifier called CHECK that is able to detect global errors in the form of circular chains and to check redundancy, subsumption, and inconsistency at the local level.

A decision-table-based method for rule-base verification has been described by Cragun and Steudel. Their Expert System Checker program processes the entire knowledge base to examine each decision table to identify inconsistency, redundancy, completeness, and missing rules at the local level. Ginsberg $[12, 13]$ describes an approach to integrity checking called KB-Reduction that can detect all inconsistencies, redundancies, and potential contradictions in a knowledge base. Recently, Hicks $[14]$ proposed an approach called R4 Algorithm to ‘normalize’ decision-table relations in an attempt to remove anomalies in the RB.

Our approach to RB maintenance is different from these techniques. First, the OCM is designed for preventive maintenance rather than curative maintenance. Knowledge verification techniques take already established knowledge and detect errors and anomalies resident in the rules. We view the preventive approach to be as important as the curative one. Second, we are concerned with maintainability as well as integrity of the RBs. The advantages of writing readable and understandable codes are well known in traditional software maintenance. The graph-based approach helps knowledge engineers eliminate a-priori redundancy and subsumption, thus keeping RBs structured for easy change.

## 5. The object classification model

Here, a graphical model for knowledge representation called the object classification model (OCM) is defined as a tool for RB maintenance. The OCM is created on the basis of the structured object model (SOM) that was originally developed as an analysis, design, and query tool for database applications $[16]$ . The SOM itself is a derivative of the ‘system entity structure’ that was initially developed as a model representation scheme for simulation modeling $[26]$ .

<table><tr><td>Component</td><td>Representation</td></tr><tr><td>Object</td><td>Object_Name: text only</td></tr><tr><td>Attribute</td><td></td></tr><tr><td>Name</td><td>○ATTRIBUTE_Name: a circle with text</td></tr><tr><td>Value</td><td>Value: an attribute value underneath an arc</td></tr><tr><td>Relationship</td><td></td></tr><tr><td rowspan="2">Aspect</td><td>Object_A (or an attribute)</td></tr><tr><td>Object_B: an object underneath an arc</td></tr><tr><td rowspan="3">Categorization(Specification)</td><td>Object_A (or a value)</td></tr><tr><td>○ATTRIBUTE_X</td></tr><tr><td>value_y</td></tr><tr><td>Goal</td><td>↓Goal_Value: a value underneath an arrow</td></tr><tr><td>Connector</td><td>○A: a connector label inside a circle</td></tr></table>

Fig. 1. Components of OCM.

## 5.1. Components and constructs of OCM

The OCM represents data semantics using objects, attributes, and two types of relationships: aspects and specialization. An object is an event or an activity about which users wish to collect and store information. Attributes are used to describe objects by providing them with descriptive properties. Relationships represent associations among objects. Aspects describe owner–member relationships, while specialization expresses the classification/categorization relations of objects. The components of the OCM are summarized in Fig. 1 (refer to [15] for more detail).

Translating a set of rules into the OCM diagram is quite a simple mechanical process. Each rule becomes a path of the tree. Each attribute in the antecedent part of the rule becomes a classification (specification) of a path. Naturally, the consequence, or goal value, of a rule becomes the leaf. For example, “IF QC=G.P2 AND PUB<2 AND EXP<2 THEN RECOM is G” will be translated as the left-most path of the top tree in Fig. 2, which shows the OCM diagram translated from the RB used for the experiment in this paper. This process is completely automatable, since it requires no human interaction. The production rules, listed in

Appendix A, are designed to evaluate applicants to an international research institute and to determine their appropriate rank (G, P1 to P4) based on an applicant's age, education, past experience and foreign language fluency. In the OCM diagram, multiple classification leaving an object typically indicates a reasoning chain; for example, there are three classifications exiting from the root object (applicant), QC (rank qualification class), I\_Q (initial qualification) and AGE; therefore, the three sub-trees form a reasoning chain.

Although there are several systems that automatically check for logical completeness and consistency of a rule set, it is a good practice to check for these problems manually before using the system. It is generally known that manual tracing (including the structured walk through) reduces the cost of programming. Similarly, a manual check of the knowledge structure will reduce the cost of knowledge-base development.

The proposed OCM is similar to a decision tree. However, a normal decision tree cannot be used for designing and maintaining rule bases because it has no distinction between aspects and specialization of objects.

![](/api/attachments/5R643YGN/fulltext/images/017f417c2efafc4fa39dea7faa2377ebdc026d3303f53b364bc2d1f0f28fa68f.jpg)  
Fig. 2. The experiment rule set OCM.

## 6. Experiment

The essence of the OCM method is that it uses graphs to represent and maintain the RB.

## 6.1. Research hypotheses

Assuming that a required modification to the RB is semantically correct, the effectiveness of RB maintenance can be measured by the correctness of any modification and ease of future maintenance. The following three hypotheses were tested in a controlled laboratory experiment with MBA students as subjects.

Between the traditional approach and the OCM in modifying the rule set:

H1: Subjects perform significantly better using the OCM.

H2: Subjects produce significantly fewer unreliable rules using the OCM.

H3: Subjects make significantly fewer ill-structured rules using the OCM.

These three hypotheses test the positive effect of using the OCM diagram on the maintenance of the RB. For H2, rules with characteristics that cause an integrity problem (conflicting rules, Dead-end-IF and missing rules) are considered to be unreliable. Similarly for H3, rules with characteristics that cause maintainability problem (duplication, subsumption and adjacency) are considered ill-structured.

It is unrealistic to assume that a typical RB consists only of simple structures. Therefore, for this experiment, a rule set that contained 33 rules with some complex structures was used. The experiment required the insertion of three new rules; for each insertion, the addition affects the existing complex rule structure. Thus, each insertion required modification of more than one existing rule in the set, and the maintenance task was non-trivial.

## 6.2. Experiment design

## 6.2.1. Independent variables

Two approaches to RB maintenance, traditional and graph-based (using OCM), were used. The traditional approach relies solely on the skill of a knowledge engineer, while the graph-based approach uses the

OCM to help the knowledge engineer maintain the RB.

## 6.2.2. Dependent variables

Integrity and maintainability of rules after maintenance are used as dependent variables. Since logical correctness is the most important factor for maintenance, higher priority is given to the integrity variable than to the maintainability one. There are several correct solutions, and each was considered the same from a scoring standpoint.

## 6.2.3. Subjects

Forty-eight MBA students enrolled in the ‘Introduction of Expert Systems’ class were recruited and trained to perform RB modification tasks. Subjects had received limited credit for the course based on their performance in the modification tasks. The average age of the subjects was 28; they had an average work experience (full time) of 4.8 years and none had previous experience in the maintenance of RBs.

## 6.2.4. Procedure

The subjects were divided into two groups, 24 subjects per group, based on their age and work experience. As pre-test training, one lecture, one homework and one in-class exercise (both similar to the task in the experiment), each of 90-min duration, were given to the subjects one week before the experiment. For one group, the OCM diagram was taught and used throughout the pre-test training. Then, the subjects were asked to perform the RB modification task.

Prior to the experimental task, subjects were informed as follows:

\- There are three insertions of rules for the maintenance task, and there is no time limit for the task, though 30 min is suggested.

\- Subjects' performance (for their course credit) is strictly based on the correctness of the modification; the time taken is irrelevant to the evaluation of their performance.

The 30-min suggestion was based on the result from a pilot test.

The experiment was conducted as follows:

\- First, the two-page instruction was distributed to the subjects. This included requirements for modification, abbreviations used in the tasks, and domain definitions for the rule sets (see Appendix A and B). Similar instruction had been used in pre-test training.

Table 1
Evaluation criteria

<table><tr><td>Criteria</td><td>Evaluation</td></tr><tr><td>Incomplete insertion</td><td>A score of 0 was given if the insertion process was not completed</td></tr><tr><td>Logical inconsistency</td><td>A score of 0 was given if the insertion caused any logical inconsistency between rules. Number of conflicts (inconsistency between rules) and Dead-end-IF rules were also recorded for each subject</td></tr><tr><td>Incomplete domain coverage</td><td>A score of 0 was given if the insertion resulted in any incomplete domain coverage. Since each original rule set has complete domain coverage (all attribute and goal values are covered by the rule set), each incomplete coverage resulting from the insertion can be considered as a missing rule. Thus, the number of missing rules was also recorded for each subject</td></tr><tr><td>Ill-structured rule</td><td>0.5 point was taken off the score if the insertion created any adjacency, duplication and subsumption in the rule set. The original rule set contained some ill-structured rules. Therefore, only new ill-structured rules after the insertion was counted, and the number of ill-structured rules were recorded for each subject</td></tr></table>

\- The rule set and the task sheet were distributed to the subjects. They were not allowed to start until told to do so by performing the maintenance job for the rule set.

\- As soon as a subject completed the task, he or she brought the answer or the OCM diagram to the nearest proctor (there were four proctors in the room). The proctor then recorded the subject's completion time, and the subject was asked to leave the room.

## 6.2.5. Grading

A subject could score 3 points if the rule set was logically sound and contained no ill-structured rules after three insertions; that is, a score of 1 was given for each correct insertion. A score of 0 was given for an incorrect insertion that made the rule set unreliable (i.e., if the students' answer contained Dead-end-IF rules, conflicting rules, or missing rules). Ill-structured rules did not immediately make the set unreliable; however, they did make the set inefficient and expensive to maintain. Therefore, 0.5 point was taken off for each ill-structured rule created by the insertion. The detailed evaluation criteria are provided in Table 1.

## 6.3. Results

Six types of anomalies were actually created by the subjects: adjacent, duplicated, subsumed, Dead-end-

IF, conflicting, and missing rules. The first three types make the future RB maintenance difficult, and the latter three are logical errors and, thus, make the RB unreliable. Table 2 shows the total number of these anomalies made by the two groups.

There was no significant difference between the two groups in creating duplicated and subsumed rules (only two subjects in the OCM group and four subjects in the traditional group made these kinds of errors). Adjacent rules are easy to create but difficult to detect, and the result indicated that the OCM diagram helped the subjects to avoid creating adjacent rules. In terms of the number of reliability errors, the difference between the two groups was significant.

Ten out of twenty four subjects in the OCM group created no anomaly, while only three subjects in the traditional group did. This provides a general picture of the performance between the two groups in RB maintenance: subjects using the OCM perform better than the other group in all categories. The study has used a critical significance level, alpha of 0.05, for testing the differences in means of scores. All three hypotheses are supported with significance below this alpha level. The summary of the experimental results is provided in Table 3.

H1 tests the difference in overall quality of modification correctness between the traditional approach and the OCM approach. The OCM group performed much better than the traditional group. The difference was statistically significant $p=0.003$ .

The difference for unreliable rules in modifying the rule set by the two groups is tested in H2. Three types of unreliable rules (conflicting, Dead-end-IF, and missing) were actually produced by all the subjects.

Table 2  
Number of rule anomalies by two groups

<table><tr><td rowspan="2"></td><td colspan="4">OCM</td><td colspan="4">Traditional</td></tr><tr><td>(1)a</td><td>(2)b</td><td>(1)/(2)</td><td>(3)c</td><td>(1)a</td><td>(2)b</td><td>(1)/(2)</td><td>(3)c</td></tr><tr><td colspan="9">Maintainability</td></tr><tr><td>adjacent</td><td>6</td><td>6</td><td>1.0</td><td>25%</td><td>16</td><td>12</td><td>1.33</td><td>50%</td></tr><tr><td>duplicate</td><td>0</td><td>0</td><td>—</td><td>0%</td><td>1</td><td>1</td><td>1.0</td><td>4%</td></tr><tr><td>subsumed</td><td>2</td><td>2</td><td>1.0</td><td>8%</td><td>3</td><td>3</td><td>1.0</td><td>13%</td></tr><tr><td>Total</td><td>8</td><td>8</td><td>1.0</td><td>33%</td><td>20</td><td>15</td><td>1.33</td><td>63%</td></tr><tr><td colspan="9">Reliability</td></tr><tr><td>Dead-end-IF</td><td>0</td><td>0</td><td>—</td><td>0%</td><td>3</td><td>3</td><td>1.0</td><td>13%</td></tr><tr><td>conflict</td><td>11</td><td>6</td><td>1.833</td><td>25%</td><td>19</td><td>12</td><td>1.583</td><td>50%</td></tr><tr><td>missing</td><td>2</td><td>2</td><td>1.0</td><td>8%</td><td>14</td><td>9</td><td>1.556</td><td>38%</td></tr><tr><td>Total</td><td>13</td><td>8</td><td>1.625</td><td>33%</td><td>36</td><td>19</td><td>1.895</td><td>79%</td></tr></table>

$^{a}$ Number of errors.  
$^{b}$ Number of subjects who made errors;  
$^{c}$ Proportion of subjects who made errors.  
Table 3

Results of the study

<table><tr><td>Hypotheses</td><td>OCM (mean)</td><td>Traditional (mean)</td><td>Significant level</td><td>Hypothesis support</td></tr><tr><td>H1: OCM group performs better</td><td>2.33</td><td>1.625</td><td>0.003</td><td>Yes</td></tr><tr><td>H2: OCM group has less unreliable rules</td><td>0.54</td><td>1.500</td><td>0.005</td><td>Yes</td></tr><tr><td>H3: OCM group has less ill-structured rules</td><td>0.33</td><td>0.833</td><td>0.015</td><td>Yes</td></tr></table>

Because all three insertions were designed such that multiple rules had to be modified for each insertion, the potential for creating unreliable rules was high. In fact, 19 subjects in the traditional group (79% of the group) made 36 unreliable rules, as compared to eight subjects with 13 unreliable rules in the OCM group. The difference in score means between the two groups was statistically significant $p=0.005$ .

H3 tests the difference in the number of ill-structured rules in modifying the rule set. Using the OCM diagram, ill-structured rules (duplication, subsumption and adjacency) are easy to detect. As expected, only eight subjects made eight ill-structured rules in the OCM group. On the other hand, 15 subjects made 20 ill-structured rules in the traditional group. The difference in score means between the two groups was also statistically significant $p=0.015$ .

In this experiment, subjects in the OCM group were asked to draw their own OCM diagram based on the given rule set. Because of this arrangement, the OCM group took 10 min longer on average to complete the task. After the evaluation of the experiment results, we found that some incorrect modifications were caused by incorrectly drawn OCM diagrams. Thus, the number of rule anomalies of the OCM group could further be reduced if a machine-drawn OCM diagram were available. Because the drawing of an OCM diagram from a rule set can be automated, this will allow us to measure the effect of the OCM on RB maintenance more accurately. Nevertheless, the OCM group performed significantly better than the traditional group. The result of this experiment clearly validates the potential of the graph-based approach for RB maintenance.

## 7. Discussion

Although there is no widely accepted methodology for rule base maintenance, knowledge engineers generally agree that modularity is an important strategy to ease maintenance hurdles. In fact, the nature of the rule-based programming paradigm permits flexibility: new knowledge can be added without significantly impacting other parts of the program (the ‘modularity advantage’). Davis suggests, through a laboratory experiment, that modularity plays a significant role for RB maintenance [9]. However, modularity itself provides no well-defined techniques for documenting change in the RB [1].

The OCM method adopts a graph-based approach beyond modularity for RB maintenance. A variety of graphical techniques have already been used to describe and analyze several types of information processing systems; indeed visual graphs facilitate interpretation of information structure and semantics $[5]$ ; for example, data flow diagrams, data structure diagrams, and entity-relationship diagrams all help in the design of IS. In particular, the entity-relation approach, which has a graphical view of the relationships, has been widely used for database design.

Most people, if not all, perform better when things are pictorially associated. The graph-based approach transforms a large quantity of data and information into a visual form that allows users to perceive the meaning and relations of the information instead of using their cognitive powers to figure it out $[10]$ . This may explain why the OCM group performs better.

It should be noted, however, that the OCM method is more than just organizing information and relations in a visual form: the OCM method incorporates aspects and specializations of the objects into relational graphs, which are not available in a decision tree. This also contrasts with the Petri-Net approach, suggested by Agarwal and Tanniru for RB verification, since the Petri-Net does not allow for such descriptions as aspects and specialization of objects. Thus, the OCM method, if combined with the modularity advantages of the rule-based programming paradigm, can significantly enhance the RB maintenance performance of knowledge engineers.

## 8. Conclusion

The degree of maintainability of a software product is a function of its understandability and, consequently, its adaptability. This, in turn, is dependent on the software development techniques. Good techniques make software much easier to understand and maintain.

Much effort in expert-systems research has been focused on initial rule building or verifying established RBs, leaving its maintenance unexplored. This is partly because only a few well-documented systems have reached the maintenance phase. However, even these prove that the maintenance of RBs is not a simple matter; the system eventually requires an overhaul, and an extensive re-write for the maintenance unless it is equipped with a well-structured maintenance method. For instance, Digital's XCON has been re-implemented in a better maintenance environment called RIME.

RB maintenance is challenging when the expert systems are intended to support decision makers in organizations. Unlike conventional transaction systems, expert-systems developers in general adopt a prototyping methodology where new knowledge augments continuously during the system's evolution. The experiment in this study indicates that a graph-based approach increases the integrity as well as the maintainability of RBs. This preventive methodology should lead to better RB maintenance by complementing existing knowledge verification techniques.

## Appendix A

## Experiment rule set

This system evaluates applicants for a research institute and determines their appropriate rank (G, P1-4) for their qualifications.

## A.1. Rule set

r1: if AGE<25 then I\_Q=NQ

r2: if AGE>50 then I\_Q=NQ

r3: if 24<AGE<51 and LNG=1 then I\_Q=NQ

r4: if 24<AGE<51 and LNG>1 and DGREE=Others then I\_Q=NQ

r5: if 24<AGE<51 and LNG>1 and DGREE=H then I\_Q=LQ

r6: if 24<AGE<51 and LNG>1 and DGREE=A then I\_Q=LQ

r7: if 24<AGE<51 and LNG>1 and DGREE=B

r8: if 24<AGE<51 and LNG>1 and DGREE=M then I\_Q=HQ

r9: if 24<AGE<51 and LNG>1 and DGREE=P then I\_Q=HQ

r10: if I\_Q=NQ then RECOM=NA

r11: if I\_Q=LQ and DEGREE=H and AGE<36 then RECOM=G

r12: if I\_Q=LQ and DEGREE=H and AGE>35

r13: if I\_Q=LQ and DEGREE=A and AGE<36 then RECOM=G

r14: if I\_Q=LQ and DEGREE=A and AGE>35 then RECOM=NA

r15: if I\_Q=LQ and DEGREE=B and AGE<36 then QC=G.P2

r16: if I\_Q=LQ and DEGREE=B and AGE>35 then RECOM=NA

r17: if I\_Q=HQ and DEGREE=M and AGE<40 then QC=P2.P3

r18: if I\_Q=HQ and DEGREE=M and 39<AGE<46 then QC=P3.P4

r19: if I\_Q=HQ and DEGREE=M and AGE>45 then RECOM=NA

r20: if I\_Q=HQ and DEGREE=P and AGE<46 then QC=P3.P4

r21: if I\_Q=HQ and DEGREE=P and AGE>45 then RECOM=NA

r22: if QC=G.P2 and PUB<2 and EXP<2 then RECOM=G

r23: if QC=G.P2 and PUB<2 and EXP>1 then RECOM=P1

r24: if QC=G.P2 and PUB>1 and EXP<2 then RECOM=G

r25: if QC=G.P2 and PUB>1 and EXP>1 then RECOM=P2

r26: if QC=P2.P3 and EXP<3 then RECOM=P2

r27: if QC=P2.P3 and PUB>2 and EXP>2 then RECOM=P3

r28: if QC=P2.P3 and PUB<3 and EXP>2 then RECOM=P2

r29: if QC=P3.P4 EXP<5 then RECOM=NA

r30: if QC=P3.P4 and 4<EXP<7 and PUB<6 then RECOM=P3

r31: if QC=P3.P4 and 4<EXP<7 and PUB>5 then RECOM=P4

r32: if QC=P3.P4 and EXP>6 and PUB<7 then RECOM=P3

r33: if QC=P3.P4 and EXP>6 and PUB>6 then RECOM=P4

## A.2. Abbreviations

LNG number of languages
H high school
B Bachelor degree
M Master degree
P Ph.D.
EXP international work experience
PUB number of professional publications
I\_Q initial qualification
LQ low qualification
HQ high qualification
NQ not qualified
QC rank qualification class
G general rank
P1-4 professional I-IV level rank
RECOM final recommendation
NA no rank appropriate.

## A.3. Attribute domains

AGE=[0...100]: integer; LNG=[1...10]: integer; DEGREE={H, B, M, P, Others}; EXP=[0...25]: integer; PUB=[0...100]: integer; I\_Q={LQ, HQ, NQ}; QC={G.P1, P2.P3, P3.P4}; RECOM={G, P1, P2, P3, P4, NA}.

## Appendix B

## Experiment problem set

B.1. Rule modification problem

ID: \_\_\_\_ Name: \_\_\_\_

Requirements:

1. Assume that the rule set is complete and logically consistent. Then perform the given modifications on the rule set. For each modification, you must maintain the logical consistency and completeness of the rule set.

2. Always apply each modification to the original rule set, not to the modified set.

3. For each modification, do not touch any other rules except for those rules that are directly related to the modification.

4. For each modification, do not create any new duplicate, subsumption, overlap, and adjacent rules. If you find any such already existing rules, do not touch them unless they are directly related to the specified modification.

ID: \_\_\_\_

Insert 1: “if I\_Q=LQ and DEGREE<>B and 35<AGE<41 then RECOM=G”

Answer:

Insert 2: “if I\_Q=LQ and DEGREE=B and AGE<36 and EXP<2 then RECOM=P1”

Answer:

Insert 3: “if I\_Q=HQ and AGE>44 then RECOM=NA”

Answer:

## References

[1] R. Agarwal, M. Tanniru, A structured methodology for developing production systems, Decision Support Systems 8, 1992, pp. 483–499.

[2] R. Agarwal, M. Tanniru, A Petri-Net based approach for verifying the integrity of production systems, International Journal of Man-Machine Studies 36, 1992, pp. 447–468.

[3] J. Bachant, E. Soloway, The engineering of XCON, Communications of the ACM 32(3), 1989, pp. 311–317.

[4] V.E. Barker, D.E. O'Connor, Expert systems for configuration at Digital: XCON and beyond, Communications of the ACM 32(3), 1989, pp. 298–310.

[5] A. Basu, R.W. Blanning, Metagraphs: A tool for modeling decision support systems, Management Science 40(12), 1994, pp. 1579–1600.

[6] B.W. Boehm, Software Engineering Economics, Prentice Hall, 1981.

[7] F. Coenen, T. Bench-Capon, Maintenance of Knowledge-based Systems, Academic Press, London, 1993.

[8] B.J. Cragun, H.J. Steudel, A decision-table-based processor for checking completeness and consistency in rule-based

expert systems, International Journal of Man-Machine Studies 26, 1987, pp. 633–648.

[9] J.S. Davis, Effect of modularity on maintainability of rule-based systems, International Journal of Man-Machine Studies 32, 1990, pp. 439–447.

[10] T.A. Defanti, M.D. Brown, Visualization: Expanding scientific and engineering research opportunities, Computer, August 1989, pp. 12–25.

[11] T.G. Gill, Early expert systems: Where are they now, MIS Quarterly, March 1995, pp. 51–81.

[12] A. Ginsberg, A new approach to checking knowledge bases for inconsistency and redundancy, Proceedings of the Third Annual Expert Systems in Government Conference, Washington, DC, 1987, pp. 102–111.

[13] A. Ginsberg, Knowledge-base reduction: A new approach to checking knowledge bases for inconsistency and redundancy, Proceeding of National Conference on Artificial Intelligence, 1988, pp. 595–589.

[14] R.C. Hicks, Minimizing maintenance anomalies in expert systems, Information and Management 28, 1995, pp. 177–184.

[15] K. Higa, Y. Liou, Object classification model (OCM): A graph-based technique for knowledge acquisition and representation, Proceedings of the 7th Banff Knowledge Acquisition for Knowledge-based Systems Workshop, Banff, Alberta, Canada, 1992, pp. 13.1–13.13.

[16] K. Higa, O.R. Liu Sheng, An object-oriented methodology for an end-user logical database design: The structured entity model approach, Proceedings of IEEE 13th International Computer Software and Applications Conference, Orlando, FL, 1989, pp. 365–373.

[17] R.J.K. Jacob, J.N. Froscher, A software engineering methodology for rule based systems, IEEE Transactions on Knowledge and Data Engineering 2(2), 1990, pp. 173–189.

[18] C. Kai, S. Weston, Software maintainability: Perceptions of EDP professionals, MIS Quarterly 12(2), 1988, pp. 167–186.

[19] D.L. Nazareth, Issues in the verification of knowledge in rule-based systems, International Journal of Man-Machine Studies 30, 1989, pp. 255–271.

[20] H.P. Newquist III, Struggling to maintain, AI Expert 3(8), 1988, pp. 69–71.

[21] T.A. Nguyen, Verifying consistency of production systems, Proceedings of The Third Conference on Artificial Intelligence Applications, IEEE Computer Society Press, Washington, DC, 1987, pp. 4–8.

[22] T.A. Nguyen, W.A. Perkins, T.J. Laffey, D. Pecora, Checking and expert system's knowledge base for consistency and completeness, Proceedings of IJCAI85, 1985, pp. 375–378.

[23] T.A. Nguyen, W.A. Perkins, T.J. Laffey, D. Pecora, Knowledge base verification, AI Magazine, Summer 1987, pp. 69–75.

[24] M. Suwa, A.C. Scott, E.H. Shortliffe, An approach to verifying completeness and consistency in a rule-based expert system, AI Magazine (1982) 16–21.

[25] M. Suwa, A.C. Scott, E.H. Shortliffe, Completeness and consistency in a rule-based system, in: B.G. Buchanan, E.H. Shortliffe (Eds.), Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project, Reading, MA: Addison-Wesley, 1984, pp. 159–170.

[26] B.P. Zeigler, System-theoretic representation of simulation models, IIE Transactions 16(1), 1985, pp. 19–34.

![](/api/attachments/5R643YGN/fulltext/images/d731464659e3a0cf473ecec141ebd74bcab77ef04a21d269e4bfb22f2c538f04.jpg)

Kunihiko Higa received a Ph.D. in management information systems from the University of Arizona in 1988. He was a faculty member at the Georgia Institute of Technology and then at the Hong Kong University of Science and Technology. He is currently an associate professor at the Tokyo Institute of Technology. His research interests include database analysis/design methodology, database/knowledge base integration, well-

structured rule base design, and Telework. He has published in the Communications of ACM, DSS, and many other academic journals. He is currently on the editorial board of the Journal of Database Management. He is a member of ACM, AIS, INFORMS, and JASMIN.

![](/api/attachments/5R643YGN/fulltext/images/c5a55b25bced9c90b0e538512a0f34ed500bcf6f54df385e0e634fdc650485eb.jpg)

Ho Geun Lee is an ssistant professor of College of Business and Economics at Yonsei University in Korea. He received his Ph.D. in management information systems from the University of Texas at Austin in 1993. His research area includes IT productivity, EDI and interorganizational systems, and electronic commerce. Before joining Yonsei University, he was a visiting scholar at the Rotterdam School of Management, Erasmus University, in the

Netherlands and an assistant professor at the Hong Kong University of Science and Technology. His recent articles appear (or will appear) in the Communications of the ACM, Journal of Management Information Systems, International Journal of Electronic Commerce, Annals of Operations Research, Decision Support Systems, Journal of Organizational Computing, and Electronic Commerce.
