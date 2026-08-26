---
otero_id: 23453
otero_key: "JEBGMVN9"
title: "Deriving semantic data models from structured process descriptions of reality"
authors: "George L Benwell; Peter G Firns; Philip J Sallis"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Deriving semantic data models from structured process descriptions of reality

GEORGE L. BENWELL, PETER G. FIRNS and PHILIP J. SALLIS

Computer and Information Science, The University of Otago, PO Box 56, Dunedin, New Zealand

Abstract: This paper begins by describing a generally accepted view of the contemporary information systems development process. This process assumes the direct derivation of a prototype from data models which have themselves been derived from a functionally decomposed representation of reality. The data models are constructed using entity-relationship modelling (ERM) and data flow diagram (DFD) techniques. The paper also considers the use of Petri net representations as structured process models of reality. These representations are a means of structuring the functional analysis of observed situations for which an information system design is required. The paper then suggests a refinement to the model just described. It examines the relationship between the ERM and DFD techniques and proposes the use of logical access mapping (LAM) as a method of synthesizing the product of these two data modelling activities. An example is used to illustrate the derivation of ERM and DFD from Petri nets. Also an example of the refined process model is given. 'Weak links' in this model are identified and further work towards establishing a method for formally proving data models is proposed.

## Introduction

The evolution of information systems development methods has by no means produced a consensus view of the sequence or nature of activities carried out by systems designers. Throughout the literature, (Lucas, 1985; Mantha, 1987; Necco et al, 1987 and more recently, Sallis, 1988) there is continuing reference made to the observable phenomenon of the system development life cycle (SDLC). Although acknowledged not to be a strictly sequential set of activities, the SDLC, as shown in Figure 1, provides a framework in which to consider, in general terms, the events which occur during the development of information systems. Usually these events are considered as phases of development and say more about the organizational or production processes of the work in progress than the techniques which are actually applied.

A more task-oriented illustration of the system development events which occur is given in Figure 2a. This figure shows the production of a functionally decomposed representation of reality, usually in the form of organizational hierarchy models, in addition to function and process charts. Derived from this representation are both data flow and data structure models; the latter commonly being developed using ERM techniques. These techniques were originally devised by Chen (1976) and have since been extended by others.

Figure 2b illustrates, in greater detail, the intermediate steps in proceeding from data models to an information system. From the data flow diagrams (DFDs), data processing algorithms can be derived, (Gane and Sarsen, 1979), and from the ERMs, a database schema can be derived. Debate concerning the exclusive appropriateness of each of these methods continues in the literature, but Mantha (1987) has some empirical evidence which indicates that the resultant set of relations and attributes issuing from either DFD or ERM are imperceptibly different. There is a small variation in favour of the ERM method. In the research carried out by Mantha (1987), the analysts used were trained using one or other of these methods to produce DFDs and ERMs from a common set of data. Conceptually at least, this paper proposes the use of both methods to produce a composite data model in order to develop an integrated design for data flow and data structure which can be implemented.

Together, these provide input to the construction of a prototype which may in turn become the final information system, or more likely, be used as the user requirements specification (URS) (Sallis, 1988). Production of the prototypes (specifications) in this way has recently been facilitated by the use of computer aided software engineering (CASE) tools and fourth generation languages (4GLs) (Sallis, 1989).

Figure 3 redefines the elements of the process in three primary ways. These are as follows:

(1) The inter-dependence between the DFDs and ERMs is explicitly represented. It is proposed that logical access maps (LAMs) (McFadden and

![](/api/attachments/JEBGMVN9/fulltext/images/0199bea8cdd0a74b90e135700b8671acf4b6d4c8c6a0c6dd4c523ce4278127f8.jpg)  
Figure 1 The system development life cycle

![](/api/attachments/JEBGMVN9/fulltext/images/ce6b79c5e89a96af262e08de451f8b3ddd2b17da71b7ae047f4b942063f1782b.jpg)  
Figure 2b An enriched data oriented view of the system development process

Hoffer, 1988) can be used to synthesize the two resultant models;

(2) The inclusion of structured process models, in the form of Petri nets, as a rigorous means of representing the functional decomposition activity;

(3) The taxonomy of the process which indicates that both functional decomposition and structured process models represent reality, whereas the data models, algorithm and database descriptions represent the information system.

Any representation of the reality depends upon some method for categorizing and defining what is being observed in a given situation. For example, for any situation being observed it may be desirable to categorize items as entity types or processes. During the observation, all phenomena and their most obvious situation-related processes are then classified. For instance, in a 'vehicle rental' situation, a customer and a vehicle would be classified as entity types. This method, with some variations, has been described as an object-oriented approach to systems analysis, (Bailin, 1989). In ERMs entity types may be people, objects or events. In structured process modelling the emphasis is more on processes which relate to the dynamics of information in reality. Using this method, the reality of the situation being observed can be described in terms of its data and processes. The next step is to produce an ERM and DFD as shown in Figure 3.

Whilst this approach has proved successful over a wide range of applications, the link between the functional decomposition model and the ERM/DFD is considered to be weak. That is to say the transformation from one to the other depends greatly upon the knowledge, experience and intuition of the system developer. It is therefore proposed that some more rigorous intermediate step is needed to strengthen the interface between the two models. The intermediate step suggested here is the use of rigorous state/transition nets, and in particular, Petri nets. These are described later in the paper.

The next weak link identified in this process definition is that between ERMs and DFDs. This paper proposes the use of LAMs as a means by which the two models can be synthesized to provide a more rigorous model than is currently available. LAMs represent the database interactions necessary to support processes acting on data. This representation utilizes components of the ERMs from which database structures are derived. Given that DFDs represent the flow of data between processes in the information system, then LAMs have the potential to help identify any inconsistencies between a DFD and the associated ERM.

![](/api/attachments/JEBGMVN9/fulltext/images/7c7f88169cfee0557b3fce5b9d69e7f2b38d4fcf4b9e3ce84d91530235d76b1b.jpg)  
Figure 3 A new conceptual model of the system development process

## Introduction to the modelling techniques

## Petri Nets

Petri nets, (Symons, 1982) are a scientific and mathematical tool to study systems and processes. Systems fundamentally have components and these components have states. A component may in fact be an entire system made up of other components, but its modus operandi can be described independently of the components. The state of a component is a representation of the relevant information describing its actions, whether past, present or future. These components may occur concurrently, in parallel or serially.

Petri nets (Pns) are designed to model these systems, i.e. processes with interacting concurrent components. First, Pns are used as an auxiliary analysis tool. The system is modelled as a net and the net is analysed. The model is modified to correct any known short fall in design. The system may then, via the Pn, be analysed and understood. Second, and more radical, is the concept of the design and specification of a process entirely in terms of Pns, a notion advocated in this paper.

Petri net theory was developed by Dr Petri in his 1962 PhD thesis (Petri, 1962). The theory of Pns is based on bag theory, which is an extension of set theory (Peterson, 1986). A bag, like a set, is a collection of elements which belong to, and are wholly contained in, a domain. In bag theory, however, elements may have multiple occurrences. In set theory an element is or is not a member of a set, and never a member of more than one set at the same time (the exception being disjoint sets). For a bag, an element may not exist, may exist once, or may exist any specified number of times. This definition does not exclude a bag from being, in the limiting case, a set.

The properties and characteristics of Pns are such that they are very suitable for the representation and analysis of the flow of control and data information in systems, especially those systems which are composed of communication subsystems which operate asynchronously and concurrently. Pns can be related to physical systems in several ways, but the simplest way is for the presence of a 'token' in a 'place' (or state) to represent the holding of a particular 'condition', and for the 'firing' of a 'transition' to represent the occurrence of an event enabled by the holding of the condition. Pns, historically, did not consider time. However they have been developed to a level where certain 'tokens' can be created which represent time, cost and/or resources. When the firing of 'transitions' in a Pn represents events which occur in a physical system, a dynamic graphical representation shows the behaviour of the system under all possible and probable combinations of events.

Owing to their ability to represent concurrency, Pns have been widely used by computer scientists to model concurrent and parallel programs (Krishnamurthy, 1989). The main motivation has been to provide models which could assist in the understanding and solution of problems associated with concurrency, such as deadlocks, competition for resources, synchronization, mutual exclusion and critical races (Symons, 1982, p11).

## Coloured Numerical Petri nets

Coloured Numerical Petri nets (cnPn) are claimed to be the true generalization of Pns and are better equipped to model practical systems. Each 'transition' has an enabling condition and firing rule for each colour of 'token' associated with the 'transition'. The 'tokens' have the following characteristics and may represent any attribute in a process:

(1) They may have any nature and value;

(2) The enabling and firing conditions are independent of each other;

(3) The ‘transition’ enabling conditions refer to both ‘tokens’ from input places, firing ‘tokens’ into output places, and operations on ‘transition’ memory data;

(4) They are removed from the input places according to the relevant firing rules;

(5) They are received into the output places according to the relevant firing rules;

(6) Only one ‘transition’ in a net may fire at a time; if more than one ‘transition’ is enabled, the ‘transition’ to fire is chosen at random from a set of enabled ‘transitions’;

(7) 'Tokens' can have any number of attributes, which may or may not change during a 'transition';

(8) The collection and distribution of the ‘tokens’ in a net define the net’s marking.

![](/api/attachments/JEBGMVN9/fulltext/images/367f5c1a8a2932bd10824942e61de8e7021529e86cfe273e1885b37617657164.jpg)  
Figure 4 Basic semantics of a Petri net where $\bigcirc =$ place; $-\text{—} =$ transition; $\blacksquare \bullet =$ tokens; $\square =$ timed transition; $\blacklozenge =$ direction arc; E1 and E2 = enabling rules; F1 and F2 = firing rules.

Figure 4 is typical of a simple cnPn. Without colour the 'tokens' have been shown by different shapes. 'Places' correspond to system states, (Marco and Buxton, 1987) and are usually the static components of a system (De and Sen, 1984). These 'places' have information attributes attached to them. 'Transitions' (or events by De and Sen, 1984) are happenings in a process and connect (or transform) information (or data) from place to place. While 'transitions' have been traditionally considered as atomic, this restriction need not apply in the more general case. Timed 'transitions' are not only possible but desirable.

The markings reached can then be studied to determine deadlocks and the net's efficiencies which could be in terms of time, cost and/or resources. The time, costs and resources may be logged through the life cycle by appropriate 'tokens'. Although not portrayed in Figure 4 some markings may be unreachable, i.e. a particular net configuration is impossible. Some 'places' may be unreachable due to the initial arrangement of 'tokens' and/or the enabling and firing rules.

## Entity Relationship Model

The ERM was first proposed by Chen (1976) as a means of obtaining a unified view of data. At that time a method of obtaining a logical view of data was becoming increasingly important and Chen aimed to provide a framework from which each of the three existing data models – the network model, the relational model and the entity set model – could be derived. Following Chen's paper, many researchers have embraced the concept and various modifications and extensions have been proposed in order to make the ERM semantically richer (see for example Chen, 1980; Chen, 1983; Chen, 1985; Spaccapietra, 1987; March, 1988; Finkelstein, 1989).

The principal characteristic of ERMs is that they are developed independently of the physical structure in which they will be stored. This means that the modeller is primarily concerned with developing an appropriate representation of reality from the point of view of the user(s) of the data. Assumptions as to what is an appropriate representation of reality can be built

![](/api/attachments/JEBGMVN9/fulltext/images/f529fbd471dcb4a4c54bdae8fc4dacc1b36ef3806b7103fb308b328a6a4e2c8b.jpg)  
(a) The relationship from A to B is of degree 1:1

![](/api/attachments/JEBGMVN9/fulltext/images/19cac9150c6d381e72f810ae19377e81ae6098abe2b7749339291816b9a2156b.jpg)  
(b) The relationship from A to B is of degree 1:n

![](/api/attachments/JEBGMVN9/fulltext/images/3dc3ba36ced9f4522c504447af7bce7af7d1aa5fa918a167f91b1972d2ddabf8.jpg)

(c) A has an optional relationship with B. (i.e. an instance of A may exist without an associated B.)

![](/api/attachments/JEBGMVN9/fulltext/images/89e9dd1314a9f111187d0a35b6cdb08a608eb4871d124737f0b23f640b9a4c7e.jpg)  
(d) A has a mandatory relationship with B. (i.e. an instance of A must have one associated instance of B.)

into the model and the data modeller can then verify the assumptions or modify the model as necessary. The model should therefore, at any point in time, represent the modeller's current understanding of reality. This characteristic, combined with the fact that an ERM is able to be implemented in any one of the major physical database models, has gained the ERM extremely wide acceptance as an analytical tool.

Using the ERM, a data model will at least represent the existence of relationships between entity sets. A relationship can be specified in terms of the following properties which provide essential input for the development of a database schema:

(1) Whether participation by specific entities within each of the participating entity sets is optional or mandatory; this characteristic will be termed relationship participation;

(2) The cardinality or degree of the relationship indicates the number of such relationships in which specific entities within each of the participating entity sets may appear.

In general, the nature of relationships can vary, e.g. one to one (1:1), one to many (1:n), many to one (n:1) or many to many (n:m). Figure 5 illustrates the diagram techniques used here for representing relationships in terms of these two properties. The concept of entity sub-types, (Ferguson, 1988) is also illustrated in Figure 5. The techniques adopted here are adapted from those proposed by Finkelstein (1989).

Figure 5 ERM diagram techniques  
![](/api/attachments/JEBGMVN9/fulltext/images/c02f7765b5dc5a67c5fe24dbacce83ea846eae5597d3516cba07bcdc5c2d66b7.jpg)  
(e) A has a 1:n relationship with B. Furthermore, the vertical line shows that at least one instance 0 exists (i.e. there may be one or many of B) for each A, and the circle shows that there is optionally instance of A associated with each B (i.e. there be zero or one A for each B).

![](/api/attachments/JEBGMVN9/fulltext/images/3329de79ed7a75cbad506d874256c22f7a19af9bcf1ca8f1d79902c7e8ae3d5f.jpg)  
(f) B and C are sub-types of A. This means that they are of the same basic entity-type, but they also each have their own characteristics which are relevant only to the particular subset.

Representing the cardinality and participation of relationships facilitates the development of normalized ERMs from which sets of relations conforming to the relational integrity rules (Date, 1990) can be derived. There are however, various semantic characteristics of data relationships which can also be modelled, thereby enriching the model both as a database design technique and as a means for representing reality. A data model should also include the specification of relevant attributes of entities. Obviously, this is essential if the database structure is to effectively support information requirements. For the data modeller, there is a very pragmatic reason for defining attributes early in the modelling process, e.g. analysis of attributes provides insight to the semantics of data relationships. Part of the process of attribute analysis is the designation of primary key attributes for each entity, which, in turn, enables relationships between entities to be represented by foreign keys.

## Data Flow Diagrams

The data flow diagram (Gane and Sarsen, 1979) is a technique for representing the flow of data between data stores, external entities (i.e. entities outside the information system) and processes in an information system. There are two potential benefits to be gained from the use of data flow diagrams:

(1) As a communication medium between systems analyst and client, DFDs can provide the means to bridge the gap between the client's and the analyst's understanding of a system;

(2) As an analysis tool, DFDs provide the means to identify which elements of a data structure will be accessed by processes.

DFDs are not directly translatable to a set of processing algorithms in the same way as ERMs are to database schemas. Gane and Sarsen (1979) advocate DFDs as an integral and essential component of the system design and that DFDs must be developed before data structure modelling can proceed. It is the authors' experiences that this is not necessarily so. ERMs and DFDs complement each other, and as implied by Figures 2a and 2b and Figure 3, the two types of models can be developed in parallel.

There are four major components of DFDs (illustrated in Figure 8 and Figure 9): data flows (represented by arrows), processes (circles), data stores (open-ended rectangles) and external entities (rectangles).

## Illustrative example

Having now discussed the modelling techniques the following example is used to develop the connection between ERMs, DFD and Petri nets (as illustrated in

Figure 3). Take, for example the vehicle rental business. The firm rents vehicles to customers and for each rental contract there is one customer and one vehicle involved. Customer details are recorded independently of the rental contracts as, over time, an individual customer may be involved in many rental contracts. Customer names, addresses and driver's licence numbers are recorded. Vehicle details are also maintained independently of the rental. A record of completed contracts is also to be maintained. The odometer reading is recorded at the time each rental commences and again upon completion of the contract. The dates upon which vehicles are rented and returned are also recorded for each contract.

Additional aspects of the business such as advance bookings and the transfer of vehicles between centres are deliberately omitted from the example. This simplification of the business rules is intentional so as to succinctly expose the connection between ERMs and Pns without clouding it in a complex model. The Pn of the customer-vehicle rental process is shown in Figure 6.

The net consists of the following:

(1) Places:

pl prospective customers,

p2 customers about to rent vehicles,

p3 rented vehicles index,

p4 customers using vehicles,

p5 existing contracts,

p6 contracts returned,

p7 rentable vehicles index,

p8 vehicles returned,

p9 completed contracts,

(2) Transitions:

t1 customers decide to rent,
t2 customers sign contracts,
t3 customers finish with rented
vehicles,
t4 vehicles serviced,
t5 customers settle contracts,

The nominally passive components of the net are the 'places' (represented by circles) and the nominally active components are the 'transitions' (represented by boxes) (Reisig, 1986). The net models the process by which vehicles and customers form relationships, when information is stored and retrieved and when the relationships cease. 'Place' p1 represents a set of people who may be considered to be prospective customers. After 'transition' t2 has fired a relationship, customer-vehicle, is formed. Places p3, p4 and p5 show respectively that a vehicle is rented, a customer has a vehicle and that the relationship customer-vehicle is formed via the contract. There is no conditionality on these events, therefore, until such time as there is a coloured 'token' in places p3, p4 and p5 no strong relationship can be assumed. Matching coloured 'tokens' are placed in these output places so that the customer-vehicle relationship is maintained throughout the net. The places p1 and p7 (prospective customers and rentable vehicles) could initially contain all respective occurrences regardless of whether or not they are involved in a current rental. For the initial marking, plausible limits on the number of 'tokens' have been placed on p1 and p7. For an entity-relationship diagram and the subsequent schema and database, a relationship must exist between customers and vehicles. This is reflected in places p3, p4 and p5 and the weaker relationships at places p2, p6 and p9; the latter are weaker in the sense that no physical relationship exists. That is to say, the relationship is, in the first case (p2) highly probable, the second case (p6) just about to cease and the third case (p9) recorded historically.

![](/api/attachments/JEBGMVN9/fulltext/images/65da046f3cdcef9569df68f07f87de96c6a40f2ca2ef1491d4dde9fe0ec612b8.jpg)  
Figure 6 Petri net specification for a vehicle hire service (similar to Reisig, 1986)  
Table 1 Initial marking of the Pn

<table><tr><td colspan="9">Initial marking</td></tr><tr><td>p1</td><td>p2</td><td>p3</td><td>p4</td><td>p5</td><td>p6</td><td>p7</td><td>p8</td><td>p9</td></tr><tr><td>n*</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>100</td><td>0</td><td>0</td></tr></table>

\*n indicates any reasonable positive integer

Table 2 Transition enabling rules

<table><tr><td colspan="10">Enabling rules</td></tr><tr><td></td><td>p1</td><td>p2</td><td>p3</td><td>p4</td><td>p5</td><td>p6</td><td>p7</td><td>p8</td><td>p9</td></tr><tr><td>t1</td><td>&gt;0</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>t2</td><td>-</td><td>≥1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>&gt;0</td><td>-</td><td>-</td></tr><tr><td>t3</td><td>-</td><td>-</td><td>≥1c*</td><td>≥1c*</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>t4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td></tr><tr><td>t5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>=1c</td><td>=1c</td><td>-</td><td>-</td><td>-</td></tr></table>

\*c indicates the presence of appropriate coloured tokens

Table 3 Transition firing rules

<table><tr><td colspan="10">Firing rules</td></tr><tr><td></td><td>p1</td><td>p2</td><td>p3</td><td>p4</td><td>p5</td><td>p6</td><td>p7</td><td>p8</td><td>p9</td></tr><tr><td>t1</td><td>-1</td><td>+1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>t2</td><td>-</td><td>-1</td><td>+1c*</td><td>+1c*</td><td>+1c*</td><td>-</td><td>-1</td><td>-</td><td>-</td></tr><tr><td>t3</td><td>-</td><td>-</td><td>-1c*</td><td>-1c*</td><td>-</td><td>+1c*</td><td>-</td><td>+1</td><td>-</td></tr><tr><td>t4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>+1</td><td>-1</td><td>-</td></tr><tr><td>t5</td><td>+1 $^{5}$ </td><td>-</td><td>-</td><td>-</td><td>-1c*</td><td>-1c*</td><td>-</td><td>-</td><td>+1</td></tr></table>

\*c indicates the presence of appropriate coloured tokens

Tables 1, 2 and 3 respectively show the initial marking, the enabling rules and the firing rules for the Pn. The Tables have been abbreviated from the conventional ones for the sake of space. It is customary to tabulate such information separately for all coloured 'tokens' in the net.

The ERM corresponding to this example is given in Figure 7. There are three main entities in Figure 7: customers, vehicles and rental contracts. The diagram is read as follows: for each member of the entity-set customer, there may be one or more occurrences of the entity rental contract. Conversely, each rental contract is associated with only one customer. Each rental contract will be either a current contract or completed contract (membership of these two subsets is mutually exclusive for rental contracts). The subsets current contracts and completed contracts each pertain to one and only one vehicle. A vehicle can be related to, at most, only one current rental, whereas it can be related to any number of completed contracts.

The entity-set rental contracts is divided into two entity sub-types for two reasons. First, completed contracts have the additional attributes end-odometer (for the odometer reading at the completion of a contract), cost and date-paid. Second, the relationship between vehicles and current rentals is of a 1:1 relationship and individual current contracts mandatorily participate in such a relationship, whereas the relationship between vehicles and completed rentals is 1:n with completed contracts optionally related to vehicles (because details of completed contracts will be maintained even upon disposal of vehicles).

## Synthesis of the modelling techniques

Consider now the connection between the Pn representation of the business and the ERM. Place p2 in the Pn corresponds to the customers entity, places p3, p7 and p8 correspond to the vehicles entity and places p5 and p9 correspond to the current contracts and completed contracts entities respectively. Note that the different places corresponding to the vehicles entity indicate that vehicles could also be divided into sub-types on the basis of whether or not they are currently on hire. In this case, under the assumption that currently hired and currently available vehicles have all other attributes in common, a design decision has been made to use the attribute status of vehicles to indicate whether vehicles are currently on hire.

![](/api/attachments/JEBGMVN9/fulltext/images/caf9ea80e56d1a9bea1737f5743e473504cdc99673e7054eb897fcf9bbd63e3b.jpg)  
Figure 7 ERM for vehicle service

The existence of relationships between entities may not be so readily identifiable from a Pn in the absence of coloured 'tokens'. As previously stated, the presence of 'tokens' in places can indicate the existence of relationships between entities. Therefore, until a Pn is analysed to determine the possible markings, it cannot be used to directly derive relationships between entities. Another pertinent point is that there is evidence of some connection between 'tokens' in a Pn and attributes in an ERM. This, juxtaposed with the fact that attribute analysis provides insight to the relationships in an ERM, adds weight to the contention that the derivation of ERM relationships from a Pn is dependent upon an analysis of the marking of 'tokens' in the Pn. While it has been demonstrated that there is, prima facie, a connection between places, 'transitions' and 'tokens' on the one hand and relationships, entities and attributes on the other hand, the derivation of relationships and attributes from Pns is the subject of ongoing research.

It is therefore concluded that Pns are a valid precursor to ERMs and furthermore they are rigorous and capable of validation.

Figure 8 is the level 0 DFD of the vehicle rental information system. Comparing the DFD processes to the Pn transitions, it can be seen that these processes are readily derived from the Pn – although a one to one correspondence between DFD processes and Pn transitions does not exist. The level 1 DFD of the hire out vehicle process is given in Figure 9. In this instance there is no apparent analogy between the DFD processes and the Pn transitions. This is partly because the Pn represents the view of the customers as well as that of the company. Also, data processing functions at a detailed level correspond to the firing of transitions and thus to changes in the markings of the Pn. Analysis of the transition enabling and firing rules, markings of the Pn and the nature of the tokens will provide insight to the data processing functions. This issue is the subject of further research.

![](/api/attachments/JEBGMVN9/fulltext/images/49792c95ba99277bae5cc11e5cb4312953d9c7bb2f28f35507b149de76629cf1.jpg)  
Figure 8 Level 0 DFD for vehicle rental system

## Verification of the proposal

Figure 10 is presented as an alternative way of explaining the concept. Reality is modelled via ERM and the resultant conceptual schema is used to develop a database. Petri nets may be seen as an alternative or parallel modelling technique. This hypothesis should be capable of being tested and Figure 10 is a representation of this concern.

![](/api/attachments/JEBGMVN9/fulltext/images/3c57dfb735dbbea1fd4e87930babe787127af7f2e30f40fd41dddf9ad9a904fd.jpg)  
Figure 9 Level 1 DFD for 'hire out vehicle' process

The definitions are as follows:

$E_{n}$ = the error associated with a particular model abstraction.

$\Sigma_{n} =$ the resources (information, data, people, time, etc) required to perform the abstraction.

$\delta \Phi_{n} =$ the change in functionality of a model.

![](/api/attachments/JEBGMVN9/fulltext/images/02b377b4dea760e9988cbff8d876626b5b353dfb2bc2197e5087700b25a851cf.jpg)  
Figure 10 Model linkage and functionality where E3, $\Sigma 3$ , $\delta \Phi 3 =$ measure of modelling errors, resources and functionality; $\rightarrow =$ existing and proposed model linkages; $-\rightarrow =$ conceptual model linkage; DATA BASE = model type

This new model can be validated if some values (and variance) can be attached to $E_{n}$ , $\Sigma_{n}$ and $\delta\Phi_{n}$ . Regardless of the values, for an improvement it shall be true that

$$
[ (\mathrm{E} _ {2}) + (\mathrm{E} _ {4}) + (\mathrm{E} _ {3}) ] _ {\mathrm{T}} <   [ (\mathrm{E} _ {1}) + (\mathrm{E} _ {3}) ] _ {\mathrm{T}}
$$

$$
[ (\Sigma_ {2}) + (\Sigma_ {4}) + (\Sigma_ {3}) ] _ {\mathrm{T}} <   [ (\Sigma_ {1}) + (\Sigma_ {3}) ] _ {\mathrm{T}}
$$

$$
\text { and } \left[ (\delta \Phi_ {2}) + (\delta \Phi_ {4}) + (\delta \Phi_ {3}) \right] _ {\mathrm{T}} <   \left[ (\delta \Phi_ {1}) + (\delta \Phi_ {3}) \right] _ {\mathrm{T}}
$$

In other words, it shall be true that at epoch T

(1) The sum of the errors of the new model linkages shall be less than the old;

(2) The sum of the resources of the new model linkages shall be less than the old;

(3) The functionality of the new modelling system shall be greater than the old.

The concept of time is introduced to reflect that no system is static and developments to include Pns and integrate CASE may be matched by concurrent improvements in existing systems development techniques.

## Conclusion

The authors are singularly and collectively researching the matters raised in this paper. Special emphasis is being devoted to the application of rigorous modelling of information processes, the relationship between Pns and ERM, the establishment of an integrated CASE tool using ERMs, DFDs and LAMs, and the determination of the variables shown in Figure 10 and the resultant verification of the proposed improvements.

The SDLC has been re-defined here to represent the reality of the transition from a functional specification to a database definition and processing description. ERM and DFD techniques have emphasized the data driven development process, with the optimizing influence of logical access mapping techniques. Petri nets have provided a new dimension for development control and a modelling mechanism which incorporates these other methods. This combinatorial approach has provided the basis for a means of formally proving the validity of data models and a way of identifying logic and data relationship errors.

## Acknowledgements

The authors wish to thank their colleagues for assistance, with particular reference to Mr Andrew Turk (Department of Surveying and Land Information, University of Melbourne) for his contribution to the concepts represented in Figure 10.

## References

Bailin, S.C. (1989) An object-orientated requirements specification method, Communications of the ACM, 32, 5.

Chen, P.P. (1976) The entity relationship model - toward a unified view of data, ACM Transactions on Database Systems, 1, 1.

Chen, P.P. (1980) (ed) Entity relationship approach to systems analysis and design, in Proceedings of the International Conference on E-R Approach to Systems Analysis and Design, North-Holland, Los Angeles.

Chen, P.P. (1983) (ed) Entity relationship approach to information modelling and analysis, Proceedings of the 2nd International Conference on E-R Approach to Systems Analysis and Design, North-Holland, Washington.

Chen, P.P. (1985) (ed) Entity relationship approach – The use of E-R concept in knowledge representation, in Proceedings of the 4th International Conference on E-R Approach to Systems Analysis and Design, North-Holland, Chicago.

Date, C.J. (1990) An Introduction to Database Systems (5th ed.), 1, Addison-Wesley, Reading, Massachusetts.

De, P. and Sen, A. (1984) A new methodology for database requirements analysis, Management Information Systems Quarterly, September, 179–193.

Ferguson, J.R. (1988) Data modelling and systems analysis, in Proceedings of the 19th Colleges of Advanced Education Computing Conference, Australia.

Finkelstein, C. (1989) An Introduction to Information Engineering, Addison-Wesley, Sydney.

Gane, T. and Sarsen, C. (1979) Structured Systems Analysis, Prentice-Hall, Englewood Cliffs, New Jersey.

Krishnamurthy, E.V. (1989) Parallel Processing, Principles and Practice, Addison-Wesley, Sydney.

Lucas, H.C., Jr, (1985) The Analysis, Design and Implementation of Information Systems, (International Student Ed) McGraw-Hill, New York.

Mantha, R.W. (1987) Data flow and data structure modeling for database requirements determination: a comparative study, Management Information Systems Quarterly, December, 531–544.

March, S.T. (1988) (ed) Entity relationships approach, in Proceedings of the 6th International Conference on E-R Approach to Systems Analysis and Design, North-Holland, New York.

Marco, A. and Buxton, J. (1987) The Craft of Software Engineering, Addison-Wesley, London.

McFadden, F.R. and Hoffer, J.A. (1988) Database Management (2nd ed.), Benjamin Cummings, California.

Necco, C.R., Gordon, C.L. and Tsai, N.W. (1987) Systems analysis design: current practices, Management Information Systems Quarterly, December, 461–475.

Peterson, J.L. (1986) Petri Net Theory and the Modelling of Systems, Prentice-Hall, New Jersey.

Petri, C.A. (1962) Communications with Automata,

Supplement 1 to RADc-TR-65-377 Vol. 1, Griffiss Air Force Base, New York, 1966. – Originally published in German ‘Kommunikation mit Automaten’, University of Bonn.

Reisig, W. (1986) Petri nets: applications and relationships to other models of concurrency, advances in Petri nets 1986, Part II, in Proceedings of an Advanced Course Bad Honnef, Springer-Verlag, 63–96.

Sallis, P.J. (1988) Quality assurance and productivity enhancement, in Proceedings of The Rutherford Conference, (New Zealand Computer Society Bi-Annual Conference), New Zealand Computer Society, New Plymouth.

Sallis, P.J. (1989) Integrating computer aided software engineering tools with a generalised information system development methodology, in Proceedings of the 11th New Zealand Computer Society Computer Conference, New Zealand Computer Society, Wellington, 589–596.

Spaccapietra, S. (1987) (ed) Entity relationships approach, in Proceedings of the 5th International Conference on E-R Approach to Systems Analysis and Design, Dijon, North-Holland.

Symons, F.J.W. (1982) The application of petri nets and numerical petri nets, Technical Report 7520, Telecom Australia Research Laboratories, Clayton, Victoria.

## Biographical notes

George L. Benwell is a Senior Lecturer in Information Science at the University of Otago, New Zealand. He joined the Department in January 1990 after more than a decade of lecturing in the Department of Surveying and Land Information at the University of Melbourne. He holds a BA in Surveying from The University of Melbourne, an MPhil from The City

University, London and is currently undertaking a PhD at the University of Melbourne in 'Rigorous modelling of spatially referenced information processes using numerical petri nets'. He has published many articles on surveying matters and more recently on geographic information systems.

Peter Firns is a lecturer in Information Science at the University of Otago, New Zealand. He holds a B.Comm in Information Systems and is currently studying for a PhD in Information Science. His doctoral research is in the area of data modelling and the specification of CASE tools for spatial database design. Peter's teaching interests include fourth generation system development techniques, data modelling and project management. He has regularly undertaken consulting assignments and professional development courses relating to his areas of teaching and research.

Philip Sallis is Foundation Professor of Information Science at the University of Otago, New Zealand. He has a BA in Computer Science from Victoria University, Wellington and a PhD in Information Science from The City University, London. He has held academic positions in England, Australia and New Zealand. He is well known as a conference speaker and consultant in the areas of data modelling and database design, fourth generation languages and software engineering. In addition to these topics he has published articles on natural language processing and expert systems.

Address for correspondence: George L. Benwell, Dept. of Information Science, University of Otago PO Box 56, Dunedin, New Zealand.
