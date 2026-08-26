---
otero_id: 6360
otero_key: "FD6WK6DB"
title: "Representing Part-Whole Relations in Conceptual Modeling: An Empirical Evaluation"
authors: "Graeme Shanks; Elizabeth Tansley; Jasmina Nuredini; Daniel Tobin; Ron Weber"
year: "2008"
journal: "MIS Quarterly"
doi: "10.2307/25148856"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Representing Part-Whole Relations in Conceptual Modeling: An Empirical Evaluation Author(s): Graeme Shanks, Elizabeth Tansley, Jasmina Nuredini, Daniel Tobin and Ron Weber  
Source: MIS Quarterly, Vol. 32, No. 3 (Sep., 2008), pp. 553-573  
Published by: Management Information Systems Research Center, University of Minnesota  
Stable URL: http://www.jstor.org/stable/25148856

Accessed: 25/06/2014 04:04

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# REPRESENTING PART-WHOLE RELATIONS IN CONCEPTUAL MODELING: AN EMPIRICAL EVALUATION $^{1}$

By: Graeme Shanks
Department of Information Systems
University of Melbourne
Parkville, Victoria 3052
AUSTRALIA
gshanks@unimelb.edu.au

Elizabeth Tansley
School of Computing Sciences
Central Queensland University
Rockhampton, Queensland 4702
AUSTRALIA
e.tansley@cqu.edu.au

Jasmina Nuredini
Simsion and Associates
131-135 Gore Street
Fitzroy, Victoria 3065
AUSTRALIA
jasminan@optusnet.com.au

Daniel Tobin
Marketing and Communications
University of Melbourne
Parkville, Victoria 3052
AUSTRALIA
dtobin@unimelb.edu.au

Ron Weber
Faculty of Information Technology
Monash University
Caufield East, Victoria 3145
AUSTRALIA
ron.weber@infotech.monash.edu.au

## Abstract

The part-of construct is a fundamental element of many conceptual modeling grammars that is used to associate one thing (a component) with another thing (a composite). Substantive theoretical issues surrounding the part-of construct remain to be resolved, however. For instance, contrary to widespread claims, some researchers now argue the relationship between components and composites is not always transitive. Moreover, how the part-of construct should be represented in a conceptual schema diagram remains a contentious issue. Some analysts argue composites should be represented as a relationship or association. Others argue they should be represented as an entity. In this paper we use an ontological theory to support our arguments that composites should be represented as entities and not relationships or associations. We also describe an experiment that we undertook to test whether representing composites as relationships or entities enables users to understand a domain better. Our results support our arguments that using entities to represent composites enables users to better understand a domain.

Keywords: Conceptual modeling, information systems development, ontology, part-of relations, aggregation, composition, meronymic relations, mereology, mereotopology

## Introduction

The notion that one thing may be a “part of” or a “component of” another thing (e.g., a wheel is part of a car) seems fundamental to the way humans conceive some types of phenomena in the perceptual worlds they create. For this reason, part-whole (meronymic) relations have been a focus of psychologists concerned with human cognition (e.g., Winston et al. 1987) and philosophers concerned with ontology (the nature of the world) (e.g., Bunge 1977). Indeed, within the field of philosophy, part-whole relations are the primary focus of the subfields of mereology and mereotopology (e.g., Gerstl and Pribbenow 1996; Simons 1987; Smith 1996; Varzi 1996). Moreover, recently philosophers also have begun to focus specifically on the mereology of artifacts (Simons and Dement 1996).

Part-whole relations also have long been a concern of information systems and computer science researchers and practitioners concerned with finding better ways to model the world. For instance, they feature in early work on “database abstractions” (Smith and Smith 1977) and extensions to Chen’s (1976) entity-relationship model (Teorey et al. 1986). Subsequent to this early work, they have remained a focus of researchers concerned with conceptual modeling (e.g., Storey 1991). More recently, part-whole relations feature in object-oriented conceptual modeling approaches (e.g., Artale et al. 1996, Opdahl et al. 2001)—in particular, the de facto standard for object-oriented conceptual modeling, the unified modeling language (UML) (Rumbaugh et al. 2005).

In the context of conceptual modeling work, part-whole relations remain problematical for two reasons. First, substantive theoretical issues surrounding them remain unresolved. For example, Rumbaugh et al. (2005, p. 164) state: "The aggregation (part-whole) relationship is transitive and antisymmetric across all aggregation links, even across those from different aggregation associations." Winston et al. (1987, pp. 431-432) illustrate the difficulties with such claims using the following example: If Simpson's arm is a part of Simpson, and Simpson is a part of the Philosophy Department, by transitivity Simpson's arm is a part of the Philosophy Department. They point out that the validity of this conclusion is questionable because "part of" has two different meanings in their example. One is a component-object relation (arm is a part of Simpson). The other is a member-collection relation (Simpson is a part of the Philosophy Department). Moreover, Winston et al. argue that the conclusion is "false (as well as strange), since Simpson's arm is neither a component nor a member of the Philosophy Department" (p. 432). Clearly, a deeper understanding of different meanings of part-whole relations is needed as a basis for designing conceptual modeling languages and methods (Wand and Weber 2002).

Second, alternative ways of representing part–whole relations in conceptual models have been proposed. In particular, composite things are sometimes represented as entities (classes) and sometimes represented via relationships (associations) between the components of the composite. A small amount of theoretical work has been undertaken to evaluate the merits of these alternative representations (e.g., Wand et al. 1999), but much still needs to be done. Moreover, to the best of our knowledge, no rigorous empirical evaluation of alternative representations of part–whole relations has so far been undertaken.

In this paper, therefore, we describe research we undertook to extend prior theory about and to evaluate empirically alternative conceptual-modeling representations of part-whole relations. Specifically, our motivation was to appraise whether entity-based (class-based) or relationship-based (association-based) representations of part-whole relations in a conceptual model enable application end users to better understand the semantics of their domain as represented by the conceptual model. More generally, our research is part of a larger agenda that is aimed at improving the clarity of the domain semantics represented via conceptual models. In this regard, as model-driven architectures gain increasing prominence as a means of developing and implementing information systems, having accurate, complete, and clear representations of domain semantics (as the first step in a series of automated or semiautomated model transformations toward executable code) assumes greater importance (Frankel and Parodi 2004). Similarly, as more organizations place increasing reliance on industry-standard conceptual models (e.g., the HL7 models in the health services area, http://www.hl7.org/, the SID models in the telecommunications area, http://www.tmforum.org/, and the SCOR models in the supply-chain area, http://www.supply-chain.org), having accurate, complete, and clear representations of domain semantics assumes greater importance.

The remainder of the paper proceeds as follows. The next section provides the theoretical background to the research. The third section articulates and provides the rationale for the proposition we tested empirically. The fourth section describes the empirical method we used to test the proposition. Our results are presented in the fifth section. The sixth section discusses some implications of our results for practice and research. Finally, we outline future research directions in the seventh section.

## Theory

Figures 1 and 2 show two examples of how part-whole relations have been represented in two widely used conceptual modeling/database textbooks. Both representations show a composite represented implicitly via a relationship or an association construct. $^{2}$

Figure 1 is a section of an entity-relationship diagram from Elmasri and Navathe (2004, p. 102). It shows a “faculty” entity linked to a “grad\_student” entity via a “committee” relationship. In their explanation of this section of the diagram, however, Elmasri and Navathe clearly intend the “committee” to be a composite entity that has “faculty” entities and “student” entities as components. They comment, “We also relate the graduate student to a faculty advisor... and to a thesis committee ... if one exists” (p. 101, emphasis added).

Figure 2 is a UML diagram from Teorey et al. (2006). In relation to this diagram, Teorey et al. provide the following semantics: “Engineers are divided into groups for certain projects. Each group has a leader” (p. 91). Their use of an aggregation symbol on the recursive association in the diagram (hollow diamond) “indicates part-of associations, where the parts have an independent existence” (Teorey et al. 2006, p. 36). Thus, the association with the aggregation symbol in Figure 2 implicitly represents a “group” composite that has “engineers” as components (some of whom lead the group). $^{3}$

Figures 3 and 4 provide alternative representations of the domains manifested in Figures 1 and 2. In contrast to Figures 1 and 2, both figures show a composite represented explicitly rather than implicitly. In particular, “committee” is a separate entity type in Figure 3, and “group” is a separate class in Figure 4. In Figures 3 and 4, note that we have made some assumptions about the domain semantics that might underlie Figures 1 and 2 (semantics that are not clear from an examination of Figures 1 and 2). For instance, in Figure 3 we have assumed that a particular (thesis) committee can have only one graduate student as a member and that a particular graduate student can be a member of only one committee, and in Figure 4 we have assumed that a group may have a leader but no subordinates.

Wand et al. (1999) contend that implicit representations of composites (like those in Figures 1 and 2) are more difficult to understand than explicit representations of composites (like those in Figures 3 and 4). Their arguments are founded on two theories. The first is an ontological theory proposed by Bunge (1977). This theory articulates a set of rigorously defined constructs to describe all types of phenomena in the world. Furthermore, it provides the bases by which a particular phenomenon can be identified as an instance of a specific theoretical construct. Bunge's theory is primarily an instance of an analytical theory (Gregor 2006, pp. 622-624), although it also has explanatory and predictive elements. As such, an implicit claim underlying the theory is that classifying phenomena according to the theory will aid analysis in some way.

Based on Bunge's theory, Wand et al.'s analysis of composites runs as follows:

1. “The world is made of things that possess properties” (p. 497). Things and properties are the two atomic constructs needed to describe the world.

2. Every thing in the world possesses one or more properties (there are no bare things) (p. 498).

3. Properties themselves cannot have properties. Moreover, properties cannot exist by themselves. They must attach to some thing (p. 498).

4. Two types of properties that exist in the world are intrinsic properties, which depend on one thing only, and mutual properties, which depend on two or more things (p. 498).

5. Two things interact (are coupled) when a history of one thing (manifested as a sequence of the thing's states) would be different if the other thing did not exist (p. 503).

6. The existence of a mutual property between two things can indicate that they interact with each other. Mutual properties that manifest interactions between two things are called binding mutual properties (p. 503).

![](/api/attachments/FD6WK6DB/fulltext/images/f04b9d6cb12544f6d09c54861ba33efd9adaf64544f2eb2a00b072cf4de7e0e9.jpg)  
Figure 1. "Committee" Composite Represented as an ER Relationship (Source: Elmasri /Navathe FUNDAMENTALS OF DATABASE SYSTEMS, p. 102, Figure 4.9, "An EER Schema for a University Database," © 2007, 2004 Shamkant B. Navanthe & Ramez A. Elmasri. Reproduced by permission Pearson Education, Inc.)

![](/api/attachments/FD6WK6DB/fulltext/images/27af1cbd08c086313b195b9745d1f4ab9b95ec330714a560609024f2b952bf47.jpg)  
Figure 3. "Committee" Composite Represented as an ER Entity

7. "Two things may associate to form another thing." A thing is a composite if and only if it is formed from the combination of at least two other things. Otherwise, it is a simple thing (p. 504).

8. Every composite thing possesses emergent properties, properties that are not possessed by the components of the composite (p. 504).

According to Bunge's theory, a composite is clearly a thing and not a property (either intrinsic or mutual). The reason is that composites possess properties. For instance, they must at least possess the emergent binding mutual property of being related to their components, because their histories depend on the histories of their components. If composites are conceived as properties, however, they cannot themselves have properties (number 3 above). Thus, they must be things.

![](/api/attachments/FD6WK6DB/fulltext/images/013f56d7d03ed469af57b0da450aa830c7f33037b43e3f891b1aae5a5bd948f5.jpg)  
Figure 2. "Group" Composite Represented as UML Association (Source: Database Modeling and Design: Logical Design (4th ed.), T. Teory, S. Lightstone, and T. Nadeau, p. 91. Copyright © 2006, Elsevier)

![](/api/attachments/FD6WK6DB/fulltext/images/5cc316528cbad766c7555f97530b7b1df9c3aafc7da84f4b4d015dd626989d83.jpg)

The second theory on which Wand et al.'s arguments are founded is Wand and Weber's (1993) theory of ontological clarity. This theory seeks to account for variations in the ability of users of conceptual schema diagrams to understand the semantics of the real-world domain represented by the diagrams. The theory is an example of a recognition and representation theory of human vision systems (e.g., Dretske 1995; Edelman 1999; Palmer 1978). In these types of theories, the nature of the mapping between representations and real-world phenomena is a critical determinant of humans' ability to recognize and understand the phenomena being represented:

On the most general possible account, both the representations and their targets are treated formally as sets. Within this framework, representation becomes a mapping....The best situation one can hope for is an isomorphism between the domain and the range of the mapping, in which case it must be, formally, “one-to-one” and “onto” (Edelman 1999, pp. 20-22).

In Wand and Weber's (1993) theory, ontological clarity is achieved only when the mapping between a set of conceptual modeling constructs and a set of ontological constructs is isomorphic. They identify four situations where they argue that lack of isomorphism will undermine a user's ability to understand a conceptual model. $^{4}$

1. Construct overload: A single modeling construct maps to two or more ontological constructs.

2. Construct redundancy: Two or more modeling constructs map to a single ontological construct.

3. Construct deficit. An ontological construct exists that is not the image of a mapping from any modeling construct.

4. Construct excess: A modeling construct does not map onto any ontological construct.

Note that recognition and representation theories, and thus Wand and Weber's (1993) theory of ontological clarity, are rooted in computational and algorithmic theories rather than neurophysiological theories of human visual object recognition systems (Biederman 1987; Bruce et al. 2003). Nonetheless, Marr's (1982) seminal work shows why computational and algorithmic theories take precedence over neurophysiological theories and thus need to be developed first: "In order to study bird flight we have to understand aerodynamics; only then do the structure of feathers and the different shapes of bird wings make sense" (p. 27).

As a computational and algorithmic theory, the theory of ontological clarity provides a rationale for why ontological clarity is important—namely, ambiguous mappings between a representational construct and the phenomenon it is intended to represent confuse humans about the nature of the phenomenon. The theory does not articulate neurophysiological processes, however, to support why this outcome will occur. Nonetheless, as Marr points out, there is little point to articulating neurophysiological theories if the computational and algorithmic theories they are supposed to support are not robust.

Similarly, the theory of ontological clarity is not a psychological theory of human visual object recognition systems. Again, following Marr, proposing psychological theories to provide a rationale for why ontological clarity is important to human understanding of represented phenomena is problematical unless the computational and algorithmic theory first proves robust. $^{5}$

The theory of ontological clarity is also not a contingency theory. In other words, according to the theory, instances of construct overload, construct redundancy, construct deficit, and construct excess will always undermine users' understanding of conceptual models. Contextual factors like domain complexity do not moderate associations among components in the theory. Similarly, the choice of syntax (e.g., a rectangle or a circle) to represent a modeling construct is not a feature of the theory. Irrespective of how specific modeling constructs are represented syntactically, the theory predicts that users' understanding of a conceptual model will be undermined whenever it lacks ontological clarity.

## Proposition Development

When relationships are used to represent composites, construct overload arises, because a single modeling construct is used to represent two ontological constructs (a mutual property and a composite). As a result, ontological clarity is undermined, and Wand and Weber (1993) predict that users of a conceptual model will have greater difficulty understanding the semantics of the real-world domain represented by the model.

Ambiguities about the semantics of a domain arise in several ways if relationships or associations are used to represent both composites and mutual properties. First, users of a conceptual model must employ tacit knowledge to determine whether the relationship or association represents a composite thing or a mutual property of (relationship between) two or more things. For example, in Figure 1, the label “committee” could be interpreted as a mutual property or relationship (association) between a “faculty” thing and a “grad\_student” thing. It could also be interpreted as a composite thing called “committee” with components “faculty” and “grad\_student.” The composite thing “committee” would then have a separate existence with its own properties (e.g., the size of the committee and the date it was created).

Second, if intrinsic properties are attached to the relationship/association, are these properties intended as properties of the relationship/association or properties of the composite? For example, in Figure 2, assume that an attribute called “performance rating” is attached to the recursive association on the class “engineer” via an association class. Does the performance rating apply to the role that individual engineers play as a leader of or a subordinate in a group? Or is it an emergent property that applies to the composite “group” comprising engineers who lead and are subordinates in the group? In short, with the composite represented as an association, it is not clear whether the performance rating applies to a component of the composite or the composite itself.

Third, in a similar vein, if mutual properties are attached to the relationship or association, are these properties intended as properties of the relationship or association or properties of the composite? For example, in Figure 2, assume that an association class called “manager” is attached to the recursive association on the “engineer” class. $^{6}$ Does the “manager” class indicate the manager of a pair of engineers, one of whom is a leader of a group and the other of whom is a subordinate in a group? Or does the “manager” class apply to the group of engineers, given that the recursive relationship has an aggregation symbol at one of its ends? In short, does the “manager” class apply to a specific pair of engineers, considered as a stand-alone pair, or a set of pairs of individuals, all of whom are in a particular group?

Fourth, if composites are represented as relationships, subclasses of the composite cannot always be shown easily. For example, in Figure 1, assume that the size and makeup (and perhaps other characteristics) of committees vary depending on whether the thesis on which a student works is deemed to be cross-disciplinary. As a first step, we might attach an optional attribute to the “committee” relationship to show the name of any cross-discipline that must be covered by the committee when a thesis is deemed to be cross-disciplinary. Depending on the nature of the cross-discipline, however, we may need to include certain types of experts on the committee. Again, optional attributes might be attached to the “committee” relationship to allow for the possible existence of these experts. Through judicious use of optional attributes, therefore, we can show the varying phenomena that arise as a function of whether a graduate student is undertaking a cross-disciplinary thesis. As more optional properties are used, the “laws” and behavior that apply to committees become increasingly difficult to specify and to comprehend. Such difficulties motivate the use of subclasses (Wand et al. 1999). If “committee” is shown as a relationship, however, subclasses cannot be used.

Fifth, often the semantics that apply to the phenomena are unclear. For instance, in Figure 2, can an engineer be a leader in one group and a leader or subordinate in another group? The UML multiplicities in Figure 2 show that (1) an engineer leads from zero to many subordinate engineers (presumably in the one group), and (2) a subordinate engineer may be led by only one engineer (presumably in the one group). Nonetheless, the multiplicities do not enable us to determine whether being a lead engineer in one group precludes an engineer from being a subordinate engineer in another group. Moreover, UML seems to provide no way to represent this constraint in the diagram. On the other hand, if “group” were represented as a separate class, and engineers were divided into “leader” and “subordinate” subclasses, this constraint could be shown by indicating whether the two subclasses were mutually exclusive.

Sixth, if composites are shown via recursive relationships or associations, existence constraints are unclear. For instance, in Figure 2, can a group exist with a leader engineer but no subordinate engineer? The multiplicities in Figure 2 show that not all engineers are leaders. Can engineers lead themselves, however? Would this representation be used if a group has only one member (in other words, the group member is also the leader of the group)?

In light of our arguments above, we contend that the choice of representation for composites and components is important in terms of users' ability to elicit the meaning of the phenomena described via the representation. When composites are represented as entities rather than relationships or associations, conceptual models provide clearer semantics about the domain being represented. In this regard, the theory of ontological clarity provides a formal means of identifying when and why two conceptual models differ in terms of the amount of and precision of the semantics they convey to users (in other words, why the two models do not have information equivalence).

Prima facie, having an ontologically clear conceptual model might always seem preferable if such models contain a greater amount of and more-precise semantics. In experimental work, however, Bowen et al. (2004) found that end users who employed large, ontologically unclear conceptual schema diagrams as a basis for formulating SQL queries on a database made fewer errors, took less time, and were more confident in the accuracy of their queries than users who employed large, ontologically clear conceptual schema diagrams. Similarly, Bodart et al. (2001) found that users who employed ontologically unclear conceptual schema diagrams performed better in diagram reconstruction and comprehension tasks than users who employed ontologically clear diagrams. Thus, the contexts in which ontologically clear conceptual models assist users still need to be teased out and understood better.

Moreover, lack of ontological clarity in conceptual models can take many forms. For instance, Bowen et al. and Bodart et al. tested empirically whether instances of construct excess undermined users' ability to elicit semantics from a conceptual model. They focused on the impact of optional attributes and relationships. In Bunge's ontology, optional attributes and attributes have no place (Bunge 1977, pp. 60-61). Thus, an optional attribute and an optional relationship are conceptual modeling constructs that have no corresponding ontological construct. Our focus is on whether undermining ontological clarity via instances of construct overload affects users' ability to elicit the semantics from a conceptual model. We are interested in the effects on users of using the same modeling construct (an association class) to represent two different ontological constructs (a class of things and a mutual property in general). More broadly, the differential effects on users of various practices that undermine the ontological clarity of conceptual models (and their interactions) need to be assessed empirically.

In this light, we tested the following proposition empirically to determine whether ontologically clear representations of part-whole relations led to better understanding of these relations:

Proposition: Conceptual models that use an entity/class construct to represent a composite will enable their users to better understand the semantics associated with the composite than conceptual models that use a relationship/association construct to represent the composite.

## Research Method

To test our proposition, we chose an experiment so that we could control extraneous factors that might confound any impacts of alternative representations of part-whole relations on how well users understand these relations.

## Design and Measures

A two-group, post-test only experimental design was used with one active between-groups factor. This factor, type of representation, had two levels. The first, the ontologically clear level, had both composites and components in part-whole relations represented as entity classes in a UML class diagram. An association construct was used to show the relationship between composites and components. In this way, construct overload was avoided in the diagram. The second, the ontologically unclear level, had components represented as entity classes in a UML class diagram. Composites were represented, however, via associations between components. Thus, construct overload existed in the diagram because the association construct was used to represent both relationships and composites. As a result, the amount and precision of the semantics conveyed via the ontologically clear diagrams should be greater than the amount and precision of the semantics conveyed via the ontologically unclear diagrams.

Choice of a dependent variable involved our finding a way to measure how well the conceptual schema diagrams conveyed semantics to their users and, at the same time, seeking to preclude as many confoundings as possible in assessing this outcome. For instance, in practice, users of conceptual schema diagrams might elicit semantics from a diagram in consultation with others (e.g., an application end user with an analyst). If the outcome of such interactions were to be assessed, however, other factors potentially confound how well conceptual schema diagrams convey semantics to their users (such as the quality of interactions among users). For this reason, following Mayer (1989), prior research has employed measures of performance based on recall, comprehension, and problem-solving tasks (e.g., Bodart et al. 2001; Gemino and Wand 2005; Parsons and Cole 2005). These tasks act as a proxy for how well users elicit semantics from conceptual schema diagrams in practice. Nonetheless, in past psychological research they have enabled effective experimental control over and valid and reliable measurement of how well humans elicit meaning from diagrams.

In this research, we used problem-solving performance as our dependent variable. Relative to recall and comprehension performance, problem-solving performance provides a better indicator of someone's “deep” understanding of a domain (see, e.g., Bloom 1956). It also incorporates comprehension performance. If problem solvers comprehend a domain better, they are better able to structure their problem space. Better-structured problem spaces in turn facilitate problem solving (e.g., Voss and Post 1988).

We also see problem-solving tasks as an important way in which analysts might engage application end users in validating a conceptual model. In the context of UML, problems are akin to “use-case” scenarios. We believe that solving problems using a conceptual model is more likely to surface incorrect or incomplete semantics with the model than other techniques for validating models (for example, having analysts ask questions of application end users in the hope that users will identify defects in the model). In this regard, end users’ solutions to problems can be used as the basis for a well-directed, purposive dialog between analysts and application end users about the accuracy and completeness of the domain semantics represented by a conceptual model.

To reduce potential confounding effects from prior knowledge of the domain being modelled, we formulated our problem-solving tasks carefully so that participants in our experiment who provided solutions based on prior domain knowledge were unlikely to have correct answers. Achieving this outcome in practice would also be important if problem-solving tasks were to be used as a means of validating a conceptual model. As a result, our tasks involved more elements of comprehension than those used in some earlier research where prior domain knowledge and tacit knowledge were perhaps more important to success in the problem-solving tasks given to participants (e.g., Bodart et al. 2001; Gemino and Wand 2005).

We measured how well participants understood the domain represented in the UML class diagram via problem solution accuracy. We also used two ancillary measures of performance: (1) time taken to provide a problem solution, and (2) perceptions of the ease of use of the UML class diagram. If the ontologically clear class diagram better communicated domain semantics to the experimental participants, participants should solve problems faster. Similarly, if participants believed they had done well at the problem-solving tasks, they should rate the ontologically clear class diagram as easier to use. We were circumspect about the likely outcome with both ancillary measures, however, because the ontologically clear class diagram was syntactically more complex than the ontologically unclear class diagram (i.e., it contained more diagrammatic elements).

## Materials

We used five sets of materials in the experiment. The first was a summary of the UML symbols that appeared in the class diagrams provided to participants in the experiment. The summary was prepared to inform participants of the meaning of each UML symbol. In the materials provided to participants who were to receive the ontologically unclear UML class diagram, the meaning of tertiary associations was explained. $^{7}$

The second set of materials comprised two UML class diagrams (diagrams that provide a static view of phenomena) of a project-planning domain. $^{8}$ The first showed an ontologically clear conceptual model (Figure 5). In other words, both components and composites were represented as entity classes and linked via associations. The second UML class diagram showed an ontologically unclear conceptual model (Figure 6). In other words, only components were shown as classes, and composites were represented via ternary associations between component classes. The project-planning domain was chosen because it is widely understood and requires little specialized knowledge. Nonetheless, it is sufficiently rich to make some problem-solving tasks difficult. For both diagrams, data dictionaries were also prepared to show the definition of attributes notated on the diagrams.

The second set of materials, comprising Figures 5 and 6, was developed as follows:

\- We first drew a UML class diagram that included attributes for a routine project-planning domain. We checked the diagram for ontological clarity, particularly with respect to part-whole relations. We were careful to follow the UML syntax that was the “standard” at the time of our experiment.

![](/api/attachments/FD6WK6DB/fulltext/images/b35c51c116ce6d93350f2d9a421f68021da80773a3bc59bbb381ec022ce14f77.jpg)  
Figure 5. Ontologically Clear UML Class Diagram

\- Two expert data modeling practitioners and several academics then checked the class diagram for accuracy, completeness, and clarity. $^{9}$

\- Next, we derived the ontologically unclear class diagram from the clear class diagram by converting each “aggregate/composite” class to a diamond—that is, a UML association. $^{10}$ We sought to minimize changes to the layout of the diagram to mitigate a possible confounding in the experiment because of changed layout effects.

\- Finally, we included the constraints in each model and checked them for consistency (with the clear understanding that at a detailed level the constraints could not easily be made equivalent across the two diagrams). Adding further constructs or comments to the unclear model would have made it too different overall from the clear model. $^{11}$

As we indicated above, in the ontologically unclear diagram (Figure 6) we used ternary associations to represent composites implicitly. Otherwise, an implicitly represented composite cannot be associated with any other class. Prior research suggests that ternary associations/relationships are often difficult to model (or design) accurately (e.g., Batra et al. 1990; Shoval and Shiran 1997). The results in relation to comprehension of ternary relationships, however, are less clear-cut. For instance, when ternary relationships are modeled using a diamond symbol (as per Figure 6), Shoval and Frumerman (1994) found high levels of comprehension in relation to the “facts” they represent. In any event, if we had not used ternary relationships to represent implicit composites, we could have tested users’ ability to elicit semantics only with very simple models (perhaps better conceived as model fragments). $^{12}$ In short, our experiment would have dubious merit.

![](/api/attachments/FD6WK6DB/fulltext/images/45785a07d175ee053b6b32ed681707770cd0d68dc8b3a7167b14608ffcf598ce.jpg)  
Figure 6. Ontologically Unclear UML Class Diagram

The third set of materials comprised 11 problem-solving questions (Appendix A), to which participants had to give a response of “possible,” “not possible,” or “unsure.” The questions were the result of extensive discussions among us. We designed them to ensure they (1) provided good coverage of the different semantics represented in the UML diagrams, (2) were representative of domain problems that application end users might have to solve, (3) had different levels of complexity, and (4) forced participants to use the UML class diagrams to obtain a correct answer rather than rely on tacit knowledge of the domain. Nine of the 11 questions were designed to force participants to focus on semantics that we believed would be difficult to understand in the ontologically unclear diagram. Two questions seeded randomly among the 11 questions (questions 4 and 10 in Appendix A), however, were designed to force participants to focus on semantics that should have been equally easy (or difficult) to elicit from both the ontologically clear and ontologically unclear diagrams. $^{13}$ In essence, these two questions constituted baseline questions. They were chosen to provide us with some assurance that any performance differences between the two participant groups could be ascribed to the experimental treatment rather than some other confounding factor.

The fourth set of materials comprised three questions to measure participants' perceptions about the ease of use of the UML class diagram they employed in their problem-solving tasks. The questions were based upon Moore and Benbasat's (1991) short-form version of the instrument developed by Davis (1989) to measure perceived ease of use. The original questions were modified to suit the conceptual modeling domain. The three questions used were: (1) overall, I believe it was easy for me to understand what the class diagram was trying to model; (2) overall, I believe that the class diagram was easy to use; and (3) understanding the class diagram was difficult.

The fifth set of materials comprised a “personal-profile” questionnaire to obtain information about participants’ academic qualifications, the industry in which they worked, the number of years they had spent in the workforce, the number of years they had spent in their current position, and the extent to which they had previously been involved with any form of modeling.

## Participants

Participants in the experiment were 30 individuals working in industry whom we knew and who were willing to help us with the experiment. All acted as surrogate application system end users in the experiment. To the extent end users cannot understand the semantics of a conceptual model, they may make errors in validating a conceptual model prepared by an analyst. Similarly, they may make errors when they rely on the model for other purposes, such as formulating a query in SQL to extract information from a database.

We might have used other types of users of conceptual models—for instance, analysts or programmers. We chose to focus on end users, however, because (1) they are an important class of users of conceptual models, and (2) variations in knowledge about and experience with conceptual modeling methods was less likely to confound our experimental results.

Table 1 shows selected demographic data about participants. Nine had information systems/technology qualifications. We still used them as participants because they did not play a technical information technology role in their organizations. Four were near completion of their bachelors' degrees and had at least 5-years' full-time work experience in industry. Despite not having tertiary qualifications, they were deemed appropriate participants because of their work knowledge and experience. The remaining participants all had at least a bachelor's degree. Fourteen had no modeling experience. The remainder had minor experience of one or two modeling techniques like flowcharts, financial models, UML, data flow diagrams, entity-relationship diagrams, and collaboration models.

## Procedures

Participants were first assigned randomly to one of the two treatments (15 per treatment). They were then run singly through the experiment. When they arrived to undertake the experiment, they were given a consent form and a sheet to obtain demographic and experiential information about them. The nature of the experiment, the tasks they were to undertake, and the goals they were to strive to achieve were also explained to them.

Next they were given the document that explained the UML symbols. The nature of the symbols and some example uses of the symbols were discussed with them. Any questions they had were answered. This process continued until participants indicated they felt confident with the UML symbols and that they were ready to undertake the problem-solving tasks. Participants retained and could refer to the summary document of UML symbols throughout the experiment.

When participants indicated they were ready to begin, they were then given either the ontologically clear or ontologically unclear UML class diagram to peruse. They could retain the diagram throughout the experiment. Participants then undertook the problem-solving tasks. They were asked to speak aloud as they attempted to solve each problem-solving question. Their verbalizations were tape-recorded. The times they took to answer each problem-solving question also were recorded. In addition, notes were made based on participant reactions, queries, and approaches to each problem-solving question. Recall, participants had to choose from one of three possible answers to the problem-solving questions: “possible,” “not possible,” and “not sure.” Finally, participants completed the perceived ease-of-use instrument. They were then thanked and dismissed. On average, the experiment took about 60 minutes to complete.

<table><tr><td colspan="4">Table 1. Participant Demographic Data</td></tr><tr><td>Industry Sector</td><td>Ontologically Clear</td><td>Ontologically Unclear</td><td>Total</td></tr><tr><td>Banking &amp; Finance</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Consulting</td><td>4</td><td>3</td><td>7</td></tr><tr><td>Contact Centers</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Health</td><td>0</td><td>1</td><td>1</td></tr><tr><td>IT</td><td>8</td><td>5</td><td>13</td></tr><tr><td>IT/Accounting</td><td>1</td><td>1</td><td>2</td></tr><tr><td>IT Consulting</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Time in Workforce</td><td>Ontologically Clear</td><td>Ontologically Unclear</td><td>Total</td></tr><tr><td>&lt;1 Year</td><td>5</td><td>5</td><td>10</td></tr><tr><td>1-5 Years</td><td>5</td><td>4</td><td>9</td></tr><tr><td>5-10 Years</td><td>0</td><td>4</td><td>4</td></tr><tr><td>10-15 Years</td><td>4</td><td>0</td><td>4</td></tr><tr><td>&gt;20 Years</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Current Employment</td><td>Ontologically Clear</td><td>Ontologically Unclear</td><td>Total</td></tr><tr><td>&lt;1 Year</td><td>10</td><td>8</td><td>18</td></tr><tr><td>1-5 Years</td><td>4</td><td>5</td><td>9</td></tr><tr><td>5-10 Years</td><td>0</td><td>2</td><td>2</td></tr><tr><td>10-15 Years</td><td>1</td><td>0</td><td>1</td></tr><tr><td>&gt;20 Years</td><td>0</td><td>0</td><td>0</td></tr></table>

The same two of us conducted all experiments. One instructed the participant and managed the experiment overall. The other controlled the tape-recorder, observed the participant's behavior, made notes, and recorded the time taken to complete tasks.

## Results

Our data analysis involved four steps. First, we calculated scores for individual items on the problem-solving measure. Second, we performed reliability analyses on the problem-solving and ease-of-use measures. Third, we performed statistical analyses to test for treatment differences in the scores for the problem-solving, time, and ease-of-use measures. Fourth, we analyzed the qualitative data we had collected to better understand how the two treatment groups differed in terms of their performance on the problem-solving tasks.

## Data Scoring

The maximum score for solution accuracy for each problem-solving question was three. The score was calculated as follows:

1. Answer: One mark was given if the answer (“possible” or “not possible”) was correct; zero was given if the answer was incorrect or “not sure” was given as the answer (unknown to the participants, “not sure” was never a correct answer). Note that the correct answers for problems 2, 3, 5, 6, 9, and 11 differed between the ontologically clear and unclear diagrams (as per our theory, a reflection of their different capabilities to represent the domain semantics). $^{14}$ For instance, with the ontologically clear diagram, the correct answer to problem 2 is “possible.” Because team leader is weakly aggregated in the ontologically clear diagram, the team can still exist if the team leader resigns. In the ontologically unclear diagram, however, the correct answer to problem 2 is “not possible.” Because a team is an instance of a ternary association that links team leader, team member, and project, the team association instance will no longer exist if the instance of team leader is removed.

2. Explanation: A judgment on the marks to be awarded for this item was made based on the participant's explanations, our notes, and the audio recording. Clear explanations (matching sample answers) to support an answer were awarded one mark. Moderately clear explanations (partially matching sample answers) were awarded a half mark. Unclear explanations (not matching sample answers) were awarded zero marks.

3. Interpretation: Again, a judgment on the marks to be awarded for this item was made based on the participant's explanations, our notes, and the audio recording. Clear interpretations of those aspects of the domain on which the problem-solving question focused were awarded one mark. Moderately clear interpretations were awarded a half mark. Unclear interpretations were awarded zero marks.

We also used participants' explanations, our notes (based on our observations of a participant's problem-solving behavior), and the audio recording to determine whether participants used tacit knowledge to solve the problems. Initially we intended to exclude any participants who used tacit knowledge from our analyses. Only 11 used tacit knowledge—6 in the ontologically clear model, and 5 in the ontologically unclear model. Excluding these participants from our analyses produced little change in our results. Retaining these participants, however, adds to the external validity of our results. Thus, their scores are included in the analyses reported in the next two subsections.

Two of us independently scored the three problem-solving solution accuracy measures on preformatted scoring sheets. Few differences arose between the two sets of scores (Pearson r for the two sets of scores was .981 for the ontologically clear model and .969 for the ontologically unclear model). Where differences did occur, they were discussed and reconciled. Recall, the solution accuracy answer scores were straightforward to assign because a participant's answer was either correct or incorrect. The explanation and interpretation scores, however, required that a judgment be made. Note, we could not use independent coders to score the explanation and interpretation measures because good judgments could not be made in the absence of a coder (1) understanding the nature of the research, and (2) being present when the experiment was in progress. In essence, the notes and audio recordings provided the stimuli for our recalling events that took place as the experiment progressed.

## Reliability Assessment

Cronbach alpha for the 11-item problem-solving instrument was .83. Deletion of any problem-solving question produced no marked effect on the instrument's reliability score. Cronbach alpha for the three-item ease-of-use instrument (third item reverse scored) was .81. Deletion of questions 2 and 3 produced a moderate drop in reliability (.13 and .08), whereas deletion of question 1 produced only a minimum drop in reliability (.003). In light of these results, we retained all items on both instruments.

## Quantitative Data Analysis

Table 2 shows descriptive statistics for the total accuracy, total time, and ease-of-use measures. Because the total accuracy and total time scores for the 11 problem-solving questions are relatively uncorrelated (r = -.216, p = .251), we used an independent samples multivariate t-test to compare the performance of the ontologically clear and ontologically unclear treatment groups rather than multivariate analysis of variance (Tabachnick and Fidell 1996, p. 402). For all three dependent measures, Levene's test indicated that the variances of the ontologically clear and ontologically unclear groups could be considered to be the same.

For problem-solving accuracy, the difference between the two groups was statistically significant using a two-tailed multivariate t-test (t = 7.465, df = 28, p < .001). $^{15}$ Eta squared was .666, which means that 66.7 percent of the variance in problem-solving accuracy is accounted for by the treatment. For the problem-solving time performance measure, however, the difference between the ontologically clear and ontologically unclear groups was not significant using a two-tailed test $t = -1.166, df = 28, p = .253$ . Similarly, for the ease-of-use measure, the difference between the two groups was not statistically significant using a two-tailed test $t = 0.371, df = 28, p = .713$ .

Table 2. Descriptive Statistics for Dependent Measures

<table><tr><td>Group</td><td>Measure</td><td>Mean</td><td>Std. Dev.</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td rowspan="3">Ontologically Clear (n = 15)</td><td>Problem Solving</td><td>24.533</td><td>6.022</td><td>-0.44</td><td>-0.481</td></tr><tr><td>Time</td><td>33.244</td><td>11.464</td><td>0.089</td><td>-1.534</td></tr><tr><td>Ease of Use</td><td>8.94</td><td>2.417</td><td>-0.242</td><td>0.175</td></tr><tr><td rowspan="3">Ontologically Unclear (n = 15)</td><td>Problem Solving</td><td>10.7</td><td>3.904</td><td>-0.159</td><td>0.52</td></tr><tr><td>Time</td><td>38.989</td><td>15.258</td><td>0.896</td><td>1.587</td></tr><tr><td>Ease of Use</td><td>8.56</td><td>3.143</td><td>-0.049</td><td>-0.962</td></tr><tr><td rowspan="3">Total (n = 30)</td><td>Problem Solving</td><td>17.617</td><td>8.623</td><td>0.278</td><td>-1.074</td></tr><tr><td>Time</td><td>36.117</td><td>13.578</td><td>0.774</td><td>1.246</td></tr><tr><td>Ease of Use</td><td>8.75</td><td>2.761</td><td>-0.161</td><td>-0.604</td></tr></table>

To identify how the two groups differed in terms of problem-solving accuracy, follow-up univariate t-tests were performed for each problem-solving question. For each group, Table 3 shows the mean accuracy scores and standard deviations for each problem-solving question. For 8 of the 11 questions, Table 3 also shows that the ontologically clear group outperformed the ontologically unclear group using a two-tailed univariate t-test (p < .05). Moreover, using a one-tailed t-test, the ontologically clear group also outperformed the ontologically unclear group on question 11 (p = .04). As expected, only for questions 4 and 10 (the baseline questions) were the means of the two groups not statistically different. If a Bonferonni adjustment procedure is used with a family level of significance of .05, however, the individual tests must be significant at the .0045 level. Even with this conservative test procedure, 6 of the 11 questions still show significant differences between the two groups.

In summary, we obtained strong support for our proposition based on the overall accuracy measure of problem-solving performance. Furthermore, statistical tests of each problem-solving question showed that this support derived from performance differences pertaining to those questions where we expected differences to exist. We obtained no support for our proposition, however, using the time and ease-of-use measures. We suspect this outcome reflects that the ontologically clear class diagram was syntactically more complex than the ontologically unclear class diagram.

## Qualitative Data Analysis

A qualitative analysis of the data was undertaken to obtain insights that we could not obtain via the quantitative analysis about the effect of the treatment. Recall, each participant's verbalizations were tape-recorded. Moreover, we took notes of participants' reactions and responses to the experimental materials. Our goal was to obtain a deeper understanding of participants' thought processes as they attempted to answer the problem-solving questions.

As a first step in analyzing the transcriptions and notes, we derived iteratively a set of problem-solving phases that we concluded participants would most likely traverse as they attempted to answer the problem-solving questions. In essence, we employed a model-based approach to verbal protocol analysis. Following Ericsson and Simon (1993, pp. 198-199), we formulated a tentative model, evaluated it against participant protocols and our notes, and then refined the model until we concluded the model's phases provided a comprehensive and useful way of categorizing those verbalizations in the participant protocols that interested us. By first articulating this model, we could then identify and code specific verbalizations that we believed were pertinent to testing our proposition.

The seven problem-solving phases we used as the basis for our coding were

\- Phase 1: Can I understand the question asked/problem posed?

\- Phase 2: What are the key real-world concepts in the question asked/problem posed?

<table><tr><td colspan="4">Table 3. Accuracy Performance on Problem-Solving Questions</td></tr><tr><td rowspan="2">Question</td><td>Ontologically Clear(n = 15)</td><td>Ontologically Unclear(n = 15)</td><td rowspan="2">t-Statistic(2-tail Significance)</td></tr><tr><td>Mean(Standard Deviation)</td><td>Mean(Standard Deviation)</td></tr><tr><td>1</td><td>2.467(1.077)</td><td>0.933(1.033)</td><td>3.980(.000)</td></tr><tr><td>2</td><td>1.500(1.309)</td><td>0.467(1.060)</td><td>2.376.025</td></tr><tr><td>3</td><td>2.100(1.137)</td><td>0.200(0.561)</td><td>5.805(.000)</td></tr><tr><td>4</td><td>2.233(1.208)</td><td>2.100(1.242)</td><td>0.298(.768)</td></tr><tr><td>5</td><td>2.667(0.990)</td><td>0.400(0.910)</td><td>6.859(.000)</td></tr><tr><td>6</td><td>2.400(1.121)</td><td>0.333(0.617)</td><td>6.254(.000)</td></tr><tr><td>7</td><td>2.367(1.043)</td><td>1.033(0.935)</td><td>3.687(.001)</td></tr><tr><td>8</td><td>1.900(1.256)</td><td>1.000(0.926)</td><td>2.233(.034)</td></tr><tr><td>9</td><td>2.467(1.126)</td><td>0.400(1.056)</td><td>5.187(.000)</td></tr><tr><td>10</td><td>1.900(1.285)</td><td>2.033(1.316)</td><td>-0.281(.781)</td></tr><tr><td>11</td><td>2.533(0.990)</td><td>1.800(1.207)</td><td>1.189(.080)</td></tr><tr><td>Total</td><td>24.533(6.022)</td><td>10.700(3.904)</td><td>7.465(.000)</td></tr></table>

\- Phase 3: Can representations for these key real-world concepts be found in the diagram?

\- Phase 4: Can I identify clearly the subset of the model on which I should focus to answer the problem posed/question asked?

\- Phase 5: Can I articulate clearly the semantics of the subset of the model that is my focus?

\- Phase 6: In the context of the model semantics, can I solve the problem asked?

\- Phase 7: Phase change—this represents the sequence and iteration undertaken by participants between phases 1 and 6.

The primary coding process involved the two of us who were present at each experiment first choosing a participant at random. We then jointly examined the participant's transcript of verbalizations for statements of concern that indicated she/he was having difficulty answering the problem-solving question. Where necessary, we also used our notes to clarify our understanding of a participant's concern. We next coded each participant's statement according to the phase that we believed she or he was traversing. $^{16}$

For each participant, each problem-solving question, and each problem-solving phase, we then recorded in a table the nature of the statement of concern. $^{17}$ For example, statements made by participants about their difficulties in interpreting the semantics of a model belong in phase 5 (the type of concern might have been confusion over the meaning of a ternary association or cardinality restriction). When coding was complete, the table provided us with a breakdown of the number of and types of statements of concern for each question, each participant, and each model. We anticipated that most statements of concern would be coded under phase 5, especially in relation to the ontologically unclear model.

After coding 10 participants' protocols (5 chosen at random who received the ontologically clear treatment, and 5 chosen at random who received the ontologically unclear treatment), no new types of statements of concern were emerging. Moreover, no marked differences in the distribution of statements of concern across problem-solving phases were emerging. In this light, we ceased further coding and then used the table we had created to compare the ontologically clear and unclear models. We focused on the number and types of statements of concern recorded for each problem-solving question.

Table 4 shows the total number of statements of concern for each phase and each problem-solving question made by the 10 participants whose protocols we analyzed. Note that entries in the table are sparse for the five participants who received the ontologically clear model. For instance, no statements were made for phase 2 and questions 1 and 5. Moreover, one participant completed the entire problem-solving task without uttering a single statement of concern. These outcomes suggest that (1) participants found the problem-solving tasks to be relatively straightforward, and (2) they progressed somewhat effortlessly through all phases. The maximum number of statements of concern made for each phase by any one of the participants who received the ontologically clear model was as follows: one participant made two statements in phase 3 for question 6 as she could not locate a key real-world construct; one participant made two statements in phases 4 and 5 for question 8 (her concern arose from an inability to locate the required subset of the model and then understand its semantics); and one participant made five statements in phase

5 for question 2 because she had difficulty understanding the model's notation. The remainder were single statements of concern. They were minor, and the transcripts showed that participants resolved them quickly. For example, one participant remarked that he thought one question was “silly.” Across all questions and phases, the average number of statements made by each participant who received the ontologically clear model was 5.8. For phase 5 alone (the phase that was our primary focus), participants made an average of 1.4 statements.

By comparison, more entries occurred in the table for participants who received the ontologically unclear model. The least number of statements made was in phase 4 (total of 4). The largest number of statements made was in phase 5 (total of 63). In this regard, one participant made nine statements for phase 5 in relation to a single question. Typical of statements made in phase 5 are the following: “the ternary relationship is what confuses me,” “I can’t understand why consumables and deliverables are related—what’s that got to do with anything,” “the model’s wrong,” “I’m not sure about the cardinality though,” and “it’s not simple—this is where it gets muddy for me.” Every question and every phase had at least one statement of concern. On average, participants who received the ontologically unclear model made 29.6 statements of concern. These results indicate that participants who received the ontologically unclear model had much greater difficulty responding to the problem-solving questions. The difficulties they experienced are well illustrated by one participant who at one point said, “Well, I don’t know. No, I don’t know. I honestly don’t know this one.”

The different outcomes with each model are also highlighted in phase 7, which reflects the sequence and iterations undertaken by participants between phases 1 and 6. In other words, it shows how many times participants had to return to a previous phase to work through a problem-solving question—for example, they might have reached phase 5, became confused with the semantics, and then returned to phase 1 to clarify whether they understood the question correctly. With the ontologically clear model, only three phase changes took place, two of which were for the same participant for the same question (he simply reread the question after he had experienced difficulty interpreting an aggregation diamond). With the ontologically unclear model, however, all participants made phase changes for at least one problem-solving question. In total, the 5 participants performed 17 phase changes. Of these, four were shifts from phase 5 to 1. These indicate that participants could not articulate clearly the semantics of the subset of the model on which they were focusing. As a result, they returned to the statement of the question to attempt it again. Of the 17 phase-shift statements, 8 indicated shifts from phase 6 to 5. These suggest that participants were not confident in the answers they had derived due to a semantic concern that lingered. A further 3 statements were made after participants had reached phase 6 but returned to clarify a real-world concept, reread the question, or double-check the subset of the model on which they should focus. The last two statements simply arose from lack of familiarity about a real-world concept.

<table><tr><td colspan="12">Table 4. Total Number Statements of Concern for Sample of 10 Participants</td></tr><tr><td rowspan="2">Question/Phase</td><td colspan="11">Ontologically Clear Model (Sample of 5 Participants)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>1</td><td></td><td></td><td>3</td><td>1</td><td></td><td></td><td>1</td><td>1</td><td></td><td></td><td></td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td></tr><tr><td>5</td><td></td><td>3</td><td></td><td>1</td><td></td><td></td><td></td><td>2</td><td></td><td></td><td>1</td></tr><tr><td>6</td><td></td><td>2</td><td>1</td><td></td><td></td><td></td><td></td><td>2</td><td>1</td><td>2</td><td>1</td></tr><tr><td>7</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td>2</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Question/Phase</td><td colspan="11">Ontologically Unclear Model (Sample of 5 Participants)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>1</td><td>6</td><td>1</td><td>1</td><td>3</td><td>6</td><td>1</td><td></td><td></td><td></td><td>1</td><td>1</td></tr><tr><td>2</td><td></td><td></td><td></td><td></td><td>4</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>1</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>1</td><td></td><td>3</td><td></td></tr><tr><td>4</td><td></td><td></td><td>1</td><td></td><td></td><td></td><td>2</td><td></td><td></td><td>1</td><td></td></tr><tr><td>5</td><td>12</td><td>7</td><td>4</td><td>6</td><td>11</td><td>4</td><td>2</td><td></td><td>11</td><td>4</td><td>2</td></tr><tr><td>6</td><td>4</td><td></td><td>4</td><td>5</td><td>7</td><td>1</td><td></td><td></td><td>5</td><td>3</td><td>4</td></tr><tr><td>7</td><td>3</td><td></td><td>1</td><td></td><td>6</td><td>1</td><td>1</td><td></td><td>2</td><td>2</td><td>1</td></tr></table>

Aside from supporting our quantitative findings, the qualitative results also suggest that the outcomes we have obtained from out experiment manifest treatment effects rather than some type of confounding. Thus, we are confident that our results support the fundamental proposition we have sought to test in our research.

## Implications of the Research

Our results have implications for practice and research. For practice, we believe we have strong support for our proposition that composites should be modeled as an entity or class and not as a relationship or an association. When composites are modeled as an entity or class, the resulting diagram is syntactically more complex because it contains more elements. In the context of problem-solving, however, our results suggest that the additional semantics contained in an ontologically clear diagram overcome the disadvantages associated with its higher syntactic complexity. We recommend, therefore, that practitioners be especially circumspect if they model composites as relationships or associations. They run the risk that they will undermine users' understanding of the real-world phenomena that a conceptual schema diagram is intended to represent. Syntactically simpler conceptual schema diagrams might be useful if the goal is to give users a surface-level understanding of a domain. Where a deep-level understanding of a domain is needed, however, our results support the notion that ontologically clear diagrams are essential (Bodart et al. 2001; Gemino and Wand 2005).

Our results also suggest a way in which information systems practitioners might validate the conceptual models they create. To date, little guidance has been provided on how this task should be undertaken. A typical suggestion is that users should simply be asked to examine conceptual models and provide feedback. Unless users engage fully with a conceptual model, however, they are unlikely to identify errors, omissions, redundancies, or ambiguities. Our results support those obtained by Gemino and Wand (2005) and Bodart et al. (2001) on the efficacy of problem-solving tasks as a means of testing how well conceptual models communicate the semantics of a domain to users. Thus, asking users to validate a conceptual model by requiring them to solve problems using the model (use-cases in UML) seems a fruitful way to proceed. Other approaches, such as asking users to recall models, answer comprehension questions about models, and verify models against user requirement statements, seem less efficacious (e.g., Bodart et al. 2001).

In terms of research, our results add strength to a growing body of empirical work that supports the usefulness of ontological theories, especially Bunge's (1977) theory, as a means of predicting the strengths and weaknesses of conceptual modeling grammars and practices (e.g., Bodart et al. 2001; Burton-Jones and Meso 2006; Gemino and Wand 2005; Green and Rosemann 2000; Opdahl and Henderson-Sellers 2001; Parsons 1996; Parsons and Cole 2005; Parsons and Wand 2000; Siau et al. 1997; Weber 1996). Specifically, ontological theories allow us to pinpoint which features of conceptual modeling grammars and practices are likely to be problematical and to then design empirical research to test our predictions. This approach stands in stark contrast to previous approaches that attempted omnibus feature comparisons or case-study comparisons of different grammars and methods (e.g., Olle et al. 1983). The equivocal results produced using such approaches motivated calls for better theory to guide conceptual modeling research (e.g., Floyd 1986).

The problem-solving phases we identified in our protocol analyses also should prove useful for researchers who are seeking to understand better how users of conceptual models interpret the semantics of the domain that the models are intended to represent. The phases provide a way of classifying and thus comparing different cognitive activities in which users of conceptual models engage as they attempt to interpret the semantics of the domain that underpins the model.

## Future Research Directions

Future research work might be pursued in three directions. First, ontological theory can be used to predict the strengths and weaknesses of other conceptual modeling practices. For instance, UML provides various approaches to modeling the dynamics of a domain. Bunge's (1977) theory might be used to predict whether these approaches are likely to facilitate or inhibit users' understanding of domain dynamics that involve composite things. Second, more work needs to be done on developing valid and reliable measures of users' understanding of the semantics of a domain. In the research we have described above, the problem-solving measures seem valid and reliable. Whether our results hold generally or reflect the idiosyncracies of the current research, however, is unclear. Furthermore, the measures need to take into account that users create their worlds (Hirschheim et al. 1995). Thus, shared meaning among a cohort of users may or may not exist. Third, a more-systematic articulation of and evaluation of different methods of validating conceptual models needs to be undertaken (Shanks et al. 2003). The current research suggests that methods based on having users solve problems with conceptual models have merit.

## Acknowledgments

An Australian Research Council Discovery Grant funded this research. We are indebted to participants in workshops at The University of Queensland, City University of Hong Kong, Chinese University of Hong Kong, and The University of Auckland for comments on previous versions of this paper. We also thank Daniel Moody, Steve Hitchman, Graeme Simsion, and Yair Wand for helpful comments on our research. An earlier, partial version of this paper was presented at the 23 $^{rd}$ International Conference on Information Systems, Barcelona, December 15–18, 2002. We are indebted to attendees at our presentation for helpful comments. We thank the senior editor, associate editor, and three reviewers for helpful comments on our paper.

## References

Artale, A., Franconi, E., Guarino, and N. Pazzi, L. 1996. "Part-Whole Relations in Object-Centered Systems: An Overview," Data & Knowledge Engineering (20:3), pp. 347-383.

Batra, D., Hoffer, J. A., and Bostrom, R. P. 1990. “Comparing Representations with Relational and EER Models,” Communications of the ACM (33:2), pp. 126-139.

Biederman, I. 1987. “Recognition by Components: A Theory of Human Image Understanding,” Psychological Review (94:2), pp. 115-145.

Bloom, B. S. (ed.). 1956. Taxonomy of Educational Objectives: The Classification of Educational Goals: Handbook I: Cognitive Domain, New York: Longmans.

Bodart, F., Sim, M., Patel, A., and Weber, R. 2001. “Should Optional Properties Be Used In Conceptual Modeling? A Theory and Three Empirical Tests,” Information Systems Research (12:4), pp. 384-405.

Bowen, P. L., O'Farrell, R. A., and Rohde, F. H. 2004. "How Does Your Model Grow? An Empirical Investigation of the Effects of Ontological Clarity and Application Domain Size on Query Performance," in Proceedings of the $25^{th}$ International Con

ference on Information Systems, R. Agarwal, L. J. Kirsch, and J. I. DeGross (eds.), Washington, DC, December, pp. 77-90.

Bruce, V., Green, P. R., and Georgeson, M. A. 2003. Visual Perception: Physiology, Psychology and Ecology ( $4^{th}$ ed.), Hove, UK: Psychology Press.

Bunge, M. 1977. Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World, Boston: Reidel.

Burton-Jones, A., and Meso, P. 2006. "Conceptualizing Systems for Understanding: An Empirical Test of Decomposition Principles in Object-Oriented Analysis," Information Systems Research (17:1), pp. 38-60.

Burton-Jones, A., Wand, Y., and Weber, R. 2007. “Information Equivalence, Computational Equivalence, and the Evaluation of Conceptual Modeling,” in Proceedings of the Sixth AIS SIGSAND Symposium on Research in Systems Analysis and Design, Dinesh Batra (ed.), Tulsa, OK, May, pp. 35-42.

Chen, P. P. S. 1976. “The Entity-Relationship Model: Toward a Unified View of Data,” ACM Transactions on Database Systems (1:1), pp. 9-36.

Cohen, J. 1960. “A Coefficient for Agreement of Nominal Scales,” Educational and Psychological Measurement (20), pp. 37-46.

Davis, F. D. 1989. “Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology,” MIS Quarterly (13:3), pp. 319-340.

Dretske, F. 1995. Naturalizing the Mind, Cambridge, MA: MIT Press.

Edelman, S. 1999. Representation and Recognition in Vision, Cambridge, MA: MIT Press.

Elmasri, R., and Navathe, S. B. 2004. Fundamentals of Database Systems ( $4^{th}$ ed.), Boston: Pearson/Addison-Wesley.

Ericsson, K. A., and Simon, H. A. 1993. Protocol Analysis: Verbal Reports as Data (rev. ed.), Cambridge, MA: MIT Press.

Eriksson, H-E., and Penker, M. 1998. UML Toolkit, New York: John Wiley & Sons.

Floyd, C. A. 1986. “Comparative Evaluation of System Development Methods,” in Information System Design Methodologies: Improving the Practice, T. W. Olle, H. G. Sol, and A. A. Verrijn-Stuart (eds.), Amsterdam: North-Holland, pp 19-54.

Frankel, D. S., and Parodi, J. (eds.). 2004. The MDA Journal: Straight from the Masters, Tampa, FL: Megan-Kiffer Press.

Gemino, A., and Wand, Y. 2005. “Complexity and Clarity in Conceptual Modeling: Comparison of Mandatory and Optional Properties,” Data & Knowledge Engineering (55:3), pp. 301-326.

Gerstl, P., and Pribbenow, S. 1996. “A Conceptual Theory of Part-Whole Relations and Its Applications,” Data & Knowledge Engineering (20:3), pp. 305-322.

Green, P., and Rosemann, M. 2000. “Integrated Process Modeling: An Ontological Evaluation,” Information Systems (25:2), pp. 73-87.

Gregor, S. 2006. "The Nature of Theory in Information Systems," MIS Quarterly (30:3), pp. 611-642.

Hirschheim, R., Klein, H., and Lyytinen, K. 1995. Information Systems Development and Data Modeling: Conceptual Foundations and Philosophical Foundations, Cambridge, UK: Cambridge University Press.

Marr, D. 1982. Vision: A Computational Investigation into the Human Representation and Processing of Visual Information, San Francisco: W. H. Freeman.

Mayer, R. E. 1989. “Models for Understanding,” Review of Educational Research (59:1), pp. 43-64.

Moore, G. C., and Benbasat, I. 1991. “Development of an Instrument to Measure the Perceptions of Adopting an Information Technology Innovation,” Information Systems Research (2:3), pp. 192-222.

Olle T. W, Sol, H.G., and Tully, C. J. (eds.). 1983. Information System Design Methodologies: A Feature Analysis, Amsterdam: North-Holland.

Opdahl, A. L., and Henderson-Sellers, B. 2001. “Grounding the OML Metamodel in Ontology,” Journal of Systems and Software (57:2), pp. 119-143.

Opdahl, A. L., Henderson-Sellers, B., and Barbier, F. 2001. "Ontological Analysis of Whole-Part Relationships in OO Models," Information and Software Technology (43:6), pp. 387-399.

Palmer, S. E. 1978 “Fundamental Aspects of Cognitive Representation,” in Cognition and Categorization, E. Rosch and B. B. Lloyd (eds.), Hillsdale, NJ: Lawrence Erlbaum, pp. 259-303.

Parsons, J. 1996. “An Information Model Based On Classification Theory,” Management Science (42:10), pp. 1437-1453.

Parsons, J., and Cole, L. 2005. “What Do the Pictures Mean? Guidelines for Experimental Evaluation of Representation Fidelity in Diagrammatical Conceptual Modeling Techniques,” Data & Knowledge Engineering (55:3), pp. 301-326.

Parsons, J., and Wand. Y. 2000. “Emancipating Instances from the Tyranny of Classes in Information Modeling,” ACM Transactions on Database Systems (25:2), pp. 228-268.

Prietula, M. J., and March, S. T. 1991. “Form and Substance in Physical Database Design: An Empirical Study,” Information Systems Research (2:3), pp. 287-314.

Rumbaugh, J., Jacobson, I., and Booch. G. 2005. The Unified Modeling Language Reference Manual ( $2^{nd}$ ed.), Boston: Addison-Wesley.

Shanks, G., Tansley, E., and Weber, R. 2003. “Using Ontology to Validate Conceptual Models,” Communications of the ACM (46:10), pp. 85-89.

Shoval, P., and Frumerman, F. 1994. “OO and EER Conceptual Schemas: A Comparison of User Comprehension,” Journal of Database Management (5:4), pp. 28-38.

Shoval, P., and Shiran, S. 1997. “Entity-Relationship and Object-Oriented Modeling: An Experimental Comparison of Design Quality,” Data & Knowledge Engineering (21:3), pp. 297-315.

Siau, K., Wand, Y., and Benbasat, I. 1997. “The Relative Importance of Structural Constraints and Surface Semantics in Information Modeling,” Information Systems (22:2-3), pp. 155-170.

Simons, P. M. 1987. Parts: A Study in Ontology, Oxford, UK: Clarendon Press.

Simons, P. M., and Dement, C. W. 1996. “Aspects of the Mereology of Artifacts,” in Formal Ontology, R. Poli and P. M. Simons (eds.), Dordrecht, The Netherlands: Kluwer Academic Publishers, pp. 255-276.

Smith, B. 1996. “Mereotopology: A Theory of Parts and Boundaries,” Data & Knowledge Engineering (20:3), pp. 287-303.

Smith, J. M., and Smith, D. C. P. 1997. “Database Abstractions: Aggregation,” Communications of the ACM (20:6), pp. 405-413.

Storey, V. 1991. “Meronymic Relationships,” Journal of Database Administration (2:3), pp. 22-35.

Tabachnick, B. G., and Fidell, L. S. 1996. Using Multivariate Statistics ( $3^{rd}$ ed.), New York: HarperCollins.

Teorey, T., Lightstone, S., and Nadeau, T. 2006. Database Modeling and Design: Logical Design ( $4^{th}$ ed.), San Francisco: Morgan KaufmannPublishers.

Teorey, T. J., Yang, D., and Fry, J. P. 1986. “A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model,” ACM Computing Surveys (18:2), pp. 197-222.

Varzi, A. C. 1996. “Parts, Wholes, and Part–Whole Relations: The Prospects of Mereotopology,” Data & Knowledge Engineering (20:3), pp. 259-286.

Voss, J. F., and Post, T. A. 1988. “On the Solving of Ill-Structured Problems” in The Nature of Expertise, M. H. Chi, R. Glaser, and M. J. Farr (eds.), Hillsdale, NJ: Lawrence Erlbaum Associates, pp. 261-285.

Wand, Y., and Weber, R. 1993. “On the Ontological Expressiveness of Information Systems Analysis and Design Grammars,” Journal of Information Systems (3:4), pp. 217-237.

Wand, Y., and Weber, R. 2002. “Information Systems and Conceptual Modeling: A Research Agenda,” Information Systems Research (13:4), pp. 363-376.

Wand, Y., Storey, V., and Weber, R. 1999. “An Ontological Analysis of the Relationship Construct in Conceptual Modeling,” ACM Transactions on Database Systems (24:4), pp. 494-528.

Weber, R. 1996. “Are Attributes Entities? A Study of Database Designers’ Memory Structures,” Information Systems Research (7:2), pp. 137-162.

Winston, M. E., Chaffin, R., and Herrman, D. 1987. “A Taxonomy of Part-whole Relations,” Cognitive Science (11:4), pp.417-444.

## About the Authors

Graeme Shanks is Professor of Information Systems at the University of Melbourne. He received his Ph.D. in Information Systems from Monash University. Prior to becoming an academic, Graeme worked for a number of years as programmer, programmer-analyst, and project leader in several large organizations. His research interests focus on conceptual modeling, data quality, decision support systems, identity management and the implementation and impact of enterprise and interorganizational systems. Graeme has published in journals including Journal of Information Technology, Journal of Strategic Information Systems, Information Systems Journal, Information Systems, Information and Management, Behaviour and Information Technology, Communications of the AIS, Communications of the ACM, Requirements Engineering, and Australian Journal of Information Systems. He is a member of the editorial boards of six journals and was recently a member of the Australian Research Council College of Experts.

Elizabeth Tansley is a senior lecturer in the School of Computing Sciences at Central Queensland University. Elizabeth lectures principally in database theory and management systems and is particularly interested in the journey faced by students learning the skills of data modeling and database design. Elizabeth was awarded her Ph.D. in 2004 in the area of data modeling from the same institution.

Jasmina Nuredini has acted as a consultant to a number of private, government, and educational institutions over eight years, with a specialization in data and process modeling. She comes from a financial and data modeling background with solid experience in data management, process modeling, and enterprise (corporate) data modeling and is currently working at Simsion Associates, Australia. Jasmina has also held research positions at Deakin University, the University of Melbourne, and Monash University. Through her academic and professional experience she has developed a keen interest in exploring new ideas and relating them to industry practices, particularly in data and process modeling. Her research results have been published at several Australian and international conferences.

Daniel Tobin is the Market Research Manager at the University of Melbourne. He has worked for large organizations, focusing on customer satisfaction, market segmentation, and strategic direction. Daniel has an interest in the relationships between business products/processes and customer needs.

Ron Weber is Dean, Faculty of Information Technology, Monash University. He graduated with a first-class honours degree and University Medal in accounting from the University of Queensland and an MBA and Ph.D. in management information systems from the University of Minnesota. His research interests lie in the areas of the ontological foundations of information systems, management of the information systems function, and computer control and audit. He is a past president of the Association for Information Systems and a past Editor-in-Chief of the MIS Quarterly.

## Appendix A

## Problem-Solving Questions

For each of the following questions, participants were asked to choose from the following three responses: possible; not possible; not sure. They were then asked to briefly explain their answer.

1. Project X is made up of ten phases. Does the model allow more than one team leader to work on some of the phases?

2. A team leader has resigned. Does the model allow the team to continue to work on the project without him?

3. A client has requested that a project will start in five months time. A department wants to create a team with a leader now, and give the leader the next five months to select appropriate team members as she pleases. Is this possible?

4. Project Z has overlapping phases, which occur simultaneously. Is it possible for a single team member to work on two concurrent phases?

5. Project Y consists of two phases. Phase 1 has been completed without consumables. Phase 2 now requires the purchase of consumables such as floppy disks, zip drives, and architects' pencils. Does the model allow the team to purchase these necessary consumables?

6. The client of project D decides on a weekly basis what work will be required for the project. The project has no key deliverables but will require consumables. Can the project keep track of the consumables it purchases?

7. The client for project X wishes to make purchase requisitions for its next three phases, as there are rumors that the consumables they require will be experiencing a shortage. The supplier has not yet been decided. Does the model allow the purchase requisitions to be made?

8. An employee wishes to check their skill appropriateness for an upcoming project by checking the key deliverables and scope of the project. At this point, the project has been divided up into phases, but contains no project plan. Using the diagram, can the employee check their suitability?

9. Client Z has used the same supplier for the past 5 years. The supplier charges at a discount rate and bills at the end of each phase. Does the model allow the purchase of consumables if there are no key deliverables?

10. An employee becomes a member on a project that has been running for 3 years. He has been given a project plan, but its budget and scope do not seem to match the size and completeness of the project. Can he check that he has the current plan?

11. A client has had to significantly reduce the budget of a project with five phases remaining. The reduced budget is not enough to cover all these phases. Can the team leader prioritize the remaining phases?
