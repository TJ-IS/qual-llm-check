---
otero_id: 17027
otero_key: "R7348372"
title: "A quantitative approach to logical inference"
authors: "J.N. Hooker"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90097-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Quantitative Approach to Logical Inference $^{1}$

J.N. HOOKER

Graduate School of Industrial Administration, Carnegie-Mellon University, Pittsburgh, PA 15213, USA

Logical inference is of central importance in the information and decision sciences but presents a very hard computational problem. Since the traditional symbolic inference methods have had limited success on large knowledge bases, this papers investigates a quantitative approach. It surveys the application of integer programming methods to inference problems in propositional logic. It displays a number of remarkable parallels between logic and mathematics and shows that these can lead to fast inference methods, both quantitative and symbolic. In particular it explains why the logical concepts of resolution, extended resolution, input and unit refutation, the Davis–Putnam procedure, and drawing of inferences pertinent to a given topic are closely related to the mathematical concepts of cutting planes, Chvátal's method, elementary closure, branch and bound, and projection of a polytope, respectively. Much of the paper should be intelligible to persons with limited background in logic and mathematical programming, but recent mathematical results are stated precisely.

Keywords: Logical Inference, Integer Programming.

![](/api/attachments/R7348372/fulltext/images/ff495369a5daf13c92a616a31650de914b11443e7dfcfea54cba8269a7145b94.jpg)

John N. Hooker is assistant professor of industrial administration at the Graduate School of Industrial Administration, Carnegie-Mellon University. He received an A.B. in mathematics from Princeton University in 1971, a Ph.D. in philosophy from Vanderbilt University in 1974, and a Ph.D. in management science from the University of Tennessee in 1984. His research interests lie in the application of mathematical programming to logical problems, as well as in location on networks, transportation problems and other areas of operations research.

## 1. Introduction

The problem of inference is fundamental in the information and decision sciences. It asks, how can one tell whether a given proposition is implied by a massive collection of data? Or more generally, how can one draw from these data all inferences that pertain to a particular question?

It is well known that inference is an important issue in data bases, expert systems, and such logical programming languages as PROLOG. But the role of inference is more central than these applications may suggest, and its difficulty is greater than often recognized. Furthermore, the generally accepted type of inference procedure, symbolic calculation, has failed to solve large inference problems even in propositional logic, the simplest sort of logic.

Symbolic, as opposed to numeric, calculation is the mechanical manipulation of symbols. It was envisioned by Leibniz and implemented by Boole, both of whom believed that the reasoning process could be as automatic as long division if it were couched in a sufficiently precise language (Leibniz's characteristica universalis). Today the artificial intelligence community relies heavily on symbolic calculation, even using it to do some chores once reserved to numeric calculation.

The thesis of this paper is that in the case of inference, the reverse emphasis is worth investigating, at least for propositional logic. Although logical inference seems quintessentially suited to symbolic calculation, we propose to apply quantitative methods, in particular the methods of mathematical programming. We do so for two main reasons. One is that, at least in propositional logic, mathematical programming methods are potentially very fast. The other is that a quantitative interpretation of propositional logic reveals a remarkable degree of mathematical structure. Some important concepts of propositional logic have close parallels in mathematical programming and polyhedral theory. An understanding of these parallels can lead to better methods, both quantitative and symbolic.

We make no exclusive claims for the effectiveness of a quantitative approach. Rather, we claim that the inference problem is important enough and hard enough to justify several angles of attack. The almost total reliance on symbolic methods is sometimes accompanied by the attitude that their sluggishness will be moot when the next generation of faster computers comes along. But we will see that the problem will not yield merely to fast computers; better methods are needed as well.

We also acknowledge that propositional logic alone has limited usefulness. Most applications call for some sort of epistemic logic (which indicates the degree of confidence in a proposition), or predicate logic (which has such quantifiers as 'for all' and 'for some'), or some other elaboration. But propositional logic is fundamental and provides a natural stepping stone to more advanced logics.

In section 2 below we make a case for the importance and difficulty of inference. We then recount in section 3 a brief history of automated inference methods, both symbolic and quantitative. Sections 4 and 5 show how to formulate inference problems in propositional logic as integer programs and indicate briefly how integer programs are solved. The remainder of the paper explores more deeply the parallels between logic and mathematics and describes some inference methods to which such explorations have led. Section 6 explains the connection between the well known Davis–Putnam algorithm in logic with the branch and bound method for solving integer programs. This connection led to a fruitful interaction of logic and mathematics, since the symbolic Davis–Putnam procedure suggested a superior quantitative inference method, which in turn suggested an even better symbolic algorithm. Section 7 establishes the connection between resolution methods for logic and cutting plane methods for integer programming. Here again we have fruitful interaction, since resolution provides a class of effective cutting planes for solving an integer programming model of logic, and an extension of that class leads to a generalized resolution method for a broader class of logical formulas. Also an important class of 'easy' inference problems, those soluble by 'input deduction' and consisting essentially of 'Horn clauses', has a very close connection with a natural class of 'easy' integer programming problems, namely Chvátal's 'rank 1' problems. Furthermore, 'extended' resolution is in a certain sense equivalent in 'power' to Chvátal's cutting plane method on satisfiability problems. Section 8 suggests some of the logical ramifications of the properties of the 'linear programming relaxation' of an integer program and its dual. Section 8 shows that the problem of deducing all implications that relate to a particular subject can be seen as equivalent to a projection problem in polyhedral theory. Finally, section 10 indicates some future directions.

## 2. The Importance and Difficulty of Inference

We must first make clear that by ‘inference’ here we mean deductive inference, which is inference that is based solely on the laws of logic and the senses of the words involved. For example, from the premise that George Bernard Shaw was a bachelor one can deduce that Shaw was unmarried. For we know by definition of ‘bachelor’ that all bachelors are unmarried, and from this we infer (using the logical rules of universal instantiation and modus ponens) that Shaw was unmarried. When the definitions are listed explicitly as premises, deductive inference relies solely on the laws of logic and in this case is called logical inference.

Deductive inference is often contrasted with inductive inference, which is the backbone of empirical science. Upon observing 100 ravens and noting that all are black, one might inductively infer that all ravens are black. In its broadest sense inductive inference encompasses pattern recognition and theory formation, the processes by which we synthesize unorganized data and make them intelligible. (See Quine [76,77], however, for a famous critique of the inductive/deductive distinction.)

Deductive inference is much more circumscribed but nonetheless essential, because it is the way we keep track of what is already implicit in the knowledge we have accumulated. This intellectual housekeeping is no trivial task, for at least two reasons. One is that synthesis and pattern recognition play an important role here as in inductive inference, as any mathematician can confirm. The ultimate premises from which Hadamard and Poussin proved the elegant and powerful Prime Number Theorem [80] could equally well be used to prove thousands of totally uninteresting propositions. In recent years automated theorem provers have had some limited success in discovering interesting theorems [8], but their discovery remains primarily a difficult job for creative mathematician.

The other reason for the difficulty of deductive inference is the main focus of this paper. It is that the human community has collected so much information that we are overwhelmed by the sheer computational burden of checking whether it implies a given proposition, interesting or otherwise. Many have remarked the explosion of medical and other scientific literature, the growing complexity of legal regulations and case law, and the proliferation of massive computer data bases. In the old days one could distinguish what was ‘known’ from what was ‘unknown’ simpliciter, because the ‘known’ was what one could look up in the library. Now the notion of a common pool of human knowledge is becoming problematic, because it has become increasingly difficult to know what we know.

The information explosion occurs at a deeper level as well. Certain large systems that we want very much to understand, such as the atmosphere or the economy or the human body or a large manufacturing plant, are so complex as to be in a sense their own best description. There are no simple overarching laws from which we can deduce predictions with only second-order error. To get even a first approximation we must work with a system description that may be nearly as complex as the system itself. Newtonian simplicity has given way to what is in effect a large descriptive data base. To make predictions with such a data base is essentially to deduce its implications with respect to a given question, and for this we need efficient and powerful inference methods.

Unfortunately fast computers alone cannot solve the computational problem of drawing inferences. Inference methods now in use, if applied to a data base of even moderate size, would run eons on the fastest computers. We will see below that the 'inference engines' of existing expert systems provide no counterexamples of this statement, since they deal with large data bases either by severely restricting the expressiveness of the data base or by sacrificing the ability to draw all but a small subset of the valid inferences, or both.

Neither do existing large relational data bases provide counterexamples, since their query-answering procedures search for data records that instantiate a given relation rather than drawing inferences from propositions in the data base [29,30]. Large bibliographic data base systems are even more primitive, since they settle for text search procedures that not only fail to draw inferences but also retrieve much that is irrelevant.

The underlying difficulty is that inference is inherently a very hard, combinatorial problem. Suppose, for example, that a data base is encoded in the propositional calculus, the simplest sort of logical language. No one knows how to solve the inference problem in better than 'exponential time'. That is, as far as anyone knows, the time required to check whether a proposition is implied increases exponentially with the size of the data base in the worst case (technically, the problem is 'NP-complete' [31]). A popular inference algorithm, the resolution algorithm of Robinson [78], was recently proved by Haken [42] to require exponential time in the worst case even when applied to the propositional calculus (see also [88]). Computational experience [46] indicates that resolution's computation time rapidly explodes in the typical case as well as in the worst case. Furthermore, Franco and Paull [27,28] showed that a variant of the Davis–Putnam procedure with 'splitting' [62], another well-known inference method for propositional logic, requires exponential time with probability approach one when large random problems are chosen from a 'reasonable' distribution; earlier results to the contrary are artifacts of inappropriate distributions [26].

When the computation time tends to grow exponentially with the size of the data base, faster computers are of little avail. If inference takes one second for a data base containing 50 facts and two seconds for one containing 100 facts, then it takes over 18 billion years for one containing just 3000 facts. Even if future computers run many orders of magnitude faster than present ones, they will be no less daunted by this task.

The situation is even worse when the data are expressed in first order predicate logic, often used in relational data base queries. In this case the problem is not only hard but insoluble in general. Although there are procedures, such as the resolution method, that verify that any given implication in fact follows from the premises, there is no procedure that can always verify in finite time that a given nonimplication does not follow. This is the import of Alonzo Church's celebrated 1936 proof [14] that there is no finite decision procedure for first-order logic. (Turing [86] independently proved a similar result shortly afterward.) To have a finite decision procedure one must restrict himself to a fragment of quantified logic, and even then inference is very hard. One such fragment consists of formulas in Shönfinkel–Bernays form, in which all existential quantifiers ('for some') precede all universal quantifiers ('for all'). Plaisted [72] proved that checking the satisfiability of Horn formulas in Schönfinkel–Bernays form, which comprise a very limited fragment, requires exponential time in the worst case. Lewis [61] proved that checking satisfiability of an arbitrary formula in Schönfinkel–Bernays form requires 'nondeterministic exponential' time and thus is even more difficult.

## 3. Previous Work in Logical Inference

## 3.1. The Origin of Quantitative Methods for Inference

The application of mathematical programming, or quantitative methods of any sort, to logical inference has a very short history. Boolean algebra is over a hundred years old, but Boole had no intention of drawing inferences via numerical calculation ([9] opening section). On the contrary, Boole's main contribution was to implement Leibniz's dream of symbolic calculation in a real, workable system. His use of 0 and 1 for truth values and of arithmetical symbols for logical operations was only a stylistic device ([58], Sect. VI).

The idea for the recent quantitative methods for logic can be found in Wittgenstein's notion of logical space, introduced in the 1920's [95]. Consider propositional logic, which consists of atomic propositions $(x_{1}, x_{2}, \text{etc.})$ joined by various logical conrectives (such as and, or, not and implies) to make formulas. The truth or falsehood of a formula, such as

$$
\left(x _ {1} \text {   or   } x _ {2}\right) \text {   and   not- } x _ {3},
$$

depends solely on the truth values of the atomic propositions in it. For example, if we assign truth values $(x_{1}, x_{2}, x_{3}) = (1, 0, 0)$ to the atomic propositions (where 1 means true and 0 means false), the formula is true. Wittgenstein realized that the meaning of a formula can, for the purposes of propositional logic, be identified with a list of the satisfying truth assignments (those that make the formula true), which in this case are $(1, 0, 0)$ , $(0, 1, 0)$ , and $(1, 1, 0)$ . But these three ordered triples can be viewed as coordinates in three-dimensional space, and in particular as the coordinates of three vertices of a three-dimensional unit cube. In general, if there are n atomic propositions, the meaning of a formula is identified with a subset of the vertices of an n-dimensional unit cube. Since the unit n-cube is an object of interest to two rich areas of mathematics, integer programming and polyhedral combinatorics, the door to a quantitative treatment of logic is opened.

But this spatial interpretation of logic has only recently been applied. To the writer's knowledge, none of the methods of logical calculation invented since Boole's day, except the new methods described here, have involved numerical calculation. The nonnumeric methods are basically of two types, whose history we survey only in enough detail to indicate their weaknesses. They are the complete and the incomplete methods. In the context of propositional logic, a complete inference method identifies every implication of a given set of propositions (and a complete refutation method detects inconsistency whenever it is present). An incomplete inference method identifies only some implications, or identifies all implications only when the propositions are restricted to a certain type, such as 'Horn clauses' (defined below).

## 3.2. Complete Symbolic Methods

One of the best known complete methods is Robinson's resolution algorithm [78], which is designed for first-order predicate logic. Resolution applied to propositional logic is called ground resolution (section 7.1) and is essentially a portion of the Quine–McClusky algorithm [74,75,66]. Refinements of resolution include set-of-support resolution [96,97], linear resolution [62,65], SL-resolution [63], model elimination [63], and connection graphs [59,25].

The difficulty with resolution-based methods is that their running time tends to explode exponentially with the number of variables (atomic propositions). The Quine–McClusky algorithm [68] and subsequently the resolution algorithm [42] were recently shown to have exponential complexity. These algorithms are not only exponential in the worst case but tend to become rapidly impractical as the problem increases in size [46]. The refinements can be efficient in some contexts, but to the writer's knowledge not in the general context of drawing inferences from a large non-Horn knowledge base. 'Extended' resolution [85], discussed in section 7.5, runs in polynomial time on a class of problems on which ordinary resolution is exponential [19] and is as 'powerful' as Chvátal's method for integer programming [15,18], but there is no indication that it is more practical than the other methods on large data bases.

Due to the inability of existing complete inference methods to deal with large knowledge bases, most of the recent work in this area has been directed toward automated theorem proving, which involves relatively small knowledge bases ([7],[83, pp. 663–708]). Applications involving large data bases, such as expert systems, typically use incomplete methods [44,90,5].

## 3.3. Incomplete Symbolic Methods

The most popular incomplete methods are forward and backward chaining and variations of thereof ([70, Ch. 6]), often in the context of semantic networks. Forward chaining operates on rules of the form, 'If $A_1$ and $A_2$ and ... and $A_n$ , then $B'$ , in which $A_1, \ldots, A_n$ are antecedents and $B$ the consequent. (If there are no antecedents, the rule asserts the consequent; if there is no consequent, the rule denies the conjunction of the antecedents.) It begins with a number of propositions know to be true and infers the consequent of a rule whenever all of the premises are given or have been inferred via some other rule.

Any rule is equivalent to a clause, which is a disjunction of literals (atomic propositions or their negations). For instance, 'if $x_1$ and $x_2$ , then $x_3$ ' is equivalent to the clause 'not- $x_1$ or not- $x_2$ or $x_3$ ' A rule is Horn if it contains no negated propositions, so that the example just presented is Horn, but 'if $x_1$ and not- $x_2$ , then $x_3$ ' is not. A clause is Horn if it can be written as a Horn rule and therefore if and only if it contains at most one unnegated literal.

That forward chaining is an incomplete inference method can be seen in a simple example.

Suppose that a medical knowledge base contains the rules, 'If the blood contains X, then it contains Y', and a blood test reveals, 'The blood contains X or it contains Y'. It obviously follows that the blood contains Y, but forward chaining cannot draw this simple inference. Backward chaining and other variations of chaining founder on examples equally simple.

It is true that chaining methods are more powerful when used in indirect proof, because they can always detect inconsistency in a set of Horn rules. For example, the medical rule 'if the blood contains X, then it contains Y', and the statement 'the blood contains X or Y', can be written as the rules,

$$
\text { if } x \text { then } y
$$

$$
\text { if   not- } x \text { then } y.\tag{1}
$$

This data base is not Horn, and indeed if we add to it the assumption not-y, or ‘the blood does not contain Y’, we cannot derive the resulting contradiction with forward chaining. But it happens that a change of notation makes (1) a Horn set, so that we might say that (1) is ‘essentially’ Horn. If we define $\bar{y}$ to be the complement not-y of y, (1) becomes,

## if $\bar{y}$ then not- $x$

## if $\bar{y}$ then $x$ ,

a Horn set. (Note that we replaced the first rule by its equivalent contrapositive 'if not-y then not-x' and similarly for the second.) Now if we add $\bar{y}$ (i.e., not-y) to the set, chaining immediately yields the contradiction between x and not-x, and we conclude not- $\bar{y}$ , i.e., that the blood contains Y.

Although we can make chaining a complete refutation method by restricting the data base to Horn clauses, the price is a restriction on expressibility. Consider a data base with the following rules,

If the blood contains X, then it contains Y or Z; if the blood contains Y, then it contains X; if the blood contains Z, then it contains X. In clausal form the rules can be written,

not-x or y or z,

x or not-y,

x or not-z.

This is not a Horn set and cannot made to be one by complementing variables. Thus even so simple a data base is not essentially Horn.

Furthermore, in practice Horn data bases are explicitly as well as essentially Horn. This is because one cannot tell by examining a rule whether its addition to the data base will destroy the essential Hornness of the data base; one must examine the entire data base as well. Thus Horn data bases are generally built by adding rules that contain no negated propositions. If 'the blood contains X' and 'the blood does not contain X' occur in a rule, they must be regarded as unnegated atomic propositions and not as contradictories. This severely restricts the expressibility of the data base, as it rules out even (1).

Horn clauses appear to have been adequate for many applications, including such well-known expert systems as MYCIN [82,10], CADUCEUS [69,73], and XCON (R1) [67,2], and the logical programming language PROLOG [89]. But the unavailability of practical inference algorithms for non-Horn data bases has selected strongly against them. Early implementations of PROLOG, for example, were non-Horn, but they were soon restricted to Horn clauses due in part to inference difficulties. There have been recent efforts to extend PROLOG to a complete system [84], but the resulting implementation is much slower and more complex than standard PROLOG; attempts are underway to obtain efficiently in an almost Horn PROLOG that is designed to accommodate a few non-Horn formulas [64].

## 3.4. Quantitative Methods

We conclude with a brief history of the application of mathematical methods to inference.

The connection between logic and integer programming has been well known for some years; it was noted by G. Dantzig in his classic 1963 book on linear programming [21], used by R.M. Karp [56] in 1972 to prove the NP-completeness of integer programming, and elaborated by H.P. Williams [93,94] among others. But C.E. Blair, R. Jeroslow and J.K. Lowe were apparently the first, in 1985, to solve nontrivial inference problems with mathematical programming methods [4]. We will describe their contributions, as well as those of Jeroslow and Wang [54,55] and the author [45,46,47], in the next several sections.

Jeroslow has also begun to explore the mathematical modeling of first-order predicate calculus, certain data base problems, and inferences that involve uncertainty. In [50] he 'lifts' the integer programming approach to testing ground clauses for consistency to a procedure for doing the same in a typed predicate calculus, showing how unification may be accomplished by a partial instantiation technique. In [51] he develops a theory of when and how problems with both a discrete and a spatial component may be 'embedded' in a mixed integer programming (MIP) model. He is particularly concerned to characterize 'sharp' embeddings, which have the property that the convex hull of the MIP feasible set corresponding to the conjunction of two logical formulas is identical to the intersection of the convex hulls corresponding to the individual formulas. This work is an application of his basic MIP representability theorem, which is proved elsewhere [50] and derives from the insight that MIP representability is tantamount to representability in a disjunctive program. In [52] he proves that forward chaining with confidence factors may be accomplished by solving a certain MIP. To date, however, none of this work has led to the demonstration of a fast inference method for predicate or epistemic logic.

We should also mention that several investigators have examined the connection between certain inference problems and networks, including Glover and Greenberg [35], Hansen, Jaumard and Minoux [43], and others; see Chapter III of [48] for a survey. Network inference methods are seldom numeric, but they are closely related to the numerical treatment of inference problems because of the important role of networks in mathematical programming. These methods typically apply to rules with at most one antecedent; the network structure disappears when there are multiple antecedents. This is hardly surprising, because a satisfiability problem with two literals per clause (“2-SAT”) is very easy (soluble in linear time), whereas a problem with three literals per clause (“3-SAT”) is notoriously hard and was in fact the first problem to be shown NP-complete [17]. We will see in section 8.1, however, that Horn rules with multiple antecedents (for which the satisfiability problem is soluble in linear time [23]) have the sort of network structure one finds in dynamic programming models.

4. An Integer Programming Model of Inference in Propositional Logic

## 4.1. Conjunctive Normal Form

To model an inference problem as an integer program, all formulas must first be converted to conjunctions of clauses (conjunctive normal form). Four logical rules suffice to do this:

$$
\text { not- } (A \text {   or   } B) \quad \text { is   equivalent   to } \quad \text { not- } A \text {   and   not- } B,\tag{2}
$$

$$
\text { not- } (A \text {   and   } B) \quad \text { is   equivalent   to } \quad \text { not- } A \text {   or   not- } B,\tag{3}
$$

$$
A \text {   or   } (B \text {   and   } C) \quad \text { is   equivalent   to } \quad (A \text {   or   } B) \text {   and   }
$$

$$
(A \text {   or   } C),\tag{4}
$$

$$
\text { if   } A, \text {   then   } B \quad \text { is   equivalent   to } \quad \text { not- } A \text {   or   } B.\tag{5}
$$

Suppose, for example, we want to know whether the following inference is valid:

if not- $x_{1}$ , then $x_{2}$ or $x_{3}$

not- $x_{1}$ or $[(x_{2}$ or not- $x_{4})$ and $x_{3}$ and (not- $x_{3}$ or $x_{4})]$

not-(not- $x_{1}$ and $x_{3}$ )

where the horizontal line signifies ‘therefore’. Applying rule (5) to premise 1, rule (4) to premise 2, and rule (3) to premise 3, we get

$$
x _ {1} \text {   or   } x _ {2} \text {   or   } x _ {3}\tag{6}
$$

$$
\text { not- } x _ {1} \text {   or   } x _ {2} \text {   or   not- } x _ {4}\tag{7}
$$

$$
\text { not- } x _ {1} \text {   or   } x _ {3}\tag{8}
$$

$$
\text { not- } x _ {1} \text {   or   not- } x _ {3} \text {   or   } x _ {4}\tag{9}
$$

$$
x _ {1} \text {   or   not- } x _ {3}\tag{10}
$$

$$
x _ {2}\tag{11}
$$

The length of the conjunctive normal form of a given formula, and the time required to obtain it, are in the worst case exponential functions of the number of variables in the formula. There are procedures that achieve linear time in the worst case by adding new variables [4,17], but there is usually no compelling reason to use them. Since a knowledge base is the conjunction of its formulas, one can put the entire knowledge base into conjunctive normal form simply by doing so for its individual formulas. The formulas are usually short, so that even exponential time or length is small. Also, formulas in many applications are rules, which are easily rewritten as disjunctions of the same length using schema (5).

## 4.2. Propositions as Inequalities

The next step is two write each clause as an inequality. For example, (7) can be written

$$
\left(1 - x _ {1}\right) + x _ {2} + \left(1 - x _ {4}\right) \geq 1.\tag{12}
$$

Here each $x_{j}$ is a mathematical variable rather than a proposition and is interpreted as having the numerical value 1 when the proposition $x_{j}$ in (7) is true and 0 when $x_{j}$ is false. Thus if we suppose that each $x_{j}$ is binary (i.e., can take only the values 0 and 1), (12) asserts that at least one of the three literals in (7) is true, as it should.

Notice that (12) can be written $-x_{1} + x_{2} - x_{4} \geq 1 - 2$ . This suggests the following general notation for clauses,

$$
c _ {1} x _ {1} + \dots + c _ {n} x _ {n} \geq 1 - n (c) \quad \text { or } \quad c x \geq 1 - n (c),
$$

where c is a row vector and x a column vector, and where $n(c)$ is the number of negative components in the vector c. Each $c_{j}$ is 1 to indicate that the literal $x_{j}$ appears, -1 to indicate that not- $x_{j}$ appears, or 0 to indicate that neither appears.

## 4.3. A Generalized Covering Model

The final step is to write (6)-(11) as the following integer program:

$$
\text { minimize } \quad x _ {2}\tag{13}
$$

$$
\text { subject   to } \quad x _ {1} + x _ {2} \quad + x _ {3} \quad \geq 1,
$$

$$
- x _ {1} + x _ {2} \quad - x _ {4} \geq 1 - 2,
$$

$$
- x _ {1} \quad + x _ {3} \quad \geq 1 - 1,
$$

$$
- x _ {1} \quad - x _ {3} + x _ {4} \geq 1 - 2,
$$

$$
x _ {1} \quad - x _ {3} \geq 1 - 1,
$$

$$
x _ {1}, x _ {2}, x _ {3}, x _ {4} \in \{0, 1 \}.
$$

An integer program having this particular form is a generalized covering model. An assignment of binary values to $(x_{1}, x_{2}, x_{3}, x_{4})$ that satisfies the five inequality constraints is a feasible solution of the integer program.

To say that (6)-(10) imply (11) is to say that every truth value assignment that satisfies the premises (6)-(10) also satisfies the conclusion (11). This is equivalent to saying that all feasible solutions of (13) satisfy the inequality $x_{2} \geq 1$ . On the other hand, if (6)-(10) do not imply (11), then some feasible solution of (13) fails to satisfy $x_{2} \geq 1$ and therefore reduces the objective function $x_{2}$ below 1. We conclude that (6)-(10) imply (11) if and only if the minimum value of the objective function in (13) is at least 1. As it happens, the minimum value is 1, so that there is implication.

In general a set of m clauses containing n variables can be written as a system $Ax \geq a$ of m linear inequalities, where A is an $m \times n$ matrix, each row of which corresponds to a clause. $Ax \geq a$ implies a clause $cx \geq 1 - n(c)$ if and only if every binary value of x that satisfies the former satisfies the latter. Thus $Ax \geq a$ implies $cx \geq 1 - n(c)$ if and only if the minimum value of cx in the following integer program is at least $1 - n(c)$ :

$$
\begin{array}{l l} \min & c x \\ \text {s.t.} & A x \geq a, \\ & x _ {j} \in \{0, 1 \}, \quad j = 1, \dots , n. \end{array}\tag{14}
$$

Although a recurrent problem in symbolic methods is directing the search for a refutation, here we provide a natural search direction by minimizing an objective function that represents the clause whose implication is in question.

Suppose we want to know whether $Ax \geq a$ logically implies an arbitrary formula F, possibly not a clause. We can do so by expressing not-F as a system $Bx \geq b$ of p clauses and checking whether the combined system $Ax \geq a$ , $Bx \geq b$ has a feasible binary solution. If it does not, $Ax \geq a$ implies F. In applications $Ax \geq a$ is likely to represent a knowledge base known to be consistent. In this case there is advantage in solving a problem that is a special case of (14):

$$
\begin{array}{l l} \min & x _ {0} \\ \text {s.t.} & x _ {0} e + B x \geq b, \\ & A x \geq a, \\ & x _ {j} \in \{0, 1 \}, \quad j = 0, \dots , n, \end{array}\tag{15}
$$

where $x=(x_{1},\ldots,x_{n})$ and e is a column of p ones. $Ax \geq a$ implies F if and only if the minimum value of $x_{0}$ is 1.

## 5. Solving the Integer Program

Since integer programs have the reputation of being very hard to solve, an initial reaction to the idea of formulating an inference problem as an integer program is that it makes a hard problem harder. But some integer programs are surprisingly easy to solve, and this appears to be true of generalized covering models of inference problems.

## 5.1. The Linear Programming Relaxation

A first step to solving the integer program (14) is to solve its linear programming (LP) relaxation, which is obtained by replacing $x_{j} \in \{0, 1\}$ with $0 \leqslant x_{j} \leqslant 1$ . The LP relaxation can be solved quite rapidly with sophisticated implementations of G. Dantzig's simplex method [21] or some variation of N. Karmarkar's new method [55,1]. If the resulting values of the $x_{j}$ 's happen to be integers, which in this case is quite likely, then the integer program is solved already.

Even if the solution of the LP relaxation is noninteger, the inference problem may yet be solved. Suppose, for example, that we solve the relaxation of (13). The solution is $(x_{1}, x_{2}, x_{3}, x_{4}) = (1/2, 0, 1/2, 0)$ with an objective function value of 0. This does not tell us whether an integer solution of (13) can result in an objective function of zero, so that the inference problem is unresolved. But suppose the minimum value of $x_{2}$ in the relaxation had been 1/2. This would make it clear that if the $x_{j}$ 's were required to be integers, the minimum value of the objective function could be no less than 1/2 and would moreover be integer, so that it would necessarily be at least 1. We would know that the premises implied the conclusion, even though we had not finished solving the integer program.

In general, if the LP relaxation of (14) has an integer solution $x^{*}$ , there is implication if and only if $cx^{*} \geq 1 - n(c)$ ; if the solution is noninteger and $cx^{*} > -n(c)$ , there is implication; but if the solution is noninteger and $cx^{*} \leq -n(c)$ , the issue is unresolved.

When solving the LP relaxation does not resolve the issue of implication, we begin to solve the integer program with some appropriate algorithm, carrying out just enough steps to answer the implication question. Most successful integer programming algorithms are based on 'branch and bound' or 'cutting plane' techniques, or some combination of the two [32].

## 5.2. Solution by Branch and Bound

The most straightforward way to solve an integer program is by branch and bound. Consider (13), for which the LP relaxation yielded the solution $(x_{1}, x_{2}, x_{3}, x_{4}) = (1/2, 0, 1/2, 0)$ . Since $x_{1}$ , for example, is fractional in this solution, we branch on $x_{1}$ . That is, we first try re-solving the LP with $x_{1} \leq 0$ as one of the constraints. When we do this we are lucky enough to get an integer solution (called an incumbent solution), $(x_{1}, x_{2}, x_{3}, x_{4}) = (0, 1, 0, 0)$ , with objective function value 1. Since we do not know this to be optimal, we also try setting $x_{1} \geq 1$ and solving the LP. This yields another incumbent solution $(x_{1}, x_{2}, x_{3}, x_{4}) = (1, 1, 1, 1)$ with objective function value again 1. Since we have exhausted the possibilities, we conclude that either solution is optimal for the integer program.

If setting $x_{1} \leq 0$ (or $x_{1} \geq 1$ ) had produced a noninteger solution, we would have branched on one of the fractional variables, perhaps $x_{2}$ , and re-solved the LP once with extra constraints $x_{1} \leq 0$ and $x_{2} \leq 0$ , and again with extra constraints $x_{1} \leq 0$ and $x_{2} \geq 1$ . Each such LP we solve corresponds to a node of a search tree (whose root corresponds to the original LP relaxation), and the two immediate successors of a node correspond to the two branchings $x_{j} \leq 0$ and $x_{j} \geq 1$ . When we obtain an incumbent solution at a node, there is no need to branch further at that node; i.e., we fathom the node. In this way we implicitly enumerate of all the successors of the node.

Another way to enumerate implicitly is to bound the objective function value. Each time we obtain an incumbent solution we get a new upper bound on the minimum value of the objective function. If at some node the LP yields an objective function value that exceeds the best upper bound obtained so far, then we can fathom that node, since its successors can only be worse. The search continues until we have branched at or fathomed every node in the current search tree, and the best incumbent solutions solve the original integer program. In section 6 we show how to apply branch and bound to the inference problem.

## 5.3. Solution by Cutting Planes

To understand the idea of a cutting plane it is helpful to define the convex hull of the feasible solutions of an integer program. Consider problem (13), whose constraints are satisfied by three integer lattice points (points whose coordinates are all integers), namely $(0, 1, 0, 0)$ , $(0, 1, 0, 1)$ , and $(1, 1, 1, 1)$ . If a half space is the portion of space satisfying some linear inequality, then the convex hull of the three points is the intersection of all half spaces containing them. The convex hull is a bounded polyhedron or polytope (in this case a triangular area with the three points as vertices), which we call the integer hull. Since all of its vertices are integer lattice points, we say that it is an integral polytope.

The set of feasible solutions of the LP relaxation of (13) also form a polytope, which we can call the relaxed polytope. At least one vertex of the relaxed polytope is an optimal solution of the relaxed problem, and the simplex method finds such a vertex. The difficulty is that the relaxed polytope is generally larger than the integer hull and therefore not integral. This is why the solution of the relaxed LP may be noninteger.

Suppose, however, that we augment the constraints of the LP relaxation with some 'separating cuts'. A cut is an inequality satisfied by all the feasible solutions of the integer program, and the hyperplane it defines is a cutting plane. A separating cut is one that the solution $x^{*}$ of the LP relaxation violates and therefore one that 'cuts off' a part of the relaxed polytope containing $x^{*}$ . Its cutting plane passes between $x^{*}$ and the integer hull and so 'separates' $x^{*}$ from the integer hull.

For example, the constraint $x_{2} + x_{3} \geq 1$ is a cut for (13) because all feasible solutions of (13) satisfy it, and it is a separating cut because the solution $x^{*} = (1/2, 0, 1/2, 0)$ of the relaxed problem violates it. If we add this constraint to the relaxed LP and re-solve, we necessarily get a different solution, namely $x = (3/4, 1/4, 3/4, 1/2)$ with objective function value 1/4. This solves the inference problem already, since the positive-valued objective function indicates implication. But if we want an integer solution we can keep adding cuts until the solution of the relaxed problem is integer.

Two general methods for deriving cuts are Gomory's method [36,37] and Chvátal's method [15], and we discuss the latter in section 6. But Gomory cuts and randomly-chosen Chvátal cuts tend to be 'weak', in the sense that they cut off relatively little of the relaxed polytope. The success of a cutting plane algorithm requires the invention of special algorithms, tailored to a particular problem, for generating 'strong' separating cuts. This approach has had remarkable success in solving such hard combinatorial problems as the traveling salesman problem [38]. We will show how to apply this approach to the generalized covering model in section 7.

6. Branch and Bound and the Davis-Putnam Procedure

One very promising symbolic method for testing satisfiability, still largely unknown to the artificial intelligence and information science communities, grew out of an investigation of a quantitative method. Blair, Jeroslow and Lowe [4] showed that a branch and bound approach not only solves satisfiability problems quickly but is closely related to a variant of the well-known Davis–Putnam procedure in logic. Later Jeroslow and Wang [53] replaced the LP in the branch and bound method with a variable-fixing heuristic that serves much the same purpose and obtained a symbolic method even faster than branch and bound.

## 6.1. The Davis-Putnam Procedure with Splitting

The Davis–Putnam procedure determines whether a proposition in conjunctive normal form is satisfiable. It can determine whether A implies B by checking the satisfiability of A and not-B.

The procedure is a combination of chaining and enumeration. It solves the problem with chaining and ‘monotone variable fixing’ (a simplification device) whenever possible, and enumerates only when necessary. The enumeration phase can be seen as the construction of a search tree much like that in the branch and bound procedure, but here each node of the tree is a proposition in conjunctive normal form. This ‘splitting’ technique is actually Loveland’s modification [63] of the original algorithm [22], which uses resolution.

As an illustration we apply the technique to (6)-(10) conjoined with the denial not- $x_{2}$ of the conclusion (11). Note that we have a unit clause (clause with a single literal), namely not- $x_{2}$ . This forces $x_{2}$ to be false, and we use this fact to eliminate $x_{2}$ from (6) and (7). This is essentially chaining, since when we change (6), for example, from 'x $_{1}$ or x $_{2}$ or x $_{3}$ ' to 'x $_{1}$ or x $_{3}$ ', we are changing the rule 'if not- $x_{1}$ and not- $x_{2}$ , then x $_{3}$ ' to 'if not- $x_{1}$ , then x $_{3}$ ' by virtue of the fact that we already know the second antecedent not- $x_{2}$ to be true. If not- $x_{2}$ had occurred in any clauses, we could have deleted them, because once we know $x_{2}$ is false they are redundant.

Since there are no more unit clauses, we split on a variable, say $x_{1}$ . We first force $x_{1}$ to be true by making $x_{1}$ an additional premise. Chaining yields the two unit clauses, $x_{3}$ and not- $x_{3}$ , a contradiction. Thus we try adding not- $x_{1}$ instead, whereupon we again get $x_{3}$ and not- $x_{3}$ . We conclude that the clauses are unsatisfiable, so that (6)-(10) imply $x_{2}$ .

We now state the procedure in general. It uses the following two subroutines, which apply to an input formula Q in conjunctive normal form.

Chaining subroutine. Pick any unit clause l of Q; if there is none, exit the subroutine. If l is the negation of another unit clause of Q, Q is inconsistent; exit the subroutine. Otherwise force l to be true by deleting from Q all clauses containing l and all occurrences of not-l from other clauses. Repeat the subroutine.

Monotone Variable Fixing subroutine. For each monotone variable $x_{j}$ in Q (i.e., each $x_{j}$ that occurs negated everywhere or unnegated everywhere in Q), delete from Q all clauses containing $x_{j}$ . Exit the subroutine.

At the beginning the search tree consists solely of the unfathomed node P, whose satisfiability we wish to check.

Step 1. Pick an unfathomed node Q with no successors. If there are no such nodes, stop; P is unsatisfiable. Apply Chaining and Monotone Variable Fixing to Q. If Q is empty, stop; P is satisfiable. If chaining found Q to be inconsistent, fathom Q and repeat Step 1.

Step 2 (splitting, or branching). Pick any variable $x_{j}$ in $Q$ and branch at $Q$ , creating successor nodes 'Q and $x_{j}$ ' and 'Q and not- $x_{j}$ '. Go to Step 1.

## 6.2. A Branch and Bound Solution

Branch and bound can be used to check whether P is satisfiable by modifying Step 2 of the Davis–Putnam procedure above. We represent Q in Step 2 as a system of inequalities in the usual way and solve the LP relaxation of an associated integer program before branching. We then branch on one of the variables that are fractional in the solution. So, Step 2 becomes,

Step 2'. Write Q as a system Ax ≥ a of m linear inequalities and solve the LP,

min $x_0$

$$
\text { s.t. } \quad e x _ {0} + A x \geq a,\tag{16}
$$

$$
0 \leq x _ {j} \leq 1, \quad i = 0, \dots , n,
$$

where e is a vector of m ones. If the solution $x^{*}$ is integer, or if the objective function value exceeds that of a previous incumbent solution, fathom node Q and go to Step 1. Otherwise branch on a fractional $x_{j}^{*}$ by creating successor nodes 'Q and $x_{j}'$ and 'Q and not- $x_{j}'$ , and go to Step 1.

Monotone Variable Fixing must also be slightly altered so that it does not fix $x_{0}$ to true.

The computational experience of Blair, Jeroslow and Lowe [4] shows that incumbent solutions tend to occur very early in the process, so that nodes can be fathomed when the traditional Davis–Putnam procedure would require further enumeration. In fact, these investigators were obliged to make a special effort to find search trees with more than two or three nodes. This was the case even though they did not use chaining and monotone variable fixing (Step 1) to simplify the subproblems in the branch and bound tree. They simply submitted the problem to various commercial mixed integer programming codes, whose branching procedures do not take advantage of the special structure of logic problems.

## 6.3. A Branching Method with a Variable-Fixing Heuristic

Jeroslow and Wang [53] found that the speed of the above branch-and-bound procedure can apparently be increased an on random satisfiability problems by replacing the LP step with a heuristic procedure that serves the same purpose of finding incumbent solutions.

The algorithm uses a heuristic to choose a variable on which to split. It pursues first the successor that a weight function indicates has a high probability of being satisfiable. The heuristic is contained in the following subroutine, which applies to node Q.

Variable-fixing subroutine. For an arbitrary set S of clauses define a weight function $w(S)=\sum_{k}N(k)2^{-k}$ , where k ranges over positive integers and $N(k)$ is the number of clauses in S containing k literals. If $S(j,v)$ is the set of clauses of Q in which $x_{j}$ occurs (for v=true) or in which not- $x_{j}$ occurs (for v=false), pick j and v so as to maximize $w(S(j,v))$ . Split on $x_{j}$ but generate only one successor of Q, namely Q and $x_{j}$ if v=true and Q and not- $x_{j}$ otherwise.

The Variable-Fixing Subroutine is executed repeatedly, beginning at an 'active' node, in an attempt to find an incumbent solution. If one is found, P is satisfiable. If Chaining detects an inconsistency after one or more variables are fixed, the algorithm backtracks immediately to the active nodes and tries its other branch. The precise backtracking scheme is rather complex and goes as follows. At the beginning both Q and the active node are the root node P.

Step 1 (try to find an incumbent solution). Applying Chaining and Monotone Variable Fixing to Q. If Q is empty, stop; P is satisfiable. If Chaining found Q to be inconsistent, go to Step 2. Otherwise perform Variable-Fixing and let Q be the successor it generates. Repeat Step 1.

Step 2 (backtrack to active node). Fathom Q. If Q is the root node, stop; P is unsatisfiable. Let Q be the active node, unless it is already, in which case both Q and the active node are changed to Q's parent. If Q has two fathomed successors, repeat Step 2.

Step 3 (branch). If Q has no successors, go to Step 1. If Q has two successors, let Q and the active node be the unfathomed successor, and repeat Step 3. Otherwise if Q's successor is fathomed, generate Q's other successor, let Q be it, and repeat Step 3. If it is not fathomed, generate Q's other successor, let both Q and the active node be it, and go to Step 1.

Although the variable-fixing method outperformed branch and bound by an order of magnitude, the comparison was somewhat unfair, because the LP approach used standard MIP codes rather than taking advantage of chaining and monotone variable fixing. Also the occasional ability of a noninteger LP solution to settle the satisfiability question was not used (see section 5.1). Jeroslow and Wang acknowledge this, but Jeroslow has expressed in conversation his doubt that simplex-based branch and bound could become competitive unless one uses a special-purpose simplex algorithm as well as the devices just mentioned.

## 7. Cutting Planes and Resolution

We first describe the resolution algorithm and a closely related but much faster cutting plane algorithm that is based on the fact that resolvents can be interpreted as a class of cutting planes generated by Chvátal's method. We then describe a close connection between 'easy' inference problems and 'easy' integer programs, namely that any proposition deducible by unit resolution or by an input proof is a 'rank 1' Chvátal cut obtainable directly from the original constraint set. We also show how a generalization of resolution cuts can lead to a generalized resolution procedure that is complete for clauses that assert at least a certain number, rather than at least one, of their literals are true. Finally, we state a result to the effect that 'extended' resolution can deduce a refutation in polynomial time whenever Chvátal's method can.

## 7.1. Resolution

Robinson [78] showed that a relatively simple procedure, resolution, is a complete refutation method for first order predicate calculus. In simplified form ('ground resolution') it applies to propositional logic, for which it (plus 'absorption') is a complete inference method.

Two clauses have a resolvent (of which they are the parents) when exactly one variable $x_{j}$ appears unnegated in one parent and negated in the other. Their resolvent is a clause consisting of all the literals in either parent except for $x_{j}$ and not- $x_{j}$ , which cancel. We obtain the resolvent of (6) and (7), for instance, by resolving on $x_{1}$ to get (17) below.

$$
x _ {1} \quad \text { or } x _ {2} \quad \text { or } x _ {3},\tag{6}
$$

$$
\text { not- } x _ {1} \quad \text { or } x _ {2} \quad \text { or   not- } x _ {4},\tag{7}
$$

$$
x _ {2} \quad \text { or } x _ {3} \quad \text { or   not- } x _ {4}.\tag{17}
$$

Note that the resolvent logically follows from the conjunction of its parents but from neither individually.

When one parent of a resolvent is a unit clause, we say that the resolution is unit resolution, which is identical to the chaining procedure in Step 2 of the Davis–Putnam algorithm of section 6.1. When both parents are unit clauses, the result is the empty clause, which is necessarily false and therefore indicates that the original clauses were inconsistent.

To state the resolution procedure we must characterize logical implication between clauses. We say that one clause absorbs another when all literals of the former occur in the latter. For instance, $x_{2}$ or $x_{3}$ absorbs not- $x_{1}$ or $x_{2}$ or $x_{3}$ . One clause logically implies another if and only if the one absorbs the other.

The resolution procedure is as follows. The problem is to determine whether a set S of clauses implies a clause C. (S is unsatisfiable if it implies the empty clause, which is absorbed only by itself.)

Step 1. If a clause in S absorbs C, stop; S implies C.

Step 2. Generate all resolvents that have parents in S and that are not absorbed by any clause in S (the latter test ensuring that the procedure terminates). If there are no such resolvents, stop; S does not imply C. Otherwise delete from S all clauses absorbed by any of the new resolvents (to simplify the problem), add the new resolvents to S, and go to Step 1.

In the example, (6)-(10) yield seven resolvents including (17), which together yield the resolvents $x_{2}$ or $x_{4}$ , $x_{2}$ or not- $x_{4}$ , and $x_{2}$ or not- $x_{3}$ . Of these the first two yield $x_{2}$ , which absorbs (and is in fact identical to) the conclusion. Thus (6)-(10) imply $x_{2}$ .

The completeness of this procedure was actually first proved by Quine. In fact, Quine and McCluskey [66] developed it as part of a method for simplifying formulas in propositional logic. Quine defined a prime implication of a set of clauses to be a clause implied by the set but absorbed by no other clause implied by the set. He then proved,

Theorem 1 (Quine [74,75]). The clauses remaining at the end of the resolution procedure are precisely the prime implications of the original clauses. The procedure is therefore a complete inference method.

Completeness follows because any implication of a set of clauses is absorbed by some prime implication of those clauses. Some of the prime implications may be redundant, and Quine stated the problem of discovering redundancies with one of the earliest formulations of a set covering model. (Quine actually defined ‘prime implicants’ because he worked with formulas in disjunctive normal form.)

In the example, the resolution algorithm yields the following implications of (6)-(10):

$$
\begin{array}{l} x _ {2}, \\ \text {not-} x _ {1} \text {or} x _ {3}, \\ x _ {1} \text {or not-} x _ {3}, \\ \text {not-} x _ {1} \text {or} x _ {4}, \\ \text {not-} x _ {3} \text {or} x _ {4}. \end{array}
$$

Since the conclusion $x_{2}$ is absorbed by (in fact identical to) one of these, it is implied by the premises.

## 7.2. Cutting Planes as Resolvents

It is a simple but remarkable fact that resolvents in logic correspond to a certain type of cutting plane in integer programming. (This is observed in [18], [45], [94], and probably elsewhere; also the cutting plane procedure of [6], when applied to clauses, is resolution.) When resolvents are used as cuts in a cutting plane method, rather than simply as additional premises in a symbolic resolution procedure, they can solve inference problems much more rapidly.

We remarked in section 5.3 that one method of obtaining cuts for an integer program is Chvátal's method. It is based on the fact that if one takes a positive linear combination of inequalities from a system $Ax \geq a$ and rounds up any nonintegers in the resulting inequality, the latter is satisfied by all integer solutions of $Ax \geq a$ and is therefore a cut, called a Chvátal cut. One can then obtain further Chvátal cuts by taking positive linear combinations of the original inequalities and previously generated cuts, and so on. Chvátal proved the deep result that any cut (including Gomory cuts) can eventually be generated this way [15].

Resolvents in an inference problem form a particular class of Chvátal cuts for the corresponding LP relaxation. For example, the resolvent (17) of (6) and (7) is a Chvátal cut for the LP relaxation of (13). To see this, note that we can get the resolvent by adding (18)-(21) below, dividing the result by 2, and rounding up the right-hand side to get (22):

$$
x _ {1} + x _ {2} + x _ {3} \geq 1,\tag{18}
$$

$$
- x _ {1} + x _ {2} \quad - x _ {4} \geq 1 - 2,\tag{19}
$$

$$
x _ {3} \geq 0,\tag{20}
$$

$$
- x _ {4} \geq - 1,\tag{21}
$$

$$
x _ {2} + x _ {3} - x _ {4} \geq 1 - 1.\tag{22}
$$

Note that (18) and (19) are the parents (6) and (7), and (20) and (21) are bounds of the form $x_{j} \geq 0$ and $x_{j} \leq 1$ . Since the resolvent (22) is the result of rounding a positive linear combination of constraints in the LP relaxation of (13), it is a Chvátal cut. In general, if $x_{k}$ is the only variable with opposite signs in the two clauses $x_{k} + cx \geq 1 - n(c)$ and $-x_{k} + dx \geq -n(d)$ , then their resolvent can be obtained by: (1) adding to them $x_{j} \geq 0$ for all j for which $c_{j} + d_{j} = 1$ , and $-x_{j} \geq -1$ for all j for which $c_{j} + d_{j} = -1$ , (2) dividing the sum by 2, and (3) rounding up the right-hand side of the resulting inequality.

Resolvents not only provide cuts but provide enough cuts to solve any inference problem. For if $Ax \geq a$ implies $cx \geq 1 - n(c)$ , then some prime implication of $Ax \geq a$ absorbs $cx \geq 1 - n(c)$ . So, we can solve the inference problem, if no other way, by adding as cuts all prime implications of $Ax \geq a$ . If the minimum value of cx in the relaxation is at least $1 - n(c)$ , implication is obviously indicated. But if the minimum value is less than $1 - n(c)$ , then no prime implication absorbs $cx \geq 1 - n(c)$ , which means by Theorem 1 that $cx \geq 1 - n(c)$ is not implied.

In practice we expect that the inference problem will be solved long before all prime implications are generated. For example, the LP relaxation of (13) has solution $x = (1/2, 0, 1/2, 0)$ , with objective function value $x_{2} = 0$ . We note in section 5.3 that $x_{2} + x_{3} \geq 1$ is a separating cut that when added to the constraint set yields the new relaxed solution $x = (3/4, 1/4, 3/4, 1/2)$ , which already indicates implication because $x_{2} = 1/4$ . But this cut is the resolvent of constraints 1 and 3. Thus we can solve the problem with a single resolution cut.

Usually the key to success of a cutting plane method is having a fast algorithm for finding separating cuts. In this instance we have one. Given a relaxed solution $x^{*}$ , let the truth value of a positive literal $x_{j}$ be $x_{j}^{*}$ and of a negative literal $-x_{j}$ be $1 - x_{j}^{*}$ . It is easy to show that a clause can be a parent of a separating resolution cut only if the truth values of its literals in the current relaxed solution sum to a number strictly less than 2, and even then only if one resolves on a variable $x_{j}$ with a fractional truth value. Computational experience [46] suggests that relatively few clauses pass the first test, so that one can rapidly screen for all separating resolvents. This ability to find separating resolvents easily adds a powerful direction-finding capability to a cutting plane method.

The computational tests [46] also showed that a simple cutting plane method that relied on resolution cuts alone was orders of magnitude faster than 'set-of-support' resolution [97] on most random problems. It is a characteristic of random problems that when the conclusion is implied, it generally follows from only one or two premises, and for this reason resolution was able to detect implication (when it occurred) almost as rapidly as the cutting plane method. But when implication did not occur, which is the situation in most random and probably most practical problems, resolution cuts solved problems (even with as few as 20 variables and 40 clauses) at least 1000 times faster than set-of-support resolution. In real problems, in which implications could be less trivial, the direction-finding capability of a cutting plane method could result in even greater superiority over resolution.

The LP relaxation solved 88% of the problems, but those requiring cuts usually needed only one or two additional solutions of a relaxed LP and were almost always solved very rapidly. But in about 20% of the random problems requiring cuts, there were no separating resolution cuts. In these cases stronger cuts, as well as the ability to revert to branch-and-bound, would have been useful.

## 7.3. Input Deduction and the Elementary Closure

We saw above that resolution corresponds to the generation of certain Chvátal cuts. But the resolution of two premises is a special case of a more general type of deduction, an input deduction, and one may ask whether input deductions correspond to a broader class of Chvátal cuts. They do, and moreover, they correspond precisely to the elementary closure of the LP relaxation, one of the fundamental concepts of cutting plane theory [47]. Since these cuts are generally stronger than resolution cuts, and it is relatively easy to find separating cuts of this form, they could also be very useful in a cutting plane algorithm. Thus in a single insight we uncover both a close parallel between logic and mathematics and a promising inference algorithm.

An input deduction is a resolution proof in which at least one parent of every resolvent is among the original premises. An input refutation is a refutation proof with the same property. There is a close connection between input refutations, unit resolutions, and Horn clauses. Let a set of clauses be minimally inconsistent when the removal of any one clause would make it consistent. Then,

Theorem 2 (Chang [13], Loveland [63]). A set of clauses has an input refutation if and only if it has a refutation by unit resolution (i.e., a unit refutation), and if and only if any minimally inconsistent subset of the clauses is essentially Horn.

A similar connection exists for deductions (not just refutations). Let a supporting variable for a clause C, as well as for a proof of C, be a variable that occurs in C. A unit support deduction of C is a deduction that resolves on nonsupporting variables only and that would be a unit refutation if all occurrences of supporting variables were erased. (It follows that the supporting variables are monotone in the premises. Also any resolution is a unit support deduction of the resolvent from the parents.) Finally, let a set S of premises be a minimal implicant of clause C if S implies C but fails to imply C when any one clause is removed from S. Then Theorem 2 has the following generalization.

Theorem 3 [47]. There is an input deduction from a set S of premises of a clause absorbing clause C if and only if there is a unit support deduction from S of a clause absorbing C, and if and only if any subset of S that is a minimal implicant of C is essentially Horn.

The upshot of Theorems 2 and 3 is that when one speaks of inference problems soluble by input deduction, or soluble by unit support deduction, or consisting of Horn clauses, he is speaking of essentially the same class of 'easy' problems.

The elementary closure of a set of inequalities is the set of all Chvátal cuts that are obtained by taking positive linear combinations of the original inequalities only. It is the 'first level' of Chvátal cuts, or the set of 'rank 1' cuts. The following two theorems establish that clauses that can be inferred via input deduction are precisely those belonging to the elementary closure.

Theorem 4 [47]. A clause belongs to the elementary closure of a set S of clauses (and bounds of the form $x_{j} \geq 0$ , $x_{j} \leq 1$ ) if it is the result of an input deduction from S.

Theorem 5 [47]. A clause C belongs to the elementary closure of a set S of clauses (and bounds of the form $x_{j} \geq 0$ , $x_{j} \leq 1$ ) only if a clause that absorbs C is the result of an input proof from a subset T of S in which the variables supporting C are monotone.

We can show in an example why Theorem 4 is true. Its approximate converse, Theorem 5, is more complicated, and the reader is referred to [47].

For clarity we will indicate a clause, such as $x_{1}-x_{3}+x_{6}\geq0$ , by listing only the coefficients and right-hand side, in this case $10-1001\geq0$ . We consider the following input deduction of $x_{5}+x_{6}\geq1$ , or $000011\geq1$ . The premises are on the left, and each resolvent on the right receives arrows from its parents. For the moment ignore the numbers in parentheses.

(1)

$$
1 0 1 1 1 0 \geq 1\tag{23}
$$

(1)

$$
\begin{array}{l}1 0 - 1 0 1 0 \geq 0 \rightarrow \quad 1 0 0 1 1 0 \geq 1\\(2 0 0 1 2 0 \geq 1)\end{array}\tag{2}
$$

$$
\begin{array}{c}\downarrow\\- 1 1 0 0 1 1 \geq 0 \rightarrow\begin{array}{l l l l l l}0&1&0&1&1&1 \geq 1\\(0&2&0&1&4&2 \geq 1)\end{array}\end{array}\tag{2}
$$

$$
\begin{array}{c}\downarrow\\0 - 1 0 1 0 1 \geq 0 \rightarrow\begin{array}{c c c c c c}0&0&0&1&1&1 \geq 1\\(0&0&0&3&4&4 \geq 1)\end{array}\end{array}\tag{3}
$$

$$
\begin{array}{c}\downarrow\\0   0   0   - 1   0   1 \geq 0 \rightarrow\begin{array}{c}0   0   0   0   1   1 \geq 1\\(0   0   0   0   4   7 \geq 1)\end{array}.\end{array}
$$

To show that 000011≥1 belongs to the elementary closure of the premises (and bounds $0 \leq x_{j} \leq 1$ ), we must recover it by taking a positive linear combination of these inequalities and rounding up the nonintegers. The above diagram shows how. Each inequality in parentheses below a resolvent is a weighted sum of the premises used to obtain the resolvent (as parents, parents of parents, etc.), where the weights are indicated on the left in parentheses. To obtain the weights, first assign weight 1 to the first two premises and compute the sum 200120≥1. Now give premise 3 weight 2 to cancel the first 2 in 200120≥1, since resolution takes place on $x_{1}$ ; compute the sum 020142≥1. Give premise 4 weight 2 to resolve on $x_{2}$ and compute 000344≥1; give premise 5 weight 3 to resolve on $x_{4}$ and compute 00047≥1. Now the weighted sum of the premises, using the weights indicated, is just 000047≥1, or $4x_{5} + 7x_{6} \geq 1$ . By adding to it 3 times the bound $x_{5} \geq 0$ , dividing the sum by 7, and rounding up the 1/7 on the right to 1, we obtain the desired $x_{5} + x_{6} \geq 1$ , which therefore belongs to the elementary closure.

We remark in passing that the weights in (23), when divided by 7, indicate the optimal solution of the 'dual' of the LP model of the inference problem.

Theorems 4 and 5 suggest an easy way to find clauses that are rank 1 cuts. We know that if clause C is a rank 1 cut, C (or a clause absorbing C) is the result of a unit support deduction in whose premises the supporting variables are monotone. By erasing the supporting variables we obtain a unit refutation. Thus C can always be found by looking for sets of clauses in which the variables supporting C are monotone and that have a unit refutation when these variables are dropped. For example, we can obtain the rank 1 cut $x_{5} + x_{6} \geq 1$ in (23) by noting that $x_{5}$ and $x_{6}$ are monotone and that their removal permits a unit refutation of the five clauses. Since unit resolution can be done in linear time, there is the potential here for the fast generation of cuts.

Moreover there is a simple algorithm for finding clauses that are separating rank 1 cuts [47]. It is based partly on the fact that if we find no separating rank 1 cuts by resolving on k-1 variables, then any cut we find by resolving on k variables must be such that these variables have fractional values in the LP solution. The algorithm starts by solving the LP relaxation of a set S of clauses and setting k=0.

Step 1. Set $k = k + 1$ . If $k > n$ , stop; no clauses are separating rank 1 cuts.

Step 2. Pick a set K (from those sets not already picked) of k variables with fractional truth values in the solution of the LP relaxation. If none remain, go to Step 1.

Step 3. Pick a clause D containing exactly one variable $x_{j}$ in K, such that the sum of the truth values of the other literals in D is strictly less than one. If there is no such clause, stop; there are no separating elementary cuts.

Step 4. Derive all possible resolvents on $x_{j}$ of D with other clauses in S. Delete from S clauses absorbed by the resolvents. If all resolvents contain one or more variables in K, or if no resolvent is separating, go to Step 3. Otherwise stop.

## 7.4. Generalized Resolution

In the previous section we generalized on the logic side: we generalized resolution (to input deduction) and found a correspondingly larger class of cuts (rank 1 cuts). In this section we will work from the cutting plane side: we will expand the class of resolution cuts and find a correspondingly generalized resolution procedure [45].

Ordinary clauses assert that at least one of their literals is true. The object here is to find a complete resolution procedure for clauses that assert that at least a certain number of their literals are true, where that number may be greater than one. When written as inequalities these clauses have the form $cx \geq \beta - n(c)$ and assert that at least $\beta$ of their literals are true (see [60,3] for some properties of such inequalities). We will call them $\beta$ -clauses, or clauses of degree $\beta$ , so that ordinary clauses are 1-clauses. The strategy for finding a complete inference procedure for $\beta$ -clauses is to find a class of Chvátal cuts that suffice to solve inference problems.

Implication between 1-clauses amounts to absorption. But between $\beta$ -clauses implication is more complicated, and we must characterize it before stating the generalized resolution procedure. We say that a $\beta_{1}$ -clause $C_{1}$ absorbs a $\beta_{2}$ -clause $C_{2}$ when $\beta_{1} \geq \beta_{2}$ and $C_{1}$ can be obtained by deleting zero or more literals from $C_{2}$ . Also a $\beta_{1}$ -clause $C_{1}$ is a reduction of a $\beta_{2}$ -clause $C_{2}$ if $C_{1}$ can be obtained by deleting exactly $\beta_{2} - \beta_{1} (\geq 0)$ literals from $C_{2}$ . (This is closely related to the 'logical reduction' discussed in [39].) Then a clause $C$ logically implies (dominates) a clause $D$ if and only if some reduction of $C$ absorbs $D$ [45,60].

Generalized resolution consists of the repeated application of two types of resolution, ‘cancellation’ resolution (similar to the ordinary kind) and ‘circulant’ resolution. (26) below is a cancellation resolvent of (24) and (25).

$$
x _ {1} + x _ {2} - x _ {3} + x _ {4} + x _ {5} \geq 4 - 1,\tag{24}
$$

$$
- x _ {1} + x _ {2} - x _ {3} \quad \geq 2 - 2,\tag{25}
$$

$$
x _ {2} - x _ {3} \geq 1 - 1.\tag{26}
$$

It is obtained by first reducing (24) to a clause of the same degree as (25):

$$
x _ {1} + x _ {2} - x _ {3} \geq 2 - 1,\tag{27}
$$

and then by resolving (25) and (27) as in ordinary resolution, except that $\beta$ need not be one. In general, we say that a $\beta$ -clause E is a direct cancellation resolvent of $\beta$ -clauses C and D if exactly one variable $x_{j}$ has opposite signs in C and D, and E consists of all the literals occurring in either C or D except $x_{j}$ and $-x_{j}$ . E is a cancellation resolvent of C and D if E is a direct cancellation resolvent of some reduction of C and some reduction of D. A cancellation resolvent can be seen to be a Chvátal cut much as an ordinary resolvent can.

Circulant resolution is applied to clauses that exhibit a circulant pattern, such as the following

$$
x _ {1} + x _ {2} \geq 1,\tag{28}
$$

$$
x _ {1} \quad + x _ {3} \geq 1,\tag{29}
$$

$$
x _ {2} + x _ {3} \geq 1,\tag{30}
$$

$$
x _ {1} + x _ {2} + x _ {3} \geq 2.\tag{31}
$$

(31) is a circulant resolvent of (28)-(30). It is also a Chvátal cut, since it is got by adding (28)-(30), dividing by 2, and rounding up the right-hand side. A more complex example of circulant resolution derives (35) from (32-34) below,

$$
x _ {1} + x _ {2} \quad - x _ {4} - x _ {5} \geq 3 - 2,\tag{32}
$$

$$
x _ {1} \quad + x _ {3} - x _ {4} \geq 2 - 1,\tag{33}
$$

$$
- x _ {1} + x _ {2} + x _ {3} - x _ {4} - x _ {5} \geq 4 - 3,
$$

$$
x _ {1} + x _ {2} + x _ {3} + x _ {4} + x _ {5} \geq 2.\tag{34}
$$

(35)

Here we can reduce (32)-(34) respectively to (28)-(30) and obtain (31) as above; it is therefore valid to infer (35), which (31) absorbs. We do not obtain (31) directly as a circulant resolvent because we require that the literals removed to effect the reductions $(-x_4, -x_5)$ have opposite sign than the corresponding literals in the resolvent $(x_4, x_5)$ . This restriction simplifies the search for resolvents without sacrificing completeness. We can recover (31) indirectly by doing a cancellation resolution of (35) and, say, (32) to get $x_1 + x_2 + x_3 + x_4 \geq 2$ , and another between the latter and (28) to get (31).

To describe circulant resolution rigorously, for an index set $J \in \{1, \ldots, n\}$ define $c_{J}$ by $(c_{J})_{j} = c_{j}$ for $j \in J$ and $(c_{J})_{j} = 0$ for $j \notin J$ . Then a clause $cx \geq (\gamma + 1) - n(c)$ is a circulant resolvent on $J$ of a set $S$ of clauses $a^{i}x \geq \beta_{i} - n(a^{i})$ , $i \in I$ , if each $a^{i}x \geq \beta_{i} - n(a^{i})$ has a reduction $b^{i}x \geq \gamma - n(b^{i})$ that absorbs $c_{J}x \geq \gamma - n(c_{J})$ , such that for all $j$ , (a) $b_{j}^{i} = 0$ for some $i \in I$ , and (b) $a_{j}^{i} = b_{j}^{i}$ or $a_{j}^{i} - b_{j}^{i} = -c_{j}$ for all $i \in I$ .

The following generalized resolution procedure determines whether a set S of $\beta$ -clauses (of various degrees) implies a $\beta$ -clause C.

Step 1. If some clause in $S$ dominates $C$ , stop; the original clauses imply $C$ .

Step 2. If possible, find a pair of clauses of S having one or more cancellation resolvents that are not already dominated by clauses in S. Delete from S all clauses dominated by these resolvents, and add the resolvents to S.

Step 3. If possible, find a set of clauses in S that has a circulant resolvent that is not dominated by a clause in S. Delete from S all clauses dominated by this resolvent, and add the resolvent to S.

Step 4. If no resolvents were added to S in Step 2 or 3, stop; the original clauses do not imply C. Otherwise go to Step 1.

We can define a generalized prime implication of S to be a $\beta$ -clause implied by S but dominated by no other clause implied by S. Then we have a generalization of Quine's result (Theorem 1):

Theorem 6 [45]. The generalized resolution procedure generates all generalized prime implications of a set of clauses and is therefore a complete inference method. The same procedure with circulant resolution omitted is a complete refutation method.

Generalized resolution therefore provides a way to generate enough Chvátal cuts to solve any inference problem involving $\beta$ -clauses. It can also be used in 1-clause problems to generate cuts stronger than ordinary resolution cuts and the elementary cuts of the last section. Although generalized resolution cuts may be less useful, due to the complexity of their generation, they have fairly strong separation conditions. In particular, a $\beta$ -clause can be the parent of a separating cancellation resolvent only if the truth values of its literals sum to a value strictly less than $\beta + 1$ , and resolution takes place on a variable with fractional truth value. Also a clause C can be a parent of a separating circulant resolvent on J of degree $\gamma + 1$ only if the sum of the truth values of C's literals indexed by J is strictly less than $\gamma + 1$ .

## 7.5. Extended Resolution and Chvátal's Method

Tseitin [85] has pointed out that a set of clauses representing the pidgeon hole problem can be solved in polynomial time with 'extended' resolution but not, apparently, with ordinary resolution; Haken [42] confirmed the latter, since he used the pidgeon hole problem to prove that ordinary resolution has exponential complexity in the worst case. In this section we will see that extended resolution is in a sense equal in power to Chvátal's method for solving satisfiability problems.

The pidgeon hole problem is to place $n + 1$ pidgeons in n holes so that no hole contains more than one pidgeon. Since the problem is insoluble, a set of clauses stating otherwise should be unsatisfiable. Such a set for n = 2 is,

$$
\begin{array}{r l r l} x _ {1 1} & + x _ {1 2} & \geq 1, \\ x _ {2 1} & + x _ {2 2} & \geq 1, \\ x _ {3 1} & + x _ {3 2} & \geq 1, \\ - x _ {1 1} - x _ {2 1} & & \geq - 1, \\ - x _ {1 1} & - x _ {3 1} & \geq - 1, \\ - x _ {2 1} - x _ {3 1} & & \geq - 1, \\ - x _ {1 2} - x _ {2 2} & & \geq - 1, \\ - x _ {1 2} & - x _ {3 2} & \geq - 1, \\ - x _ {2 2} - x _ {3 2} & \geq - 1. \end{array}\tag{36}
$$

Here $x_{ij}=1$ is interpreted to mean that pidgeon i is placed in hole j. Thus the first three clauses of (36) assert that each pidgeon is placed in a hole. The remaining clauses assert, for each pair of pidgeons, that both do not occupy the same hole. Resolution requires exponential time to detect the inconsistency of these clauses.

Whereas resolution permits the addition to a system $Ax \geq a$ of clauses of any resolvent of two of those clauses, extended resolution permits something more: the addition of the clauses $x_{i}$ or $x_{j}$ , $x_{i}$ or $x_{k}$ , and not- $x_{i}$ or not- $x_{j}$ or not- $x_{k}$ , where $x_{j}$ and $x_{k}$ are variables that occur in $Ax \geq a$ , but $x_{i}$ occurs nowhere in $Ax \geq a$ . This has the effect of introducing a new variable $x_{i}$ that is equivalent to $x_{j}$ or $x_{k}$ . By cleverly introducing new variables, the number of resolutions needed to refute (36) is at most a polynomial function of the number of literals in (36). Meanwhile, it can be shown that a refutation can be obtained with $n^{3}$ Chvátal cuts, also a polynomial function of the number of literals in (36). This suggests the following theorem.

Theorem 7 (Cook, Coullard, Turán [18]). If Chvátal's method can solve an inference problem in polynomial time, extended resolution can do the same.

This theoretically very interesting result was proved as part of an investigation of the P = NP question [31] and was not intended to point to a fast practical inference method. Indeed, to date no such application has been found for it.

8. Properties of the Linear Programming Relaxation

We noted earlier that solving the LP relaxation of the integer programming model of an inference problem often solves the inference problem. This is a very desirable state of affairs, since linear programs can be solved in polynomial time in the worst case $[57,55]$ and quickly in the typical case. So, it is important to know what sorts of inference problems can be identified a priori as soluble by the LP relaxation; a data base made of these would present an easy inference problem. Here we describe two sorts: Horn problems and problems with totally unimodular constraint matrices.

## 8.1. Horn Clauses and the LP Relaxation

Since knowledge bases are typically restricted to Horn clauses precisely to make inference easy, it is interesting to observe that Horn inference problems are among those solved by the LP relaxation. We will also see that the LP relaxation is related to dynamic programming, and that by solving its 'dual' one can obtain additional information about a Horn problem.

One can determine the satisfiability of a set of Horn clauses simply by checking whether the corresponding LP relaxation is feasible.

Theorem 8 (Blair, Jeroslow and Lowe [4]). A system $Ax \geq a$ of Horn clauses is satisfiable if and only if chaining detects no inconsistency, and if and only if the linear system $Ax \geq a$ , $0 \leq x \leq e$ is feasible (has a feasible solution).

(As usual, we can check whether A implies B by checking the satisfiability of A and not-B.)

It is easy to see why the theorem is true. It is obvious that if the clauses are satisfiable, then the linear system has a feasible solution. Also one can see by the following example that if chaining detects no inconsistency, then the clauses must be consistent. Consider the set of clauses (also written as rules),

$$
\begin{array}{l l} x _ {1} \text {   or   not- } x _ {2} \text {   or   not- } x _ {3} & \text { if   } x _ {2} \text {   and   } x _ {3}, \text {   then   } x _ {1}, \\ x _ {1} \text {   or   not- } x _ {3} \text {   or   not- } x _ {4} & \text { if   } x _ {3} \text {   and   } x _ {4}, \text {   then   } x _ {1} \\ x _ {3} \text {   or   not- } x _ {4} & \text { if   } x _ {4}, \text {   then   } x _ {3}, \\ x _ {4} & x _ {4} \end{array}\tag{37}
$$

Chaining detects no inconsistency and leaves the single clause $x_1$ or not- $x_2$ . This remaining clause must contain at least one negated variable (namely, not- $x_2$ ), since it contains at least two literals (else chaining is unfinished) and is Horn. Thus the original system can be satisfied by setting all eliminated variables $(x_{3}, x_{4})$ to the values fixed by chaining (both true), and all remaining variables $(x_{1}, x_{2})$ to false.

It remains to show that if the linear system is feasible, then chaining detects no inconsistency. The linear system for (37) is,

$$
\begin{array}{r l} & x _ {1} - x _ {2} - x _ {3} \geqslant - 1, \\ & x _ {1} - x _ {3} - x _ {4} \geq - 1, \\ & \quad x _ {3} - x _ {4} \geq 0, \\ & \quad x _ {4} \geq 1, \\ & 0 \leq x _ {j} \leq 1, \text {   all   } j. \end{array}\tag{38}
$$

It is clear that when chaining fixes a variable (e.g., $x_{4}$ to true), the corresponding linear constraint ( $x_{4} \geq 1$ ) fixes that variable to 0 or 1. Thus if chaining had found inconsistency, the LP would not have been feasible.

Another way the LP relaxation can solve an inference problem is for it to have an integral solution. Curiously, the LP relaxation for a Horn problem need not describe an integral polytope. For instance, if we remove $x_{4} \geq 1$ from (38), the resulting Horn system describes a polytope with the fractional vertex $(x_{1}, x_{2}, x_{3}, x_{4}) = (0, 1/2, 1/2, 1/2)$ .

But Jeroslow and Wang [54] have shown that the 'dual' of the LP relaxation of a Horn problem (in which the implication of an atomic proposition is in question) necessarily describes an integral polytope. Furthermore, the dual solution indicates not only whether the truth of an atomic proposition is implied but reveals part of the structure of a resolution proof of the proposition. To make this result precise we must first reformulate the LP relaxation of a Horn problem by complementing all the variables. Suppose, for instance, we want to check whether (37) implies the atomic proposition $x_{1}$ . We add the objective function 'minimize $x_{1}'$ to (38) and replace each $x_{j}$ with $1 - \overline{x}_{j}$ to obtain,

$$
\begin{array}{l l l} \min & x _ {1} \\ \text {s.t.} & - \bar {x} _ {1} + \bar {x} _ {2} + \bar {x} _ {3} & \geq 0 \quad (y _ {1 1}), \\ & - \bar {x} _ {1} & + \bar {x} _ {3} + \bar {x} _ {4} \geq 0 \quad (y _ {1 2}), \\ & & - \bar {x} _ {3} + \bar {x} _ {4} \geq 0 \quad (y _ {3 1}), \\ & & - \bar {x} _ {4} \geq 0 \quad (y _ {4 1}), \\ & \bar {x} _ {1}, \bar {x} _ {2}, \bar {x} _ {3}, \bar {x} _ {4} \leq 1 & (y _ {1 0}, \dots , y _ {4 0}). \end{array}\tag{39}
$$

The dual of a linear program $\min\{cx \mid Ax \geq a\}$ is $\max\{ya \mid yA = c, y \geq 0\}$ , where y is a vector of dual variables (discussed in any linear programming text, such as [16]). To write the dual of (39) we associate dual variable $y_{ij}$ with the j-th rule containing consequent $x_i$ , as illustrated in (39). We also associate dual variable $y_{i0}$ with each bound $\bar{x}_i \leq 1$ . (Note that the bounds $\bar{x}_j \geq 0$ are not needed in a Horn problem.) Thus the dual of (39) is,

$$
\begin{array}{l l} \max & - y _ {1 0} - y _ {2 0} - y _ {3 0} - y _ {4 0} \\ \text {s.t.} & - y _ {1 0} - y _ {1 1} - y _ {1 2} = - 1, \\ & - y _ {2 0} + y _ {1 1} = 0, \\ & - y _ {3 0} + y _ {1 1} + y _ {1 2} - y _ {3 1} = 0, \\ & - y _ {4 0} + y _ {1 2} + y _ {3 1} - y _ {4 1} = 0, \quad \text {all} y _ {i j} \geq 0. \end{array} \tag {4}\tag{40}
$$

Jeroslow and Wang's result says that any vertex solution of (40) is integral; in fact, the solution is $y_{12} = y_{31} = 1$ , $y_{41} = 2$ , and all other $y_{ij} = 0$ .

Theorem 9 (Jeroslow and Wang [54]). If $Ax \geq a$ is a Horn set, let $B\overline{x} \geq b$ be the system that results when each $x_j$ is replaced by $1 - \overline{x}_j$ . Then for any $k$ the constraint set of the LP dual of the problem $\min\{-\overline{x}_k | B\overline{x} \geq b, \overline{x}_j \leq 1 \text{ for all } j\}$ defines an integral polytope.

Furthermore, the fact that $y_{12}=y_{31}=1$ in the dual solution indicates that the corresponding clauses, $x_{1}-x_{3}-x_{4}\geq0$ and $x_{3}-x_{4}\geq0$ , serve as resolution parents once in a resolution proof of $x_{1}$ . Since $y_{41}=2$ and $y_{11}=0$ , $x_{4}\geq1$ serves twice as a parent in this proof, and $x_{1}-x_{2}-x_{3}\geq0$ not at all.

Finally, we briefly indicate how Theorem 9 relates to dynamic programming and networks. Let $J(i, l)$ contain the indices of the variables occurring in the $l$ -th rule with consequent $x_i$ , and let there be $m(i)$ such rules. Then the constraint set of (39) in general has the form,

$$
\bar {x} _ {i} \leq \alpha_ {i l} + \sum_ {j \in J (i, l)} \bar {x} _ {i}, \quad l = 1, \dots , m (i), \quad \text { all } i,\tag{41}
$$

where $\alpha_{il}$ is 0 or 1. The problem of minimizing $-\bar{x}_{k}$ subject to (41) has the same solution as,

$$
\overline {{x}} _ {i} = \min \biggl \{\alpha_ {i l} + \sum_ {j \in J (i, l)} \overline {{x}} _ {j} | l = 1, \ldots , m (i) \biggr \},\tag{all i.}
$$

(42)

For instance, the solution $(\overline{x}_1, \overline{x}_2, \overline{x}_3, \overline{x}_4) =$

(0, 0, 0, 0) of (39) also solves,

$$
\begin{array}{l} \overline {{{x}}} _ {1} = \min \big \{\overline {{{x}}} _ {2} + \overline {{{x}}} _ {3},   \overline {{{x}}} _ {3} + \overline {{{x}}} _ {4} \big \}, \\ \overline {{{x}}} _ {3} = \overline {{{x}}} _ {4}, \\ \overline {{{x}}} _ {4} = 0. \end{array}
$$

(See [54] for a precise statement of this result.) Readers familiar with dynamic programming will recognize (42) as a dynamic programming recursion. The problem therefore has the network structure that characterizes such dynamic programming problems (see [24] for background).

Although Theorems 8 and 9 uncover some interesting connections between Horn clauses and mathematics, to date they have not led to quantitative inference methods competitive with the linear-time symbolic methods for Horn problems.

## 8.2. Totally Unimodular LP Relaxations

We remarked that one way an LP relaxation can answer the inference question is to have an integral solution. Thus LP problems with integral polytopes are of great interest (not only for logic), since the simplex method always find a vertex solution and therefore, for such problems, an integral solution.

Integral polytopes characterize more classes of problems than one might expect. The best-known class is that of problems whose coefficient matrices are totally unimodular, meaning that the determinant of every square submatrix is 1, -1 or 0. Thus inference problems with totally unimodular constraint matrices form a rather large and unstudied class of inference problems soluble in polynomial time, since LP's are soluble in polynomial time.

Obviously a totally unimodular matrix must consist entirely of 1's, -1's and 0's, as does the matrix for a logical inference problem. Several necessary and sufficient conditions have been proved for total unimodularity, such as the following. Let the row (column) sum of a matrix be even when the rows (columns) sum to a vector with all even components. Then a matrix is totally unimodular if and only if the sum of the entries in any square submatrix with even row and column sums is divisible by four [11,12], and if and only if the columns can be split into two parts so that the sum of the columns in one part minus the sum of the columns in the other part is a vector with entries 1, -1 and 0 [34,71]. These and most other criteria require exponential time to check a matrix for total unimodularity, but a remarkable theorem of Seymour [81] characterizes totally unimodular matrices as composed in a certain sense of 'network matrices' and permits a polynomial time check [20,79].

What is needed, however, is a condition easily applied in a logical context, and it is unclear how the above conditions might meet this need.

## 9. The Boolean Projection Problem

The foregoing discussion deals with the decision problem for inference: the problem of testing whether a given proposition can be inferred from a knowledge base. There is a more general but closely related problem that has great practical import. This is the problem of inferring in some sense everything that relates to a given topic. An investigation of this problem reveals a parallel between logic and mathematics in addition to those already discussed.

Specifically, we will see that one natural way of making this general inference problem precise shows it to be identical to a certain projection problem in polyhedral theory. Williams [91] has observed that Fourier elimination, a well-known projection technique, is easily modified to solve this problem, and this modification is identical to resolution.

## 9.1. Formulation of the Problem

Suppose we have a medical knowledge base in which some of the variables are 'disease variables' in that they are atomic propositions to the effect that the patient has a certain disease. If the object of an expert system is diagnosis, then what the user really wants to know is everything that can be truly said using only disease variables. In other words, the knowledge base, along with statements about symptoms and laboratory tests, is likely to imply such propositions as, 'the patient has disease X or disease Y', or 'the patient does not have both disease X and disease Y', and the user wants to know all such statements that are implied.

The problem of identifying all implications that contain only disease variables is a projection problem. We can make this precise as follows. Let the knowledge base contain variables $x_{1}, \ldots, x_{n}$ , and let $x_{1},\ldots,x_{k}$ be the disease variables. Recall that the meaning of a proposition is given by the set of truth assignments $(x_{1},\ldots,x_{n})$ that are compatible with it (i.e., that satisfy it). Thus to know everything that a system $Ax\geq a$ of clauses says about the patient's disease is to know which truth assignments $(x_{1},\ldots,x_{k})$ involving only the disease variables are compatible with $Ax\geq a$ . But $(x_{1},\ldots,x_{k})$ is compatible with $Ax\geq a$ just in case there is at least one way to assign truth values to the remaining variables to get an assignment $(x_{1},\ldots,x_{n})$ that satisfies $Ax\geq a$ .

So, we can find all the assignments $(x_{1},\ldots,x_{k})$ compatible with $Ax\geq a$ by looking at each complete assignment $(x_{1},\ldots,x_{n})$ and dropping the nondisease variables to zero to get the projection $(x_{1},\ldots,x_{k})$ of x. The collection of all assignments $(x_{1},\ldots,x_{k})$ obtained this way represents all that can be inferred in terms of disease variables.

One way to capture the inferred information in propositions is to find a set of constraints $Bx \geq b$ defining a polytope that contains precisely those integer lattice points that are projections of integer lattice points in the relaxed polytope for $Ax \geq a$ . In other words, the integer hull for $Bx \geq b$ is the projection of that for $Ax \geq a$ . We will say that such a system $Bx \geq b$ is a boolean projection of $Ax \geq a$ . (A boolean projection is presumably more useful if $Bx \geq b$ is a system of clauses and bounds $0 \leq x \leq e$ , since in this case the constraints have an easily recognized logical meaning.) The general inference problem, then, can be interpreted as the problem of finding a boolean projection of a system of clauses.

## 9.2. Resolution and Fourier Elimination

Like the decision problem for inference, the boolean projection problem can be solved either symbolically or numerically. One straightforward symbolic technique is resolution. To see this, suppose we carry out the resolution algorithm on $Ax \geq a$ (section 7.1) but restrict ourselves to resolutions on $x_{k+1}, \ldots, x_n$ . If we then delete all clauses containing any of the variables $x_{k+1}, \ldots, x_n$ , we obtain a system $Bx \geq b$ of clauses that jointly imply all and only implications of $Ax \geq a$ containing variables $x_1, \ldots, x_k$ . Thus $Bx \geq b$ is a boolean projection of $Ax \geq a$ .

Suppose for example we want to deduce all we can from (6)-(10) involving variables $x_{1}$ and $x_{2}$ .

The output of the resolution algorithm, restricted to resolutions on $x_{3}$ and $x_{4}$ , is the set of clauses, $x_{1}$ or $x_{2}$ ,

$$
\begin{array}{l} \text {not-} x _ {1} \text {or} x _ {2}, \\ \text {not-} x _ {1} \text {or} x _ {3}, \\ \text {x} _ {1} \text {or} \text {not-} x _ {3}, \\ \text {not-} x _ {1} \text {or} x _ {4}. \end{array}\tag{43}
$$

Deleting the last three (since they contain $x_{3}$ or $x_{4}$ ), we conclude that the first two capture all that can be inferred regarding $x_{1}$ and $x_{2}$ . We can now, if we wish, apply the resolution algorithm to this set of two clauses to reduce it to its prime implications. Here they are equivalent to a single prime implication, $x_{2}$ .

A numeric way to solve the boolean projection problem is to treat it as a projection problem in linear algebra. We can use a modification of Fourier elimination to find a boolean projection of $Ax \geq a$ onto $x_{1}, \ldots, x_{n-1}$ , then onto $x_{1}, \ldots, x_{n-2}$ , and so on down to $x_{1}, \ldots, x_{k}$ . This method turns out to be identical to resolution.

Fourier elimination is a method of eliminating a variable, say $x_{n}$ , from a system $Ax \geq a$ of inequalities. The resulting system defines a polyhedron that is the projection onto $x_{1}, \ldots, x_{n-1}$ of the polyhedron defined by $Ax \geq a$ . Suppose, for example, we wish to eliminate $x_{4}$ from (13). Then we rearrange all inequalities involving $x_{4}$ so that $x_{4}$ is alone on one side of the inequality:

$$
\begin{array}{r l} - x _ {1} + x _ {2} + 1 & \geq x _ {4} \\ 1 & \geq x _ {4} \\ x _ {4} & \geq x _ {1} + x _ {3} + 1 \\ x _ {4} & \geq 0. \end{array}
$$

We now form new inequalities by setting each expression on the left of $x_{4}$ greater than or equal to each expression on the right. In this case there are four pairings, which yield the inequalities,

$$
- 2 x _ {1} + x _ {2} - x _ {3} \geq - 2,\tag{44}
$$

$$
- x _ {1} + x _ {2} \geq - 1,\tag{45}
$$

$$
- x _ {1} \quad - x _ {3} \geq - 2,\tag{46}
$$

$$
1 \geq 0.\tag{47}
$$

Since (45)-(47) are redundant of the bounds $0 \geq x_{j} \geq 1$ , we add just (44) to the inequalities of (13) that do not contain $x_{4}$ . The resulting system defines a polytope that is the projection of the relaxed polytope for (13) onto $x_{1}, x_{2}, x_{3}$ .

Note that (44) is simply the result of adding constraints 2 and 4 of (13) and letting the $x_4$ and $-x_4$ cancel, as we do when resolving these constraints. In fact we can obtain the resolvent $x_1 + x_2 - x_3 \geq -1$ of constraints 2 and 4 as follows: reduce (44) to $-2x_1 + 2x_2 - 2x_3 \geq -3$ by adding $x_2 \geq 0$ and $-x_3 \geq -1$ to (44), divide by 2, and round up the right-hand side. Thus resolution is Fourier elimination with an additional reduction and rounding up step. In similar fashion we can apply this modified Fourier elimination to the clauses of (13) not containing $x_4$ , as well as the resolvent $x_1 + x_2 - x_3 \geq -1$ , to obtain (43).

## 9.3. The General Projection Problem

The reason we seek a boolean projection rather than an ordinary linear projection is that the latter loses information. In mathematical terms, the integer lattice points in the projection of polytope Q need not all be projections of lattice points in Q. For example, the polytope Q defined by

$$
\begin{array}{l} x _ {1} + x _ {2} + x _ {3} \geq 1, \\ x _ {1} + x _ {2} - x _ {3} \geq 0, \\ x _ {1} - x _ {2} + x _ {3} \geq 0, \\ x _ {1} - x _ {2} - x _ {3} \geq - 1, \quad 0 \leq x _ {j} \leq 1, \quad j = 1, \ldots , 4, \end{array}
$$

contains lattice points $(1,0,0)$ , $(1,0,1)$ , $(1,1,0)$ and $(1,1,1)$ . But its projection onto $x_{1}$ is the entire interval defined by $0 \leq x_{1} \leq 1$ and thus contains a lattice point $x_{1} = 0$ that is the projection of no lattice point in Q. So, the projection of the relaxed polytope for an inference problem contains too many lattice points in general and therefore represents a weaker logical statement than desired.

An algebraic expression for the projection of the relaxed polytope may nonetheless provide useful cutting planes, as did the Fourier projection onto $x_1, \ldots, x_{n-1}$ . In general we project onto $y = (x_1, \ldots, x_k)$ the polytope defined by $\overline{A}y + \overline{B}z \geq b$ , where $z = (x_{k+1}, \ldots, x_n)$ . For our purposes $\overline{A}y + \overline{B}z \geq b$ has the form $Ax \geq a$ , $0 \leq x \leq e$ , where $Ax \geq a$ is a system of clauses. The projection is the set of points $y$ satisfying all constraints of the form $u\overline{A}y \geq ub$ for any row vector $u$ satisfying $u\overline{B} \leq 0$ , $u \geq 0$ . (Actually it is enough to consider all vectors $u$ that are extreme rays of the polyhedral cone defined by $u\overline{B} \leq 0$ , $u \geq 0$ .) Some of the constraints $u\overline{A}y \geq ub$ may, after reduction and rounding, provide valid inferences that are useful cutting planes.

For example, suppose we project the polytope defined by (13) onto $x_{1}$ and $x_{2}$ . The projection is the polytope defined by

$$
\begin{array}{c} 2 x _ {1} + x _ {2} \geq 1, \\ - 3 x _ {1} + x _ {2} \geq - 2, \quad 0 \leq x _ {2} \leq 1. \end{array}
$$

(This constraint set also happens to be a boolean projection of (13), since its two feasible lattice points (1, 0), (1, 1) are projections of lattice points in the original polytope). We can add $x_2 \geq 0$ to the first constraint, divide by 2, and round up to obtain the cut $x_1 + x_2 \geq 1$ . We can add $2x_2 \geq 0$ to the second constraint, divide by 3, and round up to obtain the cut $-x_1 + x_2 \geq 0$ . The former cut can be obtained by resolving constraints 1 and 5 of (13), but the latter cut is the resolvent of no two of the original constraints. Thus we obtain a cut that cannot be obtained in a single step of resolution or Fourier elimination. It can be obtained, however, in two steps of the same.

## 10. Future Directions

At the top of the research agenda is completing the development of fast methods for inference in propositional logic. In particular, the mathematical programming approach appears worthy of further investigation, since the LP relaxation of an inference problem provides information that helps direct the search for a solution and that is unavailable in a purely symbolic approach.

Both the branch and bound and cutting plane solution techniques for solving the generalized covering model have their advantages. The branch and bound approach permits the use of chaining to simplify subproblems in the search tree. The cutting plane approach permits the generation of separating cuts, which are particularly effective in directing the search. Both, as well as their combination, deserve further attention.

We saw that the branch and bound approach led to an essentially symbolic method, in which a variable fixing heuristic replaced the LP relaxation, and that this symbolic method seems to outperform branch and bound. But this scarcely indicates that quantitative methods should be de-emphasized. To begin with, the variable fixing heuristic performs well on random problems, but it remains to be seen how it does on highly-structured real problems, in which satisfying truth assignments may be 'harder' to find. Also the variable-fixing method was, after all, obtained by first devising a quantitative approach and reintroducing some symbolic elements, a strategy that may work in other contexts. For example, the current LP-based approaches are handicapped by the necessity of using a relatively sluggish general LP code to solve a problem with special structure. It may be possible to develop a fast, specialized LP algorithm for logic problems that has an important symbolic component.

Other research needs include stronger cutting planes for inference problems, ways to exploit the fact that a set of clauses may be ‘almost’ Horn, computational testing on large, realistic non-Horn data bases, and a better mathematical understanding of the characteristics of realistic data bases. It would also be useful to characterize classes of inference problems that are soluble in the LP relaxation, perhaps by appealing to the large literature on total unimodularity and related topics.

A broader research goal is the application of quantitative methods to logics beyond the propositional calculus. In particular, epistemic and doxastic logics (which take into account the strength of evidence for or belief in a proposition) should be addressed, as should multivalued and fuzzy logics (which account for vagueness), modal and temporal logics (which deal with necessity and time precedence), nonmonotonic logic (which allows inferences based partly on tacit assumptions that may be overturned by new evidence), and of course useful fragments of predicate logic (see [33,87,40,41]). It may even be possible to design a new logic that is suitable for applications but has convenient mathematical structure.

The spatial interpretation of propositional logic developed in these pages suggests a principle that may be helpful in discovering broader applications. Recall that when propositional logic is viewed from a semantic point of view, a formula can be seen as merely one way of describing its interpretation, which is a set of truth assignments to its variables. The same can be said of a formula in quantified logic, which is interpreted as a set of ordered n-tuples (i.e., a relation). Since the meaning of a formula can be identified with its interpretation, any description satisfied uniquely by that interpretation captures the full meaning of the formula. For instance, the meaning of a set of logical clauses is captured by any system of inequalities satisfied by precisely the integer lattice points that represent satisfying truth assignments for the clauses.

Thus the problem of inference can be conceived as the problem of starting with one description of an interpretation and proceeding to other true statements one can make about the interpretation. One way to proceed is the traditional one of using inference rules, such as resolution, to deduce other true statements in the same logical idiom. But another way is to exploit the mathematical structure of the interpretation to derive other truths about it in a mathematical idiom, perhaps by generating valid linear inequalities, as done in the cutting plane approach. Thus quantitative modeling of logic need not be seen as a contrived effort to impose on logic something that is foreign to it. Rather, one can see the traditional symbolic treatment of logic as only one, rather narrow approach that discovers only one type of structure in the underlying semantics, when there may be other approaches that perceive a much richer sort of structure. Since a fuller exploitation of structure oftens leads to more powerful methods, its seems worthwhile to examine the semantics of the more advanced logics for mathematical structure that is missed by the traditional symbolic analysis.

## References

[1] Adler, I., M.G.C. Resende, and G. Veiga, An Implementation of Karmarkar's Algorithm for Linear Programming, Dept. of Industrial Engineering and Operations Research, University of California, Berkeley, CA 94720 (1986).

[2] Bachant, J., and J. McDermott, R1 Revisited: Four Years in the Trenches, AI Magazine 5 (Fall, 1984) 21–32.

[3] Balas, E., and R. Jeroslow, Canonical Cuts on the Unit Hypercube, SIAM Journal of Applied Mathematics 23 (1972) 61–69.

[4] Blair, C.E., R.G. Jeroslow and J.K. Lowe, Some Results and Experiments in Programming Techniques for Propositional Logic, to appear in Computers and Operations Research.

[5] Barr, A., and E.A. Feigenbaum, The Handbook of Artificial Intelligence 2, William Kaufman (1982).

[6] Blair, C., Two Rules for Deducing Valid Inequalities for 0–1 Problems, SIAM Journal of Applied Mathematics 31 (1976) 614–617.

[7] Bledsoe, W.W., Non-resolution Theorem Proving, Artificial Intelligence 9 (1977) 1–35.

[8] Bledsoe, W.W., and D.W. Loveland, eds., Automated Theorem Proving: After 25 Years, Contemporary

Mathematics 29, American Mathematical Society, Providence, RI (1984).

[9] Boole, G., The Mathematical Analysis of Logic, 1847. Reprinted by Oxford University Press (1948).

[10] Buchanan, B., and E. Shortliffe, Use of MYCIN Inference Engine, in: Buchanan and Shortliffe, eds., Rule-Based Expert Systems, Addison-Wesley (1984) 295–301.

[11] Camion, P., Charactérisation des Matrices Unimodulaires, Cahiers du Centre d'Etudes de Recherche Opérationelle 5 (1963) 181–190.

[12] Camion, P., Characterizations of Totally Unimodular Matrices, Proceedings of the American Mathematical Society 16 (1965) 1068–1073.

[13] Chang, C.L., The Unit Proof and the Input Proof in Theorem Proving, Journal of the ACM 17 (1970) 698–707.

[14] Church, A., A Note on the Entscheidungsproblem, Journal of Symbolic Logic 1 (1936) 40–41, correction 101–102.

[15] Chvátal, V., Edmonds Polytopes and a Hierarchy of Combinatorial Problems, Discrete Mathematics 4 (1973) 305–337.

[16] Chvátal, V., Linear Programming, W.H. Freeman (1983).

[17] Cook, S.A., The Complexity of Theorem-Proving Procedures, Proceedings of the Third Annual ACM Symposium on the Theory of Computing (1971) 151–158.

[18] Cook, W., C.R. Coullard and Gy. Turán, On the Complexity of Cutting-plane Proofs, Working paper, Cornell University, Ithaca, NY (1985).

[19] Cook, S.A., and R.A. Reckhow, The Relative Efficiency of Propositional Proof Systems, Journal of Symbolic Logic 44 (1979) 36–50.

[20] Cunningham, W.H., and J. Edmonds, A Combinatorial Decomposition Theory, Canadian Journal of Mathematics 32 (1980) 734–765.

[21] Dantzig, G.B., Linear Programming and Extensions, Princeton University Press (1963).

[22] Davis, M., and H. Putnam, A Computing Procedure for Quantification Theory, Journal of the ACM 7 (1960) 201–215.

[23] Dowling, W.F., and J.H. Gallier, Linear Time Algorithms for Testing the Satisfiability of Horn Formulae, Journal of Logic Programming 3 (1984) 267–284.

[24] Dreyfus, S.E., and A.M. Law, The Art and Theory of Dynamic Programming, Academic Press (1977).

[25] Eisinger, N., What You Always Wanted to Know about Clause Graph Resolution, 8th International Conference on Automated Deduction, Lecture Notes in Computer Science 230, Springer-Verlag (1986) 316–336.

[26] Franco, J., On the Probabilistic Performance of Algorithms for the Satisfiability Problem, Information Processing Letters 23 (1986) 103–106.

[27] Franco, J., Search Rearrangement Backtracking almost always Requires $O(2^{n^{\alpha}})$ Time to Verify Unsatisfiability, Working paper, Dept. of Computer Science, Indiana University, Bloomington (1987).

[28] Franco, J., and M. Paull, Probabilistic Analysis of the Davis Putnam Procedure for Solving the Satisfiability Problem, Discrete Applied Mathematics 5 (1983) 77–87.

[29] Gallaire, H., and J. Minker, Logic and Data Bases, Plenum Press, New York (1978).

[30] Gallaire, H., J. Minker, and J.-M. Nicolas, Logic and Databases: A Deductive Approach, Computing Surveys 16 (1984) 153–185.

[31] Garey, M.R., and D.S. Johnson, Computers and Intractability: A Guide to the Theory of NP-Completeness, W.H. Freeman, San Francisco (1979).

[32] Garfinkel, R.S., and G.L. Nemhauser, Integer Programming, Wiley, New York, (1972).

[33] Genesereth, M.R., and N.J. Nilsson, Logical Foundations of Artificial Intelligence, Morgan Kaufmann (1987).

[34] Ghouila-Houri, A., Caractérisation des Matrices Totalement Unimodulaires, Comptes Rendus Hebdomadaires des Séances de l'Académie des Sciences (Paris) 254 (1962) 1192–1194.

[35] Glover, F., and H.J. Greenberg, Logical Testing for Rulebase Management, to appear in R. Jeroslow, ed., Approaches to Intelligent Decision Support, a volume in the Annals of Operations Research series.

[36] Gomory, R.E., Outline of an Algorithm for Integer Solutions to Linear Programs, Bulletin of the American Mathematical Society 64 (1958) 275–278.

[37] Gomory, R.E., An Algorithm for Integer Solutions to Linear Programs, in: R.L. Graves and P. Wolfe, eds., Recent Advances in Mathematical Programming, McGraw-Hill (1963) 269–302.

[38] Grötschel, M., and M. Padberg, Polyhedral Aspects of the Travelling Salesman Problem. I: Theory, II: Computation, in: E. Lawier, J. Lenstra, A. Rinnooy Kan, eds., The Travelling Salesman Problem: A Guided Tour of Combinatorial Optimization, Wiley (1982) 251–360.

[39] Guignard, M., and K. Spielberg, Logical Reduction Methods in Zero-one Programming (Minimal Preferred Variables), Operations Research 29 (1981) 49–74.

[40] Haack, S., Deviant Logic: Some Philosophical Issues, Cambridge University Press (1974).

[41] Haack, S., Philosophy of Logics, Cambridge University Press (1978).

[42] Haken, A., The Intractability of Resolution, Theoretical Computer Science 39 (1985) 297–308.

[43] Hansen, P., B. Jaumard and M. Minoux, A Linear Expected-time Algorithm for Deriving all Logical Conclusions Implied by a Set of Boolean Inequalities, Mathematical Programming 34 (1986) 223–231.

[44] Hayes-Roth, F., D.A. Waterman and D.B. Lenat, Building Expert Systems, Addison-Wesley (1983).

[45] Hooker, J.N., Generalized Resolution and Cutting Planes, to appear in R. Jeroslow, ed., Approaches to Intelligent Decision Support, a volume in the Annals of Operations Research series.

[46] Hooker, J.N., Resolution vs. Cutting Plane Solution of Inference Problems: Some Computational Experience, to appear in Operations Research Letters.

[47] Hooker, J.N., Input Proofs and Rank One Integer Programs, Working paper, Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, PA 15213.

[48] Jaumard, B., Extraction et Utilisation des Relations Booléennes pour la Résolution des Programmes Linéaires en Variables 0-1, Doctoral thesis, Ecole nationale superieure des télécommunications, Paris (1986).

[49] Jeroslow, R., Representability in Mixed Integer Programming, I: Characterization results, Working paper, Georgia Institute of Technology, Atlanta, GA (1984).

[50] Jeroslow, R., Computation-oriented Reductions of Predi-

cate to Propositional Logic, Working paper, Georgia Institute of Technology, Atlanta, GA (1985).

[51] Jeroslow, R., An Extension of Mixed-integer Programming Models and Techniques to some Database and Artificial Intelligence Settings, Working paper, Georgia Institute of Technology, Atlanta, GA (1985).

[52] Jeroslow, R., On Monotone Chaining Procedures of the CF Type, Working paper, Georgia Institute of Technology, Atlanta, GA (1985).

[53] Jeroslow, R.G., and J. Wang, Solving Propositional Satisfiability Problems, Working paper, Georgia Institute of Technology, Atlanta, GA (1987).

[54] Jeroslow, R.G., and J. Wang, Dynamic Programming, Integral Polyhedra and Horn Clause Knowledge Bases, Working paper, Georgia Institute of Technology, Atlanta, GA (1987).

[55] Karmarkar, N., A New Polynomial-time Algorithm for Linear Programming, Combinatorica 4 (1984) 373–395.

[56] Karp, R.M., Reducibility among Combinatorial Problems, in: R.E. Miller and J.W. Thatcher, eds., Complexity of Computer Computations, Plenum Press (1972) 85–103.

[57] Khakian, L.G., A Polynomial Algorithm in Linear Programming, Doklady Akademii Nauk SSSR 244 (1979) 1093–1096, Translated in Soviet Mathematics - Doklady 20, 191–194.

[58] Kneale, W., and M. Kneale, The Development of Logic, Oxford University Press (1962).

[59] Kowalski, R., A Proof Procedure using Connection Graphs, Journal of the ACM 22 (1975) 572–595.

[60] Kovács, L.B., Extended Set Covering Problem and Logical Programming, Working paper, Computer and Automation Institute, Hungarian Academy of Sciences, Budapest (1984).

[61] Lewis, H., Complexity Results for Classes of Quantification Formulas, Journal of Computer and System Sciences 21 (1980) 317–353.

[62] Loveland, D.W., Theorem-provers Combining Model Elimination and Resolution, in: Meltzer and Michie, edsd., Machine Intelligence 4, Edinburgh University Press (1969) 73–86.

[63] Loveland, D.W., Automated Theorem Proving: A Logical Basis, North-Holland (1978).

[64] Loveland, D.W., Automated Theorem Proving: Mapping Logic into AI, to appear in Proceedings of the International Symposium on Methodologies for Intelligent Systems, ACM SIGART Press.

[65] Luckham, D., Refinement Theorems in Resolution Theory, Symposium on Automatic Demonstration, Lecture Notes in Mathematics 125, Springer-Verlag (1970) 163–190.

[66] McCluskey, E.J., Minimization of Boolean Functions, Bell System Technical Journal 35 (1956) 1417–1444.

[67] McDermott, J., R1: A rule-based configurer of computer systems, Artificial Intelligence 19 (1982).

[68] McMullen, C., and J. Shearer, Prime Implicants, Minimum Covers, and the Complexity of Logic Simplification, IEEE Transactions on Computers C-35 (1986) 761–762.

[69] Miller, R.A., H.E. Pople, and J.D. Myers, INTERNIST-I, An Experimental Computer-based Diagnostic Consultant for General Internal Medicine, New England Journal of Medicine 307 (1982) 468–476.

[70] Nilsson, N.J., Principles of Artificial Intelligence, Tioga Publishing Company (1980).

[71] Padberg, M.W., A Note on the Total Unimodularity of Matrices, Discrete Mathematics 14 (1976) 273–278.

[72] Plaisted, J.A., Complete Problems in the First-order Predicate Calculus, Journal of Computer and System Sciences 29 (1984) 8–35.

[73] Pople, H.E., Knowledge-based Expert Systems: The Buy or Build Decision, in: W. Reitman, ed., Artificial Intelligence Applications for Business, Ablex (1984).

[74] Quine, W.V., The Problem of Simplifying Truth Functions, American Mathematical Monthly 59 (1952) 521–531.

[75] Quine, W.V., A Way to Simplify Truth Functions, American Mathematical Monthly 62 (1955) 627–631.

[76] Quine, W.V., Two Dogmas of Empiricism, in: From a Logical Point of View, Harvard University Press (1961).

[77] Quine, W.V., Word and Object, MIT Press (1964).

[78] Robinson, J.A., A Machine-oriented Logic Based on the Resolution Principle, Journal of the ACM 12 (1965) 23–41.

[79] Schrijver, A., Theory of Linear and Integer Programming, Wiley, New York (1986).

[80] Selberg, A., An Elementary Proof of the Prime Number Theorem for Arithmetic Progressions, Canadian Journal of Mathematics 2 (1950) 66–78.

[81] Seymour, P.D., Decomposition of Regular Matroids, Journal of Combinatorial Theory (B) 28 (1980) 305–359.

[82] Shortliffe, E.H., S.G. Axline, B.G. Buchanan, T.C. Merigan, S.N. Cohen, An Artificial Intelligence Program to Advice Physicians Regarding Antimicrobial Therapy, Computers and Biomedical Research 6 (1973) 544–560.

[83] Siekmann, J.H., ed., 8th International Conference on Automated Deduction, Lecture Notes in Computer Science 230, Springer-Verlag (1986).

[84] Stickel, M.E., A Prolog Technology Theorem Prover, New Generation Computing (1984) 309–322.

[85] Tseitin, G.S., On the Complexity of Derivations in the Propositional Calculus, in: A.O. Slisenko, ed., Structures

in Constructive Mathematics and Mathematical Logic, Part II (translated from Russian, 1968) 115–125.

[86] Turing, A., On Computable Numbers, With an Application to the Entscheidungsproblem, Proceedings London Mathematical Society 42 (1936) 230–265.

[87] Turner, R., Logics for Artificial Intelligence, Ellis Horwood (1984).

[88] Urquhart, A., Hard Examples for Resolution, Journal of the ACM 34 (1987) 209–219.

[89] Warren, D.H.D., L.M. Pereira and F. Pereira, PROLOG – The language and its Implementation Compared with LISP, Proceedings of the Symposium on Artificial Intelligence and Programming Languages (ACM); SIGPLAN Notices 12; and SIGART Newsletter 64 (1977) 109–115.

[90] Waterman, D.A., A Guide to Expert Systems, Addison-Wesley (1986).

[91] Williams, H.P., Fourier-Motzkin Elimination Extension to Integer Programming Problems, Journal of Combinatorial Theory (A) 21 (1976) 118–123.

[92] Williams, H.P., Logical Problems and Integer Programming, Bulletin of the Institute of Mathematics and its Applications 13 (1977) 18–20.

[93] Williams, H.P., Model Building in Mathematical Programming, Wiley (1985).

[94] Williams, H.P., Linear and Integer Programming Applied to the Propositional Calculus, International Journal of Systems Research and Information Science 2 (1987) 81–100.

[95] Wittgenstein, W., Tractatus Logico-Philosophicus (translated from German), Routledge and Kegan Paul (1961).

[96] Wos, L., D. Carson, and G. Robinson, The Unit Preference Strategy in Theorem Proving, AFIPS Conference Proceedings 26, Spartan Books (1964) 615–621.

[97] Wos, L., G. Robinson, and D. Carson, Efficiency and Completeness of the Set of Support Strategy in Theorem Proving, Journal of the ACM 12 (1956) 536–541.
