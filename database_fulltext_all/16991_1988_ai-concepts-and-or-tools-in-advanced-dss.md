---
otero_id: 16991
otero_key: "HE29UHGX"
title: "AI-Concepts and OR-tools in advanced DSS"
authors: "M.M. Richter"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90007-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# AI-Concepts and OR-Tools in Advanced DSS

M.M. RICHTER

University of Kaiserslautern, 6750 Kaiserslautern, FRG

The relation between Decision Support Systems and Expert Systems (as far as they are related to decisions) is discussed. We distinguish three different levels: the conceptual, the model-theoretic and the data structure level. In analyzing the differences between these two approaches we isolate the problems which arise in attempts to amalgamate the two different methodologies.

Keywords: Decision Support Systems, Expert Systems, AI Concepts, Functional-Logical Programming.

![](/api/attachments/HE29UHGX/fulltext/images/5cd7e5e16d0775d06726896a58e45779ed8265a59e22168b02bb9c6e8d2c502b.jpg)

## 1. Introduction

For any approach to deal with such a situation we can distinguish three levels of formalization:

The notion of an expert system is a very general one and it subsumes a great number of techniques which deal with a wide range of applications. In order to relate Expert Systems to Decision Analysis one has to restrict the area of applications in such a way that the following quotation from [7] becomes true: 'The intent of both Expert Systems and Decision Analysis is to help decision makers make better informed decisions'. That means, one is faced with a more or less complex situation which one has to analyze and where one has to make a decision of what to do. The activities based upon the decision may have desirable or undesirable consequences; the term 'better' refers to those consequences. The difficulty is that there are a number of different aspects involved each of which has its own notion of 'better' which in the first place may not even be individually clearly formulated and which in the second place may be in conflict with each other.

Michael M. Richter holds a chair in the Computer Science Department of the University of Kaiserslautern (West Germany). His main research area is Artificial Intelligence with emphasis on Expert Systems, in particular applications in engineering sciences. He wrote his doctoral thesis in mathematics at the University of Freiburg and has held teaching and research positions at different universities.

(1) The conceptual level:

Here one discusses informally the concepts which influence the decision and the aspects from which the situation under investigation is described.

(2) The model-theoretic and representational level: It contains the logical or mathematical models which are used to represent formally the conceptual level.

(3) The level of data structures and algorithms: It can be viewed as an implementation of the second level enriched by detailed computational methods of carrying out the formal procedures.

From the methodological point of view these three levels should be separated as much as possible. In principle the highest level should obtain its orientation only from the problem itself, and should be discussed without any reference to available methods of computation. In practice, however, such an ideal separation cannot always be carried out: The available methods for realizing a process will at least implicitly influence the proposals for its construction. In the sequel we will discuss the methods of Expert Systems and Decision Analysis on these three levels. It will turn out, that in some sense both have complementary strength but also have a common domain of competence. Complex problem areas in most cases contain parts which require techniques from both sides for an adequate solution. This calls for a merging of Expert Systems and Decision Analysis methods rather than a choice of one alternative. On the other hand one has to admit that such a merging has not really taken place. The reasons for this have to be made clear and tasks have to be formulated in order to overcome this undesirable situation.

## 2. The Conceptual Level

In principle there are not necessarily differences between the approaches of Artificial Intelligence and Decision Analysis on this level. One can observe a longer tradition and much more practical experience on the Decision Analysis side. Here historical reasons play an important role; the need for DSS was there before one even thought of AI. For lack of available uniform systems Decision Support Systems do not make decisions but, as the term indicates, only support them. As a consequence, concepts, aspects and methods have not to be fully represented at the lower levels and can therefore be discussed informally without any restrictions. Such aspects include psychological views and management techniques, uncertainty and common sense learning and general principles from sociology, economics and natural sciences. The aim is to model the process of decision making as a whole and to decide later on which parts can be computationally supported. The research in Decision Analysis has made a great number of contributions to the study of this mental process of decision making.

In contrast to this, Artificial Intelligence and Expert Systems investigations had in the past very little connections with actual, real-life decisions. The activities in AI have dealt more with general principles of thinking.

In the decade of the sixties a big goal for AI was the development of a ‘General Problem Solver’. This approach as a leading motive has turned out not to be successful and was given up later on. The research in this period has nevertheless made clear that problem solving does not take place in a mathematically clearly defined model. In order to simulate or to mimic human problem solving one has to take into account aspects from cognition theory, psychology, common sense and other areas: in principle most of those topics which also have been discussed in the Decision Support approach. The difference now was that the basic hypothesis of the AI-approach relies on the assumption that each of the mental processes under discussion can be represented in the form of symbol manipulation. In practice, this resulted into an axiomatization in some formal language of each of the areas under consideration. Instead of producing a General Problem Solver in this way one now studies models in which the available (partial) information can be used to infer in a formal process the desired conclusion, e.g. the decision.

This process of formalization was very much influenced by the available methods which we will discuss in section 4. Presently one can observe a tendency of axiomatizing the meta level rather than the object level alone. In a certain sense, this can partially be regarded as an axiomatization which has been formally discussed in Decision Analysis.

## 3. The Model Theoretic and Representational Level

J. McCarthy has called Artificial Intelligence the engineering science of logic. This is reflected by the fact that AI-systems are somehow always logical systems (in the sense of mathematical or philosophical logic). Usually one deals with extensions or variations of classical first order predicate logic. Extensions are obtained with respect to the expressive power by adding e.g. modal operators or higher order predicates; in principle the languages used can always be regarded as fragments of higher order predicate logic. These languages allow expressions like ‘necessary’ and ‘possible’, ‘allowed’ and ‘forbidden’, they admit causal and temporal reasoning as well as quantifications over predicates and functions and contain other devices.

Each of these languages has a well-defined syntax and semantics where the latter refers to the notion of truth. This notion of truth is the aspect which is what is mainly changed in the variations of predicate logic. Here we distinguish essentially two types. In the first kind one keeps the traditional truth values 'true' and 'false'. What is changed is the meaning of the logical symbols, which becomes most prominent in the case of negation. Classically, negation is a Boolean function which just interchanges 'true' and 'false'. The constructive or dynamic approach regards negation as a function which has as arguments not only a proposition A (and its truth value) but also the state of information about the whole world model as far as it is related to A. The problem of determining the truth value for 'not A' is reduced to the question 'Under which conditions are we entitled to reject A?' which of course does not have a unique answer and has led to various concepts like the closed world assumption or negation as failure.

A very different way of changing the notion of truth is to introduce additional truth values, as it is done e.g. in Fuzzy-logic, in which the set of truth values is the real interval [0,1]. The difficulty here is to relate the additional truth values to aspects introduced at the conceptual level. The state of this relation is not always satisfactory and has sometimes led to purely formalistic discussions at the representational level.

A very popular branch of logic in AI is the so-called non-monotonic logic. In the older literature is has been discussed under the name of inductive logic and its aim is not to deduce true conclusions from true assumptions but to generate general laws from an incomplete sample of observations. A typical example is the creation of an hypothesis which one uses for further inferences and manipulations. As an additional information may invalidate such an inductive inference one needs a book-keeping procedure for the dependencies on such not quite safe assumptions; these procedures are called truth-maintenance systems (see e.g. [9]).

The models investigated in Decision Support and Operations Research do not have this general descriptive character as in AI but they are more specific. We will just mention three of them:

\- Utility functions and the v. Neumann–Morgenstern theory,

\- Preference orders,

\- Statistical models.

All three aspects reflect partial views of reality and usually all three of them play a role in a DSS. What they have in common is that they ultimately reduce the problem situation to something which can be formulated in terms of real numbers. Particularly in case of multi-attributed decisions much of the work consists in establishing a proper utility function. The construction of such a utility function is at most partially supported by formal methods and is more dominated by experience by experience rather than by the use of mathematical models.

An important aspect of concrete situations is the incomplete character of information as indicated above. One possibility to deal with partial information is to reduce it to a statistical problem. In general this approach amounts to an optimal estimate for an unknown probability. These techniques again rely on the one hand on certain mathematical assumptions but incorporate on the other hand ideas whose formalization is presently not available in Expert Systems (see e.g. [1]). The difficulties AI has with statistical inference is discussed in detail in [13].

In order to model uncertainty one has used a variety of methods, one is the above-mentioned Fuzzy-logic. Although one runs in the same fundamental difficulties as in the AI-approach one has made a number of successful experiences in special situations. This was in particular then the case when the Fuzzy method could be naturally amalgamated with linear programming techniques (see e.g. [14]).

In general one can say that the choice of models considered in Decision Analysis has been very much dominated by the possibilities of compiling them down to lower levels. In particular the search for applying linear models is due to the fact that they can easily be computationally realized. A basic problem is that there is no systematic procedure and no formalism available which combines different views and solves possible conflicts.

## 4. The Level of Data Structures and Algorithms

In implementations of O.R.-systems one has made full use of two main techniques in classical data processing systems:

\- fast algorithms and

\- efficient database operations.

The implementation of fast algorithms requires a programming language with an efficient implementation and as little overhead as possible. In principle, very low-level languages offer the most possibilities for very efficient implementations. On the other hand, complex problem situations ask for tools to structure the programs; these are not available on very low levels. As a compromise most O.R.-algorithms are written in one of the classical programming languages like COBOL, FORTRAN, PASCAL etc. The available data base systems get their strength from the ability to handle large sets of data which have to be, however, of some simple and uniform structure. One can say that O.R.-techniques in Decision Analysis have made good use of the present data processing tools but they did not lead to new programming styles and corresponding programming languages or to essentially new database concepts.

In a case where data processing methods did not meet the requirements presented by the problem situation one did always change the representation of the problem rather than enriching and strengthening the methods. The change in the representation is achieved by encoding the original problem in a different way. Although the universality of classical programming languages guarantees the possibility of such an encoding this process nevertheless destroys in some sense the structure of the problem: Properties which could previously be expressed explicitly are only implicitly present and have to be explained on the meta level by additional comments. The success of such an encoding in a practical situation depends not so much on the size of the problem but essentially on its structural complexity.

The Artificial Intelligence approach used in Expert Systems was in so far radically different that it also resulted in new types of programming languages. This was not so clear in the first decade (the 1960s) where LISP was the basic AI-language. Although the nucleus of LISP, pure LISP, is a functional language, the use of the actual LISP system was rather a matter of convenience. LISP as a list processing language supported AI-systems but could very well be understood in the traditional sense, the only novelty was that there was no distinction between data and programs. In functional programming one does not specify explicitly the order of commands which the program has to carry out but only the input-output behavior of the program regarded as a mathematical function. In some sense this means that one only declares something, but on the other hand the listing in the definition of the functions allows to incorporate much of the procedural knowledge; therefore we would like to locate functional programming somewhere between imperative and logical programming. The real break-through of the declarative point of view came with the idea of logic programming as first realized in PROLOG. Logic programming allows to write down directly in the language the facts and rules which one knows about the situation; this knowledge can be of a very incomplete nature. The advantage of this approach is that one has not to worry about how the knowledge is used: The system takes care of the logical inferences and returns only valid consequences. That this way of knowledge processing is really an advantage depends on the situation, however. In case where the programmer can express everything he knows in the language he may be happy that the system does the rest of the work. Now PROLOG is essentially (a fragment of) first order predicate logic and there are many aspects which in principle cannot be expressed here. In particular one cannot formulate knowledge about an effective organization of the inference process itself, and such knowledge may be very well available to the programmer. The ways such knowledge can enter a logic program are again of an implicit character. In case the programmer knows the interpreter he can choose an appropriate ordering of facts and rules in order to avoid unnecessary backtracking; in addition he can use control structures like the cut symbol. To mimic procedural programs in a declarative language in such a way is certainly an undesirable step back towards the programming style of the early 1950s.

In order to enlarge the expressive power classical AI languages have been enriched by new features, other languages have been developed and complex representation systems were created. The most important extension (compared with PROLOG) was the incorporation of hierarchical aspects. One way to do this is the object-oriented approach. This idea has two conceptual fathers: The frame idea as formulated by Minsky and the class concept in SIMULA (or later SMALL-TALK). In LISP the object-oriented addition is called the FLAVOR-system. The advantages of the object-oriented programming style are twofold. On the one hand methods are associated to objects; this enforces a certain kind of modularization and therefore supports structured programming. Secondly, the objects are ordered in an hierarchical way and an inheritance mechanism automatically transfers properties and methods attached to some general object to their specializations. In principle, one could regard this as a very compact representation of rules; it is , however, something more because it makes intrinsic structures of the problem situation visible. Another way to deal with hierarchic dependencies is the use of types. In type theory, higher order structures can be represented adequately. This was of major importance in functional programming languages where one distinguishes functions, functions of functions, etc. (higher order functionals). Typical examples of such languages are ML or MIRANDA, which is SASL with a polymorphic type structure, see e.g. [3].

Modern knowledge representation systems have incorporated a number of complicated representation techniques and reasoning methods. Some of these quite powerful instruments are commercially available like KEE, ART or Knowledge Craft. The applicability of these and other systems still depends on the fact whether the type of reasoning required in the application is supported in the system. For many problem areas arising in Decision Analysis this is unfortunately not the case. We will discuss this in the next section.

## 5. Gaps between the AI and the O.R. Approach

In analyzing the differences between Expert Systems and Decision Support Systems we have carefully to distinguish between those aspects which are inherent to the chosen approaches and those which just happen to exist in present systems. Concerning the former ones we will concentrate on the two techniques mentioned at the beginning of section 4, fast algorithms and efficient database operations. They can both be considered as essential instruments of classical data processing systems but they are only in a rudimentary form available in present AI systems. This is due to the fact that the expressive power of knowledge representation systems is not sufficiently strong to express that kind of knowledge which is responsible for making algorithms and operations fast. In addition, designers of complex representation systems have not put very much effort into the incorporation of (mostly low-level) techniques to speed up programs. On the other hand AI systems have certain advantages over traditional algorithms also with respect to efficiency. An algorithm has to obey its defining rules as stupid as they may be in some specific situation, whereas AI systems have the chance to use unforeseen knowledge in order to shorten the arguments. We observe here two interface problems: The relation between a knowledge representation system on the one side and a traditional programming language and a database system on the other side (see also [10]). In order to close the gap between the declarative and the procedural programming style, one would like to combine as a first attempt logical and functional programming in a unifying language. From a theoretic point of view one still deals with two kinds of declarative knowledge. This would not only allow to call algorithms if they are available and to use inference techniques if incomplete knowledge prohibits a precise formulation of a procedure. This would also make possible to interweave both approaches. In real-life situations we encounter always alternations of logical and functional knowledge which can only be separated artificially: In order to solve a certain problem one reduces it to a number of subproblems where some can be solved by precise algorithms and others have to be logically further reduced to problems which in turn might call inference methods or algorithms, which again... etc.

We will mention two approaches for unifying functional and logical programming. One is TEL which merges first order logical programming and first order functional programming (cf. [12]). The other approach was realized in SASLOG which is a symbiosis of PROLOG and the purely functional programming language SASL (cf. [8] and [5]). Although SASLOG has been implemented on the basis of an operational semantics, there are still several fundamental questions open. One of the main problems is a missing denotational semantics, which is essentially due to the fact that logic programming is mainly first order logic whereas functional programming is higher order. From the practical point of view, however, SAS-LOG or TEL provide a first basis for merging functional and logical tools.

The second interface is between a knowledge representation system and a database system. As long as AI-systems have been applied only to small toy problems there was no need for a database system, because all the knowledge could easily be stored in the core memory of a computer. For large industrial application this is no longer possible. Here the main problem is the following: Knowledge representation systems are structured for an intelligent and flexible behavior and pay for this ability by being very slow. Traditional database systems can perform fast a great number of steps, but these have to be of a very simple and uniform manner. To close this gap there have been two main approaches which are ultimately not so far from each other.

One way is to introduce a new generation of knowledge base management systems which on the one hand can store complex information but on the other hand still keeps most of the power of database systems. The general demand for such systems is discussed in [2], the realizations are undertaken e.g. by Jarke et al (cf. [6]).

The other method is to introduce a certain buffer zone between the expert system and the database. In this zone one has to organize queries from the expert system to the database and to optimize these queries. First examples have shown that one encounters here a great number of problems, and simple-minded approaches will not work (see e.g. [4] or [11]).

In summary one can say that the gap between Expert Systems and DSS is not only due to historical reasons but at least as much to difficulties resulting from data processing problems. These problems have now been isolated, clearly formulated and led to a number of new research activities. The developments have certainly been influenced by a great pressure coming from practical needs: Quite a number of problems call for the application of AI as well as O.R. techniques and therefore require a merging of both of them. This, however, cannot be achieved without an essentially new progress also on the level of programming languages and database techniques. Some steps in this direction have been done, but only the very first ones. In addition, it is now time to work out mechanisms on the model theoretic and representation level which describe the merging techniques on a principal level and regulate the diverging views.

## References

[1] P. Abel: Stochastische Optimierung bei partieller Information. Mathematical Systems in Economics 96, 1984.

[2] M. Brodie, J. Mylopoulos (eds.): On Knowledge Base Management Systems: Integrating Artificial Intelligence and Database Technologies. Springer-Verlag 1984.

[3] W. Correnz, J. Ingenerf, M.M. Richter: Remarks on ML and its Polymorphic Type Structure. In: 'it – Informationstechnik', 29. Band (1987), p. 235–240.

[4] Th. Härder, N. Mattos, F. Puppe: Einige Schritte zur Kopplung von Datenbanksystemen und Expertensystemen. In: State of the Art 3 – Expertensysteme, Oldenbourg-Verlag 1987.

[5] K. Hinkelmann, K. Nökel, R. Rehbold: SASLOG: Lazy Evaluation Meets Backtracking. Preprint. Kaiserslautern 1987.

[6] M. Jarke: Kopplung qualitativer and quantitativer Theorien in der Entscheidungsunterstützung. MIP 8716, Passau 1987.

[7] R.L. Keeney: Value-driven Expert Systems for Decision Support. In: Expert Judgement and Expert Systems, ed. J.L. Mumpower et al., Springer-Verlag 1987, p. 155–171.

[8] K. Nökel, R. Rehbold: SASL: Implementierung einer rein funtionalen Sprache mit Lazy-Evaluation. SEKI Working Paper SWP-86-07, University of Kaiserslautern 1986.

[9] M. Reinfrank: An Introduction to Non-Monotonic Reasoning SEKI Memo 85-02, University of Kaiserslautern 1985.

[10] M.M. Richter: Expertensysteme und konventionelle Programme – Unterschiede und Kopplungsprobleme. In: 'Technologie, Wachstum und Beschäftigung'. Festband zum 50. Geburtstag von Lothar Späth, ed. R. Henn, Springer-Verlag 1987, p. 283–292.

[11] A. Reuter: Interfacing Database and Expert Systems. In 'it – Informationstechnik', 29. Band (1987), p. 164–175.

[12] G. Smolka: TEL Version 0.9. Report and User Manual. SEKI Report SR-87-11, University of Kaiserslautern 1987.

[13] J.W. Sutherland: Assessing the Artificial Intelligence Contribution to Decision Technology. IEEE Transactions on Systems, Man, and Cybernetics 16 (1986), p. 3–20.

[14] R. Weber: Entscheidungsprobleme bei Unsicherheit und mehrfacher Zielsetzung. Mathematical Systems in Economics 80, 1982.
