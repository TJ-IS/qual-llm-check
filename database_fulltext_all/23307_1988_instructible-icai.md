---
otero_id: 23307
otero_key: "EXSJQ7Y3"
title: "Instructible ICAI"
authors: "P Duchastel; S Doublait; J Imbeau"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.31"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Instructible ICAI\*

P. Duchastel, S. Doublait and J. Imbeau, Faculté des Sciences de l'Education, Université Laval, Quebec

## Introduction

This paper is structured in two sections. In the first section, we present the rationale for instructible ICAI by considering the scope for this aspect of ICAI systems. In the second section, we discuss our current work in providing the GEO tutor with the capability for augmenting its knowledge base through interactions with its users.

## The scope for instructible ICAI

Intelligent computer-assisted instruction (ICAI) systems constitute an applied domain of artificial intelligence which shows much promise not only for extending the range of learning resources made available to students and trainees, but also for refining and formalizing our intuitive conceptions of teaching. Just as the development of expert systems has created unprecedented interest in AI on the part of many user communities, including business, medicine and government, it can be expected that continued development of the ICAI field will lead to very high interest in the educational and training communities.

At present, however, ICAI systems are far from offering the practical applications which will eventually be expected from them. Past and current ICAI systems, such as those surveyed in Sleeman and Brown (1982), remain experimental prototypes which explore various factors involved in teaching through heuristic computational procedures, and which serve mainly to demonstrate the potential eventually sought rather than current feasibility in instructional settings. Few systems are simple enough or efficient enough to be seen as implementable in practice (one positive example, however, is Anderson's LISP Tutor (1985) which has recently been offered on the market). On the whole, ICAI remains very experimental, with many different approaches being tried out in prototype development work.

This is certainly a healthy state of affairs in such an open field as computer-based teaching, although one of its associated costs is that there is often little follow-up once an initial system is developed. The problems encountered in designing a system lead the researchers on to designing new systems which address further concerns in new situations. The older systems are left aside as new interests are pursued in other directions.

The problem with keeping systems going is partly due to various practical difficulties inherent in the systems themselves and their implementation context, but also due in our view to the lack of ease with which the systems can be maintained and upgraded. This is the price paid by the handcrafting required for experimental work. The expert systems technology is largely being widely adopted today because it involves a formalism which is easily used by professionals without the expertise needed for handcrafting complex systems. Expert systems can be built and upgraded relatively easily because the knowledge on which the systems run can be input in a fairly straightforward manner. Even if knowledge engineering (especially the extraction of expertise from knowledgeable people) remains somewhat of a bottleneck, the input process itself is not a problematical one when the knowledge base is relatively small. The input of knowledge into an ICAI system, in contrast, is a major undertaking. This leads us to the view that the design of means through which the initial knowledge base of an ICAI system can be gradually augmented will greatly facilitate the maintenance and eventual potential for practical implementation of the system. This in fact means that an ICAI system must be instructible, i.e. that it can profit from interactions with persons other than its designers.

Carbonell (1970), in designing the very first ICAI

## Context

system (SCHOLAR), foresaw the desirability of such a feature and proposed (but did not implement) a conversational program to assist a teacher in inputting additional knowledge to the system. SCHOLAR's knowledge base contained facts about the geography of South America and thus constitutes a domain of discourse which is certainly extensible. The following teacher-computer simulated dialogue illustrates what was sought (teacher input follows double asterisks):

<table><tr><td>Name of unit:** Chile</td></tr><tr><td>Part of speech:** XN</td></tr><tr><td>Superconcept, please:** Country</td></tr><tr><td>In what continent is Chile?** South America</td></tr><tr><td>More about the location of Chile?** No</td></tr><tr><td>Name of unit:** Cordoba</td></tr><tr><td>Superconcept, please:** Province</td></tr><tr><td>Undefined. Do you want to define it now?** Yes</td></tr><tr><td>Part of speech:** CN</td></tr><tr><td>Superconcept, please:</td></tr></table>

The great advantage here is that it is a teacher who interacts with the system, and not the AI specialist who designed the system. As we all know, there are more of the former in the world than there are of the latter.

SCHOLAR's instructible facility remained but a proposal, yet its feasibility does not seem problematical. Indeed, the dialogues supported by current instructible knowledge-based systems, such as KLAUS (Haas and Hendrix, 1983), are very similar to the one illustrated above. In fact, the task of creating front-ends to knowledge bases which can augment their vocabulary and their conceptual base itself is an active area of research subsumed under machine learning (even if 'learning from being told' is perhaps less difficult than other forms of learning such as inductive and analogical learning). Yet another well-known acquisition interface is TEIRESIAS (Davis and Lenat, 1982), which assists computationally naive users (experts in their own speciality, however) in upgrading the set of rules included in an expert system (MYCIN in this case). TEIRESIAS illustrates in particular that the natural language component need not necessarily be sophisticated, although one would not want to generalize too much from that.

A prototypical ICAI system is generally considered to involve four components, as follows:

\- a knowledge base, which contains the knowledge or expertise to be taught;

\- a tutorial model, which guides the instructional session by applying its tutorial rules;

\- a student model, which constantly updates a particular student's status with respect to the knowledge base (unknown facts, misconceptions, unused skills ...);

\- a user interface, often involving a natural language capability, which allows the learner to interact fairly freely with the system.

The latter two components, while they are essential features of an ICAI system, do not share the general importance or extensibility of the first two. The knowledge base contains what to teach and the tutorial module contains the strategies regarding how to teach it. Both can encapsulate knowledge in a declarative form and both are thus extensible. It is these two components of an ICAI system which are instructible.

## Domain knowledge

The domain knowledge of a system can be augmented or refined through interactions either with mentors or with students. Carbonell had foreseen interactions of the first type for the SCHOLAR system: specialists in geography would be called upon to augment the facts known to the system, thereby providing an increasingly larger knowledge base for the students to interact with. With respect to expert systems, TEIRESIAS has a similar approach in that medical experts are called upon to refine the rule base of the MYCIN system.

Interactions with students constitute another means through which the knowledge domain of a system can be augmented or refined. Kimball's calculus tutor (1982), which contained symbolic integration heuristics, is a case in point. The initial set of solution heuristics had been introduced into the system by the designer and were based on his own mathematical experience. The system, however, also contained a capability to recognize superior problem solutions (those involving fewer steps) made by the students and to replace the initial ones by the latter ones where appropriate. The system thus learned from the spontaneous discoveries of some of the students with whom it interacted.

A system we are currently designing to teach Canadian geography is also instructible via interactions with students. The system (GEO) is similar to SCHOLAR in that it supports a mixed-initiative dialogue through which either the student or the system can query the other. The type of interaction which is sought is illustrated below (student input follows double asterisks):
What is the capital of Ontario?
\*\* Toronto
What is its population?
\*\* Where is Kingston
I do not know. What is Kingston?
\*\* A city
O.K. In what province is Kingston?
\*\* Ontario
O.K. Do you know its size?
\*\* No. Let's talk about Alberta.
Fine. What are its major cities?
\*\* Calgary
Yes, and another one?
\*\* -
Edmonton. Which one is the capital?

The geographical facts known to the system will always be limited, but since most people with whom the system will interact will be experts of sorts on their own local geography, it will learn these particulars from them in addition to teaching them about other areas of the country. The GEO system is considered in more depth in the second part of this paper.

## Teaching strategies

In both the calculus tutor and GEO, it is the domain knowledge of the system which is extensible, not its knowledge about teaching. This latter knowledge, however, also constitutes an aspect of the system which is potentially instructible, as was demonstrated by O'Shea's quadratic equations tutor (1979) which led students to discover how to solve equations.

The system's tutorial strategy encapsulated a number of rules which were triggered by the particulars of the current state of the student's knowledge (in the student model) and which directed the system in setting the task difficulty, the order of examples, the extent to which it tested various hypotheses, the nature of prompting, etc.

The system monitored a number of efficiency factors such as post-test scores (over a number of students), time spent in learning, etc. and could thus determine how well it was doing as a teaching system. With this basic ability, the system could experiment with various rule modifications (i.e. slightly modify its teaching strategy) and assess whether it was doing better or worse. It did in fact try modifications which paid off, while others did not. What can be gained here is, of course, limited by the nature of the initial strategy, for the system cannot invent new rules; it only alters the operation of its initial rules, thereby (it is hoped) refining its tutorial strategy.

Our current understanding of tutoring remains limited and tutoring itself may well be very task-bound, such that general strategies may remain an ideal rather than become a reality. That being the case, any self-improving ability of a tutorial system is likely to pay high dividends. If we cannot predict, let us at least experiment and learn from that experience.

## Conclusions

In summary, ICAI systems contain two knowledge components which may be augmented or refined through their interactions with users: their domain knowledge and their teaching knowledge. Both constitute a potentially powerful aspect of instructible ICAI, although self-improvement in the system is brought about in different ways.

In the first case, the limited knowledge base of the system (what it teaches) is extended through instructive interactions with mentors or with the students themselves. The relatively straightforward ability to thus learn from being told shows much promise for the maintenance and practical long-term viability of the system. One problem with such learning, which was not discussed here but which will eventually need consideration, concerns the validity of the knowledge thus acquired, for a knowledge base with even a small amount of rubbish in it will be shunned by potential users and could hardly be recommended as a teaching vehicle. This difficulty is probably not insuperable, however, and solutions may well borrow from experience with expert systems, the maintenance of which share an analogous concern.

In the second form of instructible ICAI, the system seeks through experimentation and the accumulation of experience to refine its tutorial strategies (how it teaches). The users of the system are needed as much here as in the first case, although their role changes altogether: here they indirectly provide valuable learning data to validate experimental modifications to the tutorial rules of the system. Such experimentation is greatly needed, given our lack of clear theoretical models to guide our design of tutorial strategies. Here again also, an instructible ICAI system cannot be left totally on its own to concoct its own variant of a teaching strategy. External monitoring will be required to avoid awkward modifications with spurious results.

Despite these unsolved problems, instructible ICAI is seen as a powerful aid to reduce the bottleneck of knowledge input to a tutorial system. The extent to which the examples provided here are generalizable to other domains remains, of course, to be seen.

What we are likely to see over the next decade is the development not only of additional systems along these lines, but probably also new ideas for extending and improving the instructibility of ICAI. Much will probably be gained in this respect from the theoretical and practical efforts in the currently active field of machine learning (Michalski, Carbonell and Mitchell, 1986).

## Current research on GEO

GEO is an ICAI learning environment which aims to increase the student's knowledge of Canadian geography (Duchastel, 1986a; Doublait and Duchastel, 1987). Like SCHOLAR (Carbonell, 1970; Collins et al., 1975) — its predecessor and model in a number of ways — GEO does this through a mixed-initiative dialogue in which control of the learning interaction is mostly in the hands of the student. GEO goes further in this direction, however, and it is one of the research issues which are examined in the project to determine how learner control can be put to best use in learning situations involving mostly declarative knowledge.

A second important research issue in GEO, concerns how the knowledge base of the system can be augmented during interactions with students. This is a form of machine learning termed 'learning from being told' (Michalski et al., 1983), and although such knowledge augmentation is more straightforward than other forms of machine learning, many practical issues need to be addressed.

Even though GEO contains tutorial heuristics, it constitutes principally a learning environment in which students are free to explore geography in a very open-ended manner, according to their own particular interests and whims of the moment. Thus, it is less a teaching system than a learning environment, and reflects in this sense much of the spirit of ICAI.

The knowledge domain of GEO is a factual one (like SCHOLAR's); this places it somewhat apart from most recent efforts in ITS design, which have been concerned mainly with structural and procedural knowledge, as well as with the development of particular skills and reasoning strategies in problem-solving contexts. It is often implied that computer power is best suited to these higher forms of learning and that traditional CAI techniques can adequately teach factual knowledge. While that is partly true, we must not forget that the main disadvantage of CAI lies in its inability to provide learner control. That is the principal strength of ICAI (Duchastel, 1986b), whether in domains of factual knowledge or domains involving other forms of learning. The optimal degree of learner control in a given situation is an open research question, and the GEO project hopes to provide some indications in this respect.

As learning opportunities become less institutionalized and more informal (push being replaced with pull) (Brown, 1983), learning systems will become more global and varied. A system such as GEO will eventually involve not only a core mixed-initiative dialogue component, but also other more traditional components such as short CAI modules on specific topics (e.g. the capitals of the 10 Canadian provinces), videodisc sequences on particular cities or regions, and instructional games involving geographic knowledge. The aim is to provide a global environment for students to explore, while leaving principally with them the choice of how to proceed.

The core component of GEO involves a standard ITS architecture (Woolf and McDonald, 1984);

1. a domain knowledge base organized as a semantic net with which are associated various inferencing procedures;

2. a student model which tracks student progress and dynamically determines student status with respect to instructional objectives;

3. a tutorial module which seeks tutoring opportunities within the learner-controlled setting and which handles responses to the student in an adequate manner;

4. a communication module which interprets student input in a natural language form.

## An acquisition dialogue

The potential for acquisition in GEO lies in the fact that all users of the system (whether students or other users) know specific facts about their own particular region. If users are natives of Edmonton in the province of Alberta, they will generally have quite a bit of specific knowledge about Edmonton and about Alberta, even if their knowledge of other parts of Canada may be limited. The system's knowledge, likewise, is always limited: while it may know the principal facts concerning the major cities and regions in Canada, as well as specific facts about particular cities we will have told it about, there will always be places and characteristics it will not know about. Thus, the task of the acquisition module is to recognize unknown places and to engage users in a dialogue through which it can learn new facts from them.

The nature of this task can be best gleaned from an illustrated dialogue representing the type of interaction GEO will soon handle. In the following illustration, student input is preceded by double asterisks:

\*\* Let's talk about Western Canada. Fine. What is the capital of British-Columbia?

## \*\* Vancouver

No, the capital of British-Columbia is Victoria. Where is Victoria situated?

\*\* Let's discuss Banff.

I do not know Banff. Is Banff the name of a place?

\*\* Yes. It is a town.
Where is Banff located?

\*\* In the Rocky Mountains
Is Banff in British-Columbia or in Alberta?

\*\* In B.C.

What is the population of Bar f?

\*\* 5000.
What other towns are near B unff?

\*\* Tell me about Victoria.

Victoria is situated on Vancouver Island. It is the second largest city in British-Columbia. What else would you like to know?

\*\* What is its population?

The characteristics of the above dialogue are the following:

\- the student is always in control of the interaction;

\- the system is not only responsive, but can also question the student in order to give gentle direction towards certain learning objectives;

\- an acquisition routine is activated when the student mentions a place either unknown or only partially known to the system (and once the student confirms that it is indeed a place).

The dialogue illustrated above will require further tuning before GEO can be considered satisfactory, and even then problems are sure to be present. One purpose of the GEO project is precisely to explore the nature of these problems and to seek solutions to them.

## Research issues

The principal research issues are to be found at the specific level of the acquisition dialogue and concern the very nature of the interaction. Which questions are to be asked by the system? How many can be asked before the student tires of this intrusion? How will these intrusions be perceived? When should acquisition take place and when should it not? These issues interact with the tutorial heuristics of the system and will be clarified only as development work progresses and practical experience is gained through usage of the system.

At the moment, the acquisition routine of GEO is activated whenever the system encounters a word in the student's input which it does not recognize and which it suspects might be the name of a place. For instance, GEO recognizes all the words but the last in the following question from the student:

\*\* What is the population of Charlesbourg?

The fact that the question contains a geographical concept (population), but no associated name place activates the following response:

I do not know the word Charlesbourg and I assume that it is the name of a geographical place. Is that correct?

If the student replies in the affirmative, the acquisition routine is activated with Charlesbourg as its focus.

Our first approach for acquisition was algorithmic: the routine stepped through a series of conditional questions requesting information from the student, such as whether the focus was a city; if so, which province it was situated in, what its population was, and so on.

These conditional questions were activated with respect to students' answers to previous questions, assuming the fact that, for instance, if the students could not answer a quite simple question, they could not answer more difficult ones. The branching to questions also depended on students' sophistication (initially based on age) and the nature of the place to learn (city, province, lake, etc...).

This algorithmic approach works well, but it is bulky since it does not make use of GEO's knowledge of geographical concepts. Our current approach is knowledge-based and thus much more generalizable.

GEO contains knowledge about geographical concepts, such as the fact that the appropriate features of a province are its location, its neighbouring provinces, its population, its capital etc. . . . These features are specific to the concept and would not apply to another concept (for instance, a city has no capital, but it may well have suburbs, etc. . . .). What GEO does is to use these features in deciding which questions to ask of the student. The acquisition questions are thus tailored to the type of geographical concept involved and do not require a complex branching process of the algorithmic sort.

With respect to how far to go on questioning students about a new place, other decision rules are required. Indeed, students may well be quite familiar with the place, in which case detailed questions can be asked. However, if they know little of the place (and answers to the initial questions will reveal this), there is little point in delving into details. We are currently exploring the factors which go into this sort of decision-making on the part of the system.

Yet another set of decision processes which occupy our attention are those related to the timing of acquisition. If a student is in the middle of a conversation with GEO about a particular place (say the province of Alberta), it may not be appropriate just then to intrude with secondary questions concerning a new place the student has mentioned. It may be better to wait for a more opportune moment. This aspect of the acquisition process implicates general decision-making at the level of the overall dialogue and relates to the question of learner control mentioned earlier. The design of GEO is still not yet very advanced in this respect, although we hope to tackle this issue soon.

One of the acquisition issues currently being addressed concerns the accuracy and coherence of the knowledge base. As novel information is provided by the student, this information is added to the existing knowledge base and is thus available to other students when they in turn interact with the system. But what about misinformation? Users could enter information even if they are not quite sure of the information (as in the illustration above: the population of Banff is actually closer to 3000 than to 5000). Even worse, users could deliberately enter misinformation just to fool around ('The population of Banff is 25 million'). GEO will generally have few means of checking the coherence of the new information with respect to its existing knowledge (an interesting research issue in itself) and will therefore have to rely on external verification for the accuracy of new knowledge.

What GEO currently does is to augment its knowledge base with the new information, but at the same time keep track of all new information provided by a user. Any time the system designers later interact with GEO, a verification routine is activated so that the new information can be examined and corrected if need be. Such a mentor role for GEO will always be required if misinformation is not to render the system useless for instructional or any other purpose. However, in the meantime (before the information is in fact verified), GEO does use the new information if needed, although with proper notice to the student:

\*\* What is the population of Banff?

I have been told that it is 5000.

Whether this strategy (which is currently implemented) will continue to prove practical or not will be determined with use.

## Conclusions

As can be gleaned from our above discussion of GEO, the research issues involved in the acquisition of declarative knowledge for an ICAI system are not simple, although we believe them certainly to be tractable. Some issues concern dialogue regulation, some relate to the psychology of the interaction, and others to the coherence of the knowledge base. All are important issues in as much as we are aiming for a practical system to be used by students. Our work in this sense is very applied, yet it touches upon deep concerns in AI.

GEO is a particular type of ICAI system. The type of knowledge it deals with and its emphasis on learner control provide us with problems and solutions which we believe will become of more and more interest as AI continues to inform work on user-system interfaces. Instructible ICAI is in this respect part of a larger domain concerned with user interactions with knowledge-based systems.

## References

Anderson, J.R. and Reiser, B. (1985) The LISP tutor. BYTE, April, 159–175.

Brown, J.S. (1983) Learning by doing revisited for electronic learning environments. In M.A. White (ed.) The Future of Electronic Learning. Lawrence Erlbaum Associates, Hillsdale, N.J.

Carbonell, J. (1970) AI in CAI: an artificial intelligence approach to computer-aided instruction, IEEE Trans. MMS 11, 190–202.

Collins, A., Warnock, E., Aiello, N., and Miller, M. (1975) Reasoning from incomplete knowledge. In D. Bobrow and A. Collins (eds.) Representation and Understanding. Academic Press, New York.

Davis, R. and Lenat, D. (1982) Knowledge-Based Systems in Artificial Intelligence. McGraw-Hill, New York.

Doublait, S. and Duchastel, P. (1987) Vers un système tutoriel intelligent: Le système GEO. Proceedings of the Colloque Québécois en Informatique Cognitive des Organisations, Montréal, Canada, June.

Duchastel, P. (1986a) The design of an adaptive geography tutor. Document DR 86–14. Laboratoire d'Intelligence Artificielle en Education, Université Laval, Québec, Canada.

Duchastel, P. (1986b) Intelligent computer-assisted instruction systems: the nature of learner control. Journal of Educational Computing Research, 2, 379–393.

Haas, N. and Hendrix, G. (1983) Learning by being told: acquiring knowledge for information management. In R. Michalski, J. Carbonell and T. Mitchell (eds.) Machine Learning: An Artificial Intelligence Approach. Tioga Publishing, Palo Alto.

Kimball, R. (1982) A self-improving tutor for symbolic integration. In Sleeman and Brown (eds.) Intelligent Tutoring Systems. Academic Press, New York.

Michalski, R., Carbonell, J. and Mitchell, R. (1986) Machine Learning: An Artificial Intelligence Approach, Vol. II. Morgan Kaufmann, Palo Alto.

O'Shea, T. (1979) Self-Improving Teaching Systems. Birkhauser Verlag, Basel.

Sleeman, D. and Brown, J.S. (eds.) (1982) Intelligent Tutoring Systems. Academic Press, New York.

Woolf, B. and McDonald, D. (1984) Building a computer tutor: design issues. Computer, September, 61–73.

## Biographical notes

Dr Philippe Duchastel has been involved in information technology since the 1970s, when he was working in distance teaching at the Open University in Great Britain. He is currently building ICAI prototypes and exploring modes of learning as people interact with information-rich systems in educational and training settings.

Stephan Dublais is a graduate in computer science from Laval University. His interests lie in artificial intelligence.

Dr Jacques Imbeau has a background in physics. He has been involved in computer-assisted learning for a number of years and is currently exploring ICAI possibilities in physics.

Address for correspondence: Laboratoire d'Intelligence Artificielle en Education, Faculté des Sciences de l'Education, Université Laval, Quebec G1K 7P4, Canada.
