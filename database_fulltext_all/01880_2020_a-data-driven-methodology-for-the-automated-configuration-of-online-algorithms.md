---
otero_id: 1880
otero_key: "CFNZZPHK"
title: "A data-driven methodology for the automated configuration of online algorithms"
authors: "Fabian Dunke; Stefan Nickel"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113343"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

A data-driven methodology for the automated configuration of online algorithms

ELSEVIE Decision Support Systems

Fabian Dunke, Stefan Nickel

![](/api/attachments/CFNZZPHK/fulltext/images/e908ecfd40fea989695aac156aec9b0b4ff25a1901c5b81343107ce0e9ba8d61.jpg)

PII: S0167-9236(20)30098-1

DOI: https://doi.org/10.1016/j.dss.2020.113343

Reference: DECSUP 113343

To appear in: Decision Support Systems

Received date: 17 January 2020

Revised date: 3 June 2020

Accepted date: 10 June 2020

Please cite this article as: F. Dunke and S. Nickel, A data-driven methodology for the automated configuration of online algorithms, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113343

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

A data-driven methodology for the automated configuration of online algorithms Fabian Dunke , Stefan Nickel

## Abstract

With the goal of devising algorithms for decision support in operational tasks, we introduce a new methodology for the automated configuration of algorithms for combinatorial online optimization problems. The procedure draws upon available instance data and is capable of recognizing data patterns which prove beneficial to the overall outcome. Since online optimization requires repetitive decision making without complete future information, no online algorithm can be optimal for every instance and it is reasonable to restrict attention to rule-based algorithms. We consider such algorithms in the form of procedures which derive their decisions using a threshold value. Threshold values are computed by evaluating a mathematical term (threshold value expression) composed of the available instance data elements. The goal then consists of determining the structure of the threshold value expres ion leading to the best algorithm performance. To this end, we employ a simulated annealing scheme returning the most favorable term composition given the available instance data. The resulting methodology can be implemented as part of data-driven support systems in order to facilitate knowledge-based decision making. Decisio les are generated in an automated fashion once historical input data is provided. The methodology is successfully instantiated in a series of classes of combinatorial online optimization problems (scheduling, packing, lot sizing). Results show that automatically configured online algorithms are even capable of substantially outperforming well-known online algorithms in respective problem settings. We attribute this effect to the methodology’s capability of integrating instance data into the process of algorithm configuration.

Keywords: automated decision making; data-driven optimization; automated algorithm configuration; online optimization; simulated annealing; lean decision making.

## 1 Introduction

Decision makers facing the same type of problem on a recurring basis can be supported in their decision making process through decision support systems ([1]). At the same time, companies have recognized the importance of data in order to translate information contents into improved analytical decision making in their business intelligence systems ([2]). In this paper, we enhance decision support systems by providing them with decision making routines which are configured automatically using available data and knowledge that can be deduced from the data. made without complete information about the future are addressed in the discipline $\stackrel { \frown } { \mathopen { \sim } } \mathbf { c } _ { \mathrm { \tiny { \tt { c a a m e } } } }$ optimization. Due to the impossibility to foresee the future, there is no hope for algorithms yielding decisions that are optimal in retrospective. Hence, every algorithm for an online optimization problem (online algorithm) is heuristic by definition. Regarding a heuristic as a well-defined sequence of decision making rules, online algorithms can be viewed as rule-based procedures. Research in online optimization has focused on worst case $\mathrm { p } ^ { \prime } \mathrm { f f } 0$ rmance guarantees leading to overly conservative algorithms with inferior average performance. For a practitioner, however, overall algorithm behavior may be crucial. Motivated by this shortcoming and today’s availability of large data volumes, we introduce a new approach for devising rule-based online algorithms and configuring their decision making rules using available data. We search for the configuration of a rule-based online algorithm delivering the best average objective value over a given data set. Hence, our approach represents a meta-concept asking for an optimization of online optimization algorithms.

Since it is not possible to consider all rule-based online algorithms, we restrict attention to rules that can be derived by so-called threshold value expressions. Threshold value expressions are mathematical terms composed of the available instance data and additional coefficients. When evaluated with actual values for the data elements, a threshold value is returned as the basis for the decision to be made by the online algorithm. Such expressions are prevalent in many rule-based decision making procedures, even though users are often unaware of their explicit functioning.

Example 1 (Threshold value expression for lot sizing).

Customer demands $D _ { \scriptscriptstyle 1 } , D _ { \scriptscriptstyle 2 } , \cdots$ have to be produced such that the overall costs depending on the setup costs A per production batch and the holding costs h per unit and period are minimized. The well-known Silver-Meal heuristic ([3]) uses the ratio

$$
C (s) := \frac {A + h \sum_ {i = t + 1} ^ {s} (i - t) D _ {i}}{s - t + 1}
$$

which gives the average costs per unit time. The decision to be made in period t amounts to integrating demand D for an upcoming period $s > t$ into the current production batch of period t if and only if the condition $C \left( s \right) > C \left( s - 1 \right)$ is fulfilled. Hence,

$$
C (s) - C (s - 1) = \frac {- A + h (s - t) ^ {2} D _ {s} - h \sum_ {i = t + 1} ^ {s - 1} (i - t) D _ {i}}{(s - t) (s - t + 1)}
$$

represents a threshold value expression and implies to include or not to include demand $D _ { \textit { s } }$ into the production quantity of period t based on whether the expression value is larger than 0 or not. Observe that for fixed s and t , $C \left( s \right) - C \left( s - 1 \right)$ elements A , h , and $D _ { { \scriptscriptstyle t + 1 } } , D _ { { \scriptscriptstyle t + 2 } } , \cdots , D _ { { \scriptscriptstyle s } }$

The overall goal then consists of determining an optimal composition (parametrization) of a threshold value expression and related coefficients. Due to the computational complexity of this problem, we employ a meta-heuristic search procedure in the form of a simulated annealing scheme to find a favorable set of threshold value expression parameters. Figure 1 summarizes the resulting methodological outline.

## Figure 1: Algorithmic outline for the automated algorithm configuration procedure.

The obtained threshold value expression can be implemented in a decision support system as a knowledge-based decision making scheme which is created in an automated fashion based on a model of the problem under consideration and related available historical data. Hence, properties of three types of decision support systems are addressed: Data-driven decision support systems ([4]), knowledge-driven decision support systems ([5]), and model-driven decision support systems ([1]). The combination of these three paradigms within a generic approach to rule-based decision making represents an enhancement to traditional, problem-specific decision making without specific consideration of data and knowledge.

The paper contributes a new meta-heuristic-based methodology for the automated configuration of rule-based online algorithms based on available instance data. These algorithms effectively make use of the configuration possibilities of threshold value expressions, and they are capable of outperforming well-known online algorithms without overfitting to data. Therefore, the proposed methodology allows to translate data into decisions, hereby eliciting value out of data as opposed to statically devised algorithms which do not incorporate any data. The resulting algorithms are computationally inexpensive making them attractive when lean decision making without computational overhead is required. Moreover, we establish a foundation for intertwining algorithmic decision making with available instance data in an automated meta-optimization procedure. This foundation can be further solidified in future research with respect to adaptively integrating changes in available data.

The remainder of the paper is organized as follows: Section 2 discusses related work both from a methodological perspective (online optimization, automated algorithm configuration, meta-heuristics) and an application-oriented persp scheduling, packing, lot sizing). The methodological topics are combined in Section 3 leading to a new framework for the automated configuration of rule-based online algorithms using available instance data. Computational experiments in three combinatorial online optimization problems in Section 4 show substantial improvements over classical online algorithms. Benefits of the method are summarized in Section 5. Section 6 yields an outlook on promising future research.

## 2 Related work

We review literature for the different topics involved in the automated configuration of rule-based online algorithms. Section 2.1 addresses online optimization and related multi-stage decision making methods. Section 2.2 then examines automated algorithm configuration and selection. In contrast to traditional algorithm configuration, our method is controlled by a meta-heuristic search procedure. Hence, the review also encloses generic methodologies amenable to a meta-optimization process. Finally, Section 2.3 discusses results on online algorithms for specific problems (packing, scheduling, lot sizing) considered in our numerical exp eriments. To the best of our knowledge, the paper at hand is the first one devoted to the automated configuration of algorithms in online optimization. Therefore, no existing literature can be referenced considering all of the topics combined in this work.

## 2.1 Online optimization and related sequential decision making methods

In contrast to offline optimization where all information is known in advance, online optimization ([6]) assumes that data arrives sequentially such that any related decision making method must be “on the line” to provide decisions for incoming data. There are several models ([7]) depending on whether real time plays a role (time-stamp model) or not (sequential model). Commonly, data is represented as a sequence $\sigma = ( \sigma _ { 1 } , \sigma _ { 2 } , ^ { \cdots } )$ of input elements $\sigma _ { i }$ with $i \in \mathbb { N }$ Due to the lack of future knowledge, no online algorithm can be optimal in the sense that it yields an optimal offline solution for every instance. Therefore, substitute concepts for measuring algorithm performance were devised. Widely accepted is $\mathrm { c c } _ { \mathrm { a } , \mathrm { \ v e } }$ titive analysis ([8]). In a $c \geq 1$ if on any problem instance the objective attained by the online algorithm is no more than c times the objective of an optimal offline algorithm which would have known in advance. Competitive analysis is a double worst case analysis: The guarantee has to hold for all instances and against the mos powerful adversary. There is agreement that competitive analysis is overly pessimistic and yields little practical insight ([9]). Additionally, it is oblivious to average algorithm behavior. Therefore, extensions and alternatives (e.g., fair adversaries ([10]), resource augmentation ([11]), comparative ratio ([12]), stochastic dominance ([13]), counting distribution functions ([14, 15])) have been devised to look-ahead ([16]) the offline case. Look-ahead – a limited number of future input elements which are made ilable earlier – allows to factor in the near future. Such information can technologically be made available by tracking and tracing or other sensor data ([17]). Typically, online optimization is concerned with basic settings – often coined from a theoretical perspective – due to its origin in computer science. As an extension to more complex real world settings, typically encountered in production, logistics, and supply chain management, we point out rolling horizon decision making ([18]). Originating from production planning ([19]), it adopts the same outline as online optimization with look-ahead, but with the difference that information about the future is only given through forecasts. Hence, rolling horizon decision making also requires sequential decision making, but takes into account uncertain predictions about future developments. Frequent realms of applications nowadays also comprise routing and scheduling ([20]). Further information about the integration of rolling horizon schemes into enterprise software systems such as advanced planning systems are found in [21] emphasizing tha computerized planning and execution of dynamic operations are indispensable in today’s supply chain processes.

## 2.2 Automated algorithm configuration and related meta-optimization concepts

Automated algorithm configuration and selection has been introduced in the mid 1970s by [22]. It tunes parameters of optimization algorithms to achieve favorable algorithm behavior. When the algorithm itself is the parameter, the task is to choose the best candidate from a set of viable algorithms. In contrast to our setting where the average objective is used to assess algorithm performance, automated algorithm configuration allows for arbitrary cost functions, but often focuses on achieving optimal solutions with least computational effort. For instance, parameters of a mathematical programming solver may be adjusted so as to receive short run times for a sample set of instances in a specific application (e.g., [23] considers decentralized energy systems where capacities and operations of energy resources $\mathbf { n } \mathbf { \hat { \Pi } } ^ { \mathbf { n } \mathbf { d } }$ to be optimized). Surveys on algorithm configuration and selection are given by [24] and [25], respectively, providing definitions of automated algorithm selection (a selector which gives for each instance the most suitable parameter configuration) and automated algorithm configuration (a selector which gives for a set of instances the most suitable parameter configuration). Specialized topics such as parallelization, multi-objective settings, or online rithm selection are addressed to extend algorithm configuration methodologies. Recent research discusses improvements of algorithm configuration procedures, e.g., concerning the sensitivity of algorithm responses upon changes in parameters ([26]) or the development and utilization of algorithm configurators for multi-objective optimization ([27]).

Another general method to algorithmically create algorithms are hyper-heuristics. In the survey [28], these are described as heuristics to choose heuristics, i.e., they generate algorithms by combining heuristic components (such as construction heuristics, perturbation heuristics, genetic algorithms, greedy rules). Hyper-heuristics intend to make algorithms for new applications easily available in a meta-procedure which is as independent from an application as possible, but rather seeks within the available search space of heuristics to assemble an algorithm. Hyper-heuristics can be categorized into selection and generation methods. In the former approach, an algorithm is created on the basis of already available entire heuristics, while in the latter approach the algorithm is created through composing different heuristic elements. Follow-up surveys on these two classes are found in [29] and [30], respectively. The mentioned surve ys [28, 29] provide references to papers addressing hyper-heuristics for bin packing (where rules for item to bin assignments are learned) and production scheduling (where different dispatching rules are combined). We explicitly mention [31] and [32] as examples for hyper- heuristics which use meta-heuristics (in the form of genetic algorithms) to construct online bin packing algorithms capable of emulating the decision making process of humans and that of well-known packing heuristics. We point out analogies between configuring a rule-based online algorithm and simulation optimization ([33]). Instead of configuring the parameters of a decision rule of an online algorithm, simulation optimization seeks to optimize parameters of a system or an algorithm to control the system. Hence, it distinguishes between parametric optimization and control optimization ([34]). Parametric optimization aims to determine system parameters so as to optimize the system output. In a search process, parameters are set repeatedly and the simulation is executed to return the (average) output as an evaluation of the current parameter setting. Control optimization dynamically asks during execution of a simulation model to determine the required decisions. As we seek to find an optimized version of an algorithm which is parametrized by the composition of a threshold value expression, we find ourselves in parametric optimization with the peculiarity that the parameter is the algorithm configuration. Depending on the structure of the parameter space (finite vs. infinite, discrete vs. continuous), different techniques have to be used for parametric simulation such as ranking $\mathrm { { a t . ^ { + } } }$ selection, derivative-free optimization, simulation meta-models ([35]). Implementations of simulation optimization methods mainly rely on meta-heuristics such as scatter search, tabu $\sin \angle 3 = 9 0 ^ { \circ }$ or genetic algorithms ([36, 37]).

The automated ${ \boldsymbol { \varsigma } } ^ { 1 } { \boldsymbol { \mathcal { o } } } ^ { \cdot }$ rithm configuration method presented in this paper is based on the simulated annealing meta-heuristic ([38]). For a comprehensive overview on meta-heuristics, including alternatives to simulated annealing, e.g., genetic algorithms ([39]) or threshold acceptance ([40]), we refer to [41]. The combination of meta-heuristics with data-driven learning represents a promising field of future research as it facilitates an integration of machine learning ([42, 43, 44]) into higher level procedures such as meta-heuristics.

## 2.3 Online algorithms in applications

We review literature on online algorithms for the applications examined in Section 4. We find that in all three online settings there are widely used and recognized online algorithms which operate on the basis of data-dependent threshold values.

## 2.3.1 Interval scheduling

In the interval scheduling problem (for a survey see [45]), jobs are to be processed on machines during their admissible processing interval in order to optimize some objective function related to the realized processing of jobs. Hence, each job comes with a prescribed processing interval and weight, and the overall goal is to maximize the sum of the weights of the jobs which have experienced completed processing. The offline variant can be reformulated as a coloring problem in an interval graph and solved in polynomial time ([46]). In the online version, it has to be decided at the moment of job arrival whether to start the job or not. In case of acceptance and all machines occupied, it additionally has to be decided which machine to free to make room for the new job. For a single machine, [47] considers an algorithm based on a threshold value and determines its performance in the competitive analysis framework. A similar analysis is carried out in [48] for the case of randomized onli ne algorithms. [49] derives performance guarantee bounds, often using a rule-based greedy algorithm, for several versions of the problem differing in specifications of interval lengths and job weights as well as in an extension of the problem to flow shops.

## 2.3.2 Bounded-space bin packing

In the bin packing $\because 0 . 1 = 1 1 ,$ items with a specified size need to be packed into unit-sized bins such that the total number of bins used is minimized. The offline variant is $\mathcal { N P }$ -hard ([50]). Research has focused $\mathrm { \ n } ^ { \cdot \cdot }$ only on tailored solution algorithms from mathematical programming ([51]), but also on approximation algorithms ([52]). The most frequently used algorithms for online bin packing are rule-based algorithms which decide upon the bin into which a new item has to be put on the basis of the current bin fill levels ([53]). A natural restriction in the online setting instills that at each time at most m bins are allowed to be opened. Hence, whenever a bin needs to be opened to accommodate an item, one of the m open bins needs to be closed first. This problem setting is called the bounded-space bin packing problem and it was introduced in [52]. Competitive analysis is provided in [54] for extensions of rule-based algorithms to the bounded-space case. Moreover, performance measures specifically tailored to the bounded-space case are introduced in

[55].

## 2.3.3 Lot sizing

The basic version of lot sizing consists of determining the production plan for a product demanded in time-varying quantities over a fixed time horizon. The goal is to find a balance between fixed ordering and inventory holding costs leading to minimal overall costs. The offline variant has been introduced in the 1950s by Wagner and Whitin ([56]) and exhibits pseudo-polynomial complexity. In the online version with look-ahead ([15]), the decision maker knows a limited number of upcoming demands, but not all demands until the end of the time horizon. In such a rolling horizon setting, the algorithm of Wagner and Whitin has limited use as repetitive utilization leads to plan nervousness which is unacceptable in practice ([57]). Therefore, algorithms were considered taking into account the impossibility of knowing the end of the time horizon ([3, 58, 59]). They operate on a rule-based strategy exploiting the trade-off between ordering and holding costs in a threshold value computed from the cost parameters and available demands. In numerical experiments, these algorithms yield stable results ([60]) making them candidates for use in real world applications. Moreover, competitive analysis results have been derived for rule-based online algorithms both in the pure online setting ([61]) and in the online setting with look-ahead ([62]).

## 3 Automated data-driven configuration of online algorithms

The research question to be answered subsequently is summarized as follows: Given a set of available instance data for a specific setting of an online optimization problem, how can a suitable online algorithm be devised by an automated data-driven outline? Once established, the obtained algorithm could be used as part of a decision support system in order to assist the decision maker whenever a decision is required. Recalling that due to incomplete information it is impossible to make retrospectively optimal decisions, we restrict ourselves to rule-based online algorithms. We search for a concrete specification of such an algorithm leading to favorable overall results. As we intend to generate the algorithm in an automated fashion, we speak of an (algorithmically) automated configuration of an online algorithm. The main task hence consists of constructively devising a methodology for the automated generation of online algorithms using

available data.

This section details the components and the resulting overall methodology for the automated data-driven configuration of rule-based online algorithms. In Section 3.1, we first specify the repetitive decision making task to be accomplished in an online optimization problem. The rule-based algorithms operate on threshold values which are calculated using the data available at each time a decision is required. Hence, decision making rules are based on threshold value expressions introduced in Section 3.2. Details on the resulting online algorithms and the required set of instance data are provided in Section 3.3; the overall data-driven meta-heuristic optimization procedure for finding a most suitable threshold value expression is then specified in Section 3.4.

## 3.1 Online snapshot problems

In online optimization, decisions have to be made repetitively without knowledge about future input data. An instance of an online optimization problem is represented by an input sequence $\sigma = ( \sigma _ { 1 } , \sigma _ { 2 } , \cdots )$ . The elements $\mathrm { { ~ \small ~ \mathscr ~ { ~ C ~ Z ~ } ~ } } \sigma$ have to be processed by an online algorithm one after another without knowledge of future elements, i.e., processing of input element $\sigma$ only relies upon knowledge of ${ \sigma _ { 1 } } , \cdots , \sigma$ $\sigma _ { { \scriptscriptstyle 1 } } , \cdots , \sigma _ { { \scriptscriptstyle i - 1 } }$ . Processing an input $\sigma _ { \mathrm { ~ i ~ } }$ transferring the system o a successor state. Hence, the notion of a system state becomes necessary $\mathbf { \Omega } _ { \alpha }$ an input for the decision making problem related to $\boldsymbol { \sigma } _ { \mathbf { \lambda } _ { i } }$ Previous decisions have brought the system into its current state and are manifested in the current state. As a consequence, an online algorithm can be viewed as a computational method to be invoked whenever a new input element $\sigma _ { i }$ is seen in the current system state. The task of an online algorithm then is to provide a decision upon notifying $\sigma _ { i }$ ; we capture this requirement in the notion of an online snapshot problem.

## Definition 2 (Online snapshot problem).

An online snapshot problem of an online optimization problem is the task of deciding about how to translate the occurrence of an input element $\sigma _ { \textit { i } }$ into the current system state such that a favorable

new system state is reached.

As can be seen from this definition, there is vagueness with respect to what a “favorable” new system state is. Due to the lack of a natural optima lity concept in online optimization, this vagueness can only be resolved artificially. For instance, it is possible to provide a restricted formulation of the overall problem when only input elements ${ \boldsymbol { \sigma } } _ { _ { 1 } } , \cdots , { \boldsymbol { \sigma } } _ { _ { i } }$ are considered (exact re-optimization). Although frequently used, this approach is questionable as it starts from false assumptions. Another established concept is concerned with rule-based decision making. Typically, rules for online decision making are dependent on the problem data, the current system state, and the new input element $\sigma _ { \textit { i } }$ . As a major advantage, any rule-based approach is entirely independent of a formulation of an auxiliary problem. In particular, no objective function needs to be formulated which is worthwhile considering the impossibility to know the “right” objective function of a snapshot problem. In this paper, the rules of a rule-based online algorithm are realized by so-called threshold value expressions.

## 3.2 Threshold value expressions for online snapshot problems

Decisions required by online snapshot problems are derived upon threshold value expressions. Informally, a threshold expression is a real-valued function returning a threshold value T V which is used for decision making as follows: If $T V \geq 0 \left( T V < 0 \right)$ , then a transfer the system from its current to the next state. As we seek to utilize threshold value expressions that take as input the data provided, the determination of the data to be used in each online decision making step is decisive to the overall outcome. Hence, the most crucial component of a threshold value expression comprises the set of (data) symbols $\boldsymbol { S } = \{ \boldsymbol { s } _ { 1 } , \boldsymbol { s } _ { 2 } , \cdots , \boldsymbol { s } _ { n } \}$ with $n \in ^ { \mathbb { N } }$ to be considered. Typically, S involves those data components of a problem setting which the decision maker believes to impact the quality of the decisions made. S may also involve data that is generated throughout the solution process, e.g., quantities describing the current state.

Let $S = \{ s _ { 1 } , s _ { 2 } , \cdots , s _ { n } \}$ be the set of symbols to be considered and ${ \mathcal { P } } _ { \left( S \right) }$ be the power set of S . Moreover, we introduce an ordering $P _ { o r d } = ( P _ { 1 } , P _ { 2 } , \cdots , P _ { { _ { 2 ^ { n } } } } )$ of the $2 ^ { n }$ subsets in ${ \mathcal { P } } _ { \left( S \right) }$ Technically, threshold value expressions have to be constructed according to a specific format involving sums, products, quotients, max-expressions, min-expressions, etc. which take as arguments the symbols from S . Subsequently, we restrict ourselves to sums and products and refer to future research for additional formats. In addition, we attribute a coefficient $c _ { \scriptscriptstyle i } \in \mathbb { R }$ to each subset $P _ { _ i }$ for $i = 1 , 2 , \cdots , 2 ^ { n }$ , i.e., we get an ordering of coefficients $\boldsymbol { c } _ { o r d } = ( c _ { _ 1 } , c _ { _ 2 } , \cdots , c _ { _ { _ { \ n } } } )$ as well. Finally, let $\nu = ( \nu _ { _ 1 } , \nu _ { _ 2 } , \cdots , \nu _ { _ n } )$ be a list of values $\nu _ { \mathrm { ~ } _ { i } } \in \mathbb { R }$ for $i = 1 , 2 , \cdots$ n  , where $\nu _ { \mathbf { \rho } _ { i } }$ gives the current value for symbol $s _ { i } \in S$ . We also write $\nu ( s )$ to indicate the value of $s \in S$

![](/api/attachments/CFNZZPHK/fulltext/images/c99155024fa290c33d07d69014b45438972d618a2b01826fb05f255ef0e663f3.jpg)

With symbol set $\boldsymbol { S } = \left\{ \boldsymbol { s } _ { 1 } , \boldsymbol { s } _ { 2 } , \cdots , \boldsymbol { s } _ { n } \right\}$ , the power set ${ \mathcal { P } } _ { \left( S \right) }$ holds $2 ^ { n }$ subsets; the number of elements in a subset varies between 0 and n . In practice, it may be reasonable to limit the number of elements in a subset as it is rather unlikely that a $\mathrm { r e } ^ { \gamma _ { - } } \hat { - } \mathrm { \hat { n _ { a } } } ^ { \dagger }$ le decision rule imitating trade-offs between different data components includes products wit (or a number close to n ) coefficients. Hence, it makes sense to restrict attention to $\mathrm { t h . . . }$ subsets in ${ \mathcal { P } } _ { \left( S \right) }$ with at most $n ^ { \prime } < n$ elements reducing the number of subsets to be considered from $2 ^ { n }$ to $\sum _ { i = 0 } ^ { n ^ { \prime } } { \binom { n } { i } }$ . More generally, this approach can be extended to considering a restricted ordering $P _ { o r d } = ( P _ { 1 } , P _ { 2 } , \cdots , P _ { _ k } )$ with any $k \in \{ 1 , 2 , ^ { \cdots } , 2 ^ { ^ n } \}$

## Definition 3 (Threshold value expression, value of a threshold value expression).

For a given symbol set S , let $P _ { o r d }$ be an ordering of k subsets of ${ \mathcal { P } } _ { \left( S \right) }$ with $k \in \{ 1 , 2 , ^ { \cdots } , 2 ^ { ^ { n } } \}$ and let $c _ { o r d }$ $P _ { o r d }$ . Moreover, let v be a list of values $P _ { o r d }$ and $c _ { _ { o r d } }$ is the algebraic expression $\sum _ { i = 1 } ^ { k } { c _ { i } \prod _ { s \in P _ { i } } s }$ . We synonymously identify the threshold value expression by a triple $T V E = ( S , P _ { o r d } , c _ { o r d } )$ . The value va l T V E v( , ) of threshold value expression T V E over symbol set S with respect to $P _ { o r d } , c _ { o r d } , \nu $ is the value of $\sum _ { i = 1 } ^ { k } c _ { i } \prod _ { s \in P _ { i } } \nu \left( s \right)$ . We synonymously identify the value of a threshold value expression by a quadruple $\nu a l ( T V E , \nu ) = ( S , P _ { o r d } , c _ { o r d } , \nu )$ . v a l T V E v ( , ) is also called threshold value. 

A threshold value expression can be understood as a function consisting of k terms of products composed of coefficients and concatenated symbols, whereas the value of a threshold value expression gives the return value of this function for a specific set of symbol values. Concerning the purpose of decision making, a threshold value suggests alternatives: If the threshold value is non-negative, then some action is carried out, otherwise some other action is carried out. In both cases, the system advances from its current state to a decision-dependent successor state. Hence, two alternative actions need to be defined in a threshold value expression setting of decision making as displayed in Algorithm 3.1.

```txt
Algorithm 3.1 evaluateThresholdValueExpression
Input: threshold value expression TVE, symbol values v, current system state z requiring decision, definitions of action alternatives 1 and 2
1: if val(TVE,v) ≥ 0 then
2: carry out action alternative 1 in system state z
3: else
4: carry out action alternative 2 in system state z
5: end if
Output: successor system state z' after action has been implemented
```

Threshold value expressions represent one possibility for realizing rule-based decision making. Extensions or generalizations allowing for a more differentiated algorithmic choice as opposed to two alternatives are to suggest that the presented structure of threshold value expressions already leads to surprisingly good results.

## 3.3 Online algorithms based on threshold value expressions

The overall methodology utilizes available data instances for the problem setting under consideration. Different algorithmic solutions in the form of different threshold value expressions are then evaluated over the set of available data instances using the average ob jective value achieved over the instances. Algorithm 3.2 first illustrates how a specific threshold value expression constituting a rule-based online algorithm is executed over a single data instance given by an input sequence $\sigma = ( \sigma _ { 1 } , \sigma _ { 2 } , ^ { \cdots } )$ . Since the overall outline (cf. Section 3.4) opts at finding a threshold value expression which is most favorable over the entire available data set, Algorithm 3.3 then represents the procedure of executing a threshold value expression over an entire data sample $\mathcal { D }$ . Observe that each solution (threshold value expression T V E ) can be associated to its performance which is measured as the average objective value $a \nu g ( T V E , ^ { \mathcal { D } } )$ attained over all available data instances, i.e., a solution can be represented by a pair $( T V E , a \nu g ( T V E , \mathcal { D } _ { ) ) }$ for a given data set .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3.2 executeOverInstance

Input: data instance represented by input sequence  $\sigma = (\sigma_{1}, \sigma_{2}, \cdots)$ , threshold value expression TVE, initial system state z, definitions of action alternatives  $a_{1}$  and  $a_{2}$ 

1: for i := 1 to n do

2: v := symbol values as contained in  $\sigma_{i}$  and z

3: z := evaluateThresholdValueExpression TVE,  $v, z, (a_{1}, a_{2})$ 

4: end for

Output: objective value (as contained in terminal system state z) of executing threshold value expression based algorithm over data instance  $\sigma_{i}$ 

Algorithm 3.3 executeOverSample

Input: data sample D consisting of N instances where each instance is represented by an input sequence  $\sigma^{i}$  and an initial system state  $z^{i}$  for  $i = 1, \cdots, n$ , threshold value expression TVE, definitions of action alternatives  $a_{1}$  and  $a_{2}$ 

1: sum := 0

2: for i := 1 to N

3: sum += executeOverInstance( $\sigma^{i}, TVE, z^{i}, (a_{1}, a_{2})$ )

4: end for

5: avg :=  $\frac{sum}{N}$ 

Output: average objective value avg(TVE, D) of executing threshold value expression based algorithm over data sample D
</div>

It is recommended to validate the obtained threshold value expression against further data sets to check robustness and sensitivity of the resulting online algorithm. To this end, a two-stage approach involving a training data set and a testing data set is typically used. The most favorable threshold value expression is found on the basis of the training data set; the testing data set is used afterward to validate the performance of the suggested threshold value expression. The mo tivation behind these two stages is to rule out the possibility of overfitting the threshold value expression to the training data set. As confirmed by the numerical experiments in Section 4, overfitting is unlikely as threshold value expressions do not exhibit an excessively large number of degrees of freedom compared to other machine learning techniques such as artificial neural networks or regression analysis.

Several options are possible for collecting data instances. In case of an available data history, instances are taken from past recordings and subdivided into training and testing data. In case that no historic data is available, a data generation method needs to be employed. Both training and testing data should be collected / generated $\therefore \therefore \cdot \vert { \boldsymbol { \mathbf { \mathit { h } } } } $ the same data collection / generation mechanism, i.e., corresponding data elements should be drawn from the same distribution. In this way, the question whether the selected threshold value expression is capable of providing beneficial decisions under the given data process can be answered on a profound basis. In case that one is not sure about the data process, robustness considerations play a role, and it would be advisable to check algorithm behavior against data sets sampled by different data generation schemes similar to a sensitivity analysis.

## 3.4 Simulated annealing-based overall methodology

The input to an online snapshot problem (current system state, general problem instance data, new input element) also serves as the input to a threshold value expression which provides the required answer to the online snapshot problem. Applying a specific threshold value expression to the sequence of online snapshot problems encountered upon processing an input sequence then amounts to the execution of a rule-based online algorithm which is based upon this threshold value expression (see also Algorithm 3.2). The main goal of the decision maker is to find a threshold value expression which proves to be best testing over the available data instances. Hence, the search space comprises the set of all possible threshold value expressions for the problem setting under consideration.

We adopt the simulated annealing meta-heuristic to search for a most favorable threshold value expression. Simulated annealing was introduced by [38] as a generic heuristic outline for solving combinatorial optimization problems. To find a global optimum, the main idea consists of working towards locally optimal solutions based on the neighborhood definition of a feasible solution, while in addition allowing randomly to escape local optima through temporarily accepting deterioration in the objective value. Over the years, evidence has accumulated that simulated annealing is a reliable meta-heuristic which outperforms other meta-heuristic procedures in many applications of combinatorial optimization ([63, 64, 65, 66]). As will be seen in the following discussion, the problem of determining a most favorable threshold value expression is a combinatorial optimization problem when the set of symbols $S \ = \ \{ s _ { { } _ { 1 } } , s _ { { } _ { 2 } } , \cdots { } _ { \ O } , s _ { { } _ { n } } \}$ and the set C of feasible coefficients are discrete sets.

A solution yielded by the simulated annealing scheme is represented by a threshold value expression $T V E = ( S , P _ { o r d } , c _ { o r d } )$ . Recall from Definition 3 t $\mathbf { l a } \mathbf { \Psi } \cdot \mathbf { \Psi } \in \mathbb { N }$ is the number of subsets of ${ \mathcal { P } } _ { \left( S \right) }$ to be considered in a threshold value expres io i.e., potentially there could be k non-zero coefficients in T V E . It is rather unlikely that an optimal threshold value expression exhibits a large number of non-zero coefficients. Contrarily, many problem settings admit trade-offs involving a limited number of data components. To obtain a reasonable and manageable selection of practically relevant threshold value expressions, we therefore restrict the number of non-zero coefficients in $c _ { o r d }$ to a $\nabla \mathcal { Z } \mathbf { \Delta } _ { \mathbf { i } } \mathbf { U } ^ { \epsilon } , \quad \mathcal { S } \in \left\{ \ 1 , 2 , \cdots , k \right\}$ . As a consequence, a threshold value expression can also be represented more efficiently by storing only those subsets from $P _ { o r d }$ associated to a non-zero coefficient $c _ { o r d }$ . In this case, T V E can also be represented by a triple $T V E = ( S , P _ { \ast 0 } , c _ { \ast 0 } )$ wher $\mathrm { ~  ~ \dot { ~ } { ~ \mu ~ } ~ } _ { 0 } = ( P _ { \dot { \imath } _ { 1 } } , P _ { \dot { \imath } _ { 2 } } , \cdots , P _ { \dot { \imath } _ { \delta } } )$ and $c _ { \scriptscriptstyle \neq 0 } = ( c _ { \scriptscriptstyle i _ { 1 } } , c _ { \scriptscriptstyle i _ { 2 } } , \cdots , c _ { \scriptscriptstyle i _ { \delta } } )$ hold those subsets from $P _ { o r d }$ and coefficient $c _ { _ { o r d } }$ , respectively, where $i _ { 1 } , i _ { 2 } , \cdots , i _ { \delta }$ are the indices in $c _ { _ { o r d } }$ with a non-zero coefficient.

Let $T V E = ( S , P _ { \neq 0 } , c _ { \neq 0 } )$ be a threshold value expression representing the current solution during the search for finding a most favorable threshold value expression. The simulated annealing procedure requires to generate the neighborhood of the current solution in order to find a better solution. We define the neighborhood of a threshold value expression T V E by allowing a fixed number of subsets in $P _ { \neq 0 }$ to be changed while the remaining subsets are retained. Introducing a maximum number $\Delta \in \{ 1 , 2 , \cdots , \delta \}$ of allowed changes in the form of an index shift by +1 or -1, we define the neighborhood of T V E by referring to the indices of the subsets of $P _ { o r d }$ to be changed in a neighboring threshold value expression $T V E ^ { \prime }$

Definition 4 (Neighborhood of a threshold value expression).

For symbol set S , let $P _ { o r d }$ be an ordering of subsets of ${ \mathcal { P } } _ { \left( S \right) }$ , and let $T V E = ( S , P _ { \neq 0 } , c _ { \neq 0 } )$ be a threshold value expression over S with $P _ { \mathbf { \varphi } _ { \neq } 0 } = ( P _ { \mathbf { \varphi } _ { i _ { 1 } } } , P _ { i _ { 2 } } , \cdots , P _ { \mathbf { \varphi } _ { i _ { \delta } } } )$ and $c _ { \scriptscriptstyle \neq 0 } = ( c _ { \scriptscriptstyle i _ { 1 } } , c _ { \scriptscriptstyle i _ { 2 } } , \cdots , c _ { \scriptscriptstyle i _ { \delta } } )$ such that $I = \{ i _ { { \scriptscriptstyle 1 } } , i _ { { \scriptscriptstyle 2 } } , \cdots , i _ { { \scriptscriptstyle \delta } } \}$ are the increasingly sorted indices of the non-zero coefficients in $c _ { _ { o r d } }$ Moreover, let C be the set of feasible coefficients, and let  be the number of allowed index changes. The index set I  of non-zero coefficients of a neighbor of T V E is obtained by changing  elements from I as follows:

• If $i _ { \mathrm { 1 } } \neq 1$ and $i _ { \delta } \neq k$ , then I  is obtained from I through changing exactly  elements $i \in I$ to i − 1 or to i + 1 .

• If $i _ { \mathrm { 1 } } = 1$ and $i _ { \delta } ~ = ~ k$ , then I  is obtained from I through changing exactly $\Delta - 2$ elements $i \in I \ \backslash \ \{ i _ { \scriptscriptstyle 1 } , i _ { \scriptscriptstyle \delta } \ \}$ to i−1 or to i + 1 ad seing $i _ { { \scriptscriptstyle 1 } ^ { \prime } } = 2$ , and $i _ { \delta } ^ { \prime } \ = \ k - 1$

• If $i _ { 1 } = 1$ and $i _ { \delta } \neq k$ , then I' is obt in from 1 through changing exactly ∆−1 elements $i \in I \ \backslash \ \{ i , \}$ to i  1 or $\llcorner $ , and setting $i _ { \mathrm { 1 ^ { \prime } } } = 2$

• If $i _ { \mathrm { 1 } } \neq 1$ and $i _ { \delta } ~ = ~ k$ elements $i \in \textit { I } \backslash \{ i _ { \delta } \}$ to i − 1 or to i + 1 , and setting $i _ { \delta } ^ { \prime } \ = \ k - 1$

The neighborhood $\mathcal { N } _ { \mathrm { ~ ( } T V E ) } \mathcal { ( } \dot { \textbf { o } _ { \perp } }$ T V E consists of all threshold value expressions $T V E ^ { \prime } = ( S , P _ { \neq 0 } ^ { \prime } , c _ { \neq 0 } ^ { \prime } )$ with <sub>0</sub>P<sub></sub>  $\mathbf { \Sigma } _ { \neq 0 } ^ { \prime } = ( P _ { i _ { 1 } ^ { \prime } } ^ { \prime } , P _ { i _ { 2 } ^ { \prime } } ^ { \prime } , \cdots , P _ { i _ { \delta } ^ { \prime } } ^ { \prime } )$ and $\boldsymbol { c } _ { \neq 0 } ^ { \prime } = ( c _ { i _ { 1 } ^ { \prime } } ^ { \prime } , c _ { i _ { 2 } ^ { \prime } } ^ { \prime } , \cdots , c _ { i _ { \delta } ^ { \prime } } ^ { \prime } )$ where $I ^ { \prime } = \{ i _ { 1 } ^ { \prime } , i _ { 2 } ^ { \prime } , \cdots , i _ { \delta } ^ { \prime } \}$ is constructed by the above procedure and $\boldsymbol { c } _ { \neq 0 } ^ { \prime } \in \boldsymbol { C } ^ { \delta }$ 

![](/api/attachments/CFNZZPHK/fulltext/images/030e497890956747888fb5bf5e49084e0a40eceb72857bf843c91317619b1deb.jpg)

Observe that for a neighbor of T V E no restrictions except for feasibility are imposed on coefficients $\boldsymbol { c } _ { \neq 0 } ^ { \prime } = ( c _ { i _ { 1 } ^ { \prime } } ^ { \prime } , c _ { i _ { 2 } ^ { \prime } } ^ { \prime } , \cdots , c _ { i _ { \delta } ^ { \prime } } ^ { \prime } )$ . In particular, when the set of feasible coefficients C is continuous, then $\mathcal { N } _ { ( T V E ) }$ contains an infinite number of elements. To admit a neighborhood amenable to practical purposes, we typically restrict C to be a discrete set, e.g., all integers in a specific interval.

Algorithm 3.4 summarizes the resulting simulated annealing scheme for the optimization of threshold value expressions. The algorithm makes use of Algorithm 3.1 to Algorithm 3.3 in a nested fashion.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3.4 simulatedAnnealingForThresholdValueExpressions
Input: data sample D, initial temperature T, minimum temperature  $T_{0}$ , cooling rate  $r \in (0,1)$ , number L of iterations with unchanged temperature, number M of inspected neighbors per iteration, initial threshold value expression TVE, definitions of action alternatives  $a_{1}$  and  $a_{2}$ 
1: while  $T \geq T_{0}$  do
2: for i := 1 to L do
3: for j := 1 to M do
4: determine  $TVE' \in N(TVE)$  randomly
5: avg( $TVE',D$ ) := executeOverSample( $T',TVE',(a_{1},a_{2})$ )
6:  $\Omega := avg(TVE,D) - avg(TVE',D)$ 
7: if  $\Omega \geq 0$  and overall problem asks for maximization or  $\Omega \leq 0$  and overall problem asks for minimization then
8:  $TVE := TVE'$ 
9: else
10: with probability  $p := \exp\left(-\frac{\Omega}{T}\right)$ ,  $TVE := TVE'$ 
11: end if
12: endfor
13: end for
14: T := rT
15: end while
Output: optimized threshold value expression TVE
</div>

On a related note, we mention the opportunity to employ the procedure on a rolling horizon basis with updated data sets integrating the most recent data into the methodology. Data updates could result from extending the available data set to currently observed realizations or from coupling the method with adaptive forecasting methods.

We next perform computational experiments for three practical settings in Section 4 in order to demonstrate the applicability and usefulness of the presented methodology for establishing decision making procedures in an automated fashion. On a general basis, advantages and benefits of the data-driven automated configuration of online algorithms are then discussed in Section 5.

## 4 Computational experiments

We evaluate the automated algorithm configuration scheme in numerical experiments for three combinatorial online optimization problems: Online interval scheduling (Section 4.2), online bounded-space bin packing (Section 4.3), and online lot sizing with look-ahead (Section 4.4). For every application, we follow the same methodological outline which puts the performanc e of the automatically configured online algorithm in relation to an optimal offline algorithm and an established heuristic. The obtained results allow for an assessment of the methodology’s applicability in practical settings and illustrate for which application type there is a good chance of transforming available instance data into prom $\mathrm { i s u } _ { \mathrm { i s } }$ rule-based online algorithms. Hence, the numerical experiments also contribute to the formation of an application-related knowledge base on rule-based decision making in online optimization.

## 4.1 Experimental setup

In every experiment, the simulated annealing scheme from Algorithm 3.4 is carried out with an initial temperature $\smash { 0 , \sum [ 6 ] }$ , a minimum temperature of 1, a cooling rate of 90%, 10 iterations with unchanged te perature, and 10 neighbors being considered in each iteration. For the threshold value expressions, we consider a maximum of $\delta = 4$ non-zero coefficients and also allow for $\Delta = 4$ changes in the subset indices. The maximum number of symbols from S multiplied in a single term of the threshold value expression is limited to 2 resulting in an ordering of $k = \left( \begin{array} { l } { | \boldsymbol { S } \mid } \\ { 0 } \end{array} \right) + \left( \begin{array} { l } { | \boldsymbol { S } \mid } \\ { 1 } \end{array} \right) + \left( \begin{array} { l } { | \boldsymbol { S } \mid } \\ { 2 } \end{array} \right)$ subsets of ${ \mathcal { P } } _ { \left( S \right) }$ . Each coefficient is allowed to take on the values from the set of feasible coefficients $C = \{ - 2 , - 1 , 0 , 1 , 2 \}$ . Hence, for each index combination of a threshold value expression, there are $5 ^ { 4 } = 6 2 5$ feasible coefficient configurations. The threshold value expression is determined from a training data set of 100 instances; the same instances are also applied to the other algorithms of a problem setting. To validate the quality of the resulting online algorithm, a testing data set consisting of 100 instances is generated and subjected to all algorithms of a problem setting.

We carried out further experiments to check the sensitivity of objective values upon changes in parameters of the simulated annealing algorithm and related quantities such as the number of non-zero coefficients. Overall, stable and reliable performance is found as reported also for several other combinatorial optimization problems ([63, 66]). Since the goal of this paper is to establish the validity of the methodology, an additional presentation of sensitivity analysis results would by far exceed the scope of the paper. Hence, the following discussion focuses on the experimental setup introduced above.

Due to the heuristic approach and the negligible computational costs related to evaluating threshold value expressions, results are obtained in a few seconds on a desktop computer with 3.5 GHz dual core processor, 4 GB random-access Algorithms were implemented in Java; mathematical programming formulations of the offline instances were solved using the IBM ILOG CPLEX 12.6 solver.

The results analysis focuses on the relative error (in terms of degradation from the optimal offline objective value) that is incurred $\mathbf { b } _ { \mathcal { I } } ^ { \phantom { \dagger } }$ the online heuristic and the automated algorithm configuration scheme, respectively. Observe that this quantity can be interpreted as an experimental competitive ratio (see also Section 2.1). In detail, the following quantities are determined for both algorithm $\mathrm { { ^ t y } _ { r } { ^ \circ s } }$ in relation to the optimal offline algorithm OPT over 100 instances: mean relative (mean rel err), maximum relative error in % (max rel err), standard deviation of relative err in % (std dev rel err), share of instances that reaching the optimal offline objective value (instances opt). Additionally, we provide information concerning a direct comparison between the automated algorithm configuration and the established online heuristic: share of instances where the automated algorithm configuration beats the online heuristic (AUTO heuristic), the online heuristic beats the automated algorithm configuration (AUTO heuristic), the automated algorithm configuration exhibits the same objective as the online heuristic (AUTO heuristic) in % .

## 4.2 Online interval scheduling

The input sequence $\sigma = ( \sigma _ { _ 1 } , \sigma _ { _ 2 } , \cdots )$ represents the sequence of jobs that can be processed on the $m$ machines. Each job $\sigma _ { \textit { i } }$ is a triple $\boldsymbol { \sigma } _ { i } = ( s _ { i } , t _ { i } , w _ { i } )$ with $( s _ { i } , t _ { i } )$ representing the processing interval start / end and $w _ { \textit { i } }$ representing the reward (in case of completed processing) of the i th job. When a new job arrives, the current system state is described by the machine states (remaining processing time $r _ { j }$ and potential reward $w _ { \mathbf { \lambda } _ { j } }$ in case of a job being currently processed on machine j ), the new job $\boldsymbol { \sigma } _ { i } = ( s _ { i } , t _ { i } , w _ { i } )$ , and the number $m$ of parallel machines. In addition, we order machines by their potential reward such that any decision rule does not depend on the machine indexing. The symbol set S is $S = ( ( r _ { _ { ( 1 ) } } , w _ { _ { ( 1 ) } } ) , \cdots , ( r _ { _ { ( m ) } } , w _ { _ { ( m ) } } ) , ( s _ { _ { i } } , t _ { _ i } , w _ { _ { i } } ) , m )$ . Whenever a machine is free and a new job arrives, the job is started. When all machines are busy, a running job may be interrupted and replaced by a supposedly more lucrative new job as it arrives. This decision is made depending on the sign of the threshold value expression. We impose that in case of a job abortion, the job with the lowest potential reward is canceled (greedy strategy).

Symbols Current machine statuses (remaining processing times, potential rewards), data of new

job (processing interval, potential reward), number of machines.

Action alternative 1 Interrupt the processing of the job with the lowest potential reward and start processing the job which has currently arrived.

Action alternative 2 Reject the job which has currently arrived.

The test environment comprises three classes of algorithms: The online algorithm obtained from the automated algorithm configuration methodology (AUTO), the online interval scheduling formulation of the offline $\therefore \min$ scheduling problem (OPT; see [46]).

Results for six problem settings differing in the overall processing time interval and the number of machines are summarized in Table 1. Both in the case of a single machine and two parallel machines, AUTO substantially outperforms WOE in terms of solution quality and variability. This is seen both in the relative error analysis with respect to the optimal offline algorithm OPT and in the direct comparison between AUTO and WOE. In particular, the order of magnitude of AUTO’S edge over WOE shows the enormous potential of an automated algorithm configuration scheme to exploit instance data and turn them into favorable decisions. The flexibility of an automated algorithm configuration method to tune algorithm instructions according to available instance data hence becomes a major advantage over statically formulated algorithms without any options for further adaptation.

<table><tr><td></td><td colspan="2">1 machine</td><td colspan="2">1 machine</td><td colspan="2">1 machine</td></tr><tr><td></td><td colspan="2">50 time units</td><td colspan="2">75 time units</td><td colspan="2">100 time units</td></tr><tr><td></td><td>WOE/OPT</td><td>AUTO/OPT</td><td>WOE/OPT</td><td>AUTO/OPT</td><td>WOE/OPT</td><td>AUTO/OPT</td></tr><tr><td>mean rel err(training)</td><td>16.3</td><td>4.5</td><td>11.5</td><td>4.2</td><td>10.1</td><td>3.4</td></tr><tr><td>mean rel err(testing)</td><td>17.6</td><td>4.3</td><td>12.0</td><td>3.3</td><td>9.4</td><td>3.0</td></tr><tr><td>max rel err(training)</td><td>35.6</td><td>20.9</td><td>26.4</td><td>13.8</td><td>27.1</td><td>14.8</td></tr><tr><td>max rel err(testing)</td><td>35.6</td><td>15.0</td><td>24.8</td><td>12.7</td><td>24.2</td><td>8.8</td></tr><tr><td>std dev rel err(training)</td><td>7.2</td><td>3.5</td><td>5.8</td><td>3.4</td><td>5.0</td><td>2.8</td></tr><tr><td>std dev rel err(testing)</td><td>8.2</td><td>3.2</td><td>6.1</td><td>2.7</td><td>5.3</td><td>2.5</td></tr><tr><td>instances opt(training)</td><td>0</td><td>6</td><td>1</td><td>12</td><td>0</td><td>12</td></tr><tr><td>instances opt(testing)</td><td>0</td><td>10</td><td>0</td><td>14</td><td>0</td><td>15</td></tr><tr><td>AUTO ↗ / ~ ↕WOE (training)</td><td colspan="2">94/2/4</td><td colspan="2">87/5/8</td><td colspan="2">92/4/4</td></tr><tr><td>AUTO ↗ / ~ ↕WOE (testing)</td><td colspan="2">93/3/4</td><td colspan="2">93/4/3</td><td colspan="2">87/5/8</td></tr><tr><td colspan="7"></td></tr><tr><td></td><td colspan="2">2 machines</td><td colspan="2">2 machines</td><td colspan="2">2 machines</td></tr><tr><td></td><td colspan="2">50 time units</td><td colspan="2">75 time units</td><td colspan="2">100 time units</td></tr><tr><td></td><td>WOE/OPT</td><td>AUTO/OPT</td><td>WOE/OPT</td><td>AUTO/OPT</td><td>WOE/OPT</td><td>AUTO/OPT</td></tr><tr><td>mean rel err(training)</td><td>8.6</td><td>3.5</td><td>5.5</td><td>1.9</td><td>3.5</td><td>1.3</td></tr><tr><td>mean rel err (testing)</td><td>7.7</td><td>3.3</td><td>4.8</td><td>1.8</td><td>3.3</td><td>1.3</td></tr><tr><td>max rel err (training)</td><td>20.8</td><td>12.6</td><td>13.3</td><td>6.7</td><td>12.0</td><td>5.9</td></tr><tr><td>max rel err (testing)</td><td>17.0</td><td>12.8</td><td>14.0</td><td>6.7</td><td>13.1</td><td>5.7</td></tr><tr><td>std dev rel err (training)</td><td>4.7</td><td>2.4</td><td>3.2</td><td>1.5</td><td>2.4</td><td>1.5</td></tr><tr><td>std dev rel err (testing)</td><td>3.8</td><td>2.8</td><td>3.1</td><td>16</td><td>2.5</td><td>1.5</td></tr><tr><td>instances opt (training)</td><td>2</td><td>6</td><td>0</td><td>14</td><td>3</td><td>33</td></tr><tr><td>instances opt (testing)</td><td>2</td><td>8</td><td>2</td><td>20</td><td>6</td><td>36</td></tr><tr><td>AUTO ↗ / ~ ↖ WOE (training)</td><td colspan="2">87/7/6</td><td colspan="2">87/7/6</td><td colspan="2">81/6/13</td></tr><tr><td>AUTO ↗ / ~ ↖ WOE (testing)</td><td colspan="2">82/3/15</td><td colspan="2">81/9/10</td><td colspan="2">76/11/13</td></tr></table>

Table 1: Computational results in the interval scheduling problem for 100 instances with 50 jobs.

As an example, Figure 2 illustrates the objectives attained by the three algorithms WOE, AUTO, and OPT over all training and testing instances in the case of two machines and an overall processing time interval of 100. Recall that the overall goal in interval scheduling consists of maximizing the total reward of completed jobs. The objectives of WOE and AUTO are below the objective of the optimal offline algorithm OPT, but only by a slight margin. Hence, both online algorithms exhibit a rather competitive performance. In the majority of the instances, the blue dot of AUTO lies between the red dot of WOE and the green dot of OPT, thereby establishing the automatically generated online algorithm AUTO as the superior method for online decision making.

Figure 2: Objective values in the interval scheduling problem for 100 instances with 2 machines, 50 jobs, and overall processing time interval of length 100.

## 4.3 Online bounded-space bin packing

The input sequence $\sigma = ( \sigma _ { 1 } , \sigma _ { 2 } , ^ { \cdots } )$ represents the sequence of item sizes that need to be packed into the bins. At each time, at most m bins are allowed to be opened. Without loss of generality, bins are unit-capacitated and item sizes are from (0 ,1 ] . When a new item arrives, the current system state is described by the bin fill levels $f _ { j }$ of the m open bins, the new item size $\boldsymbol { \sigma } _ { \mathbf { \lambda } _ { i } }$ , and the number $m$ of allowed open bins. In addition, we order bins by their fill levels such that any decision rule does not depend on the bin indexing. The symbol set S is $S = ( f _ { _ { ( 1 ) } } , \cdots , f _ { _ { ( m ) } } , \sigma _ { _ { i } } , m )$ . Whenever an arriving item needs to be packed, it has to be checked first if any of the m bins allows for packing this item. If not, a new bin must be opened (and an already open bin closed) where the new item is accommodated. If only one bin is capable of accommodating the new item, the decision is trivial. If there is more than one already opened bin available that could accommodate the new item, a bin to be closed must be selected. This decision is made depending on the sign of the threshold value expression. We impose that the item is put either into the fullest or into the emptiest available bin capable of accommodating the item. An extension to cases where more than two action alternatives are possible is a field for future research (cf. Section 6).

Symbols Current bin fill levels, size of new item, number of allowed opened bins.

Action alternative 1 Put the item into the fullest bin capable of accommodating it.

Action alternative 2 Put the item into the emptiest bin capable of accommodating it.

The test environment comprises three classes of algorithms: The online algorithm obtained from the automated algorithm configuration methodology (AUTO), the Best Fit algorithm in its version for online bounded-space bin packing (BFB; for details see [54]), and solving a mathematical programming formulation of the offline bounded-space bin packing problem (OPT; for details see [67]).

Results for three problem settings differing in the number of allowed open bins are summarized in Table 2. AUTO produces results which are nearly indistinguishable from those produced by BFB – in some quantities with a slight margin for AUTO, in others for BFB. The variability of AUTO is no different than that of BFB both in the training and testing data set pointing to a stable behavior of the method. We conclude that in online bin packing, competitive rule-based online algorithms can be obtained with the automated algorithm configuration scheme.

<table><tr><td></td><td colspan="2">3 open bins</td><td colspan="2">5 open bins</td><td colspan="2">7 open bins</td></tr><tr><td></td><td>BFB/OPT</td><td>AUTO/OPT</td><td>BFB/OPT</td><td>AUTO/OPT</td><td>BFB/OPT</td><td>AUTO/OPT</td></tr><tr><td>mean rel err(training)</td><td>5.7</td><td>5.7</td><td>3.9</td><td>3.8</td><td>3.5</td><td>3.3</td></tr><tr><td>mean rel err(testing)</td><td>6.8</td><td>6.8</td><td>4.6</td><td>16</td><td>3.9</td><td>4.0</td></tr><tr><td>max rel err(training)</td><td>16.0</td><td>16.0</td><td>12.5</td><td>12.5</td><td>12.5</td><td>12.5</td></tr><tr><td>max rel err (testing)</td><td>19.0</td><td>19.0</td><td>14.3</td><td>14.3</td><td>14.3</td><td>14.3</td></tr><tr><td>std dev rel err(training)</td><td>3.2</td><td>3.2</td><td>2.7</td><td>2.7</td><td>2.7</td><td>2.6</td></tr><tr><td>std dev rel err(testing)</td><td>3.2</td><td>3.2</td><td>3.0</td><td>3.0</td><td>3.0</td><td>3.0</td></tr><tr><td>instances opt(training)</td><td>10</td><td>10</td><td>21</td><td>22</td><td>26</td><td>28</td></tr><tr><td>instances opt(testing)</td><td>4</td><td>4</td><td>19</td><td>19</td><td>27</td><td>25</td></tr><tr><td>AUTO  $\succ / \sim \prec$  BFB(training)</td><td colspan="2">0/100/0</td><td colspan="2">2/98/0</td><td colspan="2">5/95/0</td></tr><tr><td>AUTO  $\succ / \sim \prec$  BFB(testing)</td><td colspan="2">0/100/0</td><td colspan="2">2/97/1</td><td colspan="2">7/84/9</td></tr></table>

Table 2: Computational results in the bounded-space bin packing problem for 100 instances with 50 items.

In Figure 3, the exemplary illustration for the case of seven open bins shows that both online algorithms BFB and AUTO demonstrate similar performance. This can be implied from the fact that in the vast majority of instances, the objectives of BFB and AUTO coincide with each other.

Additionally, it can be recognized that the optimal offline algorithm OPT leads to an overall saving of at most two bins. Although this represents a non- negligible percentage of bins, both algorithms BFB and AUTO still exhibit a high quality of performance considering that they have to make decisions in an online fashion as opposed to the offline algorithm OPT.

Figure 3: Objective values in the bounded-space bin packing problem for 100 instances with 50 items for 7 open bins.

## 4.4 Online lot sizing with look-ahead

The input sequence $\boldsymbol { \sigma } = ( \sigma _ { _ 1 } , \sigma _ { _ 2 } , \cdots )$ represents the respective periods. Due to look-ahead of size $l \in ^ { \mathbb { N } }$ $\sigma _ { \textit { i } }$ is seen in period i , but also $\sigma _ { i + 1 } , \cdots , \sigma _ { { i + l - } }$ such that an overall of l demands is seen in period i . Apart from the demand data, the cost coefficients A for the fixed ordering cost and h for the inventory holding cost per product unit and period are relevant data. $\because e$ symbol set S is $S = ( \sigma _ { i } , \sigma _ { i + 1 } , \cdots , \sigma _ { i + l - 1 } , A , h , l )$ Observe that there is no need to specify the inventory level in period i because decisions are only made when previously ordered quantities are fully used up (zero inventory policy). Whenever demands of the last production batch have been consumed, the size of the next production batch needs to be determined. or an empty inventory at the beginning of period i , this amounts to successively checking for eac demands $\sigma _ { { i + 1 } } , \cdots , \sigma _ { { i + l - 1 } }$ whether to include it into the production batch. This decision is made depending on the sign of the threshold value expression. In more detail, when checking whether to include $\sigma _ { \textit { i - } }$ with $j \in \{ 1 , \cdots , l - 1 \}$ , we pretend to be in period j and – in accordance with the available information at period i – are able to foresee demands until period i l  1 . Hence, in period i for deciding upon including the demand of period $i + j$ , we use a restricted symbol set $\boldsymbol { S } ^ { \prime } = ( \sigma _ { { i + j } } , \cdots , \sigma _ { { i + l - 1 } } , A , h , l )$ . This outline shows that threshold value expressions can be used in a rather versatile way by adapting them to the information state of the decision maker. In this case, this amounts to introducing an additional loop into the loop of Algorithm 3.3 iterating over j l= 1 , , 1 .

Symbols Demand values known due to look-ahead, fixed ordering cost, inventory holding cost, look-ahead size.

Action alternative 1 Include demand of period i j in the production batch of period i . Action alternative 2 Start a new production batch in period i j  including demand of period

$$
i + j
$$

The test environment comprises three classes of algorithms: The online algorithm obtained from the automated algorithm configuration methodology (AUTO), the Silver-Meal heuristic (SM; for details see [60]), and solving the dynamic programming scheme for offline lot sizing (OPT; for details see [56]). Both heuristic algorithms are adapted to the look-ahead case by taking into account decisions which affect the periods contained in the look-ahead.

Results for three problem settings differing in the (ratio between fixed ordering and) inventory holding costs are summarized in Table 3. Observe that the setting with inventory holding costs $h = 0 . 0 5$ is the most difficult setting as seen from the row on the number of instances solved (coincidentally) to optimality by SM and AUTO, respectively. In this setting, AUTO outperforms the established heuristic SM, both in terms of the relative error with respect to OPT and in terms of the substantially beneficial when required from the difficulty of the problem setting. In contrast, the settings $h = 0 . 2 5$ and $h = 0 . 5$ are easier as seen from the number of instances which could be solved to optimality also by the heuristic approaches. These settings also show a significant decrease in the relative error with t to OPT. Therefore, despite the slight edge of SM over AUTO, the minor order of magnitude of the mean relative error (e.g., for $h = 0 . 5$ below 1.5% for both training and testing data) displays that AUTO represents a promising algorithm for the online lot sizing problem with look-ahead which even has the potential to excel SM in difficult problem settings.

<table><tr><td></td><td colspan="2">holding cost 0.05</td><td colspan="2">holding cost 0.25</td><td colspan="2">holding cost 0.5</td></tr><tr><td></td><td>SM/OPT</td><td>AUTO/OPT</td><td>SM/OPT</td><td>AUTO/OPT</td><td>SM/OPT</td><td>AUTO/OPT</td></tr><tr><td>mean rel err (training)</td><td>5.2</td><td>3.4</td><td>1.5</td><td>2.8</td><td>0.5</td><td>0.8</td></tr><tr><td>mean rel err (testing)</td><td>5.3</td><td>3.7</td><td>1.6</td><td>2.8</td><td>0.4</td><td>1.3</td></tr><tr><td>max rel err(training)</td><td>13.9</td><td>10.5</td><td>4.9</td><td>11.8</td><td>2.4</td><td>5.5</td></tr><tr><td>max rel err (testing)</td><td>13.5</td><td>10.1</td><td>6.8</td><td>8.8</td><td>2.2</td><td>7.0</td></tr><tr><td>std dev rel err (training)</td><td>2.8</td><td>2.1</td><td>1.1</td><td>1.9</td><td>0.6</td><td>0.9</td></tr><tr><td>std dev rel err (testing)</td><td>2.6</td><td>2.2</td><td>1.1</td><td>1.6</td><td>0.5</td><td>1.4</td></tr><tr><td>instances opt (training)</td><td>0</td><td>0</td><td>5</td><td>0</td><td>39</td><td>16</td></tr><tr><td>instances opt (testing)</td><td>0</td><td>0</td><td>6</td><td>1</td><td>38</td><td>7</td></tr><tr><td>AUTO  $\succ / \sim \prec$  SM (training)</td><td colspan="2">70/0/30</td><td colspan="2">18/1/81</td><td colspan="2">33/6/61</td></tr><tr><td>Auto  $\succ / \sim \prec$  SM (testing)</td><td colspan="2">58/0/42</td><td colspan="2">48/0/52</td><td colspan="2">48/1/51</td></tr></table>

Table 3: Computational results in the lot sizing problem with look-ahead of 5 demands for 100 instances with 50 demands and fixed ordering costs of 15.

Figure 4 conveys a comprehensive picture of algorithm quality for the exemplary setting with holding costs of 0.5. The performance of both online algorithms SM and AUTO is assessed to be of equal quality since substantial shares of instances are found where SM dominates AUTO and vice versa. Considering the order of magnitude of the overall costs, both online algorithms exhibit performance close to the performance of the optimal offline algorithm OPT. Hence, automated decision making by AUTO can be recommended not only in comparison to peer online algorithms such as SM, but also from an absolute point of view regarding the maximum potential for optimization.

Figure 4: Objective values in the lot sizing problem with look-ahead of 5 demands for 100 instances with 50 demands, fixed ordering costs of 15, and holding costs of 0.5.

## 4.5 Conclusions from computational experiments

The numerical experiments show that the automated algorithm configuration scheme introduced in Section 3 is a viable and competitive approach for the automated generation of online algorithms in different applications. The achieved performance in the interval scheduling application substantially beats that of an established online heuristic showing the method’s capability and flexibility of turning data into reasonable decisions. Together with the bin packing application where comparable performance with respect to a famous heuristic is achieved and the lot sizing application where improved performance is achieved in the most difficult setting, these findings provide evidence to the fact that the data-driven method is capable of delivering high quality solutions in applications of different nature.

Throughout all applications, an important result found from a comparison of the performance over training data and testing data is the performance insensitivity of the resulting method to the specific data set. This yields an indication that the method is not at risk for overfitting to data, but rather likely to adapt to trade-offs derivable from data in general. Considering the limited configuration possibiliti ${ \boldsymbol { \mathbf { \rho } } } _ { \mathbf { S } } \ { \mathrm { ~ c ~ f ~ } }$ threshold value expressions, this result makes the methodology even more fa $\mathbf { v o r a } ^ { \mathbf { k } ^ { 1 } \mathbf { \widetilde { \Gamma } } }$ compared to other machine learning techniques prone to overfitting such as artificial neural networks or regression analysis.

Likewise, the method does not exhibit increased variability in performance as shown by the acceptable values of maximum relative error and standard deviation of relative error. Hence, the algorithms generated by the automated algorithm configuration scheme lead to a rather robust performance over all instances without incurring additional volatility in attained objective values.

Finally, also the $d ^ { : } { \cdot } { \omega } _ { \cdot \mathrm {  ~ } \mathrm { \ p e r f o r m a n c e } }$ comparison between the automatically generated online algorithm and the established online heuristics shows that the automated algorithm configuration leads to promising algorithmic decision making on an instance-wise basis. In many settings, the share of instances where the automatically generated online algorithm is better than the online heuristic is larger than vice versa.

## 5 Advantages and benefits of the proposed methodology

The automated configuration of online algorithms with threshold value expressions provides the decision maker with a number of advantages and benefits from different perspectives. These can be realized by implementing the methodology as part of a decision support system.

Once implemented, it becomes possible to automate the generation of decision making procedures and to translate data into problem-specific knowledge on a repetitive basis.

In contrast to consciously devised problem-specific algorithms, the automated configuration of rule-based online algorithms promotes the detection of higher-order effects and data patterns. Trade-offs between data components and resulting effects on overall algorithm performance originate from the interplay between data and algorithmic decisions, and as such are unlikely to be recognized consciously. Hence, a potential value of data – which may have remained undetected without an automated algorithm configuration scheme – can be incorporated

As seen in the numerical experiments in Section 4, it becomes possible to outperform established online heuristics by integrating their rationale into the threshold value expressions. Hence, new online algorithms which prove superior to established online algorithms based on the given data obtain the opportunity to come into focus in the first place.

Due to the impossibility of knowing future input elements, there is no natural concept of optimality in online optimization. It is unclear how supposedly good partial solutions (e.g., derived by exact re-optimization) contribute to the overall solution. As a major advantage of the automated configuration of rule-based online algorithms, this issue is resolved by the non-necessity of formulating an optimization problem for the online snapshot problem. Instead, trade-offs between data elements are pursued to be uncovered using data-related threshold value expressions which do not rely on a substitute optimization problem.

The automated algorithm configuration methodology can be used in any situation making where no algorithms are yet available. Decisio n making routines are configured with rule-based online procedures in an automated fashion which is particularly important when no application-specific knowledge or insights on trade-offs exist. Due to the minor computational effort for evaluating threshold value expressions, the approach is well-suited for a fast and conceptually transparent development of online algorithms which could directly be implemented and deployed by practitioners.

## 6 Concluding remarks

The methodology devised in this paper serves as a starting point for future research on self-optimizing algorithmic procedures for decision making problems. The introduced framework shows that – despite the impossibility of designing online algorithms which yield an optimal solution to every problem instance – the availability of instance data and the restriction to rule-based decision rules can be exploited algorithmically as presented in Section 3 to automatically create online algorithms of high quality. We do so by requiring the online algorithm to adhere to a rule-based decision mechanism which is configured through available instance data. The resulting rule-based online algorithm can be understood as a lean decision making structure, suggesting a high degree of acceptance in practical contexts where transparency for the origin of decisions is sought besides performance quality. In particular, they can be used as part of decision support systems to assist decision makers with knowledge extracted from historical data. Even though admissible decision rules are restricted to threshold value expressions, computational results in Section 4 show that the automatically generated online algorithms are in a position to substantially outperform established online algorithms. The proposed methodology ultimately allows to transform data into new and better algorithms, yielding an immediate value of existing data.

Extensions of the methodology represent a broad field for future research: First, threshold value expressions (allowing for two alternatives to tackle an online snapshot problem) are more generally replaced by a vector of threshold values (allowing for more than two alternatives); likewise, nested decision rules (allowing for a hierarchy of conditions to be fulfilled by several threshold values) may formalize more complex decision making structures. Second, interlocking more closely the automated algorithm configuration scheme with data sampling and data analysis can be used to continuously adapt online algorithms throughout operations leading to a direct integration of recent data. In data-driven decision support systems, this capability is known as online analytical processing and it represents a challenging area of future research, especially when online variants of combinatorial optimization problems are considered. Finally, the general idea of a self-optimizing algorithm configuration method related to available instance data can be used as a blueprint for further artificial intelligence methodologies applicable to contexts different from online optimization, such as combinatorial (offline) optimization, data mining, or machine learning.

## References

[1] D. J. Power and R. Sharda, Model-driven decision support systems: Concepts and research directions, Decision Support Systems 43 (3) (2007) 1044 – 1061, https://doi.org/10.1016/j.dss.2005.05.030.

[2] A. Popovi c , R. Hackney, P. S. Coelho and J. Jakli c , Towards business intelligence systems success: Effects of maturity and culture on analytical decision making, Decision Support Systems 54 (1) (2012) 729 739, https://doi.org/10.1016/j.dss.2012.08.017.

[3] E. A. Silver and H. C. Meal, A heuristic for selecting lot size quantities for the case of a deterministic time-varying demand rate and discrete opportunities for replenishment,

[4] D. J. Power, Understanding data-driven decision support systems, Information Systems Management 25 (2) (2008) 149–154, https://doi.org/10.1080/10580530801941124.

[5] C. W. Holsapple, Decisions and knowledge, i n: Handbook on Decision Support Systems 1: Basic Themes, pages 21–53, Springer, 2008, https://doi.org/10.1007/978-3-540-48713-5\_2.

[6] A. Fiat and G. Woeginger (Eds.), Online Algorithms: The State of the Art, Springer, 1998.

[7] M. Grötschel, S. Krumke, J. Rambau, T. Winter and U. Zimmermann, Combinatorial online optimization in real time, in: M. Grötschel, S. Krumke and J. Rambau (Eds.), Online Optimization of Large Scale Systems, pages 679–704, Springer, 2001, https://doi.org/10.1007/978-3-662-04331-8\_33.

[8] A. Borodin and R. El-Yaniv, Online Computation and Competitive Analysis, Cambridge University Press, 2nd edition, 2005.

[9] J. Boyar, S. Irani and K. S. Larsen, A comparison of performance measures for online algorithms, Algorithmica 72 (4) (2015) 969–994, https://doi.org/10.1007/s00453-014-9884-6.

[10] M. Blom, S. Krumke, W. De Paepe and L. Stougie, The online tsp against fair adversaries, INFORMS Journal on Computing 13 (2) (2001) 138–148, note= https://doi.org/10.1287/ijoc.13.2.138.10517.

[11] L. Epstein and R. van Stee, Online bin packing with resource augmentation, Discrete Optimization 4 (3-4) (2007) 322–333, note=

https://doi.org/10.1016/j.disopt.2007.09.004.

[12] E. Koutsoupias and C. Papadimitriou, Beyond competitive analysis, SIAM Journal of Computing 30 (1) (2000) 300–317, https://doi.org/10.1137/S0097539796299540.

[13] B. Hiller and T. Vredeveld, Probabilistic alternatives for competitive analysis, Computer Science – Research and Development 27 (3) (2012) 189–196, https://doi.org/10.1007/s00450-011-0149-1.

[14] F. Dunke and S. Nickel, Evaluating the quality of online optimization algorithms by discrete event simulation, Central European Journal of Operations Research 25 (4) (2017) 831–858, https://doi.org/10.1007/s10100-016-0455-6.

[15] F. Dunke and S. Nickel, Online optimization with gradual look-ahead, Operational Research article in press, https://doi.org/10.1007/s12351-019-00506-z.

[16] F. Dunke and S. Nickel, A general modeling approach to online optimization with lookahead, Omega 63 (2016) 134–153,

Control, Wiley, 2004.

[18] S. Sethi and G. Sorger, A theory of rolling horizon decision making, Annals of Operations Research 29 (1) (1991) 387–415, https://doi.org/10.1007/BF02283607.

[19] C. Bes and S. P. Sethi, Concepts of forecast and decision horizons: Applications to optimization problems, Mathematics of Operations Research 13 (2) (1988) 295–310, https://doi.org/10.1287/moor.13.2.295.

[20] W. B. Powell, P. Jaillet and A. Odoni, Stochastic and dynamic networks and routing, in: Network Routing, volume 8 of Handbooks in Operations Research and Management Science, pages 141 295, Elsevier, 1995, https://doi.org/10.1016/S0927-0507(05)80107-0.

[21] B. Fleischmann, H. Meyr and M. Wagner, Advanced planning, in: H. Stadtler, C. Kilger and H. Meyr (Eds.), Supply Chain Management and Advanced Planning: Concepts, Models, Software, and Case Studies, pages 71–95, Springer, 5th edition, 2015, https://doi.org/10.1007/978-3-642-55309-7\_4.

[22] J. R. Rice, The algorithm selection problem, Advances in Computers 15 (C) (1976) 65–118, https://doi.org/10.1016/S0065-2458(08)60520-3.

[23] H. Schwarz, L. Kotthoff, H. Hoos, W. Fichtner and V. Bertsch, Improving the computational efficiency of stochastic programs using automated algorithm configuration: An application to decentralized energy systems, Annals of Operations Research https://doi.org/10.1007/s10479-018-3122-6.

[24] P. Kerschke, H. Hoos, F. Neumann and H. Trautmann, Automated algorithm selection: Survey and perspectives, Evolutionary Computation 27 (1) (2018) 3–45, https://doi.org/10.1162/evco\_a\_00242.

[25] L. Kotthoff, Algorithm selection for combinatorial search problems: A survey, in: C. Bessiere, L. De Raedt, L. Kotthoff, S. Nijssen, B. O’Sullivan and D. Pedreschi (Eds.), Data Mining and Constraint Program Approach, Springer, pages 149–190, https://doi.org/10.1007/978-3-319-50137-6\_7.

[26] Y. Pushak and H. Hoos, Algorithm configuration landscapes:, in: A. Auger, C. M. Fonseca, N. Lourenço, P. Machado, L. Paquete and D. Whitley (Eds.), Parallel Problem Solving from Nature XV, Springer, 2018 pages 271–283, https://doi.org/10.1007/978-3-319-99259-4\_22.

[27] A. Blot, A. Pernet, Jourdan, M. Kessaci-Marmion and H. Hoos, Automatically configurin ti-objective local search using multi-objective optimisation, in: H. Trautmann, G. R lamroth, O. Schütze, M. Wiecek, Y. Jin and C. Grimme (Eds.), Evolutiona Multi-Criterion Optimization, Springer, 2017 pages 61–76, https://doi.org/10.1007/978-3-319-54157-0\_5.

[28] E. K. Burke, M. Gendreau, M. Hyde, G. Kendall, G. Ochoa, E. Özcan and R. Qu, Hyper-heuristics: A survey of the state of the art, Journal of the Operational Research Society 64 (12) (2013) 1695–1724, https://doi.org/10.1057/jors.2013.71.

[29] J. H. Drake, A. Kheiri, E. Özcan and E. K. Burke, Recent advances in selection hyper- heuristics, European Journal of Operational Research https://doi.org/https://doi.org/10.1016/j.ejor.2019.07.073.

[30] J. Branke, S. Nguyen, C. W. Pickardt and M. Zhang, Automated design of production

scheduling heuristics: A review, IEEE Transactions on Evolutionary Computation 20 (1) (2016) 110–124, https://doi.org/10.1109/TEVC.2015.2429314.

[31] E. K. Burke, M. R. Hyde and G. Kendall, Evolving bin packing heuristics with genetic programming, in: T. P. Runarsson, H. Beyer, E. K. Burke, J. J. Merelo-Guervós, L. D. Whitley and X. Yao (Eds.), Parallel Problem Solving from Nature - PPSN IX, Springer, 2006 pages 860–869, https://doi.org/10.1007/11844297\_87.

[32] E. K. Burke, M. R. Hyde, G. Kendall and J. Woodward, Automatic heuristic generation with genetic programming: Evolving a jack-of-all-trades or a master of one, in: GECCO ’07, ACM, 2007 pages 1559–1565,

[33] S. Amaran, N. V. Sahinidis, B. Sharda and S. J. Bury, Simulation optimization: A review of algorithms and applications, Annals of Operations Research 240 (1) (2016) 351–380, https://doi.org/10.1007/s10288-014-0275-2.

[34] A. Gosavi, Simulation-Based Optimization: Parametric Optimization Techniques and Reinforcement Learning, Operations Research/Computer Science Interfaces Series, Springer, 2nd edition, 2015, https://doi.org/10.1007/978-1-4899-7491-4.

[35] M. C. Fu, Optimization via simulation: A review, Annals of Operations Research 53 (1) (1994) 199–247, https://doi.org/10.1007/BF02136830.

[36] M. C. Fu, S. Andradottir, J. S. Carson, F. Glover, C. R. Harrell, Y. C. Ho, J. P. Kelly and S. M. Robinson, Integrating optimization and simulation: Research and practice, Winter Simulation Conference Proceedings 1 (2000) 610–616, https://doi.org/10.1109/WSC.2000.899770.

[37] A. A. Juan, J. Faulin, S. E. Grasman, M. Rabe and G. Figueira, A review of simheuristics: Extending metaheuristics to deal with stochastic combinatorial optimization problems, Operations Research Perspectives 2 (2015) 62–72, https://doi.org/10.1016/j.orp.2015.03.001.

[38] S. Kirkpatrick, C. D. Gelatt and P. Vecchi, Optimization by simulated annealing, Science 220 (4598) (1983) 671–680, https://doi.org/10.1126/science.220.4598.671.

[39] D. E. Goldberg, Genetic Algorithms in Search, Optimization and Machine Learning, Addison-Wesley, 1989.

[40] G. Dueck and T. Scheuer, Threshold accepting: A general purpose optimization algorithm appearing superior to simulated annealing, Journal of Computational Physics 90 (1) (1990) 161 – 175, https://doi.org/10.1016/0021-9991(90)90201-B.

[41] C. Blum and A. Roli, Metaheuristics in combinatorial optimization: Overview and conceptual comparison, ACM Computing Surveys 35 (3) (2003) 268–308, https://doi.org/10.1145/937503.937505.

[42] M. Mohri, A. Rostamizadeh and A. Talwalkar, Foundations of Machine Learning, Adaptive computation and machine learning, MIT Press, 2012.

[43] S. Marsland, Machine Learning: An Algorithmic Perspective, CRC Press, 2nd edition, 2014.

[44] V. N. Vapnik, The Nature of Statistical Learning Theory, Statistics for engineering and information science, Springer, 2nd edition, 2000, https://doi.org/10.1007/978-1-4757-3264-1.

[45] M. Y. Kovalyov, C. Ng and T. E. Cheng, Fixed interval scheduling: Models, applications, , European Journal of Operational Research 178 (2) (2007) 331 – 342, https://doi.org/10.1016/j.ejor.2006.01.049.

[46] E. M. Arkin and E. B. Silverberg, Scheduling jobs with fixed start and end times, Discrete Applied Mathematics 18 (1) (1987) 1 8, https://doi 1016/0166-218X(87)90037-0.

[47] G. Woeginger, On-line scheduling of jobs with fixed start and end times, Theoretical Computer 130 (1) (1994) 5 16, https://doi.org/10.1016/0304-3975(94)90150-3.

[48] S. S. Seiden, Randomized online interval scheduling, Operations Research Letters 22 (4-5) (1998) 171–177, https://doi.org/10.1016/S0167-6377(98)00019-4.

[49] M. Hopf, C. Thielen and O. Wendt, Competitive algorithms for multistage online scheduling, European Journal of Operational Research 260 (2) (2017) 468 – 481, https://doi.org/10.1016/j.ejor.2016.12.047.

[50] M. Garey and D. Johnson, Computers and Intractability: A Guide to the Theory of

NP-Completeness, Freeman, 1979.

[51] J. Valério de Carvalho, Exact solution of bin-packing problems using column generation and branch-and-bound, Annals of Operations Research 86 (1999) 629–659, https://doi.org/10.1023/A:1018952112615.

[52] D. Johnson, Near-Optimal Bin Packing Algorithms, Ph.D. thesis, Massachusetts Institute of Technology, 1973.

[53] J. Csirik and G. Woeginger, On-line packing and covering problems, in: A. Fiat and G. Woeginger (Eds.), Online Algorithms: The State of the Art, pages 147–177, Springer,

[54] J. Csirik and D. S. Johnson, Bounded space on- line bin packing: Best is better than first, Algorithmica 31 (2) (2001) 115–138, https://doi.org/10.1007/s00453-001-0041-7.

[55] J. Sgall, Online bin packing: Old algorithms and new results, in: A. Beckmann, E. Csuhaj-Varju and K. Meer (Eds.), Language, Life, Limits: 10th Conference on Computability in Europe, pages 362–372, Springer, 2014, https://doi.org/10.1007/978-3-319-08019-2\_38.

Management Science 5 (1) (1958) 89–96, https://doi.org/10.1287/mnsc.1040.0262.

[57] G. Heisig, Planning Stability in Material Requirements Planning Systems, Springer, 2002, https://doi.org/10.1007/978-3-642-55928-0.

[58] G. K. Groff, A lot sizing rule for time-phased component demand, Production and Inventory Management 20 (1) (1979) 47–53.

[59] J. J. DeMatteis, An economic lot-sizing technique: The part-period algorithm, IBM Systems Journal 7 (1) (1968) 30–38, https://doi.org/10.1147/sj.71.0030.

[60] E. A. Silver, D. F. Pyke and R. Peterson, Inventory Management and Production Planning and Scheduling, Wiley, 3rd edition, 1998.

[61] W. Van den Heuvel and A. P. M. Wagelmans, Worst-case analysis for a general class of online lot-sizing heuristics, Operations Research 58 (1) (2010) 59–67, https://doi.org/10.1287/opre.1080.0662 .

[62] L. Ahlroth, A. Schumacher and H. Haanpää, On the power of lookahead in online

lot-sizing, Operations Research Letters 38 (6) (2010) 522–526, https://doi.org/10.1016/j.orl.2010.09.010.

[63] S. S. Skiena, Combinatorial search and heuristic methods, in: The Algorithm Design Manual, pages 230–272, Springer, 2008, https://doi.org/10.1007/11523468\_48.

[64] I. Wegener, Simulated annealing beats metropolis in combinatorial optimization, in: International Colloquium on Automata, Languages, and Programming, Springer, 2005 pages 589–601, https://doi.org/10.1007/11523468\_48.

[65] D. Henderson, S. H. Jacobson and A. W. Johnson, The theory and practice of simulated annealing, in: Handbook of Metaheuristics, pages 287–319, Springer, 2003, https://doi.org/10.1007/0-306-48056-5\_10.

[66] D. Delahaye, S. Chaimatanan and M. Mongea applications, in: Handbook of pages 1–35, Springer, 2019, https://doi.org/10.1007/978-3-319-91086-4\_1.

[67] F. Dunke, Online Optimization with Lookahead, Ph.D. thesis, Karlsruhe Institute of Technology, 2014, https://doi.org/10.5445/IR/1000042132.

![](/api/attachments/CFNZZPHK/fulltext/images/879ab6b3c5ed561f6f946427599610e83dda65bb019496321c0f78fe977c6fba.jpg)  
Figure 1

![](/api/attachments/CFNZZPHK/fulltext/images/34cd0dc2c35938e9b07c73b0f37c2d542e94d576ca562c99378c541e7e44e7a0.jpg)

![](/api/attachments/CFNZZPHK/fulltext/images/ed840f4f382370e1bf9957792d9939bd3e117da33b7718659bd29220c4ef3769.jpg)  
Figure 2

![](/api/attachments/CFNZZPHK/fulltext/images/71345536a80c914acf4f4b5c94a4d6e6c0cf1a319d973902b4b535df1807f858.jpg)

![](/api/attachments/CFNZZPHK/fulltext/images/0ceee477f326a1fd6df32a480fca402550687cc55a129157fc2f39d9c5a1434c.jpg)  
Figure 3

![](/api/attachments/CFNZZPHK/fulltext/images/05fabb4a4dcb92d8856e138410907f2c13d89d0a995ff5c84969964c7bee6f58.jpg)

![](/api/attachments/CFNZZPHK/fulltext/images/94cdcf71a741b7d9641eb14f1e51867bf7ed0f66577418189d6c28ca6b0050ed.jpg)  
Figure 4

![](/api/attachments/CFNZZPHK/fulltext/images/292f595229f3141de36b666dfabecb988ecb06194b8afbced11243bb6118e962.jpg)  
Figure 5
