---
otero_id: 1190
otero_key: "B8BNH6FW"
title: "Introducing functional classification theory to land use planning by means of decision tables"
authors: "Frank Witlox; Marc Antrop; Peter Bogaert; Philippe De Maeyer; Ben Derudder; Tijs Neutens; Veronique Van Acker; Nico Van de Weghe"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Introducing functional classi<sup>fi</sup>cation theory to land use planning by means of decision tables

Frank Witlox ⁎, Marc Antrop, Peter Bogaert, Philippe De Maeyer, Ben Derudder, Tijs Neutens, Veronique Van Acker, Nico Van de Weghe

Ghent University, Department of Geography, Krijgslaan 281 (S8), B-9000 Gent, Belgium

## a r t i c l e i n f o

Article history: Received 6 June 2007 Received in revised form 26 November 2008 Accepted 7 December 2008 Available online 10 December 2008

Keywords: Spatial planning Knowledge representation Decision tables Relational matching

## a b s t r a c t

This paper contributes to the conceptualisation and analysis of double-sided matching problems, taking the land use planning problem as an example. It does so by introducing functional classi<sup>fi</sup>cation theory at the knowledge level, the symbol level and the system level of a DSS. This theory explicitly expresses the methodological viewpoint of relational realism. At the knowledge level this implies de<sup>fi</sup>ning knowledge on the basis of matching the intension and extension of concepts. At the symbol level it deals with knowledge representation and here decision tables are advanced and formally introduced. At the system level the formalism used at the symbol level is implemented to develop a relational matching DSS

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Urban planners and decision-makers often face the problem of having to deal with complex decision situations. This complexity is mainly due to the fact that a huge number of in<sup>fl</sup>uential decision factors have to be considered and that the interactions and internal dependencies between these different factors are sometimes dif<sup>fi</sup>cult to understand. To illustrate the latter, decision variables may change in relevancy due to the presence or absence of other factors (i.e. conditional relevance), and their (un)importance may alter given the fact that certain factors have or have not been assigned particular values (i.e. conceptual interaction). The result is that internal relationships between factors are not limited to the interdependence of categorizations of factors. Apart from this categorization problem, also the quantity of the information and the issue of variable interrelatedness result in that people are no longer capable of over-viewing the complete decision problem [3,13].

In land use planning, i.e. the process of deciding where will what kind of (economic) activities best take place in space, the complexity of the decision problem is obvious. On the one hand the urban planner puts forward a number of requirements an economic activity has to meet in order for it to be able to locate at a certain location site. On the other hand, economic activities (such as companies) have certain demands that have to be met by a location site so the site can be considered suitable for setting up business. Clearly this matching of demand and supply implies linking locational requirements with company demands, and linking locational demands with company requirements. In other words the land use decision-making process involves a double-sided matching problem, and it is here that a computer-based decision support system (DSS) can be of help [15,20].

Over the years, a large number of DSS for urban planning have been developed. For a comprehensive overview, see [34]. What is however lacking is a more fundamental treatment of the issue of how DSS are able to tackle double-sided matching problems and what de<sup>fi</sup>nes the basic requirements for building such a system. This is the main topic of this paper. It aims to contribute to the conceptualisation and analysis of the issue of the double-sided matching problems, taking the land use planning problem as an example.

The paper is organised as follows. Firstly we focus on the knowledge level. We point to the fact that several theories exist that relate to de<sup>fi</sup>ning knowledge and concepts, but that not all of these theories are adequate when trying to develop a DSS that meets the above-mentioned requirements. Secondly, we turn our attention to the symbol level. Here, we focus on how to represent knowledge and concepts, and advance and formally introduce decision tables as potential representation formalism. In the third section, we focus on the system level referring to the implementation of the formalism used at the symbol level when developing a DSS. Finally, in Section 4, we summarize our main <sup>fi</sup>ndings.

## 2. The knowledge level

In conceptual modelling, a distinction is made between an objecttype and an object on the basis of the intension and extension of concepts [19,28]. The intension of a concept refers to a set of necessary and suf<sup>fi</sup>cient conditions that should be satis<sup>fi</sup>ed by an object in order that the object may be classi<sup>fi</sup>ed under the particular concept. Therefore, the intension of a concept refers to the object-type, as it sets the scene for evaluating whether an object is or is not to be considered to belong to the class covered by the concept. The extension of the concept points to a set of objects that comply with the object-type. A simple example may clarify this distinction somewhat further. Take, for instance, a concept like ‘bachelor’ (see also [4]). The intension of this concept is determined by three necessary conditions that put together are suf<sup>fi</sup>cient: ‘male’, ‘adult’, and ‘not married’. Only those persons that comply with all three conditions are considered as extensions of the concept ‘bachelor’. Persons that do not match with all three conditions cannot accurately (and also literally) be classi<sup>fi</sup>ed as extensions of the concept ‘bachelor’. For instance, a person that lacks the ‘unmarried’ condition might be termed a ‘man’, and if the ‘married’ condition is present, a ‘husband’. Turning to our problem setting of land use planning, the object-type is ‘suitable location site’ or ‘suitable economic activity’ and the objects are ‘location sites’ or ‘economic activities’. The idea is then to match objects to the object-type in the sense that constraints de<sup>fi</sup>ned by the objecttype need to be directly matched by a set of attributes de<sup>fi</sup>ning an object in order that the object can be classi<sup>fi</sup>ed as an object-type.

In the literature (see e.g., [4,6,10,22–24,32,34]), several theories have been put forward to interpret and solve this matching problem. In the classical theory ([14], cited in [10]), the matching of objects as object-types is established on a simple ‘yes’ or ‘no’ (all-or-nothing) basis, in the sense that an object either complies or does not comply with the de<sup>fi</sup>nition of the object-type. So, if we assume, for the sake of illustration, that the object-type “suitable location site” is de<sup>fi</sup>ned as a location satisfying the following four conditions: a high productivity rate (C ), a low transport cost (C ), a moderate market demand (C ), and an easy access to public utilities (C ), it implies that only when the object's characteristics correspond exactly with all the object-type's conditions that a match is established. Characteristic of the classical theory is the assumption that the set of necessary and suf<sup>fi</sup>cient conditions de<sup>fi</sup>ning the object-type is totally univocal, which automatically implies a totally unambiguous matching. If this were true, matching would be very straightforward. However, intuitively, it stands to reason that matching is far more complex than the classical theory perceives it to be. Note also that if one of the properties of the object no longer matches the corresponding condition of the objecttype, the object can no longer be classi<sup>fi</sup>ed as object-type. This problem could be solved by leaving that particular condition out of the de<sup>fi</sup>nition of the object-type. However, this is not really a valid solution. As a consequence, a number of alternative theories have been developed that assumed that matching problems result from a delineation problem in the set of constraints that de<sup>fi</sup>ne an objecttype. One of these theories is the probabilistic theory.

The probabilistic theory [25] assumes that random disturbances on an empirical level cause confusion in deriving the set of constraints that de<sup>fi</sup>ne the object-type. Therefore, it is not always possible to be absolutely certain of all conditions of the object-type. Sometimes the presence of one condition can compensate for the absence of another. This results in the existence of imprecisely de<sup>fi</sup>ned sets of necessary and suf<sup>fi</sup>cient conditions that prevent a univocal matching. In order to be able to match objects with object-types, probabilities are assigned to each condition of the object-type and an objective function is de<sup>fi</sup>ned. These probabilities re<sup>fl</sup>ect the relative signi<sup>fi</sup>cance of different attributes in the set de<sup>fi</sup>ning the object-type. Conditions that are assumed to be important are assigned a high probability, while less important conditions are allotted a relatively low probability. The ultimate matching takes place by comparing the properties of an object to the de<sup>fi</sup>nition of the object-type, and calculating the overall probabilities of the satis<sup>fi</sup>ed conditions in the objective function. If the set of satis<sup>fi</sup>ed conditions is suf<sup>fi</sup>cient to ful<sup>fi</sup>ll the objective function, the object matches the de<sup>fi</sup>nition of the object-type, and is classi<sup>fi</sup>ed accordingly. In contrast to the classical theory, the probabilistic view is still able to match objects to the de<sup>fi</sup>nition of the object-type if not all conditions are satis<sup>fi</sup>ed. Hence, the probabilistic approach assumes that conditions can compensate for one another. However, this is not always a valid hypothesis, since in many de<sup>fi</sup>nitions of object-types non-compensatory conditions are found that should be satis<sup>fi</sup>ed at any time. Consequently, de<sup>fi</sup>ning object-types according to the principles of the probabilistic approach to matching will not always result in reliable matching outcomes.

A third matching approach, which also recognizes the problem of imprecisely de<sup>fi</sup>ned sets of necessary and signi<sup>fi</sup>cant conditions specifying the object-type, is the prototypical or stereotypical theory [2]. In contrast to the classical and the probabilistic view, the prototypical theory postulates that it is impossible to de<sup>fi</sup>ne a set of conditions that all objects must satisfy to match the object-type. Instead, it assumes that an object-type is described by means of a prototype (or stereotypical example or archetype). This prototype consists of the set of necessary and suf<sup>fi</sup>cient conditions. However, since no object will satisfy all conditions, the object's degree of resemblance to the prototype will determine whether classi<sup>fi</sup>cation is possible or not. Representativeness in prototype theory is exclusively based on element-to-element similarity. In other words, the higher the similarity with the prototype, the higher the likelihood that the object is an extension of the concept. Thus, according to the prototype theory, imprecision is not caused by random disturbances, but results from the ambiguity that is inherent to categorizing the real world. Note also that the matching procedure becomes very complicated when objects present themselves in many different ways in the real world. Consequently, what is called for is yet another theory that offers a totally different explanation for the existence of imprecision in the delineation of the set of constraints that de<sup>fi</sup>ne an object-type. This theory is called the functional classification theory which aims at explicitly expressing the methodological viewpoint of relational realism [9,21,28].

The central notion of functional classi<sup>fi</sup>cation, as stated by [28], is that on a theoretical level, an object-type cannot be univocally de<sup>fi</sup>ned by means of a precise set of constraints. In this respect, the functional classi<sup>fi</sup>cation theory corresponds with the probabilistic and prototypical approaches. However, what is quite different, is the explanation given for this observed imprecision. It is assumed to have a systematic character. Therefore, it cannot be adequately dealt with either by some mathematical technique or by comparing the objects to a prototypical object-type. Thus, the problem should be solved in another way. The solution is found by consequently allowing for the systematic identi<sup>fi</sup>cation and modelling of several object-types, instead of working with one single object-type. There is no single de<sup>fi</sup>nition of an object-type because the de<sup>fi</sup>nition is context-dependent. If, in the suitable location site example, the aim is to determine whether a location is appropriate for a petrochemical industry or not, the objecttype “suitable location site for a petrochemical industry” has to be de<sup>fi</sup>ned by specifying the conditions an object (i.e. a speci<sup>fi</sup>c location) must satisfy in order to be matched with the object-type. Clearly, the context set forward determines which conditions are relevant for object-type de<sup>fi</sup>nition.

In this respect, matching is based on the “functionality” of the objects. This means that objects, although they have different sets of attributes, are assigned to distinct classes if they can ful<sup>fi</sup>ll speci<sup>fi</sup>c functions associated with these classes. As such, objects with different properties can match the same object-type. In the functional classi<sup>fi</sup>cation theory, this speci<sup>fi</sup>c characteristic is referred to as functional equivalence, or “the phenomenon that objects, possibly differing in many respects, are equivalent in achieving a nominally speci<sup>fi</sup>ed function in a certain context” [10].

Fig. 1 represents the matching process according to the functional classi<sup>fi</sup>cation theory in diagram form. In this simple example, two different object-types are de<sup>fi</sup>ned and three different objects are displayed. It can be noted that the <sup>fi</sup>rst object only matches the de<sup>fi</sup>nition of the <sup>fi</sup>rst object-type, while the third object only matches the de<sup>fi</sup>- nition of the second object-type. The only object that matches both object-types is the second object. Its properties, $\{ A _ { 1 } , A _ { 3 } , A _ { 4 } \}$ , directly match the conditions of the <sup>fi</sup>rst object-type $\{ C _ { 1 } , C _ { 3 } , C _ { 4 } \}$ , but also those of the second object-type $\{ C _ { 1 } , { \sim } C _ { 2 } , C _ { 3 } \} .$ It follows that the <sup>fi</sup>rst and second object are said to be functionally equivalent in respect to the <sup>fi</sup>rst object-type because both objects, having different properties, match the same object-type. An identical situation is found for the second and third object in respect to the second object-type.

![](/api/attachments/B8BNH6FW/fulltext/images/c609494b37c296b67072f7bb4ca1874b574e90a82e43929a9f15b5ff1714a48a.jpg)  
Fig. 1. Matching according to the functional view.

Note, as also illustrated in Fig. 1, that an object-type of a concept is modelled by means of a disjunction of conjunct sets [10]. This means that the modelling problem essentially reduces to reconstructing the set of rules that can identify a subset of functionally equivalent objects for a given context [1,36]. This process depends not only on the properties of the object but also on the characteristics of the actor re<sup>fl</sup>ected in the conditions de<sup>fi</sup>ning the object-type. It also follows that in a disjunctive relation of conjunct sets, single conditions are seldom termed strictly necessary for realizing a successful match because their absence can be compensated for by the other elements of the disjunction. To put it succinctly, within a conjunct set a particular condition may be deemed necessary for achieving a certain match, but the conjunct set itself to which the particular condition belongs, is replaceable by other conjunct sets. As such, any element or condition of a conjunct set is considered as an Insuf<sup>fi</sup>cient but Necessary (or Non-redundant) part of that conjunct set which is Unnecessary but Suf<sup>fi</sup>cient for the result. Abbreviated, this is termed an INUS-condition. The INUS-conditionality is derived from the theory of causes and conditions as developed by Mackie [11,12], and later discussed and amended by Tacq [26] and Denise [7]. In the functional approach, INUSconditionality implies that a single empirical property of an object cannot by itself be considered as a necessary and suf<sup>fi</sup>cient condition of such a function. It is only within a certain context that the object's characteristics may be considered as contributing to such a function. Consequently, “no characteristic of a location or region can, on its own account, generate a suitable environment for locating economic activities. Whether or not such a characteristic can contribute to site suitability depends on the spatial production requirement of the economic activity for which it must be assessed” [21]. As such, the individual locational properties (i.e. the location factors) represent the necessary but insuf<sup>fi</sup>cient conditions for site suitability, while the totality of all individual locational properties represents a suf<sup>fi</sup>cient but unnecessary combination as it is one out of many combinations of location factors that may generate a suitable location site.

Note further that three mechanisms are responsible for the fact that a matching result is attainable by quite different strategies [1,10,33,35]. The <sup>fi</sup>rst mechanism, which is called variation limited to goal-constructed categories, refers to the situation that objects may have different attribute values, but that this variation is limited to, or falls within, a goal-constructed category. In other words, functional equivalence occurs when different attribute levels fall within the same context-dependent attribute category. The second aspect leading to functional equivalence is the mechanism by which the relevance of an object's attribute may be conditional upon another attribute of that object. As such, a conditional relevance in the attributes is caused. A third important mechanism of functional equivalence is the fact that categorizations of attributes of objects in<sup>fl</sup>uence each other. Functional equivalence may occur if the relevant categorization of the attribute levels depends on other attributes. This form of dependency between attributes is referred to as conceptual interaction.

A <sup>fi</sup>nal point is that the matching process is not restricted to a onesided approach. The functional classi<sup>fi</sup>cation of objects as object-types may be realized either by matching the object's characteristics to the imposed context conditions or the context's characteristics to the imposed object conditions. As such, a double-sided matching is advocated.

Having discussed the basic mechanisms underlying functional equivalence, it should be clear that an appropriate representation formalism or methodology should be advanced that complies with these principles. More speci<sup>fi</sup>cally, the modelling formalism used should allow the model designer to include conditional relevance (attributes being dependent upon other attributes) and conceptual interaction (the use of <sup>fl</sup>exible attribute categorizations). Given its speci<sup>fi</sup>c advantages, we would like to advance the decision table approach for this purpose.

## 3. The symbol level: decision table approach

## 3.1. Decision table formalism

A decision table (DT) is informally de<sup>fi</sup>ned by Verhelst $\left[ 3 0 \right] \mathsf { a s } ^ { \ast } ( \ldots )$ a table representing the exhaustive set of mutual exclusive conditional expressions within a pre-de<sup>fi</sup>ned problem area”. Each DT contains four parts. The upper left part of the table lists the condition subjects $C S _ { i }$ for $i { = } 1 , { \ldots } , { } c$ (with c being the number of conditions) which are the criteria for the decision-making process. The universe of discourse $C D _ { i }$ for each condition i is the set of all possible values that the condition can attain. The condition-state set for each condition i consists of the possible states of the condition:

$$
\mathrm{CT} _ {i} = \left\{S _ {i 1}, S _ {i 2}, \dots , S _ {i t _ {i}} \right\}\tag{1}
$$

where $t _ { i }$ is the number of categories for the ith condition and $S _ { i j }$ determines a subset of $C D _ { i } .$ . The condition space of a DT is the Cartesian product of the condition state sets $C T _ { i } ,$ as follows:

$$
\begin{array}{r l} \text {SPACE} (C) = \text {CT} _ {1} \times \text {CT} _ {2} \times \dots \times \text {CT} _ {c} & \text {for c > 1} \\ = \text {CT} _ {1} & \text {for c = 1} \end{array}\tag{2}
$$

An element of SPACE(C) is an ordered c-tuple and is called a condition entry (CE). The set of CE's which are present in the DT de<sup>fi</sup>nes the domain of the DT and is denoted as DOM(DT).

The bottom left part contains the action subjects ${ \mathsf { A } } { \mathsf { S } } _ { i }$ for $i { = } 1 , { \ldots } , a$ (with a being the number of actions), which represent the terms in which decision outcomes are expressed. For each action i, the action state set $\mathsf { A T } _ { i }$ contains the possible values action i can attain:

$$
\mathrm{AT} _ {i} = \left\{m _ {i 1}, m _ {i 2}, \dots , m _ {i t _ {i}} \right\}\tag{3}
$$

The action space of a DT is de<sup>fi</sup>ned as the Cartesian product of the action state sets:

$$
\begin{array}{r l} \text {SPACE} (A) = \text {AT} _ {1} \times \text {AT} _ {2} \times \ldots \times \text {AT} _ {a} & \text {for a > 1} \\ = \text {AT} _ {1} & \text {for a = 1} \end{array}\tag{4}
$$

An element of SPACE(A) is an ordered a-tuple called an action entry (AE).

As Vanthienen [29] has shown, a DTcan be de<sup>fi</sup>ned in different ways as a relation, a function or a matrix. The matrix de<sup>fi</sup>nition suits the present purpose and can be written as follows. Let n be the number of columns and c the number of conditions. Then, the condition part of a DT can be de<sup>fi</sup>ned in matrix notation as:

$$
D = \left(d _ {i j}\right), \quad i = 1, \dots , c \text {   and   } j = 1, \dots , n\tag{5}
$$

where $d _ { i j } { = } \cup _ { x \in S _ { i j } } X$

The action part can be written as:

$$
E = \left(e _ {i j}\right), \quad i = 1, \dots , a \text { and } j = 1, \dots , n\tag{6}
$$

where $e _ { i j } { = } m _ { i j }$

A DT de<sup>fi</sup>nes the relation between condition space and action space. Formally:

$$
\mathrm{DT} = \left(d t _ {i j}\right) = \binom{D}{E}\tag{7}
$$

where,

$$
\begin{array}{l} d t _ {i j} = d _ {i j}, \quad \text { for } i = 1, \ldots , c \text { and } j = 1, \ldots , n \\ \qquad = e _ {(i - c) j}, \text { for } i = c + 1, \ldots , c + a \text { and } j = 1, \ldots , n. \end{array}
$$

The three key-properties of DTs are consistency, exclusivity and completeness. The properties can be formally de<sup>fi</sup>ned as follows. Let $D ^ { j }$ denote the jth column of D and $E ^ { j }$ the jth column of E. Then, consistency can be de<sup>fi</sup>ned as:

$$
\text { a   DT   is   consistent } \Leftrightarrow \forall (D ^ {j}, D ^ {k}): \text { if } \forall (d _ {i j}, d _ {i k}): d _ {i j} \cap d _ {i k} \neq \varnothing \text { then } E ^ {j} = E ^ {k} \tag {8}
$$

where $i = 1 , . . . ,$ c and $j , k { = } 1 , { \ldots } , n .$ . The DT is consistent, because there is no intersecting pair of columns in the DT of which the action parts differ.

The property of exclusivity can be de<sup>fi</sup>ned as:

$$
\text { a   DT   is   exclusive } \Leftrightarrow \forall (D ^ {j}, D ^ {k}): \text { if   } j \neq k \text {   then   } \exists (d _ {i j}, d _ {i k}): d _ {i j} \cap d _ {i k} = \varnothing\tag{9}
$$

where $i { = } 1 , { \ldots } , c$ and $j , k { = } 1 , { \ldots } , n$ . A DT meets the exclusivity constraint because for every pair of columns there is at least one condition of which the condition states exclude each other.

Finally, a DT is complete if it meets the following two constraints:

$$
\operatorname{DOM} (D T) = \operatorname{SPACE} (C) \text {   and   } \forall E ^ {j}: \exists e _ {i j} \in A T _ {i}\tag{10}
$$

The DT is complete since every CE is included in the condition part of the DT and in every column at least one action is speci<sup>fi</sup>ed.

Compared to other representation formalisms (e.g. decision tree, decision plan nets), the current practice of using DTs offers several advantages. A DT provides a schematic view of the inference process of a decision-making procedure. It also offers a more compact visual presentation, and is more ef<sup>fi</sup>cient and effective than the decision tree with respect to checking the information input on completeness, correctness, and consistency. Moreover, a DT is easier to manipulate and satis<sup>fi</sup>es a number of logical constraints.

## 3.2. An example

To bring out some of the properties of using the decision table formalism, a brief example is worked out in the <sup>fi</sup>eld of land use planning. Although, in the present context, we are chie<sup>fl</sup>y interested in the general structure of the DT rather than in its particular contents, it is useful to point out that the example relates to a concept that is part of the Dutch national location policy aimed at matching location and mobility characteristics of companies. The basic idea is to reduce caruse by locating companies with a high potential for public and private transport use (e.g. labour or visitor intensive <sup>fi</sup>rms) near public transport facilities or private transport nodes. To this end, Verroen [31] has de<sup>fi</sup>ned three mobility pro<sup>fi</sup>les re<sup>fl</sup>ecting a company's mobility needs and three corresponding accessibility pro<sup>fi</sup>les re<sup>fl</sup>ecting the accessibility characteristics of a location. Given these pro<sup>fi</sup>les, it is possible to indicate which combinations of <sup>fi</sup>rm-types and location-types are most suitable to achieve a maximum transport reduction. The example DT depicted in Table 1 (split into two parts to <sup>fi</sup>t the size of a page) represents the de<sup>fi</sup>nition of a B-accessibility pro<sup>fi</sup>le. It corresponds to locations that are relatively well accessible by both private and public transport.

In Table 1, it can be noted that the condition set consists of six conditions and the action set of two actions. Each condition is further speci<sup>fi</sup>ed by means of a (varying) number of condition states. The interaction of the different condition states determines whether a potential location site meets (action $A _ { 1 } )$ or does not meet (action $A _ { 2 } )$ the B-accessibility pro<sup>fi</sup>le. Conditions and actions are directly matched with one another by means of a set of decision rules. As such, each conditional statement explicitly links an element of the condition space with an element of the action space. In total, 13 such decision rules have been speci<sup>fi</sup>ed, corresponding to the total number of columns in the table. Note that the speci<sup>fi</sup>ed decision rules are mutually exclusive and jointly form an exhaustive set. This property is referred to by Cohn and Hazarika [5] as JEPD (Jointly Exhaustive and Pairwise Disjoint). As such, the example DT ful<sup>fi</sup>ls the JEPD-property. Exhaustiveness implies that all alternative condition states together cover the whole domain of the condition. Hence, no single distance value falls outside the speci<sup>fi</sup>ed condition states. Exclusiveness implies that all alternative condition states exclude each other. Hence, no single distance can at the same time fall in more than one speci<sup>fi</sup>ed condition state. As a result of the exhaustivity and exclusivity property, processing a particular case (i.e. the characteristics of a potential location site) through the table results in at least one matching rule (exhaustiveness) and no more than one matching rule (exclusiveness). As such, there exists one and only one match between a combination of condition states and a single action state.

Decision table de<sup>fi</sup>ning a B-accessibility pro<sup>fi</sup>le

<table><tr><td>1. C1 Area type</td><td colspan="7">Large city district</td><td colspan="2">Other city district</td></tr><tr><td>2. C2 Dist. railway station</td><td colspan="7">X=&lt;500 or 500800</td><td colspan="2">X=&lt;500</td></tr><tr><td>3. C3 Dist. public transport mode</td><td colspan="3">-</td><td colspan="4">-</td><td colspan="2">-</td></tr><tr><td>4. C4 Dist. city centre</td><td colspan="3">-</td><td colspan="4">-</td><td colspan="2">-</td></tr><tr><td>5. C5 Dist. exit national highway</td><td colspan="3">-</td><td>X=&lt;2000</td><td colspan="3">20002500</td><td colspan="2">X=&lt;2000 or 2000</td></tr><tr><td>6. C6 Dist. regional highway</td><td colspan="3">-</td><td>-</td><td>X=&lt;500</td><td colspan="2">X&gt;500</td><td colspan="2">-</td></tr><tr><td>1. A1 Site meets ‘B’ profile</td><td colspan="3">X</td><td>x</td><td>x</td><td colspan="2">.</td><td colspan="2">x</td></tr><tr><td>2. A2 Site does not meet ‘B’ –prof</td><td colspan="3">.</td><td>.</td><td>.</td><td colspan="2">x</td><td colspan="2">.</td></tr><tr><td></td><td colspan="3">1</td><td>2</td><td>3</td><td colspan="2">4</td><td colspan="2">5</td></tr><tr><td>1. C1 Area type</td><td colspan="8">Other city district</td><td>Out of city district</td></tr><tr><td>2. C2 Dist. railway station</td><td colspan="2">X=&lt;500</td><td colspan="6">500800</td><td>-</td></tr><tr><td>3. C3 Dist. public transport mode</td><td colspan="2">-</td><td colspan="5">X=&lt;500</td><td>X&gt;500</td><td>-</td></tr><tr><td>4. C4 Dist. city centre</td><td colspan="2">-</td><td colspan="4">X=&lt;2500</td><td>X&gt;2500</td><td>-</td><td>-</td></tr><tr><td>5. C5 Dist. exit national highway</td><td colspan="2">X&gt;2500</td><td colspan="4">X=&lt;2000 or 2000X&gt;2500--</td><td>-</td><td>-</td><td>-</td></tr><tr><td>6. C6 Dist. regional highway</td><td>X=&lt;500</td><td>X&gt;500</td><td colspan="2">-</td><td>X=&lt;500</td><td>X&gt;500</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1. A1 Site meets ‘B’-profile</td><td>X</td><td>.</td><td colspan="2">x</td><td>x</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>2. A2 Site does not meet ‘B’ –prof</td><td>.</td><td>x</td><td colspan="2">.</td><td>.</td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td></td><td>6</td><td>7</td><td colspan="2">8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td></tr></table>

Table 1 also illustrates a number of interesting relational or functional modelling features which have been introduced and explained in the previous section. First, the set of decision rules used in a DT corresponds to a disjunctive relation of conjunct sets. Therefore, DTs satisfy the necessary conditions for reconstructing rules de<sup>fi</sup>ning functional equivalence. Functional equivalence appears when different condition states induce the same action state. In other words, in the above example, there are many different ways in which a location site can satisfy the de<sup>fi</sup>nition of a B-accessibility pro<sup>fi</sup>le: e.g. rules $R _ { 1 } ,$ $R _ { 2 } , R _ { 3 } , R _ { 5 } , R _ { 6 } , R _ { 8 } ,$ and $R _ { 9 } .$ Similar, although rules $R _ { 4 } , R _ { 7 } , R _ { 1 0 } , R _ { 1 1 } ,$ and $R _ { 1 2 }$ combine different condition states, they are termed functionally equivalent in achieving action $A _ { 2 }$ (i.e. location site does not meet the B-pro<sup>fi</sup>le). Note also that in such a disjunctive relation of conjunct rules, single condition states are termed INUS-conditions. Arentze et al. [1] have noted that identical rule sets to construct a DT can also be reconstructed using lower order formalisms such as predicate logic. However, the key question is whether the formalism used also systematic accounts for conditional relevance of conditions and conceptual interactions between conditions. Both properties underlie functional equivalence.

The property of conditional relevance is illustrated in that condition $C _ { 3 } ,$ representing the distance to public transport node, is only relevant if condition $C _ { 1 } ,$ representing the area type, is equal to “other city district” (i.e. condition state $C S _ { 1 2 } )$ and if condition $C _ { 2 } ,$ re<sup>fl</sup>ecting the distance from railway station in the urban area, is equal to “XN500” (i.e. condition state $C S _ { 2 4 } ) .$ . In all other cases, condition $C _ { 3 }$ is considered not relevant. The characteristic of conceptual interaction between conditions is exempli<sup>fi</sup>ed by conditions $C _ { 2 }$ and $C _ { 5 } .$ . It can be noted in Table 1 that, in both cases, the categorization of these conditions is subject to the resulting condition states of higher speci<sup>fi</sup>ed conditions. For instance, the appropriate categorization of condition $C _ { 2 }$ is equal to “X≤800” and ${ } ^ { \mathfrak { a } } X { > } 8 0 0 ^ { \mathfrak { n } } \ { \mathrm { ~ i f ~ } } \ C _ { 1 }$ is equal to “large city district”, and $" X { \le } 5 0 0 "$ and ${ } ^ { \mathfrak { u } } X { > } 5 0 0 ^ { \mathfrak { w } } \ \mathrm { i f } \ C _ { 1 }$ is equal to “other city district”. Given that both the relevance and categorization of conditions in the DT is dependent on the outcome of higher speci<sup>fi</sup>ed condition states, it implies that DTs can systematically allow for conditional relevance and conceptual interaction. Hence, the effects of the internal relatedness of conditions is acknowledged in the approach.

Another point which can be illustrated using the example DT is the fact that multiple (instead of only dichotomous) evaluation categories can be used, and that both compensatory and non-compensatory rules are allowed. In respect to the latter point, it can be noted that compensatory relationships follow from the existence of functional equivalence. In other words, it is only possible to specify functional equivalent decision rules on the basis of compensatory relationships between condition states. An example of a non-compensatory decision rule is rule $R _ { 1 3 } .$ It states that if condition $C _ { 1 } ,$ re<sup>fl</sup>ecting the area type, is equal to “out of city district”, the location site is automatically eliminated from the set of sites meeting the B-accessibility pro<sup>fi</sup>le. Note that, in this case, all other choice in<sup>fl</sup>uential conditions are assigned the “don't care” entry (denoted by ‘-’).

## 4. The system level

One decision table does not make up a DSS. Hence, at the system level, we focus on implementing the formalism used at the symbol level (in our case, a DT) to develop a DSS. In others words, what is called for is a set of hierarchical or nested DTs that can function as DSS. A generic example of such an interacting system using DTs is shown in Table 2.

Although it appears from Table 2 that only one DT is used to represent the entire matching process, it should be noted that, in fact, an entire hierarchical system of DTs is implied. This is because both location factors are further speci<sup>fi</sup>ed and matched using a system of subDTs on a lower DT-level. The call for a subDT routine is indicated in the table by the symbol “^” in front of the condition's name. Note also that the use of additional subDTs within a subDT to further specify a subdimension or to refer to yet another decision problem is allowed, whereby it should be borne in mind that the actions of the (condition) subDTs always point to the condition states of a table at a higher level.

The tabular representation of the decision situation is thus characterized by the separation between conditions and actions, on one hand, and between subjects and conditional expressions (states), on the other. Every table column (decision column) indicates which actions should (or should not) be executed for a speci<sup>fi</sup>c combination of condition states. Hence, the matching results are represented as disjunct sets of conjoint conditional statements which can be thought of as a group of so-called if-then rules: i.e. “if this condition state (or premise or antecedent) occurs, then some action state (or attribute evaluation, or conclusion, or consequence) will (or should) follow”. In the case of the interactive match evaluation (Table 2), a generic decision rule may be written as follows:

A generic relational matching approaches by means of a DT

<table><tr><td colspan="2">Matching result</td></tr><tr><td> $C_1$  ^Location factor 1</td><td>Condition states  $C_1$ </td></tr><tr><td> $C_2$  ^Location factor 2</td><td>Condition states  $C_2$ </td></tr><tr><td> $A_1$  Match evaluation</td><td>Action states  $A_1$ </td></tr></table>

IF condition state of $C _ { 1 }$ (referring to location factor 1) AND condition state of $C _ { 2 }$ (referring to location factor 2)

THEN action state of $A _ { 1 }$ (re<sup>fl</sup>ecting a matching outcome or rule).

Viewed from a decision table approach, a match evaluation or rule is presented as one of the action states of a decision table, or as the “then”-part of a decision or production rule. This approach implies that the supplied matching outcomes by the respondents are interpreted as evaluations of how different attributes (referring either to the actor, the object, or the interaction of actor and object) interact with one another and lead to different sets of locational matching outcomes. Consequently, these sets of matching rules function as representative sets of decision rules that are applied by an industry when faced with the selection of a location site.

Note also that, as a result of the speci<sup>fi</sup>cation of different condition states, functionally equivalent matching results can be obtained (i.e. decision rules that lead to identical action states or matching evaluations). It can also be seen that, whereas in the DT presented in Table 2 only two conditions (i.e. C and $C _ { 2 } )$ interact with each other to determine the <sup>fi</sup>nal match evaluation, it is evident that the use of more conditions is allowed. The consequence, however, is that, with each supplementary condition speci<sup>fi</sup>cation in the DT, the matching outcomes are additionally being in<sup>fl</sup>uenced, since more conditional interactions in the condition space of the DT may take place.

## 5. Discussion and conclusions

This paper contributed to the theoretical debate on the conceptualisation and development of a decision support system for land use planning. Land use planning involves deciding where will what kind of (economic) activities best take place in space. It is a complex decision problem having speci<sup>fi</sup>c characteristics, making it quite different from other non-spatial decision problems. One such particular property is the issue of being able to deal with a double-sided matching. This process refers to the fact that spatial requirements on the one hand have to be matched with company demands on the other, but that the opposite relationship (i.e. linking spatial demands with company requirements) should hold as well. In most DSS developed so far this dual matching characteristic is lacking; hence, our interest in de<sup>fi</sup>ning the basic requirements for building such a system. To this end, we analysed the consequences of allowing for a relational matching approach on three different layers: the knowledge level, the symbol level and the system level. At the knowledge level the functional classi<sup>fi</sup>cation theory seems most promising. This theory expresses the methodological viewpoint of relational pragmatism, and is able to account for conditional relevance and conceptual interaction between decision variables, two prominent mechanisms underlying functional equivalence. Moreover, a doublesided matching approach is a typical characteristic.

At the symbol level decision tables are used as representational formalism. The decision table formalism was chosen to represent the choice heuristics because it has some advantageous modelling properties. Firstly, because they are exclusive, consistent and complete, DTs return for every possible case within the domain a determined response. This behaviour is not guaranteed by traditional decision trees or by production systems and represents a clear advantage of DTs for any modelling purpose. Secondly, the DT provides a suitable formalism for representing various types of interactions between variables, such as conditional relevance and conceptual interaction. Within each column, a partition of a condition can be de<sup>fi</sup>ned independently of other columns. Conditional relevance captures this notion that particular requirements are relevant only for particular condition states. Conceptual interaction implies that different locational pro<sup>fi</sup>les may be equally suitable for site selection.

Finally, at the system level, a <sup>fi</sup>rst indication was given of how a hierarchical or nested decision table structure can function as relational DSS. The construction of such a system involves the development of a procedure of knowledge acquisition and knowledge representation by means of a set of interacting decision tables. The DSS can be used in a straightforward manner. Locational requirements can be activated, or changed during consultation sessions, and the system will identify those locations that satisfy these requirements. Alternatively, when new locations are added, or the characteristics of the existing locations change, the system may be used to identity the type of <sup>fi</sup>rms whose locational requirements are consistent with the new locational pro<sup>fi</sup>le. These types of consultations may thus support the urban planning process in a variety of ways. This type of support is not unique, but the use of the decision table formalism for this particular application is.

Equally important to note is that the system can be easily extended. All it takes is to make a number of elementary changes to the decision table structure in order to incorporate additional relevant location and organisational characteristics. Spatial and temporal transferability of the system are no real problem. As such, the current approach distinguishes itself from, and can be considered an alternative to, the more traditional spatial modelling approaches that use random utility modelling (e.g., [8]), structural equation modelling (e.g., [27]), or timespace modelling (e.g., [16–18]).

## Acknowledgements

The corresponding author would like to thank Wout Dullaert (UA-ITMMA) for his useful remarks made on an earlier version of this paper. Also we acknowledge the very useful suggestions made by the three anonymous referees that have added to the overall quality of the paper. Obviously, all remaining errors are ours.

## References

[1] T.A. Arentze, G.L. Lucardie, et al., A functional decision table based approach to multi-attribute decision making. 3rd International Conference on Retailing and Consumer Services Science. Telfs/Buchen Austria 1996

[2] R.J. Brachman, I lied about the trees. Or, defaults and de<sup>fi</sup>nitions in knowledge representation, AI Magazine 6 (3) (1985) 80–93.

[3] J.J. Castro-Schez, L. Jimenez, et al., Using fuzzy repertory table-based technique for decision support, Decision Support Systems 39 (3) (2005) 293–307.

[4] B. Cohen, G.L. Murphy, Models of concepts, Cognitive Science 8 (1) (1984) 27–58.

[5] A.G. Cohn, S.M. Hazarika, Qualitative spatial representation and reasoning: an overview, Fundamenta Informaticae 46 (1-2) (2001) 1–29.

[6] J. De Gelder, G.L. Lucardie, Criteria for the selection of conceptual modelling languages for knowledge based systems, Proceedings of the 3rd Design & Decision Support Systems in Architecture & Urban Planning Conference. Part one: Architecture Proceedings - DDSS, Spa, Eindhoven University of Technology, Faculty of Architecture, Building and Planning 1996

[7] T.C. Denise, On the nature of inus conditionality, Analysis 44 (2) (1984) 49–52.

[8] H. Hammadou, I. Thomas, et al., How to incorporate the spatial dimension in destination choice models: the case of Antwerp, Transportation Planning and Technology 31 (2) (2008) 153–181.

[9] P.H.J. Hendriks, De Relationele De<sup>fi</sup>nitie Van Begrippen, Geogra<sup>fi</sup>sch en Planologisch Instituut, Nijmegen, 1986 (PhD thesis).

[10] G.L. Lucardie, Functional Object-Types as a Foundation of Complex Knowledge-Based Systems, TNO Bouw, Rijswijk, 1994 (PhD thesis).

[11] J.L. Mackie, Causes and conditions, American Philosophical Quarterly 2 (4) (1965) 245–264.

[12] J.L. Mackie, The Cement of the Universe: A Study of Causation, Oxford University Press, Oxford, 1974.

[13] D. Martens, L. Bruynseels, et al., Predicting going concern opinion with data mining, Decision Support Systems 45 (4) (2008) 765–777.

[14] J. Martin, J. Odell, Object-Oriented Analysis and Design, Prentice Hall, Englewood Cliffs, 1992.

[15] E. Natividade-Jesus, J. Coutinho-Rodrigues, et al., A multicriteria decision support system for housing evaluation, Decision Support Systems 43 (3) (2007) 779–790.

[16] T. Neutens, F. Witlox, et al., Space-time opportunities for multiple agents: a constraintbased approach, International Journal of Geographical Information Science 21 (10) (2007) 1061–1076.

[17] T. Neutens, T. Schwanen, et al., My space or your space? Towards a measure of joint accessibility Computers Environment and Urban Systems 32 (5) (2008) 331-342

[18] T. Neutens, N. Van de Weghe, et al., A three-dimensional network-based space-time prism Journal of Geographical Systems 10 (1) (2008) 89–107

Email: frank.witlox@ugent.be

[19] C.K. Ogden, I.A. Richards, The Meaning of Meaning, Harcourt Brace Jovanovitch, New York, 1946.

[20] B. Recio, J. Ibanez, et al., A decision support system for analysing the impact of water restriction policies, Decision Support Systems 39 (3) (2005) 385–402.

[21] F. Reitsma, Functional Classi<sup>fi</sup>cation of Space. Aspects of Site Suitability Assessment in a Decision Support Environment, International Institute for Applied Systems Analysis (IIASA), Laxenburg, 1990 (PhD thesis).

[22] E.E. Smith, D.L. Medin, Categories and Concepts, Harvard University Press, Cambridge, MA, 1981.

[23] M. Smithson, Fuzzy Set Analysis for Behavioral and Social Sciences, Springer Verlag, New York, 1987.

[24] J.F. Sowa, Conceptual Structures: Information Processing in Mind and Machine, Addison-Wesley Publishing Company, Reading, MA, 1984.

[25] R.E. Stepp, R.S. Michalski, Conceptual clustering of structured objects: a goal-oriented approach, Arti<sup>fi</sup>cial Intelligence 28 (1986) 43–69.

[26] J. Tacq, Causaliteit in Sociologisch Onderzoek, Sociologische Gids 24 (1) (1982) 4–39.

[27] V. Van Acker, F. Witlox, et al., The effects of the land use system on travel behaviour: towards a new research approach, Transportation Planning and Technology 30 (4) (2007) 331–353.

[28] A.G.M. Van der Smagt, De<sup>fi</sup>niëren En Relateren in Sociaal Wetenschappelijk Onderzoek, Geogra<sup>fi</sup>sch Instituut Nijmegen, Nijmegen, 1985 (PhD thesis).

[29] J. Vanthienen, Quality by design: using decision tables in business rules, Business Rules Journal 5 (2) (2004) 1–7.

[30] M. Verhelst, De Praktijk Van Beslissingstabellen, Kluwer, Deventer and Antwerp,1980

[31] E.J. Verroen, Lokatiebeleid Voor Bedrijven En Voorzieningen: Het Concept Van Mobiliteitspro<sup>fi</sup>elen En Bereikbaarheidspro<sup>fi</sup>elen Nader Bekeken, Tijdschrift Vervoerswetenschap 27 (1) (1991) 115–139.

[32] F. Witlox, Towards a relational view on industrial location theory, Tijdschrift voor Economische en Sociale Geogra<sup>fi</sup>e 91 (2) (2000) 135–146.

[33] F. Witlox, Matisse: a relational expert system for industrial site selection, Expert Systems with Applications 24 (1) (2003) 133–144.

[34] F. Witlox, Expert systems in land-use planning: an overview, Expert Systems with Applications 29 (2) (2005) 437–445.

[35] F. Witlox, H.J.P. Timmermans, Representing locational requirements using conventional decision tables: theory and illustration, Geographical & Environmental Modelling 6 (1) (2002) 59–79.

[36] F. Witlox, H. Tindemans, The application of rough sets analysis in activity-based modelling. opportunities and constraints, Expert Systems with Applications 27 (4) (2004)585-592

![](/api/attachments/B8BNH6FW/fulltext/images/5f792684659db210f25d2d9493c6c6c43d0ad51fb2b729d571736e14e6eab84c.jpg)

MA Applied Economics, 1989, University of Antwerp MA Maritime Sciences, 1990, University of Antwerp

Ph.D. Urban Planning, 1998, Eindhoven University of Technology

Frank Witlox holds a Ph.D. in Urban Planning (Eindhoven University of Technology) a Master's Degree in Applied Economics and a Master's Degree in Maritime Sciences (both University of Antwerp). Currently, he is Professor of Economic Geography at the Department of Geography of the Ghent University. He teaches among others Population and Urban Geography; Economic Geography; Location Theory; Transport, Logistics and Space; Spatial Modelling Techniques; Geography of the World Economy; Maritime Economic Geography; Current Issues in Social and Economic Geography. He is also a senior researcher at the Department of Transport and Regional Economics of the University of Antwerp, a visiting professor at ITMMA (Institute of Transport and Maritime Management Antwerp), and an Associate Director of GaWC (Globalization and World Cities, Loughborough University). His research focuses on transport economics and geography, economic geography, spatial modelling techniques, (city) logistics, and world cities and globalization.

## Career

– 01/10/2008–present

Professor of Economic Geography, Ghent University

– 01/09/2007–present

– 01/10/2006–30/09/2008

Associate Director 'Globalization and World Cities'— Study Group & Network, Loughborough University (UK) Associate Professor of Economic Geography, Ghent University

– 01/10/2002–present

Part time visiting Professor Hinterland Transportation, University of Antwerp-Institute of Transport and Maritime Management Antwerp

Assistant Professor of Economic Geography, Ghent University

– 01/10/2000–30/09/2002 Part time visiting Assistant Professor of Economics, University of Antwerp

– 01/10/1998–30/09/2008 Part time Assistant Professor of Transport Policy, Hasselt University

– 01/10/1990–30/09/2000 Teaching and doctoral assistant, University of Antwerp – 01/04/1990–30/09/1990 Research assistant, University of Antwerp

## Research unit

SEG — Social and economic geography (Department of Geography):

http://www.geoweb.ugent.be/research/econ.asp

## Most important academic services

2008–present Chairman of the Educational Commission Geography-Geomathics

2000–2008 Secretary of the Examination Commission Geography/Land Surveying

2005–present Chairman ‘Vervoerslogistieke Werkdagen’ (Den Haag)

2005–present Vice Chairman Benelux Interuniversity Assocation of Transport Economists (Brussels)

2006–present Member of Faculty Counci

2007–present Member of the Steering Committee ‘Vlaanderen in Actie’

## Present editorial boards

Tijdschrift Vervoerwetenschap, De Aardrijkskunde, Business Logistics, Aerlines Magazine, Educational Research and Reviews, Belgian Journal of Geography, Journal of Mobile Communication

## Research projects and expertise

As project manager or consultant he conducted research for the European Commission, the Belgian Government (DWTC, Kabinet Minister van Mobiliteit en Vervoer; OFO; Federaal Wetenschapsbeleid), the Flemish Government (PBO, FWO-V, IWT, Steunpunt Ruimte en Wonen, Steunpunt Verkeersveiligheid, MORA, Studiedienst van de Vlaamse Regering), city councils, professional associations (FEBETRA, SAV), consultancy <sup>fi</sup>rms (Studiegroep Omgeving, Resource Analysis, GEDAS, WES, IBM Business Consulting Services, BCI, RebelGroup), universities and institutions (SFO, BOF-UA, BOF-UGent, Vlaams Instituut voor de Logistiek, VITO), and private companies (Touring Wegenhulp, VTB-VAB, PaperPak, SGS Belgium) in the <sup>fi</sup>eld economic geography, location theory, transport economics and geography, urban planning, logistics, and spatial modelling techniques.

## Awards

– Laureate of the “Van Eesteren-Fluck & Van Lohuizen Stichting” (The Hague) (1993–1994)

– Laureate Prix Fondation Louis Davin (2e période biennale 1995-1996), Académie Royale des sciences, des lettres & des beaux-arts De Belgique (Classe des Lettres — Ministère de la Communauté française) (1995–1996)

– Winner of the “Two-year research award of the Joint Research Board of the University of Antwerp (category Applied Economic Sciences and Political Sciences)” (1999).

## Conferences

A large number of international congresses with active participation (AAG, AirNeth, ASRDLF, ATRS, BELGIUM/FUZZY 2, BMI, CUPUM, CVS, DDSS, ECTQG, EFDAN, EIRASS, ERSA, ETC, EUFIT, EUGEO, EURESCO, EURO, EUROFUSE, FLAGIS, FRANCORO, FUZZY, FUZZY/IEEE, ICLSP, ICOR, IESM, IGU, INSNA, ISA, NECTAR, NAFIPS, ORBEL, RmR, SeBGIS, SSE, TRB, UPE, VLW, VWEC, and WCTR).

## Doctoral dissertations

Supervisor of 10 doctoral dissertations in progress.

## Publications: http://anet.ua.ac.be/acadbib/ua/200

• 31 articles cited in the Web-of-Science: Regional Studies; Computers, Environment and Urban Systems; Tijdschrift voor Economische en Sociale Geogra<sup>fi</sup>e; Expert Systems with Applications; Mitteilungen der Österreichischen Geographischen Gesellschaft; Transportation Planning and Technology; Journal of Air Transport Management; IEEE Intelligent Systems; Urban Studies; Transport Reviews; Childhood; International Journal of Pattern Recognition and Arti<sup>fi</sup>cial Intelligence; Lecture Notes in Computer Science; Lecture Notes in Arti<sup>fi</sup>cial Intelligence; Urban Geography; International Journal of Geographical Information Science; Eurasian Geography and Economics; Journal of Transport Geography; Journal of Geographical Systems; International Migration; Journal of Urban Technology; Decision Support Systems; International Journal of Production Economic

• 40 articles in peer reviewed journals not in W-o-S: Netherlands Journal of Housing and the Built Environment; Belgium Journal of Operations Research, Statistics and Computer Science: Geographical and Environmental Modelling: Journal of Retailing and Consumer Services; Electronic Journal of Geography and Mathematics; The Land; Brussels Economic Review; Belgian Journal of Geography; Journal of World Transport Policy and Practice; Children, Youth and Environments; Tijdschrift Vervoerswetenschap; The Journal of European Economic History; Flux: International Scienti<sup>fi</sup> Quarterly on Networks and Territories; Revue d'Economie Régionale et Urbaine; Agora; European Journal of Transport Infrastructure and Research

• 37 articles in other (local) journals

• 29 proceedings contributions

• 6 books, 19 edited books, and 89 chapters in books.
