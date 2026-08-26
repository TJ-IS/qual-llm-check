---
otero_id: 23377
otero_key: "H5NCJHG8"
title: "A Software Engineering Perspective"
authors: "R J Cunningham"
year: "1989"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1989.4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Software Engineering Perspective

R.J. Cunningham, Department of Computing, Imperial College, London

## The field

The term ‘software engineering’ was introduced at a NATO Science Conference (Naur and Randell, 1968) to describe that area of human endeavour whose products are computer programs. From the start it has been a marriage between computer scientists with interest in the technical issues of producing sound software and managers faced with the practical problems of software projects, some of which could already be measured in man-millenia. The need for software specification, software quality and software engineering education were evident in the 1968 conference, central to the successor conference (Buxton and Randell, 1969), and embraced by the profession. In contrast, many of the programming languages and methods used at the time have since been forgotten. There was a software crisis then, and a gulf between theory and practice for engineers to bridge. As we look for a software engineering discipline to exploit the fifth generation architectures of the 1990s we must also expect to overturn yet again some of the traditional technologies of software and perhaps rediscover the principles of an evolving profession.

To perceive the future we project from the past, aligning by our perception of current research. This perspective is hard to calibrate. Research is by nature a long-term and high risk activity better judged by results than in anticipation of them. The well being of the software industry depends on the mass of technology transfer and innovative development which is part of the quest for the goals of research. To ensure that investment in research catches and endows benefits from the peaks of impact it is necessary to invest on a broad front. This has led to national programmes in the leading industrial nations and international programmes such as the Esprit project of the European Commission. The closely related areas of software engineering and software technology are major parts of these programmes. Where we mention particular projects it is by way of illustration only.

A decade after the founding conferences of the software engineering field the US Department of Defense launched its Software Technology Initiative (Redwine et al., 1981) in recognition of the soaring cost of embedded software compared with the hardware for which it was purchased. A summary of responses to a questionnaire (Siegel, 1982) showed a familiar picture of problem areas across the whole development process, most frequently perceived by the difficulty of finding and keeping qualified personnel, defining goals and measuring success. These responses were strong indicators of 'the poor state of the art in software engineering', and made clear the need to make technical considerations high in the proposed initiative. The complexity, reliability and availability of software had become crucial issues. Short-term palliatives could be prescribed; long-term cures were required.

## The software engineering process

The untenable distribution of costs in the software development life-cycle has served to focus much software engineering research. The most obvious manifestation of problems in the 1970s was the excessive proportion of costs (variously estimated as between 50 and 90 per cent) incurred in activities which were euphemistically called maintenance but were in reality fault rectification and evolutionary development. Paradoxically, the symptom of excessive ‘maintenance’ has been partly alleviated by the revolution in hardware technology. The wide availability of cheap personal machines has changed the overall pattern of the industry by introducing a retail market for both hardware and software, partly decoupling the customer from the producer and fostering the growth of an independent software products industry with more conventional sales and marketing policies. However, this structural change in the industry has done little to change the methods used by the industry.

The weakness of present software engineering stems from its dependence on people. It is labour-intensive. Expensive, trained people are required to convert requirements into a specification and to go from specification to product. People of adequate training are in short supply. Their scarcity allows the industry to indulge in short cuts of poor workmanship and mystique rather than literate professionalism. Inevitably problems build up and re-appear as 'maintenance' requirements. The limits of such software processes were foreshadowed by Lehman (1974), who observed that large systems could collapse under the metaphorical weight of their own errors. The sketch of a solution has been foreseen by Balzer, Cheatham and Green (1983):

<table><tr><td>Automation based paradigm</td><td>Current Paradigm (1983)</td></tr><tr><td>Formal specification</td><td>Informal specification</td></tr><tr><td>Prototyping standard</td><td>Prototyping uncommon</td></tr><tr><td>Specification is the prototype</td><td>Prototype created manually</td></tr><tr><td>Prototype validated against intent</td><td>Code validated against intent</td></tr><tr><td>Prototype becomes implementation</td><td>Prototype discarded</td></tr><tr><td>Implementation machine aided</td><td>Implementation manual</td></tr><tr><td>Testing eliminated</td><td>Code tested</td></tr><tr><td>Formal specification maintained</td><td>Concrete source maintained</td></tr><tr><td>Development automatically documented</td><td>Design decisions lost</td></tr><tr><td>Maintenance by replay</td><td>Maintenance by patching</td></tr></table>

Because there is no technology that can replace the informal human processes of the current development paradigm we must change the paradigm to one which can be automation-based.

This new paradigm will have formal processes at its heart. Balzer, Cheatham and Green make the following comparison:

Once the key role of a formal specification is recognized it is easy for trained software engineers to see the enhanced possibility for introducing various elusive elixirs of software productivity. Formal specifications are the potential data for databases of re-usable software and for knowledge-based systems to support design and modification. It is less easy to predict the relative importance of the different paradigms which may mark the introduction of methods to exploit formal notation.

Alternative future paradigms have been a subject of a recent series of software process workshops (Potts, 1984; Wilden and Dowson, 1986; Dowson, 1987). These workshops have served the purpose of drawing attention to the need for models on which to base the software environments of tomorrow. It has been suggested that software processes may themselves be treated as algorithmic processes, albeit with parallelism and asynchrony (Osterweil, 1986). A calculable basis for future software engineering has yet to be provided.

## The software factory

A major strategic objective set by the UK Alvey programme in software engineering (Talbot and Witty, 1983) was that the UK should become a world leader in information systems factories. The cottage industry of application specific software system development had to be replaced by some more efficient kind of production facility. This was perceived as an Integrated Project Support Environment or ISPE. The major part of the programme would be research and development leading to the overall objective, but supporting issues such as training in new methods could not be ignored.

In the Software Engineering context an IPSE is a set of computer-based facilities which gives integrated support to all, or most, tasks involved in the production of the software . . .' (Talbot, 1986).

The uniform program interfaces and language

processing tools of the Unix system (Ritchie and Thompson, 1978; Kernighan 1981) made it the basis for ideas of programming environments. The version and configuration control systems developed as extensions (Feldman, 1979) were an early step towards the IPSE of the future. These IPSE extensions were insecure for their purpose because the functions could be bypassed and were limited by the file concepts of the operating system. More abstract requirements for a programming support environment were crystallized in the US DoD Stoneman Report (Buxton and Stenning, 1981), which has led to recent work on Ada Programming Support Environments.

There are now several major IPSE development projects under way. Some experimental language-dependent environments are reported in the proceedings of two recent conferences on software engineering environments (Sommerville 1986, Henderson 1987). Ultimately IT companies must expect to make large investments in this kind of production facility so we will try to clarify the relationship between the current major projects and the fifth generation systems of the 1990s.

Three generations of IPSEs were conceived in the UK Alvey programme, according to the technology used for the information base: (1) FILE SYSTEM, (2) DATA BASE, (3) KNOWLEDGE BASE. By this classification most current major projects are second generation IPSE developments evolved from first generation Unix technology. The new environments are large distributed systems intended to be the base for industrial system development, either directly or as a prototype. They are evolutionary rather than revolutionary. There is considerable risk in the application of network technology to support geographically distributed project teams with individual workstations and local databases. To make an IPSE also depend on research into knowledge-based technology would defer its development. Thus the software support systems of the 1990s will be half a generation behind the knowledge-based expert systems of fifth generation style applications.

The second generation IPSEs differ considerably in their functional emphasis. Some have obvious potential for evolution. For example ISTAR (Dowson, 1987), one of the few already available, is in essence a distributed project support environment utilizing a subcontract principle for task deliverables, but with the flexibility to include toolsets for specific process models. The Esprit PCTE project (Campbell, 1986) implements a public common tool interface based on an entity-relationship model for data object management and inter-process communication. Thus it too can support specific process environments such as the Graphic representations of informal methods used in the UK ECLIPSE project (Reid and Welland, 1986).

Ultimately the dependence on current semi-formal database technology and the absence of a calculable basis for software development will prove limiting for evolution of most current IPSE schemes, but alternatives without the limitations are still research experiments. The Japanese IOTA system (Nakajima et al., 1980) is an interesting prototype of an environment for formal design specifications. A selection for future interest might include the developments of Balzer's paradigm (Balzer, Goldman and Neches, 1984), plan-based aids to programming like the Programmer's Apprentice (Waters, 1985), moves towards environments based on formal transformation for software design (Krieg-Bruckner et al., 1986), and new Alvey and Esprit projects to support formal language environments. The use of mathematical notation for the discrete processes of software engineering has been recognized as the key to future software process environments, but schemes to exploit the use of suitable notation in an IPSE are still in their infancy.

## Formal methods and notations

One of the first effective methods of the software development process was 'structured programming' (Wirth, 1971; Dijkstra, 1972). This was popularized as an informal program design method based on successive refinement from an initial statement of the program's function as a process with a single entry and a single exit. It helped to yield programs of clear structure, and thence of enhanced quality because the improved possibilities for reasoning about programs reduced malfunction. Programming languages like Pascal were fostered because the clear procedural abstraction for encapsulating parts of a program's function made well-structured programs natural. In fact a major trend towards the abstract structuring of systems is reflected in the contemporary development of relational calculi for databases (Codd, 1970; 1972), schemes for structuring systems by integrating data and procedural abstraction, (Hoare, 1972; 1974) and forms of module specification and information hiding (Parnas, 1972). Paradigms for well-built systems were thus established but method itself was de-emphasized. Subsequently some useful frameworks for informal methods have been achieved by concentrating on the structure of the input-output relation (Jackson, 1975) and the data flow structure (DeMarco, 1979).

Formal design procedures for conventional programming styles depend on the foundation work of Floyd (1967) and Hoare (1969) in axiomatizing the effect of conventional imperative program constructs by specifying the condition of the data before and after execution. Similar adaptations of predicate logic to formalize programs are loosely known as Hoare logics. These have been extended to include special treatments for parallelism (Lamport and Schneider, 1984). Rigorous design methods based on Hoare logics can provide verifiable programs (Wirth, 1973; Dijkstra, 1976; Jones, 1980). Informal methods like structured programming are inadequate because the program specification is implicit. The practical application of the more rigorous methods to large systems has depended on skilled personnel making empirical use of notations for data and procedure abstraction rather than the development of concomitant formal methods of system structuring. These techniques have strained the linguistic resources of traditional programming languages and made them cumbersome.

Incisive progress on data abstraction was achieved with an algebraic framework (Goguen et al., 1975; Guttag, 1978). Typical data types such as sets and stacks can be axiomatized in an equational style and the defining equations then re-interpreted as rewriting schemes for operation as abstract data-access procedures. The rewriting technique fits well with notations known as functional or applicative languages, the archetype being pure Lisp (McCarthy, 1960; 1962). Today there are several new and exciting functional languages (Backus, 1978; Burstall et al., 1980; Milner, 1983; Turner, 1985). They are one practical manifestation of that class of programming languages known as declarative languages (as opposed to the traditional imperative ones) because their style is that of defining rules rather than procedures. The other main group of declarative languages are the logic programming languages, of which Prolog (Colmerauer et al., 1973, Kowalski 1979) is the main example. Declarative languages are well developed but not yet widely used outside research circles because their interpreters on traditional von Neumann machines have been inefficient for mundane applications.

Declarative languages can more easily accommodate massively parallel execution (Darlington and Reeve, 1981), so technology is in their favour for fifth generation systems. Appropriate software development methods are required. An embryo method of design through successive program transformation was introduced by Burstall and Darlington (1977) and has been extended to logic programming (Clark and Darlington, 1981). Another well-developed technique is the tableau design method of Manna and Waldinger (1980). Because pure declarative programs can be treated as formal mathematical objects, a variety of systematic techniques for rigorous deduction are applicable. Declarative languages constitute an important bridge between traditional programming skills and more rigorous mathematical notation for system specification.

A programming method, no matter how sophisticated, cannot compensate for the inadequacies and inconsistencies arising from a poor specification, even though a good design method can help to expose a poor specification. Unlike the well-developed notations for programs, notations for specification are relatively unknown. Instead, bulky documents in pompous but inexact English are prevalent in the procurement circles of government and industry. Good specifications are difficult to achieve. A notation for specification should enable what is required to be expressed with abstract precision but enable the user to avoid concrete bias on how the requirements should be satisfied in a design. It is not surprising that the technically adequate notations for specification languages have been adaptations of formal logic or algebra. These are formal languages in a strict sense. Both their form and their meaning are well defined mathematically. Furthermore, a useful formal language has proven rules for deduction. Only this type of language can be a candidate for Balzer's automation-based software development paradigm of the future.

Two styles of formal notation stand out as candidates for the 1990s: (a) pure declarative programming languages, and (b) formal specification languages. These styles are often associated with different research communities, but they have in common presentations of set theory, recursive function theory, algebra and logic. Rule-based systems and fifth generation architecture seek to interpret inference steps of the formal presentation language as execution steps of an abstract computer. Fundamental research on the constructive logic of programs (Martin-Loef, 1979; Constable, 1983; Coquand and Huet, 1986) will clarify this area for future architectures. Current declarative programming notations severely restrict the formal language and its interpretation in order to ensure tolerable efficiency in execution. This limits their acceptability as specification languages because clarity and soundness of the system of reasoning are compromised. The distinctions will be less pertinent with future generations of logic programming and specification logic.

At present VDM (Bjorner and Jones, 1978) is one of the few commercially supported notations in the formal specification style and for this reason it may become the dominant specification language in the short term. However it carries a notational burden from traditional programming which makes it unnatural for declarative programming design styles. Various other candidates promise technical advantages; the greater clarity of Z (Abrial, 1980), the higher order combinators of Clear (Burstall and Goguen, 1977; 1981) and the expressiveness of modal logics for time, action and duty (Pnueli, 1986; Jeramaes et al., 1986). The use of modal logics for specification is a natural generalization of Hoare logics for program correctness (Goldblatt, 1982). These logics do not suffer from the limitations of traditional programming notation and can express properties that are cumbersome in standard Predicate logic. The potential advantages have not yet been widely explored.

Although the principles of these new formal notations are founded in logic and mathematics, systematic ways of using formal language in software engineering are still a research area. Methods for developing a formal requirements specification, for validating it, for initiating design, for reifying it as an implementation, and for maintaining useful function in a world of replaceable software parts are research goals which will themselves deploy the systems of inference used in fifth generation systems. Figure 1 depicts some of the problem areas for software engineering as they are seen from the UK Alvey Forest Project with which the author is associated (Cunningham et al., 1985; Finkelstein and Potts, 1986; Jeremaes et al., 1986).

For the early fifth generation applications a number of mathematically-based notations for specification and program will be available, giving the possibility of rigorous reasoning in design to ensure highly reliable systems in subsequent application. The extent to which enhanced quality alone will support the introduction of formal methods remains to be seen. Many practitioners feel the productivity payoff will arise only when the formal basis can be exploited to provide new avenues for software development and maintenance. These avenues would include greater automation in the software process and more effective methods for using parallelism in design. Maturity in the use of formal methods could be long in arriving.

## Software tools and technology

One of the misconceptions about software engineering research arises from the pre-eminence of concern with method. This obscures its dependence on the underlying technology. The problems identified by the DoD did not come from the lack of disciplined methods in the management of software production. They came rather from the inability of discipline and method alone to contain the problems arising from obsolete technology. Third and fourth generation developments in software technology have improved the situation by providing software tools to assist the use of accepted methods and thus make the production processes more efficient and reliable. Many of these tools are associated with proprietary operating systems and products. Some of the ideas on integrated data and program abstraction have been embodied in the modules or packages of new programming languages like Modula 2 and Ada, and in the style of object-oriented programming (Goldberg, 1984). The ramifications of the object-oriented view of systems as a hierarchy of combined process-cum-data objects is still permeating the software engineering world, but it has clear advantage for easily perceived software design when there are possibilities of concurrent processing and it appears to ease the problems of human interfaces to such systems because of the enhanced potential for graphical presentation.

It may be observed that for each new method of system development there are possibilities of supporting tools. A wide variety of systems have evolved to support the implementation of distributed systems, following research effort into the problems in the late 1970s. The solutions differ in characteristic from operating system support for a network of heterogeneous components (Tannenbaum and van Renesse, 1985) to programming languages for Hoare's model of synchronous communicating processes (Hoare, 1978). Technical solutions to related problems like evolution and reconfiguration have also been provided (Kramer and Magee, 1985). Similarly, recent research into the problems of requirements analysis and specification in software engineering is leading to workstations for system analysis and specification building (e.g. Stephens and Whithead, 1985). However, to appreciate the future tools technology of knowledge-based software engineering systems we cannot afford to look for the particular integrated package which supports a favoured specification or programming language. We can hope that past lessons on uniform interfaces and modular abstraction have been learnt and can be improved upon. We must search for the universal tools of the future, the latter-day analogues of the languages and parser generators which arose out of applied syntactic theory from the 1960s. Since then we have developed our semantic theories and their application in deductive programming systems. We can look towards formal systems with higher-order objects (Burstall and Goguen 1977) in which specifications themselves can be manipulated and implementations derived by machine. The difficulty lies in the deductive machinery.

![](/api/attachments/H5NCJHG8/fulltext/images/8b1f6a89e28f17c78f214474bf6a56cd514958c18c8c8331db9f5043976b20a0.jpg)  
Figure 1. Formal requirements specification techniques. Thus the foundations for the use of formal methods in software engineering are well-established but the paradigms, methods and training for their use are much more problematic. There are major issues in these areas which will only be resolved by quantitative assessments of cost effectiveness.

Logic programming is not a deductive panacea. Its manifestation as Prolog is a programming language with its roots in the Horn Clause theorem-proving technology of the early 1970s. These theorem-proving methods are already dated and being supplanted by other systems. But Prolog is a mature, rule-based, system implementation technology for the 1990s, with adaptation for parallelism (Clark and Gregory, 1986) and few advanced contenders. Because logic programming languages exploit unification (a form of two-way matching) to decide which rule to apply they eliminate the need for detailed case analysis by the application programmer, who can thus be more productive than with a traditional high-level imperative language. Like other programming languages, Prolog has some natural fields of application, and in this case expert systems figure prominently, but it will also evolve and be used in other areas where convenience and familiarity are the determining factors.

The newer technologies of automated deduction are at present embodied in experimental suites like LCF (Gordon et al., 1979), Boyer and Moore's (1979), ITP (Lusk et al., 1986), MKRP (Eisinger and Ohlbach, 1986), and REVE (Lescanne, 1986).

These are used by researchers to validate and support their own reasoning. The applications range from problems of Hardware Design (Gordon and Herbert, 1986) to traditional mathematics (Bundy, 1983; Dick and Cunningham, 1986). Strategies for problem solving in different logics are being evolved and will be the engine designs of future software processors.

Another major theoretical stride of the 1970s was foundation work on the denotational definition and semantic domains of programming languages (Scott and Strachey, 1971; Stoy, 1977). This is still the source of much foundation work on programming logics (Abramsky, 1989), but meanwhile a number of research tools have been developed which generate an interpreter for a language from its definition (Mosses, 1976; Wand 1985). Future applications of denotational semantics include natural language itself because there is a link with Montague's formal treatment of English (Montague 1974).

If we distinguish the tool building of the future from the bulk of new product development, we must recognise that after 20 years graphics has become a mature technology with established standards. This will be exploited in the products of the fifth generation because the technology for networks of high resolution graphical interfaces is available. Software systems for programming the essentially asynchronous processes involved in this form of interaction are still evolving. A new challenge here is to marry enhanced visual imagery with specialized deductive systems. In the products of the future, knowledge-based deduction must be applied not just as an introspective ingredient of future IPSEs, which are the machine tools of the future, but through sympathetic interfaces to improve our real factories, hospitals and schools.

## The future software engineer

In taking a rather high-level perspective of technical advances in software engineering we have not given much attention either to problems of team management, productivity and quality in the practice of today, or to the gaps in the technical advances. We are not going to remedy the first deficiency, for better qualified authors have written books about these problems (e.g. Brookes, 1975; Buckle, 1977; Evans, 1983). The technical deficiencies in our advance are the first of the matters which do concern us here.

Fifth generation architectures are a timely way to exploit massive parallelism available at the processor level. They use the one credible means for effective general exploitation of massive parallelism with current software technology, that is through the declarative, rule-based programming systems popularised by Prolog. The expert system style of application is a good fit with this new fifth generation software technology. In other areas of artificial intelligence, particularly natural language interfaces, logic programming schemes are only the best available technology for addressing the issues of representing knowledge simply and making non-trivial inferences. For special forms of processing such as signal processing more conventional vector processing technologies are unlikely to be supplanted, while for custom-built distributed systems there are a variety of special programming systems for communicating processes.

There are two serious technical concerns with the fifth generation outlook for software engineering. The first is that declarative programming systems are not yet supported by good methods for the engineering of software. Unsound software can be developed. Large ill-conceived 'logic programs' have the problems of other large software systems without the support of informal methods for structured design, error diagnosis and maintenance. As mentioned earlier there exist sound bases for the formal development of a declarative system from its specification, but the methods are not well-developed and perhaps weakest with Prolog programs. Thus there is a software process 'problem' for fifth generation software. This could be acute with those areas of application which are not well-matched to the concepts of present declarative programming languages, e.g. real time systems. This is the second serious technical concern. The designer of a real-time fifth generation system has a dilemma over how to exploit massive parallelism. Should the work be done in the conceptual quagmire of a declarative programming logic not intended for real-time control (but see also Kowalski and Sergot 1986), or use some lower-level concurrent programming logic like CSP (Hoare 1978) which provides finer control but is limited in programming abstraction and methodological support?

There are also some matters of professionalism which concern us all and deserve inclusion as essentials for the future of our profession. We might summarize them as fitness and social responsibility. This form of fitness is technical fitness to practise the profession. It must be clear to all by now that training specific to the field will be essential for the proper drafting and interpretation of a specification, let alone for those charged with developing a system to implement the requirements. Unfortunately our education system, including most university science and mathematics departments, is firmly bound to the classical mathematics of the nineteenth century. This was a rich era which laid the foundation for the might of modern science. It passed over elementary foundation questions such as which axioms hold for sets, or when an inductive argument is sound. It had nothing to say on the structure of language itself. These are not questions pertinent to physics or chemistry. Yet as a result, in periods of industrial change an able graduate from some such discipline will be expected to assist in the implementation of an air traffic control system, perhaps blithely unaware of the formal, logical, junior-school level of distinction between a set and a bag or multiset.

Without dwelling on resolution of the training problem for the fifth generation technologist, let us briefly raise the issue of social responsibility. It is related because technical strength gives authority. Because there are many unresolved issues over the methods of reasoning and inference for knowledge-based systems it behoves us to be frank about the difficulties. There is an unfortunate tradition of hyperbole as a substitute for science in securing large contracts for new applications of computers. The computer field is large enough to support a profession in software engineering. Professionals have a duty to society which goes beyond contractual obligation to employer or customer. This is not reflected in the legal structure of the profession. Until it is we will be unable to use fully our technical knowledge for the benefit of society or to protect it from its own excesses.

Fifth generation systems are a challenge worthy of any engineer. Training and professionalism should make us fit for it. Paul Abrahams, in a recent ACM President's Letter (December 1986) refers to the role of failure in software design, reporting Henry Petroski's view that engineering failures may be viewed as disproving design hypotheses. When the limits of analysis are exceeded in large system engineering, a scientific approach based on a working hypothesis is our best way forward. Novelty in design is a feature of progress, it is not doomed to failure. Michael Jackson, at a recent talk of the Association for Information Technology, reminded his audience of Knuth's reference to the Shanley Principle (Knuth, 1974), the need for integration rather than modularity when pushing technology to its limit, so that the rocket skin is both structural and aerodynamic in function. The principle seems to be used when the rules of fifth generation systems are both knowledge representation and program, but there are new technologies on the horizon beyond fifth generation, perhaps using connectionist technology (MacClelland and Rumelhart, 1986), for which the strength and responsibility of a software engineer will be further tested.

## Acknowledgements

While the opinions are those of the author, constructive criticism from academic and industrial colleagues, in particular Professor M.M. Lehman and W.M. Turski, Dr J Kramer and Mrs Jennifer Eastwood of Imperial College, and Messrs. E. Pacello and R.D. Tavendale of GEC Research has been of much assistance.

## References

Abramsky, S. (1989) Domain Theory in Logical Form. Annals of Pure and Applied Logic.

Abrial, J.R. (1980) The Specification Language Z: (1) Syntax and Semantics (2) Basic Library. Oxford Univ. Programming Research Group.

Backus, J. (1978) Can programming be liberated from the Von Neumann style? A functional style and its algebra of programs. Comm. ACM, 21, 613–641.

Balzer, R., Cheatham, T.E. and Green, C. (1983) Software technology in the 1990s: using a new paradigm. In Computer, IEEE Computer Society.

Balzer, R., Goldman, N. and Neches, B. (1984) Specification base computing environments for information management. Proc. Int. Conf. on Data Engineering, Los Angeles.

Bjorner, D. and Jones, C.B. (eds.) (1978) The Vienna Development Method: the meta-language. LNCS, 61, Springer-Verlag.

Boyer, R.S. and Moore, J.S. (1979) A Computational Logic. Academic Press.

Brookes, F.P. (1975) The Mythical Man-month. Addison-Wesley.

Buckle, J.K. (1977) Managing Software Projects. MacDonald and Jane's, London.

Bundy, A. (1983) The Computer Modelling of Mathematical Reasoning. Academic Press.

Burstall, R.M. and Darlington, J. (1977) A transformational system for developing recursive environments. J. ACM, 24, 44–67.

Burstall, R.M. and Goguen, J.A. (1977) Putting theories together to make specifications. Proc. Fifth IJCAI.

Burstall, R.M. and Goguen, J.A. (1981) An informal introduction to specifications using CLEAR. Proc. Int. Summer School on Theoretical Foundations of Programming Methodology. Technical University of Munich.

Burstall, R.M., McQueen, D.B. and Sannella, D.T. (1980) Hope: an experimental applicative language.

Proc. LISP Conf. Stanford Univ., 136–143.

Buxton, J.N. and Randell, B. (eds.), (1969) Software Engineering Techniques. Conf. sponsored by Nato Science Committee, Rome.

Buxton, J. and Stenning, V. (1981) Principles for an Ada Environment (Stoneman). US Department of Defense.

Campbell, I. (1986) PCTE proposal for a public common tool interface. In Software Engineering Environments. I. Sommerville (ed.), ibid.

Clark, K.L. and Darlington, J. (1981) Algorithm classification through synthesis. The Computer Journal, 23, 1.

Clark, K.L. and Gregory, S. (1986) Parlog: Parallel Programming in Logic. ACM TOPLAS, 8, 1.

Codd, E.F. (1970) A relational model of data for large shared data banks. Comm. ACM, 13.

Codd, E.F. (1972) Relational competeness of data base sublanguages. In Data Base Systems, R. Rustin (ed.), Prentice-Hall.

Colmerauer, A., Kanoui, H., Pasero, R. and Roussel, Ph. (1973) Un Systeme de Communication Homme/Machine. Rapport, Group Intelligence Artificielle University d'Aix Marseille Luminy.

Constable, R.L. (1983) Programs as proofs. Info. Processing Letters, 16, 3, 105–12.

Coquand, Th. and Huet, G. (1986) The calculus of constructions. Information and Control.

Cunningham, R.J., Finkelstein, A., Goldsack, S.J., Maibaum, T.S.E. and Potts, C. (1985) Formal requirements specification – The Forest Project. Third Intl. Workshop on Software Specification and Design. IEEE Comp. Society Press.

Darlington, J. and Reeve, M. (1981) ALICE – a multipurpose reduction machine. Proc. ACM Conf. on Functional Languages and Architectures. Portsmouth NH.

DeMarco, T. (1979) Structured Analysis and System Specification. Prentice Hall.

Dick, A.J.J. and Cunningham, R.J. (1986) Using narrowing to do isolation in symbolic equation solving — an experiment in automated reasoning. Proc. 8th Intl. Conf. on Automated Deduction LNCS 230. Springer Verlog.

Dijkstra, E.W. (1972) Structured programming. In Structured Programming O-J. Dahl (ed.). Academic Press.

Dijkstra, E.W. (1976) A Discipline of Programming. Prentice Hall.

Dowson, M. (ed.) (1987) Proc. 3rd Int. Software Process Workshop. IEEE Computer Press.

Eisinger, N. and Ohlbach, H.J. (1986) The Markgraf Karl refutation procedure (MKRP). Proc. 8th International Conference on Automated Deduction, LNCS, 230, Springer-Verlag.

Evans, M.W. (1983) Principles of Productive Software Management. Wiley.

Finkelstein, A. and Potts, C. (1986) Structured common sense: the elicitation and formalisation of system requirements. In Software Engineering 86, Barnes, D.J. and Brown, P.J. (eds.) IEE Computer Series 6 Peter Peregrinus.

Feldman, S.I. (1979) Make - a program for maintaining computer programs. Software-Practice and Experience, 9, 255–265.

Floyd, R.W. (1967) Assigning meanings to programs Proc. American Math. Soc. Symp. on Applied Math, 19.

Goguen, J.A., Thatcher, J.W., Wagner, E.G. and Wright, J.G. (1975) Abstract data-types as initial algebras and correctness of data representations. Proc. Conf. on Comp. Graphics, Pattern Recognition and Data Structure.

Goldberg, A. (1984) Smalltalk-80; The Interactive Programming Environment. Addison-Wesley.

Goldblatt, R. (1982) Axiomatising the logic of computer programming. LNCS 130. Springer-Verlag.

Gordon, M., Milner, R. and Wadsworth, C. (1979) Edinburgh LCF. LNCS, 78, Springer-Verlag.

Gordon, M.J.C. and Herbert, J. (1986) Formal hardware verification methodology and its application to a network interface chip. IEE Proceedings E, Computers and Digital Techniques, 133, E,5

Guttag, J.V. (1978) The algebraic specification of data types. Acta Informatica, 10.

Henderson, P. (ed.) (1987) Proc. Software Engineering Symposium on Practical Software Development Environments. ACM SIGPLAN Notices, 22, 1.

Hoare, C.A.R. (1969) An axiomatic basis for computer programming. Comm. ACM, 12, 10, 666–667.

Hoare, C.A.R. (1972) Proof of correctness of data representations. Acta Informatica, 1, 271–281.

Hoare, C.A.R. (1974) Monitors: an operating system structuring concept. Comm. ACM, 17, 10, 549–557.

Hoare, C.A.R. (1978) Communicating Sequential Processes. Comm. ACM, 21, 8, 666–667.

Jackson, M.A. (1975) Principles of Program Design. Academic Press.

Jeremaes, P., Khosla, S. and Maibaum, T.S.E. (1986) A modal (action) logic for requirements specification. In Software Engineering 86, Barnes, D.J. and Brown, P.J. (eds.). IEE Computer Series 6. Peter Peregrinus.

Jones, C.B. (1980) Software Development: A Rigorous Approach. Prentice-Hall.

Kernighan, B. (1981) The Unix programming environment. IEEE Computer.

Knuth, D. (1974) Structured programming with go to statements. CACM.

Kowalski, R.A. (1979) Logic for Problem Solving. North-Holland Publishing.

Kowalski, R.A. (1979) Programming = Logic + Control. Comm. ACM, 22.

Kowalski, R.A. and Sergot, M. (1986) A logic based calculus of events. New Generation Computing, 4, 1.

Kramer, J. and Magee, J. (1985) Dynamic configuration for distributed systems. IEEE Trans. on Software Engineering, SE-11, 4.

Krieg-Bruckner, B. et al. (1986) Program development by specification and transformation. Proc. Esprit Conf. CEC Brussels.

Lamport, L. and Schneider, F.B. (1984) The 'Hoare logic' of CSP and all that. ACM TOPLAS, 6, 2, 281–296.

Lehman, M.M. (1974) Programming systems growth dynamics. Infotech State of the Art Lectures, 20, 391–412.

Lescanne, P. (1986) REVE - A rewrite rule laboratory. Proc. 8th International Conference on Automated Deduction, LNCS, 230. Springer-Verlag.

Lusk, E., McCune, W. and Overbeek, R. (1986) ITP at Argonne National Laboratory. Proc. 8th International Conference on Automated Deduction, LNCS, 230, Springer-Verlag.

Martin-Loef, P. (1979) Constructive mathematics and computer programming. Proc. 6th Intl. Congress for Logic, Method and Philosophy of Science.

Manna, Z. and Waldinger, R. (1980) A deductive approach to program synthesis. ACM TOPLAS, 2, 1.

McCarthy, J. (1960) Recursive functions of symbolic expressions and their computation by machine. Comm. ACM, 3, 184–195.

McCarthy, J. (1962) LISP 1.5 Programmers Manual. MIT Press.

MacClelland, J.M. and Rumelhart, D. (1986) Parallel Distributed Processing: Explorations in the Microstructure of Cognition. MIT Press.

Milner, R. (1983) A proposal for standard ML. Report of the Dept. of Computer Science, University of Edinburgh.

Montague, R. (1974) The proper treatment of quantification in ordinary English. In Formal Philosophy, Selected Papers of Richard Montague, R Thomason (ed.). Yale University Press.

Mosses, P.D. (1976) Compiler generation using denotational semantics. In LNCS, 45 436–441.

Mosses, P.D. (1979) SIS - Semantics implementation system, manual and user guide. Report DAIMO MD-33, Computer Science Dept., Aarus University.

Nakajima, R., Honda, M. and Nakahara, H. (1980) Hierarchical program specification and verification – a many-sorted logical approach. Acta Informatica, 14, 135–155.

Naur, P. and Randell, B. (eds.) (1968) Software Engineering. Conf. sponsored by Nato Science Committee, Garmisch.

Osterweil, L. (1986) Software Process Interpretation and Software Environments. Department of Computer Science Report CU-CS-324-86, University of Colorado, Boulder, USA.

Parnas, D.L. (1972) On criteria to be used in decomposing systems into modules. Comm. ACM, 15, 1053–1058.

Pnueli, A. (1986) Specification and development of reactive systems. Proc. IFIP Congress.

Potts, C. (ed.) (1984) Proc. Software Process Workshop. IEEE Computer Society.

Redwine, S.T., Seigel, E.R. and Berglass, G.R. (1981) Candidate R&D Thrusts for the Software Technology Initiative. United States Department of Defense.

Reid, P. and Welland, R.C. (1986) Project development in view. In Sommerville (ed.) Software Engineering Environments, IEE Computer Series 7, Peter Peregrinus.

Ritchie, D.M. and Thompson, K. (1978) The Unix time-sharing system. BSTJ, 57, 6, 1905–1929.

Siegel, E.R. (1982) Summary of Responses to the Software Technology Initiative Questionnaire. Report of The MITRE Corporation, McLean, Virginia.

Scott, D.S. and Strachey, C. (1971) Towards a mathematical semantics for computer languages. Proc. Symp. Computers and Automata. Polytechnic Press.

Sommerville, I. (ed.) (1986) Software Engineering Environments, IEE Computing Series 7. Peter Peregrinus.

Stephens, M. and Whithead, K. (1985) The Analyst – a workstation for analysis and design. Proc. 8th Intl. Conf. on Software Engineering. IEEE Comp. Soc. Press.

Stoy, J.E. (1977) Denotational Semantics: The Scott-Strachey Approach to Programming Language Theory. MIT Press.

Talbot, D.E. (1986) Software Engineering. In The Alvey Programme Annual Report. The Alvey Directorate, London.

Talbot, D.E. and Witty, R.W. (1983) Alvey Programme: Software Engineering Strategy. The Alvey Directorate, London.

Tannenbaum, A. and van Renesse, R. (1985) Distributed operating systems. ACM Computing Surveys, 17, 4, 419–470.

Turner, D.A. (1985) A non-strict functional language with polymorphic types. In Functional Programming Languages and Computer Architecture, J.P. Jouannaud (ed.), LNCS, 201, Springer-Verlag.

Wand, M. (1985) From interpreter to compiler: a representational derivation. In Proc. Workshop on Programs as Data Objects, LNCS 217, Springer-Verlag.

Waters, R.C. (1985) The programmer's apprentice: a session with KBEmacs. IEEE Trans. on Software Eng., SE-11, (Nov.)

Wilden, J.C. and Dowson, M. (eds.) (1986) Proc. 2nd Int. Software Process Workshop. ACM Software Engineering Notes, 11, 4.

Wirth, N. (1971) Program development by stepwise refinement. Comm. ACM, 14, 4.

Wirth, N. (1973) Systematic Programming: An Introduction. Prentice-Hall.

## Biographical notes

Jim Cunningham is a graduate of Melbourne University and a Senior Lecturer in the Department of Computing at Imperial College where he has been closely associated with the development of teaching and research into Formal Methods in Software Engineering. He has been a leader of the Alvey Forest and Esprit Formast projects and instrumental in research aimed at productive use of Mechanised Deduction in Software Engineering. This is now being pursued through a new Esprit Basic Research Action on Mechanised Deduction in the Logics of Practical Reasoning.

Address for correspondence: Department of Computing, Imperial College, London SW7 2BZ.

![](/api/attachments/H5NCJHG8/fulltext/images/b2fadbc2410830d2483b9c3cb5ee936767f774f97fcd86df320fce61e96c2971.jpg)
