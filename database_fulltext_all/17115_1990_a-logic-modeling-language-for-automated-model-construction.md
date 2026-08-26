---
otero_id: 17115
otero_key: "KPD8CHSA"
title: "A logic modeling language for automated model construction"
authors: "Ramayya Krishnan"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90004-b"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Logic Modeling Language for Automated Model Construction

Ramayya KRISHNAN

Decision Systems Research Institute, School of Urban and Public Affairs, Carnegie–Mellon University, Pittsburgh, PA, 15213, USA

This paper describes PM\* (read PM-star), a first-order logic based language, that is the basis of a knowledge based system designed to help non-expert users construct Linear Programming models in the Production, Distribution and Inventory planning domain. Problems specified in PM\* define a logic model which is used to generate problem-specific inferences, and inferences required to automate model construction. PM\* extends previous work on the PM language (Krishnan, 1988) through the integration of problem representation and model construction within a uniform predicate logic framework.

Keywords: Logic Modeling, Formal Languages, Model Management.

![](/api/attachments/KPD8CHSA/fulltext/images/b127ac11c82ac2decac1ffc2b1775a7e2e6abed548c072ac3cf2f13ba52f6ca9.jpg)

Ramayya Krishnan is Assistant Professor of Management Science and Information Systems at the School of Urban and Public affairs at Carnegie-Mellon University. He received his B. Tech. from the Indian Institute of Technology, Madras, and a M.S. and Ph.D. from the University of Texas at Austin. His primary research interests are in logic modeling, knowledge representation, and conceptual modeling languages.

$^{1}$ We use the term ‘non-expert’ to refer to a users mathematical modeling expertise. We assume such users to be knowledgeable about their problem domain.

## 1. Introduction

Linear Programming (LP) models are among the most commonly used mathematical models used to support planning in a variety of contexts. While the quality of system support for LP modeling has improved considerably in recent years, the need to conceptualize a problem in terms of abstract concepts and mathematical notation has inhibited their use by non-expert $^{1}$ users. This has led to considerable interest in tools that might help automate LP model construction [Binbasioglu and Jarke (1986), Bu-Halaiga and Jain (1988), Ma et al. (1986), Murphy and Stohr (1986), Krishnan (1988, 1989) and Muhanna and Pick (1988)].

The construction of LP models involves the development of mathematical abstractions. However, non-expert users develop qualitative problem conceptualizations. In account of this difference, our approach facilitates qualitative problem specification while employing LP modeling principles to automate model construction.

Previous work by the author [Krishnan (1987), Krishnan (1988a, b)] employing this approach to support non-expert users in the construction of Linear Programming (LP) models in the Production, Distribution and Inventory (PDI) planning domain led to the development of the PDM system. The inability to integrate qualitative problem specification and automated model construction within a rigorous formalism was a shortcoming of the PDM system. Efforts to address this shortcoming within a predicate logic framework led to the development of PM\*

## 1.1. Context and Organization of the Paper

The paper assumes the following context (refer fig. 1): a user knowledgeable about the working of a “physical” system, i.e., a real-world system, requires decision support. The problem is stated by the user in terms of real-world objects that make up the system, their inter-relationships, and attributes. This specification is what we refer to as a qualitative model, and when specified in PM\*, a logic model.

![](/api/attachments/KPD8CHSA/fulltext/images/28f44546846e06f7efbe169eec5fdafe5547cc5cfea463c5b72121abc3a5dacb.jpg)  
Fig. 1.

Two kinds of inference drawn from this logic model are used to provide decision support:

(a) Answers to conventional or deductive data base style queries. These are referred to as problem-specific inferences and employ domain-specific knowledge.

(b) The automated construction of the LP model schema corresponding to the problem specification. This employs domain-independent model building rules. $^{2}$

The paper is organized as follows. The next section presents an informal discussion of the PDI planning domain in order to set the domain vocabulary of PM\* in context. Following an introduction to the syntax of PM\*, the paper presents an example-driven introduction to each of the key features of the context described above: (a) problem specification, (b) problem-specific inferences, and (c) automated model construction.

## 2. PDI Planning

PDI planning, which has been studied extensively in the literature [Bradley et al. (1977), Glover et al. (1979), Glover and Klingman (1981, 1984), Geoffrion (1974), Hackman and Leachman (1986), Helferich (1983), Kendrick et al. (1983) and Klingman et al. (1987)], is primarily concerned with the development of plans for systems that produce, store, and distribute products (fig. 2). We have chosen to focus on a large subset of problems in this class. While a precise characterization of the PDI problem class of interest is developed in section 6.2 and described in its entirety in Appendix D, the following provides an informal discussion.

Production systems consist of a set of primitive production processes housed in plants that serve as production sites. These processes employ a set of storable and non-storable inputs to produce a set of products. Examples of storable inputs include raw-materials and intermediate products, while non-storables include resources such as machine time and labor. Production planning, carried out over a planning horizon which is typically divided into planning periods, is concerned with determining levels of production which minimize metrics such as production cost.

Resources unavailable at a production site are supplied from other remote sites, as is often the case with raw-materials. Similarly, products are distributed and sold at locations physically removed from production sites. Raw-material supply processes include the specification of purchase plans and plans to ship purchased materials from purchase sites to production sites via multi-echelon distribution systems (i.e., purchase-sites, distribution centers, warehouses, production sites). Since these supply processes take place over a period of time, distribution systems accommodate inventory options.

Similarly, on the demand side, sales at customer sites geographically distinct from production sites may necessitate shipping along multi-echelon distribution systems using constructs similar to those described for raw-materials. In summary, the class of PDI planning problems of interest can be conceptualized to consist of plan development for multi-process production systems which may distribute products to remote customer sites and receive raw-materials from remote purchase sites via multi-echelon distribution systems with inventory options.

![](/api/attachments/KPD8CHSA/fulltext/images/7f1313c9c85cb3f20bd16516cb60eac1f2b04c18139b22c147feb0b7f7edcb85.jpg)  
Fig. 2.

PM\* provides a rich vocabulary of concepts to represent problems arising in the PDI planning domain.

## 2.1. Mathematical Models of PDI problems

The mathematical models that have been formulated for the class of PDI problems we deal with are linear (LP) or non-linear (NLP) mathematical programming models. The assumptions about the nature of the processes present in a given PDI problem, i.e., assumptions about the linearity or non-linearity of their processes, their associated cost structures, etc. determine whether an LP or an NLP is appropriate. PDI problems with either linear or nonlinear processes can be specified in PM\*.

However, since the description of non-linear processes requires the specification of complex functional relationships, and the class of users we seek to support are assumed to be naive about mathematical modeling, we focus on PDI problems with linear processes. Consequently, the PDI problems specified in PM\* are formulated as LP models.

## 3. PM\*: The Language

PM\* is designed to specify PDI planning problems. The semantics of a PM\* specification, like that of any other first-order language, may be analyzed denotationally. Since denotation corresponds to the set of relationships between the symbols of the language that make up the model and the entities that make up the “world” being modeled [Dowty et al. (1978)], the following describes our conceptualization of entities that characterize PDI planning.

## 3.1. Ontology

An intuitive characterization of PDI planning can be made using an entity-relationship metaphor. We assume different sets of entities such as products, raw-materials, machines, processes, etc. Relationships are defined using these sets, and attributes of these sets and/or relationships which require the measurement of the cost, rates of utilization, activity level, etc. of a process described using functions.

Our ontology consists of five types of individuals: entities, sets, relations, functions, and indices. Entities are real-world individuals such as coal, steel, etc. Sets of entities, such as the set product of which the entity steel is a member, are also treated as individuals. Similarly, relations used to describe processes such as purchase or storage, and functions used to describe attributes of objects such as production-level or production cost are also treated as individuals. Finally, indices which are associated with each set, relation, and function are also a distinguished type of individual. The relationships between these individuals form the basis for a logic model in PM\*.

The treatment of sets, relations, and functions as individuals in our ontology, while non-standard, is required to render problem specification and model construction within a first-order language.

## 4. Vocabulary and Grammar of PM\*

The vocabulary of PM\*, like any first-order language, is composed of predicate constants, individual constants, function symbols, variables, and logical constants. $^{3}$ These symbols, combined using a set of formation rules, are used to model the individuals in our ontology and describe the relationships they enter into.

While a core vocabulary referred to as the closed vocabulary is sufficient to represent the generic concepts that characterize PDI planning, specific PDI problems are described using user-supplied vocabulary specific to the problem at hand. This user-supplied vocabulary is referred to as the open vocabulary. User-supplied elements of the open vocabulary are required to be related to elements of the closed vocabulary.

## 4.1. Closed Vocabulary of PM\*

\- primitive one-place predicates: set, relation, function, entity, indices;

\- primitive n-place predicates: domain, fdomain, range, subtype, fsubtype, fapply, ins-of, index, = , computed-using, resource, resource-utilizer, rate-of-utilization, process-activity, min-process-activity, max-process-activity, input-level, output-level, inflow, outflow, set-of-inputs, set-of-outputs, unit-income, unit-cost, set-of-costs, set-of-incomes, flow, sink, source, supply-capacity, demand-requirement, member;

\- primitive function symbols: union, ., prev, next, length, pos, app;

\- individual constants: products, machines, raw-materials, regular-labor, overtime-labor, capital, production-process, plant, distribution-center, warehouse, customer-site, purchase-yard, time, real-number, used-in, produced-by, purchased-at, stored-at, sold-at, available-at, supplied-from, received-at, shipped-from, reachable-from, unit-process-cost, unit-process-price, process-level, utilization-rate, min-level, max-level, transformation-process, utilized-at, [ ], +, \*, -, /, sum, ≤, ≥;

\- variables: denumerably many variables:

\- logical constants: and, or, if/then, if/only if, not.

## 4.2. Open Vocabulary of PM\*

\- individual constants: denumerably many constants;

\- variables: denumerably many variables.

## 4.3. Rules of Formation for PM\*

The rules of formation of $PM^{*}$ are very similar to fairly standard versions of the first-order predicate logic with equality. In describing the grammar of $PM^{*}$ , we use Greek characters such as $\alpha$ , $\beta$ , $\psi$ , $\Phi$ as part of our metalanguage to represent constants while $\mu$ is used to designate a variable.

Grammar of $PM^*$ : There are two types of expressions in $PM^*$ : terms and well-formed formulae (wffs). A term in $PM^*$ is either an individual constant or an individual variable. A functional expression which consists of a function symbol followed by terms is also a term. In addition lists of terms are also treated as terms. Thus if $t_1, \ldots, tn$ are terms, then so is [t1, t, ..., tn].

A well-formed formula (wff) of PM\* is defined recursively as follows.

1. If $\Phi$ is a predicate of $n$ places, $(n \geq 0)$ and $\alpha 1, \ldots, \alpha n$ are terms, then $\Phi(\alpha 1, \ldots, \alpha n)$ is a wff.

2. If $\Phi$ is a wff, then so is not $(\Phi)$ .

3. If $\Phi$ is a wff and $\psi$ is a wff, then so are $\Phi$ and $\psi$ ; $\Phi$ or $\psi$ .

4. If $\Phi$ is a wff and $\beta$ is a wff then if $\Phi$ then $\beta$ is also a wff.

5. If $\Phi$ is a wff and $\beta$ is a wff then $\Phi$ if and only if $\beta$ is also a wff.

6. $\forall \mu \Phi$ is a wff if $\Phi$ is a wff.

7. $\exists \mu \Phi$ is a wff if $\Phi$ is a wff.

## 5. Examples in PM \*

This section clarifies, with examples, a few features associated with lists and then focusses on illustrating typical usage of PM\* in defining logic models of PDI planning problems.

While defining a term in PM\*, we noted that lists of individual constants and functional expressions were also terms. Since lists are themselves terms, lists may be nested within lists. Lists of arbitrary length may be defined using the infix operator (binary function) ‘’. In particular, a term of the form $\alpha1.\alpha2$ designates a sequence in which $\alpha1$ is the first element and $\alpha2$ is the rest of the list. With this operator we can describe the relation member (modeled using the predicate member) as follows.

$\forall X \forall L$ member $(X, X.L)$

AX∀Y∀L if member(X, L)

then member(X, Y.L)

Commonly used functions such as length which return the length of a list, pos which returns elements in a list positionally (i.e., first, second, etc.), and app which appends any two lists allow useful operations and relations on lists to defined in PM\*. In the following, we often drop the universal quantifier $\forall$ where its use is obvious. The rest of the section presents an example-driven introduction to representing PDI problem in PM\*. The examples consist of specifications that users would be required to provide. $^{4}$

Section 3.1 described the ontological basis behind models defined in PM\*. Since different kinds of individuals exist in the world, they are each distinguished. Individuals such as products, raw materials, etc. interpreted as referring to set-of-products, set-of-raw materials, etc. are identified as sets. Processes denoted by individuals such as produced-by, used-in, etc. are identified as relations, while attributes by individuals such as production-level, production-cost, etc. are identified as functions.

Individual constants such as production-level are also referred to as function individuals.

set(products)

set(production-processes)

set(machines)

The assertion set(products) is interpreted as "The individual named by "products" is a set".

Since used-in, produced-by, shipped-from are relations, they are specified as:

relation(used-in)

relation(produced-by)

Functions such as unit-process-cost, process-level, etc. are similarly specified.

function(unit-process-cost)

function(process-level)

Individual constants that do not denote sets, functions or relations are entities. For example, stainless steel and brown coal denote real-world individuals.

entity(stainless-steel)

entity(brown-coal)

Individuals such as stainless-steel and brown coal are introduced by users to model real-world objects in specific PDI planning problems and are part of PM\* 's open vocabulary.

Individual constants identified to be either relations or functions are related to the individual constants identified as sets through domain and range relationships. Consider the assertion shown below.

domain(produced-by, [product, production-process, plant, time])

This is interpreted as “The relation named by “produced-by” represents the production of product in production-processes at plants over time”.

Similarly, each individual which denotes a function is related to the individuals which define its domain and range.

domain(process-level,

[product, customer-site, time])

range(process-level, real-number)

This is interpreted as “The individual named by “process-level” denotes a function which measures the quantity of product sold at a customer-site over time”.

The foregoing described predicates such as set, function, and relation being used in conjunction with individual constants of the closed vocabulary. These predicates are also used in conjunction with the user-supplied individual constants introduced to model specific PDI planning problems. In addition to the predicates seen thus far, relationships between individuals of the open and closed vocabulary are modeled using predicates such as subtype, subtype, etc. These features are illustrated with a simple example.

The problem concerns a steel manufacturer, ABC Inc., which manufactures steel at its mills in Pittsburgh. The point of this example is to develop a representation in PM\* that characterizes the relationships between, and the attributes of, important objects such as the manufacturing processes used, products produced, and raw-materials and resources employed. The sets introduced to describe the problem are:

set(types-of-steel)

set(types-of-coal)

set(set-of-mills)

set(years)

set(types-of-steel-production-process)

Each of these sets must be related to a set in the closed vocabulary. This is done as follows.

subtype(types-of-steel,product)

subtype(types-of-coal, raw-material)

subtype(types-of-fuel, raw-material)

subtype(years, time)

It should be noted that subtype describes a subset relationship between the sets under consideration. Note that there might be several subtypes of each individual constant of the closed vocabulary. For instance, types-of-coal and types-of-fuel are subtypes of raw-material.

Membership relations of individuals in sets and/or relations are described using the predicate ins-of. Thus, for example, since stainless steel is a type of steel (i.e., an element of the set types-of-steel), we have:

ins-of(stainless-steel, types-of-steel)

ins-of (1978, years)

User supplied constants are introduced to model problem-specific relationships. For instance, a user supplied constant such as steel-production may be introduced to model the production of steel at the steel mills. The sentences shown below state this relationship.

relation(steel-production)

domain(steel-production, [types-of-steel, types-of-steel-production-process, set-of mills, years])

Just as sets introduces in the open vocabulary are related to sets of the closed vocabulary, the predicate subtype is used to relate individuals that denote relations. Thus, steel-production is related to produced-by using the predicate subtype.

subtype(steel-production, produced-by)

Elements (tuples) of this relation are also specified using the predicate ins-of. Lists are particularly useful in representing tuples.

ins-of([stainless-steel, open-hearth, pittsburgh, 1978], steel-production)

This assertion can be considered equivalent to: steel-production(stainless-steel,

open-hearth, pittsburgh, 1978)

in traditional first-order predicate logic syntax if the constant steel-production was interpreted as a predicate constant.

Functions to describe attributes are also introduced as individual constants.

function(steel-production-level)

range(steel-production-level, real-number)

domain(steel-production-level, [types-of-steel,

types-of-steel-production-process, mill, years])

Individuals related by function application are related using the predicate fapply. In the example shown below fapply applies the function steel-production-level to the termlist to return the value 13.8. The principal value of fapply is the ability to treat functions as individuals within a predicate logic framework.

fapply(steel-production-level, [steel, steel-production-process, mill, years], 13.8)

It should be noted that there is a clear separation between the schema and instance of the qualitative model. Only those assertions involving the predicates ins-of and fapply contain specific data. They also turn out to be the source of parameter values once the LP model schema has been formulated. The other assertions describe the general structure of the prevailing inter-relationships.

The example described thus far illustrates the declarative specification of problems in PM\*. However, in introducing predicates and functions, we have not formally indicated how the syntactic structure of formulae in PM\* is enforced. As we shall see, the formation rules described earlier are by themselves insufficient.

## 5.1. Syntactic Structure of PM\*

The syntax of a language is determined by its grammar. The examples in the previous section illustrate the syntax of PM\*. However the syntactic structure of the set of the formulae that defined the logic model in the example is only one among the several admitted by the grammar as described in section 4.3. Consider two simple examples.

set(steel)

function(steel-production-level)

subtype(steel, steel-production-level)

relation(steel-production)

The first example consist of three well-formed formulae (wffs). The first two identify the individual constants steel and steel-production-level to be a set and function respectively. The third sentence relates these using the predicate subtype. The third formula, while being syntactically well formed, is incorrect as subtype is intended to model only a subset relation between sets or relations. In other words, the arguments of the predicate subtype should only be sets and/or relations.

The second example consists of a single well-formed formula that identifies steel-production as a relation. However, there is no domain predicate that defines the domain of steel-production. Once again we intend each individual identified to be a relation to have an associated domain declaration and this intention is not enforced by the grammar.

To enforce these constraints that are not part of the rules of formation, we add axioms within PM\* which we refer to as integrity constraints [Reiter (1984)]. Formally, if the wffs that make up the logic model are labelled L and the set of integrity constrains are labelled IC, then only those interpretations (model theoretically speaking), say I, that are models of IC and L are allowed. The following describes a few of the integrity constraints in PM\*. The complete set is described in Appendix C.

Integrity constraints enforce intended use and restrict the set of relationships that the individuals in the ontology may enter into. For instance, an individual constant that denotes a set in PM\* does not exist in isolation. It is either used to define the domain of a relation, or the domain and range of a function. This can be stated as the following integrity constraint. All variables not explicitly quantified are assumed to be universally quantified.

if sets(S)

then $(\exists R \exists L$ relation $(R)$ and domain $(R, L)$ and member $(S, L)$ or

$(\exists F$ function $(F)$ and $(\exists D$ domain $(F, D)$ and member $(S, D)$ or (range $(F, S)))$

Integrity constraints may also be used to ensure that certain wffs are specified collectively (i.e., certain properties of individuals are stated). Consider a relation R. Each individual that is a relation has a domain defined to be the cross product of individuals that are sets. In PM\*, the collection of the sets that define the domain are collected into lists. The length of these lists should equal the arity of the relation. Thus we have:

dom-list $(L)$ if and only if

(∀Sif member (S, L)

then set(S) or relation(S))

A domain list is a collection of sets and/or relations.

if relation(R)

then $\exists D$ dom-list $(D)$ and length $(D) = \operatorname{arity}(R)$ and domain $(R, D)$

The function length returns the length of a list of terms, while arity is used describe the arity of a function or a relation.

Similar integrity constraints are stated which require each function to have a domain and range declaration. In the example introduced earlier, we noted that PM\* employs predicates such as subtype and fsubtype to relate individuals that are sets, relations and functions to other sets, relations and functions. The types of individuals that may be arguments to these predicates may be enforced using the constraints shown below.

if subtype(X, Y)

then(set $(X)$ and set $(Y))$ or (relation $(X)$ and relation $(Y))$ or (relation $(X)$ and set $(Y))$

if fsubtype(X, Y)

then function(X) and function(Y)

Enforcing syntactic structure is similar to compilation in programming languages. The advantage with logic is the elegant means of stating and using axioms to ensure syntactic integrity.

## 6. Inferences in PM\*

Inferences drawn from a PM\* specification may be broadly classified into two categories: (a) problem-specific inferences, and (b) automated model construction. While domain-specific axioms are used to generate qualitative inferences, a small set of model building rules is used to construct the LP model schema.

## 6.1. Problem Specific Inferences

Problem specifications in PM\* consist of a collection of wffs that describe some specific PDI system. They are thus a collection of facts similar to a database. The inferences that make explicit the problem details implicit in these specifications are referred to as problem specific inferences. They are generated using axioms about PDI planning.

Since domain axioms are stated in terms of the generic concepts that characterize PDI planning in contrast to the user-supplied vocabulary used to specify specific PDI planning problems, the application of these axioms require other axioms which relate individual constants of the closed and open vocabulary. An example is shown below.

if ins-of $(A, B)$ and subtype $(B, C)$ then ins-of $(A, C)$

The axiom relates three individuals A, B and C. While A and B represent user-supplied individual constants, C is a constant of the closed vocabulary. Given

ins-of(stainless-steel, steel)
subtype(steel, product)

The axiom allows us to infer ins-of(stainless-steel, product). Similarly, individual constants of the open and closed vocabulary that are identified to be functions are related using an axiom. It is in this context that the benefit of treating functions as individuals is realized. Note that our variables F and CF range over “function individuals”. This would not otherwise be possible within a first-order logic based language. As described later, the treatment of functions, relations, and sets as individuals is fundamental to inferences employed to automate model construction.

if fapply(F, A, B) and fsubtype(F, CF) then fapply(CF, A, B)

The utility of these axioms in conjunction with domain-specific axioms is illustrated with a simple example.

set(types-of-steel)
set(types-of-iron)

ins-of(stainless-steel, types-of-steel)
ins-of(scrap-iron, types-of-iron)

subtype(types-of-steel, product)
subtype(types-of-iron, product)

relation(iron-production)
relation(iron-usage)

subtype(iron-production, produced-by)
subtype(iron-usage, used-in)

domain(iron-production, [types-of-iron, type-of-blast-furnace-process, set-of-mills, years])

domain(iron-usage, [types-of-iron, types-of-steel-production-

process, set-of-mills, years])

ins-of([scrap-iron, blast-furnace, pittsburgh, 1988], iron-production)
ins-of([scrap-iron, open-hearth, pittsburgh, 1988], iron-usage)

The example describes a fragment of a production planning problem which involves two varieties of product, types-of-steel and types-of-iron. Iron is produced by the blast furnace process and used in steel production. A common need in manufacturing systems is to be able to track intermediate products. These are products such as the types of iron that are produced by certain production processes only to be consumed by other processes that produce the final product. Given the large number of processes in a production system and the variety of inputs used and outputs produced, deducing intermediate products and the specific processes they link is an important service. This may be done as follows.

The axioms which were introduced previously to relate individual constants of the closed and open vocabulary are applied to yield the following predicates.

ins-of(scrap-iron, product)

ins-of([scrap-iron, blast-furnace, pittsburgh, 1988], produced-by)

ins-of([scrap-iron, open-hearth, pittsburgh, 1988], used-in)

These predicates are combined using the rule shown below.

if ins-of(A, product) and
ins-of([A, P1, L, T], produced-by) and
ins-of([A, P2, L, T], used-in)

then intermediate-product (A, P1, P2)

This yields the predicate:

intermediate-product(scrap-iron, blast-furnace, open-hearth)

The above being interpreted as “scrap-iron is an intermediate product produced in a blast-furnace and consumed in an open-hearth furnace”. In general intermediate-product(A, B, C) is interpreted as A is intermediate product that is produced by B and consumed in C.

The example demonstrated a simple type of inference, representative of the some of the most useful types of inferences generated in PM\* wherein knowledge of a series of inter-relationships is used to help users understand complex systems.

In addition to the rules we have seen thus far, relationships between important processes in PDI planning such as production, sales, purchase etc. are formalized as domain axioms. A complete set of these may be found in Appendix A. An example is shown below.

if ins-of([X, P, M, T], produced-by) then ins-of([X, M, T], sold-at) or ins-of([X, M, T], supplied-from) or ins-of([X, M, T], stored-at) or $\exists Q, P \neq Q$ , ins-of([X, Q, M, T], used-in)

The axiom relates the objects involved in a production process to related processes such as sales, supply, storage, and continued production available at the production site. Note that the axiom is not a horn clause since the consequent is a disjunction.

The process of problem specification in PM\*, i.e., assertions of various facts about the system being modeled, yield an evolving logic model of the problem. Facts in this evolving model are used in conjunction with the domain axioms to focus the attention of the user on processes related to those already specified. Thus, if a user had asserted a fragment similar to that introduced previously about production, the axiom shown above could be used to query the user about the relevance of related processes such as sales, supply, storage, etc. This serves two purposes. It helps the user in problem specification and prevent certain simple kinds of infeasibilities associated with errors of omission. Second, answers obtained from the user about the relevance of particular processes are used to tailor a horn clause version of the axiom shown above. For instance, if the user had indicated that only sales at the plant and supply from the plant were relevant to his particular problem $^{5}$ , then the axiom is as shown below.

if ins-of([X, P, M, T], produced-by) then ins-of([X, M, T], sold-at) and ins-of([X, M, T], supplied-from)

Since each generic process in PDI planning is related to other processes axiomatically, a variety of inferences which require the chaining together of these axioms may also be generated.

For example, at a market, it is often important to know the source of the products at hand since different sources may employ different lead times, an important factor in the event products have to be restocked. This type of inference is made possible by considering an axiom similar to the one considered earlier which related sales to purchase, receipt and storage processes. Assuming that receipt is the only relevant process in the problem at hand, we have:

if ins-of([X, M, T], sold-at)

then ins-of([X, M, T], recieved-at)

Similarly, receipt is axiomatically related to the supply process.

if ins-of([X, M, T], received-at) then $\exists Y M \neq Y$ ins-of([X, Y, T], supplied-from)

These axioms in conjunction with the axiom about production processes may be used to infer that sales at a particular market, say M, were supplied from products produced at plant P. These types of inference are very useful in typical PDI planning problem contexts that often include several alternative sources of supply, points of sale and channels of distribution.

## 6.2. A Formal Definition of PDI Planning

Previous sections have introduced the language, provided illustrative examples, and detailed two specific features (integrity constraints and domain-specific axioms) that demonstrate the advantages to be gained from a logic modeling approach. However, we have only dealt with the PDI problem domain on an informal basis. A formal definition of PDI planning is developed in this section. The complete set of definitions is in Appendix D. As we shall see in the next section, formal problem definitions play an important role in automated model construction.

The PM\* language is designed to specify PDI planning problems. However, in the absence of a formal definition of PDI planning, it is unclear as to what set of wffs in PM\* constitute a production or distribution planning problem. The principal reasons for providing a formal definition are detailed below.

(a) A formal definition provides an objective tool to understand the class of PDI planning problems that may be specified in PM\*.

(b) A related ability is to reason with a given specification in PM\* to determine if the set of wffs constitute a production problem, a distribution problem or a combination of both. Furthermore, if the set of wffs do not constitute a "known" problem type as defined, the definitions could be used to supply intelligent feedback.

(c) Finally, the definitions provide a framework to extend the class of PDI planning problems that may be specified in PM\*.

The definition of production and distribution problems in PM\* is done in a recursive manner. Definitions are developed for distribution planning. The reader is urged to consult Appendix D at this juncture.

The approach to developing a recursive definition of distribution planning problems consists of separating the relations that define the structure of the problem from the functions which determine quantities that can be shipped (i.e., capacity at source) and demanded (i.e., demand at sinks). This separation is necessitated due to the several alternative means of supplying a source e.g., purchase, storage, etc.) and generating demand at a sink e.g., sales, storage, etc.). Consider the collection of wffs represented by the following definition of $\phi_{bdis}$ . All variables are assumed to be existentially quantified. The comma is used to abbreviate an “and”.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{\mathrm{bdis}}(C, [S_1], [S_2], T, [P], [F], [CF] :=$ subtype(C, comm), subtype $(S_1, \mathrm{csource})$, subtype $(S_2, \mathrm{csink})$, subtype $(T, \mathrm{time})$,
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
relation(P),  
domain(P, [C, $S_{1}$, T, $S_{2}$, T]),  
subtype(P, shipped-from),  
function(F),  
domain (F, [C, $S_{1}$, T, $S_{2}$, T]),  
range(F, real-number),  
fsubtype(F, process-level),  
function(CF),  
domain(CF, [C, $S_{1}$, T, $S_{2}$, T]),  
range(CF, real-number)  
fsubtype(CF, unit-process-cost)
</div>

The set of wffs simply require a commodity C to be shipped from a set of sources $S_{1}$ to a set of sinks $S_{2}$ across time periods T. The variables F and CF (i.e., the flow and unit cost of shipping, respectively) range over function individuals. This represents the structure of the simplest distribution planning problem.

The wffs described above ignore alternative processes that create supplies and demands. Among the several alternatives to generate supply capacity, let us consider the purchase process. The symbol $\phi_{purch}$ specifies a collection of wffs that describe the purchase process.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{\mathrm{purch}}(C, S_1, T, R, [SF]) :=$ relation $(R)$, domain $(R, [C, S_1, T])$, subtype $(R, \text{purchased-at})$, functions $(SF)$, domain $(SF, [CS_1, T])$, range $(SF, \text{real-number})$, fsubtype $(SF, \text{process-level})$
</div>

The purchase process describes the purchase of a commodity at a location across time. The variable SF that ranges over function individuals denotes the quantity purchased. Purchase levels are often constrained to be between upper and lower bounds. The symbols $\phi_{nlb}$ and $\phi_{nub}$ define a general means of specifying lower and upper bounds.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{\mathrm{nlb}}(C, L, T, R, F) :=$ function(F), domain(F, [C, L, T]), range(F, real-number), fdomain(F, R) fsubtype(F, min-level)  
$\phi_{\mathrm{nub}}(C, L, T, R, F) :=$ function(F), domain(F, [C, L, T], range(F, real-number), fdomain(F, R) fsubtype(F, max-level)
</div>

A recursive definition of the purchase process now employs the base case described earlier with the definitions of the upper and lower bounds. Thus the pruchase process with the lower bound and the purchase process with upper bound are also defined to be purchase processes. The recursive definition is shown below.

$$
\begin{array}{r l} & {\phi_ {\mathrm{purch}} (A, B, C, R, L. D) :=} \\ & {\quad \phi_ {\mathrm{purch}} (A, B, C, R, D), \phi_ {\mathrm{nlb}} (A, B, C, R, L)} \\ & {\phi_ {\mathrm{purch}} (A, B, C, R, U. D) :=} \\ & {\quad \phi_ {\mathrm{purch}} (A, B, C, R, D), \phi_ {\mathrm{nub}} (A, B, C, R, U)} \end{array}
$$

Similarly, the sales process may be used to generate a demand requirement. The definition of the sales process is exactly analogous to that of the purchase process.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{\mathrm{sale}}(C, S_1, T, [SF]) :=$ relation $(R)$, domain $(R, [C, S_1, T])$, subtype $(R, \text{sold-at})$, function $(SF)$, domain $(SF, [C, S_1, T])$, range $(SF, \text{real-number})$, fsubtype $(SF, \text{process-level})$ $\phi_{\mathrm{sale}}9A, B, C, R, E.D) :=$ $\phi_{\mathrm{sale}}(A, B, C, R, D)$, $\phi_{\mathrm{nlb}}(A, B, C, R, E)$ $\phi_{\mathrm{sale}}(A, B, C, R, E.D) :=$ $\phi_{\mathrm{sale}}(A, B, C, R, D)$, $\phi_{\mathrm{nub}}(A, B, C, R, E)$
</div>

At this point we have the elements required to define one possible distribution problem by combining the base distribution structure described using $\phi_{bdis}$ with the purchase and sales processes described using $\phi_{purch}$ and $\phi_{sale}$ . The definition is shown below. Note that this is but one possible distribution problem. Other alternatives are possible by considering combinations of possible supply and demand processes. Appendix D lists the whole set.

$$
\begin{array}{c} \phi_ {\mathrm{dis}} (C, S _ {1}, S _ {2}, T, P, F, C F, S F, D F) := \\ \phi_ {\mathrm{bdis}} (C, S _ {1}, S _ {2}, T, P, F, C F), \\ \phi_ {\mathrm{purch}} (C, S _ {1}, T, L, S F), \\ \phi_ {\mathrm{sale}} (C, S _ {2}, T, M, D F) \end{array}
$$

Just as we had extended purchase and sales processes using lower and upper bounds, similarly constraints may be placed on the shipment levels that are part of a distribution problem. The upper and lower bounds that may be placed on shipment levels are described below.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
fdomain(LB, P)
range(LB, real-number),
fsubtype(LB, min-level)

 $\phi_{\mathrm{ub}}(E, S_1, S_2, T, P, UB) :=$ 
function(UB),
domain(UB, [C, S₁, T, S₂, T]),
fdomain(UB, P)
range(UB, real-number),
fsubtype(UB, max-level)
</div>

These lower and upper bounds allow the base distribution problem to the extended. Thus a distribution problem with constraints on shipment levels is also defined to be a distribution problem. This recursive definition is shown below.

$$
\begin{array}{r l} & {\phi_ {\mathrm{dis}} (C, S _ {1}, S _ {2}, T, P, L B. F, C F, S F, D F) :=} \\ & {\qquad \phi_ {\mathrm{dis}} (C, S _ {1}, S _ {2}, T, P, F, C F, S F, D F),} \\ & {\qquad \phi_ {\mathrm{lb}} (C, S _ {1}, S _ {2}, T, P, L B)} \\ & {\phi_ {\mathrm{dis}} (C, S _ {1}, S _ {2}, T, P, U B. F. C F, S F, D F) :=} \\ & {\qquad \delta_ {\mathrm{dis}} (C, S _ {1}, S _ {2}, T, P, F, C F, S F, D F),} \\ & {\qquad \phi_ {\mathrm{ub}} (C, S _ {1}, S _ {2}, T, P, U B)} \end{array}
$$

The simplest analogy to these recursive definitions are string grammars. If the base cases are treated as terminal symbols, then the definitions serve as rewrite rules of a context free grammar to generate non-terminal symbols. The set of all possible non-terminals correspond to the set of distribution problems that may be defined within PM\*. The strategy used to develop a recursive definition of production planning problems is similar to that detailed for distribution problems.

## 6.3. Automated Model Construction

Linear Programming models are algebraic models. They consist of a set of indexed constraints and functions referred to as the schema. When instantiated with data, a schema generates a model instance.

The problem we are interested in consists of inferring the mathematical expressions associated with the constraints and functions of the LP model schema. The mathematical expressions consist of variables, which range over the “function individuals” used to measure quantities in the PM\* logic model. Automated model construction, viewed as deduction, thus reduces to the problem of inferring the mathematical relationships between these function individuals of the logic model. While the rest of the section details with examples the inferential process used in automated model construction, Appendix E proves two theorems that demonstrate correctness of the inferential process used.

Consider, for example, a fragment of the linear programming model used to decide levels of production in a steel mill.

max sum(i, j, l, t)

(steel-production-level(i, j, l, t) \*

steel-production-cost(i, j, l, t))

s.t.

sum(i, j) (steel-production-level (i, j, l, t) \* utilization-rate(i, k, j, l, t)) $\leq$ coal-purchase-level(k, l, t)

The fragment consists of an objective function which represents the total cost of production, and a resource constraint which limits the amount of coal used in steel production to the quantity supplied through purchase. Examples of parameters and variables in this model include steel-production-level and steel-production-cost, respectively. The letters such as i, j, etc., are referred to as indices. Indices allow a compact representation of an LP model schema. Note that these variables and parameters would be specified as “function individuals” in the PM\* model of the steel production problem. Given a PM\* model of a steel production problem, we seek to automatically construct the mathematical expressions associated with the constraint and objective function shown above. The specific data required to generate an instance such as the elements of index sets and the values of parameters are obtained from the ins-of and fapply assertions of the PM\* specification, respectively.

The process begins with the assignment of indices to the relevant terms in a PM\* specification. Indices in PM\* are viewed as a distinguished set of individual constants that are part of the open vocabulary. Individuals that denote sets, relations and functions have an associated index. Thus, for example each individual that denotes a set is assigned an unique index. A fragment of PM\* specification that includes indices and the predicate index is shown below.

indices(s)

index(types-of-steel, [s])

index(years, [t])

index(set-of-mills, [m])

index(types-of-steel-production-process, [p])

All user-supplied sets are assigned an unique index latter. The index of individuals that are relations or functions is inferred from index values of sets that define their domain.

if domain(F, [A1,..., An]) and
    index(A1, I1)... and index(An, In) then in-
    dex(F, union(I1,...In))

The rule deduces the index of an individual that denotes a function or a relation using the predicate domain and the function union that returns a list of indices given a set of index sublists. Thus, given an individual such as steel production and its domain, we have its index to be $[s, p, m, t]$ which is the union of the index sublists $[s], [p], [m]$ , and $[t]$ .

domain(steel-production, [types-of-steel, types-of-steel-production-process, set-of-mills, years])
index(steel-production, [s, p, m, t])

The mathematical form of the relationships between individuals that denote measurements functions is deduced using model building rules. An example of such a rule is material balance.

if set-of-inputs([[X1, IX1], ..., [Xn, IXn]]) and set-of-outputs([[Y1, IY1], ..., [Yn, IYn]]) then $\exists F$ function(F) and computed-using $(F, [[X1, IX1], +, \ldots, +, [Xn, IXn], \geqslant, [Y1, IY1], +, \ldots, +, [Yn, IYn]])$

The rule relates a list of inputs to a system denoted by the variables X1, X2, etc. to a list of outputs represented by variables such as Y1, Y2, etc. The variables X1, X2, etc. and Y1, Y2, etc. range over “function individuals”. The indices associated with each of these inputs and outputs is represented by the variables IX1, IY1, etc.

The predicates set-of-inputs and set-of-outputs predicate the property of being an input or an output on each function individual. The predicate computed-using associates a mathematical expression with a function individual, i.e., computed-using(F, Exp) is interpreted to mean “the value of function F is computed using the expression Exp”. Mathematical expressions are represented in list notation and consist of individuals which denote measurement functions (e.g., inputs, outputs, etc.) and individuals which denote numeric functions such as + and relations such as $\geq$ . Note that since all these functions and relations are treated as individuals, a list of such individuals, ordered left to right, is a convenient representation of an indexed material balance constraint. The complete set of model building rules may be found in Appendix B. The need to predicate properties of functions and manipulate them as model building rules do is the motivation behind treating functions as individuals.

Since model building rules are stated in terms of domain-independent concepts such as inputs and output, their application to a logic model stated in domain-specific vocabulary presents a problem. The correspondence between individuals in an user-supplied PM\* specification to concepts such as inputs and outputs need to be established. This correspondence is deduced using a set of rules referred to as transformation rules. An example is used to illustrate how PDI problem definitions, transformation rules, and model building rules are combined to construct a LP model schema.

Consider a fragment of the steel production problem stated in PM\*.

index(types-of-steel, [s])

index(types-of-coal, [c])

index(set-of-mills, [m])

index(years, [t])

set(product)
set(types-of-steel)
subtype(types-of-steel, product)
set(raw-material)
set(types-of-coal)
subtype(types-of-coal, raw-material)
subtype(types-of-steel-production-process, production-process)

relation(produced-by)
relation(steel-production)
subtype(steel-production, produced-by)
subtype(coal-usage, used-in)

function(steel-production-level)
function(coal-purchase-level)
function(process-level)

domain(steel-production-level, [types-of-steel, types-of-steel
    -production-process, set-of
    -mills, years])
range(steel-production-level, real-number)

index(steel-production-level, [s, p, m, t])
index(coal-purchase-level, [c, m, t])

The specification identifies important sets, relations and functions and describes inter-relationships in the form of domain and range predicates.

The resource constraint for types of coal that may be deduced from the logic model is shown below.

$\operatorname {sum}(I,J)$ (steel-production-level $(I,J,L,T)^*$

utilization-rate $(I, K, J, L, T))$

$\leq$ coal-purchase-level $(K, L, T)$

The left hand side (LHS) of the constraint represents the utilization of the various types of coal in the steel production process while its right hand side represents the quantity available through purchase. The following describes the inferences used in its construction.

The process used to construct the LP model schema begins with the determination of the problem context. The problem context determines the type of the problem described in PM\*: is it a production problem, a distribution problem or some combination of both? The recursive definition of PDI problems developed in section 6.2 is used to determine the problem context. In some sense this is analogous to a parsing problem. Given the base cases and the alternative ways of combining them to build more complicated descriptions, the problem context is determined by analyzing the logic model using the rules of problem definition.

The example on hand is a simple production planning problem since the base case of production as described in $\phi_{bprod}$ and $\phi_{purch}$ (refer Appendix D) account for the wffs in the logic model. The problem context is used to determine the sequence of model building rules that are to be applied. Since the problem is a production planning problem, the first step is to determine the mathematical form of the utilization functions for each type of input used in each type of production process. In this example this reduces to determining the utilization of coal (i.e., the LHS of the constraint under construction). Since the utilization of a resource is determined using a model building rule stated in domain-independent terms, a set of transformation rules are applied.

Since production processes are a type of transformation process, i.e., they transform coal and other resources to steel, the first set of transformation rules deduce which of the objects associated with the process are resources and which are resource utilizers.

if subtype(X, production-process) then subtype(X, transformation-process)

if subtype(Y, produced-by) and

domain(Y, [Ru, P, L, T])

and subtype(P, transformation-process)

then resource-utilizer(Ru, P, L, T)

resource-utilizer(Ru, P, L, T) is interpreted as Ru is the utilizer of resources in processes P at location L in period T.

The rule infers that a product produced by a production process is a resource utilizer by virtue of the fact that it is produced by a transformation process. Similarly objects used in transformation processes are deduced to be resources.

if subtype(Y, used-in) and

domain(used-in, $[R, P, L, T]$ )

and subtype (P, transformation-process)

then resource $(R, P, L, T)$

resource $(R, P, L, T)$ is interpreted as R is a resource used in processes P at location L in period T.

Resources are utilized in transformation processes at measured rates of utilization to produce products at measured production levels. Individuals in the user-supplied logic model that correspond to utilization rates and production levels are deduced using another set of transformation rules.

if resource $(R, P, L, T)$ and

resource(Ru, P, L, T) and

fsubtype(X, utilization-rate) and

domain(X, [R, Ru, P, L, T])

then rate-of-utilization(X, R, Ru, P, L, T)

rate-of-utilization $(X, R, Ru, P, L, T)$ is interpreted as X denotes the function which is rate of utilization of resource R to produce Ru in processes P at location L in period T.

if resource-utilizer (Ru, P, L, T) and fsubtype (PL, process-level) and domain (PL, [Ru, P, L, T])

then process-activity $(PL, Ru, P, L, T])$

process-activity (PL, Ru, P, L, T) is interpreted as PL denotes the function which measures the production of Ru in processes P in location L in period T.

These rules when applied to the PM\* specification yield the following predicates. They are:

process-activity(steel-production-level, types-of-steel, types-of-steel-production-process, set-of-mills, years)

This wff is interpreted to mean “steel-production-level represents the activity of the various steel-production-process used to produce types of steel at mills over time”.

rate-of-utilization(coal-util-rate, types-of-coal, types-of-steel, types-of-steel-production-process, set-of-mills, years)

This wff is interpreted to mean “coal-util-rate represents the utilization of the various types of coal used to produce the different types of steel in various steel-production-processes at mills over time”.

A model building rule similar to the material balance rule referred to as the “transformation-in-form” rule is used to deduce the functional form of the coal utilization function.

if rate-of-utilization(X, R, RU, P, L, T) and process-activity(PL, Ru, P, L, T) and index(X, IR)

and index(PL, IPL) and index(P, IP) and index(Ru, Iru) and

subtype(Dom, utilized-at) and domain(Dom, $[R, L, T]$ )

then ∃ New function(New) and fsubtype(New, Process-level)
and fdomain(New, Dom)
and domain(New, [R, L, T]) and
computed-using(New, [[sum, Iru[, [sum, IP], [X, IR], \*, [PL, IPL]])

The rule is very similar to the material balance rule in that the functional form is once again represented as a relation between lists of individual constants which are either measurement functions or arithmetic functions such as \*. The application of the “transformation-in-form” rule yields the functional form of the LHS. Assume that the new function has been assigned a name such as coal-until-function.

computed-using(coal-util-function, [[sum, [p]], [sum[s]], [coal-util-rate, [c, s, p, m, t]], \*, [steel-production-level, [s, p, m, t]]])

This in conventional notation is:

sum(p) sum(s) (coal-util-rate(c, s, p, m, t) \* steel-production-level (s, p, m, t))

Once the utilization of resources in the production process has been inferred, the next step in the production problem context involves the construction of a material balance condition involving each resource utilized. Thus all functions which measure the use and supply of the various types of coal are related using the principle of material balance. Since material balance is stated in terms of inputs and outputs, this requires the utilization and purchase functions to be transformed appropriately. The rule used to deduce that the coal utilization function is an output is quite straightforward.

if subtype(Dom, utilized-at) and type(Dom, $[R, L, T]$ ) and

fdomain(F, Dom) and index(F, IF)

then output-level([F, IF])

The rule simply identifies a “function individual” which measures the quantity of resource usage as an output-level (note: utilized-at is a individual which denotes the usage of a resource).

The purchase level of coal is transformed into an input-level. The basic metaphor used in the transformation rule views purchases and sales as types of exchange. Purchase is viewed as a process that involves the exchange of goods for money. Rules that manipulate exchange are used to deduce that purchase is a type of input to a system.

if subtype(X, purchased-at) and

domain(X, [C, L, T])

then $\exists$ New exchange $(X, \text{New}, C, L, T)$

The context determines if an exchange is an output or an input. The predicate exchange $(X, A, B, L, T)$ can be read as “X denotes the exchange of A for B at location L in period T”. If the context is set by A then the exchange would be an outflow and vice versa if the context is set by B. Since in purchase the context is set by “B”, the good being purchased, we deduce that purchase is an inflow. A function which measures the rate of inflow is then treated as an input to the system under consideration.

if context(A, L, T) and

exchange(X, New, A, L, T)

then inflow(X, A, L, T)

if inflow(X, A, L, T) and
    fsubtype (Y, process-level) and
    fdomain(Y, X) and index(Y, IY)
then input-level([Y, IY])

These rules on application to our example yield the predicates shown below.

input-level([coal-purchase-level, [c, m, t]])
output-level([coal-util function, [c, m, t]])

The material balance rule is stated in terms of predicates such as set-of-inputs and set-of-outputs which are defined in terms of input-levels and output-levels as shown below.

$\forall L$ set-of-inputs $(L)$ if and only if ( $\forall X$ if member $(X, L)$ then input-level $(X)$ )

Similarly, set-of-outputs is defined in terms of output-level.

$\forall L$ set-of-outputs $(L)$ if and only if ( $\forall X$ if member $(X, L)$ then output-level $(X)$ )

Since we have only one input-level, coal-purchase-level and one output-level, coal-util-function, the corresponding wffs with the set-of-inputs and set-of-outputs predicates are as shown below.

set-of-inputs([[coal-purchase-level, [c, m, t]]])
set-of-outputs([[coal-util-function, [c, m, t]]])

These predicates when combined using the material balance model building rule yield the indexed material balance constraint which is represented using the predicate computed-using shown below.

computed-using(consl,

[[coal-util-function, [c, m, t]], ≤ ,

[coal-purchase-level, $[c, m, t]]])$

This in conventional notation is:

coal-util-function(c, m, t)

$\leq$ coal-purchase-level $(c, m, t)$

The mathematical expressions associated with the schema of LP model are thus constructed mechanically from a PM\* problem specification using a combination of transformation and model building rules, the application sequence of which is determined as a function of the problem context. The specific data required to generate an instance such as the element of index sets and the values of parameters are obtained from the ins-of and fapply assertions of the PM\* specification respectively. The schema and the specific data can be syntactically transformed into the syntax of a mathematical modeling language such as GAMS [Kendrick and Meeraus (1987)] or Structured Modeling Language [Geoffrion (1987)]. These languages generate the model instance and provide links to algorithms that solve such models.

## 7. Conclusions

This paper introduced a language called PM\*, described its syntax and semantics, and illustrated with examples the principal kinds of inferences that may be drawn within it. The principal insight gained by the author in developing PM\* is the role played by the choice of ontology in a logic modeling effort. PM\* 's predecessor PM used a traditional conceptualization of PDI planning problems which allowed it to effectively model PDI planning problems and support qualitative inferences. However, since model construction is fundamentally a task that involves the representation and manipulation of functions as individual objects, PM could not integrate model construction and problem specification within a first-order framework.

This integration of problem specification, qualitative inferences and model construction within a first-order language required a rethinking of our ontological assumptions and resulted specifically in the treatment of relevant sets, relations, and measurement functions as individuals. Furthermore, model constructions also required additional representational features such as lists and the ability to describe recursive relations. These were the extensions that resulted in PM\*.

The paper also illustrates the principal advantage of a logic modeling approach: that of a uniform language to state integrity constraints to enforce syntactic structure, domain-specific axioms, model building axioms, and formal definitions of the class of problems dealt with in PM\*. These features translate into important types of support that a system designed around PM\* may provide.

(a) The integrity constraints may be used “outside” the language as the basis of a syntax directed editor. Such an editor could provide meaningful feedback to a user to help rectify the syntactic form of his logic model.

(b) Domain-specific axioms allow a logic model to function like a deductive database in that conventional retrieval is extended with the ability to perform deduction.

(c) Formal recursive definitions of PDI problems help in determining the problem context, an essential step in model construction. By helping partition the sequence of applicable model building rules by problem context they improve the efficiency of the process. Furthermore, they are essential to the development of a formal proof that a logic model that fits one of the known problem classes will results in a correct LP model schema. In the event a problem specification does not fit a problem class, the definitions allow intelligent feed back as to how the specification may appropriately altered.

Finally, it should be noted that while the language and the various inferential features have been described in the context of PDI planning, none of these are specific to this domain. The framework developed in the language is viewed to address the larger goal of designing formal approaches to automated model construction.

## Acknowledgement

I would like to thank the editor and two anonymous reviewers for feedback that helped improve the quality of the paper.

## Appendix A: Axioms of PDI Planning

if ins-of([X, PR, P, T], used-in)

then not(ins-of([X, PR, P, T] produced-by))

if ins-of([X, PR, P, T], produced-by)

then not(ins-of[(X, PR, P, T], used-in))

if ins-of([X, PR, P, T], used-in)

then (ins-of([X, P, T], received-at) or
ins-of([X, P, T], purchased-at) or
ins-of([X, P, T], available-at) or ins-of
([X, P, T], stored-at))

if ins-of([X, PR, P, T], produced-by)

then (ins-of([X, P, T], sold-at) or
ins-of([X, P, T], supplied-from) or ins-of
([X, P, T], stored-at))

if ins-of([X, P, T], received-at)

then (ins-of([X, PR, P, T], used-in) or
    ins-of([X, P, T], stored-at) or ins-of([X, P, T],
    sold-at))

if ins-of([ $X, P, T$ ], supplied-from)

then (ins-of([X, PR, P, T], produced-by) or ins-of([X, P, T], purchased-at) or ins-of([X, P, T], available-at) or ins-of([X, P, T], stored-at))

if ins-of([ $X, L, T$ ], supplied-from)

then $\exists M L \neq M$ ins-of([ $X, M, T$ ], received-at)

if ins-of([X, L, T], received-at)

then $\exists M L \neq M$ ins-of([ $X, M, T$ ], supplied-from)

if ins-of([X, P, T], stored-at)

then ins-of([X, P, Q], stored-ai) and $Q = \operatorname{prev}(T)$

if ins-of([ $X$ , $P$ , $T$ ], stored-at)

then ins-of([X, P, Q], stored-at) and $Q = \mathrm{next}(T)$

if ins-of([ $X$ , $P$ , $T$ ], stored-at)

then (ins-of([X, P, T], supplied-from) or ins-of([X, P, T], recieved-at) or ins-of([X, PR, P, T], produced-by) or ins-of([X, PR, P, T], used-in))

if ins-of([ $X$ , $P$ , $T$ ], purchased-at) then

(ins-of([X, PR, P, T], used-in) or
ins-of([X, P, T], supplied-from) or ins-
of([X, P, T], stored-at))

if ins-of([X, P, Q], sold-at)

then (ins-of([X, PR, P, T], produced-by) or ins-of([X, P, T], received-at) or ins-of([X, P, T], stored-at))

if ins-of([X, L1, T1, L2, T2], shipped-from)

then ins-of([X, L1, T1], supplied-from) and ins-of([X, L2, T2], received-at) and ins-of([L1, T1, L2, T2], reachable-from)

if ins-of([X, P, T], available-at)

then (ins-of([ X, PR, P, T], used-in) or ins-of([ X, P, T], supplied-from))

ins-of([X, P, T], source-plan) := (ins-of([X, P, T], purchased-at) or ins-of([X, P, T], available-at) or ins-of([X, PR, P, T], produced-by) or ins-of([X, P, T], supplied-from) or ins-of([X, P, T], stored-at))

ins-of([X, P, T], sink-plan) := (ins-of([X, P, T], sold-at) or ins-of([X, PR, P, T], used in) or ins-of([X, P, T], stored-at) or ins-of([X, P, T], received-at))

if ins-of([X, L1, T1], source-plan) and
ins-of([X, L2, T2], sink-plan) and L1 ≠ L2

and ins-of([L1, T1, L2, T2], reachable-from) then ins-of([X, L1, T1, L2, T2], shipped-from)

## Appendix B: Primitive Model Building Rules

## Transformation in Form

if rate-of-utilization(X, R, RU, P, L, T) and process-activity(PL, RU, P, L, T) and index (X, IR)
index(P, IP) and index(PL, IPL) and index(RU, IRU)
and index(A, IA) and subtype(Dom, utilized-at) and
domain(Dom, [R, L, T])

then ∃ New function(New) and fsubtype(New, process-level)
and fdomain(New, Dom) and domain(New [R, L, T]) and
computed-using(New, [[sum, IRu], [sum, IP], [X, IX], \*, [PL, IPL]])

## Material Balance

if set-of-inputs([[X1,IX1],...,[Xn,IXn]]) and set-of-outputs([[Y1,Iy1],...,[Yn,IYn]])

then $\exists F$ , function $(F)$ and computed-using $(F$ , $[X1, IX1], +, \ldots, +, [Xn, IXn], \geq, [Y1, IY1], +, \ldots, +, [Yn, IYn]])$

Single Commodity Distribution (Transformation in Space)

if flow(F, C, L1, T1, L2, T2) and sink(L2, T2) and source(L1, T1)
and index(L2, IL2) and index(L1, IL1) and index(F, IF)
and supply-capacity(SC, C, L1, T1) and demand-requirement(SD, C, L2, T2)

then $\exists F1$ function(F1) and $\exists F2$ function(F2) and computed-using(F1, [[sum, IL2], [F, IF], ≤,[SC, IL1]]) and computed-using(F2, [[sum, IL1], [F, IF], ≥,[SD, IL2]])

## Cost and Profit Structures

if unit-cost(UC, A, L, T) and process-
activity(A, C, L, T) and
index(UC, IUC) and index(A, IA)

$$
F,
$$

$$
[ C 1, +, \dots , C n ], -, [ I 1, +, \dots , + I m ])
$$

## Bounds

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
if min-process-activity(MIL, C, L, T) and max-process-activity(MAL, C, L, T) and activity-level(Al, C, L, T) and index(MIL, IMI) and index(MAL, IMA) and index(AL, IA) then  $\exists F$  function(F) and computed-using(F, [[MIL, IMI],  $\leq$ , [Al, IA],  $\leq$ , [MAL, IMA]])
</div>

Appendix C: Integrity Constraints Used to Enforce Syntactic Structure

Note: the “and” connective is represented using a comma.

Each set is either part of the domain of some relation of function, or the range of some function.

Each set has some elements that are entities. The membership of entities in a set is represented using the ins-of predicate

A domain list is a collection of sets or relations. These lists usually define the domain of functions or relations.

$\forall R \text{ relation}(R) \to \exists D \text{ dom-list}(D), \text{ length}(D) = \text{ arity}(R), \text{ domain}(R, D)$

Every relation has a domain represented as a domain list whose length should equal the arity of the relation.

$\forall F$ function $(F) \to \exists D$ $\exists R$ dom-list $(D)$ , length $(D)$ $= \operatorname{arity}(F)$ , domain $(F, D)$ , set $(R)$ , range $(F, R)$

Every function has a domain and a range. Once again the length of the domain list should equal the arity of the function.

$$
\forall F _ {1} F _ {2} D F
$$

$$
(F _ {1}),
$$

$$
(F _ {2}, D),
$$

$$
\left. F _ {2}\right)
$$

$$
\left. \left. F _ {1}, F\right) \right.
$$

$$
F _ {1}, D)
$$

$$
\left. F _ {2}, F\right)
$$

$\rightarrow \exists R_{1}R_{2}R_{1}\neq R_{2},\mathrm{relation}(R_{1}),\mathrm{relation}(R_{2}),\mathrm{domain}(R_{1},D),$

domain $(R_{2}, D)$ , fdomain $(F_{1}, R_{1})$ , fdomain $(F_{2}, R_{2})$

When two functions $F_{1}$ and $F_{2}$ have exactly the same domain and are fsubtypes of the same function (for, e.g., purchase level and sales level), there should exist unique relations $R_{1}$ and $R_{2}$ defined on the same domain that may be used to distinguish between these functions.

$\forall R$ relation $(R) \to \exists L$ structure $(L)$ , length $(L) = \text{arity}(R)$ , ins-of $(L, R)$

The elements of a relation are also described using the ins-of predicate. Each relation has a collection of entities (i.e., tuples) that are its elements.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\forall R \forall D \forall L$ relation $(R)$, domain $(R, D)$, ins-of $(L, R)$ $\rightarrow \forall I = 1$, length $(L)$, ins-of(pos $(L, I)$, pos $(D, I))$
</div>

The tuples of relations are constructed from the elements of the sets in the domain list. The function pos returns the i th element of a list of elements.

$\forall F$ function $(F) \to (\exists L \exists E$ structure $(L)$ , length $(L) = \text{arity}(F)$ , fapply $(F, L, E)) \vee (\exists M$ math-formula $(M)$ , computed-using $(F, M))$ Every function is either extensionally specified using the fapply predicate or is computed using an expression called a math formula. $\forall F \forall D \forall R \forall L \forall E$ function $(F)$ , domain $(F, D)$ , range $(F, R)$ , fapply $(F, L, E) \to \forall I = 1$ , length $(L)$ , ins-of(pos $(L, I)$ , pos $(D, I))$ , ins-of $(E, R)$ The domain and range elements of a function are constructed from sets that define them. $\forall L$ index-list $(L) \leftrightarrow (\forall X$ member $(I, L) \to \text{indices}(I))$ An index-list is a structure composed of indices. $\forall X$ set $(X) \vee$ relation $((X) \vee$ function $(X) \to \exists Y$ index-list $(Y)$ , index $(X, Y)$ Every set, relation and function has an index list composed of individuals that are indices. $\forall X \forall Y$ subtype $(X, Y) \to (\text{set}(X), \text{set}(Y)) \vee (\text{relation}(X), \text{relation}(Y)) \vee (\text{relation}(X), \text{set}(Y))$ Only sets and relations are allowed to be arguments of predicate subtype. $\forall R \forall D$ domain $(R, D) \to (\text{relation}(R) \vee \text{function}(R))$ , dom-list $(D)$ $\forall F \forall R$ fdomain $(F, R) \to \text{function}(F)$ , relation $(R)$ $\exists D$ domain $(F, D)$ , domain $(R, D)$ $\forall L \forall R$ ins-of $(L, R) \to \text{structure}(L)$ , (relation $(R) \vee \text{set}(R))$ , length $(L) = \text{arity}(R)$ $\forall F \forall L \forall R$ fapply $(F, L, R) \to \text{function}(F)$ , structure $(L)$ , entity $(R)$ , length $(L) = \text{arity}(F)$ $\forall F \forall M$ computed-using $(F, M) \to \text{function}(F)$ , math-formula $(M)$ $\forall X \forall Y$ fsubtype $(X, Y) \to \text{function}(X)$ , function $(Y)$

Only functions are arguments of the predicate fsubtype.

## Appendix D

The variables are assumed to be universally quantified.

subtype(S, comm) ↔

    subtype(S, product) ∨

    subtype(S, raw-material)

subtype(X, input) ↔

    subtype(X, raw-material) ∨

    subtype(X, machine) ∨

    subtype(X, regular-labor) ∨

    subtype(X, overtime-labor) ∨

    subtype(X, capital)

subtype(X, csource) →

    subtype(X, plant) ∨

    subtype(X, distribution-center) ∨

    subtype(X, warehouse) ∨

    subtype(X, purchase-yard)

subtype(X, csink) ↔

    subtype(X, customer-site) ∨

    subtype(X, plant) ∨

    subtype(X, distribution-center) ∨

    subtype(X, warehouse)

## Definition of Distribution Planning Problems

Note: All variables are existentially quantified. The “and” connective is represented as a comma. The := symbol is used as a definition operator. $\phi_{\text{bdis}}(C, [S_1], [S_2], T, [P], [F], [CF]) :=$ subtype(C, comm),

subtype( $S_1$ , csource),

subtype( $S_2$ , csink),

subtype(T, time),

relation(P),

domain P, [C, $S_1$ , T, $S_2$ , T]),

subtype(P, shipped-from),

function(F),

domain(F, [C, $S_1$ , T, $S_2$ , T]),

range(F, real-number),

fsubtype(F, process-level),

function(CF),

domain(CF, [C, $S_{1}$ , T, $S_{2}$ , T]), range(CF, real-number), fsubtype(CF, unit-process-cost)

$\phi_{\mathrm{nlb}}(C, L, T, R, F) :=$ function $(F)$ , domain $(F, [C, L, T])$ range $(F, \text{real-number})$ , fdomain $(F, R)$ fsubtype $(F, \text{min-level})$

$\phi_{\mathrm{nub}}(C, L, T, R, F) :=$ function $(F)$ , domain $(F, [C, L, T])$ , range $(F, \text{real-number})$ , fdomain $(F, R)$ fsubtype $(F, \text{max-level})$

$\phi_{\mathrm{purch}}(C, S_1, T, R, [SF]) :=$ relation $(R)$ , domain $(R, [C, S_1, T])$ , subtype $(R$ , purchased-at), function $(SF)$ , domain $(SF, [C, S_1, T])$ , range $(SF$ , real-number), fsubtype $(SF$ , process-level)

$\phi_{\mathrm{purch}}(A, B, C, R, E, D) := \phi_{\mathrm{purch}}(A, B, C, R, D), \phi_{\mathrm{nlb}}(A, B, C, R, E)$ $\phi_{\mathrm{purch}}(A, B, C, R, E, D) := \phi_{\mathrm{purch}}(A, B, C, R, D), \phi_{\mathrm{nub}}(A, B, C, R, E)$

$\phi_{\mathrm{avail}}(C, S_1, T, R, [SF]) :=$ relation $(R)$ , domain $(R, [C, S_1, T])$ , subtype $(R$ , available-at), function $(SF)$ , domain $(SF, [C, S_1, T])$ , range $(SF$ , real-number), fsubtype $(SF$ , process-level)

$$
\phi_ {\text { avail }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\text { avail }} (A, B, C, R, D), \phi_ {\mathrm{nlb}} (A, B, C, R, E)
$$

$$
\phi_ {\text { avail }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\text { avail }} (A, B, C, R, D), \phi_ {\text { nub }} (A, B, C, R, E)
$$

$\phi_{\mathrm{store}}(C, S_1, T, R, [SF]) :=$ relation $(R)$ , domain $(R, [C, S_1, T])$ , subtype $(R, \text{stored-at})$ , function $(SF)$ , domain $(SF, [C, S_1, T])$ , range $(SF, \text{real-number})$ , fsubtype $(SF, \text{process-level})$

$$
\phi_ {\text { store }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\text { store }} (A, B, C, R, D), \phi_ {\text { nlb }} (A, B, C, R, E)
$$

$$
\phi_ {\text { store }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\text { store }} (A, B, C, R, D), \phi_ {\text { nub }} (A, B, C, R, E)
$$

$$
\phi_ {\text { sale }} (C, S _ {1}, T, R, [ S F ]) :=
$$

$$
\operatorname{domain} (R, [ C, S _ {1}, T ]),
$$

$$
\text { subtype } (R, \text { sold - at }),
$$

$$
\text { function } (S F), \text { domain } (S F, [ C, S _ {1}, T ]),
$$

$$
\text { fsubtype } (S F, \text { process - level })
$$

$$
\phi_ {\text { sale }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\mathrm{sale}} (A, B, C, R, D), \phi_ {\mathrm{nlb}} (A, B, C, R, E)
$$

$$
\phi_ {\text { sale }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\text { sale }} (A, B, C, R, D), \phi_ {\text { nub }} (A, B, C, R, E)
$$

$$
\phi_ {\text { req }} (C, S _ {1}, T, R, [ S F ]) :=
$$

$$
\text { relation } (R),
$$

$$
\operatorname{domain} (R, [ C, S _ {1}, T ]),
$$

$$
\text { subtype } (R, \text { required - at }),
$$

$$
\text { function } (S F), \text { domain } (S F, [ C, S _ {1}, T ]),
$$

$$
\text { range } (S F, \text { real - number }),
$$

$$
\text { fsubtype } (S F, \text { process - level })
$$

$$
\phi_ {\text { req }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\mathrm{req}} (A, B, C, R, D), \phi_ {\mathrm{nlb}} (A, B, C, R, E)
$$

$$
\phi_ {\text { req }} (A, B, C, R, E. D) :=
$$

$$
\phi_ {\text { req }} (A, B, C, R, D), \phi_ {\text { nub }} (A, B, C, R, E)
$$

$\phi_{1b}(C, S_1, S_2, T, P, LB) :=$ function(LB), domain(LB, [C, S1, T, S2, T]), fdomain(LB, P) range(LB, real-number), fsubtype(LB, min-level)

$\phi_{\mathrm{ub}}(C, S_1, S_2, T, P, UB) :=$ function(UB), domain(UB, [C, $S_1$ , T, $S_2$ , T]), fdomain(UB, P) range(UB, real-number), fsubtype(UB, max-level)

$\phi_{\mathrm{ncsource}}(C, NS, S, T, P, F, CF) :=$ subtype(NS, csource), relation(P), domain(P, [C, NS, T, S, T]), subtype(P, shipped-from), function(F), domain(F, [C, NS, T, S, T]), fsubtype(F, process-level), range(F, real-number), function(CF), domainCF, [C, NS, T, S, T]), range(CF, real-number), fsubtype(CF, unit-process-cost)

$\phi_{\mathrm{ncsink}}(C, S, NS, T, P, F, CF) :=$ subtype(NS, csink), relation(P), domain(P, [C, S, T, NS, T]), subtype(P, shipped-from), function(F),

domain(F, [C, S, T, NS, T]), fsubtype(F, process-level), range(F, real-number), function(CF), domain(CF, [C, S, T, NS, T]), range(CF, real-number), fsubtype(CF, unit-process-cost)

Recursive Definition of Distribution Planning Problems

All variables are assumed to universally quantified

$\phi_{\mathrm{bdis}}(C, NS.S_1, S_2, T, P_1.P, F_1.F, CF_1.CF) := \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \phi_{\mathrm{ncsource}}(C, NS, S_2, T, P_1, F_1, CF_1) \phi_{\mathrm{bdis}}(C, S_1, NS.S_2, T, P_1.P, F_1.F, CF_1.CF) := \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \phi_{\mathrm{ncsink}}(C, S_1, NS, T, P_1, F_1, CF_1) \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \phi_{\mathrm{prec}}(C, S_1, T, SF), \phi_{\mathrm{srec}}(C, S_2, T, DF)$

Since $S_{1}$ and $S_{2}$ may be lists of source types and sink types, supply and demand alternatives have to be specified for each source and sink type. $\phi_{prec}$ and $\phi_{srec}$ recursively ensure that each source type and sink type associated with a distribution structure has an associated purchase and sales process respectively. All $\phi$ symbols with the rec subscript are similar. They have been omitted owing to space limitations.

/\* All variables in the definition of $\phi_{\mathrm{prec}}$ and $\phi_{\mathrm{srec}}$ are universally quantified unless otherwise specified \*/

$\phi_{\mathrm{prec}}(C, A.[ ], T, [SF]) := \exists E \phi_{\mathrm{purch}}(C, A, T, E, SF)$ $\phi_{\mathrm{prec}}(C, A.\mathrm{Sup}, T, S. SF) := \exists F \phi_{\mathrm{purch}}(C, A, T, F, S), \phi_{\mathrm{prec}}(C, \mathrm{Sup}, T, SF)$ $\phi_{\mathrm{srec}}(C, A.[ ], T, [SF]) := \exists E \phi_{\mathrm{sale}}(C, A, T, E, SF)$ $\phi_{\mathrm{srec}}(C, A.\mathrm{Sup}, T, S, SF) := \exists F \phi_{\mathrm{sale}}(C, A, T, F, S), \phi_{\mathrm{srec}}(C, \mathrm{Sup}, T, SF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \phi_{\mathrm{arec}}(C, S_1, T, SF), \phi_{\mathrm{srec}}(C, S_2, T, DF), \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, Sf, DF) :=$

$\phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \quad \phi_{\mathrm{strec}}(C, S_1, T, SF), \quad \phi_{\mathrm{srec}}(C, S_2, T, DF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \quad \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \quad \phi_{\mathrm{prec}}(C, S_1, T, SF), \quad \phi_{\mathrm{rqrec}}(C, S_2, T, DF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \quad \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \quad \phi_{\mathrm{arec}}(C, S_1, T, SF), \quad \phi_{\mathrm{rqrec}}(C, S_2, T, DF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \quad \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF) \quad \phi_{\mathrm{prec}}(C, S_1, T, SF), \quad \phi_{\mathrm{strec}}(C, S_2, T, DF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \quad \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \quad \phi_{\mathrm{ared}}(C, S_1, T, SF), \quad \phi_{\mathrm{strec}}(C, S_2, T, DF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, DF) := \quad \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \\    \phi_{\mathrm{strec}}(C, S_1, T, SF), \\    \phi_{\mathrm{strec}}(C, S_2, T, DF)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, F_1. SF, DF) := \quad \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, CF, SF, DF), \\    \phi_{\mathrm{purch}}(C, S_1, T, R, F_1)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, F_1. SF, DF) := \quad \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, CF, SF, DF), \\    \phi_{\mathrm{avail}}(C, S_1, T, R, F_1)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, F_1. SF, DF) := \quad \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, CF, SF, DF), \\    \phi_{\mathrm{store}}(C, S_1, T, R, F_1)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, F_1. DF) := \quad \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, CF, SF, DF), \\    \phi_{\mathrm{sale}}(C, S_2, T, R, F_1)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, F_1. DF) := \quad \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, CF, SF, DF), \\    \phi_{\mathrm{req}}(C, S_2, T, R, F_1)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F, CF, SF, F_1. DF) := \quad \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, CF, SF, DF), \\    \phi_{\mathrm{store}}(C, S_2, T, R, F_1)$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, LB.F. CF. SF. DF) := \quad \phi_{\mathrm{dis}}(C. S_1. S_2. T. P. F. SF. DF), \\    \phi_{\mathrm{lb}}(C. S_1. S_2. T. P. LB)$ $\phi_{\mathrm{dis}}(C. S_1. S_2. T. P. UB.F. CF. SF. DF) := \quad \phi_{\mathrm{dis}}(C. S_1. S_2. T. P. F. SF. DF), \\    \phi_{\mathrm{ub}}(C. S_1. S_2. T. P. UB)$

/\* The function "app" append any two lists and returns an appended list \*/

$\phi_{\mathrm{dis}}(C, \mathrm{app}(S_1, S_2), \mathrm{app}(S_2, S_3), \mathbf{k} T, \mathrm{app}([P], [Q]), \mathrm{app}(F_1, F_2), \mathrm{app}([CF_1], [CF_2]), \mathrm{app}(SF_1, SF_2), \mathrm{app}(DF_1, DF_2)) := \phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F_1, CF_1, SF_1, DF_1), \phi_{\mathrm{dis}}(C, S_2, S_3, T, P, F_2, CF_2, SF_2, DF_2)$

## Definition of Production Planning Problems

Note: All variables are existentially quantified.

$\phi_{bprod}([I], [O], [P], L, T, [M], [U], [F], [CF], [R]) :=$ subtype(O, product),
subtype(I, input),
subtype(P, production-process),
subtype(L, plant), subtype(T, time),
relation(U), domain(U, [I, P, L, T]),
subtype(U, used-in), relation(M),
domain(M, [O, P, L, T]),
subtype(M, produced-by),
function(F), domain(F, [O, P, L, T]),
range(F, real-number),
fsubtype(F, process-level),
function(CF),
domain(CF, [O, P, L, T]),
range(CF, real-number),
fsubtype(CF, unit-process-cost),
function(R), domain(R, [I, O, P, L, T]),
range(R, real-number),
fsubtype(R, utilization-rate) $\phi_{ninp}(N, O, P, L, T, U, R) :=$ subtype(N, input), relation(U),
domain(U, [N, P, L, T]),
subtype (U, used-in),
function(R),
domain(R, [N, O, P, L, T]),
range(R, real-number),
fsubtype(R, utilization-rate) $\phi_{rec}(C, L, T, R, F) :=$ subtype(C, comm), relation(R),
domain(R, [C, L, T]),
subtype(R, received-at),
function(F), domain(F, [C, L, T]),
range(F, real-number),
fsubtype(F, process-level) $\phi_{supp}(C, L, T, R, F) :=$ subtype(C, comm),

relation(R), domain(R, [C, L, T]), subtype(R, supplied-from), function(F), domain(F, [C, L, T]), range(F, real-number), fsubtype(F, process-level) $\phi_{nproc}(I, O, P, L, T, R_1, R_2, F_1, F_2, F_3) :=$ subtype(P, production-process), subtype(I, input), subtype(O, product), relation( $R_1$ ), domain( $R_1$ [I, P, L, T]), relation( $R_2$ ), domain( $R_2$ , [O, P, L, T]), subtype( $R_1$ , produced-by), function( $F_1$ ), domain( $F_1$ , [O, P, L, T]), fsubtype( $F_1$ , process-level), function( $F_2$ ), domain( $F_2$ , [O, P, L, T]), fsubtype( $F_2$ , unit-process-cost), function( $F_3$ ), domain( $F_3$ , [I, O, P, L, T]), range( $F_3$ , real-number), fsubtype( $F_3$ , utilization-rate) $\phi_{plb}(C, P, l, T, R, F) :=$ function(F), domain(F, [C, P, L, T]), range(F, real-number), fdomain(F, R), fsubtype(F, min-level) $\phi_{pub}(C, P, l, T, F) :=$ function(F), domain(F, [C, P, L, T]), range(F, real-number), fdomain(F, R), fsubtype(F, max-level)

## Recursive Definition of Production Problems

All variables are assumed to be universally quantified $\phi_{\mathrm{bprod}}(N.I, O, P, L, T, M, V.U, F, CF, R2.R1) :=$ $\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, R1),$ $\phi_{\mathrm{ninp}}(N, O, P, L, T, V, R2)$ $\phi_{\mathrm{bprod}}(I, O, P_2.P_1, L, T, N.M, V.U, F2.F1, CF2.CF1, R2.R1) :=$ $\phi_{\mathrm{bprod}}(I, O, P_1, L, T, M, U, F1, CF1, R1),$ $\phi_{\mathrm{nproc}}(I, O, P_2, L, T, N, V, F2, CF2, R2)$

$\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, UB.F, CF, UR) := \phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, UR), \phi_{\mathrm{pub}}(O, P, L, T, UB)$ $\phi_{\mathrm{bprod}}(I, O, P, L, T, M, : U, LB.F, CF, UR) := \phi_{\mathrm{bprod}}(I, O, P, L, T, M, UI, F, CF, UR), \phi_{\mathrm{plb}}(O, P, L, T, LB)$ $\phi_{\mathrm{bprod}}(\mathrm{app}(I1, I2), \mathrm{app}(O1, O_2), \mathrm{app}(P1, P2), L, T, \mathrm{app}(M1, M2), \mathrm{app}(U1, U2), \mathrm{app}(F1, F2), \mathrm{app}(CF1, CF2), \mathrm{app}(R1, R2)) := \phi_{\mathrm{bprod}}(I1, O2, P1, L, T, M1, U1, F1, CF1, R1), \phi_{\mathrm{bprod}}(I2, O2, P2, L, T, M2, U2, F2, CF2, R2)$

Since each base production structure might consist of a series of input types, only those problems that have at least one related supply processes for each input type are defined to be production planning problems. An illustrative recursive definition to ensure that each type of input has an associated purchase process is developed. Other alternative supply processes such as storage, etc. have similar structures. They have been omitted due to space limitations.

All variables in the definition of the symbol $\phi_{pprec}$ are assumed to be universally quantified.

$$
\phi_ {\mathrm{pprec}} (A. [ ], L, T, [ S ]) :=
$$

$$
\phi_ {\text { purch }} (A, L, T, R, S)
$$

$$
(A. I, L, T, S. S F) :=
$$

$$
\phi_ {\text { p   u   r   c   h }} (A, L, T, R, S),
$$

$$
\phi_ {\mathrm{pprec}} (I, L, T, S F)
$$

The definition recurses down the list of input types collecting associated supply functions.

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR, SF,$ [ ]):=

$$
\phi_ {\mathrm{pprec}} (I, L, T, S F)
$$

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR, SF,$ [ ]):=

$\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, UR)$ $\phi_{\mathrm{rcprec}}(I, L, T, Sf)$

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR, SF,$ [ ]):=

$\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, UR)$ $\phi_{\mathrm{stprec}}(I, L, T, SF)$

$$
[ ]) :=
$$

$$
\phi_ {\mathrm{bprod}} (I, O, P, L, T, M, U, F, C F, U R)
$$

$$
\phi_ {\mathrm{avprec}} (I, L, T, S F)
$$

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR,\ \mathrm{union}$ $(SF1, SF2, SF3, SF4)), [ ] :=$ $\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, UR),$ $\phi_{\mathrm{rcprec}}(K, L, T, SF1),$ $\phi_{\mathrm{pprec}}(M, L, T, SF2),$ $\phi_{\mathrm{stprec}}(N, L, T, SF3),$ $\phi_{\mathrm{avprec}}(O, L, T, SF4)$ $I = \mathrm{union}(K, M, N, O)$

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, R, SF, DF.D): = \phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR, SF, D),$

$$
\phi_ {\text { store }} (O, L, T, R, D F)
$$

$$
\phi_ {\text { prod }} (I, O, P, L, T, M, U, F, C F, R, S F,
$$

$$
D F. D) :=
$$

$$
\begin{array}{l} \phi_ {\text { prod }} (I, O, P, L, T, M, U, F, C F, U R, S F, \\ D), \end{array}
$$

$$
\phi_ {\mathrm{sale}} (O, L, T, R, D F)
$$

## Appendix E

The following proves two propositions that demonstrate correctness of the inferential process used in automated model construction. The model building rules referred to in the proof are from Appendix B.

Proposition 1. A PM\* specification that is a valid distribution planning problem has a corresponding well-formed Linear Programming (LP) model schema.

Proof. The proof is constructive and follows the definition of distribution planning. Each possible type of distribution planning problem will be shown to have a corresponding LP model structure obtained through the application of a sequence of model building rules.

Case 1. The base structure, represented by the symbol $\phi_{bdis}$ , consists of a set of sources, a set of sinks, links between them with a defined shipment level and unit cost of shipping.

$$
\phi_ {\mathrm{bdis}} (C, [ S _ {1} ], [ S _ {2} ], T, [ P ], [ F ], [ C F ]) :=
$$

subtype(C, comm),

$$
\text { subtype } (S _ {2}, \text { csink }),
$$

subtype(T, time),

relation(P),

$$
\operatorname{domain} (P, [ C, S _ {1}, T, S _ {2}, T ]),
$$

```prolog
if unit-cost(UC, A, L, T) and process-
activity(A, C, L, T) and
index(UC, IUC) and index(A, IA)
then ∃F function(F) and
computed-using(F, [[sum[IUC], [UC, IUC], *, [A, IA]]))

TC = sum(i, j, t, k, t) (F(i, j, t, k, t) * CF(i, j, t, k, t))
```

```txt
subtype(P, shipped-from),
function(F),
domain(F, C, S₁, T, S₂, T]),
range(F, real-number),
fsubtype(F, process-level),
function(CF),
domain(CF, [C, S₁, T, S₂, T]),
range(CF, real-number),
fsubtype(CF, unit-process-cost)
```

The simplest distribution planning problem consists of the base structure with a single type of supply at the source and a single type of demand at the sink such as shown below.

![](/api/attachments/KPD8CHSA/fulltext/images/892ddf76f1ac18db03aadf51affdbccfdde54743916794b93b02052aa74e86de.jpg)

Let the subtypes of comm, csource, csink, and time have indices i, j, k, and t respectively. Then by the index assignment rule shown below, the index of the functions (i.e., variables) F and CF is the list $[i, j, t, k, t]$ .

if domain(F, [A1,..., An]) and index(A1, I1)... and index(An, In) then index(F, app(A1, A2,..., An))

Similarly, the indices associated with the supply function SF and the demand function DF are the list $[i, ij, t]$ and $[i, k, t]$ respectively.

Since F measures the flow from a source to a sink, with supply and demand levels represented by the functions SF and DF, the applications of the transformation in space rule shown below yields the supply and demand constraint referred to using the symbols C1 and C2.

if flow(F, C, L1, T1, L2, T2) and sink(L2, T2) and source(L1, T1)
and index(L2, IL2) and index(L1, IL1) and index(F, IF)
and supply-capacity(SC, C, L1, T1) and demand-requirement(SD, C, L2, T2)

then $\exists F1$ function(F1) and $\exists F2$ function(F2) and computed-using(F1, [[sum, IL2], [F, IF], $\leq$ , [SC, IL1]]) and

computed-using(F2, [[sum, IL1], [F, IF], ≥, [SD, IL2]])

We use standard mathematical syntax for the presentation of indexed variables.

Similarly since F is a type of flow (i.e., the activity level of a transformation in space process) and CF measures unit-cost of flow, the application of the cost structure rule yields the total cost function TC.

The function TC and the constraints C1 and C2 define the schema of the LP model corresponding to the simplest distribution planning problem.

Case 2. The next case consists of the base structure with multiple sources of supply at a source and multiple sources of demand at a sink such as shown below (refer fig. 4)

![](/api/attachments/KPD8CHSA/fulltext/images/35d6616b4b8c5a9659b1b9a7fada60d2eef37a49b7acd66034744f68d43d4b39.jpg)

$$
\phi_ {\mathrm{bdis}} (C, S _ {1}, S _ {2}, T, P, F, C F),
$$

$$
\phi_ {\text { p   u   r   c   h }} (C, S _ {1}, T, S F 1), \phi_ {\text { a   v   a   i   l }} (C, S _ {1}, T, S F 2),
$$

$$
\phi_ {\text { store }} (C, S 1, T, S F 3), \quad \phi_ {\text { store }} (C, S _ {1}, T, D F 1),
$$

$$
\phi_ {\text { sale }} (C, S _ {2}, T, D F 2), \phi_ {\text { req }} (C, S _ {1}, T, D F 3)
$$

Introduce two new measurement functions A and B with domains domain(A, [C, $S_{1}$ , T]) and domain(B, [C, $S_{2}$ , T] to represent aggregate supply and demand at source and sink respectively. The indices of these functions by the index assignment rule are the lists $[i, j, t]$ and $[i, k, t]$ .

![](/api/attachments/KPD8CHSA/fulltext/images/33285969e121a4e0105c2fd65186e58adc1b4d6f058858d9c033b15d4a809006.jpg)

From the point of view of material balance, since aggregate supply is an outflow and the alternative supply functions are inflows, the application of the material balance rule shown below yields:

```txt
if set-of-inputs([[X1, IX1], ..., [Xn, IXn]])
and set-of-outputs([[Y1, IY1], ..., [Yn, IYn]])
Then ∃F, function(F) and
computed-using(F, [[X1, IX1], +, ..., +,
Xn, IXn], ≥,
[Y1, IY1], +, ..., +, [Yn, IYn]])
SF1(i, j, t) + SF2(i, j, t) + ... + SFn(i, j, t)
= A(i, j, t)
```

Applying the same logic to the demand functions, we have:

$$
\begin{array}{l} D F 1 (i, K, t) + D F 2 (i, k, t) + \dots + D F m (i, k, t) \\ = B (i, k, t) \end{array}
$$

Since the functions A and B represent total supply and demand at the source and sink, case 1 applies. The schema of the LP model consists of the case 1 schema with two additional material balance constraints.

Case 3: The base structure $\phi_{\mathrm{bdis}}$ associated with a distribution planning problem may be extended through the addition of a new sets of sources represented by $\phi_{\mathrm{ncsource}}$ .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{\mathrm{ncsource}}(C, NS, S, T, P, F, CF) :=$ subtype(NS, csource), relation(P), domain(P, [C, NS, T, S, T]), subtype(P, shipped-from), function(F), domain(F, [C, NS, T, S, T]), fsubtype(F, process-level), range(F, real-number), function(CF), domain(CF, [C, NS, T, S, T]), range(CF, real-number), fsubtype(CF, unit-process-cost)
</div>

![](/api/attachments/KPD8CHSA/fulltext/images/3c497cbeb11b444fc82f9af263f61fb3f085a49bd598c5d14accb298925cd3f8.jpg)

Let there be N sets of sources, say $S_{1},\ldots,S_{N}$ . Each of these has a set of links to a set of sinks as shown above. Let D1, D2, ..., DN be N new demand functions defined at the sink Si with domains domain(Di, [C, Si, T]) and consequently with indices [i, k, t]. This is shown in the figure below.

![](/api/attachments/KPD8CHSA/fulltext/images/efa106214b14ddcb7084a3acb6b386d7582f3d1e204e537812a564624f31656b.jpg)

Each such new demand function $D_{j}$ may be paired with one of the N supply functions associated with N sets of sources. Each such pairing results in a case 1 or case 2 structure. Since DF, the original demand function at the sink, is an outflow and the newly introduced demand functions are inflows, the application of the material balance rule yields:

$$
\begin{array}{r l} & D 1 (i, k, t) + D 2 (i, k, t) + \dots + D N (i, k, T) \\ & = D F (i, k, T) \end{array}
$$

Since each case 1 structure obtained from the pairing generates 2 supply and demand constraints, the schema has a total of 2N case 1 supply and demand constraints. Similarly, the pairing yields N case 1 cost functions, say TC1,...,TCN. These are summed to yield the total cost function TC using a cost structure rule shown below.

if set-of-costs([C1,...,Cn]) and

set-of-incomes([I1,,,Im])

then $\exists F$ function $(F)$ and

computed-using(F, [C1, +, ..., + Cn], -,

$$
[ I 1, +, \dots , + I m ])
$$

The total cost function $TC$ is:

$$
T C = T C 1 + T C 2 + \dots + T C N
$$

The function TC, the 2N case 1 constraints and the material balance constraint define the LP model schema.

Case 4: Similar to case 3 except that a single set of sources supplies multiple sets of sinks. These are represented as shown below:

$$
\phi_ {\mathrm{ncsink}} (C, S, N S, T, P, F, C F) :=
$$

subtype(NS, csink), relation(P),

domain(P, [C, S, T, NS, T]),

subtype(P, shipped-from),

function(F),

domain(F, [C, S, T, NS, T]),

fsubtype(F, process-level),

range(F, real-number),

function(CF),

domain(CF, [C, S, T, NS, T]),

range(CF, real-number),

fsubtype(CF, unit-process-cost)

$\phi_{\mathrm{bdis}}(C, S_1, NS.S_2, T, P_1.P, F_1.F, CF_1.CF) := \phi_{\mathrm{bdis}}(C, S_1, S_2, T, P, F, CF), \phi_{\mathrm{ncsink}}(C, S_1, NS, T, P_1, F_1, CF_1)$

The proof is similar to case 3, except that N new supply functions are introduced instead of demand functions. The material balance equation relates the new supply function to SF, the original supply function at the source.

Case 5: Two distribution problems with a common set of source and sink node types may be joined to create a transhipment structure as shown below.

![](/api/attachments/KPD8CHSA/fulltext/images/b64d330d131e424e77c5433399d0dd45562011418a3dae5f514fa1919d5895d6.jpg)

$\phi_{\mathrm{dis}}(C, \mathrm{app}(S_1, S_2), \mathrm{app}(S_2, S_3), T, \mathrm{app}([P], [Q]),$ app $(F_1, F_2)$ , app $([CF_1], [CF_2]),$ app $(SF_1, SF_2)$ , app $(DF_1, DF_2)) :=$ $\phi_{\mathrm{dis}}(C, S_1, S_2, T, P, F_1, CF_1, SF_1, DF_1),$ $\phi_{\mathrm{dis}}(C, S_2, S_3, T, P, F_2, CF_2, SF_2, DF_2)$

In the general case there can be N such transhipment locations. Introduce two new functions $A_{i}$ and $B_{i}$ for each set i of transhipment locations. Let $A_{i}$ represent demand at the transhipment location, i.e., the receipt of goods and $B_{i}$ represent supply out of the transhipment location. This reduces the simplest transhipment structure (i.e., two distribution planning problems with a common set of transhipment locations) into two case 1 structures. Generally, if the number of transhipment locations is N, there are $N+1$ case 1 structures obtained through the introduction of the functions such as $A_{i}$ and $B_{i}$ at each transhipment location.

Let $T1sk, \ldots, Tmsk$ be the functions at transhipment location $k$ that measure the inflows (i.e., purchase, production, etc.) of commodity and $T1dk, \ldots, Tqdk$ be the functions that measure outflow of the commodity. Assume that the index of a transhipment location is $w_k$ . Then the index of functions at the transhipment location $i$ is $[i, w_k, t]$ , by material balance we have for each of the $N$ transhipment locations:

$$
\begin{array}{r l} & A (i, w _ {k}, t) + T 1 s (i, w _ {k}, t) + \ldots + T m s (i, w _ {k}, t) \\ & = T 1 d (i, w _ {k}, t) + \ldots + T q d (i, w _ {k}, t) + \\ & B (i, w _ {k}, t) \end{array}
$$

Since the introduction of the functions A and B reduce a problem with N transhipment locations to one with $N + 1$ case 1 structures, there are $2N + 2$ case 1 supply and demand constraints. Similarly, there are $N + 1$ case 1 cost functions which are summed as in the previous case with a cost structure rule to yield the total cost function TC:

$$
T C = T C 1 + \dots + T C N + 1
$$

The function TC, the $2N+2$ supply and demand constraints, and N material balance constraints define the schema of the LP model.

Case 6: Supply and demand levels associated with a distribution planning problem may have upper and lower bounds such as shown below.

$$
\phi_ {\text { purch }} (A, B, C, R, L. D) :=
$$

$$
\phi_ {\text { purch }} (A, B, C, R, D), \phi_ {\text { nib }} (A, B, C, R, L)
$$

$$
\phi_ {\text { p   u   r   c   h }} (A, B, C, R, U. D) :=
$$

$$
\phi_ {\text { p   u   r   c   h }} (A, B, C, R, D), \phi_ {\text { n   u   b }} (A, B, C, R, U)
$$

Similarly, shipment levels may also have upper and lower bounds.

$\begin{array}{rl}\phi_{\mathrm{dis}}(C,S_1,S_2,T,P,LB.F,CF,SF,DF):= & \\ \phi_{\mathrm{dis}}(C,S_1,S_2,T,P,F,SF,DF), & \\ \phi_{\mathrm{lb}}(C,S_1,S_2,T,P,LB) & \\ \phi_{\mathrm{dis}}(C,S_1,S_2,T,P,UB.F,CF,SF,DF):= & \\ \phi_{\mathrm{dis}}(C,S_1,S_2,T,P,F,SF,DF), & \\ \phi_{\mathrm{ub}}(C,S_1,S_2,T,P,UB) & \end{array}$

Let there be three functions F, L, and U where F measures the process-level and L and U are lower and upper bounds. Let I be a list of indices. Then by the bound structures rule shown below, we have:

If min-process-activity(MIL, C, L, T) and max-process-activity(MAL, C, L, T) and activity-level(AL, C, L, T) and index (MIL, IMI) and

computed-using(F, [[MIL, IMI], ≤, [AL, IA], ≤, [MAL, IMA]])

The bound constraint:

$$
L (I) \leq F (I) \leq U (I)
$$

The six cases considered are the only allowed distribution planning problem types and in each case model building rules and transformations exist to build valid LP model schema.

Proposition 2. A PM\* specification that is a valid production planning problem has a corresponding well-formed LP model schema.

Proof. The proof is constructive and follows the definition of the production planning problem. Once again each possible type of production planning problem is shown to have an associated well-formed LP model schema.

There are five cases.

Case 1: The simplest production planning problem consists of a base structure composed of a single type of production process with a single type of input, a single type of output (i.e., product), utilization rates of the input, and production and unit-production-cost of the product as illustrated below.

$\phi_{\mathrm{bprod}}([I], [O], [P], L, T, [M], [U], [F], [CF], [R]) :=$ subtype $(O, \text{product})$ ,

subtype(I, input),
subtype(P, production-process),
subtype(L, plant), subtype(T, time),
relation(U), domain(U, [I, P, LT]),
subtype(U, used-in), relation(M),
domain(M, [O, P, L, T]),
subtype(M, produced-by),
function(F), domain(F, [O, P, L, T]),
range(F, real-number),
fsubtype(F, process-level),
function(CF),
domain(CF, [O, P, L, T]),
range(CF, real-number),
fsubtype(CF, unit-process-cost),
function(R), domain(R, [I, O, P, L, T]),
range(R, real-number),
fsubtype(R, utilization-rate)

![](/api/attachments/KPD8CHSA/fulltext/images/9b794045281a6752fee6b8636c25172b526b417fc00c8f223d95dcac11992907.jpg)

Let the subtypes of product, input, production-process, plant and time have indices i, j, p, l, and t respectively. By the index assignment rule, the indices of the functions F, CF, and R that are subtypes of process-level, unit-process-cost, and utilization-rate are $[i, p, l, t]$ , $[i, p, l, t]$ , and $[i, j, p, l, t]$ respectively.

Since the base structure describes the transformation of an input to a product, the application of the transformation in form rule shown below yields a utilization function, say U:

If rate-of-utilization(X, R, RU, P, L, T) and process-activity(PL, RU, P, L, T) and index(X, IR)
index(P, IP) and index(PL, IPL) and index(RU, IRU)
and index(A, IA) and subtype(Dom, utilized-at) and
domain(Dom, [R, L, T])

Then $\exists$ New function(New) and fsubtype(New, process-level) and fdomain(New, Dom) and domain(New, $[R, L, T]$ ) and computed-using(New, [[sum, IRu], [sum, IP], $[X, IX], *, [PL, IPL]])$

$$
\begin{array}{l} U (j, l, t) = \operatorname{sum} (i) \operatorname{sum} (p) \\ \left(F (i, p, l, t) * R (i, j, p, l, t)\right) \end{array}
$$

The simplest production planning problem combines the base structure with a one or more types of supply alternatives.

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR,$ appSF1, SF2, SF3, SF4), [ ]:= $\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, UR)$ $\phi_{\mathrm{purch}}(I, L, T, R, SF1),$ $\phi_{\mathrm{rec}}(I, L, T, R, SF2),$ $\phi_{\mathrm{avail}}(I, L, T, R, SF3),$ $\phi_{\mathrm{store}}(I, L, T, R, SF4)$

Since each supply function for the input represents an inflow and utilization represents an outflow, the application of material balance yields:

$$
U (j, l, t) \leq S F 1 (j, l, t) + \dots + S F 4 (j, l, t)
$$

Similarly, since F and CF measure the process-level and unit-process-cost of same production process, the application of the cost structure rule yields total cost function, say TC.

The function TC and the material balance constraint define the schema of the LP model for the simplest production planning problem.

Case 2: The base structure employed in case 1 may be extended through the addition of a new type of input to the production process.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{\mathrm{ninp}}(N, O, P, L, T, U, H) :=$ subtype(N, input), relation(U), domain(U, [N, P, L, T]), subtype(U, used-in), function(H), domain(H, [N, O, P, L, T]), range(H, real-number), fsubtype(H, utilization-rate)  
$\phi_{\mathrm{bprod}}(N.I, O, P, L, T, M, V.U, F, CF, R2.R1)$ $\mathbf{\Phi}:=$ $\phi_{\mathrm{bprod}}(I, O, P, L, T, M, U, F, CF, R1),$ $\phi_{\mathrm{ninp}}(N, O, P, L, T, V, R2)$
</div>

Let n be the index of the new type of input N. Then the utilization rate function H for this input would have the index $[i, n, p, l, t]$ . The application of the transformation in form rule yields a new utilization function, say V:

$$
(F (i, p, l, t) * H (i, n, p, l, t))
$$

A production planning problem associates supply functions for each type of input used in a production process. If the supply functions associated with the input type N are $SF1N,\cdots,SFmN$ , the application of material balance yields a new constraint:

$$
V (n, l, t) \leq S F 1 N (n, l, t) + \dots + S F m N (n, l, t)
$$

The addition of a new type of input to a production process results in the addition of a new material balance constraint to the LP model schema of case 1.

Case 3: The base structure in case 1 may be extended through the addition of a new type of production process.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\phi_{nproc}(I, O, P, L, T, R_1, R_2, F_1, F_2, F_3) :=$ subtype $(P, \text{production-process})$, subtype $(I, \text{input})$, subtype $(O, \text{product})$ relation $(R_1)$, domain $(R_1, [I, P, L, T])$, relation $(R_2)$, domain $(R_2, [O, P, L, T])$, subtype $(R_1, \text{used-in})$, subtype $(R_2, \text{produced-by})$, function $(F_1)$, domain $(F_1, [O, P, L, T])$, fsubtype $(F_1, \text{process-level})$, function $(F_2)$, domain $(F_2, [O, P, L, T])$, fsubtype $(F_2, \text{unit-process-cost})$, function $(F_3)$, domain $(F_3, [I, o, P, L, T])$, range $(F_3, \text{real-number})$, fsubtype $(F_3, \text{utilization-rate})$ $\phi_{bprod}(I2.I1, O, p_2.P_1, L, T, N.M, V.U,$ $F2.F1, CF2.CF1, R2.R1) :=$ $\phi_{bprod}(I1, O, P_1, L, T, M, U, F1, CF1, R1)$, $\phi_{nproc}I2, O, P_2, L, T, N, V, F2, CF2, R2)$
</div>

Let the new type of production process be assigned the index q. Since the new type of process produces the same kind of output as the production system, the indices associated with both the process-level and unit-cost functions $F_{1}$ and $CF_{1}$ are $[i, q, l, t]$ . The index of the utilization rate function $R_{2}$ is $[i, j, q, l, t]$ .

There are two cases:

(a) Let the new type of process have an input type different from that currently used in the other processes in the production system. Then this is exactly similar to case 1. If the production process has multiple inputs then it is similar to case 2. This case would result in the generation of a cost function and material balance condition for each input used in the production process.

(b) Let the new type of process have an input type that is the same as that used in other processes. Let this input type J have an index j. By transformation in form we have a utilization function, say T:

$$
\begin{array}{r l} T (j, l, t) & = \text { sum } (q) \text {   sum } (t) \\ F _ {1} (i, q, l, t) ^ {*} R _ {2} (i, j, q, l, t)) \end{array}
$$

If the input type J is used in N distinct types of production processes, there are N such utilization functions. Let the functions $T1,\ldots,TN$ represent the utilization of input type J in each of the N distinct types of production processes. Let $SF_{1},\cdots,SF_{m}$ be the supply functions for input type J. Then by material balance we have:

$$
\begin{array}{r l} & T 1 (j, l, t) + \ldots + T N (j, l, t) \\ & \quad = S F 1 (j, l, t) + S F 2 (j, l, t) \\ & \quad + \ldots + S F m (j, l, t) \end{array}
$$

The addition of a new type of process that utilizes a input type that is currently being used adds an utilization function component to an existing case 1 or case 2 constraint.

The addition of a new type of production process also generates a case 1 cost function, say CN, which becomes a component of the total cost function obtained using the cost structure rule shown below.

if set-of-costs([C1,...,Cn]) and

set-of-incomes([I1,,,Im])

then $\exists F$ function $(F)$ and

computed-using

$$
(F, [ C 1, +, \dots , + C n ], -, [ I 1, +, \dots , + I m ])
$$

Case 4: Product produced may be either be stored and/or sold as shown in the figure below.

$$
\xrightarrow [ \text {production} ]{\quad \downarrow \text {storage from t - 1}} \boxed {\quad \rightarrow \text {supply}}   \boxed {\quad \downarrow \text {storage in t}}
$$

$$
\begin{array}{c} \phi_ {\text { prod }} (I, O, P, L, T, M, U, F, C F, R, S F, \\ D F. D) := \end{array}
$$

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR, SF, D),$

$$
\phi_ {\text { store }} (I, L, T, R, D F)
$$

$$
\begin{array}{l} \phi_ {\text { prod }} (I, O, P, L, T, M, U, F, C F, R, S F, \\ D F. D) := \end{array}
$$

$\phi_{\mathrm{prod}}(I, O, P, L, T, M, U, F, CF, UR, SF, D),$

$$
\phi_ {\text { sale }} (I, L, T, R, D F)
$$

Let there be N production processes in the production system that produce product O. Let the functions that measure the production level of product be $F1,\cdots,FN$ . Let the indices associated with the N production processes be $p_{1},\cdots,p_{n}$ . The index of function $F_{k}$ is $[i,p_{k},l,t]$ .

Let the functions $ST$ and $SA$ measure the sales or storage of a product. The indices associated with these functions are $[i, l, t]$ . From the point of view of material balance, since product stored in any period $t$ and sold in any period $t$ are outflows and product produced in period $t$ and that stored in the previous (i.e., $t-1$ ) are inflows the application of material balance yields

$$
\begin{array}{l} \text { sum } (p) F _ {1} (i, p _ {1}, l, t) + \dots \\ \quad + \text { sum } (p _ {n}) F _ {n} (i, p _ {n}, l, t) + S T (i, l, t - 1) = \\ \quad S T (i, l, t) + S A (i, l, t) \end{array}
$$

The addition of sales or storage of a product thus results in the addition of a material balance constraint.

Case 5: Finally, bounds may be placed on all the process levels. These are directly transformed by the bound structure model building rule.

$$
\begin{array}{r l} & {\phi_ {\mathtt {b p r o d}} (I, O, P, L, T, M, U, U B. F, C F, U R) :=} \\ & {\qquad \phi_ {\mathtt {b p r o d}} (I, O, P, L, T, M, U, F, C F, U R),} \\ & {\qquad \phi_ {\mathtt {p u b}} (O, P, L, T, U B)} \\ & {\phi_ {\mathtt {b p r o d}} (I, O, P, L, T, M, U, L B. F, C F, U R) :=} \\ & {\qquad \phi_ {\mathtt {b p r o d}} (I, O, P, L, T, M, U, F, C F, U R),} \\ & {\qquad \phi_ {\mathtt {p l b}} (O, P, L, T, L B)} \end{array}
$$

Let there be three functions F, L, and U, where F measures the process-level and L and U are lower and upper bounds. Let I be a list of indices. Then by the bound structures rule, we have:

$$
(L (I) \leq F (I) \leq U (I)
$$

These five cases are the only possible types of production planning problems. In each case we have demonstrated how transformations through the application of model building rules produce well-formed LP model schema.

## References

Binbasioglu, M. and M. Jarke, Domain Specific Tools for Knowledge-Based Model Building, Decision Support Systems (1986).

Bradley, S., A. Hax and T. Magnanti, Applied Mathematical Programming (Addison-Wesley, Reading, MA, 1977).

Bu-Halaiga, M. and H.K. Jain, An Interactive Plan Based Procedure for Model Integration in DSS. Proceedings of the 21st Annual Hawaii Conference on the System Sciences (Kona, HI, 1988).

Dowty, D.R., R.E. Wall, and S. Peters, Introduction to Montague Semantics (Reidel, Dordrecht, 1978).

Geoffrion, A.M. and G. Graves, Multicommodity Distribution System Design by Benders Decomposition, Management Science 20, No. 5 (1974) 822–844.

Geoffrion, A.M., SML: A Language for Structured Modeling, Working Paper (Western Management Science Institute, University of California, Los Angeles, CA, 1988).

Glover, F., G. Jones, D. Karney, D. Klingman and J. Mote, An Integrated production, Distribution and Inventory Planning System, Interfaces 9, No. 5 (1979) 21–35.

Glover, F. and D. Klingman, Mathematical Optimization - A successful Tool for Logistics Problems, Operational Research, J. Brans, ed., North-Holland, Amsterdam, 1981).

Glover, F. and D. Klingman, Tutorial on Networks, CBDA 118 (Center for Business Decision Analysis, University of Texas, Austin, TX, 1984).

Hackman, S. and R. Leachman, A General Framework for Modeling Production, Working Paper (Operations Research Center, University of California, Berkeley, CA, 1986).

Helferich, O.K., An Introduction to Logistics Decision Sup-

port Systems, Computers in Distribution, (Auerbach, Pennsauken, NJ, 1983).

Kendrick, D. and A. Meeraus, GAMS: An Introduction, The World Bank (Scientific Press, Palo Alto, January, 1987).

Kendrick, D., A. Meeraus and J. Alatorre, The Planning of Investment Programs in the Steel Industry (Johns Hopkins University Press, Baltimore, MD, 1983).

Klingman, D., N. Phillips, D. Steiger, R. Wirth, R. Padman and R. Krishnan, An Optimization Based Integrated Short-Term Refined Petroleum Product Planning System, Management Science 33, No. 7 (1987) 813–830.

Krishnan, R., Knowledge-Based Aids for Model Construction, Unpublished Ph.d. Thesis (University of Texas, Austin, TX, 1987).

Krishnan, R., PDM: A Knowledge-Based Tool for Model Construction, Proceedings of the 22nd Annual Hawaii Conference on the System Sciences (Kona, HI, 1988a).

Krishnan, R., Automated Model Construction: A Logic Based Approach, Annals of Operations Research, Issue on Linkages with Artificial Intelligence (1988b).

Ma, P., F. Murphy and E.A. Stohr, The Science and Art of Formulating Linear Programs, IMA Journal of Mathematics in Management (1986).

Muhanna, W. and R. Pick, Composite Models in SYMMS. Proceedings of the 21st Annual Hawaii Conference on the System Sciences (Kona, HI, 1988).

Murphy, F. and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems (1986).

Reiter, R., Towards a Logical Reconstruction of Relational Database Theory, in: On Conceptual Modeling, Brodie et al., eds. (1984).
