---
otero_id: 13078
otero_key: "D6BK76FQ"
title: "A mean–variance model to optimize the fixed versus open appointment percentages in open access scheduling systems"
authors: "Xiuli Qu; Ronald L. Rardin; Julie Ann S. Williams"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A mean–variance model to optimize the <sup>fi</sup>xed versus open appointment percentages in open access scheduling systems

Xiuli Qu <sup>a,</sup>⁎, Ronald L. Rardin <sup>b</sup>, Julie Ann S. Williams <sup>c</sup>

<sup>a</sup> North Carolina Agricultural and Technical State University, Department of Industrial and Systems Engineering, 1601 E. Market Street, Greensboro, NC 27411, United States

<sup>b</sup> University of Arkansas, Department of Industrial Engineering, 4169 Bell Engineering Center, Springdale, AR 72767, United States

<sup>c</sup> University of West Florida, Department of Management and MIS, 11000 University Parkway, Bldg 76/128, Pensacola, FL 32514-5752, United State

## a r t i c l e i n f o

Article history: Received 3 March 2011 Received in revised form 26 December 2011 Accepted 15 April 2012 Available online 24 April 2012

Keywords: Appointment scheduling Health care policy Service operations Open access scheduling Mean–variance model

## a b s t r a c t

Although healthcare quality may improve with short-notice scheduling and subsequently higher patient show-up rates, the variability in patient <sup>fl</sup>ow may negatively impact the service design. This study demonstrates how to select the percentage for short-notice or open appointments in an open access scheduling system subject to two quality performance metrics. Speci<sup>fi</sup>cally, we develop a mean–variance model and an ef<sup>fi</sup>cient solution procedure to help clinic administrators determine the open appointment percentage subject to increasing the average number of patients seen while also reducing the variability. Our numerical results indicate that for cases with high patient demand and high patient no-show rates for <sup>fi</sup>xed appointments, one or more Pareto optimal percentages of open appointments signi<sup>fi</sup>cantly decrease the variability in the number of patients seen with only a negligible decrease in the expected number of patients seen. While our method provides a useful tool for clinic administrators, it also presents a modeling foundation for open access scheduling with quality management objectives to smooth patient <sup>fl</sup>ow and improve capacity utilization.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Health expenditures have grown rapidly in all developed countries. Faced with the dual pressures of reducing costs and improving quality of care, hospitals have not only improved their operations but they have also shifted care from inpatient facilities to outpatient clinics since the 1980s [21,42]. Subsequently, outpatient primary care clinics have been forced to improve their just-in-time accessibility and use of limited capacity. A signi<sup>fi</sup>cant problem for primary care clinics is the traditional appointment scheduling system, which schedules patients’ routine check-ups months in advance. When a healthcare delivery system is viewed as a production system in which the deliverables are patients receiving healthcare services, production concepts related to scheduling and capacity management can be adapted to improve allocation of provider capacity. Healthcare delivery research is making important contributions to optimize elective surgery schedules under uncertain demand for emergency surgeries [8,20]. Unlike surgical appointment scheduling, primary care outpatient scheduling experiences signi<sup>fi</sup>cantly high patient no-shows while being constrained by a lower degree of <sup>fl</sup>exibility to increase capacity into emergency hours with emergency staff.

While over <sup>fi</sup>fty years of appointment scheduling research has focused on traditional appointment scheduling systems and its parameters [9,18,19,23–25,33,47] (see the review by Cayirli and Veral [5] and the review by Gupta and Denton [14]), our paper makes important contributions to determine the parameters for the new shortnotice scheduling systems. The key principle of short-notice scheduling is to see patients when they want to be seen, similar to the idea of just-in-time in the manufacturing industry. Throughout the paper, short-notice appointments are called open appointments, while appointments scheduled in advance are called fixed appointments. While scheduling a routine check-up months in advance accommodates patients who need longer lead times to accommodate transportation, work, family, or pre-test dietary intake arrangements, there are also several key costs that include a scarcity of appointment slots for short-notice acute care appointments and historically high patient no-show rates [2,11,22]. Therefore, the short-notice scheduling, called open access scheduling, advanced access scheduling or same-day scheduling, redesigns outpatient appointment scheduling systems to provide short-notice appointments for both routine check-ups and acute illnesses. Reports of successful implementation of open access scheduling in primary care clinics demonstrate its advantages: reduced patient no-show rates and cost per service as well as improved continuity of care, patient satisfaction, operational ef<sup>fi</sup>ciency and productivity of healthcare providers, including physicians, nurse practitioners, or physician's assistants [1,4,15,17,30, 35,36,40,44]. However, some failure stories to implement open access scheduling point out the dif<sup>fi</sup>culties in determining open access scheduling parameters when patient demand is high [29,31].

The critical parameters for open access scheduling systems are reported to be determined by expert's experiences rather than analytical methods. For example, the percentage of open appointments may range from 30% to 80% depending on the experiences of the expert managing the open access clinics [15,17,30]. Qu et al. [38] presented an analytical method to determine the percentage of open appointments that maximizes the expected number of patients consulted. Their numerical results demonstrate that the optimal percentage of open appointments to maximize the expected number of patients consulted mainly depends on the ratio of the average demand for open appointments to provider capacity and the ratio of the show-up rates for <sup>fi</sup>xed versus open appointments. However, the variability in the number of patients consulted is not considered. In an outpatient clinic, healthcare providers have to see all patients who show up for their appointments. High variability in the number of patients consulted per session may result in provider overtime in some sessions, while in other sessions it may result in long provider idle time and low capacity utilization which increases clinic operation costs and adversely affects the experiences of the patients and the staff [3,26,34,48]. Our paper extends the aforementioned analytical model to determine the percentage of open appointments in a critical way. We explicitly consider variability. We seek to not only maximize the average number of patients consulted but also minimize the variance in the number of patients consulted.

The structure of the paper is organized as follows. In the next section, we propose the mean–variance model to determine the percentage of open appointments for a healthcare provider, followed by a procedure to search all Pareto optimal solutions to the model in Section 3. Using the procedure, numerical cases are solved in Section 4 to examine the performance improvement using Pareto optimal percentages of open appointments, and the impacts of patient no-show rates and patient demand on the Pareto optimal solutions. The signi<sup>fi</sup>cance of our study is discussed in Section 5. Finally, potential future research is discussed and conclusions are drawn in Section 6.

## 2. Mean–variance model

A primary care provider typically sees patients in half-day sessions. Since the average number of patients consulted in each session affects the revenues and costs of a clinic as well as patient access, it is one of the key performance measures that concerns healthcare administrators and providers. Another performance measure concerning both healthcare administrators and providers is the variation in the number of patients consulted by each provider in each clinic session. The variation in the number of patients consulted results in clinic overtime and long patient waiting time in some sessions, but long provider idle time in other sessions. In a study [19], LaGanga and Lawrence discussed the challenges of managing varying patient attendance and the tradeoffs of overbooking, provider productivity, patient access, patient waiting time, and provider overtime. Their simulation results demonstrate that the average patient waiting time and the average clinic overtime increase as the variation in patient attendance increases. On the other hand, given the expected number of patients seen in a session, the average provider productivity decreases as the variation in the number of patients consulted in each clinic session increases [19]. The decrease of the average provider productivity is equivalent to the increase of the average provider idle time. The variation in the number of patients consulted in a session is caused by patient no-shows and the variation of patient demand for appointments. However, an appropriate percentage of open appointments could reduce the overall variability in an open access scheduling system. Therefore, the percentage of open appointments is better determined by considering both the expectation and the variance of the number of patients consulted.

## 2.1. Model assumptions

Recent research suggests that continuity of care can improve patient satisfaction, especially early in the patient relationship and for patients with worse health [39,41]. Some clinics group two to four providers as a provider team in an effort to balance continuity of care with scheduling <sup>fl</sup>exibility. We assume a healthcare provider's (or provider team's) schedule is independent of the schedules of other providers (or provider teams). Thus, we model appointment scheduling for one provider (or provider team).

We assume that the patients independently request appointments and independently choose appointments in other sessions when the desired session is full. Many discrete models for customer choice behavior make a similar assumption about independent customer choice [28,45]. Thus, patient demand in a session is independent of patient demands in other sessions. We assume that for a given provider (or provider team), the joint distribution of demands for <sup>fi</sup>xed and open appointments is known. Demand correlation between open and <sup>fi</sup>xed appointments within the same session may be positive, negative, or independent. In the numerical study section, we examine the sensitivity of Pareto optimal percentages of open appointments to independent, positively correlated, and negatively correlated demand distributions for <sup>fi</sup>xed and open appointments.

Since clinics have <sup>fi</sup>xed hours and a limited number of scheduled providers and exam rooms, the maximum number of patients that could be seen in a session without overtime is known. Then the total number of appointments to be scheduled in a session could be determined based on the maximum number of patients seen in a session, the average no-show rate and the acceptable possibility of clinic overtime [16,43,47]. In addition, we also assume that patient noshows are independent of each other, and the no-show rates of <sup>fi</sup>xed and open appointments are known. Meanwhile, it is assumed that no-show rates increase with the increase in the interval from the date an appointment is scheduled to the appointment date [2,11,22].

## 2.2. Formulation

Since the total number of appointments that can be scheduled with a healthcare provider in a session, denoted by N, is known, determining the optimal percentage of open appointments with a provider in a session is equivalent to determining the optimal number of <sup>fi</sup>xed appointments that can be scheduled with the provider in the session $\left( n _ { 1 } \right)$ . Thus, the mean–variance model to Pareto optimize the expectation and the variance (equivalently standard deviation) of the number of patients consulted can be formulated

$$
\begin{array}{l l} \left(\mathrm{P} _ {0}\right) & \text { maximize } E _ {n _ {1}} (\underset {\sim} {M}) \\ & \text { minimize } \sqrt {V _ {n _ {1}} (\underset {\sim} {M})} \\ & \text { subject   to } n _ {1} \leq N \\ & n _ {1} \text { is   integer } \end{array}
$$

where $M _ { \sim }$ denotes the random number of patients consulted by a pro-<sup>˜</sup>vider in a session, and $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( \underset { \sim } { M } )$ denote its expectation and <sup>ð ˜ Þ ð ˜ Þ</sup>variance, respectively, given that at most $n _ { 1 }$ <sup>fi</sup>xed appointments can be scheduled. The mean–variance model $\left( \mathrm { P _ { 0 } } \right)$ determines Pareto optimal allocations of open versus <sup>fi</sup>xed appointments that maximize the expected number of patients consulted while minimizing the standard deviation of the number of patients consulted. Pareto optimal solutions to the model $\left( \mathrm { P } _ { 0 } \right)$ provide more decision options for clinic administrators when they have to make a trade-off between the average number of patients seen and the variability in the number of patients seen.

## 3. Solution method

## 3.1. Expectation and variance of the number of patients consulted

To search a Pareto optimal solution to Problem $( \mathrm { P } _ { 0 } )$ , we <sup>fi</sup>rst derive the formulas to determine the expectation and the variance of the number of patients consulted, $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( M )$ . When a limited number of <sup>fi</sup>xed <sup>˜ ˜</sup>appointments can be scheduled with a provider in a session, the number of patients consulted (M) is a function of the total number of appoint-<sup>˜</sup>ments available (N), the limit of <sup>fi</sup>xed appointments to be scheduled $( n _ { 1 } ) _ { \cdot }$ , the no-show rates of <sup>fi</sup>xed and open appointments (denoted by $\gamma _ { 1 }$ and $\gamma _ { 2 } )$ , and the demand distribution for <sup>fi</sup>xed and open appointments (denoted by $D _ { 1 }$ and $D _ { 2 } )$ . The joint probability mass function of demands $D _ { 1 }$ and $\bar { D _ { \mathrm { 2 } } } \mathrm { i } \bar { \mathrm { s } } p ( d _ { \mathrm { 1 } } , \bar { d _ { \mathrm { 2 } } } ) = P \Big ( \bar { D } _ { \mathrm { 1 } } = \bar { d } _ { \mathrm { 1 } } , \bar { D } _ { \mathrm { 2 } } = \bar { d } _ { \mathrm { 2 } } \Big )$ for $d _ { 1 } = 0 , 1 , 2 , \cdots$ and $d _ { 2 } = 0 , 1 , 2 , \cdots$ 7

Let $M _ { 1 } ^ { ( n _ { 1 } ) }$ Þ and $M _ { 2 } ^ { ( n _ { 1 } ) }$ denote the random numbers of <sup>fi</sup>xed and open ap-<sup>˜ ˜</sup>pointments scheduled, respectively, with a provider in a clinic session. We know $\underset { \sim } { M } \overset { ( n _ { 1 } ) } { _ { 1 } } = \operatorname* { m i n } ( n _ { 1 } , \overset { \cdot } { _ { \sim } } 1 )$ and $\mathbf { \dot { \boldsymbol { M } } } _ { 2 } ^ { ( n _ { 1 } ) } = \operatorname* { m i n } ( \boldsymbol { N } - \underset { \sim } { M } _ { 1 } ^ { ( n _ { 1 } ) } , \underset { \sim } { D } _ { 2 } )$ . De<sup>fi</sup>ne in-<sup>˜ ˜</sup>dependent random variables

X <sup>n1</sup> ð Þ<sub>1i</sub> 1;if the patient with the<sup></sup> $\mathrm { i } ^ { \mathrm { t h } _ { \mathrm { f } } }$ fixed appointment in a session shows up

1

and

$\underset { ^ { \sim } 2 i } { \underbrace { X _ { 2 i } ^ { ( n _ { 1 } ) } } } = \left\{ \begin{array} { l l } { 1 } \\ { 0 } \end{array} \right.$ ;if the patient with the $\mathrm { i } ^ { \mathrm { t h } }$ open appointment in a session shows up ; otherwise

2

where $P ( X _ { \sim 1 i } ^ { ( n _ { 1 } ) } = 1 ) = 1 - \gamma _ { 1 }$ and $P ( X _ { \sim 2 i } ^ { ( n _ { 1 } ) } = 1 ) = 1 - \gamma _ { 2 } .$ . Thus

$$
\underset {\sim} {M} = \sum_ {i = 1} ^ {\underset {\sim} {M} ^ {(n _ {1})}} \underset {\sim} {X} _ {1 i} ^ {(n _ {1})} + \sum_ {i = 1} ^ {\underset {\sim} {M} ^ {(n _ {1})}} \underset {\sim} {X} _ {2 i} ^ {(n _ {1})}\tag{3}
$$

Therefore, $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( M )$ are also functions of $N , n _ { 1 } , \gamma _ { 1 } , \gamma _ { 2 }$ , and $p ( d _ { 1 } , d _ { 2 } )$ <sup>ð</sup>. Given N, $\gamma _ { 1 } , \gamma _ { 2 } ,$ <sup>ð</sup>and $p ( d _ { 1 } , d _ { 2 } )$ , Propositions 1 and 2 present recurrence relations to ef<sup>fi</sup>ciently calculate $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( M )$ for all $\boldsymbol { n _ { 1 } } { \in } \{ 0 ,  1 , { \ldots } , \boldsymbol { N } \}$ , respectively.

Proposition 1. Given N, $n _ { 1 } , \gamma _ { 1 } , \gamma _ { 2 } ,$ and $p ( d _ { 1 } , d _ { 2 } ) _ { i }$ , the expected number of patients consulted by a provider in a clinic session can be determined by a recurrence relation

$$
\begin{array}{l} E _ {n _ {1}} (\underset {\sim} {M}) = E _ {n _ {1} - 1} (\underset {\sim} {M}) - (\gamma_ {1} - \gamma_ {2}) [ 1 - F _ {1} (n _ {1} - 1) ] \\ \quad + (1 - \gamma_ {2}) [ F _ {2} (N - n _ {1}) - F (n _ {1} - 1, N - n _ {1}) ], f o r 0 <   n _ {1} \leq N, \end{array}
$$

with

4

$$
E _ {0} (\underset {\sim} {M}) = (1 - \gamma_ {2}) \left[ N - \sum_ {d _ {2} = 0} ^ {N} (N - d _ {2}) p _ {2} (d _ {2}) \right],\tag{5}
$$

where $F _ { 1 } ( \bullet ) , F _ { 2 } ( \bullet )$ , and $F ( \bullet )$ are the marginal and joint cumulative probability distribution functions of $D _ { 1 }$ and $\underset { \sim } { D } _ { 2 } ,$ , respectively, and $p _ { 2 } ( \bullet )$ is the probability mass function of $\boldsymbol { D } _ { 2 }$ <sup>˜</sup><sub>.</sub>

Proof. See Appendix A.

Proposition 2. Given N, $n _ { 1 } , \ \gamma _ { 1 } , \ \gamma _ { 2 } ,$ and $p ( d _ { 1 } , d _ { 2 } )$ , the variance of the number of patients consulted by a provider in a session can be determined by a recurrence relation

$$
\begin{array}{l} V _ {n _ {1}} (\underset {\sim} {M}) = V _ {n _ {1} - 1} (\underset {\sim} {M}) + \gamma_ {1} (1 - \gamma_ {1}) [ 1 - F _ {1} (n _ {1} - 1) ] \\ \qquad + (1 - \gamma_ {1}) ^ {2} [ 1 - F _ {1} (n _ {1} - 1) ] [ C _ {1} (n _ {1} - 1) + C _ {1} (n _ {1}) ] \\ \qquad - \gamma_ {2} (1 - \gamma_ {2}) G (n _ {1} - 1, N - n _ {1}) - (1 - \gamma_ {2}) ^ {2} G (n _ {1} - 1, N - n _ {1}) [ C _ {2} (n _ {1} - 1) \\ \qquad + C _ {2} (n _ {1}) ] + 2 (1 - \gamma_ {1}) (1 - \gamma_ {2}) \{G (n _ {1} - 1, N - n _ {1}) [ N - n _ {1} - C _ {1} (n _ {1} - 1) ] \\ \qquad - [ 1 - F _ {1} (n _ {1} - 1) ] [ N - n _ {1} - C _ {2} (n _ {1}) ] + C _ {3} (n _ {1} - 1, N - n _ {1}) \}, f o r 0 <   n _ {1} \leq N, \end{array}\tag{6}
$$

with

$$
\begin{array}{l} V _ {0} (\underset {\sim} {M}) = \gamma_ {2} (1 - \gamma_ {2}) [ N - C _ {2} (0) ] \\ \qquad + (1 - \gamma_ {2}) ^ {2} \left\{\sum_ {d _ {2} = 0} ^ {N} (N - d _ {2}) ^ {2} p _ {2} (d _ {2}) - [ C _ {2} (0) ] ^ {2} \right\}. \end{array}\tag{7}
$$

Here $G ( n _ { 1 } - 1 , ~ N - n _ { 1 } ) = 1 - F _ { 1 } ( n _ { 1 } - 1 ) - F _ { 2 } ( N - n _ { 1 } ) + F ( n _ { 1 } - 1 $ , N $- n _ { 1 } ) , \qquad C _ { 1 } ( n _ { 1 } ) = n _ { 1 } - E \biggl [ { \cal M } _ { 1 } ^ { ( n _ { 1 } ) } \biggr ] , \qquad C _ { 2 } ( n _ { 1 } ) = N - n _ { 1 } - E \biggl [ { \cal M } _ { 2 } ^ { ( n _ { 1 } ) } \biggr ]$ and $C _ { 3 } ( n _ { 1 } - 1 , N - n _ { 1 } ) = \sum _ { d _ { 2 } = 0 } ^ { N - n _ { 1 } } d _ { 2 } p _ { 2 } ( d _ { 2 } ) - \sum _ { d _ { 1 } = 0 } ^ { n _ { 1 } - 1 } \sum _ { d _ { 2 } = 0 } ^ { N - n _ { 1 } } d _ { 2 } p ( d _ { 1 } , d _ { 2 } ) ,$ where $E \left[ \underset { \sim } { M } _ { 1 } ^ { ( n _ { 1 } ) } \right] \mathrm { a n d } E \left[ \underset { \sim } { M } _ { 2 } ^ { ( n _ { 1 } ) } \right]$ , the expectations of $M _ { 1 } ^ { ( n _ { 1 } ) }$ and $M _ { 2 } ^ { ( n _ { 1 } ) }$ , can be calculated, respectively, by

$$
E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \right] = E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] + [ 1 - F _ {1} (n _ {1} - 1) ],\tag{8}
$$

and

$$
E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] = E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] - G (n _ {1} - 1, N - n _ {1}) \cdot\tag{9}
$$

Proof. See Appendix A.

## 3.2. Procedure to search Pareto optimal solutions

According to the recurrence relations in Propositions 1 and 2, a procedure is developed to <sup>fi</sup>nd all Pareto optimal solutions to Problem $\left( \mathrm { P } _ { 0 } \right)$ . Fig. 1 illustrates the steps in this procedure. In the procedure, the <sup>fi</sup>rst step is to calculate the marginal probabilities and the joint cumulative probabilities of the demands for <sup>fi</sup>xed and open appointments. In the second step, the expectations and the variances of the number of patients consulted, $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( M )$ , for all possible $n _ { 1 } ,$ are calcu-<sup>ð ˜ Þ ð ˜ Þ</sup>lated using Eqs. (4)–(7). The last step is to <sup>fi</sup>nd all Pareto optimal solutions by sorting and comparing all pairs of $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( M )$ . The detailed procedure is provided in Appendix B.

In this procedure, calculating the probabilities needed takes time $O ( N ^ { 2 } )$ , where N is the total number of appointments to be scheduled with a provider (or a provider team) in a clinic session. After that, calculating $E _ { n _ { 1 } } ( M )$ and $V _ { n _ { 1 } } ( M )$ for all possible $n _ { 1 }$ takes time $O ( N ^ { 2 } )$ . Lastly, <sup>ð ˜ Þ</sup>sorting all pairs of $E _ { n _ { 1 } } ( M )$ <sup>Þ</sup>and $V _ { n _ { 1 } } ( M )$ takes time ${ \cal O } ( N { \sf I } { \sf o g } N ) .$ , and iden-<sup>˜ ˜</sup>tifying all Pareto optimal solutions takes time $O ( N )$ . The procedure can quickly <sup>fi</sup>nd all Pareto optimal limits for the number of <sup>fi</sup>xed appointments to be scheduled in a primary care clinic of typical size. For example, Procedure 1 is coded using MATLAB 7.0.4 to search all Pareto optimal solutions. The computation time to <sup>fi</sup>nd all Pareto optimal solutions for any representative numerical case in the next section is less than 1 second on a DELL Pentium IV 2.8 G personal computer.

## 4. Numerical study

Using 540 representative numerical cases, we investigate the two questions of interest to the healthcare administrator: (1) Compared to the percentage of open appointments that maximizes the expected number of patients consulted, does the mean–variance model lead to better decisions on the allocation of open versus <sup>fi</sup>xed appointments? (2) How sensitive are the Pareto optimal allocations of open versus <sup>fi</sup>xed appointments to the patient demands and patient no-show rates? These questions focus on performance improvement using Pareto optimal allocations of open versus <sup>fi</sup>xed appointments, and the impacts of patient characteristics.

![](/api/attachments/D6BK76FQ/fulltext/images/fa27dd2f3fe47a26956e1e2f90e87c819a935c9a5455e17c863ca3bcb6e29662.jpg)  
Fig. 1. Flowchart of the procedure to <sup>fi</sup>nd all Pareto optimal solutions to Problem (P<sub>0</sub>).

## 4.1. Characteristics of numerical cases

The characteristics of the numerical cases were based on reallife examples from clinics visited. In an outpatient clinic, the total number of appointments to be scheduled represents the daily capacity of a provider. The clinics visited had 4-hour sessions in which 10–20 appointments were scheduled with a provider in a session. To examine the impact of the total number of appointments available, three levels are tested in the numerical cases: 12, 16 and 24.

Due to the national shortage of primary care providers, there are many primary care clinics where patient demand exceeds provider capacity [12,13,27]. To manage excess demand, clinic administrators and physicians control the patient panel size of each physician by limiting the number of new patients. Meanwhile, many clinics adopted open access scheduling to increase provider utilization by reducing patient no-show rates and by accepting more new patients [15,36,46]. Therefore, three levels of total average patient demand relative to provider capacity are considered in the numerical cases: $E ( \underbrace { D \phantom { 1 } } _ { \sim } + \underline { { { D } } } _ { 2 } ) = 0 . 8 N , E ( \underbrace { D \phantom { 1 } } _ { \sim } + \underline { { { D } } } _ { 2 } ) = N$ and $\begin{array} { r } { E ( { D _ { 1 } } + { D _ { 2 } } ) = 1 . 2 N . } \end{array}$ In addition, <sup>˜ ˜ ˜ ˜ ˜ ˜</sup>to examine the impact of equal and unequal demands for <sup>fi</sup>xed and open appointments, three demand allocations, $E ( \underset { \sim } { D } _ { 1 } ) { : } E ( \underset { \sim } { D } _ { 2 } ) = 1 { : } 4$ <sup>˜ ˜</sup>1:1 and 4:1, are assumed in the numerical cases. Since clinics experience seasonal surges in demand such as <sup>fl</sup>u season, testing three demand allocations will provide insights into whether the capacity allocation should be adjusted for seasonality.

Since the demand for <sup>fi</sup>xed or open appointments is the number of requests for appointments occurring in a given time period, a Poisson distribution is a routine choice for the demand. When all <sup>fi</sup>xed appointment slots in a session are full, some patients may call back later for an open appointment in their desired session. This results in the positive correlation between the demands for <sup>fi</sup>xed and open appointments in a session. On the other hand, if the patient panel size is assumed to be stable, the decrease in the demand for <sup>fi</sup>xed appointments leads to the increase in the demand for open appointments. That means that the demand for open appointments in a session may be negatively correlated with that for <sup>fi</sup>xed appointments in the session. Therefore, in the numerical cases, the demands for <sup>fi</sup>xed and open appointments are assumed to have independent Poisson distributions or a bivariate Poisson distribution with correlation coef-<sup>fi</sup>cient of −0.4, −0.2, 0.2 or 0.4.

Since <sup>fi</sup>xed appointments can be scheduled weeks in advance, their no-show rates can reach as high as 50–55% according to the literature [11,22]. On the other hand, the no-show rate of open appointments reported in the literature is 3–16% [4]. In the study of Qu et al. [38], four combinations of the no-show rates of <sup>fi</sup>xed and open appointments are investigated: (0.1556, 0.05), (0.2, 0.1), (0.3667, 0.05), and (0.4, 0.1). For comparison, the same combinations of the no-show rates are considered in the numerical cases here. Table 1 summarizes the levels of provider capacity (N), the no-show rates $( \gamma _ { 1 } , \gamma _ { 2 } )$ , and the demand distribution for <sup>fi</sup>xed and open appointments. Combining these levels generates the 540 numerical cases.

4.2. Performance of optimal allocations determined by the mean–variance model

As mentioned earlier, Qu et al. [38] present a method to determine the percentage of open appointments that maximizes the expected number of patients consulted. Let $\pi ^ { U }$ denote the percentage maximizing the expected number of patients consulted, which is an optimal solution to the model presented in the study of Qu et al. [38] and one of the Pareto optimal solutions to the mean–variance model $( \mathrm { P } _ { 0 } )$ . For any case, $\pi ^ { U }$ leads to a higher expectation and a higher standard deviation of the number of patients consulted than other Pareto optimal percentages of open appointments. However, in many numerical cases, some Pareto optimal percentage signi<sup>fi</sup>cantly decreases the standard deviation while only slightly decreasing the expectation of the number of patients consulted. In such cases, the mean–variance model $\left( \mathrm { P } _ { 0 } \right)$ provides better decision-making options for the allocation of open versus <sup>fi</sup>xed appointments. Fig. 2 illustrates the performance comparison between $\dot { \pi } ^ { \dot { U } }$ and the Pareto optimal percentages of open appointments in terms of the relative decreases in the standard deviation and the expectation of the number of patients consulted. Fig. 2(a) shows that in more than 80% of 540 numerical cases, the percentage of the decrease in the standard deviation of the number of patients consulted is greater than the percentage of the decrease in the expected number of patients consulted. In these cases, the average relative decrease in the standard deviation is 5.82%, and the magnitude of average decrease in the standard deviation is 0.16. The results of LaGanga and Lawrence [19] implies that the decrease of 0.16 in the standard deviation, on average, results in a decrease of about 4 min in the average patient waiting time and a decrease of about 7 min in the average clinic overtime. Fig. 2(b) demonstrates that the standard deviation of the number of patient consulted decreases by less than 0.1% in about 25% of the 540 numerical cases, by 0.1%–1% in about 30% of all cases, by 1%–5% in about 23% of all cases, and by more than 5% in about 22% of all cases. Furthermore, Fig. 2(a) also reveals that in about 25% of the 540 numerical cases, the percentage of the decrease in the standard deviation is more than 10 times greater than the percentage of the decrease in the expected number of patients consulted.

Levels of clinic and patient characteristics in numerical cases.

<table><tr><td colspan="2">Clinic characteristics</td><td>Levels</td></tr><tr><td colspan="2">Total number of appointments to be scheduled (N), i.e. provider capacity</td><td>12, 16, and 24</td></tr><tr><td colspan="2">No-show rates of fixed and open appointments ( $\gamma_1$ ,  $\gamma_2$ )</td><td>(0.1556, 0.05), (0.2, 0.1), (0.3667, 0.05), and (0.4, 0.1)</td></tr><tr><td rowspan="2">Patient demand</td><td>Distribution of $D_1$ and $D_2$ </td><td>Independent Poisson distributions and Bivariate Poisson distributions with correlation coefficient ( $\rho$ ) of -0.4, -0.2, 0.2 and 0.4</td></tr><tr><td>Average demands for fixed and open appointments ( $E(D_1)$ ,  $E(D_2)$ )</td><td> $E(D_1 + D_2) = 0.8N$ (0.16N, 0.64N), (0.4N, 0.4N), (0.64N, 0.16N) $E(D_1 + D_2) = N$ (0.2N, 0.8N), (0.5N, 0.5N), (0.8N, 0.2N) $E(D_1 + D_2) = 1.2N$ (0.24N, 0.96N), (0.6N, 0.6N), (0.96N, 0.24N)</td></tr></table>

![](/api/attachments/D6BK76FQ/fulltext/images/1c8f81791e640d00519ed85bea22f5fcf7048deb812fd114cb68d7c727d8fc09.jpg)  
Ratio of the percentage of the decrease in the standard deviation versus the percentage of the decrease in the expectation of the number of patients consulted

![](/api/attachments/D6BK76FQ/fulltext/images/3cd6643cf695498723a1a64ca7da522a4d03624124365424a2b7f3d4100d818c.jpg)  
Fig. 2. Performance comparison between Pareto optimal percentages of open appointments and the percentage that only maximizes the expected number of patients consulted.

Table 2 illustrates 22 cases in which a Pareto optimal percentage decreases the standard deviation by at least 3% while decreasing the expectation by at most 0.6%. In one of the cases highlighted in Table 2, a Pareto optimal percentage decreases the standard deviation by 17.22% while decreasing the expectation only by 0.59%. In all 22 cases, the total average patient demand is higher than the provider capacity, and the no-show rate of <sup>fi</sup>xed appointments is at the high level (i.e. 36.67% or 40%). This implies that for a case with high patient demand and a high no-show rate of <sup>fi</sup>xed appointments, one or more Pareto optimal percentages of open appointments may signi<sup>fi</sup>cantly decrease the variation in the number of patients consulted while only slightly decreasing the expected number of patients consulted. Therefore, for such clinics the mean–variance model could provide better decision options for the allocation of open versus <sup>fi</sup>xed appointments.

4.3. Sensitivity of Pareto optimal solutions to patient demand and no-show rates

Before discussing the details of the sensitivity analysis, we begin with a discussion of two of the typical mean–variance curves from the 540 numerical cases. Fig. 3(a) illustrates the mean–variance curve and Pareto optimal solutions for a case with provider capacity $N = 1 2$ , no-show rates $\gamma _ { 1 } = 0 . 3 6 6 7$ and $\gamma _ { 2 } = 0 . 0 5$ , and positively correlated demands for <sup>fi</sup>xed and open appointments. Each point on the curve depicts the expectation and the standard deviation of the number of patients consulted for one feasible solution of the case. For this case, the feasible solutions are $n _ { 1 } = 0 , 1 , . . . , 1 2 ,$ where $n _ { 1 }$ is the number of <sup>fi</sup>xed appointments allowed to be scheduled. Since some feasible solutions, such as $n _ { 1 } = 1 0 ,$ , 11 and 12, have very close expectations and standard deviations, the points (markers) corresponding to these feasible solutions overlap in Fig. 3(a). Solid points on the mean–variance curve represent Pareto optimal solutions, which are not dominated by any other feasible solution. Similarly, Fig. 3(b) illustrates the mean–variance curve and Pareto optimal solutions for another case with provider capacity $N = 1 2 ,$ no-show rates $\gamma _ { 1 } = 0 . 3 6 6 7$ and $\gamma _ { 2 } = 0 . 0 5$ , and positively correlated demands for <sup>fi</sup>xed and open appointments. The difference between the two cases is that the case in Fig. 3(b) has a total average patient demand 20% higher than provider capacity while the case in Fig. 3(a) has a total average patient demand 20% lower than provider capacity. Next, we discuss the impact of patient demand and no-show rates on the mean–variance curves and the Pareto optimal solutions.

Fig. 4 demonstrates that the mean–variance curve shape and the ef<sup>fi</sup>cient frontier shape for each case do not depend solely on provider capacity. Instead, the mean–variance curve shape and the ef<sup>fi</sup>cient frontier shape depend on the relationship between average patient demand and provider capacity. Since the average patient demands in the numerical cases are determined based on the relationship between average patient demand and provider capacity, we compare the mean–variance curves and Pareto optimal solutions for 72 cases with the same provider capacity N=16, which are illustrated in Fig. 5. For the cases in Fig. 5(a), (c) and (e), the total average demand for <sup>fi</sup>xed and open appointments is 20% lower than provider capacity, while for the cases in Fig. 5(b), (d) and (f), the total average demand is 20% higher than provider capacity. Meanwhile, the ratio of the average demands for <sup>fi</sup>xed versus open appointments is 1:1 for the cases in Fig. 5(a) and (b), is 1:4 for the cases in Fig. 5(c) and (d), is 4:1 for the cases in Fig. 5(e) and (f).

Fig. 5(a), (c) and (e) demonstrates that for the cases with patient demand lower than provider capacity, the average patient demands and the demand correlation for <sup>fi</sup>xed and open appointments dominates the shapes of mean–variance curves and ef<sup>fi</sup>cient frontiers. Compared with the average patient demand and the demand correlation, the no-show rates of <sup>fi</sup>xed and open appointments have less sig ni<sup>fi</sup>cant effect on the shapes of mean–variance curves and ef<sup>fi</sup>cient frontiers. Fig. 5(e) reveals that for the cases with patient demand lower than provider capacity and the average demand for open appointments lower than that for <sup>fi</sup>xed appointments, the ef<sup>fi</sup>cient frontier includes all feasible solutions. For a few cases in Fig. 5(a), the ef<sup>fi</sup>cient frontier also includes all feasible solutions. The reason is that when provider capacity is much higher than patient demand, most requests for appointments are granted, which results in the simultaneous increases in the expectation and the standard deviation of the number of patients consulted. For such cases, the percentage of open appointments has to be determined by making a trade-off between the expectation and the variance of the number of patients consulted. One way to make this trade-off is to choose the percentage of open appointments for a provider (or a provider team) that maximizes the expectation while ensuring that the variance does not exceed the desired value. However, Fig. 5(c) shows that for the cases with patient demand lower than provider capacity and the average demand for open appointments higher than that for <sup>fi</sup>xed appointments, the standard deviation of the number of patients consulted may decrease with the increase in the expectation.

Numerical cases in which a Pareto optimal percentage signi<sup>fi</sup>cantly decreases the standard deviation while slightly decreasing the expectation of the number of patients consulted.

<table><tr><td rowspan="2">Provider capacity (N)</td><td colspan="3">Patient demand</td><td colspan="2">No-show rate</td><td colspan="2">Using  $\pi^{U}$ </td><td colspan="2">Using a Pareto optimal percentage</td><td colspan="2">Percentage of the decrease</td></tr><tr><td> $E(D_1)$ </td><td> $E(D_2)$ </td><td> $\rho$ </td><td> $\gamma_1$ </td><td> $\gamma_2$ </td><td>Expected number</td><td>Standard deviation</td><td>Expected number</td><td>Standard deviation</td><td>Expected number</td><td>Standard deviation</td></tr><tr><td rowspan="2">12</td><td rowspan="2">7.2</td><td rowspan="2">7.2</td><td rowspan="2">-0.2</td><td>0.3667</td><td>0.05</td><td>8.946</td><td>1.728</td><td>8.937</td><td>1.666</td><td>0.11%</td><td>3.57%</td></tr><tr><td>0.4</td><td>0.1</td><td>8.476</td><td>1.768</td><td>8.467</td><td>1.714</td><td>0.11%</td><td>3.06%</td></tr><tr><td rowspan="10">16</td><td rowspan="6">3.84</td><td rowspan="6">15.36</td><td rowspan="2">0</td><td>0.3667</td><td>0.05</td><td>13.654</td><td>1.953</td><td>13.604</td><td>1.734</td><td>0.37%</td><td>11.23%</td></tr><tr><td>0.4</td><td>0.1</td><td>12.936</td><td>2.026</td><td>12.888</td><td>1.838</td><td>0.37%</td><td>9.31%</td></tr><tr><td rowspan="2">0.2</td><td>0.3667</td><td>0.05</td><td>13.639</td><td>1.967</td><td>13.614</td><td>1.837</td><td>0.18%</td><td>6.59%</td></tr><tr><td>0.4</td><td>0.1</td><td>12.921</td><td>2.037</td><td>12.897</td><td>1.925</td><td>0.18%</td><td>5.50%</td></tr><tr><td rowspan="2">-0.4</td><td>0.3667</td><td>0.05</td><td>13.706</td><td>1.786</td><td>13.670</td><td>1.615</td><td>0.26%</td><td>9.57%</td></tr><tr><td>0.4</td><td>0.1</td><td>12.984</td><td>1.883</td><td>12.951</td><td>1.739</td><td>0.26%</td><td>7.68%</td></tr><tr><td rowspan="4">9.6</td><td rowspan="4">9.6</td><td rowspan="2">0.4</td><td>0.3667</td><td>0.05</td><td>11.956</td><td>2.148</td><td>11.940</td><td>2.060</td><td>0.14%</td><td>4.09%</td></tr><tr><td>0.4</td><td>0.1</td><td>11.327</td><td>2.177</td><td>11.312</td><td>2.099</td><td>0.14%</td><td>3.58%</td></tr><tr><td rowspan="2">-0.4</td><td>0.3667</td><td>0.05</td><td>12.158</td><td>1.939</td><td>12.151</td><td>1.866</td><td>0.06%</td><td>3.76%</td></tr><tr><td>0.4</td><td>0.1</td><td>11.518</td><td>1.995</td><td>11.511</td><td>1.932</td><td>0.06%</td><td>3.18%</td></tr><tr><td rowspan="10">24</td><td rowspan="8">5.76</td><td rowspan="8">23.04</td><td rowspan="2">0</td><td>0.3667</td><td>0.05</td><td>20.862</td><td>2.300</td><td>20.778</td><td>2.028</td><td>0.40%</td><td>11.85%</td></tr><tr><td>0.4</td><td>0.1</td><td>19.764</td><td>2.406</td><td>19.745</td><td>2.263</td><td>0.10%</td><td>5.95%</td></tr><tr><td rowspan="2">0.2</td><td>0.3667</td><td>0.05</td><td>20.849</td><td>2.312</td><td>20.811</td><td>2.158</td><td>0.18%</td><td>6.66%</td></tr><tr><td>0.4</td><td>0.1</td><td>19.751</td><td>2.416</td><td>19.716</td><td>2.284</td><td>0.18%</td><td>5.45%</td></tr><tr><td rowspan="2">-0.2</td><td>0.3667</td><td>0.05</td><td>20.870</td><td>2.298</td><td>20.747</td><td>1.955</td><td>0.59%</td><td>14.93%</td></tr><tr><td>0.4</td><td>0.1</td><td>19.771</td><td>2.404</td><td>19.715</td><td>2.162</td><td>0.29%</td><td>10.05%</td></tr><tr><td rowspan="2">-0.4</td><td>0.3667</td><td>0.05</td><td>20.877</td><td>2.295</td><td>20.753</td><td>1.900</td><td>0.59%</td><td>17.22%</td></tr><tr><td>0.4</td><td>0.1</td><td>19.779</td><td>2.402</td><td>19.701</td><td>2.093</td><td>0.39%</td><td>12.84%</td></tr><tr><td rowspan="2">14.4</td><td rowspan="2">14.4</td><td rowspan="2">0</td><td>0.3667</td><td>0.05</td><td>18.415</td><td>2.424</td><td>18.406</td><td>2.312</td><td>0.05%</td><td>4.64%</td></tr><tr><td>0.4</td><td>0.1</td><td>17.446</td><td>2.488</td><td>17.437</td><td>2.390</td><td>0.05%</td><td>3.94%</td></tr></table>

(a) E( D ) = E( D ) = 4.8 and = 0.2  
![](/api/attachments/D6BK76FQ/fulltext/images/4984c87ff3ccfc816a8aba20a01ff845abf3d9e6dd0f2750398d4abab62c3c1a.jpg)

(b) E( D ) = E( D ) = 7.2 and = 0.2  
![](/api/attachments/D6BK76FQ/fulltext/images/d8fe3c6f1a1bfa29dd803b8a122c27afd3e60dc4e1f158dc5eecac180ce65fb3.jpg)  
Fig. 3. Mean-variance curves for two cases with $N = 1 2 , \gamma _ { 1 } = 0 . 3 6 6 7$ and $\gamma _ { 2 } = 0 . 0 5 .$

On the other hand, Fig. 5(b), (d) and (f) demonstrates that for the cases with patient demand higher than provider capacity, the average patient demands for <sup>fi</sup>xed and open appointments dominate the shapes of mean–variance curves and ef<sup>fi</sup>cient frontiers. The effect of the no-show rates on the shapes of mean–variance curves and ef<sup>fi</sup>- cient frontiers is less signi<sup>fi</sup>cant than the effect of the average demands, but is more signi<sup>fi</sup>cant than the effect of the correlation between the demands for <sup>fi</sup>xed and open appointments. Fig. 5(b) and (d) shows that for the cases with patient demand higher than provider capacity and the average demand for open appointments not less than that for <sup>fi</sup>xed appointments, Pareto optimal percentages

![](/api/attachments/D6BK76FQ/fulltext/images/c9d5b318fef7cc6714a52b01aa73a3eb8fb419018aa5e6fa8ad8e167089f5251.jpg)

<table><tr><td></td><td>N = 12</td><td>N = 16</td><td>N = 24</td></tr><tr><td rowspan="3"> $E(D_1 + D_2) =$ </td><td> $\cdot \diamond \cdot 1.2N$ </td><td> $\cdot \square \cdot 1.2N$ </td><td> $\cdot \triangle \cdot 1.2N$ </td></tr><tr><td> $\cdot \diamond \cdot -N$ </td><td> $\cdot \square \cdot -N$ </td><td> $\cdot \triangle \cdot -N$ </td></tr><tr><td> $\diamond \cdot 0.8N$ </td><td> $\square \cdot 0.8N$ </td><td> $\triangle \cdot 0.8N$ </td></tr></table>

Fig. 4. Mean–variance curves for the cases with $\begin{array} { r } { E ( \underset { \sim } { D } _ { 1 } ) = E ( \underset { \sim } { D } _ { 2 } ) , \gamma _ { 1 } = 0 . 3 6 6 7 , \gamma _ { 1 } = 0 . 0 5 , } \end{array}$ <sup>˜ ˜</sup>and =0.2 for three provider capacities (N=12, 16, and 24).

![](/api/attachments/D6BK76FQ/fulltext/images/a9dce04d0ace55d34bab369db2c2cf43fa013e4d0750a276083853ad93b016d5.jpg)  
Fig. 5. Mean-variance curves for the cases with $N = 1 6 .$

have very close expectations and standard deviations, or one or more Pareto optimal percentages signi<sup>fi</sup>cantly reduce the standard deviation while only slightly decreasing the expectation. This observation reveals that for such cases the percentage of open appointments that minimizes the standard deviation is a good choice for open access scheduling because it only slightly decreases the expected number of patients consulted. It also supports that for a clinic with high patient demand and high no-show rates for <sup>fi</sup>xed appointments, the mean–variance model could provide better decision options for the allocation of open versus <sup>fi</sup>xed appointments.

## 5. Discussion

An open access scheduling system requires clinic administrators to make additional new decisions when compared to decision making in traditional appointment scheduling systems. One of these new decisions is the percentage of open appointments, which we have shown in this paper impacts the number of patients seen. In this paper, we propose a mean–variance model and a solution procedure for clinic administrators to determine the percentage of open appointments subject to two objectives: (1) maximizing the average number of patients seen, and (2) minimizing the variability in the number of patients seen. Our numerical results indicate that Pareto optimal solutions to our mean–variance model may decrease the standard deviation by up to 17.22% while decreasing the expectation by only 0.59% when compared to the earlier model in the study of Qu et al. [38]. Meanwhile, the proposed procedure reports all Pareto optimal percentages of open appointments, which provides all of the best options for clinic administrators to determine the percentage of slots reserved for open appointments based on their priorities and concerns. For example, clinic administrators could use our model to reduce the variability in the number of patients seen and to smooth patient <sup>fl</sup>ows.

The results of this study also provide insights for clinic administrators to improve the allocation of provider capacity. First, for a clinic with low patient demand for total appointments and either lower demand for open appointments (see Fig. 5(e)), or higher or equal demand for open appointments independent of or positively correlated with demand for <sup>fi</sup>xed appointments (see Fig. 5(a) and (c)), clinic administrators have to determine the percentage of open appointments by making a trade-off between the expected number of patients seen and the variability in the number of patients seen because the expectation and the variance of the number of patients seen increase simultaneously. One way to make this trade-off is to choose the percentage of open appointments for a provider (or a provider team) that maximizes the expectation while ensuring that the variance does not exceed the desired limit. On the other hand, if the clinic has low demand for total appointments as well as higher or equal demand for open appointments negatively correlated with demand for <sup>fi</sup>xed appointments (see Fig. 5(a) and (c)), clinic administrators can optimize the expectation and variance simultaneously. If a clinic has high patient demands for total appointments and open appointments, clinic administrators could choose the percentage of open appointments that minimizes the variability in the number of patients seen, while only negligibly decreasing the average number of patients seen. Our results indicate that clinic administrators should adopt strategies to increase patient demand for open appointments and subsequently improve the performance of an open access scheduling system. The long-term strategy to increase patient demand is to improve the quality of and the access to clinical services [10,44], while there are many short-term strategies such as informing the clinic's patients how to request open appointments, mailing the local community brochures introducing the advantages of open access scheduling, etc. [10].

In addition, the ability to manage the trade-offs between the mean and the variance of the patient <sup>fl</sup>ow is critical to the performance of open access scheduling systems. In the open access clinics we visited, clinic administrators always need to make the trade-offs between the average number of patients seen per clinic session and clinic overtime and patient waiting time caused by the uncertainty of patient <sup>fl</sup>ow. Meanwhile, the negative impacts of the variation in patient attendance on a scheduling system have been investigated in other studies [3,19,32]. For example, as the variation in patient attendance increases, the average patient waiting time, the average provider idle time, and the average clinic overtime increase [19]. The mean–variance model and the recursive procedure proposed are a useful tool for clinic administrators to make the appropriate trade-offs between the average number of patients seen per clinic session and the negative impact of the variation in patient attendance.

From a research perspective, the results of our research offer evidence that model-based decisions may improve process quality and capacity management, particularly in healthcare [6,37]. Since the quality of care depends on healthcare access and process quality at least as much as clinical quality, model-based decision approaches can help healthcare administrators determine how to allocate their resources [7]. In most capacity management studies, patient waiting cost, provider idle cost and/or overtime cost are considered as objectives. The variation in the number of patient arrivals per clinic session, which directly affects these costs, is considered as one of the objectives in the mean–variance model proposed in this paper. This idea could be applied in other capacity management models to improve decision making in other service sectors. Reducing the variance in healthcare provider utilization may also have positive impacts on medical supply inventories, an interesting supply chain implication for future research.

## 6. Limitation and conclusions

Our analytical approach required several limiting assumptions. We assumed that the patient demand between sessions is independent. An important research question is how to relax this assumption by considering more than one session for optimization and the impact of correlated patient demands between sessions. While the research presented here assumed that a healthcare provider has a <sup>fi</sup>xed number of slots per session (<sup>fi</sup>xed N), a future direction is to allow limited <sup>fl</sup>uctuation for N. If demand varies widely over time (for example high acute condition appointment demand during <sup>fl</sup>u season or high demand for routine check-ups prior to the start of the academic year), an interesting question is to examine the impact of scheduling if forecasted demand varies and limited capacity modi-<sup>fi</sup>cations are allowed.

Our analytical approach provides a decision‐making tool needed by healthcare administrators considering or managing an open access scheduling system. We introduce the <sup>fi</sup>rst mean–variance model to determine the percentage of open appointments for a provider (or a provider team). Then we prove the recurrence relation for the variance of the number of patients consulted, given the total number of appointments available, the no-show rates, and the demand distributions for <sup>fi</sup>xed and open appointments. According to the recurrence relations for the expectation and the variance of the number of patients consulted, a recursive procedure is proposed to ef<sup>fi</sup>ciently calculate all expectations and variances, and then a search checks all Pareto optimal solutions to the mean–variance model. When compared to a single objective model that maximizes the patients seen, our mean–variance model can improve clinic operations by reducing the variability in the number of patients seen while maintaining high levels of patient consultations.

In closing, our research extends the <sup>fi</sup>rst model for open access scheduling by evaluating not only the expected number of patients consulted but also the variance in the number of patients consulted in an effort to help healthcare administrators achieve greater capacity management, patient access, and smoother patient <sup>fl</sup>ow through improved patient scheduling. Each of the future research directions will extend the discussion from here to address patient scheduling needs for short lead time and provider continuity.

## Acknowledgments

The authors want to thank the administrators, physicians, and staff in the Indiana University Medical Group—Primary Care clinics for providing insights into traditional and open access appointment scheduling in outpatient clinics. The authors are grateful to Professor Bruce W. Schmeiser of Purdue University for the valuable discussions and references. The authors also gratefully acknowledge the support from the Regenstrief Center for Healthcare Engineering.

## Appendix A. Proofs

Proof of Proposition 1. The number of patients consulted with a provider in a clinic session is $\underset { \sim } { M } = \sum _ { i = 1 } ^ { M ^ { ( n _ { 1 } ) } } \underset { \sim } { X } _ { 1 i } ^ { ( n _ { 1 } ) } + \sum _ { i = 1 } ^ { M ^ { ( n _ { 1 } ) } } \underset { \sim } { X } _ { 2 i } ^ { ( n _ { 1 } ) }$ where $\underline { { M } } _ { 1 } ^ { ( n _ { 1 } ) } = \operatorname* { m i n } ( n _ { 1 } , \underline { { D } } _ { 1 } ) , ~ \underline { { M } } _ { 2 } ^ { ( n _ { 1 } ) } = \operatorname* { m i n } ( N - \underline { { M } } _ { 1 } ^ { ( n _ { 1 } ) } , \underline { { D } } _ { 2 } )$ , and $\underset { \sim } { X } _ { 1 i } ^ { ( n _ { 1 } ) }$ and $X _ { \sim 2 i } ^ { ( n _ { 1 } ) }$ are independent Bernoulli random variables with $P ( \underset { \sim } { X } _ { 1 i } ^ { ( n _ { 1 } ) } = 1 ) = 1$ $- \gamma _ { 1 }$ and $P ( \underset { \sim } { X } _ { 2 i } ^ { ( n _ { 1 } ) } = 1 ) = 1 - \gamma _ { 2 } ,$ , respectively. Thus, the expected number of patients consulted with the provider in the session is

$$
E _ {n _ {1}} (\underset {\sim} {M}) = (1 - \gamma_ {1}) E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \right] + (1 - \gamma_ {2}) E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right].\tag{A.1}
$$

When the limit of <sup>fi</sup>xed appointments to be scheduled increases from $n _ { 1 } - 1$ to $n _ { 1 }$ , the number of <sup>fi</sup>xed appointments scheduled increases by 1 if $\begin{array} { r } { D _ { 1 } > n _ { 1 } - 1 ; } \end{array}$ otherwise, the number does not change. Thus

$$
\begin{array}{r l} E \bigg [ \widetilde {M} _ {1} ^ {(n _ {1})} \bigg ] & = E \bigg [ \widetilde {M} _ {1} ^ {(n _ {1} - 1)} \bigg ] + 1 \times P \bigg (\widetilde {D} _ {1} > n _ {1} - 1 \bigg) + 0 \times P \bigg (\widetilde {D} _ {1} \leq n _ {1} - 1 \bigg) \\ & = E \bigg [ \widetilde {M} _ {1} ^ {(n _ {1} - 1)} \bigg ] + [ 1 - F _ {1} (n _ {1} - 1) ] \cdot \end{array}\tag{A.2}
$$

On the other hand, when the limit of <sup>fi</sup>xed appointments to be scheduled increases from $n _ { 1 } - 1$ to $n _ { 1 } ,$ , the number of open appointments scheduled decreases by 1 if $\textstyle D _ { 1 } > n _ { 1 } - 1$ and $D _ { 2 } \geq N - ( n _ { 1 } - 1 ) ;$ ; other-<sup>˜</sup>wise, the number does not change. Thus

$$
\begin{array}{l} E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] = E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] + (- 1) \times P \left(\underset {\sim} {D} _ {1} > n _ {1} - 1 \text { and } \underset {\sim} {D} _ {2} \geq N - n _ {1} + 1\right) \\ \quad + 0 \times P \left(\underset {\sim} {D} _ {1} \leq n _ {1} - 1 \text { or } \underset {\sim} {D} _ {2} <   N - n _ {1} + 1\right) \\ \quad = E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] - [ 1 - F _ {1} (n _ {1} - 1) - F _ {2} (N - n _ {1}) + F (n _ {1} - 1, N - n _ {1}) ]. \end{array}\tag{A.3}
$$

By substituting Eqs. (A.2) and (A.3) into Eq. (A.1), Eq. (4) is proven.

Next, we derive the initial condition for calculating $E _ { n _ { 1 } } ( M )$ . When $n _ { 1 } = 0 , M _ { 1 } ^ { ( 0 ) } { = } 0$ and $M _ { 2 } ^ { ( 0 ) }$ equals the minimum of $D _ { 2 }$ <sup>ð ˜ Þ</sup>and N. Thus

$$
\begin{array}{l} E \left[ \underset {\sim} {M} _ {2} ^ {(0)} \right] = E \left[ \min \left(\underset {\sim} {D} _ {2}, N\right) \right] = \sum_ {d _ {2} = 0} ^ {N} d _ {2} p _ {2} (d _ {2}) + \sum_ {d _ {2} = N + 1} ^ {\infty} N p _ {2} (d _ {2}) \\ = N - \sum_ {d _ {2} = 0} ^ {N} (N - d _ {2}) p _ {2} (d _ {2}) \cdot \end{array}\tag{A.4}
$$

Substituting $E \biggl [ \underset { \sim } { M } _ { 1 } ^ { ( 0 ) } \biggr ] = 0$ and $\operatorname { E q . } \ ( \mathsf { A . 4 } )$ into $\operatorname { E q . } \ ( \mathrm { A . 1 } )$ , we obtain Eq. (5).

Proof of Proposition 2. Let $V a r \bigg \vertupmu _ { \sim } ^ { ( n _ { 1 } ) } \bigg \vert$ and $V a r \bigg [ \underset { \sim } { M } _ { 2 } ^ { ( n _ { 1 } ) } \bigg ]$ denote the variances of $M _ { 1 } ^ { ( n _ { 1 } ) }$ and $M _ { 2 } ^ { ( n _ { 1 } ) }$ , respectively, and $C o \nu \bigg [ \underset { \sim } { M } _ { 1 } ^ { ( n _ { 1 } ) } , \underset { \sim } { M } _ { 2 } ^ { ( n _ { 1 } ) } \bigg ]$ denote the covariance of $\mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } } \mathbf { \stackrel { . } { \sim } }$ and $M _ { 2 } ^ { ( n _ { 1 } ) }$ . Since it is assumed that patient no-shows are independent of each other and the no-show rates of <sup>fi</sup>xed and open appointments $( \gamma _ { 1 }$ and $\gamma _ { 2 } )$ are known, the variance of the number of patients consulted by a provider in a session is

$$
\begin{array}{c} V _ {n _ {1}} (\underset {\sim} {M}) = \gamma_ {1} (1 - \gamma_ {1}) E \bigg [ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \bigg ] + (1 - \gamma_ {1}) ^ {2} V a r \bigg [ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \bigg ] + \gamma_ {2} (1 - \gamma_ {2}) E \bigg [ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \bigg ] \\ + (1 - \gamma_ {2}) ^ {2} V a r \bigg [ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \bigg ] + 2 (1 - \gamma_ {1}) (1 - \gamma_ {2}) C o v \bigg [ \underset {\sim} {M} _ {1} ^ {(n _ {1})}, \underset {\sim} {M} _ {2} ^ {(n _ {1})} \bigg ]. \end{array}\tag{A.5}
$$

When the limit of <sup>fi</sup>xed appointments to be scheduled increases from $n _ { 1 } - 1$ to $n _ { 1 } ,$ the number of <sup>fi</sup>xed appointments scheduled increases by 1 if $_ { \sim } \mathrm { D } _ { 1 } { > } n _ { 1 } - 1$ , and the number of open appointments <sup>˜</sup>scheduled decreases by 1 if $_ { \sim }  { D _ { 1 } } > n _ { 1 } - 1$ and $\begin{array} { r } { D _ { 2 } \geq N - \left( n _ { 1 } - 1 \right) } \end{array}$ . Therefore, we can obtain

$$
\begin{array}{l} E \left[ \binom {\widetilde {M} _ {1} ^ {(n _ {1})}} {\sim} ^ {2} \right] - E \left[ \binom {\widetilde {M} _ {1} ^ {(n _ {1} - 1)}} {\sim} ^ {2} \right] = (2 n _ {1} - 1) \times P \left(\widetilde {D} _ {1} > n _ {1} - 1\right) \\ \quad + 0 \times P \left(\widetilde {D} _ {1} \leq n _ {1} - 1\right) = (2 n _ {1} - 1) [ 1 - F _ {1} (n _ {1} - 1) ] \end{array}\tag{A.6}
$$

$$
\begin{array}{l} E \bigg [ \bigg (\widetilde {M} _ {2} ^ {(n _ {1})} \bigg) ^ {2} \bigg ] - E \bigg [ \bigg (\widetilde {M} _ {2} ^ {(n _ {1} - 1)} \bigg) ^ {2} \bigg ] = [ - 2 (N - n _ {1}) - 1 ] \times P \Big (\underline {{D}} _ {1} > n _ {1} - 1 \text { and } \underline {{D}} _ {2} \geq N - n _ {1} + 1 \Big) \\ \qquad + 0 \times P \Big (\underline {{D}} _ {1} \leq n _ {1} - 1 \text { or } \underline {{D}} _ {2} <   N - n _ {1} + 1 \Big) = - [ 2 (N - n _ {1}) \\ \qquad + 1 ] [ 1 - F _ {1} (n _ {1} - 1) - F _ {2} (N - n _ {1}) + F (n _ {1} - 1, N - n _ {1}) ], \end{array}\tag{A.7}
$$

and

$$
\begin{array}{l} E \bigg [ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \underset {\sim} {M} _ {2} ^ {(n _ {1})} \bigg ] - E \bigg [ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \bigg ] = 0 \times P \Big (\underset {\sim} {D} _ {1} \leq n _ {1} - 1 \Big) + \sum_ {d _ {1} = n _ {1}} ^ {\infty} \sum_ {d _ {2} = 0} ^ {N - n _ {1}} d _ {2} p (d _ {1}, d _ {2}) \\ \qquad + [ n _ {1} (N - n _ {1}) - (n _ {1} - 1) (N - n _ {1} + 1) ] \\ \qquad \times P \Big (\underset {\sim} {D} _ {1} > n _ {1} - 1 \text {   and   } \underset {\sim} {D} _ {2} \geq N - n _ {1} + 1 \Big) \\ \qquad = (N - 2 n _ {1} + 1) [ 1 - F _ {1} (n _ {1} - 1) - F _ {2} (N - n _ {1}) \\ \qquad + F (n _ {1} - 1, N - n _ {1}) ] + \sum_ {d _ {1} = n _ {1}} ^ {\infty} \sum_ {d _ {2} = 0} ^ {N - n _ {1}} d _ {2} p (d _ {1}, d _ {2}). \end{array}\tag{A.8}
$$

Thus, we know

$$
\begin{array}{l} \operatorname{Var} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \right] = \operatorname{Var} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] + \left\{E \left[ \left(\underset {\sim} {M} _ {1} ^ {(n _ {1})}\right) ^ {2} \right] - E \left[ \left(\underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)}\right) ^ {2} \right] \right\} \\ \qquad - \left\{E ^ {2} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \right] - E ^ {2} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] \right\} = \operatorname{Var} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] \\ \qquad + \left\{2 n _ {1} - 1 - E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \right] - E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] \right\} \left[ 1 - F _ {1} (n _ {1} - 1) \right], \end{array}\tag{A.9}
$$

$$
\begin{array}{l} \operatorname{Var} \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] = \operatorname{Var} \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] + \left\{E \left[ \left(\underset {\sim} {M} _ {2} ^ {(n _ {1})}\right) ^ {2} \right] - E \left[ \left(\underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)}\right) ^ {2} \right] \right\} \\ \qquad - \left\{E ^ {2} \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] - E ^ {2} \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] \right\} = \operatorname{Var} \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] \\ \qquad - \left\{2 (N - n _ {1}) + 1 - E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] - E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] \right\} G (n _ {1} - 1, N - n _ {1}), \end{array}\tag{A.10}
$$

and

$$
\begin{array}{l} \operatorname{Cov} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})}, \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] = \operatorname{Cov} \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)}, \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] + \left\{E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] \right. \\ \quad - E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] \Bigg \} - \left\{E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1})} \right] E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] \right. \\ \quad - E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1} - 1)} \right] \Bigg \} = G (n _ {1} - 1, N - n _ {1}) \\ \quad \times \left\{N - 2 n _ {1} + 1 + E \left[ \underset {\sim} {M} _ {1} ^ {(n _ {1} - 1)} \right] \right\} \\ \quad - [ 1 - F _ {1} (n _ {1} - 1) ] E \left[ \underset {\sim} {M} _ {2} ^ {(n _ {1})} \right] \\ + \sum_ {d _ {1} = n _ {1}} ^ {\infty} \sum_ {d _ {2} = 0} ^ {N - n _ {1}} d _ {2} p (d _ {1}, d _ {2}) \cdot \\ (A) \end{array}\tag{A.11}
$$

By substituting Eqs. (A.2), (A.3), (A.9), (A.10) and (A.11) into Eq. (A.5), Eq. (6) is proven.

Next, we derive the initial condition for calculating $V _ { n _ { 1 } } ( M )$ . When $n _ { 1 } = 0 , \ : M _ { 1 } ^ { ( 0 ) } = 0$ and $\underset { ^ { \sim } } { M }  { \stackrel { \left( 0 \right) } { \left( 2 \right) } } = \operatorname* { m i n } \left( D _ { 2 } , N \right)$ . Thus, we have $E \left[ \underset { \sim } { M } _ { 1 } ^ { ( 0 ) } \right] = 0$ $V a r \bigg [ \underline { { { M } } } _ { 1 } ^ { ( 0 ) } \bigg ] = 0 , C o \nu \bigg [ \underline { { { M } } } _ { 1 } ^ { ( 0 ) } , \underline { { { M } } } _ { 2 } ^ { ( 0 ) } \bigg ] = 0 ,$ , and

$$
V _ {0} (\underset {\sim} {M}) = \gamma_ {2} (1 - \gamma_ {2}) E \left[ \underset {\sim} {M} _ {2} ^ {(0)} \right] + (1 - \gamma_ {2}) ^ {2} \operatorname{Var} \left[ \underset {\sim} {M} _ {2} ^ {(0)} \right].\tag{A.12}
$$

Since $\underset { ^ { \prime } } { M } \sb { 2 } ^ { ( 0 ) } = \operatorname* { m i n } \biggl ( D _ { 2 } , N \biggr )$ , we know

$$
\begin{array}{c} E \left[ \left(M _ {2} ^ {(0)}\right) ^ {2} \right] = \sum_ {d _ {2} = 0} ^ {N} d _ {2} ^ {2} p _ {2} (d _ {2}) + \sum_ {d _ {2} = N + 1} ^ {\infty} N ^ {2} p _ {2} (d _ {2}) \\ = N ^ {2} - \sum_ {d _ {2} = 0} ^ {N} \left(N ^ {2} - d _ {2} ^ {2}\right) p _ {2} (d _ {2}) \cdot \end{array}\tag{A.13}
$$

$$
\begin{array}{l} \text { Thus, } V \left[ \underset {\sim} {M} _ {2} ^ {(0)} \right] = E \left[ \left(\underset {\sim} {M} _ {2} ^ {(0)}\right) ^ {2} \right] - E ^ {2} \left[ \underset {\sim} {M} _ {2} ^ {(0)} \right] = N ^ {2} - \sum_ {d _ {2} = 0} ^ {N} \left(N ^ {2} - d _ {2} ^ {2}\right) p _ {2} (d _ {2}) \\ \quad - \left\{N - \sum_ {d _ {2} = 0} ^ {N} (N - d _ {2}) p _ {2} (d _ {2}) \right\} ^ {2} \\ \quad = \sum_ {d _ {2} = 0} ^ {N} (N - d _ {2}) ^ {2} p _ {2} (d _ {2}) - \left[ \sum_ {d _ {2} = 0} ^ {N} (N - d _ {2}) p _ {2} (d _ {2}) \right] ^ {2} \cdot \end{array} \tag {A.14}
$$

Substituting Eqs. (A.4) and (A.14) into $\operatorname { E q . }$ (A.12), we obtain Eq. (7).

Appendix B. Procedure to <sup>fi</sup>nd all Pareto optimal solutions to problem $( \mathbf { P _ { 0 } } )$

Step 1 Input the total number of appointments available, N, the noshow rates $\gamma _ { 1 }$ and $\gamma _ { 2 } ,$ , and the joint probability mass function $p ( d _ { 1 } , d _ { 2 } )$ of $D _ { 1 }$ and $D _ { 2 }$ for $0 \leq d _ { 1 } \leq N$ and $0 \leq d _ { 2 } \leq N .$

<sup>˜ ˜</sup>Step 2 Calculate p (d ), p (d ), F (d ), F (d ), and $F ( d _ { 1 } , d _ { 2 } )$ fo

$$
0 \leq d _ {1} \leq N
$$

$$
0 \leq d _ {2} \leq N.
$$

Step 3 Let i=0. Set $\begin{array} { l } { \displaystyle \Sigma ^ { \boldsymbol { a } _ { 2 } \geq I \boldsymbol { \Psi } . } } \\ { \displaystyle C _ { 1 } ( i ) = 0 , \quad \boldsymbol { C } _ { 2 } ( i ) = \sum _ { d _ { 2 } = 0 } ^ { N } ( N - d _ { 2 } ) p _ { 2 } ( d _ { 2 } ) } \end{array}$ and $C _ { 3 } ( 0 , N - 1 ) = \sum _ { d _ { 2 } = 0 } ^ { N - 1 } d _ { 2 } [ p _ { 2 } ( d _ { 2 } ) - p ( 0 , d _ { 2 } ) ]$ <sup>¼</sup>. Calculate $E _ { i } ( M )$ and V M using Eqs. (5) and (7), respectively.

Step 4 Let i=i+1. Calculate $G ( i - 1 , N - i ) = 1 - F _ { 1 } ( i - 1 )$ $- F _ { 2 } ( N - i ) + F ( i - 1 , \quad N - i ) , \quad C _ { 1 } ( i ) = C _ { 1 } ( i - 1 ) + F _ { 1 } ( i - 1 ) ,$ $C _ { 2 } ( i ) = C _ { 2 } ( i - 1 ) - 1 + G ( i - 1 , ~ N - i ) ,$ and then calculate $E _ { i } ( M )$ and $V _ { i } ( M )$ using Eqs. (4) and (6), respectively.

Step 5 If i=N, go to Step $6 ;$ otherwise, calculate $C _ { 3 } ( i , N - i - 1 ) =$

$$
\begin{array}{l} C _ {3} (i - 1, N - i) - \sum_ {d _ {2} = 0} ^ {N - i - 1} d _ {2} p (i, d _ {2}) \\ - (N - i) \left[ p _ {2} (N - i) - \sum_ {d _ {1} = 0} ^ {i - 1} p (d _ {1}, N - i) \right] \text {   and   go   to   Step   4. } \end{array}
$$

Step 6 Sort $n _ { 1 }$ <sup>¼</sup>in the descending order of $E _ { n _ { 1 } } ( M )$ into $\{ n \} ^ { ( 0 ) } , n \} ^ { ( 1 ) } , \cdots$ $n _ { 1 } ^ { ( N ) } \} , \mathrm { i . e . } E _ { n _ { 1 } ^ { ( 0 ) } } ( { \underline { { M } } } ) { \geq } E _ { n _ { 1 } ^ { ( 1 ) } } ( { \underline { { M } } } ) { \geq } { \cdots } { \geq } E _ { n _ { 1 } ^ { ( N ) } } ( { \underline { { M } } } )$

Step 7 Let the set of the Pareto optimal solutions, S, be empty, i.e. $S = \{ \} .$

Step 8 Let i = 0. Set $S { = } S \cup \{ n _ { 1 } ^ { ( i ) } \}$

Step 9 Let $i = i + 1$ . If $V _ { n _ { 1 } ^ { ( i ) } } ( \underset { \sim } { M } ) { < } V _ { n _ { 1 } ^ { ( j ) } } ( \underset { \sim } { M } )$ for all $n \ L ^ { ( j ) } \in S ,$ then $S { = } S \cup \{ n _ { 1 } ^ { ( i ) } \}$

Step 10 If i=N, stop; otherwise, go to Step 9.

## References

[1] B. Armstrong, O. Levesque, J.B. Perlin, C. Rick, G. Shectman, Reinventing veterans health administration: focus on primary care, Journal of Healthcare Management 50 (2005) 399–408.

[2] A.G. Bean, J. Talaga, Predicting appointment breaking, Journal of Health Care Marketing 15 (1995) 29–34.

[3] J. Bowers, G. Mould, Managing uncertainty in orthopedic trauma theatres, European Journal of Operational Research 154 (2004) 599–608.

[4] D.G. Bundy, G.D. Randolph, M. Murray, J. Anderson, P.A. Margolis, Open access in primary care: results of a North Carolina pilot project, Pediatrics 116 (2005) 82–87.

[5] T. Cayirli, E. Veral, Outpatient scheduling in health care: a review of literature, Production and Operations Management 12 (2003) 519–549.

[6] S. Chopra, W. Lovejoy, C. Yano, Five decades of operations management and the prospects ahead, Management Science 50 (2004) 8–14.

[7] R.W. Day, M.D. Dean, R. Gar<sup>fi</sup>nkel, S. Thompson, Improving patient <sup>fl</sup>ow in a hospital through dynamic allocation of cardiac diagnostic testing time slots, Decision Support Systems 49 (2010) 463–473.

[8] B. Denton, D. Gupta, A sequential bounding approach for optimal appointment scheduling, IIE Transactions 35 (2003) 1003–1016.

[9] B.E. Fries, V.P. Marathe, Determination of optimal variable-sized multiple-block appointment systems, Operations Research 29 (1981) 324–344.

[10] N.B. Gailmard, Short-term strategies to increase patient demand, Optometric Management (2010) www.optometricmanagement.com/mtotw/tip new.asp?tip=445.

[11] A. George, G. Rubin, Non-attendance in general practice: a systematic review and its implications for access to primary health care, Family Practice 20 (2003) 178-184

[12] D.C. Goodman, Twenty-year trends in regional variations in the U.S. physician workforce, Health Affairs - Web Exclusive (2004) VAR90–VAR97.

[13] D.C. Goodman, E.S. Fisher, Physician workforce crisis? Wrong diagnosis, wrong prescription, The New England Journal of Medicine 358 (2008) 1658–1661.

[14] D. Gupta, B. Denton, Appointment scheduling in health care: challenges and opportunities, IIE Transactions 40 (2008) 800–819.

[15] S. Herriott, Reducing delays and waiting times with open-of<sup>fi</sup>ce scheduling, Family Practice Management 6 (1999) 38–43.

[16] B.J. Johnson, J.W. Mold, J.M. Pontious, Reduction and management of no-shows by family medicine residency practice exemplars, Annals of Family Medicine 5 (2007) 534–539.

[17] J.G. Kennedy, J.T. Hsu, Implementation of an open access scheduling system in a residency training program, Family Medicine 35 (2003) 666–670.

[18] K.J. Klassen, T.R. Rohleder, Scheduling outpatient appointments in a dynamic environment, Journal of Operations Management 14 (1996) 83–101.

[19] L.R. LaGanga, S. Lawrence, Clinic overbooking to improve patient access and increase provider productivity, Decision Sciences 38 (2007) 251–276.

[20] M. Lamiri, F. Grimaud, X. Xie, Optimization methods for a stochastic surgery planning problem, International Journal of Production Economics 120 (2009) 400–410.

[21] S. Leader, M. Moon, Medicare trends in ambulatory surgery, Health Affairs, Web Exclusives 8 (1989) 158–170.

[22] V.J. Lee, A. Earnest, M.I. Chen, B. Krishnan, Predictors of failed attendances in a multi-specialty outpatient centre using electronic databases, BMC Health Services Research 5 (2005).51–-58

[23] C.-J. Liao, C.D. Pegden, M. Rosenshine, Planning timely arrivals to a stochastic production or service system, IIE Transactions 25 (1993) 63–73.

[24] L. Liu, X. Liu, Block appointment systems for outpatient clinics with multiple doctors, Journal of the Operational Research Society 49 (1998) 1254–1259.

[25] L. Liu, X. Liu, Dynamic and static job allocation for multi-server systems, IIE Transactions 30 (1998) 845–854.

[26] C. Martin, T. Perfect, G. Mantle, Non-attendance in primary care: the views of patients and practices on its causes, impact, and solutions, Family Practice 22 (2005).638-643

[27] Massachusetts Medical Society, MMS Physician Workforce Study, Massachusetts Medical Society, Waltham, MA, 2007 [2007].

[28] D. McFadden, Economic choices, The American Economic Review 91 (2001) 351–378.

[29] A. Mehrotra, L. Keehl-Markowitz, J.Z. Ayanian, Implementing open-access scheduling of visits in primary care practices: a cautionary tale, Annals of Internal Medicine 148 (2008) 915–922.

[30] M. Murray, C. Tantau, Same-day appointments: exploding the access paradigm Family Practice Management 7 (2000) 45–50.

[31] M. Murray, T. Bodenheimer, D. Rittenhouse, K. Grumbach, Improving timely access to primary care—case studies of the advanced access model, Journal of the American Medical Association 289 (2003) 1042–1046.

[32] M. Murray, M. Davis, B. Boushon, Panel size: how many patients can one doctor manage? Family Practice Management 14 (2007) 44–51.

[33] K. Muthuraman, M. Lawley, A stochastic overbooking model for outpatient clinical scheduling with no-shows, IIE Transactions 40 (2008) 820–837.

[34] C.D. O'Hare, J. Corlett, The outcomes of open-access scheduling, Family Practice Management 11 (2004) 35–38

[35] D.H. Parente, M.B. Pinto, J.C. Barber, A pre-post comparison of service operational ef<sup>fi</sup>ciency and patient satisfaction under open access scheduling, Health Care Management Review 30 (2005) 220–228.

[36] S. Pierdon, T. Charles, K. McKinley, L. Myers, Implementing advanced access in a group practice network, Family Practice Management 11 (2004) 35–38.

[37] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (2007) 1044–1061.

[38] X. Qu, R.L. Rardin, J.A.S. Williams, D.R. Willis, Matching daily healthcare provider capacity to demand in advanced access scheduling systems, European Journal of Operational Research 183 (2007) 812–826.

[39] H.P. Rodriguez, W.H. Rogers, R.E. Marshall, D.G. Safran, The effects of primary care physician visit continuity on patients' experiences with care, Journal of General Internal Medicine 22 (2007) 787–793.

[40] J.E. Rohrer, M. Bernard, J. Naessens, J. Furst, K. Kircher, S. Adamson, Impact of open-access scheduling on realized access, Health Service Management Research 20 (2007) 134–139.

[41] J.W. Saultz, J. Lochner, Interpersonal continuity of care and care outcomes: a critical review, Annals of Family Medicine 3 (2005) 159–166.

[42] S.M. Schappert, E.A. Rechtsteiner, Ambulatory medical care utilization estimates for 2006, National Health Statistics Reports, National Center for Health Statistics, 2008.

[43] W. Shonick, B.W. Klein, An approach to reducing the adverse effects of broken appointments in primary care systems, Medical Care 15 (1977) 419–429.

[44] L.I. Solberg, M.C. Hroscikoski, J.M. Sperl-Hillen, P.J. O'Connor, B.F. Crabtree, Key issues in transforming health care organizations for quality: the case of advanced access, Joint Commission Journal on Quality and Safety 30 (2004) 15–24.

[45] K.E. Train, Discrete Choice Methods with Simulation, Cambridge University Press, Cambridge, UK, 2003

[46] W.M. Valenti, J. Bookhardt-Murray, Advanced-access scheduling increases quality, productivity, and revenue, The AIDS Reader 14 (2004) 220–224.

[47] J. Vissers, Selecting a suitable appointment system in an outpatient setting, Med ical Care 17 (1979) 1207–1220.

[48] E.W. Woodcock, Managing your appointment 'no-shows', The Journal of Medical Practice Management 15 (2000) 284–288.

Xiuli Qu is an assistant professor in the Department of Industrial and Systems Engi neering at North Carolina Agricultural and Technical State University. Dr Qu received her PhD in industrial engineering from Purdue University. Before that, she received a BSEE and MSEE from the University of Science and Technology Beijing. Her research and teaching interests focus on health care engineering, sustainable systems, and stochastic modeling and optimization.

Ronald L. Rardin is the John and Mary Lib White Systems Integration Chair and a Distinguished Professor of Industrial Engineering at the University of Arkansas—Fayetteville. He is also the head of the University's Center on Innovation in Healthcare Logistics. Professor Rardin retired as Professor Emeritus of Industrial Engineering at Purdue University after directing the Purdue Energy Modeling Research Groups and playing a leading role in its Regenstrief Center for Healthcare Engineering. He also served a rotation from 2000 to 2003 as Program Director for Operations Research and Service Enterprise Engineering at the National Science Foundation including founding the program to foster research in service industries, especially healthcare. Dr. Rardin obtained his B.A. and M.P.A. degrees from the University of Kansas, and after working in city government, consulting and distribution for <sup>fi</sup>ve years, a Ph.D. at Georgia Institute of Technology. His current teaching and research interests center on large-scale optimization modeling and algorithms, especially their applications in healthcare delivery. He is an award winning teacher of those topics, and co-author of numerous research papers and two comprehensive textbooks: a graduate text Discrete Optimization, published in 1988, and a comprehensive undergraduate textbook Optimization in Operations Research in 1998. He has been selected as a fellow of the Institute for Operations Research and the Management Sciences

Julie Ann Stuart Williams is an associate professor in the Dept. of Management and MIS at the University of West Florida. Professor Williams received her PhD in industrial and systems engineering from Georgia Institute of Technology. Before moving to UWF, she was a faculty member at Purdue University and The Ohio State University. She is a registered professional engineer in the state of Ohio. Her research and teaching interests focus on sustainable operations and health care systems.
