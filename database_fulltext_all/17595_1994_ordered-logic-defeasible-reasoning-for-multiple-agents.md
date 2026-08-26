---
otero_id: 17595
otero_key: "4UU4NJNP"
title: "Ordered logic: defeasible reasoning for multiple agents"
authors: "P Geerts; D Vermeir; D Nute"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90030-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ordered logic: defeasible reasoning for multiple agents $^{1}$

P. Geerts and D. Vermeir

University of Antwerp, Antwerpen, Belgium

D. Nute

The University of Georgia, Athens, GA, USA

Our goal is to provide a theoretical foundation for knowledge based applications which support nonmonotonic or defeasible reasoning and which incorporate the knowledge of multiple experts in a principled way. We present a generalized proof theory for defeasible reasoning and briefly explain the relationship of this system to other nonmonotonic formalisms. Then we present a proof theory and semantics for a logic that allows us to explicitly model internal perspectives or multiple agents. This ordered logic properly extends defeasible logic by allowing more complex precedence structure on rules. It provides a mechanism for resolving conflicts between competing perspectives without obscuring the opinions of those perspectives. We show which defeasible theories can be transformed into an equivalent theory in the new logic for multiagent reasoning and how a theory in the logic for multiagent reasoning can be transformed into an equivalent set of defeasible theories, one for each perspective or agent. We present a proof theory for quantified ordered logic and introduce the concept of a curtain which shields the cognitive resources of one agent from another agent. Finally, we consider some examples and discuss how it is possible to specify the relative superiority of some experts over others in a natural way using ordered logic.

Keywords: Defeasible reasoning; Multiple experts; Non-monotonic logic; Ordered logic.

## 1. Introduction

Many knowledge based expert systems or decision support systems with a knowledge based component rely on classical logic. Classical logic is monotonic, meaning that a conclusion p is always derivable from a theory T if it is derivable

![](/api/attachments/4UU4NJNP/fulltext/images/c706b322c08f7acb23468c21e8184e74d7d8057887810be9ebadf0a06e3fee10.jpg)

Donal Nute received a B.S. in philosophy and mathematics from the University of Kentucky in 1969 and the Ph.D. in philosophy from Indiana University in 1974. He is Head of the Department of Philosophy and Director of Artificial Intelligence Programs at the University of Georgia. His research interests include philosophical logic, logic programming, automated reasoning, expert systems, and decision support systems. He has held visiting research positions at the Universities of Stuttgart and Tübingen in Germany and at the University of Antwerp in Belgium. He has published more than seventy books, book chapters, journal articles, and reports on philosophical logic and artificial intelligence including Prolog Programming in Depth (Scott, Foresman and Company, 1988) co-authored with Michael Covington and André Vellino. He is President of AI Associates, Inc., a consulting firm that has developed AI applications for industry since 1988.

![](/api/attachments/4UU4NJNP/fulltext/images/0b1591928bb1bfd91c1d5b1a7ee73992663d2273cfd229ec083911ba9daac107.jpg)  
clarative user interface design.

Dirk Vermeir is Professor in the department of Mathematics and Computer Science at the University of Antwerp. His current research interests include the theoretical development and application of non-classical logics in computer science, focusing on the semantics of deductive and object-oriented knowledge base formalisms. He is the author of over 60 scientific papers in the areas of formal languages, semantic data models, nonmonotonic logic and de-design.

![](/api/attachments/4UU4NJNP/fulltext/images/4aef656e1737cb81e2f151d0f6eea20e6681b412a72a3e9cdd3a704dbc132c06.jpg)

Patricia Geerts is teaching Assistant and PhD Candidate in the department of Mathematics and Computer Science at the University of Antwerp. Her research interests include non-classical logics and their applications in logic programming, automated reasoning and expert systems.

from any subtheory of T. Human reasoning, on the other hand, is notoriously nonmonotonic. It is often necessary to draw conclusions based on incomplete information because the complete evidence is difficult to obtain or because of constraints on time. The best conclusion that can be drawn from incomplete information may be quite different than the conclusion that would be drawn from complete information. Policies for drawing conclusions based on available information are often incorporated into so-called default rules. Examples include “Italian food is delicious”, “Trains run on time in Germany”, and “American cars use a lot of gasoline”. Another source of nonmonotonicity in reasoning is normative rules like “Vehicles should stop at red lights” or “Promises should be kept”. All of these rules have exceptions, and we will withdraw the conclusions we reach using these rules if we acquire new evidence that indicates we are dealing with an exception to a rule.

Alternatives to classical logic include numerical methods for handling uncertainty, frame based systems with default rules, and inheritance-with-exceptions reasoners. The difficulty in eliciting numerical certainty factors from domain experts and in maintaining systems that depend on these methods is well known. Furthermore, many of the numerical methods actually in use have been developed as ad hoc attempts at solving the problem of nonmonotonic reasoning and do not have the firm foundation in probability theory that one might first assume. Much of the work on frame based systems and inheritance-with-exceptions reasoners also lacks a theoretical foundation. Recent work by Touretzky (1986) and others addresses this lacuna for inheritance systems, but the fact remains that such systems are severely limited in the kind of knowledge they can be used to represent.

A number of nonmonotonic formalisms have been developed which provide a nonnumerical foundation for nonmonotonic reasoning systems. Several of these are discussed in section 2. These typically are based on a robust formal language that has at least the expressive power of frame based systems or inheritance systems. Many are extensions of first-order classical logic (FOL). FOL is not decidable, meaning that there is no algorithm for deciding whether a particular result is derivable from a set of assumptions. The consequences derivable in FOL from a set of assumptions is not recursive but only recursively enumerable. Such systems are called semidecidable. Unfortunately, nonmonotonic extensions of semidecidable systems are not themselves even semidecidable.

For applications, decidability is obviously an important property of an inference system. In logic programming generally and nonmonotonic logic programming specifically, one reasonable approach is to look for interesting decidable fragments of larger, undecidable systems. Horn clause logic is an example of an interesting and useful fragment of FOL. It is the foundation for pure Prolog (Prolog without cut and negation-by-failure). Nute (1991) has described a family of decidable nonmonotonic systems in which defaults have a Horn-like structure.

While useful nonmonotonic formalisms are available, they typically do not address issues that arise when we want to incorporate the knowledge of several experts into our applications in a principled way. When we try to represent the knowledge of several experts in a single system, each expert has his own perspective on the relevant domain, and this difference in perspectives can lead to different conclusions. Even where knowledge of a single person is involved, a decision maker often has to take several conflicting perspectives into account when drawing conclusions on a certain body of evidence. One approach to representing multiple perspectives is to determine where conflicts arise and resolve them before building the knowledge representation. On this approach the differences in perspectives are lost in the representation. Another approach is to present the conclusions of all perspectives, leaving it to the user to make final decisions. The best approach is a system that resolves differences and makes an overall recommendation in at least some cases, but that can also recover the viewpoints of the individual perspectives. In such a system, the conclusions drawn from a given perspective are defeasible and may be retracted when other perspectives are taken into account.

Examples of conflicting perspectives include conflicts between short- and longterm strategies or between strategies with different goals, such as situations where we might say, "As your teacher I must require you to hand in all assignments in this course, but as your friend I advise you to forget about the project for this class, take the lower grade, and concentrate on your other classes where you are in danger of failing." Although it is possible to represent such conflicting perspectives as ordinary default rules in a single theory, this distorts the reality that there are really two different perspectives each of which leads to its own conclusions. We have the instructor's perspective and the friendly advisor's perspective. It may be helpful to derive the conclusions of each of the single perspectives even if there is not an overall conclusion that can be drawn in a particular case.

In what follows, we situate our logic for reasoning with multiple perspectives in the class of nonnumerical nonmonotonic formalisms (section 2). We present a proof theory for a single-perspective defeasible logic (section 3) and a proof theory and semantics for a logic for representing multiple perspectives (sections 4, 7, 8 and 9). In section 6, we give a technical exploration of the relationship between these two logics, showing how the former can be modeled in the latter in a principled way if certain requirements are satisfied. This permits us to model experts using a single-perspective defeasible logic where much of the inferential structure is implicit, and then embed this structure into a multiple-expert representation with an explicit structure for both the defaults used by each individual expert and the relative superiority of the different experts in the system. This lets us represent in a single ordered theory what is represented in defeasible logic by a family of theories. Section 10 introduces a proof theory for a quantified version of our logic, where each ground literal can be thought of as a propositional constant. Although our system is basically developed to incorporate knowledge of several perspectives without obscuring their opinions, we show in section 5 that it can also support intuitively correct reasoning about some well-known problems of commonsense reasoning involving single agents which cause problems for many other systems. In particular, we show how our system can be used to solve the Yale Shooting Problem and problems dealing with inheritance with exceptions. Furthermore, we suggest a way to attack the Qualification Problem. In section 11, we introduce the concept of a curtain which shields the information of one agent from others. These curtains offer interesting applications to problems involving multiple agents. Finally, section 12 briefly discusses how knowledge of different experts can be combined, specifying the relative superiority of some experts over others.

## 2. Approaches to nonmonotonic logic

Much recent work on nonmonotonic formalisms divides roughly into three different approaches which we call the minimalist approach, the fixpoint approach, and the defeasible approach. The system of nonmonotonic inference for multiple-expert systems that we develop here is of the defeasible variety. We will take a brief look at some important differences between the defeasible approach to nonmonotonic reasoning and the other two approaches.

The minimalist approach looks at the models of a classical theory that are minimal with respect to some set of predicates that occur in the theory (McCarthy, 1980, 1986; Lifschitz, 1985, 1986; Bossu and Siegel, 1985). For example, we know that birds typically fly, that penguins do not fly, and that penguins are birds. Introducing a new predicate “Abnormal”, we could represent these three principles in classical logic as:

$$
\begin{array}{l} (\forall x) (\text { Bird } (x) \& \neg \text { Abnormal } (x) \supset \text { Fly } (x)) \\ (\forall x) (\text { Penguin } (x) \supset \neg \text { Fly } (x)) \\ (\forall x) (\text { Penguin } (x) \supset \text { Abnormal } (x)) \\ (\forall x) (\text { Penguin } (x) \supset \text { Bird } (x)) \end{array}
$$

We add facts about birds and penguins to this set of rules (e.g., “Bird(tweety)” and “Penguin(opus)”), then minimize with respect to the property “Abnormal”. In the resulting model, only those individuals are abnormal that could be shown to be abnormal in the theory – in this case, only Opus. So Tweety is a bird that is not abnormal in this model, and hence Tweety must fly to satisfy the first sentence in the theory.

Fixpoint formalisms include McDermott's and Doyle's (1980) nonmonotonic logic, Reiter's (1980) default logic, and autoepistemic logic (Moore, 1984, 1985; Konolige, 1988). Default rules in these systems involve a special condition just as the rules in minimalist systems do, but the role of these conditions is explained in the proof theory rather than in the semantics. The rule that birds fly, for example, would become something like:

$$
(\forall x) (\operatorname{Bird} (x) \& M (\operatorname{Fly} (x)) \supset \operatorname{Fly} (x))
$$

Here we understand “ $M(\text{Fly}(x))$ ” as stating a requirement that “ $\text{Fly}(x)$ ” is consistent with the conclusions that we draw. When rules conflict, the conclusions we draw (and what will be consistent with them) will depend on which of the rules we decide to use. This roughly corresponds to the order in which we apply the rules. By applying rules, in whatever order we wish, we eventually arrive at a fixpoint where we can reach no new conclusions through further application of the rules. Some rules may become blocked along the way because they require that some proposition should be consistent with our conclusions and we earlier applied another rule that contradicts this proposition. Fixpoint theories may impose additional conditions on what counts as a legitimate fixpoint.

At a fixpoint, every default of a theory is either inapplicable or applied. That is, if all the conditions of the default are in the fixpoint, then the consequent of the default is also in the fixpoint. Similarly, every default of a theory is either inapplicable or applied in every minimal model. If all the conditions of the default are true in a minimal model, then the consequent of the default is also true. We notice that a single theory might have more than one fixpoint. Similarly, a single theory might have more than one minimal model. Where there is more than one fixpoint or minimal model, we could adopt either a credulous or a skeptical strategy. The credulous strategy is to accept one of the fixpoints or minimal models until forced by further information to reject it. The skeptical strategy is to accept only those propositions contained in the intersection of the fixpoints or minimal models.

The defeasible approach (Touretzky, 1986; Horty et al., 1987; Loui, 1987a,b,c; Geffner, 1988, 1989; Geffner and Pearl, 1989; Nute, 1988, 1990, 1991) is basically a proof-theoretic approach, but it treats defaults quite differently from the fix-point approach. On the defeasible approach, we can have a consistent theory that contains a default or defeasible rule, the antecedent condition of the rule, and the negation of the consequent of the rule. For example, a theory containing

$$
(\forall x) (\operatorname{Bird} (x) \Rightarrow \operatorname{Fly} (x))
$$

Bird(tweety)

$\neg$ Fly(tweety)

would be consistent. Thus, the symbol $\Rightarrow$ does not represent material implication as $\supset$ does on both the minimalist and the fixpoint approaches. The order in which rules are applied makes no difference in a defeasible theory, and the proof theory generates a unique fixpoint which may be distinct from any fixpoint or minimal model generated in the corresponding fixpoint or minimalist treatment. This is accomplished by partially ordering the defeasible rules in the theory so conflicts between conflicting rules can be resolved. Where conflicts remain unresolved by this partial ordering of rules, the skeptical strategy is employed, no conclusion is drawn, and the two rules are said to defeat each other.

The partial ordering of defeasible rules in a single-perspective system is usually implicit and based on some notion of specificity. In our multiple-perspective system, this partial ordering becomes explicit.

## 3. General defeasible logic

The defeasible theories we will consider are expressed in a two-tiered language. The first tier includes all the formulae of the language and the second tier contains all the rules.

A literal is a propositional constant or the negation of a propositional constant. Where p is a propositional constant, p and $\sim p$ are complements of each other. Where p is any literal, we denote the complement of p as $\neg p$ . A sentence is a literal or an expression of the form Ep where p is a literal. We read Ep as ‘Evidently, p’.

We assume three symbols $\rightarrow$ , $\Rightarrow$ , and $\rightsquigarrow$ distinct from each other and from all propositional constants. Where $A$ is a finite set of literals and $p$ is a literal, a strict rule is a triple $(A, \rightarrow, p)$ (denoted $A \rightarrow p$ ), a defeasible rule is a triple $(A, \Rightarrow, p)$ (denoted $A \Rightarrow p$ ), and a defeater is a triple $(A, \rightsquigarrow, p)$ (denoted $A \rightsquigarrow p$ ). We usually omit the set brackets when the antecedent set has only one member, and we usually omit an empty antecedent set altogether. Thus $\{p\} \rightarrow q$ is usually written $p \rightarrow q$ and $\emptyset \Rightarrow p$ is usually written $\Rightarrow p$ .

Defeaters are very weak rules often expressed in English as “might” conditionals, e.g., “Something that looks red under red light might not be red.” Defeaters never directly support inferences.

For example, we cannot use our defeater to conclude that something is not red because it looks red under red light. Instead, defeaters are used only to defeat rules that we might otherwise apply, such as the rule “Something that looks red is red”. We note that strict and defeasible rules may act as defeaters, but they also support inferences. Pollock (1987) discusses different kinds of defeaters in some detail. $^{2}$

Definition 1 A defeasible theory is a pair $(R, K)$ where R is a recursive set of rules (strict rules, defeasible rules, and defeaters) and K is a recursive set of literals.

Definition 2 A superiority relation is a partial order $\leq$ on the set of all rules such that

(1) if $A \to p$ , $\pi \in R$ , then $\pi \leq A \to p$ ;

(2) if $A \to p$ , $B \Rightarrow q \in R$ ,

$$
\text { then } A \to p \not \leqslant B \Rightarrow q; \text { and }
$$

(3) if $A \to p$ , $B \rightsquigarrow q \in R$ , then $A \to p \not\leq B \rightsquigarrow q$ . Where $\pi$ and $\pi'$ are rules and $\leq$ is a superiority relation, we will write $\pi < \pi'$ just in case $\pi \leq \pi'$ , but $\pi' \not\leq \pi$ .

For any superiority relation, every strict rule is strictly superior to every defeasible rule and every defeater. We can use a superiority relation to determine which if either of two defeasible rules to apply in a theory when the two rules have contradictory consequents. $A \Rightarrow p$ says that, other things being equal, we should accept p whenever we accept every member of A. Of course, it is the “other things being equal” that causes the problems. We could also say that in typical or normal cases where every member of A is true, so is p. But we can and often do adopt conflicting rules $A \Rightarrow p$ and $B \Rightarrow \neg p$ , where it is possible that everything in both A and B is true. Such conflicts can only be resolved if we give one of the rules precedence over the other. One might interpret this as meaning that one rule is more reliable than the other, but that is not the interpretation we intend. Suppose $A \Rightarrow p$ has precedence over $B \Rightarrow \neg p$ . This does not mean that $A \Rightarrow p$ is more reliable than $B \Rightarrow \neg p$ in the sense that we are better justified in adopting $A \Rightarrow p$ than we are in adopting $B \Rightarrow \neg p$ . Each rule could be the very best possible rule for the case where its condition is satisfied, “all other things being equal”. It is just that when A and B are both satisfied, all things aren’t equal where B is concerned. A situation where A and B are both satisfied may not be a typical or normal situation in which B is satisfied.

As the rules in our logic may be defeated, our inference mechanism will be more complicated than in monotonic logics where a simple iterative procedure yields conclusions which remain true no matter what deductions are performed next. We will avoid using rules that may later turn out to be defeated by restricting application to those rules that will definitely not be defeated. For any rule that is applied, the proof theory will first require that we show that no potential defeater is applicable. This is done by not only inferring positive conclusions like “p holds” (denoted as $p^{+}$ ) but also negative ones like “demonstrably, p does not hold” (denoted as $p^{-}$ ).

Definition 3 Let $(R, K)$ be a defeasible theory and let $\leq$ be a superiority relation. Where $p$ is a sentence and $s$ is + or -, a proof tree for $p^s$ in $(R, K)$ using $\leq$ is a finite tree where each node is labeled $q^t$ , where $q$ is a sentence and $t$ is + or -, such that the root is labeled $p^s$ and each node $m$ is labeled by an adorned sentence $l$ satisfying one of the following conditions:

(D1) $l = p^{+}$ and either $p \in K$ or there is $A \to p \in R$ such that for each $a \in A$ , $m$ has a child node labeled $a^{+}$ .

(D2) $l = p^{-}, p \notin K$ , and for every rule $A \to p \in R$ , there is $a \in A$ and a child node of $m$ labeled $a^{-}$ .

(D3) $l = Ep^{+}$ and either $m$ has a child node labeled $p^{+}$ or there is $\pi \in R$ , where $\pi = A \to p$ or $\pi = A \Rightarrow p$ , such that

(D3.1) for every $a \in A$ , $m$ has a child node labeled $Ea^{+}$ ,

(D3.2) for every rule $\pi' \in R$ with antecedent $B$ and consequent $\neg p$ , either $\pi' < \pi$ or there is $b \in B$ and a child node of $m$ labeled $Eb^{-}$ , and

(D3.3) $m$ has a child node labeled $\neg p^{-}$ .

(D4) $l = Ep^{-}$ , $m$ has a child node labeled $p^{-}$ , and for every $\pi \in R$ , where $\pi = A \to p$ or $\pi = A \Rightarrow p$ , either

(D4.1) there is $a \in A$ and a child node of $m$ labeled $Ea^{-}$ ,

(D4.2) there is a rule $\pi' \in R$ with antecedent $B$ and consequent $\neg p$ such that $\pi' \neq \pi$ and for every $b \in B$ , $m$ has a child node labeled $Eb^{+}$ , or

(D4.3) $m$ has a child node labeled $\neg p^{+}$ .

We write $(R, K)|_{\leq}p^{s}$ just in case there is a proof tree for $p^{s}$ in $(R, K)$ using $\leq$ . We call the logical formalism defined by this proof theory GDL for general defeasible logic. $^{3}$ Billington (1989) shows that if there is a proof tree for $p^{+}$ in $(R, K)$ using $\leq$ , then there is no proof tree for $p^{-}$ in $(R, K)$ using $\leq$ ; and if there is a proof tree for $Ep^{+}$ in $(R, K)$ using $\leq$ , then there is no proof tree for $Ep^{-}$ in $(R, K)$ using $\leq$ . However, we can have a theory $(R, K)$ , a literal p and a superiority relation $\leq$ such that there exists neither a proof tree for $p^{+}$ in $(R, K)$ using $\leq$ nor a proof tree for $p^{-}$ in $(R, K)$ using $\leq$ .

Definition 4 Let $D$ be a defeasible theory and $\leq$ a superiority relation. We say that $\leq$ is decisive for $D$ if for each literal $p$ , either $D|_{\leq}Ep^{+}$ or $D|_{\leq}Ep^{-}$ .

Various natural principles can be used to determine a superiority relation. Probably the most commonly used are specificity principles of one kind or another. Four specificity principles discussed in Nute (1989) are strict specificity, naive specificity, defeasible specificity, and intact defeasible specificity. $^{4}$ These specificity principles can be defined in terms of the rules in the theory, and special proof theories can be developed that incorporate demonstrations of the superiority of rules into the proofs (Nute, 1988, 1990). Both GDL and special defeasible logics that depend on specificity principles have been implemented as defeasible extensions of Prolog (Nute and Lewis, 1986).

## 4. Ordered theories

Definition 5 An ordered theory is a tuple $(\Sigma, \leq, R, f)$ where

(1) $(\Sigma, \leq)$ is a finite partially ordered set of nodes or perspectives

(2) $R$ is a finite set of defeasible rules, and

(3) $f: \Sigma \to \rho(R)$ is a function assigning a set of rules to each node in $\Sigma$ .

The partial order on the nodes in an ordered theory will determine the precedence of the rules at the nodes. Another way of looking at the partial order is as an “influence” relation between perspectives. If $\alpha$ , $\beta$ and $\gamma$ are perspectives in $\Sigma$ with $\alpha \leq \gamma$ and $\beta \leq \gamma$ , then $\gamma$ is a perspective that is influenced by perspectives $\alpha$ and $\beta$ .

Typically, there will be a top perspective $\top$ such that $\alpha \leq \top$ for all perspectives $\alpha \in \Sigma$ . $\top$ can be regarded as the final consolidation of all perspectives in the theory. Similarly, there may be a unique bottom node.

Since each node in an ordered theory can represent a distinct perspective, different conclusions will normally be derivable at different nodes. The final integrated conclusions of the theory are the ones that hold in the unique top node or perspective (if any).

Definition 6 Let $(\Sigma, \leq, R, f)$ be an ordered theory. Where $p$ is a literal and $s$ is $+$ or $-$ , a proof tree for $p^s$ at a perspective $\alpha$ in $(\Sigma, \leq, R, f)$ is a finite tree where each node is labeled $q^t$ , where $q$ is a literal and $t$ is $+$ or $-$ , such that the root node of the tree is labeled $p^s$ and each node $m$ is labeled by an adorned literal $l$ satisfying one of the following conditions:

(C1) $l = p^{+}$ and there exists $A \Rightarrow p \in f(\beta)$ , where $\beta \leq \alpha$ , such that

(C1.1) for each $a \in A$ , $m$ has a child node labeled $a^{+}$ , and

(C1.2) for each $B \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \leq \alpha$ and $\gamma \neq \beta$ , there is $b \in B$ and a child node of $m$ labeled $b^{-}$ .

(C2) $l = p^{-}$ and for each $A \Rightarrow p \in f(\beta)$ , where $\beta \leq \alpha$ , either

(C2.1) there is $a \in A$ and a child node of $m$ labeled $a^{-}$ , or

(C2.2) there is $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha, \gamma \not\prec \beta$ , such that for each $b \in B$ , $m$ has a child node labeled $b^{+}$ .

Condition (C1) expresses defeasible rule application: a rule can be applied at $\alpha$ only if its antecedent holds and it is not defeated by an applicable competing rule. Condition (C2) states that we can show that a literal doesn't hold if all rules that could conclude it are either not applicable or defeated by a competing rule. $^{5}$

Intuitively, the existence of a proof tree of $p^{+}$ at a perspective $\alpha$ in T means that p is provable at $\alpha$ in T. The existence of a proof tree of $p^{-}$ at perspective $\alpha$ in T means that we can show that p cannot be proven at $\alpha$ in T. We write $T|_{\overline{\alpha}}p^{s}$ whenever there is a proof tree t for $p^{s}$ at perspective $\alpha$ in T. The position of the perspective in an ordered theory plays the role of the superiority relation in a general defeasible theory.

Example 1 Consider the ordered theory ( $\{\alpha, \beta, \gamma\}, \leq, R, f$ ) where $\gamma < \beta < \alpha$ , $f(\alpha) = \{\Rightarrow p\}$ , $f(\beta) = \{\Rightarrow r, p \Rightarrow \neg q\}$ , and $f(\gamma) = \{r \Rightarrow q\}$ . $\neg q$ holds at $\alpha$ since $p \Rightarrow \neg q$ at $\beta$ is applicable at perspective $\alpha$ and all rules at or below $\alpha$ with consequent $q$ are weaker (i.e., at a perspective below $\beta$ ). However $q$ holds at $\beta$ , since the rule $r \Rightarrow q$ at $\gamma$ is applicable at $\beta$ while its competing rule $p \Rightarrow \neg q$ is not. In terms of agents, we can say that $\alpha$ is in a position to use the rules available at $\beta$ to overrule $\beta$ 's conclusion that $q$ because $\alpha$ is in possession of information represented by $\Rightarrow p$ that $\beta$ lacks.

Example 2 Consider the ordered theory ( $\{\alpha, \beta, \gamma\}, \leq, \{\Rightarrow p, \Rightarrow \neg p, p \Rightarrow q\}, f$ ) with $\beta < \alpha$ , $\gamma < \alpha$ , $f(\alpha)=\emptyset,\quad f(\beta)=\{\Rightarrow p,p\Rightarrow q\},\quad\text{and}\quad f(\gamma)=\{\Rightarrow\neg p\}.$ p and q hold at $\beta$ where q is obtained by applying $p\Rightarrow q$ . However, the condition that p used to derive q at $\beta$ does not hold at $\alpha$ since it is defeated by $\Rightarrow\neg p$ at $\gamma$ . Rule $p\Rightarrow q$ is therefore not applicable at $\alpha$ , and q cannot be proven at $\alpha$ .

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
α  $\bigcirc$ $\Rightarrow p$ 
β  $\bigcirc$ $\Rightarrow r, p \Rightarrow \neg q$ 
γ  $\bigcirc$ $r \Rightarrow q$ 
Example 1
α  $\bigcirc$ 
β  $\bigcirc$ $\gamma$ $\Rightarrow p \Rightarrow \neg p$ 
p  $\Rightarrow q$ 
Example 2
</div>

Lemma 1 If $T$ is an ordered theory, then not both $T|_{\alpha}p^{+}$ and $T|_{\alpha}p^{-}$ . $\square$

This shows that $\vdash_{\alpha}$ is well-behaved, and we can without any possibility of contradiction interpret $T\vdash_{\alpha}p^{+}$ as saying that p is derivable at $\alpha$ in T and $T\vdash_{\alpha}p^{-}$ as saying that demonstrably, p is not derivable at $\alpha$ in T. The converse of this Lemma doesn't always hold, as is illustrated by the following example.

Example 3 Consider the ordered theory $(\{\alpha\},\emptyset, \{\Rightarrow p, p \Rightarrow \neg p\},f)$ with $f(\alpha)=\{\Rightarrow p, p \Rightarrow \neg p\}$ . $p$ doesn't hold at $\alpha$ (there exists no proof tree of $p^{+}$ at $\alpha$ ), but we cannot show that $p$ doesn't hold (there is no proof tree of $p^{-}$ at $\alpha$ ).

Lemma 1 has the following corollary:

Corollary 1 No proof tree for any perspective in any ordered theory contains both a node labeled $p^{+}$ and a node labeled $p^{-}$ .

Lemma 2 If $T$ is an ordered theory, then not both $T|_{\alpha}p^{+}$ and $T|_{\alpha}\neg p^{+}$ . $\square$

The depth of a proof tree is the number of nodes in a longest branch of the tree. For any ordered theory, we need only consider proof trees of depth no greater than the number of literals occurring in the theory.

Lemma 3 If $T$ is an ordered theory and there is a proof tree of $p^{s}$ at perspective $\alpha$ in $T$ , then there is a proof tree of $p^{s}$ at $\alpha$ in T with depth not exceeding N, where N is the number of propositional constants in T. ☐

From Lemma 3 we immediately obtain the following decidability result:

Theorem 1 There exists an algorithm which, for any ordered theory T, perspective $\alpha$ in T, and adorned literal $p^{s}$ , decides whether or not $T|_{\alpha}p^{s}$ . ☐

## 5. Using ordered logic to formalize commonsense reasoning

An acceptable nonmonotonic formalism must support intuitively correct reasoning about a wide range of examples of commonsense reasoning. In this section, we use ordered logic to formalize some examples of commonsense reasoning that are known to cause problems for some other nonmonotonic systems. In ordered logic some rules can be declared to be superior to other rules. In this way conflicts between competing rules can be resolved, yielding a unique, intuitively correct extension, whereas the same competing rules would result in corresponding competing multiple extensions in some other systems.

To formalize temporal reasoning, a logic system must be able to express the knowledge that most events do not affect the truth of most facts under most circumstances, or, in other words, to represent the persistence of “normal” facts across the occurrence of “normal” events. This is called the Persistence Principle (PP), or Law of Inertia. However, some events interfere with the persistence of some facts. This suggests that we need a nonmonotonic system for this formalization. The problem with the logics of McCarthy (1980), McDermott (McDermott et al., 1980) and Reiter (1980) is that they have no criteria for deciding when to violate the Persistence Principle. All of these systems include a special condition in the antecedent of each nonmonotonic rule. Causal principles which require that some facts change from one event to the next, compete with PP. To preserve the causal principle, either we can override PP at the time the causal principle is applied, or we can override PP earlier, thus preventing satisfaction of one of the conditions of the causal principle. Minimalization gives us a choice, while defeasible logics require us to postpone violation of any defeasible principle until as late in a line of argument as possible. As we shall see, this feature of defeasible proof theory mirrors our intuition about temporal reasoning.

The Yale Shooting Problem is a simple example. A potential murderess loads her gun, waits for her intended victim to arrive, then points the gun at her victim and fires. Is the victim alive or dead at the end of the story, assuming the murderess has deadly aim?

Before we use ordered logic to solve the Yale Shooting Problem, we will start with the formalization of this problem as suggested by Hanks and McDermott (Hanks et al., 1987). We use variables p for properties or facts, e for events and s for situations, the property constants loaded, alive and dead, the event constants load, shoot and wait, a function symbol res and two predicate symbols h (holds) and ab. The formula $h(p,s)$ expresses the fact that p is true in situation s, $res(e,s)$ indicates the situation in which the effects of the occurrence of event e in situation s are reflected, and $ab(p,e,s)$ expresses the fact that p is abnormal with respect to event e occurring in state s. The Yale Shooting Problem can then be formalized by the following axioms:

$$
h (a l i v e, s _ {0})\tag{1}
$$

$$
h (\text { loaded }, \text { res } (\text { load }, s))\tag{2}
$$

$$
h (\text { loaded }, s) \rightarrow h (\text { dead }, \text { res } (\text { shoot }, s))\tag{3}
$$

$$
h (\text { loaded }, s) \rightarrow a b (\text { alive }, \text { shoot }, s)\tag{4}
$$

$$
h (p, s) \wedge \neg a b (p, e, s) \rightarrow h (p, r e s (e, s))\tag{5}
$$

Using these axioms to decide which facts hold after the occurrence of the events load, wait and shoot, the logics of McCarthy, McDermott and Reiter all derive two possible extensions: one in which the person under consideration is dead (the intuitively correct one), and one in which he is still alive. This second extension can be derived because it is possible to violate the persistence principle for the fact loaded during the occurrence of the event wait: the gun could cease to be loaded after waiting. Indeed, there is no way to express that abnormality should occur as late as possible.

In ordered logic, this problem can be solved by integrating the knowledge that an applicable causal principle must always defeat the Persistence Principle. However, the Persistence Principle must be applied whenever it is not defeated by a causal principle. This can be accomplished by declaring all causal principles to be superior to the persistence principle, as is shown in Example 4. Because we are working in the propositional version of ordered logic, we actually have to replace each rule in the example by a set of instances for the situations $s_0$ , res(load, $s_0$ ), res(wait,res(load, $s_0$ )) and res(shoot,res(wait,res(load, $s_0$ )), the events load, wait and shoot, and the property constants loaded and alive.

$$
\begin{array}{c} \boxed { \begin{array}{l} \circ \Rightarrow h (\text { alive }, s 0) \\ \quad \Rightarrow h (\text { loaded }, \text { res } (\text { load }, s)) \\ \circ h (\text { loaded }, s) \Rightarrow \neg h (\text { alive }, \text { res } (\text { shoot }, s)) \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \end{array} } \\ \circ h (p, s) \Rightarrow h (p, r e s (e, s)) \\ \hline \end{array}  \\ \text { Example   4 } \end{array}
$$

In this ordered theory, we can show that $\neg h(\text{alive},\text{res(shoot},\text{res(wait},\text{res(load},s_0))))$ holds at the top node of our theory, and we can also show that $h(\text{alive},\text{res(shoot},\text{res(wait},\text{res(load},s_0))))$ does not hold. Therefore, this theory supports the intuitively correct solution to the Yale Shooting Problem. In general, we handle persistence by putting a bottom node in our ordered theory where PP resides.

In commonsense reasoning problems dealing with inheritance with exceptions, we have to cope with contradictory rules resulting in ambiguity. These problems are as critical for evaluating non-monotonic systems as the Yale Shooting Problem, since some nonmonotonic systems fail to reach the right conclusion in cases where the ambiguity is not genuine, that is in cases where there is an intuitively correct solution based on the superiority between the conflicting rules.

An example of inheritance with exceptions where the ambiguity resulting from contradictory rules is not genuine involves the premises that Tweety is a penguin, all penguins are birds, penguins normally don't fly and birds normally do. Intuitively, the rule saying that penguins do not fly is superior to the rule about birds flying. However, nonmonotonic systems lacking the power to express superiority between rules provide no way to choose between the two competing rules; so that they yield two extensions: one in which Tweety flies, and one in which he does not. In ordered logic, however, we can express superiority between rules; so that this example can be easily formalized in an ordered theory yielding a unique extension in which Tweety does not fly. This is shown in Example 5, where we have to change the rules into instances for Tweety, if we are working in the propositional version.

$$
\begin{array}{c} \text {O} \Rightarrow \text {penguin(Tweety)} \\ \text {penguin(x)} \Rightarrow \text {bird(x)} \\ \text {O} \text {penguin(x)} \Rightarrow \neg \text {fly(x)} \\ \text {O} \text {bird(x)} \Rightarrow \text {fly(x)} \\ \hline \text {Example 5} \end{array}
$$

In cases where there is no way to choose between contradictory rules (that is when none of them is superior to the other), there is a genuine ambiguity which results in multiple extensions which are intuitively acceptable in the systems mentioned above. Because ordered logic is designed to be a skeptical system, always yielding a unique extension, the contradictory rules will have to defeat each other in case of genuine ambiguity. However, we can reflect this genuine ambiguity by putting each contradictory rule in his own perspective without any superiority relationship between these perspectives. The example shown below involves the premises that Nixon is both a Quaker and a Republican, Quakers are normally pacifists and Republicans are normally not pacifists. The ordered theory formalizing this example does not conclude whether Nixon is a pacifist or not, if we replace the rules by instances for Nixon.

![](/api/attachments/4UU4NJNP/fulltext/images/51372a1931d640d58e86fb77b63d974fcf3bb4aac0ca289345eba99f5fcf22f3.jpg)

Geerts (1991) has developed a fixed point procedure to derive so-called credulous extensions of theories like this. A credulous reasoner chooses to believe either p or $\neg p$ when presented with evidence for both and no way to resolve the conflict. In this example, the fixed point procedure will derive two extensions: one in which Nixon is a pacifist, and one in which he is a non-pacifist. The ability to generate credulous extensions of a theory is particularly interesting when accepting the disputed conclusion has further consequences.

Another problem frequently mentioned when treating inheritance reasoning with exceptions is the problem of preemption. Let us illustrate the notion of preemption by means of an example. Suppose that normally a computer science professor at a junior college is poor, even though computer science professors at junior colleges normally have a Ph.D. in computer science, and people who have a Ph.D. in computer science normally are not poor. Suppose also that ne'er-do-well, disinherited scions of wealthy families normally are poor, even though such individuals are clearly scions of wealthy families, and scions of wealthy families normally are not poor. If Fred is both a computer science professor at a junior college and a ne'er-do-well, disinherited scion of a wealthy family, we would intuitively conclude that Fred is poor. However, if we represent this knowledge in an inheritance network, we have to face the problem that none of the positive links to the property 'poor' is more specific than both negative links to the same property. To solve this problem, inheritance reasoners like SIR [Horty et al., 1987] impose the requirement that a compound path is permitted only when every conflicting path is preempted. More specific, SIR requires that a positive path is permitted provided only that the part up to the last link is permitted and for every negative link competing with the last link, either there is no permitted positive path up to its start node or there is another positive link such that there is a permitted path through the start node of this positive link ending in the start node of the negative link. Using this principle, we arrive at the conclusion that Fred is poor in the inheritance network resulting from the example.

We can translate this principle into ordered logic by making the restriction that a rule can only be defeated by a competing rule which is not itself defeated by a strict competitor (that is, by a defeater in a higher node). This preemption principle can easily be integrated into the proof theory for ordered logic.

Definition 6\* Let $(\Sigma, \leq, R, f)$ be an ordered theory. Where $p$ is a literal and $s$ is $+$ or $-$ , a proof tree for $p^s$ at a perspective $\alpha$ in $(\Sigma, \leq, R, f)$ is a finite tree where each node is labeled $q^t$ , with $q$ a literal and $t$ either $+$ or $-$ , such that the root is labeled $p^s$ and each node $m$ is labeled by an adorned literal $l$ satisfying one of the following conditions:

(C1) $l = p^{+}$ and there exists a rule $A \Rightarrow p$ at perspective $\beta$ , where $\beta \leq \alpha$ , such that

(C1.1) for each $a \in A$ , $m$ has a child node labeled $a^{+}$ , and

(C1.2) for each rule $B \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \leq \alpha$ and $\gamma \neq \beta$ , either there is $b \in B$ and a child node of $m$ labeled $b^{-}$ or there is $C \Rightarrow p \in f(\delta)$ , where $\delta > \gamma$ , such that for each $c \in C$ , $m$ has a child node labeled $c^{+}$ .

(C2) $l = p^{-}$ and for each rule $A \Rightarrow p \in f(\beta)$ , where $\beta \leq \alpha$ , either

(C2.1) there is $a \in A$ and a child node of $m$ labeled $a^{-}$ , or

(C2.2) there is $B \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \leq \alpha$ and $\gamma \neq \beta$ , such that for each $b \in B$ , there is a child node of $m$ labeled $b^{+}$ .

If we introduce the literals $p$ (poor), $a$ (computer science professors at junior colleges), $b$ (disinherited ne'er-do-well scions of wealthy families), $c$ (holders of a Ph.D. in computer science) and $d$ (scions of wealthy families), we can formalize the example in the following ordered theory.

![](/api/attachments/4UU4NJNP/fulltext/images/590cd2b607bc5f2892688207127f397828d901920a834aac120d8b7372a047bd.jpg)

The original proof theory would derive no conclusion about whether Fred is poor or not, while the proof theory with the preemption principle arrives at the intuitively correct conclusion that Fred is poor.

As is shown in Nute et al. (1991) the same approach can be followed to develop a special defeasible theory with the preemption principle. However, because of the existence of defeaters, this special defeasible theory has a problem that does not occur in ordered logic, as can be seen in the following example. We know that birds normally fly and that penguins normally don't. Because penguins are birds, this knowledge about penguins is superior to the knowledge about birds in general. We can also assume that a mutant penguin with unusually large wings might fly (a defcater). Suppose that Tweety is a mutant penguin. Using the special defeasible theory with preemption, we derive that Tweety can fly. The reason for this is that the defeater preempts the rule that penguins normally don't fly, so that there is no rule left to defeat the rule about birds flying. Intuitively, though, we are uncertain about such an animal's flight characteristics. We want its mutation to prevent our normal inference that as a penguin it cannot fly without reinstating our inference that as a bird it can fly. In ordered logic, this example can be formalized in the theory shown in Example 8. The proof theory for ordered logic with the preemption principle gives us the desired result: there is no conclusion about whether Tweety can fly or not.

$$
\begin{array}{c} \text {O} \Rightarrow p, \Rightarrow m \\ \Big | \quad p \Rightarrow b \\ \text {O} \{p, m \} \Rightarrow f, p \Rightarrow \neg f \\ \text {O} b \Rightarrow f \\ \hline \text {Example 8} \end{array}
$$

Ordered logic suggests a solution to the Qualification Problem. The Qualification Problem is concerned, not with the effects of a given event (like the Yale Shooting Problem), but with the conditions that must be satisfied to insure that a given effect will be produced. Suppose we want to start an automobile. To succeed, a great many conditions must be satisfied. There must be fuel in the tank, the battery must have sufficient charge, all of the wiring in the engine must be intact, the exhaust pipe must be unobstructed, etc. Checking to see if all of these conditions are satisfied before we put the key in the ignition is out of the question. So how do we represent the knowledge an automated reasoner needs to start automobiles?

We suggest that humans solve this problem with defeasible reasoning, a kind of “laziness”, and an ability to recover from failed plans. Humans employ simple, defeasible rules like “If you pump the gas a couple of times and turn the key in the ignition, the engine will start.” This rule will have many defeaters such as “If there is no fuel in the tank, the engine will not start.” Lacking specific information about the fuel tank, however, this defeater will be ineffective. But we suggest that humans don’t even consider whether they have specific information about any number of things that might defeat the rule about the engine starting. Somehow, these defeaters are compartmentalized so that they are only called into use at appropriate times. This is where ordered logic can be applied.

Suppose we have an ordered logic containing two nodes which we will call the car-starting node and the automotive-theory node. The car-starting node is a descendant of the automotive-theory node, as is every other node involving the functioning of automobiles. At the car-starting node, we have only our simple car-starting rule. Below that, we have a node where we store information about the car. The important feature of ordered logic that suggests the possibility for solving the Qualification Problem is that we can perform inferences at any node in the theory, not just at the top node. In particular, we can perform an inference at either the car-starting node or at the automotive-theory node. Since many more rules are accessible from the automotive-theory node, inferences performed here will take longer than inferences performed at the car-starting node. The “lazy” system will perform inferences about starting the car at the car-starting node. Only if these inferences fail to conform with observation will the system perform more expensive inferences at a higher and better-informed node.

If a system could be built using this suggestion, it would have several advantages apart from the obvious one of providing a partial model of human cognition to be tested and enhanced. Memory and time are two resources that constrain all inference and planning. Computational systems often conserve one of these resources by using more of the other. Ordered logic may provide a way of conserving both at the same time. Since one node with its rules may be accessible to many ancestor nodes, we do not need multiple copies of rules to represent various kinds of partitioning of knowledge into modules representing different contexts. Instead, we only represent the relations between nodes or perspectives. Further, we focus on the most specific context that fits a problem by performing all inferences at the lowest possible node in the system. This conserves time.

There are problems that must be worked out in actual systems if this approach to the Qualification Problem is to work. First, how do we decide at which node to perform an inference? Second, how do we move to the correct higher node to perform more precise reasoning when “lazy” reasoning fails? Additional mechanisms will have to be developed to perform these functions, but the foundation for the system would be an ordered theory of the sort described in this paper.

## 6. Relation between defeasible and ordered theories

We would like to convert defeasible theories into equivalent ordered theories. Obviously there is a simple way of doing this, at least for consistent defeasible theories, by creating an ordered theory with a single node and putting the rules $\Rightarrow p$ in that node for each literal p such that $Ep^{+}$ holds in the corresponding defeasible theory. However, the transformation algorithm we are interested in should preserve the structure of the original defeasible theory in some interesting way. We will describe this algorithm first.

Let $(R, K)$ be a defeasible theory and $\leq$ a superiority relation such that $(R, K)$ has a consistent, finite closure using $\leq$ . We will construct an equivalent ordered theory by assigning all the rules to a partially ordered structure of nodes. We will have a top node $\top$ such that $f(\top) = \{\Rightarrow p: (R, K)|_{\leq} \neg p^{+}\}$ . Because $(R, K)$ is consistent, there will be no literal $p$ such that both $(R, K)|_{\leq} p^{+}$ and $(R, K)|_{\leq} p^{+}$ , there will be no literal $p$ such that both $\Rightarrow p$ and $\Rightarrow \neg p$ are in $f(\top)$ , and thus no rule at $\top$ can be defeated. Furthermore, we will have a perspective $\alpha$ between perspective $\top$ and all the other perspectives such that $f(\alpha) = \{B \Rightarrow q: B \rightarrow q \in R\}$ . For each $A \Rightarrow p \in R$ , we will have a node $\alpha_{A \Rightarrow p}$ associated such that $f(\alpha_{A \Rightarrow p}) = \{A \Rightarrow p\}$ . We will also add $\alpha_{A \Rightarrow p} \leq_{o} \alpha_{B \Rightarrow q}$ to the partial order on the perspectives if $A \Rightarrow p \leq B \Rightarrow q$ . The trickiest part is the simulation of defeaters. We can achieve this by associating a node $\alpha_{C\to p}$ with each defeater $C\rightsquigarrow p$ with $f(\alpha_{C\to p}) = \{A\cup C\Rightarrow p: C\rightsquigarrow p$ and $A\Rightarrow \neg p$ in $R$ and $C\rightsquigarrow p\not\prec A\Rightarrow \neg p\}$ . We will add $\alpha_{C\to p} < _o$ $\alpha_{B\Rightarrow q}$ if $C\rightsquigarrow p < B\Rightarrow q$ .

$\leq_{o}$ incorporates the partial order on the set of rules in R restricted to pairs $\langle r_{1}, r_{2} \rangle$ where $r_{2}$ is not a defeater. Indeed, the reason why we need an order relation on rules is to determine which rule should be applied if both $r_{1}$ and $r_{2}$ are applicable. Because a defeater can never be applied, the only thing we have to know when $r_{1} < C \leadsto p$ is that $C \leadsto p \not\leftrightarrow r_{1}$ , so that $C \leadsto p$ is a candidate for defeating $r_{1}$ . This knowledge is preserved in the ordered theory resulting from the algorithm described above.

A rule $A \cup C \Rightarrow \neg p$ in a node $\alpha_{C \to \neg p}$ will be called a quasi-defeater, and the rule $A \Rightarrow p$ in $\alpha_{A \Rightarrow p}$ is the target rule for this quasi-defeater. The reason why we put the antecedent of a target rule into the antecedent of a quasi-defeater, is to make sure the quasi-defeater will never be applied. Indeed, for the rules $A \cup C \Rightarrow \neg p \in f(\alpha_{C \to \neg p})$ and $A \Rightarrow p \in f(\alpha_{A \Rightarrow p})$ , we know that $\alpha_{C \to \neg p} \not\prec_{o} \alpha_{A \Rightarrow p}$ and $\alpha_{A \Rightarrow p} \not\prec_{o} \alpha_{C \to \neg p}$ , so that both rules defeat each other when they are both applicable.

This algorithm does not yield an equivalent ordered theory for all defeasible theories. One of the problems is that however we try to simulate defeaters in ordered theories, it will always be the case that the rule we construct to take over the role of the defeater will be considered for application, while the defeater in the defeasible theory will never be considered for application. In any defeasible theory, a defeater is never applied, while in ordered theories, to show that a quasi-defeater is not applied, we have to show that it is not applicable (by showing that one of its antecedents does not hold), or that a competing rule (e.g. the target rule for this quasi-defeater) is applicable. It can be the case that none of these requirements is satisfied in the defeasible theory, for a quasi-defeater with consequent p. Even if it can be shown that a literal q of the antecedent of the quasi-defeater does not hold at the corresponding defeasible theory, it can be the case that every proof tree for $Eq^{-}$ contains a node labeled $Ep^{-}$ , as is illustrated in Example 9. In this example, there is a literal in the antecedent of the quasi-defeater that can be shown not to hold in the defeasible theory, while this can not be shown in the ordered theory. Similarly, it can be the case that the antecedent of the target rule holds at the defeasible theory, while there is a literal in the antecedent for which all proof trees contain a node labeled $Ep^{-}$ , as is shown in Example 10. In this example, there is a literal in the antecedent of the target rule that holds in the defeasible theory, while this can not be shown in the ordered theory.

Example 9 Consider the defeasible theory $D = (\{p \Rightarrow a, a \Rightarrow \neg p, \Rightarrow b, b \rightsquigarrow p\}, \emptyset)$ . Because there are no rules which could conclude $p$ in this theory, we know that $D|_{\leq} Ep^{-}$ , and therefore also that $D|_{\leq} Ea^{-}$ .

If we translate this defeasible theory into an ordered theory following the algorithm described above, we get the theory $O = (\{\top, \alpha, \alpha_{p \Rightarrow a}, \alpha_{a \Rightarrow \neg p}, \alpha_{\Rightarrow b}, \alpha_{b \rightarrow p}\}, \leq_o, \{\Rightarrow b, p \Rightarrow a, a \Rightarrow \neg p, \{a, b\} \Rightarrow p\}, f)$ , where no node is superior to node $\top$ and no node except $\top$ is superior to $\alpha$ . Furthermore, we have that $f(\top) = f(\alpha) = \emptyset$ , $f(\alpha_{p \Rightarrow a}) = \{p \Rightarrow a\}$ , $f(\alpha_{a \Rightarrow \neg p}) = \{a \Rightarrow \neg p\}$ , $f(\alpha_{\Rightarrow b}) = \{\Rightarrow b\}$ , and $f(\alpha_{b \rightarrow p}) = \{\{a, b\} \Rightarrow p\}$ . If we try to show that $p^{-}$ holds in this theory, we either have to show that the rule $\{a, b\} \Rightarrow p$ is not applicable at $\top$ , or that the rule $a \Rightarrow \neg p$ is applicable at $\top$ . Because it is obvious that $O|_{\top}b^{+}$ , this comes down to show that either $O|_{\top}a^{+}$ or $O|_{\top}a^{-}$ , but neither of them can be shown. The reason why the fact that $Ea^{-}$ holds in the defeasible theory is not reflected in the corresponding ordered theory, is that in the defeasible theory, the only proof tree for $Ea^{-}$ contains a node labeled $Ep^{-}$ , which causes looping when we try to build proof trees for $p^{-}$ or $a^{-}$ in the ordered theory. Therefore, the constructed ordered theory is not equivalent to the original defeasible theory.

![](/api/attachments/4UU4NJNP/fulltext/images/6e6f5c0de1409d58c1c48f66f2817cdfe81d86fcfdfb63a289e8be8bf4b40fe2.jpg)

Example 10 Consider the defeasible theory $D = (\{p \Rightarrow \neg a, a \Rightarrow \neg p, b \rightsquigarrow p, \Rightarrow a, \Rightarrow b\}, \emptyset)$ . Because there are no rules which could conclude $p$ in this theory, we know that $D|_{\leq} Ep^{-}$ , and therefore also that $D|_{\leq} Ea^{+}$ .

If we translate this defeasible theory into an ordered theory following the algorithm described above, we get the theory $O = (\{\top, \alpha, \alpha_{p \to \neg a}, \alpha_{a \to \neg p}, \alpha_{\Rightarrow b}, \alpha_{\Rightarrow a}, \alpha_{b \to p}\}, \leq_{o}, \{\Rightarrow b, \Rightarrow a, p \Rightarrow \neg a, a \Rightarrow \neg p, \{a, b\} \Rightarrow p\}, f)$ , where no node is superior to node $\top$ and no node except $\top$ is superior to $\alpha$ . Furthermore, we have that $f(\top) = f(\alpha) = \emptyset$ , $f(\alpha_{p \to \neg a}) = \{p \Rightarrow \neg a\}$ , $f(\alpha_{a \to \neg p}) = \{a \Rightarrow \neg p\}$ , $f(\alpha_{\Rightarrow b}) = \{\Rightarrow b\}$ , $f(\alpha_{\Rightarrow a}) = \{\Rightarrow a\}$ , and $f(\alpha_{b \to p}) = \{\{a, b\} \Rightarrow p\}$ . If we try to show that $p^{-}$ holds in this theory, we either have to show that the rule $\{a, b\} \Rightarrow p$ is not applicable at $\top$ , or that the rule $a \Rightarrow \neg p$ is applicable at $\top$ . Because it is obvious that $O|_{\top}b^{+}$ , this comes down to show that either $O|_{\top}a^{+}$ or $O|_{\top}a^{-}$ , but neither of them can be shown. The reason why the fact that $Ea^{+}$ holds in the defeasible theory is not reflected in the corresponding ordered theory, is that in the defeasible theory, the only proof tree for $Ea^{+}$ contains a node labeled $Ep^{-}$ , which causes looping when we try to build proof trees for $p^{-}$ or $a^{+}$ in the ordered theory. Therefore, the constructed ordered theory is not equivalent to the original defeasible theory.

The second problem is that when a defeasible rule $r_{1}$ with consequent p is defeated by a defeater $r_{2}$ in defeasible logic, it is sufficient to show that the antecedent of the defeater $r_{2}$ holds. It is not necessary to show that the antecedent of the defeasible rule $r_{1}$ holds. In fact, it can be the case that it can not be shown whether or not the antecedent of $r_{1}$ holds. Even if it can be shown that the antecedent of the defeasible rule $r_{1}$ holds, it can very well be the case that every proof tree showing that a

![](/api/attachments/4UU4NJNP/fulltext/images/b079ebcf8dbb2892fbf5fc679352697865e0c6af97c872b425ff544c7d21d9f2.jpg)

particular literal of this antecedent holds contains a node labeled $Ep^{-}$ , as is shown in Example 11. In this example, the antecedent of the defeasible rule holds, while this can not be shown in the ordered theory. Similarly, it can be the case that a literal of the antecedent of $r_{1}$ can be shown not to hold, while all proof trees showing this contain a node labeled $Ep^{-}$ , as is shown in Example 12. In this example, there is a literal in the antecedent of the defeasible rule that can be shown not to hold, while this can not be shown in the ordered theory. To obtain the defeat of the defeasible rule $r_{1}$ (the target rule) by a quasi-defeater taking over the role of the defeater $r_{2}$ in an ordered theory, we have to show that the antecedent of the quasi-defeater holds, which comes down to show that the antecedent of the defeater $r_{2}$ holds, but also that the antecedent of the defeasible rule $r_{1}$ holds.

Example 11 Consider the defeasible theory $D = (\{p \Rightarrow \neg a, a \Rightarrow p, b \rightsquigarrow \neg p, \Rightarrow a, \Rightarrow b\}, \emptyset)$ . Because $D|_{\leq} Eb^{+}$ , we can construct a proof tree for $Ep^{-}$ in which the rule $a \Rightarrow p$ is defeated by the defeater $b \rightsquigarrow \neg p$ , so that $D|_{\leq} Ep^{-}$ and therefore also $D|_{\leq} Ea^{+}$ . In this case, every proof tree that can possibly be constructed for $Ea^{+}$ does contain a node labeled $Ep^{-}$ .

If we translate this defeasible theory into an ordered theory following the algorithm described above, we get the theory $O = (\{\top, \alpha, \alpha_{p \Rightarrow \neg a}, \alpha_{a \Rightarrow p}, \alpha_{\Rightarrow b}, \alpha_{\Rightarrow a}, \alpha_{b \Rightarrow \neg p}\}, \leq_{o}, \{\Rightarrow b, \Rightarrow a, p \Rightarrow \neg a, a \Rightarrow p, \{a, b\} \Rightarrow \neg p\}, f)$ , where no node is superior to node $\top$ and no node except $\top$ is superior to $\alpha$ . Furthermore, we have that $f(\top) = f(\alpha) = \emptyset$ , $f(\alpha_{p \Rightarrow \neg a}) = \{p \Rightarrow \neg a\}$ , $f(\alpha_{a \Rightarrow p}) = \{a \Rightarrow p\}$ , $f(\alpha_{\Rightarrow b}) = \{\Rightarrow b\}$ , $f(\alpha_{\Rightarrow a}) = \{\Rightarrow a\}$ , and $f(\alpha_{b \Rightarrow \neg p}) = \{\{a, b\} \Rightarrow \neg p\}$ . If we try to show that $p^{-}$ holds in this theory, we either have to show that the rule $\{a, b\} \Rightarrow \neg p$ is applicable at $\top$ , or that the rule $a \Rightarrow p$ is not applicable at $\top$ . Because it is obvious that $O|_{\top}b^{+}$ , this comes down to show that either $O|_{\top}a^{+}$ or $O|_{\top}a^{-}$ , but neither of them can be shown. The reason why the fact that $Ea^{+}$ holds in the defeasible theory is not reflected in the corresponding ordered theory, is that in the defeasible theory, the only proof tree for $Ea^{+}$ contains a node labeled $Ep^{-}$ , which causes looping when we try to build proof trees for $p^{-}$ or $a^{+}$ in the ordered theory. Therefore, the constructed ordered theory is not equivalent with the original defeasible theory.

![](/api/attachments/4UU4NJNP/fulltext/images/cc75b7a43f79b29bec99952b271a44e5de50f3965289a95c3b9433c939dc430c.jpg)

Example 12 Consider the defeasible theory $D = (\{a \Rightarrow p, p \Rightarrow a, b \rightsquigarrow \neg p, \Rightarrow b\}, \emptyset)$ . Because $D|_{\leq} Eb^{+}$ , we can construct a proof tree for $Ep^{-}$ in which the rule $a \Rightarrow p$ is defeated by the defeater $b \rightsquigarrow \neg p$ , so that $D|_{\leq} Ep^{-}$ , and therefore also $D|_{\leq} Ea^{-}$ .

If we translate this defeasible theory into an ordered theory following the algorithm described above, we get the theory $O = (\{\top, \alpha, \alpha_{a \Rightarrow p}, \alpha_{p \Rightarrow a}, \alpha_{\Rightarrow b}, \alpha_{b \Rightarrow \neg p}\}, \leq_o, \{\Rightarrow b, a \Rightarrow p, p \Rightarrow a, \{a, b\} \Rightarrow \neg p\}, f)$ , where no node is superior to node $\top$ and no node except $\top$ is superior to $\alpha$ . Furthermore, we have that $f(\top) = f(\alpha) = \emptyset$ , $f(\alpha_{a \Rightarrow p}) = \{a \Rightarrow p\}$ , $f(\alpha_{p \Rightarrow a}) = \{p \Rightarrow a\}$ , $f(\alpha_{\Rightarrow b}) = \{\Rightarrow b\}$ , and $f(\alpha_{b \Rightarrow \neg p}) = \{\{a, b\} \Rightarrow \neg p\}$ . If we try to show that $p^-$ holds in this theory, we either have to show that the rule $a \Rightarrow p$ is not applicable at $\top$ , or that the rule $\{a, b\} \Rightarrow \neg p$ is applicable at $\top$ . Because it is obvious that $O|_{\top}b^+$ , this comes down to show that either $O|_{\top}a^+$ or $O|_{\top}a^-$ , but neither of them can be shown. The reason why the fact that $Ea^-$ holds in the defeasible theory is not reflected in the corresponding ordered theory, is that in the defeasible theory, the only proof tree for $Ea^-$ contains a node labeled $Ep^-$ , which causes looping when we try to build proof trees for $p^-$ or $a^-$ in the ordered theory. Therefore, the constructed ordered theory is not equivalent to the original defeasible theory.

![](/api/attachments/4UU4NJNP/fulltext/images/2084ecd9634e231b4e2ec97b07303c14a7aed73708e8fbdb33d42873c7ebbb3a.jpg)

The last problem is that in defeasible logic, absolute rules can never be defeated, while every rule in ordered logic can possibly be defeated. Because the defeasible theory we want to convert must be consistent, no rule in the top perspective $\top$ of the ordered theory can be defeated. However, there is no way we can prevent rules in the perspective $\alpha$ (corresponding with absolute rules) from being defeated, as is shown in Example 13.

Example 13 Consider the defeasible theory $D = (\{p \to p, \Rightarrow q, p \Rightarrow \neg q\}, \{\neg p\})$ . In this theory, we can only show $\neg p^{+}, q^{-}, \neg q^{-}, E \neg p^{+}$ and $E \neg q^{-}$ . We can say nothing about $p$ or $Ep$ , and therefore also nothing about $Eq$ .

If we translate this defeasible theory into an ordered theory, we get the theory $O = (\{\top, \alpha, \alpha_{\Rightarrow q}, \alpha_{p \Rightarrow \neg q}\}, \leq_o, \{\Rightarrow \neg p, p \Rightarrow p, \Rightarrow q, p \Rightarrow \neg q\}, f)$ , where no node is superior to node $\top$ and no node except $\top$ is superior to $\alpha$ . Furthermore, we have that $f(\top) = \{\Rightarrow \neg p\}$ , $f(\alpha) = \{p \Rightarrow p\}$ , $f(\alpha_{\Rightarrow q}) = \{\Rightarrow q\}$ and $f(\alpha_{p \Rightarrow \neg q}) = \{p \Rightarrow \neg q\}$ . In this theory, we can show that $\neg p^+$ holds at the top perspective, but we can also show $p^-$ , because the rule $p \Rightarrow p$ at $\alpha$ becomes defeated by the rule $\Rightarrow \neg p$ at $\top$ . Therefore, the rule $p \Rightarrow \neg q$ can be shown to be inapplicable, so that the rule $\Rightarrow q$ can be shown to be not defeated, and we have that $O|_{\top}q^+$ , which does not correspond with the defeasible theory. This can be solved by requiring that in the defeasible theory we are converting, we must be able to show for every absolute rule either that the rule is applicable or that the rule is inapplicable. If this requirement is satisfied, the defeasible theory is decisive about literals (meaning that for every literal $p$ , either $D|_{\leq}p^+$ or $D|_{\leq}p^-$ ), but not necessarily about $E$ -sentences.

$$
\begin{array}{c} \text { O } \Rightarrow \neg p \\ \text { O } p \Rightarrow p \\ \text { O } \Rightarrow q \quad \text { O } p \Rightarrow \neg q \end{array} \tag {Example13}
$$

Any algorithm for constructing an ordered theory that preserves the structure of any given defeasible theory in some meaningful way, and that is equivalent to its defeasible counterpart with regard to the conclusions derivable at the top node of the ordered theory, must address these problems. We propose the following construction algorithm.

Let $D = (R_d, K)$ be a defeasible theory and let $\leq$ be a superiority relation such that $D$ has a finite, consistent closure using $\leq$ . In our ordered theory, we will include a top node $\top$ , a node $\alpha$ that is a child node of $\top$ and an ancestor of every other node in the theory, and a node for every defeasible rule or defeater in $R_d$ . These nodes corresponding to rules will inherit their partial order in the ordered theory from the superiority relation on the rules that index them. Let

$$
\begin{array}{r l}\Sigma = \big \{\top , \alpha \big \}&\\\cup \big \{\alpha_ {A \Rightarrow p} \colon A \Rightarrow p \in R _ {d} \big \}&\\\cup \big \{\alpha_ {A \rightarrow p} \colon A \rightsquigarrow p \in R _ {d} \big \},&\end{array}
$$

and let

$$
\begin{array}{r l} \le_ {o} = \{\langle \beta , \top \rangle : \beta \in \Sigma \} \\ & \cup \{\langle \beta , \alpha \rangle : \beta \in \Sigma - \{\top \} \} \\ & \cup \{\langle \alpha_ {r}, \alpha_ {A \Rightarrow p} \rangle : r \le A \Rightarrow p \}. \end{array}
$$

Literals strictly derivable in D become rules with empty antecedents at the top node of our corresponding ordered logic, strict rules in $R_{d}$ are associated with the node $\alpha$ , and defeasible rules in $R_{d}$ are associated with the nodes they index. A defeater in $R_{d}$ is converted into a set of rules which is then associated with the node indexed by the defeater. Let

$$
\begin{array}{r l}R _ {o}&= \left\{\Rightarrow p \colon D | _ {\leq} p ^ {+} \right\}\\&\cup \left\{A \Rightarrow p \colon A \rightarrow p \in R _ {d} \text {or} A \Rightarrow p \in R _ {d} \right\}\\&\cup \left\{A \cup B \Rightarrow p \colon A \Rightarrow \neg p \in R _ {d} \quad \text {and} \right.\\&B \rightsquigarrow p \in R _ {d} \quad \text {and}\\&B \rightsquigarrow p \not <   A \Rightarrow \neg p \},\end{array}
$$

and let

$$
\begin{array}{r l}&f (\top) = \{\Rightarrow p \colon D | _ {\leq} p ^ {+} \},\\&f (\alpha) = \{A \Rightarrow p \colon A \to p \in R _ {d} \},\\&f (\alpha_ {A \Rightarrow p}) = \{A \Rightarrow p \}, \text { and }\\&f (\alpha_ {B \rightarrow p}) = \{A \cup B \Rightarrow p \colon A \Rightarrow \neg p \in R _ {d} \quad \text { and }\\&B \rightsquigarrow p \in R _ {d} \quad \text { and }\\&B \rightsquigarrow p \not \prec A \Rightarrow \neg p \}.\end{array}
$$

Finally, let $O_{\leq}^{D} = (\Sigma, \leq_{o}, R_{o}, f)$ . Our conjecture is that $D|_{\leq} Ep^{+}$ iff $O_{\leq}^{D}|_{\top} p^{+}$ , provided $D$ satisfies the following conditions.

(1) there is no literal $p$ such that $D|_{\leq}p^{+}$ and $D|_{\leq}\neg p^{+}$ ;

(2) for every literal $p$ , either $D|_{\leq}p^{+}$ or $D|_{\leq}p^{-}$ ;

(3) for every literal $p$ such that $D|_{\leq}Ep^{-}$ and every $A \Rightarrow \neg p \in R_d$ and $C \rightsquigarrow p \in R_d$ , where $C \rightsquigarrow p \nmid A \Rightarrow \neg p$ , either

(i) for every $a \in A$ , there is a proof tree for $Ea^{+}$ that does not contain a node labeled $Ep^{-}$ , or

(ii) there is $c \in A \cup C$ and a proof tree for $Ec^{-}$ that does not contain a node labeled $Ep^{-}$ ; and

(4) for every literal $p$ such that $D|_{\leq}Ep^{-}$ and every $A \Rightarrow p \in R_d$ , either

(i) for every $a \in A$ , there is a proof tree for $Ea^{+}$ that does not contain a node labeled $Ep^{-}$ , or

(ii) there is $a \in A$ and a proof tree for $Ea^{-}$ that does not contain a node labeled $Ep^{-}$ .

The problem of finding a method for constructing interesting equivalent ordered theories for some class of defeasible theories is, as we have found, non-trivial. We reported such a result in Vermeir et al. (1990), but we have since found an error in that proof. So far, we have neither constructed a proof for our conjecture nor discovered a counterexample.

The algorithm described here is different from the one suggested in Vermeir et al. (1990). We will explain the previous algorithm here and show the reason why we had to correct it. The only difference between the previous algorithm and this one is the way defeaters are simulated in ordered theories. We associated a node $\alpha_{C\to\neg p}$ with each defeater $C\rightsquigarrow\neg p$ and let $f(\alpha_{C\to\neg p})=\{C\Rightarrow\neg p,C\Rightarrow p\}$ . The reason why we put the rule $C\Rightarrow p$ in the node $\alpha_{C\to\neg p}$ is because its presence will prevent $C\Rightarrow\neg p$ at node $\alpha_{C\to\neg p}$ from ever being applied. We also required that $a_{C\to\neg p}\not\prec_{o}\alpha_{A\Rightarrow p}$ whenever $C\rightsquigarrow\neg p\not\prec A\Rightarrow p$ in the original defeasible theory. Because we did not want rule $C\Rightarrow p$ at node $\alpha_{C\to\neg p}$ to compete with any rule $D\Rightarrow\neg p$ at node $\alpha_{D\Rightarrow\neg p}$ , we had to require that $\alpha_{C\to\neg p}<_{o}\alpha_{D\Rightarrow\neg p}$ in the ordered theory. The problem is that in an arbitrary defeasible theory, it can very well be the case that

$D \Rightarrow \neg p < A \Rightarrow p,$ and therefore $\alpha_{D \Rightarrow \neg p} < _o \alpha_{A \Rightarrow p}$ . By transitivity of the partial order on the set of nodes, we obtain that $\alpha_{C \Rightarrow \neg p} < _o \alpha_{A \Rightarrow p},$ even if we have that $C \rightsquigarrow \neg p \nless A \Rightarrow p$ and therefore $\alpha_{C \Rightarrow \neg p} < _o \alpha_{A \Rightarrow p}$ . Then $C \rightsquigarrow \neg p$ can defeat $A \Rightarrow p$ in the defeasible theory, but not at $\top$ in the corresponding ordered theory.

Investigating the relationship between ordered theories and defeasible theories further, we find it is much easier to show that each ordered theory $O = (\Sigma, \leq_{o}, R_{o}, f)$ corresponds to a family of defeasible theories $D_{\alpha}$ with $\alpha \in \Sigma$ such that $D_{\alpha}$ is equivalent to O at node $\alpha$ . The main idea is that we introduce into the language of our defeasible theories a set of new sentence constants $p_{\alpha}$ with $\alpha \in \Sigma$ . Let $R_{d} = \{\{p_{\alpha}\} \cup A \Rightarrow p: A \Rightarrow p \in f(\alpha)\} \cup \{\{p_{\alpha}\} \to p_{\beta}: \beta \leq_{o} \alpha\}$ . For each $\alpha \in \Sigma$ , let $D_{\alpha} = (R_{d}, \{p_{\alpha}\})$ . The common superiority relation for all defeasible theories in the family is given by $A \Rightarrow p \leq B \Rightarrow q$ if $p_{\alpha} \in A$ , $p_{\beta} \in B$ and $\alpha \leq_{o} \beta$ , together with the usual constraints on strict rules. The idea is that $p_{\alpha}$ triggers the rules which correspond to the rules at node $\alpha$ and all nodes below $\alpha$ in the original ordered theory. Intuitively, $p_{\alpha}$ says “We are drawing conclusions from a perspective influenced by node $\alpha$ .”

Theorem 2 If $O = (\Sigma, \leq_{o}, R_{o}, f)$ is an ordered theory, then for all $\alpha \in \Sigma$ , $O|_{\overline{\alpha}} p^{+}$ iff $D_{\alpha}|_{\leq} Ep^{+}$ where $p \notin \{p_{\beta}: \beta \in \Sigma\}$ .

## 7. Semantics for ordered logic

Definition 7 Let $(\Sigma, \leq)$ be a finite partially ordered set. A $\leq$ -structure is a mapping M from $\Sigma$ to sets of literals that assigns a consistent set of literals to each element of $\Sigma$ .

We can think of a $\leq$ -structure as representing the beliefs associated with each perspective in the field of T. We call a $\leq$ -structure M a model of an ordered theory T if all rules of T are “valid” in M. But first we need to define the notion of the validity of a rule $A \Rightarrow p$ . In classical model theory, this is easily done: a rule is valid in a structure if whenever its antecedent holds, its consequent also holds. We adapt this definition to the present situation by counting defeated rules as valid.

Definition 8 Let $T = (\Sigma, \leq, R, f)$ be an ordered theory. A $\leq$ -structure $M$ is a weak model of $T$ if for each rule $A \Rightarrow p$ at perspective $\alpha$ and each perspective $\beta \geq \alpha$ , either

(m1) $A \Rightarrow p$ is applied at $\beta$ , i.e., $A \subseteq M(\beta)$ and $p \in M(\beta)$ ;

(m2) $A \Rightarrow p$ is not applicable at $\beta$ , i.e., $A \subsetneq M(\beta)$ ; or

(m3) $A \Rightarrow p$ is defeated at $\beta$ , i.e., $A \not\subseteq M(\beta)$ , $p \notin M(\beta)$ and there exists $\gamma \leq \beta$ , $B \Rightarrow \neg p \in f(\gamma)$ , with $\gamma \not\prec \alpha$ , such that $B \subseteq M(\beta)$ .

Although the above definition seems natural from a semantical point of view, it turns out that the class of models of a theory is too large to allow for a soundness result, as is illustrated by the next example.

Example 14 Consider the ordered theory ( $\{\alpha\}$ , $\leq$ , $\{\Rightarrow p, q \Rightarrow \neg p\}$ , $f$ ) where $f(\alpha) = \{\Rightarrow p, q \Rightarrow \neg p\}$ . $M(\alpha) = \{\neg p, q\}$ is a weak model for this theory since $q \Rightarrow \neg p$ is applied at $\alpha$ and $\Rightarrow p$ is defeated at $\alpha$ . But we can construct proofs for $p^{+}$ and $q^{-}$ .

The fact that our system in its present form is not sound should not be surprising since we can hardly expect soundness (“everything that can be proven is true in every model”) to coexist with non-monotonicity (“modifying a model to accommodate a new premise may yield a model that is not an extension of the original one”). There are two directions we an take: either we restrict our definition of a model or we modify the notion of soundness. We will try both approaches.

A closer inspection of Example 14 reveals that the problem lies in the fact that making additional assumptions in the model may cause a rule that is applied in the proof theory (based on just the facts given in the theory) to become defeated. We will define a strong model in which this can't happen. First we introduce the notion of the conservative extension of an ordered theory.

Definition 9 Let $T = (\Sigma, \leq, R, f)$ be an ordered theory. We define the conservative extension $\mu^*$ of $T$ by $\mu^*(\alpha) = \{p: T|_{\overline{\alpha}} p^+\}$ for each $\alpha \in \Sigma$ .

We define a strong model of an ordered theory by adapting condition (m3) in Definition 8 to require that the defeating rule is applicable at the perspective in the conservative extension.

Definition 10 Let $T = (\Sigma, \leq, R, f)$ be an ordered theory. A $\leq$ -structure $M$ is a strong model of $T$ if for each $\alpha \in \Sigma$ , each $A \Rightarrow p \in f(\alpha)$ and each perspective $\beta \geq \alpha$ , either

(m1) $A \Rightarrow p$ is applied at $\beta$ ;

(m2) $A \Rightarrow p$ is not applicable at $\beta$ ; or

(m3) $A \Rightarrow p$ is defeated at $\beta$ , i.e., $A \subseteq M(\beta)$ , $p \notin M(\beta)$ and there exists $\gamma \leq \beta$ , $B \Rightarrow \neg p \in f(\gamma)$ , with $\gamma \not\prec \alpha$ , such that $B \subseteq \mu^{*}(\beta)$ .

Theorem 3 If $T$ is an ordered theory, $M$ is a strong model of $T$ , and $T|_{\overline{\alpha}}p^{+}$ , then $p \in M(\alpha)$ .

Although the logic is sound with respect to strong models, it is still not complete. Consider Example 3 once again and suppose $M$ is a strong model of $T$ . Then $\Rightarrow p$ must be applied, inapplicable, or defeated at perspective $\alpha$ in $M$ . Since the antecedent of $\Rightarrow p$ is empty, the rule can't be inapplicable. Suppose it is defeated. Then since $p \Rightarrow \neg p$ is the only competing rule, $p$ must be in $\mu^{*}(\alpha)$ . But we saw that nothing is provable at $\alpha$ in $T$ , so $\mu^{*}(\alpha)$ is empty. So $\Rightarrow p$ must be applied at $\alpha$ in $M$ , and $p$ is a member of $M(\alpha)$ for every strong model $M$ of $T$ . But $T \nVdash_{\alpha} p^{+}$ . We seek a restriction on ordered theories, such that for this class of theories, our logic is complete.

## 8. Properly ordered theories

Definition 11 Let $T = (\Sigma, \leq, R, f)$ be an ordered theory. With each $\alpha \in \Sigma$ , we associate a dependency digraph $G_{\alpha}$ , with positive and negative edges. The positive directed edges are defined as the pairs $(a, p)$ where there is $\beta \leq \alpha$ and $A \Rightarrow p \in f(\beta)$ such that $a \in A$ . The negative edges are defined as the pairs $(a, p)$ where there is $\beta \leq \alpha$ , $\gamma \leq \alpha$ , $B \Rightarrow p \in f(\beta)$ , $A \Rightarrow \neg p \in f(\gamma)$ , such that $\gamma \not\prec \beta$ and $a \in A$ .

The intuition behind a negative edge $(a, p)$ , where $A \Rightarrow \neg p \in R$ and $a \in A$ , is that a may “block” an argument for p. Clearly this can only happen if an argument for p is possible, i.e., a rule $B \Rightarrow p$ is available. Moreover, this rule cannot be “stronger” than $A \Rightarrow \neg p$ since otherwise, it could never be blocked by $A \Rightarrow \neg p$ .

Example 15 Consider the ordered theory ( $\{\alpha, \beta, \gamma\}$ , $\leq$ , $\{\Rightarrow p, \Rightarrow q, p \Rightarrow \neg q, q \Rightarrow \neg p\}$ , $f$ ) with $\beta < \alpha$ , $\gamma < \alpha$ , $f(\alpha) = \emptyset$ , $f(\beta) = \{\Rightarrow p, p \Rightarrow \neg q\}$ , and $f(\gamma) = \{\Rightarrow q, q \Rightarrow \neg p\}$ .

![](/api/attachments/4UU4NJNP/fulltext/images/c532d144663d40224756e266db06acb6bf849c08018a27132c876aaef73b58bb.jpg)

The digraphs $G_{\beta}$ and $G_{\alpha}$ are shown below.

![](/api/attachments/4UU4NJNP/fulltext/images/38ea9f6a1d13987eff941710cbba853af431bc657d4be27dce964e447093f812.jpg)

Definition 12 An ordered theory T is properly ordered at perspective $\alpha$ if and only if the corresponding dependency digraph $G_{\alpha}$ does not contain a cycle with a negative edge. An ordered theory T is properly ordered if and only if T is properly ordered at each perspective of T.

Literal p is a potential counterargument for literal q if there is a path from p to q passing through a negative edge. If a theory has no cycles with negative edges, then no literal can be its own counterargument.

Keeping this in mind, we can refine our proof theory. A repetition of a negative label $p^{-}$ in a proof tree at perspective $\alpha$ with only negative labels in between, means that we are passing through a positive cycle in the corresponding dependency digraph $G_{\alpha}$ , which implies that p has to be satisfied in order to satisfy p. The expansion of this path in the proof tree may therefore be stopped after the second occurrence of $p^{-}$ . However, when the path has a positive label in between the occurrences of $p^{-}$ , then we are passing through a cycle in $G_{\alpha}$ with a negative edge, which means that p is a counterargument for itself. Therefore, we can not conclude that we can show that $p$ doesn't hold. This motivates the addition of a third condition (C3) in our definition of a proof tree.

Definition 6\*\* Let $(\Sigma, \leq, R, f)$ be an ordered theory. Where $p$ is a literal and $s$ is $+$ or $-$ , a proper proof tree for $p^s$ at a perspective $\alpha$ in $(\Sigma, \leq, R, f)$ is a finite tree where each node is labeled $q^t$ , with $q$ a literal and $t$ is $+$ or $-$ , such that the root node of the tree is labeled $p^s$ and each node $m$ is labeled by an adorned literal $l$ satisfying one of the following conditions:

(C1) $l = p^{+}$ and there exists a rule $A \Rightarrow p$ at perspective $\beta$ , where $\beta \leq \alpha$ , such that

(C1.1) for each $a \in A$ , there is a child node of $m$ labeled $a^+$ , and

(C1.2) for each rule $B \Rightarrow \neg p$ at perspective $\gamma$ where $\gamma \leq \alpha, \gamma \nmid \beta$ , there is $b \in B$ and a child node of $m$ labeled $b^{-}$ .

(C2) $l = p^{-}$ and for each rule $A \Rightarrow p$ at perspective $\beta$ , where $\beta \leq \alpha$ , either

(C2.1) there is $a \in A$ for which there is a child node of $m$ labeled $a^{-}$ , or

(C2.2) there is a rule $B \Rightarrow \neg p$ at perspective $\gamma$ with $\gamma \leq \alpha, \gamma \neq \beta$ , such that for each $b \in B$ , there is a child node of $m$ labeled $b^{+}$ , or

(C3) $l = p^{-}$ and $m$ has an ancestor $k$ labeled $p^{-}$ , such that there is no node between $m$ and $k$ having a positive label.

We will say that $p^{s}$ holds properly at perspective $\alpha$ on theory T (in symbols, $T\|_{\overline{\alpha}}p^{s}$ ), iff there is a proper proof tree t for $p^{s}$ at $\alpha$ in T.

Lemma 1, Lemma 2, and Theorem 3 still hold for $\Vdash$ , while Lemma 3 has to be slightly adapted: the depth of the proper proof tree can exceed $N$ , but not $(N+1)^{2}$ .

Consider again the theory of Example 15. Clearly, $p$ and $\neg q$ hold properly at $\beta$ , while $q$ and $\neg p$ hold properly at $\gamma$ . At $\alpha$ however, we cannot prove either that $p$ holds properly or that $p$ doesn't hold properly. The same is true for $q$ . It is also clear that $T$ is properly ordered at perspectives $\beta$ and $\gamma$ , but not at perspective $\alpha$ .

The theories in the Examples 1, 2 and 14 are properly ordered, while the theory of Example 3 is not.

Example 16 Consider the ordered theory ( $\{\alpha\}$ , $\emptyset, \{p \Rightarrow p\}, f$ ) with $f(\alpha) = \{p \Rightarrow p\}$ . $p$ doesn't hold at $\alpha$ , but we can also show that it doesn't hold properly by the existence of a proper proof tree of $p^{-}$ , which results from adding the condition (C3) in the proof theory. This theory is properly ordered.

Lemma 4 If $T$ is a properly ordered theory, then not $T\|_{\overline{\alpha}}p^{+}$ implies $T\|_{\overline{\alpha}}p^{-}$ . $\square$

Lemma 5 If $T$ is a properly ordered theory, then the proper conservative extension $\mu^{*}$ (defined now using $\Vdash$ ) is a strong model. $\square$

Using this last Lemma, we can prove that our logic is complete with respect to the class of properly ordered theories.

Theorem 4 If $T$ is a properly ordered theory and $p \in M(\alpha)$ for every strong model $M$ of $T$ , then $T \Vdash_{\alpha} p^{+}$ .

Many familiar examples of nonmonotonic reasoning involve properly ordered theories, but there are reasonable theories that are not properly ordered.

Example 17 Presumably, Bush will live in the White House next year. But if Bush dies, Quayle will live in the White House next year. If Bush lives in the White House, Quayle won't; and if Quayle lives in the White House, Bush won't. We can represent this as an ordered theory $(\{\alpha\},\emptyset, R,f)$ where $f(\alpha)=R=\{\Rightarrow b,d\Rightarrow q,b\Rightarrow\neg q,q\Rightarrow\neg b\}$ . This theory is not properly ordered since we have negative edges from $b$ to $q$ and from $q$ to $b$ in the dependency digraph $G_{\alpha}$ .

## 9. Monotonic semantics for ordered logic

In this section, we follow an alternative approach to soundness by modifying the definition of soundness.

Soundness is often interpreted as “whatever you can prove (in a theory) is true in all (its) models.” This is equivalent, at least in the classical case, to “whatever you can prove is true in the smallest models”, where smallest has to be interpreted according to the $\subseteq$ (partial) order.

For us, soundness would require that there is some partial order on models such that the conservative extension is minimal in this partial order. Since $\subseteq$ doesn't satisfy this requirement, we propose a different partial ordering which extends the $\subseteq$ ordering for standard logic and allows for a soundness result. The idea of a preference order between models is also proposed, with a different motivation, by Shoham (1987).

Definition 13 Let $(\Sigma, \leq, R, f)$ be an ordered theory, $\alpha \in \Sigma$ , $G_{\alpha}$ the dependency digraph at $\alpha$ , and $l_{1}$ and $l_{2}$ literals. We say that $l_{1}$ dominates $l_{2}$ at perspective $\alpha$ , denoted as $l_{1} \operatorname{dom}_{\alpha} l_{2}$ , if there is a path in $G_{\alpha}$ , from $l_{1}$ to $l_{2}$ passing through a negative edge.

Intuitively, $l_{1}$ dominates $l_{2}$ if $l_{1}$ can be used in a counterargument for $l_{2}$ . Put in another way, the truth of $l_{1}$ may block the proof of $l_{2}$ . Roughly, we will say that a model $M_{1}$ is more faithful to a theory than another model $M_{2}$ if $M_{1}$ makes fewer assumptions that block proofs of other literals; i.e., we try to minimize dominating literals in a model.

Definition 14 Let $T = (\Sigma, \leq, R, f)$ be an ordered theory and let $M_1$ and $M_2$ be two models of $T$ . We say that $M_1$ is more faithful to $T$ than $M_2$ , denoted $M_1 \leq_T M_2$ , if for each $\alpha \in \Sigma$ and each literal $p \in M_1(\alpha) - M_2(\alpha)$ , there exists a literal $q \in M_2(\alpha) - M_1(\alpha)$ such that $q \operatorname{dom}_{\alpha} p$ .

Note that the above definition implies that $M_{1} \leq_{T} M_{2}$ whenever $M_{1}(\alpha) \subseteq M_{2}(\alpha)$ for each perspective $\alpha$ . Thus, the partial order $\leq_{T}$ is a proper generalization of the usual $\subseteq$ ordering on models.

Lemma 6 If $T$ is a properly ordered theory, then $\leq_{T}$ is a partial order on the weak models of $T$ . $\square$

Theorem 5 (soundness and completeness) The conservative extension $\mu^{*}$ of a properly ordered theory $T$ is the unique minimal model, according to $\leq_{T}$ , in the class of all weak models of $T$ .

Recent research has investigated another class of ordered theories, choice theories, which allow several minimal models. This approach resembles the credulous approach where a minimal model is accepted until further information forces us to reject it. In Laenens et al. (1989), a fixpoint procedure is introduced which allows for the computation of all minimal models.

## 10. Quantified ordered logic

For quantified ordered logic we modify the definition of a literal. We assume a recursive set P of predicate symbols, a recursive set C of constant symbols, and a countable set VR of variable symbols satisfying the usual distinctness conditions $(P, C, \text{and } VR \text{ are mutually disjoint; no member of } P \text{ is a sequence of members of } P, C \text{ or } VR; \text{ etc}). t \text{ is a term iff } t \in C \text{ or } t \in VR.$ An atomic formula is an expression of the form $F(t_{1}, \ldots, t_{n})$ where F is an n-place predicate symbol in P and $t_{1}, \ldots, t_{n}$ are terms. A literal is an atomic formula or the negation of an atomic formula. The definition of a defeasible rule remains unchanged except that we now understand the term literal in the definition in this new sense. A quantified ordered theory will just be an ordered theory in which all the defeasible rules allow antecedent sets of literals and literal consequents in this new sense.

In quantified ordered logic, we must somehow handle substitution of constants for variables in the rules we apply. We simplify our proof theory by requiring that every node in a proof tree is labeled with a ground literal, i.e., a literal that contains no variables. Furthermore, we require that all constants occurring in the tree must occur either in the label of the root node or in some rule in the theory. To accomplish this, we restrict substitution to constants occurring in the conclusion of the argument (the label of the root node) and in the rules in the theory.

Definition 15 Where C is a set of constants and p is a literal, p is ground in C iff p is ground and every constant that occurs in p is a member of C.

Definition 16 Where C is a set of constants, a substitution in C is a function $\sigma: VR \to C$ . Where p is any formula, we will denote the result of applying $\sigma$ to all the variables in p as $p\sigma$ . Where A is a set of formulae, we let $A\sigma = \{p\sigma: p \in A\}$ .

Definition 17 Let $(\Sigma, \leq, R, f)$ be a quantified ordered theory. Where $p$ is a ground literal, $s$ is $+$ or $-$ and $C$ is the set of constants occurring in $p$ or in some member of $R$ , a ground proof tree for $p^s$ at a perspective $\alpha$ in $(\Sigma, \leq, R, f)$ is a finite tree where each node is labeled $q^t$ , with $q$ a literal ground in $C$ and $t$ is $+$ or $-$ , such that the root is labeled $p^s$ and each node $m$ is labeled by an adorned literal $l$ satisfying one of the following conditions:

(Q1) $l = p^{+}$ and there exists a substitution $\sigma$ in $C$ and a rule $A \Rightarrow q$ at perspective $\beta$ , where $\beta \leq \alpha$ and $q\sigma = p$ , such that

(Q1.1) for each $a \in A$ , there is a child node of $m$ for which $a\sigma^{+}$ is the label, and

(Q1.2) for each substitution $\tau$ in $C$ and rule $B \Rightarrow r$ at perspective $\gamma$ where $\gamma \leq \alpha$ , $\gamma \neq \beta$ , and $r\tau = \neg p$ , there is $b \in B$ and a child node of $m$ for which $b\tau^{-}$ is the label.

(Q2) $l = p^{-}$ and for each substitution $\sigma$ in $C$ and rule $A \Rightarrow q$ at perspective $\beta$ , where $\beta \leq \alpha$ and $q\sigma = p$ , either

(Q2.1) there is $a \in A$ for which there is a child node of $m$ with label $a\sigma^{-}$ , or

(Q2.2) there is a substitution $\tau$ in $C$ and a rule $B \Rightarrow r$ at perspective $\gamma$ with $\gamma \leq \alpha$ , $\gamma \neq \beta$ , and $r\tau = \neg p$ , such that for each $b \in B$ , there is a child node of $m$ with label $b\tau^{+}$ .

Theorem 6 Where $T = (\Sigma, \leq, R, f)$ is a quantified ordered theory, $\alpha \in \Sigma$ , $p$ is a literal, $s$ is + or -, and $C$ is the set of constants occurring in $R$ and $p$ , let $R^p = \{A\sigma \Rightarrow q\sigma: A \Rightarrow q \in R \text{ and } \sigma \text{ is a substitution in } C\}$ , for each $\alpha \in \Sigma$ let $f^p(\alpha) = \{A\sigma \Rightarrow q\sigma: A \Rightarrow q \in f(\alpha) \text{ and } \sigma \text{ is a substitution in } C\}$ , and let $T^p = (\Sigma, \leq, R^p, f^p)$ . Then $t$ is a ground proof tree for $p^s$ at $\alpha$ in $T$ iff $t$ is a ground proof tree for $p^s$ at $\alpha$ in $T^p$ .

We can think of each ground literal as a propositional constant, so that for any quantified ordered theory T and literal p, the theory $T^{p}$ as defined above is essentially propositional since it contains no rules in which variables occur. Thus the substitutions referred to in the proof theory play no role in the proof tree for $T^{p}$ , and the lemmas and theorems shown for ordinary proof trees also hold for ground proof trees.

In first order logic (FOL), we can derive $(\exists x)F(x)$ from $(\forall x)F(x)$ . In another version of quantified logic called free logic, this derivation is not possible. From the point of view of free logic, the inference from “Everything is a frog” to “Something is a frog” is an enthymeme where the suppressed premise is “There is something”. Our proof theory for quantified ordered logic is closer to free logic than to FOL in this respect. For example, for a theory T with a single perspective $\alpha$ at which we find the rules $F(x) \Rightarrow p$ and $\Rightarrow F(x)$ , we do not have a ground proof tree of $p^{+}$ at $\alpha$ for T. We can view the rules in T as saying that p is normally true if anything is an F, and everything is an F. According to our ground proof theory, this does not imply that p since we have no assurance that there is anything that could be an F. Since neither p nor any of the rules in T contain any constants, there is no commitment to the existence of any object. As it turns out, developing a proof theory which will allow us to prove p from this quantified ordered theory is no easy task. This is because we do not want to defeat rules simpliciter, rather, we want to defeat their application to particular individuals. This raises interesting problems for coordinating substitutions in different branches of a proof tree, problems which are avoided in ground proof trees.

## 11. Multiple agents and curtains for ordered theories $^{6}$

In an ordered theory, every higher perspective has complete access to all rules at any lower perspective. Where perspectives are viewed as different perspectives of a single agent, this is intuitively plausible. However, when some perspectives are thought of as distinct agents this is not plausible. Consider a consultant-client relation. The consultant makes recommendations to the client which the client then uses in further reasoning. Even when the consultant provides an explanation of her recommendation to her client, she normally has access to much more information and rules that the client is not aware of.

To model this common kind of situation in ordered logic, we need to identify the agents in an ordered theory that correspond to distinct agents and to shield the rules available to one agent from the view of other agents. To accomplish this, we introduce the notion of a curtain for an ordered theory.

Definition 18 $C = (A, \sqsubseteq)$ is a curtain for an ordered theory $(\Sigma, \leq, R, f)$ iff

(1) $\mathbf{A} \subseteq \Sigma$

(2) $\subseteq \subseteq (\leq \cap (\Sigma \times A))$

(3) for all $\alpha \in A$ , $\alpha \subseteq \alpha$

(4) for all $\beta \in \Sigma - A$ , there is $\alpha \in A$ , $\beta \sqsubseteq \alpha$

(5) for all $\alpha \in A$ and all $\beta, \gamma \in \Sigma - A$ , if $\beta < \gamma \sqsubseteq \alpha$ and there is no $\alpha^{*} \in A$ such that $\beta \sqsubseteq \alpha^{*} < \gamma$ , then $\beta \sqsubseteq \alpha$ .

(6) for all $\alpha \in A$ and all $\beta, \gamma \in \Sigma - A$ , if $\gamma < \beta < \alpha$ , $\gamma \sqsubseteq \alpha$ , and there is no $\alpha^* \in A$ such that $\beta \sqsubseteq \alpha^* < \alpha$ , then $\beta \sqsubseteq \alpha$ .

We read “ $a \sqsubseteq b$ ” as “a is visible from b” and we write “ $a \sqsubseteq b$ ” when $a \sqsubseteq b$ but not $b \sqsubseteq a$ .

A curtain divides an ordered theory into several more or less private areas associated with distinct nodes in the ordered theory conceived of as agents. Each non-agent node is visible to at least one agent. Agents can be visible to each other, but as we will see when we look at the proof theory, they are only visible to each other in the sense that one agent can know what literals another agent proves or disproves. The rules available at nodes in one agent's sphere of influence may not be directly accessible to another agent. When a non-agent node is visible to an agent, the agent has access to all the rules at that node. This notion of rules being accessible is made explicit in the proof theory for ordered theories with curtains.

Conditions 5 and 6 in the definition of a curtain make it clear that the curtain is in some sense a conservative restriction of the partial order of the ordered theory. If an agent can see any non-agent node in the theory, then it should be able to see non-agent nodes below that nodes and non-agent nodes between itself and that node. This visibility can only be obstructed by another agent that stands between the first agent and the non-agent node.

Definition 19 Let $T = (\Sigma, \leq, R, f)$ be an ordered theory and let $C = (A, \sqsubseteq)$ be a curtain for $T$ . A proof tree in curtain $C$ for $(\Sigma, \leq, R, f)$ is a finite tree where each node is labeled $q_{\alpha}^{t}$ , where $q$ is a literal, $t$ is + or -, and $\alpha \in A$ , such that each node $m$ is labeled by an adorned literal $l$ satisfying one of the following conditions:

(CC1) $l = p_{\alpha}^{+}$ and there exists $\beta \in (\Sigma - A) \cup \{\alpha\}$ and $B \Rightarrow p \in f(\beta)$ , where $\beta \sqsubseteq \alpha$ , such that

(CC1.1) for each $b \in B$ , there is a child node of $m$ labeled $b_{\alpha}^{+}$ ,

(CC1.2) for each $\gamma \in (\Sigma - A) \cup \{\alpha\}$ and $D \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \subseteq \alpha$ and $\gamma \neq \beta$ , there is $d \in D$ and a child node of $m$ labeled $d_{\alpha}^{-}$ , and

(CC1.3) for each $\alpha^{*} \in A$ , where $\alpha^{*} \sqsubset \alpha$ and $\alpha^{*} \nmid \beta$ , there is a child node of $m$ labeled $\neg p_{\alpha^{*}}^{-}$ .

(CC2) $l = p_{\alpha}^{+}$ and there exists $\alpha^{*} \in A$ , where $\alpha^{*} \sqsubset \alpha$ , such that

(CC2.1) there is a child node of $m$ labeled $p_{\alpha^{*}}^{+}$ ,

(CC2.2) for each $\gamma \in (\Sigma - A) \cup \{\alpha\}$ and $D \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \subseteq \alpha$ and $\gamma \neq \alpha^{*}$ , there is $d \in D$ and a child node of $m$ labeled $d_{\alpha}^{-}$ , and

(CC2.3) for each $\alpha^{**} \in A$ , where $\alpha^{**} \sqsubset \alpha$ and $\alpha^{**} \nless \alpha^*$ , there is a child node of $m$ labeled $\neg p_{\alpha^{**}}^{-}$ .

(CC3) $l = p_{\alpha}^{-}$

(CC3.1) for each $\beta \in (\Sigma - A) \cup \{\alpha\}$ and all $B \Rightarrow p \in f(\beta)$ , where $\beta \sqsubseteq \alpha$ , either

(CC3.1.1) there is $b \in B$ and a child node of $m$ labeled $b_{\alpha}^{-}$ ,

(CC3.1.2) there is $\gamma \in (\Sigma - A) \cup \{\alpha\}$ and $D \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \sqsubseteq \alpha$ and $\gamma \neq \beta$ , such that for each $d \in D$ , there is a child node of $m$ labeled $d_{\alpha}^{+}$ , or

(CC3.1.3) there is $\alpha^{*} \in A$ , where $\alpha^{*} \sqsubset \alpha$ and $\alpha^{*} \neq \beta$ , such that there is a child node of $m$ labeled $\neg p_{\alpha^{*}}^{+}$ ; and

(CC3.2) for each $\alpha^{*}\in A$ , where $\alpha^{*}\sqsubset \alpha$ , either

(CC3.2.1) there is a child node of $m$ labeled $p_{\alpha}^{-*}$ , (CC3.2.2) there is $\gamma \in (\Sigma - A) \cup \{\alpha\}$ and $D \Rightarrow \neg p \in f(\gamma)$ , where $\gamma \sqsubseteq \alpha$ and $\gamma \neq \alpha^{*}$ , such that for each $d \in D$ , there is a child node of $m$ labeled $d_{\alpha}^{+}$ , or

(CC3.2.3) there is $\alpha^{**} \in A$ , where $\alpha^{**} \sqsubset \alpha$ and $\alpha^{**} \nless \alpha^*$ , such that there is a child node of $m$ labeled $\neg p_{\alpha^{**}}^{+}$ .

Where T is an ordered theory, C is a curtain for T, $\alpha$ is an agent in C, p is a literal, and s is either + or -, we write $T \frac{C}{\alpha} p^{s}$ if and only if there is a proof tree in curtain C for T whose root node is labeled $p_{\alpha}^{s}$ .

Lemma 7 If $T$ is an ordered theory and $C$ is a curtain for $T$ , then not both $T \models_{\alpha}^{C} p^{+}$ and $T \models_{\alpha}^{C} p^{-}$ .

Lemma 8 If $T$ is an ordered theory and $C$ is a curtain for $T$ , then not both $T \models_{\alpha}^{C} p^{+}$ and $T \models_{\alpha}^{C} \neg p^{+}$ . $\square$

Theorem 7 If $T = (\Sigma, \leq, R, f)$ is an ordered theory, $A = \{\beta \in \Sigma: \text{there is no } \gamma \in \Sigma \text{ such that } \beta < \gamma\}$ , $\sqsubseteq = \{\langle \beta, \alpha \rangle: \beta \leq \alpha \text{ and } \alpha \in A\}$ , $C = (A, \sqsubseteq)$ , $\alpha \in A$ , $p$ is a literal, and $s$ is + or -, then $T \models_{\alpha} p^s$ iff $T \models_{\alpha}^{C} p^s$ .

Theorem 7 says that what is derivable at top nodes in an ordered theory is exactly the same as what is derivable at those nodes if they are considered as the only agents specified in a curtain for the ordered theory and the curtain includes the visibility relation that results from restricting the partial order on the ordered theory minimally.

Definition 20 An agent $\alpha$ is opaque in a curtain $(A, \sqsubseteq)$ for a theory $(\Sigma, \leq, R, f)$ iff $\alpha \in A$ and for all $\beta \in \Sigma$ and all $\alpha^{*} \in A$ , if $\beta < \alpha$ and $\beta \sqsubseteq \alpha^{*}$ , then $\alpha^{*} \leq \alpha$ .

Definition 21 A curtain $(A, \sqsubseteq)$ is totally opaque iff for all $\alpha \in A$ , $\alpha$ is opaque.

Intuitively, all agents are opaque and no agent has direct access to the cognitive resources of another agent. But of course, some knowledge may be common to more than one agent. We can represent this common knowledge by putting it at nodes that are visible to all the agents that share the knowledge. Of course, this is just for convenience since we could duplicate the shared subtrees, making copies for each agent which shares the knowledge.

There are cases, however, where it is natural and intuitive to make some non-agent nodes visible to more than one agent. This is the case when an agent in the usual sense advises another agent in some special domain. For example, a doctor may be a medical authority for her patient without at the same time being a legal or an economic authority for her patient. The patient accepts the advice of the doctor qua doctor, but may not accept her advice otherwise. Then a new virtual agent, the doctor qua doctor, arises. Of course, this is really just a perspective of the doctor which the patient somehow treats as a separate agent. All the cognitive resources available to the doctor qua doctor are also available to the doctor as a complete person. We will examine this kind of example in more detail in the next section.

Opaque agents also have interesting formal properties. Under certain circumstances, they may in an interesting sense be replaced in a curtained ordered theory by a single nonagent node in a roughly equivalent curtained theory.

Definition 22 An agent $\alpha$ is decisive in a curtain $C$ for a theory $T$ iff for every $p$ , either $T \left| \frac{C}{\alpha} p^{+} \right.$ or $T \left| \frac{C}{\alpha} p^{-} \right.$ . For any agent $\alpha$ and any curtain $C$ for a theory $T$ , let $\alpha^{C} = \{\Rightarrow p: T \left| \frac{C}{\alpha} p^{+} \right\}$ .

Theorem 8 Suppose $\alpha$ is an opaque agent in curtain $C = (A, \sqsubseteq)$ for ordered theory $T = (\Sigma, \leq, R, f)$ . Let $\Sigma^{*} = \{\gamma: \gamma \in \Sigma \text{ and } \gamma < \alpha\}$ , let $\leq^{*} = \leq \cap (\Sigma^{*} \times \Sigma^{*})$ , let $R^{*} = \{r: r \in f(\gamma) \text{ for some } \gamma \in (\Sigma^{*} - \{\alpha\})\} \cup \alpha^{C}$ , let $f^{*}(\gamma) = f(\gamma)$ for all $\gamma \in \Sigma^{*} - \{\alpha\}$ and let $f^{*}(\alpha) = \alpha^{C}$ , let $T^{*} = (\Sigma^{*}, \leq^{*}, R^{*}, f^{*})$ , let $A^{*} = A \cap \Sigma^{*}$ , let $\sqsubseteq^{*} = \sqsubseteq \cap \leq^{*}$ , and let $C^{*} = (A^{*}, \sqsubseteq^{*})$ . (1) $\alpha$ is decisive for $T^{*}$ and $C^{*}$ .

(2) for all $\beta \in A^{*}$ , if $T \mid_{\alpha}^{\mathbb{C}} p^{s}$ then $T^{*} \mid_{\beta}^{\mathbb{C}^{*}} p^{s}$ .

(3) If $\alpha$ is decisive for $T$ and $C$ , then for all $\beta \in A^{*}$ , $T \models_{\beta}^{C} p^{s}$ iff $T^{*} \models_{\beta}^{C^{*}} p^{s}$ .

The converse of (2) in Theorem 8 is false, as we see from the following example.

Example 18 Let $T = (\{\alpha, \beta\}, \leq, \{\Rightarrow p, p \Rightarrow \neg p, p \Rightarrow q\}, f)$ where $\beta < \alpha$ , $f(\alpha) = \{p \Rightarrow q\}$ , and $f(\beta)$

$= \{\Rightarrow p, p \Rightarrow \neg p\}$ . Let $C = (\{\alpha, \beta\}, \leq)$ . $\{\Rightarrow r: T \mid_{\frac{C}{\beta}} r\} = \emptyset$ , so the theory we construct using the method in Theorem 8 is $T^{*} = (\{\alpha, \beta\}, \leq, \{p \Rightarrow q\}, f^{*})$ where $f^{*}(\alpha) = \{p \Rightarrow q\}$ and $f^{*}(\beta) = \emptyset$ , and $C^{*} = (\{\alpha, \beta\}, \leq)$ . Then $T^{*} \mid_{\frac{C^{*}}{\alpha}} q^{-}$ . But we can show neither $p^{+}$ nor $p^{-}$ at $\beta$ in $T$ using $C$ , and therefore we cannot show $T \mid_{\frac{C}{\alpha}} q^{-}$ .

The notion of a decisive agent is important because we would expect an advice taker to treat his advisers as decisive even if they aren't. When an adviser is asked about $p$ , he might respond "I have evidence for $p$ " ( $\frac{C}{\alpha}p^{+}$ ) "My evidence does not support $p$ " ( $\frac{C}{\alpha}p^{-}$ ), or "I can't tell whether my evidence supports $p$ or not". If the latter is the case, then the adviser might not respond to the query about $p$ at all since our theory very likely is not decidable in the quantified case. An advice taker might be inclined to treat the last two cases as equivalent. Practically, an advice taker might impose resource constraints on advisers and thereby treat them as decisive. For example, the advice taker might require advice to be given by a certain deadline. If an adviser does not respond by the deadline, the advice taker acts as if the adviser said "My evidence does not support $p$ ".

## 12. Modeling multiple agents

If we begin by representing two or more perspectives by different ordered theories, we can combine these two trees into a larger tree in several ways. One way is to simply create a new top node and hang both trees below it, as in the following example.

![](/api/attachments/4UU4NJNP/fulltext/images/a42c802d087018893f1d1070b214eda887a621ceb6796c56521f8461861efc3b.jpg)  
In this new tree, we clearly give equal weight to the perspectives represented by the two separate trees T1 and T2 in reaching any overall conclusions at T. But we might not want to give equal weight to T1 and T2. Instead, we might want one perspective to dominate another partially or totally, as in Example 20.

![](/api/attachments/4UU4NJNP/fulltext/images/2733143505df490c9d58ea6ff323869b06d46d2e8a1e262bd48beb4e07253790.jpg)

This subordinates T2 to T1, but not entirely. While all rules in the left branch of T1 are superior to any rules in T2, the rules in the middle and right branches of T1 and the rules in T2 have equal impact on the conclusions that hold at the top of the joined tree. If we want T1 to completely dominate T2, we have to add a bottom node to T1 (Example 21).

![](/api/attachments/4UU4NJNP/fulltext/images/06d74cde10ab82437a7b9d524c342dff71d7f3549a94f9d05aa9f2a5edbba79d.jpg)

Notice that in all these patterns, we can still recover all of the original opinions generated at the top of the separate tree T2, but we cannot be sure of recovering all of the original opinions of the separate tree T1. This is because T1 is now influenced by T2. To preserve all the original opinions of T1 while also indicating the dominance of T1 over T2 would require an additional copy of T1.

![](/api/attachments/4UU4NJNP/fulltext/images/48bf47a8f1367ffdbdb1acfc4394eb96a22b96f298b0bc73975e045b896f7bfe.jpg)

These models are plausible when we take them to represent multiple perspectives of a single agent. We sometimes compartmentalize our thinking, but we are theoretically capable of transcending any single perspective and using the cognitive resources of all available perspectives to arrive at an all-things-considered best conclusion. But this is not possible for situations where the different perspectives represent different agents. In this case, one agent has no direct access to the cognitive resources of another. This, of course, is where we use the notion of a curtain for an ordered theory developed in the last section.

We will consider one extended example using curtains, an example that also introduces the notion of a virtual agent. One agent often considers another agent to be an expert in one domain but not in every domain. Consider the case of a doctor and a lawyer each of whom considers the other to be an absolute authority in her particular domain. The doctor, however, disregards the medical opinions of the lawyer, and the lawyer disregards the legal opinions of the doctor. So the doctor-qua-doctor is an absolute medical authority for the lawyer, and the lawyer-qua-lawyer is an absolute legal authority for the doctor. These two new entities, doctor-qua-doctor and lawyer-qua-lawyer, are virtual agents.

To model this situation, we begin with an ordered theory with two simple trees:

![](/api/attachments/4UU4NJNP/fulltext/images/f0cf1f389443284d36e2826d659e90579f6e88db061b8c159b47dd35f408c874.jpg)

To this model we add two new nodes and two new connections. Then we impose a curtain on the theory in which the doctor, the lawyer, and the two new nodes are agents.

![](/api/attachments/4UU4NJNP/fulltext/images/84b1405fd2776f014ffe5bdbdf21c43170b7618e599478c7beed03bb2981ec17.jpg)

Here all the doctor's rules will be visible to the doctor, but only the doctor's medical rules and none of the lawyer's medical rules will be visible to the doctor-qua-doctor. The lawyer will see only the opinions of the doctor-qua-doctor, but these opinions will be superior to all of the lawyer's medical rules. In a similar way, the lawyer is made a legal authority for the doctor. In the diagram, agent nodes have access only to those rules below them that are represented in the same font (normal or italics) as the agent node.

## 13. Conclusions

Using ordered logic and ordered logic with curtains, we have an interesting tool for modeling multiple perspectives or societies of agents. It provides a method for resolving differences in perspectives, while making it possible to recover the individual conclusions. By explicitly modeling perspectives, it is possible to solve several problems encountered in commonsense reasoning in an attractive way. It also allows us to represent the knowledge of several agents in distinct theories and then combine them according to the relative superiority of some experts over others. Curtains can be used to protect the cognitive sources of one agent from others. When one agent is curtained off from another, the former may have access only to the reported opinions of the latter.

Ordered logic suggests methods for constructing experimental automated defeasible reasoning systems. Augmented with curtains, the application of ordered logic to problems with organizing processors in a parallel system and distributed computing can be investigated.

One possible use for this formalism is to model organizations and observe how the decision making process works with different organizational structures and with different knowledge available to the members of the organization. This could provide a way to uncover potential problems with existing organizational structures or a way to design an organization for a particular task.

Another use for ordered logic is in the implementation of planning systems involving multiple agents. Some of these agents may be automated, and some agents may take advice from others. In some cases, one agent will need to explicitly reason about the beliefs and intentions of other agents. This will require the addition of explicit epistemic reasoning capability to ordered logic. Hexmoor, Nute and Underwood (1990) have conducted initial investigations into the use of ordered logic for multi-agent planning.

## Appendix

The results cited in this paper, together with their proofs, are collected here for the convenience of the reader.

Lemma 1 If $T$ is an ordered theory, then not both $T|_{\overline{\alpha}}p^{+}$ and $T|_{\overline{\alpha}}p^{-}$ . $\square$

Proof We will show by induction on the depth of a proof tree that there cannot be two proof trees at $\alpha$ having top nodes labeled respectively $p^{+}$ and $p^{-}$ . Recall that by the depth of a proof tree we mean the number of nodes in a longest branch in the tree. Here and in the following proofs, we will denote the depth of a proof tree t by $|t|$ .

Basis step: Let $q$ be any literal and suppose there are two proof trees of depth 1 at $\alpha$ with top nodes $r$ and $r'$ labeled respectively $q^+$ and $q^-$ . Then $r$ must satisfy C1, and since $r$ has no child node, $\Rightarrow q \in f(\beta)$ for some $\beta \leq \alpha$ . Furthermore, $r'$ must satisfy C2, and since the antecedent of $\Rightarrow q$ is empty and $r'$ has no child node, $\Rightarrow \neg q \in f(\gamma)$ for $\gamma \leq \alpha$ such that $\gamma \not\leq \beta$ . But then since $r$ satisfies C1, $r$ has a child node labeled $a^-$ , where $a$ is in the antecedent of $\Rightarrow \neg q$ , which is impossible. So there cannot be two proof trees at $\alpha$ of depth 1 with top nodes labeled $q^+$ and $q^-$ .

Induction step: Let q be any literal. Assume that there are no proof trees at $\alpha$ of depth less than k having top nodes labeled respectively $s^{+}$ and $s^{-}$ for any literal s, and suppose there are two proof trees at $\alpha$ of depth less than or equal to k with top nodes r and $r'$ labeled respectively $q^{+}$ and $q^{-}$ . Then r must satisfy C1 and we can let $A \Rightarrow q \in f(\beta)$ for some $\beta \leq \alpha$ such that for each $a \in A$ , r has a child node labeled $a^{+}$ . By our inductive hypothesis, then, for each $a \in A$ , there is no proof tree at $\alpha$ of depth less than k with top node labeled $a^{-}$ . But $r'$ satisfies C2, so there is $\gamma \leq \alpha$ and $B \Rightarrow \neg q \in f(\gamma)$ such that $\gamma \not\prec$ $\beta$ and for each $b \in B$ , there is a child node of $r'$ labeled $b^{+}$ . Then since $r$ satisfies C1, there is $b \in B$ and a child node of $r$ labeled $b^{-}$ . But then there are proof trees at $\alpha$ of depth less than $k$ whose top nodes are labeled $b^{+}$ and $b^{-}$ , contradicting our inductive hypothesis. So there cannot be two proof trees at $\alpha$ of length less than or equal to $k$ with top nodes labeled $q^{+}$ and $q^{-}$ .

Lemma 1' If $T$ is an ordered theory, then not both $T\|_{\overline{\alpha}}p^{+}$ and $T\|_{\overline{\alpha}}p^{-}$ . $\square$

Proof For this proof, we will define the height of a node n in a proof tree to be the depth of the subtree with root node n. We will denote the height of n as $\|n\|$ .

Let $T$ be an ordered theory and let $\alpha$ be any perspective in $T$ . By induction on the height of a node in a proper proof tree, we will first show that there is no literal $q$ and nodes $n$ and $n'$ in proper proof trees at $\alpha$ in $T$ such that $n$ is labeled $q^{+}$ , $n'$ is labeled $q^{-}$ , and $n'$ does not satisfy condition C3 in Definition 6\*\*.

Basis step: Suppose $n$ and $n'$ are nodes in proper proof trees at $\alpha$ in $T$ such that $\| n \| = 1$ , $n$ is labeled $q^+, n'$ is labeled $q^-$ , and $n'$ does not satisfy C3. Then $n$ satisfies C1.1 and there is $\beta \leq \alpha$ and $\Rightarrow q \in f(\beta)$ . But $n'$ satisfies C2; so there is $\gamma \leq \alpha$ and $B \Rightarrow \neg q \in f(\gamma)$ such that $\gamma \not\prec \beta$ and for all $b \in B$ , $n'$ has a child node labeled $b^+$ . Since $n$ must also satisfy C1.2, there is $b^* \in B$ and a child node of $n$ labeled $b^{*-}$ . Since $\| n \| = 1$ , so this is impossible.

Induction step: Assume there is no literal $q$ and nodes $n$ and $n'$ in proper proof trees at $\alpha$ in $T$ such that $\| n \| < k$ , $n$ is labeled $q^+, n'$ is labeled $q^-$ , and $n'$ does not satisfy C3. Suppose $q$ is a literal and $n$ and $n'$ are nodes in proper proof trees at $\alpha$ in $T$ such that $\| n \| = k$ , $n$ is labeled $q^+, n'$ is labeled $q^-$ , and $n'$ does not satisfy C3. Then $n$ must satisfy C1.1, and we can let $\beta \leq \alpha$ and $A \Rightarrow q \in f(\beta)$ such that for each $a \in A$ , $n$ has a child node $n_a$ labeled $a^+$ .

Case 1: $n'$ satisfies C2.1 for $A \Rightarrow q$ . Then there is $a^* \in A$ and a child node $n_{a^*}'$ of $n'$ labeled $a^{*-}$ . If $n_{a^*}'$ does not satisfy C3, then since $\| n_{a^*} \| < k$ , we have contradicted our inductive hypothesis. But if $n_{a^*}'$ does satisfy C3, then there is a node above $n_{a^*}'$ which is also labeled $a^{*-}$ . Let $m$ be the highest node above $n_{a}^{\prime*}$ that is labeled $a^{*-}$ . Then m cannot satisfy C3 and once again we contradict our inductive hypothesis.

Case 2: $n'$ satisfies C2.2. Then there is $\gamma \leq \alpha$ and $B \Rightarrow \neg q \in f(\gamma)$ such that $\gamma \neq \beta$ and for each $b \in B$ , $n'$ has a child node $n_b'$ labeled $b^+$ . But since $n$ must also satisfy C1.2, there is $b' \in B$ and a child node $n_{b'}$ of $n$ labeled $b'^{-}$ . Note that $n_{b'}$ cannot satisfy C3 since it is a child node of $n$ which has a positive label. Since $n_{b'}$ and $n_b'$ are both of height less than $k$ , this contradicts or inductive hypothesis.

By inductive hypothesis, there cannot be a literal q and two nodes n and $n'$ in proper proof trees at $\alpha$ in T such that n is labeled $q^{+}$ , $n'$ is labeled $q^{-}$ , and $n'$ does not satisfy C3.

Now suppose there is a literal q and nodes n and $n'$ in proper proof trees at $\alpha$ in T such that one of n and $n'$ is labeled $q^{+}$ and the other is labeled $q^{-}$ . By our result above, we conclude that $n'$ must satisfy C3. Then there is another node above $n'$ which is also labeled $q^{-}$ and with no positively labeled nodes in between, and there is a highest such node m which cannot satisfy C3. So there are nodes n and m in proper proof trees at $\alpha$ in T such that n is labeled $q^{+}$ , m is labeled $q^{-}$ , and m does not satisfy C3. This again contradicts our earlier result. Since the root node of a proper proof tree cannot satisfy C3, our lemma follows immediately.

Lemma 2 If $T$ is an ordered theory, then not both $T|_{\overline{\alpha}}p^{+}$ and $T|_{\overline{\alpha}} \neg p^{+}$ . $\square$

Proof Suppose $T|_{\alpha}p^{+}$ and $T|_{\alpha}\neg p^{+}$ . Then there is a proof tree at $\alpha$ with top node r labeled $p^{+}$ and there is a proof tree at $\alpha$ with top node $r'$ labeled $\neg p^{+}$ . Since R satisfies C1, we can let $A\Rightarrow p\in f(\beta)$ for some $\beta\leq\alpha$ such that for each $a\in A$ , r has a child node labeled $a^{+}$ . And since $r'$ also satisfies C1, we can let $B\Rightarrow\neg p\in f(\gamma)$ such that $\gamma\leq\alpha$ and for each $b\in B$ , $r'$ has a child node labeled $b^{+}$ . If $\beta\not\prec\gamma$ , then since $r'$ satisfies C1, there is $a\in A$ such that some child node of $r'$ is labeled $a^{-}$ . But this violates Lemma 1; so $\beta<\gamma$ . By a similar argument, $\gamma<\beta$ . But this is impossible.

Lemma 2' If $T$ is an ordered theory, then not both $T\|_{\overline{\alpha}}p^{+}$ and $T\|_{\overline{\alpha}} \neg p^{+}$ . $\square$

Proof The proof is similar to that of Lemma 2, but the fact established in the proof of Lemma 1' that proper proof trees can't have nodes labeled with the same literal but of different sign.

Lemma 3 If T is an ordered theory and there is a proof tree of $p^{s}$ at perspective $\alpha$ in T, then there is a proof tree of $p^{s}$ at $\alpha$ in T with depth not exceeding N, where N is the number of propositional constants in T. ☐

Proof Assume that t is a proof tree at perspective $\alpha$ of $p^{s}$ . We need only show that if $|t| > N$ , then there is another proof tree at perspective $\alpha$ of $p^{s}$ with fewer nodes. Suppose $|t| > N$ . As a consequence of Lemma 1, there cannot be nodes in t labeled $q^{+}$ and $q^{-}$ . So no branch in t can have more than N nodes with distinct labels and the longest branch in t must have at least two nodes with identical labels. Consider a longest branch in t with at least one pair of nodes $n_{1}, n_{2}$ having the same label l such that $n_{1} < n_{2}$ . Let $t_{1}$ be the subtree of t with root $n_{1}$ , and $t_{2}$ the subtree of t with root $n_{2}$ . We can replace $t_{2}$ by $t_{1}$ , which will yield a tree $t'$ which is easily verified to be a proof tree of $p^{s}$ and which has fewer nodes than t.

Lemma 3' If $T$ is an ordered theory and there is a proper proof tree of $p^{s}$ at perspective $\alpha$ in $T$ , then there is a proof tree of $p^{s}$ at $\alpha$ in $T$ with depth not exceeding $(N+1)^{2}$ , where $N$ is the number of propositional constants in $T$ and $p$ .

Proof Assume that t is a proper proof tree of $p^{s}$ at perspective $\alpha$ in T such that $|t| > (N + 1)^{2}$ . We need only show that there is another proof tree $t^{*}$ of $p^{s}$ at $\alpha$ in T with fewer nodes than t. (We can assume that every non-root node in t is labeled $q^{+}$ or $q^{-}$ for some q occurring in T since a tree produced by pruning such nodes is easily verified to be a proper proof tree.)

Let $b$ be a longest branch in $t$ . If $b$ contains two nodes $m$ and $n$ labeled $q^{+}$ such that $n < m$ , let $t_{n}$ be the subtree with root node $n$ , let $t_{m}$ be the subtree with root node $m$ , and let $t^{*}$ be the tree that results from replacing $t_{m}$ in $t$ with $t_{n}$ . It is easily verified that $t^{*}$ is a proper proof tree of $p^{s}$ at $\alpha$ in $T$ . (NB: any node in $t_{n}$ that satisfies condition C3 in $t$ still satisfies C3 in $t^*$ since $n$ has a positive label.)

Suppose b does not have two distinct nodes labeled $q^{+}$ for any literal q. Suppose further that b does not contain a non-leaf node that satisfies C3. Then b can contain at most N consecutive non-leaf nodes with negative labels since otherwise some non-leaf node would satisfy C3. Each string of N consecutive negatively labeled nodes must be separated by a positively labeled node. But there can only be N of these since by our hypothesis no two positively labeled nodes have the same label. So there can be at most $N + 1$ strings of consecutive negatively labeled nodes and each of these can have at most N nodes in it. Thus, there can be at most $N(N + 1)$ negatively labeled non-leaf nodes in b, N positively labeled nodes in b, and 1 leaf node in b which satisfies C3, or a total of $(N + 1)^{2}$ nodes in b. But since $|t| > (N + 1)^{2}$ and b is a longest branch in t, b must have more than $(N + 1)^{2}$ nodes. So there must be a non-leaf node n in b which satisfies C3. We produce $t^{*}$ by pruning all nodes in t below n. $t^{*}$ is easily verified to be a proper proof tree of $p^{s}$ at $\alpha$ in T, and $t^{*}$ has fewer nodes than t.

Notice that in our proof of Lemma 3', we ignored the fact established in the proof of Lemma 1' that there cannot be two nodes in a proper proof tree where on node is labeled $q^{+}$ and the other is labeled $q^{-}$ for some literal q. This makes the proof simpler. We think that in fact $N+1$ is the limit on the depth of a proper proof tree, but this would be much more difficult to prove. Any easily computable limit on the depth of a proper proof tree is sufficient to establish our first theorem.

Theorem 1 There exists an algorithm which, given an ordered theory T, a perspective $\alpha$ in T, and an adorned literal $p^{s}$ , decides whether or not $T\vdash_{\overline{\alpha}}p^{s}$ . ☐

Proof We describe an algorithm which constructs a proof tree for $p^{s}$ at perspective $\alpha$ in T if there is one. Begin by writing down the top node and labeling it $p^{s}$ . Then at each succeeding step, do the following. Find the left-most node in the tree that does not satisfy any of the conditions in Definition 6. If there are N-1 nodes above this node, erase it and go to the next step. Otherwise, expand the node to satisfy one of the conditions in Definition 6. (Nodes are expanded by creating properly labeled child nodes below them.)

If every node satisfies Definition 6, the tree is a proof tree and $T|_{\overline{\alpha}} p^s$ . If the tree consists of only the root node and every way to expand the root node to satisfy Definition 6 has been tried, then $T \nVdash_{\alpha} p^s$ .

Since there are only finitely many nodes and rules in an ordered theory, there are also only finitely many ways to expand a node to satisfy Definition 6. This is enough to ensure that our algorithm always halts.

Theorem 1' There exists an algorithm which, given an ordered theory $T$ , a perspective $\alpha$ in $T$ , and an adorned literal $p^{s}$ , decides whether or not $T\|_{\overline{\alpha}}p^{s}$ . $\square$

Proof The proof is exactly like Theorem 1 except that we use $(N + 1)^2 - 1$ and Definition $6^{**}$ .

Theorem 2 Let $O = (\Sigma, \leq_{o}, R_{o}, f)$ be an ordered theory and let $\{p_{\alpha} : \alpha \in \Sigma\}$ be a set of sentence constants indexed by $\Sigma$ that do not occur in $O$ such that for all $\beta, \gamma \in \Sigma$ , if $\beta \neq \gamma$ , then $p_{\beta} \neq p_{\gamma}$ . Then there is a family of defeasible theories $\{D_{\alpha} : \alpha \in \Sigma\}$ and a superiority relation $\leq$ such that for all $\beta \in \Sigma$ and all $p \notin \{p_{\alpha} : \alpha \in \Sigma\}$ , $O|_{\overline{\beta}} p^{+}$ iff $D_{\beta}|_{\leq} Ep^{+}$ .

Proof Let $O = (\Sigma, \leq_{o}, R_{o}, f)$ be an ordered theory and let

$$
\begin{array}{r l}&{R _ {d} = \left\{\left\{p _ {\alpha} \right\} \cup A \Rightarrow p \colon A \Rightarrow p \in f (\alpha) \text {in} O \right\}}\\&{\qquad \cup \left\{p _ {\alpha} \rightarrow p _ {\beta} \colon \alpha , \beta \in \Sigma \quad \text {and} \quad \beta \le_ {o} \alpha \right\};}\\&{\leq = \left\{\langle A \Rightarrow p, B \Rightarrow q \rangle \colon p _ {\alpha} \in A, p _ {\beta} \in B, \right.}\\&{\qquad \text {and} \alpha \le_ {o} \beta \};}\\&{D _ {\beta} = (R _ {d}, \{p _ {\beta} \}) \text {for each} \beta \in \Sigma .}\end{array}
$$

Then for each $\beta \in \Sigma$ , $D_{\beta}$ is a defeasible theory, $\leq$ is a superiority relation on $D_{\beta}$ , and we will show that $O|_{\overline{\beta}}p^{+}$ iff $D_{\beta}|_{\leq}Ep^{+}$ where $p \notin \{p_{\alpha}: \alpha \in \Sigma\}$ .

Lemma A For all $\alpha, \beta \in \Sigma$ , there is a proof tree of $Ep_{\beta}^{+}$ in $D_{\alpha}$ using $\leq$ iff $\beta \leq_{o} \alpha$ , and there is a proof tree of $Ep_{\beta}^{-}$ in $D_{\alpha}$ using $\leq$ iff $\beta \not\leq_{o} \alpha$ .

Proof of Lemma A: If $\beta \leq_{o} \alpha$ , then $p_{\alpha} \to p_{\beta} \in R_{d}$ , and a tree with two nodes, a root node labeled $p_{\beta}^{+}$ and a child node labeled $p_{\alpha}^{+}$ constitutes a proof tree of $p_{\beta}^{+}$ for $D_{\alpha}$ using $\leq$ .

Suppose t is a proof tree for $D_{\alpha}$ using $\leq$ with root node r labeled $Ep_{\beta}^{+}$ . Then $\beta = \alpha$ or there is $p_{\gamma} \to p_{\beta} \in R_{d}$ with $\beta \leq_{o} \gamma$ and a child node n of r labeled $p_{\gamma}^{+}$ . The same is true for n, and so on. The final node in this tree must be labeled $p_{\alpha}^{+}$ since this is the only initial premise in $D_{\alpha}$ . Since $\leq_{o}$ is transitive, it follows that $\beta \leq_{o} \alpha$ .

Suppose $\beta \not\leq_{o}\alpha$ . We construct the requisite proof tree as follows. Let the root node $r$ be labeled $Ep_{\beta}^{-}$ . Create a child node of $r$ labeled $p_{\beta}^{-}$ , and for each $p_{\delta} \to p_{\beta} \in R_{d}$ , create a child node of $r$ labeled $Ep_{\delta}^{-}$ . By the definition of $R_{d}$ , $\beta \leq_{o}\delta$ for each such $\delta$ , and thus $p_{\delta} \neq p_{\alpha}$ . Since there are by definition no other rules in $R_{d}$ with consequent $p_{\beta}$ , $r$ satisfies $D4$ . We continue in this way for each child node of $r$ , and for their child nodes, and so on. Eventually, we will produce leaf nodes all of which are labeled $p_{\delta}^{-}$ for some top node $\delta$ in $O$ . Since by our definition of $R_{d}$ , there is no $p \to p_{\delta} \in R_{\delta}$ if $\delta$ is a top node in $O$ , these leaf nodes also satisfy $D2$ . So the completed tree is a proof tree for $D_{\alpha}$ using $\leq$ .

Suppose $t$ is a proof tree for $D_{\alpha}$ using $\leq$ with root node $r$ labeled $Ep_{\beta}^{-}$ . If $\beta \leq_{o} \alpha$ , then $p_{\alpha} \to p_{\beta} \in R_{d}$ , $r$ has a child node labeled $p_{\alpha}^{-}$ , and by $D2 \, p_{\alpha} \notin \{p_{\alpha}\}$ , which is clearly false. So $\beta \not\leq_{o} \alpha$ .

This completes our proof of Lemma A. Using this lemma, let $t_{\alpha}$ be a proof tree of $Ep_{\alpha}^{-}$ in $D_{\beta}$ using $\leq$ for each $\alpha \in \Sigma$ such that $\alpha \not\leq_{o} \beta$ .

(1) First, we will show that if $p \notin \{p_{\alpha} : \alpha \in \Sigma\}$ and $O|_{\overline{\beta}} p^{+}$ , then $D_{\beta}|_{\leq} Ep^{+}$ . We will use induction on the depth of the proof tree to show that for each proof tree $t$ at $\beta$ in $O$ , either

(OI1) $t$ is a proof tree of $p^+$ at $\beta$ in $O$ and $D_{\beta} \models_{\leq} E p^{+}$ , or

(OI2) $t$ is a proof tree of $p^{-}$ at $\beta$ in $O$ and $D_{\beta} \models_{\leq} Ep^{-}$ .

Basis step: Assume that t is a proof tree at $\beta$ with root node r labeled l such that $|t|=1$ . Then r must satisfy C1 or C2 (Definition 6).

Case 1: r satisfies C1. Then $l = p^{+}$ and we can let $\alpha \leq_{o} \beta$ such that $\Rightarrow p \in f(\alpha)$ and since r has no child node,

there is no $\gamma \leq_{o} \beta$ and $B \Rightarrow \neg p \in f(\gamma)$

such that $\gamma \prec_{o} \alpha$ .

(1)

Then $p_{\alpha} \Rightarrow p \in R_d$ . Because $\alpha \leq_o \beta$ , $p_{\beta} \to p_{\alpha} \in R_d$ . So there is clearly a proof tree for $p_{\alpha}^{+}$ in $D_{\beta}$ using $\leq$ , and therefore also for $Ep_{\alpha}^{+}$ . Let $t_{\alpha}$ be a proof tree for $Ep_{\alpha}^{+}$ in $D_{\beta}$ . Furthermore, since there is no $A \to \neg p \in R_d$ , a single node labeled $\neg p^{-}$ constitutes a proof tree $t_{\neg p}$ of $\neg p^{-}$ in $D_{\beta}$ using $\leq$ .

Construct a tree $t^*$ with root $r'$ labeled $Ep^+$ with subtrees $t_\alpha, t_{\neg p}$ , and $t_\gamma$ (with root node labeled $Ep_\gamma^-$ ; Lemma A) for every $\gamma \not\leq_o \beta$ . $r'$ satisfies D3.1 for $p_\alpha \Rightarrow p$ because of $t_\alpha$ , and $r'$ satisfies D3.3 because of $t_{\neg p}$ . There is no $A \to \neg p \in R_d$ or $A \rightsquigarrow \neg p \in R_d$ . Suppose $\{p_\gamma\} \cup B \Rightarrow \neg p \in R_d$ . Then $B \Rightarrow \neg p \in f(\gamma)$ , and by (1), either $\gamma <_o \alpha$ or $\gamma \not\leq_o \beta$ . In the first case, $\{p_\gamma\} \cup B \Rightarrow \neg p < p_\alpha \Rightarrow p$ ; in the second case, $t_\gamma$ is a subtree attached to $r'$ whose root node is labeled $Ep_\gamma^-$ . So $r'$ satisfies D3.2, $t^*$ is a proof tree of $Ep^+$ in $D_\beta$ using $\leq, D_\beta|_{\leq}Ep^+$ , and $t$ satisfies OI1.

Case 2: $r$ satisfies C2. Then $l = p^{-}$ and for every rule $A \Rightarrow p \in f(\alpha)$ with $\alpha \leq_{o} \beta$ , there is a rule $\Rightarrow \neg p \in f(\gamma)$ with $\gamma \not\prec_{o} \alpha$ and $\gamma \leq_{o} \beta$ (since $r$ has no child nodes). Since there is no $A \to p \in R_{d}$ , a single node labeled $p^{-}$ constitutes a proof tree $t_{p}$ of $p^{-}$ in $D_{\beta}$ using $\leq$ . Consider a rule $\{p_{\delta}\} \cup A \Rightarrow p \in R_{d}$ , then either $\delta \not\leq_{o} \beta$ or there is a rule $p_{\gamma} \Rightarrow \neg p \in R_{d}$ with $\gamma \leq_{o} \beta$ and $\gamma \not\prec_{o} \delta$ . If $\delta \not\leq_{o} \beta$ , there is a proof tree $t_{\delta}$ of $Ep_{\delta}^{-}$ (Lemma A). Otherwise, $p_{\gamma} \Rightarrow \neg p \not\leqslant \{p_{\delta}\} \cup A \Rightarrow p$ , and there is a proof tree $t_{\gamma}$ of $Ep_{\gamma}^{+}$ , because $\gamma \leq_{o} \beta$ .

Construct a tree $t^*$ with root node $r'$ labeled $Ep^-$ with subtree $t_p$ , subtrees $t_\gamma$ of $Ep_\gamma^+$ for each $\{p_\alpha\} \cup A \Rightarrow p$ where $\alpha \leq_o \beta$ and subtrees $t_\delta$ (with root node $Ep_\delta^+$ ; Lemma A) for each $\delta \not\leq_o \beta$ . Then $r'$ satisfies $D4, D_\beta|_{\leq}Ep^-$ , and $t$ satisfies OI2.

Induction step: Assume that for each proof tree t at $\beta$ in O, if $|t| < k$ , then t satisfies OI1 or OI2. Suppose t is a proof tree at $\beta$ in O with root node r labeled l such that $|t| = k$ .

Case 1: r satisfies C1. Then $l = p^{+}$ , and we can let $\alpha \leq_{o} \beta$ and $A \Rightarrow p \in f(\alpha)$ such that r has a child node labeled $a^{+}$ for each $a \in A$ , and for each $\gamma \leq_{o} \beta$ and $B \Rightarrow \neg p \in f(\gamma)$ such that $\gamma \neq_{o} \alpha$ , we can let $b \in B$ such that r has a child node labeled $b^{-}$ . Because $\alpha \leq_{o} \beta$ , $p_{\beta} \to p_{\alpha} \in R_{d}$ , and we can let $t_{\alpha}$ be a proof tree of $Ep_{\alpha}^{+}$ in $D_{\beta}$ using $\leq$ . Since each child node of r labeled $a^{+}$ for $a \in A$ is the root node of a proof tree at $\beta$ in O of depth less than k, this subtree satisfies OI1 by induction and we can let $t_a$ be a proof tree of $Ea^+$ in $D_\beta$ using $\leq$ . Suppose $\{p_\gamma\} \cup B \Rightarrow \neg p \in R_d$ , $\{p_\gamma\} \cup B \Rightarrow \neg p \not\leq \{p_\alpha\} \cup A \Rightarrow p$ , and $\gamma \leq_o \beta$ . Then $B \Rightarrow \neg p \in f(\gamma)$ , $\gamma \not\leq_o \alpha$ , and we can let $b \in B$ such that $r$ has a child node $n$ labeled $b^-$ . But the subtree with root node $n$ is of depth less than $k$ ; so by induction it satisfies OI2 and we can let $t_b$ be a proof tree of $Eb^-$ in $D_\beta$ using $\leq$ . Furthermore, since there is no $A \to \neg p \in R_d$ , a single node labeled $\neg p^-$ constitutes a proof tree $t_{\neg p}$ of $\neg p^-$ in $D_\beta$ using $\leq$ .

Construct a tree $t^*$ with root node $r'$ labeled $Ep^+$ , with subtree $t_\alpha$ , subtree $t_{\neg p}$ , subtrees $t_a$ for each $a \in A$ , subtrees $t_b$ for each $\{p_\gamma\} \cup B \Rightarrow \neg p \in R_d$ such that $\{p_\gamma\} \cup B \Rightarrow \neg p \not\leqslant \{p_\alpha\} \cup A \Rightarrow p$ , and $\gamma \leq_o \beta$ , and subtrees $t_\delta$ (with root node labeled $Ep_\delta^-$ ; Lemma A) for each $\delta \not\leqslant_o \beta$ . Then $r'$ satisfies $D3, D_\beta|_{\leq}Ep^+$ , and $t$ satisfies OI1.

Case 2: $r$ satisfies C2. Then $l = p^{-}$ , and for every $\alpha \leq_{o} \beta$ and $A \Rightarrow p \in f(\alpha)$ , either there is $a \in A$ and a child node of $r$ labeled $a^{-}$ , or there is $\gamma \leq_{o} \beta$ and $B \Rightarrow \neg p \in f(\gamma)$ such that $\gamma \not\prec_{o} \alpha$ and for each $b \in B$ , $r$ has a child node labeled $b^{+}$ . Since there is no $A \to p \in R_{d}$ , a tree $t_{p}$ consisting of a single node labeled $p^{-}$ constitutes a proof tree of $p^{-}$ in $D_{\beta}$ using $\leq$ . Suppose $\{p_{\alpha}\} \cup A \Rightarrow p \in R_{d}$ and $\alpha \leq_{o} \beta$ . If there is $a \in A$ and a child node $n$ of $r$ labeled $a^{-}$ , then the subtree with root $n$ is of depth less than $k$ , and by induction we can let $t_{a}$ be a proof tree of $Ea^{-}$ in $D_{\beta}$ using $\leq$ . On the other hand, if there is $\gamma \leq_{o} \beta$ and $B \Rightarrow \neg p \in f(\gamma)$ such that $\gamma \not\prec_{o} \alpha$ and $r$ has a child node labeled $b^{+}$ for each $b \in B$ , then by induction for each $b \in B$ we can let $t_{b}$ be a proof tree of $Eb^{+}$ in $D_{\beta}$ using $\leq$ . Furthermore, since $\gamma \leq_{o} \beta$ , $p_{\beta} \to p_{\gamma} \in R_{d}$ , and there is clearly a proof tree $t_{\gamma}$ of $Ep_{\gamma}^{+}$ in $D_{\beta}$ using $\leq$ . Construct a tree $t^{*}$ with root node $r$ labeled $Ep^{-}$ , with subtree $t_{p}$ , subtree $t_{a}$ or the collection of trees $t_{b}$ and $t_{\gamma}$ as required for each $\{p_{\alpha}\} \cup A \Rightarrow p \in R_{d}$ where $\alpha \leq_{o} \beta$ , and subtrees $t_{\delta}$ (with root node labeled $Ep_{\delta}^{-}$ ; Lemma A) for each $\delta \not\leq_{o} \beta$ . Then $r'$ satisfies D4, $D_{\beta}|_{\leq}Ep^{-}$ , and $t$ satisfies OI2.

(2) Next, we will show that if $p \notin \{p_{\alpha} : \alpha \in \Sigma\}$ and $D_{\beta}|_{\leq} Ep^{+}$ , then $O|_{\overline{\beta}} p^{+}$ . Let $t$ be a proof tree of $Ep^{+}$ or $Ep^{-}$ in $D_{\beta}$ using $\leq$ , where $p \notin \{p_{\alpha} : \alpha \in \Sigma\}$ . For each node $n$ in $t$ , let $\| n \|$ be the number of nodes below $n$ that are labeled either $Eq^{+}$ or $Eq^{-}$ for some $q \notin \{p_{\alpha} : \alpha \in \Sigma\}$ . Using induction on $\| n \|$ , we will show that for every node n in t, if n is labeled $Eq^{+}$ or $Eq^{-}$ for some $q \notin \{p_{\alpha}: \alpha \in \Sigma\}$ , then n satisfies one of the following conditions:

DI1. $n$ is labeled $Eq^{+}$ and $O|_{\overline{\beta}}q^{+}$ .

DI2. $n$ is labeled $Eq^{-}$ and $O|_{\overline{\beta}}q^{-}$ .

Basis step: $\| n\| = 0$

Case 1: n is labeled $Eq^{+}$ . We will show that a tree $t^{*}$ consisting of a single node r labeled $q^{+}$ is a proof tree at $\beta$ in O.

Since there is no $A \to q \in R_d$ , let $\{p_\alpha\} \cup A \Rightarrow q \in R_d$ such that for all $a \in A$ , $n$ has a child node labeled $Ea^+$ . But since $\| n \| = 0$ , $A = \emptyset$ . So $p_\alpha \Rightarrow q \in R_d$ and $\Rightarrow q \in f(\alpha)$ . Furthermore, since $t$ has a node labeled $Eq^+$ , $\alpha \leq_o \beta$ by Lemma A. So $r$ satisfies C1.1.

Suppose $\gamma \leq_{o} \beta$ , $\gamma \not\prec_{o} \alpha$ , and $B \Rightarrow \neg q \in f(\gamma)$ . Then $\{p_{\gamma}\} \cup B \Rightarrow \neg q \in R_{d}$ and $\{p_{\gamma}\} \cup B \Rightarrow \neg q \not\prec p_{\alpha} \Rightarrow q$ . So we can let $b \in \{p_{\gamma}\} \cup B$ such that $n$ has a child node labeled $Eb^{-}$ . Since $\| n \| = 0$ , $b \notin B$ , $n$ has a child node labeled $Ep_{\gamma}^{-}$ , and $\gamma \not\prec_{o} \beta$ , contradicting our assumption. So there is no $\gamma \leq_{o} \beta$ , and $B \Rightarrow \neg q \in f(\gamma)$ such that $\gamma \not\prec_{o} \alpha$ . So $r$ satisfies C1.2.

Case 2: n is labeled $Eq^{-}$ . We will show that a tree $t^{*}$ consisting of a single node r labeled $q^{-}$ is a proof tree at $\beta$ in O. Suppose

$\alpha \leq_{o} \beta$ and $A \Rightarrow q \in f(\alpha)$ .

(2)

Then $\{p_{\alpha}\} \cup A \Rightarrow q \in R_d$ .

Case 2.1: There is $a \in \{p_{\alpha}\} \cup A$ and a child node of $n$ labeled $Ea^{-}$ . Since $\| n \| = 0$ , $a = p_{\alpha}$ . Then $\alpha \not\leq_{o} \beta$ , contradicting (2); so this case is impossible.

Case 2.2: There is $\{p_{\gamma}\} \cup B \Rightarrow \neg q \in R_d$ such that $\{p_{\gamma}\} \cup B \Rightarrow \neg q \not\prec \{p_{\alpha}\} \cup A \Rightarrow q$ and for all $b \in \{p_{\gamma}\} \cup B$ , $n$ has a child node labeled $Eb^{+}$ . Since $\| n \| = 0$ , $B = \emptyset$ . And since $\{p_{\gamma}\} \cup B \Rightarrow \neg q \not\prec \{p_{\alpha}\} \cup A \Rightarrow q$ , $\gamma \not\prec_{o} \alpha$ ; and since $D_{\beta}|_{\leq} Ep_{\gamma}^{+}$ , $\gamma \leq_{o} \beta$ . So there is $\gamma \leq_{o} \beta$ and $\Rightarrow \neg q \in f(\gamma)$ such that $\gamma \not\prec_{o} \alpha$ .

So $r$ satisfies C2, and $O|_{\beta}q^{-}$ .

Induction step: This is like the basis step except that we invoke our inductive hypothesis for any child node of n which is labeled $Er^{+}$ or $Er^{-}$ for $r \notin \{p_{\alpha}: \alpha \in \Sigma\}$ to establish that there is a proof tree of $r^{+}$ or $r^{-}$ at $\beta$ in O; then we attach these as subtrees to the root node as we construct our proof tree of $r^{+}$ or $r^{-}$ at $\beta$ in O.

Theorem 3 If $T$ is an ordered theory, $M$ is a strong model of $T$ , and $T|_{\overline{\alpha}}p^{+}$ , then $p\in M(\alpha)$ . $\square$

Proof The proof is by induction on the depth $|t|$ of the proof tree $t$ of $p^{+}$ at $\alpha$ .

Basis step: Suppose $t$ is a proof tree of $p^+$ at $\alpha$ and $|t| = 1$ . Then there is $\Rightarrow p \in f(\beta)$ with $\beta \leq \alpha$ , and

there is no rule $B \Rightarrow \neg p \in f(\gamma)$

with $\gamma \leq \alpha$ and $\gamma \nless \beta (1)$ .

Since $\Rightarrow p$ is applicable at $\alpha$ in $M$ , either m1 or m3 (Definition 8) must hold for $\Rightarrow p$ and $\alpha$ . But (m3) contradicts (1); so m1 applies and $p \in M(\alpha)$ .

Induction step: Assume that for each q for which there exists a proof tree $t'$ of $q^{+}$ at $\alpha$ , with $|t'| < k$ , $q \in M(\alpha)$ . Suppose t is a proof tree with root node r of $p^{+}$ at $\alpha$ , and $|t| = k$ . Let $A \Rightarrow p \in f(\beta)$ with $\beta \leq \alpha$ such that

$r$ has a child node with label $a^{+}$

for every $a \in A(1)$ ,

and $r$ has a child node with label $b^{-}$

for a $b \in B$ for each rule $B \Rightarrow \neg p \in f(\gamma)$

where $\gamma \leq \alpha$ and $\gamma \neq \beta(2)$ .

From (1) by induction, $A \subseteq M(\alpha)$ and m1 or m3 must hold for $A \Rightarrow p$ and $\alpha$ . Condition m3 implies that there exists a rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \not\prec \beta$ , such that $B \subseteq \mu^{*}(\alpha)$ and for each $b \in B$ there is a proof tree for $b^{+}$ at $\alpha$ ; but by the proof of Lemma 3', this contradicts (2). Hence, m1 holds for rule $A \Rightarrow p$ at $\alpha$ and $p \in M(\alpha)$ .

Lemma 4 If $T$ is a properly ordered theory, then not $T\|_{\overline{\alpha}}p^{+}$ implies $T\|_{\overline{\alpha}}p^{-}$ . $\square$

Proof The proof is by induction on the maximum number $\eta(p)$ of negative edges found on any path to p in the dependency digraph $G_{\alpha}$ . (Note that $\eta(p)$ is well defined since T is properly ordered at $\alpha$ .)

Basis step: Suppose $\eta(p)=0$ . This means that there is no path to $p$ passing through

a negative edge.

(1)

In particular,

for each rule $A \Rightarrow p \in f(\beta)$ with $\beta \leq \alpha$ ,

there is no rule $B \Rightarrow \neg p \in f(\gamma)$

with $\gamma \leq \alpha$ and $\gamma \neq \beta$ .

(2)

From (1), no putative proof tree of $p^{-}$ at $\alpha$ contains a positively labeled node. The absence of a proof tree of $p^{+}$ with $\eta(p)=0$ implies that for each rule $A\Rightarrow p\in f(\beta)$ with $\beta\leq\alpha$ , either there is $a\in A$ for which there is no proof tree of $a^{+}$ , or there is a rule $B\Rightarrow\neg p\in f(\gamma)$ with $\gamma\leq\alpha$ and $\gamma\not\prec\beta$ such that there is no $b\in B$ for which there is a proof tree of $b^{-}$ . The latter possibility would contradict (2). So for each rule $A\Rightarrow p\in f(\beta)$ with $\beta\leq\alpha$ there is $a\in A$ for which there is no proof tree of $a^{+}$ .

Construct a tree t for $p^{-}$ with root r labeled $p^{-}$ as follows. For each rule $A \Rightarrow p \in f(\beta)$ with $\beta \leq \alpha$ , we know that there is $a \in A$ for which there is no proof tree of $a^{+}$ , with $\eta(a) = 0$ . Then the same procedure can be followed to create a tree for $a^{-}$ at $\beta$ in O; attach this tree to r as a subtree. The expansion of a path of the tree for $p^{-}$ stops when we reach a node $m_{1}$ labeled $q^{-}$ for which either

(i) there is a node $\mathfrak{m}_2$ labeled $q^{-}$ which is an ancestor of $\mathfrak{m}_1$ , or

(ii) there are no rules $C \Rightarrow q \in f(\gamma)$ with $\gamma \leq \alpha$ .

$t$ is a proof tree for $p^{-}$ .

Induction step: Assume that the lemma holds for every q with $\eta(q) < k$ and suppose $\eta(p) = k$ . By C1, we know that the absence of a proof tree of $p^{+}$ implies that for every rule $A \Rightarrow p \in f(\beta)$ with $\beta \leq \alpha$ , either

there is $a \in A$ for which there is no proof tree

of $a^+$

(3)

or

there is a rule $B \Rightarrow \neg p \in f(\gamma)$

with $\gamma \leq \alpha$ and $\gamma \neq \beta$ such that there is

no $b \in B$ for which there is a proof tree of $b^{-}$ .

(4)

If (3) is the case, then for this $a \in A$ for which there is no proof tree for $a^{+}$ at $\alpha$ , either $\eta(a) < \eta(p)$ , in which case by induction there is a proof tree $t_{a}$ of $a^{-}$ at $\alpha$ , or $\eta(a) = \eta(p)$ . If (4) is the case, then for the rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \neq \beta$ , there are negative edges $(b, p)$ in the dependency digraph $G_{\alpha}$ for each $b \in B$ , so that $\eta(b) < \eta(p)$ for each $b \in B$ . By induction, for this rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \neq \beta$ , there is a proof tree $t_{b}$ of $b^{+}$ for each $b \in B$ .

Construct a tree t with root r labeled $p^{-}$ and for each $\beta \leq \alpha$ and $A \Rightarrow p \in f(\beta)$ , either

(a) there is a rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \neq \beta$ such that there is a proof tree $t_b$ of $b^+$ for each $b \in B$ . Let these proof trees be subtrees of $r$ . The expansion of the tree is finished where this rule is concerned.

(b) there is $a \in A$ with $\eta(a) < \eta(p)$ for which there is a proof tree for $a^{-}$ at $\alpha$ . Let this proof tree be a subtree of node $r$ . The expansion of the tree is finished where this rule is concerned.

(c) there is $a \in A$ with $\eta(a) = \eta(p)$ for which there is no proof tree for $a^{+}$ at $\alpha$ . Use the same procedure to create a tree for $a^{-}$ , and let this tree be a subtree of r.

Each path in the tree will terminate either with a node that satisfies case (a) or (b), or with a node $m_{1}$ labeled $q^{-}$ for which either

(i) there is a node $\mathfrak{m}_2$ labeled $q^{-}$ which is an ancestor of $\mathfrak{m}_1$ , and every node between $\mathfrak{m}_1$ and $\mathfrak{m}_2$ is having a negative label, or

(ii) there is no $C \Rightarrow q \in f(\gamma)$ with $\gamma \leq \alpha$ .

$t$ is a proof tree for $p^{-}$ .

Lemma 5 If $T$ is a properly ordered theory, then the proper conservative extension $\mu^{*}$ (defined now using $\Vdash$ ) is a strong model. $\square$

Proof Let $\alpha, \beta \in \Sigma$ such that $\beta \leq \alpha$ and let $A \Rightarrow p \in f(\beta)$ . We have to show that $A \Rightarrow p$ and $\alpha$ satisfy one of the conditions m1, m2 or m3 in $\mu$ .

Case 1: $A \not\subseteq \mu^{*}(\alpha)$ . Then $A \Rightarrow p$ is not applicable at $\alpha$ and m2 is satisfied.

Case 2: $A \subseteq \mu^{*}(\alpha)$ and there exists a proof tree of $a^{+}$ at $\alpha$ for each $a \in A$ .

Case 2.1: There is a rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \not\prec \beta$ such that $B \subseteq \mu^{*}(\alpha)$ . Then there is a proof tree of $b^{+}$ at $\alpha$ for each $b \in B$ . By Lemma 1, there is a rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \not\prec \beta$ such that there is no $b \in B$ for which there exists a proof tree for $b^{-}$ at $\alpha$ .

If there is a proof tree for $p^{+}$ at $\alpha$ , then for each rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \neq \beta$ there is $b \in B$ for which there is a proof tree for $b^{-}$ at $\alpha$ , which contradicts (5). Therefore, there is no proof tree of $p^{+}$ at $\alpha$ , $p \notin \mu^{*}(\alpha)$ , and m3 is satisfied.

Case 2.2: For each rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \neq \beta$ , there is $b \in B$ such that $b \notin$ $\mu^{*}(\alpha)$ . Then there is no proof tree for $b^{+}$ for this $b \in B$ . By Lemma 4, for each rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \not\prec \beta$ , there is $b \in B$ for which there is a proof tree for $b^{-}$ at $\alpha$ . Let $t_{B}$ be a proof tree for $b^{-}$ for this $b \in B$ .

Construct a tree t with root labeled $p^{+}$ and subtrees for $a^{+}$ for each $a \in A$ , and subtrees $t_{B}$ for each rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha$ and $\gamma \neq \beta$ . C1 is satisfied for the root node with label $p^{+}$ , t is a proof tree for $p^{+}$ at $\alpha$ , $p \in \mu^{*}(\alpha)$ , and m1 is satisfied.

Theorem 4 If $T$ is a properly ordered theory and $p\in M(\alpha)$ for every strong model $M$ of $T$ , then $T\|_{\overline{\alpha}}p^{+}$ . $\square$

Proof By Lemma 5, $\mu$ is a strong model of $T$ . Therefore, $p \in \mu^{*}(\alpha)$ , so that by definition of $\mu^{*}$ , $T\|_{\overline{\alpha}} p^{+}$ .

Lemma 6 If $T = (\Sigma, \leq, R, f)$ is a properly ordered theory, then $\leq_T$ is a partial order on the weak models of $T$ .

Proof a) $\leq_{T}$ is reflexive since clearly $M \leq_{T} M$ for each model $M$ of $T$ .

b) To show that $\leq_{T}$ is antisymmetric, suppose $M_{1} \leq_{T} M_{2}$ , $M_{2} \leq_{T} M_{1}$ , $\alpha \in \Sigma$ , and $p \in M_{1}(\alpha) - M_{2}(\alpha)$ . Since $M_{1} \leq_{T} M_{2}$ , there is $q \in M_{2}(\alpha) - M_{1}(\alpha)$ such that $q$ dom $_{\alpha} p$ . And since $M_{2} \leq_{T} M_{1}$ , there is a $r \in M_{1}(\alpha) - M_{2}(\alpha)$ such that $r$ dom $_{\alpha} q$ . Again, since $M_{1} \leq_{T} M_{2}$ , there is a $s \in M_{2}(\alpha) - M_{1}(\alpha)$ such that $s$ dom $_{\alpha} r$ , ...

Because for each $\alpha \in \Sigma$ , $M_1(\alpha)$ and $M_2(\alpha)$ are finite, we obtain a negative cycle after a certain sequence of literals, which contradicts the fact that $T$ is properly ordered. Therefore, there is no perspective $\alpha$ for which there is a $p \in M_1(\alpha) - M_2(\alpha)$ , and $M_1(\alpha) \subseteq M_2(\alpha)$ for each $\alpha \in \Sigma$ .

In a similar way, we can show that for each $\alpha \in \Sigma$ , $M_2(\alpha) \subseteq M_1(\alpha)$ .

Then $M_1(\alpha) = M_2(\alpha)$ for each $\alpha \in \Sigma$ , and $M_1 = M_2$ .

c) To show that $\leq_T$ is transitive, suppose $M_1 \leq_T M_2$ , $M_2 \leq_T M_3$ , and $p \in M_1(\alpha) - M_3(\alpha)$ .

Case 1: $p \notin M_2(\alpha)$ . Then $p \in M_1(\alpha) - M_2(\alpha)$ . Since $M_1 \leq_T M_2$ , there is $q \in M_2(\alpha) - M_1(\alpha)$ such that $q \operatorname{dom}_{\alpha} p$ .

Case 1.1: $q \in M_3(\alpha)$ . Then $q \in M_3(\alpha) - M_1(\alpha)$ and $q \operatorname{dom}_{\alpha} p$ .

Case 1.2: $q \notin M_3(\alpha)$ . Then $q \in M_2(\alpha) - M_3(\alpha)$ . Since $M_2 \leq_T M_3$ , there is $r \in M_3(\alpha) - M_2(\alpha)$ such that $r \operatorname{dom}_\alpha q$ and therefore $r \operatorname{dom}_\alpha p$ .

Case 1.2.1: $r \notin M_1(\alpha)$ . Then let $r \in M_3(\alpha) - M_1(\alpha)$ such that $r \operatorname{dom}_{\alpha} p$ .

Case 1.2.2: $r \in M_1(\alpha)$ . Then $r \in M_1(\alpha) - M_2(\alpha)$ . Since $M_1 \leq_T M_2$ , let $s \in M_2(\alpha) - M_1(\alpha)$ such that $s \operatorname{dom}_\alpha r$ and therefore $s \operatorname{dom}_\alpha p$ .

Case 1.2.2.1: $s \in M_3(\alpha)$ . Then $s \in M_3(\alpha) - M_1(\alpha)$ and $s \operatorname{dom}_{\alpha} p$ .

Case 1.2.2.2: $s \notin M_3(\alpha)$ . We can continue as in case 1.2.

Because for each $\alpha \in \Sigma$ , $M_1(\alpha)$ , $M_2(\alpha)$ and $M_3(\alpha)$ are finite and $T$ is properly ordered, this sequence has to stop. So there is a $q \in M_3(\alpha) - M_1(\alpha)$ such that $q \operatorname{dom}_{\alpha} p$ .

Case 2: This is analogous to case 1.

Theorem 5 (soundness and completeness) The conservative extension $\mu^{*}$ of a properly ordered theory $T$ is the unique minimal model, according to $\leq_{T}$ , in the class of all weak models of $T$ .

Proof Let $T = (\Sigma, \leq, R, f)$ be a properly ordered theory and let M be a (weak) model of T, $\alpha \in \Sigma$ and $p \in \mu^{*}(\alpha)$ . Let t be a proof tree of $p^{+}$ at $\alpha$ in T. The proof is by induction of $|t|$ .

Basis step: Assume that t is a proof tree of $p^{+}$ at $\alpha$ for T with $|t|=1$ . The root node r of t with label $p^{+}$ must satisfy C1. Let $\Rightarrow p\in f(\beta)$ , $\beta\leq\alpha$ such that

there is no rule $B \Rightarrow \neg p \in f(\gamma)$

with $\gamma \leq \alpha$ and $\gamma \neq \beta$ .

(1)

Suppose $p \notin M(\alpha)$ . The rule $\Rightarrow p \in f(\beta)$ is applicable at $\alpha$ ; so $\Rightarrow p \in f(\beta)$ has to be defeated at $\alpha$ in model $M$ , and there has to be a rule $D \Rightarrow \neg p \in f(\delta)$ with $\delta \leq \alpha$ and $\delta \nmid \beta$ such that $D \subseteq M(\alpha)$ , which contradicts (1). Therefore, $p \in M(\alpha)$ and we can conclude that for each $\alpha \in \Sigma$ and for each $p \in \mu^{*}(\alpha) - M(\alpha)$ (such that there is a proof tree of $p^{+}$ with depth 1), there is a $q \in M(\alpha) - \mu^{*}(\alpha)$ such that $q \operatorname{dom}_{\alpha} p$ .

Induction step: Assume that the theorem holds for each $\alpha \in \Sigma$ and $s \in \mu^{*}(\alpha) - M(\alpha)$ such that there is a proof tree $t$ for $s^{+}$ at $\alpha$ with $|t| < k$ . Suppose $p \in \mu^{*}(\alpha)$ such that there is a proof tree $t$ for $p^{+}$ at $\alpha$ such that $|t| = k$ . The root node $r$ with label $p^+$ has to satisfy C1. Let $A \Rightarrow p \in f(\beta)$ with $\beta \leq \alpha$ such that

r has a child node with label $a^{+}$ for each $a \in A$ , (2)

and

for each rule $B \Rightarrow \neg p \in f(\gamma)$

with $\gamma \leq \alpha$ and $\gamma \nmid \beta$ , there is $b \in B$

and a child node of $r$ labeled $b^{-}$ .

(3)

If $p \notin M(\alpha)$ , then either $A \Rightarrow p \in f(\beta)$ is not applicable at $\alpha$ , i.e. $A \not\subseteq M(\alpha)$ (m2), or $A \Rightarrow p \in f(\beta)$ is defeated at $\alpha$ , i.e. there is a rule $B \Rightarrow \neg p \in f(\gamma)$ with $\gamma \leq \alpha, \gamma \neq \beta$ , and $B \subseteq M(\alpha)$ (m3). If (m3) holds, then by (3) that there is $b \in B$ such that $b \notin \mu^{*}(\alpha)$ . By definition of the dependency digraph $G_{\alpha}$ , there is a negative path from $b$ to $p$ ; so $b \in M(\alpha) - \mu^{*}(\alpha)$ with $b \operatorname{dom}_{\alpha} p$ . Otherwise, if (m2) holds, there is $a \in A$ for which $a \in \mu^{*}(\alpha) - M(\alpha)$ for which by induction there exists $q \in M(\alpha) - \mu^{*}(\alpha)$ such that $q \operatorname{dom}_{\alpha} a$ , and therefore $q \operatorname{dom}_{\alpha} p$ .

Theorem 6 Where $T = (\Sigma, \leq, R, f)$ is a quantified ordered theory, $\alpha \in \Sigma$ , $p$ is a literal, $s$ is + or -, and $C$ is the set of constants occurring in $R$ and $p$ , let $R^p = \{A\sigma \Rightarrow q\sigma : A \Rightarrow q \in R \text{ and } \sigma \text{ is a substitution in } C\}$ , for each $\alpha \in \Sigma$ let $f^p(\alpha) = \{A\sigma \Rightarrow q\sigma : A \Rightarrow q \in f(\alpha) \text{ and } \sigma \text{ is a substitution in } C\}$ , and let $T^p = (\Sigma, \leq, R^p, f^p)$ . Then $t$ is a ground proof tree for $p^s$ at $\alpha$ in $T$ iff $t$ is a ground proof tree for $p^s$ at $\alpha$ in $T^p$ .

Proof The result follows immediately from examining the tree.

Lemma 7 If $T$ is an ordered theory and $C$ is a curtain for $T$ , then not both $T \left| \frac{C}{\alpha} p^{+} \right.$ and $T \left| \frac{C}{\alpha} p^{-} \right.$ .

Proof The proof is analogous to the proof of Lemma 1.

Lemma 8 If $T$ is an ordered theory and $C$ is a curtain for $T$ , then not both $T \left| \frac{C}{\alpha} p^{+} \right.$ and $T \left| \frac{C}{\alpha} \neg p^{+} \right.$ .

Proof The proof is analogous to the proof of Lemma 2.

Theorem 7 If $T = (\Sigma, \leq, R, f)$ is an ordered theory, $A = \{\beta \in \Sigma: \text{there is no } \gamma \in \Sigma \text{ such that } \beta < \gamma\}$ , $\sqsubseteq = \{\langle \beta, \alpha \rangle: \beta \leq \alpha \text{ and } \alpha \in A\}$ , $C = (A, \sqsubseteq)$ , $\alpha \in A$ , $p$ is a literal, and $s$ is + or -, then $T \models_{\alpha} p^s$ iff $T \models_{\alpha}^{C} p^s$ .

Proof First, suppose t is a proof tree of $p^{s}$ at $\alpha$ for T. Construct $t^{*}$ from t by changing the label of each node in t from $q^{u}$ to $q_{\alpha}^{u}$ . Since for all $\alpha \in A$ and $\beta \in \Sigma$ , $\beta \sqsubseteq \alpha$ iff $\beta \leq \alpha$ , $t^{*}$ is a proof tree for C in T with root node labeled $p_{\alpha}^{s}$ .

Next, suppose t is a proof tree for C in T and the root node of t is labeled $p_{\alpha}^{s}$ . Construct $t^{*}$ from t by changing the label of each node in t from $q_{\alpha}^{u}$ to $q^{u}$ . Since for all $\alpha \in A$ and $\beta \in \Sigma$ , $\beta \sqsubseteq \alpha$ iff $\beta \leq \alpha$ , $t^{*}$ is a proof tree of $p^{s}$ at $\alpha$ for T.

Theorem 8 Suppose $\alpha$ is an opaque agent in curtain $C = (A, \sqsubseteq)$ for ordered theory $T = (\Sigma, \leq, R, f)$ . Let $\Sigma^{*} = \{\gamma : \gamma \in \Sigma \text{ and } \gamma < \alpha\}$ , let $\leq^{*} = \leq \cap (\Sigma^{*} \times \Sigma^{*})$ , let $R^{*} = \{r : r \in f(\gamma) \text{ for some } \gamma \in (\Sigma^{*} - \{\alpha\})\} \cup \alpha^{C}$ , let $f^{*}(\gamma) = f(\gamma)$ for all $\gamma \in \Sigma^{*} - \{\alpha\}$ and let $f^{*}(\alpha) = \alpha^{C}$ , let $T^{*} = (\Sigma^{*}, \leq^{*}, R^{*}, f^{*})$ , let $A^{*} = A \cap \Sigma^{*}$ , let $\sqsubseteq^{*} = \sqsubseteq \cap \leq^{*}$ , and let $C^{*} = (A^{*}, \sqsubseteq^{*})$ .

(1) $\alpha$ is decisive for $T^{*}$ and $C^{*}$ .

(2) for all $\beta \in A^{*}$ , if $T \models_{\beta}^{C} p^{s}$ then $T^{*} \models_{\beta}^{C^{*}} p^{s}$ .

(3) If $\alpha$ is decisive for $T$ and $C$ , then for all $\beta \in A^{*}$ , $T \mid_{\beta}^{C} p^{s}$ iff $T^{*} \mid_{\beta}^{C^{*}} p^{s}$ .

Proof (1) We must consider two cases.

Case 1: $T \left| \frac{C}{\alpha} p^{+} \right.$ . Then $\Rightarrow p \in f^{*}(\alpha)$ , $\Rightarrow \neg p \notin f^{*}(\alpha)$ by Lemma 8 and the definition of $f^{*}$ , there is no $A \Rightarrow \neg p \in f^{*}(\alpha)$ , and a single node labeled $p_{\alpha}^{+}$ constitutes a proof tree for $C^{*}$ in $T^{*}$ .

Case 2: not $T|_{\alpha}^{C}p^{+}$ . Then there is no $A \Rightarrow p \in f^{*}(\alpha)$ and a single node labeled $p_{\alpha}^{-}$ constitutes a proof tree for $C^{*}$ in $T^{*}$ .

(2) Assume $\beta \in A^{*}$ and $T\big|_{\beta}^{C}p^{s}$ . Let $t$ be a proof tree in $C$ for $T$ whose root node is labeled $p_{\beta}^{s}$ . Construct $t^{*}$ from $t$ by eliminating every node $n$ in $t$ such that for some literal $q$ and some ancestor $m$ of $n$ , $m$ is labeled $q_{\alpha}^{+}$ or $m$ is labeled $q_{\alpha}^{-}$ . Then by the proof of (1) and by examination of all the nodes in $t^{*}$ , $t^{*}$ is a proof tree in $C^{*}$ for $T^{*}$ .

(3) All we have to do is assume that $\alpha$ is decisive for C and T and show the converse of (2). Let $t$ be a proof tree for $C^*$ in $T^*$ . Let $n$ be any node in $t$ labeled $q_{\alpha}^{+}$ or $q_{\alpha}^{-}$ for some literal $q$ . Since $\alpha$ is decisive for $C$ and $T$ , and since $\Rightarrow q \in f^{*}(\alpha)$ iff $T \left| \frac{C}{\alpha} q^{+}, \right.$ there exists a proof tree $t_q$ for $C$ in $T$ whose root node has the same label as $n$ . Construct $t^*$ from $t$ by replacing every subtree in $t$ whose root node is labeled $q_{\alpha}^{+}$ or $q_{\alpha}^{-}$ by the corresponding tree $t_q$ . Then $t^*$ is a proof tree for $C$ in $T$ .

## References

Billington, David, 1989, Some Results on Defeasible Logic, Research Report AI-1989-09. Artificial Intelligence Programs, The University of Georgia, Athens, Georgia.

Bossu, G. and Siegel, P., 1985, Saturation, nonmonotonic reasoning and the closed-world assumption, Artificial Intelligence 25: 13–65.

Geerts, P. and Vermeir, D., 1991, Credulous and Autoepistemic Reasoning using Ordered Logic, Proceedings of the First International Workshop on Logic Programming and Non-Monotonic Reasoning, Washington D.C., 21–36.

Geffner, H., 1988, On the logic of defaults, AAAI-88: 449–454.

Geffner, H., 1989, Default Reasoning: Causal and Conditional Theories, PhD dissertation, Computer Science Department, UCLA. To be published by MIT Press.

Geffner, H. and Pearl, J., 1989, A framework for reasoning with defaults, In Kyburg, H., Loui, R. and Carlson, G. (eds.), Knowledge Representation and Defeasible Reasoning. Studies in Cognitive Systems, Kluwer Academic Publishers, Boston: 69–88.

Hanks, S. and McDermott, D., 1987, Nonmonotonic logic and temporal projection, Artificial Intelligence 33: 379–412.

Hexmoor, H. Nute, D., and Underwood, W., 1990, PACE (Planning, Acting, and Control Environment): a testbed for multi-agent planning and acting, Test Technology Symposium III, Johns Hopkins University, Baltimore, Maryland, April 21, 1990.

Horty, J., Thomason, R. and Touretzky, D., 1987, A skeptical theory of inheritance in nonmonotonic semantics networks, AAAI-87: 358–363.

Konolige, K., 1988, On the relation between default theories and autoepistemic logic, Artificial Intelligence 35: 343–382.

Laenens, E. and Vermeir, D., 1989, A fixpoint semantics for ordered logic, Journal of Logic and Computation 1: 159–186.

Lifschitz, V., 1985, Computing circumscription, IJCAI-8: 121–127.

Lifschitz, V., 1986, Pointwise circumscription: preliminary report, AAAI-86: 406–410.

Loui, R., 1987a, Theory and Computation of Uncertain Inference and Decision, PhD dissertation, Technical Report

228, Department of Computer Science, The University of Rochester.

Loui, R., 1987b, Response to Hanks and McDermott: temporal evolution of beliefs and beliefs about temporal evolution, Cognitive Science 11: 303–317.

Loui, R., 1987c, Defeat among arguments: a system of defeasible inference, Computational Intelligence 3: 100–106.

McCarthy, J., 1980, Circumscription – a form of non-monotonic reasoning, Artificial Intelligence 13: 27–39.

McCarthy, J., 1986, Applications of circumscription to formalizing common sense knowledge, Artificial Intelligence 28:89–116.

McDermott, D. and Doyle, J., 1980, Non-monotonic logic I, Artificial Intelligence 13: 41–72.

Moore, R., 1984, Possible-worlds semantics for autoepistemic logic, Proceedings of the 1984 Non-monotonic Reasoning Workshop. AAAI, Menlo Park, California.

Moore, R., 1985, Semantical considerations on non-monotonic logic, Artificial Intelligence 25: 75–94.

Nute, D., 1988, Defeasible reasoning: a philosophical analysis in Prolog, In J. Fetzer (ed.), Aspects of Artificial Intelligence, Kluwer Academic Publishers, Boston: 251–288.

Nute, D., 1990, Defeasible logic and the frame problem, In H. Kyburg, R. Loui, and G. Carlson (eds.), Knowledge Representation and Defeasible Reasoning, Studies in Cognitive Systems, Kluwer Academic Publishers, Boston: 3–21.

Nute, D., 1991, Basic defeasible logic, In L. Fariñas-del-Cerro and M. Penttonen (eds.), Intensional Logics for Programming, Oxford University Press.

Nute, D., Billington, D. and De Coster, K. 1989, Defeasible logic and inheritance hierarchies with exceptions, Proceedings of the Tübingen Workshop on Semantic Nets, Inheritance and Nonmonotonic Reasoning, December, 1988, SNS Bericht 89–48, University of Tübingen: 69–92.

Nute, D. and Lewis, M., 1986, A users manual for d-Prolog, ACMC Research Report 01-0016, The University of Georgia, Athens, Georgia.

Pollock, J., 1987, Defeasible Reasoning, Cognitive Science 11:481–518.

Reiter, R., 1980, A logic for default reasoning, Artificial Intelligence 13: 81–132.

Shoham, Y., 1987, A semantical approach to nonmonotonic logics, IJCAI-87: 388–393.

Touretzky, D., 1986, The Mathematics of Inheritance Systems, Research Notes in Artificial Intelligence, Pittman, London.

Vermeir, D., Laenens, E., Verdonk, B. and Cuyt, A., 1989, A Logic for Objects and Inheritance, Universitaire Instelling Antwerpen, Wilrijk, Belgium.

Vermeir, D., Nute, D. and Geerts, P., 1989, A defeasible logic for multi-expert systems, Proceedings of the International Symposium on Computational Intelligence, Milan, Italy, to appear.

Vermeir, D., Nute, D., and Geerts, P., 1990, Modeling defeasible reasoning with multiple agents, Proceedings of the 23rd Hawaii International Conference on System Science, Vol. III. IEEE Computer Society Press, Washington: 534–543.
