---
otero_id: 21563
otero_key: "X5D4GNM5"
title: "Defeasible logic graphs"
authors: "Donald Nute; Katrin Erk"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00063-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Defeasible logic graphs I. Theory <sup>1</sup>

Donald Nute <sup>a,)</sup>, Katrin Erk <sup>b</sup>

<sup>a</sup> Department of Philosophy and Artificial Intelligence Center, The UniÕersity of Georgia, Athens, GA 30602, USA <sup>b</sup> Department of Computer Science, UniÕersity of Koblenz-Landau, Koblenz, Germany

## Abstract

We propose development of an argument-based decision support system utilizing defeasible or nonmonotonic reasoning. Defeasible logic graphs d-graphs represent the knowledge contained in a defeasible theory. A method for propagating Ž . labels through a d-graph is developed as a means for reasoning about the theory from which the d-graph is generated. This method is proven to be sound with respect to Nute’s defeasible logic and complete for finite, consistent theories with acyclic d-graphs. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Nonmonotonic logic; Defeasible logic; Decision support systems

## 1. Defeasible reasoning for decision support

Knowledge-based systems KBS that model in-Ž . ference about specific domains incorporate representations of the knowledge necessary to solve problems in their domains. We believe that another kind of decision support tool is needed, one that allows users to model knowledge not already represented in the system. Such an argumentation-based system ABSŽ . would provide tools to help the user represent knowledge about any domain. It would incorporate an inference mechanism to help the user derive conclusions from the knowledge that has been mod eled. The system would make the inference process visible to the user and allow the user to construct a variety of ‘what–if’ scenarios easily and quickly. While a KBS applies preselected argument structures to the information provided by the user, an ABS would allow the user to construct and evaluate competing arguments on any subject before making a decision. Systems of this sort have been reported in <sup>w</sup> <sup>x</sup> <sup>2</sup> Ref. 2 .

An ABS inference mechanism should support reasoning in uncertain domains and reasoning with incomplete information. Many KBS use certainty factors, probabilities, fuzzy logic, or other essentially quantitative methods for this kind of reasoning. Finding useful numbers for such systems is a major part of the knowledge acquisition process. An ABS should incorporate a qualitatiÕe approach to the representation of uncertain or incomplete information, one that does not require the user to assign numbers to pieces of knowledge. The inference scheme must be reasonably simple and intuitive. Fortunately, recent AI research provides formalisms for defeasible reasoning in which a line of argument can be defeated by another line of argument 1,3,4,7,8,13,16,20,21 .Ž<sup>w</sup> <sup>x</sup>. Defeasible formalisms directly model the ways in which arguments can rebut or undercut each other. These systems represent the pieces from which arguments are constructed as rules having no numerical component.

This is the first of two papers presenting the theory and implementation of an ABS incorporating defeasible reasoning. In this paper, we will describe a visually oriented knowledge representation system and a defeasible inference mechanism that lends itself to implementation as an ABS. Knowledge is represented in a defeasible logic graph d-graph . AŽ . node in a d-graph represents the premise or conclusion of a rule. The arcs in a d-graph are arrows, and different kinds of arrows indicate different roles a rule can play in an argument. We reason with a d-graph by propagating the markers <sup>q</sup>, <sup>y</sup>, and ? through the graph to mark which of the premises or conclusions are true, false, or impossible to establish from available information. The system of defeasible logic graphs is based on the family of defeasible logics developed in Ref. 13 . We will establish a<sup>w</sup> <sup>x</sup> series of results that explain how the formal proof theory serves as a semantics for the defeasible logic graph system.

The companion to this paper 19 describes a <sup>w</sup> <sup>x</sup> prototype ABS, d-GRAPHER, that helps a user construct defeasible logic graphs. d-GRAPHER implements the graph-marking algorithm described in this paper. All figures in this paper showing examples of defeasible logic graphs are copies of d-GRAPHER screens.

## 2. The language

It is well-known that first-order logic FOL isŽ . semi-decidable. There are algorithms that can detect when a formula p is derivable from a FOL theory T, but there is no algorithm that can always detect when a formula $p$ is not derivable from a FOL theory T. Much of the research in logic programming has involved development of fully-decidable subsets of FOL such as Horn-clause logic without functions.

The problem is even more extreme when we consider defeasible extensions of FOL. All defeasible or nonmonotonic formalisms depend upon defeasible rules or defaults. Suppose we use rules of the form $p \Rightarrow q$ which we read as ‘If $p ,$ then evidently $q ^ { , }$ . Before we can detach $q ,$ we need minimally to establish that $p$ is derivable and that $\sim { q }$ is not derivable. But for FOL, we have no effective way to determine that <sup>;</sup>q is not derivable from a given theory. We can write a program that will list the theorems of $T$ Žsince this set is recursively enumerable, but this is not possible for the non-theorems. . As a result, any extension of FOL depending on such rules is necessarily not even semi-decidable. Ginsberg states the problem succinctly when he writes, ‘‘The difficulty in developing such an implementation is that none of the formal descriptions provides a constructive definition of a valid nonmonotonic derivation’’ 5 , p. 72 . We will develop a defeasibleŽ<sup>w</sup> <sup>x</sup> . formalism that provides a constructive definition of a valid nonmonotonic derivation. This formalism extends a fragment of FOL. In Ref. 15 , Nute showed<sup>w</sup> <sup>x</sup> that a version of the formalism presented there is decidable. The same method can be used to show that the formalism presented here is also decidable.

We restrict ourselves to a language containing only atomic formulas, their negations, and simple rules made up of these. What can be shown is that when proofs are restricted to ground instances of the rules of such theories that is, to formulas containingŽ no variables and when the original theories are. finite and contain no function symbols, then there is an effective procedure for determining whether a ground formula is derivable from a theory. These are significant restrictions on the language, the class of theories, and the proof mechanism for our defeasible formalism, but we shall see that the resulting system is nevertheless powerful enough to represent a wide range of problems. We define atomic formulas in the usual way as an n-ary predicate symbol combined with n many terms. All terms in the language are either variables or constants. A literal is any atomic formula or its negation. Where p is an atomic formula, we say p and $\sim p$ are the complements of each other. $\lnot p$ denotes the complement of any literal $p ,$ positive or negative.

Rules are a class of expressions distinct from formulas. Rules are constructed using three primitive symbols: $ , \implies$ , and \. Where $A \cup \{ p \}$ is a set of formulas, $A  p$ is a strict rule, $A \Rightarrow p$ is a defeasible rule, and $A  p$ is an undercutting defeater. In each case, we call A the antecedent of the rule and we call $p$ the consequent of the rule. Where $A = \{ q \}$ , we denote $A  p$ as $q \to p ,$ and similarly for defeasible rules and undercutting defeaters. Antecedents for strict rules and undercutting defeaters must be non-empty; antecedents for defeasible rules may be empty. We will call a rule of the form $\scriptstyle { \mathcal { D } } \Rightarrow p \ { \mathrm { ~ a ~ } }$ presumption and represent it more simply ${ \mathrm { a s } } \ \Rightarrow p .$ All rules are read as ${ \cdot } _ { \mathrm { i f - t h e n } } ,$ statements. We read $A  p$ as ‘If A, then definitely $p ^ { \prime } , A \Rightarrow p$ as ‘If A, then evidently normally, typically, pre-Ž sumably. $p ^ { \prime } , \Rightarrow p$ as ‘Presumably, $p '$ , and $A  p$ as ‘If A, then it might be that $p '$ . The role of an undercutting defeater is only to interfere with the process of drawing an inference from a defeasible rule. Undercutting defeaters never support inferences directly, although they may support inferences indirectly by interfering with an argument that would otherwise defeat an inference. If free variables occur in a rule, we interpret the rule as though all variables were bound by universal quantifiers that have the entire rule within their scope. ${ \mathrm { S o } } ,$ for example, we read $F x \Rightarrow G x { \mathrm { ~ a s ~ } } ^ { * } F ^ { \prime } s$ are typically $G ' { \mathrm { s } } '$

Rules themselves are conceived as policies for forming and revising beliefs. A typical example of a defeasible rule in English is ‘Birds fly’. We might accept this rule because most birds do fly. We might even call the English sentence true for this reason. But as a rule, we interpret the sentence to mean something like ‘Take a thing’s being a bird as evidence that it flies’. This is an imperative and does not have a truth value. We understand a rule, not by knowing what would make it true or false, but by knowing what would be involved in complying with it. So defeasible rules have compliance conditions rather than truth conditions. We expect that any suitable semantics for defeasible logic will be procedural and will derive directly from proof theory. For further discussion, see Ref. 14 .<sup>w</sup> <sup>x</sup>

## 3. Defeasible logic

Definition 1: A defeasible theory is a set of literals and rules.

The literals in a defeasible theory represent initial assumptions in the theory that are never questioned or defeated. We only apply a defeasible rule when we think that it is not defeated. As noted earlier, we sometimes need to show that something is not derivable from available information in order to apply a defeasible rule. For example, we know that birds typically fly and penguins do not. We should not use the first of these rules to infer that a particular bird flies when we have evidence that the bird is a penguin. To demonstrate that flight evidently follows from what information we have about a particular bird, we need to demonstrate that available information will not support the conclusion that the bird is a penguin.

We write $T \vdash p$ to indicate that p is derivable from T using only the strict rules in T. We write $T \gets p$ to indicate that the derivation of $p$ from T may require the use of defeasible rules in T. We use $T  p$ to indicate that demonstrably, $p$ is not derivable from $T$ using only the strict rules in T. And we use $T \gets p$ to indicate that demonstrably, p is not derivable from T using both the strict and defeasible rules in T. Read $T \vdash p$ as T proÕes $p , T  p$ as T supports $p , T \to p$ as T will not proÕe p, and $T \to p$ as T will not support p. Note that $T \to p$ is quite different from T not $- \vdash p ( p$ is not strictly deriÕable from $T )$ , and $T \to p$ is quite different from $T \mathrm { n o t } \cdot  p ( p $ is not defeasibly deriÕable from $T )$ . Just because a conclusion is not derivable does not mean that we can demonstrate that it is not derivable.

To define a defeasible logic , we must specify when a defeasible theory T proves, will not prove, supports, or will not support a literal p in . We do this by identifying with a set of inference rules defining $\vdash , \lnot , $ , and <sup>x</sup>.

Definition 2: Where $\Sigma$ is a set of rules defining $\vdash$ $\dashv $ , and <sup>x</sup> , T is a defeasible theory, and p is a literal, $T \vdash _ { \Sigma } p$ iff we can show $T \vdash p$ using finitely many applications of the rules in . We define $T \mathsf { \ - l _ { \nabla \Sigma } } \mathsf { p } , T \mathsf { \ - e } _ { \Sigma } p ,$ and $T \to _ { \Sigma } p$ similarly. Where A is a set of literals, $T \vdash _ { \Sigma } A$ iff $T \vdash _ { \Sigma } p$ for all $p \in A ,$ $T \dashv { i } _ { \Sigma } A \ i f f T \to _ { \Sigma } p f o r$ some $p \in A$ , and similarly for $T  { _ { \Sigma } A }$ and $T \to _ { \Sigma } A$

Not just any set of rules for $\vdash , \ \ l \right. \left.$ , and <sup>x</sup> will define a reasonable logic. Since $T \vdash p$ means p is derivable from T and $T \to p$ means p demonstrably is not derivable from T, a set of rules that allowed us to show both would be incoherent. The same is true for <sup>y</sup> and <sup>x</sup> .

Definition 3: is a defeasible logic iff is a set of rules defining $\vdash , \ \right. \ \left.$ , and <sup>x</sup>, and there is no defeasible theory T and literal p such that either $T \vdash _ { \Sigma } p$ and $T \to { \ u { p } } ,$ or $T \gets _ { \Sigma } p$ and $T \to _ { \Sigma } p$

In the rules we will present here, all variables stand for ground literals or sets of ground literals. When we say that $p \in T$ , we mean that the literal p is a ground instance of a literal in T. When we say that $A \to p \in T$ , we mean that $A  p$ is a ground instance of a rule in T.

M<sup>q</sup>: If

1. $p \in T$ , or

2. $A \to p \in T$ and $\mathbf { \Delta } T \vdash A$

then $T \vdash p .$

M : If

1. $p \notin T$ and

2. for every $A \to p \in T , T \to A$

then $T \to p .$

$E ^ { + }$ : If T <sup>&</sup> p, then $T \gets p$

EE : If $\mathbf { \nabla } T \dashv p$ and $T \gets \neg p ,$ , then $T \to p .$

Definition 4: $\mathbf { M } = \{ \mathbf { M } ^ { + } , \mathbf { M } ^ { - } , \mathbf { E } ^ { + } , \mathbf { E } \mathbf { E } ^ { - } \}$

Theorem 1: M is a defeasible logic.

Proofs or references to proofs for theorems cited in the main body of the paper are collected in Appendix A.

The system M represents a minimal defeasible logic, one that includes little more than the monotonic core of a defeasible logic. This system is quite close to the minimal system defined in Ref. 13<sup>w</sup> <sup>x</sup> except that the rule EE replaces the slightly weaker rule $\mathbf { E } ^ { - }$ in that paper.

We could allow detachment of the consequent of a strict rule whenever its antecedent is defeasibly derivable. But consider the case when we have competing strict rules, and the antecedents of both are only defeasibly derivable. In this case, we will not detach the consequent of either strict rule. This localizes contradictions. We call defeasible logics with this feature semi-strict.

$$
S S ^ {+}: \text {   If   }
$$

1. $\mathbf { \nabla } \pmb { T }  \supset \mathbf { p } ,$

2. there is $A \to p \in T$ such that ${ \pmb T }  { \pmb A }$ , and

3. for each $B  \lnot p \in T , T \lnot B$

then $T \gets p .$

Now we introduce a rule for detaching the consequent of a defeasible rule.

$\pmb { D } _ { \Rightarrow } ^ { + }$ : If there is $A \Rightarrow p \in T$ such that

1. $\mathbf { \nabla } T \dashv \neg p ,$

2. $T \gets A ,$

3. for each $B \to \lnot p \in T , T \to B$ , and

4. for each $C \Rightarrow \neg p \in T { \mathrm { ~ o r ~ } } C \to \neg p \in T$ , either

Ž .a $T \to C { \mathrm { ~ o r ~ } }$

Ž . b $A \cup T _ { R }  C$ , and $C \cup T _ { R } \to A$

then $T \gets p$

We want to add ${ \bf S } { \bf S } ^ { + }$ and $\mathbf { D } _ { \Rightarrow } ^ { + }$ to M, but we must also add a stronger rule than EE that will allow us to conclude that a theory T will not support p in a wider range of cases. We need a rule that says we can do this when $\mathbf { E } ^ { + } , \mathbf { S } \mathbf { S } ^ { + }$ , and $\mathbf { D } _ { \Rightarrow } ^ { + }$ can all be shown to fail.

SD<sub>´</sub>: If

1. $\mathbf { \nabla } T \dashv { p } _ { \mathbf { \cdot } }$

2. for each $A \to p \in T$ , either

Ž .a $T \to A , \operatorname { o r }$

Ž . b there is $B \to \lnot p \in T$ such that ${ \pmb T }  { \pmb B }$

3. for each $C \Rightarrow p \in T$ , either

Ž .a $T \to C ,$

Ž . b there is $D \to \lnot p \in T$ such that $T \gets D ,$ or

Ž .c there is $E \Rightarrow \neg p \in T$ or $E \to \neg p \in T$ such that ${ \mathbf { } } T \gets E$ , and either

i. E <sup>j</sup> T <sup>y</sup> C, or <sub>R</sub>

ii. $C \cup T _ { R } \to E ,$

then $\pmb { T }  \pmb { p }$

Definition 5: $\mathbf { S D } = \mathbf { M } \cup \{ \mathbf { S S } ^ { + } , \mathbf { D } _ { \Rightarrow } ^ { + } , \mathbf { S D } _ { \Rightarrow } ^ { - } \}$

Theorem 2: SD is a defeasible logic.

It would help at this point to provide some examples to motivate this complex proof theory. However, we will defer the examples until we have defined defeasible logic graphs. We can then represent our examples graphically. After all, one of the advantages claimed for defeasible logic graphs is that they make the information of a defeasible theory clearer by presenting it in a visual format.

## 4. Defeasible graphs

The argumentation-based system we envision will allow the user to build a graph that represents defeasible theories. Initial assumptions of the theory and the antecedents and consequents of rules in the theory become labels for nodes in the graph, and rules in the theory become arcs in the graph. The user will build a graph by interacting with the screen using the keyboard and the mouse. Our defeasible language allows variables, but our ABS will only support graphs whose structure is propositional. In the rest of this paper, ‘atom’ will mean a propositional constant and ‘literal’ will mean an atom or its negation. Since users will only construct finite graphs, we restrict ourselves to graphs corresponding to finite theories. Special problems arise when there are loops in the reasoning. If we linked compound nodes to all the atoms that occur in them, these loops would show up in graphs as cyclical paths. We restrict our investigations to acyclic graphs.

We will mark a node in a graph with $\mathrm { ~ a ~ } + \mathrm { ~ t o ~ }$ indicate that it is evidently true and withŽ . $\mathrm { ~ a ~ - ~ } \mathrm { t o }$ indicate that it is evidently false. We will some-Ž . times establish that a particular atom cannot be shown either to be true or to be false. We will indicate this by marking that literal with ?. When we use a graph to reason, we first mark some nodes with <sup>q</sup> or <sup>y</sup> to show our initial assumptions. Then we propagate markers through the graph. We want to develop a method for doing this, one that is sound and complete relative to our defeasible logic.

Definition 6: G is a defeasible graph iff G is a directed graph satisfying the following conditions.

1. Each node in G is either a finite set of literals or the symbol <sup>i</sup>.

2. Each arc in G is labeled $ , \nrightarrow , \Rightarrow , \nRightarrow , \nrightarrow$ or $\phi$

3. If an arc is directed toward a node or if a node has no arc directed toward or away from it, then the node is a singleton haÕing an atom as its only element.

4. For any arcs x and y in G, if x and y are directed away from the same node, x and y are directed toward the same node, and x and y haÕe the same label, then x<sup>s</sup>y.

Definition 7: If G is a defeasible graph and A is a node in G, then A is atomic iff there is an atom p such that $A = \{ p \}$

Definition 8 Let G be a defeasible graph and let x be an arc in G.

1. $a n t ( x ) = A$ iff x is directed away from A.

2. $c o n s ( x ) = p$ { } iff x is directed toward p .

3. x is a positive arc iff x is labeled either ™ , ´ , or \ .

4. x is a negative arc $i f x$ is labeled either ¢, £, or $\phi$

5. x is a strict arc iff x is labeled either ™ or ¢ .

6. x is a defeasible arc $i f f x$ is labeled either ´ or £.

Definition 9: A finite sequence  of arcs in a defeasible graph G is a path in G iff for all $i < \ell ( \sigma )$ (where, of course, $\ell ( \sigma )$ ) is the length of , either $c o n s ( \sigma _ { i } ) \in \ a n t ( \sigma _ { i + I } ) \ o r \ \sim c o n s ( \sigma _ { i } ) \in a n t ( \sigma _ { i + I } ) .$

Definition 10: A path sigma in a graph G is a cyclic path $i f f$ there are $i , j \le \ell ( \sigma )$ such that $i \neq j$ and $\sigma _ { i } = \sigma _ { j }$

Definition 11: A defeasible graph G is acyclic $i f f$ there are no cyclic paths in G.

Definition 12: Let A be a node in a defeasible graph G and let $S _ { A } = \langle n \rangle$ there is a path in G such that $\ell ( \sigma ) = n$ and either cons $\sigma _ { n } ^ { } ) \in A \mathrm { ~ } o r \mathrm { ~ } \sim c o n s ( \sigma _ { n } ^ { } ) \in$ $A { \big / } .$ . Then depth $\mathbf { \bar { \Psi } } A , G ) = k$ if and only if either max $( S _ { A } ) = k ,$ , or $m a x ( S _ { A } )$ does not exist and $k = \infty$

Definition 13 A marked graph is a defeasible graph in which some of the atomic nodes are marked <sup>q</sup>, <sup>y</sup>, or ?.

Definition 14 For any two marked defeasible graphs $G _ { I }$ and $G _ { 2 }$ containing exactly the same nodes and arcs, $G _ { I } \subseteq G _ { 2 }$ iff for eÕery node A in $G _ { I }$ , if A is marked x in G then A is marked x in $G _ { 2 }$ .

Theorem $3 \subseteq$ is transitiÕe.

Definition 15 Let G be a defeasible graph, let A be a set of literals or <sup>i</sup>, let p be an atom, let ¨ be either ™, ¢, ´, £, \, or $\phi$ , and let x be either <sup>q</sup>, <sup>y</sup>, or ?.

1. A <sup>A</sup> G iff A is a node in G.

2. If p is an atom, then p <sup>A</sup> G iff p{ } <sup>A</sup> G.

3. $A \mapsto p \propto G$ if there is an arc y in G such that ant y( )<sup>s</sup>A, con $s ( y ) = p ,$ and x is labeled ¨. <sup>x</sup> 4. p <sup>A</sup> G iff p <sup>A</sup> G and $\{ p \}$ is marked x in G .

Definition 16: Let G be a defeasible graph and let A be a set of literals.

1. A succeeds in G iff A<sup>A</sup>G and for eÕery atom p, ( ) a $i f p \in A ,$ , then $p ^ { + } \propto G ,$ , and ( ) b $i f \sim p \in A ,$ then $p ^ { - } \propto G .$

2. A fails in G iff A<sup>A</sup>G and there is an atom p such that either ( ) a $p \in A$ <sup>y</sup> <sup>?</sup>  and either p <sup>A</sup> G or p <sup>A</sup> G, or ( )  <sup>?</sup> b <sup>;</sup>p<sup>g</sup>A and either p <sup>A</sup>G or p <sup>A</sup>G.

Definition 17: Let G and $G ^ { * }$ be marked graphs, let p be an atom such that $p \propto G ,$ and let x be $^ + , - ,$ (or ?. Then mark p, x, $G ^ { \ v { r } } ) = G ^ { * } \ v { U } ( G ^ { \ v { r } } ) = G ^ { \ v { r } }$ is the result of ) marking p with x in G $i f f \ G ^ { * }$ is exactly like G except that $p ^ { x } \not \propto G$ and $p ^ { x } \propto G ^ { * }$

Definition 18: If T is a defeasible theory, let Base T( ) $= \{ p { : } p$ is a ground atom and either $p \in T , \sim p \in T ,$ or there is a rule $r \in T$ such that $p \in a n t ( r ) , \ \sim p \in$ ant r , cons r( ) ( ) <sup>s</sup> p, or $c o n s ( r ) = \sim p .$

Definition 19: Let T be a defeasible theory. Then the initial graph for T is the marked graph $G ^ { T }$ satisfying the following conditions.

1. For each set of literals A, A <sup>A</sup> $G ^ { T }$ iff either ( ) ( )a there is p<sup>g</sup>Base T such that $A = \{ p \} , o r$ ( ) b there is a rule $r \in T$ such that A is the antecedent of r.

2. There is a node labeled <sup>i</sup> in $G ^ { T }$ iff there is a rule $R \in T$ such that the antecedent of r is B.

<sup>T</sup> [ <sup>T</sup> <sup>T T</sup> 3. A ™ p <sup>A</sup> G A ´<sup>A</sup> G , <sup>i</sup>´ p <sup>A</sup> G , or A \ p <sup>T</sup> <sup>A</sup>G iff A ] [ ™p<sup>g</sup>T A´p<sup>g</sup>T,´p<sup>g</sup>T, or A $ p \in T J$

T <sub>[</sub> T T <sub>4.</sub> <sub>A ¢ p</sub> A <sub>G</sub> <sub>A £ p</sub> A <sub>G</sub> <sub>,</sub> i<sub>£ p</sub> A <sub>G</sub> <sub>,</sub> <sub>or</sub> <sub>A \</sub>u <sup>T</sup> p<sup>A</sup>G iff A ] [ ™<sup>;</sup>p<sup>g</sup>T A´<sup>;</sup>p<sup>g</sup>T,´<sup>;</sup>p<sup>g</sup> T, or $A \to \sim p \in T J .$

5. For each node n, either

( ) a $n = \top$ and n is marked <sup>q</sup>,

( )b $n = \{ p \} , p \in T ,$ and n is marked <sup>q</sup>,

( )c $n = \{ p \} , \sim p \in T ,$ and n is labeled <sup>y</sup> , or

( ) d n is not marked.

Once we have generated the initial graph for a theory, we need a mechanism for marking additional nodes to represent the inferences the graph supports. Let us look at some examples that illustrate some of the features this mechanism should have.

Example 1: Tweety Triangle: Birds normally fly and penguins normally do not, but penguins are birds. Tweety is a penguin. The corresponding defeasible theory is Pt,{ $B x \Rightarrow F x ,$ } , Px´<sup>;</sup>Fx, Px™Bx . But what we are really interested in is the corresponding propositional theory Pt,{ $B t \Rightarrow F t , P t \Rightarrow \sim$ Ft, Pt ™ Bt . The initial graph is shown in} Fig. 1.

In the Tweety Triangle, we begin with a single node marked <sup>q</sup>. Only a satisfied positive arrow points toward Bt Ž . Tweety is a bird . So we have evidence that Tweety is a bird and no evidence to the contrary. We mark node Bt with <sup>q</sup>. Now we have conflicting evidence about whether Tweety flies: a satisfied positive arrow and a satisfied negative arrow pointing toward node Ft. We resolve the conflict by noting that there is a satisfied positive arrow pointing from Pt to Bt. So we could infer as weŽ just did that Tweety is a bird from the information. that he is a penguin. Given the knowledge represented in the graph, Pt provides more specific information than Bt. So Pt£Ft is the superior link and we mark Ft with <sup>y</sup>. The notion of specificity used here is captured in Condition 4b of rule $D _ { \Rightarrow } ^ { + }$ . Condition 4 of rule $D _ { \Rightarrow } ^ { + }$ says we can infer p from $A \Rightarrow p$ in part if for each competing rule $C \Rightarrow \neg p$ or $C \to \neg p ,$ , either our theory will not support C or C is less specific than A relative to our theory.

Example 2: The University Student: Adults are normally employed and employed people normally support themselÕes. But uniÕersity students normally are adults, normally are not employed, and normally do not support themselÕes. Jane is a uniÕersity student and Jane is employed. The propositional Õersion of this theory is u, e, a{ ´e, e ´s, u ´a, $u \Rightarrow \sim e , \ u \Rightarrow \sim s , \ - u$ . The initial graph is shown in Fig. 2.

In Example 2, we begin with u and e marked <sup>q</sup>. We only have a satisfied positive arrow pointing toward a; so we conclude that apparently Jane is an adult and mark a with <sup>q</sup>. Now we have conflicting

![](/api/attachments/X5D4GNM5/fulltext/images/47841c72d35277df32aba5872b65dfb1bf12e401abd0a434d5944f137cc242ac.jpg)  
Fig. 1. Tweety Triangle.

![](/api/attachments/X5D4GNM5/fulltext/images/0a2f3bc3ab31e5d1f19e7a40988d2112ac682a93c3f62fdfb40ef262f9ba0e43.jpg)  
Fig. 2. The University Student.

evidence about s. There is a path from u to e made up entirely of satisfied positive arrows, which suggests that u is more specific than e. But we also have a satisfied negative arrow directly from u to e. So the argument to show that u is more specific than e is itself defeated. We must mark s with ?

These examples use presumptions and other defeasible rules almost exclusively. In fact, strict rules and undercutting defeaters do not occur that often in natural examples. If we had a strict and a defeasible arrow pointing toward the same conclusion, one positive, one negative, and both satisfied, we should prefer the strict arrow. This is built into our defeasible logic and should be a part of our inference mechanism for defeasible graphs. For more patterns of defeasible arguments, see Refs. 13,19 . <sup>w</sup> <sup>x</sup>

## 5. Monotonic extensions of defeasible theories

We define monotonic extensions of a defeasible theory T, intuitively, as graphs generated by marking nodes in the initial graph for T, which are strictly derivable from the theory T.

Definition 20: Let T be any defeasible theory. Then a finite sequence  of marked graphs is a monotonic construction of G from T iff

1. $\sigma _ { 0 } = G ^ { T } ,$

2. $\sigma _ { \ell ( \sigma ) } = G ,$ and

3. for all $\begin{array} { r } { O < j \le \ell ( \sigma ) , } \end{array}$ there is $A \to p \propto G ^ { T }$ or[ $A \not \to p \propto G ^ { T } J$ such that A succeeds in $\sigma _ { j - I }$ and $\sigma _ { j } =$ <sub>j</sub>m a r k p , ( ) [ <sup>q</sup> , <sub>y 1 j</sub>o r  <sup>s</sup> $m a r k ( p , - , \pmb { \sigma } _ { j - 1 } ) J .$

Once we make our intuitive notion of a monotonic extension precise, it follows immediately that $G ^ { T }$ is itself a monotonic extension of T.

Definition 21: A marked graph G is a monotonic extension of a defeasible theory T iff there is a monotonic construction of G from T.

Theorem 4 $_ { I f G }$ is a monotonic extension of T, then $G ^ { T } \subseteq G$

Our first important result is that our method for generating monotonic extensions of defeasible theories is sound with respect to our defeasible logic. That means that literals whose truth is indicated in a monotonic extension of a theory T are strictly or monotonically derivable in T.

Theorem 5 If G is a monotonic extension of a finite defeasible theory T and p is an atom, then

1. $i f p ^ { + } \propto G$ then $T \vdash _ { s D } p ,$ and

2. $i f p ^ { - } \propto G$ then $T \vdash _ { s D } \sim p .$

Definition 22 Let T be a defeasible theory and let G be a monotonic extension of T. Then G is a maximal monotonic extension of T iff for eÕery monotonic extension $G ^ { * }$ of $G ^ { T } , G ^ { * } \subseteq G$

It does not matter in what order we mark the strict consequences of a theory in the corresponding defeasible graph. Once a strict arrow in a graph is satisfied, nothing can prevent us from marking the consequent of the arrow either $+ \mathrm { o r } \mathrm { ~ - ~ }$ . No matter what order we mark the nodes in a graph, we eventually reach a fixed-point where no further nodes can be marked. Furthermore, this fixed-point is unique and does not depend on the order in which nodes are marked in its construction.

Theorem 6: For each finite defeasible theory T, there exists a unique maximal monotonic extension of $G ^ { T }$

Definition 23: $G _ { M } ^ { T }$ is the maximal monotonic extension of the defeasible theory T.

Having established the existence of a unique maximal monotonic extension of a defeasible theory, we have given it a name. More importantly, this graph plays a crucial role in our soundness and completeness results that complete this section. Together, these results show that for any finite, acyclic theory T and any literal $p , T \vdash p$ if and only if p is marked appropriately in $G _ { M } ^ { T }$

Theorem 7: If T is a finite defeasible theory and p is an atom, then if $T \vdash _ { S D } p$ then $p ^ { + } \propto G _ { M } ^ { T }$ , and if $T \vdash _ { s D } \sim p$ then $p ^ { - } \propto G _ { M } ^ { T }$

Definition 24: Let T be a theory. Then T is SD-consistent iff there does not exist an atom p such that $T \vdash _ { S D } p$ and $T \vdash _ { s D } \sim p$

In the rest of this paper, we will restrict our attention to finite, SD-consistent theories whose initial graphs are acyclic. It will be convenient to have a name for such theories.

Definition 25: T is SD-proper if and only iff T is a finite SD-consistent defeasible theory and $G ^ { T }$ is acyclic.

Theorem 8: Let T be SD-proper.

1. If $p ^ { + } \not \propto G _ { M } ^ { T }$ , then $T \to _ { s D } p .$

2. $I f p ^ { - } \not \propto G _ { M } ^ { T }$ , then $T \mathrm { \ - } \mathrm { \ - } \mathrm { \ - } \mathrm { \ - } \mathrm { \ - } \mathrm { \ - } \mathrm { \ - } S D \mathrm { \ } \sim p .$

## 6. Defeasible extensions of defeasible theories

As the University Student example shows, relative specificity can sometimes be used to adjudicate between competing defeasible rules. One rule $A \Rightarrow p$ is more specific than another rule $B \Rightarrow \sim p$ , relative to a theory T, when we can derive B from A and the rules in T, but we cannot derive A from B and the rules in T. However, when we perform these derivations to establish specificity, we may use all the rules in T except presumptions, that is, except defeasible rules with empty antecedents. To see why this is so, consider the following example.

Example 3: Weakened Tweety Triangle: Again, birds normally fly and penguins normally do not, but penguins are birds. But this time, we only presume that Tweety is a penguin. The corresponding propositional theory is $\{ \Rightarrow P t , \ B t \Rightarrow F t , \ P t \Rightarrow \sim F t , \ P t $ Bt} Fig. 3.

In the Weakened Tweety Triangle, we should get exactly the same result as we did in the original example; apparently, Tweety does not fly. But something goes wrong in our specificity check if we use all the rules. Of course, we can still infer that Tweety is a bird if we add to our rules the fact that Tweety is a penguin. But suppose we add the fact that Tweety is a bird to our rules. Then if we use the presumption $\Rightarrow P t$ , we infer that apparently Tweety is a penguin. So neither rule is more specific than the other and we can conclude nothing about whether Tweety flies! The problem, of course, is that presumptions are analogous to defeasible facts. Just as we do not want to assume that Tweety is definitely a penguin when we are trying to see if we can infer this fact from his being a bird, neither do we want to assume that he is presumably a penguin. We must suppress all facts and presumptions in our specificity checking.

![](/api/attachments/X5D4GNM5/fulltext/images/ce87d4016c882a685a7de500a11a0dbc5414dd00561e7947003a1d9ac0beacc5.jpg)  
Fig. 3. Weakened Tweety Triangle.

In the statement of our principles for constructing defeasible graphs, we need a convenient way to refer to all the rules in a theory, excluding any presumptions in the theory.

Definition 26: Let T be any defeasible theory and let A be any finite set of literals. Then $T ( A ) = A \cup \{ R { : } R$ is a rule in T and ant $\left( R \right) \neq \emptyset$

Definition 27 Let T be any defeasible theory. Then a finite sequence of marked graphs is a defeasible construction of G from T iff

1. $\sigma _ { 0 } = G _ { M } ^ { T }$

2. $\sigma _ { \ell ( \sigma ) } = G ,$ , and

3. for all $\begin{array} { r } { O < j \le \ell ( \sigma ) , } \end{array}$ , one of the following holds.

ssG<sup>q</sup> For some atom p, $\sigma _ { j } = m a r k ( p , + , \sigma _ { j - 1 } )$ [or $\sigma _ { j } = m a r k ( p , - , \sigma _ { j - 1 } ) \bar { \cal J } ,$ and

<sup>T</sup> [ <sup>T</sup> i. there is A™p<sup>A</sup>G or A¢p<sup>A</sup>G such] that A is satisfied in $\sigma _ { j - I } ,$

ii. for all $B \not \to p \propto G ^ { T }$ [  or $B \to p \propto G ^ { T } J ,$ , B fails in $\sigma _ { j - I } .$

$\mathbf { d } \mathbf { G } ^ { \pm }$ For some atom p, $\sigma _ { j } = m a r k ( p , + , \sigma _ { j - 1 } )$ [or $\sigma _ { j } = m a r k ( p , - , \sigma _ { j - 1 } ) \bar { \cal J } ,$ and

i. there is $A \Rightarrow p \propto G ^ { T }$ [  or $A \Rightarrow p \propto G ^ { T } J$ such that A is satisfied in $\sigma _ { j - I } ,$

<sup>T</sup> [ ii. for all B ¢ p <sup>A</sup> G or $B \to p \propto G ^ { T } J ,$ B fails in $\sigma _ { j - I } ,$ , and

<sup>T</sup>iii. for all C £ p <sup>A</sup> G or $C \not \to p \propto G ^ { T }$ or [ $C \Rightarrow p \propto G ^ { T }$ <sup>T</sup> or C \ p <sup>A</sup> G , either]

A. C fails in $\sigma _ { j - I } , \ : o r$

B. there is a defeasible extension $G ^ { A }$ of $A \cup T _ { R }$ and a defeasible extension $G ^ { B } o f$ $B \cup T _ { R }$ such that B succeeds in $G ^ { A }$ and A fails in $G ^ { B }$

$\mathbf { d } \mathbf { G } ^ { ? }$ For some atom p, $\sigma _ { j } = m a r k ( p , ~ ? , ~ \sigma _ { j - 1 } ) .$

i. for each $A \to p \propto G ^ { T }$ [  or $A \not \to p \propto G ^ { T } ] ,$ either

A. A fails in $\sigma _ { j - I } , ~ o r$

<sup>T</sup> [ B. there is B ¢ p <sup>A</sup> G or $B \to p \propto G ^ { T } J$ such that B is satisfied in $\sigma _ { j - I } ,$ , and

ii. for each link $C \Rightarrow p \propto G ^ { T } ~ { l o r } ~ C \Rightarrow p \propto$ $G ^ { T } \bar { J } ,$ either

A. C fails in $\sigma _ { j - I } ,$

<sup>T</sup> [ B. there is a D ¢ p <sup>A</sup> G or $D \to p \propto G ^ { T } J$ such that D is satisfied in $\sigma _ { j - I } , ~ o r$

C. there is $E \not \Rightarrow \boldsymbol { \mathrm { p } } \propto \boldsymbol { \mathrm { G } } ^ { \mathrm { T } }$ <sup>w</sup>  or $\operatorname { E } \twoheadrightarrow p \propto G ^ { T }$ [ or $E \Rightarrow p \propto G ^ { T }$ or $E \to p \propto G ^ { T } J$ such that E is satisfied in $\sigma _ { j - I }$ and either

<sup>Ø</sup> there is a defeasible construction of a graph $G ^ { E }$ from the theory $E \cup R _ { T }$ such that C is satisfied at $\tau \ell ( \tau ) ,$ , or

<sup>Ø</sup> there is a defeasible construction  of a graph $G ^ { C }$ from the theory $C \cup T _ { R }$ such that E fails at $\tau _ { \ell ( \tau ) } .$

Conditions $\mathbf { s s } \mathbf { G } ^ { + }$ , and $\mathbf { d } \mathbf { G } ^ { ? }$ in Definition 27 correspond roughly to the rules ${ \bf S } { \bf S } ^ { + } , { \bf S D } _ { \Rightarrow } ^ { + }$ , and $\mathbf { S D } _ { \Rightarrow } ^ { - }$ in our defeasible logic SD. Notice that our definition is recursive. The notion of defeasible constructions from theories $E \cup R _ { T }$ and $C \cup T _ { R }$ are mentioned at the end of the definition of a defeasible construction from theory $T . \ S 0 ,$ to actually show that one defeasible construction existed, we would sometimes need to show that another existed. As we shall see when we restrict some of our results, this turns out not to be a problem. When we restrict ourselves to finite, acyclic theories, each new construction required must be in a sense ‘shorter’ than the construction for which it is required. Eventually, we must reach a construction that requires no further construction.

Definition 28: A marked graph G is a defeasible extension of a defeasible theory T iff there is a defeasible construction of G from T.

Theorem 9 If G is a defeasible extension of T, then $G _ { M } ^ { T } \subseteq G$

To show that our graph-marking principles are correct, we need to show that whenever a node in a graph is marked <sup>q</sup> or <sup>y</sup>, the corresponding atom labeling the node or the negation of that atom is defeasibly derivable in the theory upon which the graph is based. To show this, we will need a more specific notion of what it means for a graph to be correct or sound at a single node.

Definition 29 Let T be a defeasible theory, G a defeasible extension of T, and p an atom. Then G is T-sound at $p ~ i f f$

1. if ${ p ^ { + } \propto G } ,$ then $T \gets { } _ { S D }$ p and $T \to _ { s D } \sim p$

2. $i f p ^ { - } \propto G ,$ then $T  _ { S D } \sim p$ and $T  _ { _ { S D } } p ,$ and

3. $i f p ^ { ? } \propto G ,$ then $T \to _ { S D }$ p and $T \to _ { \mathit { s D } } \sim p .$

The notion of T-soundness at a node is used in the proof of the following soundness results.

Theorem 10: Let G be a defeasible extension of an SD-proper theory T such that for eÕery node p in { } $G ^ { T }$ , if depth $\begin{array} { r } { \{ p \} , G ^ { T } ) \leq k , } \end{array}$ then G is T-sound at p. If A is a node in $G ^ { T }$ such that depth ${ \bf \ddot { \theta } } { \bf \Phi } ^ { \prime } { \bf \Phi } _ { A , G } ^ { T } { \bf \Phi } ^ { \prime } \le k ,$ then

1. if A succeeds in G, then $T \gets { } _ { S D }$ A, and

2. if A fails in G, then $T \to _ { S D } \ A .$

Theorem 11: If T is SD-proper, G is a defeasible extension of T, and $p \propto G ^ { T }$ , then G is T-sound at p.

Since strict rules can never be defeated when their antecedents are strictly derivable, it is not too surprising that we arrive at a unique maximal monotonic extension of a defeasible theory. But defeasible rules can interfere with one another. One might expect that whether a particular rule can be used might depend on whether or not some possible competitor has already been applied. In fact, in such well-known non-monotonic formalisms as Mc-Carthy’s circumscription 9,10 , Reiter’s default logic<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 22 , McDermott’s and Doyle’s non-monotonic logic <sup>w x</sup> <sup>w x</sup> 11 , or Moore’s autoepistemic logic 12 , this is exactly what happens and we get multiple minimal models, extensions, or fixed-points for a single theory. But this is not the case for defeasible logic graphs or, for that matter, for the defeasible logic Ž SD upon which they are based ..

Definition 30: If T is SD-proper, then G is a maximal defeasible extension of T iff G is a defeasible extension of T and for eÕery defeasible extension $G ^ { * }$ of T, $G ^ { * } \subseteq G$

Theorem 12: If T is SD-proper, then there exists a unique maximal defeasible extension of T.

Definition 31: If T is SD-proper, let $G _ { D } ^ { T }$ be the unique maximal defeasible extension of T.

Theorem 13: If T is SD-proper and $p \propto G ^ { T }$ , then p is marked in $G _ { D } ^ { T }$

This brings us to our final theorem, a completeness result for defeasible logic graphs.

Theorem 14: If T is SD-proper and $p \in B a s e ( T )$ then

1. $i f T  _ { S D } p ,$ then ${ p } ^ { + } { \propto } G _ { D } ^ { T } ,$

2. $i f T  _ { S D } \sim p ,$ then $p ^ { - } \propto G _ { D } ^ { T } ,$

3. if $T \to _ { \mathit { s D } } p ,$ then $p ^ { - } \propto G _ { D } ^ { T } \ o r p ^ { ? } \propto G _ { D } ^ { T } \ a n d$

4. $i f T ^ { \ l - 3 } { } _ { S D } \sim p ,$ then $p ^ { + } \propto G _ { D } ^ { T } \ o r p ^ { ? } \propto G _ { D } ^ { T } ,$

## 7. Conclusions

The defeasible logic SD is a nonmonotonic extension of a fragment of first-order logic. While the language is much weaker than that of FOL, and the proof theory is effectively restricted to the propositional case, SD still allows us to represent and reason about a large class of interesting situations.

Defeasible logic graphs represent a further restriction on defeasible logic. While defeasible logic allows variables to appear in theories, defeasible logic graphs are explicitly propositional. The algorithm for marking defeasible logic graphs is applicable only to SD-proper theories. SD is not restricted in these ways.

While defeasible logic graphs are strictly weaker than defeasible logic in these respects, d-graphs also have some clear advantages. First and foremost, d-graphs offer a clear, visual representation of complex situations. The relations between the propositions in a domain are much clearer in a graph than in a set of rules. Furthermore, we have found that for an SD-proper theory T, eÕery node in the corresponding graph is eventually marked either $+ , -$ or ?. That means that our algorithm determines for each atom in Base T( ) whether it is derivably true, derivably false, or underdetermined. Defeasible logic graphs are decisiÕe. This is not the case for SD and defeasible theories in general. In fact, d-graphs provide a decision procedure for a sub-class of defeasible theories.

Some projected extensions to the theory of defeasible logic graphs are discussed in the sequel 19 .<sup>w</sup> <sup>x</sup>

## Acknowledgements

During preparation of the final version of this paper, we received helpful criticism from members of the Defeasible Logic Discussion Group at the Artificial Intelligence Center: Victor Bancroft, David Goodman, Christopher Henderson, and Zachary Hunter. The second author gratefully acknowledges support from the Deutscher Akademischer Austauschdienst during her year at the University of Georgia.

## Appendix A. Proofs of results

Results equivalent to Theorems 1 and 2 are proved in Ref. 13 . Theorems 3, 4, and 9 are trivial.<sup>w</sup> <sup>x</sup>

Theorem 15: If G is a monotonic extension of a finite defeasible theory T and p is an atom, then

1. if p <sup>A</sup> G then $T \vdash _ { s D } p ,$ and

2. $i f p ^ { - } \propto$ G then $T \vdash _ { s D } \sim p .$

Proof. Suppose T is a finite defeasible theory and is a monotonic construction of G from T.

Basis step: $\sigma _ { 0 } = G ^ { \mathrm { T } }$ . By definition, if $p ^ { + } \propto G ^ { \mathrm { T } }$ then $p \in T$ . But then by $\mathbf { M } ^ { + } , T \vdash \ l _ { S D } p .$ The argument for $p ^ { - } \propto G$ is exactly parallel.

Induction step: assume that $0 < k \leq \ell ( \sigma )$ , and for all $j < k$ and $p \propto G ^ { T } ,$ , if $p ^ { + } \propto \sigma _ { j }$ <sup>w</sup>or $\mathfrak { p } ^ { - } \propto \sigma _ { i } ] ,$ , then $T \vdash _ { \mathit { s D } } p \ [ { \mathrm { o r } } \ T \vdash _ { \mathit { s D } } \sim p ]$ . Suppose $p ^ { + } \propto \sigma _ { k }$ . If $p ^ { + } \alpha$ $\sigma _ { k - 1 }$ then by our inductive hypothesis we are finished. So suppose p is unmarked in $\sigma _ { k - 1 }$ . Then $\sigma _ { k } = m a r k ( p , + , \sigma _ { k - 1 } )$ and we can let $A \to p \propto G ^ { T }$ such that A succeeds in $\sigma _ { k - 1 } . ~ \mathrm { \bf ~ B y }$ our inductive hypothesis, for every atom q, if $q \in A$ , then $T \vdash _ { S D } q .$ and ${ \mathrm { i f ~ } } \sim q \in A$ , then $T \vdash _ { S D } \sim q . \mathrm { S o } \ T \vdash _ { S D } A$ . Since $A \to p \propto G ^ { T } , \ A \to p \in T$ . So by $M ^ { + } , T \vdash _ { S D } p$ . The argument for $p ^ { - } \propto G$ is exactly parallel.

By mathematical induction, for all $i \le \ell ( \sigma )$ and all atoms $p ^ { + } \propto \sigma _ { i }$ , then ${ \mathrm { T } } \vdash { _ { S D } p } .$ , and if $p ^ { - } \propto G$ then $T \vdash _ { s D } \sim p$ . But $G = \sigma _ { \ell ( \sigma ) }$

Theorem 6: For each finite defeasible theory T, there exists a unique maximal monotonic extension of $G ^ { T }$

Proof. Let T be a finite defeasible theory. Let n be twice the number of nodes in $G ^ { T }$ . For any monotonic extension of T, let marked G( ) be the number of nodes in G marked <sup>q</sup> plus the number of nodes in G marked <sup>y</sup>. Since G has the same nodes as $G ^ { T } .$ and allowing that each node might be marked both $+ ~ \mathrm { a n d } ~ - , ~ m a r k e d ( G ) \leq n .$ . Let m be the largest integer such that there is a monotonic extension G of T such that $m a r k e d ( G ) = m$ , and let $G _ { M } ^ { T }$ be a mono-(tonic extension of T such that marked ${ \overset { \underset { \mathrm { . . } } { } } { G _ { M } ^ { T } } } ) = m$ . We shall show that $G _ { M } ^ { T }$ is a unique maximal monotonic extension of T. Let G be any monotonic extension of T and let be a monotonic construction of G from T.

Basis step: Since $\sigma _ { 0 } = G ^ { T }$ and $G _ { M } ^ { T }$ is a monotonic extension of T, $\sigma _ { 0 } \subseteq G _ { M } ^ { T }$ by a previous theorem.

Induction step: Assume $j < \ell ( \sigma )$ and $\sigma _ { j } \subseteq G _ { M } ^ { T }$ Then let $A \to p \propto G ^ { T }$ <sup>w</sup> or $A \not \to p \propto G ^ { T } ]$ such that A succeeds in $\sigma _ { j }$ and $p ^ { + } \not \propto \sigma _ { i } ]$ <sup>w</sup>or $p ^ { - } \not \propto \sigma _ { i } ]$ . Since $\sigma _ { i } \subseteq G _ { M } ^ { T }$ , A succeeds in $G _ { M } ^ { T }$ . If $p ^ { + } \not \propto \dot { G } _ { M } ^ { T }$ <sup>w</sup> or $p ^ { - } \not \propto$ $\begin{array} { r } { \check { G } _ { M } ^ { T } ] _ { : } } \end{array}$ , let $G ^ { * } = m a r k ( p , + , G _ { M } ^ { T } )$ <sup>w</sup> or let $G ^ { * } =$ Ž mark $p , - , G _ { M } ^ { T } ) ]$ . Then $G ^ { * }$ is a monotonic extension ( of T and marked $G ^ { * } ) >$ Ž <sup>T</sup> marked G ., which is impossible. So $p ^ { + } \propto G _ { M } ^ { T }$ <sup>w</sup> or $p ^ { - } \propto G _ { M } ^ { T } ]$ , and $\sigma _ { j + 1 } \subseteq G _ { M } ^ { T }$

By mathematical induction, for each $j \le \ell ( \sigma )$ $\sigma _ { \mathrm { i } } \subseteq G _ { M } ^ { T }$ . So $\sigma _ { \ell ( \sigma ) } \subseteq G _ { M } ^ { T }$ , i.e., $G \subseteq G _ { M } ^ { T }$ . So $G _ { M } ^ { T }$ is a maximal monotonic extension of T. If $G _ { 1 }$ and $G _ { 2 }$ are both maximal monotonic extensions of T, then $G _ { 1 } \subseteq G _ { 2 }$ and $G _ { 2 } \subseteq G _ { 1 }$ . But then, $G _ { 1 } = G _ { 2 }$ . So $G _ { M } ^ { T }$ is a unique maximal monotonic extension of T.

Theorem 7: If T is a finite defeasible theory and p is an atom, then if $T \vdash _ { S D } p$ then $p ^ { + } \propto G _ { M } ^ { \varGamma }$ , and if $T \vdash _ { s D } \sim p$ then $p ^ { - } \propto G _ { M } ^ { T }$

Proof. If $p \in T$ , then ${ \boldsymbol { p } } ^ { + } \propto { \boldsymbol { G } } ^ { T } ,$ , and since $G ^ { T } \subseteq G _ { T } ^ { M }$ $p ^ { + } \propto G _ { M } ^ { T }$ . Similarly, if $\sim p \in T$ , then ${ \boldsymbol { p } } ^ { - } \propto G ^ { T }$ and $p ^ { - } ~ G _ { M } ^ { T }$

Suppose $A \to p \in T$ and A succeeds in $G _ { M } ^ { T }$ . Then $p ^ { + } \propto G _ { M } ^ { T }$ since $G _ { M } ^ { T }$ is a maximal monotonic extension of $G ^ { \mathrm { T } }$ . Similarly, if $A \to \sim p \in T$ and A succeeds in $G _ { M } ^ { T }$ then $p ^ { - } \propto G _ { M } ^ { T }$

Our result follows immediately by induction on the length of a proof in SD.

Theorem 8: Let T be SD–proper.

1. If $p ^ { + } \not \propto G _ { M } ^ { T }$ , then $T \to _ { s D } p .$

2. if $p ^ { - } \not \propto G _ { M } ^ { T }$ , then $T \dashv _ { s D } \sim p .$

Proof. Assume the hypothesis.

Basic step: Suppose $\{ p \}$ is a node in $G ^ { T } { \mathrm { . } }$ $d e p t h ( \langle p \rangle , G ^ { T } ) = 0$ , and $p ^ { + } \not \propto G _ { M } ^ { T }$ . Then $p ^ { + } \not \propto G ^ { T }$ since $G ^ { T } \subseteq G _ { M } ^ { T }$ . So $p \notin T$ . If $A \to p \in T$ , then $A $ $p \propto G ^ { T }$ and $d e p t h ( \{ p \} , G ^ { T } ) > 0$ . So there is no $A  p$ $\in T$ . Then by $M ^ { - } , T \mathcal { - } \vert _ { s D } p$

By a parallel argument, if $\{ p \}$ is a node in $G ^ { T } { \mathrm { . } }$ $d e p t \dot { h } ( \{ p \dot { \jmath } , G ^ { T } ) = 0$ , and $p - \notin { \cal G } _ { M } ^ { T }$ then $T \dashv _ { s D } \sim p$

Induction step: Assume $0 < k$ and for every atomic node $\{ p \}$ in $G ^ { T }$ ({ } , if depth p , $G ^ { T } ) < k$ , then

1. if $p ^ { + } \not \propto G _ { M } ^ { T }$ , then $T  _ { _ { S D } } p ,$ , and

2. if $p ^ { - } \not \propto G _ { M } ^ { T }$ , then $T \dashv _ { s D } \sim p .$

Suppose $\{ p \}$ is a node in $G ^ { T } .$ $d e p t h ( \{ p \} , G ^ { T } ) = k$ and $p ^ { + } \not \propto G _ { M } ^ { T }$ . Then as above, $p \notin T .$ . Suppose $A $ $p \in T$ . Then $A \to p \propto G ^ { T }$ . If A succeeds in $G _ { M } ^ { T }$ then $\mathfrak { p } ^ { + } \propto G _ { M } ^ { T }$ by the definition of a monotonic extension since $G _ { M } ^ { T }$ is a maximal monotonic extension of T. So since $p ^ { + } \not \propto G _ { M } ^ { T }$ A does not succeed in $G _ { M } ^ { T }$ . So there is an atom q such that either $q \in A$ and $q ^ { + } \not \propto G _ { M } ^ { T } , \mathrm { o r } \ \sim q \in A$ and $\mathsf { q } ^ { - } \not \propto G _ { M } ^ { T }$ . Then depth q ,({ } $G ^ { T } ) <$ depth

$( \{ p \} , G ^ { T } ) = k$ Ž since $A \to p \propto G ^ { T }$ and either $q \in A$ or $\sim q \in A )$ . By our inductive hypothesis, either $q \in A$ and $q ^ { + } \not \propto G _ { M } ^ { T }$ and $T \dashv { i } _ { s D } q , \mathrm { o r } \sim q \in A$ and $q ^ { - } \not \propto G _ { M } ^ { T }$ and $T \dashv _ { s D } \sim { \mathsf { q } }$ . In either case, $T \to _ { s D } A$ . Thus, for each $A \to p \in T , T \to _ { s D } A$ . Then by M , $T \dashv _ { s D } p .$

By a similar argument, if $\mathrm { p } ^ { - } \propto G _ { M } ^ { T } , T \to \ L _ { S D } \sim p .$

By mathematical induction, our claim holds for nodes of any depth in $G _ { M } ^ { T }$

Theorem 10: Let G be a defeasible extension of an SD–proper theory T such that for eÕery node p in { } $G ^ { T }$ ({ }  , if depth p , $G ^ { T } ) \leq k ,$ , then G is T-sound at p. If A is a node in $G ^ { T }$ ( such that depth A, $G ^ { T } ) \leq k ,$ then

1. if A succeeds in G, then $T  { } _ { S D } A$ , and

2. if A fails in $G ,$ then $T \to _ { S D } \ A .$

Proof. Assume the hypothesis.

Suppose A succeeds in G. If atom $p \in A$ , then ({ } depth p , $G ^ { T } ) \le d e p t h ( A , G ^ { T } )$ and, by our hypothesis, G is T-sound at p. But since A succeeds in G, $\mathfrak { p } ^ { + } \propto G .$ . By the definition of T-soundness at $p ,$ $T \gets _ { s D } p$ . By a parallel argument, if $\sim p \in A , T  _ { S D }$ $\sim p .$ . So $T  { } _ { S D } A$

Suppose A fails in G. If $p ^ { - } \propto G$ and $p \in A$ , then $d e p t h ( \bar { \langle } p \boldsymbol { \jmath } , G ^ { T } ) \leq d e p t h ( \boldsymbol { A } , G ^ { T } )$ and G is T-sound at $p .$ But then by the definition of T-soundness at p, $T  _ { _ { S D } } p$ and $T \to _ { S D } A$ . By parallel arguments, if $p ^ { + } \propto G$ and $\sim p \in A$ , then $T \to _ { S D } \ A $ ; and if $p ^ { ? } \propto G$ and either $p \in A { \mathrm { ~ o r ~ } } \sim p \in A$ , then $T \to _ { S D } A$

Theorem 11: If T is SD-proper, G is a defeasible extension of T, and $p \propto G ^ { T }$ , then G is T-sound at p.

Proof. By mathematical induction on the depth of a node in an extension, we shall show that for any theory T, defeasible extension G of T, and atom $p ,$ G is T-sound at $p .$

Basic step: Let G be a defeasible extension of a theory T and let $\sigma$ be a defeasible construction of G. We will use mathematical induction on the length of $\sigma$ to show that for all $0 \leq k \leq \ell ( \sigma )$ , if $\{ p \}$ is a node in $\sigma _ { k }$ and $d e p t h ( \{ p \} , G ^ { T } ) = 0$ , then $\sigma _ { k }$ is $T _ { - }$ sound at p.

Basis step for subderivation 1: $\sigma _ { 0 } = G _ { M } ^ { T }$ . Suppose $\{ p \}$ is a node in $G _ { M } ^ { T }$ ({ } and depth p , $G ^ { T } ) = 0$ . If $p ^ { + } \propto G _ { M } ^ { T }$ , then by a previous theorem, $T _ { S D } p ,$ so $T \gets _ { s D } p$ by $E ^ { + }$ . Since T is SD-proper and therefore Ž . SD-consistent, T not $\mathbf { \Pi } _ { - \vdash } \int \mathbf { \Pi } _ { S D } \sim \mathbf { \Pi } _ { p }$ . But if $p ^ { - } \propto G _ { M } ^ { T }$ then by the monotonic soundness of ${ G _ { M } ^ { T } , T \vdash \ l _ { S D } \sim p }$ So $p ^ { - } \not \propto G _ { \mathrm { M } } ^ { \mathrm { T } }$ . Then by a previous theorem, $T \to _ { S D } \sim$ $p ,$ and by $E E ^ { - } , T  \ l _ { S D } \sim p$

Similarly, if $p ^ { - } \propto G _ { M } ^ { T }$ , then $T  { } _ { S D } \sim p$ and T $ _ { S D P }$ . Notice that no node is marked ? in $G _ { M } ^ { T } ; \mathrm { { s o } }$ we can ignore this case. So $G _ { M } ^ { T }$ is T-sound at $p .$

Induction step for subderivation 1: Assume $0 < k$ $\le \ell ( \sigma )$ , and for all $0 \le j < k$ , if there is a node $\{ p \}$ in $G ^ { T }$ ({ } such that depth p , $G ^ { T } ) = 0$ , then $\sigma _ { j }$ is T-sound at $p .$

 4 Suppose p is a node in $G ^ { T }$ and depth p , ({ } $G ^ { T } ) = 0 . { \mathrm { ~ I f ~ } } \{ p \}$ is marked in $\sigma _ { k - 1 } ,$ then since $\sigma _ { k - 1 }$ $\subseteq \sigma _ { k }$ and by our inductive hypothesis, $\sigma _ { k }$ is T-sound at p. So suppose p is not marked in $\sigma _ { k - 1 }$

If $p ^ { + } \propto \sigma _ { k }$ , then $\sigma _ { k } = m a r k ( p , + , \sigma _ { k - 1 } )$ and either there is $A \to p \propto G ^ { T }$ or there is $A \Rightarrow p \propto G ^ { T }$ . In either case, $d e p t h ( \{ p \} , G ^ { T } ) > 0$ . So this case is impossible. Similarly, the case where $p ^ { - } \propto \sigma _ { k }$ is impossible.

Suppose $p ^ { ? } \propto \sigma _ { k }$ . Since p is unmarked in $\sigma _ { k - 1 }$ and $G _ { M } ^ { T } = \sigma _ { 0 } \subseteq \sigma _ { k - 1 } , ~ p ^ { + } \not \propto G _ { M } ^ { T }$ and $p ^ { - } \not \propto G _ { M } ^ { T }$ . So by a previous theorem, $T \dashv _ { s D } p$ and $T \dashv _ { s D } \sim p .$ . Since $\bar { d e p t h { ( i p / , ~ G ^ { T } ) } } = 0 .$ , there is no A such that $A  p$ $\propto G ^ { T } , A \not \to p \propto G ^ { T } , A \Rightarrow p \propto G ^ { T }$ , or $A \not \Rightarrow p \propto G ^ { T }$ So by the definition of $G ^ { T } { \mathrm { . } }$ , there is no A such that $A \to p \in T , \ A \to \sim p \in T , \ A \Rightarrow p \in T ,$ , or $A \Rightarrow \sim p$ $\in T$ . So the remaining conditions for $S \mathrm { D } _ { \Rightarrow } ^ { - }$ are satisfied vacuously for both p and $\sim p .$ . Therefore, $T \to _ { S D } p$ and $T \to _ { s D } \sim p$

By mathematical induction, for all $0 \leq k \leq \ell ( \sigma )$ if $\{ p \}$ is a node in $G ^ { T }$ and $d e p t h ( \{ p \} , G ^ { T } ) = 0$ , then $\sigma _ { k }$ is T-sound at p. But $G = \sigma _ { \ell } ( \sigma )$

This establishes the basis step for our main proof. Induction step: Let $0 < k$ and assume that if T is a defeasible theory, G is a defeasible extension of $T ,$ $\{ p \}$ is a node in $G ^ { T }$ , and $d e p t h ( p , G ^ { T } ) < k$ , then G is T-sound at $p .$

Suppose T is a defeasible theory, G is a defeasible extension of T, and is a defeasible construction of G. We will use mathematical induction to show that for all $0 \leq j \leq \ell ( \sigma ) , \operatorname { i f } \left\{ p \right\}$ is a node in $G ^ { T }$ and $d e p t h ( \{ p \} , G ^ { T } ) = k$ , then $\sigma _ { j }$ is T-sound at $p .$

Basis step for subderivation $2 \colon \sigma _ { 0 } = G _ { M } ^ { T }$ . Suppose $\{ p \}$ is a node in $G ^ { T }$ and $d e p t h ( \{ p \} , G ^ { T } ) = k$

Suppose $p ^ { + } \propto G _ { M } ^ { T }$ . Then by a the monotonic soundness of $G _ { M } ^ { T } , T \vdash \ l _ { S D } p$ . But then by $E ^ { + } , T  \infty p .$ Since T is SD-consistent, T not $\vdash _ { _ { S D } } \sim p ,$ , and by the monotonic soundness of $G _ { M } ^ { T } , \mathfrak { p } ^ { - } \propto G _ { M } ^ { T }$ . Then by a previous theorem, $T \to _ { s D } \sim p$

Similarly, if $p ^ { - } \propto G _ { M } ^ { T }$ , then $T  { } _ { S D } \sim p$ and T $\boldsymbol { \dashl } _ { S D } p .$

Since there are no nodes in $G _ { M } ^ { T }$ marked ?, we can conclude that $\sigma _ { 0 }$ is T-sound at p.

Induction step for subderivation 2: Assume $0 < j$ $\le \ell ( \sigma )$ and for every $0 \leq l < j$ , if $\{ p \}$ is a node in $G _ { T }$ and $d e p t h ( \{ p \} , G _ { T } ) = k$ , then $\sigma _ { 1 }$ is T-sound at $p .$ Assume $\{ p \}$ is a node in $G _ { T }$ and $d e p t h ( \{ p \} , G _ { T } ) = k$

Suppose $p ^ { + } \propto \sigma _ { j }$ . If $p ^ { + } \propto \sigma _ { j - 1 }$ , then $\sigma _ { j }$ is Tsound at p by our inductive hypothesis. So suppose $p ^ { + } \not \propto \sigma _ { j - 1 }$ Then $\sigma _ { i } = m a r k ( p , + , \sigma _ { i - 1 } )$ and p and $\sigma _ { j - 1 }$ satisfy one of ss $G ^ { + }$ or $d G ^ { \pm }$ . Since $\{ p \}$ is not marked in $\sigma _ { j - 1 }$ and $G _ { M } ^ { T } \subseteq \sigma _ { j - 1 } , \ p ^ { - } \not \propto G _ { M } ^ { T }$ and, by a previous theorem, $T \dashv _ { s D } \sim p .$

Case 1: p and $\sigma _ { j - 1 }$ satisfy $s s G ^ { + }$ . Let $A \to p \alpha$ $G ^ { T }$ such that A succeeds in <sub>y</sub> . By the definition of $G ^ { T } , \ A \to p \in T$ . Since $A \to p \propto G ^ { T }$ $d e p t h ( A , G ^ { T } )$ $< d e p t h ( \{ p \} , G ^ { T } ) = k$ . Then by our inductive hypothesis and the preceding theorem, $T  { } _ { S D } A$ . By a similar argument, if $B \to \sim p \in T$ , then $\bar { B } \not \to p \propto G ^ { T } ,$ , B fails in $\sigma _ { j - 1 }$ since p and $\sigma _ { j - 1 }$ satisfy $s s G ^ { + }$ , and $T \to _ { S D } B _ { \ O }$ . So by $S S ^ { + } , T  _ { S D } \dot { p } .$

Case 2: p and $\sigma _ { j - 1 }$ satisfy $d G ^ { \pm }$ . Let $A \Rightarrow p \propto G ^ { T }$ such that A succeeds in $\sigma _ { j - 1 } .$ and for all $B \not \Rightarrow p \propto G ^ { T }$ <sup>w</sup> or $B \not \to \ p \propto G ^ { T } ] ,$ , either B fails in $\sigma _ { j - 1 }$ or there are defeasible extensions $G ^ { A }$ of $A \cup { \dot { T } } _ { R }$ and $G ^ { B }$ of $B \cup T _ { R }$ such that B succeeds in $G ^ { A }$ and A fails in $G ^ { B } .$ . Then as above, $T  { } _ { S D } A$ . By the definition of $G ^ { T } , A \Rightarrow p \in T$ . Now suppose $B \Rightarrow \sim p \in T $ . Then $B \not \Rightarrow p \propto G ^ { T } .$ . If B fails in $\sigma _ { j - 1 } ,$ then since $B \nRightarrow p \propto$ $G ^ { T }$ ( , depth B, $G ^ { T } ) < d e p t h ( \check { p , } G ^ { T } ) = k .$ So by our inductive hypothesis and the preceding theorem, T $ _ { S D } B _ {  }$ . Suppose, on the other hand, that there are defeasible extensions $G ^ { A }$ of $A \cup T _ { R }$ and $G ^ { B }$ of $B \cup T _ { R }$ such that B succeeds in $G ^ { A }$ and A fails in $G ^ { B }$ Clearly, $d e p t h ( { \cal A } , { \cal G } ^ { B } ) \leq d e p t h ( { \cal A } , { \cal G } ^ { T } ) <$ $d e p t h ( p , G ^ { T } ) = k$ and $d e p t h ( B , G ^ { A } ) \leq d e p t h ( B , G ^ { T } ) <$ $d e p t h ( \{ p \} , G ^ { T } ) = k$ . So by our inductive hypothesis and the preceding theorem, $A \cup T _ { R }  _ { S D } B$ and B<sup>j</sup> $T _ { R } \to _ { S D } A$ . Finally, as in Case 1, since p and $\sigma _ { j - 1 }$ satisfy $d G ^ { \pm }$ , if $B \to \sim p \in T$ , then $B \not \to p \propto G ^ { T }$ and $T \to _ { S D } B _ { \ O }$ . So by $S D _ { \Rightarrow } ^ { + } , \ T  _ { S D } p$ . As in Case 1, we can also show that $T \to _ { \mathit { s D } } \sim p$

Similarly, if $p ^ { - } \propto \sigma _ { i - 1 } , T  _ { s D } \sim p$ and $T \to _ { s D } p$ Suppose $p ^ { ? } \propto \sigma _ { i - 1 }$ . Then p and $\sigma _ { j - 1 }$ satisfy $d G ^ { ? }$ . If $A \to p \in T$ , then $A \to p \propto G ^ { T } ,$ , and either A fails in $\sigma _ { j - 1 }$ Žand, as above, $T  { } _ { S D } A )$ or there is $B \not \to p \propto { \bar { G } } ^ { T }$ Žand thus $B \to \sim p \in T )$ such that B succeeds in $\sigma _ { j - 1 }$ Žand, as above, $T \gets _ { S D } B )$ . Similarly, if $A \to { \overset { \cdot } { \sim } } p \in T$ , then either $T \to _ { S D } A$ or there is $B \to p \in T$ such that $T \gets _ { S D } B$ . If $A \Rightarrow p \propto G ^ { T }$ then one of three cases holds.

Case 1: A fails in $\sigma _ { j - 1 }$ . Then as above, $T \to _ { S D } A$

Case 2: There is $\Breve { B ^ { \prime } } \not  p \propto G ^ { T }$ such that B succeeds in $\sigma _ { j - 1 }$ . Then as above, $B \to \sim p \in T$ and $T \gets _ { S D } B .$

Case 3: There is $B \not \to p \not \propto G ^ { T }$ <sup>w</sup> or B $\not \to p \propto G ^ { T } ]$ such that B succeeds in $\sigma _ { j - 1 }$ and either there is a defeasible extension $G ^ { A }$ of $A \cup T _ { R }$ such that B fails in $G ^ { A }$ or there is a defeasible extension $G ^ { B }$ of $B \cup T _ { R }$ such that A succeeds in $G ^ { B }$ . For such a $B \nRightarrow p$ <sup>w</sup>or $B \not \to p ]$ $B \Rightarrow \sim p \in T$ <sup>w</sup>or $B \to \sim p \in T ]$ As above, since B succeeds in $\sigma _ { j - 1 } , \ T  _ { \mathit { s D } } B$ . If there is a defeasible extension $G ^ { A }$ of $A \cup T _ { R }$ such that B fails in $G ^ { A }$ , then as above, $A \cup T _ { R } \lnot _ { s D } B$ . If there is a defeasible extension $G ^ { B }$ of $B \cup T _ { R }$ such that A succeeds in $G ^ { B }$ , then $B \cup T _ { R }  _ { S D } A$

The case where $A \Rightarrow p \propto G ^ { T }$ is exactly parallel.

So by $S D _ { \Rightarrow } ^ { - } , \ T  _ { S D } p$ and $T \to _ { s D } \sim p .$ . So $\sigma _ { j }$ is T-sound at $p .$

Thus, by mathematical induction, for all $0 \leq j \leq$ $\ell ( \sigma )$ , nodes $\{ p \}$ in $G ^ { T }$ such that $d e p t h ( \{ p \} , G ^ { T } ) = k$ $\sigma _ { j }$ is T-sound at $p .$ Since $G = \sigma _ { \ell } ( \sigma )$ , for all nodes $\{ { \overset { \cdot } { p } } \}$ in $G ^ { T }$ ({ } such that depth p , $G ^ { \acute { T } } ) = k .$ , G is T-sound at $p .$ This completes our second subderivation.

Then by mathematical induction, for all k, if $T$ is SD-proper, $G$ is a defeasible extension of T, and there is a node $\{ p \}$ in $G ^ { T }$ such that $d e p t h ( \{ p \} ,$ $G ^ { T } ) = k ,$ , then $G$ is T-sound at $p .$ But for any atom $p ,$ if T is SD-proper and $p \propto G ^ { T }$ , then there is a k ({ } such that depth p , $G ^ { T } ) = k .$ . So for SD-proper theory $T _ { \ast }$ , every defeasible extension $G$ of $T _ { \ast }$ , and every atom p, G is T-sound at $p .$

Theorem 12: If T is SD-proper, then there exists a unique maximal defeasible extension of T.

Proof. The proof is exactly parallel to the proof that every defeasible theory has a unique maximal monotonic extension.

Theorem 13: If T is SD-proper and $p \propto G ^ { T }$ , then $p$ is marked in $G _ { D } ^ { T }$

Proof. Suppose $p \propto G ^ { T }$ . If p is not marked in $G _ { D } ^ { T }$ then by examination of cases, we see that $G _ { D } ^ { T }$ and $p$ must satisfy one of $s s G ^ { + }$ $d G ^ { \pm }$ , or $d G ^ { ? }$ . So there is a defeasible extension $G$ of T such that $G =$ mark $( p , + , G _ { D } ^ { T } )$ $G = m a r k ( p , - , G _ { D } ^ { T } )$ or $G =$ $m a r k ( p , ? , G _ { D } ^ { T } )$ . But then $G _ { D } ^ { T }$ is not a maximal defeasible extension of T. Since this is impossible, $p$ is marked in $G _ { D } ^ { T }$

Theorem 14: If T is SD-proper and $p \in B a s e ( T )$ then

1. if $T \gets _ { s D } p ,$ then ${ p } ^ { + } { \propto } G _ { D } ^ { T } ,$

2. $i f T  _ { S D } \sim p ,$ then $p ^ { - } \propto G _ { D } ^ { T }$

3. $i f T \negmedspace \ l _ { S D } p ,$ then $p ^ { - } \propto G _ { D } ^ { T } \stackrel { - } { o r } p ^ { ? } \propto G _ { D } ^ { T }$ , and

4. $i f T ^ { \ l - 3 } { } _ { S D } \sim p ,$ then $p ^ { + } \propto G _ { D } ^ { T }$ or $p ^ { ? } \propto G _ { D } ^ { T } .$

Proof. If $p \in B a s e ( T )$ , then $p \propto G ^ { T }$ by the definition of $G ^ { T }$ . So by the previous theorem, $p$ is marked in $G _ { D } T$

Suppose $T \gets _ { s D } p .$ . If $p ^ { - } \propto G _ { D } ^ { T }$ , then $T  { } _ { S D } \sim p$ and $T$ is SD-inconsistent. If $p ^ { ? } \propto G _ { D } ^ { T }$ , then $T \to _ { s D } p$ and SD is not a defeasible logic. Since neither of these is possible, $p ^ { + } \propto G _ { D } ^ { T }$

The other cases are proved in similar fashion.

## References

<sup>w</sup> <sup>x</sup> 1 T. Colburn, Defeasible reasoning and logic programming, Minds and Machines 1 1991 417–436.Ž .

<sup>w</sup> <sup>x</sup> 2 J. Conklin, M.L. Begemena, gIBIS: A tool for all reasons, J. Am. Soc. Information Systems 40 1989 140–152.Ž .

<sup>w</sup> <sup>x</sup> 3 J. Delgrande, An approach to default reasoning based on a first-order conditional logic: revised report, Artif. Intell. 36 Ž . 1988 63–90.

<sup>w</sup> <sup>x</sup> 4 H. Geffner, Default Reasoning: Causal and Conditional Theories. MIT, Cambridge, MA, 1992.

<sup>w</sup> <sup>x</sup> 5 M. Ginsberg, AI and nonmonotonic reasoning, in: D. Gabbay, C. Hogger Eds. , Handbook of Logic for ArtificialŽ . Intelligence and Logic Programming, Vol. III, Oxford Univ. Press, Oxford, 1994.

<sup>w</sup> <sup>x</sup> 7 S. Kimbrough, An introduction to the method of sweeping presumptions for modeling nonmonotonic reasoning, in: J. Nunamaker Ed. , Proc. 24th Annu. Int. Conf. on SystemŽ . Sci., Vol. III, IEEE Computer Soc. Press, 1991, pp. 339–348.

<sup>w</sup> <sup>x</sup> 8 R. Loui, Defeat among arguments: a system of defeasible inference, Comput. Intell. 3 1987 100–106.Ž .

<sup>w</sup> <sup>x</sup> 9 J. McCarthy, Circumscription—a form of non-monotonic reasoning, Artif. Intell. 13 1980 27–39.Ž .

<sup>w</sup> <sup>x</sup> 10 J. McCarthy, Applications of circumscription to formalizing common sense knowledge, Artif. Intell. 28 1986 89–116.Ž .

<sup>w</sup> <sup>x</sup> 11 D. McDermott, J. Doyle, Non-monotonic logic I, Artif. Intell. 13 1980 41–72. Ž .

<sup>w</sup> <sup>x</sup>12 R. Moore, Possible-worlds semantics for autoepistemic logic, in: Proceedings of the 1984 Non-monotonic Reasoning Workshop, Menlo Park, CA, 1984, AAAI.

<sup>w</sup> <sup>x</sup> 13 D. Nute, Basic defeasible logic, in: L. Farinas del Cerro, M.˜ Penttonen Eds. , Intensional Logics for Programming, Ox-Ž . ford Univ. Press, Oxford, 1992.

<sup>w</sup> <sup>x</sup> 14 D. Nute, Inference, rules, and instrumentalism, Int. J. Expert Systems Res. Applications 5 1993 267–274.Ž .

<sup>w</sup> <sup>x</sup> 15 D. Nute, A decidable quantified defeasible logic, in: D. Prawitz, B. Skyrms, D. Westerstahl Eds. , Logic, Methodol-Ž . ogy and Philosophy of Science IX, Elsevier, New York, 1994, pp. 263–284.

<sup>w</sup> <sup>x</sup> 16 D. Nute, Defeasible logic, in: D. Gabbay, C. Hogger Eds. ,Ž . Handbook of Logic for Artificial Intelligence and Logic Programming, Vol. III, Oxford Univ. Press, Oxford, 1994.

<sup>w</sup> <sup>x</sup> 17 D. Nute, K. Erk, Defeasible logic graphs for decision support, in: Proceedings of the 29th Hawaii International Conference on System Science, Vol. II, IEEE Comput. Soc. Press, Washington, 1996, pp. 11–19.

<sup>w</sup> <sup>x</sup> 18 D. Nute, C. Henderson, Z. Hunter, d-Graph: an argument-Based system incorporating defeasible graphs, in: Proc. 30th Hawaii Int. Conf. on System Sci. IEEE Comput. Soc. Press, Washington, 1997.

<sup>w</sup> <sup>x</sup> 19 D. Nute, C. Henderson, Z. Hunter, Defeasible logic graphs: II. Implementation, Decision Support Systems, Decision Support Systems, this issue.

<sup>w</sup> <sup>x</sup> 20 J. Pearl, H. Geffner, Probabilistic semantics for a subset of default reasoning. Technical Report TR-93-III, Cognitive Systems Laboratory, UCLA, 1988.

<sup>w</sup> <sup>x</sup> 21 J. Pollock, A theory of defeasible reasoning, Int. J. Intell. Systems 6 1991 33–54.Ž .

<sup>w</sup> <sup>x</sup> 22 R. Reiter, A logic for default reasoning, Artif. Intell. 13 Ž . 1980 81–132.

![](/api/attachments/X5D4GNM5/fulltext/images/e3e41ee8c4394d65578ed1fdcdae1dae3af27d62c42afcd83ac33fab217cd554.jpg)

Dr. Donald Nute is Director of the Artificial Intelligence Center and Head of the Department of Philosophy at the University of Georgia. He has authored, co-authored, or edited approximately one-hundred books and papers on philosophy, logic, and artificial intelligence including Topics in Conditional Logic, Essential Formal Semantics, Prolog Programming in Depth with Michael Ž Covingon and Ande’ Vellino, and De-. feasible Deontic Logic ed. . A frequent Ž .

speaker at universities and conferences in Europe and North America, he has held visiting positions at the Universities of Stuttgart, Tuebingen, and Antwerp, and directed AI projects funded by NSF, EPA, USDA Forest Service, and Lockheed. His research interests include logic programming and knowledge representation.

![](/api/attachments/X5D4GNM5/fulltext/images/3322bf80c8b22f7fc7167dea17893359c2997878f81514fce40ab0f3f82b2042.jpg)

Katrin Erk received support from the Deutscher Akademischer Austauschdienst to study artificial intelligence at the University of Georgia while working on a degree in computer science at the University of Koblenz-Landau.
