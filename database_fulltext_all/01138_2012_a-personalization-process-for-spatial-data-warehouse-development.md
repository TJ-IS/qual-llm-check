---
otero_id: 1138
otero_key: "CSA28DC3"
title: "A personalization process for spatial data warehouse development"
authors: "Octavio Glorio; Jose-Norberto Mazón; Irene Garrigós; Juan Trujillo"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.11.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A personalization process for spatial data warehouse development

Octavio Glorio ⁎, Jose-Norberto Mazón, Irene Garrigós, Juan Trujillo

Lucentia Research Group, Department of Software and Computing Systems, University of Alicante, PO BOX 99 E-03080, Alicante, Spain

a r t i c l e i n f o

Available online 22 December 2011

Keywords: Spatial data warehouse Geographic information Personalization

## a b s t r a c t

Spatial data warehouses (SDW) rely on extended multidimensional (MD) models in order to provide decision makers with appropriate structures to intuitively explore spatial data by using different analysis techniques such as OLAP (On-Line Analytical Processing) or data mining. Current development approaches are focused on de<sup>fi</sup>ning a unique and static Spatial multidimensional (SMD) schema at the conceptual level over which all decision makers ful<sup>fi</sup>ll their current spatial information needs. However, considering the required spatiality for each decision maker is likely to derive in a potentially misleading SMD schema (even if a departmental DW or data mart is being de<sup>fi</sup>ned). Furthermore, spatial needs of each decision maker could change over time or depending on the context, thus requiring the SMD schema to be continuously updated with changes that can hamper decision making. Therefore, if a unique and static SMD schema is designed, acquiring the required spatial information is more costly than expected for decision makers and they may get frustrated during the analysis. To overcome these drawbacks, we argue for considering spatiality as a personalization feature within a formal design process. In this way, each decision maker will be able to access its own personalized SMD schema with its required spatial structures and instances, suitable to be properly analyzed at a glance. Our approach considers several novel artifacts: (i) a UML pro<sup>fi</sup>le for spatial multidimensional modeling at the conceptual level, (ii) a spatial-aware user model in order to de<sup>fi</sup>ne decision maker pro<sup>fi</sup>le; and (iii) a spatial personalization language to de<sup>fi</sup>ne spatial needs of decision makers as personalization rules. The de<sup>fi</sup>nition of personalized SMD schemas by using these artifacts is formally de<sup>fi</sup>ned using the Software Process Engineering Metamodel Speci<sup>fi</sup>cation (SPEM) standard. Finally, the applicability of our approach is shown through a running example based on our Eclipse-based tool for SDW development. © 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Data warehouses (DW) are at the core of BI (Business Intelligence) systems, since they provide adequate mechanisms for storing huge quantities of data from many heterogeneous data sources. Therefore, DW systems must structure data to be intuitive for decision makers to interactively analyze them by means of different techniques, such as OLAP (On-Line Analytical Processing) or data mining, thus achieving their information needs. To do so, DW development is based on a conceptual multidimensional (MD) model in order to organize data into facts (containing the measures of the analysis) and dimensions (containing the contexts of analysis).

Interestingly, data analysis over MD modeling is often concerned with spatiality, e.g. by means of spatial data structures, such as location dimensions [18] or novel OLAP operators that consider spatiality, such as spatial intersection [27]. Therefore, MD modeling must be extended in order to consider spatiality in DWs. These spatial data warehouses (SDW) are useful for improving the decision making process for many reasons, among which: (i) they allow users to relate different MD elements by using their geometries (e.g. clients near a store), (ii) they allow users to relate MD information of a certain domain with spatial information external to it (e.g. stores near a metro station), and (iii) they could represent more complex measures as a collection of geometries (e.g. a spatial measure describing a geometric collection of pollution clouds). It is worth noting that in this paper, we have considered spatial data as those representing geometric characteristics of real world phenomena by an absolute and relative position, an associated geometry and some descriptive attributes<sup>1</sup> (e.g. rivers described by line geometries in UTM<sup>2</sup> coordinate system and with a measure of associated water level).

Current SDW development approaches rely on extended MD models in order to obtain a unique and static spatial MD (SMD) schema at the conceptual level, over which all decision makers intuitively ful<sup>fi</sup>ll their spatial information needs (see Section 2 for further details). However, considering required spatiality for all decision makers in just one SMD schema could be potentially misleading (even if a departmental DW or data mart is being de<sup>fi</sup>ned). This unique SMD schema may be quite large as it should support many kinds of decision makers who may each have different needs [29]. For example, within the same sales department, several decision makers have different geographic requirements: if they are concerned about pharmaceutical product promotion, then they need both the location of chain stores and hospitals, while if they are concerned about delivery promotions they need geographic locations of chain stores and customers' addresses. It is worth noting that considering all these requirements in a unique SMD schema hinders a single decision maker from carrying out a proper data analysis due to the complexity of MD spatial structures and operators. Furthermore, individual spatial needs of each decision maker could change over time or depending on the context, thus requiring the SMD schema to be properly adapted without affecting the other decision makers (e.g., one decision maker is interested in spatial data about stores and customers to further analyze location of sales, while the others only need the “alphanumeric” name of the location to aggregate sales by location in a simpler manner).

Consequently, if a unique and static SMD schema is designed, then (i) decision makers are forced to understand and navigate along the whole complex SMD schema to <sup>fi</sup>nd and acquire adequate spatial data which may be a costly and frustrating task; and (ii) SMD schema may suffer from unforeseeable changes which are useful for some decision makers and harmful for others. Even if a departmental data warehouse (also known as data mart) is developed to improve this situation, spatial structures in a data mart would still be too complex.<sup>3</sup>

To overcome these drawbacks, we argue that spatiality should be considered as a convenient feature to personalize in MD modeling. In this way, a unique and static MD schema should be personalized in order to provide spatial versions of the original DW for every particular decision maker, thus better satisfying each of them. To start tackling this task, in the short version of this paper [13] we presented a modeling approach for spatial personalization of MD conceptual models by providing: (i) a UML pro<sup>fi</sup>le for spatial MD modeling; (ii) a spatial-aware user model that captures all the decision maker information needed to be personalized; and (iii) a spatial personalization rule language called SPRML (Spatial Personalization Rules Modeling Language) that is used to specify the required personalization actions. SPRML is an extension of PRML (Personalization Rules Modeling Language) [7] which is a high level rule-based language that has been successfully applied to the development of several Web personalized systems. PRML has been extended in order to support spatiality as explained in Section 6.

These new artifacts allow users to spatially personalize the multidimensional model, obtaining spatial multidimensional models tailored to each decision maker. Fig. 1 shows a schema of our process describing how all the artifacts work together. It starts by de<sup>fi</sup>ning a spatial-aware user model, a common static multidimensional model and a set of spatial personalization rules. Then, a Rule Interpreter executes personalization rules for each user and multidimensional schemas resulting in different personalized schemas. Finally, these models are transformed by a Code Generator [10] in spatial database code and spatial OLAP (SOLAP) metadata. The resulting personalized schemas make the analysis easier for each decision maker, since they only contain the required spatial multidimensional structures and instances, and the number of required spatial operations is therefore lower than using a unique spatial schema for all users. Interestingly, this process could also be executed on runtime over the personalized schemas in order to properly adapt it for one decision maker without affecting the others. Considering that both designtime and runtime executions make the process complex, so it has been formalized by means of the Software Process Engineering

Metamodel (SPEM) [26]: an OMG standard useful for describing a software development process or a family of related software development processes.

Therefore, in this paper, we extend the short version [13] as follows: (i) we provide a SPEM-based formal description of our process for SDW development by using spatial personalization over MD schemas, (ii) the case study has been improved to better show the applicability of our approach, with more details that clarify how to use our approach in real world scenarios; and <sup>fi</sup>nally, (iii) further details about implementation of our approach have been included.

The remainder of this paper is structured as follows. Related work is reviewed next. Section 3 presents a running example to back up our approach, and useful background about our previous research in SMD modeling is described in Section 4. Then, Section 5 presents our process for SDW development by using spatial personalization. In Section 6, we present the new modeling artifacts, while a sample application of the developed process over the running example is described in Section 7. Section 8 presents some speci<sup>fi</sup>c details about the implementation of our approach. Finally, conclusions are presented in Section 9 together with a summary of our expected future works.

## 2. Related work

There are many works on the subject of conceptual modeling of SDW systems, some of the most well-known approaches are listed hereafter. Bimonte et al. [28] proposed a multidimensional model (GeoCube) which integrates geographic information and ensures correct aggregation over this kind of measures. Then, they presented GeWOlap [2], an extended model that supports a Web implementation of spatial OLAP tools. Finally, in [1], they propose the extension of the traditional spatial dimensions to support complex map navigation.

Gomez et al. also de<sup>fi</sup>ne a formal model for representing spatial data [14] and an analysis tool for MD models named Piet [6]. Malinowski and Zimanyi have integrated spatial dimensions, measures, facts and levels in one concise model supported by a diagram editor named MADS [17]. Also, they introduce into this model some topological types in order to spatially describe different hierarchies. Then, in [19], they provide some guidelines to obtain implementations of SDW by using MADS for modeling. Vaisman and Zimányi have <sup>fi</sup>nally presented the integration of certain complex data in their modeling methodologies, these were the temporal [33] and continuous <sup>fi</sup>eld [32] data types.

Fidalgo et al. [5] proposed a formal model named GeoDWFrame for guiding the design of a Geographical Data Warehouse (GDW). Then, some extensions were made to this framework by the authors where a formal metamodel for GDW is de<sup>fi</sup>ned [31] and a set of aggregation functions for spatial measures were developed [3]. Finally, they presented a geographic and multidimensional data cube metamodel and a query language named GeoMDQL [4], which allows simultaneous usage of both multidimensional and spatial operators.

In [9], we have proposed a framework for SDW development aligned with the Model Driven Architecture standard (MDA) [23]. Then, in [10], we have added some geographic elements and algebra to this framework in order to introduce geographic information external to the domain. Finally, in [12], we have combined the spatial multidimensional analysis with data mining techniques at conceptual and logical levels.

After having reviewed current state-of-the-art SDW developments, one common characteristic arises: they rely on extended MD models in order to obtain a unique and static SDW schema at the conceptual level, over which all decision makers intuitively ful<sup>fi</sup>ll their spatial information needs. Unfortunately, considering required spatiality for all decision makers in just one SMD schema could make it potentially large and spatial structures could become increasingly too complex to be analyzed at a glance. The main drawback of current approaches for designing SDWs is that they do not consider mechanisms that allow to adequately present the correct spatial information required for each decision maker. Therefore, we argue that spatiality should be considered as a convenient feature to personalize in SMD modeling. In this way, a generic MD schema should be personalized in order to provide spatial versions of the original DW for every particular decision maker, thus better satisfying each of them.

![](/api/attachments/CSA28DC3/fulltext/images/1745eeef1e11cf9041d41c4d9807794d3e310c65359aeb4b837549bc6799f699.jpg)  
Fig. 1. Our approach to spatial personalization multidimensional models.

## 3. A motivating example

In order to back up our approach, we de<sup>fi</sup>ne the following sample scenario: two different departments of a chain of supermarkets are interested in meeting certain analysis requirements for decision support. The Sales Department is interested in analyzing two different promotions, one for delivery and the other for pharmaceutical products, while the Human Resources Department is interested in analyzing employee productivity.

For the delivery promotions, the decision maker needs to analyze the sales to customers living near the store. Therefore, he/she requires the spatial description of customers' addresses and store locations. For the pharmaceutical product promotions, the decision maker wishes to analyze the sales of pharmaceutical products in chain stores near any hospital. Therefore, he/she requires the spatial description of hospital and store locations. On the other hand, the decision maker in the Human Resources Department wishes to analyze the productivity of employees related to the transportation details between work and home. Initially, he/she requires the spatial description of employees' home, subway stations and store location. He/she may also be interested in other public transportation facilities such as bus stations.

Initially, decision makers in the Sales Department were interested in analyzing who bought (Customer), where (Store), what (Product) and when (Time). Whereas, the Human Resources Department was interested in analyzing who sold (Employee), where (Store), cost (Sales) and when (Time). Therefore, both unique MD schemas of the company have to be modi<sup>fi</sup>ed according to the new spatial requirements of every decision maker, as stated above. Importantly, after the required modi<sup>fi</sup>cations to the Sales Department data mart are carried out, the resulting model could become complex and dif<sup>fi</sup>cult to analyze for decision makers which are not concerned with all the spatial needs. On the other hand, after doing the required modi<sup>fi</sup>cations to the Human Resources Department data mart, the resulting spatial model is no longer of any use to the rest of decision makers in this department.

To overcome these drawbacks, we present throughout this paper a spatial personalization process to adapt MD models to the speci<sup>fi</sup>c spatial necessities of decision makers. In this way, spatiality is considered as a personalization feature: e.g. although a unique MD model is considered for both decision makers in the Sales Department, each of them will be able to achieve his/her spatial requirements without affecting each other. Also, the spatiality of the decision maker in the Human Resources Department is tracked in order to adapt the MD model to his/her spatial necessities, at the same time that the underlying MD model remains useful to the rest of the decision makers within the same department.

## 4. Background on spatial multidimensional modeling

In this section, we outline our previous approach for spatial MD modeling at the conceptual level, and we also exemplify its use by means of the aforementioned motivating example.

Our spatial MD modeling approach is speci<sup>fi</sup>cally based on three different UML pro<sup>fi</sup>les: (i) one for MD modeling presented in [16], (ii) another one for spatial multidimensional levels and measures modeling presented in [9], and (iii) a last one for geographic information modeling presented in [12]. Furthermore, we have also added a new modeling element to the previous pro<sup>fi</sup>le set, that is the ≪PersonalizedStarPackage≫ stereotype. This element allows users to keep resulting personalization details (e.g., the user id) in the MD schemas. An overview of our <sup>fi</sup>nal UML pro<sup>fi</sup>le is given in Fig. 2 and we refer readers to our previous works for more details [9,12,16].

Multidimensional models for our motivating example are shown in Fig. 3 for the Sales Department and Fig. 4 for the Human Resources Department. They correspond to an early multidimensional model common to all users in the same department and without spatial elements. Sales are represented as a Fact class ( ) and the contexts of analysis are represented as Dimension classes ( ). Measures for Fact classes (i.e., UnitSales, StoreCost, and so on) are represented as FactAttributes ( ). With respect to dimensions, each level of a dimension hierarchy is speci<sup>fi</sup>ed by a Base class. Every Base class ( ) contains a number of descriptive attributes ( ). Associations between pairs of Base classes ( ) represent aggregation paths.

MD schemas in Figs. 3 and 4 require to be personalized to obtain SMD schemas useful for decision makers to achieve their spatial information requirements. The de<sup>fi</sup>nition of a personalized SMD schemas requires several new modeling artifacts, described in Section 6 and which are de-<sup>fi</sup>ned upon our UML pro<sup>fi</sup>le for spatial MD modeling [9], namely (i) the Spatial-aware USer model (SUS) that captures all the decision maker information needed to be personalized; and (ii) the Spatial Personalization Rule Modeling Language (SPRML) that is used to specify the required personalization actions. These new artifacts allow users to spatially personalize the multidimensional model obtaining spatial multidimensional models tailored to each decision maker.

## 5. A personalized spatial data warehouse development process

Our personalization process for SDW development was informally introduced in Fig. 1. However, this process could also be executed on runtime over the personalized schemas in order to properly adapt it for one decision maker. As previously mentioned, considering both design-time and runtime executions make the process complex, so it has been formalized by using SPEM. This metamodel is useful for describing a software development process or a family of related software development processes. Therefore, it is appropriate to describe our approach in its entirety.

![](/api/attachments/CSA28DC3/fulltext/images/d79e01a4a44414ddd175ddc834d8c96e73e5af1a33c9e6b9b2e1dc1e5a35774d.jpg)  
Fig. 2. UML pro<sup>fi</sup>le for spatial data warehouse modeling.

SPEM is based on the idea that a software development process is a collaboration between active entities called ProcessRole ( ), which perform operations called Activity ( ), on concrete and real entities called WorkProduct ( ). A concrete generalization of the work product concept exists for UML models represented by . Each role interacts or collaborates by exchanging work products and triggering the execution of activities. The overall goal of a process is to bring a set of work products to a well-de<sup>fi</sup>ned state. In order to encourage the modeling of a complex process, it is possible to split it in different parts called Phase ( ) and further break them down into a set of sub-phases called WorkDefinition $( ^ { \dag } { } ^ { \dag } { } ^ { \dag } )$

Nevertheless, a SPEM role represents an active entity and some MDA artifacts do not <sup>fi</sup>t in such a description. Therefore, we have extended the SPEM metamodel in order to represent a role executed by an automatic entity such as a grammar interpreter or a transformation engine. We have called the new element AutomaticRole ( ) and it has been implemented as a generalization of the ProcessRole element. Fig. 5 shows a portion of the SPEM metamodel showing our extension.

![](/api/attachments/CSA28DC3/fulltext/images/8f899cce95e846f9edcd1ea5b08100a02ea6c09354d9052520bddbfe107f57f4.jpg)  
Fig. 3. MD data mart for the Sales Department.

![](/api/attachments/CSA28DC3/fulltext/images/30d08e468a8f8f76decc50c9705b84e88a3e50ac8e70408a2be1a30aa9ffcf9a.jpg)  
Fig. 4. MD data mart for the Human Resources Department.

SPEM standard also includes a pro<sup>fi</sup>le that de<sup>fi</sup>nes stereotypes for UML2 Superstructure model elements for almost every metamodel concept that can be represented in UML2 diagrams in a meaningful way (Fig. 6 shows the speci<sup>fi</sup>c iconography). Speci<sup>fi</sup>cally, we have selected two behavior diagrams that depict different behavioral features of our process, those are Use-Case and Activity diagrams. The Use-Case diagram has been used to represent the <sup>fi</sup>rst breakdown of our process in two main parts, one corresponding to the development at design-time and another at runtime. Then, Activity diagrams have been used to specify further details for each of these parts.

Consequently, Fig. 7 shows the UML Use-Case diagram that describes the <sup>fi</sup>rst breakdown of our process. It shows the main phase (stereotyped as Phase ) called Personalized Spatial Data Warehouse Development that is broken down into two sub-phases (stereotyped as ≪WorkDefinition≫). Those are called Design-time Personalization and Runtime Personalization. The <sup>fi</sup>rst one occurs when the designer executes the process for designing the SDW for the <sup>fi</sup>rst time. The second one occurs when the user makes use of the SDW and triggers some actions with his/her behavior and some updates are performed. Therefore, design-time process is strictly required but the runtime process might never be triggered. Therefore, the relationships among the above elements are respectively stereotyped as ≪mandatory≫ and ≪optional≫.

The breakdown is not over, in fact, each sub-phase of Fig. 7 can be broken down in turn into a set of correlated activities, modeled as ≪Activity≫ stereotyped instances with an associated responsible actor. The following subsections give an in-depth presentation of the two sub-phases of our approach by using UML Activity diagrams.

## 5.1. 1. Design time personalization sub-phase

This sub-phase corresponds to the designer development process. It is modeled by a ≪WorkDefinition≫ stereotyped element named Design-time Personalization (shown in Fig. 7). The breakdown of this package element is shown in the UML Activity diagram of Fig. 8. There, are shown three different actors stereotyped as ≪Process-Role≫: the Designer, the SPRML Engine, the Code Generator. The SPRML Engine is the interpreter of our spatial personalization approach (see Sections 6 and 7).

The Designer starts de<sup>fi</sup>ning different models: a non spatial multidimensional model common to all the users (see Section 3), a spatialaware user model (see Section 1) and a set of SPRML rules (described in Section 7). These tasks correspond to classes stereotyped respectively as ≪Activity≫ and called Design Multidimensional Model, Design User Model and Design Personalization Rules.

![](/api/attachments/CSA28DC3/fulltext/images/9d61ec2dcb9fe1df874a5f1140dca1f9bb7a45db05367e73603dca3c01e112d9.jpg)  
Fig. 5. A portion of SPEM metamodel showing the new element AutomaticRole.

![](/api/attachments/CSA28DC3/fulltext/images/8d607f4a3a22944c41612627c6ea649385e0bf84d92ccd2153d3546ecefaee53.jpg)  
Fig. 6. Main SPEM stereotype icons used.

Then, when the SchemaDesign event is triggered, the SPRML Engine executes the rules that modi<sup>fi</sup>ed the multidimensional schema for every user and needs. The resultant output is a set of spatial multidimensional models personalized for every user called Schema Personalized SMD Models. However, the desire instances have not been selected yet. Therefore, when the InstancesDesign event is triggered, the SPRML Engine executes the instance rules and an OCL <sup>fi</sup>lter is added to every spatial multidimensional model. Finally, the Code Generator derivates the required code and metadata to accomplish an implementation by using the <sup>fi</sup>nal models called Instances Personalized SMD Models.

## 5.2. 2. Runtime personalization sub-phase

This sub-phase is the response of the evolution of the system depending on the user behavior. It is also modeled by ≪WorkDefinition≫ stereotyped element named Runtime Personalization (shown in Fig. 7). The breakdown of this package element is shown in the UML Activity diagram of Fig. 9. There, are shown three different actors stereotyped as ProcessRole : the User, the SPRML Engine, the Code Generator.

The behavior of the User while using the system could generate an SPRML event that could trigger an adaptation of the SDW on runtime. Speci<sup>fi</sup>cally, the tracked event is called SpatialSelection event and is de-<sup>fi</sup>ned in Section 1. On the other hand, the speci<sup>fi</sup>c behavior that generates the above event is de<sup>fi</sup>ned in the user model presented in Section 1.

Then, when the SpatialSelection event is triggered, the SPRML Engine executes the rules that modi<sup>fi</sup>ed the spatial multidimensional schema for a speci<sup>fi</sup>c user. The resultant output is a new spatial multidimensional model personalized for that user called Updated Personalized SMD Model. Finally, when SessionEnd is triggered by the user, the Code Generator derivates the required updates to accomplish a new updated implementation with some speci<sup>fi</sup>c modi<sup>fi</sup>cations to cover a precise user need without affecting other users' schemas.

## 6. Spatial personalization modeling

Spatial Personalization can be in<sup>fl</sup>uenced by several factors [8]. Hence, our proposal considers (i) user-specific characteristics (irrespective of the domain), (ii) spatial user-behavior in order to derive the preferences or interest on different elements of the system, taking into account the user behavior, and (iii) the changing spatial user-context in order to de<sup>fi</sup>ne personalization strategies. The structure of the data required for personalization is speci<sup>fi</sup>ed in a user model. This model has been de<sup>fi</sup>ned as a class diagram by means of a UML pro<sup>fi</sup>le named SUS (Spatial-aware USer model), as will be explained throughout the next sections. On the other hand, we can consider two different types of spatial personalization actions. Personalization can be applied over the schema of the DW (e.g., adding spatiallity to a level if it is required), and it can also be applied over the instance of the SDW (e.g., selecting certain fact instances according to a geographic condition).

As explained in Section 1, we extended the PRML [7] (Personalization Rules Modeling Language) language in order to support spatiality. PRML is a rule-based high level language created to specify personalization upon Web applications. PRML is based on a MOF (Meta Object Facility) metamodel [24] and could be extended. Indeed, in [8], we have adapted it to peculiarities of OLAP systems such as complex operations required to analyze data. Now, in this work we have adapted the PRML language to the peculiarities of SDW systems becoming SPRML (Spatial Personalization Rules Modeling Language), as will be explained throughout this section. It is important to notice that spatial personalization has been considered to occur at two different moments: (i) at design-time (when the system is designed according to users' requirements), and (ii) at runtime (personalization actions are triggered depending on user behavior).

Therefore, two new artifacts have to be de<sup>fi</sup>ned to be able to properly personalize MD schemas: (i) the Spatial-aware USer model (SUS) that captures all the decision maker information needed to be personalized; and (ii) the Spatial Personalization Rule Modeling Language (SPRML) that is used to specify the required personalization actions. In the following subsections, each of these two new artifacts is described in detail.

## 6.1. 1. Spatial-aware user model

Personalization is a user-centered process, therefore, user modeling is the basis for personalization support [15]. In order to provide personalized spatial data warehouses, relevant knowledge about the decision maker should be captured. The structure of the data required for personalization is speci<sup>fi</sup>ed in the user model. This model should be de<sup>fi</sup>ned based on the personalization requirements we want to support in a concrete system. The information speci<sup>fi</sup>ed in the user model builds the user profile and will be updated during the lifetime of the system. The information stored in the user model typically contains data related to the user (e.g., user characteristics like age or role) and may also contain information related to the domain (e.g., preferences over data). Therefore, based on [8], we have considered the following criteria in order to take into consideration the spatial data on data warehouses:

User-specific characteristic. It refers to information, irrespective of the domain, that is directly related to the description of the decision maker. Typical characteristics are the user language or the speci<sup>fi</sup>c department that he/she belongs to.

![](/api/attachments/CSA28DC3/fulltext/images/77cbed5f0da9c75760c7d266c128a31f019b6a5622c176bf99618fb5eaf6ee43.jpg)  
Fig. 7. Use-case diagram of the development process: relationships between main phase (left) and work de<sup>fi</sup>nitions expressing sub-phases (right).

![](/api/attachments/CSA28DC3/fulltext/images/0a099a3c6b16b9b359d0cfaaefd84757e4173441c19ecf713019ce526d25d2b8.jpg)  
Fig. 8. Activity diagram of the Design Time sub-phase

Spatial user-context. This information characterizes the changing environment that surrounds the user analysis. Speci<sup>fi</sup>cally, it refers to information relative to the geographical location of the context of analysis. For example, a user may only need sales made in stores less than 5 km away from his/her assigned region. Therefore, his/ her assigned location is required to cover that analysis requirement.

Spatial user-behavior. We can track the user spatial behavior in the system and infer the interest or preferences he/she has on certain elements. For this purpose we store information about the spatial operations performed by the decision maker. For example, if the user is usually interested in employees whose home-store subway connection is less than 5 km, maybe he/she could also be interested in employees whose home-store bus connection is less than 3 km. To cope with this requirement, the <sup>fi</sup>rst step is to gather this speci<sup>fi</sup>c user interest in such instances.

The user model is represented by means of a UML pro<sup>fi</sup>le in a class diagram. Several stereotypes have been de<sup>fi</sup>ned in this UML pro<sup>fi</sup>le as shown in Fig. 10. The different criteria considered in the user model are de<sup>fi</sup>ned as an extension of the UML class and property concepts. Different stereotypes for representing the different types of criteria have been de<sup>fi</sup>ned: (i) ≪Characteristic≫ and ≪AnalysisRole≫ stereotype for user-speci<sup>fi</sup>c characteristics, (ii) ≪ SpatialSelection≫ stereotype for spatial user-behavior, and (iii) ≪LocationContext≫ stereotype for spatial user-context. The user and the session are also de<sup>fi</sup>ned extending the UML class concept by the ≪User≫ and ≪Session≫ stereotypes. Finally, all the allowed geometric primitives, similar to spatial multidimensional model presented in Section 3, are grouped in the GeometricTypes element.

![](/api/attachments/CSA28DC3/fulltext/images/a3ccf0c8a6f2bd78fa5dfe3c8f867e0fac5ed6196de7175439389bbcdbd32377.jpg)  
Fig. 9. Activity diagram of the Runtime Personalization sub-phase

![](/api/attachments/CSA28DC3/fulltext/images/71dfb9514a11ff64d8a0f6ff0168f8500c194c19fd17a8592dc4ad5109c7f245.jpg)  
Fig. 10. UML pro<sup>fi</sup>le for the spatial-aware user model.

The ≪AnalysisRole≫ stereotype is a generalization of the ≪Characteristic≫ one. It represents a precise characteristic that describes the speci<sup>fi</sup>c analysis role of the user. For example, a Sales Department is interested in analyzing two different promotions, one for delivery and another one for pharmaceutical products. Each of these promotions requires a set of speci<sup>fi</sup>c personalization actions. However, the Sales Department analyst is a common user. Therefore the different user analysis roles have to be stored.

The ≪SpatialSelection≫ stereotype has a selection attribute that stores the speci<sup>fi</sup>c spatial expression that needs to be tracked and written using SPRML (see Section 2). For example, this attribute will de<sup>fi</sup>ne a spatial expression selecting customers living less than 2 km away from the chain store. This tracking task also requires for a ≪Session≫ stereotype to be present in order to listen to the start and end of the session. Finally, the ≪LocationContext≫ stereotyped has a geometry attribute that describes the speci<sup>fi</sup>c geometry of the context, for example a rectangle that describes the region in which a promotion could be available.

A sample of a spatial-aware user model de<sup>fi</sup>ned for the motivating example (see Section 3) is shown in Fig. 11 and the respective instance for each user in Fig. 12. As mentioned previously, in the last model we store different information needed to ful<sup>fi</sup>ll the personalization requirements initially speci<sup>fi</sup>ed for the SDW. There, we have represented the two different users, stereotyped as ≪User≫, one corresponding to the decision maker involved in promotions and the other one involved in human resources. We also have three different needs based on different analysis roles stereotyped as ≪Analysis-Role . Two of them are for the promotion decision maker, one for the delivery analysis and the other one for pharmaceutical products analysis and the last one is for the human resources decision maker.

The user model also describes the language of both users by using the ≪Characteristic≫ stereotype in order to allow a possible personalization of the interface. For the human resources user, we have added ≪ SpatialSelection ≫ and ≪Session≫ stereotyped elements, in order to track the user interest in employee's subway transportation details between work and home. Finally, for the promotion decision maker, we have added a ≪LocationContext≫ stereotyped element, in order to select only the stores in the region where the promotions must apply.

![](/api/attachments/CSA28DC3/fulltext/images/78cb14d13d93871f398fdf74ad842fac552f6fb507458f13437136c2a03bb6e6.jpg)  
Fig. 11. Spatial aware user model for the motivating example.

![](/api/attachments/CSA28DC3/fulltext/images/9d3973cabeed640ea8c13cecabf5a6a275f360f9d6e6870cb8dead48f4b48acb.jpg)  
Fig. 12. Spatial aware user model instances for the motivating example.

## 6.2. Spatial personalization model

After specifying the structure of the data needed for personalization, the designer should de<sup>fi</sup>ne a set of personalization rules to apply to the SDW system. The rules express the following: when an Event is triggered if a Condition is fulfilled an Action is performed.

Fig. 13 shows (an excerpt of) the PRML metamodel language adapted for SDW systems and named SPRML (Spatial Personalization Rule Modeling Language). It is described by a UML-like model, gray elements are the new spatial elements added and white ones correspond to the original PRML metamodel. This <sup>fi</sup>gure de<sup>fi</sup>nes the set of constructs of the language such as the different parts that form a SPRML rule and the different events, actions and expressions supported. It is worth noting that the SPRML metamodel can be extended if a new kind of element is detected. The main element of the metamodel is the Rule metaclass which represents the concept of rule containing the elements that de<sup>fi</sup>ne it. The elements de<sup>fi</sup>ning a rule are the ones that represent its main structure and are explained along the following subsections.

## 6.2.1. Tracking events

There are two different types of events, the design-time ones and the runtime ones. At design-time, we have de<sup>fi</sup>ned the SchemaDesign and InstancesDesign events. On the other hand, at runtime, we have de<sup>fi</sup>ned the SpatialSelection event and some events related to the analysis session, i.e. SessionStart event is triggered when the session is initiated by the user, whereas the SessionEnd event indicates the end of that session.

6.2.1.1. SchemaDesign. This event is triggered when the designer starts the development of the spatial schema of the data warehouse. Therefore, all the rules associated with this event make the required changes in the multidimensional structure for every user.

6.2.1.2. InstancesDesign. This event is triggered when the designer starts the spatial <sup>fi</sup>ltering of the required instances of the spatial data warehouse. Therefore, all the rules associated with this event build and store the required spatial <sup>fi</sup>lter in the spatial multidimensional structure for every user.

6.2.1.3. SpatialSelection. This event is triggered when the user satis<sup>fi</sup>ed a spatial expression (SpatialExp) and some speci<sup>fi</sup>c instances are selected (by using the SelectInstance action). Therefore, this method has two parameters, the SMD element selected and the spatial expression. It is used to track the user interest in certain instances and if the interest exceeds a threshold some actions could be taken (e.g., add other related instances).

## 6.2.2. Rule conditions

When specifying conditions, SPRML rules can refer to different elements of the conceptual models in order to de<sup>fi</sup>ne condition expressions. As already explained, personalization is mainly based on the user model information. A mechanism to access the user model structures is needed. To access a certain element of a model, SPRML navigates over the model using path expressions (PathExp). These expressions are based on the path expressions de<sup>fi</sup>ned in OCL [25]. The PathExp to access information de<sup>fi</sup>ned in the spatial-aware user model always contains the pre<sup>fi</sup>x “SUS” and the source concept is always the User class. As an example for a PathExp over the user model de<sup>fi</sup>ned in Fig. 12, consider that we want to access the language of the decision maker. The expression would be SUS.DecisionMaker. Language. Furthermore, an SPRML rule can also refer to information from the multidimensional model for specifying some needed conditions to de<sup>fi</sup>ne personalization actions. In the same way, in the personalization actions we may need to refer to an element of the multidimensional model to be modi<sup>fi</sup>ed. In this case the PathExp contains the “MD” pre<sup>fi</sup>x and the source concept of the PathExp is always the Fact class we want to access. In this case, to navigate through the model elements we go over the Base classes and Descriptor attributes of the multidimensional model, for instance, to refer to the name on the State we use MD.Sale.Store.State.name. Otherwise, if we want to de<sup>fi</sup>ne a rule using a new spatial element added to the multidimensional model, we use the pre<sup>fi</sup>x “SMD” referring to a spatial multidimensional schema. For example, if we want to access the geometric description of the Store we use SMD.Sale.Store.geometry.

## 6.2.3. Spatial expressions

Once all the elements can be accessed, the condition expressions have to be de<sup>fi</sup>ned. PRML initially considered logical operators, therefore, we have added some new operators to the original metamodel in order to de<sup>fi</sup>ne spatial expressions. These new operators are a subset of spatial methods of the OGC [22] standard.<sup>4</sup> Speci<sup>fi</sup>cally, there are two kinds of methods in our subset: (i) methods for testing spatial relations between geometric objects, and (ii) methods that support spatial analysis. We have given further details below:

4 Speci<sup>fi</sup>cally the OpenGIS©Simple Features Access (SFA) standard, also called ISO 19125

![](/api/attachments/CSA28DC3/fulltext/images/e7b5db6fc5072f77a5b74a3f65ef6aaa1ee8c4f56830515d60bec076dc28e9df.jpg)  
Fig. 13. An excerpt of our SPRML metamodel for spatial personalization.

6.2.3.1. Methods for testing spatial relations between geometric objects.

• Equal: returns true if this geometric object is “spatially equal” to another geometry.

• Disjoint: returns true if this geometric object is “spatially disjoint” from another geometry.

• Intersect: returns true if this geometric object “spatially intersects” another geometry.

• Cross: returns true if this geometric object “spatially crosses” another geometry.

• Inside: returns true if this geometric object “spatially contains” another geometry.

6.2.3.2. Methods that support spatial analysis.

• Distance: returns the shortest distance between any two points in the two geometric objects as calculated in the spatial reference system of this geometric object.

• Intersection: returns a collection of geometric objects that represent the intersection of this geometric object with another geometry.

## 6.2.4. Spatial personalization actions

Personalization rules can contain three kinds of actions. Firstly, as previously mentioned, satisfying a personalization requirement may imply acquiring knowledge about the user at runtime. For this purpose, an acquisition action (SetContent) has been de<sup>fi</sup>ned to update the spatial-aware user model. Secondly, we have the actions that add the required spatiality into the schema of the DW by either adding some geometric description to a previously multidimensional element (BecomeSpatial action) or adding new geographic elements (AddLayer action). These actions allow users to add spatiality at the conceptual level according to each decision maker needs. In order to describe the geometry of the new elements, the geometric types de<sup>fi</sup>ned in the spatial-aware user model are used (GeometricTypes). Finally, we have the actions taken over the instances of the SDW (SelectInstance action). The great advantage of this action is when used in combination with spatial conditions. In this way, it is possible to select speci<sup>fi</sup>c instances for every decision maker according to a spatial expression. Further details of these actions are described next:

• SetContent(Property p, ValueSpecification v): this action allows users to update the value of a property p of the user model or the different multidimensional models. The new value v can be a literal or a formula.

• SelectInstance(Variable i): this action allows to select a speci<sup>fi</sup>c instance i. It is mainly used for <sup>fi</sup>ltering the SDW by combining spatial and boolean SPRML expressions. For example, the decision maker could select only the sales made less than 5 km from a hospital.

• BecomeSpatial(Element e, GeometricType g): this action allows users to add a spatial description g to an MD element e. For example, in order to correlate the distance between Stores and Clients, we have to spatially describe both elements.

• AddLayer(String s, GeometricType g): this action allows users to add new geographic data to the MD structure. These data are grouped in a thematic layer named s and geometrically described by g. For example, in order to analyze sales made in stores near a highway exit, we have to add the geographic information describing highways.

## 7. Case study

This section presents the execution of the different personalization rules set for each user of our motivating sample scenario. Furthermore, the actions taken over the common model are detailed and the <sup>fi</sup>nal models are presented.

## 7.1. Spatial personalization for the deliveryPromotion role

For the delivery promotion analysis, the user requires the sales to customers living near the store. First, he/she requires the modeling of a spatial description of the customer and store elements. Then, he/she requires to select only the customers near the store (let's say less than 500 m). Below, we have presented the required SPRML rules set in order to cover these user needs.

Speci<sup>fi</sup>cally, the set is conformed by two rules promoDelivery1 and promoDelivery2.

```matlab
Rule: promoDelivery1 When SchemaDesign do
    For each u in (SUS.User) do
    If (u.AnalysisRole = "deliveryPromotion") then
    BecomeSpatial(MD.Customer,POINT);
    BecomeSpatial(MD.Store,POINT);
    endif
    endForeach
endWhen

Rule: promoDelivery2 When InstancesDesign do
    For each u,c,s in(SUS.User,SMD.Customer,SMD.Store) do
    If (u.AnalysisRole = "deliveryPromotion") AND
    Distance(c,s) < 500) then
    SelectInstance(c);
    endif
    endForeach
endWhen
```

Rule promoDelivery1 is triggered when the SchemaDesign event occurs and it performs two actions in order to convert the multidimensional elements corresponding to customers and stores into spatial levels (with a point description). Whereas, rule promoDelivery2 is triggered when the InstancesDesign event occurred and it selects the stores near customers by using the Distance operator in the condition statement and the SelectInstance action. It is important to notice that these rules only affect the schema for the deliveryPromotion role by also including this constraint in the condition.

Fig. 14 shows the spatial model for the user involved in the delivery promotion analysis obtained after applying the previous rules to the MD model of Fig. 3. Notice the new spatial levels for customers and stores stereotyped as ≪SpatialLevel≫ and represented by icon (check Fig. 2).

## 7.2. Spatial personalization for the pharmaceuticalPromotion Role

For the pharmaceutical product promotion analysis, the user requires the sales of pharmaceutical products in stores near any hospital.

First, he/she requires the modeling of a spatial description of hospital and store elements. Then, he/she requires to select only the stores near a hospital (say less than 700 m). Below, we have presented the required SPRML rules set in order to cover these user needs. Speci<sup>fi</sup>cally, the set is conformed by two rules promoHosp1 and promoHosp2 that only affect the schema for the pharmaceuticalPromotion role by including a boolean constraint in the condition statement.

```txt
Rule: promoHosp1 When SchemaDesign do
    For each u in (SUS.User) do
    If(u.AnalysisRole = "pharmaceuticalPromotion")
    then
    AddLayer("Hospitals", POINT);
    BecomeSpatial(MD.Store, POINT);
    endif
    endForeach
endWhen

Rule: promoHosp2 When InstancesDesign do
    For each u, s in (SUS.User, SMD.Store) do
    If(u.AnalysisRole = "pharmaceuticalPromotion")
    AND Distance(SMD.Hospital, s) < 700) then
    SelectInstance(s);
    endif
    endForeach
endWhen
```

Rule promoHosp1 is triggered when the SchemaDesign event occurs and it performs two actions: (i) add a geographic layer to describe hospital location by using AddLayer action, and (ii) convert the stores' multidimensional element to a spatial level (with a point description). Then, in the promoHosp2 rule, this spatial information is used in order to select the nearby stores by using the Distance operator and SelectInstance action.

Fig. 15 shows the spatial model for the user involved in the delivery promotion analysis obtained after applying the previous rules to the MD model of Fig. 3. Notice the new spatial level for stores stereotyped as ≪SpatialLevel≫ and represented by icon and a hospital geographical layer stereotyped as ≪Layer≫ and represented by icon (check Fig. 2).

![](/api/attachments/CSA28DC3/fulltext/images/e3c3ca430084693d256d35a4b817b50388b65b154c9cfa926d8db3a5bc982dbd.jpg)  
Fig. 14. SMD model obtained for the deliveryPromotion role

![](/api/attachments/CSA28DC3/fulltext/images/ef532388aa156e29c7bded83ea8ce10a6a0d0ea11014eaa2c949682f8c61adc4.jpg)  
Fig. 15. SMD model obtained for the pharmaceuticalPromotion role.

## 7.3. Spatial personalization for the employeeAnalysis Role

For the human resource analysis, the user requires to select employees based on the public transportation that they use to go to work. Initially, he/she requires the spatial description of the employees' home, subway stations and store locations. Then, he/she requires to select only the employees living near the store (say less than 5 km away) and with a subway connection.

Below, we have presented the required SPRML rules set in order to cover these user needs. Speci<sup>fi</sup>cally, the set is conformed by two rules rrhh1 and rrhh2 that only affect the schema for the pharmaceuticalPromotion role.

```txt
Rule: rrhh1 When SchemaDesign do
    For each u in (SUS.User) do
    If (u.AnalysisRole = "employeeAnalysis") then
    AddLayer ("SubwayStations", POINT);
    BecomeSpatial(MD.Employee, POINT);
    BecomeSpatial(MD.Store, POINT);
    endif
    endForeach
endWhen

Rule: rrhh2 When InstancesDesign do
    Foreach u, e, s in(SUS.User, SMD.Employee, SMD.Store) do
    If (u.AnalysisRole = "employeeAnalysis") AND
    e.storeId = s.storeId AND Distance(e, s) < 5000 AND
    Distance(e, SMD.SubwayStations) < 500) then
    SelectInstance(e);
    endif
    endForeach
endWhen
```

Rule rrhh1 is triggered when the SchemaDesign event occurs and it performs three actions: (i) add a geographic layer to describe subway stations by using AddLayer action, (ii) convert the stores' multidimensional element to a spatial level (with a point description), and (iii) convert the employees multidimensional element to a spatial level (with a point description). Then, in the rrhh2 rule, this spatial information is used in order to select the employees living near a subway station and the store by using the Distance operator and SelectInstance action.

Furthermore, the user could also be interested in other public transportation connections, such as bus stations. For example, we can add some instances to the analysis if the user has manifested enough interest in subway connections. To cope with this requirement, the <sup>fi</sup>rst step is to gather the user interest in employees living close to a subway station and near the store. For this purpose we de-<sup>fi</sup>ne the interest of the user as the times he/she selects those instances, and we store this information in the spatial-aware user model by means of the following rule:

```txt
Rule: rrhh3 When SpatialSelection(SMD.Store, Distance (SMD.Store,
    SMD.SubwayStations) < 5000) do
    For each u in (SUS.user) do
    If (u.AnalysisRole = "employeeAnalysis") then
    SetContent(u.Subway2StoreInterest.
    degree,
    SetContent(u.Subway2StoreInterest.
    degree,
    u.Subway2StoreInterest.degree + 1);
    endif
    endForeach
endWhen
```

Rule rrhh3 is triggered when the SpatialSelection event occurs and it increments the user interest attribute in the spatialaware user model by using the SetContent action. Then, another personalization rule has to be de<sup>fi</sup>ned to also select employees living close to a bus stop and the store if the spatial selection degree is higher than a threshold de<sup>fi</sup>ned by the designer (let say 5). These actions correspond to the rrhh4 and rrhh5 rules described next:

![](/api/attachments/CSA28DC3/fulltext/images/1a0b7c8f8c5cfcbb77755fe2b6b04c0f1ab2236d0fc787ec5f322419ba021ae5.jpg)  
Fig. 16. SMD model obtained for the employeeAnalysis role.

```txt
Rule: rrhh4 When SessionEnd do
    For each u, e, s in (SUS.User) do
    If (u.AnalysisRole = "employeeAnalysis") AND
    u.Subway2StoreInterest.degree > 5) then
    AddLayer("BusStops", POINT);
    endif
    endForeach
endWhen
```

```txt
Rule: rrhh5 When SessionStart do
    For each u,e,s in (SUS.User,SMD.Employee,SMD.Store) do
    If (u.AnalysisRole="employeeAnalysis") AND
    u.Subway2StoreInterest.degree > 5 AND e.storeId = s.storeId
    AND Distance(e,s) < 3000 AND Distance(e,SMD.Bus-Stops) < 500)
    then
```

![](/api/attachments/CSA28DC3/fulltext/images/63a066f03fff4408dddc4f74046e955f2e7680569f66b3f1fe8cb640949a0463.jpg)  
Fig. 17. Portion of the EBNF-grammar corresponding to the SPRML inside ANTLR grammar editor

SelectInstance(e); endIf endForeach

endWhen

Rule rrhh4 is triggered when the SessionEnd event occurs and it adds a geographic layer to describe bus stops by using AddLayer action if the user interest degree exceeds the threshold. Then, rule rrhh5 is triggered when the SessionStart event occurs and it performs the required action in order to add the additional instances. Fig. 16 shows the spatial model for the user involved in human resources. That model has been obtained after applying the rule set described above for the employeeAnalysis role to the MD model of Fig. 4. It is supposed that a runtime update occurs while a precise behavior has been detected in the user. Speci<sup>fi</sup>cally, the user has selected many times the employees living near a subway station and the store. Therefore, the interest degree became greater than the threshold and during the restart of the session some personalization actions are done. Notice the new spatial levels for employees and stores represented by ≪SpatialLevel≫ stereotype ( ) and the subway and bus geographical layers represented by a ≪Layer≫ stereotyped class ( ).

## 8. Implementation

In this section, we describe the implementation of our spatial personalization approach. In previous works [9,11,20], we have presented conceptual modeling and code generation implementations under Eclipse Ganymedes framework [30] by using plugin extensions. Then, these plugins had been grouped in the Lucentia BI Suite.<sup>5</sup> Brie<sup>fl</sup>y, the modeling part of this suite is encourage using the native UML2 API available. We have used this plugin in order to de<sup>fi</sup>ne all our pro<sup>fi</sup>les and the different model instances. For the code generation, the suite follows the MDA standard where a platform independent model (PIM) could be transformed in different platform speci<sup>fi</sup>c models (PSM) from which code is obtained in straightfoward way. Speci<sup>fi</sup>cally, PIM models are de<sup>fi</sup>ned by using our SMD pro<sup>fi</sup>le and the speci<sup>fi</sup>c PSM selected is de<sup>fi</sup>ned by using a CWM editor built using EMF generation tools. Finally, the mapping between PIM and PSM models had been implemented using the ATL <sup>6</sup> plugin and the PSM to code generation with the MOFScript<sup>7</sup> plugin.

The novel part of the implementation is the SPRML Interpreter. Firstly, a language tool generator is required. There are different textual language workbenches available, especially on the Textual Modeling Framework project of Eclipse community. Most of the well-known approaches are enumerated and detailed in [21]. However, there are two main approaches of Eclipse community, those are Xtext and TCS. On one hand, Xtext starts de<sup>fi</sup>ning a simple Extended Backus Naur Form (EBNF) style grammar in order to obtain a metamodel, an editor and a parser. On the other hand, TCS starts de<sup>fi</sup>ning a metamodel and then make some kind of scanner/parsing at runtime. As Xtext and TCS, many other approaches use some kind of ANTLR<sup>8</sup> technology in order to support the parsing process. ANTLR is itself a tool that is used in the construction of language tools such as interpreters or compilers by using a formal EBNF grammar.

In previous work [7], we have implemented an EBNF grammar de<sup>fi</sup>nition for the PRML and that is our starting point. Therefore, in the same way, we have de<sup>fi</sup>ned a similar EBNF grammar to represent SPRML (see Fig. 17). Then, we have taken advantage of ANTLR that only requires a formal EBNF grammar in order to build the required interpreter. It is important to notice that this generated interpreter also uses the UML2 API in order to take the respective personalization actions over the models.

## 9. Conclusions and future works

Current SDW development approaches rely on a unique and static spatial multidimensional model for all decision makers. However, due to the great volume of spatial information, personalization is highly convenient in order to provide spatial multidimensional models tailored to speci<sup>fi</sup>c decision makers, improving their satisfaction [29].

In this paper, we have presented a modeling approach for spatial data warehouse personalization by providing two new design artifacts: (i) a spatial-aware user model which captures all the userrelated information needed for personalization, and (ii) a set of spatial personalization rules which specify the required personalization actions. The resulting personalized schemas help simplify the analysis since they only contain the required spatial multidimensional structures and instances and the number of required spatial operations is therefore lower than using a unique spatial schema for all users. Our personalization process for SDW development has been formalized by means of SPEM. Finally, we have presented an implementation of our approach under Eclipse framework that mainly focuses in the SPRML interpreter. As a short-term future work, we plan to integrate the SPEM model of the process in a model-driven approach in order to generate SDW development tools automatically. Moreover, we are working on integrating other new complex data types, specifically, the temporal [33] and continuous field [32] data types. Finally, we are also working on a new set of spatial operations in order to simplify rule de<sup>fi</sup>nition and avoid the use of hard-to-understand combinations of spatial operators.

## Acknowledgments

This work has been partially supported by the MANTRA project (GRE09-17) from the University of Alicante, by the QUASIMODO project (PAC08-0157-0668) from the Castilla-La Mancha Ministry of Education and Science (Spain), and by the MESOLAP project (TIN2010- 14860) from the Spanish Ministry of Education and Science. Octavio Glorio is funded by the University of Alicante under the 11th Latin American grant program.

## References

[1] S. Bimonte, A. Tchounikine, M. Bertolotto, Integration of geographic information into multidimensional models. Part I. ICCSA'08. Proceedings of the Internationa Conference on Computational Science and Its Applications, Springer-Verlag, 2008, pp. 316–329.

[2] S. Bimonte, P. Wehrle, A. Tchounikine, M. Miquel, GeWOlap: A web based spatial OLAP proposal, OTM workshops, 2006 (2), pp. 1596–16.

[3] J. da Silva, V.C. Times, A.C. Salgado, C. Souza, R. do Nascimento Fidalgo, A.G. de Oliveira, A set of aggregation functions for spatial measures, in: DOLAP, 2008, pp. 25–32

[4] J. da Silva, A.S.C. Vera, A.G. de Oliveira, R. do Nascimento Fidalgo, A.C. Salgado, V.C. Times, Querying geographical data warehouses with GeoMDQL, in: SBBD, 2007, pp. 223–237.

[5] R. do Nascimento Fidalgo, V.C. Times, J. da Silva, F. da Fonseca de Souza, Geodwframe: A framework for guiding the design of geographical dimensional schemas, in: DaWaK, pp. 26–37.

[6] A. Escribano, L. Gomez, B. Kuijpers, A.A. Vaisman, Piet: A GIS-OLAP Implementation, in: DOLAP'07: Proceedings of the ACM Tenth International Workshop On Data Warehousing and OLAP, ACM, New York, NY, USA, 2007, pp. 73–80.

[7] I. Garrigós, A-OOH: Extending web application design with dynamic personalization, Ph.D. thesis, University of Alicante, 2008.

[8] I. Garrigós, J. Pardillo, J.N. Mazón, J. Trujillo, A conceptual modeling approach for OL AP personalization. ER'o9: Proceedings of the 28th International Conference on Conceptual Modeling, Springer-Verlag, Berlin, Heidelberg, 2009, pp. 401–414.

[9] O. Glorio, J. Trujillo, An MDA approach for the development of spatial data warehouses, in: DaWaK, 2008, pp. 23–32.

[10] O. Glorio, J. Trujillo, Designing data warehouses for geographic OLAP querying by using MDA , in: ICCSA, 2009 (1), pp. 505–519.

[11] O. Glorio, J. Pardillo, J.N. Mazón, J. Trujillo, Dawara: an eclipse plugin for using i\* on data warehouse requirement analysis, IEEE International Conference on Requirements Engineering (2008) 317–318.

[12] O. Glorio, J. Zubcoff, J. Trujillo, A model driven framework for geographic knowledge discovery, Geoinformatics, , 2009, pp. 1–6.

[13] O. Glorio, J.N. Mazón, I. Garrigós, J. Trujillo, Using web-based personalization on spatial data warehouses, EDBT'10: Proceedings of the 2010 EDBT/ICDT Workshops, ACM, New York, NY, USA, 2010, pp. 1–8.

[14] L. Gomez, S. Haesevoets, B. Kuijpers, A.A. Vaisman, Spatial Aggregation: Data Model and Implementation, CoRR abs/0707.4304, , 2007.

[15] Y.E. Ioannidis, G. Koutrika, Personalized systems: models and methods from an IR and DB perspective, in: VLDB, 2005, pp. 1365.

[16] S. Luján-Mora, J. Trujillo, I.Y. Song, A UML pro<sup>fi</sup>le for multidimensional modeling in data warehouses, Data & Knowledge Engineering 59 (2006) 725–769.

[17] E. Malinowski, E. Zimányi, Representing spatiality in a conceptual multidimensional model, GIS'04: Proceedings of the 12th Annual ACM International Workshop on Geographic Information Systems, ACM, New York, NY, USA, 2004, pp. 12–22.

[18] E. Malinowski, E. Zimányi, Advanced Data Warehouse Design: From Conventional to Spatial and Temporal Applications (Data-Centric Systems and Applications), Springer Publishing Company, Incorporated, 2008.

[19] E. Malinowski, E. Zimányi, Implementing spatial data warehouse hierarchies in object-relational DBMSS, in: ICEIS, 2007 (1), pp. 186–191.

[20] J.N. Mazón, J. Trujillo, An MDA approach for the development of data warehouses Decision Support Systems 45 (2008) 41–58.

[21] B. Merkle, Textual modeling tools: overview and comparison of language workbenches, SPLASH'10, Proceedings of the ACM International Conference Companion on Object Oriented Programming Systems Languages and Applications Companion, ACM, New York, NY, USA, 2010, pp. 139–148.

[22] OGC, Open Geospatial Consortium Inc, OpenGIS Implementation Standard, Version 1.2.1, 2010http://www.opengeospatial.org.

[23] OMG, Object Management Group, Model Driven Architecture (MDA), http:/ www.omg.org/mda/2004.

[24] OMG, Object Management Group, Meta Object Facility (MOF) 2.0, http://www. omg.org/spec/MOF/2.02006.

[25] OMG, Object Management Group, Object Constraint Language, (OCL), http:// www.omg.org/spec/OCL/2.0/2006.

[26] OMG, Object Management Group, Software Process Engineering Meta-Model (SPEM), http://www.omg.org2008.

[27] T.B. Pedersen, N. Tryfona, Pre-aggregation in spatial data warehouses, SSTD'01: Proceedings of the 7th International Symposium on Advances in Spatial and Temporal Databases, Springer-Verlag, London, UK, 2001, pp. 460–480.

[28] Bimonte Sandro, Tchounikine Anne, Miquel Maryvonne, Geocube, a multidimensional model and navigation operators handling complex measures: application in spatial OLAP, Advances in Information Systems (ADVIS), Springer, Berlin/Heidelberg, Germany, 2006, pp. 100–109.

[29] K. Stefanidis, E. Pitoura, P. Vassiliadis, Modeling and storing context-aware pref erences, in: ADBIS, 2006, pp. 123–140.

[30] The Eclipse Foundation, Eclipse Ganymedes, Version 3.4, http://www.eclipse org2009.

[31] V. Times, R. Fidalgo, R. Fonseca, J. Silva, A. Oliveira, A metamodel for the speci<sup>fi</sup>cation of geographical data warehouses, New Trends in Data Warehousing and Data Analysis, volume 3, Springer, 2009, pp. 1–22.

[32] A.A. Vaisman, E. Zimányi, A multidimensional model representing continuous <sup>fi</sup>elds in spatial data warehouses, in: GIS, 2009, pp. 168–177.

[33] A.A. Vaisman, E. Zimányi, What is spatio-temporal data warehousing?, in: DaWaK, 2009, pp. 9–23.

![](/api/attachments/CSA28DC3/fulltext/images/2e575020560622c777b47bdf7123e62272dc2be497337b711c092babbf62b1a2.jpg)  
Octavio Glorio is a PhD in Computer Science from the University of Alicante (Spain). He holds a Master in Bioinformatics at the University of Turin (Italy) and Electronic Engineering from the Universidad Simon Bolivar (Venezuela). He has done a research stay at the Free University of Brussels (Belgium). His research is mainly oriented to the design of spatial data stores and processes of spatial search of knowledge. Email: oglorio@dlsi.ua.es

![](/api/attachments/CSA28DC3/fulltext/images/2cf2fff342f01ff06b06a9e3ed0253e9eb31628310ad7f31222738b2256a43a4.jpg)

Jose-Norberto Mazón obtained his Ph.D. in Computer Science from the University of Alicante (Spain). He currently enjoys a research grant from the Spanish Ministry of Education and Science. He has published several papers about data warehouses in national and international workshops and conferences, (such as DAWAK, ER, DOLAP, BNCOD, JISBD and so on) and in several journals such as Decision Support Systems (DSS) or Data and Knowledge Engineering (DKE). His research interests are: business intelligence, design of data warehouses, multidimensional databases, and model driven development. Email: jnmazon@dlsi.ua.es

![](/api/attachments/CSA28DC3/fulltext/images/e06f490ad2399dce4196d710ca1e0ecbcf2cc437fd9ed61dbaa21943d8eeca2d.jpg)

Irene Garrigós is an assistant professor and post-doc researcher at the University of Alicante, (Spain), from which she holds a PhD and a Master in Computer Science. She has published several papers in national and international workshops and conferences, such as ICWE, ER, WISE, APWEB, JISBD and so on. Dr. Garrigós has served as a Program Committee member of several workshops and conferences such as ER, WISM, MDA, FPUML, UWA and has served as assistant referee in several international conferences such as WWW and ICWE. She has done research stays in Belgium (Vrije Universiteit Brussel) and the Netherlands (Technische Universiteit Eindhoven). Her research interests are: Web engineering personalization model

driven development, Web and business intelligence, adaptive systems. Email: igarrigos@dlsi.ua.es

![](/api/attachments/CSA28DC3/fulltext/images/897f8222c368365123c912d852004e3c61b031b7fa3ab30737010787e509d497.jpg)

Juan Trujillo is an associated professor at the Computer Science School at the University of Alicante, Spain. Trujillo received a Ph.D. in Computer Science from the University of Alicante (Spain) in 2001. His research interests include database modeling, data warehouses, conceptual design of data warehouses, multidimensional databases, data warehouse security and quality, mining data warehouses, OLAP, as well as object-oriented analysis and design with UML. He has published many papers in high quality international conferences such as ER, UML, ADBIS, CAiSE, WAIM or DAWAK. He has also published papers in highly cited international journals such as IEEE Computer, Decision Support Systems (DSS), Data and Knowledge Engi

neering (DKE) or Information Systems (IS). Dr. Trujillo has served as a Program Committee member of several workshops and conferences such as ER, DOLAP, DAWAK, DSS, JISBD and SCI and has also spent some time as a reviewer of several journals such as JDM, KAIS, ISOFT and JODS. He has been Program Chair of DOLAP'05 and BP-UML'05, and Program Co-chair of DAWAK'05, DAWAK'06, BP-UML'06, FP-UML'07, FP-UML'08, and FP-UML'09. Email: jtrujillo@dlsi.ua.es
