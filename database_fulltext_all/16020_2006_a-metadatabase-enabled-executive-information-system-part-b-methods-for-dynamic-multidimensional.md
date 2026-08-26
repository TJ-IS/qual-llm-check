---
otero_id: 16020
otero_key: "YMJYSAB3"
title: "A metadatabase-enabled executive information system (Part B): Methods for dynamic multidimensional data analysis"
authors: "Waiman Cheung; Gilbert Babin"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.01.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# A metadatabase-enabled executive information system (Part B): Methods for dynamic multidimensional data analysis

Waiman Cheung <sup>a,⁎</sup>, Gilbert Babin

Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong Shatin, Hong Kong <sup>b</sup> Service d'enseignement des technologies de l'information, HEC Montréal, 3000, chemin de la Côte-Sainte-Catherine, Montréal (Québec), Canada H3T 2A7

Received 16 November 2004; received in revised form 24 January 2006; accepted 29 January 2006 Available online 6 March 2006

## Abstract

In tandem with the growth of the Internet and e-business, the number of digital data sources has increased immensely. These data sources contain important transactional data and are generally interconnected via a network. This has created a pressing need for a suitable executive information system (EIS) that is capable of extracting data from internal and external data sources and providing data analysis on demand for business executives. On-demand data analysis requires an information integration approach that can manage rapid changes in data sources. Existing EISs commonly adopt data warehousing technology to consolidate data from multiple sources in a tailor-made fashion, and support predefined multidimensional data analysis. However, this architecture is neither adaptable to changes in local sources nor flexible enough for ad hoc analyses. This paper develops methods and algorithms for a new EIS architecture that takes advantage of a metadatabase to achieve adaptability and flexibility. A PC-based prototype is built to prove the concept. © 2006 Elsevier B.V. All rights reserved

Keywords: Executive information systems; Systems integration; Metadatabase management system; Data warehouse; On-line analytical processing

## 1. Introduction

In an evolving marketplace, it is important to rapidly and properly assess the performance and state of an enterprise. Such assessment is often performed using indicators, which are measures of enterprise performance, used to determine how well an enterprise is performing against predetermined critical success factors. Analysis is usually performed by comparing an indicator's value with previous and planned values to derive a measure of performance against goals.

Data warehousing has been adopted as a key technology that aids executive information systems (EISs). Data warehouses consolidate data from multiple sources in a tailor-made fashion and support predefined multidimensional data analysis. Multidimensional data analysis is a method of consolidating, viewing, and analyzing indicators in accordance with multiple dimensions that are used by executives to analyze their enterprises. This type of analysis helps executives to discover problematic areas and reveals opportunities for improving the competitive edge of enterprises. For example, an executive may examine the indicator of total sales with respect to product category by sales office, or of product category against customer income level to review an enterprise's sales strategy. In this case, product category, sales office, and customer income level are the dimensions for the analysis. An indicator can also be analyzed at different abstraction levels along a particular dimension, such as the total sales of a given sales representative, sales office, district office, or regional office. In multidimensional analyses, these changes of scope or abstraction levels are referred to as roll-ups when the scope is increased (for example, from sales representative to regional office), and drill-downs when the scope is decreased (for example, from regional office to sales representative). Indicators and dimensions are closely related, and dimensions can only be defined based on indicators. Therefore, an indicator and its related dimensions are always considered as a unit, which is known as a multidimensional analysis unit (MAU).

EISs are developed to support the needs of executives in reviewing critical indicators. Contemporary EISs are often equipped with a data warehouse that supports multidimensional data analysis [16], but unfortunately current EIS architectures offer only limited flexibility and adaptability [4]. Flexibility here refers to the ability to accommodate the changing needs of executives in data analysis, and adaptability refers to the ability to adapt to changes that may occur in local data sources. As executives become more computer literate, their information needs will become more and more sophisticated [14], and EISs must also be able to rapidly adapt to changes in local systems, which they are not currently able to do [17,18,19]. Indeed, existing EISs rely on a fixed data schema and predetermined data analysis patterns that hinder their flexibility and adaptability. Following an analysis of current EIS architecture, Cheung and Babin [4] presented a metadatabase-enabled EIS architecture that provides this needed flexibility and adaptability. In this paper, we develop methods and algorithms to support this architecture to show the viability of the approach.

This paper is organized as follows. Section 2 presents an overview of the proposed EIS architecture, and Sections 4 and 5 describe the functionalities of the subsystems to support this architecture. These functionalities are illustrated using a small example, which is described in Section 3. Section 6 provides an evaluation of the EIS architecture, and we conclude the paper in Section 7.

## 2. A metadata-based EIS architecture

Fig. 1 presents a detailed design of the new EIS architecture that is proposed in [4]. This architecture supports dynamic indicator management, and enables executives and their staff to identify and set up new indicators in an ad hoc manner. It consists of three main sub-systems: the Metadatabase Management System (MDBMS), the ROLAP/MDB Analyzer, and the ROLAP/MDB Interface.

## 2.1. The metadatabase system

The MDBMS is a knowledge-based system that has been developed to integrate and manage multiple local systems through the use of metadata, which are stored in a metadatabase, or database of metadata [1,3,6,8,7,10– 12]. The metadata describe the global model of the enterprise using four views: application, functional, structural, and operational. The first three views describe the different application systems. The structural view presents an enterprise-wide conceptual model of all of the data sources, and the functional view includes rules to map data across applications. The operational view describes the implementation details of the local systems, such as operating systems, DBMS, and database schema. With this global model and the Global Query System (GQS) [5] of the MDBMS, ad hoc queries can be dynamically formulated and generated to retrieve data from local systems. Therefore, the MDBMS provides transparent access to data that are stored in local systems.

In the EIS architecture that is proposed in this paper, we use the metadata content of the MDBMS to perform dynamic, ad hoc multidimensional data analysis. In the ROLAP/Analysis sub-system, metadata are used with various algorithms and methods to generate queries to local systems. In the ROLAP/MDB Interface subsystem, metadata are used in a browsing facility for the formulation of analyses.

## 2.2. The ROLAP/MDB Analyzer

Algorithms and methods are needed to enable on-line multidimensional data analysis. These algorithms and methods are designed to take full advantage of the metadata that are provided by the MDBMS. They are implemented as different software modules of the ROLAP/MDB Analyzer, namely, the Dimension Determination module, the MAU Sub-view Materializer, the ROLAP/MDB Processor, the MAU Saver, and the MQL Generator. These modules are described in Section 4.

## 2.3. The ROLAP/MDB Interface

This sub-system presents information about the indicators and dimensions (MAUs) to the user through the Indicator Browser module and the Dimension

![](/api/attachments/YMJYSAB3/fulltext/images/3528583ac2a19b59686af70ab213ebf1bf508daee56eecf67e4dbe308d892072.jpg)  
Fig. 1. Detailed EIS architecture.

Selector module. It also enables the dynamic multidimensional analysis of an indicator using the Multidimensional Data Analyzer. Section 5 presents a detailed description of these different modules.

## 3. An illustrative scenario

To better illustrate the use of the methods and algorithms, we employ the following business scenario, which is based on a (simplified) enterprise in the stationery business. The enterprise has three functional systems: Accounting, Marketing, and Sales Force Management, which are implemented on different hardware platforms using different database management systems.

For data modeling purposes, we use the Two-Stage Entity-Relationship (TSER) modeling methodology [9,13,15]. The TSER model was developed primarily to enable the integration of heterogeneous, distributed database systems, and is the underlying data model that is used in the MDBMS. The TSER functional model captures the business rules of the applications that are to be integrated (first stage), and the TSER structural model, which is an Entity-Relationship-like representation, is used to describe the database schemata (the second stage). In this paper, we focus on the data schema but not the use of business rules, and thus present only the TSER structural model of the scenario. The structural model uses four basic constructs: Operational Entities (OEs), which are entities or tables that are characterized by a singular key and are represented by a rectangle; plural relationships (PRs), which are entities or tables that are characterized by a composite key that shows a many-to-many relationship and are represented by a single-line diamond; functional relationships (FRs), which are many-to-one relationships that are represented by a dashed-line diamond; and mandatory relationships (MRs), which are one-to-many, owner and owned relationships that are represented by a double-line diamond.

![](/api/attachments/YMJYSAB3/fulltext/images/05331e05380edc1aa1a46f68079bffc8732714b054b7cd4d7b06b7061d34f8d8.jpg)  
Fig. 2. Structural model of the example enterprise.

The global data model of our sample enterprise is illustrated in Fig. 2. Different dashed lines are used to outline the three functional systems in the figure.

## 4. The ROLAP/MDB Analyzer

The main roles of the ROLAP/MDB Analyzer subsystem are to process metadata about the data sources that are available in the enterprise to generate and store an MAU for a given indicator, and to access the distributed data sources to retrieve the necessary data for materializing an MAU. The materialized MAU is stored in a relational database within the ROLAP/MDB Analyzer. The functionalities of this sub-system can be analyzed against these two basic functions, and are the topic of the following two subsections.

## 4.1. MAU generation and dimension determination

An important goal of database modeling is to capture business logic and to place it in the database schema. This business logic, or business rules, is represented through the identification of entities, keys, relationships, and integrity constraints. The generation of MAUs utilizes these embedded business rules in the TSER structural model to determine possible dimensions that would be applicable to an indicator.

A multidimensional analysis unit (MAU) is a database view that contains an indicator and all of the potential dimensions that can be used to examine that indicator, which essentially means that an MAU defines the indicator's analysis space. In a given database schema, there may be many indicators, but there is only one MAU for each indicator. A database conceptual schema, such as the TSER structural model, provides a navigation map that can be used to identify valid ways to analyze an indicator (whether it conforms to business rules). Specifically, given an indicator i, which is any data field in data table d to which an aggregation function may be applied (for example, the sum of the field “total sale” for all invoices in the data table “Invoice”), possible drill-down paths may only be located in data tables that are reachable from d through many-to-one relationships. Therefore, to construct the MAU, we start from table d and follow all of the possible many-to-one relationships, and the data fields that are on the “one” side of the relationship are the potential dimensions.

In the TSER model, an indicator can be found either in an OE or in a PR, as only these two constructs may contain data fields. Both the FRs and the MRs represent integrity constraints, and as such contain neither indicators nor dimensions. If an indicator is found in an OE (or a PR), the potential dimensions for analyzing the indicator include all of the attributes of that OE (or PR). For example, in Fig. 3 attribute price in the OE “Product” can be used to define an indicator, and its related dimensions can be the data fields in “Product,” such as category and color if an executive wants to look at the average product price for different category and color combinations. The MAU for price is shown as MAU in Fig. 3.

Potential dimensions can be extended to the attributes of other OEs (or PRs) that are functionally related (that is, for which there is a many-to-one path) to the OE (or PR) that contains the indicator. They represent higher levels of abstraction (a roll-up path). For example, in Fig. 3, “salary” in OE SalesRep can be used to define an indicator. All of the attributes in SalesRep, such as age and gender, can be used as dimensions to examine the salary of a sales representative. Dimensions are extended to the attributes of Office, which is functionally related to SalesRep, and of Region, which is also functionally related to SalesRep through the transitivity of the functional relationships. Therefore, $\mathbf { M A U } _ { 2 }$ in Fig. 3 represents all of the possible paths for a drill-down or roll-up analysis of the salary indicator.

![](/api/attachments/YMJYSAB3/fulltext/images/7fb787e63b20cfe1491686bab4c754a75486cf8ab9422be4e3a80381f47bbafb.jpg)  
Fig. 3. MAUs of different indicators.

When an indicator is found in a PR, not only all of the attributes of that PR, but also all of the attributes of all of the OEs that are immediately connected to the PR, are potential dimensions. This follows from the fact that the primary key of each of these OEs is a member of the composite key in the PR. The potential dimensions are extended to the attributes of other OEs that are functionally related to these OEs. Consequently, for the indicator “total sale” in the Invoice PR, the entire schema is an MAU (MAU ), and there are three drilldown/roll-up paths: Product to Invoice, Region to

Customer to Invoice, and Region to Office to SalesRep to Invoice.

## 4.1.1. Saving the MAU

Information about MAUs is stored within the ROLAP/MDB Analyzer sub-system (represented by RDBMS in Fig. 1) by the MAU Saver. The schema of this database is shown in Fig. 4, again using a TSER structural model.

Saving an MAU enables its reuse in future analyses, and also allows the reuse of MAU fragments that have already been used for other indicators. MAUs are stored for performance purposes only, as they can always be reconstructed from the metadata, and in fact do not need to be reconstructed unless there are changes in the local source schemata.

The OE MAU\_Indicator stores the data item that is used as an indicator and the OE or PR within which it is contained. The PR MAU\_RollUp shows the possible drill-down or roll-up paths between pairs of OEs or PRs. The PR MAU\_BelongTo indicates the potential data items that can be used as dimensions along the drilldown or roll-up paths. The OE MAU\_ENTREL contains the list of OEs (ENT for entity) and PRs (REL for plural relationship) that are used in the MAUs, and OE MAU\_ITEM lists data items that are stored in the different OEs and PRs. Fig. 5 shows the MAU information for the “total sale” indicator.

![](/api/attachments/YMJYSAB3/fulltext/images/a1b43724de3a921c14ce078d08f2f8ad661c8fd50bd92f15c3229ae11c9cd4f2.jpg)  
Fig. 4. The MAU schema.

## 4.1.2. Creating the MAU

Fig. 6 presents the algorithm that is used to construct the MAU. The algorithm is started by a call to Initialize\_Algorithm(i,d). For a data object (d) (for example, an OE or PR) that contains an indicator (i), the algorithm recursively examines FRs and MRs with other data objects in the enterprise data model following many-to-one paths. The algorithm makes use of the metadata that are stored both in the MAU schema (Fig. 4) and the metadatabase. Whenever the metadatabase content is accessed, a comment indicates the use of “embedded MQL.” MQL, or Metadatabase Query Language, is a query language that was developed along with the GQS [5] to simplify access to distributed, heterogeneous systems through the metadatabase, and to access the metadata content itself.

## 4.1.3. Ordering indicators or dimensions for selection

Note that the list of potential indicators is large, and that for a given indicator the list of potential dimensions may also be large [4]. Metadata can be used to provide a relative ranking of the potential indicators or dimensions to help executives in the selection process. The intention is not to determine the indicators, which clearly depend on an enterprise's objectives and other strategic and operational factors, but the ranking provides some measure that enables executives to choose the most “appropriate” dimension from a choice of potential indicators.

We have developed a series of metrics (see [2] and Appendix A for details) based on metadata to provide such a relative ranking. These metrics are based on the following observations. A data item for selection as an indicator ideally has a large MAU that combines multiple dimensions and abstraction levels; is numeric, as most aggregate functions only work on numeric data types; and is not a key item, as key attributes only serve to identify, rather than qualify, entities. This method favors the numeric indicators to which all of the aggregate functions are applicable, but does not preclude non-numeric indicators to which only the “count” function may be applied. In contrast, a data item for selection as a dimension ideally displays the opposite characteristics of an indicator: its MAU is small, it is non-numeric, and it is a key item.

We first determine whether a data object d shows a good likelihood of containing indicators or dimensions. The Global Table Ranking metric, which is denoted as GT(d), is closer to 1 when data object d shows a greater likelihood of containing indicators (its MAU is large) and is closer to −1 when data object d shows a greater likelihood of containing dimensions (its MAU is small). The value of GT(d) decreases as we follow a roll-up path and increases as we follow a drill-down path. We use this metric to order data objects (smaller values first) when selecting potential drill-down or roll-up paths.

MAU\_Indicator

<table><tr><td>Indicator</td><td>ERname</td></tr><tr><td>TotalSale</td><td>Invoice</td></tr></table>

MAU\_RollUp

<table><tr><td>Drill-Down</td><td>Roll-Up</td></tr><tr><td>Invoice</td><td>Product</td></tr><tr><td>Invoice</td><td>SalesRep</td></tr><tr><td>Invoice</td><td>Customer</td></tr><tr><td>SalesRep</td><td>Office</td></tr><tr><td>Office</td><td>Region</td></tr><tr><td>Customer</td><td>Region</td></tr></table>

MAU\_BelongTo

<table><tr><td>ERname</td><td>Itemname</td></tr><tr><td>Invoice</td><td>InvoiceID</td></tr><tr><td>Invoice</td><td>InvoiceDate</td></tr><tr><td>Invoice</td><td>SalesRepID</td></tr><tr><td>Invoice</td><td>CustomerID</td></tr><tr><td>Invoice</td><td>ProductID</td></tr><tr><td>Invoice</td><td>TotalSale</td></tr><tr><td>...</td><td>...</td></tr></table>

Fig. 5. MAU for the “sum of total sale” indicator.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Initialize_Algorithm(i, d) {
    If ((i, d) not exist in MAU_Indicator) {
    Write_MAU_Indicator(i, d);
    Determine_All_Dimension_Path(d);
    }
}

Determine_All_Dimension_Path(d) {
    A = Determine_All_Attribute(d);
    Write_MAU_BelongTo(d, A);
    D = Determine_Immediate_Dimensions(d);
    for each  $d_j$  in D {
    If ((d, d_j) not exist in MAU_RollUp) {
    Write_MAU_RollUp(d, d_j);
    If (d_j ≠ d) {
    Determine_All_Dimension_Path(d_j);
    }
    }
}

Determine_Immediate_Dimensions(d) {
    if (d is an Operation Entity) {
    Return (Determine_Dimension_To_OE(d));
    } Else {
    Return (Determine_Dimension_To_PR(d));
    }
}

Determine_All_Attribute(d) {
    Return (
    FROM ENTREL Item GET Itemname
    FOR Itemtype = number
    AND Ername = d;
); /* mbedded MQL
}

Determine_Dimension_To_OE(d) {
    D_FR = FROM ENTREL Integrity GET Slave
    FOR Master = d
    AND Inttype = “FR”; /* embedded MQL
    D_MR = FROM ENTREL Integrity GET Master
    FOR Slave = d
    AND Inttype = “MR”; /* embedded MQL
    Return (D_FR + D_MR);
}

Determine_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity GET Slave
    FOR Master = d
    AND Inttype = “FR”; /* embedded MQL
    D_MR = FROM ENTREL Integrity GET Master
    FOR Slave = d
    AND Inttype = “MR”; /* embedded MQL
    Return (D_FR + D_MR);
}

Determine_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity GET Slave
    FOR Master = d
End
    AND Inttype = “FR”; /* embedded MQL
End
    D_MR = FROM ENTREL Integrity GET Master
End
    FOR Slave = d
End
    AND Inttype = “MR”; /* embedded MQL
End
}

Determine_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity GET Slave
    FOR Master = d
End
    AND Inttype = “FR”; /* embedded MQL
End
    D_MR = FROM ENTREL Integrity GET Master
End
    FOR Slave = d
End
    AND Inttype = “MR”; /* embedded MQL
End
}

Determine_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity GET Master
End
End
Write_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity GET Slave
End
    FOR Master = d
End
    AND Inttype = “FR”; /* embedded MQL
End
    D_MR = FROM ENTREL Integrity GET Master
End
End
    FOR Slave = d
End
    AND Inttype = “MR”; /* embedded MQL
End
}

Determine_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity GET Slave
End
    FOR Master = d
End
    AND Inttype = “FR”; /* embedded MQL
End
    D_MR = FROM ENTREL Integrity GET Master
End
End
    FOR Slave = d
End
    AND Inttype = “MR”; /* embedded MQL
End
}

Determine_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity Get Slave
End
End
Write_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity Get Slave
End
End
Write_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity Get Slave
End
End
Write_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity Get Slave
End
End
Write_Dimension_To_PR(d) {
    D_FR = FROM ENTREL Integrity Get Slave
End
End
Write_Dimension_To_PR(d) {
End
Write_Dimension_To_PR(d) {
End
Write_Dimension_To_PR(d) {
End
Write_Dimension_To_PR(d) {
End
Write_Dimension_To_PR(d) {
End
Write_Dimension_To_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension.To_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension_TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension TO_PR(d) {
End
Write_Dimension To_PR(d) {End}
}
}
}
}
}
}
</div>

Fig. 6. Dimension determination algorithm.

We then determine whether data item i has the potential to be an indicator or a dimension based on its data type and whether or not it is part of a key. The Local Column Ranking metric, which is denoted as LC(i), is closer to 1 when data item i shows a greater likelihood of being an indicator and closer to −1 when it shows a greater likelihood of being a dimension.

However, the LC(i) metric does not consider data objects that contain the data item that is being ranked, and thus by combining the GT(d) and LC(i) metrics, we obtain a metric for ranking data item i in data object d, the Global Column Ranking metric, which is denoted as

GC(i,d). This metric provides a relative ranking among data items, where a data item with a higher value has a greater likelihood of being an indicator, and a data item with a lower value has a greater likelihood of being a dimension. The GC(i,d) metric is used in the prototype to order the potential indicators in descending order and the potential dimensions in ascending order.

## 4.2. MAU sub-view retrieval and materialization

After the user has selected an indicator and dimensions of interest, an MAU sub-view is extracted from local data sources. This sub-view contains all of the data that are required to perform an analysis of the indicator. In other words, the sub-view that is specified by the MAU is materialized. This materialization process is performed by an MQL Generator, which constructs a global query using MQL. The GQS then retrieves production data from the local systems using the generated MQL statements. Fig. 7 shows the general structure of the MQL statements that are generated for this task. The resulting data are joined or denormalized to form a flat table, which is the MAU sub-view.

![](/api/attachments/YMJYSAB3/fulltext/images/06c4c72f420d97eeae90fdd22b3fa54aa1c7b2ce17f6af3042bff658d9279bf3.jpg)  
Fig. 7. MQL statements for retrieving an MAU sub-view.

After retrieval from local sources, the MAU Subview Materializer stores the MAU sub-view into the relational database and completes the materialization process. This is undertaken to provide reusability and performance enhancement, and users can repeatedly analyze the same MAU sub-view by performing different operations, such as slice-and-dice or rotation. Rather than retrieving data from the local systems every time an indicator and its dimensions are selected, the materialized MAU sub-view provides a readily available data set to support this repeated analysis. This reusability enhances the performance of the system, as data only need to be retrieved from a single site, which takes a lot less time than retrieving data from multiple sites. It also reduces the need to access local systems and potentially interfere with operations. We should point out, however, that the user may decide to reload the MAU sub-view before performing the analysis, in which case the EIS has completed its preparation phase and is ready to perform on-line analytical processing (OLAP) operations.

## 5. The ROLAP/MDB Interface

Whereas the ROLAP/MDB Analyzer provides the underlying mechanisms for the construction of MAUs, the ROLAP/MDB Interface offers the methods and mechanisms to facilitate the indicator and dimension selection process (and thus provides the user interface to the ROLAP/MDB Analyzer that is described in Section 4), and performs the actual analysis of an indicator using drill-down or roll-up, rotation, and slide-and-dice operations. We present these functionalities in the following subsections.

## 5.1. Indicator browsing

The Indicator Browser assists executives in selecting an indicator from a short list of potential indicators. Again, we emphasize that the tool supports the choice, but that the final decision is in the hands of the user. The idea is to allow an executive (or a technical assistant) to identify indicators without prior knowledge of the data schema based on the ordering approach that has been described (Section 4.1). To support such a browser, metadata on the global model are required from the

![](/api/attachments/YMJYSAB3/fulltext/images/2b0ce1d008e8c1832c07a1a1aa4a206ae767263c57a7a9aabcee089e70b04447.jpg)  
Text between [...] is optional and exists only if the value in “...” is specified by the executive.

Fig. 8. MQL statements to retrieve metadata for the Indicator Browser.

![](/api/attachments/YMJYSAB3/fulltext/images/5baa6754ae8d1ad45f006bcd7c9411c6abf7b7e316ebedf7af19f67505dd8afa.jpg)  
Fig. 9. Indicator Browser that shows the confined potential indicator.

MDBMS. We extract these metadata using the MQL. Four sample MQL queries are shown in Fig. 8. These queries are used by the Indicator Browser to construct the list of known applications, views, data objects, and potential indicators.

The current prototype implementation of the Indicator Browser provides a pull-down menu that contains a list of data items that may be selected as indicators (Fig. 9). An executive may not know which indicator to examine or where to look for the indicator, in which case a long list of potential indicators will be shown. In this version of the prototype system, we only provide the actual data item name, assuming that the summation is the aggregate function, but clearly this could be improved by providing more information, such as the description of the data items, a list of aggregate functions, or allowing the use of synonyms. The executive can also choose to provide supplementary information, such as the application, view, or data object, to limit the choices. The conceptual grouping of indicators, such as financial- or resource-oriented indicators, can also be provided if such group information has been modeled, and can then be stored in the metadatabase. In our scenario, we assume that the data item “total sale” is selected as an indicator.

## 5.2. Dimension selection

A multidimensional data analysis with too many dimensions may not be easy for a person to comprehend, and thus a system with a feature that allows an executive to focus on two to five dimensions at a time would be helpful. Recall that an MAU defines a view in the global enterprise schema, that is, a TSER sub-model of all of the data constructs that are functionally related to the OE (or PR) that contains the selected indicator. Selecting dimensions is equivalent to constructing a subset of an existing MAU. The Dimension Selector implements mechanisms to construct that subset, and provides a list of potential dimensions for the user to choose from by retrieving metadata from the RDBMS that describes the MAU (see Section 4.1).

Our prototype of the Dimension Selector uses SQL statements to retrieve MAU metadata from the RDBMS to build the dimension specification menu (Fig. 10). The main menu first shows the data object that contains the selected indicator, which is Invoice in this case. If a rollup operation is possible, then a sub-menu pops up to provide additional selections. The upper part of that submenu shows the data objects that are available for further roll-up operations, and the lower part shows the attributes (dimensions) that are contained in the highlighted data object. For example, Customer, Product, and SalesRep are the data objects that are related to Invoice, which contains the selected indicator, whereas Total Sale, Invoice ID, Customer ID, Product

![](/api/attachments/YMJYSAB3/fulltext/images/c88190e5f84dc6c07504d0673f5eb023c1dbb318d09406ff8119bf0b5f975ff2.jpg)  
Fig. 10. Dimension specification menu

![](/api/attachments/YMJYSAB3/fulltext/images/ea0eb72f9fc85b8c58b295aaf0e0c2de7f04b2871dcb3f540313b1e0822d7517.jpg)  
Fig. 11. A three-dimensional data cube formed by two-dimensional slices.

ID, and SalesRep ID are some of the attributes in Invoice that are dimensions that are available for the analysis of total sale.

## 5.3. Multidimensional data analysis

The purpose of multidimensional data analysis is to present summarized data using simple analytical functions, such as count, sum, average, maximum, and minimum, according to multiple data dimensions; and to provide on-line operations for this data set. This facility was developed to obtain a complete, integrated EIS, but as the multidimensional data analysis module does not rely on metadata from the Metadatabase, the MAU subview can be exported to any commercially available ROLAP analysis tool to perform these analyses.

In our proposed EIS architecture, we use SQL to first produce two-dimensional tables that are composed of data cells. The value in each cell represents the result of an analytical function of the indicator. For instance, the front slice of Fig. 11 could be the sum of sales for the Sharpener product, which is sold by all of the salespeople to different customers. Each cell is the result of an SQL query in the MAU sub-view. A three-dimensional data cube can be constructed using multiple slices from the two-dimensional tables in which each slice represents a specific group instance (for example, Sharpener, Ruler, and Pencil) of the third dimension (for example, Product). To view the data cube one slice at a time, the executive will need to specify a group instance in the third dimension. A four-dimensional space can be constructed in the same manner, and can be viewed one slice at a time by providing a group instance for the third and fourth dimensions. The ROLAP/MDB Processor enables multidimensional data analysis by generating the required SQL statements to perform such operations in an MAU sub-view.

The Multidimensional Data Analysis Interface of the ROLAP/MDB allows users to perform on-line analytical processing (OLAP) operations such as slice-anddice, drill-down or roll-up, and rotation. The slice-anddice operation presents the disaggregated values of an indicator in a two-dimensional table (a slice) or one at a time (a dice). The drill-down and roll-up operations allow the user to look at the indicator values at different levels of abstraction. Finally, the rotation operation transposes a data cube to enable a multi-faceted analysis.

Our prototype interface is presented in Fig. 12, in which the slice operators are shown, and Fig. 13, in which the dice operators are shown. At the top of the interface, the user selects whether a slice or dice operation is to be performed. The second section of the interface enables the selection of the dimensions of interest for the analysis, and the third section shows the actual values of the indicator. The last section contains different buttons to control the analysis.

![](/api/attachments/YMJYSAB3/fulltext/images/7eb1f27945128f8f3701a0d9959e514574f1b2e170dc608dec5678f6f2208ec1.jpg)  
Fig. 12. The Multidimensional Data Analysis Interface.

![](/api/attachments/YMJYSAB3/fulltext/images/cd0bf4660716af6060faef9cca260651eabc388106cba2d71d0c11ac696485a6.jpg)  
Fig. 13. Performing a dice operation.

To perform a slice operation, the user first specifies the two dimensions for display using the dimension X and dimension Y pull-down lists, and then clicks the Show Query button. At any point, a roll-up or drilldown operation may be performed by identifying specific dimensions and values for the other three dimensions. This is shown in Fig. 12, in which a slice is performed on a product name and office site, and a drilldown is carried out for a customer named Andrew.

It may be that instead of asking about the total sales of each product at each office, a user wants to know the total sales at each office for each product. In this case, the result must be reorganized so that the Yaxis now shows the Office Site and the X-axis shows the product name. The Rotate Query button may be used to perform such a transposition. Finally, the Clear Query button is used to clear the screen and start another query.

A dice operation shows the value of the indicator for each specific instance of a dimension to answer a question such as how many pencils were sold to Andrew from the Hong Kong office. To perform a dice operation, the user is required to specify the value of dimensions X and Y. Fig. 13 presents a dice operation that was performed on the previous slice (Fig. 12) by specifying a product name (pencil) and an office site (HK).

## 6. Evaluation of the new EIS architecture

The new EIS architecture has new features that are not found in contemporary EISs, such as the ability to access on-line production data to dynamically construct a multidimensional analysis unit (MAU) and to allow ad hoc multidimensional data analysis.

The centralized databases or data warehouses of existing EISs only provide off-line, historical data, and on-line production data are not available for analysis. Thus, the information that is delivered to executives may be outdated, and a comparison with current status may not be possible. The new EIS architecture that is proposed here integrates and manages heterogeneous local database systems at the metadata level. Instead of duplicating local data into a centralized database or a data warehouse, the new EIS utilizes the Global Query Facility of the Metadatabase approach to directly retrieve data from local systems, which makes on-line production data available for the generation of up-to-date MAU for multidimensional data analysis.

By using metadata together with the algorithms and methods that are presented here, potential indicators, their dimensions, and drill-down or roll-up paths (the abstraction levels) can be examined and selected on-line during an analysis. Hence, the ad hoc analytical needs of executives, which are usually unstructured and novel, can now be entertained. Through a step-by-step process of multidimensional data analysis, the new EIS helps executives to explore or traverse business data models to gain information that they may not initially have thought of seeking.

A major potential drawback of the new EIS architecture is the apparent trade-off between processing efficiency and the improvements and new features. This inefficiency may stem from two sources: the extra processing steps that go into the performance of an analysis, including indicator identification, dimensions and the determination of drill-down and roll-up path determination, and the retrieval of on-line production data from local databases, which can be time consuming. This inefficiency may become more serious when the MAU of an indicator is very large and involves many local systems, and the additional processing time could potentially render an EIS that uses this new architecture practically useless. We now highlight some methods that have been incorporated into the architecture to improve the processing efficiency and, as a consequence, enhance performance.

When the data analysis process involves a new indicator, its MAU must be determined. This MAU remains valid as long as the schema of the local systems remains unchanged, as it only describes a view of these local systems. An MAU may be large, and the determination of large MAUs is time consuming. To avoid running the determination process unnecessarily, we save it into a Relational Database Management System (RDBMS), so that when the same indicator is reused for analysis, we do not need to repeat the determination process unless there have been changes in the schema of the local systems. Instead, we retrieve the dimensional information of the indicator from the RDBMS.

The Dimension Selector provides a friendly interface for a user to choose just a few (a sub-view) of the possible dimensions (an MAU) in each analysis. This cuts down the number of data fields that need to be retrieved from local systems, which in effect significantly mitigates the processing efficiency problem. Furthermore, by ranking the potential dimensions, we provide additional guidance to the user to make the data analysis more focused and meaningful.

To further improve processing efficiency, the MAU Sub-view Materializer stores the MAU sub-view in an RDBMS, which means that when an executive wants to perform an analysis based on the same indicator and dimensions, the materialized view can be reused. The retrieval of data directly from the local systems is required only if the analysis is new or if an executive wants to make sure that the analysis reflects recent changes in local data sources. Obviously, the executive can always choose to re-run the MAU materialization process if there is uncertainty as to whether there have been changes in local systems.

The adaptable nature of the new EIS architecture makes it possible and reasonably easy to incorporate a data warehouse, if one exists, as a sub-system of the EIS. The global query optimization process of the MDBMS aims to minimize the number of local systems from which data are retrieved for a given query, so that the EIS will access local systems only when the data are not available in the data warehouse. In addition, the MAU generation process may be used to design star schemata that can then be implemented in the data warehouse, and the MQL that is generated to materialize the MAU subview can be used to automate the population of the data warehouse.

## 7. Conclusion

In this study, we have developed algorithms and methods to support a proposed new Executive Information System (EIS) architecture [4]. This new architecture includes a systems integration mechanism, the metadatabase approach, which enables ad hoc OLAP from heterogeneous systems and databases. Thus, novel and ad hoc requirements for e-business intelligence are now supported with the help of metadata. The algorithms and methods for this approach have been implemented as software modules in a prototype.

A major obstacle for this new architecture is its performance, and the seeming trade-off to obtain adaptability and flexibility. However, we have incorporated methods to alleviate this problem, such as the MAU Saver, Sub-views Selector, and MAU Sub-view Materialization. It transpires that deficient performance only occurs when a new indicator or a new analysis that uses new dimensions is proposed, or when the most recent changes in local data need to be reflected in the data analysis. With existing EISs, extra processing time is also inevitable under the same conditions, as analysts and programmers may be called upon to recompile or redesign the data warehouse to support new requests.

The performance of EISs is an important concern for executives, and therefore a natural extension of this research would be to improve the efficiency of the proposed EIS. Now that we have included view materialization and maintenance mechanisms in the proposed architecture, the next obstacles to surmount include the creation of methods and tools to better couple the metadatabase and data warehouses, the development of MAU materialization criterion, and the establishment of update scheduling to further improve the performance of the EIS by providing the most updated data in a reasonable time frame.

## Appendix A. Metric for classifying indicators and dimensions

## Definitions

d A data object I A data item

Card(X) Number of elements in set X

Roll\_Up(d) The set of data objects that can be directly reached in a roll-up operation from data object d

Drill\_Down(d) The set of data objects that can be directly reached in a drill-down operation from data object d

IsKey(i) 1 if i is not a key, − 1 if i is a key

IsNumeric(i) 1 if i is numeric, −1 if i in not numeric

LT(d) Local classification of data object d

GT(d) Global classification of data object d

LC(i) Local classification of data item i

GC(i,d) Global classification of data item I that is stored in data object d

Sum(X,x,y(x)) The sum of y(x) for all x elements of set X

Adjacent(d) The nodes that are adjacent to data object d

## Formulae

LT(d) (Card(Roll\_Up(d)) − Card(Drill\_Down(d))) /

Adjacent(d) Roll\_Up(d) ∪ Drill\_Down(d)

GT(d) (LT(d) ⁎ (Card(Adjacent(d)) + 1) + Sum(Adja-

cent(d),d′,LT(d′))) / (2 ⁎ Card(Adjacent(d)) + 1)

LC(i) (IsKey(i) + IsNumeric(i)) / 2

GC(i,d) (((GT(d) + 1) ⁎ (LC(i) + 1)) / 2) − 1

Classification of tables

<table><tr><td>d</td><td>LT(d)</td><td>GT(d)</td></tr><tr><td>Product</td><td>-1</td><td>-0.333</td></tr><tr><td>Invoice</td><td>1</td><td>0.429</td></tr><tr><td>Customer</td><td>0</td><td>0.000</td></tr><tr><td>SalesRep</td><td>0</td><td>0.200</td></tr><tr><td>Office</td><td>0</td><td>-0.200</td></tr><tr><td>Region</td><td>-1</td><td>-0.600</td></tr></table>

Classification of data items

<table><tr><td>i</td><td>d</td><td>IsKey(i)</td><td>IsNumeric(i)</td><td>LC(i)</td><td>GC(i,d)</td></tr><tr><td>Product ID</td><td>Product</td><td>-1</td><td>1</td><td>0</td><td>-0.667</td></tr><tr><td>Product name</td><td>Product</td><td>-1</td><td>-1</td><td>-1</td><td>-1.000</td></tr><tr><td>Total sale</td><td>Invoice</td><td>1</td><td>1</td><td>1</td><td>0.429</td></tr></table>

<table><tr><td>Invoice ID</td><td>Invoice</td><td>-1</td><td>1</td><td>0</td><td>-0.286</td></tr><tr><td>Customer ID</td><td>Invoice</td><td>-1</td><td>1</td><td>0</td><td>-0.286</td></tr><tr><td>Product ID</td><td>Invoice</td><td>-1</td><td>1</td><td>0</td><td>-0.286</td></tr><tr><td>SalesRep ID</td><td>Invoice</td><td>-1</td><td>1</td><td>0</td><td>-0.286</td></tr><tr><td>Invoice date</td><td>Invoice</td><td>1</td><td>-1</td><td>0</td><td>-0.286</td></tr><tr><td>Customer ID</td><td>Customer</td><td>-1</td><td>1</td><td>0</td><td>-0.500</td></tr><tr><td>Customer site</td><td>Customer</td><td>1</td><td>-1</td><td>0</td><td>-0.500</td></tr><tr><td>Customer name</td><td>Customer</td><td>-1</td><td>-1</td><td>-1</td><td>-1.000</td></tr><tr><td>SalesRep ID</td><td>SalesRep</td><td>-1</td><td>1</td><td>0</td><td>-0.400</td></tr><tr><td>Office ID</td><td>SalesRep</td><td>-1</td><td>1</td><td>0</td><td>-0.400</td></tr><tr><td>SalesRep name</td><td>SalesRep</td><td>-1</td><td>-1</td><td>-1</td><td>-1.000</td></tr><tr><td>Office ID</td><td>Office</td><td>-1</td><td>1</td><td>0</td><td>-0.600</td></tr><tr><td>Region ID</td><td>Office</td><td>-1</td><td>1</td><td>0</td><td>-0.600</td></tr><tr><td>Office name</td><td>Office</td><td>-1</td><td>-1</td><td>-1</td><td>-1.000</td></tr><tr><td>Region ID</td><td>Region</td><td>-1</td><td>1</td><td>0</td><td>-0.800</td></tr></table>

## References

[1] G. Babin, Adaptiveness in Information Systems Integration, Rensselaer Polytechnic Institute, Aug. 1993.

[2] G. Babin, E. Audet, Sélection des indicateurs et des dimensions pour le forage d′Information, Expertise Informatique 3 (1) (1997).

[3] M. Bouziane, Metadata Modeling and Management, Rensselaer Polytechnic Institute, 1991.

[4] W. Cheung, G. Babin, A metadatabase-enabled executive information system (Part A): a flexible and adaptable architecture, Decision Support Systems 42 (2006) 1589–1598. doi:10.1016/j.dss.2006.01.005 (this issue).

[5] W. Cheung, C. Hsu, The model-assisted global query system for multiple databases in distributed enterprises, ACM Transactions on Information Systems 14 (4) (Oct. 1996).

[6] C. Hsu, The metadatabase project at Rensselaer, ACM SIGMOD Record 20 (4) (1991).

[7] C. Hsu, Enterprise Integration and Modeling: The Metadatabase Approach, Kluwer Academic Publishers, 1996.

[8] C. Hsu, G. Babin, A rule-oriented concurrent architecture to effect adaptiveness for integrated manufacturing enterprises, Proceedings of the International Conference on Industrial Engineering and Production Management, Brussels, Belgium, 1993.

[9] C. Hsu, A. Perry, M. Bouziane, W. Cheung, TSER: a data modeling system using the two-stage-entity-relationship approach, Proceedings of the 6th International Conference on Entity-Relationship Approach, New York, NY, 1987.

[10] C. Hsu, M. Bouziane, W. Cheung, J. Nogus, L. Rattner, L. Yee, A metadata system for information modeling and integration, Proceedings of the 1990 International Conference on Systems Integration, IEEE Computer Society, April 1990.

[11] C. Hsu, M. Bouziane, L. Rattner, L. Yee, Information resources management in heterogeneous distributed environments: a metadatabase approach, IEEE Transactions on Software Engineering 17 (6) (1991).

[12] C. Hsu, G. Babin, M. Bouziane, W. Cheung, L. Rattner, L. Yee, Metadatabase modeling for enterprise information integration, Journal of Systems Integration 2 (1) (1992).

[13] C. Hsu, Y. Tao, M. Bouziane, G. Babin, Paradigm translation in integrating manufacturing information using a meta-model: the TSER approach, Journal of Information Systems Engineering 1 (Sept. 1993).

[14] S.H. Hung, Expert versus novice use of the executive support systems: an empirical study, Information and Management 40 (2003).

[15] IBMS/TSER, Documentation: viu.eng.rpi.edu/ibmsv1\_1.exe, Software: viu.eng.rpi.edu/tser1.exe and viu.eng.rpi.edu/tser2.exe.

[16] E.A. Rundensteiner, A. Koeller, X. Zhang, Maintaining data warehouses over changing information sources, Communications of the ACM 43 (6) (2000 (June)).

[17] M.T. Warmouth, D. Yen, A detailed analysis of executive information systems, International Journal of Information Management 12 (3) (1992 (Sept.)).

[18] H.J. Watson, M.N. Frolick, Executive information systems: determining information requirements, Information Systems Management 9 (2) (1992 (Spring)).

[19] H.J. Watson, M.N. Frolick, Determining information requirements for an EIS, MIS Quarterly 17 (3) (1993 (Sept.)).

Waiman Cheung received his MBA and PhD in Decision Sciences and Engineering Systems from Rensselaer Polytechnic Institute. He is currently a Professor and Associate Dean of the Faculty of Business Administration, The Chinese University of Hong Kong, where he teaches both graduate and undergraduate MIS courses. Dr. Cheung’s current research interests are e-business, cargo logistics and supply chain management. He is also the director of the Li & Fung Institute of Supply Chain Management and Logistics in the University. Dr. Cheung has contributed articles to ACM Transactions on Information Systems, Decision Sciences, IEEE Transactions on Systems, Man and Cybernetics, Annual of OR, Decision Support Systems, Information & Management, Journal of Intelligent Manufacturing, etc.

Gilbert Babin received his B.Sc. and M.Sc. from Université de Montréal (Canada) in 1986 and 1989, respectively. He then completed his doctoral studies in 1993 at Rensselaer Polytechnic Institute (Troy, New York, USA), where he studied integration approaches for heterogeneous, distributed systems. His doctoral thesis earned him the Del and Ruth Karger Dissertation Award in 1995. He worked at the Computer Science department at Université Laval from 1993 to 2000. Since then, he then joined the Information Technologies Department at HEC-Montreal (Canada) as Associate Professor. Gilbert Babin is a member of ACM and the Computer Society of the IEEE. He has more than 45 papers published in refereed journals and conferences. His research interests revolve around distributed systems and approaches to integrate them.
