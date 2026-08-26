---
otero_id: 20150
otero_key: "9CUYHD9U"
title: "A specification pattern for use cases"
authors: "Isabel Dı́az; Francisca Losavio; Alfredo Matteo; Oscar Pastor"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.10.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A specification pattern for use cases

Isabel Dı´az<sup>a,b,c,\*</sup>, Francisca Losavio<sup>b</sup>, Alfredo Matteo<sup>b</sup>, Oscar Pastor<sup>c</sup>

<sup>a</sup>Facultad de Ciencias Econo´micas y Sociales, Universidad Central deVenezuela, Caracas 1041-A, Venezuela

<sup>b</sup>Facultad de Ciencias, Universidad Central de Venezuela, Escuela de Computacio´n — Centro ISYS, Caracas 1041-A, Venezuela <sup>c</sup>Departamento de Sistemas Informa´ticos y Computacio´n, Universidad Polite´cnica de Valencia — Camino de Vera s/n, Valencia 46022, Spain

Accepted 1 October 2003

Available online 9 April 2004

## Abstract

In this paper, general formats and guidelines are proposed, in an attempt to ameliorate the impact of frequently observed difficulties during the specification of use cases generated using ‘‘natural language’’ for the documentation of system functionality. The various writing styles derived from the multiple grammatical alternatives found in the Spanish language and the terminological diversity that characterises this language tend to reduce the clarity of text in a use-case specification. Thus, the purpose of its use in the different stages of development in a software system or component is seriously affected. However, even if this study has been made specifically for the Spanish language, it could be easily generalised to any language whose sentences are of the form subject/predicate. In order to control these problems, the use of a specification pattern supported by a series of guidelines on style and terminology is proposed for drafting use cases. Additionally, various degrees of refinement are suggested to guide specifiers towards obtaining a use case written according to this pattern.

Keywords: Use case; Use case model; Use case specification; Requirements determination; Information systems development; Requirements elicitation; Requirements specification

## 1. Introduction

Requirements determination is one of the most critical tasks in software development. Its main goal is to identify and establish the functionality required by the system in order to satisfy the requirements of its potential users [3]. The success of this process should guarantee, to a great extent, the success of the software systems that will be constructed from the specification. The requirements determination process can be described as having three phases: requirements identification (elicitation), requirements documentation (representation) and proof correctness of the requirements (validation) [19,24].

The construction of the use case model is one of the most widely used techniques of requirements determination. It is applied to all phases of this process, facilitating requirements elicitation, representation and further validation [17]. This model is basically made up of four elements: the actor, the use case, the actor–use case relationship and the use case–use case relationship. An actor represents the role that a set of system users must play (a type or category of system users). One or more use cases are identified for each actor; they describe the services that the system should offer to these users.

The use case specification is expressed in natural language: this is quite convenient, because it is the natural way to interact with the potential users of the system, in order to capture their desired functionality. However, natural language has a drawback for requirements validation because of its ambiguity. The goal of this work is to take advantage of the grammatical structure of the natural language to provide a structure for use case textual specification in order to avoid ambiguities, while maintaining the communicational advantages of the natural language.

In the early stages of development, the most common form of expressing a use case is by means of a text written in ‘‘natural language’’. Using this representation, the specification of a use case is a document in which a specific functionality of an entity is described (i.e. a system, software component or modelling element). This functionality is expressed as the complete sequence of interactions that take place between the actor and the entity for the purpose of complying with a specific requirement.

Through the use of natural language, any person can understand the manner of expressing use cases without needing to be trained to do so. Modellers can easily write the requirements and communicate them to the domain experts, users and software developers using a simple terminology which is well known by most. However, these natural language advantages may become disadvantageous as ambiguities, inconsistencies and redundancies may be generated in the description of the entity’s requirements [2,4]. Two factors have a decisive influence on this situation: the writing, a determinant factor for the comprehension of the use case and the terminology, relating to the identification of the elements that intervene in the entity’s functionalities.

Writing and terminology depend mainly on the people in charge of the specification; they have different writing skills and styles and use various terms to express the same concept or idea. However, when the use case is adopted at different times during the development stage, ‘‘incorrect’’ or ‘‘complicated’’ writing could result in wrong or doubtful interpretation of the requirement. Diversity in vocabulary could also create redundancies or inconsistencies in the design of the entity. For example, different classes of objects may be defined with the same name or different names may be used for a single class of objects.

On the other hand, since there are no restrictions on the abstraction levels of the use case, its specification can be as detailed or as general as desired. This leaves the level of abstraction up to the judgement of the people responsible for creating the use cases; therefore, they may be so general as to be too ambiguous or so detailed that any modification in the requirements requires a complete rewrite.

This paper studies various aspects of the textual specification of use cases from a grammatical perspective. Some restrictions are established to diminish difficulties arising from the use of a ‘‘natural language’’ by controlling multiple writing styles and the variety of terms characteristic of the Spanish language, by the definition of a conceptual framework and by establishing certain norms and formats. These facilitate the specification task and enable better understanding which leads to better use cases, based on the objective they fulfil during the construction process [11–14]. The proposed conceptual framework is based on that defined by the unified modelling language (UML) for the use case model [22]. The proposed guidelines and formats are based on those described by Cockburn and Constantine in [6–9].

The theoretical framework presented here is expressed by a UML meta-model, which extends the use case package meta-model and provides the conceptual basis for our approach. It is used to structure and organise the natural language specification of the use case. Our approach does not exclude other representations; it can also be used to complement them. Different representations of use case can be appropriate, depending on the phase of the system’s development. For example, sequence or collaboration diagrams are used mostly during the analysis activity, while the textual specification is more appropriate for early stages of development. Textual specification uses the natural language of the potential system users, whereas other representations can only be elaborated and understood by more trained participants in the software project. It is generally accepted that formal representations overcome ambiguity. However, there is also general agreement that informal representations facilitate the exchange of information required to elicit and specify the requirements at early stages of development.

## 2. Specification of use cases through simple sentences

In its written form, the description of activities carried out by an entity when interacting with an actor is expressed through a series of sentences. From the grammatical standpoint, these may be simple or compound. Simple sentences are characterised as having only one subject and one predicate. Compound sentences may have more than one subject and/or more than one predicate [1,15,21]. Fig. 1 presents examples of these types of sentences.

The use of compound sentences to describe a use case makes it harder to understand. This is because these types of sentences could simultaneously express various activities carried out by the entity in one or more interactions with the actor. If we add the various ways in which compound sentences can be constructed (by co-ordination or subordination) and their corresponding classifications, the grammatical complexity that they can achieve becomes unmanageable. It would thus be desirable not to use compound sentences in the description of use cases.

A compound sentence can always be divided into two or more simple sentences (Fig. 2), except when there is a compound subject and the verbal action does not correspond separately to each subject (Fig. 3). Nevertheless, this limitation would never be present when writing use cases. Inasmuch as use cases describe the functionality of the entity through their interactions with an actor, the subject of the sentences could only be the actor or the entity. Therefore, it is impossible for sentences for a use case to have compound subjects. Two important conclusions can be gathered from this. Firstly, compound sentences in a use case always admit decomposition into two or more simple sentences. Secondly, a use case can be written using only simple sentences.

## 2.1. Simple interface and process sentences

Given that a use case can be completely written using simple sentences, these may be considered as its basic construction units. Thus, each simple sentence would describe one single activity or action (predicate) carried out by the actor or the entity (subject).

According to the definition of a use case, the activity or action described in a simple sentence can only refer to an actor-entity interaction or to an internal action executed by the entity itself. Let us analyse these two situations using an elemental communication model for the sole purposes of illustrating how each simple sentence is dedicated to communicating, transmitting, or reporting what the actor or the entity knows, does, or has.

Fig. 4 shows the elements intervening in the communication model and their counterparts in the specification of a use case:

\- The speaker or sender (actor or entity).

\- The interlocutor or receiver (actor or entity).

\- The communications channel or route (mechanism by means of which the sender-receiver interaction is carried out).

\- The message (communication sent by the sender to the receiver).

The communication relationship is established when the sender sends a message to the receiver through a specific channel. Within the context of a use case, this relationship can be expressed in written form using a simple sentence with the following characteristics:

<table><tr><td>SIMPLE SENTENCE</td><td>Louise goes to the market</td></tr><tr><td>COMPOUND SENTENCE (TWO SUBJECTS)</td><td>Louise and Carmen go to the bakery</td></tr><tr><td>COMPOUND SENTENCE (TWO PREDICATES)</td><td>Louise goes to the market and to the bakery</td></tr></table>

Fig. 1. Simple and compound sentences.

<table><tr><td>COMPOUND SENTENCE (TWO PREDICATES)</td><td>Louise goes to the market and to the bakery</td></tr><tr><td>SIMPLE SENTENCE</td><td>Louise goes to the market</td></tr><tr><td>SIMPLE SENTENCE</td><td>Louise goes to the bakery</td></tr></table>

Fig. 2. Decomposition of a compound sentence into two simple sentences.

![](/api/attachments/9CUYHD9U/fulltext/images/4b3cc7ef7d9d524ca9f41596443f1e92cefbb5416a3ac77524a709c7481c0917.jpg)  
Fig. 3. Compound sentence that admits no decomposition.

(1) The sender corresponds to the subject of the simple sentence. Therefore, the subject can be the actor for which the use case is written or the entity for which the functionality is being specified. In the example of an automatic teller machine system (ATMS), there are three possible senders (Fig. 5): the client and the operator as well as the ATM machine itself.

(2) The message sent by the sender through the communication channel corresponds to the predicate in a simple sentence. A message is information about the action or operation executed by the subject in the sentence at a given moment. Notice that this information can be:

 Supplied by the actor for the entity (Fig. 6A).

 Produced by the entity for the actor (Fig. 6B).

 Referring to an action carried out internally by the entity that may or may not modify its status (Fig. 6C).

(3) When the sender is the actor, the receiver of the message is always the entity (sender ¼ actor and receiver ¼ entity). Therefore, the predicate of the simple sentence describing the interaction between these shall correspond to an action executed by the actor to supply information to the entity.

![](/api/attachments/9CUYHD9U/fulltext/images/3cd49d2d2e4b5fd443cb9749ee506b77cf1a9a19d9583e219a72142f1d969506.jpg)  
Fig. 5. Use case model for an ATMS.

(4) When the sender is the entity, two situations can take place: the receiver might be the actor (sender ¼ entity and receiver ¼ actor), or the receiver can be the entity itself (sender ¼ receiver ¼ entity). In the first case, the predicate of the simple sentence corresponds to the information that the entity sends to the actor. In the second case, the predicate describes an action executed by the entity on itself, which may or may not create a change in its internal status.

The characteristics of simple sentences allow us to distinguish two communicational properties: unidirectionality (each simple sentence describes only one direction of the interaction) and atomicity (decomposition into several unidirectional interactions is not allowed). Note that the use of simple sentences as basic constructors of the use case textual specification is sufficient to express all the information that the specification must provide: each simple sentence describes the exchange of actor-entity information or the actions that are internally performed by the entity, as a consequence of this interaction. The unidirectionality and the atomicity properties permit the complete representation of the functionality of an entity in terms of the use case definition.

![](/api/attachments/9CUYHD9U/fulltext/images/57ed205f954b0a721ccbd1812a5ebd2c95b5626a598177464bf1510b88a17da9.jpg)  
Fig. 4. Elemental communication model.

<table><tr><td>(A) The Client introduces the digits of his secret password.</td></tr><tr><td>(B) The ATMS informs the Client on the types of transaction he may carry out.</td></tr><tr><td>(C) The ATMS verifies the validity of the password in the magnetic tape of the card.</td></tr></table>

Fig. 6. Examples of communications.

On the other hand, according to the types of messages sent to the receiver (depending on whether the sender is the actor or the entity), there are two types of simple sentences that can be used in the specification of a use case: interface and process sentences. Interface sentences describe the communication between the actor and the entity or vice versa. Their characteristic is that they refer to the actor-entity interaction and indicate, directly or indirectly, implicitly or explicitly, how this is carried out and the mechanisms used to support the communication (windows, buttons, protocols etc.). Sentences (A) and (B) in Fig. 6 are examples of simple interface sentences.

Process sentences show the actions carried out individually by the entity that have implications on it. They are different from simple interface sentences, as they do not require participation by the actor. The entity is, at the same time, the sender and the receiver of the communication. Fig. 6C presents an example of a simple process sentence.

## 2.2. Elements in a simple sentence

Any simple sentence used in the specification can be written as indicated in the sketch in Fig. 7. This format, which is similar to that proposed by Cockburn in [5], has two optional construction elements: a precondition and a restriction. The rest of its elements are indispensable for the sentence to make sense as it forms the subject and predicate. The actor or the entity is responsible for executing an activity in the use case that is being written. Using the communication model, the sender of a message is identified. In general terms, the sender fulfils the function of the subject in a simple sentence.

The activity in a simple sentence describes the action executed by the actor or the entity. From the standpoint of the communication model, the activity corresponds to the message sent by the sender to the receiver. Grammatically speaking, the activity is the predicate of the simple sentence. Therefore, its specification revolves around a verb which indicates the action executed by the subject.

![](/api/attachments/9CUYHD9U/fulltext/images/2ae5144572ea1656be71b1ddec84a570d6f8d82ccce9e5468d655d32a2124e31.jpg)  
Fig. 7. Pattern for a simple sentence.

<table><tr><td colspan="4">After the cash has been dispensed, the ATMS returns the card to the client in a time lapse no greater than 10 seconds</td></tr><tr><td>Precondition</td><td>Entity</td><td>Activity</td><td>Restriction</td></tr></table>

Fig. 8. Example of a simple sentence.

On the other hand, restrictions are conditions or limitations that are applicable to the activity. The precondition stops the execution of the simple sentence unless it fulfills the prior requirement. It can be expressed in different connectors: temporal, ranking, place, etc. Grammatically speaking, preconditions as well as restrictions are propositions that are subordinated to the subject or to the predicate of the sentence. If extracted from the sentence in which they appear, these propositions lack meaning and are ambiguous or lose the function for which they were originally written. The simple sentence shown in Fig. 8 was written in the proposed form.

## 2.3. The style of a simple sentence

The richness of linguistic elements and the diversity of grammatical structures in the Spanish language make it possible for a simple sentence to be expressed in several ways. The proposed format for the construction of sentences of this type requires an initial effort to restrict the possibilities offered by the language. In particular, by means of the pattern of Fig. 7, one single static structure was established for the construction of simple sentences. Thus, each was structured in the same fashion and the same components were located in the same order in any of the sentences.

Nevertheless, in spite of the structure, the spectrum of possible ways to express a simple sentence still remains very broad. This is because the components, principally the subject and the predicate, can be presented using various forms, meanings, numbers, modes, times and genders. The intention then is to propose some guidelines or directives in an attempt to reduce this broad array of grammatical alternatives. The objective is to establish controls for handling the diversity of simple sentences in an attempt to facilitate the job of the people who draft use cases. Also, with a uniform writing style, comprehension by the people using use cases in other entity development tasks are facilitated.

To achieve this objective, the following norms are proposed to govern the writing of simple sentences in a use case [20]:

(1) The simple sentence must be written in a declaratory, affirmative and active manner. A sentence is declaratory or enunciative when it communicates or informs that something is taking place. By means of this norm, the use of interrogation, exclamation, or imperative sentences is hindered in the specification of use cases. On the other hand, the sentence must indicate affirmative actions. The active mode shows the subject of the sentence as directly responsible for the declaration. For instance, in Fig. 9, one sentence has been expressed in various ways. The first on this list presents the desired traits whereas the others do not comply with the guidelines.

<table><tr><td>DECLARATORY, AFFIRMATIVE AND ACTIVE SENTENCE</td><td>The Client introduces the digits of his secret password</td></tr><tr><td>OTHER TYPES OF NOT ALLOWED SENTENCES :</td><td></td></tr><tr><td>INTERROGATIVE SENTENCE</td><td>Does the Client introduce the digits of his secret password?</td></tr><tr><td>IMPERATIVE SENTENCE</td><td>Introduce the digits of your secret password</td></tr><tr><td>EXCLAMATIONSENTENCE</td><td>All the digits of the secret password have been introduced!</td></tr><tr><td>DUBITATIVE SENTENCE</td><td>Perhaps the Client will introduce the digits of his secret password</td></tr><tr><td>DESIDERATIVE SENTENCE</td><td>Hopefully the Client will introduce the digits of his secret password</td></tr><tr><td>NEGATIVE DECLARATORY SENTENCE</td><td>The Client does not introduce the digits of his secret password</td></tr><tr><td>PASSIVE DECLARATORY SENTENCE</td><td>The digits of the secret password have been introduced</td></tr><tr><td>NAME WITHOUT ADJACENT WORDS</td><td>The Client introduces the digits of his secret password</td></tr><tr><td colspan="2">NAME WITH ADJACENT WORDS OF THE TYPE (NOT ALLOWED SENTENCES):</td></tr><tr><td>ADJECTIVE</td><td>The attentive Client introduces the digits of his secret password</td></tr><tr><td>PREPOSITIONAL SYNTAGMA</td><td>The Client that is in the queue introduces the digits of his secret password</td></tr><tr><td>EXPLICATIVE SENTENCE</td><td>The Client, with no cash, introduces the digits of his secret password</td></tr><tr><td>NAME WITH APPOSITION</td><td>The Client, the person who has a bank account, introduces the digits of his secret password</td></tr></table>

Fig. 9. Declaratory, affirmative and active sentences versus other types of sentences.

Fig. 10. Names with and without adjacent words.

(2) Identification of the subject in the simple sentence. The actor or entity must be a proper substantive name stated in the singular. To highlight this characteristic, the first letter in the name should be written in upper case. On the other hand, the name may or may not have a corresponding article, depending on its gender (female or male). Notice that the structure for simple sentences in a use case does not allow for the use of terms that are adjacent to the name. The use of the accompaniments of the names (adjective, explanation and apposition) provides no further information about their interaction with the entity. What is really important is the action performed by the actor (‘‘. . .the client introduces the digits . . .’’). Fig. 10 shows how the name in a simple sentence may be complemented with other terms. Such examples are an attempt to illustrate what must not be done according to the established norms.

(3) The verb of the simple sentence, i.e. the word in the predicate indicating the action to be executed by the subject, must be expressed in:

 Indicative mode: the verb must absolutely and conclusively indicate the action to be executed without needing another verb.

 Present tense: the verb must temporally locate the action of the subject in the present moment.

 Simple form: the syntax of the verb must consist of one single word.

 Singular number: since the actor or entity only executes the action of the sentence, the verb must be presented in the singular.

 Third person: the conjugation of the verb must correspond to the third person, singular (he, she, or it).

Fig. 11 exemplifies the characteristics that the verb must have in a simple sentence for use case. Examples of verbal constructions that do not comply with these guidelines are also given.

## 2.4. Terminology in simple sentences

Up to this point, we have established one single structure as well as a series of guidelines to support the construction of sentences describing a use case. Both measures are aimed at alleviating problems related to their writing. Another aspect that must be considered has to do with the domain of the problem. Knowing the multiple problems that could arise due to its inadequate handling, it is advisable to make some observations.

The terms employed for writing a simple sentence, especially those identifying physical or conceptual elements, must basically coincide with those used in the domain of the definition of the entity. They must only be modified when a reasoned argument exists; for instance, for terms that may be confused with others or in order to highlight a specific aspect of their semantics.

<table><tr><td>SIMPLE INDICATIVE MODE, PRESENT TENSE ANDTHIRD PERSON SINGULAR:</td><td>The Client introduces the digits of his secret password</td></tr><tr><td colspan="2">VERB WITH DIFFERENT CHARACTERISTICS (NOT ALLOWED SENTENCES):</td></tr><tr><td>COMPOUND VERB FORM</td><td>The Client has introduced the digit of his secret password</td></tr><tr><td>FUTURE TENSE</td><td>The Client shall introduce the digits of his secret password</td></tr><tr><td>THIRD PERSON PLURAL</td><td>The Clients introduce the digits of their secret password</td></tr></table>

Fig. 11. Characteristics of the verb in a simple sentence.

In order to homogenise and control the terminology, the use of the following resources is suggested:

(1) Construct a top-level model for the objects of the domain, prior to initiating the development of the use case model. This could help in establishing a common vocabulary that would serve as the basis for writing the use cases.

(2) Create data dictionaries to record and centralise the meaning of the terms used by all the people responsible for writing use cases.

(3) Establish work strategies that would keep all the people involved in writing the use cases informed of all updates to the data dictionaries.

## 3. Pattern for the specification of use cases

The writing of use cases is an incremental and iterative process. Thus, it first takes the form of a short, generic text written in prose. However, as a greater knowledge of the domain is garnered, this text can grow in size and detail, acquiring complex forms.

One action pursuing this objective involves the manner in which the use case is finally expressed. For this, the following directives can be set forth:

\- As Jacobson et al., proposed in [16], the basic path must be differentiated from alternatives.

\- The basic path must be developed as a numbered list of chronologically ordered simple sentences (See Fig. 12).

\- The first sentence in the basic path must report the event that activated the execution of the functionality described in the use case. It will always be the actor who initiates the execution of the path of events in a use case.

\- The last sentence in the basic path must describe the termination of the execution of the functionality.

\- Pre-conditions in simple sentences belonging to the basic path of the use case must not refer to events describing situations leading to an alternative. By default, it is supposed that, so long as the sequence of the basic path is followed, the event generating the activation of the alternative path is not being met.

\- Each alternative path must be preceded by the event it activates. When this event takes place, then the

<table><tr><td>USE CASE</td><td></td></tr><tr><td>SUMMARY</td><td></td></tr><tr><td>ACTOR</td><td></td></tr><tr><td>PRECONDITION</td><td></td></tr><tr><td>DESCRIPTION</td><td>Basic PathINITIATES WHEN1) [][2) [N) [ENDAlternative Paths1) |[2) |......</td></tr><tr><td>OSTCONDITION</td><td></td></tr></table>

Fig. 12. Basic format for the specification of use cases.

![](/api/attachments/9CUYHD9U/fulltext/images/ba4bb2fdf5478b8c8e445ecfcbea82e1e8e460737b976d77ecd5d272eef97b9a.jpg)  
Fig. 13. Example of a use case specification.

basic path ceases to be fulfilled and the sequence for the alternative path begins. Therefore, the event may be considered to be a condition that must be met for the execution of the following actions: heventi :¼ hconditioni :¼ htexti. Each of these actions must be written using numbered simple sentences (just as in the basic path).

Fig. 12 presents the basic format for the specification of use cases, which responds to the directives previously enumerated. From a linguistic point of view, the semiotic levels of this specification are its syntax and the associated semantics [10].

To illustrate this, Fig. 13 shows the specification for the withdrawal use case in an ATMS.

## 3.1. Control structure

The flow of events in a use case can be presented as a numbered list of simple sentences. However, this flow of events does not always follow a sequential path that develops in the same order as the sentences. On occasion, the sequence of events may bifurcate or may have an iterative or repetitive nature, when complying with a specific condition.

![](/api/attachments/9CUYHD9U/fulltext/images/ca5b6b1ca291fb076dae4ec1220b491d545bd661dcc489cbce0e1e0a8f8d3c9b.jpg)  
Fig. 14. Control structures.

In order to represent these special cases, the use of traditional logical control structures in structured programming is used. Fig. 14 shows an example.

## 3.2. Extension and inclusion relationships among use cases

Complexity (reuse) in the use cases model is handled by the extend and include relationship. In this sense, Special sentences are proposed.

The extend relationship, which was defined by UML in a similar fashion to that of Jacobson, establishes the existence of a ‘‘condition’’ and a reference to an ‘‘extension point;’’ i.e. a position in the use case where the incorporation of the new functionality is to take place. The functionality of the base use case is independent of the functionality that describes the use case that extends (Fig. 15). A use case may extend many use cases just as a use case may be extended by more than one use case.

The specifications of the use cases involved in an extension relation are explicitly represented in the extending use case where the special sentence shown in Fig. 16 is used. The extension is executed before or after the extension points of the base use case. The true value of the extension condition determines whether the extension will be executed. In view of the fact that a use case can extend a base use case at more than one point, while keeping the same extension condition, the format gives one or more extension points.

![](/api/attachments/9CUYHD9U/fulltext/images/eec3ec6c96d9707158d5ed2a2b73c374bfe594a69eb20968b1cb7fdf483915ec.jpg)  
Fig. 15. Types of relationships among use cases.

It is possible for the extending functionality itself to be an alternative path. When this occurs, the event that activates the alternative path coincides with the condition so that the extension takes place. For these cases, the format is that shown in Fig. 17.

In the include relationship, the functionality defined in a use case is completely incorporated into the base use case, in the place specified. Unlike the extension relationship, the inclusion relationship that carries out the functionality specified by the base use case depends on what is described in the included use case. It may be included in more than one use case but it is also possible to include the functionality of several use cases into one single one.

Similarly, the include relationship only required to be expressed in the text of the base use case. The

EXTEND TO <base use case> WHEN <event>

Fig. 17. Sentence for extending a use case (alternative path).

INCLUDE <name IncludedUseCase>

Fig. 18. Sentence for including a use case in a base use case.

execution of the use case that is included does not depend on where it is included. The sentence in Fig. 18 is applied in order to express the include relationship. It should be located according to the specification pattern at the location of the base use case sequence where the functionality is included.

The degrees of refinement in the specification allow for the establishment of a reference scale: ranging from the first, which presents the most elemental use case specification, to the last, showing the greatest detail. Consider a use called A and suppose that $A _ { \mathrm { i } }$ and $A _ { \mathrm { J } }$ are two descriptions of the same use case with varying degrees of refinement. It is said that $A _ { \mathrm { J } }$ is a refinement of $A _ { \mathrm { i } }$ if $A _ { \mathrm { J } }$ has a greater degree of refinement than $A _ { j } .$

Degrees of refinement in the specification of use cases are selected by the specifiers as per their convenience, depending on their knowledge of the domain of the problem, the entity’s stage of development, the demands established at the managerial level and their expertise with respect to the writing of use cases.

The degrees of refinement in the specification of a use case are:

Degree 1 In prose (unstructured textual) form.

Degree 2 As a numbered listing of sentences.

Degree 3 As a numbered listing of sentences in which the basic path is differentiated from alternative paths.

Degree 4 As a numbered listing of simple sentences in which the basic path is differentiated from alternative paths.

Degree 5 As a numbered listing of simple sentences written according to the basic format for the specification of use cases, where the basic path is differentiated from alternative paths.

Degree 6 As a numbered listing of simple sentences written according to the basic format for the specification of use cases where the basic path is differentiated from alternative paths. Simple sentences are written applying the rules on style.

Degree 7 As a numbered listing of simple sentences written according to the basic format for the specification of use cases, where the basic path is differentiated from alternative paths. Apart from style considerations, control structures are incorporated into the sequence as well as the respective beginning and closing sentences.

Degree 8 The terminology used in each of the simple sentences is adapted to what was defined through the objects domain model and the dictionaries created for this purpose.

Degree 9 The use case is documented using, for instance, meta-information descriptors associated to the basic format for the specification of use cases.

## 4. Refinement of a use case

The refinement of a use case has to do with the amount of detail incorporated in the text of a use case, regardless of its scope, i.e. the context or domain in which it is defined [18]. The more precise, thorough and explanatory the description, the higher the refinement of the use case.

Using the classification introduced by Constantine, if the use case is expressed with a refinement of degree 1, it has a high level format; whereas if the use case with a refinement of degree 2 or more, it has an expanded format.

On the other hand, Fig. 19 describes the more important characteristics in use cases in terms of their structure, the relationships that are established ACCORDING TO THE CLASSIFICATION ESTABLISHED BY CONSTANTINE IN [6]

<table><tr><td>USE CASE</td><td></td></tr><tr><td>LEVEL OF ABSTRACTION †</td><td>{&#x27;essential&#x27; | &#x27;real&#x27;} | {&#x27;dialogue&#x27; | &#x27;semantic&#x27;}</td></tr><tr><td>LEVEL OF DETAIL ‡</td><td>{&#x27;high level&#x27; | &#x27;expanded&#x27;}</td></tr><tr><td>DEGREE OF REFINEMENT</td><td></td></tr><tr><td>EXTENSIONS</td><td>EXTEND TOWHENAFTER|BEFORE</td></tr><tr><td>INCLUDES</td><td></td></tr><tr><td>STATUS</td><td>&lt;`proposed&#x27;, `in development&#x27;, `awaiting revision&#x27;, `approved&#x27;&gt;</td></tr><tr><td>OBSERVATIONS</td><td></td></tr></table>

† ACCORDING TO THE CLASSIFICATIONS ESTABLISHED, RESPECTIVELY, BY CONSTANTINE AND COCKBURN IN [6, 8]

Fig. 19. Format for the registration of meta-information in a use case.

among them and the degrees of refinement. This information complements that shown in Fig. 12.

## 5. Meta-model for use cases specification

Fig. 20 shows a synthesis of the theoretical framework to the written description of functionalities in an entity. The framework is presented as an extension or profile of the use case package of the

UML meta-model. Note that 14 new classes related by association, aggregation or inheritance to the UML classes of the use cases package were incorporated (use case, actor, extend and include).

Each use case holds a textual specification described by the specification class. This specification is associated to a degree of refinement (refinement degree class). The basic and alternative classes describe the types of paths of a textual specification. Each path is composed by sentences which can be simple sentence or special sentences. The activation of a sentence belonging to an alternative path depends on an event (Event class). The Sub-functionality class represents the group of sentences defining a partition of the functionality of the use case.

![](/api/attachments/9CUYHD9U/fulltext/images/f46b333b484a00a32b9124eb88485a46348ed3c03659ac71c64b0c5d88e27bc8.jpg)  
Fig. 20. Meta-model for the specification of use cases.

The interface sentence class and the process sentence class distinguish the simple sentences of actorentity interaction from those modifying the state of the entity. The special sentences describing the type of relations among the use cases are represented by the extend and include classes. Special sentences expressing bifurcations or iterations of a set of simple sentences are represented by the control class. Other types of special sentences allow for the identification of the begin-end of a basic path (beginning and end classes).

The UML meta-model expresses the conceptual elements related to the specification pattern; it is used as a guide to implement the semantic component of a support tool under development at the Universidad Central de Venezuela. The purpose of this tool is to provide automatic support to the use case textual specification. The main functionalities are: consistency control for validation, version management for specification reuse, administration management and co-operative work for collaborative specification, partial or automatic edition of the structure rules and style and use of the terminology. It includes the use case degree of refinement for specification flexibility. This tool can be focused as a ‘‘plug-in’’ of rational products [23].

Up to now, the proposed use cases specification pattern has been applied manually for academic and commercial projects. The results have been satisfactory for solving structure, abstraction and terminology problems of use case specifications, thereby improving the overall quality of the textual specification. However, this experience has shown that co-operative work, changes and consistency control are tasks that must be supported by automation. In this sense, the requirements of the supporting tool have been established.

## 6. Conclusions

From a grammatical standpoint, any use case can be specified using an orderly sequence of simple sentences, that is to say sentences with a single subject (the actor or entity) and a single predicate (the activity or action executed by the actor or entity). Execution of the activity in a simple sentence may or may not be limited by the fulfilment of a prior requirement (precondition) or may be executed in a specific manner (restriction). Guidelines have been established on the style and terminology to be used to express simple sentences for a use case.

Simple sentences in a use case are classified as interface or process sentences according to their objective. Apart from simple sentences, a use case may contain special sentences. These can be beginning, end, control, extension and inclusion sentences. Specifically, special control sentences are made up by a series of sentences that can be simple or special.

The communication model has shown that it is possible to express the complete functionality by the use case, with only simple sentences. The use of simple sentences is not restricted to the Spanish language and can be applied to any other language that has the subject/predicate construction as a basic structure for sentences.

A pattern for the specification of use cases including meta-information relating has also been proposed. The main body of the pattern differentiates the basic path from alternative paths. Each one of these is conceived as a sequence of simple and special sentences with a particular format. Nine degrees of refinement in a use case were established; each expresses varying levels of abstraction in its specification. Finally, the metamodel constrains the conceptual elements related to the proposed specification framework. The metamodel is used as a semantic basis to build a support tool that automates the use case specification pattern. Our meta-model is an extension of the use case package of the UML meta-model.

## Acknowledgements

This research has been financed by CONICIT – Venezuela, Project MOODe S1-95000512.

## References

[1] E. Alarcos, Grama´tica de la Lengua Espan˜ola. Real Academia Espan˜ola. Coleccio´n Nebrija y Bello. Editorial Espasa Calpe. Madrid, Espan˜a. Octubre, 2000.

[2] E. Berard, Be Careful with ‘‘Use Case’’. http://www.toa.com/ pub/use\_cases.htm.

[3] G.J. Browne, V. Ramesh, Improving information requirements determination: a cognitive perspective, Information & Management 39, 2002, pp. 625–645.

[4] A. Cockburn, Goals and use cases, Journal of Object-Oriented Programming 10 (5), 1997, pp. 35–40.

[5] A. Cockburn, Using goal-based use cases, Journal of Object-Oriented Programming 10 (7), 1997, pp. 56–62.

[6] A. Cockburn, Writing Effective Use Cases. Addison-Wesley, 2001.

[7] L. Constantine, Essential modeling: use case for user interfaces, Interactions ACM 2 (2), 1995, pp. 35–46.

[8] L. Constantine, L. Lockwood, Software for Use: A Practical Guide to the Models and Methods of Usage-Centered Design. Addison-Wesley, Boston, 1999.

[9] L. Constantine, L. Lockwood, Structure and style in use cases for user interface design, in: M.V. Harmelen, S. Wilson (Eds.), Object Modeling and User Interface Design: Designing Interactive System, Addison-Wesley, 2001.

[10] A. de Moor, H. Weigand, Towards a semiotic communications quality model, In Organizational Semiotics: Evolving a Science of Information System. ISBN 1-4020-7189-2. Kluwer, Boston, 2002. pp. 275–285.

[11] I. D´ıaz, A. Matteo, Refinamiento de Casos de Uso. III Workshop de las Segundas Jornadas Iberoamericanas de Ingenier´ıa de Requisitos y Ambientes de Software (IDEAS’99), Costa Rica, 1999.

[12] I. D´ıaz, A. Matteo, Te´cnicas para el Proceso de Ana´lisis. MSc Thesis in Computer Science, Faculty of Science, Venezuela Central University, June, 1999.

[13] I. D´ıaz, A. Matteo, Alternativas Gramaticales del Espan˜ol y la Especificacio´n de Casos de Uso. XXVII Conferencia Latinoamericana de Informa´tica CLEI’2001. Me´rida, Venezuela, 2001.

[14] I. D´ıaz, A. Matteo, Directrices para la Especificacio´n de Casos de Uso en el Idioma Espan˜ol. Acta Cient´ıfica Venezolana 53(2). Asociacio´n Venezolana para el Avance de la Ciencia. ISBN 001 5504. Caracas, Venezuela. December 2002, pp. 139–148.

[15] L. Go´mez, Grama´tica Dida´ctica del Espan˜ol. Ediciones SM. Madrid, Espan˜a. Enero 2002 (octava edicio´n).

[16] I. Jacobson, M. Christerson, P. Jonsson, G. O<sup>¨</sup> vergaard, Object-oriented software engineering, A use case driven approach, Addison-Wesley, 1992.

[17] I. Jacobson, G. Booch, J. Rumbaugh, The Unified Software Development Process, Addison-Wesley, 1999.

[18] C. Larman, Applying UML and Patterns, Prentice Hall, Upper Saddle River NJ, 1998.

[19] T.J. Larsen, J.D. Naumann, An experimental comparison of abstract and concrete representations in systems analysis, Information & Management 22, 1992, pp. 29–40.

[20] F. La´zaro, Curso de Lengua Espan˜ola. Ediciones Anaya, Madrid, 1979.

[21] A. Moreno, Entienda la Grama´tica Moderna. Ediciones Larousse, Me´xico, 1985.

[22] Omg Unified Modeling Language Specification, Version 1.5, March 2003, http://www.omg.org/uml.

[23] Rational Products Information Center. http://www.rational.- com/products.

[24] N.P. Vitalari, Structuring the requirements analysis process for information systems: a propositional viewpoint, in: W.W. Cotterman, J.A. Senn (Eds.), Challenges and Strategies for Research in Systems Developments, Wiley, New York, 1992.

![](/api/attachments/9CUYHD9U/fulltext/images/f7bd81c64e06933461e2f49563f9d2234312677e142c5f655f60618031ab3ae9.jpg)

Isabel D´ıaz is an aggregate professor in the Social and Economic Sciences Faculty of the Venezuela Central University. She obtained a MSc degree in Computer Science and Specialist degree in Information Systems from this University. Her research interests include requirements engineering, natural language processing, knowledge management, ontology engineering, information systems and soft-

ware automatic production. She is a leader researcher of the Socioeconomic Statistics Information Automated System (SAIDES) Project and she is member of the ISYS (Systems and Software Engineering) Research Center of the Faculty of Science, Venezuela Central University.

![](/api/attachments/9CUYHD9U/fulltext/images/ad2fc1f122520f5edc1adf3286efabb77f1b10926fbfcc43828f513298b9ef30.jpg)

Francisca Losavio is a full Professor in the School of Computer Science, Faculty of Science, Venezuela Central University. She received her PhD in Computer Science and the Cycle Doctor degree in Computer Science from the Paris-Sud University (Orsay, France). She also obtained a MSc degree in Computer Science from the Simo´ n Bol´ıvar University (Venezuela). Dr.

Losavio co-ordinates the Software Technology Laboratory (LaTecS) at the ISYS (Systems and Software Engineering) Research Center. She participates in European Community Research Projects. Her main research axes are software architecture, software quality and software development process.

![](/api/attachments/9CUYHD9U/fulltext/images/5a7b87a72c07efcec3f95214ef2097254c01acdd6310611e3148d1fe88489e7a.jpg)

Alfredo Matteo is a full Professor in the School of Computer Science, Faculty of Science, Venezuela Central University. He received his PhD in Computer Science from the Paul Sabatier University (Toulouse, France). He co-ordinates the TOOLS Laboratory of the ISYS (Systems and Software Engineering) Research Center. His research includes software engineering environments

and architectures, methodologies and standards for software development.

![](/api/attachments/9CUYHD9U/fulltext/images/4f24edfcad03894ca1d4bd5808e66c11d78c9cc63f2b0d53e9f235b15ab303c8.jpg)

Oscar Pastor is currently the Director of the Computation and Information Systems Department at the Valencia University of Technology (Spain). He is a full Professor in this University where received his PhD after a research stay in HP Labs, Bristol, UK. Author of over 100 research papers in conference proceedings, journals and books, received numerous research grants from public institutions and private industry. Research activities focus on web engineering, objectoriented conceptual modelling, requirements engineering, information systems and model-based software production. Dr. Pastor is the leader of the OO-Method Research Group undertaken by the Valencia University of Technology and CONSOFT S.A. that has originated an advanced Model Driven Development tool that produces a final software product starting from a Conceptual Schema where the system requirements are captured.
