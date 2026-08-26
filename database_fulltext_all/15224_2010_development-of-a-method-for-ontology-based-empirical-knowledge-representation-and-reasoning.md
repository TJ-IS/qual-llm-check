---
otero_id: 15224
otero_key: "4WKKR4FQ"
title: "Development of a method for ontology-based empirical knowledge representation and reasoning"
authors: "Yuh-Jen Chen"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.02.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development of a method for ontology-based empirical knowledge representation and reasoning

Yuh-Jen Chen ⁎

Department of Accounting and Information Systems, National Kaohsiung First University of Science and Technology, Kaohsiung, Taiwan, ROC

## a r t i c l e i n f o

Article history: Received 7 September 2009 Received in revised form 26 February 2010 Accepted 28 February 2010 Available online 4 March 2010

Keywords: Empirical knowledge Ontology OWL Knowledge representation Knowledge reasoning

## a b s t r a c t

In the knowledge economy era of the 21st century [14,17], the competitive advantage of enterprises has shifted from visible equipment, capital and labor in the past to invisible knowledge nowadays. Knowledge can be distinguished into tacit knowledge and explicit knowledge. Meanwhile, tacit knowledge largely encompasses empirical knowledge dif<sup>fi</sup>cult to be documented and generally hidden inside of personal mental models. The inability to transfer tacit knowledge to organizational knowledge would cause it to disappear after knowledge workers leaving their post, ultimately losing important intellectual assets for enterprises. Therefore, enterprises attempting to create higher knowledge value are highly concerned with how to transfer personal empirical knowledge inside of an enterprise into an organizational explicit knowledge by using a systematic method to manage and share such valuable empirical knowledge effectively. This study develops a method of ontology-based empirical knowledge representation and reasoning, which adopts OWL (Web Ontology Language) to represent empirical knowledge in a structural way in order to help knowledge requesters clearly understand empirical knowledge. An ontology reasoning method is subsequently adopted to deduce empirical knowledge in order to share and reuse relevant empirical knowledge effectively. Speci<sup>fi</sup>cally, this study involves the following tasks: (i) analyze characteristics for empirical knowledge, (ii) design an ontology-based multi-layer empirical knowledge representation model, (iii) design an ontology-based empirical knowledge concept schema, (iv) establish an OWL-based empirical knowledge ontology, (v) design reasoning rules for ontology-based empirical knowledge, (vi) develop a reasoning algorithm for ontology-based empirical knowledge, and (vii) implement an ontology-based empirical knowledge reasoning mechanism. Results of this study facilitate the tacit knowledge storage, management and sharing to provide knowledge requesters with accurate and comprehensive empirical knowledge for problem solving and decision support. © 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The global economy has shifted recently from a manufacturingbased value system to a knowledge-based one. Knowledge is essential for entrepreneurial success in the knowledge economy era. Capable of deciding the life or death of an enterprise, knowledge application has become pivotal for enhancing entrepreneurial competitiveness. Consequently, an effective means of improving the competitive advantage of an enterprise is to promote its organizational knowledge value through knowledge accumulation and sharing, as well as effective management of the accumulated empirical knowledge from employees in an enterprise. The increasing importance of an enterprise to implement knowledge management [4,9,13] in the knowledge economy era is thus apparent.

Enterprise knowledge management can be implemented as either a systematization strategy or a personalization strategy [13,26]. Systematization strategy largely focuses on managing explicit knowledge and increasing the dispersion and distribution of explicit knowledge through information systems. Meanwhile, personalization strategy allows experts to own tacit knowledge by cooperating and communicating with a certain expert. Additionally, tacit knowledge [7,12] generally symbolizes an enterprise value and is generally hidden inside of personal mental models. The inability to transfer tacit knowledge to organizational knowledge (i.e., explicit knowledge) would cause it to disappear after knowledge workers leave their post, ultimately losing important intellectual assets for enterprises. Therefore, enterprise attempting to create higher knowledge value are highly concerned with how to transfer personal empirical knowledge inside of an enterprise into organizational explicit knowledge by using a knowledge-based system to manage and share such valuable empirical knowledge effectively.

Recent studies [2,17,30,32,34,36,37] indicated that most knowledge-based systems cannot effectively address the representation, storage and reasoning for empirical knowledge to offer accurate and comprehensive empirical knowledge for knowledge requesters. This circumstance incurs a bottleneck when sharing personal empirical knowledge in an enterprise.

Ontology [5,8,10,11,19,24] refers to a consensus that de<sup>fi</sup>nes an entity, attribute and relationship among knowledge concepts within a speci<sup>fi</sup>c domain using explicit descriptions and speci<sup>fi</sup>cations that present an interoperable format understandable by both humans and machines, thereby it can be used for building knowledge-based systems.

This study develops a method of ontology-based empirical knowledge representation and reasoning, which mainly uses OWL (Web Ontology Language) to represent empirical knowledge in a structural manner to help knowledge requesters clearly understand the empirical knowledge. An ontology reasoning method is subsequently adopted to deduce empirical knowledge in order to share and reuse relevant empirical knowledge effectively. Speci<sup>fi</sup>cally, this study involves the following tasks: (i) analyze characteristics for empirical knowledge, (ii) design an ontology-based multi-layer empirical knowledge representation model, (iii) design an ontology-based empirical knowledge concept schema, (iv) establish an OWL-based empirical knowledge ontology, (v) design reasoning rules for ontology-based empirical knowledge, (vi) develop a reasoning algorithm for ontology-based empirical knowledge, and (vii) implement an ontology-based empirical knowledge reasoning mechanism.

The rest of this paper is organized as follows. Section 2 de<sup>fi</sup>nes the ontology-based representation model for empirical knowledge based on the identi<sup>fi</sup>ed characteristics of empirical knowledge. Section 3 then describes the ontology-based reasoning method for empirical knowledge. Next, Section 4 presents an example of <sup>fi</sup>nancial diagnosis of an enterprise to illustrate how to implement the proposed method of ontology-based empirical knowledge representation and reasoning. Section 5 summarizes the results of implementing a prototype ontology-based empirical knowledge reasoning mechanism. Conclusions are <sup>fi</sup>nally drawn in Section 6, along with recommendations for future research.

## 2. Design of ontology-based empirical knowledge representation model

This section analyzes the characteristics of empirical knowledge and then describes the design of an empirical knowledge representation model as well as empirical knowledge concept schema by using ontology techniques.

Table 1  
Empirical knowledge characterization.

<table><tr><td></td><td>Empirical Knowledge</td><td>Description</td></tr><tr><td>Composition Element</td><td>Problem/Cause/Solution</td><td>As either a problem solving method or a modified action, empirical knowledge can be described by three elements of problem, cause, and solution.</td></tr><tr><td>Feature</td><td>Tacit</td><td>Characterized as generally having a particular context and personalization, empirical knowledge is not easily understood, learned, imitated, communicated, transferred, and shared.</td></tr><tr><td rowspan="5">Characteristic</td><td>Hierarchical</td><td>Empirical knowledge can be distinguished into different layers based on the use purpose.</td></tr><tr><td>Descriptive</td><td>“Descriptive” refers to the concept, class, and structure of empirical knowledge.</td></tr><tr><td>Causal</td><td>“Causal” refers to the causality and consequence of empirical knowledge.</td></tr><tr><td>Procedural</td><td>“Procedural” refers to the operational activity and procedure of an event.</td></tr><tr><td>Relational</td><td>“Relational” refers to how operational activities of an event are related.</td></tr><tr><td rowspan="2">Trait</td><td>Action-oriented</td><td>Empirical knowledge can be viewed as action-oriented knowledge, which is represented by conditional action.</td></tr><tr><td>Skillful</td><td>Skill indicates the objective-oriented expressional behavior, which is difficult to be represented by language. While empirical knowledge can be treated as action-oriented knowledge, an action can represent knowledge through its skill.</td></tr></table>

## 2.1. Empirical knowledge characterization

Based on reviewing and integrating relevant empirical knowledge literature [1,3,16,18,22,23,25–29,31,33,36,39], empirical knowledge is used here to mean: dif<sup>fi</sup>cult and costly to transfer, making it considerably less mobile than more explicit forms. Firms can possess unique capabilities that are hard to replicate and often are invisible to outside observers. For a notable example is particular knowledge such as empirical rule or know-how.

This study analyzes and explains empirical knowledge in terms of composition element, trait, characteristic, and feature, as shown in Table 1.

## 2.2. Ontology-based empirical knowledge representation model design

This section <sup>fi</sup>rst divides empirical knowledge into four different layers of “know-what”, “know-why”, “know-how”, and “know-with” based on the empirical knowledge characterization in Section 2.1. The conceptual model of ontology-based multi-layer empirical knowledge representation is then designed by using ontology techniques, as shown in Fig. 1.

In Fig. 1, descriptive empirical knowledge is de<sup>fi</sup>ned as a knowwhat layer that identi<sup>fi</sup>es class, hierarchy, layer, and composition of empirical knowledge; in addition, the relationships include the taxonomy relationship $" \mathrm { I s \_ a " }$ and the partonomy relationship “Part\_ of”. Casual empirical knowledge is treated as a know-why layer that explains the causality and is a consequence of empirical knowledge. Therefore, the relationships are de<sup>fi</sup>ned as “Cause” and “Caused\_by”, respectively. Moreover, procedural empirical knowledge is de<sup>fi</sup>ned to a know-how layer that describes the operational activity and procedure of an event; the relationships are “Follow” and “Is\_followed\_by”. Finally, the know-with layer mainly presents the relational empirical knowledge that records the relationships among operational activities of an event. The relationship is therefore de<sup>fi</sup>ned as “Cooperate\_with” to represent the collaboration among empirical knowledge concepts.

![](/api/attachments/4WKKR4FQ/fulltext/images/374dad52768d6f2442a534f34ff6e05d397c2cf77cbefc93b46a78629c7aafc2.jpg)  
Fig. 1. Conceptual model of ontology-based multi-layer empirical knowledge representation.

## 2.3. Ontology-based empirical knowledge concept schema design

For the empirical knowledge concept in the conceptual model of ontology-based empirical knowledge representation designed in Section 2.2, this section adopts the object-oriented method [20,38] to design an concept schema of empirical knowledge, as shown in Fig. 2. The schema is used to construct empirical knowledge ontology, so as to design reasoning rules and reason empirical knowledge. The empirical knowledge concept schema consists of three elements of concept, property, and relationship. Each element is described as follows:

· Concept: Concept refers to the name of the basic unit that can constitute an empirical knowledge ontology to express a visible or invisible object.

· Property: Empirical knowledge properties include “Concept\_ID”, “De<sup>fi</sup>nition”, “Synonym”, “Appearance Reason”, “Status”, and “Action”. Meanwhile, “Concept\_ID” refers to the number of empirical knowledge concepts, while the property “De<sup>fi</sup>nition” describes a certain concept of empirical knowledge, making it easy to understand and specify. Furthermore, the property “Synonym” describes the same semantic using various terms for an empirical knowledge concept. Additionally, “Appearance Reason” and “Status” are de<sup>fi</sup>ned based on the causal relationships “Cause” and “Cause\_by” for expressing casual empirical knowledge (knowwhy layer). For the rationality of logical reasoning, the value of property “Appearance Reason” is de<sup>fi</sup>ned to have one or more characteristic values according to particular domain requirements in order to properly express the appearance reason of an empirical knowledge concept, while the value of property “Status” is either normal or abnormal. The property “Action” is adopted for expressing the procedural empirical knowledge (know-how layer) or relational empirical knowledge (know-with layer) based on the procedural relationships “Follow” and “Is\_followed\_ by” or the cooperative relationship “Cooperate\_with”. The value of property “action” refers to a characteristic value based on the particular domain requirements in order to satisfy the rationalit of logical reasoning.

· Relationship: Relationships between empirical knowledge concepts include “Is\_a”, “Part\_of”, “Cause”, “Cause\_by”, “Follow”, “Is\_followed\_ by”, and “Cooperate\_with”. Meanwhile, the relationship “Is\_a” indicates the classi<sup>fi</sup>cation relationship between empirical knowledge concepts, while the relationship “Part\_of” indicates the part-whole relationship between empirical knowledge concepts. Moreover, the relationships “Cause” and “Cause\_by” represent the causal relationship between empirical knowledge concepts. Finally, the relationships “Follow” and “Is\_followed\_by” refer to the procedural relationship between empirical knowledge concepts. Meanwhile, the relationship “cooperate\_with” is the collaborative relationship between empirical knowledge concepts.

## 3. Development of ontology-based empirical knowledge reasoning method

Based on the designed ontology-based empirical knowledge representation model in Section 2, this section develops related techniques to empirical knowledge reasoning, which involves “OWLbased empirical knowledge ontology establishment”, “ontologybased reasoning rules design for single-layer empirical knowledge”, “ontology-based reasoning rules design for cross-layer empirical knowledge”, and “reasoning algorithm design for ontology-based empirical knowledge” as well.

## 3.1. Establishment of OWL-based empirical knowledge ontology

According to the conceptual model of ontology-based empirical knowledge representation and the ontology-based empirical knowledge concept schema designed in Section 2, an OWL-based empirical knowledge ontology is developed in the following based on the basic axiom and constraint of OWL DL [6,15,21] and OWL language, thus paving the way for reasoning rules design of ontology-based empirical knowledge. Table 2 lists the relevant symbols for establishing OWLbased empirical knowledge ontology.

In Table 2, OWL-based empirical knowledge ontology is composed of different OWL constructs. Each OWL construct can be represented by a different DL Syntax. Each OWL construct is detailed as bellow.

(i) rdf:subClassof: the hierarchical relationship between two concept classes.

(ii) owl:ObjectProperty: the object relationship between two concept objects.

(iii) owl:TransitiveProperty: the inheritance relationship between two concepts. In the relationship, the inheritance inherits the characteristics from the original concept that had been inherited.

![](/api/attachments/4WKKR4FQ/fulltext/images/5ca6a5b01df4d50463f5586c8a84dadd9de9c72606ca12aba460eed0a0267b8d.jpg)  
Fig. 2. Empirical knowledge concept schema.

Table 2  
Relevant symbols for establishment of OWL-based empirical knowledge ontology.

<table><tr><td>OWL construct</td><td>DL syntax</td><td>Relationship of empirical knowledge ontology</td></tr><tr><td>rdf:subClassof</td><td> $\subseteq$ </td><td>Is_a</td></tr><tr><td>owl:ObjectProperty</td><td> $P \subseteq P_i$ </td><td>Part_of, Cause, Follow, Cooperate_with</td></tr><tr><td>owl:TransitiveProperty</td><td> $P^+ \subseteq P$ </td><td></td></tr><tr><td>owl:SymmetricProperty</td><td> $P_1 \equiv P_{\overline{1}}^-$ </td><td>Cooperate_with</td></tr><tr><td>owl:inverseOf</td><td> $P \equiv P^-$ </td><td>Has_part, Caused_by, Is_followed_by, ...etc.</td></tr><tr><td>OWL Construct</td><td>DL Syntax</td><td>Property of Empirical Knowledge Ontology</td></tr><tr><td>owl:DatatypeProperty</td><td> $U \subseteq U_i$ </td><td>Appearance Reason, Status, Action</td></tr><tr><td>owl:minCardinality</td><td> $\geq n P$ </td><td>Appearance Reason</td></tr><tr><td>owl:maxCardinality</td><td> $\leq n P$ </td><td>Status, Action</td></tr></table>

(iv) owl:SymmetricProperty: the relationship symmetry between two concepts.

(v) owl:inverseOf: the reversibility between concept relationships.

(vi) owl:DatatypeProperty: the data property of a concept.

(vii) owl:minCardinality: constraint on the minimum of a property value.

(viii) owl:maxCardinality: constraint on the maximum of a property value.

By using the above OWL constructs, the empirical knowledge concept, relationship and property of OWL-based empirical knowledge ontology are established, as shown in Figs. 3 and 4, respectively.

Fig. 3 shows the empirical knowledge concept and relationship of OWL-based empirical knowledge ontology. First, the empirical knowledge ontology uses the OWL construct rdf:subClassof to represent a situation in which the taxonomy relationship “Is\_a”exists between the empirical knowledge concepts A and B, implying that the empirical knowledge concept A is the subclass of empirical knowledge concept B. The partonomy relationship “Part\_of” exists between empirical knowledge concepts D and E, indicating that empirical knowledge concept D belongs to empirical knowledge concept

E. Additionally, the partonomy relationship “Part\_of” can become the transitive relationship through the OWL construct owl:Transitive-Property. Moreover, a causal relationship “Cause” exists between empirical knowledge concepts H and I. Therefore, the relationship “Caused\_by” is the inversive relationship of the relationship “Cause” by using the OWL construct owl:inverseOf. A cooperative relationship “Cooperate\_with” exists between the empirical knowledge concepts N and O, implying that empirical knowledge concept N cooperates with empirical knowledge concept O. Through the OWL construct owl: SymmetricProperty, the cooperative relationship “Cooperate\_with” can be the symmetric relationship.

Fig. 4 illustrates the property of OWL-based empirical knowledge ontology. The empirical knowledge concept possesses properties “Appearance Reason” and “Status”; they are both de<sup>fi</sup>ned as the OWL construct owl:DatatypeProperty. For the rationality of logical reasoning, the minimum value of property “Appearance Reason” is limited to be 1 (by owl:minCardinality), suggesting that <sup>fi</sup>lling in one or more property values to describe appearance reason is necessary. Additionally, the maximum value of property “Status” is identi<sup>fi</sup>ed as 1 (by owl:maxCardinality) to <sup>fi</sup>ll in the value “Normal” or “Abnormal”.

## 3.2. Ontology-based reasoning rules design for single-layer empirical knowledge

According to Ronald et al. (2000) [31], the knowledge representation method and the logical rules used for reasoning must be considered in designing reasoning rules. Meanwhile, description logics can be applied to related reasoning methods and can effectively support the ontology language OWL DL as well as identify implied knowledge through ontology reasoning methods to facilitate the sharing of tacit knowledge [8,19,24,35]. Therefore, this section describes the ontology-based reasoning rules for single-layer empirical knowledge based on the OWL-based empirical knowledge ontology and related methods of knowledge reasoning, description logics, OWL DL basic axiom and constraint [6,15,21] established from

![](/api/attachments/4WKKR4FQ/fulltext/images/618a309c83cc88a9d33228d5da8d7505af10cb6ea2bf12701ac71f3b596a3c7d.jpg)  
Fig. 3. Part of OWL-based empirical knowledge ontology (empirical knowledge concept and relationship).

![](/api/attachments/4WKKR4FQ/fulltext/images/7d4997c753acf6e896b6fd4a4f1fb7c8b53c8e3250d9e0c576fa755932a05d78.jpg)  
Fig. 4. Portion of OWL-based empirical knowledge ontology (Property).

Section 3.1, as shown in Table 3. The empirical knowledge reasoning rules in Table 3 comprise four different types of know-what, knowwhy, know-how, and know-with. Their descriptions are detailed as follows with Figs. 5–8 showing the conceptual models.

## 3.3. Empirical knowledge reasoning model in the know-what layer

Relationships in the know-what layer of empirical knowledge mainly include two types of hierarchical relationship “Is\_a” and partonomy relationship “Part\_of”. According to Fig. 5, a hierarchical relationship “Is\_a” exists between empirical knowledge concepts A and B, and also the hierarchical relationship “Is\_a” between the empirical knowledge concepts B and C. Therefore, the hierarchical relationship “Is\_a” tacitly exists between the empirical knowledge concepts A and C is deduced by the reasoning rule (1) from Table 3. Moreover, the relationship between empirical knowledge concepts D and E is partonomy relationship “Part\_of”, and the relationship between the empirical knowledge concepts E and F is also partonomy relationship “Part\_of”. The implied partonomy relationship “Part\_of” between the empirical knowledge concepts D and E can be deduced through the reasoning rule (2) from Table 3. Additionally, an inversive relationship (Rule (3) from Table 3) exists between the partonomy relationship “Part\_of” and the partial relationship “Has\_part”. Meanwhile, the partonomy relationship “Part\_of” exists between the empirical knowledge concepts D and E, implying that the empirical knowledge concept D is a part of the empirical knowledge concept E. Thus, the fact that empirical knowledge concept E belongs to empirical knowledge concept D is identi<sup>fi</sup>ed through the reasoning rule of an inversive property (Rule (4) in Table 3).

## 3.4. Empirical knowledge reasoning model in the know-why layer

In the know-why layer of empirical knowledge, a causal relationship “Cause” exists between empirical knowledge concepts G and H, and a causal relationship “Cause” also exists between the empirical knowledge concepts H and I. By the reasoning rule of transitive property (Rule (5) in Table 3), the implied causal relationship “Cause” between the empirical knowledge concepts G and I is derived. Additionally, the relationship between the causal relationships “Cause” and “Caused\_by” belongs to the transitive relationship (Rule (6) in Table 3), and a causal relationship “Cause” exists between the empirical knowledge concepts H and I. This <sup>fi</sup>nding suggests that empirical knowledge concept H causes the generation of empirical knowledge concept I. According to the reasoning rule of inversive property (Rule (7) in Table 3), the fact that the empirical knowledge concept I is caused by empirical knowledge concept H is deduced. Hence, their relationship is identi<sup>fi</sup>ed as “Caused\_by”, as shown in Fig. 6.

Table 3  
Ontology-based Reasoning Rules for Single-Layer Empirical Knowledge.

<table><tr><td>Single-LayerEmpiricalKnowledgeType</td><td>Relationship</td><td>Reasoning rule</td></tr><tr><td rowspan="3">Know-WhatLayer</td><td>Is_a</td><td>(1) (?A rdfs:subClassOf ?B) ∧(?B rdfs:subClassOf ?C) ⇒ (?A rdfs:subClassOf ?C)</td></tr><tr><td>Part_of</td><td>(2) ∀D,E,F:Part-of(D,E) ∧ Part-of(E,F) ⇒</td></tr><tr><td>Has_part</td><td>Part-of(D,F)(3) Has-part ≡ Part-of $^{-1}$  (inverse)(4) ∀D,E:Part-of(D,E) ⇔ Has-part(E,D)</td></tr><tr><td rowspan="2">Know-WhyLayer</td><td>Cause</td><td>(5) (?Cause rdf:type owl:TransitiveProperty) ∧(?G ? Cause ?H) ∧ (?H ? Cause ?I) ⇒(?G ? Cause ?I)</td></tr><tr><td>Caused_by</td><td>(6) Cause ≡ Caused_by $^{-1}$  (inverse)(7) (?Cause owl:inverseOf ? Caused_by) ∧(?H ? Cause ?I) ⇒ (?I ? Caused_by ?H)</td></tr><tr><td rowspan="2">Know-HowLayer</td><td>Follow</td><td>(8) (?Follow rdf:type owl:TransitiveProperty) ∧(?J ? Follow ?K) ∧ (?K ? Follow ?L) ⇒(?J ? Follow ?L)</td></tr><tr><td>Is_followed_by</td><td>(9) Follow ≡ Is_followed_by $^{-1}$  (inverse)(10) (?Follow owl:inverseOf ? Is_followed_by) ∧(?K ? Follow ?L) ⇒ (?L ? Is_followed_by ?K)</td></tr><tr><td>Know-WithLayer</td><td>Cooperate_with</td><td>(11) (?Cooperate_with rdf:typeowl:TransitiveProperty) ∧ (?M ? Cooperate_with?N) ∧ (?N ? Cooperate_with ?O)⇒(?M ? Cooperate_with ?O)(12) (?Cooperate_with rdf:type owl:SymmetricProperty) ∧ (?N ? Cooperate_with ?O) ⇒(?O ? Cooperate_with ?N)</td></tr></table>

NOTE:  
(1) Parameters A B C… denote the concept names of empirical knowledge.  
(2) Symbol “^” represents the logical operator AND.  
(3) Symbol “⇒”means reasoning.

## 3.5. Empirical knowledge reasoning model in the know-how layer

Fig. 7 displays the conceptual model of empirical knowledge reasoning in the know-how layer. In the model, the procedural relationship “Follow” exists between the empirical knowledge concepts J and K, and the procedural relationship “Follow” also exists between the empirical knowledge concepts K and L. Therefore, the implied procedural relationship “Follow” between the empirical knowledge concepts J and L is identi<sup>fi</sup>ed based on the reasoning rule of the transitive property (Rule (8) in Table 3). Additionally, an inversive relationship (Rule (9) in Table 3) exists between the procedural relationships “Follow” and “Is\_Followed\_by” as well as a procedural relationship “Follow” exists between empirical knowledge concepts K and L, demonstrating that empirical knowledge concept L appears before empirical knowledge concept K. Through the reasoning rule of inversive property (Rule (10) in Table 3), appearance of the procedural relationship of the empirical knowledge concept K after the empirical knowledge concept L is “Is\_followed\_by” is derived.

## 3.6. Empirical knowledge reasoning model in the know-with layer

In this conceptual model of empirical knowledge in the know-with layer, a cooperative relationship “Cooperate\_with” between the empirical knowledge concepts M and N and a cooperative relationship “Cooperate\_with” between the empirical knowledge concepts N and O are existent. Via the reasoning rule of transitive property (Rule (11) in Table 3), the cooperative relationship “Cooperate\_with” between empirical knowledge concepts M and O is therefore deduced. Additionally, a cooperative relationship “Cooperate\_with” exists between empirical knowledge concepts N and O. Therefore, the fact that empirical knowledge concept O has a cooperative relationship with the empirical knowledge concept N is deduced based on the reasoning rule of synonymous relationship (Rule (12) in Table 3), as shown in Fig. 8.

3.7. Ontology-based reasoning rules design for cross-layer empirical knowledge

According to the OWL-based empirical knowledge ontology and the related methods of knowledge reasoning, description logics, and OWL DL basic axiom and constraint [14,34] established in Section 3.1, this section analyzes how the relationships among empirical knowledge in different layers are related based on the ontologybased multi-layer empirical knowledge representation model. Additionally, as well as the ontology-based reasoning rules for cross-layer empirical knowledge are designed by using ontology language OWL DL. According to Table 4, the ontology-based reasoning rules for crosslayer empirical knowledge involve three categories. They are, i.e. “know-what layer vs. know-why layer”, “know-what layer vs. know-

![](/api/attachments/4WKKR4FQ/fulltext/images/d665465efe554ca0c0a44e73353ef8174669251855d94fd4373ee12326c668c9.jpg)  
Fig. 5. Conceptual model of empirical knowledge reasoning in the Know-What Layer.

![](/api/attachments/4WKKR4FQ/fulltext/images/0079f549b076fb81d02ea8bf63571379a8dc49fe7b9c9befeec67bd76a34bb55.jpg)  
Fig. 6. Conceptual model of empirical knowledge reasoning in the Know-Why Layer.

![](/api/attachments/4WKKR4FQ/fulltext/images/1d539a07113b1dff66e29f207013bb02e568ab3228ad25acdbd3ca864fe306dd.jpg)  
Fig. 7. Conceptual model of empirical knowledge reasoning in the Know-How Layer.

![](/api/attachments/4WKKR4FQ/fulltext/images/d16300cc834574a51c46ab30839950ef2f5b90d35696b1446fac89f8a5883c9c.jpg)  
Fig. 8. Conceptual model of empirical knowledge reasoning in the Know-With Layer.

how layer”, and “know-what layer vs. know-with layer”, respectively. Each category is described as follows.

3.8. Empirical knowledge reasoning model between the know-what layer and know-why layer

Fig. 9 presents the conceptual model of empirical knowledge reasoning between the know-what layer and know-why layer. In the model, a causal relationship “Cause” exists between the empirical knowledge concepts X and Y and the partonomy relationship “Part\_of” exists between empirical knowledge concepts Y and Z.

Hence, the fact that a causal relationship “Cause” exists between the empirical knowledge concepts X and Z is derived through the reasoning rule (1) from Table 4.

3.9. Empirical knowledge reasoning model between the know-what layer and know-how layer

In the empirical knowledge reasoning between the know-what layer and know-how layer, a procedural relationship “Follow” between empirical knowledge concepts U and V and a partonomy relationship “Part\_of” between empirical knowledge concepts V and

Table 4  
Ontology-based reasoning rules for cross-layer empirical knowledge.

<table><tr><td>Cross-empirical knowledge type</td><td>Relationship</td><td>Reasoning rule</td></tr><tr><td>Know-What Layer vs. Know-Why Layer</td><td>Part_of Cause</td><td>(1) X $\subseteq$   $\exists$  Cause. Y $\land$ Y $\subseteq$   $\exists$  Part-of. Z $\Rightarrow$ X $\subseteq$   $\exists$  Cause. Z</td></tr><tr><td>Know-What Layer vs. Know-How Layer</td><td>Part_of Follow</td><td>(2) U $\subseteq$   $\exists$  Follow. V $\land$ V $\subseteq$   $\exists$  Part-of. W $\Rightarrow$ U $\subseteq$   $\exists$  Follow. W</td></tr><tr><td>Know-What Layer vs. Know-With Layer</td><td>Part_of Cooperate_with</td><td>(3) R $\subseteq$   $\exists$  Cooperate_with. S $\land$ S $\subseteq$   $\exists$  Part-of. T $\Rightarrow$ R $\subseteq$   $\exists$  Cooperate_with. T</td></tr></table>

NOTE:  
(1) Parameters X Y Z…denote the concept names of empirical knowledge.  
(2) Symbol “^” represents the logical operator AND.  
(3) Symbol “⇒” implies reasoning.  
(4) Symbol “⊆” implies a subset.  
(5) Symbol “∃” implies an existential quanti<sup>fi</sup>er.

W are existent. Consequently, the procedural relationship “Follow” between the empirical knowledge concepts U and W is found based on the reasoning rule (2) from Table 4, as shown in Fig. 10.

3.10. Empirical knowledge reasoning model between the know-what layer and know-with layer

Fig. 11 shows the conceptual model of empirical knowledge reasoning between the know-what layer and know-with layer. A cooperative relationship “Cooperate\_with” exists between the empirical knowledge concepts R and S and a partonomy relationship “Part\_of” exists between empirical knowledge concepts S and T, indicating that the cooperative relationship “Cooperate\_with” between the empirical knowledge concepts R and T is exposed according to the reasoning rule (3) from Table 4.

3.11. Reasoning algorithm design for ontology-based empirical knowledge

This section introduces the reasoning algorithm for ontologybased empirical knowledge based on the established empirical knowledge reasoning rules in Sections 3.2 and 3.3. The ontologybased empirical knowledge reasoning algorithm involves single-layer empirical knowledge reasoning and cross-layer empirical knowledge reasoning.

## 3.11.1. Reasoning algorithm for single-layer empirical knowledge

According to the ontology-based reasoning rules for single-layer empirical knowledge from Section 3.2, this subsection describes the reasoning algorithm for single-layer empirical knowledge, as shown in Fig. 12. The operational steps are described in order as follows:

Step 1. Input the single-layer empirical knowledge ontology and perform the reasoning of single-layer empirical knowledge.

Step 2. Determine whether the input empirical knowledge ontology belongs to “know-what”, and whether the relationship is ${ } ^ { \mathfrak { u } } [ s _ { - } \mathsf { a } ^ { \mathfrak { n } } ,$ , “Part\_of” or “Has\_part”. If yes, then go to Step 3 to operate the judgment of relationship value; otherwise, go to Step 4.

Step 3. If the relationship value is “Is\_a”, then execute the reasoning process for the relationship “Is\_a”. If the relationship value is “Part\_of”, then execute the reasoning process for the relationship “Part\_of”. If the relationship value is “Has\_part”, then execute the reasoning process for the relationship “Has\_part”.

Step 4. Determine whether the input empirical knowledge ontology belongs to “know-why” and whether the relationship is “Cause” or “Caused\_by”. If yes, then go to Step 5 to implement the judgment for relationship value; otherwise, go to Step 6.

Step 5. If relationship value is “Cause”, then execute the reasoning process for the relationship “Cause”. If the relationship value is “Caused\_by”, then execute the reasoning process for the relationship “Caused\_by”.

![](/api/attachments/4WKKR4FQ/fulltext/images/fc59fec69a0c549ae9dd89abbdf38322b660505b9a4475ec38d398d94952c724.jpg)  
Fig. 9. Conceptual model of empirical knowledge reasoning between the Know-What Layer and Know-Why Layer.

![](/api/attachments/4WKKR4FQ/fulltext/images/488b87e5ef308b2fd9c87aefdebed34cf94d235068b65be3b4ac0db9073cf589.jpg)  
Fig. 10. Conceptual model of empirical knowledge reasoning between the Know-What Layer and Know-How Layer.

Step 6. Determine whether the input empirical knowledge ontology belongs to “know-how” and whether the relationship is “Follow” or “Is\_followed\_by”. If yes, then go to Step 7 to proceed with the judgment for relationship value; otherwise, go to Step 8.

Step 7. If the relationship value is “Follow”, then operate the reasoning process for the relationship “Follow”. If the relationship value is “Is\_followed\_by”, then operate the reasoning process for the relationship “Is\_followed\_by”.

![](/api/attachments/4WKKR4FQ/fulltext/images/a8b7581f9738532ab993298c070acef474e1245734db4c7eb67179ea1be50fed.jpg)  
Fig. 11. Conceptual model of empirical knowledge reasoning between the Know-What Layer and Know-With Layer.

![](/api/attachments/4WKKR4FQ/fulltext/images/839402b7e6268c58fb0c47c8fca759ebfe19cd1cf5791799df1b3c5546c98d14.jpg)  
Fig. 12. Reasoning process for Single-Layer Empirical Knowledge

Step 8. Determine whether the input empirical knowledge ontology belongs to “know-with” and whether the relationship is “Cooperate\_with”. If yes, then go to Step 9 to proceed with the judgment for rule value; otherwise, end the algorithm.

Step 9. If the rule value is “Transitive”, then execute the reasoning process for the relationship “Transitive”. If the rule value is “Symmetric”, then execute the reasoning process for the relationship “Symmetric”.

In Fig. 12, the reasoning process for single-layer empirical knowledge can be represented as an algorithm written in Pseudo Code (Fig. 13).

3.11.2. Reasoning algorithm for cross-layer empirical knowledge

According to results of Section 3.3, this subsection describes the reasoning algorithm for cross-layer empirical knowledge, as shown in Fig. 14. This algorithm involves the following steps:

Step 1. Input the cross-layer empirical knowledge ontology and perform the reasoning of cross-layer empirical knowledge.

Step 2. Determine whether the input empirical knowledge covers “know-what” and “know-why” and whether the relationships are “Part\_of” and “Cause”. If yes, then go to Step 3; otherwise, go to Step 4.

Step 3. Execute the reasoning rules for cross-layer empirical knowledge “know-what layer vs. know-why layer”.

Step 4. Determine whether the input empirical knowledge covers “know-what” and “know-how” and whether the relationships are “Part\_of” and “Follow”. If yes, then go to Step 5; otherwise, go to Step 6.

Step 5. Execute the reasoning rules for cross-layer empirical knowledge “know-what layer vs. know-how layer”.

Step 6. Determine whether the input empirical knowledge covers “know-what” and “know-with”, and whether the relationships are “Part\_of” and “Cooperate\_with”. If yes, then go to Step 7; otherwise end the algorithm process.

Step 7. Execute the reasoning rules for cross-layer empirical knowledge “know-what layer vs. know-with layer”.

The reasoning process for cross-layer empirical knowledge shown in Fig. 14 can be represented as an algorithm written in Pseudo Code (Fig. 15).

## 4. Illustrative example of an enterprise's <sup>fi</sup>nancial diagnosis

Based on the proposed method of ontology-based empirical knowledge representation and reasoning, the applicability and feasibility of the proposed method are demonstrated using an illustrative example of enterprise's <sup>fi</sup>nancial diagnosis.

![](/api/attachments/4WKKR4FQ/fulltext/images/5f727d078f2c0419ee4d961f5613ae4cba25a313faa2165cfb46953ed6870a6a.jpg)  
Fig. 13. Reasoning algorithm for Single-Layer Empirical Knowledge (Pseudo Code).

## 4.1. Ontology-based multi-layer financial diagnosis empirical knowledge

This section describes a practical example of an enterprise's <sup>fi</sup>nancial diagnosis to establish the ontology-based multi-layer <sup>fi</sup>nancial diagnosis empirical knowledge, as shown in Fig. 16. The knowledge representation content for each layer is discussed as below:

(1) Know-what layer: A taxonomy relationship “Is\_a” exists between the empirical knowledge concepts Diet\_Enterprise and Enterprise\_a/Enterprise\_b, implying that the empirical knowledge concepts Enterprise\_a and Enterprise\_b are the subclasses of the empirical knowledge concept Diet\_Enterprise.

![](/api/attachments/4WKKR4FQ/fulltext/images/9a301359dfbad3f54eecaba7ff2919dca6388756052d506f9038dafbe333684e.jpg)  
Fig. 14. Reasoning process for Cross-Layer Empirical Knowledge.

Moreover, a taxonomy relationship “Is\_a” exists between the empirical knowledge concepts Company\_a and Enterprise\_b, indicating that empirical knowledge concept Company\_a is the subclass of the empirical knowledge concept Enterprise\_b. Additionally, a partonomy relationship “Part\_of” exists between the empirical knowledge concepts Enterprise\_a and Subconglomerate\_1/Sub-conglomerate\_2. This <sup>fi</sup>nding suggests that both empirical knowledge concepts Sub-conglomerate\_1 and Sub-conglomerate\_2 are parts of the empirical knowledge concept Enterprise\_a. Meanwhile, a partonomy relationship “Part\_of” exists between the empirical knowledge concepts Sub conglomerate\_2 and Subsidiary\_2/Subsidiary\_3/Subsidiary\_4/ Subsidiary\_5, implying that the empirical knowledge concepts Subsidiary\_2, Subsidiary\_3, Subsidiary\_4, and Subsidiary\_5 are all parts of the empirical knowledge concept Sub-conglomerate\_ 2.

(2) Know-why layer: A causal relationship “Cause” exists between the empirical knowledge concepts Subsidiary\_3 and Subsidiary\_ 2. Meanwhile, the empirical knowledge concept Subsidiary\_3 owns two properties “AppearanceReason” and “Status”. The

![](/api/attachments/4WKKR4FQ/fulltext/images/a56c87ca555f5b1c82e6ab58013c17e5ae5a86a08ccceabe2b81ea3a3fa677e0.jpg)  
Fig. 15. Reasoning algorithm for Cross-Layer Empirical Knowledge (Pseudo Code).

![](/api/attachments/4WKKR4FQ/fulltext/images/8c7ef98e0f56b483547381c4608858da664b39ff059a9df91d198ab28a1da03b.jpg)  
Fig. 16. Ontology-based multi-layer <sup>fi</sup>nancial diagnosis empirical knowledge representation.

former values are dishonoured cheque and cash turnover crisis, while the latter value is financial abnormal. Concerning the empirical knowledge concept Subsidiary\_2, the values of the property “AppearanceReason” are cash turnover crisis and delivery delay, while the value of the property “Status” is <sup>fi</sup>nancial abnormal. The relationships and property values from the above statement address the fact that the <sup>fi</sup>nancial abnormal situation occurs in Subsidiary 2. as attributed to the financial abnormal situation in Subsidiary\_3. Moreover, a causal relationship “Cause” exists between the empirical knowledge concepts Subsidiary\_3 and Subsidiary\_4. The values of the property “AppearanceReason” from the empirical knowledge concept

Subsidiary\_4 are cash turnover crisis and accounting tricks, while the value of the property “Status” is <sup>fi</sup>nancial abnormal. These relationships and property values imply that a <sup>fi</sup>nancial abnormal situation occurs in Subsidiary\_4, as attributed to the <sup>fi</sup>nancial abnormal situation in Subsidiary\_3”. Additionally, a causal relationship “Cause” exists between the empirical knowledge concepts Subsidiary\_4 and Subsidiary\_5. The values of the property “AppearanceReason” from Subsidiary\_5 are cash turnover crisis and accounting tricks, while the value of the property “Status” is <sup>fi</sup>nancial abnormal. Based on these relationships and property values, a <sup>fi</sup>nancial abnormal situation occurs in Subsidiary\_5, as attributed to the <sup>fi</sup>nancial abnormal situation in Subsidiary\_4”. Finally, the relationship “Caused\_by” exists between the empirical knowledge concepts Subsidiary\_6 and Subsidiary\_5, and the value of the property “Status” from Subsidiary\_6 is <sup>fi</sup>nancial abnormal. The relationship and the property value indicate that reason of the <sup>fi</sup>nancial abnormal situation in Subsidiary\_6 is attributed to Subsidiary\_5.

(3) Know-how layer: The empirical knowledge concepts in this layer contain Pro<sup>fi</sup>t\_Flow, Fund\_Flow, Financial\_Structure, and Five\_Financial\_Aspect. Each concept has one property “Action”, and its value is diagnosis. In this case, a procedural relationship “Follow” exists between the empirical knowledge concepts, which addresses a situation in which <sup>fi</sup>nancial diagnosis is proceeded with for an enterprise's <sup>fi</sup>nancial abnormal problem. The diagnosis process involves three main steps: pro<sup>fi</sup>t <sup>fl</sup>ow diagnosis, fund <sup>fl</sup>ow diagnosis, and <sup>fi</sup>nancial structure diagnosis. While the relationship “Is\_follow\_by” exists between the empirical knowledge concepts Fund\_Flow and Five\_Financial\_ Aspect, this statement expresses a situation in which the fund <sup>fl</sup>ow diagnosis must be performed before the <sup>fi</sup>ve\_<sup>fi</sup>nancial\_ aspect diagnosis in a <sup>fi</sup>nancial diagnosis process.

(4) Know-with layer: The empirical knowledge concepts in this layer include Stability, Pro<sup>fi</sup>tability, Growth, Activity, and Productivity. Their property values are all diagnosis. The cooperative relationship “Cooperate\_with” exists between the empirical knowledge concepts, explaining that these <sup>fi</sup>ve different diagnoses must be cooperated with each other.

## 4.2. OWL-based financial diagnosis empirical knowledge ontology

Based on the established ontology-based multi-layer <sup>fi</sup>nancial diagnosis empirical knowledge, this section establishes the OWLbased <sup>fi</sup>nancial diagnosis empirical knowledge ontology by using OWL constructs, as shown in Figs. 17 and 18. Meanwhile, Fig. 17 shows the part of the empirical knowledge concept and relationship of OWL-based <sup>fi</sup>nancial diagnosis empirical knowledge ontology, while Fig. 18 depicts the part of property of OWL-based <sup>fi</sup>nancial diagnosis empirical knowledge ontology.

## 4.3. Ontology-based single-layer financial diagnosis empirical knowledge reasoning

This section illustrates the ontology-based single-layer <sup>fi</sup>nancial diagnosis empirical knowledge reasoning by using the empirical knowledge ontology “know-why” as an example. For this example, the empirical knowledge ontology “know-why” is <sup>fi</sup>rst represented by using OWL DL. Subsequently, reasoning in the know-why layer of <sup>fi</sup>nancial diagnosis empirical knowledge is performed through the de<sup>fi</sup>ned ontology-based reasoning rules for single-layer empirical knowledge.

Table 5 lists the partial contents of the reasoning in the know-why layer of <sup>fi</sup>nancial diagnosis empirical knowledge before and after the executing reasoning process. Meanwhile, a causal relationship “Cause” exists between the empirical knowledge concepts Subsidiary\_ 3 and Subsidiary\_4, as well as between the empirical knowledge concepts Subsidiary\_4 and Subsidiary\_5 (Fig. 19). Thus, the causal relationship “Cause” exists between the empirical knowledge concepts Subsidiary\_3 and Subsidiary\_5 is deduced by using the reasoning rule of transitive property (Rule (1) in Table 5). Moreover, the relationship “Cause” is the inversive relationship of the relationship “Caused\_by” (Rule (2) in Table 5). Therefore, the relationship “Caused\_by” between the empirical knowledge concepts Subsidiary\_5 and Subsidiary\_4, between the empirical knowledge concepts Subsidiary\_4 and Subsidiary\_3, and between the empirical knowledge concepts Subsidiary\_5 and Subsidiary\_3 are deduced by applying the reasoning rule of inversive property (Rule (3) in Table 5).

<table><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></table>

Fig. 17. Portion of OWL-based <sup>fi</sup>nancial diagnosis empirical knowledge ontology (empirical knowledge concept and relationship).

## 4.4. Ontology-based cross-layer financial diagnosis empirical knowledge reasoning

This section demonstrates the feasibility of the proposed crosslayer empirical knowledge reasoning method by selecting the crosslayer empirical knowledge ontology “know-what layer vs. know-why layer” as an illustrative example. In this example, the ontology language OWL DL is initially adopted to represent the cross-layer <sup>fi</sup>nancial diagnosis empirical knowledge “know-what layer vs. knowwhy layer”. Next, the de<sup>fi</sup>ned ontology-based reasoning rules for cross-layer empirical knowledge in Section 3.3 are applied to the reasoning between the know-what layer and know-why layer of <sup>fi</sup>nancial diagnosis empirical knowledge.

<table><tr><td>&lt;owl:Class rdf:ID=&quot;Empirical_Knowledge_Concept&quot;&gt;</td></tr><tr><td>&lt;rdfs:subClassOf&gt;</td></tr><tr><td>&lt;owl:Restriction&gt;</td></tr><tr><td>&lt;owl:onProperty&gt;</td></tr><tr><td>&lt;owl:DatatypeProperty rdf:ID=&quot;AppearanceReason&quot;/&gt;</td></tr><tr><td>&lt;/owl:onProperty&gt;</td></tr><tr><td>&lt;owl:minCardinality rdf:datatype=&quot;http://www.w3.org/2001/XMLSchema#int&quot;</td></tr><tr><td>&gt;1&lt;/owl:minCardinality&gt;</td></tr><tr><td>&lt;/owl:Restriction&gt;</td></tr><tr><td>&lt;/rdfs:subClassOf&gt;</td></tr><tr><td>&lt;rdfs:subClassOf&gt;</td></tr><tr><td>&lt;owl:Restriction&gt;</td></tr><tr><td>&lt;owl:onProperty&gt;</td></tr><tr><td>&lt;owl:DatatypeProperty rdf:ID=&quot;Status&quot;/&gt;</td></tr><tr><td>&lt;/owl:onProperty&gt;</td></tr><tr><td>&lt;owl:maxCardinality rdf:datatype=&quot;http://www.w3.org/2001/XMLSchema#int&quot;</td></tr><tr><td>&gt;1&lt;/owl:maxCardinality&gt;</td></tr><tr><td>&lt;/owl:Restriction&gt;</td></tr><tr><td>&lt;/rdfs:subClassOf&gt;</td></tr><tr><td>&lt;rdfs:subClassOf rdf:resource=&quot;http://www.w3.org/2002/07/owl#Thing&quot;/&gt;</td></tr><tr><td>&lt;/owl:Class&gt;</td></tr><tr><td>&lt;owl:DatatypeProperty rdf:about=&quot;#Status&quot;&gt;</td></tr><tr><td>&lt;rdfs:domain rdf:resource=&quot;#Empirical_Knowledge_Concept&quot;/&gt;</td></tr><tr><td>&lt;/owl:DatatypeProperty&gt;</td></tr><tr><td>&lt;owl:DatatypeProperty rdf:about=&quot;#AppearanceReason&quot;&gt;</td></tr><tr><td>&lt;rdfs:domain rdf:resource=&quot;#Empirical_Knowledge_Concept&quot;/&gt;</td></tr><tr><td>&lt;/owl:DatatypeProperty&gt;</td></tr><tr><td>&lt;Empirical_Knowledge_Concept rdf:ID=&quot;Subsidiary_3&quot;&gt;</td></tr><tr><td>&lt;status rdf:datatype=&quot;http://www.w3.org/2001/XMLSchema#string&quot;</td></tr><tr><td>&gt;Financial Abnormal&lt;/status&gt;</td></tr><tr><td>&lt;AppearanceReason rdf:datatype=&quot;http://www.w3.org/2001/XMLSchema#string&quot;</td></tr><tr><td>&gt;Cash Turnover Crisis&lt;/AppearanceReason&gt;</td></tr><tr><td>&lt;AppearanceReason rdf:datatype=&quot;http://www.w3.org/2001/XMLSchema#string&quot;</td></tr><tr><td>&gt;Dishonoured Cheque&lt;/AppearanceReason&gt;</td></tr><tr><td>&lt;/Empirical_Knowledge_Concept&gt;</td></tr></table>

Fig. 18. Portion of OWL-based <sup>fi</sup>nancial diagnosis empirical knowledge ontology (Property).

OWL-based <sup>fi</sup>nancial diagnosis empirical knowledge reasoning contents (Know-Why Layer).

<table><tr><td rowspan="77">Financial diagnosis empirical knowledge before reasoning</td><td rowspan="26">TransitiveProperty rdf:about=&quot;#Cause&quot;&gt;rdf:domain rdf:resource=&quot;#G&quot;/&gt;rdf:type rdf:resource=&quot;http://www.w3.org/2002/07/ owl#ObjectProperty&quot;/&gt;rdf:range rdf:resource=&quot;#H&quot;/&gt;TransitiveProperty&gt;TransitiveProperty rdf:about=&quot;#Cause&quot;&gt;rdf:domain rdf:resource=&quot;#H&quot;/&gt;rdf:type rdf:resource=&quot;http://www.w3.org/2002/07/ owl#ObjectProperty&quot;/&gt;inverseOf rdf:resource=&quot;#Caused_by&quot;/&gt;rdf:range rdf:resource=&quot;#I&quot;/&gt;</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan="25">(1) (?Cause rdf:type owl:TransitiveProperty)A(?G ? Cause ?H)A(?H ? Cause ?I)⇒(?G ? Cause ?I)(2) Cause ≡ Caused_by-1(inverse)(3) (?Cause owl:inverseOf ? Caused_by)A(?H ? Cause ?I)⇒(?I ? Caused_by ?H)</td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td rowspan="25"></td></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr></tr><tr><td></td></tr></table>

OWL-based <sup>fi</sup>nancial diagnosis empirical knowledge reasoning contents between the Know-What Layer and Know-Why Layer.

<table><tr><td rowspan="26">Financial diagnosis empirical knowledge before reasoning</td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td>Reasoning rules used</td><td> $\mathrm{X} \subseteq \exists$  Cause.  $\mathrm{Y}\land \mathrm{Y} \subseteq \exists$  part-of.  $\mathrm{Z} \Rightarrow \mathrm{X} \subseteq \exists$  Cause.  $\mathrm{Z}$ </td></tr><tr><td rowspan="9">Financial diagnosis empirical knowledge after reasoning</td><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></table>

![](/api/attachments/4WKKR4FQ/fulltext/images/917a2d136574b15a86e62cb2a03ec6c80543f59a110cc2946f06a582bb791eb2.jpg)  
Fig. 19. Ontology-based <sup>fi</sup>nancial diagnosis empirical knowledge reasoning (Know-Why Layer)

![](/api/attachments/4WKKR4FQ/fulltext/images/6af908d8e7508fd16421bd6cc7c035d1849ff90ad06593372b25bff3f39f1830.jpg)  
Fig. 20. Ontology-based <sup>fi</sup>nancial diagnosis empirical knowledge reasoning between the Know-What Layer and Know-Why Layer.

Table 6 lists the partial contents of the reasoning between the knowwhat layer and know-why layer of <sup>fi</sup>nancial diagnosis empirical knowledge before and after the executing reasoning process. Meanwhile, a partonomy relationship “Part\_of” exists between the empirical knowledge concepts Financial\_Abnormal\_of\_Subsidiary\_2 and Financial\_Abnormal\_of\_Sub-conglomerate\_2, while a causal relationship “Cause” (Fig. 20) exists between the empirical knowledge concepts Financial\_Abnormal\_of\_Subsidiary\_3 and Financial\_Abnormal\_of\_ Subsidiary\_2. Therefore, a causal relationship “Cause” exists between empirical knowledge concepts Financial\_Abnormal\_of\_Subsidiary\_3 and Financial\_Abnormal\_of\_Sub-conglomerate\_2 is deduced by the reasoning rule for cross-layer empirical knowledge, as shown in Table 6.

![](/api/attachments/4WKKR4FQ/fulltext/images/18150bb8ffcc63b68b296f962ff5faeeb08786f79e208bea3db908c4c3fab841.jpg)  
Fig. 21. Mechanism implementation environment.

![](/api/attachments/4WKKR4FQ/fulltext/images/592cd43f8960ba1b6f7c4f802c2f48f112e8354f0b1473a4c818c877302f79c1.jpg)  
Fig. 22. Financial diagnosis empirical knowledge before reasoning (Know-What Layer).

## 5. Ontology-based empirical knowledge reasoning mechanism implementation

Based on the above developed method of ontology-based empirical knowledge representation and reasoning, this section uses the software Protégé 3.4 Beta to construct an ontology-based empirical knowledge reasoning mechanism. The implementation environment and results with a <sup>fi</sup>nancial diagnosis case are described in the following subsections.

## 5.1. Implementation environment

This study implements a prototype of the ontology-based empirical knowledge reasoning at the Knowledge Engineering and Management Laboratory of National Kaohsiung First University of Science and Technology. The implementation environment was as follows. Computer hardware used was an Intel Core2-2.13G PC. Software was MS Windows XP Professional, Protégé 3.4 Beta (Ontology Construction), and Pellet 1.5.1 (Ontology Inference).

Fig. 21 illustrates the mechanism implementation environment, which consists mainly of ontology construction system Protégé, ontology repository, and ontology inference engine Pellet.

## 5.2. Implementation results

Figs. 22–24 show portions of the user interfaces for the ontologybased empirical knowledge reasoning mechanism. Fig. 22 presents the screen of the know-what layer <sup>fi</sup>nancial diagnosis empirical knowledge before reasoning, while Fig. 23 presents the reasoning rules in know-what layer of <sup>fi</sup>nancial diagnosis empirical knowledge. Fig. 24 shows the screen of know-what layer <sup>fi</sup>nancial diagnosis empirical knowledge after reasoning.

## 6. Conclusions and further research

This study developed a method for ontology-based empirical knowledge representation and reasoning using ontology techniques to help knowledge requesters to retrieve empirical knowledge for their problem-solving and decision support. Therefore, the tasks involved in the development include: (i) analyzing characteristics for empirical knowledge, (ii) designing an ontology-based multi-layer empirical knowledge representation model, (iii) designing an ontologybased empirical knowledge concept schema, (iv) establishing an OWL-based empirical knowledge ontology, (v) designing reasoning rules for ontology-based empirical knowledge, (vi) developing a reasoning algorithm for ontology-based empirical knowledge, and (vii) implementing an ontology-based empirical knowledge reasoning mechanism.

![](/api/attachments/4WKKR4FQ/fulltext/images/25c7207a83b2dbf0a91d0d9125d1ae0c3e61f98d0df7febb561cc1aa464cd769.jpg)  
Fig. 23. Financial diagnosis empirical knowledge reasoning rules (Know-What Layer).

![](/api/attachments/4WKKR4FQ/fulltext/images/c0b4cd9296933623717456c287d0f88816cc4537054bf4173ade2c53d8167ded.jpg)  
Fig. 24. Financial diagnosis empirical knowledge after reasoning (Know-What Layer).

The main results and contributions of this study are as follows:

· Ontology-based empirical knowledge representation model: The proposed model is a generic one that can be applied to any knowledge-intensive work for empirical knowledge representation, such as product design knowledge, medical diagnosis knowledge, and software development knowledge.

· Ontology-based empirical knowledge reasoning method: This designed reasoning method can effectively reason empirical knowledge within the same knowledge type or between the different knowledge types for a speci<sup>fi</sup>c domain, as well as share the retrieved empirical knowledge with the knowledge requesters.

Based on the proposed model and method in this study, the following future research issues are recommended:

· Distributed empirical knowledge representation and reasoning: Given the intensely global competitive environment, management strategies highly prioritize virtual enterprises. In a virtual enterprise, the generated empirical knowledge possesses characteristics of distributed and heterogeneity. Thus, in addition to focusing on how to represent the distributed and heterogeneous empirical knowledge, future studies should as well develop a method for distributed empirical knowledge reasoning.

· Situated empirical knowledge representation and reasoning: Empirical knowledge is associated with situation property. Situated empirical knowledge can comprise basic elements such as spatial relation and temporal relation. Therefore, future studies should consider the situation property of empirical knowledge to develop a method of situated empirical knowledge representation and reasoning in order to deduce a more suitable empirical knowledge that would satisfy the requirements from a knowledge requester under certain circumstances.

## Acknowledgements

The author would like to thank the National Science Council of the Republic of China, Taiwan, for partially supporting this research under Contract No. NSC98-2221-E-327-039.

## References

[1] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: Conceptual foundations and research issues, MIS Quarterly 25 (1) (2001) 107–136.

[2] J. Andrade, J. Ares, R. García, J. Pazos, S. Rodríguez, A. Rodríguez-Patón, A. Silva, Towards a lessons learned system for critical software, Reliability Engineering and System Safety 92 (7) (2007) 902–913

[3] J.H. Bradley, R. Paul, E. Seeman, Analyzing the structure of expert knowledge, Information & Management 43 (1) (2006) 77–91.

[4] N. Bolloju, M. Khalifa, E. Turban, Integrating knowledge management into enterprise environments for the next generation decision support, Decision Support Systems 33 (2) (2002) 163–176.

[5] B. Chandrasekaran, J.R. Josephson, V.R. Benjamins, What are ontologies, and why do we need them? IEEE Intelligent Systems 14 (1) (1999) 20–26.

[6] S.K. Das, A logical reasoning with preference, Decision Support Systems 15 (1) (1995) 19–25.

[7] B.E. Dixon, J.J. McGowan, G.D. Cravens, Knowledge sharing using codi<sup>fi</sup>cation and collaboration technologies to improve health care: lessons from the public sector, Knowledge Management Research & Practice 7 (2009) 249–259.

[8] D. Ejigu, M. Scuturici, L. Brunie, An ontology-based approach to context modeling and reasoning in pervasive computing, Pervasive Computing and Communications Workshops, PerCom Workshops '07, Fifth Annual IEEE International Conference on, 2007, pp. 14–19.

[9] R.M. Grant, Prospering in dynamically-competitive environments: Organizational capability as knowledge integration, Organization Science 7 (4) (1996) 375–388

[10] T.R. Gruber, A translation approach to portable ontologies, Knowledge Acquisition 5 (2) (1993) 199–220.

[11] N. Guarino, Understanding, building and using ontologies, International Journal of Human-Computer Studies 46 (2–3) (1997) 293–310.

[12] T. Guo, D.G. Schwartz, F. Burstein, H. Linger, Codifying collaborative knowledge: using Wikipedia as a basis for automated ontology learning, Knowledge Management Research & Practice 7 (2009) 206–217.

[13] M.T. Hansen, N. Nohria, T. Tierney, What's your strategy for managing knowledge? Harvard Business Review 77 (2) (1999) 106–116.

[14] C.T. Ho, Y.M. Chen, Y.J. Chen, C.B. Wang, Developing a Distributed Knowledge Model for Knowledge Management in Collaborative Development and Implementation of an Enterprise System, Robotics and Computer Integrated Manufacturing 20 (5) (2004) 439–456

[15] I. Horrocks, P.F. Patel-Schneider, F. van Harmelen, From SHIQ and RDF to OWL: the making of a Web Ontology Language, Web Semantics: Science, Services and Agents on the World Wide Web 1 (1) (2003) 7–26.

[16] J.A. Horvath, Working with tacit knowledge, Knowledge Management Yearbook Woods Boston 2000

[17] J.Y. Hsu, Y.H. Lin, Z.Y. Wei, Competition policy for technological innovation in an era of knowledge-based economy, Knowledge-Based Systems 21 (8) (2008) 826-832

[18] B. Kamsu Foguem, T. Coudert, C. Béler, L. Geneste, Knowledge formalization in experience feedback processes: An ontology-based approach, Computers in Industry 59 (7) (2008) 694–710.

[19] E.G. Little, G.L. Rogova, Designing ontologies for higher level fusion, Information Fusion 10 (1) (2009) 70–82.

[20] C.J. Martinez, K.L. Campbell, M.D. Annable, G.A. Kiker, An object-oriented hydrologic model for humid, shallow water-table environments, Journal of Hydrology 351 (3–4) (2008) 368–381.

[21] B. Motik, U. Sattler, R. Studer, Query Answering for OWL-DL with rules, Web Semantics: Science, Services and Agents on the World Wide Web 3 (1) (2005) 41–60.

[22] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5 (1) (1994) 14–37.

[23] I. Nonaka, H. Takeuchi, The knowledge-creating company, Oxford University Press, Inc, 1995.

[24] J.Z. Pan, Description logics: Reasoning support for the semantic web, 2004.

[25] A. Paschke, M. Bichler, Knowledge representation concepts for automated SLA management, Decision Support Systems 46 (1) (2008) 187–205.

[26] P.R.O. Payne, E.A. Mendonça, S.B. Johnson, J.B. Starren, Conceptual knowledge acquisition in biomedicine: A methodological review, Journal of Biomedical Informatics 40 (5) (2007) 582–602.

[29] J. Quinn, P. Anderson, S. Finkelstein, Managing professional intellect: Making the most of the best, Harvard Business Review, 1996.

[27] M. Polanyi, Personal knowledge, University of Chicago Press, Chicago, 1958

[28] M. Polanyi, The tacit dimension, Routledge & Keegan Paul, London, 1966.

[30] J. Ronald, H.J.L. Brachman, Knowledge representation and reasoning, Morgan Kaufmann, Amsterdam, Boston, 2004.

[31] M. Ronald, From experience: Harnessing tacit knowledge to achieve breakthrough innovation, Journal of Product Innovation Management 17 (3) (2000) 179–193.

[32] S. Schulz, U. Hahn, Part-whole representation and reasoning in formal biomedical ontologies, Arti<sup>fi</sup>cial Intelligence in Medicine 34 (3) (2005) 179–200.

[33] O. Steen, Practical knowledge and its importance for software product quality, 2007.

[34] C.A. Tacla, J.P. Barthes, A multi-agent system for acquiring and sharing lessons learned, Computers in Industry 52 (1) (2003) 5–16.

[35] X.H. Wang, D.Q. Zhang, T. Gu, H.K. Pung, Ontology based context modeling and reasoning using OWL, Pervasive Computing and Communications Workshops, Proceedings of the Second IEEE Annual Conference on, 2004, pp. 18–22.

[36] R. Weber, D.W. Aha, I. Becerra-Fernandez, Intelligent lessons learned systems, Expert Systems with Applications 20 (No, 1) (2001) 17–34.

[37] R.O. Weber, D.W. Aha, Intelligent delivery of military lessons learned, Decision Support Systems 34 (3) (2003) 287–304.

[38] W.L. Xu, L. Kuhnert, K. Foster, J. Bronlund, J. Potgieter, O. Diegel, Object-oriented knowledge representation and discovery of human chewing behaviors, Engineering Applications of Artificial Intelligence 20 (7) (2007) 1000–1012

[39] M. Zack, Managing codi<sup>fi</sup>ed knowledge, Sloan Management Review (1999) 45–48

![](/api/attachments/4WKKR4FQ/fulltext/images/3044293d8fc31ef8ff37f3b4a156c5727c2857162c912126337053db38895377.jpg)  
Dr. Yuh-Jen Chen is currently an Assistant Professor of Department of Accounting and Information Systems, National Kaohsiung First University of Science and Tech nology, Taiwan, ROC. He received his Ph.D. and MS degrees in Institute of Manufacturing Information and Systems of National Cheng Kung University in 2005 and 2001 respectively, and gained his BS degree from the Department of Applied Mathematics of Chung Yuan Christian University, Taiwan, ROC, in 1999. His current research interests include Enterprise Information Systems, Decision Support Systems, Knowledge Engineering and Manage ment, and Service Science.
