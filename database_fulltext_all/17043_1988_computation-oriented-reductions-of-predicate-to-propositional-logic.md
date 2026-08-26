---
otero_id: 17043
otero_key: "4D9Z36RU"
title: "Computation-oriented reductions of predicate to propositional logic"
authors: "Robert G Jeroslow"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90128-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computation-Oriented Reductions of Predicate to Propositional Logic

Robert G. JEROSLOW $^{1}$

College of Management, Georgia Institute of Technology, Atlanta, GA 30332-0520, USA

We give a sequential reduction technique for transforming a formula of the pure predicate calculus to a sequence of 'increasingly accurate' propositional logic 'approximations' to the predicate formula. At each stage of approximation, one of the following three cases occurs: (1) the approximation shows the predicate formula to be satisfiable; or (2) the approximation shows the predicate formula to be unsatisfiable; or (3) neither (1) nor (2) occurs, and a 'more accurate' refinement of the current propositional 'approximation' is obtained. The overall reduction technique is finite for the $\vec{\forall}$ -, $\vec{\exists}$ -, and $\vec{\exists}$ -satisfiability fragments of pure logic. In fact, it achieves the proven complexity bounds of Lewis [38] for these fragments, where nondeterminism is replaced by exponentiation. Since discrete programming and mixed integer programming can be used to treat propositional logic, this sequential reduction technique opens further possibilities for applications of mathematical programming to logic-based methods of decision support. In this respect, there is particular interest in the combination of logic with the nonlogical side constraints typical in mathematical programming, which are not efficiently handled by logic alone (e.g., material balances, capacity restrictions, demand requirements, etc.).

Keywords: Integer Programming, Theorem-proving, Branch-and-bound, Artificial Intelligence.

![](/api/attachments/4D9Z36RU/fulltext/images/80a30175b1e9b1f3cab897b0eb5caecbf4928d2e1fadb2a228c909c393eb78ae.jpg)

Robert G. Jeroslow is Professor in the College of Management at the Georgia Institute of Technology, and also Adjunct Professor in the School of Industrial and Systems Engineering. He received the B.S. in Industrial Engineering from Columbia University in 1964 and the Ph.D. in Mathematical Logic from Cornell University in 1969. His research interests are applied artificial intelligence, decision support systems, information systems, applied logic, knowledge representation for discrete optimization, operations management, strategic planning, and strategy.

This research is partially supported by National Science Foundation Grant MCS-8304075, USA.

## Introduction

In recent years, there has been increasing interest in enhancing decision support capabilities by combining databases with the quantitative models of Operations Research, and in providing some ‘intelligent’ capabilities for drawing inferences from data, model structure, and model calculations [7].

First order logic [52] plays an important role in the areas of data handling and inference, as it is directly focused on logical deduction and it interfaces well with relational databases [45]. In some instances, logic can provide an efficient representation of models and of knowledge [34]; or it may appear as an ‘as needed’ procedural attachment in a different representational scheme, such as frames [2]; or it may be used to structure the calling of representational schemes.

In this paper, we show an interconnection between first order logic (i.e., the first order predicate calculus) and discrete programming. This provides the potential for the techniques and decision support models of discrete programming to be utilized within the important logic modules of decision support systems, rather than simply being juxtaposed within such systems as a separate and unrelated part of the Operations Research modules.

We provide a sequential reduction of the classical predicate logic to classical propositional logic and we develop means of implementing these reductions in computational settings. Our approach utilizes the efficiently-calculated Prenex Normal Form of a given sentence, but it does not require the exponential-space procedure for the calculation of a clausal (i.e., conjunctive normal) form and (in particular) is not restricted to Horn clauses. The approach can utilize the algorithm for unification of lists of terms [37], [47]. It is designed to be implemented with a possible type structure on variables and constants, and allows implicit handling of a relational database.

At each point in the implementation, a partial reduction of the theorem-proving task is at hand. The partial reduction is evaluated by means of truth valuations, as in propositional logic, and two results (Lemma 2.2.1 and 2.2.2) provide conditions under which the partial reduction is adequate to determine whether or not the given sentence is valid. When these 'fathoming' conditions are not satisfied, a further partial reduction is obtained using unification, and the process continues. For sentences of the $\vec{\exists}$ , $\vec{\forall}$ , and $\vec{\exists\forall}$ sort, the process is finite. In fact, it achieves the complexity bounds of Lewis [38] for these fragments, when nondeterminism is replaced by exponentiation. Most conventional theorem-proving techniques do not have this latter property. Moreover, in our method the necessary unifications are guided by propositional truth valuations, to focus work where unifications are needed (see our discussion in section 2.2).

By placing most of the work of theorem-proving into propositional logic, techniques from integer and mixed-integer programming become available to assist the process, and these can be particularly effective as they now stand [5]. Moreover, as we will show in subsequent papers, mixed-integer programming approaches for propositional logic can be substantially expanded and refined, while always retaining the ability to carry, along with logic itself, general linear constraints and a linear criterion vector. Such constraints arise from, e.g., budget or resource restrictions, material balance equations, multiple goal formulations, etc. These restrictions are not easily treated efficiently in conventional approaches to logic.

The plan of the paper is as follows.

In section 1, the basic theoretical reductions (due largely to Herbrand) of predicate to propositional logic are recalled [52], in both validity and satisfiability forms, and several consequences of these reductions are obtained. Among such corollaries is the fact that validity for purely existential sentences of predicate logic (or, equivalently, satisfiability for purely universal sentences) is at least exponential time.

Validity for such sentences has been associated with query-answering from databases [45]. Consequently, simply the database applications of theorem-proving have a complexity well beyond that of the NP-completeness associated with mixed-integer programs and other discrete programs.

In section 2, which is the main part of the paper, we develop two means of implementing the theoretical reductions of section 1, in a way which tends to limit their potentially exponential growth. The first means (discussed in subsection 2.1) is the concept of a type for predicate variables and constants. The second means (discussed in subsection 2.2) is what we call partial instantiation, which is developed by analogy with partial enumeration, where lemmas from logic are needed as 'fathoming' (i.e., as search-curtailing) devices. We also provide several worked examples of our method.

In section 3, we relate our results, on the purely existential fragment of predicate logic, to the approach of Reiter on database query answering.

## 1. Preliminary Reductions of Predicate to Propositional Logic

In this section, we address some general issues of theoretical interest, concerning reductions of fragments of predicate logic to propositional logic. The main results are Theorem 1.1 and Corollary 1.4. Theorem 1.1 is well-known in several equivalent forms, and essentially due to Herbrand.

We treat a predicate logic with symbols for individuals ('constants'), but without equality and without function symbols. In this way, we can achieve sharper results. E.g., the inclusion of function symbols allows reduction of the entire predicate logic to its $\vec{\forall}$ -validity fragment, a fact which prevents characterizations like Theorem 1.1(b) for that fragment. However, our approach can be extended to include computed functions.

We refer the reader to excellent texts (eg. [39], [52]) for a fuller discussion of predicate and propositional logic. We provide only some intuitive discussion of the concepts from logic which we utilize.

The propositional connectives are the disjunction ‘∨’ read: ‘or’), the conjunction ‘∧’ (read: ‘and’), the negation ‘¬’ (read: ‘not’), the implication ‘⊃’ (read: ‘implies’), and the bi-conditional ‘↔’ (read: ‘if and only if’). By assigning a truth value to the constituent letters of a formula in only propositional connectives, one can determine a truth value for the formula. For example, if P and Q are ‘true’ and R is ‘false’, then $(P \lor R) \land \neg(Q \land R)$ is ‘true’. A formula is called a tautology if it is true for all truth valuations of its letters; e.g., $P \vee \neg P$ is a tautology. A formula is satisfiable if it is true for at least one truth valuations of its letters, or equivalently, if its negation is not a tautology.

The logical quantifiers are the existential quantifier ‘∃’ (read: ‘there exists’) and the universal quantifier ‘∀’ (read: ‘for every’). E.g., $(\forall x_{1})((\exists x_{2})B(x_{1}, x_{2}) \vee \neg C(x_{1}))$ is read: ‘for every $x_{1}$ , either there is an $x_{2}$ with $B(x_{1}, x_{2})$ true, and/or $C(x_{1})$ is false’ (thus the possibility of both $B(x_{1}, x_{2})$ and $\neg C(x_{1})$ is allowed). Here $B(x_{1}, x_{2})$ is a two-place relation on an underlying set, and $C(x_{1})$ is a one-place relation on it (i.e., $C(x_{1})$ defines a subset).

A model M for predicate logic consists of a set S, together with: (a) An assignment of an element of S for each constant; (b) An assignment of a subset of $S^{k}$ for each relation symbol $B(x_{1},\ldots,x_{k})$ of predicate logic. The cardinality of M is that of its underlying set S.

For a well-formed formulae (wff) A of predicate logic, its universal closure $A'$ is obtained by prefacing A with a universal quantifier for each predicate variable in A that is free in A, i.e., that is not in the scope of a logical quantifier. This results in a sentence, i.e., a wff with no free variables. For any sentence A and model M, the statement 'A is true in M' has its natural, intuitive meaning (see, e.g., [39], [52]).

For a sentence, $A$ , $\models A$ (read: 'A is valid') abbreviates the fact that $A$ is true in every model; $\models^{F}A$ abbreviates that $A$ is true in every finite model; and $\models^{M}A$ abbreviates that $A$ is true in every model for which all its elements are designated by the constants (i.e., individual symbols) occurring in $A$ (or, if $A$ has no symbols, that $A$ is true in every one-element model).

Similarly, $\mathcal{I} \models A$ (for a theory $\mathcal{I}$ ) abbreviates that $A$ is true in every model in which $\mathcal{I}$ is true. For $\mathcal{I}$ finite, it is known that $\mathcal{I} \models A$ iff $\models C \supset A$ , where $C$ is the conjunction of the formulas of $\mathcal{I}$ . More generally, $\mathcal{I} \models A$ iff for some finite subtheory $\mathcal{J}$ of $\mathcal{I}$ , we have $\mathcal{J} \models A$ .

A sentence A is quantifier-free (or: a proposition) if no logical quantifiers occur in A. Thus, if a relation symbol B occurs in A, it occurs as, e.g., $B(c_{1},\ldots,c_{k})$ where the $c_{i}$ are constants $1 \leq i \leq k$ , and B is a k-place relation symbol. We say that $(c_{1},\ldots,c_{k})$ is an instantiation for $B(x_{1},\ldots,x_{k})$ .

Proposition 1.1. Suppose that $A$ is a quantifier-free sentence. Then $\models A$ iff $\models {}^F A$ iff $\models {}^M A$ iff $A$ is a tautology.

Proof. If A is not a tautology, there is a truth valuation on the set of all propositions in which A is false.

From this valuation, we may construct a model M as follows. For any predicate symbol B and vector $\vec{c}$ of constants occurring in A, such that $\vec{c}$ is congruent with B, we set $B(\vec{c})$ true in M iff $B(\vec{c})$ is valued ‘true’.

Then A is false in M. Hence, $\models^{M}A$ is false; thus also $\models^{F}A$ and $\models A$ are false.

If $A$ is a tautology, then immediately $\models A$ follows. Thus also $\models {}^F A$ and $\models {}^M A$ . Q.E.D.

We shall be particularly concerned with the relationship between certain fragments of predicate logic, and its quantifier-free fragment. From our perspective, the quantifier-free fragment is merely a propositional logic. However, due to the pattern of instantiations, it is also highly structured. Our next result concerns the quantifier-free fragment of predicate logic.

Let $A = (\exists x)B(x)$ , where $B$ is quantifier-free, and let $C = \{c_1, \ldots, c_t\}$ be a non-empty list of constants. Define $A^* = \bigvee_{c \in C} B(c)$ . Similarly, if $A = (\forall x)B(x)$ , then define $A^* = \bigwedge_{c \in C} B(c)$ . For general quantified wff $A$ , define $A^*$ inductively in this manner, working from the smallest subformula of $A$ outward to subformulas which contain these. Then the following result is easily established by a suitable induction on the number of quantifiers occurring in $A$ .

Proposition 1.2. Let $A$ be a wff, $B$ a subformula of $A$ , and $A'$ the result when $B$ is replaced by $B^*$ in $A$ . Here $C = \{c_1, \ldots, c_t\}$ is the set of all constants occurring in $A$ , if any; while $C = \{c\}$ for some constant $c$ if no constants occur in $A$ . Then $\models^M A$ iff $\models^MA'$ . In particular $\models^MA$ iff $\models^MA^*$ .

Let $x = (x_{1}, \ldots, x_{n})$ be a vector of $n$ individual predicate variables. For a wff $A(x) = A(x_{1}, \ldots, x_{n})$ , we let $(\exists \vec{x})A(\vec{x})$ abbreviate $(\exists x_{1})\ldots(\exists x_{n})A(x_{1}, \ldots, x_{n})$ ; and $(\forall \vec{x})A(\vec{x})$ abbreviates $(\forall x_{1})\ldots(\forall x_{n})A(x_{1}, \ldots, x_{n})$ .

Techniques for proving our next result can be obtained from the proof of Proposition 1.1 and from Henkin [24] and, as regards in part(d), from G. Sacks. We omit the proofs as variants of Theorem 1.1 are well-known and available with proofs elsewhere (e.g., [52]).

In the next and main section, we utilize Theorem 1.1(a), in its equivalent form of Corollary 1.4(b), as an important element of our approach to theorem proving. As regards motivation for Theorem 1.1(a), since $(\exists \vec{x})B(\vec{x})$ asserts the existence of a vector of objects $\vec{c}$ such that $B(\vec{c})$ is true, it is not surprising that its truth in all models (i.e., validity) would require $B(\vec{c})$ necessarily true for some $\vec{c}$ drawn from constants in $B(\vec{x})$ .

Theorem 1.1. Let B be quantifier-free and let C be the set of constants occurring in B, if any; otherwise $C = \{c\}$ where c is a constant, if no constants occur in B. Let $\vec{C}$ denote the set of vectors of constants from C, of length suitable for instantiation in B. Then

(a) $\models (\exists \vec{x})B(\vec{x})\quad iff\quad \models {}^F (\exists \vec{x})B(\vec{x})\quad iff\quad \models {}^M$ $(\exists \vec{x})B(\vec{x})\text{iff}\vee_{\vec{c}\in \vec{C}}B(\vec{c})$ is a tautology.

(b) $\models (\forall \vec{x})B(\vec{x})\quad iff \quad \models {}^F (\forall \vec{x})B(\vec{x})\quad iff \quad B(\vec{d})\quad is\quad a$ tautology, where $\vec{d}$ is a vector of distinct constants, none of which occur in $B$ .

(c) $\models (\forall \vec{x})(\exists \vec{y})B(\vec{x},\vec{y})$ iff $\models {}^F (\forall \vec{x})(\exists \vec{y})B(\vec{x},\vec{y})$ iff $\bigvee_{\vec{g}\subseteq \vec{G}}B(\vec{d},\vec{g})$ is a tautology. Here $d$ is a vector of distinct constants, none of which occur in $B$ , and $\vec{G}$ consists of all vectors of the dimension of $\vec{y}$ , whose elements are drawn from $C$ or the elements of $\vec{d}$ .

(d) Put $D_0 = \emptyset$ , $D_1 = C$ , and inductively, with $\vec{D}_n$ the set of all vectors in $D_n$ of appropriate dimension, let $g(\vec{d})$ for $\vec{d} \in \vec{D}_n$ be a vector of constants not in $D_n$ nor in any $g(\vec{d}')$ for $\vec{d}' \neq \vec{d}$ , $\vec{d}' \in D_n$ ; and let $D_{n+1}$ be the union of $D_n$ with all constants occurring in all $g(\vec{d})$ for $\vec{d} \in \vec{D}_n$ . (Thus $g$ is not a function symbol). Let $A_n$ be $\bigvee_{\vec{d} \in \vec{D}_n \setminus \vec{D}_{n-1}} B(\vec{d}, g(\vec{d}))$ .

Then $\models (\exists \vec{x})(\forall \vec{y})B(\vec{x},\vec{y})$ iff, for some $n$ , $A_{1}\vee A_{2}\vee \dots \vee A_{n}$ is a tautology.

Corollary 1.1. Suppose that $B$ has no occurrences of constants. Then $\models (\exists \vec{x})B(\vec{x})$ iff $B$ is true in every one-element model iff $\models (\forall \vec{x})B(\vec{x})$ .

Corollary 1.2. Suppose that $B$ has no occurrences of constants. Then $\models (\forall \vec{x})(\exists \vec{y})B(\vec{x},\vec{y})$ iff in every model M and for each vector $\vec{h}$ of elements of M, there is a vector $\vec{k}$ of elements of $\vec{h}$ such that $B(\vec{h}, \vec{k})$ is true in M.

Corollary 1.3. Suppose that $B$ has $n'$ occurrences of distinct constants, and let $n = \max\{1, n'\}$ . Then if $\vec{x}$ has $t$ elements, $\models (\forall \vec{x})B(\vec{x})$ iff $(\forall \vec{x})B(\vec{x})$ is true in every model with $\leq n + t$ elements. Similarly, $\models (\forall \vec{x})(\exists \vec{y})B(\vec{x}, \vec{y})$ iff $(\forall \vec{x})(\exists \vec{y})B(\vec{x}, \vec{y})$ is true in every model with $\leq n + t$ elements.

Corollary 1.4. Let $B, C, \vec{d}, \vec{g}, \vec{G}, D_k$ and $A_k$ be as in Theorem 1, with $D_\infty = \bigcup_{k=1}^\infty D_k$ . Let $n$ and $t$ be as in Corollary 1.3.

(a) $(\exists \vec{x})B(\vec{x})$ is satisfiable iff $B(\vec{d})$ is satisfiable iff $(\exists \vec{x})B(\vec{x})$ has a model of size $\leq n + t$ elements.

(b) $(\forall \vec{x})B(\vec{x})$ is satisfiable iff $\bigwedge_{\vec{c}\in \vec{C}}B(\vec{c})$ is satisfiable iff $(\forall \vec{x})B(\vec{x})$ has a model of $\leq n$ elements.

(c) $(\forall \vec{x})(\exists \vec{y})B(\vec{x},\vec{y})$ is satisfiable iff there is a truth valuation satisfying all $B(\vec{d},g(\vec{d}))$ simultaneously for all $\vec{d}\in D_{\infty}$ .

(d) $(\exists \vec{x})(\forall \vec{y})B(\vec{x}, \vec{y})$ is satisfiable iff $\Lambda_{\vec{g}\in\vec{G}}B(\vec{d},\vec{g})$ is satisfiable iff $(\exists \vec{x})(\forall \vec{y})B(\vec{x},\vec{y})$ has a model of $\leq n+t$ elements.

Proof. The method of proof is the same in all cases (a)-(d). We illustrate it for the case (c):

$(\forall \vec{x})(\exists \vec{y})B(\vec{x},\vec{y})$ is satisfiable

$\leftrightarrow \mathbf{not} - \models (\exists \vec{x})(\forall \vec{y})B(\vec{x},\vec{y})$

$\Leftrightarrow$ (by Theorem 2(d)) it is not the case that, for some $n A_1' \vee \ldots \vee A_n'$ is a tautology (with $A_i' = \bigvee_{\vec{d} \in \vec{D}_i \setminus \vec{D}_{i-1}} B(\vec{d}, g(\vec{d}))$ )

$\leftrightarrow$ for all $n, \neg A_i'$ for $1 \leq i \leq n$ are simultaneously satisfiable

$\leftrightarrow$ (by compactness) there is a truth valuation satisfying all $\neg A_{n}^{\prime}$ simultaneously, for all $n$ , $\leftrightarrow$ there is a truth valuation satisfying all $B(\vec{d}, g(\vec{d}))$ simultaneously for all $\vec{d} \in \vec{D}_{\infty}$ . Q.E.D.

Our result Corollary 1.4(d) is closely related to Lewis' result in [38] on an upper bound for the satisfiability of formulas $(\exists \vec{x})(\forall \vec{y})B(\vec{x},\vec{y})$ of the 'Schonfinkel-Bernays' type. As shown in [38], the bound on the size of a model yields a nondeterministic exponential time procedure for satisfiability. Lewis also shows that a lower bound of this type is also best possible, which is quite significant in view of the provably high complexity. This contrast with complexity measures of the type NP or PSPACE (see, e.g., [17], [33]).

Using the undecidability of predicate logic [55], one easily shows that the validity of formulas of the type $(\exists \vec{x})(\forall \vec{y})B(\vec{x},\vec{y})$ is likewise undecidable, via reductions of the entire predicate calculus to such formulas. The reduction, via the equivalent satisfiability of $(\forall \vec{x})(\exists \vec{y})B(\vec{x},\vec{y})$ forms, proceeds in four steps: (a) First, the well-known technique of Skolem functions reduces an arbitrary predicate sentence $A$ (as regards satisfiability) to an equivalent one $A'$ with Skolem function symbols and only universal quantifiers (see, e.g., [52]); (b) Via the introduction of relation symbols for the graph of these functions, one achieves a sentence $A''$ of pure predicate logic in only universal quantifiers, such that $A$ is satisfiable exactly if $B\wedge A''$ is satisfiable where $B$ asserts that the functions have values for all arguments; (d) In view of the fact that the logical quantifier of $B$ are $\vec{\forall}\vec{\exists}$ , and of $A''$ are $\vec{\forall}$ , one notes that $B\vee A''$ is logically equivalent to $\vec{\forall}\vec{\exists}$ sentence, as claimed. We leave the details of the construction in (a)-(d) to the reader.

The undecidability of the $(\forall\vec{x})(\exists\vec{y})B(\vec{x},\vec{y})$ fragment of pure predicate logic substantially explains why Theorem 1.1(d) and Corollary 1.4(c) involve an equivalence to an infinite series of propositional forms. In fact, a careful study of our construction (a)–(d) of the last paragraph will reveal that the infinite series of propositional forms in the case of Corollary 1.4(c) is (essentially) the 'Henkin universe' or 'Skolem universe' of Henkin's well-known proof of the completeness of predicate logic (see [24]).

The following result is due to H. Lewis (recall that constant symbols are permitted here, but not in [38]).

Theorem 1.2. [38]. The complexity of the condition ‘(∀x)B(x) is satisfiable’ is exactly nondeterministic exponential time.

As we shall see in section 3, database query-answering involves the validity of $(\exists\vec{x})B(\vec{x})$ -form sentences, or, equivalently, the satisfiability of $(\forall\vec{x})B(\vec{x})$ -form sentences. By Theorem 1.2, such query answering is of substantially higher complexity than, e.g., mixed-integer programming (or even mixed-integer programs with such optimization in constraints, iteratively). Fortunately, not all predicate logic questions are in the high complexity classes, as we see in the next result.

Corollary 1.5. The condition ‘(∃x)B(x) is satisfiable’ is NP-complete.

Proof. By Corollary 1.4(a), it is in NP. However, it includes the satisfiability problem, so it is also NP-hard. Q.E.D.

Theorem 1.1 is closely related to Gentzen's Haupsatz in its extended form [18], which details how rules of propositional logic can be used to do 'most' of predicate reasoning, with the application of predicate rules occurring only in a restricted setting. In fact, Theorem 1.1 can be used to strengthen instances of the extended Haupsatz.

## 2. Two Techniques for Limiting the Extent of Instantiations

From Corollary 1.4(b), the satisfiability of $(\forall \vec{x})B(\vec{x})$ , for $B$ quantifier free, is reduced to the propositional issue of whether or not the propositional formula $\Lambda_{\vec{c} \in \vec{C}} B(\vec{c})$ is satisfiable. If $x$ is of length, say, less than three or four, (or if $|C| = 1$ ), this can by itself be a useful fact. However, in most other instances, one must avoid having even to form the instantiations $B(\vec{c})$ for all $\vec{c} \in \vec{C}$ .

In this section, we discuss two techniques which are aimed at limiting the extent of instantiations: (1) The use of the type [25] concept, which occurs naturally in the great majority of intended applications; (2) The use of partial instantiation, a more technical device, which is related to, both, the partial enumeration ideas of implicit enumeration and branch-and-bound and to resolution.

We begin with a discussion of the more intuitive concept of type.

Type is a widely-used technique for curtailing instantiation, and we provide a treatment of it here to place it in our framework in a rigorous manner. Following that discussion, we introduce the technique of partial instantiation, which is the central new feature of our approach.

## 2.1. Type

Quite often in a database setting, different predicate variables in $\vec{x}$ in the quantifier-free wff $B(\vec{x})$ , range over different fields [56]. Possibly $\vec{x} = (x_1, x_2, x_3)$ , where $x_1$ is a customer, $x_2$ is a city, and $x_3$ is total sales to that customer. Here $B$ (Apex Corporation, Philadelphia, \$503) is of the 'right syntactic type' whether or not it is true. However, $B$ (\$100, account receivable, \$503) is not of the proper syntactic type, and one should not need to form such an instantiation.

For simplicity in our exposition in subsequent sections, as well as for substantial savings in computation, we shall restrict ourselves to co-ordinate-wise types. I.e., each position (field) in a relation symbol shall have a restriction as to the type of individual constant which can be instantiated there, but otherwise there shall be no restriction. Furthermore, for each type there shall be at least one constant symbol of that type. This coordinate-wise type structure is not needed for the results in this section.

The following result allows a substantial restriction on instantiations, utilizing the type concept. We omit its (straightforward) proof.

Since $(\forall \vec{x})(\mathrm{Typ}_A(\vec{x}) \supset A(\vec{x})) \supset (\exists \vec{y})(\mathrm{Typ}_B(\vec{y}) \land B(\vec{y}))$ is logically equivalent (by Prenex laws) to $(\exists \vec{x})(\exists \vec{y})((\mathrm{Typ}_A(\vec{x}) \supset A(\vec{x})) \supset \mathrm{Typ}_B(\vec{y}) \land B(\vec{y}))$ , Theorem 1.1(a) applies. In models where the type structure is completely specified (via the formula $T$ in Proposition 2.1.1 below), the equivalence of (2.1.1) and (2.1.2), as asserted below, is not surprising.

Proposition 2.1.1. Let $A(\vec{x})$ , $B(\vec{y})$ , $\text{Typ}_A(\vec{x})$ and $\text{Typ}_B(\vec{y})$ be quantifier-free formulas, and $D$ a quantifier free sentence, such that no predicate symbol occurring in either $\text{Typ}_A$ or $\text{Typ}_B$ also occur in either $A, B$ or $D$ . Let $C$ be the set of all constants in $A, B, D$ , $\text{Typ}_A$ or $\text{Typ}_B$ , or, if none occur, let $C = \{c\}$ . Let $\vec{C}_1$ respectively $\vec{C}_2$ denote all sequences from $C$ of the length of $\vec{x}$ resp. $\vec{y}$ . Finally, let $T$ be propositionally equivalent to the conjunction $T'$ containing exactly one of $\text{Typ}_A(\vec{c}_1)$ or $\neg \text{Typ}_A(\vec{c}_1)$ for each $\vec{c}_1 \in \vec{C}_1$ , and exactly one of $\text{Typ}_B(\vec{c}_2)$ or $\neg \text{Typ}_B(\vec{c}_2)$ for each $\vec{c}_2 \in \vec{C}_2$ .

Then

$$
\begin{array}{r l} T \wedge D & \vDash (\forall \vec {x}) \big (T y p _ {A} (\vec {x}) \supset A (\vec {x}) \big) \\ & \supset (\exists \vec {y}) \big (T y p _ {B} (\vec {y}) \wedge B (\vec {y}) \big), \end{array}\tag{2.1.1}
$$

$$
\begin{array}{l} \text {exactly if} \\ D \supset \bigvee_ {\vec {c} _ {1} \in \vec {C} _ {1}} \bigvee_ {\vec {c} _ {2} \in \vec {C} _ {2}} \left\{A (\vec {c} _ {1}) \supset B (\vec {c} _ {2}) \mid T y p _ {A} (\vec {c} _ {1}) \right. \\ \quad \text {and} T y p _ {B} (\vec {c} _ {2}) \text {occur in} T ^ {\prime} \Big \} \end{array}
$$

is a tautology.

(2.1.2)

Corollary 2.1.1. Let $B(\vec{y})$ , $\text{Typ}(\vec{y})$ and $D$ be quantifier-free, with no free variables in $D$ , such that no predicate symbol occurring in $\text{Typ}(\vec{y})$ also occurs in either $B$ or $D$ . Let $C$ be the set of constants occurring in $B$ , $\text{Typ}(\vec{y})$ , or $D$ , or if none occur, let $C = \{c\}$ . Let $\vec{C}$ denote all sequences from $C$ of the length of $\vec{y}$ . Finally, let $T$ be a conjunction containing exactly one of $\text{Typ}(\vec{c})$ or $\neg \text{Typ}(\vec{c})$ for each $\vec{c} \in \vec{C}$ .

Then

$$
T \wedge D \vDash (\exists \vec {y}) (T y p (\vec {y}) \wedge B (\vec {y})),\tag{2.1.3}
$$

exactly if

$$
D \supset \bigvee_ {\vec {c} \in \vec {C}} \left\{B (\vec {c}) \mid T y p (\vec {c}) o c c u r s i n T \right\}\tag{2.1.4}
$$

is a tautology.

In particular, if $\text{Typ}(\vec{y})$ is a relation symbol, $(\forall\vec{y})(\text{Typ}(\vec{y})\supset B(\vec{y}))$ is satisfiable in some model in which $D \wedge T$ is true, precisely if the propositional formula

$$
D \wedge \bigwedge_ {\vec {c} \in \vec {C}} \left\{B (c) \mid \text { Typ } (\vec {c}) \text {   occurs   in   } T \right\}\tag{2.1.5}
$$

is satisfiable.

Proposition 2.1.1 and Corollary 2.1.1 allow a substantial restriction in the number of propositions $B(\vec{c}), \vec{c} \in \vec{C}$ , etc., which need to be formed, as typically the set of instantiations which satisfy type restrictions is a very small fraction of all possible instantiations. Moreover, the 'long' conjunction $T$ can be used implicitly in (2.1.2) or (2.1.5), without actually being formed.

The following result is also easily established.

Corollary 2.1.2. Suppose that, in (2.1.2), $A(\vec{x})$ has the form $A_1(\vec{x}) \wedge A_2(\vec{x})$ , where $A_1(\vec{c}_1)$ is true whenever $\text{Typ}_A(\vec{c}_1)$ occurs in $T$ and $D$ is true.

Then (2.1.2) is a tautology exactly if

$$
\begin{array}{r l} D & \supset \bigvee_ {\vec {c} _ {1} \in \vec {C} _ {1}} \bigvee_ {\vec {c} _ {2} \in \vec {C} _ {2}} \left\{A _ {2} (\vec {c} _ {1}) \supset B (\vec {c} _ {2}) \mid T y p _ {A} (\vec {c} _ {1}) \right. \\ & \quad \text { and } T y p _ {B} (\vec {c} _ {2}) \text { occur   in } T ^ {\prime} \} \end{array}\tag{2.1.6}
$$

is a tautology, i.e., if any truth valuation making D true also makes the right-hand-side of (2.1.6) true.

Corollary 2.1.2 is cited in limiting the search for valuations which make (2.1.2) false, and also will be useful in section 3.

## 2.2. Partial Instantiation

In order to have a uniform setting in which to discuss partial instantiation, we shall take the setting of Corollary 2.1.1 and we will focus on the satisfiability equivalent (2.1.5) to validity. In addition, we will treat the database D (i.e., conjunction of known relational assertions, including negations) in an implicit manner.

Thus the queries we address here have the form: 'Given the known data $D$ , is it possible that $B(\vec{y})$ is true for every $\vec{y}$ of the appropriate type?' If the known data $D$ is complete (i.e., contains, for every relational assertion, either it or its negation), then this query is equivalent to: 'Does $B(\vec{y})$ evaluate to 'true' for every $\vec{y}$ of the appropriate type, where the truth valuation on relational assertions is obtained from $D$ ?' (Here 'relational' and 'atomic' have the same sense). In general, the first query is of a more general type than the second.

With the closed world assumption [45], any relational assertion not posited has its negation posited. Thus this assumption leads to an instance of a complete database. Indeed, since for most relations either the relation or its complement is of huge size, some form of default options are typically used when a complete database is desired. Here we are not concerned with such completeness.

Our technique, for avoiding the complete instantiation which occurs in (2.1.5), is called partial instantiation? It involves conjunctions of the form

$$
B _ {1} \wedge \dots \wedge B _ {t},\tag{2.2.1}
$$

in which each $B_{i}, 1 \leq i \leq t$ , arises by substituting, throughout $B(\vec{y})$ some constants of C for some variables in $\vec{y}$ . Initially, we will begin with $B(\vec{y})$ , a conjunction of one term.

While we write the conjunction (2.2.1) as an implicit list structure in $B_1, B_2, \ldots, B_t$ , actually the relation of 'refinement of' partially orders these formula, and the latter ordering structure is central to our method. Initially, with $B_1 = B(\vec{y})$ , $t = 1$ , the partial order is trivial. After we discuss unblocked valuations below, we will describe how it is extended.

We need to develop methods for deciding when we have already done enough computation on (2.2.1), to know whether or not (2.1.5) is satisfiable. Here this will be done via Lemmas 2.2.1 and 2.2.2.

An individual conjunct $B_{i}$ is said to cover $\vec{c} \in \vec{C}$ , where $\operatorname{Typ}(\vec{c})$ occurs in $T$ , if $B(\vec{c})$ arises by substituting, throughout $B_{i}$ , some constants of $C$ for some variables of $y$ . $B_{i}$ directly covers $\vec{c} \in \vec{C}$ if $B_{i}$ covers $\vec{c}$ and no strict refinement $B_{j}$ of $B_{i}$ covers $\vec{c}$ .

In the conjunctions (2.2.1) each $B_{i}, 1 \leq i \leq t$ , will directly cover at at least one $\vec{c} \in \vec{C}$ . A given $\vec{c} \in \vec{C}$ may, however, be directly covered by several $B_{i}$ depending on the details of a given implementation of the partial instantiation technique. Any given $\vec{c} \in \vec{C}$ for which $\operatorname{Typ}(\vec{c})$ holds will always be covered by some $B_{i}$ , in any case.

We shall consider truth valuations on the propositional letters contained in (2.2.1), where we understand that any distinct free variables occurring in a conjunct $B_{i}$ are viewed as if they were distinct new constants not occurring in C. Thus, e.g., $R(c_{1}, x_{1})$ , $R(c_{1}, x_{3})$ and $R(c_{1}, c_{2})$ are treated as distinct and unrelated propositional letters.

A truth valuation is variant independent if it gives the same truth value to all variants of the same atomic (relational) formula. Thus, $R(c_{1}, x_{1})$ and $R(c_{1}, x_{3})$ would have the same truth value in a variant independent valuation. (Recall that two formulas are variants if they differ only in the names of their variables). Variant independent valuations are useful in obtaining strong ‘fathom-ing tests’, as the following result shows.

Recall that the purpose of the fathoming tests in the next two lemmas, is to limit the need for further instantiation.

Lemma 2.2.1. If (2.2.1) is not satisfiable by a variant independent valuation in which $D$ is true, then neither (2.1.5) nor $T \wedge D \wedge (\forall \vec{y})(Typ(\vec{y}) \supset B(\vec{y}))$ are satisfiable.

Proof. For each type select one constant of that type and insert it in $B_{i}$ whenever a variable of that type appears, and call the result $B_{i}'$ .

$B_{1}^{\prime}\wedge\ldots\wedge B_{t}^{\prime}$ is part of the conjunction in (2.1.5), so if it is not satisfiable, neither is (2.1.5).

However, as a propositional form, $B_1' \wedge \ldots \wedge B_t'$ is an instance of $B_1 \wedge \ldots \wedge B_t$ , in which all variables of the same type have equal values, and in which some distinct propositional letters of $B_1 \wedge \ldots \wedge B_t$ may be the same in $B_1' \wedge \ldots B_t'$ . As $B_1 \wedge \ldots \wedge B_t$ is not satisfiable by a variant independent valuation with $D$ true, $B_1' \wedge \ldots \wedge B_t'$ is not satisfiable at all. Q.E.D.

Suppose now that a truth valuation is at hand which makes (2.2.1) and (T and) D both true. That truth valuation is called blocked if there are indices $1 \leq i$ , $j \leq t$ (possibly i = j) and partially or fully instantiated predicate letters R occurring in $B_{i}$ or D, and S occurring in $B_{j}$ , such that all the following conditions hold:

(2.2.2a) $R$ and $S$ have opposite truth values;

(2.2.2b) There is $\vec{c}_1 \in \vec{C}$ and either $R$ occurs in $B_i$ and $\vec{c}_1$ is directly covered by $B_i$ , or $R$ occurs in $D$ and is a predicate letter completely instantiated by $\vec{c}_1$ , and there is a $\vec{c}_2 \in \vec{C}_2$ directly covered by $B_j$ , for which $R$ and $S$ become identical in form, when $\vec{c}_1$ and $\vec{c}_2$ are instantiated in $B(\vec{y})$ .

In definition (2.2.2), we note that D, if satisfiable, cannot contain both a relational assertion and its negative. Hence, in (2.2.2b) we do not need to consider the case that S occurs in D, since at most one of R or S will occur in D if (2.2.2a) holds.

Lemma 2.2.2. If a truth valuation which makes $D$ and (2.2.1) true is not blocked, then (2.1.5) is satisfiable, and $(\forall \vec{y})(\text{Typ}(\vec{y}) \supset B(\vec{y}))$ is satisfiable with $D$ and $T$ true.

Proof. Let any $\vec{c} \in \vec{C}$ be given which meets all type restrictions (i.e., $\operatorname{Typ}(\vec{c})$ occurs in $T$ ).

Let P be any fully instantiated predicate symbol occurring in $B(\vec{c})$ . Let $i (1 \leq i \leq t)$ be chosen so that $\vec{c}$ is directly covered by $B_{i}$ . Then in $B_{i}$ there is at least one partially or fully instantiated predicate letter R which, upon utilizing the substitution which takes $B_{i}$ to $B(\vec{c})$ , becomes identical in form to P. Assign to P the truth value which is assigned to R by the valuation which makes (2.2.1) and D true.

By (2.2.2), this truth value for $P$ is independent of $\vec{c}$ , of the predicate letter $R$ chosen in $B_i$ , and of $i, 1 \leq i \leq t$ . Thus all predicate letters of $B(\vec{c})$ receive truth values, in a manner that makes $B(\vec{c})$ true. This valuation also makes $D$ true. As $\vec{c} \in \vec{C}$ was arbitrary among $\vec{c}$ meeting all type restrictions, this truth valuation make (2.1.5) true. Thus (2.1.5) is satisfiable. Q.E.D.

Lemma 2.2.1 allows a determination that $(\forall \vec{y})(\text{Typ}(\vec{y}) \supset B(\vec{y}))$ and $D$ are not simultaneously satisfiable, while Lemma 2.2.2 decides certain cases when both are satisfiable together.

When neither case holds, i.e., when a given variant independent satisfying valuation for $(2.2.1)$ is at hand, but it is blocked, further computation is needed. We next describe that computation, which proceeds from any two R and S which satisfy $(2.2.2)$ .

In the ‘blocked’ case, further substitution of either $B_{i}$ or $B_{j}$ , or both, is performed, and there is wide leeway as to how this is to be done. Such further processing is called unblocking.

The process of unblocking can be viewed as a resolution method not requiring clausal form, which is guided by truth valuations to determine where resolution can make progress in testing for satisfiability.

As the satisfying truth valuation is variant independent, R and S are not variants of each other by (2.2.2a). As they become identical (2.2.2b) after substitutions, they are unified [37] by these substitutions, and at least one of R or S can be further instantiated in accordance with this unification. One may then ‘unblock’ by performing such a further instantiation in either R or S (or both, if possible), by going completely or only partially toward a unifier. In addition, several pairs of such letters R and S can be simultaneously unblocked.

When such unblocking is performed by, say, further instantiation in R occurring in $B_{i}$ , one retains $B_{i}$ and one extends the partial ordering on $B_{1},\ldots,B_{t}$ by stating that $B_{i}^{\prime}$ (the result of instantiating in R in $B_{i}$ ) is a refinement of $B_{i}$ . If $B_{i}$ does not occur among $B_{1},\ldots,B_{t}$ it is added as $B_{t+1}$ , but possibly it does occur in that list. In either case, the partial order of refinement is extended, due to the hypothesis (2.2.2b) that $B_{i}$ directly covers $\vec{c}\in\vec{C}$ .

If the current satisfying truth valuation already gives truth values for all letters in $B_{i}$ , it can (if one desires) again be examined for blockage (2.2.2). Otherwise, one seeks to extend it to a truth valuation for $B_{t+1} = B_i'$ . In either case, the process of appealing to Lemmas 2.2.1 and 2.2.2 is repeated, as is the process of testing for blockage, if necessary.

Quite clearly, this approach to removing blockage via, in essence, examining possible unifications, is reminiscent of many other techniques for theorem proving based on resolution [37]. However, it differs in: (1) Being guided by truth valuations, and being aimed directly at removing obstacles to the satisfaction of the formula; (2) Having tests such as Lemmas 2.2.1 and 2.2.2 which allow termination long before all unifications are performed; (3) Not being restricted to clausal form; and (4) Utilizing the $\forall$ satisfiability fragment in an optimal way, as regards complexity (see Theorem 2.2.2 below).

In regard of implementability, we note that the clause (2.2.b) asserts simply that a unification can be performed between R and S, which will be nontrivial (i.e., have a variable set to a value) for a variant independent valuation. Indeed, if unification is possible, values can be found so that a unification can be performed between R and S, which will be nontrivial (i.e., have a variable set to a value) for a variant independent valuation. Indeed, if unification is possible, values can always be found for the variables not set to constants by the unification. The restrictions, in (2.2.a), go beyond the possibility of unification. These additional restrictions serve to limit the computation needed.

Despite these relative advantages, computation is affected by the specific truth valuations found, and even with (1) many obstacles (blockages) can be present, which require many unifications. This is to be expected, since in the worst case one is treating problem which is exponential time even for nondeterministic automata (Theorem 1.2).

Our next two results, which show the finiteness and validity of partial instantiation, are direct consequences of Theorem 2.2.2 below.

Lemma 2.2.3. Any sequence of unblockings is finite.

Theorem 2.2.1. Any sequence of unblockings terminates either with $(\forall \vec{y})(Typ(\vec{y}) \supset B(\vec{y}))$ and $D \wedge T$ proven simultaneously satisfiable by Lemma 2.2.2, or proven not simultaneously satisfiable by Lemma 2.2.1.

Theorem 2.2.2. For a formula $D \wedge B(\vec{y})$ of length

L, the procedure of partial instantiation requires time at most $c2^{(3L)^{L}}$ for some constant c, until either Lemma 2.2.1 or Lemma 2.2.2 applies to determine if $(\forall\vec{y})(Typ(\vec{y})\supset B(\vec{y}))$ and $D\wedge T$ are simultaneously satisfiable.

Proof. We define the state of a given formula $B_{i}$ in (2.2.1) as the set of $\vec{c}$ it directly covers, and we define the state of the list in (2.2.1) to be the Cartesian production of the states of its $B_{i}$ .

First we need to bound above the number of possible states of $B_{i}$ . If $B = B(y_{1}, y_{2}, \ldots, y_{n})$ has n variables $y_{i}$ and there are m domain constants $c_{j}$ , there can be at most $m^{n}$ vectors $\vec{c} \in \vec{C}$ directly covered by $B_{i}$ ; hence $B_{i}$ has at most $2^{m^{n}}$ states.

To bound above the number of possible states of the list, we first bound t, the number of elements in the list. There are at most $(m+n)^{n}$ ways of substituting variables and constants into $\vec{y}$ , hence $t \leq (m+n)^{n}$ . Thus the number of states in a list is bounded by $(m+n)^{n}2^{m^{n}}$ .

When neither Lemma 2.2.1 nor Lemma 2.2.2 applies, an unblocking is performed. This changes the list state in a nonreversible way, since at least one $B_{i}$ no longer directly covers at least one $\vec{c} \in \vec{C}$ and will not directly cover this $\vec{c}$ again.

In order to obtain a variant independent satisfying truth valuation in those cases when both Lemma 2.2.1 and 2.2.2 do not apply, in the worst case all truth valuations would need to be examined. If $B(\vec{y})$ has $w$ letters, the number of propositional letters in the entire list cannot exceed $w(m + n)^n$ , and hence the number of truth valuations cannot exceed $2^{w(m + n)^n}$ each of which takes at most time $kw(m + n)^n$ to evaluate.

In looking for blockage, no more than $w(m+n)^{2n}L^{2}$ pairs of letters R and S in D and the $B_{i}$ of the list need to be examined, and the test for nontrivial unifiability requires linear time, i.e., $k^{\prime}L/w$ for some constant $k^{\prime}$ . If unifiability is obtained, the time to test for the directness of the covering is bounded by $k''(m+n)^{n}$ , since the number of refinements of a $B_{i}$ is at most $(m+n)^{n}$ .

If we multiply all these factors together, and note that $w + m + 2n \leq L$ and L > 4 (counting the space taken for left and right parentheses, logical connectives, etc.), we obtain

$2^{w(m + n)^n}$ . $kw(m + n)^n$ (to generate and evaluate truth valuations)

$$
\begin{array}{l l} \times & w (m + n) ^ {2 n} L ^ {2} (k ^ {\prime} L / w) (k ^ {\prime \prime} (m + n) ^ {n}) \\ & \text { determine   blockage) } \end{array}\tag{to}
$$

![](/api/attachments/4D9Z36RU/fulltext/images/c289383c2fd130bedfdca1279126463c7903648536c8fa3b77be20557ecbcbe0.jpg)  
Fig. 1.

$\times (m + n)^n 2^{m^n}$ (maximum on iterations of the process)

$= kk^{\prime}k^{\prime \prime}L^{3}(m + n)^{5n}w2^{w(m + n)^{n}}2^{m^{n}}$

$\leq cL^{5L + 4}2^{\dot{L}.L^L}\leq c2^{(3L)^L}$

with $c = kk'k''$ . Q.E.D.

A flowchart of the algorithm framework is given in fig. 1.

## 2.3. Extensions of Partial Instantiation

Clearly, the same techniques for partial instantiation, as in section 2.2, is fully applicable for partial instantiation in the form $\bigvee_{\vec{g} \in \vec{G}} B(\vec{d}, \vec{g})$ of Theorem 1.1, so that the validity of $(\forall \vec{x})(\exists \vec{y})B(\vec{x}, \vec{y})$ can be determined by this technique. While the (non recursive) validity of $(\exists\vec{x})(\forall\vec{y})B(\vec{x},\vec{y})$ cannot be mechanically determined, the partial instantiation technique is applicable in the context of Theorem 1.1 to $A_{1}\vee A_{2}\vee\ldots\vee A_{n}$ for each n, with an appropriate type structure.

Of course, in both the $(\forall\vec{x})(\exists\vec{y})B(\vec{x},\vec{y})$ and $(\exists\vec{x})(\forall\vec{y})B(\vec{x},\vec{y})$ instances, the introduction of new constant symbols leads to many more possible partial instantiations, and so is likely to lengthen the computation process very substantially. Nevertheless, the partial instantiation technique, used in this manner, is a general theorem-proving technique, since the entire predicate logic, with or without function symbols, is reducible to its $(\exists\vec{x})(\forall\vec{y})B(\vec{x},\vec{y})$ fragment (see section 1).

If one wishes to allow the explicit occurrence of function symbols, this can be done in the context of Theorem 1.1(d), by allowing such explicit occurrences in place of the implicit occurrences of $g(\vec{d})$ .

## 2.4. Utilization of Tree Search Techniques for Truth Valuations In Partial Instantiation

To this point, we have not described an implementation framework for deciding that (2.2.1) is or is not satisfiable with D. Toward this end, we have in mind certain techniques from mathematical programming or, alternatively from the Davis–Putnam algorithm [15] augmented by an incumbent-finding feature. These algorithms are discussed in detail in [5]. However, many other tree-search algorithms, for the satisfiability problem of propositional logic, can also be used in regard to (2.2.1).

In forthcoming reports, we will be describing enhancements of logic processing capabilities derived from discrete programming. These include integral polyhedra associated with Horn clause knowledge bases, as well as tightenings of the linear relation for more general logic constraints, via new representations of logic in linear constraints. The issue of problem representation emerges as important, as does the widely appreciated issue of search structuring.

To fix ideas, we shall suppose that the integer programming algorithm discussed in [5] is used. It requires a conjunctive normal form (c.n.f), and one easily verifies that the linear-time reduction to c.n.f. in [5] also works for predicate logic.

The algorithm is given the task of making (2.2.1) and D true via a variant independent valuation. Thus if it reports the problem to be unsatisfiable, Lemma 2.2.1 applies. If it finds a satisfying truth valuation for this problem, and the valuation is unblocked, Lemma 2.2.2 holds.

Note that the incumbent-finding feature of the branch-and-bound algorithm of [5] is essential to quickly locating, where possible, a satisfying valuation. In branch-and-bound, it is the linear programming subroutine which, from time to time, provides such truth valuations, to curtail a more extensive tree search.

We next describe the important issues which arise when an unblocking is performed for a satisfying truth valuation which is blocked.

Although the truth valuation is found at some specific node of the tree, the unblocking operation affects the entire tree. It introduces new disjuncts $B_{i}^{\prime}$ and/or $B_{j}^{\prime}$ which now must also be satisfied (adding constraints), and it may introduce new propositional letters (adding variables), due to computation at any node of the tree. However, rather than ‘update’ the entire tree at once, we suggest that a node be updated only when it is later considered for further processing, if ever (see below).

In view of the fact that constraints have been added, any node of the tree which was previously fathomed due to inconsistency (from an infeasible linear program, in this example) will remain fathomed by inconsistency.

The tree search can then continue from the tree with nodes and arcs as modified above. When, in the course of the search, one returns to an unfathomed node previously set aside, its subroutine (here a linear program) is to be a re-run with the new node specifications. In the event that the node is now fathomed (by, e.g., inconsistency of the linear program), one proceeds up the tree to its 'parent' node to repeat the re-run process, and one does this iteratively until fathoming fails. When the node is not fathomed upon being re-run, one proceeds as in the usual discrete programming algorithms to, e.g., look for an incumbent or to branch.

In deriving an unblocking for a blocked truth valuation found at a given node, typically one wishes to have maximal effect at that node. In most algorithms, one will continue to process that node before seeking other nodes to process.

It seems likely that, among the instantiations and substitutions available, one which introduces a smaller number of new propositional letters is more desirable than one which introduces more new letters, if both would directly cover about the same cardinality of $\vec{c} \in \vec{C}$ . The smaller number of new propositional letters increase the likelihood that the previous falsifying truth valuation cannot be re-used simply by forming an extension to the new letters (as the problem is more tightly constrained). Good heuristics need to be developed, for achieving a reasonable trade-off between new letters introduced and the extent of direct coverage.

A particular instance of the procedure described in this subsection occurs when the problem is efficiently transformable to a conjunction of Horn clauses [34], as, e.g., via repeated use of the de Morgan laws to derive negation inwards. The satisfiability problem for such conjunctions of Horn clauses is solvable by the linear programming relaxation, or equivalent by clausal chaining, as shown in [5]. Thus, branching never occurs and there is only one problem node at all times.

## 2.5. Some Examples

We now give examples to illustrate the techniques discussed in the previous subsections. In the first three examples, the search tree of subsection 2.4 has one node throughout computation, so that all effort is focused on obtaining variant independent satisfying valuations, where possible, and on the unblocking of blocked valuations. We also illustrate some of the preprocessing of predicate logic formulas, in order to obtain a purely existential Prenex Normal Form [39], [52].

Example 2.5.1. Clearly $(\exists y_1)P(a_1, y_1) \supset (\exists y_2)(\exists y_3)P(y_2, y_3)$ is a valid formula of predicate logic (here, ' $a_1$ ' is a constant). Hence, its negation, which is logically equivalent to $(\exists y_1)P(a_1, y_1) \wedge (\forall y_2)(\forall y_3) \neg P(y_2, y_3)$ is not satisfiable.

By Prenex Laws, its negation is logically equivalent to $(\exists y_1)(\forall y_2)(\forall y_3)(P(a_1, y_1) \land \neg P(y_2, y_3)$ . By Corollary 1.4(b) and (d), this latter formula is satisfiable exactly if $(\forall y_2)(\forall y_3)(P(a_1, a_2) \land \neg P(y_2, y_3))$ is satisfiable, where $a_2$ is a new constant (we use $d = (a_2)$ ). We thus can apply Corollary 2.1.1 and (2.1.5) with $D$ and $\operatorname{Typ}(\vec{y})$ vacuous, as well as the development for partial instantiation in (2.2.1).

We put $B(y_{2}, y_{3}) = P(a_{1}, a_{2}) \wedge \neg P(y_{2}, y_{3})$ and we begin with (2.2.1) with $t = 1$ and $B_{1} = B(y_{2}, y_{3})$ , $B_{1}$ covers all $(y_{2}, y_{3}) = (a_{1}, a_{1}), (a_{1}, a_{2}), (a_{2}, a_{1})$ and $(a_{2}, a_{2})$ . A satisfying truth valuation $V$ is immediately obtained by $V(P(a_{1}, a_{2})) = T$ , $V(P(x_{2}, x_{3})) = F$ . This valuation is blocked because (in (2.2.2a)) $R = P(a_{1}, a_{2})$ and $S = P(x_{2}, x_{3})$ have opposite truth values, and (in (2.2.2b)) with $\vec{c}_{1} = \vec{c}_{2} = (a_{1}, a_{2})$ both $R$ and $S$ become identical in form. We chose to unblock by further instantiation of $(a_{1}, a_{2})$ for $(y_{2}, y_{3})$ .

We next have $t = 2$ , $B_{1}$ as before (directly covering $(a_{1}, a_{1})$ , $(a_{2}, a_{1})$ and $(a_{2}, a_{2})$ ), and $B_{2} = (P(a_{1}, a_{2}) \wedge \neg P(a_{1}, a_{2}))$ (directly covering $(a_{1}, a_{2})$ ). Now there is no truth valuation which satisfies (2.2.2), since $B_2$ alone is unsatisfiable. By Lemma 2.2.1, we have shown that $(\forall y_2)(\forall y_3)B(y_2, y_3)$ is not satisfiable.

In this example, it is instructive to note how the instantiation used to show blockage can also be used to progress toward a demonstration of unsatisfiability.

Example 2.5.2. $(\exists x_{1})P(a_{1},x_{1})\supset (\forall x_{2})(\forall x_{3})P(x_{2},$ $x_{3})$ is not a valid formula, but it is satisfiable. By Prenex rules, it is logically equivalent to $(\forall x_{1})$ $(\forall x_{2})(\forall x_{3})(P(a_{1},x_{1})\supset P(x_{2},x_{3}))$

We begin our analysis with $t = 1$ in (2.2.1), $B_{1} = B(x_{1}, x_{2}, x_{3}) = (P(a_{1}, x_{1}) \supset P(x_{2}, x_{3}))$ , $C = \{a_{1}\}$ . $B_{1}$ covers (and directly covers) $(x_{1}, x_{2}, x_{3}) = (a_{1}, a_{1}, a_{1})$ .

A valuation $V$ which makes $B_{1}$ true is $V(P(a_{1}, x_{1})) = V(P(x_{2}, x_{3})) = T$ . This valuation is variant independent and it is unblocked. Hence, we can conclude that $(\exists x_{1})P(a_{1}, x_{1}) \supset (\forall x_{2})(\forall x_{3})P(x_{2}, x_{3})$ is satisfiable, by Lemma 2.2.2.

Another possible variant independent satisfying valuation is $V(P(a_{1}, x_{1})) = F$ , $V(P(x_{2}, x_{3})) = T$ . This valuation is blocked, since $P(a_{1}, x_{1})$ and $P(x_{2}, x_{3})$ are oppositely valued, but become identical for $(x_{1}, x_{2}, x_{3}) = (a_{1}, a_{1}, a_{1})$ . We can unblock using the refinement $B_{2} = (P(a_{1}, x_{1}) \supset P(a_{1}, x_{1}))$ of $B_{1}$ , and setting t = 2. Now $B_{2}$ directly covers $(x_{1}, x_{2}, x_{3}) = (a_{1}, a_{1}, a_{1})$ and $B_{1}$ does not directly cover any vector.

The given valuation V is defined on all letters of $B_{2}$ and satisfies $B_{2}$ . Now it is unblocked, since $B_{1}$ is not a direct cover.

In this example, note that the second truth valuation implicitly constructed a model in which $(\exists x_{1})P(a_{1}, x_{1}) \supset (\forall x_{2})(\forall x_{3})P(x_{2}, x_{3})$ is satisfied. This model has the single element $a_{1}$ , and $P(a_{1}, a_{1})$ is false in it.

Actually, both valuations can be viewed as constructing a satisfying model. The proof of Lemma 2.2.2 is constructive and it describes how to obtain such models from a satisfying valuation.

Example 2.5.3. We now give an example of use of Corollary 1.4(d) for $\vec{\forall}\exists$ forms.

We will use Corollary 1.4(c) to verify that $(\forall x)(\exists y)(P(x)\land\neg P(y))$ is not satisfiable. Here we have $B(x,y)=P(x)\land\neg P(y)$ , and if the given formula is satisfiable, then there is a satisfying valuation for $B(d,g(d))$ simultaneously for all $d\in D_{\infty}$ .

We have $C = \{a_1\}$ (since $B(x, y)$ has no constant symbol, one is adjoined) and we can set $g(a_1) = a_2$ . We have $D_1 = \{a_1\}$ , $D_2 = \{a_1, a_2\}$ , so $a_2$ is the unique element of $D_2 \setminus D_1$ . We can set $g(a_2) = a_3$ , so that $D_3 = \{a_1, a_2, a_3\}$ , etc. The valuation sought must make true all the formula on this infinite list: $P(a_1) \wedge \neg P(a_2)$ , $P(a_2) \wedge \neg P(a_3)$ , etc. Clearly, no satisfying valuation can exist, as $P(a_2)$ cannot be both true and false.

Example 2.5.4. In this example, we will highlight some issues which arise when search methods are used to assist in the attempt to find a satisfying, unblocked truth valuation.

We use the technique of partial instantiation to determine the satisfiability of $(\forall x_{1})(\forall x_{2})B(x_{1},x_{2})$ , where $B(x_{1},x_{2})$ is $(P(x_{1})\lor Q(x_{1},a_{2}))\land(\neg P(a_{1})\lor Q(a_{1},x_{2}))\land(P(x_{1})\lor\neg Q(x_{1},x_{2}))\land(\neg P(x_{1})\land\neg Q(x_{1},x_{2}))$ .

With t=1 and $B_{1}=B$ , there are many satisfying valuations. If one simply processes the atomic predicates from left to right, setting them 'true' until one is forced (by satisfiability) to a 'false' setting, one obtains the variant independent satisfying valuation $V[P(x_{1})]=V[Q(x_{1},a_{2})]=V[P(a_{1})]=V[Q(a_{1},x_{2})]=T$ , $V[Q(x_{1},x_{2})]=F$ . There is blockage due to $(x_{1},x_{2})=(a_{1},a_{2})$ , $V[Q(x_{1},a_{2})]=T$ , $V[Q(x_{1},x_{2})]=F$ . This leads to unblocking via t=2 with $B_{2}=(P(a_{1})\vee Q(a_{1},a_{2}))\wedge(\neg P(a_{1})\vee Q(a_{1},a_{2}))\wedge(P(a_{1})\vee\neg Q(a_{1},a_{2}))\wedge(\neg P(a_{1})\vee\neg Q(a_{2},a_{2}))$ , which directly covers $(a_{1},a_{2})$ , while $B_{1}$ directly covers $(a_{1},a_{2})$ , $(a_{2},a_{1})$ and $(a_{2},a_{2})$ .

Now $B_{2}$ alone is unsatisfiable (showing that $(\forall x_{1})(\forall x_{2})B(x_{1}, x_{2})$ is unsatisfiable). However, if a straight backtracking method is used on the given truth valuation, unnecessary computation can occur.

Specifically, since the setting $V[P(a_1)] = T$ causes the inconsistency that $Q(a_1, a_2)$ must be true (second clause of $B_2$ ) and false (fourth clause of $B_2$ ), one will backtrack and release the settings $V[Q(a_1, x_2)] = T$ , $V[Q(x_1, 'x_2)] = F$ , in order to reset $V[P(a_1)] = F$ . This latter setting again causes the inconsistency that $Q(a_1, a_2)$ must be true (first clause of $B_1$ ) and false (third clause of $B_2$ ).

At this point, a straight backtracking method will reset $V[Q(x_{1}, a_{2})] = T$ and again try all four truth settings of $P(a_{1})$ and $Q(a_{1}, a_{2})$ , before backtracking to reset $V[P(x_{1})] = F$ . Clearly, most of this computation is unnecessary, and can be avoided if either search rearrangement backtracking [19] or treeless searches [4] are used.

## 3. Database Uses of the Existential Fragment of Predicate Logic

As shown by Reiter [45], the $\vec{\exists}$ validity fragment of pure predicate logic can be used for query formation and answering in databases. In this section, we elaborate on these aspects of predicate logic from our present perspective.

The database itself is a collection of relations [45], [56] and as such it can be viewed as a conjunction D of fully-instantiated predicate letters P, in which the constants are names for the objects treated in the database.

The logical axioms for the database are a finite number of universally quantified formulas of the pure predicate logic (i.e., without function symbols), where type restrictions are permitted in these axioms. If we summarize these axioms as $(\forall\vec{x})(\mathrm{Typ}_{A}(\vec{x})\supset A(\vec{x}))$ , then the axioms, together with type assertions T and the 'data' D, imply a type restricted existential $(\exists\vec{y})(\mathrm{Typ}_{B}(\vec{y})\land B(\vec{y}))$ , exactly if $\models T\land D\land(\forall\vec{x})(\mathrm{Typ}_{A}(\vec{x})\supset A(\vec{x}))\supset(\exists\vec{y})(\mathrm{Typ}_{B}(\vec{y})\land B(\vec{y}))$ . Using predicate reasoning, the latter holds exactly if $\models(\exists\vec{x})(\exists\vec{y})(T\land D\land(\mathrm{Typ}_{A}(\vec{x})\supset A(\vec{x}))\supset(\mathrm{Typ}_{B}(\vec{y})\land B(\vec{y}))$ .

This latter validity is of a purely existential statement nature, and so by Theorem 1.1(a), here $\models$ can be replaced by $\models^{M}$ . Hence, such assertions $(\exists \vec{y})(\text{Typ}_B(\vec{y}) \land B(\vec{y}))$ are valid exactly if they are valid in al models for $T$ , $D$ and $(\forall \vec{x})(\text{Typ}_A(\vec{x}) \supset A(\vec{x}))$ in which the only individuals are those named as constants in $T$ , $D$ , $\text{Typ}_A$ , $\text{Typ}_B$ , $A$ , or $B$ . In most applications, all such constants already occur in some row of the database relations, i.e., in $D$ .

In this setting, Proposition 2.1.1 applies, and in (2.1.2) a reduction to propositional logic is given in which the type restrictions of T are treated implicitly. Moreover, (2.1.2) is of the form to which the theorem-proving techniques of subsections 2.2 and 2.4 apply. The theorem-proving part of the work can, in principle, be separated from database evaluations. However, such separation can cause more computation than does early use of the data in D.

In [45] equality is a distinguished predicate for which the usual (universal) axioms are written, and for which one adds to the database all assertions c = c for any constant c and $\neg(c = c')$ for distinct constant c, $c'$ . Also, using equality a (universal) 'domain closure' axiom DC is added, which asserts that the only objects which exist are those named by constants of the database.

In this setting, we may use Corollary 2.1.2 of subsection 2.1. Here we let $A_1(x)$ treat equality axioms together with the DC axiom, and we let $A_2(x)$ treat the remaining axioms. We can then verify that all properly-typed instantions of an equality or DC axiom $A_1(\vec{c})$ is already implied by the data $D$ , which here includes all the equality instances $c = c$ and $\neg (c = c')$ . By Proposition 2.1.1 and Corollary 2.1.2, these equality and DC axioms then play no role. In this manner, we recover Theorem 1 of [45].

## References

[1] E. Balas, Disjunctive Programming, in: P.L. Hammer, E.L. Johnson and B.H. Korte, eds., Discrete Optimization II (North Holland, Amsterdam, 1979) 3–52.

[2] Avron Barr and Edward A. Feigenbaum, The Handbook of Artificial Intelligence (Heuris Tech Press and William Kaufman, Stanford and Los Altos, CA, 1981).

[3] Eamon Barrett, Proving Theorems in Continuous Logic by Linear Programming Techniques, (Smart Systems Technology, McLean, VA, 1985).

[4] C.E. Blair and R.G. Jeroslow, Treeless Searches (1976).

[5] C.E. Blair, R.G. Jeroslow and J.K. Lowe, Some Results and Experiments on Programming Techniques for Propositional Logic, Computer and Operations Research 13 (1986) 633–645.

[6] W.W. Bledsoe and D.W. Loveland, eds. Automated Theorem Proving: After 25 Years, Contemporary Mathematics (American Mathematical Society, Rhode Island, 1983).

[7] Robert H. Bonczek, Clyde W. Holsapple, and Andrew B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1982).

[8] Michael C. Chen and Lawrence J. Henschen, On the Use and Internal Structure of Logic-Based Decision Support Systems, to appear in Decision Support Systems.

[9] E.F. Codd, Relational Completeness of Data Base SubLanguages, in: Data Base Systems, R. Rustin, ed. (Prentice-Hall, Englewood Cliffs, NJ, 1972) 65–98.

[10] S.A. Cook, The Complexity of Theorem-Proving Procedures, in: Proc. Third ACM Symposiums on the Theory of Computing (1971) 151–158.

[11] H. Crowder, E.L. Johnson, and M.W. Padberg, Solving Large-Scale Zero-One Linear Programming Problems, Operations Research 31 (1983) 803–834.

[12] H. Crowder and M.W. Padberg, Solving Large-Scale Symmetric Travelling Salesman Problems to Optimality, Management Science 26 (1980) 495–509.

[13] R.J. Dakin, A Tree Search Algorithm for Mixed Integer

Programming Problems, Computer Journal 8 (1965) 250–255.

[14] G.B. Dantzig, Discrete Variable Extremum Problems, Operations Research 5 (1957) 266–277.

[15] M. Davis and H. Putnam, A Computing Procedure for Quantification Theory, Journal of the ACM 7 (1960) 201–215.

[16] G.D. Eppen and F.J. Gould, Quantitative Concepts for Management (Prentice-Hall, Englewood Cliffs, NJ, 1979).

[17] M. Garey and D. Johnson, Computers and Intractability (Freeman, San Francisco, CA, 1979).

[18] G. Gentzen, Investigations into Logical Deduction, in: The Collected Papers of Gerhard Gentzen, M.E. Szabo, ed. (North Holland, London, 1969) 68–131.

[19] F. Glover and L. Tangedahl, Dynamic Strategies for Branch and Bound, Omega 4 (1976) 1–6.

[20] K. Godel, Die Vollstandigkeit der Axiome des logischen Funktionen Kalkuls, Monatschrift für Math. Phys 37 (1930) 349–360.

[21] R.E. Gomory, An Algorithm for Integer solutions to Linear Programs, in: R.L. Graves and P. Wolfe, ed., Recent Advances in Mathematical Programming (McGraw-Hill, New York, 1983).

[22] R.E. Gomory, Some Polyhedra Related to Combinatorial Problems, Linear Algebra and its Applications 2 (1969) 451–558.

[23] C.C. Green, Theorem Proving by Resolution as a Basis for Question Answering Systems, in: Machine Intelligence 4, B. Meltzer and D. Michie (American Elsevier Publishing, New York, 1969) 183–208.

[24] L. Henkin, The Completeness of the First Order Functional Calculus, Journal of Symbolic Logic 14 (1949) 159–166.

[25] L. Henkin, Completeness in the Theory of Types, Journal of Symbolic Logic 15 (1950) 81–91.

[26] T. Ibaraki, Integer Programming Formulation of Combinatorial Optimization Problems, Discrete Mathematics 16 (1976) 39–52.

[27] R.H.F. Jackson and R.P. O'Neil, eds. COAL Special Issue: Mixed Integer Programming in Mathematical Programming Systems, an ORSA and COAL/MPS publication (1981).

[28] R.G. Jeroslow, There Cannot be any Algorithm for Integer Programming with Quadratic Constraints, Operations Research 21 (1973) 221–224.

[29] R.G. Jeroslow, Representability in Mixed-Integer Programming, I; Characterization Results, Discrete Applied Mathematics 17 (1987) 223–243.

[30] R. Jeroslow, Representability in Mixed Integer Programming, II: A Lattice of Relaxations, College of Management, Georgia Institute of Technology (Oct., 1984).

[31] R. Jeroslow and J.K. Lowe, Modelling with Integer Variables, Mathematical Programming Studies 22 (1984) 167–184.

[32] R. Jeroslow and J.K. Lowe, Experimental Results on the New Techniques for Integer Programming Formulations, Journal of the Operational Research Society 36 (1985) 393–403.

[33] Richard M. Karp, Reducibility Among Combinatorial Problems, in: Complexity of Computer Computations, R.G. Miller and J.W. Thatcher, ed. (Plenum Press, New York, 1972) 85–104.

[34] Robert Kowalski, Logic for Problem-Solving (North Holland, Amsterdam, 1979).

[35] A.H. Land and A.G. Doig, An Automatic Method for Solving Discrete Programming Problems, Econometrica 28 (1960) 497–520.

[36] J.D.C. Little, K.G. Murty, D.W. Sweeney and C. Karel, An Algorithm for the Travelling Salesman Problem, Operations Research 11 (1963) 979–987.

[37] Donald W. Loveland, Automated Theorem-Proving: A Logical Basis (North Holland, Amsterdam, 1978).

[38] Harry R. Lewis, Complexity Results for Classes of Quantification Formulas, Journal of Computer And Systems Sciences 21 (1980) 317–353.

[39] E. Mendelson, Introduction to Mathematical Logic (D. van Nostrand Company, New York, 1964).

[40] R.R. Meyer, Integer and Mixed-Integer Programming Models: General Properties, Journal of Optimization Theory and Applications 16 (1975) 191–206.

[41] R.R. Meyer, A Theoretical and Computational Comparison of 'Equivalent' Mixed Integer Formulations, Naval Research Logistics Quarterly 28 (1981) 115–131.

[42] Arthur J. Nevins, A Human Oriented Logic for Automatic Theorem-Proving, Journal of the Association for Computing Machinery 21 (1974) 606–621.

[43] M.W. Padberg, Convering, Packing, and Knapsack Problems, Annals of Discrete Mathematics 4 (1979) 265–287.

[44] Dag Prawitz, Natural Deduction: A Proof-Theoretical Study (Almquist and Wiksell, Stockholm, 1965).

[45] R. Reiter, Deductive Question-Answering on Relational Databases, in: Logic and Data Bases, H. Gallaire and J. Minker, eds. (Plenum Press, New York, 1978) 149–176.

[46] Elaine Rich, Artificial Intelligence (McGraw-Hill, New York, 1983).

[47] J.A. Robinson, A Machine Oriented Logic Based on The Resolution Principle, Journal of the ACM 12 (1965) 23–41.

[48] J.A. Robinson, The Generalized Resolution Principle, Machine Intelligence 3, Dale and Mitchie, eds. (Oliver and Boyd, Edinburgh, 1968) 77–93.

[49] R.T. Rockafellar, Convex Analysis (Princeton University Press, Princeton, NJ, 1970).

[50] Hartley Rogers, Jr., Theory of Recursive Functions and Effective Computability (McGraw-Hill, New York, 1967).

[51] T.J. Van Roy and L.A. Wolsey, Solving Mixed Integer Programs by Automatic Reformulation, CORE Discussion Paper No. 8432 (June, 1984).

[52] Joseph R. Shoenfield, Mathematical Logic (Addison-Wesley, London, 1967).

[53] Herbert A. Simon, The Structure of Ill-Structured Problems, Artificial Intelligence 4 (1973) 181–201.

[54] J. Stoer and C. Witzgall, Convexity and Optimization in Finite Dimensions I (Springer-Verlag, 1970).

[55] A. Tarski, A. Mostowski and R. Robinson, Undecidable Theories (Amsterdam, 1953).

[56] Jeffrey D. Ullman, Principles of Database Systems, 2nd ed. (Computer Science Press, Rockville, MA, 1982).

[57] H.P. Williams, Experiments in the Formulation of Integer Programming Problems, Mathematical Programming Study 2 (1974) 180–197.

[58] H.P. Williams, Model Building in Mathematical Programming, 2nd ed. (Wiley, New York, 1985).

[59] Patrick Henry Winston, Artificial Intelligence, 2nd ed. (Addison-Wesley, London, 1984).
