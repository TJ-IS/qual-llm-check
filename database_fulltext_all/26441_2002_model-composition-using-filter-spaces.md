---
otero_id: 26441
otero_key: "Q7858FAK"
title: "Model Composition Using Filter Spaces"
authors: "Kaushal Chari"
year: "2002"
journal: "Information Systems Research"
doi: "10.1287/isre.13.1.15.95"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.252.86.83] On: 15 September 2016, At: 13:27 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/Q7858FAK/fulltext/images/3453a4f8f7d09acee78105842a3f85484bd26ca20b29d11ea205ecc63e872290.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Model Composition Using Filter Spaces

Kaushal Chari,

## To cite this article:

Kaushal Chari, (2002) Model Composition Using Filter Spaces. Information Systems Research 13(1):15-35. http:// dx.doi.org/10.1287/isre.13.1.15.95

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2002 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/Q7858FAK/fulltext/images/804a670beefe28328be6f08a3d4b07303faf0e626eaeb6a527e1365844582882.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Model Composition Using Filter Spaces

Kaushal Chari

Information Systems/Decision Sciences, College of Business Administration, University of South Florida, 4202 East Fowler Avenue, CIS 1040, Tampa, Florida 33620-7800 kchari@coba.usf.edu

D ecision support systems (DSS) typically contain data and models to facilitate decision making. DSS users, in response to a particular decision-making situation, often execute a sequence of models, in which inputs to a model in the sequence are obtained from outputs of other models upstream in the sequence and from database retrievals. The problem of generating a sequence of models from the set of available models is known as the model composition problem. In this paper, we propose a new construct called filter spaces to support model composition. We show how filter spaces can significantly facilitate automation of model composition and execution process, and provide effective means to integrate partial solutions from multiple composite models and databases.

(Decision Support Systems; Model Management; Model Composition)

## 1. Introduction

Decision support systems (DSS) consist of data and models, where models are viewed as computerexecutable procedures that typically require data inputs (Chang et al. 1993, Will 1975, Sprague and Carlson 1982, Bonczek et al. 1981). Examples of a model include: a demand-forecasting program that uses price data to forecast product demands, and a productionplanning program based on linear programming that determines the optimal quantities of products to be produced. For certain decision-making situations, a sequence of models is executed in order to answer a query. Typically, inputs to a model in the sequence are obtained from outputs of other models upstream in the sequence and from database retrievals. The problem of composing a sequence of models (i.e., creating a composite model) in response to a user query is known as the model composition problem (Krishnan 1993). In model composition, the internal schemata of models are not exposed for manipulation. This contrasts with other forms of model integration such as “deep” integration (Geoffrion 1999) in structured modeling (Geoffrion 1987) and ASCEND (Krishnan et al. 1993) where the internal schemata of models are combined into a single schema.

Model composition and execution pose many challenges. First, generating an appropriate sequence of models by searching the set of available models in an organization can be computationally complex, especially when there are many model resources (Basu and Blanning 1994). Second, a composite model may provide only a partial solution to a query. Generating multiple composite models and then combining their solutions to answer a given query may not be simple. Third, in order for the DSS to be user friendly, the process of model composition as well as the process of model execution (including data acquisition from multiple commercial databases) should be automated. Developing data and model representation schemes to support automation of model composition and execution can be challenging.

## 1.1. Model Composition Example

Consider a DSS of a hypothetical organization, ABC Inc., that can access two database tables as shown in Table 1 and Table 2, and a collection of models as shown in Table 3. Table 1 contains data on items (products with pid [product identifier] in the range 101–104) that are produced by ABC Inc., while Table 2 contains data on items that are procured from vendors (products with pid in the range 105–106). In Table 2, unit\_cost represents the price ABC Inc. pays to vendors for each unit of item procured. For items produced by ABC Inc., unit\_cost is not stored but computed using a composite model.

Table 1 Relation ptable1 Containing Data on Items Produced at ABC

<table><tr><td>Pid</td><td>pname</td><td>price</td></tr><tr><td>101</td><td>Washer-1/4</td><td>4.00</td></tr><tr><td>102</td><td>Washer-1/2</td><td>6.00</td></tr><tr><td>103</td><td>Bolt-2</td><td>8.00</td></tr><tr><td>104</td><td>Bolt-3</td><td>10.00</td></tr></table>

Table 2 Relation ptable2 Containing Data on Items Outsourced for Production

<table><tr><td>Pid</td><td>pname</td><td>price</td><td>unit_cost</td></tr><tr><td>105</td><td>Hinge-1/2</td><td>12.00</td><td>6.00</td></tr><tr><td>106</td><td>Hinge-1</td><td>14.00</td><td>7.00</td></tr></table>

Consider query1 that requires unit\_cost of all products sold by ABC Inc. The output for query1 is shown in Table 4. A single data source cannot provide all the data needed for the query. Instead, partial solutions from two composite models as well as data retrieved from a database table are combined to obtain the output for query1. The composite model obtained by linking models dem1 and prod1 generates the first two rows of the query output corresponding to pid 101 and 102 in Table 4. dem1 uses input data from ptable1, namely price, to generate forecasted demands for products with pid 101 and 102. The demand vector (i.e., quantity) generated by dem1 is the input to model prod1. Model prod1 uses a production function to compute unit\_cost for products 101 and 102. Similarly, another composite model that links model dem2 and prod2 is used to generate unit\_cost for products with pid 103 and 104. unit\_cost data for products with pid 105 and 106 are retrieved directly from the database table ptable2.

Consider query2 that requires unit\_cost as well as price information for all products sold by ABC Inc. In this case, the outputs from prod1 and prod2 respectively, are joined with ptable1 in order to generate the first four records in Table 5.

The above two examples highlight the need for a DSS to support features such as: (1) the capability to generate one or more composite models and to combine their partial solutions to answer a user-specified query with minimal or no human intervention, and (2) the capability to automate the process of executing one or more composite models, by hiding all formatting and data retrieval details from the user. The need to have automation during model composition and execution is also highlighted by the results of a recent study (Wright et al. 1998). In our view, user-controlled automation, where users are able to affirm the component models being selected, is more desirable than having no automation or having total automation in the model composition process. However, with regard to the composite model execution process, total automation is certainly very desirable.

In this paper we present a new theoretical construct called filter spaces as the basis to support the capabilities discussed above. Filter spaces are n-dimensional spaces that provide a means to represent constraints on data attribute values, as well as support for an inferential mechanism to determine if a collection of database and model resources satisfy stated constraints on data attribute values. Filter spaces enable the integration of partial solutions from multiple composite models as well support the automation of model composition and execution process. In the next section, we review the existing literature on model composition and highlight the benefits of our approach.

## 1.2. Literature Review

Few papers on model composition are available in the literature (see surveys by Blanning 1993, Dolk and Kottemann 1993, and Krishnan 1993). The capabilities of select model composition approaches available in the literature are summarized in Table 6.

In Table 6, Type denotes the logical representation of composite models, which can be relational, graphical, knowledge-based, or script-based. In the relational approach, models are treated as virtual relations whose tuples are generated on demand. Two models are linked together by joining their corresponding virtual relations, thereby facilitating model composition. The relational approach does not provide any mechanisms to differentiate between two models that map the same

Table 3 Models Accessible to DSS Users

<table><tr><td>Name</td><td>Type</td><td>Input</td><td>Output</td></tr><tr><td>dem1</td><td>Demand forecasting model for products with pid 101 and 102</td><td>price</td><td>quantity</td></tr><tr><td>dem2</td><td>Demand forecasting model for products with pid 103 and 104</td><td>price</td><td>quantity</td></tr><tr><td>prod1</td><td>Production model for products with pid 101 and 102</td><td>quantity</td><td>unit_cost</td></tr><tr><td>prod2</td><td>Production model for products with pid 103 and 104</td><td>quantity</td><td>unit_cost</td></tr></table>

<table><tr><td colspan="2">Table 4 Output for query1</td></tr><tr><td>Pid</td><td>unit_cost</td></tr><tr><td>101</td><td>2.00  $$  dem1 → prod1</td></tr><tr><td>102</td><td>3.00  $$ </td></tr><tr><td>103</td><td>4.00  $$  dem2 → prod2</td></tr><tr><td>104</td><td>5.00  $$ </td></tr><tr><td>105</td><td>6.00  $$  ptable2</td></tr><tr><td>106</td><td>7.00  $$ </td></tr></table>

Table 5 Output for query2

<table><tr><td>Pid</td><td>price</td><td>unit_cost</td><td></td></tr><tr><td>101</td><td>4.00</td><td>2.00</td><td rowspan="2">{dem1 → prod1, ptable1}</td></tr><tr><td>102</td><td>6.00</td><td>3.00</td></tr><tr><td>103</td><td>8.00</td><td>4.00</td><td rowspan="2">{dem2 → prod2, ptable1}</td></tr><tr><td>104</td><td>10.00</td><td>5.00</td></tr><tr><td>105</td><td>12.00</td><td>6.00</td><td rowspan="2">ptable2</td></tr><tr><td>106</td><td>14.00</td><td>7.00</td></tr></table>

inputs to outputs, even when they differ on underlying assumptions and mapping functions. In graphical approaches, graphs represent the interconnection of models to form composite models. Models are viewed as nodes or edges of a graph. Graphical representations with the notable exception of Basu and Blanning (1998) are typically weak in representing domain knowledge such as model preconditions or assumptions. In knowledge-based approaches, models are represented as components of a knowledge base and various reasoning mechanisms are used to construct composite models. Knowledge-based approaches are capable of representing model preconditions, model assumptions, and specifications pertaining to model input and output. In script-based approaches, model composition is achieved via predefined scripts. These scripts specify the sequence of model executions and data-formatting requirements.

The model composition process can range from being highly automated, as in the case of knowledgebased approaches, to being low on automation, as in the case of script-based approaches. The levels of automation in the case of relational approaches and some graph-based approaches (Basu and Blanning 1994, 1998) are at medium levels. In Table 6, Automation denotes the level of automation associated with various approaches.

Controls guide model search and execution. They can be implicit or explicit (Mookerjee and Chaturvedi 1993). Controls in Table 6 specifies the type of control associated with various approaches. In the case of implicit controls, the domain knowledge (i.e., meta data pertaining to models, data, and solvers) is tightly coupled to the control knowledge or procedure needed for model composition. Explicit controls provide a “clean” separation between domain knowledge and control knowledge. The benefits of explicit controls are as follows. First, domain knowledge can easily be changed without affecting control knowledge or procedure, or vice versa. Second, domain knowledge can be partitioned into overlapping subsets based on user needs. These partitions, just like database views, can provide users exposure to a limited number of model and data resources. Thus, partitions have the potential to reduce the computational time involved in searching the domain knowledge for generating a composite model. The partitions can also provide DSS security and facilitate the distribution of domain knowledge in a distributed DSS environment. Note that controls are not applicable when composite models are specified manually by a user.

Table 6 Comparison of Notable Approaches on Model Composition

<table><tr><td>Paper</td><td>Type</td><td>Controls</td><td>Automation</td><td>Integrating Partial Solutions</td><td>Implementation</td><td>Comments</td></tr><tr><td>Bhargava et al. 1997</td><td>Script-Based</td><td>Not applicable</td><td>Low</td><td>Not addressed. Need to write scripts for every modeling situation.</td><td>Decision Net infrastructure has been implemented.</td><td></td></tr><tr><td>Jeusfeld and Bui 1997</td><td>Script-Based</td><td>Information unavailable</td><td>Low</td><td>Not addressed. Need to write scripts for every modeling situation.</td><td>No</td><td>Logical representation scheme specific to HTTP protocol.</td></tr><tr><td>Blanning 1985</td><td>Relational</td><td>Explicit</td><td>Medium</td><td>Not addressed</td><td>No</td><td>Cannot handle modeling assumptions nor can it differentiate between two models with the same attributes while they differ in functional forms. Automation is therefore limited.</td></tr><tr><td>Liang 1988</td><td>Graphical (augmented by knowledge-based approach)</td><td>Explicit</td><td>High</td><td>Not addressed</td><td>Yes</td><td>Simple implementation in prolog that requires significant changes to enable the use of data from multiple commercial database tables.</td></tr><tr><td>Muhanna 1992, Muhanna and Pick 1994</td><td>Graphical</td><td>Not applicable</td><td>Low</td><td>Not addressed</td><td>Yes</td><td>Implementation does not support the automation of model input data acquisition or support significant automation of the model composition process.</td></tr><tr><td>Basu and Blanning 1994 and 1998</td><td>Graphical</td><td>Explicit</td><td>Medium</td><td>Not addressed. May be possible by augmenting metagraphs with independent procedures.</td><td>No</td><td>Procedures for automating data acquisition, integrating partial solutions, or processing query not part of metagraph specifications.</td></tr><tr><td>Dutta and Basu 1984</td><td>Knowledge-Based</td><td>Implicit</td><td>High</td><td>Not addressed</td><td>No</td><td>Uses first-order logic.</td></tr><tr><td>Shaw et al. 1988</td><td>Knowledge-Based</td><td>Implicit</td><td>High</td><td>Not addressed</td><td>No</td><td>Uses Machine learning.</td></tr><tr><td>Mookerjee and Chaturvedi 1993</td><td>Knowledge-Based</td><td>Explicit</td><td>High</td><td>Not addressed</td><td>No</td><td>Uses blackboard control architecture.</td></tr><tr><td>Holocher et al. 1997</td><td>Knowledge-Based</td><td>Information unavailable</td><td>High</td><td>Not addressed</td><td>Yes</td><td>Limited to Structured models. Weak on modeling assumptions.</td></tr><tr><td>Ba et al. 1997</td><td>Knowledge-Based</td><td>Implicit</td><td>High</td><td>Not Addressed</td><td>Yes</td><td>Implementation cannot support models and data that are implemented or stored on a variety of platforms.</td></tr><tr><td>Current Approach</td><td>Knowledge-Based</td><td>Explicit</td><td>High</td><td>Addressed</td><td>Yes</td><td></td></tr></table>

In Table 6, Implementation indicates whether an approach has been implemented. There are many approaches that are purely at the conceptual level and those that are validated by partial or complete implementations. Although the ideas presented in approaches at the conceptual level are theoretically interesting, there are always some unanswered questions on the feasibility of implementing those ideas. Integrating partial solutions in Table 6 denotes whether the problem of integrating partial solutions from multiple sources is addressed by an approach. Additional comments pertaining to various approaches are presented under Comments in Table 6.

As seen from Table 6, none of the approaches other than the current approach addresses the issue of integrating partial solutions from multiple sources to provide solutions to a query. One notable graphical approach based on metagraphs (Basu and Blanning 1994, 1998), perhaps could be extended to support integration of data from multiple sources, as well as aid in data acquisition. The metagraph approach primarily provides the means to capture dependencies among models and data. However, procedures needed to automate data acquisition from databases, process queries, and combine partial solutions are not part of metagraph specifications. Automation during model composition may be limited in the metagraph approach. This is due to the fact that conditional metagraphs (metagraphs that incorporate assumptions) do not use negated propositions. Thus, manual reasoning is used to remove any inconsistencies that arise during model composition (Basu and Blanning 1998). This contrasts with our approach, where inconsistencies are automatically avoided during model composition. Our approach is dynamic, where the model composition process is interleaved with the model execution process. This contrasts with static approaches, such as the metagraph approach, where all possible composite models are generated first and then a routine is used to select the most appropriate composite model for a given query. Our approach is one of the few that have been validated by an implementation.

This paper contains seven sections and two appendices, A and B. Section 2 contains definitions that are used to describe basic concepts in this paper. Representations of databases and models in the DSS are presented in §3. Section 4 presents model composition using filter spaces. The control procedure used for model composition and execution is presented in §5. Brief details of our implementation are presented in §6. Section 7 summarizes the contributions of this paper. Appendix A contains the definition of the join operator used in this paper, while proofs of various propositions are presented in Appendix B.

## 2. Basic Definitions

Domain knowledge about models and data is used in selecting the “right” models and databases during model composition and execution. This knowledge can be represented in DSS using a meta language. An inference mechanism operates on the domain knowledge to generate composite models in response to user queries. The DSS meta language, like any first order language (FOL) (Chang and Lee 1973) consist of predicates, constants, variables, etc. Definition 1 provides a formal definition of the DSS meta language.

Definition 1. The DSS meta language is given by $L = ( A , W )$ where A is an alphabet of symbols and W is a set of well-formed formulae (wff) constructed using symbols of A. The symbols of A consist of variables, constants, predicates, logical constants, and punctuation signs as follows:

Variables (V): finitely many variables such as pid, price, quantity, . . . ,

Constants (C): finitely many constants such as 101, 10, “pid”, nut, bolt, . . . . ,

Predicates (U): finitely many symbols such as LE, LT, GE, GT, OR, . . .

Punctuation Signs: (,), , , . . . ,

Logical Constants: <sup>#</sup> (and), <sup>3</sup> (or), ⇔ (equivalent), ⇒(implies), <sub>C</sub>(not)

A wff in W is constructed using logical constants and terms from A. A term consists of individual constants from C and individual variables from V. A predicate symbol followed by terms is also a term. A list of terms is also a term. A wff is defined recursively similar to Chang and Lee (1973) as follows:

(1) If U is a n-ary predicate of A, and $ { \alpha } _ { l } , \ldots ,  { \alpha } _ { n }$ are terms, then $\Phi ( \alpha _ { l } , \dots , \alpha _ { n } )$ is a wff.

(2) If U<sub>1</sub> and $\Phi _ { 2 }$ are wff, then $( \Phi _ { 1 } \wedge \Phi _ { 2 } ) , ( \Phi _ { 1 } \vee \Phi _ { 2 } )$ $( \Phi _ { 1 } \Rightarrow \Phi _ { 2 } ) , ( \Phi _ { 1 } \Leftrightarrow \Phi _ { 2 } )$ and $\lnot \Phi _ { 1 }$ are also wffs.

(3) If x is a variable in V, then ∀(x) and ∃(x) are also wffs, where ∀ and ∃ are universal and existential quantifiers, respectively.

A class of wff that is at the core of the domain knowledge representation scheme is the filter clause. A filter clause can be used to represent preconditions of models or to specify ranges of values associated with data.

Definition 2. A filter clause is defined as follows: Type 1. A predicate of 2 places, $\Phi ( \alpha _ { 1 } , \ \alpha _ { 2 } )$ is a filter clause when $\Phi \in \{ L T ( < ) , L E ( \leq ) , G T ( > ) , G E ( \geq ) \}$ , and $\alpha _ { 1 } , \alpha _ { 2 }$ are nonpredicate terms as follows: (a) $\alpha _ { 1 } , \alpha _ { 2 } \in$ V represent variables; (b) $\alpha _ { 1 } \in V ,$ and $\alpha _ { 2 } \in C$ is a constant such that MIN\_RANGE $\leq \alpha _ { 2 } ^ { 1 } \leq M A X$ \_RANGE, where MIN\_RANGE and MAX\_RANGE are low and high values, respectively, that are never taken by $\alpha _ { 1 }$ Type 2. A predicate of n places, $\Phi ( \alpha _ { 1 } , \ldots , \alpha _ { n } )$ is a filter clause when U - OR (disjunction), $\alpha _ { 1 } , \ldots , \alpha _ { n }$ are predicates of Type 1, and $n > 0 . ^ { 1 }$

Examples of filter clauses are as follows:

Type 1a. GE(price, unit\_cost) represents price  unit\_cost, where variables price, unit\_cost  V.

Type 1b. GE(pid, 101) represents pid  101, where variable pid  V and constant $1 0 1 \in C .$

Type 2. OR(GE(pid, 101), LE(pid, 999)) represents (pid $\geq 1 0 1 ) \vee ( p i d \leq 9 9 9 )$

By limiting the filter clauses to contain only LT, LE, GT, and GE, it becomes easier to deduce nonbinding clauses (see Definition 5).

Definition 3. A filter list is a set of filter clauses in the conjunctive normal form (Rich and Knight 1991). A filter list represents the conjunction of filter clauses when it is represented in the conjunctive normal form (also known as clausal form). An example of a filter list is:

[OR(GE(pid, 101), LE(pid, 999)), GE(price, 10.0), LE(quantity, 100)], which represents the expression: $( ( p i d \ge 1 0 1 ) \lor$ $( p i d \leq 9 9 9 ) ) \land ( p r i c e \geq 1 0 . 0 ) \land ( q u a n t i t y \leq 1 0 O )$ . An ndimensional space called the filter space can be associated with a filter list as follows.

Definition 4. Let the filter list $\pi = \{ \Phi _ { k } ( X _ { \pi k } ) \} _ { k = 1 , \dots , m } ,$ where $X _ { \pi k }$ is the set of variables that participate in the filter clause $\Phi _ { k } ( . ) , X _ { \pi } = \cup _ { k = 1 , \ldots , m } X _ { \pi k } = \{ x _ { l } , \ldots x _ { n } \} \subseteq V$ is the set of unique variables that participate in $\pi ,$ and the total dimensions $n = \mid X _ { \pi } \mid$ . The filter space of p is given by $F S _ { \pi } = \{ c \mid c \in C ^ { n } \land$ substitution $\theta = \{ c _ { l } / x _ { l } , \ldots ,$ $c _ { n } / x _ { n } \} \wedge ( \wedge _ { k = 1 , . . . , m } \Phi _ { k } ( X _ { \pi k } ) \ : \Theta ) \}$

The filter space of p is thus a collection of n-tuples. The tuple $( c _ { l } , \ldots , c _ { n } )$ is contained in the filter space of p if all filter clauses of p are evaluated to be true when the variables in p are instantiated by the substitution $\theta ~ = ~ \{ c _ { l } / x _ { l } , \ldots , ~ c _ { n } / x _ { n } \}$ . Each dimension of the filter space is defined by a variable in $X _ { \pi } .$ The total dimensions of the filter space (i.e., n) is therefore equal to the cardinality of $X _ { \pi } .$ The definition of a filter space does not preclude it from being unbounded.

For example, consider $\pi ~ = ~ \mathit { l G E } ( p i d , ~ \mathit { 1 0 1 } )$ , LE(pid, 103), GE(price, 10.0), LE(price, 20.0)]. The filter space associated with p is a two-dimensional space with dimensions price and pid. This space is illustrated in Figure 1. Tuples involving all combinations of (pid, price) values that enable all filter clauses in p to be true are enclosed in the filter space of p.

We explore key properties of filter spaces next.

Property 1. Given a filter clause $\varPhi ( \alpha _ { l } , \ldots , \alpha _ { m } )$ of Type 2 that has total dimensions $n ,$ where $\alpha _ { l } , \ldots , \alpha _ { m }$ are predicates of Type 1, $\varPhi = O R$ (disjunction) and n represents the number of unique variables in the argument set $\{ \alpha _ { l } , \ldots ,$ $\alpha _ { m } \}$ . The filter space of U is given by $F S _ { \Phi } = \cup _ { k = 1 , \dots , m } F S _ { \alpha k } ,$ $F S _ { \Phi } \in C ^ { n }$ , where $F S _ { \alpha k } \in C ^ { n }$ is the filter space associated with $\alpha _ { k }$ in n dimensions.

According to Property 1, the filter space associated with an OR clause is the union of the filter spaces associated with the arguments of the OR clause. The arguments of the OR clause can only be Type 1 clauses since filter lists by definition are required to be in the clausal form. Therefore, nesting of OR clauses will not occur in the filter list. The union can only be defined when there is dimensional consistency; $\mathrm { i . e . , }$ all dimensions of the filter spaces of the arguments are the same. This is similar to the notion of union-compatibility requirement in relational database theory (Date 1986). If all dimensions of a particular argument $\alpha _ { k }$ are not the same as those of the argument set $\{ \alpha _ { l } , \ldots , \alpha _ { m } \} _ { \scriptscriptstyle { A } }$ , dummy clauses of the form LT(x, MAX\_RANGE) or GT(x, MIN\_RANGE) for each variable x not present in $\alpha _ { k }$ but present in $\{ \alpha _ { l } , \ldots , \alpha _ { m } \}$ can be added, without introducing any inconsistencies.

Figure 1 Filter Space (FS) Indicated by the Shaded Region Defined by p - [GE (pid, 101), LE (pid, 103), GE (price, 10.0), LE (price, 20.0)]  
![](/api/attachments/Q7858FAK/fulltext/images/ee3611899c57650174e063a9605d510f9992fc8e4b84b7004120734dc1ddad2c.jpg)

The following example illustrates Property 1. Consider the clause: OR(LT(pid, 106), GT(price, 10)). The dimension of this clause is 2 (i.e., pid and price). While generating the filter space for the first argument, GT(price, MIN\_RANGE) could be added to a filter list containing LT(pid, 106). Similarly, while generating the filter space for the second argument, LT(pid, MAX\_RANGE) could be added to a filter list containing GT(price, 10). The filter space of the OR clause is then the union of filter spaces defined by [LT(pid, 106), GT(price, MIN\_RANGE)] and [GT(price, 10), LT(pid, MAX\_RANGE)].

Property 2. Given a filter list $\pi = \{ \phi _ { k } ( X _ { \pi k } ) \} _ { k = 1 , \dots , m }$ with total dimensions $n , F S _ { \pi } = \cap _ { k = 1 , \dots , m } F _ { \Phi k }$ where $F S _ { \pi } \in$ $C ^ { n } ,$ , and $F S _ { \Phi k } \in C ^ { n }$ are the filter spaces of p and $\Phi _ { k } \left( X _ { \pi k } \right)$ respectively, in n dimensions.

Thus, the filter space of a filter list in n dimensions is the intersection of the filter spaces of its member clauses in n dimensions, where n is the total number of unique variables in the filter list. Since the filter list is in the clausal form, i.e., conjunction of disjuncts, all clauses have to be true. Therefore the intersection of filter spaces of clauses will determine the filter space of the filter list. A contradiction involving member clauses is detected when the filter space of a nonempty filter list is a null space. Just like union operation, intersection also requires union-compatibility. Therefore dimensional consistency is required for the filter spaces of all clauses and this could be addressed by following the same procedure that was discussed under Property 1.

The following example illustrates Property 2. Consider the filter list:

[LT(pid, 106), GT(price, 10)]. The total dimension of the filter list is 2 (i.e., pid and price). Adding the dummy clause GT (price, MIN\_RANGE) to a list containing just the first clause could generate the filter space of the first clause of the example filter list in two dimensions. Similarly the filter space of the second clause of the example filter list in two dimensions could be generated by adding the dummy clause LT(pid, MAX\_RANGE) to a filter list containing just the second clause. The filter space of the example filter list is then the intersection of filter spaces defined by [LT(pid, 106), GT(price, MIN\_RANGE)] and [GT(price, 10), LT(pid, MAX\_RANGE)]. This is equivalent to the filter list of the single list: [LT(pid, 106), GT(price, MIN\_RANGE), GT(price, 10), LT(pid, MAX\_RANGE)]. Note that dummy clauses can always be dropped to obtain the list: [LT(pid, 106), GT(price, 10)], which is then the original example list.

In the list: [LT(pid, 106), GT(price, MIN\_RANGE), GT(price, 10), LT(pid, MAX\_RANGE)], dummy clauses are nonbinding since stronger binding clauses exist in the list. The following definition formalizes the notion of nonbinding clauses.

Definition 5. Consider any two filter clauses $\Phi _ { 1 } ( X _ { \pi 1 } )$ and $\Phi _ { 2 } ( X _ { \pi 2 } )$ in the filter list p such that $X _ { \pi 1 } =$ $X _ { \pi 2 } . \Phi _ { 1 } ( X _ { \pi 1 } )$ is a non-binding clause in p with respect to $\Phi _ { 2 } ( X _ { \pi 2 } )$ if and only if $F S _ { \Phi 2 ( X \pi 2 ) } \subset F S _ { \Phi 1 ( X \pi 1 ) } ,$ where $F S _ { \Phi 1 ( X \pi 1 ) }$ and $F S _ { \Phi 2 ( X \pi 2 ) }$ are filter spaces in n dimensions of clauses $\Phi _ { 1 } ( X _ { \pi 1 } )$ and $\Phi _ { 2 } ( X _ { \pi 2 } )$ , respectively, and n is the total number of unique variables in p.

Filter spaces can be used to determine nonbinding filter clauses, which can then be removed from a filter list without affecting its filter space. According to Definition 5, if two clauses 1 and 2 in a filter list have the same variables, then clause 1 is nonbinding with respect to clause 2 if and only if the filter space of clause 2 is fully contained in the filter space of clause 1. Again to maintain dimensional consistency, the filter spaces of the filter clauses are constructed in n dimensions where n is the number of variables in the filter list. Consider the filter list [GT(pid, 106), LT(price, 10), LT(price, 5)]. It can be clearly seen that LT(price, 10) is nonbinding since a tighter binding clause LT(price, 5)

exists in the filter list. Nonbinding clauses can be easily identified when LT or GT clauses are used.

As mentioned earlier, the basic purpose of the DSS meta language is to represent domain knowledge of models and data in the DSS in order to facilitate model composition and execution. Database tables, as well as model inputs and outputs that are relational tables, could be described by key-value set definitions.

Definition 6. A key-value set definition (j) of a relation consists of four parts: $\kappa - \nu = \langle \eta , \kappa , \nu , \pi \rangle ,$ , where g is an identifier string of the key-value set definition, $\kappa = \{ k _ { l } , \textrm { . . . } , k _ { k } \} , k _ { l } , \textrm { . . . } , k _ { k } \in C$ are strings that represent the names of attributes participating in the primary key of the relation, $\nu = \{ \nu _ { l } , \dots , \nu _ { m } \} , \nu _ { l } , \dots , \nu _ { m } \in C$ are strings that represent the names of the nonkey $( \mathrm { i . e . }$ value) attributes in the relation $( \nu _ { l } , \dots , \nu _ { m } \notin$ j) and p is the filter list containing binding clauses that define the filter space of the relation.

Key-value set definitions specify relational data that is used in domain knowledge representations. In addition to its identifier string, a key-value set consists of a set of strings that represent key attributes of a relation, a set of strings that represent nonkey attributes of a relation and a filter list that specifies the filter space to describe the extent of a relation.

Definition 7. The filter list p of a key-value set definition $\kappa - \nu = \langle \eta , \kappa , \nu , \pi \rangle$ has the maximum dimensional property when $X _ { \pi } ,$ the set of unique variables in p is given by $f \colon \kappa \cup \nu  X _ { \pi } ,$ where f is a one-to-one function that maps an attribute name string in j -  to a variable in $X _ { \pi } .$

The maximum dimensional property of a filter list of a key-value set of a relation requires that it contain clauses such that all variables corresponding to the key and nonkey attributes of a relation are present. This property ensures that the dimensions of the filter space of the filter list of a relation map to the attributes of the relation. An example of a key-value set definition that represents the relational table of Table 1 is as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\kappa - \nu = \langle 'product1', \{pid\}, \{pname, price\}, [GE(pid, 101), LE(pid, 104), GT(pname, MIN_RANGE), LT(pname, MAX_RANGE), GT(price, MIN_RANGE), LT(price, MAX_RANGE)] \rangle$
</div>

In the above example, the key attribute is pid, and value attributes (i.e., nonkey attributes) include pname and price. The filter clauses specify the range of values associated with the key and the value attributes of ptable1. Note that the filter list contains dummy clauses involving variables price and pname to facilitate the maximum dimensional property. These dummy clauses implicitly indicate that price and pname are unconstrained.

## 3. Database and Model Representation

Database and model templates represent domain knowledge on databases and models respectively. A control procedure operates on these templates for generating and executing composite models.

Definition 8. A database template is an ordered pair $D B = \left. \mathbf { \kappa } \cdot \mathbf { \sigma } \right. ,$ Database, where $\operatorname { \kappa } - \nu = \langle \eta , \kappa , \nu , \pi \rangle$ is the key-value set definition of the database with filter list p having the maximum dimensional property and corresponding filter space $F S _ { \pi } \neq \varnothing ;$ Database is a string that encodes the database name, path, and access method.

The database template maps a key-value set definition representing relational data to a database table that is accessible to the DSS. The maximum dimensional property of the filter list facilitates model composition as described later in §4. The filter space of the filter list describing the database is nonnull, implying that there are no contradictions involving the clauses in the filter list. The following example describes the database template of ptable1 (see Table 1).

```txt
DB = ⟨ ‘product1’,
{pid},
{pname, price},
[GE(pid, 101), LE(pid, 104), GT(pname, MIN_RANGE),
LT(pname, MAX_RANGE), GT(price, MIN_RANGE), LT(price,
MAX_RANGE)]⟩, odbc::acad::ptable1⟩.
```

The key-value set definition identified by product1 defines the contents of the database. The string, odbc::acad::ptable1, identifies the access method as ODBC (Umar 1997), the database source as acad, and the relational table as ptable1.

Model templates are more complex than database templates. Models accept a list of relations as input and generate a list of relations as output (a singleton value is a special case of a relation). Key-value set definitions representing input and output relations incorporate model preconditions or assumptions. There are three categories of model preconditions or assumptions: (1) those related to a single model input relation, (2) those related to multiple model input relations, and (3) those not related to any model input. Model templates handle all the three types.

Definition 9. A model template M is composed of six parts, M - ModelName, Input, Output, Assumption, Filter, Source, where

ModelName is a string that identifies the model;

Input $= \{ \kappa - \nu _ { j } ^ { i } \} _ { j = 1 , \dots , p }$ is the set of key-value set definitions $\kappa - \nu _ { j } ^ { i } = \langle \eta _ { j } ^ { i } , \dot { \kappa } _ { j } ^ { i } , \nu _ { j } ^ { i } , \pi _ { j } ^ { i } \rangle$ representing p model input relational data, where

(1) $\pi _ { j } ^ { i } , j = 1 , \ldots , p ,$ has the maximum dimensional property,

${ \bf ( 2 ) } \ \lnot ( \exists \Phi _ { 1 } ( x ) \in \pi _ { i } ^ { i } \ \exists \Phi _ { 2 } ( x ) \in \pi _ { k j \ne k } ^ { i } \ ( \Phi _ { 1 } ( x ) \ne \Phi _ { 2 } ( x ) ) )$ where $\Phi _ { 1 } ( x )$ and $\Phi _ { 2 } ( x )$ are clauses of Type 1b that have the same predicate symbols and variable $x ,$

(3) the filter space associated with $\pi _ { j } ^ { i } , F S _ { \pi j } ^ { i } \neq \emptyset , j =$ $1 , \ldots , p ;$

$O u t p u t = \{ \kappa - \pmb { \nu } _ { k } ^ { o } \} _ { k = 1 , \ldots , q }$ is the set of key-value set definitions $\kappa - \nu _ { k } ^ { o } = \left. \eta _ { k } ^ { o } , \kappa _ { k } ^ { o } , \nu _ { k } ^ { o } , \pi _ { k } ^ { o } \right.$ representing $q$ model output relational data. The filter list $\pi _ { k } ^ { o }$ has

(1) clauses to support the maximum dimensional property involving variables associated with $\kappa _ { k } ^ { o }$ and $\nu _ { k } ^ { o } ,$

(2) additional binding clauses from $\cup _ { j = 1 , \dots , p } \pi _ { j } ^ { i }$ and Filter such that $\pi _ { k } ^ { o } \supset \{ \cup _ { j = 1 , \ldots , p } \pi _ { j } ^ { i } \} \cup F i l t e r ,$ and

(3) the filter space associated with <sup>o</sup>p , $F S _ { \pi k } ^ { o } \neq \varnothing ;$ Assumption is a set of predicate clauses representing model assumptions that are not related to model inputs;

Filter is the set of filter clauses representing constraints among model inputs and can only contain clauses of Type 1a and clauses of Type 2 that are in turn composed of clauses of Type 1a. The filter space associated with Filter, $F S _ { F i l t e r } \neq \emptyset ,$ when $\mid F i l t e r \mid \ne 0 ;$

Source is a string that encodes the physical location and access method of the model executable.

A model template includes the model identifier, followed by model input, output, assumptions, and model access information. The filter list of the keyvalue set definition of a model input relation incorporates intra-input constraint clauses representing model preconditions related only to a single model input relation. As per Definition 9, this list does not contain any nonbinding clauses and has the maximumdimensional property. Furthermore, two model inputs cannot have two different filter clauses of Type 1b involving the same predicate symbol and variable. Thus, if the filter list associated with input1 of a model has a clause GE(pid, 101), then input2 of the model cannot have a Type 1b clause involving predicate symbol GE and variable pid that is different from GE(pid, 101), i.e., GE(pid, 105). This requirement, while needed to maintain consistency across model inputs, may impose restrictions on the type of models being represented. The filter space associated with the filter list of the keyvalue set of a model input relation is required to be nonnull so that there are no contradictions involving filter clauses of the model input relation.

The filter list of the key-set definition of a model output relation, in addition to containing clauses involving variables related to model output, also contains binding filter clauses from all model inputs as well as binding clauses from Filter, where Filter contains constraints between two input relations $( \mathrm { i . e . , }$ interinput constraints). The requirement that the filter space associated with a model output relation be nonnull is needed to ensure that there are no contradictions involving clauses in the filter list of the model output relation. By limiting Filter to having Type1a clauses and Type 2 clauses containing Type1a clauses, filter space comparisons that are needed for model selection can be easily facilitated (see Definition 12). The filter spaces of model outputs depend on the interinput as well as on the intrainput constraint clauses. This dependence is needed to enforce model preconditions while selecting models. Furthermore, intrainput as well as interinput constraint clauses facilitate the acquisition of model input data relations during model execution. Thus, filter clauses not only support inference during model selection but also facilitate model input data acquisition during model execution. Model assumptions that are not related to model inputs are specified in Assumption. Clauses in Assumption can be represented as wff, thus, automated reasoning is possible during model selection. The location as well as the access method of a model is encoded as a string

# that is represented by Source. The following example illustrates the model template of dem1 (see Table 3).

M - ‘dem1’,

{‘priceinput’, {pid}, {price}, [GE(pid, 101), LE(pid,102),

GT(price, MIN\_RANGE), LT(price, MAX\_RANGE)]},

{‘forecast\_demand’, {pid}, {quantity}, [GE(pid, 101), LE(pid, 102), GT(quantity, MIN\_RANGE),

LT(quantity, MAX\_RANGE), GT(price, MIN\_RANGE), LT(price, MAX\_RANGE)]},

model\_type(‘linear regression model’),

‘corba::134.126.40.232::d’

The first argument of the model template is the string dem1 that identifies the model. The second argument consists of a set containing a single key-value set definition of a model-input relation with pid and price as the two attributes. The filter clauses of the model input indicate that this model can only be used to forecast demands of products with pid in the range 101–102. The third argument identified by forecast\_demand represents the key-value set definition of a single model output relation that contains attributes pid and quantity. The fourth argument is a list that contains a single model assumption clause that is not related to any input. The fifth argument representing interinput constraints is an empty list. The last argument gives the location of dem1 and the access method to execute the model executable. This argument indicates that dem1 is located at a machine with IP address 134.126.40.232 and is executed using CORBA middleware (Umar 1997) using a default value for the server name.

An interinput constraint is illustrated by the following example. Consider a production model that computes the unit\_cost of items produced for items whose demand is more than its current inventory level. The following model template represents the production model:

[GT(forecast\_demand.quantity, inventory\_level.level)], ‘corba::134.126.40.232::d’

The production model prod3 has two inputs: forecast\_ demand and inventory\_level, while the output is unit\_cost. The interinput constraint clause GT(forecast\_ demand.quantity, inventory\_level.level) specifies that the quantity associated with the input forecast\_demand be greater than level that is associated with the input inventory level, thereby implying that the model is only applicable for products that satisfy the interinput constraint clause. Note that the filter list associated with the model output unit\_cost contains the filter clauses of all model inputs as well as the filter clause representing the interinput constraint. This list also supports the maximum dimensional property with respect to the attributes present in the key and value sets of ‘unit\_cost’.

Data and model templates could be created by a user or by a DSS administrator. The key-value set definitions representing model-input relations are totally independent of existing databases because they merely specify the data needed by a model. Therefore, changes made to the contents of database tables (i.e., addition or deletion of tuples) will not affect model templates. Model and database templates are self-contained and independent of the control procedure. Thus, model and database templates can be changed without affecting the control procedure. Furthermore, small sets containing only those model and database templates that are of interest to a particular user could be created for a DSS user, thereby greatly reducing the computation time for composing models.

Key-value set definitions representing relations pertaining to model outputs and database tables available to a user, constitute the set of data sources for that user.

Definition 10. Let D and X denote the set of keyvalue set definitions of relations associated with database templates and relations associated with outputs of model templates available to a user, respectively. A data source is a key-value set definition $\kappa - \nu \in \Delta \cup \Omega .$

## 4. Model Composition Using Filter Spaces

Model composition entails matching the key-value set definition of the query relation (henceforth referred to simply as a query) to the key-value set definition of a data source relation. If the data source is a model output relation that is generated by a model requiring input, then the model input in turn is posed as a query where the query relation’s key-value set definition has to match other data sources. Matching a query to a data source involves operations such as projection. The projection operation entails projecting a higher dimensional filter space into a lower dimensional space. This is done so as to enable two filter spaces with different dimensions to be compared. The projection operation is defined next.

Definition 11. Let $X _ { \pi i }$ and $X _ { \pi j }$ denote sets of unique variables appearing in filter lists $\pi _ { i }$ and $\pi _ { j } ,$ respectively. A projection of list $\pi _ { j }$ over $\pi _ { i }$ is defined by the function u<sub>Pji</sub>: $\pi _ { j } \to \pi _ { j i }$ as follows:

11.1 Set $\pi _ { j i } = \pi _ { j }$

11.2 Remove all clauses of Type 1b of the following form from $\pi _ { j i \cdot }$

$\Phi ( x , c )$ where $x \notin X _ { \pi i }$ and c - MIN\_RANGE or MAX\_RANGE.

11.3 Replace Type 2 clauses in $\pi _ { j i }$ that has arity - 1 with its remaining Type 1 component clause.

Remove all Type 2 clauses that have arity - 0.

11.4 Remove all nonbinding clauses from $\pi _ { j i } .$

As an example, consider two filter lists:

$\pi _ { i } = { \cal I } G E ( p i d , 1 0 1 ) , L E ( p i d , 1 1 0 ) , L E ( p r i c e , 1 0 ) { \cal I }$ and $\pi _ { j } =$ [GE(pid, 101), LT(pid, 999), GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE), GT(price, MIN\_RANGE), LT(price, MAX\_RANGE), OR(GT(price, 5), LT(unit\_cost, MAX\_RANGE))].

The projection of $\pi _ { j }$ on $\pi _ { i }$ is given by $\phi _ { \pi j i } .$ The projected list is given as follows:

$\pi _ { j i } = I G E ( p i d ,$ 101), LT(pid, 999), GT(price, 5), LT(price, MAX\_RANGE)].

Note that clauses GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE) and LT(unit\_cost, MAX\_RANGE) are eliminated from $\pi _ { j i }$ in Step 11.2. In Step 11.3 the OR clause now with arity $\mathbf { \lambda } \cdot \mathbf { \lambda } = 1$ is replaced by its component clause GT (price, 5). Finally, in Step 11.4, the nonbinding clause GT(price, MIN\_RANGE) is eliminated because the binding clause GT(price, 5) exists. It can be seen that the projected filter list $\pi _ { j i }$ has the same dimensions as the filter list $\pi _ { i } .$ . Therefore the filter spaces can be matched as follows.

Definition 12. Let $\pi _ { i }$ and $\pi _ { j }$ denote two filter lists, and $\pi _ { j i }$ denote the filter list obtained after the projection of $\pi _ { j }$ over $\pi _ { i } .$ Furthermore, let $X _ { \pi i }$ and $X _ { \pi j i }$ denote sets of unique variables appearing in $\pi _ { i }$ and $\pi _ { j i } ,$ respectively, and $F S _ { \pi i }$ and $F S _ { \pi j i }$ denote the filter spaces of $\pi _ { i }$ and $\pi _ { j i } ,$ respectively. The filter list $\pi _ { i }$ is covered in $\pi _ { j }$ iff 12.1 $X _ { \pi i } = X _ { \pi j i } ( \mathrm { i . e . }$ , the dimensions of $\pi _ { j } ,$ after projection, are the same as that of $\pi _ { i } )$ and

12.2 $F S _ { \pi i } \subseteq F S _ { \pi j i }$ (i.e., the filter space of $\pi _ { i }$ is contained in the projected filter space of $\pi _ { j } )$ .

Definition 12 specifies the necessary preconditions for a data source to provide data for a query. Consider the following example where the filter list of a query is $\pi _ { i } = l G E ( p i d , 1 0 1 )$ , LE(pid, 102)], and the filter list of a data source is $\pi _ { j } ~ = ~ \ l G E ( p i d , ~ \ l O 1 ) _ { . }$ , LE(pid, 999), GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE), GT(price, 0), LT(price, MAX\_RANGE)]. On projecting $\pi _ { j }$ over $\pi _ { i } ,$ the projected filter list obtained is $\pi _ { j i } = I G E ( p i d ,$ 101), LE(pid, 999)]. It can be easily seen that $X _ { \pi i } = X _ { \pi j i }$ and $F S _ { \pi i } \subseteq F S _ { \pi j i } .$ Therefore $\pi _ { i }$ is covered in $\pi _ { j } .$ Corresponding filter spaces are illustrated in Figure 2. Note that the filter spaces are one-dimensional spaces.

Now consider the example where the filter list of a query is $\pi _ { i } = [ G E ( p i d , 1 0 1 ) , L E ( p i d , 1 0 9 ) , G E ( p r i c e , 1 0 . 0 ) ]$ LE(price, 20.0)], and the filter list of a data source is $\pi _ { j }$ - [GE(pid, 101), LE(pid, 102), GT(unit\_cost, MIN\_RANGE), LT(unit\_cost, MAX\_RANGE)]. On projecting $\pi _ { j }$ over $\pi _ { i } ,$ , the resultant filter list obtained is $\pi _ { j i }$ - [GE(pid, 101), LE(pid, 102)]. In this case, $X _ { \pi i } \neq X _ { \pi j i }$ (i.e., dimensions do not match), therefore the filter list p is not covered in $\pi _ { j } .$

We have the following propositions on data sources.

Proposition 1. A single data source $\kappa - \nu ^ { s } = \langle \eta ^ { s } , \kappa ^ { s } ,$ $\nu ^ { s } , \pi ^ { s } \rangle$ can provide data for a query defined by the key-value set definition $\kappa - \nu ^ { q } \ = \ \langle \eta ^ { q } , \ \kappa ^ { q } , \ \nu ^ { q } , \ \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset$ , when the following conditions are true: $( 1 ) \kappa ^ { q } =$ $\kappa ^ { s } , ( 2 ) \nu ^ { q } \subseteq \nu ^ { s }$ and $( 3 ) \pi ^ { q }$ is covered in $\pi ^ { s }$ (See proof in Appendix B.)

Figure 2 Filter Spaces Corresponding to $\pi _ { j } = { \mathit { l G E } }$ (pid, 101), LE (pid, 102)] and $\pi _ { j j } = ~ { \it I G E }$ (pid, 101), LE (pid, 999)]

<table><tr><td>101</td><td>102</td><td>999</td></tr><tr><td></td><td></td><td>pid →</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\kappa - \nu^{s} = \langle 'product1', \{pid\}, \{pname, price\}, [GE(pid, 101), LE(pid, 104), GE(pname, MIN_RANGE), LT(pname, MAX_RANGE), GE(price, MIN_RANGE), LT(price, MAX_RANGE)] \rangle,$
</div>

According to Proposition 1, a single data source can provide all the data needed for a query when the following conditions hold: (1) the set of key attributes of the query matches with the set of key attributes of the data source, (2) the set of value attributes of the query is a subset of the set of value attributes of the data source, and (3) the filter list of the query is covered in the filter list of the data source. To illustrate this, consider a query that requires the prices of product with pid - 101 and 102 and a data source given by the following key-value set definition:

The query can be represented by the following keyvalue set definition:

$$
\begin{array}{l} \kappa - \nu^ {q} = \langle ` q u e r y 3 ^ {\prime}, \\ \quad \{p i d \}, \\ \quad \{p r i c e \}, \\ \quad [ G E (p i d,   1 0 1),   L E (p i d,   1 0 2) ] \rangle . \end{array}
$$

It can be seen that the key attribute of the query $( \mathrm { i . e . , }$ pid) matches with the key attribute of the data source, the value of attribute of the query, namely price, is contained in the value set of the data source, and the filter list of the query is covered in the filter list of the data source. Therefore, the single data source ‘product1’ can provide all the data for the query.

The significance of the maximum-dimensional property (Definition 7) is explained next. Consider a query that requires pid and pname values for price - 10. The filter list of this query is $\pi ^ { q } = { \cal I } G E ( p r i c e , 1 0 ) { \cal I } .$ . Consider the database table product(pid, pname, price), where $p i d ,$ pname, and price can take unrestricted values from their respective domains. If we follow the convention of not including an attribute in the filter list if its value is unrestricted in the domain, then the filter list for product will be given by $\pi _ { j } = [ ]$ , i.e., an empty list. In this case, product, a valid data source, will not be selected for obtaining data for the query since, $X _ { \pi j q } \ne X _ { \pi q } ,$ i.e., the dimensions of the filter list of the query are not the same as the dimensions of the filter list of the database template after projection over $\pi ^ { q } .$ Thus, dummy clauses involving MIN\_RANGE and MAX\_RANGE are added for attributes that are unconstrained to the filter list, so as to satisfy the maximum-dimensional property. The filter list for product is then given by $\pi _ { j } ~ =$ [GT(pid, MIN\_RANGE), LT(pid, MAX\_RANGE), GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE), GT(price, MIN\_RANGE), LT(price, MAX\_RANGE)].

Proposition 2. A minimal set of data sources ${ \boldsymbol { S } } \ =$ $\{ \kappa - \nu _ { j } ^ { s } \} _ { j = 1 , \dots , m } ,$ where $\kappa - \nu _ { j } ^ { s } = \eta _ { j } ^ { s } , \kappa _ { j } ^ { s } , \nu _ { j } ^ { s } , \pi _ { j } ^ { s } \rangle ,$ can provide , data for a query defined by key-value set $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } ,$ $\nu ^ { \boldsymbol { \theta } } , \pi ^ { \boldsymbol { q } } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset ,$ , when the following conditions are true: (1) $\kappa ^ { q } = \kappa _ { j } ^ { s } , j = 1 , \ldots , m , ( 2 ) \iota ^ { q } \subseteq \nu _ { j } ^ { s } , j$ $\ = \ 1 , \ldots , m , ( 3 ) \ X _ { \pi q } = \ X _ { \pi j q } , j = 1 , \ldots , m $ , where $X _ { \pi q }$ and $X _ { \pi j q }$ are the set of unique variables appearing in $\pi ^ { q }$ and $\pi _ { j q } ^ { s } ,$ respectively, $\pi _ { j q } ^ { s }$ is obtained by projecting over p<sup>q</sup>, (4)  <sup>s</sup>  p <sub>j</sub> $F S _ { \pi } ^ { q } \subseteq \cup _ { j = 1 , \dots , m } F S _ { \pi j q }$ where $F S _ { \pi j q }$ denotes the filter space associated with $\pi _ { j q } ^ { s } ,$ , and (5) no subset of S satisfies (4). (See proof in Appendix B.)

When a single data source by itself cannot provide all the data needed for a query, data from multiple sources can be combined to obtain the data needed for the query. Proposition 2 pertains to the case when data from multiple sources are combined using the union operator. According to Proposition 2, a minimal set of data sources can provide data for a query when the following conditions hold: (1) the key attributes of the query match with the key attributes of all data sources in the set, (2) the set of value attributes of the query is a subset of the value attribute set of all data sources in the set, (3) the dimensions of the filter list of all data sources after projection on the filter list of the query match with the dimensions of the filter list of the query, (4) the filter space of the query is a subset of the union of filter spaces of the data sources (after necessary projection), and (5) no subset of the set of data sources satisfies condition (4). This is demonstrated by the following example.

Consider a query that requires pid and unit\_cost of products with pid in the range 103–106 and unit\_cost in the range 4–10. The key-value set definition of the query is j<sup>q</sup> - ‘query4’, {pid}, {unit\_cost}, [GT(pid, 102), LE(pid, 106), GE(unit\_cost, 4), LE(unit\_cost, 10)]. The minimal set of data sources that can provide all the data for the query is given by

S - {‘prod2\_unit\_cost1’, {pid}, {unit\_cost}, [GT(pid, 102), LE(pid, 104), GT(unit\_cost, MIN\_RANGE), LT(unit\_cost, MAX\_RANGE), GT(quantity, MIN\_RANGE), LT(quantity, MAX\_RANGE)], ‘product2’, {pid}, {pname, price, unit\_cost}, [GT(pid, 104), LE(pid, 106),

GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE), GT(price, MIN\_RANGE), LT(price, MAX\_RANGE), GT(unit\_cost, MIN\_RANGE), LT(unit\_cost, MAX\_RANGE)]}.

Set S consists of two data sources identified by prod2\_unit\_cost1 and product2, where prod2\_unit\_cost1 refers to the output of model prod2 (see Table 3) and product2 refers to the data stored in ptable2 (Table 2). It can be seen that the key attributes of the query match with the key attributes of the data sources, the value attributes of the query are contained in the value set of the data sources, and on projecting the filter lists of the data sources in S over the query filter list, the dimensions (i.e., pid and unit\_cost) are the same as that of the query filter list. The contribution made by the first data source is given by the following filter list: [GT(pid, 102), LE(pid, 104), GE(unit\_cost, 4), LT(unit\_ cost, 10)]. The remaining filter space of the query after subtracting the contributions made by the first data source corresponds to the following list: [GT(pid, 104), LE(pid, 106), GE(unit\_cost, 4), LE(unit\_cost, 10)]. This space is covered by the second source. Figure 3 illustrates the contributions made by the two sources in covering the filter space of the query. Note that the difference between the filter space of the query and the filter spaces covered by the two sources is a null space.

Sometimes multiple data sources have to be joined in order to provide data for a query. For this purpose, a join operator is used. The join operator joins two keyvalue set definitions and creates a new key-value set definition with key and value sets obtained by combining key and value sets of join components. The filter clauses of the two join components are also combined and the nonbinding clauses removed. The join operator is defined in Appendix A.

Figure 3 Filter Space of a Query Covered by Two Data Sources  
![](/api/attachments/Q7858FAK/fulltext/images/eb0ad0a7d358c5f499d2d56144acae3efc26d08122cc2acd5a9dc498c5349262.jpg)  
Information Systems Research Vol. 13, No. 1, March 2002

Proposition 3. Given an ordered set of data sources S $= \{ \kappa - \nu _ { j } ^ { \varsigma } \} _ { j = 1 , \dots , m }$ such that $\kappa - \nu ^ { s } = \kappa - \nu _ { 1 } ^ { s }$ Join $\kappa - \nu _ { 2 } ^ { s } \dots$ Join $\kappa - \dot { \nu _ { m } ^ { s } } , \kappa - \nu _ { j } ^ { s } = \eta _ { j } ^ { s } , \kappa _ { j } ^ { s } , \nu _ { j } ^ { s } , \pi _ { j } ^ { s } \rangle . \kappa - \nu ^ { s } = \langle \eta ^ { s } , \kappa ^ { s } , \nu ^ { s } , \pi ^ { s } \rangle$ can provide data for a query defined by $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } ,$ $\pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset ,$ when the following conditions are true: (1) $\kappa ^ { q } = \kappa ^ { s }$ and $\nu ^ { q } \subseteq \nu ^ { s } , ( 2 ) \pi ^ { q }$ is covered in $\pi ^ { s }$ (See proof in Appendix B.)

By joining key-value set definitions of data sources, a single joined key-value set definition is obtained. According to Proposition $^ { 3 , }$ multiple data sources, upon being joined, provide all the data needed for a query when the following conditions are true: (1) the key attributes of the query match with the key attributes of the joined key-value set definition, (2) the set of value attributes of the query is contained in the set of value attributes of the joined key-value set definition, and (3) the filter space of the query is covered in the filter space of the joined key-value set definition.

The following example illustrates Proposition 3. Consider a query that requires pid, pname, price, and unit\_cost of products with pid in range 101–102. The key-value set definition of the query is given by:

j<sup>q</sup> - ‘query5’, {pid}, {pname, price, unit\_cost}, [GE(pid, 101), LE(pid, 102)]. ptable1 (Table 1) can provide pid, pname, and price for the query, but not unit\_cost, which is required to be computed using model prod1. Thus, in order to provide all the data needed for the query, ptable1 is required to be joined with the output of prod1. The key-value set definition of the relational data in ptable1 is

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\kappa-\nu_{l}=\langle\text{'product1',\{\mathrm{pid}\},\{pname, price\},\{GE(pid, 101), LE(pid, 104), GT(pname, MIN_RANGE), LT(pname, MAX_RANGE), GT(price, MIN_RANGE), LT(price, MAX_RANGE)\rangle.$
</div>

The key-value set definition of the output of model prod1 is given by:

$$
\begin{array}{l} \kappa - v _ {2} = \langle^ {\prime} p r o d 1 \_ u n i t \_ c o s t 1 ^ {\prime}, \\ \quad \{p i d \}, \\ \quad \{u n i t \_ c o s t \}, \\ \quad [ G E (p i d, 1 0 1), L E (p i d, 1 0 2), G T (u n i t \_ c o s t, M I N \_ R A N G E), \\ \quad L T (u n i t \_ c o s t, M A X \_ R A N G E), G T (q u a n t i t y, M I N \_ R A N G E), \\ \quad L T (q u a n t i t y, M A X \_ R A N G E) ] \rangle . \end{array}
$$

On joining $\kappa - \nu _ { 1 }$ and $\kappa - \nu _ { 2 }$ on the common attribute pid, the joined key-value set obtained is

j - ‘product1\_prod1\_unit\_cost1’, {pid}, {pname, price, unit\_cost}, [GE(pid, 101), LE(pid, 102), GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE), GT(price, MIN\_RANGE), LT(price, MAX\_RANGE), GT(unit\_cost, MIN\_RANGE), LT(unit\_cost, MAX\_RANGE), GT(quantity, MIN\_RANGE), LT(quantity, MAX\_RANGE)].

It can be seen that the key attribute of the query matches with the key attribute of j and value attributes of the query are contained in the value set of $\kappa - \nu$ . Furthermore, the filter clause of the query is covered in the filter clause of j. Hence, the key-value set definition obtained by joining $\kappa - \nu _ { 1 }$ and $\kappa - \nu _ { 2 } ,$ can provide all the data needed for the query.

We now consider mechanisms to automate model input data acquisition whereby the DSS, upon receiving a query, composes a composite model and translates query conditions to database queries for model input data acquisition. The clauses of a query, which are covered by the filter list of a model output, typically impose tighter restrictions on model inputs. The process of propagating query conditions to model input queries is defined next.

Definition 13. Let output relation s of model m defined by $\kappa - \nu ^ { s } = \langle \eta ^ { s } , \kappa ^ { s } , \nu ^ { s } , \pi ^ { s } \rangle$ provide data for a query $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ . Furthermore, let $\begin{array} { r } { \kappa - \nu _ { j } = \langle \eta _ { j } , } \end{array}$ $\kappa _ { j } , \nu _ { j } , \pi _ { j } \rangle$ denote the key-value set definition of the jth model input relation, $X _ { \pi q }$ denote the set of unique variables appearing in $\pi ^ { q } ,$ , and $X _ { \pi j }$ denote the set of unique variables appearing in $\pi _ { j } .$ The input filter reduction of $\pi _ { j }$ over $\pi ^ { q }$ is defined by the function <sup>q</sup> w : <sub>p</sub> $\pi _ { j } \to \pi _ { j q } ^ { \prime }$ as follows:

Step 13.1. Set $\pi _ { j q } ^ { \prime } = \pi _ { j } .$

Step 13.2. Replace all clauses of Type 1b of the form U(x, c1) in $\pi _ { j q } ^ { \prime } ,$ where $x \in X _ { \pi q } \cap X _ { \pi j }$ and c1 $\in { \cal C }$ with clauses of the same type U(x, c2) from $\pi ^ { q }$ where $c 2 \in C$

Step 13.3. Remove all clauses of Type 1b of the following form from $\pi ^ { \prime } { } _ { j q } \colon \Phi ( x , c )$ where x $\notin X _ { \pi q }$ and $c =$ MIN\_RANGE or MAX\_RANGE.

Step 13.4. Add clauses U(x, y) from $\pi ^ { q }$ such that U(x, y) $\notin \pi _ { j q } ^ { \prime } ,$ and the set of variables associated with arguments x and $y , X _ { x }$ and $X _ { y } ,$ respectively, are contained in $X _ { \pi j } , \operatorname { i . e . , } X _ { x } \subseteq X _ { \pi j }$ and $\mathrm { X } _ { y } \subseteq { X } _ { \pi j } .$

The input filter reduction facilitates the propagation of query restrictions to model inputs. Step 13.2 replaces model input clauses of Type 1b (which are less restrictive) with more restrictive clauses of the same type from the query. Dummy clauses in model input pertaining to variables not present in the query are removed in Step 13.3. In Step 13.4 those clauses from the query that were not incorporated in $\pi ^ { \prime } { } _ { j q }$ during Steps 13.1–13.3 are added, provided all variables in these query clauses are present in the filter list of the model input relation under consideration. Note that Step 13.4 does not introduce any infeasible clauses because the query’s filter space is required to be contained in the filter space of a model output (that includes filter clauses from the model input under consideration), before input filter reduction is attempted.

The following example illustrates input filter reduction. Consider a query that requires unit\_cost of product items with pid in the range: 101–104 such that the forecasted demand for product items is greater than its inventory level (i.e., product items that need to be produced). The key-value set representation of this query is

This query can be matched to the output ‘unit\_cost’ of model template prod3 presented earlier in §3 following Definition 9. This model has two inputs: forecast\_demand and inventory\_level. The filter list of forecast\_demand is [GE(pid, 101), LE(pid, 110), GT(quantity, MIN\_RANGE), LT(quantity, MAX\_RANGE)]. After input filter reduction, this filter list reduces to [GE(pid, 101), LE(pid, 104)]. The filter clause, LE(pid, 110) in the original filter list, is replaced by a tighter clause LE(pid, 104) is Step 13.2. Clauses GT(quantity,MIN\_RANGE), LT(quantity,MAX\_RANGE) are then eliminated in Step 13.3. Similarly the filter list of model input inventory\_level is also reduced. The key-value sets of the model input relations with reduced filter lists can now be posed as query.

The input filter reduction in Definition 13 does not propagate query clauses that involve variables from two or more model inputs (i.e., GT(quantity, level)). This is done during model template customization as follows:

Definition 14. A model template M with Input - $\{ \kappa - \nu _ { j } ^ { i } \} _ { j = 1 , \dots , m } ,$ and inter-input constraint set Filter can be customized for a given query q with filter list $\pi ^ { q }$ as follows:

Step 14.1. Reduce filter list of $\kappa - \nu _ { j } ^ { i } , j = 1 , \textrm { \hdots } , m$ (Definition 13).

Step 14.2. Set $F i l t e r = F i l t e r \cup C ,$ where $C = \{ \varPhi ( . ) \mid$ $\begin{array} { r } { \varPhi ( . ) \in \pi ^ { q } \wedge \exists \kappa - \nu _ { j } ^ { i } \ : ( X _ { \Phi ( . ) } \cap X _ { j } ^ { i } \neq \emptyset ) \wedge \exists \kappa - \nu _ { k } ^ { i } \ : ( X _ { \Phi ( . ) } \cap } \end{array}$ $\times _ { k } ^ { i } \neq \emptyset ) \land ( \mathrm { j } \neq \mathbf { k } ) \} ,$ , and $X _ { \Phi ( . ) } , \bar { X } _ { j } ^ { i } , X _ { k } ^ { i }$ represent the set of variables in $\Phi ( . ) , \kappa - \nu _ { j } ^ { i } ,$ and $\kappa - \nu _ { k } ^ { i } ,$ respectively.

Model template customization enables a model template to incorporate query clauses. In Step 14.1, query clauses involving variables from single model input are propagated to the respective inputs. Query clauses that involve variables from multiple inputs are incorporated into Filter in Step 14.2. Thus, during model execution, after model input data is obtained, clauses from Filter can be enforced to filter input data before it is used by the model. Step 14.2 does not introduce any infeasible clauses since the query’s filter space is contained in the filter space of the model output (that includes filter clauses from the model input as well as Filter). Continuing with the previous example, the filter clause GT(quantity, level) is added to Filter in Step 14.2. Note that a union operation is involved in Step 14.2. The content of Filter remains unchanged after Step 14.2 since GT(forecast\_demand.quantity, inventory\_level.level) and GT(quantity, level) are equivalent. The following proposition holds for the model customization transformation specified in Definition 14.

Proposition 4. Given a query specified by the key-value set definition $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q }$ $\neq \emptyset$ and model $M = \langle M o d e l N a m e _ { \cdot }$ , Input, Output, Assumption, Filter, Source with Input $= \{ \kappa - \nu _ { j } ^ { i } \} _ { j = 1 , \dots , m } ,$ $\kappa - \nu _ { j } ^ { i } = \langle \eta _ { j } ^ { i } , \kappa _ { j } ^ { i } , \nu _ { j } ^ { i } , \pi _ { j } ^ { i } \rangle , O u t p u t = \{ \kappa - \nu _ { k } ^ { o } \} _ { k = 1 , \dots , q }$ and the interinput constraint set Filter, such that the $k ^ { t h }$ model output $\kappa - \nu _ { k } ^ { o } = \eta _ { k } ^ { o } , \kappa _ { k } ^ { o } , \nu _ { k } ^ { o } , \pi _ { k } ^ { o } \rangle$ provides data for $\kappa - \nu ^ { q }$ Model customization with respect to p<sup>q</sup> will not lead to any infeasibilities in $\pi _ { j } ^ { i } , j = 1 , \ldots , m$ and Filter. (See proof in Appendix B.)

## 5. Model Composition and Execution Procedure

Model composition and execution entails searching the domain knowledge in the DSS for data sources (model outputs and database tables) in response to the query posed. The search process matches the query to data sources. To enhance the clarity of presentation in this paper, we make the assumption that attributes and variables are named such that there are no homonyms and synonyms. In fact, the restriction on synonyms is relaxed in our implementation. Schemes such as quiddity (Bhargava et al. 1991) can always be used to handle homonyms and synonyms. The control procedure used for composing and executing composite models is described next.

## 5.1. Query Processing Procedure (QPS)

The query processing procedure receives a query as a key-value set definition $( \kappa - \nu )$ . It then recursively processes $\kappa - \nu$ as follows:

(1) Search the domain knowledge for a database template such that j matches the key-value set definition of a database relation (Proposition 1). If successful, retrieve data and place it in OUT. Search is successful. Stop.

(2) Search the domain knowledge for a model template such that $\kappa - \nu$ matches the key-value set definition of a model output relation (Proposition 1) and model assumptions are affirmed by the user. If successful, customize model template (Definition 14) to obtain the set $K V _ { i n p u t }$ of key-value definitions of all model input relations as well as an updated set of interinput model constraints Filter. Set $O U T _ { i n p u t } = \emptyset ,$ $K V ^ { u } = \emptyset$

2.1. If $K V ^ { u } \neq \emptyset ,$ then go to 3. Else if $K V _ { i n p u t } = \emptyset ,$ filter model input data stored in $O U T _ { i n p u t }$ based on clauses specified in Filter of the model, execute model, put model output in OUT. Search is successful. Stop;

else remove a key-value set $\kappa - \nu$ from $K V _ { i n p u t } .$

2.2. Execute 1 with the change that on success, put data in $O U T _ { i n p u t } ,$ and go to 2.1.

2.3. Execute 2 with the change that on success, put output in $O U T _ { i n p u t , , }$ , and go to 2.1.

2.4. Execute 3 with the change that on success, put output in $O U T _ { i n p u t , \prime }$ , and go to 2.1.

2.5. $K V ^ { u } = K V ^ { u } \cup$ {j} and go to 2.1.

(3) Attempt to retrieve data from multiple data sources (Steps 3.1–3.6 in § 5.2). If successful, place data in OUT. Search is successful. Stop.

(4) Search is unsuccessful. Stop.

## 5.2. Procedure for Obtaining Data from Multiple Sources

When multiple data sources are required to provide data for a query, the following procedure is used. This procedure receives a key value set definition of the query $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ as input. The steps of this procedure are as follows:

3.1. Set $\pi ^ { \prime } = \pi ^ { q } .$

3.2. If the filter space $F S ^ { \prime }$ associated with $\pi ^ { \prime }$ is a null space or if $F S ^ { \prime }$ remains unchanged, then go to 3.6.

3.3. Search the domain knowledge for a database template such that $\kappa - \nu ^ { q }$ matches with the key-value set definition of the database template relation (with filter $\pi ^ { d } )$ after relaxing requirement 12.2, while satisfying requirement 12.1 for covering the filter list. If found, project $\pi ^ { d }$ to $\pi _ { d q }$ (Definition 11). If $F S ^ { \prime } \cap F S _ { \pi d q }$ is a nonnull space, where $F S _ { \pi d q }$ is the filter space associated with $\pi _ { d q } ,$ retrieve data from the database, and place it in OUT. Modify $\pi ^ { \prime }$ to incorporate the reduction in the filter space given by $F S ^ { \prime } \cap F S _ { \pi d q , } { \mathrm { g o } }$ to 3.2.

3.4. Search the domain knowledge for a model output such that $\kappa - \nu ^ { q }$ matches with the key-value set of the model output relation (with filter p<sup>o</sup>) after relaxing requirement 12.2, while satisfying requirement 12.1 for covering filter lists. If found, project $\pi ^ { o }$ to $\pi _ { o q } . \mathrm { I f } \ F S ^ { \prime } \ \cap$ $F S _ { \pi o q }$ is a nonnull space, where $F S _ { \pi o q }$ is the filter space associated with $\pi _ { o q } ,$ customize and execute model (as per steps under 2 in Section 5.1), and place the output in OUT. Modify $\pi ^ { \prime }$ to incorporate the reduction in the filter space given by $F S ^ { \prime } \cap F S _ { \pi o q } , { \bf g o }$ to 3.2.

3.5. Search the domain knowledge for a set of data sources $S = \{ \kappa - \nu _ { j } ^ { s } \} _ { j = 1 , \dots , m }$ such that (1) the key attributes of $\kappa - \nu ^ { q }$ match the key attributes of $\kappa - \nu ^ { s } ~ =$ $\kappa - \nu _ { 1 } ^ { s }$ Join $\kappa - \nu _ { 2 } ^ { s } \ldots$ . Join $\kappa - \pmb { \nu } _ { m } ^ { s } , \kappa - \pmb { \nu } ^ { s } = \langle \eta ^ { s } , \kappa ^ { s } , \pmb { \nu } ^ { s } , \pi ^ { s } \rangle .$ (2) the value attributes of $\kappa - \nu _ { q }$ are contained in $\nu ^ { s }$ (Proposition 3), and (3) on projecting $\pi ^ { s }$ to $\pi _ { s q }$ the requirement in 12.1 is satisfied and $F S ^ { \prime } \cap F S _ { \pi s q }$ is a nonempty space where $F S _ { \pi s q }$ is the filter space associated with $\pi _ { s q } .$ If S can be found, then depending on the data source, retrieve data from the database or customize and execute model (as per steps under 2 in § 5.1), and place it in OUT. Modify $\pi ^ { \prime }$ to incorporate the reduction in the filter space given by $F S ^ { \prime } \cap F S _ { \pi s q } , { \bf g 0 }$ to 3.2.

3.6. Combine the tuples in OUT using the union operator. If $F S ^ { \prime }$ is null, report solution found.

The query processing procedure always generates a feasible solution to a query upon successful termination as stated by the following proposition:

Proposition 5. The query processing procedure (QPS) always generates a feasible solution to the query $\kappa - \nu ^ { q } =$ $\langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset$ , upon successful termination.

(See proof in Appendix B.)

The composite models created follow partial ordering (Klein 1973, Ch. 3), thus, they can be represented by acyclic graphs. Two component models of a composite model need not have any precedence relationship. The query processing procedure presented, however, does not support any parallelism during model composition or execution (see Kottemann and Dolk 1992). Furthermore, the query processing procedure interleaves the search process for selecting model and database templates with database retrieval and model execution. Thus, model composition and execution are conducted together.

An implementation of the query processing procedure (discussed in § 6) supports user-controlled automation of the composition process. Model preconditions related to model inputs that are represented in the filter list of model outputs are automatically matched by the query processing procedure. Model assumption clauses contained in Assumption (see Definition 9) that are not related to any model inputs have to be affirmed by the user, before the model is selected. Thus, the user has control over the model to be selected. It is, however, not difficult to automate reasoning with clauses in Assumption. There could be multiple candidate composite models to answer a query. The query processing procedure presents candidate component models to users by following a depth-first search, which the user can accept or reject. This procedure does not generate all possible composite models and lets the user pick the best. But rather, it executes the first composite model whose component model assumptions have been affirmed by the user. The query processing procedure also does not guarantee the satisfaction of the minimality property (see Proposition 2). We developed the query processing procedure with the sole purpose of demonstrating the feasibility of using filter spaces during model composition. Sophisticated search procedures from the artificial intelligence literature (Rich and Knight 1991) can always be used to enhance the processing efficiencies of the query processing procedure. The worst-case complexity of the query processing procedure is $O ( ( M + N ) ! )$ , where M is the number of model templates and N is the number of database templates in the DSS. This complexity expression takes into account the steps associated with searching the domain knowledge only, and does not include the complexity of model execution logic.

The query procedure is explained using an example query that requires the unit\_cost of products with pid in the range 103–106. This query is represented by the following key-value set definition:

$$
\begin{array}{l} \kappa - \nu_ {q} = \langle^ {\prime} q u e r y 7 ^ {\prime}, \\ \quad \{p i d \}, \\ \quad \{u n i t \_ c o s t \}, \\ \quad [ G T (p i d, 1 0 2), L E (p i d, 1 0 6) ] \rangle . \end{array}
$$

The filter space of $\kappa - \nu _ { q }$ is a single-dimensional space defined by [GT(pid, 102), LE(pid, 106)]. The resources available to DSS include ptable1 (Table 1), ptable2 (Table 2), and models given in Table 3. It can be verified that no single data source (relational table or a model) covers the entire filter space of the query. Therefore, Steps 1 and 2 are not successful in generating data for the query. Steps 3.1–3.6 are executed next. Step 3.3 is successful, since after projecting the filter list of ptable2 [GT(pid, 105), LE(pid, 106), GT(pname, MIN\_RANGE), LT(pname, MAX\_RANGE), GT(price, MIN\_RANGE), LT(price, MAX\_RANGE), GT(unit\_cost, MIN\_RANGE), LT(unit\_cost, MAX\_RANGE)] on the filter list of the query, the projected list [GE(pid, 105), LE(pid, 106)] has the same dimensions as that of the query (i.e., pid) and the two filter spaces overlap. Thus, data can be retrieved from ptable2 and the tuples [[105, 7.00], [106, 7.00]] can be added to OUT.

The filter space of the query left to be covered (defined by p) is now [GT(pid, 102), LT(pid, 105)]. Step 3.2 is executed next. Since there was a change in the filter space, Steps 3.3–3.5 are executed again. In this iteration, Step 3.3 is not successful. Model prod2 output covers the data required by the filter space defined by $\pi ^ { \prime } .$ Therefore prod2 is executed next according to steps under 2. The customization of prod2 is carried out with respect to the query (Definition 14) and the input set $K V _ { i n p u t , , }$ , which contains a key-value set definition for quantity, is then posed as a subsidiary query to obtain data for the model-input quantity. Model dem2 is then identified as the source for quantity. Then the customization of dem2 is carried out and yet another new subsidiary query is generated to obtain its input price. The query data for price is retrieved from ptable1, and then model dem2 is executed to obtain quantity. Data for quantity is then passed on to model prod2, which then generates the tuples [[103, 4.00], [104, 5.00]] that are added to OUT. The resultant filter space left to be covered after prod2 execution is a null space since the filter list $\pi ^ { \prime } = I G T ( p i d ,$ 102), LT(pid, 105)]  [GT(pid, 102), LT(pid, 105)] - , after subtracting the contributions made by prod2 in covering the filter space. Control now passes back to Step 3.2. Since the filter space is now a null space, Step 3.6 is executed next where the tuples in OUT are combined, using the union operator to obtain the data for the query: [[103, 4.00], [104, 5.00], [105, 7.00], [106, 7.00]].

## 6. Implementation

We implemented a DSS prototype for a distributed environment to validate core concepts related to filter spaces. The domain knowledge and control procedures were implemented using ALS Prolog 2.08 (ALS Prolog 1997). ALS prolog is a logic programming language that supports foreign language interface, thereby making it possible to implement prolog predicates pertaining to data retrieval and model execution in ${ \mathrm { C } } / { \mathrm { C } } + +$

Database tables accessible to the DSS prototype were implemented as Oracle and Microsoft Access tables, whereas models were implemented in C and perl. While testing the prototype, models and data were distributed over multiple machines. Models were executed using object brokers based on the Common Object Request Broker Architecture (CORBA) standard (Umar 1997), and by executing Common Gateway Interface (CGI) scripts via HTTP (Umar 1997). The CORBA middleware used was Orbix 2.3 (Orbix 2.3C 1997). Database tables were accessed via Open Database Connectivity (ODBC) calls (Umar 1997). Further details on the DSS architecture and implementation can be found in Chari (2000).

While testing the DSS prototype, model composition involving three models was achieved, thereby validating core concepts related to filter spaces. The prototype has some limitations that include nonimplementation of the join operator and nonenforcement of the interinput model constraint, as well as partial support for OR clauses. These limitations can be overcome by additional programming effort.

## 7. Conclusion

Model composition is an important problem in model management. We have presented the state-of-the-art in model composition and execution via a comprehensive literature survey. Our literature survey shows two areas of weaknesses in existing approaches: (1) the issue of integrating partial solutions from multiple sources to provide solutions to a query, and (2) the issue of automating model composition and execution process. In response to this, we have introduced a new theoretical concept called filter spaces to facilitate model composition and execution. We have shown how filter spaces can facilitate the integration of partial solutions from multiple sources and automate model composition and execution. Filter spaces provide a “clean” separation between the control procedure and domain knowledge. This facilitates ease of maintenance as well as the partitioning of domain knowledge into small sets based on specific user needs. Computational times in searching the domain knowledge during model composition could therefore be greatly reduced. Our DSS prototype implementation has validated core concepts related to filter spaces.

We have demonstrated the notion that logic clauses that have predicate symbols representing inequalities can be viewed as constraints represented in multidimensional spaces when clause variables take values from an ordered set, and that reasoning with these clauses could be accomplished by matching filter spaces. Our approach allows contradiction among a set of clauses to be detected simply by assessing the size of the filter space, which, in the case of contradiction, is a null space.

There are many additional research issues that have to be addressed in the future. For practitioners, the development of tools to automate the generation of model and database templates would be useful. Such tools would draw information from data dictionaries of commercial databases and from prototypes of functions that contain model solution logic. Other important research issues relate to query processing capabilities that enable a DSS to compose models based on all types of SQL queries. This will be helpful in generating the next generation of DSS.

## Appendix A. The Join Operator

Definition A1. Given two key-value set definitions $\kappa - \nu ^ { x } = \langle \boldsymbol \eta ^ { x } ,$ $\kappa ^ { x } , \nu ^ { x } , \pi ^ { x } \rangle$ , and $\kappa - \nu ^ { y } = \langle \eta ^ { y } , \kappa ^ { y } , \nu ^ { y } , \pi ^ { y } \rangle ,$ , and the common joining attribute set r, $\kappa - \nu ^ { z } = \langle \eta ^ { z } , \kappa ^ { z } , \nu ^ { z } , \pi ^ { z } \rangle ,$ where $\mathbf { \kappa } \mathbf { \mathbf { k } } - \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } } ^ { z } = \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } } \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \Lambda } } } } } } }$ Join $\kappa - \nu ^ { y } = \kappa - \nu ^ { y }$ Join $\kappa - \nu ^ { x }$ is given below:

A1.1 If $\boldsymbol { \sigma } = \boldsymbol { \kappa } ^ { x } = \boldsymbol { \kappa } ^ { y } ,$ set $\star ^ { z } = \star ^ { x } , \star ^ { z } = \star ^ { x } \cup \star ^ { y } , \pi ^ { z } = \pi ^ { x } \cup \pi ^ { y } ,$ remove all nonbinding clauses from p<sup>z</sup>.

A1.2 If $\sigma = \kappa ^ { x }$ and r $\cap \kappa ^ { y } = \emptyset ,$ set $\mathbf { \nabla } \mathbf { \kappa } ^ { z } = \mathbf { \kappa } ^ { y } , \mathbf { \nu } ^ { z } = \nu ^ { x } \cup \nu ^ { y } \cup \kappa ^ { x } ,$ $\pi ^ { z } = \pi ^ { x } \cup \pi ^ { y } ,$ , remove all nonbinding clauses from p<sup>z</sup>. Else exchange values between $\kappa - \nu ^ { x }$ and $\kappa - \nu ^ { y }$ and repeat the preceding step in A1.2.

A1.3 If $\sigma = { \kappa } ^ { x }$ and $\sigma \subset \kappa ^ { y }$ set $\kappa ^ { z } = \kappa ^ { y } , \nu ^ { z } = \nu ^ { x } \cup \nu ^ { y } , \pi ^ { z } = \pi ^ { x }$ - $\pi ^ { y } ,$ remove all nonbinding clauses from p<sup>z</sup>. Else exchange values between $\kappa - \nu ^ { x }$ and $\kappa - \nu ^ { y }$ and repeat the preceding step in A1.3.

A1.4 If $\sigma \subset { \kappa ^ { x } }$ and r $\cap \kappa ^ { y } = \emptyset ,$ set j<sup>z</sup> - {j<sup>x</sup> - j<sup>y</sup>}  {<sup>y</sup>  j<sup>x</sup>}, <sup>z</sup> - <sup>x</sup> - <sup>y</sup>, p<sup>z</sup> - p<sup>x</sup> - p<sup>y</sup>, remove nonbinding clauses from p<sup>z</sup>. Else exchange values between $\kappa - \nu ^ { x }$ and $\kappa - \nu ^ { y }$ and repeat the preceding step in A1.4.

A1.5 If $\ u \subset \kappa ^ { x }$ and $\qquad \subset \ \kappa ^ { y } ,$ set $\kappa ^ { z } = \{ \kappa ^ { x } \cup \kappa ^ { y } \} - \{ \kappa ^ { y } \cap \nu ^ { x } \} -$ {j<sup>x</sup> $\cap \nu ^ { y } \} , \nu ^ { z } = \nu ^ { x } \cup \nu ^ { y } , \pi ^ { z } = \pi ^ { x } \cup \pi ^ { y } ,$ , remove all nonbinding clauses from p<sup>z</sup>.

A1.6 If $\ u { \ u { \cdot } } \cap \ d { \bf { k } } ^ { x } = \emptyset$ and r $\cap \ \kappa ^ { y } \ = \ \mathcal { O } ,$ set $\mathbf { \kappa } ^ { z } ~ = ~ \{ \mathbf { \kappa } ^ { x }$ - j<sup>y</sup>}  $\{ \kappa ^ { y } \ \cap \ \nu ^ { x } \} \ - \ \{ \kappa ^ { x } \ \cap \ \nu ^ { y } \} , \ \nu ^ { z } \ = \ \nu ^ { x } \ \cup \ \nu ^ { y } , \ \pi ^ { z } \ = \ \pi ^ { x } \ \cup \ \pi ^ { y } ,$ remove all nonbinding clauses from p<sup>z</sup>. Examples.

A1.1 Given j $\begin{array} { r } { \cdot \nu ^ { x } = \langle ^ { \prime \prime } x ^ { \prime \prime } , \{ a \} , \{ b \} , [ L T ( a , 1 0 ) , L T ( b , 1 0 ) ] \rangle , \kappa - \nu ^ { y } = } \end{array}$ “y”, {a}, {c}, [LT(a, 5), LT(c, 10)], r - {a}, then $\begin{array} { r } { \kappa - \nu ^ { z } = \big \langle \sp { \prime \prime } z \sp { \prime \prime } , \{ a \} , \{ b , } \end{array}$ c}, [LT(a, 5), LT(b, 10), LT(c, 10)].

A1.2 Given j<sup>x</sup> - “x”, {a}, {b}, [LT(a, 10), LT(b, 10)], $\kappa - \nu ^ { y } =$ “y”, {c}, {a}, $[ L T ( a , 5 ) , L T ( c , 1 0 ) ] \rangle , \sigma = \{ a \} _ { }$ , then $\kappa - \nu ^ { z } = \langle { } ^ { \prime \prime } z { } ^ { \prime \prime } , \{ c \} , \{ a ,$ b}, [LT(a, 5), LT(b, 10), LT(c, 10)].

A1.3 Given j<sup>x</sup> - “x”, {a}, {b}, [LT(a, 10), LT(b, 10)], j<sup>y</sup> - “y”, {a, c}, {d}, [LT(a, 5), LT(c, 10), LT(d, 10)], r - {a}, then $\kappa - \nu ^ { z } =$ “z”, {a, c}, {b, d}, [LT(a, 5), LT(b, 10), LT(c, 10), LT(d, 10)].

A1.4 Given j<sup>x</sup> - “x”, {a, b}, {c}, [LT(a, 10), LT(b, 10) LT(c, 10)], $\kappa - \nu ^ { y } = \langle { ' y ' } { ' } , \{ d \} ,$ {a}, [LT(a, 5), LT(d, 10)], r - {a}, then $\kappa - \nu ^ { z } =$ “z”, {b, d}, {c, a}, [LT(a, 5), LT(b, 10), LT(c, 10), LT(d, 10)].

A1.5 Given $\ \kappa - \nu ^ { x } = \langle \prime \prime x ^ { \prime \prime } ,$ {a, b}, {c}, [LT(a, 10), LT(b, 10), LT(c, 10)], $\begin{array} { r } { \kappa - \nu ^ { y } = \langle { } ^ { \prime \prime } y ^ { \prime \prime } , } \end{array}$ {a, d}, {b}, [LT(a, 5), LT(d, 10), LT(b, 10)], r - {a}, then $\begin{array} { r } { \kappa - \nu ^ { z } = \langle { \boldsymbol { \mu } } _ { z ^ { \prime \prime } } ^ { \prime \prime } , } \end{array}$ , {a, d}, {b, c}, [LT(a, 5), LT(b, 10), LT(c, 10), LT(d, 10)].

A1.6 Given $\kappa - \nu ^ { x } = \langle { ' z } x { ' } { ' } , \{ b  \} , \{ a \} , [ L T ( a , 1 0 ) , L T ( b , 1 0 ) ] \rangle , \kappa - \nu ^ { y } =$ “y”, {c}, {a, b}, [LT(a, 5), LT(b, 10), LT(c, 10)], r - {a}, then $\kappa - \nu ^ { z } =$ “z”, {c}, {a, b}, [LT(a, 5), LT(b, 10), LT(c, 10)].

## Appendix B. Proposition Proofs

Proposition 1. A single data source $\kappa - \nu ^ { s } = \langle \eta ^ { s } , \kappa ^ { s } , \nu ^ { s } , \pi ^ { s } \rangle$ can provide data for a query defined by the key-value set definition $\kappa - \nu ^ { q } =$ $\langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset ,$ when the following conditions are true: $\left( 1 \right) \kappa ^ { q } = \kappa ^ { s } , \left( 2 \right) \nu ^ { q } \subseteq \nu ^ { s }$ and (3) p<sup>q</sup> is covered in $\pi ^ { s } .$

Proof. Since ${ \bf { \kappa } } ^ { q } = { \bf { \kappa } } { \bf { \kappa } } ^ { s } ,$ , every tuple identified by the query can map to a unique tuple of the data source. Furthermore conditions j<sup>q</sup> $\boldsymbol = \boldsymbol { \kappa } ^ { s } ,$ and $\nu ^ { q } \subseteq \nu ^ { s }$ jointly imply that the data attributes required by the query are contained in the data source. Since $\pi ^ { q }$ is covered in $\pi ^ { s }$ (Definition 12), the filter space of the query is contained in the filter space of the source after necessary projection to equalize dimensions (Definition 11). Therefore the tuples required by the query are contained in the data source. Q.E.D.

Proposition 2. A minimal set of data sources $\begin{array} { r l r } { S } & { { } = } & { \{ \kappa - }  \end{array}$ $\pmb { \nu } _ { j } ^ { s } \} _ { j = 1 , . . . m } ,$ where $\kappa - \nu _ { j } ^ { s } = \eta _ { j } ^ { s } , \kappa _ { j } ^ { s } , \nu _ { j } ^ { s } , \pi _ { j } ^ { s } \rangle$ can provide data for a query , defined by key-value set $\kappa - \nu ^ { q } , = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq $ $\scriptstyle { \big | } { \big | } { \big | } _ { \big { \cdot } }$ when the following conditions are true: $\left( 1 \right) \kappa ^ { q } = \kappa _ { j } ^ { s } , j = 1 , \ldots , m , ( 2 )$ $\nu ^ { q } \subseteq \nu _ { j } ^ { s } , j = 1 , \ldots , m \left( 3 \right) X _ { \pi q } = X _ { \pi j q } , j = 1 , \ldots ,$ m, where $X _ { \pi q }$ and $X _ { \pi j q }$ are the set $o f$ unique variables appearing in $\pi ^ { q }$ and $\pi _ { j q } ^ { s } ,$ respectively, $\pi _ { j q } ^ { s } ~ i s$ obtained by projecting $\pi _ { j } ^ { s }$ over p<sup>q</sup>, $( 4 ) \ F S _ { \pi } ^ { q } \subseteq \cup _ { j = 1 , \dots , m } \ F S _ { \pi j q }$ where $F S _ { \pi j q }$ denotes the filter space associated with $\pi _ { j q } ^ { s }$ and $( 5 )$ no subset of S satisfies (4).

Proof. Since $\kappa ^ { q } = \kappa _ { j } ^ { s } , , j = 1 , \ldots , m ,$ , every tuple identified by the query can map to a unique tuple of a data source. Furthermore $\mathbf { \nabla } \kappa ^ { q } = \mathbf { \nabla } \kappa _ { j } ^ { s } ,$ and $\nu ^ { q } \subseteq \nu _ { j } ^ { s } , j = 1 , \dots , m _ { \cdot }$ , jointly imply that the data attributes required by the query are contained in a data source. The filter spaces of the different data sources after necessary projection (Definition 11) have the same dimensions as the filter space of the query since $X _ { \pi q } = X _ { \pi j q } , j = 1 , \ldots , m . F S _ { \pi q } \subseteq \cup _ { j = 1 , \ldots , m } F S _ { \pi j q } ,$ implies that all tuples required by the query are contained in the set of data sources $S .$ According to (5), S is a minimal set, since no subset of S provides all the data needed for the query. Q.E.D.

Proposition 3. Given an ordered set of data sources $\begin{array} { r l } { S } & { { } = } \end{array}$ $\{ \kappa - \nu _ { j } ^ { s } \} _ { j = 1 , \dots , m }$ such that $\kappa - \nu ^ { s } ~ = ~ \kappa - \nu _ { 1 } ^ { s }$ Join $\kappa - \nu _ { 2 } ^ { s } \ \ldots$ Join $\kappa - \nu _ { m } ^ { s } ,$ $\kappa - \nu _ { j } ^ { s } \ = \ \eta _ { j } ^ { s } , \kappa _ { j } ^ { s } , \ \nu _ { j } ^ { s } , \pi _ { j } ^ { s } \rangle . \kappa - \nu ^ { s } \ = \ \langle \eta ^ { s } , \kappa ^ { s } , \ \nu ^ { s } , \ \pi ^ { s } \rangle$ can provide data for a query defined by $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset ,$ , when the following conditions are true: $( 1 ) \kappa ^ { q } = \kappa ^ { s }$ and $\nu ^ { q } \subseteq \nu ^ { s } , ( 2 ) \pi ^ { q }$ is covered in p <sup>s</sup>.

Proof. Since ${ \bf { \kappa } } ^ { q } = { \bf { \kappa } } { \bf { \kappa } } ^ { s } ,$ , every tuple identified by the query can map to a unique tuple defined by $\kappa - \nu ^ { s }$ that is obtained by $\kappa \mathrm { ~ - ~ } \nu _ { 1 } ^ { s }$ Join $\mathbf { \epsilon } \mathbf { \kappa } - \mathbf { \nu } _ { 2 } ^ { s } \mathbf { \epsilon } \mathbf { \cdot } \mathbf { \cdot } \mathbf { \nabla } J o i n \ \kappa - \nu _ { k } ^ { s }$ Furthermore. $\kappa ^ { q } = \kappa ^ { s }$ and $\nu ^ { q } \subseteq \nu ^ { s }$ jointly imply that the data attributes required by the query are contained in the tuple set defined by $\kappa - \nu ^ { s } ,$ . Since $\pi ^ { q }$ is covered in $\pi ^ { s }$ (Definition 12), the filter space of the query is contained in the filter space defined by $\pi ^ { s }$ after necessary projection to equalize dimensions. Therefore the tuples required by the query are contained in the tuple set defined by j<sup>s</sup>. Q.E.D.

Proposition 4. Given a query specified by the key-value set definition $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ and model M - ModelName, Input, Output, Assumption, Filter, Source with Input $= \{ \kappa - \nu _ { j } ^ { i } \} _ { j = 1 , \ldots , m } , \kappa - \nu _ { j } ^ { i } = \eta _ { j } ^ { i } ,$ $\kappa _ { j } ^ { i } , \quad \nu _ { j } ^ { i } , \quad \pi _ { j } ^ { i } \rangle$ $\begin{array} { r l r } { O u t p u t } & { { } = } & { \{ \kappa - \nu _ { k } ^ { o } \} _ { k = 1 , \ldots , q } } \end{array}$ and the interinput constraint set Filter, such that the $k ^ { \mathrm { { t h } } }$ model output $\kappa - \nu _ { k } ^ { o } = \langle \eta _ { k } ^ { o } , \kappa _ { k } ^ { o } , \nu _ { k } ^ { o } ,$ provides data for<sup>o</sup> p  $\kappa - \nu ^ { q } .$ Model customization with respect to p<sup>q</sup> will not lead to any infeasibilities in $\pi _ { j } ^ { i } , j = 1 , \ldots , m$ and Filter.

Proof. Since $\kappa - \nu _ { k } ^ { o }$ provides data for j<sup>q</sup>, p<sup>q</sup> is covered in $\pi _ { k } ^ { o } .$ (Proposition 1). Model Customization involves Step 14.1 (Definition 13) and Step 14.2 (Definition 14). Let $I n p u t ^ { \prime } = \{ \kappa - \nu _ { j } ^ { i \prime } \} _ { j = 1 , \dots , p } ,$ $\kappa - \nu _ { j } ^ { i \prime } = \langle \eta _ { j } ^ { i } , \kappa _ { j } ^ { i } , \nu _ { j } ^ { i } , \pi _ { j q } ^ { \prime } \rangle$ be the set of inputs of model M after input reduction over p<sup>q</sup> (Definition 13) where $\pi _ { j } ^ { i }$ is transformed to $\pi _ { j q } ^ { \prime } , j =$ $1 , \ldots , p ,$ based on the given p<sup>q</sup>. The model customization sequence is as follows:

Step 13.1. After this step, $\pi _ { j q } ^ { \prime } , j = 1 , \ldots , p$ is feasible since $\pi _ { j q } ^ { \prime } =$ $\pi _ { j } ^ { i } ,$ where $\pi _ { j } ^ { i } ,$ is feasible due to $\mathrm { F S } _ { \pi j } ^ { i } \neq \emptyset , j = 1 , \ldots , p$ (Definition 9). Step 13.2. No infeasibilities introduced in $\pi _ { j q } ^ { \prime }$ since tighter clauses in $\pi ^ { q }$ replace corresponding clauses in $\pi _ { j q } ^ { \prime } ,$ thereby leading to a reduction in the filter space of $\pi _ { j q } ^ { \prime } j = 1 , \ldots , p .$

Step 13.3. Dummy clauses of Type 1b involving variables not present in $\pi ^ { q }$ are removed from $\pi _ { j q } ^ { \prime } ,$ which due to the maximum dimen-, sional property of $\pi _ { j } ^ { i }$ (Definition 9) contains clauses involving all variables associated with input $j .$ This also does not lead to any infeasibility due to the nature of dummy clauses.

Step 13.4. Clauses from $\pi ^ { q }$ that are not present in $\pi _ { j q } ^ { \prime }$ and involve only those variables present in $\pi _ { j } ^ { i }$ are added to $\pi _ { j q } ^ { \prime } .$ Since $F S _ { \pi k } ^ { o } \neq \emptyset$ and $\pi _ { k } ^ { o } \supset \{ \cup _ { j = 1 , \ldots , p } \pi _ { j } ^ { i } \} \cup$ Filter (Definition 9), there are no contradictions involving clauses of $\pi _ { j } ^ { i } , j = 1 , \ldots , p$ and Filter. Furthermore, condition: $\lnot ( \exists \Phi _ { 1 } ( x ) \in \pi _ { j } ^ { i }$ ∃U<sub>2</sub>(x)   <sup>i</sup>  p <sub>k</sub> ${ \bf \Gamma } _ { j \neq k } \left( \Phi _ { 1 } ( x ) \neq \Phi _ { 2 } ( x ) \right) )$ (Definition 9) forbids any and<sup>i</sup>p $\pi _ { k } ^ { i } , j \neq k$ from having two different Type 1b clauses with the same predicate symbol and the same variable x. Therefore, since $\pi ^ { q }$ is covered in $\pi _ { k } ^ { o }$ and $\pi _ { k } ^ { o } \supset \{ \cup _ { j = 1 , \ldots , p } \pi _ { j } ^ { i } \} , \pi _ { j } ^ { i }$ can never have tighter clauses than $\pi ^ { q } .$ . When $\mathrm { F } S _ { \pi } ^ { q } \neq \emptyset ,$ , clauses added in Step 13.4 can only be more restrictive and would not lead to any infeasibility in $\pi _ { j q } ^ { \prime } .$

Step 14.2. Filter, when not empty, is initially feasible since its associated filter space is not null (Definition 9). Let $F i l t e r ^ { \prime }$ be obtained by modifying Filter in Step 14.2. Since $\pi ^ { q }$ is covered in $\pi _ { k } ^ { o }$ and $\pi _ { k } ^ { o } \supset$ Filter (Definition $^ { 9 ) , }$ all interinput constraint clauses in $\pi ^ { q }$ are always tighter than the interinput constraint clauses in Filter. Therefore, $F i l -$ $t e r ^ { \prime }$ is feasible and Step 14.2 can only cause a reduction in the filter space of Filter based on p<sup>q</sup>. Q.E.D.

Proposition 5. The query processing procedure (QPS) always generates a feasible solution to the query $\kappa - \nu ^ { q } = \langle \eta ^ { q } , \kappa ^ { q } , \nu ^ { q } , \pi ^ { q } \rangle$ with filter space $F S _ { \pi } ^ { q } \neq \emptyset ,$ , upon successful termination.

Proof. Control flows in QPS in the following sequence:

Step 1. Database templates are searched. QPS successfully terminates in Step 1 when a database template with key-value set definition $\kappa - \nu ^ { \hat { d } } = \langle \eta ^ { d } , \kappa ^ { d } , \nu ^ { d } , \pi ^ { d } \rangle$ exists such that $( 1 ) { \bf \nabla } \kappa ^ { q } = { \bf \nabla } \kappa ^ { d } , ( 2 ) { \bf \nabla } \nu ^ { q }$ $\subseteq \nu ^ { d }$ and (3) p<sup>q</sup> is covered in $\pi ^ { d }$ (Proposition 1). In which case a feasible solution to the query is obtained.

Step 2. This step is executed only when Step 1 is unsuccessful. A model template M with an output given by j $\cdot \nu ^ { o } = \langle \eta ^ { o } , \kappa ^ { o } , \nu ^ { o } , \pi ^ { o } \rangle$ is selected only when (1) ${ \bf \delta } \kappa ^ { q } = \kappa ^ { o } , ( 2 ) \nu ^ { q } \subseteq \nu ^ { o } , ( 3 )$ p<sup>q</sup> is covered in $\pi ^ { o }$ (Proposition 1), and (4) model assumptions are affirmed. The subsidiary queries generated for model inputs after model customization are feasible (Proposition 4). QPS successfully terminates in Step 2 only when $K V ^ { u } = \emptyset$ and $K V _ { i n p u t } = \ O$ in Step 2.1 (i.e., data successfully generated for the subsidiary queries as per recursive steps 2.2 through 2.4, which in turn involve Steps 1 through 3 with control back to Step 2.1), input data filtered as per the clauses in $F i l t e r ,$ and model is executed successfully.

Step 3. Step $3 \ ( \mathrm { i . e . } ,$ Steps 3.1–3.6 in Section 5.2) is only executed when Step 2 is unsuccessful. $F S ^ { \prime } = \pi ^ { q }$ in Step 3.1, where $F S ^ { \prime }$ denotes the filter space of the query remaining to be covered. Step 3 successfully terminates only when $\begin{array} { r l r } { F S ^ { \prime } } & { { } = } & { F S _ { \pi q } \quad - \quad F S _ { \pi 1 q } \quad - } \end{array}$ $F S _ { \pi 2 q } - . . . - F S _ { \pi m q } = \mathcal { O } , \mathrm { i . e . , }$ , satisfies the condition $F S _ { \pi } ^ { q } \subseteq \cup _ { j = 1 , \dots , m }$ $F S _ { \pi j q }$ (condition [4] in Proposition 2), and the data obtained from multiple sources as per Steps 3.3–3.5 are combined using the union operator leading to a feasible solution for the query.

Step 3.3 is executed successfully only when $F S ^ { \prime } \neq \emptyset$ and a database template with key-value set definition j $\cdot \nu ^ { j } = \langle \eta ^ { j } , \kappa ^ { j } , \nu ^ { j } , \pi ^ { j } \rangle$ exists such that $( 1 ) \ \kappa ^ { q } = \kappa ^ { i } , ( 2 ) \ \nu ^ { q } \subseteq \nu ^ { j }$ (Proposition 1) and $( 3 ) ~ F S _ { \pi j q }$ $\cap F S ^ { \prime } \neq \emptyset$ where $F S _ { \pi j q }$ is the filter space obtained after projecting p over p<sup>q</sup>. $F S _ { \pi j q } \cap F S ^ { \prime } \neq \emptyset \Rightarrow F S ^ { \prime }$ can be reduced by retrieving data from the database. Step 3.3 is repeated until all database templates have been searched or $F S ^ { \prime } = \varnothing$

Step 3.4 is executed only when $F S ^ { \prime } \ne \emptyset ,$ , and the execution is successful only when a model template with an output with keyvalue set definition $\kappa - \nu ^ { j } = \langle \eta ^ { j } , \kappa ^ { j } , \nu ^ { j } , \pi ^ { j } \rangle$ exists such that it satisfies conditions (1), (2), and (3) in Step 3.3 above, and the model is executed successfully. Step 3.4 is repeated until all model templates have been searched or $F S ^ { \prime } = \varnothing$

Step 3.5 is executed only when $F S ^ { \prime } \ne \emptyset ,$ , and the execution is successful when a derived data source $\kappa - \nu ^ { j } = \langle \eta ^ { j } , \kappa ^ { j } , \nu ^ { j } , \pi ^ { j } \rangle$ obtained by joining a set of data sources satisfies conditions (1), (2), and (3) in Step 3.3 above and data for $\kappa - \nu ^ { i }$ is obtained successfully. Step 3.5 is repeated until all possible joins have been explored or $F S ^ { \prime }$ $= \varnothing .$

When any one of Steps 1, 2, or 3 is successful, QPS terminates successfully and a feasible solution is generated for the query. Q.E.D.

## Acknowledgments

The author wishes to thank the Associate Editor and the anonymous reviewers for their helpful comments. An earlier version of this paper was presented at the Workshop of Information Technologies and Systems (WITS), December 1999.

## References

ALS Prolog User Manual. 1997. Applied Logic Systems Inc., Cambridge, MA.

Ba, S., K. R. Lang, A. B. Whinston. 1997. Enterprise decision support using Intranet technology. Decision Support Systems 20(2) 99– 134.

Basu, A., R. W. Blanning. 1994. Model integration using metagraphs. Inform. Systems Res. 5(3) 195–218.

—, ——. 1998. The analysis of assumptions in model bases using metagraphs. Management Sci. 44(7) 982–995.

Bhargava, H. K., S. O. Kimbrough, R. Krishnan. 1991. Unique names violations, a problem for model integration or you say tomato, I say tomahto. ORSA J. Comput. 3(2) 107–120.

——, R. Krishnan, R. Muller. 1997. Decision support on demand: Emerging electronic markets for decision technologies. Decision Support Systems 19(3) 193–214.

Blanning, R. H. 1985. A relational framework for join implementation in model management systems. Decision Support Systems 1(1) 69–81.

——. 1993. Model management systems: An overview. Decision Support Systems 9 9–18.

Bonczek, R. H., C. W. Holsapple, A. B. Whinston. 1981. Foundations of Decision Support Systems. Academic Press, New York.

Chang, A. M., C. W. Holsapple, A. B. Whinston. 1993. Model management issues and directions. Decision Support Systems 9 19– 37.

Chang G. L., R. C-T. Lee. 1973. Symbolic Logic and Mechanical Theorem Proving. Academic Press, New York.

Chari, K. 2000. Multi-dimensional matching in enterprise-wide decision support systems. Working paper, Information Systems & Decision Sciences, University of South Florida, Tampa, FL.

Date, C. J. 1986. An Introduction to Database Systems Volume 1, 4th ed. Addison-Wesley Publishing Company, Reading, MA.

Dolk, D. R., J. E. Kottemann. 1993. Model integration and a theory of models. Decision Support Systems 9 51–63.

Dutta, A., A. Basu. 1984. An artificial intelligence approach to model management in decision support systems. IEEE Comput. 17(9) 89–97.

Geoffrion, A. M. 1987. An introduction to structured modeling. Man agement Sci. 33 547–588.

——. 1999. Structured modeling survey and future directions. Interactive Trans. ORMS 1(3).

Holocher, M., R. Michalski, D. Solte, F. Vicuna. 1997. MIDA: An open systems architecture for model-oriented integration of data and algorithms. Decision Support Systems 20(2) 135–147.

Jeusfeld, M. A., T. X. Bui. 1997. Distributed decision support and organizational connectivity. Decision Support Systems 19(3) 215– 225.

Klein, E. 1973. Mathematical Methods in Theoretical Economics. Academic Press, New York.

Kottemann, J. E., D. R. Dolk. 1992. Model integration and modeling languages: A process perspective. Inform. Sys. Res. 3(1) 1–16.

Krishnan, R. 1993. Model management: Survey, future research directions and a bibliography. ORSA CSTS Newsletter 14(1) 8–16.

——, P. Piela, A. Westerberg. 1993. Reusing mathematical models in ASCEND. C. Holsapple and A. Whinston, eds. NATO ASI on Decision Support Systems. Springer-Verlag, New York 275–294.

Liang, T. 1988. Development of a knowledge-based model management system. Oper. Res. 36(6) 849–863.

Mookerjee, V. S., A. R. Chaturvedi. 1993. A blackboard control architecture for model selection and sequencing. Eur. J. Inform. Systems 2(1) 3–14.

Muhanna, W. A. 1992. On the organization of large shared model bases. Ann. Oper. Res. 38 359–396.

——, R. A. Pick. 1994. Meta-modeling concepts and tools for model management: A systems approach. Management Sci. 40(9) 1093– 1123.

Orbix 2.3C for Windows NT. 1997. Iona Technologies Inc., Cambridge, MA.

Rich, E., K. Knight. 1991. Artificial Intelligence, 2nd ed. McGraw-Hill.

Shaw, M. J., P. Tu, P. De. 1988. Applying machine learning to model management in decision support systems. Decision Support Systems 4 285–305.

Sprague, R. H., Jr. E. D. Carlson. 1982. Building Effective Decision Support Systems. Prentice Hall, Upper Saddle River, NJ.

Umar, A. 1997. Object-Oriented Client/Server Internet Environments. Prentice Hall, Upper Saddle River, NJ.

Will, H. J. 1975. Model management systems. E. Grochia and N. Szyperski, eds. Information Systems and Organization Structure. Walter de Gruyter, Berlin, Germany 468–482.

Wright G. P., A. R. Chaturvedi, R. V. Mookerjee, S. Garrod. 1998. Integrated modeling environments in organizations: An empirical study. Inform. Systems Res. 9(1) 64–84.

Amit Basu, Associate Editor. This paper was received on August 4, 1999, and was with the authors 7 months for 3 revisions.
