---
otero_id: 17416
otero_key: "VQZFR3ZD"
title: "Formal semantics of the unified modeling language"
authors: "Sa Neung Hong; Michael V. Mannino"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)e0046-g"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Formal semantics of the unified modeling language $\mathcal{L}_U$

Sa Neung Hong $^{a}$ , Michael V. Mannino $^{b}$

$^{a}$ Department of Management Science & Information Systems, The University of Texas at Austin, Austin, TX 78712, USA $^{b}$ Department of Management Science, DJ10, University of Washington, Seattle, WA 98195, USA

## Abstract

A formal semantics is an essential element of language design because it supports comparison of language designs, provides implementation guidelines, and enables properties about a language to be proved. However, in the field of model management, there has been a lack of attention to the formal semantics of modeling languages. In this paper, the philosophy and formal semantics of the Unified Modeling Language $(\mathcal{L}_{U})$ are presented. The $L_{U}$ supports integrated modeling environments with a large number of models from diverse domains and management science paradigms. We discuss the philosophy of the $L_{U}$ in which logical deduction about empirical worlds is combined with efficient computations about mathematical worlds. We argue that measurement theory stressing homomorphic mappings from empirical to mathematical worlds is an ideal foundation for integrated modeling environments. A denotational semantics is given for the $L_{U}$ including the semantic domain, meta functions, and semantic equations. The $L_{U}$ is unique because measurement theory plays a salient role in its underlying denotational semantics. In particular, the semantic domain of the $L_{U}$ includes explicit homomorphic mappings from empirical to mathematical worlds and semantic equations define conditions, based on homomorphisms, that must be satisfied by valid models.

Keywords: Modeling language; Measurement theory; Formal semantics; Homomorphism; Knowledge representation; Model management

## 1. Introduction

Model management is widely recognized as a key component of decision support systems because of the importance of modeling in problem solving and decision making. The primary role of model management is the convenient and efficient update, retrieval, and execution of models. Frequently, model management systems have emphasized these functions in relation to specific modeling languages, management science paradigms, and application domains. As management science techniques have become more widely accepted in organizations, there is a need to integrate the tools and models used in decision support systems. Model integration emphasizes large model bases containing complex models based on diverse management science paradigms and application domains. Model integration involves knowledge intensive tasks such as model formulation, model reuse, model analysis, and output interpretation.

We have developed the Unified Modeling Language $(\mathcal{L}_U)$ to support integrated modeling environments. The $\mathcal{L}_U$ uses the discipline of logic modeling [19] to represent mathematical models and domain worlds. Mathematical models are defined declaratively using predicates and standard queries rather than algebraically. This promotes a clean separation between the specification of a model and its associated solvers. In addition, the use of logic modeling supports logical deduction about domain worlds, while interfaces to solvers provides efficient computation about mathematical systems. In [16], we presented the salient features of the language with detailed examples, and defined inheritance as a way of knowledge organization in an integrative modeling environment.

In this paper, we present the formal semantics of the $\mathcal{L}_U$ . A formal semantics defines the meaning of language elements. There are three major approaches to define semantics [26] — operational, axiomatic, and denotational. In the operational approach, the state transitions of a translator for a language of interest are defined. The operational approach is targeted to implementors of the language. In the axiomatic approach, a collection of axioms defines properties of a language. The axiomatic approach, although an indirect way to define the meaning of language elements, facilitates the definition of reasoning systems for the language. In the denotational approach, a collection of equations defines the mapping from syntax to elements of a semantic domain. A denotational semantics includes a semantic domain, a meta-language to express mappings, and a collection of semantic equations, one for each syntactic category of a language.

We emphasize the denotational approach because it should precede the axiomatic and operational approaches, it has been neglected by designers of modeling languages, and it permits language definitions to be reused and extended. In related areas including object-oriented programming languages [7,23] and frame description languages [4,22], denotational semantics has been routinely defined resulting in an orderly progression of language designs. Later languages have extended and modified the denotational semantics of earlier designs. We believe that denotational semantics should likewise play the essential role in comparing and extending modeling languages.

For model management languages, measurement theory provides an attractive basis for semantics because it is concerned with homomorphic mappings from empirical worlds to mathematical systems. The $\mathcal{L}_U$ is unique in that its semantics and underlying architecture are based on homomorphic mappings from empirical relations and functions to mathematical relations and functions. The use of homomorphic mappings in the semantic domain and equations provides insight into the nature of modeling as well as a solid blueprint for implementation, comparison and expected use of the language.

In the following, Section 2 discusses related work. Section 3 proceeds with an overview of the features of $\mathcal{L}_U$ . Section 4 discusses the philosophy underlying $\mathcal{L}_U$ in which homomorphisms of measurement theory bind empirical worlds and mathematical systems. Section 5 defines the formal semantics of the $\mathcal{L}_U$ including the semantic domain and the meta-language notation, and semantic equations. Section 6 summarizes the paper and identifies further directions of research.

## 2. Related work

Measurement theory [27] and logic modeling [19] provide the foundation of our work. Foremost, we have attempted to design a knowledge representation that reflects a major concern in measurement theory: mapping from empirical worlds composed of objects and relations into mathematical systems. We strongly believe that model management systems should explicitly represent this mapping to the extent possible. Our most unique contribution is a knowledge representation with a semantics based on measurement theory and features to support an explicit mapping from the real world to mathematical models.

Logic modeling is another major influence because of the importance of a declarative representation and powerful inference procedure. There is a growing body of model management work based on logic modeling. Most notably, $[1,2]$ described a logic framework for model representation in the TEFA system. They pioneered the embedded language approach as a way to achieve economy of representation and support multiple target modeling languages.

As far as we are aware, the $L_{U}$ is the first model management language in which a denotational semantics based on measurement theory has been defined. Often semantics is defined informally through examples. In other cases, theories from logic or programming languages are used without considering the role of measurement theory. For example, $L^{\uparrow}$ and $L_{\downarrow}$ , the languages of the TEFA system, are both derivatives of the first order predicate calculus. Consequently, the semantics of predicate calculus is assumed, and the complex nature of binding empirical and mathematical worlds is not considered. Similarly, $PM^{*}$ , a language for production planning models, is formulated as a derivative of first order predicate calculus [3].

Uschold and Bundy ([6],[28]) defined Elklogic, an ecological simulation language based on the typed lambda calculus [8]. Elklogic represents both the qualitative specifications of ecological situations and the quantitative specifications in terms of differential equations. The typed lambda calculus provides a strong foundation for Elklogic because of its rich type structures and higher-order functions. However, because Elklogic relies solely on the typed lambda calculus, the semantic domain does not include homomorphic mappings and hence the measurement theoretic perspective is not considered.

Geoffrion developed a semantics for the Structured Modeling Language $[13]$ based on graph theory. He provides an elegant description of structured models as definitional systems. However, he has not addressed the role of measurement theory in definitional systems. An alternative formulation of Structured Modeling $[9]$ in terms of first order predicate calculus likewise does not consider the measurement theoretic perspective.

## 3. An overview of the unified modeling language $\mathcal{L}_U$

The Unified Modeling Language $L_{U}$ emphasizes independence between domain and mathematical knowledge and control of meaningful combinations to form models. The independence promotes autonomous and parallel development of taxonomies for better knowledge organization, and the meaningfulness of model specifications becomes the basis of automated reasoning. Fig. 1 depicts the overall view of the representation scheme. The syntax of $L_{U}$ is summarized in Appendix A. A detailed discussion of the features of the $L_{U}$ is presented in [15,17].

## 3.1. Description of domain worlds

A domain-world describes a decision situation. The description is further decomposed into an individual- and a class-level specifications (individual-world and class-world). The world of individuals is not organized. The world of classes classifies the individual elements and provides their meanings. In the analogy of relational databases, an individual-world is the extensions of relations and a class-world is the schemata of the relations. In spreadsheet models, an individual-world is specified as values with cell identifiers and a class-world as labels. In general, an individual-world is required for detailed reasoning such as model solution and expression evaluation and a class-world for high-level reasoning such as model formulation and interpretation.

At the individual level, a domain world defines an object by an identifier (ind-id), a dependency relation (ind-dep), and a collection of attribute values (attr-spec-list). The dependency shows what objects are required for the existence of the object being defined, and hence is specified by a list of individual identifiers. Each attribute value specification in an (attr-spec-list) is specified by a value (attr-val) and its unit (ind-unit) separated by keyword measured-in. The attribute value is known, unknown, or computed. Unknown values are noted by a question mark(?), and computed values by an algebraic expression. The ind-unit is specified by a specific measurement unit (unit) such as kg and \$/lb or a unit variable (unit-var).

![](/api/attachments/VQZFR3ZD/fulltext/images/6d2d75a4c4bdc0c38c2b32503c220f6d4dbe0e62b9e874d9aecb79cd3b3c70a1.jpg)  
Fig. 1. Overview of modeling world representation.

At the class level, a domain world is organized into classes (sets) of objects where each set has a class identifier (class-id), a dependency relation among classes (class-dep), and a collection of attributes (attr-def-list). The elements of a class-dep are a class, or an object set constructed by applying the aggregator All or powerset constructor Some to a class. An attribute is specified with the attribute name (attr), the mapping range (range), and the unit specification (class-unit). The range is specified with a set (set), a set identifier (set-id), an interval (interval) or a range variable (range-var). In addition to specific measurement units and variables, the class-unit may be a dimension (dimension) such as currency and length. Range and unit variables are used to partially specify the relationship between attributes without committing to a specific unit or range. They are instantiated when a class-world and an individual-world are combined into a domain-world. To illustrate, consider the following definitions:

```txt
object A
depends-on ∅
has-attributes [3 measured-in $/box, ? measured-in box]
in-class-of PRODUCT
class PRODUCT
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
depends-on ∅
has-attributes {
unit-price in-range-of R$^{+}$ measured-in $/U$_{3}$,
prod-level in-range-of R$_{1}$ measured-in U$_{3}$}
</div>

The first defines an individual object denoted by A. The empty dependency shows that the object is primitive. The object has two attributes; one attribute has the value 3 measured in dollars per box, and the other is measured in boxes but its value is unknown. The second defines the class PRODUCT. The definition shows that all objects in the class have an empty dependency (i.e., they are primitive objects), and have two attributes. Given this class definition, we can make clear the meanings of the individual definition; the object denoted by A is a product, and the two elements in the attribute value specification denote the unit price and the production level of A, respectively. Note that the unit variable used in the class definition is the means of organizing products measured in different units into the same class without committing to a specific measurement unit. Thus unit variables facilitate semantic modeling in which the modeler may use specialization/instantiation in order to denote different measurement units.

The world of individuals forces a modeler to collect the detailed data and to define detailed relationships among the objects and their attribute values. The world of classes forces the modeler to define the scope of interest by identifying the classes with their common dependencies and attributes. Combining the specifications of the two different levels, a domain world provides a proper view of the imminent decision situation. The separation promotes the flexibility of modeling in the direction of top-down or bottom-up or in parallel.

## 3.2. Description of mathematical systems

A model type (model-type) defines a mathematical system that can be applied to construct models for a specific type of decision problem. Each model type is defined by two different sets of assumptions; existential and structural. The existential assumptions (EA-list) declare what kinds of objects should exist in the domain world. If a model type is independent of application domains, it is specified by pairs of a class variable and an attribute variable – optionally, together with unit and range specifications. If a model type is defined for a specific domain, it is specified by the classes in the domain. To maximize the applicability, we require that existential assumptions in a domain dependent model type to be as general as possible. The dependency of model types on application domains determines the kinds of unification when a model type is applied to decision problems.

The structural assumption set (SA-list) defines the mathematical properties of the model type. Each assumption is specified by a predicate followed by arguments within parentheses. We can view assumption predicates as the important modeling concepts. The arguments are the class-level elements representing the domain world – classes and attributes – optionally followed by numbers or algebraic expressions. The assumptions are similar to the representation axioms in measurement theory or the axioms and postulates in abstract systems. Therefore, a domain world should satisfy the assumptions in order to utilize the mathematical system for modeling.

The metric list (MD-list) defines the mathematical relationships among the attributes in the EA-list. The standard queries (SQ-list) specify the computational procedures derived from the mathematical structure. A procedure may be simple arithmetic or be defined as a specialized solver. Explicit specification of standard queries allows us to control different computational procedures efficiently. The MD-list and SQ-list should satisfy the assumptions in SA-list. The detailed data for the attributes specified in EA-list but not defined in MD-list nor SQ-list should be supplied by the modeler as the input to the model-type.

## 3.3. Model templates and instances

Domain and mathematical knowledge are meaningfully combined in model templates. Unification constraints in a model template propagate the assumptions and standard queries of a model type to elements of a domain world. To illustrate, consider the following definitions in the $L_{U}$ :

```txt
class PRODUCT
    depends-on ∅
    has-attributes {unit-price, prod-level}
class USE
    depends-on (PRODUCT, RESOURCE)
    has-attributes {:unit-usage}
assumption linear(C₁.x, C₅.a₁)
instantiate C₅.a₁ into USE.unit-usage
instantiate C₁.x into PRODUCT.prod-level
```

The first two definitions shows the general structures of the classes PRODUCT and USE in a domain world description. (Units and ranges are omitted to make the example simple.) The third definition comes from a model type, and says that the x attribute values of objects in the class $C_{1}$ is linearly related to the $a_{1}$ attribute values of objects in the class $C_{5}$ . The last two definitions show that the attribute variable $C_{5}.a_{1}$ is instantiated into USE.unit-usage and $C_{1}.x$ into PRODUCT.prod-level in a model template. The unification constraints propagates the linear relationship defined in the model type to domain world description so that PRODUCT.prod-level is assumed to linearly related to USE.unit-usage.

A model instance binds a model template or a class-level domain specification to sources of inputs. An input source can be a user defined function, a database name or expression, an external model, or a user definition. Model instances provide a more flexible and compact way to organize data.

## 3.4. Inheritance in $\mathcal{L}_U$

Another salient feature of the $L_{U}$ is inheritance to support reuse of the specifications of domain worlds and model types. Classes in domain worlds share the attributes and dependencies of more general classes. Inheritance for domain worlds is based on interface compatibility [29] to emphasize substitution of one class with another. Model types share assumptions of more general model types. Inheritance for model types is based on behavioral compatibility [29], stronger than interface compatibility, to emphasize the similarity of assumptions among model types. Details of inheritance in $L_{U}$ are beyond the scope of this paper, but are presented in [15,16,24].

## 4. A unified view of mathematical modeling

We view mathematical modeling as developing a measurement system which facilitates reasoning about the domain world. Here, measurement means assignment of numbers to domain objects such that the assigned numbers, together with numeric relations and functions, reflect the properties of the domain world. Measurement theory provides an appealing basis to abstract mathematical models in a uniform way since it is concerned with homomorphic mappings from empirical worlds into mathematical systems.

A measurement function is fundamental if the mapping is defined directly from an empirical system to a mathematical system. A measurement function is said to be derived if it is defined in terms of other measurement functions. Measurement theory is mainly concerned with two basic problems: representation and uniqueness. The representation problem is to find sufficient conditions for the existence of a homomorphism from an empirical system to a given mathematical system. The conditions are called representation axioms and the existence of the measurement is stated by representation theorems. Uniqueness theorems define the properties and valid operations of different measurement systems.

As an example of fundamental measurement, consider extensive measurement that defines a homomorphism h embedding $\langle A, r, f \rangle$ into $\langle N, >, + \rangle$ where r is a binary relation and f is a binary operation over the objects in A, and N is the set of real numbers. The axioms for extensive measurement are:

1. the operation $\mathbf{f}$ is weakly associative,

2. $\langle A, r \rangle$ is a strict weak order,

3. the operation $\mathbf{f}$ is monotonic with respect to $\mathbf{r}$ , and

4. $\langle A, r, f \rangle$ is Archimedian. $^{1}$

The representation theorem states that if the above axioms are satisfied there exists a real valued function h on A which embeds the former relational system into the latter. The uniqueness theorem states that h is a ratio scale. (See [27] for details of the axioms and theorems.) Other types of measurement require different sets of axioms and embed empirical relational systems into different mathematical relational systems.

Extensive measurement defines a set of empirical relational systems which are embeddable into the mathematical system $\langle N, >, +\rangle$ . An instance of this set is $\langle Iron-Bars, is longer than, connect\rangle$ where Iron-Bars denotes a set of iron bars and connect an operation adjoining two iron bars. The representation theorem of extensive measurement states that we can define a real valued function, say length, over the iron bars to preserve the relation is longer than by > and the function connect by +. Therefore, mapping length as an instance of extensive measurement assigns real numbers to iron bars such that

$$
i s - l o n g e r - t h a n \left(b a r _ {i}, b a r _ {j}\right) \Leftrightarrow l e n g t h \left(b a r _ {i}\right) > l e n g t h \left(b a r _ {j}\right)
$$

$$
\operatorname{connect} \left(\operatorname{bar} _ {i}, \operatorname{bar} _ {j}\right) = \operatorname{connect} \left(\operatorname{bar} _ {k}, \operatorname{bar} _ {l}\right) \Leftrightarrow
$$

$$
\operatorname{length} \left(\text { bar } _ {i}\right) + \operatorname{length} \left(\text { bar } _ {j}\right) = \operatorname{length} \left(\text { bar } _ {k}\right) + \operatorname{length} \left(\text { bar } _ {l}\right)
$$

for all $bar_i$ , $bar_j$ , $bar_k$ and $bar_l$ .

To illustrate our view of mathematical modeling as developing a measurement system, consider a decision maker who wants to know the total length of a set of iron bars. Suppose that the lengths of the individual iron bars are already measured. Conceptually, the decision maker is measuring the length of an object, say $bar_{0}$ , which is constructed by connecting all iron bars. Here, the decision maker implicitly assumes the existence of $bar_{0}$ . With an empirical operation connect, the construction of $bar_{0}$ is specified as follows:

$$
\operatorname{bar} _ {0} = \operatorname{connect} \left(\operatorname{bar} _ {1}, \operatorname{connect} \left(\operatorname{bar} _ {2}, \dots \left(\operatorname{connect} \left(\operatorname{bar} _ {n - 1}, \operatorname{bar} _ {n}\right) \dots\right)\right) \right.
$$

Of course, the decision maker can measure the length of $bar_{0}$ as an instance of extensive measurement, i.e., by assigning a number as the value of the length of $bar_{0}$ . But that is not the intention of formulating a mathematical model. Instead, the decision maker wants to define a measurement function, say totlength, that will compute the total length of the iron bars in terms of the measurement function length. For the computation, the decision maker assumes that the fundamental measurement function length is additive to totlength. The assumption allows the decision maker to compute totlength by the following mathematical formula:

$$
\operatorname{totlength} \left(\text { bar } _ {0}\right) = \operatorname{length} \left(\text { bar } _ {1}\right) + \dots + \operatorname{length} \left(\text { bar } _ {n}\right)
$$

Mathematical modeling is analogous to developing a measurement system. In mathematical modeling one specifies the decision problem, identifies the mathematical system into which the domain world is to be embedded, makes assumptions for the embedding, and defines the required measurement functions. In the above example, the decision problem is to determine the total length of iron bars. The domain world, composed of iron bars with the is longer than relation and the connect function, is mapped into the mathematical system $\langle N, >, + \rangle$ by the given measurement function length, and the additivity assumption is made to define totlength as the sum of the lengths of individual bars. Note that we use the term ‘assumption’ instead of ‘axiom’ since models are based on assumptions to generate alternative scenarios rather than true beliefs.

With this measurement theoretic view, one abstracts mathematical models in a uniform way regardless of the underlying mathematical paradigm. For example, EOQ models can be abstracted as a system of measuring the optimum order quantity and the reorder point, and M/M/1 queueing models as a system of measuring characteristics of a queueing system such as average time in the queue or average number of customers in the system. As in measurement theory, the view emphasizes the assumptions about the structure of domain worlds. We believe that the assumptions such as the constant demand rate and the deterministic lead time for EOQ models, and Poisson process of customer arrivals and exponential distribution of service times for M/M/1 queueing models are more important than the algebraic specification of model solutions. Also the view allows us to combine mathematical modeling with logic modeling since measurement theory constructs the domain world as the relational system which is the semantic domain of first-order logic languages.

## 5. Formal semantics of $\mathcal{L}_U$

In this section, we define the formal semantics of $L_{U}$ model theoretically. As model theory investigates the relationship between a formal language and its interpretations (which is called models in logic), our semantic definitions specify the relationship of the language element to the modeling elements. That is, the meanings of the expressions of $L_{U}$ are defined to denote the modeling elements of the conceptualized modeling world. The semantics is truth conditional in that some of the syntactic elements are chosen to say things about the modeling world. In particular, the semantics of model unit is defined to specify the truth conditions in domain worlds and mathematical systems, and conditions for the meaningful combination of the domain and mathematical knowledge.

## 5.1. Semantic domain of $\mathcal{L}_U$

Following first-order model theory, we conceptualize the application domain and the mathematical system as relational systems and call them domain world and the mathematical system, respectively. The two systems are connected by homomorphic mappings. Use of mathematical systems requires the constraints that the application domain should satisfy for correct reasoning. We conceptualize the constraints as structural assumptions and separate them from the other elements. Therefore, the semantic domain is composed of a domain world and a mathematical system, and homomorphisms and assumptions specifying the connections between the two relational systems. Formally, the semantic domain of modeling language $L_{U}$ is the following tuple:

$$
\mathcal {W} = \langle \mathbf {O}, \mathbf {N}, \mathbf {R} _ {E}, \mathbf {R} _ {N}, \mathbf {F} _ {E}, \mathbf {F} _ {N}, \mathbf {F} _ {H}, \mathbf {A} \rangle
$$

O is the set of application domain objects

N is the set of numeric objects (real numbers)

$\mathbf{R}_E$ is the set of relations over $\mathbf{O}$

$$
\mathbf {R} _ {E} = \mathbf {R} _ {D} \cup \mathbf {R} _ {M} \cup \mathbf {R} _ {E} ^ {\prime}
$$

$\mathbf{R}_D$ is the set of relations showing the dependencies among the objects in $\mathbf{O}$

$\mathbf{R}_M$ is the set of measurable relations defined over $\mathbf{O}$

$\mathbf{R}_E^{\prime}$ is the set of other empirical relations, that is, $\mathbf{R}_E^{\prime} = \mathbf{R}_E - (\mathbf{R}_D \cup \mathbf{R}_M)$

$\mathbf{F}_E$ is the set of functions defined over $\mathbf{O}$

$$
\mathbf {F} _ {E} = \mathbf {F} _ {M} \cup \mathbf {F} _ {E} ^ {\prime}
$$

$\mathbf{F}_M$ is the set of mathematically computable functions over $\mathbf{O}$

$\mathbf{F}_E^\prime$ is the set of other empirical functions over $\mathbf{O}$

$\mathbf{R}_N$ is the set of relations over $\mathbf{N}$

$\mathbf{F}_N$ is the set of functions over $\mathbf{N}$

$\mathbf{F}_H$ is the set of homomorphic mappings from $\mathbf{O}$ to $\mathbf{N}$

A is the set of assumptions; an assumption a is a subset of $(2^{\mathbf{O}}\cup \mathbf{F}_H)^n\times \mathbf{N}^{m^2}$

$\mathbf{F}_E, \mathbf{F}_N$ and $\mathbf{F}_H$ may have partial functions

Without loss of generality, we define N as the set of real numbers. But it can be any set of mathematical objects that obey specified properties. Note that we keep the domain world separated from the mathematical system for clear semantics and explicit connections between the two systems.

Dependency relations represent the structure of complex and/or abstract objects showing the interrelationships among the domain objects. They are similar to 'part-of' or 'structured-as' relations. They have been defined as indexes in GAMS [25], and as the calling sequences of entities in Structured Modeling [13,14]. We precisely formalize them in the representation of domain objects and classes. The formal representation of dependencies is useful for reasoning about indexes and validating model completeness.

An $n$ -ary empirical relation $\mathbf{r}_M$ is measurable and thus is in $\mathbf{R}_M$ if and only if there exists an $n$ -ary numeric relation $\mathbf{r}_N$ in $\mathbf{R}_N$ and a (partial) mapping $\mathbf{f}_H$ in $\mathbf{F}_H$ such that

$$
\mathbf {r} _ {M} \left(\mathbf {o} _ {1}, \dots , \mathbf {o} _ {n}\right) \Leftrightarrow \mathbf {r} _ {N} \left(\mathbf {f} _ {H} \left(\mathbf {o} _ {1}\right), \dots , \mathbf {f} _ {H} \left(\mathbf {o} _ {n}\right)\right)
$$

for all $\mathbf{o}_1, \ldots, \mathbf{o}_n$ in $\mathbf{O}$ . Similarly, an $n$ -ary empirical function $\mathbf{f}_N$ is mathematically computable and thus is in $\mathbf{F}_M$ if and only if there exist an $n$ -ary numeric function $\mathbf{f}_N$ in $\mathbf{F}_N$ and a (partial) mapping $\mathbf{f}_H$ in $\mathbf{F}_H$ such that

$$
\mathbf {f} _ {M} \left(\mathbf {o} _ {i _ {1}}, \dots , \mathbf {o} _ {i _ {n}}\right) = \mathbf {f} _ {M} \left(\mathbf {o} _ {j _ {1}}, \dots , \mathbf {o} _ {j _ {n}}\right) \Leftrightarrow \mathbf {f} _ {N} \left(\mathbf {f} _ {H} \left(\mathbf {o} _ {i _ {1}}\right), \dots , \mathbf {f} _ {H} \left(\mathbf {o} _ {i _ {n}}\right)\right) = \mathbf {f} _ {N} \left(\mathbf {f} _ {H} \left(\mathbf {o} _ {j _ {1}}\right), \dots , \mathbf {f} _ {H} \left(\mathbf {o} _ {j _ {n}}\right)\right)
$$

for all $o_{i_{1}},\ldots,o_{i_{n}},o_{j_{1}},\ldots,o_{j_{n}}$ in O. Usually, measurable relations and mathematically computable functions are not represented explicitly in models, but inferred from mathematical relations and functions through homomorphic mappings.

## 5.2. Meta-language for semantic definitions

We define the semantics of $\mathcal{L}_U$ denotationally. That is, the expressions of the language are defined to denote the elements in the semantic domain $\mathcal{W}$ . Formally the semantics of $\mathcal{L}_U$ is defined by the denotation function ‘[1]’:

$$
[   [ ]   ] \colon E x p r \to \left(\mathbf {O} \cup \mathbf {N} \cup \mathbf {R} _ {E} \cup \mathbf {R} _ {N} \cup \mathbf {F} _ {E} \cup \mathbf {F} _ {N} \cup \mathbf {F} _ {H} \cup \mathbf {A} \cup \{\mathbf {T}, \mathbf {F} \}\right)
$$

where Expr is the set of legal expressions in the language. The denotation function is defined by a set of equations, one per syntactic category of the language. The semantic equations use 1) set notation, 2) predicate logic, 3) assignment function ‘:=’, and 4) meta-functions. In equations, we freely quantify the relations and functions in the domain world. The use of second-order notation is justified because finite second-order logic can be reduced to first-order through many-sorted logic ([10]). Assignment functions are an imperative specifying how to compute a metric with a mathematical procedure, which is equivalent to defining a derived measurement in measurement theory. They are similar to substitution in programming languages. The evaluation of the equations provides the formal meanings of syntactic elements.

Meta-functions are defined on syntactic elements. The function $\delta$ takes an argument of an individual or class identifier and returns its dependency. The function $\alpha$ takes an argument of an individual identifier and returns its attribute specification list. For both functions, the subscript l notes the length function, and the subscript p notes the projection function. Length and projection functions may take a dependency or attribute specification instead of an identifier.

$$
\delta \colon (I D \to 2 ^ {I D}) \cup (C I D \to 2 ^ {C I D})
$$

$$
\delta_ {l} \colon \left(\left(I D \cup 2 ^ {I D}\right)\rightarrow N a t\right) \cup \left(\left(C I D \cup 2 ^ {C I D}\right)\rightarrow N a t\right)
$$

$$
\delta_ {p} \colon \left(\left(I D \cup 2 ^ {I D}\right) \times N a t \rightarrow I D\right) \cup \left(\left(C I D \cup 2 ^ {C I D}\right) \times N a t \rightarrow C I D\right)
$$

$$
\alpha \colon I D \to 2 ^ {V \cup E}
$$

$$
\alpha_ {l} \colon (I D \cup 2 ^ {V \cup E}) \to N a t
$$

$$
\alpha_ {p} \colon (I D \cup 2 ^ {V \cup E}) \times N a t \rightarrow (V \cup E)
$$

where ID is the set of individual identifiers (ind-id)

CID is the set of class identifiers (class-id)

V is the set of numeric values (val)

E is the set of algebraic expressions (alg-expr)

Nat is the set of natural numbers $(0,1,2,\ldots)$

$2^{X}$ is the power set of $X$

Let $f$ be a function and $A$ be its domain: $\operatorname{Dom}(f) = A$ . A restriction of function $f$ to a set $B$ is noted by $f \parallel B$ . If $f$ and $g$ are functions, $f \cdot g$ is a function composed of $f$ and $g$ , that is, $f \cdot g(x) = g(f(x))$ . In semantic equations, syntactic categories are specified in typewriter font, syntactic elements in italic font, and semantic domain elements in bold font.

## 5.3. Semantics of $\mathcal{L}_U$

## 5.3.1. Semantics of individual world description

An individual identifier (ind-id) uniquely denotes an object in the domain world. There are no restrictions on the object set; each o in O can be any conceivable object. Some objects are considered as primitive, while others are not. The existence of primitive objects does not depend on others. Non-primitive objects are complex or abstract, and are constructed with simpler or more concrete objects. An individual dependency (ind-dep) makes explicit this structural information. An ind-dep denotes a sequence of objects required for the existence of an object: The dependent object together with the sequence is an instance of a $(\delta(\text{ind-dep}) + 1)$ -ary relation $r_{D}$ in $R_{D}$ . Formally, ind-id and ind-dep are defined as follows:

$$
\begin{array}{l} \llbracket \text {ind - id} \rrbracket = \mathbf {o} \text {such that} \mathbf {o} \in \mathbf {O} \\ \llbracket \text {ind - dep} \rrbracket = \langle [ [ \delta_ {p} (\text {ind - dep}, 1) ], \dots , [ [ \delta_ {p} (\text {ind - dep}, \delta_ {l} (\text {ind - dep})) ] ] \rangle \text {such that} \\ \exists \mathbf {r} _ {D} \in \mathbf {R} _ {D} \exists \mathbf {o} \in \mathbf {O} \mathbf {r} _ {D} (\mathbf {o}, [ [ \delta_ {p} (\text {ind - dep}, 1) ], \dots , [ [ \delta_ {p} (\text {ind - dep}, \delta_ {l} (\text {ind - dep})) ] ]) \end{array}
$$

The existentially quantified object in the above definition is instantiated when the dependency is combined with an identifier.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{ind-id depends-on ind-dep} \rrbracket = \langle [\text{ind-id}], [\delta_p(\text{ind-dep}, 1)], \ldots, [\delta_p(\text{ind-dep}, \delta_l(\text{ind-dep}))] \rangle$ such that $\exists \mathbf{r}_D \in \mathbf{R}_D \mathbf{r}_D([\text{ind-id}], [\delta_p(\text{ind-dep}, 1)], \ldots, [\delta_p(\text{ind-dep}, \delta_l(\text{ind-dep}))])$
</div>

In Fig. 2, for example, $[A]$ is the object $A$ which is primitive, and so has an empty dependency. On the other hand, $[U_1]$ depends on the objects $[X]$ and $[A]$ . It means that there is a relation $\mathbf{r}_D$ in $\mathbf{R}_D$ such that $\mathbf{r}_D([U_1], [X], [A])$ . The relation becomes definite when the object becomes an instance of a class in a class-level description.

Each object in O is associated with a sequence (attr-spec-list) of mathematical objects. The elements of the sequence are composed of attribute values with optional unit specification (attr-val [measured-in ind-unit]). Attribute values (attr-val) are val, ? or alg-expr. A val denotes a real number (or any other mathematical object) in N. An unknown value ? is like an anonymous variable, and hence takes some value val when it is evaluated.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[[val]] = n such that  $n \in N$ 
[?] = [[val]] for some val
</div>

An algebraic expression alg-expr is constructed as a combination of individual terms (ind-id.pos or val) and operators (fop). Each fop denotes a mathematical function in $F_{N}$ . Applied to a list of individual terms, fop defines an anonymous function. Therefore, each alg-expr is defining another function in terms of other functions.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \mathsf{f}\circ \mathsf{p}\rrbracket = \mathbf{f}_N$ such that $\mathbf{f}_N\in \mathbf{F}_N$ $\llbracket \mathsf{f}\circ \mathsf{p}$ ind-term-list $] = \llbracket \mathsf{f}\circ \mathsf{p}\rrbracket (\llbracket \mathsf{ind}\text{-term - list} ])$ $\llbracket \operatorname {alg - expr}\rrbracket = \mathbf{f}_N(\llbracket \operatorname {ind}\text{-term - list} ])$ where $\mathbf{f}_N\in \mathbf{F}_N$ and ind-term-list is the list of individual terms in the algebraic expression (alg-expr)
</div>

In the above definition, ind-term-list may include unit specifications. A measurement unit (unit) denotes the special object in the domain which is the standard (unit) for a numeric assignment function. Unit variables take the meaning of a specific unit when instantiated.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket unit\rrbracket = o_u$ such that $o_u \in O$ and $f_H(o_u) = 1$ for a mapping $f_H$ in $F_H$ $\llbracket unit - var\rrbracket = \llbracket unit\rrbracket$ for some unit
</div>

An attr-spec denotes the mathematical object returned by applying a mapping to a domain object. The mapping is defined by a class specification, and the domain object is an instance of the class. Intuitively, if the mapping assigns value 1 to the unit object, the mapping assigns the value denoted by attr-val to the presumed domain object. If unit is omitted or nilunit is specified, the unit object is existentially quantified. Formally, the semantics of attr-spec is defined as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{attr-val} \rrbracket = \text{val such that val} \in \mathbf{N}$ $\llbracket \text{attr-val measured-in ind-unit} \rrbracket = \llbracket \text{attr-val} \rrbracket$ such that
$\exists \mathbf{a} \in \mathbf{F}_H \exists \mathbf{o} \in \mathbf{O} (\mathbf{a} (\llbracket \text{ind-unit} \rrbracket) = 1 \to \mathbf{a} (\mathbf{o}) = \llbracket \text{attr-val} \rrbracket)$ $\llbracket \text{attr-spec} \rrbracket = \llbracket \text{attr-val} \rrbracket$ or $\llbracket \text{attr-val measured-in ind-unit} \rrbracket$
</div>

An ind-id has an attr-spec if there exists a mapping such that if applied to the ind-id, the mapping returns the attr-val in the attr-spec. Depending on the syntax of each element, the mapping returns the value immediately or requires a significant computational effort.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{ind-id has-attribute attr-val measured-in ind-unit} \rrbracket = \langle \llbracket \text{ind-id} \rrbracket, \llbracket \text{attr-val} \rrbracket \rangle$ such that
$\exists f \in F_H (f(\llbracket \text{ind-unit} \rrbracket) = 1 \to f(\llbracket \text{ind-id} \rrbracket) = \llbracket \text{attr-val} \rrbracket))$
</div>

If ind-unit is not specified, a unit variable is introduced by an existential quantifier. The variable will be instantiated into an attribute unit of the class to which the individual (ind-id) belongs.

Each element in an alg-spec-list is referenced by its position concatenated to the associated object identifier (ind-id.pos). However, [[pos]] should not be greater than the length of the alg-spec-list. A combination of an object identifier and an attribute specification list is the conjunction of the meanings of the permutation of the identifier and the elements in the list.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
[ind-id.pos] =
    if  $\alpha_{l}(\text{ind-id}) \leq \text{pos then}$ $\exists f \in F_{H}(f([ind-id.pos.unit]) = 1 \rightarrow f([ind-id]) = [[ind-id.pos.value]])$ 
[ind-id has-attributes attr-spec-list] =
[ind-id.1] and...and [ind-id. $\alpha_{l}(\text{ind-id})$ ]
</div>

The expressions ind-id.pos.unit and id-id.pos.value are the functions extracting the unit and value components from an attr-spec designated by ind-id.pos, respectively.

To illustrate, consider an expression ‘has-attributes [18 measured-in $N_{1}$ , $(A.2 \times U_{1}.1 + B.2 \times U_{3}.1)$ measured-in $N_{1}]$ ’ which is the attr-spec-list of X in Fig. 2. The expression A.2 refers to the second element of attr-spec-list of the objects denoted by A. Likewise, the first element 18 measured-in $N_{1}$ of the list will be referred by X.1. Combined with the object identifier X, the list means that there is a mapping with the unit object $[N_{1}]$ that maps the objects $[X]$ to the value 18, and another with the same unit object that will be computed by the algebraic expression. From the measurement theoretic perspective, the definitely known values are measured by a fundamental measurement, and others (unknown values and algebraic expressions) are defined as derived ones. From the modeling perspective, the unknown values are mathematically computed by embedding (or representing) the domain world into the mathematical system.

Together, 'object ind-id depends-on ind-dep has-attributes attr-spec-list' denotes a triple of an individual object, a sequence of objects and a sequence of attribute values such that the object depends on the objects in the dependency and has the attribute values in the attribute specification list.

```txt
Id: Product-Mix Planning
Individual-World:
A has-attributes [3 measured-in $/box, ? measured-in box]
B has-attributes [4 measured-in $/kg, ? measured-in kg]
X has-attributes [
    18 measured-in N₁,
    (A.2 × U₁.1 + B.2 × U₃.1) measured-in N₁]
Y has-attributes [
    12 measured-in N₂,
    (A.2 × U₂.1 + B.2 × U₄.1) measured-in N₂]
U₁ depends-on (X,A) has-attributes [2 measured-in gm/can]
    in-class-of Z
U₂ depends-on (Y,A) has-attributes [3] in-class-of Z
U₃ depends-on (X,B) has-attributes [2 measured-in gm/kg]
    in-class-of Z
U₄ depends-on (Y,B) has-attributes [1] class Z
P depends-on (X,Y,A,B)
    has-attributes [(A.1 × A.2 + B.1 × B.2) measured-in $]

Class-World:
PRODUCT has-attributes {
    price in-range-of R⁺ measured-in $/N₃,
    prod-level in-range-of R₁ measured-in N₃}
RESOURCE has-attributes {
    availability in-range-of 3..80 measured-in kg,
    usage in-range-of 2..70 measured-in kg}
USE
depends-on (RESOURCE, PRODUCT)
has-attributes {unit-usage in-range-of R⁺ measured-in kg/N₃}
PRODUCTION
depends-on (All(RESOURCE), All(PRODUCT))
has-attributes {revenue measured-in currency}
```  
Fig. 2. Domain world of product mix planning.

```txt
[[ind-id depends-on ind-dep has-attributes attr-spec-list]] = 
    <[ind-id], [ind-dep], [attr-spec-list] such that
    ∃r_D ∈ R_D r_D([ind-id], [δ_p(ind-dep, 1)], ..., [δ_p(ind-dep, δ_l(ind-dep))]) and
    ∃f_1 ∈ F_H (f_1([ind-id.1.unit]) = 1 → f_1([ind-id]) = [ind-id.1.value])
    and ...and
    ∃f_{α_l(ind-id)} ∈ F_H (f_{α_l(ind-id)}) ([ind-id.1.unit]) = 1 →
    f_{α_l(ind-id)} ([ind-id]) = [ind-id.α_l(ind-id).value])
For example, with the expression
Y has-attributes [
    18 measured-in N_2, (A.2 × U_1.1 + B.1 × U_3) measured-in N_2]
```

in Fig. 2, the modeler identifies that the tuple of $[Y]$ , $[\emptyset]$ , and $[18\ measured-in\ \cdots\ N_2]$ as important for the decision problem. Furthermore, the modeler specifies the relationship among the three elements: There is a dependency relation $\mathbf{r} \in \mathbf{R}_D$ such that $\mathbf{r}([Y])$ , and there are mappings $\mathbf{f}_1$ and $\mathbf{f}_2 \in \mathbf{F}_H$ such that $\mathbf{f}_1$ and $\mathbf{f}_2$ map $[Y]$ to 18 in $[N_2]$ and $[A.2 \times U_1.1 + B.1 \times U_3]$ in $[N_2]$ , respectively.

Let's consider the specification of an individual $\langle id \text{ depends-on } dp \text{ has-attributes } ASL \rangle$ for an individual identifier $id$ , an individual dependency $dp$ and an attribute specification list $ASL$ . Define $\sigma_{id}$ and $\phi_{id,i}$ as follows:

$$
\sigma_ {i d} = \exists \mathbf {r} _ {D} \in \mathbf {R} _ {D} \mathbf {r} _ {D} ([ [ i d ] ], [ [ \delta_ {p} (i d, 1) ] ], \dots , [ [ \delta_ {p} (i d, \delta_ {l} (i d)) ] ])
$$

$$
\phi_ {i d. 1} = \exists \mathbf {f} _ {1} \in \mathbf {F} _ {H} \left(\mathbf {f} _ {1} ([ [ i d. 1. \text { unit } ] ]) = 1 \rightarrow \mathbf {f} _ {1} ([ [ i d ] ]) = [ [ i d. 1. \text { value } ] ]\right)
$$

$$
\phi_ {i d. \alpha_ {l} (i d)} = \exists \mathbf {f} _ {\alpha_ {l} (i d)} \in \mathbf {F} _ {H} \left(\mathbf {f} _ {\alpha_ {l} (i d)} ([ [ i d. 1. \text {unit} ]) ]\right) = 1 \rightarrow \mathbf {f} _ {\alpha_ {l} (i d)} ([ [ i d ] ]) = [ [ i d. \alpha_ {l} (i d). \text {value} ])
$$

Then the semantics of the individual specification is defined as follows:

[id depends-on dp has-attributes ASL] =

$$
\langle [ [ i d ] ], [ [ d p ] ], [ [ A S L ] ] \rangle \mathrm{suchthat} \{\sigma_ {i d}, \phi_ {i d. 1}, \dots , \phi_ {i d. \alpha_ {l} (i d)} \}
$$

Let $ID$ be the set of identifiers in an individual-level description of the domain world, and $\langle [ID]\rangle$ , $[ \delta (ID) ]$ , $[ \alpha (ID) ]\rangle$ be the set of tuples of an individual object, the object sequence in the dependency and the attribute value list. Also let $\Sigma_{ID}$ be the set of $\sigma_{id}$ 's and $\Phi_{ID}$ be the set of $\phi_{id,k}$ 's, for all $id$ in $ID$ and $k\leq \alpha_l(id)$ . Then the union of the two sets of $\Sigma_{ID}$ and $\Phi_{ID}$ for an individual identifier set $ID$ defines the semantics of the individual-worlds:

$$
[ [ \text { individual - world } ] ] = \langle [ [ I D ], [ [ \delta (I D) ], [ [ \alpha (I D) ] ] \rangle \text {   such   that   } \Sigma_ {I D} \cup \Phi_ {I D}
$$

In other words, the individual-level description identifies the set of objects of interest together with dependencies and attribute values such that $\Sigma_{ID}$ and $\Phi_{ID}$ specify the formal meanings of the association of the objects with their dependencies and attribute values.

With the specification of the IW section in Fig. 2, for example, the modeler identifies the individual object set as $\{[\mathbf{A}], [\mathbf{B}], [\mathbf{X}], [\mathbf{Y}], [\mathbf{U}_1], [\mathbf{U}_2], [\mathbf{U}_3], [\mathbf{U}_4], [\mathbf{P}]\}$ , and asserts the dependency relations and mappings for the individuals denoted by the identifiers in the set.

To summarize, individual-world is a convenient medium to specify the detailed data about individual objects. That is, an individual-level specification identifies the individual objects in the application domain by identifiers, and specifies the structure of the objects by dependencies, and the attribute values of the objects by attribute specification lists. The specification also asserts the existence of the dependency relations defined over the domain objects and of the mappings from the domain objects to the mathematical objects. However, it does not provide a way to organize the knowledge about the application world, nor the meanings of the attribute values, which is the main role of the class-level specification.

## 5.3.2. Semantics of class-level description

A class-id denotes a set of objects in the application domain. Like individual objects, some classes are primitive, but others are not. The existence of objects in primitive classes does not depend on other objects. Non-primitive class C depends on classes $C_{1},\ldots,C_{n}$ iff, for some $dp_{C}$ in $R_{D}$ and for all $o\in C$ , there exist $o_{1}\in C_{1},\ldots,o_{n}\in C_{n}$ such that $\mathbf{dp}_{\mathbf{C}}(\mathbf{o},\mathbf{o}_{1},\ldots,\mathbf{o}_{n})$ . The class dependency is abbreviated to

$$
\mathbf {d p} _ {\mathbf {C}} (\mathbf {C}, \mathbf {C} _ {1}, \dots , \mathbf {C} _ {n})
$$

which is equivalent to

$$
\forall \mathbf {o} \exists \mathbf {o} _ {1}, \dots , \exists \mathbf {o} _ {n} \mathbf {C} (\mathbf {o}) \rightarrow \left(\mathbf {d p} _ {\mathbf {C}} (\mathbf {o}, \mathbf {o} _ {1}, \dots , \mathbf {o} _ {n}) \wedge \mathbf {C} _ {1} (\mathbf {o} _ {1}) \wedge \dots \wedge \mathbf {C} _ {n} (\mathbf {o} _ {n})\right)
$$

if we treat sets as predicates. To facilitate reasoning on properties of object sets, we define two operators on classes; All and Some. The operator Some applied to a class returns another class each member of which is a subset of the powerset of the argument class. The operator All applied to a class returns a singleton class composed of all objects in the argument class.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{class-id} \rrbracket = \mathbf{C}$ such that $\mathbf{C} \subseteq \mathbf{O}$ $\llbracket \text{All}(\text{class-id}) \rrbracket = \{\llbracket \text{class-id} \rrbracket\}$ $\llbracket \text{Some}(\text{class-id}) \rrbracket = \{\mathbf{B} \mid \mathbf{B} \subseteq \llbracket \text{class-id} \rrbracket\}$ $\llbracket \text{class-dep} \rrbracket = \langle [\delta_p(\text{class-dep}, 1]), \ldots, [\delta_p(\text{class-dep}, \delta_l(\text{class-dep}))] \rangle$ such that

$\exists \mathbf{d}\mathbf{p}_{\mathbf{C}} \in \mathbf{R}_D \exists \mathbf{C} \, \mathbf{d}\mathbf{p}_{\mathbf{C}}(\mathbf{C}, [\delta_p(\text{class-dep}, 1)], \ldots, [\delta_p(\text{class-dep}, \delta_l(\text{class-dep}))])$
</div>

The existentially quantified relation in the above definition is instantiated when the dependency is combined with a class identifier.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{class} \text{class-id depends-on class-dep} \rrbracket = \langle \llbracket \text{class-id} \rrbracket, \llbracket \delta_p (\text{class-dep}, 1) \rrbracket, \ldots, \llbracket \delta_p (\text{class-dep}, \delta_l (\text{class-dep})) \rrbracket \rangle$ such that $\mathbf{dp}_{\llbracket \text{class-id} \rrbracket}(\llbracket \text{class-id} \rrbracket, \llbracket \delta_p (\text{class-id}, 1) \rrbracket, \ldots, \llbracket \delta_p (\text{class-id}, \delta_l (\text{class-id})) \rrbracket)$
</div>

In Fig. 2, for example, by defining the pair of the class USE and the dependency (RESOURCE, PRODUCT), the modeler asserts that for each object U in [USE], there are objects R in [RESOURCE] and P in [PRODUCT] such that dp[USE](U, R, P).

While a specific measurement unit denotes a unit object, a dimension denotes a set of such unit objects. For each element in the dimension, there should be a mapping which assigns the unit value to the element.

$$
[ [ \text { dimension } ] ] = \mathbf {O} _ {u} \text {   such   that   } \mathbf {O} _ {u} \subseteq \mathbf {O} \text {   and   } \forall \mathbf {o} _ {u} \in \mathbf {O} _ {u} \exists \mathbf {f} _ {H} \in \mathbf {F} _ {H} \mathbf {f} _ {\mathrm{H}} (\mathbf {o} _ {u}) = 1
$$

Each attribute denotes a mapping from the domain objects to mathematical objects. $^{3}$ In addition, it is defined (hopefully) to preserve an n-ary measurable relation with an n-ary mathematical relation. If unit is specified, the mapping assigns to the unit object the value 1, and if dimension is specified, the unit object is an element in the unit object set denoted by the dimension. The mapping assigns to the domain objects the values within the range. A set of attributes simply denotes a set of such mappings.

$\llbracket \text{range} \rrbracket = \mathbf{N}' \text{ such that } \mathbf{N}' \subseteq \mathbf{N}$

[attr] = f\_H such that f\_H ∈ F\_H

[attr in-range-of range measured-in unit] = [attr] such that

$$
(\mathbf {r} _ {M} (\mathbf {o} _ {1}, \dots , \mathbf {o} _ {n}) \Leftrightarrow \mathbf {r} _ {N} ([ [ \texttt {a t t r} ] ] (\mathbf {o} _ {1}), \dots , [ [ \texttt {a t t r} ] ] (\mathbf {o} _ {n})))
$$

for a measurable relation $\mathbf{r}_M\in \mathbf{R}_M$ , a mathematical relation $\mathbf{r}_N\in \mathbf{R}_N$

and all $\mathbf{o}_1, \ldots, \mathbf{o}_n$ in a class $\mathbf{C}$

```json
[attr in-range-of range measured-in dimension]
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \{\text{attr-def-list}\} \rrbracket = \{\llbracket \text{attr-def} \rrbracket | \text{attr-def} \in \text{attr-def-list}\}$
</div>

[[attr in-range-of range measured-in dimension]] = [[attr]] such that $\exists \mathbf{u} \in [\text{dimension}]([\text{attr}](\mathbf{u}) = 1)$ and $[\overline{\text{attr}}](\mathbf{C}) \subseteq [\text{range}]$ and $(\mathbf{r}_M(\mathbf{o}_1, \ldots, \mathbf{o}_n) \Leftrightarrow \mathbf{r}_N([\text{attr}](\mathbf{o}_1), \ldots, [\text{attr}](\mathbf{o}_n)))$ for a measurable relation $\mathbf{r}_M \in \mathbf{R}_M$ , a mathematical relation $\mathbf{r}_N \in \mathbf{R}_N$ , and $\mathbf{o}_1, \ldots, \mathbf{o}_n$ in a class $\mathbf{C}$

```txt
[attr-def] =
```

```txt
[attr in-range-of range measured-in unit] or
```

If range is omitted, it is equated to N. If unit is omitted, it is assumed to be a variable over O. Concatenation of an attribute to a class identifier denotes the restriction of the attribute mapping to the class. The unit object may or may not be in the class, but it is in the domain of the attribute mapping. A tuple of a class identifier and a set of attributes abbreviates the concatenations of the attributes to the class identifier.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{class-id.} \text{attr-def} \rrbracket = \llbracket \text{attr} \rrbracket \text{such that} \left( \llbracket \text{attr} \rrbracket (\llbracket \text{attr.unit} \rrbracket) = 1 \right) \text{and} \llbracket \text{attr} \rrbracket (\llbracket \text{class-id} \rrbracket) \subseteq \llbracket \text{attr.range} \rrbracket \text{and} \exists \mathbf{r}_M \in \mathbf{R}_M \exists \mathbf{r}_N \in \mathbf{R}_N \forall \mathbf{o}_1, \ldots, \mathbf{o}_n \in \llbracket \text{class-id} \rrbracket (\mathbf{r}_M (\mathbf{o}_1, \ldots, \mathbf{o}_n) \Leftrightarrow \mathbf{r}_N (\llbracket \text{attr} \rrbracket (\mathbf{o}_1), \ldots, \llbracket \text{attr} \rrbracket (\mathbf{o}_n)))$ $\llbracket \text{class-id has-attributes} \{\mathsf{a}_1, \ldots, \mathsf{a}_n\} \rrbracket = \llbracket \text{class-id.a}_1 \rrbracket \text{and} \ldots \text{and} \llbracket \text{class-id.a}_n \rrbracket$
</div>

A class definition provides summary information about the objects in the class. The class dependency declaring the dependency relation summarizes the common structure of the objects in the class. The attribute set declaring the domain of mappings characterizes the objects in the class.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{class-id depends-on class-dep has-attributes } \{a_1, \ldots, a_n\} \rrbracket = \langle \llbracket \text{class-id} \rrbracket, \llbracket \text{class-dep} \rrbracket, \llbracket \{a_1, \ldots, a_n\} \rrbracket \rangle$ such that $\mathbf{dp}_{\llbracket \text{class-id} \rrbracket}(\llbracket \text{class-id} \rrbracket, \llbracket \delta_p(\text{class-id}, 1) \rrbracket, \ldots, \llbracket \delta_p(\text{class-id}, \delta_l(\text{class-id})) \rrbracket)$ and $\llbracket \text{class-id.} a_1 \rrbracket$ and ... and $\llbracket \text{class-id.} a_n \rrbracket$
</div>

For example, consider the following class definition in Fig. 2:

## PRODUCTION depends-on (All(RESOURCE), All(PRODUCT)) has-attributes {revenue measured-in currency}

With the definition, the modeler asserts that the objects in [[PRODUCTION]] depend on all objects in [[RESOURCE]] and [[PRODUCT]], and there is a measurable relation of interest, say prefer to, which is to be preserved by the mapping revenue measured in some currency with the relation > in the mathematical system.

Let's consider a class definition $\langle cid\ depends-on\ cdp\ has-attributes\ \{a_1,\ldots,a_n\}\rangle$ for a class identifier $cid$ , a class dependency $cdp$ and an attribute definition set $\{a_1,\ldots,a_n\}$ . We also define $\sigma_{cid}$ and $\phi_{cid.a_i}$ 's for $i\leq n$ as follows:

$$
\sigma_ {c i d} = \mathbf {d p} _ {[ c i d ]} \left(\llbracket c i d \rrbracket , \llbracket \delta_ {p} (c i d, 1) \rrbracket , \dots , \llbracket \delta_ {p} (c i d, \delta_ {l} (c i d)) \rrbracket\right)
$$

$$
\phi_ {c i d. a _ {i}} = \left(\llbracket a _ {i} \rrbracket (\llbracket a _ {i}. \text { unit } \rrbracket) = 1\right) \text {   and   } \llbracket \overline {{a _ {1}}} \rrbracket (\llbracket c i d \rrbracket) \subseteq \llbracket a _ {i}. \text { range } \rrbracket \text {   and   }
$$

$$
\exists \mathbf {r} _ {i M} \in \mathbf {R} _ {M} \exists \mathbf {r} _ {i N} \in \mathbf {R} _ {N} \forall \mathbf {o} _ {1}, \dots , \mathbf {o} _ {n} \in [ [ c i d ] ]
$$

$$
\left(\mathbf {r} _ {i M} (\mathbf {o} _ {1}, \dots , \mathbf {o} _ {n}) \Leftrightarrow \mathbf {r} _ {i N} \big ([ [ a _ {i} ] ] (\mathbf {o} _ {1}), \dots , [ [ a _ {i} ] ] (\mathbf {o} _ {n}) \big)\right)
$$

Then the semantics of the class definition is defined as follows:

[[cid depends-on cdp has-attributes $\{a_1,\ldots ,a_n\} ] =$

$$
\langle [ c i d, [ c d p ], [ \{a _ {1}, \dots , a _ {n} \} ] \rangle \text {   such   that   } \{\sigma_ {c i d}, \phi_ {c i d. a _ {1}}, \dots , \phi_ {c i d. a _ {n}} \}
$$

Let $CID$ be the set of all class identifiers in the class-level description of a domain world, $\langle [CID, [\delta(CID)], [\alpha(CID)]\rangle$ be the set of tuples of classes, dependences and attribute definition lists, and $CA$ be the attributes concatenated to their class identifier. For example, in the above class definition, $CID$ is a singleton $\{cid\}$ , $\langle [CID], [\delta(CID)], [\alpha(CID)]\rangle$ is $\{\langle [cid, [cdp], [\{a_1, \ldots, a_n\}]\rangle\}$ , and $CA$ is the set of $n$ elements $\{cid.a_1, \ldots, cid.a_n\}$ . And let $\Sigma_{CID}$ be the set of $\sigma_{cid}$ 's and $\Phi_{CA}$ be the set of $\phi_{cid.a_i}$ 's for all $cid$ in $CID$ and $a_i$ in the attribute set of $cid$ . Then the semantics of a class-world is defined as the union of the two sets of $\Sigma_{CID}$ and $\Phi_{CA}$ for class identifier set $CID$ and attribute set $CA$ in the class definitions:

$$
[ [ \text { class - world } ] ] = \langle C I D \rangle , [ [ \delta (C I D) ], [ [ \alpha (C I D) ] ] \rangle \text { such   that } \Sigma_ {C I D} \cup \Phi_ {C A}
$$

With the specification of the CW section in Fig. 2, for example, the modeler defines the classes $\{[PRODUCT], [RESOURCE], [USE], [PRODUCTION]\}$ , identifies the dependency relations for the classes $(\mathbf{dp}_{[PRODUCT]}, \ldots, \mathbf{dp}_{[PRODUCTION]})$ , and the attributes of interest for each class.

A class-world facilitates high-level reasoning in modeling. In the specification, a modeler defines the object classes in the application domain, identifies the dependency relation for each class, and specifies attributes of interest as the mappings from the class objects to the mathematical objects. However, details of individual objects are not described in class-level specifications. A individual-world instantiates a class-world, and the latter provides the meanings of the elements in the former. A domain-world which is the combination of a individual-world and a class-world will provide the overall description of the domain world.

## 5.4. Semantics of domain world description

Now we are ready to define the formal semantics of domain world specifications. Let $ID$ and $CID$ be the sets of individual and class identifiers specified in a domain world. Recall that $\sigma_{id}$ is defined in the previous subsection to assert that the tuple of $[id]$ and the objects in $[\delta(id)]$ is an instance of an existentially quantified dependency relation. When combined with a class-level description, the relation is instantiated into $\mathbf{dp}_{cid}$ for a $cid \in CID$ :

$$
\sigma_ {i d} ^ {\prime} = \mathbf {d p} _ {[ [ c i d ] ]} ([ [ i d ] ], [ [ \delta_ {p} (i d, 1) ] ], \dots , [ [ \delta_ {p} (i d, \delta_ {l} (i d)) ] ])
$$

Similarly, the existentially quantified mapping in $F_{H}$ for each $\phi_{id,i}$ is instantiated into $[cid.a_{i}]$ for a $cid \in CID$ and an $a_{i}$ in the attribute set of cid. However, the id.i.unit should be compatible with $cid.a_{i}.unit$ . Two units are compatible if they are convertible. Two specific measurement unit $u_{i}$ and $u_{j}$ are convertible iff there is a numeric function g which systematically transforms the measurement in terms of $u_{i}$ into the other in terms of $u_{j}$ :

$$
\text { convertible } (u _ {i}, u _ {j}) \Leftrightarrow \exists \mathbf {g} \in \mathbf {F} _ {N} \mathbf {f} _ {u _ {i}} = \mathbf {f} _ {u _ {j}} \cdot \mathbf {g}
$$

where $f_{u_{i}}$ and $f_{u_{j}}$ are measurement functions which assign unit values to $[u_{i}]$ and $[u_{j}]$ . We call g the conversion function of $u_{i}$ into $u_{j}$ . The semantics of an attribute specification of an individual is instantiated as follows:

$$
\phi_ {i d, i} ^ {\prime} = \llbracket c i d. a _ {i} \rrbracket (c i d. a _ {i}. \text {unit}) = 1 \rightarrow \llbracket c i d. a _ {i} \rrbracket (\llbracket i d \rrbracket) = \llbracket \alpha_ {p} (i d, i). \text {value} \rrbracket \cdot \mathbf {f}
$$

where f is the conversion function of id.i.unit into cid.a;.unit.

Let $\Sigma_{ID}^{\prime}$ and $\Phi_{ID}^{\prime}$ be the set of $\sigma_{id}^{\prime}$ 's and $\phi_{id}^{\prime}$ 's, respectively. And define $\Sigma_{CID}$ and $\Phi_{CA}$ as in the previous subsection. Then the semantics of domain-world is the set of individual objects and classes and the set of assertions specified by the union of $\Sigma_{ID}^{\prime}, \Phi_{ID}^{\prime}, \Sigma_{CID}$ , and $\Phi_{CA}$ :

[domain-world] =

$$
\begin{array}{l} \langle [ [ I D ], [ [ \delta (I D) ], [ [ \alpha (I D) ] ] \rangle \cup \langle [ [ C I D ], [ [ \delta (C I D) ], [ [ \alpha (C I D) ] ] \rangle \text {   such   that } \\ \Sigma_ {I D} ^ {\prime} \cup \Phi_ {I D} ^ {\prime} \cup \Sigma_ {C I D} \cup \Phi_ {C A} \end{array}
$$

By combining individual- and class-level descriptions into domain-world, the modeler identifies the extensions of classes, dependency relations and attribute mappings. In the other direction, the modeler organizes and interprets the individual objects into the class definitions. In the top-down modeling, the class descriptions can be viewed as the constraints on the instantiation of class objects. In bottom-up modeling, they can be viewed as the classification criteria for individual objects to organize the domain knowledge.

As a comprehensive example, consider Product Mix Planning in Fig. 2. With the specification of an individual object $[id]$ , the modeler asserts $\sigma_{id}^{\prime}$ and $\phi_{id,i}^{\prime}$ 's. For example, with the specification of the object $[A]$ , the modeler asserts the following dependency relation and attribute mapping:

$$
\sigma_ {\mathrm{A}} ^ {\prime} = \mathbf {d p} _ {[ [ \text { PRODUCT } ] ]} ([ [ \mathrm{A} ] ])
$$

$$
\phi_ {\mathrm{A}. 1} ^ {\prime} = [ \text {PRODUCT.unit - price} ] ([ A ]) = 3   / b o x
$$

So, the object $[A]$ is described in detail. With the definition of a class $[cid]$ , the modeler asserts $\sigma_{cid}$ and $\phi_{cid.a_{i}}$ 's. For example, with the definition of the class $[PRODUCTION]$ , the modeler declares the dependency relation and attribute mapping as follows:

$\sigma_{\mathrm{PRODUCTION}} =$

$$
\mathbf {d p} _ {[ [ \text { PRODUCTION } ] ]} ([ [ \text { PRODUCTION } ], [ [ \text { All(RESOURCE) } ], [ [ \text { All(PRODUCT) } ] ])
$$

$\phi_{\mathrm{PRODUCTION.revenue}} =$

$\exists \mathbf{c} \in [\text{currency}] (\text{[revenue]}(\mathbf{c}) = 1)$ and [revenue] (PRODUCTION) $\subseteq \mathbf{N}$ and

$$
\forall \mathbf {P} _ {i}, \mathbf {P} _ {j} \in [ [ \text { PRODUCTION } ] ] (\text { prefer   } \mathbf {P} _ {i} \text {   to   } \mathbf {P} _ {j} \Leftrightarrow [ [ \text { revenue } ] ] (\mathbf {P} _ {i}) > [ [ \text { revenue } ] ] (\mathbf {P} _ {j}))
$$

We believe that the semantics of the specification of Product Mix Planning is well defined by $\Sigma_{ID}^{\prime}$ , $\Phi_{ID}^{\prime}$ , $\Sigma_{CID}$ and $\Phi_{CA}$ constructed as above. In addition, by combining the specifications of two different levels, the modeler partitions the object set into the classes. The partition can be acquired either by instantiating classes or by classifying individual objects. The following shows the partition the modeler gets after specifying Product Mix Planning:

$$
[ [ \text { PRODUCT } ] ] = \{[ [ \mathrm{A} ], [ [ \mathrm{B} ] ] \}
$$

$$
[ [ \text { RESOURCE } ] = \{[ [ X ], [ [ Y ] ] \}
$$

$$
[ \mathbf {U S E} ] = \{\left[ \mathbf {U} _ {1} \right], \left[ \mathbf {U} _ {2} \right], \left[ \mathbf {U} _ {3} \right], \left[ \mathbf {U} _ {4} \right] \}
$$

$$
[ [ \text { PRODUCTION } ] ] = \{[ [ \text { P } ] ] \}
$$

## 5.5. Semantics of model types

A model type is a mathematical pattern developed by management scientists to solve an important class of problems. As such, each model type is defined by existential assumptions (EA-list) declaring the object classes in the domain world, structural assumptions (SA-list) imposing the mathematical structure on the domain world, and metric definitions (MD-list) and standard queries (SQ-list)

mathematically specifying the class of problems and their solution procedures. Existential assumptions are similar to specifying the domain world at the class level except that class and attribute variables are used in domain independent model types. Structural assumptions are relations defined over classes and attributes, and represent important mathematical modeling concepts. Metric definitions specify the relationships between attributes in the existential assumptions, and governed by the structural assumptions. Standard queries are metric definitions together with the solver specifications.

Classes, dependencies and attributes defined in model types have the same semantics as those in domain worlds; object sets, dependency relations and homomorphic mappings. If variables are used for class or attribute specifications, they become a specific class or attribute through instantiation.

```txt
[class-var] = [[class-id]] for some class-id
[attr-var] = [[attr-def]] for some attr-def
[class-var.attr-var] = [[attr-var]] || [class-var]]
```

As defined in the syntax, the EA-list of domain dependent model types is defined by class definitions, and that of domain independent model types by pairs of a class variable and an attribute variable. Let CID be the set of class identifiers in a domain dependent model type. Depending on the domain dependency of the model type, let CA be the set of pairs of a class identifier and an associated attribute definition or the set of pairs of a class variable and an attribute variable. And define $\sigma_{cid}$ , $\phi_{cid.a_i}$ , $\Sigma_{CID}$ and $\Phi_{CA}$ as defined for [[class-world]]. For domain independent model types, define $\phi_{cvar.avar}$ to be the semantics of a pair cvar.avar of a class variable and an attribute variable, and $\Phi_{CA}$ to be the set of $\phi_{cvar.avar}$ 's. The semantics of EA-list is the same as [[class-world]]:

$$
[ [ E A - l i s t ] ] = \langle [ [ C I D ], [ [ \delta (C I D) ], [ [ \alpha (C I D) ] ] \rangle \text {   such   that   } \Sigma_ {C I D} \cup \Phi_ {C A}
$$

But note that if the model type is domain independent, $\Sigma_{CID}$ is empty and the variables in CA should be instantiated for each $\phi_{cvar.avar}$ in $\Phi_{CA}$ to take a definite meaning.

Structural assumptions are made on classes. For example, one may assume that a class is static, which means that the object set defined by a class does not change during the modeling period. Then, a relation, say static, is defined over the classes and denoted by a predicate static. The semantic value of the relation is a subset of the power set of the domain objects, that is, $\left[\left[static\right]\subseteq2^{0}\right]$ . The assumptions on classes often accompany a numeric value. For example, in Fig. 3 of M/M/1 Queueing Model Type, it is assumed by $eq(|PROCESSOR|,1)$ that there is one and only one processor. The semantics of the predicate eq can be defined as a subset of $(2^{0}\times N)\times N$ ; first the class is mapped to a number by the cardinality function ‘||’ and then the mapping and a numeric value form an instance of the eq relation.

Assumptions are frequently made on attributes, too. One may assume, for example, that attribute values can be definitely measured and do not change during the modeling period; $constant(C_{1}.a)$ in Fig. 4. Then $[constant]$ is a subset of $F_{H}$ . Also assumptions are made on more than one attributes like $linear(C_{5}.lhs, C_{4}.x)$ , letting $[linear]$ be a subset of $F_{H} \times F_{H}$ . We define structural assumptions as a relation over classes and attributes, optionally including a sequence of numeric values and algebraic expressions.

$\llbracket \text{assump-pred}_{n+m} \rrbracket \subseteq (2^{\mathbf{0}} \cup \mathbf{F}_H)^n \times \mathbf{N}^m$

where $n$ is the number of class terms and $m$ is the number of values and algebraic expressions in the argument list

[a r g] = C or $\mathbf{f}_H$ or $\mathbf{n}$ where $\mathbf{C} \subseteq \mathbf{O}$ , $\mathbf{f}_H \in \mathbf{F}_H$ , and $\mathbf{n} \in \mathbf{N}$

$\llbracket SA \rrbracket = \llbracket \text{assump-pred}(\text{arg-list}) \rrbracket =$

if [arg-list] ∈ [assump-pred] then T else F

![](/api/attachments/VQZFR3ZD/fulltext/images/b63bd8ac3cf8a0c80178b07e5ab2096fba6b825f3cb4d15c60aa95b02d87f715.jpg)  
Fig. 3. M/M/1 queueing model type.

Let $\theta$ be the semantics of a structural assumption in SA-list, and $\Theta$ be the set of all $\theta$ 's:

$$
\Theta = [ [ S A - l i s t ] ]
$$

The semantics of metrics is similar to that of attributes. They are mappings from an existentially assumed class to the specified range and are defined to preserve a measurable relation over the class objects with a mathematical relation over N. The mapping also returns the unit value (which is usually 1) for the unit object.

$$
\begin{array}{r l} & {\llbracket \text {metric} \rrbracket = \mathbf {f} _ {H} \in \mathbf {F} _ {H} \text {such that}} \\ & {\qquad \mathbf {f} _ {H} (\llbracket \text {metric.unit} \rrbracket) = 1 \text {and} \overline {{\mathbf {f} _ {H}}} (\mathbf {C}) \subseteq \llbracket \text {metric.range} \rrbracket \text {and}} \\ & {\qquad (\mathbf {r} _ {M} (\mathbf {o} _ {1}, \dots , \mathbf {o} _ {n}) \Leftrightarrow \mathbf {r} _ {N} (\mathbf {f} _ {H} (\mathbf {o} _ {1}), \dots , \mathbf {f} _ {H} (\mathbf {o} _ {n})))} \end{array}
$$

for a measurable relation $\mathbf{r}_M\in \mathbf{R}_M$ , a mathematical relation $\mathbf{r}_N\in \mathbf{R}_N$ , a class $\mathbf{C}$ , and all domain objects $\mathbf{o}_1,\ldots ,\mathbf{o}_n\in \mathbf{O}$

Applying a mathematical function to a metric is equivalent to composing the two functions. That is, mathematical objects mapped by the metric from domain objects are computed again by the mathematical function. The composition maps a domain object to a mathematical object, so defining another metric.

$$
\begin{array}{r l} \llbracket \text {fop metric} \rrbracket & = \llbracket \text {metric} \rrbracket \cdot \llbracket \text {fop} \rrbracket \\ & = \mathbf {f}: \mathbf {F} _ {H} \to \mathbf {N} \\ & = \mathbf {f}: (\mathbf {C} \to \mathbf {N}) \to \mathbf {N} \\ & = \mathbf {f}: \mathbf {C} \to \mathbf {N} \\ & = \mathbf {f} _ {M} \cdot \llbracket \text {metric} \rrbracket \end{array}
$$

The commutative diagram is shown in Fig. 5. The mathematical operation fop performs the computation in the mathematical system mirroring the empirical operation of a mathematically computable function $\mathbf{f}_M$ in $\mathbf{F}_M$ .

$$
\mathbf {f} _ {M} \cdot [ [ \text { metric } _ {i} ] ] = [ [ \text { metric } _ {j} ] ] \cdot [ [ \text { fop } ] ]
$$

For example, a mathematical function + composed with a metric revenue which preserves the relation prefer to in $R_{M}$ computes numerically to mirror the empirical operation, say combine in $F_{M}$ :

$$
[ [ \text { revenue } ] ] (\text { combine } (\mathbf {A}, \mathbf {B})) = [ [ \text { revenue } ] ] (\mathbf {A}) + [ [ \text { revenue } ] ] (\mathbf {B})
$$

Therefore, the empirical operation combine which may be difficult, or even impossible is replaced with simple arithmetic.

More generally, a mathematical function applied to a list of metrics defines a new metric. And hence the semantics of algebraic expressions composed of metrics and mathematical functions is defined as metrics.

[fop]: $\mathbf{N}^n\to \mathbf{N}$ for $n$ -ary fop

$$
\begin{array}{r l} \llbracket \text {fop metric - list} _ {k} \rrbracket & = \mathbf {f}: \mathbf {F} _ {H} ^ {k} \to \mathbf {N} \\ & = \mathbf {f}: ((\mathbf {C} _ {1} \to \mathbf {N}) \times \dots \times (\mathbf {C} _ {k} \to \mathbf {N})) \to \mathbf {N} \\ & = \mathbf {f} ^ {\prime}: (\mathbf {C} _ {1} \times \dots \times \mathbf {C} _ {k}) \to \mathbf {N} \\ & = \mathbf {f} ^ {\prime \prime}: \mathbf {C} _ {k + 1} \to \mathbf {N} \\ & = \llbracket \text {metric} \rrbracket \end{array}
$$

where $\mathbf{C}_{k + 1}$ depends on $\mathbf{C}_1,\dots ,\mathbf{C}_k$

$$
[ [ \text { alg - expr } ] ] = [ [ \text { metric } ] ]
$$

The metric definitions show the relationships among the metrics and are subject to the assumptions specified in domain terms. For example, in Fig. 4, the metric definition of $C_5$ .lhs should be linear with respect to $C_4$ .x as specified by assumptions in the SA-list. By a metric definition, the mapping on the left hand side is substituted by the assignment operator with the metric specified as the algebraic expression on the right hand side.

$$
\begin{array}{r l} & {\llbracket \text {metric - def} \rrbracket = \llbracket \text {metric = alg - expr} \rrbracket =} \\ & {\llbracket \text {metric} \rrbracket := \llbracket \text {alg - expr} \rrbracket} \end{array}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Id: LP Type
EA-list:
    attribute a associated-with  $C_{1}$ 
    attribute b associated-with  $C_{2}$ 
    attribute c associated-with  $C_{3}$ 
    attribute x associated-with  $C_{4}$ 
    attribute lhs associated-with  $C_{5}$ 
    attribute z associated-with  $C_{6}$ 

SA-list:
    deterministic( $C_{1}.a$ )
    constant( $C_{1}.a$ )
    deterministic( $C_{2}.b$ )
    constant( $C_{2}.b$ )
    deterministic( $C_{3}.c$ )
    constant( $C_{3}.c$ )
    le( $C_{5}.lhs, C_{2}.b$ )
    continuous( $C_{4}.x$ )
    nonnegative( $C_{4}.x$ )
    linear( $C_{5}.lhs, C_{4}.x$ )
    linear( $C_{6}.z, C_{4}.x$ )

MD-list:
    $C_{6}.z = C_{3}.c \times C_{4}.x$ $C_{5}.lhs = C_{1}.a \times C_{4}.x$ 

SQ-list:
    Optimize  $C_{6}.z$ 
    s.t.  $C_{5}.lhs \leq C_{2}.b$ $C_{4}.x \geq 0$ 
    with [simplex]]

IP Type
    attribute a associated-with  $C_{1}$ 
    attribute b associated-with  $C_{2}$ 
    attribute c associated-with  $C_{3}$ 
    attribute  $x_{1}$  associated-with  $C_{4}$ 
    attribute  $x_{2}$  associated-with  $C_{5}$ 
    attribute lhs associated-with  $C_{6}$ 
    attribute z associated-with  $C_{7}$ 

deterministic( $C_{1}.a$ )
    constant( $C_{1}.a$ )
    deterministic( $C_{2}.b$ )
    constant( $C_{2}.b$ )
    deterministic( $C_{3}.c$ )
    constant( $C_{3}.c$ )
    le( $C_{6}.lhs, C_{2}.b$ )
    continuous( $C_{4}.x_{1}$ )
    nonnegative( $C_{4}.x_{1}$ )
    discrete( $C_{5}, x_{2}$ )
    nonnegative( $C_{5}.x_{2}$ )
    linear( $C_{6}.lhs, C_{4}.x_{1}$ )
    linear( $C_{7}.z, C_{4}.x_{1}$ )
    linear( $C_{6}.lhs, C_{5}.x_{2}$ )
    linear( $C_{7}.z, C_{5}.x_{2}$ )

$C_{7}.z = C_{3}.c \times (C_{4}.x_{1} + C_{5}.x_{2})$ $C_{6}.lhs = C_{1}.a \times (C_{4}.x_{1} + C_{5}.x_{2})$

Optimize  $C_{7}.z$ 
s.t.  $C_{6}.lhs \leq C_{2}.b$ $C_{4}.x_{1} \geq 0$ $C_{5}.x_{2} \geq 0$ 
with [simplex-with-rounding,
branch-and-bound,
cutting-planes]
</div>

Fig. 4. Optimization model types.

From the measurement theoretic perspective, the assignment can be viewed as defining the metric on the left hand side as a derived measurement function which will be computed with the algebraic expression. From the modeling perspective, the assignment can be viewed as specifying the computational (inference) procedure of a modeling object—the metric on the left hand side.

Let $\xi_{\text{metric}}$ be the semantics of a metric definition, $MD$ the set of metrics defined in MD-list, and $\Xi_{MD}$ the set of $\xi_m$ for all $m \in MD$ . Then $\Xi_{MD}$ is the semantics of MD-list.

$$
\Xi_ {M D} = [ [ M D - l i s t ] ]
$$

An algebraic equation is composed of a mathematical relational operator and a list of terms where each term is an algebraic expression. The semantics of the equation is the same as defined in first-order logic except that it is defined at the class level instead of at the individual level. The semantic definition is naturally extended for lists of algebraic equations.

![](/api/attachments/VQZFR3ZD/fulltext/images/57a2a376369e31d1dd2ad33fae67c8783fe413e254136339ccbc0b579e4f70db.jpg)  
Fig. 5. Commutative diagram of algebraic expression.

$\llbracket \mathsf{r}\circ \mathsf{p}\rrbracket \subseteq \mathbf{N}^n$ for $n$ -ary rop

[alg-eqn] = [rop term-list] =

if [term-list] $\subseteq$ [rop] then T else F,

$$
[ [ a l g - e q n - l i s t _ {n} ] ] = [ [ r o p _ {1} \text {term - list} _ {1}, \dots , r o p _ {n} \text {term - list} _ {n} ] ] = \{\mathrm{T}, \mathbf {F} \} ^ {n}
$$

Note that the semantics of alg-eqn is defined by a subset relation instead of a membership relation, for the notation is at the class level.

Similarly to mathematical operations, a mathematical relation rop mirrors a measurable relation $r_{M}$ in $R_{M}$ . For example, $\leq$ preserves the measurable relation is less than or equal to such that ‘the total usage of a resource is less than or equal to the availability of the resource’ iff

## RESOURCE.usage ≤ RESOURCE.availability

where usage and availability are the metrics mapping resource objects to numeric objects.

A standard query in a model type is a special kind of metric definition. It specifies not only an interesting metric, but also mathematically interpreted constraints and the computational procedures of the metric values. The computational procedure may be simple enough to compute with usual mathematical functions, or very complex requiring external solver systems. In both cases, we see that the procedure defines the query metric mathematically. Then the semantics of a query is asking to compute mathematically the metric satisfying all constraints. The semantics of a standard query SQ is the conjunction of an imperative to compute the metric with the solver or solver-expr and a conditional asserting that the computation will satisfy all constraints.

```ini
[query] = [metric s.t. alg-expr-list_n] =
    [metric] such that [alg-expr-list_n] = T^n
[solver expr] = f_N ∈ F_N
[solver] = solver ∈ F_N
[SQ_metric] = [metric s.t. alg-eqn-list_n = solver expr] =
    [metric] := [solver expr] and
    if [metric] = [solver expr] then [alg-eqn-list_n] = T^n
[SQ_metric] = [metric s.t. alg-eqn-list_n with solver-list] =
```

$$
\begin{array}{l} \llbracket \text {metric} \rrbracket := \llbracket \text {solver - expr} \rrbracket \text {and} \\ \text {if} \llbracket \text {metric} \rrbracket = \llbracket \text {solver} \rrbracket \text {then} \llbracket \text {alg - eqn - list} _ {n} \rrbracket = \mathbf {T} ^ {n} \\ \text {for all solver in solver - list} \end{array}
$$

For example, the standard query of LP type in Fig. 4 specifies that the metric $\llbracket$ Optimize $C_6.z\rrbracket$ is interesting and the value satisfying the linear constraints can be computed by the solver simplex.

For each standard query which will compute a metric, define $\xi_{metric}$ to be the semantics of $SQ_{metric}$ :

$$
\xi_ {m e t r i c} = [ [ m e t r i c ] ] := [ [ s o l v e r - e x p r ] ] \text {   and   }
$$

$$
\text { if   } [   [ m e t r i c ]   ] = [   [ s o l v e r - e x p r ]   ] \text {   then   } [   [ a l g - e q n - l i s t _ {n} ]   ] = T ^ {n}
$$

Define $\Xi_{SQ}$ to be the set of $\xi_{\text{metric}}$ 's defined for each query in (sq-list) in a model type.

For each n-ary measurable relation r in $R_{M}$ , define $\gamma_{r}$ to be the relation preserving condition:

$$
\gamma_ {\mathbf {r}} = \exists [ [ r o p ] ] \in \mathbf {R} _ {N} \exists [ [ m ] ] \in \mathbf {F} _ {H} \forall \mathbf {o} _ {1} \dots \mathbf {o} _ {n} \in \mathbf {O}
$$

$$
\mathbf {r} (\mathbf {o} _ {1} \dots \mathbf {o}) \text {iff} [   [ r o p ]   ] ([   [ m ]   ] (\mathbf {o} _ {1}), \dots , [   [ m ]   ] (\mathbf {o} _ {n}))
$$

For each $n$ -ary mathematically computable function $\mathbf{f}$ in $\mathbf{F}_M$ , define $\gamma_{\mathbf{f}}$ to be the function preserving condition:

$$
\begin{array}{l} \gamma_ {\mathbf {f}} = \exists [ [ f o p ] ] \in \mathbf {F} _ {N} \exists [ [ m ] ] \in \mathbf {F} _ {H} \forall \mathbf {o} _ {i _ {1}} \dots \mathbf {o} _ {i _ {n}} \mathbf {o} _ {j _ {1}} \dots \mathbf {o} _ {j _ {n}} \in \mathbf {O} \text { and } \\ \quad \mathbf {f} (\mathbf {o} _ {j _ {1}}, \dots , \mathbf {o} _ {j _ {n}}) \Leftrightarrow \\ \quad [ [ f o p ] ] ([ [ m ] ] (\mathbf {o} _ {i _ {1}}), \dots , [ [ m ] ] (\mathbf {o} _ {i _ {n}})) = [ [ f o p ] ] ([ [ m ] ] (\mathbf {o} _ {j _ {1}}), \dots , [ [ m ] ] (\mathbf {o} _ {j _ {n}})) \end{array}
$$

Let $\Gamma_{\mathbf{R}}$ be the set of $\gamma_{\mathbf{r}}$ 's and $\Gamma_{\mathbf{F}}$ is the set of $\gamma_{\mathbf{f}}$ 's.

The semantics of model-type is defining classes whose properties are specified by the union of the sets of the assertions defined above:

[model-type] =

$$
\begin{array}{l} \langle [ [ C I D ] ], [ [ \delta (C I D) ] ], [ [ \alpha (C I D) ] ] \rangle \text {   such   that } \\ \Sigma_ {C I D} \cup \Phi_ {C A} \cup \Theta \cup \Xi_ {M D} \cup \Xi_ {S Q} \cup \Gamma_ {\mathbf {R}} \cup \Gamma_ {\mathbf {F}} \end{array}
$$

Note that $\Gamma_{R}$ and $\Gamma_{F}$ are not well defined until the domain world is fully conceptualized. But they are the constraints which modelers should keep in mind when combining a model type with a domain world. We include them in the semantics of model-type as a guideline for modeling. Developed by management scientists who are basically mathematicians, model types have prescriptive meanings while domain specifications are descriptive in general. We believe that our semantic definitions are rigorous enough to impose the developers' intention on the applications of model types. In particular, the sets $\Theta$ , $\Gamma_{R}$ and $\Gamma_{F}$ will help modelers or decision makers decide whether the modeling situation can be formulated into the specific mathematical form and to evaluate the validity of the models thus formulated.

## 5.6. Semantics of model templates and instances

A model template is a combination of a model type with a domain world formalizing a recurring pattern of decision problems. For example, Feed-Mix is a model template applying the LP model type to the situations in which decision makers want to optimize the use of a few kinds of raw materials with the fulfillment of minimum requirements. The elements in the model-template are inherited from the specifications of a domain-world and a model-type. The semantics of the unification constraints (UC-list) makes clear the connection between the two systems.

The term ‘unification’ is commonly defined as the problem of, given the descriptions of X and Y, finding Z that will fit both X and Y [20]. In the $L_{U}$ , the set of unification constraints in a model template defines the constraints of specialization and/or instantiations which make the mathematical concepts defined in the model type applicable to the domain world. Thus after applying the unification constraints to the model type and propagating the assumptions to the domain world, the two descriptions become identical. In this sense, our usage of the term is consistent with the definition, and extends first-order unification to decision models. Other types of extension are described in [20].

Consider a specialization of a metric $cid_{i}.a_{i_{t}}$ in a domain dependent model type to an attribute $cid_{j}.a_{j_{k}}$ in a domain world. Specializing a metric to an attribute restricts the former mapping to the latter. For the restriction of the mapping, the domain of the latter ( $cid_{j}$ ) should be a subset of that of the former ( $cid_{i}$ ). But again, to be in the subset relation, the classes in the dependency of the latter should be the subclasses of the corresponding classes in the dependency of the former. In addition, units in the two mappings should be compatible, and values returned by the restricted mapping should be within the range of the unrestricted. More precisely, the semantics of the specialization is defined as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\llbracket \text{specialize } cid_i.a_{i_l} \text{ into } cid_j.a_{j_k} \rrbracket =$ $\llbracket cid_j \rrbracket \subseteq \llbracket cid_i \rrbracket$ and
$\llbracket \delta_p (cid_j, 1) \rrbracket \subseteq \llbracket \delta_p (cid_i, 1) \rrbracket$ and ... and $\llbracket \delta_p (cid_j, \delta_l (cid_j)) \rrbracket \subseteq \llbracket \delta_p (cid_i, \delta_l (cid_i)) \rrbracket$ and $\llbracket cid_j.a_{j_k} \rrbracket = \llbracket cid_i.a_{i_l} \rrbracket \parallel \llbracket cid_{j_k} \rrbracket$ and
$\llbracket cid_j.a_{j_k}.\text{range} \rrbracket \subseteq \llbracket convert (cid_i.a_{i_l}.\text{range in } cid_i.a_{i_l}.\text{unit}, cid_j.a_{j_k}.\text{unit}) \rrbracket$
</div>

In the definition, the function convert takes two arguments—a value set in one scale (unit) and another unit, and converts the value set in the second unit. Therefore, convert(1..100 in m, cm) returns 100..10000 (in cm scale) as its value. According to the definition, expression ‘specialize EVENT.rate into ARRIVAL.rate’ in Fig. 6 means that ARRIVAL and CUSTOMER are a subset of EVENT and OBJECT, respectively, and that ARRIVAL.rate is the restriction of the occurrence rate of EVENT’s to ARRIVAL’s.

On the other hand, class and attribute variables are substituted to classes and attributes such that every instantiation of a pair of a class variable and an attribute variable is a specialization of the instantiated pair of the class and attribute. To illustrate, suppose that a pair cvar.avar of a class and an attribute variables in a model type is instantiated to a pair $cid_{i}.a_{i_{l}}$ of a class and an attribute definitions in the model template. Then the semantics of the instantiation is to assign cvar.avar to a class $cid_{k}$ and an attribute $a_{k_{n}}$ such that $cid_{i}.a_{i_{l}}$ is a specialization of $cid_{k}.a_{k_{n}}$ .

[instantiate cvar.avar into $cid_{i}.a_{i}$ ] =

$$
[ c v a r. a v a r ] := [ c i d _ {k}. a _ {k _ {n}} ] \text {   and   } [ \text { specialize   } c i d _ {k}. a k _ {n} \text {   into   } c i d _ {i}. a _ {i _ {l}} ]
$$

In other words, an instantiation is the combination of a variable substitution and a specialization. The substitution is for multiple instantiations of the variables. In mathematical terms, the substitution is constructing a matrix big enough to accommodate all instantiations of the variable, and the specialization is partitioning the matrix. Suppose that the same cvar.avar is instantiated to $cid_{j}.a_{j_{m}}$ again. Then the semantics of $cid_{k}$ should be general enough for both the classes $cid_{i}$ and $cid_{j}$ to be its subclasses, i.e., $(\llceil cid_{i}\rrbracket \cup \llbracket cid_{j}\rrbracket) \subseteq \llbracket cid_{k}\rrbracket$ . For another example, if $C_{5}.lhs$ in the LP type is instantiated to RAW-MATERIAL.usage and to LABOR.usage again, then the value of $C_{5}$ should be a superset of the union of RAW-MATERIAL and LABOR such as RESOURCE which includes raw material and labor as well as machine capacity.

```txt
Id: Customer Checkout System Model Template
DW:
    CUSTOMER has-attributes {waiting-time, time-for-checkout}
    ARRIVAL depends-on (CUSTOMER, INTERVAL)
    has-attributes {arrival-rate}
    CHECKOUT depends-on (CLERK, CUSTOMER)
    has-attributes {checkout-time}
    QUEUE depends-on Some(CUSTOMER)
    has-attributes {#-of-customers}
    COUNTER depends-on (CHECKOUT, QUEUE)
    has-attributes {#-of-customers}
    ARRIVALS depends-on All(ARRIVAL)
    has-attributes {mean-arrival-rate}
    CHECKOUTS depends-on All(CHECKOUT)
    has-attributes {mean-checkout-time}
    QUEUES depends-on All(QUEUE)
    has-attributes {avg-#-of-checkout}
    STORE depends-on All(COUNTER)
    has-attributes {avg-#-of-checkout}
    CUSTOMERS depends-on All(CUSTOMER)
    has-attributes {avg-time-in-queue, avg-time-for-checkout}
MT: M/M/1 Queuing Model Type
UCL:
specialize OBJECT.waiting-time into CUSTOMER.waiting-time
specialize EVENT.rate into ARRIVAL.arrival-rate
...
specialize EVENTS.mean-rate into ARRIVALS.mean-arrival-rate
specialize PROCESSES.mean-time into CHECKOUTS.mean-checkout-time
...
specialize OBJECTS.avg-time-in-system
into CUSTOMERS.avg-time-for-checkout
```  
Fig. 6. Customer checkout system model template.

Let $\omega_{cid_i.a_{i_l}}$ be the semantics of a unification (a specialization or an instantiation into $cid_i.a_{i_l}$ ): $\omega_{cid_i.a_{i_l}} = [\text{specialize } cid_k.a_{k_n} \text{ into } cid_i.a_{i_l}] \text{ or } [\text{instantiate cvar.avar into } cid_i.a_{i_l}]$

Unification propagates the structural assumptions, metric definitions and standard queries of the model type to the model template. Consider an assumption $P(cid_{i})$ in a model type, and suppose that there is a unification $\omega_{cid_{i}.a_{j_{m}}}$ whose left hand side is $cid_{i}.a_{i_{k}}$ in a model template. Since the semantics of the unification implies $cid_{j} \subseteq cid_{i}$ , we can deduce $P(cid_{j})$ .

$$
\begin{array}{c} \left\{P (c i d _ {i}), \omega_ {c i d _ {j}. a _ {j _ {m}}} \right\} \vDash \left\{P (c i d _ {i}), c i d _ {j} \subseteq c i d _ {i} \right\} \\ \vDash P (c i d _ {j}) \end{array}
$$

For example, we can infer infinite(CUSTOMER) from infinite(OBJECT) given the unification 'specialize OBJECT.waiting-time into CUSTOMER.waiting-time' in Fig. 6, The same is true for attributes. Similarly, the assumption continuous(PRODUCT.prod-level) is inferred from the unification 'instantiate $C_4.x$ into PRODUCT.prod-level' and the assumption continuous( $C_4.x$ ).

Consider a model template. Let $\Omega_{CA}$ be the set of all $\omega_{cid.a_i}$ 's defined in the model template. Note that $CA$ is the set of all pairs of class identifier and the associated attributes of the accompanying domain world description. Let $\Theta$ be the assumptions in the model type. Given $\Omega_{CA}$ and $\Theta$ , define $\Theta/\Omega_{CA}$ to be the set of assumptions specified in terms of classes and attributes in the domain world through all $\omega_{cid.a_i}$ in $\Omega_{CA}$ . Then the union of the two sets implies a set $\Theta/\Omega_{CA}$ :

$$
\Theta \cup \Omega_ {C A} \vDash \Theta / \Omega_ {C A}
$$

On the other hand, since the metrics and standard queries are defined and solved based on the structural assumptions, and since the assumptions are propagated to the domain classes and attributes by the above implication, we can restate the metric definitions, standard queries and solution procedures in domain terms. For example, a query metric and the solver expression in Fig. 3

OBJECTS.avg-time-in-system

PROCESSES.mean-time - EVENTS.mean-rate

can be reformulated in domain terms as

CUSTOMER.avg-time-for-checkout

1

for the Customer Checkout System Model Template in Fig. 6.

Again, let $\Xi_{MD}/\Omega_{CA}$ and $\Xi_{SQ}/\Omega_{CA}$ be the sets of metrics and queries derived from the metric definitions and standard queries of the model type through the unification constraints $\Omega_{CA}$ .

A model template combines a domain world and a model type through the unification constraints list. The semantics of the three components is as follows:

$$
\begin{array}{l} \llbracket \text {domain - world} \rrbracket = \\ \quad \langle [ [ I D _ {W} ], [ [ \delta (I D _ {W}) ], [ [ \alpha (I D _ {W}) ] ] \rangle \cup [ [ C I D _ {W} ], [ [ \delta (C I D _ {W}) ], [ [ \alpha (C I D _ {W}) ] \rangle \text {such that} \\ \Sigma_ {I D _ {W}} ^ {\prime} \cup \Phi_ {I D _ {W}} ^ {\prime} \cup \Sigma_ {C I D _ {W}} \cup \Phi_ {C A _ {W}} \\ \llbracket \text {model - type} \rrbracket = \\ \quad \langle [ [ C I D _ {T} ], [ [ \delta (C I D _ {T}) ], [ [ \alpha (C I D _ {T}) ] ] \rangle \text {such that} \\ \Sigma_ {C I D _ {T}} \cup \Phi_ {C A _ {T}} \cup \Xi_ {M D} \cup \Xi_ {S Q} \cup \Theta \cup \Gamma_ {\mathbf {R}} \cup \Gamma_ {\mathbf {F}} \\ \llbracket U C - l i s t \rrbracket = \Omega_ {C A _ {W}} \end{array}
$$

$\Sigma_{ID_{w}}^{\prime}$ and $\Phi_{ID_{w}}^{\prime}$ will be empty in most cases, and $\Sigma_{CID_{T}}$ is also empty if the model type is domain independent.

In addition, through the unification we derive three more semantics sets, namely, $\Theta/\Omega_{CA_{w}}$ which is the set of structural assumptions imposed on the domain classes ( $CID_{w}$ ) and attributes ( $CA_{w}$ ), and $\Xi_{MD}/\Omega_{CA_{w}}$ and $\Xi_{SQ}/\Omega_{CA_{w}}$ which are the sets of metrics and queries restated in domain terms ( $CA_{w}$ ). When defining a model template, decision makers and modelers want to compute the metrics in $\Xi_{SQ}/\Omega_{CA_{w}}$ . For the computation of those metrics, the assumptions in $\Theta/\Omega_{CA_{w}}$ are required. We include explicitly these two sets in the semantics of model templates since they are more important than $\Theta$ and $E_{SQ}$ themselves for modeling. Therefore, the semantics of model-template is the union of 15 sets.

$$
\begin{array}{r} \llbracket \text {model - template} \rrbracket = \Sigma_ {I D _ {W}} ^ {\prime} \cup \Phi_ {I D _ {W}} ^ {\prime} \cup \Sigma_ {C I D _ {W}} \cup \Phi_ {C A _ {W}} \cup \\ \Sigma_ {C I D _ {T}} \cup \Phi_ {C A _ {T}} \cup \Xi_ {M D} \cup \Xi_ {S Q} \cup \Theta \cup \Gamma_ {\mathbf {R}} \cup \Gamma_ {\mathbf {F}} \cup \\ \Omega_ {C A _ {W}} \cup \Xi_ {M D} / \Omega_ {C A _ {W}} \cup \Xi_ {S Q} / \Omega_ {C A _ {W}} \cup \Theta / \Omega_ {C A _ {W}} \end{array}
$$

The role of unification $\Omega_{CA_W}$ is summarized as follows:

$$
\left(\Sigma_ {C I D _ {W}} \cup \Phi_ {C A _ {W}}\right) \stackrel {\Omega_ {C A _ {W}}} {\Longrightarrow} \left(\Sigma_ {C I D _ {T}} \cup \Phi_ {C A _ {T}}\right)
$$

$$
\Theta \stackrel {\Omega_ {C A _ {W}}} {\Longrightarrow} \Theta / \Omega_ {C A _ {W}}
$$

$$
\Xi_ {M D} \xrightarrow {\Omega_ {C A _ {W}}} \Xi_ {M D} / \Omega_ {C A _ {W}}
$$

$$
\Xi_ {S Q} \xrightarrow {\Omega_ {C A _ {W}}} \Xi_ {S Q} / \Omega_ {C A _ {W}}
$$

where $X \stackrel{Z}{\Rightarrow} Y$ denotes that $X$ is transformed into $Y$ through the unification constraints $Z$ .

On the other hand, $\Gamma_{R}$ and $\Gamma_{F}$ connect between $\langle O, R_{M}, F_{M} \rangle$ which is a subsystem of the domain world and the mathematical system $\langle N, R_{N}, F_{N} \rangle$ . We have included the two semantic sets because we want to remind modelers and decision makers of the fact that quantitative reasoning should always be validated in terms of those empirical semantic sets.

## 6. Summary and directions

We presented the philosophy and the formal semantics of the Unified Modeling Language $(\mathcal{L}_{U})$ . The philosophy underlying the $L_{U}$ stresses the integration of logic and mathematical modeling to provide deduction and quantitative problem solving. This integration requires a uniform representation of models regardless of domain and mathematical paradigm. Measurement theory, concerned with homomorphic mappings from empirical to mathematical worlds provides an appealing basis to abstract mathematical models in a uniform manner. We described in detail the role of homomorphic mappings in the denotational semantics of the $L_{U}$ . Homomorphic mappings are explicitly represented in the semantic domain of the $L_{U}$ and they are used in semantic equations to define conditions that bind empirical and mathematical worlds in models.

An important direction is to extend the denotational semantics and develop certain kinds of automated reasoning. We have extended the denotational semantics to inheritance based on partial order relations for domain worlds and model types. The rationale and definitions of inheritance are described in [HMG91], while the denotation of partial order relations is described in [Hong91]. We are currently developing a deductive inference system for types, units of measure, and indices that permits substitution according to the partial order relations. The heart of the inferencing system is a collection of unification algorithms for domain worlds and model types. We plan to extend the rules of inference in type systems of programming languages [Card84,88] to dimensional analysis ([Brid31], [Fock53], [Lang51]). We are also interested in further extending the inference system with qualitative reasoning capabilities [KHS90].

Another interesting direction for our work is the dynamic aspects of modeling. Most work in model management has emphasized the static aspects of modeling but largely ignored the dynamic aspects. Consequently, decision makers and modelers lack support for proper documentation of model evolutions

I change management. We aim to extend our knowledge representation so that model changes as well their causality and evolution can be explicitly represented. To enhance the performance of modelers, will develop operators for propagation of changes both within and between models, and generation of dels from the specification of possibly non-existing, incomplete, and multiple versions of decision blems.

## endix A. Syntax of $\mathcal{L}_U$

The syntax of the language is specified by BNF notation. The left hand side denotes syntactic nents, and the right hand side defines the element on the left hand side. Syntactic categories are in $\text{bewriter font}$ , and keywords in $\text{bold}$ . Vertical bars ‘|’ denote a selection from possible definitions. List denotes a possibly empty, comma-separated list of X’s and X- $\text{list}^{+}$ denotes a nonempty list X’s. Square brackets ‘[]’ surround optional elements. Double quotes enclose comments. Angled ckets ‘<〉’, parentheses ‘()’, and braces ‘{}’ denote themselves.

```txt
del := domain-world | model-type | model-template | model-instance
main-world := <world-id, individual-world, class-world>

dividual-world := individual-list+ | model-instance
dividual := 
object] ind-id
[depends-on ind-dep]
has-attributes attr-spec-list+
[in-class-of class-spec]

ass-spec := class-id | class-var
tr-spec := attr-val [measured-in ind-unit]
d-unit := unit | unit-var
tr-val := val | ind-term | alg-expr
d-term := ?| ind-id.pos
d-dep := <ind-id-list>

ass-world := class-def-list
ass-def := 
class] class-id
[depends-on class-dep]
has-attributes {attr-def-list+}
ass-dep := <cdp-list>
o := class-id | All(class-id) | Some(class-id)
tr-def := attr [in-range-of range] [measured-in class-unit]
range := set | set-id | interval | range-var
ass-unit := unit | dimension | unit-var

del-type :=
{model-type-id, EA-list+, SA-list+, MD-list, SQ-list+}
"existential assumption" := attr-var-def | class-def
```

```ini
SA "structural assumption" := [assumption assump-pred(arg-list⁺)
attr-var-def :=
    [attribute] attr-var
    [in-range-of range]
    [measured-in class-unit]
    associated-with class-spec
arg := val | class-term | alg-expr
class-term :=
    class-spec | class-id.attr | attr-var
MD "metric definition" := metric = alg-expr
metric := class-id.attr-def | class-var.attr-var
SQ "standard query" :=
    query = solver-expr | query with solver-list⁺
solver-expr := alg-expr
query := [fop] metric [s.t. alg-eqn-list]
alg-eqn := alg-expr  rop alg-expr

model-template := <model-template-id, domain-world-id,
    model-type-id, UC-list>
UC "unification constraint" :=
    specialize class-id.attr into class-id.attr |
    instantiate class-var.attr-var into class-id.attr

model-instance :=
    <model-instance-id, class-model-id, metric-source-list>
class-model-id := domain-world-id | model-template-id
metric-source := metric source
source := user defined function | ← database name |
    ← external model name | : definition

alg-expr := op term | term binary-op term
term := val | ind.term | class-term | alg-expr | (alg-expr)
```

## References

[1] H. Bhargava and S. Kimbrough, "On Embedded Languages for Model Management," in Proc. 23rd Hawaii Intl. Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, Hawaii, January 1990.

[2] H. Bhargava, S. Kimbrough, and R. Krishnan, “Unique Name Violations: A Problem for Model Integration (Or You Say Tomato, I Say tomahto),” ORSA Journal on Computing, 1990.

[3] H. Bhargava and R. Krishnan, “A Formal Approach in a Model Management System,” in Proc. 23rd Hawaii Intl. Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, Hawaii, January 1990.

[4] A. Borgida, R. Brachman, D. McGuiness, and L. Resnick, “CLASSIC: A Structural Data Model for Objects,” in Proc. ACM SIGMOD Conf., Portland, Oregon, May 1989, pp. 58–67.

[5] P. Bridgeman, Dimensional Analysis, Yale University Press, New Haven, CT, 1931.

[6] A. Bundy and M. Uschold, “The Use of Typed Lambda Calculus for Requirements Capture in the Domain of Ecological Modelling,” DAI Research Paper No. 446, Department of Artificial Intelligence, University of Edinburgh, October 1989.

[7] L. Cardelli, “A Semantics of Multiple Inheritance,” in Semantics of Data Types, Lecture Notes in Computer Science, 173, Springer-Verlag, 1984, pp. 51–67.

[8] L. Cardelli, “Structural Subtyping and the Notion of Power Type,” in Proceedings ACM POPL, 1988.

[9] S. Chari and R. Krishnan, “Towards a Logical Reconstruction of Structured Modeling,” in Proc. 23rd Hawaii Intl. Conf. on System Science, Kona-Kailua, Hawaii, 1990.

[10] H. Enderton, Mathematical Introduction to Logic, 1972.

[11] C. Focken, Dimensional Methods and Their Applications, Edward Arnold and Co., London, U.K., 1953.

[12] S. Gass, “Managing the Modeling Process: A Personal Reflection,” European Journal of Operational Research 31, 1 (July 1987), pp. 1–8.

[13] A. Geoffrion, "Introduction to Structured Modeling," Management Science, 33, 5, May 1987, 547-588.

[14] A. Geoffrion, “Formal Aspects of Structured Modeling,” Operations Research, 37, 1, January-February 1988, pp. 30–51.

[15] S. Hong, A Formal, Unified Modeling Framework: Knowledge Representation and Automated Reasoning, Ph.D. Disseration, The University of Texas at Austin, Dept. of Management Science and Information Systems, August 1991.

[16] S. Hong, M. Mannino, and B. Greenberg, “Inheritance and Instantiation in Model Management,” in Proc. 23rd Hawaii Intl. Conference on System Sciences, Decision Support and Knowledge Based Systems Track, Kona-Kailu, Hawaii, January 1990, pp. 424–432.

[17] S. Hong, M. Mannino, and B. Greenberg, “Measurement Theoretic Representation of Large, Diverse Model Bases: The Unified Modeling Language $L_{U}$ ,” Decision Support Systems 10, 1993, 319–340.

[18] J. Kalagnanam, M. Henrion, and E. Subrahmanian, “The Scope of Dimensional Analysis in Qualitative Reasoning,” Working Paper, Carnegie Mellon University, January 1990.

[19] S. Kimbrough and R. Lee, “Logic Modeling: A Tool for Management Science,” Decision Support Systems, April, 4, 1, 1988, pp. 3–16.

[20] K. Knight, “Unification: A Multidisciplinary Survey,” ACM Computing Survey Vol. 21, No. 1, March 1989, pp. 93–124.

[21] H. Langhaar, Dimensional Analysis and Theory of Models, John Wiley, New York, N.Y., 1951.

[22] H. Levesque and R. Brachman, “Expressiveness and Tractability in Knowledge Representation and Reasoning,” Computational Intelligence, Vol. 3, 1987, 78–93.

[23] M. Mannino, I. Choi, and D. Batory, “The Object-Oriented Functional Data Language,” IEEE Trans. Software Engineering 16, 11 (Nov. 1990), 1258–1272.

[24] M. Mannino, B. Greenberg, and S. Hong, “Model Libraries: Knowledge Representation and Reasoning,” ORSA Journal on Computing, Summer 1990, 2, 3, 287–301.

[25] A. Meeraus, “An Algebraic Approach to Modeling,” Journal of Economic Dynamics and Control, Vol. 5, 1983, pp. 81–108.

[26] F. Pagan, Formal Specification of Programming Languages-A Panoramic View, Prentice-Hall, 1981.

[27] R. Roberts, Measurement Theory, Addison-Wesley Publishing Company, 1979.

[28] M. Uschold, “The Use of Domain Information for Comprehension and Construction of Simulation-Models,” DAI Research Paper No. 534, Department of Artificial Intelligence, University of Edinburgh, October 1991.

[29] P. Wegner, “Concepts and Paradigms of Object-Oriented Programming,” OOPS Messenger 1, 1 (August 1990), ACM, 7–87.

![](/api/attachments/VQZFR3ZD/fulltext/images/118de842cd50c14c64ebee7004806825963122538c04300773111827b313315e.jpg)  
Sa Neung Hong received a B.Ag. degree from the Seoul City University in 1976 and a Ph.D. degree from the University of Texas, Austin in 1991. He is currently a lecturer of information systems in the Department of Management Science and Information Systems at the University of Texas at Austin. His research interests are in model management, integration of modeling paradigms, constraint satisfaction problems, distributed systems, telecommunication, and organizational computing.

![](/api/attachments/VQZFR3ZD/fulltext/images/4bf5b0ea473687e8c132629b160bc2a481b452c0ce5444b658e18f46bc1fd233.jpg)

Michael V. Mannino received a B.B.A. degree from the University of Cincinnati in 1978 and an M.S. and a Ph.D. degree both from the University of Arizona. Tucson in 1981 and 1983, respectively. He was an assistant professor in the Department of Management Science and Information Systems at the University of Texas at Austin. He joined the Department of Management Science, University of Washington, Seattle in September 1991. Dr. Mannino teaches and conducts research in the areas of database management, software engineering, and knowledge representation. His articles have appeared in major journals including IEEE Transactions on Software Engineering, IEEE Transactions on Knowledge and Data Engineering, ACM Computing Surveys, MIS Quarterly, Journal of Management Information Systems, and ORSA Journal of Computing.
