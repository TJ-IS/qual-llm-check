---
otero_id: 26728
otero_key: "KCR5XAGX"
title: "A Computational Study of Distributed Rule Learning"
authors: "Riyaz Sikora; Michael J. Shaw"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.2.189"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Information Systems Research

## HSR Information Systems Research

![](/api/attachments/KCR5XAGX/fulltext/images/0447f7c0056dbb75bc22cd31a914d8f69227ee18c7462f4580658f8b420553a8.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## A Computational Study of Distributed Rule Learning

Riyaz Sikora, Michael J. Shaw,

## To cite this article:

Riyaz Sikora, Michael J. Shaw, (1996) A Computational Study of Distributed Rule Learning. Information Systems Research 7(2):189-197. https://doi.org/10.1287/isre.7.2.189

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

## informs®

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Computational Study of Distributed Rule Learning

Riyaz Sikora • Michael J. Shaw

Industrial and Manufacturing Systems Engineering, The University of Michigan-Dearborn,

4901 Evergreen Road, Dearborn, Michigan 48128

rsikora@umich.edu

Beckman Institute for Advanced Science and Technology, The University of Illinois at Urbana-Champaign,
405 N. Mathews Avenue, Urbana, Illinois 61801
mshaw@ux1.cso.uiuc.edu

This report is concerned with a rule learning system called the Distributed Learning System (DLS). Its objective is two-fold: First, as the main contribution, the DLS as a rule-learning technique is described and the resulting computational performance is presented, with definitive computational benefits clearly demonstrated to show the efficacy of using the DLS. Second, the important parameters of the DLS are identified to show the characteristics of the Group Problem Solving (GPS) strategy as implemented in the DLS. On one hand this helps us pinpoint the critical designs of the DLS for effective rule learning; on the other hand this analysis can provide insight into the use of GPS as a more general rule-learning strategy.

(Group Problem Solving; Genetic Algorithms; Group Learning; Hybrid Learning System)

## 1. Introduction

This report describes the Distributed Learning System (DLS) for rule induction. The problem of rule learning, or rule induction, from examples is a widely studied problem in the area of machine learning. Algorithms like ID3 (Quinlan 1986) and PLS1 (Rendell 1990) are a few of the successful algorithms for learning from examples. The problem of rule learning can be simply stated as follows: based on a set of positive and negative examples of a concept, infer a description or hypothesis of the concept that correctly explains all the positive examples without covering any of the negative examples.

Rule learning techniques are important for information management because of their ability to generate useful decision knowledge out of the data. As such, effective rule learning can be used to sort out the vast amount of data typical in today's enterprise information systems, and convert them into a much more manageable set of rules that nicely summarizes the essence of the knowledge underlying the data (Shaw 1993). The knowledge learned can also provide insight for developing more desirable decision strategy. One example of applying rule learning to business information management is using it to generate credit-granting rules out of the database of past application cases (Shaw and Gentry 1988); another example is to learn the consumer profiles and purchasing behaviors based on point-of-sale data collected by retailers (Currim et al. 1988, Ing and Mitchell 1994).

It has been well established that rule learning can be viewed as a problem-solving process, and most existing rule-learning algorithms operate on a training data set to find the concept (or rules) for explaining the data. From the standpoint of McGrath's (1984) taxonomy of task types, rule learning may be characterized as a combination of intelligence, creativity, and preference. Because of its involvement with these multiple task types, it can potentially benefit from the use of group problem solving (GPS). Computationally, the GPS method for rule learning is analogous to the "group induction" process studied in the psychology literature (Laughlin and

Figure 1 The Distributed Learning System Using Group Problem Solving  
![](/api/attachments/KCR5XAGX/fulltext/images/8b39380691b1d09aefe69e01504cbff904854c8736cc20636413be5ad676778b.jpg)

Shippy 1983). In DLS, we incorporate the GPS approach to learning from examples in which the data set is divided among the different agents (rule learning programs) and they infer a set of hypotheses based on their individual data subsets. The agents then engage in group interaction based on their individual solutions to reach a consensus about a group solution. In this report, we use the GPS strategy as a paradigm to examine how decomposition and distribution can be incorporated to enhance rule learning computationally.

The Distributed Learning System (DLS) presented in this report implements a restricted version of the GPS, where the group, consisting of identical learning agents, uses a decomposition strategy to distribute the data set and infer a hypothesis. It is helpful to characterize the DLS as using a GPS strategy because of the potential of extending the DLS by incorporating different learning algorithms as agents in the group. Just as the decomposition strategy used by Dantzig and Wolfe (1961) has implications for coordination in organizations, the use of the decomposition strategy in DLS has useful implications for evaluating GPS parameters, such as data distribution schemes, diversity, group size, and group strategies.

What this report is aiming at accomplishing is twofold: First, as the main contribution, the Distributed Learning System as a rule-learning technique is described and the resulting computational performance is presented, with definitive computational benefits clearly demonstrated to show the efficacy of the DLS.

Second, the important parameters of the DLS are identified to show the characteristics of the GPS strategy as implemented in the DLS. On one hand this helps us pinpoint the critical designs of the DLS for effective rule learning; on the other hand this analysis can provide insight into the use of GPS as a more general rule-learning strategy for future research.

The rest of the report is organized as follows: in §2 we discuss the Distributed Learning System (DLS); in §3 we present an example that compares the performance of the group problem-solving approach to that of a single-agent approach; in §4 we investigate the effect of various parameters on the performance of DLS; in §5 we present a discussion of the results; and §6 concludes the report.

## 2. The Distributed Learning System

The task of rule learning is concerned with deriving rules that can best explain a set of training examples. In the traditional approach to rule learning, a single learning program is used that generates a hypothesis and successively refines it to explain all the examples. Since the process involves generating and evaluating hypotheses at each stage, it may conceivably benefit from using a group problem-solving approach where the examples are distributed to different learning programs and they are allowed to interact to reach a consensus about the final hypothesis.

Such a group problem-solving approach is implemented in the Distributed Learning System (DLS). Since a learning agent is now working on only a fraction of the original problem and the different agents can work asynchronously, this method of distributing the amount of resources (data) can make the process parallel in nature. At the same time, by using multiple agents that provide several different hypotheses of the solution, it can potentially provide better performance. However, the performance of the group also depends on the circumstances in which the group problem-solving process is being conducted.

The GPS paradigm has been extensively and independently studied in the Distributed Artificial Intelligence (DAI) (Huhns 1987, Bond and Gasser 1988) and Group Decision Support Systems (GDSS) (Nunamaker et al. 1988, Kraemer and King 1988, DeSanctis and

Gallupe 1987) communities. Although DAI is concerned with computational agents and GDSS is concerned with human agents, they both share the common objective of coordinating the problem solving by a group of agents. More recently, there has been some interdisciplinary work aimed at addressing the core issues related to GPS (Durfee 1991). A number of GPS models have been developed based on the blackboard model (Lesser 1991), the scientific community model (Kornfield and Hewitt 1981), the negotiation model (Sycara 1991, 1993), and the multiagent model (Huhns and Bridgeland 1991, Guha and Lenat 1994).

Figure 1 illustrates the DLS, modeling the group problem-solving approach to rule learning. The detailed implementation of DLS is described in Sikora and Shaw (1994). In this report, we focus on the incorporation of the GPS paradigm and the computational study. Each agent in DLS is an implementation of the probabilistic learning system, PLS1 (Rendell 1990). The figure also illustrates the different steps in the distributed, group problem-solving approach (Smith and Davis 1981). The four steps correspond to: (1) problem decomposition, (2) subproblem allocation, (3) subproblem solution, and (4) solution synthesis. At first, the problem (or data set) P is decomposed into different subproblems $P_{1}, P_{2} \cdots P_{n}$ , which are then allocated to different inductive learning programs (or agents). Each agent solves its subproblem independently of the other agents. The individual solutions are then synthesized into a final solution.

Each agent's solution can be thought of as an alternative hypothesis being suggested by that agent. The final step corresponds to the group decision-making process where, at each stage, every agent proposes a solution and the group deliberates on the strengths and weaknesses of each alternative. Each agent then refines its solution and the above process repeats itself until all the group members reach a consensus. The solution synthesis phase of the DLS, implemented by a genetic algorithm (GA) (Holland 1975, Goldberg 1989), is designed to simulate the evolution of a group solution resulting from group interaction and coordination. To actually make the agents interact with each other entails the design of a communication protocol and language, which is not the intent of this paper. In general, a GA can be used to simulate the group adaptation process in any GPS situation as long as the solutions, that the agents are working towards, can be encoded in a string-like structure used by a GA.

In order to simulate the group activity by which the members jointly learn rules from the data set, we use an unbiased random sampling technique called the jackknife technique (Efron 1982) to decide the initial data distribution. In the jackknife technique, one or more data points are randomly removed from the data set to obtain a sample. We define a decomposability index, d, that controls the redundancy among the different subsets of data generated. That is, d is the expected fraction of the data set obtained by an agent. Stated differently, for a given decomposability index d, each example in the data set has a probability d of being assigned to any agent. Since all the agents in our case are homogeneous, we simulate the diversity in their proposed solutions by providing each with a different perspective (i.e., a different sample) of the same problem.

## 3. Computational Advantages of the DLS: An Example

In this section, we present an example to compare the performance of the group problem-solving approach discussed before to that of a single-agent approach, using the problem of rule learning as the underlying domain. For the empirical analysis, a large set of real-world data from a chemical plant was used for all the experiments discussed in this and the next section. The problem related to the control of a chemical process, producing a certain chemical product, with about 30 process variables. In the process of producing the product, an undesirable byproduct was produced, which was not measured directly. To remove this byproduct, an expensive chemical was added in just sufficient quantities. The problem was to change the controllable process variables (nine out of the thirty variables) so that the usage of the expensive chemical was minimized. Since there were no theoretical formulae linking the process variables with the amount of the product produced, the only way to solve this problem was to induce the relationships based on a set of actual plant readings. The problem was formulated as a single concept learning problem by considering the examples corresponding to a large quantity of the expensive chemical used as being positive examples and the rest as negative examples.

The data set had 572 instances, of which 355 were positive examples and 217 were negative examples. It was randomly broken up into a training set of 458 examples and a testing set of 114 examples. In this section, we present an example to show the advantage of using a multiagent group problem-solving approach to inductive learning vis-à-vis that of using a single-agent approach. The concept learning problem (single-agent) can be stated as follows: based on a set of positive and negative examples of a concept, infer a description or hypothesis of the concept that correctly explains all the positive examples without covering any of the negative examples. The group problem-solving approach to the same concept learning problem can then be termed as follows: distribute the data set among several agents as their given initial belief; let them induce a concept description or hypothesis explaining their data subsets; and based on the information exchange about their individual results, let them reach a group consensus about the final concept.

The following parameter values were used for the DLS: n = 5 and d = 0.2. The detailed empirical results for different values of n and d are given in §4 where we show that the best performance is obtained for these parameters values. In this section, we discuss the computational advantages of using the group problem-solving approach over the single-agent approach to inductive learning, where we used the whole training set of 458 instances on the PLS1 program (with s = 1). $^{1}$ The learning performance of the system as a whole was measured by decision quality determined by prediction accuracy and rule-size (i.e., the length of the concept generated). The result from the single-agent approach, in which PLS1 is used to solve the whole problem, was as follows:

$$
\text { Prediction   Accuracy } = 83.3 \%; \quad \text { Rule   Size } = 17.
$$

Table 1 shows the results obtained by DLS when GPS is applied. Also shown in Table 1 are the performance of each individual learning agent used by the DLS to solve the subproblems.

Table 1 Computational Performance Results of Applying the DLS

<table><tr><td>Agents</td><td>Prediction Accuracy</td><td>Rule Size</td></tr><tr><td>Agent 1</td><td>74.6%</td><td>4</td></tr><tr><td>Agent 2</td><td>75.4%</td><td>4</td></tr><tr><td>Agent 3</td><td>79.8%</td><td>4</td></tr><tr><td>Agent 4</td><td>76.3%</td><td>4</td></tr><tr><td>Agent 5</td><td>76.3%</td><td>5</td></tr><tr><td>Synthesis</td><td>86%</td><td>3</td></tr></table>

The best result given by an individual agent (agent 3) was: accuracy = 79.8% and rule-size = 4, and the final result obtained by the group problem-solving approach was: accuracy = 86% and rule-size = 3. Thus, the synthesis step, modeling the evolution of group solution from the individual solutions resulting from group interaction and coordination, improves upon the individual results given by the agents by a minimum of about 9% in accuracy and 25% in rule-size, and is better than the single-agent result by about 3.2% in accuracy and about 82% in rule-size.

While the above result shows that the performance of the group is better than the performance of a single learning agent, one may argue that the superior performance of DLS is due to the combination of two algorithms (PLS1 and GA), and not because of the inherent differences in the systems owing to group versus solo activity. To test this hypothesis, we carried out another set of experiments where GA was made available even to the single agent. The GA would take the output from the single agent and work in the same way as described earlier. The following results, averaged over five experiments, were observed from the single-agent version of DLS, i.e., a learning agent combined with the GA:

$$
\text { Prediction   accuracy } = 82.1 \%; \quad \text { Rule   size } = 15.
$$

These results show that the performance of the learning agent actually decreases (from 83.3% accuracy when single-agent learning is used) when it is combined with a GA. Although this phenomenon seems strange at first it becomes clear when one considers the role played by the GA in the learning system. As has been emphasized earlier, the GA is used as a model for the evolution of group solutions from the individual solutions of the agents. The GA works by combining the diverse and the best parts of the hypotheses generated by the agents. However, when the GA is applied to only a single set of hypotheses, there is a marked absence of diversity and the GA ends up combining the different parts of the same hypothesis set. This leads to the weaker parts of the set getting combined with the better ones, resulting in a decline in the overall quality of the hypothesis set. This analysis also sheds light on the synergistic effects of the group problem-solving process in solving the learning problem. More importantly, this experiment shows that mere combination of two methods sometimes can actually lead to inferior solutions, and demonstrates that the improvement brought on by the DLS is in fact due to the group problem-solving approach rather than just the combination of two methods.

It can be argued that the DLS essentially contains just one agent that decomposes the data, goes through iteratively working on each of the subsets of data separately, and uses a GA to synthesize the different results it has generated. Algorithmically, this is correct. As we have mentioned earlier, the above algorithm is used to simulate the group process. The different results generated by the agent on different subsets simulate the results given by the different agents. The GA simulates the group interaction and information exchange process. The DLS can be further extended by actually using different learning programs as different agents, rather than using the same learning program as was done in these experiments.

## 4. Experimental Study

The example presented in the last section compared the performance of the GPS approach to rule learning with the traditional single-agent approach. However, the performance of the GPS approach depends on several factors, such as the number of agents used, the kind of problem decomposition used, etc. (Nunamaker et al. 1988). In this section, we present an empirical study designed to test the effect of these variables on the performance of the GPS approach.

We use the same Distributed Learning System, implemented in Common Lisp on a TI-Explorer machine, for this empirical study. The same real world data set from the chemical process control problem was used for all the experiments discussed in this section. As in the previous experiment, the data set was randomly broken up into a training set of 458 and a testing set of 114 examples. All the results given are the average of 5 runs with a different training and testing set used in each run. The following parameter values for the GA were used for all the experiments: total number of generations used was 100, Baker's (1987) SUS algorithm was used for selection, the uniform crossover operator was used with probability 0.7, and the probability of mutation was 0.05. The population size corresponds to the number of unique alternatives generated by the group.

The performance of DLS, simulating the group problem-solving task of rule learning, was measured in terms of (1) decision quality, given by prediction accuracy and rule-size; and (2) number of unique alternatives generated.

## 4.1. Effect of Data Distribution

Table 2 presents the results of the group problem-solving approach for different degrees of data distribution among the members. The distribution of data is reflected in a parameter d, which is the decomposability index. The decomposability index, d (see section 2 for explanation), corresponds to the fraction of the total data (in our case, the number of training examples) allocated to each agent.

One can identify a general trend from Table 2 that the group performance is best when the data (resources) are about equally divided among the agents. The GPS approach can, therefore, achieve more with the same amount of resources. This observation is, however, not validated for the case when n = 10. This can be explained by the fact that dividing up the resources among too many agents leaves each with an insufficient amount of the resources. It also indicates that the group size is an important group parameter. To realize the benefits of the GPS approach one has to enforce the proper group parameters. This is also confirmed by the results on the effect of the group size, discussed next.

## 4.2. Effect of Group Size

In this part of the experiments we attempt to analyze the effect of varying the group size on the DLS performance measured by the decision quality and number of unique solution-candidates generated. Table 3 extracts the relevant information from Table 2.

Table 2 DLS Results for Different Values of n and d

<table><tr><td colspan="4"> $n = 1$ </td></tr><tr><td> $d$ </td><td>Prediction Accuracy</td><td>Rule-Size</td><td>No. of Unique Alternatives Generated</td></tr><tr><td>1.0</td><td>85.4%</td><td>17.4</td><td>17.4</td></tr><tr><td></td><td></td><td> $n = 2$ </td><td></td></tr><tr><td>0.05</td><td>70.4%</td><td>2.2</td><td>5.4</td></tr><tr><td>0.1</td><td>72.1%</td><td>2.4</td><td>5.6</td></tr><tr><td>0.2</td><td>79.8%</td><td>3.2</td><td>11.4</td></tr><tr><td>0.4</td><td>81.1%</td><td>3.6</td><td>16</td></tr><tr><td>0.5</td><td>85.1%</td><td>3.4</td><td>21.4</td></tr><tr><td>0.6</td><td>83.9%</td><td>2.8</td><td>21.8</td></tr><tr><td>0.8</td><td>80.5%</td><td>2.8</td><td>25</td></tr><tr><td></td><td></td><td> $n = 5$ </td><td></td></tr><tr><td>0.05</td><td>73%</td><td>2</td><td>9</td></tr><tr><td>0.1</td><td>78.8%</td><td>2.8</td><td>14.4</td></tr><tr><td>0.15</td><td>81.6%</td><td>3</td><td>20.8</td></tr><tr><td>0.2</td><td>86.9%</td><td>3.2</td><td>29.2</td></tr><tr><td>0.4</td><td>84.1%</td><td>2.8</td><td>44</td></tr><tr><td>0.6</td><td>81.9%</td><td>2</td><td>49.6</td></tr><tr><td>0.8</td><td>82%</td><td>2.8</td><td>50</td></tr><tr><td></td><td></td><td> $n = 7$ </td><td></td></tr><tr><td>0.05</td><td>77.2%</td><td>3</td><td>15.4</td></tr><tr><td>0.1</td><td>82.6%</td><td>3.4</td><td>23.2</td></tr><tr><td>0.15</td><td>80.5%</td><td>3</td><td>29.6</td></tr><tr><td>0.2</td><td>80.7%</td><td>2.8</td><td>35.2</td></tr><tr><td>0.4</td><td>80.9%</td><td>2.8</td><td>50</td></tr><tr><td>0.6</td><td>81.6%</td><td>3</td><td>50</td></tr><tr><td></td><td></td><td> $n = 10$ </td><td></td></tr><tr><td>0.05</td><td>77.4%</td><td>2.8</td><td>22.6</td></tr><tr><td>0.1</td><td>78.4%</td><td>3.8</td><td>31.6</td></tr><tr><td>0.15</td><td>81.2%</td><td>3</td><td>41.8</td></tr><tr><td>0.2</td><td>80%</td><td>3</td><td>47.6</td></tr><tr><td>0.4</td><td>82.3%</td><td>2.8</td><td>&gt;50</td></tr><tr><td>0.6</td><td>80.5%</td><td>3.2</td><td>&gt;50</td></tr><tr><td>0.8</td><td>81.6%</td><td>3.6</td><td>&gt;50</td></tr></table>

As can be expected, the number of unique alternatives generated by the group increases with an increase in group size. However, the marginal increase in the number of unique alternatives generated decreases as the group size increases. In terms of quality of the decision, although rule-size more or less remains the same, there is a distinct trend with respect to the prediction accuracy. The accuracy peaks when five agents are used and then consistently drops as the group size increases. This clearly shows the dependence of group performance on group size. However, it remains explaining why the performance peaks at a certain group size and then decreases. We will return to answer this question in the next section.

## 4.3. Effect of Diversity Among Agent's Data

Diversity in a group problem-solving situation has several dimensions. The agents may differ in: (1) the knowledge (i.e., procedures and expertise) they possess; (2) the individual beliefs about the problem; (3) the strategies they apply in pursuing the solution; and (4) the goals of the individuals. In our controlled experiments, the agents apply the same set of procedures and strategies to collaborate on the same learning problem. So the only source of diversity comes from the data given to them, which can be viewed as their individual beliefs.

In this subsection, we test the effect on group performance of varying the degree of diversity in the hypotheses generated by the agents. Since the best group performance was obtained when five agents were used, we focus on the case with a group size of five. Table 4 shows the results of the experiment.

Table 3 Effect of Group Size on DLS Performance

<table><tr><td>No of Agents</td><td>Prediction Accuracy</td><td>Rule-Size</td><td>No. of Unique Alternatives Generated</td><td>Amount of Resources Available to Each Agent</td></tr><tr><td>1</td><td>85 4%</td><td>17 4</td><td>17.4</td><td>1</td></tr><tr><td>2</td><td>85 1%</td><td>3.4</td><td>21.4</td><td>1/2</td></tr><tr><td>5</td><td>86 9%</td><td>3.2</td><td>29.2</td><td>1/5</td></tr><tr><td>7</td><td>80 5%</td><td>3</td><td>29.6</td><td>1/7</td></tr><tr><td>10</td><td>78.4%</td><td>3.8</td><td>31 6</td><td>1/10</td></tr></table>

Table 4 Effect of Diversity Among Agents' Data on DLS Performance

<table><tr><td colspan="4">n = 5 d = 0.2</td></tr><tr><td>Diversity Number</td><td>Prediction Accuracy</td><td>Rule-Size</td><td>Number of Alternatives Generated</td></tr><tr><td>1</td><td>79.3%</td><td>2.8</td><td>26</td></tr><tr><td>2 (2 + 3)</td><td>81.1%</td><td>2.2</td><td>27.6</td></tr><tr><td>2 (1 + 4)</td><td>81.2%</td><td>2.2</td><td>31.4</td></tr><tr><td>3 (1 + 1 + 3)</td><td>83.5%</td><td>2.8</td><td>30.4</td></tr><tr><td>3 (1 + 2 + 2)</td><td>84.4%</td><td>4</td><td>26.2</td></tr><tr><td>4 (1 + 1 + 1 + 2)</td><td>82.3%</td><td>2.8</td><td>31</td></tr><tr><td>5</td><td>86.9%</td><td>3.2</td><td>29.2</td></tr></table>

The diversity number corresponds to the degree of diversity in the data given to the agents. For example, diversity number “3 (1 + 2 + 2)” corresponds to having a total of three different data sets given to the group of five agents, with two agents getting the same data set as two other agents. The results show that the decision quality, as measured by prediction accuracy, depends on diversity. Moreover, there is a general trend of increasing accuracy with an increase in such diversity among the data given to the learning agents.

## 5. Discussion of Results

The GPS approach used in DLS embodies two fundamental problem solving strategies: decomposition and diversification. The decomposition used in DLS is basically a divide-and-conquer method to break the problem into simpler subproblems to tackle. Interestingly, just as the way we gains insight into group problem-solving strategies through DLS, the decomposition approaches to solving optimization problems are, besides being used as a solution strategy (Dantzig and Wolfe 1961, Burton et al. 1974), also used to model decision making in decentralized organizations. On the one hand it helps solve difficult problems by transforming them into several subproblems that have simpler structures and are easier to solve; on the other hand, the decomposition process helps introduce parallelism into the solution process which may potentially benefit from parallel computing. Diversification has been pointed out before as an important strategy for general problem solving and optimization (Brady 1985). DLS uses the diversity among its learning agents to maintain a sufficient set of fit partial solutions.

The group problem-solving paradigm implemented in DLS assumes that the problem can be decomposed into independent subproblems. This is the case for rule learning from training examples. This problem structure simplifies group problem-solving considerably, since each agent can be totally autonomous without having to depend on the solution processes of other agents. When the solution processes of different agents are interdependent, there must be more interactions among the agents and the group performance becomes more contingent upon the ability of the agents to coordinate. When the subproblems are highly dependent, the group behaviors we found in relation to group size, diversity, and data distribution might not exist.

In the experimental study, we showed the performance improvement obtained by the DLS over that of a single learning agent. The group performance was found to depend on the group size, the distribution of data, and the diversity (in the data) among the agents. The decision quality, measured by the prediction accuracy, peaked when a certain number of agents (five in our experiments) with equally distributed data were used. The group performance then decreased as the group size was increased. To rationalize this phenomenon, consider once again the effect of the group size on the group performance, as summarized in Table 3.

There are two opposing forces affecting the group performance as the group size increases. Since the resources (that is, the training examples) are equally divided among the group members, the amount of resources available to each member decreases with an increase in the group size, and consequently the quality of output from individual members suffers. At the same time, the number of unique alternatives generated by the whole group increases as the group size is increased. Because of these opposing effects of decreasing quality of the individual outputs and increasing number of the alternatives generated, the group performance peaks at a certain group size and then starts to decrease.

The DLS presented in this paper employs a restricted version of GPS. That is, the group of agents consists of identical rule-learning programs, whose diversity is reflected solely by the data assigned to each individual. However, the computational advantages demonstrated by the DLS's performance show the promise of GPS as a paradigm for rule learning, which may be further perfected by, for example, incorporating different learning strategies in the learning agents (Michalski and Tecuci 1993) to accentuate the effect of group diversity. Moreover, although the DLS uses GPS only as a rule-learning paradigm, the emphasis on the group metaphor, the decomposition strategy, and data distribution makes it suitable for parallel processing, which should further enhance the learning system's computational performance.

## 6. Conclusions

In this report we have investigated the application of the GPS paradigm to the domain of machine learning—specifically inductive rule learning. The GPS paradigm has been extensively studied by the DAI and GDSS communities, and many studies have shown the importance of such group parameters as group size, the makeup of the group, task allocation, and the group's diversity on the group performance. We have applied the GPS paradigm to inductive rule learning and have demonstrated that it can be very beneficial in terms of producing more accurate rules, and it can also be used to understand the performance sensitivity of DLS to various parameters.

It should be noted that the particular type of group problem as solved by our distributed learning system is characterized by the decomposability of the problems' structure. That is, the subproblems given to the group of agents are independent. There are other distributed problem-solving (DPS) applications, however, where the tasks are not easily decomposable and the agents need to cooperate to reach a solution. An example is Lesser's (1991) functionally accurate/cooperative (FA/C) paradigm that uses cooperative control mechanisms to coordinate agents.

The performance experiments in §3 show that DLS performs better than single-agent learning techniques. By the same token, one can reason that the DLS may be extended by using a variety of inductive learning algorithms as agents, provided we make sure that the reppresentations used by the learning agents are made compatible with that of the GA. Since the concept of $bias^{2}$ is an important one in inductive learning and since different algorithms use different biases (either implicitly or explicitly), using different algorithms in DLS as different agents provides a unique approach of using multiple biases. This also has important implications in terms of solution (hypothesis) quality and efficiency, because it is usually not known a priori which bias is suitable for the problem at hand, and use of the wrong bias can sometimes make the problem inefficient or hard to learn. Thus, combining different rule-learning algorithms can help avoid the problem of choosing the right bias and result in improved performance.

Although a specific problem domain of rule learning was used in this report, the general model can be extended to other domains that have traditionally been solved by the single-agent paradigm of problem-solving. For example, the design of a survivable networks in telecommunication network management (Davis et al. 1993) over a wide geographic area can benefit from a GPS type approach where the problem is decomposed into smaller and manageable geographic areas. The individual designs for these smaller subproblems is then synthesized by an iterative process of a GA. In some applications, like air traffic control, it is difficult if not impossible to collect all the necessary data at one place. In such applications, a GPS-type approach is more suitable. The local data residing at different locations can be individually processed (by local agents) and the final solution (a flight path for an airplane) can be generated by a group synthesis process such as a GA.

To generalize the results to group problem-solving situations where subproblems assigned to different agents may be interdependent, more complex strategies must be considered. To extend our model, a possible source of ideas may again come from mathematical programming problems. When there are indecomposable constraints in applying Dantzig-Wolfe decomposition, those constraints are moved to the objective function in the form of Lagrangian functions (Lasdon 1968). In group problem-solving, this may correspond to moving the interdependent constraints to the group level by incorporating them into the fitness function of the GA. Thus, the need for the agents to cooperate in seeking the group solution may be reflected in the extended model in which the ability to cooperate (i.e., to meet the constraints imposed by other agents) defines at least a portion of the fitness of an agent's solution.

## References

Baker, J. E., "Reducing Bias and Efficiency in the Selection Algorithm," Proc Second International Conf. on Genetic Algorithms, MIT, Cambridge, MA, 1987, 14–21.

Bond, A. and L. Gasser, Readings in Distributed Artificial Intelligence, Morgan Kaufmann Publishers, San Mateo, CA, 1988.

Brady, R M., "Optimization Strategies Gleaned from Biological Evolution," Nature, 317 (October 1985), 804–806

Burton, R. M., W. W. Damon, and D. W. Loughridge, "The Economics of Decomposition: Resource Allocation vs. Transfer Pricing," Decision Sciences, 5, 3(1974), 297–310

Currim, I S., R. J. Meyer, and N T. Le, "Disaggregate Tree-Structured Modeling of Consumer Choice Data," J. Marketing Res., 25 (August 1988), 253–265.

Dantzig, G. and P Wolfe, "The Decomposition Algorithm for Linear Programming," Econometrica, 29, 4(1961), 767–778

Davis, L., D Orvosh, A. Cox, and Y Qiu, "A Genetic Algorithm for Survivable Network Design," Proc Fifth International Conf on Genetic Algorithms, Morgan Kaufmann Publishers, San Mateo, CA, 1993, 408–415.

Desanctis, G. and R. B. Gallupe, "A Foundation for the Study of Group Decision Support Systems," Management Sci., 33, 5(May 1987), 497–509.

Durfee, E. H., Guest Editor, IEEE Trans. Systems, Man, and Cybernetics, Special Issue on Distributed Artificial Intelligence, 21, 6(1991).

Efron, B., The Jackknife, the Bootstrap and Other Resampling Plans., SIAM, Philadelphia, PA, 1982.

Goldberg, D., Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley, Reading, MA, 1989.

Guha, R. and D. Lenat, "Enabling Agents to Work Together," Comm ACM, 37, 7(July 1994), 126-142.

Holland, J., Adaptations in Natural and Artificial Systems, University of Michigan Press, Ann Arbor, MI, 1975.

Huhns, M. N. and D. M. Bridgeland, "Multiagent Truth Maintenance," IEEE Trans Systems, Man, and Cybernetics, 21, 6(Nov. 1991), 1437-1445

——, (Ed.), Distributed Artificial Intelligence, Pitman, London, 1987

Ing, D and A. Mitchell, "Point-of-Sale Data for Consumer Goods Marketing Transforming the Art of Marketing into the Science of Marketing," in Marketing Information Revolution, Blattberg, Glacer, and Little (Eds), Harvard Business School Press, Cambridge, MA, 1994.

Kornfeld, W. and C. Hewitt, "The Scientific Community Metaphor," IEEE Trans Systems, Man, and Cybernetics., 11 (1981), 24–33.

Kraemer, K. L. and J. L. King, "Computer-Based Systems for Cooperative Work and Group Decision Making," ACM Computer Survey, 20 (1988), 329–380.

Lasdon, L. S., "Duality and Decomposition in Mathematical Programming," II.EE Trans Systems, Man, and Cybernetics, 4 (1968), 86-100.

Laughlin, P. R and T. A Shippy, "Collective Induction," J. Personality and Social Psychology, 45 (1983), 94–100

Lesser, V R, "A Retrospective View of FA/C Distributed Problem Solving" IEEE Trans. Systems, Man, and Cybernetics, 21, 6(Nov. 1991), 1347–1362

McGrath, J., Groups Interaction and Performance, Prentice Hall, Englewood Cliffs, NJ, 1984

Michalski, R. and G. Tecuci, Proc. Second International Workshop on Multistartegy Learning (Eds.), Center for Artificial Intelligence, George Mason University, Fairfax, VA, May 26–29, 1993.

Nunamaker, J., L. Applegate, and B. Konsynski, "Computer-Aided Deliberation Model Management and Group Decision Support," Operations Res., 36, 6(Nov-Dec. 1988), 826-848.

Quinlan, J. R., "Induction of Decision Trees," Machine Learning, 1, (1986), 81-106.

Rendell, L. A., "Induction as Optimization," IEEE Trans Systems, Man, and Cybernetics, 20, 2(1990), 326–328

Shaw, M J, (Guest Editor), Special Issue on Machine Learning Methods for Intelligent Decision Support, Decision Support Systems, 10, 2(1993)

—, and J Gentry, "An Expert System with Inductive Learning for Business Loan Evaluation," Financial Management, Fall (1988), 45–55.

Sikora, R and M. Shaw, "A Double-Layered Learning Approach to Acquiring Rules for Classification: Integrating Genetic Algorithms with Similarity-based Learning," ORSA J. Computing, 6, 2(Spring 1994), 174–187.

Smith, R G. and R Davis, "Frameworks for Cooperation in Distributed Problem Solving," IEEE Trans Systems, Man, and Cybernetics, SMC-11, 1 (1981), 61–70

Sycara, K., "Machine Learning for Intelligent Support of Conflict Resolution," Decision Support Systems, 10 (1993), 121–136
——, "Problem Restructuring in Negotiation," Management Sci., 37, 10 (1991), 1248–1268

Thomas W. Malone, Associate Editor. This paper was received on April 9, 1991 and has been with the authors 15 months for 4 revisions.
