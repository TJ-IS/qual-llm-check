---
otero_id: 7834
otero_key: "RE4JVE82"
title: "Identifying generic routings for product families based on text mining and tree matching"
authors: "Jianxin (Roger) Jiao; Lianfeng (Linda) Zhang; Shaligram Pokharel; Zhen He"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.01.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Identifying generic routings for product families based on text mining and tree matching

Jianxin (Roger) Jiao <sup>a,⁎</sup>, Lianfeng (Linda) Zhang <sup>a</sup>, Shaligram Pokharel <sup>a</sup>, Zhen He <sup>b</sup>

<sup>a</sup> School of Mechanical and Aerospace Engineering, Nanyang Technological University, Nanyang Avenue 50, 639798, Singapore <sup>b</sup> School of Management, Tianjin University, China

Received 8 March 2006; received in revised form 3 January 2007; accepted 22 January 2007 Available online 27 January 2007

## Abstract

Product customization leads to an exponentially increased number of product and process variants, which exaggerates the difficulties in building up customization capabilities for make-to-order production systems. It is imperative for companies to configure existing operations routings by exploiting similarities among product and process families so as to take advantage of repetitions. Corresponding to a product family, a process family comprises a set of similar production processes that share certain common operations routings (namely, generic routings). In addition to leveraging the costs of delivering variety, exploiting process families around generic routings can reduce development risks by reusing existing facilities and proven process elements. This paper applies data mining techniques to identify generic routings from large amount of production information and process data available in a firm's legacy systems. Generic routing identification encompasses three consecutive stages, including routing similarity measure, routing clustering and routing unification. Text mining and tree matching techniques are applied to cope with the textual and structural types of data underlying generic routings. A case study of mass customization production of vibration motors for mobile phones is reported to illustrate the feasibility and potential of generic routing identification. © 2007 Elsevier B V All rights reserved

Keywords: Mass customization; Data mining; Product family; Process configuration; Operations routing; Product variety; Text mining; Tree matching; Generic representation

## 1. Introduction

Due to diverse customer needs and product proliferation, manufacturers are confronted with difficulties in dealing with frequent design changes and recurrent process variations, which augments complexity of product and production structures [37]. Developing multiple products based on product families sharing a common platform has been well recognized as a successful approach in many industries [30]. Current practice in developing product families only encompasses the design domain — dealing with the transformation of diverse customer needs to functional requirements and subsequently the fulfillment of these requirements through a variety of design parameters [32]. It seldom, if not at all, explicitly considers the input from the backend of product realization, viz., production processes [7,23]. While seeking technical solutions is the major concern in design, it is at the production stage that product costs are actually committed and product quality and lead times are highlighted per se [17].

The direct consequence of product customization on production is evidenced by an exponentially increased number of process variants, such as diverse machines, tools, fixtures, setups, cycle times, and labors [37]. Process variety introduces significant constraints to production planning and control, preventing make-toorder systems from building up customization capabilities [21]. Consequently, companies are eagerly interested in configuring existing operations routings by exploiting similarities among product and process families so as to take advantage of repetitions [31]. Corresponding to a product family, a process family comprises a set of similar production processes that share certain common operations routings (referred to as generic routings). In addition to leveraging the costs of delivering variety, exploiting process families around generic routings can reduce development risks by reusing proven elements in a firm's activities [25].

Generic routings entail the conceptual structure and overall logical organization of producing a family of products, thus providing a generic umbrella to capture and utilize commonality, within which each new product fulfillment is instantiated and extends so as to anchor production planning to a common process structure [24]. The rationale of such generic routings lies in not only unburdening the knowledge base from keeping variant forms of the same solution, but also in modeling the production of a class of products that can widely variegate the operations and process sequences in accordance with specific design changes within a coherent framework [25]. Therefore, identification of generic routings becomes an important task for fulfilling product families in mass customization production [11,20].

Considering the fact that large amount of production information and process data are available in a firm's legacy systems, reusing knowledge from historical data suggests itself as a natural technique to facilitate the handling of process variety and tradeoffs between design changes and process variations. Towards the end, this paper proposes to apply data mining techniques to solve the generic routing identification problem. Data mining has been well recognized for decision support by efficient knowledge discovery of previously unknown and potentially useful patterns of information from past data [9]. More specifically, text mining and tree matching techniques are applied to cope with the textual and structural types of data underlying generic routings.

## 2. Related work

The historical practice of classifying or grouping individual parts into families originates from the concept of group technology (GT). The practical acceptance of GT, however, has remained limited due to the overwhelming effort involved in developing an effective coding scheme to incorporate numerous part features and manufacturing information [29]. Martinez et al. [24] propose the concept of a meta-product for modern production environments that are organized in product families with multiple options and variants, along with many choices of assembly sequences. The GT is used to allow the classification of manufacturing sequences as tree-like manufacturing plans.

Focusing on reducing subassembly proliferation and the cost of offering product variety, Gupta and Krishnan [12] propose a methodology for designing product family-based assembly sequences. While attempting to create common assembly processes, their method neglects the link between product and process families. De Lit et al. [10] put forward the integrated design of product families and the corresponding assembly systems. Their focus is on new product families with little attention to the reuse of existing assembly plans. He and Kusiak [15] discuss the design of assembly systems for modular products. An assembly line is divided into the basic and variant subassembly lines, such that the basic subassembly line is used for common and basic operations, whereas the variant ones for variant operations. Shierholt [31] presents the concept of process configuration that combines the principles of product configuration and process planning. This work, however, takes the availability of process family structures for granted and does not shed light on the construction of such process families from historical process data.

Aiming at integrated production data modeling, Hastings and Yeh [14] propose a concept of bill of manufacture (BOMfr). The BOMfr combines the routing with traditional bills of materials (BOMs) to provide material requirement data for each operation scheduled, resulting in a time-phased material requirement plan derived from a feasible schedule. Blackburn [5] demonstrates how combining routings and BOMs in one document can support just-in-time manufacturing in a traditional MRP-implemented production environment. Chang et al. [6] discuss the planning of a manufacturing BOM, which involves compressing the multi-level engineering BOM into a three-level manufacturing BOM. Bertrand et al. [4] propose a type of hierarchical pseudo BOMs and discuss their applications to customer order acceptance and optimal material replenishment.

To deal with product variety, van Veen [36] proposes the concept of a generic BOM (GBOM). A GBOM empowers the specification of product variants by means of an item and a set description at any level in a multilevel BOM rather than only for top-level items. Its strength lies in the reduction of variant differences to the variants of the generic items at the lowest level of the GBOM. Jiao et al. [19] put forward a generic bill-ofmaterials-and-operations for the purpose of unifying BOMs and routings to accommodate a large number of product and process variants. Tatsiopoulos [33] discusses the consequences of unifying BOMs and routings on the basic functions of production planning and control. The MRP planning logic based on the unification of BOMs and routings avoids the intricacy of the optimized production technology system and is more readily accepted by manufacturing personnel.

To support variant design activities, Romanowsk and Nagi [28] propose an approach to forming GBOM based on text mining. Romanowski and Nagi [29] study the structural similarity of BOMs using tree matching techniques. With focus on BOM data, their work hardly takes into account process data explicitly. Chen [8] applies association rule induction to find the associations among machines from the process database, based on which the configurations of machine cells are determined. Agard and Kusiak [1] apply text mining and association rule mining to the design of product families. The focus is on the mapping between functional requirements and design solutions. Agard and Kusiak [2] develop association rules for selecting subassemblies based on the analysis of prior orders received from the customers. While focusing on mapping relationships from requirements to solutions, their work does not address the precedence issue of production processes.

## 3. Problem description

In general, an operations routing, noted as ROU, describes a specific manufacturing process for producing a particular product. It comprises a sequence of operations, in the form of a tree-like precedence graph, to represent a production process [24]. A generic routing, noted as GROU, describes the common process structure (operations and sequences) inherent in a set of similar ROU variants, $\mathcal { Q } { = } \left\{ \mathrm { R O U } _ { 1 } , . . . , \mathrm { R O U } _ { P } \right\}$ , for producing a product family, $\mathrm { P F } = \{ P d _ { 1 } , . . . , P d _ { P } \}$

Definition 1. A generic routing is defined as a tuple: ${ \mathrm { G R O U } } = \langle A , \ \succ \rangle$ , where the precedence relation $\succ$ describes the ordering of pairs of operations from the set $A { = } \{ O _ { 1 } , ~ O _ { 2 } { , } { . } { . } { . } , ~ O _ { N } \}$ , and $\mathrm { O } _ { i \mid i = 1 , . . . , N }$ denotes an individual operation class, may it be a type of machining or assembly operations.

Definition 2. The precedence relation ≻ means sequence of execution between two operations and is defined such that a transitive closure of ≻ is irreflexive and $( ( O , X ) \in \succ ) \land ( ( O , Y ) \in \succ ) \Rightarrow X = Y ,$ where $O , X$ and $Y \in A .$ . This means, with Λ, the ≻ forms trees (i.e., precedence graphs).

For example, in Fig. 1, an ROU can be regarded as an instance of the class definition of a GROU, i.e., $\scriptstyle \mathrm { R O U  G R O U = } \langle A , \succ \rangle$ , where the set of operations Λ consists of a few machining and assembly operations, i.e., Λ= {M1, M2, M3, A1, A2, A3, A4}. With the addition of precedence relations, this ROU can thus be defined as: ROU = {M1 ≻ A2, M2 ≻ A2, A2 ≻ A1, $\mathrm { M } 3 \succ \mathrm { A } 3 , \mathrm { A } 4 \succ \mathrm { A } 3 , \mathrm { A } 3 \succ \mathrm { A } 1 \}$

Definition 3. Associated with each operation, $O \in A ,$ , is an operation description such that, $\bar { \psi _ { O } } = \langle \varPhi _ { O } ^ { M } , \varPhi _ { O } ^ { P } , R _ { O } \rangle$ , where $\varPhi _ { O } ^ { M } , \varPhi _ { O } ^ { P }$ and $R _ { O }$ are called the material, product and resource classes of operation $O ,$ respectively.

The material flow of each operation is distinguished by component classes. A component class may be an end product, a subassembly, an intermediate part or raw material type. A material class of an operation is a set of component classes. It refers to the types of input materials that will be transformed to their parent class by the operation. A product class of an operation is also one of component classes, but denotes one type of products that will be produced by the operation. Usually an operation produces only one type of products whilst it may require multiple types of materials.

While $\varPhi _ { O } ^ { M }$ and $\mathbf { \varPhi } _ { O } ^ { P }$ constitute the material flow through operation $O ,$ , a resource class, $R _ { O } ,$ characterizes the types of manufacturing resources required by the operation in order to produce $\varPhi _ { O } ^ { P }$ . A resource class of an operation, $O \in A ,$ is defined as a triplet: $R _ { O } = \langle W _ { O } .$ $T _ { O } , S _ { O } \rangle$ , where $W _ { O } , T _ { O }$ and $S _ { O }$ stand for the workcenter, cycle time and setup classes that are consumed by the operation, respectively. A workcenter class denotes the type of machines or work stations to be used for an operation. The cycle time class of an operation suggests variation of the cycle time of an operation under different production conditions. A setup class represents various types of tooling and/or fixture related to an operation. A setup class can be described by a tooling or fixture class, or both of them.

![](/api/attachments/RE4JVE82/fulltext/images/b112f1d0f56f162c0d6e7bc8361fbcbb5239f8036972b366c174c9eb901ffabb.jpg)  
Fig. 1. An ROU represented as a partial order.

Fig. 2 illustrates the class definitions and their interrelationships within the context of a GROU. The definitions of component and operation classes enable inheritance among component and operations classes $( \mathrm { i . e . }$ the generic components and operations) and facilitate hierarchical composition among the instances of component and operation classes (i.e., the specific component and operation variants). The class-member relationships between generic components or operations and their variants constitute a generic variety representation in mass customization production [20].

When an assembly operation takes place, it is common that each time only two material components are assembled together. Hence, an ROU should be represented as a labeled binary tree, in which the maximal number of child nodes for each parent node is 2. An ROU tree contains two types of process information — operations details and sequences. While details of an operation such as the product, materials, and manufacturing facilities are embedded in the nodes of the representation tree, the operations precedence (i.e., the order of operations execution) is exhibited by the tree structure.

Two types of nodes are involved in an ROU representation tree: leaf node (noted as l-node) and intermediate node (noted as i-node). Each l-node represents a machining or assembly operation that consumes at least one primitive component (e.g., raw materials and purchased parts) to produce a compound component (e.g., subassemblies) required by downstream operations. Each i-node indicates an assembly operation that produces a subassembly or end product. The materials of an i-node are all compound components, i.e., the subassemblies or intermediate parts produced from prior operations (lnodes or other i-nodes). For example in Fig. 1, operations M1, M2, M3 and A4 are l-nodes, whilst operations A1, A2 and A3 are i-nodes.

The mining of GROUs from existing ROUs involves two types of data: (1) textual data associated with the nodes describing characteristics of individual operations, and (2) structural data associated with the arcs depicting precedence relationships among operations. To solve this unique data mining problem, this research develops a systematic methodology by integrating the text mining and tree matching techniques. It includes three stages: (1) ROU similarity measure, (2) ROU clustering, and (3) ROU unification.

Given a set of routings, $\mathcal { Q } { = \{ \mathrm { R O U } _ { 1 } , . . . , \mathrm { R O U } _ { P } \} }$ , the similarity, $S _ { r s } ,$ between two routings, ROU and $\mathrm { R O U } _ { s } ,$ is derived based on pairwise comparisons of $P$ individual routings. In accordance with the textual and structural data associated with each routing, $S _ { r s }$ comprise two respective components: (1) node content similarity, $S _ { r s } ^ { \mathrm { N C } }$ , and (2) tree structure similarity, $S _ { r s } ^ { \mathrm { T S } }$

## 4. Application case

A case study is carried out in an electronics company producing mass customized vibration motors for mobile phones. The proposed framework has been tested using production data of one vibration motor family containing 30 product models. Seemingly not a complicated product, vibration motors involve diverse customer needs related to mobile phones. The design and production of vibration motors are typically custom built, resulting in an exponentially increased number of product and process variety. To fulfill diverse design changes, the operations routings of these 30 product models vary from one another while bearing certain similarity in either operations characteristics or process sequences.

![](/api/attachments/RE4JVE82/fulltext/images/28db15a79cf9f184d99650d6601cd0ccc49b1e84b19b3e60cc536d105e55a730.jpg)  
Fig. 2. Operations and component classes associated with a GROU.

![](/api/attachments/RE4JVE82/fulltext/images/e0652f596a8ad099b6e7d7f363d06e4f05e59ecd8ae38bd8579645da668da7ec.jpg)  
Fig. 3. Vibration motor structure.

As shown in Fig. 3, the component parts of a vibration motor includes “rubber holder” (rh), “weight” (wt), “frame” (fm), “bracket a” (ba), “bracket b” (bb), “terminal” (tl), “magnet” (mt), “magnet housing” (mh), “coil” (cl), “shaft” (st), “commutator” (ct), “tape” (tp), and “washer” (ws). For each component type, there are a number of variants catering for specific mobile phone requirements. Fig. 4 shows the routings for producing two different product models. In each routing tree, the nodes represent specific operations (machining or assembly). The label of each node indicates the ID of the operation concerned. For example, $^ { \mathrm { { * } } } \mathrm { { F } } m \mathrm { { A } } 2 ^ { \mathrm { { * } } }$ represents a particular assembly operation for producing the “frame assembly”, and “StM3” denotes a specific variant of shaft machining operation.

## 5. Node content similarity measure

The contents of an ROU are embodied in the nodes of the representation tree. While two ROUs may be similar in their tree structures (operations sequences), they may be discerned by diverse node contents (operations characteristics). Node content similarity measures the degree of approximation of two routings in terms of their operations descriptions. To cope with such textual data, the text mining technique is employed, which performs sentence semantic analysis [3].

For a given set of routings, there are a number of operation types (nodes), $\{ O _ { j } \} _ { N } ,$ from which each individual routing is constituted. Some routings may not assume all these operations; that is, they may comprise a subset of $\{ O _ { j } \} _ { N } .$

Corresponding to $P$ number of routings, each operation, $O _ { j } \in \{ O _ { j } \} _ { N } ,$ assume a maximal number of P specific variants, $\{ O _ { j k } ^ { * } \} _ { N \times P }$ . Let $S _ { r s } ^ { O _ { j } }$ be the similarity measure of two operations variants, $O _ { j r } ^ { * }$ and $O _ { j s } ^ { * }$ , ∀r, $s { = } 1 , { \ldots } P$ and $r \neq s ,$ corresponding two routings, ROU and ${ \mathrm { R O U } } _ { s } ,$ respectively. The node content similarity between these two routings is thus given as the sum of their operations similarity measures, as the following:

![](/api/attachments/RE4JVE82/fulltext/images/94b1f880c64e328c67aa3efe1656895b80f01065a7c1fdaaffbc9c8e6c56a1eb.jpg)  
Fig. 4. Two ROU variants for producing vibration motors.

$$
S _ {r s} ^ {N C} = \sum_ {j = 1} ^ {N} S _ {r s} ^ {O _ {j}}.\tag{1}
$$

As defined in Section 3, each operation description includes three aspects: materials, $\{ \varPhi _ { O _ { i } } ^ { M } \}$ , the product, $\{ \varPhi _ { O _ { i } } ^ { P } \}$ , and resources, $\{ R _ { O _ { i } } \}$ }. Accordingly, the operation similarity measure, $S _ { r s } ^ { O _ { j } }$ , consists of three elements, namely material similarity, $S _ { r s } ^ { M _ { j } }$ , product similarity, ${ \bf \nabla } { \cal S } _ { r s } ^ { P _ { j } } ,$ and resource similarity, $S _ { r s } ^ { R _ { j } }$ . Therefore, the operation similarity measure is given as the following:

$$
S _ {r s} ^ {O _ {j}} = S _ {r s} ^ {M _ {j}} + S _ {r s} ^ {P _ {j}} + S _ {r s} ^ {R _ {j}}.\tag{2}
$$

## 5.1. Material similarity

The basic construct of an operation description is shown in Fig. 5. The materials of an operation are a set of components, which may be a type of raw materials, intermediate parts, and/or subassemblies, i.e., $\varPhi _ { O _ { j } } ^ { M } =$ $\{ { \bf C o } _ { j k } ^ { M } | \forall k { = } 1 , . . . , K _ { j } \}$ . For a labeled binary tree, there are always two material components, i.e., $K _ { j } { = } 2$ . Therefore, material similarity of two operation variants, $O _ { j r } ^ { * }$ and $O _ { j s } ^ { * } ,$ , is calculated based on all their material components. Since some material components may be more important than others for an operation, a weighted sum of individual material component similarity measures should be used, i.e.,

$$
S _ {r s} ^ {M _ {j}} = \sum_ {k = 1} ^ {K} \left(w _ {j k} ^ {M} S _ {r s} ^ {\mathrm{Co} _ {j k} ^ {M}}\right),\tag{3}
$$

where $S _ { r s } ^ { \mathrm { C o } _ { j k } ^ { M } }$ refers to the component similarity measure between two component variants, $\mathrm { C o } _ { j k r } ^ { M * }$ and $\mathrm { C o } _ { j k s } ^ { M * }$ and $\textstyle \sum _ { k = 1 } ^ { k _ { j } } w _ { j k } ^ { M } = 1$ indicate the relative importance of $\{ \mathbf { C o } _ { j k } ^ { M } \} _ { K _ { j } } ^ { \cdots }$ <sup>¼</sup>in regard to $O _ { j } .$ . Component similarity indicates how similar two components are and to what extent they can be used as an alternative to the other. In practice, the weights are determined based on domain knowledge. Some structured methods, e.g., the analytical hierarchy process, can be employed to improve the decision making as well.

![](/api/attachments/RE4JVE82/fulltext/images/8c086b78154cc630d9d5989ca2008160cd95ee63ee8020021d8c4600fa3786a8.jpg)  
Fig. 5. Master component description for $\mathrm { a \ ^ { 6 6 } b a ^ { 7 } }$ variant.

For an l-node of an ROU representation tree, the corresponding operation takes at least one primitive component as input materials. If an operation is an i-node, its material components are all compound components that are produced from prior operations. Accordingly, the material similarity measure of two component variants, $\mathrm { C o } _ { j k r } ^ { M * }$ and $\mathrm { C o } _ { j k s } ^ { M * }$ , depends on two cases: whether or not component $\dot { \mathrm { C o } _ { j k } ^ { M } }$ is a primitive or compound component.

## 5.2. Similarity measure for primitive components

Text mining begins with the preparation of data files. Descriptions of all nodes are extracted from P number of ROU representation trees and are organized according to their corresponding operations. All component descriptions of the nodes are further sorted by primitive and compound components, which are saved separately in two text files. One contains the descriptions of all primitive components. The other documents the contents of all compound components. Similarity measure for primitive components proceeds as follows.

## 5.2.1. Encode semantics

The primitive component data file must be organized in proper formats for text mining to work on. A component is generally depicted by some characteristics – more specifically a list of attribute values with respect to some descriptive fields. The basic attribute field is the name or ID of the component type. Fig. 5 shows an example of attribute descriptions for a specific bracket variant, called BA. In the figure, four attribute fields are used to describe a bracket component type, including “name/ID”, “shape”, “color”, and “weight”. Different bracket variants assume different values of these attribute fields.

Two types of attributes can be distinguished: nominal and numerical. While a nominal attribute value is in the form of a symbolic text, values of numerical attributes are numbers. In practice, a nominal attribute value itself is meaningful enough for identifying a unique record, $\mathrm { e . g . }$ ., “square shape”. However, this is not the case for numerical attributes. A specific numerical value alone cannot suggest which attribute field it pertains to. For example, “10 mm” can indicate an instance of “length” or “width”. Therefore, rather than by listing single values, numerical attributes are described using attribute-value pairs, for example, “weight 0.08 $\mathrm { g } ^ { \dag }$ in Fig. 5.

## 5.2.2. Extract keywords

A parser is used to scan the text file for primitive components. The result is a list of extracted significant words or phrases. The keywords are generated as separated records in three forms. Single words and word combinations constitute phrases, representing the values of nominal attributes. Word–number pairs are related to numerical attribute fields.

## 5.2.3. Derive occurrence frequencies

All extracted keywords are cataloged according to their corresponding attribute fields. The occurrence of each attribute is counted by the actual values assumed. Assume a total number of Q attributes, $\{ a _ { q } ^ { k } | \forall q { = } 1 , . . . , Q \}$ , are used to describe component $\mathrm { C o } _ { j k } ^ { M } { \in \{ \mathrm { C o } _ { j k } ^ { \bar { M } } \} } _ { K _ { i } } .$ . Dividing the number of occurrence by the total number of records scanned from the text file, $\{ a _ { q i } ^ { k ^ { * } } | \ \forall i { = } 1 , . . . , P \}$ , the occurrence frequency of each attribute is determined, as below:

$$
f _ {q} ^ {k} = \frac {c _ {q} ^ {k}}{P},\tag{4}
$$

where $f _ { q } ^ { k }$ denotes the occurrence frequency of the qth attribute of the kth component, $a _ { q } ^ { k } , \ \bar { c } _ { q } ^ { k }$ is the count of active instances of $a _ { q } ^ { k } ,$ and $P$ is the total number of records contained in the text file, which equals to the total number of routing instances. The occurrence frequencies explicitly suggest how often the attributes are used to characterize individual components of the same type.

## 5.2.4. Prioritize attribute fields

More frequently an attribute is used to describe specific components, more similar of these components are, in the sense that they exhibit this attribute more than others. Therefore, the relative importance of attributes in terms of occurrence frequencies should be introduced to model their relevance to the similarity measure. This coincides with the common practice that some criteria play more important roles than others in discerning similar things. The relative importance of these attributes is indicated by their weights, i.e.,

$$
w _ {q} ^ {k} = \frac {f _ {q} ^ {k}}{\sum_ {q = 1} ^ {Q} f _ {q} ^ {k}}\tag{5}
$$

where $w _ { q } ^ { k }$ denotes the weight of attribute $a _ { q } ^ { k } ,$ , and $\textstyle \sum _ { q = 1 } ^ { Q } w _ { q } ^ { k ^ { \prime } } = 1$

## 5.2.5. Determine scales for nominal values

To compare nominal values, a semantic scale is necessary in assessing the corresponding attribute type. Usually a number between 0 and 1 is assigned for a specific nominal value, whereby 0 represents no information content and 1 indicates the maximal amount of information content. For example, the semantic scale for attribute “color” may be established by assigning 0.2,

0.3, 0.4 and 0.6 for “yellow”, “green” “red” and “blue”, respectively. Usually such scales are determined a priori based on domain knowledge. If no domain experts are available, then simply use 1 for exactly the same nominal values and 0 for different ones, regardless of their proximity. With quantification of nominal attributes, both nominal and numerical values can be processed in the same manner, despite of their origins.

## 5.2.6. Compare attributes for their similarity

For an attribute, $a _ { q } ^ { k } \in \{ a _ { q } ^ { k } \} _ { Q } ,$ the similarity of its instances is determined by comparing their difference (i.e., dissimilarity) in attribute values, i.e.,

$$
S _ {r s} ^ {a _ {q} ^ {k}} = 1 - \frac {| a _ {q r} ^ {k ^ {*}} - a _ {q s} ^ {k ^ {*}} |}{\max \left\{a _ {q i} ^ {k ^ {*}} | \forall i = 1 , \dots , P \right\} - \min \left\{a _ {q i} ^ {k ^ {*}} | \forall i = 1 , \dots , P \right\}},\tag{6}
$$

where $S _ { r s } ^ { a _ { q } ^ { k } } \in [ 0 , 1 ]$ denotes the similarity of two attribute values, $\bar { a } _ { q r } ^ { k ^ { * } } , \bar { a } _ { q s } ^ { k ^ { * } } \bar { \in } \{ a _ { q i } ^ { k ^ { * } } \} _ { P }$

## 5.2.7. Calculate similarity degree

The similarity of two primitive component variants, $S _ { r s } ^ { \mathbf { C o } _ { j k } ^ { M } }$ , is calculated as a weighted sum of similarity measures of all their attributes, i.e.,

$$
S _ {r s} ^ {\mathrm{Co} _ {j k} ^ {M}} = \sum_ {q = 1} ^ {Q} \left(w _ {q} ^ {k} S _ {r s} ^ {a _ {q} ^ {k}}\right),\tag{7}
$$

where $0 \leq S _ { r s } ^ { \mathrm { C o } _ { j k } ^ { M } } \leq 1$

## 5.2.8. Construct component similarity matrices

Repeat steps (6)–(7) for all the instances of this component type recorded in the data file. Then a $P \times P$ matrix, $[ S _ { r s } ^ { \mathbf { C o } _ { j k } ^ { M } } ] _ { P \times P } ,$ , is constructed to present pairwise similarity measures for this primitive component type. Enumerating all the primitive components, a number of such $P \times P$ matrices, $\{ [ S _ { r s } ^ { \mathrm { C o } _ { j k } ^ { M } } ] _ { P \times P } | k { = } 1 , { \ldots } , K ^ { \mathrm { P r i } } \}$ , are constructed, in accordance with a total number of $K ^ { \mathrm { P r i } }$ primitive component types contained in the data file.

## 5.3. Similarity measure for compound components

Each l-node operation, $O _ { j } ,$ , enacts a subtree for producing a compound component, ${ \mathrm { C o } } _ { j } ^ { P } ,$ from primitive components, $\{ \mathbf { C o } _ { j k } ^ { M } \} _ { K _ { i } } .$ Romanowski and Nagi [28] demonstrate that, when structural differences mean less than content dissimilarity, a bottom-up approach using bipartite matching excels in finding the minimum difference between individual subtrees. Therefore, bipartite matching is applied to derive compound component similarity from the similarity measures of its primitive components. Further considering that different primitive components may contribute differently to the compound component, weighted bipartite matching [29] can be adopted by introducing different weights to the child nodes. Thus the end result is a weighted sum, that is,

$$
S _ {r s} ^ {\mathrm{Co} _ {j} ^ {P}} = \sum_ {k = 1} ^ {K j} \left(w _ {j k} ^ {M} \max \left\{S _ {r s} ^ {\left(\mathrm{Co} _ {j k} ^ {M}, \mathrm{Co} _ {j g} ^ {M}\right)} | \forall k, g = 1, \dots , K _ {j} \right\}\right),\tag{8}
$$

where $0 \leq S _ { r s j } ^ { \mathbf { C o } ^ { P } } \leq 1$ suggests the similarity measure of two compound components of the same type, $\mathrm { C o } _ { j r } ^ { P * }$ and $\begin{array} { r } { \mathrm { C o } _ { j s } ^ { P * } , \ \sum _ { k = 1 } ^ { \bullet } { \bf w } _ { \mathrm { j k } } ^ { \mathrm { M } } = \dot { 1 } \ } \end{array}$ , indicate the relative importance of $\{ \mathbf { C o } _ { j k } ^ { M } \} _ { K _ { j } }$ <sup>¼</sup>in regard to $O _ { j } ,$ and $S _ { r s } ^ { ( \mathrm { C o } _ { j k } ^ { M } , \mathrm { C o } _ { j g } ^ { M } ) }$ denotes the similarity measure of a paired child nodes, $\mathrm { C o } _ { j k r } ^ { M * }$ and $\mathrm { C o } _ { j g s } ^ { M * }$

## 5.4. Product similarity

Each product component, $\varPhi _ { O _ { i } = \mathrm { C o } j } ^ { P }$ , is a type of compound components. Its similarity measure follows the same text mining procedure as that of compound components, i.e., $S _ { r s } ^ { P _ { j } } { = } \bar { S } _ { r s } ^ { C 0 _ { j } ^ { P } }$ . The data records of product components are extracted from the text file for compound components by identifying those i-nodes. As a result, a product similarity matrix, $[ S _ { r s } ^ { P _ { j } } ] _ { P \times P } ,$ , can be constructed for each product component type. Finally, enumerating all the product components contained in the data file, $\{ { \mathrm { C o } } _ { j } ^ { P } \} _ { N } ,$ a total number of N product similarity matrices are constructed.

## 5.5. Resource similarity

The resource description, $R _ { j } ,$ of each operation, $O _ { j } \in \{ O _ { j } \} _ { N } ,$ includes three attributes: workcenter, $W _ { j } ,$ cycle time, $T _ { j } ,$ and setup, $S _ { j } .$ While $W _ { j }$ and $S _ { j }$ are nominal attributes, $T _ { j }$ is of the numerical type. Text mining is conducted in a similar fashion as that of primitive components. Resource descriptions of all operations (both l-nodes and i-nodes) are cataloged in a separate text file. Then text mining is carried out with respect to the three attribute fields and thus similarity measures in terms of workcenter $( S _ { r s } ^ { W _ { j } } )$ cycle time $( S _ { r s } ^ { T _ { j } } )$ and setup $( S _ { r s } ^ { S _ { j } } )$ are derived, i.e.,

$$
S _ {r s} ^ {\Theta_ {j}} = 1 - \frac {| \Theta_ {j r} ^ {*} - \Theta_ {j s} ^ {*} |}{\max \{\Theta_ {j i} ^ {*} | \forall i = 1 , \dots , P \} - \min \{\Theta_ {j i} ^ {*} | \forall i = 1 , \dots , P \}},\tag{9}
$$

where $S _ { r s } ^ { \Theta _ { j } }$ denotes $S _ { r s } ^ { W _ { j } } , \ S _ { r s } ^ { T _ { j } } , \ S _ { r s } ^ { S _ { j } } \in [ 0 ,$ 1]and $\Theta _ { j i } ^ { * }$ stands for $W _ { j i } ^ { * } , \ T _ { j i } ^ { * }$ and $S _ { j i } ^ { * }$ , meaning the specific values of workcenter, cycle time and setup of operation $O _ { j } ,$ respectively.

Accordingly, the resource similarity measure of two operation variants, $S _ { r s } ^ { R _ { j } }$ , is calculated as a weighted sum of similarity measures regarding all their attributes, i.e.,

$$
S _ {r s} ^ {R _ {j}} = w ^ {W _ {j}} S _ {r s} ^ {W _ {j}} + w ^ {T _ {j}} S _ {r s} ^ {T _ {j}} + w ^ {s _ {j}} S _ {r s} ^ {S _ {j}},\tag{10}
$$

where, $0 \le S _ { r s } ^ { R _ { j } } \le 1 , \ w ^ { W _ { j } } + w ^ { T _ { j } } + w ^ { S _ { j } } = 1$ and $w ^ { W _ { j } } , \ \boldsymbol { w } ^ { T _ { j } }$ and $w ^ { S _ { j } }$ denote the relative importance of workcenter, cycle time and setup attributes in regard to operation $O _ { j } ,$ respectively. Enumerating all instances of resource description, $R _ { j } ,$ a resource similarity matrix, $[ S _ { r s } ^ { R _ { j } } ] _ { P \times P } ,$ is constructed to present pairwise resource comparisons of all variants of operation $O _ { j } .$ Similarly, a total number of N resource similarity matrices are constructed for all the operations, $\{ O _ { j k } ^ { * } \} _ { N \times P }$

## 5.6. Normalized node content similarity matrix

Since $0 { \leq } S _ { r s } ^ { M _ { j } } , \ S _ { r s } ^ { P _ { j } } , \ S _ { r s } ^ { R _ { j } } { \leq } 1 , \ S _ { r s } ^ { O _ { j } }$ and $S _ { r s } ^ { N C }$ may not suggest a relative measure ranging from 0 to 1. They need to be normalized to achieve a consistent comparison. Many normalization methods are available such as the z-score and the max–min normalization methods [13]. This research adopts the max–min method to convert the node content similarity measure to a relative magnitude between 0 and 1, as the following:

$$
S _ {r s} ^ {N C ^ {\prime}} = \frac {S _ {r s} ^ {N C} - \min \left\{S _ {r s} ^ {N C} | \forall r , s = 1 , \dots , P \right\}}{\max \left\{S _ {r s} ^ {N C} | \forall r , s = 1 , \dots , P \right\} - \min \left\{S _ {r s} ^ {N C} | \forall r , s = 1 , \dots , P \right\}},\tag{11}
$$

where $S _ { r s } ^ { N C }$ and $S _ { r s } ^ { N C ^ { \prime } }$ denotes the original and normalized node content similarity measures between $\mathrm { R O U } _ { r }$ and ${ \mathrm { R O U } } _ { s } ,$ respectively.

Enumerate node content similarity calculation for all the ROUs in the routing data set. Then present all pairwise similarity measures in the form of an ROU node content similarity matrix, $[ S _ { r s } ^ { N C ^ { \prime } } ] _ { P \times P } .$ Each matrix element indicates the node content similarity of two routing variants corresponding to row and column, respectively.

## 5.7. Vibration motor case

The SPSS software package (www.spss.com) is employed for text analysis. Three attributes are used to describe the characteristics of each operation, including the material, product and resource types. In preparing data files for text mining, raw materials are described as material components of machining operations. Fig. 5 shows an example of the text file describing the characteristics of a component. An operation description data file is obtained by enumerating all the operations contained in the 30 routings corresponding to 30 product variants. Assorting all primitive and compound components for each operation, this data file is separated into two text files, one containing all primitive components and the other containing compound components. Then these two files are input into SPSS for text analysis.

![](/api/attachments/RE4JVE82/fulltext/images/8cd28464eb2432a49df7758d7904bfa32769b0e539923632d8abe5cb91149a33.jpg)  
Fig. 6. Extracted keywords and their occurrences for “ba” component type.

For illustrative simplicity, only one primitive component type (“ba”) is presented here. Fig. 6 shows the results of text analysis, including the extracted keywords (i.e., attribute values describing “ba” variants), and their respective occurrence counts. Based on extracted information, the relevant attributes are identified and their weights are calculated, as shown in Table 1.

For the set of attributes identified in Table 1, shape, color and material are of nominal type whilst weight and thickness are numerical ones. To quantify each nominal attribute, a semantic scale is assigned for its specific instances based on domain knowledge. Table 2 shows the scaled values for all attribute instances.

Based on established semantic scales, attribute similarity measures are calculated using Eq. (6) and the result is shown in Table 3. When measuring attribute similarity, 0 is used as the smallest semantic value to indicate nonexistence of an attribute. Based on the results of attribute similarity, similarity measure of component “ba” among 30 routing variants is derived using Eq. (7). The result is presented in a matrix form.

For “Bracket Assembly” operation, three primitive components, “ba”, “bb” and “tl”, constitute its material components while compound component “bassy” is the product component of this operation. Based on Eq. (8), compound component similarity is derived for “bassy”. Resource similarity measure precedes with text analysis in a similar fashion, where workcenter and setup are nominal variables and cycle time numerical. Semantic scales for nominal attributes workcenter and setup are assigned by the company's production engineers. Applying Eq. (9), the resource similarity matrix is obtained. Compiling results of component and resource similarity measures, operation similarity is derived using Eq. (2). Further applying Eqs. (1) and (11), the normalized node content similarity measures are calculated.

## 6. Tree structure similarity measure

Tree structure similarity measures the degree of commonality of two routings in terms of their operations sequences (i.e., the arcs of precedence graphs). To deal with such structural data, the tree matching technique is applied, which acquires the difference between two trees by finding the similarity of their structures [35]. The procedure proceeds as follows.

## 6.1. Determine a base ROU

For a specific ROU precedence graph, each particular operation executes in a different sequence from one another. As a result, an ROU constitutes a partial order set, in that not all the items in the set follow the same binary relation [27]. Since a partial order can be represented by more than one tree [24], each ROU may possess a number of alternative representation trees. The similarity measure of two ROUs may vary if different representation trees of them are used for the comparison. It is thus necessary to make decision based on pairwise comparisons of all possible representation trees of two ROUs.

Identified attributes and their relative importance

<table><tr><td>Attribute</td><td>Value set</td><td>Weight</td></tr><tr><td>Shape</td><td>Square, round, rectangle, trapezoid, half-oval-rectangle</td><td>0.235</td></tr><tr><td>Color</td><td>Black, yellow, gray, white, blue</td><td>0.165</td></tr><tr><td>Material</td><td>ABS, acrylic, pthene, PVC, nylon</td><td>0.152</td></tr><tr><td>Weight</td><td>0.05 g, 0.074 g, 0.08 g, 0.084 g, 0.12 g</td><td>0.224</td></tr><tr><td>Thickness</td><td>1.52 mm, 1.85 mm, 2.37 mm, 3.04 mm, 3.53 mm</td><td>0.224</td></tr></table>

Table 2  
Similarity scales for nominal attributes of “ba”

<table><tr><td rowspan="2">Shape</td><td>Instance</td><td>Square</td><td>Round</td><td>Rectangle</td><td>Trapezoid</td><td>Half-oval-rectangle</td></tr><tr><td>Scaled value</td><td>0.28</td><td>0.35</td><td>0.27</td><td>0.44</td><td>0.53</td></tr><tr><td rowspan="2">Color</td><td>Instance</td><td>Black</td><td>Gray</td><td>White</td><td>Yellow</td><td>Blue</td></tr><tr><td>Scaled value</td><td>0.32</td><td>0.16</td><td>0.47</td><td>0.36</td><td>0.25</td></tr><tr><td rowspan="2">Material</td><td>Instance</td><td>ABS</td><td>PVC</td><td>Acrylic</td><td>Pthene</td><td>Nylon</td></tr><tr><td>Scaled value</td><td>0.56</td><td>0.21</td><td>0.39</td><td>0.62</td><td>0.45</td></tr></table>

Owing to the symmetric property of distance measure and cyclic representation of a partial order [24], the pairwise comparisons can be simplified to merely compare an arbitrary tree of one ROU (referred to as a base ROU) with all representation trees of the rest ROUs. To reduce the total number of pairwise comparisons among ROUs, the ROU with the most representation trees should be selected as the base ROU.

## 6.2. Generate representation trees

For a number of P given routings, $\{ \mathrm { R O U } _ { r } | \forall r = 1 , . . . , P \}$ each of the first (P − 1) routings, $\{ \mathrm { R O U } _ { r } | \forall r { = } 1 , . . . , P { - } 1 \}$ serves as a base ROU for comparison of tree structure similarity with its immediate next ROU, $\{ \mathrm { R O U } _ { r + 1 } |$ $\forall r { = } 1 { , } . . . , P { - } 1 \}$ . Thus a total number of $P { \times } ( P { - } 1 ) / 2$ pairwise comparisons are needed. Except for the ROU selected to be the first base ROU, $\mathrm { e . g . , R O U _ { 1 } }$ , all the rest ROUs, e.g., $\{ \mathrm { R O U } _ { r } | \forall r { = } 2 , . . . , P \}$ , are compared with their corresponding base ROUs, ,e.g., $\{ \mathrm { R O U } _ { r - 1 } | \forall r = 2 , . . . , P \}$ To achieve this, all corresponding representation trees need to be generated for each of these (P− 1) ROUs.

## 6.3. Establish a tree edit graph

The basic principle of tree matching is to compare two trees based on tree transformation — to transform one tree to exactly the same as the other one [29]. It is accomplished by adopting a series of tree editing operations, including node insertion, deletion, and substitution. The transformation manifests certain costs incurred by the editing operations. The value of editing costs indicates the distance between two trees, namely their dissimilarity.

Since no constraints are introduced to the order of executing these editing operations, there may exist a number of ways to convert one tree to another. It would, however, be difficult to enumerate all possible ways of transformation in order to compare two trees. As a consequence, the obtained smallest transformation cost from enumeration may not be the optimal measure to suggest the distance of two trees. To circumvent this problem, the tree edit graph [35] is employed in this research to provide an indirect way of tree transformation.

Table 3  
Result of attribute similarity measure

<table><tr><td colspan="5">Weight similarity</td><td colspan="5">Thickness similarity</td></tr><tr><td>1</td><td>0.20</td><td>0.25</td><td>0.28</td><td>0.58</td><td>1</td><td>0.09</td><td>0.24</td><td>0.43</td><td>0.57</td></tr><tr><td>0.20</td><td>1</td><td>0.05</td><td>0.08</td><td>0.38</td><td>0.09</td><td>1</td><td>0.14</td><td>0.34</td><td>0.48</td></tr><tr><td>0.25</td><td>0.05</td><td>1</td><td>0.03</td><td>0.33</td><td>0.24</td><td>0.15</td><td>1</td><td>0.19</td><td>0.33</td></tr><tr><td>0.28</td><td>0.58</td><td>0.03</td><td>1</td><td>0.30</td><td>0.43</td><td>0.34</td><td>0.19</td><td>1</td><td>0.14</td></tr><tr><td>0.58</td><td>0.38</td><td>0.33</td><td>0.30</td><td>1</td><td>0.57</td><td>0.48</td><td>0.33</td><td>0.14</td><td>1</td></tr><tr><td colspan="5">Shape similarity</td><td colspan="5">Color similarity</td></tr><tr><td>1</td><td>0.13</td><td>0.02</td><td>0.30</td><td>0.47</td><td>1</td><td>0.34</td><td>0.32</td><td>0.09</td><td>0.15</td></tr><tr><td>0.13</td><td>1</td><td>0.15</td><td>0.17</td><td>0.34</td><td>0.34</td><td>1</td><td>0.66</td><td>0.43</td><td>0.19</td></tr><tr><td>0.02</td><td>0.15</td><td>1</td><td>0.32</td><td>0.49</td><td>0.32</td><td>0.66</td><td>1</td><td>0.23</td><td>0.47</td></tr><tr><td>0.30</td><td>017</td><td>0.32</td><td>1</td><td>0.17</td><td>0.09</td><td>0.43</td><td>0.23</td><td>1</td><td>0.23</td></tr><tr><td>0.47</td><td>0.34</td><td>0.49</td><td>0.17</td><td>1</td><td>0.15</td><td>0.19</td><td>0.47</td><td>0.23</td><td>1</td></tr><tr><td colspan="5">Material similarity</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>0.56</td><td>0.27</td><td>0.10</td><td>0.18</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.56</td><td>1</td><td>0.29</td><td>0.66</td><td>0.39</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.27</td><td>0.29</td><td>1</td><td>0.37</td><td>0.10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.10</td><td>0.66</td><td>0.37</td><td>1</td><td>0.27</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.18</td><td>0.39</td><td>0.10</td><td>0.27</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr></table>

The cost of an editing operation is reflected as a value attached to the corresponding arc. To facilitate comparisons based on a consistent common ground, the unit cost values for different types of tree editing operations are assumed to be the same. Therefore, the costs of different editing operations are indicated by the number of operations per se. For tree similarity measure between each ROU with the base ROU, the total number of tree edit graphs need to be generated equals to the number of representation trees implied by this ROU.

## 6.4. Find the shortest path for distance measure

In a tree edit graph, there are many paths from the top-left corner to the bottom-right corner. Each such a path suggests a possible way of transforming one tree to another, which carries different costs as well. The distance between two trees should be measured according to the shortest path that requires minimum number of arcs and thus fewest editing operations. The distance measure between every two trees is hence given as $D _ { r s } ^ { T S } { = } A ^ { * } C ,$ , where A <sup>⁎</sup> is the total number of valid arcs in the shortest path and C is a constant indicating unit cost value associated with each operation, regardless of its type.

Repeat the above procedures for comparing all the representation trees for one ROU with the base ROU. The distance measure between this ROU and the base ROU is determined by the minimum distance among all distance measures between its representation trees and the base ROU. Enumerate all the (P − 1) ROUs in the given ROU set. Their tree structure distances from the based ROU are reckoned in the same manner.

## 6.5. Normalize distance data

The above distance measures are all absolute values instead of relative magnitude. For consistent comparison, they need to be normalized. The max–min method is adopted to convert the absolute distance measure of each ROU pair to a dimensionless value ranging between 0 and 1, as the following:

$$
D _ {r s} ^ {T S ^ {\prime}} = \frac {D _ {r s} ^ {T S} - \min \left\{D _ {r s} ^ {T S} | \forall r , s = 1 , \dots , P \right\}}{\max \left\{D _ {r s} ^ {T S} | \forall r , s = 1 , \dots , P \right\} - \min \left\{D _ {r s} ^ {T S} | \forall r , s = 1 , \dots , P \right\}},\tag{12}
$$

where $D _ { r s } ^ { T S }$ and $D _ { r s } ^ { T S ^ { \prime } }$ denotes the absolute and normalized distance measures between ROU and ${ \mathrm { R O U } } _ { s } ,$ respectively.

## 6.6. Calculate tree structure similarity

According to the normalized distance measure, the similarity can be calculated as the following:

$$
S _ {r s} ^ {T S} = 1 - D _ {r s} ^ {T S ^ {\prime}}.\tag{13}
$$

## 6.7. Construct an ROU structure similarity matrix

Calculate similarity values for all the ROUs in the routing data set. Then present all pairwise similarity measures in a P × P matrix, $[ S _ { r s } ^ { T S } ] _ { P \times P }$ . Each matrix element indicates the structure similarity of two ROUs corresponding to row and column, respectively.

For the vibration motor case, representation trees are generated for each routing and then tree edit graphs are established for every paired trees in accordance with the number of i-node contained in each routing tree. The result of pairwise distance measures of 30 routing trees constitutes a tree structure distance matrix. Applying Eqs. (12) and (13) to these distance measures, tree structure similarity matrix is calculated.

## 7. ROU similarity measure

As node content similarity, $S _ { r s } ^ { N C ^ { \prime } } \in [ 0 , 1 ]$ , and tree structure similarity, $S _ { r s } ^ { T S } \in [ 0 , \dot { 1 } ]$ , are two independent measures, the overall ROU similarity, $S _ { r s } ,$ is composed by an Euclidian distance, i.e.,

$$
S _ {r s} = \sqrt {(S _ {r s} ^ {N C ^ {\prime}}) ^ {2} + (S _ {r s} ^ {T S}) ^ {2}}.\tag{14}
$$

To convert $S _ { r s }$ to a consistent magnitude for comparison ranging from 0 to 1, the normalization process is applied. Then the normalized ROU similarity value, $S _ { r s } ,$ is given as the following:

$$
S _ {r s} ^ {\prime} = \frac {S _ {r s} - \min \left\{S _ {r s} | \forall r , s = 1 , \dots , P \right\}}{\max \left\{S _ {r s} | \forall r , s = 1 , \dots , P \right\} - \min \left\{S _ {r s} | \forall r , s = 1 , \dots , P \right\}},\tag{15}
$$

such that $0 \leq S _ { r s } ^ { \prime } \leq 1$

Repeat ROU similarity calculation for all the ROUs in the routing data set. Then present all pairwise ROU similarity measures in a $P \times P$ matrix, $[ S _ { r s } ^ { \prime } ] _ { P \times P }$ . Each matrix element indicates the normalized similarity measure of two ROUs corresponding to row and column, respectively.

For the vibration motor case, compiling the node content similarity matrix and the tree structure similarity matrix, the normalized pairwise similarity measures of 30 routings are obtained and represented as a routing similarity matrix.

## 8. ROU clustering

ROU clustering aims to group a set of individual routings into classes of similar routings. An ROU cluster is a collection of routings that are similar to one another within the same cluster yet dissimilar to the routings in other clusters. Considering the complex data types involved in routings, this research adopts a fuzzy clustering approach [13,26].

Fuzzy equivalence relations excel in revealing the similarity between any two objects involving subjectiveness and imprecision [38]. Fuzzy clustering is to create a hierarchical decomposition of the given set of objects, in which each object forms a separate group and successively the objects or groups close to one another are merged at different similarity levels. In our case, historical data about ROU instances contained in the data files can be used to measure the similarity degree based on the compatibility of routing data. In comparison with the k-means method, fuzzy clustering partitions ROU instances based on the similarity degree that is derived from the real data of operations, rather than based on subjectively pre-defined clusters. The procedure of ROU clustering is as follows.

## 8.1. Define a fuzzy compatible relation

A fuzzy compatible relation, R, is defined as similarity measures for a given set of ROUs, $\mathcal { Q } { = } \left\{ \mathrm { R O U } _ { 1 } , . . . , \right.$ $\mathrm { R O U } _ { P } \}$ . The R is constructed in a matrix form, that is, $R = [ S _ { r s } ^ { \prime } ] _ { P \times P } $ , where $0 \leq S _ { r s } ^ { \prime } \leq 1$ suggests a pair-wise relationship (similarity grade) between any two ROU instances. Within the context of ROU clustering, R is called a compatible matrix as it is identical to an ROU similarity matrix.

In an ROU similarity matrix, it holds true that $S _ { r r } ^ { \prime } { = }$ $1 | \forall r { = } 1 { , } . . . , P ,$ suggesting that R is reflexive. Also true is $S _ { r s } ^ { \prime } { = } S _ { s r } ^ { \prime } , \forall r , s { = } 1 { , } { \ldots } , P ,$ suggesting that R is symmetrical. Therefore, matrix $R { = } [ S _ { r s } ^ { \prime } ] _ { P { \times } P } , \ S _ { s r } ^ { \prime } { \in } [ 0 { , } 1 ]$ becomes a fuzzy compatible relation defined on Ω. Representing a subset of Cartesian product $\varOmega \times \varOmega$ , matrix R is called a fuzzy compatible matrix.

## 8.2. Construct a fuzzy equivalence relation

A fuzzy equivalence relation is defined for Ω with transitive closure of a fuzzy compatible relation [38]. The fuzzy compatible matrix R is a fuzzy equivalence matrix if and only if the transitive condition can be met, i.e.,

$$
S _ {r s} ^ {\prime} \geq \max \left\{\min \left\{S _ {r z} ^ {\prime}, S _ {z s} ^ {\prime} \mid \forall R O U _ {r}, R O U _ {z}, R O U _ {s} \in \Omega \right\} \right\}.\tag{16}
$$

To convert a compatible matrix to an equivalence matrix, the “continuous multiplication” method is often used. Multiplication in fuzzy relations is also known as max–min composition [13]. Let $R ( \mathrm { R O U } _ { r } , \mathrm { R O U } _ { z } )$ and $R ( \mathrm { R O U } _ { z } , \mathrm { R O U } _ { s } )$ be two fuzzy compatible relations, then R∘ R=[max{min $\{ S _ { r z } ^ { \prime } S _ { z s } ^ { \prime } \} \}$ is also a fuzzy compatible relation.

## 8.3. Determine a λ-cut of the equivalence matrix

The λ-cut is a crisp set, $R _ { \lambda } ,$ , that contains all the elements of the universe, Ω, such that the similarity grade of R is no less than λ, that is,

$$
R _ {\lambda} = [ \tau_ {r s} ] _ {P \times P},\tag{17}
$$

where

$$
\tau_ {r s} = \left\{ \begin{array}{l l} 1 & \text { if } \quad S _ {r s} ^ {\prime} \geq \lambda \\ 0 & \text { if } \quad S _ {r s} ^ {\prime} <   \lambda \end{array} , S _ {r s} ^ {\prime} \in [ 0, 1 ]. \right.\tag{18}
$$

Then each λ-cut, $R _ { \lambda } ,$ is an equivalence relation representing the presence of similarity among ROU instances to the degree λ. For this equivalence matrix, there exists a partition on $\varOmega , \psi ( R _ { \lambda } ) ,$ , such that each compatible matrix is associated with a set, $\scriptstyle \psi ( R ) = \{ \psi ( R _ { \lambda } ) \}$

## 8.4. Identify ROU clusters

A netting graph method [38] is applied to identify partitions of ROU instances with respect to a given equivalence matrix.

With the hierarchy of partitions of objects, k-clusters of ROU instances can be identified. The value of $\lambda \in [ 0 , 1 ]$ indicates the similarity threshold of a λ-cut. Given an equivalence matrix, different clustering results may be obtained according to individual similarity thresholds. In practice, the value of λ is often determined by domain experts with many practical considerations, such as the extent of process reuse, convenience of process configuration, and capabilities of the product and process platforms.

For the vibration motor case, the routing similarity matrix, by its property, is a fuzzy compatible relation itself. Applying the max–min composition, a fuzzy equivalence matrix is obtained. Based on domain knowledge on clustering, a threshold level of 0.85 is decided. Accordingly the λ-cut matrix is obtained. The netted graph is developed, based on which the ROU clusters are derived. Table 4 gives the result of ROU clustering with four ROU clusters identified.

## 9. ROU unification

ROU unification attempts to unify all members of each ROU cluster into a generic routing. The major elements of a generic routing, ${ \mathrm { G R O U } } = \langle { \varLambda } , \succ \rangle$ include a set of master routings and a set of selective routings. The GROU entails a de facto configuration mechanism underlying a routing family.

The master routing set comprises sets of master operation classes, $A ^ { M } { } _ { ; }$ , and master precedence classes, $\succ ^ { M }$ , which constitute the common building blocks of a process family (i.e., the corresponding ROU cluster). Within this process family, all individual routings conform to a common process structure while exhibiting variations in specific operations characteristics.

Selective routings are sets of selective operation classes, $A ^ { S } ,$ , and selective precedence classes, $\succ ^ { \dot { S } } ,$ , which enable differentiation of individual routings. One routing variant may possess a different process structure from one another by adding different selective routings to the master routings in order to meet specific production requirements. The inclusion of an operation in an ROU is indicated by the presence of its related precedence. Each precedence, $O _ { i } { \succ } O _ { j } | \forall i \neq j \in [ 1 , N ]$ , is a binary variable with a 0/1 value, suggesting the existence of operation sequence $O _ { i } { \succ } O _ { j }$ and in turn the inclusion of operation $O _ { i } .$

While all master operations must be assumed by any routing variant, namely $O _ { i } ^ { M } { \succ } O _ { j } ^ { M } { \equiv } 1$ for all $O _ { i } ^ { \dot { M } } ,$ $O _ { j } ^ { \bar { M } } \in A ^ { M }$ and $O _ { i } ^ { M } { \succ } O _ { j } ^ { M } { \in } { \bf \bar { \Gamma } } ^ { M } ,$ , their characteristics in components and resources may be different among individual routings. This is modeled by specifying execution rules for the precedence class concerned. Execution rules are logical expressions defined for the instantiation of master operation classes by clarifying the circumstances under which individual operations are carried out. The general form of execution rules is like a production rule: $^ { 6 6 } \mathrm { I F }$ antecedent THEN consequent”. Logic operations such as AND, OR and XOR can be applied to both the antecedent and the consequent. Usually the antecedent is defined in terms of combinations of specific instances of operations material or product components, whilst the consequent depicts particular characteristics of related operations.

Table 4  
ROU clusters and respective ROU members

<table><tr><td>ROU cluster</td><td>ROU variants</td></tr><tr><td>RC1</td><td>R1, R3, R10, R13, R14, R17, R20, R22, R25</td></tr><tr><td>RC2</td><td>R2, R4, R5, R6, R7, R8, R9, R11, R16, R18</td></tr><tr><td>RC3</td><td>R23, R26, R27, R28, R29, R30</td></tr><tr><td>RC4</td><td>R12, R15, R19, R21, R24</td></tr></table>

A selective operation, $O _ { i } ^ { S } \in { \cal { A } } ^ { S } ,$ , is adopted if and only if its related precedence assumes a valid value, i.e., $\exists O _ { i } ^ { S } { \succ } O _ { i } ^ { S } { = } I ,$ , where $O _ { i } ^ { S } { \succ } O _ { j } ^ { S } { \in } { \succ } ^ { S }$ . When $\forall O _ { i } ^ { S } { \succ } O _ { j } ^ { S } { = } 0$ the selective routing (both $O _ { i } ^ { \bar { S } }$ and $O _ { i } ^ { S } { \succ } O _ { j } ^ { S } )$ by no means presents in a routing variant. The instantiation of selective routings is modeled by specifying inclusion conditions. An inclusion condition is expressed as production rules as well, where the antecedent bears the same implications as that of execution rules and the consequent however is defined by the existence of the related selective precedence.

Built upon the master and selective routing elements, the GROU is formed by maintaining a valid tree structure. The generic tree structure of a GROU, referred to as a generic tree, ${ \overline { { G } } } ,$ is developed, through a tree growing process, from the general tree structures embedded in individual routings, referred to as basic trees, $\{ \overline { { T } } _ { z } \} _ { Z } ,$ within an ROU cluster. The formation of a GROU involves four major steps, including assorting basic routing elements, identifying master and selective routing elements, forming basic trees, and tree growing, as discussed below.

## 9.1. Basic routing elements

The first step of ROU unification is to breakdown individual routings into operations and precedence elements. For each member of an ROU cluster, ${ \mathrm { R O U } } _ { r } \in$ $\{ \mathrm { R O U } _ { r } | \forall r = 1 , . . . , M \le P \}$ , the nodes (operations) and arcs (precedence) of the corresponding ROU tree are assorted and categorized by l-nodes or i-nodes. This results in a l-node set, $\{ L N _ { j r } \ast \} _ { N ^ { L N } \times M } ,$ an i-node set, $\lbrace I N _ { j r } { } ^ { * } \rbrace _ { N ^ { I N } \times M } ,$ a l-node arc set, $\{ L A _ { j r } \} _ { N ^ { L N } \times M } ^ { * } ,$ and an i-node arc set, $\lbrace L A _ { j r } ^ { * } \rbrace _ { ( N ^ { I N } - 1 ) \mathrm { x } M } ,$ corresponding to l-node type $\{ L N _ { j } \} _ { N ^ { L N } } ,$ , i-node type $\{ I N _ { j } \} _ { N ^ { L N } } ,$ l-node arc type $\{ L A _ { j } \} _ { N ^ { L N } } ,$ and i-node arc type $\{ { \cal { A } } _ { j } \} _ { N ^ { I N - } 1 } .$ , respectively, where $N ^ { L N } + N ^ { I N } = N , \ \forall L N _ { j } , \ \hat { I } N _ { j } \in \mathring { A } , \ \{ L N _ { j } \} \cap \ \mathring { \{ I }  N _ { j } \} = \mathring { \bigotimes }$ $\forall L A _ { j } , L A _ { j } \in \ \Join$

Configuration rules are also compiled for every node and arc contained in the ROU cluster. For exactly the same operations in different routings, their related rules need to be documented only once. All rules are initially placed in one rule set.

## 9.2. Master and selective routing elements

The second step is to generalize each individual routing element (operation or precedence variant) with regard to its original type. This is achieved by replacing the specific name or ID of each specific node or arc with the general name or ID of the operation or precedence class that it belongs to. As a result, each particular routing element is labeled with its class identification. And in turn each operation or precedence class assumes a certain number of occurrences in terms of the number of times individual routing elements are generalized into this class. Such an occurrence count performs as a commonality index revealing to what extent each routing element is reused among individual members of an ROU family.

Given an ROU cluster, $\{ \mathrm { R O U } _ { r } \} _ { M } ,$ if the occurrence count of a precedence class $( O _ { i } \succ O _ { j } )$ reaches the maximal number of instances of this class contained in the cluster, $\mathrm { i . e . , ~ } \varphi _ { O _ { i } \succ O j } { = } M ,$ it means that all individual routings in the cluster employ this precedence class. Therefore, this precedence class along with the related operation classes suggest themselves to be the master routing elements, i.e., the master precedence and operation classes, respectively. Should $1 \leq \varphi _ { O _ { i \times } O j } < M ,$ the related operation and precedence classes are defined as selective operation and precedence classes, respectively, as not all individual variants assume them. In this way, all basic routing elements are grouped into either master or selective routing elements.

In accordance with the identified master and selective routing elements, the configuration rules are orchestrated and classified into one execution rule set for master routings and one inclusion condition rule set for selective routings. The purpose of grouping all execution rules or inclusion conditions into one separate rule set is to warrant that the execution rules or inclusion conditions are defined globally, rather than associated with individual master or selective routing elements. This helps to maintain the respective configuration rules more concisely and in consistent forms.

## 9.3. Basic tree structures

The third step deals with the generalization of basic trees underlying all the ROU family members. A basic tree refers to the common tree structure assumed by certain routing variants. Given a number of basic routing elements, many possible routings may be configured. But some routing configurations may not form a valid tree. For example, some precedence classes may form a circle or violate certain execution rules or inclusion conditions. Therefore, a number of $Z \le M$ basic tree structures, $\{ \overline { { T } } _ { z } \} _ { Z } ,$ are identified from M member trees of the ROU family.

While each member tree denotes a specific routing variant, a basic tree represents a class of individual routing variants bearing the same tree structure. To track commonality of a basic tree with respect to its represented routing variants, each arc of the basic tree is assigned a weight indicating the degree of repetition of this arc among $M _ { z } \le Z$ routings. Initially, the value of such a weight is set to be the same as the occurrence count of each arc, regardless it is a master or selective precedence. In accordance with the assortment of basic routing elements, a basic tree is specified by a 4-tuple, denoted as:

$$
\bar {T} _ {z} = \left(\bar {L} ^ {N}, \bar {I} ^ {N}, \bar {L} ^ {A}, \bar {I} ^ {A}\right),\tag{19}
$$

where $\begin{array} { r } { \bar { L } ^ { N } ( \overline { { T } } _ { z } ) = \{ L n _ { z j } \} _ { Z \times N _ { \circ } ^ { L N } } , \bar { I } ^ { N } ( \overline { { T } } _ { z } ) = \{ I n _ { z j } \} _ { Z \times N _ { \circ } ^ { I N } } , \bar { L } ^ { A } ( \overline { { T } } _ { z } ) = } \end{array}$ $\{ L a _ { z j } \} _ { Z \times N _ { z } ^ { L N } }$ and $\bar { I } ^ { 4 } ( \overline { { T } } _ { z } ) = \bar { \{ { I a _ { z j } \} } } _ { Z \times ( N _ { z } ^ { I N } - 1 ) }$ are sets of basic routing elements, encompassing all l-node classes, i-node classes, l-node arc classes and i-node arc classes contained in $\overline { { T } } _ { z } ,$ respectively. Their respective variant sets are $\begin{array} { r l } { \{ L n _ { z j r } ^ { * } \} _ { Z \times N _ { z } ^ { L N } \times M _ { z } } , } & { { } \{ I n _ { z j r } ^ { * } \} _ { Z \times N _ { z } ^ { I N } \times M _ { z } } , \{ L a _ { z j r } ^ { * } \} _ { Z \times N _ { z } ^ { L N } \times M _ { z } } } \end{array}$ and $\{ I a _ { z j r } ^ { * } \} _ { Z ^ { \times } ( N _ { z } ^ { I N } - 1 ) \times M _ { z } }$ , where $\begin{array} { r } { \dot { \sum _ { z = 1 } ^ { Z } } ( N _ { z } ^ { L N } + \dot { N } _ { z } ^ { I N } ) ^ { \top } = N } \end{array}$ <sup>¼</sup>The basic routing elements constituting basic trees are further classified into master or selective sets based on the occurrence counts of individual precedence variants $\varphi _ { O _ { i } ^ { z } \succ O _ { j } ^ { z } } { = } M _ { z } o r 1 \le \varphi _ { O _ { i } ^ { z } \succ O _ { j } ^ { z } } { < } M _ { z } .$

## 9.4. Tree growing

The fourth step aims to form the generic tree by pasting all basic trees one by one, that is, $\overline { { G } } = \overline { { T } } _ { 1 } \cup . . . .$ ⋃ $\overline { { T } } _ { z }$ This entails that $\overline { { L } } ^ { N } ( \overline { { G } } ) { = } \overline { { L } } ^ { N } ( \overline { { T } } _ { 1 } ) \cup . . . \cup \overline { { L } } ^ { N } ( \overline { { T } } _ { z } )$ and likewise for $\overline { { I } } ^ { N } ( \overline { { G } } ) , \overline { { L } } ^ { A } ( \overline { { G } } )$ , and $\bar { I } ^ { A } ( \overline { { G } } )$

Tree growing starts with the selection of a seed, i.e., an initial generic tree, ${ \overline { { G } } } _ { I } .$ Among basic trees, $\{ \overline { { T } } _ { z } \} _ { Z } ,$ the one holding a longest path and possesses the maximal number of i-nodes is recognized as the seed. Such a comprehensive tree encompasses most production conditions occurring among the process family members. Then the initial generic tree, $\overline { { G } } _ { 1 : }$ , starts to grow by unifying with the other $Z - 1$ basic trees one by one, that is, $\overline { { G } } _ { i } = \overline { { G } } _ { i - 1 } \cup \overline { { T } } _ { i } ,$ where $\overline { { G } } _ { i }$ is a growing tree. After all basic trees are unified, the growing tree reaches its final form, ${ \overline { { G } } } _ { Z } ,$ namely, the generic tree structure of the GROU.

Since the generic structure of a GROU includes all operations occurred in the ROU cluster, both $\overline { { L } } ^ { N } ( \overline { { G } } )$ and $\bar { I } ^ { \bar { N } } ( \overline { { G } } )$ are simply union of all node sets contained in basic trees, i.e.,

$$
\overline {{L}} ^ {N} (\overline {{G}} _ {i}) = \overline {{L}} ^ {N} (\overline {{G}} _ {i - 1}) \cup \{L n _ {i j} \} _ {1 \times N _ {i} ^ {L N}},\tag{20}
$$

$$
\overline {{I}} ^ {N} (\overline {{G}} _ {i}) = \overline {{I}} ^ {N} (\overline {{G}} _ {i - 1}) \cup \{I n _ {i j} \} _ {1 \times N _ {i} ^ {I N}}.\tag{21}
$$

However, $\overline { { L } } ^ { A } ( \overline { { G } } )$ and ${ \overline { { I } } } ^ { A } ( { \overline { { G } } } )$ do not work with simple union operations, because a tree structure has to be maintained throughout the tree growing process. All the master l-node arcs and master i-node arcs contained in $\overline { { T } } _ { i }$ must be added to the respective master l-node arc set and master i-node arc set of $\overline { { G } } _ { i - 1 }$ . The selective $l -$ node arcs and master i-node arcs of $\overline { { T } } _ { i }$ however may not always contribute to maintaining the generic structure. If adding some arcs of $\overline { { I } } ^ { A } \ : ( \overline { { T } } _ { i } )$ to the growing tree may jeopardize the generic tree structure, these arcs are put in an additional arc set, $A _ { A S } ,$ for further examination with such arcs derived from other tree growing operations. In addition, adding an arc must be conducive to making the generic tree as common as possible to most routing variants. Hence only arcs demonstrating certain commonality (indicated by recorded weights) are added; otherwise put in $A _ { A S }$ for further evaluation as well.

If a l-node arc exists in $\textstyle { \overline { { T } } } _ { i }$ but not in $\bar { G } _ { i ^ { - } I }$ then this arc is of selective type, i.e., $L a _ { i j } ^ { S }$ . Such selective arcs, $\{ L a _ { i j } ^ { S } \} _ { N _ { i } ^ { L N S } } ,$ are pasted to $\overline { { G } } _ { i - 1 }$ only when their associated operations, i.e., selective l-nodes, $\{ L a _ { i j } ^ { S } \} _ { N _ { i } ^ { L N S } } ,$ do not exist in $\overline { { G } } _ { i - l }$ at the same time. Except this situation, if to include a selective l-node arc of ${ \overline { { T } } } _ { i } ,$ $L a _ { i j } ^ { S } { \in } \overline { { L } } ^ { A } ( \overline { { T } } _ { i } )$ , into $\bar { G } _ { i - 1 }$ or to put it in $A _ { A S }$ depends on the result of comparing its weight, $W _ { j } ^ { L a _ { i j } ^ { S } }$ , with that, $W _ { j } ^ { L a _ { ( i - l ) j } ^ { S } }$ , of the corresponding arc in $\overline { { G } } _ { i - I }$ . Whichever assuming higher weight should be included, as a higher weight means more common of a selective arc. Such a weight results from the sum of the occurrence count of this arc in all member trees and the recorded weight of the same arc in $A _ { A S } ,$ if it is not empty.

Likewise a selective i-node arc, $I a _ { i j } ^ { S } { \in } \overline { { L } } ^ { A } ( \overline { { T } } _ { i } )$ , does not exist in $\bar { G } _ { i - 1 }$ . Only when the associated parent i-node and child i-nodes do not exist in $\bar { G } _ { i - 1 }$ at the same time can this i-node arc be added to $\overline { { G } } _ { i - 1 }$ Otherwise, evaluation of its weight is needed. Arc unification essentially aims to combine the arc sets of $\boldsymbol { \overline { { T } } } _ { i }$ and $\bar { G } _ { i - 1 }$ while removing those less common arcs.

Upon completion of the tree growing process, the formed GROU consists of a generic tree structure and an additional arc set. Due to the presence of selective arcs in the generic tree, the GROU is by no means the union of all member trees. Addition and removal of certain arcs according to their weights ensure that the resulted generic structure is most common among individual routings in an ROU family.

## 9.5. Vibration motor case

For each ROU cluster, one GROU is formed by tree growing. For example, routing cluster “RC1” contains 9 member trees (R1, R3, R10, R13, R14, R17, R20, R22 and R25). The tree structures of these 9 routings are unified as a generic tree. Fig. 7 presents the identified GROU for “RC1”, which is represented using the unified modeling language (www.uml.org). As shown in the GROU, not all operation types are necessary for producing each motor variant. For example, $^ { 6 6 } \mathrm { w t } ^ { 9 }$ is purchased rather than made in house for some customer orders, and thus the corresponding “wt” machining operation manifest itself as a type of selective operations.

The performance of the identified generic routings is tested by benchmarking with the traditional manual approach — a pen-and-paper method performed by domain experts. Also considered is the performance with respect to different data sizes. Five different sets of routing data are used, including 30 (the base case used in the case study), 60, 100, 150 and 220 product models produced in the company. The performance is measured according to the expected utility of product families as perceived by the customers with respect to the fix cost of the product and process platforms corresponding to the identified GROU [18]. Fig. 8 shows the result of testing in terms of normalized comparison. As shown in the figure, the data mining approach outperforms the manual method in overall. With the increase of data size, the advantage of the data mining approach over the manual method become evident. While the data mining approach performs better with more routing data, the performance of the manual method does not keep pace with the increase in data size and even deteriorates when given a large size of data. This may verify the fact that data mining usually works well with large amount of data available. To the contrary, human intelligence works with limited amount of data and always gets lost when facing overwhelming amount of data.

## 10. Concluding remarks

A generic routing essentially performs as a process platform to support the fulfillment of product families. It contributes to the utilization of commonality underlying process variations. The identification of generic routings coincides with the wisdom of knowledge reuse and economy of repetition [34]. Most of the industries have a host of historical information on product changes and process variations incorporated in mass customization [16]. As the information size could be quite large, structured query techniques can be used for data and text mining so that it can form a process platform to assist in managing variety and producing the mass customized products with economic efficiency. Generating generic routings based on knowledge discovery from past data avails to maintain the integrity of existing product and process platforms, as well as the continuity of the infrastructure and core competencies, hence leveraging existing design and manufacturing investments. The application of data mining opens opportunities for incorporating experts' experiences into the projection of production planning patterns from historical data, thereby enhancing the ability to explore and utilize domain knowledge more effectively.

![](/api/attachments/RE4JVE82/fulltext/images/97ab56e4e215cccf33280c414de74a1a8e71cfa085ce0c872d0954dbc88843f7.jpg)  
Fig. 7. Identified GROU for routing cluster “RC1”.

The clustering result depends upon specification of the threshold, which requires intensive collaboration with domain experts and considerations of particular problem contexts. Decisions on the proper similarity threshold may be tricky or complex for enterprise managers. In practice, this can be alleviated through iterative interactions between generic routing identification and evaluation. Usually, a few scenarios with different settings of similarity threshold are identified and then input to the generic routing formation process. Based on the running results, the performances of them are evaluated against a few pre-defined business objectives. Then the best setup is determined and the generic routing identified is refined. Hence, generic routing identification and its evaluation are iterative in implementation and thereby should be integrated within a unified framework of process platform planning. This paves an avenue to further research.

Furthermore, the current approach assumes that operations similarity and precedence similarity carry an equal importance. In practice, this may depend on particular production environments [22]. For example, in capital intensive and highly automated industries like automobile or electronics assembly systems, line balancing is an important concern. Their routings sequences are far more important than individual operation characteristics. On the other hand, some labor intensive production systems may not be sensitive to changes in operations sequences, whereas operations characteristics like tooling and setup play a major role. Therefore, a number of practical issues should be taken into account when formulating different similarity measures.

Normalized Performance MeasureData Mining Manual  
![](/api/attachments/RE4JVE82/fulltext/images/ddc6dde98c573d573b9ca0f541a5c9fdd651ed818ceda276188b6fdce8f5eb8b.jpg)  
Fig. 8. Performance comparison of the data mining and manual approaches.

## References

[1] B. Agard, A. Kusiak, Data-mining-based methodology for the design of product families, International Journal of Production Research 42 (15) (2004a) 2955–2969.

[2] B. Agard, A. Kusiak, Data mining for subassembly selection, ASME Transactions: Journal of Manufacturing Science and Engineering 126 (3) (2004b) 627–631.

[3] J. Atkinson-Abutridy, C. Mellish, S. Aitken, A semantically guided and domain-independent evolutionary model for knowledge discovery from texts, IEEE Transactions on Evolutionary Computation 7 (6) (2003) 546–560.

[4] J.W.M. Bertrand, M. Zuijderwijk, H.M.H. Hegge, Using hierarchical pseudo bills of material for customer order acceptance and optimal material replenishment in assemble to order manufacturing of non-modular products, International Journal of Production Economics 66 (2) (2000) 171–184.

[5] J.H. Blackburn, Improve MRP and JITcompatibility by combining routings and bills of material, Proceedings of the American Production and Inventory Control Society, 1985, pp. 444–447.

[6] S.-H. Chang, W.-L. Lee, R.-K. Li, Manufacturing bill-of-material planning, Production Planning and Control 8 (5) (1997) 437–450.

[7] P.-C. Chang, C.-H. Liu, Y.-W. Wang, A hybrid model by clustering and evolving fuzzy rules for sales decision supports in printed circuit board industry, Decision Support Systems 42 (3) (2006) 1254–1269.

[8] M.C. Chen, Configuration of cellular manufacturing systems using association rule induction, International Journal of Production Research 41 (2) (2003) 381–395.

[9] M. Chen, J. Han, P. Yu, Data mining: an overview from database perspective, IEEE Transactions on Knowledge and Data Engineering 8 (6) (1996) 866–883.

[10] P. De Lit, A. Delchambre, J.M. Henrioud, An integrated approach for product family and assembly system design, IEEE Transactions on Robotics and Automation 19 (2) (2003) 324–333.

[11] R.R. Farrell, T.C. Maness, A relational database approach to a linear programming-based decision support system for production planning in secondary wood product manufacturing, Decision Support Systems 40 (2) (2005) 183–196.

[12] S. Gupta, V. Krishnan , Product family-based assembly sequence design methodology, IIE Transactions 30 (3) (1998) 933–945.

[13] J. Han, M. Kamber, Data Mining: Concepts and Techniques, Morgan-Kanfmann, San Mateo, CA, 2001.

[14] N.A.J. Hastings, C.-H. Yeh, Bill of manufacture, Production and Inventory Management Journal 33 (4) (1992) 27–31.

[15] D.W. He, A. Kusiak, Design of assembly systems for modular products, IEEE Transactions and Automation 13 (5) (1997) 646–655.

[16] M.R. Hoogeweegen, D.W. van Liere, P.H.M. Vervest, L.H. van der Meijden, I. de Lepper, Strategizing for mass customization by playing the business networking game, Decision Support Systems 42 (3) (2006) 1402–1412.

[17] J. Jiao, M.M. Tseng, Customizability analysis in design for mass customization, Computer-Aided Design 36 (8) (2004) 745–757.

[18] J. Jiao, Y. Zhang, Product portfolio identification based on association rule mining, Computer-Aided Design 37 (2) (2005) 149–172.

[19] J. Jiao, M.M. Tseng, Q. Ma, Y. Zou, Generic bill of materials and operations for high-variety production management, Concurrent Engineering, Research and Application 8 (4) (2000) 297–322.

[20] J. Jiao, L. Zhang, S. Pokharel, Process platform planning for variety coordination from design to production in mass customization manufacturing, IEEE Transactions on Engineering Management 54 (1) (2007) 119–129.

[21] R. Kolisch, Integration of assembly and fabrication for make-toorder production, International Journal of Production Economics 68 (3) (2000) 287–306.

[22] R.J. Kuo, Y.T. Su, C.Y. Chiu, K.-Y. Chen, F.C. Tien, Part family formation through fuzzy ART2 neural network, Decision Support Systems 42 (1) (2006) 89–103.

[23] H.J. Lee, J.K. Lee, An effective customization procedure with configurable standard models, Decision Support Systems 41 (1) (2005) 262–278.

[24] M.T. Martinez, J. Favrel, P. Ghodous, Product family manufacturing plan generation and classification, Concurrent Engineering, Research and Applications 8 (1) (2000) 12–22.

[25] M. Meyer, A.P. Lehnerd, The Power of Product Platform — Building Value and Cost Leadership, Free Press, New York, 1997.

[26] B.K. Mohanty, B. Bhasker, Product classification in the Internet business— A fuzzy approach, Decision Support Systems 38 (4) (2005) 611–619.

[27] NIST, http://www.nist.gov/dads/HTML/partialorder.html.

[28] C.J. Romanowski, R. Nagi, A data mining approach to forming generic bills of materials in support of variant design activities, ASME Journal of Computing and Information Science in Engineering 4 (4) (2004) 316–328.

[29] C.J. Romanowski, R. Nagi, On comparing bills of materials: a similarity/distance measure for unordered trees, IEEE Transactions on Systems, Man, and Cybernetics, Part A 35 (2) (2005) 249–260.

[30] S.W. Sanderson, M. Uzumeri, Managing Product Families, McGraw-Hill Management and Organization Series, Singapore, 1997.

[31] K. Schierholt, Process configuration: combining the principles of product configuration and process planning, AIEDAM — Artificial Intelligence for Engineering Design, Analysis and Manufacturing 15 (5) (2001) 411–424.

[32] T.W. Simpson, Product platform design and customization: Status and promise, AIEDAM, Special Issue on Platform Product Development for Mass Customization 18 (2) (2004) 3–20.

[33] I.P. Tatsiopoulos, On the unification of bills of materials and routings, Computers in Industry 31 (3) (1996) 293–304.

[34] A.P. Tchangani, A satisficing game theory approach for group evaluation of production units, Decision Support Systems 42 (2) (2006) 778–788.

[35] G. Valiente, Algorithms on Trees and Graphs, Springer-Verlag, Berlin, 2002.

[36] E.A. van Veen, Modeling Product Structures by Generic Bills-of-Materials, Elsevier, New York, 2002.

[37] E. Westkämper, Th. Schmidt, H.-H. Wiendahl, Production planning and control with learning technologies: Simulation and optimization of complex production processes, in: G. Leondes (Ed.), Knowledge-based Systems, vol. 3, Academic Press, New York, 2000.

[38] H.J. Zimmermann, Fuzzy Set Theory and Its Applications, Kluwer Academic Publishers, USA, 2001.

![](/api/attachments/RE4JVE82/fulltext/images/781719b98d1af58a26436b7165057e38e602408ad45117100f49dfcd6b4585cc.jpg)

Jianxin (Roger) Jiao is Assistant Professor of Systems and Engineering Management, School of Mechanical and Aerospace Engineering, Nanyang Technological University, Singapore. He received his Ph.D. in Industrial Engineering from Hong Kong University of Science & Technology. He holds a Bachelor degree in Manufacturing Engineering from Tianjin University of Science & Technology in China, and a Master degree in Mechanical

Engineering from Tianjin University, China. His research interests include mass customization, design theory & methodology, reconfigurable manufacturing systems, engineering logistics, and intelligent systems. His publications appear in IIE Transactions, IEEE Transactions on Engineering Management, Computer-Aided Design, CIRP Annals, Journal of Intelligent Manufacturing, Expert System with Applications, Computers and Operations Research, AIEDAM, Computers in Industry, International Journal of Production Research, etc He is a member of IEEE, ASME, and IIE.  
![](/api/attachments/RE4JVE82/fulltext/images/52a03a5cc9193e98d191dd12bae095443f187b68be6e88c584de6bf3f9af17d0.jpg)

Lianfeng Zhang is Adjunct Lecturer of Operations Management in the Business School at Singapore Management University. She received her Ph.D. in Industrial Engineering from Nanyang Technological University, Singapore. She received her Bachelor of Engineering Degree from School of Management at Tianjin University, China. Before her Ph.D. study, she has worked as an industrial engineer in ST Microelectronics in Shenzhen,

China. Her current research is focused on product–process platform development for mass customization, Petri net application for process configuration modeling, and production reconfiguration.

![](/api/attachments/RE4JVE82/fulltext/images/b17199b6cbb97bfd9257bdf77c4656661f1d4664df051e18413463e0b0a7288f.jpg)  
Shaligram Pokharel is an Associate Professor of Systems and Engineering Management Division, School of Mechanical and Aerospace Engineering, the Nanyang Technological University, Singapore. He received his B.E. in Mechanical Engineering from The University of Kashmir, India, and M.A.Sc. and Ph.D. in Systems Design Engineering from the University of Waterloo, Canada. His main research interests are in systems design,  
logistics and supply chain management, product and process platform development and energy planning. His publications appear in journals such as International Journal of Operations Research, European Journal of Operations research, Journal of Enterprise Information Management, Energy, and Energy Policy.

![](/api/attachments/RE4JVE82/fulltext/images/ed370e6e8fe5119ba000c5ce6665a635044b9ce56d98f3e4fb769cd3c611d4b4.jpg)  
HE Zhen is a professor of industrial engineering in School of Management, Tianjin University, China. He received his PhD degree from School of Management, Tianjin University, China, in 2000. His research interests include industrial engineering, quality engineering and six Sigma management, etc.
