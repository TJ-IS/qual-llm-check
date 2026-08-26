---
otero_id: 16891
otero_key: "HM5TBM59"
title: "Domain specific DSS tools for knowledge-based model building"
authors: "Meral Binbasioglu; Matthias Jarke"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90029-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Domain Specific DSS Tools for Knowledge-Based Model Building $^{1}$

Meral BINBASIOGLU \* and

Matthias JARKE \*\*

\* Krannert School of Management, Purdue University, West Lafayette, IN 47907, USA

\*\* Graduate School of Business Administration, New York University, 90 Trinity Place, New York, NY 10006, USA

The formulation of complex planning models, such as linear programming (LP) systems, is a difficult task that enjoys little support by current decision support systems. It is hypothesized that current artificial intelligence technology is insufficient to build generalized formulation tools that would be usable by OR-naive end users. As an alternative, this paper presents a domain-specific approach to knowledge-based model formulation which combines the use of 'syntactic' knowledge about linear programming with 'semantic' guidance by knowledge specific to some application domain. As a prototype of this approach, a model formulation tool for LP-based production management is being developed at New York University.

![](/api/attachments/HM5TBM59/fulltext/images/c94148397681cd6a9b22f26c3fb7aae9e4703d72d7184d1485e0ecc606e3250a.jpg)

Meral Binbasıoglu joined the faculty of the Krannert Graduate School of Management at Purdue University in 1986. She received a B.S. and an MBA in Management from Middle East Technical University in Ankara, Turkey, and is currently completing a doctoral thesis on knowledge-based methods for model formulation at New York University. Her research interests include decision support systems and artificial intelligence applications in business.

![](/api/attachments/HM5TBM59/fulltext/images/a7364ebabe21c4d7e8228019e4a040a332f6daa1221b756171cf84a43095f01e.jpg)

Matthias Jarke is an Associate Professor of Computer Applications and Information Systems at New York University and a Professor of Applied Computer Science at Johann Wolfgang Goethe - University, Frankfurt, West Germany. He received a doctorate in Economical Sciences, and Diplomas in Computer Science and Business Administration from the University of Hamburg, West Germany. In his research, Dr. Jarke investigates the optimal interaction of database systems with advanced application systems, such as decision support systems and knowledge-based expert systems. He has authored or edited four books, and published a number of articles on DBMS design and implementation, database interfaces, expert systems and databases, and cost-benefit studies of information systems.

## 1. Introduction

A Decision Support System (DSS) is a computerized system which utilizes knowledge about a particular application area to help decision makers working in that area to solve ill-structured problems [Bonczek et al. (1984)]. DSS need a number of content abilities [Holsapple and Moskowitz (1983)] to support the three stages of the decision making process (intelligence, design, and choice) identified by [Simon (1960)]. In this paper, we examine the content ability of model formulation which is required mostly in the design phase. Model formulation involves the following processes: to clarify and understand the problem; to invent, develop and analyze potential solutions to the problem; and to test the solutions for feasibility. In particular, we are interested in the question how general (i.e., application-independent) a DSS tool for model formulation can and should be made.

DSS generators attempt to offer generalized modelling tools that help managers formulate and solve decision problems. However, the kinds of models offered by such systems tend to be quite simple, involving, e.g., spreadsheet systems but no automatic solution-seeking. As shown in [Dhar (1984)], however, even the formulation and maintenance of large spreadsheet models may require substantial use of complex Artificial Intelligence (AI) tools.

The difficulties increase if the problem at hand requires the use of more sophisticated goal-seeking models, such as linear programming (LP). Managers typically use an intermediary to get such models built. With this approach, the process of formulating and executing a decision model tends to get quite lengthy and indirect, and the risk of misunderstandings increases. Therefore, it seems desirable to provide the manager with automatic model building tools usable by him directly, rather than through an intermediary.

The approach to model formulation we present in this paper combines structural knowledge about management science models, with application-specific knowledge about a particular domain of interest. The general case for this approach is made in section 2. Section 3 describes a knowledge base structure for the example model formulation tool we have chosen for this research: linear programming models for production management. The capabilities of such a combined knowledge representation technique are illustrated by a detailed example in section 4. Section 5 summarizes the discussion and points out current research directions.

## 2. Model Formulation Tools in Model Management

As pointed out in [Bonczek et al. (1984)], as well as in a recent survey by Hwang (1985), research in automatic or computer-aided model building is still in its early stages. Work in this area is typically described in the broader context of model management.

Three levels of model management capability can be distinguished [Bonczek et al. (1982)]. With the first modelling level, a user procedurally specifies the model's algorithm. As pointed out earlier, this option requires an intermediary if models become complex.

Under the second alternative, a user is familiar with a collection of pre-specified models available to the DSS and selects one of these for execution. User-friendly model manipulation languages can support this task. For example, Blanning (1985) presents a theory of model management where the user views a model as a virtual relation representing a mapping from input attributes to output attributes. Using relational operations, the user can synthesize more complex models from existing ones.

Under the third alternative, a user does not directly formulate or select a model; he or she may even be unaware that the DSS uses models in generating responses. Upon receipt of the user's problem description, an appropriate model is selected or composed by the DSS itself. For example, Sivasankaran and Jarke (1985) describe a system called the Actuarial Consulting System (ACS) that composes models in actuarial science (life insurance mathematics) from a library of stored formulas using AI techniques to search through a relational structure similar to Blanning's. Another system – outside the DSS area – based on this design principle of 'formulation by configuration' is the well-known expert system R1 [McDermott (1982)] which configures VAX computers. If the set of problems under consideration is too broad or unstructured to permit the definition of such a library, models must be formulated from scratch.

Model formulation from scratch consists of two steps: (a) identifying the appropriate modelling technique (e.g., LP, dynamic programming, etc.) and application domain boundaries, and (b) formulating the model within the chosen modelling/ domain combination. This paper is concerned with model formulation, i.e., task (b), for LP models; automatic model selection has also been studied recently [Hwang (1985)].

There are at least two approaches to building model formulation tools. The first approach relies on structural knowledge about a particular modelling tool. For example, Murphy and Stohr (1985) propose a LP model formulation tool based on a decomposition approach, relying on the inherent network structure of major portions in almost every large linear program. This tool is chiefly intended to support an operations research specialist in building very large LP models. For a managerial end user, such a system has the drawback that it does not remind the user of application domain-specific knowledge he may have to include. In other words, the 'structural knowledge' approach supports you in formulating a constraint but it does not tell you which constraints to formulate.

Experience with knowledge-based systems ('expert systems') in AI, the rapid growth of the market in tailored domain-specific software packages (i.e., databases for real-estate rather than generic DBMS), and recent work on the definition of Knowledge Base Management Systems [Mylopoulos and Brodie (1986)] all suggest that better model formulation support can be provided if the structural knowledge base component is augmented by an application knowledge base that guides the user not only in the syntactic but also in the semantic aspects of model formulation.

In the remainder of this paper, we describe a formulation tool that combines structural LP knowledge with application knowledge about production management. A PROLOG implementation of such a system is being developed at NYU within the context of a long-range research effort that studies the role of artificial intelligence in management information systems and decision support systems [Jarke and Vassiliou (1984)].

## 3. LP Models in Production Management: Knowledge Representation

## 3.1. Knowledge Base Structure and Systems Architecture

Linear programming is one of the most successful operations research methods for solving very large optimization problems. Fig. 1 illustrates the typical life cycle of linear program development and usage. In this paper, we are concerned with the first step of this life cycle, the conceptual development and symbolic (as contrasted to numeric) formulation of the model. The result of this model formulation step can then be turned over to any of a number of commercially available matrix generators, e.g., ECL or OMNI. Computerized tools are available for the checking and sensitivity analysis of existing models [Greenberg (1983)]. In contrast, the model formulation step has frequently been considered too fuzzy to be computerized effectively. This is one of the reasons why we propose the combined use of method and application knowledge to support this process.

![](/api/attachments/HM5TBM59/fulltext/images/45e00e9aecdb127952f24aa907947582ba03ea147494c1a00d764b9c6d5ab3a0.jpg)  
Fig. 1.

The system architecture is summarized in fig. 2. It divides the model formulation problem into three steps or levels, using different kinds of knowledge bases.

The context identification step accepts the input problem description, and identifies the problem area within a knowledge base for the business application (here: production management). It then refines - interactively if necessary - the problem description by identifying all the relevant business objects and the relationships among them.

The problem formulation step instantiates the context identified in the previous stage, determines the decision variables using an additional knowledge base of structural knowledge, assigns indices to the variables, and constructs the format of the constraints and the objective function, using dummy parameter values.

![](/api/attachments/HM5TBM59/fulltext/images/f16f36ae2644d594b7ea9c5dafe283cb9e31373c3aa348c18978bb9d3c99219a.jpg)  
Fig. 2.

Finally, the model building step selects and accesses (or computes) the parameters that go with the constraints and objective function. First, each parameter is semantically identified by analyzing the left-hand side and right-hand side components of the constraint. Then, its unit of measure is determined syntactically based on the units of the components. This uses a third knowledge base for the transformation of units of measure and similar relationships.

The idea behind this hierarchical design of the problem solving steps is to approach the problem with a holistic view [Stefik (1980)]. This will help formulating the problem without optimizing any subpart of it at the expense of the whole. The information at any level determines and coordinates the activities in the next level. A blackboard is used to store intermediate results, and access to a matrix generator will be provided in case the user wants to see the solution to a partially formulated problem.

In the following subsections, a brief overview of the two knowledge sources of the system will be given. Then, a knowledge representation scheme tailored to the integration of these knowledge sources will be described.

## 3.2. LP Knowledge Bases

Mathematical models are symbolic representations which incorporate the essential features of actual problems. In particular, a linear programming (LP) problem is a problem of minimizing or maximizing a linear function in the presence of linear constraints. It can be represented mathematically as

Maximize/minimize $\Sigma_{j}c_{j}X_{j}$

subject to $\sum_{j}a_{i,j}X_{j} < = b_{i}$ for each $i$ ,

$$
X _ {j} > = 0 \text {   for   each   } j,
$$

where $i = 1,\dots ,m,j = 1,\dots ,n.$

The decision variables, or activity levels, to be determined are represented by $X_{1}, X_{2}, \ldots, X_{n}$ . $c_{1}, c_{2}, \ldots, c_{n}$ represent the cost or return coefficients that these variables take. The coefficients $a_{i,j}$ are called the technological coefficients.

Mathematically speaking, the problem of model formulation is the problem of determining the index sets i and j, the decision variables, and the coefficient values. There are many ways to formulate such models. As Charmes and Cooper (1967) point out there is a danger for models to be inadequate, to overlook essentials, or to incorporate extraneous features and thereby micropresent the situation.

There are two knowledge bases associated with LP knowledge. The first one contains knowledge about problem types, defining index sets, naming and selecting variables, etc. The second one is concerned with the actual procurement and correct interpretation of parameter values.

## 3.3. Application Knowledge Base

The system's domain is resource allocation in production planning. This covers a broad range of problems, such as the selection and allocation of resources, the relative composition and distribution of marketable products, the allocation of resources to products, or any combination of them. If we want a DSS tool to understand business at the level that it can help formulate management science models we have to equip it with real-life knowledge about business.

The system has to know the types of resources, their properties, the type or actions that operate on these resources, and possible relationships among these components. Some of these relationships may take the form of equations. Therefore, the general pattern of object properties, and of relations among the objects should be identified and represented.

LP-based managerial decisions strive for careful use of resources while achieving the firm's objectives. On a very high level of abstraction, these resources are employees, space, machines, money, and material. The firm plans the allocation of these resources to various activities. Basically, resources have a 'state' and there are some 'actions' which change the states of these resources. For instance, 'hire' and 'fire' are actions which both operate on resource 'employees', where the former increases, the latter decreases the level of employees. LP decision variables can be inferred from the relationship between resources and actions.

Actions such as procurement of materials or hiring/firing employees, production of products. etc., are governed by the firm's policies. Some possible policies are: limiting overtime to a certain proportion of regular production hours, maintaining a smooth production by not allowing the fluctuations between the periods to exceed a certain percentage, allowing backorders, maintaining a service level of at least a certain proportion of demand, etc. Actions and changes of the state of the resources should not violate the firm's policies. Thus, relevant policy equations should be part of every decision model.

Fig. 3 summarizes the conceptual relationships between the object types mentioned in this subsection. In the sequel, a knowledge representation scheme tailored to this kind of knowledge will be presented.

## 3.4. Knowledge Representation Scheme

Knowledge representation can be viewed at two levels [Newell (1981)]. The 'Symbol Level' involves looking at knowledge in terms of how it is held, for instance, collection of nodes, or routines for indexing and inheritance. The 'Knowledge Level' does not distinguish among the different ways of capturing the same information or even between explicit and implicit information storage.

![](/api/attachments/HM5TBM59/fulltext/images/7c170d5db40678afc81dc00261458c430cb8e16422c01cef5b69f9bf81e40219.jpg)  
Fig. 3.

It only considers what the entire body of information says about the world, that is, how well the knowledge base provides a clear picture of the world that it represents [Brachman and Levesque 1984]. In this paper we will briefly review the representation of business and LP knowledge at the knowledge and symbol levels. A formal theory of the representation and its implementation will be discussed in a forthcoming paper [Binbasioglu and Jarke (1986)].

The scheme has to represent business knowledge about resources, possible actions on resources and policies that govern these, in the context of planning with LP. Concepts like MACHINE, EMPLOYEE, MONEY, WAREHOUSE, PRODUCTION, SALES, DEMAND, FLOW-EQUATION,... are represented with their possible attributes within the domain of production planning and resource allocation. In addition to the attributes, relationships to other objects will also be specified. These could be resources, actions, equations or relations on and among the resources. For example, MACHINE and PRODUCT have a relation of the form <Product-name, Machine-name, Machine capacity required to produce a unit of product>.

We represent business knowledge by using abstraction methods such as aggregation and generalization discussed in Smith and Smith (1977) and Jarke (1982). In the domain of production management, the highest level of abstraction is BUSINESS, an aggregation of resources, relationships among resources, actions, policies, and equations. The latter are the most generic object types in the business knowledge base. Objects at any given level of abstraction are related to more generic ones through an IS-A hierarchy. For example, the instantiations of the concept ‘resources’; namely, EMPLOYEE, MONEY, MATERIALS,... are linked to RESOURCES via IS-A links.

At the symbol level, a common use of this hierarchy is to minimize conceptual and storage redundancies by allowing properties associated with general object types to be inherited by more specialized ones. Another use is providing the means for the overall organization and management of a large knowledge base [Mylopoulos and Levesque (1984)]. We view property inheritance as a default which the description of the specialized class can override.

Objects are represented as ‘frames’ [Minsky (1975)] where all the facts about the given object are attached to slots provided by the frame structure. Some of these slots describe properties unique to the given object, others employ procedural attachments when facts are not explicitly provided. The above-mentioned generalization hierarchy is implemented by a slot called ‘IS-A’ which stores the name of the next generic object the given object is related to. Depending on the characteristics of the object to be described, the number of slots and the values that are stored in them may vary. All the objects in fig. 3 are defined using frame representations. In addition to these explicit representations of relationships, rules of inference are employed to derive implicit facts.

Fig. 4 illustrates the different knowledge representation techniques used at the symbol level. The knowledge representation scheme has been implemented in PROLOG with added object-oriented capabilities.

## 4. LP Models for Production Management: Model Formulation Example

In this section, the use of the combined structural and application knowledge base will be illustrated by means of a concrete model formulation example. The interaction will loosely follow a PROLOG syntax. Fig. 5 shows an extract of the knowledge base to be used in this example.

## 4.1. Context Identification Step

The interaction alternates between user-driven and system-driven dialog, depending on the level of initial knowledge the user can express. The function of the context identification step is to locate the relevant area of the knowledge base from which a more detailed analysis of the formulation problem at hand can be initiated.

Consider the production process in a bakery shop. The baker initially has a vague idea that

![](/api/attachments/HM5TBM59/fulltext/images/21fc78d60662f3a40aa87f42c581303578bee73ed6c1c497ceadfbfda7d53840.jpg)  
Fig. 4.

![](/api/attachments/HM5TBM59/fulltext/images/91743ab166bd23f3524b1e572805c400b18d69f389bce05b26d6a65965ab34bf.jpg)

some planning is needed in the area of cookies production, and the purchasing of associated raw materials. Moreover, he suspects that there are constraints on sales, the minimum required service level, the availability of his mixer, and raw material budgets. In a PROLOG-like notation, the initial problem statement would look as follows:

?- problem(production(cookies), purchase(raw\_material)), constraints(mixer, sugar, service\_level(cookies), sales\_limits(cookies)).

The system tries to associate this information with certain nodes and arcs in the knowledge base. For example, production (cookies) will be associated with the node 'produce'. Since the system does not know the term 'cookies', it has to disambiguate among the possible classes 'final product' and 'intermediate product' (not shown in fig. 5).

This can be done quite easily since there is a constraint on sales for ‘cookies’; therefore, cookies must be a final product. However, it might be one final product or a whole class of them (some of which may already be stored in the knowledge base). Thus, the system displays the set of known products and asks the user to check those that belong to the class of cookies:

... WHICH OF THE FOLLOWING
'FINAL PRODUCT' ITEMS
ARE 'COOKIES'?
1 - ICE CREAM
2 - PEANUT\_BUTTER\_COOKIE
3 - WHOLE\_WHEAT\_ROLL
4 - DANISH\_BUTTER\_COOKIE
5 - CHOCOLATE\_CHIP\_COOKIE
...
OTHERS (LIST)?

The user answers with 2, 4, and 5. Since there is more than one product in the group, the system infers that there is a product mix problem. The knowledge base is amended by the new class definition ‘cookies’ as shown in fig. 6.

The system knows that ‘sugar’ is a kind of raw material (in the bakery) and infers that there is a constraint on sugar availability by looking at the node for ‘raw material’ and then further at the node ‘resource’ where it finds out that resources tend to be limited.

On the other hand, the system does not know the term ‘mixer’. All it knows is that ‘mixer’ refers to a constraint. A system-driven dialog with the user is initiated to determine the meaning more precisely. The system knows that most constraints are associated with resources and can thus follow down the IS-A hierarchy of resources, using menu selection:

```txt
:- IS 'MIXER'
1 - EMPLOYEE
2 - MACHINE
3 - RAW MATERIAL
...
NO RESOURCE
```

The user could answer this by selecting '2'. The system infers that the constraint is a capacity constraint; furthermore, it can continue the dialog to find out whether 'mixer' is a synonym for some machine instance appearing in the knowledge base. If that is not the case, it has to request units of capacity measure, the capacity itself, etc., in order to fill the machine-type slots.

![](/api/attachments/HM5TBM59/fulltext/images/c05644f77d0dad30e1ddcccddc02275a3490f1c40a18acdf4f050cc80e26b6b7.jpg)  
Fig. 6.

By now, the system has marked all relevant nodes mentioned in the original problem statement. The next step is to check for incompleteness of the problem statement. Incompleteness is detected in two ways. First, the system asks the user whether certain neighbors of the marked nodes are also of interest. For example, it may ask whether there are employee problems (coming from the production node). Similarly, it may suggest the existence of storage problems (coming from cookies via its generalization, final product). Assume that the user answers the latter affirmatively.

The second method of detecting incompleteness identifies disconnected components of the knowledge base and tries to establish additional nodes that connect these components. For example, since there is a storage problem associated with the sales/product mix problem, the system hypothesizes that the problem is really a multi-period problem. Indeed, this is confirmed by the user.

In summary, the context identification step has produced the following result. The problem was originally stated as a production problem of cookies, with purchasing of raw material sugar. Using the application-specific knowledge base, the system refined the problem definition to a multi-period product-mix and purchasing problem with storage considerations.

## 4.2. Problem Formulation Step

After identifying the boundaries of the problem context, the system proceeds to assist the user in determining the necessary constraints, as well as specifying the format of these constraints and of the objective function.

The first step in this process is the choice of a suitable problem decomposition. A knowledge base of standard problem prototypes supports this process, using classification techniques [Clancey 1984] similar to those used in differential diagnosis [Pople (1982)]. Essentially, the constraints found in context identification serve as 'symptoms' observed, and the problem prototypes as 'diseases' to be diagnosed [see Binbasioglu (1986) for details]. Metarules for this step essentially follow the principle of minimal coupling and maximum cohesion among subproblems known from structured design [DeMarco (1978)]. These meta-rules are applied both to the initial decomposition of the problem, and to the subsequent integration of submodels. The example problem is initially decomposed into two subproblems as shown in fig. 7: product-mix (problem 1) and raw material purchasing (problem 2). Note, that both problems are coupled only via the decision variables associated with raw material.

Next, the decision variables and their position in relevant constraints and in the objective function are determined for each subproblem. The relevant constraints are retrieved from the knowledge base using the 'in-equation' slots of the object frames identified in the Context Identification Step (see fig. 4). If in doubt the system can ask the user to confirm their relevance in a particular case.

The KB for structural knowledge is now employed to construct the actual constraints and objective function. This step is shown for some example equations of the bakery example, below.

![](/api/attachments/HM5TBM59/fulltext/images/c1b30bb48c452c34e7ccf3253842d4b8320ade9ceb8989cd711b73a45d256cd1.jpg)  
Fig. 7.

We shall consider the following constraints for problem 1.

(1.1) Machine availability constraint

(1.2) Raw material availability constraint

(1.3) Market limitation (demand)

(1.4) Service level

(1.5) Objective function.

A major problem in LP formulation is the choice of the decision variables and their index sets. The following rule can be used to determine the decision variable: 'IF the aim is to determine the production level of final products THEN the decision variable, P, is the level of final product to be produced'. Another rule says that 'IF the problem type is product-mix THEN an index for product (say i) is needed'. Now consider the actual formulation of the equations for problem 1.

(1.1) Machine Availability Constraint. The stored form of this constraint looks as follows:

$$
\Sigma_ {i} \text { capusage } _ {i, j} P _ {i} <   = \text { Capacity } _ {j},
$$

where capusage $_{i,j}$ is the units of time each unit of product i requires on machine j.

Using the knowledge acquired during the Context Identification Step, this standard form can be specialized. Since the problem is product-mix, the index i is required and takes the values defined in the set 'cookies', i.e., 'Peanut butter cookie, danish butter cookie, chocolate chip cookie'. On the other hand, the system knows that there is only one machine which could be a bottleneck, namely the 'mixer'. Therefore, the index j can be dropped. Thus, we obtain the specialized constraint

$\Sigma_{i\in COOKIES}$ capusage $_{i,MIXER}P_{i}<=\text{Capacity}_{MIXER}$ . In a similar way, the other constraints can be specialized.

(1.2) Raw Material Availability Constraint.

$$
\begin{array}{r l} \sum_ {i \in \text { COOKIES }} & \text { rawusage } _ {i, \text { SUGAR }} P _ {i} \\ <   = & \text { availability } _ {\text { SUGAR }} \end{array}
$$

(1.3) Market Limitation

$$
P _ {i} <   = \text { Demand } _ {i}.
$$

(1.4) Service Level Equations.

$$
P _ {i} > = \text { Minimum   Sales } _ {i}.
$$

(1.5) Objective Function.

Maximize $\sum_{i\in\text{COOKIES}}P_i\text{Contribution}_i$ .

Note that the contribution coefficients must be computed from information stored at different nodes of the business knowledge base, including SELL (price), RAW-MATERIAL (costs), and possibly others.

In equal fashion, we determine constraints and objective function in problem 2.

(2.1) Meet the Internal Demand

$$
\text { Purchase } _ {\text { SUGAR }} > = \sum_ {i \in \text { COOKIES }} \text { rawusage } _ {i, \text { SUGAR }} P _ {i}.
$$

(2.2) Objective Function

Minimize cost $_{SUGAR}$ Purchase $_{SUGAR}$ .

Note that in (2.2) the $\Sigma$ sign has been removed from a standard formula since there is only one summand.

When the system combines the two subproblems, it cannot simply use the existing equations but has to modify those related to regions of the business knowledge base where subproblems overlap (cf. fig. 7). While eqs. 1.1, 1.3, and 1.4 can be used as they are, eq. 1.2 must be merged with 2.1:

$$
\begin{array}{l} \text {Availability} _ {\text {SUGAR}} + \text {Purchase} _ {\text {SUGAR}} \\ > = \sum_ {i \in \text {COOKIES}} \text {rawusage} _ {i, \text {SUGAR}} P _ {i}. \end{array}
$$

Moreover, the global objective function includes components from both subproblems. A new contribution margin is computed for the products which does not include the SUGAR costs. This change in contribution margin is necessary because the combined model takes care of raw material cost explicitly.

The combination of the subproblems must also take into account that the problem is multi-period. We can purchase raw materials earlier for use in production in later periods or produce final products earlier to meet future demand. Therefore, IF the problem is a multi-period problem THEN it is necessary to distinguish the quantities of each raw material bought, used and stored and the quantities of each final product produced, sold and stored at each time period. Moreover, there is a rule that 'IF a problem is multiperiod THEN add an index t to all variables'. (There are also additional, more complex rules which are skipped here for simplicity of exposition.)

All the previous equations are also indexed by t to accommodate the time feature in multi-period analysis. Eq. 1.3. has to be changed to reflect the fact that Sales for any period – instead of productions – must be less than Demand for the period. The objective function has to be modified and balance flow equations have to be added (cf. fig. 4).

$$
\begin{array}{l} (1. 3 ^ {\prime}). \\ \text { Sales } _ {i, t} <   = \text { Demand } _ {i, t} \end{array}
$$

We assume here (realistic in a bakery) that all demand not satisfied in the period is lost.

$$
\begin{array}{r l} & \text { Storage } _ {\mathrm{SUGAR}, t - 1} + \text { Purchase } _ {\mathrm{SUGAR}, t} \\ & = \text { Usage } _ {\mathrm{SUGAR}, t} + \text { Storage } _ {\mathrm{SUGAR}, t}, \end{array} \tag {3.1}
$$

$$
\begin{array}{l} \text {(3.2).} \\ \text {Storage} _ {i, t - 1} + P _ {i, t} = \text {Sales} _ {i, t} + \text {Storage} _ {i, t}, \\ \text {where} i \in \text {COOKIES}. \end{array}
$$

The new objective function will use the sales level instead of the production level, and will accommodate the minimization of storage costs. The final version has the following form:

Maximize

$$
\begin{array}{r l} & \Sigma_ {t} \Sigma_ {i} (\text { Sales } _ {i, t} \text { Price } _ {i, t} - P _ {i, t} \text { ProdCost } _ {i, t} \\ & \quad - \text { Storage } _ {i, t} \text { StorCost } _ {i, t}) \\ & - (\Sigma_ {t} (\text { Purchase } _ {\text { SUGAR }, t} \text { Cost } _ {\text { SUGAR }, t} \\ & \quad + \text { Storage } _ {\text { SUGAR }, t} \text { StorCost } _ {\text { SUGAR }, t})). \end{array}
$$

## 4.3. Model Building Step

After the completion of the model structure, the final step of model formulation is the instantiation of the right-hand-side and coefficient values. If these values are available explicitly in the knowledge base they are just retrieved. If there are 'if-needed' slots in the relate frames (cf. fig. 4), the values are computed using the formulas in these slots. Otherwise, the user is requested to supply the missing values.

This completes the formulation of the model. The result is now converted into a suitable matrix generator format and submitted for computation. In the discussion above, we have neglected the important issue of consistency checking. Although some of the consistency problems present in model formulation are removed by the knowledge-based approach presented here, others will remain. Structural linear programming knowledge will be required to do the associated checks, e.g., for formal inconsistency of constraints or unbounded objective functions [see Murphy and Stohr (1985) for a detailed discussion].

## 5. Concluding Remarks

The example in the previous section should have demonstrated the usefulness of domain-specific knowledge in model formulation. Without such knowledge, little guidance can be expected from a formulation support tool. Instead, the tool will have to focus on problem structuring and consistency checking. Both are extremely important, especially in the formulation of very large models. However, if model formulation by end users is intended, semantic guidance must also be offered.

A system incorporating the capabilities described in this paper is being implemented in PROLOG [Clocksin and Mellish (1981)] enhanced by object-oriented features that facilitate the implementation of frame representations, as in fig. 4. In further research, we shall try to integrate this knowledge-based tool with a more structurally oriented method [Binbasioglu and Jarke (1986)]

Another question of substantial interest is the construction of a meaningful domain knowledge base. Bouwman (1983) describes a way to extract a knowledge base (in financial analysis) from experienced analysts, essentially modelling the psychological structures of the analysts as objects of the knowledge base. Our initial solution is based more on textbook knowledge of the firm. Experience with the actual system will have to show whether that level of knowledge is sufficient, and what will be the optimal scope of the application domain. Finally, as shown in the cookie example, the interaction with the end user can also lead to incremental enhancement of the knowledge base through limited machine learning features.

## 6. References

Binbasioglu, M., Knowledge-based Support for Linear Modelling, Ph. D. thesis, graduate School of Business Administration, New York University, New York, 1986.

Binbasioglu, M. and M. Jarke, Knowledge Representation for LP Modelling Support, 1986.

Blanning, R.W., A Relational Theory of Model Management, Working paper 85–106, Owen Graduate School of Management, Vanderbilt University, Nashville, TN, 1985.

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, The Evolution from MIS to DSS: Extension of Data Management to Model Management, in: M.J. Ginzberg, W.R. Reitman and E.A. Stohr, eds., Decision Support Systems, North-Holland, Amsterdam, 1982.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston. Developments in Decision Support Systems, Advances in Computers 23, Academic Press (1984) 141–175.

Bouwman, M.J., Human Diagnostic Reasoning by Computer: An Illustration from Financial Analysis, Management Science 29(6) (1983) 653–672.

Brachman, R.J. and H.J. Levesque. What Makes a Knowledge Base Knowledgeable? A View of Databases from the

Knowledge Level, Proceedings First International Workshop on Expert Database Systems, Kiawah Island, SC, 1984.

Charnes, A. and W.W. Cooper, Management Models and Industrial Applications of Linear Programming, Wiley, New York, 1967.

Clancey, W.C., Classification Problem Solving, Proceedings AAAI-84 Conference, Austin, TX (1984) 49–55.

Clocksin, W.F. and C.S. Mellish, Programming in Prolog, Springer-Verlag, 1981.

DeMarco, T., Structured Analysis and System Specification, Yourdon, 1978.

Dhar, V., PLANET: An Intelligent Decision Support System for the Formulation and Investigation of Formal Planning Models, Ph. D. thesis, University of Pittsburgh, PA, 1984.

Greenberg, H.J., A Functional Description of ANALYZE: A Computer-assisted Analysis System for Linear Programming Models, ACM Transactions on Mathematical Software 9(1) (1983) 18–56.

Holsapple, C.W. and H. Moskowitz, A Conceptual Framework for Studying Complex Decision Processes, Policy Sciences 12(1), 1980.

Hwang, S., Automatic Model Building Systems: A Survey, DSS-85 Transactions, San Francisco, CA (1985) 22–32.

Jarke, M., Developing Decision Support Systems: A Container Management Example, Journal of Policy Analysis and Information Systems 6(4) (1982) 351–372.

Jarke, M., and Y. Vassiliou, Coupling Expert Systems and Database Management Systems, in: W. Reitman, ed., Artificial Intelligence Applications for Business, Ablex, Norwood, NJ (1984) 65–85.

McDermott, J., R1: A Rule-based Configurer of Computer Systems, Artificial Intelligence 19(1) (1982) 39–88.

Minsky, M., A Framework for Representing Knowledge, in: P.H. Winston, ed., The Psychology of Computer Vision, McGraw-Hill, New York (1975) 211–277.

Murphy, F.H. and E.A. Stohr, An Intelligent System for Formulating Linear Programs, New York University Working Paper Series CRIS ≠ 95, GBA (1985) 85–40.

Mylopoulos, J. and M.L. Brodie, eds., On Knowledge Base Management Systems, Springer-Verlag, 1986.

Mylopoulos, J. and H.J. Levesque, An Overview of Knowledge Representation, in: M.L. Brodie, J. Mylopoulos and J.W. Schmidt, eds., Conceptual Modelling, Springer-Verlag, 1984.

Newell, A., The Knowledge Level, AI Magazine 2(2) (1981) 1–20.

Pople, H.E., Heuristic Methods for Imposing Structure on Ill-structured Problems: The Structuring of Medical Diagnostics, in: P. Szolovits, ed., Artificial Intelligence in Medicine, Westview Press, Boulder, CT (1982) 119–185.

Simon, H., The New Science of Management Decisions, Harper and Row, New York, 1960.

Sivasankaran, T.R. and M. Jarke, Knowledge-based Formula Management Strategies in an Actuarial Consulting System, Decision Support Systems 1(3) (1985) 251–262.

Smith, J.M. and D.C.P. Smith, Database Abstraction: Aggregation, Communications of the ACM, 20(6) (1977) 405–413.

Stefik, M.J., Planning with Constraints, Ph. D. dissertation, Computer Science Department, Stanford University, 1980.
