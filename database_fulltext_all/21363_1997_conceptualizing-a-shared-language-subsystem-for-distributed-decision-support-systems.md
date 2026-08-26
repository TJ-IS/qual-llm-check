---
otero_id: 21363
otero_key: "8YNMN4FR"
title: "Conceptualizing a shared language subsystem for distributed decision support systems"
authors: "Shawn D Bird"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00049-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Conceptualizing a shared language subsystem for distributed decision support systems

Shawn D. Bird

Advanced Technologies Group, CAP Gemini America, 1001 Fourth Avenue Plaza, Suite 3120, Seattle, WA 98154, USA

## Abstract

Researchers have only recently begun to develop formal architectures for support systems that capitalize on advancements in distributed technologies. Conceptual models have been proposed for distributed versions of both DSS and GDSS. To date, however, these developments have largely been limited to techniques employing shared global data spaces. Research on other approaches to distributed support systems development, including that based on the shared language techniques of distributed artificial intelligence, is still lagging. To introduce this research area, this paper reviews architectural principles for distributed decision support and develops the notion of a shared language as an extension of the DSS language subsystem. © 1997 Published by Elsevier Science B.V.

Keywords: DSS; Distributed DSS; Architecture; Distributed artificial intelligence

## 1. Introduction

From its local-system, single-user beginnings, decision support technologies have begun to evolve into distributed, multi-user architectures. This extension of support systems to the inherently distributed decision making activities of the modern organization is motivated by a desire to realize advantages of shared data, models, and knowledge as well as those of communication and distributed coordination.

Interestingly enough, this idea has been around since the earliest days of DSS. One of the first descriptions of distributed DSS is that of Sprague and Carlson, the DSS Network Architecture:

"The DSS network architecture... is perhaps the most adaptive approach to component integration. The primary goals of the network approach are to permit different modeling and dialog components to share data and to simplify addition of new components. The architecture permits the components to be nonhomogeneous. That is, the architecture is designed to permit intermixing of components developed by different groups, at different times, in different programming languages, and for different operating environments' ([49], pp. 280-281).

Though not yet achieving this level of functionality, the emergence of new tools and techniques has made the goal of developing the “DSS network architecture” ever more realizable. The direct application of new tools and techniques to distributed and decentralized organizational structures provides among the latest challenges to support systems researchers. More recent definitions include Distributed Decision Making Systems [10], Distributed DSS [50], Distributed GDSS [28], and the inherently distributed Organizational Decision Support [21] and Organizational Activity Support [12] Systems.

Yet, and despite that many conceptual architectures and frameworks have been proposed for this new generation of support system technologies, the mechanisms by which distributed decision support may be achieved have not been developed much beyond global data space techniques. This paper presents shared language as an alternative to shared data space techniques by conceptually extending the DSS language subsystem to distributed environments.

The next section briefly outlines the need for a distribution of the traditional DSS components: the problem processing, knowledge, and language subsystems. The third section then develops a framework for distributed DSS based on a shared language implementation. Finally, a summary and conclusions are presented.

## 2. Distributed support systems

Although a great many extensions have been made to the basic support system concept, the core of the DSS family of technologies has remained essentially a tripartite architecture. In fact, the generalized intelligent decision support system proposed by Bonczek et al. [7,8], as in Fig. 1, remains the canonical architectural reference and the typical starting point for conceptual developments in the field of DSS.

Across its many extensions, the three subsystems illustrated in Fig. 1 provide the same basic capabilities to all members of the DSS family:

\- the problem processing subsystem supports problem recognition and model formulation, the collection of data, and data analysis,

\- the knowledge subsystem captures and applies systematically organized knowledge about one or more problem domains,

![](/api/attachments/8YNMN4FR/fulltext/images/177034b6cac7ae250d2444007882bd806400ca66efcaaf877e3ec9acbb252fa9.jpg)  
Fig. 1.

\- the language subsystem handles communications between the user(s) and the system.

## 3. Distributed problem processing subsystem

Models give decision makers an ability to analyze problems by developing and comparing alternative structures [49]. A key element of the problem processing system is then a model management function, as formalized within a model management subsystem:

“...a model management system makes it easy for a user to assemble information from a variety of sources and thus, allows the user more flexibility in identifying and solving problems” ([5], p. 69).

Although this, and virtually every other published description of model management identifies potentially many “sources” for the construction of decision models, those sources have generally resided within a single support system. That is, few of the published enhancements to the basic concept of the model management system (cf. [33]) provide for multiple, heterogeneous external sources of modeling constructs, despite that model management has been, and continues to be a rich area of DSS investigation.

Blanning further notes that the purpose of a model management system is to “insulate the users of a DSS from the physical aspects of model storage and processing” ([6], p. 10). Thus, the model management subsystem performs an essential abstraction function that must be maintained when extended to distributed environments. Although some research has begun to address this issue in GDSS [31,32] and environmental scanning [18], those extensions are perhaps more accurately decentralized systems. That is, popular support technologies based on global data structures, or blackboards (cf. [42]), are often distributed only in a limited sense.

## 4. Distributed knowledge subsystem

Architectures for the distribution of the knowledge subsystem are similarly few in the literature.

The distribution of knowledge is, however, well researched in the field of distributed artificial intelligence (DAI) [20,9,16,48]. Consequently, many concepts from DAI can be directly applied to distributed DSS [46]. As an illustration, one framework defined for networked knowledge-based systems [27] was also recast for application to distributed GDSS [28].

One emerging DSS problem to which DAI concepts may well apply is the typical assumption of homogeneity among knowledge bases. With few exceptions, knowledge-base enhanced conceptual models of DSS have supported a singular, homogenous knowledge repository. Courtney et al. [15], in contrast to this trend, conceptualized a model with two separate knowledge bases, but did not include a management system for those knowledge bases. More recently, Rao et al. [42] proposed and simulated an IDSS architecture with multiple, loosely coupled knowledge sources coordinated by a blackboard. Yet neither of these, nor any other widely published DSS paper explicitly addresses the problems of knowledge base heterogeneity. The heterogeneity of distributed knowledge bases is critical in distributed AI, and is similarly critical to the development of truly distributed DSS.

## 5. Distributed language subsystem

The third basic component of the DSS architecture is designed to handle human-computer and, in agent architectures, computer-computer interaction. Bonczek et al. offer a good working definition of this subsystem: a language system is the sum total of all linguistic facilities made available to the decision maker by a decision support system ([7], p. 617). The language subsystem can be “characterized by the syntax that it furnishes to the decision maker and by its statements, commands, or expressions that it allows the user to make” ([45], p. 22).

The distribution of the language subsystem has, as yet, to be developed in the published DSS literature. As above, however, DAI offers a valuable source of concepts for distributed DSS because communication is the foundation of a great deal of DAI research. One immediate extension that can be made from DAI to DSS is, as hinted at above, the interpretation of distributed DSS as a limited type of “multi-agent” system.

Supporting both this interpretation and, more directly, the shared language notion is the multi-agent system taxonomy defined by Bird [4]. That paper defines the taxon “Multi-Agent Language Systems” as a collection of potentially heterogeneous, machine-based knowledge sources that are globally controlled by a single agent through local interfaces using a common interaction language as the integration mechanism. This architectural description provides a ready definition for shared language, distributed DSS: a collection of decision support tools with potentially heterogeneous components that are globally controlled by individual users and agents through local interfaces via a common interaction language for data, model, and knowledge sharing. The development of such a language is a promising research area.

## 6. Conceptualization of a shared language distributed DSS

To realize the distributed counterparts of traditional DSS subsystems like those presented above, underlying principles must first be developed: architectural layering, functional models of interaction, and requisite multi-system language capabilities. To better focus the discussion of these principles, a conceptual architecture integrating these three elements is illustrated in Fig. 2.

Starting at the level of computational abstraction in Fig. 2, computational primitives, data types, and data, model, and knowledge structures abstract away the details of hardware, operating, and programming environments. Moving to the next level of abstraction, knowledge and models are then readily manipulated and applied to problems. This follows the AI-enhanced tradition of model management (cf. [17]). The final layer, the communication level abstraction, represents both a variety of media and an extensible common language that embodies a conversational interaction metaphor. These principles – layering, interaction/communication, and language – and related elements of the architecture are discussed in depth in the sections that follow.

![](/api/attachments/8YNMN4FR/fulltext/images/5a135d66676adabb7d372b5ed8853b38a6058e697fc589a9deb7247aca854529.jpg)  
D0 & D1: procedures by which agents interact and understand each other.  
$p0^{i}$ : procedures that interface agent problem processing systems to the world.  
p1 $^{i}$ : agent meta-procedures that interpret and provide an understanding of the world.

Fig. 2.

## 6.1. Layering

The essence of the layered architecture is that it provides a conceptual means by which patterns of successive function reimplementations can be identified to facilitate the isolation of particular characteristics $[3]$ . Perhaps no area better demonstrates the need for, and utility of layered architectures than data communications. In this field, heterogeneous computing platforms are networked using layered frameworks such as the OSI seven-layer reference model.

Underlying layered implementations is a strategy of insulating successively higher layers from the physical and logical characteristics of lower layers. The ultimate goal when applied to intelligent support systems is then to separate both data and knowledge manipulation, as well as modeling from the representational structures and techniques employed in their definition and utilization. Two benefits emerge from this layered conceptualization:

\- each layer can have many independent implementations that are transparent to other layers,

\- complete layer implementations can be replaced or used interchangeably as the technologies of those layers develop.

In DSS, as in other computer-based technologies, the lowest level is that at which the computational hardware exists. Different hardware platforms necessarily have different physical characteristics. One level of abstraction beyond hardware is a Computational Level of Abstraction, introduced in Fig. 2 by a Primitives layer. This layer concerns the lowest computational elements: bits and bytes. Modern programming tools insulate the programmer from computational primitives by defining basic data types within each language. In Fig. 2, this layer is referred to as the Data Types layer.

To insulate developers and users from needing to explicitly know and manipulate memory locations, development tools also provide a layer of abstraction between the memory space allocated for data and the manipulation of values in that memory space. This abstraction occurs in the form of simple variables, data structure variables, and abstract data types. Utilizing variables, a developer manipulates labels, or symbolic references to memory space. This layer is referred to as the Data / Knowledge Structures layer in Fig. 2. At this level both knowledge representation and model structures are defined.

In this view, knowledge is independent of the symbol level at which it is defined [34,35], and modeling is independent of its machine-usable structures [6]. Knowledge representation schemes and modeling formalisms, which exist at the data/knowledge structures layer, are then logically independent of system knowledge and models, as represented at the Knowledge and Modeling Level of Abstraction.

Finally, the Communication Level of Abstraction in Fig. 2 provides the essential ability to isolate the physical detail of communication media and protocols, allowing distributed components to be focused on the means of interaction as well as on the content of exchange. Evidence for this need is, again, perhaps best demonstrated by the area of data communications in which applications on heterogeneous computing platforms are coupled using a variety of layered frameworks (cf. [24]).

To achieve the level of logical independence advanced here, communication channels must necessarily be considered beyond their physical and functional attributes. Fortunately, some DSS-focused work has been done in this area. Pendergast, for example, provides some direction by outlining requirements that are “vital to the successful implementation of [group support systems] applications” ([40], p. 29). Those requirements include broadcast transmission, asynchronous messaging, dynamic multicasting, and session management and control.

## 6.2. Interaction / communication

Implicit in many models of human-machine interaction is a theory of conversation, the thrust of which is that meaning exchange underlies all interaction. The seminal work in conversation theory emerged from the research of Pask $[37–39]$ , who applied a cybernetic perspective to the construction of adaptive learning devices $[36]$ . Pask found that, for learning to occur, at least two levels of processing are required: one to interface with the external world, the other to actively modify interface procedures. Coombs and Alty $[14]$ later provided a representation and investigation of this learning structure for expert system dialogue development. An enhanced version of the Coombs and Alty model suitable for distributed DSS is illustrated in Fig. 3.

In Fig. 3, rectangles represent a domain over which multiple processors, $A_{i}$ , share basic knowledge. Within each processor's representation of this shared knowledge domain, $p0^i$ represent sets of procedures by which interaction occurs between the representation of the domain and the environment. Associated with these, the $p1^i$ represent meta-procedures by which each processor builds, rebuilds, and reinterprets lower-level procedures. Finally, D0 and D1 represent procedures between interacting processors at both the procedural and meta-procedural levels. Within this basic model, multiple “processors” can not only interact with the world, but also interact with, understand, and learn from each other.

![](/api/attachments/8YNMN4FR/fulltext/images/4074e9dad606688f50274aa398fa166538b7dc674e1a73bac03a186ae89b272a.jpg)  
Fig. 3.

As developed, this notion of conversational interaction explicitly embodies concepts of understanding, memory, and explanation [37,14]. “Conversations” between processors, both human and machine, are interpretable as a series of exchanges concerning some topic defined by a set of connected assertions embodying a formal interpreted relationship and a mutually shared, revisable interpretation context [14].

Note that the syntax of inter-processor conversations must be defined through a common language; the medium for conversation is provided through some layered communication framework. Via the processes of communication – in which conflict is resolved by negotiation [16] or similar – processors reach an understanding for the exchange of knowledge and coordination of problem solving activities. Anecdotal and empirical evidence provide a great deal of support for this form of interaction between humans and (semi-)intelligent machines [2,13,14,11,52].

Also note that the basic forms of organizational learning [25] are similarly captured by this model. Cogential learning takes place through the formation of a problem-solving system from the set of processors. Vicarious learning takes place when one processor learns from the knowledge of another via the D1 and D0 procedures. Perhaps more importantly for distributed DSS, learning can also occur through grafting, a process by which new processors are added to the group of available “experts”. Finally, experiential learning is acquired as the processors interact with the world and each other.

As a final note, this section has presented only one model of human-machine interaction. A great many others suitable for the task certainly exist! The point that must be reemphasized, then, is that models of interaction between distributed human and machine processors demand capabilities of this nature. Human-computer interaction is increasingly recognized as a complex process demanding layered techniques (cf. [23,51]) based on two-way interaction [22] that incorporates cognitive(-like) aspects of learning, concept refinement, and interpretation or evaluation of often imperfect, conflicting, or incomplete information (cf. [41,19]).

## 6.3. Language considerations

A fundamental requirement for any multi-system language is the definition of a shared name space – not to be confused with a shared data space – across all component systems. In multi-database environments, for instance, this means defining a common name space across all participating schemata [26].

```txt
I. Schema Conflicts
A. Table-versus-table
1. One-to-one tables
a. Table names
b. Table structures
c. Table constraints
2. Many-to-many tables (as above)
B. Attribute-versus-attribute
1. One-to-one attributes
a. Attribute names
b. Default values
c. Attribute constraints
2. Many-to-many attributes (as above)
C. Table-versus-attribute (as above)

II. Data Conflicts
A. Wrong data
1. Incorrect data
2. Obsolete data
B. Different representation for the same data
1. Expressions
2. Units
3. Precision
C. Same representation of different data (as above)
```  
Fig. 4. Summary of Kim and Seo's [29] classification of schema and data conflicts in multi-database systems.

![](/api/attachments/8YNMN4FR/fulltext/images/c7e59e2896d221c9c5238c5172cb4b2b2998200788a2091db78be1bc5a9bf08f.jpg)  
Fig. 5. Expansion of Bird's [4] classification of heterogeneity in multi-knowledge source systems.

For distributed DSS, the realization of this requirement involves the qualification of data, model, and knowledge elements not only with a node identifier, but also with associated data base, model base, and knowledge base identifiers. A problem then arises if data, model, or knowledge objects are transient, i.e., not owned by any single system, or possibly owned by multiple systems. (Note that if objects are simply moved among systems common name spaces can be easily updated to maintain location independence.)

As with multi-database systems, primary language extensions for distributed DSS will involve manipulating data, model, and ultimately knowledge representations. Fortunately, the schematic and data heterogeneity of multi-database systems $[29,47]$ and knowledge base systems $[4]$ have already begun to be explored. These classifications provide a good starting point for investigating heterogeneity in the distributed problem processing, language, and knowledge subsystems of DSS architectures. For example, a classification scheme for heterogeneity in multi-database systems $[29]$ is given in Fig. 4.

As outlined by this figure, two main types of conflict are present in multi-database systems: those related to schema and those related to data. Within these exist a variety of conflicts related to name, value, integrity, age, and units of measure, among others. As with many other component pieces of our model, however, research in heterogeneous data translations is well under way (cf. [43]).

As a second example, a heterogeneity classification of multi-knowledge source systems [4] is summarized in Fig. 5. As this classification suggests, heterogeneity in knowledge systems carries with it not only definitional problems, but also additional burdens related to knowledge organization, meaning, usage, and strength. Research in heterogeneous knowledge translations is also under way (cf. [30]), but is presently far from adequate for the demands of distributed AI [1] or distributed DSS.

Turning from knowledge to modeling concerns, it is clear from the literature that the heterogeneity of model bases has yet to be formally explored. It seems reasonable, though, that many of the associated model base issues can be generalized from the discussion above. One undeniable problem in such an attempt is that clear definitions of model base “structure” and “schema” have not emerged, with a few exceptions such as those related to relational and network modeling (cf. [6]). But consistent with the heterogeneity issues identified above for data and knowledge bases, Blanning notes that “[t]he study of model base structure includes not only the syntactical issues addressed by networks and relations, but also certain issues in model semantics” ([6], p. 10). Thus, the heterogeneity issues of model management can be approached, at least until further direction is found, as a variant of those for multi-database and multi-knowledge source systems.

Accepting this and recognizing that representational differences will exist across queries, model constructs, and knowledge exchange, a shared language must have the ability to transform source information into representations most useful to the distributed DSS user or agent. Toward this end, multi-database developers have found that language nonproceduralism is particularly desirable $[26]$ . Further, the model subsystem should be able to make many of these transformations automatically, providing either appropriate defaults, suggestions, or making (intelligent) implicit decisions.

Hurson and Bright [26] note that multi-database languages should also include capabilities for iterating operations over multiple but slightly varying objects, performing single operations over multiple equivalent objects with varying attributes, and performing mechanical operations such as implicit joins. Similar language capabilities can be reasonably expected for distributed DSS data and model bases, particularly given relational modeling techniques and the importance of join implementation [5]. For distributed knowledge bases, the problem is even more complex, as it will require that the language be temporal and its assertions revisable.

Finally, ease of use is a primary factor in the development of a shared language subsystem. Allowing a user to search for information across a distributed system or examine the contents of particular components are obvious ease of use considerations. Other considerations influencing ease of use are less straightforward: transparent local and remote access, protecting private information $[44]$ , distributing processing activities, and deciding to what extent local resources are available to non-local users, including priority and simultaneity considerations.

## 7. Summary and conclusion

That the language subsystem is a key element of DSS is well understood. Extended to distributed DSS, the functionality of the language subsystem is even more critical. It must not only allow the user to communicate with a local support system, but must also allow the user or a local system component to communicate with other, non-local components of a distributed system.

Advances in distributed DSS to date have generally approached this challenge by making one dramatically simplifying assumption – that all distributed system components utilize essentially homogeneous model, data, and knowledge base structures. It is far more likely, however, that many local DSS have unique representational structures for these elements, the particulars of which are not easily assumed away at implementation. The extension of the DSS language subsystem to distributed support is indeed a challenging area for researchers because it encompasses all of the traditional problems of data, model, and knowledge utilization and compounds them through distribution. This paper has made the first (known) attempt to define shared language capabilities for distributed DSS.

As developed, this new generation of distributed decision support systems will have several fundamental characteristics that follow from layering, interaction, and language considerations:

\- interaction between the human and machine components will transpire through a conversational structure that presupposes a common language;

\- language functionality will include locating needed knowledge, model, and data elements, transporting and translating those elements into appropriate formats, and resolving various problems arising from heterogeneity through layered protocols;

\- centralized control mechanisms will ultimately disappear, but user or system components will retain the ability to locally exercise system-wide control over the distributed environment, given rights and privileges;

\- problem solving and learning will take place through knowledge source grafts or through interactions that advance the inferential or problem solving state of one or more component systems, or that refine a processor's contextual understanding.

An implementation of the architecture proposed here would provide a level of control for individual decision makers or agents that is both local and global in a truly distributed, heterogeneous environment. The implications of this are many. Foremost, though, is that a shared, extensible common language system may ultimately provide one of the most effective means by which a DSS user or local component is able to locate, access, and exploit a wealth of resources in a distributed environment.

By both reviewing architectural demands for distributed support systems and developing this notion of the shared language subsystem, this paper has formalized a promising alternative direction for DSS research and development. This direction both surpasses homogeneity-dependent and simpler translation-oriented approaches, and inherently provides greater flexibility for developing and utilizing DSS in distributed environments.

## Acknowledgements

The author gratefully acknowledges Robert Blanning and George Kasper for their contributions to earlier stages of this work.

## References

[1] M. Adler, E. Durfee, M. Huhns, W. Punch and E. Simoudis, AAAI Workshop on Cooperation Among Heterogeneous Intelligent Agents, AI Magazine 13, No. 2 (1992) 39–42.

[2] J. Alty and M. Coombs, Face-to-Face Guidance of University Computer Users-I: A Study of Advisory Services, International Journal of Man-Machine Studies 12 (1980) 390–406.

[3] C. Bachman, A Personal Chronicle: Creating Better Information Systems, with Some Guiding Principles, IEEE Transactions on Knowledge and Data Engineering 1, No. 1 (1989) 17–32.

[4] S.D. Bird, Toward a Taxonomy of Multi-Agent Systems, International Journal of Man-Machine Studies 39 (1993) 689–704.

[5] R.W. Blanning, A Relational Framework for Join Implementation in Model Management Systems, Decision Support Systems 1, No. 1 (1985) 69–81.

[6] R.W. Blanning, Model Management Systems, Decision Support Systems 9, No. 1 (1993) 9–18.

[7] R. Bonczek, C. Holsapple and A. Whinston, Future Directions of Developing Decision Support Systems, Decision Sciences 11, No. 4 (1980) 616–631.

[8] R. Bonczek, C. Holsapple and A. Whinston, Foundations of Decision Support Systems (Academic Press, NY, 1981).

[9] A. Bond and L. Gasser, Eds., Readings in Distributed Artificial Intelligence (Morgan Kaufmann, San Mateo, CA, 1988).

[10] A. Burns, M.A. Rathwell and R.C. Thomas, A Distributed Decision-Making System, Decision Support Systems 3, No. 2 (1987) 121–131.

[11] J. Carroll and J. McKendree, Interface Design Issues for Advice-Giving Expert Systems, Communications of the ACM 30, No. 1 (1987) 14–31.

[12] Cecez-Kecmanovic, Organizational Activity Support Systems, Decision Support Systems 12, No. 4/5 (1994) 365-379.

[13] M. Coombs and J. Alty, Face-to-Face Guidance of University Computer Users-II: Characterising Advisory Interactions, International Journal of Man-Machine Studies 12 (1980) 407–429.

[14] M. Coombs and J. Alty, Expert Systems: An Alternative Paradigm, International Journal of Man-Machine Studies 20 (1984) 21–43.

[15] J. Courtney, D. Paradice and N. Ata Mahammed, A Knowledge-Based DSS for Managerial Problem Diagnosis, Decision Sciences 18, No. 2 (1987) 373–399.

[16] R. Davis and R. Smith, Negotiation as a Metaphor for Distributed Problem Solving, Artificial Intelligence 20, No. 1 (1983) 63–109.

[17] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (1984) 89–97.

[18] G. Elofson and B. Konsynski, Delegation Technologies: Environmental Scanning with Intelligent Agents, Journal of Management Information Systems 8, No. 1 (1991) 37–62.

[19] B. Espinasse, A Cognitivist Model for Decision Support: COGITA Project, a Problem Formulation Assistant, Decision Support Systems 12, No. 4/5 (1994) 277–286.

[20] L. Gasser, Distributed Artificial Intelligence, AI Expert 4, No. 7 (1989) 26–33.

[21] J.F. George, The Conceptualization and Development of

Organizational Decision Support Systems, Journal of Management Information Systems 8, No. 3 (1991) 109–125.

[22] M.J. Ginzberg and E.A. Stohr, Decision Support Systems: Issues and Perspective, in: M.J. Ginzberg, W. Reitman and E.A. Stohr, Eds., Decision Support Systems (North-Holland, Amsterdam, 1982) 9–31.

[23] D. Hale, J. Hurd and G.M. Kasper, A Knowledge Exchange Architecture for Collaborative Human-Computer Communication, IEEE Transactions on Systems, Man, and Cybernetics 21, No. 3 (1991) 555–564.

[24] F. Halsall, Data Communications, Computer Networks and OSI, 2nd Edition (Addison-Wesley, Reading, MA, 1988).

[25] G. Huber, Organizational Learning: The Contributing Processes and the Literatures, Organization Science 2, No. 1 (1991) 88–114.

[26] A. Hurson and M. Bright, Multidatabase Systems: An Advanced Concept in Handling Distributed Data, in: M. Yovits, Ed., Advances in COMPUTERS 32 (Academic Press, Boston, MA, 1991) 149–200.

[27] V. Jacob and H. Pirkul, A Framework for Networked Knowledge Based Systems, IEEE Transactions on Systems, Man, and Cybernetics 20, No. 1 (1991) 119–127.

[28] V. Jacob and H. Pirkul, A Framework for Supporting Distributed Group Decision-Making, Decision Support Systems 8, No. 1 (1990) 17–28.

[29] W. Kim and J. Seo, Classifying Schematic and Data Heterogeneity in Multidatabase Systems, IEEE Computer (1991) 12–18.

[30] R. Knaus and C. Jay, Transporting Knowledge Bases: A Standard, AI Expert 5, No. 11 (1990) 34–39.

[31] W. Liang, Model Management for Group Decision Support, MIS Quarterly 12, No. 4 (1988) 667–680.

[32] W. Liang, Development of a Knowledge-Based Model Management System, Operations Research 36, No. 6 (1988) 849–863.

[33] W.A. Muhanna, Issues in Distributed Model Management Systems, Proceedings of the Eleventh International Conference on Information Systems (1990) 231–242.

[34] A. Newell, The Knowledge Level, Artificial Intelligence 18, No. 1 (1982) 87–127.

[35] A. Newell, Reflections on the Knowledge Level, Artificial Intelligence 59, No. 1/2 (1993) 31–38.

[36] G. Pask, Electronic Keyboard Teaching Machines, in: Glaser and Lumsdaine, Eds., Teaching Machines and Programmed Learning (National Education Association, Washington, DC, 1960) 336–349.

[37] G. Pask, Conversation, Cognition and Learning (Elsevier Press, Amsterdam, 1975).

[38] G. Pask, Conversation Theory: Applications in Education and Epistemology (Elsevier Press, Amsterdam, 1976).

[39] G. Pask, Developments in Conversation Theory, Part I, International Journal of Man-Machine Studies 13 (1980) 357–411.

[40] M.O. Pendergast, Multicast Channels for Collaborative Applications: Design and Performance Evaluation, ACM SIGCOMM 23, No. 2 (1993) 25–38.

[41] F.J. Radermacher, Decision Support Systems: Scope and Potential, Decision Support Systems 12, No. 4/5 (1994) 257–265.

[42] H.R. Rao, R. Sridhar and S. Narain, An Active Intelligent Decision Support System – Architecture and Simulation, Decision Support Systems 12, No. 1 (1994) 79–91.

[43] M. Ruschitzka and J.L. Clevenger, Heterogeneous Data Translations Based on Environment Grammars, IEEE Transactions on Software Engineering 15, No. 10 (1989) 1236–1251.

[44] A.P. Sage, Information Systems Engineering for Distributed Decisionmaking, IEEE Transactions on Systems, Man, and Cybernetics 17, No. 6 (1987) 920–936.

[45] M.S. Scott Morton, The State of the Art of Research, in: F.W. McFarlan, Ed., Information Systems Research Challenge (Harvard Press, Boston, MA, 1984) 13–45.

[46] M.J. Shaw and M.S. Fox, Distributed Artificial Intelligence for Group Decision Support, Decision Support Systems 9, No. 4 (1993) 349–367.

[47] A. Sheth and J. Larson, Federated Database Systems for Managing Distributed, Heterogeneous, and Autonomous Databases, ACM Computing Surveys 22, No. 3 (1990) 183–236.

[48] R. Smith and R. Davis, Frameworks for Cooperation in Distributed Problem Solving, IEEE Transactions on Systems, Man, and Cybernetics 11, No. 1 (1981) 61–70.

[49] R. Sprague, Jr. and E. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[50] E.B. Swanson, Distributed Decision Support Systems: A Perspective, Proceedings of the 23rd Hawaii International Conference on Systems Science (1990) 129–136.

[51] A.S. Targowski, Beyond a Concept of a Communication Process, The Journal of Business Communication 27, No. 1 (1990) 75–86.

[52] D. Woods, Paradigms for Intelligent Decision Support, in: Hollnagel et al., Eds., Intelligent Decision Support in Process Environments, NATO ASI Series 21 (1986) 153–173.

Dr. Bird received his Ph.D. from Texas Tech University in 1993 in the area of Information Systems. Specializing in knowledge and decision technologies, he publishes primarily in the human-machine and decision support fields and consults to clients including Microsoft, Digital, and Hewlett Packard. Dr. Bird currently holds a Principal Consultant position at CAP Gemini America where he focuses on corporate applications of object-oriented, AI, and web-related technologies.
