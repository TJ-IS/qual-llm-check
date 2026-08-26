---
otero_id: 21251
otero_key: "U8TXC75M"
title: "An agent for selecting optimal order set in EC marketplace"
authors: "Hyung Rim Choi; Hyun Soo Kim; Byung Joo Park; Young Jae Park; Andrew B. Whinston"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00027-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An agent for selecting optimal order set in EC marketplace

Hyung Rim Choi<sup>a,</sup>\*, Hyun Soo Kim<sup>a</sup>, Byung Joo Park<sup>a</sup>, Young Jae Park<sup>a</sup>, Andrew B. Whinston

<sup>a</sup> Department of MIS, Dong-A University, 840 Hadan-dong, Saha-gu, Busan 604-714, South Korea <sup>b</sup> Center for Research in Electronic Commerce, University of Texas, Austin, TX, USA

## Abstract

For most small manufacturing companies, the selection and completion of orders placed by buyers are closely linked to the load status of their production lines. The decision to accept an order, or the selection of optimal order set, critically depends on the production schedule when orders exceed production capacity. However, production scheduling is mainly performed by human experts, and small companies lack resources to implement such a task. As a result, most small manufacturers suffer from the difficulty to meet due dates or to make proper decision in accepting new orders. To address this problem, this paper develops an automatic agent that selects an optimal set of orders using commonly available Internet technology. The main engine of the selection agent is based on a typical job shop scheduling model, formulating and implementing it as an Integer Program (IP) model. We also translate IP into Genetic Algorithm (GA) to address its NP-hard problem. We conclude with a suggestion for an agent architecture that tackles Web-based order selection problems. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Intelligent agent; Job shop scheduling; Genetic algorithm

## 1. Introduction

## 1.1. Backgrounds

The Internet-based electronic commerce is beginning to be recognized as a potential tool for small manufacturing companies to increase sales. However, small manufacturers cannot operate properly and optimally in the Internet environment due to their lack in resources such as personnel and information technology. For them to take advantage of the new tool, core technologies should be developed and improved in a way that supports electronic commerce by small manufacturing companies.

The changing digital environment requires small manufacturers to perform management tasks, such as production scheduling, more rapidly and accurately in order to fulfill requested due dates of buyers in real time. For example, injection-molding companies manufacture products that are specific to each order, which makes it hard for them to keep a ready inventory of pre-manufactured goods. Moreover, the limited production capacity of small manufacturers makes it imperative to quickly select a set of optimal orders that will generate maximum profit when orders exceed their production capacity.

However, most small manufactures lack appropriate resources in personnel, funds, and cost-effective technology to respond quickly. To solve these problems, an agent that can carry out production scheduling rapidly and automatically without human intervention is needed.

In this paper, we present a methodology for rapidly selecting an optimal order set and provide a general architecture of a selection agent that can be used in the Internet environment. The methodology of selection agent developed in this paper is successfully applied to the cases of small injection-molding companies.

## 1.2. Research scope

Our research stems from real-world problems experienced by injection-mold manufacturers. A mold is a frame or shape composed of metal ingredients used for forming a shape by such processes as injection, press, casting, and forging. The injection molding is a production method acquiring geometry by rapidly stuffing high tempered melting material into a mold.

Injection-molding products have various appearances and characteristics depending on products’ shape and functions required by specific buyers. Machine and human labor are the most important resources in the injection-mold production. An injection mold is produced after a series of operation each of which requiring a different machine. Milling, lathe, and drilling are some of the machines used for this purpose. All of the operations have to be carried out in a sequence; a certain operation must be completed before moving on to the next operation. Fig. 1 shows the shape of a divided cavity plate as an example of injection molding.

While firms may invest in adequate machinery to support manufacturing activities, small and medium molding manufacturers in Korea suffer from poor production management. Especially, the problem seems to be in scheduling because most serious complaints from customers tend to be about missed due dates. A confounding factor is the fact that most production activities in the molding industry are specific to each order. Thus, these companies cannot rely on such a standardized process management as the ones used by mass producers. Injection molds cannot be produced prior to any order. Profit-enhancing production management in this business must focus on meeting due dates and reducing costly overtime work.

This study aims at offering solutions for production management problems for small and medium molding manufacturers and to provide them with a selection agent that can schedule and select proper orders with minimum computing facilities like Internet-enabled client PCs. The selection agent-based scheduling analyzes such data as job operation sequence, processing time, due date, and profit of orders. When molding manufacturers cannot produce all the orders, the selection agent automatically presents users with an optimal set of orders that generates the most profit.

![](/api/attachments/U8TXC75M/fulltext/images/a33c3d98e64ba1d713a21e7baef16bcbc5a42aa7e16bbeaae9b615def134c3ba.jpg)  
Fig. 1. A drawing of injection mold, divided cavity plate.

## 2. Literature review

While intelligent agents have been a major part of research in artificial intelligence, intelligent agent as an independent research subject began in the late 1980s. During the preceding decade, numerous international scientific conferences and symposia have been organized for artificial intelligence, and the field has been extremely active as a number of agent-based products have been applied to real world commerce [5].

The precise definition of an intelligent agent varies. Franklin and Graesser [7] postulated that this variance was due to the specificity of each model and agent system being implemented, each emphasizing only certain attributes that are salient to the tasks to be carried out. To arrive at a common definition, then, we need to review various attributes of an intelligent agent. These attributes that differentiate them from other types of software applications include autonomy, communication ability, capacity for cooperation, capacity for reasoning, adaptive behavior, and trustworthiness [16]. Based on these attributes, we can define an intelligent agent as a software which learns, infers, and cooperates, if necessary, with other agents or systems to solve given problems actively, autonomously, and distinctively [6]. This type of intelligent agent is studied in various fields such as General Agent Theory which focuses on definition and characteristics of an agent, Agent Architecture focusing on component factors, control, and communication protocols of an agent, and other agent application fields aiming at developing application software of practical usage.

Most researches regarding job shop scheduling deal with minimizing production costs. However, our focus here is on maximizing profit through selecting an optimal set of orders that was accepted under the limited production capacity. While existing studies on scheduling focus on the production of confirmed orders, this study considers production constraints prior to confirmation of order and tries to determine starting time for each order, to satisfy due date, and to search for a set of orders that maximizes profit.

## 3. Architecture of selection agent and implementation

Fig. 2 below shows the overall architecture of a selection agent.

 Communication Controller: consisting of message converter, message queuing, and message manager; controls communications to and from other agents or inside applications of production-related agents. Functions of each module are as follows.

![](/api/attachments/U8TXC75M/fulltext/images/248eb92f03b625a3bd219002f3649a2b092b988930ce98be9f8be6e0245b6fc8.jpg)  
Fig. 2. Architecture of a selection agent.

– Message converter: every message is transmitted through the message converter and the message is changed to TCP/IP protocols. It also controls the connection with other agents.

– Message queuing: it manages outbound and inbound messages permitting only valid messages to pass.

– Message manager: it inspects message forms based on all the hierarchies of Knowledge Query and Manipulation Language (KQML) [11], and initializes the reasoning engine to generate a response message according to the query message.

 Problem Solver: is a selection agent engine that executes a Genetic Algorithm (GA) program.

 Result Analyzer: saves results which are the scheduling outcome of Problem Solver (GA module), then it saves the results into database.

 Database Handler: saves and manages input data and result data.

## Other Agents [6].

 Manufacturability Analysis Agent: this determines the manufacturability of a product based on the geometry information of a product received from the sales agent, considering various constraints satisfied in the process of manufacturing.

 Process Planning Agent: this generates a feature set from the Feature-Based Model (FBM) and determines the optimal operation sequences using knowledge base and geometric information of a product. This generates man-hours for manufacturing each product by machine and calculates cost of each product.

## 4. The scheduling method

In this study, Mixed Integer Programming (MIP) and Genetic Algorithm (GA) are used as the scheduling methods for selecting an optimal order set. Our MIP model was formulated based on Manne’s [13] mixed-integer linear programming. In this formulation, the objective function maximizes profit while constraints are imposed to satisfy due date requirements.

The scheduling process proceeds as follows. After setting up an initial schedule for orders requested on a certain day, a manufacturer produces all those orders if she can meet due dates for all orders. And if she determines that she cannot produce all orders, production will be carried out in a sequence based on the selection process that generates most profit. The first stage of the selection process focuses on selecting the optimal order set that can meet due dates. In the second stage, a manufacturer plans a job schedule for those selected orders in order to minimize makespan.

## 4.1. Stage 1: selecting an optimal order set

In the selection problem of the first stage, the following are assumed [1].

 Setting time for a machine will be included in the processing time of some operation on the machine.

 Only one operation can be performed with one machine, and an operation cannot be performed simultaneously with multiple machines.

 When there are alternative machines, each of those machines is considered as an independent machine.

A summary of symbols that are used in our model follows.

## 4.1.1. Constants

 $p _ { i } \mathbf { \cdot }$ profit generated when order i is produced.

$p _ { i j k } \mathrm { : }$ the processing time of the jth operation of order i on machine k.

$r _ { i j k } \colon ~ 1$ , if the jth operation of order i requires machine $k ; 0 ,$ otherwise.

 d<sub>i</sub>: due date of order i.

 M: an arbitrary large integer.

## 4.1.2. Variables

$T _ { i j k } \colon \geq 0$ , the starting time of the jth operation of order i on machine k.

$O _ { i \cdot } ^ { \cdot } 1$ , if order i is selected; 0, if not.

$F _ { \mathrm { m a x } } .$ : indicates finishing time of last job.

$Y _ { ( i j ) ( i ^ { \prime } j ^ { \prime } ) k } \colon 1$ , if the jth operation of order i proceeds the jVth operation of order iVon machine $k ; 0 ,$ , otherwise.

The first stage to determine an optimal order set proceeds as follows.

## 4.1.3. Objective function

$$
\text { MAX } \quad \sum_ {i} p _ {i} O _ {i}
$$

Variable $O _ { i }$ represents the selection of orders. If an order is selected, it has a value of 1 and, if not, it has a value of 0. The objective is to maximize profits (revenues) from the selected set of orders, subject to following constraints.

## 4.1.4. Constraints

(1) Operation j must precede operation $j + l$ for order i.

$$
\sum_ {k} r _ {i j k} (T _ {i j k} + p _ {i j k}) - \sum_ {k} r _ {i, j + 1, k} \cdot T _ {i, j + 1, k} \leq (1 - O _ {i}) M
$$

(2) The last operation of each order must be completed before the due date. Index m indicates the final operation of each order.

$$
\sum_ {k} r _ {i m k} (T _ {i m k} + p _ {i m k}) \leq d _ {i}
$$

(3) For example, assume that there are two operations with machine k. If operation j of order i must precede operation jVof order iV, then it has to satisfy $T _ { i ^ { \prime } j ^ { \prime } k } - T _ { i j k } { \ge } p _ { i j k }$ . On the other hand, if operation jVof order iVmust precede operation j of order i, it has to satisfy $T _ { i j k } - T _ { i ^ { \prime } j ^ { \prime } k } { \geq } p _ { i ^ { \prime } j ^ { \prime } k }$ . This restriction is called disjunctive constraints and since this type of constraint cannot be solved with general integer programming, an indication variable such as $Y _ { i j i ^ { \prime } j ^ { \prime } k }$ is needed [14]. This kind of disjunctive constraint can be divided into two independent constraints using the indication variable and the big M as follows:

$$
\begin{array}{l} (1 - O _ {i}) M + (1 - O _ {i ^ {\prime}}) M + M Y _ {i j i ^ {\prime} j ^ {\prime} k} \\ \quad + (T _ {i j k} - T _ {i ^ {\prime} j ^ {\prime} k}) \geq p _ {i ^ {\prime} j ^ {\prime} k} \\ (1 - O _ {i}) M + (1 - O _ {i ^ {\prime}}) M + M (1 - Y _ {i j i ^ {\prime} j ^ {\prime} k}) \\ \quad + (T _ {i ^ {\prime} j ^ {\prime} k} - T _ {i j k}) \geq p _ {i j k} \end{array}
$$

## 4.2. Stage 2: scheduling to minimize finishing time

At the second stage, scheduling is established for the selected set of orders. The goal of the objective function is to minimize completion time for each order. The model derives from Bowman [3], Manne [13], and Wagner [19]. Its description below will follow Manne’s model.

## 4.2.1. Objective function

MIN $F _ { \mathrm { m a x } }$

## 4.2.2. Constraints

Completion time, instead of due dates employed in the first stage, is used as a constraint in the second stage.

$$
\sum_ {k} r _ {i m k} (T _ {i m k} + p _ {i m k}) \leq F _ {\max}
$$

Table 1 summarizes objective functions and constraints of the selection agent.

## 4.3. Experiment results

To test the above formulation, we used Muth and Thompson’s [15] MT6  6 which is well recognized as a benchmark problem in job shop scheduling domain. We used the ILOG package (http://www.ilog.com) for solving MIP. The result of our experiment was 55 (makespan), which is equal to the optimal solution of $\mathrm { M T } 6 \times 6 .$ . Table 2 summarizes the process sequence and process time of each job and the result of our experiment in $\mathrm { M T } 6 \times 6 .$ The result is start time and finish time of each machine for each job.

Next, our formulation was run to test another problem of selecting an optimal order set that maximizes profit. Its result was successful and satisfactory. The ILOG package was good up to the size of an 8  8 problem. But the ILOG package failed to find a solution in larger problems. From these results, we concluded that a more general and robust method was needed to solve the problem which is known as NP-hard [12].

## 4.4. Genetic algorithm module

Most scheduling problems are NP-hard from the computational viewpoint. Scheduling problems in the real world tend to be solved using a combination of search and heuristics to get optimal or near-optimal solutions. Among various search methods used for

Table 1  
Stage by stage approach of selection agent

<table><tr><td colspan="2">Stage 1</td></tr><tr><td>Objective function</td><td>MAX $\sum_{i} p_{i} O_{i}$ </td></tr><tr><td>Constraints</td><td> $\sum_{k} r_{ijk}(T_{ijk} + p_{ijk}) \leq \sum_{k} r_{i,j+1,k} T_{i,j+1,k} + (1 - O_{i}) M$  $\sum_{k} r_{imk}(T_{imk} + p_{imk}) \leq d_{i}$  $(1 - O_{i}) M + (1 - O_{l'}) M + MY_{ijl'f'k} + (T_{ijk} - T_{l'f'k}) \geq p_{l'f'k}$  $(1 - O_{i}) M + (1 - O_{l'}) M + M(1 - Y_{ijl'f'k}) + (T_{l'f'k} - T_{ijk}) \geq p_{ijk}$ </td></tr></table>

Stage 2

<table><tr><td>Objective function</td><td>MIN  $F_{\text{max}}$ </td></tr><tr><td>Constraints</td><td> $\sum_{k} r_{ijk}(T_{ijk} + p_{ijk}) \leq \sum_{k} r_{i,j+1,k} T_{i,j+1,k}$  $\sum_{k} r_{imk}(T_{imk} + p_{imk}) \leq F_{\text{max}}$  $(M + p_{i'f'k}) Y_{iji'f'k} + (T_{ijk} - T_{i'f'k}) \geq p_{i'f'k}$  $(M + p_{ijk})(1 - Y_{iji'f'k}) + (T_{i'f'k} - T_{ijk}) \geq p_{ijk}$ </td></tr></table>

scheduling problems, the GA, inspired by the process of Darwinian evolution, has been recognized as a general search strategy and optimization method which is often useful in attacking combinatorial problems. The GA utilizes a population of solution in its search, giving it more resistance to premature

Table 2  
The result of experiment

<table><tr><td colspan="13">MT6 × 6 problem, optimal value=55</td></tr><tr><td></td><td>Machine</td><td>Man-hours</td><td>Machine</td><td>Man-hours</td><td>Machine</td><td>Man-hours</td><td>Machine</td><td>Man-hours</td><td>Machine</td><td>Man-hours</td><td>Machine</td><td>Man-hours</td></tr><tr><td>Job1</td><td>2</td><td>1</td><td>0</td><td>3</td><td>1</td><td>6</td><td>3</td><td>7</td><td>5</td><td>3</td><td>4</td><td>6</td></tr><tr><td>Job2</td><td>1</td><td>8</td><td>2</td><td>5</td><td>4</td><td>10</td><td>5</td><td>10</td><td>0</td><td>10</td><td>3</td><td>3</td></tr><tr><td>Job3</td><td>2</td><td>5</td><td>3</td><td>4</td><td>5</td><td>8</td><td>0</td><td>9</td><td>1</td><td>1</td><td>4</td><td>7</td></tr><tr><td>Job4</td><td>1</td><td>5</td><td>0</td><td>5</td><td>2</td><td>5</td><td>3</td><td>3</td><td>4</td><td>8</td><td>5</td><td>9</td></tr><tr><td>Job5</td><td>2</td><td>9</td><td>1</td><td>3</td><td>4</td><td>5</td><td>5</td><td>4</td><td>0</td><td>3</td><td>3</td><td>1</td></tr><tr><td>Job6</td><td>1</td><td>3</td><td>3</td><td>3</td><td>5</td><td>9</td><td>0</td><td>10</td><td>4</td><td>4</td><td>2</td><td>1</td></tr><tr><td colspan="13">The results of experiment</td></tr><tr><td></td><td>Start time</td><td>Finish time</td><td>Start time</td><td>Finish time</td><td>Start time</td><td>Finish time</td><td>Start time</td><td>Finish time</td><td>Start time</td><td>Finish time</td><td>Start time</td><td>Finish time</td></tr><tr><td>Job1</td><td>5</td><td>6</td><td>10</td><td>13</td><td>30</td><td>36</td><td>36</td><td>43</td><td>43</td><td>46</td><td>49</td><td>55</td></tr><tr><td>Job2</td><td>0</td><td>8</td><td>8</td><td>13</td><td>15</td><td>25</td><td>28</td><td>38</td><td>40</td><td>50</td><td>50</td><td>54</td></tr><tr><td>Job3</td><td>0</td><td>5</td><td>5</td><td>9</td><td>9</td><td>17</td><td>18</td><td>27</td><td>41</td><td>42</td><td>42</td><td>49</td></tr><tr><td>Job4</td><td>8</td><td>13</td><td>13</td><td>18</td><td>22</td><td>27</td><td>27</td><td>30</td><td>30</td><td>38</td><td>46</td><td>55</td></tr><tr><td>Job5</td><td>13</td><td>22</td><td>22</td><td>25</td><td>25</td><td>30</td><td>39</td><td>43</td><td>51</td><td>54</td><td>54</td><td>55</td></tr><tr><td>Job6</td><td>13</td><td>16</td><td>16</td><td>19</td><td>19</td><td>28</td><td>28</td><td>38</td><td>38</td><td>42</td><td>54</td><td>55</td></tr></table>

Fig. 3. Representation of JSSP.

convergence on local minima. For this reason, GA has been regarded as a proper tool for solving scheduling problems. In this section, we describe a GA approach to the Job Shop Scheduling Problem (JSSP).

## 4.4.1. Genetic algorithm design

We introduce the major components—representation, initialization, crossover, mutation, and replacement—of the GA which are already proven successfully through various benchmark JSSPs [17,18]. The GA approach produced optimal solution in MT6  6 benchmark problem, as MIP produced optimal solution. Also, it produced optimal solution in larger benchmark problems.

 Representation: a very important issue in building a GA for the job shop problem is to select an appropriate representation of solutions. We have adopted an Operation-Based Representation [8], which is capable of coping with additional constraints of the JSSP. For an n-job m-machine, an Operation-Based Representation uses an unpartitioned permutation with m-repetition of job numbers. Here, each job number occurs m times in the permutation. The kth occurrence of a job number refers to the kth operation in the technological order of this job. In this way we avoid scheduling operations whose technological predecessors have not yet been scheduled. For example, consider the chromosome of three jobs and three machines represented in Fig. 3. An index number refers to the kth occurrence of a particular job number. It is used to point to the corresponding operations in crossover. A permutation with repetition of job numbers merely expresses the order in which operations of jobs are scheduled.

 Initialization: a chromosome is made by the G&T (Giffler and Thomson) algorithm [9] to generate active schedules. Initial population is composed of chromosomes generated by G&T.

 Selection: a tournament selection [10] is adopted as a selection procedure. And a makespan is used as an objective function to evaluate a chromosome.

 Crossover: the crossover operator is the most important search operator in GA. Among the various permutation operators proposed, we use Modified Order Crossover (MOX) which is modified from the techniques of GOX [2]. MOX assembles one offspring from two parental chromosomes. In MOX, as we can see in Fig. 4, a substring is chosen randomly from the parent 1. MOX implants the substring into the parent 2 at the position where the first gene of substring is located. Then all genes of the substring are deleted with respect to their index of occurrence in the receiving chromosome. The process of crossover follows the same procedure after exchanging the parents 1 and 2 with the same interval. Then two offspring are evaluated and the best one is chosen.

Changing the parents 1 and 2 with same interval generates offspring 2.

![](/api/attachments/U8TXC75M/fulltext/images/55d4090b5c8b933524e93be9c5fb80bc13e82b4d4b281521ec27e721c8828b54.jpg)  
Fig. 4. Modified order crossover.

<table><tr><td>Parent chromosome</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Neighbor chromosomes</td><td>↓</td><td></td><td></td><td></td><td>↓</td><td></td><td></td><td></td><td>↓</td></tr><tr><td>case 1</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>case 2</td><td>2</td><td>2</td><td>3</td><td>1</td><td>1</td><td>3</td><td>1</td><td>2</td><td>3</td></tr><tr><td>case 3</td><td>2</td><td>2</td><td>3</td><td>1</td><td>3</td><td>3</td><td>1</td><td>2</td><td>1</td></tr><tr><td>case 4</td><td>3</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>1</td></tr><tr><td>case 5</td><td>3</td><td>2</td><td>3</td><td>1</td><td>1</td><td>3</td><td>1</td><td>2</td><td>2</td></tr><tr><td>case 6</td><td>1</td><td>2</td><td>3</td><td>1</td><td>3</td><td>3</td><td>1</td><td>2</td><td>2</td></tr></table>

Fig. 5. Neighborhood search-based mutation.

 Mutation: is used to produce small perturbations on chromosomes in order to maintain the diversity of population. We adopt neighborhood search-based mutation [4]. For permutation representation, the neighborhood for a given chromosome can be considered as the set of chromosomes transformable from a given chromosome by exchanging the positions of three genes (randomly selected and non-identical genes). The permutations of the genes together with the remaining genes of the chromosome form the neighbor chromosomes shown in Fig. 5. Subsequently, we evaluate all neighbor chromosomes and the best one is used as the offspring of mutation.

In Fig. 5, the mutation comparing all six cases (cases 1–6) is called six-case mutation; the mutation comparing only five cases (cases 2–6) is called five-case mutation. The former is used right after crossover, whereas the latter is used as the general mutation operator.

 Replacement: the next generation replaces the current generation only after the new population is completely created. The procedure of replacement is shown in Fig. 6. And we use elitism in replacement. Elitism can guarantee to do no worse than conventional GA does, especially in case of GA where the initial population is generated with heuristics that generates well-adapted initial population.

## 5. Case study

For selecting an optimal order set, we implement a selection agent as a single agent which has the abilities of autonomy, intelligence, and adaptation for dynamic environment. If there are other agents such as a buyer agent, the selection agent could communicate with it, relaying its order message using KQML. As a case study, we used the example of Jesan Precision, an injection-molding company. On a certain day, Jesan Precision received three orders for an elbow, a picnic case, and a cake box as shown in Table 3, where the size indicates the size of the job shop. It is denoted by the number of jobs  the number of machines needed to fulfill the order.

![](/api/attachments/U8TXC75M/fulltext/images/fb060ac78556478a326dbb675c6c115fddd0a30271206bc912d62b1403d25d4f.jpg)  
Fig. 6. The progress of replacement

Table 3  
The order data of Jesan Precision

<table><tr><td>Order</td><td>Size</td><td>Due date</td><td>Profit ($)</td></tr><tr><td>Elbow</td><td> $7 \times 10$ </td><td>2001-06-25</td><td>100</td></tr><tr><td>Picnic case</td><td> $9 \times 9$ </td><td>2001-06-25</td><td>120</td></tr><tr><td>Cake box</td><td> $7 \times 9$ </td><td>2001-06-25</td><td>130</td></tr></table>

5.1. The information regarding an order is transmitted from a buyer agent to the manufacturer’s selection agent

Three orders are received from buyer1, buyer2, and buyer3. The KQML messages are as follows. Also, the detailed information of a product is received from buyer agent.

(ask-one :sender buyer1 :receiver Jesan Co. :language KQML :reply-with order1 :date 2001-06-10 :contents (product\_name picnic case, due\_date 2001-06-25, price \$30000))

(ask-one :sender buyer2 :receiver Jesan Co. :language KQML :reply-with order2 :date 2001-06-10 :contents (product\_name cake box, due\_date 2001-06-25, price \$40000))

(ask-one :sender buyer3 :receiver Jesan Co. :language KQML :reply-with order3 :date 2001-06-10 :contents (product\_name elbow, due\_date 2001-06-25, price \$35000))

5.2. After the orders are scheduled by problem solver (GA module), the selection agent decides on acceptance or rejection for each order

First, the selection agent determines manufacturability based on the information of a product received and performs process planning using product information and generates optimal process plans through manufacturability agent and process planning agent [6]. Next, the selection agent schedules these orders.

In this case, the IP module could not schedule three orders simultaneously because the size of scheduling problem was too big (23 jobs, 13 machines). Thus, we scheduled three orders using GA module. Genetic parameters are determined through various experiments. In our experiment, crossover and mutation rates, population size, generation number, elitism size, and selection probability were 0.8, 0.1, 200, 1000, 10, and 0.75, respectively. The experiment was carried out on a PC with Pentium III 600 E and 128 Mb of main memory.

When the GA module schedules new orders, it produces completion time of each order by incremental scheduling based on available information from the previous production schedule. The completion time for three orders was calculated to be 2001-06-30, 2001-06-29, and 2001-06-30, respectively. In this scheduling, we could not meet the due dates for all three orders.

When the due dates of all orders cannot be met, the GA module searches optimal combinations of orders that can be completed while meeting due dates. First, it searches one order with the largest profit that can be completed before its due date, then continues to search for a combination of two orders, then a combination of three orders, and so on. The combination with a larger profit is ranked higher.

In our example of three orders, the GA module confirms the completion time of the cake box which produces the largest profit. Since the due date is met, the GA module searches and confirms the possible production combination of cake box and picnic case, which produces most profit as shown in Table 4. This combination meets all due dates. As a result, we are able to find a possible production combination of two orders, and decide to produce picnic case and cake box.

Table 5 The order data of Jesan Precision  
Table 4  
The results of the example

<table><tr><td>Order selection</td><td>Completion time</td><td>Computational time (s)</td><td>Due date</td><td>Observance of due date</td><td>Profit ($)</td><td>Selection</td></tr><tr><td>Elbow</td><td>2001-06-30</td><td>164</td><td>2001-06-25</td><td>×</td><td>0</td><td></td></tr><tr><td>Picnic case</td><td>2001-06-29</td><td></td><td>2001-06-25</td><td>×</td><td></td><td></td></tr><tr><td>Cake box</td><td>2001-06-30</td><td></td><td>2001-06-25</td><td>×</td><td></td><td></td></tr><tr><td>Cake box</td><td>2001-06-20</td><td>46</td><td>2001-06-25</td><td>○</td><td>130</td><td></td></tr><tr><td>Picnic case</td><td>2001-06-23</td><td>98</td><td>2001-06-25</td><td>○</td><td>250</td><td>○</td></tr><tr><td>Cake box</td><td>2001-06-24</td><td></td><td>2001-06-25</td><td>○</td><td></td><td></td></tr></table>

## 5.3. The result of scheduling is transmitted from selection agent to a buyer agent

Since Jesan Precision cannot produce all orders, the selection agent sends confirmation messages regarding order acceptance as follows.

(tell :sender Jesan Co. :receiver buyer1 :language KQML :in-reply-to order1 :reply-with confirm1 :date 2001-06-10 :contents (product\_name picnic case, due\_date 2001-06-25, price \$30000, contract\_confirm YES)) (tell :sender Jesan Co. :receiver buyer2 :language KQML :in-reply-to order2 :reply-with confirm2 :date 2001-06-10 :contents (product\_name cake box, due\_date 2001-06-25, price \$40000, contract\_confirm YES)) (tell :sender Jesan Co. :receiver buyer3 :language KQML :in-reply-to order3 :reply-with reject1 :date 2001-06-10 :contents (product\_name elbow, due\_date 2001-06-25, price \$35000, contract\_confirm NO))

Fig. 7 is a screen developed to test the selection agent, the left side is for input buyer’s request and the right side is for displaying information sent by the selection agent. Buyers send detailed information of a product through FTP protocol. Also, Selection agent is now being implemented using Java, including KQML-based knowledge management module. JDK v1.1.8 of Sun Microsystems and JAT Lite v0.4 beta version, KQML-based agent template, are used to develop Java applications.

The next day, Jesan Precision received two orders for a paper box and a fan as shown in Table 5.

Two orders are received from buyer4 and buyer5. The KQML message is as follows:

(ask-one :sender buyer4 :receiver Jesan Co. :language KQML :reply-with order4 :date 2001-06-11 :contents (product\_name paper box, due\_date 2001-07-02, price \$33000))

(ask-one :sender buyer5 :receiver Jesan Co. :language KQML :reply-with order5 :date 2001-06-11 :contents (product\_name fan, due\_date 2001-07-02, price \$34000))

<table><tr><td>Order</td><td>Size</td><td>Due date</td><td>Profit ($)</td></tr><tr><td>Paper box</td><td>7 × 10</td><td>2001-07-02</td><td>100</td></tr><tr><td>Fan</td><td>7 × 9</td><td>2001-07-02</td><td>120</td></tr></table>

![](/api/attachments/U8TXC75M/fulltext/images/857b034b9298758f7bbaaf78e2d1c56d43c342256867a0f910b6cdb93657174c.jpg)  
Fig. 7. Screenshot of selection agent.

For these new orders, the GA module produces completion time for each order by incremental scheduling given the existing production schedule. The previous schedule is not changed while new jobs are added.

Given the calculated completion times for additional orders, the GA module first compares these with buyers’ due dates. Producing both orders fail to meet due dates. Then the GA module confirms the completion time of fan, which produces a bigger profit than paper box, as shown in Table 6. This combination meets the due date. As a result, we decide to produce fan. Here, we can confirm that GA is more suitable as a scheduling module of selection agent.

Since Jesan could not produce two orders, the selection agent should send the message regarding order acceptance as follows.

(tell :sender Jesan Co. :receiver buyer4 :language KQML :in-reply-to order4 :reply-with reject2 :date 2001-06-11 :contents (product\_name paper box, due\_date 2001-07-02, price \$33000, contract\_confirm NO))

(tell :sender Jesan Co. :receiver buyer5 :language KQML :in-reply-to order5 :reply-with confirm3 :date 2001-06-11 :contents (product\_name fan, due\_date 2001-07-02, price \$34000, contract\_confirm YES))

Table 6  
The results of a new scheduling

<table><tr><td>Order selection</td><td>Completion time</td><td>Computational time (s)</td><td>Due date</td><td>Observance of due date</td><td>Profit ($)</td><td>Selection</td></tr><tr><td>Paper box</td><td>2001-07-07</td><td>92</td><td>2001-07-02</td><td>×</td><td>0</td><td></td></tr><tr><td>Fan</td><td>2001-07-07</td><td></td><td>2001-07-02</td><td>×</td><td></td><td></td></tr><tr><td>Fan</td><td>2001-07-02</td><td>46</td><td>2001-07-02</td><td>○</td><td>120</td><td>○</td></tr></table>

## 6. Conclusion

We focused on small and medium companies in this paper, because the size of order-based company is small or medium. In order to support production and sales capacity of small and medium companies in the age of the Internet, we have proposed an architecture and methodology of a selection agent. We have developed an integer programming formula to acquire an optimal set of orders that maximize profit and to schedule production processes that minimize production cost. Like other scheduling algorithms, this problem is NP-hard, which cannot be solved using IP model. To cope with the complexity inherent in this type of scheduling problem and to replicate the necessarily dynamic environment, we have proposed a Genetic Algorithm, and our case study shows that it performs satisfactorily.

The main implication of the paper is to build an agent that can act as a sales engineer who estimates the incoming orders from a B2B EC marketplace by fully understanding the production capacity and scheduling to know whether the company can satisfy the due date of orders. The agent couples with optimization method to promptly schedule and select optimal order sets as well as communication facilities in the dynamic EC environment. In other sense, this paper is an approach to harmonize the traditional conflicts between sales and production activity. The conflicts are usually due to difference of the goals and lack of information from each activity. The agent can connect the gap of knowledge of each activity and can do decision making in small and medium companies where the human experts are not sufficiently available.

Future research directions will be to cope with dynamic negotiation features between buyers and manufacturers, and variety of fluctuant situation during manufacturing process.

## Acknowledgements

This work was supported by the Brain Korea 21 Project in 2002 and partly by Dong-A University.

## References

[1] K.R. Baker, Introduction to Sequencing and Scheduling, Wiley, New York, 1974.

[2] C. Bierwirth, A Generalized Permutation Approach to Job Shop Scheduling with Genetic Algorithms, OR-Spektrum, Special Issue: Applied Local Search, in: E. Pesch, S. Vo (Eds.), vol. 17 (213), 1995, pp. 87– 92.

[3] E.H. Bowman, The schedule-sequencing problem, Operations Research 7 (5) (1959) 621– 624.

[4] R. Cheng, A study on genetic algorithms-based optimal scheduling techniques, PhD thesis, Tokyo Institute of Technology, (1997).

[5] J.M. Choi, Overview and research direction of agent, Korea Information Science Society Review 15 (3) (1997) 7 –15.

[6] H.R. Choi, H.S. Kim, Y.J. Park, K.H. Kim, M.H. Joo, H.S. Shon, A sales agent for part manufacturers: VMSA, Decision Support Systems 28 (4) (2000) 333 – 346.

[7] S. Franklin, A. Graesser, Is it an Agent or just a program?: a taxonomy for autonomous agents, Proceedings of the 3rd International Workshop on Agent Theories, Architecture and Language, 1996.

[8] M. Gen, R. Cheng, Genetic Algorithms and Engineering Design, Wiley, New York, 1997.

[9] J. Giffler, G.L. Thompson, Algorithms for solving production scheduling problems, Operations Research 8 (1960) 487– 503.

[10] D.E. Goldberg, K. Deb, A comparative analysis of selection schemes used in genetic algorithms, in: G. Rawlins (Ed.), Foundations of Genetic Algorithms, Morgan Kaufmann, San Mateo, CA, 1991, pp. 69 – 93.

[11] Y. Labrou, T. Finin, A Proposal for a New KQML Specification, Univ. of Maryland Computer Science and Electrical Engineering Dep., tech. report CS-97-03, 1997.

[12] K.J. Lee, Y.S. Chang, H.R. Choi, H.S. Kim, Y.J. Park, B.J. Park, Negotiation and decision making of virtual manufacturing agent under time-bounded environment, Proceedings of the ICEC 2001, Oct 31–Nov 4, Vienna, Austria, 2001.

[13] A.S. Manne, On the job-shop scheduling problem, Operations Research 8 (2) (1960) 219–223.

[14] T.E. Morton, D.W. Pentico, Heuristic Scheduling System, Wiley, New York, NY, 1993, pp. 366 – 369.

[15] J.F. Muth, G.L. Thompson, Industrial Scheduling, Prentice-Hall, Englewood Cliffs, NJ, 1963.

[16] M. Nissen, Intelligent Agent: A Technology and Business Application Analysis, 1995. http://www.haas.berkeley.edu/ \~helimann/agents/.

[17] B.J. Park, A Development of Hybrid Genetic Algorithms for Scheduling of Static and Dynamic Job Shop, PhD thesis, Department of Industrial Engineering, Dong-A University, (1999).

[18] B.J. Park, H.R. Choi, H.S. Kim, A hybrid genetic algorithms for job shop scheduling problems, in: E. Goodman (Ed.), Genetic and Evolutionary Computation Conference Late-Breaking Papers, July 7 – 11, ISGEC Press, San Francisco, 2001, pp. 317– 324.

[19] H.M. Wagner, An integer linear-programming model for machine scheduling, Naval Research Logistics Quarterly 6 (2) (1959) 131– 140.

![](/api/attachments/U8TXC75M/fulltext/images/cd7350ebaf591524569f6b0999d6f63fb6e8710d8d842bc37ca5e1ba5cd0adbc.jpg)

Hyung Rim Choi is a professor of Management Information Systems at the Dong-A University in Korea. He received his BBA from Seoul National University, an MS and PhD in management science from the Korea Advanced Institute of Science and Technology. His major research interests include AI for electronic commerce, automation of process planning, and scheduling in manufacturing systems. Now he is interested in the research area

![](/api/attachments/U8TXC75M/fulltext/images/91b2318dcc4c26b6cceefdf13c82a9056cbdf7a3c42194dd5b6c45f780f7e742.jpg)

Young Jae Park is a graduate student of Management Information Systems at the Dong-A University in Korea. He received his BBA from Busan University of Foreign Studies and majored in management information system. His major research interests include AI for electronic commerce, decision support system/expert system, agent applications, and management information system. Now he is interested in the research area of port and logistics systems.

of port and logistics systems. He is a member of the American Association for Artificial Intelligence.

![](/api/attachments/U8TXC75M/fulltext/images/b4f74b4d0cc88c2a9ce6f74c96d31b416a7eeeebe7764b6c8a6372fb6f0d3b58.jpg)

Hyun Soo Kim is a professor of Management Information Systems at the Dong-A University in Korea. He received his BBS from Seoul National University, an MS and PhD in management science from the Korea Advanced Institute of Science and Technology. His current research interests lie in agent-mediated commerce and collaboration in supply chain and virtual market.

![](/api/attachments/U8TXC75M/fulltext/images/a538398e5e07e07a4deb7cf6f3cd35f6ae444f447e2f5bbeb233759bf18240e7.jpg)

Byung Joo Park is a post-doctor of BK21 Agent-based Electronic Commerce team at the Dong-A University in Korea. He received his BS, MS, and PhD in industrial engineering from the Dong-A University. His major research interests include intelligent agent system, application of optimization method, and scheduling in manufacturing systems.

![](/api/attachments/U8TXC75M/fulltext/images/f55499e528ee22aaab06ca1bbdb55ddbc04373ea7c443f65241e93cabc1c611a.jpg)

Andrew B. Whinston is currently a Professor of Information Systems, Economics, and Computer Science, Hugh Roy Cullen Centennial Chair in Business Administration, Director of Center for Research in Electronic Commerce at The University of Texas, Austin. He has published over 300 papers in top-rated scientific journals. He recently co-authored the following books: The Frontiers of Electronic Commerce, Electronic Commerce—A Manager’s

Guide, The Economics of Electronic Commerce, The Internet Economy: Technology and Practice, and Electronic Commerce and the Revolution in Financial Markets.
