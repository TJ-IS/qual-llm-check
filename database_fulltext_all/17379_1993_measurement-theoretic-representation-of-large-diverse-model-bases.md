---
otero_id: 17379
otero_key: "F9ZJNV3W"
title: "Measurement theoretic representation of large, diverse model bases"
authors: "Sa Neung Hong; Michael V. Mannino; Betsy Greenberg"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90066-c"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Measurement theoretic representation of large, diverse model bases

The unified modeling language $\mathcal{L}_{\mathrm{U}}$

Sa Neung Hong, Michael V. Mannino and Betsy Greenberg

The University of Texas at Austin, Austin TX, USA

The philosophy and features of the Unified Modeling Language $L_{U}$ are presented with emphasis on the support of large, diverse model bases. We argue that measurement theory stressing homomorphic mappings from empirical to mathematical systems is an ideal foundation for integrated modeling environments. Homomorphic mappings are an integral part of the semantics of the $L_{U}$ and motivate a number of language features that support large, diverse model bases. The $L_{U}$ provides a separate but uniform representation of domain worlds and mathematical systems known as model types. Domain worlds are composed of empirical objects, relations, and functions organized into classes and attributes, while model types are defined by standard queries and a rich collection of assumptions. To emphasize the importance of homomorphic mappings, unification constraints combine common patterns of domain and mathematical knowledge in model templates. Reusability and incremental refinement are supported by inheritance based on partial order relations for classes, attributes, assumptions, and model types. Together, the semantic foundation and language features provide a practical and formal knowledge representation for large, diverse model bases.

Keywords: Modeling language; Measurement theory; Formal semantics; Homomorphism; Knowledge representation and organization

## 1. Introduction

Model management is widely recognized as a key component of decision support systems because of the importance of models in decision making. The primary role of model management is the convenient and efficient update, retrieval,

![](/api/attachments/F9ZJNV3W/fulltext/images/5c9223968e3dec7f995e1f3a2311dd18026c959ea6d5b77f50e9e14a86d5605e.jpg)

Michael V. Mannino received a B.B.A. degree from the University of Cincinnati in 1978 and an M.S. and a Ph.D. degree both from the University of Arizona. Tucson in 1981 and 1983, respectively. He was an assistant professor in the Department of Management Science and Information Systems at the University of Texas at Austin. He joined the Department of Management Science, University of Washington, Seattle in September 1991. Dr. Mannino teaches

and conducts research in the areas of database management, software engineering, and knowledge representation. His articles have appeared in major journals including IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, ACM Computing Surveys, MIS Quarterly, Journal of Management Information Systems, and ORSA Journal on Computing.

![](/api/attachments/F9ZJNV3W/fulltext/images/59c54a6755c9e74c6d2d82914e421a2f861f9d2d06fa3df0fd2e47a3f8e10024.jpg)

Betsy Greenberg is an Assistant Professor at the University of Texas at Austin. She received a bachelors degree in Electrical Engineering from Brown University and a Ph.D. in Operations Research from the University of California, Berkeley. Her research interests are primarily in stochastic processes and queueing systems. She has recently developed an interest in model management.

![](/api/attachments/F9ZJNV3W/fulltext/images/f135d557dc9fcf26304764c3aae17348149c777e19bb291fac2aa9577fb4595e.jpg)

Sa Neung Hong received a B.Ag. degree from the Seoul City University in 1976 and a Ph.D. degree from the University of Texas, Austin in 1991. He is currently a lecturer of information systems in the Department of Management Science and Information Systems at the University of Texas at Austin. His research interests are in model management, integration of modeling paradigms, constraint satisfaction problems, distributed systems, telecommunication, and organizational computing.

and execution of models. Frequently, model management systems have emphasized these functions in relation to specific modelling languages, management science paradigms, and application domains. As management science techniques have become more widely accepted in organizations, there is a need to integrate the tools and models used in decision support systems. Model integration emphasizes large model bases containing complex models based on diverse management science paradigms and application domains. Model integration involves knowledge intensive tasks such as model formulation, model reuse, model analysis, and output interpretation.

To achieve integration, the underlying modeling language should adhere to the following principles:

(1) declarative. Use specification and inference as the basis of model specification;

(2) uniform. Represent multiple application domains and modeling paradigms in a uniform notation. This is similar to Geoffrion's [19] idea of neutrality;

(3) broad. Maintain knowledge about the defining properties of application domains and modeling paradigms;

(4) independent. Separate application domains and mathematical knowledge;

(5) controlled. Support meaningful combinations of application domains and mathematical knowledge to form models;

(6) incremental. Support refinement of models, application domains, and modeling paradigms by level of generalization and detail;

(7) rigorous. Possess a clear semantics consistent with measurement theory.

In this paper, we describe the unified modeling language $(\mathcal{L}_{\mathrm{U}})$ that supports these principles of model integration. Foremost, the $L_{U}$ uses the discipline of logic modeling [23]. Mathematical models are defined declaratively using predicates and standard queries rather than algebraically. This promotes a clean separation between the specification of a model and its associated solvers. Logic modeling also promotes a uniform and deep representation of mathematical models and domain worlds. Models can be represented in an individual level for detailed reasoning and a class level representation for model formulation.

Independence, control of meaningful combinations, and incremental refinement are important practical themes of integrated modeling environments. The $L_{U}$ separates domain and mathematical components to promote parallelism and autonomy in their development. The domain component represents empirical worlds. At the individual level, a domain world is described by objects, relations, and functions. At the class level, the domain world is organized into classes and attributes. The mathematical component represents model types (i.e., modeling paradigms) as collections of assumptions covering standard mathematical relations. Domain and mathematical knowledge are meaningfully combined in model templates through explicit unification constraints and attribute realizations. Reusability and incremental refinement are supported by inheritance based on partial order relations for attributes, assumptions, and model types. These partial order relations extend notions of interface compatibility and behavioral compatibility in object-oriented programming.

A formal semantics is an essential element of language design because it provides meaning to syntactic expression, it is a guide to implementation, and it permits reusing and extending language definitions. For model management languages, measurement theory provides an attractive basis for the semantics because it is concerned with homomorphic mappings from empirical worlds to mathematical systems. The $L_{U}$ is unique because its semantics is based on homomorphic mappings from empirical relations and functions to mathematical relations and functions.

In the following, we proceed in section 2 by discussing the semantic foundation of $L_{U}$ and the role of homomorphisms to combine logic and mathematical modeling. Section 3 defines the $L_{U}$ through a summary of its syntax, numerous examples, and a brief discussion of its semantics. Section 4 presents partial order relations for classes, attributes, assumptions, and model types. Section 5 compares our work to previous work. Section 6 summarizes the paper and identifies further directions of research.

## 2. A unified view of mathematical modeling

In this section, we develop a framework which accommodates our design goals for integrated modeling systems. The framework is composed of three parts: Measurement theoretic view of mathematical modeling; conceptualization of modeling worlds; and representation scheme. Measurement theory provides a foundation for uniform representation of models based on different mathematical paradigms. In addition, the theory integrates logic and mathematical modeling. Modeling worlds are conceptualized set theoretically. The conceptualization underpins the design of our modeling language described in the next section. Lastly, the representation scheme is carefully developed to maintain independence between domain and mathematical knowledge as well as to control meaningful combinations.

## 2.1. Measurement theoretic approach to mathematical modeling

We view mathematical modeling as developing a measurement system which facilitates reasoning about the domain world. Here, measurement means assignment of numbers to domain objects such that the assigned numbers, together with numeric relations and functions, reflect the properties of the domain world. Measurement theory provides an appealing basis to abstract mathematical models in a uniform way since it is concerned with homomorphic mappings from empirical worlds into mathematical systems.

A measurement function is fundamental if the mapping is defined directly from an empirical system to a mathematical system. A measurement function is said to be derived if it is defined in terms of other measurement functions. Measurement theory is mainly concerned with two basic problems: Representation and uniqueness. The representation problem is to find sufficient conditions for the existence of a homomorphism from an empirical system to a given mathematical system. The conditions are called representation axioms and the existence of the measurement is stated by representation theorems. Uniqueness theorems define the properties and valid operations of different measurement systems.

As an example of fundamental measurement, consider extensive measurement that defines a homomorphism h embedding $\langle A, r, f \rangle$ into $\langle N, >, + \rangle$ where r is a binary relation and f is a binary operation over the objects in A, and N is the set of real numbers. The axioms for extensive measurement are:

(1) the operation $\mathbf{f}$ is weakly associative;

(2) $\langle \mathbf{A},\mathbf{r}\rangle$ is a strict weak order;

(3) the operation $\mathbf{f}$ is monotonic with respect to $\mathbf{r}$ ; and

(4) $\langle A, r, f \rangle$ is Archimedian. $^{1}$

The representation theorem states that if the above axioms are satisfied there exists a real valued function h on A which embeds the former relational system into the latter. The uniqueness theorem states that h is a ratio scale. (See [33] for details of the axioms and theorems.) Other types of measurement require different sets of axioms and embed empirical relational systems into different mathematical relational systems.

Extensive measurement defines a set of empirical relational systems which are embeddable into the mathematical system $(N, >, +)$ . An instance of this set is $\langle Iron-Bars, is longer than, connect\rangle$ where Iron-Bars denotes a set of iron bars and connect an operation connecting two iron bars. The representation theorem of extensive measurement states that we can define a real valued function, say length, over the iron bars to preserve the relation is longer than by > and the function connect by +. Therefore, mapping length as an instance of extensive measurement assigns real numbers to iron bars such that

is-longer-than $(bar_{i}, bar_{j})$

$$
\Leftrightarrow \text { length } (b a r _ {i}) > \text { length } (b a r _ {j})
$$

$$
\begin{array}{r l} c o n n e c t (b a r _ {i}, b a r _ {j}) & = c o n n e c t (b a r _ {k}, b a r _ {l}) \\ & \Leftrightarrow l e n g t h (b a r _ {i}) + l e n g t h (b a r _ {j}) \\ & = l e n g t h (b a r _ {k}) + l e n g t h (b a r _ {l}), \end{array}
$$

for all $bar_i$ , $bar_j$ , $bar_k$ and $bar_l$ .

To illustrate our view of mathematical modeling as developing a measurement system, consider a decision maker who wants to know the total length of a set of iron bars. Suppose that the length of the individual iron bars are already measured. Conceptually, the decision maker is measuring the length of an object, say $bar_{0}$ , which is constructed by connecting all iron bars. Here, the decision maker implicitly assumes the existence of $bar_{0}$ . With an empirical operation connect, the construction of $bar_{0}$ is specified as follows.

$$
\begin{array}{c} \text {bar} _ {0} = \text {connect} \big (b a r _ {1}, \text {connect} \big (b a r _ {2}, \dots \\ \big (\text {connect} \big (b a r _ {n - 1}, b a r _ {n} \big) \dots \big) \big). \end{array}
$$

Of course, the decision maker can measure the length of $bar_{0}$ as an instance of extensive measurement, i.e., by assigning a number as the value of the length of $bar_{0}$ . But that is not the intention of formulating a mathematical model. Instead, the decision maker wants to define a measurement function, say totlength, that will compute the total length of the iron bars in terms of the measurement function length. For the computation, the decision maker assumes that the primitive measurement function length is additive to totlength. The assumption allows the decision maker to compute totlength by the following mathematical formula.

$$
\begin{array}{r l} \text {totlength} (b a r _ {0}) & = \text {length} (b a r _ {1}) + \dots \\ & + \text {length} (b a r _ {n}). \end{array}
$$

Mathematical modeling is analogous to developing a measurement system. In mathematical modeling one specifies the decision problem, identifies the mathematical system into which the domain world is to be embedded, makes assumptions for the embedding, and defines the required measurement functions. In the above example, the decision problem is to determine the total length of iron bars, the domain world, composed of iron bars with the is longer than relation and the connect function, is mapped into the mathematical system $(N, >, +)$ by the given measurement function length, and the additivity assumption is made to define totlength as the sum of the lengths of individual bars. Note that we use the term ‘assumption’ instead of ‘axiom’ since models are based on assumptions to generate alternative scenarios rather than true beliefs.

With this measurement theoretic view, one abstracts mathematical models in a uniform way regardless of the underlying mathematical paradigm. For example, EOQ models can be abstracted as a system of measuring the optimum order quantity and the reorder point, and M/M/1 queueing models as a system of measuring characteristics of a queueing system such as average time in the queue or average number of customers in the system. As in measurement theory, the view emphasizes the assumptions about the structure of domain worlds. We believe that the assumptions such as the constant demand rate and the deterministic lead time for EOQ models, and Poisson process of customer arrivals and exponential distribution of service times for M/M/1 queueing models are more important than the algebraic specification of model solutions. Also the view allows us to combine mathematical modeling with logic modeling since measurement theory constructs the domain world as the relational system which is the semantic domain of first-order logic languages. We describe the scheme to represent mathematical models as a measurement system in the remainder of this section, and define the syntax of our modeling language $L_{U}$ in the next section.

## 2.2. Conceptualization of modeling worlds

Following first-order model theory, we conceptualize the application domain and the mathematical system as relational systems and call them domain world and the mathematical system, respectively. The two systems are connected by homomorphic mappings. Use of mathematical systems requires the constraints that the application domain should satisfy for correct reasoning. We conceptualize the constraints as structural assumptions and separate them from the other elements. Therefore, the semantic domain is composed of a domain world and a mathematical system, and homomorphisms and assumptions specifying the connections between the two relational systems. Formally, the semantic domain of modeling language $L_{U}$ is the following tuple:

$$
\mathcal {W} = \langle \mathbf {O}, \mathbf {N}, \mathbf {R} _ {\mathrm{E}}, \mathbf {R} _ {\mathrm{N}}, \mathbf {F} _ {\mathrm{E}}, \mathbf {F} _ {\mathrm{H}}, \mathbf {A} \rangle ,
$$

where:

O is the set of application domain objects; N is the set of numeric objects (real numbers); $R_{E}$ is the set of relations over O;

$$
\mathbf {R} _ {\mathrm{E}} = \mathbf {R} _ {\mathrm{D}} \cup \mathbf {R} _ {\mathrm{M}} \cup \dots ;
$$

$R_{D}$ is the set of relations showing the dependencies among the objects in O;

$R_{M}$ is the set of measurable relations defined over O;

$F_{E}$ is the set of functions defined over O;

$$
\mathbf {F} _ {\mathrm{E}} = \mathbf {F} _ {\mathrm{M}} \cup \dots ;
$$

$\mathbf{F}_{\mathbf{M}}$ is the set of mathematically computable functions over $\mathbf{O}$ ;

$\mathbf{R}_{\mathbf{N}}$ is the set of relations over $\mathbf{N}$ ;

$\mathbf{F}_{\mathbf{N}}$ is the set of functions over $\mathbf{N}$ ;

$F_{H}$ is the set of homomorphic mappings from O to N;

A is the set of assumptions; an assumption a is a subset of $(2^{\mathbf{O}} \cup \mathbf{F}_{\mathrm{H}})^{n} \times \mathbf{N}^{m};^{2}$

$F_{E}, F_{N}$ and $F_{H}$ may have partial functions.

Without loss of generality, we define N as the set of real numbers. But it can be any set of mathematical objects that obey specified properties. Note that we keep the domain world separated from the mathematical system for clear semantics and explicit connections between the two systems.

Dependency relations represent the structure of complex and/or abstract objects showing the interrelationships among the domain objects. They are similar to 'part-of' or 'structured-as' relations. They have been defined informally as indexes in GAMS [31], and formally but in an awkward way as the calling sequences of entities in Structured Modeling [18]. We precisely formalize them in the representation of domain objects and classes. The formal representation of dependencies is useful for reasoning about indexes and validating model completeness.

An n-ary empirical relation $r_{M}$ is measurable and thus is in $R_{M}$ if and only if there exists an n-ary numeric relation $r_{N}$ in $R_{N}$ and a (partial) mapping $f_{H}$ in $F_{H}$ such that

$$
\mathbf {r} _ {\mathrm{M}} \left(\mathbf {o} _ {1}, \dots , \mathbf {o} _ {n}\right) \Leftrightarrow \mathbf {r} _ {\mathrm{N}} \left(\mathbf {f} _ {\mathrm{H}} \left(\mathbf {o} _ {1}\right), \dots , \mathbf {f} _ {\mathrm{H}} \left(\mathbf {o} _ {n}\right)\right),
$$

for all $\mathbf{o}_1, \ldots, \mathbf{o}_n$ in $\mathbf{O}$ . Similarly, an $n$ -ary empirical function $\mathbf{f}_N$ is mathematically computable and thus is in $\mathbf{F}_M$ if and only if there exist an $n$ -ary numeric function $f_{N}$ in $F_{N}$ and a (partial) mapping $f_{H}$ in $F_{H}$ such that

$$
\begin{array}{r l} & {\mathbf {f} _ {\mathrm{M}} (\mathbf {o} _ {i _ {1}}, \ldots , \mathbf {o} _ {i _ {n}}) = \mathbf {f} _ {\mathrm{M}} (\mathbf {o} _ {j _ {1}}, \ldots , \mathbf {o} _ {j _ {n}}) \Leftrightarrow} \\ & {\qquad \mathbf {f} _ {\mathrm{N}} \big (\mathbf {f} _ {\mathrm{H}} (\mathbf {o} _ {i _ {1}}), \ldots , \mathbf {f} _ {\mathrm{H}} (\mathbf {o} _ {i _ {n}}) \big)} \\ & {\qquad = \mathbf {f} _ {\mathrm{N}} \big (\mathbf {f} _ {\mathrm{H}} (\mathbf {o} _ {j _ {1}}), \ldots , \mathbf {f} _ {\mathrm{H}} (\mathbf {o} _ {j _ {n}}) \big),} \end{array}
$$

for all $o_{i_{1}},\ldots,o_{i_{n}}$ , $o_{j_{1}},\ldots,o_{j_{n}}$ in O. Usually, measurable relations and mathematically computable functions are not represented explicitly in models, but inferred from mathematical relations and functions through homomorphic mappings.

## 2.3. Representation of modeling worlds

We propose a representation system with three major features: (1) independence between domain and mathematical knowledge with control of meaningful combinations; (2) multiple reasoning processes with user control; and (3) inheritance of domain and mathematical knowledge. Domain worlds represent empirical or observable objects, relations among objects, and functions. At the individual level, a domain world defines an object by an identifier, a dependency relation, and a collection of measurable attributes. At the class level, a domain world is organized into sets of objects where each set has a class identifier, a dependency relation among classes and a collection of attributes. Model types uniformly represent mathematical systems (i.e., management science paradigms) as assumptions, function definitions, and standard queries with associated solution procedures. Domain and mathematical knowledge are meaningfully combined in model templates. Unification constraints in a model template propagate the assumptions and standard queries of a model type to elements of a domain world. A model instance binds a model template to sources of input data. Fig. 1 shows the overall view of our representation scheme.

The second feature of our representation system is multiple reasoning processes controlled by queries from the model user. If the requested reasoning is about the value of a measurement function and the measurement function is defined as one of the standard queries, it is computed by the associated solution procedure. If the requested reasoning is about the value of a measurement function but the function is not defined in the standard queries, the system invokes the general mathematical computations. If the requested reasoning is not about the value of a measurement function, the system tries to answer the question using logical deduction. It is also possible to augment the reasoning support with other reasoning mechanisms such as database queries and expression evaluations.

![](/api/attachments/F9ZJNV3W/fulltext/images/75a9c780d7646b9b8a0fb06131b19c7e37eddd5ec1f2a1b1cba4fe0a0ac27a90.jpg)  
Fig. 1. Overview of modeling world representation.

The third feature of the representation system is inheritance to support incremental refinement and reuse of domain worlds and model types. Classes in domain worlds share the attributes and dependencies of more general classes. Inheritance for domain worlds is based on interface compatibility to emphasize substitution among worlds. Model types share the assumptions of more general model types. Inheritance for model types is based on behavioral compatibility, stronger than interface compatibility, to emphasize the similarity of assumptions among model types.

## 3. The unified modeling language $L_{U}$

The unified modeling language $L_{U}$ is designed to reflect the unified view of modeling. Since mathematical models are viewed as measurement systems, the $L_{U}$ uniformly represents management science paradigms as assumptions and queries instead of algebraic equations. Modeling elements identified in the subsection 2.2 are represented in a domain-world and a model-type, and meaningfully combined into a model-template. The combination is specified by unification constraints that propagate the assumptions and queries specified in the model-type to the domain-world. A model-instance provides the data to a model-template for detailed reasoning. Overall, the language keeps the balance between the domain and mathematical aspects in modeling. This section defines the syntax of $L_{U}$ , and illustrates the language with examples. The formal semantics of the language is also briefly discussed.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
domain-world := &lt;world-id, individual-world, class-world&gt;
individual-world := individual-list$^{+}$
individual := &lt;ind-id, ind-dep, attr-spec-list$^{+}$&gt;
attr-spec := attr-val [in ind-unit]
ind-unit := unit | unit-var
attr-val := val | ind-term | alg-expr
ind-term := ? | ind-id.pos
ind-dep := &lt;ind-id-list&gt;
class-world := class-def-list
class-def := class-id=class-dep:{attr-def-list$^{+}$}
class-dep := &lt;cdp-list&gt;
cdp := class-id | All(class-id) | Some(class-id)
attr-def := attr[:range [in class-unit]]
range := set | set-id | interval | range-var
class-unit := unit | dimension | unit-var
</div>

## 3.1. Description of domain worlds

A domain-world describes a decision situation. The description is further decomposed into an individual-level (individual-world) and a class-level description (class-world). The individual world is uninterpreted. The class world provides the meanings of the individual-level elements. In the analogy of relational databases, individual-world is the extensions of relations and class-world is the schemata of the relations. In spreadsheet models, the former is values with cell identifiers and the latter is labels. In general, the individual-world is required for detailed reasoning such as model solution and the class-world for high-level reasoning such as model formulation and interpretation. Thus, a user will only specify the individual-world for small problems. For large problems, the domain-world will be generated after the model is instantiated from external sources. Table 1 shows the syntax for the description of domain worlds. $^{3}$

An (individual-world) is specified by a set of individual objects. Each individual is described by a tuple of an identifier (ind-id), its dependency (ind-dep), and a list of attribute value specifications (attr-spec-list). An ind-id denotes an individual object in the domain world. The dependency shows what objects are required for the existence of the object being defined. Roughly speaking, it represents 'part-of' or 'structured-as' relationship. Elements in attr-spec-list composed of pairs of a numeric value and its measurement unit. They (attr-spec's) are referenced by their position within the attr-spec-list concatenated to the associated ind-id. For example, id.3 refers to the third attribute specification of an individual object denoted by id.

An attr-spec is specified by a value (attr-val) and its unit (ind-unit). The attribute value is known, unknown, or computed. Unknown values are noted by a question mark(?) . Computed values are specified by algebraic expressions. An algebraic expression in the individual world does not include class-level objects. Each attribute value is a mathematical object describing an aspect of the associated domain object. The specific meaning of the attribute value is provided by an attribute definition when the class-level description is combined with a class-level description. The ind-unit specifies the dimension along which the associated attribute value is measured or computed. In individual-world, it is specified by a specific measurement unit or a unit variable. Unit variable are used to partially specify the constraints on the attribute values without committing to a specific unit. They are instantiated by an attribute definition in a class-world. The attribute value or unit is extracted by concatenating the keyword value or unit to the referenced specification; e.g., id.3.value or id.3.unit.

A class-level specification (class-world) is described by a set of class definitions. A class identifier (class-id) denotes a set of objects, and is defined by a class dependency (class-dep) and a set of attribute definitions (attr-def-list). The class dependency summarizes the dependencies of the objects in the class. The elements of a class-dep are a class, or an object set constructed by applying the aggregator (All) or the powerset constructor (Some) to a class. All creates a singleton set composed of all objects in the argument class. Some constructs a class which is a subset of the powerset of the argument class. Note that complex index requirements requiring the use of Boolean expressions are not specified in class definitions. Instead, complex index requirements are specified in model instances (see section 6).

An attribute denotes a mapping from the domain objects to mathematical objects. It is defined to reflect a measurable relation in the domain world. The mapping is fully specified with the attribute name (attr), the mapping range (range), and the unit specification (classunit). The range denotes a set of mathematical objects, and it can be specified with a set (set), a set identifier (set-id), an interval (interval) or a range variable (range-var). In addition to specific measurement units and variables, the class-unit may be a dimension such as currency and length. This generality expands the applicability of class-level specifications. Range and unit variables, used to partially specify the relationship between attributes, are instantiated when the attribute is combined with a definite specification of the ranges and units. The unit and range of an attribute definition is referenced by concatenating the keyword unit and range to the attribute identifier; attr.unit and attr.range.

When a class-world is combined with a individual-world, the system uses unit and range information to maintain model integrity. If ind-unit is specified, it should be compatible with class-unit. If dimension is specified in the class-world, the ind-unit should be an instance of the dimension. For example, mile is compatible with km by conversion, and the unit hour is an instance of the time dimension. The range limits the attribute values in the individual-world. For example, it is not possible to make an attribute value 350 in g an instance of an attribute definition attr:1..5 in kg since the value is not within the specified range. Therefore, range and unit specification limits the combination of a attr-def and attr-spec's within a domain-world to meaningful one.

We use the following scenario describing a decision situation of a production manager as an example of domain world descriptions.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Id: Product-Mix Planning
IW:  $\langle a,\emptyset,[3\ in\ /box,?\ in\ box]\rangle,\langle b,\emptyset,[4\ in\ /kg,?\ in\ kg]\rangle,$ $\langle x,\emptyset,[18\ in\ U_{1},(a.2\times u_{1}.1+b.2\times u_{3}.1)\ in\ U_{1}]\rangle,$ $\langle y,\emptyset,[12\ in\ U_{2},(a.2\times u_{2}.1+b.2\times u_{4}.1)\ in\ U_{2}]\rangle,$ $\langle u_{1},(x,a),[2\ in\ gm/can]\rangle,\langle u_{2},(y,a),[3]\rangle,$ $\langle u_{3},(x,b),[2\ in\ gm/kg]\rangle,\langle u_{4},(y,b),[1]\rangle,$ $\langle p,(x,y,a,b),[(a.1\times a.2+b.1\times b.2)\ in\ $]\rangle]$ 
CW: [PRODUCT = ∅ :{unit-price:R$^{+}$ in $/U$_{3}$, prod-level:R$_{1}$ in U$_{3}$}, RESOURCE = ∅ :{availability:3..80 in kg, usage:2..70 in kg}, USE = (RESOURCE, PRODUCT) :{unit-usage:R$^{+}$ in kg/U$_{3}$}, PRODUCTION = (All(RESOURCE), All(PRODUCT)) :{revenue:in currency}]
</div>

Fig. 2. Product mix planning.

Company ABC manufactures products a and b whose unit prices are three and four dollars, respectively. For the production of one unit of a, two and three units of resources x and y are required, while for one unit of b, two and one units of each resource. During the planning period, 18 and 12 units of x and y are available in total.

We name the problem as Product Mix Planning. Fig. 2 shows its specification in $\mathcal{L}_{\mathrm{U}}$ .

The products denoted by a and b and the resources denoted by x and y are primitive objects. They do not depend on other objects, and so have empty dependencies. The uses of the resources by the products $(u_{1}, u_{2}, u_{3}, \text{and } u_{4})$ and the production activity $(p)$ are non-primitive objects, and their existence is valid only if the products and resources are defined in the model. Three formulas are defined to compute attribute values, and two values are unknown. The formulas show the interdependency of attribute values. For example, the formula in the last tuple in the IW section states that the attribute value of p is determined by the first and second attribute values of a and b. Note that dependency specification (ind-dep) are different from attribute value dependencies. They are distinguished because one represents existential dependency while the other computational dependency. Accordingly, the former is represented by the ind-dep, and the latter (implicitly) by the alg-expr. (See the definitions of x and y in the IW section). Given the above specification, computing the unknown values of a and b (production levels) is the task of model solution.

The specification shows that the first attribute of a has value 3 dollars per box, and the second attribute value is unknown but measured (or computed) in boxes. The unit variables $U_{1}$ and $U_{2}$ are used for the first and second attribute specifications of x and y, respectively, and thus the unit specifications lay the constraint that the two attribute values of the resource objects should be measured in terms of the same unit. Also, unit specifications enforce correctness of algebraic expressions and permit automatic unit conversion. To illustrate, consider the specification of x.2. It is equivalent to the following:

$(a_{2}.\text{value in box} \times 2$ in gm/can

$$
+ b. 2. \text { value   in } k g \times 2 \text { in } g m / k g) \text { in } U _ {1}.
$$

By factoring out units, we have the following unit equation:

$$
\left(b o x \cdot g m / c a n + k g \cdot g m / k g\right) i n U _ {1}.
$$

The equation tells us that the algebraic expression is ill-defined if the unit box is incompatible with can. If the two units are compatible, the unit equation becomes gm in $U_{1}$ , and when $U_{1}$ is instantiated the system converts gm into another unit or detect a unit error depending on the value of $U_{1}$ .

PRODUCT and RESOURCE are primitive classes because they have empty dependencies. USE and PRODUCTION are non-primitive classes, and their definitions are valid only if the other classes they depend on are defined in the same model. Note the difference between the dependencies of USE and PRODUCTION. The objects in USE depend on one object in RESOURCE and one in PRODUCT, while those in PRODUCTION on all resources and all products at once. The attributes are defined to preserve some meaningful relations in the domain world with the well-defined relations in mathematical systems. For example, revenue if defined correctly should reflect a relation, say prefer to, such that, for two different productions $p_{1}$ and $p_{2}$ , the manager does prefer $p_{1}$ to $p_{2}$ iff $revenue(p_{1}) > revenue(p_{2})$ .

The unit specification at the class level is usually more general than that at the individual level. This generality allows attribute definitions to be instantiated into attribute specifications with different units. For example, both a and b can be instances of PRODUCT since units of their attribute specifications satisfy the unit constraint defined in PRODUCT attributes. Also, the unit currency of PRODUCTION.revenue allows attribute values measured not only in dollars but also in British pounds. Combined with elements at the individual level, the range specification sets the limits of attribute values. When a unit is converted into another, the associated range should converted as well. For example, 2..7 in km becomes 2000..7000 in m if we convert the unit km into m. The unit $U_{3}$ constrains the relationship between the unit usage and production level.

The separation of the individual-world and class-world supports flexibility of modeling. The individual-world will usually be empty for large, complex problems. This permits the class-world to be combined with different model types for different mathematical assumptions, and with different model instances where the individual-world is populated. The separation promotes efficient data organization and facilitates testing different scenarios.

## 3.2. Description of mathematical systems

A model type (model-type) defines a mathematical system that can be applied to construct models for a specific type of decision problem. Model types are generally created by management scientists who rigorously define their properties. In our framework, a model type is defined by two different sets of assumptions: Existential and structural. The existential assumptions (EA-list) declare what kinds of objects should exist in the domain world. If a model type is independent of application domains, it is specified by pairs of a class variable and an attribute variable. If a model type is defined for a specific domain, it is specified by the classes in the domain. To maximize the applicability, we require that existential assumptions in a domain dependent model type to be as general as possible. The dependency of model types on application domains determines the types of unification when a model type is applied to decision problems.

The structural assumption set (SA-list) defines the mathematical properties of the model type. Each assumption is specified by a predicate followed by arguments within parentheses. We can view assumption predicates as the important

```txt
Table 2
Model type syntax.
```

```txt
model-type:=
    <model-type-id, EA-list+, SA-list, MD-list, SQ-list>
EA ``existential assumption `' := class-var.attr-var | class-def
SA ``structural assumption `' := assump-pred(arg-list+)
arg := val | class-term | alg-expr
class-term :=
    class-id | class-var | class-id.attr | class-var.attr-var
MD ``metric definition `' := metric = alg-expr
metric := class-id.attr-def | class-var.attr-var
SQ ``standard query `' :=
    query = solver-expr | query with solver-list+
solver-expr := alg-expr
query := [fop] metric [s.t. alg-eqn-list]
alg-eqn := alg-expr rop alg-expr
```

modeling concepts. The arguments are the second-order elements representing the domain world - classes and attributes - optionally followed by numbers or algebraic expressions. The assumptions are similar to the representation axioms in measurement theory or the axioms and postulates in abstract systems. Therefore, a domain world should satisfy the assumptions in order to utilize the mathematical system for modeling.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Id: LP Type
EA-list:  $[C_{1}.a, C_{2}.b, C_{3}.c, C_{4}.x, C_{5}.lhs, C_{6}.z]$ 

SA-list:  $[deterministic(C_{1}.a), constant(C_{1}.a), deterministic(C_{2}.b), constant(C_{2}.b), deterministic(C_{3}.c), constant(C_{3}.c), le(C_{5}.lhs, C_{2}.b), continuous(C_{4}.x), nonnegative(C_{4}.x), linear(C_{5}.lhs, C_{4}.x), linear(C_{6}.z, C_{4}.x)]$ 

MD-list:  $[C_{6}.z = C_{3}.c \times C_{4}.x, C_{5}.lhs = C_{1}.a \times C_{4}.x]$ 

SQ-list:  $[Optimize C_{6}.z$ 

s.t.  $C_{5}.lhs \leq C_{2}.b$ $C_{4}.x \geq 0$ 

with [simplex]]

IP Type

 $[C_{1}.a, C_{2}.b, C_{3}.c, C_{4}.x_{1}, C_{5}.x_{2}, C_{6}.lhs, C_{7}.z]$ $[deterministic(C_{1}.a), constant(C_{1}.a), deterministic(C_{2}.b), constant(C_{2}.b), deterministic(C_{3}.c), constant(C_{3}.c), le(C_{6}.lhs, C_{2}.b), continuous(C_{4}.x_{1}), nonnegative(C_{4}.x_{1}), discrete(C_{5}, x_{2}), nonnegative(C_{5}.x_{2}), linear(C_{6}.lhs, C_{4}.x_{1}), linear(C_{7}.z, C_{4}.x_{1}), linear(C_{6}.lhs, C_{5}.x_{2}), linear(C_{7}.z, C_{5}.x_{2})]$ $[C_{7}.z = C_{3}.c \times (C_{4}.x_{1} + C_{5}.x_{2}), C_{6}.lhs = C_{1}.a \times (C_{4}.x_{1} + C_{5}.x_{2})]$ $[Optimize C_{7}.z$ 

s.t.  $C_{6}.lhs \leq C_{2}.b$ $C_{4}.x_{1} \geq 0$ $C_{5}.x_{2} \geq 0$ 

with [simplex-with-rounding, branch-and-bound, cutting-planes]]
</div>

Fig. 3. Optimization model types.

The metric list (MD-list) defines the mathematical relationships among the attributes in the EA-list. The standard queries (SQ-list) specify the computational procedures derived from the mathematical structure. A procedure may be simple arithmetic or be defined as a specialized solver. Explicit specification of standard queries allows us to control different computational procedures efficiently. The MD-list and SQ-list should satisfy the assumptions in SA-list. The detailed data for the attributes specified in EA-list but not defined in MD-list nor SQ-list should be supplied by the modeler as the input to the model-type. Table 2 shows the model type syntax.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Id: M/M/1 Queueing Model Type
EA-list: [OBJECT = {:waiting-time, time-in-system},
EVENT = (OBJECT, INTERVAL) {:rate},
PROCESS= (PROCESSOR, OBJECT) {:duration},
QUEUE = Some(OBJECT) {:#-of-objects},
SYSTEM = (PROCESS, QUEUE) {:#-of-objects},
EVENTS = All(EVENT) {:mean-rate},
PROCESSES = All(PROCESS) {:mean-time},
QUEUES = All(QUEUE) {:avg-#-of-objects},
SYSTEMS = All(SYSTEM) {:avg-#-of-objects},
OBJECTS = All(OBJECT)
:{avg-time-in-queue, avg-time-in-system}]
SA-list: [poisson(EVENT.rate, EVENTS.mean-rate),
exponential(PROCESS.duration, PROCESSES.mean-time),
lt(EVENTS.mean-rate/PROCESSES.mean-time, 1),
eq(|PROCESSOR|, 1),
infinite(INTERVAL),
infinite(OBJECT)]
MD-list: []
SQ-list: [SYSTEMS.avg-#-of-objects =
EVENTS.mean-rate
PROCESSES.mean-time-EVENTS.mean-rate
OBJECTS.avg-time-in-system =
1
PROCESSES.mean-time-EVENTS.mean-rate
OBJECTS.avg-time-in-queue =
EVENTS.mean-rate
PROCESSES.mean-time(PROCESSES.mean-time-EVENTS.mean-rate)
QUEUES.avg-#-of-objects =
(EVENTS.mean-rate)$^{2}$
PROCESSES.mean-time(PROCESSES.mean-time-EVENTS.mean-rate)]
</div>

Fig. 4. M/M/1 Queueing model type.

Fig. 3 shows examples of two optimization model types. The optimization model types are domain independent because the existential assumptions use class and attribute variables. The structural assumptions of the LP type define a deterministic linear structure with continuous variables, and those of the IP type define a deterministic linear structure with both continuous and discrete variables. The metric definitions are the algebraic expressions detailing the linearity assumptions. The standard query shows that we can compute the value of $C_{4}.x$ optimizing the value of $C_{6}.z$ subject to the constraints within a continuous linear vector space using the solver simplex.

In fig. 4, the structural assumptions of the M/M/1 queueing model type define a stochastic process with a poisson-distributed rate of arrival events and an exponential processing time of one processor. The model type is domain dependent

Table 3
Model template syntax.

```txt
model-template :=
<model-template-id, domain-world-id, model-type-id, UC-list>
UC ``unification constraint`' := 
    class-id.attr ⇒ class-id.attr `specialization`' |
    class-var.attr-var ← class-id.attr `instantiation`'
```

because the existential assumptions use class definitions. The standard query list defines how we can compute the values characterizing the queueing system such as the average time in the system and the average length of the queue. The power-set construction Some(OBJECT) shows that QUEUE is composed of a set of arrival objects, and the aggregation. All(EVENT) shows that EVENTS is composed of all arrival events. The aggregation and powerset construction allow us to compute properties of sets rather than individuals. In fig. 4, we omitted units and ranges to make the exposition simple, but we expect that most attributes will be defined with a unit and range more specific than :in nilunit; e.g. duration: $R^{+}$ in time for the class PROCESS.

![](/api/attachments/F9ZJNV3W/fulltext/images/a1bcbeb1c3a7637cfc6ba823b7fe12f09e383601ee592e90ffeb464bbb179a05.jpg)  
Fig. 5. Unification of a domain world with a model type.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Id: Product Mix Template
DW: Product-Mix Planning
MT: LP Type
UCL:  $[C_{3}.c \Leftarrow PRODUCT.unit-price, C_{4}.x \Leftarrow PRODUCT.prod-level, C_{2}.b \Leftarrow RESOURCE.availability, C_{5}.lhs \Leftarrow RESOURCE.usage, C_{1}.a \Leftarrow USE.unit-usage, C_{6}.z \Leftarrow PRODUCTION.revenue]$
</div>

Fig. 6. Product mix model template.

## 3.3. Model templates

A model template (model-template) combines the domain knowledge in a domain-world and the mathematical knowledge in a model-type. Therefore, a model template shows the classes of objects existing in the application domain and the structural assumptions required to utilize the mathematical system to solve a nonempty set of domain problems. The domain-world and the model-type are combined into the model template through a unification constraint list (UC-list). The UC-list details how the class and attribute variables of a domain independent model type are instantiated or how the classes and attributes in a domain dependent model type are specialized in order to combine the two different kinds of knowledge. The unification imposes the structural assumptions in the model type on the domain world and instantiates the metrics definitions and standard queries into domain terms. Table 3 shows the model template syntax.

Fig. 5 shows the unification of a domain world and a model type diagrammatically. In the figure, $\langle\mathbf{O},\mathbf{R}_{\mathrm{D}}\cup\mathbf{R}_{\mathrm{M}},\mathbf{F}_{\mathrm{M}}\rangle$ denotes the portion of a decision situation which will be reasoned mathematically. In the $\mathcal{L}_{\mathrm{U}}$ , $\mathbf{O}$ and $\mathbf{R}_{\mathrm{D}}$ are represented by the ind-id and ind-dep and organized by the class-id and class-dep. $\mathbf{R}_{\mathrm{M}}$ and $\mathbf{F}_{\mathrm{M}}$ are supposed to be represented and reasoned with $\mathbf{R}_{\mathrm{N}}$ and $\mathbf{F}_{\mathrm{N}}$ through the set $\mathbf{F}_{\mathrm{H}}$ of homomorphisms. The $\mathcal{L}_{\mathrm{U}}$ specifies $\mathbf{F}_{\mathrm{H}}$ with the attr-spec-list and attr-def-list in the domain-world. By unification, the existential assumptions (EA) are specified by domain classes and attributes (EA/DW), the structural assumptions are imposed upon the domain-world (SA/DW), and the metric definitions (MD), the structural queries (SQ) and the associated solvers are instantiated into domain terms (MD/DW, SQ/DW and Solver/DW). Note that we formulate the unified model within the general mathematical system ( $\langle\left(\mathbf{N}, \mathbf{R}_{\mathbf{N}}, \mathbf{F}_{\mathbf{N}}\right\rangle$ ), and that the application domain is a relational system ( $\langle\mathbf{O}, \mathbf{R}_{\mathbf{E}}, \mathbf{F}_{\mathbf{E}}\rangle$ ). As a result, it is possible to apply logical deduction, general mathematical computation and specialized algorithms to the unified model.

Fig. 7. Customer checkout system model template.  
```txt
Id: Customer Checkout System Model Template
DW: [CUSTOMER = {:waiting-time, time-for-checkout},
ARRIVAL = (CUSTOMER, INTERVAL) {:arrival-rate},
CHECKOUT = (CLERK, CUSTOMER) {:checkout-time},
QUEUE = Some(CUSTOMER) {:#-of-customers},
COUNTER = (CHECKOUT, QUEUE) {:#-of-customers},
ARRIVALS = All(ARRIVAL) {:mean-arrival-rate},
CHECKOUTS = All(CHECKOUT) {:mean-checkout-time},
QUEUES = All(QUEUE) {:avg-#-of-checkout},
STORE = All(COUNTER) {:avg-#-of-checkout},
CUSTOMERS = All(CUSTOMER) {:avg-time-in-queue,
avg-time-for-checkout}]
MT: M/M/1 Queuing Model Type
UCL: [OBJECT.waiting-time ⇒ CUSTOMER.waiting-time,
EVENT.rate ⇒ ARRIVAL.arrival-rate,
...
EVENTS.mean-rate ⇒ ARRIVALS.mean-arrival-rate,
PROCESSES.mean-time ⇒ CHECKOUTS.mean-checkout-time,
...
OBJECTS.avg-time-in-system ⇒
CUSTOMERS.avg-time-for-checkout]
```

In fig. 6, the domain-world “Product-Mix Planning” is combined with the LP model type into a model template “Product Mix Template”. Since the LP model type is domain independent, the class and attribute variables are instantiated into the classes and attributes defined in “Product-Mix Planning”. For example, $C_{4}.x$ is instantiated into PRODUCT.prod-level and $C_{5}.lhs$ into RESOURCE.usage. Units and ranges of attribute definitions of domain-world are preserved in the model template. Unification propagates the assumptions metric definitions, and standard queries of the LP model type to the model template and thus to the domain world. Therefore, PRODUCT.prod-level is assumed to be continuous and non-negative as $C_{4}.x$ is. In the propagation, the attribute ranges if specified should be consistent with the assumptions. It is not possible to unify an attribute definition whose range is (0..100 and Integer) with an attribute variable assumed to be continuous. The metrics and standard queries are restated in domain terms as follows.

RESOURCE.usage = USE.unit-usage ×
PRODUCT.prod-level.
PRODUCTION.revenue = PRODUCT.unitprice × PRODUCT.prod-level.

maximize PRODUCTION.revenue

s.t. RESOURCE.usage ≤ RESOURCE.

availability

PRODUCT.prod-level ≥ 0.

Finally, PRODUCT. prod-level maximizing PRODUCTION.revenue satisfying the constraints is computed by the solver simplex.

Fig. 7 shows another example of a model template. Since the M/M/1 model type is domain dependent, classes and attributes are specialized rather than instantiated. Of course, assumptions and standard queries of the M/M/1 model type are propagated to “Customer Checkout System” template, too. Therefore, for example, ARRIVAL.arrival-rate of customers is assumed to be poisson distributed, and STORE.avg#-of-checkouts is computed by dividing the result of the subtraction of ARRIVALS.mean-arrival-time from CHECKOUTS.mean-checkout-time by ARRIVALS.mean-arrival-time. The second-order description component of a model template can be called from a predefined domain world, or can be fully described in the template. “Product Mix” template is an example of the former, while “Customer Checkout System” template illustrates the latter. Modelers can choose either method at their convenience.

## 3.4. Model instances

A model instance (model-instance) is similar to an individual-world in that both provide detailed data. It can be viewed as an application of a model template to a specific decision problem or as a more flexible and compact way to organize data by utilizing databases and other models. Since environments of organizations change rapidly, the storage of an individual world definitions or a model instance is justified only in cases where it is very complicated or repeatedly required to define the instance. Each model instance is defined by the list of sources (metric-source-list). The syntax of model instances is defined in table 4.

```txt
Table 4
Model instance syntax.

model-template :=
  <model-instance-id, model-template-id, metric-source-list> |
  <model-instance-id, world-id, metric-source-list>
metric-source := metric source
source :=
  = user defined function | ← database name |
  ← external model name | : definition
```

<table><tr><td colspan="2">Id: Product Mix Model Instance</td></tr><tr><td>Source:</td><td>[PRODUCT.unit-price ←Production policy database, RESOURCE.availability = f(RESOURCE.unit-usage, RESOURCE.unit-cost, ir), RESOURCE.unit-usage ←Accounting database, RESOURCE.unit-cost ←Accounting database, ir: expected inflation rate]</td></tr></table>

Fig. 8. Product mix model instance.

As shown in table 4, a source can be a user defined function(=), a database name or expression(←), an external model(←), or a user definition(:). User defined functions are not constrained by the assumptions of the instance's model type since they are defined outside of the model. Similarly, no mathematical assumptions are made about the data supplied from databases, external models, or users definitions. The use of a database expression supports complex index requirements with Boolean expressions such as all parts except widgets. The metrics required to compute the standard queries should be defined in the model instance if they are not defined in the individual-world or model-template.

Consider the product mix model instance in fig. 8. Data for usage of raw material by products, RESOURCE.unit-usage, is already computed by some accounting procedure and stored into the accounting database. Arguments of a user defined function may not have been defined in the model template, e.g., RESOURCE.unit-cost in the function for the availability of raw material (RESOURCE.availability). If this is the case, the arguments should be defined in the model instance until the function can take a definite value. The argument ir is defined as the expected inflation rate, but it is also legitimate to provide a specific value such as 5% per year.

```typescript
Id: Customer Checkout System Instance,
Source: [ARRIVAL.arrival-rate ←Sales forecasting model,
CHECKOUTS.mean-checkout-time ←Customer service database]
```  
Fig. 9. Customer checkout system model instance.

Fig. 9 shows the instance of the customer checkout system template defined in fig. 7. Note that only two metrics (ARRIVAL.arrival-rate and CHECKOUTS.mean-checkout-time) are defined in this instance. Other metrics are not required for the model solution.

## 3.5. Formal semantics of $\mathcal{L}_U$

The formal semantics of $L_{U}$ is defined model theoretically. As model theory investigates the relationship between a formal language and its interpretations (which is called models in logic), our semantic definitions specify the relationship of the language elements to the modeling elements. That is, the meanings of the expressions of $L_{U}$ are defined to denote the elements of the modeling world conceptualized in section 2.2. The semantics is truth conditional in that some of the syntactic elements are chosen to say things about the modeling world. In particular, the semantics of models is defined to specify the truth conditions in domain worlds and mathematical systems, and the conditions for the meaningful combination of the domain and mathematical knowledge.

Formally, the semantics of $\mathcal{L}_{\mathrm{U}}$ is defined by the denotation function '[]':

$$
\begin{array}{r l}\llbracket   \rrbracket : E x p r \rightarrow \big (\mathbf {O} \cup \mathbf {N} \cup \mathbf {R} _ {\mathrm{E}} \cup \mathbf {R} _ {\mathrm{N}} \cup \mathbf {F} _ {\mathrm{E}} \cup \mathbf {F} _ {\mathrm{N}} \cup \mathbf {F} _ {\mathrm{H}}\\&\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \cup \mathbf {A} \cup \{\mathbf {T}, \mathbf {F} \} \big),\end{array}
$$

where Expr is the set of legal expressions in the language. The denotation function is defined by a set of equations, one per syntactic category of the language. The semantic equations use set notation, predicate calculus and meta-functions defined over syntactic elements. Evaluation of the equations provides the formal meanings of syntactic elements.

To illustrate, consider the following semantic equations for syntactic elements of individual domain worlds:

$$
[ [ \text { ind - id } ] ] = \mathbf {0} \in \mathbf {0},
$$

$$
\begin{array}{r l} \llbracket \text {ind - dep} \rrbracket = & \exists \mathbf {r} _ {\mathrm{D}} \in \mathbf {R} _ {\mathrm{D}} \exists \mathbf {o} \in \mathbf {O} \\ & \mathbf {r} _ {\mathrm{D}} \big (\mathbf {o}, \llbracket \delta_ {p} (\text {ind - dep}, 1) \rrbracket , \dots , \\ & \llbracket \delta_ {p} (\text {ind - dep}, \delta_ {l} (\text {ind - dep})) \rrbracket \big), \end{array}
$$

$$
\begin{array}{r l} & {\llbracket \langle \mathrm{ind-id}, \mathrm{ind-dep} \rangle \rrbracket} \\ & {\quad = \exists \mathbf {r} _ {\mathrm{D}} \in \mathbf {R} _ {\mathrm{D}}} \\ & {\qquad \mathbf {r} _ {\mathrm{D}} \big (\llbracket \mathrm{ind-id} \rrbracket ,} \\ & {\qquad \llbracket \delta_ {p} (\mathrm{ind-dep}, 1) \rrbracket , \dots ,} \\ & {\qquad \llbracket \delta_ {p} (\mathrm{ind-dep}, \delta_ {l} (\mathrm{ind-dep})) \rrbracket \big)} \end{array}
$$

The first equation defines that an individual identifier (ind-id) denotes an object in the domain world. The others rely on meta-functions and predicate calculus. In the definitions, meta-functions $\delta_{l}$ and $\delta_{p}$ are defined over dependencies. The former computes the length of a dependency and the latter projects an element (an identifier) from a dependency. The second equation defines the meaning of an individual dependency: An individual dependency specifies a sequence of objects such that the sequence together with another object is an instance of a dependency relation. The existentially quantified object in the second equation becomes instantiated by combining a dependency with an individual identifier as shown in the third equation. The existentially quantified relation will be instantiated when the individual world specification is combined with a class world specification.

The semantics of domain-world is rather descriptive since it asserts the known facts about the decision situations. On the other hand, we emphasize the prescriptive meanings of model-type since it is obligatory to satisfy the structural assumptions for the application of model types to decision problems. The semantics of model-template is defined to combine the description and the prescription into one specification. Details of the semantic equations are outside the scope of this paper. Interested readers are referred to [20].

## 4. Organization of domain and mathematical knowledge

In this section, we extend the $L_{U}$ with inheritance to support incremental definition and reuse of models. We discuss alternative forms of inheritance and present definitions of inheritance based on partial order relations for domain worlds and model types.

## 4.1. Motivation and design alternatives

Inheritance has been widely studied as a knowledge organization technique in artificial intelligence, database management, and software engineering. There is a general consensus that inheritance is a form of sharing of data and/or code. The most apparent benefit of inheritance is abbreviation as inherited definitions need not be repeated. Beyond sharing, there is much diversity about the precise meanings and uses of inheritance. Many inheritance relations have been defined including subclass, subtype, like, and inherits\_from with different uses. Some emphasize flexibility in reasoning about exceptions and dynamic binding of code, while others emphasize software correctness in type checking, subsumption testing, and change propagation.

Wegner [35] defines four kinds of inheritance to support various levels of flexibility and correctness. The strongest form of inheritance is behavioral compatibility where a subclass produces results that are identical to results from its parent classes or different in well-defined ways. Behavioral compatibility is an algebraic view of inheritance where subclasses are compatible with the axioms of their parent classes. A slightly weaker form of inheritance is interface compatibility where a subclass can be substituted for any of its parent classes but the result may be different. Interface compatibility ensures that expressions compute meaningful values (i.e., type and unit safe). In addition, interface compatibility can be checked at compile-time. A more flexible but weaker form is name compatibility where a subclass must preserve the names used in its parent classes. A benefit of this approach is dynamic binding of code to procedure names at execution time. The weakest but most flexible form of inheritance is cancellation where unrestricted modification to subclasses is permitted. Cancellation inheritance supports modeling of natural objects with no well-defined class boundaries.

We utilize inheritance for domain worlds and model types. For domain worlds, we use interface and name compatibility to reason about substitution of classes and attributes. For model types, we use behavioral compatibility to reason about the similarity of the assumptions among model types. Partial orders ( $\sqsubseteq$ ) over attributes, classes and assumptions are defined as the basis of inheritance, and are extended to domain worlds and model types. The following sections provide detailed definitions of partial order relations that support our views of inheritance for domain worlds and model types.

## 4.2. Organization of domain knowledge

In object-oriented languages, classes are represented by labeled records. A labeled record is a set of labeled values, and the type of the record is specified by the set of label and type (value range) pairs [11]. The subtype relation between labeled record types is based on identical labels and restricted types as shown.

$$
\begin{array}{l} \left\{a _ {1}: t _ {1}, \ldots , a _ {n}: t _ {n},   a _ {n + 1}: t _ {n + 1}, \ldots , a _ {n + m}: t _ {n + m} \right\} \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qend{array}
$$

The definition established interface compatibility, and thus permits a labeled record to be substituted by a subtype record in any expression.

Classes in the $L_{U}$ extend labeled records by decomposing labels into class dependencies and attributes, a form better suited for mathematical modeling. Thus, the subtype relation for classes uses both dependencies and attributes. In addition, attribute names can be redefined in subclasses.

$$
c _ {i} = c d p _ {i}: \left\{a _ {1} ^ {\prime}: t _ {1}, \dots , a _ {n} ^ {\prime}: t _ {n}, \right.
$$

$$
\left. a _ {n + 1}: t _ {n + 1}, \ldots , a _ {n + m}: t _ {n + m} \right\},
$$

$$
\begin{array}{l} c _ {j} = c d p _ {j}: \big \{a _ {1}: w _ {1}, \ldots , a _ {n}: w _ {n} \big \}, \\ c _ {i} \sqsubseteq c _ {j} \Leftrightarrow \\ \forall i \leq n (t _ {i} \sqsubseteq w _ {i}) \wedge \\ \forall k \leq \delta_ {l} (c d p _ {j}) \exists l \leq \delta_ {l} (c d p _ {j}) \big (\delta_ {p} (c d p _ {i}, k) \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \end{array}
$$

Each $a_{i}^{\prime}$ is either identical to $a_{i}$ or explicitly redefined. The function $\delta_{l}$ computes the length of the argument class dependency, and $\delta_{p}$ projects the class in the position specified by the second argument from the class dependency specified by the first argument. The recursive relation is well defined since primitive classes are simply collections of attributes.

The subclass relation between primitive classes is the same as the subtype relation between labeled records except for attributes. In the $\mathcal{L}_{\mathrm{U}}$ , attribute types are specified by value range and unit of measurement. For example, the attribute RESOURCE. usage has the type $\langle 0..500, lbs\rangle$ . Consider two attributes with their types $t_i \equiv \langle r_i, u_i \rangle$ and $t_j \equiv \langle r_j, u_j \rangle$ . The subtype relation between attribute types is determined by unit compatibility and range inclusion. If $u_i$ and $u_j$ are identical, $t_i$ is a subtype of $t_j$ iff $r_i$ is a subrange of $r_j$ . If $u_i$ and $u_j$ are not identical, but compatible, then $t_i$ is a subtype of $t_j$ iff $r_i'$ is included in $r_j$ , where $r_i'$ is the range of $t_i$ when the associated unit is converted to $u_i$ . For example, attribute type $\langle 100..500, gm\rangle$ is a subtype of $\langle 0..4, kg\rangle$ since units $gm$ and $kg$ are compatible and the range of the latter includes the converted range of the former.

The extended subtype definition provides for substitutability in expressions and equations. For example, consider the following definitions:

PRODUCT = ∅:{unit-price, prod-level},

RESOURCE = ∅:{availability, usage},

USE = (RESOURCE, PRODUCT): {unit-usage}.

$$
\begin{array}{r l} \text { RESOURCE.usage } & = \text { USE.unit - usage } \\ & \times \text { PRODUCT.prod - level }. \end{array}
$$

Since class USE depends on primitive classes RESOURCE and PRODUCT, the above formula is equivalent to the following:

$$
\begin{array}{r l} & \text { RESOURCE.usage } \\ & = (\text { RESOURCE,   PRODUCT }). \text { unit - usage } \\ & \times \text { PRODUCT.prod - level }. \end{array}
$$

Now, by factoring out class RESOURCE from both sides, the system can infer the following relationship:

$$
\text { usage } _ {i} = \sum_ {j \in \text { PRODUCT }} \text { unit - usage } _ {i j} \cdot \text { prod - level } _ {j},
$$

for all $i$ in RESOURCE.

Substitutions in the above equation are governed by the class subtype definition. For example, any class that includes the dependencies and attributes of USE can be substituted. If a subclass has additional dependencies, additional indices are generated. Similarly, if a subclass has additional attributes or renames attributes, those attributes may appear in the equation.

## 4.3. Taxonomy of model types

The subtype rule for model types is based on a form of behavioral compatibility. True behavioral compatibility requires that the axioms of a sub model type imply the axioms of parent model types, and ensures that sub model types compute the same result as their parent model types when given the same input values. True behavioral compatibility facilitates the development of more efficient solvers to take advantage of special problem structures. For example, network models are linear programs with a special problem structure and more efficient solvers. However, true behavioral compatibility is too strong for classifying model types because specialization occurs by restricting outputs as well as by limiting inputs and problem structure. For example, an integer program is a linear program except that part of the output must be integers rather than real numbers. In general, the result of an integer program will be different than a corresponding linear program when given the same input. Thus, our definition of behavioral compatibility emphasizes inclusion of structural assumptions for specialization by input and problem structure restrictions and partitioning of existential assumptions for specialization by output restrictions.

For structural assumptions, we use the relaxation relation for individual assumptions and extend this definition to inclusion of sets of assumptions. An assumption predicate is non-primitive if it can be decomposed into simpler ones. For instance, the efficient market assumption, a pillar of most financial models, is a conjunction of assumptions of human rationality, instantaneous information transfer, and a few others. Furthermore, human rationality can be decomposed into more basic assumptions according to the purpose of the exposition and the knowledge level of the audience. Primitive assumptions are at the end of this chain, which means that they can be explained only by linguistic semantics, not by other assumptions. The choice of primitive assumptions partially depends on the level of mathematical knowledge of users of the model management system. If the model management system provides tutoring functions to naive users, for example, a fine level of detail is required for assumptions.

We define the function $\rho$ that converts an assumption predicate into a set of primitive ones.

$$
\rho : P _ {n p} \rightarrow 2 ^ {P _ {p}},
$$

where $P_{np}$ is the set of all assumption predicates, and $P_{p}$ is the set of all primitive assumption predicates. As an example, $\rho(\text{linear})$ may return the set $\{\text{proportional}, \text{additive}\}$ with the most common interpretation of the predicates.

The function $\rho$ induces a partial order ( $\sqsubseteq$ ) relation on assumption predicates. The relation $p_i \sqsubseteq p_j$ holds iff $\rho(p_i) \subseteq \rho(p_j)$ . Another way to think about the partial order is as a relaxation relation. The set $P_{np}$ can be represented as a directed, acyclic graph where nodes are assumption predicates denoting the interesting combinations of primitive predicates, and arcs are the elements of the set inclusion relation. We interpret each arc as a one step relaxation of an assumption predicate. For example, both proportional and additive are one step relaxations of the predicate linear. Some primitive predicates are enforced to be in one step relaxation relation by definition. For example, both continuous and discrete may be primitive predicates, but the former is generally considered relaxing the latter predicate.

Based on taxonomies of assumption predicates, classes and attributes, we define the relaxation relation for structural assumptions. Let $P \equiv p(t_{1}, \ldots, t_{n})$ and $Q \equiv q(u_{1}, \ldots, u_{n})$ be assumptions with n-place predicates of p and q and arguments of $t_{i}$ 's and $u_{i}$ 's. Q is a relaxation of P if p is a relaxation of q and every non-numeric argument of p is a specialization of the corresponding argument of q.

$$
P \sqsubseteq Q \Leftrightarrow (p \sqsubseteq q) \wedge \forall i \leq n ((t _ {i} \notin N) \rightarrow (t _ {i} \sqsubseteq u _ {i})).
$$

For example, additive(RESOURCE.usage, PRODUCT.product-level) is a relaxation of linear(RM.usage, PRODUCT.product-level), since linear ⊆ additive and RM.usage ⊆ RESOURCE. usage. The relaxation relation is extended to sets of assumptions. Let $SA_{1}$ and $SA_{2}$ be two sets of structural assumptions. $SA_{1}$ is a relaxation of $SA_{2}$ iff every assumption in $SA_{2}$ is a relaxation of an assumption in $SA_{1}$ .

$$
S A _ {1} \sqsubseteq S A _ {2} \Leftrightarrow \forall P _ {j} \in S A _ {2} \exists P _ {i} \in S A _ {1} (P _ {i} \sqsubseteq P _ {j}).
$$

The partial order relation between two sets of existential assumptions is based on partitioning one set into the other. This permits specialization by restricting the output. More precisely, $EAL_{i} \sqsubseteq EAL_{j}$ iff there exists a bijective mapping $m: EAL_{j} \to 2^{EAL_{i}}$ such that:

(1) if $m(cid_j) = X$ , then $cid_i \sqsubseteq cid_j$ for all $cid_i \in X$ ;

(2) for all two different $cid_{i}$ and $cid_{j}$ in $EAL_{j}$ , $m*\left(cid_{i}\right)\cap m\left(cid_{j}\right)=\emptyset$ (disjoint); and

$$
\cup_ {c i d _ {j} \in E A L _ {i}} \mathrm{m} (\mathrm{cid} _ {j}) = E A L _ {i} (\text { complete }).
$$

Note that the first condition above does not apply to domain independent model types where the structural assumptions contain only class and attribute variables, not class definitions.

The subtype relation for model types is based on partial orders of existential and structural assumptions. Consider two model type definitions $\langle MT_{1}, EAL_{1}, SAL_{1}, SQL_{1} \rangle$ and $\langle MT_{2}, EAL_{2}, SAL_{2}, SQL_{2} \rangle$ . $MT_{1}$ is a subtype of $MT_{2}$ iff $EAL_{1}$ partitions $EAL_{2}$ and $SAL_{2}$ is a relaxation of $SAL_{1}$ .

$$
M T _ {1} \subseteq M T _ {2} \Leftrightarrow (E A L _ {1} \subseteq E A L _ {2}) \vee (S A L _ {1} \subseteq S A L _ {2}).
$$

As an example, consider the LP and IP model types in fig. 3 (section 3.2). All existential assumptions in both model types are composed of class and attribute variables (both model types are domain independent). By instantiating $C_{4}.x$ of the LP Type into $C_{4}.x_{1}$ and $C_{4}.x_{2}$ of the IP Type, the existential assumptions LP are partitioned into those of IP and hence in the $(\sqsubseteq)$ relation. The structural assumption sets of the two model types are also in relaxation relation because continuous is defined as a relaxation of discrete. Based on the definition of subtype relation we conclude that the IP model type is a subtype of the LP model type. Therefore, IP model type computes the values of decision variables within a linear vector space as LP type does, but limits some of them of integer values as defined by the discrete assumption.

## 5. Related work

Measurement theory [33] and logic modeling [23] provide the foundation of our work. Foremost, we have attempted to design a knowledge representation that reflects a major concern in measurement theory: Mapping from empirical worlds composed of objects and relations into mathematical systems. We strongly believe that model management systems should explicitly represent this mapping to the extent possible. Our most unique contribution is a knowledge representation with a semantics based on measurement theory and features to support an explicit mapping from the real world to mathematical models.

Logic modeling is another major influence because of the importance of a declarative representation and powerful inference procedure. There is a growing body of model management work based on logic modeling. Most notably, Bhargava et al. [1,2,3,4] describe a logic framework for model representation in the TEFA system. They pioneered the embedded language approach as a way to achieve economy of representation and support multiple target modeling languages. Our work takes a different approach to higher order representation. We represent individual and class order worlds in our domain component and provide a realized mapping in model templates and instances. We have not addressed the issue of multiple target languages.

Besides these fundamental influences, the model management literature has contributed important work on complex models, inheritance and frame representations, and model construction. The work on complex models emphasizes input and output dependencies among models and efficient reasoning procedures to select a model or a path of models to compute a desired output. Dutta and Basu [14] describe an inference procedure that finds a path of models that produces a requested output and verifies the preconditions of the models. Liang [25,26] proposes an AND/OR graph to represent complex models and a graph based inferencing procedure. Muhanna and Pick [32] also permit choice in model versions and enforce compatibility on the data types and units of the interfaces of related models. Our representation of complex models builds on the schemes in these works so that we can adapt one of these well-defined inferencing procedures.

Another important area of model management is the use of frames and inheritance. Borgida et al. [6] stressed the use of inheritance for information system design. Sowa [34] distinguished between types and schemata to represent the obligatory properties of concepts and background knowledge which are similar to model types and templates. Wegner [35] discussed the meanings of inheritance in programming languages. We have adopted two guidelines from [35]: Behavioral compatibility for model types and interface compatibility for domain worlds.

For model management, Dolk and Konsynski [13] first proposed frames and inheritance and demonstrated the representation of linear and integer programming. We extend their use of inheritance to classes, attributes, and assumptions. Liang [27] proposed levels of instantiation similar to ours, but he does not describe inheritance and representation of assumptions. Inheritance has been exploited for dimensional analysis in [8,9,17] and [3]. We augment their use of inheritance with partial order relations for attributes, classes, assumptions, and model types.

Model formulation tools such as proposed by Jarke and Binbasiglou [5], Krishnan [24], Ma et al. [28], and Dhar and Croker [12] address formulation in one paradigm. These approaches have a fine level of knowledge about one paradigm and provide translation into executable modeling languages such as structured modeling [18]. Since our focus is not on model execution, we have not attempted to deal with these issues.

This paper extends our earlier work [29,22]. The earlier work introduced the basic idea of inheritance and instantiation, but the current paper provides a semantic foundation and extends the representation of domain knowledge, mathematical knowledge and their combinations. A complementary version of this work including a detailed description of search and explanation operators is described in [29].

## 6. Summary and directions

We defined a declarative modeling language, $L_{U}$ with both practical and theoretical implications for integrated modeling environments. On the practical side, the $L_{U}$ supports the design goals of uniformity, modeling independence, meaningful combination, and incremental refinement. Domain, mathematical, and modeling knowledge are expressed in one uniform notation. The $L_{U}$ distinguishes between domains represented as worlds composed of objects and relations and mathematical knowledge represented as model types composed of assumptions and standard queries. Unification constraints in model templates define common patterns of domain and mathematical knowledge. Inheritance supports incremental refinement through partial order relations for attributes, classes, assumptions, model types, and domain worlds. On the theoretical side, the notion of homomorphic mappings from measurement theory strongly influenced the design of $L_{U}$ . In particular, the semantic domain, the separation of domain and mathematical worlds, unification constraints, and support for quantitative and qualitative reasoning were motivated by homomorphisms.

An important direction is to develop certain kinds of automated reasoning using this knowledge representation. Our current work has focused on browsing, explanation, and inexact search to support model identification $[15,16]$ . Browsing permits a modeler to navigate among a network of related models. Inexact search locates models that most closely match requirements, thus providing a convenient starting point for browsing. Explanation enhances a modeler's understanding about the symbols, assumptions, components, and relationships among models. Further details on browsing, inexact search, and explanation operators for model types can be found in $[29]$ and $[21]$ . We want to extend our current work with automated reasoning based on type inference $[11]$ and classification $[7]$ in object-oriented systems. Type inference, extended to metrics, units of measure, time, and indices, ensures a notion of consistency and provides a form of automatic documentation. A classifier detects partial order relations among models and their components. This can have the obvious benefit of detecting inconsistencies and the more subtle benefit of discovering relationships. Together, the type inferencing and classification will be important tools to support model formulation.

Another interesting direction for our work is the dynamic aspects of modeling. Most work in model management has emphasized the static aspects of modeling but largely ignored the dynamic aspects. Consequently, decision makers and modelers lack support for proper documentation of model evolutions and change management. We aim to extend our knowledge representation so that model changes as well as their causality and evolution can be explicitly represented. To enhance the performance of modelers, we will develop operators for propagation of changes both within and between models, and generation of models from the specification of possibly non-existing, incomplete, and multiple versions of decision problems.

## Acknowledgements

We thank Ron Lee, Ramaya Krishnan, and Arthur Geoffrion for helpful comments and discussions of ideas.

## References

[1] H.K. Bhargava, M. Bieber and S.O. Kimbrough, Oona, Max and the WYWWYWI Principle: Generalized Hypertext and Model Management in a Symbolic Programming Environment, in: Proceedings of the Ninth International Conference on Information System (1988) 179–191.

[2] H.K. Bhargava and R. Krishnan, A Formal Approach in a Model Management System, in: Proceedings of the 23rd Hawaii International Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, HI, January, 1989.

[3] H.K. Bhargava and S.O. Kimbrough, On Embedded Languages for Model Management, in: Proceedings of the 23rd Hawaii International Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, HI, January, 1990.

[4] H.K. Bhargava, S.O. Kimbrough and R. Krishnan, Unique Names Violations, a Problem for Model Integration or You Say Tomato, I Say Tomato, ORSA Journal on Computing 3, 2 (1991) 107–120.

[5] M. Binbasioglu and M. Jarke, Domain-Specific DSS Tools for Knowledge-Based Model Building, Decision Support Systems 2, 3 (1986) 213–223.

[6] A. Borgida, J. Mylopoulos and H. Wong, Generalization/Specialization as a Basis for Software Specification, in: Brodie, Mylopoulos, and Schmidt, Eds., On Conceptual Modeling (Springer-Verlag, 1984) 434–443.

[7] R. Brachman and H. Levesque, The Tractability of Subsumption in Frame-Based Description Languages, in Proc. AAAI-84 (1984) 34–37.

[8] G. Bradley and R. Clemence, Model Integration with a Typed Executable Modeling Language, in: Proceedings of the 21st Hawaii International Conf. on System Sciences, Kailu-Kona, HI, January 1988, 403–410.

[9] G. Bradley and R. Clemence, A Type Calculus for Executable Modelling Languages, IMA Journal of Mathematics in Management 3, 1 (1988) 277–291.

[10] L. Cardelli, A Semantics of Multiple Inheritance, in: Semantics of Data Types, Lecture Notes in Computer Science 173 (Springer-Verlag, 1984) 51–67.

[11] L. Cardelli and P. Wegner, On Understanding Types, Data Abstraction, and Polymorphism, ACM Computing Surveys 17, 4 (December 1985) 471–522.

[12] V. Dahr and A. Croker, Knowledge-Based Decision Support in Business: Issues and a Solution, IEEE Expert 3, 1 (Spring 1988) 53–62.

[13] D. Dolk and B. Konsynski, Knowledge Representation for Model Management Systems, IEEE Transactions on Software Engineering SE-10, 6 (June 1984) 619–628.

[14] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, 9 (September 1984) 89–97.

[15] S. Gass, Decision-Aiding Models: Validation, Assessment, and Related Issues for Policy Analysis, Operations Research 31, 4 (July–August 1983) 603–631.

[16] S. Gass, Managing the Modeling Process: A Personal Reflection, European Journal of Operational Research 31, 1 (July 1987) 1–8.

[17] N. Gehani, Databases and Units of Measure, IEEE Transaction on Software Engineering SE-8, 6 (November 1982) 605–610.

[18] A. Geoffrion, Introduction to Structured Modeling, Management Science 33, 5 (May 1987) 547–588.

[19] A. Geoffrion, Computer-Based Modeling Environments, European Journal of Operational Research (1984).

[20] S. Hong, A Formal, Unified Modeling Framework: Knowledge Representation and Automated Reasoning, Ph.D. Dissertation, The University of Texas at Austin, Austin, TX, August 1991.

[21] S. Hong and M. Mannino, Taxonomies, Assumptions, and Complex Objects in Prolog: Applications to the Model Library System, Technical Report CBDA 152, Center for Business Decision Analysis, The University of Texas at Austin, Austin, TX, 1988.

[22] S. Hong, M. Mannino and B. Greenberg, Inheritance and Instantiation in Model Management, in: Proceedings of the 23rd Hawaii International Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, HI, January 1990.

[23] S.O. Kimbrough and R.M. Lee, Logic Modeling: A Tool for Management Science, Decision Support Systems 4, 1 (April 1988) 3–16.

[24] R. Krishnan, Knowledge Based Aids for Model Construction, Ph.D. Dissertation, The University of Texas at Austin, Austin, TX, November 1987.

[25] T. Liang, A Graph-Based Approach to Model Management, in: Proceedings of the Seventh International Conference on Information Systems, San Diego, CA, December 1986, 136–151.

[26] T. Liang, Reasoning in Model Management Systems, in: Proceedings of the 21st Hawaii International Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, HI, January 1988, 461–468.

[27] T. Liang, Modeling by Analogy: An Approach to Enhancing Model Management Systems, Working Paper No. 89-1524, College of Commerce and Business Administration, University of Illinois at Urbana-Champaign, Urbana, IL, January 1989.

[28] P. Ma, F. Murphy and E. Stohr, Representing Knowledge about Linear Programming Formulation, (April 1988), working paper, submitted for publication.

[29] M. Mannino, B. Greenberg and S. Hong, Knowledge Representation for Model Libraries, in: Proceedings of

the 21st Hawaii International Conference on System Science, Decision Support and Knowledge Based Systems Track, Kona-Kailu, HI, January 1988, 349–355.

[30] M. Mannino, B. Greenberg and S. Hong, Model Libraries: Knowledge Representation and Reasoning, ORSA Journal on Computing 2, 3 (Summer 1990) 287–301.

[31] A. Meeraus, An Algebraic Approach to Modeling, Journal of Economic Dynamics and Control 5 (1983) 81–108.

[32] W. Muhanna and R. Pick, Composite Models in Symms, in: Proceedings of the 21st Hawaii International Conference on System Science, Decision Support and Knowledge Based Systems Track, Kona-Kailu, HI, January 1988, 418–427.

[33] R.S. Roberts, Measurement Theory (Addison-Wesley Publishing Company, Reading, MA, 1979).

[34] J.F. Sowa, Conceptual Structures: Information Processing in Mind and Machine, Chapters 3 and 4 (Addison-Wesley Publishing Company, Reading, MA, 1984).

[35] P. Wegner, Concepts and Paradigms of Object-Oriented Programming, OOPS Messenger 1, 1 (August 1990) ACM, 7–87.
