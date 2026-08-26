---
otero_id: 17271
otero_key: "3UXRTNN3"
title: "Analysis of the behavior of logic-based computation for deductive databases and default reasoning"
authors: "Colin E. Bell; Dae Yong Lee"
year: "1992"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(92)90044-p"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analysis of the behavior of logic-based computation for deductive databases and default reasoning

Colin E. Bell and Dae Yong Lee
University of Iowa, Iowa City, IA, USA

One advantage of logic programming is the ability to use formal logic to analyze program behavior. Formal logic provides a basis for demonstrating that a program will behave as the user intends. This paper attempts to present to the non-logician known program behavior results for logic programs in the context of deductive databases. Previous results are extended through an investigation of a class of programs more general than logic programs. Specific attention is given to computational approaches which involve the solution of a finite sequence of progressively larger integer linear programming problems (ILP's). Constraints for such problems are constructed by a form of logical unification. Results indicate

![](/api/attachments/3UXRTNN3/fulltext/images/391ad501adfb6dbd86803e161c124d3212cabe1a105e659f56eacf5eead8608a.jpg)

Colin E. Bell is Professor and Chairperson in the Department of Management Sciences at the University of Iowa. He holds B.A. and M.A. degrees from The University of California, Berkeley and a Ph.D. from Yale University. Professor Bell specializes in production scheduling as associate editor of Naval Research Logistics. His research has been published widely in Management Science, Operations Research, and Naval Research Logistics. Current research interests include issues of knowledge representation in deductive databases and operations research/artificial intelligence models for scheduling scientific experiments on spacecraft missions.

![](/api/attachments/3UXRTNN3/fulltext/images/24ce3aa97b604a16ad1388796a90d65ee2e2fc4d686b34d45cd392507e94ed71.jpg)

Dae Yong Lee is an Associate Professor in the College of Business Administration at Chosun University in Kwangju, Korea. He received his Ph.D. in Management Sciences from The University of Iowa. Professor Lee's research interests include logic programming, deductive databases, expert systems, and interaction between ILP and logic.

that under certain conditions the solution to the last ILP yields a Herbrand model for the original set of statements in logic.

Keywords: Deductive databases, Default reasoning, Logic programming, Models of logic programs.

## 1. Introduction

Logic programming has gained widespread attention because of the popularity of PROLOG as a programming language for knowledge-based applications. Although all known implementations of PROLOG are not pure logic programming languages, PROLOG captures many of the desirable features of logic programming. One such feature is to allow the programmer to approximate Kowalski's ideal [6]: Algorithm = Logic + Control in which the programmer specifies the Logic and the PROLOG interpreter worries about Control issues.

Logic programming is also appealing because formal logic can be used for demonstrating program correctness. In this paper we start by examining logic programs, gradually make a sequence of more general program assumptions, and end by considering computational approaches for programs whose assumptions are general enough to incorporate default reasoning. The Least Exception Logic (LEL) approach to default reasoning in $[10]$ is an example of the latter type of approach. As our assumptions become more general, we can provide less assurance that a program's behavior matches a user's intent. Thus, we must be progressively more careful about making claims of program correctness. Results in the early parts of the paper are well-known but worth bringing to the reader's attention, lest he or she be carried away with blind enthusiasm for logic programming. Section 4 contains a new (albeit negative) result concerning ‘forced models’. In Section 5, we examine properties of solution procedures analogous to LEL’s which alternate logical unification with solution of integer linear programming problems (ILP’s). Hopefully, the discussion in Section 5 provides some insight into the behavior of such computational processes.

Logic programming also provides a paradigm for deductive databases, relational databases supplemented by inference rules. A PROLOG program can be viewed as just such a deductive database. Allowing the presence of rules in addition to facts (tuples in a relation) provides for economy of storage. Rather than explicitly storing all knowledge, a deductive database allows for explicitly storing some knowledge as facts while deriving some conclusions from applications of its rules. If deductive databases are to be used in practice, it is important to answer the following question affirmatively: “will the system respond to user queries in the manner intended by the user?” Much of this paper is devoted to examining this question. We need to know two things: (1) how will the system respond? and (2) what was the user’s intent?

Because use of formal logic for discussing program correctness is a rather formal process, we will need to develop various model-theoretic concepts. Before being overcome by such formality we will present examples more casually in this section to illustrate the type of difficulty which will arise later.

All of the trouble arises from the presence of negation in a logic program. Such issues involving negation have been thoroughly examined in [7,15,16] and elsewhere. Using the symbol “ $\neg$ ” to denote negation, if one wishes to express (1) rules with negative conclusions, e.g. “if dodo(X), then $\neg$ flies(X)”; (2) negative facts, e.g. $\neg$ flies(tweety); or (3) rules with negation in their premise, e.g. “if bird(X) and $\neg$ dodo(X) and $\neg$ fried\_chicken(X) then flies(X)” then it becomes more difficult to analyze a program’s behavior.

In the remainder of this section, relevant concepts from logic programming are reviewed briefly. Statements will be written using the restricted subset of Edinburgh syntax for PROLOG described in the Appendix. The Appendix also contains definitions and examples of logical concepts such as 'term', 'literal', etc. Readers familiar with logic and with PROLOG should be familiar with our notation without relying on the Appendix. For standard logical negation we use the symbol “ $\neg$ ”. PROLOG has a built-in “negation as failure” operator, “not”. Negation as failure is an important issue in logic programming which has received widespread attention [1,2,7,9,14,15, 16]. Explicit use of PROLOG’s “not” will not be made in this paper. However, we will often use the spirit of negation as failure when we assume that a given literal is false if we have failed to prove it true.

A logic program can be viewed as a collection of facts and rules. A rule fits the following general pattern

$$
A: - L _ {1}, L _ {2}, \dots , L _ {n}. \quad n \geqslant 0,
$$

where A is a positive literal and $L_{1}, L_{2}, \ldots, L_{n}$ are positive or negative literals. A is the head (or conclusion) of the rule and $L_{1}, L_{2}, \ldots, L_{n}$ is its body (or premise). A rule with an empty body (i.e. n = 0) is called a fact and is simply written “A.” rather than “A:−.”

To illustrate the concepts of this section it is helpful to introduce the following two example logic programs concerning members of one author's family. Simple Programs 1 and 2 below provide for an informal glimpse of the analysis to follow. Note that Mom, Dad, and Child in Program 1 are logical variables (with more mnemonic value than say X, Y, and Z). Any logical variable appearing in a rule is implicitly universally quantified, e.g. one should read the father rule in Program 1 as “for all Dad and Child, if Dad is male and Dad is the parent of Child then Dad is the father of Child.”

## /\* Program 1 \*/

parent(colin, alison). % meaning “colin is a parent of alison”

parent(colin,kent).

parent(jenny, alison).

parent(jenny,kent).

male(colin).
male(kent).

female(jenny).
female(alison).

plays(kent,soccer).

father(Dad,Child):- male(Dad), parent(Dad,Child).

mother(Mom,Child):- female(Mom), parent(Mom,Child).

/\* end Program 1 \*/

/\* Program 2 \*/

needs\_ride(alison).

drives(kent).

needs\_chauffeur(X):- $\neg$ drives(X),
needs\_ride(X).

/\* end Program 2 \*/

Program 1 contains no negative literals. As a deductive database, the two rules allow the user to avoid explicit storage of father and mother facts. If queries were submitted to a PROLOG interpreter which has loaded Program 1, the interpreter would exhibit behavior intended by its author. In particular, it would respond exactly as expected when given a query about the predicates father and mother. You would probably also agree that the only reasonable conclusions about these two predicates are father(colin, alison), father (colin, kent), mother (colin, alison), mother (colin, kent).

Program 2 contains only two facts and one rule but is not quite so clean. It is not a valid PROLOG program because of the presence of “ $\neg$ ”, but it still satisfies the definition of a logic program. What are reasonable conclusions from this program? Program 2 mentions two objects, alison and kent. Who needs a chauffeur? Most readers will agree that the only way to demonstrate that someone needs a chauffeur is to successfully apply the program’s rule with conclusion needs \_chauffeur(X). Since drives(kent) is a fact and $\neg$ drives(X) is part of the rule’s premise, this rule cannot be applied with X = kent. Unfortunately, there are still two answers to the question of whether alison needs a chauffeur.

First, $\neg$ drives(alison) cannot be proved from Program 2. It is not a logical consequence of the program. No chain of reasoning using facts and rules allows one to derive $\neg$ drives(alison). If we cannot prove $\neg$ drives(alison), then we should not be able to use a rule that requires $\neg$ drives(alison) in its premise. Thus, we cannot conclude needs\_chauffeur(alison). Neither can we conclude $\neg$ needs\_chauffeur(alison) so the truth value of needs\_chauffeur(alison) is simply left undetermined.

Second, we can make an assumption of the author's intent. Surely, if drives(alison) were true he would have mentioned it as a fact along with drives(kent). Thus, we can assume that $\neg$ drives (alison) is true. We can then successfully apply the program's rule to conclude that needs\_chauffeur(alison) is true. The assumption made here is the Closed World Assumption (CWA) of Reiter [14]. This is a form of default reasoning: "with no evidence to the contrary, assume that any object mentioned in the program cannot drive." The default assumption is overridden only when one can prove from the program that an object mentioned in the program can drive, e.g. by observing the fact "drives(kent)." Default reasoning is often essential for real-world knowledge-based applications. However, its presence muddies the water when it comes to analyzing program behavior. Thus, in the case of Program 2, if we are willing to make an assumption, we get one answer; if we favor a strict approach without additional assumptions, we get another. Our analysis cannot suggest which alternative to choose.

We will refer to Programs 1 and 2 again in a more formal context. First, in the next section, we present various assumptions on program structure. In Section 3, we discuss methods for analyzing program behavior. Section 4 presents some results: Attempted analysis of program behavior using the methods of Section 3 on programs with various assumptions given in Section 2. In Section 5, computational approaches in the spirit of that used by LEL are analyzed. Such approaches may start with programs more general than logic programs in which negative or disjunctive conclusions to rules are allowed. In such cases, finding an appropriate set of truth values for literals appearing in the program typically requires extensive search. We present procedures in which such search is carried out in the process of solving a sequence of ILP's. Hopefully, the size of such ILP's is within reason and their special structure keeps the amount of search required manageable.

## 2. Assumptions on program structure

We have defined a logic program above as a collection of statements of the form:

$$
A: - L _ {1}, L _ {2}, \dots , L _ {n},
$$

where A is a positive literal, the rule's conclusion or head, and $L_{1}, L_{2}, \ldots, L_{n}$ are positive or negative literals which together form the rule's premise or body. Such program statements with a single positive literal for a conclusion are called Horn Clauses and a logic program is often called a Horn Clause Program. A program consisting exclusively of Horn Clauses in which no negative literals appear (e.g. Program 1) will be called a Definite Horn Clause Program. If a Horn Clause Program contains one or more negative literals (e.g. Program 2), then we will call it a Horn Clause Program with Negation to emphasize the presence of negative literals.

One restricted form of Horn Clause Program with Negation which has received much recent attention in [1,9] and elsewhere is the Stratified Horn Clause Program. In such a program, negation is allowed but only according to the following stratification protocol. The various predicates appearing in the program are classified into strata 1, 2, ..., m. A rule whose head contains a predicate in stratum i may have positive literals in its body containing predicates only from strata 1, 2, ..., i and may have negative literals in its body containing predicates only from strata 1, 2, ..., i - 1. There can be more than one acceptable stratification of predicates for a given program. Restricting the appearance of negative literals in this manner makes the behavior of a Stratified Horn Clause Program a bit easier to understand.

Program 2 can be stratified with stratum 1 = {needs\_ride, drives} and stratum 2 = {needs\_chauffeur}. Stratification supports an orderly processing of queries in which truth values of literals involving predicates at stratum i - 1 can be determined and used as inputs to the process of establishing truth values of literals involving predicates at stratum i. According to the usual convention for stratified programs, in Program 2 drives(alison) is assigned false (henceforth F) when stratum 1 literals are analyzed. This is then used to help assign true (henceforth T) to needs\_chauffeur(alison) when stratum 2 literals are analyzed.

Unfortunately, stratification is impossible for some Horn Clause Programs with Negation. Other programs possess multiple possible stratifications.

Since a Horn Clause Program has a single positive literal for the conclusion of each rule it obviously satisfies the following Condition 1.

Condition 1. Absence of negative conclusions to rules.

When this condition is satisfied, the program cannot contain negative assertions, e.g. “ $\neg$ flies (tweety)”, since a negative assertion is simply a rule with an empty premise and negative conclusion. We will later wish to examine programs which do not satisfy this condition, and thus are no longer logic programs.

The role of logical variables in rules is important. Difficulties arise when we try to state general universally quantified (i.e. “for all …”) facts or try to reach universally quantified conclusions to rules. The following two statements each meet the definition of a logic programming statement but can be a source of difficulty in analyzing a program’s meaning:

potential\_chauffeur(Anybody,X):-

$\neg \text{drives}(X),$

needs\_ride(X).

plays(Everyone, soccer).

These two statements violate the following Condition 2.

Condition 2. Covering Axiom. Any variable appearing in the conclusion of a rule must appear in a positive literal in the premise of the rule.

Since a fact is a rule with an empty premise, when the Covering Axiom is satisfied, the program cannot contain assertions with variables, e.g. “plays(Everyone,soccer).” Notice also that the simple rule “female(X):- $\neg$ male(X).” violates Condition 2.

Another condition concerning the role of logical variables is

Condition 3. Allowedness. Any variable appearing in a negative literal in the premise of a rule must appear in a positive literal in the same premise.

When Conditions 2 and 3 are satisfied, a logic program is well-behaved in the following sense. If given a ground query (like “?–flies(tweety).”), any rule used in a forward reasoning process will produce a ground conclusion. Also, by reordering literals in the premise of a rule, any negative literal is ground before being unified. Although negation must always be used with caution, it is generally preferable to be constrained to proving ground negative literals like “ $\neg$ flies(tweety)” rather than unground literals like “ $\neg$ flies(X).”

To this point we have defined a logic program and described special conditions which it may or may not satisfy: Definite Horn Clause Program, Horn Clause Program with Negation, Stratified Horn Clause Program, Condition 2, and Condition 3. We also observed that no logic program can violate Condition 1, the absence of negative assertions or negative conclusions to rules.

We now define a broader class of programs. A logic program statement can be mapped into a clause in Conjunctive Normal Form (CNF). The rule

$$
A := - L _ {1}, L _ {2}, \dots , L _ {n}.
$$

becomes

$$
A \vee \neg L _ {1} \vee \neg L _ {2} \vee \dots \vee \neg L _ {n}.
$$

Since we can rewrite $\neg (\neg L)$ as $L$ , any negative literal $L_{i}$ in the above rule becomes a positive literal in CNF. Thus a CNF representation of a rule is a disjunction of positive and negative literals. If the logic program statement is a Definite Horn Clause then the mapping from rule to CNF is 1-1. The original statement can be recovered from the CNF clause by recognizing that the only positive literal in the CNF clause is the original statement's conclusion and all negative literals in the CNF clause appear as positive literals in the original statement's premise. If the logic program statement contains negation in the premise then the mapping is many-to-1 and the original logic program statement cannot be recovered from the CNF clause. For example, the CNF clause

male(X) ∨ female(X),

might equally well have arisen from either of the rules

male(X):- $\neg$ female(X).

female(X):- $\neg$ male(X).

When we discuss more general programs in Section 5 we will consider a program as a collection of CNF clauses and will allow an arbitrary number of positive and negative literals in each clause. This flexibility permits clauses which might be assumed to come from negative facts, rules with negative conclusions, or rules with disjunctive conclusions (none of which are allowed in logic programming). We pay a price for this flexibility in representation: The behavior of the resulting program is harder to analyze and the computational process is more expensive. When we view a program as a collection of CNF clauses it is helpful to consider Condition 4 which, like conditions 2 and 3, concerns the role of logical variables:

Condition 4. Extended Covering Axiom. In a clause in conjunctive normal form, any variable appearing in a positive literal must also appear in a negative literal.

Notice that Condition 4 allows universal negative assertions like “ $\neg p(X)$ .” but does not allow universal positive assertions like “ $p(X)$ .” Conditions 1–3 refer to rules of a logic program and Condition 4 refers to CNF clauses. Thus, one must be careful in comparing these conditions that one is not comparing apples to oranges.

It is easily shown that: (a) If rule r satisfies both Conditions 2 and 3, then the CNF clause of rule r must satisfy Condition 4; (b) if rule r satisfies Condition 2 alone or Condition 3 alone, then the CNF clause of rule r may violate Condition 4; and (c) if a CNF clause satisfies Condition 4 it may have been derived from a rule r which violates either Condition 2 or Condition 3. Finally, if we insist that any CNF clause be derived from some rule r satisfying Condition 1 then: Rule r satisfies Conditions 2 and 3 if and only if the corresponding CNF clause satisfies Condition 4.

If Condition 4 holds then substitution of a constant for each variable in each negative literal will leave a clause with all ground literals. For example, forward reasoning in Program 2 yields the ground clause

drives(alison) ∨ ¬needs\_ride(alison) ∨

needs\_chauffeur(alison).

If, on the other hand, Program 2's last clause were modified to be

drives(X) ∨ ¬needs\_ride(X) ∨

potential\_chauffeur(Anybody, X).

which might come from a rule meaning “if X doesn't drive and $X$ needs a ride then Anybody is potentially $X$ 's chauffeur", then forward reasoning would yield a clause with an uninstantiated variable.

In this section we have classified programs as logic programs or sets of clauses in CNF. We have also discussed special conditions which programs may satisfy. In the next section, we present a framework for analyzing the behavior of a program.

## 3. Methods for analyzing program behavior

When we write a logic program, we generally ascribe meaning to the program's statements. We have a particular universe of objects in mind about which we are writing the program. In Programs 1 and 2, one author intends that the objects 'alison' and 'kent' represent his children, not dolls, hurricanes, or chimpanzees in the San Diego Zoo. Without writing it into the program, we know what 'alison' and 'kent' stand for. In order to discuss program correctness, we must be a little more formal. Accordingly, we will make frequent use of the Herbrand Universe and Herbrand Base of a program. These concepts have particularly simple definitions in light of the restrictive syntax which we have chosen to employ. This restricted syntax does not accommodate the definition of objects through functions. If fred and father\_of(fred) were legitimate objects then so would be father\_of(father\_of(fred)) and father\_of(father\_of(father\_of(fred))), etc. Without such functions, our programs contain a finite number of objects.

The Herbrand Universe is the set of all objects which appear in the program. In restricting attention to this set of objects for checking program correctness, we assume that program correctness is a concern only for conclusions involving those objects mentioned explicitly in the program. In Program 1 the Herbrand Universe is {colin, alison, kent, jenny, soccer} while in Program 2 it is {alison, kent}. The predicates or relations appearing in Program 1 are parent/2, male/1, female/1 plays/2, father/2, and mother/2 where the integer following the “/” is the number of arguments or ‘arity’. Predicates in Program 2 are needs\_ride/1, drives/1, and needs\_chauffeur/1.

The Herbrand Base of a program is the set of all atomic formulae which could be constructed using a predicate appearing in the program and using members of the Herbrand Universe as arguments. The Herbrand Base for Program 1 would include: male(colin), father(colin, alison), parent(alison, jenny), male(soccer), father(soccer, colin), and numerous other atomic formulae. Only the first two of these five specific examples are conclusions which we would all want to draw from the program. The complete Herbrand base for Program 2 is needs\_ride(alison), needs\_ride(kent), drives(alison), drives(kent), needs\_chauffeur(alison), needs\_chauffeur(kent).

If the Herbrand Base contains n elements, we can define $2^{n}$ distinct interpretations each of which assigns either T or F to each element. Interpretations which are consistent with the program's statements are called models. For a logic program, such interpretations assign T to all facts of the program and must not provide a contradiction to any of the program's rules. Thus, in Program 1, we could not assign T to parent(jenny, alison), T to female(jenny) but F to mother(jenny, alison). Program 1 has many models, among them: (1) The model which assigns T to only the given facts and the following four consequences of applying the two rules: father(colin,kent), father(colin, alison), mother(jenny,kent), and mother(jenny, alison); (2) the model which treats 'soccer' as of type 'sport' and alison, kent, jenny, and colin as of type 'person' and assigns T to exactly those members of the Herbrand Base which meet the following type restrictions: parent('person', 'person'), male('person'), female('person'), plays ('person', 'sport'), father('person', 'person'), and mother('person', 'person'); and (3) the model which assigns T to every member of the Herbrand Base.

For Program 1 we would have little trouble agreeing that Model (1) is somehow what we intended, that Model (2) is a bit bizarre since it would have to assign T simultaneously to father(colin,kent), father(kent,colin), and father(jenny,jenny), and that model (3) is more bizarre yet since it would also assign T to father(soccer, colin), etc. Logicians have little difficulty agreeing that Model (1) is also the most reasonable. Four common forms of analysis all reach the same conclusion. Let us consider these forms of analysis.

First, for a logic program it seems reasonable to assign the value T only to those ground literals which can be ‘proved true’ from the program. One way to do this is to repeatedly apply the $T_{P}$ -operator of van Emden and Kowalski [17], and thereby to investigate the effects of ‘forward reasoning.’ The $T_{P}$ -operator maps from the space of interpretations into the space of interpretations. Given an interpretation I, an assignment of either T or F to each element of the Herbrand Base, one application of the $T_{P}$ -operator yields a new interpretation which assigns T to exactly those ground literals which are a consequence of I and a single ‘firing’ of each applicable ground instance of a rule (or fact) in the program. A ground instance of a rule R has elements of the Herbrand Base substituted for any logical variables appearing in R. Such a ground instance of R is applicable if all positive (negative) literals in R’s premise are T (F) under interpretation I. When this rule ‘fires’ T is assigned to its conclusion.

For a general program in CNF, the $T_{P}$ -operator can be similarly defined. For a given interpretation I, one application of the $T_{P}$ -operator yields a new interpretation which assigns T (or F) to exactly those literals whose truth values are forced to be T (or F) through the analysis of ground instances of each CNF clause in the program.

Consider Program 1. We could assume that we start with the interpretation $I_{0}$ that assigns F to every literal. The first iteration yields interpretation $I_{1}$ in which T is assigned to only the facts of the program: the parent, male, female, and plays literals in the program. Applying the $T_{P}$ -operator to $I_{1}$ yields the new interpretation $I_{2}$ which assigns T to the same set of literals as does $I_{1}$ but also assigns T to father(colin, alison), father(colin, kent), mother(jenny, alison), and mother(jenny, kent). Applying the $T_{P}$ -operator to $I_{2}$ produces the interpretation $I_{3}$ which is identical to $I_{2}$ . Thus a fixed point of the $T_{P}$ -operator has been found. This interpretation is Model (1) which we claimed was most reasonable.

A second approach to analyzing Program 1 is to recognize that if $M_{1}$ and $M_{2}$ are both Herbrand Models (i.e. models which assign truth values to elements of the Herbrand Base) then so is their intersection, $M_{1} \cap M_{2}$ , which assigns T to exactly those literals assigned T by both $M_{1}$ and

$M_{2}$ . With this model intersection property and only a finite number of possible models, there must be a unique least model $M^{*}$ with the property that every other model assigns T to the set of elements of the Herbrand Base assigned T by $M^{*}$ . It is easy to show that Model (1) of Program (1) is this unique least Herbrand Model. Model (1) assigns T to as few elements as possible in the Herbrand Base without contradicting any facts or rules in Program 1. The use of a least model again reflects the position that it is reasonable to assign T to as few literals as possible, only those that can be proved true from the program.

A third related approach for a logic program is to seek a minimal supported model. A supported model views the program's statements as a potential means of justifying an assignment of truth values. A model is supported if it assigns T only to literals which appear in the head of a rule whose body is 'true.' (A fact, being a rule with an empty body, provides this kind of support.) Thus, in a supported model, there is at least some justification for assigning T to a literal. In Program 1, Model (1) again emerges as a supported model. Assigning T to the parent, male, female, and plays literals which appear as facts is justified by the appearance of these facts in the program. Assigning T to the four mother/father facts of Model (1) is justified because the premises of the program's two rules are true based on the assignment of T to the appropriate parent, male, and female literals.

A model M is minimal if there are no models which assign T only to a proper subset of those literals assigned T by M. Changing T to F for any subset of the 13 literals assigned T by Model (1) will not produce a model since the resulting interpretation will be inconsistent with the statements of Program 1. Thus, Model (1) is a minimal supported model.

A fourth approach which can be used for either a logic program or a general CNF program has even stronger justification. A forced model views the program's statements as a set of constraints on truth values and assigns T only to literals which are forced to be true by such constraints. Any literal is assigned F unless it is a fact, or is the consequence of some rule whose premise is forced to be true because of other truth assignments. Applying this approach to Program 1, Model (1) again emerges as a forced model. The parent, male, female, and plays literals which appear as facts must each be assigned T. Given this assignment, T must be assigned to the four mother/father facts of Model (1) because the premises of the program's two rules are forced to be true. Although the concept of 'forced model' might be more reassuring than 'supported model', it is more difficult to find practical situations in which a forced model emerges.

Clearly, any forced model is supported but not all supported models are forced. Since literals are assigned T in M as a result of propagating inviolable constraints, it would be impossible to find a new model by changing the assignment from T to F for some non-empty subset of literals assigned T in M. Thus, if a forced model exists, it is minimal and it is a supported model. Unfortunately, forced models have little practical value. Large classes of programs of practical interest can be shown to have no forced models.

For Program 1, it is encouraging that the same model results from (1) forward reasoning by application of the $T_{P}$ -operator, (2) application of the model intersection property to find a least model, (3) verifying that the model is a minimal supported model, and (4) viewing the program statements as constraints to find a forced model. Program 1 is a Definite Horn Clause Program. This special structure guarantees that the results of these four processes agree.

A Definite Horn Clause program supports only monotonic reasoning. If M is the model of Program P derived by any of the above four processes and Program P is modified by the addition of more Definite Horn Clauses, then all literals assigned T in M will be assigned T in any model of the revised program. Monotonic reasoning is appropriate for many fields of endeavor. A research mathematician proving theorem after theorem is encouraged by the fact that a successful proof of Theorem 1 will remain valid no matter how many additional theorems she proves. However, in realistic knowledge-based applications it can be essential to permit non-monotonic reasoning in which we allow for the possibility that tentative conclusions must be revised. Much of this paper focuses on such non-monotonic contexts.

Program 2 is a Horn Clause Program with Negation. Even though Program 2 is very short and has only 6 elements in its Herbrand Base and thus only $2^{6}=64$ interpretations, the presence of a negative literal in the premise of one of its rules prevents us from finding a mutually-agreed-upon interpretation by the four methods introduced above. Applying the $T_{P}$ -operator, we first assign F to all 6 elements. On the first iteration, the two facts needs\_ride(alison) and drives(kent) are assigned T while the other four literals remain false. On the next iteration, needs\_chauffeur(alison) is assigned T. This assignment is a fixed point.

Of the 64 interpretations, 48 directly contradict one of the program's two facts. Of the remaining 16, four are not models because they assign F to drives(alison), T to needs\_ride(alison), but F to needs\_chauffeur(alison). Thus, there are 12 models. The intersection of these 12 models assigns T to only the two facts drives(kent) and needs\_ride(alison) and is not a model. Thus, we cannot find a least model by taking intersections of models.

Support is defined with respect to a logic program's facts and rules. In Program 2, the two facts drives(kent) and needs\_ride(alison) are logical consequences of the program. Assigning T to only these two facts and to needs\_chauffeur(alison) yields a supported model. This interpretation somehow seems more reasonable than others. In order to justify that this interpretation is more reasonable than others, it is necessary to make additional assumptions. One way to proceed is to make the Closed World Assumption that any ground atomic formula which cannot be proved true is assumed false. This is particularly useful in database applications where, for example, a person for whom an airline reservation cannot be found is reasonably assumed not to have a reservation. Another approach is to restrict the class of models to one for which the model intersection property holds. This is used in program stratification approaches of [1] and [9]. We shall investigate both approaches below.

The two facts drives(kent) and needs\_ride(alison) are logical consequences of the program. Assigning T to only these two facts does not yield a model. Thus there is no forced model. We cannot assign T to needs\_chauffeur(alison) because there is nothing in the program that forces us to assign F to drives(alison). As mentioned above, the concept of forced model, although appealing, will be demonstrated to be useless in many applications. In particular, a Horn Clause Program with Negation will have a forced model only in highly restricted circumstances.

```prolog
drives(alison) ∨ ¬needs_ride(alison) ∨ needs_chauffeur(alison).
drives(kent) ∨ ¬needs_ride(kent) ∨ needs_chauffeur(kent).
```

In this section, we have introduced four approaches for finding a reasonable model of a logic program and have shown informally that these approaches reach the same conclusion for a Definite Horn Clause Program. In the case of Program 2, a Horn Clause Program with Negation, it was still possible to find a fixed point of the $T_{P}$ -operator and to find a minimal supported model, but there was no forced model and no least model.

For some knowledge-based applications involving non-monotonic (e.g. default) reasoning it is essential to be able to make negated assertions and/or to reach a negative conclusion from applying a rule. In Section 5, approaches to default reasoning which allow such possibilities are examined. A model is sought through the solution of a sequence of progressively more constrained integer linear programming (ILP) problems. The behavior of this sequential process is compared to that of a more idealized (but computationally impractical) approach which solves the ILP based on all constraints which could be constructed from the original program using the program's Herbrand Base.

Much of the analysis below will be based on examining an ILP constraint representation of the clauses of a program in CNF. To build a set of ILP constraints it is helpful to view a clause containing no variables as a constraint on truth values and a clause containing variables as shorthand for a collection of constraints on truth values. The last statement of Program 2 translates into the clause “drives(X) ∨ ¬needs\_ride(X) ∨ needs\_chauffeur(X).” which is shorthand for the following two ground clauses that result by making each possible substitution of a member of the Herbrand Universe for each logical variable appearing in the clause

Truth values must be assigned to the three literals in each of these CNF clauses to that at least one literal is T. If we let #drives(alison), #needs\_ride(alison), and #needs\_chauffeur(alison) be 0–1 variables which take on the value 0 for F and 1 for T then we require

```txt
#drives(alison) + (1 - #needs_ride(alison)) +
#needs_chauffeur(alison) ≥ 1,
#drives(kent) + (1 - #needs_ride(kent) +
#needs_chauffeur(kent) ≥ 1.
```

We will assume throughout that such ILP constraints are written as “ $\geqslant$ ” inequalities with 1 on the right hand side. Obviously, in a program of practical interest, the Herbrand Universe has many members, the cardinality of the set of ILP constraints constructed in this manner is large, and the number of 0–1 decision variables appearing is also large. Finding a feasible solution by general ILP solution methods is unrealistic. We will refer frequently to the ILP formulation obtained in the above manner by substituting each object in the Herbrand Universe for each variable in each clause. An ILP with this constraint set will be called a Herbrand ILP.

## 4. Analysis of logic programs

We first formalize the result demonstrated in Section 3 through the example of Program 1.

Theorem 1. For Definite Horn Clause Program P, there is a unique model $M(P)$ which is the least fixed point of $T_{P}$ , least model, minimal supported model, and minimal forced model of P.

Proof. First, the interpretation which assigns T to all literals in the Herbrand Base is clearly a model for P. Thus, the set of all models is non-empty (and finite).

Second, the model intersection property can be shown to hold. Let $M_{1}$ and $M_{2}$ be two distinct models. Let A be a literal assigned T by $M_{1}$ and F by $M_{2}$ . If A does not match the head of any rule in P, then there is nothing to prevent assigning F to A (as required by the model intersection property). If A matches the head of a rule, then one or more literals in the rule's body must be assigned F by $M_{2}$ . These literals would be assigned F under the model intersection property and the rule could not force a value of T for A.

Since the model intersection property holds, there must be a unique least model, $M(P)$ . Assume that $M(P)$ is not a forced model. Since a forced model must be minimal and $M(P)$ is the only minimal model, there must be no forced model. There must be some literal A assigned T but not forced to be T through Program P's rules and facts (viewed as constraints). Changing the truth assignment for A from T to F will yield a new model $M(P)\{-A\}$ since no rule with A in its conclusion will be violated, no rule with A in its premise will be violated, and the status of rules not involving A will be unchanged. But existence of this new model $M(P)\{-A\}$ contradicts the assumption that $M(P)$ is a least model. Thus $M(P)$ must be forced.

Finally, $M(P)$ is the least fixed point model of $T_{P}$ . On repeated applications of $T_{P}$ , the set of literals assigned T strictly expands until two successive applications of $T_{P}$ yield the same model, $\text{LFP}(P)$ . Thus, on the last application of $T_{P}$ , any literal A whose value is forced to be T because A is in the head of some rule R whose body is true, must already have been assigned T in the model $\text{LFP}(P)$ . Because $M(P)$ is a forced model, the set of literals assigned T in $M(P)$ must be a subset of the set of literals assigned T in $\text{LFP}(P)$ . Assume that A is a literal assigned T in $\text{LFP}(P)$ but F in $M(P)$ . Then there is no rule whose application forces A to be T. But then A would never be assigned T through any mapping by the $T_{P}$ -operator, a contradiction. Thus $M(P)$ and $\text{LFP}(P)$ must be identical. □

We can see immediately that Theorem 1 is not useful for Horn Clause Programs with Negation. Consider Program 3.

/\* Program 3 \*/

tired(fred):- $\neg$ confused(fred).

stressed(fred):- $\neg$ tired(fred).

confused(fred):- $\neg$ stressed(fred).

/\* end Program 3 \*/

Any model requires that two or more of the three literals in the Herbrand Base be assigned T. Applying the $T_{P}$ -operator once with the initial interpretation which assigns F to all three literals in the Herbrand Base yields an assignment of T to all 3 literals. Applying the $T_{P}$ -operator a second time yields the initial interpretation assigning

F to all three literals. Thus, starting with this initial interpretation, there is no fixed point.

Clearly, the model intersection property for Program 3 does not hold and there is no least model. The intersection of any two distinct minimal models (each of which assigns T to exactly two literals) is not a model since it assigns T to exactly one literal.

None of the four models for Program 3 are supported. Consider the model which assigns T only to tired(fred) and confused(fred). Since tired(fred) appears in the conclusion of only the first rule, it can be supported only by this rule. However, the premise $\neg$ confused(fred) is not true so the necessary support is absent. A symmetrical argument applies to each of the other two minimal models. The non-minimal model which assigns T to all three literals is also not supported. Since the concept of forced model is stronger than that of supported model, there are no forced models either.

Reasonable people might well disagree over an appropriate model for Program 3. The analysis of Program 3 might well make one uncomfortable with logic programming. We prefer the more positive frame of mind which recognizes that failure to yield a single agreed upon model may be a highly appropriate conclusion. Consider the three statements of Program 3 translated into CNF clauses

tired(fred) ∨ confused(fred).

stressed(fred) ∨ tired(fred).

confused(fred) ∨ stressed(fred).

If we view these as three facts in a database, how much do we really know about fred? We cannot provide a certain answer to the specific queries: "is fred tired?"; "is fred confused?"; or "is fred stressed?" We have provided four models for Program 3. In terms of the information content of the three disjunctive statements in CNF, any answer that we can provide for any query is consistent with at least one of the four models.

Still, we would like assurance that a logic program possesses a model which all of us would agree is appropriate. Theorem 1 provides this in the Definite Horn Clause Program case. Next, we discuss Horn Clause with Negation logic programs. The concept of ‘forced model’ has an associated level of reassurance to the user that T is assigned only to literals that can be proved true. We show quickly that ‘forced model’ has little or no practical value once we allow programs to contain negation.

Consider the following process for seeking a forced model. First, use all members of the Herbrand Universe in turn as values to substitute for logical variables to replace any rule containing one or more variables by a set of rules containing only ground literals. If the Herbrand Universe contains n objects and v distinct logical variables appear in rule R, then rule R would be rewritten as $n^{v}$ distinct rules with only ground literals. First, we can use constraint propagation on this set of rules with only ground literals to assign truth values to certain literals and modify the remaining set of constraints. This amounts to execution of the following loop

WHILE a fact “A.” can be found

Assign T to A;

remove fact “A.” from the program;

remove A from the premise of every rule in which A appears as a positive literal; remove all modified constraints which cannot be binding on the values of remaining literals (i.e. rules with $\neg A$ in their premise)

ENDWHILE

If this process terminates with an empty set of constraints, then a model has been found. At the very least, all literals assigned T in the execution of this WHILE loop must be assigned T in any model (if any model exists). In a Definite Horn Clause Program, a model can be built by assigning F to all still unassigned literals in the Herbrand Base.

It is exactly the above WHILE loop that is executed in searching for a forced model. Consider the class of Horn Clause Programs with Negation. Any rule has a positive literal for its head and any fact is a positive literal. Negated literals may appear only in the body of a rule. Theorem 2 below shows that the concept of forced model may be of limited value.

Theorem 2. For Horn Clause Program with Negation P, let $P^{*}$ be the program that results from removing all rules with negation from P. M is a forced model for Program P iff M is the minimal forced model for $P^{*}$ and M is a model for P.

Proof. Since $P^{*}$ is a Definite Horn Clause Program, it has a minimal forced model, M. If M is also a model for P then M is forced (by a subset of the constraints associated with model P) and M is minimal (otherwise M would not be minimal for $P^{*}$ ).

If M is a forced model for Program P then M is a model for $P^{*}$ . Assume, however, that M is not a forced model for $P^{*}$ . Let L be a literal assigned T by M which is not forced to have the value T by the facts and rules of $P^{*}$ . Then since M is a forced model for P, L must be forced to have value T by a larger set of facts and rules including one or more rules which were removed from those associated with P in defining $P^{*}$ . But no such removed rule R can force a value of T for the literal in its conclusion because R contains a negative literal $\neg L$ in its premise, no literal L can be forced to be F, and thus $\neg L$ cannot be forced to be T, and thus the premise of R cannot be forced to be true and cannot force a value on the conclusion of R.☐

Theorem 2 quickly demonstrates that Program 2 has no forced model. Reduced program $P^{*}$ consists of just the two facts and its forced model M assigns T to exactly these two facts. M is not a model for Program 2 because the program's rule with X = alison is not satisfied.

Applying the above WHILE loop to Programs 1 and 2, when the WHILE loop terminates for Program 1, remaining rules are

father(colin, colin):- parent(colin, colin).

father(colin,jenny):- parent(colin,jenny).

father(colin,soccer):- parent(colin,soccer).

father(alison, colin):- male(alison), parent(alison, colin).

mother(colin, colin):- female(colin), parent(colin, colin).

father(soccer,soccer):- male(soccer), parent(soccer,soccer).

Since the premise of every remaining rule contains at least one positive literal, a model can be built by assigning F to each literal appearing in any of these rules.

In Program 2, when the WHILE loop terminates, the only remaining rule is

needs\_chauffeur(alison):- $\neg$ drives(alison).

and the literals needs\_ride(alison) and drives (kent) have both been assigned T. This remaining rule has three feasible truth assignments. The 12 models of Program 2 are obtained from 'crossing' these three solutions with the four assignments of truth values to the two literals needs\_ride(kent) and needs\_chauffeur(kent) which do not appear in the remaining rule and whose truth values have not been established.

We now turn attention to recent efforts to provide a format for logic programs which allows negation, is sufficiently restricted to make use of negation only in controlled circumstances, yet is general enough to accommodate programs of interest (including non-monotonic and default reasoning). Stratified logic programs are investigated in $[1,9,13]$ . Stratification is a useful construct for allowing controlled use of negation. Relations (predicates) are assigned to strata 1, 2, ..., S so that the use of negation in definitions is appropriately limited. Specifically: The definition of a predicate in stratum s may: (1) Make use of negated literals defined in strata 1, 2, ..., s - 1 but may not refer to negated literals defined in strata s, $s + 1, \ldots, S$ ; and (2) make use of positive literals defined in strata 1, 2, ..., s but may not refer to positive literals defined in strata $s + 1$ , $s + 2, \ldots, S$ .

Program 2 is a stratified program with S = 2, {needs\_ride, drives} in stratum 1 and {needs\_chauffeur} in stratum 2. Does this stratification give any sense of purpose to the development of an appropriate widely agreed upon model? If we have to make an assumption, should we do it about a predicate in stratum 1 first? For example, we could assume that drives(alison) = F since we have no facts or rules that would force drives (alison) to be T. Then there is only one remaining assignment:

needs\_chauffeur(alison) = T.

Recall that the WHILE loop in the previous section yielded a model for a Definite Horn Clause Program. In the presence of negation, we have seen that the four approaches to finding widely agreed upon models are not satisfactory. However, for a stratified logic program, the following approach which considers strata 1, 2, ..., S in turn yields a model with some appealing features.

A unique model can be found for a stratified logic program if the following strategy is adopted.

FOR Stratum = 1 to S DO

while a fact “A.” can be found in Stratum assign T to A;

remove fact "A." from the program;

remove A from premise of every other rule in which A appears;

remove all modified rules which have $\neg A$ in their premise

ENDWHILE;

assign F to all remaining positive literals L associated with Stratum;

substitute F for L in every rule in which L appears;

remove all modified rules have L in their premise

ENDFOR

With this approach, we assume that any literal is assigned the truth value F unless it is forced to be T. This is a form of Closed World Assumption (CWA). Unlike the CWA for a general logic program presented in [14], this CWA is implemented sequentially.

The results of executing the above WHILE loop is a model (since truth assignments are made so that no rules are violated). It is also a minimal model, since converting truth values from T to F for any subset of literals will no longer yield a model. This model is a supported model since literals are assigned T only as a result of applying a rule whose premise is already true. However, the resulting model is not necessarily forced since assumptions may have been made. In Program 2, the model developed assigns T to only the literals needs\_ride(alison), drives(kent), and needs\_chauffeur(alison). The last of these literals is not forced to be T since $\neg$ drives(alison) is not forced to be T.

Program 2 showed that there is no least model because the model intersection property does not hold. However, if we suitably restrict the class of models to consider, we can obtain a class of models called ‘natural’ by Naqvi for which the model intersection property holds. Thus, within the restricted class of natural models there is a least natural model.

A natural model is one which could be built sequentially by considering strata in the order 1, 2,..., S. First, a truth assignment is established for literals in the Herbrand Base associated with stratum 1. For literals associated with stratum s, any truth assignment must be consistent with the truth assignment already established for literals associated with strata 1, 2, ..., s - 1. Provided the overall truth assignment exhibits this consistency, the resulting model will be natural in the sense of Naqvi. Such natural models present an appealing way of handling negation. Whenever an attempt is made to prove that a negative literal is true, the literal is already ground. The attempted proof could then be viewed as requiring a simple reference to a table containing truth values for all possible ground instances of that literal.

## 5. Herbrand ILP solution methods

In this section we start by viewing a program as a set of (facts and) rules. We consider Conditions 1–3 with respect to such rules. If Condition 1 is satisfied, each CNF clause contains at least one positive literal. Since a fact is a rule with no premise, Condition 1 allows no negative assertions like “ $\neg$ flies(tweety).” Condition 1 is too restrictive to accommodate default reasoning where a negative assertion such as “ $\neg$ flies(tweety)” may be present yet the positive literal “flies(tweety)” would have been a logical consequence of a subset of the program’s facts and default rules. Conditions 2 and 3 concern the placement of logical variables within rules. Violation of one of these Conditions may have undesirable consequences in leaving some logical variables uninstantiated when a rule is otherwise ground.

Finally, we view a program as a set of CNF clauses. Condition 4 is appropriate when we view a program as a set of CNF clauses. The set of well-formed formulas which can be expressed in CNF includes rules with negative conclusions and rules with disjunctive conclusions. In short, we are allowed much more modeling flexibility than provided by a logic program framework.

This general CNF representation is appropriate for certain default reasoning contexts. For example, the clause

$$
\neg \operatorname{bird} (X) \vee \operatorname{flies} (X) \vee
$$

$$
\text { exception } (\text { non\_flying\_bird } (X)).
$$

might well have been derived from a rule with a disjunctive conclusion

flies(X) ∨ exception(non\_flying\_bird(X)):-
bird(X).

"Any bird either flies or is a non-flying-bird exception."

This type of rule appears in the Least Exception Logic (LEL) model of $[10,11,12]$ . The computational procedure of LEL alternates ILP solution with logical unification. LEL's forward reasoning process yields a sequence of progressively larger ILP's. Hopefully, no ILP solved in this process has anywhere near as many variables and constraints as the Herbrand ILP. The LEL computational process terminates after a finite number of rounds (of alternating unification with ILP solution). Without examining LEL in further detail, we can make some observations about the value of LEL and other approaches.

First, in all but the most trivial practical examples, the size of the Herbrand ILP makes its solution by general ILP solution techniques (e.g. branch and bound) fruitless. We visualize the Herbrand ILP as an appropriate set of constraints on truth values of all literals which could arise in a specific domain, but we do not want to attempt to solve it directly.

Second, there are usually many literals represented as decision variables in the Herbrand ILP whose truth values are not of interest. Hopefully, we would not have to exert computational effort to establish such truth value. For example, in Program 1, it can be expected that we would never pose a query involving parent(soccer,soccer). We should either be able to ignore its truth value or be able to establish its truth value through an efficient computational process. Indeed, we solve the Herbrand ILP for Program 1 by: (1) Applying the $T_{P}$ -operator to Program 1 until a fixed point is found; and (2) except for those literals whose truth values has been established as T by (1), assigning F to all literals. Steps (1) and (2) are both efficient. At the end of step (2) we are both efficient. At the end of step (2) we have a Herbrand ILP solution. This two step procedure is appropriate for a Definite Horn Clause program but not for the more general type of program represented as an arbitrary set of clauses in CNF.

In this section we address such two-phase computational procedures for solving the Herbrand ILP. Typically, the first phase terminates with an assignment of truth values to a subset of all literals in the domain while the second phase extends this partial solution to a feasible Herbrand ILP solution by assigning truth values to all other literals.

The LEL model of $[10]$ is a heuristic device for default reasoning. As such we expect that it (and other approaches in the same spirit) might appear to have undesirable properties when subjected to formal scrutiny. However, that does not imply that such approaches are not of practical value, since compromises are often required when default reasoning is involved.

In the remainder of this section we consider a finite program without functions. This gives rise to a Herbrand ILP with a finite number of variables and constraints. Examples in this section may appear to be of theoretical interest only. However, if small pieces of a large real-world application program violate assumptions which prevent these types of pathological behavior, then the behavior of the large program may also be pathological or at least difficult to analyze.

Again, consider Programs 1, 2, and 3 above. A model which is reasonable in all four senses can be found for Program 1 by 'forward reasoning', repeated application of the $T_P$ -operator. The Herbrand ILP can be solved without resorting to general ILP solution procedures such as branch and bound. This is true of all Definite Horn Clause Programs which satisfy our assumption of containing no function symbols (e.g. father\_of) and thus give rise to a finite Herbrand ILP.

For Stratified Horn Clause with Negation Program 2, the Herbrand ILP can also be solved by 'forward reasoning' paying careful attention to the stratification. For Stratum 1 with relevant constraints: #needs\_ride(alison) ≥ 1 and #drives(kent) ≥ 1, we assign 1 to #needs\_ride(alison) and #drives(kent). We assign 0 to #needs\_ride(kent) and #drives(alison), the other Stratum 1 decision variables which appear in no stratum 1 constraints of the Herbrand ILP. With these truth values fixed, we can satisfy the two stratum 2 constraints: #needs\_chauffeur(alison) + #drives(alison) + (1 - #needs\_ride(alison)) ≥ 1 and #needs\_chauffeur(kent) + #drives(kent) + (1 - #needs\_ride(kent)) ≥ 1 by assigning 1 to #needs\_chauffeur(alison) and 0 to #needs\_chauffeur(kent).

In both Programs 1 and 2, the Herbrand ILP could be solved without resorting to general ILP solution procedures such as branch and bound. With (unstratifiable) Horn Clause with Negation Program 3 we are not so lucky. The forward reasoning process does not terminate. Any Herbrand ILP solution is a model but is not supported. By minimizing the number of decision variables set to 1 we could find a minimal model. For a general program in CNF, solving the Herbrand ILP will produce a model, but the model may have little appeal. For Definite Horn Clause and Stratified Horn Clause with Negation Programs, the Herbrand ILP is solvable by a polynomial time forward reasoning algorithm. For more general programs such as Program 3, general ILP solution methods must be used.

Attention is now turned to programs with more general structure than Definite Horn Clause or Stratified Horn Clause with Negation Programs. In investigating them, we first consider Conditions 1–3 listed in Section 2. Conditions 1–3 refer to properties of a set of rules. We will investigate the behavior of a computational procedure in which a sequence of ILP's $\{ILP_{1}, ILP_{2}, \ldots\}$ will be generated and solved until two successive ILP's are identical. The set of constraints in any ILP in this sequence is a subset of all Herbrand ILP constraints. If $ILP_{n}$ , $ILP_{n+1}$ have constraint sets $C_{n}$ , $C_{n+1}$ then $C_{n}$ is a subset of $C_{n+1}$ . This iterative process terminates with ILP\* with constraint set $C^{*}$ . The process of extending a given feasible solution to ILP\* to a solution of the Herbrand ILP will then be investigated.

Results below do not depend on the choice of objective function for the various ILP's. Thus, the objective function will be unspecified. In some cases, generation of successive constraint sets corresponds exactly to application of the $T_{P}$ -operator. A solution to $ILP_{n}$ with constraint set $C_{n}$ corresponds to an assignment of truth values to all literals appearing in $C_{n}$ . Based on this assignment of truth values, constraint set $C_{n+1}$ for $ILP_{n+1}$ is constructed by adding more constraints to $C_{n}$ . This process must terminate because there are a finite number of Herbrand ILP constraints and the number of constraints in $ILP_{1}$ , $ILP_{2}$ , … increases as successive ILP's are generated. The exact procedure by which constraints are added is important for our analysis.

Simple Program 4 will illustrate our procedures. Since Program 4 contains no logical variables, it satisfies Conditions 2 and 3. It violates Condition 1 because of its last rule.

/\* Program 4 \*/

$$
s: - p, \neg r.
$$

$$
\neg s: - q, \neg r.
$$

/\* end Program 4 \*/

A rule $R$ has the general form

$$
A: - P _ {1}, P _ {2}, \dots , P _ {p}, N _ {1}, N _ {2}, \dots , N _ {n}.
$$

One possible procedure for extending constraint set $C_{n}$ to $C_{n+1}$ is to add constraints corresponding to all ground instances of rule R for which the solution to $ILP_{n}$ makes the premise of R ‘true.’ This is simply the application of the $T_{P}$ -operator and we shall say that we add constraints according to the ‘ $T_{P}$ -operator convention.’ Variables corresponding to $P_{1}, P_{2}, \ldots, P_{p}$ , and to the complements of $N_{1}, N_{2}, \ldots, N_{n}$ must all appear in $ILP_{n}$ and must have the appropriate truth value in the solution to $ILP_{n}$ . For Program 4, this procedure yields constraints $C^{*}$ corresponding to the two facts in the Program.

Since building ILP constraint sets of modest magnitude is important, it is helpful to insist on Condition 2. If the premise of rule R meeting Condition 2 is ground, then the conclusion will also be ground. If Condition 2 is violated, rule R could have a ground premise but its conclusion would be unground since it would contain at least one logical variable not appearing in the premise. In this instance, we could choose to add a separate constraint for each possible instantiation of such logical variables. In order to keep the size of ILP's within reason, we will add one constraint corresponding to rule R only when we discover an instance of R in which both premise and conclusion are ground.

Assume that Conditions 1, 2, and 3 are satisfied. With Condition 1, no ground literal will ever be forced to be F. Thus, only rules with no negative literals in their premise will have corresponding constraints added to successive ILP's as the constraint set $C^{*}$ is built according to the $T_{P}$ -operator convention. Every decision variable appearing in $C^{*}$ will be 1 (corresponding to an assignment of T to its literal). If there was a stratification for the original program, $C^{*}$ would yield the result of computing the values of all stratum 1 literals. If there was a stratification, computations could continue to find a natural model. For all predicate symbols P appearing in $C^{*}$ (e.g. “drives” in Program 2), one would assume that all ground literals formed with P but not appearing in $C^{*}$ (e.g. “drives(alison)” in Program 2) are F. Then one could add constraints for all remaining rules whose premise was made true by this assumption and could solve a new ILP, $C^{**}$ . This process could be iterated. Unfortunately, not all programs can be stratified. In the absence of stratification, it is not clear how to proceed.

For a stratified program satisfying Conditions 1–3, the procedure in the last paragraph never has to solve an ILP by search. If Condition 1 is relaxed so that rules could have negative conclusions, then $C^{*}$ could include rules with negative literals in their premise. With Condition 1 relaxed, it is necessary to further analyze the interaction between constraints. Thus, search may be necessary in solving ILP's. Program 4 illustrates this. The fact that r must be T follows from the interaction of the last two rules and cannot be deduced through forward reasoning.

This discussion is summarized in the following theorem.

Theorem 3. When Conditions 1–3 hold and a program can be stratified, adding constraints according to the $T_{P}$ -operator convention yields a solution to ILP\* corresponding to the assignment of truth values of all stratum 1 literals. Search is not required up to this point. By making appropriate assumptions, computations can be continued without search to find the solution to the Herbrand ILP corresponding to the ‘natural’ model. If Condition 1 is violated or if the program cannot be stratified, search may be required in solving one or more of the ILP's in the sequence $\{ILP_{1}, ILP_{2}, \ldots, ILP^{*}\}$ .

A second convention for adding constraints to $C_{n}$ to obtain $C_{n+1}$ is to add constraints corresponding to all ground instances of rule R for which the solution to ILP $_{n}$ makes $P_{1}, P_{2}, \ldots, P_{p}$ , all ‘true.’ $P_{1}, P_{2}, \ldots, P_{p}$ must all appear in ILP $_{n}$ and must be assigned T. With this second procedure, the presence of negative literals $N_{1}, N_{2}, \ldots, N_{n}$ in R is ignored in adding a constraint corresponding to a ground instance of R. For Program 4, this procedure yields constraints C\* corresponding to the two facts and two rules in the program. For want of better terminology, we call this the ‘more general convention’ for adding constraints. Its condition is easier to satisfy than the condition for the T $_{P}$ -operator convention. Thus ILP’s with larger constraint sets are often formed. Program 4 illustrates the fact that C\* must have no fewer constraints under the more general convention.

Assume that constraints are added according to the more general convention and that Conditions 2 and 3 are satisfied. Conditions 2 and 3 guarantee that if $P_1, P_2, \ldots, P_p$ are ground, all other literals in $R$ will be ground. Herbrand ILP constraints corresponding to ground instances of $R$ and missing from $C^*$ will then have one or more literals in $P_1, P_2, \ldots, P_p$ either not appearing in $C^*$ or false. If there are one or more false literals, the constraint is satisfied and can henceforth be ignored. Any remaining Herbrand ILP constraints missing from $C^*$ will then have one or more literals in $P_1, P_2, \ldots, P_p$ not appearing in $C^*$ . Arbitrarily assign $F$ to any one such literal, ignore the constraint as well as any other constraints corresponding to ground instances of rules in which the newly assigned literal appears as a positive literal in the premise. Continue this procedure until no more Herbrand ILP constraints missing from $C^*$ remain to be considered. Notice that this procedure does not alter the truth values already found when $C^*$ is solved. This situation is summarized in the following theorem.

Theorem 4. When Conditions 2 and 3 are satisfied, adding constraints according to the more general convention yields a solution to ILP\* which can be extended to a Herbrand ILP solution without search. However, search may be required in solving one or more of $\{ILP_1, ILP_2, \ldots, ILP^*\}$ .

Programs 5, 6, and 7 provide examples in which insistence that an instance of a rule be ground before an ILP constraint is introduced results in a set of constraints $C^{*}$ which is too small even when the more general convention for adding constraints is used. Search is then required in extending a solution of ILP\* into a Herbrand ILP solution. In Program 5, Condition 2 is violated.

$$
\begin{array}{l} \text {   /   } * \text {   Program   5   } * / \\ q (a). \\ s (a, a). \\ r (X, Y): - \neg p (X, Y), s (X, Y). \\ p (X, Y): - q (X). \\ \text {   /   } * \text {   end   Program   5   } * / \\ \text {   Herbrand   ILP   constraints   are   } \\ \# q (a) \geqslant 1, \\ \# s (a, a) \geqslant 1, \\ \# r (a, a) + \# p (a, a) + (1 - \# s (a, a)) \geqslant 1, \\ \# p (a, a) + (1 - \# q (a)) \geqslant 1. \end{array}
$$

$C^{*}$ includes only the first three of these constraints and has three acceptable pairs of values for $\#r(a,a)$ and $\#p(a,a)$ : (1, 1), (1, 0), and (0, 1). The last of these violates the last Herbrand ILP constraint. In this case, search is required to find a feasible Herbrand ILP solution.

If Condition 2 is satisfied, but Condition 3 is violated then again search may be required. Programs 6 and 7 are variations of each other in which both the constraint corresponding to the last rule and the variable $\#q(a,a)$ are not in $C^*$ . In Program 6, a Herbrand ILP solution must be built by setting $\#q(a,a)$ to 1; in Program 7, $\#q(a,a)$ must be set to 0. Thus it is not clear how to extend a solution to ILP\* to a Herbrand ILP solution.

$$
\begin{array}{l} / * \text {Program 6*} / \\ \neg p (a). \\ r (a). \\ p (X): - r (X), \neg q (X, Y). \\ / * \text {end Program 6*} / \end{array}
$$

$$
\begin{array}{l} / * \text {   Program   } 7 * / \\ \neg p (a). \\ r (a). \\ p (X): - r (X), q (X, Y). \\ / * \text {   end   Program   } 7 * / \end{array}
$$

We conclude with a brief discussion in which we assume that a program is expressed as a set of CNF clauses rather than as a set of rules. As mentioned above, the set of well-formed formulas which can be expressed in CNF includes rules with negative conclusions and rules with disjunctive conclusions. We assume a convention analogous to the ‘more general convention’ above for adding additional ILP constraints. A CNF clause Cl has the general form

$$
\mathrm{Cl}: P _ {1} \vee P _ {2} \vee P _ {p} \vee N _ {1} \vee N _ {2} \vee N _ {n}.
$$

A constraint will be added representing a ground instance of a CNF clause Cl whenever the current assignment of truth values to ground literals yields a false ground instance of $N_{1} \vee N_{2} \vee N_{n}$ . If Condition 4 is satisfied, all positive literals in Cl will also be ground. We will also call this the ‘more general convention’ since if all of our CNF clauses came from rules satisfying Conditions 2 and 3 and the more general convention was used in that context an identical sequence of ILP’s would be constructed.

The argument is the same as that leading up to Theorem 4. Assume that Condition 4 is satisfied. Herbrand ILP constraints corresponding to ground instances of Cl and missing from $C^*$ will then have one or more literals in $N_1, N_2, \ldots, N_n$ either not appearing in $C^*$ or true. If there are one or more true literals, the constraint is satisfied and can henceforth be ignored. Any remaining Herbrand ILP constraints missing from $C^*$ will then have one or more literals in $N_1, N_2, \ldots, N_n$ not appearing in $C^*$ . Arbitrarily assign $T$ to any one such negative literal $N_j$ (i.e. make its unnegated complement false), ignore the constraint as well as any other constraints corresponding to ground instances of CNF clauses in which $N_j$ appears. Continue this procedure until no more Herbrand ILP constraints missing from $C^*$ remain to be considered. Again, notice that this procedure does not alter the truth values already found when $C^*$ is solved. We can summarize this result in the following theorem.

Theorem 5. When a program is represented as a set of CNF clauses for which Condition 4 is satisfied, adding constraints according to the more general convention yields a solution to ILP\* which can be extended to a Herbrand ILP solution without search. However, search may be required in solving one or more of $\{ILP_1, ILP_2, \ldots, ILP^*\}$ .

In this section we have discussed approaches to finding a model by solving a sequence of ILP's. If Conditions 2 and 3 (in the case of a program represented as a set of rules) or Condition 4 (if the program is a set of CNF clauses) hold and the more general convention for building successively larger ILP constraint sets is used, then we are able to find a Herbrand ILP solution by a simple process from ILP\*. Although search may be required in solving $\{\mathrm{ILP}_1,\mathrm{ILP}_2,\dots ,\mathrm{ILP}^*\}$ , it should be pointed out that special structure of such ILP's can sometimes be exploited. In other cases, computational experience has shown that LP relaxations of such ILP's often contain few fractional variables in their solution and the successful search for an ILP solution is often not extensive. A discussion of such computational issues is provided in [5]. Hopefully, the approaches of alternating ILP solution and logical unification discussed in this section will stimulate additional research toward appropriate computational approaches to default reasoning.

## 6. Acknowledgement

The Research of Colin Bell was supported by a University of Iowa College of Business Administration Faculty Research Grant.

## 7. References

[1] K.R. Apt, H.A. Blair, and A. Walker, 'Towards a Theory of Declarative Knowledge', in [8].

[2] Clark, K.L., 'Negation as Failure', in [3].

[3] H. Gallaire and J. Minker, eds., Logic and Data Bases (Plenum, New York, 1978).

[4] H. Gallaire, J. Minker, and J-M. Nicolas, 'Logic and Databases: a Deductive Approach', Computing Surveys 16, No. 2, pp. 154–185 (1984).

[5] J.N. Hooker, 'A Quantitative Approach to Logical Inference', Decision Support Systems 4, pp. 45–69 (1988).

[6] R.A. Kowalski, ‘Algorithm = Logic + Control’, Communications of the ACM 22, No. 7, pp. 424–436 (Jul. 1979).

[7] K. Kunen, ‘Negation in Logic Programming’, Journal of Logic Programming 4, pp. 289–308 (1987).

[8] J. Minker, Foundations of Deductive Databases and Logic Programming (Morgan-Kaufman, Los Altos, CA, 1988).

[9] S.A. Naqvi, 'A Logic for Negation in Database Systems', in Proceedings of the Workshop on Foundations of Deductive Databases and Logic Programming, pp. 378–387, Washington, DC (1986).

[10] S.D. Post and C.E. Bell, 'Default Reasoning Through Integer Linear Programming', in Operations Research and Artificial Intelligence: The Integration of Problem Solving Strategies, eds. C.C. White and D.E. Brown, pp. 171–195 (Kluwer, Norwell, MA, 1990).

[11] S.D. Post, 'A System for Reasoning by Minimizing Exceptions.' Proceedings of the Third IEEE International Symposium on Intelligent Control. IEEE Computer Society Press, Los Angeles, CA (1988).

[12] S.D. Post, ‘Nonmonotonic Reasoning by Minimizing Contradiction in a Hedged Predicate Calculus.’ Proceedings of Expert Systems in Government Symposium. IEEE Computer Society Press, Los Angeles, CA (1987).

[13] T.C. Przymusinski, 'On the Declarative Semantics of Deductive Databases and Logic Programs', in [8].

[14] R. Reiter, 'On Closed World Data Bases', in [3].

[15] J.C. Shepherdson, ‘Negation in Logic Programming’, in [8].

[16] J.C. Shepherdson, 'Negation as Failure: a Comparison of Clark's Completed Data Base and Reiter's Closed World Assumption', Journal of Logic Programming, 1, pp. 51–79 (1984).

[17] M.H. van Emden and R.A. Kowalski, 'The Semantics of Predicate Logic as a Programming Language, Journal of the ACM 23, No. 4, pp. 841–862 (1976).

## Appendix A. Restricted subset of Edinburgh syntax for Prolog

This appendix describes the minimal subset of Edinburgh syntax required to understand example programs in the paper. These examples appear throughout the paper and are numbered as Programs 1–7. Concepts presented below are frequently illustrated by referring to these example programs.

An object is a string of one or more characters. The first character must be a lower case character; remaining characters may each be lower case characters or “\_”. An object plays the role of an argument in a relation. The following are all valid objects appearing in example programs 1–7: colin, alison, kent, jenny, soccer, fred, a.

A variable is a string of one or more characters. The first character must be an upper case character. A variable appears as an argument in a relation and any object may be substituted for it. Variables appearing in example programs 1–7 are Mom, Dad, Child, X, Y.

A predicate symbol is a string of one or more characters. The first character must be a lower case character; remaining characters may each be lower case characters or “\_”. A predicate symbol stands for the name of a relation between 0 or more objects. The following are all valid predicate symbols appearing in example Programs 1–7: parent, male, female, plays, father, mother, needs\_ride, drives, needs\_chauffeur, tired, stressed, confused, p, q, s, r.

A positive literal is either a predicate symbol (e.g. $p, q, s, r$ ) representing a relation with 0 arguments or a predicate symbol followed by one or more objects and/or variables enclosed in parentheses and separated by commas (e.g. plays(kent,soccer), male(colin), needs\_ride(X), $q(X, Y)$ ). The number of arguments of a relation is called arity. The arities of $p$ , plays(kent,soccer), male(colin), needs\_ride(X), $q(X, Y)$ are 0, 2, 1, 1, and 2 respectively.

A negative literal is a positive literal preceded by “ $\neg$ ” (e.g. $\neg$ drives(X), $\neg$ parent(Parent, Child)).

A term is a positive or negative literal. (Note that with a less restricted language than that used here, 'term' has a more complicated definition.)

A fact is a positive literal followed by “.” (e.g. “parent(colin, alison).”)

A rule is a positive literal followed by “:-” followed by one or more terms separated by commas, followed by “.” (e.g. father(F,C):- parent(F,C), male(F).). The literal to the left of “:-” is called the conclusion or head of the rule. Literals to the right of “:-” form the premise or body of the rule.

A fact is about a predicate p if the predicate symbol for that fact is p. A rule is about a predicate p if the predicate symbol for its conclusion is p. (e.g. the fact “male(colin).” is about the predicate ‘male’; the rule “father(F,C):- parent (F,C), male(F).” is about the predicate ‘father’.)

A procedure is an ordered sequence of facts and/or rules about the same predicate. (Notice that order of facts and/or rules within a procedure is important.)

A program is a collection of procedures. (Note that order of procedures within a program is unimportant.)

PROLOG has many built-in predicates, reserved words, and extra-logical features concerning program efficiency and input/output, etc. None of these are of concern in this paper. Most implementations of PROLOG also allow constants and variables to contain additional characters not mentioned above.
