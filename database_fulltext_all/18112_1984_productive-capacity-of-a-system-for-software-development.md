---
otero_id: 18112
otero_key: "C324NM9V"
title: "Productive capacity of a system for software development"
authors: "Mario Italiani"
year: "1984"
journal: "Information & Management"
doi: "10.1016/0378-7206(84)90049-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Productive Capacity of a System for Software Development \*

Mario Italiani
Istituto di Cibernetica, Università di Milano, Via Viotti 5, I - 20133
Milano, Italy

Economic aspects of software production make it necessary to evaluate the performance of a Systems for Software Development (SSD) in a methodical manner.

In this article, the resources (people, tools, services, etc.) of an SSD are first analyzed using a method based on Conventional Experience and Relative Capacity and introducing a Working Environment Quality Coefficient. The workload of an SSD is also considered, and for this a Workload matrix involving development activities is introduced. Evaluation of the Productive Capacity of an SSD thus takes into account both the resources and the workload of the system.

Keywords: Productive capacity, Relative capacity, Software development, Software Engineering Economics, Work experience, Working environment, Workload.

![](/api/attachments/C324NM9V/fulltext/images/9924fe6d07fcb08808e414d16542581ba8c872d4571be17e7536ba4ed095b09f.jpg)

Mario Italiani received the degree in Mathematics in 1952 from the University of Modena where he spent 5 years as an Assistant Professor of Geometry. He began his activity in the Computer field in 1959 working for Olivetti Electronic Division, where he became the manager of a unit for scientific applications of computers. From 1964 to 1969 he was the manager of the System Software Department in the Olivetti-General Elec tric Company (later General Electric Information Systems Italia) and from 1969 to 1975 he was the Technical Manager of Syntax, one of the largest Software Company in Italy. In 1976 he became a Full Professor of Computer Science at the University of Turin and afterwards at the University of Pavia, where he also was Dean of the Faculty of Engineering. He is currently a Full Professor of Computer Science at the University of Milan. From 1976 to 1979 he was President of the Italian Association for Automating Computing (AICA). His main research interests are in the fields of Computer Assisted Instruction and Performance Evaluation.

## 1. Introduction

The manager of a software operation who wishes to address the problem of evaluating staff productivity usually finds that only vague criteria are available, mainly based on feelings.

There are a lot of useful propositions for programming productivity measurement and software cost estimation in the literature. For example Walston and Felix [8] present some methods for measuring and estimating programming project duration, staff size, and computer cost. Chrysler [4] examines the relationship between processing characteristics of programs and experience characteristics of programmers and program development time. Putnam [7], starting from the Norden model [6], introduces the software equation in order to produce accurate estimates of manpower, costs and times to reach critical milestones of software projects. Jones [5] discusses the unit of measure for assessing program quality and programmer productivity and suggests the use of programming cost units. The volume of Boehm [2] contains a thorough survey of the economic aspects of software engineering and supplies several models and techniques for estimating software development and maintenance costs, for project planning and control, and for software productivity improvement.

On the contrary models and technique for evaluating the performance of a software staff are not widely used, while the problem of Computer Performance Evaluation has been examined by researchers for several years and important results have been obtained. When we consider the economic importance of software today it seems obvious that the similar problem of evaluating the performance of Systems for Software Development should be investigated, starting with consideration of the variables to be measured. A System for Software Development (SSD) is defined here as an organized set of resources (people, tools, services, etc.) devoted to software implementation.

SSD Performance Evaluation requires, by analogy with Computer Performance Evaluation, an analysis of resources and workload. In the following, we will first discuss the problem of measuring the resources of an SSD and subsequently that of characterizing the workload. We conclude with the determination of the Productive Capacity of an SSD.

## 2. Resource Analysis

The resources of an SSD may be considered made up of three major parts:

\- Technical personnel

\- Management, services, and tools

\- Capital

In the following discussion, capital will not be considered, because it has relatively little influence on system performance, at least if we consider performances from a non economic point of view. We try here to define parameters that give a quantitative measure, even though many human activities do not easily fit this mold. However we are convinced that the measurement of intellectual activities will become more and more important in future, and therefore attempts must be made to do this.

## 2.1. Technical Personnel

## 2.1.1. Conventional Experience

The most rudimentary measure of technical personnel working within an SSD is the number of programmers (including senior analysts, system programmers, application programmers, etc.). However, because the contribution of people differs substantially, a meaningful measure requires each person to have a coefficient characterizing capability.

Moreover, it may be possible to group programmers into classes of individuals with homogeneous capability and then give each class a numerical coefficient characterizing the average capability of its members. Such a grouping may be made on the basis of the functions performed, but this may result in inconsistencies because the function is often interpreted differently in different organizations or situations. Therefore a measure based on a parameter such as length of the work experience in the software area seems to be more advisable.

The work experience however should be adjusted by the addition of terms taking into account the level of education and the quality of the experience. The first of these must take account of the fact that an education in Computer Science partly substitutes for work experience, and that education should increase the value of experience, shortening the time needed for acquisition of some skills.

If e is the length of the actual work experience in the software field, in years, and $T_{1}$ , $T_{2}$ the additive terms mentioned above, we may define the Conventional Experience, E, as:

$$
E = e + T _ {1} + T _ {2}.\tag{1}
$$

To determine $T_{1}$ , we assume the base level of experience to be that of a high school graduate ( $T_{1}=0$ ) and hypothesize that the importance of the education level decreases with increase in actual experience. As a first approximation to $T_{1}$ , we may assume a sum of constants such as:

$$
T _ {1} = a _ {0} + \sum_ {i = 1} ^ {n} a _ {i},\tag{2}
$$

where n is the gratest integer lower that the length of the actual work experiences in years, while the values of the constants $a_{i}$ are suggested in Table 1, based on personal experience. $a_{0}$ measures any work experience that can be substituted for education, while the decreasing values of $a_{i}$ ( $i = 1,2,\ldots,n$ ) represent the increase in value of actual work experience as a consequence of a higher level of education. The years over 10 are completely ignored. Of course, the evaluator may consider different kinds of education and the qualifications of specific schools to obtain better results. For term $T_{2}$ we propose the expression:

$$
T _ {2} = b _ {0} + \sum_ {i = 1} ^ {h} b _ {i} m _ {i},\tag{3}
$$

Suggested values for the constants $a_{i}$ (The values have been determined taking into consideration the structure of the Italian schools and therefore they should be adjusted for different school organizations).

<table><tr><td></td><td>HIGH SCHOOL GRADUATION (Not specific curriculum)</td><td>HIGH SCHOOL GRADUATION (specific curriculum)</td><td>UNIVERSITY GRADUATION (Not specific curriculum)</td><td>UNIVERSITY GRADUATION (specific curriculum)</td><td>PHD (specific curriculum)</td></tr><tr><td>i = 0</td><td>0</td><td>1</td><td>0.50</td><td>1.50</td><td>2.50</td></tr><tr><td>i = 1</td><td>0</td><td>0</td><td>0.60</td><td>0.80</td><td>1.00</td></tr><tr><td>i = 2</td><td>0</td><td>0</td><td>0.55</td><td>0.70</td><td>0.90</td></tr><tr><td>i = 3</td><td>0</td><td>0</td><td>0.50</td><td>0.60</td><td>0.80</td></tr><tr><td>i = 4</td><td>0</td><td>0</td><td>0.45</td><td>0.50</td><td>0.70</td></tr><tr><td>i = 5</td><td>0</td><td>0</td><td>0.40</td><td>0.40</td><td>0.60</td></tr><tr><td>i = 6</td><td>0</td><td>0</td><td>0.30</td><td>0.30</td><td>0.50</td></tr><tr><td>i = 7</td><td>0</td><td>0</td><td>0.20</td><td>0.20</td><td>0.40</td></tr><tr><td>i = 8</td><td>0</td><td>0</td><td>0.10</td><td>0.10</td><td>0.30</td></tr><tr><td>i = 9</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.20</td></tr><tr><td>i=10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.10</td></tr><tr><td>i&gt;10</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

where $m_{i}$ are the durations (in years) of the h periods of work experience for which a coefficient $b_{i}$ applies, and $b_{0}$ is a constant that depends on the value of work experience in other fields than software.

## 2.1.2. Distribution of Conventional Experience

However, even if experience, particularly Conventional Experience, is a parameter useful for classifying technical personnel into homogeneous classes, we cannot expect that personnel performance increases indefinitely with time. Therefore, for Conventional Experience it is convenient to fix an upper bound $(E_{x})$ . We shall subdivide the interval $(0, E_{x})$ into k parts, not necessarily equal, and group the N technical personnel of an SSD into k classes $S_{i}$ ( $i = 1, 2, \ldots, k$ ), based on this subdivision. Programmers with Conventional Experience that would be greater than $E_{x}$ will be assigned to the class $S_{k}$ .

The number of programmers in class $S_{i}$ will be indicated by $p_{i}N$ where the $p_{i}$ ( $i=1,2,\ldots,k$ ) are

such that:

$$
\sum_ {i = 1} ^ {k} p _ {i} = 1,\tag{4}
$$

while $\bar{E}_{i}$ ( $i=1,2,\ldots,k$ ) will indicate the average Conventional Experience of the programmers in the class $S_{i}$ . The average Conventional Experience of the technical personnel is thus:

$$
\overline {{{E}}} = \sum_ {i = 1} ^ {k} \overline {{{E}}} _ {i} p _ {i}.\tag{5}
$$

This is, of course, scarsely a meaningful index, but some indicators may be derived from an analysis of the distribution of the Conventional Experience in the organization.

The distribution may depend on several factors, such as the historical evolution of the team, the quality of their prior work experience, the location of their office, the conditions of the market, the Company policy on technical salaries, education, incentives, etc., and the quality of the management. However, we assume that a careful management tries to avoid both bottom-heavy structures (generally technically weak) and top-heavy structures, which may present career problems.

Some rudimentary indices for the evaluation of Conventional Experience distribution in an SSD may be the location of the 50th and 75th percentiles.

If the value of the 50th percentile for instance is less than three or four units of conventional experience, we may suspect to find a bottom-heavy structure, while a value of the 75th percentile higher than 12–14 units suggests a top-heavy structure [1].

## 2.1.3. Standard Productive Capacity

The subdivision of technical personnel in an SSD into classes is meaningful if we can associate a value expressing productivity of the personnel in each class. This value may be the number of source instructions delivered in a given time interval [2] by each programmer class.

Productivity depends on several factors, including personal capability, experience, the project size and difficulty, the organization of the SSD, and the methods and tools used.

Let us consider standard projects, namely those whose size and difficulty are average, developed in standard condition (we will define these terms carefully later).

Let the Standard Productive Capacity C of a programmer be the expected number of source instruction delivered per month for standard projects in standard conditions. Moreover, for technical personnel of average capability, the Standard Productive Capacity is assumed to be a function of Conventional Experience only:

$$
C = C (E)
$$

Experience shows that the function $C(E)$ , increases with $E$ . The rate of increase, however, tends to zero and therefore we may suppose that, for $E \geqslant E_x$ , the function $C(E)$ is practically constant ( $C_x$ ).

The Relative Capacity $C_{r}(E)$ is defined as the ratio between the Standard Productive Capacity $C(E)$ of a programmer with Conventional Experience E and the maximum Standard Productive Capacity $C_{x}=C(E_{x})$ .

On the basis of numerous observations the behaviour of the Relative Capacity $C_{\mathrm{r}}(E)$ seems to be that shown in fig. 1: a typical learning curve. At present we do not have an analytical representation of the function $C_{\mathrm{r}}(E)$ ; we intend to perform research on this in future. Its form is, however, in three parts. The first part has negative Relative Capacity up to a threshold value $E_{T}$ . This behaviour results from the inevitable reduced production due to the addition of inexperienced personnel in an SSD.

The threshold $(E_{\mathrm{T}})$ , of about one unit of Conventional Experience, concludes the apprenticeship phase.

During the second period (the growth phase) the Relative Capacity rapidly rises, while its derivative $C_{\mathrm{r}}^{\prime}(E)$ , reaches a maximum and then decreases again. If we conventionally fix the end of the growth phase when $C_{\mathrm{r}}(E)$ assumes the value 0.70, the phase is about 3 to 4 units of Conventional Experience long.

Finally, the third period (the maturity phase) has a much slower increase of Relative Capacity, which tends to 1. The behaviour of the function $C_{r}(E)$ during the maturity phase does not mean that technical personnel of high experience cannot increase their performances. Most programmers, after productive experience, tend to move to other activities (managerial, etc.).

Let $C_{\text{TS}}$ be the Total Standard Productive Capacity of the whole SSD of $N$ programmers subdivided into $k$ classes $S_i$ ( $i = 1,2,\ldots,k$ ) of average Conventional Experiences $\overline{E}_{i}$ ( $i=1,2,\ldots,k$ ), working on standard projects in standard conditions. Then:

![](/api/attachments/C324NM9V/fulltext/images/925f1c198243e743d5023fc52bfea2bf36e2ba1d2ccaa60aa25660ca5b253dad.jpg)  
Fig. 1. Behaviour of Relative Capacity $C_{R}$ as a function of Conventional Experience E.

$$
C _ {\mathrm{TS}} = C _ {x} N \sum_ {i = 1} ^ {k} p _ {i} C _ {\mathrm{r}} (\overline {{{E}}} _ {i})\tag{6}
$$

When the capabilities of the technical personnel differ from the average, a coefficient $V_{i}$ (the Specific value) may be given to each class $S_{i}$ .

Values of $V_{i}$ less than 1 are used when the capabilities of programmers are considered below average, and greater than 1 when above average. We suggest that the values of $V_{i}$ should range from 0.5 to 1.5.

With the introduction of coefficients $V_{i}$ expression (6) becomes:

$$
C _ {\mathrm{TS}} = C _ {x} N \sum_ {i = 1} ^ {k} p _ {i} V _ {i} C _ {\mathrm{r}} \left(\bar {E} _ {i}\right).\tag{7}
$$

## 2.2. Management, Services, and Tools

Measurement of the quality of the management, services, and tools of an SSD is not easy and therefore, to a first approximation, we must be satisfied with rough measures. One relevant aspect of management quality is the capability to motivate the technical personnel. This may be indirectly evaluated by means of Personnel Turnover, which however is affected by other factors (not necessarily controlled by management).

The annual turnover index may be defined as the ratio $T = N_{d}/N$ , where $N_{d}$ is the number of programmers who left during the year and N the average number of programmers during the same period. A turnover index between 0.05 and 0.20 may be considered normal. Values greater than 0.20 are clearly anomalous; while values less than 0.05 may cause doubts on the team structure (becoming top-heavy), but do not necessarily imply poor motivation of the technical personnel.

Another aspect of the quality of management, services, and tools is the Working Environment Quality, which may be evaluated through indices related to the facilities and tools of the SSD, such as:

a) the ratio of the number of auxiliary personnel (secretaries, typists, operators, clerks, etc.) to the number of technical personnel (N);

b) the percentage time of technical personnel dedicated to seminars and training (excluding the initial training) to the total;

c) the average office space for each technical person;

d) the number of volumes (books, congress proceedings, scientific reviews, technical manuals) in the SSD library per Technical person;

e) the number of daily compilations and text runs per person (a low value may indicate inadequate computing resources; a high value may show a lack of effective development methods);

f) the number of available terminals per technical person.

Many other elements affect the Working Environment Quality but are difficult to measure; examples are:

\- enforcement of adequate procedures for planning and control;

\- enforcement of procedures for cost control;

\- availability of an updated historical project file;

\- enforcement of documentation standards;

\- use of effective design, programming, and testing methods;

\- availability of adequate tools for the automatic management of programs and data.

We believe that an evaluation of the indices and other elements makes it possible, even if on the basis of discretionary criteria, to assign a value of the Working Environment quality Coefficient (Q).

It probably ranges from 0.5 to 1.5, where 1.0 corresponds to an average quality of the working environment: the standard conditions. Values less than one are assigned when the Working Environment Quality is considered inadequate.

The Working Environment Quality Coefficient may be used as a multiplicative corrector of the Standard Productive Capacity.

## 3. The Workload of an SSD

## 3.1. Workload Components

The workload of an SSD is the set of tasks of the SSD. One functional classification of the workload activities may be:

\- Development

Maintenance

\- External Activities

Development includes those activities devoted to the implementation of new software projects, both by external and by internal commitment, while Maintenance refers to activities linked with the removal of bugs from a project and with the updating or upgrading of a software product.

Table 2  
A Workload Matrix.

<table><tr><td></td><td colspan="4">LEVEL OF DIFFICULTY</td></tr><tr><td rowspan="6">SIZE</td><td></td><td>LOW</td><td>MEDIUM</td><td>HIGH</td></tr><tr><td>Below 4K</td><td> $n_{11} = 8$  $(d_{11} = 2800)$ </td><td> $n_{12} = 4$  $(d_{12} = 2950)$ </td><td> $n_{13} = 1$  $(d_{13} = 1900)$ </td></tr><tr><td>4K TO 16K</td><td> $n_{21} = 3$  $(d_{21} = 8700)$ </td><td> $n_{22} = 5$  $(d_{22} = 10500)$ </td><td> $n_{23} = 0$ </td></tr><tr><td>16K TO 64K</td><td> $n_{31} = 2$  $(d_{31} = 30400)$ </td><td> $n_{32} = 3$  $(d_{32} = 42300)$ </td><td> $n_{33} = 1$  $(d_{33} = 50800)$ </td></tr><tr><td>64K TO 256K</td><td> $n_{41} = 0$ </td><td> $n_{42} = 1$  $(d_{42} = 135700)$ </td><td> $n_{43} = 0$ </td></tr><tr><td>OVER 256K</td><td> $n_{51} = 0$ </td><td> $n_{52} = 0$ </td><td> $n_{53} = 1$  $(d_{53} = 315000)$ </td></tr></table>

External Activities are those not directly productive, such as those of programmers in sales support or to user assistance.

However attendance at seminars or training courses should not be considered a workload component; in fact, this activity, which absorbs SSD resources, must be considered a necessary overhead. On the other hand, the value of the maximum Standard Productive Capacity $C_{x}$ in Eqs. (6) and (7) takes training into account.

A first elementary characterization of the workload consists of determining the percentages of the Total Standard Productive Capacity $C_{TS}$ devoted to Development, Maintenance, and External Activities ( $q_{s}$ , $q_{m}$ , $q_{e}$ respectively).

These values are useful indicators. If $q_{e}$ is greater than 0.10, management should beware a corresponding reduction in production could be expected in the near future.

Moreover, a value of $q_{d}$ much lower than $q_{m}$ (as frequently happens in a computer user organization) may point to lack of motivation of technical personnel due to high degree of maintenance activity.

## 3.2. Development

In order to characterize the development workload we develop a Workload Matrix of projects with p lines and q columns. The lines are a classification of the projects on the basis of their size, expressed in number of source statements; the columns are a classification of the level of difficulty. Each element $n_{ij}$ ( $i=1,2,\ldots,p$ ; $j=1,2,\ldots,q$ ) of the Workload Matrix contains the number of projects in the category, developed within the SSD in the given time interval.

We may also associate with this the average size $(d_{ij})$ of the projects.

Table 2 shows an example of Workload Matrix with three levels of difficulty (low, medium, high) and five classes of size.

With each element, we may also associate a constant $(r_{ij})$ which is the ratio of the Productive Capacity of a programmer with high Conventional Experience (greater or equal to the upper bound

Table 3
A Relative Capacity Matrix.

<table><tr><td></td><td colspan="4">LEVEL OF DIFFICULTY</td></tr><tr><td rowspan="6">SIZE</td><td></td><td>LOW</td><td>MEDIUM</td><td>HIGH</td></tr><tr><td>BELOW 4K</td><td>1.83</td><td>1.41</td><td>1.10</td></tr><tr><td>4K TO 16K</td><td>1.72</td><td>1.18</td><td>0.83</td></tr><tr><td>16K TO 64K</td><td>1.61</td><td>1</td><td>0.63</td></tr><tr><td>64K TO 256K</td><td>1.49</td><td>0.85</td><td>0.48</td></tr><tr><td>OVER 256K</td><td>1.30</td><td>0.72</td><td>0.36</td></tr></table>

Table 4

$E_{x}$ ) on projects in the class to the Productive Capacity of the same programmer on standard projects. The matrix of the constants $r_{ij}$ will be called Relative Capacity Matrix. An example is given in Table 3 where we assume a standard project of medium difficulty and size between 16K and 64K source statements.

The expression:

$$
W = \frac {\sum_ {i = 1} ^ {p} \sum_ {j = 1} ^ {q} d _ {i j} n _ {i j} r _ {i j}}{\sum_ {i = 1} ^ {p} \sum_ {j = 1} ^ {q} d _ {i j} n _ {i j}}\tag{8}
$$

then gives a Workload Index, which may be used as a multiplicative corrector of the Standard Productive Capacity (for development activities).

W typically produces values greater than one if the workload consists mainly of small projects with low-medium difficulty and values less than one if the workload consists mainly of large projects with medium-high difficulty.

## 4. Productive Capacity

If we limit ourselves to considering development activities, we may determine the Monthly Productive Capacity $C_{M}$ of an SSD, using Eq. (7), the Working Environment Quality coefficient introduced in section 2.2, and the Workload Index introduced in section 3.2. We then obtain the following expression:

Data collected for the example.

<table><tr><td>Class</td><td> $p_i$ </td><td> $\overline{E}_i$ </td><td>C  $(\overline{E}_i)$ </td><td> $V_i$ </td></tr><tr><td> $S_1 (0 < E ≤ 2)$ </td><td>0.235</td><td>1.19</td><td>0.08</td><td>1</td></tr><tr><td> $S_2 (2 < E ≤ 4)$ </td><td>0.118</td><td>2.15</td><td>0.36</td><td>1</td></tr><tr><td> $S_3 (4 < E ≤ 6)$ </td><td>0.176</td><td>5.17</td><td>0.74</td><td>1</td></tr><tr><td> $S_4 (6 < E ≤ 8)$ </td><td>0.118</td><td>7.29</td><td>0.90</td><td>1</td></tr><tr><td> $S_5 (8 < E ≤ 10)$ </td><td>0.118</td><td>8.79</td><td>0.92</td><td>1</td></tr><tr><td> $S_6 (10 < E)$ </td><td>0.235</td><td>10.70</td><td>0.96</td><td>1</td></tr></table>

$$
C _ {\mathrm{M}} = C _ {x} N Q q _ {\mathrm{d}} W \sum_ {i = 1} ^ {k} p _ {i} V _ {i} C _ {\mathrm{r}} \left(\bar {E} _ {i}\right).\tag{9}
$$

If we recall that N is the number of programmers belonging to the SSD under consideration, while $C_{x}$ is the Standard Productive Capacity of a programmer with Conventional Experience greater or equal to the upper bound $E_{x}$ , the expression:

$$
I _ {\mathrm{c}} = Q q _ {\mathrm{d}} W \sum_ {i = 1} ^ {k} p _ {i} V _ {i} C _ {\mathrm{r}} (\bar {E} _ {i})\tag{10}
$$

may be considered as a global Characteristic Index of resources and workload.

The value supplied by Eq. (9) may give useful indications when compared with experimentally measured productivity data.

Indeed comparison may locate problem areas and help in choosing a possible corrective action.

## 5. Example

Experience and levels of education of 34 programmers devoted to development activities ( $q_{d} = 1$ ) in a Software house were surveyed. Results are shown in Table 4.

Table 5
Workload matrix for the example.

<table><tr><td></td><td colspan="4">LEVEL OF DIFFICULTY</td></tr><tr><td rowspan="2">S</td><td></td><td>LOW</td><td>MEDIUM</td><td>HIGH</td></tr><tr><td>BELOW 4K</td><td> $n_{11} = 0$ </td><td> $n_{12} = 0$ </td><td> $n_{13} = 0$ </td></tr><tr><td>I</td><td>4K TO 16K</td><td> $n_{21} = 2$  $d_{21} = 7111$ </td><td> $n_{22} = 0$ </td><td> $n_{23} = 0$ </td></tr><tr><td>Z</td><td>16K TO 64K</td><td> $n_{31} = 4$  $d_{31} = 33710$ </td><td> $n_{32} = 0$ </td><td> $n_{33} = 0$ </td></tr><tr><td rowspan="2">E</td><td>64K TO 256K</td><td> $n_{41} = 0$ </td><td> $n_{42} = 0$ </td><td> $n_{43} = 0$ </td></tr><tr><td>OVER 256K</td><td> $n_{51} = 0$ </td><td> $n_{52} = 0$ </td><td> $n_{53} = 0$ </td></tr></table>

The Working Environment Quality Coefficient Q and the specific values $V_{i}$ have been fixed to one. All the projects of these programmers were business application of low difficulty and their analysis led to the Workload Matrix of table 5 and to the value W=1.620 for the Workload Index. As a consequence, the value of the Characteristic Index $I_{c}$ (from Eq. 10) was 1.024.

If we assume $C_{x}=350$ , the Monthly Productive Capacity of the SSD may be estimated at 12185 delivered instructions per month, with an average Productive Capacity of about 358 delivered lines of instructions per man-month. The actual productivity was measured as a mean of 390 delivered instructions per man-month.

## References

[1] G.C. Baldovini and M. Italiani, “Dinamica del Personale in una Società di Software”, Sviluppo e Organizzazione (Milano, Italy), n. 38, Oct. 1976, pp. 21–24.

[2] B.W. Boehm, Software Engineering Economics, Prentice Hall, Englewood Cliffs, N.J., 1981.

[3] F.P. Brooks, The Mythical Man-Month, Addison Wesley, Reading, MA, 1975.

[4] E. Chrysler, “Some Basic Determinants of Computer Programming Productivity”, Comm. ACM, June 1978, pp. 472–483.

[5] T.C. Jones, "Measuring programming quality and productivity", IBM System Journal 17, 1, 1978, pp. 39–63.

[6] S. Norden, “Useful tools for project management” in Management of Production, M.K. Starr ed., Penguin, Baltimore, MD, 1970.

[7] L.H. Putnam, “A General Empirical Solution to the Macro Software Sizing and Estimating Problem”, IEEE Transaction on Software Engineering, 4, 4, 1978, pp. 345–361.

[8] C.E. Walston, C.P. Felix, “A method of programming measurement and estimation” IBM System Journal, 16, 1, 1977, pp. 54–73.
