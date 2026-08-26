---
otero_id: 18595
otero_key: "K9NRFQ6F"
title: "Software methodologies for decision support"
authors: "Alfs T. Berztiss"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90024-c"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software Methodologies for Decision Support

Alfs T. Berztiss

Department of Computer Science, University of Pittsburgh, Pittsburgh, PA 15260, USA and SYSLAB, University of Stockholm, Sweden

Automation of complex decision-making processes in business enterprises depends on the satisfactory solution of two major problems: the management of unreliable data and the cost-effective introduction of expert systems. This paper shows that there exist appropriate frameworks to support the solution of both problems, and suggests ways in which practical software methodologies can be developed within these frameworks. It also indicates where additional research is required.

Keywords: Expert Systems, Modularization, Object Orientation, SF, Unreliable Data.

![](/api/attachments/K9NRFQ6F/fulltext/images/56cd101bec0b7da85c27afaaed96512669f5c27b860d2fe2e82ae1cf3715521d.jpg)

Alfs Berztiss has been doing teaching and research in computer science and software engineering for the past 30 years. He is the author of the book Data Structures: Theory and Practice, and of many technical papers. Currently he belongs to the faculty of the University of Pittsburgh and is also a research associate of the University of Stockholm. He has given courses and been a consultant with numerous universities and other enterprises, including IBM and SEI. He is a Fellow of the Australian Computer Society, and belongs to ACM, IEEE Computer Society, European Association for Theoretical Computer Science, and IFIP Working Group 8.1 (Design and Evaluation of Information Systems). His research interests include specification and prototyping languages for software, visual programming, application of artificial intelligence techniques in software engineering, and curricula for education in computer science and software engineering.

## 1. Introduction

We first distinguish between a data base, an information base, and a knowledge base. Here a data base is simply a collection of facts. In an information base the data become interpreted by the imposition of constraints, but all the data are still “hard”; i.e., we regard them as reliable, irrespective of whether they are stable (e.g., a person’s Social Security number), or change more or less frequently (e.g., overtime worked by a person in the past week). Now, if we were to rely exclusively on reliable data, much of what is identified as intelligent behavior in humans would stop. Therefore, the admission of “soft” data into a system promotes an information base to a knowledge base. Note that an inference making capability does not differentiate between information and knowledge bases: it is a necessary component of a knowledge base management system, but it may be provided by an information base management system as well.

Although much is currently written about the transformation of information bases into knowledge bases (see, e.g., [8]), the fundamental difference of dealing with reliable data alone or with data known to be wholly or partially unreliable prevents a smooth transition from one to the other: while the essence of management of an information base is a conservative attitude to what may be admitted to the information base, the essence of management of a knowledge base is a liberal attitude. We classify unreliable data, survey existing methods for dealing with such data, and show that object orientation can help to combine data belonging to different classes of uncertainty, and thus promote the transition from information bases to knowledge bases.

Routine business decisions often take up time that would be better spent on strategic planning.

This has created considerable interest in expert systems, but comparatively few expert systems do, in fact, support day-to-day operation of business enterprises [37]. Part of the reluctance by management to commit resources to the introduction of expert systems is due to the lack of procedures for determining which business activities could be taken over by expert systems, and for establishing the cost-effectiveness of such changes. A methodology is described for incremental cost-effective replacement of manual decision-making functions by expert systems.

## 2. Categories of unreliable data

Unreliability can manifest itself in many ways. We first list the classes of unreliable data, and then survey the literature to show that there exist techniques for drawing inferences from such data.

1. Straight-out contradictions. Suppose that the budget deficit of Ruritania just keeps growing. One economist suggests lowering taxes as the cure, while another suggests raising them.

2. Permanent exceptions. A well known example arises with the statement "All birds fly"; of course, penguins and emus do not.

3. Temporary exceptions. A data base constraint may state that all vice-presidents have offices on the ninth floor. Ms. Smith has just been made vice-president, but there has not yet been time to move her office.

4. Limited validity. Mr. Brown rents a room from Mrs. Jones. Mr. Brown has no personal telephone, but, since he has access to Mrs. Jones's telephone, he can be considered as having a phone.

5. Multiple options. People often have several addresses, each being used for some different purpose, such as home, office, etc.

6. Obscurity. There may be a trend in the values of data collected over a period of time, but it may be obscured by seasonal variations; e.g., monthly income at a resort.

7. Fuzziness. We designate Mr. Smith as tall, but tallness is not a well defined property. Hence we have to introduce a tallness index, which would be interpreted differently for different groups of people (what is tall among six year olds may be short among sixteen year olds).

8. Vagueness. In the statement "All smaller boats should be taken out of the water in the autumn" the term "smaller" is fuzzy, but "autumn" is vague. The time span officially designated as autumn may not be intended here.

9. Faults. An electric utility meter breaks down, and is unable to supply information. Here it may be important to know when the meter broke.

10. Either/or uncertainty. If the electric utility meter continues to register the same value over a period of time, it may be working, if the customer is away on a trip, or it may be broken. Also, the rumor “Company X will show a loss this quarter” may be true or false, but we do not know which.

11. No knowledge as negation. In logic programming, the absence of a fact X from the data base implies not(X). For example, if the data base does not contain the fact “Mr. Khachaturian is married”, and the fact is not derivable from, say, “The husband of Ms. Khachaturian is Mr. Khachaturian”, the answer to the query “Is Mr. Khachaturian married?” will be “no”. This interpretation, known as the closed world assumption, is common in data base semantics.

12. Interpretation uncertainty. In 1960, France changed from old to new francs. An amount of money relating to expenditures made at about that time may be expressed in either currency. Similarly an age may indicate age last birthday, or age next birthday, or age nearest birthday.

13. Rounding. Is \$5,000,000 an exact or a rounded amount? This becomes grotesque when an Australian newspaper changes “The tornado damage around Someplace, Oklahoma is estimated at \$5,000,000” to “The tornado damage around Someplace, Oklahoma is estimated at \$A6,841,817.”

14. Noisy data. An experimentally determined value is nearly always uncertain, e.g., the speed of light.

15. Partial knowledge. Four prisoners escape. Their names are known. Now they split into two groups of two. We can tell that the two in a particular group are a subset of the four, but may not be able to be more precise.

Methods for dealing with some of the categories of unreliable data were devised by statisticians well before the computer era. The use of expected values and measures of centrality (mean) and dispersion (variance) with noisy data, and of time series analysis to deal with seasonal variations, are just a few relevant statistical techniques.

Much of the work on fuzziness derives from Zadeh's fuzzy set theory [39]. Fuzzy systems have been thoroughly explored in this framework, and fuzzy logic is well developed [14,20,21,33]. Approaches to fuzziness without particular emphasis on fuzzy set theory are surveyed by Nilsson [28]. Exceptions have been studied by Borgida [5,6]; of particular interest is an investigation of exceptions in object-oriented systems [6]. He also refers to the classes of unreliability that we call multiple options and faults. Exceptions with respect to inheritance have been studied by Etherington and Reiter [15], and inheritance of statistical properties by Rowe [32].

Conflicting evidence can be dealt with by the technique of endorsement [12]; support logic programming [2] is a similar approach. Negation and the closed world assumption have produced much literature – for some examples see [26,27]. A recent survey of non-monotonic reasoning can be found in [29]. An excellent bibliography on default knowledge is provided by Yager [38]. Integration of knowledge from different sources that may be contradictory is covered in [18].

Uncertainty has been studied specifically as it affects information systems: in the context of the entity-relationship model $[40]$ , nonmonotonic logic and data bases $[7]$ , probabilistic approaches to uncertainty in data bases $[19]$ , and adaptation of data models to uncertain situations $[11]$ .

## 3. Modularization in information systems

Every information system relates entities to other entities, and it is only natural to group these entities into sets. Thus, in discussing personnel, the sets are employees (or, more broadly, persons), salary values, dates (of hiring, retirement, etc.), and so forth. These sets, together with operations appropriate to them, define data types. The identification of data types with modules has become a basic principle of good programming practice, but it is not as yet fully established in information system methodology.

Let us consider the specification of a module or segment of an information system. We shall write it in the SF (Set-Function) specification language [3], but any one of a number of similar approaches could have been chosen [1,16,17,23,31]. Besides these works, SF has a strong resemblance to the functional data model [35,34]. An SF segment has three components:

\- a schema definition,

\- specifications of events,

\- a responder that consists of transactions.

The schema definition identifies a set of interest in the segment, and a set of functions (finite maps), which, for the most part, have the set of interest as their domain. In this we deal with a conceptual level, i.e., our concern is the concept of person, say, and not deliberations of whether to represent a person by a name or a number. Our example relates to an establishment that hires out boats.

The set of interest is that of boats (B), which is partitioned into the subsets of registered (R) and deregistered (DR) boats; the latter are no longer in use, i.e., have been scrapped. The set of registered boats is partitioned into boats that are free (F), hired (H), overdue (OD), requiring their seaworthiness to be checked (C), or in maintenance (M), SF permits property inheritance. Thus the type of boats is a subtype of water vehicles and hire objects. A secondary type S\~ code merely defines a finite set of values; this type is not sufficiently important to have its own segment.

The functions serve the purpose of answering queries. For example, Latest\~hire indicates the time at which the latest hiring event took place for the given boat. The set-valued function $H^{~set}$ returns a set of triples indicating, for each regular hiring event, the date and time it took place, as well as the length of time that the boat had been out, and functions $OD^{~set}$ and $INSP^{~set}$ maintain similar histories of the times the boat has been overdue or inspected for seaworthiness. Answers to very complicated queries can be constructed from this information.

These functions require the importation into the segment under consideration of several predefined types. Type $T^{\sim}$ min is assumed to contain function $T^{\sim}$ min. Now that returns the current time with a resolution of one minute, and the other types also contain appropriate functions. The set of type $T^{\sim}$ dur\~min consists of time durations measured in minutes. It is only a coincidence that all three of the imported types relate to time.

```txt
An abridged schema definition for the segment Boat~hire:
IMPORTED TYPE T~min ENDTYPE;
IMPORTED TYPE Date ENDTYPE;
IMPORTED TYPE T~dur~min ENDTYPE;

TYPE Boat ISA Water~vehicle ISA Hire~object;

SET- B (SUBSETS: R (SUBSETS:
F, H, OD, C, M), DR);
SECONDARY TYPES-
S~code = {"ok", "repair", "scrap"};
FUNCTIONS-
Latest~hire: R → T~min;
H~set: B → (Date × T~min × T~dur~min)-set;
OD~set: B → (Date × T~min)-set;
INSP~set: B → (Date × T~min)-set;
... ... ...
... ... ...
ENDTYPE;
Notation: X-set stands for the power set of X;
ISA may be read as "is a".
```

The specification of events consists of preconditions and postconditions. Preconditions determine under what circumstances an event may take place. They serve as a check on the feasibility of input values, and embody consistency criteria for the data base of the information system. Postconditions are subdivided into setconditions and mapconditions that indicate the changes that sets and maps undergo as a consequence of an event taking place, and sigconditions that send signals to the responder in the form of raised flags. Postconditions are assertions rather than assignments. The operational interpretation of a postcondition is the minimal modification of the data base that makes the assertion hold.

Continuing with the example of the enterprise that hires out boats, the majority of the events move boats from one subset into another. Some such events are Hire (which moves a boat from subset F to subset H); Return (from H to F); Mark\~o\~due (from H to OD, applied to all boats that have not been returned after the establishment closes for the night). Event Mark\~o\~due differs from the others in that it is initiated by the system itself. We call such events internal. Events may exercise control by means of sigconditions. For example, when a boat is taken out of service by event Request\~inspection, the sigcondition Check\~condition asks the responder to initiate an inspection of the boat. Only some of the events of

```matlab
the complete segment Boat~hire are listed here:
EVENT Hire(b: Boat);
(* Assume hiring hours between 9:00 and 20:00.
A primed quantity indicates a value after the event, an unprimed quantity a value before the event. *)
PRECONDITIONS-
Member(b, F);
T~ min.Now ≥ 09:00;
T~ min.Now ≤ 20:00;
SETCONDITIONS-
F' = F - {b};
H' = H ∪ {b};
MAPCONDITIONS-
Latest~hire'(b) = T~min.Now;
ENDEVENT;

EVENT Return(b: Boat);

DEFINITIONS-
t~ dur: T~min.Now-Latest~hire(b);
PRECONDITIONS-
Member(b, H);
SETCONDITIONS-
H' = H - {b};
F' = F ∪ {b};
MAPCONDITIONS-
H~set'(b) = H~set(b) ∪
{<Date.Now, Latest~hire(b), t~dur>}};
ENDEVENT;

INTERNAL EVENT Mark~o~due(b: Boat);
SETCONDITIONS-
H' = H - {b};
OD' = OD ∪ {b};
MAPCONDITIONS-
OD~set'(b) = OD~set(b) ∪
{<Date.Now, Latest~hire(b)>};
ENDEVENT;

EVENT Request~inspection(b: Boat);
PRECONDITIONS-
Member(b, F);
SETCONDITIONS-
F' = F - {b};
C' = C ∪ {b};
SIGCONDITIONS-
(Check~condition (b))ON;
ENDEVENT;
```

```sql
ENDTRANSACTION;
```

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
EVENT Maintenance~check (b: Boat, status: S~ code);
SETCONDITIONS-
 $C' = C - \{b\}$ 
status = "ok" →  $F' = F \cup \{b\}$ ;
not(status = "ok") →  $M' = M \cup \{b\}$ ;
MAPCONDITIONS-
 $INSP~set'(b) = INSP~set(b) \cup \{\langle Date.Now, T~min.Now \rangle\}$ ;
SIGCONDITIONS-
status = "repair" → (Repair~boat(b))ON;
status = "scrap" → (Scrap~boat(b))ON;
ENDEVENT;
</div>

The next example of an event arises in a different context; it assigns a referee to a technical paper. Two of the preconditions test that the argument $p$ does indeed belong to the set of submitted papers $S$ , and that ref is an active referee. The prefix Referee indicates that Active has been defined in the referees' segment; similarly for prefix CO (conference organization). The other preconditions test that the number of papers assigned to ref does not exceed some limit, and that the number of referees for the paper does not exceed another limit. The mapcondition adjusts the set-valued function Referees. The flag Paper\~to\~ref, set by the sigcondition, is to initiate the actual sending out of the paper to the referee.

```txt
EVENT Assign~referee~to~paper
(p: Paper, ref: Referee);

PRECONDITIONS-
Member(p, S);
Referee. Active(ref);
Ref~paper~count(ref) < CO. Ref~paper~limit;
Card(Referees(p)) < CO. Ref~number;
MAPCONDITIONS-
Referees'(p) = Referees(p) ∪ {ref};
SIGCONDITIONS-
(Paper~to~ref (p, ref))ON;
ENDEVENT;
```

The responder processes signals either immediately or at some specific time (e.g., 06:30 every morning). The responder initiates events, prompts the user to initiate events, or reminds the user that some action is to be performed. For example, in a system that manages bank accounts, a withdrawal event may cause the account to become overdrawn. In such a case, an overdraft signal is to be sent to the responder. A transaction (in the responder) now initiates an event that assesses a penalty charge against the account and reminds the account manager to send out an overdraft notice to the customer. An event initiates another event only via a responder transaction, and events and transactions can be made to define complicated processes. Sometimes the responder establishes the fact that an event is to be initiated, but cannot do so on its own. It then issues a prompt to the user. For example, in the assigning of referees to a paper, the responder prompts the user to initiate referee assignment events until the required number has been reached. Reminders issued by transactions do not, in general, relate to events.

Our first example of a transaction prompts the editor to initiate the event Assign\~referee\~to\~paper. It is to take place immediately, i.e., at the time indicated by $T^{\sim}$ min.Now.

TRANSACTION Referee\~ search;

```lisp
@(T~min.Now): Forall(x: Paper):
ON(Find~refs(x))OFF:
PROMPT(Assign~referee~to~paper; x);
ENDTRANSACTION;
```

The next example relates to banking. The transaction initiates an event that assesses an overdraft charge against every overdrawn account as it becomes overdrawn and issues a reminder that an overdraft notice is to be sent to the customer.

TRANSACTION Deal\~ with\~ overdraft;

@(T\~min.Now): Forall(x:Account):

The next three transaction relate to boat hiring again. The first prompts a qualified person to initiate event Maintenance\~check. The second initiates the event Mark\~o\~due for every boat that has not been returned by 9:15 p.m., and, at 8:30 next morning, the third reminds management of the establishment to send out people to look for the boats that have not been returned.

TRANSACTION Maintenance;

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$(T^{\sim}min.Now)$: Forall $(x:C)$:
</div>

```txt
ON(Check~condition(x))OFF:
PROMPT(Maintenance~check: x);
ENDTRANSACTION;
TRANSACTION O~due~check;
@(21:15): Forall(x:H): Mark~o~due(x);
ENDTRANSACTION;
TRANSACTION Send~out~searchers;
@(08:30): Forall(x:OD):
REMIND("Find boat": x);
ENDTRANSACTION;
```

## 4. Object-oriented system development

We need to combine data of various types and degrees of uncertainty into a single system. Here the inheritance hierarchies of object orientation help. We are particularly interested in multiple inheritance, such a provided by SF and Taxis [25]. Multiple inheritance can be of two kinds. First, an object of type X can inherit properties of both a type Y and another type Z. Second, some objects of type X may inherit the properties of type Y, while other objects of type X may inherit properties of type Z. At this time SF provides only the first kind of inheritance, by multiple application of the ISA.

A diagram of the type declaration of the set of boats B is shown as Fig. 1. In this diagram, both dashed and solid lines indicate that a set is a subset of the set above it. However, while sets connected by solid lines define different segments, sets connected by broken lines are in the same segment. The solid lines are ISA links, and the ISA facility permits property inheritance; e.g., the properties associated with water vehicles are also properties of boats. However, a different style may be used in the specification of water vehicles. Thus, the specification can be a set of descriptive statements, such as “Water vehicles float,” and need not contain any events or responder transactions at all.

Sets linked by ISA can actually be identical. In this case, the different segments can define properties belonging to different reliability classes, and, within a reliability class, to different levels of reliability. Often the unreliable data can be part of a standard SF segment. Then the subset facility (dashed lines) allows the data to be partitioned according to their levels of reliability.

![](/api/attachments/K9NRFQ6F/fulltext/images/16b6e7c4bbaa81418bc508d9b94bb693249aed7dcf6b4f5c750a9846d71b4a44.jpg)  
Fig. 1.

In contrast to day-to-day boat hiring operations that result in the building up of histories for the boats, the attributes of Water\~vehicles do not change. We call these data class attributes. Although class attributes do not often change, they may be “soft” or “hard”. Thus, segment Water\~vehicles may contain the statement “All smaller boats are taken out of the water in the fall,” but there is no exact size limit above which all boats remain in the water for the winter.

Organization of types into inheritance hierarchies permits us to mix specification languages in the description of a single object. We can now study the specification of one class of data independently of other classes, but still within the single framework of an object-oriented software architecture. The difficulty of reasoning in a knowledge base increases with the expressiveness of the representation system $[24]$ . Modularization leading to inheritance hierarchies lets us pick a representation with the expressive power that is precisely right for each situation.

## 5. Introduction of expert systems

Numerous books on expert systems have appeared, such as [22,37]. A paraphrased and slightly generalized statement of objectives by Raulefs [30] defines an expert system. It will:

\- mechanize activities of human experts in some areas of their expertise, and

\- have representations of domains of application amenable to mechanical manipulation.

The first objective assumes dependability of human expertise. Numerous collapsed bridges, and countless court cases involving negligence and malpractice seem to question this assumption. However, the mishaps are generally not due to lack of expertise, but to time constraints, which lead to carelessness in the application of the expertise. Consequently this is a reasonable objective. The second objective presupposes a formal model of the application domain of the expert system, and this is exactly what a conceptual model of an enterprise should provide.

The three main obstacles to the introduction of expert systems into business enterprises have been the lack of techniques for capturing the expertise of a human in a form appropriate for mechanization, for determining the cost-effectiveness of a proposed expert system, and for the appropriate modularization of the system. The first obstacle is closely related to the difficulty of eliciting the needs of a client when an information system is being constructed, and the techniques developed there $[13]$ should be applicable in expert system design. Of course, designers of expert systems have themselves also devised methodologies for extracting knowledge from experts $[37]$ .

The removal of the other two obstacles is again helped by the SF philosophy. To begin with, SF is based on the partition of an information system into segments. Moreover, each segment is partitioned into a schema, the events, and the responder. Expert systems relate to responder transactions alone, so that there is a well-defined restriction of the field in which the design of expert systems is to occur.

Responder transactions initiate events by themselves or by means of prompts, or they issue reminders of actions to be performed. The latter relate to the sending out of forms, and permit SF to be applied to the specification of office information systems [4]; this can be easily automated, and an information system would become fully automated if prompts were replaced by automatic initiation of events. Each replacement requires that an expert system provide the expertise that the prompt asks from a human agent.

Thus the introduction of expert systems into an enterprise can proceed incrementally, one prompt at a time, and its cost-effectiveness can be estimated beforehand. Most significantly, since the specification should cover all information needs of an enterprise, all opportunities for introducing expert systems can be evaluated.

Responder transactions need not always be initiated by events that send out signals; e.g., a transaction can be initiated by an expert system that monitors the information base for time-dependent trends. Then, if some parameter has not yet reached a threshold value defined by a precondition, but the rate of increase of the parameter has been excessive, the responder can initiate corrective action. Monitoring the rate of increase may be more reliable if carried out by the system rather than by a human, but the correcting action can still be left to humans.

## 6. An agenda for the future

Expert systems base their actions on soft as well as hard data, and there exist methodologies for reasoning with soft data. Brookes [9] lists numerous facilities that a decision support system should have. Many of them are covered in section 2, but many remain to be investigated. In particular, we need to associate each class of data with its appropriate inference making facilities, and devise a methodology for integrating these diverse facilities. Moreover, expert system should be provided with domain specific interfaces; e.g., their inputs should be in terms familiar to the user (the domain terminology), and they should explain their reasoning in terms familiar to the user. These are a major long-term undertaking. The time lag between publishing of research ideas and results, and application of them in practical situations is 10–15 years [10].

There are already some of the methodologies needed for decision support and, in principle, no obstacles to the development of additional methodologies exist, but there remains the practical problem of getting them accepted. Sibley [36] adduces multiple cases where conventional systems were improperly constructed without a separate specification stage. The temptation to omit specification of decision support systems is even stronger. An important part of our agenda should be persistence in demonstrating the cost benefits of specification, both to managers and software developers. The most forceful demonstration consists of providing systems that automatically transform specifications into efficient implementations. Such systems can, in principle, be built today.

## Acknowledgement

The basic ideas presented in this paper were developed while the author was with SYSLAB at the University of Stockholm in the summers of 1986 and 1987. Support for these stays provided by STU (Swedish National Board of Technical Development) is gratefully acknowledged.

## References

[1] Albano, A., Cardelli, L., and Orsini, R., Galileo: A Strongly-Typed, Interactive Conceptual Language. ACM Trans. Database Systems 10 (1985), 230–260.

[2] Baldwin, J.F., An Uncertainty Calculus for Expert Systems. In Approximate Reasoning in Intelligent Systems, Decision and Control (E. Sanchez and L.A. Zadeh, eds.), Pergamon Press, Oxford, England, 1987, pp. 33–54.

[3] Berztiss, A.T., Data Abstraction in the Specification of Information Systems. Proc. IFIP Congress 86, pp. 83–90.

[4] Berztiss, A., Sites in the SF Specification Language. Proc. 1987 IEEE Workshop on Languages for Automation. pp. 201–205.

[5] Borgida, A., Language Features for Flexible Handling of Exceptions in Information Systems. ACM Trans. Database Syst. 10 (1985), 565–603.

[6] Borgida, A., Exceptions in Object-oriented Languages. Proc. Object-Oriented Prog. Workshop 1986, SIGPLAN Notices 21, 10, Oct. 1986, 107–119.

[7] Bossu, G., and Siegel, P., Nonmonotonic Reasoning and Databases. In Advances in Data Base Theory, Vol. 2 (H. Gallaire, J. Minker, and J.M. Nicolas, Eds.), Plenum Press, New York, 1984, pp. 239–284.

[8] Brodie, M.L., and Mylopoulos, J. (eds.), On Knowledge Base Management Systems. Springer-Verlag, New York, 1986.

[9] Brookes, C.H.P., Requirements Elicitation for Knowledge Based Decision Support Systems. In Decision Support Systems: A Decade in Perspective, E.R. McLean and H.G. Sol (Eds.), North-Holland, Amsterdam, 1986, pp. 129–144.

[10] Bubenko, J.A., Information System Methodologies – A Research View. In Information System Design Methodologies: Improving the Practice, T.W. Olle, H.G. Sol, and A.A. Verrijn-Stuart (Eds.), North-Holland, Amsterdam, 1986, pp. 289–318.

[11] Buckles, B.P., and Petry, F.E., Uncertainty Models in Information and Database Systems. J. Inf. Science 11 (1985), 77–87.

[12] Cohen, P.R., Heuristic Reasoning about Uncertainty: An Artificial Intelligence Approach. Pitman, London, 1985.

[13] Davis, G.B., Strategies for Information Requirements Determination. IBM Systems J. 21 (1982), 4–30.

[14] Dubois, D., and Prade, H., Fuzzy Sets and Systems: Theory and Applications. Academic Press, New York, 1980.

[15] Etherington, D.W., and Reiter, R., On Inheritance Hierarchies with Exceptions. Proc. AAAI-83, 1983, 104–108. (Reprinted in Readings in Knowledge Representation, R.J. Brachman and H.J. Levesque (Eds.), Morgan Kaufmann, Los Altos, CA, 1985, pp. 329–334.)

[16] Fiadeiro, J., and Sernadas, A., The Infolog Linear Tense Propositional Logic of Events and Transactions. Information Systems 11 (1986).

[17] Furtado, A.L., and Neuhold, E.J., Formal Techniques for Data Base Design. Springer-Verlag, Berlin, 1986.

[18] Garvey, T.D., Lowrance, J.D., and Fischler, M.A., An Inference Technique for Integrating Knowledge from Disparate Sources. Proc. IJCAI-81, 1981, 319–325. (Reprinted in Readings in Knowledge Representation, R.J. Brachman and H.J. Levesque (eds.), Morgan Kaufmann, Los Altos, CA, 1985, pp. 457–464.)

[19] Gelenbe, E., and Hebrail, G., A Probability Model of Uncertainty in Data Bases. Proc. Internat. Conf. Data Engineering, 1986, 328–333.

[20] Gupta, M.M., and Sanchez, E. (eds.), Approximate Reasoning in Decision Analysis. North-Holland, Amsterdam, 1982.

[21] Gupta, M.M., Kandel, A. Bandler, W., and Kiszka, J.B. (eds.), Approximate Reasoning in Expert Systems. North-Holland, Amsterdam, 1985.

[22] Hayes-Roth, F., Waterman, D.A., and Lenat, D.B. (eds.), Building Expert Systems. Addison-Wesley, Reading, MA, 1983.

[23] Kung, C.H., and Solvberg, A., Activity Modeling and Behavior Modeling, In Information System Design Methodologies: Improving the Practice, T.W. Olle, H.G. Sol, and A.A. Verrijn-Stuart (eds.), North-Holland, Amsterdam, 1986, pp. 145–171.

[24] Levesque, H.J., and Brachman, R.J., A Fundamental Tradeoff in Knowledge Representation and Reasoning (revised version). In Readings in Knowledge Representation (R.J. Brachman and H.J. Levesque, eds.), Morgan Kaufmann, Los Altos, CA, 1985. pp. 42–70.

[25] Mylopoulos, J., Bernstein, P., and Wong, H.K.T., A Language Facility for Designing Interactive Database-Intensive Systems. ACM Trans. Database Syst. 5 (1980), 185–207.

[26] Naish, L., Negation and Control in Prolog. Springer-Verlag LNCS No. 238, Berlin, 1986.

[27] Naqvi, S.A., Negation in Knowledge Base Management Systems. In On Knowledge Base Management Systems (M.L. Brodie and J. Mylopoulos, eds.), Springer-Verlag, New York, 1986, pp. 125–145.

[28] Nilsson, N.J., Probabilistic Logic. Artificial Intelligence 28 (1986), 71–87.

[29] Nilsson, N.J., and Genesereth, M.R., Logical Foundations of Artificial Intelligence. Morgan Kaufmann, Los Altos, CA, 1987.

[30] Raulefs, P., Expert Systems: State of the Art and Future Prospects. In Proc. GWAI-81 (J.H. Siekmann, ed.), Springer-Verlag Informatik Fachberichte, No. 47, 1981, pp. 98–111.

[31] Rolland, C., and Richard, C., The Remora Methodology for Information Systems Design and Management. In

Information System Design Methodologies: A Comparative Review (T.W. Olle, H.G. Sol, and A.A. Verrijn-Stuart, Eds.), North-Holland, Amsterdam, 1982, pp. 369–426.

[32] Rowe, N.C., Inheritance of Statistical Properties. Proc. AAAI-82, 1982, 221–224.

[33] Sanchez, E., and Zadeh, L.A. (eds.), Approximate Reasoning in Intelligent Systems, Decision and Control. Pergamon Press, Oxford, England, 1987.

[34] Shipman, D.W., The Functional Data Model and the Data Language DAPLEX. ACM Trans. Database Syst. 6 (1981), 140–173.

[35] Sibley, E.H., and Kerschberg, L., Data Architecture and Data Model Considerations. Proc. Natl. Comp. Conf., 1977, 85–96.

[36] Sibley, E.H., The Evolution of Approaches to Information

Systems Design Methodology. In Information System Design Methodologies: Improving the Practice, T.W. Olle, H.G. Sol, and A.A. Verrijn-Stuart (eds.), North-Holland, Amsterdam, 1986, pp. 1–17.

[37] Waterman, D.A., A Guide to Expert Systems. Addison-Wesley, Reading, MA, 1986.

[38] Yager, R.R., Using Approximate Reasoning to Represent Default Knowledge. Artificial Intelligence 31 (1987), 99-112.

[39] Zadeh, L.A., Fuzzy sets. Information and Control 8 (1965), 338–353.

[40] Zvieli, A., and Chen, P.P., Entity-Relationship Modeling and Fuzzy Databases. Proc. Internat. Conf. Data Engineering, 1986, 320–327.
