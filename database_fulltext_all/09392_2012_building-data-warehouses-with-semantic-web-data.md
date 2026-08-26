---
otero_id: 9392
otero_key: "HB6KCNM8"
title: "Building data warehouses with semantic web data"
authors: "Victoria Nebot; Rafael Berlanga"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building data warehouses with semantic web data

Victoria Nebot ⁎, Rafael Berlanga

Departamento de Lenguajes y Sistemas Informáticos, Universitat Jaume I, Campus de Riu Sec, 12071, Castellón, Spain

a r t i c l e i n f o

Available online 29 November 2011

Keywords: Semantic Web Ontologies Data warehouses OLAP Multidimensional design

## a b s t r a c t

The Semantic Web (SW) deployment is now a realization and the amount of semantic annotations is ever increasing thanks to several initiatives that promote a change in the current Web towards the Web of Data, where the semantics of data become explicit through data representation formats and standards such as RDF/(S) and OWL. However, such initiatives have not yet been accompanied by ef<sup>fi</sup>cient intelligent applications that can exploit the implicit semantics and thus, provide more insightful analysis. In this paper, we provide the means for ef<sup>fi</sup>ciently analyzing and exploring large amounts of semantic data by combining the inference power from the annotation semantics with the analysis capabilities provided by OLAP-style aggregations, navigation, and reporting. We formally present how semantic data should be organized in a well-de<sup>fi</sup>ned conceptual MD schema, so that sophisticated queries can be expressed and evaluated. Our proposal has been evaluated over a real biomedical scenario, which demonstrates the scalability and applicability of the proposed approach.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

The effort behind the Semantic Web (SW) is to add machineunderstandable, semantic annotation to web-published contents so that web information can be effectively retrieved and processed by both humans and machines in a great variety of tasks. This is in practice achieved by using SW technologies, which enable to attach semantics to resources, ranging from very simple to very complex annotations depending on the requirements. SW technologies open a new dimension to data integration by providing a common terminology, standard formats for knowledge resources (e.g., RDF/(S)<sup>1</sup> and OWL<sup>2</sup>), semantically linked data, and more formal representations like description logic axioms for inference tasks. As a result, more and more semi-structured data and knowledge resources are being published in the Web, creating what is called the Web of Data [11]. At the same time, there is a great urgency of new analytical tools able to summarize and exploit all these resources.

Semantic search has emerged as one of the <sup>fi</sup>rst applications making use and exploiting the Web of Data. New systems that offer search and browsing over RDF data have been developed [16,19,20,39,40]. Research in this area is a hot topic because it enhances conventional information retrieval by providing search services centered on entities, relations, and knowledge. Also, the development of the SW demands enhanced search paradigms in order to facilitate acquisition, processing, storage, and retrieval of semantic data. Albeit interesting, semantic search does not provide users with great insight into the data. Various advanced applications that have recently emerged impose modern user and business needs that require a more analytical view. Some examples include customer support, product and market research or life sciences and health care applications with both structured and unstructured information available.

The biomedical domain is one of the most active areas where signi<sup>fi</sup>- cant efforts have been spent to export database semantics to data representation formats following open standards, which explicitly state the semantics of the content. The use of ontologies and languages such as RDF and OWL in the area of medical sciences has already a long way, and several web references to medical ontologies for different areas of medicine can be found (UMLS [12], SNOMED-CT [6], GALEN [1], GO [2], etc.). Moreover, a growing penetration of these technologies into the life science community is becoming evident through many initiatives (e.g. Bio2RDF [9], Linked Life Data [3], Liking Open Drug Data [4], etc.) and an increasing number of biological data providers, such as UniProt [7], have started to make their data available in the form of triples. In these complex scenarios keyword or faceted search may be useful but not enough, since advanced analysis and understanding of the information stored are required. Given the previous analysis requirements over these new complex and semantic representation formats, the well-known data warehousing (DW) and OLAP technologies seem good candidates to perform more insightful analytical tasks.

During the last decade, DW has proved its usefulness in traditional business analysis and decision making processes. A data warehouse can be described as a decision-support tool that collects its data from operational databases and various external sources, transforms them into information and makes that information available to decision makers in a consolidated and consistent manner [24]. One of the technologies usually associated to DW is multidimensional (MD) processing, also called OLAP [17] processing. MD models de<sup>fi</sup>ne the analytic requirements for an application. It consists of the events of interest for an analyst (i.e., facts) described by a set of measures along with the different perspectives of analysis (dimensions). Every fact is described by a set of dimensions, which are organized into hierarchies, allowing the user to aggregate data at different levels of detail. MD modeling has gained widespread acceptance for analysis purposes due to its simplicity and effectiveness.

This work opens new interesting research opportunities for providing more comprehensive data analysis and discovery over semantic data. In this paper, we concentrate on semantic annotations that refer to an explicit conceptualization of entities in the respective domain. These relate the syntactic tokens to background knowledge represented in a model with formal semantics (i.e. an ontology). When we use the term “semantic”, we thus have in mind a formal logical model to represent knowledge. We provide the means for ef<sup>fi</sup>- ciently analyzing and exploring large amounts of semantic data by combining the inference power from the annotation semantics with the analysis capabilities provided by OLAP-style aggregations, navigation, and reporting. We formally present how semantic data should be organized in a well-de<sup>fi</sup>ned conceptual MD schema, so that sophisticated queries can be expressed and evaluated. As far as we know there is no tool providing OLAP-like functionality over semantic web data. In Section 2.3 we elaborate on the requirements and challenges faced when dealing with semantic web data.

The main contributions of the paper are summarized as follows:

• We introduce a semi-automatic method to dynamically build MD fact tables from semantic data guided by the user requirements.

• We propose two novel algorithms to dynamically create dimension hierarchies with “good” OLAP properties from the taxonomic relations of domain ontologies for the fact tables generated with the previous method.

• We provide an application scenario and a running use case in the biomedical domain to illustrate the usefulness and applicability of our method.

The rest of the paper is organized as follows. Section 2 introduces the application scenario with a use case that motivates our approach. Section 3 provides an overview of the method. Section 4 contains the user conceptual MD schema de<sup>fi</sup>nition. Section 5 is devoted to the fact extraction process, and we cover both the foundations and implementation issues. In Section 6, we propose two methods for dimension extraction. Section 7 describes the experimental evaluation and implementation. Section 8 reviews related work regarding the trends in analytical tools for non-conventional data sources, mainly the semi-structured ones and <sup>fi</sup>nally, in Section 9 we give some conclusions and future work.

## 2. Application scenario

In this paper we adopt the application scenario of the Health-e-Child integrated project (HeC) [37], which aimed to provide a grid-based integrated data infrastructure for new decision support systems (DSS) for Pediatrics. Such DSS tools are mainly focused on traditional diagnosis/ prognosis tasks and patient follow-up.

This scenario regards three main types of data sources: well standardized records coming from hospital information systems (e.g. HL7-conformant records), highly heterogeneous semi-structured clinical reports, and a variety of unstructured data such as DICOM <sup>fi</sup>les, ECG data, X-ray and ultrasonography images. All data are delivered to the HeC infrastructure in XML format, usually lacking of any schema for the semi- and unstructured data sources. Unfortunately, most of the interesting analysis dimensions are located in the schema-less data sources. The integration solution proposed in the HeC project formerly consisted in de<sup>fi</sup>ning a <sup>fl</sup>exible integrated data model [10], which is built on top of a grid-aware relational database management system (see left hand side of Fig. 1). As clinical reports present very irregular structures (see the example presented in Fig. 2), they are decomposed and classi<sup>fi</sup>ed into a few organizational units (i.e. patient, visit, medical event and clinical variables), thus disregarding much information that could be useful for the intended DSS tools. Additionally, this data model also includes tables that map clinical variables to concept identi<sup>fi</sup>ers from the UMLS Metathesaurus [12]. These tables are intended to link patient data to bibliographic resources such as MEDLINE [5]. It is worth mentioning that a similar scenario and solution have been proposed in the OpenEHR initiative.<sup>3</sup>

However, in this paper we adopt a different integration architecture (see right hand side of Fig. 1), which follows the current trends in biomedical [13] and bioinformatics data integration [27], and relies entirely on SW technology. In this architecture, the integrated data model is de<sup>fi</sup>ned as an application ontology that models the health care scenario (e.g. patients, visits, reports, etc.) This ontology can import concepts de-<sup>fi</sup>ned in external knowledge resources (reference domain ontologies in Fig. 1). Finally, the biomedical data is semantically annotated according to the application ontology and stored as RDF triples (i.e. triple store). In the HeC scenario, the application ontology modeling the rheumatology domain has 33 concepts and 39 roles. However, this ontology can import any concept from UMLS, which is used as reference domain ontology, and contains over 1.5 million concepts. The triple store of the application scenario has 605,420 instances containing references to 874 different concepts of UMLS. Moreover, depending on the user's requirements (i.e. dimensions selected) more domain ontology axioms will be imported in order to build the dimension hierarchies.

In this paper, we aim at analyzing and exploiting all this semantic data through OLAP-based tools. Subsequent sections present the representation formalism of the semantic data, some examples of OLAPbased analysis, and <sup>fi</sup>nally, the main issues involved in carrying out OLAP-based analysis over semantic data.

## 2.1. Semantic data representation

We use the language OWL-DL to represent the application ontology to which semantic annotations refer. OWL-DL has its foundation in the description logics (DL) [8]. Basically, DLs allow users to de<sup>fi</sup>ne the domain of interest in terms of concepts (called classes in OWL), roles (called properties in OWL) and individuals (called instances in OWL). Concepts can be de<sup>fi</sup>ned in terms of other concepts and/or properties by using a series of constructors, namely: concept union (⊔), intersection (⊓) and complement (¬), as well as enumerations (called oneOf in OWL) and existential (∃), universal (∀) and cardinality (≥, ≤, =) restrictions over a role R or its inverse R<sup>−</sup>.

Concept de<sup>fi</sup>nitions are asserted as axioms, which can be of two types: concept subsumption (C⊑D) and concept equivalence (C≡D). The former one is used when one only partially knows the semantics of a concept (the necessary but not suf<sup>fi</sup>cient conditions). Equivalence and subsumption can be also asserted between roles, and roles can have special constraints (e.g., transitivity, symmetry, functionality, etc.) The set of asserted axioms over concepts and roles is called the terminological box (TBox).

Semantic data is expressed in terms of individual assertions, which can be basically of two types: assert the concept C of an individual a, denoted C(a), and assert a relation between two individuals a and b, denoted R(a,b). The set of assertions over individuals is called the assertional box (ABox).

For practical purposes, the TBox and the ABox are treated separately. Notice that while the ABox is usually very dynamic for it is constantly updated, the TBox hardly changes over time. From now on, we will use the term ontology to refer to the TBox, and instance store to refer to the ABox storage system. We assume that the instance store is always consistent w.r.t. the associated ontology.

![](/api/attachments/HB6KCNM8/fulltext/images/dfd1d204dee31232e4f0cd1495d1fcba3c6376f8883f93fdeabf955434eed776.jpg)  
Fig. 1. HeC data integration architecture (left hand) versus the Semantic Web integration architecture (right hand).

Fig. 3 shows a fragment of the ontology designed for patients with rheumatic diseases in our application scenario, whereas Table 1 shows a fragment of an instance store associated to this ontology. In this case, the instance store is expressed as triples (subject,predicate, object), where a triple of the form (a,type,C) corresponds to a DL assertion C(a), and otherwise the triple (a,R,b) represents the relational assertion R(a, b).

## 2.2. Example of use case

In the previous application scenario, we propose as use case to analyze the ef<sup>fi</sup>cacy of different drugs in the treatment of in<sup>fl</sup>ammatory diseases, mainly rheumatic ones. At this stage, the analyst of this use case should express her analysis requirements at a conceptual level. Later on, these requirements will be translated into dimensions and measures of a MD schema that will hold semantic data.

Fig. 4 depicts the conceptual model of the analyst requirements where the central subject of analysis is Patient. The analyst is interested in exploring the patient's follow-up visits according to different parameters such as gender, age, the drugs prescribed, the affected body parts, the diseases diagnosed, the articular damage and the number of occurrences.

Later on, the previous analysis requirements will be formally expressed in terms of DL expressions over the ontology and these

```txt
Ultrasonography
WristExamination
    date '10/10/2006'
    hasUndergoneWrist True
    rightWrist False
    leftWrist True
WristScore
    wristExamined 'Left'
    PannusAndJointEffusion
    distalRadioUlnarJoint
    result 'No Synovial thikening and no joint effusion'
    radioCarpalJoint
    result 'Only synovial pannus without joint effusion'
    midCarpalCMCJ
    result 'None'
Synovitis
    distalRadioUlnarJoint 'Mild'
    radioCarpalJoint 'None'
    midCarpalCMCJ 'Severe'
BoneErosion
    distalUlna
    erosionDegree 0
    carpalBones
    erosionDegree 1
```  
Fig. 2. Fragment of a clinical report of the rheumatology domain.

Patient  =1 hasAge.string Patient  =1 sex.Gender Patient ∀ hasGeneReport.GeneProfile GeneProfile⊆∀over.Gene∀under.Gene Patient ≤∀ hasHistory.PatientHistory PatientHistory ∃familyMember.Family\_Group∃ hasDiagnosis.Disease\_or\_Syndrome Patient ≤∃ hasVisit.Visit Visit ≤ =1 date.string Visit ≤ ∀ hasReport.(Rheumatology  Diagnosis  Treatment □ Laboratory) Rheumatology ≤∃ results.(Articular  ExtraArticular  Ultrasonography) Rheumatology ≤ = 1 damageIndex.string Ultrasonography ≤∀ hasAbnormality.Disease\_or\_Syndrome Ultrasonography ≤∀ location.Body\_Space\_or\_Junction ArticularFinding ≤∃ affectedJoint.Body\_Space\_or\_Junction ArticularFinding ≤∀ examObservation.string Diagnosis ∃ hasDiagnosis.Disease\_or\_Syndrome Treatment ≤ =1 duration.string Treatment ≤∃ hasTherapy.DrugTherapy DrugTherapy ≤ = 1 administration.AD DrugTherapy  =1 hasDrug.Pharmacologic Substance AD ⊆∃ dosage.string ∃ route.string ∃ timing.string Laboratory ∃ bloodIndicants.(∃ cell.Cell ∃ result.string ∃ test.Lab\_Procedure) Rheumatoid Arthritis  Autoimmune Disease Autoimmune\_Disease ≤ Disease\_or\_Syndrome

Fig. 3. Ontology axioms (Tbox).

expressions will be mapped to elements of a MD schema (i.e. dimensions and measures) that will eventually be populated with the semantic annotations of the instance store. The ultimate goal of the approach is to effectively analyze and explore the semantic annotations using OLAP-style capabilities. In this use case, the analyst will be able to specify useful MD queries in order to analyze patient data and discover useful patterns and trends. As an example, we show two MD queries expressed in MDX-like syntax that an analyst would execute over the resulting fact table in order to generate cubes. The <sup>fi</sup>rst query builds a cube where for each administered drug and diagnosed disease the articular damage registered is averaged. By exploring this cube the analyst can <sup>fi</sup>nd out interesting patterns such as which drugs mitigate the articular damage depending on the disease type.

Table 1  
Semantic annotations (Abox).

<table><tr><td>Subject</td><td>Predicate</td><td>Object</td></tr><tr><td>PTNXZ1</td><td>hasAge</td><td>“10”</td></tr><tr><td>PTNXZ1</td><td>sex</td><td>Male</td></tr><tr><td>PTNXZ1</td><td>hasVisit</td><td>VISIT1</td></tr><tr><td>VISIT1</td><td>date</td><td>“06182008”</td></tr><tr><td>VISIT1</td><td>hasReport</td><td>RHEX1</td></tr><tr><td>RHEX1</td><td>damageIndex</td><td>“10”</td></tr><tr><td>RHEX1</td><td>results</td><td>ULTRA1</td></tr><tr><td>ULTRA1</td><td>hasAbnormality</td><td>“Malformation”</td></tr><tr><td>ULTRA1</td><td>hasAbnormality</td><td>Knee</td></tr><tr><td>VISIT1</td><td>hasReport</td><td>DIAG1</td></tr><tr><td>DIAG1</td><td>hasDiagnosis</td><td>Arthritis</td></tr><tr><td>VISIT1</td><td>hasReport</td><td>TREAT1</td></tr><tr><td>TREAT1</td><td>hasDrugTherapy</td><td>DT1</td></tr><tr><td>DT1</td><td>hasDrug</td><td>Methotrexate</td></tr><tr><td>PTNXZ1</td><td>hasVisit</td><td>VISIT2</td></tr><tr><td>VISIT2</td><td>date</td><td>“08202008”</td></tr><tr><td>VISIT2</td><td>hasReport</td><td>RHEX2</td></tr><tr><td>RHEX2</td><td>damageIndex</td><td>“15”</td></tr><tr><td>RHEX2</td><td>results</td><td>ULTRA2</td></tr><tr><td>ULTRA2</td><td>hasAbnormality</td><td>“Malformation”</td></tr><tr><td>ULTRA2</td><td>hasAbnormality</td><td>Knee</td></tr><tr><td>RHEX2</td><td>results</td><td>ULTRA3</td></tr><tr><td>ULTRA3</td><td>hasAbnormality</td><td>“Rotation 15degrees”</td></tr><tr><td>ULTRA3</td><td>hasAbnormality</td><td>Right_Wrist</td></tr><tr><td>VISIT2</td><td>hasReport</td><td>DIAG2</td></tr><tr><td>DIAG2</td><td>hasDiagnosis</td><td>Systemic_Arthritis</td></tr><tr><td>VISIT2</td><td>hasReport</td><td>TREAT2</td></tr><tr><td>TREAT2</td><td>hasDrugTherapy</td><td>DT2</td></tr><tr><td>DT2</td><td>hasDrug</td><td>Methotrexate</td></tr><tr><td>TREAT2</td><td>hasDrugTherapy</td><td>DT3</td></tr><tr><td>DT3</td><td>hasDrug</td><td>Corticosteroids</td></tr><tr><td>...</td><td>...</td><td>...</td></tr></table>

CREATE CUBE [cubeArticularDamage1]

FROM [patient\_dw]

MEASURE [patient\_dw].[avgArtDamIndex],

DIMENSION [patient\_dw].[Drug],

DIMENSION [patient\_dw].[Disease]

The second query builds a cube where the articular damage is explored over different analysis perspectives, namely the affected body parts and the patient's gender. This way the analyst can discover which body parts contribute most to the total damage index contrasted by gender.

![](/api/attachments/HB6KCNM8/fulltext/images/00b7836eae92b1b62d16aadc83b14bf23d73a71f2dfe2787f6040e50abef679c.jpg)  
Fig. 4. Use case analysis requirements.

CREATE CUBE [cubeArticularDamage2]

FROM [patient\_dw]

MEASURE [patient\_dw].[avgArtDamIndex],

DIMENSION [patient\_dw].[BodyPart],

DIMENSION [patient\_dw].[Gender]

## 2.3. Issues in analyzing semantic data

The full exploitation of semantic data by OLAP tools is far from trivial due to the special features of semantic data and the requirements imposed by OLAP tools. Next, we describe some of the main challenges we encounter when dealing with semantic web data, which are treated in this paper:

• Usability: when dealing with the Web of Data, the user typically needs to specify a structured query in a formal language like SPARQL. However, the end user often does not know the query language and the underlying data graph structure. Even if she did, languages such as SPARQL do not account for the complexity and structural heterogeneity often common in RDF data. We overcome this issue by providing the user with a simple mechanism to specify her analysis requirements at the conceptual level. We ask the user to compose a conceptual MD schema by selecting concepts and properties of interest from the available ontologies.

• Imprecision: the information needs expressed by the user might be imprecise. On one hand, the <sup>fl</sup>exibility and ease of use offered to the user in the requirements phase can lead to an ambiguous speci<sup>fi</sup>cation (i.e. the concepts and properties selected might be used in several contexts in the ontologies). On the other hand, the user might have limited knowledge about the domain and her speci<sup>fi</sup>cation might be too general or abstract. Our method overcomes both types of imprecision by taking into account all possible interpretations of the concepts speci<sup>fi</sup>ed by the user. Moreover, thanks to the semantics attached to the data, implicit information can be derived and made explicit so that the user can re<sup>fi</sup>ne her MD speci<sup>fi</sup>- cation by selecting these new inferred concepts.

• Scalability: as the amount of available data is ever growing, the ability to scale becomes essential. What is more important, scalability is known to be an issue when reasoning with large ontologies. In this work, we overcome this issue by applying speci<sup>fi</sup>c indexes to ontologies in order to handle basic entailments minimizing the use of the reasoner.

• Dynamicity: the web is continuously changing and growing. Therefore, analytical tools should re<sup>fl</sup>ect these changes and present fresh results. Also, data are being provided at an overwhelming level of detail and only a subset of attributes constitute meaningful dimensions and facts for the analyst. For these reasons, our method allows the user to select only the concepts of interest for analysis and automatically derives a MD schema (i.e. dimensions and facts) and its instantiation ready to be fed into an off the shelf OLAP tool, for further analysis.

## 3. Method overview

In this section we present an overview of our method. We focus on the end-to-end description of the data <sup>fl</sup>ow from expressing the analysis requirements to returning analytical query results. Fig. 5 depicts a schematic overview of the whole process. The repository of semantic annotations on the left of Fig. 5 stores both the application and domain ontology axioms (i.e. Tbox) and the semantic annotations (i.e. instance store). This repository maintains the necessary indexes for an ef<sup>fi</sup>cient management. For obtaining OLAP style functionality, our goal is to create a MD schema from both the analyst requirements and the knowledge encoded in the ontologies. The fact table is populated with facts extracted from the semantic annotations – a fact is not a simple RDF triple but a valid semantic combination of structurally related instances – while dimension hierarchies are extracted by using the subsumption relationships inferred from the domain ontologies. Each of the phases are described in turn.

• During the design of the conceptual MD schema, the user expresses her analysis requirements in terms of DL expressions over the ontology. In particular, she selects the subject of analysis, the potential semantic types for the dimensions and the measures.

• The fact extractor is able to identify and extract facts (i.e. valid combinations of instances) from the instance store according to the conceptual MD schema previously designed, giving rise to the base fact table of the DW.

• The dimensions extractor is in charge of building the dimension hierarchies based on the instance values of the fact table and the knowledge available in the domain ontologies (i.e. inferred taxonomic relationships) while also considering desirable OLAP properties for the hierarchies.

![](/api/attachments/HB6KCNM8/fulltext/images/d6e317946f9b2bbc72de2ea2af0cf9f36b02f5b7ce41c81592dcc56d2c70675c.jpg)  
Fig. 5. Architecture for semantic annotations analysis

subject ::= ′SU BJECT(′ name ′,′ concept ′)' dimension := 'DIM(' name ′,' concept | datatypeprop')' measure := 'M(' name ′,' numValueFunction '('datatypeprop'))' name ::= identifier concept ::= concept definition according to OWL DL syntax datatypeprop ::= datavaluedPropertyID numValueFunction := 'AVG' |′SUM'| ′COUNT'| ′MAX′ | ′MIN datavaluedPropertyID ::= URIreference identifier := valid string identifier

Fig. 6. BNF syntax for MD schema speci<sup>fi</sup>cation.

SUBJECT( PatientCase , Patient )

DIM(Disease , Disease\_or\_Syndrome)

DIM(Drug , Pharmacological\_Substance)

DIM( Age , hasAge)

DIM( Gender , Gender)

DIM( BodyPart , Body\_Space\_Or\_Junction)

M(AvgArtDamIndex , AVG (damageIndex)

M(NumberOccs. , COUNT (PatientCase))

Fig. 7. MD schema speci<sup>fi</sup>cation for the use case.

• Finally, the user can specify MD queries over the DW in order to analyze and explore the semantic repository. The MD query is executed and a cube is built. Then, typical OLAP operations (e.g., roll-up, drill-down, dice, slice, etc.) can be applied over the cube to aggregate and navigate data.

## 4. Multidimensional schema de<sup>fi</sup>nition

In this section, we present how the analyst information requirements are translated into a conceptual MD schema in order to leverage the aggregation power of OLAP. The analyst de<sup>fi</sup>nes the MD elements with DL expressions, which seems the most natural choice given that the data sources are expressed under this logical formalism. In particular, the MD schema contains the following elements:

• Subject of analysis: the user selects the subject of analysis from the ontology concepts. We name this concept $C _ { S U B } .$

• Dimensions: usually, a dimension is de<sup>fi</sup>ned as a set of levels with a partial order relation among them (i.e., hierarchy). We postpone the hierarchy creation of each dimension in order to dynamically adapt it to the base dimension values appearing in the resulting fact table. Therefore, the analyst must specify just the semantic type of each dimension. They can be either concepts, named C, or data type properties, named dtp, selected from the ontology.

• Measures: the user selects measures from the ontology by specifying the numeric data type property dtp and the aggregation function to be applied (i.e., sum, average, count, min, max, etc.).

Notice that at this point. the analyst does neither know the dimension values nor the roll-up relationships that will eventually be used in the resulting MD schema. The method presented in this paper will automatically capture this information from the application and the domain ontologies involved in the analysis but always taking into account the user requirements. The syntax for the de<sup>fi</sup>nition of the MD elements is speci<sup>fi</sup>ed in Fig. 6 by means of a version of Extended BNF where terminals are quoted and non-terminals are bold and not quoted. For the running use case, the MD schema de<sup>fi</sup>nition is shown in Fig. 7.

## 5. Extracting facts

This section addresses the process of fact extraction from the semantic annotations. First, the foundations of the approach are presented and then we discuss implementation details.

## 5.1. Foundations

The ultimate goal of the approach is to identify and extract valid facts according to the user's requirements. However, the user's conceptual MD schema is ambiguous in the sense that it can have several interpretations. In the running example, the dimension Disease can refer to the patient's main diagnosis, to some family member diagnosis, or it can be a collateral disease derived from the main disease detected through laboratory tests or rheumatic exams. In absence of further knowledge, the fact extraction process should account for all possible interpretations of the user's conceptual MD schema. Later on, when constructing OLAP cubes, the system will ask the user for her interpretation of the dimensions and measures in case there is more than one. This section elaborates on the de<sup>fi</sup>nitions that allow to capture all possible interpretations of the user analysis requirements and thus extract all possible facts under these different interpretations. From now on, O refers to the ontology axioms, IS to the instance store and $C _ { S U B } ,$ D and M are the subject of analysis, dimensions and measures, respectively. We show examples of the de<sup>fi</sup>nitions with a simpli<sup>fi</sup>ed version of the user requirements for the sake of readability and comprehension. Suppose the analyst is interested in analyzing rheumatic patients with the following dimensions and measures: C =Patient, D={Gender,Drug,Disease}, M={damageIndex}. Fig. 8 shows a graph-based representation of the ontology fragment where the schema elements are shaded.

De<sup>fi</sup>nition 1. The subject instances are the set $I _ { S U B } = \{ i / i \in I S ,$ $O \cup I S | = C _ { S U B } ( i ) \}$ .

In the running example $C _ { S U B }$ is Patient and $I _ { S U B }$ is the set of all instances classi<sup>fi</sup>ed as Patient.

![](/api/attachments/HB6KCNM8/fulltext/images/468e600cc2b50ff28eb7847e74e8fdfa9d258bc0c4ecc763aa40c6b791968817.jpg)  
Fig. 8. Example of ontology graph fragment

De<sup>fi</sup>nition 2. Let $c \in D$ be a dimension. We de<sup>fi</sup>ne the senses of c as the following set:

$$
\text { senses } (c) = M S C \left(\left\{c ^ {\prime} \mid \exists r \in O, O \vDash \left(c ^ {\prime} \sqsubset \exists r. c\right) \right\} \cup T\right)
$$

where the function $\mathsf { M S C } ^ { 4 }$ returns the most speci<sup>fi</sup>c concepts of a given concept set, that is, those concepts of the set that do not subsume any other concept in the same set.

Similarly, we can de<sup>fi</sup>ne the senses of a measure $p { \in } M$ as follows:

$$
\text { senses } (p) = M S C \left(\left\{c ^ {\prime} \mid O \vDash c ^ {\prime} \sqsubset \exists p. T \right\} \cup T\right)
$$

Finally, we de<sup>fi</sup>ne S as the union of the senses of each dimension and measure:

$$
S = \bigcup_ {\forall i \in D \cup M} s e n s e s (i)
$$

Example 1. In Fig. 8 the senses of each MD element are enclosed in boxes. senses(Drug) = {DrugTherapy}, senses(Disease) = {Diagnosis, Ultrasonography}, senses(Gender)={Patient} and senses(damageIn-$d e x ) = \{ R h e u m a t o l o g y \}$ . Notice that the senses are the different interpretations that the MD elements can have in the ontology.

We need to identify the senses for both dimensions and measures because dimension values can participate in different parts of the ontology and measures can also be applied to different domain concepts.

The following De<sup>fi</sup>nitions (3–6) are aimed at capturing the structural properties of the instance store w.r.t. the ontology in order to de<sup>fi</sup>ne valid instance combinations for the MD schema.

De<sup>fi</sup>nition 3. The expression $( r _ { 1 } \circ \cdots \circ r _ { n } ) \in P a t h s ( C , C ^ { \prime } )$ is an aggregation path from concept C to concept $C ^ { \prime }$ of an ontology O iff $O { \stackrel { \textstyle \ k } { = } } C { \stackrel { \underbrace { \ v } } { = } } \exists r _ { 1 } { ^ { \circ \cdots \circ } } r _ { n } . C ^ { \prime } .$

De<sup>fi</sup>nition 4. Let $C _ { a } , C _ { b } \in S$ be two named concepts. Contexts $\textstyle C _ { a } , C _ { b } ,$ $C _ { S U B } ) = \cup _ { \forall C ^ { \prime } \in L C R C ( C _ { a } , C b , C S U B ) } \{ C ^ { \prime \prime } / C ^ { \prime \prime } \subseteq C ^ { \prime } \}$ , where the function $L C R C ( C _ { a } ,$ $C _ { b } , C _ { S U B } )$ returns the set of least common reachable concepts, that is,

1. |Paths $\cdot ( C ^ { \prime } , C _ { a } ) | > 0 \land | P a t h s ( C ^ { \prime } , C _ { b } ) | > 0 \land | P a t h s ( C _ { S U B } , C ^ { \prime } ) | > 0$ (C′ is common reachable concept).

2. ∄E∈O such that E satis<sup>fi</sup>es the condition 1 and $| P a t h s ( C ^ { \prime } , E ) | >$ 0 (C′ is least).

The <sup>fi</sup>rst condition states that there must be a path connecting C′ and $C _ { a } ,$ another path connecting C′ and $C _ { b }$ and a third path connecting the subject concept $C _ { S U B }$ with C′. The previous de<sup>fi</sup>nition is applied over all the senses in S pairwise in order to <sup>fi</sup>nd common contexts that semantically relate them.

Example 2. In Fig. 8, Contexts(DrugTherapy,Diagnosis,Patien $t ) = \{ V i s i t \}$ because $p _ { 1 } = V i s i t$ . hasReport ∘hasTherapy. DrugTherapy, $p _ { 2 } = V i s i t .$ hasReport.Diagnosis and $p _ { 3 } = P a t i e n t . h a s V i s i t . V i s i t .$

De<sup>fi</sup>nition 5. Let $i , i ^ { \prime } { \in } I S$ be two named instances. The expression $( r _ { 1 } \circ \cdots \circ r _ { n } ) \in P a t h s ( i , i ^ { \prime } )$ is an aggregation path from i to i′ iff:

1. There exists a list of property assertions $r _ { j } ( i _ { j - 1 } , i _ { j } ) \in I S , 1 \leq j \leq n .$

2. There exists two concepts $C , C ^ { \prime } { \in } O$ such that $O \cup I S { \lneq } C ( i ) \land C ^ { \prime } ( i ^ { \prime } )$ and $( r _ { 1 } \circ \cdots \circ r _ { n } ) \in P a t h s ( C , C ^ { \prime } )$

The <sup>fi</sup>rst condition of the previous de<sup>fi</sup>nition states that there must be a property chain between both instances in the IS, and the second one states that such a path must be also derived from the ontology.

De<sup>fi</sup>nition 6. Let $i _ { a } , i _ { b } \in I S$ be two named instances such that $O \cup I S \vdash C _ { a } ( i _ { a } ) \land C _ { b } ( i _ { b } ) \land C _ { a } , C _ { b } \in S \land C _ { a } \neq C _ { b } . \qquad C o n t e x t s ( i _ { a } , i _ { b } , i _ { S U B } ) =$ $\cup _ { \forall i ^ { \prime } \in L C R I ( i _ { a } , i _ { b } , i _ { S U B } ) } \{ i ^ { \prime } \}$ , where the function $L C R I ( i _ { a } , i _ { b } , i _ { S U B } )$ returns the set of least common reachable instances, that is,

1. |Paths(i′, i )| > 0 ∧ |Paths(i′, i )| > 0 ∧ |Paths(i , i′)| > 0 (i′ is common reachable instance).

2. $\nexists j \in I S$ such that j satis<sup>fi</sup>es the condition 1 and $| P a t h s ( i ^ { \prime } , j ) | > 0 ( i ^ { \prime }$ is least).

The previous de<sup>fi</sup>nition is applied over instances belonging to different senses pairwise in order to <sup>fi</sup>nd common contexts that relate them.

Example 3. Fig. 9 shows an example of IS represented as a graph that is consistent with ontology fragment in Fig. 8. In this example, Contexts $( D T 1 , D I A G 1 , P T N \_ X Y 2 1 ) = \{ V I S I T 1 \}$ because $p _ { 1 } = V I S I T 1$ .hasReport∘has Therapy.DT1, $p _ { 2 } { = } V I S I T 1$ 1.hasReport.DIAG1 and $p _ { 3 } = P T N \_ X Y 2 1 . h a s V i s i t .$ VISIT1.

Now, we can de<sup>fi</sup>ne which instances can be combined to each other for a certain analysis subject $C _ { S U B }$

De<sup>fi</sup>nition 7. Two instances $i _ { a } , i _ { b } { \in } I S$ are combinable under a subject instance $i _ { S U B } \mathrm { ~ i f f } \exists C _ { 1 } \in \{ C ( i _ { x } ) / i _ { x } \in C o n t e x t s ( i _ { a } , i _ { b } , i _ { S U B } ) \} , \exists C _ { 2 } \in C o n t e x t s ( C ( i _ { a } )$ $C ( i _ { b } ) , C _ { S U B } )$ such that $O { \models } C _ { 1 } \exists C _ { 2 }$ where C(i) is the asserted class for the instance i in IS.

![](/api/attachments/HB6KCNM8/fulltext/images/b52f557943053a25c61386126ce0339b32d70e4b1956b509e593da07dfad3a94.jpg)  
Fig. 9. Example of instance store fragment consistent with ontology fragment of Fig. 8.

Example 4. As an example of the previous de<sup>fi</sup>nition, let us check if instances DT1 and DIAG1 of Fig. 9 are combinable. In the de<sup>fi</sup>nition, $C _ { 1 }$ can only be Visit and $C _ { 2 }$ is also Visit by looking at Fig. 8. Since $O { \Vdash } V i s i t { \equiv } V i s i t ,$ , instances DT1 and DIAG1 are combinable under subject instance PTN \_XY21. The intuition of the previous de<sup>fi</sup>nition is that two instances are combinable only if at the instance level (i.e., in the instance store or Abox) they appear under a context that belongs to or is more general than the context speci<sup>fi</sup>ed at the conceptual level (i.e., in the Tbox). Following this intuition, instances DT1 and DIAG2 are not combinable because their contexts at the instance level are {PTN \_XY21} whose type is Patient while at the conceptual level their contexts are {Visit}. This makes complete sense because the ontology has been de<sup>fi</sup>ned in such a way that each visit contains the diseases diagnosed along with the drugs prescribed.

Only valid combinations conformant with the MD schema are taken into account in the following de<sup>fi</sup>nition.

De<sup>fi</sup>nition 8. An instance context associated to $i _ { S U B } { \in } I S$ is the tuple $( i _ { 1 } , \cdots , i _ { n } )$ , with $n { \geq } | D \cup M |$ , satisfying the following conditions:

1. $\forall c \in \{ D \cup M \}$ , there is at least one tuple element $i _ { x } , 1 \le x \le n ,$ such that $O \cup I S { \vdash } C ( i _ { x } )$ and $C { \in } s e n s e s ( c )$ or $i _ { x } { = } N U L L$ otherwise. From now on, we will denote with dim $l { \left( i _ { x } \right) }$ to the MD element associated t $0 i _ { x } \left( \mathrm { i } . \mathrm { e } . c \right)$

2. $\forall ( j , k ) , 1 \le j , k \le n , j \neq k , ( i _ { j } , i _ { k } )$ are combinable instances under i<sub>SUB</sub>.

In other words, each of the elements of an instance context tuple is an instance that belongs to one sense and satis<sup>fi</sup>es the combinable condition of De<sup>fi</sup>nition 7 with the rest of instances in the tuple. Therefore, an instance context tuple represents all the potential valid interpretations from IS for a MD schema speci<sup>fi</sup>cation since all the elements of the MD schema must be covered by at least one instance or the NULL value if there is not such instance (i.e. in case of optional values in the ontology).

We say that an instance context tuple is ambiguous if there is more than one sense associated to the same dimension (measure). For example, tuples in Table 2 are ambiguous because the dimension Disease has associated two senses in all the tuples.

Example 5. Given dimensions $D = \{ D i s e a s e ,$ Drug, Gender} and measures $M { = } \{ d a m a g e I n d e x \}$ with their associated senses, Table 2 shows the instance context tuples generated for subject instance PTN\_XY21. Notice we keep track of the subject of analysis (i.e. Patient) in a new column.

Finally, we must project the intended values to obtain the facts that will populate the MD schema.

De<sup>fi</sup>nition 9. A data fact associated to an instance context tuple $( i _ { 1 } , \cdots , i _ { m } )$ is a tuple $( d _ { 1 } , \cdots , d _ { n } )$ with $n { \ge } m$ such that

$$
d _ {k} = \left\{ \begin{array}{l l} j _ {k} & \text { if } d i m (i _ {k}) \in D \text { and } j _ {k} \in \prod_ {p} (i _ {k}) \text { and } O \cup I S \vDash C (j _ {k}) \text { and } C \subseteq d i m (i _ {k}) \\ v _ {k} & \text { if } d i m (i _ {k}) \in M \text { and } v _ {k} \in \prod_ {d i m (i _ {k})} (i _ {k}) \\ n u l l & \text { otherwise } \end{array} \right.
$$

where $\prod _ { p }$ is the projection operation over an instance through the property $p .$

Notice that we take into consideration that the projection can be multivalued (i.e. more than one value can be accessed with the same property in an instance).

## Table 2

Instance context tuples generated for the running example. The second row accounts for the senses associated to each dimension

<table><tr><td>Dimensions</td><td colspan="2">Disease</td><td>Drug</td><td>Gender</td><td>damageIndex</td></tr><tr><td>Senses</td><td>Ultrasono.</td><td>Diagnosis</td><td>DrugTherapy</td><td>Patient</td><td>Rheuma.</td></tr><tr><td>PTN_XY21</td><td>ULTRA1</td><td>DIAG1</td><td>DT1</td><td>PTN_XY21</td><td>RHEX1</td></tr><tr><td>PTN_XY21</td><td>ULTRA2</td><td>DIAG2</td><td>DT2</td><td>PTN_XY21</td><td>RHEX2</td></tr><tr><td>PTN_XY21</td><td>ULTRA2</td><td>DIAG2</td><td>DT3</td><td>PTN_XY21</td><td>RHEX2</td></tr><tr><td>PTN_XY21</td><td>ULTRA3</td><td>DIAG2</td><td>DT2</td><td>PTN_XY21</td><td>RHEX2</td></tr><tr><td>PTN_XY21</td><td>ULTRA3</td><td>DIAG2</td><td>DT3</td><td>PTN_XY21</td><td>RHEX2</td></tr></table>

It is worth mentioning that “disambiguation” of instance tuples and data facts must be performed before building the OLAP cubes. Such a disambiguation can only be manually performed by the user according to her analysis requirements and the semantics involved. We will not treat further this issue as we consider it out of the scope of this paper.

Example 6. The previous instance context tuples in Table 2 give rise to the data fact tuples in Table 3 where each instance has been projected according to the previous de<sup>fi</sup>nition. In the data fact tuples, measures are treated the same way as dimensions. Only when data fact tuples are going to be loaded into a cube, measure values sharing dimension values are aggregated according to the aggregation function selected.

## 5.1.1. Complexity issues

In our method, the extraction of facts from the IS (De<sup>fi</sup>nition 9) requires the generation of different subsets of O (i.e. senses, paths and contexts), which in turn requires the use of a reasoner to perform inferences like $O { \ v Q } = { \ v Q }$ and $O \cup I S { \mathsf { = } } \alpha .$ The complexity of current reasoners depends on the expressiveness of both O and α, and consequently it directly affects to the ef<sup>fi</sup>ciency of our method. It is worth mentioning that the expressivity of OWL DL leads to exponential complexity for these inferences. Fortunately, recently proposed OWL2 pro<sup>fi</sup>les (EL, QL and RL) have been demonstrated to be tractable for the main reasoning tasks (i.e. ontology consistency, class subsumption checking and instance checking). Additionally, De<sup>fi</sup>nitions 4–8 require intensive processing over the inferred taxonomy of O and the underlying graph structure of IS. For this reason, we have designed a series of indexes and data structures aimed to ef<sup>fi</sup>ciently perform the required operations. Next section is devoted to this issue.

## 5.2. Implementation

The process of identi<sup>fi</sup>cation and extraction of valid facts from a semantic data repository involves several steps. In the previous section we have explained the identi<sup>fi</sup>cation of facts by means of a conceptual MD schema de<sup>fi</sup>ned by the user. We have also lied down the foundations of valid facts from a semantic point of view. In this section we present an implementation for fact extraction that resembles ETL processes.

Fig. 10 sketches the steps involved in the fact extraction process. In the upper part of the <sup>fi</sup>gure we can see how ontology axioms (i.e., Tbox) are indexed in order to handle basic entailments and hence minimizing the need of a reasoner. This task needs to be performed just once for each ontology and it can be done off-line. The on-line phase is shown in the bottom part of Fig. 10. The <sup>fi</sup>rst task consists of creating the composition triples from the instance store (i.e., Abox) according to the user MD schema. These triples allow ef<sup>fi</sup>- cient instance retrieval as well as reachability queries. Then, we generate instance context tuples (see De<sup>fi</sup>nition 8) from the composition triples with the help of the indexes. Since each context tuple can give rise to multiple facts, we project them over the desired attributes speci<sup>fi</sup>ed in the user MD schema, obtaining the intended data fact tuples (see De<sup>fi</sup>nition 9). Finally, we apply the required transformations over data fact tuples (e.g., normalizing or making partitions of numeric values). Next sections illustrate the index structures and their role in the fact extraction process.

## 5.2.1. Ontology indexes

We have designed two indexes over the ontology in order to handle basic entailments namely: is-a index and aggregation index.

The is-a index is intended to ef<sup>fi</sup>ciently answer concept subsumption queries and ancestors/descendants range queries. Brie<sup>fl</sup>y, the construction of the index involves the following steps: the TBox is normalized and completion rules are applied to make implicit subsumptions explicit. This process is similar to that presented in [14]. Then, all “is-a” relationships are modeled as a graph where nodes correspond to concepts and edges to “is-a” relationships. An interval labeling scheme able to encode transitive relations is applied to the graph. As a result, each node (i.e., concept) has assigned a descriptor that includes compressed information about its descendant and ancestor nodes in the form of intervals. Moreover, we provide an interval's algebra over the node descriptors that allows performing basic DL operations over concepts. A detailed description of the indexing process and interval's algebra can be found in [30].

The aggregation index is an index structure that allows answering reachability queries between concepts (see De<sup>fi</sup>nition 3). In order to construct this index, we apply the same interval labeling scheme as before over the ontology graph $G = ( V , L , E )$ , where nodes in V are associated to the ontology classes, edge labels L represent the object property relation names and the $" _ { 1 S - Q " }$ relation and edges $e ( \nu _ { 1 } ,$ $v _ { 2 } ) \in E$ represent the asserted relationships $e { \in } L$ between nodes $\nu _ { 1 } ,$ $\nu _ { 2 } \in V .$ By encoding descendants (i.e., reachable nodes following edge direction) and ancestors (i.e., reachable nodes following inverse edge direction) for each node, we are able to encapsulate reachable nodes through both explicit and implicit aggregation paths. Going back to the graph fragment G showed in Fig. 8, concept Drug has among its ancestors (i.e., reachable nodes) not only DrugTherapy and Treatment, but also Visit through inheritance of hasReport property of Visit. The operation Contexts $\left( C _ { a } , C _ { b } , C _ { S U B } \right)$ (see De<sup>fi</sup>nition 4) can be easily implemented using the aggregation index as follows:

$$
\text { Contexts } (C _ {a}, C _ {b}, C _ {S U B}) = \bigcup_ {C \in n c a (C _ {a}, C _ {b}) \cap \text { descendants } (C _ {S U B})} (\text { ancestors } (C) \cup C)
$$

where operations nca, descendants and ancestors are ef<sup>fi</sup>ciently performed through the interval's algebra previously mentioned.

## 5.2.2. Instance store index

The main purpose of the instance store (IS) index is to ease the task of <sup>fi</sup>nding out if two instances, or an instance and a literal, are connected in the instance store (see De<sup>fi</sup>nition 5). This index is materialized as composition triples.

De<sup>fi</sup>nition 10. A composition triple is a statement of the form $( s , p , o )$ where the subject (s) and object (o) are resources, and the predicate (p) is a composition path from the subject to the object. A composition path is an alternate sequence of properties and resources that connect both the subject and the object.

For our purposes, the instance store index only keeps the composition triples that go from each instance of $C _ { S U B }$ (i.e., the subject of analysis) to each of the instances i such that C(i) where C is a sense of the dimensions and measures. Moreover, both the subject and object of a composition triple contain a reference to their concept type C in the is-a index. Consequently, we can perform searches over the composition triples not only at the instance level (i.e., by exact matching of instance names in the subject and object) but also at the conceptual level (i.e., by specifying the subject and object concepts). The main operation de<sup>fi</sup>ned over the composition triples is get\_instances(subject,path,object), where subject and object can be either a concept or instance, and path is a pattern matching string over the intended paths.

Table 3  
Data fact tuples generated for the running example.

<table><tr><td>Dimensions</td><td colspan="2">Disease</td><td>Drug</td><td>Gender</td><td>damageI.</td></tr><tr><td>Senses</td><td>Ultrasono.</td><td>Diagnosis</td><td>DrugTherapy</td><td>Patient</td><td>Rheuma.</td></tr><tr><td>PTN_XY21</td><td>Malformation</td><td>Arthritis</td><td>Methotrexate</td><td>Male</td><td>10</td></tr><tr><td>PTN_XY21</td><td>Malformation</td><td>Systemic_Arthritis</td><td>Methotrexate</td><td>Male</td><td>15</td></tr><tr><td>PTN_XY21</td><td>Malformation</td><td>Systemic_Arthritis</td><td>Corticosteroids</td><td>Male</td><td>15</td></tr><tr><td>PTN_XY21</td><td>Bad rotation</td><td>Systemic_Arthritis</td><td>Methotrexate</td><td>Male</td><td>15</td></tr><tr><td>PTN_XY21</td><td>Bad rotation</td><td>Systemic_Arthritis</td><td>Corticosteroids</td><td>Male</td><td>15</td></tr></table>

![](/api/attachments/HB6KCNM8/fulltext/images/350251b7b0e2d766c52f08974cae9da692d2f90a5d9fec80b9c41205f2741988.jpg)  
Fig. 10. ETL process for fact extraction.

Notice that the number of composition triples between two instances is equal to the number of unique paths in the IS graph for these instances. If the graph contains cycles, this number can be in<sup>fi</sup>- nite. To avoid this problem, we assume that the IS forms a DAG, which indeed usually occurs in real world applications. We also require the composition path between a subject and an object to be unique. This way the number of composition triples is limited to |subjects|×|objects| and the relation between a subject and an object is unambiguous, avoiding possible summarizability issues in the resulting facts due to redundancy.

Table 4 shows an excerpt of composition triples for the IS fragment in Fig. 9. The fourth column of the table shows the concept reference for the object. The concept reference for the subject is omitted because it is Patient for all the composition triples showed.

## 5.2.3. Instance context and data fact generation

Our method to generate instance context tuples according to De<sup>fi</sup>nition 8, does not perform an exhaustive search over the instance store, since checking the combinable condition (see De<sup>fi</sup>nition 7) for each pair of instances would result in a combinatorial explosion. Instead, we use the ontology axioms to just select proper contexts

## Table 4

An excerpt of the composition triples of instance store fragment in Fig. 9.

<table><tr><td>Subject</td><td>Composition path</td><td>Object</td><td>Type</td></tr><tr><td>PTN_XY21</td><td>/hasVisit</td><td>VISIT1</td><td>Visit</td></tr><tr><td>PTN_XY21</td><td>/hasVisit</td><td>VISIT2</td><td>Visit</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT1/hasReport</td><td>RHEX1</td><td>Rheumatology</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT1/hasReport/RHEX1/results</td><td>ULTRA1</td><td>Ultrasono.</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT1/hasReport</td><td>DIAG1</td><td>Diagnosis</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT1/hasReport/TREAT1/ hasTherapy</td><td>DT1</td><td>DrugTherapy</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT2/hasReport</td><td>RHEX2</td><td>Rheumatology</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT2/hasReport/RHEX2/results</td><td>ULTRA2</td><td>Ultrasono.</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT2/hasReport/RHEX2/results</td><td>ULTRA3</td><td>Ultrasono.</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT2/hasReport</td><td>DIAG2</td><td>Diagnosis</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT2/hasReport/TREAT2/ hasTherapy</td><td>DT2</td><td>DrugTherapy</td></tr><tr><td>PTN_XY21</td><td>/hasVisit/VISIT2/hasReport/TREAT2/ hasTherapy</td><td>DT3</td><td>DrugTherapy</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

that lead to valid combinations of instances. For this purpose we de-<sup>fi</sup>ne the following data structure.

De<sup>fi</sup>nition 11. Let O be an ontology (only the Tbox), C the subject concept, $D M = D \backslash$ ∪M the set of dimensions and measures and S the set of senses of the dimensions and measures. The Contexts Graph (CG) is a graph-like structure generated from O that satis<sup>fi</sup>es the following conditions:

1. The root of the CG is $C _ { S U B } .$

2. The rest of the nodes of the CG are $D M \cup S \cup \{ n d / \forall C _ { i } , C _ { j } , 1 \leq i , j \leq | S | ,$ $C _ { i } , C _ { j } { \in } S , n d { \in } c o n t e x t s ( C _ { i } , C _ { j } , C _ { S U B } ) \} .$

3. There is one edge from node nd to node nd iff $| P a t h s ( n d _ { i } , n d _ { j } ) | > 0 ,$ $\exists n d _ { k } \in n o d e s ( C G )$ such that $| P a t h s ( n d _ { i } , n \bar { d _ { k } } ) | > 0 \land | P a t h s ( n \bar { d _ { k } } , n d _ { j } ) |$ >0, where nodes(CG) denotes the set of nodes of CG.

The generation of the CG is performed by calculating context nodes of the dimensions and measures senses. This process is sup ported by the operations provided by the aggregation index.

Example 7. Given the conceptual MD schema of Example 5, the CG according to the previous de<sup>fi</sup>nition is shown in the upper part of Fig. 11, where shaded nodes act as contexts. The actual dimensions and measures are obviated for the sake of readability.

Algorithm 1 generates instance context tuples and uses the CG as a guide to process each subject instance (see Fig. 11). The main idea is to process the CG in depth in order to recursively collect and combine instances under context node instances. They are collected with the operation gI(i ,path,CG\_node), where each output instance is a tuple and path is recursively constructed as the CG is processed, re<sup>fl</sup>ecting the actual path. Tuples are combined with the cartesian product until complete context tuples are obtained. The resulting instance context tuples are shown in Table 2. Data fact tuples are generated according to De<sup>fi</sup>nition 9 by projecting instances over the dimensions and measures. The resulting data fact tuples are shown in Table 3.

## 6. Extracting dimensions

Once instance facts are extracted, the system can proceed to generate hierarchical dimensions from the concept subsumption relationships inferred from the ontology. These dimensions, however, must have an appropriate shape to perform properly OLAP operations. Therefore extracted hierarchies must comply with a series of constraints to ensure summarizability [22]. In this section, we propose a method to extract “good” hierarchies for OLAP operations from the ontologies in the repository, but preserving as much as possible the original semantics of the involved concepts. In this work we only consider taxonomic relationships, leaving as future work other kind of relationships (e.g. transitive properties, property compositions, etc.), which have been previously treated in the literature [34].

![](/api/attachments/HB6KCNM8/fulltext/images/71d16ca3922d0f144143170832e8657e2e8c734b10a0fadc1d8e163db5ed7ffd.jpg)  
Fig. 11. Contexts graph processing along with the generation of context tuples for instance store of Fig. 9. Shaded nodes correspond to contexts. Function gI is the short name for function get\_instances.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. Fact_Extraction_Algorithm
Require: CG: contexts graph (as global var.), CT: composition triples (as global var.), $i_{SUB} =$ “*”: subject instance, cpath = “*”: composition path, CG_node = CG.root: node from CG

Ensure: ICT: valid instance context tuples (as global var.)

1: tuples = ∅
2: Dvals = ∅
3: Cvals = ∅
4: instances = CT.get_instances($i_{SUB}$, cpath, CG_node)
5: for i ∈ instances do
6:    if $i_{SUB} ==$ “*” then
7:    $i_{SUB} = i$
8:    else
9:    cpath = concatenate(cpath, i)
10:    end if
11:    for n ∈ CG.successors(CG_node) do
12:    if not CG.context_node(n) then
13:    v = CT.get_instances($i_{SUB}$, cpath, n)
14:    add(Dvals, v)
15:    end if
16:    end for
17:    Dvals = cartesian_product(Dvals)
18:    for n ∈ CG.successors(CG_node) do
19:    if CG.context_node(n) then
20:    L = Fact_Extraction_Algorithm($i_{SUB}$, cpath, n)
21:    add(Cvals, L)
22:    end if
23:    end for
24:    Cvals = combine(Cvals)
25:    combs = cartesian_product(Dvals, Cvals)
26:    if CG.is_root_node(CG_node) then
27:    add(ICT, combs)
28:    else
29:    add(tuples, combs)
30:    end if
31: end for
32: return tuples
</div>

## 6.1. Dimension modules

The <sup>fi</sup>rst step to extract a hierarchical dimension $D _ { i }$ consists of selecting the part of the ontology that can be involved in it. Let Sig(D ) be the set of most speci<sup>fi</sup>c concepts of the instances participating in the extracted facts (see De<sup>fi</sup>nition 9).

We de<sup>fi</sup>ne the dimension module $M _ { D _ { i } } \subseteq O$ as the upper module of the ontology O for the signature $S i g ( D _ { i } )$ . We de<sup>fi</sup>ne upper modules in the same way as in [21,23,30], that is, by applying the notion of conservative extension. Thus, an upper module M of O for the signature Sig is a sub-ontology of O such that it preserves all the entailments over the symbols of $S i g$ expressed in a language ${ \mathcal { L } } ,$ that is, O ⊨ α with $S i g ( \alpha ) \subseteq S i g$ and $\alpha { \in } { \mathcal { L } }$ iff $M _ { D _ { i } } { \models } \alpha$

For OLAP hierarchical dimensions we only need to preserve entailments of the form C⊑D and C disjoint D, being C and D named concepts. Thus, the language of entailments corresponds to the typical reasoners output. This kind of upper modules can be extracted very ef-<sup>fi</sup>ciently over very large ontologies [30].

## 6.2. Dimension taxonomies

Let $T A X ( M _ { D _ { i } } )$ be the inferred taxonomy for the module $M _ { D _ { i ^ { \prime } } }$ which is represented as the directed acyclic graph (DAG) (V,E), where V contains one node for each concept in $M _ { D _ { i ^ { \prime } } }$ and $c _ { i } \to c _ { j } \in E { \mathrm { ~ i f ~ } } c _ { i }$ is one of the least common subsumers of $c _ { j }$ (i.e. direct ancestor). $T A X ( M _ { D _ { i } } )$ is usually an irregular, unbalanced and non-onto hierarchy, which makes it not suitable for OLAP operations. Therefore, it is necessary to transform it to a more regular, balanced and tree-shaped structure. However, this transformation is also required to preserve as much as possible the original semantics of the concepts as well as to minimize the loss of information (e.g. under-classi<sup>fi</sup>ed concepts). Former work about transforming OLAP hierarchies [33] proposed the inclusion of fake nodes and roll-up relationships to avoid incomplete levels and double counting issues. Normalization is also proposed as a way to solve non-onto hierarchies [26]. These strategies however are not directly applicable to ontology taxonomies for two reasons: the number of added elements (e.g. fake nodes or intermediate normalized tables) can overwhelm the size of the original taxonomy and, the semantics of concepts can be altered by these new elements. Recently, [15] proposes a clustering-based approach to reduce taxonomies for improving data tables summaries. This method transforms the original taxonomy to a new one by grouping those nodes with similar structures and usage in the tuples. However, this method also alters the semantics of the symbols as new ones are created by grouping original ones.

## 6.3. Selecting good nodes

Similarly to our previous work about fragment extraction [30], we propose to build tailored ontology fragments that both preserve as much as possible the original semantics of the symbols in $S i g ( D _ { i } )$ and present a good OLAP-like structure. For the <sup>fi</sup>rst goal, we will use the upper modules $M _ { D _ { i } }$ as the baseline for the hierarchy extraction. For the second goal, we propose a series of measures to decide which nodes deserve to participate in the <sup>fi</sup>nal hierarchy.

Before presenting the method, let us analyze why $T A X ( M _ { D _ { i } } )$ presents such an irregular structure. The usage of symbols in Sig(D ) can be very irregular due to the “popularity” of some symbols (i.e. Zipf law), which implies that few symbols are used very frequently whereas most of them are used few times. As a result, some parts of the taxonomy are more used than others, affecting to both the density (few dense parts and many sparse parts) and the depth of the taxonomy (few deep parts). A direct consequence is that some concepts in $S i g ( D _ { i } )$ are covered by many spurious concepts which are only used once, and therefore are useless for aggregation purposes. So, our main goals should be to identify dense regions of the taxonomy and to select nodes that best classify the concepts in $S i g ( D _ { i } )$ .

The <sup>fi</sup>rst measure we propose to rank the concepts in $T A X ( M _ { D _ { i } } )$ is the share:

$$
\operatorname{share} (n) = \prod_ {n _ {i} \in \operatorname{ancs} (n)} \frac {1}{| \text { children } (n _ {i}) |}
$$

where ancs(n) is the set of ancestors of n in $T A X ( M _ { D _ { i } } ) ,$ , and children(n) is the set of direct successors of n in the taxonomy.

The idea behind the share is to measure the number of partitions produced from the root till the node n. The smaller the share the more dense is the hierarchy above the node. In a regular balanced taxonomy the ideal share is $S ( n ) ^ { d e p t h ( n ) }$ , where S is the mean of children the ancestor nodes of n have. We can then estimate the ratio between the ideal share and the actual one as follows:

$$
\text { ratio } (n) = \frac {S (n) ^ {\text { depth } (n)}}{\text { share } (n)}
$$

Thus, the greater the ratio, the better the hierarchy above the node is.

The second ranking measure we propose is the entropy, which is de<sup>fi</sup>ned as follows:

$$
\begin{array}{c} \text {entropy(n) = \Sigma_ {n_{i} \in children(n)} P _ {sig} (n, n_{i})\cdot log\left(P _ {sig} (n, n_{i})\right)} \\ P _ {s i g} (n, n _ {i}) = \frac {\text {coveredSig} (n _ {i})}{\text {coveredSig} (n)} \end{array}
$$

where covered $S i g ( n )$ is the subset of $S i g ( D _ { i } )$ whose members are descendants of n.

The idea behind the entropy is that good classi<sup>fi</sup>cation nodes are those that better distribute the signature symbols among its children. Similarly to decision trees and clustering quality measures, we use the entropy of the groups derived from a node as the measure of their quality.

In order to combine both measures we just take the product of both measures:

$$
\operatorname{score} (n) = \operatorname{entropy} (n) \cdot \operatorname{ratio} (n).
$$

## 6.4. Generating hierarchies

The basic method to generate hierarchies consists of selecting a set of “good” nodes from the taxonomy, and then re-constructing the hierarchy by applying the transitivity property of the subsumption relationship between concepts. Algorithm 2 presents a global approach, which consists of selecting nodes from the nodes ranking until either all signature concepts are covered or there are no more concepts with a score greater than a given threshold (usually zero). Alternatively, we propose a second approach in Algorithm 3, the local approach, which selects the best ancestors of each concept leaf of the taxonomy. In both approaches, the <sup>fi</sup>nal hierarchy is obtained by extracting the spanning tree that maximizes the number of ancestors of each node from the resulting reduced taxonomy [30]. One advantage of the local approach is that we can further select the number of levels up to each signature concept, de<sup>fi</sup>ning so the hierarchical categories for the dimensions. However, this process is not trivial and we decided to leave it for future work. Each method favors different properties of the generated hierarchy. If the user wants to obtain a rich view of the hierarchy, she must select the global one. Instead, if the user wants a more compact hierarchy (e.g., few levels) then she must select the local one. Fig. 12 illustrates both approaches.

Algorithm 2. Global approach for dimension hierarchy generation Require: the upper module $( M _ { D _ { i } } )$ and the signature set $( S i g ( D _ { i } ) )$ for dimension $D _ { i } .$

Ensure: A hierarchy for dimension $D _ { i } .$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
nsure: A hierarchy for dimension $D_{i}$.
Let $L_{rank}$ be the list of concepts in $M_{D_i}$ ordered by score(n) (highest to lowest);
Let Fragment = ∅ be the nodes set of the fragment to be built.
repeat
    pop a node n from $L_{rank}$
    add it to Fragment
until score(n) ≤ 0 or $\cup_{n \in Fragment} coveredSig(n) == Sig(D_i)$
Let NewTax be the reconstructed taxonomy for the signature Fragment
return spanningTree(NewTax)
</div>

Algorithm 3. Local approach for dimension hierarchy generation Require: the upper module $( M _ { D _ { i } } )$ and the signature set $( S i g ( D _ { i } ) )$ for dimension $D _ { i } .$

Ensure: A hierarchy for dimension $D _ { i } .$

Let $L _ { l e a v e s }$ be the list of leaf concepts in $M _ { D _ { i } }$ ordered by ratio(n) (highest to lowest);

Let Fragment=∅ be the nodes set of the fragment to be built.

for all $c { \in } L _ { l e a v e s } { \mathbf { d o } }$

![](/api/attachments/HB6KCNM8/fulltext/images/3fd6b4a5033039d3f4026c34da43209878634690a1db57da1913b52603cdb1b8.jpg)

![](/api/attachments/HB6KCNM8/fulltext/images/2a337b9a5025f06f7423f7da7c8a28363e88798105d5de8dd3301f3b4af25f82.jpg)  
Fig. 12. Example of local and global methods: (a) node selection and (b) hierarchy reconstruction. Dashed edges in (b) are removed in the <sup>fi</sup>nal spanning tree. Nodes inside squares in (b) are those that change its parent in the resulting dimension.

Set up $L _ { a n c s } ( c )$ with the ancestors of c ordered by score(n) for all $ { n _ { a } } \in L _ { a n c s } ( c )$ do

if there is no node $n _ { 2 } { \in } L _ { a n c s } ( c )$ such that score $\left( n _ { 2 } \right)$ ≤ score $\left( n _ { a } \right)$ and order(n )≤ order(n ) then

$$
n _ {a} \notin
$$

$$
n _ {a}
$$

Let NewTax be the reconstructed taxonomy for the signature Fragment

return spanningTree(NewTax)

## 7. Evaluation

We have conducted the experiments by applying our method to a corpus of semantic annotations about rheumatic patients. The experimental evaluation has two differentiated setups. On one hand, we are concerned with scalability and performance issues regarding the generation of facts from the analyst requirements. On the other hand, we evaluate the two proposed methods for generating dimensions from the ontology knowledge by measuring the quality of the resulting hierarchies.

## 7.1. Fact extraction

The dataset used for the fact extraction evaluation has been synthetically generated from the features identi<sup>fi</sup>ed from a set of real patients. For this purpose, we have extended the XML generator presented in [36] with new operators speci<sup>fi</sup>c for RDF/OWL. The Tbox template has been carefully designed following the structure of the medical protocols de<sup>fi</sup>ned in the Health-e-Child<sup>5</sup> project for rheumatic patients. Moreover, domain concepts are taken from UMLS. With the previous setup, we are able to generate synthetic instance data of any size and with the intended structural variations to account for heterogeneity and optional values of semantic annotations. In particular, the dataset contains more than half million of instances.

Fig. 13 presents how the number of elements in the MD schema (i.e. number of dimensions and measures) affects the time performance to generate the fact table with all valid combinations of instances (i.e. data fact tuples). For the experiment setup we have preselected a set of 11 candidate dimensions and measures from the ontology and have computed all the fact tables that can be generated from all subsets of these 11 elements. The total number of fact tables $\mathrm { i } s 2 ^ { 1 1 } = 2 0 4 8$ . Then, we have organized the fact tables according to the number of dimensions and measures in their MD schema (x axis), from two dimensions to eleven. Axis y shows the time performance in seconds. Each boxplot in the <sup>fi</sup>gure shows the variance in time between fact tables having the same number of dimensions and measures. The explanation for this variance is that different MD con<sup>fi</sup>gurations of the same size may obtain very different CGs depending on their structural dependencies. Therefore, the number of instances processed and the levels of recursion are different, resulting in different processing times. In general, the time complexity increases linearly with respect to the number of dimensions and measures of the fact table, which proves the scalability and ef<sup>fi</sup>ciency of the approach.

On the other hand, we are also concerned about how the size of the instance store affects the generation of the fact tables. Fig. 14 illustrates the results. From the previous experiment we have selected one of the smallest (i.e., 2 elements) and the largest (i.e., 11 elements) MD schema speci<sup>fi</sup>cation. For these two MD con<sup>fi</sup>gurations we measure the time to create the respective fact tables with instance stores of different sizes, ranging from 100 to 3000 complex instances of type Patient. Notice axis x measures the number of subject instances, although the number of total instances in the store ranges from a thousand to more than half million instances. For both con<sup>fi</sup>gurations, the time performance is linear w.r.t. the size of the instance store, which means the proposed method is scalable.

## 7.2. Dimensions extraction

In order to measure the quality of the dimension hierarchies obtained with the methods proposed in Section 6 (i.e. global vs. local), we have adapted the measures proposed in [15], namely

$$
\begin{array}{l} \text { dilution } (D _ {i}, \text { Fragment }, T) = \frac {1}{| T |} \sum_ {t \in T} \Delta_ {0} \Big (\text { parent } _ {O} (t [ D _ {i} ]), \text { parent } _ {\text { Fragment }} (t [ D _ {i} ]) \Big) \\ \text { diversity } (D _ {i}, \text { Fragment }, T) = \frac {2}{(| T | ^ {2} - | T |)} \sum_ {t _ {1}, t _ {2} \in T, t _ {1} \neq t _ {2}} \Delta_ {\text { Fragment }} (t _ {1} [ D _ {i} ], t _ {2} [ D _ {i} ]) \end{array}
$$

where T is the fact table, hits(T, n ) is the times $n _ { i }$ has been used in $T ,$ paren $\mathrm { \bar { \rho } } ( n ) ^ { 6 }$ is the parent of n in O, and $\varDelta _ { 0 }$ is the taxonomic distance between two nodes in O. t[D<sub>i</sub>] represents the concept assigned to the fact t for the dimension $D _ { i } .$

Dilution measures the weighted average distance in the original taxonomy between the new and original parents of the signature concepts from dimension $D _ { i } .$ . The weight of each signature concept corresponds to its relative frequency in the fact table. The smaller the dilution, the less semantic changes have been produced in the reduced taxonomy. Diversity measures the weighted average distance in the reduced taxonomy of any pair of concepts from dimension $D _ { i }$ used in the fact table. The greater the diversity, the better taxonomies are obtained for aggregation purposes. A very low diversity value usually indicates that most concepts are directly placed under the top concept.

We have set up 25 signatures for 14 dimensions of the dataset described in the previous section. The size of these signatures ranges from 4 to 162 concepts (60 on average). The corresponding uppermodules are extracted from UMLS following the method proposed in [29]. The size of these modules ranges from 40 to 911 concepts (404 on average). Their inferred taxonomies present between 8 and 23 levels (17 on average). Results for the global and local methods are shown in Table 5.

From these results we can conclude that: (1) the local method generates smaller dimension tables, (2) the local method implies less signature lost, but dilution values of both methods are not statistically different and, (3) diversity is usually greater in the global method (i.e. richer taxonomies are generated). To sum up, each method optimizes different quality parameters, and therefore their application will depend on the user requirements.

## 7.3. Implementation

We use MySQL<sup>7</sup> database as back-end to store the semantic annotations (i.e. ABox), the domain and application ontologies (i.e. TBox) and the required indexes. On the other hand, we use the Business Intelligence (BI) tool of Microsoft SQL Server 2008<sup>8</sup> to instantiate the MD schema designed by the user and create cubes. Our method is completely independent of any data management system. We simply need to create an API to the back-end where the information is stored and the populated MD schema is delivered as a series of tables that can be fed into any off the shelf analysis tool.

Table 5  
time (s)  
![](/api/attachments/HB6KCNM8/fulltext/images/8c98aa940eca28df78fcd76e2e72bd3079509bf59ec4d0f5ce98e1ca8fa1a40f.jpg)  
Fig. 13. Fact table generation performance w.r.t. the number of dimensions and measures involved.

In Fig. 15 we show the result of one of the MD queries proposed for the use case in Section 2. In this use case, the user is interested in analyzing the ef<sup>fi</sup>cacy of different drugs w.r.t. a series of dimensions, such as the disease diagnosed, the patient's age, gender, etc. The method <sup>fi</sup>rst generates the fact table according to the conceptual MD schema proposed by the analyst and then, for each dimension, a dimension hierarchy is extracted using the global approach. The result (i.e. the populated MD schema) has been fed to SQL Server and the BI tool allows the analyst to create cubes and navigate through them. In particular, Fig. 15 shows the cube generated by averaging the damageIndex measure by disease (rows) and drug (columns). As shown, the user can navigate through the different levels of the dimension hierarchies and the measures are automatically aggregated. It is worth mentioning the added value that provides the semantics involved in the aggregations, since the dimension hierarchies express conceptual relations extracted from a domain ontology.

## 8. Related work

Although there is a signi<sup>fi</sup>cant amount of literature that relates to different aspects of our approach (e.g. SW, MD models, OLAP analysis, etc.), there is little or no research that addresses the analysis of semantic web data (i.e. RDF/(S) and OWL) by using the abovementioned technologies. However, we <sup>fi</sup>nd worth reviewing some work on querying and analysis over heterogeneous XML data, which is the standard on which SW languages rely on.

Some research has focused on querying complex XML scenarios where documents have a high structural heterogeneity. In [25,41] it is shown that XQuery is not the most suitable query language for data extraction from heterogeneous XML data sources, since the user must be aware of the structure of the underlying documents. The lowest common ancestor (LCA) semantics can be applied instead to extract meaningful related data in a more <sup>fl</sup>exible way. Li et al. and Xu and Papakonstantinou [25,41] apply some restrictions over the LCA semantics. In particular they propose SLCA [41] and MLCA [25] whose general intuition is that the LCA must be minimal. However, in [28,32] they showed that these approaches still produced undesired combinations between data items in some cases (e.g. when a data item needs to be combined with a data item at a lower level of the document hierarchy). In order to alleviate the previous limitations they propose the SPC (smallest possible context) data strategy, which relies on the notion of closeness of data item occurrences in an XML document. There exist other strategies to extract transactions or facts from heterogeneous XML [38]. However, they are used in data mining applications and they do not care for OLAP properties such as “good” dimensions and summarizability issues. We face similar challenges as the previous approaches mainly due to the structural heterogeneity of the semantic annotations. However, we still need to deal with the semantics, which requires logical reasoning in order to derive implicit information.

![](/api/attachments/HB6KCNM8/fulltext/images/101c28be4c1e4ff5e6de6def202895ba73cdeb47d8558ea07faab9a0d5d1c36d.jpg)  
Fig. 14. Increase in the time complexity w.r.t. the size of the instance store.

Other approaches such as [34,35] try to incorporate semantics in the design of a data warehouse MD schema by taking as starting point an OWL ontology that describes the data sources in a semiautomatic way. Instead of looking for functional dependencies (which constitute typical fact-dimension relations) in the sources, they are derived from the ontology. However, this work focuses on the design phase, overlooking the process of data extraction and integration to populate the MD schema. This issue is partially addressed in [24] by using SPARQL over RDF-translated data sources. However, this is not appropriate for expressive and heterogeneous annotations. By combining IE techniques with logical reasoning, in [18] they propose a MD model specially devised to select, group and aggregate the instances of an ontology. In our previous work [31] we de<sup>fi</sup>ne the semantic data warehouse as a new semi-structured repository consisting of semantic annotations along with their associated set of ontologies. Moreover, we introduce the multidimensional integrated ontology (MIO) as a method for designing, validating and building OLAP-based cubes for analyzing the stored annotations. However, the fact extraction and population is pointed out in a shallow way and it is the main concern of the current paper.

Results for global and local dimension extraction methods. Value ranges represent the 0.75 confidence intervals of the results for all the signatures

<table><tr><td>Measure</td><td>Global</td><td>Local</td></tr><tr><td>Reduction (%)</td><td>72.5–75.9</td><td>76.5–79.8</td></tr><tr><td>Sig. lost (%)</td><td>7.08–12.12</td><td>3.5–7.8</td></tr><tr><td>Dilution</td><td>0.367–0.473</td><td>0.342–0.429</td></tr><tr><td>Diversity</td><td>9.08–10.79</td><td>7.72–9.46</td></tr></table>

Level 02Level 03

<table><tr><td rowspan="2" colspan="3"></td><td rowspan="2" colspan="2">LEVEL 02 - Level 03</td><td rowspan="2">C0003209=anti-inflammatory</td><td rowspan="2">C0021054=Factors,Immunologic</td><td colspan="2">C2170827=tumornecrosisfactoralphablockers</td></tr><tr><td>C0666743=INFLIX</td><td>C1122087=tumornecrosis</td></tr><tr><td>Level 02</td><td>Level 03</td><td>Level 04</td><td>Avg damage Index</td><td>Avg damage Index</td><td>Avg damage Index</td><td>Avg damage Index</td><td>Avg damage Index</td><td></td></tr><tr><td rowspan="8">C0003873=Arthritisorpol</td><td colspan="2">C0409651=rheumatoid/seropositivearthritis</td><td>26,10167</td><td>26,14971</td><td>26,16316</td><td>26,50977</td><td></td><td></td></tr><tr><td colspan="2">C0427391=Rheumatoidfactormegative</td><td>26,64191</td><td>26,93696</td><td>27,21934</td><td>27,03086</td><td></td><td></td></tr><tr><td rowspan="5">C0553662=IdiopathicArth</td><td>C1384600=Juvenilearthritiswithsyste</td><td>26,18157</td><td>26,48039</td><td>26,67122</td><td>27,00051</td><td></td><td></td></tr><tr><td>C1444840=Juvenileseronegativepoly</td><td>26,77114</td><td>26,97851</td><td>27,29854</td><td>27,24215</td><td></td><td></td></tr><tr><td>C1444841=Juvenileidiopathicarthritis</td><td>27,21066</td><td>26,63931</td><td>26,25423</td><td>26,79112</td><td></td><td></td></tr><tr><td>C1444844=juvenileidiopathicarthritis</td><td>27,22942</td><td>27,60329</td><td>26,49961</td><td>26,82511</td><td></td><td></td></tr><tr><td>Total</td><td>26,83747</td><td>26,92224</td><td>26,67816</td><td>26,96601</td><td></td><td></td></tr><tr><td colspan="2">Total</td><td>26,68180</td><td>26,79518</td><td>26,69152</td><td>26,89885</td><td></td><td></td></tr><tr><td colspan="3">Total general</td><td>26,68180</td><td>26,79518</td><td>26,69152</td><td>26,89885</td><td></td><td></td></tr></table>

Fig. 15. Example of MD cube created by averaging the damageIndex measure by disease (rows) and drug (columns)

## 9. Conclusions

More and more semantic data are becoming available on the web thanks to several initiatives that promote a change in the current Web towards the Web of Data, where the semantics of data become explicit through data representation formats and standards such as RDF/(S) and OWL. However, this initiative has not yet been accompanied by ef<sup>fi</sup>cient intelligent applications that can exploit the implicit semantics and thus, provide more insightful analysis.

In this paper, we investigate how semantic data can be dynamically analyzed by using OLAP-style aggregations, navigation and reporting. We propose a semi-automatic method to build valid MD fact tables from stored semantic data expressed in RDF/(S) and OWL formats. This task is accomplished by letting the user compose the conceptual MD schema by selecting domain concepts and properties from the ontologies describing the data. Dimension hierarchies are also extracted from the domain knowledge contained in the ontologies. The bene<sup>fi</sup>ts of our method are numerous, however we highlight the following: 1) we provide a novel method to exploit the information contained in the semantic annotations, 2) the analysis is driven by the user requirements and it is expressed always at the conceptual level, and 3) the analysis capabilities (i.e. the OLAP-style aggregations, navigation, and reporting) are richer and more meaningful, since they are guided by the semantics of the ontology. To our knowledge, this is the <sup>fi</sup>rst method addressing this issue from ontological instances. Hence, we do believe this work opens new interesting perspectives as it bridges the gap between the DW and OLAP tools and SW data.

As future work, we plan to improve the method in several aspects. In particular, we plan to extend the local method for generating dimension hierarchies so that the dimension values can be grouped into a de<sup>fi</sup>ned number of levels or categories. We are also working on an extended conceptual MD speci<sup>fi</sup>cation for the analyst in terms of richer ontology axioms. Regarding performance issues, a promising direction is the application of bitmap indexing techniques to SW data management, including ef<sup>fi</sup>cient reasoning. Finally, we are also concerned about different SW scenarios where the development of the ontology axioms and the instance store is not coupled. In such scenarios, we need to study how to treat the possible vagueness of the ontology axioms (or even absence) w.r.t. to the instance store, which hinders the proposed extraction of facts.

## Acknowledgments

This research has been partially funded by the Spanish Research Program (TIN2008-01825/TIN) and the Health-e-Child integrated EU project. Victoria Nebot was supported by the PhD Fellowship Program of the Spanish Ministry of Science and Innovation (AP2007-02569).

## References

[1] GALEN ontology, http://www.opengalen.org/.

[2] GO: The Gene Ontology, http://www.geneontology.org/.

[3] Linked life data, http://linkedlifedata.com/.

[4] Linking Open Drug Data (LODD), http://esw.w3.org/HCLSIG/LODD.

[5] MEDLINE: National Library of Medicine"s database, http://www.nlm.nih.gov/ databases/databases\_medline.html.

[6] SNOMED CT: Systematized Nomenclature of Medicine—Clinical Terms, http:// www.ihtsdo.org/snomed-ct/

[7] The Universal Protein Resource: UniProt, http://uniprot.org.

[8] F. Baader, D. Calvanese, D.L. McGuinness, D. Nardi, P.F. Patel-Schneider (Eds.), The Description Logic Handbook: Theory, Implementation, and Applications, Cambridge University Press, 2003

[9] F. Belleau, M.-A. Nolin, N. Tourigny, P. Rigault, J. Morissette, Bio2rdf: Towards a mashup to build bioinformatics knowledge systems, Journal of Biomedical Informatics 41 (2008) 706–716.

[10] R. Berlanga, E. Jiménez-Ruiz, V. Nebot, D. Manset, A. Branson, T. Hauer, R. McClatchey, D. Rogulin, J. Shamdasani, S. Zillner, J. Freund, Medical data integration and the semantic annotation of medical protocols, CBMS, IEEE Computer Society, 2008, pp. 644–649.

[11] C. Bizer, T. Heath, T. Berners-Lee, Linked data — the story so far, International Journal on Semantic Web and Information Systems 5 (3) (2009) 1–22.

[12] O. Bodenreider, The Uni<sup>fi</sup>ed Medical Language System (UMLS): integrating biomedical terminology, Nucleic Acids Research 32 (Database issue) (2004).

[13] O. Bodenreider, Biomedical ontologies in action: role in knowledge management, data integration and decision support, Yearbook of medical informatics, 2008, pp. 67–79.

[14] S. Brandt, Polynomial time reasoning in a description logic with existential restrictions, GCI axioms, and — what else? ECAI, 2004, pp. 298–302.

[15] K.S. Candan, M. Cataldi, M.L. Sapino, Reducing metadata complexity for faster table summarization, in: I. Manolescu, S. Spaccapietra, J. Teubner, M. Kitsuregawa, A. Léger, F. Naumann, A. Ailamaki, F. Özcan (Eds.), EDBT, Volume 426 of ACM International Conference Proceeding Series, ACM, 2010, pp. 240–251.

[16] G. Cheng, W. Ge, Y. Qu, in: J. Huai, R. Chen, H.-W. Hon, Y. Liu, W.-Y. Ma, A. Tomkins, X. Zhang (Eds.), Falcons: Searching and Browsing Entities on the Semantic Web, ACM, 2008 pp. 1101-1102. WWW

[17] E.F. Codd, S.B. Codd, C.T. Salley, Providing OLAP (On-Line Analytical Processing) to User Analysts: An IT Mandate, E. F. Codd and Ass, 1993.

[18] R. Dánger, R.B. Llavori, Generating complex ontology instances from documents, Journal of Algorithms 64 (1) (2009) 16–30.

[19] M. dAquin, C. Baldassarre, L. Gridinoc, S. Angeletou, M. Sabou, E. Motta, Watson: a gateway for next generation semantic web applications, Poster, ISWC 2007, 2007.

[20] L. Ding, T. Finin, A. Joshi, R. Pan, S.R. Cost, Y. Peng, P. Reddivari, V. Doshi, J. Sachs, Swoogle: a search and metadata engine for the semantic web, CIKM'04: Proceedings of the Thirteenth ACM Conference on Information and Knowledge Management, ACM Press, New York, NY, USA, 2004, pp. 652–659.

[21] B.C. Grau, I. Horrocks, Y. Kazakov, U. Sattler, Modular reuse of ontologies: theory and practice, Journal of Arti<sup>fi</sup>cial Intelligence Research (JAIR) 31 (2008) 273–318.

[22] C.A. Hurtado, C. Gutierrez, A.O. Mendelzon, Capturing summarizability with integrity constraints in OLAP, ACM Transactions on Database Systems 30 (3) (2005) 854–886.

[23] E. Jiménez-Ruiz, B. Cuenca-Grau, U. Sattler, T. Schneider, R. Berlanga, Safe and economic re-use of ontologies: a logic-based methodology and tool support, in: S. Bechhofer, M. Hauswirth, J. Hoffmann, M. Koubarakis (Eds.), ESWC, Volume 5021 of Lecture Notes in Computer Science, Springer, 2008, pp. 185–199.

[24] R. Kimball, M. Ross, The Data Warehouse Toolkit: The Complete Guide to Dimensional Modeling, 2nd edition Wiley, April 2002.

[25] Y. Li, C. Yu, H.V. Jagadish, Schema-free XQuery, VLDB"04: Proceedings of the Thirtieth International Conference on Very Large Data Bases, VLDB Endowment, 2004, pp. 72–83.

[26] J.-N. Mazón, J. Lechtenbörger, J. Trujillo, A survey on summarizability issues in multidimensional modeling, Data & Knowledge Engineering 68 (12) (2009) 1452–1469.

[27] M. Mesiti, E. Jiménez-Ruiz, I. Sanz, R.B. Llavori, P. Perlasca, G. Valentini, D. Manset, Xml-based approaches for the integration of heterogeneous bio-molecular data, BMC Bioinformatics 10 (S-12) (2009) 7.

[28] T. Näppilä, K. Järvelin, T. Niemi, A tool for data cube construction from structurally heterogeneous XML documents, JASIST 59 (3) (2008) 435–449.

[29] V. Nebot, R. Berlanga, Building tailored ontologies from very large knowledge resources ICEIS Conference Proceedings, volume 2, ICEIS, May 2009, pp. 144–151.

[30] V. Nebot, R. Berlanga, Ef<sup>fi</sup>cient retrieval of ontology fragments using an interval labeling scheme, Information Sciences 179 (24) (2009) 4151–4173

[31] V. Nebot, R. Berlanga, J.M. Pérez, M.J. Aramburu, T.B. Pedersen, Multidimensional integrated ontologies: a framework for designing semantic data warehouses, JoDS XIII 5530 (2009) 1–35.

[32] T. Niemi, T. Näppilä, K. Järvelin, A relational data harmonization approach to XML, Journal of Information Science 35 (5) (2009) 571–601.

[33] T.B. Pedersen, C.S. Jensen, C.E. Dyreson, A foundation for capturing and querying complex multidimensional data, Information Systems 26 (5) (2001) 383–423.

[34] O. Romero, A. Abelló, Automating multidimensional design from ontologies DOLAP'07, ACM, New York, NY, USA, 2007, pp. 1–8.

[35] O. Romero, D. Calvanese, A. Abelló, M. Rodriguez-Muro, Discovering functional dependencies for multidimensional design, in: I.-Y. Song, E. Zimányi (Eds.), DOLAP, ACM, 2009, pp. 1–8.

[36] I. Sanz, M. Mesiti, G. Guerrini, R. Berlanga, Fragment-based approximate retrieval in highly heterogeneous XML collections, Data & Knowledge Engineering 64 (1) (2008) 266–293.

[37] K. Skaburskas, F. Estrella, J. Shade, D. Manset, J. Revillard, A. Rios, A. Anjum, A. Branson, P. Bloodsworth, T. Hauer, R. McClatchey, D. Rogulin, Health-e-Child: a grid platform for European Paediatrics, Journal of Physics Conference Series 119 (2008).

[38] A. Tagarelli, S. Greco, Semantic clustering of XML documents, ACM Transactions on Information Systems 28 (1) (2010).

[39] G. Tummarello, R. Cyganiak, M. Catasta, S. Danielczyk, R. Delbru, S. Decker, Sig.ma: live views on the web of data, Journal of Web Semantics 8 (4) (2010) 355–364

[40] H. Wang, Q. Liu, T. Penin, L. Fu, L. Zhang, T. Tran, Y. Yu, Y. Pan, Semplore: a scalable IR approach to search the web of data, Web Semantics 7 (September 2009) 177–188.

[41] Y. Xu, Y. Papakonstantinou, Ef<sup>fi</sup>cient keyword search for smallest LCAs in XML databases, SIGMOD'05: Proceedings of the 2005 ACM SIGMOD International Conference on Management of Data, ACM, New York, NY, USA, 2005, pp. 527–538.

![](/api/attachments/HB6KCNM8/fulltext/images/64bd17e6fd34aa837fdb91695a8821fac7e3e11d3059c257a8d1c1fee2986905.jpg)  
Victoria Nebot received her B.S. degree in Computer Science from Universitat Jaume I, Spain, in 2007. She joined the Temporal Knowledge Bases Group (TKBG) at Universitat Jaume I as a PhD Student in 2008. Her main research is focused on analyzing and exploiting semi-structured and complex data derived mainly from the Semantic Web. In particular, she is interested in applying data warehousing and OLAP techniques that enable to analyze semantic data for decision support system tasks and the application of these techniques to the biomedical domain.

![](/api/attachments/HB6KCNM8/fulltext/images/a640d1bf2259c1ac9cc2f34c7b59ac70fe995bbb205e68e8dbbe1906a679bd63.jpg)

Rafael Berlanga is associate professor of Computer Science at Universitat Jaume I, Spain, and the leader of the TKBG research group. He received the BS degree from Universidad de Valencia in Physics, and the PhD degree in Computer Science in 1996 from the same university. In the past, his research was focused on temporal reasoning and planning in AI. His current research interests include knowledge bases, information retrieval and the semantic web. He has directed several research projects and has published in several journals and international conferences in the above areas.
