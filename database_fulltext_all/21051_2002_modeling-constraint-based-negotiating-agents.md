---
otero_id: 21051
otero_key: "QQR2CKQE"
title: "Modeling constraint-based negotiating agents"
authors: "Huaiqing Wang; Stephen Liao; Lejian Liao"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00138-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Modeling constraint-based negotiating agents

Huaiqing Wang\*, Stephen Liao, Lejian Liao

Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong, China

## Abstract

Most existing decision support systems (DSSs) are hard to fit satisfactorily into emerging working practices or organizational environments. Decision-making is becoming more pluralistic and less hierarchical, determined not so much by position in the corporate hierarchy but much by the argumentative and evidential value. Such decision-making can only be supported by those DSSs with negotiation support facilities. Intelligent negotiation agents can be used to model many decisionmaking negotiation tasks. Such negotiation agents are able to interact and negotiate with users and with each other. In addition, the newly emerging constraint agent technology provides a promising solution for such negotiation agents. In this paper, we present a model by applying constraint negotiation agents for DSSs. An object-oriented constraint language for modeling constraint agents is defined. Within our model, constraint DSS agents are able to reason cooperatively with users or with other agents. Negotiation among agents and users is modeled as a process of interactive constraint satisfaction. Efficient algorithms for the implementation of negotiation-oriented constraint satisfaction are also presented. As manpower costs become more and more expensive and as the negotiation workload increases, the future DSSs will play more important roles in the negotiation process. It is expected that our work will contribute to the future DSS design and development. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Decision support systems; Constraints; Intelligent agents; Negotiation; Interactive constraint satisfaction

## 1. Introduction

Most of the existing decision support systems (DSSs) do not fit satisfactorily into emerging working practices or organizational environments. Decisionmaking is becoming more pluralistic and less hierarchical, determined not so much by the position in the corporate hierarchy but much by the argumentative and evidential value. Such ephemeral status can only be captured by systems, which mediate and transcribe argumentation and the shifting contracts, which are continually being created as work tasks progress and vary through time [21]. It is clear that decision support systems with the negotiation support facility will be a key issue in the next decade.

Over the last few years, there has been increasing interest in coupling intelligent agents with decision support systems. The potential contributions of intelligent agents to decision support systems (DSSs) will be enormous [30]. Constraint technology and agent technology are two disciplines which can produce commercial benefits in a wide range of industrial applications. Constraint agent technology as a combination of both has emerged as a promising research field. Constraint languages are powerful tools to support the development of constraint agent systems. They provide necessary facilities of representation, reasoning and maintenance of constraint-based knowledge bases. In a constraint programming position paper for the ACM Workshop on Strategic Directions in Computing Research, Freuder indicated the value of constraint programming to agent design. He especially pointed out that constraint satisfaction is a natural medium for negotiation among network agents. Constraint agent technology is a powerful tool for DSS because its facilities are very important for DSS design. One of the most important aspects of future DSS is to model the decision-making process based on a given decision problem. Constraint agent technology has been shown to be a successful modeling tool in widespread DSS applications. It is common in operation research to model decision problems as equations and equalities, which are special forms of numerical constraints. Symbolic constraints are also adopted when qualitative models are used. Constraint languages make it easy to build and manage such constraint-based models. In addition, another important aspect of DSS is the interaction between the users and the DSS system to support the decision-making process. To achieve better performance, the interface of a DSS should be more cooperative in interacting with users. Agent programming is a good technology for such intelligent interaction between a DSS and DSS users.

Not only can a DSS take advantage of both constraint technology and agent technology, but also the combination of both technologies will bring further benefits of DSSs. In fact, smart interactive decisionmaking in DSS can be implemented through constraint-based negotiation between a software agent in the DSS and the DSS users. Based on this point of view, we will investigate the implementation issue of agent-based negotiation through interactive constraint satisfaction, as well as a model of the negotiating agents with the help from an object-oriented constraint language.

Negotiation models have been attracted much attention from the DSS research community. Norita [16] presented a model for representing social conflict under disagreements, with the view that the resolution of such disagreements often affects the resolution of the conflict itself. In Ref. [12], a negotiation model has been developed to attempt to provide a framework for understanding the context of inter-organizational negotiations by identifying and illuminating the factors that influence the outcome of interactions in various long-term supplier relationships. Sprinkle et al. [23] described an agent negotiation model and presented an implementation. In Ref. [29], a multi-step negotiation mechanism for multi-agent systems has been presented. This mechanism uses marginal utility gain and marginal utility cost to structure the negotiation process.

Furthermore, constraint agent technology has stemmed from two AI sub-fields, constraint technology and agent technology, which are the most promising research areas for industrial applications. Constraint technology has been successfully applied in various research and application areas for a long time. The major concern of constraint technology has been focused on two issues: constraint satisfaction search and constraint languages. Constraint-based interaction has been investigated mainly in some engineering fields such as intelligent graphic interfaces and industrial design and scheduling [3,5,14,17]. With the emergence of agent-based methodology, numerous agent systems with constraint-based representation are designed, especially in the area of scheduling and design [10,19,22,27]. In these areas, the constraints are a natural means to specify the requirements of the tasks. The satisfaction of the requirements involves multiple participants of software or human agents. Negotiation is necessary to balance the satisfaction among different agents. The strategies of such negotiation are usually domain-specific and different from one another.

In addition to traditional constraint applications such as scheduling, constraint agent technology has also found its way in some hot application areas. For instance, a constraint-based information searching agent has been designed in Europe to aid scientists in finding relevant literatures across distributed electronic libraries. A representation of constraints in an objectoriented style is exploited to express the requirements. The main concern of such work is the reuse of search results among different searching agents. Another interesting application of constraint agent technology is to support the quality of services in multi-media communication across the Internet [8,9]. In this system, a client applies for communication resources with a given level of the service. The requirements are specified with constraints and are submitted to the network resource manager. Negotiation takes place when the requirements cannot be satisfied and an alternative solution is to be provided. The negotiation process in such systems is in line with our framework in the sense of negotiation as interactive constraint satisfaction. Actually, our framework is very suitable to serviceoriented negotiation in which a service agent and a customer agent can cooperate to find a near-optimal solution to the requirements. However, our framework is different from many negotiation approaches in electronic commerce [25,28]. The latter are competitive and market-oriented, whereas our framework is cooperative. Our framework is also different from negotiation supporting systems [6] which are designed to aid users in making negotiation decisions. Negotiation in our framework is a method of agent-oriented interactive problem solving.

Negotiation has been the main concern in the research on multi-agent systems. Various methods and techniques have been proposed for different tasks [15,31,32]. Although some difficult tasks need sophisticated negotiation methods, interactive constraint satisfaction is sufficient for most of DSS tasks. Sophisticated negotiation strategies can be programmed with no great effort with flexible constraint programming. The goal of this paper is twofold. The first is to provide a general and domain-independent framework with which a wide range of DSS negotiating agents can be modeled. The second is to show that negotiation can be performed in an efficient way in the constraint-based framework. We have also proposed to use generic local search to achieve high efficiency.

As a constraint-based agent modeling language, CLAM has some agent-oriented features which are different from the mainstream constraint programming languages such as constraint logic programming languages [4]. Constraint logic programming languages are purely declarative. This feature is elegant for knowledge-based programming, but it makes the modeling reactive behaviors of agents inconvenient. In addition, the main strategy of the search in constraint logic programming is backtracking plus constraint propagation. Such searching strategy is not suitable for fast constraint satisfaction with soft constraints and objective functions, which are widely used in modeling constraint agents.

There are also constraint programming languages which are not logic-based such as OZ [20]. OZ is an object-oriented concurrent constraint programming language for general purposes. Our framework is similar to OZ in that both systems support the objectoriented feature and imperative programming within the constraint-based declarative framework. To model the negotiation tasks, heuristic components such as soft constraints, objective functions and generic local search are introduced in our framework. Such heuristic features make our framework less rigorous but more flexible.

## 2. Background

A typical feature of DSS, which distinguishes it from fully automated systems, is its interaction with users. In the sense of such interaction, a DSS can be viewed as a cooperative agent system in which both the DSS program and the users are participating agents. Such an agent-based point of view of DSSs can enhance the system with more intelligent features when the mechanism of the interaction with the users is designed. Although there has been no standard definition of the agents among the research community, a number of basic characteristics of agents as a computational entity have been identified [26].

An agent is autonomous in the sense that it has its own computational process, and it is able to make decisions and take action on its own.

It interacts with the environment by exchanging information with human users or other agents. Furthermore, it typically has some social ability such as coordination, cooperation, negotiation and argumentation.

It is active or reactive with regard to events in the environment or its own process. Furthermore, it is typically adaptive to events in improving its behaviors.

Although agent systems do not necessarily satisfy all these properties, generally, they satisfy one or more of them. Agent systems in different areas embody these properties to different degrees. For DSS agents that provide services to users and try to satisfy the user’s requirements, interaction, cooperation and negotiation are very important. Using a DSS, the user tells the DSS agent about his/her requirements and inputs data. The DSS agent seeks one or more solution(s) and presents it to the user for his/her selection or confirmation. Due to the limitation of information and resource availability, the user’s requirements may not be satisfied, and the solution presented may not be what the user wants. In such case, the user may simply reject the presented solution and the DSS agent turns to seek other solutions. For closer cooperation, the user can be allowed to dynamically change his preferences to the problem-solving state by revising the intermediate solutions presented. The DSS agent and the user thus can negotiate towards a problem-solving state which is achievable for the DSS agent and acceptable to the user. The process between a DSS agent and a user can be sketched as follows.

1. Accept user’s requirements.

2. Find a solution to the requirements.

3. Inquiry with the user regarding acceptance of (or revision to, if the user is not satisfied with the solution) the solution.

4. Take the revision as input and restart to find a new solution.

5. Repeat 3 and 4 until a solution satisfactory to the user is found.

## 2.1. Negotiation as interactive constraint satisfaction

From the process described above, on the one hand, it is a typical process of interactive constraint satisfaction. On the other hand, it can also be viewed as a process of negotiation between a DSS agent and a user. In many cases, requirements can be naturally represented as constraints and objective functions of a set of variables. In addition to the constraints about the user’s requirements, an answer to the user may also have to satisfy the constraints from the DSS system, such as constraints on the resources of the systems, and the constraints about the relations among the agents, etc. The problem of answering the user’s requirements with these system constraints becomes a constraint satisfaction and optimization problem. In a DSS, user requirements may be allowed to be prioritized to achieve flexibility. The constraints to model the requirements thus should also have different priorities. The most important constraints are the hard constraints that must be satisfied without any relaxation. Any violation of a hard constraint by an assignment will make the assignment unacceptable as a solution. Constraints other than hard constraints are soft constraints, which can be relaxed if the requirement is over-constrained. The violation of a soft constraint makes the values assigned to the variable less preferred as a solution but does not necessarily reject them. Soft constraints can be prioritized. When inconsistency occurs among a set of soft constraints, less important constraints can be relaxed while the most important ones are retained. A simple approach to prioritize soft constraints is to associate each soft constraint with a positive number representing its level of importance. The lesser the number, the more important is the constraint. Thus, the problem can be formulated in multi-objective programming as follows.

## Given

a set of hard constraints H,

a set of soft constraints S, and

a set of objective functions G

Find a solution such that

all the constraints in H are satisfied, the constraints in S are maximally satisfied, and the sum of objective functions in G is maximal.

## 2.2. Constraint-based modeling

For simple tasks, a simple representation, including a collection of variables and constraints and objective functions on the variables, is enough for such modeling. For more complex tasks, however, such simple representation is not enough because it can only describe the domain tasks at the proposition level. It lacks the ability for abstraction that is essential for modeling complex tasks. To facilitate the maintenance of knowledge for modeling negotiating agents, more expressive languages are necessary. There are a number of constraint languages (Ref. [4], OZ) which provide expressive representation of constraints. Constraint logic programming languages provide elegant declarative representation by the combination of logic programming and constraint satisfaction techniques. However, the pure declarative style of such languages makes them inconvenient to represent actions and state change events. They are not sufficient for modeling active and reactive behaviors, which are very common in DSSs. In addition, these languages commonly use backtracking as their search strategy, which is very inefficient. Because the computation of soft constraints and negotiation is generally heuristic in nature, a constraint language with heuristic components is needed.

In this paper, we present a simple language, Constraint Language for Agent Modeling (CLAM), for modeling agent problem solving and negotiation with constraints. A homogenous representation is assumed between the negotiation agents. If the agents use different representation schemes internally, they should translate their internal schemes to CLAM for communication and negotiation.

## 3. An object-oriented constraint language for agent modeling

CLAM is an object-oriented constraint rule language with the style of concurrent constraint programming. It means that it allows blocking control over the constraint execution. A body of a constraint is executed only if all the required information is available. Otherwise, it is suspended until the information is available. Another feature of CLAM is that it allows both declarative and imperative representations. Such combination is important for agent modeling because an agent should have the abilities of both reasoning with knowledge, computing with processes and dynamically coping with changing environments. The use of conventional programming constructs makes the programs more friendly and easy to learn for system builders who are familiar with conventional programming languages such as C/C++ and Java. The integration of declarative and imperative representations is achieved by distinguishing between declarative components and imperative components in the language. The declarative components are made up of logical variables and constraints between the variables, which are transformed to constraint networks in a dynamic execution. A logic variable can be bound with either a value or a range of values. Once a logical variable is bound with a value in a context, the value will remain unchanged unless the context is changed. The imperative components of the language are made up of imperative variables and imperative statements. A transient variable always holds a value, but the value can be changed from time to time. Imperative statements include sequential constructs, iterative constructs and assignment statements for transient variables. While the execution of a declarative statement constrains the declarative environments of constraint networks, the execution of an imperative statement makes an immediate change to the current state of transient variables. Both the declarative statements and the imperative statements are combined within a rule and are encapsulated in an object. Such combination of declarative representation and imperative representation provides great flexibility for modeling agents.

The syntax of CLAM is defined as follows.

```txt
definition_list := definition|definition_list definition
definition := enum_definition|class_definition |rule_definition
enum_definition := 'ENUM' enum_name type_spec enum_spec
enumspec:='{'const_list'}'
class_definition:= 'CLASS' class_name [':' class_name] '{'member_decl';'}']
member_decl := var_decl|method_decl;
var_decl:= type_spec variable;
method_decl:= method_type method_name {prototype}
method_type := 'FUNCTION'|'NEW'|'RELATION'|'ACTION'
prototype := '('typeList')
rule_definition:= class_name‘::’ method_name
arg_list condition rule_body
condition := statement
rulebody := {'{'statement';'} '}
```

## 3.1. Objects and constraints

An object encapsulates a set of attributes, constraints and methods. An attribute is a variable, either a logical variable or a transient variable, that is local to the object. An attribute, which is a logical variable, is called a port. A port is public and can be queried and constrained with an external message. An object can have a set of constraints among its ports called local constraints of the object. The local constraints of an object are specified in the method constraints of the object. Whenever a port of an object is added to the constraint networks as a part of the environment, the local constraints of the object are correspondingly added to the constraint networks as well as a part of the environment.

FUNCTION method(class<sub>1</sub>, . . ., class<sub>n</sub>); or

As an example, in an electricity supplying management system discussed in Section 4, an electrical branch is modeled as a kind of two-terminal device such as a resistor or a switch which obeys some physical laws. The following are some classes and constraints for such modeling.

```txt
CLASS terminal {
    Float $voltage;
    float $current;
    FUNCTION connect_to(CLASS terminal);
}
CLASS device_2tm {
    Terminal terminal1;
    Terminal terminal2;
    NEW device2(terminal, terminal);
}
CLASS resistor:device_2tm {
    INT resistance;
    NEW resistor(INT, terminal, terminal);
}
ENUM boolean SYMBOL {%open, %close}
CLASS switch:device_2tm
{
    ENUM boolean $state;
    NEW switch(terminal, terminal);
    ACTION set_state(ENUM boolean);
}
resistor::constraints()
{
    sum(terminal2.$voltage, terminal1.$voltage, INT $Voltdiff);
    times($Voltdiff, resistance, terminal1.$current);
}
switch::constraints()
{
    IF($state = %open)
    equal(terminal1.$current, 0);
    ELSE
    terminal1.connectedto(terminal2);
}
```

In the example above, the physical state is modeled with ports such as \$voltage, \$current in class terminal and \$state in class switch because they are parts of the constraint network in execution. Physical parameters are modeled as transient variables such as resistance. The behaviors of devices resistor and switch are specified as local constraints of the objects.

In addition to local constraints, constraints can also appear in the body of other methods. Soft constraints are represented as:

```sql
SOFT < constraint >, or
SOFT < n > < constraint >
```

where < constraint > is a constraint, and < n> is a positive integer representing its priority of importance. The less the integer, the more important the constraint is. When n is not specified as in the first case above, the default is 1. The representation is similar to the system of constraint hierarchies [29]. Because our framework both has soft constraints and objective functions, soft constraints are transformed into objective functions in the implementation. The details will be discussed in Section 5.

## 3.2. Methods

The methods of an object can be at three levels. The top level is the action level which defines the agent actions with objects. A method at this level is declared as the following.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
ACTION method(class $_{1}$ , ..., class $_{n}$ );
</div>

The middle level is the belief level in which a method represents a set of facts and rules representing the belief of the agent about the world. A method at this level corresponds to a predicate that is local to the object. A rule of the method takes the assertion about the predicate as the conclusion part. A reduction to the call of such a method to a rule is actually a hypothetical backchaining inference step. A method at this level is declared as the following.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
BELIEF method(class $_{1}$ , ..., class $_{n}$ );
</div>

The lowest level, i.e. the base level, is the function level which defines the basic functions and relations for the object. A method at this level can be determined in that any call to the method matches one and only one rule. A method at this level is declared as:

ACTION method(class<sub>1</sub>, . . ., class<sub>n</sub>); or NEW class(class<sub>1</sub>, . . ., class<sub>n</sub>;).

There are several advantages to represent methods into different levels. One advantage is to enhance the clarity of the model. A more important advantage is to enhance the efficiency of program execution with the strategy of the least commitment. A lower level method cannot call a higher level method in the body of the rule. Hypothetical reductions are only made at the belief level. Thus, backtracking only has to focus on the choice points at this level. The function level reduction corresponds to the primary functional computation and constraint propagation. Among a set of method calls to be executed, those that are at the function level and match exactly one rule are executed firstly so that more information can be available before a choice is selected. In implementation, methods at the function level are executed immediately when they are encountered, whereas methods at the belief level or at the action level are pushed on to a stack for scheduling after all the necessary function level methods have been executed.

## 3.3. Rules

User-defined methods are implemented with a set of concurrent constraint rules. A concurrent constraint rule is of the following form:

$$
\begin{array}{l} \text {Method - name (Arg_{1} ,\ldots,Arg_{n})} \\ \text {[ASK - condition]} \\ \text {[statements]} \end{array}
$$

Both ASK-condition and statements are optional. A fact is a special form of a rule in which all the arguments are constant and both the ASK-condition part and statements part are null.

Arg<sub>i</sub> is either a variable [ < class-name >] < variable-name > or a constant. < variable-name > is a string with a capital letter (for transient variable) or a \$ (for logical variable). Concurrent control is implemented by treating transient variables and logical variables in different ways when they match against the parameters in a method call. A transient variable can only accept a value of the same class as the input. If a parameter corresponding to the variable is an unbound logical variable, the reduction of the user-defined method is suspended until the logical variable is instantiated with a value.

After the parameters of a method call successfully match the argument list of a rule, the condition in the ASK part is evaluated. If the condition is evaluated to be true and the rule is ranked highest among the other alternative rules, the statements in the body of the rule will be executed.

Since there can be multiple rules matching a method at the belief level, the execution is an indeterminate process and exploration with different rules is possible. In order to simplify such complex processes, the search in CLAM is divided into two phases such that the advantage of backtracking for complex representations and the advantage of local search algorithms for fast opportunistic search can be combined. The first phase is method reduction in which all the method calls are reduced. The result of this phase is either a solution or a set of constraints and objective functions generated in the reductions. For choosing a rule for a method call at the belief level, the heuristic evaluation based on the unification and the computation of the ASK-condition is conducted in order to evaluate different candidate rules. The rule considered to bring the maximal objective function value will be chosen. When a consistency or a dead end is encountered, backtracking for a belief level method will be called by retracting all the binding constraints to the environment.

## 4. Formalization of the modeling language

For efficiency reasons, the execution of a CLAM program is divided into two stages. In the first stage, CLAM reduces all the method calls to primary constraints. In the second stage, CLAM solves the resulting constraints through constraint satisfaction search. In the first stage, the program execution involves processing declarative statements and imperative statements. To give a more clear view of the CLAM program execution process, we give a brief description of the operation semantics for the first stage execution that can be described in terms of a series of reductions of CLAM method calls.

Definition. A configuration is a tuple: (S, G, C, s) where S is a sequence of statements representing the flow of the program statement, and G is a set of belief level method calls representing the triggered belief level method calls. s is a state of transient variables. $( C , s )$ is called the execution environment in which a statement is executed. The semantic of a statement q in the program environment $( C , s )$ is denoted as $q | ( C ,$ s). The semantics of CLAM is defined as following transformation rules:

 For a primary constraint c, the execution of c will join c constraint environment C.

$$
\begin{array}{l} (\{c; S \}, G, C, s) \\ = > (S, G, C \cup \{c \mid (C, s) \}, s) \end{array}
$$

 For a function level method call $\boldsymbol { a } \cdot \boldsymbol { m } ( t _ { 1 } , . . . ,$ $t _ { n } ) ,$ its execution will be a reduction of the call into the body of a rule $m ( u _ { 1 } , . . . . , u _ { n } )$ of a class of instance a: $\mathrm { I F } \ : c \ : \{ S _ { 1 } \}$ , along with the matching binding:

$$
\begin{array}{c} \left(\left\{a \cdot m (t _ {1}, \dots , t _ {n}); S \right\}, G, C, s\right) \\ = > \left(\left\{S _ {1}; S \right\}, G, C ^ {\prime}, s\right) \end{array}
$$

where $\{ S _ { 1 } ; ~ S \}$ is the result of appending sequence $S _ { 1 }$ to the top of $S ; ~ C ^ { \prime } =$ $C \cup \mathrm { L C } ( a ) \cup \{ u _ { 1 } = t _ { 1 } , . . . , u _ { n } = t _ { n } \}$ ; LC(a) is the set of local constraints of object a; and $c | ( C ^ { \prime } \mathrm { ~ , ~ } s )$ must be evaluated to be true. For a belief level method call $^ { g , }$ the immediate action of $g$ will put it into G:

$$
(\{g; S \}, G, C, s) = > (S, G \cup \{g \}, C, s)
$$

Belief level goal scheduled execution. Let $g = b { \cdot } m ( t _ { 1 } , . . . ,  t _ { n } )$ be a belief level method call which is scheduled for execution with predefined strategy. The execution of the method call will be its reduction into the body of a rule of the class of the instance b: $m ( u _ { 1 } , \ldots , u _ { n } ) \mathrm { ~ I F ~ } c \{ S \}$ , along with the matching binding:

$$
(\{\}, G \cup \{g \}, C, s) = > (S, G, C ^ {\prime}, s)
$$

where $C ^ { \prime } = C \cup \mathrm { L C } ( b ) \cup \{ u _ { 1 } = t _ { 1 } , . . . , u _ { n } = t _ { n } \}$ ; LC(b) is the set of local constraints of object $b ;$ and $c | ( C ^ { \prime } \cup s )$ must be evaluated to be true. This rule means that when constraints at all the function levels have been executed, one of the belief level goals is scheduled for execution.

 Let $g$ be a primary action, $g | ( C , s )$ changes s to $s ^ { \prime }$ . The execution of $g$ will be the change of the state:

$$
\left(\{g; S \}, G, C, s\right) = > (S, G, C, s ^ {\prime}).
$$

After the first stage execution, a constraint satisfaction search will be conducted to find a solution, which will be discussed in the next section.

## 5. Negotiation via interactive constraint search

After all the method calls have been reduced in the execution of a CLAM program, either a solution is found or a set of constraints and objective functions are generated as an answer. If the answer is a solution, the solution is submitted to the user for confirmation. If the solution cannot be accepted by the user, the system continues the search for other solutions. If the answer is a set of constraints and objective functions, the system will conduct constraint satisfaction search with a search strategy in order to get a solution.

5.1. Transforming soft constraints into objective functions

The satisfaction of a set of soft constraints can be measured in different ways. To make the problem simpler, prioritized soft constraints are interpreted in our framework as objective functions. The satisfaction of the constraint will bring a gain and will be rewarded with a positive utility value, while a violation of it will bring a loss and is punished with a negative utility value. The importance of a soft constraint can be interpreted as the difference between the rewarding value for the satisfaction of the constraint and the punishing value for the violation of the constraint. Therefore, a prioritized soft constraint can be translated into an objective function as:

$$
\operatorname{Obj} ^ {s} (x) = \left\{ \begin{array}{l} K / n, \text {   if   } s (x) \text {   is   true } \\ | - K / n, \text {   otherwise } \end{array} \right..
$$

With such translation, user requirements can be presented as a combination of a set of hard constraints and an objective function. The previous procedure for the interaction between the decision agent and the user can be implemented as a process of interactive constraint satisfaction and optimization. Generally, to find a solution that satisfies all the constraints is NP hard. Furthermore, to find the best solution for a constrained optimization requires the generation of all the feasible solutions. When the scale of a problem is large, the response from the decision agent to the user will be very slow because of the large amount of computation. It often needs to sacrifice the quality of the solution in exchange for a faster response. In our framework, a heuristic and cooperative approach is proposed. An approximate optimal solution is computed and then presented to the user for confirmation. The user can accept the solution, revise the solution or simply reject it. If the solution is accepted, the process ends successfully. If it is simply rejected, the search continues and only better solutions than the rejected one are considered as outputs. If the solution is revised by the user, the revised solution will be taken as a soft constraint to guide the search. Because a revised solution by the user reflects the user’s feedback to the solution, it is also called the adapted state. Previous procedure for the interaction between the decision agent and the user can be implemented as a process of interactive constraint satisfaction and optimization as follows.

Given a set H of hard constraints H and an objective function g:

```txt
Set Value = e
Initialize adapted_state
Repeat
    Find a solution that
    1. satisfies all the constraints, and
    2. is approximately optimal with respect to the objective function g and adapted state s.
    3. g(s) ≥ e
Output s to the user for confirmation
    If s is accepted by the user, then the process ends successfully.
    If s is simply rejected by the user,
    then set e = g(s) and continue the search process.
    If s is revised by the user,
    then
    set s as the new adapted state.
Until the search is exhaustive.
```

Although such a search process may also transverse the whole search space, it allows the user to get an approximate optimal solution without waiting until the whole process is completed. In many cases, a suboptimal solution is enough.

## 5.2. A backtracking algorithm for heuristic constraint optimization

There have been different search algorithms for solving constraint satisfaction and optimization problem. Generally, to find a solution that satisfies all the constraints is NP hard. Furthermore, to find the best solution for a constrained optimization requires the generation of all the feasible solutions. It often needs to sacrifice the quality of the solution in exchange for a faster performance.

The algorithms for constraint satisfaction and optimization can be divided into two categories: the systematic search and the opportunistic search. Systematic search techniques include generating, and testing and backtracking search. Generating and testing generate all the possibilities of the variable value combinations and check their consistency and optimality. It is the most straightforward and inefficient way to solve constraint satisfaction and optimization problems. Backtracking search is commonly used in various AI systems especially constraint satisfaction systems. The major advantage of backtracking search is that it is systematic which guarantees to find a solution if any. Another advantage is that it can be integrated into a wide range of representations such as rules and logical clauses. This advantage makes it possible to support reasoning with abstract representations. An adaptive basic backtracking algorithm is sketched as follows.

Given a set of hard constraints $H ,$ and an objective function g, and an adapted state s:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Repeat
Forward:
 $i=i+1$ 
If all the variables are instantiated
    Return the solution
    Choose an uninstantiated variable v, and a value a from the domain of v, followed by constraint propagation, such that
    1.  $E+\{v=a\}$  satisfy all the constraints
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
2.  $E + \{v = a\}$  has the largest heuristic value
If no such a in the domain of v satisfies condition 1, do backtrack
Else do forward
Backtrack:
i = i - 1
If ( $i \leq 0$ )
Return failure-message
Retract the binding value of  $v_{i}$ 
Choose an untried value a for  $v_{i}$ , such that
1.  $E + \{v = a\}$  satisfy all the constraints
2.  $E + \{v = a\}$  has the largest heuristic value
If no such value, do backtrack
Else do forward
</div>

In backtracking algorithms for constraint satisfaction search, there are different strategies for the selection of a variable and the value of the variable. The rule to select the next instantiated variable is to select a variable with only one choice of values. A more general heuristic is to select the variable with the minimal number of choices [13]. Such strategy aims at finding a solution in a fast way. For the problem of constraint optimization, a straightforward approach is to select the combination of a variable and a value which maximizes the total value of the objective functions. A problem for such approach is that the total value of the objective functions in general cannot be completely determined before all the variables are instantiated. To overcome this difficulty, there are several strategies to evaluate the total value of the objective functions described as follows.

## 5.2.1. Known objective functions

For this strategy, among the possible combinations of uninstantiated variables, each choice is evaluated with the sum of those objective functions in which all the arguments are known. Unless there is an uninstantiated variable which has only one choice, this strategy selects the choice with the largest known objective function value. For example, two variables x IN {1, 3} and $y \operatorname { I N } \{ 3 , 4 \}$ , with constraint $x + y < 7$ , and objective functions $g _ { 1 } = x$ and $g _ { 2 } = y .$ . Among the choices $\{ x = 1$ $x = 3 , y = 3 , y = 4 \} , y = 4$ is chosen according to this strategy because it has the largest value of 4 of the known objective functions. From this example, it can be seen that the strategy may be misleading sometimes because $y = 4$ is not the best choice at this point. The best solution to this problem is actually $\{ x = 3 , y = 3 \}$

## 5.2.2. Setting unknown objective functions heuristically

Another strategy is to set the unknown objective functions heuristically. One method is to set the values of unknown variables in the objective functions to those in the adapted state. Since an adapted state represents a state that the user prefers, the search process tends to reach this state. The choice guided by the adapted state is plausible. Another method to set the value of an unknown objective function $g$ is to set it to the average value of the g values for all the possible choices of the unknown variables in $g .$ For the above example, when the choice for x is evaluated, $g _ { 2 }$ is taken to be $( 3 + 4 ) / 2 = 3 . 5 ;$ when choices for y are evaluated, $g _ { 1 }$ is taken to be $( 1 + 3 ) / 2 = 2$ . Thus, the heuristic values for each choice in $\{ x = 1 , x = 3 , y = 3 , y = 4 \}$ are listed below.

$$
\begin{array}{l} x = 1: g _ {1} + g _ {2} = 1 + 3. 5 = 4. 5 \\ x = 3: g _ {1} + g _ {2} = 3 + 3. 5 = 6. 5 \\ y = 3: g _ {1} + g _ {2} = 2 + 3 = 5 \\ y = 4: g _ {1} + g _ {2} = 3 + 3 = 6. \end{array}
$$

The best choice at this point is thus $x = 3$ , which coincides with the best solution $\{ x = 3 , y = 3 \}$

## 5.2.3. The most important choice first

Firstly, we define the importance measurement of a combination $\nu = a$ as:

$$
\begin{array}{l} \text { Importance } (V, a) = (\text { the   total   value   of   known } \\ \text { objective   functions   for   v   =   a }) \\ \quad - \max \{\text { the   total   value   of } \\ \text { known   objective   function   for } \\ \quad v = b \text { for   any   b   in   the   of } \\ \quad \text { domain   v   and   a!   =   b } \}. \end{array}
$$

The intuitive meaning is that a combination $\nu = a$ is important if it is much better than its alternatives. The strategy is then described as follows.

1. If a variable v has a value a as the only choice, choose variable v and value a as the next instantiation. Otherwise,

2. Choose a variable v and a value a from the domain of v such that Importance $( V , a )$ is maximal.

When applied to the above example given choices $\{ x = 1 , x = 3 , y = 3 , y = 4 \}$ , we have:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Importance $(x,1) = 1 - 3 = -2$   
Importance $(x,3) = 3 - 1 = 2,$   
Importance $(y,3) = 3 - 4 = -1$ , and   
Importance $(y,4) = 4 - 3 = -1$
</div>

Thus, $x = 3$ is the best choice at this point, which coincides with the best solution.

The advantage of a backtracking algorithm is that it is systematic and can guarantee to find a consistent solution given enough time. However, the backtracking search is slow due to the its several drawbacks. One is thrashing, i.e. repeated failures due to the same reason. Thrashing occurs because the standard backtracking algorithm does not identify the real reason of the conflict, i.e. the conflicting variables. Therefore, the search in different parts of the space keeps failing for the same reason. Thrashing can be avoided by intelligent backtracking and constraint propagation. However, they also increase the costs of time and space.

## 5.3. Repair-based local search

Complementary to systematic search, opportunistic search, such as repair-based local search, genetic algorithms and neural networks, is incomplete but much faster in finding a solution. Such search methods are widely used in constraint optimization problems. CLAM adopts the local search [1,18] because its state-based feature is very suitable for the negotiation process in which the agent state evolves as the agent exchanges with the environment.

In general, a local search algorithm starts from an initial state of variable values and repeatedly and gradually changes the state to achieve a desirable one. The desirability of a state is evaluated with an evaluation function, and the changes are limited within the neighboring sates of the current state and are in the direction of maximally increasing the evaluation function unless a local optimum is reached. A neighboring state of s is a state which can be achieved from s by changing the value(s) of one or limited number of variable(s). For constraint optimization problems, the evaluation function is composed of two parts: a penalty function for the violation of the constraints and the sum of objective functions.

$$
E (s) = - p (s) + \sum g _ {i} (s)
$$

In the formula, $p ( s ) = c { \cdot } \nu \left( s \right)$ is the penalty function, $\nu \left( s \right)$ is the number of constraints violated by $s , g _ { i } ( s )$ is the value of the objective function $g _ { i }$ at $s , \ c$ is a coefficient such that $p ( s ) \gg \sum g _ { i } ( s )$ . It means that the search is firstly directed by the goal of satisfying all the constraints. A state is acceptable as a solution only if the constraint violation decreases to zero and the optimization reaches a large enough local optimum at this state. A negotiation process based on repair-based local search is sketched as follows.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Set Value = b
S = a random initial state
Repeat
    Let  $s'$  be a neighboring state of s such that  $E(s')$  is the largest among the evaluation function values of all the neighboring state of s.
    If  $E(s') \geq E(s)$ ,
    then  $s = s'$ , continue the loop
    If  $p(s) &lt; 0$  or  $E(s) &lt; b$ 
    then set s = a randomly generated state,
    continue the loop
    output s to the user for confirmation
    If s is accepted by the user
    then the process ends successfully.
    set  $b = \mathrm{E}(s)$ 
    If s is simply rejected by the user
    then set s = a randomly generated state,
    continue the loop
    If s is revised by the user to  $s'$ 
    then set  $s = s'$ , continue the loop
Until the time runs out
</div>

Two points should be addressed regarding the algorithm. Firstly, the adapted state is used as an input stimulus after the user restarts the search process when a local optimum is reached. This lets the search focus on what the user prefers. A problem for such approach is that as the search goes on, the state may gradually move away from the adapted state. This makes the algorithm less sensitive to user adaptation and less desirable for negotiation.

The second point to be addressed is the treatment of local optimums. When the search is trapped into an unsatisfactory local optimum, the algorithm jumps out by simply getting into another random state. In fact, the problem of jumping out of a local optimum trap is a big issue in the local search technology. There are numerous strategies to cope with this problem. One strategy is to make use of the evolutionary approach. A limited size k of cache is maintained which keeps the k top best locally optimal states. When a new unsatisfactory local optimum s is reached, the original range of neighbors is expanded to those states, which can be achieved through applying generic operators between s and one of the k states in the cache.

In order to make the local search algorithm more suitable for agent negotiation, we adopt such an evolutionary approach in a more negotiation-oriented way in the hope that the adapted state inputted from the user will have more significant influence on the search process. This can be achieved in the following way. Two caches are maintained: the local optimum cache and the adaptation cache. The local optimum cache keeps a number of top best local optimums, while the adaptation cache keeps a number of the most recently inputted adapted states. When a local optimum is unsatisfactory or rejected by the user, the generic operator crossover is applied between the two states, from the local optimum cache and the other either from the adaptation cache or from the local optimum. Given a state $s _ { \mathrm { o } }$ from the local optimum cache and a state $s _ { \mathrm { a } }$ from the adaptation cache or the local optimum cache, the crossover operator generates a set of offspring states. In each offspring state, some variables take the value of $\dot { } s _ { \mathrm { o } }$ and the others take the value of $\dot { s } _ { \mathrm { a } } .$ . A state s is chosen from among these offspring states so that the following fitting function is maximized:

$$
\begin{array}{l} F (s) = E (s), \text {   if   } s _ {\mathrm{a}} \text {   is   from   the   local   optimum   cache } \\ \quad = E (s) + 1 / t _ {\mathrm{a}} ^ {*} M (s, s _ {\mathrm{a}}), \text {   if   } s _ {\mathrm{a}} \text {   is   from } \\ \quad \text { the   adaptation   cache } \end{array}
$$

where $M ( s , s _ { \mathrm { a } } )$ is a function measuring the matching degree between s and $s _ { \mathrm { a } } ,$ and $t _ { \mathrm { a } }$ is a positive integer measuring the ‘age’ of $s _ { \mathrm { a } } .$ .

By putting adapted states into the generic operation, the search will be either in a direction that increases the satisfaction degree or reset to a state which is close to the recently adapted state. A generic version of the above negotiation-oriented local search algorithm is changed to the following evolutionary local search algorithm.

Set Value = b

$S = \mathbf { a }$ randomly initialized state

Cache={s}

Repeat

Let $s ^ { \prime }$ be a neighboring state of s such that $E ( s ^ { \prime } )$ is the largest among the evaluation function values of all the neighboring state of s. If $E ( s ^ { \prime } ) \geq E ( s )$

then set $s { = } s ^ { \prime }$ , continue the loop

Put s into optimum cache if it is better than some states in the cache or if the cache is not full.

$\mathrm { I f } p ( s ) < 0$ or $E ( s ) < b$

then set s as a state generated with the crossover operator, continue the loop

output s to the user for confirmation

If s is accepted by the user

then the process ends successfully.

set $b = E ( s )$

If s is simply rejected by the user

then set s as a state generated with the crossover operator, continue the loop

If s is revised by the user to $s ^ { \prime }$

then put s into the adaptation cache, set $s { = } s ^ { \prime } ,$ continue the loop

Until the time runs out

The local search has greater advantages for negotiation. Comparing with the backtracking algorithms, it is much faster to find a near-optimal solution for constraint optimization problems. This is important for the negotiation between the human user and a software agent because it is basically an interactive task which requires quick response. The weakness of the local search is that it may not achieve a global optimum even when given with a long-enough time. However, this is not a serious problem for most negotiation tasks since the objective functions transformed from soft constraints are subjective and heuristic in nature. The ultimate goal is to generate a solution that is good enough for the acceptance of the user.

## 6. Applications

Two application prototypes of our CLAM model will be presented in this section in order to demonstrate the usefulness and the power of our framework proposed in the last a few sections.

## 6.1. Power-distributed system application

This application involves scheduling switched capacitors in power distribution systems. The goal of the scheduling is to determine the daily schedule (‘ON’ or ‘OFF’) of each switched capacitor such that the expected constraints and objectives can be satisfied. The capacitors in the example can be switched through a remote-controlled switch rather than manual operation. It is beneficial for the feeder operator to have greater loss reduction and higher power quality. During a capacity switching, both transient over-voltage and high frequency noise can be produced. These transient over-voltage and high frequency noise, if enough, can damage sensitive power electronic devices or even electrical equipment. Furthermore, too frequent operation of the switches will deteriorate the lifetime of the switch equipment. Therefore, the problem has two conflicting goals. The first is to minimize the daily line loss of the feed and the second is to try to avoid switching operations unless they are necessary, and the second goal can be represented as soft constraints, which can directly be transformed into an objective function as the total number of switching operations during the day.

The problem is modeled with our framework as a multi-agent DSS system with two program agents, the line loss minimizer (LLM) and the switching operation minimizer (SOM), and a human agent, the human direct manager (HDM). The LLM takes the minimization of daily line loss as the main goal and the minimization of switching operation as an accidental one, whereas the SOM takes the minimization of switching operation as the main goal and the minimization of daily line loss as an accidental one. When an agent finds a solution pursuing its own goal, it reports its solution to the HDM. The HDM decides if the solution is acceptable or is not satisfied and sends its decision to the other agent as an adapted state. A compromise is then gradually reached between the two conflicting goals by exchanging solutions between the two program agents.

6.1.1. Modeling common knowledge about physical systems

In addition to their different goals, both LLM and SOM share knowledge about the electric power distribution systems, including the topological structure of the distribution networks and the physical state of the networks. In this example, only the linear topological structure is considered. CLAM provides a convenient means for the declarative modeling of such physical systems and problem-solving goals over the systems. For instance, a switch can be modeled as a CLAM object as follows.

```cpp
CLASS terminal {
    Float $voltage[24]; // for 24 hours in a day
    float $current[24];
    FUNCTION connect_to(CLASS terminal);
}
CLASS switch_capacitor
{
    ENUM boolean $state[24];
    Float capacity;
    Float $power[24];
    NEW switch(terminal, terminal);
    RELATION device_function();
    RELATION goal();
}
switch_capacitor::device_function() {
    FOR (i=0; i<24; i++) {
    IF ($state[i]=% open)
    $Power[i]=0;
    ELSE 
    $Power[i]=capacity;
    }
    switch_capacitor::constraints() {
    device_function();
    }
Another important class is the bus, which represents a node in the electric networks. A bus is modeled as a
```

Another important class is the bus, which represents a node in the electric networks. A bus is modeled as a subclass of the terminal:

```txt
CLASS bus : terminal {
    Int bus_No;
    Bus next_bus;
    Float resistance;
```

```perl
Float reactance;
Folat $real_power;
Float $reactive_power;
Float $reactive_power;
Float $real_load;
float $power_loss;
RELATION r_power_loss(INT);
RELATION equation1(INT);
RELATION equation2(INT);
RELATION equation3(INT);
RELATION limits(INT);
```

where attribute \$power<sub></sub>loss[i] is defined with the formula:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$(\text{$Real}_{\text{power}}[i]^2 + \text{$reactive}_{\text{power}}[i]^2)/\text{voltage}[i]^2$
</div>

\$equation1(INT), equation2(INT), equation3(INT) are equations based on physical laws. For instance, equation1 is defined as:

```rust
Bus::equation1(INT i) {
    Sum($real_power[i], next_bus.real_power[i], next_bus.real_load[i], power_loss[i]);
}
```

Method limits specify the values of maximal and minimal for \$voltage and \$current:

```cpp
bus::limits(INT i) {
    $voltages[i]>v_min;
    $voltages[i]>v_max;
    $current[i]<c_max;
}
```

These constraints are asserted into the knowledge state of the program by agents such as the local constraints of bus objects.

```rust
bus::constraints {
    FOR (i = 0; I < 24; i++) {
    Equation1(i);
    Equation2(i);
    Equation3(i);
    Limits(i);
}
```

## 6.1.2. Modeling agent goals

In addition to such common knowledge about the physical system, each program agent specifies its goal within its own body. To specify the goal of the agent SOM on switch<sub></sub>capacitor, a subclass switch<sub></sub>capacitor SOM of switch capacitor is defined within SOM. The goal is expressed as soft constraints representing SOM’s requirements that any switch capacitor should be kept unchanged as much as possible.

```txt
CLASSswitch_capacitor_SOM:switch_capacitor
{
    RELATION som_goal();
}
switch_capacitor_SOM::som_goal() {
    FOR (i=0; i<22; i++) {
    SOFT $state[i]=$state[i+1]; }
    //preferably no switching operation
}
```

Similarly, the goal of LLM can be specified within its body of the class bus<sub></sub>llm, and an objective over a bus object.

```txt
CLASS bus_llm: bus {
    RELATION llm_goal();
}
bus_llm::llm_goal() {
    FOR (i=0; i<23; i++) {
    MIN $power_loss[i]; // specify objective function
}
```

## 6.1.3. Negotiation among agents and users

Based on the above model, the process of negotiation among LLM, SOM and HDM is sketched as follows. Firstly, each program agent commits its own goal and common knowledge about the electric distribution to its computation process. In the first phase of the process, the object-oriented representation is reduced into a set of constraints and objective functions. Since all the methods can be found, such reductions are straightforward. No selection or backtracking is involved. In the second phase, one of the two program agents searches for a solution that satisfies all the constraints and nearly satisfies all the objective functions using the previously described local search program. This solution will be sent to the HDM for confirmation. The HDM decides if the solution is acceptable or not based on the search history from another program agent. If it is satisfied, the process ends. Otherwise, the other program agent will receive the most recent solution reported from the opposition agent as an adapted state. A compromise can be reached gradually between these two conflicting goals by exchange solutions between two program agents. The evaluation of this example can be done in the following way. After the implementation of this application, using a programming language, such as C++ or Java, the system is able to record the negotiation processes among these agents. We can also set up some benchmarks for the evaluation, such as a number of extreme cases, negotiation steps, etc.

## 6.2. Real estate brokerage application

In this application, we use the brokerage example adopted from the article of Jung and Jo [11] in decision support systems. This application involves dealing with the negotiation of buyers and sellers of real estate business. The problem is modeled with our framework as a multi-agent DSS system with three agents: the buyer agent representing a buyer, the seller agent representing a seller and the broker agent, that is a software agent acting as a broker between the buyer agent and the seller agent.

Similar to the application in Section 6.1, our CLAM provides a convenient means for the declarative modeling of the real estate brokerage application and problem-solving goals over systems. For instance, a house can be modeled as a CLAM object as follows.

```txt
CLASS house {
    Float price;
    Float location;
    FUNCTION traffic_to();
}
```

Agents can be modeled using CLAM. As an example, the model of the buyer<sub></sub>agent is shown as follows.

```txt
CLASS buyer_agent {
    String buyer_name;
    house target_house;
    Float income;
```

```cpp
Float saving;
Float max_mortgage;
}
buyer_agent::constraints() {
target_house.price < saving * 10;
target_house.price < saving + max_mortgage;
......
}
```

There are a number of constraints from the buyer side. As an example, the first constraint represents that the down payment should be at least 10% and the second constraint represents that the house should be affordable. The negotiation process of this application can be modeled as follows. Firstly, three agents commit their goals and constraints. The broker agent will try to match the goals and constraints from the buyer agent and the seller agent. If they cannot match, the broker agent will generate a suggestion based on the constraints of both sides. The suggestion satisfies the hard constraints of both sides and nearly satisfies the soft constraints of both sides. Then, the broker agent will send the suggestion to each side to see whether this suggestion is acceptable. After receiving the suggestion, the buyer agent and the seller agent will examine it based on its own goals and constraints and will return the replies to the broker agent. Usually, such replies are modified solutions of the suggestion from the broker agent. After several negotiation circles, the system may reach two possible results gradually: a final compromise or a dead lock.

## 7. Summary

The main focus of this paper is on modeling constraint agents for DSS applications. Constraint agents are at the early stage for real world applications. It is our viewpoint that a key feature of constraint agent technology is constraint-based interaction and negotiation among users and agents. This feature distinguishes constraint agent technology from ordinary constraintbased problem-solving systems and ordinary agent systems. Such constraint-based interaction systems have the following features.

. Constraint-based modeling. Constraints are the representation for constraint agents, and constraint satisfaction is the basic formalism for agent reasoning.

. Interactive and able to negotiate. A problem solving process is not simply a one-shot process of returning an answer for a given requirement. User preferences over the solutions are not wholly embodied as requirements. They can be transferred to the system by means of evaluating and revising the im perfect solutions.

. Adaptive and cooperative. The system takes the evaluation and revision as feedback from users or agents to improve the solution in an evolutionary way. The system should be able to learn from the dynamic user behaviors and adjust its own problem goals to adapt the revised user preferences.

. Heuristic. A typical feature of intelligent agents is that it has its own goals which the computational process is trying to achieve. Constraints and objective functions are natural means to represent agent goals. Due to the response requirements of the interactive agents, it is unrealistic and often unnecessary to conduct exhaustive search for a globally optimal solution. Heuristic opportunistic search is needed to find a nearly optimal solution in a short time.

Such features presented above make our framework a good modeling tool for future DSSs since such DSSs will be basically interactive systems with intensive decision-making capabilities. As manpower costs become more and more expensive and as the negotiation workload increases, the future DSSs will play more important roles in the negotiation process. Therefore, negotiation facilities will become more and more important for DSS applications. The CLAM presented in this paper can serve as a knowledge representation model for such DSS design, as well as the basics of the development of such future DSSs.

## Acknowledgements

This research is supported by research grants (Nos. 9049451, 7000840 and 7001014) from the Hong Kong Government and the City University of Hong Kong.

## References

[1] P. Alimonti, New local search approximation techniques for maximum generalized satisfiability problems, Information Processing Letter 57 (1996) 151 – 158.

[3] A. Borning, B. Freeman-Benson, Ultraviolet: a constraint satisfaction algorithm for interactive graphics, International Journal Constraints 3 (1) (April 1998) 9 – 32.

[4] J. Cohen, Constraint logic programming languages, Communications of the ACM 33 (1) (1990) 52– 68.

[5] K. Dockx, Y. De Boeck, K. Meert, Interactive scheduling in the chemical process industry, Computers & Chemical Engineering 21 (9) (1997) 925–945.

[6] B. Espinasse, G. Picolet, E. Chouraqui, Negotiation support systems: a multi-criteria and multi-agent approach, European Journal of Operational Research 103 (2) (1 December 1997) 389–409.

[8] L.A. Guedes, P.C. Oliveira, L.F. Faina, E. Cardozo, An agentbased approach for supporting quality of service in distributed multimedia systems, Computer Communications 21 (14) (15 September 1998) 1269–1278.

[9] A. Hafid, G. von Bochmann, R. Dssouli, A quality of service negotiation approach with future reservations (NAFUR): a detailed study, Computer Networks and ISDN Systems 30 (8) (1 May 1998) 777– 794.

[10] K.H. Kim, J.Y. Song, K.H. Wang, A negotiation-based scheduling for items with flexible process plans, Computers & Industrial Engineering 33 (3–4) (December 1997) 785– 788.

[11] J.J. Jung, G.S. Jo, Brokerage between buyer and seller against constraint satisfaction problem models, Decision Support Systems 28 (2000) 293– 304.

[12] G. Kleinman, D. Palmon, A negotiation-oriented model of auditor – client relationship, Group Decision and Negotiation 9 (2000) 17–45.

[13] V. Kumar, Algorithms for constraint satisfaction problems: a survey, AI Magazine 13 (1) (1992) 32– 44.

[14] C. Lottaz, R. Stalker, I. Smith, Constraint solving and preference activation for interactive design, Artificial Intelligence for Engineering Design, Analysis and Manufacturing (AIEDAM) 12 (1) (January 1998) 13 – 27.

[15] F.P. Maturana, D.H. Norrie, S. Kraus, Negotiation and cooperation in multi-agent environments, Artificial Intelligence 94 (1 – 2) (July 1997) 79 – 97.

[16] M. Norita, Folding arguments: a model for representing conflicting views of a conflict, Group Decision and Negotiation 9 (2000) 63 – 68.

[17] G.M. Oster, A.J. Kusalik, Icola, Incremental constraint-based graphic for visualization, International Journal Constraints 3 (1) (April 1999) 33– 59.

[18] G. Pesant, M. Gendreau, A view of local search in constraint programming, CP (1996) 353– 366.

[19] R.J. Rabelo, L.M. Camarinha-Matos, H. Afsarmanesh, Multiagent-based agile scheduling, Robotics and Autonomous Systems 27 (1–2) (30 April 1999) 15– 28.

[20] The OZ programming Systems. http://ps-www.dfki.uni-sb.de/ oz/.

[21] J.A.A. Sillincea, M.H. Saeedi, Computer-mediated communication: problems and potentials of argumentation support systems, Decision Support Systems 26 (4) (October 1999) 287 – 306.

[22] P. Sousa, C. Ramos, A distributed architecture and negotiation

protocol for scheduling in manufacturing systems, Computers in Industry 38 (2) (March 1999) 103– 113.

[23] J. Sprinkle, C.P. van Buskirk, G. Karsai, Modeling agent negotiation, Proceedings of 2000 IEEE International Conference on Systems, Man, and Cybernetics October 8 – 11 (2000) 454 – 459, Nashville, Tennessee.

[25] J. Teich, H. Wallenius, J. Wallenius, Multiple-issue auction and market algorithms for the world wide web, Decision Sup port Systems 26 (1) (July 1999) 49 – 66.

[26] H. Wang, C. Wang, Intelligent agents in the nuclear industry, IEEE Computer 30 (11) (November 1997) 28–34.

[27] J.P. Wangermann, R.F. Stengel, Principled negotiation between intelligent agents: a model for air traffic management, Artificial Intelligence in Engineering 12 (3) (July 1998) 177 – 187.

[28] C.A. Weber, J.R. Current, A. Desai, Non-cooperative negotiation strategies for vendor selection, European Journal of Operational Research 108 (1) (1 July 1998) 208 – 223.

[29] M. Wilson, A. Borning, Hierarchical constraint logic programming, Journal of Logic Programming 16 (3 – 4) (1993) 277 – 318.

[30] A. Winston, Intelligent agents as a basis for decision support systems, Decision Support Systems 20 (1997) 1.

[31] X.Q. Zhang, R. Podorozhny, V. Lesser, Cooperative, multistep negotiation over a multi-dimensional utility function, Proceeding of the IASTED International Conference, Artificial Intelligence and Soft Computing (ASC 2000), Elsevier Science, Banff, Canada, July, 2000, pp. 136–142.

[32] G. Zlotkin, J.S. Rosenschein, Mechanism design for automated negotiation, and its application to task-oriented domains, Artificial Intelligence 86 (2) (October 1996) 195 – 244.

## Further reading

[33] G. Zlotkin, J.S. Rosenschein, Compromise in negotiation: exploiting worth functions over states, Artificial Intelligence 84 (1 – 2) (July 1996) 151 – 176.

![](/api/attachments/QQR2CKQE/fulltext/images/26bfa3b38706f20f690a85eef45d6e092d53b9ec3395fba5c281455bdddf105f.jpg)

Huaiqing Wang is an associate professor at the Department of Information Systems, City University of Hong Kong. He received his PhD in Computer Science from the University of Manchester in 1987. Dr. Wang specializes in the research and development of intelligent systems, intelligent agents and their business applications, such as agent-oriented modeling, multi-agent-supported risk monitoring systems, agent-based knowledge manage-

ment systems and intelligent Web-based educational systems. His email address is iswang@is.cityu.edu.hk.

Stephen Liao is an associate professor in the Department of Information Systems, City University of Hong Kong. He received his PhD in Information Systems from Aix Marseille III University in 1993. His research areas include object-oriented modeling, systems and technology, user profiling in eBusiness and data mining techniques and applications. His email address is isliao@is.cityu.edu.hk.

Lejian Liao is an associate professor in the Department of Computer Science, Beijing Institute of Technology. He received his PhD in Artificial Intelligence from the Institute of Computing, Chinese Academy of Science in 1994. His research areas include artificial intelligence, decision support systems and intelligent agents.
