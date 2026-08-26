---
otero_id: 17504
otero_key: "B9XX7JWW"
title: "Theoretical foundations for conceptual modelling in information systems development"
authors: "Yair Wand; David E. Monarchi; Jeffrey Parsons; Carson C. Woo"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00043-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Theoretical foundations for conceptual modelling in information systems development

Yair Wand $^{a,*}$ , David E. Monarchi $^{b}$ , Jeffrey Parsons $^{c}$ , Carson C. Woo $^{d}$

$^{a}$ Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, B.C., V6T 1Z2, Canada $^{b}$ University of Colorado, Campus Box 419, Boulder, CO 80309-0419, USA

$^{c}$ Faculty of Business Administration, Memorial University of Newfoundland, St. John's, Newfoundland, A1B 3X5, Canada $^{d}$ Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, B.C., V6T 1Z2, Canada

## Abstract

Conceptual modelling in information systems development is the creation of an enterprise model for the purpose of designing the information system. It is an important aspect of systems analysis. The value of a conceptual modelling language (CML) lies in its ability to capture the relevant knowledge about a domain. To determine which constructs should be included in a CML it would be beneficial to use some theoretical guidelines. However, this is usually not done. The purpose of this paper is to promote the idea that theories related to human knowledge can be used as foundations for conceptual modelling in systems development. We suggest the use of ontology, concept theory, and speech act theory. These approaches were chosen because: (1) they deal with important and different aspects relevant to conceptual modelling and (2) they have already been used in the context of systems analysis. For each approach we discuss: the rationale for its use, its principles, its application to conceptual modelling, and its limitations. We also demonstrate the concepts of the three approaches by analysing an example. The analysis also serves to show how each approach deals with different aspects of modelling.

Keywords: Conceptual modelling; Ontology; Concept theory; Speech act theory

## 1. Introduction

Modelling is an essential aspect of information systems development [[34], p. 35]. Indeed, an information system can be viewed as a representation, or a model, of another system (usually termed the real system) [8,24,59]. Modelling is especially important in the analysis stage of systems development when abstract models of the represented system and its organizational environment are created. Such models are termed conceptual models. A conceptual model should reflect knowledge about the application domain rather than about the implementation of the information system. Conceptual modelling has been defined as “an abstract model of the enterprise” [[10], p. 399], and as a formal description of “some aspects of the physical or social reality for the purpose of understanding and communicating” [[31], p. 51]. It has been proposed that there are four roles for conceptual models [25]: Provide a way for developers and users to communicate, increase analysts understanding, serve as the basis for design, and serve as documentation of the original requirements of the system for maintenance purposes. In a discussion of conceptual modelling, Mylopoulos [31] suggests that there are four types of knowledge related to information systems development: the subject world (i.e., the represented domain), the usage world (i.e., the environment within which the system is being used), the development world (i.e., the process and environment within which the system is developed), and the system world (i.e., the information system itself). In this paper, conceptual models refer to the first two. In other words, a conceptual model is an abstract description of an organizational setting (of which part is the represented domain and part is the usage environment).

The role of a conceptual model can also be described within the view of systems development consisting of analysis, design, and implementation. Analysis transforms a perceived real-world system into a conceptual model of that system. In the terms mentioned above, this is the creation of models of the subject and usage worlds. Design transforms the conceptual model of the subject world, into a model of the information system. In particular, the system interfaces are designed based on the usage model. Finally, implementation transforms the model of the information system into an implemented information system, which is a machine-executable representation (Fig. 1).

A conceptual model is constructed using a conceptual modelling language (CML). The language specification consists of fundamental modelling constructs and rules on how they can be combined into meaningful “statements” about the modelled domain. Typical constructs used in conceptual models include entities, relationships, activities, processes, and objects. Clearly, the semantics of the conceptual modelling language constructs determines the nature of the phenomena that can be described using it. A CML that is too restrictive, might not provide enough “modelling power” to capture relevant aspects of the modelled domain (more on this notion can be found in [60]). For example, in an article about conceptual modelling [31], Mylopoulos explains why a certain class of modelling languages is deficient in not being able to capture all the necessary information about some domains. A question of crucial importance to conceptual modelling is how does one go about defining an “appropriate” conceptual modelling language. The power of a modelling language lies in the semantics of its constructs. The semantics defines what individual constructs and their combinations “stand for” in the modelled domain. Therefore, the semantics of the constructs of a modelling language is of particular importance [14].

In this paper, we propose that conceptual modelling can be anchored in models of human knowledge. We identify three sources for such models: ontology, concept theory, and linguistics. Ontology is the branch of philosophy which deals with what is “out there” in the world, Hence, ontology can be used to define the concepts that should be represented by a modelling language, that is, the semantics of the language. Concept theory deals with how humans organize knowledge about the environment in terms of categories or concepts. Hence, concept theory can be used as a guidance for choosing meaningful constructs in conceptual models. Linguistics deals with how humans represent knowledge for the purpose of communication and how they communicate it. We refer to a specific area of linguistics – speech act theory. Speech act theory studies and classifies utterances according to speaker’s intention and possible effect on the receivers. Speech act theory can be used in conceptual modelling to capture the detailed dynamics of interactions among communicating agents (both humans and machines).

![](/api/attachments/B9XX7JWW/fulltext/images/511242328d9a1d429fd6d51f9d4dc6f845838ab66b6de4d53705cd17efe497f0.jpg)  
Fig. 1. The role of a conceptual model in systems development.

The purpose of the paper is not to provide a comprehensive analysis of all possible foundations for conceptual modelling. For example, we do not discuss the use of semiotics, which is the study of the use of symbols to convey knowledge [42,52]. Rather, our purpose is to demonstrate how such foundations can be beneficially used for conceptual modelling. The three domains we describe were chosen because: (1) they deal with important aspects of conceptual modelling, (2) each deals with aspects that the others do not deal with, and (3) each has already been used in the context of information systems modelling. The contribution of the paper lies in showing how these three models can be used together to provide a foundation for conceptual modelling where each covers aspects not dealt with by the others.

The paper proceeds as follows: the next three sections (2, 3 and 4) describe ontology, concepts theory, and speech act theory. For each, we discuss the rationale why it seems useful for conceptual modelling, present its principles, describe applications to conceptual modelling and provide some critique. In Section 5 we demonstrate the concepts of the three types of models by applying them to a standard example (the IFIP Working Conference Case [33], described in the Appendix)

and show that each of these models deals with aspects not dealt with by the others. Finally, Section 6 is a conclusion.

## 2. Ontology

## 2.1. Rationale

The fundamental assumption behind the use of ontology is that an information system represents a perceived real-world system. Accordingly, information system development can be viewed as a process of mapping users' perceptions into a "script" that is executable in some computing environment. The first step in this process is to create a well-defined model of the real system (as perceived). This is the conceptual model.

To create a conceptual model we need a set of constructs to model real-world systems. For this we turn to ontology which can be defined as “the branch of philosophy which deals with the order and structure of reality” [[3],p.198]. The ontological model we use is based on Bunge’s work [11,12]. We chose this work for several reasons. First, it is oriented towards systems. Second, it is intended to deal with a wide range of systems, from physical to social. Third, it is well formalized, both in defining the concepts and outlining the premises and in providing a consistent notation. Finally, it draws upon an extensive body of prior work related to ontology.

Since Bunge's ontology is intended to model systems, it can be applied to both the real-world system and to the information system representing it (which, once implemented, is also part of the world). Using the same set of concepts to model both systems can facilitate the mapping from the conceptual model to the design model of the system. Furthermore, using a well-formalized model for specification allows for automating parts of the analysis and design process [44].

## 2.2. Concepts and principles

In the following, the word “ontology” will refer specifically to Bunge’s ontology. According to Bunge, the world is made of things that possess properties. A property can be intrinsic to a thing or mutual to several things. For example, the height of a person is intrinsic to a person while being an employee is mutual to a person and a company.

Things can associate to form a composite thing. A composite thing must possess emergent properties - properties not possessed by any component. For example, the processing power of a computing system is an emergent property.

Things possess properties whether it is known to humans or not. In contrast, an attribute is a characteristic assigned to a thing by humans. Every property is representable by an attribute. For example, colour is an attribute representing the property of reflecting a certain electromagnetic wavelength. However, not every attribute has to represent a property.

A thing is modeled in terms of a functional schema which is a set of attribute functions, usually functions of time. The same functional schema may apply to many things. There may be different views of a thing, each represented by a different functional schema. Each view depends on the observer and may relate to only some of the properties.

The above fundamental concepts and premises are the basis for defining the notions of state, event, interaction, and system. Thus, in ontology these are derived concepts that have a precise meaning rather than being defined intuitively.

At a given time, the state of a thing from a particular view is the set of values of the functions of the functional schema defining that view.

Ontology postulates that every thing changes, and every change is a change of things, that is the change of properties of things. It follows that changes in the world are manifested as changes of states of things. A change of state is termed an event. An event is modelled as a triplet: < initial state, final state; transformation > where the transformation represents the mechanism that affects the change.

Both states and events are subject to constraints that are termed laws. Laws are also properties of things.

The notion of interaction is important for the definition of a system. Thing y acts-on thing x if the states x goes through are affected by the presence of y. Things x and y interact if at least one of them acts on the other. A system consists of interacting things which cannot be partitioned into non-interacting subsets. The composition of a system is the set of its components. The environment of the system is the set of things which interact with the system's components but which are not in the composition. The structure of the system is the set of all interactions involving its components (between components or between components and things in the environment). A subsystem is a system made of some of the components and part of the structure of another system.

A system can be viewed both as a thing and as an aggregate of things. Since a system is a composite thing, it possess emergent properties.

The dynamics of things (and systems) is described in terms of interactions and internal transformations. The following concepts are some additions to Bunge's original model. An external event is a change of state due to the action of other things. A stable state is a state that will change only with an external event. An unstable state is a state that will change without an external event. We assume that a thing in an unstable state will eventually reach a stable state. If a thing in a stable state undergoes an external event, it will change its state. If the resulting state is unstable, the thing will keep changing until it reaches a stable state. Hence the behaviour of a system can be analyzed with respect to a given set of external events termed the relevant event set. This set effectively defines the “interesting” behaviour of the system. A thing will be said to be well-behaved (predictable) if and only if for each event in the relevant event set that changes the state to unstable, the thing will reach exactly one stable state.

## 2.3. Applications to conceptual modelling

Three types of models related to systems analysis and design were developed based on the above ontology [59]. The representation model deals with the mapping between ontological constructs and information systems constructs. The state tracking model views an information system as an artifact that changes state to reflect the changes of state of the represented real system. The system model analyzes the structure and behaviour of a system as a whole in terms of the states and laws of its components. In the following we outline briefly the outcomes of the work most related to conceptual modelling. Most are consequences of the representation model.

Use of the ontological concepts in executable conceptual models

The ontological model described above was used as one of the sources for constructs in a recent proposal for an executable conceptual modelling language $[62]$ . The purpose of such a language is to enable rapid prototyping of a systems by using the conceptual model as a computer-executable definition of the prototype. Such a prototype can be used for validating the conceptual model with the user.

## Evaluation of modelling methods in systems analysis and design

An important question in evaluating a systems analysis method is its capability to model the application domain. We propose that this capability can be evaluated by examining the mapping between the ontological constructs and the constructs of the method [58]. This leads to the notion of ontological expressiveness [60].

The analysis is carried out by recognizing that two mappings are involved in conceptual modelling: a representation mapping from the application domain to the conceptual model, and an interpretation mapping from the conceptual model to a view of the application. For a system modelling technique to be useful, it should enable both mappings without loss of information. Various types of loss can occur, indicating deficiencies of the modelling technique. To demonstrate, assume that there exists an ontological construct for which there is no matching construct in the modelling technique. This situation can be termed construct deficiency. It indicates that the modelling technique may not be able to capture certain relevant aspects of an application domain.

## Interpretation of semantic data models

Semantic data models are used in systems analysis and database design. The most commonly used of these is the entity-relationship (ER) model $[16,54]$ . However, despite its popularity, the ER model relies on intuitive understanding of the concepts of entity, relationship and attribute. In practice, it is not always clear which of these constructs should be used to represent a given object in the application domain.

The ontological model was used to suggest precise meaning to these constructs, especially that of relationship [57]. In this analysis an entity is considered to be a representation of a thing, an entity type to be a representation of a functional schema, and a relationship to be a representation of a mutual property or interaction. The outcomes of the analysis include: rules for the use of entities, relationships and attributes; rules for modelling composite things; and rules for avoiding ambiguities and inconsistencies in ER models.

## Analysis of the object concept

The object-oriented approach evolved as a programming discipline. Recently, the approach has been adapted for modelling in systems analysis. There is a substantial difference between the two applications of the object concept. In programming, it is an implementation construct. In analysis, it is a representation construct.

Bunge's ontology was used to propose a model of objects as representation constructs [56]. In this model, an object is viewed as a representation of a thing. The model suggests that certain characteristics of object-oriented programming environments should not be adapted in object-oriented analysis. For example, the practice of considering classes as objects has no ontological support, and message passing appears to be an implementation metaphor rather than a fundamental modelling concept. The model also suggests certain characteristics that should be available in object-oriented analysis. For example, the model supports multi-parent classification structure and composite objects, and requires that composite objects possess emergent attributes or behaviour.

This model of objects was used as the basis for an object-oriented conceptual modelling approach [53]. In addition, it served to propose guidelines for object-oriented modelling [38,61].

## Analysis of formal specifications

The ontological constructs can be used directly to create a conceptual model of an application. The modelling constructs used would be things, states (defined in terms of state variables), laws (governing states and state transitions), and external events to which the system has to respond.

Since the concepts are well-formalized, such specifications may lend themselves to automated analysis. Two types of automated analyses were applied to ontologically-based specifications. First, notions of consistency and completeness of the dynamic aspects of specifications were developed [41]. Incompleteness means the response of the system to an external event is not completely specified. Inconsistency means the transition laws lead to more than one stable state from an unstable state.

Second, an automated method for generating a system decomposition from the specifications was developed [40]. This method was based on the notion that subsystems in a good decomposition should have a well-defined response to each external event. The decompositions generated agreed with system design done independently using other methods. Comparing the generated decompositions to the user view of the system can indicate information missing in the specifications.

## 2.4. Limitations and criticisms

There are three main criticisms of the ontological approach. First, there is no “generally accepted” ontology. A different ontology may employ different concepts and postulates and might, therefore, lead to different outcomes. This suggests that the choice of modelling constructs may be arbitrary. Despite this, we believe that it is better to have a well-defined set of underlying concepts and premises than to have none. In the final analysis, it is the usefulness of the outcomes that determines whether the model is the “right” one.

A second criticism is that ontological models seem to assume an “objective reality” while the world is only known through human perceptions. However, consider a group of individuals with shared beliefs about what is “out there.” For the members of such a group, it might not matter whether the things they believe exist are really “out there.” Thus, the objective reality can be replaced by an “inter-subjective” reality. Even in such an inter-subjective reality there are assumptions about what can exist, namely, an ontology.

The third criticism is that the specific ontological model used (Bunge's model) does not deal with the organizational and behavioral aspects of information systems. Nevertheless, we believe that this ontological model is still useful for three reasons. First, the need for a formal description of the application is independent of organizational and behavioral issues. Second, the conceptual model defines what is “out there” independent of the justification and use of the information system. Third, Bunge's model permits user views through the notions of attribute and functional schema.

## 3. Classification theory

## 3.1. Rationale

In conceptual modelling, there is no “direct access” to reality. Rather models are constructed based on human perceptions of reality, or knowledge about the domain being modelled. In this paper, we informally define knowledge as the cognitive representation of things in reality. Things may be tangible or intangible, and are represented by their properties and behaviour. The analysis which follows is based on two premises. First, conceptual modelling is a process of extracting and representing knowledge. Second, conceptual modelling constructs should reflect what is being modelled (rather than, for example, the implementation environment). It follows from these assumptions that theories of how knowledge is organized are an appropriate source of constructs for conceptual modelling.

The ability to effectively and efficiently store and retrieve knowledge about daily experiences is crucial to human survival and adaptation. Cognitive science has offered a number of theories and models of knowledge organization and retrieval (e.g., [2,9,43,51]). These theories recognize classification as a fundamental mechanism for organizing knowledge. According to Lakoff [[26] p. 6]: "Without the ability to categorize, we could not function at all, either in the physical world or in our social and intellectual lives. An understanding of how we categorize is central to any understanding of how we think and how we function...."

Classification enables us to group similar things and separate dissimilar things. Classification theory deals with the nature of categories or concepts, and with why and how humans organize knowledge about individual things by forming concepts and classifying experiences [51]. To the extent that information systems collect, store, maintain, and disseminate knowledge about physical and social worlds, an understanding of classification is of importance to effective conceptual modelling.

## 3.2. Concepts and principles

Several theories of classification have been proposed which differ in important ways $[26,51]$ . For example, the classical view holds that a class is a well defined set of properties, and that membership in a class is all-or-none, while prototype and exemplar views relax this assumption to allow classes having less clearly defined boundaries (for a detailed discussion of the theories, see $[51]$ or $[29]$ ). However, each of these theories holds that classes should be effective in managing the complexity of human experience with things in the world. This means that classes are not arbitrary collections of properties or instances. The formation of classes appears to be governed by two functions they support in organizing knowledge: cognitive economy and inference $[45,50]$ .

Cognitive economy means that identifying several instances as being the same in some respects offers economy of representation. One class is distinguished from another when its instances possess meaningful differences [[45] p. 29], where meaningfulness can only be evaluated with respect to some use of knowledge. Since what is meaningful may differ from person to person (or for a single person over time), this suggests that there can be no single “best” set of classes for modelling a domain [26].

Inference is the ability to draw conclusions about unobserved properties of instances by classifying them based on an observed subset of properties. Since a class abstracts the sameness of its instances, there is a “high correlational structure” [[45] p. 29] between the properties of these instances.

Classification theory deals with the role of categories in organizing knowledge about things in the world. Under the two assumptions given above, classification theory may have implications for both the constructs used in modelling, and for the activity of creating models.

## 3.3. Applications to conceptual modelling

Guidelines for choosing classes in conceptual modelling

According to concept theory a class is defined in terms of a set of properties. It is important that a class is not an arbitrary set. It should be noted that the same principle is used in Bunge's ontology. Thus, both in ontology and in concept theory a class is an intensional, not an extensional, concept. In accordance with the cognitive foundation, there are constraints on the choice of classes (in terms of sets of properties) when modelling a domain. The notion of class structure is defined, imposing necessary conditions for a set of classes to constitute an acceptable model of a domain [39]. A class structure is a set of relevant properties satisfying four conditions that support cognitive economy and inference:

\- each class must be able to have instances,

\- each class must contain every property common to all its instances,

\- every known property of an object must be included in the definition of at least one class in the class structure, and

\- no class in a class structure is defined as the union of the properties of any other classes.

The first two conditions restrict the classes that may possibly be defined. The remaining conditions restrict which classes can coexist with others. In particular, the last condition implies that a class cannot be formed just as an intersection of the membership of other classes.

An important consequence of these conditions is that the model permits more than one class structure to be defined over the same domain of objects and properties [39]. This calls into question a common (and often implicit) assumption in conceptual modelling methods (e.g., data and object models) that an early step in modelling is to identify the set of classes for an application (e.g., [16,17,22,54]). For example, identifying entity types in entity-relationship modelling effectively imposes a single classification scheme. In contrast, concept theory suggests that instances and properties are more fundamental than are classes. A practical consequence for modelling is that the modeller should not attempt to impose a single set of classes on a domain. Rather, it should be possible for different users to be able to identify different classes over the same domain.

Concept theory can be used to analyze object-oriented concepts [38]. Several approaches to object-oriented systems analysis (OOA) have claimed to offer modelling constructs that reflect the way humans organize knowledge [17,27,46]. The principles outlined above have been used to evaluate several OOA methods in terms of the degree to which they support constructs of classification theory [36]. This evaluation shows that, while various models support cognitive constructs to a limited degree, none offers any theory-based guidance for choosing classes.

## Implications to translation from a conceptual model to implementation

A main issue in systems development is the “translation” from a conceptual model to an implementation. Accordingly, the model described here may have implications for implementation technologies. In particular, relational databases distinguish between base relations and views, suggesting that the former are more “fundamental” than the latter (e.g., [28]). Object-oriented databases similarly focus on storing data according to a fixed set of classes. An implementation which supports coexistence of multiple classifications should not make this distinction.

## A conceptual model based on classification theory

One application of classification theory has been the development of a conceptual IS meta-model called MIMIC [35,37]. The model consists of a set of formally defined constructs for representing knowledge about classes and instances. Two primitive elements - object and property - provide the basic representation of knowledge about instances, and are used to define the notion of a class.

Objects represent instances of concepts. Three kinds of properties are defined: structural properties describe the form of objects, relational properties describe associations with other objects, and behavioral properties describe possible changes of state (in terms of changes to structural and relational properties). A class is an abstraction defined in terms of a set of properties which are the same for all instances (members) of the class.

## 3.4. Limitations and criticisms

Since the application of classification theory to conceptual modelling is a new area of research, the long-term contribution of this work is uncertain. It remains to be seen whether a sound and useful methodology can be developed based on concept theory, or whether a viable data model based on instances and properties can be implemented.

Another potential concern in using classification theory to explore problems in conceptual modelling involves “which theory of concepts to use.” As mentioned, at least three theories exist. The research summarized here is based on categories with well-defined boundaries and binary membership. Experiments have shown limitations of this view as a general theory of concepts $[26,51]$ . Hence, it may be necessary to consider conceptual models based on “prototype” or “exemplar” views before a final judgment on the usefulness of classification theory in conceptual modelling can be made.

A final potential criticism of classification theory is that it ignores some aspects of cognition that may be relevant to IS development, such as beliefs and goals of those involved in the process. While this statement is true, it is not a relevant criticism in the context of conceptual modelling, since constructs such as beliefs and goals are generally beyond the scope of conceptual modelling.

## 4. Speech act theory

## 4.1. Rationale

Many activities in information systems can be considered interaction between “agents” that might be humans, computerized systems or machines. At the simplest level, a procedure calling another procedure can be viewed as an interaction between different units. At a more abstract level, we can view a system model (e.g., a data flow diagram) as a model for describing how different units (i.e., processes) interact with each other (i.e., by exchanging data flows). Interactions are not limited to units within a system. For example, electronic mail messaging is an interaction between one sender and one or more receivers, possibly in totally distinct organizations. This section describes how speech act theory can be used to model interactions.

In general, there are two problems in modelling interactions: the large number of possible actions and the lack of a sound method for identifying all the types of interactions needed to model a system. Even after a set of action types has been identified, it still may be difficult to understand how they interrelate (that is, are they sequenced in a particular way).

Speech act theory deals with classification of communicative acts according to their intention and possible effects. We propose that speech act theory can be used to resolve the above difficulties by providing classification of actions and suggesting the types of actions that might be present and their interrelationships. Moreover, since speech act theory is anchored in language use, the classification it proposes reflects the types of systems events or interactions that can be described in the language we know. Hence, conceptual models constructed using speech act theory will reflect the way a system can be described with the spoken language. Conversely, if we can perform certain actions in an information system, then we should be able to describe the actions using the spoken language and represent them in a conceptual model. Since speech act theory provides a relatively small number of classifications for the performative (namely, action-describing) aspects of language, it seems a good candidate for modelling interactions.

## 4.2. Principles

Linguists believe in a close relationship between speaking and acting [5]. For example, if a person says he will have lunch at 12 noon (his utterance), then around 12 noon, he will be eating his lunch (his action). The term “speech act” refers to the effects of an utterance on the addressee. The speech act “I am going to have lunch at 12 noon” in effect commits the speaker to eat lunch at 12 noon. The speech act “please close the door” motivates the addressee to perform the action of closing the door. Because actions are difficult to specify, linguists focus instead on the speech acts themselves. Linguists also believe that speech act verbs can be classified into a relatively small number of categories. To illustrate the principles underlying speech act theory, we shall briefly describe two approaches to speech act classification: top-down and bottom-up.

In the top-down approach, categories of speech acts are suggested based on some general observations of communicative acts and their possible effects. Of the top-down approaches, Searle's [47–49] speech act classification is the most developed and widely used one. Searle noticed that a speech act describes a correspondence between the words and the state of the world. For example, the speech act “close the door” makes the world fit the words (i.e., the speaker uses words to get the addressee to change the state of the world). By enumerating all possible directions of fits between words and world, Searle constructed the following speech act classification:

(1) assertives: describe the state of affairs (i.e., the speaker selects words to fit the world)

(2) directives: request the addressee to do something (i.e., the speaker gets the addressee to change the world to fit the words)

(3) commissives: promise to do something (i.e., the speaker attempts to change the world to fit the words)

(4) declaratives: bring about change by virtue of the propositional content of the utterance (i.e., a fit is effected between the world and the words and vice versa)

(5) expressives: reveal the psychological state of affairs (i.e., there does not have to be a fit between the world and the words)

Searle's classification approach is top-down because it was formulated without first considering all possible speech act verbs.

Searle also recognized different degrees of fit (known as illocutionary force) between the speech act and the environment in which it is used. For example, both speech acts “order” and “politely request” are directives, but “order” has a higher degree of illocutionary force than “politely request”. Illocutionary force, therefore, adds an additional dimension to Searle’s fivefold speech act classification.

In the bottom-up approach, speech act categories are formed by grouping verbs in the spoken language into categories, according to their meaning and possible effects. We are aware of only one bottom-up approach to speech act classification, that of Ballmer and Brennenstuhl [6]. They approach the classification task by considering all speech act verbs from a German verb dictionary. Speech act verbs taken from the dictionary are grouped around semantic clusters which are formed by using the meaning of verbs. Some examples of semantic clusters are: expressing emotion, influencing others, and verbal struggle. Verbs in each semantic cluster that are similar in meaning are grouped into categories. Categories in a semantic cluster exhibit natural order based on temporal relations and degree of effectiveness. For example, “dissent” is temporally ordered after “make claim”, and “threaten” is more effective than “warn”. These categories are grouped together with the ordering information to form a model. There are 24 models and 600 categories in Ballmer and Brennenstuhl’s classification.

## 4.3. Applications

Speech act theory has been used by different researchers to model different aspects of interactions. To demonstrate the use of speech act theory, we briefly discuss three application areas. For each area, we provide one or two examples.

## Speech act based conceptual models

The SAMPO systems analysis methodology proposed by Auramaki et al. [4] employs speech act categories to specify the semantics of each unit of information passing from one process to another in terms of the intention of the interaction. The basic idea behind SAMPO is Habermas' theory of social action [21] which uses speech act theory to distinguish between social and nonsocial communication. Searle's speech act categories and his illocutionary force concept [49] are also used in SAMPO to specify the information flow semantics. According to [4], SAMPO provided insights into observing and understanding information flows. However, the authors encountered several problems due to the ambiguity of identifying speech act categories in certain situations and the difficulty of interpreting the results specified by SAMPO. We believe that these problems can be overcome if an appropriate speech act theory is used (see the discussion in the “limitations and criticisms” section).

Another proposal of a conceptual modelling approach based on speech act theory is DEMO described in [18]. DEMO is intended to model open active systems. A fundamental principle of the approach is a distinction between subjects which are the active elements of the system and objects which are the elements acted upon. The communicative acts performed in the system are categorized into performative acts that are intended to invoke actions and informative acts that are only intended to transmit information. Based on this idea, a set of modelling constructs and a graphic modelling technique (termed ABC-Net) are used to represent organizational activities.

## Modelling communications

Speech act categories can be used to model communication activities. One example is the Coordinator system [19]. Coordinator structures and provides semantics for the content of an electronic mail message using Searle's speech act classification. The type of speech act implies what the receiver is expected to do. For instance, a directive message means the receiver needs to do something, while an assertive message is merely a piece of information. Note that this is an improvement over current electronic mail systems because they provide only structures for the header information (e.g., "To", "From", and "Subject" fields); the contents of messages are unstructured. With the availability of message semantics, the system also provides appropriate user assistance (e.g., remind the user if a certain requested task has not been performed yet). Carasik and Grantham [13] conducted a trial of using the Coordinator system. Their findings indicate that users experience difficulties in structuring what they want to communicate using the speech act categories provided in Coordinator. As was true with the SAMPO methodology, we believe this was caused by the inappropriate use of speech act classification rather than the speech act theory itself.

A second example involves electronic data interchange (EDI) protocols. SANP [64], a negotiation protocol, was designed using the Ballmer and Brennenstuhl struggle model of speech act classification. A study reported in [15] solicited feedback from two pairs of users on how well the protocol provided the functionality necessary for negotiation. Although some limitations of the protocol were identified, they were not insurmountable. Users, in general, did not experience the same difficulties with SANP as those that used the Coordinator.

## Application to information gathering methods

Speech act theory can also be used to evaluate information (and knowledge) gathering methods employed in systems analysis (and in knowledge acquisition). The idea is to study the performative (action-invoking) features of different methods by mapping them into different speech act categories or models. This enables study of experience-based information and knowledge gathering methods using speech act theory. An example of such an application is the use of Ballmer and Brennenstuhl's classification to analyze and compare two knowledge acquisition methods: the multidimensional scaling method and the recall method [23]. A similar approach can be applied to requirement analysis in conceptual modelling.

## 4.4. Limitations and criticisms

The use of speech act theory in information systems has its critics. A major criticism is the difficulty users experience in structuring their communication using speech act categories $[13]$ . There are two possible explanations for this finding: (1) other foundations are needed to fit the use of speech acts to specific situations, and (2) designers used the wrong speech act classification system for the domain which they were trying to model. We now briefly discuss these two points.

Speech act theory tries to capture activities at a very low and detailed level. It lacks a comprehensive overall picture of how actions fit and relate to each other. To model interactions properly, a higher level foundation must supplement speech act theory. For example, in addition to Ballmer and Brennenstuhl's Struggle model, work in sociology (e.g., potential strategies of and structuring of negotiation and/or arguments) may be useful in developing a negotiation protocol [64].

Although Searle's speech act theory is widely used, it has two major limitations. First, it focuses on unidirectional speech act performance and, hence, cannot properly capture speech act performances occurring in sequence. Second, the speech act concept is restricted to spoken discourse. Linguists (e.g., Ballmer and Brennenstuhl [6]) contend it is very difficult to study general human communication by imposing this restriction. Therefore, Searle's work is useful for modelling only unidirectional spoken discourse.

By considering all (German) speech act verbs, Ballmer and Brennenstuhl's speech act classification does not have the same domain limitations as Searle's work. However, it has two other major limitations. First, the classification is ambiguous. For example, it is unclear why a specific speech act verb is classified under several categories even though one category would seem more appropriate [55]. Second, Ballmer and Brennenstuhl's English version of the speech act classification is a direct translation of the German version. This is problematic because there are English speech act verbs that do not have German equivalents and vice versa. Nevertheless, we believe that Ballmer and Brennenstuhl's speech act classification is still useful, provided we can supplement it with additional theory or empirical work to adjust the shortcomings.

## 5. An example

The theoretical foundations discussed above were not intended to be used directly as conceptual modelling approaches. However, it is useful to demonstrate the concepts of these foundations by applying them to an example. In particular, the example can serve to show that the three proposed foundations deal with different aspects of the modelled domain.

The example we use is a standard case used in comparative analysis of information systems methodologies. This is the IFIP Working Conference Case ([33], pp. 8-9] see the Appendix).

## 5.1. The use of ontology $^{1}$

## Things

The ontological view is based on perceiving the world as made of individual things. However, ontology recognizes that rather than considering individual entities, people view the world in terms of model things. The specific model suggested is that of a functional schema which is a set of attribute functions used to describe a certain set of things. That is, a functional schema can be viewed as defining a type of things. Note, the same thing can be described by more than one functional schema.

Some of the types of things we identify in the IFIP Conference example are: Program committee, Organizing Committee, people who might be involved, and papers. Note that we do not yet make a distinction between a committee member, invited person, authors etc. For now, they are all instances of the same type of things – person.

## Properties and attributes

According to ontology, things possess properties whether we are aware of them or not. People are only aware of properties in terms of attributes – characteristics humans assign to things. All properties are, in principle, representable as attributes, but not all of them will be represented. Moreover, it is not necessary that an attribute represents a property.

According to Bunge's ontology, properties do not have to be fixed. A thing can “acquire” or “lose” properties and still be the same thing. This implies that the same thing can be described by a different functional schema as its properties are changing. For example, a submitted paper may become an accepted paper, and an author can become a participant.

Since we only know about properties as attributes, in the analysis of the example we discuss both properties and attributes.

## Attributes of a person

Address - an attribute that reflects a mutual property of a person and a location. Note, location is not included as a thing of interest.

IFIP Working Group membership - an attribute that reflects a mutual property of a person and a working group.

Height - an attribute that reflects the (intrinsic) property height. This property is not relevant in our example and therefore will not be represented as an attribute in any relevant functional schema.

Nationality – an attribute that reflects a mutual property. It might be relevant (e.g., if the committee wants to encourage multinational participation).

Name - this is an attribute that does not reflect any property of the individual.

Attributes of a paper

Title - an attribute that may reflect the contents of the paper (which is a property of the paper).

Author names - an attribute reflecting a mutual property of a paper and an author.

Quality - this attribute may or may not reflect real properties of a paper. Note, in this particular case, it is clear that the attribute has no meaning without a human observer.

Type (indicating “theory” or “practice”) – an attribute that reflects a property (contents) and subjective judgement by an observer.

## Association of things

Two examples for a composite thing are: Program committee, organizing committee. It is interesting to show in these cases the distinction between inherited property and emergent property.

Example for an inherited property: affiliation of committee chair. This property might be of interest, but it is not an emergent property of the committee.

Example for an emergent property: ability to decide on acceptance of papers. Note, while each member can make a recommendation on acceptance or rejection of a paper, it is the whole committee that has the power to accept or reject it.

## Functional schema

Consider a person as a program committee member. A possible functional schema is:

Name, Address, Affiliation, Areas of expertise

Consider now a person as an author of a submitted paper. A likely functional schema is:

Name, Address, Affiliation, Title of submitted paper (this reflects a mutual property of an author and a paper).

Consider a paper as a submitted paper:

Title, Keywords, Author(s) names, Date received

consider now a paper as an accepted paper:

Title, Author(s) names, Category (research, application,...), Session assignment, Version (original, revised, proof-edited)

## Laws

Laws define the states that can occur. Usually they are described as constraints on states (and events). Examples for laws are:

A person who was not invited cannot be registered.

A paper that was not accepted cannot be assigned to a session.

Note, this formulation indicates states that cannot occur, and as well, changes (events) that should not happen.

## Interaction

Interaction is the ability of a thing to affect state changes of another thing. Two examples are:

(1) A reviewer recommends acceptance of a paper. This indicates an interaction between the reviewer and the paper.

(2) The program committee has decided to accept a paper. If a paper was accepted, the author will have to present it. This is an interaction between the program committee and the author.

## A system

The whole conference organization can be viewed as a system. To show that a certain collection of things is a system, one has to show that there are interactions between the subsets in every bi-partition of the set of components. While we have not indicated which things are in the system and which are in the environment of the system, the following (types of) things are clearly in the system:

Participants, papers, committees, committee members.

In order to examine this system, one has to identify the specific instances of each type of things. However, the analysis may be carried by just considering generic things. For example, each participant interacts with the organizing committee (by receiving an invitation and by registering). Each paper “interacts” with the program committee. The paper creates work for the committee, the committee determines the fate of the paper. Also, there is interaction between the two committees. The organizing committee appoints the program committee. The program committee, in turn, affects the activities of the organizing committee.

## Events, stable and unstable states

Events are any changes happening to the states of things. Some typical events for the conference case are:

(1) A paper is received

(2) A paper is accepted

(3) A person registers

The first and third events are external to the conference organization; the second event is internal.

Consider the event “a paper is received.” From an ontological point of view, this is not when the paper was created (or completed). However, in information systems design, that is when the paper record would be added to the database (this is typically viewed as “creation” of the paper in the database).

When a paper is received, certain actions must be taken by the program committee to process the paper. This implies that just after receiving the paper the state of the program committee becomes unstable. The new stable state will be one where the paper has been sent to reviewers.

## What do we learn from this analysis?

The ontological model was not suggested as a conceptual model. However, the example demonstrates how ontology can guide us in identifying the information that has to be known, and how the information about a domain can be organized. Indeed, as suggested above (section 2), one of the uses of ontology is to analyze the expressive power of systems analysis methods, namely, their capacity to capture information about a modelled domain.

## 5.2. Concept theory

The ontological view provides a set of modelling constructs to describe the statics and dynamics of a domain. In particular, in terms of relevant things, their states, and the relevant state changes (whether external or internal). However, in our discussion above, we did not usually refer to individual things but rather to types of things. For example, we did not enumerate individual people. Instead, we referred to: committee member, invited person, author, reviewer, and participant. Indeed, the same person could play more than one role. In each role, we may view the person differently, according to a different concept. Ontology does not provide us with clues on how to organize the information about things in terms of categories or concepts to be used. This is the domain of Concept Theory. In particular, Concept Theory can be used to analyze whether a certain choice of categories (classes) provides for cognitive economy and inference. Cognitive economy implies that a relatively small number of concepts be used to capture knowledge about a domain. Inference indicates the ability to derive the relevant information from the concepts. As explained above (section 3), cognitive economy and inference impose several requirements on the choice of classes. We now discuss these requirements in the context of the IFIP Conference example.

(1) Each class must be able to have instances:

The concepts used in our analysis above include Program Committee, Organizing Committee, invited person, author, and paper. Clearly, all those are necessary for the conference to take place. Thus, there is no point analysing a conference without assuming that all these concepts can have instances. To demonstrate a concept that might be mentioned in the context of travelling to a conference, but might not be needed, consider a tour guide. There is nothing in the description of the case that indicates there will be an instance of this concept. Hence, it should not be included.

(2) Each class must contain every property common to all its instances.

Assume, for example, that we found that every author has an affiliation (that is, nobody who is not affiliated with a university or another organization ever submits a paper). Moreover, suppose it is important for the organizing committee to know the distribution of submissions by type of organization (e.g., university/industry/government). Then, affiliation is a relevant property, and it should be included in the definition of the author concept.

(3) Every known property must be included in the definition of at least one class.

Assume we found that the property “subject area” of a paper is important for the purpose of organizing the conference. If this property is not included in any defined concept, this might indicate that an existing concept is not well defined (not all properties of the instances are used in the concept definition). Alternatively, this might indicate that a new concept has to be created. Assume subject area can only be judged after the paper has been reviewed. It might make sense to amend the definition of the accepted paper concept to include subject area. However, if subject area cannot be identified for every accepted paper, it cannot be a property of the accepted paper class. We might then consider the new concept classified paper that can be useful in assigning papers to sessions.

(4) No class is defined just as the union of two existing classes.

To demonstrate, assume that there is a suggestion to include the class: “authors who are IFIP members.” If there is no additional information about the instances that belong to both classes, than there is no reason to define this new class. Assume, however, that authors of accepted papers who are IFIP members are eligible for special reduction in conference fee. Then a new class can be created, where the members possess all attributes of author and of an IFIP member, and some additional attributes related to fee discount.

## What do we learn from this analysis?

As shown, Concept Theory can provide guidelines to examine the choice of concepts used to describe a domain. In particular, it can indicate the need to add or modify concepts, and help to identify redundant concepts.

## 5.3. Speech act theory

While the ontological view provides us with constructs to model the dynamics of a domain, it does not deal with the meaning of this dynamics. This meaning is important in order to guide the identification of relevant events, and for understanding the activities in the system. Speech act theory can be used to analyze the activities in the modelled domain.

Note, Winograd and Flores [[63] p. 76] make a clear distinction between two roles of the use of language. One is to transmit information (about the states of the world). The other is to evoke communicative actions that may affect the state of the world. Speech act theory deals with the second role only. Knowing the type of speech act implies knowledge of its possible effects as a message, rather than the exact meaning of its contents.

To demonstrate the possible use of speech act theory, we analyze some of the actions taking place in the IFIP Conference example. To do this, we use the five types of speech acts of Searle's classification: Assertives, Directives, Commissives, Expressives and Declarative. We will show how knowledge of the type of speech act can support modelling a domain.

Consider, first, that an author has submitted a paper for review. The act of submission is viewed by the committee as a commitment of the author to present the paper if it is accepted. Thus, when the committee accepts the paper, they can assume that the paper can be assigned to a session and act accordingly.

Next consider that a paper is sent by the program committee to a reviewer. This is a directive, and therefore implies an expectation by the committee that a review will be returned after some time. If this were to be described ontologically, there will be an external event that indicates a review has been received from a reviewer.

When a reviewer sends a review, this is an assertive act. From the reviewer's point of view, no further action is necessary, but the committee is expected to update its information (and possibly take an action).

Consider now a notification by the program committee to an author that the paper has been accepted. If this is interpreted as an declarative, this means a change of state of affairs, and practically be manifested as a change of state of the paper and the conference at large. On the other hand, this notification could be viewed as a directive to the author to send a camera-ready copy. In this case, the state of affairs should be also changed such that there will happen a follow-up on submission of final versions.

## What do we learn from this analysis?

These examples demonstrate that identification of the specific speech act can indicate the nature of events occurring in a system, as well as the possibility of future events. In contrast, while the ontological constructs can model these possibilities, ontology does not provide the tools to identify and analyze them.

## 5.4. Comparison of the approaches

Ontology can be defined as: “That branch of philosophy which deals with the order and structure of reality.” Since ontology defines what is “out there,” ontological concepts can be used to define the formal semantics that underlies conceptual modelling. However, ontology does not provide guidance on identifying or organizing the important concepts in a certain domain or on analysing the dynamics of the domain. The answers to this may be found in the other two areas. In particular: (1) the notions of cognitive economy and inference can be used to provide guidelines on the choice of an appropriate set of concepts to describe a domain, and: (2) The use of speech act theory can provide guidelines for analysing the dynamics of the modelled domain.

It is important to note that speech act theory does not deal with the informative contents of communications, rather than with the possible effects of communicative acts on the state of affairs. Thus, speech act theory in itself does not provide constructs for modelling domains. In contrast, concept theory refers to the way knowledge may be organized by human beings. However, concept theory in itself does not provide a complete set of constructs for modelling a domain. To do this, one has to assume an ontology.

We conclude that the three approaches are complementary, and cover different aspects of modelling the world. In combination, they can be used to provide a theoretical basis for conceptual modelling.

## 6. Summary

There is a general trend in information systems development methods towards modelling approaches that are implementation-independent. This has manifested itself via the growing recognition of the importance of conceptual modelling [30]. Conceptual models are recognized as an important tool in systems analysis, especially to promote understanding and communication with users. However, the question of how to define a “good” conceptual modelling language is still unresolved.

The most important characteristic of a conceptual model approach is its modelling power, namely its ability to capture knowledge about the relevant domain. This modelling power depends on the semantics of the conceptual modelling language (CML).

In this paper, we proposed that it would be beneficial to decide what constructs should be included in a conceptual modelling language based on theoretical foundations. Given that conceptual models represent knowledge about a domain, we suggested that such foundations can be sought in theories about human knowledge. Specifically, we suggested the use of ontology, concept theory, and speech act theory. We showed how each approach can be used in the context of conceptual modelling. Ontology can provide a generalized (that is, non domain-dependent) semantics for conceptual modelling languages. Concept theory can provide guidance for determining the specific classes (or types) used when modelling a domain. Speech act theory can be used to model the details of interactions among intelligent agents. Each of these approaches deals with modelling aspects not covered by the others. Since these approaches can be well-formalized, using them as the basis for defining system specifications can enable automated analysis. Hence, an important potential application of theoretically-based approaches can be for constructing CASE tools.

There are two types of modelling approaches used in systems development that are closely related to conceptual modelling: semantic data models and knowledge representation. Semantic data models can be viewed as the ancestors of conceptual models. However, they were originally proposed for the purpose of designing databases (rather than the complete system). Knowledge representation techniques usually reflect reasoning about system behaviour [[31] p. 51] and are usually developed for the purpose of being incorporated into an executable system [7]. To the extent that ontological models are used in artificial intelligence work (e.g. [1,20]) they usually refer to concepts necessary to describe specific types of domains. For example, Neches et al. [32] claim: “An ontology defines the basic terms and relations comprising the vocabulary of a topic area.” Thus, these two approaches have more specific objectives than just creating an abstract model of a domain. However, we believe that the models discussed above can also be used as theoretical foundations for these two approaches.

Finally, we note that the approaches we discussed are not the only possible ones, neither are they necessarily the best ones. Indeed, the study of theoretically-based conceptual models might prove to be very fruitful and beneficial for advancing techniques for systems development.

## Acknowledgements

This paper is based in part on a panel presentation at WITS 92. The authors wish to thank Terry Barron, University of Rochester, for participating in the panel. We also like to thank the anonymous referees for constructive suggestions on earlier drafts of this paper.

This work was supported in part by research grants from the Social Sciences and Humanities Research Council of Canada to Jeffrey Parsons and to Yair Wand.

## Appendix A

The IFIP working conference case

(Adapted from Olle, 1982, pp. 8-9)

## Background

An IFIP Working Conference is an international conference centred on a topic of specific interest to one or more IFIP Working Groups. The conference is not open to everyone and participation is by invitation only. Two objectives of the conference organizers are to ensure that members of the involved Working Group(s) and Technical Committee(s) are invited and that attendance is sufficient for financial break-even without exceeding the capacity of the facilities available.

Two committees are involved in organizing an IFIP Working Conference: a Program Committee and an Organizing Committee. The Program Committee deals with the technical content of the conference and an Organizing Committee with financial and local arrangements, and with invitations and publicity. These committees have to work together closely and have a need for common information.

The objectives of the information system is to support the activities of both committees. Some of the information is common to both.

Activities to be supported by the information system

Program committee:

(1) Preparing a mailing list for sending the call for papers.

(2) Registering letters of intent for participation.

(3) Registering the submitted papers.

(4) Sending the papers to reviewers.

(5) Collecting reviewers reports and deciding on which papers to accept.

(6) Grouping accepted papers into sessions and assigning sessions chairs.
Organizing committee:

(1) Preparing a list of people to invite.

(2) Issuing priority invitations to National Representatives and to members of related Working Groups.

(3) Ensuring all authors of each submitted paper receive an invitation.

(4) Registering acceptance of invitations and generating a final list of participants.

Note: An effort is made to avoid sending duplicate invitations to any individual.

## References

[1] J.H. Alexander, M.J. Freiling, S.J. Shulman, S. Rehfuss, and S.L. Messick, Ontological analysis: an ongoing experiment, Knowledge-Based Systems, Vol. 2, 1988, 25–37.

[2] J. Anderson, The Architecture of Cognition, Cambridge. MA: Harvard University Press, 1983.

[3] P.A. Angeles, Dictionary of Philosophy, Harper Collins Publishers, New York, NY, 1981.

[4] E. Auramaki, E. Lehtinen, and K. Lyytinen, A Speech-Act-Based Office Modelling Approach, ACM Transactions on Office Information Systems, Vol. 6, No. 2, April 1988, 126–152.

[5] J.L. Austin, How To Do Things With Words, 2nd ed., J.O. Urmson and M. Sbisa (eds.), Cambridge, MA: Harvard University Press, 1962.

[6] Th. Ballmer, and W. Brennenstuhl, Speech Act Classification, New York, NY: Springer-Verlag, 1981.

[7] A. Borgida, Knowledge Representation and Semantic Data Modelling: Similarities and Differences, Proceedings of the 9th Entity-Relationship Conference, Geneva, 1990.

[8] A. Borgida, S. Greenspan, and J. Mylopoulos, Knowledge Representation as the Basis for Requirements Specifications, IEEE Computer, Vol. 18, No. 4, April 1985, 82–90.

[9] B. Brachman, and J. Schmolze, An Overview of the KL-ONE Knowledge Representation System, Cognitive Science, Vol. 9, 1985, 171–215.

[10] J.A. Bubenko, Jr., Information Modelling in the Context of Systems Development, Information Processing 1980, proceedings of IFIP Congress, North Holland, 395–411.

[11] M. Bunge, Treatise on Basic Philosophy (Volume 3): Ontology I, The Furniture of the World, D. Reidel Pub. Co.: Boston, 1977.

[12] M. Bunge, Treatise on Basic Philosophy (Volume 4): Ontology II, A World of Systems, D. Reidel Pub. Co.: Boston, 1979.

[13] R.P. Carasik, and C.E. Grantham, A case study of Computer Supported Cooperative Work (CSCW) in a dispersed organization, Proceedings of Computer-Human Interactions, Washington, D.C., May 15–19, 1988, 61–66.

[14] R.P. Carasik, S.M. Johnson, D.A. Patterson, and G.A. Von Glahn, Towards a Domain Description Grammar: An Application of Linguistic Semantics, R.J. Norman and R. Van Ghent, R. (eds.), Proceedings of the Fourth International Workshop on Computer-Aided Software Engineering, Irvine, CA, December 5–8, 1990, 410–419.

[15] M.K. Chang, SANP: A Communication Level Protocol for Supporting Machine-to-Machine Negotiation in Organization. M.Sc. thesis, Faculty of Commerce and Busi

ness Administration, University of British Columbia, 1991.

[16] P. Chen, The Entity-Relationship Model: Toward a Unified Model of Data, ACM Transactions on Database Systems, Vol. 1 No. 1, March 1976, 9–36.

[17] P. Coad, and E. Yourdon, Object-Oriented Analysis, Englewood Cliffs, NJ: Prentice-Hall, 1991.

[18] J.L.G. Dietz, Subject-Oriented Modelling of Open Active Systems, in: E.D. Falkeberg, C. Rolland, and E.N. El-Sayed (eds.) Proceedings of the IFIP WG 8.1 Conference on Information Systems Concepts: Improving the Understanding, Alexandria, Egypt, April 13–15, 1992,, Netherlands: Elsevier Science Publishers B.V., 227–238.

[19] F. Flores, M. Graves, B. Hartfield, and T. Winograd, Computer Systems and the Design of Organizational Interaction, ACM Transactions on Office Information Systems, Vol. 6, No. 2, April 1988, 153–172.

[20] R.V. Guha, and D.B. Lenat, Cyc: A Midterm report, AI Magazine, Fall 1990, 32–59.

[21] J. Habermas, The Theory of Communicative Action, Vol.1, Thomas McCarthy (trans.), Boston, MA: Beacon Press, 1981.

[22] R. Hammer, and D. McLeod, Database Description with SDM: A Semantic Database Model, ACM Transactions on Database Systems, Vol. 6, No. 3, September 1981, 351–386.

[23] M.A. Janson, and C.C. Woo, Investigating Information and Knowledge Gathering Methods: A Speech Act Lexicon Perspective, in: E.D. Falkeberg, C. Rolland, and E.N. El-Sayed (eds.) Proceedings of the IFIP WG 8.1 Conference on Information Systems Concepts: Improving the Understanding, Alexandria, Egypt, April 13–15, 1992., Netherlands: Elsevier Science Publishers B.V., 239–257.

[24] W. Kent, Data and Reality, Amsterdam, the Netherlands: North-Holland, 1978.

[25] C.H. Kung, and A. Solvberg, Activity Modelling and Behaviour Modelling, in: T.W. Olle, H.G. Sol, and A.A. Verrijn-Stuart (eds.), Information Systems Design Methodologies: Improving the Practice, Amsterdam, North-Holland, IFIP 1986, 145–171.

[26] G. Lakoff, Women, Fire and Dangerous Things: What Categories Reveal About the Mind, Chicago: University of Chicago Press, 1987.

[27] J. Martin, and J. Odell, Object-Oriented Analysis and Design, Englewood Cliffs, NJ: Prentice-Hall, 1992.

[28] F. McFadden, and J. Hoffer, Database Management, Redwood City, CA: Benjamin/Cummings, 1991.

[29] D. Medin, and E. Smith, Concepts and Concept Formation, Annual Review of Psychology, Vol. 35, 1984, 113–138.

[30] P. Loucopoulos, and R. Zicari, R. (eds.) Conceptual Modelling, Databases and CASE, New York, John Wiley and Sons, 1992.

[31] J. Mylopoulos, Conceptual Modelling and Telos, Ch. 2 in: P. Loucopoulos and R. Zicari (eds.) Conceptual Mod-

elling, Databases and CASE, New York, John Wiley and Sons, 1992, 49–68.

[32] R. Neches, R. Fikes, T. Finin, T. Gruber, R. Patil, T., Senator and W.R. Swartout, Enabling Technology for Knowledge Sharing, AI Magazine, Fall 1991, 36–56.

[33] W. Olle, Comparative Review of Information Systems Design Methodologies, in: Olle, T.W., H.G. Sol, and A.A. Verrijn-Stuart (eds.), Information Systems Design Methodologies; A Comparative Review, Amsterdam, North-Holland, IFIP 1982.

[34] T.W. Olle, J. Hagelstein, I.G. Macdonald, C. Rolland, H.G. Sol, Van Assche, F.J.M. and Verrijn-Stuart, A.A., Information Systems Methodologies, A Framework For Understanding, Wokingham, England, Addison-Wesley Publishing Co., 1988.

[35] J. Parsons, A Classification Theory Based Information Systems Model, Ph.D. Dissertation, The University of British Columbia, May 1992.

[36] J. Parsons, A Cognitive Foundation for Comparing Object-Oriented Analysis Methods, Proceedings of the Twenty-Sixth Hawaii International Conference on Systems Sciences, Vol. IV, Maui, January 1993, 699–708 (1993a).

[37] J. Parsons, An Information Model Based on Classification Theory, Management Science, forthcoming 1996.

[38] J. Parsons, and Y. Wand, The Object Paradigm - Two for the Price of One?, Proceedings of the First Workshop on Information Technologies and Systems (WITS'91), Cambridge, MA, December 1991, 308-319.

[39] J. Parsons, and Y. Wand, Guidelines for Evaluating Classes in Data Modelling, Proceedings of the Thirteenth International Conference on Information Systems, Dallas, TX, December 1992.

[40] D. Paulson, and Y. Wand, An Automated Approach to Information Systems Decomposition, IEEE Transactions on Software Engineering, Vol. 18, No. 3, March 1992, 174–189.

[41] D. Paulson, and Y. Wand, Analysing the Completeness and Consistency of Information Systems Specifications, Working Paper, Univ. of B.C., July 1992.

[42] J. H. Petzer, Signs and Minds: an Introduction to the Theory of Semiotic Systems.: in: J.H. Petzer (ed.), Aspects of Artificial Intelligence, Kluwer Academic Publishers, 1988, 133–161.

[43] R. Quillian, Semantic Memory, in M. Minsky (ed.), Semantic Information Processing, Cambridge, MA: MIT Press, 1968.

[44] G.C. Roman, A Taxonomy of Current Issues in Requirements Engineering, IEEE Computer, Vol. 18, No. 4, April 1985, 14–22.

[45] E. Rosch, Principles of Categorization, in E. Rosch and B. Lloyd (eds.), Cognition and Categorization, Hillsdale, NJ: Erlbaum, 1978, 27–48.

[46] J. Rumbaugh, M. Blaha, W. Premerlani, F. Eddy, and W. Lorensen, Object-Oriented Modelling and Design, Inglewood Cliffs, NJ: Prentice-Hall, 1991

[47] J.R. Searle, Speech Acts: An Essay in the Philosophy of

Language, New York, NY: Cambridge University Press, 1969.

[48] J.R. Searle, A Taxonomy of Illocutionary Acts, in: K. Gunderson (ed.), Language, Mind and Knowledge, Vol.7: Minnesota Studies in the Philosophy of Science, Minneapolis: University of Minnesota Press, 1975, 344–369.

[49] J.R. Searle, and D. Vanderveken, Illocutionary Logic, New York, NY: Cambridge University Press, 1985.

[50] E. Smith, Concepts and Thoughts, in: R. Sternberg and E. Smith (eds.), The Psychology of Human Thought, Cambridge, MA: Cambridge University Press, 1988.

[51] E. Smith, and D. Medin, Categories and Concepts, Cambridge, MA: Harvard University Press, 1981.

[52] R. Stamper, Semantics, in: R.J. Bolland and R.A. Hirschheim (eds.), Critical Issues in Information Systems Research, John Wiley and Sons, 1987, 43–78.

[53] K. Takagaki, and Y. Wand, An Object-Oriented Information Systems Model, in: E.D. Falkenberg, C. Rolland and E.N. El-Sayed (eds.), Proceedings of the IFIP Working Group 8.1 conference on The Object Oriented Approach to Information Systems, Quebec City, Quebec, October 1991, 275–296.

[54] T. Teorey, Y. Yang, and J. Fry, A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model, ACM Computing Surveys, Vol. 18, No. 2, June 1986, 197–222.

[55] J. Verschueren, What People Say They Do With Words, Norwood, NJ: Ablex Publishing Corporation, 1985.

[56] Y. Wand, A Proposal for a Formal Model of Objects, in: W. Kim, and F.H. Lochovsky, (eds.), Object-Oriented Concepts, Databases and Applications, ACM Press, Addison Wesley Publishing Co., 1989, 537–559.

[57] Y. Wand, V. Storey, and R. Weber, Analysing the Meaning of a Relationship, Working Paper, Faculty of Commerce and Business Administration, The University of British Columbia, February, 1993.

[58] Y. Wand, and R. Weber, An Ontological Evaluation of Systems Analysis and Design Methods, in: E.D. Falkenberg and P. Lindgreen (eds.), Proceedings of the IFIP 8.1 Working Conference on Information Systems Concepts: An In-depth Analysis, Namur, Belgium, October 1989, Amsterdam, North-Holland, 79–107.

[59] Y. Wand and R. Weber, On the Deep Structure of Information Systems, Journal of Information Systems, Volume 5, 1995, 203–223.

[60] Y. Wand, and R. Weber, On the Ontological Expressiveness of Information Systems Analysis and Design Grammers, Journal of Information Systems, Vol 3, 1993, 217–237.

[61] Y. Wand, and C. Woo, Object-Oriented Analysis – Is It Really That Simple? Proceedings of the Third Annual Workshop on Information Technologies and Systems (WITS '93), Orlando, FL, December 1993, 186–195.

[62] G. Willumsen, Executable Conceptual Models in Information Systems Engineering, Ph.D. thesis, Norwegian Institute of Technology, University of Trondheim, 1993.

[63] T. Winograd, and F. Flores, Understanding Computers

and Cognition: A New Foundation for Design, Ablex Publishing Corporation, Norford, New Jersey, 1986.

[64] C.C. Woo, and M.K. Chang, An Approach to Facilitate the Automation of Semi-Structured and Recurring Negotiations in Organizations, Journal of Organizational Computing, Vol. 2, No. 1, 1992, New Jersey: Ablex Publishing Co., 47–76.

![](/api/attachments/B9XX7JWW/fulltext/images/0e05098c5f691ac4c1c5d109d66906e93022d7b34e4c55fbb34ef60de14ccd78.jpg)

David E. Monarchi is with the Accounting/Information Systems Division in the College of Business and Administration at the University of Colorado, Boulder. Professor Monarchi has been actively involved in object-oriented instruction and programming for 9 years, data modelling and database design for 16 years, and programming for 31 years. He has presented invited seminars and tutorials on object-oriented systems na-

tionally and internationally. His current research interests broadly include object-oriented systems (especially object-oriented analysis, design, and modelling), conceptual modelling, knowledge representation, evaluative models, and database design. He has Ph.D. from the University of Arizona, and is a member of ACM, AAAI < IEEE, and TIMS.

![](/api/attachments/B9XX7JWW/fulltext/images/ab1f4403dcfe7235a0daebdad61250bd14668e77a21a7d5fcffdd8857080ac51.jpg)

Jeffrey Parsons is an Assistant Professor of Information Systems at the Faculty of Business Administration, Memorial University of Newfoundland (Canada). He was awarded the Ph.D. in Information Systems from The University of British Columbia in 1992. His primary research interests are in conceptual modelling, systems analysis and design methodology, and database management. His research has been presented at a number of

conferences, including \* \*The International Conference on Information Systems \* \*.

![](/api/attachments/B9XX7JWW/fulltext/images/d78c75151b227975a5eb294375555d5042a60e1990f517c9e8b3eb4c102136a5.jpg)

Yair Wand is an Associate Professor and division chair in the Management Information Systems Division at the Faculty of Commerce and Business Administration, The University of British Columbia. He has a D.Sc. in Operations Research (Technion, Israel) and an M.Sc. in Physics (The Weizmann Institute, Israel). He has held positions at the Faculty of Management, The University of Calgary, Alberta, and at the Faculty of Indus-

trial Engineering, Technion, Israel. Professor Wand is on the editorial board of the \*\*Communications of the ACM\*\*, and the \*\*Canadian Journal of Administrative Sciences\*\*. His research interests are in the areas of Information Systems Modelling, format foundations for Systems Analysis and Design and Automation of Information System Development.

![](/api/attachments/B9XX7JWW/fulltext/images/06cf882f7eba687d1ad9af8e4efef0facc0109b41b01cad6e84d78b741d57436.jpg)

Carson Woo is Assistant Professor in the Faculty of Commerce and Business Administration and associate member of the Department of Computer Science, at the University of British Columbia (Vancouver, Canada). During the fall of 1992 he was Visiting Scientist at the Centre for Advanced Studies, IBM Canada. He received his B.Sc., M.Sc., and Ph.D. degrees in computer science from the University of Toronto. His

research interests include modelling and building computer-based systems for supporting organizational activities, and the application of speech act theory, ontology, and object-oriented concepts to information systems analysis and design. From 1991 until 1995, Dr. Woo is Chairperson of ACM's Special Interest Group on Office Information Systems (SIGOIS).
