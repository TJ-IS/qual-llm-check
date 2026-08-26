---
otero_id: 17763
otero_key: "FACNWWF7"
title: "An approach to improving the maintainability of existing rule bases"
authors: "Kunihiko Higa"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00015-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach to improving the maintainability of existing rule bases

Kunihiko Higa \*

The Hong Kong University of Science and Technology, Department of Information and Systems Management, Clear Water Bay, Kowloon, Hong Kong

## Abstract

A rule base (RB) can be both logically sound (complete and correct) and difficult to maintain often because of its complex rule structure. From examinations of several RBs in textbooks, in expert systems shells, and in research projects, complex rule structures have been found to be a rather common phenomenon. This paper reveals the side-effects of carrying complex rule structures in RBs and then provides formal definitions of complex rule structures. Next, it introduces a procedure to detect and simplify such structures. The proposed rule simplification procedure will improve the maintainability of RBs. Its use is illustrated through sample RBs.

Keywords: Expert systems; Rule structure; Rule base maintenance; Rule simplification

## 1. Introduction

Expert systems (ES) have proven to be quite effective in solving a variety of real world problems in industry and business. Consequently ES technology has been adapted by many organizations in recent years. Because of its modularity and (perceived) ease of use, production rules have been widely used in developing ES [4,14,16]. Although a rule base (RB) can be complete, correct, and acceptable to its stakeholders (including local experts, users, managers, the organization, and knowledge engineers), it can still be difficult to maintain. Difficult maintenance of a RB are often attributed to the existence of unwanted relationships between rules. In this paper, a rule set that contains unwanted relationships between rules is said to have complex rule structures. This paper reveals the side-effects of carrying complex rule structures in RBs and introduces a procedure for the simplification of rule structures.

Examination of several RBs in expert systems textbooks, sample RBs of expert systems shells, and RBs in research projects has shown that maintainability problems caused by complex rule structures appear to be the norm rather than the expectation. The following two simple RBs will illustrate this point.

## RB Example 1:

Let RB1 contain

Domains: A{true, false}, B{true, false}, C{true, false}, G{g1, g2, g3}, and Rule Set:

R1: IF A is true AND C is true THEN G is g1
R2: IF A is true AND B is true AND C is false
THEN G is g1

R3: IF $A$ is false AND $B$ is NOT(C) THEN $G$ is $g^3$

R4: IF $B$ is true AND $C$ is true THEN $G$ is gl

R5: IF B is false AND C is false THEN G is g2

RB Example 2:

Let RB2 contain

Domains: same as RB1's domains and Rule Set:

R1-R2: identical to RB1's R1 and R2

R3: IF $B$ is false AND $C$ is false THEN $G$ is $g2$

R4: IF $A$ is false AND $B$ is true AND $C$ is true THEN $G$ is $g1$

R5: IF $A$ is false AND $B$ is true AND $C$ is false THEN $G$ is $g3$

R6: IF A is false AND B is false AND C is true THEN G is g3

Then consider the following change to these RBs: "Add g4 to G and change R1's goal value from g1 to g4."

RB1 and RB2 are logically equivalent. For RB1, however, this change is not as straightforward as it seems. Unless it is carried out precisely, RB1 will become inconsistent because R1 overlaps with R4, i.e., RB1 contains a complex rule structure. In contrast, because RB2 does not have any complex rule structures, the change affects only R1 in RB2.

This example illustrates that even if a RB is logically correct and complete, it could still be difficult to maintain. This paper addresses maintainability problems that have not been addressed by previous research and introduces a procedure to resolve such problems.

## 2. Related work

Numerous research has been conducted in the area of ES design and maintenance. Most research in this area, however, tends to focus on tools for verification and validation $[1-3,7,8,10,17]$ , on automated tools for rule generation $[9,11,15]$ , and on performance issues $[6]$ . The common objective of all this research is to create expert systems that are logically correct and complete and are acceptable to the stakeholders of expert systems. However, even if this objective is achieved, the resulting knowledge bases could still be difficult (and thus expensive) to maintain. Some existing research is discussed in the following.

Prerau et al. [13] have developed several techniques and guidelines to aid maintainability of ES based on their experience with the COMPASS project. Their work on the maintainability of knowledge bases has focused on the organization of multiple knowledge bases (hierarchical organization) and control flow between knowledge bases. Their work did not address any structural issue of rule bases, however.

Nguyen et al. [10] have addressed the problem of verifying the consistency and completeness of knowledge bases and discussed the effect of certainty factors on the verification of rule bases. Chang et al. [1] have addressed the entire process of verification and validation (V&V) of knowledge bases and produced a comprehensive checklist for the V&V process. Although both studies have reported successful implementation of automated tools for V&V, neither has provided precise definitions of the problems addressed and algorithms used to detect and resolve those problems, making comparison of their work with that of other researchers impossible.

Since well-structured (WS) rules are believed to be easy to understand and to maintain, other researchers [6,12] have proposed methodologies that rely on them. Although Pedersen [12] discussed the consequences of not having WS rules, he did not provide any methodology for creating WS rules. Jacob and Froscher [6], on the other hand, described grouping of rules for promoting the modularity of RBs thus improving their maintainability. The problems addressed in [6] are quite different from this paper's, and both works can be seen as complementing to each other.

Although not primarily interested in creation of well-structured RBs, still other researchers have developed automated tools that generate high quality RBs which are efficient and contain considerably less logical errors. For example, Liang has developed an automated rule generation tool [9] that uses a composite rule induction approach and appears to produce a well-structured set of rules that perform better than Quinlan's ID3[15]. However, the tool is usable only if “good” example data are available. Pearce has reported that rules automatically generated from a qualitative model contain much less errors than rules generated by humans [11]. The qualitative model approach, however, does not guarantee the internal validity of resulting RBs.

## 3. Maintainability of rule bases

Maintainability of RBs is concerned with redundancy and stability. Redundancy in a RB is typically caused by the presence of subsumption and by duplication of rules. A RB is considered to be unstable when a simple change in one rule easily creates inconsistency in the RB. This problem typically occurs when there are overlaps and adjacent domain coverage between rules.

Therefore, a RB is said to be maintainable when it:

1. has no duplicated rules,

2. has no rule that subsumes other rules,

3. consists of rules that are minimal, i.e., there are no overlapping rules,

4. has no rule that has the same consequent value and adjacent antecedent value as any other rules. These four conditions eliminate potential inconsistency in a RB and thus improve its maintainability. The first two conditions have been defined by existing works $[1,3,10]$ while the last two conditions have not. Therefore, the last two conditions (3) and (4) are defined in this section. However, because the definition of condition (2) is required for resolving the overlapping rule structure, it is also discussed here.

## 3.1. Notations and definitions

A RB contains a set of domains (DS) and a set of rules (RS). A DS can be categorized into the domains of antecedent attributes (DSa) and the domains of goal attributes (DSg). A RS is a collection of rules, and each rule can be seen as an ordered pair (A, G) where A is an antecedent of a rule and G is a consequent of a rule. Then a RB is defined as:

$$
\mathrm{RB} = \left\{\mathrm{DS}, \mathrm{RS} \right\}, \mathrm{DS} = \left\{\mathrm{DS} a, \mathrm{DS} g \right\},
$$

$$
\mathrm{RS} = (\mathrm{R1}, \dots , \mathrm{Rn}),
$$

$Ri = (Ai, Gi)$ , where $Ai = \cap (a_{ij}, o_{ij}, v_{ij})$ for $j = 1 \ldots m$ , $a_{ij}$ is an attribute, $o_{ij}$ is an operator, $v_{ij}$ is a value, and m is the number of antecedent attributes in the RB.

The domain of $a *_{j}$ is $\mathrm{DS}a_{j}$ .

Then the aforementioned three conditions (2), (3), and (4) are defined as:

## Subsumption:

Rj subsumes Ri if $Ai \subset Aj$ and $Gi = Gj$ ,

i.e., Aj logically dominates Ai, and Gi and Gj are identical.

E.g., let R1: IF $a > 3$ AND $b = 0$ THEN $g1$ ; R2: IF $a > 2$ AND $b = 0$ THEN $g1$ .

Then $A1: (a > 3 \text{ AND } b = 0) \subset A2: (a > 2 \text{ AND } b = 0)$ and $G1: g1 = G2: g1$ .

Therefore, R2 includes R1.

Note that the duplicate condition is a special case of the subsumption condition, where $Ai = Aj$ instead of $Ai \subset Aj$ .

## Overlap:

$Ri$ overlaps with $Rj$ if the duplicate condition and the subsumption condition do not hold between $Ai$ and $Aj$ , and $Ai \cap Aj < > \phi$ and $Gi = Gj$ , where $Ai \cap Aj \langle \rangle \phi$ means that $Ai$ and $Aj$ have at least one $a-o-v$ triplet such that $(a_{is}, o_{is}, v_{is}) \cap (a_{js}, o_{js}, v_{js}) < > \phi$ and $[\cap (a_{it}, o_{it}, v_{it})] \subseteq [\cap (a_{jt}, o_{jt}, v_{jt})]$ for $t \neq s$ and $t = 1 \ldots m$ . E.g., let R1: IF $a < 5$ AND $b = 0$ THEN $g1$ ; R2: IF $a > 3$ THEN $g1$ . Then $A1.(a < 5) \cap A2.(a > 3) < > \phi$ and $A1.(b = 0) \subseteq A2.(b = *)$ .

Therefore, R1 overlaps with R2.

## Adjacency:

Ri is adjacent to Rj if $Ai \cup Aj$ contains no gap and Gi = Gj, i.e., Ai and Aj have one a-o-v triplet such that $[(a_{is}, o_{is}, v_{is}) \cup (a_{js}, o_{js}, v_{js})] = DS a_{s}$ if $a_{s}$ is a categorical attribute (note: this particular type of adjacency is also known as “unnecessary IF condition” [10])

$\left[(a_{is}, o_{is}, v_{is}) \cup (a_{js}, o_{js}, v_{js})\right]$ contains no gap if $a_s$ is a non-categorical attribute

$\left[\cap \left(a_{it}, o_{it}, v_{it}\right)\right] = \left[\cap \left(a_{jt}, o_{jt}, v_{jt}\right)\right]$ for $t \neq s$ and $t = 1 \ldots m$ .

![](/api/attachments/FACNWWF7/fulltext/images/ab6b472a0f1c75004968387af836df1b26d0729062e0fd3a3fe9ffece29ff7b5.jpg)  
Fig. 1. Overview of the RB simplification procedure.

E.g., let R1: IF a is true AND b is true THEN g1; R2: IF a is true AND b is false THEN g1. Then A1.(b is true) ∪ A2.(b is false) = DSa $_{b}$ and A1.(a is true) = A2.(a is true).

Therefore, R1 is adjacent to R2.

## 3.2. Detection and resolution of maintainability problems

As depicted in Fig. 1, the procedure for detection and resolution of maintainability problems contains three phases: preparation, detection, and resolution. In this section, each phase of the procedure is described and illustrated using the following RB example.

## RB Example 3:

Let RB3 contain

Domains: DS $a = \{A\{\text{true, false}\}, B\{\text{true, false}\}, C[1 \ldots 10]\}$ , DS $g = G\{g1, g2, g3\}$ , and Rule Set (RS):

R1: IF $A$ is true AND $B$ is true AND $C < 4$ THEN $G$ is $g1$

R2: IF A is true AND B is true AND 4 <= C
<= 7 THEN G is g2

R3: IF A is true AND B is true AND C > 7
THEN G is g3

R4: IF (A is true OR B is true) AND C < 4
THEN G is g1

R5: IF $A$ is NOT(B) AND $C > 8$ THEN $G$ is $g2$

R6: IF A is true AND B is false AND 5 <= C

$< = 8$ THEN $G$ is $g2$

R7: IF $A$ is false AND $B$ is false THEN $G$ is $g1$

R8: IF A is true AND B is false AND 4 <= C

$< = 5 \text{ THEN } G \text{ is } g2$

R9: IF A is false AND B is true AND 4 <= C
<= 8 THEN G is g3

## Phase I: Preparation

This phase makes problem detection of the target rule set manageable. In this phase, all compound rules are decomposed into simple rules, and then the RB is divided into small independent groups. All duplication and overlap problems are also automatically solved through the preparation process.

Step I.1. Remove any “OR” and “NOT” from rules. A rule that contains “OR” and/or “NOT” is a compound rule. An overlap problem that is caused by compound rules is difficult to detect; therefore, all compound rules are decomposed into simple rules in this phase.

E.g., an OR is removed from R4 and a NOT is removed from R5 then

R4.1: IF $A$ is true AND $B$ is true AND $C < 4$ . THEN $G$ is $g1$

R4.2: IF $A$ is true AND $B$ is false AND $C < 4$ THEN $G$ is $g1$

R4.3: IF $A$ is false AND $B$ is true AND $C < 4$ THEN $G$ is $g1$

R5.1: IF $A$ is true AND $B$ is false AND $C > 8$ THEN $G$ is $g2$

R5.2: IF $A$ is false AND $B$ is true AND $C > 8$ THEN $G$ is $g2$

Note that a compound rule needs not be simplified if it does not share its goal value with any other rule in the RB. In this example, R4 and R5 are simplified because they share goal values with other rules in RB3 (R2, R5, R6, and R8 all have g2, and R1, R4, and R7 all have g1).

Step I.2. Group rules by goal values. Rules that have a common goal value are grouped together. The grouping of rules makes comparison of rules easier.

Decision tables for RB3

E.g., Group1 = {R1, R4.1, R4.2, R4.3, R7} for g1; Group2 = {R2, R5.1, R5.2, R6, R8} for g2; Group3 = {R3, R9} for g3.

Step 1.3. Transform non-categorical attributes into pseudo-categorical attributes. This transformation separates intersecting parts from overlapping rules; therefore, it transforms overlap problems into adjacency problems that are easier to solve. The process is carried out in the following manner:

(1) Choose the smallest range for a non-categorical attribute in a group.

(2) Use the range to partition relevant rules.

(3) Choose the next smallest range for the attribute and perform Step (2). Repeat the process for the attribute until no further partition is possible.

(4) Repeat (1) through (3) for all non-categorical attributes in the group.

(5) Repeat (1) through (4) for all groups.

E.g., in Group1, “C < 4” in R1 and R4.\* is the smallest range for “C”, thus R7 is divided into

R7.1: IF A is false AND B is false AND $\dot{C} < 4$ THEN g1

R7.2: IF $A$ is false AND $B$ is false AND $C > = 4$ THEN $g1$ .

In Group2, “C > 8” in R5.\* covers the smallest range; however, no other rule uses this range. Therefore, “4 <= C <= 5” in R8 is used to divide R2 and R6. Thus R2 is divided into

R2.1: IF $A$ is true AND $B$ is true AND $4 < = C$ $< = 5$ THEN $G$ is $g2$

R2.2: IF $A$ is true AND $B$ is true AND $5 < C$ $< = 7$ THEN $G$ is $g2$

and R6 is divided into

R6.1: IF $A$ is true AND $B$ is false AND $C = 5$ THEN $G$ is $g2$

R6.2: IF A is true AND B is false AND 5 < C <= 8 THEN G is g2.

![](/api/attachments/FACNWWF7/fulltext/images/b17d5fd86e590adaba80ee090489c1df73a32fb06ee7868bbd3b2be515c247c0.jpg)  
Fig. 2. Decision trees for RB3.

In Group3, C > 7 is the smallest range for C, thus R9 is divided into

R9.1: IF $A$ is false AND $B$ is true AND $4 < = C$ $<= 7$ THEN $G$ is $g3$

R9.2: IF $A$ is false AND $B$ is true AND $7 < C$ $< = 8$ THEN $G$ is $g3$ .

Step 1.4. Represent each group in a decision tree format. This step consolidates duplicated rules and organizes rules in an orderly manner (see Fig. 2).

Step 1.5. Represent each tree in a decision table format. The table format makes detection of maintainability problems simple.

E.g., three trees in Step I.4 are represented in Table 1 (each column represents a rule).

Phase II: Detection

In this phase, the decision tables from Step I.5. (Table 1) are used for detection of maintainability problems. Because all overlap problems and duplicate problems are resolved in Step I.3 and Step I.4, only subsumption and adjacency problems need to be detected in this phase.

<table><tr><td colspan="6">Group 1:</td><td colspan="7">Group 2:</td><td colspan="3">Group 3:</td></tr><tr><td>A</td><td>T</td><td>T</td><td>F</td><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td><td>T</td><td>T</td><td>T</td><td>F</td><td>T</td><td>F</td><td>F</td></tr><tr><td>B</td><td>T</td><td>F</td><td>T</td><td>F</td><td>F</td><td>T</td><td>T</td><td>F</td><td>F</td><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td><td>T</td></tr><tr><td>C</td><td>4)</td><td>4)</td><td>4)</td><td>4)</td><td>[4]</td><td>[4,5]</td><td>(5,7]</td><td>[4,5]</td><td>5</td><td>(5,8]</td><td>(8)</td><td>(8)</td><td>(7)</td><td>[4,7]</td><td>(7,8]</td></tr><tr><td>G</td><td>g1</td><td>g1</td><td>g1</td><td>g1</td><td>g1</td><td>g2</td><td>g2</td><td>g2</td><td>g2</td><td>g2</td><td>g2</td><td>g2</td><td>g3</td><td>g3</td><td>g3</td></tr></table>

Table 2  
Decision tables after one simplification process

<table><tr><td colspan="4">Group 1:</td><td colspan="4">Group 2:</td><td colspan="2">Group 3:</td></tr><tr><td>A</td><td>T</td><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td><td>F</td><td>T</td><td>F</td></tr><tr><td>B</td><td></td><td></td><td>F</td><td>T</td><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td></tr><tr><td>C</td><td>4)</td><td>4)</td><td>[4]</td><td>[4,7]</td><td>[4,5]</td><td>(5)</td><td>(8)</td><td>(7)</td><td>[4,8]</td></tr><tr><td>G</td><td>g1</td><td>g1</td><td>g1</td><td>g2</td><td>g2</td><td>g2</td><td>g2</td><td>g3</td><td>g3</td></tr></table>

Step II.1. Identify subsumptions in the tables using the aforementioned condition between rules.

E.g., in Group2, column 3 subsumes column 4 because

Col4. $(C=5)\subset\mathrm{Col3.}(4<=C<=5)$ ,

Col4:(A = true AND B = true) = Col3.(A = true

AND $B = \mathrm{true})$ and

$$
\operatorname{Col} 4. (G = g 2) = \operatorname{Col} 3. (G = g 2).
$$

Step II.2. Identify adjacent rules in the tables using the aforementioned condition between rules. Columns that are not involved in the subsumption problem in Step II.1 are compared for the adjacency condition.

Col1.(A = true AND C < 4) = Col2.(A = true AND C < 4), and

E.g., in Group1, column 1 is adjacent to column 2, and column 3 is adjacent to column 4 because

Similarly, in Group2, column 1 is adjacent to column 2, and column 5 is adjacent to column 6. In Group3, column 2 is adjacent to column 3.

Col1. $(G = g1) = \operatorname{Col2}. (G = g1)$ ;

Col1.(B is true) ∪ Col2.(B is false) = DS $a_{B}$ ,

Col3. $(B$ is true) $\cup$ Col4. $(B$ is false) $= \mathrm{DS}a_{B}$ ,

Subsumption and adjacency problems are resolved in this phase.

Col3.(A = false AND C < 4) = Col4.(A = false AND C < 4), and

Phase III: Resolution

Col3. $(G=g1)=\mathrm{Col4.}(G=g1)$ .

Step III.1. Resolve subsumptions by deleting subclass rules.

E.g., in Group2, column 4 is deleted.

Step III.2. Resolve adjacency by concatenating the adjacent rules.

E.g., in Group1, columns 1 and 2 are concatenated and become (T,'4'), g1); columns 3 and 4 are concatenated and become (F,'4'), g1).

In Group2, columns 1 and 2 are concatenated and become (T, T,'[4,7], g2); columns 5 and 6 are concatenated and become (T, F, '(5', g2).

In Group3, columns 2 and 3 are concatenated and become (F, T, '[4,8]', g3).

At this point, three tables become as in Table 2. Phases II and III must be repeated until there are no more problems to be resolved.

During the second round of the detection-resolution process, two more adjacency problems are detected and resolved (between columns 1 and 2 in Group1 and between columns 2 and 3 in Group2). Then three tables become as in Table 3.

Table 3  
Simplified decision tables for RB3

<table><tr><td colspan="2">Group 1:</td><td colspan="4">Group 2:</td><td colspan="2">Group 3:</td></tr><tr><td>A</td><td></td><td>F</td><td>T</td><td>T</td><td>F</td><td>T</td><td>F</td></tr><tr><td>B</td><td></td><td>F</td><td>T</td><td>F</td><td>T</td><td>T</td><td>T</td></tr><tr><td>C</td><td>4)</td><td>[4]</td><td>[4,7]</td><td>[4]</td><td>(8)</td><td>(7)</td><td>[4,8]</td></tr><tr><td>G</td><td>g1</td><td>g1</td><td>g2</td><td>g2</td><td>g2</td><td>g3</td><td>g3</td></tr></table>

At this point, the tables contain no more problems. Thus the resulting rule set contains seven well-structured rules. The logical equivalence of this rule set with RB3 can be verified by testing with 40 different combinations of antecedent values (two for A, two for B, and ten sub-ranges for C: $2 \times 2 \times 10 = 40$ ).

Note that the proposed procedure is not intended to reduce the number of rules in a RB but to reduce the complexity of the RB structure. It simplifies the structure of each rule and the relationships between rules in the RB for manageable maintenance.

## 4. Cost of having overlapping rules

An experiment was conducted to determine the impact of having overlapping rule structure on maintenance of a RB, and the results were reported in [5]. In this section, a summary of the experiment is presented and discussed.

## 4.1. Experiment setting

Twenty one students (7 graduate and 14 undergraduate) who were enrolled in an Expert Systems course at the Georgia Institute of Technology participated in the experiment. The subjects had an average work experience (full time) of 1.8 years and none had previous experience in maintenance of RBs. As pre-test training, two lectures (50 minutes each) and one assignment (similar to the experiment task) were given to the subjects one week before the experiment.

At the experiment, subjects were asked to perform maintenance jobs for two separate rule sets, A and B. Each job included insertions of three new rules into a rule set. Set A was given to all subjects first and then Set B was given as soon as each subject completed the job for Set A. Set B was extracted from an existing RB and contained eight rules with overlapping structure while Set A was a simplified version of Set B. Therefore, both sets were logically equivalent. In addition the same job was used for both sets, i.e., three new rules for A = three new rules for B.

Since the overlapping rule structure has not been recognized as a maintenance problem, the following two hypotheses were tested in this experiment:

H1: The overlapping structure in a rule set does not affect the accuracy of the maintenance task.

H2: The overlapping structure in a rule set does not affect the time needed to complete the maintenance task.

Measurement of each factor (accuracy and time) was performed in the following manner:

Accuracy: One point is awarded for each correct insertion. 0.5 point is awarded when an insertion is near complete and does not cause any inconsistency. Zero points are awarded for all other cases. Therefore, a maximum of three points can be awarded for each set (i.e., 3 insertions/set).

Time: Start and end times of each set are recorded for each subject.

## 4.2. Results

The subjects performed near perfect maintenance on Set A (the score was 2.9/3) and were 48% less accurate on Set B (the score was 1.5/3). The difference in accuracy was statistically significant at alpha level 0.005. Since both sets are logically equivalent and the jobs are identical and performed by the same subjects, the difference in rule structures must be the explanation for the difference in accuracy.

Although, the subjects performed quite accurately on Set A, they used much less time to complete the job on Set A (an average of 15 minutes) than the job on Set B (an average of 27 minutes). The difference was statistically significant at alpha level 0.005. Again, the difference in rule structures between the two sets was the only explanation.

After the experiment, subjects were asked if they noticed that both sets were logically equivalent and both jobs were identical. None of the subjects realized either point until they were told. Many subjects felt that the job on Set B was much harder than the job on Set A. They were quite surprised to learn that both jobs were identical.

The results of this experiment clearly indicate that overlapping rule structures negatively affect the maintenance of RBs in a serious manner (they are much less accurate and require much more time). Although additional experiments will be needed to verify the discovery of the work in [5], it is obvious that research on complex rule structures is critically needed.

![](/api/attachments/FACNWWF7/fulltext/images/c75eae9ae040a12db6eeb3c832bf7fe4b995896d8d7c92e5cd67d488f9694c4b.jpg)  
Fig. 3. Overview of RB development.

## 5. Conclusion

Production rules have been widely used in developing ES. Rules were initially considered to be easy to design and maintain; however, the experience of many knowledge engineers and researchers indicated otherwise. Although many methodologies have been developed to improve quality of RBs, maintenance of RBs can still be difficult and expensive to perform. The maintainability problems of RBs are often caused by their complex rule structures. This paper has provided formal definitions of maintainability problems and has introduced a procedure to detect and resolve such problems. The use of the proposed procedure has been illustrated with a sample RB.

## 5.1. Limitations and future research directions

The proposed procedure is effective only if the target RB is logically sound. When the RB contains logical problems such as inconsistencies, dead-end if, circular if, etc., these will be carried into the simplified RB because the procedure does not detect the logical problems.

Further, the efficiency of the proposed procedure needs to be examined in future studies. For example, in RB Example 3, R2 and R9 are divided into multiple rules in Phase I and then put together to become the same rules in Phase III. This is done because rules are divided without determining the necessity for analysis of the rules. In addition, it is natural to ask if the removal of all ORs and NOTs in Phase I is necessary. Although the rules can be put together using ORs and NOTs after the simplification process, the removal of ORs and NOTs may cause an explosive increase in rule base size. An efficient way to manage selective removal of ORs and NOTs and partitioning of rules needs to be determined.

Finally, the proposed procedure should be viewed as part of the RB development cycle (see Fig. 3). Most research has focused on the creation of a complete and correct initial rule set and the subsequent optimization of that rule set. However, the optimization of a rule set should be performed only after rule structures have been simplified. In addition, the simplified rule set should be kept for future maintenance of the RB. Inclusion of simplification in the RB development cycle will improve the maintainability of the resulting RB.

## References

[1] C.L. Chang, J.B. Combs and R.A. Stachowitz, A Report on the Expert Systems Validation Associate (EVA), Expert Systems with Applications, Vol. 1 (1990) 217—230.

[2] R. Enand, G.S. Kahn and R.A. Mills, A Methodology for Validating Large Knowledge Bases, Proceedings of the 3rd Knowledge Acquisition for Knowledge-Based Systems Workshop, Banff, Canada (November 1988).

[3] J.R. Geissaman, Verification and Validation for Expert Systems: A Practical Methodology, Proceedings of the 4th Annual Artificial Intelligence and Advanced Computer Technology Conference (1988).

[4] F. Hayes-Roth, Rule-Based Systems, Communications of the ACM 28, No. 28 (September 1985).

[5] K. Higa, Cost Implication of Overlapping Rules Structures on Maintenance of Rule Bases: An Empirical Study, Working Paper, Hong Kong University of Science and Technology, Department of Business Information Systems, BIS-WPS-8/94 (1994).

[6] R.J.K. Jacob and J.N. Froscher, A Software Engineering Methodology for Rule-Based Systems, IEEE Transactions on Knowledge and Data Engineering 2, No. 2 (June 1990).

[7] P.E. Lehrer, Toward an Empirical Approach to Evaluating the Knowledge Base of an Expert System, IEEE Transactions on Systems, Man and Cybernetics 19, No. 3 (May/June 1989).

[8] R. Lelouche and L. Vignollet, Towards an Automatic Generation of Test Cases for a Knowledge Bases System Using the Inference Engine Control Strategy, Proceedings of the 3rd Annual International Association of Knowledge Engineers Symposium, Washington DC (November 1992).

[9] T.-P. Liang, A Composite Approach to Inducing Knowledge for Expert Systems Design, Management Science 38, No. 1 (January 1992).

[10] T.A. Nguyen, W.A. Perkins, T.J. Laffey and D. Pecora, Knowledge Base Verification, AI Magazine (Summer 1987).

[11] D. Pearce, Knowledge Base Validation, IEE Colloquium on 'Expert Systems and Safety', Digest, No. 026 (1991).

[12] K. Pedersen, Well-Structured Knowledge Bases, AI Expert 4, No. 4 (1989).

[13] D.S. Prerau, A.S. Gunderson, R.E. Reinke and M.R. Adler, Maintainability Techniques in Developing Large Expert Systems, IEEE Expert 5, No. 6 (June 1990).

[14] C.L. Ramsey, J.A. Reggia, D.S. Nau and A. Ferrentino, A Comparative Analysis of Methods for Expert Systems, International Journal of Man-Machine Studies, Vol. 24 (1986).

[15] J.R. Quinlan, Discovering Rules from Large Collections of Examples: A Case Study, in: D. Michie, Ed., Expert Systems in the Micro Electronic Age (Edinburgh University Press, Edinburgh, Scotland, 1979).

[16] C.Y. Suen, P.D. Grogono, R. Shinghal and F. Coallier, Verifying, Validating, and Measuring the Performance of Expert Systems, Expert Systems with Applications, Vol. 1 (1990).

[17] E. Turban, Review of Expert Systems Technology, IEEE Transactions on Engineering Management 35, No. 2 (May 1988).

![](/api/attachments/FACNWWF7/fulltext/images/08160bb1c599dbe2dc7734a4b0b138de875fd136f9bbf9e470bf3c836ba02405.jpg)

Kunihiko Higa received a Ph.D. in Management Information Systems from the University of Arizona in 1988. He was a faculty member at Georgia Institute of Technology from 1989 to 1993 and at Hong Kong University of Science and Technology from 1993 to 1996. He is currently an Associate Professor of Management Information Systems at Tokyo Institute of Technology. His research interests include database analysis/design methodology, database/

knowledgebase integration, well-structured rule base design, and Telework. He has published in the Communications of ACM, Organizational Computing, Journal of Database Management, and many other academic journals.
