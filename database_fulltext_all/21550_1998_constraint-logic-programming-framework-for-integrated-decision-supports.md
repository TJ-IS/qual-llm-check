---
otero_id: 21550
otero_key: "AD4B8QVU"
title: "Constraint logic programming framework for integrated decision supports"
authors: "Young U. Ryu"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00053-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Constraint logic programming framework for integrated decision supports

Young U. Ryu )

Decision Sciences Department, UniÕersity of Texas at Dallas, JO 4.4, Box 830688, Richardson, Texas 75083-0688, USA

## Abstract

Decision support systems provide decision-makers with an interactive environment for analyses of information with various models to help solve unstructured problems. Constraint logic programming as an improvement of logic programming can be used as a tool for the development of such decision support systems. Constraint logic programming is an integrated paradigm of logic modelling and mathematical programming. It has a modelling and analysis capacity for problems containing both qualitative and quantitative constraints; it has well-established declarative and procedural semantics, which reduce the model builder’s burden to specify problem solving procedures as a part of a model. In this paper, we demonstrate the use of constraint logic programming as a potential decision support system tool, focusing on the model representation and analysis aspects. q 1998 Elsevier Science B.V.

Keywords: Constraint logic programming; Decision support systems; Logic modelling; Model management

## 1. Introduction

Provided that a decision support system is an ‘interactive computer-based system that helps decision-makers utilize data and models to solve unstructured problems’ 25 , an aspect of decision sup-<sup>w</sup> <sup>x</sup> port systems studies is to develop techniques of data management and modelling of decision problems in a unified framework. A decision problem normally involves various numeric and non-numeric constraints, some of which are conflicting with each other. Decision-makers occasionally use heuristic and intuitional judgements based on assumptions, though they are willing to revoke their previous judgements, in the course of decision making. Decision-makers occasionally do not have complete information of the situation. Thus they perform ‘what-if’ and goal-seeking analyses involving constraints on possible situations. The analyses of a model require significant computations of both numeric and non-numeric constraints. This paper proposes the use of constraint logic programming as a tool for such decision support systems, focusing on the model representation and analyses.

Constraint logic programming is a declarative modelling and procedural programming environment that integrates qualitative<sup>r</sup>heuristic knowledge representation of logic and quantitative<sup>r</sup>algorithmic reasoning into a single paradigm. It has evolved from logic programming and provides powerful numeric manipulation features for logic programming 3,10 . <sup>w</sup> <sup>x</sup> As a result, it becomes possible to achieve the collaboration of quantitative<sup>r</sup>algorithmic programming of management science and qualitative<sup>r</sup>declarative<sup>r</sup>heuristic modelling of artificial intelligence. There are several fundamental reasons why the constraint logic programming paradigm is especially interesting. First, a constraint logic programming language is a language of predicate logic 13 ,<sup>w</sup> <sup>x</sup> in which there is a finite and mechanical procedure to generate a solution from a model, if the solution is valid. That is, given a model, constraint logic programming can mechanically generate a solution if Ž . Ž . 1 the solution validly follows the model and 2 the constraints of the model are satisfiable. Second, in principle, the declarative representation of a model is sufficient because the solution procedure for any model which can be represented by constraint logicŽ programming already exists in the language. A. model-specific solver, if required, can be obtained by applications of the build-in constraint solver. Third, two modules of the problem solver, resolution and constraint satisfaction engines, are implemented and built in the language. Thus, constraint logic programming can provide an efficient modelling environment, as well as solvers, for mathematical programming. Finally, constraint logic programming is based on well-defined procedural and declarative semantics, of which the procedural part is important as a programming language and the declarative part is essential as a modelling language.

An earlier approach to the use of constraint logic programming for decision making problems is observed in 8 , which focuses on problem solving with<sup>w</sup> <sup>x</sup> a specific version of constraint logic programming language called Keyed CLP. The integration of qualitative constraints of artificial intelligence and quantitative constraints of management science in a single paradigm of constraint logic programming is attempted in 15,16 , which discuss its relative advan- <sup>w</sup> <sup>x</sup> tages of mixed integer programming formulations obtained by converting qualitative constraints to $0 / 1$ integer constraints. While this paper agrees with these research works and in part based on their views, it more generally addresses the use of constraint logic programming as a tool for decision support systems, focusing on the aspect of the model representation and analyses, instead of problem solving and optimization capabilities.

The paper consists of three parts. Section 2 provides a concise overview of the constraint logic programming scheme, which is the underlying environment for decision support systems development. In Section 3, various modelling and model analysis features with constraint logic programming are presented. It starts with some representational aspects, demonstrates data<sup>r</sup>model analyses for decision supports, and addresses issues of heuristic components of models and constraint relaxation with hierarchical constraint reasoning. Finally, in Section 4, we propose some modification to the logical reasoning i.e., Ž resolution component of constraint logic program-. ming in order to improve its model analysis efficiency.

## 2. Constraint logic programming

Constraint logic programming 3,10 , shortly CLP, <sup>w</sup> <sup>x</sup> is an extension to logic programming 2,17 that is <sup>w</sup> <sup>x</sup> based on unification and resolution developed as a logic theorem prover 22 . Unification is a mecha-<sup>w</sup> <sup>x</sup> nism that determines if two expressions can become identical by substitutions of their variables. Suppose lowercase alphabets denote constants and uppercase alphabets denote variables. The unification of $p ( X , g ( a ) , Y )$ and $p ( f ( b ) , g ( Z ) , c )$ succeeds with the substitutions of X by f bŽ ., Y by c, and Z by a. Resolution is a process to deduce a formula from a given set of formulas. Suppose $p \vee q \thinspace (  p \thinspace $ is true or q is true and. $\neg q \lor r \mid q$ . is false or r is true are given. Then, deduced is $\boldsymbol { p } \lor \boldsymbol { r } \ ( \boldsymbol { p }$ is true or r is true . Resolution achieves this deduction by can- . celling $\lnot \ q$ from the first formula and $\lnot \ q$ from the second formula, and then establishing disjunction of the remaining components of the two formulas.

CLP uses resolution but replaces unification with a more general form of syntactic treatment, called constraint satisfaction, which is a mechanism to find ranges of variables i.e., solution spaces that satisfyŽ . a set of constraints. In fact, unification is a special case of constraint satisfaction, which is satisfaction of an equality constraint. The unification of $p ( X , g ( a ) , Y )$ and $p ( f ( b ) , g ( Z ) , c )$ is equivalent with the satisfaction of constraint $p ( X , g ( a ) , Y ) =$ $p ( f ( b ) , g ( Z ) , c )$

A CLP program consists of sentences of triples: ² : atom, list of atoms, set of constraints

in which the list of atoms and the set of constraints may be empty. An atom, or atomic formula, is the simplest form of formula in logic, which consists of a predicate symbol followed by a number of terms such as constants, variables, and functions. A constraint is either an arithmetic constraint:

$$
\langle \text { arithmetic   term } \rangle \Delta \langle \text { arithmetic   term } \rangle
$$

where is an arithmetic relation such as $\mathbf { \Phi } ^ { \bullet } = \mathbf { \Phi } ^ { , } \ \cdot \mathbf { \Phi } < \mathbf { \Phi } ^ { , }$ $^ { \cdot } \leq ^ { \prime } , \ ^ { \cdot } > ^ { \prime } , \ ^ { \cdot } \geq ^ { \prime } , \ \mathrm { o r } \ ^ { \cdot } \neq ^ { \prime }$ , a functor Ž . or identity constraint

$$
\langle \text { functor   term } \rangle \Xi \langle \text { functor   term } \rangle
$$

where $\boldsymbol { \Xi }$ is an identify relation $" = "$ , or a Boolean constraint

$$
\langle \text { Boolean   term } \rangle \Lambda \langle \text { Boolean   term } \rangle
$$

where is a Boolean relation such as $\cdot \wedge \ , \ \cdot \vee \ ^ { , }$ $\mathbf { \partial } ^ { \cdot } \supset \mathbf { \vec { \Phi } } , \mathrm { o r } \mathbf { \partial } ^ { \cdot } \equiv \mathbf { \vec { \Phi } }$ . An arithmetic term is either an arithmetic constant, a variable, or a function expression over a numeric domain. A functor term is either an arbitrary constant, a variable, a function symbol followed by a number of other functor terms, or a relational symbol followed by a number of other functor terms. A Boolean term is a relational symbol followed by a number of terms or a truth functional composition of Boolean terms. For instance, the following are arithmetic, functor, and Boolean constraints, respectively:

$$
\begin{array}{l} 2 * X + 3 * Y \leq Z + 2 \\ p (X, g (a), Y) = p (f (b), g (Z), c) \\ p (X) \vee , q (a, Y) \vee \neg r (X). \end{array}
$$

A query Ž . or goal is given as a state of a CLP interpreter, which is represented as:

² : list of variables, list of atoms, set of constraints

where the list of variables contains those appearing in the list of atoms and the set of constraints. Given a query as the initial state of a CLP interpreter:

$$
\sigma_ {0} = \left\langle V, \left(\alpha_ {1} \alpha_ {2}, \dots , \alpha_ {n}\right), C \right\rangle\tag{2.1}
$$

where $\alpha _ { 1 } , \ldots , \ \alpha _ { n }$ are atoms, C is a set of constraints, and V is the set of variables appearing in $\alpha _ { 1 } , \ldots , \alpha _ { n }$ and $C ,$ the interpreter finds a sentence in the CLP program:

$$
\langle \alpha , (\beta_ {1} \beta_ {2}, \dots , \beta_ {m}), C _ {1} \rangle
$$

where $\beta _ { 1 } , \ldots , \ \beta _ { m }$ are atoms and $C _ { 1 }$ is a set of constraints, and transforms $\sigma _ { 0 }$ to:

$$
\begin{array}{c} \sigma_ {1} = \big \langle V, (\beta_ {1} \beta_ {2}, \dots , \beta_ {m}, \alpha_ {2}, \alpha_ {3} \dots , \alpha_ {n}), \\ C \cup C _ {1} \cup \{\alpha = \alpha_ {1} \} \rangle \end{array}
$$

Under a CLP interpreter using active constraint processing, the satisfiability of

$$
C \cup C _ {1} \cup \{\alpha = \alpha_ {1} \}
$$

is tested whenever a state transformation is done. On the other hand, a CLP interpreter using passive constraint processing postpones the satisfiability test of constraints until all constraints are gathered 23 .<sup>w</sup> <sup>x</sup> Note, there exists an algorithm to determine the satisfiability of a set of equations and inequalities in the domain of real number arithmetic 26 .<sup>w</sup> <sup>x</sup>

Further transformations of states may result in:

$$
\sigma_ {k} = \langle V, (), C _ {k} \rangle\tag{2.2}
$$

where $C _ { k }$ is satisfiable. The CLP interpreter simplifies constraints in $C _ { k }$ and outputs them in terms of variables in V. If such a state is not obtained, the original query fails.

There exist a few implementations of the CLP scheme: CLPŽ . R <sup>w</sup> <sup>x</sup> <sup>w x</sup> 11,12 , Prolog III 4 , CHIP <sup>w</sup> <sup>x</sup> <sup>w x</sup> 27,28 , and Echidna 24 , among which CLPŽ . R is of special interests in this paper. CLPŽ . R implements the CLP scheme in the domain of real number arithmetic. It has been applied to various fields including financial management 14 , electrical engineering 7 , and optimization 15 . Thanks to its wide<sup>w x</sup> <sup>w</sup> <sup>x</sup> availability and relatively simple, but considerably powerful, syntax structure, we adopt it as the experimental platform in this paper.

A CLPŽ . R program consists of Horn clauses:

$$
\langle \text {   head   } \rangle : - \langle \text {   body   } \rangle
$$

in which head is an atomic formula and body is² : ² : a conjunction of atomic formulas and constraints. A query is of the following form:

$$
? - \langle \text { body } \rangle
$$

Constraints are of the form of:

$$
\begin{array}{l} \langle \text {arithmetic term} \rangle \Delta \langle \text {arithmetic term} \rangle \\ \langle \text {functor term} \rangle = \langle \text {functor term} \rangle \end{array}
$$

where is an arithmetic relation, either $\mathbf { \Phi } ^ { \bullet } = \mathbf { \Phi } ^ { \bullet } , \mathbf { \Phi } ^ { \bullet } > \mathbf { \Phi } ^ { \bullet }$ $^ { \cdot } < ^ { , } , \ ^ { \cdot } \geq ^ { , } , \ \mathrm { o r } \ ^ { \cdot } \leq ^ { , }$ . Note that CLPŽ . R does not support Boolean constraints and the disequality relation ‘<sup>/</sup> ’ which are supported by Prolog III. By excluding the disequality relation, CLPŽ . R can achieve solution-compactness in the domain of real number arithmetic as well as satisfaction-completeness. For the detail, refer to 10,26 .<sup>w</sup> <sup>x</sup>

## 3. Model analyses with constraint logic programming

## 3.1. Model representation in constraint logic programming

The fundamental building blocks of knowledge and a model in CLP are relations i.e., facts and Ž . relationships among relations i.e., rules . Let Ž . $\mathcal { D }$ be the domain of discourse of a world that a model intends to describe. Further by v² : expression b, we mean what ² : expression describes. An n-ary relation r is extensionally understood as:

$$
\llbracket r \rrbracket \subseteq \mathcal {D} ^ {n}
$$

An n-ary relation r with arguments $a _ { i } ( i = 1 , 2 , \dots ,$ n., when describing an object $\bar { d } \in \dot { \mathcal { D } }$ with properties of $\overline { { a } } _ { i } ( i = 1 , 2 , \ldots , n )$ , has an intentional meaning of:

$$
[   [ a _ {i} ]   ]: \overline {{d}} \to \overline {{a}} _ {i}, \text { where } \overline {{a}} _ {i} \in \mathcal {D}
$$

for all i. For constants $a _ { 1 } , ~ a _ { 2 } , \ldots , ~ a _ { n } ,$ , if $\left. { \mathbb { I } a _ { 1 } } \right] \mathbb { I }$ $[ [ a _ { 2 } ] ] , \ldots , [ [ a _ { n } ] ] \rangle \ \in \ [ [ r ] ]$ or there exists $\bar { d } \in \mathcal { D }$ with properties $\overline { { a } } _ { 1 } , \ : \overline { { a } } _ { 2 } , \ldots , \ : \overline { { a } } _ { n }$ such that $\mathbb { I } a _ { i } \mathbb { J } \left( \overline { { \mathrm { d } } } \right) = \overline { { a } } _ { i }$ for all i, then we say that $r ( a _ { 1 } , a _ { 2 } , \ldots , a _ { n } )$ is true.

A rule is an expression of

$$
r _ {0} \colon - r _ {1}, r _ {2}, \dots , r _ {n}
$$

where $r _ { i }$ for every i is a relation followed by a number of arguments. Its declaratiÕe meaning is $\cdot _ { r _ { 0 } }$ is true if $r _ { 1 } , \ r _ { 2 } , \ldots ,$ and $r _ { n }$ are true.’ On the other hand, its procedural meaning is ‘in order to satisfy $r _ { 0 } .$ , satisfy $r _ { 1 } .$ , and then $r _ { 2 }$ , and so on.’ The declarative interpretation of rules implies that a problem, or its model, is represented as a theory of logic that is,Ž a set of proper axioms in the CLP scheme and. computation, or control, can be considered as deduction from the theory. Ideally, thus, a model builder only specifies a theory for a problem, or a problem structure from which a theory can be obtained; the built-in resolution and constraint satisfaction engines of CLP supply all necessary computation information, independently of the provided theory 6 . The main advantage of the declarative aspect is in the improvement of model construction and management productivity.

An interesting observation can be drawn from the procedural aspect of a rule: A rule can be viewed as decomposition of a problem. That is, problem $r _ { 0 }$ is decomposed into sub-problems of $r _ { 1 } , r _ { 2 } , \ldots$ , and $r _ { n } ,$ where the dependency among the main problem and sub-problems is established by common variables and ideally nothing else. The result of solving a sub-problem is a set of constraints, which are passed to the next sub-problem, and so on. The main problem is thus solved by aggregating all those constraints obtained by solving sub-problems. The procedural interpretation has a practical implication for model builders: A model builder constructs a model by decomposing it into mutually dependent components which eventually are expressed as relations with constraints.

Though CLP, as a modelling language, does not provide such a rich model management environment as dedicated modelling languages including the structured modelling language 6 and AMPL 5 , it<sup>w x</sup> <sup>w x</sup> supports some of features of good modelling systems prescribed by Geoffrion 6 . First, two modules of<sup>w</sup> <sup>x</sup> the problem solver, resolution and constraint satisfaction engines built in CLP, not embedded in specific models, achieve the independence of model representation and model solution, to some extent. CLP’s built-in modules of the problem solver are very generic and can be used for a variety of problems. However, their generality can have problems of efficiency for specific problems. For instance, when a model is mainly structured as a network optimization model for which specific and highly efficient algorithms exist, solving the model with the generic linear constraint satisfaction engine is not efficient at all. Then, it may be desirable to manipulate the generic linear constraint satisfaction engine and build more efficient problem solver, which is embedded in the model. This will make model representation dependent on model solution.

Second, the representational independence of the abstract and general model structures e.g., model Ž classes or model library 18 and the detailed data <sup>w</sup> <sup>x</sup> needed to describe specific model instances is achieved by the separation of rules describing model structures and facts establishing model instances 8 . <sup>w</sup> <sup>x</sup>

However, CLP itself does not have a mechanism to establish relationships among model classes; such establishment would improve productivity of modelling activities. For instance, the class of integer programming models and that of general linear programming models share many common attributes in their structures; a model management system can achieve the representational efficiency by classifying both as sub-classes of a more general class of models such that the structure description of the general class contains common attributes and those of subclasses only contain specific ones 9 .<sup>w</sup> <sup>x</sup>

CLP’s relative inferiority to dedicated modelling languages in model management is attributed to its being not only a declarative modelling language, but also a procedural programming language. That is, CLP is closer to a general programming language than dedicated modelling languages are. The advantage of being close to a programming language is Ž . that complex model structures and efficient problem solving methods including heuristics specific to models can be developed with a same syntactic structure. While modelling with a dedicated modelling language requires the creation of a solver with other programming languages, when the solver is not readily available or a more efficient implementation of the solution algorithm is required, CLP can perform both with one language. That is, though CLP is less effective in model management than dedicated modelling languages, it has the advantage of the flexibility in dealing with specific solution procedures for models. Further, CLP’s being a programming language implies the possibility of implementing a model management system in CLP. Considering the fact that the model library system 17 which <sup>w</sup> <sup>x</sup> Ž is a model management system is implemented in . Prolog that can be regarded as a sub-system of CLP, the development of a model management system in CLP seems feasible. However, this issue is beyondŽ the scope of this paper and will not be further discussed..

Types of models that are suitable for CLP depend on the domains supported by specific CLP implementations. Generally speaking, CLP provides a logical and computational paradigm for constraint satisfaction problems in which a great portion of knowledge is formulated as a set of constraints on variables. The resolution and constraint satisfaction engines of CLP solves problems by 1 assigning val- Ž . ues to the variables such that the assignments are consistent with all the constraints or 2 determiningŽ . if such assignments exist or not. The domains of variables restrict types of constraints and thus types of models. Most CLP implementations support the domain, called Herbrand Universe, of traditional logic programming. Therefore, qualitative constraints obtained from unification viewed as a part of equal-Ž ity constraint satisfaction over relations and func-. tions are naturally supported in CLP. CLPŽ . R explicitly supports the domain of real numbers so that equality and inequality constraints on variables over the domain are handled. Therefore, CLPŽ . R is useful for the representation and analyses of some classes of linear programming, dynamic programming, and network models. On the other hand, CLPŽ . R is not suitable for models containing discrete domains such as integer programming models, though models with a small number of integer constraints can be established by using general programming features of CLPŽ . R . CHIP and Echidna, other CLP implementations, are more suitable for models, such as integer programming and scheduling, with constraints over discrete domains, because they support integer and arbitrary discrete domains.

## 3.2. ‘What-If’ and goal-seeking analyses

‘What-if’ and goal-seeking analyses are techniques in which a decision-maker changes relationships among variables and observes the resulting changes in values assigned to other variables. The observation of the value of a goal variable as values of other variables change is a ‘what-if’ analysis; the observation of the value of a non-goal variable as the target value of the goal variable changes is a goalseeking analysis. The essence of ‘what-if’ and goalseeking analyses is to find relationships between a goal variable and other parameters.

Though, in general, logic is suitable for the investigation of consequences from what is already known to hold, it can be used as a means for the decision analyses of ideas. In such analyses, one poses formulas as proper axioms, not because they are known to Ž be true, but because one attempts to discover what . consequences would hold if they were true. In addition, since CLP provides constraint handling facilities, one declares constraints not because they must be necessarily satisfied, but because one wants to investigate the outcome resulting from the satisfaction of the constraints. The ‘what-if’ and goal-seeking analyses with CLP follow this use of logic and the constraint satisfaction testing.

With CLP, ‘what-if’ and goal-seeking analyses are performed as follows. Upon a success Eq. 2.2Ž Ž .. of a query Eq. 2.1 , a CLP interpreter returnsŽ Ž .. $C _ { k }$ as an answer to the query. In order to find relationships between a goal variable $v _ { g }$ and certain parameters $v _ { 1 } , \ldots , v _ { n } ,$ we make all other variables bound to instances; that is, among variables in V, only $v _ { g }$ and $v _ { 1 } , \ldots , v _ { n }$ are not instantiated by the initial constraint set C of the query Eq. 2.1 . Then, every answer to Ž Ž .. the query is returned as a set of constraints specifying relationships between $v _ { g }$ and $v _ { 1 } , \ldots , v _ { n } .$ With this constraint set, we perform ‘ what-if’ and goalseeking analyses efficiently.

For instance, consider a binomial option pricing model that determines the call option value C on a stock 14 :<sup>w</sup> <sup>x</sup>

$$
C = \max (S \cdot \Delta + B, S - K)
$$

provided that

$$
\begin{array}{c} (u + 1) \cdot S \cdot \Delta + (r + 1) \cdot B = \max (0, (u + 1) \cdot S \\ - K) \end{array}
$$

$$
\begin{array}{c} (d + 1) \cdot S \cdot \Delta + (r + 1) \cdot B = \max (0, (d + 1) \cdot S \\ - K), \end{array}
$$

where S is the stock price, is the ratio of option value change relative to stock price change, B is the dollar amount in riskless bonds, K is the option exercise price, r is the interest rate, u is the up-rate of return, and d is the down-rate of return. The iteration of the binomial pricing model over a period of time is modeled as follows.

<sup>r</sup> ) c a ll s to c k Ž \_ p r ic e , o p tio n \_ v a lu e , stock\_price\_tree, option\_value\_tree, option\_exercise\_price, interest\_rate. )<sup>r</sup>

$$
\operatorname{call} (S, S - K, l (S), l (S - K), K, \_) \colon - S > K.
$$

$$
\operatorname{call} (\mathrm{S}, 0, \mathrm{l} (\mathrm{S}), \mathrm{l} (0), \mathrm{K}, \_) \colon - \mathrm{S} <   = \mathrm{K}.
$$

$$
\text { Delta } = (\mathrm{CUp} - \mathrm{CDown}) / (\mathrm{SUp} - \mathrm{SDown}),
$$

$$
(\text { Delta } * \mathrm{S} - \mathrm{C}) * (\mathrm{R} + 1) = \text { Delta } * \mathrm{SUp} - \mathrm{CUp},
$$

![](/api/attachments/AD4B8QVU/fulltext/images/56cdf569a325424bf010a628b6a3f14a544b77c36e2521943ddd90ce4f7cb2f9.jpg)  
Fig. 1. A stock price tree over a period of three time units.

call SDown,CDown,SLeft,CLeft,K,R ,Ž . call SUp,CUp,SRight,CRight,K,R .Ž .

With this CLPŽ . Ž . R program, one can perform 1 ‘what-if’ analyses to observe option values over time periods given stock prices over the same time periods, option exercise prices, and interests and 2Ž . goal-seeking analyses to find instances of other parameters to achieve a target option value.

Suppose the current price of the stock is 120 and expected to vary over the period of the next three time units as illustrated in Fig. 1, and the interest is 12%. We would like to find the current value of the option when the exercise price is 85, The following query performs this:

l 50 ,s 90,l 70 ,l 100 , Ž .. Ž Ž . Ž ...

$$
\mathrm{s} (1 8 0, \mathrm{s} (9 0, 1 (6 0), 1 (1 9 0)), \mathrm{s} (2 7 0, 1 (2 0 0), 1 (3 3 0)))),
$$

Rate<sup>s</sup>0.12, OptionValue<sup>)s</sup>0, Exercise<sup>s</sup> 85, callŽ\_,OptionValue,StockTree,OptionTree, Exercise,Rate ..

Answer´

$$
\text { OptionTree } = \mathrm{o} (6 7. 5 9 1 2, \mathrm{o} (7. 6 1 1 6 1,
$$

$$
\mathrm{o} (0, 1 (0), 1 (0)), \mathrm{o} (1 3. 7 5, 1 (0), 1 (1 5))),
$$

$$
\mathrm{o} (1 1 7. 4 3 5, \mathrm{o} (2 9. 4 2 3 1, \mathrm{l} (0), \mathrm{l} (1 0 5)),
$$

$$
\mathrm{o} (1 9 4. 1 0 7, \mathrm{l} (1 1 5), \mathrm{l} (2 4 5))))
$$

That is, the estimated current value of option is 67.6 and its values over the time period are as in Fig. 2. What will be the current value of option if the exercise price is 80, instead of 85? It could be done by issuing the similar query with Exercise<sup>s</sup> 85. But, more efficient ‘what-if’ and goal-seeking analyses would be done by deriving the relationship between the exercise price and the option value.

![](/api/attachments/AD4B8QVU/fulltext/images/0dca62c9e74b275ba64721acecc7f1f5060b8d0e24c87b509ac1cc826ea0508e.jpg)  
Fig. 2. The option value tree with exercise price of 80 and 12% interest.

```csv
?- StockTree = s(120,s(60,s(30,l(15),l(50)),s(90,l(70),l(100))),  
s(180,s(90,l(60),l(190)),s(270,l(200),l(330)))),  
Rate = 0.12,OptionValue >= 0,  
call(_,OptionValue,StockTree,  
_,Exercise,Rate).  
Answers ⇒  
Exercise < 15, OptionValue = -0.71178*Exercise + 120  
Exercise < 50, Exercise >= 15, OptionValue = -0.66362*Exercise + 119.278  
Exercise < 60, Exercise >= 50, OptionValue = -0.608999*Exercise + 116.547  
Exercise < 70, Exercise >= 60, OptionValue = -0.493934*Exercise + 109.643  
Exercise < 100, Exercise >= 70, OptionValue = -0.498406*Exercise + 109.956  
Exercise < 190, Exercise >= 100, OptionValue = -0.326239*Exercise + 92.739  
Exercise < 200, Exercise >= 190, OptionValue = -0.273608*Exercise + 82.7392  
Exercise < 330, Exercise >= 200, OptionValue = -0.215519*Exercise + 71.1213  
Exercise >= 330, OptionValue = 0  
From these answer, we build a CLP program. (Or it can be built automatically with some simple CLP codes.)  
o(OptionValue,Exercise):- Exercise < 15, OptionValue = -0.71178*Exercise + 120.  
o(OptionValue,Exercise):- Exercise < 50, Exercise >= 15, OptionValue = -0.66362*Exercise + 119.278.  
o(OptionValue,Exercise):- Exercise < 60, Exercise >= 50, OptionValue = -0.608999*Exercise + 116.547.  
o(OptionValue,Exercise):- Exercise < 70, Exercise >= 60, OptionValue = -0.493934*Exercise + 109.643.  
o(OptionValue,Exercise):- Exercise < 100, Exercise >= 70, OptionValue = -0.498406*Exercise + 109.956.  
o(OptionValue,Exercise):- Exercise < 190, Exercise >= 100, OptionValue = -0.326239*Exercise + 92.739.  
o(OptionValue,Exercise):- Exercise < 200, Exer-
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
cise &gt; = 190, OptionValue = -0.273608 * Exercise + 82.7392.
o(OptionValue,Exercise):- Exercise &lt; 330, Exercise &gt; = 200, OptionValue = -0.215519 * Exercise + 71.1213.
o(OptionValue,Exercise):- Exercise &gt; = 330, OptionValue = 0.
With this program, 'what-if' (i.e., to find the current option value when the exercise price changes) and goal-seeking (i.e., to find an exercise price given a target option value) analyses are done simply and quickly.
Similarly, the relationship between the exercise price and the interest rate, provided that our goal is to make the current option value 30, is obtained by the following.
?- StockTree = s(150,l(140),l(160)), OptionValue = 30, Rate &gt; = 0,
    call(_,OptionValue,StockTree,_,Exercise,Rate).
Answers ⇒
    Rate &lt; 0.166667, Exercise = 120 * Rate + 120
    Rate &gt; = 0.166667, -7 * Exercise + 1120 = (-7.5 * Exercise + 1170) * (Rate + 1)
That is,
 $K=\left\{\begin{aligned}120(r+1)&amp;\text{if }r&lt;1/6\\1170r+50\\\hline7.5r+0.5\end{aligned}\right.$ if $r\leq1/6$ ,
and
 $120\leq K&lt;160$ .
The following query is to find the exercise price to achieve the goal of the current option value of at least 40 provided that the interest rate is 12%.
?- StockTree = s(150,l(140),l(160)),OptionValue &gt; = 40, Rate = 0.12,
call(_,OptionValue,StockTree,_,Exercise,Rate).
Answer ⇒
    OptionValue = -0.892857 * Exercise + 150
    Exercise &lt;= 123.2
When the highest exercise price 123.2 is given, option values over the period of the current and next time units are obtained as:
?- StockTree = s(150,l(140),l(160)),Exercise = 123.2, Rate = 0.12,
call(_,StackTree,OptionTree,Exercise,Rate).
Answer ⇒
    OptionTree = o(40,l(16.8),l(36.8))
</div>

![](/api/attachments/AD4B8QVU/fulltext/images/89a5112721c8dd8ae49bb08bbd26b7579e52b6c3bfd15cab25db00a3940da6e2.jpg)  
Fig. 3. A sample AND<sup>r</sup>OR graph 20 Numbers on arcs denote<sup>w</sup> <sup>x</sup> Ž time durations of activities ..

## 3.3. Heuristics

A heuristic is ‘task-dependent information to help reduce search’ 20 or ‘a technique that improves the<sup>w</sup> <sup>x</sup> efficiency of a search process, possibly by sacrificing claims of completeness’ 21 . Heuristics can be ap-<sup>w</sup> <sup>x</sup> plied to a class of problems i.e., a general heuristicŽ . or a specific problem i.e., a problem-specific heuris-Ž tic . In this section, we demonstrate the use of. heuristics with CLP.

## 3.3.1. General heuristics

For example, consider the AND<sup>r</sup>OR graph in Fig. 3, which is used to schedule a project by extending PERT<sup>r</sup>CPM networks 19 . Differently from a PERT<sup>r</sup>CPM network in which all arcs merging to a node represent concurrent activities, arcs linked by an AND-connector represent concurrent activities and others represent choice activities. The scheduling includes finding an optimal plan, that is, a set of activities requiring the least amount of time. Let durŽ . Ž . A and source A denote the time duration and the source node, respectively, of an activity represented by an arc A. Given a node N and a set of arcs $A _ { 1 1 } , \ A _ { 1 2 } , . . . , \ A _ { 1 k }$ under an AND-connector, a set of arcs $A _ { 2 1 } , \ A _ { 2 2 } , . . . , \ A _ { 2 l }$ under an AND-connector, . . . , and a set of arcs $A _ { n 1 } , ~ A _ { n 2 } , . . . , ~ A _ { n m }$ under an AND-connector merging to N Žas in Fig. 4 we define t NŽ . as follows:

$$
t (N) = \min \left\{A _ {1} ^ {\max}, A _ {2} ^ {\max}, \dots , A _ {n} ^ {\max} \right\}
$$

where

$$
\begin{array}{c} A _ {1} ^ {\max} = \max \bigl \{\mathrm{dur} (A _ {1 1}) + t (\text { source } (A _ {1 1})), \\ \dots , \mathrm{dur} (A _ {1 k}) + t (\text { source } (A _ {1 k})) \bigr \} \\ A _ {2} ^ {\max} = \max \bigl \{\mathrm{dur} (A _ {2 1}) + t (\text { source } (A _ {2 1})), \\ \dots , \mathrm{dur} (A _ {2 l}) + t (\text { source } (A _ {2 l})) \bigr \} \end{array}
$$

$$
\begin{array}{c} A _ {n} ^ {\max} = \max \left\{\operatorname{dur} \left(A _ {n 1}\right) + t \left(\text { source } \left(A _ {n 1}\right)\right), \right. \\ \dots , \operatorname{dur} \left(A _ {n m}\right) + t \left(\text { source } \left(A _ {n m}\right)\right) \} \end{array}
$$

Note that t NŽ . denotes the shortest time duration to reach node N. We further define a heuristic value h NŽ ., an estimated future time duration after node N is reached. The value of h NŽ . depends on how many steps to look ahead. Using a one-step look-ahead, those in Fig. 3 are as follows:

$$
\begin{array}{r l} h (A) & = 7, h (B) = 9, h (C) = 3, h (D) = 5, h (E) \\ & = 1, h (F) = 2. \end{array}
$$

The heuristic search works as follows:

1. Mark the Start node.

2. Get t NŽ . of every node N, if the source node of an incoming arc of N Žnot under an AND-connector or the source nodes of an incoming arc set of. N under an AND-connector are marked.

3. Find a node N where $t ( N ) + h ( N )$ is the smallest and mark it.

4. Repeat Steps 2 and 3 until the Finish node is marked.

5. Then, the subgraph consisting of marked nodes describes an optimal plan.

Let us represent a directed AND<sup>r</sup>OR graph as:

$$
G = \langle A, N \rangle
$$

where A is a finite set of arcs and N is a binary relation:

$$
\begin{array}{l} N = \left\{\langle   \Pi_ {i}, A _ {i} \rangle | \cup_ {i} \Pi_ {i} = \Pi ; \cap_ {i} \Pi_ {i} = \emptyset ; \cup_ {i} A _ {i} \right. \\ \quad = A; \cap_ {i} A _ {i} = \emptyset \big \}, \end{array}
$$

where is a partition on A. Elements of a non-singleton set $\pi \ \in \ \pi _ { \mathrm { i } }$ represent concurrent activities Ž . i.e, arcs under an AND-connector . The following is

![](/api/attachments/AD4B8QVU/fulltext/images/eb4cf2ad3238620b39fb822ce4dcc3fadbb07564fac533df103f25e66317c719.jpg)  
Fig. 4. A component of an and<sup>r</sup>or graph.

```prolog
solve(Look_Ahead_Steps):-  
mark(X,Y),  
print('t'),print(X),print(') = '),print(Y),nl,  
repeat,  
go(Look_Ahead_Steps),  
mark(finish,_).
```

The start node is initially marked with the shortest time, 0:

The following program finds every reachable node and the shortest time to reach it with the adjustment by the look-ahead time, and then selects a node and marks it.

reachable Node,T,LookŽ . \_Ahead\_Steps :-

not mark Node,Ž . \_ ,

add\_look\_ahead LookŽ \_Ahead\_Steps,LL,Time, LLL , minof LLL,arc. Ž Ž .. \_,T .

go LookŽ . Ž Ž . \_Ahead\_Steps :- findall arc Node,T ,reachable Node,T,LookŽ . . \_Ahead\_Steps ,L ,

The above program is for the Steps 2 and 3 of the above heuristic search. Finally, the following program repeats the search until the finish node is marked:

The optimal plan of the problem in Fig. 3 is, thus, obtained as follows:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
?- solve(1).
Answer  $\Rightarrow$ 
t(start) = 0
t(c) = 3
t(e) = 6
t(f) = 7
t(finish) = 11
</div>

The above heuristic search significantly reduces the total number of calculations for t NŽ ., that is, reduces the computational complexity. With the heuristic search, only start, c, e, f, and finish nodes and connected arcs are searched. However, without the look-ahead heuristic component, the search is done for start, c, e, b, a, f, and finish nodes and connected arcs. Using a multiple-step look-ahead, when the AND<sup>r</sup>OR graph is big, one can reduce the computational complexity more significantly than using a one-step look-ahead, while possibly risking optimality.

## 3.3.2. Problem-specific heuristics

Differently from the above general heuristic, a problem-specific heuristic can be obtained from a decision-maker’s expertise and the problem structure. Consider loading a vessel with stocks of items whose weights and values are:

<table><tr><td>Item</td><td>Weight</td><td>Value</td></tr><tr><td>1</td><td>2</td><td>65</td></tr><tr><td>2</td><td>3</td><td>80</td></tr><tr><td>3</td><td>1</td><td>30</td></tr></table>

where the maximum weight is restricted to 5. It is required to determine the cargo loads with the most value without exceeding the maximum weight allowed.

This is a kind of deterministic dynamic programming problem, which is decomposed into stages that are mutually dependent via states. A transformal stage is determined by a current state and the decision made at the current stage. The optimal function of a deterministic dynamic programming model can be defined as follows:

$$
f (s _ {n}) = r \underset {k} {o p} \left\{a _ {s _ {n}} ^ {k} \circ f (s _ {n - 1} (s _ {n}, k)) \right\}
$$

where: r is an adjustment factor; n and $n - 1$ are stage indices; k is the decision taken at stage n; $s _ { n }$ and $s _ { n - 1 }$ are state descriptions at stage n and $n - 1$ respectively, such that $s _ { n - 1 }$ is determined by $s _ { n }$ and $k ; a _ { s _ { n } } ^ { k }$ is the expected contribution to the objectiveŽ . by taking decision k at stage n; op is a selection operator, typically max or min, set by the objective; and <sup>\`</sup> is an operator set by the stage decomposition method.The above function is recursively defined in the sense that the definition of the function includes the function itself.

In the case of the above example, each stage corresponds to decision-making for each item and the weights of items are states. Each stage involves courses of actions with costs i.e., weights and Ž . revenues i.e., values . It is represented as:Ž .

```txt
action(Stage_Token, Course_of_Tction, Cost, Revenue)
```

```txt
where Stage_Token is a serial number identifying a specific stage. Courses of actions at stages:
action(1,N,2*N,65*N):- int(N).
action(2,N,3*N,80*N):- int(N).
action(3,N,N,30*N):- int(N).
where:
int(0).
int(X):- X >= 1, int(X - 1).
The optimal solution predicate is defined as:
optimal(Stage_Token, State, O_Revenue, COAs, Alloc)
```

where State is the accumulated weights from stages 1 to Stage\_Token, O\_Revenue is the optimal revenue i.e., value , COAs represents selected coursesŽ . of actions i.e., quantities of items for stages 1 toŽ . Stage\_Token and Alloc is the maximal weight allowed in the vessel. Suppose the decision-maker has a heuristic that the cost of an action is to be less than 50% of the available resource, if the state is greater than 4. Then, the problem is structured as follows:

```txt
optimal(0,0,0,[]).
optimal(Stage_Token,State,O_Revenue,COAs,Alloc):
find all([P_O_Revenue + Revenue,P_State + Cost,
[coa(Stage_Token,Action)|P_COAs]],
(heuristic(Stage_Token,Cost,Alloc),
action(Stage_Token,Action,Cost,Revenue),
optimal(State_Token-1,P_State,
```

```txt
P_O_Revenue, P_COAs, Alloc-Cost),
P_State <= Alloc-Cost),
L),
maxof(L, [O_Revenue, State, COAs]).
heuristic(Stage_Token, Cost, Alloc):
Stage_Token > 4,
Cost < 0.5 * Alloc.
heuristic(Stage_Token, Cost, Alloc):
Stage_Token <= 4,
Cost <= Alloc.
The optimal solution of the above example is obtained as follows:
?- optimal(3, Total_Weights, Values, COAs).
Answer ⇒
COAs = [coa(3,1), coa(2,0), coa(1,2)]
Values = 160
Total_Weights = 5
That is, by loading 2 units of item 1, none of item 2,
and 1 unit of item 3 which have the total weight of 5,
one gets the maximal cargo value of 160.
```

## 3.4. Preference ordering on constraints

Often, solving a mathematical model is infeasible due to conflicts in constraints, or computationally too complex due to hard constraints. By relaxing such constraints, we may obtain applicable solutions. One way to achieve it is by preference ordering on constraints. Hierarchical constraint logic programming Ž . HCLP , an extension to CLP, achieves constraint relaxation through a hierarchical organization of constraints based on their preference 29 .<sup>w</sup> <sup>x</sup>

Relaxation of conflicting and thus unsatisfiableŽ . constraints has a special importance in the DSS context. As noted in Section 3.2, one poses constraints in order see consequences of the constraint satisfaction in model analyses. Suppose, those constraints are not satisfiable. Then, the next reasonable step is to retract them and pose weaker or relaxedŽ . constraints to continue the model analyses. HCLP performs it systematically. This improves the efficiency of a decision-maker’s model analysis efforts. The following description of preferential constraint reasoning is adapted from 29 .<sup>w</sup> <sup>x</sup>

We define a strict simple ordering i.e., asymmet- Ž ric, transitive, and complete relation . $\prec _ { c } ,$ called the constraint preference relation, such that $c _ { i } \prec _ { c } c _ { 2 }$ means a constraint $c _ { 2 }$ is strictly preferable to another constraint $c _ { 1 } ^ { \phantom { \dagger } }$ . We also define an equivalence $( \mathrm { i . e . } ,$ reflexive, symmetric, and transitive relation. $\sim _ { \mathrm { ~ c ~ } } ,$ called the constraint indifference relation, such that $c _ { 1 } c \ \sim c \ c _ { 2 }$ means $c _ { 1 }$ and $c _ { 2 }$ are indifferent. Given a set C of constraints, we obtain a partition $\pi _ { c }$ of $C$ induced by the constraint indifference relation $\sim c$ such that:

<sup>Ø</sup> For all $C _ { i } , \ C _ { j } \ \in \ \mathcal { \Pi } _ { C }$ , if $C _ { i } \neq C _ { j }$ then $C _ { i } ~ \cap$ C <sup>s</sup> Ø. <sub>j</sub>

$$
\cdot \quad \dot {\cup} _ {i} C _ {i} = C.
$$

<sup>Ø</sup> For all $c , d \in C _ { i } \in I I _ { c } , c \sim _ { c } d .$

A block of this partition is called an indifferent constraint set. We extend the definition of constraint preference relation $\prec _ { c }$ by allowing $C _ { i } ~ \prec _ { c } ~ C _ { j }$ if $c \prec _ { c }$ d for all $c \in C _ { i }$ and $d \in C _ { i } .$ Let the rank of $\textstyle \boldsymbol { \Pi } _ { C }$ be n. Then, we define a constraint preference ordering sequence:

$$
\begin{array}{l} C = \langle C _ {1}, C _ {2}, \dots , C _ {n} | C _ {i} \prec_ {c} C _ {i + 1}, \text { for } i = 1, 2, \dots , n \\ - 1 \rangle . \end{array}
$$

We define a deÕiation function:

$$
\delta : C \times \Theta \mapsto \Re^ {0 +}
$$

where C is a set of constraints, is a set of substitutions, and $\Re ^ { 0 + }$ is the set of non-negative real numbers. For example, using machine A, one can produce 3 units of product X per hour and 2 units of product Y per hour; using machine B, one can produce 2 units of product X per hour and 4 units of product Y per hour. Operations of the machines are limited to 8 h per day, though additional costs allow overtime. Say x and y denote numbers of units of products X and Y, respectively. The constraints are:

$$
\begin{array}{l} x / 3 + y / 2 \leq 8 \\ x / 2 + y / 4 \leq 8. \end{array}
$$

Let $\theta = \left\{ x / 1 2 , \ y / 1 0 \right\}$ be a substitution. Then, the deviations are:

$$
\begin{array}{l} \delta (x / 3 + y / 2 \leq 8, \theta) = 1 \\ \delta (x / 2 + y / 4 \leq 8, \theta) = 2. \end{array}
$$

We further extend the definition of the deviation function as follows:

$$
\delta : \Pi_ {C} \times \Theta \mapsto \Re^ {0 +}
$$

$$
\begin{array}{c} \delta \big (\big \{c _ {1}, c _ {2}, \ldots , c _ {k} \big \}, \theta \big) = \sigma \big \{\delta \big (c _ {1}, \theta \big), \\ \delta \big (c _ {2}, \theta \big), \ldots , \delta \big (c _ {k} \theta \big) \big \} \end{array}
$$

where $\sigma$ is an aggregation operator, such as sim- Ž ple or weighted maximization, average, summation, . or others, depending on the specific model.

Given a constraint preference ordering sequence C, we define a deÕiation sequence for a substitution as follows:

$$
\Delta [ \mathbf {C}, \theta ] = \left[ \delta (C _ {1}, \theta), \delta (C _ {2}, \theta), \dots , \delta (C _ {n}, \theta) \right].
$$

We define a lexicographic ordering relation $\prec _ { \varDelta }$ on deviation sequences as follows:

$$
\begin{array}{c} \big [   \delta (C _ {1}, \theta), \delta (C _ {2}, \theta), \ldots , \delta (C _ {n}, \theta)   \big ] \prec_ {\Delta} \big [   \delta (C _ {1}, \tau), \\ \delta (C _ {2}, \tau), \ldots , \delta (C _ {n}, \tau)   \big ] \end{array}
$$

$$
\begin{array}{l} \text { if   for   some } k \leq n, \delta (C _ {k}, \theta) <   \delta (C _ {k}, \tau) \text { and } \delta (C _ {i}, \theta) \\ = \delta (C _ {i}, \tau) \text { for } i <   k. \end{array}
$$

Suppose $C _ { k }$ is a set of constraints whose satisfaction is required. Then, $\Sigma _ { k }$ is the solution space for $C _ { k }$ :

$$
\Sigma_ {k} = \left\{\theta | \delta (C _ {k}, \theta) = 0 \right\}.
$$

The solution space for the given constraint preference ordering sequence C is as follows:

$\mathcal { Z } = \left\{ \theta \epsilon \mathcal { Z } _ { k } \right|$ <sup><</sup> there does not exist $\Sigma _ { k }$ such that $\Delta ( c ,$

$$
\left. \theta\right) \prec_ {\Delta} \Delta (C, \tau) \}
$$

Assume an HCLP language supporting the above hierarchical constraint reasoning, as an extension to CLPŽ . R , supporting the following. A labelled constraint is expressed as:

label preference level , deviation weight c,Ž .² : ² :

where c is an unlabelled constraint. A clause may contain both labelled and unlabelled constraints. The satisfaction of unlabelled constraints is required. Preference level values are declared by:

$$
\leftarrow \text { levels } ([ l _ {1}, l _ {2} \dots ])
$$

where constraints with $l _ { i }$ are preferable to those with $l _ { j } \mathrm { i f } i < j$ . The aggregation method for deviations ofŽ indifferent constraints is declared by:.

§aggregation aggregationŽ .² :

where aggregation key is either sum, average, ² : max, min, weighted\_sum, weighted\_average, weighted\_max, or weighted\_min.

The preference-based constraint reasoning can be applied to the goal programming and multi-objective linear programming. For instance, suppose the following constraints are given:

```prolog
:- levels([strong, desirable]).
:- aggregation(weighted_sum).
prob(X1,X2):
label(desirable,200) 7 * X1 + 3 * X2 >= 40,
label(strong,100) 10 * X1 + 5 * X2 >= 60,
label(desirable,50) 5 * X1 + 4 * X2 >= 35,
10 * X1 + 5 * X2 <= 60,
X1 >= 0, X2 >= 0.
Query:?-prob(X1,X2).finds values of x₁ and x₂ that satisfy constraints:
10 x₁ + 5 x₂ ≤ 60 x₁ ≥ 0 x₂ ≥ 0
and the multiple objectives in the following order of importance:
minimize max(100 · (60 - 10 x₁ - 5 x₂),0)
minimize max(200 · (40 - 7 x₁ - 3 x₂,0)
+ max(50.(35 - 5 x₁ - 4 x₂),0).
```

$$
7 x _ {1} + 3 x _ {2} \geq 4 0
$$

$$
1 0 x _ {1} + 5 x _ {2} \geq 6 0
$$

$$
5 x _ {1} + 4 x _ {2} \geq 3 5
$$

$$
1 0 0 x _ {1} + 5 0 x _ {2} \leq 6 0 0
$$

$$
x _ {1} \geq 0, x _ {2} \geq 0
$$

which are not satisfiable. As a way to relax constraints, say that the satisfaction of the fourth constraint is required and the satisfaction of the second constraint is more important than the satisfaction of the first and the third constraints which are indifferent. Then we represent the constraints under such preferences as follows:

## 4. CLP and computational efficiency

Consider an example of World Series Odds Žadopted from 1 . Two teams<sup>w</sup> <sup>x</sup>. A and B are to win n games. Let $P ( i , j )$ be a function returning the probability that A wins the match when if A wins i games, A wins the match and if B wins j games, B wins the match. Then the problem is recursively defined as:

$$
P (i, j) = \left\{ \begin{array}{l l} 1 & \text { if   } i = 0 \text {   and   } j > 0, \\ 0 & \text { if   } i > 0 \text {   and   } j = 0, \\ \frac {1}{2} P (i - 1, j) + \frac {1}{2} P (i, j - 1) & \text { if   } i > 0 \text {   and   } j > 0 \end{array} \right.
$$

```txt
The main structure of the problem is:
    win(0,J,1).
    win(I,0,0).
    win(I,J,0.5 * P1 + 0.5 * P2):
    win(I,J - 1,P2),
    win(I - 1,J,P1).
```

Calculation of $P ( m , n )$ requires $\left( { \overset { m + 1 } { \mathop { n } } } \right) - 1$ computations of $1 / 2 P ( i - 1 , j ) + 1 / 2 P ( i , j - 1 ) ,$ ,, whose complexity exponentially increases as m and n increase. For instance, the evaluation of

$$
? - \operatorname{win} (3, 3, P)
$$

requires 19 non-terminal evaluation of ‘win’ subgoals. This computational complexity i.e., computa- Ž tional inefficiency is a shortcoming of CLP in model. analyses. When a problem is structured recursively and the same patterns occur repeatedly, however, we can improve the computational efficiency controlling the resolution. Let us modify the model structure as follows.

```prolog
:- dynamic(windata,3).
win(0,J,1).
win(I,0,0).
win(I,J,P):
    windata(I,J,P),!.
win(I,J,0.5 * P1 + 0.5 * P2):
    win(I - 1,J,P1),
    win(I,J - 1,P2),
    assert(windata(I,J,0.5 * P1 + 0.5 * P2)).
```

As the result, calculation of $P ( m , n )$ requires m $\times n .$ instead of $\left( { \overset { m + 1 } { \mathop { n } } } \right) - 1$ , computations of $1 / 2 P ( i -$ $1 , j ) + 1 / 2 \overset { \cdot } { P } ( i , j - 1 )$ . That is, the evaluation of

$$
? - \operatorname{win} (3, 3, P)
$$

requires nine, instead of 19, non-terminal evaluation of $\mathbf { \dot { w i n } } / 3 \mathbf { \dot { \omega } }$ subgoals.

We can generalize this idea of re-using previously successful resolution steps in the backtracking scheme of CLP, by modifying its resolution procedure. It avoids the ad hoc use of the side-effect rule-base modification directive ‘assert’ and also reduces a modeller’s burden of model-specific implementation of efficiency-improvement procedures. It also improves the efficiency of repetitive ‘what-if and goal-seeking analyses, by reusing resolution steps of previous analyses.

![](/api/attachments/AD4B8QVU/fulltext/images/ed951f202efeb1a50707a43da8c1408376239040ed503cec858c1354899e4bb5.jpg)  
Fig. 5. Resolution tree for ‘?-a X , b Y ’.Ž . Ž .

Given a CLP program, suppose a state

$$
\sigma = \langle V, (\alpha), C \rangle
$$

can be successfully transformed to many instances of <sup>j</sup> ² <sup>j</sup> <sup>s</sup> V , ,Ž . C :

such that $C ^ { ( j ) }$ is satisfiable for $j = 1 , \ldots , \ k .$ . From this, we define a state record

$$
\rho_ {\alpha , C} = \left\langle V, \alpha , C, \left(C ^ {\prime}, C ^ {\prime \prime}, \dots , C ^ {k}\right) \right\rangle .
$$

A state record is a collection of a state’s successful transformations to final states. When a model involves a recursive structure or multiple solutions are obtained via backtracking, the re-use of previously successful state transformations can increase the computational efficiency. A state record provides a means of the efficiency improvement.

We modify state transformation methods of CLP, presented in Section 2, as follows. Suppose state is given

$$
\sigma_ {i} = \left\langle V, \left(\alpha_ {1}, \dots , \alpha_ {m}\right), C \right\rangle ,
$$

such that $C _ { i } \subseteq C$ is the set of constraints that contains variables in $\alpha _ { i } ,$ provided that constraints in $C _ { i }$ are obtained after constraints in C are simplified in terms of variables in $\alpha _ { i } .$

<sup>Ø</sup> Case 1. If there exists a state record

$$
\rho_ {\alpha_ {1}, C _ {1}} = \big \langle V, \alpha_ {1}, C _ {1}, \big (C ^ {\prime}, C ^ {\prime \prime}, \dots , C ^ {(k)} \big) \big \rangle ,
$$

then for some j we transform $\sigma _ { i }$ to

$$
\sigma_ {i + 1} = \left\langle V, \left(\alpha_ {1}, \dots , \alpha_ {m}\right), C \cup C ^ {(j)} \right\rangle .
$$

During the next backtracking on $\alpha _ { 1 } , C ^ { ( j ^ { \prime } ) } \left( j \neq j ^ { \prime } \right)$ is selected from the state record.

![](/api/attachments/AD4B8QVU/fulltext/images/7ce0d32b3138dbe5cc95a678e19b628f4eb27b3e084f6c19e8aa0d929b41d212.jpg)  
Fig. 6. Modified resolution tree for ‘?-a X , b Y ’. Ž . Ž .

![](/api/attachments/AD4B8QVU/fulltext/images/c8eec9fd03fe198e53a256b23fea31ce9b5138add8f02a4f05679a47471b256c.jpg)  
Fig. 7. Abbreviated Resolution tree for ‘?-win 3,3,P ’ Underlined subgoals are to be immediately resolved by unit clauses in the followingŽ . Ž . Ž step ..

<sup>Ø</sup> Case 2. If there does not exist such a state record:

( Step 2.A. We build a substate of $\sigma _ { 1 } \colon$

$$
\tau_ {1} = \left\langle V, \left(\alpha_ {1}\right), C _ {1} \right\rangle
$$

<sup>d</sup>Case 2 .A .1. If $\tau _ { 1 } ^ { \mathrm { ~ ~ } } \mathrm { ~ s ~ }$ post-transformation Ž . established by Step 2.A

$$
\pi \left(\tau_ {1}, \langle V, (), C ^ {(j)} \rangle\right)
$$

is available, hold $C ^ { ( j ) } .$ , remove the post-transformation, and change the pre-state record initiated inŽ Case 2.A.2.

$$
\overline {{\rho}} _ {\alpha_ {1}, C _ {1}} = \left\langle V, \alpha_ {1}, C _ {1} \left(C ^ {\prime}, C ^ {\prime \prime}, \dots , C ^ {(j - 1)}\right) \right\rangle
$$

to

$$
\overline {{\rho}} _ {\alpha_ {1}, C _ {1}} = \left\langle V, \alpha_ {1}, C _ {i} \left(C ^ {\prime}, C ^ {\prime \prime}, \dots , C ^ {(j)}\right) \right\rangle
$$

<sup>d</sup>Case 2.A.2. When $\tau _ { 1 } ^ { \mathrm { ~ \prime ~ s ~ } }$ post-transformation is not available, if it is transformed to

$$
\tau_ {1} ^ {(j)} = \langle V, (), C ^ {(j)} \rangle
$$

and the pre-state record does not exist, create one

$$
\overline {{\rho}} _ {\alpha_ {1}, C _ {1}} = \left\langle V, \alpha_ {1}, C _ {1} (C ^ {(j)}) \right\rangle
$$

<sup>d</sup>Case 2.A.3. If ${ \boldsymbol { \tau } } _ { 1 } ^ { \ \prime } { \mathrm { s } }$ post-transformation is not available and it is not transformed to

$$
\tau_ {1} ^ {(j)} = \langle V, (), C ^ {(j)} \rangle
$$

then the transformation of $\sigma _ { i }$ fails.

( Step 2.B. We perform one-step look-ahead for $\tau _ { 1 } .$

<sup>d</sup> Case 2.B.1. If $\tau _ { 1 }$ can be is transformed to $\tau _ { 1 } ^ { ( j ^ { \prime } ) } = \langle V , ( ) , C ^ { ( j ^ { \prime } ) } \rangle ,$

where $\tau _ { 1 } ^ { ( j ) } \neq \tau _ { 1 } ^ { ( j ^ { \prime } ) }$ . If it can, we save $\tau _ { 1 } ^ { \mathbf { \Upsilon } , } \mathbf { s }$ post-transformation:

$$
\pi \big (\tau_ {1}, \langle V, (), C ^ {(j ^ {\prime})} \rangle \big).
$$

<sup>d</sup> Case 2.B.2. Otherwise, the pre-state record $\overline { { \rho } } _ { \alpha 1 , C 1 }$ becomes the state record $\rho \alpha _ { 1 , C 1 }$

( Step 2.C. Now, we consider the transformation of $\sigma _ { i }$

<sup>d</sup> Case 2.C.1. If $C \cup C ^ { ( j ) }$ is satisfiable, $\sigma _ { i }$ is transformed to

$$
\sigma_ {1} + 1 = \left\langle V, \left(\alpha_ {2}, \dots , \alpha_ {m}\right), C \cup C ^ {(j)} \right\rangle .
$$

<sup>d</sup> Case 2.C.2. If $C \cup C ^ { ( j ) }$ is not satisfiable, go back to Step 2.A.

![](/api/attachments/AD4B8QVU/fulltext/images/2c1fb80933d8cb248a232d7323c627a547c1d06649deba9668f20c34df5c87f7.jpg)  
Fig. 8. Modified Abbreviated resolution tree for ‘?-win 3,3,P ’ Label in directed arcs denote state records, some of which are used later inŽ . Ž . Ž the resolution of subgoals written with boldface letters ..

For instance, assume we have a program a 1 . a 2 .Ž . Ž . b X :- c X .Ž . Ž .

c a . c b . Ž . Ž .

Fig. 5 shows the resolution tree for query ? <sup>y</sup> a XŽ . Ž . , b Y

in which a transformed state of ‘?- c ZŽ .’ appears twice. Re-using the successful transformation of the first occurrence reduces the computational requirement for the second occurrence, as illustrated in Fig. 6.

For more significant contributions of the propose method, compare Figs. 7 and 8. There are 19 nodes with non-terminal subgoals which are not under-Ž lined in Fig. 7, which are reduced to 9 nodes in Fig. . 8 by re-using successful sub-goals of win 1,2 ,Ž . win 1,1 , win 2,2 , and win 2,1 .Ž . Ž . Ž .

## 5. Concluding remarks

Constraint logic programming, a mathematical extension of logic programming or logic programming extension of mathematical programming, is considered as a potential tool for decision support systems. The declarative programming aspect and non-numeric constraint processing features, together with the numeric constraint satisfaction engines, of the constraint logic programming scheme are used for the model representation and analyses for decision supports.

The implication of declarative and procedural interpretations of clauses of constraint logic programming for decision model representations is addressed Ž . Section 3.1 . Typical forms of ‘what-if’ and goalseeking analyses with constraint logic programming in a sample option pricing model are demonstrated Ž . Section 3.2 . The constraint logic programming scheme can extend mathematical programming, by allowing simple implementations of general or problem-specific heuristics Section 3.3 and allowingŽ . preference-based reasoning of constraints Section Ž 3.4 . Finally, some consideration on computational. efficiencies is addressed Section 4 .Ž .

## References

<sup>w</sup> <sup>x</sup> 1 A.V. Aho, J.E. Hopcroft, J.D. Ullman, Data Structures and Algorithms, Addision-Wesley, Reading, MA, 1983.

<sup>w</sup> <sup>x</sup> 2 K.R. Apt, Introduction to logic programming, Technical Report TR-87-35 Revised and Extended Version , Depart-Ž . ment of Computer Science, The University of Texas at Austin, 1988.

<sup>w</sup> <sup>x</sup> 3 J. Cohen, Constraint logic programming languages, Commun. ACM 33 7 1990 52–68.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 A. Colmerauer, An introduction to Prolog III, Commun. ACM 33 7 1990 69–90.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 R. Fourer, D.M. Gay, B.W. Kernighan, A modelling language for mathematical programming, Manage. Sci. 36 5Ž . Ž . 1990 519–554.

<sup>w</sup> <sup>x</sup> 6 A.M. Geoffrion, An introduction to structured modelling, Manage. Sci. 33 5 1987 547–588.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 N.C. Heintze, S. Michaylov, P.J. Stuckey, CLPŽ . R and some electrical engineering problems, in: Proceedings of the Fourth International Conference on Logic Programming, Melbourne, Australia, 1987, pp. 675–703.

<sup>w</sup> <sup>x</sup> 8 K. Hiraishi, A constraint logic programming language Keyed CLP and its applications to decision making problems in OR<sup>\_</sup>MS, Decision Support Syst. 14 5 1995 269–281.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 S.N. Hong, M.V. Mannino, B.S. Greenberg, Inheritance and instantiation in model management, in: Proceedings of the Twenty-Third Annual Hawaii International Conference on System Sciences, vol. 3, 1990.

<sup>w</sup> <sup>x</sup> 10 J. Jaffar, J.L. Lassez, Constraint logic programming, in: Proceedings of the Fourteenth ACM Symposium of the Principles of Programming Languages, Munich, Germany, 1987, pp. 111–119.

<sup>w</sup> <sup>x</sup> 11 J. Jaffar, S. Michaylov, Methodology and implementation of a CLP system, in: Proceedings of the Fourth International Conference on Logic Programming, Melbourne, Australia, 1987, pp. 196–218.

<sup>w</sup> <sup>x</sup> 12 J. Jaffar, S. Michaylov, P.J. Stuckey, R. Yap, The CLPŽ . R language and system, ACM Tran. Programming Languages Syst. 14 3 1992 339–395.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 R. Kowalski, Predicate logic as programming language, in: J.L. Rosenfeld, Ed. , Proceedings of IFIP 74, 1974, pp. Ž . 569–574.

<sup>w</sup> <sup>x</sup> 14 C. Lassez, K. McAloon, R. Yap, Constraint logic programming and option trading, IEEE Expert 2 3 1987 42–50.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 H.G. Lee, R.M. Lee, G. Yu, Constraint logic programming and mixed integer programming, in: Proceedings of the Twenty-Sixth Annual Hawaii International Conference on System Sciences, vol. 3, 1993, pp. 543–553.

<sup>w</sup> <sup>x</sup> 16 H.G. Lee, R.M. Lee, G. Yu, Constraint logic programming for qualitative and quantitative constraint satisfaction problems, Decision Support Syst. 6 1 1996 67–83.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 J.W. Lloyd, Foundations of Logic Programming, Springer-Verlag, Berlin, Germany, 2nd edn., 1987.

<sup>w</sup> <sup>x</sup> 18 M.V. Mannino, B.S. Greenberg, S.N. Hong, Knowledge representation for model libraries, in: Proceedings of the Twenty-First Annual Hawaii International Conference on System Sciences, vol. 3, 1988, pp. 349–355.

<sup>w</sup> <sup>x</sup> 19 R. Marcus, An artificial intelligence to operations research, Commun. ACM 27 10 1984 1044–1047. Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 H.J. Nilsson, Principles of Artificial Intelligence, Morgan Kaufmann, Palo Alto, CA, 1980.

<sup>w</sup> <sup>x</sup> 21 E. Rich, K. Knight, Artificial Intelligence, McGraw-Hill, New York, 2nd edn., 1991.

<sup>w</sup> <sup>x</sup> 22 J.A. Robinson, A machine-oriented logic based on the resolution principle, J. ACM 12 1 1965 23–41.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 G. Sidebottom, W.S. Havens, Hierarchical arc consistency for disjoint real intervals in constraint logic programming, Technical Report CSS-IS-92-16, Centre for Systems Science, Simon Fraser University, 1992.

<sup>w</sup> <sup>x</sup> 24 S. Sidebottom, W.S. Havens, S. Kindersley, Echidna Constraint Reasoning System: Programming Manual, Expert Systems Laboratory, Centre for Systems Science, Simon Fraser University, 1992.

<sup>w</sup> <sup>x</sup> 25 R.H. Sprague Jr., E.R. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, 1982.

<sup>w</sup> <sup>x</sup>26 A. Tarski, A Decision Method for Elementary Algebra and Geometry, University of California Press, Berkeley, CA, 2nd edn., 1948.

<sup>w</sup> <sup>x</sup> 27 P. van Hentenryck, Constraint Satisfaction in Logic Programming, MIT Press, Cambridge, MA, 1989.

<sup>w</sup> <sup>x</sup> 28 P. van Hentenryck, H. Simonis, M. Dincbas, Constraint satisfaction using constraint logic programming, Artificial Intelligence 58 1–3 1992 113–159.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 M. Wilson, A. Borning, Hierarchical constraint logic programming, J. Logic Programming 16 3–4 1993 277–318.Ž . Ž .

![](/api/attachments/AD4B8QVU/fulltext/images/668f239c13e0bfdb157f6979c5954a40c086f609d0f15806eca1f0e1805b8e87.jpg)

Young U. Ryu has been Assitant Professor of Information Systems at the Department of Decision Sciences, The University of Texas at Dallas since 1992. He received a Ph. D. degree in Management Science and Information System from The University of Texas at Austin, where he had been Assistant Instructor for four years. His research interests include logic-based modeling of normative systems, automation of legal decision making procedures, defeasible rea-

soning, artificial intelligence applications, and constraint logic modeling of systems.
