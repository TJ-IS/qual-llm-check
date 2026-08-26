---
otero_id: 18379
otero_key: "PSHHNBPR"
title: "Information systems user-designer communication problems"
authors: "A.A. Verrijn-Stuart; K. Anzenhofer"
year: "1988"
journal: "Information & Management"
doi: "10.1016/0378-7206(88)90004-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems User-Designer Communication Problems

A.A. Verrijn-Stuart and K. Anzenhofer
Department of Computer Science, University of Leiden, 2333 CA
Leiden, The Netherlands

Designing an information system of some complexity requires cooperation between three parties: the user, the designer, and the builder. To achieve efficient communication between these, a number of problems that stem from the differences in background of the persons involved must be overcome.

The following vehicles for communication (forms of specification language) are discussed: graphic diagrams, tables, natural language and formal languages. Although intended for investigating design options, prototyping also renders a communication-type service, which is particularly useful when requirements are incomplete. The various forms of expression are compared, and weaknesses and strengths are highlighted.

Keywords: Information systems design, Design languages, User-designer-builder communication, Prototyping

![](/api/attachments/PSHHNBPR/fulltext/images/209d67a672f0fa27308dc3156165a06ebf0ce0b78862b7b28e9fcd7fc3bd8da0.jpg)

Alex Verrijn-Stuart is professor of computer science at the University of Leiden. Originally trained as a physicist (University of Amsterdam, Ph.D. University of Michigan) he joined the Royal Dutch/Shell Laboratory, Amsterdam in 1952, two years before the first computer was installed there. This triggered a turbulent career in computing, operations research and planning, in Paris, The Hague, London and Abadan. In 1970 he left the service of the Group to take up his present position. His current research concerns information system design methodology and office systems.

## 1. Introduction

The ultimate user of an information system is the prime mover in defining its needs. When dealing with a system of some complexity, these requirements cannot be formulated more rigorously than conceptually, certainly not in terms that would enable the designer to establish the unambiguous specification needed in the building stage. Requirements will therefore have to grow out of interaction between user and designer, alternating with user-builder consultation to check the intended system's implementability.

Fig. 1 characterizes this path in a five-step breakdown. In step (1) the essential features of the system (or of a module that can be developed in isolation) are established. This step concerns an abstraction or model of the real system that will be expressed in a language that is understandable to the user.

Steps (2) and (3) are the responsibility of the designer. The formulation resulting from the latter will be as precise as the model from step (1), but normally employs a more formal language. Step (4) is not needed until the process has advanced sufficiently for implementation to make sense or making a choice of alternatives is unavoidable. At (1) Modelling (abstract description of the system)---->
(2) A Analysis (check on consistency and correctness)---->
(3) | Translation (to a format suitable for builder)---->
(4) | Testing (optional preliminary run-tests)---->
(5) | Discussion with user (recycle until exit)----+
|

![](/api/attachments/PSHHNBPR/fulltext/images/a4858b0669cfa8a991c2ca34ea76bf768685dfd97bd049bb5d7ff05b26ce6282.jpg)  
and tools for development and management of information systems.

Fig. 1. Steps towards the specification of an information system.

this point, the use of a prototyping tool may enable the designer to demonstrate some key features of the design to the other two parties. Finally, step (5) provides the basis for the decision whether the specification has been completed or the development is to be continued.

Of course, user, designer, and builder may coincide partially or totally. One extreme occurs in personal computing, with all roles played by the same individual. For systems of any complexity, this no longer holds. In this connection the user may be described [CR88] as the acceptor to whom the design will be presented in a definitive document, termed the acceptor specification. It forms the basis for the builder specification. Together, these add up to the design product.

Because user and builder view the requirements from different angles, and because their cultural backgrounds usually are not the same, both the emphasis of the specifications and the language for expressing these will be different as well. Thus a designer has two communication problems. The situation will further vary, however, depending on the nature of the system to be developed. In large, static, data processing applications, preciseness is predominant; in real time systems the synchronization poses additional problems, and for new development in unexplored directions (as in decision support system design) the inherent uncertainty creates yet other approaches to reaching mutual understanding.

The next section discusses user-designer communication in more detail. Some practical consequences for the builder specification follow, and the alternatives offered by prototyping are taken up in the subsequent sections.

## 2. Acceptor Specification Languages

The specification agreed between user and designer must be unequivocal about any matter of interest to the user. Initially, it will be expressed in natural language. The variety of objects, associations, signals, messages, functions and processes which play a role here is, generally, too large to tackle without the use of tools. Possibilities are: graphic diagrams, tables and languages like programming languages termed formal (specification) languages here, and so on.

Graphic symbols, connected by lines and arrows, are used for describing equipment configurations, global processing schemes (block diagrams), and computer programs (flow diagrams). In principle, a common set of symbols might be used for all. One is already available: the ISO Standard for flowchart symbols for information processing [AN70]. In the design of information systems, similar diagrams are used, but there is no generally accepted standard. Two classes of diagrams exist:

\- information flow schemes, and

\- data modelling diagrams.

An information flow scheme is a natural expression of the process-oriented approach to information systems [VS79, VS85], where activities in the real system (RS) are taken as a basis for the design of the information system (IS). In the flow scheme, physical entities and flows are modelled, and data collections that are involved in these data processing activities are identified. The term “process oriented” therefore refers both to the business processes (in the RS) and the data processing functions (in the IS). Information flow schemes are drawn horizontally [GS79, YC79] or vertically [LU79], depending on the local or vendor standard. We encounter many symbols (circles, squares, polygons, etc.). For pragmatic reasons, one’s choice might be limited to those symbols that can be produced by common matrix printers. A sample set is presented in Fig. 2.

![](/api/attachments/PSHHNBPR/fulltext/images/198226c9722ecbbe951e549d816f8946d392bf872c49d20fab9d23f14fb9e257.jpg)  
Fig. 2. Some flow symbols, printable on a matrix printer.

The power of the information flow scheme lies in the clear link between the RS activities and the information processes supporting them. Also, a schematic representation is more easily understood than a formal method describing the same things. However,

\- even a moderate level of detail may destroy the understandability, since it leads to numerous parts (subsystem diagrams) that cannot be (seen to be) linked easily; existing connections may therefore be overlooked when some modification is applied, and

\- in detailed discussion of an information system component, the user may become involved in implementation considerations (the how), though the issues really concern the (organizational) information requirements (the what).

A graphic diagram of a process must be accompanied by a specification of the data. These will ultimately be included in a database, so that a tabular representation is called for (data dictionary). However, only static aspects can be represented satisfactorily in this way. For dynamic aspects, additional measures are required, such as

\- triggers (indicating initiation of processes); e.g., arrival of a query, updates to the database, and
- addition of start and stop times to the list of attributes.

In addition to schemes and tables, some detail can be represented by commentary in natural language (text). Attention must be paid, however, to the risk that such text is not changed when the design is modified.

A data modelling diagram is a means of representing details of the important objects in the RS. The graphic symbolism employed to represent entities and their relationships is as understandable as information flow schemes, but originates from the data oriented approach to IS design [VS85]. This approach evolved from the time when the concept of a shared database was first proposed.

The main concern was accessing the available data, which became feasible when magnetic tape units were connected to central computer systems around 1960 [YK58, CL62].

More independence from the mode of representation was achieved by the introduction of data abstraction in the mid 70's, e.g., in the entity-relationship (or ER) model [CH76]. The original ER-approach is based on the concepts of entities (the concrete and abstract things of interest) and their relationships. In a particular model, they are introduced as general classes, viz. the entity and relationship types.

In the ER approach data model elements are represented by rectangles (entities) with circles (which identify possible attributes), connected via rhomboids (which model relationships). Dependencies are expressed by arrows along the connections. The intention will always be to make the representation complete. In most cases, this ideal cannot be achieved, due to natural complexity of the RS.

Other problems arise as soon as dynamic system characteristics are added to the data model. This may be illustrated by the requirements needed in dealing with the semantic integrity of data (the presence in the IS of allowable values only). In principle, data integrity hinges on a dynamic restriction: if we start with an empty system, subsequent operations will not lead to an invalid state as long as operations are limited. A first requirement, therefore, is the value empty (or absent, as in [CL62]). Then the only danger to its integrity would be in update operations (addition, deletion and modification).

In practice a distinction is made between static constraints (which hold implicitly in every state of the IS) and dynamic restriction rules (applicable to state transitions and guarantee that the new state is also valid). An example of the former is the general field definition, establishing field lengths and symbol types in a database structure (as in 'typed' programming languages). Dynamic restrictions express special rules; e.g., the occurrence of existing street names in an IS containing addresses. Unfortunately, there is no simple way to denote either type of constraint in graphic techniques.

Nevertheless, graphic schema techniques can be effective, provided the time dependent (dynamic) aspects can be included and associated with state transitions of the IS. Thus we need an object type event. Additionally, each time dependent entity type must be given appropriate time attributes (time-of-creation, period-of-validity, etc.).

The way in which the graphic schema techniques may express such elements may be illustrated by (part of) the data model for the IFIP case [OL82]. Fig. 3 shows a single high level entity type person, which may occur in various (lower level) sets. Type and set are both denoted as rectangles, with distinct corners (+ and O, respectively). Semantically, the sets are specializations of the higher level entity type, and their relationship is therefore further indicated by connecting lines with a double point “--»”. Since there are constraints to the admission into these sets, brief expressions are appended to the respective arrows. If space is insufficient for denoting the full constraint, one may resort to a “footnote”.

Additionally, there is the object type event, which is represented as a rounded rectangle. Of course, an event is associated with one or more other object types. If it concerns an entity, it may mean that a change occurs to it; such is the case in connection with the sets (e.g., admission). The association of event and entity always involves a form of trigger; i.e., the event is caused by and often will also be causing another event. The dynamic restrictions applicable to the changes involved in the events may be expressed simply as pre- and post-conditions. In our notation, the former are attached to the transition arrow, the latter are placed inside the oval.

The graphic schema technique may be applied in such a way that the results are strictly formal and unambiguous [DU85]. In that sense they provide a similar basis to formal language specifications. In fact, the two representations may be shown to be fully equivalent, given some simple limitations [VS85, VS87]. This is illustrated by Figure 4, which represents precisely the same part of the IFIP case as does the graphic diagram of Fig. 3.

The representational equivalent between user-friendly graphics and builder-required formal expressions may be exploited in order to facilitate the overall communication, as will be discussed in the next section. In a later stage we will further address the problems posed by uncertain system needs, such as arise in planning and decision support. It should be stressed, however, that all

![](/api/attachments/PSHHNBPR/fulltext/images/630eb3a7b0daab9bc0b14b2a79cd8341954cf8ee555257283d428f30b812f629.jpg)

Sets ----> of persons, subject to the conditions within brackets (...); attributes of persons not encircled.
There are two sorts of "events" with respect to the "persons"; these depend on preconditions and lead to situations subject to postconditions; they are initialised by and say result in "triggers" ---->
Specific "relationships" are not indicated in this part of the model, but the reader should have no difficulty adding some for himself.

Fig. 3. Part of a graphic specification of the IFIP case.

systems other than full process control require a certain amount of human intervention (pre-action judgement). And the form this might take will depend on the capability of the ultimate system. That user and builder perspectives will thus need interactive tuning is therefore evident.

## 3. Builder Specification Languages

For transfer to the information system builder, the design must usually be specified in more detail and/or more precisely than would derive from the acceptor specification points. In some respects, the builder may even be free to choose among certain alternatives. Nevertheless the over-all description must be unequivocal, especially in regard to the aspects that concern usage of the system.

For this purpose, more formal aids are required than provided by a graphic diagram with commentary. The data model is the first candidate for expression in a formal “record-oriented” language, not least because it is more compact in its representation of the entity and relationship characteristics. In Fig. 4 the entity type “person” and its specialisations have been thus formalised, along with several instances of events.

The notation is similar to that of [BE86]; it is evident that the essential parts of the functional specification can be fitted into a formal language in a very clear way, including the dynamic elements. In comparison with the graphical notation, the same details are seen to be included; there is even the advantage that footnotes can now be integrated with formal declarations.

<table><tr><td colspan="2">TYPE Person)ATTRIBUTES - Name : STRING; /* &#x27;STRING&#x27; and other data types */Address : STRING; /* defined elsewhere */Attribute_a: STRING); /* Attrib-x is used below */Attribute_z: STRING);Role_code : /* Attribute used below */ENDTYPE;</td></tr><tr><td colspan="2">SET Program_committee OF Person)CONDITIONS - (&#x27;PC&#x27; IN Role_code); /* &#x27;PC&#x27; is agreed PC-member code */(NUMBER &lt;= max); /* &#x27;max&#x27; INTEGER def&#x27;d elsewhere */ENDSET;</td></tr><tr><td colspan="2">SET Organizing_committee OF Person)CONDITIONS - (&#x27;OC&#x27; IN Role_code); /* &#x27;OC&#x27; is agreed OC-member code */(Addr = &#x27;HC-locality&#x27;); /* Conference locality */ENDSET;</td></tr><tr><td colspan="2">SET Prospective_Authors OF Person; /* code &#x27;AUT&#x27; one of several */CONDITIONS - (&#x27;AUT&#x27; IN Role_code); /* does not prclude others */(&#x27;ACC&#x27; NOT IN Attrib-x); /* Acceptance-code */ENDSET;</td></tr><tr><td colspan="2">SET Accepted_Authors OF Person)CONDITIONS - (&#x27;AUT&#x27; IN Role_code); /* &#x27;AUT&#x27; as above */(&#x27;ACC&#x27; IN Attrib-x); /* as above */ENDSET;</td></tr><tr><td colspan="2">EVENT Becomes_OC_member)CONCERNS - ( &lt;x&gt; | Person); /* &lt;x&gt; defined by condition */TRIGGERD_BY - OC_invitation; /* event defined elsewhere */PRECONDITIONS - ( &lt;x&gt; NOT IN OC); /* &lt;x&gt; as above */POSTCONDITIONS - ( &lt;x&gt; IN OC); /* &lt;x&gt; as above */ENDEVENT;</td></tr><tr><td colspan="2">EVENT Author_acceptance)CONCERNS - ( &lt;x&gt; | Person); /* &lt;x&gt; defined by condition */TRIGGERD_BY - Referee_message; /* event defined elsewhere */TRIGGERS - Acceptance_letter; /* event defined elsewhere */PRECONDITIONS - ( &lt;x&gt; IN Prospective_authors);(Report(x) = &#x27;POSITIVE&#x27;);/* function &#x27;Report&#x27; and value &#x27;POSITIVE&#x27; defined elsewhere */POSTCONDITIONS - ( &lt;x&gt; IN Accepted_authors);/* zelfde &lt;x&gt; als in Accepted_authors */ENDEVENT;</td></tr></table>

Fig. 4. Part of a formal language specification for the IFIP case.

The equivalence of the two representations provides a good vehicle for transferring the design product; all structural detail and all logical connections are unambiguously represented to both user and builder. Yet, no commitment is made to the exact lines along which actual information transformations are to take place. However, even this aspect may be outlined to the builder by adding suggestions regarding the processes that correspond to the events.

All one has to do is to add them in the same fashion as procedures (in the programming language sense) in a higher order language program.

By a global specification, the builder is given all freedom to choose a construction fitting efficiently into the local operational environment.

From the above, it is clear that full automation of the steps leading from user-friendly design representation of reasonably non-trivial systems to working prototypes is near [VS87]. Because of the demonstrative power obtained thereby, a further vehicle for communication between user and designer becomes available. The final two sections deal with the implications of this development.

## 4. Prototyping as a Communication Vehicle

Prototyping is used in various stages of information system design. With some simplification, the following categories may be distinguished:

(1) Mock-ups: A simple presentation of on-line screens and printed reports to catalyse first interaction between designer and user on the way towards a more detailed specification.

(2) Simulation: On-line interaction or batch reporting via simulation, with no intention of using programs and files in the construction stage; relationships between transactions are made visible in a limited way, the communication process reaches as far as the actual user (but not local management).

(3) Working model: A partial system, with interaction between the files and/or transactions; functions, transactions, files and programs are not developed completely; the builder may become involved in the communication process to establish operational detail.

(4) Research and development: Replaces the IS life cycle and is equivalent to a research project, the results of which may, or may not be, developed further; the demarkation between the preparatory stages (planning, analysis) and subsequent ones (design, construction) disappears; the communication process involves all parties. Use of prototyping at this level is recommended by some as an explicit IS design methodology [WA82].

Thus many levels of prototype allow the researcher and designer to

\- evaluate the potential impact of the IS on the organization,

\- establish form and contents of the information requirements and determine the required data structure,

\- develop effective man-machine interfaces.

\- establish the exact definition of the data, plus the conditions they must meet in validation checks,

\- anticipate potential changes: these can and will occur. A prototype may provide insight into the extent to which a chosen approach can accommodate change (evolvability). And

\- determine the efficiency of various types of transaction using a test database, so that the physical structure of the actual database can be optimised.

In all these, communication between user, designer, and builder is essential. Prototyping provides almost automatic feed-back and iteration.

Prototyping is by no means restricted by the size of the target IS. Its use, however, does reflect the main problems in IS design, ranging from data modelling for large systems to a rather direct model of processes and utilities in (possibly small but often mathematically complex) decision support systems.

It is not surprising that prototyping has been used for many years in developing interactive computer systems, such as flight reservation and order processing systems. Wide-spread use, however, needed two new elements: fourth generation languages and database management systems, with corporate data already available. The biggest contribution of the former is the tremendous reduction in programming effort; the prototype is developed much faster. The latter enables the designer to demonstrate results more realistically. Thus the road from the first concept to the testing of a functional model is shortened and the parties may concentrate on the information needs and their fulfilment, rather than being distracted by computational and testing details.

There are however a few pitfalls, and it is necessary for the designer to be fully aware of them so as to take full advantage of the prototyping approach to information systems design:

Functional requirements: Conventional IS design methods define milestones that provide essential checkpoints on the road from user requirements to implemented system. The most important one for the user is the comparison of his own stated requirements with the functional specification, which the designer produces as a result of functional design activities. Prototyping tends to blur the difference between functional and technical design and it may be too difficult for the user to see whether the functional specifications are sufficiently covered. Therefore, the designer is essentially responsible for a feedback that leads to full agreement between the functional specifications and the set of requirements as stated by the user.

Operational requirements: Next to the functional requirements, an IS must meet requirements of run-time performance, security and data integrity. These aspects are virtually never addressed in prototyping, and very often the user cannot appreciate the necessity to pay attention to and spend – sometimes very substantial – effort on a proper coverage of these requirements in the ultimate operational IS. Again, the designer has to take care for the user to understand these operational requirements, and for the design to include the appropriate specifications. In view of its importance for the effectivity of the final IS, the transaction design will be discussed separately.

Delineation: An IS must be delineated with regard to other IS's. Furthermore – and certainly in organizations with a corporate database management policy – the IS must have a well-defined interface with the corporate database. Prototyping does not address these two points. Thus, here also the designer must make sure to carry them forward into the builder specification. In particular, the fundamental delineation has to be fully understood and accepted by the user.

Use of 4th generation development tools: Due to compactness of the code and the comparatively limited construction effort, it seems attractive to use the prototyping language for the construction of the operational target system; this is even recommended positively by some authors (e.g., [MF81, AP83]); at present, a difficult choice is posed here. A prototyped system often requires more computer resources than one developed using a traditional language.

Prototyping, using standard application software packages: Standard application packages are increasingly used in IS, due to the tremendous cost savings that may be achieved. The main areas are, at present: administration, project management, and logistics. Main features of the packages are:

\- Coverage of a wide spectrum of functionality;

\- No defined interfaces with other applications;

\- Regular updates and extensions;

These features present a few problems for the design of IS:

\- From the offered functionality, a selection must be made that meets the user requirements and leaves out all unnecessary features;

\- Interfaces have to be designed, as yet;

\- New releases have to be checked to see whether additional benefits are included.

Certainly the first two problems can be suitably tackled by prototyping. It is worth noting that the prototyping process is evolutionary here: the prototypes are not discarded after use in various design stages, but are gradually extended and refined towards the operational system. The designer must therefore make sure that the user understands that also with the use of standard software, the design stage is still an essential part of the IS cycle.

To sum up, prototyping has become a powerful strategy for tackling many questions in designing IS. There are some pitfalls that may put such designs at risk. The extra communication link that prototyping provides between user and designer should be used to overcome these. This is certainly feasible, because the pitfalls all arise from some incorrect and over-optimistic user ideas about prototyping. The special requirements imposed on the design process in the case of transaction design deserve special consideration.

## 5. Transaction Design

In interactive systems, the screen is an essential element for transaction handling as well as the selection of algorithms for the processing steps. The two main problems are: the choice of the screen layouts and the determination of the time constraints. Most information system design methodologies remain vague in these respects. There are exceptions, however, such as [WA82]. For both problems, the user can decide on the specification almost without any outside help, when transaction design is included in the functional design steps. These are [SC86, VO86]:

![](/api/attachments/PSHHNBPR/fulltext/images/c75a25390f55bd53d00c0634c7678390f1daa80c24e7d921c9c95697517cd942.jpg)  
Fig. 5. The roles of the user in the design process.

(1) Establish a transaction scheme, listing all human and computer activities in an interactive system,

(2) Use these to simulate the dialogs (using a dialog simulator); as a result, screen layouts and response times are determined;

(3) Finally, in the subsequent transaction analysis, quantify these requirements; on this basis, establish the resulting workload for the network and computer system.

The result is a list of ergonomic and technical specifications for the system. The role of the user in the design process is clearly extended, as illustrated in Fig. 5.

Whilst the transaction design is suitable for specific information systems, it does not address the problem of network strategy. The network design is one choice from a range of facilities. A solution to the inherent problem may be found by defining an appropriate mix. The design parameters resulting from transaction design activity may then be used; e.g., to check network alternatives concerning potential bottlenecks.

## 6. Conclusions

Two types of representation appear to be effective aids for the communication between user and designer/builder of an information system: graphic diagrams and (indirectly) prototyping. For both, the strong point is that design aspects may be illustrated and explained quickly and simply. However, there are some potential shortcomings.

For purely Graphic schema techniques these are:

\- It is impossible to achieve sufficient detail without loss of transparency, unless support is provided by other means, such as tables, comments and footnotes;

\- It is difficult to maintain consistency when updating a design requiring a large number of subdiagrams.

## For Prototyping they are:

\- There is a temptation to deal with a limited number of aspects.

\- Often the design process results in an inefficient system.

In designing interactive systems, special care must be taken to achieve an effective user-machine interface, with high quality ergonomics and appropriate response times. For this purpose, transaction design should be incorporated in the functional specification process.

The use of a formal specification language may help avoiding a number of these problems. However, the current user do-it-yourself design tools that lack a comprehensive formal framework will not provide a basis for more than relatively simple information systems. Similarly, the present forms of prototyping will only allow construction of ad-hoc extensions to existing systems.

For the time being, the major impact of formal specification languages will be found in the unequivocal establishment of the builder specification, on the basis of differently formulated expressions in the acceptor specification. In due course, the inherent equivalence of the two may be expected to provide a basis for integrated automated systems serving both purposes, including the capability of quick prototyping. The formal specification language should, therefore, be seen as the future support facility for the information system designer in dealing with the user- as well as the builder-specific parts of the design communication problem.

## References

[AN70] ANSI Standard Flowchart Symbols and Their Use in Information Processing (X3.5), American National Standards Institute, New York, (1970).

[AP83] D.S. Appleton, Data Driven Prototyping, Datamation, (Nov. 1983).

[BE86] A. Berztiss. The Set-Function Approach to Conceptual Modeling, in [CR86], pp. 107–144.

[CH76] P.P. Chen, The Entity Relationship Model: Toward a Unified View of Data, ACM Transactions on Data Systems 1 (1976) 9–37.

[CL62] CODASYL Development Committee, Language Structure Group, An Information Algebra, Comm ACM 5 (1962) 190–204.

[CR82] T.W. Olle, H.G. Sol and A.A. Verrijn-Stuart, eds. Information System Design Methodologies: A Comparative Review ("CRIS-1"). North-Holland, (1982).

[CR86] T.W. Olle, H.G. Sol and A.A. Verrijn-Stuart, eds. Information System Design Methodologies: Improving the Practice ("CRIS-86"), North-Holland, (1986).

[CR88] IFIP WG 8.1 CRIS Task Group, Information Systems Methodologies. A Framework for Understanding, Addison-Wesley, (1988).

[CR85] Dubois et al., Philips Research Memorandum M125, A Process Model for Requirements Engineering, Brussels (Sep. 1985).
Dubois et al. Philips Research Memorandum M126, A Data Model for Requirements Engineering, Brussels (Oct. 1985).

[GS79] C. Gane and T. Sarson, Structured Systems Analysis: Tools and Techniques, Prentice-Hall, (1979).

[JO83] J.R. Johnson, A Prototypical Success Story, Datamation, (Nov. 1981).

[LU79] M. Lundeberg, G. Goldkuhl and A. Nilsson, A Systematic Approach to Information Systems Development, Information Systems 4 (1979) pp. 1–12. 93–118.

[MF81] J. Martin and C. Finkelstein, Information Engineering, Savant Institute, (1981).

[OL82] T.W. Olle, IFIP Comparative Review of Information System Design Methodologies: Problem Definition, in [CR82], pp. 8–9.

[SC86] J.A. Scheltens, The Design of Interactive Applications and Computer Networks, Academic Service (The Hague), (1985) (in Dutch).

[VB82] G.M.A. Verheijen and J. van Bekkum, NIAM, An Information Analysis Method, in [CR82], pp. 537-587.

[VO86] VOLMAC Course material on A Screen Sequence Design Tool, (1986) (in Dutch).

[VS79] A.A. Verrijn-Stuart, The Past and Future of Information Systems, EURO-IFIP 79, P.A. Samet, ed., North-Holland, 1979, pp. 153–161.

[VS85] A.A. Verrijn-Stuart, Information Systems Theories and Their Uses, Report 85-27, Department of Applied Mathematics and Computer Science, University of Leiden, (1985).

[VS87] A.A. Verrijn-Stuart, Equivalence Conditions for Information System Representations, Report 87-09 A, Department of Computer Science, University of Leiden, (1987).

[WA82] A.I. Wasserman, The User Software Engineering Methodology, An Overview, in [CR82], pp. 591–628.

[YC79] E. Yourdon and L.L. Constantine, Structured Design, Prentice-Hall, (1970).

[YK58] J.W. Young and H.K. Kent. Abstract Formulation of Data Processing Problems, J. Ind. Eng. (Nov.-Dec. 1958) pp. 471-479.
