---
otero_id: 21566
otero_key: "U2EX3XQ7"
title: "Model integration using SML"
authors: "Yao-Chuan Tsai"
year: "1998"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00065-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model integration using SML

Yao-Chuan Tsai )

Department of Business Administration, National Cheng Kung UniÕersity, Tainan 701, Taiwan

Received 30 July 1997; accepted 25 November 1997

## Abstract

Structured modeling language SML is a modeling language for the structured modeling framework, which representsŽ . the semantics as well as mathematical structure of a model. This paper extends some structured modeling concepts and defines SML schema operations for formalizing model integration. Executing any of the operations could possibly disrupt the integrity of an SML model schema. Some major propositions and several examples in the paper settle practically many of the open questions for the operations studied. This research not only contributes an operational approach to perform model integration in SML, but also allows us to understand how different kinds of schema edits can disrupt the formal correctness of SML, and what can be done about it. It helps lay the foundation for the future development of an incremental static semantic analyzer and smart schema-directed editor. q 1998 Elsevier Science B.V. All rights reserved.

Keywords: Model integration; Model management; Modeling language; Structured modeling; SML

## 1. Introduction

Modeling has been an active area of research in recent years. An important aspect of modeling is model management 3,21,32 . Model management<sup>w</sup> <sup>x</sup> includes the design and updating of models, and the modification of existing models so that they can be used for other applications. Therefore, one of the most important areas in model management is model integration 6,11 . Model integration is the process <sup>w</sup> <sup>x</sup> whereby individually developed sub-models are logically combined to create a larger unified model.

There are several reasons for integrating models. First, sub-models are simpler and more convenient to test and handle than a fully integrated model. Second, model composition by integration often leads to an improved understanding of the whole model itself by bringing attention to the relevant interactions among the sub-models. Third, integrated models are often needed to support applications of MS<sup>r</sup>OR in areas such as strategic analysis and decision making <sup>w</sup> <sup>x</sup> 6,12 .

Model integration is classified into two different types 18 : deep integration and functional integra-<sup>w</sup> <sup>x</sup> tion. Other names are definitional integration and procedural integration 20 , or structural integration<sup>w</sup> <sup>x</sup> and composition integration 22 . Deep integration is <sup>w</sup> <sup>x</sup> the process of modifying as well as combining two or more given models into a single new model. Functional integration, however, leaves the given models unchanged, but connects them and directs models’ output to other models’ input while specifying the sequence of computations.

Deep integration is a difficult task 6,18 . Models<sup>w</sup> <sup>x</sup> that are not developed as modules are not easily combined to form other models as the need arises <sup>w</sup> <sup>x</sup> 26,27 . Recognizing the potential advantages of modularity, Gagliardi and Spera 9,10 formalize<sup>w</sup> <sup>x</sup> some procedures for deep integration in terms of the formal structured modeling framework, while using an object oriented language, BLOOMS 8 , to pre- <sup>w</sup> <sup>x</sup> sent examples. Geoffrion 14 proposed a five-step<sup>w</sup> <sup>x</sup> manual approach for integrating two structured models schemas written in SML structured modeling Ž language , where each participating schema can be. viewed as a module.

It is noted in Refs. 6,18 that structured model- <sup>w</sup> <sup>x</sup> ing, as a lingua franca, can be used widely in many different applications, and therefore simplify model integration. There are several choices of modeling languages for structured modeling: SML 17 , LSM<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w</sup> <sup>x</sup> 4 , and the graph based language 19 . This paper adopts SML as a model definition language due to its notable characteristics mentioned in Refs. <sup>w</sup> <sup>x</sup> 16,17,24 . SML is an executable language which is an important characteristic in today’s modeling systems 1,16 . Gagliardi and Spera 9 pointed out that<sup>w</sup> <sup>x</sup> <sup>w x</sup> effective integration procedures need to be defined as parts of a Model Management System, and to be consistent with language used in the system. In addition, model integration using SML has an advantage in that the closedness and acyclicity properties can be implied by simply checking the monotonicity property of an SML schema. This is discussed in the subsequent sections.

This paper discusses deep integration in SML. Our effort is to develop as much as automated procedures to perform model integration. We presume that the reader should know that an SML model consists of a schema and elemental detail tables, that a schema represents a structured model’s general structure, and that elemental detail tables instantiate a model schema to a specific model instance. The purpose of the paper is to formalize operations on a schema or on a pair of schemata that are of special interest for model integration, and to study in detail the effects of the operations to the static semantics of a SML schema. Some major propositions and several examples are given in the paper.

The paper is organized as follows. Section 2 defines the notion of a normal schema, and gives other necessary definitions. Section 3 then proposes the schema operations and presents an illustrative example. Section 4 validates the schema operations. Finally, in Section 5, the contributions and future research are briefly discussed.

## 2. Preparatory definitions

This section presents the theoretical foundations for developing schema operations. The reader is presumed to be familiar with the formal aspects of structured modeling 12,13 and SML 17 .<sup>w</sup> <sup>x</sup> <sup>w x</sup>

## 2.1. Normal schema definition

A schema must be syntactically correct. Besides this, a schema must satisfy certain properties so as to be valid 15 . To simplify the model integration<sup>w</sup> <sup>x</sup> process, we will use the following four important properties that any valid schema must satisfy. These properties reflect the integrity of the structured modeling framework.

The first is the property of calling sequence legitimacy: no primitive entity genus may have a calling sequence, and no compound entity genus or attribute genus may call an attribute including variable at-Ž tribute , function or test genus. .

The second is uniqueness of genus names. Genus names must be distinct within a valid schema. This avoids confusion and a genus can be referenced uniquely by its name.

The third is the non-emptiness property of all modules. Each module contains at least one genus. In a valid schema, each module paragraph must have at least one genus paragraph descendent.

The last property is that of monotonicity of the modular outline. A modular outline is a representation of modular structure. Monotonicity of the modular outline means that every generic calling sequence is allowed to call only preceding genera in the modular outline.

The monotonicity property of the modular outline implies the acyclicity and closedness properties of genera. The acyclicity property of genera means that no subset of genera $\mathbf { G } _ { 1 } , \mathbf { G } _ { 2 } , \ldots , \mathbf { G } _ { n }$ can be arranged in a cycle $\{ \mathbf { G } _ { 1 } , \mathbf { G } _ { 2 } , \ldots , \mathbf { G } _ { m } \}$ such that $\mathbf { G } _ { 1 }$ calls ${ \bf G } _ { 2 }$ ${ \bf G } _ { 2 }$ calls $\mathrm { G } _ { 3 } , \ldots , \mathrm { G } _ { m - 1 }$ calls $\mathbf { G } _ { m } = \mathbf { G } _ { 1 }$ , where n is the total number of genera within a schema and $2 ~ \leq ~ m ~ \leq ~ n .$ . The closedness property of genera means that for each genus in a schema, all genera in the calling sequence of that genus are also in the schema. It is possible that, however, the acyclicity and closedness properties of genera are satisfied, and yet a given modular outline may not satisfy monotonicity.

For example, in Fig. 1, schema &MODEL\_A satisfies monotonicity of the modular outline, acyclicity and closedness of genera. Both schemata &MODEL\_B and &MODEL\_C satisfy acyclicity

(a)

&MODEL\_A &MOD1 C /pe/ D(C) /ce/ &MOD2 A /pe/ B(D) /ce/

(b)

&MODEL\_B &MOD2 A /pe/ B(D) /ce/ &MOD1 C /pe/ D(C) /ce/

(c)

&MODEL\_C &MOD2 A /pe/ B(C) /ce/ &MOD1 C /pe/ D(A) /ce/

Fig. 1. a Satisfies monotonicity of the modular outline, acyclicity Ž . and closedness of genera. b and c Satisfy acyclicity and Ž . Ž . closedness of genera, but not monotonicity of the modular outline. A monotone ordering exists for b , but not for c .Ž . Ž .

and closedness of genera, but not monotonicity of the modular outline. A monotone ordering exists for schema &MODEL\_B: simply interchange sub-trees &MOD1 and &MOD2. For schema &MODEL\_C, since a topological sort does not succeed for the sibling set &MOD1, &MOD2 , a monotone order- 4 ing does not exist. The existence of a monotoneŽ ordering can be checked through a topological sort of each sibling set. See Lemma 2 in Section 4..

An important definition which will be referred to throughout the paper follows.

Definition 1. A normal schema is a schema that exhibits the four properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules, and monotonicity of the modular outline. A schema is abnormal if it is not normal. A schema is near-normal if it satisfies the properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules, acyclicity and closedness of genera but not necessarily monotonic- Ž ity of the modular outline ..

It should be noted that a near-normal schema with monotonicity of the modular outline is a normal schema.

## 2.2. Extended definitions and concepts

In structured modeling, primitive entity elements and compound entity elements are defined as elements that do not have a value; attribute, function and test elements are defined as elements that do have a value. We extend these definitions into the construct of two disjoint sets of elements.

Definition 2. Primitive entity and compound entity genera are entity genera; attribute, function and test genera are value genera. Elements within entity genera are entity elements; elements within value genera are value-bearing elements. For a given structured model, the finite collection of entity elements constitutes an entity elements set EES and the finiteŽ . collection of value-bearing elements constitutes a value-bearing elements set VES . Each element in aŽ . model must be a member of either EES or VES.

In the following definition, we introduce the idea of intension 25 that tends to be ignored by most <sup>w</sup> <sup>x</sup> modelers, largely because adequate formalisms and techniques for handling intensions have not been available.

Definition 3. The intended meaning of a genus is called its intension.

The problems of intension encountered here are synonyms and homonyms 2,23 . Synonyms occur<sup>w</sup> <sup>x</sup> when different genus names represent the same intension, and homonyms occur when genus names are the same but different things are intended. To avoid the confusions of synonyms and homonyms, it is assumed throughout this paper that genera within schemata to be integrated must be denoted by the same genus name if they share the same intension. Different genus names represent different intensions of genera.

Let us examine two genera, LINK and ITEM, that are defined in the transportation schema, &TRANS

Ž . Fig. 2 and the multi-item EOQ schema &MEOQ Ž . Fig. 3 , respectively. From the viewpoint of CUST Ž . customers, receivers , the genus ITEM represents any type of product or material that they might receive. The genus LINK represents the product, chairs for example, that is made in PLANTs and delivered to CUSTs. For integration purposes, a modeler may think of genus ITEM as representing the replenishment problems associated with all extant pairs of transportation links. To express this intension for genus ITEM explicitly, the modeler can edit &MEOQ by adding two primitive genera of PLANT and CUST and changing genus ITEM to be a genus LINK which is a compound entity genus defined on genera PLANT and CUST. The modified schema &MMEOQ is shown in Fig. 4.

Besides the same intensions of two genera, it is necessary to define other conditions in order for two genera to be ‘compatible’ for integration purposes.

<table><tr><td>&amp;TRANS</td></tr><tr><td>&amp;SDATA Source Data</td></tr><tr><td>PLANTI /pe/ There is a list of PLANTS.</td></tr><tr><td>SUP(PLANTI) /a/ {PLANT} : R+ Every PLANT has a SUPPLY CAPACITY measured in tons.</td></tr><tr><td>&amp;CDATA Customer Data</td></tr><tr><td>CUSTj /pe/ There is a list of CUSTOMERS.</td></tr><tr><td>DEM(CUSTj) /a/ {CUST} : R+ Every CUSTOMER has a non-negative DEMAND measured in tons.</td></tr><tr><td>&amp;TDATA Transportation Data</td></tr><tr><td>LINK(PLANTI, CUSTj) /ce/ Select {PLANT}x{CUST} where i covers {PLANT}, j covers {CUST} There are some transportation LINKS from PLANTS to CUSTOMERS. There must be at least one LINK incident to each PLANT, and at least one LINK incident to each CUSTOMER.</td></tr><tr><td>FLOW(LINKij) /va/ {LINK} : R+ There can be a non-negative transportation FLOW (in tons) over each LINK.</td></tr><tr><td>COST(LINKij) /a/ {LINK} Every LINK has a TRANSPORTATION COST RATE for use in $/ton.</td></tr><tr><td>$(COST, FLOW) /f/ ; SUMi SUMj (COSTij * FLOWij) There is a TOTAL COST associated with all FLOWS.</td></tr><tr><td>T:SUP(FLOWi., SUPi) /t/ {PLANT} ; SUMj (FLOWij) &lt;= SUPi Is the total FLOW leaving a PLANT less than or equal to its SUPPLY CAPACITY? This is called the SUPPLY TEST.</td></tr><tr><td>T:DEM(FLOW.j, DEMj) /t/ {CUST} ; SUMi (FLOWij) = DEMj Is the total FLOW arriving at a CUSTOMER exactly equal to its DEMAND? This is called the DEMAND TEST.</td></tr><tr><td>ITEMi /pe/ There is a list of ITEMS.</td></tr><tr><td>&amp;ITEMDATA Certain ITEM DATA are provided.</td></tr><tr><td>D(ITEMi) /a/ {ITEM} : R+ Every ITEM has a DEMAND RATE (units per year).</td></tr><tr><td>H(ITEMi) /a/ {ITEM} : R+ Every ITEM has a HOLDING COST RATE (dollars per unit per year).</td></tr><tr><td>F(ITEMi) /a/ {ITEM} : R+ Every ITEM has a FIXED SETUP COST (dollars per setup).</td></tr><tr><td>Q(ITEMi) /va/ {ITEM} : R+ The ORDER QUANTITY (units per order) for each ITEM is to be chosen.</td></tr><tr><td>&amp;OPCON OPERATING CONSEQUENCES following from ORDER QUANTITY choices.</td></tr><tr><td>FREQ(Di, Qi) /f/ {ITEM} ; Di / Qi Every ITEM has a SETUP FREQUENCY (average number of setups per year) equal to DEMAND RATE divided by ORDER QUANTITY.</td></tr><tr><td>SETUP$(FREQi, Fi) /f/ {ITEM} ; FREQi * Fi Every ITEM has an ANNUAL SETUP COST (dollars per year) equal to the SETUP FREQUENCY times the SETUP COST.</td></tr><tr><td>CARRY$(Hi, Qi) /f/ {ITEM} ; Hi * Qi / 2 Every ITEM has an ANNUAL CARRYING COST (dollars per year) equal to its HOLDING COST RATE times one-half of its ORDER QUANTITY (which estimates average inventory level).</td></tr><tr><td>ITEM$(SETUP$i, CARRY$i) /f/ {ITEM} ; SETUP$i + CARRY$i Every ITEM has an ANNUAL ITEM COST (dollars per year) equal to its ANNUAL SETUP COST plus its ANNUAL CARRYING COST.</td></tr><tr><td>TOT$(ITEM$) /f/ ; SUMi (ITEM$i) The TOTAL ANNUAL COST (dollars per year) is the sum of all ANNUAL ITEM COSTS.</td></tr></table>

Fig. 2. Transportation model schema &TRANS from Ref. 12 . Ž <sup>w</sup> <sup>x</sup>.

Fig. 3. Multi-item EOQ model schema &MEOQ from Ref. 12 . Ž <sup>w</sup> <sup>x</sup>.

Definition 4. Two genera are compatible if these conditions hold: 1 both genera have the same name; Ž . Ž . 2 both are entity genera or both are value genera; Ž . 3 both genera have the same symbolic index tuple if they are indexed alias indices are not considered Ž to be distinct ; 4 the respective index set statements . Ž . and generic calling sequences are consistent with a 1:1 correspondence of the elements in each genus; Ž . 5 the ranges of both genera are equivalent if both are attribute genera; 6 the domains as given in the Ž . Ž domain statement of both genera are equivalent if . both are self-indexed.

As an example, if it is assumed that condition 4Ž . holds, then genera PLANT, CUST, LINK and FLOW defined in &TRANS are compatible with genera PLANT, CUST, LINK and FLOW defined in &MMEOQ.

Calling sequence legitimacy among different genus types is formalized by a genus type hierarchy relationship as below.

Definition 5. There exists a hierarchy relationship on genus types for EES and VES. An entity genus type cannot be compared with a value genus type. The function type maps a genus into its genus type pe,Ž ce, a, va, f, or t . If . pe, ce, a, va, f and t are genera with genus type pe, ce, a, va, f and t, respectively, then the hierarchy has the following order:

$$
\operatorname{type} (\mathbf {p e}) <   \operatorname{type} (\mathbf {c e})
$$

$$
\operatorname{type} (\mathbf {a}) <   \operatorname{type} (\mathbf {v a}) <   \operatorname{type} (\mathbf {f}) = \operatorname{type} (\mathbf {t})
$$

$$
\begin{array}{l} \text {where <   means 'lower than' and = means 'equal to'.} \end{array}
$$

<table><tr><td>&amp;MMEOQ</td></tr><tr><td>PLANTi /pe/ There is a list of PLANTS.</td></tr><tr><td>CUSTj /pe/ There is a list of CUSTOMERS.</td></tr><tr><td>LINK(PLANTi, CUSTj) /ce/ Select {PLANT}x{CUST} where i covers {PLANT}, j covers {CUST} There are some transported LINK items from PLANTS to CUSTOMERS. There must be at least one LINK incident to each PLANT, and at least one LINK incident to each CUSTOMER.</td></tr><tr><td>&amp;ITEMDATA Certain ITEM DATA are provided.</td></tr><tr><td>FLOW(LINKij) /a/ {LINK} : R+ Every LINK has a non negative FLOW demand rate (units per year).</td></tr><tr><td>H(LINKij) /a/ {LINK} : R+ Every LINK has a HOLDING COST RATE (dollars per unit per year).</td></tr><tr><td>F(LINKij) /a/ {LINK} : R+ Every LINK has a FIXED SETUP COST (dollars per setup).</td></tr><tr><td>Q(LINKij) /va/ {LINK} : R+ The ORDER QUANTITY (units per order) for each LINK is to be chosen.</td></tr><tr><td>&amp;OPCON OPERATING CONSEQUENCES following from ORDER QUANTITY choices.</td></tr><tr><td>FREQ(FLOWij, Qij) /f/ {LINK} ; FLOWij / Qij Every LINK has a SETUP FREQUENCY (average number of setups per year) equal to DEMAND RATE divided by ORDER QUANTITY.</td></tr><tr><td>SETUPS(FREQij, Fij) /f/ {LINK} ; FREQij * Fij Every LINK has an ANNUAL SETUP COST (dollars per year) equal to the SETUP FREQUENCY times the SETUP COST.</td></tr><tr><td>CARRY$(Hij, Qij) /f/ {LINK} ; Hij * Qij / 2 Every LINK has an ANNUAL CARRYING COST (dollars per year) equal to its HOLDING COST RATE times one-half of its ORDER QUANTITY (which estimates average inventory level).</td></tr><tr><td>ITEMS(SETUPsij, CARRYsij) /f/ {LINK} ; SETUPsij + CARRYsij Every LINK has an ANNUAL ITEM COST (dollars per year) equal to its ANNUAL SETUP COST plus its ANNUAL CARRYING COST.</td></tr><tr><td>TOT$(ITEMS) /f/ ; SUMi SUMj (ITEMSij) The TOTAL ANNUAL COST (dollars per year) is the sum of all ANNUAL ITEM COSTS.</td></tr><tr><td>Fig. 4. Modified multi-item EOQ model schema &amp;MMEOQ.</td></tr></table>

The definition states that a primitive entity genus has a genus type order lower than a compound entity genus. An attribute genus has a genus type order lower than a function or test genus. Function and test genera have the same genus type order. Intuitively, without violating calling sequence legitimacy, a higher type genus can be defined on a lower type genus, but not vice versa. Genera with equal type orders can be defined by each other.

Genus type ordering is used in step 2 of the join operation to be developed in Section 3. When the join operation is applied to ‘merge’ two compatible genera, based on genus type ordering, the resulting genus has the same genus type as the highest level genus type from which it was created. Following this convention, it is shown in Section 4 that the schema created from the joining of a joinable pair preserves the property of calling sequence legitimacy.

## 3. Formalized schema operations

Section 2 has prepared the way for the formalization of schema operations. This section discusses the approach and develops operations for manipulating SML schemata.

## 3.1. Approach

To develop operations for manipulating SML schema, we first need to examine the characteristics of a SML schema.

A SML schema is a text representation of a structured model’s general structure. A schema consists of one module paragraph for each module and one genus paragraph for each genus, and paragraphs are arranged according to the modular outline associated with the ordered modular structure. Hence, a schema can be viewed as a tree. Each non-pe type genus paragraph has a calling sequence. Through the calling references among genera in a schema, there is an equivalent genus graph representation. Hence, a schema can be viewed alternatively as a genus graph.

If a schema is viewed as a tree, tree editing operations such as grow, cut and transplant can be used to create, delete and move paragraphs. If a schema is viewed as a genus graph, graph operations can be defined to formulate a new genus graph. A good approach therefore for manipulating schemata is to combine tree editing based on modular structure with graph operations based on the genus graph.

## 3.2. Proposed schema operations

An outliner 5 , which is available in several<sup>w</sup> <sup>x</sup> commercial packages like Framework IV 7 or Word 7.0 33 provides some tree editing capabilities. Sowa<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 25 defined some graph operations based on conceptual structures. The proposed operations combine both the features of an outliner and graph operations to provide powerful capabilities for the model integration process.

The proposed operations are divided into basic tree editing operations and derived operations. Basic tree editing operations are stated first, followed by derived operations.

## 3.2.1. Operation 1. Basic tree editing

The basic tree editing operations can change modular structure, generic structure or elemental structure.

Ž .a Create a genus paragraph. Introduce a new genus paragraph into a schema. This operation can be carried out either from scratch or by a ‘copy and change’ procedure.

Ž . b Create a module paragraph. Introduce a new module paragraph into a schema without creating any descendent paragraph.

Ž .c Delete a genus paragraph. Delete an unwanted genus paragraph from a schema.

Ž . d Delete a module paragraph, but not its descendent paragraphs. This operation entails moving all child sub-trees to sibling status with the unwanted module paragraph in a schema and then deleting the unwanted module paragraph.

Ž .e Move a genus paragraph.

Ž .f Move a module paragraph and its descendent paragraphs.

Ž . Ž . g Change create, delete, or modify a module paragraph by any combination of the following operations.

Ž . g1 Change a module name.

Ž . g2 Change module interpretation.

Ž . g2.1 Change a key phrase. This operation includes the change of either a defined key phrase or a referenced key phrase.

Ž . g2.2 Change non-key phrase text.

Ž . Ž . h Change create, delete and modify a genus paragraph by any combination of the following operations.

Ž . h1 Change a genus name.

Ž . Ž h2 Change an introduced index including alias index ..

Ž . h3 Change a calling sequence.

Ž . h4 Change a genus type.

Ž . h5 Change an index set statement.

Ž . h6 Change a domain statement.

Ž . h7 Change a range statement.

Ž . h8 Change a generic rule.

Ž . h9 Change genus interpretation.

Ž . h9.1 Change a key phrase. This operation includes the change of either a defined key phrase or a referenced key phrase.

Ž . h9.2 Change non-key phrase text.

These basic tree editing operations are exhaustive in the sense that everything one could possibly do to a schema can be described fully in terms of these operations.

The basic tree editing operations can be combined to create derived operations. The derived operations are short-cut operations that can improve system performance.

## 3.2.2. Operation 2. AdÕanced tree editing

The advanced tree editing operations provide more powerful functions than the basic tree editing operations 1 c , 1 d and 1 h .Ž . Ž . Ž .

Ž . Ž .a Globally change delete and replace a genus name, an index, or a key phrase in a schema. These three items may appear not only in genus names, introduced indices, and interpretations, but also in calling sequences, index set statements, domain statements, range statements and generic rules. The following operations a1, a2, and a3 are viewed in terms of Operations 1 h1 , 1 h2 , andŽ . Ž . 1 h9.1 , respectively.Ž .

Ž . a1 Globally change a genus name.

Ž . a2 Globally change an index.

Ž . a3 Globally change a key phrase.

Ž . b Delete all marked genus paragraphs. First, all the unwanted genus paragraphs are marked by a modeler; operation 1 c is then applied to deleteŽ . all marked genus paragraphs from a schema.

Ž .c Delete all module paragraphs which do not have any genus paragraph descendent. Use Operation 1 d .Ž .

The tree editing operations are useful for editing a schema. Some tree editing examples are the following.

<sup>Ø</sup> Edit a genus paragraph to better represent the concept being modeled.

<sup>Ø</sup> Edit a genus paragraph to make a genus compatible for a join operation.

<sup>Ø</sup> Rename an index to avoid duplications and possible confusion.

<sup>Ø</sup> Redirect calls by changing the calling sequence of a genus.

## 3.2.3. Operation 3. Projection

Schema u is a projection of schema v with respect to specified genera $\mathbf { a _ { 1 } } , \ \mathbf { a } _ { 2 } , \ldots , \ \mathbf { a } _ { n }$ of schema v, where n<sup>)</sup>0, if u can be obtained by the following procedure.

1. Mark all genus paragraphs in schema v whose corresponding genera are not called directly or indirectly by genera $\mathbf { a _ { 1 } } , \mathbf { a } _ { 2 } , \ldots , \mathbf { a } _ { n }$

2. Apply Operation 2 b to delete all marked genus Ž . paragraphs.

3. Apply Operation 2 c to delete, from the resulting Ž . schema of 2 , all module paragraphs which do Ž . not have any genus paragraph descendent.

The projection operation is viewed in terms of Operations 2 b and 2 c , but can be viewed alterna-Ž . Ž . tively in terms of Operations 1 c and 1 d .Ž . Ž .

The projection operation is useful for extracting a desired sub-model from a larger model for use in other applications. The modeler is responsible for specifying the genera for a projection operation. In the context of optimization, the specification usually is obvious. For example, genera ITEM\$ and Q are obvious choices in the Multi-Item EOQ Optimization Problem of ‘Choose Q such that ITEM\$ is minimized’.

To integrate two models or model classes, we first concatenate their corresponding schemata together. The following defines such a concatenation order.

Definition 6. A concatenation order < is defined on two schemata. Let M, N be two schemata; ‘M< N’ means that schema M comes before schema N in the concatenated modular outline when the two schemata are concatenated.

The following operations of concatenation and join are important operations for integrating two schemata.

## 3.2.4. Operation 4. Concatenation

Let v and w be two schemata. A concatenated schema u can be obtained by placing v and w in an arbitrary concatenation order.

The concatenation operation can be viewed in terms of Operation 1 f by moving a rooted tree toŽ . sibling status with another rooted tree.

Based on the compatibility relationships between two genera definition 4 , the joinability of two Ž . normal schemata can be defined as follows.

Definition 7. If two normal schemata have at least one compatible pair of genera not in the sameŽ schema and only the compatible pairs have the same. names, then the two schemata are a joinable pair. A joinable pair that has exactly one compatible pair of genera is a uniquely joinable pair.

For example, &TRANS and &MMEOQ are a joinable pair, but not a uniquely joinable pair because they have more than one compatible pair of genera, i.e., PLANT, CUST, LINK and FLOW.

## 3.2.5. Operation 5. Join

Let v and w be a joinable pair with $n > 0$ compatible pairs of genera such that genera $\mathbf { a _ { 1 } } , \mathbf { a } _ { 2 } , \ldots , \mathbf { a } _ { n }$ in schema v are compatible, respectively, with genera $\mathbf { b _ { 1 } } , \mathbf { b _ { 2 } } , \ldots , \mathbf { b _ { n } }$ in schema w. Schemata v and w may be joined to form a new schema u by performing the following procedure.

1. Apply Operation 4 to concatenate v and w in an arbitrary concatenation order. The result is a concatenated schema.

2. For each i, from 1 to n, apply Operation 1 c inŽ . the following cases.

Ž .a If $\mathrm { t y p e } ( \mathbf { a } _ { i } ) < \mathrm { t y p e } ( \mathbf { b } _ { i } )$ , then delete genus paragraph ${ \bf { a } } _ { i }$ from the concatenated schema.

Ž .b If $\mathrm { t y p e } ( \mathbf { b } _ { i } ) < \mathrm { t y p e } ( \mathbf { a } _ { i } )$ , then delete genus paragraph $\mathbf { { b } } _ { i }$ from the concatenated schema.

Ž . Ž . Ž . c If type a <sub>i i</sub><sup>s</sup> type b , and

1. If paragraph ${ \bf { a } } _ { i }$ comes before paragraph $\mathbf { { b } } _ { i }$ in the concatenated schema, then delete genus paragraph $\mathbf { { b } } _ { i }$ .

2. If paragraph $\mathbf { b } _ { i }$ comes before paragraph ${ \bf { a } } _ { i }$ in the concatenated schema, then delete genus paragraph ${ \bf { a } } _ { i }$

3. Apply Operation 2 c to delete, from the resulting Ž . schema of 2 , all module paragraphs which doŽ . not have any genus paragraph descendent.

The ordering of the compatible pairs of genera in step 2 is not significant. The join operation is viewed in terms of Operations 1 c , 2 c and 4, but can beŽ . Ž . viewed alternatively in terms of Operations 1 c , 1 dŽ . Ž . and 1 f .Ž .

It is possible that the joining of a joinable pair may result in a near-normal schema which violates monotonicity of the modular outline. The following three operations of topological reordering, default restructuring and heuristic restructuring deal with the problem of non-monotonicity for a near-normal schema. Topological reordering does not change the modular structure, but default restructuring and heuristic restructuring do change the modular structure.

## 3.2.6. Operation 6. Topological reordering

Let v be a near-normal schema that violates monotonicity of the modular outline. Assume that a monotone ordering of all sibling sets exists. The topological reordering operation repairs non-monotonicity by the following three-step procedure.

Ž . 1 Identification of sibling sets. Identify all the sibling sets in the modular outline of schema v.

Ž . 2 Topological sort on each sibling set. Obtain a topological labeling by doing a topological sort, based on the adjacency matrix, of each sibling set.

Ž .3 Manipulate the schema to achieve monotonicity. Note that each genus in a sibling set corresponds to a node a genus paragraph in the schema andŽ . each module in a sibling set corresponds to a sub-tree Ž . a module paragraph and its descendent paragraphs in the schema. For each sibling set, apply Operations 1 e move a genus paragraph and 1 f move aŽ . Ž . Ž . Ž module paragraph and its descendent paragraphs to . ‘permute’ paragraphs in the schema such that their corresponding topological labels are in an ascending order. For genera and modules with the same topological labels in the same sibling set, break ties arbitrarily the ordering among them is not signifi- Ž cant ..

In the topological sort of a sibling set, a module calls a genus if at least one of the genus descendants of the module calls the genus. A module calls a module if at least one of the genus descendants of the calling module calls some genus descendent of the called module. A genus calls a module if the genus calls at least one of the genus descendants of the module.

To do the necessary topological sort of a sibling set in 2 , perform the following steps. Ž .

Step 2a: Let the current sibling set be denoted by SIB where $\mathrm { S I B } = \{ \mathrm { S } _ { 1 } , ~ \mathrm { S } _ { 2 } , ~ \mathrm { S } _ { 3 } , . . . , ~ \mathrm { S } _ { n } \}$ , and every member of SIB is either a module or genus member. Let $k = 1 , i = 1$ , and num<sup>s</sup>n.

Step 2b: If num<sup>s</sup>0 then stop the topological sortŽ succeeds , or else go to the next step. .

Step 2c: If there exists a $\mathbf { S } _ { i } , i$ from 1 to num, that does not call any other member of SIB, then go to the next step; or else stop the topological sort fails .Ž .

Step 2d: For each i, from 1 to num: if $\mathbf { S } _ { i }$ does not call any other member of SIB, then label the member $\mathbf { S } _ { i }$ as $k ,$ delete $\mathbf { S } _ { i }$ from SIB, and set $n = n - 1$

Step 2e: Set $k = k + 1$ , num<sup>s</sup>n, and go to step 2b.

The topological reordering operation is viewed in terms of Operations 1 e and 1 f .Ž . Ž .

## 3.2.7. Operation 7. Default restructuring

Let v be a near-normal schema that violates monotonicity of the modular outline. Assume that a monotone ordering of all sibling sets does not exist. The default restructuring operation repairs nonmonotonicity by reorganizing a default modular structure with a monotone ordering by the following procedure.

Ž . Ž . 1 Apply Operation 1 d to delete all module paragraphs but not their descendent paragraphs , Ž . except the root paragraph from schema v. The resulting schema has only one sibling set other than the root.

Ž . Ž 2 Perform a topological reordering Operation 6 ..

The default restructuring operation inevitably destroys all of the original modules except for the root. In the following, a heuristic procedure is proposed for a near-normal schema that is created by joining a joinable pair, and is an attempt to preserve as much of the original modular structure as possible.

To explain the idea of the heuristic approach, it is assumed that u is a near-normal schema which is created by joining a joinable pair, v and w, where u violates modular outline monotonicity, a monotone ordering of all sibling sets does not exist, and sub-tree v comes before sub-tree w. For the integrated model u, if a genus B in sub-model v directly or indirectly calls a genus A in sub-model w, it implies that genus B is directly or indirectly defined on genus A. Then, genus A could be included in sub-model v. In the following procedure, genus A is included as an immediate descendent of module v.

## 3.2.8. Operation 8. Heuristic restructuring

Let u be a near-normal schema which is created by joining a joinable pair v and w. Assume that schema u violates monotonicity of the modular outline, that a monotone ordering of all sibling sets does not exist, and that sub-tree v comes before sub-tree w in schema u.

Ž . 1 For a genus in sub-tree v, if it directly or indirectly calls genera in sub-tree w, then move the corresponding genus paragraphs Operation 1 e ofŽ Ž .. those directly and indirectly called genera in sub-tree w to immediate descendent status of module paragraph v. Repeat until there is no genus in sub-tree v that directly or indirectly calls any genus in sub-tree w.

Ž . Ž 2 Perform a topological reordering Operation 6 . If a topological sort fails within this step, then. stop i.e., the heuristic restructuring operation fails .Ž .

Ž . Ž . 3 Apply Operation 2 c to delete all module paragraphs which do not have any genus paragraph descendent.

The default restructuring operation is viewed in terms of Operations 1 d and 6, but can be viewedŽ . alternatively in terms of Operations 1 d , 1 e andŽ . Ž . 1 f ; the heuristic restructuring operation is viewedŽ . in terms of Operations 1 e , 6 and 2 c , but can be Ž . Ž . viewed alternatively in terms of Operations 1 d , 1 eŽ . Ž . and 1 f .Ž .

## 3.3. An illustratiÕe example

All the operations developed in Section 3.2 are useful for integrating models. In the following example, however, only some operations are relevant.

An example of integrated modeling in Ref. 12<sup>w</sup> <sup>x</sup> juxtaposes the well known Hitchcock–Koopmans transportation model with the multi-item EOQ model. Assume that the transportation model is posed on an annualized basis. Solving the usual linear programming problem yields the ‘optimal’ annual flows, but does not prescribe how often shipment should be made or equivalently, what the shipment size should be. Frequent shipments lead to higher transportation costs, but also to lower inventory costs. To find the global optimal solutions of FLOW and Q that will minimize the total cost of \$ and TOT\$, the two models must be integrated.

Figs. 5 and 6 show the genus graphs for these schemata. By merging the LINK and ITEM genera as well as the FLOW and D genera, and by renaming the SETUP\$ genus to REC\$, the genus graph for the integrated model is created in Fig. 7.

To integrate the two models, the operations are applied to schemata &TRANS Fig. 2 and &MEOQ Ž . Ž . Ž Fig. 3 as follows we omit all the interpretation portions for the exhibited schemata in Figs. 8 and 9 and 11–13 ..

Ž . 1 Operation 1. Apply basic tree editing operations to edit schema &MEOQ so as to obtain schema &MMEOQ see Fig. 4 . This step adds two new Ž . genus paragraphs PLANT and CUST. Genus ITEM was defined on genera PLANT and CUST and was renamed as LINK, then genus name ITEM was globally renamed as LINK in the schema. Genus name D was globally renamed as FLOW. The original index i was globally changed to index tuple ij. The generic rule of paragraph TOT\$ was changed. The interpretations were updated.

![](/api/attachments/U2EX3XQ7/fulltext/images/a06cc4df53bfaacfc64577814b5582b5e8044750cc958cd8bdc073e74b7d9e86.jpg)  
Fig. 5. Genus graph for transportation model from Ref. 12 . Ž <sup>w</sup> <sup>x</sup>.

Ž . 2 Operation 5. Join schemata &TRANS and &MMEOQ on genera PLANT, CUST, LINK and FLOW. First, apply the concatenation operation by moving schema &TRANS the module paragraphŽ &TRANS and its descendent paragraphs to the end.

![](/api/attachments/U2EX3XQ7/fulltext/images/02bd1a2908b74f60d8c16b601ec824065a0a1378bf955459b15ae8e8be26b267.jpg)  
Fig. 6. Genus graph for multi-item EOQ model from Ref. 12 . Ž <sup>w</sup> <sup>x</sup>.

TOTCOST

![](/api/attachments/U2EX3XQ7/fulltext/images/dda7fb70c5c4d0342f9e9c768b5d3a752d612219f34c771a487e6c635e3bb87e.jpg)  
Fig. 7. Genus graph for integrated model. The dotted line extracts the projected multi-item EOQ sub-model from the integrated model.

of schema &MMEOQ in the modular outline. The concatenation order of the two schemata here is arbitrary. Second, merge the compatible genera PLANT by deleting genus paragraph PLANT in sub-tree &TRANS. Third, merge the compatible genera CUST by deleting genus paragraph CUST in sub-tree &TRANS. Fourth, merge the compatible genera LINK by deleting genus paragraph LINK in sub-tree &TRANS. Last, merge the compatible genera FLOW by deleting genus paragraph FLOW in sub-tree &MMEOQ see Fig. 8 .Ž .

The joined schema in Fig. 8 is a near-normal schema because it satisfies the properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules, acyclicity and closedness of genera. Observe that genus FREQ in sub-tree &MMEOQ calls genus FLOW in sub-tree &TRANS, and sub-tree &TRANS is below sub-tree &MMEOQ in the joined schema. Monotonicity of the modular outline is obviously violated. Moreover, a monotone ordering of all sibling sets does not exist because a topological sort does not succeed for the sibling set of &MMEOQ, &TRANS . A heuristic restructuring  4 operation is then applied in the next step.

```txt
&MMEOQ
PLANTi /pe/
CUSTj /pe/
LINK(PLANTi, CUSTj) /ce/
&ITEMDATA
H(LINKij) /a/ {LINK} : R+
F(LINKij) /a/ {LINK} : R+
Q(LINKij) /va/ {LINK} : R+
&OPCON
FREQ(FLOWij, Qij) /f/ {LINK} ; FLOWij / Qij
SETUP$(FREQij, Fij) /f/ {LINK} ; FREQij * Fij
CARRY$(Hij, Qij) /f/ {LINK} ; Hij * Qij / 2
ITEMS(SETUP$ij, CARRY$ij) /f/ {LINK} ; SETUP$ij + CARRY$ij
TOTS(ITEMS) /f/ ; SUMi SUMj (ITEMSij)
&TRANS
&SDATA
SUP(PLANTi) /a/ {PLANT} : R+
&CDATA
DEM(CUSTj) /a/ {CUST} : R+
&TDATA
FLOW(LINKij) /va/ {LINK} : R+
COST(LINKij) /a/ {LINK}
$(COST,FLOW) /f/ ; SUMi SUMj (COSTij * FLOWij)
T:SUP(FLOWi., SUPi) /t/ {PLANT} ; SUMj (FLOWij) <= SUPi
T:DEM(FLOW.j, DEMj) /t/ {CUST} ; SUMi (FLOWij) = DEMj
```  
Fig. 8. Join &TRANS and &MMEOQ based on PLANT, CUST, LINK and FLOW.

Ž . 3 Operation 8. Perform a heuristic restructuring operation as follows.

1. Move paragraph FLOW to a position between paragraphs TOT\$ &TRANS i.e., move to imme- Ž diate descendent status of module paragraph &MMEOQ see Fig. 9 .. Ž .

2. Perform a topological reordering.

2.1. Identify the sibling sets see Fig. 10 .Ž .

2.2. Topological sort on each sibling set see Fig. Ž 10 ..

2.3. Following the topological labels determined in step 2.2, move paragraph FLOW to a position between paragraph Q and paragraph &OPCON, and move paragraph CARRY\$ above paragraph FREQ see Fig. 11 . Ž .

## 3. Not applied here.

Ž . Ž . 4 Operation 2 a1 . Globally rename the SETUP\$ genus to REC\$. This step reinterprets a setup cost as a receiving cost see Fig. 12 .Ž .

Ž . Ž . 5 Operation 1 a . Create a genus paragraph TOTCOST at the very end of the integrated schema. The TOTCOST genus is a function genus whose purpose is to add the values of \$ and TOT\$ see Fig. Ž 13 ..

In the integration example, the monotonicity property of the integrated schema is violated in step 2. If in step 2, the two schemata were concatenated such that schema &TRANS comes before schema &MEOQ, then we would not have violated monotonicity of the modular outline. The heuristic restructuring operation in step 3 would not have been necessary. The ability to determine monotonicitypreserving concatenation order for schemata being joined is clearly worthwhile.

```txt
&MMEOQ
PLANTi /pe/
CUSTj /pe/
LINK(PLANTi, CUSTj) /ce/
&ITEMDATA
H(LINKij) /a/ {LINK} : R+
F(LINKij) /a/ {LINK} : R+
Q(LINKij) /va/ {LINK} : R+
&OPCON
FREQ(FLOWij, Qij) /f/ {LINK} ; FLOWij / Qij
SETUP$(FREQij, Fij) /f/ {LINK} ; FREQij * Fij
CARRY$(Hij, Qij) /f/ {LINK} ; Hij * Qij / 2
ITEM$(SETUP$ij, CARRY$ij) /f/ {LINK} ; SETUP$ij + CARRY$ij
TOTS(ITEMS) /f/ ; SUMi SUMj (ITEMSij)
FLOW(LINKij) /va/ {LINK} : R+
&TRANS
&SDATA
SUP(PLANTi) /a/ {PLANT} : R+
&CDATA
DEM(CUSTj) /a/ {CUST} : R+
&TDATA
COST(LINKij) /a/ {LINK}
$(COST,FLOW) /f/ ; SUMi SUMj (COSTij * FLOWij)
T:SUP(FLOWi., SUPi) /t/ {PLANT} ; SUMj (FLOWij) <= SUPi
T:DEM(FLOW.j, DEMj) /t/ {CUST} ; SUMi (FLOWij) = DEMj
```  
Fig. 9. Move paragraph FLOW to a position between paragraphs TOT\$ and &TRANS.

To illustrate the projection operation, we shall extract the multi-item EOQ model from the integrated model in the previous example. The first step is to identify the genera ITEM\$ and Q from the Multi-Item EOQ Optimization Problem ‘Choose Q such that ITEM\$ is minimized’. Project the integrated schema based on the genera Q and ITEM\$. The genera PLANT, CUST, LINK, FLOW, H, F, Q, FREQ, REC\$, CARRY\$, ITEM\$, and TOT\$ are extracted and the related modules are preserved. The dotted line portion of Fig. 7 shows the genus graph for the projected multi-item EOQ model. Then, by applying tree editing operations, a multi-item EOQ model schema can be obtained.

## 4. Validation of the schema operations

In applying the operations developed in Section 3 to normal schemata, it is important to determine whether those operations generate a new integrated schema that is also normal. This section studies the results of applying projection, join, topological reordering, default restructuring and heuristic restructuring operations to normal and near-normal schemata. The results of these schema operations are summarized in Fig. 14.

Proposition 1. Applying the projection operation to a normal schema yields a normal schema.

<table><tr><td>Sibling Sets</td><td>Topological Label</td></tr><tr><td>&amp;MMEOQ</td><td>1</td></tr><tr><td>&amp;TRANS</td><td>2</td></tr><tr><td>PLANT</td><td>1</td></tr><tr><td>CUST</td><td>1</td></tr><tr><td>LINK</td><td>1</td></tr><tr><td>&amp;ITEMDATA</td><td>2</td></tr><tr><td>Q</td><td>2</td></tr><tr><td>FLOW</td><td>2</td></tr><tr><td>&amp;OPCON</td><td>3</td></tr><tr><td>H</td><td>1</td></tr><tr><td>F</td><td>1</td></tr><tr><td>FREQ</td><td>1</td></tr><tr><td>CARRY$</td><td>1</td></tr><tr><td>SETUP$</td><td>2</td></tr><tr><td>ITEM$</td><td>3</td></tr><tr><td>TOT$</td><td>4</td></tr><tr><td>&amp;SDATA</td><td>1</td></tr><tr><td>&amp;CDATA</td><td>1</td></tr><tr><td>&amp;TDATA</td><td>1</td></tr><tr><td>$</td><td>2</td></tr><tr><td>T:SUP</td><td>2</td></tr><tr><td>T:DEM</td><td>2</td></tr><tr><td>SUP</td><td>1</td></tr><tr><td>DEM</td><td>1</td></tr><tr><td>COST</td><td>1</td></tr></table>

Fig. 10. Topological sort of each sibling set.

Proof. Under the first and second steps of projection, the new schema contains all the module paragraphs, and the genus paragraphs that correspond to the specified genera and the genera that are called directly or indirectly by the specified genera. No new genera are added. Thus, the properties of calling sequence legitimacy, uniqueness of genus names, monotonicity of the modular outline must hold. The third step of projection ensures the non-emptiness property of all modules.B

Proposition 2. Applying the join operation to a uniquely joinable pair yields a normal or near-normal schema.

Proof. Let schema u be created by joining a uniquely joinable pair v and w on compatible genera that are both named A. The first step of joining results in a concatenated schema. Without loss of generality we assume sub-tree v comes before sub-tree w in the modular outline.

Following the second step of the join operation, genus type ordering can be applied to ensure that the new schema will satisfy calling sequence legitimacy as described below.

Ž . 1 The join operation obviously preserves the schema property that a primitive entity genus will not call any other genus.

Ž . 2 For a normal schema, an attribute, function and test genus can only be called by function or test genera. 2a When a function or test genus is com- Ž . patible with an attribute genus, genus type ordering ensures that the resulting genus of the compatible pair is either a function genus or a test genus, not an attribute genus. This means that there is no way that an attribute genus of the joined schema could call another attribute, function or test genus. 2b Also Ž . since value genera cannot be compatible with entity genera, there is no possibility that a compound entity genus could call another attribute, function or test genus in the joined schema.

Thus, the property of calling sequence legitimacy is satisfied for the new schema.

Since there are only two compatible genera and, by the definition of uniquely joinable pair, no other pair of genera have the same names, the second step deletes one of the compatible genera and, thus, ensures uniqueness of genus names.

The third step deletes all the module paragraphs which do not have any genus paragraph descendent and, therefore, ensures the non-emptiness property of all modules in the joined schema.

After step 1 of the joining operation, the as- Ž . sumptions of normal schemata v and w imply acyclicity and closedness of genera within sub-trees v and w. If step 2 of the join operation causesŽ . paragraph A in sub-tree v to be deleted, any genus in sub-tree v that originally called the deleted genus A would be directed to call genus A in sub-tree w. Since genera in sub-tree w are acyclic and closed, there is no way of creating a loop in the joined schema. A similar argument deals with the case in which paragraph A in sub-tree w is deleted. Obviously, after step 2 , the union of two closed collec- Ž . tions of genera is still closed. Therefore, acyclicity and closedness of genera must be satisfied in the joined schema.

```txt
&MMEOQ
PLANTi /pe/
CUSTj /pe/
LINK(PLANTi,CUSTj) /ce/
&ITEMDATA
H(LINKij) /a/ {LINK} : R+
F(LINKij) /a/ {LINK} : R+
Q(LINKij) /va/ {LINK} : R+
FLOW(LINKij) /va/ {LINK} : R+
&OPCON
CARRY$(Hij, Qij) /f/ {LINK} ; Hij * Qij / 2
FREQ(FLOWij, Qij) /f/ {LINK} ; FLOWij / Qij
SETUPS(FREQij, Fij) /f/ {LINK} ; FREQij * Fij
ITEMS(SETUP$ij, CARRY$ij) /f/ {LINK} ; SETUP$ij + CARRY$ij
TOTS(ITEMS) /f/ ; SUMi SUMj (ITEMSij)
&TRANS
&SDATA
SUP(PLANTi) /a/ {PLANT} : R+
&CDATA
DEM(CUSTj) /a/ {CUST} : R+
&TDATA
COST(LINKij) /a/ {LINK}
$(COST,FLOW) /f/ ; SUMi SUMj (COSTij * FLOWij)
T:SUP(FLOWi., SUPi) /t/ {PLANT} ; SUMj (FLOWij) <= SUPi
T:DEM(FLOW.j, DEMj) /t/ {CUST} ; SUMi (FLOWij) = DEMj
```  
Fig. 11. Move paragraph FLOW to a position between paragraph Q and paragraph &OPCON, and move paragraph CARRY\$ above paragraph FREQ.

We have shown that, after the join operation, the properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules, acyclicity and closedness of genera still apply. Therefore, if monotonicity is true in the resulting schema, the schema is normal; otherwise the schema is near-normal.B

A monotone ordering of all sibling sets may or may not exist for a near-normal schema. The next lemma validates the following important result: a monotone ordering of all sibling sets always exists for a near-normal schema if the near-normal schema was created by joining a uniquely joinable pair.

Lemma 1. Let schema u be created by joining a uniquely joinable pair v and w on compatible genera

A. Then a monotone ordering of all sibling sets always exists for schema u without changing the modular structure.

Proof. The first step of joining is concatenation. We can assume without loss of generality that sub-tree v comes before sub-tree w.

If the join causes genus paragraph A in sub-tree w to be deleted, then schema u is still monotone.

If the join causes genus paragraph A in sub-tree v to be deleted, then interchange the order of sub-trees v and w; the resulting order for schema u is monotone.B

The following lemma is taken directly from Ref. <sup>w</sup> <sup>x</sup> 13 , Proposition 7, with a minor change to make it applicable to SML schemata for which elemental detail need not exist. The lemma presents a theoretical characterization of when a monotone ordering exists.

```txt
&MMEOQ
PLANTI /pe/
CUSTj /pe/
LINK(PLANTI,CUSTj) /ce/
&ITEMDATA
H(LINKij) /a/ {LINK} : R+
F(LINKij) /a/ {LINK} : R+
Q(LINKij) /va/ {LINK} : R+
FLOW(LINKij) /va/ {LINK} : R+
&OPCON
CARRY$(Hij, Qij) /f/ {LINK} ; Hij * Qij / 2
FREQ(FLOWij, Qij) /f/ {LINK} ; FLOWij / Qij
RECS(FREQij, Fij) /f/ {LINK} ; FREQij * Fij
ITEMS(RECSij, CARRY$ij) /f/ {LINK} ; REC$ij + CARRY$ij
TOTS(ITEMS) /f/ ; SUMi SUMj (ITEMSij)
&TRANS
&SDATA
SUP(PLANTI) /a/ {PLANT} : R+
&CDATA
DEM(CUSTj) /a/ {CUST} : R+
&TDATA
COST(LINKij) /a/ {LINK}
$(COST,FLOW) /f/ ; SUMi SUMj (COSTij * FLOWij)
T:SUP(FLOWi., SUPi) /t/ {PLANT} ; SUMj (FLOWij) <= SUPi
T:DEM(FLOW.j, DEMj) /t/ {CUST} ; SUMi (FLOWij) = DEMj
```  
Fig. 12. Globally rename SETUP\$ to REC\$.

Lemma 2. The following are equivalent for an SML schema whose modular structure is not necessarily monotone ordered:

Ž .i a monotone ordering exists;

Ž . ii the modular structure is acyclicity-preserving; Ž . iii for every sibling set of the modular structure tree, no subset of the siblings can be arranged in a sequence $\left\{ \mathbf { S } _ { 1 } , \ \mathbf { S } _ { 2 } , \ \mathbf { S } _ { 3 } , . . . , \ \mathbf { S } _ { n } \right\}$ such that some genus descendent of $\mathbf { S } _ { 1 }$ calls some genus descendent of $\mathbf { S } _ { 2 } , \hdots$ , some genus descendent of $\mathbf { S } _ { n - 1 }$ calls some genus descendent of $\mathbf { S } _ { n }$ , where $n > 1$ and ${ \sf S } _ { n } = { \sf S } _ { 1 }$

Proof. Omitted, see Ref. 13 .<sup>w</sup> <sup>x</sup> B

The constructive procedure used in the proof of Ž . iii is crystallized by a topological sort of each sibling set. From iiiŽ . Ž . ´ i , the existence of a monotone ordering for a schema can be easily checked by a topological sort of each sibling set. We use this lemma to validate the topological reordering and default restructuring operations in the following propositions.

Proposition 3. A near-normal schema which violates monotonicity of the modular outline can be converted to a normal schema by

1. applying the topological reordering operation if a monotone ordering of all sibling sets exists;

2. applying the default restructuring operation if a monotone ordering of all sibling sets does not exist.

Proof. Recall that a near-normal schema satisfies the properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules, acyclicity and closedness of genera.

```txt
&MMEOQ
PLANTI /pe/
CUSTj /pe/
LINK(PLANTI,CUSTj) /ce/
&ITEMDATA
H(LINKij) /a/ {LINK} : R+
F(LINKij) /a/ {LINK} : R+
Q(LINKij) /va/ {LINK} : R+
FLOW(LINKij) /va/ {LINK} : R+
&OPCON
CARRY$(Hij, Qij) /f/ {LINK} ; Hij * Qij / 2
FREQ(FLOWij, Qij) /f/ {LINK} ; FLOWij / Qij
RECS(FREQij, Fij) /f/ {LINK} ; FREQij * Fij
ITEMS(RECSij, CARRY$ij) /f/ {LINK} ; REC$ij + CARRY$ij
TOTS(ITEMS) /f/ ; SUMi SUMj (ITEMSij)
&TRANS
&SDATA
SUP(PLANTI) /a/ {PLANT} : R+
&CDATA
DEM(CUSTj) /a/ {CUST} : R+
&TDATA
COST(LINKij) /a/ {LINK}
$(COST,FLOW) /f/ ; SUMi SUMj (COSTij * FLOWij)
T:SUP(FLOWi., SUPi) /t/ {PLANT} ; SUMj (FLOWij) <= SUPi
T:DEM(FLOW.j, DEMj) /t/ {CUST} ; SUMi (FLOWij) = DEMj
TOTCOST($,TOT$) /f/ ; $ + TOTS
```  
Fig. 13. Create a genus paragraph TOTCOST.

Consider case 1, namely applying the topological reordering operation to a near-normal schema when a monotone ordering of all sibling sets exists. The topological reordering operation obviously cannot cause a loss of calling sequence legitimacy, uniqueness of genus names, or non-emptiness of all modules.

Step 1 of topological reordering identifies theŽ . sibling sets. Since a monotone ordering exists, by Lemma 2, iŽ . Ž . ´ iii , a topological sort must succeed for each sibling set in step 2 . Following the topo- Ž . logical labels determined in step 2 , step 3 manip-Ž . Ž . ulates the schema to achieve monotonicity.

We have shown that the properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules and monotonicity of the modular outline are satisfied. Thus, the resulting schema is normal.

Now consider case 2, namely applying the default restructuring operation to a near-normal schema when a monotone ordering of all sibling sets does not exist. Step 1 of default restructuring obviously Ž . cannot cause a loss of calling sequence legitimacy, uniqueness of genus names, acyclicity, or closedness of genera.

Step 1 of default restructuring reorganizes a Ž . default modular structure. The default module is clearly non-empty.

We will show that a monotone ordering exists for the resulting schema of step 1 .Ž .

After the first step, there are only two sibling sets for the new schema. One is the root module and the other is the collection of all genera. Since the first set has only one member, a topological sort must succeed for this sibling set. A topological sort must also succeed for the second set because the collection of all genera satisfies acyclicity. Thus, a topological sort succeeds for each sibling set. It follows from Lemma 2, iiiŽ . Ž . ´ i , that a monotone ordering must exist.

<table><tr><td>Input</td><td>Operation</td><td>Calling Sequence Legitimacy</td><td>Uniqueness</td><td>Non- emptiness</td><td>Monotonicity</td></tr><tr><td>A normal schema</td><td>Projection</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>A uniquely joinable pair</td><td>Join</td><td>Y</td><td>Y</td><td>Y</td><td>*(1)</td></tr><tr><td>A join lossless pair</td><td>Join</td><td>Y</td><td>Y</td><td>Y</td><td>*(2)</td></tr><tr><td>A joinable pair with n &gt; 1 compatible pairs of genera</td><td>Join</td><td>Y</td><td>Y</td><td>Y</td><td>*(3)</td></tr><tr><td>A near-normal schema (a monotone ordering exists)</td><td>Topological Reordering</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>A near-normal schema (a monotone ordering doesn&#x27;t exist)</td><td>Default Restructuring</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>A near-normal schema (a monotone ordering doesn&#x27;t exist)</td><td>Heuristic Restructuring</td><td>Y</td><td>Y</td><td>Y</td><td>*(4)</td></tr></table>

Fig. 14. The results of properties after the operations. ‘Y’ means that the property is preserved. ‘)’ means that the property may be lost. 1Ž . Acyclicity and closedness of genera must hold Proposition 2 , a monotone ordering must exist Lemma 1 . 2 Acyclicity and closedness of Ž . Ž . Ž . genera must hold Proposition 6 , a monotone ordering may or may not exist see example in Fig. 17 . 3 Acyclicity and closedness of Ž . Ž . Ž . genera may or may not hold, a monotone ordering may or may not exist see example in Fig. 16 . 4 Acyclicity and closedness of generaŽ . Ž . still hold, but a monotone ordering may or may not exist see example in Fig. 15 .Ž .

Therefore, the schema resulting from step 1 of Ž . the default restructuring operation is near-normal with a monotone ordering.

Step 2 of default restructuring applies a topolog-Ž . ical reordering to the resulting schema from step 1 . Ž . It follows from case 1 that the result is a normal schema.B

From the previous propositions, we can summarize the following important result.

Proposition 4. The combined application of the join and topological reordering operations on a uniquely joinable pair must result in a normal schema.

Proof. Follows immediately from Lemma 1 and Propositions 2 and 3.B

We now examine the behavior of heuristic restructuring. Assume that heuristic restructuring is applied to a near-normal schema which is created by joining a joinable pair. Assume that a monotone ordering does not exist for the near-normal schema.

Since heuristic restructuring does not add or delete genera, the properties of calling sequence legitimacy, uniqueness of genus names, acyclicity and closedness of genera clearly are preserved. Step 3 of Ž . heuristic restructuring ensures non-emptiness of all modules. However, heuristic restructuring does not promise monotonicity. Fig. 15 shows a counterexample. Thus heuristic restructuring cannot destroy near-normality, and may or may not achieve normality. It is possible that some other procedure can preserve much of the original modular structure and also attain monotonicity without fail. This is left for future research.

When the join operation is applied to a joinable pair with n<sup>)</sup>1 compatible pair of genera, unfortunately, acyclicity of genera may not even hold in the resulting schema. Hence, a near-normal schema would not be obtained and Proposition 3 would not apply. In Fig. 16, &MODEL\_1 and &MODEL\_2 are a joinable pair with two compatible pairs of (a1) &V (a2) &V1 A /pe/ B/pe/ C(A, B, F) /ce/ &W &W1 D(B) /ce/ E /pe/ &W2 F(D) /ce/ G /pe/

<table><tr><td>SIBLING SETS</td><td>TOPOLOGICAL SORT</td></tr><tr><td>&amp;V</td><td>X</td></tr><tr><td>&amp;W</td><td>X</td></tr><tr><td>&amp;V1</td><td>1</td></tr><tr><td>A</td><td>1</td></tr><tr><td>B</td><td>1</td></tr><tr><td>C</td><td>2</td></tr><tr><td>&amp;W1</td><td>1</td></tr><tr><td>D</td><td>1</td></tr><tr><td>E</td><td>1</td></tr><tr><td>&amp;W2</td><td>2</td></tr><tr><td>F</td><td>1</td></tr><tr><td>G</td><td>1</td></tr></table>

(b1) &V (b2)&V1A /pe/B/pe/C(A, B, F) /ce/F(D) /ce/D(B) /ce/&W&W1E /pe/&W2G /pe/

<table><tr><td>SIBLING SETS</td><td>TOPOLOGICAL SORT</td></tr><tr><td>&amp;V</td><td>1</td></tr><tr><td>&amp;W</td><td>1</td></tr><tr><td>&amp;V1</td><td>X</td></tr><tr><td>F</td><td>X</td></tr><tr><td>D</td><td>X</td></tr><tr><td>A</td><td>1</td></tr><tr><td>B</td><td>1</td></tr><tr><td>C</td><td>2</td></tr><tr><td>&amp;W1</td><td>1</td></tr><tr><td>E</td><td>1</td></tr><tr><td>&amp;W2</td><td>1</td></tr><tr><td>G</td><td>1</td></tr></table>

Fig. 15. $\left( \mathbf { a } _ { 1 } \right)$ Shows a near-normal schema without a monotone ordering before heuristic restructuring . For the schema in Ž . $( \mathbf { a } _ { 1 } ) , ( \mathbf { a } _ { 2 } )$ shows that a topological sort fails for the sibling set &V, &W . 4 $\left( \mathsf { b } _ { 1 } \right)$ Shows the resulting schema after the first step of heuristic restructuring is applied to $\left( \mathrm { a } _ { 1 } \right)$ . For the schema in $( \mathsf { b } _ { 1 } ) , ( \mathsf { b } _ { 2 } )$ shows that a topological sort fails for the sibling set &V1, F, D . Thus, heuristic restructuring  4 cannot generate a normal schema in this case.

genera A and B. By joining schemata &MODEL\_1 and &MODEL\_2 on genera A and B, a loop is formed in the joined schema &JOINED\_MODEL whereby genus A calls A1, A1 calls A2, A2 calls B, B calls B1, B1 calls B2, B2 calls A. This example shows that acyclicity of genera can be violated.

Theoretically, a loop can be created whenever we join a joinable pair with more than one compatible pair of genera. It is evident from the properties of calling sequence legitimacy that the only possible occasions for a loop to occur in the schema resulting from a join are when all the genera within the loop are either compound entity genera or test<sup>r</sup>function genera. In the first case, the concept of genus A is defined on the concept of genus B in the first sub-model, and the concept of genus B is defined on the concept of genus A in the second sub-model. We thus have a logical trap in the joined model since genus A and genus B are conceptually communicative. In the second case, where all the genera are function<sup>r</sup>test genera, a similar conceptual anomaly can exist and recursive calculations can be formed.

For a joinable pair, certain properties that ensure acyclicity and closedness of genera for the joined schema are defined as follows.

Definition 8. A joinable pair with $n > 0$ compatible pairs of genera, where CP , i<sup>s</sup>1, . . . , n denotes the ith compatible pair of genera, is join lossless if one of the following holds: 1Ž . Ž . n<sup>s</sup>1; 2 n<sup>)</sup>1 and no

&MODEL\_1 X /pe/ B/pe/ A2(B) /ce/ A1(A2) /ce/ A(A1) /ce/ C(A) /ce/

(b) &MODEL\_2 A /pe/ B2(A) /ce/ B1(B2) /ce/ B(B1) /ce/ D(B) /ce/

(c) &JOINED\_MODEL &MODEL\_1 X /pe/ A2(B) /ce/ A1(A2) /ce/ A(A1) /ce/ C(A) /ce/ &MODEL\_2 B2(A) /ce/ B1(B2) /ce/ B(B1) /ce/ D(B) /ce/

Fig. 16. a and b Show a joinable pair, &MODELŽ . Ž . \_1 and &MODEL\_2, with the compatible genera A and B. C After theŽ . joining of $\& \mathrm { M O D E L } _ { - } 1$ and &MODEL\_2, a loop exists such that A calls A1, A1 calls A2, A2 calls B, B calls B1, B1 calls B2, B2 calls A in the joined schema JOINED\_MODEL.

subset of the n compatible pairs of genera can be arranged in a cycle $\{ \mathrm { C P } _ { 1 } , \mathrm { C P } _ { 2 } , \ldots , \mathrm { C P } _ { m } = \mathrm { C P } _ { 1 } \}$ such that a genus in $\mathrm { C P _ { 1 } }$ calls a genus in $\mathrm { C P } _ { 2 }$ , a genus in $\mathrm { C P } _ { 2 }$ calls a genus in $\mathrm { C P } _ { 3 } , \ldots , \mathrm { a }$ genus in $\mathrm { C P } _ { n - 1 }$ calls a genus in $\mathrm { C P } _ { m } = \mathrm { C P } _ { 1 }$ , where $2 \leq m \leq n$

Case 1 , Ž . n <sup>s</sup> 1, implies that a uniquely joinable pair is join lossless. In Fig. 16, &MODEL\_1 and &MODEL\_2 is a joinable pair with two compatible pairs of genera A and B. A loop exists such that A calls A1, A1 calls A2, and A2 calls B in &MODEL\_1, and B calls B1, B1 calls B2, and B2 calls A in &MODEL\_2. Therefore, &MODEL\_1 and &MODEL\_2 are not join lossless.

Proposition 5. Applying the join operation to a join lossless pair yields a normal or near-normal schema.

Proof. Let the join lossless pair v and w have n compatible pairs of genera $\mathrm { C P } _ { i } ,$ where $1 \leq i \leq n$ and $\mathrm { C P } _ { i } = ( \mathbf { A } _ { i } , \ \mathbf { B } _ { i } )$ denotes the ith compatible pair of genera $\mathbf { A } _ { i }$ and $\mathbf { B } _ { i }$ in schemata v and w, respectively.

When $n = 1$ , the result follows immediately from Proposition 2.

When $n > 1$ , the first step of the join operation results in a concatenated schema. Following the second step of the join operation, genus type ordering can be applied to ensure that the new schema will have the property of calling sequence legitimacy. The detailed proof is the same as that in Proposition 2.

Since there are only n compatible pairs of genera and, by the definition of join lossless pair, no other pair of genera have the same names, the second step deletes n compatible genera i.e., delete one genus Ž from each compatible pair , and thus, ensures . uniqueness of genus names.

The third step deletes all the module paragraphs which do not have any genus paragraph descendent and, therefore, ensures the non-emptiness property of all modules in the joined schema.

After step 1 of the join operation, the assump- Ž . tions of normal schemata v and w imply acyclicity and closedness of genera in sub-trees v and w, respectively. From the definition of a join lossless pair, condition 2 , there is no subset of theŽ . n compatible pairs of genera which can be arranged in a cycle $\{ \mathrm { C P } _ { 1 } , \mathrm { C P } _ { 2 } , \ldots , \mathrm { C P } _ { m } = \mathrm { C P } _ { 1 } \}$ such that a genus in $\mathrm { C P _ { 1 } }$ calls a genus in $\mathrm { C P } _ { 2 }$ , a genus in $\mathrm { C P } _ { 2 }$ calls a genus in $\mathrm { C P } _ { 3 } , \ldots , { \mathrm { a } }$ genus in $\mathrm { C P } _ { m - 1 }$ calls a genus in $\mathrm { C P } _ { m } = \mathrm { C P } _ { 1 }$ , where $2 \leq m \leq n .$ . Step 2 of the joinŽ . operation deletes n genera from n compatible pairs Ž . one genus for each compatible pair . Thus, there is no way of creating a loop that contains any remaining genus of the n compatible pairs in the joined schema. Obviously, after step 2 , the union of two Ž . closed collections of genera is still closed. Hence, acyclicity and closedness of genera must be true for the joined schema.

It has been shown that, after the join operation, the properties of calling sequence legitimacy, uniqueness of genus names, non-emptiness of all modules, acyclicity and closedness of genera still apply. Therefore, if monotonicity is true in the resulting schema, the schema is normal; otherwise, the schema is near-normal.B

![](/api/attachments/U2EX3XQ7/fulltext/images/36c46e2eb5c9ff5c35473300f6a99f6b43fd01896c6d5b448cac1cf1ac3df33b.jpg)  
Fig. 17. Schemata &V and &W is a join lossless pair. A monotone ordering does not exist for the joined schema and &U.

Assume that near-normal schema u can be created by joining a join lossless pair v and w, and that sub-tree v comes before sub-tree w in the modular outline. A monotone ordering of all sibling sets may or may not exist for near-normal schema u. For a counterexample see Fig. 17 , if joining schemataŽ . v and w causes a paragraph A in sub-tree v and a paragraph B in sub-tree w to be deleted, any genus in sub-tree v that originally called the deleted genus A would be directed to call genus A in sub-tree w, and any genus in sub-tree w that originally called the deleted genus B would be directed to call genus B in sub-tree v. A topological sort must fail in the sibling set  4 v, w and a monotone ordering of all sibling sets may not exist. Therefore, the combined operations of join and topological reordering on a join lossless pair do not suffice to generate a normal schema.

Proposition 6. The operations of join, topological reordering and default restructuring are sufficient to generate an integrated normal schema from a join lossless pair.

Proof. From Proposition 5, the join operation generates a normal or near-normal schema from a join lossless pair. If the schema resulting from the join is near-normal with a monotone ordering, then topological reordering does suffice to convert it to a normal schema Proposition 3.1 . If the resulting schema isŽ . near-normal without a monotone ordering, then applying the default restructuring operation to the resulting schema results in a normal schema Proposi-Ž tion 3.2 .. B

## 5. Conclusions

The paper extends some structured modeling concepts and defines schema operations for formalizing model integration. We start with basic tree editing operations on an SML schema, followed by derived operations. The most significant operations are projection Žto extract a desired sub-model from a larger model for use in other application ,. Ž join to merge two models that have certain compatibility , and . three different approaches Žtopological reordering, default restructuring, and heuristic restructuring. to revise a model’s modular structure.

Executing any of the operations could possibly disrupt the integrity of an SML schema. It is shown that the combined operations of join and topological reordering can generate an integrated normal schema from a uniquely joinable pair. Moreover, the operations of join, topological reordering and default restructuring are sufficient to generate an integrated normal schema from a join lossless pair. However, the operations of join, topological reordering and default restructuring may generate an integrated abnormal schema from a joinable pair with more than one compatible pair of genera.

The contributions of this research are two-fold. First, it provides an operational approach to perform model integration in SML. Second, it contributes to the important task of understanding how different kinds of schema edits can disrupt the static semantics of SML, and what can be done about it. It helps lay the foundation for the future development of an incremental static semantic analyzer and smart schema-directed editor 31 . Hence, further research <sup>w</sup> <sup>x</sup> should consider other schema properties mentioned in Ref. 15 .<sup>w</sup> <sup>x</sup>

Another future research is how to salvage as much elemental detail as possible, when it exists, after a schema edit 28 . This is an important practi- <sup>w</sup> <sup>x</sup> cal issue that should be examined.

Object-oriented approaches to model integration are discussed in Refs. 9,10,30 . Another possible<sup>w</sup> <sup>x</sup> avenue might take a graph grammar approach based on an attribute graph view of structured modeling <sup>w</sup> <sup>x</sup> 19 . All these deserve further exploration.

This paper proposed schema operations for model management model integration similar to relationalŽ . algebra<sup>r</sup>calculus for relational data management. An interesting research topic is whether it is feasible to develop a model management theoretical counterpart to relational algebra or calculus. Thereby we may have the model management capacities for restructuring, generating, updating, querying and retrieving the results of models equal those in data management. The necessary comprehensive examination of the similarities and differences of both model management and data management has yet to be conducted 29 . <sup>w</sup> <sup>x</sup>

## Acknowledgements

I would like to thank Prof. Arthur Geoffrion for his constant guidance, inspiration and constructive criticism of the research, Srikanth Chari and the referees for their helpful suggestions, and finally Linda Leon, Charlene Polio, and Beth Kinne for their help in editing the many drafts of this paper. They are, of course, not responsible for any errors. Additionally, I would like to dedicate this paper to my dear mother, Shu Lin Tsai, who passed away during my years at UCLA. Her contributions to this paper are least direct but probably most important.

## References

<sup>w</sup> <sup>x</sup> 1 H.K. Bhargava, S.O. Kimbrough, Model management, an embedded languages approach, Decision Support Sys. 10 Ž . 1993 277–299.

<sup>w</sup> <sup>x</sup> 2 H.K. Bhargava, S. Kimbrough, R. Krishnan, Unique names violations, a problem for model integration or you say tomato, I say tomahto, ORSA J. Comput. 3 2 1991 107–120.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 R.W. Blanning, A Relational Theory of Model Management, Decision Support Systems: Theory and Application, Springer-Verlag, Berlin, 1987.

<sup>w</sup> <sup>x</sup> 4 S. Chari, R. Krishnan, Towards a logical reconstruction of

structured modeling, Decision Support Sys. 10 3 1993 Ž . Ž . 301–317.

<sup>w</sup> <sup>x</sup> 5 J. Dickinson, The business of words: outliner, PC Mag. 5 6Ž . Ž . 1986 199–220.

<sup>w</sup> <sup>x</sup> 6 D.R. Dolk, J.E. Kottemann, Model integration and a theory of models, Decision Support Sys. 9 1993 51–63.Ž .

<sup>w</sup> <sup>x</sup> 7 Framework IV, User’s Manual, Ashton-Tate, 20101 Hamilton Ave., Torrance, CA 90502, 1991.

<sup>w</sup> <sup>x</sup> 8 M. Gagliardi, C. Spera, BLOOMS: a basic language object oriented for modeling systems, Working Paper 10, Dept. of Quantitative Methods, University of Siena, Italy, April, 1995, p. 33.

<sup>w</sup> <sup>x</sup> 9 M. Gagliardi, C. Spera, Toward a formal theory of model integration, Ann. Operations Res. 58 1995 405–440.Ž .

<sup>w</sup> <sup>x</sup> 10 M. Gagliardi, C. Spera, Some new results in model integration, Proceedings of the 28th Annual Hawaii International Conference on System Sciences, 1995, pp. 398–407.

<sup>w</sup> <sup>x</sup> 11 A.M. Geoffrion, Integrated modeling systems, Comput. Sci. Econ. Manage. 2 1 1986 3–15.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 A.M. Geoffrion, An introduction to structured modeling, Manage. Sci. 33 5 1987 547–588.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 A.M. Geoffrion, The formal aspect of structured modeling, Operations Res. 37 1 1989 30–51.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 A.M. Geoffrion, Reusing structured models via model integration, Proceedings of the 22nd Annual Hawaii International Conference on System Sciences, 1989, pp. 601–611.

<sup>w</sup> <sup>x</sup> 15 A.M. Geoffrion, SML: a model definition language for structured modeling, WMSI Working Paper 360, August 1990, 137.

<sup>w</sup> <sup>x</sup> 16 A.M. Geoffrion, FW<sup>r</sup>SM: a prototype structured modeling environment, Manage. Sci. 37 12 1991 1513–1538. Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 A.M. Geoffrion, The SML language for structured modeling, Operations Res. 40 1 1992 38–75, 2-part paper. Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 A.M. Geoffrion, Structured modeling: survey and future research directions, ORSA CSTS Newslett. 15 1 1994 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 C.V. Jones, Attributed graphs, graph–grammars, and structured modeling, Ann. Operations Res. 38 1992 281–324.Ž .

<sup>w</sup> <sup>x</sup> 20 J.E. Kottemann, D.R. Dolk, Model integration and modeling languages: a process prospective, Inform. Sys. Res. 3 1992Ž . 1–16.

<sup>w</sup> <sup>x</sup> 21 T.P. Liang, Toward the development of a knowledge-based model management systems, PhD Dissertation, University of Pennsylvania, 1986.

<sup>w</sup> <sup>x</sup> 22 W. Muhanna, R. Pick, Composite models in SYMMS, Proceedings of the 21st Annual Hawaii International Conference On System Sciences, January 1988, pp. 418–427.

<sup>w</sup> <sup>x</sup> 23 S. Navathe, R. Elmasri, J. Larson, Integration User Views in Database Design, IEEE Comput., January 1986, pp. 50–62.

<sup>w</sup> <sup>x</sup>24 L. Neustadter, A. Geoffrion, S. Maturana, Y. Tsai, F. Vicuna, The design and implementation of a prototype structured modeling environment, Ann. Operations Res. 38 1992Ž . 453–484.

<sup>w</sup> <sup>x</sup> 25 J.F. Sowa, Conceptual Structures: Information Processing in Mind and Machine, Addison-Wesley, MA, 1984.

<sup>w</sup> <sup>x</sup> 26 R. Sprague, H.J. Watson, MIS concepts: part I, J. Syst. Manage. 26 1 1975 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 R. Sprague, H.J. Watson, MIS concepts: part II, J. Syst. Manage. 26 2 1975 .Ž . Ž .

28 Y. Tsai, The approach to elemental detail integration, Informal Note, UCLA, May 1988, p. 4.

<sup>w</sup> <sup>x</sup> 29 Y. Tsai, An analytical comparison of data management and model management, Working Paper, National Cheng Kung University, Tainan, Taiwan, March 1997, p. 17.

<sup>w</sup> <sup>x</sup> 30 L. Tung, R. Ramirez, R.D. St. Louis, Model integration in an objected-oriented environment, Proceedings of the 24th Annual Hawaii International Conference on System Science, January 1991, pp. 284–290

<sup>w</sup> <sup>x</sup> 31 F. Vicuna, Semantic formalization in mathematical modeling˜ languages, PhD Dissertation, Computer Science Department, UCLA, 1990, p. 189.

<sup>w</sup> <sup>x</sup> 32 H.J. Will, Model management systems, Inform. Syst. Organization Struct., Berlin, 1975, pp. 467–482.

<sup>w</sup> <sup>x</sup> 33 Word 7.0, Chinese Version, Microsoft, Microsoft Way, Redmond, WA 98052, 1995.

![](/api/attachments/U2EX3XQ7/fulltext/images/6a2f7353a16302632722ad8c523f5079ead743e23a2640ada662a299d0eb8ea2.jpg)

Yao-Chuan Tsai is an Associate Professor of Business Administration in the Graduate School of Management at National Cheng Kung University in Taiwan. He received his MS in Industrial Engineering from Northwestern University and his PhD in Management from the Anderson School at UCLA. He was a member of the FW<sup>r</sup>SM Prototype Development Team 1985–1991 andŽ . serves on the National Standard Commission draft panel for Computers and

Communications 1997–1999 . His research interests are com-Ž . puter-based modeling systems, database management, and information technology, especially the Internet, the File-Server systems, and their relationships to Business Administration. His work has recently been published in some journals, including Annals of Operations Research, Decision Support Systems, and Interfaces.
