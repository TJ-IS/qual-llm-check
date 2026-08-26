---
otero_id: 17152
otero_key: "QFBWX2B2"
title: "Unification theory"
authors: "Jörg H. Siekmann"
year: "1990"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(90)90027-o"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Unification Theory

Jörg H. SIEKMANN
Universität Kaiserslautern, D-6750 Kaiserslautern, West Germany

This article surveys what is presently known in Unification Theory and records its early history.

## 1. Introduction

Überhaupt hat der Fortschritt das an sich, daß er viel größer ausschaut, als er wirklich ist.

J.N. Nestroy, 1859

Unification theory is concerned with problems of the following kind: Let f and g be function symbols, a and b constants and let x and y be variables and consider two first order terms built from these symbols, for example:

$$
\begin{array}{l} s = f (x g (a b), \\ t = f (g (y b) x), \end{array}
$$

The problem is whether or not there exist terms which can be substituted for the variables x and y such that the two terms thus obtained from s and t become equal: in the example $g(ab)$ and a are two such terms. We shall write

$$
\sigma = \left\{x \mapsto g (a b), y \mapsto a \right\}
$$

for such a unifying substitution: $\sigma$ is a unifier of s and t since $\sigma s = \sigma t = f(g(ab)g(ab))$ . In addition to the above decision problem there is also the problem of finding a unification algorithm which enumerates the unifiers for a given pair s and t.

Consider a variation of the above problem, which arises when we assume that f is commutative:

$$
(\mathrm{C}) f (x y) = f (y x).
$$

Now $\sigma$ is still a unifying substitution and moreover $\delta=(y\mapsto a)$ is also a unifier for s and t since $\delta s=f(xg(ab))=_{C}f(g(ab)x)=\delta t$ . But $\delta$ is more general than $\sigma$ since $\sigma$ is an instance of $\delta$ obtained as the composition $\lambda\circ\delta$ with $\lambda=(x\mapsto g(ab))$ ; hence a unification algorithm only needs to compute $\delta$ .

In some cases there is a single and essentially unique least upper bound on the generality lattice of unifiers, called the most general unifier.

Under commutativity however, there are pairs of terms which have more than one most general unifier, but they always have at most finitely many. This is in contrast for example to the above situation of free terms, where every pair has at most one general unifying substitution.

Jörg H. Siekmann studied mathematics and physics at the University of Göttingen, West Germany and received a M.Sc in Computer Science from Essex University in Artificial Intelligence. From 1976 to 1983 research assistant at Karlsruhe University, West Germany, where he built his research group on deduction systems. Since 1983 professor for artificial intelligence at Kaiserslautern University, Department for Computer Science. With many research publications and books in artificial intelligence and automated reasoning his main research interest is deduction systems and unification

The problem becomes entirely different when we assume that the function denoted by f is associative:

$$
(\mathrm{A}) f (x f (y z)) = f (f (x y) z).
$$

In that case $\sigma$ is still a unifying substitution, but $\tau = \{x \mapsto f(g(ab)g(ab)), y \mapsto a\}$ is also a unifier: $\tau s = f(f(g(ab)g(ab))g(ab)) = _A f(g(ab)f(g(ab)g(ab))) = \tau t$ . But $\tau = \{x \mapsto f(g(ab)f(g(ab)g(ab))), y \mapsto a\}$ is again a unifying substitution and by iteration of this process it is not difficult to see that there are infinitely many unifiers, all of which are most general.

Finally, if we assume that both axioms (A) and (C) hold for $f$ then the situation changes yet again and for any pair of terms there are at most finitely many most general unifiers under (AC).

The above examples as well as the many practical applications of unification theory quoted in the following paragraph share a common problem, which in its most abstract form is as follows: Given a formal language L with variables and two words s and t in that language. For a given relation $\approx$ in $L \times L$ find a substitution $\sigma$ such that $\sigma s \approx \sigma t$ (provided $\sigma s$ and $\sigma t$ are welldefined).

If for example the relation can be axiomatized by some equational theory T and L is the language of first order terms, unification of s and t under T amounts to solving the equation s = t in the variety defined by T. If T is an axiomatization of the natural numbers and s and t are as before, the unification of s and t amounts to solving Diophantine equations.

The mathematical investigation of equation solving however is a subject as old as mathematics itself and, right from the beginning, very much at the heart of it: It dates back to Babylonian mathematics (about 2000 B.C.) and has dominated much of mathematical research ever since.

Unification theory carries this activity on in a more abstract setting: just as universal algebra abstracts from certain properties that pertain to specific algebras and investigates issues that are common to all of them, unification theory addresses problems, which are typical for equation solving as such.

Just as traditional equation solving drew much of its impetus from its numerous applications (for example the - for those times - complicated division of legacies in Babylonian times and the application to physics in more modern times), unification theory derives its impetus from its numerous applications in Computer Science, Artificial Intelligence and in particular in the field of Computational Logic.

Central to unification theory are the notion of a set of most general unifiers $\mu U\Sigma$ (traditionally: the set of base vectors spanning the solution space) and the hierarchy of equational theories based on $\mu U\Sigma$ . Both are defined in the second paragraph, were we denote a unification problem under a theory T by

$$
\langle s = t \rangle_ {T}.
$$

In many practical applications unification is too general, but it is of interest to know for two given terms s and t if there exists a matcher (a one-way-unifier) $\mu$ such that $\mu(s)$ and t are equal under T. We denote a matching problem under a theory T by

$$
\left\langle s \geq t \right\rangle_ {T}.
$$

In other words, in a matching problem we are allowed to substitute into one term only (into s using the above convention) and we say s matches t with matcher $\mu$ .

## 1.1. Applications

There is a wide variety of areas in Computer Science and Artificial Intelligence where unification problems arise.

## Databases

A deductive database [GM78] does not contain every piece of information explicitly. Instead it contains only certain facts from which other information can be deduced by some inference rule. Such inference rules (deduction rules) heavily rely on unification algorithms.

Also the user of a relational database [Da76] may logically AND the properties he wants to retrieve or else he may be interested in the NATURAL JOIN [Co70] of two stores relations. In neither case, would he appreciate if he constantly had to take into account that AND is an associative and commutative operation or that NATURAL JOIN obeys an associative axiom, which may distribute over some other operation [SH85].

## Information Retrieval

A patient office may store all recorded electric circuits [BC66] or all recorded chemical compounds [Su65] as some graph structure, and the problem of checking whether a given circuit or compound already exists is an instance of a test for graph isomorphism [Ul76], [Un64], [Cr68]. More generally, if the nodes of such graphs are labelled with universally quantified variables ranging over subgraphs, these problems are practical instances of a graph matching problem.

## Computer Vision

In the field of computer vision it has become customary to store the internal representation of certain scenes as some net structure [BB82], [Wn75]. The problem to find a particular object – also represented as some net – in a given scene is also an instance of the graph matching problem [Rl69]. Here one of the main problems is to specify as to what constitutes a successful match (since a test for endomorphism is too strict for most applications): matching is carried out with respect to some distance function.

## Natural Language Processing

The understanding of natural language by a computer [Wn72] [Wn83] [Te81] is based on transformation rules to change the syntax of the input sentence into a more appropriate one. Inference rules are used to manipulate the semantics of an input sentence and to disambiguate it. The knowledge about the external world a natural language understanding system must have is represented by certain (syntactic) descriptions and it is paramount to detect if two descriptions describe the same object or fact.

Transformation rules, inference rules and the matching of descriptions are but a few applications of unification theory within this field.

The meaning of a natural language utterance has to be represented in some internal representation language [BL85]. Recently developed representation languages such as PATR [SK84] have but one basic operation for their manipulation, namely unification with respect to certain constraints. Also special functional grammars have been designed for the parsing of natural languages, called unification grammars [SK85] [Ka84] [Ka85].

## Expert Systems

An expert system [BS85] is a computer program whose performance largely depends on its ability to represent and manipulate the knowledge of its field of expertise. Commonly this knowledge is represented in the form of productions such that if the conditions of a production are fulfilled its action part will be executed. Special languages such as OPS5 [Fo81] and others have been developed for the implementation of expert systems. In OPS5 the condition part of a production is matched against the entries of the knowledge base and if the match succeeds, the condition is considered true. The efficiency of the matching process is of crucial importance and special techniques (e.g. the Rete-algorithm [Fo82]) and their hardware realisation have been proposed [RZ85], which are very similar to the strive for efficient implementations of the unification algorithm in logical programming languages (see below).

## Textmanipulation Languages

The fundamental mode of operation for programming languages like SNOBOL [FG64] is to detect the occurrence of a substring within a larger string of characters (which may be a program or some other text) and there are methods known, which require less than linear time [BM77]. If these strings contain the SNOBOL 'don't-care'-variable, the occurrence problem is an instance of the stringunification problem mentioned below.

## Patterndirected Programming Languages

An important contribution to programming language design is the mechanism of pattern-directed invocation of procedures [BF77], [Ht76], [RD72], [BM82]. Procedures are identified by patterns instead of procedure identifiers as in traditional programming languages and these invocation patterns are usually designed to express goals achieved by executing the procedure. Incoming messages are tried to be matched against the invocation patterns of procedures in a procedural data base, and a procedure is activated after having completed a successful match between message and pattern. So, matching is done (1) for looking up an appropriate procedure that helps to accomplish an intended goal, and (2) transmitting information to the involved procedure.

For these applications (often called demons, censors, agents, etc.) it is particularly desirable to have methods for matching objects belonging to high level data structures such as strings, sets, multisets and others.

A little reflection will show that for very rich matching languages, as it has e.g. been proposed in MATCHLESS for PLANNER [Ht72], the matching problem is undeciable. This presents a problem for the designer of such languages: on the one hand, very rich and expressive matching languages are desirable, since they form the basis for the invocation and deduction mechanism. On the other hand, drastic restrictions will be necessary if matching algorithms are to be found. The question is just how severe do these restrictions have to be.

## Knowledge Representation Languages

Based on recently developed framelike techniques to structure and represent knowledge [Mi75] special purpose programming languages such as KRL [BW77] or KLONE [BS85] have been designed for this task. Apart from their respective commitment to the representation and structuring issue they all support but one central operation: “matching of descriptions”. In a sense unification theory relates to these new kind of programming languages – and hence to knowledge based systems – as formal language theory relates to traditional programming languages.

## Logic Programming Languages

The discovery of the close relationship between logical deduction and computation, which makes logic enjoy a role in computer science quite similar to the role of analysis in physics, is certainly one of the outstanding scientific achievements of this late century.

However there is a more specific point to this namely that predicate logic itself can be viewed as a programming language [Ko79] given a suitable machine to execute it: predicate logic relates to a deduction system as for example LISP relates to EVAL. This insight opened up a new technology race for appropriate machines [Wa77] [IM83] [GL84], for which the Japanese coined the name “Fifth Generation Computer” [FG84]. The central computation performed in logic programming is unification: in fact the unification algorithm – being it implemented in software or in silicon – is the “CPU” of these machines. Hence the speed of these machines is not expressed in MIPS (million instructions per second) as for conventional machines, but in KLIPS ( $2^{10}$ logical inferences per second), which is a measure of the number of unifications performed per second.

## Term Rewriting Systems

The manipulation of terms subject to equationally defined theories, traditionally called demodulation [WR67], has always played an important role in deduction systems. However if in addition the directed equation are confluent and finitely terminating [HO80] they can be used to compute a unique normal form. The test for confluence can be carried out by a procedure known as the Knuth-Bendix completion procedure [KB70], which uses a unification algorithm as its central component.

Certain equational axioms are notoriously difficult to handle, but sometimes they can advantageously be built into special purpose unification algorithms [PS81].

Term Rewriting Systems are of considerable interest for computer science [Bu85] and have found their place in most computer science curricula today. Not the least important among the many applications these systems have is their being a basis for a new kind of programming languages that elegantly combine functional programming with logical programming style [DL86].

## Computer Algebra

In computer algebra [Ng79] matching and unification algorithms also play an important role: for example the integrand in a symbolic integration problem [Mo71] may be matched against certain patterns in order to detect the class of integration problems it belongs to and to trigger the appropriate action for its solution (which in turn may involve several quite complicated matching attempts [Bl71], [Fa71]). Hence most computer algebra systems like REDUCE [Hn71], MACSYMA [Mo74] or MATHLAB [MB68] make extensive use of unification or matching algorithms.

## Algebra

A famous decidability problem, which inspite of many attacks remained open for over twenty five years, has been solved: the monoid problem (also called Löb's Problem in western countries, Markov's Problem in eastern countries and the Stringunification Problem in Automated Deduction [Hj64], [Hj67], [LS75], [Ma54], [SS61], [Pl72]) is the problem to decide whether or not an equation system over a free semigroup possesses a solution. This problem has been shown to be decidable [Ma77]. The monoid problem has important practical applications inter alia for Deduction Systems (stringunification [Si75] and second order monadic unification [Ht76], [Wn76]), for Formal Language Theory (the crossreference problem for van Wijngaarden Grammars [Wi76]) and for pattern directed invocation languages in Artificial Intelligence as mentioned above.

Without surveying classical equation solving as such, one “unification problem” that should be mentioned is Hilbert’s Tenth Problem [Da73], which is known to be undecidable [Ma70].

The problem is whether or not a given polynomial $P[x_{1}x_{2},\ldots,x_{n}]=0$ has an integer solution (a Diophantine solution). Although this problem was posed originally within the framework of traditional equation solving, unification theory has shed a new light upon this problem (see 3.1.1.).

Semigroup Theory [CP61] [Ho76] is the field traditionally posing the most important unification problems, i.e. those involving associativity. Although scientifically more established than unification theory is today, some interesting semigroup problems have been solved using techniques of unification theory and term rewriting systems (see e.g. [SS82], [La80], [La79]), for a survey on Semithue Systems see [Bo85].

## Deduction Systems

All present day theorem providing or deduction system – based on resolution [Ro65] or not – have a unification algorithm for first or higher order terms as their essential component. Also for almost as long as attempts at providing theorems by machines have been made, a critical problem has been well known [GO67], [Sl72], Ne71]: Certain equational axioms, if left without precaution in the data base of the deduction system, will force the system to go astray. In 1967 A. Robinson [Ro67] proposed that substantial progress (“a new plateau”) could be achieved by removing these troublesome axioms from the data base and building them into the deductive machinery.

One central idea is to build these axioms - which often define common data structures - into the unification algorithm. G. Plotkin has shown in a pioneering paper [Pl72] that whenever a deduction system is to be refutation complete, its extended unification procedure must generate a set of unifiers satisfying the three conditions completeness, correctness and minimality, which today are used to axiomatically define $\mu U\Sigma$ , the set of most general unifiers.

It is the field of Automated Deduction [Lo80], where unification problems became historically first of general importance and it is this field that contributed most to unification theory as it is known today.

## 1.2. Early History $^{1}$

The visionary thoughts about the nature of mathematics, symbols and human reasoning that Emil Post recorded in his diary and notes – partially published in [Da65] – contain the first hint as early as the 1920s to the concept of a unification algorithm that computes a most general representative as opposed to all possible instantiations (p. 370 in [Da65]).

A more concrete account of a unification algorithm, although far from our present notation, is given in J. Herbrand's celebrated thesis "Recherches sur la theorie de la demonstration" in 1930[He30], where he introduced three concepts with respect to the validity of formulas. He called them A, B and C. Concept B and C were the basis for the well-known Herbrand Theorem, whereas concept A was by and large consigned to oblivion. In order to calculate if property A hold for a formula, he gave an algorithm which computes it: the first published unification algorithm.

Based on Herbrand's idea of a finite counterexample, i.e. only a finite number of instantiations are necessary in order to show the unsatisfiability of a set of formulas, early theorem proving programs were developed, but it was not until 1960 when D. Prawitz [Pr60] suggested a way out of these “British Museum Techniques” as they were called later on: the computation of a most general representative for the albeit finite but still abundant number of instantiations that are possible otherwise. However as his logic did not contain any function symbols there was little to compute in fact.

In 1963 M. Davis published [Da63] a proof procedure that combined the virtues of Prawitz's procedure and of the Davis-Putnam procedure. The implementation of this new proof procedure on an IBM 7090 at Bell Labs used a unification algorithm to compute the “linked conjuncts” and was the first fully implemented unification algorithm in actual use. It was not until 1965 however when the seminal paper on the resolution principle by A. Robinson was published that the first explicit account of a unification algorithm for first order terms which computes an essentially unique, single representative (i.e. the most general unifier) appeared in print.

This was the most influential paper that firmly established the concept of unification for all automated deduction systems (including the nonresolution based systems) henceforth. The work for this paper was done essentially in 1963 at Argonne National Lab, a time when a different group headed by J.R. Guard at the Air Force Cambridge Lab developed a deduction system based on a Gentzen-style sequent logic that also incorporated a unification algorithm. The work was published in some internal reports [Gu84] and later in [GO69]; although their algorithm was correct and complete, it was however not formally shown so. They also suggested extensions of the algorithm to higher order logic as well as first order extensions to incorporate axioms like commutativity and associativity. The algorithms used for these latter extensions were heuristically motivated (reordering of terms, rebracketing etc.) and were incorrect and incomplete in general.

The basic unification algorithm was discovered again by D. Knuth and published in a paper [KB70] that became a classic in the field of term rewriting systems: in order to turn a given set of equations into a canonical system a completion process is described that heavily depends on a unification algorithm, whose theoretical properties (computation of the most general unifier) were recognised and shown.

In 1967 A. Robinson proposed to build certain troublesome axioms directly into the deductive machinery of an automated theorem paper and in 1972 G. Plotkin showed in a pioneering paper [Pl72] how this can be done without losing completeness. From the point of view of unification theory this paper contained two major contributions: firstly the definition of a set of most general unifiers, which became – in particular through the work of G. Huet [Ht76] – a central notion of the field. And secondly the discovery that there are equational theories (e.g. the associativity axiom) which induce an infinite set of most general unifiers.

This work was taken up in my own thesis $\{Si75\}$ , which described several special purpose unification algorithms for the axioms of associativity, commutativity and idempotence and their combinations.

Unification theory as a field worthy of its own existence - rather than an arbitrary collection of special algorithms - was suggested, centering around the concept of the Unification Hierarchy, which was introduced here along with some preliminary results about this hierarchy.

While his track of developments is viewed under its contributions towards first order unification there was important work on higher order unification around the same time: Based on the above mentioned theorem proving system of Guard et al, W.F. Gould [Go66] investigated the most general common instance of two higher order terms and discovered that there are infinitely ascending chains of most general unifiers (i.e. a minimal set of most general unifiers does not exist for $\omega$ -order-logic). Influenced by A. Robinson [Ro69] and in particular by P. Andrews [An71], whose work was most influential for higher order deduction systems, G. Huet developed a so-called “constrained resolution method” [Ht72] for higher order theorem proving, based on an $\omega$ -order unification algorithm. This work was then further developed in his “thèse d’état” [Ht76], which became of foundational importance for shaping the field of first and higher order unification theory.

## 2. Notions and Notation

Unification Theory rests upon two notational pillars: Universal Algebra (see e.g. [Gr79]) and Computational Logic (see e.g. [Lo78], [HO80] of which we shall now give a brief account.

As a starting point let us take the familiar concept of an algebra $A = (A, F)$ where $A$ is the carrier and $F$ is a family of operators (the signatur of $A$ ) given with their arities. For a given congruence relation $\rho$ the quotient algebra modulo $\rho$ is written as $A_{/\rho} = (A_{/\rho}, F)$ .

Assuming that there is at least one constant (operator of arity $O$ ) in $F$ and a denumerable set of variables $V$ , we define TERM, the set of first order terms, over $F$ and $V$ , as the least set with (i) $V \subseteq TERM$ , and if arity $(f) = 0$ for $f \in F$ then $f \in TERM$ and (ii) if $t_1, \ldots, t_n \in TERM$ and arity $(f) = n$ then $f(t_1 \ldots t_n) \in TERM$ .

Let $\operatorname{Var}(t)$ be the variables occurring in term t. A common trick is to let T denote the algebra with carrier TERM and the operators are the term constructors corresponding to each operator of F. T is called the absolutely free (term) algebra, i.e. it just gives an algebraic structure to TERM. If the carrier is ground it is called the initial algebra [GT77] or Herbrand universe [Lo78].

Given any set $\Sigma$ with elements $\Sigma, \delta, \tau, \ldots$ and a partial order $\leq$ on $\Sigma$ . Then $\mu \Sigma$ , the base of $\Sigma$ or the $\mu$ -set of $\Sigma$ is defined as:

(i) $\mu \Sigma \subseteq \Sigma$ (correctness)

(ii) $\forall \delta \in \Sigma$ there exist $\sigma \in \mu \Sigma$ with $\delta \leq \sigma$ (completeness)

(iii) $\sigma, \tau \in \mu \Sigma: \sigma \leq \tau$ implies $\sigma = \tau$ . (minimality)

We are interested in the existence, uniqueness and cardinality of such sets in the more specific context of unification.

## 2.1. Unification

A substitution $\sigma: T \to T$ is an endomorphism on $T$ , which is identical almost everywhere on $V$ and hence can be represented as a finite set of pairs $\sigma = \{x_1 \to t_1, \ldots, x_n \to t_n\}$ . The restriction $\sigma|_{V}$ of a substitution to a set of variables is defined as $\sigma|_{V}x = \sigma x$ if $x \in V$ and $\sigma|_{V}x = x$ otherwise. $\Sigma$ is the set of substitutions on $T$ and $\epsilon$ the identity. The application of a substitution $\sigma$ to a term $t$ is written written as $\sigma t$ . The composition of substitutions is defined as the usual composition of mappings: $(\sigma \circ \tau)t = \sigma(\tau t)$ for $t \in T$ .

Hence we have the substitution monoid $\Sigma := \Sigma(F, V)$ of a term algebra as the set of finitely representable endomorphisms on the term algebra:

(i) $\epsilon \in \Sigma$ and $\sigma, \tau \in \Sigma \Rightarrow \sigma \tau \in \Sigma$

(identity and composition)

$$
c \in F _ {0}, f (t _ {1}, \dots , t _ {n}) \in T \Rightarrow \sigma c = c, \sigma f (t _ {1}, \dots , t _ {n}) = f (\sigma t _ {1}, \dots , \sigma t _ {n})
$$

(iii) $\sigma \in \Sigma \Rightarrow \operatorname{card}(\{v \in V: \sigma v \neq V\}) < \infty$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Define
 $\text{DOM}\sigma = \{ x \in V: \sigma x \neq x \}$  (domain of  $\sigma$ )
 $\text{COD}\sigma = \{\sigma x: x \in \text{DOM}\sigma\}$  (codomain of  $\sigma$ )
 $\text{VCOD}\sigma = \text{Var}(\text{COD}\sigma)$  (variables of codomain of  $\sigma$ )
If  $VCOD\sigma = \emptyset$  then  $\sigma$  is a ground substitution.
</div>

An equation s = t is a pair of terms. For a set of equations T, the equational theory presented by T (in short: the equational theory T) is defined as the finest congruence $=_{T}$ on T containing all pairs $\sigma s = \sigma t$ for s = t in T and $\sigma$ in $\Sigma$ , i.e. the $\Sigma$ -invariant congruence relation generated by T. Two terms s, t are T-equal if $s =_{T} t$ . We extend T-equality in T to the set of substitutions $\Sigma$ by:

$$
\sigma = _ {T} \tau \text {   iff   } \forall x \in V \sigma x = _ {T} \tau x.
$$

If $T$ -equality of substitutions is restricted to a set of variables $W$ we write

$$
\sigma = _ {T} \tau [ W ] \text {   iff   } \forall x \in W \sigma x = _ {T} \tau x
$$

and say $\sigma$ and $\tau$ are $T$ -equal in $W$ .

A term $s$ is a $T$ -instance of $t$ , $s \leq_{T} t$ , iff there exist $\lambda \in \Sigma$ with $s =_{T} \lambda t$ ; $s$ is $T$ -equivalent to $t$ , $s \equiv_{T} t$ , iff $s \leq_{T} t$ and $s_{T} \geq t$ .

A substitution $\tau$ is more general than $\sigma$ and $W$ (or $\sigma$ is a $T$ -instance of $\tau$ on $W$ ):

$$
\sigma \leq_ {T} \tau [ W ] \text {   iff   } \exists \lambda \in \Sigma \sigma = _ {T} \lambda \tau [ W ].
$$

Two substitutions $\sigma$ , $\tau$ are called T-equivalent on W

$$
\sigma \equiv_ {T} \tau [ W ] \text {   iff   } \sigma \leq_ {T} \tau [ W ] \text {   and   } \tau \leq_ {T} \sigma [ W ].
$$

Given two terms s, t (built up over a well-defined signature) and an equational theory T a unification problem for T is denoted as $\langle s = t \rangle_{T}$ . Note that a unification problem is characterized by the equational theory T and also by the signature out of which s and t are built.

We say $\langle s=t\rangle_{T}$ is T-unifiable iff there exists a substitution $\sigma\in\Sigma$ such that $\sigma s=\tau\sigma t$ and we call $\sigma$ a T-unifier of s and t. For the set of all T-unifiers of s and t we write $U\Sigma_{T}(s,t)$ which is a left ideal in the substitution monoid $\Sigma$ , since $U\Sigma=\tau\Sigma\circ U\Sigma[W]$ . Without loss of generality we can assume the unifiers of s and t to be idempotent, since if not we can always find equivalent ones which are. For a given unification problem $\langle s=t\rangle_{T}$ , it is unnecessary to compute the whole set of unifiers $U\Sigma_{T}(s,t)$ , which is always recursively enumerable for a decidable theory T, but rather a smaller set useful in representing $U\Sigma_{T}$ . Therefore we define $cU\Sigma_{T}(s,t)$ , the complete set of unifiers of s and t on $W=\operatorname{Var}(s,t)$ as:

$$
c U \Sigma_ {T} \subseteq U \Sigma_ {T} \tag {i}
$$

$$
\forall \delta \in U \Sigma_ {T} \exists \sigma \in c U \Sigma_ {T}: \delta \leq {} _ {T} \sigma [ W ] \quad (\text { completeness }) \tag {ii}
$$

The set of most general unifiers $\mu U\Sigma_T(s,t)$ is defined as the $\mu$ -set of $U\Sigma_T(s,t)$ . A set of substitutions $\Sigma \subseteq \Sigma$ is said to be based on $W$ away from $Z \supset W$ iff the following two conditions are satisfied:

$\mathrm{DOM}\sigma = W$ for all $\sigma \in \Sigma$

$$
\operatorname{VCOD} \sigma \cap Z = \emptyset \quad \text {   for   all   } \sigma \in Z.
$$

For substitutions $\sigma$ based on some $W$ we have $\mathrm{DOM}\sigma\cap\mathrm{VCOD}\sigma=\emptyset$ , which is equivalent to the idempotence of $\sigma$ , i.e. $\sigma\cdot\sigma=\sigma$ . This property is often very useful and we usually require $\mu U\Sigma_{T}$ to be based on $W=V(s,t)$ away from $Z\supset W$ [Pl72].

The set $\mu U\Sigma_T$ does not always exist [FH83] [Sch86] [Ba86]; if it does then it is not unique. However it is unique up to the equivalence $\equiv_T$ (see [Ht76] [FH83]) and for that reason it is sufficient to generate just one $\mu U\Sigma_T$ as a representative of the equivalence class $[\mu U\Sigma_T]_{\equiv_T}$ .

Based on the cardinality of $\mu U\Sigma$ we can classify unification problems and equational theories according to the following hierarchy, which turned out to be the backbone of unification theory. A given unification problem $\langle s=t\rangle_{T}$ is of type

(i) unitary if $\mu U\Sigma (s,t)$ exists and has at most one element

(ii) finitary if $\mu U\Sigma (s,t)$ exists and is finite

(iii) infinitary if $\mu U\Sigma (s,t)$ exists and is infinite

(iv) nullary (or of type zero) if $\mu U\Sigma (s,t)$ does not exist.

Similarly we say an equational theory T is unitary (finitary) if for all $s, t \in T \mu U \Sigma_{T}(s, t)$ is unitary (finitary) and it is infinitary (nullary) if there exists a pair of terms s, t such that $\mu U \Sigma_{T}(s, t)$ is infinitary (nullary).

A Unification algorithm for a given theory T is an algorithm that takes two terms s and t as input and generates some subset of $U\Sigma_{T}(s,t)$ . A complete unification algorithm generates $cU\Sigma_{T}(s,t)$ and a minimal unification algorithm generates the base $\mu U\Sigma_{T}(s,t)$ . For many practical applications the notion of a minimal algorithm is not strong enough, since it does not imply that the algorithm terminates even for a finite $\mu U\Sigma$ . On the other hand for a finitary theory the minimality requirement is often too rigid, since an algorithm which generates a (comparatively small) superset of $\mu U\Sigma$ may be far more efficient than a minimal one and hence preferable.

For that reason we say a unification algorithm is type conformal if it generates a set $\Psi$ such that:

(i) $\mu U\Sigma \subseteq \Psi \subseteq \mathrm{U}\Sigma$

(ii) If $T$ is finitary then $\Psi$ is finite and the algorithm terminates

(iii) If $T$ is infinitary then $\Psi \equiv {}_T\mu U\Sigma$

The three major problems of unification theory can now be states as:

Problem One: For a given equational theory $T$ , is it decidable whether $s$ and $t$ are unifiable for any $s$ and $t$ ?

Problem Two: Given an equational theory T, what is its type in the unification hierarchy?

Problem Three: For a given non-nullary equational theory T find and (efficient) unification algorithm that enumerates $\mu U \Sigma_{T}$ .

## 2.2. Equational Logic

Although unification theory is not restricted to equationally defined theories most results have been obtained within this frame.

A finite set $T := \{(s, t) : s, t \in T\}$ of term pairs is called an axiomatization of an equational theory, the elements are called axioms. The equational theory is the least $\Sigma$ -invariant congruence relation $=_T$ on $T$ containing the set $T$ :

(i) $= _T$ is an equivalence relation with: if $(s, t) \in T$ then $s = _T t$

(ii) if $s_1 = _T t_1, \ldots, s_n = _T t_n$ , $f \in F_n$ then $f(s_1, \ldots, s_n) = _T f(t_1, \ldots, t_n)$ (congruence)

(iii) if $s = _T t$ , $\sigma \in \Sigma$ then $\sigma s = _T \sigma t$

We are only interested in consistent theories, i.e. theories, which do not collapse into a single equivalence class. A theory is consistent if for all $v, w \in V$ : $v = _{T}w$ implies v = w. Frequently the axiomatization T itself is called a theory, and we write s = t instead of $(s, t)$ for the axioms.

An equation $s = {}_T t$ is regular, iff $\operatorname{Var}(s) = \operatorname{Var}(t)$ [PL69]. Equations $t = {}_T v$ with $v \in V$ , $t \notin V$ are called collapse equations and equations $f(v_1, \ldots, v_i, \ldots, v_n) = {}_T v_i$ (for some $i$ with $1 \leq i \leq n$ ) with pairwise different $v_1, \ldots, v_n \in V$ are called projection equations; in this case $f \in F_n$ is called a projection symbol.

A collapse equation of the form $f(v) = _{T} v$ is called a monadic collapse equation. A theory is called regular, iff all equations are regular. A theory without collapse equations is called collapse free. Both properties are inherited from the axiomatization to the whole equational theory:

An equational theory is regular, if all axioms are regular.

An equational theory is collapse free, iff no axiom is a collapse axiom.

The above axioms (i) to (iii) are in fact Birkhoff's axioms. Writing $T| - s = t$ instead of the abbreviations $s = {}_T t$ (since starting from $T$ there is a finite sequence of operations taken from (i), (ii) of (iii) that will lead to $s = t$ ) we obtain Birkhoff's theorem [Bi35]:

$$
T \mid - s = t \quad \text { iff } \quad T \mid = s = t
$$

where $T| = s = t$ denotes that $s = t$ is valid in all models of $T$ . For a survey on classical equational logic see e.g. [Ta79], sequences of replacement are used in [Mc76]. Since neither $| = \text{nor} | -$ are particularly convenient for a computational treatment of $=_T$ , two computer oriented techniques for equational axioms called paramodulation [WR73] and demodulation [WR67] are extensively used in the field of automated deduction. Suppose the equational theory is actually presented as $T = \{l_1 = r_1, l_2 = r_2, \ldots, l_n = r_n\}$ . A term $s$ is said to be demodulated to $t$ , $s \to t$ , if there is a subterm $\hat{O}s$ in $s$ and a pair $l_i = r_i$ in $T$ such that $\hat{O}s = \mu l_i$ for some matcher $\mu$ ; term $t$ is obtained from $s$ by replacement of $\hat{O}s$ by $\mu r_i$ .

A term is said to be paramodulated to $t$ , $s \supset \to t$ , if there is a subterm $\hat{O}s$ in $s$ and a pair $l_i = r_i$ in $T$ such that $\sigma \hat{O}s = \sigma l_i$ for a unifier $\sigma$ ; term $t$ is obtained from $\sigma s$ by replacement of $\sigma \hat{O} s$ by $\sigma r_i$ . Note that this is only a special case of paramodulation, in the context of full predicate logic a little extra machinery is required [Lo78].

If for example $T = \{ g(x, 0) = 0 \}$ we have for $s = f(g(a, y), y) \supset \to f(0, 0) = t$ with $\sigma = \{ x \leftarrow a, y \leftarrow 0 \}$ but not $s \rightarrow t$ , since we are not allowed to substitute into s. The strength of the best current theorem proving systems can be largely attributed to an exploitation of these two rules: e.g. the Argonne National Lab System uses demodulation and paramodulation, also the induction prover of R. Boyer and J. Moore heavily depends on demodulation. The idea of demodulation has been taken further in a paper by D. Knuth [KB70], which is now a classic in the field called Term Rewriting Systems. The essential observation is that it is often possible to find an equivalent set of equations, which is directed from left to right $l_i \Rightarrow r_i$ , $1 \leq i \leq m$ , with $\operatorname{Var}(r_i) \subseteq \operatorname{Var}(l_i)$ ; this is then called a term rewriting system (TRS). If there are no infinite sequences $s_1 \to s_2 \to \ldots$ the relation $\to$ (based on the TRS) is said to be finitely terminating or Noetherian. The relation $\to$ is called confluent if for every r, s, t with $r \to s$ and $r \to t$ there exists a term u such that $s \to u$ and $t \to u$ ; a confluent, Noetherian relation (a TRS) is called canonical. Canonical relations are an important basis for a computational treatment of equational logic, since they define a unique normal form $\|t\|$ for every term t given by: $t \to \|t\|$ and there does not exist a term s with $\|t\| \to s$ . $\|t\|$ exists because of the finite termination property and it is unique because of confluence; hence $s = _T$ iff $\|s\| = \|t\|$ . Because of the great importance of TRS for computer science there is intensive research now on methods of how to obtain a canonical TRS from a given set of equations (see [HO80] [Bu85] for a survey).

In the paramodulation relation is based on a directed set of equations it is sometimes called narrowing [Hu80] or directed paramodulation and becomes of importance for universal unification algorithms (see 3.2.2.) as well as for the design of recent programming languages that combine functional with logical programming style [DL86].

## 3. Results

The development of unification theory into a field of its own is hallmarked by the emergence of a theory that addresses the three basic problems of unification theory as introduced above in a more general setting: How and under which conditions can unification algorithms be combined? Why is the combination of a finitary and an finitary theory sometimes finitary and sometimes infinitary? Is it possible to give a universal unification algorithm (similar to a universal Turing machine as opposed to a particular Turing machine), which takes as input a pair of terms and an equational theory? What is the exact relationship between matching and unification? It is possible to develop a general theory in order to classify equational theories with respect to the unification hierarchy? For this and other reasons this section is divided into two main paragraphs: special results and results of the general theory.

## 3.1. The Special Theory

“...a general comparative study necessarily presupposes some previous separate study, comparison being impossible without knowledge.”
N. Whitehead, 1898

This paragraph is divided into three parts giving a separate account of first and higher order unification as well as of unification in sorted logics.

## 3.1.1. First Order Unification

Unification of Free Terms. The historical experience with the first deduction systems revealed that “the unification computation occurs at the very heart of most deduction systems. It is the addition and multiplication of deduction work. There is accordingly a very strong incentive to design the last possible ounce of efficiency into a unification program. The incentive is very much the same as that for seeking maximally efficient realizations of the elementary arithmetic operations in numerical computing – and the problem is every bit as interesting.” ([Ro71], p. 64)

A first and influential paper in this direction appeared in 1971 by A. Robinson [Ro71] and a proposed table-driven implementation technique that derived its strength from an ingenious manipulation of a pointer structure, which is – with some improvements – still at the heart of current techniques.

The manipulation of pointers - instead of the objects themselves - was also proposed by R. Boyer and J. Moore and became known as structure sharing.

The final race for the fastest algorithm however started in 1973 with a proposal by L.D. Baxter [Ba73], that was further improved by M. Venturini-Zilli [VZ75] in 1975, by G. Huet [Ht76] in 1976 and by A. Martelli and U. Montanari [MM79] in 1979, who proposed an almost linear algorithm: it is a well-known fact that the original unification algorithm is exponential as a worst case. The first linear unification algorithm was designed in 1976/77 and finally published in a celebrated paper by M. Paterson and W. Wegman [PW78], who used a particular data structure (directed acyclic graphs, dag) to represent the terms. Linearity is achieved by moving an additional pointer structure through these dags.

Although this work appeared to settle the problem once and for all the issue was taken up again, when it became apparent that maintaining the dags and the pointer structure can be expensive and for most practical cases (i.e. short and usually not deeply nested terms) too inefficient.

A most recent improvement was published by D. Kapur, M.S. Krishnamoorthy and P. Narendsan [KK82] in 1982. A first comparison of several algorithms in terms of empirical findings was carried out by G. Winterstein [Wn77]; a more recent comparison by H.J. Bürckert [Bü85] shows again that the issue is far from being finally settled.

Unification in Equational Theories. The following table summarizes the results that have been obtained for unification problems $\langle s = t \rangle_{T}$ with $s, t \in T$ and special equational theories T. The special theories consist of combinations of the following equations:

A (associativity) $f(f(x,y),z) = f(x,f(y,z))$

C (commutativity) $f(x,y) = f(y,x)$

D (distributivity) $\mathrm{D}_{\mathbb{R}}\colon f(x,g(y,z)) = g(f(x,y),f(x,z)$

$$
\mathrm{D} _ {\mathrm{L}} \colon f (g (x, y), z) = g (f (x, z), f (y, z))
$$

H, E (homomorphism, endomorphism) $\phi(x \circ y) = \phi(x) \circ \phi(y)$

I (idempotence) $f(x,x) = x$

T (transitivity) $f(g(x,y),g(y,z)) = f(g(x,y),g(x,z))$

$C_{R,L}$ (right, left $f(f(x,y),z) = f(f(x,z),y)$

$$
f (x, f (y, z)) = f (y, f (x, z))
$$

FPAG: Finitely Presented Abelian Group

QG: Quasi-Groups

AG: Abelian Groups

H10: Hilbert's $10^{\text{th}}$ Problem

FH: $1 * x = x, q(x * y) = q(y)$

MINUS: $-(-x) = x; - (x*y) = (-y)*( - x)$

ABS: Signed binary trees

BR: Boolean Rings

Table 1

<table><tr><td>Theory $T$ </td><td>Type of  $T$ </td><td>Unifiability decidable</td><td> $A_T$ </td><td>References</td></tr><tr><td> $\emptyset$ </td><td>1</td><td>Yes</td><td>Yes</td><td>[He30] [Ro65] [Ro71] [KB70] [Gu64] [Pr60][Ba73] [Ht76] [MM79] [PW78] [KK82]</td></tr><tr><td>A</td><td> $\infty$ </td><td>Yes</td><td>Yes</td><td>[Hj67] [Pl72] [Si75] [LS75] [Ma77] [Si78]</td></tr><tr><td>C</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Si76]</td></tr><tr><td>I</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[RS78] [Hu80]</td></tr><tr><td>A+C</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[St81] [LS76] [Hu79] [Fa83] [Ht78] [HS85] [Bü85]</td></tr><tr><td>A+I</td><td>0</td><td>Yes</td><td>?</td><td>[SS82] [SCH86] [BA86]</td></tr><tr><td>C+I</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[RS78] [JK83]</td></tr><tr><td>A+C+I</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[LS76] [Bü86]</td></tr><tr><td>D</td><td> $\infty$ </td><td>?</td><td>Yes</td><td>[Sz82] [AT85] [Mz86] [SU78]</td></tr><tr><td>D+A</td><td> $\infty$ </td><td>No</td><td>Yes</td><td>[Sz82]</td></tr><tr><td>D+C</td><td> $\infty$ </td><td>?</td><td>Yes</td><td>[Sz82]</td></tr><tr><td>D+A+C</td><td> $\infty$ </td><td>No</td><td>Yes</td><td>[Sz82]</td></tr><tr><td>D+A+I</td><td>?</td><td>Yes</td><td>?</td><td>[Sz82]</td></tr><tr><td>H,E</td><td>1</td><td>Yes</td><td>Yes</td><td>[Vo78]</td></tr><tr><td>H+A</td><td> $\infty$ </td><td>Yes</td><td>Yes</td><td>[Vo78]</td></tr><tr><td>H+A+C</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Vo78]</td></tr><tr><td>E+A+C</td><td> $\infty$ </td><td>?</td><td>?</td><td>[Vo78]</td></tr><tr><td>T</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Ki85]</td></tr><tr><td>T+C</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Ki85]</td></tr><tr><td>T+C+C</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Ki85]</td></tr><tr><td> $C_{R,L}$ </td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Je80]</td></tr><tr><td>QG</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[Hu80]</td></tr><tr><td>AG</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[LA79] [LBB84]</td></tr><tr><td>H10</td><td>?</td><td>No</td><td>?</td><td>[MA70] [DA73]</td></tr><tr><td>FPAG</td><td> $\omega$ </td><td>Yes</td><td>Yes</td><td>[LA80] [KR85]</td></tr><tr><td>HF</td><td>0</td><td>Yes</td><td>?</td><td>[FH83]</td></tr><tr><td>MINUS</td><td> $\infty/\omega$ </td><td>Yes</td><td>Yes</td><td>[Ki85]</td></tr><tr><td>ABS</td><td> $\infty/\omega$ </td><td>Yes</td><td>Yes</td><td>[Ki82]</td></tr><tr><td>BR</td><td>1</td><td>Yes</td><td>Yes</td><td>[MN86]</td></tr></table>

type 1: unary  
$\omega$ : finitary  
∞: infinitary  
0: nullary  
The column under $A_T$ indicates whether or not a type conformal algorithm is known.  
Except for Hilbert's tenth problem, we have not included the classical work on equation solving in "concrete" structures such as rings and fields, which is well known. The relationship of universal unification to these classical results is similar to that of universal algebra to classical algebra.

Let us comment on a few entries in the above table: The Robinson Unification Problem, i.e. unification in the free algebra of terms or unification under the empty theory $\varnothing$ has attracted most attention so far.

Unification under associativity is the famous monoid problem mentioned in paragraph 1.1. G. Plotkin gave the first unification algorithm for this theory [PI72] and used it to demonstrate the existence of infinitary equational theories. Completeness, correctness and minimality proofs are presented in [SI78]. Makanin showed the decidability of this unification problem [Ma77].

Unification under commutativity has a trivial solution, whereas minimality presents a hard problem; a type conformal algorithm is presented in [Si76]. The main interest in this theory however derives from its finitary nature in contrast to the infinitary theory of associativity. A nice characterization of this difference is possible in terms of the universal unification algorithm to be presented below. However a deep theoretical explanation of why two seemingly very similar theories belong to entirely different classes is still an open research problem.

Terms under associativity and commutativity closely resemble the datastructure multisets (sets which may contain multiple occurrences of the same element), which is used in the matching of patterns (pattern directed invocation) in many programming languages of Artificial Intelligence. This pattern matching problem for multisets (often called bags in the AI-literature) was investigated by M. Stickel in [St75], [St76], who observed that this problem can be reduced to the problem of solving homogeneous linear diophantine equations over the positive integers with the additional proviso that only positive linear combinations of the solution set are admissible. His results were finally published in [St81].

Building upon the work of G. Plotkin [Pl72], Livesey and Siekmann [LS76] [LS78] investigated the axioms of associativity (A) and commutativity (C), since they so frequently occur in applications of automated theorem proving, Independently of M. Stickel they also observed the close relationship between the AC-unification problem and the solving of linear diophantine equations. They proposed a very different reduction (among other differences a reduction to inhomogeneous linear diophantine equations) which appears to have some advantages over the combinatorics of the “variable-abstraction” process in the Stickel algorithm.

However an important problem remained open: the extension of the AC-unification algorithm to the whole class of first order terms turned out to be more difficult than anticipated. The suggestions for such an extension in $[St76]$ as well as the naive sketch of an extension proposed in $[LS76]$ were missing a crucial point namely that the subformulas of a term to be AC-unified can become longer, i.e. have more symbols, than the original term. Hence the termination of the extended AC-unification procedure became a major problem, which remained open for many years. It was finally positively solved by F. Fages $[Fa83]$ using an ingenious complexity measure on AC-terms.

G. Huet [Ht78], A. Fortenbacher [Fo83], D. Lankford [La85] and W. Büttner [Bü85] give efficient methods to solve homogeneous linear equations where only positive linear combinations are admissible, a problem originally investigated in [Gl873]. this is an important component of every AC-unification algorithm. A comparison of the algorithms of Huet and Fortenbacher and an extension of these algorithms to the case of inhomogeneous equations can be found in [GH85].

J.M. Hullot [Ht80], F. Fages [Fa84] and Fortenbacher [Fo83] [Fo85] discuss computational improvements of the original Stickel-algorithm. Recently another approach to AC-unification was proposed in [Ki85].

G.E. Peterson and M.E. Stickel [PS81] present a generalisation of the Knuth-Bendix completion algorithm for term rewriting systems [KB70] based inter alia on AC-unification. The practical advantage of a special purpose AC-unification algorithm is particularly well demonstrated for term rewriting systems in [St84].

Apart from interest in a practical and fast algorithm, which computes the set of unifiers there is the main theoretical observation that the set of most general unifiers is always finite for AC-unification problems. This fact was independently discovered in [St75] and [LS76]. However, since the set of most general unifiers (mgu) corresponds to the set of nonnegative solutions of certain linear diophantine equations, the finiteness of the set of mgu's follows immediately from a theorem of Dickson [DI13].

Two recent papers by A. Herold, J. Siekmann [HS86] and W. Büttner [Bü85] improved on the original work of [LS76] [LS78]. In [HS86] an extension of the algorithm to the whole class of first order terms is presented using a modification of the Fages-complexity measure in the proof of termination.

The AC-unification algorithm has become just as important for practical work as the original Robinson Algorithm, since the axioms of associativity and commutativity so often occur in practice.

Apart from its practical relevance, however, AC-unification poses an important theoretical problem: why is it that the combination of an infinitary theory (A) with a finitary theory (C) results in a finitary theory $(A + C)$ , whereas the combination of an infinitary theory (D) with the finitary (C) results in infinitary theory $(D + C)$ ?

Unification under distributivity and associativity provides a point in case that the combination of two infinitary theories is an infinitary theory. Is this always the case? The D + A Unification Problem is also of theoretical interest with respect to Hilbert's Tenth Problem, which is the problem of Diophantine solvability of polynomial equation. An axiomatization of Hilbert's Tenth Problem would involve the axioms A and D plus additional axioms for integers, multiplication, etc. Calling the union of these axioms HTP, the famous undecidability result [Da73] shows the undecidability of the unification problem under HTP. Now the undecidability of the D + A-Unification Problem demonstrates that all Hilbert axioms in HTP can be dropped except for D and A and the problem still remains undecidable. Since A-unification is known to be decidable, the race is open as to whether or not A can be dropped as well and D on its own presents an undecidable unification problem.

More generally: it is an interesting and natural question for an undecidable problem to ask for its “minimal undecidable substructure”. Whatever the result may be, the D + A problem already highlights the advantage of the abstract nature of universal unification theory in contrast to the traditional point of view, with its reliance on intuitively given entities (like integers) and structures (like polynomials).

It is important to realize that the results recorded in the table do not always hold for the whole class of first order terms, which is but a special case of the Combination Problem of Theories:

## From the table we already have

<table><tr><td>A infinitary,</td><td>I</td><td>finitary</td><td>and A + I</td><td>nullary</td></tr><tr><td>D infinitary,</td><td>A</td><td>infinitary</td><td>and D + A</td><td>infinitary</td></tr><tr><td>D infinitary,</td><td>C</td><td>finitary</td><td>and D + C</td><td>infinitary</td></tr><tr><td>A infinitary,</td><td>C</td><td>finitary</td><td>and A + C</td><td>finitary</td></tr><tr><td>C finitary,</td><td>I</td><td>finitary</td><td>and C + I</td><td>finitary</td></tr><tr><td>H unitary,</td><td>A</td><td>infinitary</td><td>and H + A</td><td>infinitary</td></tr><tr><td>H unitary,</td><td>A + C</td><td>finitary</td><td>and H + A + C</td><td>finitary</td></tr><tr><td>DLunitary,</td><td>C</td><td>finitary</td><td>and DL + C</td><td>infinitary</td></tr><tr><td>DLunitary,</td><td>DR</td><td>unitary</td><td>and DL + DR = D</td><td>infinitary</td></tr></table>

Using a more informal notation we can write; $\infty +\infty = \infty ,\infty +\omega = \infty ,\omega +\omega = \omega ,1 + \infty = \infty ,1 + \omega =$ $\omega ,1 + \omega = \infty$ and even $1 + 1 = \infty ,\infty +\omega = 0$ for these results.

Here we assume that for example C and A hold for the same function symbol f and the combination of these axioms is denoted as $C + A$ . But what happens if C and A hold for two different function symbols, C for f and A for g? Even the most trivial extension in this spirit, which is the extension of a known unification result to additional “free” functions (i.e. the empty theory for every function symbol which is not part of the known unification result) as mentioned above is unsolved in general. The results known so far are recorded in section 3.2.1.

Summarizing we notice that unification algorithms for different theories are usually based on entirely different techniques. They provide the experimental laboratory of Universal Unification Theory and it is paramount to obtain a much larger experimental test set than the one recorded above.

Unification in Logic Programming Languages. Terms like $f(x, g(x))$ and $f(y, y)$ are not unifiable in the classical sense: although both terms are “standardized apart” (i.e. have different variables), once the first arguments of f are unified the second arguments share the same variable in y and $g(y)$ and the so-called “occur-in-check” reports failure.

In order to avoid this (expensive) checking two approaches are possible: either to admit infinite terms [Mu83] or else to accept the occasional error as for example in most PROLOG implementations [CM81].

Since unification is the central operation of logic programming languages and the CPU of Fifth Generation Computers more elaborate schemes have been designed for speed up. Most prominent is currently the WARREN-Machine [GL84], which consists of machine instructions into which a logic programming language can be compiled. This set constitutes an abstract machine and each instruction can then either be supported by actual hardware or else by some sequence of microcode instructions of a more or less conventional machine (like e.g. in the SYMBOLICS LISP-Machine).

Unification Chips. Anticipating the upcoming technology race for ultrafast unification there were early attempts to “compile the unification algorithm into silicon” and to design a special unification processor called the SUM [Ro85].

Similarly if the Warren instruction set is directly supported by suitable hardware this can be viewed as a unification machine.

Current experiments use a pipeline of unification processors or else try to marry the Warren machine with a (set of) special unification processor(s) [FG84].

## 3.1.2. Unification in Sorted Logic

This section is excluded for space limitations. Most recent work (with appropriate back references) is reported by Ch. Walther [Wa86] and M. Schmidt-Schauss [Sch86].

## 3.1.3. Higher Order Unification

This section is excluded for space limitations. A recent article with appropriate back references is by P. Andrews [An84].

## 3.1.4. Unification Grammars

This section is again excluded for space limitations. A recent collection of papers with current references is [SK84] [SK85].

## 3.2. The General Theory

“However to generalize, one needs experience…”

G.Grätzer, 1968

## 3.2.1. Combination of Unification Algorithms

Given a unification algorithm for an equational theory $T_{1}$ and another algorithm for a theory $T_{2}$ : how can we obtain an algorithm for the theory $T = T_{1} \cup T_{2}$ ?

There are at least two cases to be distinguished: if the axioms in $T_{1}$ and $T_{2}$ involve the same function symbol there is little hope for a general recipe of how to obtain a unification algorithm for T out of the separate algorithms for $T_{1}$ and $T_{2}$ . For example if $T_{1}$ is the associativity axiom (A) a complete and minimal unification algorithm is known that is infinitary. Suppose now $T_{2}$ is the commutativity axiom (C) for the same function symbol: again a type conformal algorithm is known which is finitary. But the finitary AC-algorithm for the union of A and C is completely different. Even taking the separate algorithm as a heuristic guideline in order to find the algorithm for the union would be utterly misleading in this case (however sometimes it may not): it was the distrust in the obvious combination of the C-algorithm and the A-algorithm that lead to the A + C-algorithm.

This situation is to be expected in general: solving equations in an algebra defined by $T_{1}$ and $T_{2}$ respectively may have nothing to do with solving equations in the algebra defined by $T = T_{1} \cup T_{2}$ .

However if $T_{1}$ and $T_{2}$ involve different function symbols the situation is different and under certain preconditions the separate algorithms for $T_{1}$ and $T_{2}$ can indeed be combined just as decision procedures for different theories can sometimes be combines into a decision procedure for their union [NO80].

There are currently three approaches: Building upon the variable abstraction of M. Stickel and F. Fages, that was successfully used for the AC-unification problem, K. Yelick [Ye85] and E. Tidén [Ti85] independently gave algorithms for a combination of finitary theories. Essentially these algorithms are a generalization of the AC-unification idea by abstracting those subterms to variables that do not belong to the theory of the top function symbol. K. Yelick restricts the problem to regular finitary collapse free theories whereas E. Tidén presents a combination for collapse free theories without the regularity restriction.

A second approach was presented by A. Herold [He85], whose technique is a generalization of the constant abstraction used for the AC-unification algorithm of M. Livesey and J. Siekmann. Again his technique is restricted to finitary collapse free theories.

A third approach is given by C. Kirchner in [Ki85], who tackles the problem by a decomposition of the terms to be unified. Currently his combination only works for a more restrictive class than the regular finitary collapse free theories (however this may be generalized).

## 3.2.2. Universal Unification

As unification algorithms for different theories are usually based on entirely different methods it would be interesting to have a universal unification algorithm for a whole class of theories: a universal unification algorithm (a universal matching algorithm) for a class of theories T is an algorithm which takes as input a pair of terms $(s, t)$ and a theory $T \in T$ and generates a complete set of unifiers (matchers) for $\langle s = t \rangle_{T}$ (for $\langle s \geq t \rangle_{T}$ ). In other words just as a Universal Turing Machine takes as its input the description of a special Turing Machine and its arguments, a universal unification algorithm accepts an (equational) theory T and two terms to be unified under T.

To show the essential idea behind the universal algorithms suppose $\langle s = t \rangle_{T}$ is the unification problem and R is a rewrite system for T. Let h be a “new” binary function symbol then $h(s, t)$ is a term. Using these conventions we have the following consequence of Birkhoff’s theorem as a basis for all universal unification algorithms:

There exists $\sigma \in \Sigma$ with $\sigma s = {}_T\sigma t$ iff there exist terms $p, q$ and $\delta \in \Sigma$ such that $h(s, t) \supset \to {}_R h(p, q)$ with $\delta p = \delta q$ .

A first step towards an application of this result is a proper organization of the paramodulation steps $\supset \rightarrow$ into a tree, with the additional proviso that we never paramodulate into variables.

For a given term $t$ the labeled paramodulation tree $P_{t}$ is defined as:

(i) $t$ (the root) is a node in $P_{t}$

(ii) if $r$ is a node in $P_{t}$ and $r \supset \rightarrow s$ , then $s$ (the successor) is a node in $P_{t}$ .

(iii) the edge $(r, s)$ , where $r \supset \overline{[\pi, i, \theta]} s$ , labeled with the triple $[\pi, i, \theta]$ .

Using the above result we have: if $h(p, q)$ is a node in $P_{h(s,t)}$ such that p, q are Robinson-unifiable with $\sigma$ then $\delta = s \circ \theta$ is a correct T-unifier for s and t, where $\theta$ is the combination of all the paramodulation substitutions obtained along the path from $h(s, t)$ to $h(p, q)$ .

An vice versa for every $T$ -unifier $\tau$ for $s$ and $t$ there exists a node $h(p, q)$ in $P_{h(s,t)}$ such that $p$ and $q$ are Robinson-unifiable with $\sigma$ and $\tau < \sigma \circ \theta$ .

Of course the set of unifiers obtained with this tree is far too large to be of any interest and the work of D. Lankford [La79] and G. Hullot [Hu80], based on [Fa79], is concerned with prunig this tree under the constraint of maintaining completeness. G. Hullot [Hu80] shows the close correspondence between $\rightarrow$ (rewrite) and $\supset\rightarrow$ (paramodulation, narrowing) steps and [JK83] investigate an incremental universal unification algorithm by separating the given theory T into two constituent parts $T=R\cup E$ , where only R must be E-canonical.

Since the set of unifiers $U\Sigma_{T}$ is trivially recursively enumerable for any decidable theory T there is the important requirement that a universal unification algorithm generates the minimal set $\mu U\Sigma_{T}$ or is at least type conformal. Since such a result is unattainable in general, there is a strong incentive to find classes of theories, such that a universal unification algorithm is minimal for every theory T within the class. Such a class should be large enough to contain most theories of practical interest and show that the universal unification algorithm based on $P_{t}$ is correct, minimal and complete for this class. J. Siekmann and P. Szabo propose such a class (called ACFM-class) [SS81]. A Herold [He82] gives an extension of this class, which is the widest currently known.

The Next 700 Unification Algorithms. These theoretical results can be applied in practice for the design of an actual unification algorithm. So far the design of a special purpose algorithm was more of an art than a science, since for a given theory there was no indication whatsoever of how the algorithm might work. In fact the algorithms recorded in the table of 3.1.1 all operate on entirely different principles.

Using the universal unification algorithm as a starting point this task is now much easier by first isolating the crucial parts in the universal algorithm and then designing a practical and efficient solution. A collection of canonical theories [Hu80] is a valuable source for this purpose and has already been used to find the first unification algorithms for Abelian group theory and quasi group theory [La79], [Hu80].

Logic Programming. Universal unification is the basis of an interesting new approach to programming languages that combines the virtues of functional programming [Bacus] with logical programming.

The idea is to have a logical programming language with equality and to use the (directed) equations in just the same way as they are used in the universal unification algorithm. This technique is called narrowing or directed paramodulation and interest is in finding equational classes where this can be done effectively. A collection of papers centered around this approach is contained in [DL86].

## 3.2.3. Matching and Unification

An equational theory that is finitary with respect to unification is of course finitary matching, but not vice versa: for example stringunification is finitary matching but infinitary with respect to unification.

What is then in general the relationship between matching and unification and more specifically: how are the two respective hierarchies related?

The problem is that a matcher is in general not just a special unifier. For example the substitution $m = \{x \mid \rightarrow f(x)\}$ is a matcher for the problem $\langle f(x) \leq x \rangle_{\varnothing}$ but not a unifier for the corresponding unification problem $\langle f(x) = x \rangle_{\varnothing}$ . Matching and semi-unification [HT76] are but special cases of the general notion of a V-restricted unification problem, which is a unification problem $\langle f(x) = x \rangle_{T}$ , where the unifier is allowed to move only a subset of $\operatorname{Var}(s, t)$ .

Some general results are shown in [Bü86], in particular it is shown how the most general restricted unifiers can be computed from the unrestricted most general unifiers (for the special case of collapse free equational theories).

## 3.2.4. Classification of Equational Theories

This section is again omitted for space limitations. Some results are summarized in [SI84].

## 3.2.5. Unification Hierarchy

In the 1970's many unitary, finitary and infinitary equational theories were discovered. It was also well-known that for higher order logics the minimal set of unifiers $\mu U\Sigma$ does not always exist: i.e. for certain problems there are infinitely ascending chains of unifiers $\sigma_{1}\leq\sigma_{2}\leq\sigma_{3}\leq\ldots$ with no upper bound. Hence the natural problem, which was open for several years: are there first order equational theories with the same unpleasant feature or is the class of nullary first order theories empty?

G. Huet and F. Fages showed that unfortunately this is the case: in [FH83] they construct a special equational theory, which even admits a canonical rewriting system, of type zero. Recently it was shown independently by M. Schmidt-Schauss [Sch86] and A. Baader [Ba86] that idempotent semigroups (called bands in semigroup theory) are of type nullary, thus opening up a whole class of “natural” theories (varieties) all of which are of type zero.

Similarly we may ask if the unification hierarchy is the finest possible structure or else is it possible to refine the hierarchy into subclasses? A natural candidate might be the class of finitary theories that could be decomposed into bounded theories. An equational theory $T$ is bounded by $N$ if for every pair of terms $s, t$ the cardinality of $\mu U\Sigma (\langle s = t\rangle_T)$ is less than $N$ . While it is easy to find special unification problems that are bounded by some $N$ (for certain subclasses of terms) it is shown in [BS86] that equational theories which are not unitary are unbounded. Hence this notion can not be used to refine the hierarchy. In particular it can not be used to clarify the borderline between unitary and finitary theories nor - by considering the limes - the borderline between finitary and infinitary theories.

Both of these questions are still major open research problems. There are results and hard open problems similar to the compactness theorems or Ehrenfeucht Conjecture. These are tied to the concept of local subclass of a class of equational theories.

Let $term(T) := \{l, r: l = r \in T\}$ be the set of terms in the axiomatization of $T$ and let $I(T)$ be the set of instances of these terms:

$$
I (T) := \left\{\sigma t: t \in \text { term } (T), \sigma \in \Sigma \right\}.
$$

Similarly we define $G(T)$ as the finite set of all generalizations of these terms:

$$
G (T) := \left\{\sigma t: t \in \operatorname{term} (T), \sigma = [ \pi \leftarrow x ], \pi \in \Pi (t), x \in X \right\}.
$$

We assume terms equal under renaming to be discarded, i.e. $G(T) / \sim$ . With these two sets we obtain the characteristic set of an equational theory $T$ as:

$$
\chi (T) := I (T) \cup G (T)
$$

and the finite local-characteristic set as:

$$
\lambda (T) := \operatorname{term} (T) \cup G (T).
$$

Let $\mathcal{E}(T)$ be some first order property of $T$ . If the property $\mathcal{E}$ is only considered with respect to a subset $TS$ of $T$ , we write $\mathcal{E}(T)|_{TS}$ . For a theory $T\mathcal{E}(T)$ is $\chi$ -reducible iff $\mathcal{E}(T)|_{\chi(T)}$ implies $\mathcal{E}(T)$ . Similarly theory $T$ is $\lambda$ -reducible iff $\mathcal{E}(T)|_{\lambda(T)}$ implies $\mathcal{E}(T)$ .

For certain theories it may even be possible to reduce $\mathcal{E}(T)$ to a finite test set $\operatorname{loc}(T) \subset T$ such that $\mathcal{E}(T)|_{\operatorname{loc}(T)}$ implies $\mathcal{E}(T)$ .

A typical result, shown in [Sz82] is:

Theorem. The matching problem for admissible, canonical and regular theories is $\chi$ -reducible.

This theorem greatly simplifies the test for finitary or infinitary matching since we only have to show that it holds for matching problems on $\chi(T)$ ; i.e. for all problems $\langle s \geq t \rangle_{T}$ with $s, t \in \chi(T)$ .

A major research problem of the field is to $\lambda$ -reduce (or at least to $\chi$ -reduce) the property of a theory to be unitary, finitary or infinitary. A first result in this respect is the $\lambda$ -reducibility of unitary matching theories [Sz82]:

Theorem. The test for unitary matching is $\lambda$ -reducible.

Theorems of this nature are of considerable practical importance since they allow an immediate classification of a given theory: usually it is not too hard to find some unification algorithm for a given theory – however it can be very tricky to ensure that it is complete, i.e. that it generates all unifiers. But if we already know that the given theory is unitary or finitary this task is greatly simplified.

The following results are concerned with the reducibility of unitary unification theories.

In 1975 P. Hayes conjectured that Robinson's unification algorithm for free terms may well be the only case with at most one most general unifier. Unfortunately this is not the case: for example let $T_{a,b} := \{a = b\}$ for any constants $a, b$ then $T_{a,b}$ is unitary. But the problem turned out to be more complex than anticipated at the time: for example let $T_{aa} := \{f(a, a) = a\}$ for any constant $a$ , then $T_{aa}$ is unitary. We first observe that the unitary unification theories are a proper subset of the unitary matching theories and in [Sz82] it is shown that

Theorem. The unitary unification theories are $\chi$ -reducible.

To illustrate the use of the above theorems let us consider the empty theory $T_{\varnothing}$ , i.e. the Robinson unification problem for free terms. In order to show that $T_{\varnothing}$ is unitary, in the stone age of unification theory one had to invent a special algorithm and then prove its completeness and correctness [Ro65], [KB70].

A more elegant method is contained in [Ht76]: factoring T by $\approx$ , it is possible to show that $T|_{\approx}$ forms a complete semi-lattice under $\leq$ . Hence if two terms are unifiable there exists a common instance and hence there exists a l.u.b., which is the most general such instance: thus follows $T_{\varnothing}$ is unitary.

However using the above theorem, this result is immediate: Since the absolutely free algebra of terms is in particular $\Omega$ -free: $T_{\varnothing}$ is finitary matching [Sz82]. Now since $\chi(T_{\epsilon})$ is empty every TEST set is empty. Hence there does not exist a pair in TEST with more than one mgu, thus follows $T_{\varnothing}$ is finitary.

Although the comparative study of theories and classes of theories has uncovered interesting algebraic structures this is without doubt nothing but the tip of an iceberg of still unknown results.

## 4. References

[An71] P. Andrews: “Resolution in Type Theory”, J. of Symbolic Logic, vol. 36, 1971.

[An84] P. Andrews: “Automating Higher Order Logic”, in: Contemporary Mathematics, American Math Soc., 1984.

[AT85] A. Arnberg, T. Eiden; “Unification Problems with One-Sided Distributivity”, Proc. of Conf. on Rewriting Techniques, Springer Lecture Notes on Comp. Sci., 1985.

[BA72] Barrow, Ambler, Burstall: “Some techniques for recognizing Structures in Pictures”, Frontiers of Pattern Recognition, Academic Press Inc., 1972.

[Ba78] L.D. Baxter: “The Undecidability of the Third Order Dyadic Unification Problem”, Information and Control, vol. 38, no. 2, 1978.

[Ba73] L.D. Baxter: “An efficient Unification Algorithm”, Rep. CS-73-23, University of Waterloo, Dept. of Analysis and Computer Science, 1973.

[Ba86] A. Baader: “Unification in Idempotent Semigroups is of Type Zero”, J. of Automated Reasoning, to appear 1986.

[BB82] D. Ballard, Ch. Brown: "Computer Vision", Prentice Hall, New Jersey, 1982.

[BC66] H. Bryan, J. Carnog: "Search Methods used with Transistor Patent Applications", IEEE Spectrum 3, 2, 1966.

[BF77] H.P. Böhm, H.L. Fischer, P. Raulefs: “CSSA: Language Concepts and Programming Methodology”, Proc. of ACM, SiGPLAN/ART Conference, Rochester, 1977.

[Bi35] G. Birkhoff: “On the Structure of Abstract Algebras”, Proc. Cambridge Phil. Soc., vol. 31, 1935.

[Bl71] F. Blair et al.: “SCRATCHPAD/1: An interactive Facility for symbolic Mathematics”. Proc. of the 2nd Symposium on Symbolic Manipulation, Los Angeles, 1971.

[BL77] A. Ballantyne, D. Lankford: “Decision Procedures for simple Equational Theories”, University of Texas at Austin, ATP-35, ATP-37, ATP-39, 1977.

[BL85] Brackmann, Levesque: “Readings in Knowledge Representation”, Will. Kaufmann Inc., 1985.

[BM77] R. Boyer, J.S. Moore: "A Fast String Searching Algorithm". CACM vol. 20, no. 10, 1977.

[BM82] Ch. Beilken, F. Mattern, M. Spenke: “Entwurf und Implementierung von CSSA”, vol. A-E, SEKI-Memo-82-03, University of Kaiserslautern, 1982.

[Bo68] D.G. Bobrow (ed.): “Symbol Manipulation Languages”, Proc. of IFIP, North Holland Publishing Comp., 1968.

[Bo85] R. Book: “Thue Systems as Rewriting Systems”, in: Proc. of Rewriting Techniques, Springer Lecture Notes in Comp. Sci., vol. 202, 1985.

[BS85] Brachmann, Schnolze: "An Overview of KL-ONE", Cognitive Science, vol. 9, no. 2, 1985.

[BS85] B. Buchanan, R. Shortliffe: “Rule Based Expert Systems”, Addison Wesley, 1985.

[BS86] R. Book, J. Siekmann: "On the Unification Hierarchy", to appear in J. of Symbolic Computation, 1986.

[Bu85] B. Buchberger: “Basic Features and Development of the Critical Pair Completion Procedure”, Proc. Rewriting Techniques and Applications, Springer Lecture Notes in Comp. Sci., vol. 202, 1985.

[Bü86] H.J. Bürckert: “Some Relationship between Unification and Matching”, Proc. 8th Conf. on Autotom. Deduction, Springer Lecture Notes Comp. Sci., 1986.

[Bü85] W. Büttner: “Unification in the Datastructure Multisets”, SEKI-Report, Univ. Kaiserslautern, 1985.

[Bü86] W. Büttner: “Unification in the Datastructure Sets”. Proc. of 8th Conf. on Automated Deduction, Springer Lecture notes, 1986.

[BW77] D. Bobrow, T. Winograd: "An Overview of KRL", Cognitive Science, vol. 1, no. 1, 1977.

[CK71] C. Christensen, M. Karr: “IAM, A System for Interactive Algebraic Manipulation”, Proc. of the 2nd Symposium on Symbolic Manipulation, Los Angeles, 1971.

[CM81] W. Clocksin, C. Mellish: "Programming in PROLOG", Springer 1981.

[Co70] E.F. Codd: "A Relational Model of Data for Large Shared Databanks", CACM, 13, 6, 1972.

[Co72] E.F. Codd: “Relational Completeness of Data Base Sublanguages”, in Data Base Systems, Prentice Hall, Courant Comp. Science Symposia Series, vol. 6, 1972.

[CP61] A. Clifford, G. Preston: “The Algebraic Theory of Semigroups”, vol. I and vol. II, 1961.

[Cr68] D.G. Corneil: “Graph Isomorphism”, Ph.D. Dept. of Computer Science, University of Toronto, 1968.

[Da71] J.L. Darlington: "A Partial Mechanization of second Order Logic", Mach. Int. 6, 1971.

[Da76] C.J. Date: "An Introduction to Database Systems", Addison-Wesley Publ. Comp. Inc., 1976.

[Da63] M. Davis: “Eliminating the Irrelevant from Mechanical Proofs”, Symposia of Applied Math., vol. 15. American Mathematical Society, 1963.

[Da65] M. Davis: "The Undecidable", Raven Press, New York, 1965.

[Da73] M. Davis: "Hilbert's Tenth Problem is Unsolvable", Amer. Math. Monthly, vol. 80, 1973.

[DL86] D. Degroot, G. Lindstrom: "Logic Programming: Functions, Relations and Equations", Prentice Hall, 1986.

[Fa71] R. Fateman: “The User-Level Semantic Matching Capability in MACSYMA”, Proc. of the 2nd Symposium on Symbolic Manipulation, Los Angeles, 1971.

[Fa79] M. Fay: “First Order Unification in an Equational Theory”, Proc. 4th Workshop on Automated Deduction, Texas, 1979.

[Fa83] F. Fage: “Associative Commutative Unification”, INRIA report CNRS-LITP4, 1983.

[FG64] D.J. Farber, R.E. Griswald, I.P. Polonsky: "SNOBOL as String Manipulation Language", JACM, vol. 11, no. 2, 1964.

[FG84] Proc. of Conf. on Fifth Generation Computer Systems, ICOT, North Holland, 1984.

[FH83] F. Fage, G. Huet: “Complete Sets of Unifiers and Matchers in Equational Theories”, Proc. CAAP-83, Springer Lec. Notes Comp. Sci, vol. 159, 1983.

[Fo81] C. Forgy: "OPS5 User Manual", CMU Techn. Report, CMU-CS-81-135, 1981.

[Fo82] C. Forgy: “Rete: A Fast Algorithm for the Many Pattern/Object Match Problem”, J. of Art. Intelligence, vol. 19, no. 1, 1982.

[Gi73] J.F. Gimpel: “A Theory of Discrete Patterns and their Implementation in SNOBOL4”, CACM 16, 2, 1973.

[Gl84] J. Gabriel (et al.): "A Tutorial on the Warren Abstract Machine", Argonne National Lab., ANL-84-84, 1984.

[GM78] H. Gallaire, J. Minker: “Logic and Databases”, Plenum Press, 1978.

[Go66] W.E. Gould: “A Matching Procedure for $\omega$ -Order Logic”, Scientific Report no. 4, Air Force Cambridge Research Labs., 1966.

[GO67] J.R. Guard, F.C. Oglesby, J.H. Kenneth, L.G. Settle: “Semi-Automated Mathematics”, JACM 1969, vol. 18, no. 1.

[Go81] D. Goldfarb: “The Undecidability of the Second Order Unification Problem”, Journal of Theor. Comp. Sci., 13, 1981.

[Gr79] G. Grätzer: “Universal Algebra”, Springer Verlag, 1979.

[GT77] J. Goguen, J. Thatcher, E. Wagner, J. Wright: “Initial Algebra Semantics and Continuous Algebras”, JACM, vol. 24, no. 1, 1977.

[Gu64] J.R. Guard: “Automated Logic for Semi-Automated Mathematics”, Scientific report no. 1, Air Force Cambridge Research Labs., AD 602710, 1964.

[He82] A. Herold: “Universal Unification and a class of Equational Theories”, Proc. GWAI-82, W. Wahlster (ed.) Springer Fachberichte, 1982.

[He82] A. Herold: “Some Basic Notions of First Order Unification Theory”, Univ. Karlsruhe, Interner Report, 1983.

[He86] A. Herold: “Combination of Unification Algorithms”, Proc. 8th Conf. on Autom. Deduction, Springer Lecture Notes on Comp. Sci., 1986.

[He30] J. Herbrand: “Recherches sur la Théorie de la Démonstration”, Travaux de la Soc. des Sciences et des Lettres de Varsovie, no. 33, 128, 1930.

[He75] G.P. Huet: “A Unification Algorithm for Typed $\lambda$ -Calculus”, J. Theor. Comp. Sci., 1, 1975.

[Hj64] J.I. Hmelevskij: “The Solution of certain Systems of World Equations”, Dokl. Akad. Nauk SSSR, 1964, 749 Soviet Math. Dokl. 5, 1964, 724.

[Hj66] J.I. Hmelevskij: “World Equations without Coefficients”, Dokl. Akad. Nauk SSSR 171, 1966, 1047 Soviet Math. Dokl. 7, 1966, 1611.

[Hj67] J.I. Hmelevskij: “Solution of World Equations in three Unknowns”, Dokl. Akad. Nauk SSSR 177, 1967, no. 5, Soviet Math. Dokl. 8, 1967, no. 6.

[H180] J.M. Hullot: “A Catalogue of Canonical Term Rewriting Systems”, Research rep. CSL-113, SRI-International, 1980.

[Hn71] A. Hearn: “REDUCE2, A System and Language for Algebraic Manipulation”, Proc. of the 2nd Symposium on Symbolic Manipulation, Los Angeles, 1971.

[Ho76] J. Howie; "Introduction to Semigroup Theory", Acad. Press 1976.

[HO80] G. Huet, D.C. Oppen: “Equations and Rewrite Rules”, in “Formal Languages: Perspectives and Open Problems”, Ed. R. Book, Academic Press, 1980.

[Hr73] S. Heilbrunner: “Gleichungssysteme für Zeichenreihen”, TU München, Abtl. Mathematik, Ber. Nr. 7311, 1973.

[HS85] A. Herold, J. Sekmann: “Unification in Abelian Semigroups”.

[Ht72] C. Hewitt: “Description and Theoretical Analysis of PLANNER, a Language for Proving Theorems and Manipulation Models in a Robot”, Dept. of Mathematics, Ph. C. Thesis, MIT, 1972.

[ Ht76] C. Hewitt: “Viewing Control Structures as Patterns of Passing Messages”, MIT, AI-Lab., Working Paper 92, 1976.

[Ht72] G.P. Huet: “Constrained Resolution: A Complete Method for Theory”, Jenning’s Computing Centre rep. 1117, Case Western Reserve Univ., 1972.

[Ht73] G.P. Huet: “The Undecidability of Unification in Third Order Logic”, Information and Control 22 (3), 257–267, 1973.

[Ht75] G. Huet: “Unification in Typed Lambda-Calculus”, in $\lambda$ -Calculus and Comp. Sci. Theory, Springer Lecture Notes, No. 37, Proc. of the Symp. held in Rome, 1975.

[Ht76] G. Huet: “Résolution d'Équations dans des Languages d'ordre 1, 2,..., ω”, Thèse d'État, Univ. de Paris, VII, 1976.

[Ht78] G. Huet: “An Algorithm to Generate the Basis of Solution to Homogeneous Linear Diophantine Equations”, Information Proc. Letters 7, 3, 1978.

[Ht80] G. Huet: “Confluent Reductions: Abstract Properties and Applications to Term Rewriting Systems”, JACM vol. 27, no. 4, 1980.

[Hu79] J.M. Hullot: “Associative Commutative Pattern Matching”, 5th Int. Joint Conf. on AI, Tokyo 1979.

[Hu80] J.M. Hullot: “Canonical Forms and Unification”, Proc. of 5th Workshop on Automated Deduction, Springer Lecture Notes, 1980.

[IM83] N. Ito, K. Masuda, H. Shimizu: "Parallel PROLOG Machine", ICOT Research Centre, TR-035, 1983.

[Je80] J. Jeanrond: “Deciding Unique Termination”, Proc 5th Conf. on Autom. Deduction, Springer Lecture Notes in Comp. Sci., vol. 87, 1980.

[JP73] D. Jensen, T. Pietrzykowski: “Mechanizing $\lambda$ -Order Type Theory through Unification”, Rep. CS73-13, Dept. of Applied Analysis and Comp. 4, 1972.

[JK83] J. Jouannaud, C. Kirchner, H. Kirchner: “Incremental Construction of Unification Algorithms in Equational Theories”, Proc. Int. Colloq. on Automata, Languages and Programming, 1983.

[JKK82] J. Jounnaud, C. Kirchner, H. Kirchner: “Incremental Unification in Equational Theories”, Université de Nancy, Informatique, 82-R-047, 1982.

[Ka84] M. Kay: "Functional Unification Grammars", Proc. of COLING, Stanford, 1984.

[Ka85] L. Karttunen: "Helsinki Unification Grammars", SRI-International and CSLI, 1985.

[KB70] D.E. Knuth, P.B. Bendix: “Simple World Problems in Universal Algebras”, in: Computational Problems in Abstract Algebra, J. Leech (ed), Pergamon Press, Oxford, 1970.

[Ki85] C. Kirchner: “Methodes et Outils de Conception Systématique d’Algorithms d’Unification (thèse d’état), Univ. Nancy, 1985.

[KK82] D. Kapur, M.S. Krishnamoorthy, P. Narendran: “A New Linear Algorithm for Unification”, General Electric, Rep. no. 82CRD-100, New York, 1982.

[KM72] Karp, Miller, Rosenberg: “Rapid Identification of Repeated Patterns in Strings, Trees and Arrays”, ACM Symposium on Th. of Comp. 4, 1972.

[KM74] Knuth, Morris, Pratt: “Fast Pattern Matching in Strings”, Stan-CS-74-440, Stanford University, Comp. Sci. Dept., 1974.

[KM77] S. Kühner, Ch, Mathis, P. Raulefs, J. Siekmann: “Unification of Idempotent Functions”, Proceedings of 4th IJCAI, MIT, Cambridge, 1977.

[Ko79] R. Kowalsky: "Logic for Problem Solving", North Holland, 1979.

[La79] D.S. Lankford: “A Unification Algorithm for Abelian Group Theory”, Rep. MTP-1, Louisiana Techn. Univ., 1979.

[L380] D.S. Lankford: “A New Complete FPA-Unification Algorithm”, MIT-8, Louisiana Techn. Univ., 1980.

[LB79] D.S. Lankford, M. Ballantyne: “The Refutation Completeness of Blocked Permutative Narrowing and Resolution”, 4th workshop on Autom. Deduction, Texas, 1979.

[LBB84] D.S. Lankford, G. Butler, B. Brady: “Abelian Group Unification Algorithms for elementary Terms”, Contemporary Mathematics, American Math. Soc., 1984.

[Lc72] C.L. Lucchesi: “The Undecidability of the Unification Problem for Third Order Languages”, Rep. CSRR 2059, Dept. of Applied Analysis and Comp. Sci., Univ. of Waterloo, 1972.

[Lo78] D. Loveland: "Automated Theorem Proving", North Holland, 1978.

[LS75] M. Livesey, J. Siekmann: “Termination and Decidability Results for Stringunification”, Univ. of Essex, Memo CSM-12, 1975.

[LS76] M. Livesey, J. Siekmann: “Unification of Sets and Multisets”, Univ. Karlsruhe, Techn. Report, 1976.

[LS79] M. Livesey, J. Siekmann, P. Szabo, E. Unvericht: “Unification Problems for Combinations of Associativity, Commutativity, Distributivity and Idempotence Axioms”, Proc. of Conf. on Autom. Deduction, Austin, Texas, 1979.

[LS73] G. Levi, F. Sirovich: "Pattern Matching and Goal-Directed Computation", Nota Interna B73-12, Univ. of Pisa, 1973.

[Ma54] A.A. Markov: "Trudy Mat. Inst. Steklov", no. 42, Izdat. Akad. Nauk SSSR, 1954, NR17, 1038, 1954.

[Ma70] Y. Matiyasevich: “Diophantine Representation of Rec. Enumerable Predicates”, Proc of the Scand. Logic Symp., North Holland, 1978.

[Ma77] G.S. Makanin: “The Problem of Solvability of Equations in a Free Semigroup”. Soviet Acad Nauk SSSR, Tom 233, no. 2, 1977.

[MB68] Manove, Bloom, Engelmann: “Rational Functions in MATHLAB”, IFIP Conf. on Symb. Manipulation, Pisa, 1968.

[Mi75] M. Minsky: “A Framework for Representing Knowledge” in: P. Winston: “The Psychology of Computer Vision”, McGraw Hill, 1975.

[MM79] A. Martelli, U. Montaneri: “An Efficient Unification Algorithm”, University of Pisa, Techn. Report, 1979.

[MN86] U. Martin, T. Nipkow: “Unification in Boolean Rings”, Proc. 8th Conf. on Autom. Deduction, Springer Lecture Notes, 1986.

[Mo71] J. Moses: "Symbolic Integration: The Stormy Decade", CACM 14, 8, 1971.

[Mo74] J. Moses: "MACSYMA-the fifth Year", Project MAC, MIT, Cambridge, 1974.

[Mu83] K. Mukai: "A Unification Algorithm for Infinite Trees", Report ICOT, 1983.

[Mz86] J. Mzali: "Matching with Distributivity", Proc. of 8th Conf. on Automated Deduction, Springer Lecture Notes, 1986.

[Ne71] A. Nevins: "A Human Oriented Logic for ATP", JACM 21, 1974 (first report 1971).

[Ng79] W.Ng (ed): "Proc. Conf. Symbolic and Algebraic Computation", Springer Lecture Notes in Comp. Sci., 1979.

[NO80] G. Nelson, D. Oppen: “Fast Decision Procedures Based on Congruence Closure”, JACM, 27, 2, 1980.

[PI72] G. Plotkin: "Building in Equational Theories", Machine Intelligence, vol. 7, 1972.

[Pr60] D. Prawitz: "An Improved Proof Procedure", Theoria 26, 1960.

[PS81] G. Peterson, M. Stickel: “Complete Sets of Reductions for Equational Theories with Complete Unification Algorithms”, JACM, vol. 28, no. 2, 1981.

[PW78] M. Paterson, M.W. Wegman: “Linear Unification”, J. of Comp. and Syst. Science, 16, 1968.

[RD72] Rulifson, Derksen, Waldinger: "QA4: A Procedural Calculus for Intuitive Reasoning", Stanford Univ., Nov. 1972.

[R169] J. Rastall: "Graph Family Matching", University of Edinburgh, MIP-R-62, 1969.

[Ro67] J.A. Robinson: "A Review on Automated Theorem Proving", Symp. Appl. Math., vol. 19, 1-18, 1967.

[Ro65] J.A. Robinson: "A Machine Oriewnted Logic Based on the Resolution Principle", JACM 12, 1965.

[Ro69] J.A. Robinson: "Mechanizing Higher Order Logic", Machine Intelligence, vol. 4, Edinburgh Univ. Press, 1969.

[Ro71] J.A. Robinson: “Computational Logic: The Unification Computation”, Machine Intelligence, vol 6, 1971.

[Ro85] P. Robinson: "The SUM: An AI Coprocessor", Byte, vol. 10, no. 6, 1985.

[RS78] P. Raulefs, J. Siekmann: “Unification of Idempotent Functions”, Universität Karlsruhe, Techn. Report, 1978.

[RSS79] P. Raulefs, J. Siekmann, P. Szabo, E. Unvericht: “A short Survey on the State of the Art in Matching and Unification Problems”, SIGSAM Bulletin, 13, 1979.

[RZ85] R. Ramnarayan, G. Zimmermann: “PESA, A Parallel Architecture for OPS5 Production Systems”, 19th Annual Hawaii International Conference on Systems Sciences, 1985.

[Sz79] P. Szabo: “Undecidability of the $D_{A}$ -Unification Problems”, Proc. of GWAI, 1979.

[Sch86] M. Schmidt-Schauss: “Unification under Associativity and Idempotence is of Type Nullary”, J. of Automated Reasoning, to appear 1986.

[Sch86] M. Schmidt-Schauss: “Unification in Many-Sorted Equational Theories”, Proc. of 8th Conf. on Autom. Deduction, Springer Lecture Notes Comp. Sci., 1986.

[Sh76] E.H. Shortliffe: "MYCIN: Computer Based Medical Consultations", North Holland Publ. Comp., 1976.

[SH75] B.C. Smith, C. Hewitt: "A Plasma Primer", MIT, AI-Lab., 1975.

[Sh84] R. Shostak: “Deciding Combinations of Theories”, JACM, vol. 31, no. 1, 1984.

[SH85] G. Snelting, W. Henhapl: “Unification in Many Sorted Algebras as a Device for Incremental Semantic Analysis”, Internal Report PU2R2/85, Techn. Univ. Darmstadt, FB Informatik, 1985.

[Si75] J. Siekmann: "Stringunification", Essex University, Memo CSM-7, 1975.

[Si76] J. Siekmann: "Unification of Commutative Terms", Univ. Karlsruhe, 1976.

[Si78] J. Siekmann: “Unification and Matching Problems”, Ph.D., Essex Univ., Memo CSA-4-78.

[Sk84] S. Shieber, L. Karttunen, F. Pereira: “Notes from the Unification Underground”, SRI-International, TN327, 1984.

[SK85] S. Shieber, L. Karttunen, F. Pereira: "More Notes from the Unification Underground", SRI-International, TN361, 1985.

[Sl72] J.R. Slagle: “ATP with built-in Theories including Equality, Partial Ordering and Sets”, JACM 19, 120–135, 1972.

[Sl74] J.R. Slagle: “ATP for Theories with Simplifiers, Commutativity and Associativity”, JACM 21, 1974.

SO82] J. Siekmann, P. Szabo: “Universal Unification and a Classification of Equational Theories”, Proc. of Conf. on Autom. Deduction, 1982, New York, Springer Lecture Notes Comp. Sci., vol. 87.

[SS81] J. Siekmann, P. Szabo: “Universal Unification and Regular ACFM Theories”, Proc. IJCAI-81, Vancouver, 1981.

[SS82] J. Siekmann, P. Szabo: “A Notherian and Confluent Rewrite System for Idempotent Semigroups”, Semigroup Forum, vol. 25, 1982.

[SS61] D. Skordew, B. Sendow: “Z. Math. Grundlagen”, Math. 7 (1961), 289, MR 31, 57 (Russian) (English translation at Univ. of Esex, Comp. Sci. Dept.).

[St81] M. Stickel: “A Unification Algorithm for Assoc. Commutative Functions”, JACM, vol. 28, no. 3, 1981.

[St74] G.F. Steward: "An Algebraic Model for String Patterns", Univ. of Toronto, CSRG-39, 1974.

[Su65] E. Sussenguth: “A Graph-theoretical Algorithm for Matching Chemical Structures”, J. Chem. Doc. 5, 1, 1965.

[SU78] P. Szabo, E. Unvericht: “The Unification Problem for Distributive Terms”, Univ. Karlsruhe, 1978.

[Sz82] P. Szabo: “Theory of First Order Unification” (in German, thesis) Univ. Karlsruhe, 1982.

[Ta68] A. Tarski: “Equational Logic and Equational Theories of Algebra”, Schmidt et al (eds), Contributions to Mathematical Logic, North Holland, 1968.

[Ta79] W. Taylor: "Equational Logic", Houston J. of Math., 5, 1979.

[Te81] H. Tennant: “Natural Language Processing”, Petrocelli Books, 1981.

[Ti84] E. Tiden: “Unification in Combination of Collapse Free Theories with Disjoint Sets of Function Symbols”, Proc. 8th Conf. on Autom. Deduction, Springer Lecture Notes on Comp. Sci., 1986.

[Ul76] J.R. Ullman: “An Algorithm for Subgraph Isomorphism”, JACM, vol. 23, no. 1, 1976.

[Un64] S.H. Unger: “GIT-Heuristic Program for Testing Pairs of Directed Line Graphs for Isomorphism”, CACM, vol. 7, no. 1, 1964.

[Va75] J. van Vaalen: “An Extension of Unification to Substitutions with an Application to ATP”, Proc. of 4th IJCAI, Tbilisi, USSR, 1975.

[Vo78] E. Vogel: “Unifikation von Morphismen”, Diplomarbeit, Univ. Karlsruhe, 1978.

[VZ75] M. Venturini-Zilli: "Complexity of the Unification Algorithm for First Order Expression", Clacolo XII, Fasc IV, 1975.

[Wa77] D.H.D. Warren: "Implementing PROLOG", vol. 1 and vol. 2, D.A.I. Research Rep., no. 39, Univ. of Edinburgh, 1977.

[Wa84] Ch. Walther: “Unification in Many Sorted Theories”, Univ. Karlsruhe, 1984.

[Wa86] Ch. Walther: “A Classification of Many Sorted Unification Problems”, Proc. of 8th Conf. on Automated Deduction, Springer Lecture Notes Comp. Sci., 1986.

[WC76] K. Wong, K. Chandra. "Bounds for the String Editing Problem", JACM vol. 23, no. 1, 1976.

[We73] P. Weiner: “Linear Pattern Matching Algorithms”, IEEE Symp. on SW. and Automata Theory, 14, 1973.

[Wi76] van Wijngaarden (et al.): “Revised Rep. on the Algorithmic Language ALGOL68”, Springer Verlag, Berlin, Heidelberg, N.Y., 1976.

[Wn75] Winston: "The Psychology of Computer Vision", McGraw Hill, 1975.

[Wn72] T. Winograd: "Understanding Natural Language". Edinburgh Univ. Press, 1972.

[Wn83] T. Winograd: “Language as a Cognitive Process”, vol. 1, Addison Wesley, 1983.

[Wn76] G. Winterstein: “Unification in Second Order Logic”, Bericht 3, Univ. Kaiserslautern, 1976.

[WR67] L. Wos, G.A. Robinson, D. Carson, L. Shalla: “The Concept of Demodulation in Theorem Proving”, JACM, vol. 14, no. 4, 1967.

[WR73] L. Wos, G.A. Robinson: “Maximal Models and Refutation Completeness: Semidecision Procedures in Automatic Theorem Proving”, in: Word Problems (W.W. Boone, F.B. Cannonito, R.C. Lyndon, eds), North Holland, 1973.

[Ye85] K. Yelick: “A Generalized Approach to Equational Unification, MIT/LCS/TR-344, 1985.
