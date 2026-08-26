---
otero_id: 4028
otero_key: "9A6QEFNY"
title: "A graph rewriting system for process platform planning"
authors: "Linda L. Zhang; Roger J. Jiao"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A graph rewriting system for process platform planning

Linda L. Zhang <sup>a,</sup>⁎, Roger J. Jiao <sup>b</sup>

<sup>a</sup> IESEG School of Management (LEM-CNRS), Catholic University of Lille, 3 rue de la Digue, 59000 Lille, Franc

<sup>b</sup> The George W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, 813 Ferst Drive, 30332-0405 Atlanta, GA, USA

## a r t i c l e i n f o

Article history: Received 26 September 2011 Received in revised form 18 April 2012 Accepted 11 November 2012 Available online 19 November 2012

Keywords: Process platform planning Product family Planning automation Graph rewriting system PROGRES

## a b s t r a c t

Facilitating production process planning for product families, process platform planning (P<sup>3</sup>) has been well recognized as an effective means of achieving production ef<sup>fi</sup>ciency. To support decision making in P<sup>3</sup> automation, this study adopts graph rewriting systems to 1) organize large volumes of product and process data and 2) model production process planning reasoning. The model developed represents the structural and behavioral aspects of process platforms as family graphs and related graph transformations, respectively. In view of its modeling advantage, the system is formally de<sup>fi</sup>ned using PROGRES. It includes meta, generic, and instance models at three different levels of abstraction. Meta models are de<sup>fi</sup>ned for family graphs to generalize the patterns common to planning production processes for different product families; generic models are de<sup>fi</sup>ned to describe entities pertaining to production processes of speci<sup>fi</sup>c product families; instance models represent production processes producing product variants in a family. The graph rewriting system-based P<sup>3</sup> model is applied to textile spindles' production process planning. The results obtained have demonstrated its potential and feasibility to support decision making in P<sup>3</sup> automation.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the front end of product development, design is to convert customer requirements into a list of technical speci<sup>fi</sup>cations, such as materials and dimensions. Based on a production process, companies produce a physical product con<sup>fi</sup>rming to the de<sup>fi</sup>ned technical speci<sup>fi</sup>cations. In this regard, production processes have major in<sup>fl</sup>uences on production performance, such as product quality, production lead time, and cost [2,7,8,17]. A production process consists of operations, manufacturing resources carrying out operations, and operations precedence. In accordance with component items at different levels of a product hierarchy, operations can be grouped into a number of subproduction processes. Each of these subprocesses is either to manufacture a part or to form an assembly. A production process thus provides necessary input (e.g., items, machines) to downstream computer-aided process planning and computer-aided assembly planning such that the detailed process parameters (e.g., feed rate, cutting speed) can be determined for either manufacturing a part or forming an assembly [28]. (For clarity, the term: production process is used for a <sup>fi</sup>nal product and the term: process for a component item, be it a part or an assembly.) In spite of the above important role of production processes, in practice companies plan production processes by trial-and-error based on individual ‘know-how’, experience, and intuition [8,22]. Consequently, it is not uncommon that for a same product, different planners come up different production processes with many variations. Decision on the production processes to be adopted is often made by the responsible planner with his subjective planning knowledge and skills [15]. Nevertheless, this trial and error-based production process planning is still viable in such manufacturing environments, where a very limited number of product variants are involved.

In manufacturing environments nowadays, companies strive to design product families, instead of single products, to satisfy various customer requirements while maintaining design ef<sup>fi</sup>ciency and reducing design costs and time [9,11,14]. Despite the similarities in product structures and/or product items, product variants belonging to a family require different production processes due to their distinctiveness. As a consequence of the above traditional planning, companies struggle with many frequent yet unnecessary production changeovers on shop <sup>fl</sup>oors when producing diverse customized products. On the other hand, the key to ef<sup>fi</sup>ciently produce product families is to maintain production to be as stable as possible [1,23,24]. Such stable production can only be achieved by eliminating the unnecessary production process variations, which are often caused by the traditional planning approaches [26,27]. This highlights the importance in developing solutions that plan production processes for customized products by considering the optimal production performance of the cohort of the family. In view of the importance of new planning solutions, a concept of process platform planning (P<sup>3</sup>) is put forward to address production processes planning for product families such that product family production ef<sup>fi</sup>ciency can be achieved [10,25]. The rationale of P<sup>3</sup> lies in the fact that it capitalizes on design similarity in planning. In line with the consensus on product platforms: a product platform is an abstract structure including subsystems and their interfaces, from which a family of customized products can be derived [16], whereas a process platform refers to a common, uni<sup>fi</sup>ed structure consisting of all process elements and their relationships necessary for producing a product family (see more details in Section 2). In this regard, a process platform limits the planning solution space to a priori determined framework, thus enabling con<sup>fi</sup>guration and reuse of proven planning knowledge. In addition, it helps plan for necessary changes in production processes in accordance with design variations of product family members. With process changes pre-planned, companies can timely produce diverse products while ensuring the optimal utilization of available manufacturing resources and capabilities [17].

In $\mathrm { P } ^ { 3 }$ , a family of production processes (i.e., a process family) is planned to produce a product family. In this regard, a process family refers to the set of production processes producing the corresponding product variants in the product family. In a related study [26], the authors address the construction of the generic routing structure underpinning a process platform. In this study, we go a step further by providing insight in process platform planning so as to support decision making in its automation. We accomplish this by modeling process families and their planning. By modeling a process family, we attempt to show how the large volumes of data involved in a process platform should be organized. By modeling the planning process, we aim to shed light on the reasoning behind planning production processes for product families based on process platforms. By nature, such modeling involves both static representation and dynamic modeling. It, in turn, necessitates such a tool that is able to simultaneously represent system static structures and model system dynamic processes.

Unlike most modeling tools designed to either represent a system from the static aspect or model a system from the dynamic aspect (e.g., Petri nets, simulation, mathematical programming, data diagrams, <sup>fl</sup>ow charts), graph rewriting systems are developed to model systems by capturing both systems' constituent elements, their relationships, and system dynamic behavior [19]. Their applications have been seen in a wide range of areas, such as data structure speci<sup>fi</sup>cation, process modeling, and con<sup>fi</sup>guration management [21]. In a recent related study [4], the authors apply graph rewriting systems to model how product families are designed. Their work demonstrates the advantages of modeling complex systems using graph rewriting systems. Therefore, in this study, we adopt graph rewriting systems to model $\mathrm { P } ^ { 3 } .$ . Furthermore, we de<sup>fi</sup>ne the proposed graph rewriting system-based $\mathrm { P } ^ { 3 }$ in a high level, multi-paradigm speci<sup>fi</sup>cation language: PROgrammed Graph Rewriting System (PROGRES), which supports the speci<sup>fi</sup>cation of hierarchical graph schema and parametric rewriting rules for graph transformations.

The rest of the paper is organized as follows. In Section 2, the general process of ${ \mathrm { \dot { P } } } ^ { 3 }$ and the fundamental issues are introduced. Consistent with the general process and the fundamental issues, the constructs of graph rewriting systems for $\mathrm { P } ^ { 3 }$ are discussed in Section 3. Also discussed are the guidelines of graph rewriting system-based $\mathrm { P } ^ { 3 }$ modeling. Sections 4 and 5 present the graph schema and graph transformations for $\mathrm { P } ^ { 3 }$ modeling, respectively. The results of a case study are presented in Section 6 to demonstrate the potential and feasibility of the proposed model to support decision making in $\mathsf { P } ^ { 3 }$ automation. After a further discussion of the signi<sup>fi</sup>cance of ${ \bar { \mathsf { P } } } ^ { 3 } ,$ , we end this paper in Section 7 by pointing out the limitations and the corresponding potential avenues for future research.

## 2. Process platform planning

In the literature, a product family is represented by a generic product structure (GPdS; e.g. [3]). From a design perspective, the GPdS essentially captures all data describing common and optional product components and their relationships. Similarly, a process family can be represented by a generic process structure (GPcS; [25]). As with the GPdS, the GPcS captures process data de<sup>fi</sup>ning common and optional operations, manufacturing resources, and relationships among them. Based on the interconnections between product and process data, the GPdS and the GPcS pertaining to a product family can be integrated into one uni<sup>fi</sup>ed structure: the generic routing structure (GRS; [26]). Hence, the GRS models both the product and process data and their relationships involved in a product family. The inclusion of all these necessary data and relationships enables the GRS to act as a generic umbrella, under which production processes can be planned for product family members. Thus, planning production processes for diverse products is anchored to one platform, which helps realize the bene<sup>fi</sup>t of design similarity in production.

Within the GRS, $\mathsf { P } ^ { 3 }$ entails 1) specifying product variants from the design perspective and 2) determining the corresponding production processes from the production perspective, as shown in Fig. 1. In the design view, $\mathrm { P } ^ { 3 }$ is characterized by the GPdS involving a set of design parameters, constraints among parameters, component items, and relationships among items. The valid combinations of different parameter values de<sup>fi</sup>ne product variants (i.e., end-products). These end-products consist of speci<sup>fi</sup>c component items, which are either primary or secondary. Unlike a secondary item, a primary item cannot be decomposed into child items, and itself is a child item of a secondary item. In this regard, an end-product is a special secondary item having no parent item. The variants of a secondary item are determined by the variations of its child items. Moreover, some product items (be they primary or secondary) are common to all product variants in the family, while some are optional and appear in several, but not all, product variants. Same as the end-product family, an item family is characterized by a set of parameters. The different combinations of parameter values are associated with different item variants. With a mechanism of parameter propagation [3], the parameter values of items are determined based on these of end-products. In other words, the parameters of end-products propagate from parent items to child items along the hierarchy of the GPdS. And the parameter values of a parent item determine these of its child items.

In the production view, $\mathrm { P } ^ { 3 }$ is characterized by the GPcS. As a generic data structure of the process family, the GPcS is a tree involving processes, sequence relationships, operations, and operations precedence. The processes are associated with component items located in the GPdS. More speci<sup>fi</sup>cally, a process is to produce a parent item by taking several child items as input. These processes are connected by sequence relationships (i.e., one process has to be completed before the start of another process). In accordance with the common and optional items in the GPdS, some processes are necessary to produce all product variants, whereas some are optional. Accordingly, the sequence relationships can be either <sup>fi</sup>xed indicating the associated processes are necessary for all product variants, or variable suggesting the processes concerned are not involved in the production of all product variants. While these processes are abstract concepts, they are detailed by operations and operations precedence. Unlike the output of processes, the outputs of some operations are pseudo items, which cannot be found in the GPdS. As with a sequence relationship between two processes, an operations precedence demands that the following operation cannot be started without the completion of the proceeding operation. Same as the processes, some operations are necessary to all item variants in a family and some are optional. This is in accordance with the variations among item variants.

With the above understanding, planning a speci<sup>fi</sup>c production process involves two phases: product variant speci<sup>fi</sup>cation and production process determination. With given customer requirements, a user (e.g., a designer) assigns values to parameters, resulting in a list of compatible parameter value pairs de<sup>fi</sup>ning an end-product. These parameter values then propagate along the GPdS hierarchy, determining parameter values of component items. Each item is instantiated according to the parameter values obtained from parameter propagation. Item instantiation leads to a speci<sup>fi</sup>c hierarchy pertaining to the product variant. With item variants and their goesinto relationships, the processes, sequence relationships, operations, and operations precedence in the GPcS are instantiated. Such instantiation is accommodated by the interconnections between the GPdS and the GPcS and the conditions to include an operation or process. The instantiation results in a production process consisting of several groups of ordered operations for the product variant, with each group producing a component item.

![](/api/attachments/9A6QEFNY/fulltext/images/58eba49319655d5ad22b359bd2367db7847e2263904ef64ac31bb130d9c1a88d.jpg)  
Fig. 1. An overview of process platform planning

## 3. Graph rewriting systems-based P<sup>3</sup>

A graph rewriting system consists of two parts: graphs and graph transformations. A graph is used to represent system structure, and is constructed based on two graph elements: nodes and edges. While nodes represent objects/concepts, edges represent relationships among objects/concepts. Graph transformations change graphs from one form to another. Such transformations are enabled by parametric rewriting rules (also called production rules, or simply productions). A production consists of two parts: a left-hand-side (LHS) graph to be transformed and a right-hand-side (RHS) graph to be obtained. If a system is modeled as graphs, assuming that the productions are designed properly, as long as the user employs the designed productions to manipulate graphs, the graphs produced re<sup>fl</sup>ect the characteristics of the system.

## 3.1. Overview of graph rewriting system for P<sup>3</sup>

The graph rewriting system model of P<sup>3</sup> is developed in line with the unique features introduced in Section 2. Design parameters, compatible constraints, items, processes, and operations are represented as nodes. Relationships among them are represented as edges. Manipulations of items, processes, and operations are modeled as productions. The graph representing product family elements is adopted as a starting graph. The graph of a production process is transformed based on the starting graph by invoking proper productions. In addition to productions, control structures are involved in graph generation. Such structures de<sup>fi</sup>ne the execution order of productions.

Accordingly, developing the graph rewriting system-based P<sup>3</sup> model consists of two subtasks. In the <sup>fi</sup>rst subtask, a graph schema is designed to model all the above objects involved in P<sup>3</sup>. It consists of a set of entities common to graphs of production processes in the family and describes all the necessary types of nodes and edges, as well as their associated attributes. In the second subtask, the productions and control structures are programmed to manipulate graphs by reasoning about planning production processes for given product variants.

## 3.2. PROGRES specification

A number of languages can be used to specify a graph rewriting system, such as PAGG [6], FUJABA [5], and PROGRES [18,20]. As a multi-paradigm language, PROGRES is the most expressive and advanced formalism [21]. Thus, in this study, we adopt PROGRES to formalize the graph rewriting system-based $\mathsf { P } ^ { 3 }$ model by writing the corresponding speci<sup>fi</sup>cations. The readers are referred to [18,20] for PROGRES details.

In accordance with the strati<sup>fi</sup>ed character of PROGRES, we develop the graph rewriting system-based $\mathsf { P } ^ { 3 }$ by classifying models at three levels of abstraction. These models include meta models at the meta level, generic models at the family level, and instance models at the variant level. A meta model captures the abstraction of objects/ concepts and their relationships that are common to production processes planning for different product families. Such abstraction is speci<sup>fi</sup>ed by de<sup>fi</sup>ning the corresponding node classes and edge types. In addition, to generalize the graph manipulations that are common to all process families, the related graph transformations are de<sup>fi</sup>ned at this meta level. The generic model represents the uni-<sup>fi</sup>ed generic data structure of a process family, where family related elements are speci<sup>fi</sup>ed using node classes. The relationships among these elements are speci<sup>fi</sup>ed using edge types. A generic model can be de<sup>fi</sup>ned by adapting the relevant entities of the meta model to the speci<sup>fi</sup>c characteristics of the corresponding product and process families. The graphical representation of a generic model is called a family graph. A family graph can be transformed to variant graphs, which represent operations and operations precedence of speci<sup>fi</sup>c production processes. Essentially, these variant graphs are instance models. An instance model is thus composed of node instances (i.e., speci<sup>fi</sup>c nodes) together with edges. Last, in accordance with the fact that PROGRES is a strongly typed language, the attributes de<sup>fi</sup>ned in classes can be inherited to type-level entities and the attributes de<sup>fi</sup>ned in types can be inherited to instance-level entities [18,21].

Consistent with the PROGRES speci<sup>fi</sup>cation of graph rewriting systems, modeling $\mathrm { P } ^ { 3 }$ involves two phases: construction and application. During the construction stage, the meta model and graph transformations are <sup>fi</sup>rst de<sup>fi</sup>ned by classes and productions in the PROGRES formalism. To adapt the meta model to a speci<sup>fi</sup>c generic model, node types of the process family are speci<sup>fi</sup>ed from two different views: the design view and the production view. By emerging these speci<sup>fi</sup>c types with the classes and productions, the complete PROGRES speci<sup>fi</sup>cation of a particular process family is obtained. Being named as the design view family graph, the starting graph from the design view consists of design parameters, items, compatible constraints, goes into relationships, selection constraints, and relationships among them. The starting graph from the production view consists of processes, sequence relationships, operations, operations precedence, selection constraints, and relationships among them, and is named as the production view family graph.

During the application stage (shown in Fig. 2), users input the values for design parameters. The design view family graph is then rewritten according to the control structures pre-de<sup>fi</sup>ned in the construction stage. The result is a variant graph: graphical representation of a product variant in terms of its product hierarchy. The product hierarchy is then transferred to the production view in the form of items and their goes into relationships. Taking these items and goes into relationships as input, the production view family graph starts to transform according to the control structures. The resulting variant graph represents the production process for producing the product variant obtained earlier.

## 4. Meta models and graph transformations for $\mathbf { P } ^ { 3 }$

Applicable to production process planning for different product families, the meta model includes a class level graph schema and graph transformations, as shown in Fig. 3. The class level graph schema generalizes entities common to different process families and models them as node classes and edge types. Graph transformations model the dynamic behavior of $\mathrm { P } ^ { 3 } ,$ , where a number of productions, transactions, and control structures are involved.

![](/api/attachments/9A6QEFNY/fulltext/images/968589c1d63de75c1d8afc4ab1613fefe9abeff11d0a8fa5a5a273dd6dc2e32d.jpg)  
Fig. 2. Process platform planning based on graph rewriting systems

## 4.1. Class level graph schema

The class level of PROGRES graph schema contains all common entities of process families. It de<sup>fi</sup>nes all nodes and edge classes occurring in $\mathrm { P } ^ { 3 } .$ . As shown in Fig. $3 ( \mathsf { a } )$ , PPP\_OBJECT acts as the root of the class hierarchy. Two subclasses – DSGN\_OBJECT and PROD\_ OBJECT – are de<sup>fi</sup>ned to model two views: the design and production views. In the graphical representation of node classes and edge types in Fig. 3(a), boxes, dashed lines, and solid lines represent node classes, inheritance relationships, and edge types, respectively.

DSGN\_OBJECT is a superclass encompassing all entities occurring in the design view meta model. A de<sup>fi</sup>nes edge between PRODUCT and PARAMETER indicates that design parameters de<sup>fi</sup>ne products. The edge, valueOf. between PARAMETER and VALUE models the fact that a parameter can assume a number of values. The determination of parameter values de<sup>fi</sup>nes speci<sup>fi</sup>c products (i.e., product variants). An affects edge models the fact that a parameter, whose value is the antecedent of the value of another parameter, must be assigned a value before the value assignment of the latter parameter. While the former parameter is the affecting parameter, the latter one is the affected parameter. (See below the meaning of antecedent.) Assigned is a derived attribute of PARAMETER, indicating whether or not the value of this parameter has been selected (true) or not (false). The default value is false. When a suitable value is selected, it becomes true.

A node class, COMPATIBLE\_CONSTRAINT, is de<sup>fi</sup>ned to handle compatible constraints between parameter values. A COMPATIBLE\_ CONSTRAINT node connects the antecedent and consequent of the modeled compatible constraint with the edges antecedent and consequent, respectively. The derived attribute, AnteSelected, of COMPATIBLE\_CONSTRAINT is determined by the Selected attribute of its antecedent. A COMPATIBLE\_CONSTRAINT can be a REQUIRE\_ CONSTRAINT or an EXCLUDE\_CONSTRAINT. A REQUIRE\_CONSTRAINT models the following fact: if a value, $A _ { x } ^ { * }$ , of parameter A (the antecedent) is selected and assigned to A, the value, ${ B } _ { y } ^ { * } ,$ of parameter B (the consequent) must be selected for B. An EXCLUDE\_CONSTRAINT captures the following fact: i $\cdot _ { A _ { x } ^ { * } }$ is selected for $\mathsf { A } , B _ { y } ^ { * }$ must not be selected for B.

A GOES INTO\_RELATIONSHIP node class and an ITEM node class are de<sup>fi</sup>ned to model product items and the relationships among them. An ITEM can be a PRIMARY or SECONDARY one. Being represented by one or more PRIMARY\_VARIANT, a primary item cannot be further decomposed. A secondary item is the parent item of lower level child items that may be primary or secondary. A GOES INTO\_RELATIONSHIP can be a COMMON\_GIR or OPTIONAL\_GIR. While the COMMON\_GIR models these relationships between parent and child items that are common to all product variants, OPTIONAL\_GIR captures these appearing in several, but not all, product variants. To indicate a COMMON\_GIR, an attribute, included, is introduced as a meta attribute whose value is always true. The derived attribute, included, of OPTIONAL\_GIR is determined by parameters of parent items. The node class, SELECTIVE\_ RELATION-SHIP, de<sup>fi</sup>nes the relationships between primary items and their variants. The included attribute of a SELECTIVE\_RELATIONSHIP is instantiated according to the parameters of the associated primary item. A primary item variant is included in the product's structure when included=true.

![](/api/attachments/9A6QEFNY/fulltext/images/ba1054ce05e5cff6605227db16e80b69860de71437b447d30cb5e700a254671a.jpg)  
Fig. 3. PROGRES-based speci<sup>fi</sup>cation of process platform planning.

Two edge classes, toParent and toChild, are de<sup>fi</sup>ned to model the relationships among node classes, such as PRODUCT and GOES INTO\_RELATIONSHIP. A toParent edge links a GOES INTO\_RELATION-SHIP to the associated parent item. A toChild edge connects a GOES INTO\_RELATIONSHIP with the child item. In addition, a toParent edge links a SELECTIVE\_RELATIONSHIP to the primary item. And a toChild edge connects a SELECTIVE\_RELATIONSHIP with a primary item variant.

PROD\_OBJECT in Fig. 3(a) is a superclass covering all entities in the production view meta model. A node class, PROCESS, is de<sup>fi</sup>ned to model processes to produce parent items by taking child items as input. In this regard, two edge classes, produces and inputs, connect the ITEM node in the design view with the PROCESS node in the production view. A SEQUENCE\_RELATIONSHIP node class models the relationships between items' processes. In accordance with the common and optional goes into relationships in the design view meta model, a SEQUENCE\_RELATIONSHIP can be either a FIXED\_SR or VARIED\_SR. While FIXED\_SR models those sequence relationships common to all production processes of product variants, VARIED\_SR captures sequence variations, meaning the relevant sequence relationships are only assumed by production processes of several product variants. Similarly, a meta attribute, included, with a value true is introduced to FIXED\_SR, indicating the modeled sequence relationship appears in production processes of all product variants. The derived attribute, included, of VARIED\_SR is determined by the inclusion of the items to be produced. Two edge classes, toSucceeding and toPreceding, link SEQUENCE\_RELATIONSHIP with PROCESS. A production process of a product variant thus contains all processes and their sequence relationships.

An OPERATION node class is further de<sup>fi</sup>ned to model operations forming processes. An operation can be a STARTING or an INTERMEDIATE one. A starting operation is the <sup>fi</sup>rst one involved in a process, whereas an intermediate one can be any other operation including the last one. PRECEDENCE\_RELATIONSHIP models the precedence relationships between operations. It can be a FIXED\_PR modeling precedence relationships common to all processes in relation to all variants of an item family, or VARIED\_PR indicating operations variations. To model a FIXED\_PR, the meta attribute, included, with value true is introduced. To indicate a VARIED\_PR, the derived attribute, included, is determined by the previous operation. Two edge classes, toFollowing and toPrevious, connect PRECEDENCE\_ RELATIONSHIP with OPERATION, modeling the previous operation and the following operation. Another node class, INCLUSIVE\_ RELATIONSHIP, models the inclusion of a variant of a starting operation in a process. The included attribute of an INCLUSIVE\_RELATIONSHIP is determined by parameters of the item to be produced. Included=true indicates that a starting operation variant is included in the process.

## 4.2. Graph transformations

While the class level schema addresses the static part of graph rewriting system-based P<sup>3</sup>, graph transformations deal with the operational behavior. They are associated with productions, transactions,

(b) Processing a require constraint and control structures. Basic operations are modeled as productions. Involving a number of productions, complex operations are de<sup>fi</sup>ned as graph transactions, and are executed by following control structures.

Being independent of product families, some operations are de<sup>fi</sup>ned at the meta level. First, there should be operations to allow designers to assign values to parameters characterizing a product family. Second, for a parameter value being the antecedent of a compatible constraint, if it is selected, there should be operations to process the consequent according to the constraint. Third, there should be operations to delete items, primary item variants, and processes that are not included in the product variant graph and the production process graph. Fourth, there should be operations to 1) determine operations to be included in an item's process, and 2) delete operations and starting operations variants that are not in included in the production processes graph. Fig. 3(b) shows these operations.

Fig. 4(a) presents a production, AssignValue, designed for users to assign values to parameters by selecting an appropriate one from a number of alternatives. The dashed rectangles above and below the separator ::= de<sup>fi</sup>ne the LHS and RHS of the production, respectively. The rule can be applied only if all conditions are ful<sup>fi</sup>lled. The <sup>fi</sup>rst statement in the condition part is used to check whether the parameter has been assigned a value. The second statement ensures that 1) there is no affecting PARAMETER to which a value should be assigned before the value is assigned to this parameter or 2) the affecting parameters have been assigned values. Last, the third one is to check that the affected parameters have not been assigned values. If all condition statements hold true, the elements of the LHS in the family graph are replaced by the elements of the RHS. Those unselected values are thus removed from the graph and the node attribute receives its new value according to the transfer function.

Once a value is assigned to a parameter, it is necessary to check whether this assignment in<sup>fl</sup>uences the values of other parameters. If the assigned value is an antecedent of an exclude constraint, the consequent of the constraint should be deleted from those possible values of the affected parameter. Fig. 4(c) is a production designed to perform this operation. For aPara (an instance of PARAMETER) whose value has been assigned (indicated by the hollow fat arrow, valueAssigned), if there is a path from its assigned value to the consequent of an exclude constraint (indicated by the hollow fat arrow, toConsequentE), the consequent together with the constraint node will be removed. If the selected value is an antecedent of a required constraint, the Selected attribute of its consequent should be assigned a new value of true, and all other values will be deleted, as shown in Fig. 4(b). The hollow fat arrow, toConsequentR, with a cross between nodes ′2 and ′5 leads to those unselected values of the affected parameter. Consequently, both the constraint node and unselected values are removed.

Upon the completion of value assignment of parameters, all derived attributes in the design view family graph start to be evaluated. If an item is not to be included in its parent item, the corresponding node of this item will be deleted. Production, RemoveNot IncludedItem (Fig. 5(a)), models this operation. Similarly, if a variant is not to be instantiated for its primary item, the included attribute of the corresponding SELECTIVE\_RELATIONSHIP node should take on false and thus the associated PRIMARY\_VARIANT node is removed (Fig. 5(b)). In addition to these examples, other supplementary productions on the design view family graph have been de<sup>fi</sup>ned to determine a product variant. Among them, some are to transfer the graph of a product variant to its BOM-like graph for better representing component items and their relationships. They include Construct ParentChildConnection and ConstructPrimaryVariantConnection. See Appendix A for the list of these supplementary productions.

With product items and their relationships speci<sup>fi</sup>ed, the production view family graph starts evaluating the derived attributes of its nodes. For these items that are deleted from the design view family graph, the included attributes of the corresponding VARIED\_SR are false, leading to the deletion of the corresponding processes. A production, RemoveNotIncludedProc (Fig. 6(a)), is designed to carry out this operation, as shown in Fig. 6(a). Similarly, if an operation is not included in a process, the included attribute of the corresponding VARIED\_PR is evaluated to be false, thus the operation being deleted. The same goes for a STRATING\_VARIANT node, which is not instantiated. While evaluating the included attributes of VARIED\_SR for processes is based on items and the corresponding goes into relationships, evaluating the included attributes of VARIED\_PR for operations is based on previous operations, which are ultimately determined by parameter values of the associated items. Fig. 6(b) and (c) shows two productions modeling the above two operations, respectively. Besides, there are productions designed to perform such operations as testing and con<sup>fi</sup>rmation. And some are designed to obtain production processes' tree-like graphs. See Appendix B for the list of these productions.

production AssignValue (aPara: PARAMETER, aValue: VALUE) =  
![](/api/attachments/9A6QEFNY/fulltext/images/9448d0961c25005e2004d12543ac44e9b921e4a1932311edb39b6f1342a8b6d9.jpg)  
(a) Assigning values to a parameter  
(c) Processing an exclude constraint  
Fig. 4. Some examples of productions for the design view meta model

![](/api/attachments/9A6QEFNY/fulltext/images/fcbc9d05240104c59baa68693cb99552c5d8ee9ec7f393ee4cb76e7e25914c65.jpg)  
Fig. 5. Some examples of productions on the design view family graph.

## 4.3. Production process derivation

Due to the inherent complexity, transforming a family graph into a variant graph necessitates the execution of more than one production. In this regard, imperative control structures are a key to enforce the orders of production application [18]. The control structure shown in Fig. 7 is designed to manage the execution of productions for deriving production processes. It consists of two parts with the <sup>fi</sup>rst part deriving a product variant in Fig. 7(a) and the second part deriving the corresponding production process in Fig. 7(b).

First, a graph test on the design view family graph is performed, as shown in Fig. 7(a). A parameter, whose value has not been assigned, is selected. If there is no value-unassigned parameter preceding this selected parameter, the selected parameter and its allowable values are listed to users for them to choose. After obtaining the users' input (i.e., a selected value), a production, AssignValue, is applied to the family graph. If the selected value is the antecedent of certain constraints, these constraints will be processed. After processing the constraints, it goes back to process other value-unassigned parameters till every parameter obtains a value. With all the parameter values assigned, the control structure starts to determine component items to be included in the product variant. This operation is automatic in that both include conditions and parameter propagation have been modelled as derived attributes. Derived attributes of items are evaluated. Based on the evaluation result, all those un-included items and primary item variants are removed. The desired product variant graph is <sup>fi</sup>nally obtained.

Fig. 7(b) shows the control structure for production process derivation. As with the graph test on the design view family graph, a graph test is conducted on the production view family graph <sup>fi</sup>rst. An item, whose process has not been determined, is selected. If the process of its parent item has been determined, a process will be selected to produce this item. Once all the processes together with their sequence relationships have been determined for the corresponding items, the control structure will specify the operations and the starting operation variants to be removed from the production view family graph for each process. Similarly, determining processes and operations is automatic since include conditions have been modeled as derived attributes according to the goes into relationships of items and the parameter values of items, respectively. The production process graph is <sup>fi</sup>nally derived.

![](/api/attachments/9A6QEFNY/fulltext/images/5e51ba1cf308237bbe84d56a3226ac417cf84047be4096b51f52ec04652707e0.jpg)  
(a) Removing processes not included in the production process graph

![](/api/attachments/9A6QEFNY/fulltext/images/592b39b3427d843d9f45c77927faa031d5fcac1c8f52cb07977ad367cd25e2a1.jpg)  
(b) Removing operations not included in the production process graph  
(c) Removing starting operations variants not included  
Fig. 6. Some examples of productions on the production view family graph.

![](/api/attachments/9A6QEFNY/fulltext/images/d7d8996647a9816e0eec0b080934c5a00bdf284dd27cb737efd8be9481e609d8.jpg)  
Fig. 7. Control structures in support of process platform planning.

## 5. Generic models and family graphs

While a meta model acts as a general pattern, a generic model functions as the fundamental mechanism to support planning a process family for a speci<sup>fi</sup>c product family. Hence, meta models need to be transformed to generic models to enable the planning of speci<sup>fi</sup>c process families. To do so, all family speci<sup>fi</sup>c parameters, generic items, generic processes, and generic operations in the GRS of the process family are speci<sup>fi</sup>ed as node types. A node type declaration de<sup>fi</sup>nes the label of a group of nodes (i.e., node instances) and the node class to which it belongs. It also determines the static properties of node instances. The declaration is accomplished by de<sup>fi</sup>ning three kinds of attributes: the intrinsic, derived, and meta attributes. Fig. 8 shows some examples of node type de<sup>fi</sup>nitions for AssyProc4 Chair, AssyProc4Armrest, and MOp4Wheel. AssyProc4Chair (assembly process for chair) models a process family (i.e., a generic assembly process) assembling a chair family (i.e., a generic chair) from immediate child item families (i.e., generic child items). AssyProc4Armrest captures an assembly process family for an armrest family. MOp4Wheel models a machining operations family involved in manufacturing a wheel family. (Note, an armrest is one of the immediate child items of a chair.)

Intrinsic attributes have the values that are directly assigned and do not depend on the values of any other attribute. For example, in the assembly process family of the chair family, item\_toProduce, item#1\_ Input, proc#1\_Preceding, and proc#n\_Preceding are intrinsic attributes (in Fig. 8). An intrinsic attribute has a type-dependent initial value, which may be changed by performing a graph transformation. If an item is modeled as an intrinsic attribute, its default value can be set to be the initial value of the attribute. Unlike intrinsic attributes, meta attributes are the attributes that possess constant typedependent values. Thus, those attributes with values common to all family members can be assigned as meta attributes. This enables the handling of such node properties that have the same value for all instances of a given node type. For example, for the assembly process family of the chair family in Fig. 8, a statement that the value of a meta attribute, included, is true means that production processes of all chair variants assume a chair assembly process.

In determining component items, parameter propagation from parent nodes to child nodes is modeled by derived attributes. These attributes have node instance speci<sup>fi</sup>c values and change their values as a result of graph transformations performed. Similarly, with derived attributes, the corresponding processes can be determined to be included in production processes. For example, for the assembly process family of the armrest family in Fig. 8, whether or not an armrest assembly process is included depends on the fact: whether or not an armrest is involved in the chair variant. In this regard, the derived attributes of processes are associated with the relevant items. While determining items to be included is of top-down, specifying operations follows a bottom-up approach, that is, the inclusion of operations is determined based on that of previous operations. Such bottom-up speci<sup>fi</sup>cation is modeled by the derived attributes as well. For example, in MOp4Wheel, whether or not the machining operation to be included depends on the inclusion of its previous operation: FOp4Wheel (fabrication operation for wheel).

Node types together with associated edges comprise generic models of product and process families, which are represented as family graphs. The design view family graph consists of family speci<sup>fi</sup>c node types for parameters, values, compatible constraints, goes into relationships, items, primary item variants and selective relationships. The production view family graph includes family speci<sup>fi</sup>c node types for processes, operations, sequence relationships, starting operations variants, precedence relationships and inclusive relationships. Figs. 9 and 10 give examples of product and process families' speci<sup>fi</sup>cation in the textual form in terms of node type speci<sup>fi</sup>cations and the family graphs, respectively. (Due to space limitation, operations of the family graph in the production view are not shown in Fig. 10.) For illustrative simplicity without losing generality, operations pertaining to Proc4I are given in Fig. 11(a) and (b). In accordance with the modeled operations and precedence relationships, the node attributes in Fig. 11 have different meanings although the same notations are used.

```txt
236 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 001
node_type AssyProc4Chair : PROCESS
    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -
        -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -    -
        -        -        |          |          |          |          |          |          |          |          |          |          |          |          |
        |          |          |          |          |          |          |          |          |          |          |          |          |          |
        |          |          |          |          |          |          |          |          |          |          |          |          |          |
        |          |          |          |          |          |          |          |          |          |          |          |          |          |
        |          |          |          |          |          |          |          |          | the            |          |          |          |          |
        |          |          |          |          |          |          |          |          | the            |          |          |          |          |
        |          |          |          |          |          |          |          |          | the            | the           | this         | this         | this         |
        |          |          |          |          |          |          |          |          | the            | the           | this         | this         | this         |
        |          |          |          |          |          |          |          | the            | the           | the           | this         | this         | this         |
        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        |
        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        /        |
       /            \      /
      /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
     /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
      /            \
     (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )
       (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )
       (             )              (             )              (             )              (             )              (             )              (             )                              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )              (             )
       (             )              (             )              (             )              (             )              (             )              (             )                              (             )              (             )                              (             )                              (             )                              (             )                              (             )                              (             )
       (             )              (             )              (             )              (             )              (             )                              (             )                              (             )                              (             )                              (             )                              (             )                              (             )
       (             )              (             )              (             )              (             )                              (             )                              (             )                              (             )                              (             )                              (             )                              (             )
       (             )              (             )              (             )              (             )                              (             )                              (             )                              (             )                              (             )                              (             )                              (             )
       (             )              (             )              (             )              (             )                              (             )                            ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((             ))                        ((               ))
       (           ),
```  
Fig. 8. Some declaration examples of intrinsic, derived and meta attributes.

## 6. Case study

The proposed graph rewriting system-based $\mathrm { P } ^ { 3 }$ is applied to textile spindle production in an Indian company. (Due to the con<sup>fi</sup>dential concern, the company's name is not revealed and the original data is modi<sup>fi</sup>ed without losing the capability to highlight the characteristics of this study.) Although textile spindles are not very complicated products, the degree of their product complexity not only allows illustrative simplicity but also enables the case application to be representative enough. The fact that meta models in Section 4 are common to process platform planning of any product families highlights the importance in addressing generic models and instance models in application cases. Hence, in this case study, the focus is on the generic models of a spindle family and how production processes of spindle variants are derived based on family graphs in the generic models and graph transformations in the meta models.

## 6.1. Family graphs

From the design view, there are four design parameters characterizing the spindle family, including length, diameter, thread pitch, and chamfer in Table 1. The possible values of these parameters and their compatible constraints are also given in the table. A spindle is assembled from two immediate child items: shaftassy (shaft assembly) and rockerarmassy (rockerarm assembly). Both shaftassy and rockerarmassy are secondary items. (See all the secondary and primary items in Table 1.)

Based on the available product data and the company designers' domain knowledge, the generic model in the design view is constructed, including node type speci<sup>fi</sup>cations in the textual form in Fig. 12(a) and the corresponding family graph in Fig. 13(a).

From the production view, planning production processes for the spindle family involves a number of processes in accordance with the component items at different levels of the product hierarchies. Each of these processes is further detailed by operations together with operations precedence. Similarly, the production view generic model is constructed, capturing all process elements and their relationships. Figs. 12(b) and 13(b) show this generic model in the textual form and in the graphic representation, respectively. In addition, operations details for Proc4St (process for shaft) and for Proc4RA (process for rockerarmassy) are shown in Fig. 13(b).

## 6.2. Production process derivation

Essentially, the above family graphs are starting graphs of process platform planning for the spindle family. While family graphs concern all node labels, node attributes, and edge labels from the static structural perspective, other elements, such as productions and control structures, enable graph transformations from the dynamic perspective. Therefore, production process derivation entails a series of graph transformations. All production processes, which can be obtained by graph rewriting, form the process family to produce the spindle family.

Suppose a designer decides the following parameter values when de<sup>fi</sup>ning a spindle variant: length=50 mm, diameter=10 mm, thread pitch=1 mm, and chamfer=30°. With these input values, the $\mathrm { P } ^ { 3 }$ system <sup>fi</sup>rst generates the spindle variant and then the corresponding production process. Fig. 14(a) shows the spindle variant

: node type; —: toParent; - - ≥ : toChild; CC : compatible constraint; I, : the yth variant of the xth generic item; V : the yth value of the xth parameter; I : generic item; SLR : selective relationship; GIR : goes into relationship

(a) Family graph in the design view

![](/api/attachments/9A6QEFNY/fulltext/images/ec3069b5e5b78a90a9ce750523703ef4f7e62412b2ede14f5a826906e85981dd.jpg)

(b) Node type specifications in the design view  
```txt
004 009 012 025 036 048 057 068 079 090 101 113 124 135 146 157 168 179 190 201 212 223 234 245 256 267 278 289 299 309 320 331 342 353 364 375 386 397 408 419 430 441 452 463 474 485 496 507 518 529 540 551 562 573 584 595 606 617 628 639 650 661 672 683 694 705 716 727 738 749 760 771 782 793 804 815 826 837 848 859<|box_end|><|ref_start|>code_caption<|ref_end|><|rotate_up|>
<|box_start|>005 012 999 990<|box_end|><|ref_start|>algorithm<|ref_end|><|rotate_up|>
```  
Fig. 9. Node type speci<sup>fi</sup>cations and family graph for a product family.

in the design view. It results from removing all unselected items and item variants from the design view family graph in Fig. 13(a). The transformation of Figs. 13(a) to 14(a) thus demonstrates the graph rewriting process from a starting graph to a variant graph. The production process graph in Fig. 14(b) is derived by transforming the production view family graph in Fig. 13(b) based on the control structure in

Fig. 7(b). To better represent the textile spindle variant in terms of its BOM structure and the production process with respect to its tree structure, productions in Appendixes A and B (e.g., Construct ParentChildConnection, ConstructOrderedOperationsConnection) are applied to variant graphs in Fig. 14. The resulted BOM-like and tree-like graphs are shown in Fig. 15.

(a) Family graph in the production view

![](/api/attachments/9A6QEFNY/fulltext/images/bb2df022b0dfba75d74bf9b7b4da402e62ac02592d47b51e944502e71bd5c57c.jpg)  
(b) Node type specifications in the production view

```txt
node_type Proc4LL : PROCESS
    intrinsic A₂, A₃, A₄ := [undefined];
    meta A₁ := true;
end;
node_type SR _Pr oc I₁-LL : VARIED_SR
    derived A_B := [(f(self.-toSucceeding->Proc4LL)&f(self.-toSucceeding->Proc4LL))|false];
end;
node_type SR _Pr oc I₂-LL : VARIED_SR
    derived A_A := [(f(self.-toSucceeding->Proc4LL)&f(self.-toSucceeding->Proc4LL))|false];
end;
node_type SR _Pr oc I₃-LL : VARIED_SR
    meta A_A := true;
end;
node_type Proc4I₁ : PROCESS
    intrinsic A_c, A_d := [undefined];
    derived A_e := [f(self.-produce->I₁|false)];
    meta A_a := 1; /*1 operator is required for all variants.
    A_b := Proc4LL; /*The assembly process family for LL family succeeds all the variants.
end;
node_type Proc4I₃ : PROCESS
    intrinsic A_f, A_g, A_h := [undefined];
    meta A_i := true; /* all variants are included in production processes of the product family.
    A_j := Proc4LL; /*The assembly process family for LL family succeeds all the variants.
end;
node_type Proc4I₂ : PROCESS
    intrinsic A_u, A_v, A_w := [undefined];
    derived A_z := [f(self.-produce->I₂|false)];
    meta A_x := 3; /*3 operators are required for all variants.
    A_y := Proc4LL; /*The assembly process family for LL family succeeds all the variants.
end;
node_type SR _Pr oc I₁₁-I₁ : VARIED_SR
    derived A_D := [(f(self.-toSucceeding->Proc4I₁)&f(self.-toSucceeding->Proc4I₁₁))|false];
end;
node_type SR _Pr oc I₁₂-I₁ : VARIED_SR
    derived A_E := [(f(self.-toSucceeding->Proc4I₁)&f(self.-toSucceeding->Proc4I₁₂))|false];
end;
node_type Proc4I₁₁ : PROCESS
    intrinsic A_m, A_n := [undefined];
    derived A_l := [f(self.-produce->I₁₁|false)];
end;
node_type Proc4I₁₂ : PROCESS
    intrinsic A_p, A_q := [undefined];
    derived A_r := [f(self.-produce->I₁₂|false)];
end;
```  
Fig. 10. Node type speci<sup>fi</sup>cations and family graph for the corresponding process family.

(a) Family graph of operations of Proc4I11  
![](/api/attachments/9A6QEFNY/fulltext/images/ede31c74ad18073fe8ab3c56846b94ed6ea0c5c09e310dbda85a8b448ddce38d.jpg)

(b) Node type specifications for operations in the production view

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
node_type  $Op_{4}4I_{11}$  : INTERMEDIATE
    intrinsic  $A_{2}$ ,  $A_{3}$ ,  $A_{4} := [undefined]$ ;
    meta  $A_{1} := \underline{true}$ ;
end;
node_type  $PR\_Op_{3-4}^{t_{11}}$  : FIXED_PR
    meta  $A_{1} := \underline{true}$ ;
end;
node_type  $Op_{3}4I_{11}$  : INTERMEDIATE
    intrinsic  $A_{2}$ ,  $A_{3} := [undefined]$ ;
    meta  $A_{1} := \underline{true}$ ;
end;
node_type  $PR\_Op_{2-3}^{t_{11}}$  : VARIED_PR
    derived  $A_{1} := [f(Op_{2}4I_{11}.A_{3})|false]$ ;
end;
node_type  $Op_{2}4I_{11}$  : INTERMEDIATE
    intrinsic  $A_{1}$ ,  $A_{2} := [undefined]$ ;
    derived  $A_{3} := [f(PR\_Op_{1-2}^{t_{11}}.A_{1})|false]$ ;
    meta  $A_{4} := \underline{1}$ ;
end;
node_type  $PR\_Op_{1-2}^{t_{11}}$  : VARIED_PR
    derived  $A_{1} := [f(IR\_Op_{1-2}^{t_{11}}.A_{1})|false]$ ;
end;
</div>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
node_type PR _Op $_{i2}^{I_{11}}$ : VARIED_PR
derived A$_{1}$ := [f(IR _Op $_{i2}^{*}.A_{1}$)|false];
end;
node_type Op$_{1}$4I$_{11}$ : STARTING
intrinsic A$_{2}$, A$_{3}$, A$_{4}$:=[undefined];
meta A$_{1}$ := ture;
end;
node_type IR _Op $_{i1}^{*}$ : VARIED_SR
derived A$_{1}$ := [f(Op $_{i1}^{*}$ 4 I$_{11}$.A$_{1}$)|false];
end;
node_type IR _Op $_{i2}^{*}$ : VARIED_SR
derived A$_{1}$ := [f(Op $_{i2}^{*}$ 4 I$_{11}$.A$_{1}$)|false];
end;
node_type Op$_{i1}^{*}$ 4I$_{11}$ : STARTING_VARIANT
intrinsic A$_{2}$, A$_{3}$:=[undefined];
derived A$_{1}$ := [f(I$_{i11}^{*}.included$)|false];
end;
node_type Op$_{i2}^{*}$ 4I$_{12}$ : STARTING_VARIANT
intrinsic A$_{2}$, A$_{3}$:=[undefined];
derived A$_{1}$ := [f(I$_{i12}^{*}.included$)|false];
end;
</div>

Fig. 11. Node type speci<sup>fi</sup>cations and family graph for operations detailing Proc4I .

## 7. Discussions and conclusions

To stay competitive, companies strive to quickly offer diverse products at affordable costs. In this context, developing product families arises as a promising strategy for companies to offer the expected product variety while keeping the costs as low as possible. As pointed out in [12,13], successful product family development hinges on the ef<sup>fi</sup>ciencies of both design and production of product families. In the literature, many methodologies have been reported to support product family development. With focus on design-related issues, these methodologies may contribute to design ef<sup>fi</sup>ciency, while they make limited or no contribution to achieving product family production ef<sup>fi</sup>ciency. Due to the inherent limitations, traditional trial and errorbased planning approaches do not lend themselves to ef<sup>fi</sup>ciently produce customized products with the available manufacturing resources. As a result, new solutions need to be developed to plan production processes for producing families so as to achieve production ef<sup>fi</sup>ciency.

Parameters, values, compatible constraints and secondary and primary items.

<table><tr><td colspan="2">Elements in  $P^{3}$  for the textile spindle family</td></tr><tr><td>Parameter</td><td>Value</td></tr><tr><td>Length</td><td>45 mm, 50 mm</td></tr><tr><td>Diameter</td><td>10 mm, 12 mm</td></tr><tr><td>Thread pitch</td><td>1 mm, 2 mm</td></tr><tr><td>Chamfer</td><td> $30^{\circ}$ ,  $45^{\circ}$ </td></tr><tr><td>Compatible constraint</td><td>If diameter = 12 mm, then thread pitch = 1 mm.If thread pitch = 2 mm, then chamfer =  $30^{\circ}$ .If length = 45 mm, then diameter ≠ 12 mm.</td></tr><tr><td>Secondary items</td><td>Textile spindle, shaftassy, rockerarmassy.</td></tr><tr><td>Primary items</td><td>Shaft, needle, rockerarm, sleeve.</td></tr><tr><td>Common items</td><td>Shaft, needle, rockerarm, sleeve.</td></tr></table>

The new planning solutions should utilize the design similarities among product family members while addressing the production optimality of the family as a whole. Process platform planning appears to be a promising approach to planning production processes for product families. First, it allows planning production processes for diverse products to be based on a common platform, thus limiting the planning solution space. Second, it utilizes design similarities in planning, thus leading to process similarities. It is these process similarities that ensure production stability on shop <sup>fl</sup>oors.

```vhdl
(a) Node type specifications of the generic model in the design view

node_type Textile Spindle: PRODUCT
derived defined := false;
end;
node_type Length: PARAMETER
derived assigned := [f(self.<--valueOf-VALUE.Selected)|false];
end;
node_type L_D Constraint: EXCLUDE_CONSTRAINT
end;
node_type D_T Constraint, T_C Constraint: REQUIRE_CONSTRAINT
end;
node_type GIR1, GIR2: COMMON_GIR
derived included := true;
end;
node_type Shaftassy: SECONDARY
derived Length := [f(self.-toParent->Textile Spindle.Length)|false];
Diameter := [f(self.-toParent->Textile Spindle.Diameter)|false];
end;
node_type Rockerarmassy: SECONDARY
derived Length := [f(self.-toParent->Textile Spindle.Length)|false];
Diameter := [f(self.-toParent->Textile Spindle.Diameter)|false];
Thread pitch := [f(self.-toParent->Textile Spindle.Thread pitch)|false];
Chamfer := [f(self.-toParent->Textile Spindle.Chamfer)|false];
end;
node_type GIR11, GIR12, GIR21, GIR22: COMMON_GIR
derived included := true;
end;
node_type Shaft: PRIMARY
derived Length := [f(self.-toParent->Shaftassy.Length)|false];
Diameter := [f(self.-toParent->Shaftassy.Diameter)|false];
end;
...
node_type StV1, StV2, StV3, NdV1, NdV2, RaV1, SIV1, SIV2: PRIMARY_VARIANT
end;
node_type SLR111, SLR112, SLR113: OPTIONAL_SLR
derived included :=[(f(self.-toParent->Shaft.Length)&f(self.-toParent->Shaft.Diameter))|false];
end;
...
node_type SLR221: COMMON_SLR
meta included := true;
end;

(b) Node type specifications of the generic model in the production view

node_type Proc4TS: PROCESS
instrinsic item_toProduce := [undefined];
item#1_Input := [undefined];
item#2_Input := [undefined];
meta Proc_Succeeding := nil;
included := true;
end;
node_type SR1, SR2: FIXED_SR
derived included := true;
end;
node_type Proc4SA: PROCESS
instrinsic item_toProduce := [undefined];
item#1_Input := [undefined];
item#2_Input := [undefined];
meta Proc_Succeeding := Proc4ST;
included := true;
#ofOperator := 2;
end;
...
node_type SR11, SR12, SR21, SR22: FIXED_SR
derived included := true;
end;
node_type Proc4St: PROCESS
instrinsic item_toProduce := [undefined];
item#1_Input := [undefined];
meta included := true;
#ofOperator := 3;
end;
...
node_type MOp34St: INTERMEDIATE
instrinsic item_toProduce := [undefined];
item_Input := [undefined];
meta included := true;
#ofOperator := 1;
end;

node_type MOp24St: INTERMEDIATE
instrinsic item_toProduce := [undefined];
item_Input := [undefined];
derived included := [(f(PR_OpS_{t-2},included)|false);
end;
node_type MOp14St: STARTING
instrinsic item_toProduce := [undefined];
item_Input := [undefined];
derived included := true;
end;
node_type PR_OpS_{t-3}: VARIED_PR
derived included := [(f(IR_OpS_{t-1},included)|false];
end;
node_type PR_OpS_{t-3}: VARIED_PR
derived included := [(f(self.-toPrevious->MOp24St.included)|false);
end;
node_type PR_OpS_{t-3}: VARIED_PR
derived included := [(f(OpS_{t-2},4StV_{t-2},included)|OR)
f(OpS_{t-3},4StV_{t-3},included)|false];
end;
node_type IR_OpS_{t-3}: VARIED_IR
derived included := [(f(OpS_{t-3},4StV_{t-3},included)|false];
end;
...
node_type OpS_{t-3},4StV_{t-3}: STARTING_VARIANT
instrinsic item_toProduce := [underlined];
item_Input := [undefined];
derived included := [(f(StV_{t})|false]
end;
```

![](/api/attachments/9A6QEFNY/fulltext/images/0a7aff9f10175bf3db7de73eab4532b6143e96540eea6cbd8b2f65ddabd2972d.jpg)  
Fig. 13. Family graphs for textile spindles' process platform planning.

To support P<sup>3</sup> automation, this study develops a graph rewriting system-based model, addressing both the static structure of a process family and the dynamic process of its planning. The modeling is approached from two views: design and production. In the two views, P<sup>3</sup> is represented as the design and production view family graphs. These family graphs act as the starting graphs for graph transformations. Through such transformations, production process graphs are derived by executing productions according to prede<sup>fi</sup>ned control structures. Each production process graph represents the production process for producing the corresponding product variant. The proposed graph rewriting system-based P<sup>3</sup> is speci<sup>fi</sup>ed using PROGRES, which excels in modeling major aspects of P<sup>3</sup>. In addition, in line with the unique features of PROGRES, we de<sup>fi</sup>ne 1) meta models for family graphs by generalizing P<sup>3</sup> at a higher level, thus being independent of speci<sup>fi</sup>c process families, 2) generic models modeling all speci<sup>fi</sup>c elements pertaining to particular process families, and 3) obtain data structures describing production processes for product variants. The application of the proposed graph rewriting system-based P<sup>3</sup> to textile spindling production process planning demonstrates that it accommodates documenting the knowledge from existing design and planning practice. Besides, the graph rewriting system-based P<sup>3</sup> further accommodates knowledge reuse in an interactive environment, where users can select parameter values to de<sup>fi</sup>ne product variants. Therefore, it facilitates decision making in P<sup>3</sup> automation.

In view of its potential impacts on product family development, we discuss below the managerial implications associated with process platform planning. First, facilitating production process planning for diverse customized products, a process platform is supposed to be inherent in a product family. Essentially, there is a granularity implication regarding the number of process platforms to be planned for a product family. If more process platforms are planned for one product family, more stable production may be secured by setting up different groups of production facilities. Each group relates to a process platform and is used to produce a limited number of customized products in the family. As a result, the cost of such stable production is more investment in manufacturing resources, and the resulting additional direct/indirect labor costs, training costs, etc. On the contrary, if one process platform is planned for a product family regardless of the size of the family, the operation/activity repetition may not be suf<sup>fi</sup>- cient to exploit economy of scale in production since the product family may involve many process variations from one product to another. In this regard, to achieve the optimal performance, the proper number of process platforms should be determined before applying process form planning in production. Second, consistent with the de<sup>fi</sup>nition of process platforms, the products in consideration need to have multilevel BOM structures. Such typical products are electromechanical products (e.g., automobiles). In this regard, process platform planning may not bene<sup>fi</sup>t the production of electro products, which do not possess multilevel BOM structures (e.g., surface mount assemblies).

In accordance with the limitations recognized, we have identi<sup>fi</sup>ed the corresponding avenues for future research, as pointed out below. First, the graph rewriting system-based P<sup>3</sup> is developed based on one implicit assumption, that is, the product family has been designed. (Such assumption allows the organization of data pertaining to the product and process families as the GRS.) For a new product family design, the proposed model might not be suf<sup>fi</sup>cient to facilitate planning its process family. Accordingly, efforts may be geared to develop such models that allow planning process families for new product families. Second, in the proposed model, the parameters involved are implicitly assumed to be discrete. In practice, parameters are both discrete and continuous. In this regard, an extended model, where both discrete and continuous parameters are explicitly captured, might deserve further study. Third, in line with the granularity concern mentioned above, more efforts should be made in designing a comprehensive decision support model, which not only helps identify the suitable number of process platforms for a given product family, but also assists in planning production processes for product family members based on the right process platform. Last, viewed from a sales perspective, process family planning mainly involves the selection of appropriate options for functional features and the subsequent transformation of design parameters based on the selected options. In this regard, future research might also be directed to design a comprehensive graph rewriting system-based model, encompassing sales selection, design speci<sup>fi</sup>cation and production process planning. The ultimate goal is to facilitate automation of product family development and to enhance the interactions and negotiations among sales, design, and production.

(a) The variant <sub>g</sub> ra<sub>p</sub>h i n the desi <sub>g</sub> n vi ew  
( b ) The variant <sub>g</sub> ra<sub>p</sub>h i n the <sub>p</sub> rod uction vi ew  
![](/api/attachments/9A6QEFNY/fulltext/images/c536a650b9bed408c0d6dfd2ab446573d799c0a7aa09679b190754afcfa27800.jpg)  
Fi<sub>g.</sub> 14<sub>.</sub> Variant <sub>g</sub>ra<sub>p</sub>hs for a s<sub>p</sub>indle variant and its <sub>p</sub>roduction <sub>p</sub>rocess.

![](/api/attachments/9A6QEFNY/fulltext/images/e93a712c09ee9e26db32e04f0acabff6cc96d46aacd0c0dd2325a4f99ec968e2.jpg)

![](/api/attachments/9A6QEFNY/fulltext/images/8108cc03401a34bfd3989843a74267152cdc342675719a602bf3866bbc9c9eb5.jpg)  
(a) The BOM-like graph after graph transformations  
(b) The tree-like graph after graph transformations  
Fig. 15. The BOM structure and the production process tree derived by graph rewriting

Appendix A. Supplementary productions in the design view family graph transformations

Fig. A.2: A test of con<sup>fi</sup>rming no unassigned affecting parameter.  
path toConsequentR: VALUE → value = '1 => '3 in  
![](/api/attachments/9A6QEFNY/fulltext/images/f9ad7e1e823ed36ac1e9f5977ae521fce818801f8131d18cb7eee91accedf6d3.jpg)  
Fig. A.3: Path to the consequent of a required constraint.

![](/api/attachments/9A6QEFNY/fulltext/images/8d8892fe8eb6e78d8b13f8bde3618d36a93e7ea555eada875b9f72c0abd036a4.jpg)  
Fig. A.4: Changing a GOES INTO\_RELATIONSHIP node into a forms edge.

![](/api/attachments/9A6QEFNY/fulltext/images/51228a94a33f2045e44a2373ab118853be140dbb07c52e993e374fe061d5aa17.jpg)  
Fig. A.5: Changing a SELECTIVE\_RELATIONSHIP node into a primary item variant

Appendix B. Supplementary productions in the production view family graph transformations

![](/api/attachments/9A6QEFNY/fulltext/images/94bf0ad678fd210870e7702f9d235250fdf6acab94d57be3b6e8bf97d1545053.jpg)  
Fig. B.1: A test of <sup>fi</sup>nding process-undetermined item.

test ConfirmNoUnDeterminedSucceedingProc (aProc: PROCESS) [0:1] =

![](/api/attachments/9A6QEFNY/fulltext/images/db7f37ef08635f823c73f7cf1eff329dcc298d9ee02ff4fada974629c0f05bbe.jpg)  
Fig. B.2: A test of con<sup>fi</sup>rming no undetermined succeeding process.

test FindUnDeterminedFollowingOper(anOper: OPERATION) [0:1] =

![](/api/attachments/9A6QEFNY/fulltext/images/ddf4d86f5c1f75203963a64bbb07aa40c750aa3cd0c7f2b57efd093aa0e3b1cb.jpg)  
Fig. B.3: A test of <sup>fi</sup>nding undetermined following operation.

test ConfirmNoUnDeterminedFollowingOper(anOper: OPERATION) [0:1] =

![](/api/attachments/9A6QEFNY/fulltext/images/7be49ceb495091877138fdae3555f2630a9d903959c59fe9117935d642c76ba3.jpg)  
Fig. B.4: A test of con<sup>fi</sup>rming no undetermined following operation.

production ConstructSequencedProcessConnection =

![](/api/attachments/9A6QEFNY/fulltext/images/c8297318fd28bbfb938ec120bfe77a80eff2242be8ee88dddd4c55db86c39f58.jpg)

Fig. B.5: Changing a SEQUENCE\_RELATIONSHIP node into a precedes edge

production ConstructOrderedOperationsConnection =

![](/api/attachments/9A6QEFNY/fulltext/images/3cdee90949deb4d6bc8b4a5622ce84a69978c242ac93f1e93cbf2bb498fc39b0.jpg)  
Fig. B.6: Changing a PRECEDENCE\_RELATIONSHIP node into a goes to edge.

production RepresentStartingVariant :

![](/api/attachments/9A6QEFNY/fulltext/images/42d89818a13929f3f9108cfe1f47e26daac9ca2cfc61a25e4ce867ea93253fbd.jpg)  
Fig. B.7: Changing an INCLUSIVE\_RELATIONSHIP node into a starting operation variant.

## References

[1] T. AlGeddawy, H.A. ElMaraghy, Co-evolution hypotheses and model for manufactur ing planning, CIRP Annals — Manufacturing Technology 59 (1) (2010) 445–448.

[2] K. Bengtsson, B. Lennartson, C. Yuan, The origin of operations: interactions between the product and the manufacturing automation control system, in: Proceedings of the Thirteenth IFAC Symposium on Information Control Problems in Manuf, Moscow, Russia, 2009.

[3] X. Du, J. Jiao, M.M. Tseng, Architecture of product family: fundamentals and methodology, Concurrent Engineering: Research and Application 9 (4) (2001) 309–325.

[4] X. Du, J. Jiao, M.M. Tseng, Product family modeling and design support: an approach based on graph rewriting systems, Arti<sup>fi</sup>cial Intelligence for Engineering Design, Analysis and Manufacturing 16 (2) (2002) 103–120.

[5] T. Fischer, J. Niere, L. Torunski, A. Zundorf, Story diagrams: a new graph rewriting language based on the Uni<sup>fi</sup>ed Modeling Language and Java, in: Proceedings of the Sixth International Workshop on Theory and Application of Graph Transformations, Paderborn, Germany, Springer-Verlag, Berlin, 1999, pp. 296–309, (LNCS 1764).

[6] H. Gottler, J. Gunther, G. Nieskens, Use graph grammars to design CAD systems, in: Proceedings of the Fourth International Workshop on Graph Grammars and Their Application to Computer Science, Bremen, Germany, Springer-Verlag, Berlin. 1990 pp. 396-410 (LNCS 532)

[7] H.Z. Huang, Y.K. Gu, Development mode based on integration of product models and process models, Concurrent Engineering: Research and Applications 14 (1) (2006) 27–34.

[8] S.H. Huang, Q. Liu, R. Musa, Tolerance-based process plan evaluation using Monte Carlo simulation, International Journal of Production Research 42 (23) (2004) 4871–4891.

[9] J. Jiao, T.W. Simpson, Z. Siddique, Product family design and platform-based product development: a start-of-the-art review, Journal of Intelligent Manufacturing 18 (1) (2007) 5–297.

[10] J. Jiao, L. Zhang, S. Pokharel, Process platform planning for variety coordination from design to production in mass customization manufacturing, IEEE Transactions on Engineering Management 54 (1) (2007) 112–129.

[11] J. Jiao, L. Zhang, S. Pokharel, Z. He, Identifying generic routings for product families in mass customization production based on text mining and tree matching, Decision Support Systems 43 (3) (2007) 866–883.

[12] Y. Kristianto, A. Gunasekaran, P. Helo, M. Sandhu, A decision support system for integrating manufacturing and product design into the recon<sup>fi</sup>guration of the supply chain networks, Decision Support Systems 52 (4) (2012) 790–801.

[13] R. Kuttner, K. Karjust, Coordination of complex tasks of engineering product and manufacturing process optimization, Proceedings Estonian Academy of Sciences Engineering 12 (3-1) (2006) 163–175.

[14] H.J. Lee, J.K. Lee, An effective customization procedure with con<sup>fi</sup>gurable standard models, Decision Support Systems 41 (1) (2005) 262–278.

[15] B. Lennartson, K. Bengtsson, C. Yuan, K. Andersson, M. Fabian, P. Falkman, K. Akesson, Sequence planning for integrated product, process and automation design, IEEE Transaction on Automation Science and Engineering 7 (4) (2010) 791–802.

[16] M. Meyer, A.P. Lehnerd, The Power of Product Platform — Building Value and Cost Leadership, Free Press, New York, 1997.

[17] M.T. Michaelis, H. Johannesson, Platform approaches in manufacturing — considering integration with product platforms, in: Proceedings of the ASME 2011 International Design Engineering Technical Conferences & Computers and Information in Engineering Conference, Washington, USA, 2011.

[18] A. Schurr, PROGRES: a VHL-language based on graph grammars, in: Proceedings of the Fourth International Workshop on Graph Grammars and Their Application to Computer Science, Bremen, Germany, Springer-Verlag, Berlin, 1990, pp. 641–659, (LNCS 532).

[19] A. Schurr, A. Winter, A. Zundorf, Visual programming with graph rewriting systems, in: Proceedings of the Eleventh Int. IEEE Symposium on Visual Languages, Darmstadt, Germany, IEEE Computer Society Press, 1995, pp. 326–355.

[20] A. Schurr, A. Winter, A. Zundorf, PROGRES: language and environment, in: G. Rozenberg (Ed.), Handbook on Graph Grammars: Applications, Vol. 2, World Scienti<sup>fi</sup>c, Singapore, 1998, pp. 1–61.

[21] J. Szuba, Graphs and Graph Transformations in Design in Engineering. 2005, Ph.D. Thesis, Polish Academy of Sciences, Warsaw, Poland.

[22] K.W. Tong, C.K. Kwong, K.M. Yu, Intelligent process design system for the transfer molding of electronic packages, International Journal of Production Research 42 (10) (2004) 1911–1931.

[23] C.B. Williams, J.K. Allen, D.W. Rosen, F. Mistree, Designing platforms for customizable products and processes in markets of non-uniform demand, Concurrent Engineering: Research and Applications 15 (2) (2007) 201–216.

[24] L. Xu, Z. Li, S. Li, F. Tang, A decision support system for product design in concurrent engineering, Decision Support Systems 42 (4) (2007) 2029–2042.

[25] L. Zhang, Process Platform-based Production Con<sup>fi</sup>guration for Mass Customization. 2007, Ph.D. Thesis, Nanyang Technological University, Singapore.

[26] L. Zhang, B. Rodrigues, A tree uni<sup>fi</sup>cation approach to constructing generic processes, IIE Transactions 41 (10) (2009) 916–929.

[27] L. Zhang, Q. Xu, P. Helo, A methodology integrating Petri nets and knowledgebased systems to support process family planning, International Journal of Production Research 50 (12) (2012) 3192–3210.

[28] J. Zhao, S. Masood, An intelligent computer-aided assembly process planning system, International Journal of Advanced Manufacturing Technology 15 (5) (1999) 332–337.

Dr. Zhang is a Full Professor in the Department of Management at IESEG School of Management (LEM-CNRS), Lille-Paris, France. She obtained her BEng and Ph.D. degrees in Industrial Engineering in 1998 and 2007, respectively. Her research interests include mass customization, production con<sup>fi</sup>guration, supply chain management, integrated product family development and business process reengineering. On these areas, she has published a number of articles in international refereed journals, such as Decision Support Systems, IIE Transactions, IEEE Transactions on Engineering Management, International Journal of Production Research, etc.

Dr. Jiao is an Associate Professor of Design and Manufacturing Systems in the G.W. Woodruff School of Mechanical Engineering at Georgia Institute of Technology. Before joining Georgia Tech., he was Assistant Professor and then Associate Professor of Systems and Engineering Management in the School of Mechanical and Production Engineering at Nanyang Technological University in Singapore. He earned his Ph.D. in Industrial Engineering at Hong Kong University of Science & Technology, M.S. in Intelligent Manufacturing at Tianjin University, and B.S. in Mechanical Engineering at Tianjin University of Science & Technology in China. His research interests include design systems engineering, manufacturing systems, and intelligent decision making.
