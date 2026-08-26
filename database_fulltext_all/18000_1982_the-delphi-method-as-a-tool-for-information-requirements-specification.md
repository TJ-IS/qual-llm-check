---
otero_id: 18000
otero_key: "JJKRTFTR"
title: "The Delphi Method as a tool for information requirements specification"
authors: "Victor L. Pérez; Rolf Schüler"
year: "1982"
journal: "Information & Management"
doi: "10.1016/0378-7206(82)90022-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Delphi Method as a Tool for Information Requirements Specification

Victor L. Pérez and Rolf Schüler

Departamento de Ingeniería Industrial, Universidad de Chile, Casilla 2777, Santiago, Chile

An application of the Delphi Method to the logical design of an Information System supporting the operation, control, evaluation and planning of student -related academic administration activities is presented. The logical design process was as follows: (1) a traditional top-down approach was used to define the system objectives and the information required to support structured (i.e., operational) activities; (2) the Delphi Method was used for generating a group opinion with respect to the proposed system objectives and the information required by unstructured and/or ill-structured decision making. The paper finally discusses how this search for group opinion significantly enhances the effectiveness of the resulting information system.

Keywords: Delphi Method, information systems design, statement of information requirements, academic administration.

![](/api/attachments/JJKRTFTR/fulltext/images/b40476ac144da55f58f8f56c3df5aec3acd7a4dc36b6dd229a974f090f190f0d.jpg)

Victor L. Pérez is Chairman and Professor of Management Information Systems of the Departamento de Ingeniería Industrial at the Universidad de Chile, Chile. He has published in several international journals on MIS, and he is the co-author of four textbooks on Information Systems and the author of more than 35 technical articles on data base management, information systems design and industrial management. He has served as consultant to several governmental, business and international (PAHO, UNESCO) organizations.

## 1. The Logical Design of Information Systems

The process of how to approach the logical design of an information system (IS) is a subject addressed by many authors $[2,8,17]$ , all dealing with the identification and specification of the information requirements that should be satisfied by the information system and showing the need for more research in two areas.

The first research area deals with the complexity of the IS logical design process. Different approaches have been proposed, including: top-down decomposition (structured analysis) of the system into levels of functional components (i.e., identification of design levels [2,8]); techniques that allow the analysis of, and assure the consistency among, the elements that make up the specification of the IS logical design [10,13,16], etc.

The second area deals with the relationship between management (decision making) systems and the organizational information systems: the information requirements imposed by the decision makers are directly related to the way that decision makers carry-out their activities.

Here, we describe how, using a top-down approach and the Delph Method, the interrelationships between these two types of systems were considered during the logical design of an IS. The system was designed to support student-related academic administration activities in a chilean university.

![](/api/attachments/JJKRTFTR/fulltext/images/ae9bed060131094b71a78a1415819b397e07990879bfc56b462b2e236cd00fd7.jpg)  
Rolf Schüler is a research assistant of the Departamento de Ingeniería Industrial at the Universidad de Chile. He received a M.S. in Industrial Engineering from the Universidad de Chile. He currently works in the field of information systems design.

More often than not, the need to know these interrelationships has practically no importance when the IS has to support structured [14] and/or operational level [1] decision making; then the information requirements are almost independent of the decision maker. This does not happen, however, in cases where the decisions are non-structured [14] and/or tactical-strategical [1]; here, the interrelationships are heavily dependent on the world view (background and psychological makeup) and the decision style of the decision makers who request such information. Those types of decisions are often made by means of heuristics that are specific to a given process. As a result, an attempt to structure only results in a tailor-made or “personalized” IS – one useful to that specific person, and possibly no one else. All information that is not identified by that person or request is generally ignored. For multiple users, the problem of reaching compatibility in requirements among the “personal” request of each of the users is more complex.

Several attempts are being made to provide a methodology for systems analysts. Mitroff, Emshoff and Kilmann [12] have applied a nominal group or stakeholder analysis to provide a method that uses experts for developing objectives. Stabell [15] has suggested the use of marketing techniques as a way to incorporate attitudes and perceptions about the different information alternatives supporting a given process.

## 2. Description of the Application

## 21. Framework

SINIAC is an information system designed to support the operation, control, evaluation, and planning of student academic activities for the School of Engineering of a chilean university. During its design, several facts arose:

a) The IS had to support both structured and non-structured activities. Besides manipulating the data required to carry-out all the day-to-day student related activities, the IS was also required to provide information supporting the evaluation of its effectiveness and the value of related academic administration activities (e.g., of the educational process, course planning, enrollment forecasting, class scheduling).

b) The users of SINIAC were identified as both operational (e.g., the Student Registration Office) and management control (e.g., the Dean's Academic Committee).

c) Even though the information being to support operational activities would also be useful for generating information for management control activities, two types of indicators should have to be identified to evaluate: (1) the performance of SINIAC, and (2) the planning and control aspects of the student-related academic administration.

d) In order to avoid some deficiencies of the current system, the new system should take account of the experience of able university administrators and former and potential university administrators' opinions.

e) The logical design of SINIAC was then planned as follows:

i) Using a traditional top-down approach a preliminary logical design was performed. Some of the results were: (1) a set of objectives, (2) a set of functional components implementing these objectives, and (3) a set of information requirements, including a list of performance indicators.

ii) Using the Delphi Method, the set of objectives and the lists of performance indicators were presented to a group of university administrators. They were asked to participate in the Delphi exercise (to reach a group opinion about the proposed objectives and the performance indicators). The administrators were to comment, validate, and evaluate the propositions, as well as introduce and justify new ones.

iii) Using traditional techniques all the information requirements were specified (e.g., data elements, reports layout, data manipulation tasks).

## 2.2. Preliminary logical design

## 2.2.1. Methodological framework

The preliminary logical design was carried-out as follows:

i) Searching for the new system objectives; interviewing the future final users and obtaining existing documentation on the scope, deficiencies, and operational restrictions of the current system.

ii) Identifying all the major activities required to implement the system objectives; these were considered the major functional components of SINIAC [4].

iii) Using structured analysis each functional component was decomposed into subcomponents; the decomposition process ended when the resulting subcomponents were manageable (i.e., when the designer could generate implementation alternatives for each subcomponent). The final result of this was the identification of all the functional components of SINIAC (with their corresponding functional objectives).

iv) Using cost-benefit analysis and considering the different types of restrictions (e.g., operational, administrative, personnel, institutional), one alternative was selected for each of the functional components. The identification of most of the information requirements was then straight forward.

v) The analysis, to this point, had not considered unstructured activities. In order to incorporate the manipulation of the information to support these, two types of indicators were identified by the users and analysts: first, to evaluate the effectiveness of SINIAC several indicators were identified for each component – these measured the system performance with respect to its functional objectives; second, to evaluate the effectiveness of some (student-related) academic administration activities – here, eight different academic administration activities were identified and the working group generated, for each, a set of performance indicators.

vi) Finally, the specification of all the information requirements (i.e., operational information and performance indicators) was completed. This therefore linked both the academic administration system and one of its supporting information systems.

## 2.2.2. Proposed objectives

The SINIAC objectives were defined as being to provide:

i) An adequate record of the students' academic activities.

ii) Information supporting the design, operation, control, compatibility (i.e., fulfilment of university regulations), and evaluation of academic degree programs.

iii) Information allowing the evaluation of the students' academic performance and the overall teaching process.

iv) Administrative procedures allowing the system users to provide for new requirements for supporting unstructured activities.

v) Information supporting comparative analysis of courses simultaneously offered in different sections, and the analysis of alternative courses.

vi) Information supporting comparative analysis of the different course-scheduling alternatives in a particular academic program.

vii) Statistics about academic activities in the School of Engineering (as input to other institutional information systems).

viii) Information supporting other related administrative activities (e.g., class-room scheduling, courses scheduling, administrative registration).

ix Information about the students' socio-economic and educational levels (in order to detect relationships, if any, between these and academic performance).

x) Information allowing the identification of the non-academic student skills (e.g., cultural, social and sporting activities).

## 2.2.3. Functional components

The following is the list of functional components, consisting of its name followed by the total number of indicators evaluating its effectiveness.

i) Administration of student registration (7)

ii) Course specification (9)

iii) Classroom and courses scheduling (7)

iv) Students academic registration (8)

v) Students administrative exit (2)

(i) Recording and updating of the students' academic activities (6)

vii) Students academic admittance (2)

## 2.2.4. Academic Administration activities

The following is the list of student-related academic administration activities. Along with the name of each activity, the total number of indicators evaluating its effectiveness is presented.

Evaluation of the different admission tests required to candidates applying to the School of Engineering (4).

ii) Evaluation of the academic results obtained in the courses offered by the School of Engineering (5).

iii) Evaluation of academic program size (3).

iv) Evaluation of the "output" of each academic program (7).

Evaluation of the students' academic "quality" (8).

vi) Evaluation of Special students' academic "quality" (2).

vii) Evaluation of students' academic performance, with respect to previous high school performance and geographical location of family residence (6).

viii) Administrative evaluation of academic activities (4).

## 2.3. The Delphi exercise

## 2.3.1. The Delphi Method

There are several good descriptions of the Delphi Method, including its applications and some results [3.5-7.9.11.18]. In these, Delphi is outlined as a formal way of dealing with problems (opinions) which do not have a solid information basis and that have been traditionally solved by face-to-face discussions.

As a means of diminishing some of the negative psychological factors [9] of face-to-face discussion (particularly specious persuasion, fear of retracting an expressed opinion, the distorting effect of the majority opinion, dominating personality, and group compulsion), the Delphi Method gathers opinions in writing; panel members see the anonymous collection of answers and supporting explanations and may wish to bring their answers in line with those of the group. It is hoped that several rounds will produce a group opinion or consensus of experts.

Thus, the method has three major characteristics: (1) anonymity, (2) controlled feedback and (3) statistical based answers, because the feedback to a “next round” includes the group opinion stated in terms of some central value of the distribution obtained from the previous answers.

## 2.3.2. Development of the exercise

Our exercise took five rounds and dealt with the opinions of nine experts (Department Chairmen, two former Deans, one university planning expert, one member of the Dean's Academic Committee, and a senior officer of the Registration Office of the School of Engineering). The authors of this paper were Delphi Administrators in charge of the exercise.

Rounds 1 and 2 analyzed the proposed objectives. Rounds 2 and 3 analyzed the proposed indicators evaluating effectiveness.

Rounds 4 and 5 analyzed the proposed indicators evaluating the academic administration activities being supported. Thus one can say that the study consisted of three (somewhat short) applications of the Delphi technique.

For each round, the experts received a questionnaire with directions about the subject being discussed, its scope, and the significance of the criteria and their grading scale. They evaluated each subject using a 1-to-5 points grading scale, 1 being the lowest preference and 5 the highest. Furthermore, the experts were encouraged to make comments about the subject or introduce any new variable they felt was relevant, along with its justification. New variables and a summary of the comments with a statistical summary of the numerical answers were then introduced as feedback for the next round.

During the analysis secondary evaluation aspects were included. It was not necessary to obtain consensus on these, but rather to identify those most preferred.

The analysis was as follows:

i) The objectives of SINIAC. During rounds 1 and 2 each one of the 10 proposed objectives was evaluated with respect to four categories: (1) Validity: is it valid to ask a system to pursue this objective?; (2) Desirability: does it have some benefits—either tangible or intangible?; (3) System implementation feasibility: is it possible to accomplish this objective?; (4) Degree of current success: to what extent do current mechanisms and formal procedures satisfy this objective?.

ii) The indicators evaluating the effectiveness of SINIAC. The preliminary logical design of SINIAC defined a set of indicators evaluating the performance of each of the functional components. During rounds 2 and 3, these indicators were presented to the experts; and they were asked to analyze each one for its utility (usefulness and appropriateness in measuring the effectiveness of its activity). The result of this analysis was the "utility" of each of the indicators; the median and quartiles of the group's answer distribution were then presented as a characterization of the consensus degree.

Secondary aspects addressed during round 3 were: (1) arrange, in a decreasing ordered list of preferences, all the proposed indicators within each functional component; (2) select, among all the proposed indicators of this type, the first 5, 10, 15 and 20 most important indicators. These provided implementation priority criteria.

iii) The indicators evaluating the effectiveness of the academic administration activities. The preliminary logical design identified eight academic administration activities to be evaluated. In order to evaluate the performance of these, a set of indicators was then identified for each. During rounds 4 and 5, the different sets were presented and the experts were asked to analyze each indicator for utility.

Secondary aspects addressed in round 5 were: (1) arrange in a decreasing ordered list of preferences, all the proposed indicators within each set; (2) select, among all the indicators of this type, the first 5, 10, 15 and 20 most important indicators.

## 2.4. Methods for Evaluating the Results

## 2.4.1. Numerical answers, comments, and new proposal of objectives and indicators

For each of the four categories (validity, desirability, feasibility, and degree) and for each one of the indicators evaluated with respect to their “utility”, a histogram of answers was constructed. Another histogram was made for the cumulative distribution of answers. The median and quartiles for the distribution of each type of answer were then determined; the median was interpreted as the group answer, and the quartiles indicated the degree of dispersion of the answers (See Table 1 and the “Utility” column of Tables 2 and 3).

Each objective and indicator was reevaluated (in the following round) to see whether high consensus and/or stability was obtained. Consensus was defined as a dispersion that was within a value defined by the Delphi Administrators (measured by the amplitude of the interquartile range). If a topic did not achieve a high degree of consensus, the topic was not reevaluated after the stability of its interquartile range was achieved [6].

In particular, two of the objectives (\#6 and \#9) were not reevaluated presenting dispersions of 1.6 and 1.7 in “validity”, and of 1.3 and 1.7 in “desirability”, respectively. However the Delphi Administrators required an indicator dispersion of less than or equal to 1.1 in order to be considered as “high consensus”. This apparent difference in criteria was due to the fact that the main interest of the exercise was to accept or reject each objective based upon its mean value, whereas the indicators were to be classified with respect to their usefulness in the performance evaluation process.

## 2.4.2. Arrangement and grouping of indicators

From each of the different lists of ordered indicators, a histogram of frequencies was obtained (based on the position that each indicator had in the list), as well as the corresponding mean and standard deviation. Also, for each group selecting the 5, 10, 15 and 20 most preferred indicators, a histogram of frequencies of the appearances of each indicator within each group was obtained; cumulative histograms were constructed (see the last two columns in Tables 2 and 3).

## 2.5. Analysis of the Results of the Exercise

## 2.5.1. The objectives of SINIAC

Six out of ten proposed objectives were accepted in the first round; their medians were above 4.0 in the two most important evaluation categories (validity and desirability) and their interquartile ranges were less or equal than 1.1. Two objectives (\#7 and \#10) were submitted to reevaluation in round 2; after this, objective \#7 was accepted.

Table 1:  
Results from the evaluation of all the considered objectives

<table><tr><td rowspan="2">OBJECTIVE N°</td><td rowspan="2">TQ: THIRD QUARTILE M: MEDIAN FQ: FIRST QUARTILE</td><td colspan="2">VALIDITY</td><td colspan="2">DESIRABILITY</td><td>FEASIBILITY</td><td>DEGREE</td></tr><tr><td>ROUND 1</td><td>ROUND 2</td><td>ROUND 1</td><td>ROUND 2</td><td>ROUND 1</td><td>ROUND 1</td></tr><tr><td rowspan="3">1</td><td>TQ</td><td>4.8</td><td>-</td><td>4.8</td><td>-</td><td>4.7</td><td>3.7</td></tr><tr><td>M</td><td>4.5</td><td>-</td><td>4.5</td><td>-</td><td>4.3</td><td>3.0</td></tr><tr><td>FQ</td><td>4.3</td><td>-</td><td>4.3</td><td>-</td><td>4.0</td><td>2.3</td></tr><tr><td rowspan="3">2</td><td>TQ</td><td>4.7</td><td>-</td><td>4.7</td><td>-</td><td>4.5</td><td>2.8</td></tr><tr><td>M</td><td>4.4</td><td>-</td><td>4.4</td><td>-</td><td>4.0</td><td>2.3</td></tr><tr><td>FQ</td><td>4.1</td><td>-</td><td>4.1</td><td>-</td><td>3.3</td><td>1.5</td></tr><tr><td rowspan="3">3</td><td>TQ</td><td>4.8</td><td>-</td><td>4.8</td><td>-</td><td>4.3</td><td>3.0</td></tr><tr><td>M</td><td>4.5</td><td>-</td><td>4.5</td><td>-</td><td>3.7</td><td>2.3</td></tr><tr><td>FQ</td><td>4.3</td><td>-</td><td>4.3</td><td>-</td><td>3.0</td><td>1.7</td></tr><tr><td rowspan="3">4</td><td>TQ</td><td>4.6</td><td>-</td><td>4.7</td><td>-</td><td>4.0</td><td>2.7</td></tr><tr><td>M</td><td>4.2</td><td>-</td><td>4.4</td><td>-</td><td>3.3</td><td>2.0</td></tr><tr><td>FQ</td><td>3.5</td><td>-</td><td>4.1</td><td>-</td><td>2.5</td><td>1.0</td></tr><tr><td rowspan="3">5</td><td>TQ</td><td>4.7</td><td>-</td><td>4.6</td><td>-</td><td>4.6</td><td>2.0</td></tr><tr><td>M</td><td>4.4</td><td>-</td><td>4.2</td><td>-</td><td>4.2</td><td>1.5</td></tr><tr><td>FQ</td><td>4.1</td><td>-</td><td>3.7</td><td>-</td><td>2.7</td><td>1.0</td></tr><tr><td rowspan="3">6</td><td>TQ</td><td>4.6</td><td>-</td><td>4.3</td><td>-</td><td>4.3</td><td>1.5</td></tr><tr><td>M</td><td>4.2</td><td>-</td><td>3.7</td><td>-</td><td>3.7</td><td>1.0</td></tr><tr><td>FQ</td><td>3.0</td><td>-</td><td>3.0</td><td>-</td><td>3.0</td><td>1.0</td></tr><tr><td rowspan="3">7</td><td>TQ</td><td>4.6</td><td>4.5</td><td>4.5</td><td>4.4</td><td>4.3</td><td>2.5</td></tr><tr><td>M</td><td>4.2</td><td>4.1</td><td>4.0</td><td>3.8</td><td>3.8</td><td>1.8</td></tr><tr><td>FQ</td><td>3.0</td><td>3.1</td><td>2.5</td><td>3.1</td><td>3.3</td><td>1.3</td></tr><tr><td rowspan="3">8</td><td>TQ</td><td>4.8</td><td>-</td><td>4.7</td><td>-</td><td>4.5</td><td>3.0</td></tr><tr><td>M</td><td>4.5</td><td>-</td><td>4.4</td><td>-</td><td>4.0</td><td>2.3</td></tr><tr><td>FQ</td><td>4.3</td><td>-</td><td>4.1</td><td>-</td><td>2.7</td><td>1.0</td></tr><tr><td rowspan="3">9</td><td>TQ</td><td>4.7</td><td>-</td><td>4.7</td><td>-</td><td>4.0</td><td>1.8</td></tr><tr><td>M</td><td>4.3</td><td>-</td><td>4.3</td><td>-</td><td>3.3</td><td>1.3</td></tr><tr><td>FQ</td><td>3.0</td><td>-</td><td>3.0</td><td>-</td><td>2.5</td><td>1.0</td></tr><tr><td rowspan="3">10</td><td>TQ</td><td>4.3</td><td>3.3</td><td>4.3</td><td>3.4</td><td>3.5</td><td>1.3</td></tr><tr><td>M</td><td>2.7</td><td>2.5</td><td>3.5</td><td>2.8</td><td>2.5</td><td>1.0</td></tr><tr><td>FQ</td><td>2.0</td><td>1.8</td><td>2.5</td><td>2.1</td><td>1.0</td><td>1.0</td></tr><tr><td></td><td></td><td>ROUND 2</td><td>ROUND 3</td><td>ROUND 2</td><td>ROUND 3</td><td>ROUND 2</td><td>ROUND 2</td></tr><tr><td rowspan="3">11</td><td>TQ</td><td>4.5</td><td>4.7</td><td>4.5</td><td>4.7</td><td>4.5</td><td>1.7</td></tr><tr><td>M</td><td>4.1</td><td>4.0</td><td>4.1</td><td>4.0</td><td>4.1</td><td>1.1</td></tr><tr><td>FQ</td><td>2.6</td><td>2.0</td><td>2.6</td><td>2.0</td><td>3.4</td><td>1.0</td></tr></table>

Two other objectives (#6 and #9) were accepted without submission to the second round by the Delphi Administrators because of highly favorable comments using their initial evaluation. Objective #11, which was proposed by one of the experts, obtained a high median and a very high dispersion; it was feedback into round 3, but the dispersion grew. This conflicting behavior can be explained by the fact that most of the experts thought that this objective (“to provide an adequate record of the instructors’ resume”) would correspond more to a Personnel Administration System; it was finally rejected.

Table 1 shows the results from the evaluation of all the considered objectives; all the underlined objective numbers (in the first column) correspond to the accepted objectives for SINIAC.

Results for the indicators evaluating the effectiveness of the functional component N° 1

<table><tr><td rowspan="2">INDICATOR $N^o$ </td><td colspan="2">UTILITY</td><td rowspan="2">FROM THE ARRANGEMENT OF INDICATORS (ROUND 3)</td><td colspan="4">NUMBER OF EXPERTS SELECTING THE INDICATOR, WITHIN THEIR SET OF “n” MOST PREFERRED INDICATORS (ROUND 3)</td></tr><tr><td>ROUND 2</td><td>ROUND 3</td><td>n = 5</td><td>n = 10</td><td>n = 15</td><td>n = 20</td></tr><tr><td>1</td><td>TQ 4.6M 4.2FQ 3.7</td><td>--</td><td>Mean (Me) 1.75Standard Deviation(S.D.) 1.39</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>2</td><td>TQ 4.3M 3.8FQ 3.4</td><td>--</td><td>Me 6.13S.D. 1.27</td><td>0</td><td>0</td><td>1</td><td>3</td></tr><tr><td>3</td><td>TQ 4.7M 4.3FQ 4.0</td><td>--</td><td>Me 3.13S.D. 1.90</td><td>1</td><td>5</td><td>5</td><td>5</td></tr><tr><td>4</td><td>TQ 4.6M 4.2FQ 3.5</td><td>--</td><td>Me 2.25S.D. 0.66</td><td>1</td><td>4</td><td>6</td><td>6</td></tr><tr><td>5</td><td>TQ 4.6M 4.2FQ 3.5</td><td>--</td><td>Me 5.88S.D. 1.27</td><td>0</td><td>1</td><td>1</td><td>2</td></tr><tr><td>6</td><td>TQ 4.6M 4.2FQ 3.5</td><td>--</td><td>Me 6.00S.D. 1.94</td><td>0</td><td>0</td><td>1</td><td>2</td></tr><tr><td>7</td><td>TQ 4.7M 4.3FQ 4.0</td><td>--</td><td>Me 5.75S.D. 1.39</td><td>0</td><td>0</td><td>2</td><td>2</td></tr><tr><td>8(Proposed by the experts)</td><td>TQ -M -FQ -</td><td>4.33.83.3</td><td>Me 5.13S.D. 1.96</td><td>0</td><td>0</td><td>1</td><td>2</td></tr></table>

## 2.5.2. The indicators

Results from the “utility” evaluations of the indicators are presented in Tables 2 and 3 (“utility” columns). Table 4 shows the movements towards consensus, round by round; from this, it can be seen that after rounds 3 and 5, 74 of 95 indicators reached consensus status (77.9%).

It is interesting to observe the results of the evaluation of the secondary aspects in rounds 3 and 5. It will be seen that the experts agree about the relative position of the different indicators within its sets (either a functional component or a decision-making activity).

Tables 5 and 6 show a summary of the results from the processes selecting the 5, 10, 15 and 20 most preferred indicators. Each column corresponds to one of the requested groups containing “n” indicators. The different values within the “n=5” column correspond to the amount of indicators that were equally selected by “i” experts (i=0, 1, 2,...) when they had to choose their 5 most preferred indicators (e.g., in Table 5, 4 specific indicators were selected by 5 experts to enter their group of 5 most preferred indicators).

After analyzing the results shown in Tables 5 and 6, it was possible to accept the majority's opinion (5 and 4 experts respectively) of 11 and 15 indicators as being those preferred. These indicators were given high priority for implementation. These 24 indicators were analyzed with respect to the data and data manipulation activities. The results were then introduced as formal requirements within the logical design of SINIAC.

Results for the indicators evaluating the performance of the (students-related) decision-making activity N° 2

<table><tr><td rowspan="2">INDICATOR $N^{\circ}$ </td><td colspan="2">UTILITY</td><td rowspan="2">FROM THE ARRANGEMENT OF INDICATORS (ROUND 5)</td><td colspan="4">NUMBER OF EXPERTS SELECTING THE INDICATOR, WITHIN THEIR SET OF “n” MOST PREFERRED INDICATORS (ROUND 5)</td></tr><tr><td>ROUND 4</td><td>ROUND 5</td><td>n = 5</td><td>n = 10</td><td>n = 15</td><td>n = 20</td></tr><tr><td rowspan="3">1</td><td rowspan="3">TQ 4.7M 4.4FQ 4.2</td><td>-</td><td rowspan="3">Me 1.33S.D. 1.75</td><td rowspan="3">4</td><td rowspan="3">5</td><td rowspan="3">5</td><td rowspan="3">6</td></tr><tr><td>-</td></tr><tr><td>-</td></tr><tr><td rowspan="3">2</td><td rowspan="3">TQ 4.4M 3.9FQ 3.3</td><td>-</td><td rowspan="3">Me 3.33S.D. 1.70</td><td rowspan="3">1</td><td rowspan="3">2</td><td rowspan="3">3</td><td rowspan="3">3</td></tr><tr><td>-</td></tr><tr><td>-</td></tr><tr><td rowspan="3">3</td><td rowspan="3">TQ 3.9M 3.4FQ 2.3</td><td rowspan="3">3.53.02.3</td><td rowspan="3">Me 4.67S.D. 1.37</td><td rowspan="3">0</td><td rowspan="3">0</td><td rowspan="3">3</td><td rowspan="3">3</td></tr><tr></tr><tr></tr><tr><td rowspan="3">4</td><td rowspan="3">TQ 3.9M 2.9FQ 2.3</td><td rowspan="3">3.83.02.5</td><td rowspan="3">Me 4.67S.D. 0.47</td><td rowspan="3">0</td><td rowspan="3">0</td><td rowspan="3">0</td><td rowspan="3">1</td></tr><tr></tr><tr></tr><tr><td rowspan="3">5</td><td rowspan="3">TQ 4.5M 4.1FQ 3.1</td><td rowspan="3">4.33.52.5</td><td rowspan="3">Me 3.17S.D. 1.46</td><td rowspan="3">0</td><td rowspan="3">3</td><td rowspan="3">3</td><td rowspan="3">4</td></tr><tr></tr><tr></tr><tr><td rowspan="3">6(Proposed by the experts)</td><td rowspan="3">TQ -M -FQ -</td><td rowspan="3">3.93.53.1</td><td rowspan="3">Me 3.83S.D. 1.46</td><td rowspan="3">0</td><td rowspan="3">2</td><td rowspan="3">3</td><td rowspan="3">3</td></tr><tr></tr><tr></tr></table>

Table 4:

Evaluation of indicators

<table><tr><td>ROUND N°</td><td>ACTIVITY</td><td colspan="2">INDICATORS WITH HIGH CONSENSUS</td><td colspan="2">INDICATORS THAT DID NOT OBTAIN HIGH CONSENSUS</td></tr><tr><td>2</td><td>Evaluation of indicators about the effectiveness of SINIAC (41)</td><td>34</td><td>82.9%</td><td>7</td><td>17.1%</td></tr><tr><td rowspan="2">3</td><td>Reevaluation of indicators about the effectiveness of SINIAC (7)</td><td>2</td><td>28.6%</td><td>5</td><td>71.4%</td></tr><tr><td>Evaluation of indicators proposed by panel, about the effectiveness of SINIAC (10)</td><td>5</td><td>50.0%</td><td>5</td><td>50.0%</td></tr><tr><td>4</td><td>Evaluation of indicators about the performance of decision-making activities (39)</td><td>20</td><td>51.3%</td><td>19</td><td>48.7%</td></tr><tr><td rowspan="2">5</td><td>Reevaluation of indicators about the performance of decision-making activities (19)</td><td>11</td><td>57.9%</td><td>8</td><td>42.1%</td></tr><tr><td>Evaluation of indicators proposed by panel, about the performance of decision-making activities (5)</td><td>2</td><td>40.0%</td><td>3</td><td>60.0%</td></tr></table>

Table 5:  
About the selections of indicators evaluating the effectiveness of SINIAC (Round 3)

<table><tr><td rowspan="2">Number of experts</td><td colspan="4">Amount of indicators that were equally selected by “i” experts, in the subgroup of “n” indicators</td></tr><tr><td>n = 5</td><td>n = 10</td><td>n = 15</td><td>n = 20</td></tr><tr><td>i = 8</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>7</td><td>0</td><td>1</td><td>2</td><td>2</td></tr><tr><td>6</td><td>0</td><td>0</td><td>3</td><td>5</td></tr><tr><td>5</td><td>4</td><td>4</td><td>5</td><td>3</td></tr><tr><td>4</td><td>0</td><td>5</td><td>1</td><td>8</td></tr><tr><td>3</td><td>0</td><td>2</td><td>9</td><td>9</td></tr><tr><td>2</td><td>3</td><td>7</td><td>9</td><td>15</td></tr><tr><td>1</td><td>14</td><td>13</td><td>14</td><td>4</td></tr><tr><td>0</td><td>30</td><td>19</td><td>8</td><td>4</td></tr><tr><td>Total of considered indicators</td><td>51</td><td>51</td><td>51</td><td>51</td></tr></table>

About the selections of indicators evaluating the performance of the academic activities supported by SINIAC (Round 5)

<table><tr><td rowspan="2">Number of experts</td><td colspan="4">Amount of indicators that were equally selected by “i” experts, in the subgroup of “n” indicators</td></tr><tr><td>n = 5</td><td>n = 10</td><td>n = 15</td><td>n = 20</td></tr><tr><td>1 = 6</td><td>0</td><td>1</td><td>1</td><td>4</td></tr><tr><td>5</td><td>1</td><td>3</td><td>6</td><td>6</td></tr><tr><td>4</td><td>3</td><td>3</td><td>3</td><td>5</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>:</td><td>1</td><td>3</td><td>7</td><td>7</td></tr><tr><td>.</td><td>2</td><td>6</td><td>6</td><td>8</td></tr><tr><td>.</td><td>6</td><td>6</td><td>9</td><td>9</td></tr><tr><td>(</td><td>31</td><td>22</td><td>12</td><td>5</td></tr><tr><td>Total of considered indicators</td><td>44</td><td>44</td><td>44</td><td>44</td></tr></table>

## 3. Conclusions

Several conclusions result from this application of the Delphi Method to the logical design of an IS. Some are related to using a group opinion technique for obtaining interrelationships between unstructured decision making and its corresponding information requirements, while others result from the learning that occurred during the implementation of the Delphi exercise.

## 3.1. Methodological conclusions

a) Practical results showed the usefulness of the Delphi Method during the logical design of an IS. Even though there was no parallel project team solving the same problem, the resulting logical design specification was obtained in less time than the results from previous similar projects using non-Delphi techniques.

b) The exercise took about four months. Even though a more experienced team administering the study could have reduced that time, it is necessary to consider the delays while nine experts answer specialized questionnaires. Also, this technique could be used effectively when the size, the lack of structure, and the complexity of the problem recommend the existence of an experienced Delphi team. Even then, the IS logical design team should probably complement this technique with other group opinion approaches (e.g., stakeholder analysis [12]).

c) There are some areas where new applications of Delphi could be considered. The experts only discussed the objectives and the information requirements for the target information system. The way in which each expert supposed that unstructured decision making should be carried out were not formally investigated; even though those procedures are supposed to be the prime source for determining the users' information requirements.

## 3.2. Operational conclusions

a) Even though we were proponents of the "consensus business", we were surprised how well the interchanging of opinions improved the design. Frequently after the preliminary arguments and counterarguments had been made, there was fast convergence of opinions. Possibly this is because (1) the experts not only dominated the problem-area but also had their own ideas about how to tackle the subject, (2) the Delphi Administrators had good rapport with each of the participants, (3) all participants knew the whole problem-area and were known to be skillful administrators, (4) they were asked to answer their questions as if they were in the Dean's position, and (5) they all knew the academic administration regulations and the way of overcoming problems.

b) Even though all participants (including Delphi Administrators) were involved in the activities of the student-related academic administration, the preliminary logical design helped the Delphi Administrators to understand the related decision making processes. This was not, however, enough, because the ways in which each expert visualized the implementation was only “in his mind”; the exercise did not consider formalization of the process, and this introduced difficulties when preparing the directions for filling out the questionnaires and the subsequent summary of the answers (feedback). The bias introduced by the Delphi Administrators is also not known, but lack of a formalization definitely introduces some bias to the exercise.

c) In order to avoid possible bias, the Delphi Administrators carried out several interviews with each expert; this time consuming process led some participants to quit.

d) In other Delphi exercises [9] uncertainty is mentioned; we did not find this an issue, possibly because we tried to give light to today problem rather than predict the future.

e) Finally, one major by-product of the case study is our observed need for questioning the value and deficiencies of the existing management systems; this is important if we are to introduce computerized information systems supporting them.

## References

[1] R.M. Anthony, Planning and control systems: a framework for analysis (Harvard University Press, 1965).

[2] O. Barros, V.L. Pérez and A. Holgado, Structured logical design of information systems: a methodology, documentation and experience, Information Systems, Vol. 4, No. 1, (1979).

[3] B. Brown, Delphi process: a methodology used for the elicitation of opinions of experts, P-3925, RAND Co., Santa Mónica, Cal. (Sept. 1968).

[4] C.W. Churchman, The systems approach (Dell Publishing Co., 1968).

[5] N. Dalkey and O. Helmer, An experimental application of the Delphi Method to the use of experts, Management Science, Vol. 9, No. 3 (April 1963).

[6] N.C. Dalkey, The Delphi Method: an experimental study of group opinions, RM-5888-PR, RAND Co., Sanca Mónica, Cal. (June 1969).

[7] N.C. Dalkey, B. Brown and S. Cochran, The Delphi Method, IV: Effect of percentile feedback and feed-in of relevant facts, RM-6118-PR, RAND Co., Santa Mônica, Cal. (Mar. 1970).

[8] B. Langefors, Theoretical Analysis of Information Systems (Student-literature, Lund, Sweden, 1968).

[9] H.A. Linstone and M. Turoff (eds.), The Delphi Method. Techniques and applications (Addison-Wesley Publishing Co. Inc., 1975).

[10] H. Lynch, ADS: a technique for system documentation, Data Base Vol. 1, No. 1 (Spring, 1969).

[11] G. Milkovic, A. Annoni and T. Mahoney, The use of the Delphi procedures in manpower forecasting, Management Science, Vol. 19, No. 4 (Dec. 1972).

[12] I.I. Mitroff, J.R. Emshoff and R.H. Kilmann, Assumptional Analysis: a methodology for strategic problem solving, Management Science, Vol. 25, No. 6 (June 1979).

[13] J.F. Nunamaker, B. Konsynsky Jr., T. Ho and C. Singer, Computer-aided analysis and design of information systems, Commun. ACM, Vol. 19, No. 12 (1976).

[14] H. Simor., The new science of management decision (Harper and Row, 1969).

[15] Ch.B. Stabell, On the development of decision support systems as a marketing problem, Information Processing 74 (North Hoiland Publishing Co., Amsterdam 1974).

[16] D. Teichroew, Methodology for the design of information processing systems, Proceedings of Fourth Australian Computing Conference (Australia, 1969).

[17] D. Teichroew and H. Sayani, Automation of system building, Datamation (Aug. 15, 1971).

[18] M. Turoff, Delphi and its potential impact on information systems, Fall Joint Computer Conference 1971 (1971).
