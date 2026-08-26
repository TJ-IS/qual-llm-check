---
otero_id: 17764
otero_key: "YD3PKDJ3"
title: "Knowledge acquisition as a constructive process a methodological issue"
authors: "Bernard Le Roux"
year: "1996"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(96)00016-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge acquisition as a constructive process A methodological issue

Bernard Le Roux \*

Laforia-IBP UPMC, Tour 46-0-4, place Jussieu, 75252 Paris Cedex, France
Onera Des-Sia, B.P. 72, 92320 Chatillon Cedex, France

## Abstract

This paper is concerned by the construction of the conceptual model of an expertise. The aim is to provide a principled approach to knowledge modelling, integrating model construction and knowledge elicitation. The proposed approach is derived from KADS and ACKnowledge's GDM. The paper presents the specification of a software environment for knowledge modelling and elicitation.

Keywords: Knowledge acquisition; Modelling; Elicitation; Knowledge-based systems; Model

## 1. Introduction

There is a widespread consensus in the Knowledge Acquisition (KA) community towards the need of a more principled approach. Over the past years, many activities in this field provide such foundations, KADS-2[4] and VITAL [8,5] in Europe, the Knowledge Sharing initiative [3] in the States. These researches emphasise on the necessity of modelling to drive elicitation.

The first section of this paper presents some considerations about our approach combining modelling and elicitation. The second part makes some statements about synthesis tasks because our example in Section 3 is the construction of a particular synthesis model. Our conclusion is about our work at present and in the future.

## 2. Considerations about our approach

This paper is concerned by the construction of the conceptual model of an expertise. The design and implementation problems are not directly under consideration.

Our approach is derived both from KADS and from the Generalised Directive Models approach (GDM) advocated in the framework of the European Esprit project ACKnowledge [9]. We present briefly the background of our approach.

## 2.1. A modelling language

The basic idea of the GDM is to consider the models for KA as ‘sentences’ of a modelling language. Accordingly, the goal is to construct a generative grammar able to support the writing of such ‘sentences’. This grammar is the heart of a modelling tool driving the selection and refinement of a model according to the features and domain knowledge of an application.

The modelling categories: We consider the need of four categories to model the reasoning process corresponding to an expertise.

\- Firstly, the Task Structure, a representation of the task decomposition of the application, the root of the decomposition tree is the application as a whole, then the subtasks at different levels, the leaves are the primitive inferences.

\- Secondly, the Inference Structure, a graph representing the inferences realised by the system, and the roles that denote pieces of knowledge used by these inferences.

\- Thirdly, the Control Structure, a sort of pseudocode that represents the control over inferences, using control operators that entail different paths of inference according to the case during resolution.

\- Fourthly, the Meta-Domain, that represents the domain statements related to the inferences realised by the system (e.g., an inference entails the use of a causal model, or a conceptual hierarchy, and so on).

Role Type Definition: Looking at the modelling task in all its bearings implies the consideration of different types of roles (see notations on Fig. 1).

A Static Role “points to knowledge elements that are being used in the problem solving process, but are not affected by it: e.g., causal knowledge . . .” [10]. It is a foundation stone for resolution (e.g., a decomposition model for systematic diagnosis), all related knowledge must be elicited.

A Dynamic Role “‘points to knowledge elements that are being manipulated in the problem solving process: e.g., intermediate results’”. [10] It corresponds to an intermediate step of the resolution, a result of an inference (e.g., the role hypothesis for systematic diagnostic).

Initial case data for the actual problem to solve (e.g., complaint for systematic diagnosis) corresponds to a Case Role. The related elicitation is a part of the specification of the user interface. It states about the terms used by transfer primitives that must be related to each Case Role while not appearing in the inference structure.

![](/api/attachments/YD3PKDJ3/fulltext/images/612196e0bc4dad8334306aa037e53200ec09f7a58abadf3c936b55375a1cd3cd.jpg)  
Fig. 1. The three types of roles: notations.

![](/api/attachments/YD3PKDJ3/fulltext/images/81f2cbb0a8300b4b12b7cdc32ff3a0e108d574b6c1d6401dc8ceaa567d512cfa.jpg)  
Fig. 2. The spiral of model construction and knowledge elicitation.

## 2.2. The knowledge acquisition process

This is to emphasise the difference between the KA process according to KADS (two strongly separate phases, first select a model, second proceed to KA) and according to our approach.

Fig. 2 shows the spiral of the combined process of model construction and knowledge elicitation.

Bootstrap models: The initial model to begin KA is very simple, say coarse grained. The features of the application task to select the model may be very slight, it is nevertheless possible to begin model based KA.

Of course, the model doesn't provide very useful guidance, as it is coarse grained, while the special interest of our approach is that the rewrite rules of our context sensitive grammar supports the refinement of the models. A bootstrap model selection is only related to the class of the application under consideration. It is never related to any consideration of the method that the target KBS will use to solve the application problem. We avoid to mix a classification over the different applications and a classification over the methods, knowing what is the type of the solution is different of knowing how to compute it.

A manageable scheduling on KA: A scheduling on KA is possible and useful. The models provided in the framework of a methodology are supposed to permit the KA task's organisation. One way to organise this task is to know what is the most important to acquire at some point in time, and how to acquire it.

In our approach the model is progressively refined and constructed, thus, the dependencies between pieces of knowledge come gradually into view. This gradual process provides a manageable scheduling for KA.

Considering the whole construction of the interpretation model: The only model that handled the ACKnowledge GDM [9] was the inference structure. The task structure and the control structure were never considered. We assume that the task structure, and the information that it embodies, has a great importance to provide guidance for KA. Neglecting this point during all the cycles of refinement and acquisition is a problem. Furthermore, when we reach the end of the modelling and acquisition task, it remains the whole problem of control acquisition, often underlined as a difficult problem in KA. Our approach overcomes this limitation of the early GDM.

Locality principle: The rules of our grammar apply on a fragment of a model, the general inputs and the general output of the fragment under consideration remain after the refinement, eventually further specified. The transformation remains local, more global transformations may entail many difficulties to manage the models.

Syntax of the Rules of our Grammar: Components of a rewrite rule:

\- Rule Name: Only a mnemonic.

\- Rule Index: Used to compute a first subset of rules by pattern matching. The index is an inference, embodying one or more input roles, one operator and one output. A role named Input or Output, or an operator named Infer, in the index are universal substitutions for pattern matching.

\- Rule Conditional Part (CP): It is the conditional part allowing the application of the rule when it is satisfied, either according to the specification of the current model under refinement, or according to the answers of the knowledge engineer. The questions are related to unsatisfied premises. The answers are related to the application being modelled. The different attributes used are: qualification (about a pragmatic feature of domain knowledge related to a role: a set being large or a structure being complex), semantic-type, syntactic-type, criterion (about an operator and generally specifies a static role used by this operator to perform), current-goal (specifies the goal of an operator: a teleological view) and method (a high level description of how an operator or a set of operators performs). Semantic-type and syntactic-type have been defined.

\- Inference Structure (IR), Task Structure (TR) and Goal Decomposition (GDR) Rewriting: The three items above are the rewritings of the corresponding parts of the model if the rule is applied.

\- Role Specification Rewriting: This specification, if any, is about the role type, the syntactic type and semantic types of the knowledge related to a role.

## 2.3. Domain modelling

The rationale of an Interpretation Model, or Problem Solving Method (PSM), often depends on the meta-view of the domain. Moreover, such models can be an effective guidance for KA in so far as they provide the model schema of the domain used to organise the knowledge that their inferences handle. In contrast, the consequence of the ambiguity or absence of the model schema of the domain used by a PSM is to forbid a good understanding of the method. Furthermore, domain modelling allows to tackle the interaction problem.

First Definition of a Syntax: The first syntactic characterisation of the knowledge related to a role is Set (of entities) or Element (entity). E.g., we may have a set of instances, in a domain of diagnosis of failure for cars, as following: {(Trade-mark: Citroën - Model: BX19TRD - Year: 1987) (Trade-mark: Ford - Model: Fiesta - Year: 1985)...}, this set allowing to choose a related system model in a universum of system models. The syntax allows to specify the entity that are:

\- A concept is defined as (name - attribute1: range of values (optional): type (optional) -- att.N):. E.g., in the domain of life insurance, the concept Client will be defined as following: (Client - Name: []: symbol - Age: [1 to 100]: interval of integers - Work: [manual-labour - head-work]: discrete symbols - Domain of Work: [building - car-factory - ...]: discrete symbols - and so on).

\- An instance of a concept has the corresponding attributes of this concept with a value. E.g., an instance of a client wanting to buy a life insurance, will be defined as: (Client - Name: O'Shaughnessy: symbol - Age: 32: integer - Work: head-work: symbol - Domain of Work: import-export-trade: symbol - and so on).

\- A value is an attribute of an instance having a value. E.g., a value will be defined as: (Age: 36: integer).

\- An expression is a formula. E.g., in the domain of repairing for electronic consumer products we may have the following formula (a test procedure for a subsystem or a component): (power supply test: IF test point N°47 of printed circuit Ref. AX3247 provides voltage = 15 volts DCC THEN power supply is OK). This is a logical formula.

\- A structure is a collection of concepts with relations between these concepts. E.g., in the domain of repairing for electronic consumer products we may have this structure in the case of a television set that doesn't work (see Fig. 3).

First Definition of a Semantic: A first level of semantic characterisation of knowledge related to a role depends on the syntax of this knowledge, as shown by the previous examples about structure and expression.

A first semantic characterisation of a structure is homogeneous if there is only one relation involved in the structure, or heterogeneous if there are several different relations. The second semantic characterisation is about the type of relation (or relations) involved in the structure: (is-a, can-cause, part-of, has, entail).

An expression can be semantically characterised according to its type (logical formula, calculus formula). E.g., in a model of systematic diagnosis we have a static role, system model, the knowledge corresponding to this role having for syntactic type structure and for semantic type homogeneous/part-of (as the structure given previously).

A second level of semantic characterisation of the knowledge related to a role depends on the model ontology. The model ontology provides meta-terms about a model schema. About the previous example of a structure (television set), a model ontology provides terms such as component for the leaves of the decomposition tree, sub-system for the intermediate nodes and system for the root of the tree.

![](/api/attachments/YD3PKDJ3/fulltext/images/9dd26ab52c0cc3042eac16c80420f7e68b75f1886d279fd92dcb2bc2328b9be3.jpg)  
Fig. 3. An example of a part-of structure.

![](/api/attachments/YD3PKDJ3/fulltext/images/1af3baec7385d9467f743d084399751bdad5855d476de4a59ff070630d48325c.jpg)  
Fig. 4. KADS classification for synthetic tasks.

## 3. Considerations about synthesis tasks

As our example is the development of a model for a synthesis task, according to an hypothetical application that could be for example Sysiphus2 problem (VT-elevator), this part is about synthesis tasks.

## 3.1. KADS views on synthesis

The differentiation between types of tasks, based on the consideration of the structure and elements of the artefact to design (the solution provided by a KBS), according to the KADS tree, is shown on Fig. 4.

\- Elements and structure: Having a definition of all the elements used for the design and of all the relationships between elements (the structure), then the task is Transformational Design, a subclass of Routine Design.

\- Elements: Having only the definition of the elements, then two tasks are proposed, Configuration or Scheduling. In Configuration, a set of elements is available, the task is to assemble the elements to obtain a specified behaviour. In Scheduling, the goal is usually to reach an optimum for one or several criteria depending on the organisation of the elements in time. These are two sub-classes of Routine Design.

\- Structure: Having only the definition of the structure the task is Refinement Design. This definition seems to us quite strange because we don't understand how it's possible to have the relationships between elements while not having the elements. We will consider this class of task as a first sub-class of Open Design. Then the whole set of synthesis tasks is shared into two sub-sets, Routine Design and Open Design.

![](/api/attachments/YD3PKDJ3/fulltext/images/2669b8559aa75f8b6aa03747a9a43e0f707798eac04b8b3d9a2e0168bdf3ae21.jpg)  
Fig. 5. The principles of the KADS classification.

\- None: Whether we have nor the elements neither the structure then two tasks are proposed, Planning, and Open-ended Design? These two classes are other sub-classes of Open Design.

Fig. 5 summarises these considerations.

## 3.2. Chandrasekaran views on synthesis

Let us consider now the work of Chandrasekaran about design. A design problem is a search problem in a very large space, “only a vanishingly small number of objects in this space constitute even ‘satisficing’, not to speak of optimal, solutions. What is needed to make design practical are strategies that radically shrink the search space” [2]. There is a relationship between the terms used by Chandrasekaran and the attempt to classify design in the KADS approach, the former speaks of a “set of primitive components” which is available while the latter speaks of known elements, the former speaks of a “repertoire of primitive relations or connections” while the latter speaks of known structure.

The main difference is related to the KADS project to specify disjoined classes of design. The consequence is to consider strong criteria to define these classes. We think that it is possible to define such classes, but a realistic assumption leads us to consider that they are not disjoined.

The definition of design tasks provided in [2] is as following:

"The design problem is specified by:"

![](/api/attachments/YD3PKDJ3/fulltext/images/8f86aa3d8fe7a5fea830b002f5b34836354739db43a75e94a924bf144f6f4793.jpg)  
Fig. 6. An example of a part-of structure.  
- a set of functions (explicitly stated by the design consumer as well as implicit ones defined by the domain) to be delivered by an artefact and a set of constraints to be satisfied; and  
- a ‘technology’, i.e., a repertoire of components assumed to be available and a vocabulary of relations between components.”  
There is a close mapping between the terms used by Chandrasekaran, as “set of functions and constraints” and “technology”, and the terms we use to specify Routine Design, as “set of global criterion” and “set of elements”.

## 3.3. Discriminating the types of synthesis

Let us consider how a grammar provides a first model for a synthesis task through different steps of refinement. The beginning model is the more general model for design (see Fig. 6).  
This very coarse grained model needs to be specified further according to discriminating elements allowing to differentiate between different types of synthesis tasks.  
The first rule discriminates applications according to the availability of an almost complete definition of the elements used in design. This rule leads to models of Routine Design. R55 allows to develop models of Open Design, the dual of the previous rule (see Table 1). Open Design and Routine Design are then different classes.

<table><tr><td>Name: R54</td><td>Index: input/synthesis/output</td></tr><tr><td colspan="2">CP: main design elements::qualification::available</td></tr><tr><td colspan="2">IR: input/routine-design/output</td></tr><tr><td colspan="2">TR: routine-design (input, output)</td></tr><tr><td colspan="2">GDR: synthesis (routine-design)</td></tr><tr><td>Name: R55</td><td>Index: input/synthesis/output</td></tr><tr><td colspan="2">CP: main design elements::qualification::unavailable</td></tr><tr><td colspan="2">IR: input/open-design/output</td></tr><tr><td colspan="2">TR: open-design (input, output)</td></tr><tr><td colspan="2">GDR: synthesis (open-design)</td></tr></table>

Table 3  
Table 2

<table><tr><td colspan="2">Table 2Two GDM rules</td></tr><tr><td>Name: R56</td><td>Index: input/routine-design/output</td></tr><tr><td colspan="2">CP: artefact to design structure::qualification::known</td></tr><tr><td colspan="2">IR: input/transformational-design/output</td></tr><tr><td colspan="2">TR: transformational-design (input, output)</td></tr><tr><td colspan="2">GDR: routine-design (transfo.-design)</td></tr><tr><td>Name: R57</td><td>Index: input/routine-design/output</td></tr><tr><td colspan="2">CP: artefact to design structure::qualification::unknown</td></tr><tr><td colspan="2">IR: input/global-design/output</td></tr><tr><td colspan="2">TR: global-design (input, output)</td></tr><tr><td colspan="2">GDR: routine-design (global-design)</td></tr></table>

The rules allowing to refine a model provided by the application of R54 are shown in Table 2.

The way to constrain the assembly of the elements is a set of global characters of the target system to design, then we christen this class Global Design (e.g., a set of expected behaviours of the target system).

We have now to share this class of Global Design into different sub-classes, Configuration, Allocation, Scheduling and Engineering Design.

The alternative rules for different design systems are shown in Table 3.

## 4. Constructing a model of P&R

We look now at a model building of the “propose and revise” PSM. Our starting model results of R53, R54, R57 and R61. The question occurring is: “What is the method used to reach the solution?”. R62 answers this (see Table 4).

<table><tr><td colspan="2">Rules for models of configuration and scheduling</td></tr><tr><td>Name: R58</td><td>Index: input/Global-design/output</td></tr><tr><td>CP: criterion of design :: qualification :: behaviour</td><td></td></tr><tr><td>IR: input/configurate/output</td><td></td></tr><tr><td>TR: configurate (input, output)</td><td></td></tr><tr><td>GDR: global-design (configuration)</td><td></td></tr><tr><td>Name: R60</td><td>Index: input/Global-design/output</td></tr><tr><td>CP: global design :: current goal :: correspondence construction between two input sets &amp; design :: criterion :: constraints on this correspondence</td><td></td></tr><tr><td>IR: input1 &amp; input2/allocate/output</td><td></td></tr><tr><td>TR: allocate (input1 &amp; input2, output)</td><td></td></tr><tr><td>GDR: global-design (allocation)</td><td></td></tr><tr><td>RSR: input = input1 + input2</td><td></td></tr><tr><td>Name: R59</td><td>Index: input/Global-design/output</td></tr><tr><td>CP: design :: criterion :: time dependant assembly</td><td></td></tr><tr><td>IR: input/schedule/output</td><td></td></tr><tr><td>TR: schedule (input, output)</td><td></td></tr><tr><td>GDR: global-design (scheduling)</td><td></td></tr><tr><td>Name: R61</td><td>Index: input/Global-design/output</td></tr><tr><td>CP: global design :: current goal :: value assignment &amp; global design :: criterion :: constraints on values</td><td></td></tr><tr><td>IR: input/engineering-design/output</td><td></td></tr><tr><td>TR: engineering-design (input, output)</td><td></td></tr><tr><td>GDR: global-design (engineering-design)</td><td></td></tr><tr><td colspan="2">Table 4A rule for engineering design model</td></tr><tr><td>Name: R62</td><td>Index: input/Engineering-design/output</td></tr><tr><td>CP: Eng.-design :: method :: step by step backtracking</td><td></td></tr><tr><td>IR: input/propose/output &amp; output/revise/revision &amp; revision/modify/output &amp; revision/modify/input</td><td></td></tr><tr><td>TR: While input [propose(input, output) revise (output, revision) modify (revision, output) modify (revision, input)]</td><td></td></tr><tr><td>GDR: eng.-design (propose revise modify modify))</td><td></td></tr></table>

Table 5  
A rule for propose and revise

<table><tr><td>Name: R63</td><td>Index: input/Engineering-design/output</td></tr><tr><td colspan="2">CP: Eng.-design:: method:: global solution revision</td></tr><tr><td colspan="2">IR: input/propose/output/revise/output</td></tr><tr><td colspan="2">TR: While input [propose (input, output)] revise (output, output)</td></tr><tr><td colspan="2">GDR: engineering-design (propose revise))</td></tr></table>

The model provided by R62 is based on the hypothesis that the problem solving process is a loop, each partial solution is assessed and, if not convenient, is revised. This process could be shared into two separate steps, first propose a global solution, second revise this solution if not convenient. R63 allows this solution (see Table 5).

R62 is applied, the model is transformed. Due to the length of the paper we do not draw the intermediate model resulting of rule application. R64 refines the Propose fragment (see Table 6).

R64 entails that the role input is compound. Then, the previous role input is shared into two new roles, design parameters and specification parameters.

The previous dependencies of input in the model under refinement are now duplicated for the two new roles replacing input. The model changes accordingly.

Knowledge Elicitation (KE): The elicitation task is about the set of design parameters, and the set of specification parameters, specifying the user interface of the KBS. We have also to acquire the whole set of assignment procedures, a static role, to each element of the design parameters set must correspond at least one procedure.

R15, allowing to refine a model where a role has for related knowledge a huge set of elements is applied and the fragment assignment-procedures/assign-value/... is refined. To answer “What is the criterion for selection?” R35 applies (see Table 7).

This new role, calculus parameters, being the criterion to select a calculus expression, is then a set of instances used by the calculus expressions to perform.

The selection of an expression is possible if all its terms are defined. “Does it already exist in the previous model a role or several roles that are these calculus parameters?” Yes and these roles are specification parameters and valued parameters. Then the mapping between calculus parameters and these roles is done.

<table><tr><td colspan="2">A rule to refine the propose fragment</td></tr><tr><td>Name: R64</td><td>Index: input/propose/output</td></tr><tr><td colspan="2">CP: input:: syntactic type :: set of concepts &amp; instances &amp; output :: syntactic type :: set of instances &amp; Propose :: current goal :: input concepts value assignment</td></tr><tr><td colspan="2">IR: input/assign-value/output</td></tr><tr><td colspan="2">TR: assign-value (design-par. &amp; specification-par. &amp; assignment-procedures, valued-parameters)</td></tr><tr><td colspan="2">GDR: propose (assign-value)</td></tr><tr><td colspan="2">Table 7GDM refinement rules</td></tr><tr><td>Name: R15</td><td>Index: input/infer/output</td></tr><tr><td colspan="2">CP: input:: syntactic type :: set of entities &amp; input :: qualification :: large set</td></tr><tr><td colspan="2">IR: input/select/relevant input/infer/output</td></tr><tr><td colspan="2">TR: select (input, rel. input) infer (rel. input, output)</td></tr><tr><td colspan="2">GDR: infer (select)</td></tr><tr><td colspan="2">RSR: relevant input syntactic &amp; semantic type = input entity syntactic &amp; semantic type</td></tr><tr><td>Name: R35</td><td>Index: input/select/output</td></tr><tr><td colspan="2">CP: input:: syntactic type :: set of expression &amp; input :: semantic type :: calculus &amp; Select :: criterion :: available calculus terms</td></tr><tr><td colspan="2">IR: input &amp; calculus terms/select/output</td></tr><tr><td colspan="2">TR: select (input &amp; calculus terms, output)</td></tr><tr><td colspan="2">RSR: calculus terms syntactic type = instances</td></tr></table>

Table 8

<table><tr><td colspan="2">To refine the revise fragment</td></tr><tr><td>Name: R65</td><td>Index: input/Revise/output</td></tr><tr><td colspan="2">CP: revise:: current goal :: constraint satisfaction &amp; revise :: criterion :: change a value previously assigned</td></tr><tr><td colspan="2">IR: input &amp; constraints/verify/violated constraint &amp; repairs/select/output</td></tr><tr><td colspan="2">TR: verify (input &amp; constraints, viol. constraint) select (violated constraint &amp; repairs, output)</td></tr><tr><td colspan="2">GDR: revise (verify, select)</td></tr><tr><td colspan="2">RSR: constraints &amp; repairs syntactic type = set of expressions &amp;semantic type = logical; violated constraint syntactic type = expression &amp; semantic type = logical</td></tr></table>

Table 9

<table><tr><td colspan="2">A last refinement rule</td></tr><tr><td>Name: R66</td><td>Index: input/Modify/output</td></tr><tr><td colspan="2">CP: modify::current goal::truth preserving</td></tr><tr><td colspan="2">IR: input &amp; dependencies/modify/output</td></tr><tr><td colspan="2">TR: While dependencies modify (input &amp; dep., output)</td></tr><tr><td colspan="2">RSR: dependencies syntactic type = set of expressions &amp; semantic type = logical</td></tr></table>

The refinement of the sub-task Revise is now under consideration. The first rule applied is R65 (see Table 8).

The model resulting allows to revise the two types of elements used to compute parameters, specification parameters and valued parameters. The former corresponds to the idea that if a legal solution cannot be reached then it is possible to change the specifications, it is the case when a design problem is too constrained to allow a solution. The latter corresponds to the idea that it is possible to refine the value of a parameter in such a way that the constraints are satisfied.

KE: The elicitation task is to acquire the knowledge corresponding to the static roles constraints and repairs. We must at least have a constraint for each possible valued parameter, then we must acquire a constraint for each design parameter. Whenever the set of constraints has been acquired, then we must acquire a repair for each constraint, a repair being a logical expression linking a violated constraint with a change of value of some parameter. If the revision is about a previous valued parameter then the related modify inference has to change the parameter under consideration. If the revision is about a specification parameter then the related modify has to change the specification under consideration.

![](/api/attachments/YD3PKDJ3/fulltext/images/bd5a0590bcf954ee4efff3cda6cb2b029b98e9ee4ed34e3e27c72de8225877c1.jpg)  
Fig. 7. The inference structure of the final model of Propose and Revise.

![](/api/attachments/YD3PKDJ3/fulltext/images/6ac9926528a520847ad5a1db20158e4011e182b77f40e34da4d9c374a4cbaa8b.jpg)  
Fig. 8. The goal decomposition of the final model of Propose and Revise.

As the goal is to preserve the truth, then it is necessary to recurrently update the roles valued parameters and design parameters (e.g., if a valued parameter is changed, all the parameters computed using its value are withdrawn from valued parameters and added to the set of design parameter to be computed again).

R66 (see Table 9) allows this refinement and the final model is shown in Figs. 7–9.

KE: The static role dependencies allows to know the consequences of a change of a valued parameter or a specification parameter on the two sets of valued parameters and design parameters. Of course, these dependencies are many and it is a tedious work to acquire it by hand, but according to the fact that we have the whole set of value assignment procedures, it's possible to make a recurrent computing of the set of dependencies related to a change.

About this model the question is: “Is it P & R as embodied in SALT?” (see [7]). We could say no.

The difference is related to two features of SALT.

The former is that SALT allows to overcome a contradiction between constraints and repairs (e.g., a constraint X is violated, related repair Y is applied, it entails that constraint Z is violated, related repair K is applied, it entails that constraint X is violated again and so on, an endless loop).

The latter is that SALT allows to reach a solution and to suppose that this solution is near optimality by using a total order on the repairs.

The latter feature of SALT may be added to the above model by applying again the rule R15 as the role repairs is a (large) set of expressions, the criterion being an order (total or partial) on the repairs, or another more knowledgeable criterion. The former feature of SALT is difficult to reach through this type of models because contradictions between constraints and repairs are often difficult to elicit.

To evidence such contradictions, SALT takes advantage of being a shell embodying either a KA module and a performance module allowing simulation.

## 5. Ongoing works

The writing of the grammar concentrates all the difficulties of our approach. We had an experimental approach to construct and develop the grammar. There is a large experience in the field of AI, and more particularly in KA, about PSM and KA models. The construction of a grammar is based on this experience. We have developed an empirical analysis of existing models of PSM (from the KADS library,

WHILE design parameter
[ SELECT (assignment proc. & specification-par. & valued parameters, relevant procedures)
ASSIGN-VALUE (design par. & specification-par. & relevant procedures, valued parameters)
VERIFY (valued parameters & constraints, violated constraint)
SELECT (violated constraint & repairs, revision)
WHILE dependencies [ MODIFY (revision, valued parameters) ]
WHILE dependencies [ MODIFY (revision, design parameters) ]
MODIFY (revision, specification parameters) ]

## TASK STRUCTURE

Fig. 9. The control structure of the final model of Propose and Revise.

Role Limiting Methods, Generic Tasks or other), and we have developed rules allowing the construction of such models while preserving their rationale (see [5]). This work has to be continued to improve the GDMs' grammar.

We use this grammar as grounding the competence of our tool prototype, christened TOMAOK that stands for TOwards a Modelling and Acquisition Organising Kernel. Several applications as Sysiphus-1 (room assignment), Sysiphus-2 (VT-elevator) or others are currently under realisation with this tool. We assess accordingly the limits of the existing grammar and improve it. This on going work allows both to refine the grammar and its specification and to improve our GDMs' tool.

## Acknowledgements

This research has been made in the framework of the European Esprit-II project VITAL P5365, and then partially funded by this project. We thank our partners in this project, and mainly Nigel Shadbolt and Kieron O'Hara from the University of Nottingham, and Phillippe Laublet and Jérôme Thomas from ONERA. We thank also the members of our research team at the University of Paris VI and more particularly Jean-Gabriel Ganascia.

## References

[1] A. Aamodt, B. Bredeweg, J. Breuker, C. Duursma, Ch. Lockenhoff, K. Orsvarn, J. Top, A. Valente and W. van de Velde, The Common KADS Library, Esprit Project P5248 KADS-II - KADS-II/T1.3/VUB/TR/005/1.0 - CEC Reference D1.3a (1992).

[2] B. Chandrasekaran, Design Problem Solving: A Task Analysis, AI Magazine 11 (1990).

[3] Th. Gruber, Ontolingua: A Mechanism to Support Portable Ontologies, Stanford University Knowledge Systems Laboratory Report (1992).

[4] R. de Hoog, R. Martil, B. Wielinga, R. Taylor and C. Bright, The Common KADS Model Set, Esprit Project P5248 KADS-II - KADS-II/WP I - II/RR/UvA/018/3.2 (1992).

[5] B. Le Roux, K. O'Hara, S. Outandy, N. Shadbolt, Ph. Laublet and E. Motta, The VITAL Library for Knowledge Modelling, Esprit II Project P5365 VITAL Document Reference DD215 (1993).

[7] S. Marcus, SALT: A Knowledge-Acquisition Tool for Propose-and-Revise Systems, in: S. Marcus, Ed., Automating Knowledge Acquisition for Expert Systems (Kluwer Academic Publishers, 1988).

[8] K. O'Hara, N. Shadbolt, Ph. Laublet, M. Zacklad, B. Le Roux and M. Mepham, Knowledge Acquisition Methodology, VITAL, Report VITAL/DD2.1.2, Esprit Project (1992).

[9] G. van Heijst, P. Terpstra, B. Wielinga and N. Shadbolt, Using Generalised Directive Models in Knowledge Acquisition, in: W. Althoff, B. Gaines, L. Schmalhofer, Eds., Current Developments in Knowledge Acquisition, Proceedings EKAW 92 (1992).

[10]B. Wielinga, G. Schreiber and J. Breuker, KADS: A Modelling Approach to Knowledge Engineering, Esprit Project P5248 KADS-II - KADS-II/T1.1/PP/UvA/008/1.0 (1991).

![](/api/attachments/YD3PKDJ3/fulltext/images/ea94c0b759d97210f0f3b02348bd12a4423f3c49bfa4e9c1825baeea76799157.jpg)

Bernard Le Roux was born in Paris in 1953. After having done his secondary studies in Paris and Toulouse, he studied both philosophy and electronics at the University of Toulouse. Then he joined a research laboratory of the French Thomson-CSF company. During the 12 years he spent in Thomson-CSF, he worked, for instance, on the inboard softwares for Airbus planes. He defended his thesis in computer science in 1994. He is currently research engineer

at ONERA (national French research laboratory for aeronautics and space). The author is mainly involved in research in Artificial Intelligence, knowledge engineering and knowledge intensive systems design, and cognitive sciences.
