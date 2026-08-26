---
otero_id: 19636
otero_key: "Z7EM8245"
title: "Exploring recommendations for circular supply chain management through interactive visualisation"
authors: "Guido van Capelleveen; Jesse van Wieren; Chintan Amrit; Devrim Murat Yazan; Henk Zijm"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113431"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/entcs

# Clausal Tableaux for Hybrid PDL

Mark Kaminski Gert Smolka

Saarland University Saarbr¨ucken, Germany

## Abstract

We present the first tableau-based decision procedure for PDL with nominals. The procedure is based on a prefix-free clausal tableau system designed as a basis for gracefully degrading reasoners. The clausal system factorizes reasoning into regular, propositional, and modal reasoning. This yields a modular decision procedure and pays of in transparent correctness proofs.

Keywords: hybrid logic, dynamic logic, tableau systems, decision procedures

## 1 Introduction

PDL (propositional dynamic logic) [6,13,9] is an expressive modal logic invented for reasoning about programs. It extends basic modal logic with expressions called programs. Programs describe relations from states to states and are used to express modalities. Programs are composed with the operators familiar from regular expressions. In addition, they may employ formulas so that conditionals and while loops can be expressed. Fischer and Ladner [6] show the decidability of PDL using a filtration argument. They also prove that the satisfiability problem for PDL is EXPTIME-hard. Pratt [17] shows that PDL satisfiability is in EXPTIME using a tableau method with an and-or graph representation. Gor´e and Widmann [7,8] address the eficient implementation of Pratt-style decision procedures.

We consider PDL extended with nominals [14,15], a logic we call hybrid PDL or HPDL. Nominals are atomic formulas that hold exactly for one state. Nominals equip PDL with equality and are the characteristic feature of hybrid logic [2]. The satisfiability problem of HPDL is in EXPTIME [15,18].

We are interested in a tableau system for HPDL that can serve as a basis for gracefully degrading decision procedures. We found it impossible to extend one of the existing tableau methods for PDL [17,5,1,7] to nominals. The dificulties are in the correctness proofs. For Pratt-like methods [17,7], the problem stems from the fact that the global and-or graph representation is not compatible with nominal propagation (see Remark 5.6 in [10] for a discussion and an example; the problem is also noted in [19]).

The dificulties led us to the development of a new tableau method for modal logic. The new method is based on a prefix-free clausal form. In a previous paper [10] we used the method to give a tableau-based decision procedure for the sublogic of HPDL that restricts programs to the forms a and $a ^ { * }$ where a is a primitive action. In the present paper we extend the clausal method to full HPDL and obtain the first tableau-based decision procedure for HPDL.

Our method factorizes reasoning into regular reasoning, propositional reasoning and modal reasoning. At each level we realize reasoning with tableau methods. Nominals are handled at the modal level. Given our approach, the integration of nominals is straightforward. The modular structure of our decision procedure pays of in transparent correctness proofs. Each level invites optimizations. The regular level, in particular, asks for further investigation. It may profit from eficient methods for translating regular expressions into deterministic automata.

In contrast to previous approaches, we do not rely on the Fischer-Ladner closure. Instead, we use the notion of a finitary regular DNF that can be obtained at the regular level.

Following Baader [3] and De Giacomo and Massacci [5], we disallow bad loops and thus avoid the a posteriori eventuality checking of Pratt’s method [17].

The paper is organized as follows. First we define HPDL and outline the clausal tableau method with examples. Then we address, one after the other, regular, propositional, and modal reasoning. Finally, we prove the correctness of the decision procedure.

## 2 Hybrid PDL

We define the syntax and semantics of HPDL. We assume that three kinds of names are given:

• nominals (metavariables x, y, z; denote states)

• predicates (metavariables $p , q , r ;$ denote sets of states)

• actions (metavariables $a , b , c ;$ denote relations from states to states).

The interpretations of HPDL are the usual transition systems where states are labelled with predicates and edges are labelled with actions. Formally, an interpretation I is a tuple consisting of the following components:

• A nonempty set |I| of states.

• A state $\tau x \in | \tau |$ for every nominal x.

• A set $\mathcal { T } p \subseteq | \mathcal { T } |$ for every predicate p.

• A relation $\stackrel { a } { \to } \tau \subseteq | \mathcal { I } | \times | \mathcal { I } |$ for every action a.

Formulas (metavariables $s , t , u )$ and programs $( \alpha , \beta , \gamma )$ are defined as follows:

$$
s := x \mid p \mid \neg s \mid s \wedge s \mid \langle \alpha \rangle s
$$

$$
\alpha : := a \mid s \mid 1 \mid \alpha + \alpha \mid \alpha \alpha \mid \alpha^ {*}
$$

The grammar is to be read inclusive, that is, every nominal and every predicate is a formula, and every action and every formula is a program. Given an interpretation, formulas denote sets of states and programs denote relations from states to states. We use the letters $X , ~ Y , ~ Z$ to denote states. The semantic relations $\scriptstyle { \mathcal { Z } } , X \mid = s$ and $X { \xrightarrow { \alpha } } \chi Y$ are defined by mutual induction on the structure of formulas and programs:

$$
\mathcal {I}, X \models x \iff X = \mathcal {I} x
$$

$$
\mathcal {I}, X \models p \iff X \in \mathcal {I} p
$$

$$
\mathcal {I}, X \models \neg s \iff \text { not } \mathcal {I}, X \models s
$$

$$
\mathcal {I}, X \models s \land t \iff \mathcal {I}, X \models s \text { and } \mathcal {I}, X \models t
$$

$$
\mathcal {I}, X \models \langle \alpha \rangle s \iff \exists Y \colon X \xrightarrow {\alpha} _ {\mathcal {I}} Y \text {and} \mathcal {I}, Y \models s
$$

$$
X \stackrel {a} {\longrightarrow} _ {\mathcal {I}} Y \iff X \stackrel {a} {\rightarrow} _ {\mathcal {I}} Y
$$

$$
X \stackrel {s} {\longrightarrow} _ {\mathcal {I}} Y \iff X = Y \text {and} \mathcal {I}, X \models s
$$

$$
X \stackrel {1} {\longrightarrow} _ {\mathcal {I}} Y \iff X = Y
$$

$$
X \stackrel {\alpha + \beta} {\longrightarrow} _ {\mathcal {I}} Y \iff X \stackrel {\alpha} {\longrightarrow} _ {\mathcal {I}} Y \mathrm{or} X \stackrel {\beta} {\longrightarrow} _ {\mathcal {I}} Y
$$

$$
X \stackrel {\alpha \beta} {\longrightarrow} _ {\mathcal {I}} Y \iff \exists Z \colon X \stackrel {\alpha} {\longrightarrow} _ {\mathcal {I}} Z \mathrm{and} Z \stackrel {\beta} {\longrightarrow} _ {\mathcal {I}} Y
$$

$$
X \xrightarrow {\alpha^ {*}} _ {\mathcal {I}} Y \iff X \xrightarrow {\alpha} _ {\mathcal {I}} ^ {*} Y
$$

${ \xrightarrow { \alpha } } _ { \mathcal { T } } ^ { * }$ denotes the reflexive transitive closure of $\xrightarrow { \alpha } _ { \mathcal { T } }$

Given a set A of formulas, we write $\mathcal { T } , X \models A \mathrm { ~ i f ~ } \mathcal { T } , X \models s$ for all formulas $s \in A$ An interpretation I satisfies (or is a model of) a formula s or a set A of formulas if there is a state $X \in | \mathcal { I } |$ such that ${ \mathcal { T } } , X \models s { \mathrm { ~ o r ~ } }$ , respectively, $\textstyle { \mathcal { Z } } , X \models A$ . A formula s (a set A) is satisfiable if $s \ ( A )$ has a model.

The complement ${ \sim } s$ of a formula s is t if $s = \neg t$ and $\neg s$ otherwise. Note that ${ \sim } \sim s = s$ if s is not a double negation. We use the notations $s \vee t : = \neg ( \sim s \wedge \sim t )$ and $[ \alpha ] s : = \neg \langle \alpha \rangle \sim s$ . Note that $\sim \langle \alpha \rangle p = [ \alpha ] \neg p$ and $\sim \langle \alpha \rangle \neg p = [ \alpha ] p$ . The $s i z e \ | s |$ and |α| of formulas and programs is defined as the size of the abstract syntax tree. For instance, $| a p | = | \langle p \rangle q | = 3$ . Note that $| s \vee t | > | s | , | t |$ and $| [ \alpha ] s | \geq | \langle \alpha \rangle s | > | \alpha | , | s |$

## 3 Outline of the Method

Our tableau method is based on a clausal form, which provides for the separation of regular, propositional, and modal reasoning. We start with a few definitions and three examples.

A basic formula is a formula of the form p, x, or $\langle a \alpha \rangle s .$ . A literal is a basic formula or the complement of a basic formula. A clause (written $C , D , E )$ is a finite set of literals that contains no complementary pair (i.e., a pair of the form $p ,$ $\neg p )$ . We interpret clauses conjunctively. Satisfaction of clauses $( { \mathrm { i . e . , } } T , X \mid = C )$ is a special case of satisfaction of sets of formulas $( { \mathrm { i . e . , } } { \mathcal { T } } , X \Vdash A )$ , which was defined in §2. For instance, the clause $\{ \langle a \rangle p , [ a ] ( \neg p \land q ) \}$ is unsatisfiable.

A claim is a pair $C ^ { s }$ consisting of a clause C and a diamond formula s. While we do not require $s \in C$ , for every claim $C ^ { s }$ that we consider in the following it will be the case that $C$ supports s. The notion of support is defined formally later such that C supporting s (or A) and $\pi , X \models C$ implies I, $X \models s \left( \mathbb { Z } , X \models A \right)$ . The request of a clause C for an action a is $\mathcal { R } _ { a } C : = \{ [ \alpha ] s \mid [ a \alpha ] s \in C \}$ . As an example, consider the clause $C = \{ \langle a b ^ { * } \rangle p , \ \langle b b ^ { * } \rangle p , \ [ a ( a + b ) ^ { * } ] \neg p \}$ . We have ${ \mathcal { R } } _ { a } C = \{ [ ( a + b ) ^ { * } ] \neg p \}$ and $\mathcal { R } _ { b } C = \emptyset$

Our tableau method works on clauses and links (to be formally defined later) rather than single formulas. Intuitively, a link is a pair of claims $C ^ { s } D ^ { t }$ denoting that in order for a model to satisfy the diamond literal s in $C ,$ , it sufices to satisfy $D \cup \{ t \}$ . Given a single clause, the method tries to extend it to a tableau branch in which every diamond literal s in every clause $C$ is realized with a link $C ^ { s } D ^ { t }$ where D is one of the clauses of the branch. Provided the relation induced by the links is terminating, every such branch is a model of all of its clauses. If every branch constructed by the method fails to realize some diamond literal with a link or contains a loop formed by links, we conclude that the input is unsatisfiable. Thus we obtain a decision procedure for the satisfiability of clauses. At the same time, the procedure decides the satisfiability of formulas since in HPDL a formula s is satisfiable if and only if so is the clause $\{ \langle a \rangle s \}$ (the choice of a does not matter).

The method is implemented with three reasoners. The regular reasoner decomposes a program α into simpler (according to some measure) programs $\beta _ { 1 } , \ldots , \beta _ { n }$ such that $\alpha \equiv \beta _ { 1 } + \cdots + \beta _ { n }$ . For instance, $a ^ { * }$ is decomposed into $a a ^ { * }$ and 1.

The propositional reasoner determines for every set A of formulas a set of clauses supporting A such that $\textstyle { \mathcal { Z } } , X \models A$ if and only if $\pi , X \models C$ for one of the clauses. Given the formula $\langle a ^ { * } \rangle p \wedge [ b ^ { * } ] \neg p$ , for instance, the propositional reasoner determines the single clause $\{ \langle a a ^ { * } \rangle p , \ \neg p , \ [ b b ^ { * } ] \neg p \}$

The modal reasoner is the top-level reasoner of our tableau method. For every satisfiable clause it constructs a finite model whose states are clauses and where every state $C$ satisfies the clause $C .$ . To do ${ \mathrm { s o } } .$ , the modal reasoner starts with the initial clause and derives further clauses until every diamond literal s in every clause C is realized with a link. The modal reasoner calls the regular reasoner to determine the successor formula t and the propositional reasoner to determine the successor clause D. The tableau method terminates since the derived clauses must take their literals from a finite set that can be determined from the initial formulas.

Let us now give three examples illustrating our method in action. At this point, they are there to provide some additional intuition about the method and do not have to be understood in all details. To fully understand the examples one should review them after all of the formal prerequisites have been introduced in $\ S 8$

Example 3.1 Consider the following literals and clauses:

$$
\begin{array}{l l} s := \langle a (a + b) ^ {*} \rangle p & C := \{t, \neg p, u \} \\ t := \langle b (a + b) ^ {*} \rangle p & D := \{s, t, \neg p, u \} \end{array}
$$

$$
u := [ b b ^ {*} ] (\neg p \land t) \quad E := \{p \}
$$

We start the modal reasoner with the satisfiable clause C. There is one claim $C ^ { t }$ to be realized. We need a clause that supports the formulas $\langle ( a + b ) ^ { * } \rangle p$ and $[ b ^ { * } ] ( \neg p \land t )$ The regular reasoner and the propositional reasoner determine $C ^ { t }$ and $D ^ { s }$ as possible successor clauses and successor literals. The modal reasoner rejects $C ^ { t }$ since it would introduce the loop $C ^ { t } C ^ { t }$ . The pair $D ^ { s }$ is fine and adds the clause D and the link $C ^ { t } D ^ { s }$ . The claim $C ^ { t }$ is now realized. However, the new clause $D$ has two unrealized claims $D ^ { s }$ and $D ^ { t }$ . To realize $D ^ { s }$ , we need a clause that supports the formula $\langle ( a + b ) ^ { * } \rangle p$ . The regular and the propositional reasoner yield the pairs $E ^ { \langle 1 \rangle p } , \{ s \} ^ { s }$ and $\{ t \} ^ { t }$ . We choose $E ^ { \langle 1 \rangle p }$ and add the clause $E$ and the link $D ^ { t } E ^ { \langle 1 \rangle p }$ . It remains to realize $D ^ { t }$ . To do so, we need a clause that supports the formulas $\langle ( a + b ) ^ { * } \rangle p$ and $[ b ^ { * } ] ( \neg p \land t )$ . As before, the regular and the propositional reasoner yield $C ^ { t }$ and $D ^ { s }$ Both are fine. We choose $C ^ { t }$ and add the link $D ^ { t } C ^ { t }$ . This gives us a model for the initial clause C. A graphical representation of the model looks as follows:

$$
\begin{array}{c} C \boxed {t, \neg p, u} \\ D \boxed {s, t, \neg p, u} \\ E \boxed {p} \end{array}
$$

Example 3.2 Consider the following literals:

$$
\begin{array}{l l l} s & := & \langle a (a + b) ^ {*} \rangle \neg p \\ t & := & \langle b (a + b) ^ {*} \rangle \neg p \end{array} \qquad \qquad \begin{array}{l l l} u & := & [ a (b + a) ^ {*} ] p \\ v & := & [ b (b + a) ^ {*} ] p \end{array}
$$

Here is a closed tableau for the unsatisfiable clause $\{ s , u \}$

$$
\begin{array}{c c} C _ {1} = \{s, u \} \\ \hline C _ {2} = \{s, p, u, v \} & C _ {3} = \{t, p, u, v \} \\ C _ {1} ^ {s} C _ {2} ^ {s} & C _ {1} ^ {s} C _ {3} ^ {t} \\ C _ {4} = \{t, p, u, v \} & C _ {5} = \{s, p, u, v \} \\ C _ {2} ^ {s} C _ {4} ^ {t} & C _ {3} ^ {t} C _ {5} ^ {s} \end{array}
$$

The tableau is closed since all possible links for the claims $C _ { 4 } ^ { t }$ and $C _ { 5 } ^ { s }$ introduce loops. For instance, for $C _ { 4 } ^ { t }$ the regular and the propositional reasoner yield the links $C _ { 4 } ^ { t } C _ { 2 } ^ { s }$ and $C _ { 4 } ^ { t } C _ { 4 } ^ { t }$ . Note that the clause names $C _ { i }$ do not act as prefixes. They are only used for explanatory purposes.

Example 3.3 Due to the clausal form, the extension of our tableau method to nominals is straightforward. When we add a new clause to a branch, we add to the new clause all literals that occur in clauses of the branch that have a nominal in common with the new clause. This takes care of nominal propagation. Clauses and links that are already on the branch remain unchanged.

Consider the clause $C = \{ \langle a a ^ { * } \rangle p , [ a ] ( x \wedge \neg p ) , [ b ] x , \langle b \rangle [ a ] \neg p \}$ . The initial tableau just consisting of C can be developed into a maximal branch as shown below (graphical representation). The numbers indicate the order in which the clauses are introduced. When clause 4 is introduced, nominal propagation from clause 2 takes place. Note that we obtain a model of all clauses on the branch by taking the clauses 1, 3, 4, and 5 as states and the triples 1a4, 1b4, 4a5, and 5a3 as transitions.

![](/api/attachments/Z7EM8245/fulltext/images/470fd1852295a4efaeda8c0a9be9913d34a12873aaeb67735f8156e6ab525ef5.jpg)

## 4 Language-Theoretic Semantics

We define a language-theoretic semantics for programs that treats formulas as atomic objects. This semantics is the base for the regular reasoner and decouples it from the propositional reasoner. It is also essential for the correctness proofs of the modal reasoner. The semantics is an adaption of the language-theoretic model of Kleene algebras with tests [12].

The letters A, B range over finite sets of formulas. A guarded string is a finite sequence $A a _ { 1 } A _ { 1 } \ldots a _ { n } A _ { n }$ where $n \geq 0$ . The letters $\sigma$ and $\tau$ range over guarded strings. Every program corresponds to a set of guarded strings, which can be seen as runs of the program. For instance, the program $( p a ) ^ { * } b \neg p$ corresponds to the set of all guarded strings $A _ { 1 } a A _ { 2 } \dots a A _ { n } a A _ { n + 1 } b A _ { n + 2 }$ such that $n \geq 1 , p \in A _ { 1 } \cap \cdot \cdot \cdot \cap A _ { n }$ and $\lnot p \in A _ { n + 2 }$ (there are no restrictions on $A _ { n + 1 } )$

The length |σ| of a guarded string $\sigma = A a _ { 1 } A _ { 1 } \ldots a _ { n } A _ { n }$ is n. We use For to denote the set of all formulas. A language is a set of guarded strings. For languages L and $L ^ { \prime }$ and sets of formulas A we define the following:

$$
\begin{array}{r c l} \mathcal {L} A := \{B \mid A \subseteq B \subseteq_ {\mathrm{fin}} \text {For} \} & L ^ {0} := \mathcal {L} \emptyset \\ L \cdot L ^ {\prime} := \{\omega A \omega^ {\prime} \mid \omega A \in L,   A \omega^ {\prime} \in L ^ {\prime} \} & L ^ {n + 1} := L \cdot L ^ {n} \\ & L ^ {*} := \bigcup_ {n \in \mathbb {N}} L ^ {n} \end{array}
$$

where $\omega , \omega ^ { \prime }$ range over partial, possibly empty guarded strings. Note that $L ^ { * } =$ $\mathcal { L } \varnothing \cup ( L - \mathcal { L } \varnothing ) \cdot L ^ { * }$ . We assign to every program α a language Lα:

$$
\mathcal {L} a := \{A a B \mid A, B \subseteq_ {\text { fin }} \text { For } \} \quad \mathcal {L} (\alpha + \beta) := \mathcal {L} \alpha \cup \mathcal {L} \beta
$$

$$
\begin{array}{l l} \mathcal {L} s := \mathcal {L} \{s \} & \mathcal {L} (\alpha \beta) := \mathcal {L} \alpha \cdot \mathcal {L} \beta \\ \mathcal {L} 1 := \mathcal {L} \emptyset & \mathcal {L} \alpha^ {*} := (\mathcal {L} \alpha) ^ {*} \end{array}
$$

Note that $\mathcal { L } ( s ^ { * } ) = \mathcal { L } 1 = \mathcal { L } ( ( s + t ) ^ { * } )$

Given an interpretation I, we define the relations $\sigma _ { \rangle \mathcal { T } \subseteq } | \mathcal { T } | \times | \mathcal { T } |$ by induction on the structure of $\sigma { } \mathrm { : }$ :

$$
X \stackrel {A} {\longrightarrow} _ {\mathcal {I}} Y \iff X = Y \mathrm{and} \mathcal {I}, X \models A
$$

$$
X \xrightarrow {A a \sigma} _ {\mathcal {I}} Y \iff \mathcal {I}, X \models A \text { and } \exists Z: X \xrightarrow {a} _ {\mathcal {I}} Z \text { and } Z \xrightarrow {\sigma} _ {\mathcal {I}} Y
$$

Proposition 4.1

$$
\text {(i)} \quad X \xrightarrow {\alpha} _ {\mathcal {I}} Y \iff \exists \sigma \in \mathcal {L} \alpha : X \xrightarrow {\sigma} _ {\mathcal {I}} Y
$$

$$
\text {(ii)} \mathcal {I}, X \models \langle \alpha \rangle s \iff \exists   \sigma \in \mathcal {L} \alpha   \exists Y: X \xrightarrow {\sigma} _ {\mathcal {I}} Y a n d \mathcal {I}, Y \models s
$$

$$
\text {(iii)} \mathcal {I}, X \models [ \alpha ] s \iff \forall \sigma \in \mathcal {L} \alpha \forall Y: X \xrightarrow {\sigma} _ {\mathcal {I}} Y i m p l i e s \mathcal {I}, Y \models s
$$

## 5 Regular DNF

We now describe the regular reasoner. The regular reasoner relies on the languagetheoretic semantics and ignores the propositional and modal aspects of the language.

A program is basic if it has the form aα, and normal if it is 1 or basic. Intuitively, a regular DNF of a program α is a decomposition of α into normal programs $\beta _ { 1 } , \ldots , \beta _ { n }$ such that $\alpha \equiv \beta _ { 1 } + \cdots + \beta _ { n }$ (or, more formally, $\mathcal { L } \alpha = \mathcal { L } \beta _ { 1 } \cup \cdot \cdot \cdot \cup \beta _ { n } )$ ). This simple intuition does not account for tests. The program $p ,$ for instance, cannot be represented by any set of normal programs. Hence formally we proceed as follows.

We use $\mathcal { F } \alpha$ to denote the set of all formulas that occur in α as subprograms. For instance, $\mathcal { F } ( a \neg p + b \langle a p \rangle q ) = \{ \neg p , \ \langle a p \rangle q \}$ . Formulas that occur as programs are called tests. Note that Fα does not include tests that occur in tests occurring in α.

Proposition 5.1 If $s \in { \mathcal { F } } \alpha$ , then, for every t, $| s | < | \neg s | < | \langle \alpha \rangle t | \leq | [ \alpha ] t |$

A guarded program is a pair Aα where A is a set of formulas and α is a program. A guarded program Aα is normal if α is normal. The language of a guarded program is ${ \mathcal { L } } ( A \alpha ) : = { \mathcal { L } } A \cdot { \mathcal { L } } \alpha$ . A regular DNF is a function D that maps every program α to a finite set Dα of normal guarded programs such that:

(i) $\mathcal { L } \alpha = \bigcup _ { B \beta \in \mathcal { D } \alpha } \mathcal { L } ( B \beta )$

(ii) If $B \beta \in \mathcal { D } \alpha$ , then $B \cup \mathcal { F } \beta \subseteq \mathcal { F } \alpha$

The regular reasoner computes a regular DNF. Kleene’s theorem (regular expressions translate into finite automata) [16] suggests that regular DNFs exist. We give a naive algorithm that computes a regular DNF. For space reasons we omit the correctness proof. The algorithm employs the following inference rules for guarded

programs.

$$
\begin{array}{c c c c c c} \frac {A a}{A a 1} & \frac {A s}{(A ; s) 1} & \frac {A s \beta}{(A ; s) \beta} & \frac {A 1 \beta}{A \beta} & \frac {A (\alpha_ {1} + \alpha_ {2})}{A \alpha_ {1} , A \alpha_ {2}} & \frac {A (\alpha_ {1} + \alpha_ {2}) \beta}{A \alpha_ {1} \beta , A \alpha_ {2} \beta} \\ & \frac {A (\alpha_ {1} \alpha_ {2}) \beta}{A \alpha_ {1} \alpha_ {2} \beta} & & \frac {A \alpha^ {*}}{A 1 , A \alpha \alpha^ {*}} & & \frac {A \alpha^ {*} \beta}{A \beta , A \alpha \alpha^ {*} \beta} \end{array}
$$

The notation $A ; s$ stands for the set $A \cup \{ s \}$ . Also, we write programs of the form $\alpha ( \beta \gamma )$ without parentheses as $\alpha \beta \gamma$ . Given a set G of guarded programs, we denote the closure of $G$ under the rules with $\mathcal { R } G .$ . One can show that RG describes the same language as $G ,$ , and that $\mathcal { R } G$ is finite if G is finite. If G is a set of guarded programs, we call a guarded program $A \alpha \in G$ minimal in G if there is no $B \alpha \in G$ such that $B \subsetneq A$ . We obtain a regular DNF D by taking for Dα all normal guarded programs in ${ \mathcal { R } } \{ \emptyset \alpha \}$ that are minimal in ${ \mathcal { R } } \{ \emptyset \alpha \}$

Example 5.2 Consider the program $( a + b ) ^ { * }$ . We have:

$$
\begin{array}{c} \mathcal {R} \{\emptyset (a + b) ^ {*} \} = \{\emptyset (a + b) ^ {*}, \emptyset 1, \emptyset (a + b) (a + b) ^ {*}, \emptyset a (a + b) ^ {*}, \emptyset b (a + b) ^ {*} \} \\ \mathcal {D} \{(a + b) ^ {*} \} = \{\emptyset 1, \emptyset a (a + b) ^ {*}, \emptyset b (a + b) ^ {*} \} \end{array}
$$

Example 5.3 Consider the program $( p + q ) ^ { * }$ where $p , \ q$ are predicates. We have ${ \mathcal { D } } \{ ( p + q ) ^ { * } \} = \{ \emptyset 1 \}$ . We profit from the optimization that only the minimal guarded programs are taken for the DNF. Otherwise ${ \mathcal { D } } \{ ( p + q ) ^ { * } \}$ would contain three further elements: $\{ p \} 1 , \{ q \} 1$ , and $\{ p , q \} 1$

While the above naive algorithm yields a regular DNF for every program $\alpha ,$ its eficiency in practice remains to be seen. For programs without tests (i.e., for regular expressions), eficient regular DNFs can be obtained via translation into deterministic finite automata [4]. We expect that similarly eficient regular DNFs also exist for programs with tests.

We fix some computable regular DNF D for the rest of the paper.

Proposition 5.4

$$
\text {(i)} \quad \mathcal {I}, X \models \langle \alpha \rangle s \iff \exists B \beta \in \mathcal {D} \alpha : \mathcal {I}, X \models B; \langle \beta \rangle s
$$

$$
\text {(ii)} \quad \mathcal {I}, X \models [ \alpha ] s \iff \forall B \beta \in \mathcal {D} \alpha : (\exists t \in B: \mathcal {I}, X \models \neg t) o r \mathcal {I}, X \models [ \beta ] s
$$

Proof. Follows with Proposition 4.1.

## 6 Propositional DNF

The propositional reasoner relies on a support relation from clauses to formulas that abstracts from most modal aspects of the language. We define the support relation $C \triangleright s$ by recursion on s.

$$
C \triangleright s \iff s \in C \quad \text { if } s \text { is   a   literal }
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$C\triangleright\neg\neg s\iff C\triangleright s$ $C\triangleright s\wedge t\iff C\triangleright s$ and $C\triangleright t$ $C\triangleright s\vee t\iff C\triangleright s$ or $C\triangleright t$ $C\triangleright \langle 1\rangle s\iff C\triangleright s$ $C\triangleright [1]s\iff C\triangleright s$ $C\triangleright \langle \alpha \rangle s\iff \exists B\beta \in \mathcal{D}\alpha \colon (\forall t\in B:C\triangleright t)$ and $C\triangleright \langle \beta \rangle s$ if $\alpha$ not normal  
$C\triangleright [\alpha ]s\iff \forall B\beta \in \mathcal{D}\alpha \colon (\exists t\in B:C\triangleright\neg t)$ or $C\triangleright [\beta ]s$ if $\alpha$ not normal
</div>

The last two equivalences of the definition employ the regular DNF D fixed above. The recursion terminates since either the size of the formula is reduced (verify with Proposition 5.1) or the recursion is on a formula βs or $[ \beta ] s$ where $\beta$ is normal and s is unchanged. We say C supports s if $C \triangleright s$ . We write C  A and say C supports A if $C \triangleright s$ for every $s \in A$ . Note that $C \triangleright D \iff D \subseteq C$ (recall that $C$ and $D$ denote clauses).

Proposition 6.1 $I f C \triangleright A$ and $C \subseteq D$ and $B \subseteq A$ , then $D \triangleright B$

Proposition 6.2 $I f { \cal Z } , X \models C$ and $C \triangleright A$ , then I, $X \models A$

Proof. Follows with Proposition 5.4.

We define propositional DNFs as functions that, applied to a formula set $A ,$ yield a DNF (in the traditional sense) of the conjunction of the formulas in A, represented as a set of clauses. In other words, we require that a propositional DNF D applied to a set A satisfies the equivalence $\textstyle \bigwedge _ { s \in A } s \equiv \bigvee _ { C \in { \mathcal { D } } A } \bigwedge _ { t \in C } t .$

Formally, a propositional DNF is a function D that maps every finite set A of formulas to a finite set of clauses such that:

(i) $\mathcal { T } , X \models A \iff \exists D \in \mathcal { D } A \colon \mathcal { T } , X \models D .$

(ii) $C \triangleright A \iff \exists D \in { \mathcal { D } } A \colon D \subseteq C .$

Property (ii) for propositional DNFs immediately implies the following proposition.

Proposition 6.3 $I f C \in { \mathcal { D } } A$ , then $C \triangleright A$

In the following, we will often use Proposition 6.3 implicitly.

For the termination of the modal reasoner the propositional DNF must have some additional finiteness property. We need a few preparatory definitions. The variants of a program α are the basic programs $\beta$ such that $B \beta \in \mathcal { D } \alpha$ for some $B .$ A base is a set $U$ of basic formulas such that $\langle \beta \rangle s \in U$ whenever $\langle a \alpha \rangle s \in U$ and $\beta$ is a variant of α. A base $U$ supports a formula s if the following conditions are satisfied:

(i) U contains every basic formula that occurs in s.

(ii) If $\langle \alpha \rangle t$ occurs in s, α is not basic, and $\beta$ is a variant of $\alpha _ { ; }$ , then $\langle \beta \rangle t \in U$

A base supports a set of formulas A if it supports every formula $s \in A$

Proposition 6.4 Every finite set of formulas is supported by a finite base.

Proof. Follows from property (ii) for the underlying regular DNF.

A propositional DNF D is finitary if for every finite set of formulas A and every base U supporting A and every clause $C \in { \mathcal { D } } A$ it holds that U supports $C$

Proposition 6.5 There is a computable finitary propositional DNF.

Proof. The definition of the support relation can be seen as a tableau-style decomposition procedure for formulas. Using this procedure, one develops A into a complete tableau. The literals of each open branch yield a clause. All clauses obtained this way constitute a DNF of A.

The direction $^ { 6 6 } { \mathfrak { L } } ( = ^ { 5 }$ of property (i) for propositional DNFs follows with Proposition 6.2. That the DNF is finitary follows from the fact that the decomposition does not introduce new formulas except for diamond formulas obtained with the finitary regular DNF. ✷

Example 6.6 Take the regular DNF given in $\ S 5$ and the propositional DNF given in the proof of Proposition 6.5. We have:

$$
\begin{array}{r c l} \mathcal {D} \{\langle b ^ {*} \rangle p \} & = & \{\{p \}, \{\langle b b ^ {*} \rangle p \} \} \\ \mathcal {D} \{\langle b ^ {*} \rangle p, [ b ^ {*} ] (q \land \neg p) \} & = & \{\{\langle b b ^ {*} \rangle p, q, \neg p, [ b b ^ {*} ] (q \land \neg p) \} \} \\ \mathcal {D} \{\langle a ^ {*} \rangle p, [ a ^ {*} ] \neg p \} & = & \emptyset \\ \mathcal {D} \{\langle (a + b) ^ {*} \rangle p \} & = & \{\{p \}, \{\langle a (a + b) ^ {*} \rangle p \}, \{\langle b (a + b) ^ {*} \rangle p \} \} \end{array}
$$

For the third example note that $[ a ^ { * } ] \neg p$ is the complement of $\langle a ^ { * } \rangle p .$

We fix some computable and finitary propositional DNF D for the rest of the paper.

## 7 Diamond Expansion and Nominal Propagation

We now return to the modal reasoner, which was first explained in $\ S 3$ . The modal reasoner builds a tableau where each branch contains clauses and links. The goal consists in constructing a branch where every claim is realized with a link and some further conditions are satisfied. We first make precise how the modal reasoner derives new clauses.

An expansion of a claim $C ^ { \langle a \alpha \rangle s }$ is a claim $D \langle \beta \rangle s$ such that $B \beta \ \in \ D \alpha$ and $D \in { \mathcal { D } } ( B ; \langle \beta \rangle s \cup { \mathcal { R } } _ { a } C )$ for some B. The following proposition formulates an important property of expansions (the proposition will not be needed later).

Proposition 7.1 Let $C ^ { s }$ be a claim such that $s \in C$ and let $\mathcal { T }$ satisfy C. Then there exists an expansion $D ^ { t }$ of $C ^ { s }$ such that I satisfies D.

A link is a pair $C ^ { s } D ^ { t }$ of two claims such that $s \in C$ and there is an expansion $E ^ { t }$ of $C ^ { s }$ such that $E \subseteq D$ . A quasi-branch is a finite set Γ of clauses and links such that $\{ C , D \} \subseteq \Gamma$ whenever $C ^ { s } D ^ { t } \in \Gamma$ . A quasi-branch Γ realizes a claim $C ^ { s }$ if Γ contains some link $C ^ { s } D ^ { t }$ . A base supports a quasi-branch Γ if it supports every clause of Γ. An interpretation I satisfies a quasi-branch Γ (or is a model of Γ) if I satisfies every clause in Γ.

We call a clause nominal if it contains a nominal. Let Γ be a quasi-branch and A be a set of formulas. We realize nominal propagation with the notation

$$
A ^ {\Gamma} := A \cup \{s \mid \exists x \in A \exists C \in \Gamma : x \in C \land s \in C \}
$$

Note that $A ^ { \Gamma }$ is the least set of formulas that contains A and all clauses $C \in \Gamma$ that have a nominal in common with A. Thus $( A ^ { \Gamma } ) ^ { \Gamma } = A ^ { \Gamma }$ . Moreover, $A ^ { \Gamma } = A$ if A contains no nominal.

Proposition 7.2 If an interpretation satisfies Γ and C, it satisfies $C ^ { \Gamma }$

Proposition 7.3 Let U be a base that supports a quasi-branch Γ, $C ^ { s }$ be a claim such that $s \in C \in \Gamma$ , and $D ^ { t }$ be an expansion of $C ^ { s }$ . Then U supports $D ^ { \Gamma }$

## 8 Branches and Expansion Rule

A quasi-branch that realizes all its claims does not necessarily have a model. To guarantee the existence of a model, we impose certain conditions on quasi-branches that act as invariants of the modal reasoner. One of the conditions is loop freeness.

Example 8.1 Consider the clause $C = \{ \langle a a ^ { * } \rangle { \neg p } , \ p , q , \ [ a a ^ { * } ] ( p \wedge q ) \}$ . Note that C is unsatisfiable, and that $\{ C , \ C ^ { \langle a a ^ { * } \rangle \neg p } C ^ { \langle a a ^ { * } \rangle \neg p } \}$ is a quasi-branch that realizes every claim. The link of this quasi-branch describes a loop.

A path in a quasi-branch Γ is a sequence $C _ { 1 } { } ^ { s _ { 1 } } \ldots C _ { n } { } ^ { s _ { n } }$ of claims such that:

(i) $\forall i \in [ 1 , n ] \colon C _ { i } ^ { \Gamma } = C _ { i }$

(ii) $\forall i \in [ 1 , n - 1 ] \ \exists D \colon \ C _ { i } { } ^ { s _ { i } } D ^ { s _ { i + 1 } } \in \Gamma \ \mathrm { a n d } \ D ^ { \Gamma } = C _ { i + 1 }$

A loop in a quasi-branch Γ is a path $C _ { 1 } { } ^ { s _ { 1 } } \ldots C _ { n } { } ^ { s _ { n } }$ in Γ such that $n \geq 2$ and $C _ { n } { } ^ { s _ { n } } = C _ { 1 } { } ^ { s _ { 1 } }$ . A branch is a quasi-branch Γ that satisfies the following conditions:

• Functionality: If $C ^ { s } D ^ { t } \in \Gamma$ and $C ^ { s } E ^ { u } \in \Gamma$ , then $D ^ { t } = E ^ { u }$

• Loop-freeness: There is no loop in Γ.

• Nominal coherence: If $C \in \Gamma$ , then $C ^ { \Gamma } \in \Gamma$

The core of a branch Γ is CΓ $: = \{ C \in \Gamma \mid C ^ { \Gamma } = C \}$ . A branch Γ is evident if Γ realizes $C ^ { \langle \alpha \rangle s }$ for all $\langle \alpha \rangle s \in C \in { \mathcal { C } } \Gamma$ . We will show that every evident branch has a model. The modal reasoner works on branches and applies the following expansion rule:

Expansion Rule

If $\langle \alpha \rangle s \in C \in { \mathcal { C } } \Gamma$ and Γ does not realize $C ^ { \langle \alpha \rangle s }$ •

then expand Γ to all branches $\Gamma ; D ^ { \Gamma } ; C ^ { \langle \alpha \rangle s } ( D ^ { \Gamma } ) ^ { t }$

such that $D ^ { t }$ is an expansion of $C ^ { \langle \alpha \rangle s }$ and $D ^ { \Gamma }$ is a clause.

Note that a single clause always yields a branch. So the modal reasoner can start with any clause.

Proposition 8.2 The modal reasoner terminates on every branch.

Proof. Since branches are finite by definition, we know by Proposition 6.4 that the initial branch is supported by a finite base. By Proposition 7.3 we know that the expansion rule only adds clauses that are supported by the initial base. The claim follows since a finite base can only support finitely many clauses. ✷

Given termination, the correctness of the modal reasoner can be established by showing two properties:

(i) Model Existence: Every evident branch has a model.

(ii) Soundness: Every satisfiable clause can be developed into an evident branch.

## 9 Model Existence

Proposition 9.1 Let Γ be an evident branch and $\langle \alpha \rangle s \in C \in { \mathcal { C } } \Gamma$ . Then there exists a unique path $C ^ { \langle \alpha \rangle s } \ldots D ^ { \langle 1 \rangle s }$ in Γ.

Proof. The path exists since Γ is loop-free and realizes every claim with a clause in CΓ. The path is unique since Γ is functional. ✷

Lemma 9.2 $I f X { \xrightarrow { a } } \chi Y$ and I, $Y \models B ; \langle \beta \rangle s$ and $B \beta \in \mathcal { D } \alpha$ , then I, $X \models \langle a \alpha \rangle s$

Proof. Follows with Propositions 4.1 and 5.4.

The model existence proof requires a somewhat involved induction, which we realize with the following lemma.

Lemma 9.3 Let Γ be an evident branch and I be an interpretation such that:

$| \mathcal { T } | = \mathcal { C } \Gamma$

$C \ { \stackrel { a } { \to } } _ { \mathcal { T } } D \iff \exists \alpha , s , t , E \colon \ C ^ { \langle a \alpha \rangle s } E ^ { t } \in \Gamma$ and $D = E ^ { \Gamma }$ for all actions a

$C \in { \mathcal { I } } p \iff p \in C$ for all predicates p

${ \mathcal { T } } x = C \iff x \in C$ for all nominals x that occur in Γ

Let $| \mathcal { F } \alpha | : = \operatorname* { m a x } \{ | s | | s \in \mathcal { F } \alpha \}$ . Then for all $n \in \mathbb { N }$

(i) For every path $C ^ { \langle \alpha \rangle s } \ldots D ^ { \langle 1 \rangle s }$ in Γ such that $| { \mathcal { F } } \alpha | , | s | < n$

$$
\mathcal {I}, C \models \langle \alpha \rangle s.
$$

(ii) For all $C , D , \sigma , \alpha ,$ , s such that $| { \mathcal { F } } \alpha | , | s | < n - 1$

$\begin{array} { r } { I f C \triangleright [ \alpha ] s , \sigma \in \mathcal L \alpha _ { ; } } \end{array}$ , and $C \stackrel { \sigma } { \longrightarrow } \tau D$ , then $D \triangleright s$

(iii) For all C, s such that $C \in { \mathcal { C } } \Gamma$ and $| s | = n .$

If C  s, then ${ \mathcal { T } } , C \models s$

Proof. By induction on n. See [11] for details.

Theorem 9.4 (Model Existence) Every evident branch has a finite model.

Proof. Follows with Lemma 9.3 (iii). See [11] for details.

## 10 Soundness

We have now arrived at the crucial part of the correctness proof. Ideally, we would like to show that a satisfiable branch with an unrealized claim can always be expanded. However, this is not true.

Example 10.1 Consider the following branch where $s : = [ a a ^ { * } ] ( q \vee [ a ] \neg p )$

$$
\begin{array}{c c c} \langle a a ^ {*} \rangle p, \neg p, q, s & \langle a a ^ {*} \rangle p, [ a ] \neg p, s & \langle a a ^ {*} \rangle p, \neg p, [ a ] \neg p, s \end{array}
$$

The branch is satisfiable. Still it is impossible to realize the claim for the third clause since each of the two possible expansions introduces a loop.

Following [10], we solve the problem with the notion of a straight model. A straight model requires that all links on the branch make progress towards the fulfillment of the diamond literal they serve. Every satisfiable initial branch has a straight model, and every unrealized claim on a branch with a straight model I can be expanded such that I is a straight model of the expanded branch.

Let I be an interpretation and A be a set of formulas. The depth of A and $\langle \alpha \rangle s$ in I is defined as

$$
\begin{array}{c} \delta_ {\mathcal {I}} A (\langle \alpha \rangle s) := \min \{| \sigma | \mid \sigma \in \mathcal {L} \alpha \text { and } \\ \exists X, Y \in | \mathcal {I} |: \mathcal {I}, X \models A \text { and } X \xrightarrow {\sigma} _ {\mathcal {I}} Y \text { and } \mathcal {I}, Y \models s \} \end{array}
$$

where min $\varnothing = \infty$ and $n < \infty$ for all $n \in \mathbb { N }$

Proposition 10.2 $\delta _ { \mathcal { T } } A s < \infty$ if I satisfies A ; s.

Proof. Follows with Proposition 4.1.

In particular, we have $\delta _ { \mathcal { T } } C s < \infty$ for every $s \in C \in \Gamma \ \mathrm { i f } \ \mathcal { T }$ is a model of Γ.

A link $C ^ { s } D ^ { t }$ is straight for an interpretation I if $\delta _ { \ T } C s \ > \ \delta _ { \ T } D t$ whenever $\delta _ { \mathcal { T } } C s > 0$ . A straight model of a quasi-branch Γ is a model of Γ such that every link $C ^ { s } D ^ { t } \in \Gamma$ is straight for I.

Proposition 10.3 Let I be a model of a quasi-branch Γ. Then $\delta _ { \mathcal { T } } A s = \delta _ { \mathcal { T } } A ^ { \Gamma } s$

Lemma 10.4 (Straightness) A quasi-branch that has a straight model contains no loops.

Proof. By contradiction. Let I be a straight model of a quasi-branch Γ and $\boldsymbol { C _ { 1 } } ^ { s _ { 1 } } \ldots \boldsymbol { C _ { n } } ^ { s _ { n } }$ be a loop in Γ. Then $n \ \geq \ 2$ and $C _ { 1 } { } ^ { s _ { 1 } } \ = \ C _ { n } { } ^ { s _ { n } }$ . It sufices to show that $\delta _ { \mathcal { T } } C _ { i } s _ { i } > \delta _ { \mathcal { T } } C _ { i + 1 } s _ { i + 1 }$ for all $i \in [ 1 , n - 1 ]$ . Let $i \in [ 1 , n - 1 ]$ Then $s _ { i } = \langle a \alpha \rangle t , C _ { i } ^ { \mathrm { ~ } s _ { i } } D ^ { s _ { i + 1 } } \in \Gamma$ , and $D ^ { \Gamma } = C _ { i + 1 }$ for some a, α, t, and D. Since every $\sigma \in \mathcal { L } ( a \alpha )$ contains the action a, we have $\delta _ { \ Z } C _ { i } s _ { i } > 0$ . Since $C _ { i } { } ^ { s _ { i } } D ^ { s _ { i + 1 } }$ is straight for $\mathcal { T } , \ \delta _ { \mathcal { T } } C _ { i } s _ { i } > \delta _ { \mathcal { T } } D s _ { i + 1 }$ . Hence $\delta _ { \mathcal { T } } C _ { i } s _ { i } > \delta _ { \mathcal { T } } C _ { i + 1 } s _ { i + 1 }$ by Proposition 10.3 since $D ^ { \Gamma } = C _ { i + 1 }$ ✷

Theorem 10.5 (Soundness) Let I be a straight model of a branch Γ and let $\langle \alpha \rangle s \in C \in \Gamma$ such that Γ does not realize $C ^ { \langle \alpha \rangle s }$ . Then there is an expansion $D ^ { t }$ of $C ^ { \langle \alpha \rangle s }$ such that $\Gamma ; D ^ { \Gamma } ; C ^ { \langle \alpha \rangle s } ( D ^ { \Gamma } ) ^ { t }$ is a branch and I is a straight model of $\bar { \Gamma } ; D ^ { \Gamma } ; C ^ { \langle \alpha \rangle s } ( D ^ { \Gamma } ) ^ { t }$

Proof. Since I satisfies C, by Proposition 10.2, there is some $\sigma \in { \mathcal { L } } \alpha$ and $X , Y \in | \mathcal { I } |$ be such that $| \sigma | = \delta _ { \mathcal { T } } C ( \langle \alpha \rangle s )$ and $\pi , X \models C$ and $X \stackrel { \sigma } { \longrightarrow } \tau Y$ and ${ \mathcal { T } } , Y \models s$ . Since $\langle \alpha \rangle s$ is a literal, $\alpha = a \beta$ and $\sigma = A a \tau$ for some $a , \beta , A$ , and $\tau \in \mathcal { L } \beta$ . Let $Z \in | { \mathcal { I } } |$ be such that $X \xrightarrow { a } _ {  \underline { { { Z } } } } Z$ and $Z \stackrel { \tau } { \longrightarrow } \tau Y$ . Let $B \gamma \in { \mathcal { D } } \beta$ such that $\tau \in \mathcal { L } ( B \gamma )$ ). Then ${ \mathcal { T } } , Z \models B$ and $\mathcal { I } , Z \models \langle \gamma \rangle s$ by Proposition 4.1 (ii). Moreover, ${ \mathcal { T } } , Z \models { \mathcal { R } } _ { a } C$ . Thus, by property (i) for propositional DNFs, there is some $D \in { \mathcal { D } } ( B ; \langle \gamma \rangle s \cup { \mathcal { R } } _ { a } C )$ such that ${ \cal T } , { \cal Z } \models D$ . Clearly, $D ^ { \langle \gamma \rangle s }$ is an expansion of $C ^ { \langle \alpha \rangle s }$ and, since $\tau \in { \mathcal { L } } ( B \gamma )$ $\delta _ { \mathcal { T } } D ( \langle \gamma \rangle s ) \leq | \tau | = | \sigma | - 1 < \delta _ { \mathcal { T } } C ( \langle \alpha \rangle s )$ . Then, by Proposition 10.3, $\delta _ { \mathcal { T } } D ^ { \Gamma } ( \langle \gamma \rangle s ) <$ $\delta _ { \mathcal { T } } C ( \langle \alpha \rangle s )$ Therefore, I is a straight model of $\Gamma ; D ^ { \Gamma } ; C ^ { \langle \alpha \rangle s } ( D ^ { \Gamma } ) ^ { \langle \gamma \rangle s }$ . Moreover, $\Gamma ; D ^ { \Gamma } ; C ^ { \langle \alpha \rangle s } ( D ^ { \Gamma } ) ^ { \langle \gamma \rangle s }$ satisfies the nominal coherence and functionality conditions.<sup>✷</sup>

## 11 Final Remarks

The main innovation of the present paper over our previous paper [10] is the notion of a finitary regular DNF. This makes it possible to cover all PDL programs and still have transparent correctness proofs.

It is straightforward to extend the clausal tableau method for HPDL to satisfaction formulas $@ _ { x } s$ . To deal with such formulas, one adds an additional expansion rule at the modal level as presented in [10]. Also, the optimizations for the modal level of clausal tableaux discussed in [10] carry over to HPDL.

It can be seen by a straightforward analysis that the decision procedure utilizing the naive regular reasoner presented in $\ S 5$ and the tableau-based propositional reasoner sketched in Proposition 6.5 runs in NEXPTIME.

We expect that the clausal method can be extended to diference modalities. Less clear is the possibility of extending the method to converse modalities. As recently shown by Gor´e and Widmann [8], converse modalities can be eficiently dealt with by Pratt-style decision procedures. Their treatment of converse, however, does not seem to carry over to our approach. On the other hand, Pratt-style procedures do not seem compatible with nominals (see [10,19]). Hence, developing a gracefully degrading decision procedure for a logic featuring eventualities, nominals, and converse modalities at the same time remains a challenging open problem.

## Acknowledgment

We would like to thank a referee for valuable remarks that helped to improve the paper.

## References

[1] Abate, P., R. Gor´e and F. Widmann, An on-the-fly tableau-based decision procedure for PDLsatisfiability, in: C. Areces and S. Demri, editors, Proc. 5th Workshop on Methods for Modalities (M4M-5), Electr. Notes Theor. Comput. Sci. <sup>231</sup> (2009), pp. 191–209.

[2] Areces, C. and B. ten Cate, Hybrid logics, in: P. Blackburn, J. van Benthem and F. Wolter, editors, Handbook of Modal Logic, Studies in Logic and Practical Reasoning <sup>3</sup>, Elsevier, 2007 pp. 821–868.

[3] Baader, F., Augmenting concept languages by transitive closure of roles: An alternative to terminological cycles, Technical Report RR-90-13, DFKI (1990).

[4] Berry, G. and R. Sethi, From regular expressions to deterministic automata, Theor. Comput. Sci. <sup>48</sup> (1986), pp. 117–126.

[5] De Giacomo, G. and F. Massacci, Combining deduction and model checking into tableaux and algorithms for converse-PDL, Inf. Comput. <sup>162</sup> (2000), pp. 117–137.

[6] Fischer, M. J. and R. E. Ladner, Propositional dynamic logic of regular programs, J. Comput. System Sci. (1979), pp. 194–211.

[7] Gor´e, R. and F. Widmann, An optimal on-the-fly tableau-based decision procedure for PDLsatisfiability, in: R. A. Schmidt, editor, CADE 2009, LNCS <sup>5663</sup> (2009), pp. 437–452.

[8] Gor´e, R. and F. Widmann, Optimal tableaux for propositional dynamic logic with converse, in: J. Gies and R. H¨ahnle, editors, IJCAR 2010, LNCS <sup>6173</sup> (2010), pp. 225–239.

[9] Harel, D., D. Kozen and J. Tiuryn, “Dynamic Logic,” The MIT Press, 2000.

[10] Kaminski, M. and G. Smolka, Terminating tableaux for hybrid logic with eventualities, in: J. Giesl and R. H¨ahnle, editors, IJCAR 2010, LNCS <sup>6173</sup> (2010), pp. 240–254.

[11] Kaminski, M. and G. Smolka, Clausal tableaux for hybrid PDL, Technical report, Saarland Universit <sub>(2011). URL</sub> www.ps.uni-saarland.de/Publications/details/KaminskiSmolka:2011:HPDL.html

[12] Kozen, D. and F. Smith, Kleene algebra with tests: Completeness and decidability, in: D. van Dalen and M. Bezem, editors, CSL’96, LNCS <sup>1258</sup> (1996), pp. 244–259.

[13] Kozen, D. and J. Tiuryn, Logics of programs, in: Handbook of Theoretical Computer Science, Volume B: Formal Models and Sematics, Elsevier, 1990 pp. 789–840.

[14] Passy, S. and T. Tinchev, PDL with data constants, Inf. Process. Lett. <sup>20</sup> (1985), pp. 35–41.

[15] Passy, S. and T. Tinchev, An essay in combinatory dynamic logic, Inf. Comput. <sup>93</sup> (1991), pp. 263–332.

[16] Perrin, D., Finite automata, in: Handbook of Theoretical Computer Science, Volume B: Formal Models and Sematics, Elsevier, 1990 pp. 1–57.

[17] Pratt, V. R., A near-optimal method for reasoning about action, J. Comput. System Sci. <sup>20</sup> (1980), pp. 231–254.

[18] Sattler, U. and M. Y. Vardi, The hybrid μ-calculus, in: R. Gor´e, A. Leitsch and T. Nipkow, editors, IJCAR 2001, LNCS <sup>2083</sup> (2001), pp. 76–91.

[19] Widmann, F., “Tableaux-based Decision Procedures for Fixed Point Logics,” Ph.D. thesis, Australian National University (2010).
