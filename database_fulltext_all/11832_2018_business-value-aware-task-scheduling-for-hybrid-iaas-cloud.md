---
otero_id: 11832
otero_key: "TAZ9UHMW"
title: "Business value-aware task scheduling for hybrid IaaS cloud"
authors: "Helan Liang; Yanhua Du; Fanzhang Li"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.05.007"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

ELSEVIER Decision Support Systems

Business value-aware task scheduling for hybrid IaaS cloud

Helan Liang, Yanhua Du, Fanzhang Li

![](/api/attachments/TAZ9UHMW/fulltext/images/945c53d2bb63f7374c9fdcf2950c85e2eaab30310061ed1c20a9817443bc52bc.jpg)

PII: S0167-9236(18)30089-7

DOI: doi:10.1016/j.dss.2018.05.007

Reference:

DECSUP 12958

To appear in: Decision Support Systems

Received date: 10 January 2018

Revised date: 31 March 2018

Accepted date: 31 May 2018

Please cite this article as: Helan Liang, Yanhua Du, Fanzhang Li , Business value-aware task scheduling for hybrid IaaS cloud. Decsup (2017), doi:10.1016/j.dss.2018.05.007

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Business Value-Aware Task Scheduling for Hybrid IaaS Cloud

Helan Liang <sup>1</sup>, Yanhua Du <sup>2,</sup> , Fanzhang Li <sup>1</sup> 米

1 School of Computer Science & Technology, Soochow University, Suzhou, China

2 School of Mechanical Engineering, University of Science and Technology Beijing,

Beijing, China

e-mail: hlliang@suda.edu.cn; duyanhua@ustb.edu.cn; lfzh@suda.edu.cn

## Abstract.

Since an Infrastructure as a Service (IaaS) provider has limited resources, it faces the challenge of scheduling tasks to meet the peak demand. For this issue, the task scheduling problem for hybrid cloud from an IaaS provider’s perspective should be properly addressed. However, existing research does not consider either process tasks with slack temporal constraints or the business value from an IaaS provider’s perspective, or it has to specify the type of Virtual Machine (VM) for each task prior. In this paper, we first formalize the problem in which both process tasks with slack temporal constraints and VM type selection optimization are considered, and business value is taken as the objective to comprehensively measure the earned value of an IaaS provider. Second, a novel Evolutionary Algorithm for Task Scheduling in a Hybrid IaaS Cloud (EATSHC) is proposed to solve the problem. Finally, several experiments show our approach performs more effectively and efficiently than existing research.

Keywords. Task scheduling; Business value; Hybrid cloud; Slack temporal constraint; Evolutionary algorithm;

## 1. Introduction

Cloud computing is the most recent emerging paradigm for enabling on-demand access to configurable services [16]. Many enterprises have set up cloud centers that provide various services (e.g., Infrastructure as a Service) using a pay-as-you-go model to the enterprises and cooperative partners in the supply chain. Besides, small or start-up IaaS providers are prosperous on the public cloud, which provide infrastructures in some specific industries or regions. Since this paradigm provides an economical way for both enterprises and service providers, to build complex applications through IaaS cloud has become popular [17, 28-29]. From an IaaS provider’s perspective, peak demand is often received at some business operation periods in enterprises [4], since many enterprises run business analyst at the same time (e.g., the 10th day of a month), and many business processes have to be handled in the selling season. On the other hand, the ever-changing market environment makes peak demand hard to predict [8]. Sudden load spikes take place once new products become popular. whenever new business applications deploy or change, they often need a large number of business operations, which will often lead to peak demand of an IaaS provider.

To deliver promised Quality of Service (QoS), an IaaS provider may subcontract some of its tasks to external clouds when the demand exceeds its resource limitation [26, 30]. Thus, it to challenges to business value-aware task scheduling for hybrid IaaS cloud. Since the earned business value is a critically important goal for an IaaS provider [1, 9], the value (its formal definition can be found in Section 4.1) in this paper focuses on the indicator the overall earned value of an IaaS provider by task scheduling in a hybrid cloud.

In a real business world, an IaaS provider may receive many complex applications that consist of a large number of tasks with dependencies [11]. The definition of task dependency is that a task cannot be executed until its precedence tasks are completed. Besides, to increase the flexibility of execution, slack temporal constraint is often set. According to its definition, not only the desired temporal requirement of the processes but also the penalty for per time slot delay are specified [13]. Furthermore, the type of Virtual Machine (VM) for each task may not be specified [19] (see detail in Section 2). Although many studies [2-3, 6-7, 12-13, 15, 18-20, 21-27, 30] addressed the task scheduling problem and made great contributions, they do not consider either process tasks with slack temporal constraints or the business value from an IaaS provider’s perspective, or have to specify the VM type for each task prior.

In this paper, we first design a formal model of task scheduling for hybrid IaaS cloud, in which both process tasks with slack temporal constraints and VM type selection optimization are considered, and business value is taken as the objective to measure the overall value earned by an IaaS provider. Second, an improved Evolutionary Algorithm for Task Scheduling in a Hybrid IaaS Cloud (EATSHC) is proposed, in which three kinds of strategies are used for making task priorities and a greedy based strategy is used for allocating tasks to resources according to the task priorities. Finally, different test cases show that our approach performs more effectively and efficiently than existing algorithms.

Compared with the existing works, the contributions of this paper are as follows:

(1) Our formal model can describe the task scheduling problem for hybrid IaaS cloud more comprehensively where process tasks with various slack temporal constraints are considered. Besides, the VM type selection optimization is considered, which can provide a more flexible choice for both users and IaaS providers. Furthermore, the business value can measure the earned value of the IaaS provider more precisely.

(2) Our algorithm can use the global information recorded by pheromone and the local cruise search to find a best execution plan, which can achieve better effectiveness and efficiency than existing algorithms.

The rest of this paper is organized as follows. Section 2 introduces a motivation case and problem statement. Section 3 presents related works. Section 4 and Section 5 present the formal model and our approach for the task scheduling problem in a hybrid cloud. Section 6 evaluates the performance. Finally, conclusion is drawn in Section 7.

## 2. Motivation case and problem analysis

In this section, we first give an example to demonstrate the scenario of task scheduling in a hybrid cloud, and then illustrate the problem we address.

## 2.1. Motivation case

A conglomerate of manufacturing has set up a cloud center that is independent in finance and provides infrastructure resources using a pay-as-you-go model to its subsidiaries. As shown in Fig. 1, the IaaS provider denoted as $c p _ { 1 }$ has a number of computers that are pooled to provide virtualized resources including CPU, memory, storage and so on. For simplification, in this paper, we suppose that $c p _ { 1 }$ can offer three types of VMs including Small, Large and Xlarge. As shown in Table 1, each VM type is characterized by CPU number and memory size. Note that the VM types in our approach is extensible, which can be specified according to the resource architecture and management mode of an IaaS provider.

## Table 1

Machine configurations and execution costs of different VM types in $c p _ { 1 }$ .

<table><tr><td>VM type</td><td>Machine configuration</td><td>Execution cost ($/h)</td></tr><tr><td>Small</td><td>1 CPU (2.5GHz); 1.7GB Memory</td><td>0.12</td></tr><tr><td>Large</td><td>4 CPUs (2.5GHz); 7.5GB Memory</td><td>0.34</td></tr><tr><td>Xlarge</td><td>8 CPUs (2.5GHz); 15GB Memory</td><td>0.30</td></tr></table>

![](/api/attachments/TAZ9UHMW/fulltext/images/519ad32af777769a97b49f661a772d0f47f8443a7821c23410ab5b11d339be88.jpg)

![](/api/attachments/TAZ9UHMW/fulltext/images/a9714f75170635396629e743aed296e0abb08b98f4ce5c64dfa77daaa0090ee4.jpg)  
Fig. 1. An example of task scheduling problem we address.

The IaaS provider $c p _ { 1 }$ receives many requests from users every day, some of which are complex applications containing a large number of dependent tasks. For example, a request from a subsidiary in manufacture sector includes quarterly quality analysis of production data process $( P N _ { 1 } )$ and quarterly customer order analysis process (PN ), which is shown in Fig. 1. Take $P N _ { 1 }$ as an example. It contains nine tasks that cover from clean production data $\left( t _ { 1 1 } \right)$ to output quality report $\left( t _ { 1 9 } \right)$ , among which the precedence dependence constraints exist. In this paper, the expected runtimes of each task are obtained through the statistics and analysis of historical data, which is shown in Table 2. To show a more comprehensive scenario that some tasks cannot be executed by some types of VMs or the user may specify the VM type for a task, we randomly denote some runtimes as “n.a.”.

To increase the flexibility of execution, the VM type for each task is not specified by the user, but some budget and slack temporal constraints are given: (1) \$30 is paid if all workflow processes are implemented with overall QoS satisfaction. (2) Tasks from $t _ { 1 4 } \mathrm { t o } t _ { 1 8 }$ are desired to be finished within 22 hours. Otherwise, \$1 is paid as a penalty for per hour delay. (3) Tasks from $t _ { 2 1 } \mathrm { t o } ~ t _ { 2 , 1 0 }$ are desired to be finished within 30 hours. Otherwise, \$0.5 is paid as a penalty for per hour delay.

## Table 2

Expected runtimes of each task by different VM types.

<table><tr><td rowspan="2">Task</td><td colspan="3">Expected runtime (h)</td><td rowspan="2">Task</td><td colspan="3">Expected runtime (h)</td></tr><tr><td>Small</td><td>Large</td><td>Xlarge</td><td>Small</td><td>Large</td><td>Xlarge</td></tr><tr><td> $t_{11}$ </td><td>16</td><td>4</td><td>2</td><td> $t_{21}$ </td><td>28</td><td>7</td><td>4</td></tr><tr><td> $t_{12}$ </td><td>14</td><td>4</td><td>2</td><td> $t_{22}$ </td><td>n.a.</td><td>5</td><td>3</td></tr><tr><td> $t_{13}$ </td><td>n.a.</td><td>5</td><td>3</td><td> $t_{23}$ </td><td>n.a.</td><td>6</td><td>3</td></tr><tr><td> $t_{14}$ </td><td>n.a.</td><td>n.a.</td><td>3</td><td> $t_{24}$ </td><td>12</td><td>3</td><td>2</td></tr><tr><td> $t_{15}$ </td><td>12</td><td>3</td><td>2</td><td> $t_{25}$ </td><td>36</td><td>9</td><td>5</td></tr><tr><td> $t_{16}$ </td><td>24</td><td>6</td><td>3</td><td> $t_{26}$ </td><td>n.a.</td><td>6</td><td>3</td></tr><tr><td> $t_{17}$ </td><td>28</td><td>7</td><td>4</td><td> $t_{27}$ </td><td>n.a.</td><td>n.a.</td><td>5</td></tr><tr><td> $t_{18}$ </td><td>n.a.</td><td>n.a.</td><td>6</td><td> $t_{28}$ </td><td>8</td><td>2</td><td>1</td></tr><tr><td> $t_{19}$ </td><td>40</td><td>10</td><td>5</td><td> $t_{29}$ </td><td>20</td><td>5</td><td>3</td></tr><tr><td></td><td></td><td></td><td></td><td> $t_{2,10}$ </td><td>n.a.</td><td>6</td><td>3</td></tr></table>

However, since many other demands are received by $c p _ { 1 }$ at the same time, most of its resources are occupied and only 8 CPUs and 20GB memory are left, which cannot fulfill the tasks in Table 2 with promised QoS. To maximize its earned business value, $c p _ { 1 }$ will subcontract some tasks to external clouds. As shown in Table 3, a series of external clouds can offer different VM types with various charging prices. Thus, it is necessary to allocate tasks in both $c p _ { 1 }$ and external clouds, which we call task scheduling for hybrid IaaS cloud from an IaaS provider’s perspective.

## Table 3

Charging prices of different VM types in external clouds.

<table><tr><td>External cloud</td><td>Small VM type ($/h)</td><td>Large VM type ($/h)</td><td>Xlarge VM type ($/h)</td></tr><tr><td>A</td><td>0.085</td><td>0.34</td><td>0.68</td></tr><tr><td>B</td><td>0.070</td><td>0.30</td><td>0.70</td></tr><tr><td>C</td><td>0.100</td><td>0.40</td><td>0.72</td></tr></table>

Since the ultimate goal of task scheduling is to maximize the business value earned by $c p _ { 1 }$ both revenue and cost which affect the business value must be considered. For example, suppose that an execution plan is made whose expected duration from $t _ { 1 4 }$ to $t _ { 1 8 }$ is 24h. Since the slack temporal constraint about $t _ { 1 4 } { \sim } t _ { 1 8 }$ is violated whose penalty fee is (24-22)×1=\$2, the provider can receive a revenue 30-2=\$28 from the user. Besides, when using the Small VM type of $c p _ { 1 }$ to implement the task $t _ { 1 1 }$ , the cost is 0.03×16=\$0.48. While if the Xlarge type provided by the IaaS provider C from external clouds is used, the cost will be 0.72×2=\$1.44.

As can be seen from this example, a properly designed strategy is required to meet the peak demand and increase the gained business value of an IaaS cloud. Otherwise, the IaaS provider may spend high execution cost or has to pay high penalties due to temporal violations, which is unacceptable to all stakeholders. In a real business world, many process tasks with slack temporal constraints may be received and the business value varies by allocating tasks to different VM types offered by different clouds, thus the business-aware task scheduling for hybrid IaaS cloud is a challenging problem that needs to be properly addressed.

## 2.2. Problem statement

Based on the motivation case in Section 2.1, the problem in this paper is addressed as follow: Given that (1) an IaaS cloud $c p _ { 1 }$ and a set of external clouds ExCs exist, each of which provides several types of VMs with various costs; (2) the resource pool of $c p _ { 1 }$ is limited; (3) a set of tasks to be scheduled TS is received by $c p _ { 1 }$ , among which dependency relationships and slack temporal constraints may exist, how can we find a best execution plan EP, so as to maximize the business value of the IaaS cloud cp<sub>1</sub>?

## 3. Related works

The related studies can be grouped into four research streams: (1) task scheduling for IaaS cloud without resource limitation [12-13, 19, 23-24]; (2) handling resource limitation of an IaaS cloud [18, 20, 22, 25, 27]; (3) task scheduling for hybrid IaaS cloud from a user’s perspective [2-3, 6-7, 15]; and (4) task scheduling for hybrid IaaS cloud with subcontracting [26, 30]. To make it more clear, a summary table is developed to list the related studies and our study. According to Table 4, besides the categories they belong to, the Parameters column lists the objectives and constraints they consider, the Methodology column describes the methods they use, and the Basic findings column illustrates their contributions.

## Table 4

A summary table about the related studies and our work.

<table><tr><td>Ref.</td><td>Category</td><td>Parameters</td><td>Methodologies</td><td>Basic findings</td></tr><tr><td>[12]</td><td>1</td><td>Max utility, task dependency, price and deadline constraints</td><td>A belief propagation-based method</td><td>The proposed algorithm is efficient with shorter problem solving time and smaller communication requirement.</td></tr><tr><td>[13]</td><td>1</td><td>Min cost, task dependency, slack QoS constraints, service correlations</td><td>Cooperative Coevolution algorithm (DICCC)</td><td>The proposed algorithm can find an execution plan with high effectiveness and efficiency.</td></tr><tr><td>[19]</td><td>1</td><td>Min cost, task dependency, VM types optimization, deadline constraints</td><td>Particle Swarm Optimization (PSO)</td><td>The proposed algorithm shows promising performance in both the total cost and fitness convergence.</td></tr><tr><td>[23]</td><td>1</td><td>Min cost and time, task dependency, VM types optimization, deadline constraints</td><td>Meta-heuristic methods (ACO, GA, PSO)</td><td>They conclude that Ant Colony Optimization (ACO) performances best for the problem they proposed.</td></tr><tr><td>[24]</td><td>1</td><td>Four objectives, task dependency, VM types optimization</td><td>Knee point driven evolutionary algorithm</td><td>The proposed algorithm outperforms existing popular many-objective evolutionary algorithms.</td></tr><tr><td>[18]</td><td>2</td><td>Multi-folded objectives, multi-tier service differentiation, admission control, resource limitation</td><td>Reinforcement learning</td><td>It proposes a coordinated admission control and adaptive resource provisioning approach for multi-tier service differentiation.</td></tr><tr><td>[20]</td><td>2</td><td>Deadline constraint, VM types optimization, federation cloud, resource limitation</td><td>Several scheduling policies</td><td>A new framework for efficiently schedule in cloud federation is presented.</td></tr><tr><td>[22]</td><td>2</td><td>Max profit, QoS constraints, federation cloud, resource limitation</td><td>Several heuristic principles</td><td>The proposed policies enhance the profit and utilization in a Cloud federation environment.</td></tr><tr><td>[25]</td><td>2</td><td>Max revenue, multiple distributed DCs, admission control, resource limitation</td><td>Hybrid algorithm based on PSO and SA</td><td>The proposed algorithm can greatly reduce the total cost and increase the throughput of distributed data centers.</td></tr><tr><td>[27]</td><td>2</td><td>Task dependency, deadline and budget constraints, admission control, resource limitation</td><td>Heuristic method (BHEFT)</td><td>A novel heuristic method is proposed to find a Budget-Deadline Constrained plan for admission control.</td></tr><tr><td>[2]</td><td>3</td><td>Min cost, task dependency, deadline constraints, resource limitation</td><td>Genetic Algorithm</td><td>A novel algorithm with effectiveness and scalability is proposed.</td></tr><tr><td>[3]</td><td>3</td><td>Min cost, task dependency, deadline constraints, resource limitation</td><td>Cooperative Coevolution algorithm (CCGA)</td><td>The proposed method is more effective and efficient than [2].</td></tr><tr><td>[6]</td><td>3</td><td>Min cost, task dependency, VM types optimization, deadline constraints,</td><td>Heuristic method (HCOC)</td><td>The proposed method can reduce costs while achieving the desired execution time.</td></tr></table>

<table><tr><td colspan="6">resource limitation</td></tr><tr><td>[7]</td><td>3</td><td colspan="2">Min cost, deadline constraints, resource limitation</td><td>Greedy scheduling</td><td>The proposed algorithm can schedule a large number of applications within a practical timeframe.</td></tr><tr><td>[15]</td><td>3</td><td colspan="2">Min cost, deadline constraints, resource limitation</td><td>Bonmin, CBC solver</td><td>The paper illustrates how to address the task scheduling for hybrid cloud using optimization technologies.</td></tr><tr><td>[26]</td><td>4</td><td colspan="2">Max profit, deadline constraints, resource limitation</td><td>Meta-heuristic method (SAPSO)</td><td>It can increase the throughput and the profit of an IaaS provider while guaranteeing the service delay bound.</td></tr><tr><td>[30]</td><td>4</td><td colspan="2">Max profit, deadline constraints, resource limitation</td><td>Meta-heuristic method (SLPSO-SA)</td><td>It can increase the profit compared with PSO and CPLCX for problems of nontrivial size under reasonable time.</td></tr><tr><td>Our work</td><td></td><td colspan="2">Max business value, task dependency, slack temporal constraints, VM types optimization, resource limitation</td><td>Meta-heuristic method (EATSHC)</td><td>A comprehensive model is designed and our algorithm can perform more effectively and efficiently than existing research.</td></tr></table>

From Table 4, we can see that the first category cannot deal with task scheduling with limited resources like the rest. Compared with the second and third categories, the fourth category neither causes revenue loss nor requires any formal inter-cloud agreement as the second category does, and it aims at maximizing the business value of an IaaS provider that the third category does not consider. However, the existing research in the fourth category only considers job-based tasks that are independent with each other, and the VM type for each task has to be explicitly specified by users. Thus, in this paper, a more comprehensive approach for the task scheduling problem in a hybrid IaaS cloud which considers process tasks with slack temporal constraints and VM type selection optimization is proposed.

## 4. Formal model of task scheduling for hybrid IaaS cloud

In this section, we fist give Table 5 to explain the symbols used in the rest of this section, and then define some key concepts for the task scheduling for hybrid IaaS cloud. Then, the formal model is addressed in Section 4.2.

## 4.1. Symbol explanations and definitions

## Table 5

Symbol explanations.

<table><tr><td>Parameter</td><td>Explanation</td></tr><tr><td> $x_{ij}^{kv}$ </td><td>Binary variables,  $x_{ij}^{kv}=1$  represents the task  $t_{ij}$  is executed by the vth VM type of the IaaS cloud  $cp_k$ ;</td></tr><tr><td> $st_{ij}$ </td><td>The starting time of the task  $t_{ij}$ ;</td></tr><tr><td> $y_{ijs}$ </td><td>Binary variables,  $y_{ijs}=1$  represents the task  $t_{ij}$  is being executed at the time slot s;</td></tr></table>

VMS<sub>ij</sub> The set of VM types that can implement the task t<sub>ij</sub>. Note that all VM types are considered if no VM types is explicitly specified by users; Otherwise, only the specific VM types are considered; ${ p _ { k } } ^ { \nu }$ Unit processing cost of the vth VM type offered by cp ; $q _ { k , r }$ Unit communication cost between different clouds cp and $c p _ { r }$ . Note that it is assumed to be zero in the same cloud since the internal data transfer is free in most real clouds; $r t _ { i j } ^ { ~ k \nu }$ Expected runtime required to implement the task $t _ { i j } \mathbf { b y }$ using the vth VM type offered by cp<sub>k</sub>; $c t _ { i u , i j }$ Communication time to transfer data between task $t _ { i u }$ and $t _ { i j } ;$ $c p u _ { \nu }$ Number of CPUs for the vth VM type offered by $c p _ { 1 } ;$ mem<sub>v</sub> Memory size for the vth VM type offered by $c p _ { 1 } ;$ total\_ ${ _ { - } } c p u$ Maximum number of CPUs in $c p _ { 1 } ;$ total\_mem Maximum memory size in cp<sub>1</sub>;

$C P S { = } c p _ { 1 }$ ∪ExCs, $c p _ { 1 }$ refers to an IaaS cloud and $E x C s { = } \{ c p _ { 2 } { , } ~ . . . , c p _ { n } \}$ is a set of external clouds to which $c p _ { 1 }$ may subcontract some of its tasks. Each cloud provides a set of VM types characterized by machine configurations and charging costs.

Definition 2 (Tasks to Be Scheduled): A set of tasks to be scheduled is expressed as $T S { = } \{ T _ { 1 } , \cdots , T _ { N } \}$ , where $T _ { i } = \{ t _ { i 1 } , \cdots , t _ { i , n _ { i } } \}$ is a set of transitions belonging to a workflow process PN modeled by Petri net [10-11].

Definition 3 (Execution Plan): Given a hybrid IaaS cloud $C P S { = } c p _ { 1 }$ ∪ExCs and a set of tasks to be scheduled TS, an execution plan is defined as $E P { = } \{ < t _ { i j } , c p _ { k } , \nu m _ { k } ^ { \nu } , s t _ { i j } > \mid t _ { i j } { \in } T S , c p _ { k } { \in }$ CPS} where each task $t _ { i j }$ is allocated to an instance of the VM type $\nu m _ { k } ^ { \nu }$ offered by the IaaS cloud $c p _ { k } .$ , and $s t _ { i j }$ is the starting time of $t _ { i j } .$ .

Definition 4 (Slack Temporal Constraints): A set of slack temporal constraints is defined as $S T C S { = } \{ s t c _ { 1 } , . . . , s t c _ { n } \}$ , each of which is defined as $s t c _ { i } \mathrm { { = } } { < t } , t ^ { \prime } , d _ { i } , a _ { i } >$ . If the difference between the finishing time of the task $t '$ and the starting time of the task t is less than the desired temporal requirement $d _ { i } ,$ the temporal constraint is strictly satisfied. Otherwise, a penalty $a _ { i }$ has to be paid by the IaaS provider for per time slot delay.

Definition 5 (Business Value): The business value BS is an indicator to measure the earned value of the IaaS provider $c p _ { 1 }$ <sub>1</sub>. It is calculated by BS=Revenue-Cost where Revenue is the value acquired from users and Cost is the value needed for operating all the tasks by its own resources and external clouds.

In a broad sense, business value of task scheduling can be considered as a set of indicators to evaluate the impacts of task scheduling on an IaaS provider’s performance. Usually, it is decided by many factors (e.g., monetary, social and environmental) $[ 1 , 9 ] .$ . For simplicity, in this paper, we only consider the revenue and cost that are two important indicators from the monetary perspective. Note that our approach can be extended to the other parameters. Here, we give detail descriptions of Revenue and Cost as follows:

Definition 6 (Revenue): Given the budget b and a set of slack temporal constraints $ S T C S { = } \{ \ldots , < t , \ t ^ { \prime } , \ d _ { i } , \ a _ { i } { > } , \ \ldots \}$ , the revenue is calculated by Eq. (1), in which Revenue is reduced from b if some constraints in STCS are not strictly satisfied.

$$
\text { Re   venue } = b - \sum_ {s t c _ {i} \in S T C S} \max \{(f _ {i} - d _ {i}) \cdot \alpha_ {i}, 0 \}\tag{1}
$$

where b, d<sub>i</sub> and $a _ { i }$ are explicitly specified by users. Once an execution plan is obtained, we can obtain the actual finishing time f<sub>i</sub> and calculate the revenue by Eq. (1).

Definition 7 (Cost): Given the tasks to be scheduled TS and a hybrid IaaS cloud $C P S { = } c p _ { 1 } \cup$ ExCs, the total cost is calculated by Eq. (2), which includes the processing costs by using resources in the hybrid cloud, and the communication costs for transferring data between adjacent tasks:

$$
\operatorname{Cos} t = \sum_ {t _ {i j} \in T S; c p _ {k} \in C P S; v m _ {k} ^ {v} \in V M S _ {i j}} x _ {i j} ^ {k v} \cdot p _ {k} ^ {v} \cdot r t _ {i j} ^ {k v} + \sum_ {t _ {i u} \rightarrow t _ {i j}; v m _ {r} ^ {w} \in V M S _ {i u}, v m _ {k} ^ {v} \in V M S _ {i j}} x _ {i u} ^ {r w} \cdot x _ {i j} ^ {k v} \cdot q _ {k, r} \cdot c t _ {i u, i j}\tag{2}
$$

The symbols are in Table 5. Since ${ p _ { k } } ^ { \nu }$ and $q _ { k , i }$ <sub>r</sub> are explicitly specified by IaaS providers, we can obtain ${ x _ { i u } } ^ { r w } , { x _ { i j } } ^ { k \nu } , r t _ { i j } ^ { k \nu }$ and $c t _ { i u , i j }$ to calculate the cost once an execution plan is made.

## 4.2. Formal model definition

To sum up, the task scheduling for hybrid IaaS cloud is formulized as follows:

$$
M a x \quad B S = \text { Revenue } - C o s t\tag{3}
$$

$$
s t _ {i j} \geq \max \left\{s t _ {i u} + r t _ {i u} ^ {k v} + c t _ {i u, i j} \right\}, \quad \forall t _ {i u} \rightarrow t _ {i j}; x _ {i u} ^ {k v} = 1\tag{4}
$$

$$
S T C S = \{\dots , <   t, t ^ {\prime}, d _ {i}, \alpha_ {i} >, \dots \}, \quad \forall t, t ^ {\prime} \in T S\tag{5}
$$

$$
\sum_ {c p _ {k} \in C P S; v m _ {k} ^ {v} \in V M S _ {i j}} x _ {i j} ^ {k v} = 1, \quad \forall t _ {i j} \in T S\tag{6}
$$

$$
\sum_ {t _ {i j} \in T S; v m _ {1} ^ {v} \in V M S _ {i j}} \sum_ {x _ {i j} ^ {1 v} \cdot y _ {i j s} \cdot c p u _ {v} \leq t o t a l \_ c p u,} \forall s = 1, 2, \dots , \infty\tag{7}
$$

$$
\sum_ {t _ {i j} \in T S; v m _ {1} ^ {v} \in V M S _ {i j}} \sum_ {x _ {i j} ^ {1 v} \cdot y _ {i j s} \cdot m e m _ {v} \leq t o t a l \_ m e m,} \quad \forall s = 1, 2, \dots , \infty\tag{8}
$$

$$
x _ {i j} ^ {k v} \in \{0, 1 \}, \quad \forall t _ {i j} \in T S; c p _ {k} \in C P S; v m _ {k} ^ {v} \in V M S _ {i j}\tag{9}
$$

$$
y _ {i j s} = \left\{ \begin{array}{l l} 1, & \text { if } s \in [ s t _ {i j}, s t _ {i j} + r t _ {i j} ^ {k v} ] \\ 0, & \text { otherwise } \end{array} \right.\tag{10}
$$

The symbols are in Table 5, where x<sub>ij</sub><sup>k</sup> and $s t _ { i j }$ are decision variables to answer which VM type of which cloud is used and when it is triggered for each task. Objective (3) aims at maximizing the business value of $c p _ { 1 }$ . Constraint (4) defines that each task cannot start before its preceding tasks are completed. Constraint (5) defines the set of slack temporal constraints. Constraint (6) guarantees that each task is allocated to one instance of a VM type. Constraints (7) and (8) describe the resource limitations of $c p _ { 1 }$

Compared with existing research, in this paper, a more comprehensive model for the task scheduling problem in a hybrid IaaS cloud is proposed from three aspects:

(1) Our model can adapt to process tasks with slack temporal constraints. Considering that an independent task is a special kind of workflow process with one task, our model can also be suitable for job-based task scheduling. Besides, as a special case of slack temporal constraints, the model can also cover strict deadline requirements.

(2) VM type selection optimization is considered, so that the scheduler can provide a more flexible choice for both users and IaaS providers. Besides, as a special case, the model can also cover the scenario that the VM type for each task is specified.

(3) Our business value can measure the earned value of the IaaS provider more precisely, because it considers not only the budget and resource costs but also the temporal penalties and communication costs that widely exist in a real business world.

Note that the formal model we proposed is not linear. On one hand, Eq. (2) that is a part of the objective function cannot be linearized since the products of some decision variables $x _ { i j } ^ { \ k \nu }$ and ${ x _ { i u } } ^ { r w }$ exist. On the other hand, the constraint inequalities Eq. (7) and Eq. (8) cannot be linearized since the products of $x _ { i j } ^ { \ k \nu }$ and $y _ { i j s } { \mathrm { ~ e x i s t } }$ in which $y _ { i j s }$ is an unknown variable whose value is obtained only when the decision variables $x _ { i j } ^ { \ k \nu }$ and $s t _ { i j }$ are known. Furthermore, the problem cannot be solved within a closed solution (e.g., by using simplex algorithm), thus it is necessary to propose a new algorithm for the problem we address.

## 5. EATSHC approach for task scheduling in a hybrid IaaS cloud

To solve task scheduling problems, one common method is to make the priority of each task and allocate tasks to resources according to their priorities. In this paper, we propose three kinds of strategies for making task priorities (Algorithm 1\~3 in Section 5.1), and a greedy based strategy for allocating tasks to suitable VM resources (Algorithm 4 in Section 5.2). The flowchart of our EATSHC approach is shown in Fig. 2.

![](/api/attachments/TAZ9UHMW/fulltext/images/b7788290663998dbe5839bd4b74e48a7eeea2b0e91b31f80e040571ea1042b82.jpg)  
Fig. 2. Flowchart of our EATSHC approach.

## 5.1. Deciding task priorities

## 5.1.1. Encoding

Many evolutionary algorithms operate on a population of individuals each of which represents a possible solution to the optimization problem [2, 13]. In this paper, we use the term “solution individual” to avoid confusion, which represents a solution of the priorities of tasks to occupy resources. Take the task scheduling problem in Section 2.1 as an example. One solution individual is shown in Fig. 3, in which tasks belonging to the same workflow process are filled with the same color.

<table><tr><td> $t_{11}$ </td><td> $t_{12}$ </td><td> $t_{13}$ </td><td> $t_{14}$ </td><td> $t_{21}$ </td><td> $t_{15}$ </td><td> $t_{22}$ </td><td> $t_{16}$ </td><td> $t_{17}$ </td><td> $t_{18}$ </td><td> $t_{23}$ </td><td> $t_{24}$ </td><td> $t_{25}$ </td><td> $t_{19}$ </td><td> $t_{26}$ </td><td> $t_{27}$ </td><td> $t_{28}$ </td><td> $t_{29}$ </td><td> $t_{2,10}$ </td></tr></table>

Fig. 3. Encoding of task priorities for our approach.

A valid solution individual has to satisfy that: (1) each task gets a unique priority, so that each task can only be scheduled for one time; (2) each task gets a lower priority than its preceding tasks, since each task cannot be scheduled if the finishing time of its preceding tasks is not known.

## 5.1.2. Random based strategy for deciding task priorities

In the initial phase, seldom knowledge about good solutions is obtained. Thus, a random based strategy is proposed, which is shown in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: Random based strategy for deciding task priorities
Input: Tasks to be scheduled TS.
Output: An initial solution individual ind_s.
Step 1: Put the starting task of each workflow process into ASet. Initialize k = 1.
Step 2: Randomly select a task  $t_{ij}$  ( $t_{ij} \in TS$ ) from ASet and let  $ind\_s[k] = t_{ij}$ .
Step 3: Update ASet = ASet - { $t_{ij}$ }. If  $t_{ij}$  is not an ending task, let ASet = ASet + {the successors of  $t_{ij}$ }. If ASet ≠ Φ, let k = k + 1 and go to Step 2. Otherwise, output ind_s and end the algorithm.
</div>

Here, we take the task scheduling problem in Section 2.1 as an example. As shown in Fig. 4, first, the starting tasks of $P N _ { 1 }$ and $P N _ { 2 }$ are put into ASet, so as to initialize $A S e t { = } \{ t _ { 1 1 } , t _ { 2 1 } \}$ Suppose that $t _ { 1 1 }$ is selected from ASet, so that ind $s [ 1 ] { = } t _ { 1 1 }$ . Since $t _ { 1 2 }$ and $t _ { 1 3 }$ are successors of $t _ { 1 1 } ,$ ASet is updated as $A S e t { = } \{ t _ { 2 1 } , t _ { 1 2 } , t _ { 1 3 } \}$ . Repeat Step 2 and Step 3, so as to obtain a solution individual $i n d \_ s$ that contains all the tasks.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1: initialize ASet; $ASet=\{t_{11}, t_{21}\}$; Step 3: update ASet;  
Step 2: select randomly from ASet; $ASet=\{t_{11}, t_{21}, t_{12}, t_{13}\}$;  
ind_s: $t_{11}$ $t_{13}$ $t_{12}$ $t_{14}$ $t_{21}$ $t_{15}$ $t_{22}$ $t_{16}$ $t_{17}$ ...
</div>

Fig. 4. An example of generating an initial solution individual by Algorithm 1.

Theorem 1. Each solution individual generated by Algorithm 1 is valid, which satisfies that: (1) each task gets a unique priority; (2) each task gets a lower priority than its preceding tasks. Proof. (1) Once a task is appended to a solution individual, which means it gets a priority, it is deleted from ASet and cannot been appended again. Therefore, each task gets a unique priority. (2) A task can be appended to a solution individual only when it is in ASet, and it can enter ASet only when its preceding tasks have all been appended to the solution individual. Therefore, each task gets a lower priority than its preceding tasks.

## 5.1.3. Pheromone based strategy for deciding task priorities

After a population of initial solution individuals is generated, it goes on to the iteration phase. Considering that the pheromone strategy designed in Ant Colony Optimization (ACO)

can use the global information to obtain good solutions and scale up well [13, 23], in this paper, a pheromone based strategy is proposed in Algorithm 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: Pheromone based strategy for deciding task priorities

Input: Tasks to be scheduled TS.

Output: An updated solution individual ind_u.

Step 1: Put the starting task of each workflow process into ASet. Initialize k = 1.

Step 2: Calculate the global and local information of each task in ASet according to Eq. (11) and Eq. (12). Select a task  $t_{ij}$  ( $t_{ij} \in TS$ ) from ASet according to Eq. (13) and let ind_u[k] =  $t_{ij}$ .

Step 3: Update ASet = ASet - { $t_{ij}$ }. If  $t_{ij}$  is not an ending task, let ASet = ASet + {the successors of  $t_{ij}$ }. If ASet ≠  $\Phi$ , let k = k + 1 and go to Step 2. Otherwise, output ind_u and end the algorithm.
</div>

Similar to Algorithm 1, we use a temporary variable ASet to store the tasks that are ready to be scheduled, so as to generate valid solution individuals. Besides, both variables $a r t _ { i j }$ and $\tau g u _ { i j } ^ { k }$ are designed to record the problem-specific local and global information, so as to improve the searching effectiveness and efficiency.

$$
\tau g u _ {i j} ^ {k} = \max _ {1 \leq u \leq k} \{\tau g _ {i j} ^ {u} \}, \quad \forall t _ {i j} \in A S e t\tag{11}
$$

$$
a r t _ {i j} = \frac {\sum_ {v m _ {k} ^ {v} \in V M S _ {i j}} r t _ {i j} ^ {k v}}{| V M S _ {i j} |}, \quad \forall t _ {i j} \in A S e t\tag{12}
$$

$$
o r d _ {k} = \left\{ \begin{array}{l l} \underset {t _ {i j} \in A S e t} {\arg M a x \{\tau g u _ {i j} ^ {k} \cdot a r t _ {i j} \}}, & i f r \leq p _ {0} \\ R o u (\frac {\tau g u _ {i j} ^ {k} \cdot a r t _ {i j}}{\sum_ {t _ {i j} \in A S e t} \tau g u _ {i j} ^ {k} \cdot a r t _ {i j}}), & o t h e r w i s e \end{array} \right.\tag{13}
$$

where $\tau g _ { i j } ^ { u }$ is the pheromone of allocating the task $t _ { i j }$ to the uth position. $a r t _ { i j }$ is the average runtime of the task $t _ { i j } .$ ord is the task assigned to the kth position. $p _ { 0 }$ is a threshold. $r$ is a decimal chosen randomly in [0, 1]. Rou(·) means the roulette wheel strategy where the probability of selecting each task is directly proportional.

Eq. (11) proposes an indicator $\tau g u _ { i j } ^ { k }$ to provide the global information recorded by the pheromone $\tau g _ { i j } ^ { u } \left( 1 { \leq } u { \leq } k \right)$ . Eq. (12) proposes an indicator $a r t _ { i j }$ to provide the local information that allows the tasks with higher runtimes to occupy higher priorities, so that they will have higher chances to be allocated to cheaper resources. Eq. (13) shows that once a random decimal r is bigger than $p _ { 0 } ,$ , a task with the highest global and local information $\tau g u _ { i j } ^ { k } \cdot a r t _ { i j }$ is selected; otherwise, it is selected by the roulette wheel strategy to increase variety.

Take the task scheduling problem in Section 2.1 as an example. As shown in Fig. 5, ASet is initialized as $A S e t { = } \{ t _ { 1 1 } , t _ { 2 1 } \}$ . According to Eq. (12), we can calculate that $a r t _ { 1 1 } { = } 7 . 3$ and $a r t _ { 2 1 } = 1 3$ . Suppose that $\tau g _ { 1 1 } ^ { 1 } { = } 0 . 4$ and $\tau g _ { 2 1 } ^ { 1 } = 0 . 6$ . According to Eq. (13), once a random decimal is larger than a preset threshold $p _ { 0 } ,$ the task $t _ { 2 1 } ~ \mathrm { w h o s e }$ total preference is larger is selected; otherwise, it is selected by the roulette wheel strategy where $t _ { 1 1 }$ is with a probability (0.4×7.3)/(0.4×7.3+0.6×13)=0.27 while the probability of $t _ { 2 1 }$ is 0.73. Suppose that $t _ { 2 1 }$ is selected, so that ind\_u[ $1 ] { = } t _ { 2 1 }$ . Since $t _ { 2 2 }$ is the successor of $t _ { 2 1 }$ , ASet is updated as $A S e t { = } \{ t _ { 1 1 }$ $t _ { 2 2 } \}$ . Repeat Step 2 and Step 3, thus all the tasks are appended to the solution individual.

![](/api/attachments/TAZ9UHMW/fulltext/images/eb72571fc54b8191f548412dd25d5f2992b8a6032919e6031f3bf5a64e92a8d3.jpg)  
Fig. 5. An example of generating a solution individual by Algorithm 2.

Similarly, we can prove that each solution individual generated by Algorithm 2 is valid. Since the proof is the same as that in Theorem 1, we do not address it again.

## 5.1.4. Local cruise search based strategy for deciding task priorities

To find potential better solutions and avoid local convergence, a neighbor search strategy is proposed for generating neighbors of the best solution individual in each round. Neighbor search is generally implemented by preserving some parts of the original solution individual and rearranging the others. However, this strategy cannot guarantee to generate a valid solution individual that satisfies the precedence relationships among tasks. Therefore, in this paper, a temporary variable temp is defined to record the scheduling priority of workflow processes, and a temporary variable ASet is used for mapping temp to a valid solution individual. In sum, our local cruise search strategy is proposed in Algorithm 3.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3: Local cruise search based strategy for deciding task priorities

Input: Tasks to be scheduled TS; the best individual in the population ind_b.

Output: A neighbor solution individual ind_n.

Step 1: Randomly generate two positions  $m_{1}$  and  $m_{2}$  where  $1 \leq m_{1} \leq m_{2} \leq |TS|$ .

Step 2: Initialize  $atp[p] = \text{the number of tasks in each workflow process } p$ . For  $k = m_{1}$  to  $m_{2}$ , let temp[k] = fp and  $atp[fp] = atp[fp] - 1$ , where fp is the process number of the task ind_b[k]. For k = 1 to  $m_{1} - 1$  and  $k = m_{2} + 1$  to |TS|, randomly select a process number p where  $atp[p] &gt; 0$ , and let temp[k] = p and  $atp[p] = atp[p] - 1$ .

Step 3: Put the starting task of each workflow process into ASet. Initialize k = 1.

Step 4: Randomly select a task  $t_{ij} (t_{ij} \in ASet)$  whose process number equals to temp[k], and let ind_n[k] =  $t_{ij}$ .

Step 5: Update ASet = ASet - { $t_{ij}$ }. If  $t_{ij}$  is not an ending task, let ASet = ASet + {the successors of  $t_{ij}$ }. If ASet ≠ Φ, let k = k + 1 and go to Step 4. Otherwise, output ind_n and end the algorithm.

We still take Section 2.1 as an example. As shown in Fig. 6, suppose that  $m_{1}=3$  and  $m_{2}=6$  are randomly generated, which means the priorities of tasks in the 3rd to 6th positions of ind_b are fixed. Second, since 9 tasks exist in PN₁ and 2 of them are in the fixed positions, there are 9-2=7 tasks left in PN₁. Similarly, 8 tasks are left in PN₂. That means, 7 PN₁ and 8 PN₂ can be randomly appended to the positions 1~2 and 7~19 of the temporary variable temp. Finally, ASet is initialized and we can replace the process numbers by tasks according to both ASet and temp, so as to obtain a new solution individual ind_n.

Step 1: randomly select the fixed positions; ↓m₁ ↓m₂
Step 2: generate temp by reselecting the process numbers; ind_b: t₂₁ t₁₁ t₂₂ t₁₂ t₂₃ t₁₃ t₁₄ t₂₄ t₁₆ ...
Step 3 - 5: replace by tasks according to ASet and temp; ind_n: t₁₁ t₁₂ t₂₁ t₁₃ t₂₂ t₁₄ t₂₃ t₁₅ t₁₆ ...
</div>

![](/api/attachments/TAZ9UHMW/fulltext/images/131ebb5b0a6eed13581161e4d0278275856a20cd1187ab669ff7b9da29c9104a.jpg)  
Fig. 6. An example of generating a solution individual by Algorithm 3.

To ensure each solution individual generated by Algorithm 3 is valid, Theorem 2 is derived: Theorem 2. Each solution individual generated by Algorithm 3 satisfies that: (1) each task gets a unique priority; (2) each task gets a lower priority than its preceding tasks.

Proof. (1) Suppose that  temp[p]= ${ \cdot } P N _ { k }$ (1≤p≤|TS| and 1≤k≤m where m is the total number of workflow processes) and no tasks in ASet belongs to the workflow process $P N _ { k } ,$ so that ind\_n[p]=null. However, according to Algorithm 3, the first task of $P N _ { k }$ will be initialized in ASet. Once a task belonging to $P N _ { k }$ is selected, its successors will enter ASet. Furthermore, the number of $P N _ { k }$ in temp equals to the number of tasks in $P N _ { k } .$ . Thus, if  temp[p]=PN<sub>k</sub>, in ASet there must be at least one task belonging to $P N _ { k } ,$ which is contradictory with the assumption. Since no positions in ind\_n is null and no tasks can be appended to ind\_n twice which is guaranteed by ASet, we can conclude that each task gets a unique priority. Furthermore, the proof of the assumption (2) is the same as that in Theorem 1, thus it is omitted.

## 5.2. Allocating tasks to resources

Since a solution individual only represents which task should be assigned to resources first, it is necessary to allocating tasks to resources, so as to obtain an execution plan. Considering that a slack temporal constraint always contains several tasks, the decomposition strategy for deriving local constraints from global constraints [21] is used. Therefore, we can calculate the penalty and cost about allocating each task individually, so that each task can be greedily allocated to a resource with maximum business value. In sum, a greedy based strategy is proposed in Algorithm 4.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 4: Greedy based strategy for allocating tasks to resources

Input: Tasks to be scheduled TS; VM types for each task  $VMS_{ij}$ ; hybrid IaaS cloud CPS; local slack temporal constraint of each task LSTCS; a solution individual ind.

Output: An execution plan EP.

Step 1: For p=1 to |TS|, let  $t_{ij}=ind[p]$ . Let maxBS=0, and initialize q=1.

Step 2: Let  $vm_{k}^{v}=VMS_{ij}[q]$  where  $vm_{k}^{v}$  is the vth VM type offered by the provider  $cp_{k}$ . Obtain the runtime  $rt_{ij}^{kv}$  to implement  $t_{ij}$ . Calculate its earliest starting time  $est_{ij}$  by Eq. (4).

Step 3: Calculate the available starting time  $st_{ij}$  to implement  $t_{ij}$ , which satisfies (1)  $st_{ij}\geq est_{ij}$ ; and (2) the available resources of  $cp_{k}$  in any slot  $s\in[st_{ij},st_{ij}+rt_{ij}^{kv}]$  is larger than that required by  $vm_{k}^{v}$ . Calculate the total cost c and penalty p by using  $vm_{k}^{v}$ . If b-p-c≥maxBS, let maxBS=b-p-c and tmp=&lt; $t_{ij}$ ,  $cp_{k}$ ,  $vm_{k}^{v}$ ,  $st_{ij}&gt;$ .

Step 4: If  $q\leq|VMS_{ij}|$ , let q=q+1 and go to Step 2. Otherwise, append tmp to EP.

Step 5: Update the available resources of the cloud  $cp_{k}$  for each slot  $s\in[st_{ij},st_{ij}+rt_{ij}^{kv}]$ . If  $p\leq|TS|$ , let p=p+1 and go to Step 1. Otherwise, output EP and end the algorithm.
</div>

We take the problem in Section 2.1 as an example. As shown in Fig.7, since $t _ { 1 1 }$ is in the first position of the solution individual, it is allocated first. When the Small VM type of $c p _ { 1 }$ whose capacity requirement is 1 CPU and 1.7GB memory is used, $t _ { 1 1 }$ can be implemented during the time slot from 0 to 16, and the cost is $1 6 { \times } 0 . 0 3 { = } \mathbb { 5 } 0 . 4 8 .$ . Since no temporal $p { = } 0 .$ After all clouds are iterated, we find that to implement $t _ { 1 1 }$ by the Small VM type of its own cloud is the best. Thus, the execution plan is updated as $E P = \{ < t _ { 1 1 } , c p _ { 1 } , S m a l l , 0 > \}$ , and the available CPUs and memory size of $c p _ { 1 }$ during the time slot from 0 to 16 is updated as 8-1=7 and 20-1.7=18.3GB.

![](/api/attachments/TAZ9UHMW/fulltext/images/89dc72a1170f0f7b95030f86a36c67feaccdf4b8b517ec35fc9fd146f90f66dd.jpg)  
Fig. 7. An example of allocating tasks to resources.

## 5.3. The procedure of our approach

The whole procedure of our algorithm is shown in Algorithm 5.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 5: Our approach (EATSHC) for task scheduling in a hybrid IaaS cloud

Input: Parameters for the approach such as pop_size, $p_0$, maxGen; tasks to be scheduled TS; VM types for each task VMS$_{ij}$; hybrid IaaS cloud CPS; slack temporal constraints STCS; initial pheromone of each task $\tau g_0$; the number of local cruise search lsNum.

Output: A best execution plan $EP^{gb} = \{&lt;t_{ij}, cp_k, vm_k^v, st_{ij}&gt; | t_{ij} \in TS, cp_k \in CPS\}$.

Step 1: Initialize all parameters, and derive the local constraints LSTCS by the decomposition strategy.

Step 2: A population of initial execution plans $EP\_s_i$ ($i = 1, ..., pop\_size$) is generated as follows: first, each individual ind_s_i is obtained by Algorithm 1. Secondly, ind_s_i is mapped into an execution plan $EP\_s_i$ by Algorithm 4.

Step 3: For $g = 1$ to maxGen, the following procedures are executed:

Step 3.1: A population of improved execution plans $EP\_u_i$ ($i = 1, ..., pop\_size$) is generated as follows: first, each individual ind_u_i is obtained by Algorithm 2. Secondly, ind_u_i is mapped into an execution plan $EP\_u_i$ by Algorithm 4. Finally, if (business value of ind_u_i &gt; business value of ind_s_i), replace ind_s_i by ind_u_i.

Step 3.2: Let ind_b = the individual whose business value is the highest in the population. A group of neighbors $EP\_n_j$ ($j = 1, ..., lsNum$) is generated as follows: first, each individual ind_n_j is obtained by Algorithm 3. Secondly, ind_n_j is mapped into an execution plan $EP\_n_j$ by Algorithm 4. Finally, if (business value of ind_n_j &gt; business value of ind_b), replace ind_b by ind_n_j.

Step 3.3: Record the globally best execution plan $EP^{gb}$ and update the pheromone of the tasks in the $EP^{gb}$ according to $\tau g_{ij}^k = \tau g_{ij}^k + BS(EP^{gb})$, where $BS(EP^{gb})$ is the business value of the $EP^{gb}$.

Step 4: Output the best execution plan $EP$ and end the algorithm.
</div>

Take the problem in Section 2.1 as an example. Parameters of our algorithm are set as follows: pop $s i z e { = } 2 { \times } 1 9 , p _ { 0 } { = } 0 . 7 ,$ , lsNum=5, $\tau g _ { 0 } = 3 0$ and maxGen=50. Due to the stochastic nature of our algorithm, we take one run as an example to describe our method in detail: First, 38 initial execution plans are generated by Algorithm 1 and Algorithm 4. For example, one solution individual that represents the task priorities can be made as ind\_ $s _ { 1 } = \{ t _ { 1 1 } , t _ { 1 3 } , t _ { 1 5 } , t _ { 1 2 }$ t<sub>21</sub>, t<sub>22</sub>, t<sub>24</sub>, t<sub>23</sub>, t<sub>25</sub>, t<sub>26</sub>, t<sub>14</sub>, t<sub>16</sub>, t<sub>17</sub>, t<sub>27</sub>, t<sub>28</sub>, t<sub>29</sub>, t<sub>18</sub>, t<sub>19</sub>, t<sub>2,10</sub>}. And then, each task will be allocated to a VM type provided by one IaaS cloud according to their priorities, so that we can obtain an execution plan $E P _ { 1 }$ whose business value is \$8.36. Next, the iteration phase is run. At each iteration round, 38 updated execution plans are first generated by Algorithm 2 and Algorithm

4 to replace the worse execution plans in the population. Second, Algorithm 3 and Algorithm 4 are executed to search neighbors of the best execution plan. Third, the globally best execution plan is recorded and the pheromones of tasks are updated.

After 50 iteration rounds, a best execution plan whose business value is \$12.66 is output as EP={<t<sub>11</sub>, cp<sub>1</sub>, Small, 0>, <t<sub>21</sub>, cp<sub>1</sub>, Xlarge, 16>, <t<sub>22</sub>, cp<sub>1</sub>, Xlarge, 20>, <t<sub>24</sub>, cp<sub>1</sub>, Xlarge, 23>, <t , cp , Xlarge, 25>, <t , A, Xlarge, 23>, <t , cp , Xlarge, 30> A, Xlarge, 25>, <t<sub>12</sub>, cp<sub>1</sub>, Small, 35>, <t<sub>28</sub>, B, Large, 30>, <t<sub>29</sub>, cp<sub>1</sub>, Large, 35>, <t<sub>2,10</sub>, cp<sub>1</sub>, Large, 40>, <t<sub>13</sub>, cp<sub>1</sub>, Large, 46>, <t<sub>14</sub>, cp<sub>1</sub>, Xlarge, 51>, <t<sub>17</sub>, cp<sub>1</sub>, Large, 54>, <t<sub>16</sub>, cp<sub>1</sub>, Large, 54>, <t<sub>18</sub>, cp<sub>1</sub>, Xlarge, 61>, <t<sub>15</sub>, cp<sub>1</sub>, Small, 67>, <t<sub>19</sub>, cp<sub>1</sub>, Small, 79>}, which means that $t _ { 1 1 }$ is going to be executed by launching an instance of the Small VM type of cp<sub>1</sub>, and $t _ { 2 1 }$ will be executed by launching an instance of the XLarge VM type of $c p _ { 1 }$ at the 16th hour, and so on.

According to the execution plan recommended by our algorithm, on one hand, the IaaS provider cp<sub>1</sub> can make resource reservations for the tasks executed by its own resources, and subcontract the specific tasks to the external clouds A and B. If all workflow processes are implemented correctly, cp<sub>1</sub> can earn \$12.66 from this deal of business.

Compared with existing research works, in this paper, a novel evolutionary algorithm is proposed which can solve the problem we address and obtain better performance:

(1) To adapt to the task scheduling problem we address, three strategies are proposed to decide the task priorities that meet the precedence relationships among tasks, and a greedy strategy is designed to decide the VM type selection based on business value optimization.

(2) To achieve better effectiveness and efficiency, our strategies are designed according to the characters of different phases, where not only the global information recorded by pheromone but also the local cruise search are used to find a best solution.

## 6. Performance evaluation

In order to evaluate our approach in this paper, two sets of experiments are carried out. First, the test problems in [30] are used. Second, since the problems in [30] just consider independent tasks with strict deadline constraints, more experiments that consider the process tasks with slack temporal constraints and VM type selection optimization are used.

## 6.1. Experimental setting

For each experiment, we compare our approach EATSHC with the existing algorithms SLPSO-SA [30] and SAPSO [26]. Here, a short summery is given as follows: (1) [30] defined an integer programming model for the task scheduling problem in a hybrid cloud, and proposed a Self-adaptive Learning Particle Swarm Optimization based Scheduling Approach (SLPSO-SA) where the velocity of each particle is updated by one of the four velocity updating strategies. (2) [26] formalized the task scheduling problem for hybrid cloud with varying prices, and proposed a Simulated Annealing Particle Swarm Optimization algorithm (SAPSO) where each particle updates its position by the Metropolis acceptance criterion.

The reason to choose the above studies is that both SLPSO-SA and SAPSO focus on the task scheduling problem for hybrid cloud with subcontracting, and some problem specific strategies such as solution representation, task priorities are designed to solve the problem. Thus, their models and algorithms are the most nearest to our research. Moreover, both of them use evolutionary algorithms to solve the problem. These algorithms are with high scalability, thus it is possible for us to make modifications and comparisons.

Since the competing algorithms cannot guarantee to generate execution plans that satisfy the tasks dependencies. Besides, neither of them consider VM type selection optimization. To apply them to the problem we address, some modifications have to be made: (1) to guarantee execution plans’ validation, a variable ASet is used and only the tasks in ASet can be assigned to resources at each time. (2) The VM type for each task is randomly selected to make the VM selection decision. Note that both of the competing algorithms base on Particle Swarm Optimization (PSO). The above modifications have not changed their velocity and position updating strategies that play the most important role in effectiveness and efficiency, thus they will not affect the performance evaluation. Besides, for the sake of fairness, the population size of each algorithm is $p o p \_ s i z e { = } 2 { \times } | T S |$ , and the termination criterion is maxGen=1000. Parameters in our algorithm are $p _ { 0 } { = } 0 . 7$ , lsNum=5 and $t g _ { 0 } = \ b$ where b is the budget. Parameters of other algorithms are set according to [30] and [26]. Furthermore, all methods are programmed in C# and run on a PC with 64-bit Intel core i5 CPU and 8GB memory using Windows 7 operation system, so as to make sure that the running environment is not biased. computation time. Two indicators are used to evaluate the performance:

$$
P I _ {k} = \left(\overline {{o b j _ {3}}} - \overline {{o b j _ {k}}}\right) / \overline {{o b j _ {k}}}, \quad k = 1, 2\tag{14}
$$

$$
E I _ {k} = \left(\overline {{c o m t _ {k}}} - \overline {{c o m t _ {3}}}\right) / \overline {{c o m t _ {k}}}, \quad k = 1, 2\tag{15}
$$

where $P I _ { k } , E I _ { k }$ are the effectiveness and efficiency improvement of our approach to the kth algorithm. $o b j _ { k } , \ c o m t _ { k }$ are the average objective value and computation time of the kth algorithm. k=1 represents SLPSO-SA, k=2 is SAPSO and k=3 is our approach.

## 6.2. Performance evaluation by test problems in [30]

[30] defines three test problems with different sizes. In these problems, four IaaS providers {cp<sub>1</sub>, A, B, C} exist in a hybrid cloud, each of which provides three VM types {Small, Large, Xlarge}. The charging prices of the three VM types of $c p _ { 1 }$ are \$0.08, \$0.32, \$0.64 respectively, and those of the external clouds are in Table 3.

On this basis, the description of each problem is in Table 6. Take the third problem that is the most difficult as an example. $c p _ { 1 }$ is resource limited with 512 CPUs and 1024 GB memory. 10 applications each of which composes of a random size of 1\~50 independent tasks are received by $c p _ { 1 }$ and the deadline of each application is a random integer between 1h and 168h. The allocated VM type of each task is randomly selected from the three VM types, and its runtime is a random integer between 1h and its deadline. It needs to decide which task is implemented in which cloud, and the objective is to maximize the profit of $c p _ { 1 }$ that is calculated by the charging prices of tasks minus the operating costs caused by $c p _ { 1 }$ and external clouds.

## Table 6

Description of test problems in [30].

<table><tr><td>Problem</td><td>Applications</td><td>Tasks</td><td>CPUs</td><td>Memory (GB)</td><td>Deadline (h)</td><td>Runtime (h)</td><td>VM types</td></tr><tr><td>No.1</td><td>8</td><td>~[1, 5]</td><td>20</td><td>40</td><td>~[1, 5]</td><td>~[1, deadline]</td><td>~[1, 3]</td></tr><tr><td>No.2</td><td>5</td><td>~[1, 50]</td><td>512</td><td>1024</td><td>~[1, 168]</td><td>~[1, deadline]</td><td>~[1, 3]</td></tr><tr><td>No.3</td><td>10</td><td>~[1, 50]</td><td>512</td><td>1024</td><td>~[1, 168]</td><td>~[1, deadline]</td><td>~[1, 3]</td></tr></table>

We generate 20 instances for each problem, and results of each algorithm are shown in Table 7. According to it, our algorithm obtains the best objective value and consumes least execution time in each problem. Compared with SLPSO-SA and SAPSO, the effectiveness improvement is 0%\~3.84% and 0%\~5.05%, respectively; and the efficiency improvement is 34.05%\~38.18% and 17.27%\~20.57%, respectively.

## Table 7

Comparison of average objective values and computation times for test problems in [30].

<table><tr><td rowspan="2">Problem</td><td colspan="3">Average objective value</td><td colspan="3">Average computation time (s)</td></tr><tr><td>SLPSO-SA</td><td>SAPSO</td><td>EATSHC</td><td>SLPSO-SA</td><td>SAPSO</td><td>EATSHC</td></tr><tr><td>No.1</td><td>3.06</td><td>3.06</td><td>3.06</td><td>9.197</td><td>6.872</td><td>5.685</td></tr><tr><td>No.2</td><td>2585.52</td><td>2565.81</td><td>2664.46</td><td>957.016</td><td>771.851</td><td>613.036</td></tr><tr><td>No.3</td><td>3172.33</td><td>3136.64</td><td>3295.23</td><td>1720.826</td><td>1404.876</td><td>1134.842</td></tr></table>

Thus, we can conclude that our EATSHC algorithm is more effective and efficient than SLPSO-SA and SAPSO for the task scheduling problem for hybrid IaaS cloud considering independent tasks with strict deadline constraints.

## 6.3. Performance evaluation by different test problems

To validate the effectiveness and efficiency of our approach for task scheduling considering process tasks with slack temporal constraints and VM type selection optimization, we apply it to five sets of test problems with different sizes. In the first two sets of experiments, we vary the number of tasks by varying the number of workflow processes received by the IaaS provider $c p _ { 1 }$ and the number of tasks in each workflow process. Besides, in the third and fourth sets of experiments, we vary the number of IaaS providers in a hybrid cloud and the number of VM types offered by each provider, so as to evaluate how the resource size would affect the performance. Furthermore, the fifth set of experiments is designed to evaluate the performance under slack temporal constraints. Parameters of experiments are shown in Table 8, and the objective is to maximize the business value of $c p _ { 1 }$ that is calculated by Eq. (3).

## Table 8

Parameters of experiments.

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Hybrid cloud</td><td>VM types and costs of  $cp_1$  are in Table 1. Charging prices of ExCs are: ~unif[0.05, 0.1] for Small type; ~unif[0.3, 0.5] for Large type; ~unif[0.6, 0.8] for Xlarge type. In test four which needs more VM types, each adds 1 CPU and 1GB memory, and its charging price adds ~unif[0.3, 0.5] based on the previous one.</td></tr><tr><td>Resources of  $cp_1$ </td><td>CPUs=the number of workflow processes×2; Memory size=CPUs×2.</td></tr><tr><td>Tasks to be scheduled</td><td>Several sequence processes with a set of tasks are received.  $rt_{ij}$  is ~unif[1, 20] h. Runtime of each task by a specific VM type= $rt_{ij}$  / CPUs of the VM type.</td></tr><tr><td>Budget</td><td>=∑cost to implement each task by a randomly selected VM type.</td></tr><tr><td>Slack temporal constraints</td><td>Ending time of each task≤∑average runtime of it and its preceding tasks. Otherwise, penalty = penalty rate × budget × temporal deviation.</td></tr></table>

## (1) Test cases with different number of workflow processes

In this set of experiments, the number of workflow processes is from 4 to 13 with an increase of 1. The number of tasks in each process is 10. The number of IaaS providers in the hybrid cloud is 5. The number of VM types offered by each IaaS provider is 3. The penalty rate is uniformly distributed between 0.001 and 0.2. Results are shown in Fig. 8.

![](/api/attachments/TAZ9UHMW/fulltext/images/1007ba6d44d5e0641d960a2b60494e6bf4878af332466f7d58d7afebeffbfe5f.jpg)  
(a) Business values under different number of processes

![](/api/attachments/TAZ9UHMW/fulltext/images/b2fd078cc9e919fa3c55e80dc9774ada8886c034a213fdebdb4829b5c4409632.jpg)  
(b) Computation times under different number of processes  
Fig. 8. Experiment results under different number of workflow processes.

(2) Test cases with different number of tasks in each workflow process

In this set of experiments, the number of tasks in each workflow process is from 5 to 50 with the first test in Section 6.3.2. Results are shown in Fig. 9.

![](/api/attachments/TAZ9UHMW/fulltext/images/38f03dc56dcc532ce1cdc620de4143252fd3d5fb3427abbfaa5070e1968ed49f.jpg)  
(a) Business values under different number of tasks

![](/api/attachments/TAZ9UHMW/fulltext/images/8f253ad796b93fbf1cc9a4f523e0e6e382a4408acb2cd027d9f09de71241f68b.jpg)  
(b) Computation times under different number of tasks  
Fig. 9. Experiment results under different number of tasks in each workflow process.

(3) Test cases with different number of IaaS providers in a hybrid cloud

In this set of experiments, the number of IaaS providers in a hybrid cloud is from 5 to 50 with an increase of 5. The number of workflow processes is 5. Other parameters are set the same as the first test in Section 6.3.2. Results are shown in Fig. 10.

![](/api/attachments/TAZ9UHMW/fulltext/images/63764f29d61e245c8157a6b438948c167729b2d961db61df839b283eaf5e72f5.jpg)

![](/api/attachments/TAZ9UHMW/fulltext/images/e446adde9f55d8c1c305950849383cb16558de19e87a0e623636f92cf33e9ed5.jpg)  
(a) Business values under different number of IaaS providers (b) Computation times under different number of IaaS providers Fig. 10. Experiment results under different number of IaaS providers in hybrid cloud.  
(4) Test cases with different number of VM types offered by each IaaS provider

In this set of experiments, the number of VM types offered by each IaaS provider is from 4 to 13 with an increase of 1. The number of workflow processes is 5. Other parameters are set the same as the first test in Section 6.3.2. Results are shown in Fig. 11.

![](/api/attachments/TAZ9UHMW/fulltext/images/372013db074ca58a8bb2fc17c4c8726d8b402b227d1bda870f6218dd9ea72444.jpg)

![](/api/attachments/TAZ9UHMW/fulltext/images/49c96fc5d7ca1a4a64228b2cece14a80ceccc51e7f3c6376d5fc97c12a5894a9.jpg)  
(a) Business values under different number of VM types (b) Computation times under different number of VM types Fig. 11 Experiment results under different number of VM types offered by each IaaS provider.  
(5) Test cases with different penalty rates of slack temporal constraints

In this set of experiments, the penalty rate of slack temporal constraints is from 0.128 to 0 which decreases twice each time. The number of workflow processes is 5. Other parameters are set the same as the first test in Section 6.3.2. Results are shown in Fig. 12.

![](/api/attachments/TAZ9UHMW/fulltext/images/7ba92305883cc700cf679478dc59444c2eebf28f90564d191286cf74cf93176b.jpg)

![](/api/attachments/TAZ9UHMW/fulltext/images/426d9520e85b85f2e6f2055d18bc3c5b5e645a378c51e300e220420d2b1b86a4.jpg)  
(a) Business values under different penalty rates  
(b) Computation times under different penalty rates  
Fig. 12. Experiment results under different penalty rates of slack temporal constraints.

As shown in Fig. 8\~Fig. 12, our approach can obtain better business value and consume less computation time than SLPSO-SA and SAPSO in each test case. The effectiveness improvement is from 0.61% to 57.14%, and the efficiency improvement is from 20.27% to 56.89%. Thus, we can conclude that our EATSHC algorithm is more effective and efficient than SLPSO-SA and SAPSO for the task scheduling problem in a hybrid IaaS cloud which considers process tasks with slack temporal constraints and VM type selection optimization.

## 7. Conclusion

The mechanism of hybrid IaaS cloud enables an IaaS provider to make use of public clouds when its own resources are fully occupied. In this paper, a more comprehensive formal model for the task scheduling problem for hybrid IaaS cloud is designed. Furthermore, a novel algorithm EATSHC is proposed to solve the problem we address. Finally, we test the algorithm by three experiments in [30] that considers independent tasks with strict deadline constraints and five more sets of experiments with different problem sizes that consider process tasks with slack temporal constraints and VM type selection optimization. Experimental results demonstrate the effectiveness and efficiency of our proposed algorithm. Our approach is suitable for the IaaS providers that face the challenges of task scheduling in complex situations such as limited resources, complex application requests, aperiodic and unstable demands, and changeable external clouds. Once receiving application requests from users, according to our approach the providers can collect the real-time information of their own resources and external clouds, and find a best execution plan. Thus, they can dynamically allocate their own resources and extend their capacities elastically by renting resources in external clouds. In short, our approach can not only decrease the difficulty of task scheduling but also increase the gained business value of IaaS providers. Furthermore, it is helpful to improve the service level and increase the competitiveness of IaaS providers.

In the future, we will further expand the research in the following areas: (1) our approach focus on traditional data centers that consume electricity power. However, many of current cloud providers have migrated to green cloud data centers (GCDC) and adopted renewable energy sources [5]. Since its energy consumption mode is quite different, the calculation of business value become much more complex. Thus, it would be valuable to investigate suitable approaches for such situations. (2) Besides, due to the complexity and uncertainty of business environment, service changes often take place at run-time [14]. The current version of this only focus on task scheduling at build time while it does not consider any execution such as service failures and QoS violations. Thus, how to solve the dynamic task scheduling problem at run-time will be investigated. (3) Moreover, despite generally proving to achieve efficiency, this work uses an iteration-based method for VM type selection optimization. It is time-consuming and may not scale well as the number of VM types increases. Therefore, we plan to investigate how to simplify the method for VM type selection optimization, so as to improve the calculation efficiency.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China under Grant No. 61473035 and Grant No. 51774209.

## References

[1] Ada, S., Sharman, R., Balkundi, P. (2012). Impact of meta-analytic decisions on the

conclusions drawn on the business value of information technology. Decision Support Systems, 54(1), 521-533.

[2] Ai, L., Tang, M., Fidge, C. (2010). QoS-oriented resource allocation and scheduling of multiple composite Web services in a hybrid cloud using a random-key genetic algorithm. Australian Journal of Intelligent Information Processing Systems, 12(1), 29-34.

[3] Ai, L., Tang, M., Fidge, C. (2011). Resource allocation and scheduling of multiple composite Web services in cloud computing using cooperative coevolution genetic algorithm. Neural Information Processing, 7063, 258-267.

[4] Arnott, D., Lizama, F., Song, Y. (2017). Patterns of business intelligence systems use in organizations. Decision Support Systems, 97, 58-68.

[5] Bi, J., Yuan, H., Tan, W., Li, B. (2016). TRS: Temporal Request Scheduling with bounded delay assurance 57-72.

[6] Bittencourt, L., Madeira, E. (2011). HCOC: a cost optimization algorithm for workflow scheduling in hybrid clouds. Journal of Internet Services & Applications, 2, 207-227.

[7] Bossche, R., Vanmechelen, K., Broeckhove, J. (2013). Online cost-efficient scheduling of deadline-constrained workloads on hybrid clouds. Future Generation Computer Systems, 29, 973–985.

[8] Buyya, R., Ranjan, R., Calheiros, R. (2010). InterCloud utility-oriented federation of cloud computing environments for scaling of application services. International

Conference on Algorithms & Architectures for Parallel Processing, 6081, 13-31.

[9] Chen, B., Peng, X., Yu, Y., Zhao, W. (2015). Requirements-driven self-optimization of composite services using feedback control. IEEE Transactions on Services Computing, 8(1), 107-120.

[10] Du, Y., Tan, W., Zhou, M. (2014). Timed compatibility analysis of web service composition: A modular approach based on Petri Nets. IEEE Transactions on Automation Science and Engineering, 11(2), 594-606.

[11] Du, Y., Wang, L., Li, X. (2016). Analyzing degree of parallelism for concurrent timed Workflow processes with shared resources. IEEE Transactions on Engineering management, 99, 1-15.

[12] Kong, Y., Zhang, M., Ye, D. (2017). A belief propagation-based method for task allocation in open and dynamic cloud environments. Knowledge-Based Systems, 115, 123-132.

[13] Liang, H., Du, Y. (2017). Dynamic service selection with QoS constraints and inter-service correlations using cooperative coevolution. Future Generation Computer Systems, 76, 119-135.

[14] Lina, B., Simon, M., Michael, L. (2018). Adaptive composition in dynamic service environments. Future Generation Computer Systems, 80, 215-228.

[15] Malawski, M., Figiela, K., Nabrzyski, J. (2013). Cost minimization for computational applications on hybrid cloud infrastructures. Future Generation Computer Systems, 29, 1786-1794.

[16] Marston, S., Li, Z., Bandyopadhyay, S., Ghalsasi, A. (2011). Cloud computing-the

business perspective. Decision Support Systems, 51, 176-189.

[17] Mendling, J., Baesens, B., Bernstein, A., Fellmann, M. (2017). Challenges of smart business process management: An introduction to the special ssue. Decision Support Systems, 100, 1-5.

[18] Muppala, S., Chen, G., Zhou, X. (2014). Multi-tier service differentiation by coordinated learning-based resource provisioning and admission control. J. Parallel Distrib. Comput., 74(5), 2351-2364.

[19] Netjinda, N., Sirinaovakul, B., Achalakul, T. (2014). Cost optimal scheduling in IaaS for dependent workload with particle swarm optimization. J. Supercomput., 68, 1579-1603.

[20] Rubio-Montero, A., Huedob, E., Mayo-García, R. (2017). Scheduling multiple virtual environments in cloud federations for distributed calculations. Future Generation Computer Systems, 74, 90-103.

[21] Sherry, X., Zhao, J. (2012). A decomposition-based approach for service composition with global QoS guarantees. Information Sciences, 199(15), 138-153.

[22] Toosi, A., Calheiros, R., Thulasiramy, R., Buyya, R. (2011). Resource provisioning policies to increase IaaS provider’s profit in a federated cloud environment. IEEE International Conference on High Performance Computing & Communications, 279-287.

[23] Wu, Z., Liu, X., Ni, Z., Yuan, D., Yang, Y. (2013). A market-oriented hierarchical scheduling strategy in cloud workflow systems. J. Supercomput., 63(1), 256-293.

[24] Ye, X., Liu, S., Yin, Y., Jin, Y. (2017). User-oriented many-objective cloud workflow scheduling based on an improved knee point driven evolutionary algorithm. Knowledge-Based Systems, 1-12 (In press).

[25] Yuan, H., Bi, J., Tan, W., Li, B. (2016). CAWSAC: cost-aware workload scheduling and admission control for distributed cloud data centers. IEEE Transactions on Automation Science and Engineering, 13(2), 976-985.

[26] Yuan, H., Bi, J., Tan, W., Li, B. (2017). Temporal task scheduling with constrained service delay for profit maximization in hybrid clouds. IEEE Transactions on Automation Science and Engineering 14(1), 337-348.

[27] Zheng, W., Sakellariou, R. (2013). Budget-deadline constrained workflow planning for admission control. J.GridComput., 11(4), 1-19.

[28] Zhu, X., Broucke, S., Zhu, G., Vanthienen, J., Baesens, B. (2016). Enabling flexible location-aware business process modeling and execution. Decision Support Systems, 83, 1-9.

[29] Zorrilla, M., García-Saiz, D. (2013). A service oriented architecture to provide data mining services for non-expert data miners. Decision Support Systems, 55(1), 399-411.

[30] Zuo, X., Zhang, G., Tan, W. (2014). Self-adaptive learning PSO-based deadline constrained task scheduling for hybrid IaaS cloud. IEEE Transactions on Automation Science and Engineering, 11(2), 564-573.

Helan Liang received her Ph.D. degree in management science and engineering from University of Science and Technology Beijing, Beijing, China, in 2010. She is currently a Lecturer with the School of Computer Science & Technology, Soochow University, Suzhou, China. Her research interests are in the areas of enterprise modeling, workflow management, and service computing.

Yanhua Du received his B.S. and M.S. degrees from Zhengzhou University, Zhengzhou, China, in 2000 and 2003, respectively, and the Ph.D. degree in transportation planning and management from the China Academy of Railway Sciences, Beijing, in 2006. He is currently an Associate Professor with the School of Mechanical Engineering, University of Science and Technology Beijing, Beijing, China. From 2006 to 2008, he was a Post-Doctoral Researcher with Department of Automation, Tsinghua University, China, His research interests are in the areas of business process reengineering, workflow management, knowledge management systems, and service computing.

Fanzhang Li received his Master degree in engineering from the Department of Computer Science, University of Science and Technology of China, in 1999. He is now a full Professor at the School of Computer Science and Technology, Soochow University, P. R. China, and is also an adjunct professor at Beijing Jiaotong University, China. His current interests include Lie Group Machine learning, Data Mining, Dynamic Fuzzy Logic.

# ACCEPTED MANUSCRIPT

## Highlights

 We propose a more comprehensive model to describe the task scheduling problem for hybrid IaaS cloud from a provider’s perspective.

Three kinds of individuals generation strategies are proposed, which can produce valid individuals satisfying the precedence relationships among tasks in different phases.

 A greedy based strategy for mapping individuals into execution plans is proposed, which can decide the VM type selection based on business value optimization.

 Three experiments in related works and five more sets of experiments with different problem sizes are used to evaluate the performance of our approach.
