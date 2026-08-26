---
otero_id: 16992
otero_key: "HKGB49DD"
title: "OR and AI approaches to decision support systems"
authors: "Kees M. van Hee; Antoni Lapinski"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90008-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# OR and AI Approaches to Decision Support Systems

Kees M. van HEE and Antoni LAPINSKI
Department of Mathematics and Computing Science, Eindhoven University of Technology, 5612 AZ Eindhoven, The Netherlands

First the concept of a decision support system (dss) is described. Then the first approach, in which the development of a network of models forms the kernel, is given. An example illustrates this approach. Then, architectures of decision support systems according to the first approach are given. Afterwards a second approach is considered, in which an (abstract) dss machine is described that can be tuned to specific decision situations. Finally the applicability of this approach is illustrated with an example.

![](/api/attachments/HKGB49DD/fulltext/images/bd7412035e70628906bf18f405ebce6054fc9b143d7de09edc02906f6b745a9b.jpg)

Kees van Hee studied mathematics at the University of Leiden. Then he worked for almost three years as researcher at this University. Afterwards he worked over four years at the Technological University Eindhoven where he wrote his doctoral thesis in the area of operations research. From 1987 till 1984 he was managing director of AKB B.V. in Rotterdam. This bureau specializes in model studies for planning and in the development of information systems. At that time he

gave advice to many companies in the transport sector and he conducted various decision support systems. Since 1984 he has been professor of computing science at the Technological University Eindhoven and besides he has kept his advice relations with industry.

![](/api/attachments/HKGB49DD/fulltext/images/af6f7864313164b5c2f828ddb5d922a3d9485edf443c9cfe19e927827096b5b0.jpg)

Antoni Lapinsky. Education: 1977-1982 University of Mining and Metallurgy, Cracow, Departement of Electrical Engineering, MSc in Computer Science. Currently working on doctoral thesis at the Department of Computing Science of the University of Technology Eindhoven. Professional career: 1982-1983 a scientific assistant at the Institute of Computer Science of the University of Mining and Metallurgy in Cracow. 1983-1985 a scientific assistant at the System Re

search Group of the Institute of Industrial Chemistry, Cracow. From 1985 a scientific assistant at the Department of Computing Science of the University of Technology Eindhoven. Professional interests: Logic programming, Prolog, applications of logic programming to decision support systems.

## 1. The Concept of a Decision Support System

Although there are no generally accepted definitions of Operations Research (OR) and Artificial Intelligence (AI) we call the first, and more classical approach the OR-approach and the second one the AI-approach. In the OR-approach mathematical models such as (non-)linear optimization models, combinatorial models, queuing and simulation models form the basis of a decision support systems (dss). Artificial Intelligence may be described as the study of knowledge representations and their use in language, reasoning, learning and problem solving (cf. [So84]). One of the objectives of AI is to develop methods and techniques for constructing flexible computer systems, i.e. systems that can adapt to changing environments without being reprogrammed. The use of heuristics is essential in the AI-approach.

It is a difficult task to give a precise and generally accepted definition of a decision support system. We will give our concept of a dss by presenting main functions that need to be fulfilled by such a system. We consider a dss as a subsystem of an information system and therefore we first define information systems. An information system fulfils two tasks for some target system. Examples of target systems, also called object systems, are companies as a whole, departments of companies and small production units. The tasks an information system performs are: monitoring and control of state transitions of the target system. These tasks can be realized by humans and (or) a computer system. Large parts of the monitoring task are nowadays performed by computer systems. The control task is often performed by persons, called decision makers. Besides the monitoring task computer systems assist decision makers by reporting and analysing the registered information to obtain knowledge of the mechanisms of the target system.

A dss is a computerized part of an information systems that consults decision makers with their control task by

1. Computing the effects of actions that the decision maker proposes. We call this: evaluation of actions.

2. Generation of actions that optimize some criterion function, chosen by the decision maker.

Often the evaluation and generation of actions proceeds in an iterative way. For the evaluation of actions there are evaluation functions. These functions are defined by the decision maker in the operational phase of the system, or they are defined by the designer of the dss in the design phase.

We assume the ranges of these functions are some totally ordered sets (sometimes we assume that it is the set of real numbers). Often the evaluation functions are conflicting. Two evaluation functions $E_{1}$ and $E_{2}$ are said to be conflicting if there exist two actions $a_{1}$ and $a_{2}$ such that

$$
E _ {1} (a _ {1}) <   E _ {1} (a _ {2}) \quad \text { and } \quad E _ {2} (a _ {1}) > E _ {2} (a _ {2}).
$$

There are several ways to deal with such a problem. One way is to define some linear combinations of the evaluation functions and for each one some bound. Then one of the combinations has to be optimized under the constraint that the other linear combinations do not exceed their bound. A facility to help the decision maker in choosing these linear combinations and bounds is called a facility for multicriteria analysis and is often considered to be an essential facility of a dss. Another feature of a dss is a facility for sensitivity analysis. The evaluation of the effect of an action requires a mathematical model of a part of the target system. Such a model contains parameters that are obtained from several resources, such as estimates based on historical data of the target system or hypotheses from a decision maker. To get confidence in the advises of a dss, the decision maker wants to see the influences of variations of parameter values for parameters he is not sure of. This is called sensitivity analysis.

Of course a dss has to have an adequate user interface which allows the decision maker to update parameters, to retrieve and compare already computed actions and their effects and to control the evaluation and generation processes. Dss are used for operational planning and strategic planning both. The first type of planning requires the optimal assignment of resources. Typical examples are jobshop planning and vehicle routing. The second type of planning requires the optimal determination of capacities of resources, such as the volume and locations of depots. A dss for operational planning is used frequently while a dss for strategic planning is used incidentally. This difference reflects in different architecture of human interfaces.

## 2. Models in Decision Support Systems

The use of operational research (or) techniques to assist decision makers is much older than the field of dss. Traditionally OR-specialists analysed the decision situation and selected or designed a mathematical model to describe the set of feasible actions and their effects. Then they designed algorithms to compute actions that are optimal with respect to some criterion, for instance a linear combination of effects. Finally they paid attention to the system-design. Hence in this phase they designed a database for parameters, actions and their effects, and a user interface. In the traditional approach it did not make much difference if the system was used by the OR-specialist as an intermediary between the decision maker and the model, or by the decision maker itself. In the last case the system should be more faultproof than in the first case. In fact the OR-specialist as an intermediary between the decision maker and the model, or by the decision maker itself. In the last case the system should be more faultproof than in the first case. In fact the OR-specialist made a system to automatize his own work instead of a system to assist a decision maker. At the end of the seventies OR-specialists changed their views. The dss-concept as described in section 2 was born. A system that could assist a decision maker without interference of an OR-specialist became the target of their design efforts. Optimization was no longer a goal as such, however, it became an approach to generate actions that could be considered as proposals to a decision maker. The dss has to propose actions that satisfy the needs of the decision maker and not in the first place some abstract criterion.

Nowadays adaptability of a dss for changes in the decision situation is one of the most important characteristic of a dss. Consider a dss in which some constraint on feasible actions is described by a linear inequality. Suppose that the structure of the decision situation changes such that this constraint has to be replaced by a quadratic inequality. Often a dss cannot accept such a change without a serious modification of the model and the software. A lot of dss in practice had a short life according to this kind of problems.

There is a tradeoff between adaptability and efficiency of a dss. For the generation of actions usually algorithms are used that exploit the structure of the model of the decision situation, for instance if the model is a linear program. However, to obtain a high degree of adaptability these algorithms must use as less as possible of structural details of the model that are expected to be charged in future.

The types of models that are used to build dss's are simulation models, queueing models, linear and nonlinear programming models, combinatorial optimization models and Markov decision models. The first two types are mainly used for evaluation of actions while the other models are used to generate actions. Time will almost always play a role in a decision situation. Sometimes however it is not necessary to represent time in a model. For instance if the decision maker has to take a decision for only one planning period and if the effect of this decision will not influence the decision situation after that period, time will play no role. Such decision situations can be called stationary. If a model is developed for a stationary decision situation it is usually difficult to adapt the model if it turns out that the decision situation is non-stationary. It seldom occurs that a decision situation is adequately described by only one model. Mostly decision situations have several aspects that have to be described by different models, for instance a linear program and a queueing model. If these models describe independent aspects of the decision situation the dss will not have the same architecture as with one model. Only the user-interface and the database serve more models instead of one. Models in a dss are called independent if they only need exogenous parameters of a decision situation to determine the effects of actions or the actions themselves. They are called dependent if at least one of the models needs a parameter that is computed by another model. We call these parameters endogenous parameters. Dependencies between the endogenous parameters may be represented by a directed graph, where each node represents a model and each arc is labeled with the name of an endogenous parameter. If this graph is acyclic there is an ordering of model computations such that each model only needs exogenous parameters of already computed endogenous parameters. However if there is a cycle in the graph there is a more serious dependency between the models. An example of such a situation is described in the next section. Other examples occur in hierarchical planning situations where at the highest level a capacity is optimized using a resource assignment rule from a lower level. However this assignment rule is computed for a given capacity of the resource. In Fig. 1 an example is given. The exogenous parameters as well as the endogenous parameters that are not used in other models are not represented.

![](/api/attachments/HKGB49DD/fulltext/images/e7b28ec42063bec685beafde112fdec10970b46cf98a43004732527ea8935c71.jpg)  
Fig. 1.

A consistency requirement for such a network of models is that the parameters used in the network form a fix-point for the function formed by the network that maps the set of parameter vectors into itself. In the example the vector $\langle P_{1}, P_{2}, P_{3}, P_{4} \rangle$ is a fix-point of the function if: $M_{1}(P_{3}) = \langle P_{1}, P_{4} \rangle$ , $M_{2}(P_{1}) = P_{2}$ and $M_{3}(P, P_{4}) = P_{3}$ .

Often the analytical properties of this function, such as bounds on derivatives are not known. One may only compute the function value for some parameter vector and each evaluation may be very costly. There are many techniques for the determination of fix-points; however many of them are infeasible for the situation we sketched. In practice the method of successive approximations (for $n=0,1,2,\ldots:q_{n+1}=T(q_n)$ and $q_0$ is some start vector and T the function formed by the network) often converges.

## 3. Example: dss for a Labour Pool

In this section we consider an example of a dss that reflects many of the aspects we mentioned in section 2. For a more detailed description of this dss we refer to [He87]. Consider a group of companies or departments having the same type of work and rather high variation of their daily workload. Our example originates in a harbour were stevedoring companies have highly varying workloads, with almost no correlation between each other. Such companies or departments may consider to establish a pool of worker. So they will cover their workload with own personnel and poolworkers. The pool is a non-profit organisation and therefore it cannot take the risk of idle time of workers.

The participating companies take a share of the pool personnel for which they are guarantee. The pool is so divided into guaranteed parts. Each day a company may demand its guaranteed part, and it will get it. However if a company wants more workers and other companies do not need their guaranteed part the company can get more workers. If a company does not need its part completely, some workers may be used in other companies. If there are idle workers in some part then the guaranteeing company has to pay for these people. On the other hand if a company cannot cover its workload by pool workers then it has to hire people from outside the pool, which is supposed to be more expensive.

The pool is controlled by a board formed by the participating companies. Periodically the board has to consider the guaranteed parts and the companies may wish to switch personnel from their own company to the pool and vice versa. The price of a pool worker per day is determined at the end of a period by dividing all the cost of the pool by the number of used labour days. Daily the companies put their demands to the pool and using a complex algorithm the pool management determines the daily assignments to the companies. The details of this algorithm are not important here, we only note that exaggerating the demands by the companies, in one direction or the other, does not influence the assignment.

For each company we describe the expected daily cost, using the following notations:

Model for one company

w = a random variable with known distribution expressing the daily workload,

$b =$ number of own workers, a decision variable,

$g =$ number of poolworkers in the guaranteed part, a decision variable,

$k =$ daily cost of an own worker,

$p =$ price of a poolworker per day,

$q =$ price of an external worker per day,

t = assignment of poolworkers at some day, a random variable determined by all w's of the companies, b's and g's and an algorithm.

We assume k < p < q because otherwise own workers or poolworkers would never be used. Further we define: $v = (w - b)^{+}$ , the daily demand of the company for poolworkers; this is also a random variable, note $x^{+} = \max(0, x)$ .

The exact value of the expected daily cost is

$$
\begin{array}{r l} & k * b + p * g + q * E (v - t) ^ {+} - p * E (g - t) ^ {+} \\ & \quad + p * E (t - g) ^ {+}, \end{array}
$$

where E is the expectation operator induced by the product probability of the daily workload distributions. This formula can be interpreted in the following way. The company has to pay its own workers, and its share in the pool $(k * b + p * g)$ . However if the demand v is larger than the assignment t it will hire external workers for q per day. On the other hand if the assignment is less than the guaranteed part g the company will get back the price of each poolworker for g - t workers. If a company gets more than its guaranteed part it has to pay fir t - g workers on top. If each company would know the demand of other companies they could in theory compute this value. However they do not know these distributions for privacy reasons. Therefore they work with another cost function:

$$
\begin{array}{r l} k * b + p * g + [ p * B + q * (1 - B) ] & \\ * E (v - g) ^ {+} - p * E (g - v) ^ {+}, \end{array}
$$

where B is the probability of getting a worker from another company's part, if needed. It is clear that the second cost function is not equal to the first one. However it is a good approximation and it has a nice property: it can be optimized for each company separately if B is known, because the expected values only depend on the distribution of the company itself. The companies may estimate B from the past. In fact the companies determine their policy, i.e. their determination of the desired b and g using the second cost function. Therefore we use it in the dss as well. There is also another reason.

The exact cost function, given all the workload distributions is very time consuming, since for each vector of b and g values we can only compute the cost by running a simulation program. So each evaluation of a simultaneous decision (i.e. the vector of b and g values) is very time consuming itself. Hence a simultaneous optimization over all companies, for instance minimizing the sum of the expected daily cost is not feasible in an interactive system.

![](/api/attachments/HKGB49DD/fulltext/images/1bace85255da7da75b9f6798668ff8da983d425160381bc04a2d0636e753e06d.jpg)  
Fig. 2.

The poolboard will determine for a new period to the b and g values of the companies, based on the estimated workload distributions in the following way. Note that these workload distributions are kept secret to the board members. The B values and the price p are computed by a simulation model, that given b and g values, simulates the pool for one or two years. The price p is computed as the salary cost of the workers plus a share in the overhead of the pool divided by the used labour days. The b and g values are determined by minimizing the second cost function per company, given B and p. Hence we have here a simple model network (see fig. 2).

The model called “Optim” generates decisions while the model “Sim” computes the effects of decisions including the exact expected cost per company. The model consistency requirement provides here as a by-product, an interesting optimality criterion for this multi company game. The vector of b and g values is optimal if for each company the expected cost are minimized under the condition that the intercompany parameters B and p are constant. In practice the convergence of the iteration process to get the fix-point of the model network is rather quick. The dss can also deal with constraints on b and g values, such as ranges for these values.

## 4. Architecture of Decision Support Systems

In this section we describe, using dataflow diagrams, the structure of a dss constructed following the usual OR-approach. Afterwards we change this structure into a more expert systems architecture.

The term ‘architecture’, points to structure and to the way constructing an object. We will consider both aspects here. In both approaches one has to analyse the decision situation first. The designer has to determine the exogenous parameters, the domains of the decision variables, i.e. the sets from which the actions may be drawn and the endogenous parameters that the decision maker wants to see to judge a decision.

The endogenous parameters the decision maker wants to see are computed by evaluation functions however in the first stage of design; only the names and types of these parameters are important. If there are several criteria to generate actions each criterion can often be described by linear combinations of the endogenous parameters and some bounds (cf. section 1). If for instance these endogenous parameters are $e_{1}, e_{2}, \ldots, e_{n}$ then a criterion has the form:

maximize $\sum_{j=1}^{n} \gamma_j e_j$ under the condition that

$$
\forall i \in \{1, 2, \dots , m \}: \sum_ {j = 1} ^ {n} \alpha_ {i j} e _ {j} \leq \beta_ {j}.
$$

Note that the endogenous variable may not be chosen freely but are of the form:

$$
e _ {j} = f _ {j} (p, a),
$$

where $f_{j}$ is an evaluation function, p a data structure that represents exogenous parameters and a, a data structure representing an action. Hence we are in general not dealing here with a linear programming problem. A set of coefficients $\alpha$ , $\beta$ and $\gamma$ is called a set of criterion coefficients.

A scenario is a datastructure consisting of values for the exogenous parameters, an action, a set of criterion coefficients and values for the endogenous parameters such that the action optimizes the criterion and the endogenous parameter values are the effects of an action. Hence a scenario describes one instance of the decision situation. The decision maker will only supply exogenous parameter values and an action or a set of criterion coefficients. The dss will supply the rest. If the structure of scenarios is determined the designer may perform two tasks in parallel.

One of these tasks is to design a part of the dss we call the manipulator (cf. Fig. 3). The manipulator consists of a database that conceptually may be divided into four subdatabases. One containing a set of exogenous parameter values. In each scenario only one set is used. However there may be many sets. Some of them may be derived by some filtering process from a database that monitors the target system. Others may be defined by the decision maker himself or by some external source. The second subdatabase contains actions. Note that actions, as exogenous parameters, may have complex database structures. Each action may be used in a scenario. The third database contains sets of criterion coefficient sets. Finally, the fourth subdatabase contains scenarios. The manipulator further consists of a database management system to update the four subdatabases and to query the scenario databases. The query processor must allow queries in which comparisons over several scenarios are possible.

![](/api/attachments/HKGB49DD/fulltext/images/7255f1c08ab7d592c090b8cb99909fee5f26d55588b6099123286c7babcd9df4.jpg)  
Fig. 3. The manipulator, a box represents a database, a bubble a (software) processor. (1) is coming from a monitoring database, (2) represents the decision maker.

The other task to perform is generation and evaluation of actions. In the OR-approach often models are developed that are specific for the decision situation. When there is more than one model we get the structure represented in Fig. 4. Here we have a number of models all covering some aspects of the decision situation. They can often be divided into two groups: generators and evaluators. Further there is a processor that takes care of the model interfacing and the iteration of computations to approximate a fix-point for model consistency. This processor is exchanging endogenous parameters between the models and a database for these parameters.

Often it is very expensive to construct a generator/evaluator part for one decision situation. What we wish is a system that can easily be adopted to a specific decision situation. For decision situations that can be modelled by linear programming models such systems exist. Such a system may be called a dss-generator. The only modelling activity is to create a matrix generator or to generate such a matrix generator (cf. [Om81]). For other decision situations we also would like to have an architecture in which only the domain specific knowledge has to be given to the system to behave as a dss for that situation. In expert systems constructed from a shell this is possible by only adding facts and rules to the shell. The domain specific knowledge consists of the data already considered by the description of the manipulator, a description of evaluation functions and search rules for a general purpose generator of actions. A sketch of such an architecture is given in Fig. 5. There we see three processors. One generator and one evaluator. These processors are used in each specific decision situation. However they have parameters in the form of expressions to specify the evaluation functions and search rules to control the search process of the generator. Of course there are two databases to store these expressions and rules and there is a processor to update these databases. The decision maker will only use the manipulator. The designer of a dss will fill and update the expressions and search rules databases. It is the intention that the expressions and search rule definitions are formulated in a very high level language.

![](/api/attachments/HKGB49DD/fulltext/images/512c2c701c204584e6229e9d56813ed1bedc87b8f0e1b9463d4027e8cb94a88d.jpg)  
Fig. 4. Architecture specific for one decision situation. (cf. the explanations of fig. 3).

![](/api/attachments/HKGB49DD/fulltext/images/e2f753f5e586c149f0d6aab0d576f25846eec8360b5bbff73430a8b7335146a4.jpg)  
Fig. 5. Architecture of a dss-generator.

In the next section we describe a machine that has in fact this architecture.

## 5. An Abstract dss Machine

As mentioned before the classical, model-based decision support systems have a low adaptability to changes in decision situation. One of the main reasons for this is that these decision support systems are focused on optimization of decisions according to criteria of a special structure. In order to obtain optimal decisions in a fast way the dss-designer has exploited the structural properties of the decision situation and the criteria as much as possible. However in practice these structural properties, such as linearity of constraints, do not hold in all cases, or they may change.

Perhaps there is a complementary way to go when building a dss. We think that in many practical decision situations the ability to respond quickly to changes is more important than an optimal solution according to one of the possible criteria. What really counts is to keep the object system within some feasible region. Therefore we think, the optimization aspect can be relaxed. What should be offered instead is a dss that can produce acceptable solutions and that can easily meet new requirements of a decision maker.

We would like to give the decision maker more freedom in formulating constraints imposed on a solution to a decision problem and the ability to classify constraints with respect to their relative importance. This way we come to a concept of “hard” constraints, i.e. the constraints that have to be satisfied by any solution and the “soft” constraints, i.e. desirable properties of a solution though not obligatory. It should be pointed out that the formulation of the “hard” and the “soft” constraints is a subject to change because of the changing situation within the object system and its environment.

It is a common practical situation that some decisions are generated outside of the application of the dss to a decision problem for instance, by the decision maker himself. In this case the dss is required to verify the correctness of the decisions with respect to the “hard” constraints mentioned already and if the result of the verification is positive the problem solving process should be continued by the dss. This feature makes possible the generation of decisions in a cooperative way by the dss and the decision maker.

We believe that some AI techniques especially theorem proving and search algorithms offer some hope in realizing the features of the dss discussed here though the complexity issues should not be forgotten. In the next section we describe a dss as an abstract machine in which the knowledge of the decision situation, the so-called dependent knowledge, is made explicit. Such a dss is easy to adapt by changing the domain knowledge. We suggest to call a system that can behave as a dss for a specific decision situation, if it is given the domain knowledge a dss-shell. Based on the abstract machine one could design such a shell. In section 6 we specialize the machine to become a job-shop scheduler.

5.1. Informal Presentation of the Abstract dss Machine

When specifying a problem like job-shop shedding we need to define:

(i) Target system (e.g. a job-shop). We will define the target system using first order logic (cf. [Ga86]). We will do so in order to achieve a compact and a precise description of the target system. We assume the existence of an associated proof system since it is essential to reason about the target system. For reasons of computational complexity we can restrict ourselves to a subset of first order logic like Horn Clauses with negation as a failure-rule.

(ii) Graph of plans. By the graph of plans we mean here a graph where nodes define partial plans and edges define manipulations upon plans. In order to apply a manipulation to a plan some constraints upon the plan must hold (they are preconditions to the manipulation) and some constraints must hold on the resulting plan (they are postconditions of the manipulation) (cf. [Ni82], [Ko79]).

(iii) Predicate defining a set of complete plans. We will call it a goal predicate.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
NewPlans: $\mathbf{S}^{*}*\mathbf{D}\rightarrow \mathbf{S}^{*}$
</div>

```txt
Tm (m, d) := if Rs (m) = nil then Rr(m) else
    if Goal(Rs(m), d) then Rs(m) else
    Tm(Rm(m, NewPlans(m, d)), d)
```

(iv) Some quality criterion (like a cost function) by means of which plans are evaluated.

(v) Set of functions which administrate the search process and guide the search. We will call them selection functions. By composing different selection functions we may change the search strategy in order to suit the search space and our requirements with respect to the quality of the solution, i.e. a plan (cf. [Ni82], [Pe84]).

(vi) Recovery function which defines the behaviour of the dss machine in case no plan satisfying the goal predicate is found. One possible option is to deliver the best partial plan constructed.

As it could be expected the dss machine has a memory structure for collecting constructed plans. The memory is divided into two disjoint substructures:

(i) The one which contains the plans that are going to be further transformed. These plans will be called active plans.

(ii) The one which contains the plans that will not be transformed any more. These plans are called non-active plans. This is so because either all possible transformations for non-active plans have been considered or it is not worthwhile to transform these plans any further.

We will discuss now the behaviour of the machine during the problem solving. It is assumed that all the components discussed so far are given.

To start the search for a required plan an initial plan is input to the machine as the only active plan. The memory of the machine that contains non-active plans is empty. An active plan is selected from the memory of the active plans by the selection function. In the beginning of the search the choice is limited to the initial plan. The goal predicate is applied now to the selected plan. In case the predicate evaluates to true the plan is output and the machine stops. Otherwise the machine attempts to transform the selected plan to a set of new plans by applying some manipulation to it as defined by the graph of plans. In case of a job-shop a manipulation could mean adding an operation to the schedule. Suppose a set of new plans is found. The selected plan is transferred to the non-active plans and the subset of the new plans is added to the memory of the active plans. Now the machine selects the plan for further transformations by applying a selection function to the active plans. The search continues until either a required plan is found or the memory structure containing the active plans is empty. In the latter case the recovery function is applied. One possible option for the recovery function is to select the best plan from the non-active plans as a partial solution to the problem. Since the recovery function is not a fixed element of the dss machine therefore another behaviour can be specified. In case of a cyclic graph the dss machine can enter a loop, therefore some loop-detection mechanism has to be incorporated. However we do not discuss it here.

## 5.2. An Abstract dss Machine - A Formal Definition of the Components

An abstract dss machine is defined as a 12-tuple:

$\langle D, S, A, M, Goal, Tm, T, Q, Ra, Rr, Rs, Rm, \rangle$ , where

D: a set of target systems. A target system is defined by a set of formulas of a first order language. This is a domain dependent knowledge.

S: a set of elements called plans.

A: a set of elements called manipulations.

M: $(\mathbf{S}^{*}) * (\mathbf{S}^{*})$ - a memory structure.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Goal: $\mathbf{S}*\mathbf{D}\rightarrow \{\mathrm{true},\mathrm{false}\}$
</div>

```txt
Goal(p, d) = "true if p is a required plan otherwise false".
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Tm: $\mathbf{M}*\mathbf{D}\to \mathbf{S}$; a constructor function.
</div>

Tm(m, d) = “a plan constructed in the context of the memory m and the target system d”.

NewPlans(m, d) = "a set of new plans constructed from the selected plan Rs(m) and the set of selected manipulations Ra(Q(Rs(m),d))".

T(old\_plan,a) = "a new plan created by a manipulation a to the plan old\_plan".

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Rest: $\mathbf{S}^{*}\rightarrow \mathbf{S}^{*}$ such that
</div>

```txt
Cons(First(list), Delete(Rest(list), element))
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Append: $\mathbf{S}^{*}*\mathbf{S}^{*}\rightarrow \mathbf{S}^{*}$
</div>

T has to be defined with respect to a specific application (e.g. a job-shop scheduling or vehicle routing).

Q: $\mathbf{S}*\mathbf{D}\to \mathbf{P}(\mathbf{A})$

$Q(s, d) = \text{``a set of manipulations for a given plan s with respect to the target system d''}.$ $Q$ has to be defined for a specific application.

Ra: P(A) → P(A); a manipulation selection function. P(A) denotes a power-set of A.

Ra function selects a subset of manipulations that are going to be applied to a given plan.

Rr: M → S; so called recovery function.

It defines the behaviour of the dss machine in case no plan satisfying the Goal predicate has been found. Rr has to be defined for a specific application.

Rs: $\mathbf{M}\to \mathbf{S}$

Rs (m) = "a plan selected from the memory m".
Rs is defined in the context of a specific search strategy as it is illustrated by examples.

Rm: M \* S\* → M; a memory update function.
Rm (m, plans) = “a memory m updated by a sequence of plans”.
Rm is defined with respect to specific search strategies.

We are using a higher order functional programming language to define the essential components of the dss machine. Some conventions concerning the syntax and the semantics of the language are given below. This is not a formal definition of the language however. For the introduction to functional programming see [cf. GI84].

(i) Function symbols start with uppercase and variables start with lowercase.

(ii) “fname” $(p_{1},\ldots,p_{n})$ := “expression”
A function “fname” with parameters $p_{1},\ldots,p_{n}$ is defined by an “expression”. The “expression” is made of a function application in a prefix form or it is made of “if then else” expression.

(iii) A function application in a prefix form is denoted by “fname”(a $_{1}$ , ..., a $_{n}$ ) where a $_{1}$ , ..., a $_{n}$ are arguments of the function. As opposed to the function definition the function application is never followed by ‘ := ’ symbol.

(iv) if then else expression has a form: If “condition” then “value A” else “value B”. Its meaning is: if “condition” is true then the result is “value A” otherwise it is “value B”.

(v) Lists:

$\langle \rangle$ is a list (an empty list)

If x is a list and v some value then $\text{Cons}(v,x)$ is a list.

By convention we write $\operatorname{Cons}(x_1, \operatorname{Cons}(x_2, \ldots, \operatorname{Cons}(x_n, \langle \rangle) \ldots))$ as $\langle x_1, x_2, \ldots, x_n \rangle$ .

Cons is called a list constructor and it is a primitive function.

There are two other primitive functions defined on lists. These are:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
First: $\mathbf{S}^{*}\rightarrow \mathbf{S}$ such that
</div>

First( $\langle\rangle$ ) = nil and First(Cons(x, y)) = x

$\operatorname{Rest}(\langle \rangle) = \langle \rangle$ and $\operatorname{Rest}(\operatorname{Cons}(x, y) = y$

The above equations are defined outside the functional language we consider.

(vi) Other important functions:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Delete: $\mathbf{S}^{*}*\mathbf{S}\rightarrow \mathbf{S}^{*}$
</div>

```txt
Delete(list, element) :=
```

```txt
if list = <> then <> else
```

if First (list) = element then Delete(Rest(list), element) else

Eval(f, args) = "a result of function f applied to arguments that are elements of the list args". Eval is a primitive function.

Select(list, predicate) := if list = < > then nil else
    if Eval(predicate, <First(list)>) then First(list)
    else Select(Rest(list), predicate)

set abstraction function: {x | x ∈ "domain" ∧ Predicate(x)}

means: a set of elements of the “domain” such that Predicate(x) evaluates to true. A set its represented as a sequence. The set abstraction is a primitive function.

5.3. Specifying the Abstract dss Machine - Search Strategies

We will show now how by giving the appropriate definitions of Rm and Rs functions we can change the search strategies performed by the function Tm. We deal with acyclic graphs only, therefore no loop-detection mechanism is considered here. We assume that unless stated otherwise:

$$
\begin{array}{l} \text {Ra (manipulations): = manipulations} \\ \text {(the identity function)} \\ \text {Goal (s,d): = "a predicate defined over S\times D"} \\ \text {Rr(m): = nil (the recovery function returns nil)} \end{array}
$$

Rm ( $\langle m_n, m_0 \rangle$ , extensions) := $\langle \text{Append}(extensions, \text{Rest}(m_n)), \text{Cons}(\text{First}(m_n), m_0) \rangle$ where $m_n$ : a sequence of active plans, $m_0$ : a sequence of non-active plans.

## 5.3.2. Hill-climbing (hc)

$$
\begin{array}{r l} & \mathrm{Rs} (\langle \mathrm{m} _ {n}, \mathrm{m} _ {0} \rangle) := \mathrm{First} (\mathrm{m} _ {n}) \\ & \mathrm{Rm} (\langle \mathrm{m} _ {n}, \mathrm{m} _ {0} \rangle , \text { extensions }) \\ & := \langle \text { Append } (\text { Order } (\text { extensions }), \text { Rest } (\mathrm{m} _ {n})), \\ & \quad \text { Cons } (\text { First } (\mathrm{m} _ {n}), \mathrm{m} _ {0}) \rangle \end{array}
$$

where Order: $S^{*} \rightarrow S^{*}$ , Order (plans) = “a permutation of plans for all subsequent elements $p_{i}$ and $p_{i+1}$ of the permutation, $p_{i} > p_{i+1}$ , where > is an ordering relation on S.

We call Order(plans) an ordered permutation of plans. The ordering on S can be constructed on basis of an evaluation function E: $S \rightarrow R$ in particular.

$$
\begin{array}{l} \text {5.3.3. Breadth - first Search} \\ \mathrm{Rs} (\langle \mathrm{m} _ {\mathrm{n}}, \mathrm{m} _ {0} \rangle) := \mathrm{First} (\mathrm{m} _ {\mathrm{n}}) \\ \mathrm{Rm} (\langle \mathrm{m} _ {\mathrm{n}}, \mathrm{m} _ {0} \rangle , \text {extensions}) \\ := \langle \text {Append (Rest(m} _ {\mathrm{n}}), \text {extensions)}, \\ \quad \operatorname{Cons} (\mathrm{First(m} _ {\mathrm{n}}), \mathrm{m} _ {0}) \rangle \\ \text {5.3.4. Best - first Search (bestfs)} \\ \mathrm{Rs} (\langle \mathrm{m} _ {\mathrm{n}}, \mathrm{m} _ {0} \rangle) := \mathrm{First(m} _ {\mathrm{n}}) \end{array}
$$

$$
\begin{array}{r l} \operatorname{Rm} & (\langle \mathrm{m} _ {\mathrm{n}}, \mathrm{m} _ {0} \rangle , \text { extensions }) \\ & := \langle \operatorname{Order} (\operatorname{Append} (\text { extensions }, \operatorname{Rest} (\mathrm{m} _ {\mathrm{n}}))), \\ & \quad \operatorname{Cons} (\operatorname{First} (\mathrm{m} _ {\mathrm{n}}), \mathrm{m} _ {0}) \rangle \end{array}
$$

```txt
5.3.5. A Variant of Heuristic Search
Rs(⟨m_n, m_0⟩) := Select(m_n, Rs_select)
Ra(manipulations) = Select(manipulations,
    Ra_select)
Rm(⟨m_n, m_0⟩, extensions)
:= ⟨Append (extensions, Delete (m_n, Rs(m_n))), 
    Cons(Rs(m_n), m_0)⟩
where
Rs_select: S → {true, false}
Rs_select(plan) = “true if plan satisfies some selection criterion otherwise false”.
Ra_select: A → {true, false}
Ra_select(manipulation) = “true if manipulation satisfies some selection criterion otherwise false”.
```

## 6. A Job-shop Scheduler

A job-shop is a production system consisting of a set of machines capable of performing different functions. A job-shop processes jobs. A job is defined by a set of partially ordered tasks. A task is defined as an activity performed on machine of some type for a specific period of time. Since a number of tasks is present in the job-shop possibly competing for the machines we have to solve a problem of assigning the tasks to the machines. In other words we have to construct a job-shop schedule that is an assignment of tasks to the machines with respect to some constraints. Namely a task has to be assigned to a machine of a required type and for a required period of time (such assignment is called operation). The ordering of tasks as defined by the schedule has to preserve the partial ordering of tasks within a job. A machine cannot be used by two tasks at the same time. Usually there are some time limits (deadlines) imposed on the jobs. Our goal is to define a job-shop scheduler as an abstract dss machine. We will do so by specifying elements of the 12-tuple discussed earlier. We will use a method of forward scheduling that can be described as follows. The scheduling starts at some moment of time t. We construct operations with their begin time equal to t until we cannot continue any further. This may happen when there are no required machines free or all the tasks whose predecessors were finished before the time t have been scheduled. Now we look for a future moment of time p when some of the scheduled tasks is finished. If p is found then we move the scheduling time forward to p and again we try to construct a new set of operations with their begin time equal to p. We continue the scheduling process until all the tasks are scheduled or we reach the planning horizon.

The target system i.e. a job-shop will be defined by a set of formulas of first order language. The symbols used in the definition of the target system should not be confused with the symbols used in the functional language already discussed. The conventions we follow are

(i) $\vee, \wedge, \neg, \rightarrow, \leftrightarrow$ are logical connectives, $\forall, \exists$ , are quantifiers, $= \text{is the equality symbol, } < \text{ is the symbol of the usual ordering relation on N}$ , (ii) predicate symbols start with uppercase,

(iii) variables start with lowercase; all variables are quantified,

(iv) function symbols start with lowercase or they are ‘\*’ or ‘+’.

## The Components of the Job-shop Scheduler

## S: a set of schedules.

A schedule is defined by a set of operations (we will call it plan) and by a scheduling time greater or equal to the begin time of the most recent operation in the plan. An operation defines an assignment of a task to a machine from the begin time till the end time. Schedules are represented by terms: schedule (time, plan) and operations are represented by terms: operation(task, job, machine, begin, end).

## A: a set of manipulations.

There are two classes of manipulations: manipulations represented by terms move(timex) and manipulations represented by terms operation (task, job, machine, begin, end).

The term: move(timex) defines a request to move forward :the scheduling time to timex. operation(task, job, machine, begin, end) defines a request to assign the task to the machine from the begin time till the end time.

$$
\mathrm{Q}: \mathrm{S} * \mathrm{D} \rightarrow \mathrm{P} (\mathrm{A})
$$

$$
Q (s, d) := \{a | (k \cup d \vdash \text { Manipulation } (s, a)) \}
$$

Q (s,d) = "a set of all manipulations such that Manipulation(s,a) can be deduced from the target system d. Manipulation is a predicate symbol which appear in d. The derivability relation for a theory made of d and logical axioms k of the associated proof system is denoted by $\vdash$ . Although it is a very important issue we do not discuss here how such a system performs deductions. It has to be remembered that the dummy variable a above is assigned a value as a result of a deduction process. Thus the variable a can be considered as the output variable and the variable s as the input variable. We rely here on procedural semantics of the logic language employed.

d: the set of axioms describing the target system. Each axiom is defined informally first and then formally.

## The Target System Axiomatisation

Manipulation (schedule(current\_time, plan), operation (task, job, machine, begin, end))
iff

"the task belongs to the job and the machine suits the task, and the machine is idle within a required period of time from the begin to the end, and all the predecessors of the task are finished before the current\_time".

## Formally this can be formulated as:

∀ current\_time, plan, task, job, machine, machine\_type, begin, end

Manipulation (schedule(current\_time, plan), operation (task, job, machine, begin, end)))
↔

Is\_task(task, job, machine\_type, duration) ∧
Is\_machine (machine, machine\_type, speed) ∧
Finished\_predecessors (current\_time, task, job, plan) ∧

Idle\_machine (machine, begin, end, plan) ∧ begin = current\_time ∧

$$
\text { end } = (\text { current\_time } + \text { speed } * \text { duration }))
$$

Manipulation (schedule (timex, plan), move(timey))
iff

"there is no operation(task, job, machine, begin, end) that can be created in the context of the current schedule as defined by schedule(timex, plan) and timey is the next future moment of time when one of the tasks is finished".

∀ timex, timey, plan (Manipulation (schedule (timex, plan), move(timey))

(¬∃ task, job, machine, begin, end
Manipulation (schedule (timex, plan), operation (task, job, machine, begin, end)) ∧
Nextevent (timex, timey, plan)))

Is\_task(task, job, machine\_type, duration)
iff
"the task belongs to the job and requires a machine of the type machine\_type for the nominal time: duration".
It is defined by a set of ground atoms.

Is\_machine(machine, machine\_type, speed)
iff
"the machine is of the type machine\_type and has the speed machine\_speed".
It is defined by a set of ground atoms.

Nextevent (timex, timey, plan)

“timey > timex and timey defines the first moment of time when some machine is released by a task”.

∀ timex, timey, plan
(Nextevent (timex, timey, plan)

∃ task, machine, begin, job
(operation(task, job, machine, begin, timey) ∈ plan ∧

Finished\_predecessors (time, task, job, plan) iff

"all the predecessors of the task within the job are finished before the time with respect to the plan".

∀ time, task, job, plan
(Finished-predecessors (time, task, job, plan)
↔
∀ taskx

(Predecessor (job, taskx, task) →
∃ beginx, beginy, machine, endx
(operation (taskx, job, machine, beginx, endx) ∈
plan ∧ endx < time)))

Predecessor(job, tasksx, tasky)
iff

"the taskx is a predecessor of the tasky within the job". It is defined by a set of ground atoms.

Idle\_machine(machine, begin, end, plan)
iff

"the machine is idle (not used by any task) within the period from the begin to the end in the context of the plan".

∀ machine, begin, end, plan (Idle\_machine(machine, begin, end, plan)
↔

∀ task, job, beginx, endx
(operation(task, job, machine, beginx, endx ∈ plan → ¬Overlap(begin, end, beginx, endx)))

"two periods of time from a to b and from c to d overlap".

$\forall a, b, c, d$ (Overlap $(a, b, c, d) \leftrightarrow a < b \land c < d \land b \geq c \land d \geq a)$

The Auxiliary Functions Required by the dss Machine

Rs: M → S; a selector of the active plans.
Rs ( $\langle m_{n}, m_{0} \rangle$ ) := First(m $_{n}$ )

Ra: P(A) → P(A); a selector of the manipulations applicable to a plan.
Ra (manipulations) := manipulations (we take identity function)
We will define now the function T by means of two equations:
T: S × A → S

"a plan is extended by an operation":
T (schedule(time, plan), operation(task, job, machine, begin, edn)) :=
schedule(time, Cons(operation(task, job, machine, begin, end), plan)).

"a scheduling time is move forward to a newtime": T (schedule (time, plan), move(newtime)) := schedule (newtime, plan)

Goal: $\mathbf{S} \times \mathbf{D} \rightarrow \{\text{true, false}\}$

Goal (schedule (time, plan), d) := Timelimit (time) $\vee$ All\_tasks scheduled(plan, d)

Timelimit: $\mathbf{N}\to \{\mathrm{true},\mathrm{false}\}$

Timelimit (time):="time is greater than a planning horizon".

All\_task\_scheduled(plan, d) := "all tasks as defined by the Is\_task predicate have been scheduled".

We define now the memory update function Rm:

Rm: $\mathbf{M} \times \mathbf{S}^{*} \rightarrow \mathbf{M}$

$\mathbf{Rm}(\langle \mathbf{m}_{\mathfrak{n}},\mathfrak{m}_{0}\rangle ,$ extensions):= $\langle \text{Order}(\text{Append}(\text{extensions}, \text{Rest}(\mathfrak{m}_n))), \text{Cons}(\text{First}(\mathfrak{m}_n), \mathfrak{m}_0) \rangle$ .

where

Order: $\mathbf{S}^{*}\rightarrow \bar{\mathbf{S}}^{*}$

Order (schedules) := "an ordered permutation of schedules".

An ordering relation has to be defined on schedules. We can express here our preferences with respect to schedules. As a result of our definitions we get the best-first search strategy for the job-shop scheduler.

Rr: $\mathbf{M}\rightarrow \mathbf{S}$ ; the recovery function

$\mathrm{Rr}(\langle\mathrm{m}_{n},\mathrm{m}_{0}\rangle)=“selects a plan from either m_{n} or m_{0} in case no plan satisfying Goal predicate as found.$

$\mathrm{Rr}(\langle\mathrm{m}_{n},\mathrm{m}_{0}\rangle):=\mathrm{nil}$ (we do not want any partial plan)

## 7. Conclusions

We have given a specification of the components of an abstract dss machine. We hope that the specification shows in a clear way the structure of the system with respect to the target system, the graph of plans and the search strategies. It seems possible to begin the construction of the dss by neglecting the problems of selection of search strategies and choosing a standard one, and emphasizing the correct definition of the target system together with the graph of plans. Later the efficiency of the dss can be tuned by supplying suitable selection functions and thus creating a more refined search strategy without the need to modify the whole system.

## References

[Be83] Bennet, J.L. "Building decision support-systems", Reading, Mass., Addison-Wesley, 1983.

[Ga86] Gallier Jean H. "Logic for Computer Science", Harper & Row Publishers, 1986.

[Gl84] Glaser H., Hankin C., Till D. "Principles of Functional Programming", Prentice-Hall, 1984.

[He86] van Hee K., Huitink B., Leegwater D.K. "Portplan, decision support system for port terminals", European Journal of Operations Research, 1987.

[Ko79] Kowalski R. "Logic for Problem Solving", North-Holland, 1979.

[L184] Lloyd J.W. "Foundations of Logic Programming", Springer-Verlag, 1984.

[Ni82] Nilsson N. "Principles of Artificial Intelligence", Springer-Verlag, 1982. [Om81] Omni Linear Programming System, User Reference Manual, Haverley Systems Inc., Nov. 1981.

[Pe84] Pearl J. "Heuristics: intelligent search strategies for computer problem solving", Addison-Wesley, 1984.

[So84] Sowa J.F. "Conceptual structures: information processing in mind and machine", Addison-Wesley, 1984.
