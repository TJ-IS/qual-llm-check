---
otero_id: 23206
otero_key: "FVCWG94G"
title: "An experimental investigation into the process of knowledge-based systems development"
authors: "S Lee; RM O'Keefe"
year: "1996"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.1996.29"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An experimental investigation into the process of knowledge-based systems development

S Lee $^{1}$ and RM O'Keefe $^{2}$

$^{1}$ Department of Information Systems, College of Commerce and Law, Yonsei University, Wonju, Korea; and $^{2}$ Computer Science & Information Systems, Brunel University, Uxbridge, UK

This paper presents an experimental study into the processes that may contribute to building a better knowledge-based system. A model that defines quality to be composed of two related aspects, internal and external quality, is introduced. To test the model, 24 subjects developed a knowledge-based system for MBA course planning in an experimental setting over a 7 week period. Subjects were factored by development methodology (structured vs rapid prototyping), knowledge representation scheme used (rule-based vs hybrid) and programmer quality (naive vs experienced). The major finding is that an appropriate mix of development methodology, knowledge representation and personnel is necessary. No single development methodology or knowledge representation scheme is best, and a considerable number of interactions was observed in the experiment. Rapid prototyping combined with rule-based representation produced the best external quality in terms of functionality, but when combined with hybrid representation produced the worst. Similarly, rapid prototyping combined with hybrid representation produced the worst usability. Programmer quality had a positive effect on coding productivity, which in turn resulted in an increase in system usability. As with conventional software, increasing programmer quality can be very beneficial to both process and content. The study presented provides some evidence of the anomalies that are generated in the course of system development, and how they relate to internal quality. As might be expected, experienced programmers produced significantly fewer anomalies. A relationship was found between internal quality and usability, but not functionality.

## 1 Introduction

As the technology of knowledge-based systems (KBS) has become established, much of the research surrounding KBS has moved from technological issues to methodological issues. This has been more particularly apparent in research on verification and validation (V&V) and maintenance of KBS. Early work in the computer science community focused on the development of algorithms and tools to support V&V and maintenance (for example, Jacob & Froscher, 1990; Preece, 1990), but it is now realised that the choice of various knowledge engineering (KE) methods and their interaction with a particular development methodology (DM) is perhaps even more important. Further, recent proliferation of end-user developed KBS (as seen in DuPont, which has over 1000 operational KBS and trained roughly 2000 people for KBS development), calls for KE methods which are more appropriate for development and control of small-scale, but operational KBS.

Our previous work in this area has considered these methodological issues in detail (O'Keefe et al, 1987; O'Keefe & Lee, 1990; Lee & O'Keefe, forthcoming). However, the guidelines and proposals for V&V present in that work are largely based upon an ad-hoc analysis of experience, containing anecdotes and reflections on how a certain KBS was built, which techniques were useful and so on. Empirical work is, therefore, necessary in order to provide a fuller understanding of the nature and efficacy of the methods frequently adopted in KBS development.

Our research has led us to believe that knowledge representation (KR) and DM play important roles in the quality of a KBS. KR is important because of the ease with which systems can be produced using rules; most rule-based tools will attempt to run a collection of rules in a robust fashion, even if the rules are erroneous or the output is garbage. This is in direct contrast to traditional procedural languages, where erroneous code may not even be compilable. It is thus not surprising that much research in V&V has focused on the identification and correction of the errors that can occur in rule-bases (eg, Nazarath, 1989; Preece et al, 1992).

DMs are important for two reasons. First, practice has shown that a methodology, such as prototyping can aid the production of useful, quality KBS (Jojo & O'Keefe, 1994). Second, surveys have shown that a DM can have a considerable impact on the amount of relative effort put into design, coding and V&V (O'Leary, 1991). Thus, further understanding of the effects of DMs on KBS quality is vital.

Beyond these concerns, there is simply a very limited amount of data on what helps to produce a quality KBS. There is a common sense assumption in some areas that good KE skills and productivity result in better KBS, but there is nothing but anecdotal data to support this.

The research presented in this paper was designed to examine the effects of KR and DM on KBS quality by tracing a 7-week long KBS development process in a laboratory setting. Rather than relate these to just the final content of the resulting KBS, process measures were used to help understand why the results and findings were obtained. The results show a very strong interaction between KR and DM, which shed considerable light on why choice of KR scheme is now recognised as a decision that should not be independent of other KE choices (Lee, 1993).

In the next section, we briefly review the need for empirical work in KBS development, the few relevant studies to this point in time, and relate this work to that in conventional software engineering. There follows a presentation of a model of KBS quality. The experiment is then presented, followed by results, analysis and conclusions.

## 2 A review

Traditionally, knowledge about software development has been accumulated through theoretical advances and follow-up experimentation. Brooks (1980) summarised the utilities of such experimentation, and an extensive survey of experimentation for conventional software can be found in Basili et al (1986). Some areas of KE, particularly knowledge acquisition, have been the target of many empirical studies (for example, Shephard, 1993). Here we will focus on experimentation in KBS development.

Unlike the significant empirical efforts in conventional software, until recently there have been few experimental studies in KBS development. Adelman (1989) claims that KE is a measurement problem in which there are several sources of variation: domain expert, knowledge engineers, KR schemes, knowledge acquisition method, and problem types. In addition, DM has been identified as a candidate for an additional source of variation (Lee & O'Keefe, 1996).

Previous empirical investigations in KE have focused on the characteristics of final products and performance variables (eg, run-time efficiency, accuracy, time to modify, etc) while neglecting process variables, such as development efforts and the growth and/or change rate of programmes during development (Swigger & Brazile, 1989; Nosek & Roth, 1990; Alavi & Wetherbe, 1991). Ives et al (1980) comment on the need for research on process variables which may provide answers for why and how systems perform well. Despite difficulties in controlling a lengthy development process, data for process variables can contribute to interpreting the empirical outcomes of the performance variables, as shown in the work of, for example, Boehm et al (1984) and Alavi (1984).

Swigger and Brazile (1989) examined the effectiveness of using design/structuring aids, such as an entity relationship diagram and petri-nets, to modify production systems. They found that subjects who used design aids took less time to modify their systems and suggested that conventional design aids can be utilised for KBS development. Davis (1990) conducted a laboratory experiment to evaluate the effect of modularity on the maintainability of rule-based systems. The results showed that a modular rule-based system was more effective with respect to modification time and accuracy than a non-modular version.

Nosek and Roth (1990) conducted an experiment to test the effectiveness of two KR schemes as communication tools between the domain expert and the knowledge engineer. Results showed the semantic network was significantly better with respect to the higher level tasks of comprehension and generalisation than predicate logic. At the validation stage of KBS, the semantic network has also been recommended for clarifying misunderstandings between domain experts and knowledge engineers.

Thus some conventional wisdom, such as modularity and design aids in software engineering, have been applied to KBS development and their effectiveness has been empirically tested. However, additional sources of variance, such as DMs and problem characteristics, still need to be examined to compare their relative importance. Interaction effects should be examined to provide KBS developers with more meaningful guidelines, since currently there are a wide variety of different KBS development environments that are available for a wide variety of different types of problems.

The issue of ‘process’ has been raised and tested in traditional systems development by facilitating different DMs, such as the systems development life cycle (SDLC) and rapid prototyping. For example, Boehm et al (1984) formed seven project teams (each with two or three graduate students), divided into prototyping and SDLC teams. Each team developed a system for software cost estimation. Results indicate that prototyping yielded products with roughly equivalent performance, but less code and effort. Also, prototyped products were rated higher on user-friendliness, but a little lower on functionality and robustness. SDLC teams produced more coherent programme design and, subsequently, their products were easier to integrate with existing systems. Alavi’s (1984) experiment (which is similar to Boehm et al’s (1984)) shows that prototyping tends to alleviate behavioural problems, such as communication obstacles between developers and users. The experiment suggests, however, that the developers of the prototyped products experienced more difficulty in managing and controlling the development process due to frequent changes in user requirements. Further, in the context of database systems, Alavi and Wetherbe (1991) report that a more formal prototyping that includes an entity-relationship modelling step results in more efficient data structuring than just rapid prototyping without data modelling.

Certainly, KBS DMs can vary depending on the problem type and the size of system. Current practices suggest that prototyping is the way to develop KBS, since system requirements are fuzzier and change more rapidly than with conventional software (O'Leary, 1988). However, there have been no controlled experiments that use DM as a moderating factor, as studied with conventional software, even though some researchers have begun to recognise a need for experiments in the context of KBS (Swigger & Brazile, 1989; Subramanian et al, 1992).

## 3 A research model

Traditionally, enhancement of software quality and development productivity has been viewed as a multifaceted issue (Jeffery, 1987), which should also be applied to KBS development (Adelman, 1989). However, unlike traditional software engineering, the attributes of KBS quality and their metrics have yet to be defined. Further, as reviewed in Section 2, previous laboratory experiments with KBS have not operationalised multiple factors and fail to explain the dynamics of KBS development.

It has been claimed that the high variability in performance of systems development and utility of user interfaces can be reduced by opting for the 'optimal' methods for a certain type of problem (Vessey & Galletta, 1991; Suh & Jenkins, 1992). The rationale of this research is based on the cognitive fit theory that refers to the congruence between processes (methodologies) that individuals use to solve a particular problem and specific aspects (representation) of the problem solving situation (Vessey & Galletta, 1991). The interpretation of the cognitive fit in the context of KBS development means that in order to foster KBS quality and development productivity, the system development environment, particularly KR, should be properly aligned with the DM. Hence, a research model was prepared, shown in Figure 1, for examining the interaction processes between KR and DM, as well as their effects (contents) under moderation of developers' prior experience. This model cannot be considered as a full model which includes every conceivable element affecting KBS development as noted in Jeffery (1987). But, by controlling variables, such as problem types (for a single application domain with same complexity), knowledge acquisition methods (through documents and interview), development environments (under PCs and the same tool), and domain experts (from same experts), this model is believed to meet our basic research goal: investigation of congruence of basic aspects of KBS development, relating them to measures used in previous research, and hypothesising about the effect of these on KBS quality.

In this model, there are two types of KBS quality: internal and external (explained in detail below). Based on the model developed, this research empirically tests the effectiveness of the independent variables on the dependent variables, varying the conditions (ie, DMs under different KR) in a laboratory setting.

## 3.1 Independent variables

The independent variables investigated in this research are KR type (rule-based vs hybrid), DM (rapid prototyping vs structured prototyping), and programmer quality (naive programmer vs experienced programmer).

## 3.1.1 Knowledge representation (KR) type

KR refers to the knowledge base (KB) representation into which the knowledge must be cast for it to be computationally useable. Production rules, appropriate for procedural knowledge, are easily understood by domain experts because of the uniform structure of IF–THEN statements and their naturalness (Barr & Feigenbaum, 1981). However, production rules are inadequate for describing domain objects and static relationships among objects (Fikes & Kehler, 1985).

Hybrid systems combine object-based and rule-based techniques, facilitating KR schemes which supplement the limited expressive power of production rules with frames which capture declarative knowledge in a hierarchy and provide structural semantics among objects (Fikes & Kehler, 1985). Thus, both objects and relationships, and rules for their behaviour, can be represented in a hybrid KR scheme. Relationships among objects in a domain can be shared efficiently by other frames in a class hierarchy via inheritance.

In order to facilitate the two types of KR, CLIPS version 5 (the C Language Integrated Production System), developed by NASA, was chosen for the experiment. CLIPS provides a common environment for rule-based and hybrid systems, and can be run on IBM-PC and compatible machines, with which participants were already familiar. CLIPS supports three different programming paradigms: rule-based, object-based and procedural. One can develop a KBS using only rule-based, only object-based, only procedural, or a combination of the three. It supports features such as classes with multiple inheritance, dynamic binding, abstraction, and message passing with message handlers.

## 3.1.2 Development methodology

Prototyping has received wide support from researchers and practitioners, and has been the DM of choice for KBS (Jojo & O'Keefe, 1994). This is (at least in part)

![](/api/attachments/FVCWG94G/fulltext/images/00d4cc176ac49c22d58f3c6b7ab1f90882155c207ebd41d3194c27a9d3ccb176.jpg)  
Figure 1 A model for quality of KBS.

due to the problems of acquiring knowledge from domain experts, who tend to have difficulty in expressing their knowledge in a structured way. Thus, iteratively developing the KB has been, in many cases, essential.

It has been suggested, however, that with more expressive KR schemes, and so as to plan and execute development better, a more structured approach to prototyping is required. Among different definitions or classifications, in this research, rapid prototyping and structured prototyping were operationalised (see Table 1) to investigate their advantages and drawbacks. In rapid prototyping the knowledge engineer elicits knowledge from the expert and builds it directly into the system. The expert then tries the system and points out any faults or omissions, which are then corrected. The process is repeated until the prototype reaches the desired state.

Structured prototyping involves the use of some form of intermediate representation. With this method, the prototype is built initially in the form of a 'paper model' which can be tested before proceeding to the machine based implementation. The paper model serves as a continuously updated functional specification, providing documentation during the course of the project. For larger applications with multiple experts the use of structured prototyping and intermediate representations is often essential (Long & Neale, 1993).

Table 1 Project schedule

<table><tr><td>Week</td><td>Rapid prototyping</td><td>Structured prototyping</td></tr><tr><td>1-5</td><td>Lecture/Lab Exercise</td><td>Lecture/Lab Exercise</td></tr><tr><td>6</td><td>Distribute project assignment</td><td>Distribute project assignment</td></tr><tr><td>7</td><td>Prototype 1 Demonstration with documentation</td><td>Paper Modeling with Petri-net</td></tr><tr><td>10</td><td>Prototype 2 Demonstration with documentation</td><td>Prototype 1 Demonstration with documentation</td></tr><tr><td>12</td><td>Final product with documentation</td><td>Final product with documentation</td></tr></table>

In this research, intermediate representation was operationalised by requiring a petri net during the conceptualisation stage. A petri net is an abstract, formal model of information flow (Peterson, 1981) and has been used as a KR scheme (Chen et al, 1990) and KBS verification aid (Agarwal & Tanniru, 1992). It can model the dynamic behaviour of the system and provide structural information on the system, and is thus an attractive tool for the conceptual design of KBS.

## 3.1.3 Programmer quality

Individual differences, such as cognitive style and depth of knowledge in a problem domain, have been used as an intervening variable in laboratory studies of software engineering (Brooks, 1980). Unfortunately, results of such experiments and their interpretations tend to be contradictory and lead to controversy. Major problems include: (1) difficulties in classification of difference (eg, naive vs experienced); and (2) the presence of confounding variables which suppress the effects of individual difference (eg, cognitive style).

This research uses programming experience as an independent variable for a surrogate measurement of programmers' programming quality, since much previous research (eg, Jeffery, 1987; Sackman et al, 1968) has shown its relatively strong influence on the outcomes of experiments. For example, studies of different aspects of programmer performance have found that programmer variability can be as great as 28 to 1 (Sackman et al, 1968). Even though the magnitude of difference has been controversial, differences among programmers are often of sufficient magnitude to disguise performance effects due to software practices or characteristics (Curtis, 1981; Dickey, 1981). Further, individual difference becomes more manifest in the development of smaller group projects than in the development of larger group projects (Jeffery, 1987). Since this research required individual project development, it calls for the control of programmer characteristics.

Various stratification schemes used in previous research include length of experience, number of languages known, number of programmes coded in each language, and years of education. This research includes, in addition to the above items, types of languages known as a stratification criterion.

## 3.2 Dependent variables

Figure 1 shows KBS quality to be comprised of both internal and external factors.

## 3.2.1 Internal quality

Following accepted practice in KBS V&V (O'Keefe & O'Leary, 1993), internal KBS quality can be characterised by two attributes: (1) logical consistency and completeness; and (2) modularity of the KB. Logical consistency generally refers to the KB making consistent use of the knowledge represented, and there are a number of techniques for determining whether a rule-base is consistent (eg, Preece et al, 1992). Completeness does not refer to the fact that the knowledge is complete (since this is a semantic and design issue), but generally whether or not some possible incompleteness can be observed (O'Keefe & O'Leary, 1993).

An anomaly is a potential error due to an inconsistency or incompleteness problem, and KBS V&V attempts to at least identify and document all anomalies (Preece, 1990). Logical consistency and completeness contribute to external KBS quality in the same sense that error free programmes contribute to quality with conventional software.

Modularity is not necessarily important for performance, but for updating and maintenance. It is now recognised that since many KBS are frequently updated, the ability to alter the KB easily is an important attribute of quality (Lee & O'Keefe, 1994).

Measuring internal quality is not easy – there are no accepted metrics for KBS, and no complete taxonomy of all anomalies. Further, developers will produce anomalies in the course of prototyping that disappear in subsequent prototypes due to the addition of more knowledge. In this experiment, we measure internal quality by simple identification of anomalies in the intermediate and final product. Modularity was considered in separate experiments not reported here. $^{1}$

## 3.2.2 External quality

External quality can be characterised by system functionality, usability and maintainability (O'Keefe & Lee, 1990). Functionality refers to the ability of the KBS to perform the requisite functions correctly. In this experiment, functionality was evaluated by considering the number of options that the final product provided (for example, the number of items in a main menu, the number of print formats, etc.) and the correctness (validity) and scope (blind vs customised suggestions) of the function provided.

Depending on the nature of the users (ie, expert users, naive users, developing users, etc.), usability can be defined differently. In this experiment, usability was measured by considering ease of use (Davis, 1989) from the perspective of the naive users who are knowledgeable in the problem domain, but did not participate in the development of the systems. However, items included in Davis's study (1989), such as being easy to learn, easy to become skillful, were omitted since the final products here were single-task oriented with routine operations unlike database or spreadsheet software which users may need to learn and become skillful in order to use them effectively (see Hendrickson et al, 1993). Systems with high usability should provide users with a high degree of convenience in performing desired functions (easy to use), and the avoidance of over constrained program behaviour (flexible to interact with). For example, when users are asked to choose from a list, a system which uses a 'pick list' for available options was scored higher than a system which asked users to type in a choice. In addition, systems with high usability should protect users from aborts and system crashes, and include input validation (easy to manipulate). Hence, three items for usability (easy to use, flexible to interact with, and easy to manipulate) and three items for functionality (number of options, correctness and scope of function provided) were measured in 7-point Likert scales to evaluate external quality of the final products by the two authors. Later, the scores were cross validated, with discrepancies between the two scores for any of the items discussed and a final score agreed upon.

## 3.2.3 Process measures

In addition to the content variables above, this research investigated dependent process variables. Process variables reveal the characteristics of KBS project development, while content variables reflect the characteristics of the final product under the different development environments. During the 7-week KBS development, design and coding time, code size, coding productivity, and the amount of changed code were examined as process variables. The size of the KBs were measured in terms of the number of rules, frames, and functions, as well as the total lines of code in the KB. (This is described in detail later.)

There has been a controversy over the use of lines of code (LOC) as a software productivity measure (Basili et al, 1986). This mainly arises from the differential complexity of programmes which are different in nature depending on the application domain. However, such a problem can be eliminated by controlling the complexity of the project in a laboratory setting (ie, by developing the same system under the same development environment). In this study, therefore, LOC is used as the measurement of size.

## 3.3 Research hypotheses

The research hypotheses for the independent variables can be stated as follows:

H1: Knowledge representation type (KR) does not affect KBS internal quality, KBS external quality, or process measures.

H2: Development methodology (DM) does not affect KBS internal quality, KBS external quality, or process measures.

H3: Programmer quality does not affect KBS internal quality, KBS external quality, or process measures.

H4: There is no interaction between KR, DM and programmer quality.

## 4 Experimental methodology

## 4.1 Subjects

Subjects were drawn from the student population of the graduate course Decision Support and Expert Systems, offered in the department of Decision Sciences and Engineering Systems (DSES) at Rensselaer Polytechnic Institute (RPI). This is a course available to MBA and graduate industrial engineering students specialising in information systems, and is typically taken in the last semester of study.

The class size was 27, including a student who audited the class and did not participate in this experiment. Thus this experiment began with a sample size of 26, but two participants produced unusable/incomplete products. In this study, therefore, 24 products were analysed.

## 4.2 Demographic data

Demographic data was collected at the beginning of the class and analysed (see Table 2). An analysis was conducted in order to provide background information about the sample on which the experimental results are based. The survey results indicated that students in the class possessed sufficient computer skills (eg, programming languages, database package experience, PC operating systems) to be introduced to KBS.

Among the 24 subjects who produced usable products under proper experimental control, two groups representing ‘experienced’ and ‘naive’ programmers were generated by counting the total number of programming languages, packaged software and KBS shells known to the subject. Also, performance in a KBS maintenance experiment (Lee & O'Keefe, forthcoming) was taken account to stratify two groups.

The number of programming languages used was significantly different between the resulting groups (3.8 vs 0.6; P < 0.01) while the amount of packaged software used and KBS shells used was not significantly different. A Spearman correlation test showed that there was a significant correlation between the number of programming languages used and that of shells used (P < 0.05), while there was no significant correlation between the amount of packaged software used and either programming languages or shells used.

## 4.3 Tasks

Prior to the experiment, subjects received 5 weeks of KBS development training: 15 hours of lectures (3 hours per week) and 10 hours of laboratory work (2 hours per week). Lectures covered the history of AI, KR methods, inferencing, DMs, and V&V, while in the laboratory subjects learned CLIPS. Students performed a maintenance experiment where each subject had to alter a rule-based and hybrid version of an animal classification problem (Lee & O'Keefe, 1996). Traces for the experiment allowed for a check on the skills that subjects had acquired in training. Then, as described in Section 4.2, subjects were classified into two groups (experienced and naive), and subjects in each group were randomly assigned into four cells (2 DM × 2 KR). Then, they developed a KBS as an individual project for 7 weeks.

Following the 7-week experiment, subjects then performed another maintenance experiment on a version of the 7-week experimental product (Lee, 1993). While the two maintenance experiments are not presented here, we draw on some of the results published elsewhere to address the impact of the longitudinal experiment on maintainability.

## 4.4 KBS development

Subjects developed an MBA Course Planning System which can interactively provide four semesters of course plans for new full-time MBA students at RPI. This has been a common application of KBS (Kingston, 1992). Experience from the previous use of this project in earlier offerings of the course suggested that the KB of the project consists of between 40 and 100 rules (plus domain knowledge stored as facts or objects), which appears appropriate for an experimental project, but complex enough to be non-trivial. Further, this task requires use of both classification heuristics (eg, choosing an appropriate course) and planning heuristics (eg, scheduling a course for a particular semester), and is thus appropriate for a multi-representation mixed-inference tool like CLIPS.

Table 2 Demographics of subjects

<table><tr><td>ATTRIBUTES</td><td>FREQUENCY</td><td>%</td></tr><tr><td>Sex</td><td></td><td></td></tr><tr><td>Male</td><td>19</td><td>79.2</td></tr><tr><td>Female</td><td>5</td><td>20.8</td></tr><tr><td>Major</td><td></td><td></td></tr><tr><td>MBA</td><td>14</td><td>58.3</td></tr><tr><td>MS(OR/ST)</td><td>10</td><td>41.7</td></tr><tr><td>Working experience</td><td></td><td></td></tr><tr><td>Less than 1 year</td><td>13</td><td>54.2</td></tr><tr><td>1 to 2</td><td>7</td><td>29.2</td></tr><tr><td>2 to 3</td><td>2</td><td>8.3</td></tr><tr><td>More than 3 years</td><td>2</td><td>8.3</td></tr><tr><td>Number of programming languages used</td><td></td><td></td></tr><tr><td>1</td><td>8</td><td>33.3</td></tr><tr><td>2</td><td>6</td><td>25.0</td></tr><tr><td>3</td><td>5</td><td>20.8</td></tr><tr><td>4</td><td>2</td><td>8.3</td></tr><tr><td>More than 5</td><td>3</td><td>12.5</td></tr><tr><td>Number of packaged software used</td><td></td><td></td></tr><tr><td>2</td><td>2</td><td>8.3</td></tr><tr><td>3</td><td>10</td><td>41.7</td></tr><tr><td>4</td><td>12</td><td>50.0</td></tr><tr><td>Frequency of using micro computer</td><td></td><td></td></tr><tr><td>Daily</td><td>19</td><td>79.2</td></tr><tr><td>Weekly</td><td>5</td><td>20.8</td></tr><tr><td>Competency of PC use</td><td></td><td></td></tr><tr><td>5 (Highest competency)</td><td>14</td><td>58.3</td></tr><tr><td>4</td><td>5</td><td>20.8</td></tr><tr><td>3</td><td>4</td><td>16.7</td></tr><tr><td>2</td><td>1</td><td>4.2</td></tr><tr><td>1 ((Lowest competency)</td><td>0</td><td></td></tr></table>

Descriptions of the minimum requirements for the system were handed out. In addition, the RPI graduate catalogue was used as the main source of domain knowledge, and the necessary portion of the catalogue was included in the project hand-out package. The system was not supposed to generate a blind schedule which is identical for every student. Rather, the system should incorporate the user's input, such as their preference for certain courses, as well as terms and concentrations.

In order to operationalise the difference of the two prototyping methods, the petri net, as an intermediate representation, was required for structured prototyping experimental groups as a part of documentation requirements. Those employing structured prototyping and a hybrid KR scheme also had to produce and maintain an object-hierarchy chart.

The frequency of the prototyping cycle was varied between the rapid prototyping and structured prototyping groups, as shown in Table 1. Table 3 depicts a skeleton of different experimental groups with different treatments. The authors played the role of experts and users, providing necessary feedback and rating the functionality and usability of the final products. When a problem or question was brought up by one subject, we conferred on the answer, and subsequently made the identical answer available to all subjects.

## 4.5 Design of experiment

The experiment used a 23 factorial design since interactions, which represent the proper fit of independent variables for KBS development, are of interest in this research. Also, a limited number of subjects (24) and the number of factors (more than two) leads us to opt for the factorial design over one-at-a-time experiments. The result was the following experimental model:

$$
\begin{array}{r l} \mathrm{Y(ijkl)} & = \mu + \alpha (\mathrm{i}) + \beta (\mathrm{j}) + \gamma (\mathrm{k}) + \alpha \beta (\mathrm{ij}) \\ & + \alpha \gamma (\mathrm{ik}) + \beta \gamma (\mathrm{jk}) + \alpha \beta \gamma (\mathrm{ijk}) + \epsilon (\mathrm{ijkl}) \end{array}
$$

where:

Y(ijkl) is the value of the performance measure, $\mu$ is a constant,

$\alpha (\mathbf{i})$ is the effect of the ith knowledge representation type $(\mathrm{i} = 1,2)$ ,

$\beta (\mathbf{j})$ is the effect of the jth development method type $(\mathrm{j} = 1,2)$ ,

Table 3 Treatments

<table><tr><td rowspan="2">Development Tool</td><td colspan="4">Development methodology</td></tr><tr><td>Rapid prototyping Experience Experienced</td><td>Naive</td><td>Structured prototyping Experience Experienced</td><td>Naive</td></tr><tr><td>Production Hybrid</td><td>Group 1 Group 5</td><td>Group 2 Group 6</td><td>Group 3 Group 7</td><td>Group 4 Group 8</td></tr></table>

$\gamma (\mathbf{k})$ is the effect of the kth programmer quality level $(\mathbf{k} = 1,2)$ ,

$\alpha\beta(ij)$ is the interaction of the ith knowledge representation type and the jth development method type, αγ(ik) is the interaction of the ith knowledge representation type and the kth programmer quality level,

$\beta\gamma(\mathrm{jk})$ is the interaction of the jth development method type and the kth programmer quality level,

$\alpha\beta\gamma$ (ijk) is the interaction of the ith knowledge representation type, the jth development method type, and the kth programmer quality level, and $\epsilon(\text{ijkl})$ is the experimental error term.

As an example, Y(ijkl) might be a measurement of coding productivity for one observation on a naive or experienced subject given the treatment using rule-based knowledge representation and rapid prototyping.

## 4.6 Data collection

Internal quality data was collected by analysing the 24 final products, as discussed above. Functionality and usability was measured on a 7-point Lickert scale, where each of the authors evaluated each of the 24 products individually, and then met to agree upon final scores.

For the process data, time measurements were self reported by subjects on a time sheet which had been distributed at the beginning of the project. Copies were collected every 2 weeks during the project. The size of prototypes in lines of code (LOC) and the number of lines of code changed between prototypes (CLOC) was measured from the submitted programs. Coding productivity was calculated by dividing LOC by reported time measures.

## 5 Results and analysis

Based on the Shapiro-Wilk statistic, W, all of the outcome data are considered normally distributed at the 0.05 confidence level. The scales developed for coding productivity, project development productivity, the number of errors, usability, and functionality were incorporated in a MANOVA with the three independent variables (KR, DM, and programmer quality). This analysis identified a significant two-way interaction between KR and DM (Wilks' lambda = 0.445, F(5,12) = 2.99, P = 0.056), a programmer quality main effect (Wilks' lambda = 0.221, F(5,12) = 8.43, P < 0.01), and a DM main effect (Wilks' lambda = 0.357, F(5,12) = 4.33, P < 0.05).

Next, the univariate ANOVAs and planned comparisons (using the Duncan Multiple Range Test) among individual cell means were examined to assess the hypotheses. The individual treatment means are summarised in Table 4, and the nature of interactions between independent variables are shown in Figures 2(a)–(g).

## 5.1 Process variables

## 5.1.1 Product size

The size of the final products was compared in terms of total LOC, excluding comment lines. Analysis of variance showed that there was a statistically significant difference between the two different KR schemes in terms of the total LOC (F(1,16) = 6.86, P < 0.05). The average size of the hybrid version (467 lines) was greater than that of the rule-based version (351 lines). (This result is consistent with the outcomes of Henry and Humphrey's (1990) experiment in which they compared the size, using LOC, of C and C++ programmes.)

The hybrid version requires more code for static knowledge represented with frames than the rule-based version, where the facts can be represented in a simpler form. There was no significant difference in product size when the procedural part (ie, rules and functions) of the two systems was compared without the declarative knowledge (ie, the initial facts in the rule-based version and the frames in the object-based version).

Conversely, DMs had no effect on size. This result is not consistent with that of Boehm's study in which prototyping and SDLC were operationalised as independent variables. Even though structured prototyping in this study can be viewed as 'in-between' rapid prototyping and SDLC, the average size of products developed by rapid prototyping (417 lines) was larger than that (401 lines) of products developed by structured prototyping. Such an inconsistent finding can be attributed to the different types of prototyping. Boehm et al's (1984) experimental system required participants to put a large portion of development efforts into the design of user interfaces, rather than constructing procedural components which utilise domain knowledge. On the other hand, in this study, functional prototyping was the primary task.

Table 4 Summary of treatment means for dependent measures

<table><tr><td rowspan="2"></td><td colspan="2">Rapid Prototyping</td><td colspan="2">Structured Prototyping</td><td rowspan="2"></td></tr><tr><td>Experienced</td><td>Naive</td><td>Experienced</td><td>Naive</td></tr><tr><td colspan="6">Coding Time</td></tr><tr><td>Production</td><td> $28.0 (6.0)^a$ </td><td>42.3 (3.3)</td><td>28.2 (8.6)</td><td>44.0 (3.5)</td><td></td></tr><tr><td>Hybrid</td><td>45.7 (7.1)</td><td>60.3 (7.5)</td><td>39.5 (4.8)</td><td>42.3 (4.5)</td><td> $41.3 (11.0)^b$ </td></tr><tr><td colspan="6">Design Time</td></tr><tr><td>Production</td><td>4.2 (1.6)</td><td>5.8 (2.0)</td><td>7.8 (1.0)</td><td>10.7 (1.5)</td><td></td></tr><tr><td>Hybrid</td><td>5.5 (1.8)</td><td>6.8 (1.6)</td><td>14.8 (3.5)</td><td>11.2 (2.8)</td><td>8.4 (3.9)</td></tr><tr><td colspan="6">Total Development</td></tr><tr><td>Production</td><td>32.2 (4.5)</td><td>48.2 (3.2)</td><td>36.0 (7.6)</td><td>54.7 (4.0)</td><td></td></tr><tr><td>Hybrid</td><td>51.2 (9.0)</td><td>67.2 (9.0)</td><td>54.3 (2.5)</td><td>53.5 (7.3)</td><td>49.6 (11.9)</td></tr><tr><td colspan="6">Coding Productivity</td></tr><tr><td>Production</td><td>12.6 (1.9)</td><td>8.6 (1.2)</td><td>12.8 (1.1)</td><td>7.5 (1.3)</td><td></td></tr><tr><td>Hybrid</td><td>10.5 (1.8)</td><td>7.4 (1.4)</td><td>14.4 (1.4)</td><td>8.7 (3.6)</td><td>10.3 (3.0)</td></tr><tr><td colspan="6">Project Productivity</td></tr><tr><td>Production</td><td>11.0 (2.5)</td><td>7.5 (0.7)</td><td>9.8 (0.6)</td><td>6.0 (1.0)</td><td></td></tr><tr><td>Hybrid</td><td>9.4 (1.4)</td><td>6.7 (1.3)</td><td>10.4 (1.2)</td><td>6.9 (3.0)</td><td>8.5 (7.3)</td></tr><tr><td colspan="6">Changed LOC between Prototype 1 and 2</td></tr><tr><td>Production</td><td>166.0 (81.5)</td><td>174.0 (122.3)</td><td>174.0 (59.4)</td><td>136.7 (42.0)</td><td></td></tr><tr><td>Hybrid</td><td>304.0 (138.1)</td><td>239.7 (78.1)</td><td>348.3 (27.3)</td><td>169.31 (110.8)</td><td>214.0 (104.5)</td></tr><tr><td colspan="6">Changed LOC between Prototype 1 and 2</td></tr><tr><td>Production</td><td>252.3 (76.6)</td><td>298.3 (44.1)</td><td>174.0 (59.4)</td><td>136.7 (42.0)</td><td></td></tr><tr><td>Hybrid</td><td>342.7 (130.7)</td><td>312.7 (87.3)</td><td>348.3 (27.3)</td><td>169.31 (110.8)</td><td>254.3 (104.3)</td></tr><tr><td colspan="6">Errors in Final Product</td></tr><tr><td>Production</td><td>1.33 (2.31)</td><td>2.67 (2.52)</td><td>0.67 (1.16)</td><td>3.00 (2.00)</td><td></td></tr><tr><td>Hybrid</td><td>0.67 (0.58)</td><td>2.33 (1.16)</td><td>0.67 (0.58)</td><td>1.67 (2.08)</td><td>1.63 (1.69)</td></tr><tr><td colspan="6">Usability</td></tr><tr><td>Production</td><td>6.0 (1.0)</td><td>5.0 (1.0)</td><td>4.3 (0.6)</td><td>2.3 (0.6)</td><td></td></tr><tr><td>Hybrid</td><td>5.7 (0.6)</td><td>4.0 (1.0)</td><td>6.0 (1.0)</td><td>3.7 (1.2)</td><td>4.6 (1.4)</td></tr><tr><td colspan="6">Functionality</td></tr><tr><td>Production</td><td>5.3 (1.2)</td><td>5.7 (0.6)</td><td>3.7 (1.2)</td><td>3.0 (1.0)</td><td></td></tr><tr><td>Hybrid</td><td>5.3 (1.5)</td><td>5.0 (1.0)</td><td>6.3 (0.6)</td><td>5.3 (1.5)</td><td>5.0 (1.4)</td></tr></table>

$^{a}$ Standard deviations are in parentheses.  
$^{b}$ Overall mean for each dependent measure.

## 5.1.2 Design time

As described above, the structured prototyping group was required to generate a paper model with a petri-net for rule-based systems and to generate an object-hierarchy chart and a petri-net for hybrid systems. Analysis of variance showed that DM had a significant effect on design activity and time $(F(1,16)=40.29, P<0.01)$ .

It is natural that the structured prototyping group spent more time on the design phase (11.13 h) than the rapid prototyping group (5.58 h), since the first group was forced to develop a paper model before they actually developed the product. In addition, KR schemes significantly affected design time $(F(1,16)=36.26, P_{c}<0.05)$ : the hybrid platform required more design time (9.6 h) than the rule-based one (7.1 h). This difference can be attributed to the overhead of identifying necessary objects, developing their hierarchical structures, and preparing necessary slots for each object.

The interaction between programmer quality and KR was significant for design time $(F(1,16)=3.83, P<0.1)$ and the nature of this interaction is shown in Figure 2(a). More experienced participants tended to spend more design time on hybrid systems than on rule-based systems.

## 5.1.3 Coding time

ANOVA showed that programmer quality (F(1,16) = 24.09, P < 0.01), KR (F(1,16) = 21.79, P < 0.01), and DM (F(1,16) = 5.29, P < 0.05) have significant effects on the coding time:

![](/api/attachments/FVCWG94G/fulltext/images/524cb21412cfa5dc1c87247041795ed540dc295ecc4a3a50fa2e4690e4edf3bf.jpg)

![](/api/attachments/FVCWG94G/fulltext/images/f8ae765ea89dc4cbacc8acd13e7e93ad0b99b68b2405f8d4b589ad110f71d24f.jpg)

![](/api/attachments/FVCWG94G/fulltext/images/466a185d7cd74878fc595f46ea8748c7501ab5b0592049904eb6a5681a19a99a.jpg)

![](/api/attachments/FVCWG94G/fulltext/images/b8a9ab549eb554890a28ab65b6a49dc1fa74cf2329357d000521239c8d6d2b35.jpg)

![](/api/attachments/FVCWG94G/fulltext/images/11829d02c5091984ec9a4d659da82679a23d03fa686cd8ced43006e52c761198.jpg)

![](/api/attachments/FVCWG94G/fulltext/images/f14b7f5760563f47500d7133a91f796d7c31e7f36d2d67f5dae0ddb6437089cf.jpg)

![](/api/attachments/FVCWG94G/fulltext/images/0bdd5ce4ceea1c0af463c2a94d22e8ff1ef2beac0c5c755afad3516d3b3b46ea.jpg)  
(g)  
Figure 2 Plots for the interaction among the independent variables. Interaction effect on: (a) design time; (b) coding time; (c) coding productivity; (d) project development time; (e) project development time; (f) functionality; and (g) usability.

(1) Experienced programmers spent less time to code (35.3 h) than naive programmers (47.3 h).

(2) Rule-based systems required less time to code (35.6 h) than hybrid systems (47.0 h).

(3) Experienced programmers spent less coding time on the rule-based systems (28.1 h) than on the hybrid systems (42.6 h).

On the other hand, there was no significant difference in coding time between the two versions (rule-based (43.2 h) and hybrid (51.3 h)).

As described above, programming experience was categorised into two groups based primarily on the number of programming languages known. Previous exposure to procedural languages, such as C and Pascal, tended to help participants more quickly learn a KBS shell like CLIPS. Production rules are, at least on the surface, similar to the IF–THEN structure in conventional procedural languages. This is in contrast to object-based systems which required participants to understand different programming concepts, such as default reasoning and message passing among the objects. This result indicates that the carry-over learning effects from conventional procedural languages to rule-based systems were significant for experienced programmers, even though there are differences in the underlying programming concepts between the two.

As another significant main effect, the rapid prototyping group spent more time coding (44.1 h) than the structured prototyping group (38.5 h) (F(1,16) = 5.29, P < 0.05). There may be a couple of reasons for this. First, according to the project schedule, the rapid prototyping group who did not go through formal petri-net modelling could have an extra programming week. Second, the rapid prototyping group spent more time on testing, and experienced more changes during prototyping than the structured prototyping group (this is discussed later).

The interaction between KR and DM was significant for the coding time $(F(1,16)=7.17, P<0.05)$ as shown in Figure 2(b). For hybrid systems, the structured prototyping group spent less time coding (40.9 h) than the rapid prototyping group (53.0 h), while there was no difference (35.2 h for rapid vs 36.1 h for structured) in the case of rule-based systems. This indicates that the problem structuring through paper modelling (ie, petri-net modelling) was less effective than the trial-and-error approach for development of the small size rule-based systems since even one misformulated rule tends to cause enormous side effects on other chained rules. For the hybrid systems, which inherently require structured objects, the practice of paper modelling provides developers with an understanding of relations (property inheritance) among the objects and subsequent functional attachments (methods) to the objects.

## 5.1.4 Coding productivity

ANOVA confirmed that coding productivity was a function of programmer quality (F(1,16) = 33.51, P < 0.01).

The carry-over learning effects were also applicable to higher coding productivity for experienced programmers. This finding is consistent with previous research (Sackman et al, 1968; Jeffery, 1987). The interaction between KR and DM was significant (F(1,16) = 3.72, P < 0.1) for coding productivity, and the nature of this interaction can be seen in Figure 2(c).

For rule-based systems, DM had no effect on coding productivity. On the other hand, it had a significant effect on coding productivity in the case of hybrid systems (P < 0.05). For rule-based systems, paper modelling was not effective for consistent addition of rules to the existing rule base; rather, the side effects of rule changes tended to make rule bases unstable and soon made petrinet modelling obsolete. For hybrid systems, on the other hand, structured prototyping was more productive than rapid prototyping.

## 5.1.5 Total development time

ANOVA showed a main effect for KR (F(1,16) = 28.20, P < 0.01) and programmer quality (F(1,16) = 23.01, P < 0.01):

(1) Hybrid systems required more time (55.5 h) than rule-based system (42.8 h).

(2) More experienced programmers spent less time (43.4 h) than naive programmers (55.9 h)

Unexpectedly, DM did not show a significant effect on the total development time. In fact, the rapid prototyping group spent almost the same amount of time (49.6 h) as the structured prototyping group (49.7 h). As shown above, structured prototyping required a longer design time and a shorter coding time than the rapid prototyping; hence, the difference in the total development time was off-set.

As indicated in Figures 2(d) and (e), however, total development time is dependent on the two-way interactions between KR and DM (P < 0.1), between KR and programmer quality (P < 0.1), and the three-way interaction (P < 0.1). Such interaction effects indicate that a proper alignment of these can significantly reduce project development time. With rapid prototyping, for example, experienced programmers spent significantly less time (32.2 h) developing rule-based systems, compared with naive programmers and hybrid systems (67.2 h).

The results of project productivity were similar to coding productivity: programmer quality again dominated project productivity (P < 0.01).

5.1.6 Changed lines of codes between prototype 1 and 2 For 2 weeks, rules, objects, and/or functions were deleted/added/changed between prototype 1 and prototype 2. The data for the CLOC between prototype 1 and prototype 2 were collected from the programme listing of the prototypes. CLOC indicates the net difference between the size of prototype 1 and prototype 2, rather than reflecting the change process (ie, delete, add, or modify). ANOVA revealed that there was a significant difference in CLOC depending on KR (F(1,16) = 7.78, P < 0.05) and programmer quality (F(1,16) = 3.43, P < 0.1):

(1) The size of hybrid systems grew more rapidly (265 LOC) than that of the rule-based systems (163 LOC).

(2) Experienced programmers tended to add rules and functions more consistently (248 LOC) than their counterparts (180 LOC).

In order to examine the change process, the change activities between prototypes were compiled and summarised for each subject. Rule-based systems experienced more frequent delete/add/modify processes than hybrid systems. This indicates that hybrid systems tend to grow more steadily and consistently than rule-based systems. The primary reason for high volatility between prototyping in rule-based systems was unexpected side effects primarily due to the invisible conflict resolution process. The conflict resolution strategy is not easily tractable, even though CLIPS allows users to set different types of strategies, such as depth-first, breadth-first, and simplicity strategy. Therefore, the condition statements for controlling the order of rule-firing (ie, declaration of salience value) and for forward-chaining made rules more complex. This had an effect on internal quality (see Section 5.4).

## 5.1.7 Changed lines of codes between prototype 1 and final product

As described above, the rapid prototyping group went through two prototyping processes, where the structured prototyping group produced only one prototype before the final product. As shown in Figure 3, the size of the prototype rapidly increased between the first and second prototype, but afterwards the prototyping activities stabilised and led the second prototype toward the final product with relatively few changes.

![](/api/attachments/FVCWG94G/fulltext/images/eb7935baa2293d8c363b0fad3c2be9ac5290eafc60de581d63e7c6a21172cc3b.jpg)  
Figure 3 The size growth pattern of prototypes.

KR (F(1,16) = 5.73, P < 0.05) and DM (F(1,16) = 8.42, P < 0.05) had significant effects on the total CLOC. The representational effect on the size growth between prototype 1 and the final product was similar to the result of the size growth between prototypes 1 and 2, as discussed in the previous section. In addition, DM was a factor for explaining the different pattern of size growth. This result indicates that the rapid prototyping group (which showed the longer coding time) experienced more changes (302 LOC) during the prototyping than the structured prototyping group (207 LOC). The steeper slope of size growth, as shown in Figure 4, indicates that the rapid prototyping group used their first prototype, which could handle the course planning for the first semester, as a modelling exercise which expedited the development of the second prototype.

## 5.2 Content variables

## 5.2.1 Internal quality

Internal quality was measured by counting the number of errors in the final products. KR was dropped from the ANOVA model since the category and characteristics of errors for rule-based systems are substantially different from hybrid systems; hence, its comparison was not meaningful. In this analysis, programmer quality had significant effects on internal quality (F(1,20) = 6.0, P < 0.01). ‘Experienced’ programmers committed less errors on average than ‘naive’ programmers (0.83 vs 2.42). No DM main effect or interaction effects were found.

Intermediate prototypes were also examined to see what kind of errors were persistent at each stage of development. For rule-based systems, in the first prototypes, the most frequently observed errors were completeness-related ones: undefined and/or unreferenced attribute values (all 12 products). $^{2}$ In the second prototypes $^{3}$ primary errors were rule control-related ones: mismanipulation of salience values (four errors), and/or unretracted unnecessary patterns (control knowledge) (nine errors). Three products still had undefined and unreferenced attributes, but only one product showed rule conflicts, and developers tended to struggle with controlling rules, rather than formulating consistent rules. In the final products the most persistent errors were redundancy-related errors: redundant rules (duplicated rules: two errors; chained redundant rules: one error), and subsumed rules (five errors). Also, dead-end IF conditions (five errors) and unretracted patterns (seven errors) persisted as by-products of modification of rules.

![](/api/attachments/FVCWG94G/fulltext/images/b084a468560215aa57803bf1787ea64544e1ab8548d8c398d546ad5236047795.jpg)  
Figure 4 The size growth pattern of prototypes.

Excessive use of salience values was found in two products which sequenced all scheduling knowledge with different salience values. (Salience is a mechanism whereby a certain weight is given to each rule, and then conflict resolution among rules is performed by firing the rule with the highest salience value.) The nature of the application, in particular, required that subjects should be able to know the order of rule-firing. For example, the rules in the prototype which scheduled the courses for the first semester may not be fired before the rules are added for the second semester scheduling, depending on the conflict resolution strategy chosen or the salience values assigned to the rules. This increased complexity sometimes resulted in redundant or unnecessary IF conditions which in turn led to rule subsumptions. Whenever a certain rule is misformulated, therefore, the complexity for modification increased and developers tended to delete a set of chained rules and redevelop a new set of rules, rather than modify a subset of chained rules.

For hybrid systems, in the first prototypes the most frequently observed errors were again completeness-related ones: misclassification of class (four products) and missing slots (eight errors). Subsequently, query functions for retrieving specific instances were problematic (nine errors). In the second prototypes incomplete object definition significantly improved, but the prototypes showed faulty message passing (eight errors) for filling slot values and query functions (four errors). Developers began to formulate procedural rules and tended to have difficulties in integrating them with object structures. Since CLIPS does not allow Boolean functions in the left-hand side of rules, developers misused conditional constructs, as well as other predefined CLIPS functions, in the right-hand side of rules, and it made each rule similar to a group of conventional conditional constructs (four errors). This was a violation of the basic rationale for hybrid systems in which rules can be utilised for procedural knowledge and object structures for static knowledge. The number of such nested conditional constructs increased in the final products (eight errors).

Overall, the primary errors during prototyping were undefined and unreferenced attributes, rule subsumption, mismanipulation of salience value, retention of unnecessary facts and dead-end IF conditions, missing slots, misclassification of objects, and misuse of message passing, query functions, and nested conditional construct. As expected, there was a significant difference in the total number of errors found in the final products between experienced and naive programmers (10 vs 23). However, there was no significant effect of DM on internal quality, but the characteristics of errors were different in each stage of prototyping. At the early prototyping stage, completeness-related errors, particularly missing static knowledge, were commonly committed. At the later stage, on the other hand, logical consistency of procedural (problem-solving/strategic) knowledge was problematic. Redundant rules, subsumed rules, and procedural incompleteness, such as dead-end IF conditions, were persistent during prototyping and were found more frequently in the final products than other errors. For hybrid systems, experienced subjects had less problems with message passing and query functions than naive ones, but nested conditional constructs in the right-hand side of rules were commonly found in both groups.

## 5.2.2 Functionality

ANOVA revealed that KR had a significant effect on functionality (F(1,16) = 5.64, P < 0.05), and that the interaction effect between KR and DM was significant (F(1,16) = 9.63, P < 0.01). Compared to the rule-based use of CLIPS, hybrid use tended to provide more procedural capabilities for manipulating various options (ie, the number of concentration areas) and more declarative power for controlling the static component of the KB, such as a class hierarchy. For example, message passing and encapsulation of object properties in the objects were more natural for the application than the strict pattern matching used in rule-based systems. In addition, Figure 2(f) shows the nature of the interaction effect between KR and DMs. Rapid prototyping generated more functional products for rule-based systems, while structured prototyping generated more functional products for hybrid systems.

Surprisingly, programmer quality was not found to be significant. At the beginning of development, the scope of the project was open-ended and the project assignment just described minimum requirements of the system. Post-experiment interviews revealed that participants tended to complete the project requirements which would be enough for the project grade, rather than developing systems that exceeded requirements, and allocated their extra time to other courses.

## 5.2.3 Usability

ANOVA showed that the main effects of programmer quality (F(1,16) = 23.21, P < 0.01) and DMs (F(1,16) = 8.89, P < 0.01) significantly affected the usability of systems. Unlike functionality, with the similar set of functionality as described in the previous section, more experienced participants tended to produce more usable products. It can be postulated that within the limited time-frame more experienced participants who met the functional requirements of the systems were able to further refine user interfaces. Also, rapid prototyping generated more usable systems than structured prototyping, probably because it required more frequent contacts with the experts.

Again, there was a significant interaction between DMs and KR (F(1,16) = 8.89, P < 0.01) and Figure 2(g) shows the nature of the interaction. Rapid prototyping generated more usable rule-based systems, but DMs did not affect the usability of hybrid systems.

## 5.3 Relationship between productivity and external quality

The Spearman rank correlation procedure was used to determine whether there is evidence of a significant association between coding/project productivity and external product quality. Table 5 shows correlation coefficients and probabilities. At the level of significance of 0.05, there was no evidence of a positive correlation between coding/project productivity and functionality. However, there was a positive association between usability and functionality (P < 0.01), and between coding/project productivity and usability (P < 0.05). This indicates that developers who met the minimum systems functionality tended to improve usability, rather than add more functions, and high productivity did not necessarily lead to a more functional KBS product.

## 5.4 Relationship between internal and external quality

There was a significant positive correlation between internal quality and usability (P < 0.01), but not between internal quality and functionality. The most persistent errors in rule-based systems, such as simply duplicated rules and subsumed rules, and dead-end IF conditions had little impact on functionality. However, conflicting rules and unretracted patterns which caused circular inference were detrimental to external quality. In hybrid systems missing slots and faulty message passing had a negative effect on external quality, but the most frequent errors (such as nested conditional constructs) did not. Latent errors, both in the rule-based and hybrid systems, seemingly unharmful to functionality, can significantly reduce run time performance and maintainability.

## 6 Summary of findings

The primary question of interest addressed by this study is: do KBS DMs and KR affect the KBS development process, and do the different processes, in turn, affect the quality of the final product?

## 6.1 Knowledge representation (KR)

Returning to Hypothesis H1 and summarising, the KR scheme played a significant role in determining the process variables, and had some effect on the external quality measure of functionality.

The KR scheme was a significant factor for explaining the differential effect on the final product size and design efforts. Even for the small scale hybrid system developed in this study, a significant initial overhead cost was incurred in identifying objects and their relationships. However, such front-end analysis and design, which the object-based part of the system inherently required, contributed to the incremental development of the system, rather than frequent change during prototyping.

LOC for the object representation tended to inflate the size of the final product. For example, the LOC for representing the object structures were comprised of, on average, 22% of the total LOC. In addition, the hybrid use of CLIPS required users to use more primitive and complex commands, such as traditional loop structures. Subsequently, the size of hybrid systems was larger, and the required coding time was longer than those for rule-based systems. Therefore, any expected productivity gain, acquired solely through the hybrid design, was nullified by the time required for identifying and designing object structures during the initial project development.

Table 5 Spearman correlation coefficients

<table><tr><td></td><td>CPH</td><td>PPH</td><td>USE</td><td>FUN</td></tr><tr><td>CPH</td><td>1.00000</td><td>0.94412**</td><td>0.50604*</td><td>0.21408</td></tr><tr><td>PPH</td><td>0.94412</td><td>1.00000</td><td>0.59596</td><td>0.36485</td></tr><tr><td>USE</td><td>0.50604</td><td>0.59596</td><td>1.00000</td><td>0.64223**</td></tr><tr><td>FUN</td><td>0.21408</td><td>0.36485</td><td>0.64223</td><td>1.00000</td></tr></table>

CPH: Coding productivity per hour; PPH: Project productivity per hour; USE: Usability; FUN: Functionality.  
\* $P <   0.05$  
\*\* $P <   0.01$

As suggested in the literature of object-oriented systems development (eg, Booch, 1994), however, the hybrid approach might provide an advantage in terms of code reuse and maintainability. In the first maintenance experiment undertaken by the subjects identified here and published in Lee and O'Keefe (1996), the hybrid system proved marginally easier to maintain in terms of both time to make changes and accuracy of changes. However, the second maintenance experiment performed after the 7 week experiment found no such difference.

## 6.2 Development methodology (DM)

Returning to Hypothesis H2, the DM had some effect on the process variables, such as design time and total changed LOC. The CLOC data indicated that under the same requirements, rule-based systems experienced more frequent changes between prototyping than hybrid systems.

More interestingly, the data show significant interaction effects with KR schemes on coding productivity, productivity, functionality and usability. These would seem to suggest that there is an advantage to having proper KBS development environments, depending on KR schemes and DM. Structured prototyping with hybrid systems was more productive in terms of coding, and it generated more functional products (see Figures 2(c) and (f)). However, rapid prototyping with rule-based systems generated the most usable systems, while rapid prototyping with hybrid systems generated the least usable systems (see Figure 2(g)).

This suggests that rapid prototyping is not universally applicable and effective in KBS development. This argument can be augmented by the results of Alavi and Wetherbe's (1991) study, discussed earlier, which showed that a combined approach generated more efficient systems with fewer iterations than prototyping alone.

## 6.3 Programmer quality

Returning to Hypothesis H3, programmer quality had a considerable effect on process variables and productivity, and on the external quality measure of usability.

The data suggest that background variables, such as the number of procedural languages known, may predict programmer coding and project productivity in KBS development. Similarly, the number of programming languages known and number of programmes written have been a predictor of maintenance performance for conventional programs (Boehm-Davis et al, 1992). However, previous knowledge in conventional programming tends to show a differential effect on design and project development time, depending on KR. The impact of programmer quality on the design and the project development time was much greater for rule-based than for hybrid systems. This indicates that experience in writing conventional programmes is more adaptable (transferable) to the development of rule-based systems. This might be because the mental image of the conditional construct in conventional programming is much more similar to production rules than message passing procedures in hybrid systems.

In addition to higher coding and project productivity, more experienced subjects produced more usable systems for a given set of functions, but in this experiment, at least, systems functionality tended mostly to be determined by the KR schemes. However, if there are additional motivational factors for developing more functional systems, the results might be different.

## 7 Limitations

Prior to drawing some conclusions, some cautionary notes are necessary. These relate to generalisation of the results beyond the subjects and the task used.

In any laboratory study, the use of students as subjects is a limitation to generalisability. However, for the tasks involved in the study, these graduate students are not likely to be very different from those using KBS tools to build simple, standalone systems. For example, compared to the ad-hoc KBS developers at DuPont (HBS, 1990), subjects in this experiment had, at least, the equivalent training time for KBS development (3 hours lecture and 2 hours laboratory per week for 7 weeks here vs 4 days and 3 hours for DuPont).

The projects are also a limitation, in that their size is relatively small compared to those developed in industry. It would be more desirable to use larger projects equivalent to the industry average. However, the experimental projects are complex enough for subjects to commit logical errors and for the various KB's to be different structurally. To some extent, this size limitation is compensated for by the short project schedule (7 weeks).

In establishing the experimental task, system requirements were developed and distributed. Thus the results here are probably more generalisable to systems that have meetable requirements, as opposed to open-ended development. Since even relatively small systems increasingly have some level of defined requirements (Jojo & O'Keefe, 1994), this probably reflects current practice.

## 8 Conclusions

The major finding of this study is that KBS quality is a multifaceted problem, and that an appropriate mix of DM, KR and personnel is necessary. To suggest that rapid prototyping is the most appropriate DM, or that all developed systems should use more advanced hybrid representation methods, is naive. Rapid prototyping combined with rule-based KR produced the best external quality in terms of functionality, but when combined with hybrid KR produced the worst. Similarly, rapid prototyping combined with hybrid KR produced the worst usability. The combination of structured prototyping and hybrid KR appears to be more robust, producing good (but not the best) functionality and usability. Those doing (or managing) development are advised to make combined choices of DM and KR.

A second finding relates to the effects of programmer quality. This had a positive effect on coding productivity, which in turn resulted in an increase in system usability. Functionality appears to have been constrained by the system requirements, where requirements were considered as something to be met, not exceeded. As with conventional software, increasing programmer quality can be very beneficial to both process and content.

Thirdly, this study has provided some evidence of the anomalies that are generated in the course of system development, and how they relate to internal quality. As might be expected, experienced programmers produced significantly fewer anomalies. More interestingly, a relationship was found between internal quality and usability, not functionality. Previous papers (eg, Preece, 1990) have assumed that anomalies have a primary impact on functionality.

There are three future research areas that need to be investigated. First, since V&V research has focused so much on tools that detect anomalies, it would be useful to measure the impact on quality of using a V&V tool in the development process. The study here suggests that the presence of such a tool may not be very useful for experienced programmers. Second, different studies need to be designed around other problem types. The task here involved both classification and planning heuristics; it may be that results vary depending upon problem type. Third, KE metrics for consistency and complexity, similar to conventional complexity measures, are urgently needed to benchmark and compare the internal quality of KBS developed under different environments.

## Notes

1 Lee and O'Keefe (1996) conducted two maintenance experiments (one for a classification and the other for a planning problem). Results showed that an object-based system, compared to a structured rule-based system, was easier to maintain in terms of the time to do the maintenance tasks in the case of a classification problem, but there were no significant differences in a planning problem (course scheduling system).

2 The degree of completeness is relative to the intended functionality. At the early stage of prototyping all products were in a trial stage with limited knowledge.

3 The prototypes produced by the structured group were compared with the second prototypes produced by the rapid prototyping group.

## References

ADELMAN L (1989) Measurement issues in knowledge engineering. IEEE Transactions on Systems, Man, and Cybernetics 19(3), 483–488.

AGARWAL R and TANNIRU M (1992) A Petri-net approach for verifying the integrity of production systems. International Journal of Man-Machine Studies 26, 447–468.

ALAVI M (1984) An assessment of the prototyping approach to information systems development. Communications of the ACM 27, 556–563.

ALAVI M and WETHERBE JC (1991) Mixing prototyping and data modelling for information system design. IEEE Software 8, 86–91.

BARR A and FEIGENBAUM EA (Eds) (1981) The Handbook of Artificial Intelligence. William Kaufmann, Los Altos, CA.

BASIL VR, SELBY RW AND HUTCHENS DH (1986) Experimentation in software engineering. IEEE Transactions on Software Engineering 12(7), 733–743.

BOEHM BW, GRAY TE and SEEWALDT T (1984) Prototyping versus specifying: a multiproject experiment. IEEE Transactions on Software Engineering 10(3), 290–303.

BOEHM-DAVIS DA, HOLT RW and SCHULTZ AC (1992) The role of program structure in software maintenance. International Journal of Man-Machine Studies 36, 21–63.

BOOCH G (1994) Object-Oriented Analysis and Design with Applications. The Benjamin/Cummings, Redwood City, CA.

BROOKS RE (1980) Studying programmer behavior experimentally: the problems of proper methodology. Communications of The ACM 23(4), 207–214.

CHEN S, KE J and CHANG J (1990) Knowledge representation using fuzzy Petri nets. IEEE Transactions on Knowledge and Data Engineering 2(3), 311–319.

CURTIS B (1981) Substantiating programmer variability. Proceedings of The IEEE 69(7), 846.

DAVIS FD (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly September, 319–340.

DAVIS JS (1990) Effect of modularity on maintainability of rule-based systems. International Journal of Man-Machine Studies 32, 439–447.

DICKEY TE (1981) Programmer variability. Proceedings of The IEEE 69(7), 844–845.

FIKES R and KEHLER T (1985) The role of frame-based representation in reasoning. Communications of the ACM 28(9), 904–920.

HBS (1990) Du Pont's artificial intelligence implementation strategy. Harvard Business School Case 9–189–036.

HENDRICKSON AR, MASSEY PD and CRONAN TP (1993) On the test-retest reliability of perceived usefulness and perceived ease of use scale. MIS Quarterly, June, 227–230.

HENRY SM and HUMPHREY M (1990) A controlled experiment to evaluate maintainability of object-oriented software. In Proceedings of IEEE Conference on Software Maintenance, pp 285–265, IEEE Computer Society Press, Los Alamitos, CA.

IVES B, HAMILTON S and DAVIS G (1980) A framework for research in computer-based management information systems. Management Science 26(9), 910–934.

JACOB RJK and FROSCHER JN (1990) A software engineering methodology for rule-based systems. IEEE Transactions on Knowledge and Data Engineering 2(2), 173–189.

JEFFERY DR (1987) Software engineering productivity models for management information system development. In Critical Issues in Information Systems (BOLAND RJ and HIRSCHEIM RA, Eds), pp 113–134, Wiley, Chichester.

JOJO L and O'KEEFE RM (1994) Experiences with an expert system prototyping methodology. Expert Systems: The International Journal of Knowledge Engineering 11(1), 13–22.

KINGSTON J (1992) Pragmatic KADS: a methodological approach to a small knowledge-based systems project. Expert Systems: The International Journal of Knowledge Engineering 9(4), 171–180.

LEE S (1993) Quality Issues of Knowledge Bases in Expert System Development: An Exploratory Study, PhD Thesis, Rensselaer Polytechnic Institute, Troy, New York.

LEE S and O'KEEFE RM (1994) Developing a strategy for expert system verification and validation. IEEE Transactions on Systems, Man and Cybernetics 24(4), 643–655.

LEE S and O'KEEFE RM (1996) The effect of knowledge representation schemes on maintainability of knowledge-based systems. IEEE Transactions on Knowledge and Data Engineering 8(1), 173–178.

LONG JA and NEALE IM (1993) Using paper models in validation, verification and testing. International Journal of Expert Systems 6(3), 383–400.

NAZARETH D (1989) Issues in the verification of knowledge in rule-based systems. International Journal of Man-Machine Studies 30, 255–271.

NOSEK JT and ROTH I (1990) A comparison of formal knowledge representation schemes as communication tools: predicate logic vs semantic network. International Journal of Man-Machine Studies 33, 227–239.

O'KEEFE RM, BALCI O and SMITH EP (1987) Validating expert system performance. IEEE Expert 2(4), 81–90.

O'KEEFE RM (forthcoming) Issues in the verification and validation of Knowledge-based Systems. In Advances in Software Engineering and Knowledge Engineering (AMBRIOLA V and TORTORA G, Eds), World Scientific Publishing.

O'KEEFE RM and LEE S (1990) An integrative model of expert system

## About the authors

Sunro Lee, PhD is an Assistant Professor of Information Systems in the College of Business and Public Affairs at Yonsei University at Wonju, Korea. He previously taught at Hong Kong University of Science and Technology. His research interests are in verification and validation of knowledge-based systems, cross-cultural/organizational issues of IT management, productivity measures of application systems development, and electronic commerce. His articles have been published in several information systems journals and IEEE transactions.

verification and validation. Expert Systems With Applications 1(3), 231–236.

O'KEEFE RM and O'LEARY DE (1993) A review and survey of expert system verification and validation. Artificial Intelligence Review 7(1), 3–42.

O'LEARY D (1988) Expert system prototyping as a research tool. In Applied Expert Systems (TURBAN E and WATKINS P, Eds), pp 17–32, North-Holland, Amsterdam.

O'LEARY D (1991) Design, development and validation of expert systems: A survey of developers. Verification, Validation and Testing of Expert Systems, John Wiley, New York, NY, 3–19.

PETERSON JL (1981) Petri Nets, Theory and The Modelling of Systems, Prentice-Hall, Englewood Cliffs, NJ.

PREECE AD (1990) Towards a methodology for evaluating expert systems. Expert Systems: The International Journal of Knowledge Engineering 7(4), 215–223.

PREECE AD, SHINGHAL R and BATAREKH A (1992) Verifying expert systems: A logical framework and a practical tool. Expert Systems With Applications 5, 421–436.

SACKMAN H, ERICKSON WJ and GRANT EE (1968) Exploratory experimental studies comparing online and offline programming performance. Communications of the ACM 11, 3–11.

SHEPHARD GG (1993) Providing descriptive power to guided self-elicitation. Knowledge Acquisition 5, 347–366.

SUBRAMANIAN GH et al (1992) A comparison of the decision table and tree. Communications of The ACM 35(1), 89–94.

SUH KS and JENKINS MA (1992) A comparison of linear keyword and restricted natural language data base interfaces for novice users. Information Systems Research 3(3), 252–272.

SWIGGER KM and BRAZILE RP (1989) Experimental comparison of design documentation formats for expert systems. International Journal of Man-Machine Studies 31, 47–60.

VESSEY I and GALLETTA D (1991) Cognitive fit: an empirical test of information acquisition. Information Systems Research 2(1), 63–84.

Bob O'Keefe, PhD is Professor of Information Management in the Department of Computer Science and Information Systems, Uxbridge, UK. He was previously a faculty member at Rensselaer Polytechnic Institute, Troy, New York, USA. Research interests include networked organizations and electronic commerce, decision support (including knowledge-based systems), and computing in small companies. He has published in numerous journals including Management Science and Operations Research.
