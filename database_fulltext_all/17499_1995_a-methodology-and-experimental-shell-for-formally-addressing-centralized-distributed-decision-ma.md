---
otero_id: 17499
otero_key: "4FG2YDFE"
title: "A methodology and experimental shell for formally addressing centralized/distributed decision making choices"
authors: "Shung-Kuang Kung; James R. Marsden"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00038-t"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A methodology and experimental shell for formally addressing centralized/distributed decision making choices $*$

Shung-Kuang Kung ${}^{a,*}$ , James R. Marsden ${}^{b,c}$

$^{a}$ Department of Management Information Systems, College of Business, Chung-Yuan Christian University, Chung-Li, Taiwan $^{b}$ Department of Operations and Information Management, School of Business Administration, University of Connecticut, 368 Fairfield Road, U-41 IM, Storrs, CT 06269-2041, USA

$^{c}$ Department of Decision Science and Information Systems, College of Business and Economics, University of Kentucky, Lexington, KY 40506-0034, USA

## Abstract

Managers seeking optimal organizational design require a means for choosing between centralized and distributed decision making processes. We provide a methodology for modelling and subsequently comparing centralized and distributed decision making processes. A detailed example of the implementation of all but the final stage of this methodology is provided using the context of a flexible manufacturing system (FMS) environment. An adaptable experimental shell and interface is set forth and initial experimental results are used to illustrate our methodology. We also illustrate how experimental results can be used in the development of automated bidding systems (“expert” systems) for use in subsequent simulations for comparing the performance of centralized and distributed decision making alternatives.

Keywords: Distributed decision making; Methodology; FMS; Laboratory experiments

## 1. Introduction

Optimal organizational design requires numerous determinations of whether to utilize centralized or distributed decision making processes. Even in quite hierarchical organization structures, particular decision making processes may be optimally formulated as distributed decision making environments. The research presented here provides a methodology for modelling and, subsequently, comparing centralized and distributed decision making processes. Our discussion concentrates on a flexible manufacturing system (FMS) environment. The methodology presented, however, apply to diverse centralized versus distributed decision making choices in organizations. We emphasize the general nature of our approach in summary comments in section 5. We provide a detailed example of the implementation of all but the final stage (comparison of simulation results) of this methodology in the context of a flexible manufacturing system (FMS) environment.

Historically, FMS scheduling has been most often approached as a centralized decision making process with a centralized scheduler attempting to determine an optimal (or at least satisfactory) decomposition of jobs into tasks and assignment of tasks to specific machines. Hsu, Prietula, Thompson, and Ow [6] summed up this central scheduling problem as follows: Due to the complex and interacting nature of constraints, preferences, and unpredictability of the scheduling environment, practical scheduling tasks in many firms are too complex to be solved by explicit numerical methods alone. [p. 332]

Even for rather limited FMS, centralized optimal scheduling can be a complex problem defying direct solution. Previous authors e.g., [1,8,12,13] have suggested the potential for the use of contract-nets in such environments. We employ the term contract-net to refer to a structure where the system problem is decomposed by a manager into sub-problems which are auctioned across the network to contractors for solving or for further decomposition (that is, contractors can act as managers). Such contract-nets represent a decentralized and distributed decision-making process.

Section 2 provides details of our development and implementation of a contract-net shell for use in analysing FMS scheduling and, in general, analysing centralized vs. distributed decision making processes. After presenting our contract-net shell, we demonstrate its operation using induced value controlled laboratory experiments involving FMS settings where individual nodes are operated by individuals, each provided with a decision support system (DSS). Section 3 describes the experimental methodology we followed while section 4 provides initial experimental results. This section also incorporates a discussion of the next step in our methodology: the use of expert system bidding models (constructed based upon the induced value experimentation results) in simulations comparing the performance of the distributed contract-net to various heuristics for centralized scheduling.

![](/api/attachments/4FG2YDFE/fulltext/images/a0709d667791b097b7ef11f6896d62bdaec74066943c4311744e77504d7d1295.jpg)  
Fig. 1. Research overview.

## 2. The contract-net shell

Comparing centralized and distributed decision making requires formal modelling and analysis of each. While other studies detailed the performance of various heuristics for centralized FMS scheduling (see, for example, [2], [3], [5], [7], and [11]), we are not aware of comparable distributed process information. We describe below the formulation and implementation of a contract-net which we developed to fill this gap.

## 2.1. General formulation

We sought to develop a system of problem-solving centres where system problems could be distributed (shared) among the centres for solutions. Further, we wanted a system that was sufficiently flexible so that eventually we could straightforwardly modify the system to study problem complexity, problem-solving centre capabilities, cooperation requirements, performance measures, and reward mechanisms. Fig. 1 provides an overview of our continuing research effort using the contract-net shell and interface we developed. The figure provides an outline of the structure of our contract net, provides examples of the types of controls (such as incentives, team decision structures, idiosyncratic opportunities, authority and rules, performance ambiguity and cooperation requirements) that may be imposed and studied, and highlights three particular research issues. As noted earlier, our discussion is in the context of FMS scheduling. The latter part of our current presentation provides an illustration of the process for development of expert bidding systems. The third research issue (comparison simulations) noted in Fig. 1 is briefly mentioned at the end of section 4. This area is the focus of continuing research.

There are three roles in the contract-net: manager, agent, and middleman. The manager is responsible for monitoring and providing incentives and/or penalties to impact the behaviour of agents in the system. Once incentives and/or penalties are specified, the manager can be a fully automated system that may or may not be made subject to human control. Individual agents are responsible for determining bids and for performing and completing tasks won (“awarded”) in auctions run by the manager. Each agent is supported by a decision support system (DSS) providing up-to-date information on machine capabilities (and associated costs), machine status, machine/task/bidding history, queue status, auction announcements, and auction time remaining. The middleman (not operationalized in the examples presented here) allows a number of agents to compete as a team with combined resources and production capabilities. The middleman acts as an agent to the system manager and as a manager to the agents on his/her team, but possesses no production capability.

In this decentralized process, the mapping of a problem to a solution is executed in the form of an auction. In centralized FMS scheduling, the manager searches through the solution domain and attempts to assign the problems (tasks) to agents who can perform them most efficiently. The manager in our system announces tasks for auction, records bids, and awards tasks to low bidders if relatively straightforward constraints are met. In even rather small scale centralized systems, the manager must deal with significant data storage and update intricacies. Further, the centralized system manager must repeatedly attempt to solve NP-complete scheduling problems. In the decentralized, distributed decision-making environment of our contract-net, the local bidder (human or expert system) has knowledge only of operations at the local node and of the auction rules. Local information (machine activity, machine breakdown, queue sizes, and profit) are updated each period and presented in a DSS to each bidder. The only external information maintained and updated locally is the amount of previous winning bids on tasks auctioned and awarded.

## 2.2. Production process and job decomposition

In our contract-net shell, goal decomposition prepares tasks for auction in a sequence that maintains all precedence relations. In typical production processes, jobs consist of more than one task and involve tasks which cannot be performed until one or more other tasks have been completed. Hence, before a job is sent to a production system for processing, the order and time of releasing tasks for completion must be properly determined (i.e., precedence constraints must be maintained). Since it would be redundant to have each assigned agent maintain the same precedence relationships, we had the automated manager perform the releasing procedure.

Consider the job as a tree. The component tasks that can be processed without violating the precedence constraints are the leaf tasks of the job tree. Using the tree diagram to describe the relationship of all the tasks in a job, each node (including the leafs) in the tree represents one task in the job, and the root node represents the completion of the job. If two tasks are directly connected with an arc, then there is a precedence relationship between these two tasks. The one farther from the root must be completed before the one closer to the root can start. Therefore, those tasks without any precedence constraint are at the edge of the tree and indicated as leaf tasks. These leaf tasks can be processed immediately without violating any precedence constraint.

Our job decomposition procedure can be viewed as trimming the tree leafs. Since leaf tasks have no precedence constraint, they can be processed all at once. When any of these leaf tasks are completely processed, the job tree is then updated by removing the completed leaf tasks from it. If we view the original tree as one generation and the updated tree as the next generation, the younger generation tree is a subset of the older generation tree. Also, some of the intermediate nodes (those node tasks with their precedence constraints unfulfilled) in the older generation tree may now become leaf tasks in the younger generation tree (due to the fulfilment of their precedence constraints) and become available for processing. By repeating these procedures of processing leaf tasks, collecting completed tasks, and updating the tree, all tasks of the job can be processed in their proper order with precedence constraints satisfied.

A production process typically incorporates three phases in addition to job decomposition: task distribution, task execution, and task synthesis. We briefly consider each in turn.

![](/api/attachments/4FG2YDFE/fulltext/images/5c0308748d3cb4958d57f406a9a7f9abe28516e0c54f6eade3a2faa254e34214.jpg)  
Fig. 2. Example auction screen with bids entered.

![](/api/attachments/4FG2YDFE/fulltext/images/86a02b9e8f09fb944b94c5e6eb1cec5eee0eb2ae5caad674076f2d777af88ad7.jpg)  
Fig. 3. Example auction screen with F5 pop-up activated.

## 2.3. Task distribution

Task distribution is accomplished through an auction of tasks which arrive from three sources: (1) leaf-tasks of new jobs, (2) tasks of old (existing system) jobs with precedence constraints met, and (3) tasks which must be re-bid because of machine breakdown or queue constraint violation by an agent. When a new job arrives, the corresponding precedence constraint file is reviewed

![](/api/attachments/4FG2YDFE/fulltext/images/b2d7be4cb5f62157038ac5720d77d56826dbc44bcfd1dd4dc0c7760e229acc44.jpg)  
Fig. 4. Example auction screen with F8 pop-up activated.

![](/api/attachments/4FG2YDFE/fulltext/images/21c27fb98fb0da4be169f8626a3fe3bd1712be401d4803a1bc01032aa85fd6e9.jpg)  
Fig. 5. Example task history review pop-up auction screen.

and the leaf-tasks are collected and prepared for auction. Prior to the announcement of an auction, the system is queried by the auctioneer to determine status of previously awarded tasks. Tasks with precedence constraints completed are made available for auction in the upcoming period. Finally, if machine breakdown or queue constraint violations occur, previously assigned tasks are collected for re-bid.

![](/api/attachments/4FG2YDFE/fulltext/images/5ab48efea08bdd43363ee7806f11eabcb8ee7009c242fc923758b8f962532760.jpg)  
Fig. 6. Example winning-bid summary pop-up auction screen.

## 2.4. Task execution

Task execution is guaranteed by individual agents that win performance rights in the auction process. Each agent is provided with a local DSS and interface (see Figs. 2–6 and accompanying descriptions) to aid in bid preparation and subsequent machine assignment (details infra). After collecting all agents' bids (including blank or "nobid") for each auctioned item, the auctioneer selects the agent with the lowest positive bid on each task as the "winner" of that task. When an agent is awarded a task, the agent chooses the machine at his/her station that will perform the task. An issue being addressed in our continuing research is whether we can identify a level of complexity (machine/task combinations) at which the difficulty of local scheduling problems results in the contract-net being a consistently relatively poor choice for task assignment and scheduling.

Production cost is used to compute agent profits or losses and run time is used to compute tentative completion time. When a task is assigned, the tentative completion time is set in one of the three following ways:

(1) if the assigned machine is idle, tentative completion time is set equal to run time;

(2) if the assigned machine is busy and queue space is available, tentative completion time is set equal to the remaining run time for the task in process plus the run time for all tasks in the queue plus the run time for the awarded task;

(3) if the machine is busy and there is no queue space available, a queue constraint violation is recorded and the task must be sent back to be re-bid; no tentative task completion time is computed.

## 2.5. Task synthesis and auction process

For simplicity and with no loss of generality, we ignore formalizing task synthesis since, if the process involved any significant activity, we could treat it as an additional task that must be auctioned in the contract-net. Thus, task synthesis is assumed trivial and completed by the auctioneer.

The auctioneer follows a predefined sequence of auctioning procedures and directs the auction process by sending messages to and receiving messages from the agents in the contract-net. Table 1 summarizes the instructions (messages) sent out by the auctioneer and the responses (messages) from contract-net agents. Enrolment and system time instructions (automatic machine programmed instructions to identify participants and coordinate clock settings) prepare the system. Collecting re-bid and completed tasks along with receipt of new tasks serves to update system status and compile the upcoming set of tasks for auctioning. An announcement is then sent over the network followed by bid collection and announcement of winners (task assignments). At any necessary point during the process, message resend requests can be sent and are automatically answered.

Table 1  
Instructions and responses

<table><tr><td>Instruction from auctioneer (manager)</td><td>Response of agents</td></tr><tr><td>enrolment registration</td><td>send “ready” message</td></tr><tr><td>system time</td><td>adjust local time to system time</td></tr><tr><td>collect re-bid tasks</td><td>prepare and report re-bid tasks</td></tr><tr><td>collect completed tasks</td><td>prepare and report completed tasks</td></tr><tr><td>collect new tasks and announce auctioned items (new tasks and re-bid tasks)</td><td>make bid decisions and submit to auctioneer</td></tr><tr><td>announce winners</td><td>examine auction results for awarded tasks if any, make machine assignment decisions</td></tr><tr><td>repeat last message</td><td>send request message again</td></tr></table>

## 2.6. Prototyping process

Prototyping and structuring the local agent DSS and interface involved repeated experimentation with eight doctoral student subjects over a four month period. In this process, we carefully collected subject views concerning what information should be displayed, with information ranked for relevance and importance. Repeated screen modifications were made in attempts to locate the highest ranked information near the decision-input block or screen for convenient access. Less relevant (lower ranked) information was made available to decision-making agents via call-up features (pop-up screens). In the interface, we attempted to provide the most important information on the primary decision making screen with importance rankings determining the screen locations in terms of neighbourhoods around the decision input block. After numerous repetitions of the screen testing and screen modification cycle, the criteria of relevancy and format (location) appeared to match all subject requirements and all subjects expressed satisfaction with the final presentation design. Figs. 2 to 6 provide illustrations of the general agent screen and several of the pop-up options.

## 3. Controlled laboratory experimentation

Our methodological approach draws heavily from the induced value approach pioneered by Vernon Smith [see [14], [15], [16], and [17]; also see Plott and Smith, [10]]. Smith outlined the use of a subject reward structure incorporating sufficient monetary value to drive laboratory experiments. Smith argued that well-designed laboratory experiments, which parallel real-world situations in critical processes, have significant applications in the development and testing of theories (see [16], especially, pages 274-275). In addition to the need to carefully structure experiments so that parallelism is obtained, Smith emphasized the importance of providing sufficient motivation to influence subjects to perform.

A contract-net FMS scheduling environment as structured for our experiments is a market. Individuals are rewarded based upon performance and the goal of an individual in the system may conflict with the system or organization goal. In a contract-net FMS scheduling environment, the manager's goal is commonly focused on one or more specific criteria such as minimizing the total costs of having his/her assigned problems solved by the contractors or minimizing run-time. A contractor or bidder's goal is to maximize his/her profits from solving the auctioned problems (we specify a fixed time period). In common day-to-day markets, a buyer's goal is to minimize his/her costs, and a seller's goal is to maximize his/her profits. Due to the conflict of the goals, the sellers and buyers have to reach an agreement in order to complete the exchange. If no agreement is reached, then no exchange occurs. In our experimental settings, if bids are not below specific ceilings, then no task award is made and the relevant tasks are outsourced. That is, the tasks are treated as assigned to and completed by external vendors at a cost equal to the specified ceiling amount.

The experiments reported on in the following section are directed at analysing the functioning of the contract net. One part of this effort is an analysis of whether the contract net yields competitive market results when we structure the environment consistent with such a market. The experimental results are of interest to our work as evidence of the operation of the contract-net rather than as a result supporting previous competitive market studies by experimental economists.

## 4. Experiment and results

With the contract-net shell formulated and operational and with the guidance provided by Smith's induced value experimental formulation, we were able to conduct the experiments necessary as the initial steps of our methodology for comparing centralized and distributed decision making. Following Smith's approach, our contract-net experiments used monetary rewards including a \$5 show-up payment plus an expected mean performance payout of approximately \$7.50. Depending upon competitive performance, actual individual payments could range from a \$5 show-up amount to \$35.00. Because of the complexity of possible outcomes of the set of experiments reported in the next section, we utilized a pool reward mechanism (with queue constraints) in order to be able to control experimentation costs. In this system, individual subjects are rewarded with a percentage of the pool amount set equal to the percentage of total group profits they earned. For example, if the pool amount for four subjects is set at \$35 and if subject A earns 50% of the total profits earned by the group, then subject A receives \$17.50 plus \$5 show-up payment for a total of \$22.50 $^{1}$ .

Subjects were recruited from various pools with three groups chosen. The experiments reported are part of a lengthy project requiring the tracking of identical subject sets through numerous different experimental sets. We intentionally sought diverse groups in order to be able to address questions of the breadth of applicability of results obtained in our investigation of the operation of our contract-net. In addition, subjects had to agree to and be available for participation in repeated experimentation scheduled over at least a one-year period. We were able to develop three groups (fourteen subjects), that met the criteria just mentioned and still allowed us to remain within budget. Group 1 consisted of four staff assistants and secretaries from the college of Business and Economics. Group 2 contained four doctoral students from the Department of Decision Science and Information Systems. Group 3 was a mixed group consisting of six participants (one DSIS doctoral student, one doctoral student from the Department of Finance, two undergraduate business majors, and two departmental secretaries). Members of Group 1 had little or no background in our research issues, members of Group 2 had considerable relevant background but no direct involvement, and members of Group 3 had mixed background familiarity.

Our experiments were in the form of sequential sealed-bid simultaneous first-price auctions. In our sequential simultaneous auctions, there were several auction periods with one or more items auctioned in each auction period. Participants submitted their bids to the auctioneer through a local area network, and participants with the low bid on each auctioned task were selected as the winners. Winning bids were announced to all participants but only the winners knew what items they had won. When two or more participants had the same lowest bids, the one who submitted first was selected as the winner. During the experiments, participants were not allowed to directly communicate with each other in any form.

Each experiment included several auction periods. To keep experiment time to approximately one hour, we conducted thirty-six periods for Group 2 and twenty-five periods for Groups 1 and 3. During each experimental period, participants had two minutes to make bid decisions regardless of how many bids decisions were to be made. For each task, participants could choose to submit either a no-bid or a dollar amount bid for any auctioned task which they had machines capable of performing. Available decision time was displayed and continually updated on each participant's workstation in seconds, which decreased until the time remaining reached zero. If any participant failed to make and enter all bid decisions before the available decision time reached zero, the system submitted bids automatically. When this occurred, the system submitted bids for a participant as follows: (1) if an auctioned task's bid was partially entered or left empty, the system submitted a bid indicating the participant was not competing for that task, and (2) if an auctioned task's bid was fully entered, the system submitted the entered bid for that task without the participant's confirmation.

Each participant acted as the operator of an individual node containing a set of machines with each machine being able to perform one or more tasks. Differing numbers of machines associated with differing number of production capabilities in each machine created different decision making complexities. For example, if we wished to study a fully competitive structure, each participant could be provided an identical set of machines. That is, all participants in a fully competitive structure would be equally capable of performing every announced task. On the other hand, in an idiosyncratic environment, each participant would have at least one machine which possessed a unique production capability (no one else in the system would have the same capability). Through repeated auctions in a given setting, participants can learn about the structure of the environment. For example, participants are able to learn about their idiosyncratic capabilities and can seek to maximize profits by fully utilizing their idiosyncratic power. However, each experimental session involved a randomly selected structure so that participants were not able to obtain increased performance through learning across sessions.

Reserve bids were set for all tasks. For each task, the reserve bid (outsourcing price) was set equal to production cost plus a value randomly drawn from a specified normal distribution with mean thirty. We expected bids on competitive tasks to go close to production costs as competition drove bids downward. To avoid infinite pay-offs, we restrained participants in our experiments by setting a reserve bid for each task such that each bid had to be lower than the corresponding reserve bid in order to be eligible for competition. If not, then the reserve bid was triggered (the task was “out-sourced” to external vendors).

Each machine in a local station was provided with queuing capability but the permissible size of the queue could be restricted. Participants could have their awarded tasks waiting in a local queue for processing if the assigned machine was busy. However, the number of tasks allowed to wait in the same queue was limited to three in this experiment. A penalty (\$10 in experimental dollar) was charged when this restriction was violated and the tasks involved were automatically sent back to the auctioneer to be re-bid.

In comparing our experimental results, we measured the performance by the percentage of maximum available profits (equal to the sum, for all auctioned tasks, of reserve price minus production cost) actually attained. We randomly rearranged each machine's production capability, production cost, and reserve bids for each group and across experiments. This was done to prevent information revealed in one experiment being used in a subsequent experiment. Since each task's production cost and reserve bid were different in each experiment, the maximum profit margin allowed varied from experiment to experiment making total costs an undesirable measure of participants' performance. Therefore, we sought a transformation of experimental results to a basis such that reasonable comparisons could be made. We chose to measure performance as net percentage gain of total available profits. That is, we used the following equation to measure the participants' performance:

$$
\text { Performance } = \left(\mathrm{B} _ {\mathrm{i}} - C _ {i}\right) / \mathrm{P} _ {i},
$$

where

$$
\mathbf {B} _ {\mathrm{i}} = \text { winning   bid   of   task   i }
$$

$$
\mathrm{C} _ {\mathrm{i}} = \text { production   cost   of   task   i }
$$

$$
\mathrm{P} _ {\mathrm{i}} = \text { maximum   available   profit   of   task   i }
$$

(reserve bid or outsourcing price for task i

minus the production cost for task i).

For the experiment reported on below, each participant was provided with the same machines with the same production capabilities $^{2}$ . Each group was tested in two experiments. In experiment one, each participant had two machines and each machine was capable of performing four different tasks (this environment is referred to as 2M4T). In experiment two, each participant had four machines and each machine was capable of performing two different tasks (this environment is referred to as 4M2T). In addition to the randomizing of experiments discussed earlier, we also switched the order of experiments to check if performance was different in the second experiment, possibly as a result of learning in the first experiment. Hence, we arranged our experiments in the following sequence: Groups 1 and 2 were tested in 2M4T first then in 4M2T; Group 3 was tested in 4M2T first then in 2M4T. Tables 2 and 3 list machine production costs in 2M4T and 4M2T, respectively.

Three performance comparisons were made. We first studied the participants' performance in environments with different decision complexities by comparing their performance in 2M4T with their performance in 4M2T. Second, to investigate changes in the performance with different numbers of competitors, we compared the performance of the four-participant (4P) groups (i.e., Groups 1 and 2) with the performance of the six-participant (6P) group (i.e., Group 3) in the same decision complexity environment (i.e., 2M4T and 4M2T). Third, we compared consecutive interval performances in the first and second experiments. To study the effect of learning, we compared each group's consecutive interval performances in their first experiments (i.e., 2M4T for Groups 1 and 2, and 4M2T for Group 3), and then compared their consecutive interval performances in their second experiments (i.e., 4M2T for Groups 1 and 2, and 2M4T for Group 3).

Results were compared for three intervals, with each interval containing eight auction periods. The averages of net profit percentage gains for these intervals are reported in Table 4. The net profit percentage gains for each auction period are presented in Fig. 7. As noted earlier, Groups 1 and 2 first participated in experiments 2M4T followed by 4M2T. Group 1 had average net profit percentage gains in 2M4T at a profit level of 0.0438 which decreased in the subsequent intervals to 0.0120 in interval 2, and 0.0007 in interval 3. In their second experiment, these participants started at a profit level equal to 0.0003, and maintained profit levels close to this level throughout the second experiment (0.0002 for the subsequent two intervals). In Group 2's first experiment, average net profit percentage gains were at 0.1527 in the first interval and quickly fell to 0.0011 in interval 2 and 0.0003 in interval 3. In their second experiment, Group 2 started at a profit level of 0.0003 in interval 1 and maintained this average net profit gains at the same level through out the second experiment. Group 3 displayed the same pattern as the Groups 1 and 2 did. In their first experiment, 4M2T, participants started their profit levels at 0.0034, decreased to 0.0006 in interval 2 and to 0.0002 in interval 3. In their second experiment, their profit level began at 0.0002, decreased to 0.0001 in interval 2, and went back to 0.0002 in interval 3. Their average net profit percentage gains in each interval are presented in Figs. 8 and 9.

Table 2  
Production costs in 2M4T

<table><tr><td></td><td>Task 1</td><td>Task 2</td><td>Task 3</td><td>Task 4</td></tr><tr><td>Machine 1</td><td>54.25</td><td>61.60</td><td>58.40</td><td>65.75</td></tr><tr><td>Machine 2</td><td>60.05</td><td>56.60</td><td>63.40</td><td>59.95</td></tr></table>

Such experimentation is but the first step in our methodology for studying distributed versus centralized decision making. A complete methodology requires the development of means for comparing the performance of the distributed process (contract-net) to the centralized process (central scheduler). Under a wide variety of alternate production settings, we suggest the following:

Table 3  
Production costs in 4M2T

<table><tr><td></td><td>Task 1</td><td>Task 2</td></tr><tr><td>Machine 1</td><td>54.25</td><td>60.05</td></tr><tr><td>Machine 2</td><td>61.60</td><td>56.60</td></tr><tr><td>Machine 3</td><td>58.40</td><td>63.40</td></tr><tr><td>Machine 4</td><td>65.75</td><td>59.95</td></tr></table>

(1) Develop automated bidding systems that can be used as individual bidders at each node of the contract-net; these systems would be constructed as “expert systems” with observed bidding behaviour being the basis for rule development;

(2) Determine the set of known FMS centralized scheduler results (heuristics and specific cases where heuristics have been applied);

(3) Run simulations of these cases for contract-net using expert system bidders and compare results for measures of interest including total cost (including costs of developing and maintaining central scheduler versus cost of developing and maintaining contract-net) and run time.

Consider the following analysis of participants' response to the previous outcome. Our findings are summarized in Table 5 where when participants won the object previously, 30 out of 112 times they then submitted bids higher than their previous bids, 10 out of 112 times they submitted bids lower than their previous bids, and 72 out of 112 times they submitted the same bids. On the other hand, if they did not win the objects, 71 out of 363 times they submitted bids higher than their previous bids, 129 out of 363 times they submitted bids lower than their previous bids, and 163 out of 363 times they submitted the same bids. When they won the objects previously, $73\%$ of times they submitted bids higher than or equal to their previous winning bids. When they lost the objects previously, $80\%$ of times they submitted bids equal to or lower than their previous losing bids. Post experiment interviews with experimental subjects indicated that most of the participants used the winning bids and losing bids as their bids' upper and lower bounds. That is, if a participant won an object and the winning bid

Table 4  
Even interval average net profit percentage gains

<table><tr><td></td><td>Interval 1</td><td>Interval 2</td><td>Interval 3</td></tr><tr><td rowspan="3">Group 1 2M4T</td><td> $\overline{X} = 0.0438$ </td><td> $\overline{X} = 0.0120$ </td><td> $\overline{X} = 0.0007$ </td></tr><tr><td> $S^{2} = 6.7E-4$ </td><td> $S^{2} = 1.6E-4$ </td><td> $S^{2} = 5.9E-7$ </td></tr><tr><td>N = 14</td><td>N = 17</td><td>N = 20</td></tr><tr><td rowspan="3">Group 1 4M2T</td><td> $\overline{X} = 0.0003$ </td><td> $\overline{X} = 0.0002$ </td><td> $\overline{X} = 0.0002$ </td></tr><tr><td> $S^{2} = 9E-22$ </td><td> $S^{2} = 2.1E-8$ </td><td> $S^{2} = 2.2E-8$ </td></tr><tr><td>N = 10</td><td>N = 10</td><td>N = 12</td></tr><tr><td rowspan="3">Group 2 2M4T</td><td> $\overline{X} = 0.1527$ </td><td> $\overline{X} = 0.0011$ </td><td> $\overline{X} = 0.0003$ </td></tr><tr><td> $S^{2} = 0.0236$ </td><td> $S^{2} = 1.1E-6$ </td><td> $S^{2} = 1.2E-8$ </td></tr><tr><td>N = 14</td><td>N = 16</td><td>N = 23</td></tr><tr><td rowspan="3">Group 2 4M2T</td><td> $\overline{X} = 0.0003$ </td><td> $\overline{X} = 0.0003$ </td><td> $\overline{X} = 0.0003$ </td></tr><tr><td> $S^{2} = 9E-22$ </td><td> $S^{2} = 9E-22$ </td><td> $S^{2} = 9E-22$ </td></tr><tr><td>N = 9</td><td>N = 13</td><td>N = 11</td></tr><tr><td rowspan="3">Group 3 2M4T</td><td> $\overline{X} = 0.0002$ </td><td> $\overline{X} = 0.0001$ </td><td> $\overline{X} = 0.0002$ </td></tr><tr><td> $S^{2} = 2.4E-8$ </td><td> $S^{2} = 2.2E-8$ </td><td> $S^{2} = 1.6E-8$ </td></tr><tr><td>N = 10</td><td>N = 14</td><td>N = 18</td></tr><tr><td rowspan="3">Group 3 4M2T</td><td> $\overline{X} = 0.0034$ </td><td> $\overline{X} = 0.0006$ </td><td> $\overline{X} = 0.0002$ </td></tr><tr><td> $S^{2} = 1.4E-5$ </td><td> $S^{2} = 3.1E-7$ </td><td> $S^{2} = 2.0E-8$ </td></tr><tr><td>N = 8</td><td>N = 11</td><td>N = 11</td></tr></table>

$\overline{\mathbf{X}} =$ average net profit percentage gains.  
$S^{2}=$ variance of net profit percentage gains.  
N = number of competitive tasks announced.

Group Interval Performance  
![](/api/attachments/4FG2YDFE/fulltext/images/2d8be0d63c5ff0d07ed0f4c7849b3792d91592fcecad86a350bac8525faf2f9c.jpg)

![](/api/attachments/4FG2YDFE/fulltext/images/13baf2baf84de62fbd2319d4eb85d9ec77fbec68b7b674d0a86958347943427b.jpg)

![](/api/attachments/4FG2YDFE/fulltext/images/c1a4c32c7ed19c34ddf58ed65d2f8d979e8770a4dedd0a3ddd8e7b074f7b4aa4.jpg)  
Fig. 7. Group performances periods by periods.

Group Performance Comparison in 2M4T  
![](/api/attachments/4FG2YDFE/fulltext/images/47185c2364c2a1b71269cf4e7ab1e0c7662e03072984b6e99759cd8f87f1c84f.jpg)  
Fig. 8. Group even interval performance comparison in 2M4T.

Group Performance Comparison in 4M2T  
![](/api/attachments/4FG2YDFE/fulltext/images/fc6c64ec5be4781c3545bde7171ebac8cf4310374acb830da6b7a292e8de26c7.jpg)  
\* Note: Figure below presents the same Group Even Interval Comparison as shown in Figure above but using a smaller scale.

Group Performance Comparison in 4M2T\*  
![](/api/attachments/4FG2YDFE/fulltext/images/c074986d4027e2607c95820e4cf2e0b14e428db628e8afd54f32258969a2c61b.jpg)  
Fig. 9. Group even interval performance comparison in 4M2T.

was higher than his/her current lower bound, he/she then adjusted his/her lower bound equal to this winning bid. If the previous bid was a losing bid, and the announced winning bid was between the upper bound and lower bound, he/she then adjusted his/her upper bound equal to this announced winning bid. If the announced winning bid was lower than the lower bound and higher than the cost, he/she then adjusted his/her upper bound to the announced winning bid and his/her lower bound to the cost.

We could summarize this information in the form of the following rule set which might be used in the formulation of the needed expert bidding system:

Rule set 1: (in auction mode)

(1) If optimal bid is found, submit optimal bid.

(2) If optimal bid is not found, randomly submit a bid between the lower and upper bounds.

Rule set 2: (in awarding mode)

(1) If current result is winning bid, set bounds as follows: randomly draw a response from a multinomial distribution of $f$ (u, d, e; 0.27, 0.09, 0.64); if response is:

Table 5  
Summary of participants' response to previous auction result

<table><tr><td></td><td>Last result</td><td>Higher</td><td>Lower</td><td>Same</td></tr><tr><td rowspan="2">Competitive tasks</td><td>win</td><td>30/112 (27%)</td><td>10/112 (9%)</td><td>72/112 (64%)</td></tr><tr><td>loss</td><td>71/363 (20%)</td><td>129/363 (35%)</td><td>163/363 (45%)</td></tr></table>

(1.1) u: set lower bound to current winning bid and increase upper bound by the same margin as the lower bound increased (i.e., the margin increase is the range between lower bound and the winning bid).

(1.2) d: set upper bound to $\frac{1}{4}$ of current margin (i.e., new upper bound = current upper bound - $\frac{1}{4}$ (current upper bound - current lower bound)).

(1.3) e: keep the same upper and lower bounds.

(2) If the current bids are losing bids, set bounds as follows: randomly draw a response from a multinomial distribution of $f$ (u, d, e; 0.20, 0.35, 0.45); if the response is:

(2.1) u: set new upper bound = current upper bound + $\frac{1}{4}$ (current upper bound - current lower bound).

(2.2) d: if the announced winning bid $\geq$ lower bound and $\leq$ upper bound, set upper bound = the announced winning bid.

(2.3) if the announced winning bid is less than the lower bound but higher than the cost, set upper bound to the announced winning bid and set lower bound to the corresponding cost.

(2.4) e: keep the same upper and lower bound.

(3) If upper bound equals lower bound, set optimal bid to lower bound.

This rule set can be viewed as a learning mechanism in our automated bidding or “expert” system. The purpose of this learning mechanism is to search for the optimal bids (from an agent’s perspective). The system learns by adjusting the upper and lower bounds for each object in response to auction outcomes, and these upper and lower bounds are adjusted toward optimal bids. For idiosyncratic tasks, there is no competition and the reserve bids are the optimal bids. Our winning bids adjust lower bounds upward to the optimal bids, and our losing bids adjust upper bounds downward to the reserved bids. When upper bounds equal the corresponding lower bounds, we have located the optimal bids and no adjustment is to be made afterwards. For competitive tasks, due to competition, any increase in bids decreases the probability of winning and often results in losing. These losing bids adjust upper bounds downward to the cost, and eventually the optimal bids ( $\approx$ cost) are located. However, we are not suggesting that these rules represent any bidding expert's decision-making process. These rules represent reasonable fits of our experimental subjects' behaviour. They are consistent across three distinctly different subject groups (once short term learning has occurred), and they serve to illustrate a way of operationalizing a knowledge based contract-net formulation in an FMS scheduling environment.

Once performing arrays of such systems are constructed, our methodology involves simulations for comparing the performance of the distributed contract-net environment to the centralized scheduler environment. This research is currently in progress and will be reported in upcoming presentations.

## 5. Summary remarks

In the preceding sections we have outlined a methodology for systematically addressing the centralized/distributed decision making issue, and provided a detailed illustration of the operationalization of several critical steps in fully implementing this methodology. Our experimentation was set in an FMS environment and involved the issue of utilizing a central scheduler (centralized decision making) using global knowledge or a contract-net with distributed agents making decisions using only local knowledge and knowledge of winning auction bids.

The methodology involves the modelling of the environments, the implementation of the environments (in our case as an electronic auction market for the contract-net), the performance of relevant experimentation and/or simulation. As such, our methodology is actually a compilation of processes and techniques that are frequently used in differing areas. As organizations themselves draw from and utilize the contribution of many areas, our methodology for considering issues within organization design and structure does likewise. We have set our discussion within one environment, FMS scheduling, where there exists an important centralized/distributed decision making issue. This is certainly only one of many such settings, but the methodology we have illustrated in not limited to FMS scheduling. Three steps are required: the modelling of the environments, the implementation of the environments, and the performance of relevant experimentation and/or simulation. Surely the difficulty of pursuing the methodology will vary across the settings. There are perhaps many settings that will pose substantial difficulties. We argue, however, that this methodology aids us to go beyond speculation. It enables us to formally and rigorously address the centralized/distributed decision making choice.

## Acknowledgements

The authors would like to thank Dr. Ram Pakath, Ming-Chian Ken Wang, Kimlynn Marsden, and two anonymous referees for several helpful discussions and suggestions.

## References

[1] A.D. Baker, Complete Manufacturing Control Using a Contract Net: A Simulation Study, IEEE International Conference on Computer Integrated Manufacturing (1988) pp: 100–109.

[2] Y.L. Chang and R.S. Sullivan, Real-Time Scheduling of Flexible Manufacturing Systems: A Conceptual And Mathematical Foundation, presented at ORSA/TIMS Meeting, San Francisco, CA (1984).

[3] R.H. Choi and E.M. Malstrom, Physical Simulation of Work Scheduling Rules in a Flexible Manufacturing System, Computers and Industrial Engineering, Vol. 11, No. 1–4 (1986) pp: 390–394. J.C. Cox, V.L. Smith, and J.M. Walker, Experimental Development of Sealed-Bid Auction Theory: Calibrating Controls for Risk Aversion, American Economic Review, Vol. 75 (1985) No. 2, pp: 160–165.

[5] K.K. Hitz, Scheduling of Flexible Flow Shops, Report no. LIDS-R-879, LIDS, MIT, Cambridge, MA (1979).

[6] Wen-Ling Hsu, Michael J. Prietula, Gerald Thompson, and Peng Si Ow, A Mixed-Initiative Scheduling Work-

bench: Integrating AI, OR and HCI, ISDSS Conference Proceedings (1990) pp: 331–345.

[7] Andrew Kusiak, Application of Operational Research Models And Techniques in Flexible Manufacturing Systems, European Journal of Operational Research, Vol. 24, No. 3 (1986) pp: 336–345.

[8] P.S. Ow, S.F. Smith, and R. Howie, A Cooperative Scheduling System, Expert Systems and Intelligent Manufacturing edited by M.D. Oliff (1988), pp: 43–56, Elsevier Science Publishing Co. Inc., New York, New York. H.V. Parunak, Manufacturing Experience with the Contract Net, Distributed Artificial Intelligence, edited by Michael N. Huhns (1987), Morgan Kaufmann Publishers, Inc., Los Altos, California.

[10] C.R. Plott and V.L. Smith, An Experimental Analysis of Two Exchange Institutions, Review of Economic Studies, Vol. 45, No. 139 (1978) pp: 133–153.

[11] R. Rachamadugu and K.E. Stecke, Classification and Review of FMS Scheduling Procedures, Working Paper, Graduate School of Business Administration, University of Michigan (November 1986).

[12] M.J. Shaw and A.B. Whinston, A Distributed Knowledge-Based Approach to Flexible Automation: The Contract Net Framework, The International Journal of Flexible Manufacturing System, Vol. 1, No. 1, 1988, pp: 85–104.

[13] R.G. Smith, The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver, IEEE Transactions on Computers, Vol. 29, No. 12, 1980, pp: 1104–1113.

[14] V.L. Smith, An experimental study of competitive market behaviour, Journal of Political Economy, Vol. 70, No. 2, 1962, pp: 111–137.

[15] V.L. Smith, Effect of Market Organization on Competitive Equilibrium, The Quarterly Journal of Economics, Vol. 78, 1964, pp: 181–201.

[16] V.L. Smith, Experimental Economics: Induced Value Theory, American Economic Review, Vol. 66, No. 2, 1976, pp: 274–279.

[17] V.L. Smith, Bidding and Auctioning Institutions: Experimental Results, Bidding and Auctioning for Procurement and Allocation, edited by Yakov Amihud, NY University Press, 1976, pp: 43–64.

![](/api/attachments/4FG2YDFE/fulltext/images/022377f69f41db42b167b8719f8744f15c55e710851d72721e246f44b63ee1cf.jpg)  
Shung-Kuang Kung is Associate Professor of MIS at Chung-Yuan Christian University in Taiwan. Dr. Kung received his Ph.D. from the University of Kentucky in 1993 and is currently focusing his research efforts in the areas of distributed decision making, contract-net applications in FMS, and expert systems.

James R. Marsden is currently Professor and Head, Department of Operations and Information Management, School of Business Administration at the University of Connecticut. He received an A.B. from the University of Illinois, M.S. and Ph.D. from Purdue University, and a J.D. from the University of Kentucky. The founding Chair and Philip Morris Professor at the Department of Decision Science and Information Systems at the University of Kentucky, Professor Marsden has held visiting positions at the University of North Carolina, Purdue University, University of York (England), and the University of Arizona. His research interests include distributed decision processes, knowledge acquisition, management of information, management of technology, and economics of information systems.
