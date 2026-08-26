---
otero_id: 24752
otero_key: "B853PUM6"
title: "DX: A Deontic Expert System"
authors: "Ronald M. Lee; Young U. Ryu"
year: "1995"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1995.11518073"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# DX: A Deontic Expert System

Ronald M. Lee & Young U. Ryu

To cite this article: Ronald M. Lee & Young U. Ryu (1995) DX: A Deontic Expert System, Journal of Management Information Systems, 12:1, 145-169, DOI: 10.1080/07421222.1995.11518073

To link to this article: https://doi.org/10.1080/07421222.1995.11518073

![](/api/attachments/B853PUM6/fulltext/images/6ff4b7a2a590411e2e2c71fab05ef7ca2278cbc2b146bf21eedf032a9d2cb99a.jpg)

Published online: 11 Dec 2015.

![](/api/attachments/B853PUM6/fulltext/images/2ea03c83fa462cd382d7a21acf43a95a0ba750e92e0e094a2e399a6eb0a22c97.jpg)

Submit your article to this journal ↗

![](/api/attachments/B853PUM6/fulltext/images/a4284268cefd6ac8a7d9835dd772446d5c2f2b33504c1bec597d466d8b471903.jpg)

Citing articles: 4 View citing articles ↗

# DX: A Deontic Expert System

RONALD M. LEE AND YOUNG U. RYU

RONALD M. LEE is the Director of the Erasmus University Research Institute for Decision Information System (EURIDIS) in Rotterdam, the Netherlands. Prior to that, he was Associate Professor of Information Systems at the Management Science and Information Systems Department at the University of Texas at Austin. He has a Ph.D. in decision sciences from The Wharton School, and has previously served as a research scholar at the International Institute for Applied Systems Analysis in Vienna and as Visiting Professor of Management at the Universidade Nova de Lisboa in Lisbon. His current research focuses on applications of artificial intelligence to business, with a special focus on logic modeling and the use of formal logic representations for management science applications. Current projects involve the use of logic modeling to represent and manage formal business communications systems, focusing on electronic commerce and governmental bureaucracies. Theoretical aspects include the role of deontic and illocutionary logic in representing formal business conversations. Practical value is the reduction of bureaucratic and legalistic red tape. This work also includes multilingual business communications and supporting structured communications between parties with different native languages.

YOUNG U. RYU is Assistant Professor of Information Systems, Decision Sciences Department, the University of Texas at Dallas. He received a Ph.D. in management science and information systems from the University of Texas at Austin. His research interests include logic-based modeling of bureaucratic policies and law, defeasible reasoning, nonmonotonic logic, artificial intelligence applications of management, and constraint logic programming of mathematical models.

ABSTRACT: Social norms have a pervasive effect on our lives, affecting how and what we eat, how we dress, where and how we travel, our recreation, the way we work, and our participation in the society at large. Other social norms make constraints on the behavior of commercial companies and other institutions, affecting the way they do business, their treatment of employees, their treatment of the environment, and so on. As societies grow and become more diverse, the system of norms becomes correspondingly complex. This paper attempts to bring computational assistance to bear in managing and interacting with these normative systems. A prototype expert system is described that utilizes deontic rules for reasoning about normative constraints in organizations and other social systems. Applications to bureaucracies and electronic contracting systems are discussed. DX can be used to model regulations and policies in organizations, such as library regulations of universities, resource access policies, and the like. Also, regulatory aspects in interorganizational systems (e.g., EDI) can be

Acknowledgment: The authors appreciate anonymous reviewers and the Editor-in-Chief of the Journal of Management Information Systems for useful comments, criticism, and suggestions that contributed to a significant improvement of the paper.

effectively modeled and managed by DX. Automated regulation and policy reasoning help manage normative rules and reduce complexity in their applications.

KEY WORDS AND PHRASES: bureaucratic systems, deontic logic, electronic contracting systems, expert systems, normative systems, performatives.

## 1. Introduction: The Ubiquity of Social Norms

SOCIAL NORMS ARE THE BASIS OF EVERY CIVILIZATION. They are the rules and conventions that guide the conduct of members of a society: how we dress, what and how we eat, where and how we travel, our recreation and the way we work. A primary purpose of social norms is to ensure equity. Some norms, such as styles of dress or table manners, are mainly conventional. Other norms have a more serious purpose of ensuring social equity. Thus, we have norms forbidding violence, theft, or fraud, where one individual takes unfair advantage of another. Still other norms serve the function of coordinating social activity. An example is traffic regulations, which dictate which side of the street to drive on, speed limits, when to stop, yield, and so on, in order to coordinate traffic flow. Similarly, other norms regulate commercial activity, transport, the postal service, telecommunications, and other types of services where a large number of individuals, companies, and institutions must interact cooperatively. Still other kinds of social norms are for purposes of social management, serving both equity and coordination objectives. Examples include taxation, military obligations, immigration and naturalization, import/export regulations, entitlements such as unemployment and housing benefits, public health services, and retirement benefits. All of these norms have in common the fact that they regulate human behavior.

Social norms vary in the degree to which they are articulated or made explicit. For example, it is a norm in Western societies that men wear darker, more conservative-colored clothes than women, though this is seldom stated explicitly. At the other extreme, certain norms are codified in the form of laws and published for the attention of all members of the society. Intermediate are organizational norms, the duties and conventions of the work place. Often these are communicated through informal on-the-job training; in more bureaucratic organizations the norms may be stated explicitly in the form of a job description.

For every norm, there is an enforcement or sanction imposed on violators. When informal norms are violated—such as bad table manners or outlandish dress—the sanction is typically disapproval—a raised eyebrow, a sarcastic remark. For civil and criminal laws, the sanction is more severe: a fine, a jail term, perhaps even execution. Again, organizational norms are an intermediate case. Most organizational norms are enforced by disapproval, perhaps a formal reprimand. More severe violations may lead to denial of a pay raise, demotion, or termination.

As the society grows more complex, with more specialization of roles and a wider range of activities in both work and leisure, the system of social norms also grows more complex. For instance, the EEC, attempting to regulate and coordinate all the diversity of the Common Market countries, is said to produce some 15,000 pages of reports and memoranda per day! (Most of this is translated to each of the nine languages of the member countries, multiplying the paper produced by nearly an order of magnitude.) Much of this documentation has to do with the adjustment of social norms. As the system of norms grows more complex, it also becomes more confusing, both to the people who must abide by them, as well as to the administrators who need to modify them. This has two undesirable effects. First, the social system becomes encumbered by bureaucratic overhead and so becomes less efficient. Second, the ability to make changes and adjustments to the system becomes increasingly difficult, leading to bureaucratic rigidity.

This is a situation where technological support is warranted. What we have in mind is a type of expert system whose rules represent the system of norms, and that is able to advise users of the rights, duties, and privileges that pertain to their specific circumstances. Furthermore, such an expert system should also provide aids to administrators in helping to adapt the rule base and determine the consequences of changes. The system would be made accessible to members of the organization or society through a computer network. Thus, changes in normative rules would be instantly available. As a practical consideration, such a system would only be workable for norms that are fairly explicit, thus subject to formalization as rules—for example, in areas such as income tax regulations, unemployment, and other welfare benefits, health insurance, or immigration and naturalization.

A problem arising from this proposal is that reasoning about norms involves a different kind of logic than is typically employed in expert systems. Norms are not true or false in the usual sense; for instance, a policy of no smoking does not guarantee that no one will smoke. What is needed is a different kind of rule representation and inferencing mechanism.

In the logic literature, normative reasoning is the subject of deontic logic, which formalizes such concepts as obligation, permission, and prohibition. Borrowing from this, we propose the notion of a deontic expert system, which incorporates deontic concepts in its rules and inferencing. Specifically, we will present a prototype deontic expert system, called DX, and demonstrate its operation and applicability. In later sections we discuss extensions to this basic model and its potential application to large-scale normative systems.

## 2. Computing Deontics

## 2.1. Standard Deontic Logic

DEONTIC LOGIC HAS ITS ORIGIN IN THE CLASSICAL PHILOSOPHY OF ETHICS. The modern development of deontic logic was initiated in the early 1950s by von Wright [35] who coined the term, based on the Greek δεόντως, meaning “as it should be” or “duly.” Deontic logic is a logic of normative concepts. Its major application, outside of ethics, has been to the philosophy of law. The practical relevance of deontic logic in administrative contexts is to provide automatic inference in, say, contract arbitration or the interpretation of bureaucratic regulations. Such applications are useful in complex cases where the chain of connections would otherwise be difficult to follow. Thus, the axioms and inference rules of deontic logic take on practical importance for normative systems that are complex yet explicit, amenable to formalization. The first axiomatization for deontic logic was proposed by von Wright [35, 36]. A basic concept is captured by the operator:

$$
\mathbf {O} \phi
$$

read that “ $\phi$ is obliged.” Based on this, a notion of permission can be defined as its logical dual:

$$
\mathbf {P} \phi = _ {\text { def }} \sim \mathbf {O} \sim \phi .
$$

that is, “ $\phi$ is permitted” if and only if “it is not obliged not to do $\phi$ .” A related concept of prohibition was defined as:

$$
\mathbf {F} \phi = _ {\text { def }} \mathbf {O} \sim \phi ,
$$

that is, “ $\phi$ is forbidden” if and only if “it is obliged not to do $\phi$ .” For completeness, we also add a notation for waiver (of an obligation):

$$
\mathbf {W} \phi = _ {\mathrm{def}} \mathbf {O} \sim \phi ,
$$

that is, “ $\phi$ is waived” if and only if “it is not obliged to do $\phi$ .”

Various axiomatic systems of deontic logic have been proposed. In an introductory survey, Føllesdal and Hilpinen [12] present what they call the standard system of deontic logic. Based on propositional logic, this serves as a more or less consensually accepted core on which to base further discussion. The standard system assumes elementary generic actions (in the sense of von Wright [36]). Assuming $\phi$ and $\psi$ to be actions of this type, the standard system has the following axioms:

$$
\mathbf {O} \phi \rightarrow \sim \mathbf {O} \sim \phi (\text { or   equivalently } \mathbf {O} \phi \rightarrow \mathbf {P} \phi).\tag{[DA1]}
$$

If $\phi$ is obliged, then $\phi$ is permitted.

$$
\mathbf {O} (\phi \& \psi) \leftrightarrow \mathbf {O} \phi \& \mathbf {O} \psi ;\tag{[DA2]}
$$

$\phi$ and $\psi$ are together obliged if and only if they are obliged separately.

$$
\mathbf {O} (\phi \vee \sim \phi).\tag{[DA3]}
$$

It is obliged to either do or not do $\phi$ .

Interesting theorems resulting from the above axioms and predicate calculus are $^{1}$ :

[DT1]

$$
\mathbf {F} \phi \rightarrow \mathbf {W} \phi .\tag{[DT2]}
$$

$$
\mathbf {O} (\phi) \&\mathbf {O} (\phi \rightarrow \psi) \rightarrow \mathbf {O} (\psi).\tag{[DT3]}
$$

$$
\mathbf {P} (\phi) \&\mathbf {O} (\phi \rightarrow \psi) \mathbf {P} (\psi).
$$

[DT4]

$$
\mathbf {F} (\psi) \&\mathbf {O} (\phi \rightarrow \psi) \rightarrow \mathbf {F} (\phi).\tag{[DT5]}
$$

$$
\mathbf {W} (\psi) \&\mathbf {O} (\phi \rightarrow \psi) \rightarrow \mathbf {W} (\phi).
$$

In fact, replacing the axiom [DA2] by the theorem [DT2] results in the same deontic logic system [12].

The deontic formulation $\mathbf{O}(\phi\to\psi)$ , which is often symbolized as $\mathbf{C}(\phi,\psi)$ , is called the commitment expression [35], whose behavior is expressed in [DT2–5]. A commitment expression is used to transform a deontic statement to another. For example, in an agency relation, duties and discretions of the principal are transferred to the agent; that is, an agency relation may be represented by commitment expressions.

The sense of the deontic operators obviously relies on what is meant by an action. Von Wright [36] comments:

A few words should be said about the reading of the formulae. In my first construction of a system of deontic logic the variables were treated as schematic names of actions. According to this conception, “Pp” could be read “It is permitted to p.” This conception, however, is connected with difficulties and inconveniences. It is, first of all, not clear whether the use of truth-connectives for forming compound names of actions is logically legitimate.

It now seems to be better to treat the variables as schematic sentences which express propositions. Instead of “proposition” we can also say “possible state of affairs.” According to this conception, “Pp” may be read “it is permitted that (it is the case that) p.”

Against this reading, however, it may be objected that it does not accord very well with ordinary usage. Only seldom do we say of a state of affairs that it is permitted, obligatory, or forbidden. Usually we say this of actions. But it is plausible to think that, when an action is permitted, etc., then a certain state of affairs is, in a “secondary” sense, permitted, etc. too. This is the state which, in a technical sense p can be called the result of the action in question. The formula “Pp” is thus read “it is permitted to see to it that (it is the case that) p” or “one may see to it that p.” [P. 16]

In the axioms, $\phi$ and $\psi$ are regarded as propositional variables. However, they are not exactly propositions in the usual sense of referring to a static state of affairs—for example, the window is closed. Rather, as names for generic actions, they refer to someone's causing a certain state to occur, such as closing the window. Thus, in this form of deontic logic, the concept of truth value is replaced by one of performance value [36]; in other words, whereas a proposition is either true or false, an action is either performed or not performed. Further, the actions controlled by these deontic operators presume an aspect of human agency. We do not obligate or permit natural phenomena such as the sun rising.

## 2.2. Computing Process for Deontic Reasoning

For our purposes, we would like to develop a computational version of deontic reasoning. This presents several challenges. First, the practical needs of an expert system for deontic reasoning require that we be able to distinguish how deontic status varies for different individuals: for example, in a contract, that Smith has an obligation to deliver a certain good, while Jones has an obligation to pay a certain amount of money. This leads us to pursue first-order deontic reasoning as propositional logic and its extension to predicate logic (see, e.g., [8] ch. 12). A second issue is that there is very little literature, and no readily available software, for computing modal operators. A third consideration, aside from computability, is the availability of a suitable implementation environment that facilitates programming and user-interface development. These aspects taken together lead us to attempt to couch the deontic concepts within the framework of program clause logic, computable through various logic programming languages, such as Prolog. $^{2}$ Logic programming [3, 24] is a subset of first-order logic with functions, where rules are expressed in the form:

$$
\phi \leftarrow \Psi_ {1}, \Psi_ {2}, \dots , \Psi_ {n},
$$

where $\phi$ and $\psi (i = 1,2,\dots ,n)$ are literals and commas between literals denote conjunction. Disjunction is expressed by having multiple rules for the same conclusion.

In short, we adopt aspects of deontic logic and develop a first-order program clause deontic reasoning system. The deontic reasoning system, implemented as DX, is not a deduction system for deontic logic; instead it is an expert system that provides certain reasoning features adopted from deontic logic.

The application of logic programming for deontic reasoning requires proper treatments of deontic operators. We introduce one-place predicates and a two-place predicate:

oblig(α) (corresponding to O(α))

permit(α) (corresponding to P(α))

forbid(α) (corresponding to F(α))

waive(α) (corresponding to W(α))

commit(α, β) (corresponding to C(α, β))

where $\alpha$ and $\beta$ are terms denoting actions. Note that we do not allow compound terms as arguments of the above predicate symbols. That is, for example, we do not allow an expression $\text{oblig}(\alpha \& \beta \vee \gamma)$ . The definitional relationships between deontic predicates are:

[DR1] oblig(α) = \~waive(α) (from definitions of deontic operators)

[DR2] permit(α) = \~forbid(α) (from definitions of deontic operators).

Further, from axioms and theorems, we have:

[DR3] permit(α) ← oblig(α) (from [DA1])

[DR4] waive(α) ← forbid(α) (from [DT1])

[DR5] oblig(β) ← oblig(α), commit(α, β) (from [DT2])

[DR6] permit(β) ← permit(α), commit(α, β) (from [DT3])

[DR7] forbid(α) ← forbid(β), commit(α, β) (from [DT4])

[DR8] waive(α) ← waive(β), commit(α, β) (from [DT5]).

Given a program $P$ and a query $\leftarrow \phi$ , we define a state:

$$
\sigma_ {0} = <   (\phi), \emptyset >,
$$

where $\varnothing$ is the empty substitution. Let us define possible transformal states of $\sigma_0$ as follows:

$$
\sigma_ {1} ^ {1} = <   (\psi), \emptyset >,
$$

where $\phi = \psi$ from a definitional relationship between deontic predicates (i.e., [DR1] or [DR2]),

$$
\sigma_ {1} ^ {2} = <   (\psi), \emptyset > \text { or } \sigma_ {1} ^ {2} = <   (\psi_ {1}, \psi_ {2}), \emptyset >,
$$

where $\phi \leftarrow \psi$ or $\phi \leftarrow \psi_1, \psi_2$ from a relationship of deontic predicates due to axioms and theorems of deontic logic (i.e., [DR3-8]), or

$$
\sigma_ {1} ^ {3} = <   (\psi_ {1} \theta_ {1}, \psi_ {2} \theta_ {1}, \dots , \psi_ {n} \theta_ {1}), \theta_ {1} >
$$

for every $\psi \leftarrow \psi_1, \psi_2, \ldots, \psi_n \in P$ such that $\phi \theta_1 = \psi \theta_1$ where $\theta_1$ is a substitution:

$$
\theta_ {1} = \{x _ {1} = t _ {1}, x _ {2} = t _ {2}, \dots , x _ {k} = t _ {k} \},
$$

where $x_{1}(i=1,2,\ldots,k)$ are variables in $\phi$ and $\psi$ and $t_{j}$ ( $j=1,2,\ldots,k$ ) are terms in $\phi$ and $\psi$ such that $x_{i}\neq t_{j}$ (for all i and j). Note that matching $\phi$ with $\psi$ by $\theta_{1}$ is called unification [3, 24]. We nondeterministically choose one of the above $\sigma_{1}^{j}$ as the next transformal state. Say that the following is $\sigma_{1}$ :

$$
\sigma_ {1} = <   (\psi_ {1}, \psi_ {2}, \dots , \psi_ {n}), \theta_ {1} >.
$$

We further continue the above state transformation for each of $\psi_{i}(i = 1,2,\ldots ,n)$ , until we obtain:

$$
\sigma_ {m} = <   (), \theta_ {1} \theta_ {2} \dots \theta_ {m} >,
$$

where $\theta_{1}\theta_{2}\ldots\theta_{m}$ is a composition of substitutions (as defined in [3, 24]). Then, $\theta_{1}\theta_{2}\ldots\theta_{m}$ is given as an answer to the query. Generations of $\theta_{m}$ for all nondeterministic choices of state transformations are done via the backtracking techniques [3, 24].

The computing process in this section is obtained by program clause logic programming of selected deontic logic axioms and theorems. It can be summarized as follows: By not allowing compound terms as arguments of deontic operators, we have a first-order reasoning system. By expressing deontic axioms and theorems as program clauses, we made logic programming of deontic features possible.

## 2.3. Toward a Deontic Expert System

An expert system is an interactive computer system [6] that can “help solve complex, real-world problems” using “large bodies of domain knowledge gleaned from human experts” [7, p. 79]. The term “expert system” is frequently used in two senses: (1) as an expert system application (e.g., MYCIN [31]) providing domain-specific knowledge, and (2) as a knowledge engineering system (e.g., EMYCIN [34]) for developing expert system applications of particular subject domains, which we call an expert system shell. An expert system shell provides a language for representing knowledge in the form of a certain data structure and controlling knowledge. The underlying knowledge representation of an expert system may be one of various types, but the production-rule knowledge representation has been widely accepted by many researchers [7].

The IF/THEN construct of a production rule is very similar to that of a program clause of logic programming. The control strategy for production rules, backward chaining, is similar to the resolution of logic programming. However, a principal difference lies in the treatment of negation. One typical characteristic of expert systems is that they provide a “consultation mode” for the purpose of the interaction with users $[6]$ . Therefore, the interpretation of unproved facts is not necessarily in most expert systems. The deontic expert system of this paper treats negation as explicit negation, rather than as negation as failure $[11, 30]$ . Negated information is either given as facts, derived from rules, or asserted from the users via an interactive consultation mode.

The deontic expert system shell developed here, as the name indicates, is to build applications in the domain of deontic worlds. Therefore, it is necessary to provide some closed (or predefined) vocabulary to capture deontic concepts, as well as closed vocabulary to construct IF/THEN rules and open vocabulary to capture entities and concepts in particular subject domains. The vocabulary for deontic concepts includes the notions of obligation, permission, forbearance, and waiver that are introduced and defined as modal operators in deontic logic. However, our principal departure from deontic logic is to regard these notions as predicates. In modal deontic logic, actions to which modal operators are applied are propositions. As in modal deontic logic, the arguments of deontic predicates are actions; however, there we take a somewhat different ontological perspective in regarding actions as logical individuals rather than as propositions.

In brief, the deontic expert system presented here is an interactive rule-based system with deontic reasoning based on general program clause logic programming without the negation as failure rule $[11, 30]$ .

## 3. DX: A Deontic Expert System Shell

WE OPERATIONALIZE THE CONCEPTS OF DEONTIC LOGIC PROGRAMMING and expert system in the form of a rule-based deontic expert system shell, called DX. We mainly describe the syntax and operational mode of DX, together with several examples.

## 3.1. Syntax of DX

The basic syntax of DX is based on the IF/THEN structure common to expert systems. The rule structure $^{3}$ for DX is

<condition> IF <conditions>.

or equivalently,

IF <conditions> THEN <condition>.

Notice that the period at the end of the above expressions is a part of the syntactic structure. Rules may also be unconditional, in which case they are expressed as the predicate condition by itself without the IF/THEN. The conditions may include the connectives AND and OR, where AND has the more immediate binding. When a rule includes OR, it may be decomposed to rules that do not include OR. That is, a rule:

<condition> IF <condition1> OR <condition2>.

is equivalent to rules:

<condition> IF <condition1>.

<condition> IF <condition2>.

A condition may be a simple predicate expression, such as STAFF(X), DEPT-OF(X,Y). In DX, these predicate names are regarded as part of the open vocabulary, introduced as appropriate for the problem domain. Also, there are five primitive deontic conditions that have special interpretations in the system:

OBLIG(<action>)

PERMIT(<action>)

FORBID(<action>)

WAIVE(<action>)

COMMIT(<action>, <action>) .

In addition, a condition may be negated, using the symbol “\~.” In the DX rule interpreter, since negation is treated as explicit negation, if a condition cannot be proven, the interpreter will ask the user whether it is true or false. The action is represented as:

<agent>: <condition>,

read that <agent> brings about <condition>. An <agent> is an expression of term, which is either a constant, variable, or a function. These terms are regarded as part of the open vocabulary as predicates for conditions are. The combined syntax for the DX rules is shown in figure 1.

Note that deontic conditions, such as PERMIT(<action> ), themselves may be qualified as conditions. Thus, this notation allows the recursive expression of deontic predicates. For example,

## PERMIT(X:PERMIT(Y:PERMIT(Z:A)))

is read that “X is permitted to bring about the permission of Y to bring about the permission of Z to bring about the condition A.”

Facts may also be included in the rule base as predicates. The difference between facts and unconditional rules is that facts are ground, for example, predicates without variables. These ground predicates are also regarded as part of the open vocabulary dependent on the problem domain.

```autohotkey
<rule> ::= <condition>
<rule> ::= IF <conditions> THEN <condition>
<rule> ::= <condition> IF <conditions>
<rule> ::= FROM <conditions>
IF <action>
TO <conditions>
<conditions> ::= <condition>
<conditions> ::= <condition> AND <conditions>
<conditions> ::= <condition> OR <conditions>
<condition> ::= <predicate>
<condition> ::= OBLIG( <action > )
<condition> ::= PERMIT( <action > )
<condition> ::= FORBID( <action > )
<condition> ::= WAIVE( <action > )
<condition> ::= COMMIT( <action > , <action > )
<condition> ::= ~ <condition>
<action> ::= <agent> : <condition>
<agent> ::= <term>
```

Figure 1. BNF Syntax for DX Rules

Another type of assertion is sometimes included in the rule base, to specify that certain conditions are mutually exclusive. This enables the system to infer the truth values of certain predicates without having to ask. The format is:

```txt
EXCLUSIVE([<list-of-conditions>]),
```

where

```txt
<list-of-conditions> ::= <condition>
<list-of-conditions> ::= <condition>, <list-of-conditions>.
```

For example,

```txt
EXCLUSIVE([STUDENT(X), STAFF(X), FACULTY(X)]).
```

states that “X is exclusively either a student, a staff member, or a faculty member.”
A comment on the notation: for readability, both predicate constants and variables are written in upper case; variables are just a single letter while predicate constants are longer words. Individual constants begin with a capital letter followed by lower-case letters or digits. For example,

FACULTY(X)

CONTRACT(Smith, Jones).

## 3.2. Implementation of DX

DX consists of two components, interpreter and dialog, and provides data structures for rules and facts as defined in the previous section. The interpreter consists of a knowledge control strategy, which is based on the resolution of deontic logic programming with explicit negation, and a knowledge base modifier that allows the users to update the knowledge base of a DX application.

The dialog of DX provides four types of user commands:

Query—Prove a condition.

Assess—Find the deontic status of a given action.

Update—Change a condition through the performance of an action.

Search—Find courses of action to achieve a specified condition.

Query is a command that invokes the DX knowledge control strategy to prove a given condition. The Assess command finds deontic conditions (obligation, permission, prohibition, and/or waiver) of a given action through the knowledge control strategy. DX conditions are modified by the Update command. The Update command asserts or retracts facts as results of actions. Search is a command that repeatedly applies the knowledge control strategy to find one or more courses of action that can achieve a given goal.

The dialog of DX also provides an interface that asks the users to enter a truth value of an unknown condition. Note that in a procedure of the DX knowledge control, truth values of conditions are explicitly determined by facts, rules, or assertions through the window; thus, no unproved conditions appear in the procedure.

## 3.3. DX Query Procedures

The Query command in DX performs factual deductions much like Prolog. That is, DX extends the standard backward-chaining mechanism of expert systems by allowing variables in expressions. Given a query $\phi$ , the DX query processor maintains a state:

$$
\sigma_ {0} = <   (\phi), \varnothing >,
$$

where $\varnothing$ is an empty substitution. When a rule:

$$
\phi_ {i} \text {   IF   } \psi_ {1} \text {   AND   } \psi_ {2} \text {   AND   } \dots \text {   AND   } \psi_ {n}
$$

is in the rule-base such that

$$
\phi \theta_ {1} = \phi_ {i} \theta_ {1},
$$

where $\theta_{1}$ is a substitution:

$$
\theta_ {1} = \left\{x _ {1} = t _ {1}, x _ {2} = t _ {2}, \dots , x _ {k} = t _ {k} \right\},
$$

where $x_{i}$ ( $i = 1, 2, \ldots, k$ ) are variables in $\phi$ and $\phi_{i}$ and $t_{j} (j = 1, 2, \ldots, k)$ are terms in $\phi$ and $\phi_{i}$ such that $x_{i} \neq t_{j}$ (for all $i$ and $j$ ), the DX query processor transforms $\sigma_{0}$ to:

$$
\sigma_ {1} = <   (\psi_ {1} \theta_ {1}, \psi_ {2} \theta_ {1}, \dots , \psi_ {n} \theta_ {1}), \theta >.
$$

The truth value of an unknown fact is interactively given by the user of DX. Further transformations of states by the DX query processor may result in

$$
\sigma_ {m} = <   (), \theta_ {1} \theta_ {2} \dots \theta_ {m} >,
$$

where $\theta_{1}\theta_{2}\ldots\theta_{m}$ is a composition of substitutions. Then, the DX query processor gives $\theta_{1}\theta_{2}\ldots\theta_{m}$ as an answer. When no such state $\sigma_{m}$ with the empty list of literals is reachable and the rule base contains another rule,

$$
\phi_ {j} \text {   IF   } \pi_ {1} \text {   AND   } \pi_ {2} \text {   AND   } \dots \text {   AND   } \pi_ {n},
$$

where $\phi$ and $\phi_j$ are unifiable—that is:

$$
\phi \tau_ {1} = \phi_ {j} \tau_ {1},
$$

the DX query processor backtracks the state transformation and continues the state transformation. The DX query procedures repeat until no further state transformation results in:

$$
\sigma_ {m} = <   (), \dots >.
$$

In a state:

$$
\sigma_ {l} = <   (\psi_ {1} \Theta , \psi_ {2} \Theta , \dots , \psi_ {n} \Theta), \theta_ {1} \theta_ {2} \dots \theta_ {l} >,
$$

where $\Theta = \theta_{1}\theta_{2}\ldots\theta_{l}$ , if there exists no rule whose consequence is unifiable with $\psi_{1}$ , the DX query processor asks users about its truth value.

As an example problem area, we consider deontic rules relating to the management of the information systems department of a university. Every faculty member in this department teaches computers. This is expressed in the following rule and query (see figure 2).

query: TEACHES-COMPUTER(X)

rule: TEACHES-COMPUTER(X) IF

FACULTY(X) AND

DEPT-OF(X, Information-Systems).

fact: FACULTY(Lee).

fact: DEPT-OF(Lee, Information-Systems).

response: X = Lee

Unlike Prolog, all negation is explicit. For example, we may have a rule that all faculty not on leave are on the payroll:

query:

ON-PAYROLL(X)

rule:

ON-PAYROLL(X) IF

FACULTY(X) AND

\~ON-LEAVE(X).

fact: FACULTY(Lee).

fact: \~ON-LEAVE(Lee).

![](/api/attachments/B853PUM6/fulltext/images/c2db8160fdae97b7542d228c1d1a16783d2b0bef6e8b0b9f8663ac78b51a9cdc.jpg)

(a) DX menu  
![](/api/attachments/B853PUM6/fulltext/images/84f130b9dfcda6e8a8eba8ad0d59cdca47e2c1fc0b8d78c9aada01a060cd5a11.jpg)

(b) The Query option lists templates of all available Query terms

![](/api/attachments/B853PUM6/fulltext/images/d37c7891276d0771b89d64625c2367d005ab027312c6a52f87c824419bc25e1a.jpg)

(c) A specific Query term is generated from the selected template (here, "X" in the template is replaced by a variable X).

![](/api/attachments/B853PUM6/fulltext/images/1eb0ea3a7e6d15df4c1450b64d5da9a1162d481eef0b7854f792b253a2ffe4d6.jpg)  
(d) The output screen

Figure 2. A Sample Query Session

<table><tr><td>fact:</td><td>FACULTY(Elam).</td></tr><tr><td>fact:</td><td>ON-LEAVE(Elam).</td></tr><tr><td>response:</td><td>X = Lee</td></tr></table>

## 3.4. Deontic Deduction

The Assess command is used to determine the deontic status of a specific action, following the computing process for deontic reasoning in section 2.2. When an Assess command of an action, say X:DO-SOMETHING, is given, DX tries to prove OBLIG(X:DO-SOMETHING) OR PERMIT(X:DO-SOMETHING) OR FORBID(X:DO-SOMETHING) OR WAIVE(X:DO-SOMETHING). For example, we will examine a possible set of deontic rules for controlling access to the departmental photocopy machine.

<table><tr><td>assess:</td><td>Lee:USE-COPIER</td></tr><tr><td>rule:</td><td>PERMIT(X:USE-COPIER) IFFACULTY(X).</td></tr><tr><td>fact:</td><td>FACULTY(Lee).</td></tr><tr><td>response:</td><td>PERMIT(Lee:USE-COPIER)</td></tr></table>

Students may use the copier if they are teaching assistants (see figure 3).

<table><tr><td>assess:</td><td>Chen:USE-COPIER</td></tr><tr><td>rule:</td><td>PERMIT(X:USE-COPIER) IF STUDENT(X) AND TEACHING-ASSISTANT(X).</td></tr><tr><td>fact:</td><td>STUDENT(Chen).</td></tr><tr><td>fact:</td><td>TEACHING-ASSISTANT(Chen).</td></tr><tr><td>response:</td><td>PERMIT(Chen:USE-COPIER)</td></tr></table>

Staff may use the copier if they have special copy privileges.

<table><tr><td>assess:</td><td>Fletcher:USE-COPIER</td></tr><tr><td>rule:</td><td>PERMIT(X:USE-COPIER) IFSTAFF(X) ANDCOPY-PRIVILEGE(X).</td></tr><tr><td>fact:</td><td>STAFF(Fletcher).</td></tr><tr><td>fact:</td><td>COPY-PRIVILEGE(Fletcher).</td></tr><tr><td>response:</td><td>PERMIT(Fletcher:USE-COPIER)</td></tr></table>

## 3.5. DX Update Procedures: Changing Deontic Constraints

The Update command in DX changes deontic constraints by performing an action. These changes may be physical, such as a change in location, or they may be changes in nonphysical conditions, such as becoming a student or getting married. We refer to the latter as deontic status conditions. The kinds of conditions appearing in deontic rules are mainly of this type; all previous examples have been of this type. When such (a) The Assess option lists templates of all available Assess terms

![](/api/attachments/B853PUM6/fulltext/images/785308929e1c03954644d4f41ec91a655c6f34d96d2140c6d11ba0b448b8f2e7.jpg)

![](/api/attachments/B853PUM6/fulltext/images/0be2ce4e6be2d2552d1fd955c77eeb0df41e776de584ec79343c2a18868352da.jpg)

(b) A specific Assess term is generated from the selected template (here "X" in the template is replaced by a constant, "Chen").  
![](/api/attachments/B853PUM6/fulltext/images/4cd6054bde0263f7e7a8aa38886497e5b3660fe564bd68e41c37948ee16e353c.jpg)

(c) DX asks the user to enter a truth value of an unknown condition

![](/api/attachments/B853PUM6/fulltext/images/2fdb85137f89ebf05f1798adf03814f4ed28f6cdb9b866f5519c5a8ec3879ffa.jpg)

(d) The output screen

Figure 3. A Sample Assess Session

deontic status conditions change, new types of deontic conclusions apply. Physical conditions may change due to natural causes, such as aging or the weather, or as the result of some human action, such as driving a car. Deontic status conditions, by contrast, are only changed by some human action. In DX, only human actions are considered.

In order to support changing deontic constraints, DX uses the following rule:

rule ::= FROM conditions-1 IF action TO conditions-2.

It means if conditions—1 are satisfied and action is permitted, the performance of action asserts conditions—2. DX uses the Query processor to check if conditions—1 are satisfied and the Access processor to check if action is permitted, and then asserts the conditions—2.

For example, the chairperson may grant copier privileges to staff:

update: Dyer: COPY-PRIVILEGE(Brown)

rule A: PERMIT(X:COPY-PRIVILEGE(Y)) IF CHAIR(X) AND STAFF(Y).

rule B: FROM TRUE

fact: CHAIR(Dyer).

fact: STAFF(Brown).

response: UPDATE ACCEPTED

When the Update command of Dyer:COPY-PRIVILEGE(Brown) is issued, DX first checks if it is permitted. Since Dyer is a chair and Brown is a staff member, Dyer:COPY-PRIVILEGE(Brown) is permitted by rule A. As the result, PERMIT(Brown:USE-COPIER) is asserted by rule B.

assess: Brown:USE-COPIER
response: PERMIT(Brown:USE-COPIER)

Due to the previous Update, the Assess to Brown:USE-COPIER is answered "permitted."

update: Lee:COPY-PRIVILEGE(Quintus)

response: UPDATE REJECTED

However, the Update command of Lee:COPY-PRIVILEGE(Quintus) is denied because its permission is not granted by rule A.

## 3.6. DX Search Procedures: Goal Seeking with Deontic Constraints

When a given condition is not directly permitted by the deontic rules, it may nonetheless be achievable by a certain sequence of deontic actions. The command Search will find these various action sequences. For example, suppose that Quintus, who is on the staff, is not presently permitted to use the copier.

search: PERMIT(Quintus:USE-COPIER)

action: Dyer: COPY-PRIVILEGE(Quintus).

In this case, the system has suggested that the department chair, Dyer, grant Quintus copy privileges. The explanation is as follows (see figure 4):

rule A: PERMIT(X:USE-COPIER) IF

rule B: FROM TRUE

rule C: PERMIT(X:COPY-PRIVILEGE(Y)) IF

fact: STAFF(Quintus).

fact: CHAIR(Dyer).

therefore: PERMIT Dyer: COPY-PRIVILEGE(Quintus)

action: Dyer: COPY-PRIVILEGE(Quintus)

therefore: PERMIT Quintus:USE-COPIER

To achieve the goal seeking with deontic constraints, we adopt a simple search processor. Given a goal by a Search command, the DX Search processor maintains a state:

$$
\sigma_ {0} = <   (\gamma), () >.
$$

If there exists a rule:

$$
\text { FROM } \tau_ {1} \text { AND } \dots \text { AND } \tau_ {n} \text { IF } \alpha_ {1} \text { TO } \gamma_ {1} \text { AND } \dots \text { AND } \gamma_ {k},
$$

where $\gamma \theta_{1} = \gamma_{i}\theta_{1}$ ( $\theta_{1}$ is an substitution) for some $i$ , a new state is obtained as follows:

$$
\sigma_ {1} = <   \left(\tau_ {1} \theta_ {1}, \dots , \tau_ {n} \theta_ {1}, \text { PERMIT } \left(\alpha_ {1} \theta_ {1}\right)\right), \left(\alpha_ {1} \theta_ {1}\right) >.
$$

If $\tau_{1}\theta_{1}$ is given as a fact, the following state is obtained:

$$
\sigma_ {2} = <   \left(\tau_ {2} \theta_ {1}, \dots , \tau_ {n} \theta_ {1}, \text { PERMIT } (\alpha_ {1} \theta_ {1})\right), (\alpha_ {1} \theta_ {1}) >.
$$

Otherwise if there is a rule:

$$
\tau \text {   IF   } \tau_ {1} ^ {1} \text {   AND   } \dots \text {   AND   } \tau_ {1} ^ {m},
$$

where $\tau_{1}\theta_{1} = \tau \theta_{2}$ , then the state is transformed to:

$$
\sigma_ {2} = <   (\tau_ {1} ^ {1} \theta_ {2}, \dots , \tau_ {1} ^ {m} \theta_ {2}, \tau_ {2} \theta_ {1} \theta_ {2}, \dots , \tau_ {n} \theta 1 \theta 2, \mathrm{PERMIT} (\alpha_ {1} \theta_ {1} \theta_ {2})), (\alpha_ {1} \theta_ {1} \theta_ {2}) >.
$$

Otherwise, the DX Search processor finds another rule:

$$
\text { FROM } \cup_ {1} \text { AND } \dots \text { AND } \cup_ {m} \text { IF } \alpha_ {2} \text { TO } \delta_ {1} \text { AND } \dots \text { AND } \delta_ {l},
$$

![](/api/attachments/B853PUM6/fulltext/images/711cd880d440c1a8aca635adcd2aef1b49c514c3e8fe55cf9ac652b9931541a2.jpg)  
Figure 4. A Sample Search Procedure

where $\tau_{1}\theta_{1}\theta_{2} = \delta_{i}\theta_{2}$ for some $i$ , and transforms $\sigma_{i}$ to:

$$
\begin{array}{c} \sigma_ {2} = <   (\upsilon_ {1} \theta_ {2}, \ldots , \upsilon_ {m} \theta \nu 2, \tau_ {2} \theta_ {1} \theta_ {2}, \ldots , \tau_ {n} \theta_ {1} \theta_ {2}, \text { PERMIT } (\alpha_ {1} \theta_ {1} \theta_ {2}), \\ \text { PERMIT } (\alpha_ {2} \theta_ {2})), (\alpha_ {1} \theta_ {1} \theta_ {2}, \alpha_ {2} \theta_ {2}) >. \end{array}
$$

Further transformations of the state and refutations of PERMIT(—) by deontic reasoning in section 2.2 may result in a state:

$$
\sigma = <   (), (\alpha_ {1} \Theta_ {1}, \alpha_ {2} \Theta_ {2}, \dots) >,
$$

where $\Theta_{i}$ (for all i) are compositions of substitutions. Then, the sequence of actions $\alpha_{1}\Theta_{1}, \alpha_{2}\Theta_{2}, \ldots$ is returned as an answer.

## 4. Applications: Performative Networks

AS ILLUSTRATED IN THE PREVIOUS EXAMPLES, TYPICAL APPLICATIONS for the deontic expert system are to represent bureaucratic rules and regulations within organizations. These would be especially beneficial in cases where the rules are complex and/or subject to frequent changes. In such bureaucratic organizations, the deontic expert system would be part of the organization's computer network, thus ensuring that everyone had access to the same rule set.

Deontic expert systems may also be used to model interorganizational activities and other activities in the society at large. Williamson [37, 38] offers a perspective of social organization in terms of governance structures. In this framework, organizations are one type of governance structure, based on the notion of a hierarchy where every individual has just one supervisor. However, for some organizations, where for instance production and marketing concerns compete for priority, a matrix kind of organization may be appropriate. For other types of resource-allocation situations, a market structure may be the more suitable governance structure. For Williamson, this “markets versus hierarchies” trade-off is determined by transaction cost economics: markets have lower transaction costs for standardized types of contracting exchanges, whereas hierarchies have advantages when more specialized cooperation is needed between the parties.

The kinds of governance structures described by Williamson are distinguished by their number and scope: hierarchies consist of a single, monolithic governance structure, whereas markets comprise a large number of relatively small governance structures, that is, the separate contracts. From our perspective, however, what all these governance structures have in common is that they are deontic systems; whether hierarchy or contract, the purpose is to regulate or control the behavior of certain individuals to achieve economic goals.

This suggests that the use of deontic expert systems might also have applications external to the organization, facilitating the contracting process. We refer to these types of applications as “electronic contracting” [20, 21]. Unlike internal applications, where a computer network is often already in place for data-processing applications, electronic contracting applications may require the establishment of a separate, interorganizational network. Such networks are indeed the trend, however, as more and more companies develop electronic data interchange (EDI) applications. $^{4}$ In terms of the kinds of data exchanged and the inferencing employed, EDI is rather like the external counterpart to data-processing applications internally. A potential role of deontic expert systems is to extend EDI to include reasoning about the legal rules and regulations affecting commercial transactions.

A requirement of these applications, whether for bureaucratic rule bases or electronic contracting, is the ability to actually perform actions via the network, a goal made possible because the principal actions of concern are linguistic rather than physical, namely deontic actions. These are what the philosopher Austin [4] called performative communications. In our earlier examples, the conferring of copy privileges and copy discretion were performative.

In electronic contracting, performative communications alter the legal status of the parties by conferring rights, imposing obligations, and prohibiting or waiving certain acts; that is, they change the deontic state of the parties. For example, issuing a letter of credit entitles the named beneficiary to payment upon compliance with the stated terms and conditions. Similarly, issuing a negotiable bill of lading gives the legal holder of the document title to the goods if the document directs that they are to be delivered to the bearer or to the order of a named person.

The combination of these two aspects—performative communications and deontic states—leads to the concept of a performative network: a computer network accessible to individuals, households, companies, and governmental agencies, providing the capability to perform deontic transactions. But what makes the network performative? This is not a technical feature, but rather a policy made about the network's use, what we call a performative assumption. In essence, this assumption is that communications made through the network are legally (deontically) binding. In electronic contracting applications, the network obtains legal force through an umbrella contract, a membership agreement signed by all parties using the network. In bureaucratic applications, the performative assumption may be made as a matter of organizational policy.

An important advantage of performative networks is that the computer can act as a witness to deontic transactions. Assuming that all transactions are logged, performative networks can provide an audit trail of negotiations and contract performance, providing complete and exact evidence in cases of dispute. An even more significant advantage, however, is that performative networks can actually enforce deontic constraints. This was illustrated earlier with the Update command in DX: when the user attempts to make a deontic action for which he or she is not permitted, the system rejects the action. Similarly, a performative network for electronic contracting could prevent users from forming contracts that violate trade regulations.

Using the analog of the Search command in DX, a performative network could also aid users in finding ways to achieve their goals. For example, a performative network serving welfare recipients could help users find all the support services for which they are entitled. Conceivably, such a network could be much more thorough and helpful than the human staff who presently perform such functions, also helping to reduce the high overhead of these organizations.

## 5. Future Directions

THE DX SHELL PROVIDES A BASIC MODEL FOR COMPUTER-ASSISTED DEONTIC REASONING. However, if it is to become useful for practical applications, a few extensions are needed. We present here two directions of extensions: defeasible reasoning and temporal reasoning.

## 5.1. Deontic Dilemmas and Rule Precedence

Deontic dilemmas, or deontic conflicts, are often observed in normative systems and their resolution is important from a practical standpoint [16, p. vii]:

It has often been argued that unlike “natural” necessities, obligations can conflict with one another, and the resolution of such normative conflicts is an important part of moral discourse.

A deontic dilemma arises when two or more deontic rules imply conflicting conclusions for a give situation. A classical example is Kierkegaard's analysis of Abraham's dilemma whether or not to kill his son, Isaac. God had commanded Abraham to kill his son, yet ethical principles said he should not. We distinguish two categories of dilemmas, "mild" and "deadlock." A mild dilemma occurs when deontic rules conflict, but there is still a course of action available that avoids violating either rule. There are two main cases:

## FORBID(X:A) & PERMIT(X:A)

## OBLIG(X:A) & WAIVE(X:A)

In the first case, where the same action is both forbidden and permitted, the party X may abstain from the forbidden action to avoid violation. In the second case, where the same action, A, is both obliged and waived, the party X may do the obliged action to avoid violation.

Deadlock dilemmas are more difficult. In these cases, the individual has no course of action that avoids a violation. The principal pattern of a deadlock dilemma is the following:

$$
\text { OBLIG } (X: A) \& \text { FORBID } (X: A).
$$

That is, an action A is both obliged and forbidden. Or more generally:

$$
\text { OBLIG } (X: A) \& \text { OBLIG } (X: B).
$$

where A and B are mutually exclusive actions, represented in DX with the assertion:

$$
\text { EXCLUSIVE } ([ A, B ]).
$$

Here is an example of a mild dilemma: The university library has a policy that students with outstanding fines may not use copiers on campus.

assess: Chen:USE-COPIER

rule: PERMIT(X:USE-COPIER) IF

STUDENT(X).

rule: FORBID(X:USE-COPIER) IF

STUDENT(X) AND

OUTSTANDING-FINE(X).

fact: STUDENT(Chen).

fact: OUTSTANDING-FINE(Chen).

response:

PERMIT(Chen:USE-COPIER)

FORBID(Chen:USE-COPIER).

Here is an example of a deadlock dilemma: Teaching assistants must make use of the copier to prepare exam materials for class.

assess: Chen:USE-COPIER

rule: OBLIG(X:USE-COPIER) IF

TEACHING-ASSISTANT(X) AND

REQUESTED-COPYING-EXAM(X).

rule: FORBID(X:USE-COPIER) IF

STUDENT(X) AND

OUTSTANDING-FINE(X).

fact: TEACHING-ASSISTANT(Chen).

fact: REQUESTED-COPYING-EXAM(Chen).

response:

OBLIG(Chen:USE-COPIER)

FORBID(Chen:USE-COPIER).

One of the ways to systematically avoid deontic dilemmas is hierarchical reasoning of rules $[1]$ by default or defeasible reasoning $[10, 26, 27]$ . Often we indicate that certain deontic rules apply as defaults; when a more specific situation occurs, defaults are defeated. We are currently developing the DDX shell (i.e., defeasible deontic expert system shell), as an extension to the DX shell. We adopt Nute's specificity-based defeasible reasoning $[27]$ to establish and reason about hierarchies of rules.

## 5.2. Temporal Reasoning

One of the key functions missing in the current implementation of DX is temporal inferencing. This, we believe, has a fundamental role in deontic reasoning. An aspect of temporal inferencing is the marking of transactions (i.e., actions) with the date and time they were performed. Our notations for temporal markings are [22]:

$$
\begin{array}{l} \text {< action > ON <   date > } \\ \text {< action > BY <   date > } \end{array}
$$

The first notation is used to record the time when historical actions were performed. The second is to mark deontic constraints with a deadline by which the action is to be performed. Another aspect of temporal inferencing is the sequencing of events, whether one event precedes another, or whether they occur concurrently. To achieve this, we adopt Petri nets $^{5}$ [28, 29], augmented with the action notation described above.

This is presently being developed as a generalization of the DX shell, called CASE/EDI. As its name suggests, CASE/EDI is designed to be a computer-aided system engineering tool for developing prototype EDI models. A special feature of this system is the use of direct manipulation graphics for the input and display of the Petri nets. CASE/EDI allows graphical modeling of procedures and reasoning about their deontic status during their execution. It also allows the users to retrieve (or generate) procedures (i.e., courses of action) to achieve a certain goal.

## 6. Concluding Remarks

THE DX SHELL, PROPOSED IN THIS PAPER, IS A SYSTEM for computer-assisted deontic reasoning. Its principal characteristics are:

\- DX reasoning is based on program clause logic programming.

\- DX is an interactive system. The DX consultation mode includes a menu of accessible DX commands, through which the users query and update conditions.

\- DX provides deontic deduction capabilities.

In sections 2 and 3, we focused our attention on the syntactic aspect of DX, which includes the procedural/operational model of DX reasoning. The other aspect of logic modeling, not addressed here, is semantics, which includes the specification of the domain of DX, mapping syntactic components to those in the domain, and soundness/completeness issues of DX reasoning. In particular, issues of soundness and completeness are important in that they are a means of justifying the correctness of DX reasoning. We believe DX reasoning is at least sound and complete with some restrictions, because it is founded on standard logic programming in which the resolution is proved to be sound and complete $[3, 24]$ . However, the considerations of soundness and completeness of DX reasoning require further investigations; we will leave these as a future research issue.

In section 5, we proposed two directions for extensions to DX: defeasible reasoning and temporal reasoning extensions. Another research issue to be considered addresses managing the evolution of the rule base. For managing the evolution of the rule base, we would like to model how deontic rules could be used as meta-rules to control how the rule base is modified—for instance, a manager cannot give himself a promotion. Currently DX provides for changes in single conditions only. An extension is to allow for changes, additions, and deletions in the rules too. That is, rather than modifying the rules using an ordinary text editor, all insertions, deletions, and changes would pass through deontic controls. The principal difficulty occurs when different authorities require mutually exclusive actions. Various heuristics, such as the relative power of the two authorities, the recency of the rule, and the preference of the users, may be used to decide which rule should take precedence.

All features of DX presented in this paper have been implemented in Prolog. The implementation in Macintosh® platform (with LPA™ Mac-Prolog 3.0) provides additional features of menu-driven graphical user interface. A sample DX rule base of University of Texas General Library Lending Codes is currently being developed, to demonstrate the applicability of DX.

## NOTES

1. For the proofs of theorems, see [17, 35, 36].

2. See, e.g., [9] or [33]. For a more general treatment of logic and artificial intelligence, see [13]. For a theoretical foundation of logic programming, see [3, 24].

3. Here we use the Backus-Naur Form (BNF) commonly used in computer science for presenting programming language syntax. The angle brackets are nonterminal syntactic constituents. The “::” symbol is for syntactic definitions. All other symbols are terminal symbols in the DX rule syntax.

4. For implementations, functions, trends, and other issues of EDI, see [2, 6, 15, 18, 32].

5. For variations of Petri nets and advanced issues, see [14, 19, 23, 25].

## REFERENCES

1. Alchourrón, C.E., and Makinson, D. Hierarchies of regulations and their logic. In R. Hilpinen (ed.), Deontic Logic: Introductory and Systematic Readings. Dordrecht: D. Reidel, 1981, pp. 125–148.

2. ANSI. An introduction to electronic data interchange. Report No. ASC X12D/87-02, ANSI, July 1987.

3. Apt, K.R. Introduction to logic programming. Report No. TR-87-35, Department of Computer Science, University of Texas at Austin, 1988.

4. Austin, J.L. How to Do Things with Words. Cambridge, MA: Harvard University Press,

1962.

5. Baum, M. EDI law. Working Paper, Independent Monitoring, Cambridge, MA, 1989.

6. Barr, A., and Feigenbaum, E.A., eds. The Handbook of Artificial Intelligence, vol. 1. Reading, MA: Addison-Wesley, 1981.

7. Barr, A., and Feigenbaum, E.A., eds. The Handbook of Artificial Intelligence, vol. 2. Reading, MA: Addison-Wesley, 1982.

9. Bratko, I. Prolog Programming for Artificial Intelligence. Reading, MA: Addison-Wesley, 1986.

10. Causey, R.C. EVID: a system for interactive defeasible reasoning. Decision Support System, 11, 2, (1994), 103–131.

11. Clark, K.L. Negation as failure. In H. Gallaire and J. Minker (eds.), Logic and Data Bases. New York: Plenum, 1978, pp. 293–322.

12. Føllesdal, D., and Hilpinen, R. Deontic logic: an introduction. In H. Hilpinen (ed.), Deontic Logic: Introductory and Systematic Readings. Dordrecht: D. Reidel, 1971, pp. 1–35.

13. Genesereth, M.R., and Nilsson, N.J. Logical Foundations for Artificial Intelligence. Los Altos, CA: Morgan Kaufman, 1987.

14. Genrich, H.J., and Laiutenbach, K. System modelling with high-level Petri nets. Theoretical Computer Science, 13 (1981), 109–136.

15. Harrington, L. Global EDI language may have finally arrived. Traffic Management, 27 (April 1988), 2–17.

16. Hilpinen, R., ed. Deontic Logic: Introductory and Systematic Readings. Dordrecht: D. Reidel, 1971.

17. Hilpinen, R., ed. New Studies in Deontic Logic. Dordrecht: D. Reidel, 1981.

18. ISO. Electronic data interchange for administration, commerce and transport (EDIFACT)—application level syntax rules, 1st ed. ISO 9735, July 1988.

dynamic programming, and branch and bound. In L.N. Kanal and V. Kumar (eds.), Search in Artificial Intelligence. New York: Springer-Verlag, 1988, pp. 35–53.

20. Lee, R.M. International contracting—a formal language approach. In Hawaii International Conference on System Sciences, 1988, pp. 1072–1081.

21. Lee, R.M. A logic model for electronic contracting. Decision Support Systems, 4 (1988), 27–44.

22. Lee, R.M.; Coelho, H.; and Cotta, J.C. Temporal inferencing on administrative databases. Information Systems, 10, 2 (1985), 197–206.

23. Lin, C., and Marinescu, D.C. Reachability trees for high level Petri nets with marking

variables. Report No. CSD-TR-857, Computer Sciences Department, Purdue University, 1985.

24. Lloyd, J.W. Foundations of Logic Programming, 2d ext. ed. New York: Springer-Verlag, 1987.

25. Murata, T. Petri nets: properties, analysis and applications. In Proceedings of the IEEE, 1989, pp. 541–580.

26. Nute, D. A nonmonotonic logic based on conditional logic. Report No. 01-007, Advanced Computational Methods Center, University of Georgia, 1985.

27. Nute, D. General and special defeasible logic. In Proceedings of Tübingen Workshop on Semantic Nets and Nonmonotonic Reasoning, 1989, pp. 114–122.

28. Peterson, J.L. Petri nets. ACM Computing Survey, 9, 3 (1977), 223–252.

29. Peterson, J.L. Petri Net Theory and Modeling of Systems. Englewood Cliffs, NJ: Prentice-Hall, 1981.

30. Reiter, R. On closed world assumption. In H. Gallaire and J. Minker (eds.), Logic and Data Bases. New York: Plenum, 1987, pp. 55–76.

31. Shortliffe, E.H. Computer-Based Medical Consultations: MYCIN. New York: North-Holland, 1979.

32. Sokol, P. EDI: The Competitive Edge. New York: McGraw-Hill/Intertext, 1989.

33. Sterling, L., and Shapiro, E. The Art of Prolog: Advanced Programming Techniques. Cambridge, MA: MIT Press, 1986.

34. Van Melle, W. A domain independent system that aids in constructing consultation programs. Report No. STAN-CS-80-820, Computer Science Department, Stanford University,

1980. Ph.D. dissertation at Computer Science Department, Stanford University.

35. Von Wright, G.H. Deontic logic. Mind, 60, 237 (1951), 1–15.

36. Von Wright, G.H. An essay in deontic logic and the general theory of action. Acta Philosophica Fennica, 21 (1968), 1–55.

37. Williamson, O. Markets and Hierarchies: Analysis and Anti-Trust Implications. New York: Free Press, 1975.

38. Williamson, O. Transaction-cost economics: the governance of contractual relations. Journal of Law and Economics, 22, 2 (1979), 233–262.
