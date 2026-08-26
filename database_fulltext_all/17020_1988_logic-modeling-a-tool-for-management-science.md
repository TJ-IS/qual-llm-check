---
otero_id: 17020
otero_key: "R823CJXB"
title: "Logic modeling: A tool for management science"
authors: "Steven O. Kimbrough; Ronald M. Lee"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90094-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Logic Modeling: A Tool for Management Science $^{1}$

Steven O. KIMBROUGH \*

and Ronald M. LEE \*\*

\* University of Pennsylvania, Department of Decision Sciences/CC, Philadelphia, PA 19104, USA

\*\* University of Texas-Austin, Department of General Business CBA 5.202, Austin, TX 78712, USA

Developments in logic and in information technology (especially the advent of logic programming) have converged to the point at which logic is, for a broad variety of problems, a useful tool to employ for modeling in areas of interest to management scientists. This paper presents the concept of logic modeling (model building with symbolic logic) and reviews several lines of research having in common a logic modeling approach to problems of interest in management scientist.

Keywords: Logic, Logic Programming, Prolog, Logic and Databases, Nonmonotonic Logic.

## 1. Introduction

A primary aim of management science is to develop, study the properties of, and apply formal (or mathematical) models to decision problems. Although a variety of model types have been studied by management scientists, mathematical programming and stochastic models have perhaps been the most popular. Recent developments in information systems technology and in formal logic have provided the basis for logic becoming a valuable modeling tool for problems of interest to management scientists. Consequently, several heretofore independent lines of research can be seen as belonging to a coherent whole, and a new field of research, which we call logic modeling, has begun to emerge. In what follows, we survey this rapidly-developing area of applied research. Our main goals are to make the case that logic modeling can be seen as a coherent and useful subject in management science, and to introduce information systems researchers to the relevant literature. Hence, what follows is intended only as an introduction, not as a definite treatise on the subject.

![](/api/attachments/R823CJXB/fulltext/images/3e7adc5d02c275178242b153a8b281a1ef75d03094067597fc1d3bec99b90e3a.jpg)  
Madison.

Steven O. Kimbrough is Assistant Professor in the Department of Decision Sciences, The Wharton School, University of Pennsylvania. His main research activities are in logic modeling – focusing on belief revision and automatic theorem proving – and in knowledge-based decision support systems. He is principal investigator for the Knowledge-Based Support Systems project with the U.S. Coast Guard. His Ph.D. and M.S. degree are from the University of Wisconsin

![](/api/attachments/R823CJXB/fulltext/images/75d39059e1240213c2d271e79ec8d9f4936a337ffe060f3e748ff35ad2c6b469.jpg)

Ronald M. Lee is presently of the Information Systems Group in the Management Science and Information Systems Department at the University of Texas. Previously, he was a member of the faculty at Washington University, St. Louis, a research scholar at the International Institute of Applied Systems Analysis (IIASA) in Vienna, Austria and visiting professor at the New University of Lisbon, Portugal. He has a doctorate in Decision Sciences from the Wharton School, Univer

## 2. Background

## 2.1. Why Logic?

Logic is aptly described as the study of 'what follows from what'. Less cryptically, a statement, $\phi$ , is said to follow from a (possibly empty) collection of statements, $\Gamma$ , if it is not possible for $\phi$ to be false when all the statements in $\Gamma$ are true. If so, then we say that the argument, 'Γ, therefore $\phi'$ , is valid, and we call $\phi$ the conclusion and $\Gamma$ the premises. And if a valid argument has true premises, we say it is also a sound argument. In this idiom, then, logic can be described as the study of validity. Equivalently, logic can be called the study of consistency, for if (and only if) an argument is valid, the conjunction of the premises and the denial of the conclusion is inconsistent. That is, that the argument, 'Γ, therefore $\phi'$ , is valid amounts to the statement, 'Γ and $-\phi'$ , being a self-contradiction.

What is logic good for and why should we want to use it? The fundamental reason why logic is interesting is due to the fact that we have a need to draw conclusions, to make inferences, to extract information from a body of knowledge (or description of a system). It is just this motivation that lies behind our interest in the models commonly used in management science. A particular model can be seen as a statement describing a particular situation or system. In solving the model or applying an algorithm to it we are in effect making inferences. Logic is concerned with, by its central concepts, a certain group of inferences: those in which truth is preserved. That is, if we infer, say $\phi$ from $\Gamma$ , the inference is truth-preserving if it is never possible for $\phi$ to be false when each statement in $\Gamma$ is true. In short, all and only the valid inferences are the truth-preserving inferences.

Now, logic is interesting not merely because it studies truth-preserving inferences. The main reason is that the study of logic has produced a series of formal languages (called logics, as in propositional logic, predicate logic, modal logic, and so forth). These formal languages have a number of properties that are of interest to modelers. First, many of these languages are well understood from a logical point of view, so that it is often possible to determine by a purely mechanical (hence computable) procedure whether an inference expressed in these languages is indeed valid. To the degree to which this is true it is a remarkable fact. Compare systems modeled algebraically. There simply is no general procedure for solving an arbitrary model or for determining if a particular statement can correctly be concluded. Not so with certain logical languages. In the predicate calculus (aka: predicate logic), given any model expressible in the language (premises) and given any conclusion which validly follows from the model, there is a general, finite, mechanical procedure for showing that the conclusion actually does follow.

This remarkable fact led to the idea of logic programming – the idea that a formal language for a logic could also be used as a programming language. Kowalski, an early advocate of logic programming, expressed the core idea in the title of his seminal paper, ‘Algorithm = Logic + Control’ [Kowalski (1979)]. The idea was further developed in his book, Logic for Problem Solving [Kowalski (1979)].

A second interesting property of the formal languages of logic is that their expressive powers are sufficiently rich to be generally useful. The predicate calculus, which is the core language for Prolog and other implementations of logic programming, was designed as a general-purpose language for describing individual objects, whether they be people, trees, atoms, nations, numbers, or whatever. Although much of the power of Prolog derives from its deviations from predicate logic and although much of the research in logic modeling is concerned with languages that are richer than predicate logic, it remains true that the predicate calculus is a remarkably rich and powerful language. The management science community is only beginning to understand how to exploit it. Recent notable work that applies logic to problems of longstanding concern to management science includes [Hooker (1988), Jeroslow (1988), Widmeyer (1988)].

A third important and interesting property of the languages of logic is that they inherently support declarative or non-procedural representations. We discuss related issues in section 3.

## 2.2. Developments in Information Technology

Symbolic logic is interesting as a general-purpose modeling language. What has made it a practical modeling tool are three related developments in the technology of information systems. First is the implementation of a number of logic programming languages (notably Prolog, but including Parlog, Concurrent Prolog, and GHC [see, e.g., Sterling and Shapiro (1986)]. A logic programming language can be interpreted declaratively – as a collection of axioms; it can be interpreted procedurally – as giving directions for defining a procedure; it can be given a database interpretation, in which the program elements (clauses) are seen as broad generalizations of relational tuples; and it can be given a process interpretation, which sees the elements in a complex goal as a collection of concurrent or parallel processes. This makes logic programming – and Prolog in particular – a very powerful programming idea, as echoed in the following passage from Lloyd (1984, p. 4).

It is clear that logic thus provides a single formalism for apparently diverse parts of computer science. Logic provides us with a general-purpose, problem-solving language, a concurrent language suitable for operating systems and also a foundation for database systems. This range of application together with the simplicity, elegance and unifying effect of logic programming assures it of an important and influential future. Logical inference is about to become the fundamental unit of computation.

And, happily, not only is logic programming an idea of fundamental importance and utility, but there are several Prolog products on the market that are in their third of fourth releases and that have become mature and quite efficient.

The second important technical development has to do with the fact that the move to logic programming dovetails nicely with ongoing research on parallel processing architectures. It turns out that the main algorithms for theorem proving in logic are quite amenable to being handled automatically (i.e., without explicit direction by the programmer) under a parallel processing regime. This leads to the third development, the Japanese Fifth Generation Computing Project. Central to the announced aims of this project are the development of massively parallel computers with a version of Prolog implemented in hardware. Whether or not the Fifth Generation Computing

Project is ultimately successful in bringing products to market, it has surely been influential in stimulating research in logic programming. Prolog machines, in the form of co-processors that perform deducations quickly, have been prototyped in the United States and are expected to be on the market soon. Hogger's statement (1984, p. xi), that 'It is widely expected that symbolic logic will serve as the core programming formalism for the next generation of computer systems', remains controversial, but widely believed.

These developments have not gone unnoticed. Nilsson (e.g., 1981) and Geneserth and Nilsson (1987) in the artificial intelligence community and Bonczek, Holsapple and Whinston (e.g., 1981) and Chen (1984) and Chen and Henschen (1985) in the management science community have explicitly called for knowledge based systems and decision support systems to be conceptually founded on logic.

## 2.3. Developments in Logic

First order predicate logic, the language taught in introductory courses on logic, is the fundamental logical modeling language. Predicate logic is by now well understood. Its expressive power, while quite strong, has limitations. In response to these there has been a great deal of work by philosophers and mathematicians in developing extensions of predicate logic, which have greater expressive power and are hence better able to model certain systems. Extensions include modal logic (the logic of necessity and possibility) and deontic logic (the logic of obligation and permission, often treated as a branch of modal logic), among others. Turner (1985) is good as an introductory treatment of these various logics, many of which have matured to the point to which they can be used in practical applications. The volumes edited by Gabbay and Guenther (1983, 1984, 1986) provide a more thorough going review of the subject. The appendix presents an elementary introduction to modal logic and briefly discusses other extensions to standard logic.

## 3. Representational Aspects

## 3.1. Qualitative vs Quantitative Modeling

Management science has developed primarily as a form of applied mathematics; that is, it relies mainly on numeric representations and arithmetic forms of inferencing. Thus, it tends to emphasize problems whose principal attributes are scalable, e.g., as on a ratio, interval or ordinal scale. The inferencing done is largely on the magnitude of a given set of attributes.

Logic, by contrast, supports in a natural manner inferencing on the qualitative aspects of a problem. That is, it supports reasoning about features that cannot (easily) be modeled numerically. Because logic may also be used for quantitative modeling, one could regard logic modeling as encompassing quantitative modelling as a special case. In these special cases, however, arithmetic inferencing procedures are available that are highly efficient. As a small example, consider the following two Prolog programs for reasoning about the relative hardness of materials, using a Mohs scale:

```prolog
/* program1 - qualitative reasoning */
harder(diamond, quartz).
harder(quartz, feldspar).
harder(feldspar, gypsum).
harder_than1(X, Y) :-
    harder(X, Y).
harder_than1(X, Z) :-
    harder(X, Y),
    harder_than1(Y, Z).

/* program2 - quantitative reasoning */
hardness(diamond, 10).
hardness(quartz, 7).
hardness(feldspar, 6).
hardness(gypsum, 3).
harder_than2(X, Y) :-
    hardness(X, H),
    hardness(Y, N),
    H > N.
```

In program1, an ordering of relative hardness is given by the binary relation, 'harder', while the predicate harder\_than1 is a transitive form, given by a recursive definition. In program2, the ordering of relative hardness is produced indirectly by mapping to an ordinal scale of integers. The transitivity of hardness can then be deduced arithmetically using the > predicate on the integers.

The two programs give the same results, e.g.,

```python
?- harder _ than1(diamond, X).
    X = quartz
    X = feldspar
    X = gypsum
?- harder _ than2(diamond, X).
    X = quartz
    X = feldspar
    X = gypsum
```

The second program is more efficient since it infers transitivity through the built-in > predicate rather than through recursive search. Such numeric methods, however, are only available for certain kinds of problems, i.e., for those in which a scaling or total ordering on attribute values is available [Roberts (1979)]. For weaker classes of orders, e.g., various forms of partial orders, non-numeric methods such as logic programming must be used. The paper by Widmeyer and Lee (1986) discusses these issues with respect to preference orderings, providing methods for computing non-dominated sets of alternatives in cases where preferences are only partially specified. More broadly, proper modeling of qualitative reasoning is regarded in much of the artificial intelligence literature as essential for further progress in knowledge based systems (see, e.g., the papers in Bobrow (1985)).

## 3.2. Declarative vs Procedural Representation

Every mechanical form of inferencing relies on an algorithm. The declarative/procedural distinction pertains to the extent to which this algorithm is domain dependent. An example of a highly procedural representation is a typical data processing program. The representation of the problem, and the procedure for solving it, are closely intertwined. A spreadsheet package is an example of a (more) declarative representation: one declares the structure of the problem, but not the sequence of steps for solving it. The solution procedure is built-in.

Along this dimension from declarative to procedural, logic is a paradigm example of a declarative representation. (Current Prolog implementations make various procedural compromises, e.g., the Prolog 'cut'.) Unlike non-procedural application packages and spreadsheets, which are declarative but limited to a certain class of problems, logic and logic programming are much broader in scope, potentially including the full range of problems considered by information systems.

One of the principal advantages of declarative representations is their modularity. The argument for modularity in software design is that it yields the ability to develop or modify one module without having to consider the impact on other parts of the program. The effects are limited to the arguments in the subroutine call. The advantages of structured programming are also of this type. By disciplining the control structure of the program to a hierarchical sequence of calls, one limits the possibility of unforeseen side-effects in making a modification.

Logic programming may be regarded as an extension of this trend – taking modularity down to the level of individual statements (predicate definitions). Just as the sequence of subroutines in a Fortran program is immaterial, so too is the sequence of predicate definitions in a pure logic program. As an extreme form of modularity, the possibility of unexpected side-effects is greatly reduced.

Logic programming, like structured programming, enforces a strict discipline on programming style, often thereby requiring greater modeling skill than with conventional languages. Experienced Lisp programmers often criticize Prolog on this score, arguing that Lisp allows them more freedom to develop their own programming style. In business applications, by contrast, idiosyncratic styles of programming are a curse, aggravating the difficulties of software maintenance. Further, the notation of logic – and so to an extent of logic programming – is one especially developed over centuries for its expressiveness and perspicuity. Its role in philosophy developed as a tool for clarifying arguments, to make clear the essential aspects of a debate, and to reduce deduction to a finite number of verifiable, mechanical operations. Are these not also desirable features for software specification and development?

The other major objection for declarative representations generally, and logic programming in particular, is with regard to computational efficiency. Because the solution procedure is domain independent, it is not capable of exploiting special problem structure. Thus, for deterministic problems, it may waste a great deal of time exploring irrelevant alternatives. For this reason, current Prologs include a 'cut' operator, to curtail the search in such cases. Other techniques, e.g. tail recursion optimization, and special indexing of predicates, also help to improve efficiency. Unhappily, they also tend to obscure the program, detracting from its clarity of specification.

Many of these efficiency problems may eventually be resolved through intelligent backtracking schemes, improved Prolog compilers, and parallel architecture machines. Nonetheless, even with such improvements, it is likely that many larger scale problems will be combinatorially too complex to run without some special purpose heuristics. The value of logic programming in these cases will then be more at the level of providing executable specifications of the target system, which is then successively refined with special purpose techniques to make it suitably efficient. An appropriate methodology for such successive refinement remains as an open research issue.

## 4. Logic Modelling: Applications

However interesting logic is and however powerful logic programming languages are as general-purpose tools, what is most interesting and most significant are the applications of logic modeling that are facilitated by taking a logical point of view. Our purpose in this section is to discuss, in an introductory fashion, six application areas in which modeling with logic has proven useful and appears to be especially promising.

## 4.1. Database Inferencing and Alerting

The major use of databases has been in data processing applications; hence mainly for structured, operational level activities such as sales order processing, billing and inventory control. These applications are characterized by high volumes of routine transactions. Performance criteria are mainly speed and efficiency. Databases might also be useful in less structured, longer range activities, though the requirements in this case are somewhat different:

\- Information is usually required in more summarized form.

\- Access is less routine: information must be retrievable in a variety of forms and combinations.

\- The information is often used in combination with other informational and computational resources.

These are criteria for using databases in decision support applications [Lee (1985)]. The primary point is that the data needs in these cases, though contained in the database, will often not be at the detail level, nor in the structural arrangement, in which the database was designed. It is for these uses that a mechanism providing inferencing on the database is needed.

Database management models typically distinguish between the structure and the contents of the database. In logic programming this distinction is not made. In database management, the structure/content distinction gives rise to the view of databases as repositories, somewhat akin to physical inventories. A database query specifies retrieval conditions, and the database contents that match these conditions are delivered to the user. In logic programming, queries are processed not simply by matching character strings, but rather by logical inference.

The link between relational databases and logic programming is made by recognizing that, logically, a relation is the extension of a predicate. That is, a relational $P(x_{1},\ldots,x_{k})$ consists of all the n-tuples, $\langle x_{1},\ldots,x_{k}\rangle$ , that satisfy the predicate, P. This fact is currently stimulating a great deal of interest in combining the inferential capabilities of logic programming with the large scale storage and retrieval capabilities of database management [Gallaire and Minker (1978) Gallaire, Minker and Nicholas (1980), Dahl (1984), Henschen (1984), Kershberg (1986)].

Another area where logic programming may impact on database inferencing is with regard to time modeling in databases. A current survey by McKenzie (1986) indicates a rapidly growing interest in these topics. Lee, Coelho and Cotta (1985), offer a logic-based proposal oriented to administrative databases. Kowalski and Sergot (1985) present a related but extended formalism for temporal reasoning, also based on logic programming.

Finally, interaction between logic and databases may be found in studies of database semantics and conceptual data modeling. The ISO report on 'Concepts and Terminology for the

Conceptual Schema and the Information Base' [van Griethuysen (1984)], contains major sections pertaining to uses of predicate logic for conceptual data modeling. Also, the recently formed IFIP Working Group (2.6) on Database Semantics indicates a strong influence from logic representations. See, for instance, Steel and Meersman (1985).

## 4.2. Logic for Model Management

The concept of model management is by now familiar to the management science and decision support systems community. Model management is treated in standard DSS texts [e.g., Sprague and Carlson (1982), Bonczek et al. (1981)], in recent monographs [e.g., Palmer et al. (1984)], and in research journals [e.g., special issue of Decision Support Systems, Elam and Lee (1986)]. Model management, from the point of view of predicate logic, treats models, inputs, and outputs as objects with properties in much the way we ordinarily treat, e.g. tables and chairs as objects with properties such as color, hardness, and so on. By describing a model with a series of properties, a logic model of the (application or object) model may be constructed and used for managing the application model.

There are many promising applications of logic to model management, including symbolic differentiation, in which the rules of differentiation may be declared in predicate logic, working over a domain of models. Similarly, equation solving has a natural interpretation both in logic and in Prolog [Silver (1986), Sterling and Shapiro (1986)]. Model generation, based on logic and implemented in Prolog, has been studied in a preliminary fashion by Liang (1985). Under this approach, a logical description of each of the models in a model base is declared, including a description of their inputs and outputs. Added to these is a model generation predicate (defined recursively), which states that a given parameter value (e.g., sales in 1990) is available if either (a) it is present in the database, or (b) it is an output of a model in the model base, the inputs of which model are available. This simple predicate, which is easily interpreted in first order predicate logic and which is easily represented in Prolog, permits the generation of rather complex models out of data and models. Many details, both technical and philosophical, remain to be worked out. Nonetheless, a logic modeling approach to model management appears to hold much promise.

```prolog
?- op(400, xf, diagnosed).
?- op(400, xf, observed).
?- op(450, xfy, and).
?- op(500, xfx, if).
?- op(600, fx, show).
```

A related area in model management is the problem of understanding how to manage particular types of models. What, for example, is there different about managing a discrete event simulation model from managing an econometric model? On the problem of managing a logic model, Kimbrough (1986) proposes to treat logic models as abstract data types, discusses several operations that would need to be performed on them for the purpose of model management, and presents a graph-based representation for logic models that facilitates performance of the management operations.

## 4.3. Rule-Based Advisory Systems

Recently there has been a great deal of excitement about expert systems, which often use a rule-based, IF/THEN, format. As in other uses of logic modeling, key features of these systems are

(1) They use declarative rules for expressing knowledge about the problem domain.

(2) They include reasoning about qualitative as well as quantitative information.

In a recent survey of expert system shell languages, O'Keefe (1986) describes them as 'the spreadsheets of artificial intelligence'. He argues that just as spreadsheets offer a familiar and natural representational format, so too, the rule-based representation seems to be a natural (and declarative) way of expressing qualitative concepts. In addition, the syntax of the rules is presented in a pseudo-English style that is easily understandable by the user.

While these shell languages are useful for initial, exploratory applications, they are often found to be insufficiently adaptive for more sophisticated applications. One approach is to customize one's own rule-based language. Prolog seems to be especially well suited for this. Most Prologs, for instance, offer a means of extending the logic syntax into a more English-like form, using operator definitions. Basically, these allow one to modify the syntax of particular predicates to be infix, prefix, or postfix. For example, 'likes (john, mary)' could be expressed as 'john likes mary' by defining 'likes' to have an infix syntax.

Another extension that Prolog provides to conventional logic is the ability to program at a meta-language level, i.e., to operate on predicate assertions themselves as data. These features of operator syntax and metalanguage programming can be combined to develop a rule-based syntax customized to a particular problem domain. For instance, we might have rules of the form: 'cold diagnosed if sniffles observed and fever observed'. A Prolog interpreter for rules such as this is as follows:

/\* operator definitions \*/

/\* interpreter \*/

show P :- clause(P, true).
show P and Q :- show P, show Q.
show P :- P if Q, show Q.

/\* sample rule \*/

cold diagnosed if sniffles observed and fever observed.

/\* sample database \*/

fever observed.

/\* query \*/

?- show X diagnosed.

$\mathbf{X} = \mathbf{c}\mathbf{o}\mathbf{l}\mathbf{d}$

The above example, while trivial in size, is nonetheless a complete rule-based interpreter. The op statements indicate the priority of bindings and syntax of the rule language. The predicate, show, is the rule interpreter. Its three clauses, respectively, recognize elementary facts, conjunctions, and implications. Further techniques for building customized rule-based systems using Prolog are discussed in Lee and Chu (1986).

## 4.4. Symbolization of Text

It is difficult to imagine how the standard modeling techniques of management science can be used effectively to capture the content of textual data, e.g., reports, articles, laws, plans, regulations, and so on. Yet, very much of management revolves around reasoning about the contents of various documents. Symbolic logic, combined with a logic programming implementation, bids fair to be a successful modeling tool for texts and the statements they contain. Besides the two application areas discussed below, there is ongoing work experimenting with symbolization of requests for proposals as an aid to requirements tracking and project management [Scott (1988)], and with symbolization of policy documents, such as annual reports and white papers, as an aid to policy and plan formation.

## 4.4.1. Modeling Rules and Regulations

Taking a broad view, organizations may be characterized by the degree to which they are rationalized, i.e., the degree to which their operations and decision making are institutionalized in the form of prescribed rules and procedures. Such highly rationalized organizations are called bureaucracies. These may be private corporations as well as government agencies and regulatory bodies.

A principal problem with bureaucracies is that they reach a level of complexity where their operations become sluggish and overly consuming of resources. Nearly everyone has experienced the frustration of bureaucratic red tape. A related problem is that the system of rules and regulations reaches a level of complexity that it becomes inflexible and difficult to modify.

As highly rationalized organizations, bureaucracies would seem to be natural candidates for computerization. While this has indeed taken place on a large scale, offering increased speed and efficiency, many aspects of bureaucracies continue to be performed manually, with complicated forms, signatures from multiple parties, and so on. Generally, this has to do with aspects of the operation that are nearly rationalized, but still require some amount of human discretion [Lee (1985)].

There have been a variety of efforts to analyze bureaucratic decision processes, developing computerized modeling techniques to support them. A significant amount of this work relates to legal systems (see Cook et al. (1981) for a survey). There is a long-standing project focusing on both legal and bureaucratic systems, called the LEGOL project, at the London School of Economics [Stamper (1978), Stamper (1985)]. An important aspect of this project is modeling not only stable operations of bureaucratic systems, but also the mechanisms by which the requirements for such systems are developed and how they may change. Given the complexity of such systems, it is important that they be represented in as succinct and rigorous a fashion as possible. Sergot (1985) argues for the utility of logic programming in this respect, and a demonstration in discussed in Sergot et al. (1986), by representing the British Nationality Act as a logic program.

A fruitful direction for development in modeling bureaucratic systems may be in the application of deontic logics, which contain modal operators for obligation, permission, and prohibition (see Hilpinen (1971/81) for a survey). The potential here is to support mechanical reasoning about bureaucratic processes that are only partly rationalized, with points of human discretion explicitly recognized in the logic.

## 4.4.2. Electronic Contracting Applications

A related area in which deontic logic, as well as speech act theory and illocutionary logic, may prove useful is in the formal representation of contracts. The CANDID project of Lee (1980, 1981), gives an abstract formalization of contracting relationships using predicate logic plus deontic operators. The formalization has been implemented in Prolog. Potential application of this work is to electronic support for contracting negotiations, where legal procedures and regulations are managed through an intelligent telecommunications network. Lee's work is extended in Lee (1988).

Another class of applications in this area relates to organized markets specialized for particular intraorganizational messages or for particular commodities [Malone et al. (1987), Lee and Widmeyer (1986)].

## 4.4.3. Formalized Communication Models

The so-called performative utterances are expressions that by their very utterance (in the right circumstances) bring about the fact they describe. Examples include: 'You're out!' (by an umpire), 'I pronounce you man and wife' (by a judge), 'I promise to meet you for lunch'. Several authors, writing to a management science audience, have been intrigued by the role of performative expressions in commerce [Flores and Ludlow (1981), Kimbrough, Lee and Ness (1984), Lyytinen and Lehtinen (1984a), Lyytinen and Lehtinen (1984b)], and have noted the pervasiveness of such utterances (written or spoken) in business communications. These authors have also generally been intrigued with speech act theory (from philosophy and linguistics), which views performatives as but one of several basic types of utterance.

Recent work in philosophical logic (mainly by Searle and Vanderveken) has aimed at developing a formal logic for utterances generally, including performative utterances. The logic is called illocutionary logic. Kimbrough and Lee (1986) have argued that illocutionary logic (although not necessarily the logic of Searle and Vanderveken) can be made to serve as a formal language for business communications, such that expressions in the language are interpretable both by machines and by people. In their paper they begin to explore how such a formal language might be implemented in Prolog and how it might be used for electronic shopping and electronic contracting. Lyytinen and his colleagues have explored the use of illocutionary logic for systems analysis [Lyytinen (1984), Lyytinen and Lehtinen (1984a, 19854b), SAMPO (1986)].

## 4.5. Negotiation Models: Evaluation of Arguments

There is a small, but intriguing, literature in the management science tradition, which is concerned with the formal evaluation of arguments, or reasons, and which aims at analyzing debates among interest groups. Both Mitroff, Mason, and Barabba (1982) and Vari et al. (1985) have analyzed in detail arguments for and against certain public policy questions. Interestingly, both papers draw heavily on the approach to the study of argumentation developed by the philosopher Stephen Toulmin (1958), and both employ formal logic as a tool in their analyses. Both papers claim that significant clarification can be obtained by these analyses. We believe that analysis of arguments outside of the public policy arena, e.g., in strategic planning, is a promising avenue for research. We note that the approach, to analyzing arguments, of reducing source text to a highly structured, even formal, format has long been employed by scholars. A notable example is by Wolff (1963), who does this to Kant's transcendental deduction (from the Critique of Pure Reason, one of the most difficult works in the history of philosophy). Whether applied to philosophy, government, or commerce, any approach in this area will rely upon some form of logic modeling.

## 4.6. Management of Change: Nonmonotonic Reasoning

A central problem for information systems is the management of change. An enterprise, to survive, must be able to adapt quickly to meet new competitive challenges and to exploit new market opportunities. If the information system technology is not similarly adaptive, it becomes as much a hindrance as a help [Lee (1983)].

One way to help cope with this problem is to move software design more in the direction of declarative languages. As noted earlier, declarative forms increase modularity, hence modifiability, by reducing the amount of procedural dependence within the code. On the other hand, there is a cost in terms of computational efficiency. With computation costs continuing to decrease dramatically, and with the costs of development personnel continuing to rise, the tradeoffs look increasingly attractive.

The current interest in fourth generation application packages in the software industry is an example of these trends. The packages offer a non-procedural specification for a particular application area. Often, however, they need to be supplemented with procedural code to accommodate aspects not supported by the package. Logic programming might be characterized as a fifth generation extension to this trend, by providing declarative representations with greater flexibility.

But the problem of change is not solved by declarative representations alone. One must also manage the logical consistency of such changes. Consider the case of database management. These systems are built to manage certain types of changes, i.e., updates to the database. In some cases, they can also accommodate certain types of modifications to the database schema, e.g., adding a new relation. But other types of changes, which would alter the logical consistency of existing relations, require a re-structuring of the database, which can be quite expensive. These are known as non-monotonic changes.

The term nonmonotonic reasoning comes from the artificial intelligence community and refers to two phenomena. The first is that of drawing conclusions that strictly speaking go beyond the evidence (often referred to as default reasoning in artificial intelligence and, in philosophy, defeasible reasoning or inductive, ampliative, or non-demonstrative inference). The second is that of revising beliefs based on new information and has been approached in basically two ways, as part of the default (or defeasible) reasoning problem and as a process for truth maintenance systems to support [de Kleer (1986a, b, c)].

It is widely accepted that standard, ‘monotonic’ logics cannot model these everyday processes and as a result a large literature has been spawned, seeking to address the problem, usually either by developing a new sort of logic [e.g., McDermott and Doyle (1980), Reiter (1980), McCarthy (1980), Geneserth and Nilsson (1987), Nute (1988), Belzer and Loewer (1988)] or by proposing a defense of sorts for standard logic [e.g., Kowalski (1979), Kimbrough and Adams (1988)]. The problem, of modeling belief revision, is a crucial and fundamental one. It is also one that has engendered much discussion and much controversy. However consensus is achieved, the result will be a logic or logic-like approach to the modeling of belief revision and evolving knowledge-based systems.

## 5. Concluding Remarks

Our purpose has been to examine various lines of research that take a logic modeling approach to problems of interest to management scientists. Developments in logic and logic programming have converged to the point at which logic is, for a broad variety of problems, a useful modeling tool. In none of the application areas that we have discussed can it be said that the logic modeling approach is mature. Much remains to be learned, but we believe the basic approach, of modeling with logic, will likely offer exciting opportunities.

## Appendix

The purpose of this appendix is to introduce the management science reader to extensions of standard propositional and predicate logic. We shall focus on modal logic because it is itself interesting, useful, and well-developed, because a variant of it is the basis for deontic logic, and (most importantly) it illustrates how extensions may be added in a rigorous fashion to an existing logic. Our treatment is brief and very introductory. Much deeper introductions can be found in [Hughes and Cresswell (1968), Hughes and Cresswell (1984), Gabbay and Guenther (1983, 1984, 1986)] and many other places. Our main goal here is to give the interested reader a feel of what modal logic, and other extensions of standard logic, are about.

To illustrate the idea of an extension of standard logic we shall now briefly present a system of propositional logic, the simplest variety of formal logic. Following this, we shall present and discuss several systems of modal logic. Our presentations here are necessarily much abbreviated and will focus on a proof theoretic (axiomatic) view of modal logic, rather than a model theoretic view.

Consider first a system of propositional logic, called $PM$ . $^{2}$ In propositional logic, the smallest unit of analysis is a complete sentence. $^{3}$ We shall use the letters $P$ , $Q$ , $R$ (possibly with subscripts) to represent sentences. Our logical constants, or connectors, are ‘ $\neg$ ’ (not...), ‘ $\vee$ ’ (...or...), ‘ $\wedge$ ’ (...and...), ‘ $\supset$ ’ (if...then...), and ‘ $\equiv$ ’ (...if and only if...). The system $PM$ has four axioms ( $A_i$ ) and two rules of inference ( $RI_j$ ), as follows:

$$
A _ {1} \quad (P \vee P) \supset P
$$

$$
A _ {2} \quad P \supset (Q \vee P)
$$

$$
A _ {3} (P \vee Q) \supset (Q \vee P)
$$

$$
A _ {4} \quad (P \supset Q) \supset ((R \vee P) \supset (R \vee Q))
$$

$RI_{1}$ (uniform substitution) If $\phi$ is a thesis and $\theta$ is obtained from $\phi$ by uniformly substituting any well formed formula, $\alpha$ , for any sentence variable, $\beta$ , in $\phi$ , then $\theta$ is a thesis as well.

(PM)

$RI_{2}$ (modus ponens - detachment) If $\phi$ is a thesis and if $(\phi \supset \theta)$ is a thesis, then $\theta$ is a thesis as well. Equivalently, if $\Gamma\vdash\phi$ and $\Gamma\vdash(\phi\supset\theta)$ , then $\Gamma\vdash\theta$ , for all collections of statements, $\Gamma$ .

The system $PM$ is a full system of sentence logic. It uses, as we have seen, five logical connectors, which take one or more sentences as input and produce a sentence as output. Thus, logical connectors may be thought of as functions that map from one or more sentences to another sentence. In extending $PM$ , we shall introduce a new logical connector, along with axioms and rules of inference. Our new connector is ‘ $\square$ ’ and its intend interpretation is ‘It is necessary that…’. Thus, $\square P$ is to be read as ‘It is necessary that $P$ ’. We may define a connector for possibility, ‘ $\diamond$ ’ as follows: $\diamond \phi \equiv_{\text{df}} \neg \square \neg \phi$ . Intuitively, something is possible if and only if it is not necessarily false. Modal logic is said to be the logic of possibility and necessity and the characteristic modal connectors (or operators) are $\diamond$ and $\square$ .

The five connectors used in $PM$ are said to be truth-functional connectors because the truth value of the resulting formula can be uniquely determined given the truth values of the input formulae. For example, if $\phi$ is false, then $\neg\phi$ is true and if both $\phi$ and $\psi$ are true, then $\phi \wedge \psi$ is also true. Modal operators are not, however, truth-functional. If $\phi$ if false, then surely $\Box\phi$ is false as well, but the truth value of $\Box\phi$ is simply undetermined given only that $\phi$ is true. Not everything that is true must be true. Indeed, since it would be possible to define any other truth-functional connective in terms of the existing $PM$ connectives, any genuinely new operator in an extension of $PM$ must fail to be truth-functional.

Merely defining modal connectors does not produce a modal logic. Axioms and rules of inference must be supplied as well. There are many ways to do this and in fact dozens of modal logics have been proposed. For present purposes, we shall confine ourselves to a few of what are called normal modal logics [cf., Hughes and Cresswell (1984, pp. 1–15)]. Thinking in terms of PM, all normal modal (propositional) logics contain at least two things in addition to the axioms and rules of inference of PM. First, normal systems contain a third rule of inference

$RI_{3}$ (rule of necessitation) If $\phi$ is a thesis, then $\Box\phi$ is a thesis as well. Equivalently, if $\Gamma\vdash\phi$ , then $\Gamma\vdash\Box\phi$ .

It is important to understand that the rule of necessitation is not equivalent to $\phi \supset \square \phi$ , nor does it make that formula a thesis. Recalling our definition of the possibility operator, the rule of necessitation is in effect saying that if a statement follows logically from a collection of axioms, then it is not possible for that statement to be false; that should not be controversial.

The second thing inherent in all normal systems of modal logic is the axiom

$$
A _ {5} \square (P \supset Q) \supset (\square P \supset \square Q),
$$

which is also known as the K axiom (after Saul Kripke). Now, the system of logic consisting of PM augmented by $A_{5}$ and $RI_{3}$ is a complete modal logic and is known in the literature as the system K.

K is a comparatively austere system of modal logic. While there is much uncertainly about which systems of modal logic are proper for which uses, K is an unlikely candidate for any of the popularly-envisioned applications of modal logic. Stronger systems are needed. We shall discuss three of the most studied and used systems.

System T (also known as M) consists of K plus an additional axiom

$$
A _ {6} \square P \supset P.
$$

For many intended interpretations of necessity it would seem intuitively correct that if any formula, $\phi$ , must be true, then it is true, Surprisingly, this cannot be proved in $K$ alone. Although $A_6$ is an axiom with much appeal, we note that for deontic systems it may be an undesirable axiom. In a deontic logic, the correlatives of necessity and possibility are obligation and permission. But surely $P$ should not follow from the fact that $P$ is obligatory. Logic should not make it impossible to do wrong, conscience or good sense should. Thus, in a deontic system one might postulate that $\square P \supset \diamond P$ . This is a formal expression of the idea that ought implies can, i.e., that one is obligated to do only what one is able to do.

Two further extensions of K will complete our present discussion of modal systems. The system S4 is obtained by adding to T the axiom

$$
A _ {7} \square P \supset \square \square P,
$$

which says that if P is necessary, then P is necessarily necessary. Expressions with multiple modal operators, such as $A_{7}$ , are said to have iterated modalities and are difficult to interpret intuitively. In this regard, system S5 is uniquely interesting. S5 consists of T plus the axiom

$$
A _ {8} \diamondsuit \square P \supset \square P.
$$

from which $A_{7}$ may be derived. Thus, in sum, S5 contains (every thesis of) S4, which contains T, which contains K. What makes S5 unique among modal systems is that every sequence of iterated modal operators can, with logical equivalence, be replaced by the rightmost operator. From a modeling and computational point of view, this is a tremendous advantage and it is likely a main reason for the popularity of S5 in artificial intelligence [cf., Genesereth and Nilsson (1987)]. Whether or not S5 is a good modal system for a particular modeling problem is, however, a completely different matter.

We come, then, to the problem of determining which modal system is appropriate or correct. There is quite surely no single, correct modal system. S5, for example, is widely thought to be right for representing the concept of logical necessity. But those who believe in other sorts of necessities think them to be structurally different from logical necessity. We have already seen an example in which S5 is probably not a good modal system: Modeling of deontic concepts (including moral obligation, legal obligation, social obligation, and so forth). Our quarrel was with $A_{6}$ , which is a thesis of S5. Many in artificial intelligence [e.g., Genesereth and Nilsson (1987)] think that S5 is a good system for modeling epistemic concepts and would interpret □P as (roughly) 'It is known that P'. If we accept S5 as a language for modeling knowledge and if we interpret the necessity operator this way, then it will follow for each case of someone's knowing that P that that person knows that he knows that P. The reason for this is that □P ⊃ □□P is a thesis in S5 (and S4). Among philosophers, this is known as the KK principle (to know, you have to know that you know). Although there are advocates of the KK principle and it has been defended from time to time, many if not most epistemologists would dispute it. Our point here is that, in choosing a modal logic (or indeed any logic at all) for modeling in some domain, certain assumptions are made. These assumptions may not be obvious; they are consequential.

In sum, the problem of choosing a modal, or other, logic for model building is a subtle and delicate matter, whether the envisioned interpretation of the modal operator is that the input formula is logically necessary, causally necessary, legally obligatory, morally obligatory, required for business reasons, true at and after the present time, unpreventable, required by a specified set of rules, or whatever. The logic modeler has a large number of systems from which to choose and few universally agreed upon principles for guidance. If this presents daunting prospects, it also offers highly exciting and researchable prospects.

## References

Belzer, M. and B. Loewer, A Conditional Logic for Defeasible Beliefs, Decision Support Systems 4, no. 1 (1988).

Bharath, R., Logic Programming: A Tool for MS/OR? Interfaces 16 (Sept.-Oct. 1986) 80–91.

Bobrow, Daniel G., ed., Qualitative Reasoning about Physical Systems (MIT Press, Cambridge, MA, 1985).

Bonczek, R.H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981).

Chen, Michael Chien-Kuo, On the Use and Internal Structure of Logic-Based Decision Support Systems, unpublished Ph.D. thesis (Northwestern University, 1984).

Chen, Michael C. and Lawrence J. Henschen, On the Use and Internal Structure of Logic-based Decision Support Systems, Decision Support Systems 1, no. 3 (1985) 205–219.

Cook, S., C.D. Hafner, L.T. McCarty, J.A. Meldman, M. Peterson, J.A. Sprowl, N.S. Sridharan and D.A. Waterman, The Applications of Artificial Intelligence to Law: A Survey of Six Current Projects, AFIPS Conference Proceedings 50 (1981).

Dahl, V., On Database Systems Development through Logic, ACM Transactions of Database Systems 7, no. 1 (1982).

de Kleer, Johan, An Assumption-Based TMS, Artificial Intelligence 28, no. 2 (1986) 127–162.

de Kleer, Johan, Extending the ATMS, Artificial Intelligence 28, no. 2 (1986) 163–196.

de Kleer, Johan, Problem Solving with the ATMS, Artificial Intelligence 28, no. 2 (1986) 197–224.

Elam, J. and R.M. Lee, eds., Special Issue on Model Management Systems, Decision Support Systems 2, no. 1 (1986).

Flores, F. and J.J. Ludlow, Doing and Speaking in the Office, in: G. Fick and R. Sprague, eds. Decision Support Systems-Issues and Challenges (Pergamon Press, London, 1981).

Gabbay, D. and F. Guenther, eds., Handbook of Philosophical Logic Volume I: Elements of Classical Logic (Reidel, Dordrecht, 1983).

Gabbay, D. and F. Guenther, eds., Handbook of Philosophical Logic Volume II: Extensions of Classical Logic (Reidel, Dordrecht, 1984).

Gabbay, D. and F. Guenther, eds., Handbook of Philosophical Logic Volume III: Alternatives in Classical Logic (Reidel, Dordrecht, 1986).

Gallaire, H. and J. Minker, Logic and Data Bases (Plenum, New York, 1978).

Gallaire, H., J. Minker and J. Nicholas, Advances in Data Base Theory, Vol. 1 (Plenum, New York, 1980).

Genesereth, Michael R. and Nils J. Nilsson, Logical Foundations of Artificial Intelligence (Kaufmann, Los Altos, CA, 1987).

Henschen, L.J. and S.A. Naqvi, On Compiling Queries in Recursive First-Order Databases, Journal of the ACM (Jan., 1984).

Hogger, Christopher John, Introduction to Logic Programming (Academic Press, London, 1984).

Hooker, John N., A Quantitative Approach to Logical Inference, Decision Support Systems 4, no. 1 (1988).

Hilpinen, R., Dcontic Logic: Introductory and Systematic Readings (Reidel, Dordrecht, 1971/1981).

Hughes, G.E. and M.J. Cresswell, An Introduction to Modal Logic (Methuen, London, 1968).

Hughes, G.E. and M.J. Cresswell, A Companion to Modal Logic (Methuen, London, 1984).

Jeroslow, Robert G., Spatial Imbeddings for Linear and for Logic Structures, Decision Support Systems 4, nr. 1 (1988).

Kershberg, L., ed., Proceedings of the First International Conference on Expert Database Systems (1986).

Kimbrough, Steven O., A Graph Representation for Management of Logic Models, Decision Support Systems 2 (March, 1986) 27–37.

Kimbrough, Steven O. and Fred Adams, Why Nonmonotonic Logic? Decision Support Systems 4, no. 1 (1988).

Kimbrough, Steven O., Ronald M. Lee, and David Ness, Performative, Informative, and Emotive Systems: The First Piece of the PIE, Leslie Maggie et al., eds., Proceedings of the Fifth International Conf. on Information Systems, Tucson, AZ (Nov., 1984) 141–148.

Kimbrough, Steven O. and Ronald M. Lee, On Illocutionary Logic as a Telecommunications Language, Leslie Maggie et al., eds., Proceedings of the Seventh International Conference on Information Systems, San diego, CA (Dec., 1986) 15–26.

Kowalski, R., Algorithm = Logic + Control, Comm. ACM 22, no. 7 (1979) 424–436.

Kowalski, R., Logic for Problem Solving (North-Holland, New York, 1979).

Kowalski, R., AI and Software Engineering, Datamation (Nov., 1984).

Kowalski, R.A. and M. Sergot, A Logic-based Calculus of Events, Working paper (Dept. of Computer Science, Imperial College, London, 1985).

Lee, R.M., CANDID - A Logical Calculus for Describing Financial Contracts, PhD. thesis, available as WP 80-06-02 (Dept. of Decision Sciences, University of Pennsylvania, 1980).

Lee. R.M., CANDID Description of Commercial and Financial Concepts: A Formal Semantics Approach to Knowledge Representation, WP 81-162, IIASA, 1981. Also available as WP 84/85-3-3 (Dept. of Management Sciences and Information Systems, University of Texas, 1984).

Lee, R.M., Applications Software and Organizational Change: Issues in the Representation of Knowledge, Information Systems 8, no. 3 (1983) 187–194.

Lee, R.M., Database Inferencing for Decision Support, Decision Support Systems 1, 1 (1985) 57–68.

Lee, R.M., Bureaucracy as Artificial Intelligence, in: Humphreys, P., ed., Knowledge Representation for Decision Support (North-Holland, New York, 1985).

Lee, R.M., A Logic Model for Electronic Contracting, Decision Support Systems 4, no. 1 (1988).

Lee, R.M., H. Coelho and J.C. Cotta, Temporal Inferencing on Administrative Databases, Information Systems 10, no. 2 (1985) 197–206.

Lee, R.M. and L. Miller, A Logic Programming Framework for Planning and Simulation, Decision Support Systems 2, no. 1 (1986) 15–25.

Lee, R.M. and G. Widmeyer, Shopping in the Electronic Marketplace, Journal of Management Information Systems 2, no. 4 (1986) 21–35.

Lee, R.M. and P.C. Chu, Writing Expert System Shells in Prolog, Working paper 85/86-3-6 (June, 1986).

Liang, T.P., Integrating Model Management with Data Management in Decision Support Systems, Decision Support Systems 1, no. 3 (1985) 221–232.

Lloyd, J.W., Foundations of Logic Programming (Springer, Berlin, 1984).

Lyytinen, Kalle J., Theories of Language and Information Systems: An Appraisal of Alternative Language views for Information Systems, Leslie Maggie et al., eds., Proc. Fifth International Conf. Information Systems, Tucson, AZ (1984).

Lyytinen, Kalle and Erkki Lehtinen, Discourse Analysis as an Information System Specification Method (Academy of Finland and Department of Computer Science, University of Jyvaskyla, Finland, 1984).

Lyytinen, Kalle and Erkki Lehtinen, On Information Modelling through Illocutionary Logic (Academy of Finland and Department of Computer Science, University of Jyvaskyla, Finland, 1984).

Malone, Thomas, W., Kenneth R. Grant, Franklyn A. Turbak, Stephen A. Brobst, and Michael D. Cohen, Intelligent Information-Sharing Systems, Communications of the ACM 30, no. 5 (May, 1987) 390–402.

Mitroff, I.I., R.O. Mason and V.P. Barabba, Policy as Argument – A Logic for Ill-Structured Decision Problems, Management Science 28 (1982) 1391–1404.

McKenzie, Edwin, Bibliography: Temporal Databases, Working paper (Department of Computer Science, University of North Carolina, 1986).

Nute, Donald, Defeasible Reasoning and Decision Support Systems, Decision Support Systems 4, no. 1 (1988).

O'Keefe, R.M. Microcomputer Based Expert Systems Shells - The Spreadsheets of Artificial Intelligence, in: C. Takkenberg, Ed., Expert Systems and Artificial Intelligence in Decision Support Systems, (Reidel, Dordrecht, 1986).

Palmer, Kenneth, N. Kenneth Boudwin, Helen A. Patton, A. John Rowland, Jeremy D. Sammes, and David M. Smith, A Model-Management Framework for Mathematical Programming (Wiley, New York, 1984).

Roberts, F., Measurement Theory – with Applications to Decision-Making, Utility, and the Social Sciences (Addison-Wesley, Reading, MA, 1979).

Rozenshtein, D. and N. Minsky, Controlling the Use and

Evolution of Database Systems: A Prolog-Based Approach, Journal of Management Information Systems, forthcoming.

SAMPO, SAMPO-Project Final Report: 1983–1985 (Department of Computer Science, University of Jyväskylä, SF-40 100 Jyväskylä, Finland, 1986).

Scott, Peter, Logic-Based Representation of System Requirements, Decision Support Systems 4, no. 1 (1988).

Sergot, M., Representing Legislation a Logic Programs, Working paper (Dept. of Computing, Imperial College, London, August, 1985).

Sergot, M.J., F. Sadri, R.A. Kowalski, F. Kriwaczek, P. Hammand and H.T. Cory, The British Nationality Act as a Logic Program, Communications of the ACM 29, no. 5 (May, 1986) 370–386.

Silver, Bernard, Meta-Level Inference (North-Holland, Amsterdam, 1986).

Sprague, Ralph H., Jr., and Eric D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

Stamper, R.K., Towards a Semantic Model for the Analysis of Legislation, Informatica e Diritto's Special Monographic Edition on Informatics, Logic and Law (1978).

Stamper, R.K., A Logic of Social Norms for the Semantics of Business Information, in: T. Steel and R. Meersman, eds., Database Semantics (North-Holland, New York, 1985).

Steel, T. and R. Meersman, eds., Database Semantics (North-Holland, New York, 1985).

Sterling, L. and E. Shapiro, The Art of Prolog (MIT Press, Cambridge, MA, 1986).

Toulmin, Stephen, The Uses of Argument (Cambridge University Press, Cambridge, England, 1958).

Turner, Raymond, Logics for Artificial Intelligence (The Halsted Press, New York, 1985).

van Griethuysen, J.J., ed., Concepts and Terminology for the Conceptual Schema and the Information Base, International Standards Organization, ISO/TC 97/SC 21 (1984).

Widmeyer, G., Logic Modeling with Partially Ordered Preferences, Decision Support Systems 4, no. 1 (1988).

Widmeyer, G. and R.M. Lee, Preference Elicitation in Decision Aiding – Applications to Electronic Shopping, in: E. McLean and H. Sol, eds., DSS – A Decade in Perspective (North-Holland, New York) forthcoming.

Winograd, T., Beyond Programming Languages, Communications of the ACM 2, no. 7 (1979) 391–401.

Wolff, Robert Paul, Kant's Theory of Mental Activity (Harvard University Press, Cambridge, MA, 1963).

Vari, Anna, Janos Vecsenyi, and Zita Paprika, Supporting Problem Structuring in High Level Decisions: The Case of Siting of a Hazardious Waste Incinerator, Specific paper presented at the 10th SPUDM Conference, Helsinki, Finland (Aug., 1985).
