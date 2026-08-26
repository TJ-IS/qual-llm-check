---
otero_id: 21535
otero_key: "C7PC44BY"
title: "Verification of non-monotonic knowledge bases"
authors: "Neli P Zlatareva"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00044-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Verification of non-monotonic knowledge bases

Neli P. Zlatareva )

Department of Computer Science, Central Connecticut State UniÕersity, New Britain, CT 06050-4010, USA

## Abstract

Non-monotonic Knowledge-Based Systems KBSs must undergo quality assurance procedures for the following twoŽ . reasons: i belief revision if such is provided cannot always guarantee the structural correctness of the knowledge base,Ž . Ž . and in certain cases may introduce new semantic errors in the revised theory; ii non-monotonic theories may have multipleŽ . extensions, and some types of functional errors which do not violate structural properties of a given extension are hard to detect without testing the overall performance of the KBS. This paper presents an extension of the distributed verification method, which is meant to reveal structural and functional anomalies in non-monotonic KBSs. Two classes of anomalies are considered: i structural anomalies which manifest themselves within a given extension such as logical inconsistencies,Ž . Ž structural incompleteness, and intractabilities caused by circular rule chains , and ii functional anomalies related to the. Ž . overall performance of the KBS such as the existence of complementary rules and some types of rule subsumptions . TheŽ . corresponding verification tests are presented and illustrated on an extended example. q 1997 Elsevier Science B.V.

Keywords: Verification; Performance evaluation; Testing; Validation; Quality assurance; Anomaly detection; Non-monotonic theories; Knowledge-Based Systems; Expert systems; Truth maintenance systems; Default reasoning

## 1. Introduction

In the recent years, a significant effort has been made to tackle different aspects of Knowledge-Based Systems KBS quality assurance. Although success Ž . has been achieved in certain areas, especially in the development of formal methods for KBS verification and building of verification tools, most of this work is limited to rule-based systems employing monotonic inference. More advanced KBSs often referred Ž to as a second generation KBSs are non-monotonic.. To cope with incomplete domain specifications, these systems employ some form of a closed world assumption for example, negation in logic program- Ž ming and defaults in frame representation systems and semantic networks , which may lead to the. replacement of already inferred conclusions with new ones if additional evidence becomes available later in the inference process. As a result, the consistency of the knowledge base KB can be violated. ToŽ . handle such cases, some non-monotonic systems incorporate a belief revision facility. There is no guarantee, however, that belief revision will necessarily succeed in recovering the consistency of the KB. Moreover, new semantic errors can be introduced as a result of the belief revision process 17 . This is<sup>w</sup> <sup>x</sup> why we argue that non-monotonic KBSs must undergo quality assurance procedures to ensure the structural correctness of their knowledge bases and their problem-solving adequacy.

So far, little attention has been paid in the V & V community to quality assurance of non-monotonic

KBSs. This is partially due to the fact that these systems are still at the stage of research prototypes, and partially due to the widely spread perception that the nature of non-monotonic reasoning suggests incompleteness and inconsistency in the domain specification, and thus functional problems are unavoidable. We believe that quality assurance procedures can help in detecting and correcting a large number of potential functional errors.

The first attempt to address quality assurance needs of non-monotonic KBSs was undertaken within the EVA project 2 . This research, however, was <sup>w</sup> <sup>x</sup> mostly concerned with defining what a non-monotonic KBS is, rather than with identification and characterization of classes of anomalies that a nonmonotonic KBS may contain. The types of errors examined were redundancies, inconsistencies, and incompleteness. It was suggested that the detection of such errors can be carried out in the same way as in monotonic KBS, namely by describing higherorder constructs metapredicates representing differ-Ž . ent types of errors. Metapredicates are entered as queries to the KBS, and the generated answers reveal all of the errors of a particular type detected in the KB-theory.

There are at least two problems with this approach:

<sup>Ø</sup> It is computationally very expensive, which makes it inapplicable for large-scale KBSs.

<sup>Ø</sup> It deals with a limited set of anomalies that can be defined as metapredicates.

Similar ideas have recently been presented in Ref. <sup>w</sup> <sup>x</sup> 1 , where an attempt was made to adopt methods designed for verification of monotonic rule-based systems to non-monotonic systems.

In this article, we advocate the idea that the nature of non-monotonic KBSs leads to a different expression of common types of errors such as inconsistencies, circularities and redundancies, and suggests new types of errors which have no counterpart in monotonic KBSs. To the best of our knowledge, no serious study has been made to identify and characterize errors unique to non-monotonic KBSs. In an attempt to fill this gap, in Section 2 we summarize and adapt for the purposes of KBS verification some results on error taxonomy from machine learning literature, and expand this taxonomy with new types of anomalies which are likely to alter structural or functional properties of a non-monotonic KBS. In Section 3, a brief introduction to non-monotonic systems based on default logic and truth maintenance systems is given, and an example of a non-monotonic theory is presented. Sections 4 and 5 introduce and illustrate the proposed verification technique. In Section 6, we summarize the results of this research and state our plans for future work.

## 2. Error taxonomy in non-monotonic KBs

In Mitchell et al. 10 , the following three types of <sup>w</sup> <sup>x</sup> structural problems in non-monotonic theories are outlined:

1. The incompleteness problem, which results in the fact that some conclusions cannot be inferred because relevant information is missing.

2. The inconsistency problem, which results in generating logical contradictions due to wrong assumptions.

3. The intractability problem, which results in computationally prohibitive deductions.

In Ref. 11 , incompleteness errors are divided <sup>w</sup> <sup>x</sup> into:

<sup>Ø</sup> Errors due to missing knowledge.

<sup>Ø</sup> Errors due to the lack of sufficient detail in relevant knowledge. Similarly, inconsistency errors are divided into:

<sup>Ø</sup> Errors caused by wrong knowledge.

<sup>Ø</sup> Errors caused by wrong assumptions.

Errors due to missing knowledge can be further subdivided into two categories depending on the error indicator:

<sup>Ø</sup> Errors revealed by the existence of irreleÕant rules, i.e., rules which do not contribute to the inference of any final hypothesis.

<sup>Ø</sup> Errors revealed by the existence of unreachable hypotheses.

Errors due to the lack of sufficient detail in relevant knowledge can be subdivided into:

<sup>Ø</sup> Errors revealed by the existence of irreleÕant facts, i.e., facts upon which no final hypothesis depends.

<sup>Ø</sup> Errors revealed by logical and<sup>r</sup>or semantic contradictions detected during verification.

As an instance of the intractability problem, we consider circularities among inference rules. In some cases, circular rules may result in infinite recursions. We also show that circular rule chains in a nonmonotonic theory may cause logical and<sup>r</sup>or semantic contradictions.

Another type of a functional anomaly in nonmonotonic KBSs can be caused by redundant rules if these violate the predictability requirement. According to the predictability requirement, each of the correctly solved test cases should be handled properly by the system in the future; that is, the system should never generate different solutions for the same test case because of potential conflicts among multiple rules that may fire at the same time.

A different class of anomalies unique to nonmonotonic systems are those related to the existence of multiple extensions of a non-monotonic theory. We consider two types of anomalies in this group:

<sup>Ø</sup> Anomalies caused by redundant rules, which are generalizations of existing default rules.

<sup>Ø</sup> Anomalies caused by the existence of comple mentary rules, i.e., rules forcing the same conclusion under contradictory assumptions or data.

Anomalies in this class are hard to detect, because they typically do not violate the structural properties of the knowledge base. However, as it is shown in Section 5.7, such rules may violate the functional correctness of the KBS, and therefore they must be identified and reviewed during the verification process.

## 3. Non-monotonic KB-theories employing default rules

In this article we consider non-monotonic knowledge bases incorporating default rules. The presented verification framework, however, can be applied to knowledge bases employing circumscription 9<sup>w</sup> <sup>x</sup> Žcomputational difficulties associated with this formalism limit its application is real-world KBSs , or . to logic programs although these can be handled by Ž conventional verification techniques such as DIVER <sup>w</sup> <sup>x</sup> 18 ..

Default logic 12 is one of the most popular <sup>w</sup> <sup>x</sup> formalisms for representing non-monotonic theories. It can be implemented by a non-monotonic Truth Maintenance System TMS 4 or with some ap-Ž . <sup>w</sup> <sup>x</sup> proximation by an Assumption-Based TMS 3 . At-<sup>w</sup> <sup>x</sup> tempts to use different types of TMSs in commercial environments for building KBSs started in the mideighties 7 , and today many second generation KBSs <sup>w</sup> <sup>x</sup> and advanced KBS development tools KEE 6 , forŽ <sup>w</sup> <sup>x</sup> example incorporate some kind of a TMS to handle. non-monotonic specifications or to improve the efficiency of the inference process.

Default logic employs two types of inference rules:

<sup>Ø</sup> Deductive or monotonic rules, whose conclu-Ž . sions are logically true beliefs. These have the form $\frac { A { : } } { C }$ , where A is a monotonic prerequisite for conclusion C.

<sup>Ø</sup> Default or non-monotonic rules, which have theŽ . form $\frac { A { : } C } { C }$ . Here conclusion C holds only under the assumption that it is consistent to believe in C.

Introduction of default rules in a KB-theory creates a possibility for logical inconsistencies. One form of a logical inconsistency is manifested in the existence of multiple extensions of a KB-theory. To handle this problem, a good deal of work has been done in finding a way of selecting among different extensions. Most of this work is based on the notion of more specific knowledge 5,15 , or employs the <sup>w</sup> <sup>x</sup> idea presented in Ref. 13 to explicitly introduce<sup>w</sup> <sup>x</sup> priorities between competing rules by using seminormal defaults. The latter are rules of the form $\frac { A { : } C \wedge B _ { 1 } \wedge . . . \wedge B _ { n } } { C }$ , where $C \wedge B _ { 1 } \wedge \ldots \wedge B _ { n }$ is the justification for holding C. Justifications of this form are useful for checking the rule’s consistency. However, once inferred the rule’s conclusion is no longer related to its justification. This may result in generation of semantically wrong conclusions. For example, given Adult Tom , Student TomŽ . Ž . Ž . <sup>k</sup> Priest Tom , and the two semi-normal defaults

$$
\frac {\text { Adult } (x) : \text { Married } (x) \land \neg \text { Student } (x)}{\text { Married } (x)},
$$

$$
\frac {\text { Adult } (x) : \text { Married } (x) \land \neg \text { Priest } (x)}{\text { Married } (x)},
$$

one can infer that Tom is married, although neither students nor priests are married according to the theory.

To a certain extent, this problem is fixed by TMSs where justifications are explicitly stored as a part of belief specification. In this context, default rules are represented as follows:

<sup>Ø</sup> Normal defaults: $( I _ { 1 } , I _ { 2 } , \ldots , I _ { k } ) ( \lnot C ) \to C .$ where $C \colon ( I _ { 1 } , I _ { 2 } , \ldots , I _ { k } ) ( \lnot C )$

<sup>Ø</sup> Semi-normal defaults: $( I _ { 1 } , I _ { 2 } , \ldots , I _ { k } ) ( O _ { 1 } , O _ { 2 } , \ldots ,$ $O _ { n } ) \to C$ , where $C \colon ( I _ { 1 } , \ I _ { 2 } , \ldots , \ I _ { k } ) ( O _ { 1 } , \ O _ { 2 } , \ldots ,$ $O _ { n } )$

Here $I _ { 1 } , \ I _ { 2 } , \ldots , \ I _ { k }$ are the monotonic supporters for conclusion $C ,$ called the ‘IN-list’ of the justification; and $O _ { 1 } , ~ O _ { 2 } , . . . , ~ O _ { n } , ~ \lnot C$ are the non-monotonic supporters for C, called the ‘OUT-list’ of the justification. In both cases, conclusion C holds if all of the rule’s monotonic supporters hold, and none of its non-monotonic supporters hold.

An example of a non-monotonic theory represented in a TMS-format is given below this exampleŽ is extracted from the knowledge base, which was kindly placed by Torsten Schaub at my disposal for the purposes of this research . This example is used . throughout this article to illustrate the proposed verification framework.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Deductive rules
 $R_{1}$ : (kid(x))() → has_toys(x)
 $R_{3}$ : (professor(x))() → academic(x)
 $R_{4}$ : (priest(x))() → academic(x)
Non-monotonic rules: normal defaults
 $R_{5}$ : (student(x))(¬adult(x)) → adult(x)
 $R_{6}$ : (student(x))(employed(x)) → ¬employed(x)
 $R_{7}$ : (student(x))(married(x)) → ¬married(x)
 $R_{9}$ : (academic(x))(¬adult(x)) → adult(x)
Non-monotonic rules: semi-normal defaults
 $R_{2}$ : (adult(x))(professor(x)) → ¬has_toys(x)
 $R_{8}$ : (adult(x))(student(x)) → employed(x)
 $R_{10}$ : (adult(x))(student(x)) → married(x)
 $R_{11}$ : (academic(x))(professor(x)) → ¬employed(x)
 $R_{12}$ : (academic(x))(priest(x)) → has_toys(x).
Input data: professor(x), student(x), kid(x), priest(x).
Final hypotheses: married(x), employed(x), has_toys(x), and their negations.
Semantic constraint: adult(x) ∧ kid(x).
</div>

## 4. Distributed verification revised

The distributed verification method, which has originally been developed for verification of monotonic rule-based KBSs 16 , follows the so-called <sup>w</sup> <sup>x</sup> operationalization approach to KBS verification <sup>w</sup> <sup>x</sup> 8,14 . The underlying idea is to obtain an operational version of the KB-theory by using an alternative inference engine which is known to be correct and complete. During the operationalization process all anomalies hidden in the original KB-theory become explicit and thus easily detectable. To compute the operational version of the KB-theory, the distributed verification method employs the Contradiction-tolerant TMS CTMS 17 . The operationaliza-Ž . <sup>w</sup> <sup>x</sup> tion process consists of the following three steps: iŽ . conversion of the KB-theory into a CTMS-theory; Ž . ii generation of the stable extension of the latter, where all contradictions that the KB-theory implicitly contains are revealed and represented as formulas of a special type; and iii generation of the Ž . operational version of the KB-theory by computing the transitive closure of the formulas comprising the stable extension.

Similar to a non-monotonic TMS, the CTMS has two types of rules called T-rules and U-rules. The former are monotonic rules, while the later behave non-monotonically as a result of the rule revision performed by the CTMS if a logical contradiction is encountered. Although the semantics of U-rules is different from the semantics of default rules, U-rules can be easily adjusted to represent both normal and semi-normal defaults. U-rules have the form $( T _ { 1 } , \dots ,$ $T _ { n } ) ( U _ { 1 } , \dots , \ U _ { m } ) \to A$ , where $T _ { 1 } , \ldots , \ T _ { n }$ are monotonic supporters for A representing the minimum evidence required to consider A as a plausible belief, while $U _ { 1 } , \dots , \ U _ { m }$ are additional arguments for A which, if become true, will increase the plausibility of A. Thus, each U-rule can be viewed as a scheme of plausible rules each instance of which accounts for a subset of U-arguments found to be true. Specific instances are represented by the so-called ‘duplicate rules’ which, in turn, can be:

<sup>Ø</sup> T-duplicates. These have the form $( T _ { 1 } , \dots , \ T _ { n } ,$ $U _ { 1 } , \dots , U _ { m } ) ( ) \to A$ , where $A ^ { t } { : } ( T _ { 1 } , \ldots , T _ { n } , U _ { 1 } , \ldots ,$ $U _ { m } ) ( )$

<sup>Ø</sup> U-duplicates. These have the form $( T _ { 1 } , \dots , \ T _ { n } ,$ $U _ { i _ { 1 } } , \dotsc , U _ { i _ { k } } ) ( \{ U _ { 1 } , \dotsc , \thinspace \thinspace { \cal U } _ { m } \} \setminus \{ U _ { i _ { 1 } } , \dotsc \dotsc , U _ { i _ { k } } \} )  A$ <sup>1</sup> where $A ^ { u } \colon \mathsf { \bar { ( } } T _ { 1 } , \ldots , T _ { n } , U _ { i _ { 1 } } , \ldots , U _ { i _ { k } } \mathsf { ) } ( \{ U _ { 1 } , \ldots , U _ { m } \} \setminus \mathsf { \bar { \Sigma } }$ $\{ U _ { i _ { 1 } } , \dotsc , U _ { i _ { \iota } } \} )$

There is one U-duplicate per each U-argument of the original rule.

Given a non-monotonic KB-theory ²SR, SF, SH, $S C \rangle$ , where SR is a set of monotonic and non-monotonic rules, SF is a set of input data facts , Ž . SH is a set of final hypotheses, and SC is a set of semantic constraints, its conversion into a CTMS-theory ² DB, $R \rangle$ is performed as follows.

Ž . 1 Each fact $F _ { i } \in S F$ is represented as a formula $F _ { i } ^ { t } \mathrm { { : } } ( \mathrm { { ) } } ( \mathrm { { ) } } \in D B$ , each hypothesis $H _ { i } \in S H$ is represented as a formula $H _ { i } ^ { u } \colon ( \mathrm { 0 0 } \in D \tilde { B }$ , and each rule $R _ { i } \in S R$ is represented as a formula $R _ { i } ^ { t } \mathrm { : ( ) ( ) } \in D B$

Ž . 2 Depending on the type of a KB rule, three cases of rule conversion are considered:

Ž .a Monotonic KB rules are translated into CTMS T-rules $( T _ { 1 } , \ldots , T _ { n } , R _ { i } ) ( ) \to H _ { i } .$ , where $T _ { 1 } , \ldots , T _ { n }$ are the premises of the KB-rule, and $R _ { i }$ is the rule itself.

Ž . b Normal defaults are translated into CTMS U-rules $( T _ { 1 } , \dots , T _ { n } , R _ { i } ) ( H _ { i } ) \to H _ { i }$ , where conclusion $H _ { i }$ is the only U-argument.

Ž .c Semi-normal defaults are translated into CTMS U-rules $( T _ { 1 } , \dots , \ T _ { m } , \ R _ { i } ) ( U _ { i _ { 1 } } , U _ { i _ { 2 } } , \dots , U _ { i _ { n } } ) \to H _ { i } ,$ where $\neg U _ { i _ { 1 } } , \dotsc , \dotsc U _ { i _ { n } }$ are the non-monotonic arguments comprising the ‘OUT-list’ of the KB rule.

A complete set of duplicate rules must be generated for each U-rule:

<sup>Ø</sup> For normal defaults:

$$
(T _ {1}, \dots , T _ {m}, H _ {i}, R _ {i}) () \rightarrow H _ {i}.
$$

<sup>Ø</sup> For semi-normal defaults:

$$
\begin{array}{l} (T _ {1}, \ldots , T _ {m}, U _ {i _ {1}}, R _ {i}) (U _ {i _ {2}}, \ldots , U _ {I _ {n}}) \to H _ {i}, \\ (T _ {1}, \ldots , T _ {m}, U _ {i _ {1}}, U _ {i _ {2}}, R _ {i}) (U _ {i _ {3}}, \ldots , U _ {i _ {n}}) \to H _ {i}, \end{array}
$$

$$
(T _ {1}, \dots , T _ {m}, U _ {i _ {1}}, \dots , U _ {i _ {n}}, R _ {i}) () \rightarrow H _ {i}.
$$

Ž . 3 Each semantic constraint $S C _ { i } \in S C$ is represented as a formula $C _ { S C _ { i } } ^ { u } \colon ( X _ { 1 } , \ldots , X _ { n } ) ( C _ { S C _ { i } } )$ , which is not an element of the initial DB, but is added to it only if all of its premises, $X _ { 1 } , \ldots , X _ { n }$ , hold.

Provided that the KB-theory can be converted into a CTMS-theory by means of the described procedure, the first step of the verification process consists in generating the operational version of the KB-theory. The main assumption behind the operationalization approach is that all of the hidden in the KB-theory anomalies can be revealed if the entire set of input data is enabled simultaneously. In non-monotonic theories, this assumption may explicate some logical contradictions that can be successfully handled by the belief revision facility typically imple- Ž mented by a dependency-directed backtracking procedure . It is easy to see that belief revision is. capable of handling contradictions, where the culprit is a datum serving as a non-monotonic supporter in a semi-normal default. These contradictions can be removed from consideration if the input data set is divided into maximal input sets MISs consistentŽ . with respect to the data serving as non-monotonic supporters in semi-normal defaults.

To illustrate this step, consider the example theory introduced in Section 3. There are three input data serving as non-monotonic supporters in seminormal defaults: professorŽ . Ž .x , student x , and priestŽ . x . Therefore, eight MISs containing different combinations of these data must be considered. Each of these MISs originates an independent operationalization process, which is carried out in the same way as for monotonic theories. That is, the stable extension of the corresponding CTMS-theory is computed by repeatedly applying the CTMS-rules until no more rules can fire, and then the operational theory is generated by computing the transitive closure of the formulas comprising the stable extension for Ž details, see Ref. 16 . The resulting theory, called<sup>w</sup> <sup>x</sup>. the ‘grounded stable extension’, consists of formulas of the following three types:

$$
\begin{array}{l} \bullet H _ {i} ^ {t}: (F _ {1}, \ldots , F _ {i}, R _ {1}, \ldots , R _ {j}) (). \\ \bullet H _ {i} ^ {u}: (F _ {1}, \ldots , F _ {i}, R _ {1}, \ldots , R _ {j}) (\neg F _ {k}, \ldots , \neg F _ {m}, \\ \neg H _ {p}, \ldots , \neg H _ {s}). \\ \bullet C _ {F _ {i}, F _ {j}} ^ {u}: (F _ {i}, F _ {j}) (C _ {F _ {i}, F _ {j}}). \end{array}
$$

Here ${ \dot { F } } _ { 1 } ^ { ' } , \dots , F _ { i }$ is called the data set of the formula, $\neg F _ { k } , \dotsc , \neg F _ { m } , \neg H _ { p } , \dotsc , \neg H _ { s }$ is called the assumption set, and $R _ { 1 } , \ldots , R _ { j }$ is called the rule set. $C _ { F _ { i } , F _ { j } }$ represents a logical or semantic contradiction between formulas with heads $F _ { i }$ and $F _ { j }$ Žas a special case, $F _ { i } = \neg F _ { i } )$

By analyzing individual formulas or group of formulas from the grounded stable extensions, different types of anomalies and errors in the original KB-theory can be revealed by means of the verification tests presented next.

## 5. Verification tests for non-monotonic KB-theories

Verification process involves a number of tests intended to detect and correct the following types of anomalies and errors in non-monotonic KB-theories.

<sup>Ø</sup> Logical inconsistencies caused either by wrong assumptions or wrong knowledge. All cases of logical inconsistencies are revealed by looking for formulas representing logical contradictions in each of the grounded stable extensions.

<sup>Ø</sup> Structural incompleteness caused by missing knowledge and<sup>r</sup>or lack of sufficient detail in the relevant knowledge. All cases of structural incom pleteness are revealed by looking for final hypotheses which cannot be reached by a given MIS, or by identifying irrelevant rules and irrelevant facts i.e.,Ž rules and facts which do not participate in any data or rule set of the formulas comprising grounded stable extensions ..

<sup>Ø</sup> Circular rule chains causing infinite recursions or logical and<sup>r</sup>or semantic contradictions. These are detected by looking for formulas whose heads or their negations are also encountered in their T-sets. It is important to note that formulas inferred by $T _ { - }$ duplicates of normal defaults are by definition of this type. This is why they must be recognized and treated as a special case.

<sup>Ø</sup> Redundant rules which may or may not constitute an error in the KB-theory depending on the type of redundancy, and whether or not alternative hypotheses are allowed. There are several cases of rule redundancies in non-monotonic theories: i a deduc-Ž . tive rule is subsumed by a normal default; ii aŽ . deductive rule is subsumed by a semi-normal default; iii a normal default is subsumed by a semi- Ž . normal default; and iv redundancy among rules of Ž . the same type.

A special case of rule redundancy in non-monotonic theories is the existence of complementary rules. Such rules cause the same conclusion to be inferred by inconsistent MISs, which clearly indicate a performance error.

All cases of rule redundancy can be identified by looking for formulas with the same head. To detect complementary rules, this procedure must be performed over all grounded stable extensions at the same time.

Next, we introduce the verification tests in more detail, and illustrate them by means of the example theory.

## 5.1. Test for logical inconsistencies due to wrong assumptions

Assume that instead of $R _ { 8 }$ , the example theory contains the follow ing norm al default: $R _ { 8 } ^ { * } : ( \mathrm { a d u l t } ( x ) ) ( \neg \mathrm { e m p l o y e d } ( x ) ) \to \mathrm { e m p l o y e d } ( x )$

Then, the grounded stable extension originated by the maximal input set containing professorŽ . x , studentŽ . Ž . Ž . x , priest x , and kid x contains the following logical contradiction: $C _ { \mathrm { e m p l o y e d } } ^ { \mathrm { u } } \mathrm { : ( e m p l o y e d ( \it x ) , \it \mathrm { \Omega \mathrm { \sim } e m \mathrm { - } } }$ Ž . ployed x , $R _ { 6 } , R _ { 8 } ^ { * } ) ( C _ { \mathrm { e m p l o y e d } } )$

This contradiction can be resolved if one of the two normal defaults, $R _ { 6 }$ or $R _ { 8 } ^ { * }$ , is converted into a semi-normal default by adding one of the monotonic supporters of the other default as its non-monotonic Ž . supporter. We can arbitrary choose to modify $R _ { 8 } ^ { * }$ which becomes: $R _ { 8 } \colon ( \mathrm { a d u l t } ( x ) ) ( \mathrm { s t u d e n t } ( x ) ) \to$ employedŽ . x .

That is, the detected inconsistency is resolved by specializing a normal default, $R _ { 8 } ^ { * }$ , into a semi-normal default, $R _ { 8 } { \mathrm { . } }$ , thus preventing it from firing when studentŽ . x is given.

## 5.2. Test for logical inconsistencies due to wrong knowledge

Assume that the following rule is added to the e x a m p le th e o ry : R : p ro fe s s o r Ž Ž ..Ž. x ™ <sup>!</sup>has\_toysŽ . x .

Then, grounded stable extensions originated by maximal input sets where both professorŽ . x and <sup>!</sup>priestŽ . x hold, contain the following contradiction: $C _ { \mathrm { h a s \_ t o y s } } ^ { \mathrm { u } } \mathrm { ; } ( \mathrm { p r o f e s s o r } ( x ) , R _ { 3 } , R _ { 1 2 } , R _ { i } ) ( \mathrm { p r i e s t } ( x )$ $C _ { \mathrm { h a s \_ t o y s } } ) _ { \cdot }$

The detected contradiction is caused by the inconsistency between $R _ { 3 }$ and $R _ { 1 2 } ^ { \phantom { } } .$ , on the one hand, and $R _ { i }$ on the other hand. Under the ‘minimum change rationale, we can assume that $R _ { i }$ represents semantically wrong knowledge, and it must be considered for deletion from the KB-theory.

## 5.3. Test for structural incompleteness due to missing knowledge

Assume that $R _ { 7 }$ is missing from the example theory. Then the grounded stable extension originated by the maximal input set containing <sup>!</sup>professorŽ . Ž . Ž . Ž . x , student x , <sup>!</sup>priest x , kid x consists of th e fo llo w in g fo rm u la s: $D B _ { G } \ = \ D B \ \cup$  Ž .<sup>t</sup> Ž Ž .has\_toys x : kid x , $R _ { 1 } ) ( ) _ { : }$ Ž .<sup>t</sup> , adult x : studentŽ Ž . x , $R _ { 5 } ) ( ) , \quad \neg$ Ž . <sup>t</sup> em p lo y ed x : stu d en tŽ Ž .x , $R _ { 6 } ) ( )$ Ž .<sup>t</sup> Ž Ž . .Ž. <sup>!</sup>has\_toys x : adult x , R , $C _ { \mathrm { h a s \_ t o y s } } ^ { \mathrm { u } } \mathrm { : ( k i d ( } x \mathrm { ) }$ adultŽ .x , $R _ { 1 } , R _ { 2 } ) ( C _ { \mathrm { h a s \_ t o v s } } ) \}$

Notice that contradiction $C _ { \mathrm { h a s \_ t o y s } }$ is caused by the violation of a declared semantic constraint, which is why this contradiction does not indicate a structural error in the KB-theory.

One of the final hypotheses, marriedŽ . x , is not contained in $D B _ { G }$ neither is its negation, <sup>!</sup>marriedŽ . x . This indicates that the KB-theory is incomplete. To reveal the source of the problem, the verification procedure examines all of the rules whose conclusion is either the missing final hypothesis or its negation. The only such rule here is: R : adult Ž Ž ..Ž Ž .. Ž . x student x ™ married x .

Assuming that this rule is semantically correct, a conclusion can be drawn that students are typically not married. This knowledge can be represented as t h e f o l l o w i n g n o r m a l d e f a u l t : Ž Ž ..Ž Ž .. Ž . student x married x ™ <sup>!</sup>married x ,

If this new rule is added to the KB-theory, then <sup>!</sup>marriedŽ . Ž . x can be inferred given <sup>!</sup>professor x , studentŽ . Ž . Ž . x , <sup>!</sup>priest x , and kid x .

## 5.4. Test for structural incompleteness due to the lack of sufficient detail in releÕant knowledge

This type of incompleteness arises if the initial set of facts, SF, does not contain all of the data required during the inference process. If a missing datum serves as a non-monotonic supporter in a semi-normal default, then two different extensions of SF must be considered:

<sup>Ø</sup> An extension originated by SF with the missing datum added.

<sup>Ø</sup> An extension originated by SF with the negation of the missing datum added.

It is easy to see that the KB-theory will infer contradictory conclusions depending on which of the two extensions is considered. Such a contradiction, however, will automatically go away if the missing fact is added to SF. This case of semantic inconsistency can be handled by the KBS control mechanism if heuristic knowledge for ranking different extensions is available. This is why an incompleteness of this type does not indicate a performance error, but rather an anomaly lack of required data which canŽ . be fixed by completion of the input data set.

In our example, if input datum priestŽ . x is missing, depending on whether priestŽ . Ž . x or <sup>!</sup>priest x is assumed, two different hypotheses, <sup>!</sup>has\_toysŽ . x and has\_toysŽ . x , will be inferred. Adding the missing datum to the initial data set will solve the detected problem.

## 5.5. Test for circular rule chains

Consider the following hypothetical rules:

$$
\begin{array}{l} R _ {i}: (\text {adult} (x)) (\text {student} (x)) \to \text {married} (x) \\ R _ {i + 1}: (\text {married} (x)) () \to \neg \text {kid} (x) \\ R _ {i + 2}: (\neg \text {kid} (x)) () \to \text {student} (x) \\ R _ {i + 3}: (\text {student} (x)) () \to \neg \text {married} (x). \end{array}
$$

Assume that adultŽ . Ž . x and student x are both declared as input facts, but there is no information about whether x is a student or not. Obviously, there are two MISs in this case, which contain adultŽ . x , studentŽ . Ž . Ž . x and adult x , <sup>!</sup>student x , respectively. Notice that the grounded stable extension originated Ž .<sup>t</sup> by the former MIS will contain <sup>!</sup>married x : stu-Ž dentŽ .x , $R _ { i + 3 } ) ( )$ , which is the expected conclusion. The grounded stable extension originated by the o th er M IS w ill co n tain th e fo rm u la, Ž .<sup>t</sup> student x : adultŽ Ž . Ž . x , <sup>!</sup>student x , $R _ { i } , \quad R _ { i + 1 } ,$ $R _ { i + 2 } ) ( )$ , indicating that the underlying theory is intractable, because studentŽ . x can be inferred only if <sup>!</sup>studentŽ . x holds, which is impossible.

Let us consider how the KB-theory behaves in this case. Assuming that studentŽ . x does not hold, $R _ { i }$ will fire, thus generating marriedŽ . x . This causes $R _ { i + 1 }$ to fire generating <sup>!</sup>kidŽ . x , which in turn causes $R _ { i + 2 }$ to fire generating studentŽ . x . The latter invalidates the already inferred conclusion marriedŽ . Ž . x , which in turn invalidates <sup>!</sup>kid x and studentŽ . Ž . x , thus causing married x to be inferred again. That is, $R _ { i } , \ R _ { i + 1 }$ , and $R _ { i + 2 }$ form a cycle which makes the KB-theory intractable. The verification procedure recognizes such errors by looking for formulas which depend on their own negations.

Circular rule chains may also cause logical and<sup>r</sup>or semantic contradictions. Assume that the following rule is added to the exam ple theory: $R _ { j }$ : has Ž Ž ..Ž. Ž . \_toys x ™ professor x .

Given a MIS, where <sup>!</sup>professorŽ . x holds, the Ž .<sup>t</sup> formula professor x : hasŽ Ž ..Ž. \_toys x will be inferred by $R _ { j }$ causing a logical contradiction. On the other hand, given kidŽ . Ž x which participates in all MISs , this would also constitute a semantic contra-. diction, if there were a semantic constraint professorŽ . Ž . x <sup>n</sup> kid x . Notice that the belief revision facility will not recognize this contradiction, because <sup>!</sup>professorŽ . x is not explicitly specified as an input datum.

## 5.6. Test for redundant rules

In most cases, redundant rules do not violate structural properties of a KB-theory. Sometimes, however, they may lead to alternative development of the inference process, thus violating the predictability requirement.

The test for redundant rules is applied to the rule sets of the formulas with the same head, and it checks if their data sets are identical, or one data set is a subset of another. For example, assume that: $R _ { k } { \mathrm { : ( p r o f e s s o r ( } } x { \mathrm { ) ) ( ) } } \to \hom ⨏ \operatorname { t o y s } ( x )$ is added to the example theory. Then, the following two formulas will belong to grounded stable extensions originated by maximal input sets containing both professorŽ . x and <sup>!</sup>priestŽ . x :

has\_toysŽ . Ž Ž . .Ž. x : professor x , R ,

$$
\text { has\_toys } (x): (\text { professor } (x), R _ {3}, R _ {1 2}) (\neg \text { priest } (x)).
$$

It follows from here that either $R _ { k }$ or $R _ { 3 }$ and<sup>r</sup>or $R _ { 1 2 }$ are redundant. Note that two of these rules, $R _ { 3 }$ and $R _ { k }$ , are deductive rules, while $R _ { 1 2 }$ is a semi-normal default. From a knowledge representation point of view, monotonic rules and normal defaults are weaker than semi-normal defaults. Therefore, it is reasonable to assume that monotonic rules and normal defaults are better candidates for deletion in case of rule redundancy than semi-normal defaults. Whether or not a redundant rule must be deleted from a KB-theory depends on a particular application.

## 5.7. Test for complementary rules

This test is a special case of the test for redundant rules, where all grounded stable extensions are searched for formulas with the same head simultaneously. These formulas are then searched for complementary rules, i.e., rules which force the same hypothesis under contradictory assumptions or data. To identify such rules, both T-sets and U-sets of the formulas with the same head are examined for monotonic and<sup>r</sup>or non-monotonic supporters with opposite signs.

Consider, for example, the following hypothetical rules:

$$
\begin{array}{l} R _ {l}: () (\text {priest} (x)) \to \text {has\_toys} (x) \\ R _ {l + 1}: (\text {priest} (x)) () \to \text {adult} (x) \\ R _ {l + 2}: (\text {adult} (x)) () \to \text {has\_toys} (x) \end{array}
$$

Given priestŽ . Ž . x , conclusion has\_toys x will be inferred by means of $R _ { l + 1 }$ and $R _ { l + 2 } .$ Given <sup>!</sup>priestŽ . Ž . x the same conclusion, has\_toys x , will be inferred by means of $R _ { l }$ . Notice that this error does not violate structural properties of the KB-theory. However, it clearly points a performance error, which can be detected only if different extensions are examined simultaneously.

## 6. Conclusion

In this paper, we argue that non-monotonic KBSs must undergo quality assurance procedures for the following two reasons:

1. Belief revision, if such is provided, cannot always guarantee the structural correctness of the knowledge base; moreover, in certain cases it may introduce new semantic errors in the revised theory.

2. Non-monotonic theories may have multiple extensions, and some types of functional errors which do not violate structural properties of a given extension, are hard to detect without testing the overall performance of the KBS.

We have presented an extension of the distributed verification method 16 meant to perform verifica-<sup>w</sup> <sup>x</sup> tion on non-monotonic knowledge bases incorporating default rules. The extended conversion procedure has been introduced to account for normal and semi-normal defaults in non-monotonic KB-theories. Verification tests presented in Section 5 are intended to detect two classes of anomalies in non-monotonic KB-theories: i structural anomalies which manifestŽ . themselves within a given extension such as logicalŽ inconsistencies, structural incompleteness, and intractabilities caused by circular rule chains , and ii . Ž . functional anomalies related to the overall performance of the KBS such as the existence of comple-Ž mentary rules and some types of rule subsumptions ..

The presented verification framework has been tested on relatively large example theories, and the initial results demonstrate its usefulness and efficiency. It is our hope that we will be able to test it on a real-world KBS to examine its limitations and expand the existing set of verification tests with new ones. Another direction of our future work is the implementation of an automated refinement procedure to enhance not only the verification process, but the overall development of a KBS as well.

## Acknowledgements

This research has been partially supported by a CSU-AAUP research grant. Many thanks to Charles Neville for his useful suggestions.

## References

<sup>w</sup> <sup>x</sup> 1 G. Antoniou, Verification and correctness issues for nonmonotonic knowledge bases, in: Proc. European Symposium on the Validation and Verification of Knowledge-Based Systems Eurovav-95 , 1995, pp. 141–153.Ž .

<sup>w</sup> <sup>x</sup> 2 C.L. Chang, R.A. Stachowitz, J.B. Combs, Validation of nonmonotonic knowledge-based systems, in: A. Dollas, W.T. Tsai, N.G. Bourbakis Eds. , Proc. 2nd International Confer-Ž . ence on Tools for Artificial Intelligence TAI-90 , 1990, pp.Ž . 776–782.

<sup>w</sup> <sup>x</sup> 3 J. de Kleer, An assumption-based TMS, Artificial Intelligence Netherlands 28 2 1986 127–162.Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 J. Doyle, A truth maintenance system, Artificial Intelligence Ž . Ž . Netherlands 12 1979 231–272.

<sup>w</sup> <sup>x</sup>5 D. Etherington, Reasoning with incomplete information. Research Notes in Artificial Intelligence, Pitman Publ., 1988.

<sup>w</sup> <sup>x</sup> 6 R. Fikes, T. Kehler, The role of frame-based representation in reasoning, Communications of the ACM 28 9 1985Ž . Ž . 904–920.

<sup>w</sup> <sup>x</sup> 7 R.E. Filman, Reasoning with worlds and truth maintenance in a knowledge-based programming environment, Communications of the ACM US 31 4 1988 382–401.Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 A. Ginsberg, Knowledge-base reduction: a new approach to checking knowledge bases for inconsistency and redundancy,

in: Proc. 7th National Conference on Artificial Intelligence Ž . AAAI 88 , Vol. 2, 1988, pp. 585–589.

<sup>w</sup> <sup>x</sup> 9 J. McCarthy, Applications of circumscription to formalizing common-sense knowledge, Artificial Intelligence Nether-Ž lands 28 1986 89–116.. Ž .

<sup>w</sup> <sup>x</sup> 10 T.M. Mitchell, R.M. Keller, S.T. Kedar-Cabelli, Explanation-based generalisation: a unifying view, Machine Learning Netherlands 1 1986 47–80.Ž . Ž .

11 S. Rajamoney, G. DeJong, The classification, detection and handling of imperfect theory problems, in: Proc. AAAI 1988, 1988, pp. 205–207.

<sup>w</sup> <sup>x</sup> 12 R. Reiter, A logic for default reasoning, Artificial Intelligence Netherlands 13 1980 81–132.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 R. Reiter, G. Criscuolo, On interacting defaults, in: Proc. International Joint Conferences on Artificial Intelligence Ž . IJCAI’81 , 1981, pp. 270–275.

<sup>w</sup> <sup>x</sup> 14 M.-C. Rousset, On the consistency of knowledge bases: the COVADIS system. Computational Intelligence Canada , 4Ž . Ž . 2 1988, pp. 166–170. Also in: ECAI 88, Proc. European Conference on AI, Munich, August 1–5, 1988, pp. 79–84.

<sup>w</sup> <sup>x</sup> 15 D. Touretzky, The Mathematics of Inheritance. Research Notes in Artificial Intelligence, Pitman Publ., 1986.

<sup>w</sup> <sup>x</sup> 16 N. Zlatareva, Distributed verification: a new formal approach for verifying knowledge-based systems, in: J. Liebowitz Ed. , Ž . Expert Systems World Congress Proceedings, Vol. 2, 1991, Pergamon Press, New York, pp. 1021–1029.

<sup>w</sup> <sup>x</sup> 17 N. Zlatareva, CTMS: a general framework for plausible reasoning, Int. J. Expert Syst.: Res. Appl. 5 4 1992 Ž . Ž . 229–247.

<sup>w</sup> <sup>x</sup> 18 N. Zlatareva, A. Preece, An effective logical framework for knowledge-based systems verification, Int. J. Expert Syst.: Res. Appl. 7 3 1994 239–260. Ž . Ž .

Neli P. Zlatareva is an Associate Professor of Computer Science at Central Connecticut State University in New Britain, Connecticut. She received her MS in Computer Science with the highest honor from the Higher Institute of Transport Engineering in Moscow, Russia, and her PhD in Computer Science from the Higher Institute of Mechanical and Electrical Engineering in Sofia, Bulgaria. She also holds a Habilitation Degree in Artificial Intelligence from the Bulgarian Academy of Sciences. Zlatareva’s research interests include quality assurance of Knowledge-Based Systems, knowledge base refinement and incremental learning, non-monotonic reasoning and truth maintenance systems. She is an author<sup>r</sup>co-author of more than 60 publications in these areas.
