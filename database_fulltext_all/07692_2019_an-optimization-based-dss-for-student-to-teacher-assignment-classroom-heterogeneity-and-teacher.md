---
otero_id: 7692
otero_key: "MYVGF8UV"
title: "An optimization-based DSS for student-to-teacher assignment: Classroom heterogeneity and teacher performance measures"
authors: "Matthew D. Bailey; David Michaels"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.02.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An optimization-based DSS for student-to-teacher assignment: Classroom heterogeneity and teacher performance measures

![](/api/attachments/MYVGF8UV/fulltext/images/307c97b4f769302c79ab6aea81740f8b97d9053203924c001c6252c9ccd4a771.jpg)

Matthew D. Bailey<sup>a,\*</sup>, David Michaels<sup>b</sup>

<sup>a</sup> Bucknell University, Lewisburg, PA 17837, United States of America

<sup>b</sup> Williamsport Area School District, Williamsport, PA, United States of America

## A R T I C L E I N F O

Keywords: Decision support systems Education Assignment problems Optimization Optimization Spreadsheets Open source

## A B S T R A C T

A significant amount of administrator's summer planning is spent attempting to assign hundreds of students to teachers. These assignments must satisfy federal guidelines, parent preferences, and principal preferences while pursuing classroom parity and equity in regards to academic performance, behavioral support, and demo graphics. In addition, teachers are often the most invested in these decisions given the impact on their day-to-day life and their future performance evaluations. This problem is a variant of a standard problem in operations research; however, administrators often lack the technical expertise or budgets to build and/or implement such models. We present an open-source spreadsheet model-based DSS to this purpose. We formulate the problem as a mixed integer program, present the implemented spreadsheet model interface, and illustrate on a set of student data. This DSS was implemented in the fall of 2018 for the assignment of close to 600 students to 24 classrooms saving dozens of staf and administration hours.

With minor adaptions and/or redefinitions, the DSS would provide similar value to many of the roughly 64,000 public primary and middle school principals across the country. Even more generally, the model as presented is a framework for developing and implementing an optimization-based DSS for assistance in creating project teams under a variety of potential preferences and constraints on team composition.

## 1. Introduction

Each summer the nearly 64,000 United States primary and middle public school principals [14] are each tasked with determining teacher assignments for hundreds of students. This process is repeated for as many as eight grades within the school and with practitioner articles titled, “Making Class Lists Needn’t Be A Nightmare” [16], this task is clearly neither an easy nor enjoyable annual ritual.

Annual class assignments are determined based on the demands and input from a myriad of stakeholders: administrators, teachers, parents, students, and federal requirements. Typically, these assignments take a satisficing approach requiring many attempts over many hours (and days) to arrive at a feasible solution acceptable to all stakeholders. In this paper, we present and justify several of the typical decision constraints and criteria in an attempt to streamline the process and account for the bias (real or perceived) as a result of the assignment process. More generally, the optimization-based method we present can be used a framework for creating teams or groups satisfying equity preferences and other requirements (e.g., team projects, consulting project teams, etc.).

Student-to-teacher assignments are typically made with a goal of creating diverse classrooms both in demographics and learning abilities while also satisfying federal requirements for students' individualized educational plans and parent preferences. Additionally, the advent of test-based performance metrics for teachers creates additional human resource and morale problems for administrators. Ideally the assignments will be perceived, as much as possible, as reducing the bias in teachers' subsequent student-performance based evaluations.

Finally, for any model to be efective, it is necessary to understand both the problem and the context in which it will be implemented. In the United States, public elementary school administrators typically lack the technical expertise and budgets to develop and implement optimization models using commercial software tools. As a result, our secondary goal was to develop a student-to-teacher decision support tool in an environment familiar to our end user, namely Microsoft Excel.

In this paper we present a mixed integer programming optimization model (MIP) addressing the issues of stakeholders implemented in a spreadsheet and solved using an open-source solver. In what follows, we review the literature related to student-to-teacher assignments, present our model and its implementation, and finish with a computational illustration and broader relevance.

## 2. Literature review

While developing decision support systems for timetabling in education (assigning instructors to courses and time slots) has received previous attention [12,25] along with a broader body of work on applying operations research to issues in education administration [18], the complex task of assigning students to teachers to create balanced classrooms across multiple objectives is often overlooked.

Assigning students to teachers can be seen as a special case of the set partitioning problem with maximal within group diversity. As an application of this problem, Baker and Powell [4] provide a comparative study of objectives for assigning students to groups resulting in a variety of nonlinear optimization problems. In similar work, Cutshall et al. [8] provide an integer programming formulation for designing groups for MBA case projects under a variety of equity constraints which restrict the number of students with certain traits (gender, major, etc.) to be near the class frequency (within a given tolerance).

Two publications directly address the problem of optimally as signing students to teachers. Krauss et al. [20], using constraint types similar to Cutshall et al., pursue an assignment constraining the maximum class size and seeking equitable gender ratios while accounting for student preferences for friends, teacher preferences for some students to be separated, parent “friend requests”, and limits on “energetic” students per class. Only the assignment feasibility constraints and gender ratio (each student and teacher is assigned to one class and one class only) are treated as true constraints. The others are provided points for violations and used within the fitness function of a genetic program. They implement their model using a commercial genetic algorithm add-in for Microsoft Excel and provide an example on a grade of 100 students assigned to four teachers (one teacher per class). The current best solution is accepted after a 30 minute search.

Gill [13] also adapts the Cutshall et al. model constraints for assigning students to teachers in a small elementary school in the United Kingdom. Using a broader model than Krauss et al., Gill's model's primary objective is to determine assignments that maximize the number of friends in a class for each student. This (nonlinear) objective is subject to constraints to achieve an equitable distribution (within stated tolerances) within each class of particular student traits: gender, ability, English as a second language (ESL), behavioral issues, and learning support needs. The resulting model is a binary quadratic program which is then reformulated as a mixed-integer linear program (MIP). He solves the MIP using an optimization package for the open source software R and provides a small computational illustration on a grade with 59 students and two teachers. An optimal solution is found within minutes.

Although these two papers and ours deal with creating an equitable distribution of students to teachers, as noted in education research [5], the goal is not just to improve equitable distribution. The real goals of the student-to-teacher assignments are to improve student learning, close achievement gaps, and create educational opportunities for all young people. The equitable distribution of students to teachers is intended to be a means to that end.

Additionally, based on previous research in education, segregating students according to any characteristic (gender, race, education, etc.) increases the perception of more significant diferences between the groups [6,17]. In particular, racial balance within classes has a positive efect on students' and teachers' interracial attitudes [19,32]. As a result, class design typically seeks greater diversity or, as closely as possible, mirrors the overall diversity within the grade.

However laudable the goals of within-class student diversity, they may have an unintended impact upon teacher performance metrics. As shown by Dieterle et al. [10], nonrandom assignment of students to teachers has been shown to bias student test-based value-addedmeasures (VAMs) (a measure of performance improvement versus pure outcome-based proficiency measures). The previously discussed models of Krauss et al. and Gill both ignore the potential of the student assignment to bias a teacher's later performance evaluation. As a result, this bias, whether real or perceived, will have an impact upon teacher satisfaction and morale. Below we discuss these performance measures and how to incorporate them within our model.

Additionally, federal guidelines require that special education students and gifted students are assigned to teachers with the training and additional resources for those students.

We note that Gill's model's objective of maximizing the number of friends in a class may be preferred in that setting, but within United States public schools this is rarely, if ever, a primary decision criteria. In practice, administrator's (or administrators') placement preference encompassing many tangible and intangible factors is the final word on student placement. As a result, we focus on satisfying the adminis trator's preferences to quickly obtain a quality equitable assignment satisfying the federal restrictions and the administrator's restrictions. In contrast to the papers above, our DSS implementation is both open source and in the familiar spreadsheet environment [31] for the end user. This allows the end-user to independently employ the decision support system to develop alternative solutions. Additionally and importantly, in practice we are able to quickly determine exceedingly balanced assignments for problems of a much larger scale in seconds.

## 3. Value added measures (VAMs) of teaching performance

In past initiatives, many schools were deemed deficient because their students could not meet the proficiency targets despite their measured growth or improvement being greater than students in highincome neighborhoods. In response to this and initiatives such as the 2010 Race to the Top [28], schools began comprehensive data-collection and introduced “value-added measures”(VAMs) to identify schools (and teachers) added value to student performance relative to their past performances [22]. Currently, at least 44 states in the United States (and Washington D.C.) have adopted VAMs to evaluate teachers [7]. VAMs may be interpreted as the average amount of achievement growth an individual teacher contributes to his or her students [15]. While based on sound statistical measures, there is still significant debate on the value and validity of these measures for teacher performance. VAM-estimates of teacher performance have been shown to be biased in more homogeneous sets of classrooms [27].

As cited by the American Statistical Association in 2014 [3], only 1–3% of the variance in standardized test scores can be explained by the teacher. Although the actual impact may be limited, the consequences on teacher evaluations can be significant. As a result, a system which provides a nonrandom assignment of students to teachers must also account for any real or perceived notions of classroom inequity for teachers. At the same time, these assignments must consider what is best for the students including within class gender, race, and ability diversity. The resulting decision making process in the presence of numerous constraints and limited resources provides a valuable opportunity for optimization. To better understand how to implement VAMs into the assignment process, it is worthwhile to have a basic understanding of these metrics. We briefly discuss a particular VAM from the commercial vendor SAS.

The SAS Education Value-Added Assessment System (EVAAS) [30] is a VAM service utilized by many school districts and states. It has been in use in the authors' state, Pennsylvania, since 2006 [29]. This service provides a descriptive evaluation of each teacher, school, and district performance based on improvement of student standardized test scores. In addition, the analysis of covariance (ANCOVA) model can be used to predict a student's future test scores and the likelihood of achieving a benchmark of interest. These two predictions are based on a student encountering an “average schooling experience.” As a result, if we combine these predictions with past test performance, these values can be used as a base line for the student's potential growth and exam performance in any classroom.

In the EVAAS VAM, using the univariate response model as an example, the response variable $y _ { s }$ is the projected score for student s on an exam of interest, the predictor variables $( y _ { s , 1 } , y _ { s , 2 } , \ldots )$ are the student's scores on previous tests. The $\mu \mathrm { { s } }$ are the means of the respective variables.

$$
y _ {s} = \mu_ {y} + \beta_ {1} (y _ {s, 1} - \mu_ {1}) + \beta_ {1} (y _ {s, 2} - \mu_ {2}) + \ldots + \epsilon_ {s}\tag{1}
$$

Estimates for the terms are fitted from past test data for all students. Other model variants also include fixed efects based $_ { 0 \mathrm { { n } } , }$ for example, the student's demography. The model can be used to predict a student's score on a future exam ( ) and determine $P ( \hat { y } _ { s } > b )$ , the probability that a student's score will be above a target b.

As stated above, the validity of VAMs as a teacher performance metric is a point of debate. Our inclusion of VAMs into the studentassignment process is not an endorsement of these services, but an acknowledgment that these measures have an impact on teacher and school assessment and therefore on teacher acceptance of potential assignments. Due to both teacher morale and expectations, it is naive to dismiss the impact of future VAMs on the student-to-teacher assignment process. Therefore, we explicitly incorporate these measures into our assignment model.

## 4. Student-to-teacher assignment model

We detail the core components of the required optimization model. In United States elementary and some middle-schools, students within the same grade are assigned to one of a finite set of classes. We assume there is no overlap between grades and teachers are previously assigned to a grade, so assigning a student to a class within a grade is equivalent to assigning a student to a teacher. As a result, a school administrator's student-assignment decision can be decomposed into a separate as signment problem for each grade.

We define $x _ { s t }$ to be 1 if student s is assigned to teacher t, where is the set of students to be assigned in a grade and is the set of teachers assigned to the grade. Ideally, $\frac { | S | } { | \mathcal { T } | }$ students are in each class for size equity. In our data, there are roughly 200 (lSl) students and seven to eight teachers per grade resulting in a target class size of roughly 25 students. Based on a 2012 survey [14], this is on par with national averages.

In the case of added teaching support or team teaching, we assume that these teacher teams are determined prior to student assignment. In these cases, assigning a “teacher” can equivalently be interpreted as assigning a teaching team. For ease of exposition, we will refer to all student assignments in regards to a single teacher.

## 4.1. Feasible assignments

Prior to assignment, students are evaluated and, according to fed eral guidelines, deemed to require an individualized educational pro gram (IEP) based on special educational (or emotional support) required. These students must be assigned to an IEP teacher. Similarly, students meeting performance metrics will be identified as requiring additional instruction according to a gifted individualized educational plan (GIEP). Students meeting the GIEP criteria must be assigned to a qualified GIEP teacher.

We define $S _ { \mathrm { I E P } } \subset S$ as the subset of students requiring special education IEP support and $S _ { \mathrm { G I E P } }$ as the subset of gifted IEP students. Similarly, $\mathcal { T } _ { \mathrm { I E P } } \subset \mathcal { T }$ is the set of teachers designated to teach IEP classes and $\mathcal { T } _ { \mathrm { G I E P } }$ is the set of teachers designated to teach GIEP level classes. In practice these designations are also based on teacher preferences and/ or rotations. Also, as in practice, we assume that the assignment of teachers to class type precedes and is independent of the student-assignment decision.

With these definitions and federal requirements, we can formulate a set of constraints for feasibility of a student-to-teacher assignment. Namely, each student must be assigned to one and only one teacher, each IEP student must be assigned to an IEP teacher, and the same condition holds for GIEP. These are implemented using constraints (2), (3), and (4), respectively.

$$
\sum_ {t \in \mathcal {T}} x _ {s t} = 1 \quad \mathrm{for} \quad s \in \mathcal {S},\tag{2}
$$

$$
\sum_ {t \in \mathcal {T} _ {\mathrm{IEP}}} x _ {s t} = 1 \quad \mathrm{for} \quad s \in \mathcal {S} _ {\mathrm{IEP}},\tag{3}
$$

$$
\sum_ {t \in \mathcal {T} _ {\mathrm{GIEP}}} x _ {s t} = 1 \quad \text {for} \quad s \in \mathcal {S} _ {\mathrm{GIEP}}.\tag{4}
$$

Although the above constraints provide a feasible assignment according the state and federal guidelines, the most important preference is that of the principal. Based on their knowledge of their teachers' and students' strengths and weaknesses, the principal needs to have the ability to force (or restrict) particular pairings based on a variety of intangible factors (e.g., parent preferences). As a result, we define the indicator $p _ { s t } = 1$ if the principal would prefer that student s is paired with teacher t and zero otherwise. Similarly, we define $r _ { s t } = 1$ if the principal would like to restrict such a pairing and zero otherwise.

The principal is not explicitly making an assignment for a student and may prefer (or restrict) more than one teacher for a student. To satisfy these preferences we add the following constraints to the model,

$$
\begin{array}{l l} \sum_ {t \in \mathcal {T}} p _ {s t} x _ {s t} = 1 & \text { for } \quad s \in \mathcal {S} \quad \text { if } \quad p _ {s t} = 1 \quad \text { for   some } \quad t \in \mathcal {T}, \\ \sum_ {t \in \mathcal {T}} r _ {s t} x _ {s t} = 0 & \text { for } \quad s \in \mathcal {S} \quad \text { if } \quad r _ {s t} = 1 \quad \text { for   some } \quad t \in \mathcal {T}. \end{array}\tag{5}
$$

(6)

This mechanism also allows the principal the flexibility to pair small groups of students together with a particular teacher. The combination of these five sets of constraints, assures that a feasible student-to-teacher assignment will be created according the federal and principal placement preferences.

In addition to these obligations (or “hard constraints”), as previously discussed, administrators have further preferences (or “soft constraints”) regarding classroom assignment goals and metrics. In presenting these specific examples, we provide a framework for handling these and other general characteristic within the construction of classrooms, groups, or project teams.

## 4.2. Equity and heterogeneity preferences

The most basic preference is to create classes of similar size. To thi end, we set a target size of an equal proportion of the grade in each class, defined as $\begin{array} { r } { \tau _ { \mathrm { s i z e } } = \frac { | S | } { | \mathcal { T } | } } \end{array}$ . We aim to minimize the proportional absolute size deviation from the target $\tau _ { \mathrm { s i z e } }$ for teacher t’s classroom, defined as

$$
\delta_ {\mathrm{size,t}} = \frac {| \sum_ {s \in \mathcal {S}} x _ {s t} - \tau_ {\mathrm{size}} |}{\tau_ {\mathrm{size}}} \quad \mathrm{for} \quad t \in \mathcal {T}.\tag{7}
$$

Ideally, but often not possible, all these deviations will be zero.

By minimizing $\begin{array} { r } { \sum _ { t \in \mathcal { T } } \delta _ { \mathrm { s i z e } , 1 } } \end{array}$ in the objective function, we can achieve the principal's preferred placements and the federal requirements while creating similarly-sized classrooms. However, the discontinuity and nonlinearity from the absolute value in constraint (7) is computationally problematic. As a result, we use the common technique to linearize the constraint by splitting the absolute value into the positive and negative deviation. We then treat the upper bound as a decision variable, $\delta _ { \mathrm { s i z e } , t s }$ on this pair of constraints to attain the same value as Eq. (7).

$$
\delta_ {\mathrm{size}, t} \geq \frac {\sum_ {s \in \mathcal {S}} x _ {s t} - \tau_ {\mathrm{size}}}{\tau_ {\mathrm{size}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{8}
$$

$$
\delta_ {\mathrm{size}, t} \geq \frac {\tau_ {\mathrm{size}} - \sum_ {s \in \mathcal {S}} x _ {s t}}{\tau_ {\mathrm{size}}} \quad \mathrm{for} \quad t \in \mathcal {T}.\tag{9}
$$

We adopt a similar approach and definitions across several metrics which we detail next. In more general settings the pursuit of equity over any metric need not be the target, i.e., the target can be uniquely defined as the problem context warrants for each class or group.

In addition to the assignment feasibility constraints there are administrator and education research-supported preferences for diversity and heterogeneity within classrooms. Some schools chose ability tracking (i.e., grouping students into classes by ability) of some type (beyond IEP/GIEP federal requirements), thus creating more homogeneous classrooms. We focus on the preference and practice of our local school districts - namely heterogeneity. For a general review of conditions impacting whether administrators select heterogeneous classrooms see Nesmith [26].

Similar to Cutshall et al., we use the proportion of occurrences within a class as compared to the proportion within the grade to measure class equity under various metrics. For example, if boys comprise 50% of the grade, then a preferred assignment would have 50% of each teacher's class comprised of boys. To avoid the nonlinearities that result from minimizing a class average from a target, we approximate target proportion by seeking an assignment resulting in an equal number of boys in each class. As a result of our simultaneous objective for class size equity, this will result in closely proportional equity according to this measure in each class.

We define ℬ as the set of boys in the grade. Additionally, we define $\begin{array} { r } { \tau _ { \mathrm { b o y s } } = \frac { | \mathcal { B } | } { | \mathcal { T } | } } \end{array}$ as the target number of boys in each class grade based on their representation in the entire class. As we saw for classroom size, we seek to measure and minimize the proportional (absolute) deviation from this target per class. The number of boys in any class $t \in \mathcal { T }$ can be found from $\textstyle \sum _ { s \in { \mathcal { B } } } x _ { s t } .$ To pursue this target in each class, we add the linearized constraints,

$$
\delta_ {\mathrm{boys}, t} \geq \frac {\sum_ {s \in \mathcal {B}} x _ {s t} - \tau_ {\mathrm{boys}}}{\tau_ {\mathrm{boys}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{10}
$$

$$
\delta_ {\mathrm{boys}, t} \geq \frac {\tau_ {\mathrm{boys}} - \sum_ {s \in \mathcal {B}} x _ {s t}}{\tau_ {\mathrm{boys}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{11}
$$

with the decision variables $\delta _ { \mathrm { b o y s } , t } .$ These constraints in combination with $\begin{array} { r } { \sum _ { t \in \mathcal { T } } \delta _ { \mathrm { b o y s } , t } } \end{array}$ in the objective function will drive the count of boys in each class toward our target. The structure of the above constraint is appropriate for achieving equity in any binary categorical trait for students or potential class or group members: race, gender, skills, etc.

Similarly, for class diversity, we define as the set of students of an underrepresented race in the grade. We leave the exact definition of “underrepresented” to the administration. Given this student categorization, we define $\begin{array} { r } { \tau _ { \mathrm { r a c e } } = \frac { | \mathcal { R } | } { | \mathcal { T } | } } \end{array}$ as the target number of underrepresented students in each class based upon the proportion in the overall grade. This results in the following deviation metrics per class with $\delta _ { \mathrm { r a c e } , t }$ defined as before for the other metrics,

$$
\delta_ {\mathrm{race}, t} \geq \frac {\sum_ {s \in \mathcal {R}} x _ {s t} - \tau_ {\mathrm{race}}}{\tau_ {\mathrm{race}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{12}
$$

$$
\delta_ {\mathrm{race}, t} \geq \frac {\tau_ {\mathrm{race}} - \sum_ {s \in \mathcal {R}} x _ {s t}}{\tau_ {\mathrm{race}}} \quad \mathrm{for} \quad t \in \mathcal {T}.\tag{13}
$$

As discussed above, students are classified into one of two educational support levels: IEP or GIEP. In the application we model, teachers are either qualified for IEP or for GIEP, so the students in these two levels will not be assigned to the same teachers. In spite of this and to achieve some educational diversity and parity within each class, the administration prefers to balance the workload. As a result, teachers teaching IEP students should be assigned a disproportionately higher number of non-IEP students requiring less educational support. To achieve this, we define $e _ { s } ,$ the educational support classification for student s. The administrators use a ranking of 1, 2, 3, or 4 based upon administrator and teacher judgment in addition to past student performance. A ranking of 1 signifies the highest level of educational support need (IEP students are a subset of these students). One measure of educational support parity is whether the sum of student educational support levels in each classroom is equal or near $\frac { \sum _ { s \in S } e _ { s } } { | \mathcal { T } | }$ , we define this as $\tau _ { \mathrm { e d } } .$ . Using this as a target results in the following constraints for educational support parity per teacher,

$$
\delta_ {\mathrm{ed}, t} \geq \frac {\sum_ {s \in \mathcal {S}} e _ {s} x _ {s t} - \tau_ {\mathrm{ed}}}{\tau_ {\mathrm{ed}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{14}
$$

$$
\delta_ {\mathrm{ed}, t} \geq \frac {\tau_ {\mathrm{ed}} - \sum_ {s \in S} e _ {s} x _ {s t}}{\tau_ {\mathrm{ed}}} \quad \text { for } \quad t \in \mathcal {T},\tag{15}
$$

The $\delta _ { \mathrm { e d } , t }$ are the decision variables to be minimized to attain an assignment minimizing the above proportional absolute deviation.

We prefer this measure over other measures such as “average student educational support” per class due to the support levels being ordinal and the fact that class sizes may difer. By using the cumulative education support in the class, $\textstyle \sum _ { s \in S } e _ { s } x _ { s t } ,$ and seeking some form of equity among the teacher assignments if an IEP class is larger, it will typically be compensated with more higher achieving students (level 3). We do note that if all classes are of the same size, a concurrent goal, this is equivalent to seeking average educational support parity among the teacher assignments.

The structure of the constraint pair (14) and (15) is an appropriate framework for achieving equity in any non-binary trait for students or group members, such as age or years of experience, in more general settings.

Using similar modeling approaches, we could also incorporate equity of other demographic or student characteristics into the studentto-teacher assignment problem, including the proportion of students with English as a second language or the proportion of students on subsidized meal plans. Due to the small proportion of the first and the overwhelming proportion of the second at this particular school, it was deemed unnecessary to account for these particular measures.

We can also directly account for classroom dificulties due to assigning teachers a disproportionate number of challenging students by attempting to distribute these students across the classes. A common measure of this is the number of ODRs (ofice discipline referrals) a student has collected in the previous years. This data is combined with administrator and teacher judgment to classify the student as 1, 2, 3, or $^ { 4 , }$ where a 1 is the most challenging students. We define $d _ { s } ,$ the disciplinary classification for student s, $\begin{array} { r } { \tau _ { \mathrm { d i s c } } = \frac { \sum _ { s \in S } d _ { s } } { | \mathcal { T } | } } \end{array}$ and $\delta _ { \mathrm { d i s c } , t }$ as the decision variable to minimize, resulting in the following constraints for disciplinary support parity,

$$
\delta_ {\mathrm{disc}, t} \geq \frac {\sum_ {s \in \mathcal {S}} d _ {s} x _ {s t} - \tau_ {\mathrm{disc}}}{\tau_ {\mathrm{disc}}} \quad \text {for} \quad t \in \mathcal {T},\tag{16}
$$

$$
\delta_ {\mathrm{disc}, t} \geq \frac {\tau_ {\mathrm{disc}} - \sum_ {s \in \mathcal {S}} d _ {s} x _ {s t}}{\tau_ {\mathrm{disc}}} \quad \mathrm{for} \quad t \in \mathcal {T}.\tag{17}
$$

Finally, based on administrator feedback from the output of previous models, it was communicated that it was necessary to incorporate an additional disciplinary metric. Even with disciplinary balance at the classroom level, some classes were assigned a greater number of particularly challenging students. By the central measure, they were ofset by less challenging students, but as an example of the flaw (or limits) of averages, we sought to additionally balance the absolute number of these types of students in each class. In the current process, the principal would identify these students with histories of being disruptive and distribute them evenly among the classrooms. We define $\mathcal { P }$ as this subset of students (a subset of the students with disciplinary classification of 1 in the above measure). With a target of $\begin{array} { r } { \tau _ { \mathrm { p r o b } } = \frac { | \mathcal { P } | } { | \mathcal { T } | } } \end{array}$ we have the constraints,

$$
\delta_ {\mathrm{prob}, t} \geq \frac {\sum_ {s \in \mathcal {P}} x _ {s t} - \tau_ {\mathrm{prob}}}{\tau_ {\mathrm{prob}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{18}
$$

$$
\delta_ {\mathrm{prob}, t} \geq \frac {\tau_ {\mathrm{prob}} - \sum_ {s \in \mathcal {P}} x _ {s t}}{\tau_ {\mathrm{prob}}} \quad \mathrm{for} \quad t \in \mathcal {T}.\tag{19}
$$

where $\delta _ { \mathrm { p r o b } , t }$ defined as a decision variable to minimize.

In addition to restricting IEP and GIEP students to teachers with the appropriate training, we would also like to distribute these students as evenly as possible among these class types. To that end we define targets $\begin{array} { r } { \tau _ { \mathrm { I E P } } = \frac { | S _ { \mathrm { I E P } } | } { | \mathcal { T } _ { \mathrm { I E P } } | } } \end{array}$ and $\begin{array} { r } { \tau _ { \tt G I E P } = \frac { | S _ { \tt G I E P } | } { | \mathcal { T } _ { \tt G I E P } | } } \end{array}$ . Then the number of IEP or GIEP students in a class is $\textstyle \sum _ { s \in S _ { \mathrm { I E P } } } x _ { s t }$ and $\textstyle \sum _ { s \in S _ { \mathrm { G I E P } } } x _ { s t }$ . The corresponding constraints are,

$$
\delta_ {\mathrm{IEP}, t} \geq \frac {\sum_ {s \in S _ {\mathrm{IEP}}} x _ {s t} - \tau_ {\mathrm{IEP}}}{\tau_ {\mathrm{IEP}}} \quad \mathrm{for} \quad t \in \mathcal {T} _ {\mathrm{IEP}},\tag{20}
$$

$$
\delta_ {\mathrm{IEP}, t} \geq \frac {\tau_ {\mathrm{IEP}} - \sum_ {s \in \mathcal {S} _ {\mathrm{IEP}}} x _ {s t}}{\tau_ {\mathrm{IEP}}} \quad \mathrm{for} \quad t \in \mathcal {T} _ {\mathrm{IEP}},\tag{21}
$$

$$
\delta_ {\mathrm{GIEP}, t} \geq \frac {\sum_ {s \in \mathcal {S} _ {\mathrm{GIEP}}} x _ {s t} - \tau_ {\mathrm{GIEP}}}{\tau_ {\mathrm{GIEP}}} \quad \text { for } \quad t \in \mathcal {T} _ {\mathrm{GIEP}}, \quad \text { and }\tag{22}
$$

$$
\delta_ {\mathrm{GIEP}, t} \geq \frac {\tau_ {\mathrm{GIEP}} - \sum_ {s \in \mathcal {S} _ {\mathrm{GIEP}}} x _ {s t}}{\tau_ {\mathrm{GIEP}}} \quad \mathrm{for} \quad t \in \mathcal {T} _ {\mathrm{GIEP}},\tag{23}
$$

where the deviation bound decision variables are defined as before.

While the above categorical metrics attempt to balance the student workload and demographics per teacher, they do not explicitly address the student performance metrics used to also assess teacher perfor mance.

## 4.3. Teacher assessment parity preference

As previously discussed, with student standardized test performance (or improvement) as the basis of teacher performance, teachers may be wary of how the students assigned to their class may impact their subsequent performance evaluation. In an attempt to mitigate these efects and concerns, we directly incorporate these measures as part of the student-to-teacher assignment process. It is likely that some of this parity is already accounted for within our previous equity measures due to correlations with standardized test performance (educational sup port, disciplinary referrals, etc.); however, our approach makes this explicit and transparent to teachers (and administrators).

The two major measures of academic success are proficiency on standardized tests and VAMs. We will provide model additions to ac count for each or both in experimental trials. While it may seem redundant, proficiency (or achievement) standards are a measure of a student's performance at a point in time and have been shown to be correlated with a student's demographics. On the other hand, VAMs measure growth over time relative to the student's own performance and show little correlation with student demographics. Additionally, there is often little correlation between the two (see Fig. 1 from [29]) and by state standards, schools measure both.

If the preference is for classrooms with expected VAMs (growth) parity we can account for student's previous VAM score in assigning students to teachers mirroring our previous approach for the other metrics. We define $\nu _ { s }$ as the previously reported VAM for student s. For better predictive purposes, a moving average of the last three years' reported VAMs could be used or approximated by the geometric mean of the percentage growth based upon past test results. For simplicity, we seek to achieve a target in each class, so that the cumulative student VAM scores are roughly equivalent. Due to our previous size parity metric, this will achieve a rough equality of the class average VAM score. As with our other metrics, our target is $\begin{array} { r } { \tau _ { \mathrm { { v a m } } } = \frac { \sum _ { s \in S } v _ { s } } { | \mathcal { T } | } } \end{array}$ , resulting in following constraints for VAM parity,

$$
\delta_ {\mathrm{vam}, t} \geq \frac {\sum_ {s \in \mathcal {S}} v _ {s} x _ {s t} - \tau_ {\mathrm{vam}}}{\tau_ {\mathrm{vam}}} \quad \mathrm{for} \quad t \in \mathcal {T},\tag{24}
$$

$$
\delta_ {\mathrm{vam}, t} \geq \frac {\tau_ {\mathrm{vam}} - \sum_ {s \in \mathcal {S}} v _ {s} x _ {s t}}{\tau_ {\mathrm{vam}}} \quad \mathrm{for} \quad t \in \mathcal {T}.\tag{25}
$$

Alternatively, if teacher assessment is based upon proficiency metrics, such as the proportion of students meeting minimum standards, we can utilize the predicted test result provided by the VAM provider. Let, $\hat { y } _ { s }$ be the predicted result for student s as provided by the VAM system provider. is the predicted test result for the next annual test assuming an “average education experience.” Additionally, as previously explained, VAM vendors will also report $P ( \hat { y } _ { s } \ge z )$ , the probability that a student's score on a future test will meet a target value z. We define this probability as $\ell _ { s }$ and $\begin{array} { r } { \tau _ { \mathrm { p r o f } } = \frac { \sum _ { s \in S } \ell _ { s } } { | \mathcal { T } | } } \end{array}$ as the expected number of students meeting the exam standard per class. This results in the following class proficiency parity constraints,

$$
\delta_ {\mathrm{prof}, t} \geq \frac {\sum_ {s \in S} \ell_ {s} x _ {s t} - \tau_ {\mathrm{prof}}}{\tau_ {\mathrm{prof}}} \quad \text { for } \quad t \in \mathcal {T},\tag{26}
$$

$$
\delta_ {\mathrm{prof}, t} \geq \frac {\tau_ {\mathrm{prof}} - \sum_ {s \in \mathcal {S}} \ell_ {s} x _ {s t}}{\tau_ {\mathrm{prof}}} \quad \text {for} \quad t \in \mathcal {T}.\tag{27}
$$

Due to the already complex nature of the student-to-teacher assignment process, administrators would not take such metrics into account despite its potential impact on subsequent teacher evaluations. We explore those diferences in our computational illustration. In practice students are assessed on their proficiency in mathematics and English. The above modeling process can be repeated for any additional tests of interest.

## 4.4. Model objective

With the above constraints and definitions, we can define our objective function to minimize our total classroom deviations from the target metrics. Ideally, this objective function would be zero at optimality, meaning that all class metrics exactly match their target metrics. In practice, this is both unnecessary and impractical. It is unnecessary because although we are using optimization as a framework, the end user does not require optimal solutions and is only seeking the eficient creation of very good feasible solutions. An objective function of zero is impractical because exact parity is often not possible due to the hard constraints and indivisibility of some metrics. At its simplest, if there are an odd number of teachers with an even number of boys exact parity is impossible. While we do not require optimality, as will be seen, the ability to model the problem using linear optimization allows us to leverage the state of the art algorithms with open-source optimization engines to quickly determine excellent, if not optimal, student assignments.

Optionally administrators can define proportional weights for each of the deviations from the metric targets. Such weights allow an administrator to “tune” a solution by providing greater emphasis on some metrics (or classes) over others. In our application, the metrics and classes were equally valued and quality solutions across all metrics were determined using equal weights. For completeness, we still include this option to the user. We define these weights as ρ<sub>size,t</sub>, ρ<sub>boys,t</sub>, ρ<sub>race,t</sub>, ρ<sub>ed,t</sub>, ρ<sub>disc,t</sub>, ρ<sub>prob,t</sub>, ρ<sub>IEP,t</sub>, ρ<sub>GIEP,t</sub>, $\rho _ { \mathrm { v a m } , t s }$ , and $\boldsymbol { \rho } _ { \mathrm { p r o f } , t }$ . It is assumed (or forced) that

$$
\begin{array}{l} \sum_ {t \in \mathcal {T}} \rho_ {\text {size}} + \rho_ {\text {boys}} + \rho_ {\text {race}} + \rho_ {\text {ed}} + \rho_ {\text {disc}} + \rho_ {\text {prob}} + \rho_ {\text {IEP}} + \rho_ {\text {GIEP}} + \rho_ {\text {vam}} + \rho_ {\text {prof}} \\ = 1. \end{array} \tag {28}
$$

The resulting objective function is,

![](/api/attachments/MYVGF8UV/fulltext/images/4866720083a4b9fde69db147fc3fb7e0ba2dd427f69376a56fdb528e4855c350.jpg)  
Fig. 1. Achievement vs growth.

$$
\begin{array}{l} \min \\ \mathbf {x}, \delta \sum_ {t \in \mathcal {T}} [ \rho_ {\mathrm{size}, t} \delta_ {\mathrm{size}, t} + \rho_ {\mathrm{boys}, t} \delta_ {\mathrm{boys}, t} + \rho_ {\mathrm{race}, t} \delta_ {\mathrm{race}, t} + \rho_ {\mathrm{ed}, t} \delta_ {\mathrm{ed}, t} \\ + \rho_ {\mathrm{disc}, t} \delta_ {\mathrm{disc}, t} + \rho_ {\mathrm{size}, t} \delta_ {\mathrm{size}, t} + \rho_ {\mathrm{vam}, t} \delta_ {\mathrm{vam}, t} + \rho_ {\mathrm{prof}, t} \delta_ {\mathrm{prof}, t} ] \\ + \sum_ {i \in \mathcal {T} _ {\mathrm{IEP}}} \rho_ {\mathrm{IEP}, t} \delta_ {\mathrm{IEP}, i} + \sum_ {g \in \mathcal {T} _ {\mathrm{GIEP}}} \rho_ {\mathrm{GIEP}, t} \delta_ {\mathrm{GIEP}, g} \end{array}\tag{29}
$$

where x and δ represent the arrays of decision variables for student-to teacher assignment (x) and for the deviations from the targets (δ).

The complete optimization model formulation is provided in the appendix. This model formulation provides a general framework for the problem of team or group formulation under hard constraints and categorical and continuous target metrics for each team.

As a whole the optimization will determine student-to-teacher as signments (x) which satisfy the feasibility constraints above (including administrator placement preferences and restrictions) while seeking a feasible solution which minimizes the weighted absolute proportional deviations from the targets (δ). In practice. the user is rarely interested in optimality and is seeking to eficiently find a very good feasible so lution.

Due to how the model was formulated, the problem can be solved using standard solution algorithms for linear mixed integer optimization problems available with commercial and open source optimization software engines. These algorithms determine excellent feasible solutions very quickly. The determination of a verifiably optimal solution requires a longer run time, but the additional solution time quickly yields diminishing returns in solution improvement. Fortunately, the optimization algorithm may be terminated early at the user's discretion and will report the current best found feasible solution. In our example, excellent solutions (total deviation of 15% across all classrooms and metrics - an average deviation of 0.01% for each metric within each class.) are found in under 10 s and no solution improvement is observed after 10 min. We use 15 s as a default maximum search time. but allow the user to adjust this as needed.

## 5. Functionality and interface

It would be atypical for a school administrator to have the expertise to solve the above optimization problem. Even if they have the optimization modeling expertise, the problems we explore will have several hundred constraints and close to two thousand variables (most of which are integer) this is well beyond the model size limits of the free Excel standard Solver add-in (200 variables and 100 constraints, [2]), thus requiring more powerful (and expensive) optimization solvers. Such an expense is impractical given the limited need beyond this problem and restricted budgets of the school districts in question.

As a result, our focus was to develop a DSS for school administrators using an open-source optimization add-in and modeling tools embedded in software already in common use, namely Microsoft Excel. We developed a zero-cost DSS, using the open-source Excel add-in OpenSolver [1,24] and the included MIP solver CBC [11] (both available from the open-source optimization initiative COIN-OR [23]).

The school administrators (typically principals), first enter the names and characteristics for each teacher on a “Teacher Data worksheet” as shown in Fig. 2. The data from this worksheet is referenced for pull-down menu lists in the subsequent worksheet “Admin Student Data Entry” (Fig. 3) where the principal can enter the demographics and data for each student (up to 220 students) and the students metrics. The format of this sheet directly mirrors the data format currently in use, thus allowing the principals the option to copy-and-paste the information directly into this worksheet or link the data to another worksheet. For our implementation, the administration (and the performance evaluations) were heavily focused on the students' achievement and growth on the English Language Arts (ELA) exam. As a result, our model focused on balancing that particular VAM and proficiency measure within each class. From this data the targets for each metric are computed as described above for use within the optimization model.

On the same worksheet, the principal can select the teachers they prefer for particular students or teachers they would like to restrict from students from pull-down lists. Based on user discussions, this is limited to three of each type per student (Fig. 4).

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td></tr><tr><td>1</td><td>Teacher Name (&quot;NA&quot; if none)</td><td>Martin</td><td>Hoover</td><td>Vonderheid</td><td>Schumacher</td><td>Martine</td><td>Lane</td><td>Shinnerer</td><td>Stetzel</td></tr><tr><td>2</td><td>Class Type (&quot;NA&quot; if none)</td><td>IEP</td><td>IEP</td><td>IEP</td><td>IEP</td><td>IEP</td><td>IEP</td><td>GIEP</td><td>GIEP</td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 2. Teacher characteristics input sheet.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td colspan="2">Student</td><td></td><td colspan="8">Student Characteristics</td></tr><tr><td>3</td><td>LN</td><td>FN</td><td></td><td>Gender</td><td>Racial Diversity</td><td>Academic Performance (1=High,...,4 = Low)</td><td>Discipline Support (1 = High,...,4 = Low)</td><td>Historically Disruptive (1 = yes)</td><td>IEP/GIEP</td><td>VAM Prediction</td><td>Proficiency Likelihood</td></tr><tr><td>4</td><td>Andrade</td><td>Sariah</td><td></td><td>F</td><td>N</td><td>2</td><td>4</td><td>N</td><td></td><td>-1.86</td><td>99.7</td></tr><tr><td>5</td><td>Andrews</td><td>Peyton</td><td></td><td>M</td><td>Y</td><td>3</td><td>3</td><td>N</td><td></td><td>-9.41</td><td>13</td></tr><tr><td>6</td><td>Arnold</td><td>Tripp</td><td></td><td>M</td><td>Y</td><td>1</td><td>1</td><td>Y</td><td></td><td>-2.62</td><td>47</td></tr><tr><td>7</td><td>Atkins</td><td>Mayra</td><td></td><td>M</td><td>N</td><td>3</td><td>4</td><td>N</td><td></td><td>-2.62</td><td>98.9</td></tr></table>

Fig. 3. Student characteristics input sheet.

<table><tr><td></td><td>A</td><td>B</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td><td rowspan="3"></td><td></td><td></td><td></td></tr><tr><td>2</td><td colspan="2">Student</td><td colspan="3">Principal Preferred Pairings</td><td colspan="3">Principal Restricted Pairings</td></tr><tr><td>3</td><td>LN</td><td>FN</td><td>Pref 1</td><td>Pref 2</td><td>Pref 3</td><td>Restrict 1</td><td>Restrict 2</td><td>Restrict 3</td></tr><tr><td>4</td><td>Andrade</td><td>Sariah</td><td>Shinnerer</td><td></td><td>Hoover</td><td rowspan="4"></td><td>Schumacher</td><td></td><td></td></tr><tr><td>5</td><td>Andrews</td><td>Peyton</td><td></td><td></td><td></td><td>Schumacher</td><td></td><td></td></tr><tr><td>6</td><td>Arnold</td><td>Tripp</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Atkins</td><td>Mayra</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 4. Principal preferences and restrictions.

Once completed, the requisite teacher and student data entry i completed and the user can move to the final worksheet “Student to Class Assignments” (Fig. 5). On this worksheet, the user can optionally select which metrics they would prefer to include in the assignment decision and their associated weight in the objective function. The default is that all are selected and are equally weighted. The user is allowed to put any weight from 0 to 100, but they are subsequently scaled into proportions of the total weight assigned. The user is also permitted to reduce or extend the duration of the assignment search. The default is 15 s and, as discussed previously, has been suficient in finding a feasible and well-balanced assignment. Once satisfied with their options, the user can click the “Determine Student Assignments” button on this worksheet and a macro runs the OpenSolver optimization model for Max Search Time seconds and returns the summary statistic for each teacher's class and the names of each student assigned to their class as shown in Fig. 5.

## 6. Implementation and illustration

In the Fall of 2018, the DSS was utilized at Curtin Elementary School in the Williamsport Area School District in Pennsylvania to assign 600 students to 25 teachers in three grades. By federal law, the names shown are not real, but the demographics and student data are representative of students (samples of which are shown in Figs. 2 and 3). Our sample class is comprised of 191 students which must be assigned to one of eight teachers. Of these teachers, six are qualified to teach IEP students and the remainder are qualified to teach GIEP students, see Fig. 2. The summary statistics for the entire grade are shown in Table 1 along with the targets used for each metric in the optimization.

From Table 1 we see that our target class size is 23.9 students per class. Within each class, we aim for 13.8 boys and 12.5 students of an underrepresented (nationally) race. Within the six IEP courses and two GIEP courses, our goal is an assignment where there are 5 IEP students and 4.5 GIEP students in each of their respective classrooms. The targets for the total educational support and disciplinary support in each of the eight classrooms are 60.3 and 73.8. The grade average ratings of these two metrics per student are 2.5 and 3.1. Ideally, our assigned classes would have similar per student averages. Finally, the target total VAM and Proficiency Likelihood are −62.5 and 1135.1 (likelihood pe student is reported between zero and 100). The resulting per student averages for the grade are −2.6 and 47.5. This implies that an average student in this grade at this school (not actual student data) is expected to score 62.5 points lower on standardized tests (negative growth), but have a 47.5% chance of exceeding the test target and being proficient. It is expected that well-balanced classes will have similar per student metrics.

<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td></tr><tr><td>1</td><td rowspan="3" colspan="3">Determine Student Assignments</td><td colspan="5"></td></tr><tr><td>2</td><td colspan="5">Student Assignment</td></tr><tr><td>3</td><td>Martin</td><td>Hoover</td><td>Vonderheid</td><td>Schumacher</td><td>Martine</td></tr><tr><td>4</td><td>Metric Weight</td><td>Include Metric?</td><td>Class Type</td><td>IEP</td><td>IEP</td><td>IEP</td><td>IEP</td><td>IEP</td></tr><tr><td>5</td><td>10</td><td>☑</td><td>Class Size</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td></tr><tr><td>6</td><td>10</td><td>☑</td><td>Racial Diversity Rep Count</td><td>12</td><td>12</td><td>13</td><td>13</td><td>12</td></tr><tr><td>7</td><td>10</td><td>☑</td><td>Boys Count</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td></tr><tr><td>8</td><td>10</td><td>☑</td><td>Avg Academic Ability</td><td>2.5</td><td>2.6</td><td>2.5</td><td>2.5</td><td>2.5</td></tr><tr><td>9</td><td>10</td><td>☑</td><td>Avg Discipline Issues</td><td>3.1</td><td>3.2</td><td>3.1</td><td>3.1</td><td>3.0</td></tr><tr><td>10</td><td>10</td><td>☑</td><td>Difficult Students</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>11</td><td>10</td><td>☑</td><td>IEP Students</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>12</td><td>10</td><td>☑</td><td>GIEP Students</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>13</td><td>10</td><td>☑</td><td>Avg VAM Predicted</td><td>-2.5</td><td>-2.5</td><td>-2.9</td><td>-2.5</td><td>-2.5</td></tr><tr><td>14</td><td>10</td><td>☑</td><td>Avg Proficiency Likelihood</td><td>48.0</td><td>48.0</td><td>47.6</td><td>47.4</td><td>45.6</td></tr><tr><td></td><td rowspan="2" colspan="2">Max Search Time (seconds)</td><td rowspan="2">Student</td><td rowspan="2">Martin</td><td rowspan="2">Hoover</td><td rowspan="2">Vonderheid</td><td rowspan="2">Schumacher</td><td rowspan="2">Martine</td></tr><tr><td>15</td></tr><tr><td>16</td><td colspan="2">15</td><td>1</td><td>Prince Avila</td><td>Claudia Barton</td><td>Giovani Bolton</td><td>Peyton Andrews</td><td>Tripp Arnold</td></tr><tr><td>17</td><td colspan="2"></td><td>2</td><td>Dillon Black</td><td>Lennon Cline</td><td>Chance Burke</td><td>Mayra Atkins</td><td>Lorelai Berg</td></tr><tr><td>18</td><td colspan="2"></td><td>3</td><td>Branay Convantes</td><td>Presley Cooper</td><td>Elian Castaneda</td><td>Natalie Bowle</td><td>Megan Braun</td></tr></table>

Fig. 5. Screenshot of model interface and output.

Table 1  
Table 2  
Grade summary statistics and optimization targets.

<table><tr><td>Metric</td><td>Class size</td><td>boys</td><td>Racial Diversity</td><td>Educational support</td><td>Discipline support</td><td>Difficult students</td><td>IEP</td><td>GIEP</td><td>VAM</td><td>Proficiency likelihood</td></tr><tr><td>Totals</td><td>191</td><td>110</td><td>100</td><td>482</td><td>590</td><td>32</td><td>30</td><td>9</td><td>-500.2</td><td>9080.5</td></tr><tr><td>Grade proportion</td><td></td><td>0.58</td><td>0.52</td><td></td><td></td><td>0.17</td><td></td><td></td><td></td><td></td></tr><tr><td>Grade average per student</td><td></td><td></td><td></td><td>2.5</td><td>3.1</td><td></td><td></td><td></td><td>-2.6</td><td>47.5</td></tr><tr><td>Optimization metric target per class</td><td>23.9</td><td>13.8</td><td>12.5</td><td>60.3</td><td>73.8</td><td>4</td><td>5</td><td>4.5</td><td>-62.5</td><td>1135.1</td></tr></table>

The targets used for the optimization are not always the direct metrics reported as shown in the next two tables.

We first consider the decision process without the metrics in use when the DSS was available, but with the principal preferences as sampled in Fig. 4. Namely, we eliminate VAMs and achievement proficiency from the decision making process. The metrics are all given equal weight and we use the default solution search time of 15 s. The summary class metrics output are shown in Table 2.

Clearly when comparing these results to the target values and grade statistics in Table 1, the resulting students' assignments are well balanced for all the metrics included in this run of the model. As a result, even without the inclusion of the teacher incentive-based metrics. the DSS has great value in replacing a process that required days of work to achieve somewhat balanced classroom assignments to one with almost perfectly balanced assignments in seconds.

Despite the balance across the metrics, it is clear that the teachers classrooms are unbalanced with regard to VAM and Achievement Proficiency with some teachers (Shinnerer) expecting 85% of their class to be proficient before the semester even starts while another (Vonderheid) is faced with only 27.9% of their class forecasted to be proficient. Although an excellent teacher will improve all students, even with great strides in students' scores in Vonderheid's class. this teacher is at a great disadvantage before the semester even begins.

If we rerun this student-to-teacher assignment DSS including the objective values and constraints for the VAM and Achievement Proficiency metrics, the resulting metrics for the provided assignment are shown in Table 3.

As we see, the classroom equity and parity of the previous metrics is maintained, while providing a solution with equity for the VAM and Achievement Proficiency metrics. Such equity provides a powerful argument against teachers concerned about the inequity of student assignments and its impact upon their subsequent performance evaluations. This provides the administrator with a useful rebuttal for a process that may seem biased to external stakeholders. Administrators have found the combination of the time save savings and transparent equity to be incredibly motivating toward its expanded use.

## 6.1. School administrator extensions

During the initial use of the DSS and after the student assignment was considered final, we quickly discovered a limitation of the implementation due to the last-minute addition and/or subtraction of students from/to the grade. Due to the nature of optimization, if the DSS was rerun with these changes, it would still produce a well-balanced assignment, but it ofers no assurance that the new student assignments would be similar to the previous assignments. As a result, we added the functionality to report the last found assignment and allow the user to maintain that assignment in the subsequent solution for individual students or for an entire class. We accomplished this by adding the data:

$a _ { s t }$ the previous solution's assignment. 1 if student s is assigned to teacher t and zero otherwise.

$k _ { s }$ 1 if the administrator would like to keep the previous teacher assignment for student s and 0 otherwise.

$h _ { t }$ 1 if the administrator would like to maintain all the previous student assignments for a teacher (but not restrict further student assignments to this teacher) and 0 otherwise.

The above conditions are typically warranted when the administrator would like to add or subtract students with as minimal of an impact on the current assignment as possible. These definitions result in the added constraints to the model,

$$
x _ {s t} \geq k _ {s} a _ {s t} \quad \text { for } \quad s \in \mathcal {S} \quad \text { and } \quad t \in \mathcal {T},\tag{30}
$$

$$
x _ {s t} \geq h _ {t} a _ {s t} \quad \mathrm{for} \quad s \in \mathcal {S} \quad \mathrm{and} \quad t \in \mathcal {T}.\tag{31}
$$

Classroom metrics for assigned students without VAM and achievement proficiency metrics).

<table><tr><td>TeacherClass type</td><td>MartinIEP</td><td>HooverIEP</td><td>VonderheidIEP</td><td>SchumacherIEP</td><td>MartineIEP</td><td>LaneIEP</td><td>ShinnererGIEP</td><td>StetzelGIEP</td></tr><tr><td>Class size</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td><td>23</td><td>24</td><td>24</td></tr><tr><td>Racial diversity rep count</td><td>13</td><td>12</td><td>12</td><td>12</td><td>13</td><td>12</td><td>13</td><td>13</td></tr><tr><td>Boys count</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>13</td><td>13</td><td>14</td></tr><tr><td>Avg academic ability</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.6</td><td>2.5</td><td>2.5</td></tr><tr><td>Avg discipline issues</td><td>3.1</td><td>3.1</td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.2</td><td>3.2</td><td>3.1</td></tr><tr><td>Difficult students</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>IEP students</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td></tr><tr><td>GIEP students</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>5</td></tr><tr><td>Avg VAM predicted</td><td>-1.5</td><td>-3.7</td><td>-1.2</td><td>-3.6</td><td>-4.2</td><td>-3.9</td><td>-1.0</td><td>-2.1</td></tr><tr><td>Avg proficiency likelihood</td><td>43.8</td><td>58.7</td><td>27.9</td><td>47.2</td><td>31.5</td><td>43.1</td><td>85.8</td><td>42.1</td></tr></table>

$d _ { s }$ disciplinary category of student s, $, d _ { s } = 1 , 2 , 3 , \mathrm { o r } 4 .$ , where the highest level indicates the greatest predicted disciplinary issues based on past performance.

Table 3  
Classroom metrics of created classrooms with all metrics).

<table><tr><td>TeacherClass type</td><td>MartinIEP</td><td>HooverIEP</td><td>VonderheidIEP</td><td>SchumacherIEP</td><td>MartineIEP</td><td>LaneIEP</td><td>ShinnererGIEP</td><td>StetzelGIEP</td></tr><tr><td>Class size</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td><td>24</td><td>23</td></tr><tr><td>Racial diversity representation</td><td>12</td><td>12</td><td>13</td><td>13</td><td>12</td><td>13</td><td>13</td><td>12</td></tr><tr><td>Boys</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>14</td><td>13</td><td>13</td></tr><tr><td>Avg academic ability</td><td>2.5</td><td>2.6</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.6</td><td>2.6</td></tr><tr><td>Avg discipline issues</td><td>3.1</td><td>3.2</td><td>3.1</td><td>3.1</td><td>3.0</td><td>3.0</td><td>3.1</td><td>3.1</td></tr><tr><td>Difficult students</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>IEP students</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>0</td><td>0</td></tr><tr><td>GIEP students</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>5</td><td>4</td></tr><tr><td>Avg VAM predicted</td><td>-2.5</td><td>-2.5</td><td>-2.9</td><td>-2.5</td><td>-2.5</td><td>-2.7</td><td>-2.6</td><td>-2.7</td></tr><tr><td>Avg proficiency likelihood</td><td>48.0</td><td>48.0</td><td>47.6</td><td>47.4</td><td>45.6</td><td>48.7</td><td>47.3</td><td>47.8</td></tr></table>

This added functionality allowed the principals to evaluate previous solutions and keep assignments they prefer and then rerun the DSS and allowing it to assign students in a “best of the rest” manner.

## 6.2. Broader relevance

While the application presented herein is specific to a problem at a particular school, the model represents a general problem confronted by tens of thousands of principals each year. Beyond educational administration, the model framework has implications for DSS in determining cross-functional project teams.

Approximately half of business project failures can be attributed to issues with team member selection [9]. In practice, human resource and business managers often lack the time and consistent strategies for determining team fit when selecting employees for project team assignment. These assignments should be based upon their potential fit in each of three categories: fit for the job, fit with the leader, and fit with others [21].

Our model framework as presented can be adapted to assist in these situations. Efectively, our principal is a business manager with a set of clients/projects (classrooms) and project leaders (teachers) with specific requirements. In cross-functional project teams, these requirements consist of skill sets or prior relevant experience for the project (“fit for the job”). Additionally, the manager may have knowledge of which employees do or do not work well together and may wish to restrict or require such pairings on teams (“fit with others” and “fit the leader”). Such requirements parallel the “hard constraints" discussed previously. Additionally, there may be targets for each team to achieve preferred metrics in other descriptive and demographic metrics related to issues of diversity or, more specifically, issues with experience to avoid having unnecessarily inexperienced teams. The ability to define metrics specific to particular projects/clients provides significant modeling flexibility. Using our framework also allows managers to exploit the eficiency of the available solution algorithms for mixed integer linear programs in determining team construction.

While our framework and model has more general implications, we focused on the problem at hand for two reasons: the extent to which this problem is overlooked and the potential impact from a low-cost, easily accessible DSS.

## 6.3. Conclusions

In this paper we present a student-to-teacher assignment DSS allowing school principals to eficiently assign students to teachers with the confidence that their measures of interest, preferences, and obligations are satisfied. This assignment decision process is typically an arduous and thankless task. Few stakeholders are ever fully satisfied. This DSS provides a transparent, efective, and eficient tool to deal with these issues in an unbiased fashion.

As this is a support system, in our experience, the administrators will use the tool to quickly establish a strong starting point and then make minor adjustments to account for intangible factors unaccounted for within the model. The greatest benefit we have seen has been for grades transitioning into a principal's school (e.g., 4th grade in a 4th to 6th grade middle school). The principal does not yet have a relationship with these students and lacks the perspective with which to make informed teacher assignments. In the absence of these relationships, this DSS is highly valuable and time-saving.

Based upon the success of the DSS in its trial run, we are working to expand its use to other schools within the school district. We look forward to working with the school district to refine and improve this DSS for expanded use. To request the associated workbook or seek advice on adapting the model, please contact the corresponding author at the email provided.

## Appendix A

## Indices and sets

$s \in S$ set of students to be assigned classes (typically $| S | = 2 0 0 )$

$t \in \mathcal { T }$ set of teachers to be assigned students (typically | | 8= ).

$S _ { \mathrm { I E P } } , S _ { \mathrm { G I E P } } \subset S$ set of students in educational support category IEP and GIEP, respectively.

$\mathcal { T } _ { \mathrm { I E P } } , \mathcal { T } _ { \mathrm { G I E P } } \subset \mathcal { T }$ set of teachers assigned to teach educational support IEP and GIEP students, respectively.

$s \in { \mathcal { B } } \subset S$ subset of boys.

$s \in { \mathcal { R } } \subset S$ subset of students from underrepresented races.

$s \in { \mathcal { P } } \subset S$ subset of students with a history of being severely disruptive (problem) history.

Data

$p _ { s t }$ 1 if the principal prefers to place student s with teacher t and 0 otherwise.

$r _ { s t }$ 1 if the principal prefers to restrict student s from being placed with teacher t and zero otherwise.

$e _ { s }$ administrator and teacher's subjective educational ability rating of studen $s , e _ { s } = 1 , 2 , 3$ , or 4, where the higher ranking signifies a student with a stronger performance history.

$\nu _ { s }$ testing service-provided educational growth rating or prediction of student s, where the higher rating signifies a student with a stronge predicted performance.

$\ell _ { s }$ testing service-provided educational likelihood of proficiency for student s, the value is provided as a likelihood between zero and 100. τ<sub>size</sub> The target class size. Defined as ${ \frac { | S | } { | { \boldsymbol { \eta } } | } } .$

$\tau _ { \mathrm { b o y s } }$ The target number of boys in each class. Defined as ${ \frac { | { \mathcal { B } } | } { | { \mathcal { T } } | } } .$

τ<sub>race</sub> The target number of students from underrepresented races in each class. Defined as $\underline { { \vert \mathcal { B } \vert } }$ .

τ<sub>ed</sub> race <sup>|</sup> <sup>|</sup> The target cumulative subjective educational background ranking in each class. Defined as $\underline { { \sum _ { s \in S } e _ { S } } }$

τ<sub>disc</sub> The target cumulative disciplinary background rating in each class. Defined as $\textstyle \sum _ { s \in S } d _ { s }$

τ<sub>prob</sub> The target number of students a history of being severely disruptive in each class. Defined $\mathbf { a s } ~ { \frac { | { \mathcal { P } } | } { | { \mathcal { T } } | } } .$

τ<sub>IEP</sub> The target cumulative number of GIEP students in each class. Defined as $\frac { | S _ { \mathrm { I E P } } | } { \cdot - }$ for classes in $\mathcal { T } _ { \mathrm { I E P } } .$

τ<sub>GIEP</sub> The target cumulative number of GIEP students in each class. Defined as <sup>|</sup> <sup>|IEP|</sup> <sup>|GIEP</sup> for classes in |TGIEP $\mathcal { T } _ { \mathrm { G I E F } }$ .

$$
\frac {| \mathcal {S} _ {\mathrm{GIEP}} ^ {\mathrm{IEP}} |}{| \mathcal {T} _ {\mathrm{GIEP}} |}
$$

τ<sub>vam</sub> vam The target cumulative VAM in each class. Defined as $\textstyle \sum _ { s \in S } \nu _ { s }$ s

| ${ \frac { \sum _ { s \in S } \ell _ { s } } { | \mathcal { T } | } } .$ τ<sub>prof</sub> The target cumulative likelihood of proficiency in each class. Defined as

$\boldsymbol { \rho } _ { \cdot , t }$ The (optional) objective weight for each metric for each teacher t’s class.

## Decision variables

$x _ { s t }$ 1 if student s is assigned to teacher t; 0 otherwise.

$\delta _ { \mathrm { s i z e } , t }$ an upper bound on the proportional deviation from the target size for the class assigned to teacher $t \in \mathcal { T }$

$\delta _ { \mathrm { b o y s } , t }$ an upper bound on the proportional deviations from the target number of boys in the class assigned to teacher $t \in \mathcal T$

$\delta _ { \mathrm { r a c e } , t }$ an upper bound on the proportional deviations from the target number of students from underrepresented races for the class assigned to teacher $t \in \mathcal { T }$

$\delta _ { \mathrm { e d } , t }$ an upper bound on the proportional deviations from the target subjective educational rankings for the class assigned to teacher $t \in \mathcal { T }$

$\delta _ { \mathrm { d i s c } \ , t }$ an upper bound on the proportional deviations from the target cumulative disciplinary ranking for the class assigned to teacher $\in \mathcal { T } .$

$\delta _ { \mathrm { p r o b } \ , t }$ an upper bound on the proportional deviations from the target number of students with a history of being severely disruptive in the class assigned to teacher $t \in \mathcal { T }$

$\delta _ { \tt I E P \_ t }$ an upper bound on the proportional deviations from the target cumulative number of IEP students in an IEP class for the class assigned to teacher $t \in \mathcal { T } _ { \mathrm { I E P } } .$

$\delta _ { \mathrm { G I E P } , t }$ an upper bound on the proportional deviations from the target cumulative number of IEP students in an IEP class for the class assigned to teacher $t \in \mathcal { T } _ { \mathrm { G I E P } }$

$\delta _ { \mathrm { v a m } ~ , t }$ an upper bound on the proportional deviations from the target cumulative VAM student ratings for the class assigned to teacher $t \in \mathcal T$

$\delta _ { \mathrm { p r o f } , t }$ an upper bound on the proportional deviations from the target cumulative student proficiency likelihoods for the class assigned to teacher $t \in \mathcal { T }$

## Formulation

$$
\mathbf {x}, \delta \sum_ {t \in \mathcal {T}} [ \rho_ {\mathrm{size}, t} \delta_ {\mathrm{size}, t} + \rho_ {\mathrm{boys}, t} \delta_ {\mathrm{boys}, t} + \rho_ {\mathrm{race}, t} \delta_ {\mathrm{race}, t} + \rho_ {\mathrm{ed}, t} \delta_ {\mathrm{ed}, t} +\tag{32a}
$$

$$
\rho_ {\mathrm{disc}, t} \delta_ {\mathrm{disc}, t} + \rho_ {\mathrm{size}, t} \delta_ {\mathrm{size}, t} + \rho_ {\mathrm{vam}} \delta_ {\mathrm{vam}, t} + \rho_ {\mathrm{prof}, t} \delta_ {\mathrm{prof}, t} ] +
$$

$$
\sum_ {i \in \mathcal {T} _ {\mathrm{IEP}}} \rho_ {\mathrm{IEP}, t} \delta_ {\mathrm{IEP}, i} + \sum_ {g \in \mathcal {T} _ {\mathrm{GIEP}}} \rho_ {\mathrm{GIEP}, t} \delta_ {\mathrm{GIEP}, g}\tag{32b}
$$

(32c)

s.t.

$$
\sum_ {t \in \mathcal {T}} x _ {s t} = 1, \qquad \text { for } \quad s \in \mathcal {S}\tag{32d}
$$

$$
\sum_ {t \in \mathcal {T} _ {\mathrm{IEP}}} x _ {s t} = 1, \qquad \text {for} \quad s \in \mathcal {S} _ {\mathrm{IEP}}\tag{32e}
$$

$$
\sum_ {t \in \mathcal {T} _ {\mathrm{GIEP}}} x _ {s t} = 1, \quad \text { for } \quad s \in \mathcal {S} _ {\mathrm{GIEP}}\tag{32f}
$$

$$
\sum_ {t \in \mathcal {T}} p _ {s t} x _ {s t} = 0, \qquad \text {for} \quad s \in \mathcal {S} \quad \text {if} \quad p _ {s t} = 1 \quad \text {for some} \quad t \in \mathcal {T}\tag{32g}
$$

$$
\sum_ {t \in \mathcal {T}} r _ {s t} x _ {s t} = 1, \quad \text { for } \quad s \in \mathcal {S} \quad \text { if } \quad r _ {s t} = 1 \quad \text { for   some } \quad t \in \mathcal {T}\tag{32h}
$$

$$
\delta_ {\mathrm{size}, t} \geq \frac {\sum_ {s \in \mathcal {S}} x _ {s t} - \tau_ {\mathrm{size}}}{\tau_ {\mathrm{size}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32i}
$$

$$
\delta_ {\mathrm{size}, t} \geq \frac {\tau_ {\mathrm{size}} - \sum_ {s \in \mathcal {S}} x _ {s t}}{\tau_ {\mathrm{size}}}, \quad \mathrm{for} \quad t \in \mathcal {T}\tag{32j}
$$

$$
\delta_ {\mathrm{boys}, t} \geq \frac {\sum_ {s \in \mathcal {B}} x _ {s t} - \tau_ {\mathrm{boys}}}{\tau_ {\mathrm{boys}}}, \quad \mathrm{for} \quad t \in \mathcal {T}\tag{32k}
$$

$$
\delta_ {\mathrm{boys}, t} \geq \frac {\tau_ {\mathrm{boys}} - \sum_ {s \in \mathcal {B}} x _ {s t}}{\tau_ {\mathrm{boys}}}, \quad \mathrm{for} \quad t \in \mathcal {T}\tag{321}
$$

$$
\delta_ {\mathrm{race}, t} \geq \frac {\sum_ {s \in \mathcal {R}} x _ {s t} - \tau_ {\mathrm{race}}}{\tau_ {\mathrm{race}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32m}
$$

$$
\delta_ {\mathrm{race}, t} \geq \frac {\tau_ {\mathrm{race}} - \sum_ {s \in \mathcal {R}} x _ {s t}}{\tau_ {\mathrm{race}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32n}
$$

$$
\delta_ {\mathrm{ed}, t} \geq \frac {\sum_ {s \in \mathcal {S}} e _ {s} x _ {s t} - \tau_ {\mathrm{ed}}}{\tau_ {\mathrm{ed}}}, \quad \mathrm{for} \quad t \in \mathcal {T}\tag{320}
$$

$$
\delta_ {\mathrm{ed}, t} \geq \frac {\tau_ {\mathrm{ed}} - \sum_ {s \in \mathcal {S}} e _ {s} x _ {s t}}{\tau_ {\mathrm{ed}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32p}
$$

$$
\delta_ {\mathrm{disc}, t} \geq \frac {\sum_ {s \in \mathcal {S}} d _ {s} x _ {s t} - \tau_ {\mathrm{disc}}}{\tau_ {\mathrm{disc}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32q}
$$

$$
\delta_ {\mathrm{disc}, t} \geq \frac {\tau_ {\mathrm{disc}} - \sum_ {s \in \mathcal {S}} d _ {s} x _ {s t}}{\tau_ {\mathrm{disc}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32r}
$$

$$
\delta_ {\mathrm{IEP}, t} \geq \frac {\sum_ {s \in \mathcal {S} _ {\mathrm{IEP}}} x _ {s t} - \tau_ {\mathrm{IEP}}}{\tau_ {\mathrm{IEP}}}, \quad \mathrm{for} \quad t \in \mathcal {T} _ {\mathrm{IEP}}\tag{32s}
$$

$$
\delta_ {\mathrm{IEP}, t} \geq \frac {\tau_ {\mathrm{IEP}} - \sum_ {s \in \mathcal {S} _ {\mathrm{IEP}}} x _ {s t}}{\tau_ {\mathrm{IEP}}} \quad \mathrm{for} \quad t \in \mathcal {T} _ {\mathrm{IEP}}\tag{32t}
$$

$$
\delta_ {\mathrm{GIEP}, t} \geq \frac {\sum_ {s \in \mathcal {S} _ {\mathrm{GIEP}}} x _ {s t} - \tau_ {\mathrm{GIEP}}}{\tau_ {\mathrm{GIEP}}}, \quad \text {for} \quad t \in \mathcal {T} _ {\mathrm{GIEP}}\tag{32u}
$$

$$
\delta_ {\mathrm{GIEP}, t} \geq \frac {\tau_ {\mathrm{GIEP}} - \sum_ {s \in \mathcal {S} _ {\mathrm{GIEP}}} x _ {s t}}{\tau_ {\mathrm{GIEP}}} \quad \mathrm{for} \quad t \in \mathcal {T} _ {\mathrm{GIEP}}\tag{32v}
$$

$$
\delta_ {\mathrm{prob}, t} \geq \frac {\sum_ {s \in \mathcal {P}} x _ {s t} - \tau_ {\mathrm{prob}}}{\tau_ {\mathrm{prob}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32w}
$$

$$
\delta_ {\mathrm{prob}, t} \geq \frac {\tau_ {\mathrm{prob}} - \sum_ {s \in \mathcal {P}} x _ {s t}}{\tau_ {\mathrm{prob}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32x}
$$

$$
\delta_ {\mathrm{vam}, t} \geq \frac {\sum_ {s \in \mathcal {S}} v _ {s} x _ {s t} - \tau_ {\mathrm{vam}}}{\tau_ {\mathrm{vam}}}, \quad \mathrm{for} \quad t \in \mathcal {T}\tag{32y}
$$

$$
\delta_ {\mathrm{vam}, t} \geq \frac {\tau_ {\mathrm{vam}} - \sum_ {s \in \mathcal {S}} v _ {s} x _ {s t}}{\tau_ {\mathrm{vam}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32z}
$$

$$
\delta_ {\mathrm{prof}, t} \geq \frac {\sum_ {s \in \mathcal {S}} \ell_ {s} x _ {s t} - \tau_ {\mathrm{prof}}}{\tau_ {\mathrm{prof}}}, \quad \text { for } \quad t \in \mathcal {T}\tag{32aa}
$$

$$
\delta_ {\mathrm{prof}, t} \geq \frac {\tau_ {\mathrm{prof}} - \sum_ {s \in \mathcal {S}} \ell_ {s} x _ {s t}}{\tau_ {\mathrm{prof}}}, \quad \text {for} \quad t \in \mathcal {T}\tag{32ab}
$$

$$
x _ {s t} \in \{0, 1 \}, \quad \text { for } \quad s \in \mathcal {S} \quad \text { and } \quad t \in \mathcal {T}\tag{32ac}
$$

$$
\delta_ {\text { size }, t}, \delta_ {\text { boys }, t}, \delta_ {\text { race }, t}, \delta_ {\text { ed }, t}, \delta_ {\text { disc }, t} \geq 0\tag{32ad}
$$

$$
\delta_ {\mathrm{prob}, t}, \delta_ {\mathrm{IEP}, t}, \delta_ {\mathrm{GIEP}, t}, \delta_ {\mathrm{vam}, t}, \delta_ {\mathrm{prof}, t} \geq 0\tag{32ae}
$$

## References

[1] OpenSolver for Excel, https://opensolver.org/ , Accessed date: 30 September 2018.

[2] Standard Excel Solver - dealing with problem size limits, https://www.solver.com standard-excel-solver-dealing-problem-size-limits , Accessed date: 30 September 2018.

[3] American Statistical Association, ASA Statement on Using Value-Added Models for Educational Assessment. http://www.amstat.org/asa/files/pdfs/POL-ASAVAM: Statement.pdf, (2014).

[4] K. Baker, S. Powell, Methods for assigning students to groups: a study of alternative objective functions, Journal of the Operational Research Society 53 (4) (2002) 397–404.

[5] E. Behrstock-Sherratt, The Role of School Leaders in Ensuring an Equitable Distribution of Teachers: A Review of the Literature, The Center on Great Teachers and Leaders. 2011.

[6] R.S. Bigler, L.S. Liben, Developmental intergroup theory: explaining and reducing children's social stereotyping and prejudice, Current Directions in Psychological Science 16 (3) (2007) 162–166.

[7] C. Collins, A. Amrein-Beardsley, Putting growth and value-added models on the map: a national overview. Teachers College Record 16 (2014).

[8] R. Cutshall, S. Gavirneni, K. Schultz, Indiana University's Kelley School of Business uses integer programming to form equitable, cohesive student teams, Interfaces 37 (3) (2007) 265–276.

[9] R. De Cooman, T. Vantilborgh, M. Bal, X. Lub, Creating inclusive teams through perceptions of supplementary and complementary person-team fit: examining the relationship between person-team fit and team efectiveness, Group & Organization Management 41 (3) (2016) 310–342.

[10] S. Dieterle, C.M. Guarino, M.D. Reckase, J.M. Wooldridge, How do principals assign students to teachers? Finding evidence in administrative data and the implications for value added, Journal of Policy Analysis and Management 34 (1) (2014) 32–58.

[11] J. Forrest, T. Ralphs, S. Vigerske, LouHafer, B. Kristiansson, ipfasano, EdwinStraver M. Lubin. H.G. Santos, rlougee, M. Saltzman, COIN-OR/CBC: Version 2.9.9. (July 2018).

[12] L. Foulds, D. Johnson, SlotManager: a microcomputer-based decision support system for university timetabling, Decision Support Systems 27 (4) (2000) 367–381.

[13] A.W. Gill, The school class allocation problem–maximising friendship requests subject to diversity requirements, Journal of the Operational Research Society 66 (7) (Jul 2015) 1091–1100.

[14] R. Goldring, L. Gray, A. Bitterman, Characteristics of Public and Private Elementary and Secondary School Teachers in the United States: Results from the 2011–12 Schools and Stafing Survey. First Look. NCES 2013-314. National Center for Education Statistics, 2013.

[15] C. Guarino, M. Reckase, B. Stacy, J. Wooldridge, A comparison of student growth percentile and value-added models of teacher performance, Statistics and Public Policy 2 (1) (2015) 1–11

[16] G. Hopkins, Making Class Lists Needn’t Be a Nightmare, http://www. educationworld.com/a admin/admin/admin118.shtml. (May 2009)

[17] L.J. Hilliard, L.S. Liben, Difering levels of gender salience in preschool classrooms: efects on children's gender attitudes and intergroup bias, Child Development 81 (6) (2010)1787-1798.

[18] J. Johnes, Operational research in education, European Journal of Operational

Research 243 (3) (2015) 683–696.

[19] S. Koslin, B. Koslin, R. Pargament, H. Waxman, Classroom racial balance and stu dents' interracial attitudes, Sociology of Education 45 (4) (1972) 386–407.

[20] B. Krauss, J. Lee, D. Newman, Optimizing the assignment of students to classes in an elementary school, INFORMS Transactions on Education 14 (1) (2013) 39–44.

[21] A.L. Kristof-Brown, J.Y. Seong, D.S. Degeest, W.-W. Park, D.-S. Hong, Collective fit perceptions: a multilevel investigation of person-group fit with individual-level and team-level outcomes, Journal of Organizational Behavior 35 (7) (2014) 969–989.

[22] S. Lavertu, We all need help: “Big Data" and the mismeasure of public adminis tration, Public Administration Review 76 (6) (2016) 864–872

[23] R. Lougee-Heimer, The Common Optimization INterface for Operations Research, IBM Journal of Research and Development 47 (1) (2003) 57–66

[24] A.J. Mason, OpenSolver - an open source add-in to solve linear and integer pro gammes in Excel, in: D. Klatte, H.-J. Lüthi, K. Schmedders (Eds.), Operations Research Proceedings 2011, Springer Berlin Heidelberg, Berlin, Heidelberg, 2012, pp. 401–406.

[25] J. Miranda, P.A. Rey, J.M. Robles, udpSkeduler: a web architecture based decision support system for course and classroom scheduling, Decision Support Systems 52 (2) (2012) 505–513.

[26] B.M. Nesmith, Deciding on Classroom Composition: Factors Related to Principals Grouping Practices, Ph.D. thesis Georgia Southern University, Digital Commons@Georgia Southern, 2018.

[27] X. Newton, L. Darling-Hammond, E. Haertel, E. Thomas, Value-added modeling of teacher efectiveness: an exploration of stability across models and contexts, Education Policy Analysis Archives 18 (2010) 23.

[28] U.S. Department of Education, Race To The Top: Fact Sheet, https://www2.ed.gov prorams/racetothetop/factsheet.html, (December 2009).

[29] SAS, Pennsylvania Value Added Assessment System (PVAAS) Public Access, https:/ pvaas.sas.com/welcome.html, (2018).

[30] SAS, SAS EVAAS for K-12 Statistical Models, https://www.sas.com/content/dam/ SAS/en\_us/doc/whitepaper1/sas-evaas-k12-statistical-models-107411.pdf, (2018).

[31] R.K. Şeref, Ahuja, Spreadsheet-Based Decision Support Systems, Springer Berlin Heidelberg, Berlin, Heidelberg, 2008, pp. 277–298, https://doi.org/10.1007/978- 3-540-48713-5\_14.

[32] A.S. Wells, L. Fox, D. Cordova-Cobo, How Racially Diverse Schools and Classrooms Can Benefit All Students, https://tcf.org/content/report/how-racially-diverse schools-and-classrooms-can-benefit-all-students. (February 2016).

Matthew D. Bailey is Program Chair and Associate Professor of Analytics and Operations Management within the Freeman College of Management at Bucknell University. He re ceived his Ph.D. in Industrial and Operations Engineering from the University of Michigan. His primary research interests are the theory and application of models for sequential decision making under uncertainty. In particular, he is interested in a broad range of areas within healthcare, medical decision-making, and adversarial network optimization. This work has resulted in publications in journals such as Operations Research, IIE Transactions, EJOR, Naval Research Logistics, Decision Analysis, Decision Support Systems, and Networks.

David Michaels is the principal of Curtin Intermediate School in the Williamsport Are School District
