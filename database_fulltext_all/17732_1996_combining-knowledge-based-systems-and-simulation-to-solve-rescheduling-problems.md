---
otero_id: 17732
otero_key: "65MCY35W"
title: "Combining knowledge-based systems and simulation to solve rescheduling problems"
authors: "R. Belz; P. Mertens"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(95)00029-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combining knowledge-based systems and simulation to solve rescheduling problems

R. Belz, P. Mertens

Bereich Wirtschaftsinformatik 1, Universität Erlangen-Nürnberg, Postfach 3931, D-90020 Nürnberg, Germany

## Abstract

Knowledge-based systems can help to enlarge the application range for simulation. Acting as intelligent front-ends they communicate with the user and provide statistical knowledge. As an example, the paper presents SIMULEX, a prototype decision support system for short-term rescheduling in manufacturing. SIMULEX couples expert systems and simulation to assist the production manager in handling production disturbances. Its core is a job shop simulator that models the plant and evaluates the results of various rescheduling measures. One intelligent front-end (the access system) gathers information about the disturbance and configures the simulation experiments. Another (the run time control) supervises the simulation runs. A third one (the termination/interpretation system) analyzes the data, derives conclusions and suggests the most promising measures. The paper focuses on the system's decision model that allows multi-attribute decisions under uncertainty.

Keywords: Knowledge-based systems; Intelligent front-ends; Manufacturing; Production; Scheduling; Simulation

## 1. Introduction

In the last few years, computer-based simulation models have been used more and more to represent a wide area of technical and organizational systems. The main reasons for this can be traced to the well-known advantages of simulation, which become even more prevalent as the price/performance ratio of computers improves.

But using simulation leads to some problems, too. The difficulties of simulation model building have been eased by the development of various problem-oriented simulation languages, by tools that assist the model builder and the user with graphical displays and/or AI-techniques $[3;9,25]$ , and by the availability of specialized computer hardware like AI-workstations. A fundamental problem remains, though: all simulation phases require statistical methods [18]. However, many potential users are lacking in the necessary knowledge. Therefore, they often apply simulation incorrectly.

In this domain, expert systems (XPS) or knowledge-based systems (KBS) can serve as intelligent front-ends [20] to interface between the simulation and the user. Access systems configure the simulation experiments and adjust all necessary parameters. Termination/interpretation systems analyze the often complex and confusing data produced by simulation [22] and present them in a format that is both understandable and informative. This facilitates the usage of simulation even by novices because they only have to deal with the XPS, and in the ideal case, the simulation simply becomes a “black-box” for them.

In the project SIMULEX [4], we will show the possibilities of combining XPS with simulation to solve problems in the area of scheduling and rescheduling.

## 2. The project SIMULEX

## 2.1. Problems of production control

Today's methods for automatic production control show several deficiencies [7,8,29,30]. Random disruptions in particular are disregarded, leading to a frequent need for rescheduling. A survey of several German job shops showed that about one third of all orders could not be finished as planned due to such effects [24]. If rescheduling becomes necessary, the production manager has to take many consequences into account simultaneously, but is offered hardly any support.

A solution to this problem is sought in a man-machine combination. For this purpose, a dedicated computer graphics-based scheduling support system is used, the so-called Leitstand [1]. Its possibilities, though, are often mere electronic copies of the well-known Gantt-charts and related tools used before.

In our opinion the manager could be supported much more efficiently by a simulation-based DSS residing on the Leitstand that meets certain requirements. It should be able to generate various alternative solutions, evaluate their performance in a prognosis, and then select the best one or determine a set of most promising candidates. This approach has not been used very often, though, due to the problems with simulation mentioned before.

## 2.2. Project goals

The main purpose of SIMULEX is to show that the approach outlined before is feasible. The system intends to help the shop floor personnel dealing with unforeseeable occurrences such as machine breakdowns, late deliveries of purchase items, high-priority jobs entering the system, etc. From the problems mentioned in Sections 1 and 2.1 the following requirements for a DSS that uses simulation in the area of production rescheduling were derived:

\- generate alternative solutions

\- adjust their parameters

• prepare the simulation experiments

• conduct the experiments

\- analyze the results

\- present a few “best ones” along with their specific strengths and weaknesses

This last requirement appears because, in the end, we want the production manager to decide which action to take.

In contrast to the other solutions that integrate simulation and KBS like KBOLS (K knowledge-based Online Simulation [26]), SIMULEX was designed to respect stochastic influences. This led to a special decision model (see Sections 3.1 and 3.5). Also, it is not restricted to flexible manufacturing systems, but targets the more complicated workflow in a job shop.

## 2.3. Rescheduling philosophy

Before the system can be described in detail, it is necessary to explain the underlying rescheduling philosophy since it has a strong influence on the decision criteria.

There are varying opinions on how to deal with rescheduling needs. Complete replanning is impossible under most circumstances due to time restrictions. One solution is to keep the elaborate schedule valid for the whole planning period, usually one week, by correcting deviations in such a manner that the original schedule is re-entered as soon as possible. This approach is called turnpike scheduling $[2,28]$ . Besides requiring only small modifications of the orders' schedule, it has the additional advantage of minimizing changes in the depending plans for tools, fixtures, workers, etc. $[27]$ .

The supporters of opportunistic scheduling $[10,21]$ claim that it is not worth the effort to produce a sophisticated schedule as it is valid only for a short period of time. Instead, a simple and quick new schedule is set up each time the current one cannot be maintained anymore.

SIMULEX follows the turnpike scheduling paradigm for two reasons. One reason is that we think a longer-term plan can be adapted better to the goals of the company. The other reason is that an existing schedule provides a good measure of how valuable a rescheduling method can be, because the most important criteria in this case are the differences between the planned and the actual completion dates of the job shop orders. But we know that under certain circumstances the old schedule might no longer be feasible. As a result, we intend to expand SIMULEX's capabilities to cover scheduling as well. Then generating an entirely new schedule becomes an additional rescheduling alternative.

## 2.4. The environment for SIMULEX

The knowledge about specific rescheduling alternatives cannot be stored completely independent from the considered production system. Even the access to the data necessary for production control requires information about its structure and its representation in an MRP system.

As a reference object for various research projects including SIMULEX, we have developed a model plant as part of the project UPPEX [19]. Since the plant should also be used for teaching purposes, we chose a product that could easily be understood by an average student. We use the master data of a local bicycle producer, Hercules GmbH in Nuremberg. Thus, our model plant can be regarded as an imitation of actual bicycle manufacturing.

The item identification table of the model factory contains about 700 parts. The bills of material were set up according to the building block principle, because some of the parts, for example tread bearings, can be used in several different bicycle types and the use of this principle facilitates rescheduling. Every purchase item has a supplier. 27 supplier records were defined in total. The model company produces only to stock.

Manufacturing consists of the following departments: frame and fork production, parts production and preliminary assembly, and final assembly. The departments are divided into 23 cost centers which in turn can contain multiple work centers, 68 altogether. For some of the routings alternatives are available. In the case of frame and fork production, e.g., the options are welding and soldering. The routings contain reserve capacities (back-up work stations).

Data management and organization of the manufacturing section were designed in such a way that production in the model plant can be planned and managed by the modular IBM package COPICS (Communication Oriented Production Information and Control System) available on the university's mainframe. COPICS is a classical manufacturing resource planning (MRP) system that includes functionality from customer order servicing to shop order release and shop order load analysis. It does not cover production control, however.

SIMULEX uses these COPICS databases [15]. In addition, we assume the existence of a Leitstand (see Section 2.1) that provides the detailed schedule needed for the turnpike scheduling approach (see Section 2.3). It is a necessary enhancement since some COPICS data are too rough for rescheduling. No real Leitstand is available at our department, though.

## 3. Main components of the system

## 3.1. Overview

The basic concept for SIMULEX is sketched in Fig. 1 where dotted lines indicate future enhancements. Its core is a job shop simulator that models the plant and allows us to evaluate the results of various rescheduling measures. One intelligent front-end, the access system (AS), is used to gather information about the disturbance, to generate possible actions, and to configure the simulation experiments. Another front-end, the termination/interpretation system (TIS), analyzes the data, derives some conclusions and suggests the most promising measures. A third KBS, the run time control (RTC), supervises the simulation runs.

While the tasks of the AS and the TIS are rather straightforward, the definition of the performance criteria and the design of the analysis phase need further explanation.

According to the turnpike scheduling paradigm, the quality of a rescheduling measure is mainly determined by its ability to return to the original plan. This can basically be measured by its tardiness, assuming that a detailed schedule has been provided in which each operation was assigned a precisely determined due date. While the deviations from these planned completion times have to be considered individually, the primary decision criterion becomes tardiness.

It would be insufficient as the only decision criterion, however. Capacity usage, throughput and flow times as well as costs have to be considered, too. Thus, SIMULEX's selection process consists of two distinct phases:

☐ In phase one, the alternatives that exhibit the best performance with respect to tardiness are selected. This can be viewed as a relative comparison. It is carried out by the RTC which incorporates the first part of the TIS, called SIMULEX-A1.

☐ In phase two, the remaining candidates are analyzed by absolute criteria such as throughput or average inventory. Return to plan is also considered. This helps to detect situations in which none of the measures yields satisfactory results and where complete replanning may become necessary. This is the task of SIMULEX-A2, the second part of the TIS.

The division is further supported by the fact that compensation between tardiness and the other performance measures is hard to establish.

One could argue that in a hybrid situation of job and batch shops as in our environment, other performance measures play an important role as well (e.g., inventory levels, fill and ready rates and probability of meeting demand from stock). In general, it is not difficult to add these criteria to the existing performance measures. Quite the opposite, the very design as a multi-criteria DSS eases this step. Since the decision process is divided into two separate stages, it would mean simply replacing the decision model for one iteration (see Section 3.5.1) by another module.

## 3.2. Sketch of a SIMULEX consultation

Fig. 2 illustrates the phases of a SIMULEX consultation. The following paragraphs describe the tasks of the various components and mention the sections where they are explained in more detail.

A consultation starts with the notification of a disturbance. At the moment, the production manager has to initiate the process. Instead, SIMULEX could monitor the state of production and decide by itself when to take action.

First, the system tries to classify the disruption. The user is only asked for data that SIMULEX cannot derive by itself. Afterwards, all operations and machines affected by the problem are determined (see Section 3.3.1).

Using this information, all rescheduling measures that seem applicable for this kind of disturbance are tested. For this purpose, missing measure-specific

![](/api/attachments/65MCY35W/fulltext/images/6701384130de69fa19feac44f701aa698789d171f75e0038f7f4e3e417c17fb5.jpg)  
Fig. 1. SIMULEX.

![](/api/attachments/65MCY35W/fulltext/images/c7c4480842732d4d30e37b6e83961de49c90fc532a48761d210f41cc9fa92d4e.jpg)  
simulation runs: 45 confidence level: 70 %  
Fig. 2. Phases of a SIMUEX consultation.

data are retrieved from the user, parameter values are adjusted using domain-specific knowledge, and benefits as well as the required effort are estimated (Section 3.3.2).

With respect to the user's preferences for particular measures, orders or machines, SIMULEX chooses the most promising ones and defines a simulation model common to all alternatives (Section 3.3.3).

The modified schedules are processed by the simulator which respects several important environmental influences and records some key criteria for each run (Section 3.4).

The run time control supervises the simulation runs. It evaluates the results of each replication according to tardiness (Section 3.5.1) and stops the simulation if the required confidence level has been reached or the user requests an immediate termination. Considering the data gathered so far, the RTC determines the set of alternatives passed to the TIS for further examination using a special subset selection algorithm (Section 3.5.2).

The TIS starts with a statistical analysis of the simulation data. The evaluated criteria include production-oriented measures as well as tardiness (Section 3.6.1). Then, the TIS develops a profile for each alternative based on some selected values. This list of individual strengths and weaknesses can be presented in various styles and levels of detail. The production manager can also sort it in different ways (Section 3.6.2).

With the aid of this information, the production manager selects a rescheduling measure. If the results are unsatisfactory so far, a new consultation can be started using the conclusions already drawn (e.g., no additional workload for a certain work center).

## 3.3. The access system

## 3.3.1. Disturbance classification

To speed up the generation process, only rescheduling measures that seem feasible should be considered. Therefore, it is necessary to classify the disturbance according to its cause and effects, because the possible reactions can be grouped in such a manner.

At first, the production manager has to report the kind of disturbance to SIMULEX. According to the production factor classification, there are four classes with several groups of impairments:

\- human work: worker is absent or working incorrectly

\- equipment: facility breakdown, missing working materials or errors at the facility

\- material: material is missing, wrong material, faulty material (rework is possible), or faulty material (rework is impossible)

\- disposition: internal disposition fault or external influence, e.g., change of order or rush order

Possible consequences include capacity loss, scrap, rework, and delay.

Intelligent check-lists and different levels of a help system support the production manager in classifying the disturbance correctly (see Fig. 3). The result of this process is a three-digit disturbance code that is used to select suitable reactions.

![](/api/attachments/65MCY35W/fulltext/images/198112eb20700ccd1a6fcab7b78fffc28535d9ba7df0b0df4f7d101e541b33bc.jpg)  
Fig. 3. Disturbance classification.

Afterwards, the parameters specifying the impairment are sampled, e.g., the number of the facility and the estimated duration of its breakdown. A general classification of the disturbance according to its effects on the schedule cannot be given at this time because its consequences depend on the rescheduling measures which will be chosen later. For this reason, the rating will be carried out by the agents representing the different measures.

Furthermore, the user can specify important orders and machines he or she wants to observe. Finally, he or she has the possibility to adjust the simulation scope and the simulation depth. These parameters indicate the number of alternatives which should be investigated.

## 3.3.2. Method agents

SIMULEX knows different kinds of rescheduling measures. Each of these is represented by its own knowledge base (called a “method agent”) containing all information about one measure. In our opinion, this is a classical task for an expert system [23]. The agents use forward and backward chaining to determine results. They all share the same design principles. Fig. 4 gives an overview of the various steps carried out by an agent together with an example of a measure.

Most agents need data in addition to those sampled in the disturbance classification process. It is not only used for an applicability check, like in the case of alternative production methods, but also to determine the solution space. The number of splits cannot exceed the tools at hand, e.g., for this reason, each agent acquires the additional information needed for the measure it represents in a first step. In our example, the agent searches the COPICS shop resource database for available backup machines marked as “active”.

![](/api/attachments/65MCY35W/fulltext/images/1c4cdf1a5acd4d71baafb3a2474911ef4453f870762c4996a35f676b44a339ad.jpg)  
Fig. 4. Steps of a method agent.

Using this information, it checks whether this kind of rescheduling action fails due to the actual state of production. For example, when splitting or overlapping operations the resulting lot size may not fall below a given minimum. In this case, the agent stops immediately. For the use of backup machines, the capacity available on these machines is crucial.

If the measure has not been discarded, its parameters, e.g., overlap time or splitting key, have to be adjusted. When rerouting operations, the decisions are which operations to process on which machines in what order. The agent uses remaining free capacity versus workload per order to assign machines and tries both COPICS order priority and planned finishing date to insert jobs into the queues. In this process, an order may also be split up. A dedicated “sub-agent” carries out this task, depending on how each order is affected by the disturbance (almost finished, in progress, not started yet, etc.).

In the third step, the data which have changed with respect to the plan must be stored for the simulation. This is accomplished by alterations of the original order set such as splitting one order into several new ones or using alternative routings, as it would be done in our example.

Finally, the agent estimates the quality of the measure used as a criterion by the dispatcher to select those measures which will be simulated. It is expressed in a score ranging from 0 (not applicable) to 10 (disturbance is completely avoided without additional effort). The decision is based on both expense and yield. The latter is calculated as the ratio of the workload effectively reassigned and the workload of all orders rescheduled by the measure.

It is identical for all agents. The effort comprises various components, always including the resulting delay of all orders (rescheduled or not). When rerouting orders to backup machines, no other influence is considered.

Additional effort includes costs for overtime or increased risk when delaying maintenance. In most of these cases, it is necessary to interact with the user to get some qualified estimates, e.g., if the effort required to activate a backup machine is considered high, medium or low.

The measures are selected through an intelligent check-list using the disturbance code established earlier. A reference table contains suitability classifications for each measure and problem. One purpose of this table is to assure that the agents called are appropriate. For example, working overtime does not solve problems caused by missing stock. Another object is to group agents that defend a specific influence regardless of its cause.

The implemented measures fall into several categories:

□ Methods used to handle problems caused by human work include a worker serving more than one machine and the usage of backup personnel. In the latter case, if the missing person cannot be replaced directly due to insufficient capabilities, the system also considers exchanging workers' assignments to machines to meet the qualification requirements.

☐ Agents that try to avoid capacity loss at the disturbed machine are introduction of overtime, delay of maintenance, and reordering of operations. In addition, jobs may be rerouted to parallel or backup machines, again in combination with methods that increase capacity.

□ Then, it is possible to reduce flow time by increasing an order's priority, reducing its inter-operation times, or by splitting and overlapping.

□ Finally, the order's quantity can be decreased by using available stock, external purchase or, in the last resort, by changing the quantity delivered to a customer.

We also investigate the use of combined agents. Here we assume that a single method often yields unsatisfactory results while a combination of methods will work better. Agents representing these measures use the results of the methods applied individually to determine if a combined usage makes sense. In this case, they call the corresponding agents again with new parameters.

## 3.3.3. Dispatcher

It is the dispatcher's task to configure the simulation experiments. At first, it has to choose the measures to be simulated. In a typical consultation,

SIMULEX will generate around 30 alternatives, too much to simulate under most circumstances.

On the other hand, the production manager might not want all alternatives to be considered. Some valid choices may become infeasible due to other influences, like overtime being rejected because of prior workload. Therefore, the production manager has the option to disregard any proposal which is in turn deleted from the solution set.

The number n of candidates to be simulated is determined by the time budget for a decision and whether the system should try to test a great variety of measures at a lower confidence level or rather concentrate on a few.

Our decision model requires a known maximum number of replications, depending on the size of the candidate set and the probability requirement (see [6] for tables). The possible number of replications can be calculated based on an estimate of the time for one simulation run and the time remaining.

Using this information the dispatcher chooses a suitable combination of a confidence level and a candidate number n. Then, all possible actions are ranked according to their score reported by the method agents, and the first n are chosen.

To make the simulation results comparable, it is necessary to test all alternatives with the same simulation model. To prevent the simulation from becoming unnecessarily large and time-consuming, the model should include only those machines and orders that are likely to be affected by the disturbance. Therefore, all machines and orders reported back by the chosen agents are used to construct one simulation model, trying to exclude all orders where ample slack time will probably keep delays from proliferating.

## 3.4. Job shop simulator

The job shop simulator represents the production of bicycles. We have tried to model all relevant details of the manufacturing process, so it is possible to take into account very short standard operating times which occur at punch stations.

The time components of one operation considered by the simulator correspond to those regarded by COPICS. These are transport, waiting and set-up times, some even distinguished to a greater degree.

Additional waiting time can be caused by missing stock, for example.

Inter-operation times (e.g., for cooling) are taken into account when the order's start time on the following machine is determined. Routing simulation allows flexible rescheduling when assigning work centers so that it is possible to use parallel or back-up machines. Delivery of purchase items has also been modeled. The policy according to which waiting orders can occupy a work center is PFIFO. This means that jobs are ordered first by priority, then by time of arrival. Preemption is not allowed. The simulator can correctly handle cases like simulation start or end time falling within a break.

Using several random number generators, scrap ratios and machine breakdown times are calculated. During the processing of one lot, several breakdowns may occur.

A general problem encountered in this type of simulation is that the simulated system is itself affected by the simulation results. In the case of SIMULEX, a breakdown occurring in the “real” job shop would probably cause a consultation resulting in measures like overtime, etc. It would be desirable for the simulator to work in the same way, calling SIMULEX from within the simulation, which in turn would start additional simulation runs.

We have decided to use a very simple approach in our prototype instead. When a breakdown occurs within the simulation, no particular action is taken. All operations on the machine are delayed for the calculated duration. Thus, the simulator predicts further plan deviations in a worst-case scenario.

Some exemplary purposes for the simulation results are:

• determine work center bottlenecks

• reveal stock mismanagement

• analyze the consequences of machine breakdowns

• analyze the consequences of changes in priority

• analyze the consequences of differing shifts

\- analyze the consequences of changed lot sizes, splitting keys and overlapping production

## 3.5. Run time control

This component of SIMULEX forces simulation runs of the job shop simulator until a set of suitable alternatives has been detected with sufficient probability. Information is then passed to the TIS which analyzes it and finally presents its recommendation to the user. We need such a component because of the special decision model chosen.

SIMULEX looks at individual orders and the operations that constitute them. The task is to find the method yielding the least difference between planned and actual completion dates for all orders. If each operation is considered as a separate criterion and the goal is to minimize the deviation from a given vector of completion dates, a multi-attribute decision making (MADM) problem does result. It is multi-attribute rather than multi-objective because the set of alternatives is finite and predetermined. This problem has to be solved under uncertainty since the simulation incorporates stochastic influences and the resulting vector of completion time differences for each alternative varies from run to run.

Several restrictions led to the special SIMULEX decision model. First of all, our problem is to order and select candidates. Using standard multiple analysis of variances (MANOVA) methods to compare the means of performance measures, we can only deduce whether the alternatives show the same performance or not. Even if the distinction can be made with a specified probability, the same does not hold for any ordering of the candidates (see [17] for a good explanation of this often misunderstood conception).

Statistical procedures to rank alternatives usually require very stringent assumptions concerning the distribution of the performance measure within the candidate set. These include normal distribution or the same distribution shape in terms of skewness and standard deviation. None of these prerequisites can be assumed to be valid in our case.

We base the decision if one alternative is better than another not on a single number, but on the deviation vector. The components of each vector (the different order's deviations from the plan) are stochastically dependent because the orders are competing for the same resources. Furthermore, no averages are calculated, so a normal distribution is unlikely. As with any other multi-dimensional problem, no natural order of the alternatives is given.

Since it is very difficult to rank and select alternatives under these conditions, we decided to break down the decision problem into two distinct subproblems. The first one is an elaborate comparison of all alternatives based on the completion times of an individual order for one simulation run using deterministic MADM (see Section 3.5.1). In a second step, these decisions are combined across all experiments by a multinomial subset selection procedure to filter out the best ones (see Section 3.5.2). This type of procedure offers great flexibility and does not assume any specific underlying probability distributions. The disadvantage of our approach is low performance compared to traditional ranking and selection methods.

The RTC is responsible for these tasks. It initiates a new simulation round for all alternatives. Using the MADM procedure, it selects a winner for each round (were all results are treated as deterministic) and awards it one point. Repeating these steps, each alternative is finally assigned a winning probability. The distribution of these probabilities amongst the alternatives is multinomial. A stopping rule determines if additional replications are necessary and assures that the selection process is terminated within the given time frame. A selection rule chooses the set of alternatives for final analysis. Fig. 5 depicts this process graphically.

![](/api/attachments/65MCY35W/fulltext/images/d7158cd517cd7c6621c662979c62b362aa4d0ee6150c056acbcec5ef855d29fd.jpg)  
Fig. 5. Design of the RTC.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
means $\mathrm{A_i}$ is strictly preferred to $\mathrm{A_j}$  
[2] $0 &lt; p_{1}(\mathrm{A}_{\mathrm{i}},\mathrm{A}_{\mathrm{j}}) &lt; 1$  
represents a weak preference of $\mathrm{A_i}$ over $\mathrm{A_j}$  
[3] $p_{1}(\mathrm{A}_{\mathrm{i}},\mathrm{A}_{\mathrm{j}}) = 0,$  
depicts a situation in which $\mathrm{A_i}$ is not preferred t to $\mathrm{A_j}$  
[4] $p_{1}(\mathrm{A}_{\mathrm{i}},\mathrm{A}_{\mathrm{j}}) = 0 = p_{1}(\mathrm{A}_{\mathrm{j}},\mathrm{A}_{\mathrm{i}},$  
indicates indifference between $\mathrm{A_i}$ and $\mathrm{A_j}$
</div>

## 3.5.1. Decision model for one replication

After an evaluation of several MADM models, we chose the outranking approach of PROMETHEE (Preference Ranking Organisation Method for Enrichment Evaluations [5]). This class of procedures tries to avoid aggregation of all criteria at the beginning of the process, allows restricted compensation between good and bad criteria values and offers a high degree of freedom in modelling the user's likes and dislikes with the help of preference functions.

The following paragraphs outline the PROMETHEE principle and show the adjustments chosen for SIMULEX.

3.5.1.1. The PROMETHEE methods. Let $A_{1}, \ldots, A_{k}$ be alternatives to be ranked according to the (without loss of generality) m real-valued criteria $(\mathbf{k}_{1}(\mathbf{A}_{i}), \mathbf{k}_{2}(\mathbf{A}_{i}), \ldots, \mathbf{k}_{m}(\mathbf{A}_{i}))$ . The goal is to maximize the value $w_{i,1} = k_{1}(A_{i})$ of alternative $A_{i}$ with respect to criterion $k_{1}$ simultaneously for all criteria.

For each criterion a relative weight $g_{1}$ and a preference function $p_{1}, 1 \leq 1 \leq m$ , must exist. The preference functions $p_{1}: A \times A \to [0,1], 1 \leq 1 \leq m$ , represent the degree to which the decision maker prefers two alternatives according to the criteria $K_{l}$ : $[1] p_{1}(A_{i}, A_{j}) = 1$ ,

The weight vector $\mathbf{g} = (g_1, \dots, g_m)$ is normalized such that $\Sigma g_1 = 1$ .

The preference functions do not need to be linear and can include threshold values and indifference zones (see [5] for an overview of commonly used functions). One of the values $p_{1}(A_{i}, A_{j})$ and $p_{1}(A_{j}, A_{i})$ is always zero. By separately considering dominance of $A_{i}$ over $A_{j}$ and vice versa, unwanted compensation when combining several criteria is avoided.

With the help of these data, the values $outr_{i,j}$ of the outranking relation of alternative $A_{i}$ relative to alternative $A_{j}$ are calculated and combined in an outranking matrix of dimension $k \times k$ :

$$
\operatorname{outr} _ {i, j} = \sum_ {l = 1} ^ {m} g _ {l} \cdot p _ {l} \left(w _ {i, l}, w _ {j, l}\right).
$$

The outranking relation can be represented as a graph (see Fig. 6), where

\- the vertices $\mathbf{A}_{\mathrm{i}}$ of the graph represent the alternatives,

\- and the directed arcs from $\mathbf{A}_i$ to $\mathbf{A}_j$ with label $\text{outr}_{i,j}$ show the outranking relation.

Starting from this graph, the following values are calculated for each alternative:

☐ The leaving flow $\mathrm{F}^{+}(\mathrm{A}_{\mathrm{j}}) = \sum_{i=1}^{\mathrm{k}} \mathrm{outr}_{\mathrm{j},\mathrm{i}}$ . It is defined as the sum of the values of all arcs leaving $A_{j}$ and indicates the degree to which $A_{j}$ dominates the other alternatives.

☐ The entering flow $F^{-}(A_{j})=\sum_{i=1}^{k}\text{ourt}_{i,j}$ . The entering flow contains all values of arcs entering $A_{j}$ and describes how $A_{i}$ is outranked.

☐ The net flow $F(A_{j}) = F^{+}(A_{j}) - F^{-}(A_{j})$ . It serves as a simple but rough indication of the decision maker's preference for alternative $A_{j}$ .

The PROMETHEE methods offer several possibilities to deduce a global preference structure from these flows.

The preference relation $\succ^{(1)}$ for PROMETHEE I is constructed by comparing the elements of the two-dimensional vector $(\mathbf{F}^{+}(\mathbf{A}_{i}), -\mathbf{F}^{-}(\mathbf{A}_{i}))$ and applying the resulting half order in $\mathbb{R}^2$ so that:

$$
\mathrm{A} _ {\mathrm{i}} \succ \mathrm{A} _ {\mathrm{j}} \Leftrightarrow \binom{\mathrm{F} ^ {+} (\mathrm{A} _ {\mathrm{i}})}{- \mathrm{F} ^ {-} (\mathrm{A} _ {\mathrm{i}})} > \binom{\mathrm{F} ^ {+} (\mathrm{A} _ {\mathrm{j}})}{- \mathrm{F} ^ {-} (\mathrm{A} _ {\mathrm{j}})}
$$

In this relation, incomparable alternatives can exist. They correspond to situations in which neither preference nor indifference seem sufficiently justified. Between such candidates, a decision can be made only by using additional criteria or by random selection.

PROMETHEE II avoids incomparable alternatives by resorting to net flows and the canonical order in $R^{1}$ :

$$
\mathrm{A} _ {\mathrm{i}} \succ \mathrm{A} _ {\mathrm{j}} \Leftrightarrow \mathrm{F} (\mathrm{A} _ {\mathrm{i}}) > \mathrm{F} (\mathrm{A} _ {\mathrm{j}}). \tag {2}
$$

The total order is achieved by a rather high loss of information and by an evaluation that is less accurate than that of PROMETHEE I. Still it is often used because of its simplicity. The ranking is unambiguous, one can select among the “best ones” at random.

![](/api/attachments/65MCY35W/fulltext/images/a59b457431234ad8de4161fba22857a8523cbe2d7e6da24caa630bc242aa3cd2.jpg)  
Fig. 6. The outrangking relation as a graph.

SIMULEX could use both relations. Since only a best candidate has to be selected for one simulation round (see Section 3.5.2), it seems appropriate to arbitrarily choose one of the non-dominated solutions under PROMETHEEI. As this method preserves more of the information than PROMETHEEII, it was implemented.

3.5.1.2. Adjusting PROMETHEE parameters for SIMULEX. We wanted to individually evaluate earliness and tardiness of an order with respect to the schedule by suitable weights and preference functions. Therefore, they are treated as separate criteria. The resulting problem is to minimize all criteria simultaneously. If the order is finished on time, both numbers are set to zero, otherwise the corresponding element contains the absolute value of the deviation.

Thus, several production philosophies can be modeled. If the production process does not follow the just-in-time concept, for example, earliness can be disregarded by setting the corresponding weight to zero or by using a large indifference zone in the preference function.

Preferences between orders due to tardiness or earliness do not depend solely on the differences but also on the absolute values because we have to differentiate more in the case of small deviations (minutes) than in the case of large ones (several days). Therefore, SIMULEX-A1 transforms the performance differences via the preference functions. Usually, not all deviations that can be measured technically are of practical importance. A lower threshold for each criterion describing an indifference zone does reflect that. Completion dates falling within this area are regarded as finished according to plan. An upper threshold indicates values that are intolerable. If an alternative's value exceeds this margin, every other alternative that does not exhibit the same behaviour is strictly preferred. Within these borders, preference increases uniformly with the unweighted completion date deviation.

Two classes of orders exist in the model plant. Customer orders are routed to customer order services (COS) storage, while orders that stay within the plant are sent to manufacturing requirements planning (MRP) stock. Delivery on time to customers is mainly determined by the COS orders' end delays. Starting dates, completion dates of the individual operations and flow times of the MRP orders are most important for costs and capacity usage. As they are separately considered by the TIS, SIMULEX-A1 only uses the orders' end delays and pays special attention to the COS orders. An alternative that results in all customer orders being finished on time should be strictly preferred to an alternative that shows almost no deviation in the MRP orders but delays a COS order.

Therefore, the following adjustments for the two classes were chosen:

□ COS orders:

\- The absolute end delay of an order is analyzed.

\- This is done by using “real-time” including work-breaks, weekends, etc., since they are important for a customer delivery.

\- Each order gets the same weight as all MRP orders combined. For n COS orders, the respective weight is 1VERSMn + 1.

□ MRP orders:

\- If the deviation was calculated based on the absolute end delay of an order, any lag caused in an earlier step would appear again in all following operations. Therefore, the net delay occurring in this step is used.

\- It is calculated in net working time excluding all breaks, since only this time is important within the factory.

\- The delays are given a low weight because they should influence the decision only in the second place. The sum of all MRP weights amounts to $\frac{1}{n+1}$ as well. Within this class, the relative importance can be determined by an internal priority established via the MRP system, or by using an order's production quantity or available stock.

The tolerance thresholds for the preference functions also vary by the type of order. For COS orders, absolute values are used, for MRP orders, the values depend on available stock.

These parameters have to be adjusted to the plant under consideration. In order to include actual developments (like limited stock capacity), the production manager should be able to change them online from the terminal.

## 3.5.2. Combination of the several decisions

As already explained in Section 3.5, we decided not to use one of the usual ranking methods based on one-dimensional normal distributions. Instead of trying to base a decision on the averages of some performance indices, we take the different approach of figuring out the rescheduling measure with the highest chance of winning in a series of deterministic simulation experiments. This corresponds to a very natural principle of selecting an alternative that has performed well in a number of comparable situations.

For this purpose, a best alternative is chosen for each simulation round. The winner is awarded one point. Ties can be broken by random selection. As this process is repeated, each candidate is assigned a winning frequency and finally a winning probability. The distribution of these probabilities among the alternatives is multinomial, which causes the algorithms to be named multinomial selection procedures (see $[11-13]$ for an overview). They select a group of most promising candidates with the danger of not including the real “winner” that can be specified beforehand.

The probability of a correct choice depends on the actual winning probability distribution. By identifying a least favourable configuration for each algorithm, it is possible to estimate the number of replications necessary for a certain confidence level, depending on the number of alternatives to consider. Using these information, tables for the procedures were prepared.

This approach has several advantages: The performance measures, e.g., do not have to meet any statistical requirements and the selection step is entirely independent of the evaluation model. Thus, both can be developed and improved independently. Its main drawbacks are a relatively low performance so that many replications are needed, and the fact that the selection procedures can divide the set of populations only into two classes: good and bad ones. But this is just what is required for SIMULEX.

We decided to implement a subset selection method developed by Chen [6] that is based on an algorithm by Gupta and Nagel [14]. Using the tables for various configurations, a maximum number of runs is determined. After these replications have been carried out, the candidate with the highest “score” is selected alongside with all alternatives having a distance smaller than a parameter D. By adjusting D (and thus the size of the subset) one can balance sharpness of inference and number of experiments required. Furthermore, the algorithm stops if a clear winner emerges during the course of the experiments, improving the performance of the original Gupta and Nagel method.

The simulation ends when the ranking procedure terminates, the time limit is reached, or the user requests an immediate stop. In all cases, the confidence level reached is calculated, all estimators are updated, and the results gathered so far are stored. They can be used to improve predictions by additional simulation runs in case the results are unsatisfactory.

## 3.6. Termination / interpretation system

The result of the simulation runs is a set of alternatives which have the highest probabilities of best maintaining the original schedule. At this stage, no further differentiation between these measures is possible. This is carried out by SIMULEX-A2, the second part of the TIS, which statistically analyzes the “secondary” operational criteria as its first task.

## 3.6.1. Criteria considered

The criteria evaluated by the TIS include mean flow time and throughput of the job shop, utilization, idle times, and work-in-progress levels for individual machines as well as waiting times, number of set-up and transport operations for each order, etc. Besides these rather usual measures, SIMULEX-A2 analyzes additional criteria.

An aspect considered due to the stochastic simulation is stability. It describes how strong the measure's results differ across several simulations and determines the degree to which its behavior can be relied on. For this purpose, we use mean and standard deviation of a criterion to calculate its confidence interval, indicating the range its value can be predicted with a specific probability [17]. This is called the characteristic criterion of the alternative. Additionally, the frequency of an occurrence, measured by the percentage of all simulation runs which were favourable for a certain aspect, is used to quantify stability.

The criterion “costs” incorporates all costs that can be influenced by choosing one alternative and can be measured with satisfying accuracy. These are calculated by using a combination of direct costing and activity-based costing. Besides the usual cost drivers parts, work, scrap, transports etc., we also include costs for the measures themselves, which indicate the effort necessary to implement them.

![](/api/attachments/65MCY35W/fulltext/images/a8a09d3a2b85e8807c93302644905c092cd8ec9f25d3ec3d30febd081bda0c81.jpg)  
Fig. 7. Recommendation of an alternative.

One of the more advanced measures is the so-called return to plan. It expresses the very goal of turnpike scheduling. A detailed evaluation of each order's tardiness and its consequences determines whether a state has been reached in this simulation run (and at what time) where the observed schedule matches the planned completion dates. For example, return to plan has not been accomplished if the delay of an operation expands to other job shop orders or to another production area, or if a customer order due date is threatened.

The central idea is robustness. It describes how far an alternative pushes production to its limits and makes it prone to further disturbances. An example would be a solution that requires heavy usage of safety stock. This can be an important hint for the production manager to reject an alternative. If such a measure is taken, it indicates what he should keep an eye upon. Robustness cannot be expressed in a single number, but we have identified main influence factors, depending on whether a return to plan was possible or not. The most important of these influences make up the critical success factors for a measure. In the SIMULEX prototype, the time of return to plan, its frequency and the average number of bottleneck machines and stock shortages are used to describe the robustness of an alternative.

## 3.6.2. Presentation of the results

After the statistical analysis has been carried out, the termination/interpretation system has to draw some conclusions and finally to present a concise recommendation in textual or graphical form to the user. The criteria mentioned in the preceding section are used in the presentation of the results. The user can choose between:

• the recommendation of an alternative

• the evaluation of all alternatives

• the presentation of the various criteria

The recommendation tries to identify the most promising rescheduling measure. First, the user has to specify how high the probability of return to plan should be for a measure to be considered. Since small deviations from the plan can be tolerated most of the time, a tolerance (standard: 12 minutes) is used in the analysis. If more than one candidate remains, a second criterion is used. Possible choices are the time of return to plan or costs. Several recommendations on the basis of different parameters are possible. Fig. 7 gives an example.

The evaluation accompanies the recommendation. For each alternative, it lists the same criteria as chosen for the recommendation and allows the production manager to make his own comparisons at a very high level.

For a more detailed analysis, all performance measures recorded in the simulation can be presented individually. For each aspect, the user can look at one alternative solely or at all alternatives in comparison. In addition, the lists can be restricted to elements unfavorable for a measure, e.g., only the negative deviations from the plan can be shown.

## 4. Implementation aspects and some results

## 4.1. Technical details

SIMULEX is a large system, containing more than 2,300 parameters, 1,900 rules and 106 user screens just in the front-ends. The intelligent front-ends were implemented in the Expert System Shell ESE [16] and PASCAL, while the job shop simulator was realized with GPSS-FORTRAN.

We chose these programs because we already had experience with them from related projects and they are all well-known and in use for some time. Another aspect was that they all run on the department's IBM 3090. When we started the development, no other knowledge tools could access the mainframe databases. We then decided to carry on with the somewhat outdated tool until a first prototype was finished. Our latest plans, however, call for porting the intelligent front-ends to a workstation so that the SIMULEX environment is realistic.

The programs facilitate integration by two mechanisms: First, FORTRAN and PASCAL programs can be called from ESE, with parameters being passed back and forth. Second, since the introduction of a new COPICS release, all three programs have access to SQL databases. Therefore, we can easily incorporate the planned information from COPICS and store the simulation results in a structured manner.

Due to the slow implementation tools and a constant utilization of the department's mainframe above 80 percent, run times range from 7 to 10 hours, far too long for a real-world system. Also, the user interface needs some cosmetic refinement.

However, the quality of the results is encouraging. Unfortunately, a systematic test is impossible because we cannot automatically generate several consistent COPICS data sets representing various production problems. To accomplish this, we would need a real plant or a special type of simulator that could also create new orders, start COPICS planning runs and the like.

## 4.2. Test results

For the reasons mentioned above, we had to test plausibility of the system using special cases input manually. For our test cases, all measures suggested and all conclusions drawn seemed reasonable in light of the given data. Also, the simulation led to different conclusions than the method agents had forecast beforehand, showing the necessity of additional analysis.

Furthermore, we asked several colleagues specialized in the field of production control to solve one of the test rescheduling problems. With the help of a questionnaire, we compared their problem solving approach and results with the system's. It turned out that SIMULEX was comparable in every aspect. The system proposed the same measures and considered the same criteria when evaluating their applicability. In some cases, the human decision makers were inclined to use more complicated alternatives than the computerized system. Especially, they combined more partial solutions whereas SIMULEX used fewer basic measures. They generally accepted the system's proposals, but their preliminary ranking of the measures differed from the ratings of the method agents.

When confronted with the simulation results, the human decision makers tended to question their favourite solutions, and they reranked the alternatives. The information provided by the system satisfied their requirements. A remarkable difference was found in the main criterion used to finally select a measure from SIMULEX's proposals when the alternatives were comparable in terms of the resulting delay. The “production managers” mainly based their decision on costs whereas SIMULEX stressed robustness.

All in all, SIMULEX was attested “reasonable” behavior.

## 4.3. Comparison with other approaches

We have deliberately tried to build SIMULEX as an add-on to an existing MRP system instead of the more common approach to design the whole system from scratch. Therefore, we had to accept the deficiencies of the available data and their non-optimal structure. We had to include a virtual Leitstand, for example, to get detailed schedules. On the other hand, our system integrates well within an existing production planning environment, so that very little additional strain is put on the production manager. It is crucial for good results that the data represent the actual state of production, calling for automated shop floor data collection.

Compared to a mere production simulator, the front-ends mean an enormous additional effort. But it seems well-justified, as the production manager's ability to generate rescheduling alternatives himself is extremely limited by the amount of data he would have to collect first. This collection and the generation of alternatives in such a variety is one of SIMULEX's strengths. And even if the production manager was able to generate solutions, he would still need a front-end to analyze the simulation results.

In comparison to UMDEX, a pure KBS for rescheduling also developed at our department [19], the simulator offers much better information about the resulting schedules. The simulation eases the analysis of influences that spread through the order network. In addition, our decision model provides a good way of incorporating uncertainty. As the simulation results often differed from the deterministic evaluations of the method agents (that comprise a conventional KBS for rescheduling), it seems to be a valuable addition. We are concerned about the implied double effort since the same problem (resulting delay of orders) is both forecast deterministically by the method agents to estimate an alternative's score and calculated in detail by the simulator. But this is not a principle design flaw. It is merely caused by the slow simulation runs that force us to restrict the alternatives considered.

## 5. Conclusion

In the previous sections, we have sketched how simulation can be utilized by a broader range of persons through the use of intelligent front-ends to interface to the user and shield him from its pitfalls. We think we were able to indicate the potential of this approach that is by no means restricted to manufacturing problems.

The high computing power requirements will become less of a hindrance as CPU speed increases and new AI tools become more efficient.

Our plans for the future include production scheduling capabilities for SIMULEX. Producing a new schedule in turn can be seen as a feasible rescheduling alternative. Hence, an agent “schedule specified machines” could submit its proposal alongside the “turnpike-oriented” ones. Thus, the rescheduling capabilities of SIMULEX could be enhanced as well. Another topic is the possibility to parallelize SIMULEX. In our opinion, this can be done to a great extent, speeding up the decision process significantly. Therefore, we conclude that knowledge-based simulation can indeed solve manufacturing problems.

## Acknowledgements

This research was supported by the Deutsche Forschungsgemeinschaft (DFG), grant no. ME 241/10. We would like to thank Hercules GmbH, Nuremberg, who provided us with the master data from their production plant.

## References

[1] H. Adelsberger and J.J. Kanet, The Leitstand: A New Tool for Computer-Integrated Manufacturing, Production and Inventory Management 32 No. 1 (1991) 43–48.

[2] J.C. Bean and J.R. Birge, Match-Up Real-Time Scheduling (Department of Industry and Operations-Engineering, University of Michigan, 1985).

[3] B.D. Becker and W. Dangelmaier, EXCON: An Expert System to Construct Control Strategies for Simulation Systems in Manufacturing, in: R. Crosbie and P. Luker, Eds., Proceedings of the 1986 Summer Computer Simulation Conference (The Society for Computer Simulation, San Diego, CA, 1986) 731–736.

[4] R. Belz, SIMULEX: Solving Rescheduling Problems By Knowledge-based Simulation, in: W. Krug and A. Lehmann, Eds., Proceedings of the 1992 European Simulation Symposium, Simulation and AI in Computer-Aided Techniques (The Society for Computer Simulation, San Diego, CA, 1992) 371–375.

[5] J.P. Brans, B. Mareschal and Ph. Vincke, PROMETHEE: A New Family of Outranking Methods in Multicriteria Analysis, in: J.P. Brans, Ed., Operational Research '84 IFORS (North-Holland, Amsterdam, 1984) 477–490.

[6] P. Chen, Truncated Inverse Sampling Procedure for Multinomial Subset Selection, Technical Report No. S-41 (Department of Mathematics, Syracuse University, New York, 1987).

[7] W. Dangelmaier, A. Keller, U. Mussbach-Winter and H. Wiedenmann, Kapazitätsorientierte Auftragsbildungsverfahren, Zeitschrift für wirtschaftliche Fertigung und Automatisierung 84, No. 12 (1989) 676–680.

[8] W. Dangelmaier, H. Kühnle and U. Mussbach-Winter, Einsatz von künstlicher Intelligenz bei der Produktionsplanung und -steuerung, CIM Management 6, No.1 (1990) 4–12.

[9] D.R. Ford, Combining Simulation and Artificial Intelligence: A Practical Example, in: C.C. Barnett and W.M. Holmes, Eds., Proceedings of the 1988 Summer Computer Simulation Conference (The Society for Computer Simulation, San Diego, CA, 1988) 648–652.

[10] M.S. Fox and K.G. Kempf, Complexity, Uncertainty and Opportunistic Scheduling, in: Ch. Weisbin, Ed., Second Conference on Artificial Intelligence Applications (IEEE Society Press, Washington, DC, 1985) 387–392.

[11] D. Goldsman, On Selecting the Best of K Systems: Expository Survey of Indifference-Zone Multinomial Procedures, in: S. Sheppard, U. Pooch and D. Pegden, Eds., Proceedings of the 1984 Winter Simulation Conference (North-Holland, Amsterdam, 1984) 107–112.

[12] D. Goldsman, A Multinomial Ranking And Selection Procedure: Simulation And Applications, in: S. Sheppard, U. Pooch and D. Pegden, Eds., Proceedings of the 1984 Winter Simulation Conference (North-Holland, Amsterdam, 1984) 259–264.

[13] D. Goldsman, B.L. Nelson and B. Schmeiser, Methods for Selecting the Best System, in: B.L. Nelson, W.D. Kelton and G.M. Clark, Eds., Proceedings of the 1991 Winter Simulation Conference (The Society for Computer Simulation, San Diego, CA, 1991) 177–186.

[14] S.S. Gupta and K. Nagel, On Selection and Ranking Procedures and Order Statistics from the Multinomial Distribution, Sankhya: The Indian Journal of Statistics, Series B, No. 29 (1967) 1–34.

[15] IBM Corporation (Ed.), COPICS Relational Database Guide, IBM-Form 5688-143, 1990.

[16] IBM Corporation (Ed.), Expert System Environment: Reference Manual, IBM-Form SC38-7004-04, 5th ed., 1990.

[17] A. Law and W.D. Kelton, Simulation Modeling and Analysis, 2nd ed. (McGraw-Hill, New York, 1991).

[18] J.M. Mellichamp and Y.H. Park, A Statistical Expert System for Simulation Analysis, Simulation 52, No. 4 (1989) 134–139.

[19] P. Mertens, J. Helmer, H. Rose and Th. Wedel, Ein Ansatz zu kooperierenden Expertensystemen bei der Produktionsplanung und -steuerung, in: K. Kurbel, P. Mertens and A.W. Scheer, Eds., Interaktive betriebswirtschaftliche Informations- und Steuerungssysteme (de Gruyter, Berlin, 1989) 13–40.

[20] R. O'Keefe, Simulation and Expert Systems: A Taxonomy and some Examples, Simulation 46, No. 1 (1986) 10–16.

[21] H.V.D. Parunak, Manufacturing Experience with the Contract Net, in: Distributed Artificial Intelligence 1 (M. Huhns, Pitman, London et al., 1988) 285–310.

[22] H. Pierreval, Data Analysis Oriented Techniques for Learning about Manufacturing Control with Simulation, in: H. Muller, R. Reddy and S. Takaba, Eds., Proceedings of the European Simulation Multiconference: Simulation in the Factory of the Future and Simulation in Traffic Control (The Society for Computer Simulation Europe, Gent, 1988) 61–66.

[23] R.C. Schank and P.G. Childers, The Cognitive Computer. On Language, Learning and Artificial Intelligence (Addison-Wesley, Reading, MA, 1984).

[24] E. Schmitt, Werkstattsteuerung bei wechselnder Auftragsstruktur, Ph.D. Dissertation (Universität Karlsruhe, Karlsruhe, Germany, 1989).

[25] B.J. Schroer, F.T. Tseng, S.X. Zhang and J.W. Wolfsberger, Automatic Programming of Manufacturing Simulation Models, in: C.C. Barnett and W.M. Holmes, Eds., Proceedings of the 1988 Summer Computer Simulation Conference (The Society for Computer Simulation, San Diego, CA, 1988) 569–574.

[26] P. Tajanithi, S. Manivannan and J. Banks, A Knowledge-Based Simulation Architecture to Analyze Interruptions in a Flexible Manufacturing System, Journal of Manufacturing Systems 11, No. 3 (1992) 195–214.

[27] S.D. Wu, R.H. Storer and P.-C. Chang, One-Machine Rescheduling Heuristics With Efficiency and Stability as Criteria, Computers and Operations Research 20, No. 1 (1993) 1–14.

[28] S. Zelewski, Expertensysteme in der Prozeßplanung und -steuerung in der Fabrik der Zukunft — Ein Überblick über Konzepte und erste Prototypen, Working Paper No. 22, Seminar für Allgemeine Betriebswirtschaftslehre, Industriebetriebslehre und Produktionswirtschaft (Universität Köln, Köln, 1988).

[29] G. Zimmermann, Neue Ansätze zur Strukturierung von PPS-Systemen — Erwartungsbezogene und kundenauftragsorientierte Disposition, Fortschrittliche Betriebsführung/Industrial Engineering 38, No. 2 (1989) 72–85.

[30] G. Zimmermann, PPS-Methoden auf dem Prüfstand: Was leisten sie, wann versagen sie? (Verlag moderne Industrie, Landsberg am Lech, 1987).

![](/api/attachments/65MCY35W/fulltext/images/025aa60863d7d298bc48ca8eb2149bb56b4cfc638180a27bc117bf93e9077696.jpg)

Peter Mertens is Professor of Business Administration at the University of Erlangen-Nuremberg and heads the Department of Information Systems. He received his Ph.D. from the University of Darmstadt in 1961. His main areas of interest include computer-assisted selling, MRP systems, EDP systems in logistics, DSS in business planning and knowledge-based systems.

![](/api/attachments/65MCY35W/fulltext/images/7ec4f72a060f1c31025ffface1eaef49619949b61a521a2a37e26c9b650519af.jpg)  
Reimund Belz was a member of Professor Mertens' Department from 1989 to 1993, where he led the research group for production planning and control. His work focused on decision support systems for production control combining discrete event simulation and knowledge-based systems. Mr. Belz received his Ph.D. in 1993 and is now working as an internal consultant at the Deutsche Bank head office in Frankfurt.
