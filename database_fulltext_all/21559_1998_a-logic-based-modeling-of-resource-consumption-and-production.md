---
otero_id: 21559
otero_key: "TARHF4J6"
title: "A logic-based modeling of resource consumption and production"
authors: "Young U. Ryu"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00061-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A logic-based modeling of resource consumption and production

Young U. Ryu <sup>),1</sup>

Department of Decision Sciences, The UniÕersity of Texas at Dallas, P.O. Box 830688, M<sup>r</sup>S JO 4.4, Richardson, TX 75083-0688, USA

## Abstract

Proposed are: 1 a logic modeling system called logic of resource, inspired by linear logic, for the specification of Ž . disposable resources; and 2 its implementation in the logic programming paradigm. The difficulty in the representation ofŽ . disposable resources as formulas of classical logic motivates the study of this logic modeling system. There are similarities and differences between resource consumption<sup>r</sup>production and theorem proving in logic. Both are about deducibility or Ž producibility of a formula or a thing . The major difference is that once a disposable resource is used to produce. Ž . something, it is not available anymore; but a formula can be repeatedly used in deduction. We adopt a form of non-standard logic called linear logic to develop a logic modeling system of resources and implement it in a variant of the logic programming paradigm. The resource logic modeling system can process state–space models represented by Petri net or their subclasses such as marked graphs and state machines. It can serve as a modeling tool for business procedures and production scheduling. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Linear logic; Logic of resources; Logic modeling; Resource programming; Petri net

## 1. Introduction

This paper is concerned with logic-based modeling of resource consumption and production. In classical logic, given formulas $\mathbf { \dot { \varphi } } _ { \phi } , \mathbf { \dot { \varphi } } _ { \phi } \supset \psi _ { 1 } ,$ , ‘Ž implies $\psi _ { 1 } ^ { ~ , } )$ , and $\mathbf { \dot { \Phi } } \phi \supset \psi _ { 2 } , \mathbf { \dot { \Phi } } \ ,$ Ž‘ implies $\psi _ { 2 } ^ { ~ , } )$ , we deduce both $\cdot _ { \psi _ { 1 } } ,$ and $\cdot _ { \psi _ { 2 } } :$ ’. This is from the understanding that the minor premise $\cdot _ { \phi } ,$ for the deductions of $\cdot _ { \psi _ { 1 } } ,$ and $\cdot _ { \psi _ { 2 } } ,$ is persistent in classical logic. However, $\mathrm { i f } \ ^ { \cdot } \phi ^ { \cdot }$ represents the availability of a resource, $\mathbf { \dot { \varphi } } _ { \phi } \supset \psi _ { 1 } \mathbf { \dot { \varphi } } _ { 1 }$ is understood as ‘the use of resource $\phi$ meets the requirement the establishment, the production, the purchase, the construction, the Ž creation, or whatever of resource. $\psi _ { 1 } ,$ ’ and $\mathbf { \dot { \Phi } } \phi \supset \psi _ { 2 } , \mathbf { \dot { \Phi } } \ ,$ is similarly understood, then we can have only one of $\cdot _ { \psi _ { 1 } }$ and $\cdot _ { \psi _ { 2 } } ,$ , not both. This is because when $\cdot _ { \phi } ,$ is used for the production of either $\cdot _ { \psi _ { 1 } } ,$ or $\cdot _ { \psi _ { 2 } } ,$ , it is not available for the production of the other. This difference between theorem proving in logic and resource consumption<sup>r</sup>production is a difficult problem to overcome in classical logic. However, the recent development of linear logic provides a foundation to address such a difference.

Linear logic was introduced as a ‘resource conscious logic’ 2,3 by extending intuitionistic logic. It is a<sup>w</sup> <sup>x</sup> strong system of logic in that it subsumes both classical first-order and intuitionistic logic, and additionally supports concepts of disposable resources and their consumption. Linear logic provides mechanisms to destroy and construct formulas in the process of theorem proving. The analogy between the linear logic theorem proving mechanism and resource consumption<sup>r</sup>production allows us to logically model resources and their usages. We adopt a fragment of linear logic and develop a logical system for resource-oriented modeling. The logical system, then, is implemented in a variant of logic programming, resulting in a computable resource modeling environment.

The implemented system is especially useful for various state–space models, represented by Petri net, in which space transformation corresponds to resource consumption and production. For instance, in a commodity trading market, price and trading constraints constitute the initial state, and the commodity allocation between traders transforms states. Production scheduling is another class of state–space problems in which the initial state is described by the production capacity and requirement, and transformed by task allocations.

We first propose, in Section 2, a logic of resource as a fragment of linear logic. The notations of the logic of resource represent disposable and durable resources and resource, transformation rules that can be understood as production machines. The system of the logic of resource is defined by introducing a few connectives and operators adopted from linear logic and proposing deduction structures governing production activities which Ž . Ž are provable in linear logic . Section 3 is devoted to the computation and implementation issues, resulting in a . modeling and programming environment, called resource programming, similar to logic programming languages such as Prolog. In Section 4, we address modeling techniques for Petri net. Finally, an example of simple resource requirement planning is addressed in Section 5 in order to demonstrate the use of resource programming.

## 2. Logic of resource

In classical logic, if a formula is true, it stays true whether or not it is used to prove other formulas. In the logic of resource, on the other hand, if an atomic formula representing a resource isŽ . aÕailable, it is not available again once it is used i.e., consumed to prove i.e., produce other formulas. This is the starting point Ž . Ž . of the logic of resource.

An atomic formula in the logic of resource represents a disposable resource, which can be used only once. A durable resource is represented with the storage operator ‘!’:

$$
! \phi .
$$

which stands for the unlimited availability of $\phi ,$ as many s as one wants, or a printing press for s.

There are two types of implication formulas in the logic of resource, which are resource transformation rules or production machines. The first one:

$$
\phi_ {1}, \phi_ {2}, \dots , \phi_ {n} \rightarrow \circ \psi_ {1}, \psi_ {2}, \dots , \psi_ {m}
$$

stands for a disposable machine. That is, by consuming exactly one unit of $\phi _ { 1 }$ , one unit of $\phi _ { 2 } , \ldots ,$ , and one unit of $\phi _ { n }$ , exactly one unit of $\psi _ { 1 }$ , one unit of $\psi _ { 2 } , \ldots$ , and one unit of $\psi _ { m }$ are produced. A disposable machine, like a disposable resource, can be used only once. Note that commas at the left-hand and right-hand sides of anŽ implication formula are considered as the commutative conjunction connective. Also, we assume that all variables in formulas are universally quantified, just as in Prolog. A. durable machine is represented as

$$
! \left(\phi_ {1}, \phi_ {2}, \dots , \phi_ {n} \rightarrow \circ \psi_ {1}, \psi_ {2}, \dots , \psi_ {m}\right),
$$

which is usually abbreviated as:

$$
\phi_ {1}, \phi_ {2}, \dots , \phi_ {n} \rightarrow \psi_ {1}, \psi_ {2}, \dots , \psi_ {m}.
$$

A durable machine is similar to a disposable machine, except that it can be used repeatedly.

Note that in classical logic, both the rule of strengthening the antecedent:

if $\phi \supset \psi$ then $\phi \land \phi ^ { \prime } \supset \psi$

and the contraction rule:

$$
\text { if   } \phi \land \phi^ {\prime} \land \phi^ {\prime} \supset \psi \text {   then   } \phi \land \phi^ {\prime} \supset \psi
$$

hold. But, none of them is acceptable in the logic of resource. In classical logic,

$$
\phi \supset \psi_ {1} \wedge \psi_ {2}
$$

is equivalent with two clauses:

$$
\phi \supset \psi_ {1}
$$

$$
\phi \supset \psi_ {2}.
$$

However, in the logic of resource,

$$
\phi \rightarrow \psi_ {1}, \psi_ {2}
$$

is not equivalent with:

$$
\phi \rightarrow \psi_ {1}
$$

$$
\phi \rightarrow \psi_ {2}.
$$

Under the assumption that resource $\phi$ is not dividable to components, each of which contributes to the production of $\psi _ { 1 }$ or $\psi _ { 2 }$ , there are no equivalent clausal form implications.

Let and be bags of formulas and be a sequence of atomic formulas or those prefixed by operator ‘!’. ŽNote that a bag, or a multi-set, is a collection of unordered elements in which the multiple occurrent of the same elements counts. By:.

$$
\Gamma | \Psi | \Delta ,
$$

we mean ‘ is produced from  and  remains.’ Also, by:

$$
\frac {\Gamma | \Psi | \Delta}{\Gamma^ {\prime} | \Psi^ {\prime} | \Delta^ {\prime}},
$$

Ž . we mean ‘if is produced or deduced from and remains, then $\psi ^ { \prime }$ is produced from $T ^ { \prime }$ and remains.’ Let $\overline { { \psi } }$ denote either an atomic formula or ! . Now, we define a number of deduction structures, or deduction rules, for the logic of resource.

The following four deduction structures are for the simple availability of resources:

$$
\Gamma \cup \{\psi \} | \psi | \Gamma\tag{DS1}
$$

$$
\Gamma \cup \{  ! \psi \} |! \psi |   \Gamma \cup \{  ! \psi \}\tag{DS2}
$$

$$
\Gamma |! \psi | \Delta
$$

$$
\Gamma | \psi | \Delta\tag{DS3}
$$

$$
\frac {\Gamma | \overline {{\psi}} _ {1} | \Gamma^ {\prime}   \Gamma^ {\prime} | \overline {{\psi}} _ {2} | \Gamma^ {\prime \prime}   \ldots   \Gamma^ {(n)} | \overline {{\psi}} _ {m} | \Delta}{\Gamma | \overline {{\psi}} _ {1} , \overline {{\psi}} _ {2} , \ldots , \overline {{\psi}} _ {m} | \Delta}.\tag{DS4}
$$

From Eqs. DS2 and DS3 , we can infer:Ž . Ž .

$$
\Gamma \cup \{  ! \psi \} | \psi | \Gamma \cup \{  ! \psi \},
$$

which explains the behavior of the storage operator $\because$

Productions with durable machines are explained by Eqs. DS5 and DS6 :Ž . Ž .

$$
\begin{array}{c} \Gamma \cup \left\{\overline {{\phi}} _ {1}, \ldots , \overline {{\phi}} _ {n} \to \overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} |! \phi_ {1}, \ldots ,! \phi_ {n} | \Delta \\ \hline \Gamma \cup \left\{\overline {{\phi}} _ {1}, \ldots , \overline {{\phi}} _ {n} \to \overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} | \Box | \Delta \cup \left\{\text {!} \psi_ {1}, \ldots ,! \psi_ {m} \right\} \\ \hline \Gamma \cup \left\{\phi_ {1}, \ldots , \phi_ {i},! \phi_ {i + 1}, \ldots ,! \phi_ {n} \to \overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} | \phi_ {1}, \ldots , \phi_ {i ^ {\prime}},! \phi_ {i ^ {\prime} + 1}, \ldots ,! \phi_ {n} | \Delta \\ \hline \Gamma \cup \left\{\phi_ {1}, \ldots , \phi_ {i},! \phi_ {i + 1}, \ldots ,! \phi_ {n} \to \overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} | \Box |   \Delta \cup \left\{\overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} \end{array}\tag{DS5}
$$

Ž . DS6

where $1 \leq i ^ { \prime } \leq i .$ . Note $\cdot _ { \sqsupset } ,$ denotes the empty bag. Eq. DS5 states that if unlimitedly many units ofŽ . $\phi _ { 1 } , . . . , \phi _ { n }$ are available, then unlimitedly, many units of $\psi _ { 1 } , \ldots , \psi _ { m }$ are produced from durable machine $\cdot \overline { { \phi } } _ { 1 } , \ldots , \overline { { \phi } } _ { n } $ $\overline { { \psi } } _ { 1 } , \hdots , \overline { { \psi } } _ { m } ^ { \mathrm { ~ , ~ } }$ . This is because the durable machine can be repeatedly used for the production of $\psi _ { 1 } , \ldots , \psi _ { m } .$ According to Eq. DS6 , when we have resources Ž . $\overline { { \phi } } _ { 1 } , \ldots , \overline { { \phi } } _ { i } , ! \phi _ { i + 1 } , \ldots , ! \phi _ { n }$ , where $\overline { { \phi } } _ { i ^ { \prime } } = \phi _ { i ^ { \prime } }$ for some $1 \leq i ^ { \prime } \leq i ,$ we produce $\overline { { \psi } } _ { 1 } , \hdots , \overline { { \psi } } _ { m }$ from durable machine $^ { * } \phi _ { 1 } , \ldots , \phi _ { i } , ! \phi _ { i + 1 } , \ldots , ! \phi _ { n } \to \overline { { \psi } } _ { 1 } , \ldots , \overline { { \psi } } _ { m } ,$ . In Eqs. DS5 andŽ . Ž . DS6 , the durable machines are still available after the productions. That is, the following is provable:

if ${ \cal T } | \psi | \varDelta$ and  , . . . , ™ , . . . , <sup>g</sup> , then  , . . . , ™ , . . . , <sup>g</sup> . <sub>1 n 1 m 1 n 1 m</sub>

Productions with disposable machines are similarly described as follows:

$$
\begin{array}{c}\Gamma |! \phi_ {1}, \ldots ,! \phi_ {n} | \Delta\\\hline \Gamma \cup \left\{\overline {{\phi}} _ {1}, \ldots , \overline {{\phi}} _ {n} \rightarrow \circ \overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} | \Box | \Delta \cup \left\{\overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\}\\\hline \Gamma | \phi_ {1}, \ldots , \phi_ {i ^ {\prime}},! \phi_ {i ^ {\prime} + 1}, \ldots ,! \phi_ {n} | \Delta\\\hline \Gamma \cup \left\{\phi_ {1}, \ldots , \phi_ {i},! \phi_ {i + 1}, \ldots ,! \phi_ {n} \rightarrow \circ \overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\} | \Box | \Delta \cup \left\{\overline {{\psi}} _ {1}, \ldots , \overline {{\psi}} _ {m} \right\},\end{array}\tag{DS7}
$$

DS8 Ž .

where $1 \leq i ^ { \prime } \leq i$ . Observe that once disposable machines are used in productions, they are no longer available. Another observation that explains the difference between durable and disposable machines—that is, in Eqs. Ž . Ž . DS5 and DS7 —is that though unlimitedly, many units of $\phi _ { 1 } , . . . , \phi _ { n }$ are available, one may not produce

$$
\begin{array}{c}\left\{p, s \rightarrow t, p, u \atop q, r \right\} \Bigg | q \Bigg | \left\{p, s \rightarrow t, p, u \atop r \right\} (\text {DS1}) \quad \left\{p, s \rightarrow t, p, u \atop r \right\} \Bigg | r \Bigg | \{p, s \rightarrow t, p, u \} (\text {DS1})\\\left. \right.\left\{p, s \rightarrow t, p, u \atop q, r \right\} \Bigg | q, r \Bigg | \{p, s \rightarrow t, p, u \} (\text {DS4})\\\left\{p, s \rightarrow t, p, u \atop q, r \multimap s \atop p, q, r \right\} \Bigg | p \Bigg | \left\{p, s \rightarrow t, p, u \atop q, r \multimap s \atop q, r \right\} (\text {DS1}) \quad \left\{p, s \rightarrow t, p, u \atop q, r \multimap s \atop q, r \right\} \Bigg | s \Bigg | \{p, s \rightarrow t, p, u \} (\text {DS8}, 1, \&9)\\\left. \right.\left\{p, s \rightarrow t, p, u \atop q, r \multimap s \atop p, q, r \right\} \Bigg | p, s \Bigg | \{p, s \rightarrow t, p, u \} (\text {DS4})\\\left\{p, s \rightarrow t, p, u \atop q, r \multimap s \atop p, q, r \right\} \Bigg | t \Bigg | \left\{p, s \rightarrow t, p, u \atop p, u \right\} (\text {DS6}, 1, \&9) \quad \left\{p, s \rightarrow t, p, u \atop p, u \right\} \Bigg | p \Bigg | \left\{p, s \rightarrow t, p, u \atop u \right\} (\text {DS1})\\\left.\left\{p, s \rightarrow t, p, u \atop q, r \multimap s \atop p, q, r \right\} \Bigg | t, p \Bigg | \left\{p, s \rightarrow t, p, u \atop u \right\} (\text {DS4}) \right.\end{array}
$$

Fig. 1. A sample deduction process. Given ${ } ^ { \cdot } p , s \to t , p , u ^ { \prime } , { } ^ { \cdot } q , r \to \circ s ^ { \prime } , { } ^ { \cdot } p ^ { \prime } , { } ^ { \cdot } q ^ { \prime }$ , and $" r '$ , the deduction of $\cdot _ { t , p } ,$ is showed. A deduction structure number is attached to each instance of deduction structures.

unlimitedly many units of $\psi _ { 1 } , \ldots , \psi _ { m }$ from ${ } ^ { * } \overline { { \phi } } _ { 1 } , \ldots , \overline { { \phi } } _ { n }  \circ \overline { { \psi } } _ { 1 } , \ldots , \overline { { \psi } } _ { m } { } ^ { * }$ which is a disposable machine. The use of Eqs. DS5 , DS6 , DS7 and DS8 with Eqs. DS1 , DS2 , DS3 and DS4 is achieved with:Ž . Ž . Ž . Ž . Ž . Ž . Ž . Ž .

$$
\frac {\Gamma | \Box | \Gamma^ {\prime}   \Gamma^ {\prime} | \overline {{\psi}} | \Delta}{\Gamma | \overline {{\psi}} | \Delta}.\tag{DS9}
$$

For example, Fig. 1 shows the use of deduction structures for a proof of $\cdot , \ p ^ { , }$ from:

$$
p, s \to t, p, u
$$

## 3. Resource programming interpreter

Standard logic programming 1,4 can be considered as a subset of clausal form logic. A logic program <sup>w</sup> <sup>x</sup> consists of a set of program clauses:

$$
\langle \text {   head   } \rangle \leftarrow \langle \text {   body   } \rangle
$$

where head is an atomic formula and body is conjunction of literals. All variables in a clause are assumed ² : ² : to be universally quantified. Unification and SLD-resolution or SLDNF-resolution constitute the centralŽ . computation mechanism for automated theorem proving.

Resource programming is implemented in a similar way. We introduce four new operators: resource availability checking operator $\mathbf { \ddot { j } } ^ { \ast }$ , resource producibility checking operator ‘@’, resource unavailability checking operator $^ \ast \sim$ , and resource unproducibility checking operator $"  "$ . Deductions with these operators are governed by:

$$
\begin{array}{l} \frac {\overline {{\psi}} \in \Gamma}{\Gamma | _ {i} \psi | \Gamma} \\ \frac {\Gamma | \overline {{\psi}} | \Delta}{\Gamma | @ \psi | \Gamma} \\ \frac {\overline {{\psi}} \notin \Gamma}{\Gamma | \sim \psi | \Gamma} \\ \frac {\overline {{\psi}} \text {is not producible from} \Gamma}{\Gamma | \neg \psi | \Gamma} \end{array}
$$

The syntactic structure of the resource programming is as follows. A resource program is a bag of two types of clauses:

$$
\overline {{\phi}} _ {1}, \overline {{\phi}} _ {2}, \ldots , \overline {{\phi}} _ {n} \leftarrow \tilde {\psi} _ {1}, \tilde {\psi} _ {2}, \ldots , \tilde {\psi} _ {n}
$$

$$
\overline {{\phi}} _ {1}, \overline {{\phi}} _ {2}, \ldots , \overline {{\phi}} _ {n} \circ \leftarrow \tilde {\psi} _ {1}, \tilde {\psi} _ {2}, \ldots , \tilde {\psi} _ {n}
$$

where $\overline { { \phi } }$ is either $\phi$ or $! \phi$ and $\tilde { \psi }$ is either $\psi , \ : { ^ { \ast } ! \psi ^ { \prime } } , \ : { ^ { \ast } } _ { \mathrm { i } } \psi ^ { \prime } , \ : { ^ { \ast } @ \psi ^ { \prime } } , \ : { ^ { \ast } } \sim \psi ^ { \prime } , \ : \mathrm { o r ~ } \ : { ^ { \ast } } \ : \lnot \psi ^ { \prime }$ . Atomic formulas and those prefixed by operator $\because$ may appear at both the left-hand and the right-hand side of a clause. But, formulas prefixed by operators of ${ \mathrm {  ~ \dot { \omega } ~ } } _ { \dot { \mathrm {  ~ i ~ } } } , \ \mathrm {  ~ \dot { \omega } ~ } _ { \dot { \mathrm {  ~ \omega ~ } } } , \ \mathrm {  ~ \dot { \omega } ~ } _ { \mathrm {  ~ \omega ~ } } , \ \mathrm {  ~ \omega ~ } _ { \mathrm {  ~ \omega ~ } } \mathrm {  ~ \omega ~ } _ { \dot { \mathrm {  ~ \omega ~ } } } ,$ appear only at the right-hand side of a clause. Clause:

$$
\overline {{\psi}} _ {1}, \overline {{\psi}} _ {2}, \ldots , \overline {{\psi}} _ {m} \circ \leftarrow
$$

is equivalent to:

$$
\overline {{\psi}} _ {1} \circ \leftarrow
$$

$$
\overline {{\psi}} _ {2} \circ \leftarrow
$$

$$
\overline {{\psi}} _ {m} \circ \leftarrow .
$$

Similarly, clause:

$$
\overline {{\psi}} _ {1}, \overline {{\psi}} _ {2}, \dots , \overline {{\psi}} _ {m} \leftarrow
$$

is equivalent to:

$$
\overline {{\psi}} _ {1} \leftarrow
$$

$$
\overline {{\psi}} _ {2} \leftarrow
$$

$$
\overline {{\psi}} _ {m}
$$

A query for $\tilde { \psi } _ { 1 } , \tilde { \psi } _ { 2 } , \ldots ,$ , and $\tilde { \psi } _ { m }$ is expressed as:

$$
\circ \leftarrow \tilde {\psi} _ {1}, \tilde {\psi} _ {2}, \dots , \tilde {\psi} _ {m}.
$$

A proof state in resource programming is:

$$
\sigma = \left\langle P, \left(\tilde {\psi} _ {1}, \tilde {\psi} _ {2}, \dots , \tilde {\psi} _ {m}\right), \Theta , L \right\rangle
$$

where P is a bag of formulas, $\psi _ { i }$ Ž . for each i is an atomic formula,  is a substitution, and L is a set of pairs of $\mathrm { ~ a ~ } \gets$ clause and an atomic formula. When $\phi$ is a formula and is a substitution, denotes the formula obtained by applying to $\phi .$ When and are substitutions, $\theta \circ \tau$ is the composition of and $\tau .$

From state , a transformed state $\sigma ^ { \prime }$ is obtained by the following.

## 3.1. Transformation rule 1

When $\tilde { \psi } _ { i } = \psi _ { i }$ or $\ ! \psi _ { i }$ . Select:

$$
c = \overline {{{\gamma}}} _ {1}, \overline {{{\gamma}}} _ {2}, \dots , \overline {{{\gamma}}} _ {k} \leftarrow \tilde {\phi} _ {1}, \dots , \tilde {\phi} _ {n} \in P
$$

where $\psi _ { i }$ and $\gamma _ { j }$ for some $j$ are unifiable with and $\left. c \theta , \tilde { \gamma } _ { i } \theta \right. \not \in R$ . And then, establish a substate:

$$
\tau = \left\{ \begin{array}{l} \langle P, (! \phi_ {1} \theta , \dots ,! \phi_ {n} \theta), \theta , R \cup \{\langle c \theta , \overline {{\gamma}} _ {j} \theta \rangle \} \rangle \text {   if   } \tilde {\psi} _ {i} = ! \psi_ {i} \text {   and   } \overline {{\gamma}} _ {j} = \gamma_ {j} \\ \langle P, (\tilde {\phi} _ {1} \theta , \dots , \tilde {\phi} _ {n} \theta), \theta , R \cup \{\langle c \theta , \overline {{\gamma}} _ {j} \theta \rangle \} \rangle \text {   otherwise. } \end{array} \right.
$$

Or select:

$$
c = \overline {{{\gamma}}} _ {1}, \overline {{{\gamma}}} _ {2}, \dots , \overline {{{\gamma}}} _ {k} \circ \leftarrow \tilde {\phi} _ {1}, \dots , \tilde {\phi} _ {n} \in P
$$

where $\psi _ { i }$ and $\gamma _ { j }$ for some $j$ are unifiable with . And then, establish a substate:

$$
\tau = \left\{ \begin{array}{l} \langle P - \{c \}, (! \phi_ {1} \theta , \dots ,! \phi_ {n} \theta), \theta , R \rangle \text {   if   } \tilde {\psi} _ {i} = ! \psi_ {i} \text {   and   } \tilde {\gamma} _ {j} = \gamma_ {j} \\ \langle P - \{c \}, (\tilde {\phi} _ {1} \theta , \dots , \tilde {\theta} _ {n} \theta), \theta , R \rangle \text {   otherwise. } \end{array} \right.
$$

If is transformed to:

$$
\tau^ {\prime} = \left\langle P ^ {\prime}, () \right., \Theta^ {\prime}, R ^ {\prime} \rangle ,
$$

then transform  to:

$$
\sigma^ {\prime} = \left\langle P ^ {\prime \prime}, \left(\tilde {\psi} _ {1} \Theta^ {\prime}, \dots , \tilde {\psi} _ {i - 1} \Theta^ {\prime}, \tilde {\psi} _ {i + 1} \Theta^ {\prime}, \dots , \tilde {\psi} _ {m} \Theta^ {\prime}\right), \Theta \circ \Theta^ {\prime}, R ^ {\prime} \right\rangle
$$

where:

$$
P ^ {\prime \prime} = \left\{ \begin{array}{l} P ^ {\prime} \cup \left\{\overline {{\gamma}} _ {1} \theta^ {\prime}, \ldots , \overline {{\gamma}} _ {k} \theta^ {\prime} \right\} \qquad \text {if} \tilde {\psi} _ {i} = ! \psi_ {i} \text {or} \overline {{\gamma}} _ {j} = ! \gamma_ {j} \\ P ^ {\prime} \cup \left\{\overline {{\gamma}} _ {1} \theta^ {\prime}, \ldots , \overline {{\gamma}} _ {j - 1} \theta^ {\prime}, \overline {{\gamma}} _ {j + 1} \theta^ {\prime}, \ldots , \overline {{\gamma}} _ {k} \theta^ {\prime} \right\} \text {otherwise.} \end{array} \right.
$$

## 3.2. Transformation rule 2

When $\tilde { \psi } _ { i } = \mathfrak { i } \psi _ { i }$ . If there exists $\overline { { \phi } }  \in P \mathrm { o r } \overline { { \phi } } \circ  \in P$ such that $\psi _ { i }$ and $\phi$ unify with , then transform $\sigma$ to:

$$
\sigma^ {\prime} = \left\langle P, \left(\tilde {\psi} _ {1} \theta , \dots , \tilde {\psi} _ {i - 1} \theta , \tilde {\psi} _ {i + 1} \theta , \dots , \tilde {\psi} _ {m} \theta\right), \Theta \circ \theta , L \right\rangle .
$$

## 3.3. Transformation rule 3

When $\tilde { \psi } _ { i } = @ \psi _ { i }$ . Establish a substate:

$$
\tau = \langle P, (\psi_ {i}), \Theta , L \rangle
$$

If  is converted to:

$$
\tau^ {\prime} = \left\langle P ^ {\prime}, (), \Theta^ {\prime}, L ^ {\prime} \right\rangle ,
$$

then transform to:

$$
\sigma^ {\prime} = \langle P, \left(\tilde {\psi} _ {1} \Theta^ {\prime}, \dots , \tilde {\psi} _ {i - 1} \Theta^ {\prime}, \psi_ {i + 1} \Theta^ {\prime}, \dots , \tilde {\psi} _ {m} \Theta^ {\prime}\right), \Theta \circ \Theta^ {\prime}, L \rangle .
$$

## 3.4. Transformation rule 4

When $\tilde { \psi } _ { i } = \sim \psi _ { i }$ . If there does not exist $\overline { { \phi } } \in P \mathrm { ~ o r ~ } \overline { { \phi } } \circ  \in P$ such that $\psi _ { i }$ and $\phi$ unify, then transform to:

$$
\sigma^ {\prime} = \left\langle P, \left(\tilde {\psi} _ {1}, \dots , \tilde {\psi} _ {i - 1}, \psi_ {i + 1}, \dots , \tilde {\psi} _ {m}\right), \Theta , L \right\rangle .
$$

## 3.5. Transformation rule 5

When $\tilde { \psi } _ { i } = \lnot \psi _ { i }$ . Establish a substate:

$$
\tau = \left\langle P, \left(\psi_ {i}\right), \emptyset , L \right\rangle .
$$

If is not converted to:

$$
\tau^ {\prime} = \left\langle P ^ {\prime}, (), \Theta^ {\prime}, L ^ {\prime} \right\rangle ,
$$

then transform to:

$$
\sigma^ {\prime} = \left\langle P, \left(\tilde {\psi} _ {1}, \dots , \tilde {\psi} _ {i - 1}, \psi_ {i + 1}, \dots , \tilde {\psi} _ {m}\right), \Theta , L \right\rangle .
$$

Given a resource program $P _ { 0 }$ and a query for which is a list of atomic formulas, if: $\sigma _ { 0 } = \langle P _ { 0 } , \Psi , \phi , \phi \rangle$

is transformed to:

$$
\overline {{{\sigma}}} = \langle \bar {P}, (), \overline {{{\Theta}}}, \bar {L} \rangle ,
$$

then we say the proof of $\psi$ succeeds. The success of the proof of $\psi$ means that $\psi$ is producible from $P _ { 0 }$ by using resources of $P _ { 0 }  – \overline { { P } }$

So far, resource programming allows simple resource expressions at the left-hand and right-hand side of a clause. However, by allowing § and (§ expressions at the left-hand side of a clause, we can increase the expressiveness of the resource programming. For instance: , $( \phi ^ { \prime }  \psi ^ { \prime } ) \circ  \psi$ means that if we consume $\psi$ then Ž . we can have or buy or produce resource $\phi$ and machine $\phi ^ { \prime }  \psi ^ { \prime }$ . For state:

$$
\sigma^ {\prime} = \left\langle P, \left(\tilde {\psi} _ {1}, \tilde {\psi} _ {2}, \dots , \tilde {\psi} _ {m}\right), \Theta , L \right\rangle ,
$$

we define an additional transformation rule.

## 3.6. Transformation rule 6

For $\tilde { \psi } _ { i }$ , if there exists clause $c \in P$ whose left-hand side contains:

$$
\overline {{\gamma}} _ {1}, \overline {{\gamma}} _ {2}, \dots , \overline {{\gamma}} _ {k} \leftarrow \tilde {\phi} _ {1}, \tilde {\phi} _ {2}, \dots , \tilde {\phi} _ {n} \text { or } \overline {{\gamma}} _ {1}, \overline {{\gamma}} _ {2}, \dots , \overline {{\gamma}} _ {k} \circ \leftarrow \tilde {\phi} _ {1}, \tilde {\phi} _ {2}, \dots , \tilde {\phi} _ {n}
$$

such that $\psi _ { i }$ and $\gamma _ { j }$ for some j are unifiable, then establish a substate:

$$
\tau = \left\{ \begin{array}{l} \langle   P, (\text { right - hand side of } c), \emptyset , \emptyset \rangle \quad \text { if } c \text { is a } \leftarrow \text { clause } \\ \langle   P - \{c \}, (\text { right - hand side of } c), \emptyset , \emptyset \rangle \text { if } c \text { is a } \circ \leftarrow \text { clause }. \end{array} \right.
$$

If it is transformed to:

$$
\tau^ {\prime} = \left\langle P ^ {\prime}, (), \Theta^ {\prime}, L ^ {\prime} \right\rangle ,
$$

then transform to:

$$
\sigma^ {\prime} = \left\langle P ^ {\prime \prime}, \left(\bar {\psi} _ {1}, \bar {\psi} _ {2}, \dots , \tilde {\psi} _ {m}\right), \Theta , L \cup \left\{\left\langle c, \tilde {\psi} _ {i} \right\rangle \right\} \right\rangle ,
$$

where:

$$
P ^ {\prime \prime} = \left\{ \begin{array}{l} P \cup \{\text { left   --   hand   side   of   } c \Theta^ {\prime} \} \quad \text { if   } c \text {   is   a   } \leftarrow \text { clause } \\ P \cup \{\text { left   --   hand   side   of   } c \Theta^ {\prime} \} - \{c \} \text {   if   } c \text {   is   a   } \circ \leftarrow \text { clause }. \end{array} \right.
$$

## 4. Petri net modeling

A Petri net 5 is a bipartite directed multigraph, which consists of two types of nodes called places and<sup>w</sup> <sup>x</sup> Ž transitions and directed arcs connecting a node of one type and a node of the other type. Formally, a Petri net is. defined 5 as a quadruple:<sup>w</sup> <sup>x</sup>

$$
\mathrm{PN} = \langle P, T, I, O \rangle ,\tag{4.1}
$$

where P is a finite set of places, T is a finite set of transitions, I: $T \to P ^ { \infty }$ is the input function, and $O \colon T  P ^ { \infty }$ is the output function, provided that $P ^ { \infty }$ stands for the set of all bags that are constructed with elements of P. A marked Petri net is a Petri net with tokens in places. A marking is defined as a vector:

$$
\mu = \big (\mu_ {1}, \mu_ {2}, \dots , \mu_ {n} \big),
$$

where $\mu _ { i } \geq 0$ represents the number of tokens assigned to, or residing in, place $p _ { i }$

![](/api/attachments/TARHF4J6/fulltext/images/9b4039ae9769b4f65c976d70bd71812fec896673ca5eedac9bba4a99ea19e8d1.jpg)  
Fig. 2. A sample marked Petri net. Circles are place nodes, bars are transition nodes, and bullets are tokens. Directed arcs Ž . ™ collectively represent input and output functions of transition nodes.

For instance, the Petri net in Fig. 2 is:

$$
\begin{array}{c c} P = \left\{p _ {1}, p _ {2}, p _ {3}, p _ {4}, p _ {5} \right\} \\ T = \left\{t _ {1}, t _ {2}, t _ {3}, t _ {4}, \right\} \\ I (t _ {1}) = \left\{p _ {1} \right\} & O (t _ {1}) = \left\{p _ {2}, p _ {3}, p _ {4}, p _ {4}, \right\} \\ I (t _ {2}) = \left\{p _ {2}, p _ {3}, p _ {4} \right\} & O (t _ {2}) = \left\{p _ {2} \right\} \\ I (t _ {3}) = \left\{p _ {5} \right\} & O (t _ {3}) = \left\{p _ {3}, p _ {4} \right\} \\ I (t _ {4}) = \left\{p _ {4}, p _ {4} \right\} & O (t _ {3}) = \left\{p _ {5} \right\}, \end{array}
$$

with the initial marking:

$$
\mu = (1, 0, 0, 2, 0).
$$

For bag B, let aŽ . b, B denote the number of occurrences of element b in B. Define, for transition $t _ { i } \in T$

$$
\nu_ {I} (t _ {i}) = \left(\# \left(p _ {1}, I (t _ {i})\right), \# \left(p _ {2}, I (t _ {i})\right), \dots , \# \left(p _ {n}, I (t _ {i})\right)\right)
$$

$$
\nu_ {O} (t _ {i}) = \big (\# \big (p _ {1}, O (t _ {i}) \big), \# \big (p _ {2}, O (t _ {i}) \big), \dots , \# \big (p _ {n}, O (t _ {i}) \big) \big).
$$

If $\mu \geq \upsilon _ { I } ( t _ { i } )$ , then transition $t _ { i }$ can fire. Upon the firing of $t _ { i } ,$ a new marking is established:

$$
\mu^ {\prime} = \mu - \nu_ {I} (t _ {i}) + \nu_ {O} (t _ {i})
$$

We logically represent a transition $t _ { i }$ by the following formula:

$$
O (t _ {i}) \leftarrow I (t _ {i})
$$

The marked Petri net in Fig. 2 is represented as:

$$
p (2), p (3), p (4), p (4) \leftarrow p (1)
$$

If the Petri net is attributed i.e., its tokens have attributes ,Ž . $p _ { i }$ Žfor $i = 1 , 2 , \ldots , 5 )$ are atomic formulas with variables specifying attributes, e.g.:

$$
\begin{array}{l} p (2, X, Y), p (3, Y), p (4, Y, X), p (4, Y, X) \leftarrow p (1, X, Y) \\ p (2, X, Z) \leftarrow p (2, X, Y), p (3, Y), p (4, Y, Z) \\ \vdots \\ p (4, X, Y). \end{array}
$$

![](/api/attachments/TARHF4J6/fulltext/images/c5c1afed599e9450b563251b1739e856d9bd8fd5a3725a53d860bae70c21a3b4.jpg)  
Fig. 3. Petri net extensions. The other type of arcs Ž . ™ ( , called inhibitor arcs, represents the input constraint that the connect place should have no token in order to fire the transition.

With the above representation, one can perform various Petri net analyses, such as boundedness and safeness tests. Say a program P representing a Petri net structure and its initial marking is given. If the proof of:

$$
\overbrace {p (X) , p (X) , \ldots , p (X)} ^ {k \text {times}}
$$

fails, then the Petri net is k-bounded. If it fails when k <sup>s</sup> 2, then the Petri net is safe. In general, the proof by the logic of resource for a Petri net is about the coÕerability problem. Say that is a bag of atomic formulas corresponding to a marking $\mu .$ Given a program representing a Petri net and its initial marking, if the proof of succeeds, it means there is a reachable marking $\mu ^ { \prime }$ such that $\mu ^ { \prime } \geq \mu .$ . A more restricted form of the coverability problem, called the reachability problem, can be addressed, too. If the proof of succeeds, but that of $\psi \cup \{ p ( X ) \}$ fails, then the marking represented by is reachable.

Resource programming supports various extensions to Petri nets. OR-transition $t _ { i } ,$ as in Fig. 3a, consumes a token from only one of $p _ { j }$ and $p _ { k }$ . It can be expressed with two clauses:

$$
\begin{array}{l} p (l) \leftarrow p (j) \\ p (l) \leftarrow p (k), \end{array}
$$

which can be equivalently represented with a Petri net without OR-transition, as illustrated in Fig. 4. Often, we express different meanings with an OR-transition: that is, even if both $p _ { j }$ and $p _ { k }$ have a token, the firing should produce exactly one token in $p _ { l } .$ . Then, we represent the situation as follows:

$$
\begin{array}{l} p (l) \leftarrow p (j), \sim p (k) \\ p (l) \leftarrow p (k), \sim p (j) \\ p (l) \leftarrow p (j), p (k). \end{array}\tag{4.2}
$$

Another form of OR-transition is an exclusive OR-transition, as illustrated in Fig. 3b. That is, the transition requires exactly one of input places to have a token. We represent this situation as:

$$
\begin{array}{l} p (l) \leftarrow p (j), \sim p (k) \\ p (l) \leftarrow p (k), \sim p (j) \end{array}\tag{4.3}
$$

A more significant extension to Petri net is done with the introduction of another type of arcs as shown in Ž Fig. 3c , called. Ž inhibitor arcs, restricting the input of a transition i.e., connecting from a place to a transition, not vice versa . A Petri net with such arcs requires re-definition of its structure Eq. 4.1 , especially the input . Ž Ž .. function, such that I: $T \to P ^ { \infty } \cup 2 ^ { \overline { { P } } }$ is the input function where for every $t _ { i } { \mathrm { : } }$

![](/api/attachments/TARHF4J6/fulltext/images/cd0671bb33433ffa9c4eb24988320f2061e270c881667d9244985aa4e7dd918d.jpg)  
Fig. 4. Alternative representation of an OR-transition.

![](/api/attachments/TARHF4J6/fulltext/images/75d9ce368f24151873b30117c067b9b2dcf2a9fc3a7a9b14333d7b18b7fdae3c.jpg)

![](/api/attachments/TARHF4J6/fulltext/images/96a5db35de8af21bf11ac8df538120b99e2a17d7a24a5b865e5f3efc73e2f91a.jpg)  
(a) An OR-Transition  
(b) An XOR-Transition  
Fig. 5. Representation of an OR-transition with inhibitor arcs.

$$
\hat {I} (t _ {i}) \cap \left\{p _ {j} | \bar {p} _ {j} \in \bar {I} (t _ {i}) \right\} = \phi
$$

$$
\hat {I} (t _ {i}) \cup \bar {I} (t _ {i}) = \bar {I} (t _ {i}),
$$

provided that $\hat { I } ( t _ { i } ) \in P ^ { \infty }$ and $\bar { I } ( t _ { i } ) 2 ^ { \bar { P } } .$ . Note, $2 ^ { \frac { \ d } { P } }$ stands for the power set of ${ \overline { { P } } } ,$ that is, the set of all subsets of ${ \overline { { P } } } _ { \mathrm { { : } } }$ , where $\overline { { P } } = \{ \bar { p } _ { j } | p _ { j } \in P \}$ . Define, for transition $t _ { i } \in T$ with inhibitor arcs:

$$
\nu_ {I} (t _ {i}) = \left(\# \left(p _ {1}, \hat {I} (t _ {i})\right), \# \left(p _ {2}, \hat {I} (t _ {i})\right), \dots , \# \left(p _ {n}, \hat {I} (t _ {i})\right)\right)
$$

$$
\nu_ {O} (t _ {i}) = \big (\# \big (p _ {1}, O (t _ {i}) \big), \# \big (p _ {2}, O (t _ {i}) \big), \dots , \# \big (p _ {n}, O (t _ {i}) \big) \big).
$$

If $\mu \geq v _ { I } ( t _ { i } )$ and $\mu _ { j } = 0$ for every $\overline { { p } } _ { j } \in \bar { I } ( t _ { i } )$ , then transition $t _ { i }$ can fire. Upon the firing of $t _ { i } .$ , a new marking is established:

$$
\mu^ {\prime} = \mu - \nu_ {I} (t _ {i}) + \nu_ {O} (t _ {i}).
$$

We represent the transition with an inhibitor arcs of Fig. 3b.

$$
p (l) \leftarrow p (j), \sim p (k).
$$

It can be quickly observed that the above representation of an exclusive OR-transition Eq. 4.3 consists of twoŽ Ž .. instances of inhibitor representations. Thus, Fig. 3b can be equivalently represented as Fig. 5b. Similarly, the above inclusive OR-transition Eq. 4.2 can be translated into a number of transitions and places withŽ . Ž Ž .. inhibitor arcs, as shown in Fig. 5a.

Inhibitor arcs are also useful for the representation of switches: the same action results in different states depending on the current state. For instance, an on–off switch in Fig. 6 is represented as:

$$
\begin{array}{l} p (\text { on }) \leftarrow p (\text { switch }), p (\text { off }), \sim p (\text { on }) \\ p (\text { off }) \leftarrow p (\text { switch }), p (\text { on }), \sim p (\text { off }). \end{array}
$$

Occasionally, the whole switch, corresponding to Fig. 6, is represented with a different place shape, as in Fig. 7. The switch place $p _ { s }$ Ž . with a triangle shape has a token if $p _ { \mathrm { o n } }$ of Fig. 6 has a token; it has no token if $p _ { \mathrm { o f f } }$ has a token. After $t _ { a }$ fires, if $p _ { a }$ has a token, then the token is removed; otherwise, a token is created in $p _ { a } .$ . If $p _ { i }$ has a token but $p _ { s }$ does not, $t _ { t }$ fires. If both $p _ { i }$ and $p _ { s }$ have a token, $t _ { s }$ fires; but the token in $p _ { s }$ is not removed.

![](/api/attachments/TARHF4J6/fulltext/images/8885a9b3db6adeb086a67ed87784fa36939f1402f7dc7b26f08b94ddd5e6ecb6.jpg)  
Fig. 6. An on–off switch.

![](/api/attachments/TARHF4J6/fulltext/images/4ee46c3bc80d469f90269e2bd98e27840b109cc124686244d4791c8b5c3e5e21.jpg)  
Fig. 7. A sample use of switch. The triangle shape place represents a switch, corresponding to Fig. 6. If $t _ { s }$ and $t _ { t }$ swap the switch, then there should be an arc from each of $t _ { s }$ and $t _ { t }$ to $p _ { s }$

This can be equivalently represented as the Petri net in Fig. 8. The representation of Fig. 7 in resource programming is as follows.

$$
p (j) p \leftarrow (i), \sim p (\mathrm{s}, \mathrm{on})
$$

$$
p (k) \leftarrow p (i),; p (s, \mathrm{on})
$$

$$
p (s, \text { on }) \leftarrow p (a), p (s, \text { off })
$$

$$
p (s, \text { off }) \leftarrow p (a), p (s, \text { on }).
$$

## 5. Application: resource requirement planning

We demonstrate the use of resource programming with a simple resource requirement planning problem adapted from Ref. 6 . Consider a production procedure of snow shovels, as illustrated in Fig. 9. The production<sup>w</sup> <sup>x</sup> of a unit of snow shovel sv requires a unit of top handle assembly tha , four nails n , a shaft sh , a Ž . Ž . Ž . Ž . scoop–shaft connector ssc , four rivets r , and a unit of scoop assembly sa . A unit of top-handle assemblyŽ . Ž . Ž . Ž . Ž . Ž . Ž . tha requires two nails n , a top handle th , and a unit of bracket assembly ba . A unit of bracket assembly Ž . Ž . Ž . Ž . Ž .ba requires a bracket br and a coupler c . Finally, A unit of scoop assembly sa requires six rivets r , a scoop sc , and a blade bl . Ž . Ž .

The first thing is to find how many units of what resources are required to produce a unit of show shovel. The main production procedure is modeled as follows.

sv § tha, n, n, n, n, sh, ssc, r, r, r, r, sa.

tha § n, n, th, ba.

ba§br, c.

sa § r, r, r, r, r, r, sc, bl.

The modeling of the resource requirement part is somewhat tricky. We introduce a counter for each resource Ž . e.g., ‘n\_used’, ‘sh\_used’, etc. , with which we represent the required usage of resources as follows.

n, n\_used YŽ . Ž . § n\_used X , Y is X <sup>q</sup> 1.

sh, sh\_used YŽ . Ž . § sh\_used X , Y is $\Chi + 1$

![](/api/attachments/TARHF4J6/fulltext/images/1fb8458b2591856d81ecded04e55bc711847e0c5097620a20f3894ed71234a09.jpg)  
Fig. 8. Explosion of switch. The two normal arcs Ž .™ between $p _ { \mathrm { o f f } }$ and $t _ { t }$ Ž . can be replaced by an inhibitor arc ™( from $p _ { \mathrm { o n } }$ to $t _ { t } .$

![](/api/attachments/TARHF4J6/fulltext/images/0bef6973fc22840b0afe6c5ade77857d413c0e554b17abfd698ed222f031f004.jpg)  
Fig. 9. Snow shovel production procedure. Instead of drawing multiple directed arcs between transition and place nodes, we place an integer, which denotes the multiplicity of the occurrent of the arc.  
ssc, ssc\_used YŽ . Ž . § ssc\_used X , Y is X <sup>q</sup> 1.  
r, r\_used YŽ . Ž . § r\_used X , Y is X <sup>q</sup> 1.  
th, th\_used YŽ . Ž . § th\_used X , Y is X <sup>q</sup> 1.

br, br\_used YŽ . Ž . § br\_used X , Y is X <sup>q</sup> 1.  
c, c\_used YŽ . Ž . §c\_used X , Y is X<sup>q</sup>1.  
sc, sc\_used YŽ . Ž . §sc\_used X , Y is X<sup>q</sup>1.  
bl, bl\_used YŽ . Ž . § bl\_used X , Y is X <sup>q</sup> 1.  
Each resource counter has the initial value of 0.

<table><tr><td>n_used(0).</td><td>sh_used(0).</td><td>ssc_used(0).</td></tr><tr><td>r_used(0).</td><td>th_used(0).</td><td>br_used(0).</td></tr><tr><td>c_used(0).</td><td>sc_used(0).</td><td>bl_used(0).</td></tr></table>

When one unit of nail n is used, its usage is recorded as a unit of by-product ‘nŽ . \_used’. Thus, after the production of a unit of show shovel via:

by checking the by-products e.g., ‘n Ž . \_used’, ‘sh\_used’, etc. one can find the required resources for the production of a unit of snow shovel.

Suppose preparations of resources require time units as specified by Table 1. We assume that there is no restriction on manpower and production facility so that each resource’s production time is not affected by others unless there is a precedent relationship. We specify each resource as: resource\_name Ž .total\_time\_req,unit\_time\_req , where ‘total\_time\_req’ is the time required to prepare the resource and all preceding resources counted from the beginning of the whole production procedure and ‘unit\_time\_req’ is time required to prepare a unit of the resource only. We modify the above production procedure model as follows.

Table 1  
Time requirement for shovel production

<table><tr><td>Resource</td><td>Time units</td></tr><tr><td>Shovel assembly</td><td>1</td></tr><tr><td>Top handle assembly</td><td>1</td></tr><tr><td>Top handle</td><td>7</td></tr><tr><td>Bracket assembly</td><td>1</td></tr><tr><td>Bracket</td><td>1</td></tr><tr><td>Coupler</td><td>9</td></tr><tr><td>Nail</td><td>1</td></tr><tr><td>Shaft</td><td>9</td></tr><tr><td>Scoop–shaft connector</td><td>5</td></tr><tr><td>Rivet</td><td>4</td></tr><tr><td>Scoop assembly</td><td>1</td></tr><tr><td>Scoop</td><td>2</td></tr><tr><td>Blade</td><td>1</td></tr></table>

sv SVTime,1 Ž . §

tha T1, Ž . Ž . Ž . Ž . Ž . Ž . \_ , n T2,\_ , n T2,\_ , n T2,\_ , n T2,\_ , sh T3,\_ ,

ssc T4, Ž . Ž . Ž . Ž . Ž . Ž . \_ , r T5,\_ , r T5,\_ , r T5,\_ , r T5,\_ , sa T6,\_ ,

max T1,T2,T3,T4,T5,T6 ,MaxT , SVTime is MaxTŽ<sup>w</sup> <sup>x</sup> . <sup>q</sup>1.

tha THATime,1Ž .§

n T1,Ž . Ž . Ž . Ž . \_ , n T1,\_ , th T2,\_ , ba T3,\_ ,

max T1,T2,T3 ,MaxT , THATime is MaxTŽ<sup>w</sup> <sup>x</sup> . <sup>q</sup>1.

ba BATime,1 Ž .§

br T1,Ž . Ž . Ž \_ , c T2,\_ , max T1,T2 ,MaxT , BATime is MaxT<sup>w</sup> <sup>x</sup> . <sup>q</sup> 1.

r T1, Ž . Ž . Ž . Ž . Ž . Ž . \_ , r T1,\_ , r T1,\_ , r T1,\_ , r T1,\_ , r T1,\_ ,

sc T2,Ž . Ž . Ž \_ , bl T3,\_ , max T1,T2,T3 ,MaxT , SATime is MaxT<sup>w</sup> <sup>x</sup> . <sup>q</sup>1.

n 1,1 , n Ž . Ž . Ž . \_used Y § n\_used X , Y is X <sup>q</sup> 1.

sh 9,9 , sh Ž . Ž . Ž . \_used Y § sh\_used X , Y is X <sup>q</sup> 1.

ssc 5,5 , sscŽ . Ž . Ž . \_used Y § ssc\_used X , Y is X <sup>q</sup> 1.

r 4,4 , rŽ . Ž . Ž . \_used Y § r\_used X , Y is X <sup>q</sup> 1.

th 7,7 , thŽ . Ž . Ž . \_used Y § th\_used X , Y is X <sup>q</sup> 1.

br 1,1 , br Ž . Ž . Ž . \_used Y § br\_used X , Y is X <sup>q</sup> 1.

c 9,9 , cŽ . Ž . Ž . \_used Y §c\_used X , Y is X<sup>q</sup>1.

sc 2,2 , sc Ž . Ž . Ž . \_used Y § sc\_used X , Y is X <sup>q</sup> 1.

bl 1,1 , blŽ . Ž . Ž . \_used Y § bl\_used X , Y is X <sup>q</sup> 1.

Query:

(§ svŽ . T ,\_ .

returns the total time unit required to produce a shovel; that is ‘T <sup>s</sup> 12’. The latest start time for the preparation of a resource is obtained by the following.

sv\_time SVTimeŽ . Ž .§@sv T,TU , SVTime is T-TU.

tha\_time THATimeŽ . Ž . Ž . §@tha \_,TU , sv\_time T1 , THATime is T1-TU.

ba\_time BATime Ž . Ž . Ž . § @ba \_,TU , tha\_time T1 , BATime is T1-TU.

sa\_time SATimeŽ . Ž . Ž . § @sa \_,TU , sv\_time T1 , SATime is T1-TU.

n\_time NTimeŽ . Ž . Ž . Ž . § @n \_,TU , sv\_time T1 , tha\_time T2 ,

min T1,T2 ,MinT , NTime is MinT-TU.Ž<sup>w</sup> <sup>x</sup> .

sh\_time SHTimeŽ . Ž . Ž . §@sh \_,TU , sv\_time T1 , SHTime is T1-U.

ssc\_time SSCTimeŽ . Ž . Ž . §@ssc \_,TU , sv\_time T1 , SSCTime is T1-U.

r\_time RTime Ž . Ž . Ž . Ž . § @r \_,TU , sv\_time T1 , sa\_time T2 ,

min T1,T2 ,MinT , RTime is MinT-TU. Ž<sup>w</sup> <sup>x</sup> .

th\_time THTimeŽ . Ž . Ž . §@th \_,TU , tha\_time T1 , THTime is T1-U.

br\_time BRTimeŽ . Ž . Ž . §@br \_,TU , ba\_time T1 , BRTime is T1-U.

c\_time CTimeŽ . Ž . Ž . §@c \_,TU , ba\_time T1 , CTime is T1-U.

sc\_time SCTimeŽ . Ž . Ž . §@sc \_,TU , sa\_time T1 , SCTime is T1-U.

bl\_time BLTimeŽ . Ž . Ž . §@bl \_,TU , sa\_time T1 , BLTime is T1-U.

The earliest start time for the preparation of a resource is similarly obtained.

## 6. Concluding remarks

A logic of resource is presented and its computational model is studied in a variant of the logic programming paradigm. Also, it is shown that Petri nets are modeled and analyzed in the logic of resource. The primary use of the logic of resource is in the modeling of resource-oriented systems. For instance, the logic of resource provides an action planning tool. State fluents correspond to disposable resources, and actions as state transitionŽ operators are represented as durable machines. Given an initial state as a bag of resources and descriptions of. Ž . actions as a bag of machines , the logic of resource can be used to find courses of actions that meet aŽ . prescribed goal.

Semantics of the logic of resource and the computational complexity of its implementation are not addressed in this paper. Girard 2 proposed the phase semantics as a variation of Tarskian semantics in a denotational<sup>w</sup> <sup>x</sup> Ž semantics style and the coherent semantics as a variation of Heyting’s semantics in an operational semantics. Ž style . These two types of semantics can be used for the consideration of semantics of the logic of resource. On. the other hand, the computational aspect of linear logic was intensively studied in Ref. 3 . As for the study of<sup>w</sup> <sup>x</sup> the computational complexity, however, it seems sufficient to show the recursive enumerability of the logic programming implementation of the logic of resource. We leave this issue for the future study.

## References

<sup>w</sup> <sup>x</sup> 1 K.R. Apt, Introduction to logic programming, Technical Report TR-87-35 Revised and Extended Version , Department of ComputerŽ . Science, The University of Texas at Austin, 1988.

<sup>w</sup> <sup>x</sup> 2 J.-Y. Girard, Linear logic, Theor. Comput. Sci. 50 1987 1–102.Ž .

<sup>w</sup> <sup>x</sup> 3 P.D. Lincoln, Computational Aspects of Linear Logic, PhD Thesis, Department of Computer Science, Stanford University, 1992.

<sup>w</sup> <sup>x</sup> 4 J.W. Lloyd, Foundations of Logic Programming, 2nd edn., Springer-Verlag, Berlin, 1987.

<sup>w</sup> <sup>x</sup> 5 J.L. Peterson, Petri Net Theory and the Modeling of Systems, Prentice-Hall, Englewood Cliffs, NJ, 1981.

<sup>w</sup> <sup>x</sup> 6 T.E. Vollmann, W.L. Berry, D.C. Whybark, Manufacturing Planning and Control Systems, 3rd edn., Irwin, Burr Ridge, IL, 1992.

![](/api/attachments/TARHF4J6/fulltext/images/33f63ea38aec9e1bf2a840aafb30085b6c9f7fa9412cc316a2bf264726ffbad9.jpg)

Young U. Ryu has been Assistant Professor at the Department of Decision Sciences, The University of Texas at Dallas since 1992. He received a Ph.D. degree in Management Science and Information Systems from The University of Texas at Austin, where he had been Assistant Instructor for 4 years. He also holds an MBA degree in Engineering Management Dallas and a BS degree in Mechanical Engineering Seoul National Univ. . HisŽ . Ž . research interests include logic-based modeling of systems, constraint reasoning, artificial intelligence methods, and decision theories, which are applied to legal reasoning, commodity trading, and production planning. His research papers have appeared in Knowledge Based Systems, Data and Knowledge Engineering, Annals of Operations Research, Decision Support Systems, and Journal of Management Information Systems.
