---
otero_id: 17744
otero_key: "JPDXZCH2"
title: "Formulation of qualitative models using fuzzy logic"
authors: "Narasimha Bolloju"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00005-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Formulation of qualitative models using fuzzy logic

Narasimha Bolloju $^{1}$

Department of Information Systems, City University of Hong Kong, Kowloon Tong, Hong Kong

## Abstract

Formulation of qualitative models for complex decision problems exhibiting less structure, more imprecision and uncertainty is not adequately addressed in DSS research. Typical characteristics and requirements of such problems prohibit the development of DSS using knowledge based system development methodologies. This paper presents a methodology for formulation of qualitative models using fuzzy logic to handle the imprecision and uncertainty in the problem domain. The problem domain, in this methodology, is represented using problem-solving knowledge, environmental knowledge, and control knowledge components. A high level non-procedural language for representing these components of knowledge is illustrated using a project selection and resource allocation problem. The paper also describes the implementation of a prototype decision support environment based on this methodology.

Keywords: Model formulation; Fuzzy logic; Qualitative models; Representation language

## 1. Introduction

Formulation of decision models is an important task in the problem-solving process using Decision Support Systems (DSS). This activity is usually performed by DSS builders in consultation with the decision maker. Decision problems at lower organizational levels are relatively well-structured, and once a problem is modeled it is used repetitively. The development of a DSS using quantitative modeling techniques, therefore, can involve decision makers and DSS builders. On the contrary, many decision problems at higher organizational levels are qualitative in nature. These problems are mostly ad hoc and non repetitive, and rarely sufficient time for development of a DSS for such problems is available. Many problems of this class exhibit imprecision and uncertainty in the problem-solving process and in the underlying data. Decision makers often resort to qualitative reasoning in solving such complex ill-structured problems. Their problem-solving process utilizes various rules, guide-lines, etc., and the value system of the decision maker also plays an important role in this process. Application of quantitative techniques requires many assumptions and approximations which may eventually lead to a model that is quite different from the reality.

Assistance to decision makers in model formulation process can be provided either in the form of intelligent assistance or as a methodology based support. Most research in DSS addresses the formulation of quantitative models. Research related to the provision of intelligent assistance includes, for example, knowledge-based assistance in qualitative specification of quantitative decision problems for a subsequent transformation to mathematical programming models $[3,31]$ , application of black board paradigm based on protocol analysis to model formulation $[34,35]$ .

From the perspective of methodology support, research related to the quantitative problem-solving support includes structured modeling $[15]$ and its various enhancements (e.g., $[10,16,18,27]$ ). In this area of research, the aspects of handling vagueness in the problem domain and the reasoning are delegated to the solvers. Application of the object-orientated paradigm is mostly related to the model management, reuse, and maintenance aspects (e.g., $[17,22,24,25]$ ). These approaches neither explicitly provide means nor support in qualitative model formulation for the class of problems identified above.

Approaches to qualitative problem solving commonly employ knowledge-based techniques. Despite the fundamental differences between expert systems and decision support systems $[26,30,33]$ , the knowledge-based techniques provide means for handling the issues associated with the lack of structure and inapplicability of quantitative techniques. Support for modeling in methodologies such as KADS $[36]$ is quite elaborate and suitable mostly for the development of large knowledge-based systems. Support in this form does not suit the typical DSS problems at the higher organizational levels. At these levels, problems are quite ad hoc, and the repetitive use of the same model is rare. Also, these problems are required to be solved, in relatively, much shorter time span and such characteristics prohibit building of elaborate knowledge based systems.

It follows, from the above, that the requirements of qualitative model formulation of the above mentioned class of decision problems are not adequately met by the traditional approaches. It is possible to attribute the customized development of intelligent decision support systems more as hybrid systems as the primary reason behind this trend. Significant resources and time are required to build such systems. Further, typical decision makers are neither knowledgeable of using necessary techniques nor do they have sufficient time available for a proper knowledge-based DSS development by DSS builders.

This paper aims at providing support in formulation of qualitative model process through:

1. a methodology for modeling complex ill-structured decision problems, and

2. a high-level representation language based on fuzzy logic for capturing the various components of the knowledge related to the problem domain.

In this proposed methodology, the problem domain is modeled using three components: problem-solving knowledge, environmental knowledge, and control knowledge. The problem-solving knowledge component is represented using constructs to provide model decomposition, model specification and model elaboration. The Entity-Relationship (ER) model $[11]$ is extended with facilities for representation of imprecision and uncertainty, and for deduction in modeling the environmental knowledge.

In Section 2 we present an overview of the cognitive model of qualitative problem-solving assumed by the proposed methodology. We illustrate the modeling of problem-solving knowledge using a project selection and resource allocation problem in Section 3. In Section 4 we describe the modeling of the environmental knowledge. Various types of control knowledge are presented in Section 5 with examples. In Section 6 we present the implementation details of a prototype decision support system environment for supporting the proposed methodology. Concluding remarks in Section 7 are followed with a sample session of a project selection example using the prototype.

## 2. Overview of the proposed methodology

Model formulation is a complex and ill-structured process of conceptualization and representation of the problem domain. Specific steps in this process depend upon the assumed cognitive model of the problem-solving process. Fig. 1 depicts the cognitive model of the qualitative problem-solving process assumed for the proposed methodology.

![](/api/attachments/JPDXZCH2/fulltext/images/23740c7c7fb25b21ded3439ac2c65f4e123004260a82b4e890ae1eb5f9ceee73.jpg)  
Fig. 1. Problem-solving process.

Problem-solving knowledge deals with the structuring, decomposition, specification and elaboration of decision problems. Environmental knowledge is a collection of the entities, the relationships between the entities, and the common deductive knowledge. The problem-solving knowledge refers to this environmental knowledge extensively during the representation and model execution. The control knowledge component is a collection of strategic knowledge that is useful in the model execution. This component comprises of the knowledge related to the prioritization of problem-solving tasks, heuristics for generation of alternative and controlling of the inference process.

The proposed methodology shares some common representational features with KADS [36]. For example, the four-layered representation of problem domain using strategic, task, inference and domain knowledge components of KADS correspond closely to the control, problem-solving and environmental knowledge components. Environmental knowledge in the proposed methodology corresponds to the inference and domain knowledge components of KADS.

## 2.1. Problem-solving knowledge

Formulation of qualitative models for problems with the characteristics described in Section 1 requires facilities for decomposition of complex models into simpler models, and representation of imprecision and uncertainty. Problem decomposition ranges from a simpler hierarchical decomposition to a more complex form involving alternate model selection and iteration. Representation of imprecision and uncertainty ranges from the specification of the decision problem to the model parameters. We chose fuzzy sets and fuzzy logic for qualitative model representation because it provides facilities for representation of both imprecision and uncertainty in a unified framework $[2,38–40]$ , and offers other benefits in modeling complex problems as discussed in $[41]$ .

A layered approach is proposed to model the problem-solving knowledge as depicted in Fig. 2. The top layer represents the decomposition hierarchy. In this layer, complex decision problems can be decomposed into simpler decision problems. For example, a budget allocation decision problem to allocate a specific amount of budget among a set of projects can be decomposed as short-listing of projects, selection of projects and allocation of budget decision problems. A decision model can also have multiple specifications or instances. For example, a model for resource allocation to projects can have different specifications with selection determined by type of project. We shall describe this aspect of model selection through fuzzy pattern matching later in Section 6.

![](/api/attachments/JPDXZCH2/fulltext/images/60483291b30b0aa61dba62a130d853acaaef4dcb555e962be998988dccaf46a2.jpg)  
Fig. 2. Three layers in problem-solving knowledge.

Leaf nodes of the decomposed decision models at the top layer (Fig. 2) are called decision units. Decision units represent decision problems that cannot be further decomposed naturally. A specification of problem class, class of alternatives, pre-conditions, actions, post-conditions, and ranking rules model such problems. The problem class can be one of selection, assignment, allocation, etc. The class of alternatives specifies the solution structure for the decision unit, and it refers to the entities of environmental knowledge in the simplest form and to the derived knowledge in more complex forms. Pre- and post-conditions specify various hard and soft constraints to be satisfied by the alternatives or solutions. The action part of the specification addresses the updates, if any, to the working memory. These updates are the means for exchanging complex data across various elements of the problem-solving knowledge. Ranking rules represent the objective function, possibly fuzzy, for measuring the utility of a solution and comparing the alternate solutions.

The above three types of rules constitute the decision rule layer of the problem-solving knowledge. Decision rules, in the backward chained form, are extended to support aggregation and quantification. Knowledge representation based on fuzzy logic is known to be natural, concise and more intuitive compared to simple production rules. The extensions regarding the aggregation and quantification are essential in modeling decision problems (this aspect is illustrated in Section 3).

The layered representation of problem-solving knowledge, presented above, draws upon the other problem solving methods such as heuristic classification $[12–14]$ , task structure $[9]$ , and task based specification $[37]$ . Clancey $[12–14]$ describes classification and construction as the two important methods for problem solving. From this perspective, decision models at the top level can be viewed as supporting construction of decision models through decomposition into decision models and decision units, and the decision units as supporting the classification. The chains of abstractions and the heuristics linking the different chains are represented by the decision rules.

Chandrasekaran et al. [9] propose task structure as recursive links of a task to alternative methods and the methods to their subtasks. They emphasize the separation of tasks from the methods used to achieve goals. Although this distinction is not present in the proposed approach, correspondence can be seen in hierarchical decomposition of decision models into decision models (subtasks) and decision units (multiple methods).

The Task-Based methodology of Yen and Lee [37] for specifying expert systems can also be compared with this three layered modeling of problem-solving knowledge. The behavioral specification employs compositions such as sequence, condition/selection, and iteration. The functional component is represented using pre-condition, protection, and post-condition specification. That is, the top and middle layers of the problem-solving knowledge model correspond to the process specification [37]. Yen and Lee also propose the application of fuzzy logic for generalizing the soft post-conditions to handle uncertainty in the heuristic classification systems.

## 2.2. Environmental knowledge

Traditionally, the environmental knowledge is perceived as a collection of data that is used during the specification and execution of decision models. Data used in models representing structured problems is, in general, precise and certain; and there is little need for deductions or inferences. On the contrary, decision problems at higher organizational levels deal with an imperfect environment $[4,20,21]$ . Imprecision and uncertainty, for example, could arise in attributes representing futuristic data and vaguely known external data. Similarly, some relationships can be uncertain such as the relationship between the effect of certain market fluctuations and, say, the expected demand. We elaborate the approach used for representation of imprecision and uncertainty later in Section 2.4.

From the above, one might argue that this form of knowledge is quite similar to that used in expert systems. There are, however, certain fundamental differences between the two types of knowledge $[26,30,33]$ . First, the structure of the knowledge is rarely complex in decision making environments. Usually it is a collection of simple entities, and relationships between the entities, and the depth of inference is fairly shallow compared to that in typical expert systems. Such requirements for representing environmental knowledge in decision support environments can be met using simpler models such as the Entity-Relationship model with extensions to support imprecision and uncertainty, and deductive capabilities.

## 2.3. Control knowledge

Control knowledge is used in the problem-solving process to guide the search process in the solution space. This knowledge, often in the form of heuristics, is employed by the decision maker in activities such as generation of alternative solutions, selection of an appropriate model, and ordering the execution of specific models. The control knowledge, also referred to as the strategic knowledge [36], defines the strategies to be adopted in model execution and inference process. In the proposed methodology, the control knowledge can be associated with various elements of the problem-solving knowledge, and the environmental knowledge.

![](/api/attachments/JPDXZCH2/fulltext/images/9f8d7cdbc58a386a5f699b5ad7515927f504b0d90565443aeb3c1b12c603362e.jpg)  
Fig. 3. Fuzzy sets for RiskPermitted parameter values.

## 2.4. Representation of imprecision and uncertainty

Use of fuzzy logic as a framework for management of imprecision and uncertainty helps in overcoming many limitations of conventional techniques $[40]$ . We employ possibility distributions (equivalent to membership functions defining fuzzy sets $[41]$ ) to model the imprecision in the attribute values and model parameters. Trapezoidal possibility distributions are one of the widely used methods to represent imprecision values. Fig. 3, for example, depicts three such possibility distributions to represent lowRisk, moderateRisk, and highRisk as imprecise values. The labeled imprecise values, such as these three, are called linguistic constants. It is possible to match, partially, such values with other imprecise (or precise) values.

Certainty measures, in this implementation, are represented using pairs of necessity–possibility measures $[28,29]$ . A necessity-possibility measure $[n,p]$ associated with a decision rule in the form “Y is B if X is A @ $[n,p]$ ” indicates the possibility $(p,0\leq p\leq1)$ that the consequent $(Y \text{ is } B)$ is true when the antecedent $(X \text{ is } A)$ is found true. The necessity measure $(n,0\leq n\leq1)$ indicates the impossibility that the opposite of the consequent true when the antecedent is found true (or 1 – possibility of Y is $\neg B$ ). The necessity–possibility measures can also be used for representing the results of fuzzy pattern matching (or semantic unification $[1]$ ) of an imprecise datum D with an imprecise pattern P. Given the universe of discourse U with pattern P and datum D defined on U, the possibility p of matching D with P is:

$$
p = \sup _ {u \in U} \min \left(\pi_ {P} (u), \pi_ {D} (u)\right).
$$

The necessity n of matching D with P is:

$$
n = \inf _ {u \in U} \max \left(\pi_ {P} (u), 1 - \pi_ {D} (u)\right),
$$

$$
\text { or } 1 - \sup _ {u \in U} \min \bigl (1 - \pi_ {P} (u), \pi_ {D} (u) \bigr).
$$

Applying these formulae for matching the datum moderateRisk (see Fig. 3) with the pattern highRisk results in a degree of match equal to [0,0.5].

## 3. Modeling of problem-solving knowledge

As described above, the three layers consisting of decision models at the top layer, decision units at the middle layer, and decision rules at the bottom layer model the problem-solving knowledge. In this section we discuss various features of these layers in detail using a project selection and resource allocation problem in a research laboratory environment.

## 3.1. Decision models

Decision models, as proposed in this paper, are composed using other decision models and decision units. The following types of composition operators are considered:

1. sequential composition,

2. parallel composition,

3. conditional composition, and

4. iterative composition.

Sequential composition imposes an order on the invocation of the decision models. On the other hand, the parallel composition does not impose any order on the invocation, and it offers the possibility of parallel execution. The composition operators (1), (2) and (4) are based on the principles of structured programming, and this implies that any form of composition can be made with this set of operators. We believe that this form of representation, specially for iteration, is more natural and intuitive to typical decision makers as compared to logic based recursion. It can also be argued that at this level of abstraction the conventional programming model would not compromise the readability of the composed models.

Example 1: A decision model for project selection and resource allocation.

dmodel projectSelectionAndResourceAllocation (Threshold, RiskPermitted, MaxBudget)

is screenProjects(Threshold)

$\rightarrow$ if RiskPermitted $= \sim$ lowRisk

then selectSoundProjects(MaxBudget,P)

else selectProjects(MaxBudget,P)

→foreach PJ in P do assignResources(PJ).

The decision model in Example 1 depicts a composition of model projectSelectionAnd-ResourceAllocation using four decision units: screenProjects for screening of the initial set of projects using an upper limit on the budget, selectSoundProjects for the selection of projects with low risk, selectProjects for the selection of projects with risk above \~lowRisk, and assignResources for assigning resources among the selected projects. It also illustrates sequential, conditional and iterative compositions using these four decision units. It is possible to replace the selection among the two types decision units using two different instances of selectProjects with an additional input parameter for risk.

Furthermore, the parameters of the model can be imprecisely stated. For example, the parameter RiskPermitted can be $\sim$ moderateRisk defined by the possibility distribution $\langle20,40,60,80\rangle$ on a domain of 0 to 100 (see Fig. 3). In such a case, the comparison “ $\sim$ moderateRisk = $\sim$ lowRisk” in the above decision model will succeed to a certain degree. Many parameters and attribute values may involve computations and comparisons of such imprecise values.

An example invocation of the model in Example 1 is shown below:

projectSelectionAndResourceAllocation

(500000, \~moderateRisk, \~about $_{10}$ )

The last parameter $\sim$ about\_10 indicates a soft or an elastic constraint on the maximum available budget (in millions of dollars). The definition of the linguistic constant $\sim$ about\_10 can be $\langle9, 9.8, 10.2, 11\rangle$ .

## 3.2. Decision units

Decision units represent the lowest level of decomposed parts of decision models. The specification of decision units, as proposed in this paper, captures the part of the decision problem using the following six items: 1. problem class,

2. class of alternatives,

3. pre-conditions,

4. actions,

5. post-conditions,

6. ranking.

The items (1) and (2) above together determine the type of the problem and the structure of possible solutions. For example, a decision unit for selection of a set of projects from a given list of projects can be specified using the problem class select and the class of alternatives as set of projects. The problem class corresponds to the generic class of problem such as select, assign, allocate; and the class of alternatives specifies the exact composition of alternatives. These alternatives will be constrained by the remaining specification of the decision unit. Some examples of these two types of items are listed in Table 1.

The items pre- and post-conditions constrain the possible solutions before and after the updates, if any, to the working memory. These updates are specified as part of the actions, and it is the mechanism through which various components of the problem-solving knowledge share or exchange complex data. The ranking rules define the objective function, possibly fuzzy, to the specific part of the problem. All the above items, excepting the first one, can be further elaborated using decision rules. This remaining part of the specification is common to all decision units and it merely constrains and ranks the possible alternatives. The semantics of these attributes are, therefore, independent of the problem class and class of alternatives.

Table 1  
Examples of pclass and altclass of decision unit specification

<table><tr><td>Pclass</td><td>Altclass</td><td>Description</td></tr><tr><td>Select</td><td>PJ of proposedProject</td><td>All entities, including derive, (PJ) of proposedProject are possible alternatives</td></tr><tr><td>Select</td><td>Subset P of screenedProject</td><td>All subsets (P) of screenedProject are possible alternatives</td></tr><tr><td>Assign</td><td>R of resource to PJ of projects</td><td>The alternatives are  $\langle R, PJ \rangle$  pairs of entities</td></tr><tr><td>Assign</td><td>R of resource to subset P of project</td><td>The alternatives are  $\langle R, P \rangle$  pairs where P is a set of project entities</td></tr></table>

Example 2: Decision units for (a) screening and ranking the projects, and (b) selection of a set of projects:

```prolog
a) dunit screenProjects(Threshold, RiskAllowed)
is pclass select
altclass PJ of proposedProject
precond PJ.budgetRequired ~below Threshold
action insert PJ into screenedProject
rank OQ of overallQuality(PJ,OQ).
b) dunit selectSoundProjects(MaxBudget)
is pclass select
altclass subset P of screenedProject
precond meetsBudgetoryRequirements(P,MaxBudget) and otherResourcesAvailableFor(P) and overallRiskWithinLimits(P)
action createSelectedProjects(P)
postcond combinedProjectsStrength >= ~high
rank ROI of expectedReturnOnInvestment(P,ROI).
```

Decision unit in Example 2a is a specification of short-list of the proposed project entities based on the budget requirement and ranking them on the overall quality. Overall quality of a project is defined using a set of decision rules (see Example 3c). The comparison operator $\sim$ below is a fuzzy relational operator and it implies that budget requirement above Threshold also qualify to a lower degree of certainty. Example 2b illustrates the use of set of entities as the class of alternatives. The specification defines all the possible subsets of screenedProject entities as the solution space.

## 3.3. Decision rules

The top and middle layers of the problem solving knowledge, as described in the previous sections, deal with the higher levels of abstraction of the decision problems. The bottom layer of decision rules elaborates the specification of the decision units. There are three types of rules: conditional rules (pre- and post-condition types), action rules, and ranking rules. Example 3 illustrates some decision rules.

Example 3: Decision rules illustrating aggregate functions, fuzzy quantifiers and fuzzy implication.

a) drule meetsBudgetaryRequirements(P,MaxBudget)

```txt
if sum(PJ.budgetRequired: in(PJ,P) <= MaxBudget) and
```

count(PJ:(in(PJ,P) and PJ.budgetRequired = \~high) < 3).

b) drule projectMixIsInlineWithCorpObjectives(P)

if most(PJ:in(PJ,P), PJ.relevanceToCorpObj = \~high) and

supportsFuturePlans(P).

c) drule overallQuality(PJ, \~high)

if PJ.technicalQuality = \~high and

PJ.proposedApproach = \~very sound @ [0.9,1].

drule overallQuality(PJ, \~moderate)

if PJ.technicalQuality = \~medium and

PJ.proposedApproach = \~sound.

drule overallQuality(PJ, \~low)

if PJ.technicalQuality = \~poor.

The constraint on the budgetary requirement (Example 3a) uses aggregate functions sum and count on the subset of screenedProject entities P. This rule represents a soft constraint that a subset (of projects) P meets the budgetary requirements if the sum of individual budget requirements is below the maximum available budget and there are at most two projects in the subset requiring $\sim$ high budget.

Example 3b depicts a typical situation decision makers come across in ill-structured problems. It represents a vague rule specifying whether a project mix is in line with the corporate objectives or not. The first part of the antecedent captures the condition “most (a fuzzy quantifier) of the projects in P have high relevance to the corporate objectives.” The second part of the antecedent, supportsFuturePlans(P), can be elaborated using another set of decision rules.

Example 3c lists a set of three fuzzy ranking rules defining the overall quality of a project, possibly imprecise, in terms of technicalQuality and proposedApproach. It is assumed that values to these attributes of proposedProject entities are assigned manually.

## 4. Modeling of environmental knowledge

Environmental knowledge, as described in Section 2, is a collection of knowledge that is common to many related decision problems. This collection comprises various elements such as entities, relationships between entities, and deductive rules. Elaborate description of these components and usage is reported elsewhere [5,7]. The ER diagram shown in Fig. 4 represents a typical model of entities and relationships in the research laboratory environment. Some of the definitions entity types, relationship types, domain types, and rules are listed in Example 4. Attributes of entity types are associated with domain types, dtype. Definition of a dtype includes the range, the units of measurement, and the linguistic constants.

![](/api/attachments/JPDXZCH2/fulltext/images/bf15e784ea5145a898dae900de65a6176e36989a29cb3d55e5da4c06f5aae081.jpg)  
Fig. 4. Partial ER-diagram of the example.

## Example 4:

a) etype researchStaff(id:number,name:charAt, ...)

etype proposedProject(pid:number,

budgetRequired: budgetAmount,

relevanceToCorpObj:relevance,

technicalQuality:qualityRange,

proposedApproach:valueGrade)

b) rtype coversAreas(ongoingProject,researchArea).

rtype areasOfInterest(researchStaff,researchArea).

c) dtype budgetAmount 1 to 10 millions,

lowBudget = ⟨1,1,2,3⟩,

highBudget = ⟨8,9,10,10⟩.

dtype riskValues 0 to 100,

lowRisk = ⟨0,0,20,40⟩,

moderateRisk = ⟨20,40,60,80⟩,

```txt
highRisk = ⟨60,80,100,100⟩.
```

d) erule expertiseAvailable(Area, \~highLevel)

if exists(P:ongoingProject(P), coversAreas(P,A) and A.area = Area).

erule expertiseAvailable(Area, \~moderateLevel)

if count(S: researchStaff(S) and areaOfInterest(S,A) and

A.area = Area) > \~about 3 @ [0.8,1].

Rules in the Example 4d represent a component of derived knowledge, concerning the availability of expertise, expressed using the existential quantifier and aggregate function count. These rules are similar, in structure, to the decision rules; the difference, however, is that such rules specify the knowledge common to many decision problems.

## 5. Modeling of control knowledge

This component of knowledge assists the problem-solving process particularly from the efficiency view point. Some possible elements of this form of knowledge includes the specification of:

\- heuristics to be used during the generation of alternatives (or solutions) for specific decision units,

\- heuristics linking chains of causal relationships described by decision rules,

\- priorities in execution of decision models, decision units, and decision rules,

\- priorities in selection of various elements of environmental knowledge,

\- thresholds or cut-off values of necessity–possibility measures during the inference process,

\- minimum and maximum cardinalities for the composition of solutions with structures as sets of entities,

\- defuzzification algorithm (e.g., max-of-means, centre-of-gravity) to be used in the fuzzy inference process.

Example 5: Heuristics for generation of alternatives and threshold NP measures.

a) heuristic on dunit selectSoundProjects

order screenedProject SP descending on Risk of estimatedRisk(SP,Risk).

b) npcutoff on drule meetsBudgetaryRequirements is [0.6,1].

This heuristic in Example 5a, defined for the decision unit selectSoundProject, represents the control knowledge on the generation of alternative solutions. It ensures that the alternatives generated for this decision unit select the project entities based on the descending values of estimated risk. The estimation of risk associated with a project can be specified using another set of decision rules. The cut-off value, in Example 5b, defines the cut-off necessity—possibility measure to be used by the fuzzy inference engine while inferencing the decision rule meetsBudgetaryRequirements.

![](/api/attachments/JPDXZCH2/fulltext/images/f673fbc22ed06642d8f45f513f1d29ec7a928860348cea54b5db345f851fc7f5.jpg)  
Fig. 5. Architecture of the prototype.

## 6. Implementation of a prototype

In this section we describe the implementation of a prototype that supports the proposed methodology. The architecture of the prototype, depicted in Fig. 5, is based on the generic architecture proposed by Bonczek et al. [8]. Fig. 5 also shows the components within the language system (LS), the problem-processing system (PPS) and the knowledge system (KS). The prototype, implemented in C-Prolog, provides the basic facilities required for model activation and exploratory information retrieval. The primary objective of this prototype is to demonstrate the feasibility and practicality of the proposed methodology by building a decision support environment.

Implementation of Knowledge System: The KS is primarily a representational system. The collection of various items of specification (such as decision models, decision units, decision rules, domains, entities) is maintained in a group of related text files for a given problem domain. These items are mapped, after parsing, to pre-defined Prolog structures. These structures are asserted into the Prolog database during the load operation (illustrated in Appendix A). The Prolog structure corresponding to the decision model in Example 1 is listed below:

decModel(name(projectSelectionAndResourceAllocation),

args([Threshold, RiskPermitted, MaxBudget]),

body([screenProjects(Threshold),

$$
\text { ifstat } (\text { RiskPermitted } = \text { lingConst(lowRisk) },
$$

then(selectSoundProjects(MaxBudget,P)),

else(selectProjects(MaxBudget,P)),

foreach(in(PJ,P), do(assignResources(PJ)))]).

Linguistic constants are represented using the structure $memFun(A,B,C,D)$ where the four arguments represent the four points of the trapezium depicting the possibility distribution from left to right. Pattern matching operations on such values are detailed later in this section. Necessity–possibility measures are represented using the structure $np(N,P)$ .

Implementation of Language System: LS, in the current implementation, is a simple command interpreter. The facilities in LS include model activation (or execution) and exploratory information retrieval apart from other supporting facilities. Decision models or decision units can be activated by supplying the name of the model and the input parameters (see the activate command in Appendix A). LS simply passes control to the PPS for the interpretation, execution and presentation of the alternatives to the decision problem represented by the activated model.

The second major facility provided under LS is the information retrieval based on approximate query specification. Decision makers can specify, during the process of model formulation, queries with vague or imprecise conditions and parameters using a high-level non-procedural language to operate on the environmental knowledge. This form of retrieval, in addition to providing assistance in model formulation, minimizes the need for building models for certain types of decision problems which can be expressed using decision rules. Elaborate discussion of the specifics of this query language is beyond the scope of this paper and its formal definition can be found elsewhere $[6,7]$ .

Implementation of Problem-Processing System: Implementation layers of PPS are shown in Fig. 6. In the remaining part of this section we present the algorithms activation of decision models, decision units, and semantic unification. Since the decision rule processing follows the typical backward chained inference mechanism using fuzzy rules, it is not further detailed. We describe the semantic unification that is used extensively in the selection process of decision models, decision units and decision rules.

(a) Activation of a decision model selects an applicable model among the decision models with the same name, and processes of its specification. As part of this process, the alternatives found for various parts of the decision model are reported. The algorithm detailing the model activation is listed below:

Activate decision model with name M and parameters $\mathbf{P} = \{\mathbf{p}_1,\mathbf{p}_2,\dots ,\mathbf{p}_n\}$

Search for an applicable decision model

(1) Find a decision model with name M, and let $A = \{a_1, a_2, \ldots, a_n\}$ be its arguments.

<table><tr><td colspan="2">Command Shell (Language System)</td></tr><tr><td>Decision Model Processor</td><td rowspan="2">Fuzzy Query Processor</td></tr><tr><td>Decision Unit Processor</td></tr><tr><td colspan="2">Decision Rule Processor</td></tr><tr><td colspan="2">Fuzzy Inference Engine</td></tr><tr><td colspan="2">C-Prolog</td></tr></table>

Fig. 6. Implementation layers in the problem-processing system.

(2) Perform semantic unification (see below) treating arguments in A as the pattern and parameters in P as the datum. Let NP be the combined truth value of the result of unifying the n argument-parameter pairs. (This process binds all the uninstantiated variables in A and P.)

(3) If the resultant NP is below the threshold measure (either the system default or the threshold specified for the decision model) then return to step 1 because this model instance is not applicable for activation.

Interpret the applicable decision model

(4) Analyze the decision model body, recursively activating any decision models included in the specification, until a decision unit is reached. Further processing of the decision unit (with name U and parameters $A_{u}$ ) related to this algorithm is detailed in the steps 5 and 6.

Present the alternatives found for decision unit $U$

(5) Process the decision unit U and parameters $A_{u}$ ( $A_{u}$ is a subset of P and other variables introduced for data exchange). If an alternative is found then display that alternative. Otherwise, backtrack to the previous sub-component of the decision model under activation.

(6) Prompt the user for skip, commit, or next option. The skip option skips the sub-component (as if no alternative was found). The next option ignores the current alternative. The commit option asserts the current alternative as the chosen alternative and proceeds to the next sub-component of this model instance, if any.

(b) Activation of a decision unit includes the selection of an applicable decision unit, generation of probable alternatives, and evaluation of pre-condition, action and post-condition parts of the specification to determine whether the probable alternative satisfies all the criteria. The algorithm detailing this process is listed below:

Activate decision unit with name U and parameters $P = \{p_{1}, p_{2}, \ldots, p_{m}\}$

Search for the applicable decision units

(1-3) The steps 1 through 3 are similar to those described in the above algorithm.

Generate alternatives for the applicable decision unit

(4) Order the entities to be considered for generating the probable alternatives using the heuristics defined in control knowledge for this decision unit. In the absence of any heuristic the rank rule will be considered as a heuristic wherever possible. It is not possible to use the rank rule as a heuristic when, for example, it refers to the attributes that are likely to be computed or updated in action rules. The identifiers of the entities of the probable alternatives, formed according to the pclass and altclass specification, are asserted in the working memory for later use in step 6 below.

Determine whether a probable alternative is an alternative

(5) Evaluate the pre-condition, action, and post-condition rules. If the results of evaluation of these rules are below the respective threshold necessity—possibility measures then select the next probable alternative.

(6) Evaluate the rank rule if it was not pre-computed in step 4. For subset type of alternatives it is not guaranteed that the alternatives are reported based on the rank value. The order in which the alternatives are reported is determined by the heuristic value.

(c) The semantic unification process performs a fuzzy pattern matching operation on the parameter and argument pairs. We describe below the adaptation of the definition presented in Section 2.4 for trapezoidal possibility distributions:

Semantic unification of $\mathbf{V}_1$ (datum) and $\mathbf{V}_2$ (pattern) resulting truth value [n,p] Bind and evaluate the datum and pattern

(1) If either $\mathbf{V}_1$ or $\mathbf{V}_2$ is an uninstantiated variable then bind $\mathbf{V}_1$ to $\mathbf{V}_2$ , return $[\mathfrak{n},\mathfrak{p}] = [1,1]$ .

(2) Evaluate $V_{1}$ and $V_{2}$ . Let $[a_{1},b_{1},c_{1},d_{1}]$ and $[a_{2},b_{2},c_{2},d_{2}]$ be the evaluation results of $V_{1}$ and $V_{2}$ .

respectively. Expressions with linguistic constants will be expanded to the possibility distributions as a result of this evaluation. We exclude the cases where non-fuzzy values are unified with fuzzy values, because such unification is a special case of this algorithm.

Compute the possibility measure $p$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(3) if  $d_{1} &gt; = a_{2}$  and  $d_{2} &gt; = a_{1}$ 
then if  $c_{1} &lt; b_{2}$ 
    then p = yCoordOf(intersectionOf([c₁,1],[d₁,0]],[[a₂,0],[b₂,1]])
    else if  $c_{2} &lt; b_{1}$ 
    then p = yCoordOf(intersectionOf([c₂,1],[d₂,0]],[[a₁,0],[b₁,1]])
    else p = 1
else p = 0;
</div>

Compute the necessity measure $n$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
(4) if  $a_{2} &gt; = b_{1}$  and  $d_{2} &lt; = c_{1}$ 
then n = 1
else if  $a_{1} &lt; = b_{2}$  and  $c_{2} &lt; = d_{1}$ 
then  $n = \min(yCoordOf(intersectionOf([a_{1},0],[b_{1},1]),[[a_{2},1],[b_{2},0]]))$ ,
    $yCoordOf(intersectionOf([c_{1},1],[d_{1},0]),[[c_{2},0],[d_{2},1]])))$ 
else n = 0;
</div>

The other significant part of the implementation, related to the fuzzy aspects such as the fuzzy arithmetic, comparison using fuzzy relational operators, fuzzy quantification, and fuzzy aggregation are also adaptation of relevant definitions reported in $[28,29]$ . In the appendix A, a sample session for selection of a subset of projects from a given set of proposed projects is presented.

## 7. Concluding remarks

A methodology for formulation of qualitative models for complex decision problems at higher organizational levels using fuzzy logic is presented in this paper. Imprecision and uncertainty inherent in the problem domain is modeled explicitly in this approach rather than approximating to a precise and certain terms. In this process, the proposed methodology integrates many problem solving approaches used in knowledge based systems to address the typical qualitative aspects of the problem domain. Although many of the concepts, applied in this integration, are presented in literature related to artificial intelligence and knowledge based systems, this paper addresses the typical requirements of qualitative decision problems with a special emphasis on facilitating typical decision makers with the necessary support in the model formulation.

This methodology extends and enhances the formalism and the representation language presented in [6]. McCarthy [23], in his Turing Award lecture, points out that “... beyond that (Horn clauses) lies full first-order logic including both existential and universal quantifies and arbitrary first-order formulae”. He, further, remarks that “...reasoning and problem-solving programs must eventually allow the full use of quantifies and sets ...”. The modeling language illustrated in this paper facilitates the specification of decision problems with higher level constructs for quantification and aggregation. By providing an executable high level specification, this approach can help in effective and rapid development of qualitative models for solving complex decision problems.

Three layers in the methodology help in the model formulation through:

1. integration of decision models and decision units to model complex problems,

2. a high level specification of decision units representing simplified decision problems, and

3. fuzzy rules for natural elaboration of the decision unit components.

The proposed methodology differs from KADS in modeling the problem-solving knowledge component. This component, which is the equivalent of task knowledge, has multiple concepts such as decision models, decision units, and decision rules. We believe that this distinction will enhance the flexibility in representing a variety of problem situations. Also, it addresses a drawback often found in typical rule based systems where production rules are used for the representation of different elements of problem-solving knowledge, control, user-interface, and iteration through recursion. By providing appropriate modeling paradigms and separating the different elements of the knowledge, the proposed methodology can facilitate easier formulation of complex models.

A comparative evaluation of the proposed methodology with the other knowledge based system development methodologies and with the traditional quantitative approaches is important to demonstrate its effectiveness. An important extension of this proposed methodology, in facilitating reuse, is related to the application of the concept of inheritance in various components of the knowledge system. It is possible to address this issue using the recent developments in extending inheritance concept with fuzzy set theory (e.g., [17,19]). Extensions to the proposed methodology to provide knowledge based assistance in model formulation around the generic task models [32,36] are planned. These extensions are aimed at supporting typical decision makers in the model formulation, in addition to the support in decision making, with an active intelligent assistance.

## Appendix A - A Sample Session Using the Prototype

In this appendix we present a sample session using the prototype environment. The complete session is listed in courier font, and the commands entered by user are shown in italics. Annotations have been added (in Times Roman font) to provide the necessary explanation.

## \$ qdmenv

qdm> help

Command - Description

setdom D sets the problem domain to D
listdom lists all the known problem domains
load kb loads all the three knowledge components
load ekb loads environmental knowledge component
load pkb loads problem-solving knowledge component
load ckb loads control knowledge component
edit ekb edits environmental knowledge
edit pkb edits problem-solving knowledge
edit ckb edits control knowledge
list ekb lists environmental knowledge
list pkb lists problem-solving knowledge
list ckb lists control knowledge
activate F activates a decision model or a decision unit
query exploratory information retrieval
exit exits from qdmenv

Activate and query are the two key commands for model activation and information retrieval using approximate query specification. We illustrate setdom, load, list and activate commands in this session.

qdm> setdom projectSelection

Problem domain is set to "projectSelection".

A new identifier, here, initiates a new DSS problem domain. All the three knowledge

components for the new problem domain can be entered using the edit command option.

Edit command invokes the default system editor, and upon the exit from the editor the

updated component is reloaded

qdm> load kb

Problem-solving knowledge is being loaded ...

Environmental knowledge is being loaded ...

Control knowledge is being loaded ...

qdm> list ekb

% template definitions

Comments are specified using the '%' symbol at the beginning of the line

etype proposedProject(

pid:number, title: charString, duration: projDuration,

effort:personPower,type:charString,area:charString,

complexity:projectComplexity, cost:projectCost).

etype promisingArea(aid:number, area: charString).

We use these two entity types to illustrate a decision model (every decision unit is also a

decision model) to select a set of projects from the entities of etype proposedProject. The

following dtype declarations define the fuzzy linguistic constants which are globally

available.

8 linguistic constant definitions

dtype personPower 1 to 10 years,

about\_5 = <3,5,5,7>,

about\_4 = <2, 4, 4, 6>,

twoToThree =<2,2,3,3>.

dtype projectComplexity

quiteComplex = <0.8, 0.9, 1, 1>, .

moderatelyComplex = <0.6, 0.8, 0.8, 0.9>, .

complex = <0.5, 0.7, 0.8, 0.9>, .

notSoComplex = <0.3, 0.3, 0.5, 0.5>.

dtype projectDuration 1 to 36 months

aboutTwoYears = <18,24,24,30>,

aboveTwoYears = <21, 24, 30, 36>,

about\_18\_months = <15, 18, 18, 21>.

dtype projectCost 1 to 20 millions

expensive = <1,7,10,20>,

moderatelyExpensive = <0,2,5,15>.

8 environmental knowledge

% proposed projects

proposedProject(pl, dist\_dbms, \~about\_5, <36, 36, 48, 48>, developmental,
database, \~quiteComplex, <2.376, 3.96, 5.25, 7.392>).

proposedProject(p2,dss\_generator,\~aboutTwoYears,3,research,
decision\_support,\~moderatelyComplex,
<1.35,1.8,1.8,2.25>).

proposedProject(p3,tp\_package,36,\~about\_4,developmental,
operating\_systems,\~complex,<1.584,3.168,3.168,4.752>).

proposedProject(p4, prolog\_compiler, \~aboveTwoYears, \~about\_5, research, programming\_languages, \~complex, 1.8).

proposedProject(p5,gims,12,15,turnkey,games\_management,\~notSoComplex,3.6).

proposedProject(p6,expsys\_shell,-about\_18\_months,3,research,
artificial\_intelligence,-complex,
<1.125,1.35,1.35,1.575>).

% promising areas

promisingArea(al, four\_GL).

promisingArea(a2, database) @ [0.9,1].

promisingArea(a3, networks).

promisingArea(a4, programming languages) @ [0.8,1].

promisingArea(a5,operating\_systems) @ [0.7,1].

promisingArea(a6, artificial intelligence).

promisingArea(a7,decision\_support).

promisingArea(a8, games management) @ [0.6, 0.9].

qdm> list pkb

% decision units

8 selection of a set of projects P from the set of proposed projects

dunit selectProjects(MaxBudget)

is pclass select

altclass subset P of proposedProject

precond (meetsCostConstr(P,MaxBudget) and

goodMixOfProjects(P) and

marketDriven(P)),

rank sum(PJ.cost:in(PJ,P)).

Alternatives generated by this decision unit are ranked on the total cost of projects

selected, i.e., the best utilisation of the available budget.

8 decision rules

% set of projects, P, meets the cost constraint if the total cost of

% the projects is below the available budget and there are

8 not more than 2 expensive projects in the set P

drule meetsCostConstr(P,MaxBudget)

if (sum(PJ.cost:in(PJ,P)) <= MaxBudget) and

(count(PJ: (in(PJ, P) and PJ.cost = \~expensive)) <= 2).

% the set of projects P is a good project mix provided P contains

8 at least one turnkey, one developmental and one research project.

drule goodMixOfProjects(P)

if existsa(P, turnkey) and existsa(P, developmental) and

existsa(P, research).

% the set of projects P is possibly a good project mix if P contains

% at least one turnkey and one developmental project

drule goodMixOfProjects(P)

if existsa(P, turnkey) and existsa(P, developmental) @ [0.8, 1].

drule existsa(P, Type)

if exists(PJ:in(PJ,P), PJ.type = Type).

% the set of projects P is market driven if there is at least one

8 project of a promising area

drule marketDriven(P)

if exists(PJ:in(PJ,P), exists(A:promisingArea(A),A.area = PJ.area)).

qdm> list ckb

heuristic on dunit selectProjects

order proposedProject PJ descending on PJ.cost.

Heuristic to be used during the activation of decision unit selectProjects. This indicates

that the alternatives are generated for further processing after ordering proposed projects

in descending order of cost.

qdm> activate selectProjects(<10,12,14,16>).

Activation of decision unit selectProjects with an imprecise budget value specifying

approximately between 12 and 14 million dollars. It can be noticed that the alternatives

are subsets or groups of proposed projects.

Alternative # 1

Decision Unit :selectProjects
Rank value :<7.326,9.35999,10.68,13.242>
Precondition :[0.713371,1]
Postcondition :[1,1]

proposedProject ( pid :p1,
    title :dist\_dbms,
    duration :<36,36,48,48>,
    type :developmental,
    area :database,
    complexity :-quiteComplex,
    cost :<2.376,3.96,5.28,7.392> ).

proposedProject ( pid :p5,
    title :gims,
    duration :12,
    type :turnkey,
    area :games\_management,
    complexity :-notSoComplex,
    cost :3.6).

proposedProject ( pid :p2,
title :dss\_generator,
duration :\~aboutTwoYears,
type :research,
area :decision\_support,
complexity :\~moderatelyComplex,
cost :<1.35,1.8,1.8,2.25> ).

Enter n - next alt | s - skip unit | c - commit : n

Decision Unit :selectProjects Alternative # 2

Rank value :<7.10099,8.91,10.23,12.567>

Precondition : [0.744195,1]

Postcondition : [1,1]

proposedProject ( pid :p1,
    title :dist\_dbms,
    duration :<36,36,48,48>,

<table><tr><td>type</td><td>:developmental,</td></tr><tr><td>area</td><td>:database,</td></tr><tr><td>complexity</td><td>:~quiteComplex,</td></tr><tr><td>cost</td><td>:&lt;2.376,3.96,5.28,7.392&gt; ).</td></tr><tr><td>proposedProject ( pid</td><td>:p5,</td></tr><tr><td>title</td><td>:gims,</td></tr><tr><td>duration</td><td>:12,</td></tr><tr><td>type</td><td>:turnkey,</td></tr><tr><td>area</td><td>:games_management,</td></tr><tr><td>complexity</td><td>:~notSoComplex,</td></tr><tr><td>cost</td><td>:3.6).</td></tr><tr><td>proposedProject ( pid</td><td>:p6,</td></tr><tr><td>title</td><td>:expsys_shell,</td></tr><tr><td>duration</td><td>:~about_18_months,</td></tr><tr><td>type</td><td>:research,</td></tr><tr><td>area</td><td>:artificial_intelligence,</td></tr><tr><td>complexity</td><td>:~complex,</td></tr><tr><td>cost</td><td>:&lt;1.125,1.35,1.35,1.575&gt; ).</td></tr></table>

Enter n - next alt | s - skip unit | c - commit : n

Activate command continues to display the alternatives (with the next option) unless either all the alternatives are exhausted or the user skips/commits.

## References

[1] J.F. Baldwin, An Uncertainty Calculus of Expert Systems, in: E. Sanchez and L.A. Zadeh, Eds., Approximate Reasoning in Intelligent Systems, Decision and Control (Pargamon Press, 1987).

[2] R.E. Bellman and L. Zadeh, Decision-Making in a Fuzzy Environment, Management Science 17, No. 4 (1970) 141–164.

[3] H.K. Bhargava and R. Krishnan, Computer-Aided Model Construction, Decision Support Systems 9 (1993) 91–111.

[4] R.W. Blanning, Expert Model Base Systems: Research Directions, in: C.W. Hosapple and A.B. Whinston, Eds., Recent Developments in Decision Support Systems (Springer-Verlag, Berlin, 1993) 211–244.

[5] N. Bolloju, Modelling of Imprecise and Uncertain Information, in: N. Prakash, Ed., Current Trends in Management of Data (Tata-McGraw Hill, New Delhi, 1989).

[6] N. Bolloju, A Fuzzy Rule-based Decision Support System Environment, PhD Thesis (University of Hyderabad, 1991).

[7] N. Bolloju, A Calculus for Fuzzy Queries on Fuzzy Entity-Relationship Model, Proceedings of the Fourth International Conference for Young Computer Scientists, ICYCS 1995, Beijing.

[8] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Developments in Decision Support Systems, Advances in Computers, Vol. 23 (Academic Press, 1984).

[9] B. Chandrasekaran, T.R. Johnson and J.W. Smith, Task-Structure Analysis for Knowledge Modeling, Communications of the ACM 35, No. 1 (1992) 124–137.

[10] S. Chari and R. Krishnan, Towards a Logical Reconstruction of Structured Modeling. Decision Support Systems 10 (1993) 301–317.

[11] P.P. Chen, The Entity-Relationship Model: Toward a Unified View of Data, ACM Trans. on Database Systems 1 (1976) 9-36.

[12] W.J. Clancey, Heuristic Classification, Artificial Intelligence 27 (1985) 289–350.

[13] W.J. Clancey, Viewing Knowledge Bases as Qualitative Models, IEEE Expert (1989) 9–23.

[14] W.J. Clancey, Notes on Heuristic Classification, Artificial Intelligence 59 (1993) 191–196.

[15] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987) 547–588.

[16] A.M. Geoffrion, FM/SM: A Prototype Structured Modeling Environment, Management Science 37, No. 12 (1991) 1513–1538.

[17] R. George, B.P. Buckles and F.E. Petry, Modelling Class Hierarchies in the Fuzzy Object-Oriented Data Model, Fuzzy Sets and Systems 60 (1993) 259–272.

[18] S.-Y. Huh, Modelbase Construction with Object-Oriented Constructs, Decision Sciences 24, No. 2 (1992) 409–434.

[19] I. Itzkovich and L.W. Hawkes, Fuzzy Extension of Inheritance Hierarchies, Fuzzy Sets and Systems 62 (1994) 143–153.

[20] D. Jung and J.R. Burns, Connectionist Approaches to Inexact Reasoning and Learning Systems for Executive and Decision Support, Decision Support Systems 10 (1993) 37–66.

[21] M. Klein, Research Issues for Second Generation Knowledge Based DSS, in: C.W. Hosapple and A.B. Whinston, Eds., Recent Developments in Decision Support Systems (Springer-Verlag, Berlin, 1993) 337–359.

[22] M.L. Lenard, An Object-Oriented Approach to Model Management, Decision Support Systems 9 (1993) 67–73.

[23] J. McCarthy, Generality in Artificial Intelligence (Turing Award Lecture), Communications of ACM 30, No. 12 (1987).

[24] W.A. Muhanna, An Object-Oriented Framework for Model Management and DSS Development, Decision Support Systems 9 (1993) 217–229.

[25] W.A. Muhanna, SYMMS: A Model Management System that Supports Model Reuse, Sharing, and Integration, European Journal of Operations Research 72 (1994) 214–243.

[26] R. Pfeiffer and H.J. Luthi, Decision Support Systems and Expert Systems: A Complementary Relationship?, in: H.G. Sol et al., Eds., Expert Systems and Artificial Intelligence in Decision Support Systems (Reidel, 1987).

[27] P. Piela, R. McKelvey and A. Westerberg, An Introduction to the ASCEND Modeling System: Its Language and Interactive Environment, Journal of Management Information Systems 9, No. 3 (1992–1993) 91–121.

[28] H. Prade, A Quantitative Approach to Approximate Reasoning in Rule-based Expert Systems, in: L. Bolc and M.J. Coombs, Eds., Expert System Applications (Springer-Verlag, Berlin, 1985).

[29] H. Prade, A Computational Approach to Approximate Reasoning and Plausible Reasoning with Applications to Expert Systems, IEEE Transactions on PAMI PAMI-7, No. 3 (1985).

[30] S.A. Raghavan and D.R. Chand, A Perspective on Decision Support Systems, Technical Report (Bentley College, Waltham, MA, 1988).

[31] S. Raghunathan, R. Krishnan and J.H. May, MODFORM: A Knowledge-based Tool to Support the Modeling Process, Information Systems Research 4, No. 4 (1993) 331–358.

[32] D.S.W. Tansley and C.C. Hayball, Knowledge-Based Systems Analysis and Design (Prentice-Hall, 1993).

[33] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, Transactions of the Fifth International Conference on DSS (DSS '85), 1985.

[34] A. Sen, A.S. Vinze and S.F. Liou, Construction of a Model Formulation Consultant: The AEROBA Experience, IEEE Trans. on SMC 22, No. 5 (1992) 1220–1232.

[35] A.S. Vinze, A. Sen and S.F. Liou, AEROBA: A Blackboard Approach to Model Formulation, Journal of Management Information Systems 9, No. 3 (1992–1993) 123–143.

[36] B.J. Wielinga, A. Th. Schreiber and J.A. Breuker, KADS: A Modelling Approach to Knowledge Engineering, Knowledge Acquisition 4 (1992) 5–53.

[37] J. Yen and J. Lee, A Task-Based Methodology for Specifying Expert Systems, IEEE Expert (1993) 8–15.

[38] L. Zadeh, Outline of a New Approach to the Analysis of Complex Systems and Decision Processes, IEEE Transactions Systems, Man, and Cybernetics, SMC-3 (1973) 28–44.

[39] L. Zadeh, Fuzzy Sets as a Basis for a Theory of Possibility, Fuzzy Sets and Systems 1 (1978) 3–28.

[40] L. Zadeh, The Role of Fuzzy Logic in the Management of Uncertainty in Expert Systems, Fuzzy Sets and Systems 11 (1983) 199–227.

[41] L. Zadeh, Knowledge Representation in Fuzzy Logic, IEEE Transactions on Knowledge Engineering 1, No. 1 (1989) 89–100.

![](/api/attachments/JPDXZCH2/fulltext/images/75e09e8741b166d88dce5972368f866542a4dde71565703e933f8a64bf62627e.jpg)

Narasimha Bolloju is an Assistant Professor of Information Systems at the City University of Hong Kong, Hong Kong. He received his Ph.D. in Computer Science from the University of Hyderabad in 1991. His research interest are in database management, object-oriented systems, and intelligent decision support systems. Prior to joining City University of Hong Kong in 1993, he has been involved in various information systems consultancy projects for over a decade.
