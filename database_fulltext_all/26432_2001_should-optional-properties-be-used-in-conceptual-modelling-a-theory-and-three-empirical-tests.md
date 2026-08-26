---
otero_id: 26432
otero_key: "4MM5YAAC"
title: "Should Optional Properties Be Used in Conceptual Modelling? A Theory and Three Empirical Tests"
authors: "François Bodart; Arvind Patel; Marc Sim; Ron Weber"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.4.384.9702"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/4MM5YAAC/fulltext/images/7c57f6371e9a0cfafb27dc45daf0c189bfacfcd38ebbfbd23e3f9b879261b516.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Should Optional Properties Be Used in Conceptual Modelling? A Theory and Three Empirical Tests

François Bodart, Arvind Patel, Marc Sim, Ron Weber,

To cite this article:

François Bodart, Arvind Patel, Marc Sim, Ron Weber, (2001) Should Optional Properties Be Used in Conceptual Modelling? A Theory and Three Empirical Tests. Information Systems Research 12(4):384-405. http://dx.doi.org/10.1287/ isre.12.4.384.9702

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/4MM5YAAC/fulltext/images/961cfdba8edea99479bcfe539897f5285d7db7594cc8d9389aa7866a8ab97173.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Should Optional Properties Be Used in Conceptual Modelling? A Theory and Three Empirical Tests

Franc¸ois Bodart • Arvind Patel • Marc Sim • Ron Weber

Institut d’Informatique, Faculte´s Universitaires Notre-Dame de la Paix, rue Grandgagnage, 21, B-5000 Namur, Belgium

Department of Accounting and Financial Management, The University of the South Pacific, Suva, Fiji

Department of Commerce, The University of Queensland, Australia 4072

Department of Commerce, The University of Queensland, Australia 4072

fbodart@info.fundp.ac.be • patel\_a@usp.ac.fj • sim@commerce.uq.edu.au • weber@commerce.uq.edu.au

n important feature of some conceptual modelling grammars is the features they provide to allow database designers to show real-world things may or may not possess a particular attribute or relationship. In the entity-relationship model, for example, the fact that a thing may not possess an attribute can be represented by using a special symbol to indicate that the attribute is optional. Similarly, the fact that a thing may or may not be involved in a relationship can be represented by showing the minimum cardinality of the relationship as zero. Whether these practices should be followed, however, is a contentious issue. An alternative approach is to eliminate optional attributes and relationships from conceptual schema diagrams by using subtypes that have only mandatory attributes and relationships.

In this paper, we first present a theory that led us to predict that optional attributes and relationships should be used in conceptual schema diagrams only when users of the diagrams require a surface-level understanding of the domain being represented by the diagrams. When users require a deep-level understanding, however, optional attributes and relationships should not be used because they undermine users’ abilities to grasp important domain semantics. We describe three experiments which we then undertook to test our predictions. The results of the experiments support our predictions.

(Database Design; Data Models; Entity-Relationship Model; Semantic Data Models; Systems Theory; Ontology; Optional Attributes; Optional Relationships; Subtyping)

## 1. Introduction

During the design of an information system, the task of conceptual modelling involves designers working with users to tease out and to build a representation of an application domain. This representation should capture the important features of the domain to be incorporated into the information system (Batini et al. 1992). The goal is to provide a vehicle for improved communication, discourse, and discernment among stakeholders in the system development process (Hirschheim et al. 1995). A conceptual model then forms the basis for designing different types of implementation models (e.g., data models) that take into account various aspects of the information technology platform to be used to operate the information system (e.g., the database management system). Conceptual models should not be compromised, however, by these implementation considerations (Mylopoulous 1998).

While conceptual modelling often is only a small component of the overall system development process,

Moody (1998) argues that it is critical. He points to well-known findings from the software engineering literature (e.g., Boehm 1981) and quality-assurance literature (e.g., Walrad and Moss 1993) that highlight the substantial cost savings that accrue from resolving errors earlier rather than later in the system development process. Because conceptual modelling is performed early in the system development process, high payoffs should arise if it is done well, especially given its central goal of improving communication among stakeholders. Empirical evidence supports this view (e.g., Moody and Shanks 1998).

Despite this apparent importance of conceptual modelling, research has shown that often it is not done well. For example, experimental work by Batra et al. (1990), Goldstein and Storey (1990), and Prietula and March (1991) indicates that designers encounter substantial problems when they perform conceptual modelling. Similarly, survey work by Hitchman (1995), Maier (1996), and Batra and Marakas (1995) shows that (a) conceptual modelling is not a persistent practice in many organizations even though it is deemed important, (b) often the quality of conceptual models prepared by novice and experienced designers alike is poor, and (c) users have difficulty understanding conceptual models.

The overall goal of the research described in this paper is to contribute to better conceptual modelling practice and thus, we hope, to significant cost savings ultimately in the development of information systems. We focus specifically on just one aspect of conceptual modelling practice—namely, the question of whether designers should use optional properties (manifested in the use of optional attributes and relationships) to model a domain. Optional properties permit designers to show that things may or may not possess an attribute or relationship (e.g., a person may or may not have a spouse). Their use is widely advocated (e.g., Batini et al. 1992). Moreover, we have found they are employed extensively in practice.

Our claim is that optional properties should not be used during conceptual modelling whenever they stand for real properties (as opposed to alternative ways of labelling real properties). Instead, optional properties should be replaced by subtypes that have only mandatory properties (e.g., persons are partitioned into the subtypes “married persons” and “single persons” where only married persons have the property of having a spouse). We argue that subtypes with mandatory properties more clearly convey the semantics associated with an application domain. They make explicit the subclasses associated with a class of entities and the constraints that are specific to each subclass. Given the current widespread acceptance and use of optional properties, our claim that they should be proscribed from conceptual modelling practice is therefore controversial and, we believe, important. Its acceptance would involve subtle and fundamental changes in the ways conceptual modelling is currently taught and practised.

We temper our claim by recognizing that conceptual models need to be adapted for different purposes. For example, designers might wish to provide senior management with an overview of an application domain. In this light they might need to strip detail from a conceptual model so management can gain a quick understanding of the domain. Optional properties may be a useful vehicle for reducing the complexity of a model when only a surface-level understanding of a domain is required. Indeed, our research provides us with some insights on this matter. We should not confuse presentation models with conceptual models, however. The former are motivated by a wide range of communication goals that designers might have. The latter are motivated by a single goal—namely, to provide an accurate, complete representation of someone’s or some group’s understanding of a domain.

In the sections below, we first provide some brief background to the notions of optional properties, subtypes, and mandatory properties, and their importance to conceptual modelling. We then provide theoretical justification to support our argument that optional properties should not be used in conceptual modelling when our goal is to enable deep understanding as opposed to surface understanding of a domain. Next we provide an overview and then a detailed description of three experiments we undertook to test our proposition. Finally, we discuss the implications of our work for research and practice.

## 2. Background

Optionality is an important feature of many conceptual modelling grammars. In the grammar used to generate entity-relationship (ER) diagrams, for example, optionality can be represented in two ways (Batini et al. 1992). First, a relationship can be designated as optional by showing, for example, that the minimum cardinality of the relationship is zero (Figure 1a). Second, elementary attributes can be designated as optional by showing, for example, a white circle as opposed to a black circle when they are mandatory (Figure 1b). This notion applies irrespective of whether the elementary attribute is single valued (e.g., a person’s age) or multivalued (e.g., a person’s skills).

In some object-modelling grammars, optionality also has a place. For example, as with the entityrelationship modelling grammar, a zero cardinality can be used to show that an object may or may not participate in an association with another object (Kilov and Ross 1994). Not all object-modelling grammars permit optionality, however (Cattell 1994). Some require that all attributes and relationships are mandatory.

In an analysis of the ontological foundations of constraints in NIAM that indicate entities may or may not possess certain “roles,” Weber and Zhang (1996) argue that they all manifest a single ontological construct— namely, the existence of a subclass of a class of things. If, for instance, a conceptual schema diagram indicates a warehouse may have no insurance (the role is optional), two subclasses of the class “warehouse” exist— namely, those having insurance (say, an owned domestic warehouse), and those not having insurance (say, a rented foreign warehouse). Thus, optional roles can always be transformed into mandatory roles by using subclasses (Figure 2). From a conceptual modelling perspective, therefore, it might be argued that constraints that represent optional roles and constraints that represent subclasses manifest the same real-world semantics (see, e.g., Kilov and Ross 1994). Indeed, database implementation considerations aside, it might be argued that it is a tossup as to which form of representation to use.

The second type of model is a conceptual model. These are intended to provide an accurate, complete representation of someone’s or some group’s perceptions of the semantics underlying a domain or some part of a domain. Here we argue that optional properties should be proscribed because they have a particular ontological interpretation that is nonsensical. Specifically, we see optional properties allowing for the

In this paper, we take an alternative view. Specifically, we argue that optional properties must be used selectively. We distinguish between three types of model that information systems professionals might use to represent a domain. The first is a presentation model. These are intended to provide a high-level overview of a domain or some part of the domain. For example, they might be presented to senior managers who need to gain a quick grasp of the domain. We argue that optional properties have a place in presentation models because they facilitate surface-level cognition, which ultimately is the primary purpose of these models.

Figure 2 Representing the Same Domain with Optional Properties Versus Subtyping  
![](/api/attachments/4MM5YAAC/fulltext/images/f701e434d8c49b461ed977d5d41d1ad8d5000540a4b719dc927fd77d2819997e.jpg)  
Information Systems Research Vol. 12, No. 4, December 2001

existence of an ontological construct called a negated property—a property a thing does not possess. Like Bunge (1977), we argue that negated properties have no ontic correlate because humans do not conceive of the world in terms of things and properties that the things do not possess. For example, humans do not conceive of a person in terms of all the properties they do not have—as someone who is not hearing impaired, or not having a PhD, or not having programming skills. In this light we support Bunge’s (1977, p. 60) contention that “external reality wears only positive traits.” Otherwise, the demands placed on human memory are unmanageable. If humans were to conceive things in terms of the properties they do not possess, potentially all properties in the world have to be considered to determine whether they do or do not belong to a thing—an impossible cognitive task.

Admittedly, when humans reason about things, we sometimes address the truth or falsity of a proposition about them expressed in terms of negated properties. For example, the proposition that “James has no children” may be true or false, but this does not mean James has the property of having no children. Rather, it is an outcome of a logical test undertaken to determine whether James has the property of having children. Moreover, we argue below that humans have good reasons to conceive of things in terms of properties they possess rather than properties they do not possess. As a result, we contend that conceptual models that include optional properties will convey less real-world meaning to users than conceptual models that proscribe optional properties and use subtyping and mandatory properties instead.

The third type of model is an implementation model. These are prepared to facilitate the mapping between conceptual models and the way data ultimately are laid out on storage media. They reflect many types of design decisions that must be made—for example, what data model will be used, whether null values will be permitted, and how much fragmentation of data should be allowed to occur because of normalization.

With implementation models, Wand et al. (1999) argue that optionality might be permitted. They make a critical distinction between optional attributes and relationships that stand for real properties and optional attributes and relationships that stand for alternative ways of labelling real properties. For example, a conceptual schema diagram might show that a person entity has two optional attributes: one for apartment address, and the other for house address. Optionality indicates that a person lives in either an apartment or a house. In some cases, whether a person lives in an apartment or a house proxies for different real properties of the person. For instance, people living in apartments may have different sorts of insurance needs from people living in houses. In these situations, Wand et al. (1999) argue that optional attributes and relationships should be proscribed and subtypes with mandatory attributes and relationships should be used instead. In other cases, the real property of interest may simply be that a person has a place of residence. Whether a person lives in an apartment or a house merely represents alternative ways of labelling or proxying for the same underlying real property. In these situations, Wand et al. (1999) argue that conceptual models ought to show only attributes and relationships that stand for real properties. Designers might choose to articulate implementation models, however, that show alternative attributes and relationships that proxy for the same underlying real property.

With implementation models, therefore, a case might be made for retaining the optionality construct. Our own view, however, is that optionality also should be proscribed in implementation models. The stakeholders who work with implementation models (e.g., programmers) use them to undertake deep cognition. Nonetheless, implementation modelling involves complex trade-offs between human-oriented concerns and machine-oriented concerns. For this reason, our focus in this paper is on the use of optionality in conceptual modelling and, to a lesser extent, presentation modelling.

Note, finally, that in a formal information-theoretic sense, conceptual models with subtypes and mandatory properties only contain more information than conceptual models with optional properties. For example, Figure 2b makes clear that AgentAddress is a property of foreign warehouses only. This information cannot be deduced from Figure 2a. Conceptual models with subtypes and mandatory properties only contain more diagrammatic construct instances, however (more entity symbols). Thus, users may perceive them to be more complex. As a result, they may communicate less semantics to users in spite of their higher information content. In this research, we focus on how well users glean domain semantics from conceptual models and not formal measures of their information content.

## 3. Theory and Propositions

While Weber and Zhang (1996) and Wand et al. (1999) argue that optionality should be proscribed in conceptual models on the basis of ontological theory, in this paper we argue it should be proscribed for complementary but different reasons. Specifically, we contend that optionality undermines users’ ability to reason about and solve problems based on the semantics of a domain. On the other hand, optionality may have a place in presentation models where users are simply seeking to gain an overview of a domain.

While a number of theories of memory might be used to support our arguments, because of its widespread acceptance within psychology, the one we choose is Collins and Quillian’s (1969) theory of semantic networks. In this theory, human semantic memory is structured as a network of nodes linked via directed pathways. The nodes may be entities, attributes of entities, classes, or attributes of classes. Paths stand for some type of relationship between the things represented by the nodes (e.g., membership of a specific entity in a class, or possession of a property by an entity). Nodes and pathways may be in working memory because an individual has just encoded them (e.g., read them off a conceptual schema diagram). Alternatively, they may be in long-term memory because individuals have learned them already.

Recall of information (semantics) from the network is hypothesized to occur via the process of spreading activation (Anderson and Pirolli 1984). When individuals attend to some phenomena, they “prime” those nodes in the semantic network that represent these phenomena. This priming then spreads almost instantaneously throughout the network via the paths among nodes. The strength of priming decays exponentially, however, as a function of the distance it spreads. When the priming reaches other nodes, an individual’s ability to recall the information represented by the nodes depends on two factors: first, the strength of the priming that reaches each node; and second, the residual strength of each node, which is a function of prior primings of the node. Higher priming and higher residual strength facilitate recall of the node.

In the context of this theory, three factors seem relevant to determining whether an optional property representation or a subtyping representation is better able to convey real-world meaning to the users of conceptual schema diagrams. The first is the number of construct instances in the diagram that has to be studied. As this number increases, for a given amount of learning time the likelihood of remembering the construct instance decreases because individuals have to give each less attention. Thus, each receives less priming. Accordingly, diagrams that use subtyping should be more difficult to memorize than diagrams that use optional properties because use of subtyping leads to conceptual schema diagrams having more construct instances (Figure 2). Both the entire diagram and individual construct instances in the diagram should be more difficult to remember (Shenk 1997).

The second factor is the extent to which stimuli, such as conceptual schema diagrams, facilitate elaboration in individuals. Elaboration is the cognitive process whereby individuals consciously or subconsciously establish paths between nodes in a semantic network representing newly learned material and nodes representing already known material. Elaboration facilitates recall by providing alternative retrieval paths through semantic networks. Thus, if one path fails, another may succeed. Elaborations are more successful, however, when they “constrain” the to-be-remembered material. Indeed, imprecise elaborations can inhibit memory recall because they simply increase the amount to be remembered (Bradshaw and Anderson 1982).

We propose that optional properties lead to less precise elaborations whereas mandatory properties lead to more precise elaborations. The reason is that nodes representing optional properties must have two possible states to represent the fact that an entity to which they are connected may or may not possess the property. Mandatory properties, on the other hand, have only one state to represent the fact that an entity to which they are connected will always possess them. Thus, mandatory properties should enable individuals to undertake more constrained elaborations and therefore to better understand, memorize, and recall material.

The third factor is the extent to which stimuli facilitate inferential reconstruction in individuals when they undertake recall. Inferential reconstruction is the process by which individuals infer what is plausible in light of facts they can remember. It causes them to recall what they did not study initially, but it also helps them to better recall what they did study. Individuals undertake better inferential reconstruction when they undertake better elaboration (Owens et al. 1979). Thus, we argue that mandatory properties allow individuals to undertake better inferential reconstruction than optional properties because they allow more precise, and therefore better, elaborations.

In summary, we hypothesize that one feature of conceptual schema diagrams that use mandatory rather than optional properties inhibits users’ understanding of the domains they represent. Specifically, they have a larger number of construct instances to be remembered, which undermines a user’s ability to recall the semantics of a domain. However, we hypothesize that another feature of conceptual schema diagrams that use mandatory rather than optional properties facilitates users’ understanding of the domains they represent. Specifically, they represent the properties of entities in the domain more precisely, which in turn enables users to undertake better elaboration and inferential reconstruction.

We predict, therefore, that optional properties may have differential effects on a user’s ability to understand a domain, depending on the type of understanding that is required of the user. If users require only a surface-level understanding of the domain, we predict that an optional-property representation will outperform a mandatory-property representation. Tasks that require users to have only a surface-level understanding of a domain do not forcefully engage elaborative and inferential reconstruction cognitive processes. Thus, the number-of-constructs effect will outweigh elaborative and inferential reconstruction effects. On the other hand, if users require a deep-level understanding of a domain, we predict that a mandatory-property representation will outperform an optional-property representation. Tasks that require users to have a deeplevel understanding of a domain mean they must forcefully engage elaborative and inferential reconstruction cognitive processes. The effects of these processes, therefore, will outweigh the number-of-constructs effect (see also Bradshaw and Anderson 1982). In this light, we make the following propositions:

Proposition 1. Conceptual schema diagrams that use optional properties to represent a real-world domain will assist users to undertake tasks that require a surface-level understanding of a domain better than conceptual schema diagrams that use only mandatory properties.

Proposition 2. Conceptual schema diagrams that use only mandatory properties to represent a real-world domain will assist users to undertake tasks that require a deep-level understanding of a domain better than conceptual schema diagrams that use optional properties.

## 4. Overview of the Experiments

To test the propositions, we undertook three experiments. Their designs were motivated in part by research undertaken by Mayer and his colleagues (e.g., Mayer 1989, Mayer and Gallini 1990).<sup>1</sup> They had performed a series of experiments in which they had examined the impact of text versus diagrams on their participants’ ability to learn a domain. Mayer and his colleagues made three predictions. First, they hypothesized that participants who received diagrams would perform better on problem-solving tasks than those who received text. They argued that diagrams allowed participants to develop more sophisticated cognitive models of the domain to be learned. Participants would develop a deep understanding of the domain rather than a surface understanding. Second, they hypothesized that participants who received diagrams would perform worse on verbatim-recall tasks than those who received text. They argued that the deeper conceptual processing undertaken by participants who received the diagrams would undermine their ability to retain the information they needed for verbatim recall. Third, they hypothesized that participants who received diagrams would perform about the same on comprehension tests as those who received text. To the extent that comprehension tests required more conceptual understanding of the domain, participants who received diagrams would do better. Note that Mayer and his colleagues’ work is somewhat atheoretical, because they did not base their predictions on a model of memory or cognition.

Table 1 provides an overview of the three experiments we undertook to test our two propositions, and the results we obtained. The first involved recall of conceptual schema diagrams. Consistent with Mayer and his colleagues’ arguments, we hypothesized that the task required only surface-level understanding of the domain. Thus, we predicted that the number-ofconstructs effect would dominate elaborative and inferential reconstruction effects. Participants who used conceptual schema diagrams with optional properties would therefore outperform participants who used conceptual schema diagrams with mandatory properties only. Our results supported this prediction.

The second experiment involved a comprehension task. The comprehension questions we asked of participants in the experiment were straightforward and often relied on recall of features of the conceptual schema diagram. Thus, our expectation was that participants who received the optional-properties treatment would still outperform those who received the mandatory-properties treatment. Nonetheless, because comprehension invokes deeper-level cognitive processes than does recall, we hypothesized that performance differences between the two treatments would be less clear-cut than in the first experiment. Moreover, we hypothesized that performance differences would dissipate more quickly across trials as elaboration and inferential reconstruction processes took effect. Our results provided mixed support for these predictions.

The third experiment involved a problem-solving task. Consistent with Mayer and his colleagues’ arguments, we hypothesized that this task requires a deeplevel understanding of a domain if it is to be performed effectively. Thus, we predicted that the elaborative and inferential reconstruction effects would dominate the number-of-constructs effect. Participants who used conceptual schema diagrams with mandatory properties only would therefore outperform participants who used conceptual schema diagrams with optional properties. Our results supported this prediction.

## 5. Experiment 1

To test the first proposition, we used a multitrial freerecall experiment. In this type of experiment, participants are given multiple presentations of a stimulus and asked to recall the stimulus after each presentation (e.g., Ernest 1991). Participants in the first experiment received multiple presentations of a conceptual schema diagram. After each presentation, they were asked to recall the diagram as accurately as they could.

Table 1 Overview of the Three Experiments

<table><tr><td></td><td>Experiment 1</td><td>Experiment 2</td><td>Experiment 3</td></tr><tr><td>Nature of Experiment</td><td>Free recall test</td><td>Comprehension test</td><td>Problem-solving test</td></tr><tr><td>Type of “Meaning” Transfer Evaluated</td><td>Surface-level</td><td>Mostly surface-level</td><td>Deep-level</td></tr><tr><td rowspan="3">Independent Variables</td><td>Type of representation</td><td>Type of representation</td><td rowspan="3">Type of representation</td></tr><tr><td>Domain complexity</td><td rowspan="2">Trial</td></tr><tr><td>Trial</td></tr><tr><td rowspan="3">Dependent Variables</td><td rowspan="3">Seven measures of recall accuracy</td><td>Response accuracy</td><td rowspan="3">Three measures of problem-solving performance</td></tr><tr><td>Response time</td></tr><tr><td>Normalized accuracy</td></tr><tr><td>Total Number of Participants</td><td>52</td><td>52</td><td>96</td></tr><tr><td>Primary Result</td><td>Optional properties outperform mandatory properties</td><td>Optional properties marginally outperform mandatory properties</td><td>Mandatory properties outperform optional properties</td></tr></table>

At first glance, the usefulness of a multitrial freerecall procedure as a means of testing how well different conceptual schema diagrams communicate semantics may not be apparent. In practice, users are unlikely to engage in multitrial free-recall procedures. Moreover, it might be argued that users can always refer to a conceptual schema diagram to respond to questions about the semantics of the domain it represents.

For two reasons, however, we argue that our design is an appropriate test of our theory. First, multitrial free-recall procedures have been used extensively in psychological research as a means of teasing out differences in understanding in the constrained artificial environment of experiments where treatment effects are often weak (Ashcraft 1989). Second, users often cannot refer to conceptual schema diagrams to respond to queries about a domain because they have been lost or not kept up to date. Thus, they may be forced to engage in recollection of conceptual schema diagrams and domain semantics.

## 5.1. Design and Measures

A (2 - 2) - 4 mixed design with two between-subjects factors and one within-subjects factor was used. The first between-subjects factor, “type of representation,” had two levels: Either optional properties or subtyping was used in a conceptual schema diagram.

The second between-subjects factor, “representational complexity,” had two levels: low and high. Representational complexity was evaluated by counting the number of instances of representational constructs used in a diagram. Given a particular type of representation (e.g., use of diagrams that employ optional properties), the higher representational complexity diagram had more construct instances. The purpose of having two levels of representational complexity was to determine whether the number-of-constructs effect was present even at relatively low levels of complexity. In addition, by choosing different application domains as the basis for the two levels of complexity, the external validity of the experiment was increased.

The within-subjects factor, “trial,” had four levels. The purpose of having multiple trials is to motivate participants to use at least some level of semantics as the basis for their recall rather than syntactics. It has been found, for example, that some participants initially may use the topological characteristics of a diagram to try to recall it. As they seek to improve their recall, however, inevitably they begin to use the semantics underlying the diagram to facilitate their recall (Weber 1996). In the context of semantic-network theory, elaboration and inference begin to take effect as trials progress. During pilot testing of our experiment, we found that four trials were sufficient for the task’s semantic structure, rather than its syntactic structure, to take effect.

The dependent measure was recall accuracy. Accuracy was measured via the proportion of the total number of different construct instances in the diagram (e.g., entities, attributes) that participants recalled correctly. Proportions were used rather than absolute numbers because the number of construct instances in the optional-properties diagram differed from the number in the mandatory-properties diagram for some dependent measures. Moreover, as indicated above, the number of construct instances in the easy diagram differed from the number in the hard diagram.

Specifically, recall performance was assessed using seven measures:

(1) Proportion of entities recalled correctly: Calculated by counting the number of entities that participants recalled correctly and dividing it by the number of entities on the diagram that they had to recall. Entity symbols drawn by participants without labels were not counted. Participants did not have to give the exact label shown on the diagram, but they had to give a label that was deemed equivalent.

(2) Proportion of relationships recalled correctly: Calculated by counting the number of relationships that participants recalled correctly and dividing it by the number of relationships on the diagram that they had to recall. As with entities, participants had to give relationships the correct or an equivalent label.

(3) Proportion of attributes recalled and named correctly: Calculated by counting the number of attributes that participants recalled correctly and dividing it by the number of attributes on the diagram they had to recall. Again, participants had to give attributes the correct or an equivalent label.

(4) Proportion of attributes recalled and typed correctly:

Calculated by counting the number of attributes that participants recalled correctly and correctly typed and dividing it by the number of attributes on the diagram that they had to recall. Note that all attributes on the subtyping diagram are mandatory, whereas both optional and mandatory attributes appear on the two optional-properties diagrams.

(5) Proportion of relationships recalled correctly with correct cardinalities: Calculated by counting the number of relationships that participants recalled correctly and assigned the correct cardinality, and dividing it by the number of relationships on the diagram that they had to recall. Note that two pairs of cardinalities attach to each relationship. If participants got one pair correct, they were given a half point. If they got both pairs correct, they were given one point.

(6) Proportion of correctly recalled attributes correctly typed: Calculated by counting the number of attributes that participants recalled correctly and correctly typed, and dividing it by the number of attributes that they recalled correctly.

(7) Proportion of correctly recalled relationships assigned correct cardinalities: Calculated by counting the number of relationships that participants recalled correctly and assigned the correct cardinality, and dividing it by the number of relationships that they recalled correctly.

## 5.2. Materials

Materials were based upon two application domains. One pertained to the conduct of projects within a university-research organization. The other pertained to sales, supplies, and inventory within a distribution company. For each domain, two conceptual schema diagrams were created. The first was an entityrelationship diagram where optional properties were used. No subtypes appeared on the diagram. The second was an entity-relationship diagram where subtypes were used. No optional properties appeared on the diagram. Figures 3–4 show the two diagrams for the university-research organization. In the interest of brevity, the diagrams for the distribution organization are not shown.<sup>2</sup> Table 2 shows counts of the construct instances in each diagram. The diagram for the research organization was intended to be the instantiation of the low representational complexity (easy) task because it had fewer entities, relationships, and attributes.

Table 2 Count of Construct Instances in Conceptual Schema Diagrams

<table><tr><td></td><td>Research Domain: Optional</td><td>Research Domain: Mandatory</td><td>Distribution Domain: Optional</td><td>Distribution Domain: Mandatory</td></tr><tr><td>Entities</td><td>6</td><td>12</td><td>11</td><td>24</td></tr><tr><td>Relationships</td><td>9</td><td>9</td><td>12</td><td>12</td></tr><tr><td>Mandatory Attributes</td><td>22</td><td>34</td><td>27</td><td>43</td></tr><tr><td>Optional Attributes</td><td>12</td><td>—</td><td>16</td><td>—</td></tr><tr><td>Subtypes</td><td>—</td><td>6</td><td>—</td><td>13</td></tr></table>

## 5.3. Participants

Participants in the experiment were 52 computer science students who have taken at least one conceptual modelling course in which they had studied the entityrelationship model (thus, they were second-year computer science students and above). Each was paid \$25 Aust. to encourage them to participate in the experiment and to strive to complete it satisfactorily.

## 5.4. Procedures

Participants were first assigned randomly to one of the four treatments (13 per treatment). They were then run singly through the experiment by a research assistant. He first gave them a consent form and an instruction sheet that described the procedures to be followed and the tasks to be undertaken. In particular, the instruction sheet pointed out that the objective of the experiment was to have participants redraw the conceptual schema diagram as accurately as possible. He also gave them a brief handout reminding them of the major elements of the entity-relationship model and entityrelationship diagrams.

When participants indicated they were ready to begin, the research assistant gave them the diagram associated with the treatment they were to receive. He then gave participants exactly three minutes to study the diagram. During pilot testing, we had found that three minutes was sufficient for participants who engaged with the task to reach an understanding of the

Figure 3 Easy Task: Optional Properties with University-Research Domain  
![](/api/attachments/4MM5YAAC/fulltext/images/dd4a0363f8ae852cff68226e742c36cc5d40ecb435bc58d89cb60dcc1744f048.jpg)

Information Systems Research Vol. 12, No. 4, December 2001

Figure 4 Easy Task: Subtyping with Mandatory Properties with University-Research Domain  
![](/api/attachments/4MM5YAAC/fulltext/images/fe5722ea341ad0b234a8329400919d4239ac61dea6e87c403370abad17aa9ef6.jpg)

Table 3 Analysis of Variance Results for Experiment 1’s Dependent Measures

<table><tr><td>Effect</td><td>Entities</td><td>Relationships</td><td>Attributes</td><td>AttributesTyped</td><td>RelationshipswithCardinalities</td><td>RecalledAttributesCorrectlyTyped</td><td>RecalledRelationshipswith CorrectCardinalities</td></tr><tr><td>R</td><td> $F(1,48) = 22.60$ ,p&lt;0.001</td><td> $F(1,48) = 23.16$ ,p&lt;0.001</td><td> $F(1,48) = 16.42$ ,p&lt;0.001</td><td> $F(1,48) = 13.04$ ,p=0.001</td><td> $F(1,48) = 0.39$ ,p=0.534</td><td> $F(1,40) = 0.99$ ,p=0.325</td><td> $F(1,45) = 3.11$ ,p=0.085</td></tr><tr><td>C</td><td> $F(1,48) = 2.85$ ,p=0.098</td><td> $F(1,48) = 10.49$ ,p=0.002</td><td> $F(1,48) = 8.13$ ,p=0.006</td><td> $F(1,48) = 7.45$ ,p=0.009</td><td> $F(1,48) = 9.25$ ,p=0.004</td><td> $F(1,40) = 0.30$ ,p=0.585</td><td> $F(1,45) = 2.15$ ,p=0.149</td></tr><tr><td>R × C</td><td> $F(1,48) = 0.16$ ,p=0.690</td><td> $F(1,48) = 2.17$ ,p=0.148</td><td> $F(1,48) = 0.30$ ,p=0.589</td><td> $F(1,48) = .002$ ,p=0.964</td><td> $F(1,48) = 1.62$ ,p=0.209</td><td> $F(1,40) = 0.70$ ,p=0.408</td><td> $F(1,45) = 0.32$ ,p=0.574</td></tr><tr><td>Tr</td><td> $F(3,144) = 69.88$ ,p&lt;0.001</td><td> $F(3,144) = 91.64$ ,p&lt;0.001</td><td> $F(3,144) = 282.01$ ,p&lt;0.001</td><td> $F(3,144) = 244.42$ ,p&lt;0.001</td><td> $F(3,144) = 167.63$ ,p&lt;0.001</td><td> $F(3,120) = 9.29$ ,p&lt;0.001</td><td> $F(3,135) = 54.21$ ,p&lt;0.001</td></tr><tr><td>R × Tr</td><td> $F(3,144) = 18.25$ ,p&lt;0.001</td><td> $F(3,144) = 9.00$ ,p&lt;0.001</td><td> $F(3,144) = 3.13$ ,p=0.028</td><td> $F(3,144) = 3.18$ ,p=0.026</td><td> $F(3,144) = 1.89$ ,p=0.134</td><td> $F(3,120) = 3.49$ ,p=0.018</td><td> $F(3,135) = 0.10$ ,p=0.963</td></tr><tr><td>C × Tr</td><td> $F(3,144) = 3.15$ ,p=0.027</td><td> $F(3,144) = 4.67$ ,p=0.004</td><td> $F(3,144) = 1.55$ ,p=0.204</td><td> $F(3,144) = 1.41$ ,p=0.242</td><td> $F(3,144) = 3.92$ ,p=0.010</td><td> $F(3,120) = 2.87$ ,p=0.039</td><td> $F(3,135) = 5.68$ ,p=.001</td></tr><tr><td>R × C × Tr</td><td> $F(3,144) = 0.30$ ,p=0.823</td><td> $F(3,144) = 0.07$ ,p=0.978</td><td> $F(3,144) = 1.31$ ,p=0.274</td><td> $F(3,144) = 0.99$ ,p=0.402</td><td> $F(3,144) = 0.79$ ,p=0.499</td><td> $F(3,120) = 0.25$ ,p=0.860</td><td> $F(3,135) = 0.26$ ,p=0.852</td></tr></table>

Note. R  Representation; C  Task Complexity; Tr  Trial  
Shaded cells have levels of significance below 0.05.

domain. Also, it was not an excessive period of time such that they lost their focus on the task. As participants studied the diagram, they were not permitted to make notes or annotations.

The research assistant then removed the diagram and gave participants a blank sheet of drawing paper. Participants then attempted to redraw the diagram as accurately as they could. When they indicated they could proceed no further, the research assistant removed the sheet of drawing paper and gave them the diagram to study once again. This sequence of steps was followed four times. Overall, the experiment usually lasted about 75 minutes.

## 5.5. Results

Another research assistant who knew the purpose of the research in general but not the propositions that were being tested scored the drawing sheets. Initially we thought it might be necessary to have still another research assistant code the data and undertake a comparison between the two to evaluate the reliability of coding. The coding proved to be straightforward, however, and we relied on only one set of coding.

Seven analyses of the data were undertaken—one for each recall accuracy measure. For each measure, a fully factorial 2 - 2 - 4 repeated-measures analysis of variance model (2 levels of representation, 2 levels of task complexity, 4 trials) was fitted to the data. Table 3 shows the level of significance obtained for the univariate tests of all effects. These results are consistent with those obtained from the multivariate tests which, in the interests of brevity, are not reported here. Table 4 shows the means and standard deviations for each measure averaged across the four trials for the subtyping and optional-properties treatments.

In the interests of brevity, detailed tables of means, standard deviations, and statistical results are not reported here.<sup>3</sup> A description of the detailed data analyses for this experiment (and Experiments 2 and 3) can be obtained from the last author. In summary, however, the major results for Experiment 1 were as follows:<sup>4</sup>

<sup>3</sup>Again, a longer version of this paper containing the more-detailed statistical analyses can be obtained by contacting the last author. <sup>4</sup>For each of the seven measures, note from Table 4 that we have

(1) Consistent with Proposition 1, the optionalproperties group outperformed the mandatoryproperties group in terms of the proportion of entities recalled correctly, relationships recalled correctly, attributes recalled and named correctly, and attributes recalled and typed correctly. Interestingly, for the absolute number of entities recalled correctly, the mandatoryproperties group outperformed the optional-properties group. For the other dependent measures, however, the optional-properties group outperformed the mandatoryproperties group in terms of absolute numbers recalled.

(2) As expected, participants who had to recall the less-complex domain performed better than participants who received the more-complex domain in terms of the proportion of relationships recalled correctly, attributes recalled and named correctly, attributes recalled and typed correctly, and relationships recalled correctly with correct cardinalities.

(3) The optional-properties group outperformed the mandatory-properties group only for Trials 1 and 2 in terms of proportion of entities recalled correctly and Trials 1, 2, and 3 in terms of number of relationships recalled correctly. Thus, consistent with our expectations, there is some evidence of elaborative and inferential reconstruction effects occurring in later trials. For the proportion of attributes recalled and named correctly and the proportion of attributes recalled and typed correctly, the optional-properties group outperformed the mandatory-properties group across all trials.

In short, the results obtained support the proposition that the number-of-constructs effect dominates the elaborative and inferential reconstruction effects when users of conceptual schema diagrams engage in only surface-level processing of a domain’s semantics.

## 6. Experiment 2

The second experiment involved a comprehension task. We hypothesized that the comprehension questions we asked would involve a deeper level of cognitive processing than the recall task used in Experiment 1. For the most part, however, the comprehension questions were still straightforward.<sup>5</sup> They also relied on participants being able to recall the basic features of the conceptual schema diagram they were given. Thus, we expected that the number-of-constructs effect would still dominate the elaborative and inferential reconstruction effects. Nonetheless, because participants were being forced to engage in deeper-level cognitive processing, we hypothesized that differences between the optional-properties participants and mandatoryproperties participants would be less than in Experiment 1. Moreover, we expected that differences between the two groups would dissipate more quickly over trials as higher levels of elaborative and inferential processing took effect.

Table 4 Means and Standard Deviations for Experiment 1’s Dependent Measures

<table><tr><td rowspan="2">Dependent Measure</td><td>Optional</td><td>Mandatory</td></tr><tr><td>Mean(S.D.)</td><td>Mean(S.D.)</td></tr><tr><td>1. Entities</td><td>0.963(0.011)</td><td>0.860(0.098)</td></tr><tr><td>2. Relationships</td><td>0.899(0.018)</td><td>0.720(0.186)</td></tr><tr><td>3. Attributes</td><td>0.686(0.025)</td><td>0.512(0.193)</td></tr><tr><td>4. Attributes Typed</td><td>0.640(0.029)</td><td>0.480(0.189)</td></tr><tr><td>5. Relationships with Cardinalities</td><td>0.530(0.041)</td><td>0.497(0.198)</td></tr><tr><td>6. Recalled Attributes Correctly Typed</td><td>0.890(0.138)</td><td>0.934(0.164)</td></tr><tr><td>7. Recalled Relationships with Correct Cardinalities</td><td>0.562(0.204)</td><td>0.670(0.214)</td></tr></table>

In Experiment 2, participants were shown a conceptual schema diagram on a visual display screen. They were then asked 10 questions to test their understanding of some elementary semantics of the conceptual schema diagram. A computer program controlled presentation of the conceptual schema diagram on the screen, subsequent presentation of questions, recording of participant responses to each question, and measurement of the time required to record each response.

## 6.1. Design and Measures

A mixed design with one between-subjects factor and one within-subjects factor was used. The betweensubjects factor was “type of representation.” It had two levels: Either optional properties or subtypes with only mandatory properties was used in a conceptual schema diagram. The within-subjects factor, “trial,” had five levels. The primary purpose of using multiple trials was to increase the power of the experiment. An ancillary objective was to determine whether differential rates of learning occurred, depending on whether participants received the optional-properties treatment or the mandatory-properties treatment.

Three dependent measures were used:

(1) Accuracy: Participants were asked 10 questions about the semantics underlying the conceptual schema diagram that they were shown on the visual display screen. The computer program used to control the experiment marked their response as either correct or incorrect. Their accuracy score on each trial was the total number of questions that they answered correctly.

(2) Time: The computer program used to control the experiment recorded the time taken (in seconds) by a participant to answer each question. Their time score on each trial was the total time taken for them to answer the 10 questions.

(3) Normalized accuracy: Where accuracy and time are performance measures, it is well known that participants may make tradeoffs—for example, they may compromise accuracy in their responses for increased response speed. Accordingly, a normalized accuracy score was calculated, which is a participant’s accuracy score divided by their time score. A participant’s normalized accuracy score on each trial is the number of accurate answers they provided per elapsed second.

## 6.2. Materials

Materials were based upon two application domains. One pertained to routes taken by the buses owned by a transport company. The other pertained to sales, supplies, and inventory in a distribution company. We had used this latter domain in our first experiment. We used it again in this experiment to enable us to compare our results with those obtained from our first experiment. The former domain was new. We devised it to increase the external validity of the results obtained in the experiment. For each domain, two conceptual schema diagrams were created.<sup>6</sup> The first was an entity-relationship diagram where optional properties were used. No subtypes appeared on the diagram. The second was an entity-relationship diagram where subtypes with only mandatory properties were used. No optional properties appeared on the diagram.

## 6.3. Participants

Participants in the experiment were 52 computer science students (different from those who participated in the first experiment). Each had taken at least one conceptual modelling course in which they had studied the entity-relationship model (thus, they were second-year computer science students and above). As with the first experiment, each was paid \$25 Aust. to encourage them to participate in and to strive to complete the experiment satisfactorily.

## 6.4. Procedures

Prior to their undertaking the experiment, participants were assigned randomly to one of the two application domains. Within each domain, they were then assigned randomly to a treatment (optional properties versus mandatory properties). Thus, within an application domain, each treatment had 13 participants.

When participants arrived to undertake the experiment, they were greeted by a research assistant who explained the nature of the experiment they were to undertake. He provided them with an instruction sheet, a handout that contained a summary of the entity-relationship model to remind them of the major elements in the model, and a consent form to indicate their willingness to take part in the experiment. The instruction sheet indicated that they would be shown an entity-relationship model on a visual display screen for a fixed period. The display would then cease, and they would be asked a set of questions about the diagram. Their goal was to answer these questions as accurately and completely as possible.

Participants undertook the experiment alone. When they were ready to commence, they first keyed in their identifier to the program that controlled the experiment. The program then presented them with a warmup exercise. They were shown an entity-relationship model pertaining to project management of a research application. This application and the associated entityrelationship diagram had been used in our first experiment. Depending upon the treatment to which the participants had been assigned, the diagram had only optional properties or subtypes with mandatory properties. The diagram was shown on a large (20 inch) high-resolution display screen.

After exactly 2.5 minutes had elapsed, the program ceased displaying the diagram. It then displayed the first question. Participants used a mouse to click on a radio button to choose one of three options: “yes,” “no,” or “not sure” (no participants selected the “not sure” option in either the warm-up exercise or the primary experiment). As soon as the participant had made a choice, the program logged the time taken to make the choice. It then displayed the next question. This procedure was repeated until the participant had answered all 10 questions. The program then displayed the entity-relationship diagram again for another 2.5 minutes and subsequently cycled through the 10 questions. After two iterations of displaying the diagram and presenting the questions, the program

## Table 5 Comprehension Questions for the University-Research Domain

1. Is past experience recorded for all employees? 2. Are all projects part of a research program? 3. Is a contact person an attribute of the agency entity? 4. Is the label “author” used for a relationship? 5. Must a research program have at least two projects? 6. Must all employees be led by another employee? 7. Can a research topic be associated with more than one project? 8. Do all employees have a team skill attribute? 9. Are all employees in charge of at least one research project? 10. Must all employees be an author of at least one project report?

stopped. The research assistant then asked participants whether they had any questions about the procedures.

Compared to the first experiment, note that participants had 30 seconds less time to study a diagram. As with the first experiment, we chose the study period based on pilot test experience. The comprehension task seems to be less demanding on a participant’s memory than the recall task. Thus, we concluded less study time was required.

The primary experiment then commenced. Across five repetitions, the program displayed the diagram for 2.5 minutes and then presented the 10 questions associated with the diagram. Overall, participants took about one hour to complete the experiment.

## 6.5. Results

For both domains, Table 6 shows the results for the three performance measures. Table 7 shows the statistically significant effects.<sup>7</sup> In summary, the major results were as follows:

(1) For the bus-route domain, the optionalproperties group outperformed the mandatoryproperties group for Trials 1 and 3 only in terms of normalized accuracy. There were no differences between the two groups in terms of accuracy and time.

(2) For the distribution domain, the optionalproperties group outperformed the mandatoryproperties group in terms of accuracy for Trials 2, 3, 4, and 5 (for the first trial the mandatory-properties group performed better). The optional-properties group also outperformed the mandatory-properties group in terms of normalized accuracy for Trials 3, 4, and 5. The two groups did not differ in terms of time.

As predicted, the results for the bus-route domain suggest that elaborative and inferential reconstruction effects played a greater role in the comprehension task. Performance differences between the two groups were

Table 6 Performance Statistics for Domain Questions in Experiment 2

<table><tr><td rowspan="2" colspan="2"></td><td colspan="6">(a) Accuracy</td></tr><tr><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td><td>Average</td></tr><tr><td rowspan="2">Bus Route</td><td>Optional</td><td>6.077(1.977)</td><td>7.462(1.613)</td><td>7.923(0.760)</td><td>8.462(1.127)</td><td>8.154(1.345)</td><td>7.616</td></tr><tr><td>Mandatory</td><td>4.462(1.898)</td><td>6.846(1.281)</td><td>7.077(1.498)</td><td>7.846(1.463)</td><td>8.154(1.463)</td><td>6.877</td></tr><tr><td rowspan="2">Distribution</td><td>Optional</td><td>4.923(1.605)</td><td>7.769(1.481)</td><td>9.000(1.291)</td><td>9.692(0.630)</td><td>9.538(0.660)</td><td>8.184</td></tr><tr><td>Mandatory</td><td>5.308(1.932)</td><td>6.615(1.261)</td><td>7.538(1.266)</td><td>8.154(1.281)</td><td>8.077(1.706)</td><td>7.138</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="6">(b) Time</td></tr><tr><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td><td>Average</td></tr><tr><td rowspan="2">Bus Route</td><td>Optional</td><td>82.385(21.325)</td><td>68.462(34.777)</td><td>56.769(26.221)</td><td>55.077(29.113)</td><td>43.077(12.189)</td><td>61.154</td></tr><tr><td>Mandatory</td><td>90.077(27.100)</td><td>77.000(25.482)</td><td>68.231(18.829)</td><td>63.615(23.329)</td><td>60.462(25.992)</td><td>71.877</td></tr><tr><td rowspan="2">Distribution</td><td>Optional</td><td>83.385(24.487)</td><td>63.846(16.339)</td><td>51.538(11.348)</td><td>46.308(13.400)</td><td>34.231(10.497)</td><td>55.862</td></tr><tr><td>Mandatory</td><td>101.692(32.707)</td><td>71.154(18.801)</td><td>61.231(19.635)</td><td>55.077(18.773)</td><td>44.000(14.543)</td><td>66.631</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="6">(c) Normalized Accuracy</td></tr><tr><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td><td>Average</td></tr><tr><td rowspan="2">Bus Route</td><td>Optional</td><td>0.080(0.033)</td><td>0.132(0.061)</td><td>0.158(0.052)</td><td>0.184(0.072)</td><td>0.205(0.070)</td><td>0.152</td></tr><tr><td>Mandatory</td><td>0.052(0.023)</td><td>0.101(0.049)</td><td>0.111(0.042)</td><td>0.142(0.074)</td><td>0.162(0.082)</td><td>0.114</td></tr><tr><td rowspan="2">Distribution</td><td>Optional</td><td>0.065(0.039)</td><td>0.136(0.067)</td><td>0.188(0.067)</td><td>0.227(0.072)</td><td>0.299(0.078)</td><td>0.183</td></tr><tr><td>Mandatory</td><td>0.057(0.031)</td><td>0.101(0.039)</td><td>0.137(0.058)</td><td>0.167(0.065)</td><td>0.212(0.098)</td><td>0.135</td></tr></table>

not as clear-cut as in Experiement 1. Contrary to expectations, however, for the distribution domain the optional-properties group still outperformed the mandatory-properties group. Moreover, for the distribution domain, any differences between the two groups did not dissipate faster relative to Experiment 1.

## 7. Experiment 3

The third experiment involved a problem-solving task. Our goal was to test the second proposition, in which we predicted that the elaborative and inferential reconstruction effects associated with deep processing of domain semantics would dominate the number-ofconstructs effect. Gemino suggested the design to us. Our experiment is a replication and extension of his work. His work, in turn, borrows from work we conducted in our first two experiments.<sup>8</sup>

Table 7 Summary of Significant Effects in Experiment 2

<table><tr><td rowspan="2"></td><td colspan="3">Bus-Route Domain</td><td colspan="3">Distribution Domain</td></tr><tr><td>Accuracy</td><td>Time</td><td>Nor. Acc.</td><td>Accuracy</td><td>Time</td><td>Nor. Acc.</td></tr><tr><td rowspan="3">Representation</td><td>F = 3.100</td><td>F = 1.687</td><td>F = 4.298</td><td>F = 7.626</td><td>F = 3.880</td><td>F = 6.241</td></tr><tr><td>df = 1,24</td><td>df = 1,24</td><td>df = 1,24</td><td>df = 1,24</td><td>df = 1,24</td><td>df = 1,24</td></tr><tr><td>p = 0.091</td><td>p = 0.206</td><td>p = 0.049</td><td>p = 0.011</td><td>p = 0.061</td><td>p = 0.020</td></tr><tr><td rowspan="3">Trial</td><td>F = 28.870</td><td>F = 19.742</td><td>F = 34.625</td><td>F = 55.105</td><td>F = 49.830</td><td>F = 64.910</td></tr><tr><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td></tr><tr><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr><tr><td rowspan="3">Representation × Trial</td><td>F = 1.679</td><td>F = 0.441</td><td>F = 0.278</td><td>F = 3.654</td><td>F = 0.568</td><td>F = 2.528</td></tr><tr><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td><td>df = 4,96</td></tr><tr><td>p = 0.161</td><td>p = 0.779</td><td>p = 0.892</td><td>p = 0.008</td><td>p = 0.686</td><td>p = 0.046</td></tr></table>

Note. Shaded cells have levels of significance below 0.05.

## 7.1. Design and Measures

A between-subjects, single-factor design was used. Once more, the factor was “type of representation” with two levels: a conceptual schema diagram with either optional properties or subtypes with only mandatory properties.

The dependent measure was problem-solving performance. Participants were asked nine problem-solving questions about the domain they were given. The first five for the bus-route domain were developed by Gemino (1998, 1999) for his experiment (see also Gemino and Wand 1998).<sup>9</sup> We prepared an additional four for this domain, plus nine for the university-research domain.<sup>10</sup> In developing these questions, we sought also to tap a deeper level of cognitive processing among our participants than the level elicited by Gemino with his participants. In addition, unlike Gemino who used a single measure of problem-solving performance, we used three measures: (a) the number of correct answers provided by a participant based upon information contained in the conceptual schema diagram; (b) the number of correct answers provided by a participant based upon extra-model knowledge (i.e., the answer was a plausible response, but it was not based on any information contained in the diagram); and (c) the number of incorrect answers provided by the participant.<sup>11</sup> In principle, note that the three measures should only be weakly related. For example, an incorrect answer that increases the score for the third measure does not mean that the scores for the first and second measures have to be decreased.

# Table 8 Problem-Solving Questions Asked for the University-Research Domain

1. A research project that was supposed to be completed last month has not been completed. What reasons can you provide for the delay in completion? Write down as many reasons as you can think of.

3. An employee has come up with a brilliant research idea and has submitted a research proposal. The research committee considered the proposal among other proposals and did not approve this proposal. What could be the reason for the rejection of this proposal? Write as many reasons as you can think of.

5. A research project cannot be associated with a research topic. What would have caused this situation to occur? Write as many reasons as you can think of.

6. A research project has been prematurely terminated. Write as many possible reasons as you can think of for this situation.

7. How can you ensure that a research project is completed on time? Write as many factors as you can think of that should be considered.

8. How can you increase the likelihood of support for funds from the agency? Write as many factors as you can think of that should be considered.

9. How can the team leader ensure that the team will be able to complete the research project? Write down as many possible factors as you can think of that need to be considered.

## 7.2. Materials

Materials were based upon two application domains we had used previously: the bus-route domain and the university-research domain. Gemino had used the busroute domain, so we sought to compare our results with his. He had not used the university-research domain, however, so we sought to extend the generality of his results. For each domain, two conceptual schema diagrams were again created: one with optional properties, and one with subtyping and mandatory properties.

Materials for each of the four treatments (two treatments for each of the two domains) comprised seven parts: (a) an instruction sheet describing the nature of the experiment overall; (b) a consent form; (c) a short questionnaire to collect background information about the participant, including their perceptions about their knowledge of and confidence in entity-relationship diagrams and their knowledge of the application domain they would receive; (d) a brief summary of the major elements of the entity-relationship model; (e) an entityrelationship diagram for the treatment a participant would receive; (f) 12 comprehension questions relating to the domain that the participant would receive; and (g) nine problem-solving questions relating to the domain that the participant would receive.

## 7.3. Participants

Participants in the experiment were 96 computer science/information systems students (different from those who participated in the first two experiments). Each had taken at least one conceptual modelling course in which they had studied the entity-relationship model. As with the first and second experiments, each was paid \$25 Aust. to encourage them to participate in and to strive to complete the experiment satisfactorily.

## 7.4. Procedures

Prior to their undertaking the experiment, participants were assigned randomly to one of the two application domains. Within each domain, they were then assigned randomly to a treatment (optional versus mandatory properties). Thus, within an application domain, each treatment had 24 participants.

When participants arrived to undertake the experiment, a research assistant greeted them. He provided them with an instruction sheet describing the nature of the experiment they were about to undertake and a consent form. After participants had read the instruction sheet and signed the consent form, the research assistant explained the nature of the experiment verbally and then responded to any questions.

Participants undertook the experiment in small groups (usually about 3–5 students). They performed four tasks:

(1) Completed the questionnaire that asked them about their knowledge of and confidence in using entity-relationship diagrams and their knowledge of the application domain they would study.

Table 9 Descriptive Statistics and Significance Tests for Experiment 3

<table><tr><td rowspan="2"></td><td rowspan="2">N</td><td rowspan="2">Group</td><td colspan="3">Bus-Route Domain</td><td colspan="3">University-Research Domain</td></tr><tr><td>Mean</td><td>Std. Dev.</td><td>t</td><td>Mean</td><td>Std. Dev.</td><td>t</td></tr><tr><td rowspan="2">PS1</td><td>24</td><td>Optional</td><td>14.292</td><td>5.336</td><td>-2.500</td><td>15.083</td><td>4.568</td><td>-2.639</td></tr><tr><td>24</td><td>Mandatory</td><td>18.583</td><td>6.500</td><td>(0.016)</td><td>19.250</td><td>6.243</td><td>(0.011)</td></tr><tr><td rowspan="2">PS2</td><td>24</td><td>Optional</td><td>3.292</td><td>3.277</td><td>-0.655</td><td>8.375</td><td>6.219</td><td>-0.048</td></tr><tr><td>24</td><td>Mandatory</td><td>4.000</td><td>4.160</td><td>(0.516)</td><td>8.458</td><td>5.786</td><td>(0.962)</td></tr><tr><td rowspan="2">PS3</td><td>24</td><td>Optional</td><td>8.875</td><td>4.928</td><td>3.430</td><td>4.458</td><td>4.511</td><td>2.042</td></tr><tr><td>24</td><td>Mandatory</td><td>5.000</td><td>2.520</td><td>(0.001)</td><td>2.417</td><td>1.909</td><td>(0.047)</td></tr></table>

Note. PS1  correct problem solving based on entity-relationship diagram  
PS2  correct problem solving not based on entity-relationship diagram  
PS3  incorrect problem solving  
All t-tests are two-tailed tests.  
Shaded cells have levels of significance below 0.05.

(2) For five minutes exactly, studied the experimental materials that provided them with a reminder of the major elements of the entity-relationship model.

(3) For ten minutes exactly, studied the entityrelationship diagram they had been assigned and answered the comprehension questions. Unlike in the second experiment, in this experiment participants could refer to the diagram as they attempted the comprehension questions. In this experiment our goal was not to test differences in comprehension performance, but to force participants to engage in elaboration and inferential reconstruction processes as soon as possible.<sup>12</sup> Given the time required to undertake the problem-solving questions, we concluded that we could not ask participants to perform multiple trials of the problem-solving task. Thus, we needed to mitigate recall effects on our results.

(4) For 30 minutes exactly, answered the problemsolving questions. Participants could not refer to the entity-relationship diagram during this period.

At the conclusion of the experiment, participants were asked not to discuss their experiences with other students. Overall, the experiment took about 75 minutes to complete.

## 7.5. Results

Four independent coders who were blind to the proposition being tested in the research coded the responses. Two coded all responses for the bus-route domain. The other two coded all responses for the university-research domain. The responses for each domain were randomly ordered before they were given to the coders. Each coder first worked independently. For the bus-route domain, the coders achieved the following levels of consensus in their first-pass coding as measured by the Pearson correlation coefficient: (a) 0.856 for correct responses based on the entityrelationship diagram; (b) 0.836 for correct responses not based on the entity-relationship diagram; and (c) 0.589 for incorrect responses. For the universityresearch domain, the corresponding Pearson correlation coefficients were 0.903, 0.911, and 0.683. The coders then discussed responses where they disagreed to resolve their differences. These final codes formed the basis for the data analysis

Table 9 shows descriptive statistics and the outcomes of significance tests. For both the bus-route domain and the university-research domain, the mandatory-properties group outperformed the optional-properties group in terms of the number of correct answers based on the entity-relationship diagram and the number of incorrect answers. For both domains, the two groups did not differ, however, in terms of the number of correct answers not based on the entity-relationship diagram. Gemino’s (1998, 1999) mandatory-properties group also outperformed his optional-properties group in terms of problem-solving performance relating to the bus-route domain. Thus, the results are consistent with Proposition 2. The elaborative and inferential reconstruction effects that we predict are evoked by deep processing of domain semantics appear to dominate the number-of-constructs effect.

## 8. Implications of the Research

The results of our research have implications for both practice and research. For practice, they signal the need to be circumspect about using optional properties in conceptual schema diagrams. On the one hand, use of optional properties allows designers to draw simpler conceptual schema diagrams in the sense that the diagrams have fewer elements. If the diagrams are to be used to obtain an overview of the application domain, our results indicate that those based on optional properties provide a satisfactory representation of a domain. If conceptual schema diagrams are to be used to support deep-level cognitive processing by their users, however, both Gemino’s (1998, 1999) results and our results support the proposition that optional properties should be proscribed. Indeed, the decline in deeplevel cognitive processing performance that occurs when optional properties are used appears to be substantial (in Table 9, compare the average scores for the three measures of problem-solving performance across the two domains).

One outcome of complying with our regime of proscribing optional properties for deep-level cognitive processing requirements is that the conceptual schema diagrams prepared by practitioners will increase in size. Indeed, practitioners have quickly voiced this concern when we have discussed our results with them. We contend, however, that three factors militate against this concern. First, there is little point to having concise conceptual schema diagrams if they do not communicate needed semantics. Instead, the goal should be to communicate the semantics of the domain accurately and completely in the most concise way possible. Second, when we have applied our regime to practical problems, our experience is that the diagrams do not explode in an uncontrolled way. True, combinatorial explosion will occur if optional properties all tend to be dependent on one another—in other words, the presence of one optional property dictates the presence or absence of another optional property. In the presence of dependent optionals, mutually exclusive subtypes have to be formed. Our experience is, however, that independent optional properties are more common. As a result, overlapping subtypes arise, and combinatorial explosion of conceptual schema diagrams does not occur. Third, the complexity of conceptual schema diagrams can always be controlled through levelling procedures. In other words, composition and decomposition techniques can be used to either mask or reveal detailed semantics.

For research, our results indicate the need to build and test a contingency theory that accounts for different types of transfer-of-meaning needs among different users of conceptual schema diagrams. For example, we have argued that deep-type meaning transfer is critical for end users who frequently interrogate a database and analysts or programmers who must maintain a system. Surface-type meaning transfer might be satisfactory, however, for managers who require only a high-level understanding of a domain. We need a theory that will enable us to predict and understand how different characteristics of conceptual schema diagrams will enhance or undermine the different types of meaning transfer that different types of stakeholders require. We have argued above that such a theory will be based on theories of memory and ontology.

Our results also provide a way to structure research that investigates why in practice conceptual schema diagrams are either no longer prepared or quickly fall into disuse during system development projects. We predict the answer hinges on the fact that most conceptual schema diagrams prepared in practice facilitate surface-level transfer of meaning but not deeplevel transfer of meaning. Surface-level transfer of meaning might be satisfactory at the outset of a system development project where stakeholders often acquire high levels of familiarity with the semantics of the domain they are seeking to represent. Surface-level transfer of meaning might also be satisfactory for users who sustain their understanding of the semantics of a domain through frequent interaction with the information system that represents it. Deep-level transfer of meaning is likely to be required, however, for stakeholders who do not interact frequently with the information systems (e.g., casual users of a database) or new stakeholders (e.g., maintenance programmers who were not involved with the system at the outset). Overall, we need a much richer understanding of how different types of conceptual schema diagrams facilitate transfer of meaning. Based on this understanding, we then need to provide much more precise conceptual modelling guidelines for practitioners if they are to assist stakeholders to obtain an understanding of the semantics of the domain that is represented by an information system.

Finally, we have a sense of de´ja\` vu with our findings. Long ago, Newell and Simon (1972) reported the critical impact that different representations could have on problem-solving efficacy.<sup>13</sup> In particular, they highlighted the importance of the initial representation given to problem solvers because of the difficulties they subsequently encounter in changing representations. Perhaps we might get richer insights into the impact that different types of conceptual schema diagrams will have on systems development processes if we recognize that we are dealing with an instance of an age-old problem.

## Acknowledgments

The authors thank Reece Edwards and Tan Chong Jin for their assistance with the first two experiments described in this paper and Andreas Opdahl and Peter Green for their comments on the third experiment described in this paper. The authors are especially in debted to Andrew Gemino for his insights, which led to the conduct of our third experiment. An earlier version of a paper describing the first experiment was presented as a research-in-progress session at the Seventeenth Annual International Conference on Information Systems. The authors thank attendees at their session for their helpful comments. Their thanks, also, to Izak Benbasat, Veda Storey, four reviewers, Rudy Hirschheim, Andrew Gemino, Paul Bowen, Yair Wand, and participants in workshops at the University of Michigan, University of Melbourne, City University of Hong Kong, and National Sun Yat-Sen University for comments on earlier versions of the paper. Supporting grants for the research were provided by the Australian Research Council, GWA Ltd., and the School of Commerce, The University of Queensland.

## References

Anderson, J. R., P. L. Pirolli. 1984. Spread of activation. J. Experiment. Psych.: Learning, Memory, and Cognition. 10 791–798.

Ashcraft, M. H. 1989. Human Memory and Cognition. Scott, Foresman and Company, Glenview, IL.

Batini, C., S. Ceri, S. B. Navathe. 1992. Conceptual Database Design: An Entity-Relationship Approach. Benjamin/Cummings, Redwood City, CA.

Batra, D., G. M. Marakas. 1995. Conceptual data modelling in theory and practice. Euro. J. Inform. Systems 4 185–193.

——, J. A. Hoffer, R. P. Bostrom. 1990. Comparing representations with relational and EER models. Commun. ACM 33 126–139.

Boehm, B. 1981. Software Engineering Economics. Prentice-Hall, Upper Saddle River, NJ.

Bradshaw, G. L., J. R. Anderson. 1982. Elaborative encoding as an explanation of levels of processing. J. Verbal Learning and Verbal Behavior 21 165–174.

Bunge, M. 1977. Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World. Reidel, Boston, MA.

Cattell, R. G. G. 1994. Object Data Management: Object-Oriented and Extended Relational Database Systems, Rev. edition. Addison-Wesley, Reading, MA.

Collins, A. M., M. R. Quillian. 1969. Retrieval times from semantic memory. J. Verbal Learning and Verbal Behaviour 8 240–247.

Ernest, C. H. 1991. Ability differences and prose learning. Intelligence 15 455–477.

Gemino, A. 1998. To be or may to be: An empirical comparison of mandatory and optional properties in conceptual modelling. Proc. Ann. Conf. Admin. Sci. Assoc. of Canada, Information Systems Division. Saskatoon, Saskatchewan, 33–44.

——. 1999. Empirical methods for comparing system analysis modelling techniques. Unpublished PhD thesis, University of British Columbia, Vancouver, B.C., Canada.

, Y. Wand. 1998. Empirical methods for comparing system analysis methods. K. Siau, ed. Proc. CAiSE ‘98/IFIP 8.1 Internat. Workshop on Evaluation of Modelling Methods in System Anal. and Design. Pisa, Italy, 1–12.

Goldstein, R. C., V. Storey. 1990. Some findings on the intuitiveness of entity-relationship constructs. F. H. Lochovsky, ed. Entity Relationship Approach to Database Design. Elsevier Science Publishers, B. V., North Holland, Amsterdam, 9–23.

Hirschheim, R., H. Klein., K. Lyytinen. 1995. Information Systems Development and Data Modelling: Conceptual Foundations and Philosophical Foundations. Cambridge University Press, Cambridge, UK.

Hitchman, S. 1995. Practitioner perceptions of the use of some semantic concepts in the entity-relationship model. Euro. J. Inform. Systems 4 31–40.

Kilov, H., J. Ross. 1994. Information Modelling: An Object-Oriented Ap proach. Prentice-Hall, Upper Saddle River, NJ.

Maier, R. 1996. Benefits and quality of data modelling–results of an empirical analysis. Proc. Fifteenth Internat. Conf. Entity-Relationship Approach. Cottbus, Germany, 245–260.

Mayer, R. E. 1989. Models for understanding. Rev. Ed. Res. 59 43–64. ——, J. K. Gallini. 1990. When is an illustration worth a thousand words. J. Ed. Psych. 82 715–726.

Moody, D. L. 1998. Metrics for evaluating the quality of entity relationship models. Proc. Seventeenth Internat. Conf. Conceptual Modelling. Singapore.

——, G. Shanks. 1998. Improving the quality of entity-relationship models: An action research programme. Australian Computer J. 30 129–138.

Mylopoulous, J. 1998. Information modelling in the time of the revolution. Inform. Systems 23 127–155.

Newell, A., H. A. Simon. 1972. Human Problem Solving. Prentice-Hall, Upper Saddle River, NJ.

Owens, J., G. H. Bower, J. B. Black. 1979. The ‘soap opera’ effect in story recall. Memory and Cognition 7 185–191.

Prietula, M. J., S. T. March. 1991. Form and substance in physical database design: An empirical study. Inform. Systems Res. 2 287– 314.

Shenk, D. 1997. Data Smog: Surviving the Information Age. Little, Brown, New York.

Walrad, C., E. Moss. 1993. Measurement: The key to application development quality. IBM Systems J. 32 445–460.

Wand, Y., V. Storey, R. Weber. 1999. An ontological analysis of the relationship construct in conceptual modelling. ACM Trans. Database Systems 24 494–528.

Weber, R. 1996. Are attributes entities? A study of database designers’ memory structures. Inform. Systems Res. 7 137–162.

——, Y. Zhang. 1996. An analytical evaluation of NIAM’s grammar for conceptual schema diagrams. Inform. Systems J. 6 147–170.

Veda Storey, Associate Editor. This paper was received on September 30, 1999, and was with the authors 10 months for 3 revisions.
