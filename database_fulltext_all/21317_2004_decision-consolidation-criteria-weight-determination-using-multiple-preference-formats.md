---
otero_id: 21317
otero_key: "YSAM59E4"
title: "Decision consolidation: criteria weight determination using multiple preference formats"
authors: "Quan Zhang; Jason C.H. Chen; P.Pete Chong"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00094-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision consolidation: criteria weight determination using multiple preference formats

Quan Zhang<sup>a,1</sup>, Jason C.H. Chen<sup>a,</sup>\*, P. Pete Chong b,2

<sup>a</sup> School of Business Administration, Gonzaga University, 502 E. Boone, Spokane, WA 99258, USA <sup>b</sup> Department of Finance, Accounting, and CIS, College of Business, University of Huston—Downtown, One Main Street, Houston, TX 77002, USA

Received 29 September 2002; received in revised form 12 June 2003; accepted 13 June 2003 Available online 9 August 2003

## Abstract

In multiple criteria decision making (MCDM), decision makers (DMs) always give preferences information on alternatives, criteria or decision matrices. Since the DMs may have diverse cultural and educational background and value systems, their preference would be expressed in different ways. This is especially true in cyberspace. In this study, the DMs are asked to express their preferences on a variety of criteria using any one of the following preference formats: preference orderings, utility values, multiplicative preference relation, selected subset, fuzzy selected subset, normal preference relation, fuzzy preference relation, linguistic terms, and pairwise comparison. In addition, we propose a uniformity method and an aggregating method to provide both convenience and accuracy in generating the final outcome and higher DM satisfaction. Finally, the validity of using multiple preference formats in criteria weight determination is verified through an experiment. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Multiple criteria decision making; Criterion weights; Preference format; Multiplicative preference relation; Geometric means aggregation

## 1. Introduction

Decision making is a knowledge-intensive activity with knowledge as its raw material, work in progress, by-product, and finished good [9]. Multiple criteria decision making (MCDM) refers to making preference decisions (e.g., evaluation, prioritisation, selection) on available alternatives in terms of multiple, usually conflicting, criteria. People have certain tendency in MCDM. For example, some may prefer to use a decision matrix. Using multiple decision makers (DMs) in the decision process is often preferred than a single DM [6,10,11,13– 15] to avoid bias and minimize partiality [14].

As Internet technologies are adopted to facilitate communications among a wide variety of stake holders [9], traditional methods for MCDM problems are now facing new challenges in the cyberspace environment where decision making may involve multiple

DMs sparsely distributed all over the world. Furthermore, DMs with different cultural and educational background can now express their opinion using their preferred formats in decision making [6,10,23].

In fact, different preference formats are necessary in some MCDM problems. For example, in student Information Systems project assessment [13], current preference formats are not sufficient to support group decision making in the electronic business environment, especially when the information available is fuzzy or uncertain [6,10]. At least, linguistic terms, together with other preference formats, should be provided to DMs for opinion expression, as proposed in Chiclana et al. [6] and Herrera et al. [10].

This study considers the situation where preference information on criteria is given for multiple DMs in different formats. These preferences are then used to determine the weights of the criteria. The situation of making decision after gaining consensus of the group of DMs is not considered in this study. Sometimes, the group is too large that it is difficult for the group members to negotiate, lobby or compromise with each other. The group’s opinions can be obtained under a semantic such as ‘‘most’’, ‘‘as many as possible’’, ‘‘at least half’’, etc. To express their preferences, the following preference information formats are provided to the DMs: preference orderings, utility value, multiplicative preference relation, selected subset, fuzzy selected subset, normal preference relation, fuzzy preference relation, linguistic terms, and pairwise comparison. The preference formats are transformed into multiplicative preference relation, respectively. After the preference aggregation and exploitation process, the weights of the criteria can be obtained.

The proposed mechanism allows DMs to express their opinions easily and results in a high satisfaction level on both the decision-making process and outcome. This proposition is justified through two field experiments where groups of students were asked to decide the weights of the criteria for evaluating their coursework assignments and course performances. The results validate the proposition. Furthermore, we believe that the way to obtain the weights of criteria obtained can be applied to other similar situations.

Section 2 of this paper briefly surveys relevant theories and methods. In Section 3, we propose an approach to uniform, aggregate and exploit multiple preference formats. In Section 4, we present the experimental result that validates the superiority of multiple preference formats in determining criterion weights in terms of user satisfaction level of both the decision-making process and the decision outcome. Two experiments are conducted to justify the use of multiple preference formats in determining weights of criteria. Finally, Section 5 is the conclusion.

## 2. Literature review

Since 1970, MCDM has been a promising and important field of study with many practical applications [3,22]. Traditional MCDM methods have been extended to support the fuzzy decision making. Fuzzy MCDM methods have found many practical applications in the real world [3,4,6]. Usually, linguistic terms or variables are used to model and solve fuzzy MCDM problems. Linguistic terms have been found intuitively easy to be used in expressing the subjectivity and imprecision of DMs’ assessments [16,20,]. In addition, linguistic terms can be used to express DMs’ subjective judgments in order to reduce their cognitive burden in the assessment process. They can facilitate the human rating feelings. Linguistic terms can be better modeled by fuzzy numbers, such as triangular fuzzy numbers [16,23]. At the same time, the use of preference information in different formats has attracted researchers [6,10].

The cyber-economy requires that business be operated with virtual organizations and that decision making be in this context. The cyber-economy will require new and advanced forms of decision support [2]. The traditional research has their limitations in the group decision making under the virtual environment. Chiclana et al. [6] propose the use of three criteria on alternatives, known as preference orderings, utility value, and fuzzy preference relation. Preference orderings and utility value formats are transformed into fuzzy preference relation, respectively. The uniformed preference information is aggregated into a collective fuzzy preference relation by adopting the ordered weighted average (OWA) operator based on the concept of fuzzy majority. Given the collective fuzzy preference relation, the alternative selection process is conducted by calculating the quantifier-guided dominance degree (QGDD) and the quantifier-guided nondominance degree (QGNDD) for each alternative. The

QGDD and QGNDD of each alternative are also calculated by using OWA operator based on the concept of fuzzy majority. However, the fuzzy majority-guided OWA operator cannot be used to determine the relative importance of the alternatives.

With multiplicative preference relation as the basic preference format, Herrera et al. [10] used ordered weighted geometric (OWG) operator to aggregate three formats of preference information: preference orderings, utility value, and multiplicative preference relation. The former two formats of preference information are transformed into the last one, respectively. Based on the fuzzy majority concept with fuzzy linguistic quantifier, OWG operator is used to aggregate the unified preference information. Furthermore, based on the aggregation result and the concept of fuzzy majority, the quantifier-guided dominance degree (MQGDD) and the quantifier-guided nondominance degree (MQGNDD) of each alternative are used to select the most desirable alternative(s).

With the support of fuzzy set theory [16,20], in this study, we use an extension of the current approaches to aggregate multiple DMs’ preference information in different formats. We also make use of the multiplicative preference relation and other formats of preference information expression. Multiple preference formats are then transformed and aggregated into multiplicative preference relation. Finally, based on the collective multiplicative preference relation, weighted geometric means aggregation method is used to determine the relative importance of the subjects considered.

## 3. The proposed approach

To facilitate describing the proposed approach, the following assumptions and notations are used:

 The alternatives are known. Let $S { = } \{ S _ { 1 } , S _ { 2 } , . . . , S _ { m } \}$ denote a discrete set of m ( <sub>z</sub> 2) possible alternatives.

 The criteria are known. Let $C { = } \{ C _ { 1 } , ~ C _ { 2 } , . ~ . ~ . , ~ C _ { n } \}$ denote a set of $n \ ( \geq 2 )$ criteria. The criteria are assumed additively independent.

 The vector of criterion weights is unknown. Let $w { = } ( w _ { 1 } , ~ w _ { 2 } , . ~ . ~ . , ~ w _ { n } ) ^ { T }$ be the vector of criterion weights, where $\textstyle \sum _ { j = 1 } ^ { n } w _ { j } = 1 , w _ { j } \geq 0 , j = 1 , \dotsc . n ,$ , and $w _ { j }$ denotes the weight of criterion $C _ { j } .$ Usually, w should be determined in the course of decision making.

 The decision makers (DMs) are known. Let $E { = } \{ e _ { 1 }$ $e _ { 2 } , . . . , e _ { K } \}$ denote the set of K ( <sub>z</sub> 2) DMs.

The proposed approach consists of three steps: (1) the transformation of preference formats into multiplicative preference relation, (2) the aggregation of the multiplicative preference relations from multiple DMs, and (3) the determination of the weights for criteria.

3.1. Transforming preference formats into multiplicative preference relation

In this study, the uniform preference format is multiplicative preference relation [10]. The ways to transform different preference formats into a single one are shown below.

(0) Multiplicative preference relation or pairwise comparison. DMs’ preferences on criteria can be described by a positive preference relation. The intensity of preference is measured using a ratio scale, such as Saaty’s [17] scale of ‘‘1 to $9 ^ { \ast }$ in which ‘‘1’’ indicates indifference between two subjects while ‘‘9’’ indicates that one subject is absolutely preferred to the other. The intermediate preferences are expressed in $^ { \dots } 2 ^ { \prime \prime } , \ ^ { \dots } 3 ^ { \prime \prime } , \dots , \ ^ { \dots } 8 ^ { \prime \prime }$ . The preference relation matrix is assumed multiplicatively reciprocal [17].

(1) Preference orderings or an ordered vector. Let $O ^ { k } { = } ( o ^ { k } ( 1 ) , . . . , o ^ { k } ( n ) )$ be an ordered vector used by a DM $e _ { k } ( e _ { k } \in E ,$ defined above) to express his/her preference on criteria $[ 6 , 1 0 ] . o ^ { k } ( \cdot )$ is a permutation function over the index set $\{ 1 , . . . , n \}$ and $o ^ { k } ( i )$ represents the ranking position of criterion $C _ { i } , i = 1 , . . . , n .$ . Criteria are ranked from the best to the worst.

Herrera et al. [10] discuss the methods for transforming an ordered vector into multiplicative preference relation. Commonly, the preference orderings $O ^ { k }$ can be transformed into multiplicative preference relation on the criteria $C _ { i }$ and $C _ { j }$ as follows [10]:

$$
p _ {i j} ^ {k} = 9 ^ {u _ {i} ^ {k} - u _ {j} ^ {k}}, \quad i, j = 1, \dots , n.\tag{1}
$$

In this equation, $u _ { i } ^ { k } { = } \nu ( n - o ^ { k } ( i ) )$ and $u _ { j } ^ { k } { = } \nu ( n - o ^ { k } ( j ) )$ are utility values associated with criteria $C _ { i }$ and $C _ { j } ,$ respectively, obtained by considering the effect of an increasing function v, such as $u _ { i } ^ { k } { = } ( n - o ^ { k } ( i ) ) / ( n - 1 )$

(2) Utility value or a utility vector. Let $U ^ { k } { = } ( u _ { 1 } ^ { k } ,$ $u _ { 2 } ^ { k } , . . . , u _ { n } ^ { k } )$ be a utility vector provided by a DM $e _ { k } ,$ $e _ { k } { \in } E ,$ where $u _ { i } ^ { k } { \in } [ 0 , 1 ] , \ i = 1 , . . . , n$ and ${ \bf \chi } _ { u _ { i } ^ { k } } ^ { \dag k }$ represents the utility value given by $e _ { k }$ to criterion $C _ { i } .$

Again, Herrera et al. [10] discussed the methods for transforming a utility vector into multiplicative preference relation. The utility vector $U ^ { k } { = } ( u _ { 1 } ^ { \hat { k } } , u _ { 2 } ^ { k } { \ldots } ,$ $u _ { n } ^ { k } )$ can be transformed into multiplicative preference relation on criteria $C _ { i }$ and $C _ { j }$ as follows [10]:

$$
p _ {i j} ^ {k} = \frac {u _ {i} ^ {k}}{u _ {j} ^ {k}}, \quad i, j = 1, \dots , n.\tag{2}
$$

(3) A vector of linguistic terms on $C .$ Let $L ^ { k } { = } ( l _ { 1 } ^ { k }$ $l _ { 2 } ^ { k } , . . . , l _ { n } ^ { k } )$ be a linguistic term vector given by a DM $e _ { k } ,$ $e _ { k } { \in } E$ . The notion $l _ { i } ^ { k }$ represents the linguistic evaluation given by $e _ { k }$ to criterion $C _ { i } , i = 1 , . . . , n , e _ { k } { \in } E$

Suppose two criteria $C _ { i }$ and $C _ { j }$ are awarded linguistic terms $l _ { i } ^ { k } { = } ( u _ { i } , \alpha _ { i } , \beta _ { i } )$ and $l _ { j } ^ { k } { = } ( u _ { j } , \alpha _ { j } , \beta _ { j } )$ , respectively [20,16]. Linguistic terms can be mapped into crisp values using several methods [13,16,23]. For simplicity, the following function is used in this study to transform $l _ { i } ^ { k } { = } ( u _ { i } , \alpha _ { i } , \beta _ { i } )$ and $l _ { j } ^ { k } { = } ( u _ { j } , \alpha _ { j } , \beta _ { j } )$ into multiplicative preference relation on criteria $C _ { i }$ and $C _ { j } .$

$$
p _ {i j} ^ {k} = 9 ^ {u _ {i} - u _ {j}}, \quad i, j = 1, \dots , n.\tag{3}
$$

(4) A selected subset of C. Let $\bar { C } { = } \{ C _ { i { \_ } 1 } , \ C _ { i { \_ } 2 } { , \ldots } ,$ $C _ { i \_ t } \}$ be a selected subset of C used by a DM $\textstyle e _ { k } , e _ { k } \in E ,$ to express his/her preference on part of the criteria. $\bar { C } { \subset } C , \ i \_ t { < } n$ . Criteria in $\bar { C }$ are equivalent to each other and dominate those on the left of C. The criteria in $C / \bar { C }$ are also equivalent to each other [23].

Given the selected subset of C, $\bar { C } { = } \{ C _ { i { \_ } 1 } ,$ $C _ { i \_ 2 } , . . . , C _ { i \_ t } \}$ , the multiplicative preference relation on any two criteria $C _ { i }$ and $C _ { j }$ in $C$ can be defined as

$$
p _ {i j} ^ {k} = 9 \text {   and   } p _ {j i} ^ {k} = 1 / 9, \quad i, j = 1, \dots , n; i \neq j,
$$

$$
\text { if } C _ {i} \in \bar {C}, C _ {j} \in C / \bar {C},\tag{4}
$$

$$
p _ {i j} ^ {k} = p _ {j i} ^ {k} = 1, \quad i, j = 1, \dots , n, \text { otherwise }.\tag{5}
$$

(5) A fuzzy selected subset of C. Let $\tilde { C } { = } \{ ( C _ { i { \_ } 1 } , l _ { i { \_ } 1 } ^ { k } ) $ $( C _ { i \_ 2 } , l _ { i \_ 2 } ^ { k } ) , . . . , ( C _ { i \_ 9 } , l _ { i \_ 9 } ^ { k } ) \} , i \_ { 1 \_ 9 } < n$ be a fuzzy selected subset of C used by a DM $e _ { k } , e _ { k } { \in } E _ { \mathrm { { \ell } } }$ , to express his/her preference on part of the criteria using linguistic terms. $l _ { i \_ i } ^ { k }$ <sub>r</sub> is a linguistic term in this paper, with $i \_ r = 1 , . . . , i \_ q$ [23].

For example, a DM may think that criterion $C _ { i }$ is ‘‘good’’, $C _ { j }$ is ‘‘very good’’, and criteria $C _ { h }$ and $C _ { l }$ are both $\dot { \mathfrak { s e } } _ { \mathrm { f a i r } } , \mathrm { : }$ . For any two criteria $C _ { i }$ and $C _ { j }$ in $C ,$ if they both belong to ${ \tilde { C } } ,$ where $l _ { i } ^ { k } { = } ( u _ { i } , \alpha _ { i } , \beta _ { i } )$ and $l _ { j } ^ { k } { = } ( u _ { j } , \alpha _ { j } , \beta _ { j } )$ , then the multiplicative preference relation on them can be defined as:

$$
p _ {i j} ^ {k} = 9 ^ {u _ {i} - u _ {j}}, \quad i, j = 1, \dots n; i \neq j.\tag{6}
$$

If none of the two criteria $C _ { i }$ and $C _ { j }$ belongs to ${ \tilde { C } } ,$ then

$$
p _ {i j} ^ {k} = 1, \quad i, j = 1, \dots , n; i \neq j.\tag{7}
$$

If criterion $C _ { i }$ belongs to $\tilde { C }$ and $C _ { j }$ does not belong to ${ \tilde { C } } ,$ then

$$
p _ {i j} ^ {k} = 9 ^ {u _ {i} - 0. 5}, \quad i, j = 1, \dots , n; i \neq j.\tag{8}
$$

(6) Normal preference relation. A DM may give normal preference relation on criteria to express his/ her strict preferences to the criteria. For example, DM $e _ { k } ,$ prefers criterion $C _ { i }$ to $C _ { j }$ and prefers criterion $C _ { c }$ to criteria $C _ { l }$ and $C _ { h } \ [ 2 3 ]$

In this case, for the criteria with strict preference relationships, their multiplicative preference relations are 9 ver $1 / 9$ . Thus, $p _ { i j } ^ { k } { = } 9$ and $\stackrel { \stackrel { - } { } _ { h } } { = } 1 / 9 ; \stackrel { k } { p _ { c l } } { = } 9$ and $p _ { l c } ^ { \ k } { = } 1 / 9 ; p _ { i c } ^ { \ k } { = } 1$ and ${ p \llap / } _ { l h } ^ { k } { = } 1$

(7) Fuzzy preference relation. The DMs’ preference relation is described by a binary fuzzy relation F in C, where $F$ is a mapping $C \times C \to [ 0 , 1 ]$ and $f _ { i j }$ denotes the preference degree of criterion $C _ { i }$ over $C _ { j } .$ F is assumed to be reciprocal. By definition [6,12], (i) $f _ { i j } + f _ { j i } = 1 , i , j = 1 , . . . , n ; i \ne j$ and $\mathrm { ( i i ) } f _ { i i } \mathrm { = - \ ( s y m b o l \ ^ { \circ } - ^ { \circ } }$ means that the DM does not need to give any preference information on criterion $C _ { i } )$ , bi.

Fuzzy preference relation can be transformed into multiplicative preference relation as follows:

$$
p _ {i j} ^ {k} = \frac {f _ {i j} ^ {k}}{f _ {j i} ^ {k}}, \quad i, j = 1, \dots , n.\tag{9}
$$

3.2. Aggregating the multiplicative preference relations from multiple DMs

After transforming the preference information in multiple formats into one single format, the next step is to aggregate the multiplicative preference relations from multiple DMs, described in details below.

## 3.2.1. Fuzzy majority method

Denote $P ^ { l } { = } ( p _ { i j } ^ { l } ) _ { n \times n }$ as the individual multiplicative preference relation on criteria from DM $e _ { l } , l { = } 1 , . . . , K .$ A collective multiplicative preference relation $P ^ { C } =$ $( p _ { i j } ^ { c } ) _ { n \times n }$ can be obtained according to the opinions of majority of the DMs. Traditionally, the majority is defined as a threshold number of individuals. Fuzzy majority [10] is a soft majority concept expressed by a fuzzy linguistic quantifier [20,21]. $p _ { i j } ^ { c }$ can be calculated by using the ordered weighted aggregation (OWG) operator, defined as follows.

Let $p _ { i j } ^ { 1 } , p _ { i j } ^ { 2 } , . . . , p _ { i j } ^ { K }$ be a list of values to be aggregated. The OWG operator of dimension K is a function $\phi ^ { G }$

$$
\phi^ {G}: R ^ {K} \to R
$$

which is associated with a set of weights k. k is defined as

$$
\phi^ {G} (p _ {i j} ^ {1}, p _ {i j} ^ {2}, \dots , p _ {i j} ^ {K}) = \prod_ {l = 1} ^ {K} (z _ {l}) ^ {\lambda_ {l}},\tag{10}
$$

where $\lambda { = } [ \lambda _ { 1 } , . . . , \lambda _ { K } ]$ is an exponential weighting vector such that $\lambda _ { l } { \in } [ 0 , 1 ] , \ l { = } 1 , . . . , K ,$ , and $\begin{array} { r } { \sum _ { l = 1 } ^ { K } \lambda _ { l } = 1 } \end{array}$ . Z is the associated ordered value vector. Each element $z _ { l } { \in } Z$ is the lth largest value in the collection $\{ p _ { i j } ^ { 1 } ,$ $p _ { i j } ^ { 2 } , . . . , p _ { i j } ^ { K } \}$ . The concept of fuzzy majority is used to calculate the weighting vector k by means of a fuzzy linguistic quantifier according to Yager’s ideas [18,19]. In the case of a nondecreasing proportional quantifier $\mathcal { Q } ,$ the weighting vector k is calculated using the following expression [18,19]:

$$
\lambda_ {l} = Q (l / K) - Q ((l - 1) / K), \quad l = 1, \dots , K.\tag{11}
$$

When a fuzzy linguistic quantifier Q is used to calculate the weight vector k in the OWG operator $\phi ^ { G }$ , it is represented by $\phi _ { Q } ^ { G } .$ . Therefore, the collective multiplicative preference relation is obtained as follows:

$$
p _ {i j} ^ {c} = \phi_ {Q} ^ {G} (p _ {i j} ^ {1}, p _ {i j} ^ {2}, \dots , p _ {i j} ^ {K}), i, j = 1, \dots , n; i \neq j.\tag{12}
$$

3.2.2. Geometric means aggregation rule for aggregation across multiple DMs

Again, denote $P ^ { \bar { l } } { = } ( p _ { i j } ^ { l } ) _ { n \times n }$ as the individual multiplicative preference relation on the criteria from DM $e _ { l } , \ l { = } 1 , . . . , K$ . A collective multiplicative preference relation $P ^ { C } { = } ( p _ { i j } ^ { c } ) _ { n \times n }$ can be obtained by using the geometric means aggregation rule [1]:

$$
p _ {i j} ^ {c} = \prod_ {l = 1} ^ {K} (p _ {i j} ^ {l}) ^ {T _ {l}}, \quad i, j = 1, \dots , n; i \neq j.\tag{13}
$$

where $T _ { l }$ is the power coefficient of DM $e _ { l } , l = 1 , . . . , K .$ In this study, DMs are treated equally unless specified.

Fuzzy majority method is a soft computing analysis method. It uses OWG operator to aggregate DMs’ individual multiplicative preference relations under a semantic. It provides more flexibility in group decision making to reflect the opinions of majority of the DMs, such as ‘‘most’’, ‘‘at least half’’ or ‘‘as many as possible’’. Geometric means aggregation rule is also efficient in group decision-making analysis process. Using the logarithmic least-squares method, geometric means aggregation rule can provide explicit solution to the problem, such as aggregation across the DMs and criteria [1].

## 3.3. Determining the weights of criteria

Given the collective multiplicative preference relation $P ^ { C } { = } ( p _ { i j } ^ { c } ) _ { n \times n } ,$ the geometric means aggregation rule can be used again to obtain the overall values of the criteria,

$$
d _ {i} = \left[ \prod_ {j = 1} ^ {n} \prod_ {l = 1} ^ {K} (p _ {i j} ^ {l}) ^ {1 / K} \right] ^ {1 / n}, \quad i = 1, \dots , n.\tag{14}
$$

Normalize $d _ { i } , i = 1 , . . . , n ,$ , the weight vector w of the criteria can then be obtained.

## 4. Validation of the use of multiple preference formats

In solving the student Information Systems (IS) project assessment problem, Kwok et al. [13] proposed the use of different formats in presenting individual preferences. Since the assessment criteria are different in nature, it is necessary to use different preference formats to assess the IS projects against different criteria (a MCDM problem). A similar scenario in the form of laboratory experiment is adopted in this study to validate the following hypothesis.

Hypothesis 1. Multiple preference formats in decision making increases satisfaction levels for both the decision-making process and the decision outcome than those from single preference format.

Because the validity of an experiment is directly affected by its construction and execution, attention to experimental design is extremely important. Because it is very difficult to remove the subjectivity of the experimenters and subjects, commonly, randomization is used in the experimental design. In a randomized experimental design, objects or individuals are randomly selected and assigned to experimental groups. Using randomization is the most reliable method of creating homogeneous treatment groups, without involving any potential biases or judgments.

For this study, only freshmen and sophomore students were available. They were assigned randomly to the pilot test and formal test. In the pilot test, sophomore students were assigned to four classes for tutorials. These four classes are assigned to be experimental groups and control groups using Completely Randomized Design method. In the formal test, the same randomization method is used to classify the four classes of freshmen students.

## 4.1. Pilot test

## 4.1.1. Experimental design

4.1.1.1. Subjects. The subjects are with 100 sophomore business students who attended a course of ‘‘Data Management’’ in Fall 2001. Among these students, 58% of them are male, and 42% are female. In order to fulfill the coursework requirement, they had to build database systems for a departmental digital library. The average age is 20.3 years old. Eventually, the effective sample size is 64, where 31 students are in the experimental group and 33 are in the control group.

4.1.1.2. Task. At the beginning of the experiment, the facilitator announced that the task of the experiment was to collect students’ opinions on the marking scheme in evaluating their coursework. Students were asked to express their opinions on the weights (or relative importance) of the four criteria used to evaluate their systems: $C _ { 1 }$ ‘‘ease of use’’, $C _ { 2 }$ ‘‘security’’, $C _ { 3 }$ ‘‘reliability’’ and $C _ { 4 }$ ‘‘response time’’. The facilitator then introduced the format(s) to be used by the students. Students then made their own decision without negotiating or compromising with each other. In order to do so, students are not allowed to communicate with others throughout the experiment.

During the experiment, students in the control group could express their opinions on the weights of the criteria by using only one format, i.e., utility value or a utility vector $( u _ { 1 } , . . . , u _ { 4 } ) . u _ { i } ( 0 < u _ { i } \leq 1 , i = 1 , 2 , 3 , 4 )$ represents the utility evaluation given to the ith criterion. Students in the experimental group could use any one of the eight preference formats discussed above. After that, the facilitator ran a program to calculate the criteria weights based on the student opinions. Lastly, students were asked to complete a questionnaire measuring their satisfaction levels with both the decision-making process and the decision outcome, as shown in Appendix A.

## 4.1.2. Measurement of the satisfaction of students

Two dependent variables were measured: the satisfaction levels of students with the evaluation process and with the evaluation outcome. To capture the satisfaction levels, a questionnaire with six questions was provided to the students after criteria evaluation (see Appendix A for details).

## 4.1.3. Tests on the instrument

Table 1 shows that the correlation coefficients between the scores on the first four questions and on the fifth question (overall satisfaction level with decision-making process) are high enough. In addition, the correlation coefficients between the average scores across question 1 to question 4 and that of question 5 justify the use of the four questions in measuring students’ satisfaction levels on the decision-making process. The use of these questions for measuring satisfaction on decision-making process is valid.

Correlation coefficients among the questions and the average score of questions 1 – 4

<table><tr><td></td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Q5</td></tr><tr><td>Q1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Q2</td><td>0.6559</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Q3</td><td>0.5871</td><td>0.6621</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Q4</td><td>0.4880</td><td>0.6542</td><td>0.5675</td><td>-</td><td>-</td></tr><tr><td>Q5</td><td>0.6429</td><td>0.7902</td><td>0.6470</td><td>0.5790</td><td>-</td></tr><tr><td>Average (Q1–Q4)</td><td>0.8225</td><td>0.8882</td><td>0.8391</td><td>0.8008</td><td>0.7948</td></tr></table>

Note that except the inter-item correlation, reliability score of the instrument is also computed. The figure 0.8933 suggests it is an instrument with high reliability. The questions can reflect accurately and capture the satisfaction level of the subjects with the decision-making process.

## 4.1.4. Findings and discussion

The preference exploitation process is proposed to determine the weights of criteria based on DMs preference information. With these methods, preferences expressed in different formats mentioned above can be transformed to a single one. This provides convenience and accuracy in generating a final outcome based on the opinions of multiple DMs.

In addition to the advantages discussed above, the use of multiple preferences formats also results in higher satisfaction levels of the DMs with both the decision-making process and the decision outcome. To compare the means of the students’ satisfaction levels with both the decision-making process and the decision outcome between the control group and the experimental group, an independent t-test was employed. The results are listed in Tables 2 and 3, respectively [7,8,24].

Table 2 shows that F-value is 1.573 and the significance coefficient is 0.215 for Levene’s test for equality of variances. These results justify that the variances of the students’ satisfaction levels with the decision-making process can be thought as the same, which supports the use of the t-test. The low p-value suggests that there is a significant difference in the satisfaction level with the decision-making process between the students in the control group and those in the experimental group. It implies that the students using multiple preference formats have higher satisfaction level with the decision-making process than those using single format.

Similarly in Table 3, the results for Levene’s test for equality of variances are F-value is 0.769 and the significance coefficient is 0.384. These results justify that the variances of the students’ satisfaction level with the decision outcome can be thought as the same, which supports the use of the t-test. Once again, the low p-value implies a significant difference in the satisfaction level with the decision outcome between the students in control group and those in experimental group. In other words, the students using multiple preference formats have higher satisfaction level with the decision outcome than those using single format.

4.2. Formal test for validating the use of multiple preference formats

## 4.2.1. Experimental design

4.2.1.1. Subjects. Similarly, the subjects are with 100 freshmen business students who attended a course of ‘‘Management Information Systems’’ in Spring 2002. They had to be evaluated on four perspectives: individual assignment, group project, middle term exam, and final term exam. Eventually, the effective sample size is 61, where 31 students are in the experimental group and 30 students are in the control group. As shown in Table 4, among the effective sample, 36.1% of them are male, and 63.9% are female. As shown in Table 5, 26.2% (16) students’ age fall in the range 18 – 19, while 73.8% (45) students’ age fall in the range 20–21.

Effect of using multiple preference formats on students’ satisfaction levels with evaluation process

<table><tr><td rowspan="2">Measure</td><td rowspan="2">Mean(standard deviation)for using single preference format</td><td rowspan="2">Mean(standard deviation)for using multiple preference formats</td><td rowspan="2">t-value(two-tailed)</td><td rowspan="2">p-value</td><td colspan="2">Levene&#x27;s test</td></tr><tr><td>F-value</td><td>Significance</td></tr><tr><td>Satisfaction level</td><td>2.42 (0.66)</td><td>3.74 (0.68)</td><td>7.84</td><td>0.000</td><td>1.573</td><td>0.215</td></tr></table>

Table 3  
Effect of using multiple preference formats on students’ satisfaction level with evaluation outcome

<table><tr><td rowspan="2">Measure</td><td rowspan="2">Mean(standard deviation)for using single preference format</td><td rowspan="2">Mean(standard deviation)for using multiple preference formats</td><td rowspan="2">t-value(two-tailed)</td><td rowspan="2">p-value</td><td colspan="2">Levene&#x27;s test</td></tr><tr><td>F-value</td><td>Significance</td></tr><tr><td>Satisfaction level</td><td>2.52 (0.71)</td><td>3.71 (0.64)</td><td>7.028</td><td>0.000</td><td>0.769</td><td>0.384</td></tr></table>

4.2.1.2. Task. At the beginning of the experiment, the facilitator announced that the task of the experiment was to collect students’ opinions on the marking scheme in evaluating their overall performances in taking the course. To enhance student-centered learning, a well-balanced marking scheme would encourage students’ enthusiasm and activity in the course of study [5]. Students were asked to express their opinions on the weights (or relative importance) of the four items used to evaluate their performance: $C _ { 1 }$ ‘‘individual assignment’’, $C _ { 2 }$ ‘‘group project’’, $C _ { 3 }$ ‘‘middle term exam’’, and $C _ { 4 }$ ‘‘final term exam’’. The intention is to collect student opinions under a semantic such as ‘‘most’’. The facilitator then introduced the format(s) to be used by the students. Students made their own decision without communicating with each other.

During the experiment, students in the control group could express their opinions on the weights of the criteria by using only one format, i.e., utility value or a utility vector $( u _ { 1 } , . . . , u _ { 4 } ) . \ u _ { i } \ ( 0 < u _ { i } \leq 1 , i = 1 , 2 , 3 , 4 )$

represents the utility evaluation given to the ith criterion. Students in the experimental group could use any one of the eight preference formats discussed above. After that, the facilitator ran a program to calculate the weights of the criteria based on the students’ opinions. Lastly, students were asked to complete a questionnaire measuring their satisfaction levels with both the decision-making process and the decision outcome, as shown in Appendix B.

## 4.2.2. Measurement of the satisfaction levels of students

In addition to measuring students’ general opinions, two dependent variables were measured: the satisfaction levels of students with the evaluation process and with the evaluation outcome. To capture the satisfaction levels, a questionnaire with 12 questions was provided to the students after criterion evaluation (see Appendix B for details).

## 4.2.3. Test results on the instrument

Table 6 shows the communalities in the factor analysis to measure the validity of the instrument. In addition, to measure the reliability of the construct (C1, C2, C3A, C3B), alpha value is calculated with the result as 0.9013; likewise, to measure the reliability of the construct (D1, D2, D3, D4A, D4B), alpha value is calculated with the result as 0.9115.

Levene’s test for equality of variances is conducted, and the results are favorable. To compare

Table 4 Gender

<table><tr><td></td><td>Frequency</td><td>Percent (%)</td></tr><tr><td>Female</td><td>39</td><td>63.9</td></tr><tr><td>Male</td><td>22</td><td>36.1</td></tr><tr><td>Total</td><td>61</td><td>100.0</td></tr></table>

Table 5 Age group

<table><tr><td></td><td>Frequency</td><td>Percent (%)</td></tr><tr><td>18–19</td><td>16</td><td>26.2</td></tr><tr><td>20–21</td><td>45</td><td>73.8</td></tr><tr><td>Total</td><td>61</td><td>100.0</td></tr></table>

Table 6 Factor analysis: communalities

<table><tr><td></td><td>Initial</td><td>Extraction</td></tr><tr><td>C1</td><td>1.000</td><td>0.772</td></tr><tr><td>C2</td><td>1.000</td><td>0.847</td></tr><tr><td>C3A</td><td>1.000</td><td>0.700</td></tr><tr><td>C3B</td><td>1.000</td><td>0.747</td></tr><tr><td>D1</td><td>1.000</td><td>0.841</td></tr><tr><td>D2</td><td>1.000</td><td>0.805</td></tr><tr><td>D3</td><td>1.000</td><td>0.706</td></tr><tr><td>D4A</td><td>1.000</td><td>0.690</td></tr><tr><td>D4B</td><td>1.000</td><td>0.769</td></tr></table>

the significant differences in the means of the students’ satisfaction levels with both the decisionmaking process and the decision outcome between the control group and the experimental group, independent t-test was employed. The results are listed in Table 7, which justify the hypothesis further.

## 5. Conclusion

As argued by Courtney [9], the personal perspective is based on individual experiences, intuition, personality factors, and attitudes about risk, among others. Individuals are notoriously complex and varied in decision-making styles. In a complex scenario, given the same external information, no two people might reach the same conclusion, as their background, training, experience, values, ethics, and others may differ. Sweeping in as wide a variety of individual perspectives as feasible is thus necessary for unstructured decisions. In this paper, the problem of providing preference information on criteria is investigated. Multiple DMs tend to express their preferences on the criteria in different formats due to their different cultural and educational backgrounds and their different value systems. It is obviously the case in the cyberspace environment. This paper proposes an approach to provide more flexibility to DMs in expressing their opinions by extending the current preference repression formats. The uniformity methods and aggregating methods are also discussed. The preference exploitation process is used to determine the weights of the criteria. The experiments are conducted to justify the proposed approach in using multiple preference formats. Using the proposed formats to express preference information would provide more flexibility in MCDM and also would result in higher satisfaction level on both the decision-making process and the decision outcome.

Table 7 Independent samples test

<table><tr><td rowspan="3" colspan="2"></td><td colspan="2">Levene&#x27;s test equality of</td><td colspan="7">t-test for equality of</td></tr><tr><td rowspan="2">F</td><td rowspan="2">Significance</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Significance</td><td rowspan="2">Mean difference</td><td rowspan="2">Standard error difference</td><td colspan="2">95% interval of difference</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td rowspan="2">C1</td><td>Equal variances</td><td>0.044</td><td>0.834</td><td>5.235</td><td>59</td><td>0.000</td><td>1.0323</td><td>0.1972</td><td>0.6377</td><td>1.4268</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>5.231</td><td>58.627</td><td>0.000</td><td>1.0323</td><td>0.1973</td><td>0.6374</td><td>1.4271</td></tr><tr><td rowspan="2">C2</td><td>Equal variances</td><td>0.248</td><td>0.620</td><td>4.075</td><td>59</td><td>0.000</td><td>0.9688</td><td>0.2377</td><td>0.4931</td><td>1.4445</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>4.070</td><td>58.282</td><td>0.000</td><td>0.9688</td><td>0.2380</td><td>0.4924</td><td>1.4453</td></tr><tr><td rowspan="2">C3A</td><td>Equal variances</td><td>0.230</td><td>0.633</td><td>2.084</td><td>59</td><td>0.042</td><td>0.5065</td><td>0.2431</td><td>2.010E-02</td><td>0.9928</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>2.091</td><td>57.000</td><td>0.041</td><td>0.5065</td><td>0.2422</td><td>2.153E-02</td><td>0.9914</td></tr><tr><td rowspan="2">C3B</td><td>Equal variances</td><td>0.006</td><td>0.938</td><td>3.327</td><td>59</td><td>0.002</td><td>0.7699</td><td>0.2314</td><td>0.3068</td><td>1.2330</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>3.318</td><td>56.949</td><td>0.002</td><td>0.7699</td><td>0.2320</td><td>0.3052</td><td>1.2345</td></tr><tr><td rowspan="2">D1</td><td>Equal variances</td><td>0.201</td><td>0.655</td><td>1.366</td><td>59</td><td>0.017</td><td>0.3484</td><td>0.2550</td><td>-0.1618</td><td>0.8586</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>1.362</td><td>55.809</td><td>0.019</td><td>0.3484</td><td>0.2559</td><td>-0.1642</td><td>0.8610</td></tr><tr><td rowspan="2">D2</td><td>Equal variances</td><td>1.870</td><td>0.177</td><td>2.786</td><td>59</td><td>0.007</td><td>0.6097</td><td>0.2189</td><td>0.1717</td><td>1.0476</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>2.791</td><td>58.604</td><td>0.007</td><td>0.6097</td><td>0.2184</td><td>0.1725</td><td>1.0468</td></tr><tr><td rowspan="2">D3</td><td>Equal variances</td><td>0.109</td><td>0.742</td><td>2.537</td><td>59</td><td>0.014</td><td>0.6075</td><td>0.2395</td><td>0.1283</td><td>1.0867</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>2.539</td><td>58.990</td><td>0.014</td><td>0.6075</td><td>0.2393</td><td>0.1287</td><td>1.0864</td></tr><tr><td rowspan="2">D4A</td><td>Equal variances</td><td>0.477</td><td>0.492</td><td>3.769</td><td>59</td><td>0.000</td><td>0.8677</td><td>0.2302</td><td>0.4071</td><td>1.3284</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>3.766</td><td>58.561</td><td>0.000</td><td>0.8677</td><td>0.2304</td><td>0.4066</td><td>1.3289</td></tr><tr><td rowspan="2">D4B</td><td>Equal variances</td><td>0.898</td><td>0.347</td><td>3.404</td><td>59</td><td>0.001</td><td>0.7677</td><td>0.2256</td><td>0.3164</td><td>1.2191</td></tr><tr><td>Equal variances assume</td><td></td><td></td><td>3.393</td><td>56.269</td><td>0.001</td><td>0.7677</td><td>0.2263</td><td>0.3145</td><td>1.2210</td></tr></table>

To guarantee the generalizability of this study, the reliability of the measurement instruments in both the pilot test and formal test are evaluated, with the satisfactory high significance. In experimental design, randomization method is used. Levene’s test for equality of variances is conducted. The results of Levene’s test support the use of the t-test by justifying that the variances of the students’ satisfaction level between the control group and the experimental group can be considered as the same. Independent t-test then was used to capture the significant differences in the mean of the student satisfaction levels with both the decision-making process and outcome between the control group and the experimental group.

The favorable results in our experiment validate this mechanism for distributed decision-making environment in a virtual society. The decision makers can enjoy the flexibility in expressing their opinions with their most favorite formats. The proposed method of uniformity, aggregation, and exploitation would generate valid decision results.

However, there is a need to explain and educate the users about the diverse preference formats before the method can be used. In the course of the experiment, it was necessary to announce the usage of various preference formats to the subjects. In reality, the distributed decision-making systems (to support this research) should provide user-friendly interfaces and online help to facilitate the use of preference formats.

## Appendix A. Questions used to measure students’ satisfaction levels

Question 1: It is easy for me to express my opinions by using the provided preference format(s).

Question 2: I am able to sufficiently express my opinions.

Question 3: I am able to precisely express my opinions.

Question 4: The preference format(s) provided is suitable for me.

Question 5: I am satisfied with the process of expressing my opinions.

Question 6: I am satisfied with the evaluation outcome by expressing my opinions.

The answers are on a Likert scale from 1 to 5, corresponding to strongly disagree, disagree, fair, agree, and strongly agree. When they have finished evaluating a criterion, students are given these questions to measure their satisfaction levels with the evaluation process and with the evaluation outcome.

## Appendix B. Questionnaire: measurement of satisfaction level

Instruction: Please circle the appropriate answer for each question.

## B.1. Demographic information

A1. What is your gender? Male Female

A2. How old are you? 18– 19 20 – 21 22 –23 Other

A3. What is your major?

## B.2. General opinion

B1. It is easy for me to express my opinion by using the provided preference format(s).

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Highly agree</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Highly disagree</td></tr></table>

B2. I am able to sufficiently express my opinion.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Highly agree</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Highly disagree</td></tr></table>

B3. I am able to precisely express my opinion.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Highly agree</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Highly disagree</td></tr></table>

B4. The preference format provided is suitable for me.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Highly agree</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Highly disagree</td></tr></table>

B5. I am satisfied with the process of expressing my opinion.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Highly agree</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Highly disagree</td></tr></table>

## B.3. Evaluation process

C1. How would you rate your satisfaction with the use of the evaluation process?

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Very satisfied</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Very dissatisfied</td></tr></table>

C2. Are you satisfied with using the evaluation process?

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Very satisfied</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Very dissatisfied</td></tr></table>

C3. Considered all things about the evaluation process, I am:

<table><tr><td>(a)</td><td>1Very pleased</td><td>2</td><td>3</td><td>4Neutral</td><td>5</td><td>6</td><td>7Very displeased</td></tr><tr><td>(b)</td><td>1Very contended</td><td>2</td><td>3</td><td>4Neutral</td><td>5</td><td>6</td><td>7Very frustrated</td></tr></table>

## B.4. Evaluation outcome

D1. I am satisfied with the evaluation outcome by expressing my opinion.

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Very satisfied</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Very dissatisfied</td></tr></table>

D2. How would you rate your satisfaction with the use of the evaluation outcome?

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Very satisfied</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Very dissatisfied</td></tr></table>

D3. Are you satisfied with using the evaluation outcome?

<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>Very satisfied</td><td></td><td></td><td>Neutral</td><td></td><td></td><td>Very dissatisfied</td></tr></table>

D4. Considered all things about the evaluation outcome, I am:

<table><tr><td>(a)</td><td>1Very pleased</td><td>2</td><td>3</td><td>4Neutral</td><td>5</td><td>6</td><td>7Very displeased</td></tr><tr><td>(b)</td><td>1Very contended</td><td>2</td><td>3</td><td>4Neutral</td><td>5</td><td>6</td><td>7Very frustrated</td></tr></table>

## References

[1] J. Barzilai, F.A. Lootsma, Power relations and group aggregation in the Multiplicative AHP and SMART, Journal of Multi-Criteria Decision Analysis 6 (1997) 155 – 165.

[2] C. Carlsson, Decision support in virtual organizations: the case for multi-agent support, Group Decision and Negotiation 11 (2002) 185–221.

[3] C. Carlsson, R. Fuller, Fuzzy multiple criteria decision making: recent developments, Fuzzy Sets and Systems (78) (1996) 139– 153.

[4] C.T. Chen, A fuzzy approach to select the location of the distribution center, Fuzzy Sets and Systems (118) (2001) 65 – 73.

[5] J.C.H. Chen, P.P. Chong, Y.S. Chen, Decision criteria consol idation: a theoretical foundation of Pareto Principle to Michael Porter’s competitive forces, Journal of Organizational Computing and Electronic Commerce 11 (2000) 1 –14.

[6] F. Chiclana, F. Herrera, E. Herrera-Viedma, Integrating three representation models in fuzzy multipurpose decision-making based on fuzzy preference relations, Fuzzy Sets and Systems 97 (1998) 33– 48.

[7] V.T. Clover, H.L. Balsley, Business Research Methods, Wiley, New York, 1984.

[8] D.R. Cooper, P.S. Schindler, Business Research Methods, McGraw-Hill/Irwin, Boston, 2001.

[9] J.F. Courtney, Decision-making and knowledge management in inquiring organizations: toward a new decision-making paradigm for DSS, Decision Support Systems 31 (2001) 17– 38.

[10] F. Herrera, E. Herrera-Viedma, F. Chiclana, Multiperson decision-making based on multiplicative preference relations, European Journal of Operational Research 129 (2001) 372 – 385.

[11] C.L. Hwang, M.J. Lin, Group Decision-Making Under Multiple Criteria: Methods and Applications, Springer-Verlag, Berlin, 1987.

[12] J. Kacprzyk, M. Fedrizzi, H. Nurmi, Group decision-making and consensus under fuzzy preference and fuzzy majority, Fuzzy Sets and Systems 49 (1) (1992) 21– 31.

[13] R.C.W. Kwok, D.N. Zhou, Q. Zhang, J. Ma, A fuzzy multicriteria decision-making model for IS project assessment, Decision Support Systems (2001) (under revision).

[14] J.W. Lee, S.H. Kim, Using analytic network process and goal programming for interdependent information system project selection, Computer and Operations Research 27 (2000) 367– 382.

[15] J.W. Lee, S.H. Kim, An integrated approach for interdependent information system project selection, International Journal of Project Management (19) (2001) 111 – 118.

[16] G. Liang, Fuzzy MADM based on ideal and anti-ideal concepts, European Journal of Operational Research 112 (1999) 682– 691.

[17] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[18] R.R. Yager, Families of OWA operators, Fuzzy Sets and Systems 59 (1993) 125– 148.

[19] R.R. Yager, Quantifier guided aggregation using OWA oper ators, International Journal of Intelligent Systems 11 (1996) 49– 73.

[20] L.A. Zadeh, The concept of a linguistic variable and its appli cation to approximate reasoning I, II, Information Sciences 8 (1975) 301– 357.

[21] L.A. Zadeh, A computational approach to fuzzy quantifiers in natural languages, Computing Mathematics Applications 9 (1983) 149– 184.

[22] M. Zeleny, Multiple Criteria Decision Making, McGraw-Hill, New York, 1982.

[23] D.N. Zhou, Fuzzy Group Decision Support System Approach to Group Decision Making Under Multiple Criteria, PhD Dissertation, City University of Hong Kong, Hong Kong, 2000.

[24] W.G. Zikmund, Business Research Methods, Harcourt Brace, Orlando, FL, 1997.

![](/api/attachments/YSAM59E4/fulltext/images/789781197b94136dfba97a214ebf341990f358c8261567a5782ed9633f12fc24.jpg)  
Quan Zhang, PhD, is an assistant professor in the School of Business Administration at Gonzaga University in Spokane, WA. His research interests include building and applying multi-criteria decision-making models to business applications and decision support systems.

![](/api/attachments/YSAM59E4/fulltext/images/f094e07ceeee24c21755208739fe4d95590d24835de722d2e6a7f7cb73363239.jpg)

Jason C.H. Chen is professor and the coordinator of the MIS program in the School of Business Administration at Gonzaga University in Spokane, WA, USA. He conducted Spark-MIS system for a United Nation Development Program (UNDP) project for State Science and Technology Commission of China from 1992 to 1994. He has been a senior consultant of Taskco.com, an information services firm in Taipei, since 2000. He also taught the Bei-

jing International MBA and EMBA programs at Peking University in years 1999 and 2003. His research interests include building and applying e-commerce and e-business models to business applications, improving customer services through organizational learning, decision support systems, and Pareto Principle with business applications.

![](/api/attachments/YSAM59E4/fulltext/images/afbd9e9c5bf80544ceaa5e97d2c31328529447ca0a0bfd9e77111c19785c5742.jpg)

P. Pete Chong is Martel Professor of CIS at the University of Houston—Downtown. Prior to joining UHD, Dr. Chong taught at Gonzaga University, University of Idaho, and Southeastern Louisiana University, where he also served as the head of the Business Research Unit and the editor for Southeastern Economic Outlook. His research interests are in Pareto Principle and its application to Information Systems, including Netchising, e-commerce for small

businesses, and e-government.
