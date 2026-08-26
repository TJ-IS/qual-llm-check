---
otero_id: 24040
otero_key: "3VZDM6JM"
title: "Action-oriented conceptual modelling"
authors: "Pär J Ågerfalk; Owen Eriksson"
year: "2004"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000486"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Action-oriented conceptual modelling

Pa¨r J. A<sup>˚</sup> gerfalk<sup>1,2</sup> and Owen Eriksson<sup>3</sup>

<sup>1</sup>Methodology Exploration Laboratory, Department of Informatics (ESI), O<sup>¨</sup> rebro University, O<sup>¨</sup> rebro, Sweden; <sup>2</sup>Department of Computer Science and Information Systems, University of Limerick, Limerick, Ireland; <sup>3</sup>Department of Computer Science and Informatics (IDI), Dalarna University, Borla¨nge, Sweden

## Correspondence:

Pa¨r J. A<sup>˚</sup> gerfalk, Department of Computer Science and Information Systems, University of Limerick, Limerick, Ireland. Tel: +353 61 213573 Fax: +353 61 202734 E-mail: par.agerfalk@ul.ie

An earlier version of this paper was pub-<sup>w</sup>lished as: A<sup>˚</sup> GERFALK PJ and ERIKSSON O (2002) Pragmatization of conceptual modelling. In Information Systems and the Future of the Digital Economy, Proceedings of the Xth European Conference on Information Systems (ECIS 2002), 6–8 June 2002, Gdansk, Poland, Vol 1, (Wrycza S, Ed.), pp 416–428.

## Abstract

The aim of this paper is to show how speech act theory can be used in systems development as a theoretical foundation for conceptual modelling. With the traditional notion of the conceptual model as an image of reality, the predominant modelling problem is to analyse how the external reality should be mapped into, and represented in, the system in a ‘true’ way. In contrast to this, we maintain that the main modelling problem should be to analyse the communication acts performed by use of the system within its business context. This implies an integration of traditional conceptual modelling with action-oriented business modelling based on speech act theory. With such an approach, it is possible to reconcile traditional conceptual modelling and the pragmatic aspects of language and computer use. It is argued that such reconciliation is essential to arrive at systems that provide relevant information to users and in which users can trace responsibilities for information, actions and commitments made.

European Journal of Information Systems (2004) 13, 80–92. doi:10.1057/ palgrave.ejis.3000486

## Introduction

Conceptual modelling, as a systems development activity, is basically concerned with two different views: a static and a dynamic view. The static view emphasizes static properties in terms of, for example, entities and relationships (Chen, 1976). The dynamic view captures how entities of the static model change state over time. Such state changes are often thought of as triggered by events occurring in the system’s environment (e.g. Booch et al., 1999).

Although conceptual modelling is an important activity in the systems development process, there is confusion as to how it should actually be performed. There is, for example, no consensus on how to represent associations in the static model (such as weak entities, relationships and attributes) (Wand et al., 1999). There are also problems related to the modelling of dynamic and temporal aspects (Snoeck & Dedene, 1998; Gregersen & Jensen, 1999). A further problem concerns pragmatic aspects, which are largely neglected in traditional conceptual modelling. This implies that pragmatic concepts, such as actors, responsibilities, actions and commitments, are not paid sufficient attention during conceptual modelling (Nurminen, 1988; Goldkuhl, 1995; A<sup>˚</sup> gerfalk, 2002).

These circumstances have consequences for the information system (IS) under development. They may, for example, imply that the system fails to provide relevant information to users, that users do not understand how to use it (e.g. Gulliksen et al., 1997), and that users cannot trace who is responsible for information, actions and commitments made (Erickson & Kellogg, 2000; Erikse´n, 2002). We believe, in line with, for example, Holm (1996), that one important cause of these problems is that traditional conceptual modelling is based on a descriptive perspective on information systems, which embodies an objectivistic view of reality.

In this paper, we discuss how conceptual modelling can be informed by an action-oriented perspective of information systems to provide a practical, yet theoretically founded, basis for capturing important properties of the business modelled. Properties such as actors, actions, associations, responsibilities, time constraints and statechanges. The pragmatic aspect is here seen as related to how the system is used to perform actions not only on the basis of information from the system but also through the system (Goldkuhl & A<sup>˚</sup> gerfalk, 2002).

We propose an integration of traditional conceptual modelling with action-oriented business modelling, an integration that may eliminate the tendency of contemporary conceptual modelling approaches to yield overly abstract models. One, perhaps the foremost, reason why conceptual models tend to be too abstract, we believe, is that the use of conceptual models and information systems is not analysed pragmatically from within the business context. Instead, conceptual models and information systems are considered as images or mirrors that are external to the business (Lyytinen, 1987).

The proposed approach, which we term action-oriented conceptual modelling, draws on theoretical developments within the language/action perspective (e.g. Goldkuhl & Lyytinen, 1982; Winograd & Flores, 1987; Aurama¨ki et al., 1988; Flores, 1998) and experiences from a case study, more fully described by Eriksson (1998).

The paper is structured as follows. Firstly, we discuss the prevailing descriptive perspective on information systems and point at some of its major limitations. Secondly, we introduce an alternative speech act view of information systems and discuss how speech acts has been used in systems modelling to date. This discussion includes the identification of some important limitations in current speech-act-based approaches when it comes to conceptual modelling as a basis for database design. With this as a foundation, the remainder of the paper is devoted to the suggested action-oriented conceptual modelling approach.

## Beyond the descriptive perspective on information systems

When creating a conceptual model, from a descriptive perspective on information systems, the business at hand constitutes the universe of discourse, that is, the part of reality that the model claims to reflect. The model is then transformed into a computational representation and stored in the database of the system being developed. (This is admittedly a somewhat simplified description, but it is sufficient for the purpose of this paper.) This model of the business is then used as a source of knowledge about the business, that is, the business actors can use the computerized model instead of looking directly at the world (see Figure 1). This objectivistic view of information systems and of reality reduces the user to an observer who is observing the real world from the outside, through the conceptual model as implemented in the system (Lyytinen, 1987). The pragmatic aspect is here seen as mainly related to how the user acts on the basis of information acquired from the system (Langefors, 1995); that is, action is conceived as being external to the system.

![](/api/attachments/3VZDM6JM/fulltext/images/ba77896106605ecabe8f6e8e2565657cd8d24b344d52a956ecfffd5b40949121.jpg)  
Figure 1 Traditional view of an IS as an image of reality.

The descriptive view of information and information systems as images of reality has been challenged and criticized from a language/action perspective on information systems (e.g. Goldkuhl & Lyytinen, 1982; Winograd & Flores, 1987). From a language/action perspective, an IS is regarded not as an image of reality that stores true information about the world but rather as a vehicle for social action and communication within a business context (Dietz, 2001; Goldkuhl & A<sup>˚</sup> gerfalk, 2002).

However, conceptual modelling is still important within such an action-oriented view of information systems. One reason is that the systems must contain and provide a business vocabulary that includes concepts used for communication (Goldkuhl & Lyytinen, 1982; Lyytinen, 1986). Furthermore, the systems must store information about the current state of the business and maintain a record of business actions performed. In fact, as we shall see in the next section, applying an action-oriented view of information systems implies a reconciliation of ‘traditional’ conceptual modelling and the pragmatic aspects of language and computer use.

With the notion of the conceptual model (and the IS) as an image of reality, the predominant modelling problem is to analyse how the external reality should be mapped into, and represented in, the system in a ‘true’ way. In contrast to this, we maintain that the main modelling problem should be to analyse the communication acts performed by use of the system within the business, and how these acts may affect the business context. With such a pragmatic view, conceptual modelling is still important, but we argue that the importance of the business context must be emphasized more. In the next section, speech act theory will be used to give a theoretical background for such a pragmatic approach to conceptual modelling.

## Information systems and speech acts

The assumption that information systems should serve as images of reality, used to inform users about the world, suggests a rather restrictive view on the role of information systems within organizations. We maintain that information systems are primarily used for communication and that this activity cannot be viewed only as making descriptions of reality. People do not use language only to talk about events in the external world as observers; they act and communicate within the world, as social actors. Communicating implies doing things, and messages carry more meaning than just facts about reality: they also carry the actors’ intentions and beliefs and are used to influence people and to change the world. Communication can therefore be viewed as action. Information systems are, as are language systems in general, used to perform communication actions (Goldkuhl & Lyytinen, 1982), and ‘Language does not simply symbolize a situation or object which is already there in advance F it makes possible the existence or appearance of that situation or object, for it is part of the mechanism whereby that situation or object is created.’ (Mead, 1934). This is also a main idea in the theory of speech acts (Austin, 1962; Searle, 1969). According to Austin (1962), ‘to speak is to act’. When saying something, we are doing something F for example, promising or commanding. Austin also coined the phrase ‘descriptive fallacy’ to refer to the misconception that language is only used for descriptions of reality; which is the case with a traditional conceptual view of information and information systems.

According to Searle (1969), a speech act consists of four different sub-acts:

(a) uttering words, that is, performing utterance acts;

(b) referring and predicating, that is, performing propositional acts;

(c) stating, questioning, commanding, promising, and so on, that is, performing illocutionary acts; and

(d) causing an effect in hearers, that is, performing perlocutionary acts.

Searle is explicit about the first three elements (a), (b) and (c) not being separate things that a speaker does simultaneously. Likewise, (a) and (b) are not means to achieve (c). Rather, ‘utterance acts stand to propositional acts and illocutionary acts in the way in which, e.g., making an ‘X’ on a ballot paper stands to voting’ (Searle, 1969). This is different from the perlocutionary act (d), which is not really an act at all (Allwood, 1987, 2000); rather, it is the effect that the speech act has on the hearer. It is also important to emphasize that there are a number of effects that can be the result of performing a speech act, and that these effects can also be oriented towards the speaker. For example, the effect of a promise is the creation of a commitment on the part of the speaker, to perform a subsequent act.

All semiotic acts must be understood within the social context in which they are performed (Clark, 1996). Actors must understand the context to participate successfully in communication. Aurama¨ki et al. (1988) define the context of a speech act to be a combination of speaker, hearer, time, place and possible world. The first two concepts refer to the actors who are performing and interpreting the action. Time and place represent the temporal and spatial aspects of the action. Possible world refers to the residual features of the context that make a particular action possible and meaningful, and hence potentially successful. Typically, these include shared norms, values and beliefs and the existence of certain social and material (brute) facts. Note that by referring to a possible world rather than the actual world, it becomes possible to talk about the future and what ought to be (Aurama¨ki et al., 1988). When doing business, the social context of the communication is a business context. From this discussion, we can conclude that the business context consists of actors, situated in time and space, performing communication and material actions, and these actions must be related to an inter-subjective understanding of the business context.

This theoretical discussion can be applied to the use of an IS in a business context with the help of the business offer described in Figure 2. The business offer is communicated by the use of a sales support system within a car sale/ purchase business context (Eriksson, 1998). The business offer above can be understood as a message, which consists of a propositional content and an illocutionary component (communication function). In the message, the propositional content identifies and describes the attributes of the purchase object, which is a car. The illocutionary component shows how the propositional content should be used, that is, its pragmatic meaning; in this case it should be understood and used as a business offer.

If we relate this example to Searle’s description of different sub-acts and effects, it can be described as follows:

(a) The utterance act is the production and communication of the physical written message, which can be presented on the computer screen or printed on paper.

(b) The propositional act is performed by use of the propositional content, which refers to an object, in this case a purchase object (a car) and its attributes.

(c) The illocutionary act is performed through the illocutionary verb offer.

(d) The business offer affects the business context; for example, by creating an obligation on the part of the car dealer to sell the car under the conditions described in the offer. The offer may also create the effect of the subsequent purchase of the car by the customer, which is likely the intention of the car dealer.

![](/api/attachments/3VZDM6JM/fulltext/images/8a5edcd22c2f38b359215695fbe72bd248c9203c073a3c03675fbb1ba160359b.jpg)  
Figure 2 A Business offer.

![](/api/attachments/3VZDM6JM/fulltext/images/9ed0185a9474b835df812439e6ec3dcb4f1cda3945c98643409cff04a4df270c.jpg)  
Figure 3 The CFA schema (Winograd & Flores, 1987).

In this context, we prefer to use the term communication act rather than speech act, because the acts that we are talking about are performed through different types of media, not through speech alone. The business context of the communication act consists of: time (18-12-97, 1030 hours), place (car dealer’s office), speaker (car dealer together with the system), hearer (customer), and possible world (the purchase object, that is, the car and the price of the car, as described by the propositional content; and business rules, social expectations and beliefs that govern the actors’ behaviour).

When the communication act is performed, it changes the state of the business context to the Car Offered state. The transition implies that (a) information, which consists of the propositional content, has been created, (b) the car dealer has expressed the intention and will to sell the car and (c) a commitment has been created on the part of the car dealer to sell the car under the conditions that are described in the offer.

If we agree that communication is action that involves causes and effects that change the state of the business context, and that these actions can be performed by the use of information systems, then we can use Searle’s theoretical discussion to understand the integration of the conceptual aspect of information systems with its pragmatic aspects. However, let us first give some examples of how speech act theory has been used as an alternative to the strict representational view of information systems in the information systems development community.

## Conversation for action

Traditional descriptive conceptual modelling focuses on the propositional content of information. The idea is to find generic information structures that are stable over time. However, detaching the propositional content from its pragmatic meaning and intended use is a prominent example of Austin’s descriptive fallacy (Winograd & Flores, 1987; Holm, 1996).

To put more focus on the illocutionary component that is neglected by conceptual modelling, Winograd & Flores (1987) propose a modelling approach based on speech act theory and the coordinating power of language. Their ‘conversation-for-action’ (CFA) schema (see Figure 3), which is based on transitions between states, has had a substantial impact on our understanding of computersupported collaborative work and has been of great importance for workflow management.

Winograd & Flores (1987) explain that the CFA schema is derived from the observations that computers can be used to support human communication and that computers should be programmed on the basis of repetition and reoccurrence. Their conclusion is that to design information systems that support human communication, developers must identify repetitive and reoccurring structures. They further claim that the CFA schema captures these structures accurately at a generic level.

According to the CFA schema, a business conversation is initiated by a request from a customer (the initial speaker), which specifies some conditions of satisfaction. The supplier (the initial hearer) then has the choice of accepting the conditions (promising to satisfy the request), rejecting it or making a counteroffer. If and when the parties have agreed, the supplier eventually asserts that the conditions of satisfaction have been met. The customer can then either declare that, in his or her opinion, the conditions have not been met, or express satisfaction, thus ending the conversation happily. During the conversation, both the supplier and the customer can withdraw at any point and thus cancel the conversation sequence unhappily.

Building on the generic speech act pattern of the CFA schema, the Action Workflow approach (Denning & Medina-Mora, 1995) describes business interaction as consisting of four phases: (1) request, (2) negotiation, (3) performance and (4) satisfaction. As before, the roles of customer and performer are pre-defined. These phases and roles are described by the Action Workflow loop (see Figure 4).

Both the CFA schema and the Action Workflow loop can thus be regarded as generic schema for the structure of business activity used to direct analysts’ attention to the action-oriented character of communication performed in a business context.

The advantage of these state-transition modelling techniques is that they take into consideration the illocutionary component and the way that speech acts affect the business context, when they model the business to design information systems. However, a problem with these approaches, and similar ones such as DEMO (Dietz, 2001) and COMMODIOUS (Holm & Ljungberg, 1996), is that they not only shift from a narrow focus on the propositional content of information, but that they actually tend to disregard the propositional content. As a consequence, they do not see the important coupling between the propositional content and the illocutionary component. The speech act based modelling techniques described above become as narrow as the methods used for traditional conceptual modelling but with another focus.

![](/api/attachments/3VZDM6JM/fulltext/images/da242fa6f4d3b6ea9227747b80a6af5b9f462f5c264ad61fb37fedfd57d553f0.jpg)  
Figure 4 The Action Workflow loop (Denning & Medina-Mora, 1995).

In the next section, we will discuss an alternative to contemporary speech act based approaches, an alternative that considers both propositional contents and illocutionary components and how speech acts affect the business context.

## Action-oriented conceptual modelling

Taking communication acts performed in a business context as the starting point for systems development, as suggested above, implies that business design and IS design become integrated into a single activity that encompasses both of them. This is so because information systems are not used only for storing and providing information about an external reality (i.e. the business at hand), which is the view of information systems in traditional conceptual modelling. In our view, it is important to understand the system as a vehicle used for performing communicative business actions embedded in a business context, which the system also affects.

From the discussion in the previous section, we have seen that communication can be seen as action and that the performance of communication acts is a presupposition for subsequent communication acts as well as for other ‘non-linguistic’ acts (i.e. communication acts may trigger and co-ordinate subsequent acts). This means that business modelling and systems development become an integrated activity of analysing the whole context of action. With the previous discussion in mind (see the previous section), we would like to draw attention to three important aspects of communication acts and conceptual modelling. Firstly, the propositional content of a communication act can be described by traditional static conceptual modelling (such as E/R modelling or object modelling). Secondly, the illocutionary component of the communication act should be analysed together with the propositional content; this is important for both static and dynamic modelling. Finally, actions change the state of the business context and thus ought to be the basis of dynamic conceptual modelling. These observations can be related to the distinction that is made in linguistics between the semantics and pragmatics of language. Semantics is focused on the meaning of propositional content while pragmatics is focused both on the pragmatic meaning of language and the effects that the communication have on speakers and hearers. Based on this discussion, we claim that:

(a) traditional conceptual modelling has focused too much on the semantics of language and too little on the pragmatic aspects; and that

(b) speech act based modelling techniques have focused too much on the pragmatics of language and too little on the semantic aspects.

However, by using an action-modelling approach, we can take both the semantic and pragmatic aspects into consideration. This approach makes it possible to reconcile traditional conceptual modelling and the pragmatic aspects of language and computer use. In the remainder of this section, we will give an example of how this can be done. The example is derived from a case study (Eriksson, 1998) of a sales support system used in a car sale/purchase business context. It is important to note that the example is not intended to provide empirical evidence; rather, it should be understood as an illustration of our discussion based on a realworld example.

## Dynamic modelling

The main idea with an action-oriented perspective is to analyse the way that information systems are used to perform actions within a business context. Using Action Diagrams (A<sup>˚</sup> gerfalk & Goldkuhl, 2001) is one way of doing this. The Action Diagram in Figure 5 shows five important business actions (offer, purchase, order confirmation, delivery and payment) that are performed during the car sale/purchase business process. Action Diagrams show actions and performers of actions together with information and material flows that are results of, and preconditions for, actions.

In the Action Diagram of Figure 5, we have also utilized an additional feature, tagged boxes, showing how the actions change the state of the business process. This way, state transitions and actor–communication links can be modelled together. Let us now examine further the meaning of the actions and the state transitions described in Figure 5.

Action 1 – Offer: The car dealer, together with the sales support system, performs the business offer action, which is a communication act. The transition to the Car Offered state means that the car dealer has expressed the intention to sell the car. It also implies that a commitment has been created on the part of the car dealer, who is on commission from the car company, to sell the car under the conditions described by the propositional content of the business offer; for example, not to sell the car at a price higher than that stated in the business offer.

![](/api/attachments/3VZDM6JM/fulltext/images/f6b389f3c04c643bbee901ee44c3343b8570fc2522e80bbe2169d5a84ec09ed2.jpg)  
Figure 5 Action Diagram describing the car sale/purchase process.

Action 2 – Purchase: The customer makes use of the business offer to decide whether to buy the car or not. If the customer decides to perform the purchase action, using the sales support system, then there is a transition to the Car Ordered state. The Car Ordered state means that the customer has expressed the wish that the car dealer should sell the car to him or her. It also implies that a commitment has been created on the part of the customer to pay the price and to buy the car under the conditions that are described by the propositional content of the purchase order.

Action 3 – Confirmation: The order confirmation action, which also is a communication act, is performed by the car dealer, together with the customer, with the help of the sales support system, and the order confirmation is manifested in a purchase contract. The Order Confirmed state means that the car dealer has expressed willingness to accept the purchase order from the customer. It also means that the customer has confirmed the intention of buying the car. New commitments are also created. One commitment implies that the car dealer will deliver the car under the conditions described in the purchase contract. Another commitment is created on the part of the customer, implying that he or she will pay for the car under the conditions specified in the business contract.

Action 4 – Delivery: The supplier performs the delivery action, which is a material act. The Car Delivered state implies that the car dealer (or rather the car company) has fulfilled the commitment to deliver the car under the conditions that were specified in the business contract.

Action 5 – Payment: The customer performs the payment action, which can be either a material or a communication act depending on how the payment is carried out. The Payment Issued state implies that the customer has fulfilled the commitment to pay for the car under the conditions that were specified in the business contract.

It is important to do action modelling because it shows that actions are performed with the help of information systems. These actions create information and change the state of the business process by creating commitments that must be considered and fulfilled as it proceeds.

In traditional conceptual modelling, the system is not viewed as a vehicle for performing actions embedded in a business context. With a descriptive perspective, all actions are performed outside the system, which is only used for description of an external world constituted by actions, objects and events. Certainly, information systems are used for describing actions and events that are external to the system. For example, the sales support system could be used to describe the material act of delivering the car. A clerk at the delivery office who registered a delivery report in the system would typically do this. Although this message is used to describe an external action (event) in relation to the system, it is important to emphasize that the very registration of the delivery of the car (and hence of the issuing of the delivery report) should be seen as a communication act. The Report action, which is performed by use of the system, states that the delivery action has taken place. It is important to emphasize that the clerk at the delivery office who registers the information is not only making a description of the delivery of the car (which is the part of the communication act that is called the propositional act), but is also stating that this is a fact (which is the part of the communication act that is called the illocutionary act), which commits the clerk to the truth of the propositional content. This Report action will of course not change the physical delivery of the car; nevertheless, it affects the business context because it implies that the car company claims that it has fulfilled its commitment. The state of the business is changed to Delivery Confirmed, which implies (a) the creation of information about the delivery of the car, (b) the making of a commitment on the part of the clerk regarding the truth of the report and (c) a declaration that the car company has fulfilled its commitments, which implies that it is free to invoice the customer, that is, to request that the customer should fulfil the commitment to pay for the car.

The Action Diagram in Figure 5 can be compared with the Statechart notation (Harel, 1987) often used in object-oriented modelling. A Statechart describing the car sale/purchase process, in terms of a Sales object, may look like the one in Figure 6.

The statechart in Figure 6 shows that a Sales object is created when the Offer event occurs. The Sales object’s state changes during the sales process, and eventually the sale/purchase process ends (or rather reaches a final state) when the Payment event occurs.

To describe the dynamics of the business process by use of Statecharts (or the semantically equivalent UML Activity Diagrams) can be helpful, but we suggest that Statecharts should be seen as complements to Action Diagrams, not as alternatives. The reason for this is that it is important to first understand the business and the use of an IS pragmatically from within the business context. To analyse the business in terms of state transitions of a Sales object implies that the business is viewed from the outside and that actions are viewed merely as events occurring in the external world, in line with the traditional view of information systems as images of reality. This is different compared to the Action Diagram which emphasizes that these events should be analysed as actions that change the business context, and not only the status of a Sales object. The Action Diagram also shows that these actions can be performed both within the system and externally to the system. In many object-oriented approaches (e.g., Booch, 1994; Graham, 1998; Mathiassen et al., 2000), as well as in approaches based on Soft Systems Methodology (Checkland, 1981) such as CLIC (Champion & Stowell, 2002), a clear distinction is made between the business (problem) domain (the system to be served) on the one hand, and the IS (solution) domain (the serving system) on the other. Object-oriented approaches also tend to separate events that are external to the system (business or problem domain events) from those that are internal to the IS (system events), during business analyses. From an action-oriented perspective, this type of distinction is misleading because the IS is here considered as an integrated part of the business process and what becomes important is to analyse essential business actions, no matter if these actions are performed within or outside of the system. A strong separation between system and business events is difficult to maintain when business actions are performed through or by means of the IS. For example, the offer in the example above is performed through the system. Therefore it is misleading to treat this action as an external event that should be mapped into a representation in the system. To paraphrase the quotation from Mead (1934) above: actions through the IS, as well as the IS per se are part of the mechanism whereby that sale/purchase process is created.

![](/api/attachments/3VZDM6JM/fulltext/images/b12833262aff232f2fa034a6d96bc23dfb1c78f02064e2454ba48d590efdcab1.jpg)  
Figure 6 UML Statechart describing the possible states of a Sales object.

The Action Diagram in Figure 5 and the description of the business process are, of course, simplifications of the activities performed in the actual business process. For example, we have not described the negotiation that takes place in the Proposal phase of the car deal. Normally, there is a negotiation between the car dealer and the customer when the car dealer has made the initial business offer. The purpose of the Action Diagram has been to indicate a number of generic actions in the business process that can be used to illustrate the points that we are trying to make, that is, to illustrate that:

 the business context and the way that the system is used within this context is the focus of our analyses, rather than a universe of discourse that is external to the system; that

 the business context is constituted of both material acts and communication acts, and both action types must be analysed when we model the business, to analyse how the system is used in, and affects, the business context; that

 the actions performed (both material acts and communication acts) change the state of the business context; and that

 the communication actions performed are carried out together with the IS.

## Static modelling

The static view of the business emphasizes static properties of entities and their static dependencies. Static modelling has been the focus of traditional conceptual modelling techniques but so far has not been sufficiently included in speech act based modelling techniques. In our opinion, it is important from an action-oriented perspective to focus on static aspects also. The main reason for this is that an IS must store information about important entities, their properties and relations between them, which are all elements of the business context.

From an action-oriented perspective, understanding the dynamics of the business context precedes static analyses. The reason for this is that information about essential actions, and their results must be structured and stored in the system. We claim that a thorough understanding of the business context and the business actions performed is essential for the identification of important objects, and for how information about these objects should be structured. When performing static modelling, from an action-oriented perspective, both tangible things (e.g. cars and actors) and less tangible things (e.g. actions and messages) can be regarded as objects. The reason that messages are considered as objects is that messages are the results of communication acts, and presuppositions and triggers for subsequent acts. This implies a need to store information about, and to keep track of, important communication acts and messages produced.

When making static analyses of actions, it is of interest to describe both the actions and static dependencies between actor(s) and actions. For example, if we analyse the business offer, which is a communication act, and the static dependencies between the act and the actors involved, then we can end up with a UML Class Diagram (see, e.g. Booch et al., 1999) as shown in Figure 7.

From the Class Diagram in Figure 7, we can see that the car dealer, the business offer and the customer are regarded as objects/entities; we have also described important static dependencies between such objects. A Car Dealer can be related to many Business Offers or none, and one Business Offer must be related to one Car Dealer. A Business Offer is also related to one Customer or none, and a Customer is related to many Business Offers or none. These static dependencies are conditions, or rules, that must be derived from the business action context.

![](/api/attachments/3VZDM6JM/fulltext/images/08022fc8d085c8cd7535d966d1d1bd7babd1d33f485e7374f68aa69076c7d3aa.jpg)  
Figure 7 Relations between a communication act (a business offer) and the actors involved in that act (a car dealer and a customer).

When we make a static analysis of a message, both the type of message (the illocutionary component) and the propositional content are of interest. In the diagram above, it is important to use the illocutionary component (signified by the verb offer) to describe the type of communication act performed. It is also important to analyse the propositional content because it is used for referring to important objects. It is important to notice that the propositional content of the business offer refers to something that is called a purchase object, which refers to a car that the car dealer wants to sell. In this action context, not only can the car company sell cars that physically exist at the time when the car is offered but also the car company can offer cars that will be built after the customer has purchased the car (i.e. on customer order). The pragmatic meaning of an offer is not that it is true that the car referred to exists, which would be the case if the illocutionary component were used for stating a fact, for example, in the case of a report. The pragmatic meaning of the offer should be understood as an undertaking of an obligation to sell the purchase object referred to, whether it exists or not at the time the offer is issued. This condition has consequences for the conceptual model.

Firstly, we cannot always use the licence number or the vehicle’s serial number as the key to refer to the car object, because these are identifiers used for cars that physically exist. Secondly, the attribute types and their values in the business offer may not refer to an existing car but can refer to a car that is to be built. Thirdly, even if an existing car is offered, it can be the case that the car offered has different attributes from the existing car. This would, for example, be the case if the car dealer added attributes to the car in the offer, such as extra tyres and a stereo that were to be installed before the car was delivered to the customer.

Altogether, this implies that the existing car object and the purchase object offered are not really the same object; this is also obvious because we must allow for existing cars that have not yet been offered. Ultimately, this exemplifies the need for analysing the illocutionary component and propositional content together, and the need for the concept of possible world as discussed above. Figure 8 depicts this discussion.

From the Action Diagram in Figure 5 we can also see that different actions are related to each other. The business context is a network of actions where both material and communication are related to each other. For example, the offer is a presupposition for the purchase action, and the result of the purchase action is the purchase order. This implies that we must also describe interdependencies between different actions (see, for example, the Class Diagram in Figure 9).

![](/api/attachments/3VZDM6JM/fulltext/images/ec431fa8392819936653f1f35c457d0a251a9bb4fd4fcce92c11484809126dd2.jpg)  
Figure 8 Relations between Business Offer, Purchase Object and Existing Car.

From the Class Diagram in Figure 9, we can see that a business offer can be related to many purchase orders or none, and that one purchase order must be related to one and only one business offer.

In line with this discussion, we conclude that the ‘complete’ resulting static conceptual model would consist of the classes Business Offer, Purchase Order, Purchase Contract (which would be related to the class Payment) and Car Delivery (see Figure 10).

From this discussion, we can conclude that the class Business Offer is an object type in its own right, (as is the Purchase Order, the Purchase Contract and the Payment). This is important to emphasize, as it may be tempting to view the Business Offer merely as a weak entity (as an association) between the customer and purchase object or as a state attribute of a Sales class (see Tables 1 and 2). This can cause problems during database and system design and usage, such as missing information and unintended deletion (see, e.g., Balaban & Shoval, 1999).

This condition was also experienced in the case study when evaluating the sales support system. In that particular system, the business offer was not represented as a regular entity relation in the database (i.e. it was not implemented as a separate relational table uniquely identifying offers). Instead, the offer was considered as a state attribute of a more general Sales entity (see Table 1).

Information about the Sales entity was then updated by changing its status from ‘Offer’ to ‘Order Confirmed’ when the purchase contract was established subsequently (see Table 2).

This led to the fact that when a purchase contract was established, information about the corresponding business offer (as a distinguishable and important business action) was no longer kept in the database. A problem caused by this solution was that the car dealers and the customers could not compare the offer with the purchase contract of the same car deal in situations when it was important to trace and compare these two generic business communication acts (cf. Goldkuhl, 1998). For example, it was impossible to compare the offered price (d16,000) to the price agreed upon in the business contract (d15,000). It also became difficult to make business analyses based on the information stored in the database. For example, it was difficult to see how many business offers had actually resulted in purchase contracts. This was believed to be essential information for analysing the effectiveness of the business.

![](/api/attachments/3VZDM6JM/fulltext/images/02351d601ca7fb0dbbdaac29a8cdecc0b5c9b7a8fac09b363a583d2905f5ff24.jpg)  
Figure 9 Relation between different communication actions.

![](/api/attachments/3VZDM6JM/fulltext/images/fa9cd8a369bd8d2907d82f831cd6577838f5395360e4a822d3ea7606aed8a0b0.jpg)  
Figure 10 The ‘complete’ resulting static conceptual model.

Table 1 Information stored in the Sales table when an offer had been made for a specific car deal (in this case Sale #1009)

<table><tr><td rowspan="2">Sale #</td><td rowspan="2">Date</td><td rowspan="2">Customer</td><td colspan="4">Relational Table Sales</td></tr><tr><td>Car Dealer</td><td>Amount</td><td>Status</td><td>Purchase object</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1009</td><td>18-12-97</td><td>James Howard</td><td>Jenny Doe</td><td>16000</td><td>Offer</td><td>399</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 2 Information stored in the Sales table after the purchase contract had been established for the same car deal as in Table 1 (Sale #1009)

<table><tr><td rowspan="2">Sale#</td><td rowspan="2">Date</td><td rowspan="2">Customer</td><td colspan="4">Relational Table Sales</td></tr><tr><td>Car Dealer</td><td>Amount</td><td>Status</td><td>Purchase object</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1009</td><td>20-12-97</td><td>James Howard</td><td>Jenny Doe</td><td>15000</td><td>Order confirmed</td><td>399</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

From this experience, we can learn the importance of considering important communication acts as object types in their own right, and that the state change of the business context to Order Confirmed should not merely be modelled and implemented as a state attribute associated with a Sales class. This does not mean that the business process cannot be modelled as a series of Sales object state changes in line with the Statechart in Figure 6. However, what it does mean is that if the business is modelled in this way it is important that essential communication actions that change the state of the Sales object are first thoroughly analysed from an action perspective (and not merely as events that change the state of the Sales object). They should still be modelled as separate classes and implemented in that way in the system. The lesson learned is that it is essential to examine critically all important business acts (both material and communication acts) to decide whether or not they should constitute regular entities about which the system must keep information. Our firm belief is that generally they should do so, to promote conceptual models that are capable of handling changing business requirements.

Arguably, it would be possible to arrive at a static model that reflects these concerns without explicitly applying the proposed action-oriented perspective. However, the proposed approach aims to make this occur by intention rather than by chance.

## Ontological discussion

The task undertaken in this paper, to reinforce ‘traditional’ conceptual modelling with a speech-act-based understanding of doing business, is far from unproblematic and the importance of such reconciliation may be hard to grasp at first. The reason, we believe, is that it requires a shift in perspective and because that shift brings with it a different ontological stance. As pointed out by Winograd (1988): ‘Within the community concerned with the design of computer systems, there is a growing recognition of the importance of the designer’s perspective – the concerns and interpretations that shape the design, whether they are articulated explicitly or are just part of the unexamined background of the work. A perspective does not determine answers to design questions but guides design by generating the questions to be consideredy [and] the outcome will differ depending on where we start.’ The ontological stance underpinning most contemporary conceptual modelling approaches has been characterized as founded in a descriptive view of information systems (Lyytinen, 1987). One basic assumption within the fields of entity-relationship modelling (Chen, 1976) and object orientation (e.g. Rumbaugh et al., 1991; Booch, 1994) is that information systems serve as images of reality. An IS could then be used to inform users about the state of the world. This implies an objectivistic and representational view of the use of language. With such a perspective the main modelling problem is to analyse how the external world (the universe of discourse, or business domain) should be mapped into, and represented in, the system (system domain) in a ‘true’ way. However, as recognized within the language/action perspective, there are dimensions in our language beyond the strictly representational one. People do things by using language within the world. Such doing has certain intentions and an utterance per se can therefore by viewed as an action. This also implies that an IS can be used to perform this type of actions – communication actions. With such a perspective, the main modelling problem is to analyse the communication acts performed by use of the system within the business, and how these acts may affect the business context. These properties of information as action are seldom discussed or taken into account in traditional approaches to conceptual modelling.

This ontological stance on which the proposed actionoriented perspective is founded means that what is important to capture during conceptual modelling is not restricted to what exists in the physical world, such as cars, physical deliveries, and people. In addition to these physical things, it is important to capture also social constructs existing in what can be referred to as a social world. Habermas (1979) divides the external world into an objective world consisting of physical objects and a social world consisting of semiotic objects. These semiotic objects include messages, obligations, commitments, etc., so-called social facts (Searle, 1996). Thereby, it becomes important to regard, for example, the offer and the contract as distinct and important object types during conceptual modelling. Not because they are physically manifested on (potentially) different (physical) documents, but because they are two different and important semiotic results of important business actions performed.

## Conclusion

In this paper, we have argued (a) on the one hand that traditional conceptual modelling has focused too much on the semantic aspects of language and too little on the pragmatic aspects and (b) on the other hand that speech act based modelling techniques have focused too much on the pragmatics of language and too little on the semantic aspects.

To remedy these shortcomings, we have proposed action-oriented conceptual modelling based on speech act theory. The ontological standpoint that we propose implies that information systems can be used by business actors to perform actions and to store information about performed as well as anticipated actions. We act in the world and manage information about action in the world. We must conceptualize and model the communication per se, not just the material world (or our conception of it). The propositional content of a language act can describe things that are yet to be, and we thus must understand conceptually and model both the existing world and a possible world.

Choosing speech act theory as a foundation for systems modelling is not a new concept. However, contemporary speech act based approaches, the CFA schema and Action Workflow being the most prominent examples, seem to have missed an important key notion within the theory, a notion that is crucial for the successful adoption of the theory as a foundation for conceptual modelling. In an attempt to incorporate the intentional action aspect into business and system modelling, they have actually swung the pendulum too far and neglected the coupling between the propositional content and the illocutionary component of speech – what is talked about and what speaking does. Illocutionary actions (or verbs) have not been in focus in static modelling before – neither in speech act based modelling, nor in entity-relationship or object-oriented modelling techniques. We claim that focusing on illocutionary actions together with the propositional content is essential when performing static modelling.

In this paper, we propose a focus on both material and communication acts and the business context within which these actions are performed. Based on an understanding of the dynamic structure of the business context, we have shown how a static conceptual model of the business can be arrived at. We propose actionoriented dynamic modelling where social action is analysed within a business context. This analysis is performed from within (i.e. from the actors’ perspective), and attempts to answer the question of what acting does (communicatively and materially). With this understanding as a base, we further propose action-oriented static

## References

A<sup>˚</sup> GERFALK PJ (2002) Messages are signs of action: from Langefors to speech acts and beyond. In Proceedings of the seventh international workshop on the language-action perspective on communication modelling (LAP 2002) (BARJIS J, DIETZ JLG and GOLDKUHL G, Eds), pp 81–100, Delft University of Technology, Delft, The Netherlands.

A<sup>˚</sup> GERFALK PJ and GOLDKUHL G (2001) Business action and information modelling: the task of the new millennium. In Information Modeling in the New Millennium (ROSSI M and SIAU K, Eds), pp 110–136, Idea Group Publishing, Hershey, PA.

ALLWOOD J (1987) Linguistic Communication as Action and Cooperation: A Study in Pragmatics. Department of Linguistics, University of Gothenburg, Gothenburg, Sweden.

ALLWOOD J (2000) An activity based approach to pragmatics. In Abduction, Belief and Context in Dialogue: Studies in Computational Pragmatics (BUNT H and BLACK B, Eds), pp 47–80, John Benjamins, Amsterdam.

AURAMa¨KI E, LEHTINEN E and LYYTINEN K (1988) A speech act based office modeling approach. ACM Transactions on Office Information Systems 6(2), 126–152.

AUSTIN JL (1962) How to do Things with Words. Oxford University Press, Cambridge.

BALABAN M and SHOVAL P (1999) Resolving the ‘weak status’ of weak entity types in entity relationship schemas. In Proceedings of the 18th International Conference on Conceptual Modelling (AKOKA J, BOUZEGHOUB M, COMYN-WATTIAU I and ME´TAI E, Eds), pp 369–383, Springer-Verlag, Heidelberg.

BOOCH G (1994) Object-oriented analysis and design with applications. Benjamin/Cummings, Menlo Park, CA.

BOOCH G, RUMBAUGH J and JACOBSON I (1999) The Unified Modeling Language User Guide. Addison-Wesley, Harlow, UK.

CHAMPION D and STOWELL F (2002) Navigating the gap between action and a serving information system. Information Systems Frontiers 4(3), 273–284.

CHECKLAND PB (1981) Systems Thinking, Systems Practice. Wiley, Chichester.

CHEN P (1976) The entity-relationship model: toward a unified view of data. ACM Transactions on Database Systems 1(1), 9–36.

CLARK HH (1996) Using Language. Cambridge University Press, Cambridge.

DENNING PJ and MEDINA-MORA R (1995) Completing the loops. Interfaces 25(3), 42–57.

DIETZ JLG (2001) DEMO: towards a discipline of organisation engineering. European Journal of Operational Research 128(2), 351–363.

modelling where social actions constitute conceptual objects about which the system is required to keep information. This analysis is performed from the outside, and attempts to answer the question of how the action is related to other things about which we must keep information. This way, the real strength of speech act theory as a foundation for conceptual modelling can be established. As a result, a foundation is laid for designing understandable systems that provide relevant information to users, and from which users can trace responsibilities for information, actions and commitments made.

## Acknowledgements

This work has been supported by the Swedish Knowledge Foundation’s program for the promotion of research in IT at new universities and university colleges in Sweden (IT-Lyftet), and by the Science Foundation Ireland Investigator Programme, B4-STEP (Building a Bi-Directional Bridge Between Software ThEory and Practice).

ERICKSON T and KELLOGG WA (2000) Social translucence: an approach to designing systems that support social processes. ACM Transactions on Computer-Human Interaction 7(1), 59–83.

ERIKSE´N S (2002) Designing for accountability. In Proceedings of the Second Nordic Conference on Human–Computer Interaction (NordiCHI 2002), pp 177–186, ACM Press, New York, NY.

ERIKSSON O (1998) Communication quality: a sales support system in the eyes of the customer. T&S Working Paper 1998:5, Dalarna University, Borla¨nge, Sweden.

FLORES F (1998) Information technology and the institution of identity: reflections since understanding computers and cognition. Information Technology & People 11(4), 352–372.

GOLDKUHL G (1995) Information as action and communication. In The Infological Equation: Essays in the Honour of Bo¨rje Langefors (Dahlbom B, Ed), pp 63–79, Gothenburg University, Gothenburg.

GOLDKUHL G (1998) The Six Phases of Business Processes: Business Communication and the Exchange of Value. JIBS Working Paper Series 1998-3, Jo¨nko¨ping International Business School, Jo¨nko¨ping, Sweden.

GOLDKUHL G and A<sup>˚</sup> GERFALK PJ (2002) Actability: a way to understand information systems pragmatics. In Coordination and Communication using Signs: Studies in Organisational Semiotics 2 (LIU K, CLARKE RJ, ANDERSEN PB and STAMPER RK, Eds), pp 85–113, Kluwer Academic Publishers, Boston.

GOLDKUHL G and LYYTINEN K (1982) A language action view of information systems. Proceedings of the Third International Conference on Information Systems (ICIS’82), pp 13–29.

GRAHAM I (1998) Requirements engineering and rapid development: An object-oriented approach. Addison-Wesley, Harlow, UK.

GREGERSEN H and JENSEN CS (1999) On the ontological expressiveness of temporal extensions to the entity-relationship model. In Proceedings of the er’99 workshop on evolution and change in data management, reverse engineering in information systems, and the world wide web and conceptual modelling (CHEN PP, EMBLEY DW, KOULOUMDJIAN J, LIDDLE SW and RODDICK JF), pp 110–121, Springer-Verlag, Heidelberg.

GULLIKSEN J, LIF M, SANDBLAD B, LIND M and NYGREN E (1997) Analysis of information utilisation (AUI). International Journal of Human-Computer Interaction 9(3), 255–282.

HABERMAS J (1979) Communication and the Evolution of Society. Heinemann, London.

HAREL D (1987) Statecharts: a visual formalism for complex systems. Science of Computer Programming 8(3), 231–274.

HOLM P (1996) On the Design and Usage of Information Technology and the Structuring of Communication and Work. Department of Computer & Systems Sciences, Stockholm University, Stockholm, Sweden, p 277.

HOLM P and LJUNGBERG J (1996) Multi-discourse conversations. Proceedings of the Fourth European Conference on Information Systems, p 835–848.

LANGEFORS B (1995) Essays on Infology: Summing Up and Planning for the Future. Studentlitteratur, Lund.

LYYTINEN K (1986) Information Systems Development as Social Action: Framework and Critical Implications. Department of Computer Science, University of Jyva¨skyla¨, Jyva¨skyla¨, Finland.

LYYTINEN K (1987) Two views of information modeling. Information & Management 12(1), 9–19.

MATHIASSEN L, MUNK-MADSEN A, NIELSEN PA and STAGE J (2000) Objectoriented Analysis & Design. Marko Publishing House, Aalborg, Denmark.

MEAD GH (1934) Meaning. In Mind, Self and Society from the Standpoint of a Social Behavoirist (MORRIS CW, Ed), pp 75–82, University of Chicago Press, Chicago.

## About the authors

Dr Pa¨r J A<sup>˚</sup> gerfalk, PhD, is Assistant Professor (universitetslektor) in Informatics at O<sup>¨</sup> rebro University, Sweden and postdoctoral research fellow with the University of Limerick, Ireland. Dr A<sup>˚</sup> gerfalk’s current research centres on human and social aspects of information systems development and use, particularly how language/action theory can inform the design process.

NURMINEN MI (1988) People or Computers: Three Ways of Looking at Information Systems. Studentlitteratur, Lund.

RUMBAUGH J, BLAHA M, PREMERLANI W, EDDY F and LORENSEN W (1991) Object-oriented Modeling and design. Prentice-Hall, Englewood Cliffs.

SEARLE JR (1969) Speech Acts: An Essay in the Philosophy of Language. Cambridge University Press, Cambridge.

SEARLE JR (1996) The Construction of Social Reality. Penguin, London.

SNOECK M and DEDENE G (1998) Existence dependency: the key to semantic integrity between structural and behavioural aspects of object types. IEEE Transactions on Software Engineering 24(4), 233–251.

WAND Y, STOREY VC and WEBER R (1999) An ontological analysis of the relationship construct in conceptual modeling. ACM Transactions on Database Systems 24(4), 494–528.

WINOGRAD T (1988) A language/action perspective on the design of cooperative work. Human–Computer Interaction 3(1), 3–30.

WINOGRAD T and FLORES F (1987) Understanding Computers and Cognition: A New Foundation for Design. Addison-Wesley, Reading, MA.

Dr Owen Eriksson, PhD, is Assistant Professor (universitetslektor) in Informatics, Dalarna University, Sweden. Dr Eriksson’s main research fields are systems architectures (including standardization), conceptual modelling and database design based on language/action theory, and the use of mobile technology in the transport and travel industry.
