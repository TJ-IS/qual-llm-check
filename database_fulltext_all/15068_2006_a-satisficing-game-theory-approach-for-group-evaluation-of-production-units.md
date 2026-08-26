---
otero_id: 15068
otero_key: "MWU4TWYK"
title: "A satisficing game theory approach for group evaluation of production units"
authors: "A.P. Tchangani"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.05.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A satisficing game theory approach for group evaluation of production units

A.P. Tchangani \*

Dept. GEII, IUT de Tarbes, Universite Toulouse III-Paul Sabatier, 1, rue Lautreamont, 65016 Tarbes Cedex, France Equipe Production Automatisee-Laboratoire Genie de Production, 47, Avenue d’Azereix-BP 1629-65016 Tarbes Cedex, France

Received 21 November 2003; received in revised form 18 January 2005; accepted 5 May 2005 Available online 14 June 2005

## Abstract

The problem under consideration in this paper is that of analysing the performance of a production unit in two directions: resource utilization versus output perfomance on the one hand and inter-unit comparison (within-group evaluation) on the other hand, all this subjected to possible subjective intervention of a decision maker or group of decision makers (DMs). A well known method that deals mainly with the second point (without intervention of DMs) of this problem which is widely covered in the literature is the so called data envelopment analysis (DEA). The point of view that will be expressed in this paper can be thought of as complementary to the DEA approach giving a more complete analysis in terms of the weak points of units identification and DMs’ recommendations. The performance of each decision unit is evaluated through the so called satisfiability functions in the framework of satisficing game theory. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Production systems; Performance analysis; Efficiency evaluation; Group evaluation; DEA; Satisficing game theory

## 1. Introduction

The problem of evaluating production units’ performance is of great importance for efficient management decision making such as restructuring an organization, rewarding production teams, etc. We understand by production unit, a system that utilizes some input items (resources) to produce some goods or to deliver some service. It could be a hospital, a manufacturing plant, a university, a police department, etc. The purpose here is to evaluate the efficiency in terms of resource utilization versus output performance of each production unit of an organization U that consists of n production units. Each production unit is evaluated individually as well as with regard to its counterparts’ efficiency. We suppose that each unit of U uses p input items expressed as positive numbers I <sup>j</sup> (value of item j used by unit i) to deliver m output items valued by O<sub>i</sub> (value of item j produced by unit i).

A first idea could be to define the efficiency $e _ { i }$ of unit i by

$$
e _ {i} = \frac {\sum_ {j = 1} ^ {m} O _ {i} ^ {j}}{\sum_ {j = 1} ^ {p} I _ {i} ^ {j}};\tag{1}
$$

but this definition leads to some problems as all input items or output items do not have the same importance in practice. It is then tempting to weight items in order to take into account this relative importance so that the efficiency is defined by

$$
e _ {i} = \frac {\sum_ {j = 1} ^ {m} \alpha_ {i} ^ {j} O _ {i} ^ {j}}{\sum_ {j = 1} ^ {p} \beta_ {i} ^ {j} I _ {i} ^ {j}}, \alpha_ {i} ^ {j}, \beta_ {i} ^ {j} > 0;\tag{2}
$$

but here again, a problem relative to the determination of weights $\boldsymbol { \alpha } _ { i } ^ { j }$ and $\beta _ { i } ^ { j }$ is raised.

A method to deal with the determination of these weights in the literature is the so called data envelopment analysis (DEA) established by [1]. It is an extreme point method that determines weights $\boldsymbol { \alpha } _ { i } ^ { j }$ and $\beta _ { i } ^ { j }$ in order to define a relative efficiency of each unit compared to the best production unit (possibly virtual) by solving n linear programs (see for instance [2] for definition of linear programming concepts).

But this approach has some technical drawbacks that will be recalled in the next Section and more importantly, we consider that the spirit of comparing each unit to the <sup>b</sup>best unit<sup>Q</sup> is not necessarily how humans proceed in practice. They often evaluate each unit firstly with regard to how efficiently it uses its resources to produce its output and secondly they look at how good this unit is compared to its counterparts. If we think of how students are evaluated, we see that each student is first evaluated individually (their marks reflecting the effort they have made) and then compared to the best student of the same class. This observation suggests that a production unit should be evaluated by comparing its positive attributes (output performance) to its negative attributes (input or resource consumption) at first and with regard to the other units in a second stage.

Another important issue in the process of evaluating production units is the possible existence of different decision makers that do not have the same point of view regarding the importance of input items and/or output items and this constraint should be taken into account. A framework that seems interesting to tackle this problem with is the recently developed satisficing game theory [3] that, basically for our problem, will consist in defining selectability (with regard to output items) and rejectability (with regard to input items) functions known as satisfiability functions. These functions must have a probability structure (they are non-negative and sum to one on U) which can be thought of as units sharing a unity of input item to produce a unity of output item. An efficient production unit will be that for which the selectability is at least equal to the rejectability. We consider here that there are $d$ decision makers that express their point of view regarding input items and output items by weighting them.

The remainder of this paper is organized as follows: in the Second section the DEA method is briefly presented with its strengths and its drawbacks; the Third section is devoted to a rapid presentation of satisficing game theory that is relevant to our problem and the Fourth section shows how to cast performance evaluation problems into the framework of this theory and finally, in Section five, the approach we have established is applied to a real world problem.

## 2. Data envelopment analysis

Data envelopment analysis (DEA) is a technique for assessing and ranking the performance of corporations, research projects or other entities where an entire array of indicators of performance are to be evaluated. It was invented by [1] and is a linear programming based technique for measuring the relative performance of organizational units where the presence of multiple inputs and outputs makes comparisons dificult. It is an extreme point method and compares each producer (also known in the DEA literature as decision making unit or DMU) with only the <sup>b</sup>best<sup>Q</sup> producer (possibly virtual). A fundamental assumption behind the DEA method is that if a given producer, $A ,$ is capable of producing Y(A) units of output with X(A) inputs, then other producers should also be able to do the same if they were to operate efficiently. Similarly, if producer B is capable of producing Y(B) units of output with X(B) inputs, then other producers should also be capable of the same production schedule. Producers A, B, and others can then be combined to form a composite producer with composite inputs and composite outputs. Since this composite producer does not necessarily exist, it is sometimes called a virtual producer. The heart of the analysis lies in finding the <sup>b</sup>best<sup>Q</sup> virtual producer for each real producer. If the virtual producer is better than the original producer by either making more output with the same input or making the same output with less input then the original producer is inefficient. The DEA method has been applied in many situations such as: health care (hospitals, doctors), education (schools, universities), banks, manufacturing, benchmarking, management evaluation, fast food restaurants, retail stores, police departments (see for instance [8,9,6, 4,5,7]).

The procedure of finding the best virtual producer can be formulated as a linear program. Analyzing the efficiency of n producers then requires solving n linear programming problems. The following formulation is one of the standard forms for the DEA. We consider that there are n producers, p input items and m output items for each producer; the value of input item j and the value of output item l for producer i are $I _ { i } ^ { j }$ and $O _ { i } ^ { j }$ respectively. The n linear programming problems to be solved are

$$
\max _ {\alpha_ {i} ^ {j}, \beta_ {i} ^ {j}} \sum_ {j = 1} ^ {m} \alpha_ {i} ^ {j} O _ {i} ^ {j}
$$

$$
\sum_ {l = 1} ^ {m} \alpha_ {i} ^ {l} O _ {k} ^ {l} - \sum_ {j = 1} ^ {p} \beta_ {k} ^ {j} I _ {k} ^ {j} \leq 0, 1 \leq k \leq n, k \neq i\tag{3}
$$

$$
\sum_ {j = 1} ^ {p} \beta_ {i} ^ {j} I _ {i} ^ {j} = 1
$$

a<sup>l</sup><sub>i</sub> b <sup>j</sup><sub>i z</sub>e; 1ViVn; 1VlVm; 1VjVp

1ViVn

where e denotes a small strictly positive real number.

## 2.1. Strengths of the DEA

The power of the DEA as a tool for performance evaluation is due to the following characteristics.

<sup>!</sup> DEA can handle multiple input and multiple output models.

<sup>!</sup> It doesn’t require an assumption of a functional form relating inputs to outputs.

<sup>!</sup> DMUs are directly compared against the best (possibly virtual) DMU.

<sup>!</sup> Inputs and outputs can have very different units.

## 2.2. Limitations of the DEA

But the DEA method does have a number of drawbacks reported in the literature (see [8]) among which are the following concerns.

<sup>!</sup> A judicious choice of weights will lead to a high proportion of units being efficient.

<sup>!</sup> A unit which has the highest ratio of one of the outputs to one of the inputs will be efficient, or have an efficiency which is very close to one by putting as much weight as possible on that ratio and the minimum weight (e) on the other inputs and outputs.

<sup>!</sup> A unit can appear efficient simply because of its pattern of inputs and outputs and not because of any inherent efficiency.

<sup>!</sup> Since DEA is an extreme point technique, noise (even symmetrical noise with zero mean) such as measurement error can cause significant problems.

<sup>!</sup> Since a standard formulation of the DEA creates a separate linear program for each DMU, large problems can be computationally intensive.

In the next Section, we will briefly present the concepts of satisficing game theory on which we will build the approach that constitutes the purpose of this paper.

## 3. Satisficing game theory

The underlying philosophy of the DEA approach for performance evaluation is superlative rationality i.e., looking for the best. But the superlative rationality paradigm is not necessarily the way humans evaluate options (and maybe not the best one). Most of the time humans content themselves with options that are just <sup>b</sup>good enough<sup>Q</sup>; the concept of being good enough allows a certain flexibility because one can always adjust one’s aspiration level. On the other hand, decision makers more probably tend to classify units as good enough or not good enough in terms of their positive attributes (benefit) and their negative attributes (cost) with regard to the evaluation goal instead of ranking units with regard to each other. For instance, to evaluate cars, we often make a list of positive attributes (driving comfort, speed, robustness, etc.) and a list of negative attributes (price, petrol consumption, maintainability, etc.) of each car and then make a list of cars for which positive attributes <sup>b</sup>exceed<sup>Q</sup> negative attributes in some sense. This way of evaluation falls into the framework of praxeology or the study of the theory of practical activity (the science of efficient action) derived from epistemic logic (the branch of philosophy that classifies propositions on the basis of knowledge and belief regarding their content; for a proposition to be admissible it must be both believable and informative) and developed by [3]. Here decision maker(s), instead of looking for the best options, look for the satisficing options.

Satisficing is a term that refers to a decision making strategy where options, units or alternatives are selected which are <sup>b</sup>good enough<sup>Q</sup> instead of being the best [3]. Let us consider a universe $U$ of options, alternatives or units; then for each unit u $\in \mathcal { U } ;$ a selectability function $p _ { S } ( u )$ and a rejectability function $p _ { R } ( u )$ are defined so that $p _ { S } ( u )$ measures the degree to which u works towards success in achieving the decision maker’s goal and $p _ { R } ( u )$ is the cost associated with this unit. This pair of measures called satisfiability functions must have the mathematical structure of probabilities [3]: they are non-negative and sum to one on $\mathcal { U } .$ The following definition then gives the set of options which can be considered to be <sup>b</sup>good enough<sup>Q</sup> because, for these options, the <sup>b</sup>benefit<sup>Q</sup> expressed by the function $p _ { S }$ exceeds the <sup>b</sup>cost<sup>Q</sup> expressed by the function $p _ { R }$ with regard to an index of caution $q .$

Definition 1. The satisficing set $\Sigma _ { q } \subseteq \mathcal { U }$ is the set of units defined by

$$
\Sigma_ {q} = \{u \in \mathcal {U}: p _ {S} (u) \geq q p _ {R} (u) \}.\tag{4}
$$

But for a satisficing unit u there can exist other satisficing units that are better (having more selectability and at most the same rejectability or having less rejectability and at least the same selectability) than $u ;$ it is obvious that in this case any rational decision maker will prefer the latter units. So the interesting set is that containing satisficing units for which there are no better units: this is called the satisficing equilibrium set $\mathcal { E } _ { q } ^ { S } .$ . To define this set, let us define first, for any unit $u \in { \mathcal { U } }$ the set $B ( u )$ of units that are strictly better than u

$$
\mathcal {B} (u) = \mathcal {B} _ {S} (u) \cup \mathcal {B} _ {R} (u),\tag{5}
$$

where ${ \cal B } _ { S } ( u )$ and $B _ { R } ( u )$ are defined as:

$$
\mathcal {B} _ {S} (u) = \{v \in \mathcal {U}: p _ {_ R} (v) <   p _ {_ R} (u) \text { and } p _ {_ S} (v) \geq p _ {_ S} (u) \},
$$

$$
\mathcal {B} _ {R} (u) = \{v \in \mathcal {U}: p _ {_ R} (v) \leq p _ {_ R} (u) \text { and } p _ {_ S} (v) > p _ {_ S} (u) \}.
$$

The equilibrium set E (units for which there are no strictly better units) is defined by

$$
\mathcal {E} = \{u \in \mathcal {U}: \mathcal {B} (u) = \emptyset \}\tag{6}
$$

and then the satisficing equilibrium set, $\mathcal { E } _ { q } ^ { S } ,$ , is given by

$$
\mathcal {E} _ {q} ^ {S} = \mathcal {E} \cap \Sigma_ {q}.\tag{7}
$$

In the next Section we will establish a method that puts the problem of evaluating the performance of production units, as defined in the introduction Section, into the satisficing game theory framework by defining satisfiability functions $p _ { S } ( u )$ and $p _ { R } ( u )$ for each unit u.

## 4. Satisficing performance analysis

## 4.1. Necessary data computation

In the real world, decisions are made by a certain number of decision makers; this is the problem of group decision making. For instance, strategic decisions in an enterprise are taken by the executive board members that can comprise general manager, marketing manager, production manager, financial manager etc.; political decisions such as choosing a place to build a new facility (school, hospital, airport, waste management utilities, etc.), financing projects, etc. are made most of the time by an elected council. In the case of evaluation we will talk about group evaluation. The fundamental characteristic of group evaluation is the possible conflicting interests among DMs in terms of importance to assign to each input item as well as to each output item. Our purpose in this paper is to derive a method that integrates the different points of view of the DMs expressed through weights assigned to items by each DM. We assume that d DMs express their preference with regard to input items and output items through the following weights defined on the same scale for each class of items; but the scale does not need to be the same for input items and output items:

$\cdot \ \rho _ { k j } ( k { = } 1 , \ 2 , \ . . , \ d ; \ j { = } 1 , \ 2 , \ . . , \ m )$ is the weight assigned by the DM k to the output item $j ;$ the more selectable the item j is, in the view of the DM $k ,$ the more important is the weight $\rho _ { k j } ,$

$\sigma _ { k j } ( k { = } 1 , \ 2 , \ . . , \ d ; \ j { = } 1 , \ 2 , \ . . , \ p )$ is the weight assigned by the DM k to the input item $j ;$ the more rejectable the item j is, in the view of the DM $k ,$ the more important is the weight $\sigma _ { k j }$

We think that it is easier to ask DMs to compare items in order to express their preferences rather than to compare units as is often done in the multi criteria decision literature. These weights are then combined to define selectability weights $\omega _ { j } ^ { S }$ and rejectability weights $\omega _ { j } ^ { R }$ by taking the mean value over the DMs’ preferences:

$$
\omega_ {j} ^ {S} = \frac {\sum_ {k = 1} ^ {d} \rho_ {k j}}{\sum_ {j = 1} ^ {m} \sum_ {k = 1} ^ {d} \rho_ {k j}} \text {   and   } \omega_ {j} ^ {R} = \frac {\sum_ {k = 1} ^ {d} \sigma_ {k j}}{\sum_ {j = 1} ^ {p} \sum_ {k = 1} ^ {d} \sigma_ {k j}}.\tag{8}
$$

The weights $\omega _ { j } ^ { S }$ and $\omega _ { j } ^ { R }$ measure the aggregate strength that DMs accord to the output item $j$ and the input item j respectively with regard to other items of the same category. Let us define $\omega ^ { S }$ and $\omega ^ { R }$ as row vectors

$$
\omega^ {S} = \left[ \begin{array}{c c c} \omega_ {1} ^ {S} & \omega_ {2} ^ {S} \dots \omega_ {m} ^ {S} \end{array} \right] \text {   and   } \omega^ {R} \left[ \begin{array}{c c c} \omega_ {1} ^ {R} & \omega_ {2} ^ {R} \dots \omega_ {p} ^ {R} \end{array} \right],
$$

and functions $g _ { S } ( u )$ and $g _ { R } ( u )$ for each unit $u \in U$ that work toward globally selecting u or globally rejecting u respectively as follows

$$
g _ {S} (u) = \omega^ {S} \mathbf {o} _ {u} \mathrm{and} g _ {R} (u) = \omega^ {R} \mathbf {i} _ {u}\tag{9}
$$

where $\mathbf { 0 } _ { u }$ and $\mathbf { i } _ { u } ,$ , defined by

$$
\mathbf {0} _ {u} = \left[ \frac {O _ {u} ^ {1}}{\max _ {x \in \mathcal {U}} \left(O _ {x} ^ {1}\right)} \frac {O _ {u} ^ {2}}{\max _ {x \in \mathcal {U}} \left(O _ {x} ^ {2}\right)} \dots \frac {O _ {u} ^ {m}}{\max _ {x \in \mathcal {U}} \left(O _ {x} ^ {m}\right)} \right] ^ {T}
$$

and

$$
\mathbf {i} _ {u} = \left[ \frac {I _ {u} ^ {1}}{\max _ {x \in \mathcal {U}} \left(I _ {x} ^ {1}\right)} \frac {I _ {u} ^ {2}}{\max _ {x \in \mathcal {U}} \left(I _ {x} ^ {2}\right)} \dots \frac {I _ {u} ^ {p}}{\max _ {x \in \mathcal {U}} \left(I _ {x} ^ {p}\right)} \right] ^ {T},
$$

are normalized column vectors of output and input items of unit u respectively and $\boldsymbol { x } ^ { T }$ stands for the transpose of the vector x. A normalization process (dividing each item value by the corresponding maximum value) is necessary before weighting because items do not necessarily have the same units (money, human resources, surface area, machines, etc.). The following definition then gives important data by which the performance of each unit can be analyzed in different ways (individual efficiency, efficiency within the group) in order to suggest possibilities for improving performance.

Definition 2. The satisfability functions $p _ { S }$ and $p _ { R }$ are defined by

$$
\begin{array}{l} p _ {S} (u) = \frac {g _ {S} (u)}{\sum_ {x \in \mathcal {U}} g _ {S} (x)} \text { and } \\ p _ {R} (u) = \frac {g _ {R} (u)}{\sum_ {x \in \mathcal {U}} g _ {R} (x)}, \forall u \in \mathcal {U}; \end{array}\tag{10}
$$

the set of efficient units (individual efficiency) $\boldsymbol { \Sigma }$ is defined by

$$
\Sigma = \{u \in \mathcal {U}: p _ {S} (u) \geq p _ {R} (u) \}\tag{11}
$$

and the efficient equilibrium set $\boldsymbol { S }$ (within-group efficiency) by

$$
\mathcal {S} = \Sigma \cap \mathcal {E}, \mathcal {E} = \{u \in \mathcal {U}: \mathcal {B} (u) = \emptyset \}\tag{12}
$$

where $B ( u )$ is defined as in Eq. (5) of the second section.

It is worth noticing that $p _ { S }$ and $p _ { R }$ both have a probability structure. The three sets $\Sigma , \mathcal { E }$ and S as well as $B ( u )$ (for each unit u) are the important data for performance evaluation purposes. An important question that can be raised at this stage is that of the coherency of this method: that is, if there is a unit that uses more input items to produce less output items than another unit, is there a chance that the former unit be declared as an efficient equilibrium unit? Let us consider the following definition that formalizes this idea.

Definition 3. A unit $u \in \mathcal { U }$ dominates a unit $\nu \in \mathcal { U } ,$ noted $u \succeq \nu ,$ if and only if the following inequalities

$$
O _ {u} ^ {i} \geq O _ {v} ^ {i} a n d I _ {u} ^ {j} \leq I _ {v} ^ {j}
$$

hold for any output item i and any input item j with at least one strict inequality.

The following theorem establishes the coherency of the method: a dominated unit cannot be declared as an efficient equilibrium unit.

Theorem 1. Let u and v belong to U. Then $u \succeq \nu ^ { \Rightarrow } u$ $\in \mathcal { B } ( \nu )$ and so vgE.

Proof. $u \succeq \nu \Rightarrow O _ { u } ^ { j } \geq O _ { \nu } ^ { ~ j }$ and $I _ { u } ^ { j } { \le } I _ { \nu } ^ { j }$ with at least one strict inequality. As item values are assumed to be positive and $\omega _ { j } ^ { \bar { S } } \geq 0 , \omega _ { j } ^ { R } \geq 0$ , we have $\textstyle \sum _ { j = 1 } ^ { m } \omega _ { j } ^ { S } \bigl ( \hat { O } _ { u } ^ { j } /$ $\begin{array} { r } { m a x _ { x } \in \mathcal { U } ( O _ { x } ^ { j } ) ) \geq \sum _ { j = 1 } ^ { m } \omega _ { j } ^ { S } ( O _ { \nu } ^ { j } /  } \end{array}$ max $_ { x \in \mathcal { U } } ( O _ { \nu } ^ { j } ) )$ and $\begin{array} { r } { \sum _ { j = 1 } ^ { m } \omega _ { j } ^ { R } \left( I _ { u } ^ { j } / \operatorname* { m a x } _ { x \in \mathcal { U } } \left( I _ { x } ^ { j } \right) \right) \leq \sum _ { j = 1 } ^ { p } \omega _ { j } ^ { R } \left( I _ { \nu } ^ { j } / \operatorname* { m a x } _ { x \in \mathcal { U } } \left( I _ { x } ^ { j } \right) \right) } \end{array}$ $( I _ { \nu } ^ { j } ) )$ that is $\mathrm { g } _ { \mathrm { s } } ( u ) { \geq } g _ { S } ( \nu )$ and $g _ { R } ( u ) { \le } g _ { R } ( \nu )$ and finally $p _ { S } ( u ) { \geq } p _ { S } ( \nu )$ and $p _ { R } ( u ) { \leq } p _ { R } ( \nu )$ with at least one strict inequality so $u \in B ( \nu )$ , that is $B ( \nu ) { \neq } \emptyset$ and v is not an equilibrium. 5

We are now ready to perform a performance evaluation and to establish the performance improvement recommendation procedure.

## 4.2. Performance analysis

Necessary information for performance analysis by DMs is summarized in the sets R, E and S as well as $B ( u )$

<sup>!</sup> The units of the set S are those one can qualify as <sup>b</sup>good enough<sup>Q</sup>; they use their resources efficiently in comparison to their counterparts both individually as well as within the organization.

<sup>!</sup> R is the set of units that use their resources efficiently (individually) to produce their outputs but not necessarily in the best way. If a unit $u \not \in$ R, one can do a sort of sensitivity analysis to determine the way to render it efficient by computing the amount by which it must increase its output items and the amount by which it must reduce its input items in order to be efficient if other units’ performances remain unchanged. To do so, one can compute sensitivity parameters $\delta _ { u } ^ { i } { \ge } 0 , i { = } 1 , 2 , . . , m$ and $\gamma _ { u } ^ { \ i } { \geq } 0 , i { = } 1 , 2 , . . , p ,$ such that, if one replaces $\mathbf { 0 } _ { u } ( i )$ and $\mathbf { i } _ { u } ( i )$ by $\mathbf { 0 } _ { u } ( i ) + \delta _ { u } ^ { \phantom { \dagger } i }$ and $\mathbf { i } _ { u } ( i ) - \gamma _ { u } ^ { i } .$ , respectively, under the conditions

$$
0 <   \mathbf {o} _ {u} (i) + \delta_ {u} ^ {i} \leq 1 \text { and } 0 <   \mathbf {i} _ {u} (i) - \gamma_ {u} ^ {i} \leq 1
$$

then

$$
p _ {S} (u) \geq p _ {R} (u).
$$

One can find these parameters by solving the following nonlinear program Eq. (13),

$$
\begin{array}{l} \min _ {\delta_ {u}, \gamma_ {u}} 0 \\ C _ {o} (\delta_ {u}) \geq C _ {i} (\gamma_ {u}), \\ s. t. \varepsilon_ {o} \leq \mathbf {o} _ {u} + \delta_ {u} \leq 1, \delta_ {u} \geq 0, \\ \varepsilon_ {i} \leq \mathbf {i} _ {u} - \gamma_ {u} \leq 1, \gamma_ {u} \geq 0, \end{array}\tag{13}
$$

where

$$
\delta_ {u} = \left[ \delta_ {u} ^ {1} \delta_ {u} ^ {2}... \delta_ {u} ^ {m} \right] ^ {T}, \gamma_ {u} = \left[ \gamma_ {u} ^ {1} \gamma_ {u} ^ {2}... \gamma_ {u} ^ {p} \right] ^ {T}
$$

and 1 (respect. 0) is a column vector with appropriate dimension and all entries equal to 1 (respect. 0); $\scriptstyle { \varepsilon _ { 0 } }$ and $\varepsilon _ { \mathrm { i } }$ are vectors with appropriate dimensions expressing lower bounds on output items and input items respectively; s.t. stands for <sup>b</sup>subjected $\mathrm { { t o } ^ { \circ } ; }$ ; and finally

$$
\begin{array}{l} C _ {o} (\delta_ {u}) = \frac {\omega^ {S} (\mathbf {o} _ {u} + \delta_ {u})}{\sum_ {v \in \mathcal {U} , v \neq u} \omega^ {S} \mathbf {o} _ {u} + \omega^ {S} (\mathbf {o} _ {u} + \delta_ {u})}, \\ C _ {i} (\gamma_ {u}) = \frac {\omega^ {R} (\mathbf {i} _ {u} - \gamma_ {u})}{\sum_ {v \in \mathcal {U} , v \neq u} \omega^ {R} \mathbf {i} _ {v} + \omega^ {R} (\mathbf {i} _ {u} - \gamma_ {u})}. \end{array}
$$

Notice that this program is in a very general form and other constraints can be added to take into account practical requirements such as uniform distribution of effort for a class of items for instance, or on the contrary concentrating the effort on some particular items. This analysis is well suited for units of the set ${ \mathcal { E } } - S$ (units for which there is no other units that perform better but which use inefficiently their resources individually); $\frac { \delta _ { u } ( i ) } { o _ { u } ( i ) }$ and $\frac { \gamma _ { u } ( j ) } { i _ { u } ( j ) }$ are the amount by which unit u must increase its output item $i ,$ and the amount by which it must reduce its input item $j ,$ respectively, when performances of all other units remain unchanged, in order to be efficient.

<sup>!</sup> Sets B(u) may be of great importance to DMs because they can use them to identify weak points of inefficient units and possible causes of this weakness. For instance if $u ^ { * } \in B ( u )$ ; by comparing the environments in which these units are operating, one can identify why unit $u ^ { * }$ is performing better than unit u and take an appropriate decision with regard to u (make recommendations to u in order to improve its performance; stop its activity, etc.) mainly for those units of the set $\Sigma - S . \mathrm { A }$ procedure similar to that presented in the previous point can be used by u to look for how to perform as good as $u ^ { * }$ , that is, determine parameters $\delta _ { u } ^ { u * }$ ; and $\stackrel { - } { \gamma } { } _ { u } ^ { u * }$ (defined as $\delta _ { u }$ and $\gamma _ { u }$ respectively in the previous point) so that

$$
p _ {S} (u) = \frac {\omega^ {S} \left(o _ {u} + \delta_ {u} ^ {u ^ {*}}\right)}{\sum_ {v \in \mathcal {U} , v \neq u} \omega^ {S} \mathbf {0} _ {v} + \omega^ {S} \left(\mathbf {0} _ {u} + \delta_ {u} ^ {u ^ {*}}\right)} = p _ {S} \left(u ^ {*}\right)
$$

$$
p _ {R} (u) = \frac {\omega^ {R} \left(\mathbf {i} _ {u} - \gamma_ {u} ^ {u ^ {*}}\right)}{\sum_ {v \in \mathcal {U} , v \neq u} \omega^ {R} \mathbf {i} _ {v} + \omega^ {R} \left(\mathbf {i} _ {u} - \gamma_ {u} ^ {u ^ {*}}\right)} = p _ {R} \left(u ^ {*}\right)
$$

which can be done by solving the following linear programming problem

$$
\begin{array}{l} \min _ {\delta_ {u} ^ {u *}, \hat {\gamma} _ {u} ^ {u *}} 0 \\ \omega^ {S} \delta_ {u} ^ {u *} = \frac {p _ {S} (u *) (\sum_ {v \in \mathcal {U}} \omega^ {S} \mathbf {o} _ {v}) - \omega^ {S} \mathbf {o} _ {u}}{1 - p _ {S} (u *)}, \\ s. t. \quad \omega^ {R} \gamma_ {u} ^ {u *} = - \frac {p _ {R} (u *) (\sum_ {v \in \mathcal {U}} \omega^ {R} \mathbf {i} _ {v}) - \omega^ {R} \mathbf {i} _ {u}}{1 - p _ {R} (u *)}, \\ \varepsilon_ {o} \leq \mathbf {o} _ {u} + \delta_ {u} ^ {u *} \leq 1, \varepsilon_ {i} \leq \mathbf {i} _ {u} - \gamma_ {u} ^ {u *} \leq 1, \delta_ {u} ^ {u *} \geq 0, \gamma_ {u} ^ {u *} \geq 0. \end{array}\tag{14}
$$

One may then recommend to a dominated unit u to improve its output items by $\delta _ { \mathrm { u } } ^ { * }$ and reduce its input items by $\gamma _ { u } ^ { * } .$ , for instance, with $\delta _ { u } ^ { * }$ and $\gamma _ { u } ^ { * }$ defined by

$$
\delta_ {u} ^ {*} = \max _ {u ^ {*} \in \mathcal {B} (u)} \left(\delta_ {u} ^ {u ^ {*}}\right) \text {   and   } \gamma_ {u} ^ {*} = \max _ {u ^ {*} \in \mathcal {B} (u)} \left(\gamma_ {u} ^ {u ^ {*}}\right)\tag{15}
$$

where the maximum is taken componentwise.

<sup>!</sup> The set $\mathcal { U } - \Sigma \cup \mathcal { E }$ contains completely inefficient units; they do not use their resources efficiently and do less than some other counterparts.

Remark 1. Notice that optimization problems (13) and $( I 4 )$ are mathematically ill-posed problems (many solutions) ; by using other criteria and/or constraints, for instance uniform distribution of weights $\delta _ { u }$ and $\gamma _ { u }$ or $\delta _ { u } ^ { u ^ { * } }$ and $\delta _ { u } ^ { u * }$ , lower and upper bounds etc., one can ensure well-posedness. When a unit improves its performance, the configuration of the problem may change.

## 4.3. Strengths and drawbacks of this approach

The approach presented so far has the following positive points.

<sup>!</sup> It is easy to understand and to use.

<sup>!</sup> Preferences are expressed locally (for each unit) by DMs rather than globally as is often done in the multi criteria decision making literature.

<sup>!</sup> A dominated unit knows units that perform better and so it can analyze the reasons for its weakness.

<sup>!</sup> It does not necessitate important computational power.

Some of its negative points could be the following.

<sup>!</sup> The evaluation is group related; as in the case of the DEA, the efficiency is relative (but does absolute efficiency have any sense?).

<sup>!</sup> It is necessary to normalize original data.

<sup>!</sup> Satisfiability functions do not express meaningful parameters for the unit.

In the following Section, we will apply this method to obtain a detailed analysis of a real world application that comes from the DEA literature.

## 5. Application

A large retailing organization which distributes goods to supermarkets consists of 20 depots that must be evaluated (see [8]). The input items are taken to be the value of the stock (S) and the recurrent costs in the form of wages (W). The output items, corresponding to the activity levels of the depots, are measured by the number of issues (I) representing deliveries to supermarkets, the number of receipts (Rc) in bulk from suppliers, and the number of requisitions (Rq) on suppliers where they are out of stock or approaching stock out. Data for this application are presented in Table 1 of the Appendix Section.

## 5.1. Results

## 5.1.1. Equal importance items

Application of the DEA approach leads to the results of the fourth column (see [8]) of Table 2 in the Appendix Section which shows that the relatively efficient depots are depots 12, 14, 15, and 19; for these depots there is no (possible) virtual depot that does better. If we look closely, we can see that depot 14 is declared efficient because of its performance in requests item that is very high compared to other output items; this will be revealed when applying the method established in this paper.

Applying the approach established in this paper, with equal importance of items (that is, all weights $\rho _ { k j } , j = 1 , 2 , 3$ and $\sigma _ { k i } , i { = } 1 , 2$ are supposed equal to one) leads to satisfiability functions $p _ { S }$ and $p _ { R }$ of columns 2 and 3 of Table 2 (see Appendix section). From satisfiability functions, we deduce the following sets (individually efficient set, equilibrium set and efficient equilibrium set) that are the fundamental data for our performance analysis.

R ¼ f g 01; 02; 05; 09; 10; 12; 14; 15; 16; 19; 20 ;

E ¼ f g 02; 05; 07; 09; 10; 12; 15; 19; 20 ;

S ¼ f g 02; 05; 09; 10; 12; 15; 19; 20 :

<sup>!</sup> The set ES is reduced to depot 07; it means that, though there is no depot that performs better than depot 07, this one is inefficiently using its resources (it can do better). Applying the optimization problem (13) to depot 07 we obtain

$$
\delta_ {0 7} = [ 0. 0 0 0 0 0. 0 2 9 9 0. 0 6 2 3 ] ^ {T} \text { and }
$$

$$
\gamma_ {0 7} = \left[ \begin{array}{c c} 0. 1 0 5 1 & 0. 1 0 5 1 \end{array} \right] ^ {T}
$$

which means that, as

$$
\begin{array}{l} o _ {0 7} = \left[ \begin{array}{c c c} 1. 0 0 0 0 & 0. 9 7 0 1 & 0. 8 7 6 9 \end{array} \right] ^ {T} \text { and } \\ i _ {0 7} = \left[ \begin{array}{c c c} 1. 0 0 0 0 & 0. 9 0 9 1 \end{array} \right] \end{array}
$$

if depot 07 increases its second and third output items by 3.8% and 7.10% respectively and reduces its resource consumption by 10.51% and 11.56% respectively, it will be efficient, as long as other units’ performances remain unchanged.

<sup>!</sup> RS is given by {01, 14, 16} with

$$
\mathcal {B} (0 1) = \{0 2, 0 9, 1 2, 1 0 \},
$$

$$
\mathcal {B} (1 4) = \{0 1, 0 2, 1 2, 1 9 \},
$$

$$
t \mathcal {B} (1 6) = \{0 1, 0 2, 0 9, 1 2, 1 4, 1 9 \},
$$

the sets of depots that strictly dominate depots 01, 14 and 16 respectively. This means that though depots 01, 14 and 16 are individually efficient, they can do better because there are depots that are doing better. For each of these depots, by solving a linear programming problem of the form (14), we obtain the results given in Tables 3–5 (see Appendix Section) and then vectors $\delta _ { u } ^ { * }$ and $\gamma _ { u } ^ { * }$ as defined by Eq. (15) are computed for possible recommendations for performance improvement. i) Solving the linear programming problem of the form (14) for depot 01; we obtain the data given in Table 3 and

$$
\begin{array}{l} \delta_ {0 1} ^ {*} = [ 0. 1 7 8 5 0. 0 2 7 3 0. 1 9 7 2 ] ^ {T}; \\ \gamma_ {0 1} ^ {*} = [ 0. 1 1 5 2 0. 1 2 5 0 ] ^ {T}. \end{array}
$$

So, as

$$
\begin{array}{l} o _ {0 1} = \left[ \begin{array}{c c c} 0. 5 0 0 0 & 0. 8 2 0 9 & 0. 4 6 1 5 \end{array} \right] ^ {T} \text { and } \\ i _ {0 1} = \left[ \begin{array}{c c c} 0. 4 2 8 6 & 0. 4 5 4 5 \end{array} \right] ^ {T}, \end{array}
$$

if depot 01 increases its output items by 35.70%, 3.33% and 42.73% respectively and reduces its input items by 26.88% and 25.70% respectively, it becomes non-dominated if other depots maintain their performance unchanged.

ii) As in i), we obtain for depot 14 the results given in Table 4 and

$$
\begin{array}{l} \delta_ {1 4} ^ {*} = [ 0. 1 2 7 0 0. 2 0 6 8 0. 0 1 5 4 ] ^ {T}; \\ \gamma_ {1 4} ^ {*} = [ 0. 1 8 5 3 0. 1 0 8 5 ] ^ {T}; \end{array}
$$

then, because

$$
\begin{array}{l} o _ {1 4} = [ 0. 4 7 5 0 0. 2 6 8 7 0. 9 8 4 6 ] ^ {T} \text { and } \\ i _ {1 4} = [ 0. 5 7 1 4 0. 3 6 3 6 ] ^ {T}, \end{array}
$$

if depot 14 can increase its output items by 26.74%, 76.98% and 1.56% and reduces its input items by 32.43% and 29.84% respectively it will become non-dominated. We see here that effort must be made by depot 14 mainly in the improvement of output item 2 where its performance is the worst. iii) Finally for depot 16, the results of Table 5 are obtained and

$$
\begin{array}{l} \delta_ {1 6} ^ {*} = [ 0. 2 0 2 7 0. 2 8 8 5 0. 0 2 6 8 ] ^ {T}; \\ \gamma_ {1 6} ^ {*} = [ 0. 1 4 2 6 0. 1 9 1 2 ] ^ {T} \end{array}
$$

with

$$
\begin{array}{l} o _ {1 6} = [ 0. 4 7 5 0 0. 2 9 8 5 0. 9 2 3 1 ] ^ {T}; \\ i _ {1 6} = [ 0. 4 2 8 6 0. 5 4 5 5 ] ^ {T} \end{array}
$$

so that depot 16 can become non-dominated by increasing its output items by 42.67%, 96.65% and 2.90% and reducing its input items by 33.27% and 35.05% respectively.

The rest of the performance results are summarized below.

$$
\begin{array}{l} \mathcal {U} - \Sigma \cup \mathcal {E} = \{0 3, 0 4, 0 6, 0 8, 1 1, 1 3, 1 7, 1 8 \} \\ \mathcal {B} (0 3) = \{0 2, 0 9, 1 2, 1 9 \}, \\ \mathcal {B} (0 4) = \{0 2, 0 6, 9, 1 0, 1 1, 1 2, 1 9, 2 0 \}, \\ \mathcal {B} (0 6) = \{0 2, 0 9, 1 9 \}, \\ \mathcal {B} (0 8) = \{0 1, 0 2, 0 3, 0 6, 0 9, 1 2, 1 4, 1 6, 1 9 \}, \\ \mathcal {B} (1 1) = \{0 9, 1 0, 2 0 \}, \\ \mathcal {B} (1 3) = \{0 1, 0 2, 0 3, 0 6, 0 9, 1 0, 1 1, 1 2, 1 4, 1 9, 2 0 \}, \\ \mathcal {B} (1 7) = \{0 7 \}, \\ \mathcal {B} (1 8) = \{0 1, 0 2, 0 3, 0 5, 0 9, 1 2, 1 4, 1 5, 1 6, 1 9 \}. \end{array}
$$

In comparison, we see that all depots declared efficient by the DEA method are efficient equilibrium according to our approach except depot 14 (efficient but dominated) that is dominated by depots 01, 02, 12 and 19 in our approach; this is due to the fact that in the DEA approach, by putting maximum weight on the third output item, depot 14 can be efficient since the ratio between its third output item and input items is very high compared to other ratios.

## 5.1.2. Relative importance of items

If we suppose that DMs are more sensible to wage as resource consumption than stock and give them weights 2 and 1 respectively (that is $\sigma _ { k l } = 1$ and $\sigma _ { k 2 } = 2$ for any k) and they also consider that the issues item is more important, as output, than the receipts item which, in turn, is more important than the requests item and give them weights 5, 3 and 1 respectively $( \rho _ { k l } = 5 , ~ \rho _ { k 2 } = 3$ and $\rho _ { k 3 } = 1$ for any k), then the following results are obtained.

R ¼ f g 01; 02; 03; 05; 09; 10; 12; 15; 19; 20 ;

E ¼ f g 02; 07; 09; 10; 12; 15; 19; 20 ;

$$
\mathcal {S} = \{0 2, 0 9, 1 0, 1 2, 1 5, 1 9, 2 0 \}.
$$

Now depot 05 is no longer an efficient equilibrium because it is dominated by depot 12; this is due to the fact that depot 05 performs very poorly in terms of issues, a criterion considered as very important by DMs. Of course, a sensitivity analysis can be done as previously.

## 6. Conclusion

In this paper, a problem of evaluating a group of production units by a group of decision makers (managers, administrators, politicians, experts, etc.) has been formulated and solved using the satisficing game theory paradigm. Data that are used for evaluation are input items in terms of resource consumption and output items in terms of products or delivered services in a data envelopment (DEA) type framework. A method based on the satisficing game theory has been established that allows a unit to be evaluated <sup>b</sup>individually<sup>Q</sup> in terms of its resource consumption versus its delivery performance as well as how good it is performing with regard to its counterparts, a within-group evaluation. This method can be used as a complement to the DEA approach to integrate a subjective point of view of decision makers and for analysis of causes of possible inefficiency. The application considered (a real world problem) shows the feasibility of this approach and its low demand on computational power makes it suitable for integration in computer aid decision support systems; this point will be considered in future work.

## Acknowledgment

The author would like to thank his colleague Patrick Habel (an English Lecturer) who went through the previous version of this paper to correct numerous grammatical and stylistic errors reported by reviewers as well as anonymous referees for their valuable comments.

Appendix A. Data and results for the application under consideration

<table><tr><td colspan="6">Table 1</td></tr><tr><td>Depot</td><td>S(£M)</td><td>W(00,000&#x27; S)</td><td>I(00&#x27; S)</td><td>Rc(000&#x27; S)</td><td>Rq(000&#x27; S)</td></tr><tr><td>Depot 01</td><td>3</td><td>5</td><td>40</td><td>55</td><td>30</td></tr><tr><td>Depot 02</td><td>2.5</td><td>4.5</td><td>45</td><td>50</td><td>40</td></tr><tr><td>Depot 03</td><td>4</td><td>6</td><td>55</td><td>45</td><td>30</td></tr><tr><td>Depot 04</td><td>6</td><td>7</td><td>48</td><td>20</td><td>60</td></tr><tr><td>Depot 05</td><td>2.3</td><td>3.5</td><td>28</td><td>50</td><td>25</td></tr><tr><td>Depot 06</td><td>4</td><td>6.5</td><td>48</td><td>20</td><td>65</td></tr><tr><td>Depot 07</td><td>7</td><td>10</td><td>80</td><td>65</td><td>57</td></tr><tr><td>Depot 08</td><td>4.4</td><td>6.4</td><td>25</td><td>48</td><td>30</td></tr><tr><td>Depot 09</td><td>3</td><td>5</td><td>45</td><td>64</td><td>42</td></tr><tr><td>Depot 10</td><td>5</td><td>7</td><td>70</td><td>65</td><td>48</td></tr><tr><td>Depot 11</td><td>5</td><td>7</td><td>45</td><td>65</td><td>40</td></tr><tr><td>Depot 12</td><td>2</td><td>4</td><td>45</td><td>40</td><td>44</td></tr><tr><td>Depot 13</td><td>5</td><td>7</td><td>65</td><td>25</td><td>35</td></tr><tr><td>Depot 14</td><td>4</td><td>4</td><td>38</td><td>18</td><td>64</td></tr><tr><td>Depot 15</td><td>2</td><td>3</td><td>20</td><td>50</td><td>15</td></tr><tr><td>Depot 16</td><td>3</td><td>6</td><td>38</td><td>20</td><td>60</td></tr><tr><td>Depot 17</td><td>7</td><td>11</td><td>68</td><td>64</td><td>54</td></tr><tr><td>Depot 18</td><td>4</td><td>6</td><td>25</td><td>38</td><td>20</td></tr><tr><td>Depot 19</td><td>3</td><td>4</td><td>45</td><td>67</td><td>32</td></tr><tr><td>Depot 20</td><td>5</td><td>6</td><td>57</td><td>60</td><td>40</td></tr></table>

Table 2

<table><tr><td>Depot</td><td> $p_{\text{S}}(u)$ </td><td> $p_{\text{R}}(u)$ </td><td>DEA efficiency</td></tr><tr><td>01</td><td>0.0466</td><td>0.0394</td><td>0.82</td></tr><tr><td>02</td><td>0.0503</td><td>0.0342</td><td>0.94</td></tr><tr><td>03</td><td>0.0476</td><td>0.0498</td><td>0.82</td></tr><tr><td>04</td><td>0.0476</td><td>0.0666</td><td>0.65</td></tr><tr><td>05</td><td>0.0387</td><td>0.0289</td><td>0.95</td></tr><tr><td>06</td><td>0.0496</td><td>0.0519</td><td>0.83</td></tr><tr><td>07</td><td>0.0744</td><td>0.0852</td><td>0.71</td></tr><tr><td>08</td><td>0.0389</td><td>0.0540</td><td>0.52</td></tr><tr><td>09</td><td>0.0565</td><td>0.0394</td><td>0.96</td></tr><tr><td>10</td><td>0.0675</td><td>0.0603</td><td>0.89</td></tr><tr><td>11</td><td>0.0561</td><td>0.0603</td><td>0.63</td></tr><tr><td>12</td><td>0.0480</td><td>0.0290</td><td>1.00</td></tr><tr><td>13</td><td>0.0450</td><td>0.0603</td><td>0.83</td></tr><tr><td>14</td><td>0.0452</td><td>0.0417</td><td>1.00</td></tr><tr><td>15</td><td>0.0321</td><td>0.0249</td><td>1.00</td></tr><tr><td>16</td><td>0.0443</td><td>0.0435</td><td>0.91</td></tr><tr><td>17</td><td>0.0689</td><td>0.0892</td><td>0.55</td></tr><tr><td>18</td><td>0.0310</td><td>0.0498</td><td>0.42</td></tr><tr><td>19</td><td>0.0537</td><td>0.0354</td><td>1.00</td></tr><tr><td>20</td><td>0.0581</td><td>0.0562</td><td>0.84</td></tr></table>

Table 3

<table><tr><td> $u^{*} =$ </td><td>02</td><td>09</td><td>12</td></tr><tr><td rowspan="3"> $\delta_{01}^{u*}$ </td><td>0.0663</td><td>0.1785</td><td>0.0202</td></tr><tr><td>0.0073</td><td>0.0273</td><td>0.0132</td></tr><tr><td>0.0767</td><td>0.1972</td><td>0.0241</td></tr><tr><td rowspan="2"> $\gamma_{01}^{u*}$ </td><td>0.0568</td><td>0.0002</td><td>0.1152</td></tr><tr><td>0.0641</td><td>0.0000</td><td>0.1250</td></tr></table>

Table 4

<table><tr><td> $u^{*}=$ </td><td>01</td><td>02</td><td>12</td><td>19</td></tr><tr><td rowspan="3"> $\delta_{14}^{u*}$ </td><td>0.0084</td><td>0.0669</td><td>0.0296</td><td>0.1270</td></tr><tr><td>0.0344</td><td>0.1252</td><td>0.0695</td><td>0.2068</td></tr><tr><td>0.0152</td><td>0.0154</td><td>0.0153</td><td>0.0119</td></tr><tr><td rowspan="2"> $\gamma_{14}^{u*}$ </td><td>0.0349</td><td>0.1155</td><td>0.1853</td><td>0.1017</td></tr><tr><td>0.0194</td><td>0.0591</td><td>0.1085</td><td>0.0453</td></tr></table>

Table 5

<table><tr><td> $u^{*} =$ </td><td>01</td><td>02</td><td>09</td><td>12</td><td>14</td><td>19</td></tr><tr><td rowspan="3"> $\delta_{16}^{\text{u}^{*}}$ </td><td>0.0176</td><td>0.0850</td><td>0.2027</td><td>0.0427</td><td>0.0001</td><td>0.1490</td></tr><tr><td>0.0468</td><td>0.1417</td><td>0.2885</td><td>0.0830</td><td>0.0112</td><td>0.2243</td></tr><tr><td>0.0268</td><td>0.0141</td><td>0.0027</td><td>0.0220</td><td>0.0238</td><td>0.0059</td></tr><tr><td rowspan="2"> $\gamma_{16}^{\text{u}^{*}}$ </td><td>0.0375</td><td>0.0875</td><td>0.0247</td><td>0.1426</td><td>0.0171</td><td>0.0723</td></tr><tr><td>0.0574</td><td>0.1275</td><td>0.0701</td><td>0.1912</td><td>0.0242</td><td>0.1150</td></tr></table>

## References

[1] A. Charnes, W.W. Cooper, E. Rhodes, Measuring the efficiency of decision making units, European Journal of Operational Research 2 (1978) 429– 444.

[2] G.B. Dantzig, Linear Programming and Extensions, Princeton University Press, Princeton, NJ, 1963.

[3] W.C. Stirling, Satisficing Games and Decision Making: With Applications to Engineering and Computer Science, Cambridge University Press, 2003, ISBN: 0521817242.

[4] S.A. Thore, Technology Commercialization: DEA and Related Analytical Methods for Evaluating the Use and Implementation of Technical Innovation, Kluwer Academic Publishers, Boston, 2002.

[5] S. Thore, G. Kozmetsky, F. Phillips, DEA of financial statements data: the U.S. computer industry, Journal of Productivity Analysis 2 (1994) 229 – 248.

[6] K.C. Land, K. Lovell, S. Thore, Productive efficiency under capitalism and state socialism: an empirical inquiry using chance-constrained data envelopment analysis, Technological Forecasting & Social Change 46 (1994) 139 – 152.

[7] W.L. Winston, Operations Research: Applications and Algorithms, Third Edition, Duxbury Press, 1994.

[8] http://www.deazone.com/tutorial/dual.htm.

[9] http://www.stenthore.com/DEA.htm.

![](/api/attachments/MWU4TWYK/fulltext/images/19b4438b43008fe3dd325a1b793726e511b9041105d0e1821d43175740e8a78b.jpg)

Ayeley Philippe Tchangani received an Inge´nieur Degree from Ecole Centrale de Lille, Lille, France, in 1995; an MSc (DEA) and a PhD (Doctorat) from Universite´ des Sciences et Technologies de Lille, Lille, France, in 1995 and 1999 respectively in Control and Automation. From November 1999 to December 2000, he was a Postdoctoral Fellow at French-South Africa Technical Institute in Electronics, Technikon Pretoria, South Africa. Since February

2001, he has been with the Universite´ Toulouse III (IUT de Tarbes), Tarbes, France, where he is currently an Assistant Professor (MaˆVtre de Confe´rences); he teaches control systems, automation and dependability. He is also an Assistant Research Professor at Laboratoire Ge´nie de Production (LGP), Ecole Nacionale d’Inge´nieurs de Tarbes (ENIT), Tarbes, France. Dr. Tchangani’s current research interests include modeling and deriving algorithms for control, decision making, reliability analysis and optimization and performance evaluation of systems in uncertain and conflicting environment. He has authored or co-authored over 20 papers in international journals, edited books, and international conferences proceedings. He is a Member of IEEE and SIAM.
