---
otero_id: 18359
otero_key: "NT98H8HR"
title: "Two views of information modeling"
authors: "Kalle Lyytinen"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90068-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Two Views of Information Modeling

Kalle Lyytinen

Department of Computer Science University of Jyväskylä SF-401100 Finland

The paper compares two views of information modeling. These are the reality mapping and the formal language development view. The former is the mainstream of information systems (IS) literature whereas the latter has received much less attention. Our comparison focuses on the definition of the information system in both views and evaluates some of their organizational consequences. The implications are discussed in relation to sets of beliefs underlying the two views. The paper concludes that both views are needed in IS design and they complement each other. However because the formal language development view is less articulated it is suggested that it should receive more research attention in the future

Keywords Information Model Conceptual Schema Information Modeling Enterprise Modeling Information System Information System Theory Organizational Impacts Database

![](/api/attachments/NT98H8HR/fulltext/images/65ef506d4697be1a9c277989b15aab87fc89608b745d30207abdbcbc3eb6edf0.jpg)

Kalle Lyytinen is currently an Associate Professor at the University of Jyvaskyla. He holds a PhD in Computer Science from the University of Jyvaskyla, Finland. His previous positions include research positions at the University of Stockholm and London School of Economics. He is known for his research work in the areas of information systems specification, information systems research methodology and information systems theories. He has published in MIS Quarterly and Information Systems, and in leading conferences He has also refereed for several conferences and scientific journals Kalle Lyytinen is a member of IFIP WG 82 "Information systems and Organizations" He is currently writing a book "Data Modeling- Conceptual and Philosophical Foundations" with Dr Rudi Hirschheim of the Oxford University and Dr Heinz Klein of the Suny Binghamtom

Kalle Lyytinen's research interests include system design methods and design methodologies, information system theories and frameworks management and planning of information systems as a strategic issue, IS research strategies and their selection

## 1 Introduction

As suggested by the ANSI/SPARC report [1] an information system (IS) can be viewed on three levels internal, conceptual and external. The conceptual level concentrates on the “meaning” (concepts) of information [5,7 17]. The task of developing a conceptual schema is called information modeling. Its major goal is to develop a stable and centralized description of the meaning of data – a conceptual schema. Information modeling thus differs from data modeling which evolved during the 70's and has the aim of describing data structure for access and storage of data, e.g., as a relation, a network or a tree [11]

This paper will discuss the notion of an information system as proposed in two views of information modeling. The first will be named a Reality Mapping (RM) view Approaches that are based on this view are common in the literature $[1,5,7,9,17\ 35]$ . It supposes a mapping process from the “real world” into a formal model - the conceptual schema. As a result, it represents the real world. Thus, an IS resembles models of science and engineering

The second view will be named Formal Language Development (FLD) Approaches founded on it are quite rate in the literature $[13,15\ 22,24,25,37]$ . It looks on information modeling as a process in which organizational rules are formulated, developed, and adopted. These will specify the content, form, and uses of formal language messages (data) communicated in an information system. Seen in this light, the use of an IS resembles that of mass-media for a local group

This paper will investigate sets of beliefs that determine what phenomena are the prime material for inquiry and information modeling [8] We shall discuss in more detail three beliefs which underlie both view's IS definition

## 2 On the Reality Mapping View

## 21 The IS-Definition

The basic tenets of the reality mapping view originate from analytical philosophy and mathematical logic. In particular such scholars as Frege [14] Wittgenstein [41] and Tarski [38] have been influential in its development

According to the RM view [17] an IS is a fully predictable, formal system that mirrors the deterministic behavior of the Universe of Discourse (UoD). It consists of two parts (Figure 1)

\- an information processor (IP), and

• a UoD description (UoDD)

The IP can change a state in the UoDD based on receipt of a message from the environment. The message contains either information about changes that have occurred in the UoD or it includes a command to retrieve parts of the UoDD and display them. In the first situation, the changes are “perceived” from the environment. In the second case, no change will occur to the UoDD

A UoD is a selected portion of a real or hypothetical world and it is assumed to be describable in some precise and formally defined language. All one can see in this world are entities and actions concerning one or more of them. All entities and laws about allowed actions are assumed to exist in the sense of naive realism, it is not depending on the users of the IS

A UoDD is a formal representation of the UoD. It consists of a conceptual schema (CS) and an information base (IB). A CS describes an abstraction of the UoD, ie classifications, rules and laws. An IB includes declarative sentences (first-order logic clauses) which state facts about entities

The RM view assumes that developers of the IS construct a unique mapping from a UoD to a UoDD (arrows 1 and 2) Hence the term reality mapping view

Three ideas are the cornerstones of the above IS definition. These are

(1) In the objective nature of the UoD that it can be “perceived” impartially

(2) In the factual, descriptive nature of information contained in the UoDD, and

(3) In the consensual role of the UoDD

The literature in information modeling does not discuss much these beliefs and they have not been exposed clearly. We have condensed them by a careful reading and analysis of some core works in the field. Though our results do not fill all the requirements of authenticity, we believe that they are consistent with the basic ideas of referenced works

## 22 The Objective Belief

A UoDD is a consistent collection of declarative sentences called well-formed formulas (wffs), free from any subjective or social bias, that truthfully represent the UoD

![](/api/attachments/NT98H8HR/fulltext/images/dfb0829295c157a23e46ef47011156b9b72ae1ede46e78e26d928f23c7cda06a.jpg)  
Fig 1 An information system in [19] Legend 1 classification and generalization 2 recording of facts

To formulate the UoDD, the UoD must be well understood. The perception results in knowledge about the UoD, represented by a consistent collection of declarative sentences stated in a formal language of logic. The objectivity of the UoDD is implied by its truthfulness

## Implications

The objective belief suggests the following four principles for the UoDD

(1) correspondence

(2) objectivity

(3) the excluded middle, and

(4) language neutrality

A closer look will show that all these principles are based on some unwarranted claims about the nature of social information

The principle of correspondence states that every sentence in the UoDD corresponds to users' observations about entities. The UoDD presents these and there is a one-to-one correspondence between the IS and the UoD entities. For example, Chen speaks of a UoDD as a “pure representation of reality” [9]

The correspondence principle assumes that there is a fixed, immutable entity-structure in an enterprise. However only in mathematics do such entities exist their boundaries are sharp and clear, and they can be formed in ways that are unconnected with practical problems of human activity. Therefore, this assumption is only reasonable, when one is interested in abstract mathematical reality (e.g. axiomatic set theory [14]), but not for a more concrete domain [39]. Also, the literature in information modeling illustrates the fuzzyness of the structure and shifting boundaries of entities [21]. One needs only to think of such a commonplace entity as “person”. In a legal system it will undergo gradual changes and its spatial and temporal bounds will shift, no fixed entity can be observed

The process of perception is also rife with problems especially, with soft-entities, such as “legal person”, “loan”, “customer”, “order” etc. Usually they define important classifications that are necessary to carry out activities such as ban-ing, insurance, etc. They usually form the majority of the entities populating UoD’s A distinguishing feature to soft-entities is that they do not correspond to a perception of any individual In this sense the metaphor of “perceiving” entities is inappropriate soft-entities cannot be directly observed. Indeed, they exist due to delicate and complex social mechanisms which support their identification, creation and deletion. In this sense soft-entities are always socially constructed [3] and result from negotiation and mutual belief

The principle of objectivity postulates that statements of observations are independent of an observer. So, the principle reduces all sentences in the UoDD to a form

“It is true that p”,

which does not show who knows “p” and in what way [17] Languages allowing only such expressions are called extensional languages, since sentence meanings are reduced to extensions truth-values. The logical world so constructed is called a Tractatus-world [44], from Wittgenstein’s famous logical treatment of Language [41]. In this world one distinguishes insignificant sentences from significant ones depending on whether they represent facts. So-called intentional sentences are excluded. They relate propositions about facts to subjects, they express propositional attitudes such as “A thinks that it is true that p”. The truth-values of such sentences are opaque, i.e., they cannot be composed from the truth-values of their components. Accordingly, they do not mean anything. For example, a sentence like

"The marketing director believes that the sales have dropped by $10\%$

is unmeaningful It may be true that the marketing director believes so but the sales may not have dropped

Unfortunately, the principle of objectivity reduces radically the set of meaningful sentences. For most of us such a sentence is meaningful, if issued by the chief executive in a meeting. This shows that meaningful managerial information has several other significant aspects, such as its context, producer (who said it) and modality as conveyed by modal verbs such as believing and knowing. The meaning criterion can only be associated with some subset of socially meaningful information

The principle of the excluded middle states that, "it is true that $p$ " and "it is not true that $p$ " cannot coexist in the UoDD For example Bubenko [7] says that the "information base contains a set of facts observed in or asserted true of, the UoD" The UoDD describes what is the case or what it isn't, there is no way that it can be both. The law of the excluded middle in formal logic is a way of deriving a logical contradiction. The UoDD must be logically consistent [17], because reality allows only one case at a time

However the law of the excluded middle may have some disastrous consequences when applied to organizational IS First, regulations conveyed by the IS are not as rigid as natural laws. There are always exceptions to a rule, which, when they occur, may cause the IS to behave in an undesirable way, e.g. it may not be possible to remove a manager from a department, because it leads to an inconsistent database. Second, the statement of the constraints and their enforcement via a shared database may lead to organizational inflexibility, e.g. one might not be allowed assign prices on a departmental basis

Moreover, many studies indicate that contradiction and ambiguity occur during information exchange in organizations. These may be due to advantages in misrepresenting information [10,12], having differing world-views [4,15] and in the heuristic value of confusion in organization learning [19]. When this is the case, striving for logical consistency in the UoDD is impossible because one cannot stop people from lying or changing their organizational metaphors. Moreover, this can give a false impression of consistency, when there is, in fact, none and when there is no way to guarantee it

The principle of language neutrality states that the structure of reality is independent of the structure of the language that represents it. An IS user stands “in the limit of the world” [41] by observing and recording facts in the UoD A language must serve as a technical means to represent facts. It should have no active role in shaping the conceptions of the world

This implies that information modeling does not affect the members' view of an organization. Information modeling attempts only to develop a language to record the observed facts. However, this is in conflict with some well known studies of language both ordinary [43] and scientific [39]. These studies provide quite rich evidence that language has an active role in shaping speakers' conceptions of the world. In the same way, the artificial existence of a solitary user who observes the UoD and records facts does not make sense

Studies show that language can only exist socially, i.e., through an organized human activity [42] Through language, people construct a social “reality” shared with their fellows that is significant for their activity [3] Thus, an information modeling is an vehicle to construct and make sense of organizational life [4] If this aspect is neglected, there can be overemphasis on how to represent the model rather than what it should represent It is no surprise, therefore, that the literature is abundant with examples of how to represent the UoD but actually very few studies of what the entities in the UoD are and why they must be included into the model

In conclusion the four principles of objective belief are not appropriate to understand the activity of information modeling in social settings. Their basic weakness is that they fail to appreciate the social character of information in an organizational texture [10,12]. When followed, they can lead to some harmful and even dangerous organizational consequences

## 23 The Descriptive Belief

The second belief of the RM view reads as follows [5,17]

## A UoDD represents only factual information

The IS definition states that all sentences in an IS codify facts or their invariances, laws $[7,17,35]$ . From a linguistic point of view this position limits the functions of language to just one to describe reality in a way that can be asserted or denied. This is called descriptive fallacy by Austin $[2]$ . Other functions of language to express personal attitudes wishes and evaluations, to establish and maintain social relationships and to regulate human behaviors are neglected

## Implications

If information modeling were to proceed with descriptive belief, it would lead to three shortcomings. First, it would neglect the study of linguistic functions of the IS people use IS's to make things happen. Second, it would not be able to make distinctions between referential and purposeful meaning. It would make the meaning of terms like "a morning star" and "an evening star" synonymous, though they are not. Third, it would neglect the study of interpersonal relationships created through language use

A closer study of the use of computer based information systems gives clear evidence that most information systems deal with various bargaining processes [10] order-processing involves screening and accepting of “requests”, production-planning issues “commands”, and accounts payable deals with control of “promises” and so forth All sentences in information systems are not descriptive. Instead, they involve linguistic performances [2,22] by which organizations and their members are committed to various activities and make them happen. Examples of them are “delivering” “paying” etc. The primary management purpose of introducing computer based information systems is to make activities quicker or more efficient, to improve the organization’s bargaining situation, or to obtain information of earlier bargaining processes, e.g., what is the organizational commitment etc [10]

As language has functions other than the descriptive one, the meaning of information cannot be defined only by reference an existence of an entity or a class may be defined, but this does not imply what people mean when they are using the language [42] The study of meaning cannot ignore what people intend when communicating with each other. The purpose can be inferred from the rules and conventions that govern the use of language. For example, it has been known since the 16th century that terms “the evening star” and “the morning star” have the same reference, namely, the planet Venus Yet, they do not mean the same. In most contexts, only one of the terms is meaningful

According to many scholars in the philosophy of language [2,34,43] its use necessarily establishes an interpersonal relation which can be distinguished from what the language describes. For example, the sentence

"Car number PCX999 is of type 4-door Mustang" does not only express the make of a specific car, it also says that its owner has made a statement in an institutional context. By so doing the registrant is involved in a social relationship with a registrar with specific institutionalized consequences. These concern e g the legal obligation to state correct details of registered cars So, if the car-owner misleads the car-registrar, a new set of interactions must be invoked to resolve the mis-use Thus, an IS establishes, coordinates and controls various social relationships in institutionalized settings by language [10] Information modeling must also deal and understand this issue

## 24 Consensus Belief

We define consensus belief by the statement A UoDD expresses an agreement, a theory of how the UoD behaves

The claim, that a CS describes classifications and the laws of the UoD, leads users to regard the CS as the formulation of the only valid perception of an enterprise, namely the one which defines a “long term, unrestricted model (or view) of the enterprise” [1]

This model has been called an enterprise description [35] and it models all aspects of an enterprise into a single consistent “theory of an enterprise”

## Implications

If a perceptual consensus of an enterprise is to be described by a single model, this implies that two problems have been resolved

(1) the content as a consensus, and

## (2) the reasons to defend it

Both these are problematic, because they closely relate to the organizational aspects of information systems which has often been excluded. It is, however, obvious that conflict in organizations is pervasive and that uniformity of perceptions is unlikely due to social and task differentiation, professional group formation, and organizational politics. Even one analyst can perceive the organization in several ways. Therefore one cannot generally find a consensus in organizations

In most cases, the content cannot be resolved, a vast and well-documented literature on organizational behavior e g [8], and [29], testifies to the contrary. For example, the consensus on goals is usually replaced by organizational politics. In addition, there are other fundamental problems in deriving the content for example, systematically deriving a CS from agreed goals introduces more problems than it solves, we do not know how to show that the schema is still valid if the goals change

Of course, a consensus can be forced by manipulative tactics or by fiat. However in many cases it is undesirable because it results in organizational inflexibility, power struggles and even worsening performance [6,30]. Uniformity of perception has also sometimes been reported to result in unfavourable consequences for organizations (known as “group think”) These include inflexibility of organizational structure and behavior [15], support of only one inquiring system and cognitive style [31], and gradual distortion of data used by the decision-makers [4] Therefore, an information modeler must be careful when assessing the organizational scope of the model and its organizational validity This is not just a technical problem, but involves in most cases a political mine-field who is going to control the content of communications and how they are going to take place

## 3 On The Formal Language Development View

## 31 The IS-definition

Many of the basic ideas of the FLD view are not new. Similar issues have been discussed in social theory [3], and language theory [2,34,42]. The application of these ideas to the IS field has, however, gained momentum only in recent years

In the FLD view an information system is a linguistic communication tool (see Figure 2). An information system consists of different groups of people communicating in a formal language [15]

![](/api/attachments/NT98H8HR/fulltext/images/04af3a830ae229b8ede8674e1146caf4954ec45640d4da4518313311df1e5b04.jpg)  
Fig 2 Information system in the FLD view

The language includes formal messages that are meant to be exchanged between members of an organization. Thus the definition poses the following question when developing an IS who is communicating with whom and on which topic. The communications through an IS create, set up, control, and maintain social interactions in an organizational context. The special nature of an IS as a communication tool derives from the formal nature of its language, and the prespecified ways of its use

The formal nature means that the syntax, semantics and parts of pragmatics [27] of the messages are closed. In other words, the structure, the content, and uses (intentions) of messages are clearly formulated and the IS should include messages with a permitted syntactic structure, a meaningful semantic content, and an acceptable and significant pragmatic use. Because the language is formal, it closes possible topics of communication via an IS. On the other hand, the formal nature makes it possible to define formal inferences using inference rules (programs) and axioms (data base).

The prespecified way that the IS may be used means that the IS follows a systematic, prespecified pattern. Usually this includes fixed differentiated user roles (clerk, manager etc.), and well structured use principles in terms of timing and interaction with the system, organizational procedures associated with the IS use, etc. All this amounts to a decrease in effort in repetitive and common communication tasks [3]

The communicated messages have effects on the work duties. They concern important topics that are at the core of organizational action such as accepting orders, sending bills, planning of a new production line etc. Most (but not all) communication is aimed at achieving a common understanding of the communicated issue among the organization's members, or those interacting with it (customers, suppliers, etc).

The definition of an IS gives us an idea on an existence of a purposefully developed, formal language as a major part of an IS. The IS communications take place by storing, retrieving, inferring and transmitting messages according to certain rules. The key idea in the FLD view is to see language as a rule-based system. The formal language is based on intersubject rules shared between communicators, these define which message exchanges are significant through an IS, and how and when they should take place. These rules are defined beforehand by formulating and agreeing on them when developing the IS

The IS definition in the FLD view is based on understanding language as a social phenomenon [26] In this sense, information systems are primarily “social systems” which have been “only technically implemented” [15] Three beliefs characterize such a perspective

(1) an information system is tied to action,

(2) an information system is a contextualized, institutionalized phenomenon and

(3) an information system is purposefully developed and developing or changing

## 32 Action Belief

This expresses that the formulation and use of formal messages in the IS manifests human, rule-governed behavior [15] Uses of IS constitute actions, speech acts, or communicative acts, which count as doing something that is significant for the IS users [25] The meaning of messages produced in the IS cannot be separated from the human action associated with producing these messages [34] The study of the meaning of sentence implies that we must probe whether it expresses human behavior of making statements, say the marketing director's beliefs or whether it has some more subtle meaning (e.g., irony) In every case, the FLD view suggests that we must study formal conditions that make such significant human behavior possible e.g., make sentence a meaningful utterance in a social context and understand what implications and effects such a behavior can have

It also follows that the FLD view is interested in all kinds of human behavior that can be instantiated. This set of behaviors does not only include meaning statements (descriptive fallacy), but also giving orders, promises, classifying things etc [22 24,34] In this perspective, information systems enact and enable a limited set of linguistic human behaviors to be mediated by information technology and accordingly an IS forms a specific class of linguistic discourse [25]. The FLD view suggests that information modeling should be seen as a study of message meaning (expressed in speech acts) and the formal properties of speech acts and their combinations (discourses) [13,25,40]

## 3 3 Institutional Belief

This emphasizes that an IS is a social institution. It creates classifications of types of acts and actors that are reciprocally recognized and maintained. Only agreed on forms of IS use are enforced

The institutionalization can only proceed in an interpretation and action field. This a field is formed by social practices such as producing and dispatching things, selling airline seats, taking courses etc. It is called “form of life”, by the “late” Wittgenstein [42], who shows that such a set of practices is a necessary background for any significant language use. Understanding message meaning cannot be separated from the social practices into which the message exchange is intervowen. Therefore the drive towards an all-embracing consensus on language meaning can be (and probably is) a useless effort

All this suggests that information modeling forms an activity by which a communication institution is created and maintained [28] Therefore, the success of information modeling depends on available mechanism that enforce the acceptance of the institution and the extent to which this institution is in harmony with the form of life in which it is to be embedded

## 35 Change Belief

This expresses the historical nature of message meaning Every linguistic system is a cultural, historical phenomenon that serves a specific form of life As organizations and their parts change [32] so changes the language Information systems development is one mechanism to create a language change It adjusts and constructs an understanding of a social world and defines rules for communication about that world Accordingly, the FLD view sees information modeling as a question of language change where the intersubject rules are predefined From this it follows that information modeling methods and techniques should support the IS users in actively changing their own professional languages Any attempts to achieve a “long term unrestricted model of the enterprise” are doomed to fail Instead, information modeling should emphasize adaptability flexibility and contextuality of developed conceptual schemata

## 36 Implications

The three beliefs provide a basis to develop an alternative information modeling approach. Here we only briefly outline some of its basic tenets. At this stage this approach is also less articulated than the RM approach. However, a more detailed presentation and work in progress in this area can be found in [13,15 16,25,28,36,37]

The basic goal of the FLD approaches is to achieve intersubject agreement on the formal language rules. An information model is seen as a means to understand communication in an IS and to reconstruct rules that underlie it. During information modeling the IS users formulate, develop, and agree on these rules

The study of message meaning involves at least three aspects: classifications intentions, and assumptions. First, the elicitation of the socially shared classifications, “entity-types” in the RM view, includes finding out what people mean by “customers” “accounts”, etc and what criteria they use to classify entities into these classes. In distinction to the RM view, these entity-types are dependent on the form of life and thus subject to negotiation. They can be redefined, and their definitions can vary over organizational functions and areas. There is accordingly no a priori normative principle to aim at a consistent definition of terms. Consistency is only preferred if it serves some acceptable social goals such as improved organizational coordination, less misunderstandings and so on

Second, the FLD view aims to uncover intentions of language use by the study of linguistic functions, and what commitments the linguistic performances establish. This involves an understanding of common terms and to what activities they commit the organization. In other words, the study of the message meaning in the FLD view includes also the description of the linguistic behavior associated with the use of the message. In brief, this amounts to describing for formal properties of speech acts, i.e. what are necessary and sufficient conditions to perform the acts in different contexts [25]

Third, the study of message meaning involves the study of necessary background assumptions and presuppositions that are necessary to assess the meaning of sentences in contexts. These include, among others, socially shared assumptions of what is possible, necessary, etc in the given world [25] In the RM view, these were understood as general laws, 1e constraints

Unfortunately, these three aspects together make information modeling quite complicated and demanding [25] Research is currently underway on how all these three tasks can be accomplished and how some tasks could be simplified, e.g., by the use of computer aided tools

According to the FLD view information modeling is an important vehicle for organizations to learn about their communication practices how actors make sense of their environments and communicate in them. The FLD view also underscores the study of mechanisms by which language use initiates, enforces, and controls organizational behavior. This enables also the more “political aspects” of information modeling to be clarified. Finally, information modeling can help to detect distortions and inconsistencies in communication. This covers, e.g. the identification of incompatible language meanings which are dysfunctional for an organization’s activities [28]

According to the FLD view, information modeling is mostly concerned with translating meanings in users' professional languages into a formal language. In this sense, it is a creative, interpretive task that is based on the understanding of ordinary language communication. This does not, however, preclude the application of formal methods, if they help to uncover constructs for correct language use and possible inconsistencies in them

## 4 Conclusions

Our study shows that it is important to examine beliefs that underlie information systems research and development. First, this helps us to understand differences in approach, to uncover weaknesses, and to build up cumulative traditions [20]. Second, beliefs about the nature of the IS, as an adjunct to direct research, also serve to legitimize information systems development as a kind of rationally contrived act [33]. The study of different views can therefore help us to detect various rationality bases for information systems development

It is clear, that the two views discussed appeal to two distinct world-views in the sense of Kuhnian paradigms [23] The FLD view concentrates on the nature of human communication and sense-making in IS's Information systems development is both a social and a cultural change that is carried out in relation to introducing information technology. The RM view concentrates on the completeness, predictability, and consistency of the IS design. Information systems development is mainly a matter of (software) technology change

These two views have similarity with Habermas' [18] theory of knowledge interests, namely with knowledge that helps to achieve human understanding, and with knowledge that helps to achieve technical control. This theory suggests that these views supplement each other, if their difference is acknowledged. In our case they do because the managerial use of the IS is driven by the need to understand the meaning of data for action, whereas the technical operation of the IS is driven by the need to control the data and maintain its consistency to allow correct program behavior. Data in the IS must be both socially significant and technically well controlled. Therefore, the choice is not the question of one or the other but question of a balance between them. However, more research is needed to assess the pros and cons of both approaches and how they could be combined in concrete systems development situations. This calls for a more careful evaluation of the impacts of both views on the outcomes of information systems intervention

## Acknowledgements

I acknowledge the valuable help provided by H Klein, E Lehtinen, and G Goldkuhl in improving the earlier drafts of this paper

## References

[1] ANSI/X3/SPARC, Study Group on data base management systems Interim Report 1975 FDT-Bulletin Vol 7 No 2

[2] J Austin How to do things with words Clarendon Press Oxford, 1962

[3] P Berger and T Luckmann The Social Construction of Reality Penquin University Books Middlesex 1967

[4] R J Jr Boland 'Control Causality and Information System Requirements' Accounting Organizations and Society Vol 4 No 4 1979 pp 259–272

[5] A Borgida Features of Languages for the Development of Information Systems at the Conceptual Level IEEE Software Vol 1 No 1 January 1985 pp 63–72

[6] H Brinckmann Autonomous Areas in Comprehensive Office Systems- a Perspective of Human Work in Organization paper presented at the IFIP WG 9.1 Conference Systems Design for Human Development and Productivity Berlin 12–15 5 1986

[7] J A Jr Bubenko “Information and Data Modeling - State of the Art and Research Directions” in H Kangassalo (ed) Proceeding of the Second Scandinavian Research Seminar on Information Modeling and Data Base Management University of Tampere Tampere Finland 1983 pp 9–28

[8] G Burrell and G Morgan Sociological Paradigms and Organizational Analysis Heinemann London 1979

[9] P P S Chen 'The Entity-Relationship Model a Basis for the Enterprise View of Data Proceedings of 1977 National Computer Conference, Dallas Texas Vol 46 1977 pp 77–84

[10] C U Ciborra 'Management Information Systems - A Contractual View, in Bemelmans Th M A (ed) Beyond Productivity Information Systems Development for Organizational Effectiveness North-Holland Amsterdam 1984 pp 135–146

[11] CJ Date An Introduction to Database Systems Addison-Wesley Englewood-Cliffs NJ 1982 (third edition)

[12] M S Feldham and J C March “Information in Organizations as Signal and Symbol” Administrative Science Quarterly Vol 26 No 2 June 1981 pp 171–186

[13] I Flores and J J Ludlow ‘Doing and Speaking in the Office’ in Fick G and Sprague R (eds) Decision Support Systems - Issues and Challenges Pergamon Press London, 1981 pp 95–118

[14] G Frege On Sense and Reference' in Translations from the Philosophical Writings of Gottlob Frege transl Geach P T Black M Basil Blackwell Oxford 1952

[15] G Goldkuhl and K Lyvtinen, 'A language Action View of Information Systems' in Ginzberg M and Ross C (eds) Proceedings of the 3rd International Conference on Information Systems Ann Arbor Michigan Dec 13–15 1982 pp 13–30

[16] G Goldkuhl and K Lyytinen 'Information Systems Specification as Rule Reconstruction', in Bemelmans Th M A (ed) Beyond Productivity - Information Systems Development for Organizational Effectiveness North-Holland Amsterdam, 1984, pp 79–94

[17] J J van Griethuysen (ed) Concepts and Terminology for the Conceptual Schema and the Information Base International Organization for Standardization March 1982

[18] J Habermas Knowledge and Human Interest transl Shapiro J Heinemann London 1972

[19] B Hedberg and S Jonsson 'Designing Semi-Confusing Information Systems for Organizations in Changing Environments Accounting Organizations and Society Vol 3 No 1 1978 pp 47–64

[20] P G W Keen 'MIS Research Reference Disciplines and Cumulative Traditions, in McLean E R (ed) Proceedings of the 1st International Conference on Information Systems Philadelphia, Dec 8–10 1980 pp 9–18

[21] W R Kent Data and Reality North-Holland Amsterdam 1978

[22] S O Kimbrough R M Lee and D Ness "Performative Informative and Emotive Systems The First Piece of the

PIE ' in Maggi L King JL and Kraemer KL (eds) Proceedings of the 5th International Conference of Information Systems, Nov 28–30 1984 pp 141–148

[23] T Kuhn The Structure of Scientific Revolutions 2d ed enl Chicago University of Chicago Press 1970

[24] R Lee ‘Automating the Red Tape - the Informative vs the Performative Role of Bureaucratic Documents’ Office - Technology and People No 1 Vol 3 1984

[25] E Lehtinen and K Lyvtinen, An Action Based Model of Information System Information Systems vol 13 No 4 1986 pp 299–318

[26] D Lewis Convention Cambridge Mass Harvard University Press 1969

[27] K Lyytinen, Implications of Language Theories for Information Systems MIS Quarterly vol 9 No 1 1985 pp 61–76

[28] K Lyytinen Information Systems Development as Social Action - Framework and Implications Jyväskylä Studies in Computer Science Economics and Statistics 8 University of Jyväskylä Jyväskylä Finland PhD Diss 1986

[29] J March and J Olsen Ambiguity and Choice in Organizations Universitetsforlaget Oslo 1976

[30] L Markus ‘Power Politics and MIS Implementation’ Communications of the ACM Vol 26 No 6 1983 pp 430–444

[31] I I Mitroff and R O Mason, Can we Design Systems for Managing Messes' or Why So Many Management Information Systems are Uninformative? Accounting Organizations and Society Vol 8 No 2 3 1983 pp 195–203

[32] A M Pettigrew ‘Contextualist Research A Natural Way to Link Theory and Practice’ invited paper presented to the Conference on Conducting Research with Theory and Practice in Mind Center for Effective Organizations University of Southern California Los Angeles California November 3–4 1983

[33] D Robey and L Markus 'Rituals in System Design MIS Quarterly Vol 10 No 1 March 1984 pp 5–15

[34] J R Searle Speech Acts - An Essay in the Philosophy of Language Cambridge University Press London 1969

[35] M E Senko Conceptual Schemas Abstract Data Structures Enterprise Descriptions in Morlet A and Ribbens G (eds) Proceedings of International Computing Conference 1977 North-Holland Amsterdam, 1977, pp 28–39

[36] R Stamper ‘Towards a Semantic Normal Form’ in Bracchi G and Lockeman P (eds) Database Architecture North Holland Amsterdam 1980

[37] G Stamper, “Management Epistemology Garbage In Garbage Out” in L B Methie and R H Sprague (eds) Knowledge Representation for Decision Support Systems North Holland Amsterdam 1985 pp 55–80

[38] Tarski A “The Concept of Truth in Formalized Languages in Logic Semantics Metamathematics Alfred Tarski Clarendon Press Oxford 1956

[39] S Toumin Human Understanding - the Collective Use and Evolution of Concepts, Princeton University Press, Princeton N J 1972

[40] T Winograd What Does It Mean to Understand Language Cognitive Science Vol 4 No 4 1980 pp 209–241

[41] L Wittgenstein “Tractatus-Logico Philosophicus” in Ostwalds Annalen der Naturphilosophie German-English Edition Russell B (ed) London 1922

[42] L Wittgenstein Philosophical Investigations Basil Blackwell, Oxford 1958

[43] B L Whorf Language Thought and Reality, The MIT Press Cambridge Mass 1956

[44] H von Wright, Explanation and Understanding Routledge and Kegan Paul London 1971
