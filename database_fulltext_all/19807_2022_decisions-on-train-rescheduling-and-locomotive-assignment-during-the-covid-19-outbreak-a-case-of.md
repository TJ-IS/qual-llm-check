---
otero_id: 19807
otero_key: "2EHA7A9M"
title: "Decisions on train rescheduling and locomotive assignment during the COVID-19 outbreak: A case of the Beijing-Tianjin intercity railway"
authors: "Liujiang Kang; Yue Xiao; Huijun Sun; Jianjun Wu; Sida Luo; Nsabimana Buhigiro"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113600"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decisions on train rescheduling and locomotive assignment during the COVID-19 outbreak: A case of the Beijing-Tianjin intercity railway

Liujiang Kang <sup>a</sup>, Yue Xiao <sup>a</sup>, Huijun Sun <sup>a,\*</sup>, Jianjun Wu <sup>b</sup>, Sida Luo <sup>a,\*</sup>, Nsabimana Buhigiro <sup>a</sup>

<sup>a</sup> Key Laboratory of Transport Industry of Big Data Application Technologies for Comprehensive Transport, Ministry of Transport, Beijing Jiaotong University, 100044, China

<sup>b</sup> State Key Laboratory of Rail Traffic Control and Safety, Beijing Jiaotong University, 100044, China

## A R T I C L E I N F O

Keywords: Train rescheduling Locomotive assignment Operation line COVID-19

## A B S T R A C T

Travel restriction measures have been widely implemented to curb the continued spread of COVID-19 during the Chinese Lunar New Year celebrations. Many operation lines and train schedules of China’s railway were either heavily adjusted or canceled. In this study, a mixed-integer linear programming model and a two-step solution algorithm were developed to handle such large-scale adjustments. The formulation considers a flexible time window for each operation line and locomotive traction operations, and minimizes the number of locomotives utilized with their total idle time for train rescheduling and locomotive assignment, respectively. The solution algorithm determines the minimum locomotive fleet size based on the optimal train rescheduling results; it then reduces the traction idle time of locomotives. In response to the uncertainty of COVID-19, two tailored ap proaches were also designed to recover and remove operation lines, which can insert and cut operation lines based on the results of locomotive assignment. Finally, we conducted a case study of the Beijing-Tianjin intercity railway from the start of the COVID-19 outbreak to the recovery of operations.

## 1. Introduction

In December 2019, a novel coronavirus (COVID-19) was detected in the city of Wuhan, China, and spread rapidly throughout China in the run-up to Chinese Lunar New Year’s Eve [1]. COVID-19 is characterized by an extremely high risk of transmission with adverse impacts on public transportation, health, economy, society and politics. China Railways have adjusted their overall operational plans to suit the new trends brought about by pandemic prevention and control. An emphasis was also placed on the 2020 ChunYun period, characterized by an extremely high volume of passenger demand (a mass migration reaching up to three billion trips), which requires an efficient transport organization following the so-called “one day, one diagram.” However, with the continued and rapid spread of COVID-19, nationwide travel restriction measures have been strictly implemented. As a result, many operation lines (an operation line is defined as a completed train operating process on a railway line) and train schedules were either heavily adjusted or canceled.

This operational disruption dictates a train rescheduling with the aim of flexibly adjusting schedules for a set of trains under several opera tional requirements. When performing train rescheduling, locomotive assignments should be adjusted based on the new schedules. The rational use of locomotives maximizes the benefits of locomotive oper ation, saving maintenance costs, various labor and management costs. In view of the relationship between train rescheduling and locomotive assignment, this study proposes an integrated solution for train rescheduling and locomotive assignment (TRLA) under the COVID-19 outbreak. On the other hand, travel demand changes with the outbreak of the pandemic; thus, this study proposes an approach tailored for recovering and/or cutting operation lines based on the TRLA prob lem. The logic of the TRLA demonstrated in Fig. 1 is explained in detail as follows.

Given a set of operation lines for a railway corridor, train schedules can be rescheduled to meet significant passenger flow fluctuations due to COVID-19. Train rescheduling further breeds the optimization of locomotive assignment problem, with the aim of reducing locomotive fleet size and improving operational efficiency (Algorithm 1). Based on the optimal results of locomotive utilization, additional operation lines can be inserted and/or recovered after effective epidemic control (Al gorithm 2). In addition, some operation lines may hang up if COVID-19 continues to spread (Algorithm 3). Then, the loop will be closed by returning to the starting point of the TRLA after checking the balance between transport capacity and traffic demand. The railway passenger transport has been hit hard by the pandemic, resulting in a drastic reduction in demand. For instance, in China, demand fell below 55.1% in early March to April 2020, according to statistics from the National Railway Administration. This significant reduction in passenger demand could lead to underutilization of resources (a huge loss for the railway operator) if operational plans are not adjusted to meet actual demand. By addressing the above TRLA problems, travel demand would be basically met and underutilization of resources would be avoided. Hence, railway agencies can use a minimum number of locomotives to accomplish their transportation tasks.

In the following, some recent and related studies on TRLA are reviewed. Section 3 presents the problem statement, and then Section 4 establishes the TRLA model formulations with the objective of mini mizing the locomotive fleet size and total traction idle time. Section 5 discusses the proposed two-step solution algorithm for the developed model. Section 6 reports a case study of the Beijing-Tianjin intercity railway. Finally, Section 7 concludes the study and proposes some future work.

## 2. Literature review

Disruptions such as rolling stock breakdowns, signal failures and unexpected events usually cause delays for certain trains in the railway network [2]. Besides, delay propagation will occur if the initial train delays are not properly addressed, which can lead to severe consecutive delays. To achieve a high degree of punctuality in the traffic system, real-time rescheduling is essential in practice [3]. For example, many studies aim to minimize the consecutive delays caused by disruptions [4]. For small and medium-sized disruptions, they can be eliminated by simply adjusting the train schedule. For large disruptions, adjustments to train schedules, rolling stock circulation plans and crew assignment plans are usually required [5]. To eliminate the impacts of disruptions, studies usually formulate exact mixed-integer linear programming (MILP) train rescheduling models, which can provide optimal solutions by reducing the difference between the upper and lower bounds of an objective function [6]. However, train rescheduling usually requires a high standard of computational efficiency for real-time operations [7]. Thus, the approaches used to solve train rescheduling models considered more efficient than most train scheduling models. For this reason, several studies have designed heuristics, such as the genetic algorithm and the deep neural network algorithm, to solve real-time and large scale timetable rescheduling problems [8,9]. The compromise between accuracy and efficiency is a combination of MILP and heuristics. In other words, a typical example of such a practice is the integration of heu ristics and powerful solvers. Specifically, Fischetti [10] used an ad-hoc heuristic preprocessing on top of CPLEX (a commercial optimization solver developed by IBM) for the standard event-based train resched uling MILP model. The results indicated that the approach can obtain almost optimal solutions within a very short period of time. With the development of machine learning techniques, reinforcement learning approaches have been used in train rescheduling. For instance, Semrov<sup>ˇ</sup> et al. [11] developed a Q-learning approach to reschedule trains in the event of disruptions. The key advantage of Q-learning over the MILP methods is its adaptability to different railway disruptions, scenarios, problem scales, etc.

Several studies have argued that the aim of train rescheduling is to reduce passenger inconvenience when published schedules incur traffic disruptions [12,13]. This is because the loss of passenger time and satisfaction will be implicitly and irrevocably considered [14]. Howev er, convenience-oriented rescheduling is often achieved at the cost of consecutive train delays [15]. For example, some trains must stay longer at stations to wait for passengers and maintain connections, while others must be canceled considering the line passing-through capacity. Hence, there is a trade-off between convenience-oriented rescheduling and delay-elimination-oriented rescheduling. For more studies on train rescheduling models and algorithms, we refer interested readers to Cacchiani et al. [16].

![](/api/attachments/2EHA7A9M/fulltext/images/4c3f316e0b5e0e6b03d0225e0988ae33173d2dfe274877b9a9a54e509f48bbde.jpg)  
Fig. 1. Flowchart of solving the TRLA problem.

Various rolling stock scheduling problems have been investigated [17–21]. The aforementioned studies used flow-based approaches in which the order of locomotives/vehicles within the composition was not taken into account. Haahr et al. [22] compared two exact approaches (using CPLEX and column generation) for railway rolling stock rescheduling during the real-time operation phase. The same optimal results obtained show that both methods are efficient enough to be used in real applications.

Recently, some studies have combined the locomotive planning problem with the train scheduling problem. For example, Wang et al. [23] studied the integration problem of train scheduling and vehicle circulation planning by developing a MILP model, which minimized headway deviations between train schedules and service patterns. The model has been applied to a real case and solved by CPLEX in an acceptable computational time. Note that their proposed MILP was a multi-objective problem that could be addressed by using a linear weighting method. In this case, there is no guarantee that the weights accurately represent the importance of the sub-objectives, especially in real applications. Canca and Barrena [24] investigated the integrated rolling stock circulation and depot location problem. The integration problem was solved by a sequential approach, which first determined the minimum number of vehicles and then optimized their circulation and depot locations. In the second phase, the vehicle circulation and depot location problems were formulated as a MILP model and solved by a genetic algorithm. Cadarso and Marín [25] aimed to improve the ca pacity of the rapid transit network by adjusting train schedules and rolling stock assignments. A natural extension is the recoverability of the network in case of disruptions by modifying schedules and assignments. Godwin et al. [26] developed a simulation-based approach to calculate the maximum fleet size of locomotives on a rail network. The results showed that with an increase in locomotive fleet size. the network throughput would increase. The network will become congested when more than needed locomotives enter the railway network.

Michaelis and Schobel ¨ [27] pointed out that the traditional planning process for public transportation had an obvious drawback. If companies first design lines, then calculate schedules, and finally plan vehicle (crew) schedules, the number of vehicles (the fleet size problem) required is usually overestimated. Thus, this study integrates the second and third steps mentioned above. In this way, the fleet size is flexible during the entire planning process and the objectives can be customeroriented. In contrast to previous studies, this paper proposes a global optimization approach by which the minimum locomotive fleet size can be obtained by solving the integrated exact TRLA model without using a linear weighted method. This paper presents a tailored algorithm for recovering operations from the COVID-19 outbreak by inserting opera tion lines based on the results of locomotive assignment. Therefore, in this paper, the train rescheduling problem and the locomotive assign ment problem are mutually influential and complementary natural.

## 3. Problem statement

For illustration purposes, an intercity railway line with several sta tions connecting two cities, one of which is represented by a locomotive depot at the start/end of the railway line, is considered (see Fig. 2). There are three up-train operation lines and three down-train operation lines between depot A and depot B. The start time (solid circles) and end time (solid squares) of each operation line can be optimized by adjusting the train operations between depot A and depot B.

On a typical day, a certain number of trains run from one depot to another, and these trains pass through several railway stations according to a schedule. Due to the different passenger volumes at different periods of time, trains are usually dispatched on a non-periodic basis. For example, prior to the COVID-19 outbreak, more than 50 pairs of trains were operating on the Beijing-Tianjin intercity railway with a headway of approximately 10 min, but only 12 pairs of trains remained during the period of the COVID-19 outbreak. For these 12 pairs of operation lines, they were mainly operated during the peak hours.

First, we considered robust train schedules in this study. That is, in addition to the given train schedule, it is possible to insert or reduce some extra running time or dwell time in the original schedule with flexible start and end times of the operation lines (yellow circles and yellow squares). This makes the train rescheduling problem more complex considering robust strategies.

Second, each operation line is served by at least one locomotive by hauling trains from one station to another according to a schedule. This is the locomotives’ traction operation, which is further distinguished by the up-train traction operation and the down-train traction operation. Considering both the up-train service and the down-train service, we define a locomotive's traction operation as a round trip of the locomo: tive to and from the same depot. When a locomotive completes an uptrain traction operation, it will wait for a down-train traction opera tion at the corresponding depot, and vice versa. In this process, we will consider a fixed technical operation time for each locomotive at the same depot, including the time of reformation and preparation, when preparing for up-train or down-train traction operations. In addition to this technical operation time, the time that a locomotive waits to pro vide traction at the depot is defined as the traction idle time. Moreover, each locomotive has a traction weight that specifies the maximum tractive power that can be utilized during a specific traction operation. At the same time, this traction weight cannot be less than or equal to the weight of the train. Otherwise, locomotives will not have enough power to complete the traction task. Note that the above processes are per formed over a certain period, which can often be in the range of one day to one month, depending on the scale of the problem set.

![](/api/attachments/2EHA7A9M/fulltext/images/abe1934e1ac02c35a8f3179a2dc1a473976fd09da37a7cea456fbbae3e57f13c.jpg)  
Fig. 2. Illustration of the TRLA problem.

Third, when COVID-19 becomes effectively controlled, operation lines will be gradually recovered to meet increasing travel demand; otherwise, more operation lines may be canceled. In this case, intercity railway managers must decide which operation lines in the up-train and down-train directions should be recovered or reduced in a reasonable order. The above-mentioned train rescheduling and locomotive assign ment problems become more complex and difficult to solve as the number of operation lines increases. In summary, the real-world opti mization problem under the COVID-19 framework can be defined as follows:

• How can the timetables of the remaining pairs of trains during the COVID-19 outbreak be optimally rescheduled based on the published timetables, taking into account the flexible time windows for each operation line and locomotive traction operations?

• How can locomotives be optimally assigned to operation lines, taking into account the traction power and train weight, and how can the total amount of idle time of locomotives utilized for all traction op erations be minimized?

• How can problem-specific knowledge be used to jointly solve the train rescheduling problem and locomotive assignment problem?

• Once the government has effectively contained the COVID-19 pandemic, how can canceled operation lines be recovered, and how can some operation lines be cut back as propagation continues?

## 4. Model

## 4.1. Notations

I: the set of operation lines, which are in the up-train direction, $I =$ $\{ 1 , 2 , . . . , i , . . . , m \}$

J: the set of operation lines, which are in the down-train direction, J $= \{ 1 , 2 , . . . , j , . . . , n \}$

K: the set of locomotives, $K = \{ 1 , 2 , . . . , k , . . . , p \}$

pt<sup>s</sup>: the published start time of the up-train operation line i. The same meaning applies to the down-train operation line j when the subscript changes.

$t _ { i } ^ { s . m i n }$ : the earliest start time of the up-train operation line i. The same meaning applies to the down-train operation line j when the subscript changes.

$t _ { i } ^ { s . m a x } ;$ : the latest start time of the up-train operation line i. The same meaning applies to the down-train operation line j when the subscript changes.

pt<sup>e</sup>: the published end time of the up-train operation line i. The same meaning applies to the down-train operation line j when the subscript changes.

$t _ { i } ^ { e . m i n . }$ : the earliest end time of the up-train operation line i. The same meaning applies to the down-train operation line j when the subscript changes.

$t _ { i } ^ { e m a x } ;$ : the latest end time of the up-train operation line i. The same meaning applies to the down-train operation line j when the subscript changes.

$\beta _ { i j } ^ { k } \mathrm { : }$ binary parameter, $\beta _ { i j } ^ { k } = 1$ if time is past 0:00 when the locomotive k undertakes the down-train operation line j right after the up-train operation line i without any other operation lines in between. Other wise, $\beta _ { i j } ^ { k } = 0 .$ . Similarly, $\beta _ { j i } ^ { k }$ holds the same meaning.

$\theta _ { i } \colon$ the technical operation time of locomotives at depots when pre paring for the up-train operation line i. Similarly, θ has the same meaning for the down-train operation line j.

h : the required headway time between operation line i and operation line i + 1. As for $h _ { j } ,$ it has the same meaning.

τ : the average operating time of operation lines in the up-train di rection. τ is the average operating time of operation lines in the down train direction.

ω : the train weight running on the up-train operation line i. Simi larly, ω is the train weight running on the down-train operation line j.

φ : the traction weight of the locomotive k.

π: the maximum number of traction tasks assigned to each locomo tive in daily operations.

$x _ { i j } ^ { k } \mathrm { : }$ decision binary variable, $x _ { i j } ^ { k } = 1$ if the locomotive k is assigned to the down-train operation line j right after completing traction of the uptrain operation line i. Otherwise, $x _ { i j } ^ { k } = 0$ . Similarly, $x _ { j i } ^ { k }$ has the same meaning.

t<sup>s</sup>: decision variable, the start time of the up-train operation line i. Similarly, we have the same definition for $t _ { j } ^ { s } .$

t<sub>i</sub><sup>e</sup>: decision variable, the end time of the up-train operation line i. Similarly, we have the same definition for $t _ { j } ^ { e } .$

d : decision variable, the time interval between the up-train opera tion line i and the down-train operation line j, which is equal to the start time of operation line j minus the end time of operation line i. Similarly, $d _ { j i }$ has the same calculation rule.

## 4.2. MILP model

When rescheduling train timetables and reassigning locomotives to these trains in response to a large number of canceled trains (e.g., during the COVID-19 outbreak), two important aspects should be considered. First, the fleet size of the locomotives will be considered; the smaller the fleet size being utilized, the lower the operating costs will be. As shown in Fig. 3(a), there are five operation lines that provide train services. If each operation line is assigned a different locomotive, then depot B and depot A should reserve three locomotives and two locomotives, respectively. However, if we link the different operation lines into a chain, then one locomotive can serve several consecutive operation lines. For example, operation lines i, j, and i + 2 consist of an operation chain that is assigned to one locomotive, and operation lines i + 1 and j + 1 consist of another operation chain that is assigned to another locomotive. In this case, locomotive depot B requires only two loco motives in total.

Secondly, transport companies make every effort to improve loco motive efficiency, i.e., they try to shorten the traction idle time of locomotives in depots. The shorter the traction idle time of each locomotive, the more efficient the utilization of locomotives. As shown in Fig. 3(b), there are four assignment scenarios when a locomotive completes traction on an operation line $i \colon i \to i + 1 , i \to i + 2 , i \to j ,$ , and i $ j +$ 1. The first two scenarios are inefficient because the locomotive must return to depot B after completing operation line i. This will generate vacant routes, which should be avoided whenever possible. As for operation chains i → j and $i \to j + 1$ , they have different idle times that depend on the start and end times of the operation lines.

![](/api/attachments/2EHA7A9M/fulltext/images/e38f222229baa4218dc7f7b42811cf4c75e9c28d5f6de76f709f2dab91e00e56.jpg)  
Fig. 3. Determination of locomotive fleet size and traction idle time.

Locomotive fleet size: The objective (1) minimizes the number of locomotives that stop at depots at 0:00. To calculate the minimum locomotive fleet size, we add only the number of operation lines crossing 0:00 to the calculated objective values.

$$
\text { Min } \sum_ {k} \sum_ {i} \sum_ {j} \left(\beta_ {i j} ^ {k} \cdot x _ {i j} ^ {k} + \beta_ {j i} ^ {k} \cdot x _ {j i} ^ {k}\right)\tag{1}
$$

Traction idle time: The objective (2) minimizes the traction idle time of each locomotive when conducting the traction of operation line j/i as soon as the traction of operation line i/j is completed. The traction idle time, which is captured by $( d _ { i j } \mathrm { ~ - ~ } \theta _ { j } )$ or $( d _ { j i } \mathrm { ~ - ~ } \theta _ { i } )$ , is the time that a locomotive waits for the next traction operation at the depot.

$$
\text { Min } \sum_ {k} \sum_ {i} \sum_ {j} \left[ \left(d _ {i j} - \theta_ {j}\right) \cdot x _ {i j} ^ {k} + \left(d _ {j i} - \theta_ {i}\right) \cdot x _ {j i} ^ {k} \right]\tag{2}
$$

The time interval $d _ { i j }$ is determined by the start time of the down-train operation line j and the end time of the up-train operation line i, as shown in Eq. (3). Similarly, Eq. (4) shows the opposite situation $d _ { j i } , \mathbf { i . e . , }$ the difference between the start time of the up-train operation line i and the end time of the down-train operation line j. Note that the traction idle time is non-negative, so the time intervals $d _ { i j }$ and $d _ { j i }$ should be no less than the required technical operation times of locomotives $\theta _ { j }$ and $\theta _ { i }$ at the corresponding depots, respectively, as shown in Eqs. (5) and (6). For example, in the case where locomotive k undertakes the down-train operation line j immediately after the up-train operation line i without any other operation lines in between, a time period of 1440 min will be added to the term $d _ { i j }$ $\theta _ { j }$ if the time goes beyond 0:00.

$$
d _ {i j} = t _ {j} ^ {s} - t _ {i} ^ {e}, \forall i \in I, \forall j \in J\tag{3}
$$

$$
d _ {j i} = t _ {i} ^ {s} - t _ {j} ^ {e}, \forall i \in I, \forall j \in J\tag{4}
$$

$$
d _ {i j} - \theta_ {j} + 1 4 4 0 ^ {*} \beta_ {i j} ^ {k} \geq 0, \forall i \in I\tag{5}
$$

$$
d _ {j i} - \theta_ {i} + 1 4 4 0 ^ {*} \beta_ {j i} ^ {k} \geq 0, \forall j \in J\tag{6}
$$

Equation (7) indicates that there is one and only one down-train operation line j assigned to locomotive k when it has just completed the up-train operation line i. Conversely, Eq. (8) shows that there is one and only one up-train operation line i assigned to locomotive k when it has just completed the down-train operation line j. These two constraints set limits on the post-order traction.

$$
\sum_ {k} \sum_ {i} x _ {i j} ^ {k} = 1, \forall \mathrm{j} \in J\tag{7}
$$

$$
\sum_ {k} \sum_ {j} x _ {j i} ^ {k} = 1, \forall i \in I\tag{8}
$$

Unlike the above two constraints, Eqs. (9) and (10) relate to preorder tractions. Specifically, Eq. (9) suggests that for each locomotive $k ,$ there exists one and only one pre-order and up-train operation line i that is prior to the down-train operation line j<sup>′</sup>. Similarly, Eq. (10) rep resents that for each locomotive k, there is one and only one pre-order and down-train operation line j that is prior to the up-train operation line i<sup>′</sup>.

$$
\sum_ {k} \sum_ {j ^ {\prime}} x _ {i j ^ {\prime}} ^ {k} = 1, \forall i \in I\tag{9}
$$

$$
\sum_ {k} \sum_ {i ^ {\prime}} x _ {j i ^ {\prime}} ^ {k} = 1, \forall j \in J\tag{10}
$$

By combining, for instance, Eqs. (7) with (10) and changing the right term to two, we can find that each down-train operation line j will be assigned to two locomotives. In other words, the down-train operation line j is equipped with two locomotives: in practice, one pushes the train, while the other pulls it. Similarly, we simply modify the right term of Eqs. (8) and (9) when performing the traction of operation line i. The constraints in Eqs. (7)–(10) make the model more flexible and easy to modify when dealing with train organization problems.

Moreover, sufficient maintenance time should be reserved for each locomotive in operation. Thus, Eq. (11) ensures that each locomotive will have a limited number of traction tasks, which is less than or equal to $\pi .$ The value of π is given and is determined by the number of loco motives in reserve, as well as the number of planned operation lines.

$$
\sum_ {i} \sum_ {j} \left(x _ {i j} ^ {k} + x _ {j i} ^ {k}\right) - \pi \leq 0, \forall k \in K\tag{11}
$$

In daily operations, train schedules have some timing requirements, and these schedules define the arrival and departure times of each train at each station. However, proper disturbance and adjustments are allowed when scheduling the operation lines. Eqs. (12)–(15) set limi tations on the start time and end time of operation lines.

$$
t _ {i} ^ {s - m i n} \leq t _ {i} ^ {s} \leq t _ {i} ^ {s - m a x}, \forall i \in I\tag{12}
$$

$$
t _ {i} ^ {e - m i n} \leq t _ {i} ^ {e} \leq t _ {i} ^ {e - m a x}, \forall i \in I\tag{13}
$$

$$
t _ {j} ^ {s - m i n} \leq t _ {j} ^ {s} \leq t _ {j} ^ {s - m a x}, \forall j \in J
$$

$$
t _ {j} ^ {e - m i n} \leq t _ {j} ^ {e} \leq t _ {j} ^ {e - m a x}, \forall j \in J\tag{14}
$$

(15)

Besides, for any two consecutive trains, their operation lines cannot cross on rail segments. That is, trains cannot overtake on rail segments. At the same time, there is a time headway between two consecutive train services. This also prevents train from colliding and ensures operational safety. Hence, the following four train schedule constraints should be met.

$$
t _ {i + 1} ^ {s} - t _ {i} ^ {s} \geq h _ {i}, \forall i \in I / m
$$

$$
t _ {i + 1} ^ {e} - t _ {i} ^ {e} \geq h _ {i}, \forall i \in I / m\tag{16}
$$

(17)

$$
t _ {j + 1} ^ {s} - t _ {j} ^ {s} \geq h _ {j}, \forall j \in I / n\tag{18}
$$

$$
t _ {j + 1} ^ {e} - t _ {j} ^ {e} \geq h _ {j}, \forall j \in I / n\tag{19}
$$

Each locomotive has a unique rated traction weight. It cannot be assigned to those operation lines whose weight is greater than the rated traction weight. In Eq. (20), the rated traction weight of locomotive k should be no less than the weight of the down-train operation line j when k finishes the traction of the up-train operation line i and prepares for the next traction of j. Eq. (21) indicates an opposite situation. That is, when the locomotive k completes the traction of the down-train operation line j and assigns it to the up-train operation line i, its rated traction weight should be no less than the weight of i.

$$
\sum_ {k} \sum_ {i} \left(\varphi_ {k} \cdot x _ {i j} ^ {k}\right) - \omega_ {j} \geq 0, \forall j \in J\tag{20}
$$

$$
\sum_ {k} \sum_ {i} \left(\varphi_ {k} \cdot x _ {j i} ^ {k}\right) - \omega_ {j} \geq 0, \forall j \in J\tag{21}
$$

Finally, Eqs. (22) and (23) define the domains of the decision variables.

$$
x _ {i j} ^ {k}, x _ {j i} ^ {k} \in \{0, 1 \}, \forall i \in I, \forall j \in J\tag{22}
$$

$$
t _ {i} ^ {s}, t _ {j} ^ {s}, t _ {i} ^ {e}, t _ {j} ^ {e} \geq 0, \forall i \in I, \forall j \in J\tag{23}
$$

In summary, the integrated TRLA problem can be constructed like the following model. Note that f(∙) is an implicit function that integrates objectives (1) and (2), which can be considered using solution ap proaches such as multi-objective optimization and Lagrangian relaxa tion methods.

<table><tr><td colspan="2">Model-1: MINLP of the multi-objective TRLA problem</td></tr><tr><td>Objective:</td><td>f(·) which contains objectives (1) and (2)</td></tr><tr><td>Subject to:</td><td>Constraints (3)-(23)</td></tr></table>

It should be noted that there are nonlinear terms in the objective (2), i $\begin{array} { r } { . } { \mathrm { e } . , ( d _ { i j } \underbrace { - \theta _ { j } } ) \cdot x _ { i j } ^ { k } + ( d _ { j i } - \theta _ { i } ) \cdot x _ { j i } ^ { k } = ( t _ { j } ^ { s } - t _ { i } ^ { e } - \theta _ { j } ) \cdot x _ { i j } ^ { k } + ( t _ { i } ^ { s } - t _ { j } ^ { e } } \end{array}$ $- \theta _ { i } ) \cdot x _ { j i } ^ { k } .$ . In this case, we show how to linearize the term $( t _ { j } ^ { s } - \dot { t _ { i } ^ { e } } ) \cdot x _ { i j } ^ { k } +$ $( t _ { i } ^ { s } - t _ { j } ^ { e } ) \cdot x _ { j i } ^ { k }$ . Herein, only the term $( t _ { j } ^ { s } - t _ { i } ^ { e } ) \cdot x _ { i j } ^ { k }$ is taken as an example. As for $( t _ { i } ^ { \bar { s } } - t _ { j } ^ { e } ) \cdot x _ { j i } ^ { k } ,$ it is the same. First, let us introduce an auxiliary and non-negative variable $y _ { i j } ^ { k } ,$ which is equal to 0 $\mathrm { i f } \ x _ { i j } ^ { k } = 0 .$ . Conversely, $y _ { i j } ^ { k }$ is equal to $( t _ { j } ^ { s } - t _ { i } ^ { e } ) \mathrm { i f } x _ { i j } ^ { k } = \overline { { 1 } }$ . In other words, $y _ { i j } ^ { k } = ( t _ { i } ^ { s } - t _ { j } ^ { e } ) \cdot x _ { j i } ^ { k } ;$ combining the above two situations, the auxiliary constraints in Eqs. (24)–(27) can be added to linearize the nonlinear terms of Eq. (2) as follows.

$$
y _ {i j} ^ {k} \leq M \cdot x _ {i j} ^ {k}, \forall i \in I, \forall j \in J, \forall k \in K\tag{24}
$$

$$
y _ {i j} ^ {k} - \left(t _ {j} ^ {s} - t _ {i} ^ {e}\right) \leq \left(1 - x _ {i j} ^ {k}\right) \cdot M, \forall i \in I, \forall j \in J, \forall k \in K\tag{25}
$$

$$
y _ {i j} ^ {k} - \left(t _ {j} ^ {s} - t _ {i} ^ {e}\right) \geq \left(x _ {i j} ^ {k} - 1\right) \cdot M, \forall i \in I, \forall j \in J, \forall k \in K\tag{26}
$$

$$
y _ {i j} ^ {k} \geq 0, \forall i \in I, \forall j \in J, \forall k \in K\tag{27}
$$

Therefore, objective (2) is reformulated by Eq. (28).

$$
\operatorname{Min} \sum_ {k} \sum_ {i} \sum_ {j} \left(y _ {i j} ^ {k} + y _ {j i} ^ {k} - \theta_ {j} \cdot x _ {i j} ^ {k} - \theta_ {i} \cdot x _ {j i} ^ {k}\right)\tag{28}
$$

So far, the MILP model used to integrate the TRLA problem can be specified as follows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Model-2: MILP of the multi-objective TRLA problem
Objective:  $f(\cdot)$  which contains objectives (1) and (28)
Subject to: Constraints (3)–(27)
</div>

## 5. Solution approach

## 5.1. Two-step sequential algorithm

To solve Model-2, one may first consider using a multi-objective programming method to integrate objectives (1) and (28). However, it is difficult to determine the weights of locomotive fleet size and traction idle time. As for the Lagrangian relaxation method, the main problem is the computational efficiency, which is more serious when solving large scale examples. Instead of adding some constraints to the objective function, this study developed a two-step sequential algorithm to deal with the integrated TRLA problem. The general idea is that we first compute the minimum locomotive fleet size using Model-3 and then optimize the traction idle times for these locomotives.

```txt
Model-3: MILP of locomotive assignment
Objective: Eq. (1)
Subject to: Constraints (7)–(11), (22)
```

After solving Model-3, we obtain the minimum locomotive fleet size, denoted as min(Model – 3). The found optimization results are then used as a benchmark to propose a fleet size constraint, as shown in Eq. (29), where $\epsilon ( I , J )$ represents the number of operation lines that cross 0:00.

This fleet size constraint will be added to MILP-4 of the integrated TRLA problem. In this way, the problem is solved with the minimum total traction idle time of the locomotives at the minimum fleet size.

$$
\sum_ {k} \sum_ {i} \sum_ {j} \left(\beta_ {i j} ^ {k} \cdot x _ {i j} ^ {k} + \beta_ {j i} ^ {k} \cdot x _ {j i} ^ {k}\right) \leq \min (M o d e l 3) + \epsilon (I, J)\tag{29}
$$

<table><tr><td colspan="2">Model-4: MILP of the integrated TRLA problem</td></tr><tr><td>Objective:</td><td>Eq. (28)</td></tr><tr><td>Subject to:</td><td>Constraints (3)-(27), (29)</td></tr></table>

Note that the two-step sequential Algorithm 1 can practically and optimally solve the integrated TRLA problem. When the locomotive fleet size is not limited, the obtained solution may be unreasonable or un feasible. Moreover, the purchase, use, maintenance and repair of loco motives are expensive. Using a minimum number of locomotives while meeting transportation demands maximizes savings in maintenance costs, as well as various labor and management costs.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Two-step sequential algorithm
1: Solve the MILP Model-3 and obtain the objective value min(Model - 3);
2: Check whether there are day-span operation lines $\epsilon(I, J)$;
3: If yes, the minimum locomotive fleet size is min(Model 3) + $\epsilon(I, J)$;
4: Otherwise, the minimum locomotive fleet size is min(Model 3);
5: Solve the MILP Model-4;
6: Obtain the train timetable and locomotive assignment plan.
</div>

## 5.2. Recovery and cutting of operation lines

Operation lines will be gradually recovered once the government effectively controls the spread of the pandemic. We propose the following tailored approach to recover the operation lines based on the number of operation lines inserted and the results obtained by Algo rithm 1. Let m<sup>′</sup> be the number of operation lines inserted in the up-train direction and n<sup>′</sup> be the number of operation lines inserted in the downtrain direction.

With the obtained values of $t _ { i ^ { \prime } } ^ { e m i n } , \ t _ { i ^ { \prime } } ^ { e m a x } , \ t _ { i ^ { \prime } } ^ { s m i n } , \ t _ { i ^ { \prime } } ^ { s m a x } , \ t _ { j ^ { \prime } } ^ { e m i n } , \ t _ { j ^ { \prime } } ^ { e m a x }$ $t _ { j ^ { r } } ^ { s , m i n } ,$ and $t _ { j } ^ { s , m a x }$ by Algorithm $^ { 2 , }$ we recalculate the minimum fleet size of locomotives and resolve the integrated TRLA problem using Algorithm 1. In this way, the canceled operation lines will be gradually recovered according to the travel demand.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: Recovery of operation lines
01: Input $m'$ and $n'$;
02: For the up-train direction, read $x_{ij}^{k} = 1$, $\forall i, j, k$;
03: Calculate $y_{ij}^{k} - \theta_{j} \cdot x_{ij}^{k}$, $\forall i, j, k$;
04: For $i' = 1 : m'$
05: Get the maximum value $(y_{ij}^{k} - \theta_{j} \cdot x_{ij}^{k}) \cdot x_{ij}^{k}$;
06: Calculate $t_{i}^{e\min} = t_{i}^{e\min} + y_{ij}^{k}/2$ and $t_{i}^{e\max} = t_{i}^{e\max} + y_{ij}^{k}/2$;
07: Calculate $t_{i}^{s\min} = t_{i}^{s\min} - \tau_{u}$ and $t_{i}^{s\max} = t_{i}^{e\max} - \tau_{u}$;
08: Let $x_{ij}^{k} = 0$ and update $i'$;
09: End for
10: For the down-train direction, read $x_{ji}^{k} = 1$, $\forall i, j, k$;
11: Calculate $y_{ji}^{k} - \theta_{i} \cdot x_{ji}^{k}$, $\forall i, j, k$;
12: For $j' = 1 : n'$
13: Get the maximum value $(y_{ji}^{k} - \theta_{i} \cdot x_{ji}^{k}) \cdot x_{ji}^{k}$
14: Calculate $t_{j}^{e\min} = t_{j}^{e\min} + y_{ji}^{k}/2$ and $t_{j}^{e\max} = t_{j}^{e\max} + y_{ji}^{k}/2$;
15: Calculate $t_{j}^{s\min} = t_{j}^{e\min} - \tau_{d}$ and $t_{j}^{s\max} = t_{j}^{e\max} - \tau_{d}$;
16: Let $x_{ji}^{k} = 0$ and update $j'$;
17: End for
</div>

On the other hand, operation lines can be rapidly reduced when the COVID-19 pandemic continues to spread. The reduction is based on the results of locomotive utilization. Similarly, let m<sup>′′</sup> and n<sup>′′</sup> be the numbers of operation lines reduced along the up-train direction and the downtrain direction, respectively. The idea of Algorithm 3 is to cut the operation lines with the shortest idle times of locomotives. In this way, the utilization of locomotives will be more balanced in terms of

operating time and frequency.

<table><tr><td colspan="2">Algorithm 3: Cutting of operation lines</td></tr><tr><td>01:</td><td>Input  $m''$  and  $n''$ ;</td></tr><tr><td>02:</td><td>For the up-train direction, read  $x_{ij}^{k} = 1$ ,  $\forall i, j, k$ ;</td></tr><tr><td>03:</td><td>Calculate  $y_{ij}^{k} - \theta_{j} \cdot x_{ij}^{k}$ ,  $\forall i, j, k$ ;</td></tr><tr><td>04:</td><td>For  $i' = 1:m'$ </td></tr><tr><td>05:</td><td>Get the minimum value  $(y_{ij}^{k} - \theta_{j} \cdot x_{ij}^{k}) \cdot x_{ij}^{k}$ ;</td></tr><tr><td>06:</td><td>Let  $x_{ij}^{k} = 0$  and update  $i'$ ;</td></tr><tr><td>07:</td><td>End for</td></tr><tr><td>08:</td><td>For the down-train direction, read  $x_{ji}^{k} = 1$ ,  $\forall i, j, k$ ;</td></tr><tr><td>09:</td><td>Calculate  $y_{ji}^{k} - \theta_{i} \cdot x_{ji}^{k}$ ,  $\forall i, j, k$ ;</td></tr><tr><td>10:</td><td>For  $j' = 1:n'$ </td></tr><tr><td>11:</td><td>Get the minimum value  $(y_{ji}^{k} - \theta_{i} \cdot x_{ji}^{k}) \cdot x_{ji}^{k}$ </td></tr><tr><td>12:</td><td>Let  $x_{ji}^{k} = 0$  and update  $j'$ ;</td></tr><tr><td>13:</td><td>End for</td></tr></table>

## 6. Case study

The Beijing-Tianjin intercity railway connects two important cities in North China: Beijing and Tianjin. It is an important part of intercity rail transit network around the Bohai Sea in China’s medium and long term railway network planning. It is also the first high-speed railway with a high standard design speed of 350 km/h in mainland China. In this section, we will use the Beijing-Tianjin intercity railway to test the effectiveness of the developed models and algorithms. Fig. 4 shows the 24 operation lines of the intercity railway during the COVID-19 outbreak. The up-train direction operation lines start from Tianjin Sta tion and terminate at Beijing South Station. The down-train direction operation lines are in the opposite direction. Train numbers and schedules are given above and below the operation lines, respectively.

In addition to the above information about operation lines and train schedules, the parameters in the MILP models are given as follows. The earliest and latest start times of the operation lines can be adjusted within 2 min of the published schedule. The technical operation time of the locomotives for the up-train and down-train operation lines is 30 min and 20 min, respectively. The minimum headway for each consecutive pair of trains is 12 min. The up-train weight set is {1,2, 1,2,1, 1,2, 1,1,2, 2,1} and the down-train weight set is {1,2, 2,2,2, 1,2, 2,2,2, 1,2}, which are determined based on their travel times. The longer the travel time, the less the weight of the train. The maximum number of traction tasks assigned to each locomotive is eight and the locomotive weight set is initially given as {1, 2, 1, 2, 2, 2, 2, 2}.

## 6.1. Optimal results

We first solved the MILP-3 model running on an Intel Xeon Silver CPU at 2.10 GHz and a 32 GB RAM workstation. The above scenario took approximately 12 min. As a result, the minimum fleet size is four loco motives. Based on this, the MILP-4 model was solved to obtain the minimum total traction idle time for locomotives at the minimum fleet size. It took nearly 83 min to optimally solve the MILP-4 model. After optimizing the published schedule for the Beijing-Tianjin intercity rail way, we obtained 288 combinations of traction idle times, as shown in Fig. 5. These 288 values are arranged in accordance with certain rules: traction idle times of up-train operation lines to down-train operation lines are marked with squares, traction idle times of down-train opera tion lines to up-train operation lines are marked with circles, and each operation line has 14 mappings to the operation line in the opposite direction. All mappings are ordered based on the start time and end time of their operation lines. For example, the traction idle time from train C2202 to train C2201 is 1405 min and the traction idle time from train C2201 to train C2202 is 1393 min. This indicates that train C2202 and train C2201 cannot be connected by a single locomotive due to the required technical operation time.

Among the 288 combinations of traction idle times, the optima operation chains generated by the MILP-4 model are given in Table 1. There are four chains assigned to four locomotives, which consist of the minimum fleet size of the aforementioned locomotives. It can be seen that each operation chain is characterized by the precedence operation line, the current operation line, the end time of the precedence operation line, the start time of the current operation line, and the technical operation time. Based on the above information, the corresponding traction idle time was calculated in the last column. The longest traction idle time was 215 min, indicating that the locomotive has to wait for more than 3 h after completing the traction of C2218 and preparing it for C2219. The shortest traction idle time was 0 min, indicating that the traction of C2018 and C2025 is seamless. The number of traction tasks in each operation chain is different. This is because the optimal train schedules obtained are not periodic.

Fig. 6 shows the optimal train schedule with locomotive assignment plans in an intuitive way, where the locomotive assignment plans are distinguished by a different color. The operation lines grouped in the same operating chain are connected by arrow lines from the up-train direction to the down-train direction and vice versa. In this way. each locomotive completes its daily traction tasks and is connected to the next day’s tasks. For example, when a locomotive performs a sequence of tasks C2201 - C2018 - C2025 - C2212 - C2037 - C2218 - C2219, it will be linked to the next day’s tasks in C2206 highlighted by the dotted arrow line. As can be seen, all the operation lines are connected and the lo comotives are recycled.

## 6.2. Inserting operation lines

As mentioned earlier, the operation lines will gradually recover afte an effective control of COVID-19. We set the number of operation lines to be inserted in the up-train direction m<sup>′</sup> and in the down-train direction n<sup>′</sup> to 2, respectively. Using Algorithm 2, four operation lines are generated, as shown in Table 2. Each inserted operation line receives the necessary information, such as start and end stations, departure and arrival times, as well as trip travel time.

![](/api/attachments/2EHA7A9M/fulltext/images/66476d92eb8c639998e4c33ad9fc5414b0805a2e2aa1fab94205c320005364fc.jpg)  
Fig. 4. Operation lines of the Beijing-Tianjin intercity railway during COVID-19.

![](/api/attachments/2EHA7A9M/fulltext/images/a37cb3644b1484a491bbea791fc3c05441d47d811a0a8b4942ae70e939823289.jpg)  
Fig. 5. All traction idle times after optimization

Table 1 Optimal operation chains.

<table><tr><td>Operation chain</td><td>From i/j</td><td>To j/i</td><td> $t_i^e/t_j^e$ </td><td> $t_j^s/t_i^s$ </td><td> $θ_j/θ_i$ </td><td>Idle time</td></tr><tr><td rowspan="6">Chain 1</td><td>C2201</td><td>C2018</td><td>421</td><td>552</td><td>20</td><td>111</td></tr><tr><td>C2018</td><td>C2025</td><td>586</td><td>616</td><td>30</td><td>0</td></tr><tr><td>C2025</td><td>C2212</td><td>650</td><td>671</td><td>20</td><td>1</td></tr><tr><td>C2212</td><td>C2037</td><td>712</td><td>763</td><td>30</td><td>21</td></tr><tr><td>C2037</td><td>C2218</td><td>797</td><td>829</td><td>20</td><td>12</td></tr><tr><td>C2218</td><td>C2219</td><td>870</td><td>1115</td><td>30</td><td>215</td></tr><tr><td rowspan="5">Chain 2</td><td>C2206</td><td>C2017</td><td>479</td><td>561</td><td>30</td><td>52</td></tr><tr><td>C2017</td><td>C2034</td><td>595</td><td>721</td><td>20</td><td>106</td></tr><tr><td>C2034</td><td>C2053</td><td>755</td><td>906</td><td>30</td><td>121</td></tr><tr><td>C2053</td><td>C2226</td><td>940</td><td>1088</td><td>20</td><td>128</td></tr><tr><td>C2226</td><td>C2079</td><td>1129</td><td>1253</td><td>30</td><td>94</td></tr><tr><td rowspan="5">Chain 3</td><td>C2202</td><td>C2013</td><td>415</td><td>503</td><td>30</td><td>58</td></tr><tr><td>C2013</td><td>C2210</td><td>537</td><td>610</td><td>20</td><td>53</td></tr><tr><td>C2210</td><td>C2211</td><td>651</td><td>728</td><td>30</td><td>47</td></tr><tr><td>C2211</td><td>C2050</td><td>769</td><td>943</td><td>20</td><td>154</td></tr><tr><td>C2050</td><td>C2061</td><td>977</td><td>1038</td><td>30</td><td>31</td></tr><tr><td rowspan="4">Chain 4</td><td>C2004</td><td>C2027</td><td>430</td><td>666</td><td>30</td><td>206</td></tr><tr><td>C2027</td><td>C2216</td><td>700</td><td>785</td><td>20</td><td>65</td></tr><tr><td>C2216</td><td>C2049</td><td>826</td><td>894</td><td>30</td><td>38</td></tr><tr><td>C2049</td><td>C2054</td><td>928</td><td>970</td><td>20</td><td>22</td></tr></table>

Table 3 shows the optimal results for the operation chains after inserting four operation lines and increasing the number of operation chains to five. In this case, the fleet size requires one more locomotive. As for the traction idle time, the total value increases from 1535 to 1689 min. This is due to the increased number of operation lines and opera tion chains. However, when we calculate the average traction idle time, the value decreases from 76.75 to 73.43 min, which indicates a more compact arrangement of operation lines and traction tasks. We should also note that there are still long traction idle times, such as the connection of C2018 and C2053, as well as the connection of C2050 and C2079. Such long traction idle times will be gradually eliminated as the number of inserted operation lines increases. At the same time, more locomotives will be needed for the Beijing-Tianjin intercity railway. Fig. 7 intuitively shows the optimal train schedule with five locomotive assignment plans. The five locomotive assignment plans are distin guished by different colors. Similarly, the operation lines under the same operation chain are connected by arrow lines from the up-train direction to the down-train direction and vice versa.

Table 2  
Results of inserted operation lines by using Algorithm 2.

<table><tr><td>Operation line</td><td>Between</td><td>Departure from Arriving at</td><td>Departing time Arrival time</td><td>Travel time</td></tr><tr><td rowspan="2">Insert-1</td><td>C2004</td><td>Tianjin</td><td>8:38:00</td><td>30 min</td></tr><tr><td>C2027</td><td>Beijing South</td><td>9:08:00</td><td></td></tr><tr><td rowspan="2">Insert-2</td><td>C2211</td><td>Beijing South</td><td>13:39:00</td><td>37 min</td></tr><tr><td>C2053</td><td>Tianjin</td><td>14:16:00</td><td></td></tr><tr><td rowspan="2">Insert-3</td><td>C2218</td><td>Tianjin</td><td>16:03:00</td><td>30 min</td></tr><tr><td>C2219</td><td>Beijing South</td><td>16:33:00</td><td></td></tr><tr><td rowspan="2">Insert-4</td><td>C2053</td><td>Beijing South</td><td>16:17:00</td><td>37 min</td></tr><tr><td>C2226</td><td>Tianjin</td><td>16:54:00</td><td></td></tr></table>

![](/api/attachments/2EHA7A9M/fulltext/images/7b7cbaa6e01e15de81da7c9a3949ef2eb4d867f15f9b5ab6ee310cab44249dc2.jpg)  
Fig. 6. Optimal result of locomotive assignment.

Table 4  
Table 3  
Optimal operation chains with inserted operation lines.

<table><tr><td>Operation chain</td><td>From i/j</td><td>To j/i</td><td> $t_i^e/t_j^e$ </td><td> $t_j^s/t_i^s$ </td><td> $θ_j/θ_i$ </td><td>Idle time</td></tr><tr><td rowspan="4">Chain 1</td><td>C2201</td><td>C2018</td><td>421</td><td>552</td><td>20</td><td>111</td></tr><tr><td>C2018</td><td>C2053</td><td>586</td><td>906</td><td>30</td><td>290</td></tr><tr><td>C2053</td><td>C2054</td><td>940</td><td>973</td><td>20</td><td>13</td></tr><tr><td>C2054</td><td>C2219</td><td>1004</td><td>1115</td><td>30</td><td>81</td></tr><tr><td rowspan="3">Chain 2</td><td>C2004</td><td>C2013</td><td>430</td><td>503</td><td>30</td><td>43</td></tr><tr><td>C2013</td><td>C2210</td><td>537</td><td>610</td><td>20</td><td>53</td></tr><tr><td>C2210</td><td>C2211</td><td>651</td><td>728</td><td>30</td><td>47</td></tr><tr><td rowspan="5">Chain 3</td><td>C2202</td><td>C2027</td><td>415</td><td>666</td><td>30</td><td>221</td></tr><tr><td>C2027</td><td>C2034</td><td>700</td><td>721</td><td>20</td><td>1</td></tr><tr><td>C2034</td><td>Insert-2</td><td>755</td><td>817</td><td>30</td><td>32</td></tr><tr><td>Insert-2</td><td>C2050</td><td>858</td><td>943</td><td>20</td><td>65</td></tr><tr><td>C2050</td><td>C2079</td><td>977</td><td>1253</td><td>30</td><td>246</td></tr><tr><td rowspan="6">Chain 4</td><td>Insert-1</td><td>C2025</td><td>550</td><td>616</td><td>30</td><td>36</td></tr><tr><td>C2025</td><td>C2212</td><td>650</td><td>671</td><td>20</td><td>1</td></tr><tr><td>C2212</td><td>C2037</td><td>712</td><td>763</td><td>30</td><td>21</td></tr><tr><td>C2037</td><td>C2218</td><td>797</td><td>829</td><td>20</td><td>12</td></tr><tr><td>C2218</td><td>Insert-4</td><td>870</td><td>975</td><td>30</td><td>75</td></tr><tr><td>Insert-4</td><td>C2226</td><td>1016</td><td>1088</td><td>20</td><td>52</td></tr><tr><td rowspan="5">Chain 5</td><td>C2206</td><td>C2017</td><td>479</td><td>561</td><td>30</td><td>52</td></tr><tr><td>C2017</td><td>C2216</td><td>595</td><td>785</td><td>20</td><td>170</td></tr><tr><td>C2216</td><td>C2049</td><td>826</td><td>894</td><td>30</td><td>38</td></tr><tr><td>C2049</td><td>Insert-3</td><td>928</td><td>961</td><td>20</td><td>13</td></tr><tr><td>Insert-3</td><td>C2061</td><td>992</td><td>1038</td><td>30</td><td>16</td></tr></table>

## 6.3. Analysis of timetabling parameters and locomotive idle time

Based on the timetabling parameters set by default, we adjust the minimum and maximum values of the start and end times of the oper ation lines to see how they affect the traction idle times. Table 4 shows the test results of nine scenarios, where the start and end times of the operation lines can be adjusted from 4 to 20 min in steps of 2 min. As a result, the total traction idle time of locomotives decreases with the increase in the timetabling adjustable range. This indicates that the timetabling parameters in MILP models can be appropriately set to improve locomotive turnover efficiency. However, the locomotive fleet size does not change even though the difference between the end (upper bound) and start (lower bound) times of operation lines has been increased to 20 min. This shows that the amount of traction demand plays a decisive role in the locomotive fleet size, while the operation line schedule also has an influence on the fleet size.

Fig. 8 shows the comparison of the nine tests, through which we can find a certain regularity in the results. From the first test (a range of 4 min) to the last test (a range of 20 min), there is no significant change in the optimal traction idle times in the same mapping. However, this also indicates that the range of adjustable timetabling parameters affects the total traction idle time. Furthermore, there are more data points in the lower left corner of Fig. 8(a) compared to the lower left corner of Fig. 8 (b). This confirms our aforementioned finding that for the Beijing-Tianjin intercity railway, the up-train to down-train connection case has more examples of low traction idle times compared to the downtrain to up-train connection case.

## 7. Conclusion

This study investigated the integrated TRLA problem during the COVID-19 outbreak until full recovery that was achieved with a focus on operating costs. Specifically, it optimally adjusted train schedules in the course of a significant reduction in operation lines and resumed train schedules to normal operations by fully considering the locomotive assignment problem in a dedicated railway corridor. An exact MILP model developed for the TRLA problem was solved using an optimized two-step sequential algorithm. Taking the Beijing-Tianjin intercity railway as a case study, the proposed models and algorithms were conducted for testing. The numerical results indicate that train rescheduling parameters should be properly set to improve locomotive turnover efficiency. However, the locomotive fleet size was not affected by the above parameters, but by the traction demand. The paper con tributes to the decision-making process for solving engineering prob lems, especially with respect to train scheduling and locomotive utilization problems during public health emergencies. Moreover, our study can provide advice on how to optimally start adding (cutting) operation lines back into (from) circulation based on pandemic changes. Furthermore, the proposed solution can be applied to any other type of disruption with similar characteristics, such as significantly reducing travel demand and progressively providing information. This study has some limitations; for example, it did not consider the refined passenger travel demand, which was an input to the developed model. However, it is difficult to predict the actual travel demand of passengers in COVID-

Analysis of timetabling parameters.

<table><tr><td>Test</td><td> $t_i^{s,min}$ </td><td> $t_i^{e,max}$ </td><td>Range</td><td>Objective</td><td>Fleet size</td></tr><tr><td>#1</td><td> $pt_i^s - 2$ </td><td> $pt_i^e + 2$ </td><td>4 min</td><td>5470 min</td><td>5</td></tr><tr><td>#2</td><td> $pt_i^s - 3$ </td><td> $pt_i^e + 3$ </td><td>6 min</td><td>5414 min</td><td>5</td></tr><tr><td>#3</td><td> $pt_i^s - 4$ </td><td> $pt_i^e + 4$ </td><td>8 min</td><td>5358 min</td><td>5</td></tr><tr><td>#4</td><td> $pt_i^s - 5$ </td><td> $pt_i^e + 5$ </td><td>10 min</td><td>5302 min</td><td>5</td></tr><tr><td>#5</td><td> $pt_i^s - 6$ </td><td> $pt_i^e + 6$ </td><td>12 min</td><td>5246 min</td><td>5</td></tr><tr><td>#6</td><td> $pt_i^s - 7$ </td><td> $pt_i^e + 7$ </td><td>14 min</td><td>5190 min</td><td>5</td></tr><tr><td>#7</td><td> $pt_i^s - 8$ </td><td> $pt_i^e + 8$ </td><td>16 min</td><td>5134 min</td><td>5</td></tr><tr><td>#8</td><td> $pt_i^s - 9$ </td><td> $pt_i^e + 9$ </td><td>18 min</td><td>5078 min</td><td>5</td></tr><tr><td>#9</td><td> $pt_i^s - 10$ </td><td> $pt_i^e + 10$ </td><td>20 min</td><td>5022 min</td><td>5</td></tr></table>

![](/api/attachments/2EHA7A9M/fulltext/images/50b29b55dec60ef37eac86087b0a00e674ba72b081507e4e0f344c87fd397a3c.jpg)  
Fig. 7. Optimal result of locomotive assignment with inserted operation lines.

![](/api/attachments/2EHA7A9M/fulltext/images/5963bd4e479588ea6b5c4083fb8fc0ea1b76f50bcd72b1ece0f65215618c0914.jpg)  
(a) The index of opera-on line mapping (up-train direc-on to down-train direc-on)

![](/api/attachments/2EHA7A9M/fulltext/images/1b60d643061f77162d9db34f4d212f22895e8d9e8687202581d7cc245f844cca.jpg)  
(b) The index of opera-on line mapping (down-train direc-on to up-train direc-on)  
Fig. 8. Comparison and tests with different timetabling parameters.

## 19.

In future studies, we will focus on the demand-driven TRLA problem in the context of a gradual recovery in passenger flows. During the COVID-19 outbreak, travel demand was significantly reduced and China Railway Companies made overall adjustments to the planned opera tional plans to handle the disruption. The demand-driven TRLA problem will differ from the current one in several aspects, such as the objective function and the necessary model constraints. More importantly, our proposed two-step sequential algorithm may not be suitable to address the new TRLA problem, and it is also difficult to deal with large-scale applications when considering passenger flows.

## Acknowledgments

The paper is supported by the National Key Research and Develop ment Program of China (2019YFB1600200), the National Natural Sci ence Foundation of China (72001017; 71890970/71890972; 71801181), and the Fundamental Research Funds for the Central Uni versities (2019JBZ108).

## References

[1] J.S. Jia. X. Lu. Y. Yuan, G. Xu, J. Jia, N.A. Christakis, Population flow drives spatiotemporal distribution of COVID-19 in China, Nature 582 (2020) 389–394.

[2] N. Ghaemi, A.A. Zilko, F. Yan, O. Cats, D. Kurowicka, R.M.P. Goverde, Impact of railway disruption predictions and rescheduling on passenger delays, J. Rail Transport Plan. Manag. 8 (2018) 103–122

[3] Z.E. Bowden, C.T. Ragsdale, The truck driver scheduling problem with fatigue

[4] S.P. Josyula, J.T. Krasemann, L. Lundberg, A parallel algorithm for train rescheduling, Transp. Res. C 95 (2018) 545–569.

[5] L.P. Veelenturf, M.P. Kidd, V. Cacchiani, L.G. Kroon, P. Toth, A railway timetable rescheduling approach for handling large-scale disruptions, Transp. Sci. 50 (3) (2015) 1–22.

[6] Z. Hou, H. Dong, S. Gao, G. Nicholson, L. Chen, C. Roberts, Energy-saving metro train timetable rescheduling model considering ATO profiles and dynamic passenger flow, JEEE Trans, Intell, Transp, Syst, 20 (7) (2019) 2774–2785.

[7] L. Kang, X. Zhu, H. Sun, J. Wu, Z. Gao, B. Hu, A practical model for last train rescheduling with train delay in urban railway transit networks, Omega 84 (2015)

[8] G. Yang, W. Wang, F. Zhang, S. Zhang, C. Gong, A real-time timetable rescheduling method for metro system energy optimization under dwell-time disturbances, J Adv. Transp. 5174961 (2019)

[9] M. Shakibayifar, A. Sheikholeslami, F. Corman, E. Hassannayebi, An integrated rescheduling model for minimizing train delays in the case of line blockage, Operation Res. Int. J. 20 (2017) 59–87.

[10] M. Fischetti, M. Monaci, Using a general-purpose mixed-integer linear programming solver for the practical solution of real-time train rescheduling, Eur J. Oper. Res. 263 (2017) 258–264.

[11] D. Semrov, <sup>ˇ</sup> R. Marseti, M. Zura, <sup>ˇ</sup> L. Todorovski, A. Srdic, Reinforcement learning approach for train rescheduling on a single-track railway, Transp. Res. B 86 (2016) 250–267.

[12] J.A. Nasir, Y.H. Kuo, A decision support framework for home health care transportation with simultaneous multi-vehicle routing and staff scheduling synchronization, Decis. Support. Syst. 138 (2020) 113361.

[13] K. Sato, K. Tamura, N. Tomii, A MIP-based timetable rescheduling formulation and algorithm minimizing further inconvenience to passengers, J. Rail Transport Plan. Manag. 3 (2013) 38–53.

[14] P. Kecman, F. Corman, A. D’Ariano, R.M.P. Goverde, Rescheduling models for railway traffic management in large-scale networks, Public Transport 5 (2013)

[15] M. Shakibayifar, A. Sheikholeslami, A. Jamili, A multi-objective decision suppor system for real-time train rescheduling, IEEE Trans. Intel. Transport. Syst. Magazine (2018), https://doi.org/10.1109/MITS.2018.2842037.

[16] V. Cacchiani, D. Huisman, M. Kidd, L. Kroon, P. Toth, L. Veelenturf, J. Wagenaar, An overview of recovery models and algorithms for real-time railway rescheduling Transp Res, B 63 (2014).15–37

[17] R.K. Ahuja, J. Liu, J.B. Orlin, D. Sharma, L.A. Shughart, Solving real-life locomotive-scheduling problems, Transp. Sci. 39 (4) (2005) 503–517.

[18] A. Alfieri, R. Groot, L. Kroon, A. Schrijver, Efficient circulation of railway rolling stock, Transp. Sci. 40 (3) (2006) 378–391.

[19] M. Peeters, L. Kroon, Circulation of railway rolling stock: a branch-and-price approach, Comput. Oper. Res. 35 (2) (2008) 538–556.

[20] V. Cacchiani, A. Caprara, P. Toth, Solving a real-world train-unit assignment problem, Math. Program. 124 (1–2) (2010) 207–231.

[21] L. Cadarso, A. <sup>´</sup> Marín, Robust rolling stock in rapid transit networks, Comput. Oper. Res. 38 (8) (2011) 1131–1142.

[22] J.T. Haahr, J.C. Wagenaar, L.P. Veelenturf, L.G. Kroon, A comparison of two exact methods for passenger railway rolling stock (re)scheduling, Transp. Res. E 91 (2016) 15–32.

[23] Y. Wang, T. Tang, B. Ning, L. Meng, Integrated optimization of regular train schedule and train circulation plan for urban rail transit lines, Transp. Res. E 105 (2017) 83-104.

[24] D. Canca, E. Barrena, The integrated rolling stock circulation and depot location problem in railway rapid transit systems, Transp. Res. E 109 (2018) 115–138.

[25] L. Cadarso, A. <sup>´</sup> Marín, Integration of timetable planning and rolling stock in rapid transit networks, Ann. Oper. Res. 199 (2012) 113–135.

[26] T. Godwin, R. Gopalan, T.T. Narendran, Tactical locomotive fleet sizing for freight train operations, Transp. Res. E 44 (2008) 440–454.

[27] M. Michaelis, A. Schobel, ¨ Integrating line planning, timetabling, and vehicle scheduling: a customer-oriented heuristic, Public Transport 3 (1) (2009) 211–232.

Liujiang Kang received a Ph.D. degree in traffic and transportation planning and man agement from Beijing Jiaotong University, China, in 2016. He was a Research Fellow with the Department of Civil and Environmental Engineering, National University of Singapore. He is currently a Professor at Beijing Jiaotong University. He is a reviewer of more than 10 international journals, such as Transportation Research Part A: Policy and Practice, Transportation Research Part B: Methodological, Transportation Research Part C: Emerging Technologies, the Journal of Transportation Engineering, the Journal of Advanced Transportation, and the Journal of Rail and Rapid Transit. His research interests include operations research, optimization theory, and transportation and logistics. He ha published more than 20 articles in international journals.

Yue Xiao is a graduate student at Beijing Jiaotong University. His research interests include urban traffic planning and management. He received a bachelor’s degree from Jilin Uni versity. He got a lot of awards and honors such as the national scholarship and enterprise scholarship.

Huijun Sun is a professor at Beijing Jiaotong University. Her research interests contain urban transportation, urban traffic management, and transportation and logistics. He has published more than 60 articles in international journals, such as Transportation Research Part A: Policy and Practice. Transportation Research Part B: Methodological. Trans portation Research Part C: Emerging Technologies, Transportation Research Part E: Lo gistics and Transportation Review, Omega, etc.

Jianjun Wu is a professor at Beijing Jiaotong University. His research interests focus on operations research, urban traffic management, and transportation and logistics. He has published more than 80 articles in international journals, including Transportation Research Part A: Policy and Practice, Transportation Research Part B: Methodological, Transportation Research Part C: Emerging Technologies, Transportation Research Part E: Logistics and Transportation Review, etc.

Sida Luo received his Ph.D. degree from Northwestern University. Currently, he is a pro fessor at Beijing Jiaotong University. His research interests focus on operations research and urban traffic optimization. His research contents have been published in Trans portation Research Part A: Policy and Practice, Transportation Research Part B: Method ological, Transportation Research Part C: Emerging Technologies.

Nsabimana Buhigiro is a graduate student at Beijing Jiaotong University. His research interests include urban rail transit management. His study has been published in Frontiers of Engineering Management. He received a bachelor’s degree from University of Rwanda - College of Science and Technology.
