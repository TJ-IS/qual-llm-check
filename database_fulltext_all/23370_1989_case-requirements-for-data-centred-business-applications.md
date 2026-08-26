---
otero_id: 23370
otero_key: "869DKPVS"
title: "CASE Requirements for Data-Centred Business Applications"
authors: "Graham Tate; June Verner; Richard Hayward"
year: "1989"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1989.34"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# CASE Requirements for Data-Centred Business Applications\*

Graham Tate, June Verner and Richard Hayward, Massey University, New Zealand

Abstract: From a CASE point of view business applications can be divided into three broad classes depending on their generality: those requiring general workbenches, those requiring specifically tailored workbenches, and those that could use blueprints. A CASE environment for all seasons is not what many business users really need. They would prefer an environment tailored to the specific class of application under development, one that will bring that application into being most efficiently and effectively, and keep it in vigorous operation over its lifetime. We have therefore concentrated on one particular application class of interest to the business community, namely interactive, data-centred systems. A model for the application class of interest is presented. The main CASE environment requirements identified, which should be integrated through a common project database and tailored to the characteristics of the application class, include business profile, semantic data model, state transition control model, system dictionary active during development, inheritable and tailorable objects such as reports, transactions and other user interactions, procedural facilities, configuration control, project control including costing and scheduling, and interfaces to decision support systems. It is noted that development and production have quite different characteristics and require separate environments. The need for flexibility and adaptability in some CASE environment areas, such as effort estimation and project control, is recognized and it is suggested that existing rule-based techniques should be used. Limitation of a CASE tool set to a rather narrow but common application class should result in substantial productivity gains.

## 1. Introduction

From a CASE viewpoint, business applications can be divided into three broad classes depending on their generality – namely general, intermediate and specific. The general requires ab initio development including the design of many of the objects of interest. It is suited to a general CASE workbench. The intermediate is able to build on, by tailoring or inheritance, a number of given generic object classes such as certain database components, windows of several types, reports, and their built-in relationships, assuming a certain application architecture. It is suited in some cases to fourth generation language (4GL) development. The specific has many well defined application objects such as accounts, journal entries, balance sheet entries, etc. It is suited to the use of packages, or CASE blueprints, i.e. tailorable CASE packages.

Most CASE tool sets or environments have a high ambition level, typified by two goals which none have yet achieved. The first is support of a wide range of application types; the second support over the whole life cycle, including life cycle variations such as prototyping. We can see good marketing reasons for this, but are more sceptical about the usability and productivity of such environments for certain more limited application classes, particularly those of the intermediate type. We believe that much more specific CASE environments, tailored to particular application classes, may be more productive in such cases. This is not dissimilar to the use of different programming languages for different types of programming problems.

We therefore present some requirements for an intermediate CASE environment for the narrow but common class of business applications which may be described as data-centred interactive systems, usually of medium size. Further motivation for these proposed requirements is advanced below. First, however, we shall describe the target application class more precisely.

## 2. The application class

## 2.1 Business function

The kind of organization we have in mind wants a lean, energetic and responsive information systems (IS) service. It is concerned to adapt quickly to new market opportunities, and does not want to be impeded in doing so by the inertia of existing IS applications, or difficulties and delays in developing new applications. It is not heavily centralized with massive integrated IS applications, like a bank or insurance company, but is more suited to less tightly structured groupings of moderate-sized communicating applications. There is a need to cater for incremental development balanced with available resources and the rate of takeup of application increments into the business environment.

We are concerned strictly with data processing systems, not with office automation, document processing, or other associated systems to which interfaces will be required. For the purposes of this paper we can divide data processing systems into three main types, namely operational or transaction processing systems, managerial or short term control systems, and strategic or longer term planning and control systems. The application class we are concerned with covers small to moderate volume transaction processing systems which update a database from which managerial reports and related control information is derived. For definiteness, the application volume range we are considering is from 1 to 60 (user) transactions per minute, though this is in terms of today's technology and is merely a general guide. The application databases, if measured relationally after normalization, will typically contain hundreds of relations rather than thousands, i.e. they will be generally comprehensible to one developer. We specifically exclude the strategic, planning or decision support system (DSS) functions, which are less well-structured, frequently use information from external sources, and often need ad hoc development or modification. Suitable database extraction tools interfacing to DSS and related tools are, of course, necessary.

## 2.2 Target system characteristics

Our proposal concerns a relatively limited or constrained class of data processing systems which is nevertheless very common in business applications, and is important for this reason. They are concerned with data processing rather than data processing. This class may be characterized as:

(i) Data-centred. The main activities are keeping a database up to date and extracting information from that database as required; the application either falls naturally into this mould, or can be cast into it. Module data dependencies are through the database or through a handful of parameters, rather than through a data flow network.

(ii) Few major object classes. Most, if not all, of the modules which interact with the database can be regarded as instances of just a few object classes, such as menus, screens and windows (all user interfaces), file-to-file updates or reports. These objects can inherit their standard behaviour from general, or in some cases particular, objects of each class which are tailored to fit each specific instance.

(iii) Simple state transition control mechanism. Intermodule control flow is typically through menus and can be represented as a state transition model.

(iv) Having comparatively low procedural complexity. This characteristic has several aspects. Firstly, application-specific manipulation, logic or calculation represents a relatively small proportion of the total job. However, since this part is specific and contains little that can be inherited or delegated, it may represent a rather larger proportion of the total effort. Secondly, procedural modules are in general independent of each other and are called from, or embedded in, the database manipulation object instances.

Figure 1 gives a simplified diagram of the application class in a schematic data flow diagram form. The interaction process represents a menu, screen or window. The processes P1 to P5 represent embedded or called logic modules to meet application-specific needs. Based on our experience with 4GL applications of similar structure, these can often be a mere handful of lines. Note that the main process types, A, B and C, are not connected directly by data flows, but all interact with the database. This is an oversimplification in that the menu-like control structure, which is not shown, effectively passes activating information from one process to the next; also, it is sometimes convenient to pass a few transient variables from one process to the next. This is best shown on a modified state transition diagram. The system structures of interest are the data model and the control state transition diagram, not the data flow diagram.

This class includes many database applications, whether hosted from a language such as COBOL, SQL-based, or implemented using one of a large number of 'general' 4GLs. Many business applications fall more or less into this class. Those that fit well will benefit most from the type of environment we advocate. Those that fit less well will obviously benefit rather less depending on the effort and ingenuity needed to cast them into the required mould. It is a matter of having suitable object classes and being able to take advantage of the economies of inheritance. If the object classes are not suitable, effort may be increased rather than saved. Clearly in appropriate class additional and/or different object classes could be devised, but in most cases a development method different form, or more general than, the data-centred approach would be more suitable.

![](/api/attachments/869DKPVS/fulltext/images/31a69f7140d40de29810e2d957b650918877c94905aafd802d2d2ff31bed9b3e.jpg)  
Figure 1. Schematic data flow diagram of target application class

## 3. A tailored CASE environment

## 3.1 Motivation

(i) Existing CASE tool collections don't seem to quite fit. The medium-sized data-centred business application is a common type of application for which most sets of CASE tools that we have examined are not ideally suited, in spite of their apparent generality. Some 4GLs, on the other hand, are successful in providing the rudiments on which a development environment relevant to this application class can be built. The difficulties, in a nutshell, are that most CASE tools are too general to be efficient in this situation, too unwieldy or costly for what they do, and do not yet comprise the most useful set of integrated development tools for this application class. We believe that a more specialized, yet more tailorable, CASE tool environment is needed which both takes full advantage of the special characteristics of the application class and also has built-in rule-based mechanisms to allow the developer to incorporate knowledge gained from experience into the CASE environment.

(ii) What developers in this application class want. From working with, observing and questioning developers working with data-centred systems, from asking "What annoys you most about the development environment you are using?" and "What are the things the system should be doing for you?", the main needs that emerged were:

(1) A completely integrated system dictionary - a change in one place should be sufficient to effect all consequent changes in an application

(2) Suitably tailored configuration control tools (3) Project control suited to incrementally developed data-centred systems

(4) Documentation that said why, not how

(5) A good integration of non-procedural and procedural ‘programming’.

Surprisingly perhaps, support of the systems analysis process, other than recording its results, and a desire for graphical front ends, are not as high on the list as one might expect.

(iii) Productivity the main motivation. However, the main motivation is, as it has always been, greater productivity. We want to develop and evolve applications more cheaply without loss of quality or, given the parlous state of much software, with improved quality. System quality is difficult to define precisely but it includes reliability, understandability, friendliness, maintainability, etc. We should at this point look in general terms at where productivity gains can be made. Some gains can be made be removing the busy work that developers do in activities such as chasing the implications of a change through an application; some gains arise from better project control resulting in more effective management of development resources. We believe, however, that by far the greatest gains are to be made by not reinventing wheels but by reusing, or inheriting, standard objects or components and tailoring them to the immediate needs. This is what good 4GLs do. They contain standard templates for menus, screens, windows, reports, etc., whose parameters are forms which the user fills in. Not all 4GLs have been as successful as their proponents claim, however, for a number of reasons. Most of those we have seen have not made the best choice of standard components, have somewhat awkward inheritance mechanisms, are not as well integrated around a central system dictionary as they should be, and are not integrated into a total CASE environment.

(iv) No silver bullet for all werewolves. (Any reader who has not already read Fred Brooks' 'No Silver Bullet' article (Brooks, 1987) is strongly recommended to do so.) A further motivation for our particular proposal is our distrust of what we may call the 'PL/I syndrome' that we observe in many CASE tools – a desire to be all things to all users. Frankly we are skeptical about a workbench environment for all development seasons. Reusability, and hence productivity, is likely to be greater in narrower application classes where essential differences between instances are likely to be less or, in Brooks' terms, the differences are more of accidents than of essence. As with PL/I, too generalized an environment contains too many things that one doesn't want, would rather not know about, but cannot totally ignore. Even the modest proposal we present here is difficult to tailor to particular needs and experience within its narrow application class. Tailoring a generalized tool for productivity, ease of learning and ease of use seems a tall order. Hence our concentration on one particular common application class.

(v) Simplicity. Many existing development tools seem to their users to be over-complex. Some project control systems have several thick manuals, as do some 4GLs. Add the rest of the desiderata and one might well get a shelf full of CASE environment documentation, particularly if generality is a design goal. This seems excessive. Clearly, there are no simple solutions to difficult problems, but some are simpler than others. We hope that concentrating on a particular application class may cut some of the verbiage, reduce the number of concepts that have to be mastered, and lead to manuals of manageable and readable size.

(vi) Cost effectiveness. The environment and its tools, together with associated costs of education and/or expert staff or consultants, maintenance, etc., must be priced at a level which makes it thoroughly worth-while for a medium sized organization or division to use. Such an organization or division may have equipment in the \$100,000 to \$2,000,000 range, and between 2 and perhaps 20 development staff from business analysts to programmers, though in many such organizations strict divisions between classes of development staff are somewhat blurred and the analyst/programmer is not uncommon.

(vii) Relevance with flexibility. We have already noted that any particular developer has a specific problem at any particular time and wants tools to help solve that problem – not all the world's problems. On the other hand the same developer will undoubtedly be faced with a somewhat different problem, usually of the same general type, tomorrow. Also most developers learn from their own or others' previous experience with similar systems and would like to build what they learn into the tools they use. We thus want an environment that fits the problem class without imposing too much constraint on the solutions, and which allows at least some of the less stable, or more debatable, rules to be changed.

## 3.2 Some constraints on CASE requirements

There are, of course, many problems with any proposed set of CASE requirements, one being that it is very open to criticism of its omissions. Every additional tool and feature, however, raises the cost and complexity of a CASE environment. We prefer an approach which takes moderate steps into the unknown, building on the experience acquired along the way.

It is perhaps appropriate at this point to examine in general terms some of the main omissions, or design constraints, in our proposal.

(i) It doesn't attempt to do our thinking for us. We regard tools as extensions of the developer's skills, not replacements for them. We take the view that problems are more likely to be solved by two or three gathered together round a whiteboard, than around a workbench – which is still a more formal one-on-one situation. We regard a workbench as good for recording solutions, checking their consistency, reporting on their progress and helping to implement them, rather than for providing, or even assisting, inspiration.

(ii) It excludes most analysis and overall design but starts with the results of these activities in the form required for highly productive and reasonably efficient implementation. These activities are recorded in the system dictionary which contains the organization profile, the data model, (abstract) requirements, e.g. report content structures, documentation, procedural entries, and volume data as well as data description entries.

(iii) It is not methodology-free because some methodologies or approaches are more suited to the application class than others. In particular, data flow analysis is often less helpful than semantic data modelling. The development methodology used is constrained at its end point, in that its products must be either the precise inputs required, or capable of being mapped readily into those inputs.

## 3.3 What for whom

3.3.1 The elusive user. When considering CASE tools we are concerned with two not necessarily disjoint classes of users. First, those that use the CASE environment, who we will term developers, and second those who use the developed, or developing, system, who we will call users. We hesitate somewhat to use the term end users, who would seem to be those at whom the information (and possibly the buck) stops, and who may in some cases be a step or two removed from those who interact directly with a system.

## 3.3.2 Who then, will get what?

(i) The user. In these proposed requirements we do not cater for direct user interaction with CASE tools. We regard the kind of view definition and integration which this presupposes as too difficult a problem for efficient low cost CASE tools at this stage. In our experience most users, particularly most managers, want to do their job, not the IS function as well, or instead. Even if they had the inclination, few have the time. Of course they need to be involved, but most of them soon discover that experts in the IS area are vastly more productive in the actual development of complex systems than they are.

(ii) The manager. Here we refer to a development manager who, of course, may be a user. He needs project control, including costing, budgeting and scheduling, progress reporting, version control and documentation.

(iii) The analyst. The analyst needs documentation and interaction with the system dictionary which records, and where possible checks, all the products of analysis including the (semantic) data model, the menu/control structure, report contents, special process descriptions, backup and recovery requirements, test data, etc.

(iv) The designer. The designer is also primarily concerned with the system dictionary, but more with realization than with requirements – in particular such matters as the mapping of the semantic data model into the database/file system used (which may be largely automatic), the design of specific objects and object hierarchies where sufficient commonality exists, and other matters such as the optimization of high volume transactions or reports, test database setup, backup and recovery design, etc.

(v) The developer. The developer needs an integrated support environment based on an active mode of system dictionary use with effective version control and tailored testing aids including, for example, an automatic record of all database changes made when and where during test execution and an 'as you were' operation to restore the database to its original condition.

## 4. A basic data-centred case environment

## 4.1 Scope of description

Clearly we can only hope to delineate a few main features of the proposed environment within the scope of a paper of this sort. We have therefore selected, not in order of importance – which is indeed difficult where such a degree of integration is necessary – some nine of the main desiderata. These fall into two groups, general features that could, and indeed should, grace all such workbenches and features specific to this particular proposal. Since they are intertwined, however, we will not attempt to separate them at this stage, preferring to highlight the features which are specific at the end of this section.

## 4.2 Inclusion of estimating, costing, project control and configuration control

It is our contention that these tools are of critical importance in high productivity situations where limited resources are being used to introduce, or further develop, applications on tight time scales. Moreover, the tools must be tailored to the application class. Estimating, costing, monitoring and progress reporting must be in terms of the numbers, types, sizes and status of system dictionary entries, for example data objects of various classes, module objects of various types (such as window classes and instances, or abstract report requirements (unformatted content descriptions)). Development data should be collected automatically, updated continually, and alarms raised as appropriate.

Anyone who has worked with high productivity tools in incremental development situations will know that good configuration control, tailored to the appropriate life cycle, is a must.

## 4.3 Knowledge-based management tools

Though we need the management tools of 4.2, unfortunately we do not yet know the best ways of managing projects using new environments, nor of costing them or estimating their schedules. We thus need ways of building knowledge gained by experience into our tools. A method of doing this has been described in Cowderoy and Jenkins (1988). The flexibility an approach like this provides is critical to good project management, which must be based on the best sequence of estimates available, using rules which can improve over time, to provide standards against which to measure performance and productivity.

## 4.4 Integration of development and management tools

This has two major aspects. The first is a common project database in which management and development information is thoroughly integrated and where any change in (a version of) the system dictionary is reflected in all possible uses of that component and in the system status. The former is the result of having an active system dictionary during development. The latter involves recording every development event, or at least a summary of each event, and updating all status information affected by it. This is, however, easier to say than to do effectively. The volume of potentially useful data is massive, the definition of status information fuzzy around the edges, and the management part of the database likely to be rather inflexible. Rules can let us use the information in different ways, but the database design is critical.

The second aspect of integration, namely a common and consistent interface, is relatively more straightforward and is becoming usual in modern environments.

## 4.5 Separation of development and production

The workbench approach to development, in the sense of the original Programmers' Workbench (Ivie, 1977), is crucial. That is, development should not be done using the same software on the same machine as production, since there are always conflicts both of interest and for resources. Development must be done in a logically, and preferably physically, separate environment. The requirements of development are quite different from those of production. Development uses all the cross-reference relationships available between data objects, module objects, documentation and project management, with on-line updates wherever possible. It makes full use of the delegation (or inheritance) structure within the active system dictionary, thus ensuring consistency and development efficiency at what would be a prohibitive cost to production efficiency. Of course, one needs to run applications within the development environment, but even here the needs are different from production, requiring connection to test databases, tracing, intervention of various sorts during execution, monitoring and reporting of all changes, source level debugging/oranimation, and other needs more suited to an interpretive mode than to compilation. Production, on the other hand, is concerned with run time efficiency, operator convenience, security, recovery, etc. The differences are so great that one wonders that development tools are still being compromised by production needs.

## 4.6 System dictionary active during development

An active dictionary can be defined as one which must be referenced whenever any object in it is used. The term ‘executable dictionary’ may be even more appropriate (Docker, 1986), but the system dictionary contains much that is not executable, so we will use the more usual adjective ‘active’. The significance of an active system dictionary during development is evident from the foregoing. It ensures development integrity, provides a relatively straightforward mechanism for inheritance, and results in a degree of integration lacking in most existing systems. We have discussed this briefly here under a separate heading in order to emphasize its central importance.

## 4.7 More semantics in data modelling

Data-centred business applications lend themselves particularly to semantic data modelling, which is inherently more meaningful, particularly to the user and analyst, than relational models, for example. Classes, or abstraction hierarchies, of entities provide powerful as well as natural modelling concepts. We find the SHM+ model described by Brodie et al. (1984) attractive, but any state-of-the-art object-oriented data model would be appropriate. An automatic mapping into the implementation database (e.g. relational, network, Pick, etc.) is necessary with provision for designer override for optimization purposes. These requirements are a big step up from the vanilla entity-relationship models available in most CASE tools at the time of writing.

## 4.8 More explicit and thorough use of functional inheritance mechanisms

As noted earlier, good 4GLs achieve their productivity gains by reuse of standard objects, such as windows of various types. Unfortunately none that we know of do this in a thoroughgoing way. Thus, there tend to be relatively few standard objects, with only one level of inheritance. For example, a data entry window inherits the functions of a general window which are then tailored to the specific fields, prompts and purpose (data entry) of interest. Related sets of data entry, maintenance and deletion windows, where separate windows are necessary, usually have to be defined separately and cannot have a common data-field-specific window ancestor. As a result, one tends to indulge in a good deal of copying and modification of copies, which is a strong symptom of possibility of further use of inheritance. In our experience rather more classes, and several levels, are required, together with multiple inheritance. An active system dictionary can provide a mechanism for inheritance during development.

## 4.9 A language suited to procedural fragments

Many objects, such as windows, require specific procedural fragments. These use data already explicitly imported by the object in question, and defined in the system dictionary, so apart from some strictly local working variables, or global system variables and constants (such as date, time, company/division name, etc.), data definition is not a great problem. There should be facilities for defining local variables, or for making dictionary variable entries. Good string processing and calculation facilities are most important. Sub-routines with parameters are necessary, but may not be used particularly often. Most procedural fragments will be small, many just one line. From studies of 4GL applications we have found that their size distribution is heavily skewed, with a mode around 1–4 lines of code and a long tail up to perhaps 100 lines. In our experience few 4GL-type systems have done a good job of marrying their procedural and non-procedural elements. A modified version of an existing language, such as COBOL, or some versions of structured Basic, could be used. In cases where most of a system is data-centred, but a small part is procedurally complex, an interface to a full conventional procedural language, with suitable mappings to and from the system dictionary, will be necessary.

## 4.10 Features specific to these proposed requirements

These are features that take advantage of the characteristics of the application class, namely:

(i) Built-in system dictionary objects, windows, reports, etc., and their relationships to data model objects; the menu-like state transition control structure suitable for menu-driven applications, i.e. the architectural structure of the data-centred application class. Briefly, the system dictionary is built for this class of system, though parts of it, e.g. project control, may have more general application, and some parts, e.g. the creation of new classes, say of deletion windows, provide a measure of extensibility.

(ii) Inheritance mechanisms which apply to the base objects of the environment, and those derived from them, and which are implemented through the system dictionary.

(iii) Integration with 4GL-like development and production tools tailored very specifically for this class of application.

(iv) Project, estimation and version control which understand the objects of interest, and the development methodology products, necessary for the application class.

(v) Diagraming and documentation tools specific to the underlying models, e.g. transition diagrams with parameter passing, specific data model diagrams, e.g. SHM+.

To sum up, it is the system dictionary that has, at least in part, a quite specific structure, containing quite specific base object classes and mechanisms, particularly suited to this type of application. This is what, through reuse/inheritance, gives productivity gains.

## 4.11 Requirements and reality

Few of the CASE tools we have so far seen adopt the application-specific approach we have advocated. The few CASE tools that do specifically target the business information systems market are still too general in their approach, attempting to cover a wide range of methodologies, or even to be methodology-independent – which we believe is both impossible and unproductive. They place too much emphasis on structured analysis and structured design and too little, or none, on state transition menu structures which are almost universal in such systems. None, as yet, has attempted to realize the potential of a fully active development dictionary implementing powerful inheritance mechanisms. Case suppliers seem to be very reluctant to integrate any metrics, estimation or monitoring facilities within their products.

## 5. Comments and conclusions

It has only been possible to give a brief account of the most important features that we believe should form a part of a CASE environment for the class of data-centred business applications. A number of aspects, such as documentation, have been barely mentioned, not because we do not consider them

important, but because they are not so central to this particular proposal. Inevitably, in a brief description of requirements for something as large as a CASE environment, there are loose ends, strands not tied up, and concepts not rigorously defined. We trust, however, that the main points are clear.

Our requirements are modest in that they do not attempt to solve all the world's CASE problems, but merely to take some steps towards solving those of one particular narrow, but common, application class. They are not so modest in the approaches and tools advocated for use within the tailored environment, namely estimating, costing, project and configuration management with changeable rules, an integrated project/system dictionary, different development and runtime environments with the system dictionary active during development, semantic data modelling, and substantial use of inheritance.

While our requirements set addressess a specialized CASE environment, much of it consists of adaptations of tools, such as project control, or methods, such as the use of an active system dictionary and a knowledge-based approach, which are of much more general applicability. Thus the cost of construction of such an environment could well be shared in large part with the cost of other CASE environments, either of a general, an intermediate, or a specific nature.

The limitation of the proposed set of CASE requirements to a rather narrow but common application class should result in increased relevance, greater simplicity, and above all substantial productivity gains through the use of standard object classes and inheritance as well as through the use of a class-specific system dictionary and associated tools. As a corollary, we see the object-oriented approach with suitable inheritance mechanisms, possible through an active system dictionary, as being a promising approach to productivity in future CASE environments.

## References

Brodie, Michael L. and Ridjanovic, Dzenan (1984) On the Design and Specification of Database

Transactions. In M.L. Brodie, J. Myloponlos and J.W. Schmidt (eds) On Conceptual Modelling. Springer-Verlag.

Brooks, Frederick P., Jr. (1987) No Silver Bullet. IEEE Computer 20(4), 10–19.

Cowderoy, A.J.C. and Jenkins, J.O. (1988) Preparing for Knowledge-Based Cost Estimation of Software Developments. Proceedings of the Joint International Symposium on Information Systems, Sydney. Australia.

Docker, T.W.G. and Tate, G. (1986) Executable Data Flow Diagrams. In D. Barnes and P. Brown (eds) Software Engineering '86. Peter Peregrinus LTd.

Ivie, E.L. (1987) The programmers' workbench – a machine for software development. Communications of the ACM, 20(10), 746–53.

## Biographical notes

Graham Tate is a professor of computer science at Massey University. He has thirty years experience in computing and is a consultant to government and commercial organizations and a member of a government computing policy committee in New Zealand. His main area of current research is in software economics and metrics with particular application to CASE tools.

June M. Verner is a lecturer in computer science and information systems at Massey University and a consultant to government and commercial organizations in New Zealand. Her current research is in software engineering economics, particularly software size estimation.

Richard Hayward is a senior lecturer in information systems. He has over twenty years computing experience and prior to joining Massey University he was a senior consultant with a leading consultancy organization in the UK. His current research is in information systems strategy.

Address for correspondence: Computer Science Department, Massey University, Palmerston North, New Zealand.
