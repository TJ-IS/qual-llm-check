---
otero_id: 3566
otero_key: "BGX9R599"
title: "An MDA approach for the development of data warehouses"
authors: "Jose-Norberto Mazón; Juan Trujillo"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.12.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An MDA approach for the development of data warehouses

Jose-Norberto Mazón <sup>⁎</sup>, Juan Trujillo

Department of Software and Computing Systems, University of Alicante, Spain

Available online 26 January 2007

## Abstract

Different modeling approaches have been proposed to overcome every design pitfall of different data warehouse (DW) components. However, most of them offer partial solutions that deal only with isolated aspects of the DW and do not provide developers with an integrated and standard framework for designing all DW relevant components, such as ETL processes, data sources, DW repository and so on. To overcome this problem, this paper describes how to align the whole DW development process with a Model Driven Architecture (MDA) framework. We then focus on describing one part of it: an MDA approach for the development of the DW repository, because it is the cornerstone of any DW system. Therefore, we describe how to build the different MDA models for the DW repository by using an extension of the Unified Modeling Language (UML) and the Common Warehouse Metamodel (CWM). Transformations between models are also clearly and formally established by using the Query/ View/Transformation (QVT) language. Finally, a case study is provided to exemplify the benefits of our MDA framework. © 2006 Elsevier B.V. All rights reserved.

Keywords: Data warehouse; Multidimensional modeling; MDA; QVT

## 1. Introduction

Data warehouses (DW) play a central role in current Decision Support Systems (DSS) because they provide crucial business information to improve strategic decision-making processes [8]. However, building a DW is still a challenging and complex task because it consists of several interrelated components with different functions, different design pitfalls, and different technologies [11]. In fact, the components of a DW are usually depicted as a multi-layer architecture in which data from one layer is derived from data of the previous layer [10] as seen in Fig. 1. Different methods and approaches have been proposed for the design of each DW layer. Nevertheless, these methods do not deal with the design of the whole DW in an integrated modeling framework. Instead, they provide isolated solutions for the development of certain layers, such as, ETL (Extraction-Transformation-Load) processes, DW repository, and so on. Therefore, many problems may arise from the interoperability and integration of the different layers.

To overcome this problem, our previous work [15] has defined a DW development framework based on the UML (Unified Modeling Language) [27] and the UP (Unified Process) [9]. This framework addresses the design of the whole DW by using several UML profiles. These profiles have been developed to adapt UML to certain aspects of the DW design, such as the multidimensional (MD) modeling of the DW repository [16,17,19] and the modeling of ETL processes [32], as well as of data mappings between data sources and targets [18]. This UP-based framework has a clear benefit: using the same standard notation (UML) to tackle the design of every DW component in an integrated manner, so as to provide easier interoperability among the DW layers.

![](/api/attachments/BGX9R599/fulltext/images/e158fdbe33ab2aeb590a33c2677f5b59f77a674909f5a98364ef0a2c4406eb54.jpg)  
Fig. 1. Multi-layer architecture of data warehouses.

Unfortunately, this development framework may be a little complex for non-expert designers as they can use up to 15 different diagrams. Furthermore, the development focuses on a conceptual model of every DW layer, and not much attention is paid to the transformation of these conceptual models into the final implementation of the DW.

On the other hand, the Model Driven Architecture (MDA) is a standard framework for software development by using models [24]. This framework separates the specification of system functionality in a Platform Independent Model (PIM) from the specification of the implementation of that functionality on a specific technology in a Platform Specific Model (PSM). Furthermore, the system requirements are specified in a Computation Independent Model (CIM). MDA not only allows the development of these models in a formal and integrated way by using a standard notation, but also the specification of model transformations in order to obtain the final software product. The MOF 2.0 Query/ View/Transformation (QVT) language [28] allows the formal definition of these transformations provided that the models are MOF-compliant. The main benefit of MDA is that less time and effort are needed to develop the whole software system, thus improving productivity. Furthermore, MDA provides support for system evolution, integration, interoperability, portability, adaptability and reusability [3,12,23].

Considering all these aspects, the present paper describes an MDA framework for the development of DWs.<sup>1</sup> The first step is developing a CIM that acquires user requirements. Then, according to this CIM, every DW layer is modeled by a corresponding PIM using several UML profiles. The resulting PIMs represent conceptual models of each DW component, without any reference to a concrete target platform or a specific technology. Then, each PIM can be automatically mapped to several PSMs, depending on the required target platform, by using formal QVT transformations. Finally, each derived PSM provides the code according to a platform-specific DW implementation.

The main advantages of our framework are the following: (i) the complex task of designing the whole DW is tackled in a systematic, well-structured and standard way, since MDA is applied; (ii) the design follows an integrated modeling framework, thus avoiding layer interoperability and integration problems; and (iii) the DW implementation can be derived from the previously developed PIMs by using a set of clear and formal QVT transformations, thus saving time and effort.

Once our MDA framework is introduced, we focus on describing its application to the MD modeling of the DW repository, since it is one of the most crucial issues of the DW architecture [11]. Several approaches [7,13,33] have been proposed for the design of the DW repository. These proposals try to represent the main MD properties at a conceptual level by abstracting away details of an envisaged DW implementation platform. Then, most of them describe a set of informal guidelines to transform a conceptual model into its logical representation tailored to a specific implementation technology (normally a relational implementation based on the star schema [11] or one of its variants). Unfortunately, none of these approaches defines a set of formal transformations in order to: (i) univocally and automatically derive every possible logical representation from the conceptual model; or (ii) help the designer to obtain the most suitable logical representation of the developed conceptual model.

To overcome this problem, this paper describes how to build the different MDA models for the development of the DW repository by using our UML profile for the MD modeling of DWs [19] and the Resource layer of the Common Warehouse Metamodel (CWM) [25]. Furthermore, a set of formal transformations is defined by means of QVT.

The present paper is structured as follows. Section 2 presents the most relevant related work for DW development. An overview of MDA and QVT is presented in Section 3. We introduce our MDA framework for DW development in Section 4. Section 5 outlines our MDA approach for the MD modeling of the DW repository. A case study is presented in Section 6. Finally, Section 7 presents our conclusions and sketches in our intended future work.

## 2. Related work

Various approaches for the development of DW systems have been proposed in the last few years. In this section, we present a brief discussion about some of the most well-known approaches.

In [11], different case studies of DWs are presented. The DW design is based on the use of the star schema and its different variations (snowflake and fact constellation) by using a relational approach, i.e. tables, columns, foreign keys, and so on. Although we consider this work as a fundamental reference in the DW field, authors are only concerned about a relational representation of the DW, and no other kind of technology is considered.

In [7], authors propose the Dimensional-Fact Model (DFM), a particular notation for the DW conceptual design. They also include how to derive a DW schema from the data sources described by Entity-Relationship (ER) schemas. Moreover, a goal-oriented approach to requirement analysis for DW [5] have been added to the DFM. From our point of view, this proposal is only oriented to the conceptual and logical design of the DWs repository, because it does not consider important aspects such as the design of ETL processes. Furthermore, authors assume the existence of all the ER schemas of the data sources, which unfortunately is not always true. Finally, we consider that the use of a particular notation makes the application of this proposal difficult.

In [33], the building of a conceptual MD model of the DW repository from the conceptual schemas of the operational data sources is proposed. Once again, it is highly understood that the data sources are defined by means of ER schemas. Moreover, authors only point out that several logical representations can be obtained from the conceptual model, but a set of formal transformations is not given. Finally, this proposal does not tackle every component of the DW and it is only concerned about the development of the DW repository.

In [1], a conceptual MD model for designing the DW repository is presented: YAM2. It is an object-oriented model that uses UML as a notation to represent the MD data structures. However, authors only focus on the design of the DW repository and no other DW component is considered. Furthermore, how to obtain a logical representation of the conceptual model is not described in this paper.

In [13], authors propose a well-structured approach to formalize the development of the DW repository. They propose a set of multidimensional normal forms in order to obtain the correct conceptual model of the DW repository from the operational data sources. Unfortunately, authors informally derive a relational representation from the conceptual model, but no formal transformations are defined to obtain this logical model.

Concerning the development of ETL processes, a conceptual model is proposed in [34]. This model is customized for the tracing of interattribute relationships and the respective ETL activities in the early stages of a DW project. Furthermore, in [35], the logical design of ETL scenarios is presented. This logical design is based on a metamodel particularly customized for the definition of ETL activities by following a workflowlike approach, where the output of a certain activity can either be stored persistently or passed to a subsequent activity. A recent work [31] has proposed a formal transformation between these conceptual and logical models. However, this approach is not based on a standard like QVT.

As a survey, we believe that the above-presented approaches: (i) do not define a systematic, wellstructured and standard approach for the development of every DW layer; (ii) do not provide methods to design the DW in an integrated manner to avoid interoperability and integration problems between DW layers; or (iii) do not define formal and standard transformations in order to univocally and automatically derive every possible logical representation from a conceptual model or help the designer to obtain the most suitable logical representation of the conceptual model.

On the other hand, to the best of our knowledge, only one effort has been developed for aligning the DW design with the general MDA framework, the Model Driven Data Warehousing (MDDW) [29]. This approach is based on the CWM [25] which provides a set of metamodels that are comprehensive enough to model an entire DW including data sources, ETL processes, MD modeling, and so on. However, according to [22],

CWM metamodels are (i) too generic to represent all peculiarities of MD modeling at a conceptual level (i.e. PIM) and; (ii) too complex to be handled by both final users and designers, so we believe that it is more reliable to design a PIM by using an enriched conceptual modeling approach that is easy to handle (e.g. [16,17,19]), and then transform this PIM into a CWM-compliant PSM in order to assure the interchange of DW metadata between different platforms and tools.

## 3. MDA and QVT overview

Model Driven Architecture (MDA) is an Object Management Group (OMG) standard [24] that addresses the complete life cycle of designing, deploying, integrating, and managing applications by using models in software development. MDA separates the specification of system functionality from the specification of the implementation of that functionality on a specific technology platform by means of defining several viewpoints on a system. A viewpoint on a system is a technique for abstracting away details in order to focus on particular concerns within that system and establish a simplified model [24]. MDA defines the following viewpoints: computation independent, platform independent, and platform specific. Therefore, MDA encourages specifying a Platform Independent Model (PIM) which contains no specific information to the platform or the technology that is used to realize it. Then, this PIM can be transformed into a Platform Specific Model (PSM) in order to include information about a specific technology or platform. Afterwards, each PSM is transformed into code to obtain the final implementation. On top of these models, MDA also presents a Computation Independent Model (CIM). This model focuses on specifying system requirements, showing what the system is expected to do without showing details about how it is constructed.

These MDA models can be developed using any modeling language, but typically MOF-compliant languages (as UML) are used since they are standard modeling languages for general purpose and, at the same time, they can be extended to define specialized languages for certain domains (i.e. metamodel extensibility or profiles).

In Fig. 2, we can see how the different models are related to each other. The requirements of the intended system are addressed in a CIM. Afterwards, this CIM is derived into a PIM. Then, this PIM can be automatically transformed into different PSMs according to different platforms or technologies. Finally, code is generated from each PSM in order to obtain the final software product. However, apart from these PIM–to–PSM transformations, PIM–to–PIM or PSM–to–PSM transformations can be also developed, since different kinds of model transformations are defined in MDA [24]:

![](/api/attachments/BGX9R599/fulltext/images/ca9d6c7830b61dbcfcd71a736488d8e9949f800bf660ffd9cd38674d515d234f.jpg)  
Fig. 2. Model Driven Architecture framework.

• Vertical transformations: a source model is transformed into a target one at a different level of abstraction (e.g. a PIM is transformed into a PSM).

• Horizontal transformations: a source model is transformed into a target model that is at the same level of abstraction (e.g. a PIM is transformed into another PIM).

• Merging transformations: multiple source models are combined into a single target model (e.g. two different PIMs are transformed into a PSM).

Currently, one of the most crucial issue in MDA is the definition of these transformations between models in a formal way [12,24]. These formal transformations must allow to automatically derive models assuring semantic correctness [2,4]. Furthermore, they must be easily readable, understandable, adaptable, and maintainable [30]. To this aim, OMG proposes the MOF 2.0 Query/View/Transformation (QVT) language [28], a standard approach for defining formal transformations between MOF-compliant models (e.g. UML models). This standard defines a hybrid specification for transformations. On the one hand, there is a declarative part, which provides mechanisms to define transformations as a set of relations that must hold between the model elements of a set of candidate models (source and target models). This declarative part can be split into two layers according to the level of abstraction: the relational layer that provides graphical and textual notation for a declarative specification of relations, and the core layer that provides a simpler, but verbose, way of defining transformations. On the other hand, QVT also proposes an imperative part which defines operational mappings that extend the declarative part with imperative implementations when it is difficult to provide a purely declarative specification of a relation.

In this paper, we focus on the relational layer of QVT. This layer supports the specification of relationships that must hold between MOF models by means of a relations language. A set of these relations (or transformation rules) defines a transformation between models. A relation is defined by the following elements:

• Two or more domains: each domain is a distinguished set of elements of a candidate model (source or target model). This set of elements must be matched in that model by means of patterns. A domain pattern can be considered as a template for elements, their properties and their associations, that must be located, modified, or created in a candidate model in order to satisfy the relation. The kind of relation between domains must be specified, since it can be marked as checkonly (labeled as C) or as enforced (labeled as E). When a relation is executed in the direction of a checkonly domain, then it is only checked if there exists a valid match in the model that satisfies the relationship (without modifying any model if the domains do not match); whereas for a domain that is enforced, when the domains do not match, model elements are created, deleted or modified in the target model in order to satisfy the relationship. Moreover, for each domain the name of its underlying metamodel is specified.

• When clause: it specifies the conditions under which the relation needs to hold (i.e. precondition).

• Where clause: it specifies the conditions that must be satisfied by all model elements participating in the relation (i.e. postcondition).

For further information about MDA and QVT, we refer the reader to [3,12,23,24,28].

## 4. An MDA framework for the development of data warehouses

As we have previously presented in Section 1, the architecture of a DW system is usually depicted as a set of components arranged in five layers (see Fig. 1). The design of every layer has its own characteristics and pitfalls. On the other hand, MDA presents three viewpoints, presented in Section 3 (i.e. computational independent, platform independent, and platform specific). Following these considerations, we present an MDA-oriented framework for the development of the whole DW (see Fig. 3). Within this framework, each DW layer is designed according to the three different kinds of MDA viewpoints. Obviously, for each layer and viewpoint, a different kind of model is required. Moreover, a set of transformations is defined in order to obtain and integrate every model as we can see in Fig. 3. Therefore, we consider that the whole development of a DW can be structured into an integrated framework with five layers and three viewpoints for each layer.

![](/api/attachments/BGX9R599/fulltext/images/4ee38a714d0e102d3fc38ded2b22ed736c20bf62c9788e1a845284a5b3a95be7.jpg)  
Fig. 3. Our MDA framework for the development of data warehouses.

The main advantage of our framework is that the complex task of designing the whole DW is tackled in a systematic, well-structured, and standard way by using an MDA approach. Other benefits of applying MDA to DW development are as follows:

• Productivity: the whole DW system can be automatically generated from the defined PIMs, since the transformations between models are formally established by using the QVT language. Therefore, the productivity is improved and development time and cost decrease.

• Business perspective: DW developers pay more attention in developing conceptual models of each layer of the DW, instead of focusing on technical details on a specific platform. Therefore, the developed DW fits much better with the needs of the end users and the quality of the developed DW is improved.

• Portability: the same PIM can be automatically transformed into multiple PSMs depending on different DW technologies.

• Integration and interoperability: DWs are heterogeneous systems, thus its development claims for the need of managing metadata by assuring integration and interoperability between the different layers. MDA provides an integrated modeling framework for managing this metadata.

• Reusability: best practices in DW design can be included in transformations in order to assure a high quality final product by using them in each DW project.

• Adaptability: if new DW technologies arise for certain components of the DW, then we are not obliged to change the whole DW. Instead, the PIM is preserved because it is independent of the underlying platform or technology, and DW developers only have to be concerned about the transformation between this PIM and the new PSM that is related to the arising technology.

• Support for system evolution: every new requirement in a DW system is addressed by changing the CIM and the PIM. Then, transformations can be updated in order to obtain a new PSM that reflects the changes [3,12,23].

In the following subsections, our MDA framework for the development of DWs is further explained. In Section 4.1 every DW layer is described. Section 4.2 relates MDA viewpoints to the DW system. Every necessary model for each layer and viewpoint within our framework is outlined in Section 4.3. Finally, the different kind of transformations are presented in Section 4.4.

## 4.1. Layers

According to the DW architecture described in Fig. 1, every DW component is situated within one of the followings five layers:

• Source layer, that defines the data sources of the DW, such as internal data sources (e.g. transactional systems), or external data sources (e.g. syndicated data).

• Integration layer, that defines the mapping between the data sources and the DW repository. This layer corresponds with the ETL processes and the data mapping between the data sources and the DW repository.

• Data Warehouse layer, that defines the structure of the DW repository. The basis for designing this layer is the MD modeling [8,10,11], which structures information into facts (interesting measures of a business process) and dimensions (the context for analyzing a fact).

• Customization layer, that defines special data structures that are used by the end-user applications to access the DW repository (i.e. data cubes). This is a kind of middleware layer that provides end-user applications with the necessary information from the DW.

• Application layer, that defines the end-user applications. These applications allow users to analyze data from the DW repository (supplied by the customization layer). This analysis is carried out by OLAP, data mining, reporting tools, and so on.

Our DW development framework takes into account these layers in order to deal with the design of the whole DW system.

## 4.2. Viewpoints

Each of the above-presented layers can be specified at three different levels according to the MDA viewpoint models [24]:

• CIM, that defines the requirements for the DW. It is a viewpoint of the DW within its business environment, so it plays an important role in bridging the gap between those that are experts about the domain and its requirements on the one hand (i.e. decision makers), and those that are experts of the design and construction of the DW which satisfies the requirements (i.e. DW developers), on the other.

• PIM, that defines the DW from a conceptual viewpoint. The major aim at this level is to represent the main DW properties without taking into account any specific technology detail. For example, a PIM for the DW repository should focus on representing the MD properties at the conceptual level, without considering any database technology.

• PSM, that addresses aspects of the DW design from a certain platform view. For example, a DW repository can be implemented by using different kinds of database technologies: relational approaches store MD data by using relational database technology (i.e. tables, columns, foreign keys and so on), and approaches based on a multidimensional database technology store data on proprietary structures such as MD arrays.

Apart from these viewpoints, code is generated from PSM in order to implement data structures according to a specific platform. For example, if the chosen platform for implementing the DW repository is a relational one, then we must obtain the corresponding SQL code to create tables, primary keys, foreign keys, and so on. If the chosen platform uses multidimensional technology, then we have to obtain the code to define the corresponding MD arrays.

## 4.3. Models

Each of the previously-described layers is concerned about different components of the whole DW development which must be represented at different levels of abstraction according to the above-described viewpoints. Therefore, each layer and viewpoint require different modeling formalisms. In our approach we use UML [27] and CWM [25] as modeling languages for constructing every PIM or PSM.

On one hand, UML can be extended to adapt it to specific domains by means of mechanisms such as metamodel extensibility or profiles. In previous works several UML profiles have been developed to adapt UML to certain aspects of DW design: MD modeling of the DW repository [16,17,19], modeling of the ETL processes [32], modeling the data mappings between data sources and targets [18], or the physical modeling of the DW [14].

On the other hand, CWM provides several metamodels to represent every DW component. For example, each PSM for the DW repository can be modeled by using the CWM Resource layer, since it is a standard to represent the structure of data according to several different database technologies, such as relational or multidimensional.

Requirements from DW users are modeled in a CIM. This issue is out of the scope of this paper, but we refer reader to [21] for a detailed explanation.

## 4.4. Transformations

Transformations are formally established in our framework by using QVT [28] in order to define readable, understandable, adaptable, maintainable, and automatic transformations between MOF-compliant models.

In Fig. 3 we can see every layer and viewpoint of our framework and how transformations are applied between the different models. The central part of our framework is the development of every PIM:

• Data sources PIM represents a conceptual model of the data sources. However, it is possible that only a logical schema or, even worst, only a collection of data structures are available. Then, it is possible to apply MDA transformations to start from the code or the PSM of data sources and obtain the corresponding PIM (transformations labeled as AT in Fig. 3).

• MD PIM represents a conceptual model of the DW repository. The major aim at this level is to define the main MD properties without taking into account any specific database technology. This MD PIM is constructed from the CIM (user requirements) and from the Data sources PIM by using a merging transformation (labeled as MT in Fig. 3).

• ETL PIM represents a conceptual model of the ETL processes. This PIM can be built from the Data sources PIM and from the MD PIM by using a merging transformation (MT in Fig. 3).

• Customization PIM represents a conceptual model of the data from the DW repository used by the end-user applications. This PIM can be constructed from the CIM and the MD PIM by means of a merging transformation.

• Application PIM represents a model of the end-user applications for the analysis of data by abstracting away the necessary details for a particular platform. This PIM is obtained from the CIM and the Customization PIM by means of a merging transformation.

Once we have developed every PIM, we can obtain every corresponding PSM and code from them by using vertical transformations (denoted as VT in Fig. 3). Note that the whole DW system can be then designed from the user requirements and the data sources, by developing every necessary transformation.

## 5. MDA for multidimensional modeling

Since the main issue in DW design is the MD modeling of the DW repository [6,8,11], in this paper we focus on defining how our MDA framework is applied to it. On the other hand, the most complex issue in MDA is the definition of transformations between a PIM and a PSM [12]. Therefore, due to space constraints, the following subsections explain our PIM and our PSM for the MD modeling, and a set of QVT transformations between them.

In Fig. 4, we show a symbolic diagram that will help to understand our MDA approach for the MD modeling of the DW repository. On top of this figure we have represented the PIM to specify every MD property without taking into account any technology. We consider this PIM as a conceptual model, since it is independent of any database technology. Therefore, this PIM is modeled by using our UML profile for the MD modeling of DWs [19].

A PSM is derived from a PIM taking into account the platform in which the DW will be deployed. We consider a PSM as a logical model of the DW, since it is related to a specific database technology. In this paper, the PSM is related to a relational approach in order to build a star schema, since it is the most common representation of the DW repository [11]. This model is represented in the middle of Fig. 4. CWM [25] is used to specify this PSM, since CWM provides a relational metamodel to represent data structures of relational databases (tables, columns, primary keys, foreign keys, and so on). On the other hand, transformations between PIM and PSM are formally established by using QVT.

From our PSM we can derive the necessary SQL code to create data structures for the DW in a relational platform. However, the PSM is close to relational technology, then it is quite straightforward to derive the corresponding SQL code. Thus, we do not develop this issue in this paper, and we focus on the transformation between PIM and PSM.

![](/api/attachments/BGX9R599/fulltext/images/6a74a72ed571e9bf5e93003c58842f220993970124effc6371bd2ee1fda362ba.jpg)  
Fig. 4. MDA approach for multidimensional modeling of data warehouses.

![](/api/attachments/BGX9R599/fulltext/images/bfa3c80f7e9866ea7166dcfa4c3c2bd5ac38e1f3acb83781c646df88c344f5c5.jpg)  
Fig. 5. Extension of the UML with stereotypes for the MD modeling of DWs.

## 5.1. PIM definition

A PIM is a view of a system from the platform independent viewpoint [24]. This means that this model describes the system hiding the necessary details related to a particular platform. This point of view corresponds with a conceptual level of our approach. The major aim at this level is to represent the main MD properties without taking into account any specific database technology detail, therefore the specification of the DW is independent from the platform in which it will be implemented. This PIM is developed following our UML profile for MD modeling presented in [19]. This profile contains the necessary stereotypes in order to elegantly represent main MD properties at the conceptual level (see Figs. 5 and 6).

Specifically, the structural properties of MD modeling are represented by means of a UML class diagram in which the information is clearly organized into facts and dimensions. These facts and dimensions are represented by Fact ( ) and Dimension ( ) classes respectively. Fact classes are defined as composite classes in shared aggregation relationships of n Dimension classes. The minimum cardinality in the role of the Dimension classes is 1 to indicate that every fact must always be related to all the dimensions.

![](/api/attachments/BGX9R599/fulltext/images/910df64b3d7e4040c5e9946de8eb222f70f2a8e2ffffa4f8f9e29e9f393a3bc4.jpg)  
Fig. 6. Part of the UML metamodel extended by our profile.

![](/api/attachments/BGX9R599/fulltext/images/055d94582ee10a19f4a5ec535f5019372394452fd576f66b90a2bc42b0439f57.jpg)  
Fig. 7. Part of the relational CWM metamodel.

A fact is composed of measures or fact attributes. These are represented as attributes with the FactAttribute stereotype (FA). By default, all measures in the Fact class are considered to be additive [11]. For non-additive measures, additive rules are defined as constraints and are included in the Fact class. Furthermore, derived measures (indicated by /) and their derivation rules can also be explicitly represented as tagged values of a FactAttribute.

Our approach also allows the definition of degenerate dimensions [11], thereby representing other fact features in addition to the measures for analysis. These degenerate dimensions are represented as stereotyped attributes of the Fact class (DegenerateDimension stereotype, DD).

The many-to-many relationships between a fact and a specific dimension are specified by means of the cardinality 1…n in the role of the corresponding Dimension class. In this case, we usually need to describe specific attributes to provide further features for every instance combination in this particular relationship. In doing so, the provided attributes are usually called degenerate facts [11]. These degenerate facts are represented as an association class attached to a many-to-many aggregation relationship between a Fact class and a Dimension class. This DegenerateFact class ( ) can contain FactAttributes and DegenerateDimensions.

With respect to dimensions, each level of a classification hierarchy is specified by a Base class. Every Base class ( ) can contain several dimension attributes (DimensionAttribute stereotype, DA), one OID attribute (OID stereotype, OID), and must also contain a descriptor attribute (Descriptor stereotype, D). An association (represented by a stereotype called Rolls-UpTo) between Base classes specifies the relationship between two levels of a classification hierarchy. The only prerequisite is that these classes must define a Directed Acyclic Graph (DAG) rooted in the Dimension class (DAG constraint is defined in the stereotype Dimension). The DAG structure can represent both multiple and alternative path hierarchies.

A Dimension class contains a unique first hierarchy (or dimension) level called terminal dimension level. A roll-up path is a subsequence of dimension levels, which starts in this terminal level (lower level of detail) and ends in an implicit level (not graphically represented) that represents all the dimension levels.

![](/api/attachments/BGX9R599/fulltext/images/d066b392b766d426db97ff44067ad4dab2640603cfc45666802f8eb113d5c1e9.jpg)  
Fig. 8. QVT relations (1/6).

![](/api/attachments/BGX9R599/fulltext/images/210403695b20555220fbef701a2d0c66fdbc9f391dd1abd6e30e64264c4b97b5.jpg)  
Fig. 9. QVT relations (2/6).

We use roles to represent the way the two Base classes see each other in a Rolls-UpTo association: role R represents the direction in which the hierarchy rollsup, whereas role D represents the direction in which the hierarchy drills-down. Moreover, we use roles to detect and avoid cycles in a classification hierarchy, and therefore, help us to achieve the DAG condition.

Due to flexibility of UML, we can also consider nonstrict hierarchies (an object at a hierarchy's lower level belongs to more than one higher-level object) and complete hierarchies (all members belong to one higherclass object and that object consists of those members only). These characteristics are specified, respectively, by means of the cardinality of the roles of the associations and defining the stereotype Completeness in the association between Base classes. Lastly, the categorization of dimensions is considered by means of the generalization/specialization relationships of UML.

Our profile is formally defined and uses the Object Constraint Language (OCL) [26] for expressing wellformed rules of the new defined elements (see Fig. 5), thereby avoiding an arbitrary use of the profile. We refer reader to [19] for a further explanation of this profile and its corresponding OCL constraints.

## 5.2. PSM definition

A PSM is a view of a system from the platform specific viewpoint [24]. It represents the model of the same system specified by the PIM but it also specifies how that system makes use of the chosen platform. Therefore, in our framework a PSM corresponds with a logical representation of the MD model tailored to a specific kind of database technology. According to [11] the most common logical representation of MD models is the relational star schema. This schema consists of a central fact table with a composite key which is joined to several dimension tables, each with a single primary key. In this paper, we assume that our PSM is a star schema, but other transformations can be specified to be able to obtain different kinds of PSMs.

![](/api/attachments/BGX9R599/fulltext/images/8739ac525ad9c18313d65d1e55ac74f32b4da440ad1d30b8afaeab7fc42777d8.jpg)  
Fig. 10. QVT relations (3/6).

![](/api/attachments/BGX9R599/fulltext/images/b1738a90c7fe221ca545616bddeab58737c291e257f1a5bbd1cf8030ba8f27d1.jpg)  
Fig. 11. QVT relations (4/6).

Our PSM is modeled by using the CWM relational metamodel [25], since it is a standard to represent the structure of data resources in a relational database. This relational metamodel allows us to represent tables, columns, primary keys, foreign keys and so on. On the other hand, this metamodel is SQL-compliant, thus we will be able to obtain SQL code in an easy and straightforward way from the PSM. Furthermore, since every CWM metamodel is MOF-compliant [25], it can be used as source or target for QVT transformations [28]. For the sake of clarity, we use the part of the relational metamodel shown in Fig. 7.

## 5.3. From PIM to PSM

Developing formal transformations that allow one to derive every PSM from a PIM in an automatic way is the most complex task of MDA [12]. In this paper, transformations are given by following the declarative approach of QVT [28], since it provides a graphical notation that allows to formally specify model transformations which are easily readable, understandable, adaptable and maintainable.

According to the QVT relations language, we have developed every relation to obtain a transformation between our PIM and a PSM for a relational platform (according to a star schema representation).<sup>2</sup> The developed relations (as stated by the QVT graphical notation) are shown in Figs. 8–13. Furthermore, an example of the textual notation of QVT is given in Fig. 15. We also have defined a function in order to convert a type of our PIM into a type of our PSM: MDType2RELType (see Fig. 14). Due to space constraints, we do not provide a detailed description of each transformation. Instead, only the Dimension2- Table relation is further explained. However, the rest of relations are easily understandable due to the readability and understandability of the QVT relations language.

The graphical notation for the Dimension2Table relation can be seen in Fig. 9, whereas the textual notation is shown in Fig. 15. On the left hand side of this relation (in Fig. 9) we can see the source model, and on the right hand side the target model. The source model is the part of the PIM metamodel (see Figs. 5 and 6) that has to match with the part of the PSM metamodel (see Fig. 7) which represents the target model. In this case, a collection of elements from our UML profile that represents a Dimension class and the terminal level (Base class associated with the Dimension class) matches with a set of elements from the CWM relational metamodel that represents a table (Table class) with a primary key (PrimaryKey class). This relation determines the transformation in the following way: it is checked (C arrow) that the pattern on the left side (source model) exists in the PIM, then the transformation enforces (E arrow) that the following elements (and their associations) are created according to the PSM metamodel: a new Table class with the same name that the Dimension class, a Column (with its corresponding type), and a PrimaryKey. Once this relation holds, the relations DimensionAttribute2Column, OID2Column, Descriptor2Column, Base2Table, and SpecializedBase2Table must be done (according to the where clause).

## 6. Case study

In this section, a case study, inspired from the case study presented in [6], is introduced in order to apply

![](/api/attachments/BGX9R599/fulltext/images/71f3d4a2819429185efb34e95b5967d85c8a4c9f2b114b0b002dbeb1fc08087a.jpg)  
Fig. 12. QVT relations (5/6).

our approach. In this case study, a company that comprises different dealerships sells automobiles across several states. Therefore, we focus on the automobile sales fact (Autosales). This fact contains several measures (i.e. fact attributes) to be analyzed (Quantity of sold automobiles, Price of the automobile and Total amount of the sale). Furthermore, we specify a number of contract (ContractN) as a degenerate dimension. On the other hand, we also consider the following dimensions as contexts to analyze measures: Time, Auto, Dealership, Salesperson, and Customer. However, we will only focus on two of these dimensions in order to make the case study more understandable: the Customer dimension (which has the hierarchy levels Customer personal data, City, Region, and State), and the Salesperson dimension (which has hierarchy levels that form a categorization: Salesperson personal data, Clerk, and Traveller). Furthermore, more than one salesperson could be implied in the same sale. Within a particular sale each implied salesperson receives a certain commission. Therefore, a degenerate fact (Commission) is needed in order to reflect this issue. This degenerate fact has a fact attribute (Amount) that reflects the amount of commission earned in a certain sale. The corresponding PIM is specified in Fig. 16.

From the defined PIM, we can apply the QVT transformation rules defined in Section 5.3 to obtain the corresponding PSM. The PSM is shown in the following figures:

• Fig. 17 represents the part of the obtained PSM after applying several relations to the Customer dimension and its hierarchy levels represented in the PIM (see Fig. 16). First, Dimension2Table (see Fig. 9) is applied: both the dimension Customer and its termina dimension level (Customer personal data) are transformed into a set of elements from the CWM relational metamodel according to a star schema representation: a table called Customer is created together with its corresponding primary key (ID Customer). To create a column in the new table for each attribute in the terminal dimension level, the following relations are applied (according to the where clause): Dimension-Attribute2Column, and Descriptor2- Column (see Figs. 11 and 12, respectively). Thus, Customer\_Name and Customer\_BornDate columns are created in the Customer table. Base2Table (see Fig. 10) is the next relation to be applied, since two hierarchy levels (Customer personal data and Region ) are associated by means of a Rolls-upTo association. This relation makes it possible to navigate through each level (Base class) in the classification hierarchy in order to transform every attribute within any Base class into a column of the same table according to a star schema. In this way, a new column is created in the Customer table: Region\_Name. The Base2Table relation must be applied as many times as a Rolls-upTo association between base classes has been matched.

![](/api/attachments/BGX9R599/fulltext/images/26cc8ae2684f8b885b8996e2b32a0d1de4a85fb53d6201f325184737356b0cb5.jpg)  
Fig. 13. QVT relations (6/6).

![](/api/attachments/BGX9R599/fulltext/images/0199052aa7fb7660c0012b631bd0240a159f816431a0c68607bc6fb7cb55953c.jpg)  
Fig. 14. Function to obtain a PSM type from a PIM type.

• Fig. 18 represents the part of the PSM corresponding to the Salesperson dimension and its related elements from the PIM. Once Dimension2Table (see Fig. 9) is applied as in the previous case, SpecializedBase2Table relation is applied to deal with the categorization of dimensions. In this case, every attribute in the subclasses (Location attribute in the Clerk subclass and Route attribute in the Traveller subclass) is transformed into columns (Clerk\_Location and Traveller\_Route) in the same table (Salesperson table).

• Fig. 19 represents the part of the PSM after applying Fact2Table, FactAttribute2Column, DegenerateDimension2Column, and Fact2PK to the current PIM. An Autosales table is created as a fact table, and the fact attributes in the fact class are transformed into columns. The degenerate dimension ContractN is transformed into a column that represents the primary key of the fact table. Furthermore, a column (Autosales\_REF\_ Customer) that references to the Customer table (i.e. represents a foreign key) is also considered as part of the primary key, since there is a many-to-one relationship between the Autosales fact class, and the Customer dimension class.

• Fig. 20 represents the final part of the PSM. The following relations have been applied: Fact2- BridgeTable, and DegenerateFact2Table. According to these relations, a bridge table is created in order to deal with the many-to-many relationship between the Autosales fact class and the Salesperson dimension class, and the Commision degenerate fact.

## 7. Conclusion and future work

In this paper, we have introduced our MDA-oriented framework for the development of DWs. This framework addresses the design of the whole DW system by aligning every component of the DW with the different MDA viewpoints (CIM, PIM, and PSM). The whole system is constructed by means of transformations applied to PIM in order to automatically obtain every corresponding PSM. From each PSM it is possible to obtain code in a straightforward way in order to implement the DW in a concrete platform. Thanks to the use of MDA and QVT, the development of DWs is simplified in just two tasks: (i) the development of a PIM for each DW component; and (ii) the development of the corresponding QVT transformations to automatically generate the final DW implementation from every PIM.

```txt
relation Dimension2Table {
    n_d, n_c, n_pk: String;
    checkonly domain MD d:Dimension {
    name=n_d,
    ownedAttribute=p1:Property {
    association=a:Association {
    memberEnd=p2:Property {
    class=b:Base{name=n_b}
    }
    }
    };
    enforce domain REL t:Table {
    name=n_d,
    feature=c:Column {
    name=n_c,
    type=stp:SQLDataType{name='INTEGER'}, uniqueKey=pk:PrimaryKey{name=n_pk}
    }
    ownedElement=pk
    };
    where {
    n_c = 'ID_' + n_d;
    n_pk = 'PK_' + n_d;
    DimensionAttribute2Column(b,t,n_d);
    OID2Column(b,t,n_d);
    Descriptor2Column(b,t,n_d);
    Base2Table(b,t);
    SpecializedBase2Table(b,t);
    }
}
```  
Fig. 15. Textual notation for Dimension2Table relation.

![](/api/attachments/BGX9R599/fulltext/images/fdb706f37df61a4b55cdfac39354f100e4ca824c866d348b7fb4b9210a479e6a.jpg)  
Fig. 16. PIM of our case study.

![](/api/attachments/BGX9R599/fulltext/images/5a1ed7fe94a81e8e731a9626c8f7417e2c4b09605298fea5d2a0e41272f68f99.jpg)  
Fig. 17. PSM for Customer

On the other hand, we have focused on describing one part of our framework: an MDA approach for the development of the DW repository based on the MD modeling, since it is the cornerstone of any DW system. We have defined the corresponding MDA artifacts: our MD modeling profile has been used as a PIM and the CWM relational package as a PSM, while the transformations are formally and clearly established by using the QVT language. Finally, a case study has been presented in order to show the benefits of our proposal.

![](/api/attachments/BGX9R599/fulltext/images/149b1998fa2d921ff2a47f2d8389212154364f3a4baa72b4d90dbd79e343c903.jpg)  
Fig. 18. PSM for Salesperson.

![](/api/attachments/BGX9R599/fulltext/images/765bae390abd8e150b0ec241d519933ba1d396f81bb249a23671a7636c5801fb.jpg)  
Fig. 19. PSM for Autosales fact.

Our short-term intentions include improving our MDA approach for the development of DWs by adding other PSMs according to several platforms. Furthermore, we plan to add quality metrics in the defined transformations in order to generate the best PSM and code out of different possibilities. For example, we will be able to automatically adapt transformations in order to generate a pure star schema or a snowflake schema defining the most adequate level of normalization according to different situations. Therefore, the most suitable DW schema for each concrete context will be obtained within our MDA approach.

![](/api/attachments/BGX9R599/fulltext/images/eb27bfc21484bbad7b0e1ce2e30925c134be1e6f9efa4a34e8b50b387d1b932d.jpg)  
Fig. 20. PSM for bridge table between Salesperson and Autosales.

## Acknowledgements

This work has been partially supported by the META-SIGN (TIN2004-00779) project from the Spanish Ministry of Education and Science, by the DADASMECA project (GV05/220) from the Valencia Ministry of Enterprise, University and Science (Spain), and by the DADS (PBC-05-012-2) project from the Castilla-La Mancha Ministry of Education and Science (Spain). Jose-Norberto Mazón is funded by the Spanish Ministry of Education and Science under a FPU grant (AP2005-1360).

## References

[1] A. Abelló, J. Samos, F. Saltor, YAM2: a multidimensional conceptual model extending UML, Information Systems 31 (6) (September 2006) 541–567.

[2] K. Czarnecki, S. Helsen, Classification of model transformation approaches, Proceedings of the 2nd OOPSLAWorkshop on Generative Technique in the Context of the Model Driven Architecture, Anaheim, 2003.

[3] D.S. Frankel, Model Driven Architecture. Applying MDA to Enterprise Computing, Wiley, Indianapolis, Indiana, 2003.

[4] A. Gerber, M. Lawley, K. Raymond, J. Steel, A. Wood, Transformation: the missing link of MDA, in: A. Corradini, H. Ehrig, H.-J. Kreowski, G. Rozenberg (Eds.), ICGT, Vol. 2505 of Lecture Notes in Computer Science, Springer, 2002, pp. 90–105.

[5] P. Giorgini, S. Rizzi, M. Garzetti, Goal-oriented requirement analysis for data warehouse design, DOLAP, 2005, pp. 47–56.

[6] W. Giovinazzo, Object-Oriented Data Warehouse Design. Building a Star Schema, Prentice-Hall, 2000.

[7] M. Golfarelli, D. Maio, S. Rizzi, The dimensional fact model: a conceptual model for data warehouses, International Journal of Cooperative Information Systems 7 (2-3) (1998) 215–247.

[8] W. Inmon, Building the Data Warehouse, 3rd edition, Wiley & Sons, New York, 2002.

[9] I. Jacobson, G. Booch, J. Rumbaugh, The Unified Software Development Process, Object Technology Series, Addison-Wesley, 1999.

[10] M. Jarke, M. Lenzerini, Y. Vassiliou, P. Vassiliadis, Fundamentals of Data Warehouses, Springer, 2000.

[11] R. Kimball, M. Ross, The Data Warehouse Toolkit, 2nd edition, John Wiley & Sons, 2002.

[12] A. Kleppe, J. Warmer, W. Bast, MDA Explained. The Practice and Promise of the Model Driven Architecture, Addison Wesley, 2003.

[13] J. Lechtenbörger, G. Vossen, Multidimensional normal forms for data warehouse design, Inf. Syst. 28 (5) (2003) 415–434.

[14] S. Luján-Mora, J. Trujillo, Physical modeling of data warehouses using UML, in: I.-Y. Song, K.C. Davis (Eds.), DOLAP, ACM, 2004, pp. 48–57.

[15] S. Luján-Mora, J. Trujillo, A data warehouse engineering process, in: T.M. Yakhno (Ed.), ADVIS, Vol. 3261 of Lecture Notes in Computer Science, Springer, 2004, pp. 14–23.

[16] S. Luján-Mora, J. Trujillo, I.-Y. Song, Multidimensional modeling with UML package diagrams, in: S. Spaccapietra, S.T. March, Y. Kambayashi (Eds.), ER, Vol. 2503 of Lecture Notes in Computer Science, Springer, 2002, pp. 199–213.

[17] S. Luján-Mora, J. Trujillo, I.-Y. Song, Extending the UML for multidimensional modeling, in: J.-M. Jézéquel, H. Hußmann, S. Cook (Eds.), UML, Vol. 2460 of Lecture Notes in Computer Science, Springer, 2002, pp. 290–304.

[18] S. Luján-Mora, P. Vassiliadis, J. Trujillo, Data mapping diagrams for data warehouse design with UML, in: P. Atzeni, W.W. Chu, H. Lu, S. Zhou, T.W. Ling (Eds.), ER, Vol. 3288 of Lecture Notes in Computer Science, Springer, 2004, pp. 191–204.

[19] S. Luján-Mora, J. Trujillo, I.-Y. Song, A UML profile for multidimensional modeling in data warehouses, Data and Knowledge Engineering 59 (3) (December 2006) 725–769.

[20] J.-N. Mazón, J. Trujillo, M. Serrano, M. Piattini, Applying MDA to the development of data warehouses, DOLAP, 2005, pp. 57–66.

[21] J.-N. Mazón, J. Trujillo, M. Serrano, M. Piattini, Designing data warehouses: from business requirement analysis to multidimensional modeling, in: K. Cox, E. Dubois, Y. Pigneur, S.J. Bleistein, J. Verner, A.M. Davis, R. Wieringa (Eds.), REBNITA, University of New South Wales Press, 2005, pp. 44–53.

[22] E. Medina, J. Trujillo, A standard for representing multidimensional properties: The Common Warehouse Metamodel (CWM), in: Y. Manolopoulos, P. Návrat (Eds.), ADBIS, Vol. 2435 of Lecture Notes in Computer Science, Springer, 2002, pp. 232–247.

[23] S. Mellor, K. Scott, A. Uhl, D. Weise, MDA Distilled: Principles of Model-driven Architecture, Addison Wesley, 2004.

[24] Object Management Group (OMG), MDA Guide 1.0.1. http:// www.omg.org/cgi-bin/doc?omg/03-06-01.

[25] Object Management Group (OMG), Common Warehouse Metamodel (CWM) Specification 1.1. http://www.omg.org/cgibin/doc?formal/03-03-02.

[26] Object Management Group (OMG), Object Constraint Language (OCL) Specification 2.0. http://www.omg.org/cgi-bin/doc?ptc 03-10-14.

[27] Object Management Group (OMG), Unified Modeling Language Specification 2.0. http://www.omg.org/cgi-bin/doc?formal/05-07-04.

[28] Object Management Group (OMG), MOF 2.0 Query/View/ Transformation. http://www.omg.org/cgi-bin/doc?ptc/2005-11-01.

[29] J. Poole, Model Driven Data Warehousing (MDDW). www. cwmforum.org/POOLEIntegrate2003.pdf.

[30] S. Sendall, W. Kozaczynski, Model transformation: the heart and soul of model-driven software development, IEEE Softw. 20 (5) (2003) 42–45.

[31] A. Simitsis, Mapping conceptual to logical models for ETL processes, DOLAP, 2005, pp. 67–76.

[32] J. Trujillo, S. Luján-Mora, A UML based approach for modeling ETL processes in data warehouses, in: I.-Y. Song, S.W. Liddle, T.W. Ling, P. Scheuermann (Eds.), ER, Vol. 2813 of Lecture Notes in Computer Science, Springer, 2003, pp. 307–320.

[33] N. Tryfona, F. Busborg, J.G.B. Christiansen, starER: a conceptua model for data warehouse design, DOLAP, ACM, 1999, pp. 3–8.

[34] P. Vassiliadis, A. Simitsis, S. Skiadopoulos, Conceptual modeling for ETL processes, in: D. Theodoratos (Ed.), DOLAP, ACM, 2002, pp. 14–21.

[35] P. Vassiliadis, A. Simitsis, P. Georgantas, M. Terrovitis, S. Skiadopoulos, A generic and customizable framework for the design of ETL scenarios, Information Systems 30 (7) (2005) 492–525.

![](/api/attachments/BGX9R599/fulltext/images/ddb3a7beafb928a798c35df2806cf41824155d060bb1f5e84a171c2c3fb436b8.jpg)

Jose-Norberto Mazón is a PhD student from the University of Alicante (Spain). He currently enjoys a research grant from the Spanish Ministry of Education and Science. He received a Master in Computer Science in 2004 from the University of Alicante. He has published several papers about data warehouses in national and international work shops and conferences, such as DAWAK, ER, DOLAP, BNCOD, JISBD and so on. His

research interests are: database modeling, conceptual design of data warehouses, multidimensional databases, and model driven develop ment. Contact him at jnmazon@dlsi.ua.es.

![](/api/attachments/BGX9R599/fulltext/images/2cd9d83314e115801903ded031e16997ab174f142c22e3202d2ad29271d977a3.jpg)

Juan Trujillo is an associated professor at the Computer Science School at the University of Alicante, Spain. Trujillo received a Ph.D. in Computer Science from the University of Alicante (Spain) in 2001. His research interests include database modeling, data warehouses, conceptual design of data warehouses, multidimensional databases, data warehouse security and quality, mining data warehouses, OLAP, as well as object-oriented analysis and design with

UML. He has published many papers in high quality international conferences such as ER, UML, ADBIS, CAiSE, WAIM or DAWAK. He has also published papers in highly cited international journals such as IEEE Computer, Decision Support Systems (DSS), Data and Knowledge Engineering (DKE) or Information Systems (IS). Dr. Trujillo has served as a Program Committee member of several workshops and conferences such as ER, DOLAP, DAWAK, DSS, JISBD and SCI and has also spent some time as a reviewer of several journals such as JDM, KAIS, ISOFT and JODS. He has been Program Chair of DOLAP'05 and BP-UML'05, and Program Co-chair of DAWAK'05, DAWAK'06 and BP-UML'06. Contact him at jtrujillo@dlsi.ua.es.
