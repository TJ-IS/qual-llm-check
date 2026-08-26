---
otero_id: 15318
otero_key: "7RMRJFM4"
title: "On the impact of analyzing customer information and prioritizing in a service system"
authors: "Gregory Dobson; Arvind Sainathan"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the impact of analyzing customer information and prioritizing in a service system

Gregory Dobson <sup>a,1</sup>, Arvind Sainathan <sup>b,</sup>⁎

<sup>a</sup> CS-3-310 Carol Simon Hall, William E Simon Graduate School of Business Administration, University of Rochester, Rochester, NY 14627, United States <sup>b</sup> S3-B2A-03, Nanyang Business School, 50 Nanyang Avenue, NTU, 639798, Singapore

## a r t i c l e i n f o

Available online 4 February 2011

Keywords: Prioritization Information intensive Service systems Triaging Sorters Processors Queuing

## a b s t r a c t

This paper examines prioritization in a service system and analyzes whether, in the presence of heterogeneous customers who have different needs and a costly sorting process, it pays to prioritize. In particular, in our model, sorting is costly because the task of gathering information to prioritize jobs consumes resources. We investigate a stylized model in which there are two classes of jobs — one whose waiting cost is high, called urgent, and the other whose waiting cost is low, called non-urgent. There are two types of employees, sorters, who collect information on a job and then decide whether it is urgent or non-urgent, and processors, who execute the job or provide the service. We begin by assuming that sorters categorize customers perfectly, and we relax this assumption later in the paper. We optimize two performance metrics, waiting costs (under a given budget) and total costs, and <sup>fi</sup>nd the conditions under which prioritization is beneficial for these two metrics

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

We analyze the <sup>fl</sup>ow of work through a service system and answer the question whether prioritizing jobs helps improve system performance. There are two classes of jobs that differ in their need for a quick service; one that has a high waiting cost, called urgent, and the other that has a low waiting cost, called non-urgent. Although the class of a job can be determined by reviewing or collecting information about the job, the job is not a-priori tagged as urgent or non-urgent when it arrives. The sorters collect and review this information and determine the class. They correctly classify jobs into urgent and non-urgent, and then place the jobs in the appropriate queue. The processors then provide the service using an HOL (head of the line) priority [6] for urgent customers. We compare this con<sup>fi</sup>guration to a system that has no sorters and no prioritization, and thus it saves the cost of the sorters. We use the terms “customers” and “jobs” interchangeably in the paper.

Although prioritization has been examined in the literature on queuing theory [6], there are two important features that distinguish our work. The <sup>fi</sup>rst feature is that we consider prioritization to be an information intensive process that consumes both time and money. However, most of the literature assumes that the customer class is known or can be determined for free. This assumption is not true for many service systems. For instance, in emergency departments (EDs), triage nurses typically gather this information. The main reason for having triage nurses here is because neither they nor the patient may know upfront whether the patient is urgent without this information. Therefore, for such service systems, under prioritization, another set of employees, sorters, needs to collect and review information about a job, and determine its class. The second feature is that we account for the fact that some of the information collected by the sorters might be useful to the processors who still provide the actual service (e.g., some health information collected by triage nurses can be used by physicians in EDs). While prioritization is thus bene<sup>fi</sup>cial by enabling quick service to urgent customers, it is also costly because it consumes additional resources. We describe the bene<sup>fi</sup>ts and costs below in detail.

In our model, there are two bene<sup>fi</sup>ts associated with sorting:

1. Prioritization — The literature on queuing theory shows that prioritization improves the average waiting cost of a queuing system [6] if customers are heterogeneous in waiting costs. Though the lower waiting cost customers wait longer, that is more than compensated by the higher waiting cost customers waiting less thereby reducing the expected waiting cost for the whole system. However, a shortcoming of this research literature is that it considers only this aspect of prioritization.

2. Useful information from sorters — This information gathering might result in a reduction of work for processors and hence increase their service rate resulting in shorter wait for customers. In this aspect, sorting is somewhat similar to “pre-processing” that is common in many service systems (e.g., EDs).

On the other hand, there are additional costs resulting from:

1. Expenditures on sorters — Their salaries either increase the budget or reduce the money available for processors.

2. Additional waiting by customers — Customers must go through the sorting step now. Although these customers initially incur the waiting cost, we model it as a cost that the service system incurs because it <sup>fi</sup>nally impacts that system through loss of reputation, perception of poor customer service, etc.

The fundamental contribution of this paper is that it analyzes prioritization more broadly by considering all four aspects. We perform this analysis by considering two service system designs. In the <sup>fi</sup>rst design processors see all the jobs in an FCFS manner. We will refer to this system as the base system. In the second design sorters determine whether jobs are urgent or not, and place jobs in a priority queue for the processors. We will refer to this system as the prioritized system. There are many examples of service systems for which our analysis is applicable. Below, we give three instances:

1. Healthcare operations: Our problem is best illustrated by emergency departments in which triage nurses (sorters) initially screen patients (jobs) and prioritize them based on their acuity. The patients are then seen and treated by emergency department physicians (processors). For many hospitals, reducing patient waiting times at EDs has become a number one priority to improve customer service. It also helps in “word of mouth” marketing for the hospital [20]. However, at many EDs delays continue, and patients sick from innocuous ailments such as the common cold or a minor cut have long waits before they get treated [3]. Could a prioritized queuing system at the EDs be a part of this problem? Our paper aims to answer this question. This example best illustrates our research problem. However, note that when we refer to urgent patients, we do not consider extremely urgent or emergent patients (e.g., patients with gunshot wounds) who, for many EDs, account for a small fraction of the total number of patients and more importantly, do not need triage to determine their acuity.

2. Call center operations management: In this case, call centers could employ “gatekeepers/initial contacts” whose purpose is to screen the calls and prioritize them. Hence, in our model, the gatekeepers are sorters, the actual service providers are processors, and the customers' calls are the jobs. Our question here becomes whether the call center should employ these gatekeepers at all or should it just service the calls on an FCFS basis.

3. Work<sup>fl</sup>ow scheduling/project management: In a typical of<sup>fi</sup>ce/ workplace environment, administrative assistants and managers perform the role of sorters and processors respectively. Regular of<sup>fi</sup>ce work or projects will be “jobs”. It is an important question to analyze whether the projects need to be prioritized or just executed on an FCFS basis. One speci<sup>fi</sup>c example of this case would be a DMV (Department of Motor Vehicles) of<sup>fi</sup>ce in the US where customers are initially “screened” and are then classi<sup>fi</sup>ed/prioritized based on the type of processing their work requires.

The paper is organized in the following structure. Section 2 brie<sup>fl</sup>y reviews the related literature. In Section 3 we formulate the model and discuss its assumptions. In Section 4 we analyze the impact of prioritization when the waiting costs are minimized under an exogenous budget. In Section 5 we perform a similar analysis when the total costs are minimized. In both Section 4 and Section 5 we assume sorting is perfect. In Section 6 we consider imperfect sorting and prove that it is always worse than perfect sorting. Section 7 provides a discussion about other possible extensions of our model. Section 8 concludes. All proofs can be found in the online appendix.

## 2. Literature survey

Our research problem is related to three areas: queuing optimization and priority queues, service system design, and project management/work<sup>fl</sup>ow scheduling. We consider papers from these three areas of literature.

First, there are some papers in the queuing optimization literature that involve pricing and consider capacity vs. waiting cost tradeoffs. Mendelson [14] <sup>fi</sup>nds that a <sup>fi</sup>rm's computer center/data center should be managed as a cost center for the value to be maximized. Dewan and Mendelson [7] extend the problem to a scenario in which user's delay cost is important and model it explicitly. Mendelson and Whang [15] consider the original problem with multiple priority classes for which they devise an optimal incentive compatibility pricing scheme. The similarity of these papers with our research is that all of them involve optimizing queuing systems by considering the tradeoff between capacity costs (or budget) and waiting costs. However they either do not consider priority [7] or if they do consider it [15], they devise pricing schemes so that customers will self-select. However, in our model, customers do not know their priority (e.g., patients in EDs as mentioned earlier) so self-selection is not possible.

There is an extensive literature on priority queues. We consider some important and relevant papers here. Cobham [5] considers HOL priority and derives the expected waiting times. Some papers have modeled priority with preemption in queuing systems [11,12]. Some papers have also considered the problem of <sup>fi</sup>nding optimal rules for a queuing system so that waiting cost is minimized [1,9]. There is also an extensive literature on queuing theory applied to manufacturing systems (see [4] and [16] respectively for reviews on <sup>fl</sup>exible manufacturing systems and lot sizing). The primary difference in our research from these papers is that we recognize that information collection for prioritization might consume time and money (this aspect is true in the case of EDs but not necessarily in the case of airline boarding in which prioritization is free and instantaneous, and therefore obviously preferable). Our research, therefore, generalizes some of the earlier research on priority queues.

Second, in many service environments, the process <sup>fl</sup>ow can be designed in different ways. The system that performs the best depends on the service environment. For instance, fast food outlets typically have a single queue for customers who order food while supermarkets tend to have multiple checkout aisles. Service system design involves selecting the best system depending on the performance metric(s) chosen. In this paper, we <sup>fi</sup>nd whether priority in a queuing system is preferable or not. Seidmann and Sundararajan [18] analyze different types of service-delivery processes for a <sup>fi</sup>rm that handles jobs that involve two different tasks. Shumsky and Pinker [19] consider a system with gatekeepers and specialists typical in a healthcare setting. They design a contract that will induce the gatekeepers to refer the optimal fraction of calls to specialists and enable the <sup>fi</sup>rm to achieve “<sup>fi</sup>rst best” pro<sup>fi</sup>ts. Hasija et al. [10] consider a similar setting but with waiting costs included. They then compare (for optimal staf<sup>fi</sup>ng levels) the systems with and without gatekeepers. There are two key differences between their paper and this paper — <sup>fi</sup>rst, there is no priority among jobs in their model and second, there is a critical difference between gatekeepers and sorters; while jobs leave after being treated correctly by the gatekeeper, they wait for the processor's treatment after being seen by a sorter in our model.

Third, this paper considers staf<sup>fi</sup>ng issues in addition to process and work<sup>fl</sup>ow design. Therefore, it relates to papers from the <sup>fi</sup>elds of work<sup>fl</sup>ow scheduling and project management that we now examine. Lewis et al. [13] come closest to ours in this literature. They model an administrative of<sup>fi</sup>ce as a closed queuing network to make two decisions — the staf<sup>fi</sup>ng level and the staf<sup>fi</sup>ng allocation. They consider two metrics, throughput and equity of employees. They <sup>fi</sup>nd that, for a given staf<sup>fi</sup>ng level maximizing the throughput also leads to maximizing the equity. However, that is not necessarily the case when staf<sup>fi</sup>ng level can be varied. Berman et al. [2] analyze and solve the generic problem of minimizing labor costs through ef<sup>fi</sup>cient shift scheduling in a high volume factory with service-level, contractual (e.g., certain shifts can start and end only at certain times) and physical constraints (e.g., limits on Work-In-Process inventory).

Our paper considers the impact of costly information collection during prioritization and pre-processing, in service systems. Dobson and Sainathan [8] use a similar model to study a similar problem. However, we characterize the individual cost and bene<sup>fi</sup>t components of prioritization, and <sup>fi</sup>nd how they vary with changing parameters, which they do not consider. Further, we consider the case of missorting of the customers (see Theorem 3).

## 3. The model

In this section, we provide the model that is used as a framework later to analyze the base system and the prioritized system. In the base system processors see all the jobs in an FCFS manner, and in the prioritized system, sorters determine which jobs are urgent and which are not and place them in a priority queue from which they are handled by the processors. The following notation is used in the paper:

λ Combined arrival rate of both job classes (/h)

$\mu _ { S }$ Service rate of a sorter (/h)

$\mu _ { P }$ Service rate of a processor under prioritization (/h)

$\mu _ { P } ^ { \prime }$ Service rate of a processor under the base system (/h)

$K _ { S }$ Salary of a sorter (\$/h)

$K _ { P }$ Salary of a processor (\$/h)

$q _ { u }$ Fraction of urgent jobs

$q _ { n }$ Fraction of non-urgent jobs $( = 1 - q _ { u } )$

$c _ { u }$ Waiting cost of urgent jobs $( \$ 10 b )$

$c _ { n }$ Waiting cost of non-urgent jobs (\$/h/job)

$r$ Cost ratio $\left( = c _ { u } / c _ { n } \right)$

$f$ Number of processors

$g$ Number of sorters

$\rho$ Load factor of sorters $( = \lambda / ( g \mu _ { S } ) )$

$\rho _ { u }$ Load factor of processors for urgent jobs under prioritization $( = \lambda q _ { u } / ( f \mu _ { P } ) )$

$\rho _ { n }$ Load factor of processors for non-urgent jobs under prioritization $( = \lambda q _ { n } / ( f \mu _ { P } ) )$

$W _ { S } ( K )$ For the system with sorters (i.e., under prioritization), the average waiting cost for budget $K \left( \mathbb { S } / \mathrm { h } \right)$

$W _ { S } ^ { * } ( K )$ For the system with sorters (i.e., under prioritization), the optimal average waiting cost for budget K (\$/h)

$W _ { P } ( K )$ For the system with just processors (i.e., the base system),

the optimal average waiting cost for budget K (\$/h)

We assume that the same pool of processors see both urgent and non-urgent jobs. Our focus in this paper is to understand if there is a value in sorting. To make this comparison, our base case, in which no sorting is done, must have processors that can handle both urgent and non-urgent jobs. Thus we assume that the processors handle the two types of jobs at the same rate for both designs, to focus on the bene<sup>fi</sup>t or lack of bene<sup>fi</sup>t from sorting. We assume that, from the system design perspective of this paper, all the processors receive the same average salary. We assume all service times to be exponentially distributed. In Section 7 we discuss the situation in which processors could specialize, could be in separate pools and have different rates for urgents and non-urgents, and discuss how this would affect our results. For an emergency department, except for extremely urgent or emergent patients, which we do not consider, the time to take a history and physical and generate a diagnosis is roughly the same. Though the actual diagnosis may take a little longer for urgent patients, the physician has to spend more time with non-urgent patients in counseling and providing care, and also in asking more questions because of the breadth of ailments. We <sup>fi</sup>nd that these two effects tend to cancel each other out [21].

As the name implies, urgent jobs have a higher cost of waiting so $c _ { u } > c _ { n } .$ The difference in waiting costs arises mainly because of possible future complications in some urgent patients due to the delay. Giving priority to the urgent jobs is justi<sup>fi</sup>ed in conjunction with the “cμ priority rule” [6] that states that priority for different classes is given in the decreasing order of the product of waiting cost and service rate. Because we want to focus on the design decision, whether to have sorters or not, we assume that the number of sorters and number of processors are continuous for the sake of analytical tractability. We allow for the possibility that sorting may alter the service rate of a processor because information collected by sorters may be useful to processors and thus may lead to faster service. The relationship between the average times for a processer to handle a customer in the two systems is:

$$
\frac {1}{\mu_ {P} ^ {\prime}} = \frac {1}{\mu_ {P}} + \frac {\alpha}{\mu_ {S}},\tag{1}
$$

where α is a measure of the useful information that is obtained by a sorter. If $\alpha { = } 0 ,$ then none of the information obtained by the sorter is useful to the processor, and the average service time of the processor is not impacted by the presence of sorters. If $\alpha { = } 1 0 0 \% ,$ all the information obtained by the sorter is useful to the processor, and the average service time of the processor under the base system is equal to sum of her average service time under prioritization and the sorter's average service time.

In the base system, there is no sorting and the queue is simply an FCFS queue because there is no prior knowledge of the urgency of jobs. The entire budget is spent on the processors.

In the prioritized system, service is provided in two steps: <sup>fi</sup>rst a sorter collects and reviews information on each job, determines whether it is urgent or non-urgent, and then places it in the appropriate queue. For now we assume that this sorting is perfect, i.e., the sorters correctly determine which jobs are urgent and which are not. We analyze a system with imperfect sorting in Section 6. Next, a processor services the jobs using head of the line (HOL) priority for urgents over non-urgents and a <sup>fi</sup>rst-come-<sup>fi</sup>rst-served (FCFS) discipline within each class. The service system splits the resources (budget) between the processors and sorters in a way that minimizes the average waiting cost. The process <sup>fl</sup>ow diagrams for both systems are given in Fig. 1.

![](/api/attachments/7RMRJFM4/fulltext/images/a056cee060297a5dc91a11260982aeeb36eb2db2a11106136cde8480d96b26b9.jpg)  
Fig. 1. Flow diagrams for the prioritized system and the base system.

We assume Poisson arrivals. We assume that whether each arrival is urgent or not is based on a Bernoulli random variable with a success probability of $q _ { u } .$ These random variables are also assumed to be independent. A multi-server queuing model is used for the analyses. Waiting time (that is used to compute the waiting cost that in turn is used in the performance measure) is de<sup>fi</sup>ned as the time elapsed from a job's entry to the service system to the completion of its service by a processor. Waiting costs are assumed to be linear in waiting times. In the ED, this assumption may be an approximation to reality because waiting costs might be convex. However, it would hold for many service systems and is quite commonly used in the queuing literature (see e.g., [1,9,10,14,15,18]). Although the jobs experience the wait, the service system is impacted by the waiting cost because of the perception of poor customer service, loss of reputation, loss of future revenue, additional expenditure due to service complications because of delayed service, etc. In Section 7 we discuss how one could include a deadline on waiting time in the analysis, for instance in the emergency room to allow for patients to leave without being seen.

We perform steady state mean-value analyses to <sup>fi</sup>nd the bene<sup>fi</sup>t from prioritization because we are interested only in its impact on the long-run performance of the service system.

## 4. Analysis under an exogenous budget

In this section we analyze the problem of minimizing the waiting costs, either $\boldsymbol { W } _ { S } ^ { * }$ or $W _ { P } ,$ given an exogenous budget K which is used for processors and possibly sorters. We <sup>fi</sup>rst consider how to transform the waiting times into waiting costs for the base system and the prioritized system. We de<sup>fi</sup>ne the system time for any step as the sum of time in queue and service time for that step. Then the waiting cost under prioritization is given by

$$
\begin{array}{l} W _ {s} = (\text { system   time   for   sorting }) * (\lambda q _ {u} c _ {u} + \lambda q _ {n} c _ {n}) \\ \quad + (\text { urgents } ^ {\prime} \text { system   time   for   processing }) * (\lambda q _ {u} c _ {u}) \\ \quad + (\text { non - urgents } ^ {\prime} \text { system   time   for   processing }) * (\lambda q _ {n} c _ {n}), \end{array}\tag{2}
$$

and the waiting cost for the base system is given by

$$
W _ {P} = (\text { system   time   for   processing }) * (\lambda q _ {u} c _ {u} + \lambda q _ {n} c _ {n}).\tag{3}
$$

In Eq. (2) multiplying the system time for a step by the appropriate arrival rate of jobs in a particular class gives the total number of jobs at that step (by Little's Law [6]). When this is multiplied by the waiting cost for a job, we obtain the total waiting cost of a job class at that step. So the <sup>fi</sup>rst term in Eq. (2) gives the total cost experienced by urgents and non-urgents at the sorting step. Note that the average system time for sorting is the same for both urgents and non-urgents because of an FCFS queuing discipline. Similarly, the second and third terms give the total cost experienced by urgents and non-urgents, respectively, at the processing step. Note that the system times for processing step for urgents and non-urgents are different because of prioritization. Similarly, the total waiting cost of urgents and nonurgents in the base system is given by Eq. (3). For this analysis we use an approximation from [17] to represent the waiting time in queue for each piece of the system and derive an approximation to handle the case of prioritization.

Theorem 1. For the prioritized system, the system time for sorting, the urgents' system time for processing, the non-urgents' system time for processing, and, for the base system, the system time for processing are given by

$$
\frac {1}{\lambda} \frac {\rho^ {\sqrt {2 (g + 1)}}}{1 - \rho} + \frac {1}{\mu_ {S}},\tag{4}
$$

$$
\frac {1}{\lambda} \frac {(\rho_ {u} + \rho_ {n}) ^ {\sqrt {2 (f + 1)}}}{1 - \rho_ {u}} + \frac {1}{\mu_ {p}},\tag{5}
$$

$$
\frac {1}{\lambda} \frac {(\rho_ {u} + \rho_ {n}) ^ {\sqrt {2 (f + 1)}}}{(1 - \rho_ {u}) (1 - \rho_ {u} - \rho_ {n})} + \frac {1}{\mu_ {p}},\tag{6}
$$

$$
\frac {1}{\lambda} \frac {\rho_ {P} ^ {\sqrt {2 (\widetilde {f} + 1)}}}{1 - \rho_ {P}} + \frac {1}{\mu_ {P} ^ {\prime}},\tag{7}
$$

respectively, where ρ<sub>P</sub> $I = \lambda / ( \widetilde { f } \mu _ { P } ^ { \prime } ) I$ and $\widetilde { \boldsymbol { \mathrm { f } } } \equiv \boldsymbol { \mathrm { K } } / K _ { P }$ is the number of processors in the base system.

Because we assume that the number of processors is continuous, in the base system, it is trivial that the entire budget is spent on the processors, so the number of processors equals f . In the prioritized system, the allocation of the budget that is spent on sorters vs. processors is determined by optimizing the waiting cost W . This optimization problem is formulated in Theorem 2.

Theorem 2. The optimal waiting cost under prioritization is given by

$$
W _ {S} ^ {*} = \text { Minimize } \left\{ \begin{array}{l} (q _ {u} c _ {u} + q _ {n} c _ {n}) \cdot \left(\frac {\rho^ {\sqrt {2 (g + 1)}}}{1 - \rho}\right) + \frac {\lambda q _ {u} c _ {u} + \lambda q _ {n} c _ {n}}{\mu_ {S}} \\ + q _ {u} c _ {u} \cdot \left(\frac {(\rho_ {u} + \rho_ {n}) ^ {\sqrt {2 (f + 1)}}}{1 - \rho_ {u}} + \frac {\lambda}{\mu_ {P}}\right) \\ + q _ {n} c _ {n} \cdot \left(\frac {(\rho_ {u} + \rho_ {n}) ^ {\sqrt {2 (f + 1)}}}{(1 - \rho_ {u}) (1 - \rho_ {u} - \rho_ {n})} + \frac {\lambda}{\mu_ {P}}\right) \end{array} \right\}
$$

$$
s. t. \quad \rho_ {u} = \frac {\lambda q _ {u}}{f \mu_ {P}},\tag{8}
$$

$$
\rho_ {n} = \frac {\lambda q _ {n}}{f \mu_ {P}},\tag{9}
$$

$$
\rho = \frac {\lambda}{g \mu_ {S}},\tag{10}
$$

$$
\rho_ {u} + \rho_ {n} <   1,\tag{11}
$$

$$
\rho <   1,\tag{12}
$$

$$
f K _ {P} + g K _ {S} \leq K,\tag{13}
$$

$$
f, g > 0.\tag{14}
$$

If the optimization problem in Theorem 2 is feasible, i.e., the budget is suf<sup>fi</sup>cient, it has a unique solution that splits the entire budget between sorters and processors.

![](/api/attachments/7RMRJFM4/fulltext/images/94d260be1958d8596c2b972cf95617b0e43919a32278258881e0c8b7c8ceb2ee.jpg)  
Fig. 2. Variation of the waiting cost difference $W _ { S } ^ { * } - W _ { P }$ with the cost ratio when $q _ { u } = 0 . 5$

After characterizing the optimal waiting costs for the base system and the prioritized system, we compare them varying two key parameters, the fraction of urgents $q _ { u }$ and the cost ratio r. The cost ratio, $r ,$ is a measure of the need for quick service for urgent jobs compared to non-urgent jobs. We focus on varying these two parameters, which represent how demand might vary by location.

Before we analyze the results from our numerical analysis, we examine a key tradeoff. On the one hand, prioritization might decrease the waiting cost because of queuing effects and because μ<sub>P</sub>≥μ′(from Eq. (1)). On the other hand, the base system might have a lower waiting cost because it spends the entire budget on processors and because customers do not have to spend any time in sorting. Therefore, which of these two systems performs better, i.e., has lower waiting costs, depends on the impact of these tradeoffs that in turn depends on the $( q _ { u } , r )$ parametric combination.

To demonstrate our numerical analysis, we assume the following values for these parameters unless otherwise mentioned: $\lambda { = } 1 5 / \mathrm { h }$ μ<sub>S</sub>= 20/h, μ<sub>P</sub>= 3/h, $K _ { P } = \$ 80 / \mathrm { h }$ and $c _ { n } = \$ 12 / \mathrm { h }$ , α=0.25. We assume that the budget is 10% over the minimum budget at which both the service system under prioritization and the base system are stable. Mathematically, this translates to

$$
K = 1. 1 \cdot \min \left(\frac {\lambda K _ {S}}{\mu_ {S}} + \frac {\lambda K _ {P}}{\mu_ {P}}, \frac {\lambda K _ {P}}{\mu_ {P} ^ {\prime}}\right).
$$

All these values of the parameters closely correspond to those of an emergency department the authors are familiar with. We have done extensive numerical tests with other values and the qualitative conclusions are similar to the ones presented here with this example. So, for the sake of conciseness, we present only this example.

We vary the fraction of urgents, $q _ { u } ,$ from 0 to 1 and the cost ratio r from 1 to 15 in order to compare the difference in waiting cost, $W _ { S } ^ { * } - W _ { P } ,$ which measures how much the waiting cost would increase by changing from the base system to the prioritized system. Fig. 2 shows these cost differences when $q _ { u }$ is <sup>fi</sup>xed at 0.5 and r is varied. It shows that the difference is strictly decreasing in r and that there is a small threshold cost ratio below which the base system is better and above which prioritization is better. As the cost ratio increases, an urgent job needs a much quicker service and hence it bene<sup>fi</sup>ts more from prioritization thereby making the prioritized system better. Fig. 3 separates the waiting cost difference into two components: the waiting cost difference from the sorting step (note that in the base system, since there is no sorting, waiting cost from the sorting step is just zero; so this difference would just be equal to waiting cost in the prioritized system) and the waiting cost difference from the processing step. Fig. 3 shows that the two cost differences have opposite effects and are increasing in magnitude as the cost ratio increases; the <sup>fi</sup>rst is positive because sorting is done only in prioritized system and the second is generally negative because prioritization decreases the waiting cost for the processing step (note that this happens despite fewer processors being available due to budget constraint). It also shows that, as the cost ratio increases, the bene<sup>fi</sup>t from processing outweighs the cost from sorting thereby making the prioritized system better.

![](/api/attachments/7RMRJFM4/fulltext/images/ab0e783a60c88e68daf54120ced8cc7634fa452c2dc9e7ad5387ca733737de6c.jpg)  
Fig. 3. Variation of the waiting cost differences from sorting and processing with the cost ratio when $q _ { u } = 0 . 5$

Figs. 4 and 5 show the corresponding plots when r is <sup>fi</sup>xed at 3 and $q _ { u }$ is varied. Fig. 4 has a U-shaped curve and it shows that for low or high values of $q _ { u } ,$ the base system performs better while for an intermediate range of values, prioritization is better. Fig. 5 shows that while the cost difference from sorting keeps increasing in magnitude because the cost from making the jobs wait for sorting increases as the proportion of urgent jobs increases, the bene<sup>fi</sup>t from processing initially increases and then decreases because prioritization is less valuable when either class of jobs, urgent or non-urgent, constitutes a signi<sup>fi</sup>cant fraction. We also <sup>fi</sup>nd that (plots omitted for the sake of conciseness) when $q _ { u }$ is very low or very high, and thus there is little need for prioritization, the base system does better for all the values of r from 1 to 15.

## 5. Analysis under total cost minimization

We de<sup>fi</sup>ne total cost as the sum of waiting cost and budget. We can then formulate the total cost minimization problem under prioritization as

$$
\underset {K > \frac {\lambda K _ {S}}{\mu_ {S}} + \frac {\lambda K _ {P}}{\mu_ {P}}} {\text { Minimize }} K + W _ {S} ^ {*} (K),\tag{15}
$$

and for the base system as

$$
\underset {K > \frac {\lambda K _ {P}}{\mu_ {P}}} {\text { Minimize }}   K + W _ {P} (K),\tag{16}
$$

in which the lower bounds on the budget K ensure a stable service system in both cases.

Solving the optimization problems in Eqs. (15) and (16) gives the optimal total costs under the base system and prioritization. Before we analyze the results from our numerical analysis, we examine two key tradeoffs that are important in these optimization problems. The <sup>fi</sup>rst involves the tradeoff between budget and waiting costs both under the base system and under prioritization. As the budget increases, more sorters and processors are employed and hence waiting cost decreases. So any increase in the budget beyond the optimal amount results in smaller decrease in waiting costs thereby increasing the total costs. The second tradeoff involves whether prioritization would result in a lower waiting cost for a given budget K (we analyzed this problem in Section 4). Therefore which of these two systems performs better, i.e., has lower total costs, again depends on the impact of these tradeoffs that in turn depends on the $( q _ { u } , ~ r )$ parametric combination, in addition to other parametric values for which we use the same values as we did in Section 4. $\mathsf { A g a i n } ,$ note that, though a change in any of these parameters might change which system is preferred for a particular $( q _ { u } , r )$ combination, the qualitative insights do not change.

![](/api/attachments/7RMRJFM4/fulltext/images/eba082c9fcff2735f3c7e30b22f814e3b82e8542ed241e21fdf4ce5bb0d888f3.jpg)  
Fig. 4. Variation of the waiting cost difference $W _ { S } ^ { * } - W _ { P }$ with the fraction of urgents when r=3.

Fig. 6 shows how the total cost difference varies with the cost ratio, r, when $q _ { u }$ is <sup>fi</sup>xed at 0.5. Unlike, in Fig. 3, where we found a single threshold cost ratio, here we <sup>fi</sup>nd that both for small and large cost ratios the base system is better while for intermediate cost ratios prioritization is better. The reason for this disparity becomes clear when we consider the results from Fig. 7. Here, we have split the total cost difference into three components; the cost differences from sorting and processing steps (as in Section 4), and the budget difference. As in Section 4, the sorting cost difference is positive because sorting is done only in the prioritized system and the processing cost difference is generally negative because of the bene<sup>fi</sup>ts from prioritization. Interestingly, the budget difference is also negative which implies that more money is spent on the base system than the prioritized system. This result might seem counterintuitive because the base system has only processors and the prioritized system has both sorters and processors. However, we also need to consider the budget vs. waiting costs tradeoff; additional budget just spent on processors has a higher impact on reducing waiting costs and so more budget is used in the base system. The net effect from all these components determines which system is better. As the cost ratio becomes very high, the sorting cost (which increases almost linearly in r) becomes higher than the bene<sup>fi</sup>ts from budget (which is concave in r) and processing (which is more or less constant in r), thereby making the base system better.

![](/api/attachments/7RMRJFM4/fulltext/images/107a8fd9b21351df4a005af257f505584e3f5b91b037887d9395a11542d0c859.jpg)  
Fig. 5. Variation of the cost differences from sorting and processing with the fraction of urgents when r= 3

![](/api/attachments/7RMRJFM4/fulltext/images/4f317891d62fdded07c55971ab3730bce1ca352854c4e0cbdcdf6f5eff8f628c.jpg)  
Fig. 6. Variation of the total cost difference with the cost ratio when $q _ { u } = 0 . 5 .$

Figs. 8 and 9 are similar except we now vary $q _ { u }$ keeping r <sup>fi</sup>xed at 3. Fig. 8 has a U-shaped curve (similar to Fig. 4); however we now <sup>fi</sup>nd that the base system does better for all values of $q _ { u }$ because the cost difference is always positive. But, in general, we <sup>fi</sup>nd, after analyzing with other numerical combinations, that the results here are similar to the corresponding results in Section 4. There can be two cases; if the cost ratio r is small then the base system does better always (as the numerical example above shows), otherwise the base system does better only for low or high values of $q _ { u } .$ . Next, we extend the model to consider imperfect sorting and analyze its impact on the prioritized system.

![](/api/attachments/7RMRJFM4/fulltext/images/a86749ca5e217ee92c76bae4057d5ebbe438409c54b5b596412081e29cfe08a8.jpg)  
Fig. 7. Variation of the total cost difference components with the cost ratio when $q _ { u } = 0 . 5 .$

![](/api/attachments/7RMRJFM4/fulltext/images/c0f8e9578bc780371d17d1d06a9dfa360646d4fe42ccfed048435a616fa2ec00.jpg)  
Fig. 8. Variation of the total cost difference with the fraction of urgents when $r = 3 .$

## 6. Imperfect sorting

We have earlier assumed that the sorters can perfectly sort the customers into urgent and non-urgent customers. We now brie<sup>fl</sup>y consider what happens if sorting is not perfect. Imperfect sorting occurs in an emergency department when a triage nurse underestimates or overestimates the acuity of a patient's illness and misplaces the patient in the wrong queue. In our model, there can be two possibilities; a sorter can mischaracterize an urgent patient as a non-urgent, and vice versa. Suppose $q _ { u }$ and $q _ { n }$ denote the actual fractions of urgent and non-urgent customers, respectively. Also, let $\delta _ { u }$ and $\delta _ { n }$ be the fractions of customers incorrectly sorted among urgent and non-urgent customers, respectively. The fractions of prioritized and non-prioritized customers after the sorting step are then given by $q _ { u } ^ { \prime } { = } ( 1 - \delta _ { \mathrm { u } } ) q _ { u } + \delta _ { n } q _ { n }$ and $q _ { n } ^ { \prime } = \delta _ { u } q _ { u } + ( 1 - \delta _ { n } ) q _ { n } .$ . Note that $q _ { u } ^ { \prime } + q _ { n } ^ { \prime } =$ $q _ { u } + q _ { n } = 1$ . The waiting cost for any given number of sorters and processors is now given by

$$
\begin{array}{l} W _ {S} = [ q _ {u} c _ {u} + q _ {n} c _ {n} ] \frac {\rho^ {\sqrt {2 (g + 1)}}}{1 - \rho} + \frac {\lambda q _ {u} c _ {u} + \lambda q _ {n} c _ {n}}{\mu_ {S}} \\ \qquad + [ (1 - \delta_ {u}) q _ {u} c _ {u} + \delta_ {n} q _ {n} c _ {n} ] \left[ \frac {(\rho_ {u} + \rho_ {n}) ^ {\sqrt {2 (f + 1)}}}{1 - \rho_ {u} ^ {\prime}} + \frac {\lambda}{\mu_ {P}} \right] \\ \qquad + [ \delta_ {u} q _ {u} c _ {u} + (1 - \delta_ {n}) q _ {n} c _ {n} ] \left[ \frac {(\rho_ {u} + \rho_ {n}) ^ {\sqrt {2 (f + 1)}}}{(1 - \rho_ {u} - \rho_ {n}) (1 - \rho_ {u} ^ {\prime})} + \frac {\lambda}{\mu_ {P}} \right], \end{array}\tag{17}
$$

in which $\rho _ { u } ^ { \prime } { = } \lambda q _ { u } ^ { \prime } / ( f \mu _ { P } )$ is the utilization of the processors by the customers who have been given priority. In Eq. (17), the <sup>fi</sup>rst two terms, which correspond to the waiting costs of patients at the sorting step, do not change due to misplacement. In the processing step, the customers who are classified as urgents will include some of those that are actually urgent as well as some who are non-urgent. The third term takes this aspect into account by <sup>fi</sup>nding the total number of urgent and non-urgent customers per unit time who have been given priority, and aggregating their waiting costs. Note that all the customers in this group, whether they are urgent or non-urgent customers, on average, wait for the same amount of time. Similarly, the fourth term is the total waiting cost of the group of customers that have not been given priority. Note that we use the expression $\rho _ { u } + \rho _ { n }$ in Eq. (17) instead of $\rho _ { u } ^ { \prime } + \rho _ { n } ^ { \prime }$ because $\rho _ { u } ^ { \prime } + \rho _ { n } ^ { \prime } = \rho _ { u } + \rho _ { n } = \lambda / ( f \mu _ { P } )$ Clearly, the total utilization of the processors does not depend on how customers have been sorted in the previous step.

![](/api/attachments/7RMRJFM4/fulltext/images/2e99efc8370d08b36a68f621c08f8159ce51cad70517111c193c433d142e624d.jpg)  
Fig. 9. Variation of the total cost difference components with the fraction of urgents when $r = 3 .$

The waiting cost $\mathsf { W } _ { \mathsf { S } } ,$ , given by Eq. (17), is the average waiting cost actually incurred by customers. To set the number of sorters and processors, we consider the following two scenarios, (i) the service system knows what the values of $\delta _ { u }$ and $\delta _ { n }$ are (some information), and optimizes the waiting cost in Eq. (17) subject to the budget constraint (13) and (ii) the service system does not know the values of $\delta _ { u }$ and $\delta _ { n }$ but it selects the number of sorters and processors based on perfect sorting, $\mathrm { i . e . , }$ , it assumes that q′ and $q _ { n } ^ { \prime }$ are the actual fraction of urgent and non-urgent customers (no information). Theorem 3 shows that, under either of these scenarios, imperfect sorting is worse than perfect sorting for the exogenous budget and the total costs scenarios.

Theorem 3. The waiting cost, $W _ { S } ,$ , given by Eq. (17) is strictly increasing in $\delta _ { u }$ and $\delta _ { n } .$ Further, the optimal waiting cost under the exogenous budget model and the total cost model under perfect sorting are less than those under imperfect sorting in both (i) some information and (ii) no information scenarios.

Theorem 3 shows that the analysis performed in Section 4 and Section 5 present a “best case analysis” of the prioritized system so that any advantage that the prioritized system has over the base system is diminished if there is less than perfect sorting, thus the base system will perform better for more cases. Next, we discuss other extensions to our model.

## 7. Discussion

In our model, the three changes that prioritization brings to the service system are the presence of sorters, priority assignment to the urgent class of customers, and potential faster processors. Below, we consider a few other aspects of the service system that might change under prioritization.

1. Balking/Reneging — Suppose there is some balking or reneging before service provision. On the one hand, there might be less of it under prioritization due to the presence of sorters because customers might decide to stay after receiving some service (from the sorter) early. On the other hand, sorters might themselves encourage some customers (especially among non-urgents) to return later because the current wait may be substantial. For instance, in emergency departments, a triage nurse might ask the patient having cold symptoms and using the ED as his primary care provider to come later, and in call centers customers might be asked to leave their complaint and phone number to receive a “callback” later. So it is not intuitively clear whether prioritization reduces this behavior. However, without getting into the speci<sup>fi</sup>cs of queuing, losing some customers between sorting and processing can be “approximately” modeled by varying λ. So it can be modeled by three “arrival rates”:λ<sup>priority</sup>, the arrival rate to the sorting step under prioritization which accounts for balking before this step;λ<sup>priority</sup>, the arrival rate to the processing stage under prioritization which accounts for losses before this step; andλ<sup>base</sup>, the arrival rate in the base system which accounts for balking in this system. Using these arrival rates, the two systems can again be compared under different cases.

2. The wait experienced before prioritization is “different” from the wait after it — In this case, the waiting cost for the urgents (and maybe even non-urgents) before the sorting step is higher than after it. For instance, in an emergency department, urgent patients (and even some non-urgents) might be under the care of a registered nurse after triage and hence less prone to complications which results in a lower waiting cost. This aspect can be incorporated in our model by considering waiting costs $c _ { u }$ (c<sub>n</sub>) and $c _ { u } ^ { \prime } \bigl ( c _ { n } ^ { \prime } \bigr )$ for urgent (non-urgent) jobs before and after triage respectively. Then $c _ { u } > c _ { n }$ and $c _ { u } ^ { \prime } > c _ { n } ^ { \prime }$ hold because urgents have higher waiting cost than non-urgents. Also, $c _ { u } { > } c _ { u } ^ { \prime }$ and $c _ { n } > c _ { n } ^ { \prime }$ hold because the waiting cost decreases after sorting. Again, the impact of prioritization can be analyzed as before. Further, note that the positive impact from prioritization will be higher than in our original model because sorting now reduces the waiting costs of an urgent and a non-urgent job.

3. Processor's service rates are different for urgent and non-urgent customers — There can be two possibilities here. First, the service rate for urgent customers is higher. Due to the cμ priority rule [6], it is better to give urgents priority over non-urgents. Prioritization might become more preferable compared to our earlier analysis because customers who are given priority now not only have higher waiting costs but also can be processed faster, which results in smaller wait for all customers. The second case is the opposite where urgent customers have a lower service rate. It is no longer obvious that urgent customers must be given priority. Regardless of which customer class is given priority, prioritization becomes less preferable compared to our earlier analysis. If the urgents are given priority, the bene<sup>fi</sup>t from prioritization is tempered because quicker jobs are now being made to wait longer. If the non-urgents are given priority, this bene<sup>fi</sup>t is again diminished because lower waiting cost customers are now given priority. Therefore, our analysis in this case sets an “upper bound” for the bene<sup>fi</sup>ts from prioritization.

4. Separate, dedicated processors — We have assumed in our model that both urgent and non-urgent customers are seen by the same pool of processors. If we have separate, dedicated processors for each customer type, there are several effects that may make this system better or worse than the prioritized system. First, by splitting the processors into separate pools one loses the queuing economies of scale. Second, by optimizing the number of servers between these two pools one could reduce this effect. Third, it may be possible to have the processors now specialize in either urgents or non-urgents and the management could take advantage of either improved processing rates or differences in salary between the two types of specialized processors resulting in reduced processor cost per customer served. Examples are easily generated in which the third effect dominates the loss of economies of scale, i.e., non-urgents can be handled more cheaply by less experienced and less costly staff.

Certainly if this is a feasible scenario one would want to use it rather than the prioritized system in comparing to the base system. Because there is no prioritization, the waiting cost in this scenario would be computed by just using Sakasegawa's approximations [17] for the sorting stage, urgent and non-urgent queues. Thus, such cases can be handled by similar comparisons as we have done in comparing the base and prioritized systems.

5. Deadlines — If customers become impatient and decide to leave without service (patients leave without being seen at an ED, or patients crash waiting to be seen), it would be important to account for these cases in the cost of the system. If we have separate, dedicated processors as in the extension just mentioned, then each piece of the queuing system could be replaced by a model including reneging and a cost for each lost customer could be added to the total cost of the system. A comparison of systems with and without sorting could be done once we determine the parameter for the impatience of the customer and the associated cost for a customer leaving.

## 8. Conclusion

We consider the impact of prioritization of jobs on a service system. Unlike traditional approaches of examining priority that always assume prioritization is free and instantaneous, we realize that it can be both costly and time-consuming. It implies that providing priority does not automatically bene<sup>fi</sup>t system performance. When we consider prioritization, we also account for the potential bene<sup>fi</sup>t from information obtained during “pre-processing” of customers that might be useful and result in work reduction during the actual service. In particular, our model recognizes that the following features play a crucial role in determining the impact of prioritization; the fraction of urgents $q _ { u } ,$ the waiting cost ratio r that is a measure of acuity of the urgent customer over the non-urgent customer, the performance metric that depends on whether the service system is constrained by an exogenous budget or is minimizing the total costs, and the amount of useful information from prioritization parameterized by α.

We <sup>fi</sup>rst consider whether the prioritized system performs better than the base system when the performance metric is the waiting cost that is minimized under an exogenous budget. We compute the waiting cost difference and classify it into two components, the cost difference from sorting and the cost difference from processing. When we vary the cost ratio, we <sup>fi</sup>nd that increasing it always increases the desirability of prioritization because the increase in the sorting cost difference is more than compensated by the increase in the processing cost difference. We also <sup>fi</sup>nd that prioritization is preferable typically for intermediate values of the fraction of urgents (though we note that when the cost ratio is low, the base system might always perform better).

We then consider the optimal total cost to be the performance metric in <sup>fi</sup>nding whether prioritization is better. We now compute the total cost difference that has three components, the cost differences from sorting and processing steps, and the labor cost difference. When we vary the cost ratio, unlike with the earlier performance metric, we <sup>fi</sup>nd that prioritization might be better only for intermediate values of the cost ratio. It results from the budget vs. waiting cost tradeoff that impacts the service system more negatively under prioritization. However, when we vary the fraction of urgents we <sup>fi</sup>nd, as in the earlier case, that prioritization is typically better when the fraction of urgents takes intermediate values.

We also extend our model to consider imperfect sorting by taking into account Type I and Type II errors involved in sorting customers, and <sup>fi</sup>nd that errors in sorting make the prioritized system perform worse than the one with perfect sorting so that the base system would be preferred to the prioritized system with imperfect sorting for a larger set of cases.

## Acknowledgments

We would like to thank Dr Jamie Syrett for helping us better understand the processes in emergency departments. We are grateful to Atanu Lahiri, and members at the HICSS 2010 conference in Kauai, for their valuable comments. Finally, we also thank the anonymous referees and the editorial team for their insightful suggestions that led to an improved version of this paper.

## References

[1] K.R. Balachandran, Queue length dependent priority queues, Management Science 17 (7) (1971).

[2] O. Berman, R.C. Larson, E. Pinker, Scheduling workforce and work<sup>fl</sup>ow in a high volume factory, Management Science 43 (2) (1997).

[3] Boston Globe, At the ER, the stay can reach 8 hours, http://www.boston.com/ yourlife/health/other/articles/2007/03/25/at\_the\_er\_the\_stay\_can\_reach\_8\_ hours/?page=1 (2007).

[4] J.A. Buzacott, D.D. Yao, Flexible manufacturing systems: a review of analytical models, Management Science 32 (7) (1986).

[5] A. Cobham, Priority assignment in waiting line problems, Journal of the Operations Research Society of America 2 (1) (1954).

[6] D.R. Cox, W.L. Smith, Queues, Methuen/Wiley, London, 1961.

[7] S. Dewan, H. Mendelson, User delay costs and internal pricing for a service facility, Management Science 36 (12) (1990).

[8] G. Dobson, A. Sainathan, Are pre-processing and prioritization preferable in service systems? Proceedings of the 43rd Hawaii International Conference on System Sciences (HICSS-43), 2010.

[9] L.V. Green, S. Savin, B. Wang, Managing patient service in a diagnostic medical facility, Operations Research 54 (1) (2006).

[10] S. Hasija, E.J. Pinker, R.A. Shumsky, Staf<sup>fi</sup>ng and routing in a two-tier call centre, International Journal of Operational Research 1 (1) (2005).

[11] C.R. Heathcote, A simple queue with several preemptive priority classes, Operations Research 8 (5) (1960).

[12] N.K. Jaiswal, Preemptive resume priority queue, Operations Research 9 (5) (1961).

[13] G.H. Lewis, A. Srinivasan, E. Subrahmanian, Staf<sup>fi</sup>ng and allocation of workers in an administrative of<sup>fi</sup>ce, Management Science 44 (4) (1998).

[14] H. Mendelson, Pricing computer services: queuing effects, Communications of the ACM 28 (3) (1985).

[15] H. Mendelson, S. Whang, Optimal incentive-compatible priority pricing for the M/M/1 queue, Operations Research 38 (5) (1990).

[16] C.N. Potts, L.N. Van Wassenhove, Integrating scheduling with batching and lotsizing: a review of algorithms and complexity, The Journal of the Operational Research Society 43 (5) (1992).

[17] H. Sakasegawa, An approximation formula l ≅α∙ $\rho ^ { \beta } / ( 1 - \rho )$ , Annals of the Institute of Statistical Mathematics 29 (A) (1977).

[18] A. Seidmann, A. Sundararajan, Competing in information-intensive services: analyzing the impact of task consolidation and employee empowerment, Journal of Management Information Systems 14 (2) (1997).

[19] R.A. Shumsky, E.J. Pinker, Gatekeepers and referrals in services, Management Science 49 (7) (2003).

[20] Strategic Healthcare Communications, Want big rewards? Focus on Customer Service in the Emergency Department, http://www.strategichealthcare.com/pubs/ shcm/f1\_EmergencyDeptCustomerService.php (2005).

[21] Syrett, Jamie. Private correspondence with emergency physicians at a teaching hospital in upstate New York.

![](/api/attachments/7RMRJFM4/fulltext/images/954f57779fa1d2dc81f6fb1365a01f9c1f33408080d0c014882f770ef7bc8d31.jpg)

Gregory Dobson is an Associate Professor of Operations at William E. Simon Graduate School of Business Administration. He holds a B.S. in Operations Research and Industrial Engineering from Cornell and Ph.D. in Operations Research from Stanford. Professor Dobson's current work concentrates on service systems, particularly health care systems, addressing issues of patient <sup>fl</sup>ow, appointment delays, and productivity. His research articles have appeared in Management Science, Marketing Science, Operations Research, Production Planning and Control, and Transportation Research.

![](/api/attachments/7RMRJFM4/fulltext/images/4bf07a35164fd388993c7b78d5cb01608b9f4b5f77244afdecd45dbb4c675693.jpg)

Arvind Sainathan is an Assistant Professor in the Information Technology and Operations Management division of Nanyang Business School. He received his Ph.D. in Operations Management from William E. Simon Graduate School of Business Administration in 2009. Professor Sainathan's research interests are in service management especially pertaining to healthcare operations, and supply chain management in the interface of operations and marketing.
