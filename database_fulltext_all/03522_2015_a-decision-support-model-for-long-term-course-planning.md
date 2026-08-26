---
otero_id: 3522
otero_key: "273UP4RS"
title: "A decision support model for long-term course planning"
authors: "Abdallah Mohamed"
year: "2015"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2015.03.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Abdallah Mohamed

Irving K. Barber School of Arts and Sciences, Unit 5, The University of British Columbia (Okanagan), Kelowna, BC V1V 1V7, Canada

## a r t i c l e i n f o

Article history: Received 26 December 2013 Received in revised form 7 March 2015 Accepted 8 March 2015 Available online 16 March 2015

Keywords: Decision support Diversi<sup>fi</sup>cation Long-term course planning Academic advising

## a b s t r a c t

Assisting students to prepare long-term course plans towards timely graduation is a challenging and time-consuming advising activity. Unless appropriate decisions are made, undesirable consequences may occur. Earlier, an approach called Interactive Decision Support for Course Planning (IDiSC) was developed. IDiSC performs a pro-active analysis of the impact of the different aspects of the problem and eventually suggests a study plan that balances students' preferences and advisors' recommendations, without violating any regulations. IDiSC employs mathematical optimization and follows an evolutionary and iterative decision support framework, called EVOLVE\*. This paper proposes IDiSC<sup>+</sup>, which is an improvement over IDiSC. The contribution of IDiSC<sup>+</sup> is twofold. First, in order to address uncertainties and implicit concerns not formally described in the original problem statement, IDiSC<sup>+</sup> adopts a diversi<sup>fi</sup>cation algorithm that, instead of providing a single study plan, generates a set of optimal or near optimal alternative plans that are of a similar quality and yet structurally different. Human intelligence is then employed to analyze these alternatives and to either approve one of them or re<sup>fi</sup>ne the problem settings for generating further solutions. Second, IDiSC<sup>+</sup> uses a more advanced and representative formal model that overcomes key assumptions and limitations of its predecessor and thus addresses the problem in a more realistic way. A real-world application of IDiSC<sup>+</sup> is presented in order to illustrate its added value.

© 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

Academic advising is an integral part of the mission of higher education [1]. Not only does academic advising enhance students' academic experiences [2] but it also plays a crucial role in students' retention and success [3–8]. Academic advising refers to “situations in which an institutional representative gives insight or direction to a college student about an academic, social, or personal matter.” [9].

Long-Term Course Planning (LTCP) is a challenging and timeconsuming activity involved in academic advising [10]. LTCP refers to the process of an academic advisor helping a student prepare a study plan towards graduation, with all un<sup>fi</sup>nished courses required to graduate assigned to upcoming semesters.<sup>1</sup>

LTCP is challenging for several reasons. First, many constraints related to university regulations and students' abilities and choices must be respected. Not only that, but we must also distinguish between two types of constraints:

• hard constraints, which are conditions that must never be violated, e.g., registration rules, and

• soft constraints, which are conditions that could be ful<sup>fi</sup>lled at different levels of satisfaction, e.g., course priorities.

Furthermore, some university constraints do not apply to all students in the same way due to different student statuses, e.g., the maximum credit hour load may vary depending on a student's academic record.

Second, the topic of investigation is fundamentally dynamic. Students' statuses, for example, change from one semester to another, and may even change during the same semester, e.g., when students withdraw from courses. Students' preferences and choices may also vary as time passes due to the development of their academic understanding and knowledge. There are also changes that may occur to university settings over the long run. New courses are offered and some are canceled when academic programs change. The frequency of course offerings may also change due to administrative or academic reasons. Even university regulations may change from one year to another.

Third, the above challenges should be addressed while planning a relatively high number of courses, which are of different types and attributes and may be dependent on each other. At the end of this paper, for example, we discuss the degree requirements of a faculty of computer studies, which includes courses from different areas, e.g., software development, information management, network computing, mathematics, etc., and these courses have different weights, values, offering dates, time requirements, and fees, in addition to various interdependencies such as a structure of prerequisite courses.

Unless appropriate decisions are made during academic advising, serious consequences may occur. A survey of 944 colleges and universities identi<sup>fi</sup>ed poor academic advising as the number-one characteristic associated with student attrition on their campuses [11]. Therefore, it is necessary to develop techniques that provide appropriate support for both academic advisors and students.

Decision support is a proven means to help humans make decisions when solving semi-structured or unstructured problems encountering incomplete or uncertain information [12]. The paradigm of decision support suggests a pro-active evaluation of decision alternatives and aims to provide the best knowledge available to decision makers in order to help them make more informed, transparent, and effective decisions.

This paper proposes an approach called IDiSC<sup>+</sup> (Interactive Decision Support for Course Planning). The proposed approach tries to address the LTCP problem by providing meaningful support for academic advisors and students when creating study plans. The IDiSC<sup>+</sup> approach is an advancement of a previous effort that resulted in the development an earlier approach, named IDiSC [13,14].

It is important to emphasize that neither the proposed approach nor similar ones aim to replace one-on-one student–advisor interactions [9,15,16]. Instead, such technologies should be used for automating some advising functions, saving time for other activities such as career counseling.

The remaining of this paper is organized as follows: Section 2 gives an overview of the previous work as well as the contribution of this paper. Section 3 introduces the formal model of the LTCP problem. The IDiSC<sup>+</sup> approach is then discussed in Section 4. Then, an initial validation, which illustrates the added value of the proposed work, is given in Section 5. A discussion about the approach is given in Section 6, and the conclusions and future work are given in Section 7.

## 2. Previous work and IDiSC<sup>+</sup> contributions

## 2.1. Related work

The technical literature includes several approaches for providing computerized support to the academic advising process. Many of these approaches focused on general advising tasks [9,17]. For example, Grupe [18] proposed a web-based expert system that helps high-school and freshmen students when selecting an academic major. Patankar [19] introduced a rule-based expert system to perform routine advising tasks and provide general advice to undergraduate students. Pokrajac et al. [20] introduced an interactive expert system that may be used when building con<sup>fl</sup>ict-free schedules in which courses in one semester are assigned to preferred times and dates.

On the other hand, fewer approaches focused on the LTCP problem. In [10], Petri Nets were employed in a model that tries to shorten the path length to graduation while balancing the course load and considering the number of courses per semester as determined by students. In [21], a web-based tool was presented to help students select courses from the online registration system of the authors' university; the outcome is a typical study plan for the coming semesters. In [22], project management tools were used to help students get their degree sooner by presenting course sequences using visualization maps that are customized to each student.

The above approaches, however, suffered from one or more of the following weaknesses:

• Providing only one study-plan, even if there are other plans with similar quality and different structure.

• Considering the academic regulations as the main basis for planning, while not giving enough attention to students' preferences and choices.

• Trying to <sup>fi</sup>nd only the shortest path to graduation, which might not be the best option for all students.

• Failing to consider cases that need special care, such as students at risk of dismissal because of their low cumulative GPA (Grade Point Average).

• Simplifying some aspects of the problem such as considering course prerequisites as the only type of relationships between courses.

## 2.2. The IDiSC approach

This section brie<sup>fl</sup>y discusses the earlier IDiSC approach [13,14], which is the basis for the proposed work, along with its limitations. Further details are given later in Sections 3 and 4 as part of the full description of the advanced IDiSC<sup>+</sup> approach.

The core of IDiSC is a formal model that presents an integerprogramming problem, involving a set of university and student constraints along with a student-centered objective function. This formal model is used within a three-phase iterative process that integrates human and computer intelligence. The <sup>fi</sup>rst phase involves acquiring the inputs listed in Table 1 from humans. Optimization techniques are then used in the second phase to solve the formal model and generate an optimized study plan. This plan is reviewed in the third phase by decision makers who can either accept it or re<sup>fi</sup>ne the inputs and reapply the process.

The development of IDiSC was inspired by the work done by Ruhe et al. [12,23] that aimed at supporting the process of software release planning.

While the IDiSC approach proved to be promising, there are limita tions to its application:

(i) IDiSC can generate only one study plan for each set of problem settings. This does not ful<sup>fi</sup>ll one of the key principles of decision support: to generate a set of alternative solutions from which decision makers can choose the one that addresses implicit concerns not formally described in the original problem formulation [24,25].

(ii) IDiSC uses a formal model which, while tackles many of the LTCP problem aspects, makes some assumptions that are not applicable to many universities. For example, IDiSC assumes that all courses are available every semester. Practically, speci<sup>fi</sup>c courses may be offered in some semesters (e.g. fall) but not others (e.g. spring). Another assumption is related to course dependencies: IDiSC only considers simple relationships between courses (e.g. prerequisites). Further dependencies may be imposed such as to register two courses in the same semester or in successive semesters.

Input data of the IDiSC approach.

<table><tr><td>Inputs provided by university administration</td><td>Inputs provided by students</td></tr><tr><td>List of elective and compulsory coursesPrerequisite course structureCredit hours for each courseTuition fees per courseTotal credits required from elective courses *Minimum and maximum credits per semester *Minimum GPA per semester *</td><td>Number of semesters until graduationCourse priorities in terms of importance, grade, and time allocationBudget per semesterNumber of courses per semesterNumber of credit hours per semester</td></tr></table>

\* Inputs that could be modi<sup>fi</sup>ed by students, given that new values do not violate university regulations.

## 2.3. Contributions of IDiSC<sup>+</sup>

The IDiSC<sup>+</sup> approach was developed with the aim of overcoming the above two key limitations:

(i) IDiSC<sup>+</sup> uses a novel diversi<sup>fi</sup>cation technique in order to generate a set of optimal and near optimal alternative study plans. The term ‘alternatives’ here means that the generated plans are of a similar quality and, yet, structurally different. Decision makers can compare and analyze these alternatives and then either choose one of them or modify the problem settings and regenerate further plans (details in Section 4.2).

(ii) The formal model has been improved to better address the following aspects (details in Section 3.4):

▪ The ability to address more course dependencies.

▪ The possibility to deal with courses that are available in some semesters but not in the others.

▪ The possibility to assign an elective course as a “Must-take” course, which forces the approach to include it in the suggested study plan.

▪ The use of both soft and hard constraints for some aspects that were originally modeled as hard constraints only (refer to the <sup>fi</sup>rst challenge in Section 1).

▪ The ability to implement a student's leave of absence more ef<sup>fi</sup>ciently.

The paper also explains in Appendix C an example of customizing IDiSC<sup>+</sup> in order to address further concerns.

## 3. The formal model of IDiSC<sup>+</sup>

## 3.1. Decision variables

Suppose that we have a set R of w courses, and R is made up of two subsets: $R _ { c o m p } ,$ which includes v compulsory courses, and $R _ { e l e c t } ,$ , which includes $( w - \nu )$ elective courses.

$$
\begin{array}{l} R = R _ {c o m p} \cup R _ {e l e c t} = \left\{r _ {1}, r _ {2},..., r _ {v}, r _ {v + 1},..., r _ {w} \right\} \\ R _ {c o m p} \cap R _ {e l e c t} = \varnothing \end{array}
$$

In order to get an academic degree, a student must <sup>fi</sup>nish all courses in $R _ { c o m p }$ and a subset of courses from $R _ { e l e c t } .$ . The goal is to build a study plan that assigns un<sup>fi</sup>nished courses required for graduation to a <sup>fi</sup>nite number T of semesters, where each course r is assigned to one semester t at most. This is described by the decision variables

$$
X _ {i} = \left\{x _ {i, t}: i = 1... w, t = 1... T \right\}
$$

where,

$$
\forall \boldsymbol {r} _ {i}: \quad x _ {i, t} = \left\{ \begin{array}{l l} 1 & \text { if } r _ {i} \text { is   assignend   to } t \\ 0 & \text { otherwise } \end{array} \right..
$$

Since we need to generate a student plan that includes all compulsory courses and some elective courses, excluding all <sup>fi</sup>nished courses, and assuming that $R _ { f i n }$ is the set of <sup>fi</sup>nished courses and $R _ { u n f i n }$ is the set of un<sup>fi</sup>nished courses, then

$$
\forall \boldsymbol {r} _ {i}: \quad \sum_ {t} x _ {i, t} \left\{ \begin{array}{l l l} = 1 & \Longleftrightarrow & r _ {i} \in R _ {c o m p} \cap R _ {u n f i n} \\ = 0 & \Longleftrightarrow & r _ {i} \in R _ {f i n} \\ \leq 1 & \Longleftrightarrow & r _ {i} \in R _ {e l e c t} \end{array} \right..
$$

For example, consider a study plan with four semesters $\left( T = 4 \right)$ . The set of decision variables relevant to each course $r _ { i } \mathrm { i s } \{ x _ { i , 1 } , x _ { i , 2 } , x _ { i , 3 } , x _ { i , 4 } \}$ The set {1, 0, 0, 0} means that $r _ { i }$ is assigned to the <sup>fi</sup>rst semester, {0, 1, 0, 0} means that r is in the second semester, and so on. However, $\mathrm { i f } X _ { i } = \{ 0 , 0 , 0 , 0 \}$ then r<sub>i</sub> is not assigned to any semester, which happens for all <sup>fi</sup>nished and some elective courses.

## 3.2. Course priority

Different criteria could be used to prioritize courses when building a study plan. The proposed formulation prioritizes courses in relation to three factors: importance, grade, and chronology. The importance and grade factors determine which ‘elective’ courses to include in the study plan, and the chronology factor determines when to take ‘compulsory and elective’ courses.

## a) Importance

An importance factor $w _ { i }$ represents the amount of interest a student has for an elective course $r _ { i }$ with respect to other elective courses. The more important a course is, the more likely it will be included in the developed plan. This factor is applicable only to elective courses because all compulsory courses must be taken regardless of the student's interest in them. In the proposed approach, a student is asked to use a 9-point ordinal scale to determine the importance of each elective course, where 9 means a course is extremely important, and 1 means extremely unimportant.

## b) Grade

This factor indicates the minimum expected grade $g _ { i }$ for an un<sup>fi</sup>nished course $r _ { i \cdot }$ Elective courses with high expected-grades are more likely to be included in the study plan. This factor is used to prioritize only elective courses because of the same reason mentioned in (a) above. In the proposed approach, g is determined using letter grading scale (i.e. A, B+, B, etc.), which is converted to a numeric value that represents the letter grade.

## c) Chronology

This factor is concerned with the time at which a course is assigned in the study plan, i.e. in which semester a compulsory or an elective course should be taken. In the proposed approach, a student has two options:

• hard assignments, and

• soft assignments.

A hard assignment means that the model is “forced” to pre-assign a course r to a speci<sup>fi</sup>c semester τ in the study plan, i.e. x is pre-set to 1.

A soft assignment, on the other hand, has a more subtle impact on courses assignment. A value s is determined by students for each course $r _ { i }$ on an ordinal scale from 1 to 5 with the meanings in Table 2.

It is important to note that “as soon as possible” in the above table does not translate to “the immediately coming semester”. A course could be assigned to a semester only if its prerequisites were taken in previous semesters. To estimate the “<sup>fi</sup>rst semester that a course r could be assigned to” (i.e., “as soon as possible”), a factor called ‘Nearest Starting Semester (NSS )’ is calculated for each course r based on its prerequisite course structure. The algorithm of calculating NSS is discussed in Appendix A.

In order to implement the relaxed effect of soft assignment values, a set $U _ { i } = \{ u _ { i , t } : t = 1 \ldots T \}$ is generated for each value of $s _ { i } ,$ where $u _ { i , \mathrm { ~ i ~ } }$ indicates how preferable a course $r _ { i }$ is to be assigned to a semester t. For example, assume a student chooses $s _ { i } = 3$ and $T = 7 . 8$ corresponding set $U _ { i } = \{ 0 . 0 0 2 , 0 . 0 6 4 , 0 . 5 , 1 , 0 . 5 , 0 . 0 6 4 , 0 . 0 0 2 \}$ indicates that the fourth semester has the highest preference value $( u _ { i , 4 } = 1 )$ , and that other semesters have less preferences. The proposed model would only assign a course to a less-preferred semester if this assignment has a better overall impact on the study plan. ‘Better’ here is estimated in terms of the overall value of the study plan (Section 3.5), and the satisfaction of the problem constraints (Sections 3.3 and 3.4).

The values of $U _ { i }$ are generated using a normal distribution function with the mean determined based on both s and NSS (the mean cannot be set to a value less than NSS<sub>i</sub>), and with a standard deviation set to 0.85; this value is chosen based on trial-and-error. The values of $U _ { i }$ are normalized to the range from 0 to 1.

Relationship between priority factors: The above three priority factors, importance, grade, and chronology, are independent. For example, a course $r _ { i }$ could be very important, and yet assigned towards the end of a study plan.

## 3.3. Course dependencies

Various dependencies between courses are possible. In this paper, three types of dependencies are considered: precedence, succession, and concurrency.

Precedence is related to the fact that many advanced courses have prerequisite courses that a student must <sup>fi</sup>nish before registering the advanced course. A special case of precedence relationship includes successive courses, which are pairs of courses that should be given in two consecutive semesters because the later course is a continuation of, or strongly dependent on, the earlier one. Finally, concurrent courses are those ones that should be assigned to the same semester because they complement each other.

The above three dependency types are illustrated in Table 3 for two courses $r _ { i }$ and $r _ { j } .$

The proposed formulation provides two approaches to implement the above three dependency relationships:

• hard dependency, and

• soft dependency.

Hard dependencies are modeled as hard constraints on the generated solution. Assuming that $X _ { i }$ and $X _ { j }$ are decision variables for two courses $r _ { i }$ and $r _ { j } ,$ and t is a semester in the study plan, the model must satisfy the following constraint:

$$
\boldsymbol {t} _ {\left(\text { where } x _ {j, t} = 1\right)} - \boldsymbol {t} _ {\left(\text { where } x _ {i, t} = 1\right)} = \mu
$$

where

$$
\mu \left\{ \begin{array}{l l} \geq 1 & \Leftrightarrow \quad \left(r _ {i} B E F O R E r _ {j}\right) \\ = 1 & \Leftrightarrow \quad \left(r _ {i} T H E N r _ {j}\right) \\ = 0 & \Leftrightarrow \quad \left(r _ {i} W I T H r _ {j}\right) \end{array} \right..
$$

A soft dependency, on the other hand, implies a preference to implement the relationship without an obligation to do so. This is implemented using the ‘soft assignment’ parameter that was discussed in Section 3.2 (c) where courses are given soft-assignments that re<sup>fl</sup>ect the dependency types between them.

## 3.4. Constraints

In addition to the above factors, the proposed model de<sup>fi</sup>nes eight hard constraints that must be ful<sup>fi</sup>lled when assigning courses to semesters in the suggested study plan.

## a) Must-take elective courses

In special cases, a student must take speci<sup>fi</sup>c elective courses because

## Table 2

Meaning of soft assignment values (s ).

<table><tr><td>Value</td><td>Meaning</td></tr><tr><td>1</td><td>I want to take the course as soon as possible</td></tr><tr><td>3</td><td>I want to take the course around the middle of my study plan.</td></tr><tr><td>5</td><td>I want to take the course near graduation</td></tr></table>

Even numbers can be interpreted as a re<sup>fi</sup>nement of values above and below.

of certain obligations, $\mathrm { e . g . , a }$ job requirement. The proposed approach handles such situations by modeling those elective courses as compulsory ones. Suppose that $R _ { e l e c t M u s t } \subset R _ { e l e c t }$ is the set of elective courses that a student must take, then

$$
\forall r _ {i} \in R _ {\text { electMust }}: \sum_ {t} x _ {i, t} = 1.
$$

## b) Course availability

Some courses may be offered in speci<sup>fi</sup>c semesters but not in others. Suppose that the academic year consists of two semesters: fall and spring,<sup>2</sup> and assume that $R _ { f } \subseteq R$ is a set of courses that are only offered in fall semesters, and $t _ { s }$ indicates spring semesters, then:

$$
\forall r _ {i} \in R _ {f}, \forall t _ {s} \in T: \quad \boldsymbol {x} _ {\boldsymbol {i}, \boldsymbol {t} _ {s}} = 0.
$$

Similarly, if $R _ { s } \subseteq R$ is the set of courses that are only offered in spring semesters, and $t _ { f }$ indicates fall semesters, then

$$
\forall r _ {i} \in R _ {s}, \forall t _ {f} \in T: x _ {i, t _ {f}} = 0.
$$

## c) Credit hours per semester

A course credit (a.k.a. credit hour) is a number that represents the weight, value, or time requirement of a course in an academic program. Many universities place a limit on the credit-hour load per semester. This limit may change for different cases; e.g., full-time versus part-time students, high versus low GPA students, and spring versus summer semesters. The proposed model tries to accommodate these cases using a formula where the maximum and minimum credits is de<sup>fi</sup>ned per case each semester. Assume that a course r<sub>i</sub> is worth $h _ { i }$ credit hours, and assume that $a _ { t }$ and $b _ { t }$ indicate the minimum and maximum credit hours that a student can register in a semester t. Suggested study plans must satisfy the following:

$$
\forall t: a _ {t} \leq \sum_ {i} h _ {i} \cdot x _ {i, t} \leq b _ {t}.
$$

## d) Number of courses per semester

A student may prefer to have a limit on the number of courses s/he registers per semester. Assuming that $n _ { t }$ is the maximum number of courses for a semester t, the model must satisfy the following:

$$
\forall t: \sum_ {i} x _ {i, t} \leq n _ {t}.
$$

## e) GPA per semester

Students who have low cumulative grade point average (GPA) might be at risk of dismissal if their unsatisfactory work continues for several successive semesters. This issue is considered in the proposed model by including the following constraint:

$$
\forall t: G _ {t} \geq \psi_ {t}
$$

where $G _ { t }$ is the cumulative GPA calculated at a semester t based on the generated plan, and $\psi _ { t }$ is the minimum required GPA for that semester. Usually, $\psi _ { t }$ takes the same value for all semesters, which represents the minimum acceptable GPA, e.g., 2.0. However, if a student is on academic probation, and s/he need to increase his/her GPA to above a certain threshold, but s/he cannot achieve this in one semester, then $\psi _ { t }$ should be progressively increased over two (or more) semesters until it reaches the required level.

## f) Budget per semester

Students may have limited budgets for paying their tuition fees. Assuming that $\beta _ { t }$ is the budget for a semester $t , \epsilon _ { i }$ is the registration fees for a course $r _ { i } ,$ and ε represents any extra fees paid for a semester t, e.g., admission fees, processing fees, IT fees, etc., then:

$$
\forall t: \sum_ {i} \epsilon_ {i} \cdot x _ {i, t} + \varepsilon_ {t} \leq \beta_ {t}.
$$

g) Total credit hours for elective courses

Graduation requirements in many universities state that a student must <sup>fi</sup>nish a subset of elective courses of which sum of credits $h _ { i }$ exceeds a certain threshold λ. This can be expressed as follows:

$$
\lambda \leq \sum_ {t} \sum_ {i = v + 1} ^ {w} h _ {i} \cdot x _ {i, t} \leq \lambda + c
$$

where c is a non-negative integer; c is assigned a positive value only if a student chooses to take more elective credits than the minimum requirement.<sup>3</sup>

h) Student leave

Universities usually encourage their students to maintain a continuous registration in an academic program. However, it is sometimes necessary for a student to take a leave of absence for one or more semesters. If a student using IDiSC<sup>+</sup> wants to take a leave from enrollment during a future semester τ, then

• parameters $a _ { \tau } , ~ b _ { \tau } , ~ n _ { \tau }$ , and $\beta _ { \tau }$ should be set to zero, and

• the generated study plan will satisfy the following:

$$
\forall \boldsymbol {r} _ {\boldsymbol {i}}: x _ {i, \tau} = 0.
$$

## 3.5. Objective function

The objective function brings together the problem aspects as described so far. Typically, planning for a study plan aims to: (a) maximize students' satisfaction about the study plan, and (b) achieve a high GPA at graduation; both aims should be approached without violating any university or student hard constraints.

Aim (a) is in<sup>fl</sup>uenced by two factors: w , which indicates how important an elective course, and $u _ { i , t } ,$ which re<sup>fl</sup>ects a student's preference about the time of taking a course. Aim (b) is in<sup>fl</sup>uenced by one factor: the expected grade $g _ { i \cdot }$ The proposed objective function brings these aims in a balanced way. The objective is to maximize function $F ( x )$ subject to the satisfaction of the problem constraints:

$$
F (x) = \sum_ {i} \left(w _ {i} \cdot \left(g _ {i}\right) ^ {\vartheta} \cdot \sum_ {t} u _ {i, t} \cdot x _ {i, t}\right)
$$

where ϑ is a user con<sup>fi</sup>gurable exponential weight that determines the relative impact of the grade g on the overall value of the objective function. The idea of using exponential weights lies in the Multiple Attribute Theory, speci<sup>fi</sup>cally the weighted product method [26]. The parameter ϑ is introduced based on the feedback received from expert advisors who stressed that if we want to consider students' preferences properly, the in<sup>fl</sup>uence that course grades have on study plans should be determined per student case. The value of ϑ ranges from 0.5 to 2.0, where 0.5 means that g is of a very low impact, and 2.0 means a very high impact. In the case study presented at the end of the paper, the relevant student and his advisors suggested that it is crucial to consider elective courses with higher grades, and therefore ϑ was set to 2. One should be careful not to choose higher values of ϑ otherwise it could dominate the solution.

## 4. The IDiSC <sup>+</sup> approach

Similarly to the former IDiSC approach [13,14], the improved IDiSC<sup>+</sup> approach follows EVOLVE\*, which is an iterative an evolutionary decision support framework originally proposed in [12]. EVOLVE\* provides decision support using hybrid intelligence that brings computational and human intelligence together. This is achieved through three main phases (Fig. 1(a)):

## 4.1. Overview

(1) The modeling phase, in which students and university administration de<sup>fi</sup>ne the problem settings based on the problem formulation described in Section 3 (e.g. constraint values, courses fees, etc.).

(2) The exploration phase, in which a computer relies on the formal model to generate alternative study plans. The formal model constitutes an integer programming problem [27] as all decision variables are integers, and it is solved by means of branch-andbound techniques [28]. A software tool called LINGO [29] is employed to search for optimized solutions. LINGO has been used by many researchers in the <sup>fi</sup>eld of Operations Research, e.g., [30,31]. LINGO has a scripting language that allows expressing a problem in a way similar to standard mathematical notation. Further details about how LINGO is used to optimally solve the given formulation are discussed in Appendix B.

As with most other optimization packages, LINGO can only generate one solution for any given problem. In order to achieve the goal of generating a set of alternative solutions, the diversi<sup>fi</sup>- cation technique described in Section 4.2 is used.

(3) The consolidation phase. In this phase, decision makers analyze the solutions generated in the exploration phase, and then either accept one of these solutions or adjust the problem settings in order to generate re<sup>fi</sup>ned solutions in further iterations. In addition, decision makers may perform what-if analysis in this phase where they examine the impact of changing the problem settings on the output.

Fig. 1(b) illustrates the two aspects that IDiSC<sup>+</sup> improves, i.e. the extended formal model as was introduced in Section 3, and the ability to generate a set of alternative quali<sup>fi</sup>ed solutions, which is discussed in the next section.

## 4.2. Searching for alternative solutions

The formal model described in Section 3 represents a typical optimization problem that could be solved by optimization packages such as LINGO. As stated above, LINGO can provide exactly one solution for each set of problem settings. However, for providing decision support under uncertainty, it is suggested to provide a set of alternative solutions that are quali<sup>fi</sup>ed and diversi<sup>fi</sup>ed rather than providing only one optimum solution [12,32]. The following two subsections explain the concept of quali<sup>fi</sup>ed and diversi<sup>fi</sup>ed solutions, and they discuss how such solutions could be generated using existing optimization packages.

## 4.2.1. Qualified solutions

In this paper, quali<sup>fi</sup>ed solutions are feasible study-plans that achieve high object-function values based on the given formulation. Quali<sup>fi</sup>ed solutions are generated as follows: assume that LINGO identi<sup>fi</sup>es a solution $X _ { 0 }$ with the maximum possible objective function value equal to F(X ). A quali<sup>fi</sup>ed solution is de<sup>fi</sup>ned as any solution $X _ { n }$ that possesses two characteristics [32]:

• $X _ { n }$ lies in the feasible space delimited by the problem constraints.

$F ( X _ { n } ) \geq \alpha \cdot F ( X _ { 0 } )$ , where α is a prede<sup>fi</sup>ned quality level,

$$
\alpha \in (0, 1 ].
$$

![](/api/attachments/273UP4RS/fulltext/images/592154e57165e00042d1de7ca01feb98e60008c51ab4cd7c0697da81b7bf2d56.jpg)  
Fig. 1. IDiSC<sup>+</sup> following the EVOLVE\* framework.

This paper suggests a quality level α = 0.95 in order to address the uncertainty involved when de<sup>fi</sup>ning the values of problem parameters. Requiring higher accuracy would make little sense with such uncertainty.

As mentioned earlier, the aim of identifying several quali<sup>fi</sup>ed solutions is to allow addressing implicit concerns not formally described in the original problem statement. In fact, the quality of the generated quali<sup>fi</sup>ed solutions is very similar, but they may differ in terms of their ability to accommodate additional concerns.

## 4.2.2. Diversified solutions

The generated alternative solutions should not only be quali<sup>fi</sup>ed but also different, otherwise they are not really alternatives. Diversi<sup>fi</sup>cation is a technique that provides more ef<sup>fi</sup>cient support to decision makers by providing a portfolio of quali<sup>fi</sup>ed and diversi<sup>fi</sup>ed solutions [32], giving decision makers the opportunity to review different alternatives with guaranteed level of quality. IDiSC<sup>+</sup> suggests three alternative solutions (study plans) as this number seems to be a suitable for <sup>fi</sup>nal human decision-making.

![](/api/attachments/273UP4RS/fulltext/images/6384c75f6bd8450f720e113882d18eadb031dbcaae0cfe9afd4a70eb523208d7.jpg)  
Fig. 2. Diversi<sup>fi</sup>cation algorithm

Achieving diversi<sup>fi</sup>cation may be done by several strategies. One of them was introduced in [32] in which a subset of the feasible space is searched for the most diversi<sup>fi</sup>ed solutions. However, this strategy, although provides quick results, does not guarantee the identi<sup>fi</sup>cation of quali<sup>fi</sup>ed solutions with maximum diversi<sup>fi</sup>cation among the whole feasible space.

IDiSC<sup>+</sup> uses another diversi<sup>fi</sup>cation algorithm [33] which searches the whole set of quali<sup>fi</sup>ed solutions for maximally diversi-<sup>fi</sup>ed ones. This strategy takes more time compared to [32]. However, in case of generating few alternative solutions, the increase would be in terms of seconds, which is tolerable during student advising. The proposed diversi<sup>fi</sup>cation algorithm works as follows (Fig. 2):

1. Search for $X _ { 0 }$ based on original problem formulation.

2. Set $\eta = 1$ , where η is the number of structural differences that any two plans in the <sup>fi</sup>nal solution set should have.

3. Search for two solutions $X _ { 1 }$ then X<sub>2</sub> while maintaining η structural differences as follows:

a. Search for a solution $X _ { 1 }$ according to the original problem formulation in addition to 2 constraints:

$X _ { 1 }$ must have η structural differences with $X _ { 0 } .$

$X _ { 1 }$ is quali<sup>fi</sup>ed, i.e., $F ( X _ { 1 } ) \geq 0 . 9 5 \cdot F ( X _ { 0 } )$

b. Search for a solution $X _ { 2 }$ according to the original problem formulation in addition to 3 constraints:

$X _ { 2 }$ must have η structural differences with $X _ { 0 } .$

$X _ { 2 }$ must have η structural differences with $X _ { 1 }$

$X _ { 2 }$ is quali<sup>fi</sup>ed, i.e., $F ( X _ { 2 } ) \geq 0 . 9 5 \cdot F ( X _ { 0 } )$

4. If the optimization package successfully <sup>fi</sup>nds $X _ { 1 }$ and $X _ { 2 } ,$ then store all identi<sup>fi</sup>ed solutions in the <sup>fi</sup>nal solution set, $S O L = \{ X _ { 0 } , X _ { 1 } , X _ { 2 } \}$

5. Increment η.

6. Repeat steps 3 to 5 until the optimization package fails to <sup>fi</sup>nd either $X _ { 1 }$ or $X _ { 2 } .$ When this happens, approve the last saved set SOL as the required portfolio of solutions.

The performance of the above algorithm could be improved by modifying the initial value of η and the way it changes. For example, η could be incremented by a large value, and once the optimization package fails to <sup>fi</sup>nd $X _ { 1 }$ or $X _ { 2 } ,$ η should be gradually decremented until a solution is found.

## 5. Validation

In order to validate and illustrate IDiSC<sup>+</sup>, a student case based on real-world settings is considered in this section.

## 5.1. Context

The faculty of computer studies offers 38 courses for its students: 28 compulsory courses (r1 to r28) and 10 elective courses (r29 to r38). In order for a student to graduate, s/he needs to <sup>fi</sup>nish all compulsory courses in addition to 9 credit hours from the elective courses within a maximum of 8 years. A student is allowed to take a leave of absence for up to two semesters.

A student gets an ‘academic warning’ whenever s/he gets a GPA less than 2.0. A student is expelled from the university if s/he gets four academic warnings in four consecutive semesters.

Students with up to one academic warning are allowed to register between 8 and 21 credit hours per semester, except for the graduation (last) semester during which they are allowed to register 24 credit hours. A student with two or three academic warnings may register up to 16 credit hours only.

Table 4 lists the data required to run IDiSC<sup>+</sup>. The left half of the table includes the data provided by the university administration, which include all courses along with their weights (credit hours), fees, and interdependency relationships, i.e. the precedence, succession, and concurrency relationships. The academic year is divided into two semesters, fall and spring,<sup>4</sup> during which most courses are offered. An exception is for r19 and r27, which are only offered in the fall semester, and r20 and r28, which are only offered in the spring semester.

Table 3  
Dependencies between courses

<table><tr><td>Type</td><td>Relationship</td><td>Description</td></tr><tr><td>Precedence</td><td> $r_i$  before  $r_j$ </td><td> $r_i$  should be assigned to a semester preceding the one to which  $r_j$  is assigned.</td></tr><tr><td>Succession</td><td> $r_i$  then  $r_j$ </td><td> $r_j$  should be assigned to the semester immediately following the semester to which  $r_i$  is assigned.</td></tr><tr><td>Concurrency</td><td> $r_i$  with  $r_j$ </td><td> $r_i$  and  $r_j$  should be assigned to the same semester</td></tr></table>

## 5.2. Case study

The case considered in this section is for a student who is at risk of dismissal from the university. The student's GPA is 1.53, and he already has two academic warnings. This means his GPA must be increased to 2.0 or more within a maximum of 2 semesters. To be on the safe side, IDiSC<sup>+</sup> was set to make a plan that helps the student increase his GPA to 2.0 after the <sup>fi</sup>rst coming semester.

The student had already <sup>fi</sup>nished some courses of which grades are given under the ‘Grade (previous)’ column in Table 4. A previous grade of ‘F’ indicates that the student had failed this course in a previous semester. The student was asked to estimate the ‘expected grade’ for the un<sup>fi</sup>nished courses; this was done with the help of the academic advisor. In addition, the student was asked to give his preferences in terms of chronology and importance of each course as shown in right half of Table 4.

The number of academic semesters until graduation was set by the student to seven. Then, the student was asked to set his maximum budget and the number of courses he can handle per semester (see Table 5 — a dash ‘–’ means not applicable). The student expressed his desire to take a leave of absence in the fourth semester, which is why some values under T4 in Table 5 are set to zero.

Based on the data given in Tables 4 and 5, IDiSC<sup>+</sup> generated three study plans — Fig. 3 (Top). We can see in all suggested plans that: (i) the student's GPA is increased to above 2.0 after the <sup>fi</sup>rst semester, (ii) the system satis<sup>fi</sup>ed all hard constraints and tried to satisfy most of the soft constraints, (iii) the system chose the elective course with the highest preference and grade combined, and (iv) the system assigned no courses to semester T4 as requested by student.

As an added value, the three plans are structurally different, giving the student some additional <sup>fl</sup>exibility. With the aid of the academic advisor, the student evaluated these plans based on their knowledge and experience before making a decision. A risk was identi<sup>fi</sup>ed: while the student originally stated that he could handle four courses per semester, the advisor suggested that three courses for the <sup>fi</sup>rst two semesters is recommended to avoid the risk of not achieving the required GPA and hence being subject to dismissal. Based on this, the constraints were updated as seen in Table 6 (updates are underlined), and IDiSC<sup>+</sup> was run again — the new plans are shown in Fig. 3 (Bottom).

## 6. Discussion

## 6.1. Usefulness

As demonstrated in the case study, generating alternative solutions added <sup>fl</sup>exibility for students and their advisors to review several plans with similar quality but different structures. The number of structural differences was not too large such that the plans were completely different, and yet not too small such that they were extremely similar. Such balance provided the required <sup>fl</sup>exibility without confusing the decision makers with too many variations. As seen in Fig. 3, we can easily spot the differences between the generated plans, and we can see that they are manageable. By analyzing such differences, students should be able to better understand their choices and thus make appropriate decisions, either by accepting one of the plans or by re<sup>fi</sup>ning the problem settings in order to generate further plans.

Table 4 Courses and student<sup>'</sup>s status.  
A. Mohamed / Decision Support Systems 74 (2015) 33
–45

<table><tr><td rowspan="3" colspan="2">Course ( $r_{\alpha}$ )</td><td rowspan="2" colspan="2">Offering semester</td><td rowspan="3">Credit hours</td><td rowspan="3">Fees ($)</td><td rowspan="3">Default soft assignment  $s_{\alpha}$ </td><td colspan="6">Relationships with other courses ( $r_{\beta}$ )</td><td colspan="5">Student case</td></tr><tr><td colspan="2">Precedence ( $r_{\beta}$  before  $r_{\alpha}$ )</td><td colspan="2">Succession ( $r_{\alpha}$  then  $r_{\beta}$ )</td><td colspan="2">Concurrency ( $r_{\alpha}$  with  $r_{\beta}$ )</td><td colspan="2">Grade</td><td colspan="2">Chronology</td><td rowspan="2">Importance</td></tr><tr><td>Fall</td><td>Spring</td><td>Hard</td><td>Soft</td><td>Hard</td><td>Soft</td><td>Hard</td><td>Soft</td><td>Previous</td><td>Expected</td><td>Hard</td><td>Soft</td></tr><tr><td rowspan="28">Compulsory courses</td><td>r1</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>-</td><td>-</td><td>-</td><td>r2</td><td>-</td><td>-</td><td>C+</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r2</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>2</td><td>r1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r3</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>-</td><td>-</td><td>r4</td><td>-</td><td>-</td><td>-</td><td>C+</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r4</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>r3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C+</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r5</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r6</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r7</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>-</td><td>-</td><td>-</td><td>r11</td><td>-</td><td>-</td><td>F</td><td>C</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r8</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>4</td><td>r10</td><td>-</td><td>-</td><td>-</td><td>-</td><td>r25</td><td>-</td><td>C</td><td>-</td><td>3</td><td>-</td></tr><tr><td>r9</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>2</td><td>r3</td><td>r14</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>2</td><td>-</td></tr><tr><td>r10</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>4</td><td>r3</td><td>r12,r14</td><td>-</td><td>-</td><td>-</td><td>-</td><td>F</td><td>C</td><td>-</td><td>2</td><td>-</td></tr><tr><td>r11</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>2</td><td>r7</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>2</td><td>-</td></tr><tr><td>r12</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>r3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>-</td><td>2</td><td>-</td></tr><tr><td>r13</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>F</td><td>B</td><td>-</td><td>2</td><td>-</td></tr><tr><td>r14</td><td>✓</td><td>✓</td><td>4</td><td>270</td><td>1</td><td>r3</td><td>-</td><td>r15</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r15</td><td>✓</td><td>✓</td><td>4</td><td>270</td><td>2</td><td>r14</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r16</td><td>✓</td><td>✓</td><td>4</td><td>270</td><td>2</td><td>r3</td><td>-</td><td>r17</td><td>-</td><td>-</td><td>-</td><td>F</td><td>B</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r17</td><td>✓</td><td>✓</td><td>4</td><td>270</td><td>2</td><td>r16</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r18</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>4</td><td>r10,r12</td><td>r21</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C</td><td>-</td><td>2</td><td>-</td></tr><tr><td>r19</td><td>✓</td><td>X</td><td>8</td><td>432</td><td>3</td><td>r16</td><td>-</td><td>r20</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>3</td><td>-</td></tr><tr><td>r20</td><td>X</td><td>✓</td><td>8</td><td>432</td><td>3</td><td>r19</td><td>r17</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>5</td><td>-</td></tr><tr><td>r21</td><td>✓</td><td>✓</td><td>5</td><td>324</td><td>3</td><td>r10</td><td>-</td><td>-</td><td>r10</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>1</td><td>-</td></tr><tr><td>r22</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>3</td><td>-</td></tr><tr><td>r23</td><td>✓</td><td>✓</td><td>8</td><td>432</td><td>3</td><td>r10</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C</td><td>-</td><td>3</td><td>-</td></tr><tr><td>r24</td><td>✓</td><td>✓</td><td>8</td><td>432</td><td>4</td><td>r20</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>4</td><td>-</td></tr><tr><td>r25</td><td>✓</td><td>✓</td><td>8</td><td>432</td><td>4</td><td>r18</td><td>-</td><td>-</td><td>r27</td><td>-</td><td>r8</td><td>-</td><td>B</td><td>-</td><td>4</td><td>-</td></tr><tr><td>r26</td><td>✓</td><td>✓</td><td>8</td><td>432</td><td>5</td><td>r21</td><td>-</td><td>-</td><td>-</td><td>r27</td><td>-</td><td>-</td><td>C</td><td>-</td><td>4</td><td>-</td></tr><tr><td>r27</td><td>✓</td><td>X</td><td>4</td><td>270</td><td>5</td><td>r25</td><td>-</td><td>r28</td><td>-</td><td>r26</td><td>-</td><td>-</td><td>B</td><td>-</td><td>5</td><td>-</td></tr><tr><td>r28</td><td>X</td><td>✓</td><td>4</td><td>270</td><td>5</td><td>r27</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B</td><td>-</td><td>5</td><td>-</td></tr><tr><td rowspan="10">Elective courses</td><td>r29</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C</td><td>-</td><td>3</td><td>5</td></tr><tr><td>r30</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C</td><td>-</td><td>3</td><td>5</td></tr><tr><td>r31</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>A</td><td>-</td><td>3</td><td>5</td></tr><tr><td>r32</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>B+</td><td>-</td><td>-</td><td>3</td><td>1</td></tr><tr><td>r33</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>3</td><td>1</td></tr><tr><td>r34</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C+</td><td>-</td><td>3</td><td>7</td></tr><tr><td>r35</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>C</td><td>-</td><td>3</td><td>1</td></tr><tr><td>r36</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>3</td><td>r17</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>3</td><td>1</td></tr><tr><td>r37</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>4</td><td>r17</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>4</td><td>1</td></tr><tr><td>r38</td><td>✓</td><td>✓</td><td>3</td><td>216</td><td>5</td><td>r15</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>D</td><td>-</td><td>5</td><td>7</td></tr></table>

Constraints per semester for the <sup>fi</sup>rst iteration.

<table><tr><td rowspan="2">Constraints per semester</td><td colspan="7">Minimum values</td><td colspan="7">Maximum values</td></tr><tr><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td></tr><tr><td>Number of courses</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>4</td><td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Credit hours</td><td>8</td><td>8</td><td>8</td><td>0</td><td>8</td><td>8</td><td>8</td><td>16</td><td>21</td><td>21</td><td>0</td><td>21</td><td>21</td><td>24</td></tr><tr><td>Budget ($)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1500</td><td>1500</td><td>1500</td><td>0</td><td>1500</td><td>1500</td><td>1500</td></tr><tr><td>GPA</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td></tr></table>

Considering the way the proposed approach was designed, it is not possible to have completely different plan structures. All generated plans must satisfy the same set of constraints, and they all must exceed a certain quality threshold. The quality is measured in terms of the objective function value. Guaranteeing that a plan has such high quality is achieved by forcing a constraint that the objective-function value of a selected plan must exceed 95% of the maximum objective-function value found by the optimization package (i.e., LINGO in this paper) under the given constraints.

IDiSC<sup>+</sup> was designed with a comprehensive, realistic and adaptable formal model. The model realistically represents the current regulations of the university under investigation; it does not make impractical assumptions, nor does it ignore any of that university's rules or policies. The model can be easily adapted to different university environments. By modifying the constraints, the approach can cope to new situations. For example, assume that students are required to <sup>fi</sup>nish a minimum number of elective credits with a constraint on the study areas, e.g., “each student must finish a total of 15 elective hours, and s/he must take at least two elective courses from area A and three elective courses from area B”. The current formulation can be easily adapted to implement this requirement as explained in Appendix C.

IDiSC<sup>+</sup> was created as a student-centered approach. IDiSC<sup>+</sup> focuses on each student's speci<sup>fi</sup>c case, re<sup>fl</sup>ecting his/her interests, preferences, and abilities, and it acknowledges student voice as central to the planning process, distinguishing itself from similar technologies found in the technical literature. The plans suggested by IDiSC<sup>+</sup> are optimized around how and when students want, need, or can handle different courses throughout their higher education experience. Students are able to control their GPA per semester through proper planning. They can choose the length of the study plan, the time they want to be on a leave, the course priorities and the relative importance of these priorities, the number of courses and credit hours per semester, as well as their maximum budget per semester. A student can also choose to accept one of the suggested plans or reject them all and re<sup>fi</sup>ne the settings for generating further plans.

<table><tr><td colspan="21">Three Study Plans After Iteration 1</td><td></td></tr><tr><td colspan="8">Study Plan SP1</td><td colspan="7">Study Plan SP2</td><td colspan="6">Study Plan SP3</td><td></td></tr><tr><td>Finished</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td></tr><tr><td>r1 r6</td><td>r7</td><td>r9</td><td>r11</td><td></td><td>r19</td><td>r20</td><td>r8</td><td>r7</td><td>r11</td><td>r9</td><td></td><td>r19</td><td>r20</td><td>r8</td><td>r7</td><td>r13</td><td>r11</td><td></td><td>r8</td><td>r20</td><td>r22</td></tr><tr><td>r2 r12</td><td>r10</td><td>r13</td><td>r18</td><td></td><td>r22</td><td>r26</td><td>r23</td><td>r10</td><td>r17</td><td>r13</td><td></td><td>r25</td><td>r26</td><td>r23</td><td>r9</td><td>r17</td><td>r23</td><td></td><td>r19</td><td>r26</td><td>r24</td></tr><tr><td>r3 r14</td><td>r16</td><td>r17</td><td>r31</td><td></td><td>r25</td><td>r27</td><td>r24</td><td>r16</td><td>r18</td><td>r22</td><td></td><td>r34</td><td>r27</td><td>r24</td><td>r10</td><td>r18</td><td>r31</td><td></td><td>r25</td><td>r27</td><td>r28</td></tr><tr><td>r4 r15</td><td></td><td>r21</td><td>r34</td><td></td><td></td><td></td><td>r28</td><td></td><td>r21</td><td>r31</td><td></td><td></td><td></td><td>r28</td><td>r16</td><td>r21</td><td>r34</td><td></td><td></td><td></td><td></td></tr><tr><td>r5 r32</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td># of Courses</td><td>3</td><td>4</td><td>4</td><td>0</td><td>3</td><td>3</td><td>4</td><td>3</td><td>4</td><td>4</td><td>0</td><td>3</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>0</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Credit Hours</td><td>10</td><td>15</td><td>12</td><td>0</td><td>19</td><td>20</td><td>23</td><td>10</td><td>15</td><td>12</td><td>0</td><td>19</td><td>20</td><td>23</td><td>13</td><td>15</td><td>17</td><td>0</td><td>19</td><td>20</td><td>15</td></tr><tr><td>Cost</td><td>702</td><td>918</td><td>1080</td><td>0</td><td>1296</td><td>864</td><td>1296</td><td>702</td><td>1080</td><td>1134</td><td>0</td><td>1080</td><td>864</td><td>1296</td><td>918</td><td>1134</td><td>1080</td><td>0</td><td>1080</td><td>864</td><td>1080</td></tr><tr><td>Expected GPA</td><td>2.07</td><td>2.42</td><td>2.43</td><td>2.43</td><td>2.56</td><td>2.45</td><td>2.37</td><td>2.07</td><td>2.18</td><td>2.46</td><td>2.46</td><td>2.56</td><td>2.45</td><td>2.37</td><td>2.13</td><td>2.40</td><td>2.39</td><td>2.39</td><td>2.48</td><td>2.40</td><td>2.37</td></tr><tr><td colspan="21">Three Study Plans After Iteration 2</td><td></td></tr><tr><td colspan="8">Study Plan SP1</td><td colspan="7">Study Plan SP2</td><td colspan="6">Study Plan SP3</td><td></td></tr><tr><td>Finished</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>t7</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td></tr><tr><td>r1 r6</td><td>r7</td><td>r17</td><td>r9</td><td></td><td>r22</td><td>r24</td><td>r8</td><td>r7</td><td>r9</td><td>r13</td><td></td><td>r8</td><td>r24</td><td>r11</td><td>r7</td><td>r13</td><td>r9</td><td></td><td>r8</td><td>r24</td><td>r11</td></tr><tr><td>r2 r12</td><td>r10</td><td>r19</td><td>r13</td><td></td><td>r25</td><td>r26</td><td>r11</td><td>r10</td><td>r19</td><td>r18</td><td></td><td>r25</td><td>r26</td><td>r17</td><td>r10</td><td>r19</td><td>r18</td><td></td><td>r22</td><td>r26</td><td>r17</td></tr><tr><td>r3 r14</td><td>r16</td><td>r21</td><td>r18</td><td></td><td>r31</td><td>r27</td><td>r23</td><td>r16</td><td>r21</td><td>r20</td><td></td><td>r31</td><td>r27</td><td>r23</td><td>r16</td><td>r21</td><td>r20</td><td></td><td>r25</td><td>r27</td><td>r23</td></tr><tr><td>r4 r15</td><td></td><td></td><td>r20</td><td></td><td>r34</td><td></td><td>r28</td><td></td><td></td><td>r22</td><td></td><td>r34</td><td></td><td>r28</td><td></td><td></td><td>r34</td><td></td><td>r31</td><td></td><td>r28</td></tr><tr><td>r5 r32</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td># of Courses</td><td>3</td><td>3</td><td>4</td><td>0</td><td>4</td><td>3</td><td>4</td><td>3</td><td>3</td><td>4</td><td>0</td><td>4</td><td>3</td><td>4</td><td>3</td><td>3</td><td>4</td><td>0</td><td>4</td><td>3</td><td>4</td></tr><tr><td>Credit Hours</td><td>10</td><td>17</td><td>17</td><td>0</td><td>17</td><td>20</td><td>18</td><td>10</td><td>16</td><td>17</td><td>0</td><td>17</td><td>20</td><td>19</td><td>10</td><td>16</td><td>17</td><td>0</td><td>17</td><td>20</td><td>19</td></tr><tr><td>Cost</td><td>702</td><td>864</td><td>1242</td><td>0</td><td>1296</td><td>972</td><td>1080</td><td>702</td><td>864</td><td>1458</td><td>0</td><td>1080</td><td>972</td><td>1080</td><td>702</td><td>918</td><td>1188</td><td>0</td><td>1296</td><td>972</td><td>1080</td></tr><tr><td>Expected GPA</td><td>2.07</td><td>2.32</td><td>2.37</td><td>2.37</td><td>2.50</td><td>2.41</td><td>2.37</td><td>2.07</td><td>2.31</td><td>2.36</td><td>2.36</td><td>2.46</td><td>2.38</td><td>2.37</td><td>2.07</td><td>2.43</td><td>2.34</td><td>2.34</td><td>2.46</td><td>2.38</td><td>2.37</td></tr></table>

Fig. 3. Study plans generated using IDiSC<sup>+</sup>.

Table 6  
Constraints per semester for the second iteration.

<table><tr><td rowspan="2">Constraints per semester</td><td colspan="7">Minimum values</td><td colspan="7">Maximum values</td></tr><tr><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td><td>T1</td><td>T2</td><td>T3</td><td>T4</td><td>T5</td><td>T6</td><td>T7</td></tr><tr><td>Number of courses</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>3</td><td>3</td><td>4</td><td>0</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Credit hours</td><td>8</td><td>8</td><td>8</td><td>0</td><td>8</td><td>8</td><td>8</td><td>16</td><td>21</td><td>21</td><td>0</td><td>21</td><td>21</td><td>24</td></tr><tr><td>Budget ($)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1500</td><td>1500</td><td>1500</td><td>0</td><td>1500</td><td>1500</td><td>1500</td></tr><tr><td>GPA</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>2.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td><td>4.0</td></tr></table>

The inherent dynamic nature of the course-planning problem is considered in IDiSC<sup>+</sup>. Similar to the process followed in the case study, whenever changes occur (to student or university parameters) the three-phase iterative framework of IDiSC<sup>+</sup> should be used (Fig. 1): the changes should be applied to the inputs and the computer would immediately generate re<sup>fi</sup>ned study plans based on the updated parameters. For example, assume that after the <sup>fi</sup>rst semester in the case study we <sup>fi</sup>nd that our student does not achieve the expected GPA. It would then be imperative to feed the new GPA to IDiSC<sup>+</sup> and generate updated plans. Practically, when any change occurs, students usually revisit their study plans and adjust them, probably with the help of an academic advisor. IDiSC<sup>+</sup> can be used then to save time and effort and provide better support to both students and their advisors.

In this context, one should pay attention to the dynamic nature of the course offerings. Most universities prepare long-term course schedules that include a list of the ‘intended’ courses to be offered in the next few years, and during which semester they will be offered. The aim is to help students plan which courses they will take in each semester in order to complete their degrees in a timely fashion. Yet, a note is sometimes added to such long-term schedules that they are subject to change according to the actual demand. This means that course planning is not purely sequential. It usually starts by a university offering a list of courses based on the expected demand, and eventually, the university approves a set of courses based on the actual demand generated in the registration process. To cope with changes in course offerings, the list of courses entered to IDiSC<sup>+</sup> should be immediately revised whenever a change happens, and updated plans should be generated for each student accordingly.

In relevance to the above topic, IDiSC<sup>+</sup> could also be useful to administrators who build the course offerings schedule. All course plans generated by IDiSC<sup>+</sup> and con<sup>fi</sup>rmed by students could be saved in the university computer systems. And at the end of the advising period, the system could display simple statistics that show the expected demand for each course in current and future semesters. Such information could help make informed decisions related to present and future course offerings.

## 6.2. Limitations

As with any other approach, the quality of the results greatly depends on the accuracy of the input data. The IDiSC<sup>+</sup>'s inputs suffer from some uncertainties related to course priorities and problem constraints. The approach relies on the iterative and evolutionary nature of the EVOLVE\* framework to reduce these uncertainties. As more iterations are applied, students get more engaged in the process and hence their knowledge evolves, improving the accuracy of their inputs over time. Yet, there is still another uncertainty that cannot be mitigated by repeatedly applying IDiSC<sup>+</sup>: the ‘expected course grade’. Such uncertainty could be reduced by relying on students' previous performance in similar courses, i.e., the courses in the same discipline and level and with similar weights, as the basis for future expectations.

In addition, the current model does not generate plans that involve equivalent courses, i.e., courses that serve as a replacement if other courses are canceled or cannot be scheduled. In such cases, a student using IDiSC<sup>+</sup> will have two choices: (1) If an equivalent course has the same priorities (as de<sup>fi</sup>ned in Section 3.2) as the original course, then the student will simply replace the canceled course with its equivalent in his/her study plan. (2) If the student has different priorities for the equivalent course, then s/he will have to enter these values to the model and regenerate alternative study plans.

Finally, the proposed model is not directly applicable to all academic institutions. This paper, for example, considers exactly two groups of courses, compulsory and elective, where a student is required to <sup>fi</sup>nish all compulsory courses and a subset of any elective courses. In some cases, there might be more than one group of electives, and the student is required to <sup>fi</sup>nish a subset of courses from each group. Other scenarios may also exist. To accommodate such scenarios, the proposed formal model should be adapted to the target context before it could be used. An example of such an adaptation process is given in Appendix C.

## 7. Conclusions and future work

This paper introduced $\mathrm { I D i S C ^ { + } }$ , a novel decision-support approach that relies on optimization techniques in order to help students and their advisors create a long-term course plan towards graduation. In order to provide such support, several parameters related to university system, advisors expertise, and student preferences are modeled, and a pro-active analysis of the impact of the these parameters is performed by the model which eventually suggests study plans that balance students' preferences and advisors' recommendations, without violating any regulations. The formal model used by IDiSC<sup>+</sup> overcomes key assumptions and limitations of its predecessor approach, IDiSC, and thus addresses the problem in a more realistic way.

IDiSC<sup>+</sup> approach uses a novel diversi<sup>fi</sup>cation algorithm to generate a set of optimal or near optimal alternative plans that are of a similar quality and yet structurally different. These alternatives are analyzed by decision makers (students and advisors) who may either accept one of the them or re<sup>fi</sup>ne the problem settings and generate further plans in an iterative and revolutionary manner within the EVOLVE\* decision support framework.

This paper demonstrated that IDiSC<sup>+</sup> is a student-centered approach, allowing students to have full control over each aspect of the planning process, without confusing them with the technical complexities. In general, the plans suggested by IDiSC<sup>+</sup> are optimized around how and when students want or need different courses throughout their higher education study.

A real-world case student was presented to illustrate the approach and demonstrate its bene<sup>fi</sup>ts. The results obtained from the case study were promising.

It is important to note that the proposed approach does not aim to replace one-on-one student–advisor interactions. Instead, it can be used for automating some advising functions, saving time for other activities such as career counseling.

Future directions for this research include <sup>fi</sup>nding ways to reduce uncertainties relevant to estimating the expected grades for students. Instead of relying on students to estimate their future grades (even with the help of their advisors), an algorithm is needed to improve these estimations. For example, statistical analysis of students' academic history could improve our expectations of a student's future grades.

Another future task is to perform sensitivity analysis in order to test the robustness of the results provided by IDiSC<sup>+</sup> against small changes in its input. With the existence of input uncertainties, we need to test how much in<sup>fl</sup>uence these uncertainties have on the suggested solutions.

Example of nearest starting semesters.

<table><tr><td>Course</td><td>NSS</td><td>Justification</td></tr><tr><td>B</td><td>0</td><td>B could be registered in the first coming semester because A has already been finished.</td></tr><tr><td>C</td><td>1</td><td>C could be registered after one semester during which course B should be finished.</td></tr><tr><td>D</td><td>2</td><td>D could be registered after two semesters during which B and C should be finished.</td></tr></table>

A technique is also required to provide justi<sup>fi</sup>cation about course assignments. This technique should answer questions such as “Why is a course $r _ { n }$ assigned to (or not assigned to) semester $t _ { x } ? ^ { \dag }$ , “Why are both $r _ { n }$ and $r _ { m }$ assigned to (or not assigned to) the same semester?”, and “Why do we have only n courses in semester $t _ { x } ? ^ { \dag }$ . Devising a technique that provides answers to these questions (and similar ones) would increase our understanding of the generated course plans, and hence improve the process of stepwise re<sup>fi</sup>nement of the input as well as reduce uncertainties related to our choices.

## Appendix A. Nearest Starting Semester (NSS) [13]

In the context of this paper, the NSS for a course indicates the minimum number of semesters that a student must spend <sup>fi</sup>nishing the course's prerequisites before s/he is able to register it. A course cannot be assigned to a semester preceding its NSS.

To illustrate this idea, consider the following notation: assume that a course X is a prerequisite for a course Y, and that X has been already <sup>fi</sup>nished by the student in a previous semester. This is expressed using the notation:

$$
\yen \rightarrow Y
$$

In this case, the NSS for Y is equal to zero, which means that the student can register Y in the immediately coming semester. For several dependent courses, e.g., A, B, C, and D, where

$$
\mathbf {A} \rightarrow \mathrm{B} \rightarrow \mathrm{C} \rightarrow \mathrm{D}
$$

The NSS for B, C, and D would be as shown in Table 7 below.

In some cases, a course might have two or more prerequisites. In the example below, a course Z has two prerequisite courses, D and W:

$$
\begin{array}{c} \mathbb {B} \to C \to D \\ \mathbb {V} \to W \end{array} \searrow_ {\nearrow} Z
$$

In this case, the NSS for Z would be based on the largest NSS value of its prerequisites; i.e., NSS will be equal to 2 based on the prerequisites path, $\mathsf { B } \to \mathsf { C } \to \mathsf { D }$

The algorithm for estimating the NSS is shown in Fig. 4. For each course $r _ { x } ,$ the algorithm calls a function calculateNSS, which checks all possible prerequisites of $r _ { x }$ in a loop and then calculates the NSS for each of these prerequisites by recursively calling itself. The function calculateNSS has two stopping criteria to halt the recursion: (i) to reach a prerequisite course that has been previously <sup>fi</sup>nished (e.g., B or V in the above example), or (ii) to reach a course without prerequisites, except of the student being accepted at the university. Once a stopping criteria is met, the current count of prerequisites along a speci<sup>fi</sup>c path is stored in an array NSSArray. The function keeps running until it <sup>fi</sup>nishes traversing all prerequisite paths. Once that happens, the algorithm chooses the longest path of prerequisites, which indicates the NSS value of $r _ { x } .$

## Appendix B. Finding optimum solutions

The proposed model uses LINGO package [29], which riles on branch-and-bound techniques to search the feasible space, delimited by the problem constraints, for <sup>fi</sup>nding optimum or optimal solutions. In case of linear optimization models, i.e., all constraints are linear, LINGO can <sup>fi</sup>nd a global optimum solution, which is a solution that has an objective value better than, or as good as, other feasible solutions. However, in case of nonlinear models, i.e., one or more constraints are nonlinear, the solution that LINGO <sup>fi</sup>nds is merely local optimal. This means there might be other locally optimal solutions that have objective values better than the current solution. To improve the search performance for nonlinear models, LINGO offers the option to initialize the decision variables prior running the optimization. These values are used as starting points by LINGO's solver. If they are chosen close to the solution, the search time could noticeably decrease.

In the mathematical formulation proposed in this paper, all expressions are linear except for the cumulative GPA constraint, $\mathrm { i . e . , } \forall t : G _ { t } \geq \psi _ { t }$ (Section 3.4), which could be either linear or nonlinear, based on how it is calculated. In this paper, the cumulative GPA is calculated by dividing the total grade points a student obtains by the total credit hours s/he <sup>fi</sup>nished. The total grade points is the sum of multiplying course grades by their respective credit-hour values. In order to calculate $G _ { t }$ at any semester $t , \mathrm { I D i S C S ^ { + } }$ uses the following formula,<sup>5</sup>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
START
    FOR each unfinished course  $r_{i}$ 
    Create empty array NSSArray;
    CALL calculateNSS( $r_{i},0$ );
    Set NSS $_{i}$  to Max(NSSArray)
    END FOR
END
FUNCTION: void calculateNSS( $r_{x}$ , counter $_{x}$ )
    FOR each prerequisite course  $r_{p}$  //r $_{p}$  is a prerequisite for  $r_{x}$ 
    Create counter $_{p}$  and set its value to counter $_{x}$ 
    IF ( $r_{p} \neq r_{0}$  AND  $r_{p}$  is not finished) THEN //  $r_{0}$  is the acceptance of a student at the university
    INCREMENT count $_{p}$ ;
    CALL calculateNSS( $r_{p}$ , count $_{p}$ );
    ELSE
    INSERT count $_{p}$  into NSSArray;
    END IF
END FOR
END FUNCTION
</div>

Fig. 4. NSS estimation algorithm

$$
G _ {t} = \frac {\sum_ {i} \left(g _ {i} \cdot h _ {i} \cdot \sum_ {t} x _ {i , t}\right)}{\sum_ {i} \left(h _ {i} \cdot \left(R e g _ {i} \vee \sum_ {t} x _ {i , t}\right)\right)}.
$$

As can be seen, the nonlinearity of the expression comes from having decision variable in the denominator of the expression.

Can we avoid such non-linearity? Most students have good academic records, and hence their expected GPA in future semesters is most probably above the minimum requirement. For such students, including the above constraint in not necessary as it will only result to causing the model to be nonlinear without gaining a real bene<sup>fi</sup>t. Therefore, $\mathrm { I D i S C S ^ { + } }$ is designed to search for solutions in two steps:

(1) First, $\mathrm { I D i S C S ^ { + } }$ ignores the GPA constraint and solves the problem as a linear model. Once a global optimum solution is found, $\mathrm { I D i S C S ^ { + } }$ checks the satisfaction of the GPA constraint. If it is satis<sup>fi</sup>ed, then the solution is approved and the process ends, otherwise phase 2 is performed.

(2) This step is only performed when the GPA constraint is not satis-<sup>fi</sup>ed at the end of phase 1. Here IDiSCS<sup>+</sup> repeats the search process after including the GPA constraint in the optimization model, which in this case becomes a non-linear model. To improve the search performance, the results from phase 1 are used to initialize the decision variables before running LINGO.

The above two-phase process in most cases is better than to always solve the problem with the GPA constraint included from the beginning: (i) If the GPA constraint is realized after the <sup>fi</sup>rst step, then we gain the bene<sup>fi</sup>t of working on a linear model, i.e., a global optimum solution is quickly obtained. (ii) If the second step had to be performed, then using the solution from step 1 to initialize the decision variables could improve LINGO's performance.

## Appendix C. Example of extending IDiSC<sup>+</sup>

This appendix illustrates the <sup>fl</sup>exibility of the formal model presented in this paper to accommodate different university requirements. The current model considers a university system that de<sup>fi</sup>nes two sets of courses: compulsory and elective. A student is required to <sup>fi</sup>nish all compulsory courses and a minimum number of elective credits without having any requirement related to the study areas of these credits.

In a different university system, students might be required to: (i) <sup>fi</sup>nish a minimum number of credits from all elective courses, and (ii) <sup>fi</sup>nish a minimum number of credits from different study areas. For example, “a student must <sup>fi</sup>nish a total of N elective hours, and s/he must take at least two elective courses from area A and three electives from area $\mathbb { B } ^ { \nu } .$

To accommodate this requirement, the model needs to be extended by considering further attributes and constraints. Recall that $R _ { e l e c t } =$ $\{ r _ { \nu + 1 } , . . . , r _ { w } \}$ is the set of elective courses (Section 3). Suppose that we have J areas of study represented by the set $\{ A _ { 1 } , A _ { 2 } , . . . , A _ { J } \}$ . For each course $r _ { i } \in R _ { e l e c t } ,$ a set $\{ a _ { i , 1 } , a _ { i , 2 } , . . . , a _ { i J } \}$ will indicate the study areas which $r _ { i }$ covers:

$$
a _ {i, j} = \left\{ \begin{array}{l l} 1 & \text { if } r _ {i} \text { covers } A _ {j} \\ 0 & \text { if } r _ {i} \text { does   not   cover } A _ {j} \end{array} \right..
$$

For example, if we have three study areas: $A _ { 1 } , A _ { 2 } ,$ , and $A _ { 3 } ,$ then the set $\{ 1 , 0 , 1 \}$ indicates that $r _ { i }$ covers $A _ { 1 }$ and $A _ { 3 }$ but not $A _ { 2 } .$

It is imperative that each course r<sub>i</sub> is associated with at least one study area.

$$
\forall r _ {i}: \sum_ {j} a _ {i, j} \geq 1
$$

In this context, a student may express one or more of the following requirements:

• “I want to take at least n courses from study area $A " .$

• “I want to take at least ρ credits from study area $B " .$

• A combination of both of the above requirements.

Since in all cases students must <sup>fi</sup>nish a minimum number of elective credits, then the elective-hours constraint, originally stated in Section $3 . 4 ( \mathrm { g } )$ , will not be changed. However, an additional constraint should be added in correspondence to each of the above three requirements.

Case $( a ) \colon ^ { \ast } \operatorname { I }$ want to take at least n<sub>j</sub> courses from study area $A _ { j } " .$

Let $n _ { j }$ be the minimum number of elective courses a student needs to take from an area $A _ { j } .$ The model, in this case, should satisfy the following additional constraint:

$$
\forall A _ {j}: \sum_ {i = v + 1} ^ {w} \left(a _ {i, j} \cdot \sum_ {t} x _ {i, t}\right) \geq n _ {j}.
$$

To explain: since $\sum { } _ { t } x _ { i , t }$ is equal to 1 only if $r _ { i }$ is included in the suggested study plan (refer to Section 3.1), and $a _ { i , j }$ is equal to 1 only for an area $A _ { j }$ that the course $r _ { i }$ covers, then the result of $( \boldsymbol { a } _ { i , j } \cdot \sum _ { t } \boldsymbol { x } _ { i , t } )$ is equal to 1 only for the courses that belong to an area $A _ { j }$ and, at the same time, included in the study plan. This means that the above constraint will make sure that the count of the courses included in the study plan from each area $A _ { j }$ is equals to or greater than the speci<sup>fi</sup>ed threshold n for that area.

Case $( b ) \colon ^ { \ast } \operatorname { I }$ want to take at least $\rho _ { j }$ credits from study area $A _ { j } " .$

This scenario is similar to Case (a) except that each student is required to specify the number of elective credits $\rho _ { j }$ required from each area $A _ { j } .$ . Recalling that $h _ { i }$ is the number of credits for a course $r _ { i } ,$ the following additional constraint should be respected:

$$
\forall A _ {j}: \sum_ {i = v + 1} ^ {w} \left(h _ {i} \cdot a _ {i, j} \cdot \sum_ {t} x _ {i, t}\right) \geq \rho_ {j}.
$$

Case (c): a combination of (a) and (b).

This case describes the situation in which a student wants to choose a number of courses from one study area and a minimum of electivecredits from another area. In this case, the model should selectively apply the above two constraints on various study areas; i.e. to consider each constraint for only the subset of study areas that are relevant to that constraint.

It is worth to emphasize that any values speci<sup>fi</sup>ed during the application of the model for the above three cases should not contradict with the original constraints of the model. In other words, a check should be made before running the optimization package in order to ensure that the sum of elective courses (or elective hours) speci<sup>fi</sup>ed in cases (a) and (b) does not exceed the total number of elective credit hours a student is required to finish

## References

[1] NACADA, National Academic Advising Association. Available: http://www.nacada ksu.edu/April 2014.

[2] R.J. Light, Making the Most of College: Students Speak Their Minds, Harvard University Press, Cambridge, MA, 2004.

[3] J. Cuseo, Academic Advisement and Student Retention: Empirical Connections and Systemic Interventions, National Academic Advising Association, 2003. (linked from http://www.nacada.ksu.edu/Resources/Clearinghouse/View-Articles/Retention-andattrition-resources.aspx, retrieved April 2014).

[4] D.S. Fike, R. Fike, Predictors of <sup>fi</sup>rst-year student retention in the community college, Community College Review 36 (2) (2008) 68–88.

[5] W.R. Habley, The Status of Academic Advising: Findings from the Act Sixth National Survey (Monograph No. 10), National Academic Advising Association, Manhattan, KS, 2004.

[6] C.L. Nutt, Academic Advising and Student Retention and Persistence, National Association of Academic Advising, 2003. (linked from http://www.nacada.ksu.edu Resources/Clearinghouse/View-Articles/Advising-and-Student-Retention-article. aspx, retrieved April 2014).

[7] C.S. Wiseman, H. Messitt, Identifying components of a successful faculty-advisor program, NACADA Journal 30 (2) (2010) 35–52.

[8] A.D. Young-Jones, et al., Academic advising: does it really impact student success? Quality Assurance in Education 21 (1) (2013) 7–19.

[9] V.N. Gordon, W.R. Habley, T.J. Grites, Academic Advising: A Comprehensive Handbook, 2nd ed. Jossey-Bass, 2008.

[10] R.R. Hashemi, J. Blondin, SASSY: a Petri Net based student-driven advising support system, Presented at the Seventh International Conference on Information Technology, Las Vegas, Nevada, 2010.

[11] P.E. Beal, L. Noel, What Works in Student Retention, American College Testing Program, Iowa City, Iowa, 1980.

[12] G. Ruhe, A. Ngo-The, Hybrid intelligence in software release planning, International Journal of Hybrid Intelligent Systems 1 (2) (2004) 99–110.

[13] A. Mohamed, Interactive decision support for academic advising, Quality Assurance in Education, Emerald (submitted in, March 2013).

[14] A. Mohamed, IDS-CS: an interactive approach to support academic advising, International Conference on Multimedia and Human Computer Interaction (MHCI'13), Toronto, Canada, 2013, pp. 167–177.

[15] D. Yarbrough, The engagement model for effective academic advising with undergraduate college students and student organizations, Journal of Humanistic Counseling, Education and Development 41 (1) (2002) 61–68.

[16] T. Feghali, I. Zbib, S. Hallal, A web-based decision support tool for academic advising, Educational Technology & Society 14 (1) (2011) 82–94.

[17] M.J. Leonard, The next generation of computer: assisted advising and beyond, NACADA Journal 6 (1) (1996) 47–50.

[18] F.H. Grupe, Student advisement: applying a web-based expert system to the selection of an academic major, College Student Journal 36 (4) (2002).

[19] M. Patankar, A rule‐based expert system approach to academic advising, Innovations in Education and Training International 35 (1) (1998) 49–58.

[20] D. Pokrajac, M. Rasamny, Interactive Virtual Expert System for Advising (InVEStA), 36th Annual Frontiers in Education Conference, California, 2006, pp. 18–23.

[21] M.S. Laghari, G.A. Khuwaja, Student advising and planning software, International Journal on New Trends in Education & their Implications (IJONTE) 3 (3) (July 2012) 158–175.

[22] V. Gonzalez, D. Esparza, Work in progress: advising tool to improve the time for graduation and the transfer of students from a community college to engineering school, Presented at the 40th IEEE Frontiers in Education Conference (FIE'10), Washington, D.C., 2010.

[23] G. Ruhe, M.O. Saliu, The art and science of software release planning, IEEE Software 22 (6) (Nov/Dec 2005) 47–53

[24] G. Ruhe, Software engineering decision support — a new paradigm for learning software organizations, Lecture Notes in Computer Science 2640 (Nov 2003) 104–113.

[25] G. Ruhe, Software engineering decision support — methodology and applications, in: Tonfoni, Jain (Eds.),Innovations in Decision Support Systems, vol. 3, 2003, pp. 143–174.

[26] R.V. Rao, Introduction to multiple attribute decision-making (MADM) methods, Decision Making in the Manufacturing Environment: Using Graph Theory and Fuzzy Multiple Attribute Decision Making Methods, Springer, London, 2007, pp. 27–41.

[27] L.A. Wolsey, G.L. Nemhauser, Integer and Combinatorial Optimization, John Wiley, New York, 1998.

[28] F.S. Hillier, G.J. Lieberman, Introduction to Operations Research, Tata McGraw-Hill Education, 2001.

[29] LINDO, Systems. Available: http://www.lindo.com April 2014.

[30] M.L. Cheong, R. Bhatnagar, S.C. Graves, Logistics network design with supplier consolidation hubs and multiple shipment options, Journal of Industrial and Management Optimization 3 (1) (2007) 51.

[31] V. Jayaraman, A. Ross, A simulated annealing methodology to distribution network design and management, European Journal of Operational Research 144 (3) (2003) 629–645.

[32] A. Ngo-The, G. Ruhe, A systematic approach for solving the wicked problem of software release planning, Soft Computing: A Fusion of Foundations, Methodologies and Applications 12 (1) (Aug 2007) 95–108.

[33] A. Mohamed, G. Ruhe, A. Eberlein, MiHOS: an approach to support handling the mismatches between system requirements and cots products, International Journal of Requirements Engineering, Springer London 12 (3) (2007) 127–143.

Abdallah Mohamed received his Ph.D. degree in Software Engineering from the University of Calgary, Canada, in 2007, and his B.Sc. and M.Sc. degrees in Electrical and Computer Engineering from Zagazig University, Egypt, in 1998 and 2002, respectively. His research focuses on decision support systems, especially in the areas of software engineering, energy management, and academic advising. Contact him at abdallah.mohamed@ubc.ca.
