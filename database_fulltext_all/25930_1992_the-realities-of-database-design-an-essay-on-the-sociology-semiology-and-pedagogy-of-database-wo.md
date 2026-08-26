---
otero_id: 25930
otero_key: "XPG2TW95"
title: "The realities of database design: an essay on the sociology, semiology and pedagogy of database work"
authors: "Paul Beynon‐Davies"
year: "1992"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1992.tb00076.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The realities of database design: an essay on the sociology, semiology and pedagogy of database work

Paul Beynon-Davies

Department of Computer Studies, Polytechnic of Wales, Pontypridd CF37 1DL, UK

Abstract. This paper discusses the way in which a branch of information systems development — database design — takes its context from a sociological and semiological analysis. The two major objectives of this paper are:

(a) to discuss strategies for teaching this material to undergraduate students of computing,

(b) to identify potential new directions of research in the database area.

Keywords: conceptual modelling, database design, information systems development.

## INTRODUCTION

Recently Backhouse et al. (1991) have called for a focus for Information Systems research. They have proposed an organizing framework based on the disciplines of sociology and semiology.

Two well-established areas of study provide us with a firm foundation on which to build. These are sociology on the one hand and semiology on the other. The former already constitutes the main thrust of research into social organization, institutional dynamics, group interaction, working conditions and social policy. The latter brings together the range of studies associated with contexts of language and communication, means, grammars, signs and codes.

The author is very much in sympathy with this proposal (Beynon-Davies, 1990), which dates back at least to the early theoretical work of Stamper (1973). What is clearly needed however is a number of practical demonstrations of the utility of this framework, particularly for information systems professionals.

This paper discusses a personal attempt to locate this framework within practical information systems work. It constitutes an essay on the way in which a particular branch of information systems development — database design — takes its context from a sociological and semiological analysis. The two major objectives of this paper are:

(a) to discuss strategies for teaching this material to undergraduate students of computing,

(b) to identify potential new directions of research in the database area.

We first place database design in a sociological context by providing a critique of the preferred reading of database design given in the literature. A discussion follows of a small case study in database design. This study has been presented to computer studies undergraduates by the author in an attempt to illustrate the way in which systems development is at least as much a social exercise as it is a technical exercise.

The second part of the paper develops a short semiological analysis of a fundamental database design technique — namely, entity-relationship diagramming (E-R diagramming). Using the example of the case study we illustrate how the conception of an E-R diagram as a sign system explicates some of the key problems experienced in the teaching of data analysis.

## CONCEPTUAL MODELLING

In (Beynon-Davies, 1989) I discussed the premise that information systems development is primarily a task of conceptual modelling. That is, a process of successive refinement through a number of different levels of information model. Systems analysis is equivalent to requirements modelling, systems design is equivalent to logical modelling, and systems implementation is equivalent to physical modelling (see Figure 1).

Database development is a prime example of this modelling process. A database is a model of an evolving real world. The state of a database, at a given instance, represents the knowledge it has acquired from this world. But as Sowa (1984) cogently puts it:

... models are abstractions of reality. The systems analyst or database administrator must play the role of philosopher-king in determining what knowledge to represent, how to organise and express it and what constraints to impose to keep it a consistent, faithful model of the outside world.

## Five key assumptions

This model of database development is useful in identifying database design with abstraction. As a model itself however it is overly simplistic. This is because, as an instance of conventional systems development practice, it is founded on a number of key ontological assumptions (Hirschheim & Klein, 1989):

Objective reality. Most database design techniques treat the real world as a given. They assume that there is one reality that is measurable and the same for everyone.

Objective management. Management is assumed to lead an organization via clearly defined system objectives designed to improve organizational efficiency.

Technical expertise. The primary role of the database developer is to be expert in the technology, tools and methods of database development.

![](/api/attachments/XPG2TW95/fulltext/images/95697fd4dbaa83a2fc0c2f6922c3f83a2fa58a6760fb1f6047942a3a8a19e27b.jpg)  
Figure 1. The database development process.

Reality modelling. Database systems development is the task of designing systems that model reality. Database systems are cast as utiliterian tools for management to achieve their ends. Organisational concensus. Organizational 'politics' are irrational and interfere with maximum efficiency and effectiveness. As such, they are treated as external to the realms of consideration.

In essence these assumptions are based on a limited conception of the culture of organizations. In the tradition of systems theory (Silverman, 1976), organizations are generally presented in the database literature as well-structured formal information systems. The application of computerized information systems occurs within a relatively well-bounded area of this formal domain. Figure 2 illustrates this idea.

## A critique of assumptions

The assumptions described above are clearly open to a critique from a sociological position:

Subjective reality. Reality is socially constructed. Reality is a continuing negotiation between actors in the social world (Berger & Luckman, 1971).

![](/api/attachments/XPG2TW95/fulltext/images/be4f3bc5086591946b4e9b85fbad95a4469f13f1f5324fe09915a5ab28381281.jpg)  
Figure 2. Levels of information system.

Subjective management. Management frequently do not have any clearly defined goals. They may also hold objectives which conflict with organizational effectiveness.

Human expertise. Most data analysts find themselves doing more human-related work than technical-related work (Beynon-Davies, 1990). Technical expertise is often used more as a vehicle for exercising power over users than as a tool for improving organizational efficiency (Markus & Bjorn-Anderson, 1987).

Reality shaping. Database design is usually about modelling one particular group's conception of reality — i.e., some sub-group of management. This conception may conflict with the perceptions and expectations of other organizational groups. Information systems development is not simply 'engineering'. It is at least as much organizational innovation (Keen & Gerson, 1977).

Systems conflict. Organizational 'politics' are the stuff of which information systems are made. The management (not necessarily the resolution) of organizational politics is probably one of the best ways of improving organizational effectiveness (Keen, 1981).

Any formal information system takes its context or direction from the informal information system that surrounds it. The informal information system sets the shape of the organizational reality. It determines the shape of management objectives and determines the direction of organizational 'politics'.

## A case study in design

The text which follows provides a short narrative description of the workings of an existing manual system. This is initially presented to computer studies students as a problem in systems analysis. Using the information provided as a starting point they are asked first to conduct a conventional data analysis of the system.

Goronwy Galvanizing is a small company specialising in treating steel products such as lintels, crash barriers, palisades, etc., produced by other manufacturers. Galvanizing, in very simple terms, involves dipping steel products into baths of molten zinc to provide a rust-free coating. Untreated steel products are described as being black products. Treated products are referred to as being white products. There is a slight gain in weight as a result of the galvanizing process.

Black products are delivered to Goronwy on large trailers. Each trailer carries a series of bundled products known as batches. A batch is made up of a number of steel products of the same type and is labelled with a unique job number. Each trailer may be loaded with a number of different types of steel product and is labelled with its own advice note detailing all the associated jobs on the trailer.

Goronwy mainly process lintels for a major steel manufacturer, Blackheads. The advice note supplied with trailers of Blackhead's lintels is identified by an advice number specific to this manufacturer. Each job is identified on the advice note by a job number generated by Blackhead's own check-digit routine. Smaller manufacturers like Pimples supply an advice note on which jobs are identified by a concatenation of the advice number and line number on which the job appears.

Each job, whether it be for Blackheads or Pimples, is also described on the advice note in terms of a product code, a product description, item length, order quantity and batch weight. Each advice is dated.

When Goronwy have treated a series of jobs they will stack white material on trailers ready to be returned to the associated manufacturers. Each trailer must have an associated advice note detailing material on the trailer. Partial despatches may be made from one job. This means that the trailer of white material for despatch need not correspond to the trailer of black material originally supplied to Goronwy. The despatch advice is given a unique advice number and is dated. Each despatch details the job number, product code, description, item length, batch weight, returned quantity and returned weight.

Later on, the idea of an informal information system is introduced into the discussion. Concepts such as norms, social roles and organizational sub-cultures are discussed. The key analogy is made between the systems analyst and the social anthropologist (Beynon-Davies, 1990). This serves to prepare students for a small exercise in organizational analysis.

The organization at Goronwy is made more concrete by providing three short sketches of key players in the systems project: Richard Sawyer, Robin Fryer and James Richards. These represent stereotypes of users. The sketches are presented below.

Richard Sawyer. Richard is a systems consultant from the headquarters of the owning company. Richard feels his remit is to manage the quality control of the project. The systems consultancy division never code systems themselves. They are expected, however, to oversee all systems development within the parent company.

Robin Fryer. Robin is the works manager at Goronwy. Robin wants a computer system to enhance the prestige of his brand-new plant. If the system is seen to be successful then it will probably be demanded by other galvanizing plants. Robin is also of the impression that a computer system will give him a 'tighter-ship'.

James Richards. James is the production controller at Goronwy. James will eventually be given responsibility for running the information system. He is, however, less than happy with the project. He feels that the system is unlikely to be worthwhile. He is perfectly happy with the existing manual system.

## The exercise in organizational analysis is then portrayed in the following terms:

You are a contractor brought in to develop a micro-based system for production control. Richard and Robin have already discussed the proposed system in depth and Richard has produced an initial requirements analysis/system specification which he presents to you at the first development group meeting.

Produce, in writing, a brief description of how you think the development will progress. In particular, address the following questions:

(a) What do you think your role is going to be?

(b) What role do you think Richard, Robin and James will take?

(c) Who do you think is the best person to talk to concerning how the system should look?

(d) What problems do you expect to encounter?

(e) How do you think the new system will be used?

In two years of running this exercise the author has been pleasantly surprised at the results. Working in groups, most students see the relevance of an informal analysis of information systems as part of systems analysis. There is still however something of a 'social engineering' ethos which comes across in the responses. The excerpt below is a composite of some of the best responses I have received from students:

## What do you think your role is going to be?

Richard sees me as a servant. I am going to build a system to his specification.

Robin sees me as a miracle-worker. I am going to solve all his problems.

James feels I am going to make his life difficult, perhaps even get him the sack.

My role is actually a 'mediator'. I need to keep everyone as happy as possible, if the system is going to be successful.

What role do you think Richard, Robin and James will take?

Richard is a know-it-all who will want to oversee the project.

Robin is not really interested in the specifics of the project. He just wants to see the results. James is depressed and will do everything in his power to disrupt the project, unless I persuade him otherwise.

Who do you think is the best person to talk to concerning how the system should look? I have to talk to everybody, but James is probably the person I should talk to the most, from day one.

James only knows the specifics of Goronwy. If the intention is to make this system a 'flagship' for other plants then Richard's point of view must also be taken into account.

What problems do you expect to encounter?

Richard being bossy, Robin being confused and James being downright awkward.

I need to bolster James' enthusiasm. I need to dampen some of Robin's enthusiasm. I need to preserve Richard's position without straight-jacketing myself.

How do you think the new system will be used?

If I upset James it will never be used or he will use it incorrectly.

The objectives of this exercise are summarized in a series of adages presented to students:

(a) people problems are probably the most important problems in information systems development,

(b) most systems development projects fail because of people problems,

(c) maintenance is a people problem,

(d) always investigate people interactions before anything else.

The overall intent of this exercise is to illustrate the type of material that is needed to redress the technicist imbalance in computer studies training. Computer studies students, in my experience, generally treat the findings of the behavioural sciences with some disdain. This, I feel, is largely because they see no direct practical application of such findings to the problems of information systems development. What is clearly needed therefore is more material which demonstrates the importance of social science concepts to information systems work.

## SEMIOTICS

In this section we turn our attention from the global analysis of sociological context to a specific analysis of the application of semiotics to database design.

Semiotics (in the Anglo-Saxon tradition), or semiology (in the Franco-Italian tradition) (Guiraud, 1975), is the study of signs (O'Sullivan et al., 1988). It has a history dating back at least to the stoic philosophers, through medievalists such as Roger Bacon, to John Locke, Charles Morris, and modern supporters such as Ronald Stamper (Stamper, 1989). However, semiotics is not usually seen as an academic discipline. Stamper describes it as 'not so much a new subject, as a regrouping of ideas from many disciplines having their own private jargons, and little intercommunication' (1973).

Any sign must have three essential characteristics:

(a) it must have a physical form,

(b) it must refer to something other than itself,

(c) it must be recognized and used by people as a sign.

Take the example of a rose. A rose is normally just a flower. If a young man presents a rose to his girlfriend however it becomes a sign. It then refers to, or stands for, his romantic passion, and both he and she recognizes that it does.

This example illustrates the fundamental model of semiosis — sign production and use. A sign stands for a referent. Hence, a baby crying might be taken as signifying hunger, flags might be taken as signifying nations, flowers might be taken as signifying love. Signs are however inextricably linked with agents. The stands-for relation is founded in human interpretation. Although one person might interpret a given sign as standing for a given referent, another person might disagree. He might take it as signifying something entirely different. Hence, statements about agents, signs and referents cannot be made in isolation from each other (Eco, 1976).

The problems of semiotics are usually classified under three major headings: pragmatics, semantics and syntactics. Stamper adds a fourth to this list which he terms empirics. He defines these categories in the following terms (1975):

(a) pragmatics: signs in relation to human behaviour,

(b) semantics: how signs are related to the 'real' signs they signify,

(c) syntactics: the formal relations among signs,

(d) empirics: the statistical relations among sets of signs.

Although spoken language has been used by many as their prime example of a sign system, semiotics has been particularly successful in its analysis of other media such as literature, cinema, advertising, photography and television (Barthes, 1973).

In this respect, the literature discusses the inter-linked processes of authoring and reading signs. Sless (1986), for instance, discusses the way in which authoring a written text cannot take place without projecting a reader of the text. The process of writing this paper, for instance, could not take place without some idea of its proposed audience.

A text is open to a number of potential readings, but normally is said to prefer one. Hence, it is usual to refer to the 'preferred reading' of a text. Alternative readings to the preferred one usually derive from differences in the cultural experience of author and reader. Hall et al. (1980), for instance, make a useful distinction between three main types of readings. The texts they refer to are actually television programmes.

1 The dominant reading which accepts the text according to the assumptions of the encoder. This is the preferred reading.

2 The negotiated reading which accepts the legitimacy of the dominant assumptions, but adapts the reading to the specific conditions of the reader.

3 The oppositional reading which produces a decoding that is radically opposed to the preferred reading.

## Entity modelling as a sign system

The earlier quote by Sowa portrays database developments as building an abstraction of reality. This seems to place Sowa in the camp of those persons who assume that there is an objective reality to be abstracted from. However, we did something of an injustice to Sowa in deliberately leaving off a crucial last sentence from the quote:

To do a good job in analysing reality, a systems analyst must be sensitive to semantic issues and have a working knowledge of conceptual structures. (Sowa, 1984)

Sowa, from this and other statements in his impressive work, clearly recognizes the importance of meaning in the development of database systems. This follows the tradition of portraying probably the most important part of database design — requirements analysis — as semantic modelling (Date, 1990).

However, there is something of a sleight of hand in the literature on database design. Although the importance of semantics is recognized, the primary area of research in the database area has been devoted to proposing more expressive syntactic tools for database design. Much work has gone into proposing architectures for representing semantics — the so-called semantic data models (Peckham & Maryanski, 1988). Little attempt has been made by the database community to encompass the growing literature on the social and psychological processes by which meaning is produced. Little effort has been devoted to investigating the way in which, for instance, semantic data models facilitate the capture of meaning. Little work has been directed at viewing semantic data models as tools for shaping conceptions of reality.

## Entity-relationship diagramming

Consider probably the most commonly used of all the semantic data models — the entity-relationship model (E-R model) (Chen, 1976).

In the E-R approach the 'real-world' is modelled in terms of entities, the relationships between entities and the attributes associated with entities. Entities represent objects of interest in the real world such as employees, departments and projects. Relationships represent named associations between entities. A department employs many employees. An employee is assigned to a number of projects. Employs and is assigned to are both relationships in the entity-relationship approach. Attributes are properties of an entity. Name is an attribute of the employee entity. Estimated duration of project is an attribute of the project entity.

![](/api/attachments/XPG2TW95/fulltext/images/7434dfadd30d6eb3e86120951a78d7e9da296fce42539b629c6552f7e3011ca1.jpg)

r1 - employs, is employed by

r2 - is assigned to, has assigned

Figure 3. A simple E-R diagram.

A popular diagramming technique is normally associated with the E-R model known as E-R diagramming. Figure 3 presents an E-R diagram which documents the assertions of the previous paragraph.

Klein & Hirschheim (1987) have presented a valuable framework for analysing the philosophical assumptions underlying data modelling techniques such as E-R diagramming. They discuss how current approaches to entity modelling ‘. . . follow in the footsteps of an objectivist tradition. Reality is a given “out there” and made up of discrete chunks which are called entities. Entities have properties or attributes. Both entities and their properties have an objective existence’. They contrast this with what they refer to as rule-based approaches to data modelling. Such approaches are heavily influenced by the subjectivist tradition. ‘Their proponents see the main task of data modelling as formalising the meaning of messages which are to be exchanged among a professional community’.

The main problem with this dichotomy however is that it assumes that the theory of data modelling is necessarily the same as the practice of data modelling. The theory of data modelling, which unfortunately is the most heavily documented, emphasizes the syntactics. The practice, which is poorly documented, is definitely based in semantics.

In other words, the database literature is heavily represented by notations and methods. The actual practice of applying these techniques is heavily resonant with the task of interpreting meaning.

To highlight this distinction we examine in the next section E-R diagramming as a semiotic system.

## A semiotic system

E-R diagramming is a semiotic system. When we teach a technique such as E-R diagramming we are also attempting to impart something of a method for interpreting reality.

Let us illustrate this idea first by considering a simple example and second by considering the application of this principle to the case study described above.

Suppose you are given the task of drawing an E-R diagram to represent a social convention such as marriage. The common difficulty experienced in drawing such a diagram is to decide whether marriage should be represented as an entity, relationship or attribute. In other words, we must choose to represent the same referent by a selection from a set of three possible signs.

In making such a selection however we are interpreting the world. Each possible sign has a computational significance which must be taken into account in the selection. Entities normally compute as files, relationships compute as integrity constraints and attributes compute as fields. Hence, if we model marriage as marital status (an attribute) we are explicitly assigning it a lesser role in our sign system than if we make it an entity or a relationship.

Semiosis can be seen at work in the process of teaching data analysis. If you set students a simple problem in E-R diagramming like the one described above the process of interpretation is made problematic. If you set a slightly more involved problem in design it becomes even more problematic. Providing a short snippet of description of some system is insufficient in itself to determine a solution to the problem. Students have to supply background knowledge and make assumptions. Many of these assumptions are based upon the process of projecting a reader for the system. Using the example of marriage again, making marriage marital status means projecting an implementation of a project as something like a personnel system. Making marriage an entity however means projecting a system such as a marriage registry.

To consider a more detailed problem, how does semiotics serve to enhance the data analysts' understanding of the Goronwy Galvanizing system? Some suggestions are given below.

1 At the micro-level, three different signs batch, job, and order-line seem at first glance to represent the same referent — a bundle of steel products to be processed by the plant.

The projected reader or agent of the sign is however different in each case. A batch is a sign used by people unpacking deliveries and bundling despatches. A job is of relevance to people galvanizing the material. An order-line is of relevance to clerks recording details of deliveries.

2 At the system level four different meanings can be assigned to the proposed production control system. Robin reads it as a status symbol, James reads it as a necessary chore, head office reads it as an experiment in information technology.

3 Authoring any requirements specification for a system therefore involves necessarily taking a position and projecting a readership. If there are a number of readers such as head-office, Robin, James, etc. then the analysis must involve a heavy amount of negotiation as to the true meaning of the text.

In some senses the process of semiosis would appear to be recognized by a technique known as view integration. This technique allows for the possibility that an entity model developed in association with a particular user or user-group may be different from entity models produced by other users and groups. Each of these so-called user views is subject to a process of integration. The purpose of this process is to build some form of union of differing user perspectives.

At first glance this technique seems to employ a more subjective assumption of reality than the preferred reading in the database literature. User views however are not usually seen as distinct versions of reality. They are normally portrayed as being different perspectives of the same underlying reality. There is still an assumption that at the end of the integration phase a consensus view of reality can be reached. View modelling and view integration still work within the assumption of an objective reality.

One conclusion we may draw from this analysis is that entity modelling is a process of semiosis that occurs in both the formal and informal systems domain. We might even say that the technique is usefully employed at the boundaries of formal and informal systems.

Entity modelling cannot take place without some assumptions taken from the informal context of organizations. An analysis of informal systems is therefore a necessary prerequisite for any data modelling work (Checkland, 1981; Avison and Wood-Harper, 1990). As Stamper (1985b) cogently puts it:

The typical data analysis . . . relies heavily upon the intuition of the analyst who tends not to be aware of the many subtle variations of meaning. The analyst imposes a kind of concensus of his own, by fiat! I think we shall have to be prepared for the design of semantic models to be far more complex than envisaged today.

## CONCLUSIONS

This paper has been based around the premise that many of the problems of database design arise out of a simplistic view of databases. To paraphrase Stamper (1975), a database can be viewed as a junction box through which many suppliers of information communicate with many users. Whilst there is plenty of scope for misunderstanding in face-to-face communication, and even more scope in written communication, it is rather naive to assume that we should be better able to communicate by means of files in a formal system.

In most of the available discussion of database development only the syntactic and empiric questions are seriously addressed. The pragmatic and semantic aspects are not discussed in great detail. Although not ignored by the competent data analyst they are usually dealt with informally. One of the main aims of this paper has been to attempt to resurrect some of the issues originally expressed by Stamper in the early 1970s; that information engineers should receive an equal training in the pragmatic and semantic aspects of information systems that they currently receive in the syntactic and empiric aspects.

Summarized here are some of the main conclusions that may be drawn from the discussion above under the two headings of pedagogy and potential research areas.

## Pedagogy

1 A sociological and semiological analysis of database work offers numerous insights into the underlying problems of this activity. Many of these insights revolve around the limited representation or model of systems development employed in the literature. Contemporary systems development practice is founded on a number of key assumptions. Each of these assumptions can be criticized on sociological and semiological grounds.

2 In much the same way as Winograd & Flores debate with the AI community about their over-emphasis of representation, we debate with the database community over their under-emphasis of the process of human interpretation (Winograd & Flores, 1987).

3 It is important that students of information systems (particularly computer science and computer studies students) gain an appreciation of the usefulness of such a sociological and semiological analysis.

4 Such an appreciation cannot be successfully imparted without concrete exercises in the analysis of informal systems.

## Research

1 Database research has primarily devoted attention to an analysis of form rather than content. To use the organizing framework for semiotics discussed earlier, most database research has fallen into the area of empirics and syntactics. Little attention has been paid to the pragmatic and semantic nature of database work. Hence, although semantics has been seen to underpin the database design process, most research has concentrated on suggesting modelling mechanisms with increased semantic content. Little attempt has been made to address semantics as a process of negotiation between user-groups and database designers.

2 Two strands of research into the pragmatics and semantics of database work demand further investigation. First, further examples of the application of a semiotic framework to practical projects in database design are needed. Such work is particularly needed to illustrate the process of database design in its guise as a reality-shaping exercise.

3 Secondly, a number of research projects are needed to critically examine the technology of database design, for instance, an analysis of semantic data models in terms of sign systems. Do abstraction mechanisms facilitate communication? Which modelling mechanisms encourage negotiation?

## ACKNOWLEDGEMENTS

I would like to thank Professor Ronald Stamper, Dr James Backhouse, and Professor David Avison for their valuable comments on earlier drafts of this paper.

## REFERENCES

Avison, D. & Wood-Harper, A.T. (1990) Multiview: an exploration in information systems development. Blackwell Scientific Publications, Oxford.

Backhouse, J., Liebenau, J. & Land, F. (1991) On the Discipline of Information Systems. Journal of Information Systems, 1, 19–27.

Barthes, R. (1973) Mythologies. Paladin, St Albans.

Berger, P. & Luckman, T. (1971) The Social Construction of Reality. Penguin, Harmondsworth.

Beynon-Davies, P. (1989) Information Systems Development. Macmillan, London.

Beynon-Davies, P. (1990) The Behaviour of Systems Analysts. Computer Bulletin, 2, 21–23.

Checkland, P.B. (1981) Systems Thinking, Systems Practice. John Wiley, Chichester.

Chen, P.P.S. (1976) The Entity-Relationship Model: toward a unified view of data. ACM Transactions on Database Systems, 1, 9–36.

Date, C. (1990) An Introduction to Database Systems, 5th edn. Addison-Wesley. Reading, Mass.

Eco, U. (1976) A Theory of Semiotics. Indiana University Press, Indiana.

Guiraud, P. (1975) Semiology. Roulledge and Kegan Paul, London.

Hall, S., Hobson, D., Lowe, D. & Willis, P. (eds) (1980) Culture, Media, Langauge, Hutchinson, London.

Hirschheim, R.A. & Klein, H.K. (1989) Four Paradigms of Information Systems Development. CACM, 32, 1199–1216.

Keen, P.G.W. & Gerson, E.M. (1977) The Politics of Software Systems Design. Datamation, 23, 80–84.

Keen, P.G.W. (1981) Information Systems and Organisational Change. CACM, 24, 24–33.

Klein, H.K. & Hirschheim, R.A. (1987) A comparative framework of Data Modelling Paradigms and Approaches. The Computer Journal, 30, 8–14.

Liebenau, J. & Backhouse, J. (1990) Understanding Information: an introduction. Macmillan, London.

Markus, M.L. & Bjorn-Anderson, N. (1987) Power Over Users: its exercise by system professionals. CACM, 30, 498–504.

O'Sullivan, T., Hartley, J., Saunders, D. & Fiske, J. (1988) Key Concepts in Communication. Routledge, London.

Peckham, J. & Maryanski, F. (1988) Semantic Data Models. ACM Computing Surveys, 20, 153–189.

Silver, D. (1976) The Theory of Organisations. Heinemann, London.

Sless, D. (1986) In Search of Semiotics. Croom Helm, Beckenham, Kent.

Sowa, J.F. (1984) Conceptual Structures: information processing in mind and machine. Addison-Wesley, Reading, Mass.

Stamper, R.K. (1973) Information in Business and Administrative Systems. Balsford, London.

Stamper, R.K. (1975) Information Science for Systems Analysis. In: Human Choice and Computers. Mumford, E. and Sachman, H. (eds). North Holland, Amsterdam.

Stamper, R.K. (1985a) Towards a Theory of Information: mystical fluid or a subject for scientific enquiry? The Computer Journal, 28.

Stamper, R.K. (1985b) Management Epistemology: Garbage In, Garbage Out. In: Knowledge Representation for Decision Support. Methlie, L.B. and Sprague, R.H. (eds). North Holland, Amsterdam.

Stamper, R.K. (1989) Information Management. Inaugural Lecture. Twente University, The Netherlands.

Winograd, T. & Flores, F. (1987) Understanding Computers and Cognition: a new foundation of design. Addison-Wesley. Reading, Mass.

## Biography

Paul Beynon-Davies spent a number of years in the computing industry as a programmer and analyst. He currently holds the position of lecturer in the Department of Computer Studies, Polytechnic of Wales. Dr Beynon-Davies has published four books on information systems topics:

Beynon-Davies, P. (1989) Information Systems Development. Macmillan, London.

Beynon-Davies, P. (1991) Expert Database Systems: a gentle introduction. McGraw-Hill, Maidenhead,

Beynon-Davies, P. (1991) Relational Database Systems: a pragmatic approach. Blackwell Scientific Publications, Oxford.

Beynon-Davies, P. (1992) Relational Database Design. Blackwell Scientific Publications, Oxford.

He has research interests currently in the areas of database design, knowledge engineering and the social dimension of information systems development.
