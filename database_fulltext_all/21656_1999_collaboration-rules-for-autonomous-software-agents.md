---
otero_id: 21656
otero_key: "9P3SF45G"
title: "Collaboration rules for autonomous software agents"
authors: "Sarosh N Talukdar"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00070-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Collaboration rules for autonomous software agents

Sarosh N. Talukdar )

Carnegie Mellon UniÕersity, Department of Electrical and Computer Engineering, Pittsburgh, PA 15213, USA

## Abstract

Can autonomous software agents that are distributed over a computer network collaborate effectively? Both empirical evidence and theory suggest that they can. Moreover, there seem to be simple rules for designing problem-solving organizations in which collaboration among such agents is automatic and scale-effective adding agents tends to improveŽ solution-quality; adding computers tends to improve solution-speed . This paper develops some of these rules for off-line. problems and argues that they can be extended for the on-line real-time control of power systems.Ž . q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Autonomous agents; Collaboration; Multi-agent systems; Organizations

## 1. Introduction

This paper deals with the skills that unsupervised Ž . autonomous software agents must have if they are to collaborate effectively. This section explains the terminology that will be used, formulates the collaboration problem and outlines an approach to its resolution.

## 1.1. Terminology

Let a ‘software agent’ be any encapsulated piece of computer code, such as a program or a subroutine. Functionally, such an agent can be thought of as a bundle of skills 5 that can be divided into three<sup>w</sup> <sup>x</sup> categories:

<sup>Ø</sup> problem solving skills which determine what the agent can do particularly, what computational Ž tasks it can perform ;.

<sup>Ø</sup> social or self-management skills which determine what the agent chooses to do particularly, how itŽ chooses to collaborate with the other information processing agents in its environment ;.

<sup>Ø</sup> and learning skills which determine how well the agent transforms its experiences into new skills.

Let:

<sup>Ø</sup> ‘An agent’s environment’ mean the set of all the things that the agent can affect or by which it is affected The environment of a software agent isŽ mediated by a computer network and may include other types of information-processing agents, particularly, humans ..

<sup>Ø</sup> ‘An off-line problem’ mean a computational problem without hard constraints on solution-time, as is the case with many design, planning, scheduling, optimization and diagnosis problems. ŽIn other words, dealing with an off-line problem involves two objectives: maximizing solution-quality and maximizing solution-speed. In contrast, dealing with an on-line or real-time problems involves only a single objective: maximizing solution-quality, but this must be done subject to deadlines, that is, hard constraints on solutionspeed..

<sup>Ø</sup> ‘Collaboration’ mean the exchange of data among information-processing agents, regardless of whether the exchange is productive or not.

<sup>Ø</sup> ‘An organization’ mean a triple whose elements are: a set of software agents, a network of computers for the agents to use, and a prescription for the agents’ collaborations. Organizations can beŽ of two types: hierarchic and non-hierarchic flat .Ž . In a hierarchic organization, the prescription for collaboration relies for its effectiveness on the delegation of responsibility: the agents are arranged in layers; those in a higher layer are made responsible for, and given supervisory authority over those in the layers below. In a flat organization, there are no supervisors. Rather, the agents are autonomous and the effectiveness of their collaborations are determined solely by their social skills..

<sup>Ø</sup> An ‘open organization’ mean an organization whose size can easily be changed by the addition or removal of agents and computers.

<sup>Ø</sup> A ‘scale effective organization’ mean an organization whose performance improves with size. Specifically, solution-quality improves with the addition of agents and solution-speed improves with the addition of computers.

## 1.2. A design problem

Existing software agents tend to be rich in prob lem-solving skills but poor in social and learning skills. Computer networks make it possible to interconnect very large numbers of software agents, and thereby, to amass enormous pools of raw problemsolving capability. How can all this capability be exploited? Of the many issues implied by this question, the subset that will be considered here is as follows.

Given:

<sup>Ø</sup> an instance of an off-line problem, and

<sup>Ø</sup> a set of software agents distributed over a computer network,

Design:

<sup>Ø</sup> an open, scale-effective organization for solving the off-line problem.

In other words, search through the space of all possible organizations for one whose size is easily increased and whose performance, on the given offline problem, improves with size.

The advantages of such an organization are easy growth and fault tolerance. Costly demolition and reengineering become unnecessary for performance improvements. Instead, the problem of improving performance reduces to one of finding which agents and computers to add. Conversely, the loss of agents or computers is likely to cause a gradual rather than precipitous decrease in performance.

## 1.3. A subspace of flat organizations

Rather than solving the design problem above, the approach taken here is to replace it with an easier problem. Specifically, the space of all possible organizations is replaced by a much smaller subspace with a much higher concentration of open and scaleeffective organizations. This subspace contains only a certain type of flat organization called an asynchronous team. These teams are always open and are often scale effective.

The subspace of asynchronous teams is defined by a constructive grammar. The two most important components of such a grammar are a set of primitives and a set of rules for composing organizations from the primitives.

The primitives of the grammar were obtained by examining a variety of existing organizations and extracting their better features. These primitives provide for agent autonomy as enjoyed by the membersŽ of some insect societies 20 , creation and destruc-<sup>w</sup> <sup>x</sup>. tion processes of adjustable strengths as in someŽ cellular communities 15 , populations of trial-solu- <sup>w</sup> <sup>x</sup>. tions as in genetic algorithms 9 , shared memoriesŽ <sup>w</sup> <sup>x</sup>. Žas in blackboards 19 , randomized selection as in<sup>w</sup> <sup>x</sup>. Ž simulated annealing 16 , lists of elements to be<sup>w</sup> <sup>x</sup>. avoided as in tabu search 12,13 , and uninhibitedŽ <sup>w</sup> <sup>x</sup>. creation as in brainstorming 21 .Ž <sup>w</sup> <sup>x</sup>.

The rules of the grammar ensure openness and ease of communication. Specifically, these rules permit only completely autonomous agents that collaborate only by modifying one another’s results. Therefore, the agents have no need for external supervision; no centralized control or planning systems need be built, nor are there are any managerial layers to impede the addition or removal of agents. Moreover, the needs for commonality of expression and representation are minimal. To illustrate, consider an agent that specializes in repairing one part of the results generated by other agents. This agent needs to know only how this part is represented. It interacts with the other agents only through its repairs.

## 1.4. Demonstrations

One might think that agents that are autonomous and know virtually nothing about one another, would tend to work at cross purposes. Nevertheless, effective asynchronous teams have been developed for a variety of off-line problems, including nonlinear equation solving 10,27 , traveling salesman prob- <sup>w</sup> <sup>x</sup> lems 11 , high-rise building design 22 , reconfig-<sup>w x</sup> <sup>w x</sup> urable robot design 18 , diagnosis of faults in elec- <sup>w</sup> <sup>x</sup> tric networks 7 , control of electric networks 1,25 , <sup>w x</sup> <sup>w</sup> <sup>x</sup> job-shop-scheduling 8 , steel and paper mill schedul-<sup>w</sup> <sup>x</sup> ing 4,17,23 , train-scheduling 28 , and constraint<sup>w</sup> <sup>x</sup> <sup>w x</sup> satisfaction 14 . Not only do these asynchronous <sup>w</sup> <sup>x</sup> teams find good solutions, but they appear to achieve scale effectiveness through fairly simple mechanisms. The succeeding material explains how and why. Specifically, Section 2 develops a framework for describing and analyzing collaborative efforts among autonomous software agents. Section 3 distills the descriptive elements of this framework into a set of primitives, and the prescriptive elements into a set of rules, of a grammar for asynchronous teams for off-line problems. Section 4 argues for the extension of this grammar to on-line real-time problems,Ž . particularly, distributed control and mixed initiative problems for electric power systems.

## 2. Definitions and models

This section develops a framework for analyzing collaborations among cyber agents, a class of agents that includes software agents as well as humans, and argues that scale-effectiveness is likely to occur in many asynchronous teams.

## 2.1. Cyber agents

The environment of the any agent can be divided into two spaces-one that the agent perceives or senses Ž . Ž its input-space , the other, that it affects its outputspace . Of course, these spaces may overlap. .

Definition 1. A cyber agent is an agent whose inputand output-spaces are maintained by computers. ŽThus, both software agents and humans who happen to be engaged in computer-mediated work, qualify as cyber agents..

Since a space is a set of objects, any computer maintained space can be thought of as a set of memories for symbolic objects. Therefore, every cyber agent in any organization of cyber agents can be modeled as:

<sup>Ø</sup> a set of computer-maintained memories from which the agent can read the agent’s input space , Ž .

<sup>Ø</sup> a set of computer-maintained memories to which the agent can write the agent’s output space ,Ž .

<sup>Ø</sup> an operator embodying the agent’s problem-solv-Ž ing skills that can copy objects from the input . memories, transform them, and write the results to one or more of the output memories, and

<sup>Ø</sup> a control system consisting of the agent’s own social skills together with any external controls, such as reporting requirements, imposed by the organization.

Note that this model captures all the operating possibilities for the software agent. But it is less complete for humans in that it allows only for computer-mediated exchanges of information.

Definition 2. A cyber agent is autonomous if its control system is completely self-contained, that is, if its social skills are its only controls.

As such, an autonomous cyber agent can do what it wants when it wants. In particular, autonomous agents can choose to work in parallel all the time, if enough computers are available.

Definition 3. A cyber agent is static if it remains at the same location in its computer network, that is, if it does not switch from one set of input or output memories to another.

Thus, there are only two tasks for the control system of a static cyber agent: selection choosingŽ the objects to be read from its input-memories and. scheduling determining when the operator will work Ž on the selected objects and which of the available computers it will use for this work ..

Definition 4. The work-cycle of a cyber agent consists of the following sequence: read copy a set ofŽ . objects from its input-memories, modify these objects, and write the results to one or more of its output-memories.

In some cases, the set of objects read by a cyber agent might be empty. But the work that a cyber agent does always causes the population of objects in at least one of its output-memories to change.

Definition 5. A cyber agent is destructive if it erases objects from the populations in its output-memories. Otherwise, it is constructive.

The purpose of a destructive agent is to eliminate the mistakes and potential mistakes of its constructive counterparts by erasing outputs they should not have produced and inputs they should not consider.

Notice that all the intelligence of an autonomous destroyer is in its controls-its operator has only to perform the trivial task of erasing those objects its selector has chosen.

## 2.2. Collaboration

Definition 6. Two autonomous cyber agents are connected if they can exchange data, that is, if an output memory of one is an input memory of the other.

Definition 7. Two autonomous cyber agents collaborate whenever they actually exchange data, whether the exchange is productive or not.

Any collaborative arrangement among two or more completely autonomous cyber agents can be visualized as a ‘data flow’ Fig. 1 .Ž .

Definition 8. A data flow is a directed hypergraph in which each node is a Venn diagram of overlapping input- and output-memories, and each arc represents the operator and social skills of an agent. A data flow is strongly cyclic if every one of its arcs is in a closed loop. A data flow is unary if it has one and only one node representing a single memory that is shared by all the agents in the data flow.

![](/api/attachments/9P3SF45G/fulltext/images/4dfa1548ed3fc899e1f5ee430bc0ff5b6a868c6f1cdb5ec408a144f7a0c253fc.jpg)  
Fig. 1. A data flow in which $M _ { 1 } , M _ { 2 } , M _ { 3 } , M _ { 4 }$ are memories, $C _ { 1 } ,$ $C _ { 2 } , C _ { 3 } , C _ { 4 }$ are construction agents, and $D _ { 1 } , \ D _ { 2 }$ are destruction agents. $M _ { 1 }$ holds a population of trial solutions to the problem-tobe-solved. $M _ { 2 }$ and $M _ { 3 }$ hold populations of trial-solutions to related problems. $M _ { 4 }$ is the union of $M _ { 1 }$ and $M _ { 3 }$

Definition 9. An asynchronous team is a strongly cyclic data flow, that is, a set of autonomous cyber agents, connected so their outputs can circulate, and restricted to interacting only by modifying one another’s outputs.

## 2.3. Families of problems

Experience with asynchronous teams suggests that there are advantages to having them work on families of problems that include CP, the computational problem-to-be-solved, and some of its relatives. Perhaps progress on some of the easier problems in such a family catalyzes progress in the more difficult ones.

Definition 10. Two problems are related if i goodŽ . solutions to one provide parts of, bounds for, or other clues to good solutions of the second, or iiŽ . solutions of one influence solutions of the second. Two or more related problems constitute a family.

In general, a family of problems is more than a hierarchical decomposition of the problem-to-besolved, and can include members whose only relationship is that the solutions of some influence the solutions of others. For instance, the two problems: design a car and design a process for manufacturing it, constitute a family, because the solution to the first influences the solution to the second.

The obvious way to deploy an asynchronous team on a family of problems is to dedicate each of the team’s memories to one of the problems. This is achieved by arranging for the memory to hold a population of trial-solutions to its problem, and using a representation that is understood by all the agents that read from or write to that memory.

## 2.4. EffectiÕeness

An asynchronous team is started by placing a population of solutions in each of its memories. The agents then go to work on changing these populations the constructors add new solutions while theŽ destroyers erase old solutions . Under what condi-. tions will good solutions appear in a population? To answer this question, we will model all strongly cyclic data flows by unary data flows, and all off-line computational problems by single objective optimization problems. The justifications are as follows. First, a node in a data flow represents several overlapping memories. These can always be lumped into a single equivalent memory and every disjoint subgraph that starts and ends at the node can always be lumped into a single equivalent agent, to yield a unary data flow. Since the ‘lumping’ involves only a change of name and no change of structure, the dynamics of the original node are preserved by its equivalent. Second, every computational problem can be expressed as a multi-objective, constrained optimization problem, which in turn, can be approximated by a sequence of single-objective, unconstrained optimization problems.Let:

## M be the memory of a unary data flow

Ž . S, q be the single-objective optimization problem associated with M, where S is a set of all possible solutions to the problem, and q is a scalar measure of solution-quality. An optimal solution is a member of S that maximizes q.

$G _ { q }$ be the subset of S that contains only solutions of quality q or better.

$P ( t )$ be the population of trial-solutions in M at time t. The initial value of this population, Ž Ž . P 0 , is assumed to be a randomly chosen subset of S.. C, D be the sets of construction and destruction agents that work on M, causing P to change with time.

$T ( q )$ be the expected value of t for which $P ( t )$ and $G _ { q }$ first develop a non-zero intersection, that is, the expected time for $P ( t )$ to evolve at least one member of quality q or better.

Definition 11. $G _ { q }$ is reachable if $T ( q )$ is finite, that is, if solutions of quality q or better will appear in M in an amount of time whose expected value is finite.

Definition 12. The effectiveness of M is the double: $\{ q _ { \operatorname* { m a x } } , T ( q _ { \operatorname* { m a x } } ) \}$ , where $q _ { \mathrm { m a x } }$ is the largest value of q such that $G _ { q }$ is reachable.

Definition 13. A unary data flow is scale-effective if adding agents increases $q _ { \mathrm { m a x } }$ , and adding computers decreases $T ( q _ { \mathrm { m a x } } )$ . A node in a strongly cyclic data flow is scale-effective if its equivalent unary data flow is scale-effective. An asynchronous team is scale-effective if any of its primary nodes is scale-effective. A node is a primary node if it is dedicated to CP, the problem-to-be-solved, instead of to one of its relatives.

## 2.5. Construction space

Construction space, $( S , \ g ) _ { \ l }$ , is the space of solutions, S, together with an integer-valued function, g, that measures the separation in construction-workcycles between subsets of S. The following definition of g is given in terms of the two subsets of principal concern: P tŽ . and $G _ { q }$

Definition 14. $g ( P ( t ) , G _ { q } ) _ { }$ , the separation of the set $P ( t )$ from the set $G _ { q } ,$ , is the distance of the closest point in P tŽ . to $G _ { q }$ , that is, $g ( P ( t ) , G _ { q } ) = \mathbf { M i n } \{ \mathbf { f } ( p ,$ $G _ { q } ) \} , p \in P ( t )$ , where $\mathrm { f } ( p , \mathbf { G } _ { \mathrm { q } } ) .$ , the distance of any point p from the set $G _ { q } ,$ is the minimum number of work-cycles by construction agents necessary to improve the quality of $p$ to a level of $q$ or better; that is, to modify p till it becomes a member of $G _ { q } .$

Separation measured in this way has two noteworthy properties. First, solution-quality and separation are not directly related; the highest quality member of $P ( t )$ is not necessarily its closest member to $G _ { q } .$ Second, separation depends on the skills of the operators in C, the set of construction agents. To illustrate, consider two peaks maxima in the qualityŽ . surface, $s _ { 1 }$ and $s _ { 2 } .$ . Suppose that the quality of $s _ { 1 }$ is only slightly lower than that of $s _ { 2 }$ . Suppose that C contains only greedy, hill-climbing operators that are unable to descend from a high point in order to reach an even higher point. Then, there is no path from $s _ { 1 }$ to $s _ { 2 }$ . In other words, the distance from $s _ { 1 }$ to $s _ { 2 }$ is infinite. However, if C is expanded to include operators that can go down-hill, then the distance between $s _ { 1 }$ and $s _ { 2 }$ will become finite. In general, as agents with new and useful problem-solving capabilities are added to C, points of lesser quality draw closer to points of greater quality.

## 2.6. ConÕergence conditions

Let:

$t _ { 1 } , \ t _ { 2 } , \ldots$ . be the discrete points in time at which $P ( t )$ changes.

$P _ { 0 } , P _ { 1 } , . . . , P _ { N }$ be a sequence trajectory ofŽ . populations that reaches $G _ { q }$ in N steps, where $P _ { n } = P ( t _ { n } ) .$

$\{ s _ { 1 } , \ s _ { 2 } , \ldots , \ s _ { J } \}$ be the trial-solutions contained in $P _ { n } .$

$s *$ be the solution in $P _ { n }$ that is closest to $G _ { q } .$ $g _ { n }$ be the distance of $P _ { n }$ from $G _ { q } ,$ , that is, ${ g _ { n } } =$ $g ( P _ { n } , G _ { q } ) = \mathbf { f } ( s * , G _ { q } )$

$\alpha _ { n }$ be the event: $g _ { n + 1 } < g _ { n } .$

$\beta _ { n }$ be the event: $g _ { n + 1 } > g _ { n } .$

ProbŽ . x be the probability of event x.

Definition 15. The drift, $\lambda _ { n }$ , at the n-th point of a population-trajectory is:

$$
\lambda_ {n} = \operatorname{Prob} \left(\alpha_ {n}\right) - \operatorname{Prob} \left(\beta_ {n}\right)\tag{1}
$$

In words, the drift at any point of the populationtrajectory is the difference between two probabilities. The first is the probability that the next population will be closer to the goal, $G _ { q } ,$ that is, the probability of one of the constructors selecting s) and improving it. The second is the probability that the next population will be further from $G _ { q } ,$ , that is, the probability that one of the destroyers will mistakenly erase s).

Theorem 1. If the actions of all the agents, particularly the destroyers, are reÕersible, $i f g _ { 0 }$ is finite and $i f \lambda _ { n }$ is positiÕe for all n, then the expected Õalue of

N is finite. In other words, sufficient conditions for obtaining solutions of arbitrarily high quality are: ( ) a one of the constructors must be able to replace solutions erased by the destroyers, b at least one( ) member of the initial population must be at a finite distance from the desired solutions, and c the drift ( ) at all points along the population-trajectory must be positiÕe.

Under the reversibility condition, the populationtrajectory becomes a Markov chain, and the proof of the theorem follows directly from the properties of these chains. The details can be found in Ref. 26 .<sup>w</sup> <sup>x</sup>

## 2.7. Drift

What affects the drift, $\lambda _ { n } ^ { \mathrm { ~ 2 ~ } }$ Some insights are obtained by considering the following simplified situation:

<sup>Ø</sup> The agents work in sequence and each agent modifies only one solution per work cycle. In other words, $P _ { n + 1 }$ is produced from $P _ { n }$ by a single agent. If this agent is a constructor, it adds one solution to $P _ { n } .$ , if it is a destroyer, it erases one solution from $P _ { n } .$

<sup>Ø</sup> The quality of each solution reflects its probability of being the best closest solution, that is Ž .

$$
\operatorname{Prob} \left(\delta_ {j}\right) = q _ {j}\tag{2}
$$

where $\delta _ { j }$ is the event: $s _ { j } = s *$ , and $q _ { j }$ is the quality of $s _ { j } ,$ scaled so $q _ { 1 } + q _ { 2 } + \ldots + q _ { J } = 1$

<sup>Ø</sup> All the agents use the same selection mechanism, ‘quality based selection,’ and the same scheduling mechanisms, ‘perfect sequential scheduling.

To define these mechanisms and analyze the simplified situation, suppose there are K constructors, K destroyers and the solutions in $P _ { n }$ are labelled so $q _ { 1 } \leq q _ { 2 } \leq \ldots \leq q _ { J }$ . Now, consider the transition from $P _ { n }$ to $P _ { n + 1 }$ and the following events:

$c _ { k } \mathrm { : }$ the transition is caused by the k-th constructor. $\eta _ { k j } .$ the k-th constructor selects the j-solution, $s _ { j } .$ $\delta _ { j } \colon s _ { j }$ is s), the best solution in terms of distance. $\gamma _ { k } \mathrm { : }$ the k-th constructor is able to improve s).

$d _ { k } \mathbf { \cdot }$ the transition is caused by the k-th destroyer. $\mu _ { k j } .$ the k-th destroyer selects and erases the j-solution, $s _ { j } .$ .

Definition 16. In quality-based selection, constructors and destroyers select randomly from the popula tion of solutions, such that:

$$
\operatorname{Prob} \left(\eta_ {k j}\right) = q _ {j}\tag{3}
$$

$$
\operatorname{Prob} \left(\mu_ {k j}\right) = q _ {J + 1 - j}\tag{4}
$$

Thus, constructors are more likely to select the higher quality solutions while destroyers are more likely to select lower quality solutions As such, quality-based Ž selection is a symmetrical adaptation of the solution-rejection strategy used in simulated annealing..

Definition 17. In perfect sequential scheduling, constructors and destroyers schedule themselves so that:

$$
\operatorname{Prob} \left(c _ {k}\right) = 0. 5 \text {   if   } \operatorname{Prob} \left(\gamma_ {k}\right) > \operatorname{Prob} \left(\gamma_ {i}\right) \text {   for   all   } i \neq k
$$

$$
= 0 \mathrm{otherwise}.\tag{5}
$$

$$
\operatorname{Prob} \left(d _ {k}\right) = 0. 5 / K\tag{6}
$$

Thus, a constructor is as likely as a destroyer to cause the transition from $P _ { \mathrm { n } }$ to $P _ { n + 1 } .$ . And all but the most capable constructor with the largest value ofŽ $\operatorname { P r o b } ( \gamma _ { k } ) )$ refrain from scheduling themselves.

Theorem 2. In the simplified situation the drift, $\lambda _ { n }$ , is positiÕe, if:

$$
\operatorname{Max} \left\{\operatorname{Prob} \left(\gamma_ {k}\right) \right\} > \left[ \Sigma_ {j} q _ {j} q _ {J + 1 - j} \right] / \left[ \Sigma_ {j} \left(q _ {j}\right) ^ {2} \right]\tag{7}
$$

in other words, sufficient conditions for $\lambda _ { n }$ to be positive are that there be at least one construction agent with a nonzero probability of being able to improve the best current solution, and furthermore, this probability must be greater than the right hand side of 7 . Note that this right hand side can beŽ . considerably smaller than unity. For instance, with three solutions of quality $q _ { 1 } = 0 . 1 , q _ { 2 } = 0 . 2$ and $q _ { 3 } = 0 . 7$ , the right hand side of 7 is onlyŽ . $1 / 3$

Proof. $\lambda _ { n } = \operatorname { P r o b } ( \alpha _ { n } ) - \operatorname { P r o b } ( \beta _ { n } )$ by definition. To determine the value of $\operatorname { P r o b } ( \alpha _ { n } )$ , note that the events $c _ { 1 } , c _ { 2 } , \ldots , c _ { k } , d _ { 1 } , d _ { 2 } , \ldots , d _ { k }$ are mutually exclusive, and $\alpha _ { n }$ can occur only if the agent that works on $P _ { n }$ is a constructor. Therefore:

$$
\operatorname{Prob} \left(\alpha_ {n}\right) = \Sigma_ {k} \operatorname{Prob} \left(\alpha_ {n} \mid c _ {k}\right) \operatorname{Prob} \left(c _ {k}\right)\tag{8}
$$

where $\Sigma _ { k }$ means ‘summation over all $k . ^ { \prime }$ But:

$$
\begin{array}{r l} \operatorname{Prob} \big (\alpha_ {n} | c _ {k} \big) & = \Sigma_ {j} \operatorname{Prob} \big (\eta_ {k j} \cap \delta_ {j} \cap \gamma_ {k} \big) \\ & = \Sigma_ {j} \operatorname{Prob} \big (\eta_ {k j} \big) \operatorname{Prob} \big (\delta_ {j} \big) \operatorname{Prob} \big (\gamma_ {k} \big) \end{array}\tag{9}
$$

Combining 2 , 3 and 9 gives: Ž . Ž . Ž .

$$
\operatorname{Prob} \left(\alpha_ {n} \mid c _ {k}\right) = \operatorname{Prob} \left(\gamma_ {k}\right) \Sigma_ {j} y _ {j} y _ {j}\tag{10}
$$

Combining 5 , 8 and 10 gives: Ž . Ž . Ž .

$$
\operatorname{Prob} \left(\alpha_ {n}\right) = 0. 5 \operatorname{Max} \left\{\operatorname{Prob} \left(\gamma_ {k}\right) \right\} \Sigma_ {j} \left(q _ {j}\right) ^ {2}\tag{11}
$$

when scheduling is perfect. Now, to determine the value of ProbŽ $\beta _ { n } )$ , note that $\beta _ { n }$ can occur only if the agent that works on $P _ { n }$ is a destroyer and only if $s *$ is unique. Therefore:

$$
\operatorname{Prob} \left(\beta_ {n}\right) = \Sigma_ {j} \operatorname{Prob} \left(\beta_ {n} \mid d _ {k}\right) \operatorname{Prob} \left(d _ {k}\right)\tag{12}
$$

and

$$
\begin{array}{r l} \operatorname{Prob} \big (\beta_ {n} | d _ {k} \big) & \leq \Sigma_ {j} \operatorname{Prob} \big (\mu_ {k j} \cap \delta_ {j} \big) \\ & \leq \Sigma_ {j} \operatorname{Prob} \big (\mu_ {k j} \big) \operatorname{Prob} \big (\delta_ {j} \big) \end{array}
$$

Combining 2 , 4 and 13 gives:Ž . Ž . Ž .

Ž . 13

$$
\operatorname{Prob} \left(\beta_ {n} \mid d _ {k}\right) \leq \Sigma_ {j} y _ {J + 1 - j} y _ {j}\tag{14}
$$

Combining 6 , 12 and 14 gives: Ž . Ž . Ž .

$$
\operatorname{Prob} \left(\beta_ {n}\right) \leq 0. 5 \Sigma_ {j} q _ {j} q _ {J + 1 - j}\tag{15}
$$

$\lambda _ { n }$ is positive if $\operatorname { P r o b } ( \alpha _ { n } )$ Ž . , as given by 11 , is larger than ProbŽ $\beta _ { n } )$ Ž . , as given by 15 , completing the proof.

Conjecture 1: Construction and destruction are duals:adept destruction agents can compensate for inept construction agents and vice versa. In other words, all the benefits of adding construction agents with new and useful skills can also be obtained by adding destruction agents with new and useful skills.

As yet no experiments have been conducted to clearly demonstrate the validity of this conjecture. But a strong argument for its validity is made in Ref. <sup>w</sup> <sup>x</sup> 26 .

Conjecture 2: The mix of agents can include humans without any deleterious consequences.

By way of justifying this conjecture, note that he convergence conditions do limit the type of agent, as long as the agent is autonomous and interacts with other agents only by modifying the trial-solutions they produce. Therefore, complex software agents can be mixed with simple software agents which Ž has been experimentally demonstrated 1,7,8,10,<sup>w</sup> 11,14,17,18,22,23,25,27,28 , and in principle soft- <sup>x</sup>. ware agents can be mixed with humans experimentsŽ are now underway to examine this part of the conjecture 24 .<sup>w</sup> <sup>x</sup>.

## 2.8. Remarks

The key points made by the above analysis are:

<sup>Ø</sup> Construction and destruction are duals in that any effects obtained from adding construction agents can be replicated by adding suitable destruction agents.

<sup>Ø</sup> As construction agents with new and useful problem-solving skills are added, construction space contracts, that is, solutions of lesser quality draw closer to the solutions of greatest quality.

<sup>Ø</sup> If the drift is kept positive, then solutions of increasingly high quality become reachable as construction space contracts, that is, as new construction agents are added.

<sup>Ø</sup> Drift is likely to be positive if quality-based selection and perfect sequential scheduling are used.

But perfect sequential scheduling is simulated if all the agents work in parallel which happens auto-Ž matically if the agents are autonomous and enough computers are available . Also, solution-speed may. be expected to increase as computers are added, at least to the extent that the work cycles of the agents are reduced these additions. Thus, the conditions for scale-effectiveness is asynchronous teams are not overly restrictive, and one may expect it to appear in many, if not most, asynchronous teams. The experimental evidence obtained so far 1,7,8,10,11,14, <sup>w</sup> 17,18,22,23,25,27,28 bears out this conclusion.<sup>x</sup>

## 3. A grammar for asynchronous teams

The preceding section provides a general description of the structure and properties of asynchronous teams. However, in designing these teams, it is convenient to have a more compact description. Such a description is provided by a grammar whose primitives and rules are a distillation of Definitions 1–17. The main elements of this grammar are given below, the formal details are developed in Ref. 24 .<sup>w</sup> <sup>x</sup>

The purpose of the grammar is to provide a means for constructing all asynchronous teams that might be used in solving a given instance of a family of off-line problems. In other words, the grammar constructively defines the space that must be searched if an asynchronous team that is good at solving the given problem-instance is to be found.

The primitives of the grammar are:

<sup>Ø</sup> sharable memories, each dedicated to a member of the family-of-problems, and designed to contain a population of trial-solutions to its problem.

<sup>Ø</sup> operators for modifying trial-solutions.

<sup>Ø</sup> selectors for picking trial-solutions.

<sup>Ø</sup> schedulers for determining when selectors and operators are to work.

<sup>Ø</sup> Loosely speaking, the rules of the grammar are:

<sup>Ø</sup> Form autonomous agents by packaging an operator with a selector and a scheduler.

<sup>Ø</sup> Use quality-based-selection and completely parallel execution all the agents running all the time, Ž or as close to all the time as the available computer resources will allow as the default selection. and scheduling strategies.

<sup>Ø</sup> Connect the agents and memories to form a strongly cyclic data flow.

<sup>Ø</sup> Compensate for construction deficiencies with skilled destruction.

<sup>Ø</sup> Mix agents as needed without regard to their complexity or phylla, that is big and small software agents may be combined with humans, provided only that the humans subscribe to the communication and selection conditions prescribed for the software agents.

## 4. Some research issues: real-time power system control and learning

The typical power system contains thousands of distributed, mechanical decision makers control de-Ž vices , such as relays and voltage regulators. The . restructuring of power systems that is now underway, will undoubtedly introduce entirely new classes of control devices, such as FACTS-controllers and automatic agents to trade in energy on behalf of customers and independent generators. What are the best strategies for these old and new controllers to employ?

The main obstacles to good automatic-decisionmaking in distributed systems, such as electric power systems, are:

1. The context location and view of the system ofŽ . each decision-maker is unique. Therefore, the ideal strategy for each decision-maker is also unique.

2. The system changes with time. Therefore, the strategy used by each decision-maker also needs to evolve with time.

3. Many of the rules that should be included in a strategy, such as the rules for when to switch from the normal mode of control to an the emergency mode of control, are not explicitly known.

Because of these obstacles, it is impractical to manually program the ideal strategy into each controller. An alternative is to provide these devices with the capabilities for automatic, context-dependent and lifelong learning by which we mean theŽ continual transformation of experience-actual or simulated operating data-into location-specific, strategy improvements..

Existing learning models, such as Neural Nets, Bayesian Nets and Reinforcement Learning, can deal with very large volumes of numerical data. But they cannot deal with data of high dimension, such as the state information of an entire power system. Therefore, the successful application of learning technology to a power system is contingent on decomposing the system into much smaller subsystems, each with a much smaller state-space. This decomposition can be either hierarchical or flat. But, as has been pointed out before, flat decompositions have profound advantages: they tend to be much more open and fault tolerant. Realizing on these advantages will require extending the off-line technology described earlier to real-time situations, and adding learning skills to autonomous agents. Then, the mechanical decision making can be handled by these autonomous agents, each collecting only locally available data on the state of the power system, making up for its lack of a global view by collaborating with its immediate neighbors, and continually improving its performance through automatic learning.

For quasi-repetitive problems 6 , that is, different <sup>w</sup> <sup>x</sup> instances of essentially the same general problem, it has been demonstrated that the autonomous agents in an asynchronous team can learn to collaborate more effectively 2,3 . Now, more powerful learning tech-<sup>w</sup> <sup>x</sup> niques need to be developed and the issue of hard constraints on solution-speed taken into account.

## Acknowledgements

The work reported here was supported in part by the National Science Foundation under Grant Number ECS-9615599, and by DARPA through Contact Number ONR Grant Number N00014-96-1-0854.

## References

<sup>w</sup> <sup>x</sup> 1 P. Avila-Abascal, S.N. Talukdar, Cooperative algorithms and abductive causal networks for the automatic generation of intelligent substation alarm processors, Proceedings of IS-CAS-96.

<sup>w</sup> <sup>x</sup> 2 L. Baerentzen, S.N. Talukdar, Improving cooperation among autonomous agents in asynchronous teams, Journal of Computational and Mathematical Organizational Theory, submitted.

<sup>w</sup> <sup>x</sup> 3 L. Baerentzen, P. Avila, S.N. Talukdar, Learning network designs for asynchronous teams, in: Lecture Notes in Artificial Intelligence 1237: Multi-Agent Rationality, Proc. of 8th European Workshop on Modeling Autonomous Agents in a Multi-Agent World, MAAMAW’97, Springer, Ronneby, Sweden, May 1997.

<sup>w</sup> <sup>x</sup> 4 G. Bassak, Bringing in the A-teams, IBM Research, No. 2, 1996.

<sup>w</sup> <sup>x</sup> 5 K. Carley, A. Newell, The nature of the social agent, Journal of Mathematical Sociology 19 4 1994 221–262.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 K.M. Carley, Computational and mathematical organization theory: perspectives and directions, Journal of Computational and Mathematical Organizational Theory 1 1 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 C.L. Chen, Bayesian Nets and A-Teams for Power System Fault Diagnosis, PhD Dissertation, Electrical and Computer Engineering Department, Carnegie Mellon University, Pittsburgh, PA, 1992 .Ž .

<sup>w</sup> <sup>x</sup> 8 S.Y. Chen, S.N. Talukdar, N.M. Sadeh, Job-shop-scheduling by a team of asynchronous agents, IJCAI-93 Workshop on Knowledge-Based Production, Scheduling and Control, Chambery, France, 1993.

<sup>w</sup> <sup>x</sup> 9 L. Davis Ed. , Handbook of Genetic Algorithms, Van Nos-Ž . trand Reinhold 1991 .Ž .

<sup>w</sup> <sup>x</sup> 10 P.S. deSouza, S.N. Talukdar, Genetic algorithms in asynchronous teams, Proceedings of the Fourth International Conference on Genetic Algorithms, Morgan Kaufmann, Los Altos, CA 1991 .Ž .

<sup>w</sup> <sup>x</sup> 11 P. de Souza, Asynchronous Organizations for Multi-Algorithm Problems, PhD Dissertation, Dept. of Electrical and Computer Engineering, Carnegie Mellon University, Pittsburgh, PA 1993 .Ž .

<sup>w</sup> <sup>x</sup> 12 F. Glover, Tabu Search—Part I, ORSA Journal of Computing 1 3 1989 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 F. Glover, Tabu Search—Part II, ORSA Journal of Computing 2 1 1990 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 S.R. Gorti, S. Humair, R.D. Sriram, S. Talukdar, S. Murthy, Solving constraint satisfaction problems using A-teams, to appear in AI-EDAM.

<sup>w</sup> <sup>x</sup>15 A. Kerr Jr., in: C.C. Thomas Ed. , Subacute BacteriaŽ . Endocardites, Springfield, IL 1955 .Ž .

<sup>w</sup> <sup>x</sup> 16 S. Kirkpatrick, C.D. Gelatt, M.P. Cecchi, Optimization by simulated annealing, Science 220 4598 1983 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 H. Lee, S. Murthy, W. Haider, D. Morse, Primary production scheduling in steelmaking industries, IBM Report, 1995.

<sup>w</sup> <sup>x</sup> 18 S. Murthy, Synergy in Cooperating Agents: Designing Manipulators from Task Specifications, PhD dissertation, Department of Electrical and Computer Engineering, Carnegie Mellon University, Pittsburgh, PA 1992 . Ž .

<sup>w</sup> <sup>x</sup> 19 H.P. Nii, Blackboard systems: the blackboard model of problem solving and the evolution of blackboard architectures, Parts I and II, AI Magazine, 7:2 and 7:3 1986 .Ž .

<sup>w</sup> <sup>x</sup> 20 G.F. Oster, E.O. Wilson, Caste and Ecology in the Social Insects, Princeton University Press, Princeton, NJ 1978 .Ž .

<sup>w</sup> <sup>x</sup> 21 S. Pugh, Total Design, Addison Wesley, 1990.

22 R.W. Quadrel, Asynchronous Design Environments: Architecture and Behavior, PhD Dissertation, Department of Ar-

chitecture, Carnegie Mellon University, Pittsburgh, PA Ž . 1991 .

<sup>w</sup> <sup>x</sup> 23 J. Rachlin, F. Wu, S. Murthy, S. Talukdar, M. Sturzenbecker, R. Akkiraju, R. Fuhrer, A. Aggarwal, J. Yeh, R. Henry, R. Jayaraman, Forest view: a system for integrated scheduling in complex manufacturing domains, IBM Report, 1996.

<sup>w</sup> <sup>x</sup> 24 S. Sachdev, Modular Optimization, PhD Proposal, Carnegie Mellon University, Feb. 1998.

<sup>w</sup> <sup>x</sup> 25 S.N. Talukdar, V.C. Ramesh, A parallel global optimization algorithm and its application to the CCOPF problem, Proceedings of the Power Industry Computer Applications Conference, Phoenix, May, 1993.

<sup>w</sup> <sup>x</sup> 26 S.N. Talukdar, L. Baerentzen, A. Gove, P.S. deSouza, Asynchronous teams: cooperation schemes for autonomous agents, to appear in the Journal of Heuristics, and visible at: www.ece.cmu.edu<sup>r</sup>afs<sup>r</sup>ece<sup>r</sup>usr<sup>r</sup>talukdar<sup>r</sup>heuristics.ps.

<sup>w</sup> <sup>x</sup> 27 S.N. Talukdar, S.S. Pyo, T. Giras, Asynchronous procedures for parallel processing, IEEE Trans. on PAS 102 11 1983 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 C.K. Tsen, Solving Train Scheduling Problems Using A-Teams, PhD dissertation, Electrical and Computer engineering Department, CMU, Pittsburgh, 1995.

Sarosh Talukdar is a Professor of Electrical and Computer Engineering at Carnegie Mellon University CMU . Before joining Ž . CMU, he worked as a senior staff engineer at McGraw-Edison-a manufacturer of electrical equipment. His undergraduate degree is from the Indian institute of Technology, Madras, and his PhD is from Purdue University. Talukdar is known for his work in simulation, optimization and knowledge-based systems for electric power networks, and autonomous software agents for difficult computational problems. He is a fellow of the IEEE and has been the recipient of the Eta Kappa Nu award for excellence in undergraduate teaching.
