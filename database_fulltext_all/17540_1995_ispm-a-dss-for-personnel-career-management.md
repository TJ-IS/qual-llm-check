---
otero_id: 17540
otero_key: "5BCXHFK2"
title: "ISPM: A DSS for personnel career management"
authors: "M. Bellone; M. Merlino; R. Pesenti"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00063-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# ISPM: A DSS for personnel career management

M. Bellone, M. Merlino, R. Pesenti \*

DIST-University of Genoa, Via all'Opera Pia 13, 16145 Genova, Italy

## Abstract

A decision support system (ISPM) to assist the user in personnel career management is presented. The system has been designed mainly to deal with the problem of establishing what training a human resource should undergo before occupying a job position. However, the system is also able to suggest both a set of job positions for a human resource with a given competence and the possible relations of a new job position inside an existing job-organization structure.

Keywords: DSS experience; Human resource management; Enterprise modeling

## 1. Introduction

Human Resource Management (HRM) is one of the major areas of interest for managerial culture and has an increasing impact on the competitive position of a firm. Research in the field of HRM policies and practice in leading multinational European companies [6] has pointed out the growing involvement of personnel departments in strategic planning and the need for a deep reengineering process of HRM approaches and techniques. In particular, all components of personnel career management should be much more integrated: organization, job design, career paths, and training.

In this context, a first step toward such integration can be achieved by means of ISPM (Interactive Support system for Personnel career Management), which is the decision support system (DSS) to assist a company in personnel career management described in this paper. In particular, ISPM takes into account the interrelations between career paths and training so that they may be integrated and planned consistently with the objectives of a firm and with the tasks and competences at the various levels of an organization structure.

There exists a vast literature on the use of optimization techniques for human resource management (see, for example, [10] for early references). Optimization procedures are usually included in a DSS structure that allows man-machine interaction, as it is difficult, if not impossible, to develop a mathematical model capable of taking into account all the aspects of interest to human resources. Many HRM aspects have been considered, starting from operative-level problems of personnel assignment to specific jobs [2], [8], [12], [15], up to high-level (strategic) decision problems concerning the definition of recruiting policies [1], [11], [13]. In particular, the latter references deal with manpower planning inside a company as a function of the promotion and hiring policies defined at the strategic decision level, where the human resources are evaluated in terms of number and average characteristics. Instead, the DSS described in [14] assists the user in strategic personnel planning over time by differentiating each employee from the others and by taking into account the necessary training. The environment in which it is used (manpower planning of airline pilots) presents particular characteristics: a unique way of training, limited resources, limited personnel available, new hirings allowed only for lowest-level positions. ISPM show some similarities to the DSS described in [14], as it deals with the characteristics of each employee and faces the problem of training. However, whereas the DSS presented in [14] copes with long-term strategic problems, ISPM considers more operative problems. In addition, ISPM has been designed for a completely different environment (e.g., information systems department of a manufacturing firm), where employees may undergo many different types of training. ISPM assumes, in accordance with [5], that, in the environments considered, the company's needs for employees' competences vary quite fast and unpredictably. For these reasons, ISPM is mainly focused on single human resources in order to assist the company in determining the training required to satisfy its immediate necessities. However, ISPM also permits a longer-term analysis of possible careers of human resources, for the purpose (different from those of the above-mentioned works) of defining the training experiences that makes such resources highly flexible.

In the next section, the reasons that led to the implementation of ISPM are outlined. In Section 3, a formal definition of the problems that ISPM can address is provided. In Section 4, the implemented procedures are described, and, in Section

5, a few results on a case study are reported. Finally, in Section 6, some conclusions are drawn.

## 2. The problem

ISPM has been developed as a tool for an international consultant firm (in the following indicated as IC) that is specialized, among other things, in organization restructuring and information technology outsourcing, but that may also be well suited for companies with departments subject to considerable personnel turnovers and to obsolescence of job positions.

The ISPM project started when IC had to reorganize the information systems department of the Italian greatest steel company (IGSC). The IGSC personnel database described each employee according to his/her personal and career data and to some of his/her skills, i.e., proficiency based on aptitude, practice, or training. The first tasks to be performed by the IC consultants were to rationalize the information present, in quite a confused way, in such a database and to investigate the decisional process followed by the IGSC managers in job assignments. From the results of such a work [7], the authors of this paper deduced that it is possible to extend the decisional process pursued by the IGSC managers to many companies. In particular, the following aspects of such a process are worth mentioning: many different skills of interest were examined, even though, when focusing on the assignments to a particular job position, only a relative small number of skills, in general, different for each position, were considered. The decision makers obtain a first holistic picture of the employees under consideration by performing an average evaluation to their skills with respect of few large classes (as in [12]), after excluding all candidates that do not meet minimal requirements. Whenever possible, the decision makers rank the candidates on the basis of their skills.

Eventually, a set of about 100 different skills were considered to be of interest to the company. Such a skill set included almost completely the skills mentioned in [5] and skills that are also needed by departments different from the considered one. In particular, the skills may be partitioned into four main subsets, which should coincide with the large classes considered by the decision makers:

\- functional skills: knowledge of the processes involved in the company activity (e.g., knowledge of the company functions and of the company information systems, etc.);

\- managerial skills: aptitudes for handling and organizing people (e.g., capability for business presentation, vertical communications, creativity, etc.);

\- methodological skills: aptitudes for organizing one's own work according to some specific methodologies (e.g., knowledge of break-even analysis, capacity management, cost definition, etc.);

\- technical skills: technical expertise in the job to be performed (e.g., knowledge of databases, of operating systems, etc.);

![](/api/attachments/5BCXHFK2/fulltext/images/637701f690f2d31bf727226d6f055944ea64cf4119739f43982cc19bd892676f.jpg)

1. Operator 2. Network manager

3. Network installer 4. Programmer

5. Attached to user-help desk 6. Network logistics technician

7. Technical analyst 8. Database administrator

9. HW technician 10. SW technician

11. Functional analyst 12. Technological architecture expert

13. Office automation ... etc.
architecture expert

30. Maintenance technician ... etc.

Fig. 1. The job organization structure of the internal information system department of a large Italian steel firm.

Note that only the last subset includes skills specifically for the particular department considered.

The above observations also suggested that six different values (0 minimum, 5 maximum) could be assumed to be sufficient to evaluate the different skill levels of employees. An even number of appraisal levels was adopted (unlike [5] which uses only five values) to model the decision makers' effort towards differentiating each employee. An even number prevents the possibility of translating into numerical values expressions such as "average" which are possibly misleading.

## 3. Structure of the model

This section describes in detail the data structures used by ISPM and the decisional processes this system can support.

ISPM works on a database describing three kinds of entities: Human Resources (HRs), i.e., employees, Job Positions (JPs) (each possibly occupied by numerous HRs) and Training Experiences (TEs), i.e., training courses or seminars and all controllable experiences (e.g., apprenticeship, stays in foreign countries) that can improve an employee's skill.

The possible career paths inside a company are described by use of a “precedence” relation defined for the set of job positions. In particular, a job position $jp_{a}$ is said to precede $jp_{b}$ (directly), if an employee may be moved from the former position to the latter in the development of his career, without passing through a third position. Using such a relation among JPs, the Job-Organization Structure (JOS) may be represented as a graph (Fig. 1). The precedence relation is not complete and, due to a horizontal mobility, may also allow cycles. A job position is defined as a “lowest” JP if it does not have any predecessor, apart from those on which it depends cyclically. A JP, $jp_{a}$ , is “reachable” from $jp_{b}$ if there exists a direct (career) path from $jp_{b}$ to $jp_{a}$ . All JPs reachable from the same JP are said to belong to the same area. Some JPs may belong to more than one area. Finally, the “career development level” (the CD level) of a JP is defined as the minimum topological distance of the JP from a lowest position. In this context, note that a precedence relation between two job positions does not necessarily imply a direct hierarchical dependence. On the other hand, there exists an obvious relation between the CD level of a JP and the authority and responsibility of the HRs that occupy such a JP.

It is worth noting that all case studies to test the system were found based on similar JOSs. The JPs at the low CD level were organized approximately into a tree (or a forest), with few possibilities, if any, of moving from one set of career paths to another, whereas the JPs at the high CD level were connected even in a cyclical way. This is due to the fact that the technical expertise of an HR usually plays a fundamental role in the assignment of an HR to a lowest position (e.g., operator instead of maintenance technician in Fig. 1), but loses its relative importance for higher-level positions where managerial capabilities become more and more important.

ISPM supports the solution of some Multi-Criteria Decision Making (MCDM) problems $[4]$ , which arise during job-organization restructuring, i.e., the “atomic” problems of:

\- determining the TEs that an HR must attend to be assigned to a given JP;

\- assigning a new HR to a JP, or moving an old HR from one JP to another;

\- inserting a new JP in an existing JOS;

and some other problems, such as determining the JPs and the TEs that an HR must respectively occupy and attend before reaching a given career objective. However, since ISPM solves the latter problems by considering sequences of atomic problems, they are not addressed in this work for the sake of brevity.

In general, real-world MCDM problems cannot be solved in a way that is optimal according to all criteria; therefore, any chosen solution is the result of some sort of compromise, hence it may be subject to criticism. For any MCDM problem faced, the aim of ISPM is to establish a restricted set of solutions to be submitted to the user, who will make the final decision. ISPM selects the candidate solutions from the non-dominated ones by means of some heuristics.

Note that a solution is said to be “dominated” if there exists another solution that is better for all the objectives considered.

Every decisional process considered in this work hinges on the concept of skill. In particular, the default configuration of ISPM considers the about 100 skills that have been defined in the study described in the previous section and that are partitioned into four subsets (functional, managerial, methodological, and technical skills). However, ISPM has been designed to accept flexibly any number of skills and of skill partitions. All the three kinds of entities present in the ISPM database are defined in terms of values of some skills and of other lexically descriptive attributes. The lexical attributes describing an HR are, by default (but with the possibility of increasing their number), name, code, department, etc., but also a short curriculum vitae and possibly some reports describing the HR's attitude, goals, psychology, health, and family. Analogously, the lexical attributes describing a JP are, by default, identification, code, entrance salary, etc., but also particular notes concerning, for instance, the responsibilities involved. Finally, the lexical attributes describing a TE are, by default, identification, code, cost, duration, etc., but also particular notes regarding, for instance, the degrees of satisfaction of previous participants. These lexical attributes are used by ISPM to perform simple database operations (e.g., selecting all the HRs occupying a particular JP) and to obtain more information about the HRs of interest to the user of the system. However, they are not processed by the ISPM algorithms, which, so far, only works on skill values. In particular, apart from the lexical attributes, HRs are characterized by their skill values; JPs are characterized by the minimum skill values that employees must possess to be assigned to such positions; finally, TEs are characterized by the minimum skill values that employees must have to enroll for the courses and by the skill values that employees are supposed to obtain by attending the courses. In general, a single TE allows an HR to improve more than one skill. As mentioned earlier, skill values range from 0 to 5, where 0 means that either an HR has not a given skill or a skill is of no interest for a JP or a TE. Such skill values are external inputs to ISPM.

In the following, for a given human resource $hr_{i}$ , $hr_{is}$ will indicate the $hr_{i}$ level with respect to the s-th skill; analogously, $jp_{ks}$ will denote the s-th skill level required for a generic job position $jp_{k}$ ; $te_{ms}$ will be the s-th skill level reached by attending the training experience $te_{m}$ ; and $te_{mr}$ will indicate the minimum level required (with respect to the r-th skill) to enroll for the same training experience.

As previously mentioned, the atomic MCDM problems ISPM is able to cope with are the following:

## 3.1. Problem 1 (determination of TEs).

Given a generic HR, say $hr_{i}$ , who has been assigned to the JP, $jp_{k}$ , determine the TEs that $hr_{i}$ should attend in order to reach the skill levels required for $jp_{k}$ on the basis of the following objectives:

(1) $\mathrm{hr}_{\mathrm{i}}$ should attend the minimum number of TEs;

(2) the skill levels of $hr_{i}$ , after he has attended the selected TEs, should be as close as possible to the minimum skill levels required for $jp_{k}$ ;

(3) the TEs should be chosen from an a-priori limited set.

## 3.2. Problem 2 (assignment of an HR to a JP).

Given a generic HR, say $hr_{i}$ , and a set R of JPs, determine the JPs in R that best suit the $hr_{i}$ skills on the basis of the following objectives:

(1) the skill levels required for the selected JPs should exceed as little as possible the $hr_{i}$ skills;

(2) the hr; skills should exceed as little as possible the skill levels required for the selected JPs;

(3) the selected JPs should require $hr_{i}$ to increase the minimum number of his skills.

## 3.3. Problem 3 (inserting a new JP).

Given a new JP, say $jp_{k}$ , and an already existing JOS (made up of at least one JP), determine where $jp_{k}$ can be inserted inside the JOS on the basis of the following objectives:

(1) $jp_{k}$ should precede/follow JPs requiring higher/lower managerial and methodological skill levels;

(2) $jp_{k}$ should precede/follow JPs requiring analogous functional and technical skills.

The rationale of objectives (1) and (2) of Problem 1 and of objectives (1) and (3) of Problem 2 is that $hr_{i}$ should make the minimum effort to be ready for position $jp_{k}$ ; hence $hr_{i}$ should spend the minimum time in unproductive activities. In this context, note that an HR usually requires time not only to attend a TE but also to completely master the TE content. From this point of view, it should be clear that the learning effort made by $hr_{i}$ depends not only on the number of TEs he has to attend, but also on how much he must improve his competences. Objective (2) of Problem 1 and objective (2) of Problem 2 are justified by the necessity for not wasting an HR's competences (or, vice versa, for fully exploiting them). Objective (3) of Problem 1 is justified by the need for reducing the organization load and costs; if such an objective is attained, it is likely that two or more HRs assigned to the same JP will attend the same TEs. The objectives of Problem 3 have been derived from the generalization of the empirical study mentioned in Section 2 (however, see the comments after the description of the algorithm associated with Problem 3 in the next section)

## 4. Modeling the decisional processes

This section describes the algorithms implemented in ISPM to support the decisional processes previously defined. As a general observation, it should be stressed that all the algorithms implemented in ISPM may be made interactive to such an extent that each step must be confirmed by the user. Moreover, a parameter, say n (as it will be indicated in the following), may be taken such that, whenever an optimization step is performed, ISPM will yield the first n best alternatives, together with their descriptions in terms of skills and lexical attributes, and, before continuing, ISPM will wait for the user to make a choice. Analogously, the depths of some searches may be parametrized, too.

## 4.1. Problem 1

Problem 1 is a generalization of the minimum set-covering problem, hence it is an NP-hard problem [3]. On the basis of this observation, ISPM solves this problem first by defining a set $T_{k}$ of TEs that attain objectives (2) and (3), then by selecting the minimum number of TEs necessary to $hr_{i}$ from such a limited set $T_{k}$ by means of a standard enumerative routine. Needless to say, the more limited the set $T_{k}$ , the faster the enumerative routine gives the optimal solution.

In particular, ISPM implements the following four-step procedure:

step (1) for any skill s such that $jp_{ks} > 0$ , a generic TE, $te_{m}$ , is initially included in $T_{k}$ iff $te_{ms}^{-} < jp_{ks}$ and $jp_{ks} \leq te_{ms} \leq jp_{ks} + \Delta t_{s}$ , where $\Delta t_{s}$ is a threshold fixed by the user;

step (2) the number of TEs in $T_{k}$ is reduced; for any skill s of interest, the TEs that remain included in $T_{k}$ are only the first n TEs that minimize the distance

$$
\begin{array}{c} \mathrm{d} _ {1} (\mathrm{jp} _ {\mathrm{k}}, \mathrm{te} _ {\mathrm{m}}) = \Sigma_ {\mathrm{s} \in S ^ {\prime}} (\mathrm{jp} _ {\mathrm{ks}} - \mathrm{te} _ {\mathrm{ms}}) ^ {2}, \\ \mathrm{te} _ {\mathrm{m}} \in T _ {\mathrm{k}}, \end{array}\tag{1}
$$

where $S'$ is the set of skills requiring a level higher than zero for the position $jp_{k}$ ;

step (3) if, for some skill s in S', T $_{k}$ does not include any TE that, for the enrolment, requires minimum skill levels compatible with (i.e., lower than or equal to) the ones of hr $_{i}$ , then T $_{k}$ is updated by applying the methodology described in step 1) only to TEs compatible with hr $_{i}$ and relevant to skill s;

step (4) all TEs relevant to the skills of $hr_{i}$ and all TEs that, for the enrolment, require minimum skill levels incompatible with those of $hr_{i}$ are eliminated from $T_{k}$ ; then an implicit enumerating algorithm determines the first n subsets of TEs in $T_{k}$ that cover all the skill levels required for $\mathbf{jp}_{\mathbf{k}}$ that $\mathbf{hr}_{\mathbf{i}}$ does not have.

The first two steps of the above procedure determine the sets among which to perform the first search for the TEs for $hr_{i}$ . As such sets are defined independently of the HR considered, for each JP, the first time that such a procedure is called, ISPM after executing steps (1) and (2), store their results and does not compute them again as long as no new TEs affecting $JP_{k}$ are introduced (or old TEs are eliminated). It is also worth noting that, in general, step (3) is not performed, as it is quite unlikely that an HR has a skill (required for the position to which he/she has to be assigned) to such a low degree that all TEs relevant to such a skill and present in $T_{k}$ after step (1) require incompatible minimum levels for the enrolment.

## 4.2. Problem 2

In the absence of a JP dominating the others, the system presents the user a limited number of candidate JPs for $hr_{i}$ . If not otherwise specified, ISPM assumes that the set R includes all the JPs reachable from the current position of $hr_{i}$ . If $hr_{i}$ is not a company employee, ISPM assumes R to be made up of all available JPs.

ISPM selects the “best” JPs for $hr_{i}$ from the set R by using the following procedure:

step (1) an order relation is defined in R and the first n best non-dominated JPs are extracted (n is a parameter set by the user). In particular, the chosen JPs are the ones that minimize the distance:

$$
\begin{array}{r l} \mathrm{d} _ {2} (\mathrm{hr} _ {\mathrm{i}}, \mathrm{jp} _ {\mathrm{r}}) & = \Sigma_ {\mathrm{s} \in S} \mathrm{v} _ {\mathrm{s}} \left(\left(\mathrm{hr} _ {\mathrm{is}} - \mathrm{jp} _ {\mathrm{rs}}\right) ^ {+}\right) ^ {2} \\ & + \mathrm{w} _ {\mathrm{s}} \left(\left(\mathrm{jp} _ {\mathrm{rs}} - \mathrm{hr} _ {\mathrm{is}}\right) ^ {+}\right) ^ {2}, \end{array}
$$

$$
\mathrm{jp} _ {\mathrm{r}} \in \mathrm{R},\tag{2}
$$

where S is the set of all the skills, $v_{s}$ and $w_{s}$ are weights a-priori set, and $(.)^{+}$ stands for $\max(.,0)$ ;

step (2) the selected JPs are sorted on the basis of the number of skills for which the skill levels of $hr_{i}$ are higher than or equal to those required; ties are broken on the basis of distance (2);

step (3) the JPs are finally presented to the user, together with all the related information, i.e., the skill requirements and the lexical attributes.

The authors' experience in test cases (e.g., the one outlined in Section 2 and some others on which IC has worked or is currently working) allow them to state that in (2) the default setting $\mathrm{v_s} = \mathrm{w_s} = 1 \forall s \in S$ is in general a good choice. This is not surprising, at least in all cases where the system user is not able to express a partial order relationship among the attributes describing a JP. When this is not the case the values of $\mathrm{v_s}, \mathrm{w_s} \forall s \in S$ may be determined by means of a procedure like that described in [9]. ISPM allows each value of $\mathrm{v_s}$ and $\mathrm{w_s} \forall s \in S$ to be set separately or according to the skill partition (e.g., the default functional, managerial, methodological, or technical one) the skill under consideration belongs to (see also [12]).

It is worth noting that distance (2) is computed with reference to all the skills, even those of no interest for the JP considered, in accordance with objective (2), which requires that no $hr_{i}$ skill be wasted. Moreover, it should be observed that the initial step eliminates dominated JPs as well as JPs requiring skills different from the ones of $hr_{i}$ . However, the choice of an ordering based on a quadratic distance may seem too arbitrary; therefore, step (2) is implemented to partially compensate for such arbitrariness.

## 4.3. Problem 3

ISPM implements a four-step procedure to insert a new JP, jp $_{k}$ , in an existing JOS:

step (1) the user is asked to indicate which set of JP areas (e.g., those belonging to the information systems department) should be considered to insert $jp_{k}$ ;

step (2) the subsets $F_{k}$ and $P_{k}$ of JPs that possibly will follow/precede $jp_{k}$ in the new JOS are identified in the set of JPs belonging to the areas defined by step (1); in particular the JPs selected are the ones for which the weighted sum of required managerial and methodological skill levels is greater/smaller than the weighted sum of the same levels as required for $jp_{k}$ , and which are not preceded/followed by any JP satisfying the same condition;

step (3) both sets $F_{k}$ and $P_{k}$ are further reduced; only the first n JPs that minimize the following distance (3) from $jp_{k}$ are kept in $F_{k}$ and $P_{k}$ . Such a distance is, as usual, a quadratic one:

$$
\begin{array}{r l} \mathrm{d} _ {3} (\mathrm{jp} _ {\mathrm{k}}, \mathrm{jp} _ {\mathrm{r}}) & = \Sigma_ {\mathrm{s} \in S} \mathrm{v} _ {\mathrm{s}} \big ((\mathrm{jp} _ {\mathrm{ks}} - \mathrm{jp} _ {\mathrm{rs}}) ^ {+} \big) ^ {2} \\ & + \mathrm{w} _ {\mathrm{s}} \big ((\mathrm{jp} _ {\mathrm{rs}} - \mathrm{jp} _ {\mathrm{ks}}) ^ {+} \big) ^ {2}, \\ \mathrm{jp} _ {\mathrm{r}} & \in F _ {\mathrm{k}} \text {or} \mathrm{jp} _ {\mathrm{r}} \in P _ {\mathrm{k}}, \end{array}\tag{3}
$$

where S is the set of all the skills, and $v_{s}$ and $w_{s}$ are weights a-priori set;

step (4) the JPs still included in the two sets, before being presented to the system user, are ordered according to the number of skills of interest that they share with $jp_{k}$ ; ties are broken on the basis of distance (3). The user is then asked to make the final decision, i.e., to indicate which JPs, among the ones proposed by the system, eventually precede/follow $jp_{k}$ . At this point, $jp_{k}$ can be inserted in the JOS.

For this procedure, too, the authors' experience in test cases allow them to state that the default setting of the weights to one, both in the sum in step (2) and in the sum in step (3), is in general a good choice. It is worth noting that the skill subsets (managerial and methodological) considered in step (2) of the above procedure are the ones provided by default by ISPM, in accordance with the observations made in Section 3 on the JOS. However, the system allows one to use any skill subsets.

## 5. A numerical example

So far ISPM has been realized as a prototype by means of the HyperCard software, and the times given in the following refer to a 25 MHz Macintosh with a 68030 processor. The case considered is the one shown in Fig. 1: it involves 51 JPs and 37 TEs, described by 100 different skills.

For the case of IGSC, the system takes few seconds (< 10 s) to select the best JPs for an HR, and a little longer time (< 30 s) to insert a new JP in the JOS. A longer time is required to establish the TEs that an HR should attend. In particular, to perform all three steps necessary to solve Problem 2, it takes about 1 minute when the considered JP requires 10/15 non-zero skill levels, and about 5 minutes when the considered JP requires 70/80 non-zero skill levels.

The results obtained by ISPM were found to be coincident or equivalent with the decisions made by human experts for restructuring and training operations. In particular, ISPM was used to decide whether it was worth organizing customized training or all the HRs occupying given JPs should attend the same courses.

## 6. Conclusions

This paper has described a decision system (ISPM) which assists the user in solving personnel management problems. For each of the problems ISPM can face, the system suggests an ordered set of possible solutions on the basis of objective quantitative data. Nonetheless, since personnel management problems may also involve undefinable and non-measurable qualities of HRs, ISPM allows (and sometimes asks) the user to direct the otherwise automated decisional processes. The authors are currently exploring the possibility of system improvements. A first improvement should aim at making ISPM able to process some lexical attributes (e.g., salary, prestige, location, etc.) so that the system may also assist the user in taking into account, for instance, the disposition of an HR for a JP in the decisional processes. However, this improvement would probably require non-trivial modifications to the implemented procedures. A second possible improvement should allow the storage of historical data so that some sort of user-preference learning might be introduced into the system. Moreover, the actual effectiveness of TEs and the adequacy of the skill levels required for a JP might be a-posteriori assessed.

## References

[1] A. Ciancimino, I. Lari, F. Nicolò, and M. Lucertini, A decision support system for human resource management: Strategic and tactical planning flow network models, Proceedings: IFAC Information Control Problems in Manufacturing Technology, Toronto, Canada, pp. 421–427 (1992).

[2] P. Costantopoulos, Decision for massive personnel assignment, Decision Support Systems, 5, pp. 355–363 (1989).

[3] M.R. Garey and D.S. Johnson, Computers and Intractability (New York, W.H. Freeman and C., 1979).

[4] C. Hwang and K. Yoon, Multiattribute Decision Making (Berlin, Springer-Verlag, 1981).

[5] R.L. Leitheiser, MIS skills for the 1990s: A survey of MIS managers' perceptions, Journal of Management Information Systems, 9(1), pp. 69–91 (1992).

[6] M. Merlino, P. Castelli, and L. Lopez, Europeople —Gestire e valorizzare la risorsa umana nella prospettiva dell'unificazione europea (Il Sole 24 Ore Libri, Milan, 1992) (in Italian).

[7] M. Merlino, and M. Provedel, Piano di formazione per la direzione centrale sistemi gestionali ed informativi, Andersen Consulting Internal Report, Milan, I (1980) (in Italian).

[8] R.J. Mockler, and D.G. Dolgite, Expert systems for human resource management: Development and implementation, Proceedings: 25th Hawaii International Conference on System Sciences, 3, pp. 129–132 (1991).

[9] M. Paolucci, and R. Pesenti, Assessing a new utility/cost function for multiattribute decision making, Operations Research Letters, 12(5), pp. 331–336 (1992).

[10] W.L. Price, A. Martel, and K.A. Lewis, A review of mathematical models in human resource planning, OMEGA, 8(6), pp. 639–645 (1980).

[11] J. Silverman, R.E. Steuer, and A.W. Whisman, A multi-period, multi-criteria optimization system for manpower planning, European Journal of Operational Research, 34, pp. 160–170 (1985).

[12] G.S. Taylor, and J.P. Shim, Microcomputer-based decision support systems applied to human resource management, Collegiate Microcomputer, 8(3), pp. 183–189 (1990).

[13] W.Z. Venema, and J. Wessel, Systematic modeling and model handling for manpower planning systems, Decision Support Systems, 4, pp. 503–508 (1988).

[14] P.J. Verbeek, Decision support systems: An application in strategic manpower of airline pilots, European Journal of Operational Research, 55, pp. 368–381 (1991).

[15] B. Wild, and C. Schneeweiss, Manpower capacity planning: A hierarchical approach, International Journal of Production Economy (in press).

Michele Bellone was a graduate student in the Department of Communications, Computer, and System Sciences of the University of Genoa, where he graduated with a dissertation on Decision Support Systems for human resource management.

Massimo Merlino is an associate professor of Management Science in the Department of Communications, Computer, and System Sciences of the University of Genoa and editor of the Italian Journal of Logistics and Management. He is the author of many articles on management topics and the co-author of some management books.

Raffaele Pesenti is an assistant professor of Operations Research in the Department of Electronic Engineering and Computer Science of the University of Trieste. His research and publications are in the area of applications of Decision Support Systems to industrial environments.
