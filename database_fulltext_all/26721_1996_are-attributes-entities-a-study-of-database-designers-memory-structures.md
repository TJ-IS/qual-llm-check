---
otero_id: 26721
otero_key: "FB5JTFD3"
title: "Are Attributes Entities? A Study of Database Designers' Memory Structures"
authors: "Ron Weber"
year: "1996"
journal: "Information Systems Research"
doi: "10.1287/isre.7.2.137"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/FB5JTFD3/fulltext/images/030386aefdb9b3656df832cd2a6a1390bce704947549199ee1cfb7aaea821732.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Are Attributes Entities? A Study of Database Designers' Memory Structures

Ron Weber,

To cite this article:

Ron Weber, (1996) Are Attributes Entities? A Study of Database Designers' Memory Structures. Information Systems Research 7(2):137-162. https://doi.org/10.1287/isre.7.2.137

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1996 INFORMS

Please scroll down for article—it is on subsequent pages

## informs

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Are Attributes Entities? A Study of Database Designers' Memory Structures

Ron Weber

The University of Queensland, Department of Commerce, Queensland, 4072, Australia
weber@commerce.uq.edu.au

A longstanding debate in the data modeling literature pertains to whether the grammars used to generate conceptual schemas should sustain a distinction between entities and attributes. The grammars used to generate entity-relationship diagrams and object-oriented conceptual models, for example, provide separate constructs for representing entities and attributes. The grammars used to generate binary data models, however, provide only a single construct for representing both entities and attributes.

To sharpen the focus of the debate, a multi-trial free-recall experiment was conducted with database designers who had been trained primarily in a binary conceptual schema design methodology. In the experiment, the designers were first shown conceptual schema diagrams based on a binary model. The designers were then asked to recall the diagrams. Throughout their training as designers, they had been admonished to eschew any distinction between entities and attributes. Moreover, the diagrams they were shown in the experiment did not make a distinction between entities and attributes. Their recall protocols seemed to show, however, that they were considering some elements of the diagrams to be entities and others to be attributes. Their memory structures appear to reflect, therefore, that they perceive entities and attributes to be two distinct constructs.

(Conceptual Modelling; Entities; Attributes; Objects; Ontology; Human Memory; Semantic Networks; Spreading Activation; Chunking)

Lots of things have lots of attributes. People have heights and birthdays and children, my car is blue, and New York is crowded. But as common as the term "attribute" may be, I don't know what it means. The fact that I've been using the term is totally irrelevant. If one really wanted to develop a rigorous notion of attributes . . . , then this is another nasty question to be faced. Intuitively, some might say that attributes aren't themselves entities.

But if you think that relationships are entities, and you can't distinguish attributes from relationships, then where are you left?

Kent, 1978, pp. 77, 82.

## 1. Introduction

A longstanding debate in the data modeling literature pertains to whether the grammars used to generate conceptual schemas should sustain a distinction between entities (objects or things) and attributes (reflecting properties of these entities, objects, or things). The grammars used to generate entity-relationship diagrams (Chen 1976, Teorey et al. 1986) and object-oriented conceptual models (Kilov and Ross 1994, Cattell 1994), for example, provide separate constructs for representing entities and attributes. The grammars used to generate binary data models, however, provide only a single construct for representing entities and attributes (e.g., Abrial 1974).

Why do some designers of grammars for conceptual schemas not sustain a distinction between entities and attributes? While their underlying rationale has not always been clear, nevertheless they appear to have been influenced primarily by four factors. First, some seem to believe that entities and attributes are not ontologically-distinct constructs. In other words, they argue (or at least imply) that the distinction between entities and attributes is not real—it is a misplaced view of the world. For example, Nijssen (1977, p. 38) speaks of “a best set of concepts” for conceptual schema design that does not preserve the entity-attribute distinction (see also Abrial 1974, Senko 1975). They are not alone in this stance. From time to time, various philosophers have also held the view that the entity-attribute distinction is vacuous (see further Hamlyn 1984, pp. 56–57; Bunge 1977, pp. 99–104).

Second, even if the distinction between entities and attributes is real, some designers conclude it should not be preserved, at least for conceptual modeling purposes (e.g., Nijssen and Halpin 1989). They argue, for example, that humans exhibit semantic relativism: sometimes humans see a real-world feature as an entity; sometimes they see it as an attribute. To allow users to adopt this dual perspective at any time, they argue it is better to incorporate a generalized construct in a conceptual modeling grammar that stands for either an entity or an attribute. In a specific context or database view, users of the grammar then can impose their own interpretation on the construct. Semantic relativism is also manifested in such constructs as the NIAM grammar's $^{1}$ "objectified relationship" construct, which "basically amounts to treating a relationship between objects as an object itself" (Nijssen and Halpin 1989, p. 54), and the entity-relationship grammar's "associative object type indicator" construct, which "represents something that functions as both an object and a relationship" (Yourdon 1989, p. 241).

Third, some designers are concerned about the ease with which conceptual-schema constructs can be mapped into internal-schema constructs. In particular, they seek to ensure that the way in which the conceptual schema is designed does not inhibit the way in which the internal schema might be designed. After considering two alternative “storage representations” for a single “logical structure,” Brachhi et al. (1975, p. 263) conclude “we see that from the physical point of view an entity is a set of related attributes that are frequently retrieved together. The entity is here an access concept, not a logical concept, and it corresponds to the physical record."2 As a result, they argue in support of a "binary-relation-schema."

Fourth, some designers are concerned with whether distinguishing between entities and attributes adds unnecessary complexity to a conceptual schema. For example, Codd (1990) questions the need to distinguish between entities and one type of attribute, namely, a relationship. He comments (p. 478): "If no manipulative distinctions are made between entities and relationships, why are they conceived as two different kinds of information? Is this just one more example of a distinction that leads to an increase in complexity, but no increase whatsoever in generality."3

The resolution of these four issues is important. Whether entities and attributes are ontologically distinct constructs lies at the heart of how humans perceive the real world. Do humans really distinguish between entities and attributes? or is the distinction an artifact perpetuated by successive generations of database designers? If information systems are to be a “faithful” representation of some real-world system, database design constructs must mirror real-world constructs (Kent 1977; Wand and Weber 1990, 1995). Moreover, if designers are taught to view the world in a way that is at odds with the users of their databases, presumably they will produce lower-quality designs.

If, however, designers of grammars fail to distinguish between entities and attributes because they subscribe to semantic relativism, they must then come to grips with the problems posed by semantic overload (Hull and King 1987, pp. 209–210). Once a single grammatical construct stands for two or more ontological constructs, conceptual schemas produced by the grammar no longer clearly distinguish between different ontological constructs. To interpret a conceptual schema within their own world view, users must bring to bear knowledge outside the domain of the grammar. For example, in the relational model, a relation can stand for both an entity and a relationship. Users must employ extra-model knowledge to determine whether the relation stands for an entity or a relationship. As a result, users have to work harder to interpret conceptual schemas. Moreover, confusion may arise if two different users interpret the overloaded construct differently (Wand and Weber 1993).

Finally, if the entity-attribute distinction is dismissed because of constraints imposed by conceptual schema-internal schema mappings, data independence objectives are undermined. If schemas cannot be considered independently of one another, perhaps there are better ways to decompose database descriptions.

The primary purpose of this paper is to provide evidence on the first issue—namely, whether entities and attributes are ontologically-distinct constructs. The theoretical basis for the research relies on prior findings that suggest how humans, especially those who are expert in some domain, structure knowledge in their memories. A secondary purpose of the research is to confirm that the memory structures possessed by database designers are similar to those held by experts in other domains. By sharpening the focus of the debate about whether entities and attributes should be distinguished, hopefully better decisions can be made about approaches to conceptual modeling and the design of support tools. For example, if humans do not distinguish between entities and attributes, one must question the merits of the object-oriented approach to conceptual modeling and the usefulness of the CASE tools it has spawned.

The remainder of the paper proceeds as follows. Section 2 briefly addresses the question of how we might come to know whether entities and attributes are distinct features of the real world. Section 3 describes the proposition tested in this research and the underlying theory supporting this proposition. Section 4 outlines the research method. Section 5 describes the approach used to code the data. Section 6 presents the results obtained, and §7 discusses these results. Section 8 briefly reviews some strengths and limitations of the research. Finally, §9 presents some implications and conclusions and some directions for further research.

## 2. Some Epistemological Issues

Are entities and attributes distinct features of the real world? Realists who subscribe to the distinction argue entities and attributes exist, independently of our perceptions. Unfortunately, there seems no way of establishing unequivocally what, if anything, is real in the world. Interpretivists who subscribe to the distinction take a weaker position. They argue entities and attributes are distinct real-world features because humans have learned or created mental models to understand the world where, for some reason, the distinction is important. Whether the distinction is real, however, is another (unresolvable) matter.

The research described in this paper is founded on the weaker, interpretivist position. From an interpretivist viewpoint, two strategies might be used to try to educe evidence on the existence of entities and attributes in the mental models that humans use to understand the world. One approach would be to compare the predictive and explanatory power of competing theories about the structure of the world (ontological theories) where the distinction between entities and attributes is sustained in one candidate theory and not sustained in another. For example, a critical feature of Bunge's (1977, 1979) ontology is the distinction between things (entities) and properties (attributes). In the domain of conceptual modeling, Weber and Zhang (1996) and Wand et al. (1993) have tried to extend and use Bunge's theory to explain and predict conceptual modeling phenomena such as semantic overload and the nature of relationships. If contrary explanations and predictions could be generated from an ontological theory that does not sustain a distinction between entities and attributes, the relative power of the theories could then be evaluated—for example, via empirical testing of the competing predictions and the relative appeal of their competing explanations of the same phenomena.

A second approach is to try to tap directly the structure of human memory to determine whether it manifests a distinction between entities and attributes. In essence, models that seek to account for the structure and behavior of human memory must be developed. Again, the issue is whether models that sustain a distinction between entities and attributes appear to provide better explanatory and predictive power when they are used to account for human memory phenomena—for example, the time taken for humans to retrieve information from their memories.

At this time the first approach is more difficult to pursue. There are few formal, complete ontological models available that facilitate testing the implications of sustaining or not sustaining a distinction between entities and attributes. On the other hand, there are several advantages to pursuing the second approach. First, research that seeks to tap directly the structure of human memory is well developed (Ashcraft 1989). It has more limited goals than the first approach and, as such, is more feasible. Second, there are ample theory and empirics available to enable propositions about whether human memory is structured on the basis of entities and attributes to be developed and tested (e.g., Friendly 1979). Third, the structure of human memory appears to be the primary determinant of how individuals encode and elaborate their understanding of the real world (analysis in the context of conceptual modeling) and how they undertake problem-solving activities (design in the context of conceptual modeling). In other words, there is compelling theory and empirical evidence to indicate that database conceptual modeling and design activities will be based on the same underlying human memory structure (e.g., Anderson 1990). If this memory structure can be tapped, insights should be obtained into the types of conceptual modeling tools that will facilitate database analysis and design activities. In this light, the current research is motivated by and based upon prior research that has sought to model the structure of human memory.

## 3. Theory, Proposition, and Hypotheses

The current research tests the proposition that humans distinguish between entities and attributes because the distinction facilitates information “chunking.” Chunking is a widespread finding in studies of human memory (e.g., Cofer

1965, Hirtle and Kallman 1988, Servan-Schreiber and Anderson 1990, Murdock 1993). Humans organize items into logical groups, seemingly to conserve memory (Miller 1956, Baddeley 1994). Moreover, relative to novices, experts in a domain possess a larger number of chunks and organize their chunks according to deep-structure rather than surface-structure features of their domain of expertise (De Groot 1965, Chase and Simon 1973, Reitman 1976, Egan and Schwartz 1979, Chi et al. 1977, Weber 1980, Adelson 1981, McKeithen et al. 1981). Whether chunks are “real” is a moot issue. As a theoretical construct, however, chunks seem inextricably tied to human performance. In this vein, Mandler (1967, p. 328) argues that “memory and organization are not only correlated, but organization is a necessary condition for memory.”

Several theoretical justifications might be used to support human-memory chunking of real-world features according to entities and their associated attributes (Shuell 1969; Friendly 1977). Those theories used as the basis for the current research, however, are the theory of semantic networks initially developed by Collins and Quillian (1969, 1972) and extended by Anderson (1983, 1990), the theory of ontology developed by Bunge (1977), and the theory of spreading activation developed by Anderson and Pirolli (1984).

Using Collins and Quillian's and Anderson's semantic network theories, entities and attributes are stored in memory as nodes in a network. These nodes are linked via pathways. For example, consider the simple domain of discourse represented by the semantic network shown in Figure 1. There are two entities: manager and project. Each entity possesses certain attributes. The manager entity has five attributes, and the project entity has six attributes. Note that one attribute, manager name, is common to both entities.

Figure 1 Semantic Network for a Simple Domain of Discourse  
![](/api/attachments/FB5JTFD3/fulltext/images/2a699571d3d49b95d064a160d1ca162c17f92d9ff43f6e1a91d518cd5ba0cca9.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Using Bunge's ontological theory, two principles govern the ways in which pathways in the network are constructed. First, entities are never linked directly to other entities. Rather, entities are linked only via mutual attributes (properties)—attributes that the entities have in common (Bunge 1977, pp. 101–102). For example, in Figure 1, manager name is a mutual attribute of the manager and project entities. It assigns a manager a name, and it assigns a project a name corresponding to the name of the employee who manages the project. Second, attribute nodes are never linked directly to other attribute nodes. This principle is based on the ontological assumption that there are no second-order properties in the world—that is, there are no properties of properties (Bunge 1977, pp. 98–99). For example, in Figure 1, currency (e.g., dollars) might be considered to be an attribute of the salary attribute. Whenever second-order attributes are conceived, however, Bunge argues that the primary attribute has been specified incompletely. In the example, the fully specified primary attribute is the salary of the manager expressed in dollars.

Anderson and Pirolli's spreading activation theory governs the way in which information is learned and recalled within a semantic network (see, also, Ratcliff and McKoon 1994). Some of the important principles of spreading activation are as follows:

1. When humans access a node in a semantic network, they generate an “activation” or a “priming.” This activation or priming of a node then spreads almost instantaneously to other nodes in the network.

2. Activation will decay exponentially as a function of the distance it spreads. In this regard, the total level of activation emitted by a node to all connected nodes is less than its own level of activation.

3. The total level of activation emitted from a node is divided among the connected nodes.

4. Activations that converge on a node from multiple sources will sum.

5. The level of activation of a node decays as a power function of time.

6. The total activation level strength of a node is the sum of the strengths remaining from the individual strengthenings.

To illustrate the application of these principles, consider, again, Figure 1.

As individuals learn about managers and projects, they will first create and then prime the nodes that represent the entities and their associated attributes. Over time, entities will receive higher levels of priming than attributes because the link with an entity will be made each time an attribute is learned (primed). For example, as each of the five attributes of manager is learned (see Figure 1), the attribute will be associated with the manager entity, and the entity node therefore will be primed. In other words, in a single pass of learning each of the attributes, each attribute will be primed only once, whereas the entity will be primed five times.

When individuals must recall information about a domain of discourse, they are more likely to recall an entity node first rather than an attribute node. The reason is that entity nodes are more likely to have a higher residual level of activation because of more-frequent past primings. Having retrieved an entity node, however, individuals are then more likely to retrieve the attribute nodes associated with that entity node rather than other nodes in the network. According to the theory, the activation will spread out from the entity node directly to the attribute nodes. The activation levels in the attribute nodes that arise from the spread of activation from the entity node are likely to be higher than residual activation levels in other nodes in the network. The reason is that activation levels arising from immediate priming are likely to be more intense than residual activation levels that are a function of past primings (recall from principle 5 above that activation levels decay exponentially over time). Therefore, the attribute nodes linked to the entity node that has been retrieved will be retrieved next.

Whether individuals then retrieve another entity node that is connected to a mutual attribute in the set of attributes is unclear. It will depend on the new activation level attained in the entity node as a result of priming from the mutual attribute versus the level of residual activation present in other entity nodes. For example, assume the project entity in Figure 1 was retrieved first during recall, and then its attributes were retrieved. When the manager name mutual attribute is retrieved, activation would then spread to the manager entity, albeit with decreased intensity. Whether the manager entity is retrieved as a consequence will depend on the strength of the resulting level of activation versus the residual priming strength in other entity nodes not activated by the spread (and not shown in Figure 1).

The above analysis leads to the following two hypotheses:

H1. If individuals sustain a distinction between entities and attributes, they will recall an item that represents an entity first during a recall task.

H2. If individuals sustain a distinction between entities and attributes, they will recall items that represent attributes associated with the same entity together during a recall task.

The psychological theories that can be used to support an argument that individuals do not sustain a distinction between entities and attributes have not been articulated, nor is it clear what the nature of these theories might be. Assume, however, that entities are again represented as nodes in a semantic network. Recall, there are no attribute nodes if the entity-attribute distinction is not sustained, so all the nodes in Figure 1, for example, constitute entity nodes. During a recall task, each of the nodes in the semantic network should have an equal chance of being recalled first. Otherwise, some notion of primacy attaches to those nodes that are more likely to be recalled first. This idea is the essence of the entity-attribute distinction (entity nodes are primary, and attribute nodes are secondary).

Assume, however, that an individual recalled the title node in Figure 1 first. It might be argued that the individual would next recall the manager node because a link exists between the title and manager nodes. But what nodes would then be recalled? If the individual next recalled the salary, number of dependents, education, and manager name nodes, the primacy of the manager node would again be established. Thus, evidence would exist to support an argument that the individual is, in fact, sustaining an entity-attribute distinction. In this light, it seems possible to support an argument that humans fail to distinguish between entities and attributes only if their recall protocols evidence clustering at no greater than chance levels. $^{4}$

$^{4}$ Actually, we would expect levels of clustering slightly greater than chance because the first two nodes recalled are likely to be associated.

The above analysis leads to the following two hypotheses:

H3. If individuals do not sustain a distinction between entities and attributes, they will recall an item first during a recall task only at the level of chance.

H4. If individuals do not sustain a distinction between entities and attributes, they will recall items together only at the level of chance.

## 4. Research Method

While psychologists have used many devices to try to tap the structure of human memory, a major empirical technique they employ is the free-recall experiment. In a free-recall experiment, the experimenter presents a list of items to a person, removes the items, and then asks the person to recall the items. The recall protocols exhibited by individuals are believed to reflect the content and structure of their memories. For example, Bousfield (1953) read subjects a randomized list of nouns drawn from four categories: animals, names, professions, and vegetables. He then asked his subjects to recall as many nouns as possible. Analysis of the protocols showed subjects clustered together nouns from the same category at greater than chance expectations. He concluded his four categories were “real” in the sense they reflected how humans viewed the world and structured their memories.

Two types of free-recall procedures have been used in studies of human memory. Initially, single-trial free-recall studies, such as Bousfield's, were used. Subjects were presented with a stimulus list only once, and their corresponding recall protocol was then captured. Subsequently, multi-trial free-recall studies were used (e.g., Bousfield and Bousfield 1966, Ernest 1991). Subjects were presented with the same stimulus list multiple times, and their corresponding recall protocols were captured after each presentation. Multi-trial free-recall studies allow the stability of a memory structure to be examined across trials. If the structure is stable, it is believed to manifest a characteristic of long-term memory. If it is unstable, it is believed to manifest the subject's attempt to devise and refine a short-term recall strategy to address the memory task at hand.

To investigate whether database designers distinguish between entities and attributes, in this research a multi-trial free-recall experiment was used. Participants were shown a conceptual schema diagram that did not distinguish between entities and attributes and then asked to recall the diagram after it had been removed. If participants distinguish between entities and attributes, it was expected they would recall those elements of the diagram that manifested an entity first followed by those elements that manifested the entity's associated attributes. In other words, they would impose an organization on elements of the diagram to facilitate recall, even though this organization was not featured in the diagram.

## 4.1. Design

There were two between-subjects factors and one within-subjects factor in the experimental design used. The first between-subjects factor was type of participant group: experimental or control. The experimental group comprised students who had received fairly extensive training to undertake database analysis and design; the control group comprised students who had no experience of database analysis and design.

A control group was needed so that the effects of extraneous memory organizations used by participants to facilitate their recall of the diagram's elements could be factored out in the data analysis. From prior free-recall experiments, it is well known that participants will impose some type of organization on items to facilitate recall, even when none is present (Tulving 1962). In the current experiment, participants could use, for example, the topology of the diagram they were shown to facilitate recall. To the extent the diagram's topology manifested in part the distinction between entities and attributes, the recall protocols would not reflect the database designers' long-term memory organizations. While the control group could be expected to employ such types of extraneous recall strategies, the experimental group should use long-term memory structures they had acquired through training and experience.

A control group was also needed to determine whether the experimental-group participants were using a common but idiosyncratic strategy to facilitate their recall. If, for example, they sustain an entity-attribute distinction in their memory organizations, we cannot conclude that their clients (database users) also sustain this distinction. The experimental-group participants may have acquired the distinction over time as a strategy that enhances their expertise as conceptual-schema designers. If the control-group participants also sustain the distinction, however, there is stronger evidence to support the proposition that humans in general view the world in terms of entities and attributes. In essence, the control-group participants are proxies for database users.

The second between-subjects factor was type of diagram shown to a participant: simple or complex. If designers sustain a distinction between entities and attributes, presumably it will be most beneficial in the recall of a complex diagram. If the distinction also is used to facilitate the recall of a simple diagram, however, it acquires more importance as a factor to be considered in the design of approaches and tools to support conceptual modeling. Furthermore, use of a simple and complex diagram also allows partial control to be exercised over confoundings associated with the topology of the diagram shown to participants. If a diagram's topology has an impact on the recall protocol, it should have less effect with the complex diagram because the complex diagram's topology will be more difficult to recall.

The measure of diagrammatic complexity used was the number of nodes and links in a diagram. Based upon semantic network and spreading activation theories, memory tasks will be more complex as the number of nodes and links increase. With more nodes and links, lower levels of priming will dissipate through individual paths in the network, thereby increasing recall difficulty (Ashcraft 1989). The complex diagram had almost 2.5 times the number of nodes and links as the simple diagram.

The within-subjects factor was trial. If only a single-trial free-recall experiment had been used, the recall protocols obtained may have manifested a short-term strategy devised by the participant to facilitate the recall task. If the recall strategy is constant across trials of the experiment, however, it is more likely to manifest the participant's long-term memory structure. Five trials were used in the experiment because pilot tests indicated participants discarded any short-term recall strategies (e.g., the topological layout of the diagram) after only the first one or two trials.

## 4.2. Participants

Recall from §4.1 that the experimental design required two groups of participants: an experimental group with experience in database analysis and design; and a control group with no experience of database design. Participants in both groups were students at the University of Queensland. All participated voluntarily in the experiment. They responded to a request for participation announced in lectures. Each was paid \$20 for their participation. The following subsections describe the makeup of the groups.

4.2.1. Experimental-group Participants. The experimental group comprised 30 second-year computer science students. Participation was sought from these students for four reasons. First, they were relatively expert users of the NIAM approach to database conceptual schema design (Nijssen and Halpin 1989). In their first year they undertook two courses that developed NIAM skills: a first-semester course devoted to conceptual modeling using NIAM; and a second-semester course devoted to using NIAM in conjunction with relational databases. This focus on database analysis and design continues throughout much of their subsequent coursework. Clearly they do not have the skills of experienced database designers, but neither are they novices.

Second, as a major pedagogic objective in the Department of Computer Science, the students had been exposed to other conceptual modeling tools, such as the entity-relationship model, only later in their undergraduate studies. They knew primarily NIAM, which is a binary conceptual modeling technique that does not show entities and attributes as distinct features of the world. In short, they formed a somewhat pristine group—a group that had been trained from the outset not to model the world in terms of entities and attributes and one that in general viewed other modeling approaches as inferior. Participants in the experimental group were deliberately selected, therefore, to bias the experiment against producing results that showed designers sustained a distinction between entities and attributes.

Third, if experienced database designers had been chosen to participate in the experimental group, the ways they conceive the world would have been colored by their experiences with conceptual modeling methodologies that sustain a distinction between entities and attributes. Experienced database designers are likely to have used CASE tools, for example, and the preponderance of CASE tools support methodologies like the entity-relationship approach. Thus, the experiment would have been biased toward finding that designers sustain a distinction between entities and attributes. Inquiries that were made by the researcher indicated that experienced NIAM users who might have participated in the research were also experienced users of other conceptual modeling methodologies.

Fourth, given the nature of the experiment, computer science students with a fair level of training in database analysis and design are likely to be good surrogates for experienced designers. While experienced designers should have a deeper and more extensive knowledge of database analysis and design than the students (Glaser and Chi 1988), whether they sustain a distinction between entities and attributes should be a common feature of their memory structures.

4.2.2. Control-Group Participants. The control group comprised 24 first-year undergraduate Commerce students and 6 MBA students. The undergraduate students were undertaking an introductory managerial accounting course. None had completed a computer course, and none had been exposed to conceptual modeling. In particular, they knew nothing about NIAM nor any other conceptual modeling approach, such as the entity-relationship approach. The MBA students had taken an introductory computer course that emphasized use of tools, such as spreadsheets. Like the undergraduate students, however, none had been exposed to conceptual schema design nor to conceptual modeling approaches.

## 4.3. Materials

Materials comprised two NIAM conceptual schema diagrams obtained from two organizations that used NIAM for conceptual modeling purposes (Figures 2 and 3), large sheets of paper and felt pens that participants could use to draw their responses, a stop watch to record times accurately, and a video camera to record the way in which participants drew their diagrams during the recall task. Note, the choice of NIAM was made simply because it is a good example of a binary modeling methodology. NIAM is used fairly widely in Europe and Australia, and its use in the U.S. is increasing, particularly among large organizations. $^{5}$ Moreover, it con-

Figure 2 Simple NIAM Diagram  
![](/api/attachments/FB5JTFD3/fulltext/images/c0c235bf5d9118d1b41ba41d5763097f2bcd7b946779064cc4b116c72fe5f9fe.jpg)

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Figure 3 Complex NIAM Diagram  
![](/api/attachments/FB5JTFD3/fulltext/images/73cbe0a3ffb9d6e11463dbd4646f93abe597b3b1df44e6d9ff046f36cdb51f2a.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

tinues to spawn new binary modeling methodologies, such as PSM $^{6}$ (ter Hofstede 1993). Accordingly, it provides a reasonable vehicle for the experimental task. Note, also, the two NIAM diagrams were chosen because they are representative of simple and more complex diagrams used in practice.

## 4.4. Procedure

All participants were run singly through the experiment in a room designed specifically for the conduct of social-psychology experiments. For example, the room provided a well-lit, noise-free environment, and using a one-way mirror it allowed unobtrusive monitoring of participants by a research assistant from an adjacent control room.

Upon arrival, participants were greeted and seated at a desk in the center of the room. If participants belonged to the experimental group, a research assistant explained to them that the purpose of the research was "to investigate the usefulness of NIAM for designing conceptual schemas." If participants belonged to the control group, they were told the purpose of the research was "to investigate the usefulness of some tools for designing computerized databases."

A research assistant then explained how the experiment would be conducted. In brief, participants were informed that a (NIAM) diagram would be shown to them. They would be given a short time to study the diagram, after which it would be removed. They would then be given a longer period in which they would have to redraw the diagram from memory. Participants were informed their responses would be videotaped. In this regard the research assistant pointed out the video camera mounted above the participant's workbench and explained its purpose. Participants were also told their responses were confidential and that they could cease the experiment at any time without penalty or retribution. If they were agreeable to proceeding, they were asked to sign a consent form indicating they understood the nature of the experiment and their rights as a participant.

The experiment then commenced. Participants were shown either the simple NIAM diagram or the complex NIAM diagram (randomly allocated) for a period of three minutes. The diagram was then removed, and participants were asked to redraw the diagram from memory using the paper and pen provided. They were allowed ten minutes to redraw the diagram, unless they indicated earlier they could recall no more to draw. These procedures were repeated until either the diagram had been reproduced successfully twice in succession or five attempts had been made to reproduce the diagram.

Both the materials and procedures used in the experiment had been tested and refined prior to their use in the experiment proper. Four students had participated in the pilot tests. Only minor modifications to the experimental materials and procedures were needed in light of the pilot tests.

## 5. Data Coding

Prior to coding the recall protocols, the two NIAM diagrams were shown to a computer science academic who taught systems analysis, conceptual modeling, and database design. He was an expert in both entity-relationship modeling and NIAM modeling. Thus he had a good understanding of conceptual schema modeling approaches that sustained a distinction between entities and attributes and those that did not. He was asked to identify all entities and attributes that he concluded were manifested in the two NIAM diagrams shown in Figures 2 and 3 via the entities (circles) and roles (rectangles).

Tables 1 and 2 show the entities and attributes he identified and the codes assigned to each attribute. To illustrate the nature of the expert's classification of NIAM entities and roles into entities and attributes and the coding scheme used, consider the contract entity in the simple diagram (Figure 2). The expert concluded Figure 2 showed a contract entity with five attributes (see Table 1): a contract number, which proxied for the contract entity and which could be identified from the contract (contract-no) entity on the NIAM diagram; a security deposit amount cost, which could be identified from the security deposit amount role and cost entity on the NIAM diagram; a contract price cost, which

## Table 1 Coding for Easy Diagram

Table 1 Coding for Easy Diagram
Contract
A1 contract number
A2 security deposit number cost
A3 contract price cost
A4 supervising engineer
A5 job number to which contract assigned
Contract security deposit reduction
B1 contract security deposit reduction
B2 security deposit reduction number
B3 contract number
B4 security deposit reduction amount cost
B5 date security deposit reduced
Approved Extension
C1 approved extension
C2 contract number
C3 date
C4 extension number of days
C5 nonworking number of days

could be identified from the security deposit amount role and cost entity on the NIAM diagram; a supervising engineer, which could be identified from the supervising engineer entity on the NIAM diagram; and a job number, which could be identified from the job number entity on the NIAM diagram. In some cases, note that the expert designated a NIAM entity as an attribute of more than one entity (a mutual attribute). For example, in Figure 2 he concluded that contract number was an attribute of both the contract entity and the approved extension entity.

Next, the videotapes were viewed by a research assistant who had been trained to record the sequence in which circles (entities) and rectangles (roles) were recalled by a participant during a trial. This sequence was then transformed into a recall sequence of entities and attributes. The following transformation rules applied:

1. If a NIAM entity stood for both an entity and attribute, only the attribute was recorded, but in all cases it was the highest numbered attribute. For example, in Figure 2 the contract (contract\_no) entity stands for both a contract entity and a contract\_number attribute of this contract entity. It would be recorded as attribute A1, where the "1" indicated that the contract number attribute was also proxying for the contract entity.

2. If a NIAM entity stood only for an entity, it was recorded as an entity. For example, the approved extension entity in Figure 2 would have been recorded as C1.

3. In some cases the attribute being represented could not be determined when a NIAM entity was drawn. In Figure 2, for example, if a participant drew the Cost (\$) entity, it could stand for either the security deposit amount cost attribute or the contract price cost attribute. In this type of situation, the research assistant determined the order of attribute representation by examining the order in which the roles were drawn. For example, if the security deposit amount role (rectangle) was drawn before the contract price role (rectangle), the research assistant recorded the security deposit amount reduction cost attribute as being recalled before the contract price cost attribute.

4. In those cases where a NIAM entity represented an attribute of two or more entities, the code assigned to the entity depended upon the prior or subsequent entities recalled. For example, in Figure 2, contract\_number is an attribute of both the contract entity and the approved extension entity. If, say, the participant had previously recalled the supervising engineer entity, then the cost entity, then the contract price role, and then the contract\_no entity, the contract\_no entity would have been assigned the code A1 rather than B3.

5. In some cases participants drew part of a diagram before attaching labels to the entities or roles. A code was not recorded until a label was written. Until a label is written, it is unclear whether a drawn component reflects a participant's understanding of the domain being modeled or some extraneous recall strategy—for example, a count of the number of circles on the diagram to be drawn.

As a result of the coding, recall sequences (protocols) for each participant were produced across each trial. To check the reliability of coding, however, a second research assistant, who was blind to the hypotheses being tested, also viewed the videotapes of 12 of the participants (20 percent) and coded their recall protocols. The 12 participants where duplicate coding was undertaken were chosen at random: 3 from the control group that undertook the simple task; 3 from the experimental group that undertook the complex task; 3 from the control group that undertook the complex task; and 3 from the experimental group that undertook the complex task. The Kappa Coefficient, which measures the proportion of intercoder agreement after removing the agreement that can be attributed to chance, was then calculated (Cohen 1960). For both the simple task and the complex task, the average Kappa Coefficient was .80. This level is reasonable relative to others that have been reported and deemed acceptable in experimental research (e.g., Jarvenpaa 1989, Srinivasan and Te'eni 1995). Thus, the reliability of coding was considered to be sufficiently high for the recall protocols to form the bases for the data analyses reported below.

Table 2 Coding for Hard Diagram

<table><tr><td colspan="2">Employee</td><td colspan="2">Uniform Item</td></tr><tr><td>A1</td><td>pay number</td><td>E1</td><td>uniform item</td></tr><tr><td>A2</td><td>depot number</td><td>E2</td><td>supply source</td></tr><tr><td>A3</td><td>termination date</td><td>E3</td><td>size sensitive flag</td></tr><tr><td>A4</td><td>start date</td><td></td><td></td></tr><tr><td>A5</td><td>employee name</td><td colspan="2">Pay Location</td></tr><tr><td>A6</td><td>pay location</td><td>F1</td><td>pay location</td></tr><tr><td>A7</td><td>employee category</td><td>F2</td><td>description</td></tr><tr><td colspan="2">Entitlement Issue History</td><td colspan="2">Department Division</td></tr><tr><td>B1</td><td>issue history</td><td>G1</td><td>department code</td></tr><tr><td>B2</td><td>pay number</td><td>G2</td><td>description</td></tr><tr><td>B3</td><td>entitlement items</td><td></td><td></td></tr><tr><td>B4</td><td>date</td><td colspan="2">Employee Category</td></tr><tr><td>B5</td><td>size</td><td></td><td></td></tr><tr><td>B6</td><td>quantity</td><td>H1</td><td>employee category</td></tr><tr><td></td><td></td><td>H2</td><td>department code</td></tr><tr><td></td><td></td><td>H3</td><td>category code</td></tr><tr><td colspan="2">Entitlement Issue</td><td>H4</td><td>description</td></tr><tr><td>C1</td><td>entitlement issue</td><td>H5</td><td>badge required flag</td></tr><tr><td>C2</td><td>pay number</td><td></td><td></td></tr><tr><td>C3</td><td>entitlement items</td><td colspan="2">Employee Category-Entitlement Code</td></tr><tr><td>C4</td><td>next issue date</td><td></td><td></td></tr><tr><td>C5</td><td>required size</td><td>I1</td><td>employee category-entitlement code</td></tr><tr><td>C6</td><td>required quantity</td><td>I2</td><td>employee category</td></tr><tr><td></td><td></td><td>I3</td><td>entitlement code</td></tr><tr><td></td><td></td><td>I4</td><td>issue flag months</td></tr><tr><td colspan="2">Entitlement Items</td><td></td><td></td></tr><tr><td>D1</td><td>entitlement items</td><td></td><td></td></tr><tr><td>D2</td><td>employee category</td><td></td><td></td></tr><tr><td>D3</td><td>uniform item</td><td></td><td></td></tr><tr><td>D4</td><td>quantity</td><td></td><td></td></tr></table>

## 6. Results

Six types of analysis were undertaken on the recall protocols. The first two examine whether the experimental treatments have been operationalized successfully. They are reported in the first two subsections below. The remaining four analyses examine whether participants appear to be distinguishing between entities and attributes. They are reported in the last four subsections below.

## 6.1. Number of Participants Achieving Complete Recall

The first analysis undertaken examined the number of participants who achieved complete recall of a diagram.

Table 3 shows that ten control-group participants achieved complete recall of the simple diagram: one on the second trial; two on the third trial; and seven on the fourth trial. In comparison, eleven experimental-group participants achieved complete recall of the simple diagram: one on the first trial; three on the second trial; three on the third trial; and four on the fourth trial. Note, however, that no participants achieved complete recall for the complex diagram.

These results indicate that the treatments have been operationalized successfully. The complex diagram indeed was more difficult to recall than the simple diagram. Moreover, at least for the simple diagram, more experimental-group participants achieved complete recall sooner, indicating they had a higher level of task expertise.

## 6.2. Proportion of Items Recalled

The second analysis undertaken examined the proportion of items recalled by participants in the experiment. As with the first analysis, the primary purpose of this analysis was to determine whether the independent variables in the experiment had been operationalized correctly. A fully-factorial $2 \times 2 \times 5$ repeated-measures analysis of variance model (2 levels of expertise, 2 levels of task complexity, 5 trials) was fitted to the data. Table 4 shows the mean and standard deviation for the proportion of items recalled for each treatment across each trial. Table 5 shows the levels of significance obtained for all effects. $^{7}$

As expected, the experimental group recalled a higher proportion of items than the control group, and both groups recalled a higher proportion of items for the simple diagram. These results indicate the expertise factor and task complexity factor have been operationalized correctly: Experimental group participants were indeed more proficient at the task than control group participants, and the complex diagram was indeed more difficult than the simple diagram.

Table 3 Number of Participants Who Achieved Complete Recall Across Trials

<table><tr><td rowspan="2">Trial</td><td colspan="2">Simple Diagram</td><td colspan="2">Complex Diagram</td></tr><tr><td>Control</td><td>Experimental</td><td>Control</td><td>Experimental</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>2</td><td>1</td><td>3</td><td>0</td><td>0</td></tr><tr><td>3</td><td>2</td><td>3</td><td>0</td><td>0</td></tr><tr><td>4</td><td>7</td><td>4</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

The trial factor was also significant. Difference contrasts indicate participants recalled a greater proportion of items between trials 1 and 2 $[F(4, 56) = 37.5, p < 0.001]$ , trials 2 and 3 $[F(4, 56) = 25.5, p < 0.001]$ , trials 3 and 4 $[F(4, 56) = 15.0, p < 0.001]$ , and trials 4 and 5 $[F(4, 56) = 7.9, p < 0.001]$ . Polynomial contrasts also indicate the pattern of recall across trials followed a quadratic form $[F(1, 56) = 85.9, p < 0.001]$ .

The experience-by-trial interaction was also significant. Figure 4 shows the nature of the interaction. Difference contrasts indicate that experimental-group participants recalled a greater proportion of items on trial 1 $[F(1, 56) = 17.8, p < 0.001]$ , trial 2 $[F(1, 56) = 20.5, p < 0.001]$ , and trial 3 $[F(1, 56) = 12.5, p = 0.001]$ . However, experimental-group participants and control-group participants did not differ in their recall proportions on trials 4 and 5. In short, as expected, the control-group participants were slower to warm up than the experimental-group participants, but their recall performance was as good as the experimental-group participants after three trials.

Table 4 Treatment Means and Standard Deviations for Proportion Recalled

<table><tr><td colspan="2"></td><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td></tr><tr><td rowspan="2">Novice</td><td>Easy</td><td>0.262(0 203)</td><td>0.487(0.271)</td><td>0.779(0.225)</td><td>0.887(0.190)</td><td>0.949(0.099)</td></tr><tr><td>Complex</td><td>0.136(0.122)</td><td>0.326(0.204)</td><td>0.513(0 261)</td><td>0.662(0.259)</td><td>0.749(0.240)</td></tr><tr><td rowspan="2">Expert</td><td>Easy</td><td>0.497(0.255)</td><td>0.795(0.225)</td><td>0.949(0.063)</td><td>0.959(0.104)</td><td>0.964(0.104)</td></tr><tr><td>Complex</td><td>0.297(0.109)</td><td>0.515(0.126)</td><td>0.674(0 092)</td><td>0.762(0.140)</td><td>0.826(0.123)</td></tr></table>

WEBER
Database Designers' Memory Structures  
Table 5 Analysis of Variance Results for Proportion of Items Recalled, Proportion of Entities First Recalled, Chunk Size, and Pair Frequency

<table><tr><td>Effect</td><td>Proportion</td><td>Entity 1st Recall</td><td>Chunk Size</td><td>Pair Frequency</td></tr><tr><td>E</td><td> $F(1,56) = 14.2, p < 0.001$ </td><td> $F(1,56) = 2.2, p = 0.141$ </td><td> $F(1,56) = 4.3, p = 0.042$ </td><td> $F(1,56) = 2.2, p = 0.144$ </td></tr><tr><td>T</td><td> $F(1,56) = 27.4, p < 0.001$ </td><td> $F(1,56) = 56.1, p < 0.001$ </td><td> $F(1,56) = 2.6, p = 0.116$ </td><td> $F(1,56) = 5.7, p = 0.027$ </td></tr><tr><td>E × T</td><td> $F(1,56) = 0.078, p = 0.781$ </td><td> $F(1,56) = 0.473, p = 0.495$ </td><td> $F(1,56) = 1.2, p = 0.287$ </td><td> $F(1,56) = 0.2, p = 0.637$ </td></tr><tr><td>Tr</td><td> $F(4,224) = 260.3, p < 0.001$ </td><td> $F(4,224) = 0.665, p = 0.616$ </td><td> $F(4,224) = 8.7, p < 0.001$ </td><td> $F(3,168) = 57.2, p < 0.001$ </td></tr><tr><td>E × Tr</td><td> $F(4,224) = 8.0, p < 0.001$ </td><td> $F(4,224) = 7.7, p < 0.001$ </td><td> $F(4,224) = 1.2, p = 0.304$ </td><td> $F(3,168) = 0.7, p = 0.574$ </td></tr><tr><td>T × Tr</td><td> $F(4,224) = 2.2, p = 0.066$ </td><td> $F(4,224) = 2.8, p = 0.023$ </td><td> $F(4,224) = 3.3, p = 0.013$ </td><td> $F(3,168) = 5.1, p = 0.002$ </td></tr><tr><td>E × T × Tr</td><td> $F(4,224) = 1.6, p = 0.178$ </td><td> $F(4,114) = 1.7, p = 0.159$ </td><td> $F(4,224) = 1.1, p = 0.378$ </td><td> $F(3,168) = 0.3, p = 0.822$ </td></tr></table>

Note. E = Experience; T = Task Complexity; Tr = Trial

Figure 4 also shows the nature of the quadratic function between recall proportion and trials. It is a concave, asymptotic function. After the first three trials, performance has begun to plateau.

## 6.3. Proportion of Times Entities Recalled First

The third analysis examined the proportion of times an entity was recalled first. Recall that, on the basis of semantic-network and spreading-activation theories of memory, entities should be recalled first followed by their associated attributes. In this light, for each recall protocol, the recall protocols were examined to determine whether the first item recalled from an entity-attribute set was an entity. Since not all entity-attribute sets may have been recalled during a trial, a normalized dependent-variable measure was determined by calculating the proportion of entity-attribute sets where the entity was recalled first. For example, assume some items from only the contract and approved-extension entity-attribute sets in Table 1 were recalled. No items from the contract security deposit reduction entity-attribute set were recalled. Assume, also, that contract number (an entity) was the first item recalled in the contract entity-attribute set and date (an attribute) was the first item recalled in the approved-extension entity-attribute set. Thus, the proportion of times that an entity was recalled first in this recall protocol was 0.5.

As with the second analysis, a fully-factorial $2 \times 2 \times 5$ repeated-measures analysis of variance model was fitted to the data (2 levels of expertise, 2 levels of task complexity, 5 trials). Table 6 shows the mean and standard deviation for the proportion of times entities were recalled first for each treatment across each trial. Table 5 shows the levels of significance obtained for all effects.

Only one main effect was significant, namely, task complexity. For the complex diagram, participants recalled an entity first more frequently: on average, entities were recalled first for 51 percent of entity-attribute sets compared to 18 percent for the simple diagram. Perhaps with the simple task, cuing on the entity first to recall the items in an entity-attribute set was less important. Participants had fewer problems remembering items in the simple diagram. For the complex task, however, remembering the items in an entity-attribute set was more difficult, and entity cuing appears to have been an important means of facilitating recall. $^{8}$

The experience-by-trial interaction was significant. Figure 5 shows the nature of the interaction. Difference contrasts indicate that experimental-group participants recalled a greater proportion of entities first only for trial 1 $F(1, 56) = 10.5, p < 0.001$ . However, experimental-group participants and control-group participants did not differ in the proportions of entities they recalled first on trials 2, 3, 4, and 5. Overall, cuing on the entity in an entity-attribute set was a significant feature of the recall, irrespective of the level of database design expertise.

Figure 4 Experience-by-trial Interaction for Proportion Recalled  
![](/api/attachments/FB5JTFD3/fulltext/images/703d33a8fa8ab431440859bb396d02ba3800986c13fd47a98d73fa7fff572c4e.jpg)

The task-complexity-by-trial interaction was also significant. Figure 6 shows the nature of the interaction. For the complex task, difference contrasts indicate that a greater proportion of entity items were recalled first on trial 1 $[F(1, 56) = 7.4, p < 0.001]$ , trial 2 $[F(1, 56) = 40.3, p < 0.001]$ , trial 3 $[F(1, 56) = 92.0, p < 0.001]$ , trial 4 $[F(1, 56) = 28.3, p < 0.001]$ , and trial 5 $[F(1, 56) = 46.2, p < 0.001]$ . In short, while the interaction is statistically significant, it really manifests the task complexity main effect reported above. Entities were more likely to be recalled first by both experimental-group participants and control-group participants for the complex task. The statistically significant interaction most likely reflects that the two lines in Figure 6 are not parallel—in other words, the difference in the proportion of entities recalled first between the simple task and complex task is not constant across all trials.

Figure 5 Experience-by-trial Interaction for Proportion of Times Entities Recalled First  
![](/api/attachments/FB5JTFD3/fulltext/images/2eef0f8974de3931c3443065af5998e854e6257836f0a9665226753332b666d8.jpg)

## 6.4. Size of Chunks Recalled

The fourth analysis examined the size of chunks recalled. This analysis seeks to determine whether participants are recalling items based upon a memory organization that relies upon a distinction between entities and attributes. The size of a chunk was determined by counting the number of items from an entity-attribute set recalled contiguously. In other words, any items recalled together that represented an entity or attributes of the same entity were deemed to be a chunk. Note, this measure of chunk size is accurate only to the extent that our a priori designation of entities and attributes on a NIAM diagram is correct (in the sense it reflects the memory organization used by the participants).

Table 6 Treatment Means and Standard Deviations for Proportion of Entities First Recalled

<table><tr><td colspan="2"></td><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td></tr><tr><td rowspan="2">Novice</td><td>Easy</td><td>0.133(0 303)</td><td>0.211(0.359)</td><td>0.044(0.117)</td><td>0 111(0.206)</td><td>0.155(0.213)</td></tr><tr><td>Complex</td><td>0 322(0 406)</td><td>0 580(0.259)</td><td>0.554(0.229)</td><td>0.476(0.277)</td><td>0.553(0 189)</td></tr><tr><td rowspan="2">Expert</td><td>Easy</td><td>0 367(0.310)</td><td>0.111(0.162)</td><td>0.120(0 169)</td><td>0 233(0.216)</td><td>0.233(0.216)</td></tr><tr><td>Complex</td><td>0 634(0 267)</td><td>0 534(0.107)</td><td>0.531(0.144)</td><td>0.470(0.163)</td><td>0.497(0 120)</td></tr></table>

Figure 6 Task Complexity-by-trial Interaction for Proportion of Times Entities Recalled First  
![](/api/attachments/FB5JTFD3/fulltext/images/d88fd76c9221d2c3838fa67e358568e4ebce4fbe7796a5ec1a718d05ab4d3fd2.jpg)

Again, a fully-factorial $2 \times 2 \times 5$ repeated-measures analysis of variance model was fitted to the data (2 levels of expertise, 2 levels of task complexity, 5 trials). Table 7 shows the mean and standard deviation for the chunk size for each treatment across each trial. Table 5 shows the level of significance obtained for all effects.

As expected, on average the experimental-group participants recalled larger size chunks than the control-group participants. Interestingly, however, there was no main effect for task complexity on the size of the chunk recalled.

Figure 7 Task Complexity-by-trial Interaction for Chunk Size  
![](/api/attachments/FB5JTFD3/fulltext/images/49f65f47f3877d6afb41425b77296bcf275dacc434f6642d5d1335b1b522a28c.jpg)

The trial factor was again significant. Difference contrasts indicate participants recalled larger chunks between trials 1 and 2 $[F(4, 56) = 3.3, p = 0.018]$ but not between trials 2 and 3, 3 and 4, and 4 and 5. Polynomial contrasts also indicate the pattern of recall across trials was primarily linear $[F(1, 56) = 15.9, p < 0.001]$ although there was some evidence of a quadratic form $[F(1, 56) = 6.1, p = 0.016]$ (reflecting the learning/warm-up effects that occurred between trials 1 and 2 but which then dissipated).

The task complexity-by-trial interaction was also significant. Figure 7 shows the nature of the interaction. Difference contrasts indicate that participants recalled larger chunks for the simple task only on trial 4 $[F(1, 56) = 6.5, p = 0.014]$ and trial 5 $[F(1, 56) = 12.2, p = 0.001]$ . There was no difference between the simple and complex task across the other trials. Note that the cross-over pattern of performance shown in Figure 7 is the likely reason why the task-complexity main effect is not significant, even though the task complexity-by-trial interaction is significant.

Table 7 Treatment Means and Standard Deviations for Chunk Size Recalled

<table><tr><td colspan="2"></td><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td></tr><tr><td rowspan="2">Novice</td><td>Easy</td><td>1.337(0.624)</td><td>2.115(1.520)</td><td>1 733(0.397)</td><td>2 114(0 540)</td><td>2.396(0.623)</td></tr><tr><td>Complex</td><td>1.333(1.310)</td><td>1.987(0.603)</td><td>2 118(0.681)</td><td>1 966(0 436)</td><td>1.949(0.432)</td></tr><tr><td rowspan="2">Expert</td><td>Easy</td><td>1 861(0 682)</td><td>2.152(0 809)</td><td>2.337(0.929)</td><td>2 701(1 077)</td><td>2.701(1.077)</td></tr><tr><td>Complex</td><td>1.926(0.594)</td><td>2 112(0.565)</td><td>2.088(0 427)</td><td>1 967(0 397)</td><td>1.915(0 375)</td></tr></table>

Table 8 Treatment Means and Standard Deviations for Pair Frequency Recalled

<table><tr><td colspan="2"></td><td>Trials 1-2</td><td>Trials 2-3</td><td>Trials 3-4</td><td>Trials 4-5</td></tr><tr><td rowspan="2">Novice</td><td>Easy</td><td>0 777(1.506)</td><td>1 587(1 952)</td><td>2 865(2 689)</td><td>3 363(2.973)</td></tr><tr><td>Complex</td><td>0.738(1.081)</td><td>2.499(2.897)</td><td>4 221(4 062)</td><td>5.359(4.598)</td></tr><tr><td rowspan="2">Expert</td><td>Easy</td><td>1.123(1.007)</td><td>2.793(2.377)</td><td>3 517(2.647)</td><td>3.517(2.647)</td></tr><tr><td>Complex</td><td>1 787(0 956)</td><td>4.041(2.299)</td><td>4.952(2 078)</td><td>6.640(3.676)</td></tr></table>

## 6.5. Consistency of Recall

The fifth analysis examined the consistency of a participant's recall order across trials. The pair-frequency measure of recall consistency was used, namely:

$$
\begin{array}{r l} \mathrm{PF} & = O (\mathrm{ITR2}) - E (\mathrm{ITR2}) \\ & = O (\mathrm{ITR2}) - 2 C (C - 1) / h k, \quad \text { where } \end{array}
$$

PF = pair frequency,

$O(ITR) = \text{the observed number of pairs of items recalled together in any order on a pair of successive trials,}$

$E(\text{ITR}) = \text{the expected number of pairs of items that would be recalled together in any order on a pair of successive trials through chance,}$

C = the number of items recalled on both trials in the pair,

$h =$ the number of items recalled on the first trial of the pair, and

$k =$ the number of items recalled on the second trial of the pair.

Sternberg and Tulving (1977) have compared various measures of subjective organization in free-recall data, and they have concluded that the pair-frequency measure is the most valid and reliable.

Like the second analysis, this analysis seeks to determine whether participants are recalling items based upon a memory organization that relies upon a distinction between entities and attributes. In this analysis, however, the measure of clustering is not dependent upon an a priori designation of items as either entities or attributes of a particular entity. Instead, it relies only upon two items being recalled together across successive trials.

A fully-factorial $2 \times 2 \times 4$ repeated-measures analysis of variance model was fitted to the data. In this model the trial factor had only four levels because we are dealing with pairs of trials rather than individual trials, but there are again two levels of expertise and two levels of task complexity. Table 8 shows the mean and standard deviation for the pair-frequency score for each treatment across each pair of trials. Table 5 shows the level of significance obtained for all effects.

Contrary to expectations, the experimental-group participants did not show greater recall consistency than the control-group participants. Nevertheless, there was a main effect for task complexity: participants showed greater recall consistency with the complex task.

Once again the trial factor was significant. Difference contrasts indicate the consistency of participants' recall consistency increased between trials 1 and 2 and trials 2 and 3 [F(4, 56) = 12.2, p < 0.001], trials 2 and 3 and trials 3 and 4 [F(4, 56) = 8.2, p < 0.001], and trials 3 and 4 and trials 4 and 5 [F(4, 56) = 4.3, p = 0.004]. Polynomial contrasts also indicate the increase in consistency of recall across pairs of trials was primarily linear $[F(1,56)=84.8,p<0.001]$ although there was some evidence of a quadratic form $[F(1,56)=6.6,p=0.013]$ (reflecting the learning/warm-up effects that occurred between the first two pairs of trials but which then dissipated).

The task complexity-by-trial interaction was also significant. Figure 8 shows the nature of the interaction. Difference contrasts indicate that participants showed greater recall consistency for the complex task only for the pair of trials 4 and 5 $[F(1,56)=7.8,p=0.007]$ . There was no difference in recall consistency between the simple and complex task across the other pairs of trials.

## 6.6. Multidimensional Scaling and Cluster Analysis Results

The sixth analysis used multidimensional scaling (MDS) and cluster analysis to examine whether any structure underlay the recall protocols provided by the participants. MDS is a method for describing a matrix of proximities via a configuration of points in n-dimensional space (Kruskal and Wish 1978). Cluster analysis is a method for describing a matrix of proximities via a tree representation (Aldenderfer and Blashfield 1984). Both methods present complementary information about the same data. Kruskal (1977) points out, however, that the two methods differ in an important respect. MDS provides information about large dissimilarities; local positions in n-dimensional space are not especially meaningful. Cluster analysis, on the other hand, provides information about small dissimilarities; clusters high up in the tree are not especially meaningful. He recommends that both techniques be used in conjunction with one another. MDS can be used to produce a spatial representation of proximities. Cluster analysis can then be used to group points in the spatial representation.

Friendly's formula was used to compute a matrix of proximities between any two items recalled in a trial (see Friendly 1977, pp. 199–203). Basically, Friendly's formula assigns higher proximities to items recalled closer together. For example, assume five items, A, B, C, D, and E, are presented to a participant for recall. Assume, also, that the participant's recall protocol is B, D, A, E. The interitem proximity between two items, i and j, is computed using the formula $P_{ij} = L - D_{ii}$ , where P is the proximity measure, L is the list length, and $D_{ij}$ is the intra-recall distance between a pair of items. If we consider $P_{ij}$ for B and A, since L = 5, $D_{ij} = 2$ , then $P_{ij} = 3$ . If required, proximities can be normalized by dividing $P_{ij}$ by L - 1. Note, if an item is not recalled, its proximity measure with other items will be zero.

![](/api/attachments/FB5JTFD3/fulltext/images/c2abd061d52fb88f88ebd94d72b8416dd28c7fc9ad71963a545ac10af043aa16.jpg)

\- Four MDS analyses were undertaken. The input to each analysis was a matrix of normalized proximities averaged over the 15 participants in each treatment group and over the last three trials for each participant. In other words, for each participant, the inter-item proximities were calculated for each of their last three trials. Only the last three trials were considered because, during these trials, warm-up effects are likely to have dissipated and any memory structure facilitating recall is likely to be manifested. The normalized proximities were then averaged over the three trials and then across all participants in the group to obtain the final proximity matrix. In essence, then, the matrix shows the proximity measures for an average person in the treatment group. If any element of the matrix was zero (reflecting no participant had recalled the pair of items in any trial), it was designated as missing data in the MDS analyses that were undertaken.

Four cluster analyses were then undertaken using the complete-link method. Under the complete-link method, an item is assigned to a cluster only if the distance between it and the farthest item in the cluster is smaller than the distance between any other item not in the cluster and the farthest item in the cluster. The method produces clusters with minimum diameters where all items in the cluster are completely connected. Friendly (1977, p. 212) argues the complete-link method is most appropriate when examining the sorts of memory structures that would arise if theories like semantic networks and spreading activation were true.

Figure 9 MDS for Control Group and Easy NIAM Diagram  
![](/api/attachments/FB5JTFD3/fulltext/images/df1125ea9e45e284d8a85ec3d9021556faa49e6e64113cb2ee66f1cb668f0e87.jpg)

6.6.1. Results for the Simple Task. Figures 9 and 10 show the MDS solutions in two dimensions obtained using Kruskal's algorithm for the recall protocols provided by the control group and the experimental group presented with the easy NIAM diagram. The stress level obtained for each MDS solution is reasonable: 0.111 for the control group and 0.134 for the experimental group. Shepard diagrams (scatterplots of distances between points in an MDS plot and observed proximities) also indicate the MDS solutions are not degenerate.

Figures 9 and 10 also show the lower-level clusters produced by the clustering algorithm. For the control group, three clusters emerge: one comprising A1, A2,

Figure 10 MDS for Experimental Group and Easy NIAM Diagram
DIMENSION 2  
![](/api/attachments/FB5JTFD3/fulltext/images/d33f07374ea96ceccb9f5d410999318f57222cf754ec8fbe63be3361c43be097.jpg)

Figure 11 MDS for Control Group and Difficult NIAM Diagram  
![](/api/attachments/FB5JTFD3/fulltext/images/8f6a5ad025a8e9bd881f71ecdb2f71228569ae137f297a90826cb7729b96a414.jpg)

A3, A4, and B4; a second comprising A5, B1, B2, and B3; and a third comprising B5, C1, C2, C3, C4, and C5. Thus, both the MDS and cluster analysis solutions support the predictions based on the semantic network and spreading activation theories. For the experimental group, three clusters emerge: one comprising A1, A2, A3, and A4; a second comprising B1, B2, and B3; and a third comprising A5, B4, B5, C1, C2, C3, C4, and C5. Again, the MDS and cluster analysis solutions support the predictions based on the semantic network and spreading activation theories, although they are not as strong as those for the control group.

6.6.2. Results for the Complex Task. Figures 11 and 12 show the MDS solutions in two dimensions obtained using Kruskal's algorithm for the recall protocols provided by the control group and the experimental group presented with the difficult NIAM diagram. The stress level obtained for each MDS solution is reasonable: 0.195 for the control group and 0.211 for the experimental group. Shepard diagrams (scatterplots of distances between points in an MDS plot and observed proximities) also indicate the MDS solutions are not degenerate.

Figure 12 MDS for Experimental Group and Difficult NIAM Diagram
DIMENSION 2  
![](/api/attachments/FB5JTFD3/fulltext/images/6bb101b14dbe0be1dfdea17dc4f4e32d79d477fc223385d4a33cbf8668de3f27.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Unfortunately, because of missing values, cluster analysis results could not be obtained for the control and experimental groups that worked on the difficult NIAM problem. Not all pairs of items were recalled in the protocols, and so in some cases proximity scores could not be calculated. Nevertheless, using the MDS solutions both the control group's and the experimental group's results show evidence of clustering according to the predicted form. For the control group, a number of clusters are evident—for example, A1, A2, A3, A4, A5, and A6; B1, B3, B4, B5, B6, and C1; C5 and C6; C3, E1, E2, E3, and D2; G1, G2, H1, H2, H3, H4, H5, I3, and I4. Similarly, for the experimental group, a number of clusters are evident—for example, A1, A2, A3, A4, and A5; B2 and B3; B4, B5, and B6; D4, E1, E2, and E3; and D1 and D3. In short, for the complex diagram, there is again evidence that both the control-group participants and the experimental-group participants are clustering items on the basis of entities and attributes to facilitate their recall.

## 7. Discussion of Results

Because it is impossible to examine directly the way humans structure their memories, on the basis of the results obtained in this research it is likewise impossible to state unequivocally that humans conceive the world in terms of entities and attributes. Nevertheless, the results obtained are supportive of this proposition. The following subsections discuss them in more detail.

## 7.1. Primacy of Entities

Hypotheses 1 and 3 focus on the primacy of entities if individuals sustain an entity-attribute distinction. The results show that participants recalled entities first in the complex diagram 51 percent of the time when they recalled clusters of nodes. This percentage is far higher than the percentage that would be expected through chance. Consistent with the semantic network, ontological, and spreading activation theories articulated in §3, participants in the experiment seem to be anchoring first on entities and then on attributes during the performance of the recall task. Thus, Hypothesis 1 is supported, and Hypothesis 3 is not supported. For the simple task, however, note that entities were recalled first only 18 percent of the time when participants recalled clusters of nodes. This percentage is roughly what would be expected if entities were to be recalled first through chance. Thus, Hypothesis 1 is not supported, and Hypothesis 3 is supported.

These results suggest that the topology of the simple diagram may have been a confounding factor in the recall of nodes from the diagram. The recall task was simple enough for participants to use the layout of the diagram to facilitate their recall. With the complex diagram, however, it seems that remembering the topology was too difficult for it to play much of a part in recall. Instead, the predicted focus on entity nodes and then attribute nodes occurred.

## 7.2. Amount of Clustering

Hypotheses 2 and 4 focus on the issue of whether clustering is manifested in the recall protocols. If greater-than-chance clustering levels occur, recall from §3 that the entity-attribute distinction is supported. If clustering levels are no greater than chance, however, the distinction is not supported.

Three sets of analyses provide evidence of greater-than-chance clustering levels in the recall protocols. First, in terms of the size of chunks recalled, on average the experimental-group participants recalled larger-size chunks than the control-group participants. If we assume the control-group protocols represent chance levels of recall of chunks, the experimental group has therefore exhibited greater-than-chance clustering in their recall protocols. Second, in terms of the pair-frequency measure of recall consistency, both groups appear to have equal facility with recall. Both groups manifest clustering in their recall protocols, however, at greater than chance levels. Recall, the pair-frequency measure does not depend on any a priori specification of which items constitute a cluster. Third, in terms of the multidimensional scaling and cluster analysis results, again there is evidence of greater-than-chance clustering in the recall protocols. The results are more clear-cut for the simple task, but nevertheless they are present also for the complex task.

In summary, therefore, the clustering results support the proposition that both the control-group participants and experimental-group participants appear to be using a distinction between entities and attributes to facilitate their recall of items. Specifically, Hypothesis 2 is supported, and Hypothesis 4 is not supported.

## 7.3. Stability of Clustering

In terms of whether the clustering evidenced in the recall protocols manifests long-term memory structures or short-term strategies devised to facilitate recall, the evidence is mixed. As expected, the proportion of items recalled over trials increased (prima facie evidence of instability and therefore use of short-term strategies). This measure is unlikely to be a good proxy, however, for the existence of clustering in the recall protocols. Rather, it is most likely to reflect that participants remembered more items as they were exposed for longer periods to the diagrams. In terms of the proportion of times that entities were recalled first, however, there is no evidence of a trial effect. At least in the case of the complex task, across trials participants often seem to have used an entity node to cue their recall of attribute nodes. This result indicates that participants were using a long-term memory structure to facilitate recall. In terms of the size of chunks recalled, the trial effect was significant, but only between trials 1 and 2. Thus, there was evidence of a quick warm-up effect and then stability of the memory structures used to facilitate recall throughout the remaining trials. Again, this result suggests participants were using a long-term memory structure to facilitate recall. In terms of the pair-frequency (consistency) measure of clustering, however, performance increased across trials for both the experimental and control groups. This result suggests that participants were not using a long-term memory structure to facilitate recall. In summary, two sets of results were supportive of stable memory structures having been used by participants, and one set of results was supportive of unstable memory structures having been used.

Somewhat contrary to expectations, two sets of results indicate that the experts were not using more stable memory structures than the novices. First, the experimental group did not recall entities first on more occasions than the control group. Moreover, the experiment tal-group participants recalled more entities first only on the first trial. Thus, experts and novices both seem to have been using similar memory structures to facilitate recall. Also, there was no difference between the pair-frequency (consistency) measure of recall between the experimental and control groups, nor was there an experience-by-trial interaction effect. Again, these results indicate that experts and novices were using similar memory structures to facilitate recall. In short, once control-group participants had grasped the nature of a NIAM diagram, it seems they could quickly bring to bear a strategy similar to that used by the experimental-group participants to facilitate their recall. On the other hand, experts recalled larger size chunks than novices, indicating that experts might have had better, more stable memory structures to facilitate recall. Alternative interpretations can be given to all these results, however, so they should be treated with caution.

## 8. Strengths and Limitations of the Research

The results discussed above should be considered in the context of the strengths and limitations of the research. The following subsections provide a brief discussion of those characteristics of the research that either enhance or undermine the validity and reliability of the results obtained.

## 8.1. Theory

A strength of the research is that the results can be interpreted in the context of a theory that explains why recall clustering manifests that humans sustain a distinction between entities and attributes. As far as the researcher is aware, no prior research has sought to provide a theoretical account of why humans would either sustain or not sustain the distinction between entities and attributes. Perhaps it might be possible to devise alternative theories, however, that would provide a contrary interpretation of the results obtained in this research. Indeed, researchers who wish to continue to argue that the distinction between entities and attributes should not be sustained should seek to devise such theories.

## 8.2. External Validity

Given the nature of the experiment undertaken, the external validity of the results may be limited. Only two tasks were given to participants, and only a single grammar was used to represent elements within the domain of discourse. Whether the results hold across other tasks and other grammars is an issue for further research. Students were also used as proxies for database designers and end users of information systems. Further research might seek the assistance of other types of participants to determine whether the results obtained hold generally.

## 8.3. Internal Validity

Careful control was exercised through the experimental design to try to ensure the internal validity of the results. As discussed previously, however, one threat to internal validity that might have occurred relates to the influence of the topology of the diagrams on the results obtained. Note that to some extent an entity and its related attributes cluster together topologically on a NIAM diagram. These topological characteristics may be facilitating recall, at least in part, and there is some evidence in the recall protocols to support this view. For example, in the simple diagram, the MDS and cluster analysis solutions show that control-group participants recalled security deposit reduction amount costs when they recalled the attributes of a contract. In Figure 2, note the close spatial proximity of this attribute with the contract's attributes. Participants may also have employed some other type of recall strategy that is similar to one based on entity-attribute groupings. Informal conversations with some participants subsequent to the experiments, however, suggest this is not the case. These participants indicated that entity-attribute clusterings were the primary basis they used for recall. Moreover, as discussed previously, a complex task was used, in part, to try to mitigate the effects of topology on the recall results.

## 8.4. Construct Validity

In this research, there are two major issues that relate to construct validity. First, there is the question of whether greater-than-chance clustering in recall protocols really manifests that individuals are making distinctions between entities and attributes. In §3, theoretical arguments were provided to account for why greater-than-chance clustering should indicate this distinction is being made. Second, there is the question of whether the measures of clustering used are valid. As discussed in §4, all measures of clustering have been shown to be problematical in some way. By using multiple measures of clustering, however, there is a greater chance that the amount of clustering present in the recall protocols has been measured correctly.

## 8.5. Statistical Conclusion Validity

The primary means of statistical analysis used in this research was repeated-measures analysis of variance. Because the cell sizes were equal, the results of the statistical tests undertaken should be robust to most violations of assumptions underlying the tests. In this light, the statistical conclusion validity of the results obtained should be high.

While a fair number of statistically significant results have been obtained in this research, even more might occur if the error variance associated with the tests could be reduced. In this regard, it might be possible to achieve more homogeneous experimental and control groups. For example, one factor that might contribute to a higher error variance is the tendency of participants to make or not make entity-attribute distinctions based on individual cognitive differences. If this variable could then be used as a control variable in the research, more powerful results might be obtained. Other factors like spatial-imagery ability might also be important in determining the amount of clustering evident in a participant's recall protocol (Ernest 1991). More generally, Cohen (1994) has argued forcefully for the inclusion of individual difference variables in models of memory. Similarly, other variables like age and gender have been shown to have an effect on the amount of clustering present in free recall data (Witte et al. 1993, Lewis and Ormrod 1985). Again, by taking these variables into account in the design of future research to determine whether humans sustain a distinction between entities and attributes, statistical conclusion validity might be improved.

## 9. Conclusions, Implications, and Future Research

This research tested the proposition that humans distinguish between entities and attributes when they seek to understand the real world. Even though a group of student database designers had been trained not to make this distinction, the results indicated that they still seemed to sustain the distinction as a basis for structuring information in their long-term memories. Moreover, the research found that a group of potential database users who were not trained in database design also seemed to sustain a distinction between entities and attributes. The distinction seems important, therefore, in understanding the real world, irrespective of whether individuals are trained database designers or potential users of databases.

The results of a single experiment must always be treated cautiously. Nevertheless, in light of the results obtained in this research, proponents of conceptual data models that do not sustain a distinction between entities and attributes (e.g., binary models) might wish to reflect upon the merits of their position. As discussed in the introduction, clearly there are some advantages to not sustaining the distinction. If information-systems designers are seeking to understand the way their clients perceive the world, however, failure to sustain the distinction may lead to misunderstandings. The proponents of binary models might wish to consider, therefore, whether they should modify their conceptual modeling tools to incorporate a distinction between objects that users deem to be entities and objects that users deem to be attributes. Alternatively, they should try to demonstrate both theoretically and empirically that sustaining a distinction between entities and attributes is vacuous.

The results also may provide some insights as to why, in practice, binary data models have been eschewed in favor of data models that preserve the entity-attribute distinction. If, as the results indicate, users of data models preserve the distinction in the ways they perceive the world, binary data models will create an incongruency. Users of binary data models will be forced to model the world in ways that are at odds with the ways they perceive the world, and the psychological discomfort that arises may mean they turn to data models where entities and attributes are distinct modeling constructs. The results support the current trend toward use of object-oriented conceptual modeling tools, for example, that sustain a distinction between objects (entities) and properties (attributes) of objects (e.g., Coad and Yourdon 1991). They also provide insights into why object-relationship models might not have fared well in prior empirical research that has compared them with entity-attribute-relationship models (Shoval and Even-Chaime 1987, Kim and March 1995).

Future research might further seek to tap memory structures to determine how humans seem to model the real world. Such research would assist database designers to better understand how their clients potentially perceive the world. Such research might also impact the types of data models devised by researchers to help database designers to model the world. Presumably, memory-structure research based on some theory of the structure and behavior of the real world (e.g., Bunge 1977) is likely to produce better results. $^{9}$

$^{9}$ I am indebted to Francis Chan, Tasman Hays, Craig Hume, Robyn Schwarz, and Marcus van Vugt for research assistance, to Tony Baglionu and Ray McNamara for statistical advice, and to participants in workshops at the University of Melbourne, University of New South Wales, and University of California, Los Angeles for comments on earlier versions of this paper. I am especially indebted to Peter Creasey for his assistance in obtaining participants in the research and his advice on several aspects of the research, and to Colin Ferguson, Graeme Halford, Michael Humphreys, the Associate Editor, and the reviewers for helpful comments on the paper. The research described in this paper was supported in part by grants from the Australian Research Council and GWA Ltd

## References

Abrial, J R., "Data Semantics," in J. W. Klimbie and K. L. Koffeman (Eds.), Data Base Management, North-Holland, Amsterdam, 1974, 1–59

Adelson, B., "Problem Solving and the Development of Abstract Categories in Programming Languages," Memory and Cognition, 9, 4 (1981), 422–433

Aldenderfer, M S and R K Blashfield, Cluster Analysis, Sage, CA, 1984

Anderson, J. R., "A Spreading Activation Theory of Memory," J Verbal Learning and Verbal Behavior, 22 (1983), 261–295.

——, Cognitive Psychology and Its Implications, 3rd ed, W. H. Freeman and Company, New York, 1990.

—— and P. L. Pirolli, "Spread of Activation," J. Experimental Psychology: Learning, Memory, and Cognition, 10, 4 (1984), 791–798.

Ashcraft, M. H., Human Memory and Cognition, Scott, Foresman and Company, Glenview, IL, 1989.

Baddeley, A, "The Magical Number Seven Still Magic After All These Years?" Psychological Rev., 101, 2 (1994), 353–356.

Bousfield, A. K. and W. A. Bousfield, "Measurement of Clustering and of Sequential Constancies in Repeated Free Recall," Psychological Reports, 19 (August–December 1966), 935–942

Bousfield, W A, "The Occurrence of Clustering in the Recall of Randomly Arranged Associates," J. General Psychology, 49 (October 1953), 229–240.

Bracchu, G., P. Paolini, and G. Pelagatti, "Data Independent Descriptions and the DDL Specifications," in B. C M. Douqué and G M. Nijssen (Eds.), Data Base Description, North-Holland, Amsterdam, 1975, 259–266

Bunge, Mario, Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World, Reidel, Boston, MA, 1977

——, Treatise on Basic Philosophy Volume 4: Ontology II: A World of Systems, Reidel, Boston, 1979

Cattell, R. G. G., Object Data Management: Object-Oriented and Extended Relational Database Systems, Rev. Ed Addison-Wesley, Reading, MA, 1994.

Chase, W. C and H. A. Simon, "Perception in Chess," Cognitive Psychology, 4 (1973), 55–81

Chen, P., "The Entity-Relationship Model: Toward a Unified View of Data," ACM Trans. Database Systems, 1, 1 (March 1976), 9–36

Chu, M., P. J. Feltovich, and R. Glaser, "Categorization and Representation of Physics Problems by Experts and Novices," Cognitive Sci., 5 (1977), 121–152.

Coad, P and E. Yourdon, Object-Oriented Analysis, Prentice-Hall, Englewood Cliffs, NJ, 1991

Codd, E. F., The Relational Model for Database Management: Version 2. Addison-Wesley, Reading, MA, 1990.

Cofer, C N., "On Some Factors in the Organizational Characteristics of Free Recall," American Psychologist, April (1965), 261–272

Cohen, J., "A Coefficient of Agreement for Nominal Scales," Educational and Psychological Measurement, 20, 1 (1960), 37–46

Cohen, R. L., "Some Thoughts on Individual Differences and Theory Construction," Intelligence, 18 (1994), 3–13

Collins, A. M and M R Quillian, "Retrieval Time from Semantic Memory," J Verbal Learning and Verbal Behavior, 8 (1969), 240-247.

— and —, "How to Make a Language User," in E. Tulving and W. Donaldson (Eds.), Organization and Memory, Academic Press, New York, 1972, 383–415

De Groot, A. D., Thought and Choice in Chess, Mouton, The Hague, 1965.

Egan, D. E. and B. J Schwartz, "Chunking in Recall of Symbolic Drawings," Memory & Cognition, 7, 2 (1979), 149–158.

Ernest, C. H., "Ability Differences and Prose Learning," Intelligence, 15 (1991), 455–477

Everest, G. C., Database Management: Objectives, System Functions, & Administration, McGraw-Hill, New York, 1986

Friendly, M L., "In Search of the M-Gram: The Structure of Organization in Free Recall," Cognitive Psychology, 9 (1977), 188–249

Glaser, R. and M. T. H. Chi, "Overview," in M. T. H. Chi, R. Glaser, and M. J. Farr (Eds.), The Nature of Expertise, Lawrence Erlbaum, Hillsdale, NJ, 1988, xv–xxviii

Hamlyn, D. W., Metaphysics, Cambridge University Press, Cambridge, 1984.

Hirtle, S. C. and H. J. Kallman, "Memory for the Location of Pictures: Evidence for Hierarchical Clustering," American J Psychology, 101, 2 (Summer 1988), 159–170

Hull, R. and R. King, "Semantic Database Modeling. Survey, Applications, and Research Issues," ACM Computing Surveys, 19 (September 1987), 201–260

INFORMATION SYSTEMS RESEARCH
Vol. 7, No. 2, June 1996

Jarvenpaa, Sirrka L., "The Effect of Task Demand and Graphical Format on Information Processing Strategies," Management Sci., 35, 3 (March 1989), 285–303

Kent, W., "Entities and Relationships in Information," in G. M. Nijssen (Ed.), Architecture and Models in Data Base Management Systems, North-Holland, Amsterdam, 1977, 67–91

——, Data and Reality: Basic Assumptions in Data Processing Reconsidered, North-Holland, Amsterdam, 1978

Kilov, H and J Ross, Information Modeling: An Object-Oriented Approach, Prentice-Hall, Englewood Cliffs, NJ, 1994

Kim, Y-G. and S T March, "Comparing Data Modeling Formalisms," Comm. ACM, 38, 6 (June 1995), 103–115.

Kruskal, J B. and M Wish, Multidimensional Scaling, Sage, California, 1987

—, "The Relationship Between Multidimensional Scaling and Clustering," in Van Ryzin (Ed.), Classification and Clustering, Academic Press, New York, 1977, 17–44

Lewis, M. A. and J. E. Ormrod, "Sex Differences in Semantic Clustering in Free Recall of Words and Pictures," Perceptual and Motor Skills, 61 (1985), 231–235

Mandler, G., "Organization in Memory," in K. W. Spence and J. T. Spence (Eds), The Psychology of Learning and Motivation, Volume 1, Academic Press, New York, 1967, 327–372

McKeithen, K B, J.S. Reitman, H H Rueter, and S.C. Hirtle, "Knowledge Organization and Skill Differences in Computer Programmers," Cognitive Psychology, 13 (1981), 307–325.

Miller, G A, "The Magical Number Seven, Plus or Minus Two: Some Limits on Our Capacity to Process Information," Psychological Rev, 63 (1956), 81–97.

Murdock, B. B., "TODAM2 A Model of Storage and Retrieval of Item, Associative, and Serial-Order Information," Psychological Rev., 100, 2 (1993), 183–203

Nijssen, G M, "Current Issues in Conceptual Schema Concepts," in G. M. Nijssen (Ed.), Architecture and Models in Data Base Management Systems, North-Holland, Amsterdam, 1977, 31–65.

— and T. A Halpin, Conceptual Schema and Relational Database Design, Prentice-Hall, Sydney, 1989

Ratcliff, R. and G McKoon, "Retrieving Information from Memory: Spreading Activation Theories Versus Compound-Cue Theories," Psychological Rev, 101, 1 (1994), 177–184.

Reitman, J. S., "Skilled Perception in Go: Deducing Memory Structures from Inter-Response Times," Cognitive Psychology, 8 (1976), 336–356.

Senko, M E, "The DDL in the Context of a Multilevel Structured Description: DIAM II with FORAL," in B C M Douqué and G M. Nijssen (Eds.), Data Base Description, North-Holland, Amsterdam, 1975, 239–257

Servan-Schreiber, E and J R. Anderson, "Learning Artificial Grammars with Competitive Chunking," J. Experimental Psychology: Learning, Memory, and Cognition, 16, 4 (1990), 592–608.

Shoval, P and M Even-Chaime, "Database Schema Design: An Experimental Comparison Between Normalization and Information Analysis," Database, 18, 3 (1987), 30–39

Shuell, T J, "Clustering and Organization in Free Recall," Psychological Bulletin, November 1969, 353–374.

Srinivasan, A. and D. Te'eni, "Modeling as Constrained Problem Solving: An Empirical Study of the Data Modeling Process," Management Sci., 41, 3 (March 1995), 419–434.

Sternberg, R. J. and E. Tulving, "The Measurement of Subjective Organization in Free Recall," Psychological Bulletin, 84, 3 (1977), 539–556.

Teorey, T. J., D. Yang, and J P Fry, "A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model," ACM Computing Surveys, 18, 6 (June 1986), 197–222.

ter Hofstede, A. H M., Information Modeling in Data Intensive Domains, CIP-Gegevens Koninklijke Bibliotheek, Den Haag, 1993

Tulving, E., "Subjective Organization in Free Recall of 'Unrelated' Words," Psychological Review, 69 (July 1962), 344–354

Wand, Y., V. Storey, and R. Weber, "Analyzing the Meaning of a Relationship," Working Paper, The University of British Columbia, British Columbia, Canada, February 1993.

— and R. Weber, "On the Ontological Expressiveness of Information Systems Analysis and Design Grammars," J. Information Systems, 3, 4 (October 1993), 217–237.

— and —, "An Ontological Model of an Information System," IEEE Trans Software Engineering, November 1990, 1282–1292

—— and ——, “On the Deep Structure of Information Systems,” Information Systems J, July (1995), 203–223

Weber, R., "Some Characteristics of the Free Recall of Computer Controls by EDP Auditors," J. Accounting Res, 18, 1 (Spring 1980), 214–241.

— and Y Zhang, "An Ontological Analysis of NIAM's Grammar for Conceptual Schema Diagrams," Information Systems J, 1996, publication forthcoming.

Witte, K L., J. S Freund, and S. Brown-Whistler, "Adult Age Differences in Free Recall and Category Clustering," Experimental Aging Res., 19, 1 (January–March 1993), 15–28.

Yourdon, E., Modern Structured Analysis, Prentice-Hall, Englewood Cliffs, NJ, 1989.

Amitava Dutta, Associate Editor This paper was received on February 6, 1995, and has been with the author 1 month for 1 revision.
