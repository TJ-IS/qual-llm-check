---
otero_id: 11972
otero_key: "WUA3WGQC"
title: "A UML-based data warehouse design method"
authors: "Nicolas Prat; Jacky Akoka; Isabelle Comyn-Wattiau"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.12.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A UML-based data warehouse design method

Nicolas Prat <sup>a</sup>, Jacky Akoka <sup>b</sup>, Isabelle Comyn-Wattiau <sup>c,⁎</sup>

<sup>a</sup> ESSEC, Avenue Bernard Hirsch, BP 50105, 95021 Cergy Cedex, France

<sup>b</sup> CEDRIC-CNAM and INT 292, rue Saint-Martin 75141 Paris Cedex 03, France

<sup>c</sup> CEDRIC-CNAM and ESSEC 292, rue Saint-Martin 75141 Paris Cedex 03, France

Received 7 August 2004; received in revised form 20 July 2005; accepted 1 December 2005 Available online 23 January 2006

## Abstract

Data warehouses are a major component of data-driven decision support systems (DSS). They rely on multidimensional models. The latter provide decision makers with a business-oriented view to data, thereby easing data navigation and analysis via On-Line Analytical Processing (OLAP) tools. They also determine how the data are stored in the data warehouse for subsequent use, not only by OLAP tools, but also by other decision support tools. Data warehouse design is a complex task, which requires a systematic method. Few such methods have been proposed to date. This paper presents a UML-based data warehouse design method that spans the three design phases (conceptual, logical and physical). Our method comprises a set of metamodels used at each phase, as well as a set of transformations that can be semi-automated. Following our object orientation, we represent all the metamodels using UML, and illustrate the formal specification of the transformations based on OMG's Object Constraint Language (OCL). Throughout the paper, we illustrate the application of our method to a case study. © 2005 Elsevier B.V. All rights reserved.

Keywords: Data warehouse; On-Line Analytical Processing (OLAP); Decision support; Conceptual design; Logical design; Physical design

## 1. Introduction

Data warehouses are an essential component of datadriven decision support systems (DSS) [34]. They have become the focal point for decision support in organizations today [40]. Moreover, empirical evidence suggests that DSS users can improve decision performance by implementing a data warehouse [26]. In order to gain business insight from data stored in data warehouses, decision makers typically use OLAP, query and reporting, and/or data mining tools. For OLAP tools alone, [36] estimates the worldwide market at 6 billion dollars in 2007, compared with 1 billion dollars in 1996. OLAP systems are based on a multidimensional model. This model provides managers with a business-oriented view of data. It facilitates data navigation, analysis, and ultimately decision making. Depending on the underlying database, OLAP tools are traditionally subdivided into two main categories [10]: Multidimensional OLAP (MOLAP) tools store data in a proprietary multidimensional database system. The multidimensional component of Oracle 9i Release 2 (formerly known as Express and subsequently referred to as Oracle MOLAP), and Hyperion Essbase, are representative of this category. Relational OLAP (ROLAP) tools simulate a multidimensional model with a relational database, usually based on Kimball's star or snowflake schemas [16].

From the above considerations, it ensues that the multidimensional model (1) provides decision makers with a view to the data warehouse, via OLAP tools, and (2) determines how the data are stored in the data warehouse for subsequent use, not only by OLAP tools, but also by other decision support tools, e.g. data mining [33]. Consequently, multidimensional modeling is central to data warehouse design.

The data warehouse design process is crucial and should be supported by an appropriate method. A design method is essential not only to ensure the data warehouse quality, but also to facilitate its frequent evolutions imposed by the environment or the decision makers' changing requirements.

A complete data warehouse design method should span the three abstraction levels recommended by ANSI/X3/SPARC, namely conceptual, logical and physical. These levels are widely accepted as a sound framework to guide the modeling process of operational databases. We strongly argue that this framework remains relevant in the context of data warehouses, even if the three levels need to be adapted to this context. The need to adapt these three levels to the domain of data warehousing is frequently acknowledged [13,14], although there is no agreement concerning the content of each level and hence of each data warehouse design phase.

Despite the existence of several methods presented in the literature, the data warehouse community still lacks a widely accepted method, covering all aspects of data warehouse design and specifying the various design steps. This lack of a general data warehouse design method follows from the absence of a standard, tool-independent multidimensional formalism i.e. multidimensional metamodel.<sup>1</sup> The multidimensional metamodel is central to data warehouse design; however, no consensus has emerged concerning this metamodel, as opposed to the relational standard in the On-Line Transactional Processing (OLTP) world.

Considering the need for a systematic data warehouse design method and the limitations of current methods, this paper presents a UML-based data warehouse design method that spans conceptual, logical and physical design. Starting from user requirements, the conceptual phase leads to a UML model. To this end, UML is enriched with concepts relevant to multidimensional systems. The logical phase maps the enriched UML model into a multidimensional schema, independently of any implementation tool. The physical phase maps the multidimensional schema into a physical database schema depending on the target implementation tool. Our method comprises a set of metamodels used at each phase (in particular a unified multidimensional metamodel used at the logical phase), as well as a set of transformations that can be semi-automated. Following our object orientation, we represent the metamodels using UML and specify the transformations formally using OMG's Object Constraint Language (OCL) [25]. The paper is organized as follows. Section 2 describes related research. Section 3 presents our unified multidimensional metamodel, which is at the center of our design method. Section 4 presents the design method and illustrates step by step how the method is applied to a case study. Section 5 concludes and describes further research.

## 2. Related research

There exists a fair number of papers describing multidimensional metamodels [5,39]. The Common Warehouse Metamodel (CWM) [25] is a recent endeavor to standardize data warehousing and business intelligence applications based on UML. The OLAP package describes the multidimensional metamodel, independently of any ROLAP or MOLAP implementation. The “multidimensional” package is a metamodel for MOLAP tools. MOLAP tool-specific metamodels (e.g. the metamodel of Oracle MOLAP) are defined as extensions of this metamodel.

Data warehouse design approaches can be analyzed from three vantage points. The first one is related to OLAP tools. Vendors of such tools claim that cube design (i.e. multidimensional modeling) is an intuitive and quasi-immediate process, which does not need a sophisticated design method. Oddly enough, the very same arguments were used by relational database vendors 20 years ago. There are plenty of failure stories in database design due to lack of methods. The second vantage point is related to multiple source integration approaches where the data warehouse schema results from an integration of source database schemas [15]. The hypothesis underlying these approaches is that the data warehouse must contain exactly the existing data sources. This hypothesis is rarely realistic. The third vantage point is related to the adaptation of classical database design methods. The main advantage is the clear separation between semantic considerations and physical constraints. Moreover, in this approach, data warehouse design explicitly takes into account user requirements. However, it must be followed by a data confrontation phase enabling the mapping between the data warehouse schema and the data sources. In this paper, we propose a step forward: we enrich this classical approach by defining a data warehouse design method starting from user requirements and leading to a physical schema by means of specific transformation rules. The following state-of-the-art review will concentrate on this third stream.

Published models or methods, very often, encompass only some phases of data warehouse design. These previous research works can be characterized according to the following criteria:

The underlying conceptual model, such as the Entity-Relationship (ER) model [8], an extended ER model [29,32], an object-oriented model like UML [3,21,23], a specific model [16]. Let us mention that some design methods don't have an explicit conceptual model [9].

– The associated paradigm, i.e. bottom-up when starting from operational data sources [22], top-down based on user requirements [37], or mixed when combining the two approaches [32].

The components of the system taken into account, such as the data warehouse [13], the data marts [6], the ETL (Extract-Transform-Load) process [21], etc. The target system being implemented, such as ROLAP environments [14], MOLAP environments [2], both environments [8]. Other approaches are independent of implementation issues [37].

– The degree of formalism used, ranging from a rough set of guidelines [12] to a rigorously formalized notation including meta-modeling [21].

– The abstraction levels covered by the method, namely the conceptual, logical and physical phases. As an illustration, some approaches are dedicated to the conceptual phase [37], others merge the conceptual and logical phases [32], and others concentrate on a unique logical–physical phase [16].

– The level of automation made possible: this level encompasses simple design rules [16] and can be spanned to a CASE tool [28].

To the best of our knowledge, no single method is widely accepted. Based on this categorization, we can characterize our method as follows:

– It is based on the UML notation, facilitating the process by referring to a well-known formalism. – It combines a top-down approach (data warehouse design starts from user requirements) with a bottomup approach (the resulting data warehouse is confronted with operational data sources).

– Its vocation is to enable the design of all components including the data warehouse, the data marts and the ETL processes. However, the current version concentrates on the data warehouse design.

– It is implementation-independent by providing rules for MOLAP as well as ROLAP tools.

The formalization is based on meta-models describing the three abstraction levels (conceptual, logical, and physical). Transformation rules are provided to map one level into the following one and are formalized using the OCL notation.

– A high level of automation is obtained by inserting the best practices in the rules by means of heuristics. A CASE tool is under prototyping.

Standardization relies on the combination of UML with its associated OCL formalism.

[21] seems to be the most comprehensive method for data warehouse design meeting the main requirements described above. We propose to go beyond by providing a higher level of automation and a higher degree of standardization. Moreover, our contribution also encompasses an important effort in unifying multidimensional models. The next section is dedicated to the description of our unified multidimensional metamodel.

## 3. A unified multidimensional metamodel

Among the many multidimensional metamodels proposed in the literature, no standard emerges. Furthermore, no consensus has been reached yet concerning the level of the multidimensional metamodel (physical, logical or conceptual). The star and snowflake models presented in [16] have often been considered being at the physical level. More recent publications have placed the multidimensional metamodel at the logical level [25,39] or even at the conceptual level [13,14].

We firmly contend that the multidimensional metamodel belongs to the logical level. This claim is justified by the following considerations:

– This metamodel does not belong to the physical level, since multidimensional models are often used as pivot models, enabling mapping to different physical tool implementations.

– Moreover, it should not be considered at the conceptual level since its concepts (e.g. the concept of dimension) do not have the semantic richness of traditional conceptual metamodels, e.g. ER or UML. Actually, proposals based on a combination of multidimensional metamodels with ER or UML concepts are often justified by the poor semantics of the basic multidimensional metamodel.

– If we situate the multidimensional metamodel at the conceptual level, then it seems coherent to consider at the logical level metamodels like MOLAP or ROLAP. However, once a “conceptual” multidimensional metamodel has been defined, it makes little sense to define a standard logical MOLAP metamodel, since no such standard exists in reality. Furthermore, in the case of ROLAP, the relational layer must be considered as the physical structure for data storage [5], therefore ROLAP cannot be considered belonging to the logical level either.

– There is indeed a strong parallel between the relational metamodel in the OLTP world and the multidimensional metamodel in the OLAP world—e.g. the definitions or attempts to define an associated query language and a normalization theory (even though the concept of normalization in the OLAP context differs from the traditional concept of normalization in the OLTP context). The analogy between these two metamodels is often made [2,11], confirming that the multidimensional metamodel should be situated at the same level as the relational metamodel in transactional database design, i.e. the logical level.

After an overview of the basic multidimensional concepts, we present our unified multidimensional metamodel and its associated graphical notation. The metamodel is a central component of our data warehouse design method, making the link between the conceptual and physical design phases. Among extant multidimensional metamodels, some key concepts appear recurrently, but we found no metamodel encompassing all these concepts and accurately expressing their relationships. Therefore, we defined a multidimensional metamodel, unifying the concepts of the main multidimensional metamodels. This metamodel is generic, i.e. can be mapped into any OLAP tool (this paper illustrates MOLAP tool implementation; ROLAP implementation is described in [30]).

## 3.1. Multidimensional concepts

Multidimensional metamodels store data in hypercubes, often simply referred to as cubes. Fig. 1 illustrates a cube, which represents the fact Sale.

The key multidimensional concepts are cubes–which represent facts of interest for analysis–and dimensions, i.e. the axes of the cubes. Facts are described by measures. A measure is an indicator, a value of interest for the decision maker. Measures are quantifying values; they are generally numeric. In a cube, the measures correspond to the cells. Every dimension may consist of one or several aggregation level(s), called dimension levels. Dimension levels are organized in hierarchies, i.e. aggregation paths between successive dimension levels (for example, Day→Week→Quarter→Year in Fig. 1). Hierarchies are crucial to multidimensional modeling since they are used in conjunction with aggregation functions to aggregate (“rollup”) or detail (“drilldown”) measures. Hierarchies are often completed with the special dimension level All, thereby enabling aggregation of measures at the highest possible level. Dimension levels may be described by attributes. Contrary to measures, dimension level attributes are not the object of multidimensional analysis.

![](/api/attachments/WUA3WGQC/fulltext/images/165525c46af4c1a9d79b015a676254336189fc32d5b8fbde533081a9175573f3.jpg)  
Fig. 1. Multidimensional representation of data.

Instances of dimension levels are called dimension members. For a given measure in an n-dimensional (hyper)cube, a combination of n dimension members, e.g. (3 March 02, “P1”, “Paris”), uniquely identifies a cell and therefore a measure value (4000 Euros). More specifically, for each axis, the dimension members used as coordinates are instances of the least aggregated dimension level. In the sequel, we will refer to these dimension levels (in our example, Day, Product and City) as the “base dimension levels” of their respective dimensions (Time, Product and Geography).

## 3.2. The unified multidimensional metamodel

The key concepts of the unified multidimensional metamodel (Fig. 2) are dimensions and facts. These two concepts are interrelated and composed of hierarchies and measures, respectively. Dimensions are defined by grouping dimension levels into hierarchies (through classification relationships) and then hierarchies into dimensions. A classification relationship links a child dimension level to a parent dimension level. Classification relationships are sometimes called drilling or rollup relationships in other multidimensional metamodels. Similarly to [38], we define a hierarchy as a meaningful sequence of classification relationships where the parent dimension level of a classification relationship is also the child of the next classification relationship. In other words, a hierarchy is a meaningful aggregation path between dimension levels. An aggregation path is “meaningful” if valid sequences of drill-down and/or rollup operations can be performed by following the path. Note that different hierarchies may share common dimension levels and even common classification relationships. From the definition of hierarchies, dimensions are in turn defined as meaningful groupings of hierarchies. Dimension levels own dimension level attributes, which may be identifying or non-identifying attributes. Some multidimensional metamodels do not distinguish between dimension levels and dimension level identifying attributes. However, dimension levels and their identifying attributes are not semantically equivalent; therefore they need to be represented as distinct concepts in the multidimensional metamodel. Using the isTime attribute, we distinguish between temporal and non-temporal dimension levels. This distinction is implicit at the physical level i.e. in OLAP tools, which offer builtin functions to handle time. Due to the ubiquity of time in data warehouses, as well as the specific semantics associated with it, we believe, similarly to [25], that the distinction between temporal and non-temporal dimension levels should not be postponed to the physical level and should already appear at the logical level, i.e. in the multidimensional metamodel.

![](/api/attachments/WUA3WGQC/fulltext/images/c15d3852f9674ffc290fc1893204bea4a1be24c12787b6b6cc215ce765fb765b.jpg)  
Fig. 2. Unified multidimensional metamodel.

Facts are composed of measures. We do not require measures to be of numeric type, as long as their values are totally ordered. For example, a measure can be an enumeration type. Some facts have no measure (this corresponds to the notion of factless fact table in [16]). Facts are dimensioned by dimension levels, called “base dimension levels” in Section 3.1. The relationship between a fact and each of its dimension levels is called dimensioning. Among the dimension levels related to a fact, some may not be necessary to functionally determine the fact. They are defined as not minimal in the multidimensional schema (in reference to the concept of minimal functional dependency in relational theory). For example, a fact Rental may be dimensioned by Vehicle, Customer and Date. All these dimension levels are relevant for analyzing the rental and its associated measures. However, a given Vehicle and a given Date uniquely identify a Rental. Therefore, the dimension level Customer is not minimal. It is worth noting that the concept of “minimal” is used with various meanings in multidimensional modeling. Our definition of minimal dimension level, based on functional dependencies, is in line with the notion of multidimensional normal form presented in [19]. However, following [24], we may consider that a multidimensional schema is minimal if it contains only dimensions mentioned in user queries (or more generally, user requirements). In this sense, a multidimensional schema may be minimal even if it contains non-minimal dimension levels. When they are derived from user requirements, non-minimal dimension levels are rightly represented in multidimensional schemas. However, they will often be implemented specifically in MOLAP or ROLAP tools. Therefore they are represented explicitly as non-minimal dimension levels.

Different facts may share the same set of dimension levels (in our example, we could imagine the fact Stock, indicating the quantity stored by Product, Day and City).

In order to enable correct aggregation of measures along hierarchies, the definition of applicable aggregation functions is crucial [19,20,27]. For every measure, for every dimension level dimensioning the measure (i.e. dimensioning the fact which bears the measure), the set of aggregation functions applicable along the different hierarchies starting from the dimension level has to be specified. Based on the aggregation functions available in OLAP tools, the unified multidimensional metamodel considers the following functions: SUM, AVG, MIN, MAX, MED (median), VAR (variance), STDDEV and COUNT. Following [27,31], we distinguish between three classes of aggregation functions. The first class of functions, which includes all aggregation functions ({SUM, AVG, MIN, MAX, MED, VAR, STDDEV, COUNT}), is applicable to measures that can be summed. The second class of functions ({AVG, MIN, MAX, MED, VAR, STDDEV, COUNT}) applies to measures that can be used for average calculations. The last class contains the single function COUNT. In the Sale example, considering the measure “sale amount”, the function SUM (and therefore all other aggregation functions) applies to all the hierarchies starting from the dimension levels Day, Product and City. Our model explicitly acknowledges that for a given measure, applicable aggregation functions depend not only on dimensions, but on hierarchies within dimensions. Moreover, for a given hierarchy, the aggregation functions can be applicable only to the first n levels of the hierarchy (this will be illustrated in Section 4 with the case study).

Our unified multidimensional metamodel shares many concepts with the OLAP metamodel in the CWM architecture [25]. However, OMG's OLAP metamodel is currently not acknowledged as the standard multidimensional metamodel by the research community. Furthermore, this metamodel lacks some important concepts found in other multidimensional metamodels (for example, the notion of dimension level attribute should be represented as a concept in its own right). OMG's OLAP metamodel also incorporates some concepts that are peripheral to multidimensional modeling and/or are related to implementation, i.e. belong to the physical level. In order to enable user interaction and visualization of multidimensional schemas by means of a graphical notation, we argue that logical and physical concepts must remain separate and the number of multidimensional concepts must be kept relatively small. Fig. 3 illustrates the graphical notation associated with the unified multidimensional metamodel, using the Sale example. By default, the name of a dimension is the name of its base dimension level; otherwise the name of the base dimension level is followed by the name of the dimension. When a dimensioning is not minimal—this does not happen in the Sale example—it is represented with a dotted line instead of a plain line.

![](/api/attachments/WUA3WGQC/fulltext/images/19ea8cbecfb7be678b422958e34e21d00aef1935f95cf16a3267fd9e28f6b86e.jpg)  
Fig. 3. Graphical notation for multidimensional schemas.

In order to define our graphical notation, we have used built-in extensibility mechanisms of UML, namely stereotypes and tagged values. We have also defined a specific graphical notation for stereotypes, as permitted by the UML specification. This specific notation makes multidimensional schemas more concise and more readable. However, alternatively, the standard UML notation may be used, e.g. for representing multidimensional schemas with a UML CASE tool. In Fig. 4, using an excerpt from Fig. 3, we illustrate the correspondence between our graphical notation (left part of the schema) and the standard UML notation (right part of the schema).

![](/api/attachments/WUA3WGQC/fulltext/images/74a52ea99904370d67b78c8eff8041a87dda3d58377864dbcbf3d5b994056c1c.jpg)  
Fig. 4. Representing multidimensional schemas in standard UML notation.

A graphical multidimensional schema must be completed with information on applicable aggregation functions: for each measure of each fact, the applicable aggregation functions must be specified for each dimension level. Since the specification of aggregation functions is generally complex and may reduce readability of graphical schemas, it should be presented in a separate table [14].

The unified multidimensional metamodel presented in this section is used as a pivot metamodel in our design method.

## 4. The data warehouse design method

Our method considers both user requirements and operational data sources for data warehouse development. However, we believe that data warehouse designers should first define the information needed by users (decision makers), without being limited by the information stored in operational databases. This is the only way to prevent critical business needs from being overlooked. Therefore, our method is primarily user requirements-driven. Starting from an informal statement of the information needed by decision makers, the method is decomposed into a conceptual, a logical and a physical phase. Finally, the data confrontation phase takes operational data into consideration, defining how and to what extent the decision makers' information needs can be fulfilled by operational data sources. The four phases are represented in Fig. 5.

– The conceptual phase is decomposed into two steps. In step 1, the designer collects and represents the decision makers' information requirements. To this end, he may use any UML-compliant system analysis method. Requirements engineering techniques used in the OLTP world are applicable. More specifically, interviews and joint sessions are used, as well as the study of existing reports and the prototyping of future reports. Planned queries are also considered in order to fully specify the information needed by users for analysis and decision making. User requirements are represented in a UML class diagram. This UML model is then enriched and transformed in step 2, in order to ease the automatic mapping of the model into a logical multidimensional schema.

![](/api/attachments/WUA3WGQC/fulltext/images/e5a0f7d9b225d052f8ecb98bd31ed33fdb0f6e7b87c81eb160bc974f43fd1efe.jpg)  
Fig. 5. The four phases of the data warehouse design method.

– In the logical phase, the UML model resulting from the conceptual phase is mapped into a multidimensional schema expressed with the unified multidimensional metamodel presented in Section 3. This is achieved through a set of mapping transformations.

– The physical phase maps the multidimensional schema into a physical database schema, depending on the target OLAP tool. A specific set of mapping transformations is defined for each type of tool. Due to space limitations, the present paper focuses on Oracle MOLAP implementation.

– The data confrontation phase consists in mapping the physical schema data elements to the data sources. It leads to the definition of queries for extracting the operational data in the physical data warehouse schema. This is a crucial phase in the data warehouse design method. However, the complex ETL techniques used in this phase are beyond the scope of this paper.

We detail below the content of the conceptual, logical and physical design phases, i.e. the metamodels used and the transformations performed at each phase. The transformations are described in natural language and specified formally in OCL. A transformation is represented as an operation, which is specified with pre- and post-conditions written in OCL. The latter is well suited to the formal specification of operations; in particular, the declarative style of OCL emphasizes the effect of operations rather than their actual implementation. The latest version of OCL supports collections of collections, which is useful for the specification of some transformations of our design method. We have checked the syntactic correctness of all our specifications using the OCL checker [17]. Due to space limitations, this paper shows the OCL specification for the first transformation only. For other examples, the reader may refer to [30].

In order to illustrate the step-by-step application of our method, we use a case study related to media-planning activities.

## 4.1. Conceptual design

The conceptual design phase of our method is grounded on the following principles. Having established that the multidimensional metamodel belongs to the logical level, we need a conceptual modeling formalism to specify users' information needs before proceeding to logical design. This conceptual modeling formalism needs to be familiar to users and designers, like ER or UML for example. In order to ease automatic mapping of the conceptual model into a multidimensional schema, we need to incorporate into the conceptual model some information specific to multidimensional modeling. However, we should avoid to incorporate too much multidimensional information into the conceptual model: the multidimensional metamodel belongs to the logical level and mixing multidimensional concepts like dimensions or hierarchies with concepts like entities, relationships, classes or generalizations can be a source of confusion when defining and validating the conceptual model with users. We have chosen UML as the conceptual modeling formalism. This is in line with the current trend, e.g. the Common Warehouse Metamodel. Furthermore, like [1,7], we see many benefits in applying the object-oriented approach to data warehousing and OLAP. By choosing UML for conceptual data warehouse design, we benefit from the following advantages:

– Familiarity of designers with the formalism, capitalization on previous research work concerning not only UML but also ER (since UML can be viewed as an extension to ER).

– Simplicity of UML class diagrams and richer semantics than ER diagrams. In particular, UML offers many varieties of the basic ER relationship (e.g. aggregation and generalization), which is very useful for the definition of multidimensional hierarchies in the logical phase [3].

– Possibility of mapping the conceptual UML model into a multidimensional schema in a quasi-automated way (as the description of the logical design phase shall illustrate).

The conceptual design phase is subdivided into two steps. Step 1 leads to a UML model, more precisely to a class diagram without operations. Step 2 enriches and transforms this model to facilitate its automatic mapping into a unified multidimensional schema. Four types of transformations are conducted: the determination of identifying attributes, the determination of measures, the migration of association attributes and the transformation of generalizations.

## 4.1.1. Initial UML model definition

Using any UML-compliant requirements engineering method, the designer defines the UML class diagram representing the decision makers' initial information requirements. This first step of the data warehouse design method uses no multidimensional concepts, thereby enabling maximal reuse of systems analysis methods commonly used for transactional systems engineering.

We illustrate this first step using the media-planning case study, presenting the decision makers' initial requirements and the resulting UML class diagram (Fig. 6).

A company is faced with the definition of an optimal media-planning system. Periodically, the company launches advertising campaigns for its products using several types of media. The media-planning problem consists in choosing the media which will reach the maximal number of consumers and have the maximum effect on the consumption of the advertised products. To assist managers in this complex, ill-structured problem, the company launches a data warehousing project. The data warehouse will be built incrementally and made available to managers via OLAP and data mining tools. The first step is the definition of the conceptual model of the data warehouse, which is based on the following requirements (the actual case study has been simplified for the sake of this paper). The consumer base is decomposed into predefined targets i.e. segments. A target is identified by a code and characterized by a marital status, a minimum and maximum age, a sex and a region (e.g. all married female consumers aged between 30 and 49, living in the South-West). For each region, decision makers need to know the respective percentage of the different targets located in this region. Products are characterized by a code, a name and a product type which determines the product unit. The product unit is used to measure the consumption of the product (e.g. for products of type “beer”, the consumption is measured in liters). Media are characterized by a name (e.g. “Channel n”) and an advertising price. The latter is expressed per media unit. The unit depends on the media type. In the case of TV for example, the unit is one minute and the advertising price is expressed in dollars per minute. When choosing between alternative media, knowing the shareholding structure of the media may sometimes prove useful. For every media, the decision makers must be able to know its main shareholder at a given date, as well as the percentage of shares it holds. A shareholder may be either public, private or both (jointly owned companies). Private shareholders may be either individuals or companies. Public shareholders are characterized by their level (e.g. a city, a state, the country…). The exposure of targets to media (i.e. their media “consumption”) is measured on a quarterly basis. The exposure is expressed in the media unit. Similarly, the purchase of products by target is measured every quarter. It is expressed in total quantity (based on the product unit) and in total dollar amount. Finally, the influence of past campaigns on purchases is measured by an influence coefficient, which is estimated with data mining techniques.

![](/api/attachments/WUA3WGQC/fulltext/images/df1e629676ea8f45a82cd4dcfba9daf68a874c5c629726ca7aa1810b3b464a2f.jpg)  
Fig. 6. Initial UML conceptual model for the media-planning example.

## 4.1.2. Enrichment/transformation of the UML model

This second step of conceptual design aims at facilitating subsequent mapping of the UML conceptual model into a logical multidimensional schema. To achieve this, we need to extend the standard UML metamodel, adding as few concepts as necessary to ease the automatic mapping. To extend UML, we use the extensibility mechanisms of stereotypes and tagged values [25]. The extended UML metamodel is presented in Fig. 7 (the extensions are represented in italics).

Classes which are not association classes are called ordinary classes. Similarly, associations which are not association classes are called ordinary associations. The main extensions are the attribute measure of class Attribute (which indicates if the attribute is a measure of interest), and the attribute identifyingAttribute, which indicates if an attribute identifies its owner class. The attribute identifyingAttribute is only necessary for the attributes of ordinary classes, since an association class is identified by the n-uple of identifying attributes of the participating classes.

![](/api/attachments/WUA3WGQC/fulltext/images/60d15afd79ab0a3020487aaa4571c71a7249f0fb2077503e2c39813c714c0437.jpg)  
Fig. 7. Extended UML metamodel.

The four transformations performed on the UML conceptual model in order to ease its subsequent logical mapping are presented below. Each of the four transformations is applied in turn to the media-planning case study, explaining how the initial UML model of Fig. 6 is progressively transformed into the final model of Fig. 8. In addition to the natural language definition, we illustrate the formal specification of the first transformation with OCL. A transformation is represented with OCL as an operation of the UML model considered, associated with pre- and post-conditions.

4.1.2.1. Determination of identifying attributes. Since the notion of identifying attribute is not defined in the UML standard, we need to determine explicitly the identifying attributes of classes in order to be able to define the dimensions of the multidimensional schema at the logical level. For each ordinary class of the UML model, the data warehouse designer and the user have to decide which attribute identifies the class. If necessary, a specific attribute is created in order to identify the class. Identifying attributes are specified using {id} tagged values, added to each identifying attribute.

Our method does not allow ordinary classes to be identified by a composite identifier. If an ordinary class is identified by several attributes, the latter are concatenated into a single identifying attribute, thus simplifying implementation into ROLAP or MOLAP tools. This is in line with assumptions made in related work (for example, dimension tables in Kimball's star schemas are defined as having a single part primary key [16]). The process of determining identifying attributes of ordinary classes can be synthesized by the following transformation (semiformally defined and then expressed in OCL):

## Box 1

Transformation Tcc1: Each attribute of an ordinary class is either an identifying attribute or not.

context UMLModel::Tcc1(ordinaryClass:OrdinaryClass)

post: --All attributes owned by the ordinary class before the --transformation have a determined status. Among these --attributes,at most one is an identifying attribute.

ordinaryClass.attribute@pre->forAll(a1:AttributeOfOrdinaryClass |

a1.identifyingAttribute=true or a1.identifyingAttribute=false) and

ordinaryClass.attribute@pre->select(a1:AttributeOfOrdinaryClass |

a1.identifyingAttribute=true)->size()<=1

post: --If no identifying attribute has been found among the --attributes of the ordinary class, a new identifying 1} --attribute has been created and inserted as the first --attribute of the class.

if not ordinaryClass.attribute@pre->exists

then ordinaryClass.attribute->size()= ordinaryClass.attribute@pre->size ()+1 and ordinaryClass.attribute->at(1) .oclIsNew () and ordinaryClass.attribute->at(1) .identifyingAttribute=true

else true -- else˝

endif

In the media-planning case study, all ordinary classes are identified by their first attribute; therefore no special attribute definition is required. Concerning the generalization hierarchy, the subclasses of Shareholder inherit the identifying attribute shareholder\_name.

4.1.2.2. Determination of attributes representing measures. We differentiate between attributes representing measures, and attributes expressing qualitative values. As described in Section 3, this distinction is not based on data types even if measures are generally numeric and qualitative attributes are not. Therefore this differentiation cannot be performed automatically. The designer and the user have to decide jointly which attributes are measures. Note that this is unnecessary for identifying attributes determined previously, since an identifying attribute cannot be a measure. In our UML model, attributes representing measures are specified by the {meas} tagged values. This process can be synthesized as follows:

## Box 2

Transformation Tcc2: Each attribute is either a measure or not.

In our example, all attributes of association classes are defined as measures. These attributes are: percentage\_of\_region, media\_exposure, quantity, amount, influence\_coefficient and percentage\_of\_shares. Concerning ordinary classes, the data warehouse designer and user decide that the following attributes should be considered as measures of interest: advertising\_price (class Media) and number\_of\_inhabitants (class Region).

4.1.2.3. Migration of association attributes. This step is concerned with N–1 and 1–1 associations having specific attributes (since they bear attributes, these associations are actually association classes). This case is rarely encountered in practice. If specific attributes are present in these associations, the designer should first check the validity of this representation. Even if their presence cannot be questioned, these attributes cannot be mapped into multidimensional schemas by using hierarchies, since multidimensional hierarchies do not contain information. Therefore, N–1 association attributes must migrate from the association to the participating class on the N side. 1–1 association attributes can indifferently migrate to one of the two participating classes. After migrating the attributes of an N–1 or 1–1 association, the latter is transformed into an ordinary association unless it is itself participating to other associations. The transformations for migrating association attributes are expressed as follows:

## Box 3

Transformation Tcc3a: Each attribute belonging to a 1–1 association is transferred to either one of the classes involved in the association.

Transformation Tcc3b: Each attribute belonging to an N–1 association is transferred to the N-class, i.e. the class involved several times in the association.

In the media-planning conceptual model, transformation Tcc3b is applied to the association class between the classes Region and Target: the attribute percentage\_of\_region is transferred to Target, and the association class becomes an ordinary association.

4.1.2.4. Transformation of generalizations. The generalizations of the UML notation cannot be mapped directly into hierarchies in the multidimensional schema, since the semantics of hierarchies in object-oriented and multidimensional formalisms differ.<sup>2</sup> However, we want to preserve the information contained in UML generalization hierarchies and transform them to enable their automatic mapping into multidimensional hierarchies in the logical phase. To this end, we transform the generalizations into aggregations and classes following the transformation suggested by [22] for ER models. We have adapted this transformation to UML and extended it to consider the different cases of incomplete and/or overlapping specialization. The corresponding transformation is described below:

Box 4

Transformation Tcc4: For each class C such that C is the root of a specialization hierarchy, for each specialization level $\mathrm { L } _ { \mathrm { i } }$ of C, a class named $\mathrm { T y p e - C - i }$ is created. The occurrences of these classes define all the specializations of C. In case of overlapping between specializations, a special value is created for each overlapping between two or more sub-classes of C. In case of incomplete specialization, the special value “others” is created. An aggregation is created between class C and each of the classes $\mathrm { T y p e { - } C _ { \mathrm { - } i } \ ( T y p e { - } C _ { \mathrm { - } i } }$ is the aggregate, with multiplicity 1; C is the part, with multiplicity \*).

Since Tcc4 transforms the subclasses of class C into the classes ${ \mathrm { T y p e } } { \mathrm { - } } { \mathrm { C } } { \mathrm { - i } } ,$ the attributes and/or relationships of these subclasses are transferred to class C. This strategy may result in information loss and/or null values. However, we find it preferable than purely omitting the attributes/relationships in the transformed conceptual model. Each of the classes $\mathrm { T y p e - C - _ { i } }$ has only one attribute, which identifies $\mathrm { T y p e - C - _ { i } }$ (in order to specify this information, transformation Tcc1 should be applied to all the classes $\mathrm { T y p e - C _ { \mathrm { - i } } ) }$ . The mapping of UML generalizations into multidimensional schemas is a subject in its own right. This issue is developed more thoroughly in [3], which presents a set of transformations for defining dimension hierarchies from UML generalizations and aggregations.

In the case study, the specialization hierarchy rooted in class Shareholder has two specialization levels. Therefore, two classes Type-shareholder- and Type-shareholder- are created and renamed as Shareholder\_type and Private\_ shareholder\_type respectively. The set of occurrences of Shareholder\_type (i.e. the set of values of its identifying attribute shareholder\_type) is {private, public, both}. The special value “both” results from the overlapping constraint in the initial conceptual model. Similarly, the set of occurrences of Private\_shareholder\_type is {person, company, others}. An aggregation is created for Shareholder\_type and Private\_shareholder\_type. The attributes of the subclasses (attributes manager\_name and public\_shareholder\_level) are transferred to the class Shareholder. The enriched/transformed conceptual model, resulting from transformations Tcc1 to Tcc4, is represented in Fig. 8.

![](/api/attachments/WUA3WGQC/fulltext/images/c39ca2dd2b39e7c3d1e1a09b32933d9167c18507646c79dd904de1c4bafb3936.jpg)  
Fig. 8. Enriched/transformed media-planning UML model.

After applying these transformations, the resulting UML model is ready for logical mapping.

## 4.2. Logical design

This phase maps the enriched and transformed UML conceptual model into a logical schema expressed with the concepts of the unified multidimensional metamodel. The logical multidimensional schema is generated by means of the transformations detailed below. The step-by-step application of the transformations is illustrated with the case study. The final multidimensional schema, represented with the graphical notation introduced in Section 3, appears in Fig. 9.

Logical design is decomposed into five steps, each step elaborating on the results of the previous steps: (1) Definition of facts (transformations Tcl1a and Tcl1b). The definition of a fact includes the definition of its measures and of the dimension levels related to it. (2) Definition of hierarchies (transformation Tcl2). (3) Definition of dimensions (transformation Tcl3). (4) Definition of dimension level attributes (transformation Tcl4). (5) Definition of the aggregation functions that may be applied to measures along hierarchies (transformation Tcl5).

The facts and measures of the logical multidimensional schema are defined from the N–M and n–ary associations of the enriched/transformed UML conceptual model (transformation Tcl1a), and from the ordinary classes of the UML model which own at least one attribute characterized as a measure (transformation Tcl1b):

## Box 5

Transformation Tcl1a: Every N–M or n–ary association of the conceptual model is mapped into a fact in the logical multidimensional schema. The attributes of the association (if any) are mapped into measures of the fact. The fact is dimensioned by dimension levels defined by mapping the ordinary classes directly or indirectly involved in the association.

Transformation Tcl1b: For every conceptual ordinary class with at least one attribute which is a measure of interest, a fact is defined in the logical multidimensional schema. The attributes of the ordinary class which are measures of interest, are mapped into measures of the fact. The fact is dimensioned by one dimension level, defined by mapping the class.

The association mapped by transformation Tcl1a may have one (or several) association class(es) among its participating classes. In this case, the transformation replaces the association class with its participating classes. This principle is applied recursively so that ultimately, all the classes directly or indirectly involved in the mapped association are ordinary classes. These ordinary classes may be mapped directly into dimension levels. When mapping an ordinary class into a dimension level, transformations Tcl1a and Tcl1b map the identifying attribute of the class into the identifying attribute of the dimension level. Depending on the semantics of the class, the dimension level is characterized as temporal or non-temporal.

When the association mapped by transformation Tcl1a is n–ary, it may have one (or several) association end(s) with an upper bound (maximal cardinality) of 1. In this case, the corresponding dimensioning–i.e. the link between the fact defined from the association and the dimension level defined from the class linked to the association end–is characterized as non minimal. This information will be useful for subsequent physical implementation. Transformation Tcl1a applies to the particular case of N–M and n–ary associations without attributes, which corresponds to Kimball's concept of “factless fact table” [16].

Applying transformation Tcl1a, the following N–M and n–ary associations of the enriched/transformed mediaplanning conceptual model are mapped:

– The association Purchase is mapped into a fact, with the measures quantity and amount. The dimension levels Product, Target and Quarter are created in order to characterize the fact Purchase. These dimension levels are identified by the attributes product\_code, target\_code and quarter respectively. The dimension level Quarter is characterized as temporal.

– Similarly, the association Exposure is mapped into a fact, with the measure media\_exposure. This fact is dimensioned by Media, Target and Quarter.

– The association Influence\_of\_campaign between the class Advertising\_campaign and the class Purchase is mapped into a fact. This fact includes the measure influence\_coefficient and is dimensioned by the dimension levels Advertising\_campaign, Product, Target and Quarter (since the class Purchase is an association class, the last three dimension levels correspond to the ordinary classes involved in the association class Purchase).

– The association Main\_shareholder becomes a fact with the measure percentage\_of\_shares. The fact is dimensioned by Media, Date (a temporal dimension level) and Shareholder. The dimensioning between the fact Main\_shareholder and the dimension level Shareholder is not minimal (following the multiplicity of 1 in the conceptual model).

– The N–M association between Region and Media is mapped into the fact Gets, dimensioned by Region and Media. This fact bears no measure. Similarly, the association between Media and Advertising\_campaign is mapped into the fact In.

In the enriched/transformed media-planning conceptual model, the ordinary classes Region, Target and Media have an attribute which is a measure of interest. Therefore, applying transformation Tcl1b, the facts Region\_fact, Target\_fact and Media\_fact are created with the measures number\_of\_inhabitants, percentage\_of\_region and advertising\_price respectively. These facts are dimensioned by the dimension levels Region, Target and Media respectively (these dimension levels have been created by transformation Tcl1a).

The hierarchies of the logical multidimensional schema are defined from the N–1 (and 1–1) associations of the enriched/transformed UML conceptual model:

Box 6

Transformation Tcl2: For each dimension level DL dimensioning at least one fact in the logical multidimensional schema, a set of hierarchies is defined. These hierarchies are defined starting from the conceptual ordinary class OC(DL) corresponding to DL. Each acyclic path of N–1 (or 1–1) associations between ordinary classes starting from OC(DL), noted $\mathrm { O C ( D L ) { \to } O C } _ { 2 } { \to } \ldots { \to } \mathrm { O C } _ { n } ,$ is mapped into a hierarchy $\mathrm { D L } { \longrightarrow } \mathrm { D L } _ { 2 } { \longrightarrow } . . . { \longrightarrow } \mathrm { D L } _ { n } { \longrightarrow } \mathrm { A l l } ,$ where dimension level $\mathrm { D L } _ { i ( i = 2 , \cdots , n ) }$ is defined by mapping ordinary class OC . If no acyclic path of N–1 (or 1–1) associations links OC(DL) to other ordinary classes, only the hierarchy DL→All is defined.

The dimension levels dimensioning at least one fact are those resulting from transformations Tcl1a and Tcl1b. In relational terms, a path $\scriptstyle { \mathrm { O C ( D L ) } } \to { \mathrm { O C } } _ { 2 } { \longrightarrow } \dots { \longrightarrow } { \mathrm { O C } } _ { n }$ of N–1 or 1–1 associations between ordinary classes (starting from OC(DL)) may be interpreted as a path of functional dependencies. Note that only acyclic paths are considered. Thus, transformation Tcl2 cannot generate cyclic multidimensional hierarchies. This is meant to prevent recursivity problems when performing aggregations based on the hierarchies. N–1 associations are frequently aggregations or compositions. Therefore, the hierarchies generated by transformation Tcl2 often correspond to aggregation/composition paths in the UML conceptual model. As a consequence of transformation Tcl2, the dimension level All is the upper level of all hierarchies. This will enable users of the implemented multidimensional schema to perform aggregations at the highest possible level.

Applying transformation Tcl2 to each of the dimension levels already defined in the media-planning logical multidimensional schema, we obtain the following hierarchies:

– For Product: Product→Product\_type→All

– For Target: Target→Region→All

– For Quarter: Quarter→Year→All

– For Media: Media→Media\_type→All

– For Advertising\_campaign: Advertising\_campaign→Product→Product\_type→All and Advertising\_campaign→Quarter→Year→All

– For Date: Date→Quarter→Year→All

– For Shareholder: Shareholder→Shareholder\_type→All and Shareholder→Private\_shareholder\_type→All – For Region: Region→All.

The new dimension levels resulting from transformation Tcl2 are: All, Product\_type, Year, Media\_type, Shareholder\_type and Private\_shareholder\_type. These dimension levels are created with their identifying attribute. Year is a temporal dimension level.

Dimensions are defined by grouping hierarchies using transformation Tcl3:

## Box 7

Transformation Tcl3: For each dimension level DL dimensioning at least one fact in the logical multidimensional schema, a dimension is defined. This dimension is composed of all hierarchies defined for DL.

DL is the base dimension level. By default, the name of the dimension is the name of DL. Another name may be chosen if it expresses the semantics of the dimension more appropriately.

Applying transformation Tcl3, a dimension is defined for each of the following dimension levels: Product, Target, Quarter, Media, Advertising\_campaign, Date, Shareholder and Region. The dimension defined for each dimension level comprises all hierarchies defined for this dimension level in transformation Tcl2. The dimension Date is renamed Time.

Tcl4 completes the definition of dimension levels with their non-identifying attributes:

## Box 8

Transformation Tcl4: For each dimension level DL of the logical multidimensional schema, the non-identifying attributes of DL are defined from the conceptual ordinary class OC(DL) corresponding to DL: each nonidentifying attribute of OC(DL) which is not a measure of interest is mapped into a non-identifying attribute of DL.

Transformation Tcl4 yields the following non-identifying attributes for the dimension levels of the mediaplanning multidimensional schema: For Product: product\_name; For Target: status, minimum\_age, maximum\_age and sex; For Shareholder: public\_shareholder\_level and manager\_name; For Product\_type: product\_unit; For Media\_type: media\_unit. The graphical representation of the media-planning multidimensional schema, resulting from transformations Tcl1a to Tcl4, is shown in Fig. 9 (for the sake of readability, the upper level of all hierarchies, i.e. the dimension level All, is not represented)

The last transformation of the logical design phase, Tcl5, determines the aggregation functions that may be applied to measures along hierarchies. The applicable aggregation functions are presented in a table which complements the graphical multidimensional schema. Following [20], we distinguish between measures expressing a flow (i.e. recording a cumulative effect over a period of time), measures expressing a stock (i.e. recording a level at specific points in time), and measures expressing a value per unit (e.g. the price of an item, an exchange rate or a percentage). Based on this distinction, transformation Tcl5 contains guidelines adapted from the summarizability rules defined in [20]. However, these guidelines do not work all the time: in order to determine correctly the aggregation functions that may be applied to a measure, the data warehouse designer should carefully consider the semantics of both the measure and the associated dimension levels.

![](/api/attachments/WUA3WGQC/fulltext/images/5b3052ac9bae5f874d924b0248168fa00ec293849b87003c0cc7075cf6f3d498.jpg)  
Fig. 9. Media-planning logical multidimensional schema.

## Box 9

Transformation Tcl5: For each measure M of each fact F in the logical multidimensional schema, for each dimension $\mathrm { D } _ { \mathrm { i } }$ dimensioning F, the set of aggregation functions applicable along D (i.e. along the hierarchies of $\mathrm { D } _ { \mathrm { i } } )$ is determined based on the following principles:

If M expresses a flow, the set of applicable aggregation functions is normally {SUM, AVG, MIN, MAX, MED, VAR, STDDEV, COUNT}, whatever D . If M expresses a value per unit, the set of applicable aggregation functions is normally {AVG, MIN, MAX, MED, VAR, STDDEV, COUNT}, whatever $\mathrm { D } _ { \mathrm { i } } .$ . If M expresses a stock, the set of applicable aggregation functions is normally {SUM, AVG, MIN, MAX, MED, VAR, STDDEV, COUNT} if the base dimension level of $\mathrm { \Delta D _ { i } }$ is non-temporal, and {AVG, MIN, MAX, MED, VAR, STDDEV, COUNT} otherwise. The set of applicable aggregation functions may in some cases be more restricted than suggested by these principles. Therefore, the application of these principles has to be checked against the exact semantics of M for each dimension level of every hierarchy of all $\operatorname { D } _ { \mathrm { i } } ^ { \cdot }$ for a given dimension $\mathrm { D } _ { \mathrm { i } } ,$ the applicable aggregation functions may depend on the hierarchies of $\operatorname { D } _ { \mathrm { i } } ,$ or even on the levels of the same hierarchy.

By definition, a fact F is dimensioned by a dimension $\mathrm { D } _ { \mathrm { i } }$ if F is dimensioned by the base dimension level of $\mathrm { D } _ { \mathrm { i } } .$ As mentioned in Section 3, a set of applicable aggregation functions depends on the levels of a hierarchy if the aggregation functions apply only to the first n levels of the hierarchy.

Due to space limitations, we are not able to detail the applicable aggregation functions for the media-planning example. They result from applying the guidelines of transformation Tcl5 and then checking their validity:

The measures quantity, amount and media\_exposure express a flow; therefore all aggregation functions normally apply along all dimensions dimensioning these measures. The measures influence\_coefficient, percentage\_of\_shares, percentage\_of\_region, and advertising\_price express a value per unit; therefore the functions {AVG, MIN, MAX, MED, VAR, STDDEV, COUNT} apply along all dimensions dimensioning these measures. Finally, the measure number\_of\_inhabitants expresses a stock; therefore all aggregation functions apply to this measure along the dimension Region (Region is a non-temporal dimension level and the only dimension level which dimensions Region\_fact).

– Checking the validity of the aggregation functions, we restrict the applicable aggregation functions for quantity, media\_exposure, and advertising\_price: the unit for quantity purchased depends on the product type, therefore along the Product dimension, aggregations are not valid for the last level of the hierarchy Product→Product\_type→All. Aggregations are only valid for Product→Product\_type. For example, the quantity purchased may be summed for all products of type “beer”, but the quantity of beer may not be summed with the quantity of books. Similarly, media\_exposure and advertising\_price depend on the media unit, which depends on the media type (e.g. television, magazine, …). As a result, media\_exposure and advertising\_price may not be aggregated for different media types.

Let us stress that in our design method, applicable aggregation functions are determined for each hierarchy within each dimension of each measure. This way, we can define applicable aggregation functions accurately, and specify explicitly when aggregation functions apply only to the first n levels of hierarchies (e.g. Product→Product\_type or Media→Media\_type). Our proposal goes beyond the traditional distinction between additive, semi-additive and non-additive facts, proposed in [16]. This latter distinction is centered on the SUM function, and makes no explicit distinction between the hierarchies within a given dimension. In our approach, we can say that a measure is additive (like amount in our case study) if the SUM function may be used along all dimension levels of all hierarchies of all dimensions for this measure. A measure is semi-additive (like quantity) if the SUM function may be used only along some hierarchies or parts of hierarchies. A measure is non-additive (like advertising\_price) if the SUM function may not be used at all for this measure.

## 4.3. Physical design

This phase maps the multidimensional schema (resulting from logical design) into a physical database schema. The physical schema depends on the target MOLAP or ROLAP tool. Therefore, a set of transformations is defined for each type of tool. In [30], we have defined transformations for ROLAP star implementation. In this paper, we consider Oracle MOLAP [4], which is representative of the MOLAP tool category. We present the Oracle MOLAP metamodel and then the transformations that map a logical multidimensional schema into a physical Oracle MOLAP schema.

In [25], the Oracle MOLAP package is defined as a non-normative extension to the Common Warehouse Metamodel. The metamodel shown in Fig. 10 is an adapted version, with the main concepts of the Oracle MOLAP tool.

Physical Oracle MOLAP dimensions are the equivalent of logical dimension levels. Variables correspond to logical measures or dimension level attributes, while logical hierarchies are implemented by means of relations. Both variables and relations are dimensioned. The dimensions of a variable or a relation are specified between “〈〉” in the definition of the variable or relation. A relation is a functional dependency between its dimension(s) and its reference dimension. Dimensions are temporal or non-temporal. Possible types for non-temporal dimensions are ID (a small text, no more than 8 characters), Text (a long text), and Integer (in this case, the values of the dimension will be assigned automatically, forming a series of consecutive integers). Possible types for temporal dimensions are Day, Week, Month, Quarter and Year. For variables, types are Boolean, Date, Decimal, ID, Integer, Short decimal, Short integer and Text.

![](/api/attachments/WUA3WGQC/fulltext/images/4115b9806e050b63465bdf4449b81313bb43a907208c815462257dcb4a3f1806.jpg)  
Fig. 10. Oracle MOLAP metamodel (adapted from [25]).

The transformations described below (transformations Tle1 to Tle6) map a logical multidimensional schema into a physical Oracle MOLAP schema, using the concepts of the Oracle MOLAP metamodel. The transformations map successively: (1) the logical dimension levels (transformation Tle1), (2) the logical measures and facts (transformations Tle2 to Tle4), (3) the logical hierarchies i.e. their classification relationships (transformation Tle5), and (4) the logical dimension level attributes (transformation Tle6). We have defined no transformation for mapping the aggregation functions associated with the measures and hierarchies of the logical multidimensional schema. This is due to the fact that such a mapping cannot be performed easily into Oracle MOLAP concepts. This mapping is only possible at the cost of some programming, e.g. using the Oracle MOLAP Objects development environment [4]. The application of the transformations is illustrated using the media-planning example.

Transformation Tle1 maps the dimension levels of the logical multidimensional schema into dimensions of the physical Oracle MOLAP schema:

Box 10

Transformation Tle1: Each logical dimension level is mapped into a physical dimension. A non-temporal logical dimension level is mapped into a non-temporal physical dimension with data type ID, Text or Integer. A temporal logical dimension level is mapped into a temporal physical dimension with data type Day, Week, Month, Quarter or Year.

The application of transformation Tle1 to the media-planning logical multidimensional schema yields the following physical Oracle MOLAP dimensions (the name of each physical dimension is followed by its type; a physical dimension has the same name as the corresponding logical dimension level, unless the name has to be changed to comply with the naming constraints of Oracle MOLAP Administrator):

<table><tr><td>Product_type Text</td><td>Advert_campaign ID</td><td>Media_type Text</td><td>Pri_shareho_type ID</td></tr><tr><td>Product ID</td><td>Year_ Year</td><td>Media Text</td><td>All_ID</td></tr><tr><td>Region Text</td><td>Quarter_ Quarter</td><td>Shareholder Text</td><td></td></tr><tr><td>Target ID</td><td>Date_ Day</td><td>Shareholder_type ID</td><td></td></tr></table>

Logical measures are mapped by transformation Tle2:

Box 11

Transformation Tle2: Each logical measure is mapped into a physical variable with data type Boolean, Date, Decimal, ID, Integer, Short decimal, Short integer or Text. The variable is dimensioned by the physical dimensions defined by mapping the logical dimension levels associated with the measure.

The logical dimension levels related to a measure are the ones dimensioning the fact of this measure. Note that these dimension levels have been mapped into physical dimensions by transformation Tle1.

We get the following Oracle MOLAP variables for the media-planning example (each variable is specified by its name, type and dimensioning dimensions between “〈〉”):

– Quantity Short decimal 〈Quarter\_ Product Target〉

– Amount Short decimal 〈Quarter\_ Product Target

– Influence\_coeff Short decimal 〈Quarter\_ Advert\_campaign Product Target〉

– Media\_exposure Short decimal 〈Quarter\_ Media Target〉

– Percent\_of\_share Short decimal 〈Date\_ Shareholder Media〉

– Nb\_inhabitants Integer 〈Region〉

– Percent\_region Short decimal 〈Target〉

– Advert\_price Short decimal 〈Media〉

Transformation Tle3 maps logical facts with at least one non-minimal dimensioning:

Box 12

Transformation Tle3: Each logical fact with at least one non-minimal dimensioning, is mapped by defining a physical relation for each non-minimal dimensioning $\mathrm { F D } _ { \mathrm { i } } .$ The reference dimension of the relation is the physical dimension defined by mapping the logical dimension level of $\operatorname { F D } _ { \mathrm { i } } ;$ the relation is dimensioned by the physical dimensions defined by mapping the other logical dimension levels dimensioning the fact.

By definition, among the dimension levels dimensioning a logical fact, a dimension level has a non-minimal dimensioning if it is functionally determined by the others. Therefore, non-minimal dimensionings can be mapped naturally using the Oracle MOLAP concept of relation.

In the media-planning logical multidimensional schema, the fact Main\_shareholder is dimensioned by the dimension levels Shareholder (with a non-minimal dimensioning), Date and Media. Therefore, we get the following Oracle MOLAP relation (specified by its name, reference dimension, and dimensioning dimensions between $^ { 6 6 } ( \rangle ^ { 5 9 } )$ : Main\_shareholder Shareholder 〈Date\_ Media〉.

Tle4 maps the other logical facts, unless they have at least one measure which is always defined:

Box 13

Transformation Tle4: Every logical fact without (1) at least one non-minimal dimensioning and (2) at least one measure which is always defined, is mapped into a physical Boolean variable. The variable is dimensioned by the physical dimensions defined by mapping the logical dimension levels of the fact.

A logical fact with only minimal dimensionings (i.e. a fact not mapped by transformation Tle3) cannot be mapped into an Oracle MOLAP relation. Consequently, for such a fact, we define a dummy Boolean variable in Oracle MOLAP. For each set of values of the dimension levels dimensioning the fact, the corresponding instance of the dummy variable will indicate whether the instance of the fact exists or not. Note that if a logical fact has at least one measure, this measure has been mapped into an Oracle MOLAP variable by transformation Tle2. If the measure is always defined (i.e. it has the same lifetime as the fact), the variable is defined whenever the fact is defined. Therefore, in this case, a dummy variable is not necessary.

From the media-planning logical multidimensional schema, only the fact Main\_shareholder has been mapped by transformation Tle3. Among the remaining facts, the facts Gets and In have no measure (all measures of all other facts are always defined). Therefore, a dummy variable is defined for the fact Gets, in order to indicate which regions get which media. Similarly, a dummy variable is defined for the fact In: Gets Boolean 〈Media Region〉, In Boolean 〈Advert\_campaign Media〉.

Transformation Tle5 maps logical hierarchies by mapping their classification relationships:

Box 14

Transformation Tle5: Every logical classification relationship $\mathrm { D L } _ { i } { \longrightarrow } \mathrm { D L } _ { i + 1 }$ is mapped into a physical relation. The reference dimension of the relation is the physical dimension defined by mapping the logical dimension level $\mathrm { D L } _ { i + 1 } ;$ the relation is dimensioned by the physical dimension defined by mapping the logical dimension level $\operatorname { D L } _ { i \cdot }$

In the media-planning logical multidimensional schema, the following classification relationships have been defined (in transformation Tcl2): Product→Product\_type, Product\_type→All, Target→Region, Region→All, Quarter→Year, Year→All, Media→Media\_type, Media\_type→All, Date→Quarter, Advertising\_campaign→ Product, Advertising\_campaign→Quarter, Shareholder→Shareholder\_type, Shareholder\_type→All, Shareholder→Private\_shareholder\_type and Private\_shareholder\_type→All. An Oracle MOLAP relation is defined for each of these classification relationships:

<table><tr><td>Type.product Product_type &lt;Product&gt;</td><td>Product.campaign Product &lt;Advert_campaign&gt;</td></tr><tr><td>All.product_type All_ &lt;Product_type&gt;</td><td>Quarter.campaign Quarter_ &lt;Advert_campaign&gt;</td></tr><tr><td>Region.target Region &lt;Target&gt;</td><td>Quarter.date Quarter_ &lt;Date_)</td></tr><tr><td>All.region All_ &lt;Region&gt;</td><td>Share_type.share Shareholder_type &lt;Shareholder&gt;</td></tr><tr><td>Year quarter Year_ &lt;Quarter_)</td><td>All.share All_ &lt;Shareholder_type&gt;</td></tr><tr><td>All.year All_&lt;Year_)</td><td>Pri_type.share Pri_shareho_type &lt;Shareholder&gt;</td></tr><tr><td>Type.media Media_type &lt;Media&gt;</td><td>All.private All_ &lt;Pri_shareho_type&gt;</td></tr><tr><td>All.media_type All_ &lt;Media_type&gt;</td><td></td></tr></table>

Finally, transformation Tle6 maps logical dimension level attributes. Note that transformation Tle1 deals with the identifying attributes of dimension levels (the values of each physical dimension defined by transformation Tle1 will be the values of the identifying attribute of the corresponding logical dimension level). Consequently, Tle6 maps nonidentifying dimension level attributes only:

Box 15

Transformation Tle6: Every logical non-identifying dimension level attribute is mapped into a physical variable with data type Boolean, Date, Decimal, ID, Integer, Short decimal, Short integer or Text. The variable is dimensioned by the physical dimension defined by mapping the logical dimension level containing the given attribute.

Applying transformation Tle6 to each non-identifying dimension level attribute of the media-planning logical multidimensional schema, we get the following variables:

<table><tr><td>Product_unit Text $\langle Product\_type \rangle$ </td><td>Sex ID $\langle Target \rangle$ </td></tr><tr><td>Product_name Text $\langle Product \rangle$ </td><td>Media_unit Text $\langle Media\_type \rangle$ </td></tr><tr><td>Status_ID $\langle Target \rangle$ </td><td>Pub_share_level ID $\langle Shareholder \rangle$ </td></tr><tr><td>Minimum_age Short integer $\langle Target \rangle$ </td><td>Manager_name Text $\langle Shareholder \rangle$ </td></tr><tr><td>Minimum_age Short integer $\langle Target \rangle$ </td><td></td></tr></table>

Thanks to these transformations, the definition of the Oracle MOLAP schema in the Oracle MOLAP command language can be generated from the logical multidimensional schema, in a quasi automated way. The generation of dimensions is straightforward. The process also generates new variables, going beyond the explicit requirements, such as the variable Gets which materializes the relationship between Regions and Medias. This example illustrates the richness of the conceptual modeling aspects. It would not have been easy to obtain this variable without relying on the conceptual modeling process. Moreover, the choice of implementing the dimension level All results in a list of relations All.\*(All.region, All.year, etc.).

## 4.4. Discussion

To the best of our knowledge, very few detailed data warehouse design methods have been proposed to date. The most comprehensive method we have found is the one proposed in [21]. This method and ours have both adopted the OO paradigm (UML and OCL). They both encompass classical phases of design, development and implementation. However, they differ in the way of tackling abstraction levels: [21] merges logical and physical design phases whereas we propose to adapt the three ANSI/X3/SPARC abstraction levels to multidimensional modeling. Moreover, we consider that multidimensional concepts are not suitable for conceptual modeling. [21] provides a way of defining users' views (Business Models) which are not explicitly taken into account in our approach. Finally, [21] defines an ETL process which is not yet implemented in our method. Summing up, the contribution of this paper can be characterized as follows. We provide (1) a unified multidimensional metamodel, (2) a formalization of transformation rules between metamodels and (3) a high level of standardization based on the CWM proposal. Our method spans conceptual, logical and physical design. In particular, the same logical multidimensional schema may be implemented in different physical environments. Our method adopts a top-down approach starting from user requirements. However, it also considers operational data sources, in the data confrontation phase.

## 5. Conclusion and further research

We have described a comprehensive UML-based method for data warehouse design. Capitalizing on transactional database design techniques, we proposed a conceptual design phase aimed at defining a UML model, followed by an enrichment/transformation of this model. The resulting conceptual model is then mapped into a logical multidimensional schema, which may then be mapped into any physical MOLAP or ROLAP platform, as illustrated with the Oracle MOLAP environment. The content of the conceptual, logical and physical design phases was detailed by presenting the metamodels and the associated transformations. Our design method was applied to a case study.

Elaborating from previous research, we have defined a unified multidimensional metamodel. This metamodel is used to represent the logical multidimensional schema in our data warehouse design method. The physical data warehouse schema results from mapping this logical schema into a physical multidimensional (MOLAP) or relational (ROLAP) database schema. The resulting database is accessible not only to OLAP tools, but also to other decision support tools, e.g. data mining. Furthermore, although this perspective is outside the scope of the present paper, our unified multidimensional metamodel could be used in the context of MOLAP or ROLAP tools, in order to provide decision makers with a standard, high-level view to the data warehouse. The need for a unified, MOLAP and ROLAP-independent multidimensional formalism within OLAP tools is today widely acknowledged (the Unified Dimensional Model, included in the 2005 version of Microsoft SQL Server, is a recent example).

The transformations of our data warehouse design method may be semi-automated, more specifically in the logical and physical design phases. Human interaction is required to validate the step-by-step application of the transformations, or to provide information (this information concerns mainly the applicable aggregation functions during logical design, and the definition of data types during physical design). A CASE tool is under prototyping. The tool uses Java along with OMG's XMI standard (XML Metamodel Interchange) for the definition and storage of the logical multidimensional schema. Our CASE tool aims at supporting data warehouse designers, based on our method and on the quality metrics presented in [35].

Several questions remain open. The mapping transformations need to be enriched. The method has to be further tested on extensive case studies. Non-dataoriented requirements need to be handled; this can be achieved by exploiting the dynamic concepts of UML, e.g. sequence diagrams for the definition of OLAP operations such as rotate, pivot, slice or dice [21]. Lastly, the transformations could be formalized with CWM's Transformation package, with the aim of tracing mappings between the different design phases. We are currently working on these issues, as well as on the derivation of data marts from the data warehouse and the integration of ETL processes in the design phases.

## Acknowledgements

The authors are grateful to the reviewers for their useful and helpful comments.

## References

[1] A. Abello, J. Samos, F. Saltor, Benefits of an object-oriented multidimensional data model, ECOOP 2000 Symposium on Objects and Databases, Sophia-Antipolis, France, 2000 (June).

[2] R. Agrawal, A. Gupta, S. Sarawagi, Modeling multidimensional databases, 13th International Conference on Data Engineering (ICDE '97), Birmingham, UK, 1997 (April).

[3] J. Akoka, I. Comyn-Wattiau, N. Prat, Dimension hierarchies design from UML generalizations and aggregations, 20th International Conference on Conceptual Modeling (ER 2001), Yokohama, Japan, 2001 (Nov.).

[4] S. Arkhipenkov, D. Golubev, Oracle Express OLAP, Charles River Media, 2002.

[5] M. Blaschka, C. Sapia, G. Höfling, B. Dinter, Finding your way through multidimensional data models, DEXA Workshop on Data Warehouse Design and OLAP Technology (DWDOT '98), (Vienna, Austria), 1998 (Aug.).

[6] A. Bonifati, F. Cattaneo, S. Ceri, A. Fuggetta, S. Paraboschi, Designing data marts for data warehouses, ACM Transactions on Software Engineering and Methodology 10 (4) (2001 (Oct.)) 452–483.

[7] J.W. Buzydlowski, I.-Y. Song, L. Hassell, A framework for object-oriented on-line analytical processing, 1st ACM Workshop on Data warehousing and OLAP (DOLAP '98), (Washington DC, USA), 1998 (Nov.).

[8] L. Cabibbo, R. Torlone, A logical approach to multidimensional databases, 6th International Workshop on Extending Database Technology (EDBT '98), (Valencia, Spain), 1998, (March).

[9] L. Carneiro, A. Brayner, X-META: a methodology for data warehouse design with metadata management, 4th International Workshop on Design and Management of Data Warehouses (DMDW 2002), (Toronto, Canada), 2002 (May).

[10] S. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, SIGMOD Record 26 (1) (1997 (March)) 65–74.

[11] A. Datta, H. Thomas, The cube data model: a conceptual model and algebra for on-line analytical processing in data warehouses, Decision Support Systems 27 (3) (1999 (Dec.)) 289–301.

[12] S.R. Gardner, Building the data warehouse, Communications of the ACM 41 (9) (1998 (Sept.)) 52–60.

[13] M. Golfarelli, S. Rizzi, A methodological framework for data warehouse design, 1st ACM Workshop on Data Warehousing and OLAP (DOLAP '98), (Washington DC, USA), 1998 (Nov.).

[14] B. Hüsemann, J. Lechtenbörger, G. Vossen, Conceptual data warehouse design, 2nd International Workshop on Design and Management of Data Warehouses (DMDW 2000) (Stockholm, Sweden), 2000 (June).

[15] M. Jarke, M. Lenzerini, Y. Vassiliou, P. Vassiliadis, Fundamentals of Data Warehouses, second ed., Springer-Verlag, 2003. [16] R. Kimball, The Data Warehouse Toolkit, John Wiley & Sons, 1996.

[17] Klasse Objecten, OCL Checker, version 0.3, (Feb. 2001), http:/ www.klasse.nl/ocl/ocl-checker.html.

[19] W. Lehner, J. Albrecht, H. Wedekind, Normal forms for multidimensional databases, 10th International Conference on Statis tical and Scientific Database Management (SSDBM '98), (Capri, Italy), 1998 (July).

[20] H.-J. Lenz, A. Shoshani, Summarizability in OLAP and statistical data bases, 9th International Conference on Statistical and Scientific Database Management (SSDBM '97), (Olympia, Washington, USA), 1997 (Aug.).

[21] S. Luján-Mora, J. Trujillo, A comprehensive method for data warehouse design, 5th International Workshop on Design and Management of Data Warehouses (DMDW 2003), (Berlin, Germany), 2003 (Sept.).

[22] D.L. Moody, M.A.R. Kortink, From enterprise models to dimensional models: a methodology for data warehouse and data mart design, 2nd International Workshop on Design and Management of Data Warehouses (DMDW 2000), (Stockholm, Sweden), 2000 (June).

[23] T.B. Nguyen, A.M. Tjoa, R. Wagner, An object-oriented multidimensional data model for OLAP, 1st International Conference on Web-Age Information Management (WAIM), 2000.

[24] T. Niemi, J. Nummenmaa, P. Thanisch, Constructing OLAP cubes based on queries, 4th ACM Workshop on Data warehousing and OLAP (DOLAP '01), (Atlanta, USA), 2001 (Nov.).

[25] Object Management Group, OMG Modeling and Metadata Specifications, http://www.omg.org/technology/documents/modeling\_ spec\_catalog.htm.

[26] Y.-T. Park, An Empirical Investigation of the Effects of Data Warehousing on Decision Performance, Information and Management, in press (available online at www.sciencedirect.com, April 2005).

[27] T.B. Pedersen, C.S. Jensen, Multidimensional data modeling for complex data, 15th International Conference on Data Engineering (ICDE '99), (Sydney, Australia), 1999 (March).

[28] V. Peralta, R. Ruggia, Using design guidelines to improve data warehouse logical design, 5th International Workshop on Design and Management of Data Warehouses (DMDW 2003), (Berlin, Germany), 2003 (Sept.).

[29] C. Phipps, K.C. Davis, Automating data warehouse conceptual schema design and evaluation, 4th International Workshop on Design and Management of Data Warehouses (DMDW 2002), (Toronto, Canada), 2002 (May).

[30] N. Prat, J. Akoka, From UML to ROLAP Multidimensional Databases Using a Pivot Model, 18<sup>èmes</sup> Journées Bases de Données Avancées, (Evry, France, Oct. 2002), http://faculty. essec.fr/n.prat/BDA02\_Prat\_Akoka.pdf.

[31] M. Rafanelli, F. Ricci, Proposal of a logical model for statistical databases, 2nd International Workshop on Statistical Database Management (SSDBM '83), (Los Altos, California), 1983 (Sept.).

[32] C. Sapia, M. Blaschka, G. Höfling, B. Dinter, Extending the E/R Model for the multidimensional paradigm, International Workshop on Data Warehousing and Data Mining (DWDM '98) in conjunction with the 17th Int. Conf. on Conceptual Modeling (ER '98), (Singapore), 1998 (Nov.).

[33] Z. Shi, Y. Huang, Q. He, L. Xu, S. Liu, L. Qin, Z. Jia, J. Li, H. Huang, L. Zhao, MSMiner – A Developing Platform for OLAP, Decision Support Systems, in press (available online at www. sciencedirect.com, Dec. 2004).

[34] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002 (June)) 111–126.

[35] S. Si-Saïd Cherfi, N. Prat, Multidimensional schemas quality: assessing and balancing analyzability and simplicity, International Workshop on Conceptual Modeling Quality (IWCMQ '03) in conjunction with the 22nd International Conference on Conceptual Modeling (ER '03), (Chicago, Illinois, USA), 2003 (Oct.).

[36] The OLAP Report – Market share analysis, (2005), http://www. olapreport.com/Market.htm.

[37] N. Tryfona, F. Busborg, J.B. Christiansen, starER: a conceptual model for data warehouse design, 2nd ACM Workshop on Data Warehousing and OLAP (DOLAP '99), (Kansas City, USA), 1999 (Nov.).

[38] A. Tsois, N. Karayannidis, T. Sellis, MAC: conceptual data modeling for OLAP, 3rd International Workshop on Design and Management of Data Warehouses (DMDW 2001), (Interlaken, Switzerland), 2001 (June).

[39] P. Vassiliadis, T. Sellis, A survey of logical models for OLAP databases, SIGMOD Record 28 (4) (1999 (Dec.)) 64–69.

[40] H.J. Watson, C. Fuller, T. Ariyachandra, Data warehouse governance: best practices at Blue Cross and Blue Shield of North Carolina, Decision Support Systems 38 (3) (2004 (Dec.)) 435–450.

Nicolas Prat holds a PhD in Information Systems from the University of Paris 9 and is an alumnus from ESSEC Graduate School of Business Administration. He is currently Assistant Professor of Information Systems at ESSEC Business School. His research and publication areas include information systems design, DSS, data warehouses, knowledge management and case-based reasoning.

Jacky Akoka received an M.S. degree in Computer Science and the Doctoral degree in Operations Research from the University of Paris 6, and a PhD degree in Management Information Systems from the Sloan School of Management at MIT. He is currently Professor of Information Systems and holds the Chair of Information Systems at the Conservatoire National des Arts et Métiers in Paris. He has published over 120 conference and journal papers on information and decision systems, including in the DSS journal. His research interests include information systems methodologies, DSS and data warehouse design and implementation

Isabelle Comyn-Wattiau received an Engineer Degree in Computer Science from the Institut d'Informatique d'Entreprise in Paris, an M.S. and a PhD degree in Computer Science from the University of Paris 6. She is currently Professor of Information and Computer Systems at the Conservatoire National des Arts et Métiers in Paris. She has published more than 70 journal and conference papers on information and database systems. Her research interests include information systems design, data warehouse design and database integration.
