---
otero_id: 17947
otero_key: "FQ5GS6TP"
title: "Some issues in the measurement and control of programming productivity"
authors: "D.R. Jeffery; M.J. Lawrence"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90057-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Some Issues in the Measurement and Control of Programming Productivity

D.R. Jeffery

Department of Information Systems, University of New South Wales, P.O. Box 1, Kensington 2033, N.S.W. Australia

and

M.J. Lawrence

Department of Information Systems, University of New South Wales, P.O. Box 1, Kensington 2033, N.S.W. Australia

In view of the escalating proportion of data processing expenditure going into software development, the measurement and control of software costs has become an important issue for commercial data processing managers. This paper surveys the state of the art in programming productivity research, investigates the application of research results to c.d.p. management, and suggests ways in which future research efforts can be improved. The apparent inconsistencies in the published literature of the field are highlighted and some possible explanations for them are advanced.

Keywords: Programming productivity, software metrics, information systems management, software development.

Date revised: March, 1981.

## 1. Introduction

The control of application software development costs is a primary concern of commercial data processing managers. In a situation where hardware costs continue to decline in comparison with software costs, and software development aids proliferate, the management of the human resources and their activities takes on a far greater significance to the data processing manager. However, many commercial data processing managers, because of the lack of comparable published information in this field, cannot determine whether their department is performing as well as, better, or worse than might be expected in comparison with other companies. From our experience, there is a lack of agreement in industry as to what might be considered high, medium or low performance, even in programming, and additionally many managers do not have statistics on their own department's performance. Consequently, many data processing departments lack one of the essential compo-

![](/api/attachments/FQ5GS6TP/fulltext/images/95176f1c5a5f18a97fffa17ba11cb9e98de21b6b5f86c3b89f9289a407efe0f1.jpg)

tions include papers in the areas of organisational objectives,

Ross Jeffery is currently a Lecturer in Information Systems at the University of New South Wales (Australia). He received a B. Com (Hons.) in Accountancy from the University of Queensland and an M. Com. (Hons.) in Information Systems from the University of New South Wales. During the last ten years he has also held positions at the University of Queensland and the Bendigo College of Advanced Education. His publicaprogramming productivity, and edp management, and three books on information systems. He is a member of ACM, ACS, AAANZ, SMIS and ASA.

![](/api/attachments/FQ5GS6TP/fulltext/images/2c11d376a999e73695b1e063b0d3d28ea0a38399ba5001116728ddbbc82bb2e5.jpg)

Michael Lawrence is senior lecturer in Information Systems at the University of New South Wales (Australia). He received a B.Sc, B.E. from the University of Sydney and M.S., Ph.D. from the University of California, Berkeley, majoring in Operations Research. Prior to joining the University of New South Wales he worked for Corning Glas Works, N.Y. and CIBA-GEIGY Corporation, N.Y. He has published in the fields of mathe matical reliability, inventory theory, forecasting, database systems and programming productivity.

nents of management control - a yardstick with which to compare actual performance.

A large proportion of the published material in the area of programming productivity is concerned with empirical studies using regression analysis. These studies have collected and analyzed data from a single organization in almost every case. This results in findings that are not necessarily applicable to any other organization. Unfortunately it is not only the organizational differences which make inter-company comparisons difficult; we find that the measurement methods also vary.

In order to measure programming productivity, a prerequisite is a satisfactory measurement method. Although lines of code written in a period of time is the measurement most often used, it has many drawbacks. These include:

(1) inability to account for quality, and degree of difficulty of the job, and

(2) measurement variation possible even when stated as lines of code per period of time.

Measurement of program quality has been attempted using characteristics of the code, as suggested by authors such as Gilb [9], Boehm [3], and Halstead [10]. These authors suggest that qualities such as execution time, module linkages, nesting, and memory space requirements are important properties, but as Anderson and Schneiderman point out, “these alone may not tell us whether a good algorithm has been selected, whether the code will be easy to debug or modify, whether the output is in natural and comprehensible form, or whether the modular decomposition was reasonable” [1]. Anderson and Schneiderman attempt to measure aspects of quality by the use of peer assessment methods. Further problems that exist in using lines of code in a productivity measure include lack of recognition of the impact of programming style and variability of standards; e.g. different styles result in spreading similar statements over varying numbers of lines, the count of lines may include or exclude comments, and the use or non-use of a statement such as “MOVE CORRESPONDING” in COBOL, will all affect the comparability of line counts. Thus the practitioner faces some severe problems in attempting to apply the research in the area of programming productivity to the organization. This paper investigates the problems of applying the research, and suggests ways in which future research may be improved.

## 2. Prior Research

The published research spans a period from the early 1960's to the present, providing some indication of the continuing interest in this area, but the lack of clear progress shows also the difficulties which have been experienced in deriving a suitable explanation for the variability in programmer productivity.

Work carried out by the System Development Corporation (SDC) in the 1960's led to Nelson's publication [14], where he presented the results of the statistical analysis of 169 "computer programming projects" and attempted to identify the factors causing variability in programming time, elapsed time, and computer run time. Much of the information presented is based on "the authors' experience or upon data and opinions found in the technical literature". The quantitative data collected from SDC, the U.S. Air Force, and industrial organizations, assumed that sufficient homogeneity existed between organizations to warrant the search for generally applicable forecasting equations. An example of the equations developed relevant to this paper relates the variables of Table 1 to total person-months. The equation is:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$Y = -33.63 + 9.15 \times 3 + 10.73 \times 8 + 0.51 \times 26 + 0.46 \times 30 + 0.40 \times 41 + 7.28 \times 42 - 21.45 \times 48.1 + 13.53 \times 48.5 + 12.35 \times 51 + 58.82 \times 53 + 30.61 \times 56 + 29.55 \times 72 + 0.54 \times 75 - 25.20 \times 76,$
</div>

where Y = total person-months in programming.

If we hypothesize a case: where operational requirements were well known (X3 = 0), initial design was unchanged (X8 = 0), percentage of mathematical instructions was 20% (X26 = 0.2), percentage of storage and retrieval was 40% (X30 = 0.4), number of sub programs was 10 (X41 = 10), programming language was COBOL (X42 = 0), a business program (X48.1 = 1), a stand alone program (X48.5 = 1), developed in an existing installation (X51 = 0), no hardware components were being developed (X53 = 0), random access device was used (X56 = 1), the same computer for development and operations (X72 = 0), number of trips was 5 (X75 = 5), and it was a military organization (X76 = 1), then we evaluate the previous equation to obtain Y = -39.15 person-months of programming effort. Thus, for this example, the equation produces a ridiculous estimate. Several reasons for this result may be conjectured:

Table 1

<table><tr><td>Variable</td><td>Explanation</td><td>Values</td></tr><tr><td>X3</td><td>Lack of knowledge of operational requirements</td><td>0, 1, 2</td></tr><tr><td>X8</td><td>Stability of design</td><td>0, 1, 2, 3</td></tr><tr><td>X26</td><td>Percent mathematical</td><td>% of instr.</td></tr><tr><td>X30</td><td>Percent information storage and retrieval</td><td>% of instr.</td></tr><tr><td>X41</td><td>Number of sub programs</td><td>count</td></tr><tr><td>X42</td><td>Programming language</td><td>Low level = 1High level = 0</td></tr><tr><td>X48.1</td><td>Business program</td><td>Yes = 1, No = 0</td></tr><tr><td>X48.5</td><td>Stand alone</td><td>Yes = 1, No = 0</td></tr><tr><td>X51</td><td>New Hardware</td><td>Yes = 1, No = 0</td></tr><tr><td>X53</td><td>Hardware developed with software</td><td>Yes = 1, No = 0</td></tr><tr><td>X56</td><td>Random access device</td><td>Yes = 1, No = 0</td></tr><tr><td>X72</td><td>Different computer for development</td><td>Yes = 1, No = 0</td></tr><tr><td>X75</td><td>Number of man trips for design concurrence</td><td>Count</td></tr><tr><td>X76</td><td>Military organization</td><td>Yes = 1, No = 0</td></tr></table>

This example is not intended to prove or disprove the validity of the work, but to show the ridiculous result than can be obtained when using a set of plausible values for the independent variables.

Another research effort of the 1960's was that of Sackman, Erickson and Grant [16], which was reported in 1968. These authors attempted to compare the difference in programmer debugging performance while working under conditions of online and offline access to the computer. It was found that online access resulted in substantially better performance (50% to 300% faster than off-

First, the poor fit of the regression equation, which explained only 58% of the variance in the SDC data; secondly, the domain of applicability of the equation is not given, and it is possible that our simple example lies outside the range; third, the large negative constant and large negative coefficient for “military organization” makes for an unstable equation, particularly when the program size is poorly indicated in the variables, and most of the variables are binary. In the sample from which this equation was derived, over 90 of the 169 programs were developed in less than 10 person-months, but the maximum was 300, with a mean of 40 and standard deviation of 62. Therefore, the programs ranged from quite small to large and complex, which would not be representative of most commercial applications. This must also contribute significantly to the variance in the data.

line). It was also noted that individual differences between programmers was highly significant, as shown in Table 2 [16].

In 1971, Gayle reported the results of a study of eighteen programs from three organizations, all of which were written in COBOL. By questionnaire method, the variables of Table 3 were measured [8]. One of the resulting equations that is of interest to our study is:

$$
\begin{array}{r l} \mathrm{Y1} & = 6. 3 6 - 1. 4 4 \mathrm{X} 3 + 0. 1 8 \mathrm{X} 7 \\ & - 0. 5 4 \mathrm{X} 5 + 0. 3 4 \mathrm{X} 6 \end{array}
$$

The mean of Y1 is 2.8; its standard deviation is 2.4; $R^{2}=0.58$ . In all of the equations developed by Gayle, the most frequently occurring independent variables were X3 and X7, with X10 appearing occasionally.

Table 2
Individual Differences

<table><tr><td>Performance Measure</td><td>Poorest Score</td><td>Best Score</td><td>Ratio</td></tr><tr><td>1. Debug hours Algebra</td><td>170</td><td>6</td><td>28 : 1</td></tr><tr><td>2. Debug hours Maze</td><td>26</td><td>1</td><td>26 : 1</td></tr><tr><td>3. Program size Algebra</td><td>6137</td><td>1050</td><td>6 : 1</td></tr><tr><td>4. Code hours Algebra</td><td>111</td><td>7</td><td>16 : 1</td></tr><tr><td>5. Code hours Maze</td><td>50</td><td>2</td><td>25 : 1</td></tr></table>

Another study that attempted to analyse the influence of various factors on programming productivity was reported by Walston and Felix in 1977 [17]. They defined programming productivity as the ratio of delivered source lines of code to the total effort (in person-hours) required to produce the delivered product [17]. Their objectives were to:

a. Provide data for the evaluation of improved programming technologies.

b. Provide support for proposals and contract performance.

c. Gather and preserve historical records of the software development work performed.

d. Provide programming data to management.

e. Foster a common programming terminology.

The collected data on sixty projects in the IBM Federal Systems Division. In their analysis, 29 variables were found to be significantly correlated with programming productivity. These include factors such as customer interface complexity, personnel experience and qualifications, structured programming, complexity of application processing, complexity of program flow, and hardware under concurrent development. As Kirkley [13] has pointed out, however, many of these variables (such as “customer interface complexity”) are subjective in terms of measurement.

Table 3

<table><tr><td></td><td colspan="2">Dependent variables</td></tr><tr><td>Y1</td><td colspan="2">Person months</td></tr><tr><td>Y2</td><td colspan="2">Calendar months</td></tr><tr><td>Y3</td><td colspan="2">Computer hours</td></tr><tr><td></td><td>Independent variables</td><td>Values</td></tr><tr><td>X1</td><td>Strictness</td><td>Time allowed to carry out the job. 3 = strict, 2 = moderately strict, 1 = not very strict</td></tr><tr><td>X2</td><td>Log of distance between user and programmer</td><td>Measured in feet</td></tr><tr><td>X3</td><td>Log of distance between programmer and computer</td><td>Measured in feet</td></tr><tr><td>X4</td><td>Log of data elements</td><td>No. of data elements in files</td></tr><tr><td>X5</td><td>Log of master records</td><td>No. of records in files</td></tr><tr><td>X6</td><td>No. of input formats</td><td></td></tr><tr><td>X7</td><td>No. of output formats</td><td></td></tr><tr><td>X8</td><td>Frequency of operation</td><td>Once per year = 1Once per month = 12Once per week = 52Once per day = 250</td></tr><tr><td>X9</td><td>Complexity</td><td>No. of data elements in output but not in input</td></tr><tr><td>X10</td><td>Programmer experience</td><td>No. of years</td></tr></table>

Another limiting constraint of this IBM study is that the data was collected on a project basis, rather than a program basis, which introduces the likelihood of a project lasting so long that there were changes to the project variables (in turn, this raises problems in estimating an average value for the project as a whole). Furthermore the effect of each variable on productivity was considered independently, and these results used to develop an equation purporting to relate productivity to the combined independent variables. As the joint distribution of productivity and these variables has been totally ignored, their equation is open to serious statistical question. Walston and Felix compute a productivity index as:

$$
\mathbf {I} = ^ {2 9} _ {1} W _ {i} X _ {i},
$$

where $W_{i}=$ variable weight, calculated as one-half $\log_{10}$ of the ratio of total productivity change indicated for a given question, and $X_{i}=$ question response (+1, 0, -1) depending on whether the response indicates increased, normal, or decreased productivity.

Despite these limitatins, Walston and Felix have successfully identified a number of factors which appear to influence programming productivity.

In a paper by Johnson [12], published in 1977, data on sixteen projects is presented. This data supports his hypothesis that productivity declines (on average) as project size increases. He also points out the effect of design difficulty, level of technology, and quality of staff.

Chrysler [5] reported in 1978 the results of attempts to relate program development time to program-and-programmer related variables. He set out to isolate significant independent variables that could be pre-determined (i.e. prior to commencing programming) so that a practical predictive model might be developed. Chrysler collected data on 36 programs from one organization and found that the most important variables influencing program development time were:

• number of input files;

• number of control breaks and totals;

• number of input edits;

\- months of programmer experience at this facility; and

• number of input fields.

In a later paper, Chrysler [6] explored the variables which impact the length of a program and determined from his sample that only the program related variables were significant in their effect. The identity or experience of the programmer did not appear to impact program size.

Another group currently looking at programming productivity is the Software Engineering Laboratory (SEL) at the University of Maryland. To date, they have gathered data on fifteen projects, written mainly in FORTRAN developed at NASA's Goddard Space Flight Center. The data items studied include: Total effort (time), lines of code, number of modules, elapsed time, documentation size, productivity, and average staff size. Effort is defined as "the number of man months of effort used on a project, through acceptance testing" [7]. Lines of code is measured in two ways: Delivered lines and developed lines. The difference is "reused" code, which is defined as code developed for a different project and applied with less than 20% change for this new project. Thus: Delivered lines (L) = developed lines (DL) + reused code. One aspect of this study has concentrated on a comparison of their results with those of Walston and Felix. Both studies found a nearly linear relationship (as shown below) between effort and lines of code:

W&F: $E = 5.2 \times L^{0.91}$

SEL: $E = 1.578 \times DL^{0.962}$

In an earlier paper [11] we presented the results of a study of three organizations which included the following linear relationships:

$$
T = 0. 0 9 P L + 4,\tag{1}
$$

$$
T = 0. 1 4 P L + 9. 5,\tag{2}
$$

$$
T = 0. 0 8 P L + 4. 3,\tag{3}
$$

In our study, T was defined as the total time for coding and unit testing, while PL is the number of new lines of procedure division code developed. A log model was rejected as the linear model provided a better fit. We found that programmer experience, measured as the number of years' programming, plays little or no role in how long a program takes to be written.

Another approach has been used by Putnam to estimate development time. He uses Raleigh curves to forecast project manpower, time, and effort requirements. But Putnam states that this technique is not generally applicable to small systems, because management tends to use a rectangular loading pattern, rather than reacting to need as the project develops [15].

## 3. Study Differences

The research to date in the area of programming productivity consists of studies which have collected relatively small amounts of data. The small sample size in many of the studies, as shown in Table 4, provides one possible reason for the conflicting results.

Examples of conflict occur with respect to (1) the role of experience, (2) the role of project size, (3) the independent variables selected for study, and (4) definitions of time or effort, program size, and the defined task.

## 4. Experience

In the programming environment, Chrysler found that experience significantly influences program development time [5] but this is not supported by Nelson [14] or our study [11], and it is only weakly supported by Gayle [8]. Walston and Felix found that 'overall personnel experience and qualifications' had a significant impact on productivity [17], but as their defined task included analysis, design, and programming. their findings cannot be directly compared with the other studies.

Table 4
Study Sample Sizes

<table><tr><td>SDC</td><td>169 projects</td></tr><tr><td>Gayle</td><td>18 programs</td></tr><tr><td>W&amp;F</td><td>60 projects</td></tr><tr><td>Johnson</td><td>16 projects</td></tr><tr><td>Chrysler</td><td>36 programs</td></tr><tr><td>SEL</td><td>15 projects</td></tr><tr><td>J&amp;L</td><td>93 programs</td></tr></table>

## 5. Project Size

The effect of the project size on productivity is a contentious issue. Johnson found that productivity declines on average as project size increases [12] and this was supported by Brooks [4]. However, Walston and Felix [17] and the SEL [7] have found the reverse to be the case, while our study [11] revealed a linear relationship as the best fit.

## 6. Independent Variables

Another problem encountered in attempting to compare these studies is the many different independent variables that have been measured in each study. When the equations have been developed using multiple regression, then the omission of any significant variable from the equation results in different weights being applied to the other independent variables [18]; furthermore, each equation is only representative of the study sample and may not represent "natural laws" or causative relationships. It should be noted that only one study tested the robustness of the equations developed [11], and consequently the relationships determined in the other studies may be valid only for the particular ranges and sample selected. Furthermore, management of the programming effort is management of a human resource, but the studies have only investigated the tools used and the technical environment in which the project was attempted. It is likely that factors such as objectives, group norms and interactions, and management methods and style will have substantial impact on the productivity of a programming team, but these factors have not been studied.

<table><tr><td>Input</td><td>Process</td><td>Output</td></tr><tr><td>Programmer</td><td>Technical</td><td></td></tr><tr><td>Characteristics</td><td>Environment</td><td></td></tr><tr><td></td><td>Programming</td><td>Program</td></tr><tr><td></td><td>Activity</td><td>Characteristics</td></tr><tr><td>Task</td><td>Behavioural</td><td></td></tr><tr><td>Characteristics</td><td>Environment</td><td></td></tr></table>

Fig. 1. Model of the Programming Process.

This problem can be highlighted if we look at a general model of the programming process (Fig. 1). This open system model reveals basic global variable omissions from, or assumptions in, many of the research efforts. Management of the programming effort is management in a socio-technical environment, but the studies have investigated only programmer and task characteristics and the technical environment in which the programming project was attempted. This may be an omission or an unstated assumption – that the behavioural environment will not bias the results.

Another assumption of significance revealed by this model is the fact that the task characteristics have been measured using a surrogate based on program characteristics. This is evident when we see measures of task size and task complexity being based on the number of lines, or the number of logic tests, or the number of data types in the finished code. This is not to say that such surrogates cannot be used as measures of the task, but it is important to highlight these as surrogates and not necessarily accurate measures of the target independent global variable which is the programming task.

## 7. Definitions

A problem that is evident in research is the differences in definitions that have been adopted. Time is defined in terms of person-months, person-years, and person-hours, but many of the studies provide no explanation of the units adopted. For example, the SEL does define one man-month as 172 man-hours, but Walston and Felix provide no such definition. Also the task is differently defined in terms of boundaries: i.e. where design becomes programming and when it finishes to become “production”. For example, Walston and Felix include “management administration, analysis, operational support, documentation, design, coding, and testing in the data collected”. The SEL include “programming effort and managerial and clerical overhead,” and, in our study, programming is defined as the time spent from receipt of program specifications to delivery of tested code. These differences are further compounded by the likely differences in the quality and extent of testing. "Lines of code" is not defined in some studies and defined differently in others. Again the SEL and Walston and Felix studies show differences in the definition of the "ratio of reused source code" [7]. Differences also exist in the measure of the program size, due to the fact that lines of code, number of statements, or number of verbs are all possible measures. In addition to this, the count may include or exclude comments, and is influenced by programming style. Thus the two most commonly used components of the productivity measure, time and lines of code, can both be measured and defined in different ways, and the studies do not always provide a basis for comparison or conversion.

Another significant problem is the availability of data for analysis and also the accuracy of that data. Many commercial organizations do keep records of time spent and resources allocated to projects, but very often the organizations adopt different definitions and may or may not have confidence in the accuracy of their records. Further-more, the commercial systems environment quite often undergoes change during the development lifecycle. For example, users' levels-of-understanding improve, technology changes, and business pressures and objectives change, causing difficulty in isolating the significant independent variables that impact the productivity of the system team.

## 8. Conclusions

The programming productivity studies reported in the literature present a rather confusing and conflicting picture. There is one exception; the degree of consensus that has emerged supporting a linear or near linear relationship between programming time and number of lines of code in the finished product. The problems that exist in using the literature to build a consistent model of the commercial programming environment are due to the fact that: 1. There is a lack of consistent definitions.

2. Many of the social and organizational factors impacting the programming task have not been identified and measured. This includes motivation, group norms, supervisory skills, etc.

3. A number of program related factors have been consistently omitted. These include program complexity, program quality, and documentation completeness and quality. Unfortunately appropriate metrics for these are still the subject of debate.

4. Data collection in the area is difficult, because many organizations do not collect the necessary statistics, and because the period of time required to accumulate the necessary statistics on a project is so long, the likelihood of holding many of the variables constant throughout the entire project is low.

5. Research is not being based on an accurate model of the programming activity; in consequence unstated assumptions have been made and these have not been fully explored in the problem analysis.

6. Inter-language studies are not being attempted.

In early research efforts of this kind, it is expected that a wide variety of models and variables will be tried; this avoids the error of closing in too rapidly on an incorrect or incomplete model. However it does appear that we are now close to agreeing on the right classes of factors to measure. When a number of studies have been performed using the same general programming model and the same definitions of variables, it will be possible to gain a better understanding of programming, and the factors that influence productivity.

Another class of productivity research that has great potential application for language developers and e.d.p. management is related to inter-language studies. This has been sadly neglected. Such studies could be made in a laboratory situation or, more realistically, by measuring actual development work undertaken in the languages being studied.

## References

[1] N. Anderson and B. Shneiderman, Use of Peer Ratings in Evaluating Computer Program Quality, IFSM T.R. No. 20, Department of Information Systems, University of Maryland (June, 1977).

[2] B.W. Boehm, Software and its impact: A quantitative assessment, Datamation, 19, 5 (May, 1973) 48–60.

[3] B.W. Boehm, J.R. Brown and M. Lipow, Quantitative evaluation of software quality, Proc. 2nd International Conference on Software Engineering, San Francisco (1976).

[4] F.P. Brooks, The Mythical Man-Month (Pddison-Wesley, Reading, Massachusetts, 1975).

[5] E. Chrysler, Some basic determinants of computer programming productivity, Communications of the ACM, 21, 6 (June, 1978) 472–483.

[6] L. Chrysler, The impact of program and programmer characteristics on program size, AFIPS National Computer Conference (1978) 581–587.

[7] K. Freburger and V.R. Basili, The software engineering laboratory: relationship equations, Technical Report TR-764, University of Maryland, Computer Science Center (May, 1979).

[3] J.B. Gayle, Multiple regression techniques for estimating computer programming costs, Journal of System Management, 22, 2 (Feb., 1971) 13–16.

[9] T. Gilb, Software Metrics (Winthrop Pub. Inc., Cambridge, Massachusetts, 1976).

[10] M. Halstead, Elements of Software Science (American-Elsevier Inc., New York, 1977).

[11] D.R. Jeffery and M.J. Lawrence, An inter-organizational comparison of programming productivity, Proc. 4th

International Conference on Software Engineering, Munich, ACM and IEEE (1979) 369–377.

[12] J.R. Johnson, A working measure of productivity, Data-mation, 23, 2 (Feb., 1977) 106–110.

[13] J.L. Kirkley, Programmer productivity, Datamation, 23, 5 (May, 1977) 63–69.

[14] E.A. Nelson, Management Handbook for the Estimation of Computer Programming Costs (System Development Corp., Santa Monica, Calif., March, 1967).

[15] L.H. Putnam and A. Fitzsimmons, Estimating software costs, Datamation, 25, 10 (Sept., 1979) 189–198.

[16] H. Sackman, W.J. Erikson and E.E. Grant, Exploratory experimental studies comparing online and offline programming performance, Communication of the ACM, 11, 1 (Jan., 1968) 3–11.

[17] C.E. Walston and C.P. Felix, A method of programming management and estimation, IBM Systems Journal, 16, 1 (Jan-March, 1977) 54–73.

[18] G.F. Weinwurm, ed., On the Management of Computer Programming (Auerbach Publishers, Inc., New York, 1970).
