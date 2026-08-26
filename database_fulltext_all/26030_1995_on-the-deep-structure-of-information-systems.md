---
otero_id: 26030
otero_key: "XMQQJMPA"
title: "On the deep structure of information systems"
authors: "Yair Wand; Ron Weber"
year: "1995"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1995.tb00108.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the deep structure of information systems

Yair Wand & Ron Weber\*

Faculty of Commerce and Business Administration, The University of British Columbia, Vancouver, BC, V6T 1Z2, Canada e-mail: yair-wand@ubc.ca \*Department of Commerce, The University of Queensland, 4072, Australia e-mail: weber@commerce.uq.edu.au

Abstract. The deep structure of an information system comprises those properties that manifest the meaning of the real-world system the information system is intended to model. In this paper we describe three models we have developed of information systems' deep-structure properties. The first, the representational model, proposes a set of constructs that enable the ontological expressiveness of grammars used to model information systems (such as the entity-relationship model) to be evaluated. The second, the state-tracking model, proposes four requirements that information systems must satisfy if they are to faithfully track the real-world system they are intended to model. The third, the good-decomposition model, proposes three necessary conditions that information systems must meet if they are to be well decomposed. The three models provide a theoretically based, structured way of evaluating grammars that are used to analyse, design and implement information systems and scripts that have been generated using these grammars to describe specific information systems.

Keywords: analysis and design, decomposition, formal models, ontology, representation, state tracking.

While the computer field has helped to popularize the word 'systems' and the concept of systems, it is ironic that information systems developers have not developed formal mechanisms to understand systems and the interrelationships among system components. Software engineering researchers have been unable to provide effective guidance to practitioners regarding the process of system definition and its concomitant implementation of functional elements.

Computer Science and Technology Board (1990, p. 283)

## INTRODUCTION

For some time we have been attempting to build formal models of information systems.\* Our purposes are twofold. First, we seek to understand and predict certain aspects of the structure and behaviour of 'good' information systems. In particular, we are focusing on those properties that an information system must possess if it is to manifest the meaning of the real-world system it is intended to model. Second, we seek to understand and predict the characteristics of 'good' information systems grammars (the sets of rules used to generate scripts that describe information systems).

In this paper we provide an overview and synthesis of our work. First we articulate a particular view of information systems that forms the basis of and motivates the nature of the formal models we have developed. Next we describe two important premises that underlie our formal models. We then provide a brief description of the formal models. To show their potential power, we sketch some research results we have obtained already and then show how the models can be applied to evaluate Chen's (1976) entity-relationship model. Finally, we discuss some future research directions and present some brief conclusions.

## SCOPE OF OUR MODELS

Our formal models are not intended to account for all phenomena associated with information systems. Clearly this task would be impossible to accomplish. In the following two subsections, therefore, we define the restricted scope of our models (Fig. 1).

![](/api/attachments/XMQQJMPA/fulltext/images/aea2ba7eef9065bc938da29dfb070c49ac7e3f6c91b457238d9a45b90a149b85.jpg)  
Figure 1. The domain of the models

## Internal Phenomena

The first way in which we restrict the scope of our models is to partition information systems phenomena, based upon two views. One treats the information system as a black box that delivers particular services to an organization, affects the lives of its users in particular ways, and evokes certain types of managerial concerns. This perspective might be called the external view. Researchers who adopt this perspective would be interested in phenomena such as the processes stakeholders use to define their information requirements, the formal and informal power shifts that occur among users when an organization implements an information system, and the ways in which an organization might use an information system to obtain competitive advantage.

The other perspective takes the requirements that an information system is intended to fulfil as given. It is concerned with the characteristics that information systems must have if they are to fulfil these requirements. This perspective might be called the internal view. Researchers who adopt this perspective would be interested in phenomena such as how well different screen interfaces might meet user needs, how data and processes should be structured to provide the required system functionality and what types of hardware platform will meet required response times.

In our models, we focus only on the internal view. Specifically, when building our formal models, we proceed using the following perspective:

An information system is an object that can be studied in its own right, independently of the way it is developed and deployed in its organizational and social context.

In other words, in our models we are not concerned with the way an information system is managed in organizations, nor with the characteristics of its users, nor with the way it is used, nor with the impact it has on such factors as the quality of working life or the distribution of power in organizations. Instead, we are concerned only with information systems as independent artefacts that are built to achieve certain requirements. This view is not intended to denigrate the importance of organizational and social issues to the successful development, implementation, and use of information systems. Rather, we propose that advantages accrue from decoupling the study of issues relating to the external view of information systems from issues relating to the internal view of information systems (Simon, 1981; Weber, 1987).\*

## Deep structure phenomena

To further restrict the scope of our models, we next distinguish between three sets of characteristics of the information systems object. The first set manifests the way the system appears to its users. Hence, we call it the surface structure of the information system. For example, the type of interactive dialogue and the format of reports used in an information system are surface-structure characteristics.

The second set manifests the meaning of the real-world system the information system is intended to model. Hence, following linguistic traditions (Chomsky, 1965), we call it the deep structure of the information system. For example, the rules embodied in an accounting system that indicate how transactions are to be posted to ledgers reflect deep-structure characteristics. These rules indicate how the wealth of certain organizations and individuals in the real world alters as contracts in an economy are exchanged and executed.

The third set manifests the nature and form of the technology used to implement the system. Hence we call it the physical structure of the information system. For example, the way in which data in the system is assigned to a mass-storage device or the communications protocol chosen for message transmission in the system are physical-structure characteristics.

In our formal models, we focus only on the deep-structure characteristics of an information system. We choose this stance for several reasons. First, if information systems are to fulfil the requirements established for them, they must correctly embed the meaning of someone' or some group's perception of the real-world system that the information system has been built to model. Note, however, that we are not seeking to address the deep issue of whether the view of reality modelled by the information system reflects objective reality or socially constructed reality. We take the real-world view as given, however it is derived. Moreover, we are not seeking to address the issue of whether the real-world view is 'good' from the external perspective of the information system. The view may reflect some manager's impoverished perspective on the world, or it may represent a compromise view that satisfies no one.\* We simply take the real-world view as given and undertake a study of deep-structure properties in an attempt to identify the necessary conditions that information systems must satisfy if they are to encapsulate the meaning embodied in the real-world view. Unless we understand these conditions, we have little hope of building good information systems even when the requirements articulated for the information system are, according to someone's criteria (external view), deemed to be 'good'.

Second, we believe good deep structures provide inherent stability to information systems in the face of change. Humans often expend large amounts of effort to develop their views of the world. They change these views only when they invoke significant stress or conflict (Kuhn, 1970). Providing the deep structure of an information system is a faithful representation of these views, it is therefore likely to be stable (Podger, 1979). The surface-structure and physical-structure properties of an information system must inevitably be modified, however, when social circumstances or technologies change. Moreover, they can often be changed without changing the deep structure of the information system. For example, the user interface may be modified or the system implemented on a new machine with no effect on the meaning of the information processing carried out by the system (Benbasat & Wand, 1984; Linton et al., 1989).

Third, research on the deep-structure properties of information systems has been much neglected. Most research in the information-systems discipline has focused on management and deployment issues and the surface-structure properties of information systems (Culnan, 1986). Most research in the computer science discipline has focused on the physical-structure properties of information systems. The major exceptions have been research on information systems methodologies (e.g. Bubenko, 1986) and database semantic modelling (e.g. Hull & King, 1987). These latter two types of research have refocused on building improved information-systems representations of real-world systems, primarily by attempting to better elicit the meaning that information systems users ascribe to real-world systems.

In summary, we view the core of information systems design as ensuring the deep structure of information systems reflects the meaning of the real-world systems they are intended to model. Accordingly, we assess the 'goodness' of information systems in terms of how well they embody the meaning of the real-world systems they supposedly represent. Clearly, this notion of goodness is limited. It ignores the significant impact that surface-structure and physical-structure properties might have on an information system's effectiveness and efficiency. None the less, by decoupling the study of deep-structure properties from surface-structure and physical-structure properties, we believe better insights into the overall nature of information systems effectiveness will be obtained.

## THE UNDERLYING PREMISES

Our formal models are motivated by two premises that reflect our view of an information system and its relationship to the real-world system it is intended to model. The first manifests our belief that an information system is a physical-symbol system that can convey meaning about the world:

The Physical-Symbol System Premise: A physical-symbol system possesses sufficient properties for it to be able to represent real-world meaning.

Note that this premise is an adaptation of Newell & Simon's (1976) physical-symbol system hypothesis. Whereas Newell and Simon hypothesize that a physical-symbol system has the necessary and sufficient properties for intelligent action, we adopt a weaker hypothesis relating only to real-world meaning.\* In essence, we believe humans are endowed with the ability to extract meaning from symbols. Surely this is the foundation for any symbol system — for example, spoken language or mathematics. An information system is simply a type of symbol system, and the symbols incorporated within the system as well as the manipulation of those symbols are capable of conveying meaning (Stamper, 1987; Pearson & Slamecka, 1983).

The second premise relates to our conception of information systems as providing representations of some part of the real world:

The Representation Premise. Information systems provide an artifactual representation of real-world systems (as perceived by someone).

The representation premise reflects our belief that the primary purpose of information systems is to model someone's or some group's view of the states and behavior of real-world systems (Kent, 1978; Winograd & Flores, 1986: 83–92).\* For example, consider an organization's sales and receivables information system. One real-world system represented by the information system is a specific customer. The information system represents various states and behavior of customers — for example, their credit standing (a state) and their desire, at some time, to obtain goods from the organization, as manifested via an order (an event). Similarly, the information system represents various states and events pertaining to the organization (another real-world system) — for example, the organization's current level of inventory and its incurring an obligation to supply inventory to a customer.

Note, the real-world system represented by the information system may be a concrete (tangible) system or a conceived system. For example, it may represent the states and events pertaining to an organization that currently operates within the marketplace or an organization that exists only in some manager's mind. Conceived systems are often the stuff of simulations and decision support systems.

## THE FORMAL MODELS

Based on our two premises, we have developed three formal models that can be used to describe and predict the impact of deep-structure phenomena. In this section we provide brief intuitive explanations of the models. More rigorous expositions are available elsewhere (Wand & Weber 1989a, 1989b, 1990b, 1993; Paulson & Wand, 1992).

## The representational model

Our representational model is based upon the notion that we build an information system by producing a set of scripts that are generated via grammars. Initially, designers generate scripts that employ human-oriented symbols — for example, descriptions of things (such as those represented in entity-relationship diagrams) or descriptions of processes (such as those represented in data flow diagrams). Later scripts are generated using machine-oriented grammars. These grammars often integrate the earlier scripts into one or a smaller number of scripts. Each script is progressively transformed into a new script until one is produced that can be read, interpreted, and executed by a machine (Fig. 2).\*

![](/api/attachments/XMQQJMPA/fulltext/images/c4931712de88e11f067439985b222443d84cf8e414800152a044a423dac8102a.jpg)  
Figure 2. A transformational model of information systems analysis, design and implementation

In our representational model, we provide a basis for evaluating information systems analysis and design grammars in terms of their ability to generate scripts that are good representations of the real world. We enunciate two evaluation criteria. First, a grammar is deemed complete if it contains constructs that enable it to model any real-world phenomenon. We have relied on and extended a particular ontology proposed by Bunge (1977, 1979) to identify the set of real-world constructs that grammars must be able to model (Wand & Weber, 1988, 1990a). We have chosen to work with Bunge's ontology because it deals directly with concepts relevant to the information systems and computer science domains (e.g. systems, subsystems and couplings). Moreover, Bunge's ontology is better developed and better formalized than any others we have encountered. $^{†}$ Table 1 provides an overview of the ontological constructs we have employed.

Second, a grammar is deemed clear if each of its constructs has a one-to-one correspondence with one of the ontological constructs shown in Table 1. Three situations can arise that undermine a grammar's ontological clarity:

Table 1. Ontological constructs in our representational model

<table><tr><td>Ontological construct</td><td>Explanation</td></tr><tr><td>Thing*</td><td>The elementary unit in our ontological model. The real world is made up of things. A composite thing may be made up of other things (composite or primitive)</td></tr><tr><td>Properties*</td><td>Things possess properties. A property is modeled via a function that maps the thing into some value. A property of a composite thing that belongs to a component thing is called a hereditary property. Otherwise it is called an emergent property. A property that is inherently a property of an individual thing is called an intrinsic property. A property that is meaningful only in the context of two or more things is called a mutual or relational property</td></tr><tr><td>State*</td><td>The vector of values for all property functions of a thing</td></tr><tr><td>Conceivable state space</td><td>The set of all states that the thing might ever assume</td></tr><tr><td>State law</td><td>Restricts the values of the property functions of a thing to a subset that is deemed lawful because of natural laws or human laws</td></tr><tr><td>Lawful state space</td><td>The set of states of a thing that comply with the state laws of the thing. It is usually a proper subset of the conceivable state space</td></tr><tr><td>Event</td><td>A change of state of a thing. It is effected via a transformation (see below)</td></tr><tr><td>Event space</td><td>The set of all possible events that can occur in the thing</td></tr><tr><td>Transformation*</td><td>A mapping from a domain comprising states to a codomain comprising states</td></tr><tr><td>Lawful transformation</td><td>Defines which events in a thing are lawful</td></tr><tr><td>Lawful event space</td><td>The set of all events in a thing that are lawful</td></tr><tr><td>History</td><td>The chronologically ordered states that a thing traverses</td></tr><tr><td>Coupling</td><td>A thing acts on another thing if its existence affects the history of the other thingThe two things are said to be coupled or interact</td></tr><tr><td>System</td><td>A set of things is a system if, for any bi-partitioning of the set, couplings exist among things in the two subsets</td></tr><tr><td>System composition</td><td>The things in the system</td></tr><tr><td>System environment</td><td>Things that are not in the system but interact with things in the system</td></tr><tr><td>System structure</td><td>The set of couplings that exist among things in the system and things in the environment of the system</td></tr><tr><td>Subsystem</td><td>A system whose composition and structure are subsets of the composition and structure of another system</td></tr><tr><td>System decomposition</td><td>A set of subsystems such that every component in the system is either one of the subsystems in the decomposition or is included in the composition of one of the subsystems in the decomposition</td></tr><tr><td>Level structure</td><td>Defines a partial order over the subsystems in a decomposition to show which subsystems are components of other subsystems or the system itself</td></tr><tr><td>Stable state*</td><td>A state in which a thing, subsystem or system will remain unless forced to change by virtue of the action of a thing in the environment (an external event)</td></tr><tr><td>Unstable state</td><td>A state that will be changed into another state by virtue of the action of transformation in the system.</td></tr><tr><td>External event</td><td>An event that arises in a thing, subsystem or system by virtue of the action of some thing in the environment on the thing, subsystem or system. The before-state of an external event is always stable. The after-state may be stable or unstable.</td></tr><tr><td>Internal event</td><td>An event that arises in a thing, subsystem, or system by virtue of lawful transformations in the thing, subsystem, or system. The before-state of an internal event is always unstable. The after-state may be stable or unstable</td></tr><tr><td>Well-defined event</td><td>An event in which the subsequent state can always be predicted given the prior state is known</td></tr><tr><td>Poorly defined event</td><td>An event in which the subsequent state cannot be predicted given the prior state is known</td></tr><tr><td>Class</td><td>A set of things that possess a common property</td></tr><tr><td>Kind</td><td>A set of things that possess two or more common properties</td></tr></table>

Note: \* indicates a fundamental ontological construct. All other constructs are derived from these constructs (see Wand & Weber, 1990b).

(1) One grammatical construct may map to two or more ontological constructs. This situation manifests construct overload in the grammar. The script interpreter (a person or a machine) inevitably must employ knowledge obtained outside the grammar to determine which ontological construct is being represented by the script.

(2) Two or more grammatical constructs may map to one ontological construct. This situation manifests construct redundancy in the grammar. Either the grammar provides excessive design constructs, or the mapping rules (semantics) of the grammar are unclear.

(3) A grammatical construct may not map to any ontological construct. This situation manifests construct excess in the grammar. In essence, the grammatical construct is a 'nonsense' construct in the context of the ontological model.

If a grammar is not ontologically expressive, we predict descriptions of the real-world system generated using the grammar will be deficient. A grammar that is not ontologically complete lacks the constructs (symbols) needed to convey meaning about some aspect of the real world. A grammar that lacks ontological clarity has constructs (symbols) that convey ambiguous meaning about the real world.

## The state-tracking model

If an information system is to provide a good representation of a real-world system, it must faithfully track changes in the real-world system it models. Our state-tracking model specifies four conditions that we claim an information system must satisfy if faithful state tracking is to occur. We claim, moreover, that these conditions constitute the necessary and sufficient set.

The first condition that must hold is the mapping requirement. It pertains to the structure of both the real-world and information systems:

(1) The Mapping Requirement. Each real-world system state must map to at least one information system state.

If the mapping requirement is satisfied, at least one information system state exists for every real-world system state. Note, more than one information system state might exist for each real-world system state because of the way the information system is implemented. For example, the system may delay processing of transactions to improve update efficiency. One real-world state may correspond to multiple system states to reflect the variable length of transaction queues that await processing.

Note also, the mapping may be an into mapping. In other words, not all states in the information system may correspond to the real-world system's states. This situation may reflect implementation considerations. For example, the information system may have to access multiple files before it reaches a state that corresponds to the real-world state. Some states in the sequence of states it traverses to access these files may have no real-world system correspondence.

The second requirement is the tracking requirement. It relates to the behaviour of the information system and stipulates that the information system must replicate real-world system behaviour:

(2) The Tracking Requirement. When the real-world system changes states, the information system must be able to change from a state that corresponds to the initial real-world system state to a state that corresponds to the subsequent real-world system state.

This requirement implies that a homomorphism exists between state transitions in the real-world system and state transitions in the information system. In other words, transformations in the information system must ensure the information system can change states in congruence with the state changes occurring in the real-world system.

The mapping and tracking requirements are still insufficient, however, to guarantee that the information system will faithfully represent the real-world system behaviour. The first problem may be that relevant external (input) events occurring in the real-world system are not transmitted or reported to the information system. Accordingly, we have the external-event requirement, which pertains to external events — events in a system that reflect the influence of the environment:

(3) The External-Event Requirement. If an external (input) event occurs in the real-world system, an event that is a faithful representation of the real-world external event must occur in the information system.

Consider two cases. The first is where the information system initiates an external event in the real-world system — for example, the information system activates a production system. In this situation, an event in the information system has occurred that is a representation of the real-world external event. No reporting of the external event in the real-world system is needed.

Consider, however, a case where a salesperson signs a contract with a customer. The salesperson must report the sale to the information system if, for example, the information system is to track the states of the customer as one of the real-world systems it represents. The third requirement ensures, therefore, that the information system 'knows' about relevant external events in the real-world system.

The second problem is that the events in the information system which mirror the real-world system external events may not arise in the same sequence as the real-world system external events. For example, transactions to be processed by the information system may be cached and later randomly input to the system. Thus, we have the sequencing requirement.

(4) The Sequencing Requirement. Events in the information system that represent external events in the real-world system must be ordered in the same way as the real-world system external events they represent.

The purpose of the sequencing requirement, therefore, is to ensure the information system does not lose track of the real-world system states because external events are not reported to the information system in the correct order.

The four state-tracking requirements allow us to carry out two types of evaluations. First, any grammar used to describe an information system can be examined to determine whether it contains components that enable the four requirements to be satisfied. If the grammar does not provide these components, our model predicts that scripts generated using the grammar will be defective. Second, a particular script generated via a grammar to describe an information system can be evaluated to determine whether it satisfies the four requirements. A grammar may contain components that enable scripts to be generated which satisfy the four requirements; however, a particular script produced using the grammar still may not satisfy these requirements. In short, even with good tools, a designer may still produce defective information systems designs.

## The good-decomposition model

Our decomposition model is motivated by the belief that representations which manifest 'good decompositions' of the real-world system convey more meaning about the real-world system they model than representations that are not well decomposed. In our decomposition model we have sought, therefore, to define the notion of a decomposition precisely and to identify the characteristics of a good decomposition (Wand & Weber, 1989c, 1991).

Our model specifies three conditions that must hold for a decomposition to be good. The first addresses the notion that the behaviour of subsystems in the decomposition must be predictable.

(1) Determinism. For a given set of external events at the system level, a decomposition is good only if for every subsystem (at every level in the level structure of the system) an event is either (a) a specified external event, or (b) a well-defined internal event.

The determinism requirement recognizes that subsystems undergo two types of events. The first are external events, which manifest the influence of the environment on the subsystem. The second are internal events, which manifest the state changes that occur internally to a system as a result of an external event. In our model, external events may change a subsystem to an unstable state. Transformations then act to move the subsystem back to a stable state. The state changes that occur subsequent to the external event to restore the subsystem to stability are the internal events.

External events, by their very nature, are often unpredictable. For example, the amount of inventory received in an inventory system may depend upon the amount a vendor can provide. Given the current state of inventory is, say, $s_{1}$ , the new state might be $s_{2}$ if the vendor supplies, say, 20 units, or $s_{3}$ if the vendor supplies, say, 30 units. In other words, the event is poorly defined in the sense that, without knowledge of the vendor's situation, the subsequent state of inventory cannot be predicted.

In a good decomposition, poorly-defined events (Fig. 3a) are permitted providing they are known to be (specified) external events. All internal events, however, must be well defined (Figure 3b). In other words, the subsequent state of the subsystem can be predicted given knowledge of the prior state. In summary, in a good decomposition, the event space of every subsystem is partitioned into internal events, all of which must be well-defined, and specified (named) external events that may or may not be well-defined (Figure 4a). If a poorly defined event exists that is not a specified (named) external event, the decomposition is poor (Figure 4b).

The second requirement addresses the notion that subsystems should be described via the minimal set of properties needed to characterize the states of the subsystem:

(2) Minimality. A decomposition is good only if for every subsystem (at every level in the level structure of the system) there are no redundant state variables describing the subsystem.

A redundant state variable is one that is never 'used' during the lifetime of the subsystem. In other words, it has no influence over the events that occur to the subsystem. Redundant state variables add noise to a representation and undermine its ability to convey meaning clearly.

![](/api/attachments/XMQQJMPA/fulltext/images/1211c373796ca42556d96f35368f15f91dd113b429e8ed982b879518b882b461.jpg)  
Figure 3. (a) Poorly defined event;

![](/api/attachments/XMQQJMPA/fulltext/images/123d188f7f7e7c7001c0818d434a4558a237c3e4fcaa92184d491e05a9f5dd51.jpg)  
(b) Well-defined event

![](/api/attachments/XMQQJMPA/fulltext/images/f7c0651635d917a0e9eea246345db34ebe050b2fb823ab7114e333177a4c23bf.jpg)  
Figure 4. (a) System event space under a good decomposition; (b) System event space under a poor decomposition

The third requirement addresses the notion that emergent variables must be preserved in any good decomposition:

(3) Losslessness. A decomposition is good only if every emergent variable in the system is a function of properties of at least one subsystem in the decomposition.

The value assigned to an emergent state variable (a state variable describing a property of the whole system) depends upon the values of some subset of the state variables that describe the system's subsystems (the hereditary state variables). For example, the total value of assets in an accounting system (an emergent state variable) is some function of the values of the individual assets in the various subsystems (debtors, inventory, etc.). Emergent state variables, like all other state variables, carry meaning about a system. They must not be 'lost' when the system is decomposed into subsystems.

Note that our three requirements for a representation to be well decomposed are only necessary requirements. Whether they are sufficient requirements is an ongoing research issue.

## AN APPLICATION OF THE FORMAL MODELS

As we indicated at the outset, we seek to use our models to better understand and predict some characteristics of (a) good information systems and (b) good information systems analysis and design grammars. In this regard, we believe our models have been used successfully in a number of ways. For example, they have been used to predict the impact of changes in the event space of an information system on controls and audit procedures (Wand & Weber, 1989a), to better understand the nature of objects in object-oriented design (Parsons & Wand, 1991; Wand, 1989; Takagaki, 1990; Takagaki & Wand, 1991), to provide the basis for the design of tools that automate the decomposition process (Paulson & Wand, 1992) and to define the notion of ontological expressiveness of an information systems analysis and design grammar (Wand & Weber, 1993). In this section, however, we seek to illustrate the usefulness of our models by employing them to evaluate a widely-used grammar that facilitates undertaking information systems analysis, design and implementation — namely, Chen's (1976) entity-relationship model (ERM)\* (see also Wand & Weber, 1989b; Weber & Zhang, 1991).

Usually the ERM grammar is employed to generate scripts early in the transformation process shown in Figure 2. Recall that the ERM is intended to allow 'semantic modelling' of the domain of discourse. Supposedly it enables designers and users of an information system to obtain a better understanding of the real-world system that underlies the information system they are intending to build. The mapping between ontological constructs and ERM grammatical constructs, therefore, should be fairly direct.

Consider, first, the ERM in terms of our representational model. The semantics of the ERM grammatical constructs can be interpreted using the ontological constructs listed in Table 1. The 'classic' ERM grammar has three constructs: entities, relationships and attributes (and their connections). Cardinalities (mapping ratios) can also be added to ER diagrams. Since entities model things in the application domain, a specific entity represents the ontological construct of a thing. In the ontological model, things that are viewed as similar (entity types in the ERM) constitute a class or kind. Entity attributes in the ERM correspond to the ontological construct of an intrinsic property — a property of a thing that is not related to another thing. Relationships and their attributes, on the other hand, correspond to the ontological construct of a mutual property — a property that is joint to several things.

This interpretation of the real-world meaning of the ERM constructs leads to several conclusions. First, the ontological model provides a means of resolving the well-known confusion that sometimes arises over whether to represent some aspect of the real world as an entity or a relationship in an ER diagram. Specifically, entities should be used to represent things only; relationships should be used to represent mutual properties only. Secondly, in the ontological model, both intrinsic properties and mutual properties will be represented in the functional schema that describes a class or kind of thing. In this light, connecting both attributes (intrinsic properties) and relationships (mutual properties) to entities (a class or kind of thing) via an arc is meaningful ontologically. Third, the notion of a weak entity in the ERM has an ontological interpretation. Both regular entities and weak entities correspond to the ontological construct of a thing. Regular entities can be uniquely identified, however, via intrinsic properties. Weak entities, on the other hand, must be identified uniquely via mutual properties. $^{†}$ Fourth, the representational model generates an important prediction: since a thing can have more than one functional schema (corresponding to different views of the thing), the same entity may be an instance of several entity types. Note, this idea is more general than the notion of subclassification.

Table 2. Evaluation of the entity-relationship model for ontological completeness

<table><tr><td>Ontological construct</td><td>Representation in the entity-relationship model (ERM)</td></tr><tr><td>Thing</td><td>Represented in the ERM via entities and in some cases relationships. Relationships may represent composite things when they are information-bearing relationships; that is, when they possess attributes other than the identifiers of the entities that participate in the relationship</td></tr><tr><td>Property</td><td>Represented in the ERM via attributes and in some cases relationships. If the attributes of a relationship comprise only the identifiers of the entities that make up the relationship (that is, it is a non-information-bearing relationship), then the relationship simply manifests properties of the individual entities that make up the relationship. It is not a substantial thing itself</td></tr><tr><td>State</td><td>Represented by the values of the attributes of entities and relationships at different points in time. However, the possible values are not represented directly in an ERD. They may be provided via supplemental information, e.g. a data dictionary</td></tr><tr><td>Conceivable state space</td><td>Not represented directly in an ERD. It must be determined from supplemental information, e.g. a data dictionary</td></tr><tr><td>State law</td><td>Only a small amount of state law information is represented in an ERD via referential and cardinality constraints. Other state laws must be determined from supplemental information in a data dictionary and process scripts</td></tr><tr><td>Lawful state space</td><td>Must be determined from supplemental information, e.g. a data dictionary and process scripts</td></tr><tr><td>Event</td><td>Not represented</td></tr><tr><td>Event space</td><td>Since there is no construct in the ERM to represent events, the event space also cannot be represented</td></tr><tr><td>Transformation</td><td>Not represented</td></tr><tr><td>Lawful transformation</td><td>Not represented</td></tr><tr><td>Lawful event space</td><td>Since events and lawful transformations cannot be represented in an ERD, the lawful event space also cannot be represented</td></tr><tr><td>History</td><td>Not represented</td></tr><tr><td>Coupling</td><td>Only some couplings are shown in ERD via relationships (those that reflect the existence of one thing depends upon the existence of another thing). Other types of couplings are not shown, however, for example, those that reflect a property value of one thing depends upon a property value of another thing</td></tr><tr><td>System</td><td>Providing all couplings between entities in an ERD are shown via relationships, the ERD represents a system. This outcome often does not occur because some couplings between things are not shown in an ERD</td></tr><tr><td>System composition</td><td>The entities and some information-bearing relationships in an ERD constitute the composition of the system</td></tr><tr><td>System environment</td><td>An ERD may show some entities or relationships that are part of the environment. However, it does not show which entities and relationships are in the composition of the system and which are in the environment of the system unless a boundary is drawn around the entities that are in the composition of the system. Boundaries are not within the syntax of the original ERM</td></tr><tr><td>System structure</td><td>An ERD shows the system structure providing (a) all entities in the environment and composition of the system are shown, (b) all couplings between entities in the environment of the system and entities in the composition of the system are shown via relationships and (c) all couplings between entities in the composition of the system are shown via relationships. These requirements are unlikely to be satisfied</td></tr><tr><td>Subsystem</td><td>Not represented. However, subsystems can be designated by drawing a boundary around entities in an ERD that are coupled (as manifested by relationships) in such a way that the definition of a subsystem is satisfied. Again, boundaries are not included within the syntax of the original ERM. Moreover, not all couplings may be shown on an ERD. Thus a subsystem may not be correctly identified</td></tr><tr><td>System decomposition</td><td>Not represented</td></tr><tr><td>Level structure</td><td>Not represented</td></tr><tr><td>Stable state</td><td>Not represented</td></tr><tr><td>Unstable state</td><td>Not represented</td></tr><tr><td>External event</td><td>Not represented</td></tr><tr><td>Internal event</td><td>Not represented</td></tr><tr><td>Well-defined event</td><td>Not represented</td></tr><tr><td>Poorly defined event</td><td>Not represented</td></tr><tr><td>Class/kind</td><td>A class/kind represented by an entity symbol, which stands for an entity type</td></tr></table>

Using our representational model, Table 2 shows our evaluation of the ERM in ontological terms. It shows the ERM is deficient primarily in five ways:

(1) The ERM cannot fully represent information about states, including the definition of state spaces and state laws. Thus, important semantic information about the states that a real-world system may traverse and which of these states are lawful is not captured.

(2) The ERM cannot represent information about dynamics, including events, event spaces, lawful transformations and lawful event spaces. Information systems designers must somehow capture the dynamics of the real-world system to be incorporated in the information system using other means (e.g. data flow diagrams).

(3) The ERM represents couplings between things by showing their mutual properties (relationships). Coupling implies the history of at least one entity in a relationship is conditional upon the history of the other entity in the relationship. Since states are not represented in the

ERM, however, neither is the history of a thing. Hence it is impossible to know whether relationships in an ER diagram represent all couplings between things. If all couplings are not shown via relationships, the ERM does not support representation of systems (or subsystems). (4) Since the ERM does not model states, stable states cannot be distinguished from unstable states. Furthermore, since it does not represent events, it provides no means of distinguishing between external and internal events and well-defined and poorly defined events.

(5) Construct overload and construct redundancy exist in the use of the ERM. For example, relationships are sometimes used to represent things, mutual properties, and composite things (construct overload), and things can be represented via either entities or relationships (construct redundancy). We predict that construct overload and construct redundancy sometimes lead to confusion among users of the ERM.

Note that our evaluation of the ERM helps elucidate our notion of ontological completeness. In many, if not all cases where an ERM construct has not been provided for an ontological construct, one of the ERM constructs could be perverted to provide a representation of the missing ontological construct. For example, besides representing things, entities in the ERM could also be used to represent events. Once this action is taken, however, the one-to-one mapping between ontological constructs and grammatical constructs is no longer preserved (an entity can now represent a thing and an event). As a result, construct overload arises. When construct overload occurs with an ER diagram, users must bring to bear additional knowledge not included in the ERM to interpret the ER diagram. For example, if an entity symbol is marked as an 'event', relationships connected to the event acquire a special meaning (such as 'an event affects an entity' or 'an event triggers another event'). In such cases, interpretation of the relationship symbol requires knowledge of the domain.

Consider next the ERM in the context of our state-tracking model. The ERM fails to provide constructs that ensure the designer builds information systems that faithfully track the real-world systems they are intended to model. A designer who uses the ERM would have difficulty satisfying the four requirements that must be met if an information system is to be a faithful state-tracking mechanism, primarily because the ERM provides only an impoverished representation of the dynamics of the real-world system:

(1) The mapping requirement may not be satisfied because states are not fully represented in the ERM (see Table 2).

(2) The tracking equipment may not be satisfied because the ERM does not provide constructs that represent transformations.

(3) Neither the external-event nor sequencing requirements may be satisfied because the ERM does not provide constructs to represent events.

Consider finally the ERM in the context of our good-decomposition model. The ERM is again deficient because of its impoverished representation of dynamics. Thus external events cannot be distinguished from internal events and well-defined events cannot be distinguished from poorly defined events. These constructs are needed if the goodness of a decomposition is to be evaluated.

In summary, our models provide a theoretically based, structured way of identifying the strengths and deficiencies of the ERM as a means of representing the static and dynamic aspects of real-world systems. Unlike many past evaluations of the ERM, we have not relied on atheoretical, piecemeal analyses. Moreover, while we acknowledge that some of our conclusions are well known (e.g. deficiencies with respect to dynamics), others we believe provide new insights (e.g. the nature of relationships in the ERM and those properties of the ERM that undermine a designer's ability to obtain good decompositions).

## FUTURE RESEARCH DIRECTIONS AND CONCLUSIONS

Our current research is aimed at refining, extending and testing our three models. With our representational model, we are pursuing three research directions. First, we are undertaking theoretical research to determine whether new ontological constructs and assumptions are needed to model real-world systems. Second, we are pursuing empirical work that tests our predictions about the ontological strengths and weaknesses of different information systems grammars. Third, we are applying the ontological approach to various analysis, design and implementation issues, such as specifications verification and automated support for object-oriented prototyping.

With our state-tracking model, we are seeking to evaluate information systems grammars to determine whether they provide constructs that enable the four state-tracking requirements to be satisfied. These theoretical evaluations are helping to clarify the notions of completeness and consistency in information systems specifications. In addition, the four requirements form the basis for evaluating existing, implemented information systems so their strengths and weaknesses might be predicted. These predictions can then be tested empirically.

With our decomposition model, we are seeking to identify further characteristics of good decompositions. Our ultimate goal is to identify the necessary and sufficient conditions for a good decomposition. In this light, we are evaluating existing information systems analysis, design and implementation grammars to determine whether they provide constructs that ensure the scripts they generate can lead to good decompositions. In addition, we are evaluating existing decomposition methods to determine their strengths and weaknesses and developing automated support for systems decomposition.

Many current information systems grammars are unlikely to satisfy the requirements of our three models. Future research might be undertaken, therefore, to determine the relative strengths and weaknesses of attempting to modify a grammar to rectify its deficiencies versus using the grammar in conjunction with other grammars to satisfy the requirements of the three models. If a grammar is modified to rectify its deficiencies, perhaps the grammar's surface structure will become too complex for users to be able to employ it effectively and efficiently. If multiple grammars are used to address a design problem, however, the scripts produced may be inconsistent, incomplete and not well integrated.

On the basis of our empirical work with designers, we have found that some grammars appear to work together better than others. We believe our models enable us to predict which grammars can be used more successfully in conjunction with one another. For example, we hypothesize that script inconsistencies will increase as the overlap between the ontological constructs that can be represented in one grammar and the ontological constructs that can be represented in the other grammar increases. In other words, grammars that represent disparate ontological constructs are more likely to work together better. From the viewpoint of design practice, future research that determines which grammars work together better would be especially useful.

We also see merit in examining the deep structure of information systems from the perspective of different ontologies. As we indicated earlier in the paper, we have based our models on Bunge's ontology because we find his work to be intuitively appealing and rigorous. Nevertheless, the implications of other ontologies should be explored. For example, Guha & Lenat's (1990) work is based on an ontology that assumes everything is a thing: events, processes, relationships, etc. We hope others might investigate alternative ontologies so that ultimately a choice might be made between competing ontologies in light of the insights they provide and the predictions they generate.

In summary, on the basis of our work so far, we believe the ontological approach to understanding and formalizing information systems concepts provides us with the rudiments of a theory of information system design, based upon the notion of the deep structure of an information system. As a number of writers have observed (e.g. Bubenko, 1986; Floyd, 1986), lack of suitable theory has seriously undermined research on information systems analysis, design and implementation. While our models cannot address all phenomena of interest in these areas, we believe they have been and will continue to be fruitful in examining some major issues that relate to the semantics embedded in information systems.

## ACKNOWLEDGEMENTS

We are indebted to Frank Land, Michael Lawrence, Paul Ledington, Richard Mason, Richard Mattesich, Carson Woo and participants in workshops at Bond University, the University of British Columbia and LaTrobe University for helpful comments on previous versions of this paper. We would also like to thank the reviewers and the editors for their helpful comments. The research described in this paper was supported in part by an NSERC operating grant and a grant from GWA Ltd. An earlier and condensed version of this paper was presented at the Eleventh Annual International Conference on Information Systems, Copenhagen, December 1990.

## REFERENCES

Agassi, J. (1990) Ontology and its discontent. In: Studies on Mario Bunge's Treatise, Weingartner, P. and Dom, G. (eds), 105–122. Rodopi, Amsterdam.

Ahituv, N. (1987) A metamodel of information flow: a tool to support information systems theory. Communications of the ACM, 30, 781–791.

Barker, R. (1990) CASE\*Method™: Entity Relationship Modelling. Addison-Wesley, Wokingham.

Benbasat, I. & Wand, Y. (1984) A structured approach to designing human-computer dialogue. International Journal of Man-Machine Studies, 21, 105–126.

Bochenski, J.M. (1990) On the system. In: Studies on Mario Bunge's Treatise, Weingartner, P. and Dom, G. (eds), 99–104. Rodopi, Amsterdam.

Boland, R.J. Jr. (1987) The information of information systems. In: Critical Issues in Information Systems Research, Boland, R.J. Jr. and Hirschheim, R.A. (eds.), pp. 363–379. John Wiley, New York.

Bubenko, J.A. Jr (1986) Information system methodologies — a research review. In: Information Systems Design Methodologies: Improving the Practice, Olle, T.W., Sol, H.G. and Vernijn-Stuart, A.A. (eds), pp. 289–318. North-Holland, Amsterdam.

Bunge, M. (1977) Treatise on Basic Philosophy. Vol. 3.
Ontology I: The Furniture of the World. Reidel, Boston.

Bunge, M. (1979) Treatise on Basic Philosophy. Vol. 4.
Ontology II: A World of Systems. Reidel, Boston.

Chen, P.P.S. (1976) The entity-relationship model — toward a unified view of data. ACM Transactions on Database Systems., 1, 9–36.

Chomsky, N. (1965) Aspects of a Theory of Syntax. Harvard University Press, Cambridge, MA.

Churchland, P.M. & Churchland, P.S. (1990) Could a machine think? Scientific American., 262, 26–31.

Computer Science and Technology Board (1990) Scaling up: a research agenda for software engineering. Communications of the ACM, 33, 281–293.

Culnan, M. (1986) The intellectual structure of management information systems, 1972–1982: a co-citation analysis. Management Science., 32, 156–172.

Dasgupta, S. (1989) The Structure of design processes. In: Advances in Computers, Vol. 28.. Yovits, M.C. (ed.), pp. 1–67. Academic Press, San Diego.

Fetjer, J.H. (1988) Signs and minds: an introduction to the theory of semiotic systems. In: Aspects of Artificial Intelligence, Fetzer, J.H. (ed.), pp. 133–161. Kluwer, Dordrecht.

Floyd, C. (1986) A comparative evaluation of system development methods. In: Information Systems Design Methodologies: Improving the Practice, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds.), pp. 19–54. Elsevier Science Publishers, North-Holland, Amsterdam.

Guha, R.V. & Lenat, D.B. (1990) Cyc: a midterm report. AI Magazine, 22, 32–59.

Hirschheim, R. & Klein, H.K. (1989) Four paradigms of information systems development. Communications of the ACM, 32, 1199–1216.

Hull, R. & King, R. (1987) Semantic database modelling: survey, applications, and research issues. ACM Computing Surveys., 19, 201–260.

Kent, W. (1978) Data and Reality: Basic Assumptions in Data Processing Reconsidered. North-Holland, Amsterdam.

Kuhn, T.S. (1970) The Structure of Scientific Revolutions, University of Chicago Press, Chicago.

Land, F. (1989) From software engineering to information systems engineering. In: Participation in Systems Development, Knight, K. (ed.), pp. 9–33. Kogan Page, London.

Linton, M.A., Vlissides, J.M. & Calder, P.R. (1989) Composing user interfaces with interViews. Computer, 22, 8–22.

Newell, A. (1980) Physical symbol systems. Cognitive Science, 4, 135–183.

Newell, A. & Simon, H.A. (1976) Computer science as empirical inquiry: symbols and search. Commun. ACM, 19, 113–126.

Parsons, J. & Wand, Y. (1991) The objects paradigm — two for the price of one. In: Proceedings of the Workshop on Information Technologies and Systems, pp. 308–319. Boston, Massachusetts.

Paulson, D. & Wand, Y. (1992) An automated approach to information systems decomposition. IEEE Transactions on Software Engineering, 18, 174–189.

Pearson, C. & Slamecka, V. (1983) Perspectives on informatics as a semiotic discipline. In: The Study of Information: Interdisciplinary Messages, Machlup, F. and Mansfield, U. (eds), pp. 141–147. John Wiley, New York.

Penrose, R. (1989) The Emperor's New Mind. Oxford University Press, Oxford.

Podger, D.N. (1979) High level languages — a basis for participative design. In: Design and Implementation of Computer-Based Information Systems, Szyperski, N. and Grochla, E. (eds), pp. 243–259. Sijthoff & Noordhoff, Alphen aan den Rijn.

Searle, J.R. (1990) Is the brain's mind a computer program? Scientific American, 262, 20–25.

Simon, H.A. (1981) The Sciences of the Artificial, 2nd ed. MIT Press, Cambridge, MA.

Stamper, R.K. (1979) Towards a semantic normal form. In: Data Base Architecture, Bracchi, G. and Nijseen, G.M. (eds), pp. 317–339. North-Holland, Amsterdam.

Stamper, R.K. (1987) Semantics. In: Critical Issues in Information Systems Research, Boland, R.J., Jr. and Hirschheim, R.A. (eds), pp. 43–78. John Wiley, New York.

Takagaki, K. (1990) A Formalism for Object-based Information Systems Development. Unpublished Ph.D. dissertation, University of British Columbia.

Takagaki, K. & Wand, Y. (1991) An object-oriented information systems model. In: Proceedings of the IFIP 8.1 Working Conference on the Object-Oriented Approach to Information Systems, Quebec City, Van Assche, F., Moulin, B., & Rolland, C. (eds) pp. 275–296. North Holland, Amsterdam.

Teorey, T.J., Yang, D. & Fry, J.P. (1986) A logical design methodology for relational databases using the extended entity-relationship model. ACM Computing Surveys, 18, 197–222.

Wand, Y. (1989) A proposal for a formal model of objects. In: Object-Oriented Concepts, Applications, and Databases, Kim, W. and Lochovsky, F. (eds), pp. 537–559. Addison-Wesley, Reading, MA.

Wand, Y. & Weber, R. (1988) An ontological analysis of some fundamental information systems concepts. In: Proceedings of the Ninth Annual International Conference in Information Systems, Minneapolis, MN, DeGross, J. & Olson, M.H. (eds) pp. 213–225.

Wand, Y. & Weber, R. (1989a) A model of control and audit procedure change in evolving data processing systems. The Accounting Review, 64, 87–107.

Wand, Y. & Weber, R. (1989b) An ontological analysis of some systems analysis and design methods. In: Information Systems Concepts — An In-Depth Analysis, Falkenberg, E. and Lindgreen, P. (eds), pp. 79–107. North-Holland, Amsterdam.

Wand, Y. & Weber, R. (1989c). A model of systems decomposition. In: Proceedings of the Tenth Annual International Conference on Information Systems, Boston, MA., DeGross, J., Henderson, J.C. & Konsynski, B.R. (eds) pp. 41–51.

Wand, Y. & Weber, R. (1990a) Mario Bunge's Ontology as a formal foundation for information systems concepts. In: Studies on Mario Bunge's Treatise, Weingartner, P. and

Dorn, G. (eds), pp. 123–150. Rodopi, Amsterdam.

Wand, Y. & Weber, R. (1990b) An ontological model of an information system. IEEE Transactions on Software Engineering, 1282–1292.

Wand, Y. & Weber, R. (1991) A unified model of software and data decomposition. In: Proceedings of the Twelfth Annual International Conference on Information Systems, New York, DeGross, J., Benbasat, I., DeSanctis, G. & Beath, C.M. (eds) pp. 101–110.

Wand, Y. & Weber, R. (1993) On the ontological expressiveness of information systems analysis and design grammars. Information Systems Journal, 217–237.

Weber, R. (1987) Toward a theory of artifacts: a paradigmatic basis for information systems research. Information Systems Journal, 1, 3–19.

Weber, R. & Zhang, Y. (1991) An ontological evaluation of NIAM's grammar for conceptual schema design. In: Proceedings of the Twelfth Annual International Conference on Information Systems, DeGross, J., Benbasat, I., DeSanctis, G., and Beath, C.M. (eds), pp. 75–82. New York.

Winograd, T. & Flores, F. (1986) Understanding Computers and Cognition: A New Foundation for Design. Ablex, Norwood, NJ.

## Biographies

Ron Weber is Professor of Commerce at the University of Queensland, Brisbane, Australia. His primary research interests are in formal modelling of information systems, computer control and audit, and management of the information systems function. He is a Fellow of the Australian Computer Society, a Fellow of the Australian Society of Certified Practising Accountants, and a Fellow of the Institute of Chartered Accountants in Australia. He is also a Past President of the Accounting Association of Australia and New Zealand.

Yair Wand is on faculty at the Management Information Systems Division, Faculty of Commerce, The University of British Columbia (Vancouver, Canada). He has a D.Sc. in Operations Research (Technion, Israel) and an M.Sc. in Physics from The Weizmann Institute, Israel. He has held positions in the Faculty of Management, The University of Calgary, Canada, and the Faculty of Industrial Engineering, Technion. His research interests are in the areas of information systems modelling, formal foundations for systems analysis and design, and automation of information system development.
