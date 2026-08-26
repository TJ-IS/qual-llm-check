---
otero_id: 17272
otero_key: "QFGYZDBE"
title: "A knowledge based decision support system for computer performance management"
authors: "Bay Arinze; Magid Igbaria; Lawrence F. Young"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90043-o"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A knowledge based decision support system for computer performance management

Bay Arinze and Magid Igbaria
Drexel University, Philadelphia, PA 19104, USA

Lawrence F. Young

University of Cincinnati, Cincinnati OH 45221, USA

Computer systems managers make decisions about hardware and software selection, performance evaluation, capacity

![](/api/attachments/QFGYZDBE/fulltext/images/5fcb2d0b5a84abdacd110c30403f1a5e12f44f03c96d84fb27703439bd1e7801.jpg)

Bay Arinze is an Assistant Professor of Management Information Systems in the Department of Management at Drexel University. He holds a B.Sc. in Computer Science from the University of Lagos and an M.Sc. and Ph.D. in Systems Analysis from the London School of Economics and Political Science. His current research interests include DSS design methodologies and applications, and knowledge-based systems and their uses in business applications. He has published

articles in Journal of Management Information Systems, IEEE Transactions in Engineering Management, Computers and Industrial Engineering, Industrial Marketing Management, and the ACM Sigart Special Issue on Knowledge Acquisition.

![](/api/attachments/QFGYZDBE/fulltext/images/7649870bf4f8aa6eb57b9f91ac5620538b8d8805bf3fd856cd0ed0cb3bc000b1.jpg)

Magid Igbaria is an Associate professor of management information systems at Drexel University. Formerly, he lectured at Tel Aviv University, Hebrew University and Ben-Gurion University in Israel, and acted as the administrative director of the Center of Management Information Systems (CEMIS) at Tel Aviv University. He holds a B.A. in Statistics and Business Administration, and an M.A. in Information Systems and Operations Research from Hebrew University; he

received his Ph.D. in Management Information Systems from Tel Aviv University. He has published articles on management of MIS functions, economics of computers, computer performance evaluation, charging of computer services, computational approaches in MIS, and microcomputers in business in Applied Statistics, Behaviour & Information Technology, Communications of the ACM, Computers & Operations Research, Information & Management, Information Systems and Operational Research (INFOR), International Journal of Man-Machine Studies, Journal of Management, Journal of Management Systems, Omega, and others. His current research interests focus upon economics of computers, management of information systems, computer performance evaluation, and end-user computing.

Correspondence to: Bay Arinze, Department of Management, College of Business and Administration, Drexel University, Philadelphia, PA 19104, USA.

planning, and other resource variables on the basis of factual data, accounting data, subjective judgments, and assumptions about the resource consumption of the jobs being run. The importance of computer resource planning calls for effective support methods. A Knowledge-Based DSS (KBDSS) will be able to assist managers in making these policy decisions by utilizing knowledge of the existing configuration and its capabilities, the organizational computing environment, available external resources, and their suppliers. Combining procedural and declarative methods, such a KBDSS may provide early warning of possible bottlenecks, forecast growth of hardware usage, and employ knowledge based inferencing to suggest suitable remedial actions to the systems manager. This paper presents a KBDSS for supporting computer resource planning decisions using a procedural/declarative framework, and illustrates the system's usage aspects.

Keywords: Performance of systems, Knowledge-based systems, Decision support, Management of computing and information systems, Performance and usage measurement.

## 1. Introduction

A computer operations manager bases his/her planning and operation decisions on a heterogeneous collection of usage and performance data, judgments, and assumptions concerning the resource consumption of the jobs being run. The objective data are collected and stored in the accounting routines residing in most operating systems of computers, such as SMF (System Management Facilities) in IBM mainframes [8,9]. Other inputs to these decisions include the personal heuristics and expert knowledge of the operations manager and staffs, along with other fuzzy, incomplete and judgmental knowledge that are considered in decision-making.

Having collected both types of information, it is worthwhile to consider how they may be integrated and utilized by a Knowledge-Based DSS (KBDSS) to support managerial decisions on configuration upgrade alternatives. The purpose of this study is to show how this can be done. This paper describes a KBDSS which integrates procedural computer evaluation models within a knowledge-based system for evaluating current and future resource utilization and recommending suitable upgrade paths for the existing computer configuration.

The procedural model will provide early warning of possible bottlenecks, forecast hardware usage to predict and monitor the effects of configuration changes, and gauge the effects of introducing new categories of jobs to the existing installation. Forecasts are based on the projection of future hardware usage needs from actual current usage data and on possible upgrade actions. The model may be used for making such conditional forecasts and allowing for the examination of 'What-If?' options, such as the addition of a new application or a new group of jobs, or reduction of a specific resource utilization. The statistical prediction model, which also supports goal-seeking and other enquiry functions, is described in this paper.

The KBDSS will then combine inputs from the prediction model with acquired expert knowledge pertaining to resource selection, configuration tuning, resource interactions, upgrade options, personnel capabilities and vendor characteristics. The system uses these inputs in proposing, for the computer configuration, adequate upgrade paths (tuning or equipment acquisition) and other alternatives, such as shifting applications to other systems. The KBDSS may therefore be used either in planning for, or responding quickly to unexpected workload changes. Subsequent sections of the paper describe the complete system features and further implementation steps needed to complete an operationally acceptable KBDSS.

Computer performance evaluation (CPE) belongs to the realm of computer economics and is essential in the process of computer selection, configuration design, and control of existing systems. In addition, CPE facilitates the pricing of computer services $[1,11,18,19,20,21]$ . The opportunity is identified in this paper to apply knowledge-based methods to improve the effectiveness of the procedural models that have traditionally been used for CPE. The expected gains in planning effectiveness of systems managers will result from utilizing expert knowledge of configurations, environments, and resource interactions acquired over time by expert planners.

The rest of the paper is as follows. Section 2 describes the knowledge based approach that is utilized for computer performance management, while Sections 3 and 4 discuss the knowledge-based and procedural components of the KBDSS for CPE. Section 5 illustrates the use of the KBDSS by means of an example, while Section 6 highlights the proposed implementation and usage methodology for the KBDSS. Section 7 outlines the paper's summary and conclusions.

## 2. Knowledge-based systems and computer resource management

Knowledge-based systems (KBS's) have been used for a wide range of service and manufacturing applications [22,25,27,28]. KBS's can be viewed as computer programs which utilize captured and encoded expert knowledge to solve non-trivial problems of economic value using inferencing methods [13,24]. They embody a declarative paradigm, in which problem-solving methods are separated from the knowledge required for solution. By eliciting knowledge from domain experts, and representing it in the form of facts and rules, frames, semantic nets, or other knowledge representations, KBS's may 'reason with' both stored and interactively-entered knowledge to diagnose problems, offer solutions, create plans, and monitor and control processes [7,23,24,25].

In addition to the ease of understanding offered by the declarative knowledge representation, further benefits provided by KBS's include the ability to 'intelligently' restrict computationally huge solution spaces, handle fuzzy or qualitative knowledge, and deal with incomplete or uncertain knowledge [24]. They have therefore undergone use in areas as diverse as mineral prospecting, equipment configuration, equipment failure analysis, and medical diagnosis [13,25]. The components of a KBS will typically include the user interface, inference engine (for processing encoded knowledge), knowledge-base (for storing acquired expert knowledge), and frequently, a data base and sensors [14,24,28].

## 2.1. Overall architecture of the KBDSS

The KBDSS consists of the knowledge-based (KB) component and the procedural CPE models. It was decided to utilize the rule-based paradigm to implement the KB component, using Prolog as the target language; while the modeling of the procedural CPE model was carried out using the Excel spreadsheet. Prolog was selected as the language of implementation for a variety of reasons. These included the availability of a powerful PC-based Prolog compiler (Turbo Prolog 2.0.) and accompanying libraries. In addition, the emerging consensus in the literature appears to favor Prolog over Lisp for AI applications [10,13,14,27,29]. Specifically, Turban [27, p. 554] predicts that Prolog, the most widely-used AI language in Europe and Japan, will increasingly predominate as more sophisticated implementations become available.

The rule-based KB subsystem utilized backward chaining in attempting to prove or select an upgrade or tuning alternative, representing the system's goals. The inference tree for the KBDSS is shown in fig. 1.

Fig. 1 shows the inputs to the selection decision derived from the two procedural and five declarative submodels. The following two sections describe first the knowledge-based, and then the procedural DSS components, and their architecture and operation.

## 3. The KBDSS knowledge-based component

The knowledge-based component of the KBDSS is closely integrated with the statistical and forecasting models within an overall KB framework. This close coupling of the procedural and declarative components facilitates the “synergistic effect” described by Turban [27]. Similar to a frame-based system, these models may be viewed as ‘procedural attachments’ that are invoked by the KBDSS, and whose results are returned to it.

![](/api/attachments/QFGYZDBE/fulltext/images/8b90e936d35f27fdad4fa54f0a8ce578415e3cf3f845a0a32a08b6c06d330695.jpg)  
Fig. 1. The knowledge-based DSS for computer performance planning.

The literature identifies three areas in which an MIS manager makes decisions about computer performance management, namely tuning, upgrade and selection [1,8,15]. Within the area of selection, three further dimensions may be observed, namely personnel capabilities, resource interactions and vendor performance. The resulting areas were validated by matching them against those presented in [1,8,15], and checked for completeness in interviews with senior managers of a computer installation. The knowledge representations for the implementation described in this paper were derived from a variety of sources. These included interviews with computer installation managers described further on, prior studies in the CPE area and the vendor literature. Combining the procedural model's output with encoded knowledge from the five key areas, selection of a tuning or an upgrade alternative is reached by the inferencing process. These five key areas for which knowledge elicitation must take place are described in more detail below:

(1) Knowledge of resource interactions. Many interactions between hardware and software components are synergistic, unpredictable, or even calamitous in their effects. For example, certain software may be incompatible with given operating systems, or may require specific hardware components to run correctly. Much of this knowledge is often undocumented, but is known by experienced operations personnel.

(2) Knowledge of upgrade options. Assuming resource utilization is predicted, there are typically a considerable number of hardware and software options available. Each of these has several associated characteristics such as costs (purchase and maintenance), performance, reliability, compatibility, security, and upgrade ceilings. This knowledge may be elicited as part of the knowledge base.

(3) Knowledge of tuning options. As with the upgrade options discussed above, several tuning alternatives will be available to the computer center manager, and will generally be considered prior to the upgrade options, being typically cheaper to implement. Tuning options will involve tactics such as alteration of timeslices, job priorities, primary and secondary storage allocations etc., and are the preserve of expert operations personnel and managers.

(4) Knowledge of personnel capabilities. Each computer center contains personnel with a mix of capabilities and experience on various hardware and software platforms and tools. Typically therefore, that certain otherwise viable options may not be seen as attractive if few or no operations personnel have experience with that particular compiler, operating system, or device. Knowledge of the capabilities and experience of available personnel is therefore relevant to the selection decision.

(5) Knowledge concerning vendor performance. This final component is essential in the selection decision. Expert knowledge of vendor performance will focus on criteria such as delivery time, product quality, maintenance arrangements, comparative product cost, and other factors.

A rule-based KBDSS prototype was implemented in Turbo Prolog 2.0. The rule-based paradigm was chosen due to the limited number of rules involved in the initial system, and accompanying manageability. Rules are also naturally and easily implemented in Prolog. However, further implementations of this system may employ a frame-based knowledge representation scheme. In addition, inexact reasoning, using certainty factors or probabilities was not used in this implementation, but may be installed as necessary. A backward-chained inferencing strategy was employed to determine upgrade paths based on knowledge and data supplied from different areas. The inference engine was also monotonic in operation (allowing no revision of current facts), and used a depth-first inferencing strategy for a more directed line of questioning.

## 4. The KBDSS procedural component

Ahituv and Igbaria [1] have developed a model for analyzing and predicting computer resource consumption in which groups of jobs consume computer resources and each job utilizes a certain amount of hardware resources. Present consumption, such as CPU time in seconds, is measured for each computer resource and used to predict future use. Igbaria [15] and Ahituv and Igbaria [1] note that future expected total utilization, which is denoted by $E(T)$ , equals current utilization of the given workload and the additional utilization derived from new requirements. Additional expected utilization is based on statistical relationships among the consumption of various resources.

The model refers to the following components: M is the number of homogeneous groups of jobs;

U represents a vector of the current utilization of each resource;

B is a matrix of the slope coefficients (beta coefficients) of the independent variables. B includes m sub-matrices for each group of jobs. $B_{ij}^{m}$ denotes the slope coefficient of $X_{i}$ (printer for example) to predict $X_{j}$ (CPU for example) in group m;

A is a matrix of the intercept coefficients (alpha coefficients). This matrix includes m submatrices for each group of jobs. $A_{ij}^{m}$ denotes the intercept coefficient of the independent variable $X_{i}$ to predict $X_{j}$ in group m.

Suppose it is known that the consumption of one of the computer resources will increase in the future. Then the expected future utilization of all the resources is represented by the following set of equations (for details see [1] and [15])

$$
\boldsymbol {E} (\boldsymbol {T}) = \boldsymbol {U} + [ \boldsymbol {B P} + \boldsymbol {A I} ] K,
$$

where

P Column vector of zeros except one element which corresponds to the computer resource whose consumption will increase. This element is equal to the incremented consumption;

I As P above, except that the specific element equals one;

K The number of new jobs expected to be run on the system.

If the consumption data have undergone a transformation for the purpose of using linear regression (e.g., a logarithmic transformation), then the above equation should be modified as follows

$$
\boldsymbol {E} (\boldsymbol {T}) = \boldsymbol {U} + \left[ \boldsymbol {B P} + \boldsymbol {A I} \right] ^ {f} \boldsymbol {K},
$$

where f is a transformation function (e.g., antilogarithm).

The planning process for meeting user capacity needs is carried out using this basic model and by applying a series of 'What-If?' scenarios. The model can be used by the information system manager to support new hardware policy [1,15] by:

(1) predicting the effects of adding a new group of jobs to an existing workload;

(2) providing early warning of possible bottle-necks;

(3) assessing the effect of changing technologies and user needs;

(4) providing forecasts of computer capacity demand in future time periods;

(5) allowing the managers to examine the sensitivity of the solution to changes.

The following section illustrates how this model can be used as a major component of the KBDSS.

## 4.1. The procedural CPE model: Functional requirements

Uncertainty associated with future demand on resources and the complex interactions between various resources in a typical large computer installation contribute to making the system upgrade decision a semi-structured one. The DSS approach, as defined in the literature $[4,17,26,27,31]$ is particularly suitable for such problems. Young $[30]$ in particular points to specific task requirements which include “judgment, ambiguity, creativity, and volatility of environment”, each of which exists to some degree within the computer performance management activity.

The KBDSS utilizes the procedural model as a basis for effectively exploring the problem space. To determine the required scope of such exploratory analysis, we refer to a framework advanced by Arinze [6]. He proposes a DSS methodological approach in which decision makers are seen as making three distinct types of enquiries to a DSS. These enquiry classes are called State, Action, and Projection enquiries. While State enquiries seek (descriptive, explanatory, subjective, temporal, etc.) information about some part or model of the world, Action enquiries solicit for possible action sequences that may be taken in order to reach a specified goal or consequence. The Projection enquiry on the other hand, which is equivalent to a 'What-If?'-type query, seeks information about the consequences of taking specified actions. These three types of decision enquiries are seen as forming a useful framework for organizing the information requirements of the decision makers. This framework is similar to that of other DSS researchers, such as Young [30] who refers to the same categories, respectively as: (a) 'what is?'; (b) 'what's best'; and (c) 'what if?' support functions.

Using a framework such as this, a computer operations manager can be expected to make enquiries such as the following:

(1) State enquiries ('what is?').

\- “How much unused capacity exists?”

\- “What are the costs of further capacity for different mixes of resources?”

\- “What are the available resources and their utilization (U)?”

\- “What are the proposed alternative configurations to meet the need for new/additional requirements?”

(2) Action enquiries ('what's best?').

\- “Should new jobs (K) be added, and if so, in what priority and scheduling order? (within capacity and other constraints)”

\- “Should capacity be added or reduced to meet (actual or hypothetical) requirements, and if so, how (within cost and other constraints; and in terms of upgrading/tuning the system, selecting a new system, or not allowing additional jobs)?”

(3) Projection enquiries ('what if?').

\- “If new capacity is added, which resources are potential $(E(T)/C)$ and actual $(U/C)$ bottlenecks?”

\- “If the computer resource is upgraded, will actual or hypothetical bottlenecks be removed?”

Examples of each of these types of interaction are illustrated in the following section. Furthermore, the use of the system will be preceded by the following:

(1) The user will answer all the questions given by the system. The answers to these questions help the system in constructing a regression model.

(2) The user can select the data set to be analyzed (historical data) and decide to base the prediction on two years by historical data.

(3) The system will suggest what transformation should be performed before estimating the regression parameters. The user may also suggest a transformation.

(4) The system calculates the regression coefficients (A and B) and the user is informed by these parameters and along with those, some statistics will be provided such as R-square, F and T values.

For ease of use while preserving considerable flexibility, command menus are proposed to be used at the top levels of the system in order to direct the user to the subsystem(s) appropriate to his needs. A mix of question-and-answer format and a 'fill-in-the-form' style of interface is proposed for the construction and reconstruction of models and parameters. The system also should allow the user to present the results graphically by plotting existing sets of data or displaying model-generated results. The following subsection now describes a numerical example.

## 4.2. The procedural CPE model: Usage

Usage of the procedural model is illustrated by means of a simplified numerical example. Consider a computing center consisting of three main hardware resources (central processing unit (CPU), disks, and line printers). Table 1 shows the capacity and utilization for each of the three hardware resources described above in column format [1]. The first column is defined as the vector C and the second column as U.

It is interesting to note the wide variation in resource utilization and its implication for system balance. These findings would intuitively suggest a reconfiguration of hardware resources.

Table 1  
An example of capacity and utilization data.

<table><tr><td>Hardware resource</td><td>C capacitya</td><td>U Utilizationa</td><td>Utilization percentagesb</td></tr><tr><td>CPU (seconds)</td><td>67305</td><td>31037</td><td>0.46</td></tr><tr><td>Disks (I/O operations)</td><td>1486080</td><td>1190000</td><td>0.80</td></tr><tr><td>Printers (lines)</td><td>2880000</td><td>442300</td><td>0.15</td></tr></table>

$^{a}$ It is assumed that the time interval is 24 hours.  
$^{b}$ The resource utilization percentages are defined as utilization divided by capacity for each hardware resource, that is, $U_{i}/C_{i}$ , where ii denotes resource i.

Assume there are two homogeneous groups of jobs, such as student and non-students jobs in an academic institution. Therefore, M = 2 and J = 3 (number of resources) and the matrix B includes two sub-matrices $B_{1}$ and $B_{2}$ .

$$
\begin{array}{l} \boldsymbol {B} = \left[ \begin{array}{c c} \boldsymbol {B _ {1}} & \boldsymbol {B _ {2}} \end{array} \right], \\ \boldsymbol {B} = \left[ \begin{array}{c c c c c c} 1 & 0. 7 & - 0. 1 3 & 1 & 0. 3 4 & 0. 0 6 5 \\ 0. 5 5 & 1 & - 0. 0 7 6 & 0. 8 8 & 1 & 0. 0 7 \\ - 0. 2 5 & - 0. 1 & 1 & 0. 0 8 6 & 0. 3 8 & 1 \end{array} \right]. \end{array}
$$

It is assumed that each job is not allowed to consume more than 40 seconds of CPU (this is an administrative policy).

Vector P (as mentioned above) would be equal to

$B_{1}$ is displayed in the first three columns of B, and $B_{2}$ is shown in the last three columns.

A is given by the following matrix

The matrices B and A are shown in terms of regression coefficients after the data have undergone a logarithmic transformation (assume that early in the analysis of the data it was realized that transforming the three variables, CPU time, number of lines, and disk I/O operations by using a logarithmic transformation was appropriate; details can be found in [2]). The matrices A and B were computed after sampling a large number of jobs and running a set of linear regression equations on the logarithmic transformation of the resource consumption values.

$$
\begin{array}{l} \boldsymbol {A} = \left[ \begin{array}{c c} \boldsymbol {A _ {1}} & \boldsymbol {A _ {2}} \end{array} \right] \quad (\text { similar   to } \boldsymbol {B}), \\ \boldsymbol {A} = \left[ \begin{array}{c c c c c c} 0 & - 0. 3 5 & 3. 1 & 0 & - 1. 1 8 & - 1. 7 3 \\ 3. 1 2 & 0 & 4. 8 4 & 3. 1 2 & 0 & 4. 8 4 \\ 1 1. 1 4 8 & 1. 2 6 & 0 & 5. 0 5 & 4. 9 7 & 0 \end{array} \right]. \end{array}
$$

$$
\boldsymbol {P} = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ \ln 4 0 \\ 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 3. 6 9 \\ 0 \\ 0 \end{array} \right].
$$

The first three zeros indicate that there is no change in the consumption of non-student users.

Since it is assumed that new jobs are added, vector I would be equal to

$$
\boldsymbol {I} = \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{array} \right].
$$

The analysis here assumes a computer system with only three hardware resources. In a computer system environment there are usually more than three resources. The analysis of such a system will require that the framework presented here, especially the matrices, be expanded to include all the hardware resources as well as all other user groups, of course.

![](/api/attachments/QFGYZDBE/fulltext/images/d31df52ffa2a29cb036ec0e6264e6926947fc4dc3fca66e61ec8802ec8d9b545.jpg)  
Fig. 2. Resource utilization percentages for 150 new student jobs.

![](/api/attachments/QFGYZDBE/fulltext/images/6c64ec565946e520c91a50d96fc2b5efed6dbd99a5dbb5ba2abc954b4d0a92b9.jpg)  
Fig. 3. Resource utilization percentages of 20-200 new student jobs.

This numerical example demonstrates how the model can provide the information systems manager with a tool to support hardware policy concerning the predictions of:

(1) the effect of introducing a new group of jobs on an existing workload;

(2) early warning of possible bottlenecks.

The following set of three enquiries demonstrate the range of the previously-discussed set of enquiry types, and illustrate the form of the DSS user interface:

(a) “What if 150 new student jobs are added?” This enquiry explores resource utilization implications of adding a specific number of new student jobs, namely 150. These implications or consequences are sought in the form of utilization percentages. As shown in fig. 2, the resultant utilization percentages are 16%, 86%, and 55% for printers, disks and CPU, respectively. The high disk utilization might indicate the undesirability of adding up to 150 new jobs or the need for upgrading the disk resource.

(b) “Show the resource consumption for 20 to 200 new student jobs.”

This enquiry implies the computation and presentation of resource utilization implications of adding 20 to 200 new student jobs. Fig. 3 graphically illustrates the output of this enquiry, showing resource consumption for each of the three resources—CPU, Disks, and Printers, in 20-job increments. Table 2 also displays the data in tabular form. The output of this enquiry shows disk usage rising to a height of 88% as the number of jobs reaches 200, while CPU and Printer resource utilization remain at more acceptable levels.

Resource utilization percentages for demand levels of 20–200 for new student job.

<table><tr><td>Varying demand levels (in number of jobs)</td><td>CPU expected utilization percentages</td><td>Disk I/O expected utilization percentages</td><td>Line printer expected utilization percentages</td></tr><tr><td>20</td><td>47</td><td>81</td><td>16</td></tr><tr><td>40</td><td>48</td><td>82</td><td>16</td></tr><tr><td>60</td><td>50</td><td>82</td><td>16</td></tr><tr><td>80</td><td>51</td><td>83</td><td>16</td></tr><tr><td>100</td><td>52</td><td>84</td><td>16</td></tr><tr><td>120</td><td>53</td><td>85</td><td>16</td></tr><tr><td>140</td><td>54</td><td>86</td><td>16</td></tr><tr><td>160</td><td>56</td><td>86</td><td>17</td></tr><tr><td>180</td><td>57</td><td>87</td><td>17</td></tr><tr><td>200</td><td>58</td><td>88</td><td>17</td></tr></table>

"Given CPU, Disk, and Printer limits of 60%, 90% and 19% respectively, what is the maximum number of jobs allowed?"  
![](/api/attachments/QFGYZDBE/fulltext/images/f6f3d2687f376d38a1f21faa2aab88e402806045ad6ec60e09ad7dd3f64f14fe.jpg)  
Fig. 4. Number of jobs allowed given maximum utilization percentages.

(c) “Given CPU, Disk, and Printer limits of 60%, 90%, and 19%, respectively, what is the maximum number of jobs allowed?”

This third enquiry is the most complex, and is an example of a goal-seeking enquiry. It reflects a need to know the maximum number of jobs allowed, given specific limits on individual resource utilization (in this case, 60%, 90%, and 19% for CPU, Disks, and Printers respectively). Fig. 4 illustrates the maximum number of jobs allowed for each individual resource utilization limitation; 490 for the Printer limit, and 253 and 234 for the Disk and CPU limits, respectively. The smallest of these, 234—the CPU limit, is highlighted, indicating that this number is the maximum allowed for the system.

## 4.3. Addition of a new class of jobs

The procedural model possesses the flexibility to cope with the addition of new jobs for the existing job categories. In addition however, the capability exists for adding new classes of jobs, by initially benchmarking the new job types to produce their utilization matrices. These are then input to the model and run with the existing job types to determine new resource utilization. For example, given a new set of 200 administrative jobs is introduced with the resource utilization submatrices $B_{3}$ and $A_{3}$ as follows

"What if 200 new administrative jobs are added?"  
![](/api/attachments/QFGYZDBE/fulltext/images/7da2f1bb9d45a01796795044d1bca1aa868f610257898b14dff57cdc09ecd95f.jpg)  
Fig. 5. Resource utilization percentages given 200 new administrative jobs.

$$
\begin{array}{l} \boldsymbol {B} _ {3} = \left[ \begin{array}{c c c} 1 & 0. 5 8 & 0. 5 3 \\ 0. 8 1 & 1 & 0. 5 \\ 0. 4 8 & 0. 4 3 & 1 \end{array} \right] \\ \boldsymbol {A} _ {3} = \left[ \begin{array}{c c c} 0 & - 1. 1 & - 0. 1 1 \\ 0. 8 1 & 1 & 0. 5 \\ 0. 4 8 & 0. 4 3 & 1 \end{array} \right], \end{array}
$$

and the P and I vectors as follows

$$
\boldsymbol {P} = \left[ \begin{array}{c} 0 \\ \ln 4 0 3 \\ 0 \end{array} \right] = \left[ \begin{array}{c} 0 \\ 5. 9 9 \\ 0 \end{array} \right] \qquad \boldsymbol {I} = \left[ \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right]
$$

resource utilization increases from $[0.46, 0.80, 0.15]$ of CPU, Disks and Printers respectively (see table 1) to $[0.49, 0.86, 0.21]$ . The increase in disk utilization in particular, may therefore serve to alert the manager of an impending need for more secondary storage. The output of the model is shown in fig. 5.

## 5. A case example

To illustrate the knowledge-based component of the KBDSS, an example is introduced, based on an actual computer center. In this example, an IBM 3090 Model 150E is employed, running on VM and processing both administrative and research applications in a university setting. While the Model 150E runs at roughly 11 MIPS, other models include Models 180, 200, 400, and 600 (the latter running at up to 100 MIPS.) Two classes of jobs are run, namely batch and interactive applications, with a higher priority given to interactive applications. The Model 150E is also a unary machine, containing one vector processor, which is used primarily by academic researchers.

VM HPO, the version of VM used, suffers from a limitation in the number of virtual machines which may be created. VM XA, expected to be introduced sometime in the future, can service up to 120 users. One other constraint is that the Model 204 data base currently used for administrative functions, cannot be split over multiple CPU's. The mainframe runs at roughly 60% capacity on average, and only infrequently, over 80% of capacity. Batch jobs are divided into 4 queues based on their size, possess a lower priority than interactive jobs, and are usually run at nighttime.

The manager of this computer center, who has many years of experience, recognizes the existence of cheaper plug-compatible machines. These include the AMDAHL and NAS mainframes (the former possessing no vector processor), which he estimates to be about 100% and 90% compatible with the 3090 respectively. Compatibility seems to be a major concern for the senior managers, who cite users as being intolerant of installation-emanating problems or glitches. Compatibility is also highlighted as being very important in another set of circumstances, namely when serious problems occur whose source cannot be accurately pinpointed by center personnel. Multiple vendors have been known to point accusing fingers at one another in such situations, while the computer remains down. The senior managers voiced their reticence to mixing kit from different vendors for this reason, unless they are 'loosely coupled' (vs. 'tightly coupled') to the CPU. DASD's were presented as an example of tightly-coupled devices, while laser printers were described as being loosely-coupled devices—it so happened that the current laser printer was purchased from a different manufacturer for that specific reason (and for price/performance). Concerning purchase and maintenance costs, the center managers further identified leasing as a potentially beneficial alternative in cash-constrained situations. The three main avenues they identify for hardware upgrade are summarized as CPU, memory, and I/O devices. The third category includes DASD, printers, communications controllers, and tape drives etc. While memory may be increased and I/O channels increased in number, once CPU capacity is exceeded, a more powerful model must be purchased. Third-party maintenance arrangements, which are often cheaper, may also be made.

With regard to tuning, several options were described by the operations manager. These include making use of primary memory more efficiently, the reorganization of files in the data base, based on application use, and the modification of timeslices for special events, such as student registration. Other possible practices, such as users applying checkpoints in their programs, are seen as more difficult to enforce in an academic environment. This particular problem often resulted in interrupted long jobs having to be restarted from scratch. Monitoring tools continually collect data relating to performance, and these data are frequently analyzed by both the operations personnel and the IBM to detect and rectify any usage inefficiencies.

The purchase of applications software in addition, is driven by the desires of academic users, representing one constraint the center manager must take into account in any resource acquisition.

The following subsection describes the knowledge base structure resulting from this requirements analysis and definition.

5.1. Design of the KBDSS knowledge base using Prolog

Turbo Prolog 2.0. represents knowledge by means of predicates whose structures are defined in the predicates section of the program. These predicates represent objects, their attributes, properties, and relationships, with instances of these predicates (in the form of facts and rules) found in the clauses section of the Prolog program. The domains section aids user definition of variable types, while the database section enables the storing, retrieval, and deletion of facts from the knowledge base.

The inferencing strategy or set of meta-rules guiding the inferencing process consists of four steps, namely:

(1) Check projected utilization percentages by invoking the statistical (procedural) models, and importing the results;

(2) if the projected CPU utilization is too high, propose a major upgrade for the current configuration that will increase processing capabilities;

(3) if non-CPU utilization percentages are too high, propose tuning options to the user, based on the amount of overutilization, existing constraints, and available alternatives;

(4) if non-CPU utilization percentages are still too high, propose purchase options, based on their characteristics, the amount of overutilization, existing constraints, and available resources.

The KB component of the KBDSS provides five menu options for the user. These include:

(1) Importing the projected utilization percentages;

(2) performing the required diagnosis;

(3) printing the ES recommendations;

(4) saving the current configuration details;

(5) exit the system.

## Knowledge representation: Predicates

Several predicates are required to represent the acquired knowledge. The major predicates that are used include:

projected \_utilization(cpu, disk, memory, printer) This predicate stores projected resource utilization percentages that originate from the procedural model.

maximum \_utilization(cpu, disk, memory, printer)

This predicate keeps a record of maximum acceptable resource utilization percentages that are defined by the computer installation manager.

process(1)

This predicate represents the main menu option 1.

cpu \_ diagnosis(cpu, \_, \_, \_)

disk \_diagnosis(\_, disk, \_, \_)

memory\_diagnosis(\_, \_, memory, \_)

printer \_diagnosis( \_, \_, \_, printer).

The above four predicates perform the required diagnosis of CPU, Disk, Memory, and Printer-related problems respectively, and provide recommendations.

Knowledge representation: Rules and Prolog clauses

The knowledge elicited from the computer center managers was represented in the form of facts and ruled. These rules were deterministic, given their clear-cut description, but it is possible that a further iteration of knowledge elicitation may lead to the use of inexact reasoning i.e., probability or certainty factors.

The extracted rules were represented in the form of three decision tables, handling CPU, memory and I/O (Disks and Printers) diagnosis respectively. The rule set for the CPU knowledge-base component is shown in table 3a, and an example of KBS/User Dialogue in fig. 6. Knowledge utilized by the KBDSS includes the following:

(1) Knowledge of CPU overutilization, which is collected from the procedural model;

Table 3a  
Rule set for the CPU knowledge-base component.

<table><tr><td>Criteria</td><td>Rules</td></tr><tr><td rowspan="2">CPU exceededUneven CPU usage distribution</td><td>Y Y - N -</td></tr><tr><td>N N Y N -</td></tr><tr><td rowspan="2">Restricted finances(One-off) Occured during special events</td><td>Y N - - -</td></tr><tr><td>N N N N Y</td></tr><tr><td>Modify timeslices</td><td>- - - - X</td></tr><tr><td>Redistribute batch jobs and retest</td><td>- - X - -</td></tr><tr><td>Upgrade to FEP or newer model</td><td>X X - - -</td></tr><tr><td>Consider plug-compatible (e.g., Amdahl, NAS, Hitachi)</td><td>X - - - -</td></tr><tr><td>Consider leasing options</td><td>X X - - -</td></tr><tr><td>Purchase newer model</td><td>- X - - -</td></tr></table>

(2) an indication of any unevenness in the distribution of CPU usage;

(3) the availability of finances for major system upgrades;

(4) entered facts pertaining to the coincidence of CPU overutilization and special events.

Based on the situational responses to these four conditions, the KBDSS proposes remedial actions from a set of five recommendations. These are:

(1) Modifying timeslices (during special non-recurring events);

(2) redistributing batch jobs, to address uneven CPU usage;

(3) upgrading to a newer model, as a final resort;

(4) considering leasing options (in combination with (3)), to cope with constrained finances;

(5) considering a plug compatible (e.g., AMD-AHL, NAS, HITACHI) machine, also in financially constrained situations. Given a situation in which the maximum allowed, and actual resource utilizations are

projected \_utilization(0.70, 0.82, 0.87, 0.33),

maximum \_utilization(0.65, 0.85, 0.92, 0.40),

the predicate get\_cpu\_exceed determines that the CPU resource is overutilized as follows:

projected \_utilization(CPU\_Prj, \_, \_, \_), maximum \_utilization(CPU\_Max, \_, \_, \_), get\_cpu\_exceed(CPU\_Exceed, CPU\_Prj, CPU\_Max).

get\_cpu\_exceed(CPU\_Exceed, CPU\_Prj, CPU\_Max):

CPU\_Prj > CPU\_Max,

```python
CPU_Exceed = 'Y',
```

write("<<Based on Procedural Modeling, CPU will be overutilized>p]").

get\_cpu\_exceed(CPU\_Exceed, CPU\_Prj, CPU\_Max):

CPU\_Prj <= CPU\_Max,

```txt
The Computer Performance Management Expert System
CPU-RELATED RECOMMENDATIONS
<< Based on Procedural Modeling, CPU will be overutilized >>
Is there an uneven distribution of CPU usage? [Y/N]: N
Are there restricted finances for equipment purchase? [Y/N]: Y
Were utilization percentages collected during special events? [Y/N]: N
Recommendations are as follows:
1. Upgrade to an FEP or a more powerful processor, but
2. Consider a plug-compatible mainframe, and
3. Consider Leasing options for the new equipment
Press any key to continue:
```  
Fig. 6. System user dialogue for the KBDSS.

Table 3b
Rule set for the memory knowledge-base component.

<table><tr><td>Criteria</td><td>Rules</td></tr><tr><td>Available memory exceeded</td><td>YYYYYYYYYYYYYYYYYY</td></tr><tr><td>Memory expandable</td><td>YYYYNNNNYYYYNNNN</td></tr><tr><td>More virtual machines required</td><td>YYYYNNYYYYNNYYYYNN</td></tr><tr><td>Memory reallocation possible</td><td>YYYYNYNYNYNYNYNYN</td></tr><tr><td>Memory reduction possible</td><td>YYYYYYYYNNNNNNNN</td></tr><tr><td>Reduce user memory allocation</td><td>XXXXXXX- - - - - - -</td></tr><tr><td>Improve memory usage</td><td>X-X-X-X-X-X-X-X-</td></tr><tr><td>Upgrade to VM XA operating system</td><td>XX--XX--XX--XX--</td></tr><tr><td>Purchase additional memory module</td><td>XXXX----XXXX----</td></tr></table>

Based on subsequent user responses to the questions indicated in table 3a, its first rule then fires, as shown in fig. 6 and illustrated below in the Prolog syntax

cpu\_recommend(CPU\_Exceed, CPU\_Uneven, CPU\_FRestricted, CPU\_Special):-

CPU\_Exceed = 'Y',

CPU\_Uneven = 'N',

CPU\_FRestricted = 'Y',

CPU\_Special = 'N',

write("Recommendations are as follows:"), nl, nl,

write("1. Upgrade to an FEP or a more powerful processor, but"), nl, nl,

write("2. Consider a plug-compatible mainframe, and"), nl, nl,

write("3. Consider Leasing options for the new equipment").

The above rule illustrates a situation in which the CPU is at, or heading for overutilization, resources are constrained, and no uneven CPU usage patterns or special events may be responsible. A model upgrade is now required, but due to the financial constraints, plug-compatible and leasing options should be considered.

Table 3b likewise illustrates the rule table for the diagnosis of memory-related problems, and the user interface during user interaction with the KBDSS. In the table, there are five possible conditions leading to up to four possible actions or recommendations that may be made by the KBDSS. The conditions include memory utilization, its expandability, a requirement for more virtual machines, and the feasibility of memory reallocation and/or reductions for applications. The last two conditions lead to recommendations for reducing individual memory allocations and improvements in memory usage. A need for virtual machines may be satisfied by upgrading to a suitable O/S, while additional memory purchases are proposed if the overutilized system is expandable, memory-wise.

Table 3c shows the rule set for the I/O-related knowledge-base component. As with the other rule sets, the less expensive options (typically the tuning options will be proposed first), with the more expensive options proposed only as a last resort. There are three conditions shown in table 3c, relating to I/O overutilization, tightness of device coupling to the mainframe, and existing usage inefficiencies, such as excessive thrashing, paging, swapping etc. Based on the supplied facts, the KBDSS may recommend file rearrangement on the DASD, increasing the number of channels, purchase consideration of plug-compatible devices (given loose coupling), and purchasing the device from the primary (mainframe) vendor (given tight coupling).

Table 3c  
Rule set for the I/O knowledge-base component

<table><tr><td>Criteria</td><td>Rules</td></tr><tr><td>I/O channels exceeded (Printer Terminals, DASD, Tape, Comms)</td><td>Y Y Y Y</td></tr><tr><td>Tightly-coupled device</td><td>Y Y N N</td></tr><tr><td>Usage inefficiencies (no spooling excessive thrashing, swapping paging etc.)</td><td>Y N Y N</td></tr><tr><td>Rearrange files on DASD</td><td>X - X -</td></tr><tr><td>Increase # of channels for buttleneck I/O devices</td><td>X X X X</td></tr><tr><td>Consider purchase of plug-compatible overutilized device</td><td>- - X X</td></tr><tr><td>Purchase overutilized device from primary vendor</td><td>X X - -</td></tr></table>

The initial rule base therefore contains 25 rules, representing 54 discrete condition-action matches (see tables 3a–3c), relating to the possible upgrade/tuning options in the three areas of CPU, memory and I/O bottlenecks. The implementation issues relevant to the KBDSS are discussed in the following section.

## 6. Implementation considerations

The prototype KBDSS was developed using Turbo Prolog 2.0. for the knowledge-based component, and Microsoft Excel for the procedural component, based on their suitability to each problem type. The heuristics of the installation manager were conveniently represented using Turbo Prolog, while Excel proved to be an adequate vehicle for the CPE model. However, due to the technical overhead of importing and exporting data between the two environments, a superior implementation might best be carried out (a) using a package such as GURU, which integrates both spreadsheet capabilities and inferencing and knowledge representation mechanisms within the same environment. Alternatively, (b) the KBDSS procedural component might be developed in a conventional programming language such as C or FORTRAN, and this module called (transparently) from within Prolog.

Which of these alternatives is most desirable depends on who the developer is. If such a system were to be developed in-house for large company's own use, alternative (a) should be preferable because of the likelihood of lower programming time and the cost and ease of system modification. Alternative (b) may be used however, if the technical expertise is available.

It is essential for DSS implementation to take place within the rubric of KBS development methodology. KBS development methodology has been variously documented by Parsaye [24], Gallagher [13], Turban [27], and others. Systemic aspects also need to be studied carefully [5] e.g., buying and leasing options, compatibility of various component parts, system constraints and the current decision making process, if one exists. The KBDSS methodology will guide the essential knowledge elicitation activity during development.

Requirements analysis will typically be iterative and incremental, as different problem-solving tactics are explored and experimented with $[16,30]$ , and as the captured knowledge is fine-tuned. The validation of the relevance and accuracy of the KBDSS knowledge-base is also required $[12,27]$ and it will need to evolve and be kept up-to-date with knowledge relating to new components, configurations and cost updates.

The KBDSS model is experimental, and needs fine-tuning. Unlike problems in the structured domain, several prototyping runs involving the installation manager and the analyst will be required in order to ensure the relevance of the overall system and to perform system calibration [3].

## 7. Summary and conclusions

In this paper we have proposed and illustrated a knowledge-based DSS for use in computer resource planning. It utilizes a procedural model for forecasting future hardware resource consumption, and draws upon current consumption data. It was shown that this technique provides the computer manager with a tool to control existing operations and to plan for future capacity. Furthermore, the technique was used to measure the sensitivity of the usage of one hardware resource to any changes in the usage of other resources. Thus the manager can analyze the impact of changing the current load of the system before implementation by using the 'What-If?' and other decision enquiry types discussed in this paper.

The area of performance management is one that involves a considerable amount of expertise. Good heuristics in this area, some of which are discussed in the previous section, may take months or even years to learn e.g., good installation utilization levels for single and multiple resources, The KBDSS is a promising tool for declaratively representing and manipulating expert computer resource management expertise to support the manager's decision-making, and improve overall installation performance.

One issue that has not been addressed here is the explicit incorporation of the cost parameter into the decision-making cycle for chargeback decisions. Further research should focus on enhancing the KBDSS to handle charging for computer resource consumption based on this paper. Additional research is also required to implement and validate the KBDSS for different computer configurations and areas.

## References

[1] N. Ahituv and M. Igbaria, A model for analyzing and predicting computer resource consumption, Communications of the ACM 31, Nr. 12, 1467–1473 (December 1988).

[2] N. Ahituv, Y. Benjamini, and M. Igbaria, A Compumetrical Approach for Analysis and Clustering of Computer System Performance Variables, Computers and Operations Research 15, Nr. 6, 489–496 (1988).

[3] R.J. Aldag and D.J. Power, An empirical assessment of computer-assisted decision analysis. Decision Sciences 17, 572–588 (1986).

[4] S.L. Alter, Decision Support Systems: Current Practice and Continuing Challenges (Addison-Wesley, Reading, MA, 1980).

[5] G. Ariav and M. Ginzberg, DSS design: A systemic view of decision support, Communications of the ACM 28, Nr. 10, 1045–1053 (October 1985).

[6] O.B. Arinze, Deriving DSS Specifications from a Model of the DSS/User Interface, in: Doukidis, Land, and Miller, eds., Knowledge Based Management Support Systems (Ellis Harwood, U.K., 1989).

[7] O.B. Arinze, and F. Partovi, A Knowledge Based Method for Designing Precedence Networks and Performing Job Allocation in Line Balancing, Computers and Industrial Engineering 19, Nr. 3, 351–364 (1990).

[8] I. Borovits, Management of Computer Operations (Prentice-Hall Inc., Englewood Cliffs, NJ, 1984).

[9] J.W. Boyes and D.R. Warn, A straightforward model for computer performance prediction, ACM Computing Surveys 7, Nr. 2, 73–93 (Feb. 1975).

[10] W.F. Clocksin, and C.S. Mellish, Programming in Prolog (Springer-Verlag, New York, NY, 1984).

[11] P. Denning, Performance analysis: Experimental computer science at its best, Communications of the ACM 24, Nr. 11, 725–727 (Nov. 1981).

[12] W.L. Fuerst and P.H. Cheney, Factors affecting the perceived utilization of computer-based decision support systems in the oil industry, Decision Sciences 13, 554–569 (1982).

[13] P.J. Gallagher, Knowledge Systems for Business (Prentice-Hall, Englewood Cliffs, NJ, 1988).

[14] P. Harmon, and D. King, Expert Systems (Wiley, New York, NY, 1985).

[15] M. Igbaria, A Model for Analyzing and Evaluating Computer Resource Consumption, Ph.D. dissertation, unpublished, Tel Aviv University (1986) (in Hebrew).

[16] P.G.W. Keen and T.J. Gambino, Building a decision support system: The mythical man-month revisited. In: J.L. Bennet, ed., Building Decision Support Systems (Addison–Wesley, Reading, MA, 1983).

[17] P.G.W. Keen and M. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley Publishing Company, Reading, MA, 1978).

[18] C.H. Kriebel and A. Raviv, An economic approach to modeling the productivity of computer systems, Management Science 26, Nr. 3, 247–311 (March 1980).

[19] C.H. Kriebel and A. Raviv, Application of a productivity model for computer system, Decision Science 13, Nr. 2, 206–286 (April 1982).

[20] C.B. Lewis and A.E. Crews, The evolution of benchmarking as a computer performance evaluation technique, MIS Quarterly 9, Nr. 1, 7–15 (March 1985).

[21] H.C. Lucas, Performance evaluation and monitoring, ACM Computing Surveys 3, Nr. 3, 79–91 (Sep. 1971).

[22] R.M. O'Keefe, Artificial Intelligence and the Management Science Practitioner: Expert Systems and MS/OR Methodology (Good News and Bad), Interfaces 18, Nr. 6, 105–113 (November–December 1988).

[23] D.E. O'Leary, Validation of expert systems with applications to auditing and accounting expert systems, Decision Sciences 18, 468–485 (1987).

[24] K. Parsaye, and M. Chignell, Expert Systems for Exerts (Wiley, New York, 1988).

[25] W.B. Rauch-Hindin, A Guide to Commercial Artificial Intelligence (Prentice-Hall, Englewood Cliffs, NJ, 1988).

[26] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ 1982).

[27] E. Turban, Decision Support and Expert Systems (Macmillan, NY, 1990).

[28] E. Turban, Expert Systems - Another Frontier for Industrial Engineering, Computers and Industrial Engineering 10, Nr. 3, 227-235 (1987).

[29] A. Walker, M. McCord, J.F. Sowa, and W.G. Wilson, Knowledge Systems and Prolog (Addison–Wesley, Reading, MA, 1987).

[30] L.F. Young, Decision Support and Idea Processing Systems (Wm. C. Brown, Dubuque, Iowa, 1989).

[31] L.F. Young, A Corporate strategy for decision support systems. In: R.H. Sprague and H.J. Watson, eds., Decision Support Systems: Putting Theory into Practice (Prentice-Hall, Englewood Cliffs, NJ, 1989).
