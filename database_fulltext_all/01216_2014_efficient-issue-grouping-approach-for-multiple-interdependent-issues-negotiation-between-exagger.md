---
otero_id: 1216
otero_key: "3EJD8RQ6"
title: "Efficient issue-grouping approach for multiple interdependent issues negotiation between exaggerator agents"
authors: "Katsuhide Fujita; Takayuki Ito; Mark Klein"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ef<sup>fi</sup>cient issue-grouping approach for multiple interdependent issues negotiation between exaggerator agents

Katsuhide Fujita <sup>a,</sup>⁎, Takayuki Ito <sup>b</sup>, Mark Klein <sup>c</sup>

<sup>a</sup> Faculty of Engineering, Tokyo University of Agriculture and Technology, 2-24-16 Naka-cho, Koganei-shi, Tokyo 184-8588, Japan

<sup>b</sup> Techno-Business School, Nagoya Institute of Technology, Gokiso-cho, Showa-ku, Nagoya, Aichi, 466-8555, Japan

<sup>c</sup> Sloan School of Management, Massachusetts Institute of Technology, 5 Cambridge Center, NE25-754, Cambridge, MA 02139, USA

## a r t i c l e i n f o

Available online 6 June 2013

Keywords: Multi-issue negotiation Nonlinear utility Interdependency issues Exaggerator agent Multi-agent system

## a b s t r a c t

Many real-world negotiations involve multiple interdependent issues, which makes an agent's utility functions complex, with nonlinear shapes and multiple optima. Traditional negotiation mechanisms were designed for linear utilities, and do not fare well in nonlinear contexts. One of the main challenges in developing effective nonlinear negotiation protocols is scalability; it can be extremely dif<sup>fi</sup>cult to <sup>fi</sup>nd high-quality solutions when there are many issues, due to computational intractability. One reasonable approach to reducing computational cost, while maintaining good quality outcomes, is to decompose the contract space into several largely independent sub-spaces. In this paper, we propose a method based on this concept. A mediator <sup>fi</sup>nds sub-contracts in each sub-space based on votes from the agents, and combines the sub-contracts to produce the <sup>fi</sup>nal agreement. We demonstrate, experimentally, that our protocol allows high-optimality outcomes with greater scalability than previous efforts. We also demonstrate a method for addressing the potential problem of strategic non-truthful voting by the agents.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Negotiation is an important aspect of daily life and represents an important topic in the <sup>fi</sup>eld of multi-agent system research. There has been extensive work in the area of automated negotiation; that is, where software agents negotiate with other agents in such contexts as e-commerce [13], large-scale deliberation [19], collaborative design, and so on. Many real-world negotiations are complex, involving interdependent issues. When designers work together to design a car, for example, the utility of a given carburetor choice is highly dependent on which engine is chosen. The key impact of such issue dependencies is that they create nonlinear utility functions, with multiple optima. There has been an increasing interest in negotiation with multiple interdependent issues [9,17,20,22,23]. To date, however, achieving high scalability in negotiations with multiple interdependent issues remains an open problem.

We propose a new protocol in which a mediator tries to reorganize a highly complex utility space with issue interdependencies into several tractable subspaces, in order to reduce the computational cost. We call these utility subspaces “Issue groups.” First, the agents generate interdependency graphs which capture the relationships between the issues in their individual utility functions, and derive issue clusters from that. Second, a mediator combines these issue clusters to identify aggregate issue groups. Finally, the mediator uses a nonlinear optimization protocol to <sup>fi</sup>nd sub-agreements for each issue group based on votes from the agents, and combines them to produce the <sup>fi</sup>nal agreement.

We also address the issue of strategic non-truthful voting. In our protocol, agents can make strong or weak accept/reject votes. Agents may therefore exaggerate their votes to be always “strong”, which biases the negotiation outcomes to favor the exaggerator, but at the cost of reduced social welfare. To address this, we limit the number of strong votes an agent can make, and investigate its impact of social welfare.

The remainder of this paper is organized as follows. We describe a model of multiple interdependent issue negotiation. Next, we present a clustering technique for <sup>fi</sup>nding issue sub-groups. We then propose a protocol that uses this issue group information to enable more scalable negotiations. We also describe the effect of Exaggerator Agents in multi-agent situations. We present the experimental results, demonstrating that our protocol produces more optimal outcomes than previous efforts. Finally, we describe related work and present our overall conclusions.

## 2. Negotiation with nonlinear utility functions

## 2.1. Multi-issue negotiation model

We consider the situation where N agents $\left( a _ { 1 } , . . . , a _ { N } \right)$ want to reach an agreement with a mediator who manages the negotiation from a man-in-the-middle position. There are M issues $( i _ { 1 } , . . . , i _ { M } )$ to be negotiated. The number of issues represents the number of dimensions in the utility space. The issues are shared: all agents are potentially interested in the values for all M issues. A contract is represented by a vector of values ${ \vec { s } } = s _ { 1 } , . . . , s _ { M } .$ Each issue s<sub>j</sub> has a value drawn from the domain of integers $[ 0 , X ] , \mathrm { i . e . , } s _ { j } \in \{ 0 , 1 , . . . , X \} ( 1 \leq j \leq M ) .$ 1

An agent's utility function, in our formulation, is described in terms of constraints. There are l constraints, $c _ { k } \in C .$ . Each constraint represents a volume in the contract space with one or more dimensions and an associated utility value. $c _ { k }$ has value $w _ { a } \left( c _ { k } \mathrm { ~ } , \vec { s } \right)$ if and only if it is satis<sup>fi</sup>ed by contract ${ \vec { s } } .$ . Function $\delta _ { a } ( c _ { k } , i _ { j } )$ is a region of $i _ { j }$ in $c _ { k } ,$ and $\delta _ { a } ( c _ { k } , i _ { j } )$ is $\emptyset { \mathrm { ~ i f ~ } } c _ { k }$ doesn't have any relationship to $i _ { j } .$ Every agent has its own, typically unique, set of constraints.

An agent's utility for contract $\vec { s }$ is de<sup>fi</sup>ned as the sum of the utility for all the constraints the contract satis<sup>fi</sup>es, i.e., as $u _ { a } \big ( \vec { s } \big ) =$ $\textstyle \sum _ { c _ { k } \in C , { \vec { s } } } \in x ( c _ { k } ) w _ { a } \left( c _ { k } \ { \vec { , } } \right)$ , where $x ( c _ { k } )$ is a set of possible contracts (solutions) of $c _ { k } .$ This formulation produces complex utility functions with high points where many constraints are satis<sup>fi</sup>ed and lower regions where few or no constraints are satis<sup>fi</sup>ed. Many real-world utility functions are quite complex in this way, involving many issues as well as higher-order (e.g. binary, trinary and quaternary) constraints. This represents a crucial departure from most previous efforts on multi-issue negotiation, where contract utility has been calculated as the weighted sum of the utilities for individual issues, producing utility functions shaped like hyper-planes, with a single optimum.

This constraint-based utility function representation allows us to capture the issue interdependencies common in real-world negotiations. The constraint in Fig. 1, for example, captures the fact that a value between 3 and 7 is desirable for issue 1 if issue 2 has the value 4, 5 or 6. If we have many such constraints, we can create highly complex utility functions as show in Fig. 1. Note, however, that this representation is also capable of capturing linear utility functions as a special case. A negotiation protocol for complex contracts can, therefore, handle linear contract negotiations. This formulation was described in [9]. In [17,20,21], a similar formulation is presented that supports a wider range of constraint types.

The objective function for our protocol can be described as follows:

$$
\arg \max _ {\vec {s}} \sum_ {a \in N} u _ {a} (\vec {s}).\tag{1}
$$

$$
\arg \max _ {\vec {s}} u _ {a} (\vec {s}), (a = 1, \dots , N).\tag{2}
$$

Our protocol, in other words, tries to <sup>fi</sup>nd contracts that maximize social welfare, i.e., the summed utilities for all agents. Such contracts, by de<sup>fi</sup>nition, will also be Pareto-optimal. At the same time, all the agents try to <sup>fi</sup>nd contracts that maximize their own welfare.

## 3. Our negotiation protoco

## 3.1. Decomposing the contract space

It is of course theoretically possible to gather all of the individual agents' utility functions in one central place and then <sup>fi</sup>nd all optimal contracts using such well-known nonlinear optimization techniques as simulated annealing or evolutionary algorithms. However, we do not employ such centralized methods for negotiation purposes because we assume, as is common in negotiation contexts, that agents prefer not to share their utility functions with each other, in order to preserve a competitive edge.

Our approach is described in the following sections.

## 3.2. Analyzing issue interdependency

The <sup>fi</sup>rst step is for each agent to generate an interdependency graph by analyzing the issue interdependencies in its own utility space. We de<sup>fi</sup>ne issue interdependency as follows. If there is a constraint between issue $X ( i _ { X } )$ and issue Y (i ), then we assume i and $i _ { Y }$ are interdependent. If, for example, an agent has a binary constraint between issue 1 and issue 3, those issues are interdependent for that agent.

The strength of issue interdependency is captured by the interdependency rate. We de<sup>fi</sup>ne the interdependency rate between two issues as the number of constraints that inter-relate them. The interdependency rate between issue $i _ { j }$ and issue $i _ { j j }$ for agent a is thus $D _ { a } ( i _ { j } , i _ { j j } ) = \# \{ c _ { k } | \delta _ { a } ( c _ { k } , i _ { j } ) \neq \emptyset \land \delta _ { a } ( c _ { k } , \bar { i } _ { j j } ) \neq \emptyset \}$

Agents capture their issue interdependency information in the form of interdependency graphs i.e. weighted non-directed graphs where a node represents an issue, an edge represents the interdependency between issues, and the weight of an edge represents the interdependency rate between those issues. An interdependency graph is thus formally de<sup>fi</sup>ned as: $G ( P , E , w ) : P = \{ 1 , 2 , . . . , | I | \} ( f i n i t e s e t ) ,$ $E \subset \{ \{ x , y \} | x , y \in P \} , w : E  R .$

Fig. 2 shows an example of an interdependency graph.

## 3.3. Grouping issues

In this step, the mediator employs breadth-<sup>fi</sup>rst search to combine the issue clusters submitted by each agent into a consolidated set of issue groups. For example, if agent 1 submits the clusters $\{ i _ { 1 } , i _ { 2 } \} , \{ i _ { 3 } , i _ { 4 } , i _ { 5 } \} ,$ $\{ i _ { 0 } , i _ { 6 } \}$ and agent 2 submits the clusters: $\{ i _ { 1 } , i _ { 2 } , i _ { 6 } \} , \{ i _ { 3 } , i _ { 4 } \} , \{ i _ { 0 } \} , \{ i _ { 5 } \}$ , the mediator combines them to produce the issue groups $\{ i _ { 0 } , i _ { 1 } , i _ { 2 } , i _ { 6 } \} , \{ i _ { 3 } , i _ { 4 } , i _ { 5 } \}$ . In the worst case, if all the issue clusters submitted by the agents have overlapping issues, the mediator generates the union of the clusters from all the agents. The details of this algorithm are given in Algorithm 1.

## Algorithm 1. Combine\_IssueGroups(G)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Ag: A set of agents, G: A set of issue-groups of each agent
 $(G = \{G_{0}, G_{1}, ..., G_{n}\}$ , a set of issue-groups from agent i is  $G_{i} = \{g_{i,0}, g_{i,1}, ..., g_{i,m_{i}}\})$ 

1: SG :=  $G_{0}$ , i := 1

2: while i &lt; |Ag| do

3:  $SG' := \emptyset$ 

4: for  $s \in SG$  do

5: for  $g_{i,j} \in G_{i}$  do

6:  $s' := s \cap g_{i,j}$ 

7: if  $s' \neq \phi$  then

8:  $SG' := s \cup g_{i,j}$ 

9: end if

10:  $SG := SG'$ , i := i + 1

11: end for

12: end for

13: end while
</div>

It is possible to gather all of the agents' interdependency graphs in one central place and then <sup>fi</sup>nd the issue groups using standard clustering techniques. However, it is hard to determine the optimal number of issue groups or the clustering parameters in central clustering algorithms, because the basis of clustering for every agent can be different. Our approach avoids these weaknesses by requiring that each agent generates its own issue clusters. In our experiments, agents did so using the well-known Girvan–Newman algorithm [6], which computes clusters in weighted non-direct graphs. The algorithm's output can be controlled by changing the “number of edges to remove” parameter. Increasing the value of this parameter increases the number of issue dependencies ignored when calculating the issue clusters, thereby resulting in a larger number of smaller clusters. The running time of this algorithm is 0 (kmn), where k is the number of edges to remove, m is the total number of edges, and n is the total number of vertices.

![](/api/attachments/3EJD8RQ6/fulltext/images/a47c0dfb676b814544c4df68fd978a4311ad2095d3c3b519f4ba6b2a748bc650.jpg)  
Fig. 1. Example of a nonlinear utility space.

## 3.4. Finding agreements

We use a distributed variant of simulated annealing (SA) [11] to <sup>fi</sup>nd optimal contracts in each issue group. In each round, the mediator proposes a contract that is a random single-issue mutation of the most recently accepted contract (the accepted contract is initially generated randomly). Each agent then votes to strongly accept (+2), weakly accept (+1), weakly reject (−1) or strongly reject ( 2) the new contract, based on whether it is better or worse than the last accepted contract for that issue group. When the mediator receives these votes, it adds them together. If the sum of the vote values from the agents is positive or zero, the proposed contract becomes the currently accepted one for that issue group. If the vote sum is negative, the mediator will accept the contract with probability $P ( a c c e p t ) = e ^ { \Delta U / T }$ , where T is the mediator's virtual temperature (which declines over time) and ΔU is the utility change between the contracts. In other words, the higher the virtual temperature and the smaller the utility decrement, the greater the probability that the inferior contract will be accepted. If the proposed contract is not accepted, a mutation of the most recently accepted contract is proposed in the next round. This continues over many rounds. This technique allows the mediator to skip past local optima in the utility functions, especially earlier on in the search process, in the pursuit of global optima.

![](/api/attachments/3EJD8RQ6/fulltext/images/f0dd64abf91cb38b36a08e7781c97c3ed9f5ab21adca2d7216c7b21ee6327613.jpg)  
Fig. 2. Interdependency graph (50 issues).

## Algorithm 2. Simulated\_Annealing()

```python
Value(N): the sum of the numeric values mapped from votes to N from all agents
1: S := initial solution (set randomly)
2: for t = 1 to ∞ do
3:    T := schedule(t)
4:    if T = 0 then
5:    return current
6:    end if
7:    next := a randomly selected successor of current
8:    if next.Value ≥ 0 then
9:    ΔE := next.Value - current.Value
10:    if ΔE > 0 then
11:    current := next
12:    else
13:    current := next only with probability e^ΔE/T
14:    end if
15:    end if
16: end for
```

## 3.5. Exaggerator agents

Any voting scheme introduces the potential for strategic non truthful voting by the agents, and our method is no exception. For example, one of the agents may always vote truthfully, while the other exaggerates so that its votes are always “strong.” It has been shown that this biases the negotiation outcomes to favor the exaggerator, at the cost of reduced social welfare [12]. What we need is an enhancement of our negotiation protocol that prevents the exaggerator votes and maximizing social welfare.

We hypothesized that simply placing the correct limit on the number of “strong” votes each agent can work well. If the limit is too low, we effectively lose the bene<sup>fi</sup>t of vote weight information and get the lower social welfare values that result. If the strong vote limit is high enough to avoid this, then all an exaggerator has to do is save all of its strong votes until the end of the negotiation, at which point it can drag the mediator towards making a series of proposals that are inequitably favorable to it. In the experiments, we demonstrate that the correct limit on the number of “strong” voting is ef<sup>fi</sup>cient of <sup>fi</sup>nding high solutions.

## 4. Experimental results

## 4.1. Setting

We conducted several experiments to evaluate our approach. In each experiment, we ran 100 negotiations. The following parameters were used. The domain for the issue values was [0,9]. Each agent had 10 unary constraints, 5 binary constraints, 5 trinary constraints, and so on (a unary constraint relates to one issue, a binary constraint relates to two issues, etc.). The maximum weight for a constraint was 100 × (Number of Issues).

In our experiments, each agent's issues were organized into ten small clusters with strong dependencies between the issues within each cluster. We ran two conditions: “1) Sparse Connection” and “2) Dense Connection”. Fig. 3 gives examples, for these two cases, of interdependency graphs and the relationship between the number of issues and the sum of the connection weights between issues. As these graphs show, the “1) Sparse Connection” case is closer to a scale-free distribution, with power-law statistics, while the “2) Dense connection” is closer to a random graph.

We compared the following negotiation methods: “(A) Issue-Grouping (True Voting)” applies the simulated annealing protocol based on the agents' votes, and performs the negotiation separately for each of the issue groups, and combines the resulting subagreements to produce the <sup>fi</sup>nal agreement. All agents make truthful votes. “(B) Issue-Grouping (Exaggerator Agents)” applies the simulated annealing protocol based on the agents' votes with issue-grouping. “All agents” make exaggerated votes. “(C) Issue-Grouping (limitation)” is the same as (B), except that a limitation on the number of ‘strong’ votes is applied. A limitation of 250 ‘strong’ votes was found to be the optimal number for these experiments. “(D) Without Issue-Grouping” is the method presented in Klein et.al [12], using a simulated annealing protocol based on the agents' votes without generating issue-groups.

In all these cases, the search began with a randomly generated contract, and the SA initial temperature for all these cases was 50.0 and decreased linearly to 0 over the course the negotiation. In case (D), the search process involved 500 iterations. In case (A)–(C), the search process involved 50 iterations for each issue group. Cases (A), (B), (C) and (D) thus used the same amount of computation time, and are thus directly comparable. The number of edges removed from the issue interdependency graph, when the agents were calculating their issue groups, was 6 in all cases.

1) Sparse Connection  
![](/api/attachments/3EJD8RQ6/fulltext/images/b12df45337b72e1c7de98ed6836c256ed403875d04b88c782fd680fcd25c1164.jpg)

![](/api/attachments/3EJD8RQ6/fulltext/images/c577f07f3395869430135f49ce9c08a0bb34b2b39efaf73e910984817fc7efc3.jpg)

2) Dense Connection  
![](/api/attachments/3EJD8RQ6/fulltext/images/499696e440023f1b0903d859da29337ec8ada58c1038477f99d7bccb0d37618c.jpg)

![](/api/attachments/3EJD8RQ6/fulltext/images/f57cfaf4a5c7fc2cf303566a73cefd63e1bd34a657ce958b11da4d0cddaf9e5c.jpg)  
Fig. 3. Issue interdependencies.

We applied a centralized simulated annealing to the sum of the individual agents' utility functions to approximate the optimal social welfare for each negotiation test run. Exhaustive search was not a viable option because it becomes computationally intractable as the number of issues grows. The SA initial temperature was 50.0 and decreases linearly to 0 over the course of 2500 iterations. The initial contract for each SA run is randomly selected. We calculated a normalized “optimality rate” for each negotiation run, de<sup>fi</sup>ned as (social welfare achieved by each protocol) / (optimal social welfare calculated by SA).

Our code was implemented in Java 2 (1.6) and was run on a core 2-duo CPU with 2.0 GB memory under Mac OS X (10.6).

## 4.2. Method of determining interdependency graph

Fig. 4 shows what the interdependency graph consists of in an agent.

The method of determining the interdependency in the experiment is as follows.

(Step 1) Small issue-groups are generated by connecting a part of the issues randomly.

(Step 2) The interface issues are decided randomly among issues in each issue-group. The interface issues are for connecting other small issue-groups. In small issue-groups, only the interface issues can connect to other issue-groups.

(Step 3) All combinations of each issue-group are searched, and it is decided whether connection or disconnection according to the possibility of generating connections.

## 4.3. Experimental results

Figs. 5 and 6 compare the optimality rate in the sparse connection and dense connection cases. “(A) Issue-Grouping (True Voting)” achieved a higher optimality rate than “(D) Without Issue-Grouping” which means that the issue-grouping method produces better results for the same amount of computational effort. The optimality rate of the “(A) Issue-Grouping (True Voting)” condition decreased as the number of issues (and therefore the size of the search space) increased. “(B) Issue-Grouping (Exaggerator Agents)” is worse than “(A) Issue-Grouping (True Voting)” because the exaggerator agents generate reduced social welfares in multi-agent situations. However, “(C) Issue-Grouping (limitation)” outperforms “(B) Issue-Grouping (Exaggerator Agents)”, therefore, the limitation of ‘strong’ votes is effective of improving the social welfare reduced by the Exaggerator Agents.

![](/api/attachments/3EJD8RQ6/fulltext/images/d0d4f5368ab6b3d2d3e39fdc19425a04ca7aa91979518e37609a335f2c62bba2.jpg)  
Fig. 4. Method of determining interdependency graph.

The optimality rates for all methods are almost unaffected by the number of agents, as Fig. 6 shows. The optimality rate for (A) is higher than (D) in the “1) Sparse Connections” case than the “2) Dense Connections” case. This is because the issue grouping method proposed in this paper can achieve high optimality if the number of ignored interdependencies is low, which is more likely to be true in the “1) Sparse Connections” case. Many real-world negotiations are, we believe, characterized by sparse issue inter-dependencies.

We also assessed a quality factor measure QF = (Sum of internal weights of edges in each issue-group) / (Sum of external weights of edges in each issue-group) to assess the quality of the issue groups, i.e. the extent to which issue dependencies occurred only between issues in the same clusters, rather than between issues in different groups. Higher quality factors should, we predict, increase the advantage of the issue grouping protocols, because that means fewer dependencies are ignored when negotiation is done separately for each issue group. Fig. 7 shows the quality factors when the number of agents is 3 and 20, as a function of the number of edges to be removed, which is the key parameter in the clustering algorithm we used. The number of issues is 50 in the “1) sparse connection” case. “(a) Central Method” is to gather all of the agents' interdependency graphs in one central place and then <sup>fi</sup>nd the issue groups using the well-known Girvan–Newman algorithm [6]. “(b) Our method” employs breadth-<sup>fi</sup>rst search to combine the issue clusters submitted by each agent into a consolidated set of issue groups.

Comparing (a) with (b) in Fig. 7, (b) proposed in this paper outperforms (a). This is because that our method gathers issuegrouping data from the agents without requiring a global clustering parameter. The QF becomes smaller when the number of edges to be progressively removed is larger. This is because the number of issue-groups generated by each agent is higher as the number of edges to be progressively removed becomes larger. The rapid decrease sometimes happens as the number of edges to be progressively removed increases. These points are good parameters for decomposing the issue-groups. In real life, the utility of agents contains an adequate idea of issue-groups, and agents can determine the optimal idea of issue-grouping by analyzing the utility spaces.

## 5. Related work

Even though nonlinear negotiation seems to involve a straightforward distributed constraint optimization problem [7,18], we have been unable to exploit existing work on high-ef<sup>fi</sup>ciency constraint optimizers. Such solvers attempt to <sup>fi</sup>nd the solutions that maximize the weights of the satis<sup>fi</sup>ed constraints, but do not account for the fact that the <sup>fi</sup>nal solution must satisfy at least one constraint from every agent.

Lin et al. [14] explored a range of protocols based on mutation and selection on binary contracts. This paper does not describe what kind of utility function is used, nor does it present any experimental analyses, so it remains unclear whether this strategy enables suf<sup>fi</sup>cient exploration of utility space.

Klein et al. [12] presented a protocol applied with near optimal results to medium-sized bilateral negotiations with binary dependencies, but was not applied to multilateral negotiations and higher order dependencies.

1) Sparse Connections  
![](/api/attachments/3EJD8RQ6/fulltext/images/f504e48a58d77ecccb9d1797c50cc2d47fdce74809ac8b7d5c06d47542243fd1.jpg)

2) Dense Connections  
![](/api/attachments/3EJD8RQ6/fulltext/images/b6424d16a85443fcbf176cc23ce6bf257a9842d25d3491a8e2fa66b183a8ee29.jpg)  
Fig. 5. Comparison of optimality when the number of issues changes.

A bidding-based protocol was proposed by Ito et al. [9]. Agents generate bids by <sup>fi</sup>nding high regions in their own utility functions, and the mediator <sup>fi</sup>nds the optimum combination of submitted bids from the agents. However, the scalability of this protocol is limited, and the failure rate of making agreements was sometimes high. In Fujita et al. [4], a representative-based protocol for reducing the computational cost was proposed based on the bidding-based protocol. In this method, the scalability of agents was improved but still limited. Fujita et al. [5] also focused on the decomposing the contract space for highly scalable negotiation, but the negotiation protocol was different.

Hindriks et al. [8] proposed an approach based on a weighted approximation technique to simplify the utility space. The resulting approximated utility function without dependencies can be handled by negotiation algorithms that can ef<sup>fi</sup>ciently deal with independent multiple issues, and has a polynomial time complexity. Our protocol can <sup>fi</sup>nd an optimal agreement point if agents don't have in common the expected negotiation outcome.

Fatima et al. [2,3] proposed bilateral multi-issue negotiations with time constraints. This method can <sup>fi</sup>nd approximate equilibrium in polynomial time where the utility function is nonlinear. However, this paper focused on bilateral multi-issue negotiations. Our protocol focuses on multilateral negotiations.

Zhang [25] presents an axiomatic analysis of negotiation problems within task-oriented domains (TOD). In this paper, three classical bargaining solutions (Nash solution, Egalitarian solution, Kalai-Smorodinsky solution) coincide when they are applied to a TOD with mixed deals but diverge if their outcomes are restricted to pure deals.

Maestre et al. [20,21] proposed an auction-based protocol for nonlinear utility spaces generated using weighted constraints, and proposed a set of decision mechanisms for the bidding and deal identi<sup>fi</sup>cation steps of the protocol. They proposed the use of a quality factor to balance utility and deal probability in the negotiation process. This quality factor is used to bias bid generation and deal identi-<sup>fi</sup>cation, taking into account the agents' attitudes toward risk. The scalability of the number of issues is still a problem in these works.

Jonker et al. [10] proposed a negotiation model called ABMP that can be characterized as cooperative one-to-one multi-criteria negotiation in which the privacy of both parties is protected as much as desired.

In Robu et al. [23], utility graphs were used to model issue dependencies for binary-valued issues. Our utility model is more general.

Bo et al. [1] proposed the design and implementation of a negotiation mechanism for dynamic resource allocation problem in cloud computing. Multiple buyers and sellers are allowed to negotiate with each other concurrently and an agent is allowed decommitment from an agreement at the cost of paying a penalty.

1) Sparse Connections  
![](/api/attachments/3EJD8RQ6/fulltext/images/e320529797a999a48cf53a00f8237f0d28d8d12ae6c38d7db94abb285a9705a2.jpg)

2) Dense Connections  
![](/api/attachments/3EJD8RQ6/fulltext/images/7b17e18d5fadd6b1115402882fbcf47aef9b72d0f929f8cc73459772232d217a.jpg)  
Fig. 6. Comparison of optimality when the number of agents changes.

![](/api/attachments/3EJD8RQ6/fulltext/images/374687356691a8778640b90919f69cdf533d03e1245143001c768d8259859c38.jpg)  
Fig. 7. Number of edges to be progressively removed (clustering parameter) v.s. QF.

Lin et al. [15,16] focus on the Expert Designed Negotiators (EDN) which is the negotiations between humans and automated agents in real-life. In addition, the tools for evaluating automatic agents that negotiate with people were proposed. These studies include some ef-<sup>fi</sup>cient results from extensive experiments involving many human subjects and PDAs.

## 6. Conclusion

In this paper, we proposed a new negotiation protocol, based on grouping issues, which can <sup>fi</sup>nd high-quality agreements in interdependent issue negotiation. In this protocol, agents generate their private issue interdependency graphs and use these to generate issue clusters. The mediator consolidates these clusters to de<sup>fi</sup>ne aggregate issue groups, and independent negotiations proceed for each group. We analyzed the negotiation that one of agents may always vote truthfully, while the other exaggerates so that its votes are always “strong.” We demonstrated that our proposed protocol results in a higher optimality rate than methods that don't use issue grouping, especially when the issue interdependencies are relatively sparse. In addition, the limitation of “strong” votes is effective at avoiding reduced social welfare in negotiations with exaggerators.

In future work, we will conduct additional negotiation, after the concurrent sub-contract negotiations, to try to increase the satisfaction of constraints that crossed issue group boundaries and were thus ignored in our issue grouping approach. We will also investigate using a variant of the Clarke tax [24] to address strategic nontruth-telling, wherein each agent has a limited budget from which it has to pay other agents before the mediator will accept a contract that favors that agent but reduces utility for the others. This approach has been applied successfully to bilateral negotiations: we will investigate whether and how this approach can be applied to the multilateral case.

## References

[1] B. An, V.R. Lesser, D. Irwin, M. Zink, Automated negotiation with decommitment for dynamic resource allocation in cloud computing, Proc. of the Ninth International Joint Conference on, Autonomous Agents and Multi-agent Systems (AAMAS-2010) 2010 pp. 981–988.

[2] S.S. Fatima M. Wooldridge N.R. Jennings An analysis of feasible solutions for multi-issue negotiation involving nonlinear utility functions Proc, of the Eighth International Joint Conference on Autonomous Agents and Multi-agent Systems (AAMAS-2009), 2007, pp. 1041–1048.

[3] S.S. Fatima, M. Wooldridge, N.R. Jennings, Approximate and online multi-issue negotiation, Proc. of the Sixth International Joint Conference on, Autonomous Agents and Multi-agent Systems (AAMAS-2007), 2007, pp. 947–954.

[4] K. Fujita, T. Ito, M. Klein, A representative-based multi-round protocol for multi-issue negotiations, Proc. of the Seventh International Joint Conference on, Autonomous Agents and Multi-agent Systems (AAMAS-2008), 2008, pp. 1573–1576.

[5] K. Fujita, T. Ito, M. Klein, An approach to scalable multi-issue negotiation: decomposing the contract space based on issue interdependencies, Proc. of the 2010 International Joint Conference on Intelligent Agent Technology (IAT-2010), 2010.

[6] M. Girvan, M.E.J. Newman, Community structure in social and biological networks, Proceedings of the National Academy of Sciences of the United States of America 99 (12) (2002) 7821–7826.

[7] R. Greenstadt, J. Pearce, M. Tambe, Analysis of privacy loss in distributed constraint optimization, Proc. of the 21th Association for the Advancement of, Arti<sup>fi</sup> cial Intelligence (AAAI-2006), 2006, pp. 647–653.

[8] K. Hindriks, C. Jonker, D. Tykhonov, Eliminating interdependencies between issues for multi-issue negotiation. Cooperative Information Agents X, Lecture Notes in Computer Science 4149 (2006) 301–316.

[9] T. Ito, H. Hattori, M. Klein, Multi-issue negotiation protocol for agents: exploring nonlinear utility spaces, Proc. of the 20th International Joint Conference on, Arti-<sup>fi</sup>cial Intelligence (IJCAI-2007), 2007, pp. 1347–1352.

[10] C.M. Jonker, V. Robu, J. Treur, An agent architecture for multi-attribute negotiation using incomplete preference information, Journal of Autonomous Agents and Multi-Agent Systems (JAAMAS) 15 (2007) 221–252.

[11] S. Kirkpatrick, C.D. Gelatt, M.P. Vecchi, Optimization by simulated annealing, Science 220 (4598) (1983) 671–680.

[12] M. Klein, P. Faratin, H. Sayama, Y. Bar-Yam, Negotiating complex contracts, Group Decision and Negotiation 12 (2) (2003) 58–73.

[13] S. Kraus, Strategic Negotiation in Multiagent Environments, Cambridge University Press, 2001.

[14] R.J. Lin, S.T. Chou, Bilateral multi-issue negotiations in a dynamic environment, Proc. of the AAMAS Workshop on Agent Mediated Electronic Commerce (AMEC-2003), 2003.

[15] R. Lin, S. Kraus, Can automated agents pro<sup>fi</sup>ciently negotiate with humans? Communications of the ACM 53 (1) (2010) 78–88.

[16] R. Lin, S. Kraus, Y. Oshrat, Y.K. Gal, Facilitating the evaluation of automated negotiators using peer designed agents, Proc. of the 24th Association for the Advancement of, Arti<sup>fi</sup>cial Intelligence (AAAI-2010), 2010.

[17] M. Lopez-Carmona, I. Marsa-Maestre, M. Klein, T. Ito, Addressing stability issues in mediated complex contract negotiations for constraint-based, non-monotonic utility spaces, Autonomous Agents and Multi-Agent Systems (2010) 1–50.

[18] R.T. Maheswaran, J.P. Pearce, P. Varakantham, E. Bowring, Valuations of possible states (vps):a quantitative framework for analysis of privacy loss among collaborative personal assistant agents, Proc. of the Forth International Joint Conference on Autonomous Agents and Multi-agent Systems (AAMAS-2005), 2005, pp. 1030–1037.

[19] T.W. Malone, M. Klein, Harnessing collective intelligence to address global climate change, Innovations Journal 2 (3) (2007) 15–26.

[20] I. Marsa-Maestre, M.A. Lopez-Carmona, J.R. Velasco, E. de la Hoz, Effective bidding and deal identi<sup>fi</sup>cation for negotiations in highly nonlinear scenarios, Proc. of the Eighth International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS-2009), 2009, pp. 1057–1064.

[21] I. Marsa-Maestre, M.A. Lopez-Carmona, J.R. Velasco, T. Ito, M. Klein, K. Fujita, Balancing utility and deal probability for negotiations in highly nonlinear utility spaces, Proc. of the Twenty-<sup>fi</sup>rst International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI-2009), 2009, pp. 214–219.

[22] F. Ren, M. Zhang, K.M. Sim, Adaptive conceding strategies for automated trading agents in dynamic, open markets, Decision Support Systems 46 (3) (2009) 704–716.

[23] V. Robu, D.J.A. Somefun, J.L. Poutre, Modeling complex multi-issue negotiations using utility graphs, Proc. of the Forth International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS 2005), 2005, pp. 280–287.

[24] T.W. Sandholm, Distributed rational decision making, in: G. Weiss (Ed.), Multi Agent Systems, 1998.

[25] D. Zhang, Axiomatic characterization of task oriented negotiation, Proc. of Twenty-<sup>fi</sup>rst International Joint Conference on, Arti<sup>fi</sup>cial Intelligence (IJCAI-2009), 2009, pp. 367–372.

![](/api/attachments/3EJD8RQ6/fulltext/images/4ca1633515efcc628bd528a1e285e13d33f4385b3a26e4f19d655225892d9a36.jpg)  
Dr. Katsuhide FUIITA is an Associate Professor of Faculty of Engineering, Tokyo University of Agriculture and Tech nology. He received the B.E., M.E, and Doctor of Engineering from the Nagova Institute of Technology, in 2008 2010, and 2011, respectively. From 2010 to 2011, he was a research fellow of the Japan Society for the Promotion of Science (JSPS). From 2010 to 2011, he was a visiting researcher at MIT Sloan School of Management. From 2011 to 2012, h was a Project Researcher of School of Engineering, the University of Tokyo. His main research interests includ multi-issue negotiation, multi-agent systems, intelligent agents, decision support systems and data mining.

![](/api/attachments/3EJD8RQ6/fulltext/images/e0a5217e48894034a7023617c367cfa6ade617aee9ede6776cb3800205fb6d17.jpg)

Dr. Takayuki ITO is an associate professor of Nagoya Institute of Technology. He received the B.E., M.E, and Doctor of Engineering from the Nagoya Institute of Technology in 1995, 1997, and 2000, respectively. From 1999 to 2001, he was a research fellow of the Japan Society for the Promotion of Science (JSPS). From 2000 to 2001, he was a visiting researcher at USC/ISI (University of Southern California/Information Sciences Institute). From April 2001 to March 2003, he was an associate professor of Japan Advanced Institute of Science and Technology (JAIST). From 2005 to 2006, he is a visiting researcher at Division of Engineering and Applied Science, Harvard University and a visiting researcher at the Center for Coordination Science, MIT Sloan School of Management. From

2008 to 2010, he was a visiting researcher at the Center for Collective Intelligence, MIT Sloan School of Management. From 2010, he is a senior researcher of the Policy Alternatives Research Institute, University of Tokyo. He is a board member of IFAAMAS, the PC-chair of AAMAS2013, PRIMA2009, and was a SPC/PC member in many top-level conferences (IJCAI, AAMAS, ECAI, AAAI, etc.). He received the Prize for Science and Technology (Research Category), the Commendation for Science and Technology by the Minister of Education, Culture, Sports, Science, and Technology, 2013, the Young Scientists' Prize, the Commendation for Science and Technology by the Minister of Education, Culture, Sports, Science, and Technology, 2007, the Nagao Special Research Award of the Information Processing Society of Japan, 2007, the Best Paper Award of AAMAS2006, the 2005 Best Paper Award from Japan Society for Software Science and Technology, the Best Paper Award in the 66th annual conference of 66th Information Processing Society of Japan, and the Super Creator Award of 2004 IPA Exploratory Software Creation Projects. He is the Principle Investigator of the Japan Cabinet Funding Program for Next Generation World-Leading Researchers (NEXT Program). Further, he has several companies, which are handling web-based systems and enterprise distributed systems. His main research interests include multi-agent systems, intelligent agents, group decision support systems, agent-mediated electronic commerce, and software engineering on offshoring.

![](/api/attachments/3EJD8RQ6/fulltext/images/f9a3805f5cec0379c10cb2b912162c5e2591877502e7f81ce7e4547438ff6c40.jpg)

Dr. Mark Klein (http://cci.mit.edu/klein/) is a Principal Research Scientist at the MIT Center for Collective Intelli gence, as well as an Af<sup>fi</sup>liate at the MIT Computer Science and AI Lab (CSAIL) and the New England Complex Systems Institute (NECSI). His research draws from such <sup>fi</sup>elds as computer science, economics, operations research, and complexity science in order to develop and evaluate com puter technologies that enable greater ‘collective intelligence’ in large groups faced with complex decisions, especially those in the sustainability realm. His current projects are looking at: large-scale on-line deliberation; negotiation protocols for problems with many interdependent issues; knowledge management that integrates virtual reality and social media; and managing ‘emergent’ dysfunction in large-scale networked systems. He has also made contributions in the areas of computer-supported con<sup>fl</sup>ict management for collaborative design, design rationale capture, business process re-design, exception handling in work<sup>fl</sup>ow and multi-agent systems and service discovery.
