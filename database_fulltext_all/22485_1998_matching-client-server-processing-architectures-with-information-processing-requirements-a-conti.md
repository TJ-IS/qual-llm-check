---
otero_id: 22485
otero_key: "6C5D4QDF"
title: "Matching client/server processing architectures with information processing requirements: A contingency study"
authors: "Murugan Anandarajan; Bay Arinze"
year: "1998"
journal: "Information & Management"
doi: "10.1016/s0378-7206(98)00064-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Matching client/server processing architectures with information processing requirements: A contingency study

Murugan Anandarajan $^{*}$ , Bay Arinze $^{1}$

Department of Management, Drexel University, Philadelphia, PA 19104, USA

Received 19 June 1997; accepted 28 February 1998

## Abstract

The 1990s are witnessing the rapid growth of client/server (C/S) computing, but for an organization to benefit from a C/S model, it should ensure that the processing architecture matches its information needs. Researchers have suggested that organizations moving to this model should identify their information requirements, and then determine the appropriate architectures to support them.

This study utilizes information processing theory to examine the match between an organization's information processing requirements and its C/S architectures. The independent variables in this study are task characteristics, and the processing architectures. The dependent variable is effectiveness. The data for this study was obtained from C/S managers and users in a variety of industries, through a combination of archival data, telephone interviews, and a mailed survey. It was analyzed using hierarchical regression. The results indicate that an appropriate match between task characteristics and C/S processing architectures is an important determinant of system effectiveness. © 1998 Published by Elsevier Science B.V. All rights reserved

Keywords: Client–server computing; Client–server processing architectures; IT match; Task characteristics; Information processing theory; Contingency theory

## 1. Introduction

Client/server (C/S) computing is an important topic in the field of information systems today. Not since the evolution of batch to on-line systems have we witnessed such a fundamental shift. In 1992, Benjamin and Blunt [1] predicted that C/S computing would be one of the major future application architectures.

Indeed, according to a survey in 1992, about 55–60% of all new applications used in the US were based on a C/S model.

C/S computing has been defined in various ways; for example, Elbert and Martyna [11] and Dewire [7] define the concept from a business application development standpoint. For the purpose of our study we define C/S systems from a processing architecture perspective:

They comprise of a set of processing architectures that partition computing processes among multiple systems. Application front-ends reside on client, while back-ends reside on servers. The systems cooperate to process a single unified task.

The need for a match between an organization's information processing requirements and its architecture has been identified by many practitioners. Organizations transitioning to C/S systems will benefit from identifying the information requirements of their users prior to selecting the architecture [4]. There are many types of C/S processing architectures available to developers, each having its strengths and weaknesses; hence determining the most appropriate processing architecture for an organization's information needs is difficult [10]. Failure to identify and match the architecture best suited to a given set of information processing requirements has resulted in many non-performing or over-budget projects.

The purpose of this study is to examine how a C/S processing architecture can be matched successfully to an organization's information processing needs; the appropriate match between task and technology will result in an effective system.

## 2. Background of C/S systems

Contemporary organizations need to be able to react quickly to take advantage of business opportunities and to be the first to market a new product or service. The flexibility to maneuver can be provided by an information systems architecture that can be expressed in terms of ‘reach and range’ [23]. Reach refers to who is able to receive data and range defines what information can be shared. By expanding these, an organization can become more flexible and thus empower its employees. A C/S system provides these capabilities [2].

The emergence of C/S computing can be attributed to a combination of factors:

Technical factors: Several major technical trends have converged to make C/S computing possible, such as faster and miniaturized hardware components and open standards that create portable, scalable, and inter-operable systems. Software trends such as graphical user interfaces (GUIs), fourth-generation programming languages and the development of Componentware have also helped in its evolution.

Economic factors: Processing on desktop workstations instead of mainframes has reduced computational cost processing substantially $[32]$ . The use of open system technology is mooted to be 30–50% less expensive than equivalent proprietary technologies. C/S computing generally lowers hardware costs, since it is generally built around open systems. Use of hardware and the adoption of developmental tools, such as Componentware, has led to faster and cheaper application development.

## 2.1. C/S processing architectures

The C/S processing architecture defines the framework for the client as well as the server. These architectures provide a flexibility for developing inexpensive modular applications to meet particular business needs. The three basic resources are:

1. Presentation resources: These are built into all applications and determine how users interact with the system. The functions are typically performed on client machines, such as Windows, X-Windows, or Macintosh front-ends running on microcomputers or workstations.

2. Business rules: These are made up of the different functions of the application, usually coded in a third- or fourth-generation language. The application can be split between the client and the server, depending on each platform's characteristics, such as computing power, the network communication overhead, and the number of clients.

3. Data management: These services include the addition, modification, retrieval, and deletion of data records in the database, including the associated record manipulation.

The allocation of process resources between clients and servers is vital for efficient and effective use of the C/S system. The Gartner Group $[14]$ has proposed a framework that defines five major C/S models based on how the application components are divided between the client and the server. These are briefly described below and illustrated in Fig. 1.

## 2.1.1. Distributed presentation

Here, the presentation resource is split between the client and server. This architecture uses the least amount of client processing power.

![](/api/attachments/6C5D4QDF/fulltext/images/7bbb88d64ce2e18cd50eb047fcb596cd369cf2035a8b807bee274fd9ac971ac7.jpg)  
Fig. 1. Types of C/S processing architectures.

## 2.1.2. Local presentation

This centralizes the business logic and databases on the server, so that it can be easily managed and updated. This is an important architecture for organizations using mission-critical applications that need to ensure data integrity and high data availability.

## 2.1.3. Distributed processing logic

Here, business rules are distributed, being divided between the client and the server. This model provides a more flexible environment for specific business and processing requirements. For example, it allows an order-entry application to store business rules on the server but to off-load data validation checks to the client.

## 2.1.4. Local processing logic

In this, the presentation and the business rules are completely centralized, while the databases reside on the server. This architecture enhances corporate collaboration by enabling access to shared databases by employees and its use in ways pertinent to their department. The model takes advantage of desktop power, off-loading application processing from servers, and making them more efficient and less likely to be plagued by bottlenecks.

## 2.1.5. Distributed data management

This architecture distributes the organization's database between the client and the server, thereby reducing dependency on the latter. However, interrelated data needs to be updated at almost the same time to preserve data integrity. This updating of the databases increases network traffic.

Therefore, since the system is typically utilized by multiple users, issues such as control, and security of the computing resources arise. Thus, the matching of the C/S processing architecture to the users information requirements are imperative.

## 3. Model development

The theoretical foundations for this study stem from the structural contingency perspective, which has been discussed extensively $[6, 9, 13, 18]$ . This makes one very explicit proposition: system performance is not assured by any particular structural design but is contingent on an appropriate match between contextual variables and structural design. From the information-processing view of the organization, task uncertainties give rise to information-processing needs that should be matched by the IS architectural structure. Since the different types of C/S processing architectures vary in their information processing ability, it is important to select the appropriate architecture for the given level of uncertainty.

IS designers are often faced with the dilemma of having to make this match $[3, 12]$ . A match can be defined as “the degree to which the needs, demands, objectives, and/or the structure of one component IS consistent with the needs, demands, objectives, and/or structure of another component” $[36]$ . This match can be then viewed from the interaction perspective $[16, 37]$ . Schoonhoven $[33]$ says: “when contingency theorists assert that there is a relationship between two variables which predicts a third variable, this implies that an interaction exists between the first two variables”. This concept of match has been examined extensively in the IS literature.

Therefore, the research question of this study is whether a match is required between the C/S processing architecture and its task characteristics to achieve effective system performance. This is illustrated in Fig. 2. The dependent variable is C/S system effectiveness. The independent variables are the C/S processing architecture, task analyzability, and task interdependence.

## 3.1. C/S effectiveness

An effective system is one that adds value to the organization. User satisfaction, a commonly used measure of effectiveness $[22]$ , was chosen as the dependent variable in this study, because it captures how well the system meets the needs of the user, in terms of information timeliness, accuracy, and reliability.

## 3.2. C/S processing architectures

In a server-centric architecture, the bulk of the processing is performed on the server; this architecture is suitable for mission-critical or business applications that run the business on a daily basis. If these applications cease to run, the business literally stops; they are typically routine, highly analyzable operations such as order entry, inventory, and point-of-sale systems. A transaction normally involves several steps that could change more than one database and requires the sending of multiple messages around the network. In addition, users at different locations need immediate access to business records more or less simultaneously. All associated data are therefore maintained as current records in a very dynamic database.

![](/api/attachments/6C5D4QDF/fulltext/images/a61eefbe81e821e230e14e11bf35d54c534dddfb0fb4fe950f5c0bc455893240.jpg)  
Fig. 2. Information processing model for task C/S processing architecture.

A client-centric processing architecture is based upon a structure where most of the processing is performed on the client making this architecture more suitable for investigative-type applications, that is, applications that analyze the business. Such applications range from report generators to decision support. According to Tushman [37], such applications are typically characterized by low task analyzability and interdependence. Since investigative applications are designed to support decision makers, they are not usually based on real-time data, but on a replicated subset of the live data; they feature a set of queries and provide manipulation capabilities using SQL functions, such as totaling, reporting, etc. They also allow the user to download the retrieved data into a spreadsheet format for further processing.

## 3.3. Task characteristics

Work by Ingwersen [21] and Mick et al. [29] indicates that task characteristics dictate the information processing needs. Empirical studies by Tushman and Nadler; Liberatore et al. [28]; Ghani [15]; Umanath and Kim [38]; Yadav [40] among others, indicate that task characteristics constitute an important determinant of the information processing needs. Task characteristics have been examined in terms of task analyzability and task interdependence.

Task analyzability is the extent to which there are known procedures that specify the sequence of steps to be followed. Task analyzability has been repeatedly identified as a major determinant of information processing requirements $[24]$ : as a structured set of procedures can be followed to solve the problem. This minimizes uncertainty in and reduces the processing needs. Examples of analyzable tasks include order entry and inventory control. When a task has low analyzability it is difficult to develop formal procedures to aid in decision-making, leading to reliance on heuristics and experience. Findings by Culnan $[5]$ and Daft and Lengel $[6]$ indicate that such tasks bring about higher uncertainty.

The contingency prediction depends on the way that the task context moderates the relationship between information processing and system performance. Since users performing with a low analyzable task deal with greater uncertainty, they require greater information processing and require systems which have greater information processing capability at the point of task execution, that is, front-end. Conversely, tasks with high analyzability have less uncertainty and the organization mandates centralized user architecture, which promotes adherence to business rules as well as eliminating data redundancies and errors. The argument can be summarized in two hypotheses:

H1a: Client-centric C/S processing architectures make a greater contribution to C/S system performance when task analyzability is low.

H1b: Server-centric C/S processing architectures make a greater contribution to C/S system performance when task analyzability is high.

Task interdependence is the degree of collaboration needed among members of the unit while completing a task $[34]$ . It captures the nature of work-flow among the members of the sub-unit or organization and determines the information processing requirements $[20, 26]$ . Some IS applications are essentially standalone systems with little or no interdependence in the task. When the output of one worker becomes the input for another, interdependence exists. Hackathorn and Keen $[19]$ states that (i) Independent decisions are made by decision makers acting in isolation. (ii) Pooled interdependent decisions require interaction between two or more people. (iii) Sequentially interdependent decisions are made in a certain order in which the outputs of one task become the inputs of another.

Managers have to work together in varying degrees. Greater task interdependence requires greater coordination, and greater joint decision-making. Previous research has not identified precise links between interdependence and information processing. However, according to empirical research by Tushman, the level of interdependence reflects the degree to which individuals need to work with others and this communication flow determines the amount of required information. Therefore, for tasks with a low interdependence, the level of information sharing will be minimal with most of the information processing resources in the front-end. The following interaction hypotheses result:

H2a: Client-centric C/S processing architectures make a greater contribution to C/S system performance when task interdependence is low.

H2b: Server-centric C/S processing architectures make a greater contribution to C/S system performance when task interdependence is high.

## 4. Methodology

The unit of analysis in this study is the organizational workgroup. Responses of individual members were aggregated to yield sub-unit level values. Since the task at the sub-unit level is expected to be relatively more homogeneous, the ecological validity of the aggregation of measurements at the sub-unit level is expected to be less of a problem.

## 4.1. Sample and procedure

Two hundred and forty (240) organizations were contacted by phone to discuss their possible participation in our study. Most contacts were precipitated by a published account of the organization's C/S efforts. Following phone interviews, two sets of questionnaires were mailed to 155 organizations that had agreed to participate. The number of questionnaires mailed totaled 198, because some organizations had implemented more than one C/S system. The organizational contact person distributed the research questionnaires. One set was distributed to the C/S manager or a person with in-depth knowledge of the C/S system; the other set was sent to three users in a workgroup that used the C/S system. The workgroups represented all levels of the organization, from upper management to secretarial staff.

Complete sets of surveys were returned from 89 C/S systems in 70 organizations, that is, with a response rate of 45%. Table 1 provides a breakdown of the industries represented in the sample. The C/S applications were classified as either mission-critical or decision-support in nature. Organization size and industry were treated as control variables. Operational measures for each of these variables were obtained from the questionnaire, archival data, or the phone interview.

Table 1  
Breakdown of industries represented in sample

<table><tr><td></td><td>Number of organizations</td><td>Number of C/S systems</td></tr><tr><td>Manufacturing</td><td>18</td><td>22</td></tr><tr><td>Financial services</td><td>3</td><td>12</td></tr><tr><td>Insurance</td><td>4</td><td>9</td></tr><tr><td>Accounting</td><td>3</td><td>4</td></tr><tr><td>Public sector</td><td>4</td><td>9</td></tr><tr><td>Commercial</td><td>15</td><td>23</td></tr><tr><td>Education</td><td>2</td><td>2</td></tr><tr><td>Utility</td><td>5</td><td>5</td></tr><tr><td>Other</td><td>2</td><td>3</td></tr><tr><td>Totals</td><td>56</td><td>89</td></tr></table>

## 4.2. Independent variable

The C/S manager was given a brief description of the resources of the C/S processing architectures, with the five C/S architectures. The C/S manager was then asked to select the architecture that best represented their system.

Task analyzability was measured using the four items from Withey et al. [39]; this assesses the degree of task analyzability of the work task situation. Its items include:

"To what extent is there a clearly known way to perform the major types of work you normally encounter?";

"To what extent is there a clearly defined body of knowledge of the subject matter that can guide you in doing your work?";

"To what extent is there an understandable sequence of steps that can be followed in doing your work?"; and

"To what extent can you actually rely on established procedures and practices to do your work?"

This instrument has been extensively tested by researchers, (e.g., [25, 27]). All its items are measured on a five-point Likert scale, where 1=Very Little; 3=Some Extent; 5=Very Much. The measure for the variable was the mean of the responses to the four items, with the possible range of scores for task analyzability ranging from 4 (low) to 20 (high).

Task interdependence was measured on a single item scale from a questionnaire developed by Mohr [30]. The C/S system users were asked whether the tasks were performed independently of others or whether it was a pooled or sequential task.

Table 2  
Means, standard deviation, and ranges of variables (N=89)

<table><tr><td></td><td>No of items</td><td>Cronbach alpha</td><td>Interpretation as value increases</td><td>Mean</td><td>Standard deviation</td><td>Range</td></tr><tr><td colspan="7">Independent variables</td></tr><tr><td>Task analyzability (ANATSK)</td><td>4</td><td>0.91</td><td>low–high</td><td>2.98</td><td>0.76</td><td>1.00–5.00</td></tr><tr><td>Task interdependence (INDTSK)</td><td>1</td><td>—</td><td>less–more</td><td>1.50</td><td>0.64</td><td>1.00–3.00</td></tr><tr><td>C/S architecture (ARCH)</td><td>1</td><td>—</td><td>less–more</td><td>3.00</td><td>1.31</td><td>1.00–5.00</td></tr><tr><td colspan="7">Dependent variable</td></tr><tr><td>C/S effectiveness (SATIS)</td><td>12</td><td>0.74</td><td>low–high</td><td>3.01</td><td>0.61</td><td>1.00–5.00</td></tr></table>

## 4.3. Dependent variable

The study used an instrument developed by Doll and Torkzadeh [8] to measure C/S performance. Although this instrument was developed for the end-user computing environment, its wording makes it appropriate for most computer applications [35]. The instrument of items such as

“I am satisfied with the response time in obtaining results from the C/S system”;

"As a result of the C/S system, more relevant information has been made available to me for decision-making"; and

"The C/S system has led me to greater use of analytical aids in my decision-making".

The instrument consists of 12 items measured on a five-point Likert-type scale, where 1=almost never; and 3=about half of the time; 5=almost always; it measures user satisfaction in term of systems content, format, accuracy, ease of use, and timeliness.

## 4.4. Data analysis

In order to examine the underlying structure of the multi-item measures, a principal components factor analysis with a varimax rotation was performed on groups of the questionnaire items. The minimum eigenvalue for which a factor was retained was specified as 1.0 and items that loaded with a value of 0.6 or greater on only one factor were considered for inclusion in the measure. Table 2 provides a summary of descriptive statistics. The Pearson correlation matrix shown in Table 3, suggests that a number of correlations were significant.

The hypotheses examine the moderating effect of the C/S architecture on the relationship between information processing tasks on C/S performance. Hierarchical regression analysis was employed to examine significant interactions between the task characteristics (task analyzability, and task interdependence), C/S processing architecture, and user satisfaction. A statistically significant coefficient for the multiplicative interaction term would support the interaction interpretation for the concept of matching $[38]$ : we used the unstandardized coefficients in the regression analysis to avoid the problem of multicollinearity. Each of the hypotheses was tested with equations of the following form:

Table 3  
Intercorrelation matrix

<table><tr><td></td><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>Industry</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Organizational size</td><td>0.07</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>C/S architecture</td><td> $0.25^a$ </td><td> $-0.43^c$ </td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>4</td><td>Task analyzability</td><td>0.00</td><td> $0.28^a$ </td><td> $-0.41^b$ </td><td>1.00</td><td></td><td></td></tr><tr><td>5</td><td>Task interdependence</td><td>-0.20</td><td> $0.38^b$ </td><td> $0.45^b$ </td><td> $0.26^a$ </td><td>1.00</td><td></td></tr><tr><td>6</td><td>C/S effectiveness</td><td>-0.21</td><td> $-0.47^c$ </td><td> $0.33^a$ </td><td>0.03</td><td> $-0.37^b$ </td><td>1.00</td></tr></table>

N=89.  
$^{a}$ p<0.05.  
$^{b}$ p<0.01.  
$^{c}$ p<0.005.

$$
Y = \beta_ {0} + \beta_ {1} S _ {\mathrm{i}} + \beta_ {2} T _ {\mathrm{i}} + \beta_ {3} S _ {\mathrm{i}} * T _ {\mathrm{i}} + \varepsilon_ {\mathrm{i}}\tag{1}
$$

where $S_{i}=C/S$ architectures, $T_{i}=$ each of the task characteristics, $S_{i}*T_{i}=$ interaction between architectures and task characteristics, and Y=response variable.

## 5. Results

The interpretation of Eq. 1 is limited to the interaction term $\beta_{3}$ , since the aim of the study is to examine the match between the task characteristics and C/S processing architectures. Table 3 summarizes the findings of the hierarchical regression. In model 1 of the regression analysis, the dependent variable was regressed on industry and organization size, C/S processing architecture, and task analyzability. The model was significant with a $R^{2} = 0.25$ . In model 2, the interaction term (Task analyzability\*C/S architecture) was in the regression analysis. The regression coefficient for the hypothesized interaction term between task analyzability and C/S processing architecture was significant. In addition, the overall model was significant at the 0.01 level with $43\%$ of the variation in C/S effectiveness explained (Table 4).

To determine the form of the moderating effects and to test the specific relationships proposed in the first hypothesis, subgroup analyses were performed. A significant relationship is shown only for client-centric C/S processing architectures ( $\beta=0.45$ , p<0.001), when task analyzability is regressed on C/S effectiveness. The difference in beta coefficients was significant (p<0.01) (Table 5).

A similar hierarchical regression procedure was conducted to test hypothesis 2. The regression coefficient for the hypothesized interaction term between task interdependence and C/S processing architecture was significant. Because of this a subgroup analysis was conducted. A significant relationship is shown only for client-centric C/S processing architectures $(\beta=0.24, p<0.001)$ , when task interdependence is regressed on C/S success. The difference in beta coefficients is significant $(p<0.01)$ .

Hierarchical regression results - Task analyzability (Dependent variable C/S effectiveness)

<table><tr><td>Step</td><td>Variables</td><td> $\beta$  Model 1</td><td> $\beta$  Model 2</td></tr><tr><td></td><td>Control factors</td><td></td><td></td></tr><tr><td rowspan="2">1</td><td>Industry</td><td>-0.302</td><td> $-0.274^a$ </td></tr><tr><td>Organization size</td><td>-0.387</td><td> $-0.393^a$ </td></tr><tr><td>2</td><td>C/S processing architecture</td><td>0.461</td><td>1.450</td></tr><tr><td>3</td><td>Task analyzability</td><td> $0.393^a$ </td><td>0.916</td></tr><tr><td rowspan="4">4</td><td>Task  $\text{analyzability}^{\text{a}}$  C/S Processing architecture</td><td> $-0.849^a$ </td><td></td></tr><tr><td>Overall  $R^2$ </td><td>0.25</td><td>0.43</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.23</td><td>0.39</td></tr><tr><td>N=89</td><td></td><td></td></tr><tr><td colspan="4"> $^a p<0.05.$  $^b p<0.01.$  $^c p<0.001.$ </td></tr></table>

Hierarchical regression results – Task interdependence (Dependent variable C/S success)

<table><tr><td>Step</td><td>Variables</td><td> $\beta$  Model 1</td><td> $\beta$  Model 2</td></tr><tr><td></td><td colspan="3">Control factors</td></tr><tr><td rowspan="2">1</td><td>Industry</td><td> $-0.275^a$ </td><td> $-0.203^a$ </td></tr><tr><td>Organization size</td><td> $-0.291^a$ </td><td> $-0.303^a$ </td></tr><tr><td>2</td><td>C/S processing architecture</td><td>0.159</td><td>1.080</td></tr><tr><td>3</td><td>Task interdependence</td><td> $-0.243^a$ </td><td> $0.498^a$ </td></tr><tr><td rowspan="4">4</td><td>Task interdependence  $^a$  C/S Processing architecture</td><td> $-0.945^b$ </td><td></td></tr><tr><td>Overall  $R^2$ </td><td>0.25</td><td>0.42</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.23</td><td>0.39</td></tr><tr><td>N=89</td><td></td><td></td></tr></table>

$^{a}$ p<0.05.  
$^{b}$ p<0.01.  
$^{c}$ p<0.001.

## 6. Discussion

The interaction term of task analyzability and C/S processing architecture exhibits a good match, leading to user satisfaction with the C/S system. This supports the symmetrical notion of the contingency relationship; that is, increased task analyzability resulted in greater workgroup satisfaction with a server-centric system than with a client-centric type of processing architecture. On the other hand, decreased task analyzability resulted in greater workgroup satisfaction from a client-centric system than with a server-centric system. These results confirm the theorized direction and effect of the interaction term. This study's finding that highly analyzable tasks are best implemented on a server-centric C/S system is hardly surprising.

The interaction term between task interdependence and C/S processing architecture was significant. This implies that a good match between the two variables is required for users to be satisfied with a C/S system.

## 7. Implications and summary

Organizations today face uncertain and unpredictable business environments as rapid changes in technology impose many changes. This stretches the limits of financial and managerial resources. An important determinant of the effectiveness of an organization's information processing system is its match between task and technology [17]. Therefore, organizations must develop C/S system designs that permit them to react promptly and adequately to uncertain environmental conditions if they are to survive and prosper [31].

Our research is, of course, limited by the choice of variables in the model and by the measures used for them: while it would have been preferable to obtain objective measures for many of the variables, this is impossible. Instead, it was necessary to rely on perceived measures of user satisfaction instead of an objective measure.

Some other variables could have been included in the model: these include contextual variables such as environmental uncertainty and user characteristics. In addition, industry and organizational size were treated as method variables.

This paper is the first major study on C/S systems from a processing architecture perspective, where different processing architectures are identified and linked to business activities. It also addresses a richer alternative to the unilateral research for structural variables that enhance performance, while adding to the theoretical understanding of the task-technology match by adopting a theory from a referent discipline.

There are some implications for managers, who should consider the task portfolio of the workgroup before determining a processing architecture of the C/S system. Practitioners should aim at developing architectures that best match the combined task characteristics of the workgroup.

This study clearly shows that the match between task characteristics and structural variables is an important consideration in developing a C/S system. Computer systems provided to workgroups should be based on individual and workgroup task characteristics, rather than on a uniform organization-wide policy. Practitioners should thus be cautious about developing C/S systems. A C/S processing architecture which may have worked well in one environment may not be the most appropriate for another.

## Acknowledgements

The authors wish to acknowledge Dr. E.H. Sibley for his extensive editing of this paper

## References

[1] Robert J. Benjamin, J. Blunt, Critical IT issues: The next ten years, Sloan Management Review (1992) 7–19.

[2] B.H. Boar, Implementing Client/Server Computing, McGraw-Hill, 1994.

[3] D.J. Campbell, Task complexity: A review and analysis, Academy of Management Review 13(1), 1988, pp. 40–52.

[4] D.N. Chorafas, Systems Architecture and Systems Design, New York, NY, McGraw-Hill, 1989.

[5] M.J. Culnan, The intellectual structure of management information systems. 1972–1982: A co-citation analysis, Management Science 32, 1986, pp. 156–172.

[6] R.L. Daft, R.H. Lengel, Organizational information requirements, media richness and structural design, Management Science 32(5), 1986, pp. 554–571.

[7] D.T. Dewire, Client/Server Computing, McGraw-Hill, 1994.

[8] W.J. Doll, G. Torkzadeh, The measurement of end-user computing, MISQ 12(2) 259–276.

[9] R. Drazin, A. Van de Ven, Alternate forms of fit in contingency theory, Administrative Science Quarterly 30(4), 1985, pp. 514–539.

[10] W. Eckerson, Client server architectures: Finding the best one for your collaborative computing needs, Network World (1995) 18–23.

[11] B. Elbert, B. Martyna, Client/Server Computing, Artech House Boston, 1993.

[12] R. Espejo, J. Watt, Information and/management, organization and managerial effectiveness, Journal of the Operational Research Society 39(1), 1988, pp. 7–14.

[13] J. Galbraith, Organization Design, Addison-Wesley, Reading, MA, 1977.

[14] Gartner Group, Best C/S practices, Datamation (1994) 24–32.

[15] J.A. Ghani, Task uncertainty and the use of computer technology, Information and Management (1992) 69–76.

[16] A. Ginsberg, N. Venkatraman, Contingency perspectives of organizational strategy: A critical review of the empirical research, Academy of Management Review 10, 1985, pp. 421–434.

[17] D. Goodhue, R. Thompson, Task-technology fit and individual performance, MISQ 19(2) 213–237.

[18] D.L. Goodhue, J.A. Quillard, J.F. Rockart, Managing the data resources: A contingency approach, MIS Quarterly 12(3), 1988, pp. 373–392.

[19] R.D. Hackathorn, P.G.W. Keen, Organizational strategies for personal computing in decision support systems, MIS Quarterly 5(1), 1981, pp. 15–55.

[20] L. Hrebiniak, Job technology, supervision, and work-group structure, Administrative Science Quarterly 19, 1974, pp. 395–410.

[21] P. Ingwersen, Information Retrieval Interaction, 1992, Taylor Graham, London.

[22] B. Ives, M. Olsen, J. Baroudi, The measurement of user information satisfaction, Communications of the ACM 24(1)785–793.

[23] P.G.W. Keen, Shaping the Future: Business Design through Information Technology. Harvard Business School Press, Boston, MA, 1991.

[24] P.G.W. Keen, M. Scott-Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[25] R.T. Keller, Technology-information processing fit and the performance of R and D project groups: A test of contingency theory, Academy of Management Journal 37(1) 167–179.

[26] M.N. Kiggundu, Task interdependence and the theory of job design, Academy of Management Review 6(1), 1981, pp. 499–508.

[27] K.K. Kim, N.S. Umanath, Structure and perceived effectiveness of software development subunits: A task contingency analysis, Journal of Management Information Systems 9(3), 1993, pp. 157–181.

[28] M.J. Liberatore, G.J. Titus, M.W. Varano, P.W. Dixon, Experimental investigation of the effects of some information system design variables on performance, preference, and learning, Information Processing and Management 25(5), 1989, pp. 563–577.

[29] C.K. Mick, G.N. Lindsey, D. Callahan, Towards usable user studies, Journal of the American Society for Information Science 31(5), 1980, pp. 347–365.

[30] L.B. Mohr, Organizational technology and organizational structure, Administrative Science Quarterly 16, 1971, pp. 444–459.

[31] L.G. Paul, C/S deployment – Brave new world, PC Week 18, 1992, pp. 19–22.

[32] P.E. Renaud, Introduction to client/server systems: A practical guide for systems professionals, John Wiley and Sons, Inc., New York, NY, 1993.

[33] C. Schoonhoven, Problem with contingency theory: Testing assumptions hidden within the language of contingency, Administrative Science Quarterly 26(3), 1981, pp. 349–377.

[34] J.D. Thompson, Organizations in Action, McGraw-Hill, New

York, 1967.

[35] G. Torkzadeh, W.J. Doll, Test-retest of end-user computing instrument, Decision Science, 1991.

[36] M.L. Tushman, D.A. Nadler, Information processing as an integrating concept in organizational design, Academy of Management Review 3(4), 1978, pp. 613–624.

[37] M.L. Tushman, Work characteristics and sub-unit communication structure: A contingency analysis, Administrative Science Quarterly 24(1), 1979, pp. 82–97.

[38] N.S. Umanath, K.K. Kim, Task-structure relationship of information systems development subunit: A congruence perspective, Decision Sciences 23(4), 1992, pp. 819–838.

[39] M. Withey, R.L. Daft, W.H. Cooper, Measures of Perrow's work unit technology: An empirical assessment and a new scale, Academy of Management Journal 26, 1983, pp. 45–63.

[40] S.B. Yadav, Classifying an organization to identify its information requirements, Journal of Management Information Systems 2(1), 1985, pp. 39–60.

![](/api/attachments/6C5D4QDF/fulltext/images/3ed01babd524c5f7a313ee688ffddc75d7b4689b68e6f48cc3db2368293d539f.jpg)

Murugan Anandarajan is an Assistant Professor of Management Information Systems, at Drexel University. He received his Ph.D. in Management Information Systems from Drexel University. He holds a MBA and MS in Accounting. He is an Associate member of the Chartered Institute of Management Accountants, London, U.K. Dr. Anandarajan has published and has forthcoming articles in Behaviour and Information

Technology, Computer and Operation Research, Industrial Management and Data Systems, Information and Management, International Journal of Computer Information Systems, Journal of Applied Business Research and Management Accounting among others. His research interests including Emerging technologies, the application of AI in business, and client/systems computing.

![](/api/attachments/6C5D4QDF/fulltext/images/1a3d0c0b26ed52e467e99ce5bf661e912c72df7a246d2cf01cb08789dffaaa82.jpg)

Dr. Bay Arinze is Professor of Management Information Systems and MIS Program Coordinator in the Management Department at Drexel University. He holds a B.Sc. in Computer Science from the University of Lagos, and an M.S. and Ph.D. in Systems Analysis from the London School of Economics and Political Science. His current research interests include C/S computing, ERP systems, and the uses of knowl

edge-based systems in operations management. Dr. Arinze has published articles in Journal of Management Information Systems, Decision Sciences, Decision Support Systems, IEEE Transactions in Engineering Management, International Journal of Man-Machine Studies, Journal of Computer Information Systems, Omega, International Journal of Management Science, Computers and Industrial Engineering, and Computers and Operations Research. He published a textbook with Wadsworth Publishers, entitled “Microcomputers for Managers”.
