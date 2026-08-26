---
otero_id: 5808
otero_key: "5QQGPTGQ"
title: "Expediting analytical databases with columnar approach"
authors: "Nenad Jukic; Boris Jukic; Abhishek Sharma; Svetlozar Nestorov; Benjamin Korallus Arnold"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.12.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Nenad Jukic <sup>a,</sup>⁎, Boris Jukic <sup>b</sup>, Abhishek Sharma <sup>a</sup>, Svetlozar Nestorov <sup>a</sup>, Benjamin Korallus Arnold <sup>c</sup>

<sup>a</sup> Loyola University Chicago, Quinlan School of Business, 16 E Pearson, 60611 Chicago, IL, United States

<sup>b</sup> Clarkson University, School of Business, Bertrand H. Snell Hall, Potsdam NY 13699-5790, United States

<sup>c</sup> University of Chicago, Graham School of Continuing Liberal and Professional Studies, 450 North Cityfront Plaza Drive, Chicago, IL 60611, United States

## a r t i c l e i n f o

Article history: Received 31 December 2015 Received in revised form 22 December 2016 Accepted 24 December 2016 Available online 6 January 2017

Keywords: Data warehouses Decision support Big data Performance ETL Columnar databases

## a b s t r a c t

The approaches and discussions given in this paper offer applicable solutions for a number of scenarios taking place in the contemporary world that are dealing with performance issues in development and use of analytical databases for the support of both tactical and strategic decision making. The paper introduces a novel method for expediting the development and use of analytical databases that combines columnar database technology with an approach based on denormalizing data tables for analysis and decision support. This method improves the feasibility and quality of tactical decision making by making critical information more readily available. It also improves the quality of longer term strategic decision making by widening the range of feasible queries against the vast amounts of available information. The advantages include the improvements in the performance of the ETL process (the most common time-consuming bottleneck in most implementations of data warehousing for quality decision support) and in the performance of the individual analytical queries. These improvements in the critical decision support infrastructure are achieved without resulting in insurmountable storage-size increase requirements. The efficiencies and advantages of the introduced approach are illustrated by showing the application in two relevant real-world cases.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

The importance of data in all aspects of business, science and government continues to grow. Data analysis underlies most if not all of the important decisions taken by corporate, academic and political leaders. Current technologies make available to analysts and managers a vast amount of structured and unstructured data from a variety of sources [1]. With the digitization of world commerce, the emergence of big data and the advance of analytical technologies, organizations have extraordinary opportunities to differentiate themselves through analytics [2]. Analytical processes that used to require month, days, or hours have been reduced to minutes, seconds, and fractions of seconds, with shorter processing times leading to higher expectations [3]. In fact, data and its analysis is increasingly required not only to guide and direct strategic plans but also to justify and explain tactical actions. In some ways, using analytics for these immediate operational needs can be more difficult than crafting long-term strategies. Whereas future strategies are typically iterated over time, operational decisions require precise and accurate insights to be available much more quickly: hence, the need for analytics speed [2]. This requirement, coupled with the explosion of data everywhere has led to the today's trend in which timely analytics capabilities are a must-have for many organizations.

As a result, firms are increasingly demanding immediate access to internal corporate data and external data, from an ever-growing list of sources, to develop insights and to generate actionable responses that produce measurable results in real-time [4]. To better harness the power of their own data, many firms have invested in data warehousing technology [5]. However, the increasing reliance on data analysis for everyday decisions has put a strain on the standard data warehousing technology. In particular the ETL (extract, transform, and load) process that brings data from the operational databases to the analytical data warehouse is required to run faster and more frequently than ever in order to make the most recent operational data available for analysis. For example, for many businesses detecting trends and patterns in their retail stores and supply chains is now a daily if not an hourly process that has critical implications on the bottom line [6].

Finally, the Big Data trend also plays a significant role in the increasing demands on the ETL process as many companies and organizations are shifting to data-driven decisions across all management levels. Capturing and processing data from a multitude of sensors [7] is helping companies include many external factors such as weather and traffic in their data warehouses and improve their analysis of customer patterns and trends.

In this paper, we examine a novel approach to expediting the ETL process for data warehousing by combining two key data warehousing methodologies that can enhance the ability to use massive amounts of data for more timely and comprehensive decision support and analysis. The first methodology is based on reducing the design complexity of the conceptual data model for the data warehouses by a process of denormalization of star schemas (described in detail in Section 5.1). The second methodology of our approach is based on the use of socalled columnar databases (described in detail in Section 4). Both of these methodologies have been widely used in the practice as well as academic research, however the theoretical foundations and implications of combining these methodologies, as well as practical cases based on the approach that combines them, have not so far been examined in details and presented in academic papers. In this paper, we offer a thorough examination of the synergies of the combination of denormalization and columnar databases, and analyze the requirements that justify the usage of this combination in the context of our proposed model, which we validate with a series of computational experiments. We also present two real-world projects that have taken advantage of this novel approach and describe the concrete benefits that include significantly faster ETL times, as well as improved performance of analytical queries. These benefits represent critical conditions for enabling wider use of massive amounts of data for timely decision support in near real-time tactical scenarios as well as in strategic decision making.

The key novel contribution of this approach is identifying a standard and widely accepted process of generation and usage of surrogate keys (to be explained in detail in the section below) as one of the critical bottlenecks of the ETL process and showing how our proposed approach eliminates the need for their utilization, resulting in better performance of large scale analytical depositories for timely decision making.

Another contribution of our paper is its focus on the logical implementation of the columnar database approach, and how it improves the utilization of large data depositories for decision making. There have been extensive reviews of the design and performance of column-oriented databases [8–11] for both operational and analytical databases. However, most of the articles up to the present point are focused on the physical implementation of the standard database operations and the optimal design of physical query plans. In fact, in many articles, the authors emphasized that the logical design of the database does not change and thus does not warrant any special attention. In this paper, we consider the interplay between the physical implementation of columnar databases and the logical implementation of the analytical database data models (star schemas) as a unified structure for comprehensive analytics contained within a single (denormalized) table.

The rest of this paper is organized as following. In Section 2 we give a brief overview of analytical databases, including the description of surrogate keys and slowly changing dimensions. In Section 3 we present a discussion of the role of analytical databases in the context of Big Data analytics. In Section 4 we give a brief overview of columnar databases. Section 5 gives a detailed description and discussion of the introduced columnar approach for analytical databases, providing a model based framework for performance evaluation of our approach, validated by a set of computational experiments. Section 6 describes two real-world implementations of the introduced approach, further illustrating its feasibility. And finally, Section 7 offers concluding remarks.

## 2. Analytical databases

Analytical databases, such as data warehouses and data marts, are databases that store and maintain analytical data separately from operational (transaction-oriented) databases. In the 1990′s, it has gradually became apparent that analytical databases, designed to be used specifically for decision support in the context of organizational analytics, should be deployed logically and physically separately from day-today operational systems. Using this approach, the lengthy, and often unpredictable, business intelligence queries would not spoil the response time of standard operational systems. Additionally, data warehouses are based on the recognition that the conventional query optimization and execution engines do not work well on the large sets of analytical data. Hence, extension or modifications applied on separate analytical systems are required to achieve good performance [12].

Fig. 1 shows a high-level view of the architecture of an analytical database system. The analytical data in a corporate data warehouse or data mart is periodically retrieved from various data sources. Typical data sources are internal corporate operational databases that contain analytically-useful data, such as sales-transactions databases, marketing databases and HR databases. Other data sources can include external data, such as demographics data or stock-market data, and, increasingly, Big Data sources, such as machine logs, sensor data of every imaginable kind, data generated by social networks and blogs [13], etc. These extremely large amounts of unstructured and semi-structured data can be relatively straightforwardly processed using technologies such as Hadoop [14] into useful structured information.

The data from operational data sources, external sources and other repositories of interest is brought into the data warehouse or data mart via the process of extraction, transformation and load (ETL). The ETL process is responsible for the extraction of data from sources, their cleansing, customization and insertion into a data warehouse [15]. The ETL infrastructure extracts analytically useful data from the chosen data sources, transforms the extracted data so that it conforms to the structure of the data warehouse or data mart (while ensuring the completeness, consistency and other aspects of quality of the transformed data) and then loads the data into the data warehouse or data mart. After it is loaded, this data explicitly and implicitly reflects customer patterns and trends, business practices, organizational strategies, financial conditions, know-how, and other knowledge of great value to the organization [16].

Analytical databases are modeled and structured differently than operational databases. Fig. 2 shows an example of a database modeled for operational use, with larger number of tables whereby individual tables have smaller column count. Fig. 3 shows an example of an analytical database that contains the same data as the operational database shown in Fig. 2, but it is modeled differently, with model containing a smaller number of tables whereby individual tables have larger column count.

Typical operational database relational schema contains a number of connected tables, as shown in Fig. 2. As illustrated by this figure, operational databases are structured and modeled as so-called normalized relational databases, whereby the main goal is to minimize data redundancy, i.e. eliminate instances of storing of the same data more than once. If you observe data values in the bottom part of Fig. 2, you will notice that, for example, the information for each region is listed only once in the database. The only region values that are listed more than once are the primary key values (‘C’ and ‘T’) used as foreign key in the table Store in order to connect each store with its region. Minimizing redundancy enables efficiency when data is updated. For example, if the population of Chicagoland region changes from 8 million to 9 million, that change has to be made at only one place in the database. Operational databases, by the nature of their intended use, will be frequently exposed to all four standard socalled CRUD operations (Create new records, Read existing records, Update existing records and Delete existing records). Having the structure that causes the same record stored in more than only place (a so-called non-normalized database containing redundant data) will result in the same record having to be exposed to more than one instance of the CRUD operations, which may lead to mistakes and data inconsistencies caused by so-called insertion, update and deletion anomalies. It is for those reasons that the presence of redundant data is avoided by design in operational databases.

![](/api/attachments/5QQGPTGQ/fulltext/images/eda3fb29e62955a9ef3fe04bcb20de378651a8b6e0cad69e7c0a7b6b6b5f4a63.jpg)  
Fig. 1. Analytical database architecture.

![](/api/attachments/5QQGPTGQ/fulltext/images/96ac846b922d0214e0a094ec270f8ecab2b98cc25c6909661b129379be95bf18.jpg)

<table><tr><td colspan="3">Region</td><td colspan="6">Product</td><td colspan="2">Vendor</td></tr><tr><td>RegionID</td><td>RegionName</td><td>RegionPopulation</td><td>ProductID</td><td>ProductName</td><td colspan="2">ProductPric VendorID</td><td>CategoryID</td><td></td><td>VendorID</td><td>VendorName</td></tr><tr><td>C</td><td>Chicagoland</td><td>8,000,000</td><td>1X1</td><td>Zzz Bag</td><td>$100</td><td>PG</td><td>CP</td><td></td><td>PG</td><td>Pacifica Gear</td></tr><tr><td>T</td><td>Tristate</td><td>2,000,000</td><td>2X2</td><td>Easy Boot</td><td>$100</td><td>MK</td><td>FW</td><td></td><td>MK</td><td>Mountain King</td></tr><tr><td></td><td></td><td></td><td>3X3</td><td>Cosy Sock</td><td>$15</td><td>MK</td><td>FW</td><td></td><td></td><td></td></tr><tr><td>Store</td><td></td><td></td><td>4X4</td><td>Dura Boot</td><td>$90</td><td>PG</td><td>FW</td><td></td><td>Category</td><td></td></tr><tr><td>StoreID</td><td>StoreZip</td><td>RegionID</td><td>5X5</td><td>Tiny Tent</td><td>$100</td><td>MK</td><td>CP</td><td></td><td>CategoryID</td><td>CategoryName</td></tr><tr><td>S1</td><td>60600</td><td>C</td><td>6X6</td><td>Biggy Tent</td><td>$250</td><td>MK</td><td>CP</td><td></td><td>CP</td><td>Camping</td></tr><tr><td>S2</td><td>60605</td><td>C</td><td></td><td></td><td></td><td></td><td></td><td></td><td>FW</td><td>Footwear</td></tr><tr><td>S3</td><td>35400</td><td>T</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td colspan="3">SoldVia</td><td colspan="3">Customer</td></tr><tr><td></td><td colspan="4">SalesTransaction</td><td>ProductID</td><td>TID</td><td>NoOfItems</td><td>CustomerID</td><td>CustomerName</td><td>CustomerZip</td></tr><tr><td></td><td>TID</td><td>CustomerID</td><td>StoreID</td><td>TDate</td><td>1X1</td><td>T111</td><td>1</td><td>1-2-333</td><td>Tina</td><td>60137</td></tr><tr><td></td><td>T111</td><td>1-2-333</td><td>S1</td><td>1-Jan-2015</td><td>2X2</td><td>T222</td><td>1</td><td>2-3-444</td><td>Tony</td><td>60611</td></tr><tr><td></td><td>T222</td><td>2-3-444</td><td>S2</td><td>1-Jan-2015</td><td>3X3</td><td>T333</td><td>5</td><td>3-4-555</td><td>Pam</td><td>35401</td></tr><tr><td></td><td>T333</td><td>1-2-333</td><td>S3</td><td>2-Jan-2015</td><td>1X1</td><td>T333</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td>T444</td><td>3-4-555</td><td>S3</td><td>2-Jan-2015</td><td>4X4</td><td>T444</td><td>1</td><td></td><td></td><td></td></tr><tr><td></td><td>T555</td><td>2-3-444</td><td>S3</td><td>2-Jan-2015</td><td>2X2</td><td>T444</td><td>2</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>4X4</td><td>T555</td><td>4</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>5X5</td><td>T555</td><td>2</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>6X6</td><td>T555</td><td>1</td><td></td><td></td><td></td></tr></table>

Fig. 2. Example normalized relational operational database (relational schema and sample data)

The main goal of the design of analytical databases is the speed and simplicity of data retrieval for a variety of decision making purposes. Therefore, in contrast to operational databases, analytical databases are exposed regularly to only Read (cRud) operations, and the presence of redundant data does not typically cause quality and consistency problems. One of the most common used techniques for modeling analytical databases is dimensional modeling [17]. Analytical databases are created for the analysis of one (in case of data marts) or more (in case of data warehouses) specific business subject areas. Deciding on one or more particular subjects of analysis, such as sales, returns, cost, or profit, is a first-step in the process of dimensional modeling. Once a subject of analysis is chosen, the dimensional modeling technique is used to create a so-called star schema [18] containing two types of tables: dimensions and facts.

Dimension tables contain descriptions of the business, organization, or enterprise to which the subject of analysis belongs. This information provides a basis for analysis of the subject based on the grouping criteria contained in the dimensions' attributes. For example, if the subject of the business analysis is sales, it can be analyzed by criteria such as product category, region name, region population, etc.

Fact tables contain measures related to the subject of analysis. In addition, fact tables contain foreign keys associating them with dimension tables. The measures in the fact tables are typically numeric and are intended for quantitative analysis using applicable computational methods. For example, if the subject of the business analysis is sales, one of the measures in the fact table sales could be the sale's dollar amount. The sale amounts can be calculated and recalculated using different mathematical functions across various dimension columns. For example, the total and average sale can be calculated per region, product category, etc.

![](/api/attachments/5QQGPTGQ/fulltext/images/fd530a0bec748b75840070a3bc2e0a4b269a5e1d315af8d8aeff989cb9588228.jpg)

<table><tr><td colspan="8">CALENDAR Dimension</td><td colspan="6">PRODUCT Dimension</td></tr><tr><td colspan="2">Calendar</td><td rowspan="2">Dayof Week</td><td rowspan="2">Dayof Month</td><td rowspan="2">Month</td><td rowspan="2">Qtr</td><td rowspan="2">Year</td><td rowspan="8"></td><td colspan="2">Product</td><td rowspan="2">Product Name</td><td rowspan="2">Product Price</td><td rowspan="2">Product Vendor</td><td rowspan="2">Product Category Name</td></tr><tr><td>Key</td><td>Full Date</td><td>Key</td><td>ProductID</td></tr><tr><td>1</td><td>1/1/2015</td><td>Thursday</td><td>1</td><td>January</td><td>Q1</td><td>2015</td><td>1</td><td>1X1</td><td>Zzz Bag</td><td>$100</td><td>Pacifica Gear</td><td>Camping</td></tr><tr><td>2</td><td>1/2/2015</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>2</td><td>2X2</td><td>Easy Boot</td><td>$70</td><td>Mountain King</td><td>Footwear</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td><td>3X3</td><td>Cosy Sock</td><td>$15</td><td>Mountain King</td><td>Footwear</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4</td><td>4X4</td><td>Dura Boot</td><td>$90</td><td>Pacifica Gear</td><td>Footwear</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5</td><td>5X5</td><td>Tiny Tent</td><td>$150</td><td>Mountain King</td><td>Camping</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6</td><td>6X6</td><td>Biggy Tent</td><td>$250</td><td>Mountain King</td><td>Camping</td></tr><tr><td colspan="8">STORE Dimension</td><td colspan="6">CUSTOMER Dimension</td></tr><tr><td colspan="2">Store</td><td></td><td rowspan="2">Store Region Name</td><td rowspan="2">Store Region Population</td><td rowspan="2"></td><td rowspan="2"></td><td></td><td rowspan="2">CustomerKey</td><td rowspan="2">Customer ID</td><td rowspan="2">Customer Name</td><td rowspan="2">Customer Zip</td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>Key</td><td>StoreID</td><td>StoreZip</td><td></td></tr><tr><td>1</td><td>S1</td><td>60600</td><td>Chicagoland</td><td>8,000,000</td><td></td><td></td><td></td><td>1</td><td>1-2-333</td><td>Tina</td><td>60137</td><td></td><td></td></tr><tr><td>2</td><td>S2</td><td>60605</td><td>Chicagoland</td><td>8,000,000</td><td></td><td></td><td></td><td>2</td><td>2-3-444</td><td>Tony</td><td>60611</td><td></td><td></td></tr><tr><td>3</td><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td></td><td></td><td></td><td>3</td><td>3-4-555</td><td>Pam</td><td>35401</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td colspan="3">SALES Fact table</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>Calendar Key</td><td>Store Key</td><td>Product Key</td><td>Customer Key</td><td>TID</td><td>Dollars Sold</td><td>Units Sold</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>T111</td><td>$100</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>1</td><td>2</td><td>2</td><td>2</td><td>T222</td><td>$100</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>3</td><td>1</td><td>T333</td><td>$75</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>1</td><td>1</td><td>T333</td><td>$100</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>4</td><td>3</td><td>T444</td><td>$90</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>2</td><td>3</td><td>T444</td><td>$200</td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>4</td><td>2</td><td>T555</td><td>$360</td><td>4</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>5</td><td>2</td><td>T555</td><td>$200</td><td>2</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>2</td><td>3</td><td>6</td><td>2</td><td>T555</td><td>$250</td><td>1</td><td></td><td></td><td></td><td></td></tr></table>

Fig. 3. Example dimensionally modeled data mart (star schema and sample data).

Fig. 3 shows a dimensionally modeled data mart containing the same information as the operational database shown in Fig. 2. Based on the operational database shown in Fig. 2, dimensional modeling technique is used to design an analytical database shown in Fig. 3, whose subject of analysis is sales.

As stated above, unlike operational databases, analytical databases are not modeled to eliminate redundancy. For example, note that the same information about regions (name and population of the Chicagoland region) can repeat multiple times in Fig. 3. In operational databases, end-users are routinely engaged in updating of information and, in such cases, redundant information represents a hindrance. By contrast, the end-users of analytical databases engage in retrievalsonly, as all updates are done as part of the ETL process. Therefore redundancy is not an issue that adversely affects the end-users. In fact, repeating the same information more than once makes data analysis by the end users easier and more convenient. For example, if an analyst needs to analyze in detail the product information, all of the information about the products, including their vendors and categories, is already grouped and listed in one table.

Typically, in a star schema all dimension tables are given a simple, non-composite system-generated key, also called a surrogate key [17]. In Fig. 3, the dimension CALENDAR has a surrogate key CalendarKey, dimension PRODUCT has a surrogate key ProductKey, dimension STORE has a surrogate key StoreKey, and dimension CUSTOMER has a surrogate key CustomerKey. Values for those keys, as shown in Fig. 3, are auto-increment integer values. The purpose of surrogate key is to add to each dimension a new column that serves as a primary key within the dimensional model instead of the operational key. For example, instead of using the primary key ProductID from the PRODUCT table in the operational database as the primary key of the PRODUCT dimension, a new surrogate key column ProductKey is created. One of the main reasons for creating a surrogate primary key such as ProductKey, and not using the operational primary key such as ProductID as a primary key of the dimension, is to enable the handling of so called slowly changing dimensions.

A typical dimension in a star schema contains either attributes whose values do not change (or change extremely rarely) such as store size and customer gender, or attributes whose values change occasionally and sporadically over time [17,19], such as customer zip and employee salary. A dimension that contains attributes whose values can change is often referred to as a slowly changing dimension. There are several different approaches to dealing with slowly changing dimensions, such as Type 0, Type 1, Type 2, Type 3, Type 4, etc. For brevity and simplicity we will focus here on two most basic and most commonly used approaches: Type 1 and Type 2.

Type 1 is a simple approach, used mostly when a change in a dimension is the result of a need to correct an error. The Type 1 approach simply changes the value in the dimension's record, where the new value replaces the old value. If the Type 1 approach is used, no history is preserved which, in cases when the original value is erroneous, is not a loss of information. The following simple example of a table representing a slowly changing dimension illustrates the Type 1 approach.

STORE

<table><tr><td>StoreKey</td><td>StoreID</td><td>StoreZip</td><td>StoreRegionName</td><td>StoreRegionPopulation</td></tr><tr><td>1</td><td>S1</td><td>60600</td><td>Chicagoland</td><td>8,000,000</td></tr><tr><td>2</td><td>S2</td><td>60605</td><td>Chicagoland</td><td>8,000,000</td></tr><tr><td>3</td><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td></tr></table>

Assume that the Tristate population value has to be changed from 2,000,000 to 3,000,000. If the Type 1 approach is applied, the result would be the following:

STORE

<table><tr><td>StoreKey</td><td>StoreID</td><td>StoreZip</td><td>StoreRegionName</td><td>StoreRegionPopulation</td></tr><tr><td>1</td><td>S1</td><td>60,600</td><td>Chicagoland</td><td>8,000,000</td></tr><tr><td>2</td><td>S2</td><td>60,605</td><td>Chicagoland</td><td>8,000,000</td></tr><tr><td>3</td><td>S3</td><td>35,400</td><td>Tristate</td><td>3,000,000</td></tr></table>

The previous value for the StoreRegionPopulation column in the third row was simply replaced by the new value. The Type 1 approach would be appropriate in this scenario if Tristate population was 3,000,000 from the outset, but was incorrectly recorded as 2,000,000 and it is now corrected.

Type 2 is an approach used in cases when history should be preserved. The Type 2 approach is the most commonly used approach for dealing with slowly changing dimension. It enables straightforward handling of multiple changes of dimension attributes values.

The Type 2 approach creates a new additional dimension record using a new value for the surrogate key every time a value in a dimension record changes. The same example used to illustrate the Type 1 approach will be used to illustrate the Type 2 approach.

Assume that the Tristate population value has to be changed from 2,000,000 to 3,000,000. If the Type 2 approach is applied, the result would be the following:

STORE.

<table><tr><td>StoreKey</td><td>StoreID</td><td>StoreZip</td><td>StoreRegionName</td><td>StoreRegionPopulation</td></tr><tr><td>1</td><td>S1</td><td>60,600</td><td>Chicagoland</td><td>8,000,000</td></tr><tr><td>2</td><td>S2</td><td>60,605</td><td>Chicagoland</td><td>8,000,000</td></tr><tr><td>3</td><td>S3</td><td>35,400</td><td>Tristate</td><td>2,000,000</td></tr><tr><td>4</td><td>S3</td><td>35,400</td><td>Tristate</td><td>3,000,000</td></tr></table>

A new record containing a new value for Tristate population is created, while the old record containing Tristate previous population value is retained. The Type 2 approach would be appropriate in this scenario if

Tristate population was indeed 2,000,000 and then it changed to 3,000,000.

Note the important role of surrogate keys in the Type 2 approach. Due to the multiple occurrences of records with the same operational key value (same StoreID value in the 3rd and 4th records), it is the surrogate key that provides a unique identifier for each row in the dimension table, while the original operational key is now used to identify the multiple records that refer to the same real world entity instance. If we wanted to analyze the purchase patterns in store S3, we would look at all sales fact records connected to all dimension records whose StoreID is S3. However, if we wanted to look at the purchase patterns in regions with the population of 2,500,000 or higher, we would combine the sales in the fact table connected to the 4th record with the sales connected to the 1st and 2nd record in the dimension STORE. In other words, we would only include purchases in store S3 after its region's population increased from 2,000,000 to 3,000,000.

Following this brief summary of some of the key concepts related to analytical databases, and before we consider the characteristics of columnar databases, we will present a quick discussion of the role of analytical databases with the rising eminence of Big Data analytics.

## 3. ETL process and data warehousing in the era of big data

With so much being currently debated about the evolution of data analytics infrastructure, we believe that it is important to address the ongoing discussion on the future relevance of ETL process and Data Warehousing in the era of Big Data. The concept of Data Lake has gained prominence recently, primarily driven by the need for increased agility and accessibility for data analysis [20]. Data lakes are not dependent on predefined logical schema as data warehouses and data marts are (so called schema-on-write approach). Rather, they support a concept known as late binding, or schema on read, in which users build custom schema into their queries [21]. In essence, these less formal larger depositories of analytical data, typically implemented in Hadoop, are based on concept of storing all the data in a very simple and very flexible key-value pair structure which enables analysts to create any logical schema on the fly at the point of data analysis (so called schema-onread). This approach to managing large amounts of diverse data for analysis and decision support, provides data scientists who need immediate access to all data to quickly build data-driven solutions and create analyses without needing to wait for the formalized data warehousing and BI teams to go through the rigors imposed by corporate IT [22]. Basically, integrating data involves fewer steps because data lakes don't enforce a rigid metadata schema as do relational data warehouses [21, 23].

However, this does not mean that the Data Warehouses as primary depositories of enterprise-wide historical data and the ETL process for populating them properly are on their way out. As stated in [24]: “While double-digit percentages of CIOs used to dream of replacing their enterprise data warehouses with Hadoop data repositories, that number steadily falls every year”. Many recent articles [20,22,25–30] convey the emerging realization that the data lake approach (as a catch all term for all unstructured data repositories approach based on Hadoop, NoSQL, “new” SQL etc.) cannot fulfill they key data warehouse functionalities and that these two fundamentally different approaches are not meant to replace one another but are rather complementary to each other. As the amount of structured and unstructured data increase, data lake implementations may be needed to complement the enterprise data warehouse in a variety of organizations. The contents and structure of the data lake will be determined by the amount of data and analytics which is desired that cannot be stored and processed in the conventional data warehouse architecture. The organizations may implement a BI ecosystem – a logical data warehouse in Gartner terminology – with a variety of technologies and tools, including a data lake [31].

For large, irregular datasets or for sets of data that require preliminary analytic processing, Hadoop-based data lake is the right choice to build either a set of data to be queried and analyzed immediately, (and eventually processed and loaded into a data warehouse). For data that has a well-known and controlled structure and sources, where the transformations are always the same and the target is similarly well known and stable, ETL is the proper and necessary choice. Plus, ETL can also be used to extract subsets of data from data lakes and load them into a data warehouse for regular query, reporting, and analysis [29]. In other words, structured data doesn't go away, nor does the need for doing analytics (descriptive, predictive, or prescriptive) on that type of data. An analytics engine that was created and tuned for structured data will continue to be the best place to do such analytics. Very relevant and useful data exploration can be performed in Hadoop, but organizations will still need daily/weekly/monthly reports and executive dashboards, all needing to be produced within shrinking time windows, that are all fueled by structured data [25]. At its core, the data warehouse integrates critical and valuable enterprise data that is not found in big data sources and that continues to be the primary data resource for descriptive, prescriptive and decision analytics. It serves as corporate memory, collecting the body of history that makes time-series and trend analysis possible [26]. The data warehouse itself should stay a logical representation of clean, vetted data that users at various levels can use to make decisions. Without a data warehouse, decision-makers operate by the seat of their pants, making critical decisions based on inaccurate or no data at all [31].

To conclude this discussion, data lake based analysis is useful for data wrangling as a step preceding the formal ETL process and, in some cases, spontaneous analytics, while data warehouse is best at functions for which it has initially been proposed and has been deployed in the past 20 years or so, namely, as a depository of consistent, structured, stable definitive “version of record” of organizational history to be used for reporting, dashboards, BI etc. Data warehouses make powerful use of structured, relational data, whereas Hadoop-based data lakes excel at managing unstructured, semi-structured or log data that classic data warehouses can't handle well. As stated in [32] “The two make an attractive odd couple”.

Following this brief overview of current discussions about the role of analytical databases. next we focus on the characteristics of columnar databases.

## 4. Columnar databases

In this section we will first give a brief overview of row and columnar orientation of databases. We will then elaborate further on the characteristics of columnar databases that are relevant for the approach we will introduce in the subsequent section.

## 4.1. Row and columnar orientation

Operational and analytical databases are commonly hosted by relational database systems (RDBMS). Two most common approaches used by RDBMSs to store tables are the row-oriented approach and the columnar approach. Here we give a simplified example illustrating these two approaches.

If the row-oriented approach is used, the table Product shown in Fig. 2 would be stored as a sequence of delimited rows:

Retrieval of the data from a row-oriented table, involves bringing rows of data from the disk into the memory, and then performing operations on the retrieved rows. For example, a query that displays, for each product, the name of the product and its price would retrieve all complete rows from the stored table Product from the hard drive into the memory and then display only the needed information in the result, i.e. values for Product Name and Product Price.

If the columnar approach is used, table Product shown in Fig. 2 would be stored as a sequence of delimited columns:

```csv
1X1, 2X2, 3X3, 4 × 4, 5X5, 6X6;
Zzz Bag, Easy Boot, Cosy Sock, Dura Boot, Tiny Tent, Biggy Tent;
$100, $100, $15, $90, $100, $250;
PG, MK, MK, PG, MK, MK;
CP, FW, FW, FW, CP, CP;
```

Retrieval of the data from a column-oriented table, involves bringing columns of data from the hard drive into the memory. For example, a query that displays for each product the name of the product and its price, would simply retrieve columns Product Name and Product Price from the hard drive into the memory and then display the result. In other words substantially less data would have to be brought from the hard drive into the memory then if a row-based approach was used. Consequently, the query would run faster.

Not all database operations experience improvement in performance in a columnar scenario. In general, columnar approach is more efficient in cases when selected columns are requested from very large tables, which is a typical scenario in the use of analytical databases. Row approach is more efficient when a large portion of columns from selected rows is requested, a typical scenario in the use of operational databases, such as looking up all or most of the details of individual or small number of records or creating comprehensive reports on all records involving all or most of their columns. These performance differences will be discussed more formally and in greater detail in the next section. Also columnar databases do not perform as well as row-oriented databases when it comes to update (insert, delete, modify) operations. Hence, columnar approach is usually not applied in operational databases. In general, row-oriented approach is prevalent for operational databases, whereas columnar approach is common for analytical databases [33].

## 4.2. Key columnar concepts

As we just discussed, columnar approach implements vertical partitioning of data tables. The key benefit of vertical partitioning comes in terms of efficiency of data transfer from disk to memory and from memory to CPU registers. When only certain columns are needed in processing, significantly less data has to undertake these transfers. Since vertical partitioning stores each column separately on disk, they can be retrieved separately without the need to retrieve complete rows. But, because vertical partitioning stores each column separately on disk, it requires a row identifier with every column. This row identifier cannot be explicit because that would bloat the data (by adding an identi er “column” for each individual column) and lead to counterproductive inefficiencies in the processing. Instead a virtual (implicit) identifier is utilized, equivalent to the position of the row in a given column. The implied challenge is that the position of rows in the table needs to remain consistent across all stored columns. This is a big problem for operational databases that undergo frequent modifications, deletions and insertions, but not a major issue for append-mostly databases like data warehouses where new rows are appended to existing tables in a scheduled fashion and the existing rows typically never change [12].

The following example illustrates the concept of virtual identifier. The rows of the table Product shown in Fig. 2 would have a virtual

identifier, equivalent to the position of the row, as depicted by italicized number:

<table><tr><td>1X1, Zzz Bag, $100, PG, CP,</td><td>1</td></tr><tr><td>2X2, Easy Boot, $100, MK, FW,</td><td>2</td></tr><tr><td>3X3, Cosy Sock, $15, MK, FW,</td><td>3</td></tr><tr><td>4X4, Dura Boot, $90, PG, FW,</td><td>4</td></tr><tr><td>5X5, Tiny Tent, $100, MK, CP,</td><td>5</td></tr><tr><td>6X6, Biggy Tent, $250, MK, CP,</td><td>6</td></tr></table>

Note that these virtual identifiers instead of being stored are simply calculated as a row position of each record. In the example above the value 1X1 is first in line so its VID is 1, the value 2X2 is second in line, so it VID is 2, and so on. These identifiers would be used in the columnar organization of the table Product as shown below, where the second value in each pair is not a stored value but rather an actual row position:

[1X1, 1][2X2, 2][3X3, 3][4 × 4, 4][5X5, 5][6X6, 6]; [Zzz Bag, 1][Easy Boot, 2][Cosy Sock, 3][Dura Boot, 4][Tiny Tent, 5][Biggy Tent, 6]; [\$100, 1][S100, 2][\$15, 3][\$90, 4][\$100, 5][\$250, 6]; [PG, 1][MK, 2][MK, 3][PG, 4][MK, 5][MK, 6]; [CP, 1][FW, 2][FW, 3][FW, 4][CP, 5][CP, 6];

Since data is stored in a columnar format, columns can be individually compressed with various kinds of data compression algorithms. Data compression as means for reducing the number of bits needed to store or transmit data is well established area of computer science and the methods that are most applicable in the scenario we discuss in this paper include Run-length encoding (RLE), LZ77, or Huffman coding (Zlib). The overview and detailed description of these methods is available in many scientific publications [34–38]. When properly implemented and executed, the column specific compression not only shrinks data size on the disk but also improves performance due to smaller amount of input output operations on a physical disk (disk I/ O). Simply put, compressed data is less voluminous and therefore the I/O process is shorter.

While discussing compression of tables in columnar-oriented databases, it is important to distinguish between high-cardinality data columns and low-cardinality data columns. High-cardinality data columns have a high percentage of different separate values in them, where low-cardinality data columns are columns where few distinct values repeat multiple times. In the example above columns containing Product ID and Product Name are high-cardinality columns because there is no repetition of any values, while the other columns are lower-cardinality columns because they contain values that are repeating. Columns with low cardinality data can be compressed at very high ratios. For example, run-length encoding method looks for batches of the same value in a given column and converts them into an efficient singular representation. Therefore, this method is very efficient for columns that are sorted or that have large consecutive batches of the same value. These batches are compressed by converting each individual batch into an ordered triplet with first member representing the value common in the batch, the second member representing the start position of the batch, and the third member representing the length of the batch. For example, table PRODUCT could have a large number of records but the column Vendor in table PRODUCT could contain significantly fewer distinct values. The compressed sorted Vendor column would therefore contain significantly fewer records than the original table PRODUCT, thereby significantly reducing the time needed for disk I/O for that column.

Projection is an intentional duplication of a subset of columns from an original table sorted by a specific column to achieve a better query performance. The dataset for each projection is sorted by a particular table column that is positioned as the first column of the table. The order of the remaining columns is such that the lowest-cardinality column comes first and highest-cardinality column is last, within a

particular hierarchy (i.e. hierarchical attribute grouping) of a dimension. For example, in table STORE shown in Fig. 3 the hierarchy is Store Region (Name and Population) → Store Zip → Store (ID and Key) because store region name will have multiple zip codes and each zip code can have multiple stores in it. In this case, sorting will be done by region name, zip code, and store name. Because there are no additional hierarchies, no additional projections have to be made. However, table PROD-UCT shown in Fig. 2 has three distinct hierarchies: Product Vendor → Product, Product Category → Product, and Product Price → Product, and for each of these hierarchies a projection will be made as following:

<table><tr><td>Projection 1: by Product Vendor</td><td>Projection 2: by Product Category</td><td>Projection 3: by Product Price</td></tr><tr><td>MK, FW, $15, 3X3, Cosy Sock</td><td>CP, MK, $100, 5X5, Tiny Tent</td><td>$15, MK, FW, 3X3, Cosy Sock</td></tr><tr><td>MK, FW, $100, 2X2, Easy Boot</td><td>CP, MK, $250, 6X6, Biggy Tent</td><td>$90, PG, FW, 4X4, Dura Boot</td></tr><tr><td>MK, CP, $100, 5X5, Tiny Tent</td><td>CP, PG, $100, 1X1, Zzz Bag</td><td>$100, PG, CP, 1X1, Zzz Bag</td></tr><tr><td>MK, CP, $250, 6X6, Biggy Tent</td><td>FW, MK, $15, 3X3, Cosy Sock</td><td>$100, MK, FW, 2X2, Easy Boot</td></tr><tr><td>PG, FW, $90, 4X4, Dura Boot</td><td>FW, MK, $100, 2 × 2, Easy Boot</td><td>$100, MK, CP, 5X5, Tiny Tent</td></tr><tr><td>PG, CP, $100, 1X1, Zzz Bag,</td><td>FW, PG, $90, 4X4, Dura Boot</td><td>$250, MK, CP, 6X6, Biggy Tent</td></tr></table>

Note that each projection allows for compression on different columns. These projections do take up additional space, but due to compression, the increase in space is not linear (i.e. not strictly proportional to the number of projections, but less than that). Furthermore, the incremental increase in used space is offset by the advantage of reduced I/O for any projection as compared to the I/O of unsorted and uncompressed table [39].

## 5. Our approach: the alternate columnar approach for analytical databases

## 5.1. Overview and description

As mentioned earlier, columnar approach is already commonly used in analytical databases. Typically, tables in analytical databases, such as the one shown in Fig. 3, are stored in the RDBMS in a columnar fashion. Fact tables, which are at the center of each data warehouse/data mart and contain the relevant quantitative measures to be used for decision support and analysis, usually have extremely large number of records that are orders of magnitude larger than the number of records in dimensions [19]. Most queries require limited number of columns from a join of fact table with its dimensions. Consequently, as elaborated on in Section 3, the columnar approach is advantageous, due to its efficiency of joins [8–11] and fast retrieval of the few selected voluminous columns that are needed to provide needed answers as demanded by particular decision analysis requests, and avoidance of the remaining columns that are not necessary in a particular analysis. However, the vertical partitioning for each column and respective storage provides additional opportunities for novel ways to store the data in analytical databases that further enhance their utility for timely decision support and fast analysis based on large amounts of data. Here we introduce a different approach to taking advantage of columnar organization when dealing with analytical databases.

The result of this process is a single denormalized (pre-joined) table, as shown in Fig. 4, where the attributes of all dimensions are stored as columns in one table together with the fact table attributes, as opposed to a set of tables shown in Fig. 3. The entire denormalized table is stored in columnar fashion. The last column in the table in Fig. 4 depicts the virtual identifier, equivalent to the position of the row in a given column, as explained in Section 3. Our proposed approach does not require the creation and maintenance of surrogate keys, evidenced by the absence of surrogate keys in Fig. 4.

<table><tr><td colspan="21">NORMALIZED SALES Table</td><td></td></tr><tr><td>Store ID</td><td>Store Zip</td><td>Store Region Name</td><td>Store Region Population</td><td>Product ID</td><td>Product Name</td><td>Product Price</td><td>Product Vendor Name</td><td>Product Category Name</td><td>Customer ID</td><td>Customer Name</td><td>Customer Zip</td><td>Date</td><td>Day of Week</td><td>Day of Month</td><td>Month</td><td>Qtr</td><td>Year</td><td>TID</td><td>Dollars Sold</td><td>Units Sold</td><td>VID</td></tr><tr><td>S1</td><td>60600</td><td>Chicagoland</td><td>8,000,000</td><td>1X1</td><td>Zzz Bag</td><td>$100</td><td>Pacifica Gear</td><td>Camping</td><td>1-2-333</td><td>Tina</td><td>60137</td><td>1/1/2013</td><td>Thursday</td><td>1</td><td>January</td><td>Q1</td><td>2015</td><td>T111</td><td>$100</td><td>1</td><td>1</td></tr><tr><td>S2</td><td>60605</td><td>Chicagoland</td><td>8,000,000</td><td>2X2</td><td>Easy Boot</td><td>$70</td><td>Mountain King</td><td>Footwear</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/1/2013</td><td>Thursday</td><td>1</td><td>January</td><td>Q1</td><td>2015</td><td>T222</td><td>$70</td><td>1</td><td>2</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>3X3</td><td>Cosy Sock</td><td>$15</td><td>Mountain King</td><td>Footwear</td><td>1-2-333</td><td>Tina</td><td>60137</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T333</td><td>$75</td><td>5</td><td>3</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>1X1</td><td>Zzz Bag</td><td>$100</td><td>Pacifica Gear</td><td>Camping</td><td>1-2-333</td><td>Tina</td><td>60137</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T333</td><td>$100</td><td>1</td><td>4</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>4X4</td><td>Dura Boot</td><td>$90</td><td>Pacifica Gear</td><td>Footwear</td><td>3-4-555</td><td>Pam</td><td>35401</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T444</td><td>$90</td><td>1</td><td>5</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>2X2</td><td>Easy Boot</td><td>$70</td><td>Mountain King</td><td>Footwear</td><td>3-4-555</td><td>Pam</td><td>35401</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T444</td><td>$140</td><td>2</td><td>6</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>4X4</td><td>Dura Boot</td><td>$90</td><td>Pacifica Gear</td><td>Footwear</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T555</td><td>$360</td><td>4</td><td>7</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>5X5</td><td>Tiny Tent</td><td>$150</td><td>Mountain King</td><td>Camping</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T555</td><td>$300</td><td>2</td><td>8</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>6X6</td><td>Biggy Tent</td><td>$250</td><td>Mountain King</td><td>Camping</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T555</td><td>$250</td><td>1</td><td>9</td></tr></table>

Fig. 4. Denormalized Table Sales.

Let us consider the example introduced in Section 2, where the Tristate population changes from 2,000,000 to 3,000,000. In this approach, the first record that occurs after that change occurs, will have that information recorded. This is illustrated in Fig. 5 which assumes that the newly added last record with VID value 10 occurred after the population change in the Tristate region from 2,000,000 to 3,000,000 took place.

Note that Type 2 approach of preserving history by adding a new record is implemented without the need for using a surrogate key, as shown in Fig. 5. In fact Type 2 approach is native to this solution and no additional effort to implement it during the ETL process is needed. New record is added to the table for every occurrence of a fact and it always contains all the relevant and correct data for all the associated dimensions at the time of the fact's occurrence. That preserves the history without the need for additional mechanisms such as surrogate keys.

Also note that approach of denormalizing the dimensional model would be a non-starter for the row-based dimensionally modeled analytical databases, as the size (width) of the row would be unmanageable by row-based DBMS for the number of rows implied by the fact tables. Recall that in row-based DBMS entire rows have to be read from disk to memory. The extensive disk I/O implied by the width of the single “unified” fact table that is pre-joined with its dimensions, would be cost prohibitive in terms of performance, given the large number records in such table. Therefore, the approach based on denormalizing dimensional model necessitates that the columnar-orientation be used for storing the denormalized table.

As mentioned in Section 4, projection is an intentional duplication of subset of columns of the dataset to achieve higher compression by sorting, with a goal of providing a better query performance. Before this approach of using a single denormalized dataset is implemented, datasets would have to be analyzed for the most optimal compression identifying all the relevant hierarchies (hierarchical attribute groupings) and deciding which projections will be created. This analysis will result in creation of multiple projections for various dimensions and attribute hierarchies. Even though at first glance it may look like projections will lead to a massive demand for additional space, compression ensures that the amount of needed additional disk space is not as drastic. In practice, the number of projection is limited (never exceeding five), resulting in somewhat predictable upper limit on space requirement. A more formal discussion of this performance aspect of our approach is provided in Section 5.2.3 where we show that in vast majority of cases, the increase in space requirement under our approach, based on one denormalized table is within one order of magnitude.

In Section 5.2, we present a theoretical framework for our approach, using the notation presented here. The model notation will be used in the subsequent sections to compare our approach with a traditional star-schema based row based approach, with respect to its ETL process (Section 5.2.a), size requirements (Section 5.2.b) and query execution time (Section 5.2.c). The differences in performance of both approaches, both with respect to size requirements and query execution time will be experimentally validated in the context of the introduced model in Section 5.3.

## 5.2. Model: general notation, functions and parameters

<table><tr><td>Model parameter</td><td>Explanation</td></tr><tr><td> $F$ </td><td>Number of Fact Tables in the original star schema</td></tr><tr><td> $D$ </td><td>Number of Dimension Tables in the original star schema</td></tr><tr><td> $S$ </td><td>Number of Source Tables that will be used in the ETL process</td></tr><tr><td> ${FT}_{f}$ :  $f = 1,\ldots ,F$ </td><td>Fact Tables</td></tr><tr><td> ${DT}_{d}$ :  $d = 1,\ldots ,D$ </td><td>Dimension Tables</td></tr><tr><td> ${ST}_{s}$ :  $s = 1,\ldots ,S$ </td><td>Source Tables</td></tr><tr><td> ${FC}_{f}$ :  $f = 1,\ldots ,F$ </td><td>Total number of fact columns in the fact table  ${FT}_{f}$ </td></tr><tr><td> ${DC}_{d}$ :  $d = 1,\ldots ,D$ </td><td>Total number of columns in the dimension table  ${DT}_{d}$ </td></tr></table>

<table><tr><td>Store ID</td><td>Store Zip</td><td>Store Region Name</td><td>Store Region Population</td><td>Product ID</td><td>Product Name</td><td>Product Price</td><td>Product Vendor Name</td><td>Product Category Name</td><td>Customer ID</td><td>Customer Name</td><td>Customer Zip</td><td>Date</td><td>Dayof Week</td><td>Dayof Month</td><td>Month</td><td>Qtr</td><td>Year</td><td>TID</td><td>Dollars Sold</td><td>Units Sold</td><td>VID</td></tr><tr><td>S1</td><td>60600</td><td>Chicagoland</td><td>8,000,000</td><td>1X1</td><td>Zzz Bag</td><td>$100</td><td>Pacifica Gear</td><td>Camping</td><td>1-2-333</td><td>Tina</td><td>60137</td><td>1/1/2013</td><td>Thursday</td><td>1</td><td>January</td><td>Q1</td><td>2015</td><td>T111</td><td>$100</td><td>1</td><td>1</td></tr><tr><td>S2</td><td>60605</td><td>Chicagoland</td><td>8,000,000</td><td>2X2</td><td>Easy Boot</td><td>$100</td><td>Mountain King</td><td>Footwear</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/1/2013</td><td>Thursday</td><td>1</td><td>January</td><td>Q1</td><td>2015</td><td>T222</td><td>$100</td><td>1</td><td>2</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>3X3</td><td>Cosy Sock</td><td>$15</td><td>Mountain King</td><td>Footwear</td><td>1-2-333</td><td>Tina</td><td>60137</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T333</td><td>$75</td><td>5</td><td>3</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>1X1</td><td>Zzz Bag</td><td>$100</td><td>Pacifica Gear</td><td>Camping</td><td>1-2-333</td><td>Tina</td><td>60137</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T333</td><td>$100</td><td>1</td><td>4</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>4X4</td><td>Dura Boot</td><td>$90</td><td>Pacifica Gear</td><td>Footwear</td><td>3-4-555</td><td>Pam</td><td>35401</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T444</td><td>$90</td><td>1</td><td>5</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>2X2</td><td>Easy Boot</td><td>$100</td><td>Mountain King</td><td>Footwear</td><td>3-4-555</td><td>Pam</td><td>35401</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T444</td><td>$200</td><td>2</td><td>6</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>4X4</td><td>Dura Boot</td><td>$90</td><td>Pacifica Gear</td><td>Footwear</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T555</td><td>$360</td><td>4</td><td>7</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>5X5</td><td>Tiny Tent</td><td>$100</td><td>Mountain King</td><td>Camping</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T555</td><td>$200</td><td>2</td><td>8</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>2,000,000</td><td>6X6</td><td>Biggy Tent</td><td>$250</td><td>Mountain King</td><td>Camping</td><td>2-3-444</td><td>Tony</td><td>60611</td><td>1/2/2013</td><td>Friday</td><td>2</td><td>January</td><td>Q1</td><td>2015</td><td>T555</td><td>$250</td><td>1</td><td>9</td></tr><tr><td>S3</td><td>35400</td><td>Tristate</td><td>3,000,000</td><td>2X2</td><td>Easy Boot</td><td>$70</td><td>Mountain King</td><td>Footwear</td><td>3-4-555</td><td>Pam</td><td>35401</td><td>1/3/2013</td><td>Saturday</td><td>3</td><td>January</td><td>Q1</td><td>2015</td><td>T444</td><td>$70</td><td>1</td><td>10</td></tr></table>

Fig. 5. Implicit preservation of history in denormalized Table Sales.

(continued)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Model
parameter Explanation
$SC_{s}$: $s = 1, ..., S$ Total number of columns in the source table $ST_{s}$ $DR_{d}$ The current number of rows for a dimension table $DT_{d}$ $FR_{f}$ The current number of rows for a fact table $FT_{f}$ $C_{A}$ Total number of columns in a single denormalized table under our approach (same for all projections)
m The projection multiplier
P The number of projections
$A_{p}$: $p = 1, ..., P + 1$
Denormalized $(p = 2, ..., P + 1)$
tables:
original
$(p = 1)$ and
the
projection
tables
$PC_{p}$: $p = 1, ..., P + 1$
Total number of
columns in
projection
table $A_{p}$
</div>

## 5.2.1. ETL process

In this section we will consider the complexity implications of both approaches, in the context of the ETL algorithms outlined below. The following generic functions, encapsulating table, row and column manipulations, will be used tom compare both approaches.

The two scenarios listed below represent the execution of the ETL process during the initial load of a data warehouse with extracted and transformed operational data. The subsequent periodic loads that follow the initial load will follow the similar algorithm, with the extracts of source data pertaining only to the new data that has been generated since the last ETL cycle.

The first and third step of the ETL process (E)xtract, and (L)oad, are not significantly different between two approaches. The (E)xtract steps of both approaches involve equal number of columns and thus the same number and types of calls of the generalized EXTRACT() function. (L)oad of fact and dimension tables under the traditional approach involves similar amount of data compared to one projection table in our approach. The additional projection tables will, of course, require additional time to load.

The second (T)ransform step contains the most critical differences between both approaches. The part of this step that involves the TRANSFORM() function does not contain significant differences, since transformations such as de-duplication, summarization and any other logical mathematical manipulations would be identical in both scenarios. The key difference is in the classical approach's need to conduct adding of surrogate keys to every row of every dimension table and mapping of surrogate keys for every row of every fact table, as contained in the ADDSURROGATE () and MAPSURROGATE () functions respectively. The performance needs

<table><tr><td>Function</td><td>Parameters</td><td>Description</td></tr><tr><td rowspan="2">EXTRACT(TableColumn1, TableColumn2)</td><td>TableColumn1 is a column of a source table whose content is to be extracted</td><td rowspan="2">This function extracts the content of a column in the source table and inserts it in the corresponding column in the copy of the dimension table in the data staging area.</td></tr><tr><td>TableColumn2 is a column of a destination table (dimension or fact) into which the extracted content of TableColumn1 is inserted</td></tr><tr><td>TRANSFORM(Table)</td><td>Table is a table whose columns need to undergo any kind of transformation</td><td>This generic function performs all needed transformations, such as de-duplication, summarization and any other logical mathematical manipulations. The details are abstracted out on purpose since they would be identical in both scenarios.</td></tr><tr><td>ADDSURROGATE(TableRow)</td><td>TableRow is every row of a table to which function is applied</td><td>This function adds the unique value of a surrogate key to each row in a dimension table. This is typically accomplished by some variation of an auto increment function.</td></tr><tr><td>MAPSURROGATE(TableColumn, TableRow)</td><td>TableColumn is a column of the table to which this function applies. TableRow is every row of the table.</td><td>This function maps newly created surrogate keys into the appropriate columns of the fact table (foreign key columns), populating each row of the fact table with values of surrogate keys that correspond to the surrogate key values of matching rows in the dimension tables</td></tr><tr><td>LOAD(Table)</td><td>Table is a table whose content is to be loaded from the staging area into the actual data warehouse</td><td>This function copies the content of a table in the data staging area into the data warehouse. This is typically a straightforward copy operation and it will execute in exactly the same fashion under both scenarios</td></tr><tr><td>COMPRESS(TableColumn, CompressionType)</td><td>TableColumn is a column to be compressed, CompressionType is a broad type of compression used</td><td>This function compresses a table column in one of the three broad compression types, high compression, low compression of fact compression. Various specific algorithms may be used in each of those types, and the choice of specific algorithm and its execution performance will greatly impact this function&#x27;s operation.</td></tr><tr><td>PROJECT(Table, NumberProjections)</td><td>Table is a table on which projection will be conducted, NumberProjections is the number of intended projections</td><td>This function performs the number of specified projections of the single denormalized table in our proposed approach</td></tr><tr><td>COVTABLE(SourceTable, DestinationTable)</td><td>Source and Destination Tables for which this function determines any columns of the source table are to be extracted into the destination table, either as straightforward copy or to be transformed later</td><td>COVTABLE(SourceTable, DestinationTable) = 1If source table maps any values into the destination table COVTABLE(SourceTable, DestinationTable) = 0otherwise</td></tr><tr><td> $dy_d$ </td><td>The transformation parameter for each dimension table  $DT_d$ </td><td> $dy_d$  = 1 if any of the dimension table  $DT_d$  columns need any such as deduplication, summarization and any other logical mathematical manipulations. $dy_d$  = 0 otherwiseThis parameter was not made column specific since transformation details are not different across scenarios</td></tr><tr><td> $fy_f$ </td><td>The transformation parameter for each fact table  $FT_f$ </td><td> $fy_f$  = 1 if any of the fact table  $FT_f$  columns need any such as deduplication, summarization and any other logical mathematical manipulations. $fy_f$  = 0 otherwiseThis parameter was not made column specific since transformation details are identical across scenarios</td></tr></table>

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Standard Relational Star Schema Scenario
1. (E)extract -Move all source data into the staging area
For each source table $ST_s$: s=1,..,S
    For each dimension table $DT_d$: d=1,..,D
    IF COVTABLE ($ST_s$, $DT_d$) = 1
    For each column sc of $ST_s$
    For each column dc of $DT_d$
    IF dc depends on sc
    EXTRACT(sc,dc)

For each source table $ST_s$: s=1,..,S
    For each fact table $FT_f$: f=1,..,F
    IF COVTABLE ($ST_s$, $FT_f$) = 1
    For each column sc of $ST_s$
    For each column fc of $FT_f$
    IF fc depends on sc
    EXTRACT(sc,fc)

2. (T)transform – prepare data to be moved to the Data Warehouse
For each dimension table $DT_d$: d=1,..,D
    IF dy_d=1 TRANSFORM($DT_d$)
    For each row r_i: i=1,..,DR_d
    ADDSURROGATE(r_i)

For each fact table $FT_f$: f=1,..,F
    IF fy_f=1 TRANSFORM($FT_f$)
    For each row r_i: i=1,..,FR_f
    For each column c_j: j=1,..FC_f
    IF c_j IS FOREIGN KEY
    MAPSURROGATE(c_j,r_i))

3. (L)oad – load prepared data into the data warehouse database
    For each dimension table $DT_d$: d=1,..,D
    LOAD($DT_d$)
    For each fact table $FT_f$: f=1,..,F
    LOAD($FT_f$)
</div>

of these operations need to be compared with the performance needs of projection and compression operations in our approach as contained in the PROJECT () and COMPRESS() functions respectively. ADDSURROGATE () is usually accomplished by a database sequence for each dimension which generates auto increment numbers, which is not a resource intensive process. MAPSURROGATE (), on the other hand, is very resource intensive. It performs the joins of all dimensions with the fact staging table (with large number of rows) by non-key columns (or corresponding hash values) to get surrogate keys in fact staging table. As the size of dimensions and fact staging table grows over the course of time, these joins become very expensive. Furthermore, Massively Parallel Processing (MPP) systems (used for storing large dataset) are not optimized for joins of many tables and this approach does not scale well.

Before we discuss the implication of the projection operation, as expressed by the generic PROJECT () function, requiring creating of multiple projection tables, we need to note that this operation is performed only at the initial setup, and in subsequent periodic appends, it is replaced by the multiple EXTRACT() operations for each projection. These processes, at the time of execution are straightforward and not particularly resource intensive, but we do acknowledge that the choice of projections itself is a complex problem that is similar to the problem of index selection in a relational database.

## Denormalized Single Compressed Table Scenario

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1. (E)extract -Move all source data into the staging area
For each source table $ST_s$: s=1,...,S
    IF COVTABLE($ST_s$, $A_1$) = 1
    For each column sc of $ST_s$
    For each column ac of $A_1$
    IF ac depends on sc
    EXTRACT(sc,ac)

2. (T)ransform – prepare data to be moved to the Data Warehouse
IF (any dy_d=1 :d=1,...,D) OR
    (any fy_f=1 :f=1,...,F)
    TRANSFORM($A_1$)

PROJECT ($A_1$,P)

For each projection table $A_p$: p=1,...,P+1
    For each column $c_i$: i=1,...,PCp
    (IF $c_i$ IS high compression column COMPRESS($c_i$, highComp)
    IF $c_i$ IS low compression column COMPRESS($c_i$, lowComp)
    IF $c_i$ IS fact compression column COMPRESS($c_i$, factComp))

3. (L)oad – load prepared data into the data warehouse database
For each table $A_p$: p=1,...,P+1
    LOAD ($A_p$)
</div>

5.2.2. Choice of projections

There are three general types of selection criteria that can be used to determine the projections that will be materialized:

## 1. Usage of the database

## 2. Structure of the database

## 3. Physical constraints

The first category, usage of the database, includes information about the observed or anticipated queries that will be run by the database users. Parameters such as query frequency, thresholds (hard or soft) on query running time, and prioritization should be taken into account when making the selection of projections. If we expect, or have already observed, users to perform daily analysis on certain portions of the data, we would consider the collection of dimension and fact table attributes used in their analysis as a candidate projection. In many cases, business intelligence software, connected to the database, generates automatically reports and charts. The queries used in this process and their frequency should be considered when selecting projection candidates.

The second category, structure of the database, includes details about the dimension hierarchies, correlations among attributes within or across dimensions, and the cardinality of each attribute. We can use this information to determine how to combine or expand projections without a significant increase in their physical size. For example, consider a candidate projection that includes the following three attributes: CustomerID, StoreID, DollarsSold. If we observe or expect that for most CustomerID's there is a single CustomerZip, we can add CustomerZip to the projection attributes because we will be able to use sorting on the combination of CustomerID and CustomerZip to enable high level of compression on both attributes. Since StoreId is part of the Store dimension hierarchy StoreID → StoreZip → StoreRegionName, we can consider adding StoreZip and StoreRegionName to the projection. Sorting on the combination of StoreID, StoreZip, StoreRegionName can preserve the sorting on just StoreID because for each StoreID there is only one StoreZip and for each StoreZip there is only one StoreRegionName. Therefore, we can enable at least the same level of compression for the two additional attributes (StoreZip and StoreRegionName) as the level of compression for StoreID.

The third category, physical constraints, includes the available amount of storage for the database and the projections, the cost of additional storage, and available budget. Ultimately, the selection criteria of all three categories need to be taken into account when making the decision what projections to create in addition to the original table.

This comparison of the resource requirements for the ETL process uses the row-based star schema approach as the baseline in the algorithm outlined above. However, as we discussed in Section 4, columnar approach, and use of compression and projection is commonly used for large data warehouses, so the issue of choosing the best projection and compression is present in both approaches. We conclude this analysis with a discussion how, for comparable data sets, our approach has some inherent advantages when it comes to choosing the projection tables: In a standard data model for large scale analytical databases based on a star schema with various dimensions, the sorting of dataset in one particular dimension would be expected to leave the other dimensions not optimized for compression. However, there are dimensions that are closely related to each other and hence their values repeat in sync with each other. For example, CUSTOMER and STORE are typically modeled as two different dimensions, but more often than not a customer buys from the same store or from the same region or zip code. In such cases of correlated dimensions, the additional projections may not be needed. By ascertaining the degree of association between various dimensions and finding cases of strong associations between dimensions or subsets of dimensions, redundant projections can be avoided where such associations exist. Also, by avoiding the use of surrogate keys, we do not create additional columns that cannot benefit significantly from compression. Surrogate keys columns are maximum cardinality columns, and as such the number of entries in such columns cannot be reduced by using compression. In a typical scenario, illustrated by Fig. 3, multiple such new columns are created, while no such new columns are created in our approach.

Once sorting and projections are accomplished, datasets have to be compressed accordingly, as expressed by our generic COMPRESS() function. Note that in our algorithm we distinguish between three broad types of compression: high and low compression methods for dimension columns and compression methods for fact columns. We provide additional discussion in the next subsection but here we provide some examples of applicable methods for each. The dimensions and corresponding columns can be compressed using RLE compression method. For the fact related columns, a regular LZ77 or/and Hoffman coding (Zlib) algorithm could be used. In numeric datasets, these algorithms can provide a ratio of 1:5 compression (providing 80% reduction of data that has to undertake the disk I/O process in equivalent queries) which makes up for the redundancy of the data created by projections [40,41]. In the next subsection we consider the size requirements of our proposed approach in a more formal way, using the model notation developed in the previous section, with several additional parameters and assumptions.

## 5.2.3. Size requirements

For simplicity of our discussion, and without a loss of generality, we will assume the even distribution of columns across dimensions, which each dimension having equal number of columns, labeled as $\mathsf { D C } _ { d } .$ Similarly, we use label DR as the number of “original” dimension rows where again we make a simplifying assumption that it is the same across the dimensions, for each $d = 1 , . . . , D$

Let t be the “change factor” i.e. the expected multiplier of the number of a single original dimension record as based on the expected number of changes that dimension record is to undergo in the reasonable life span of an analytical database. For the same reasons, we will assume that there is one common multiplier t across all the dimensions, resulting in the number of records in each dimension as

t D $R _ { d }$ which we will assume to be≪ $R _ { f }$

Finally let m be the projection multiplier, representing the total increase in the size of our columnar table due to the creation of multiple projection tables for certain hierarchies as discussed in Section 4.2. It is primarily determined by the number of projections that are to be implemented, but may not correspond strictly to that number, due to the fact that the size of each incremental table can be further compressed on different columns. In other words, $m \leq P ,$ where P is the number of intended projections.

In order to compare required database size of our approach with a standard row-based approach, we discuss three scenarios within our model framework.

Scenario 1. Standard row-based, dimensionally modeled, analytical databases:

The total number of memory locations<sup>1</sup> ML1 can be expressed as:

$$
M L 1 = R _ {f} \left(C _ {f} + D\right) + t D R _ {d} \left(C _ {d} + 1\right)\tag{1}
$$

where the first term represents the total number of memory locations in the fact table, with total number of fact table columns equaling number of fact columns added with the number of foreign keys (one for each dimension), and the second term represents the total number of memory locations in all dimension tables, where one extra column is needed in each dimension for a surrogate key.

Scenario 2. Row-based denormalized single table without compression: accounting for changes with the implicit history preservation.

We provide this intermediate scenario in order to illustrate the size cost of implicit history preservation when columnar approach with compression potential is not used.

In this scenario, the “change factor” t (i.e. the expected multiplier of the number of a single original dimension records as based on the expected number of changes that dimension record is to undergo in the reasonable life span of an analytical database) does not play a role, since all necessary history is preserved in each fact occurrence, as described in Section 5.1 (Fig. 5) and the “change factor” multiplier t is not necessary.

The number of memory locations under this scenario, where a single table contains all fact columns, all dimension columns for each dimensions and has as many rows as the original fact table, can be expressed as:

$$
M L 2 = R _ {f} \left(C _ {f} + D C _ {d}\right)\tag{2}
$$

The factor of size increase $S _ { \mathrm { M L } 2 }$ under this scenario can be described as follows:

$$
S _ {M L 2} = M L 2 / M L 1 = R _ {f} \left(C _ {f} + D C _ {d}\right) / \left(R _ {f} \left(C _ {f} + D\right) + t D R _ {d} \left(C _ {d} + 1\right)\right)\tag{3}
$$

If, acknowledging that $R _ { f } \gg R _ { d . }$ , we assume that the size of t D $R _ { d . }$ $( C _ { d } + 1 )$ is negligible, the size increase factor S can be expressed as

$$
S _ {M L 2} \approx (C _ {f} + D C _ {d})) / (C _ {f} + D)\tag{4}
$$

Which can be further reduced $\tan ^ { 2 }$ :

$$
S _ {M L 2} \approx 1 + (C _ {d} - 1) / \left(C _ {f} / D + 1\right)\tag{5}
$$

We can see that size increase factor is greater if the number of dimensions is higher (i.e. we account for a greater variety of influencing factors in our desired subject of analysis) and if the number of dimension columns is high (i.e. dimensions are “wide”, meaning that each influencing factor is described by a large number of individual descriptors, as is often the case). Conversely, the expected size increase will be smaller if the fact table has relatively large number of columns.

Scenario 3. Our approach: row-based denormalized columnar database with compression: accounting for changes with the implicit history preservation at a lower size increase and faster i/o times.

Without the loss of generality, let us assume that for each dimension $d = 1 , . . . , D$ the term $C _ { d L C }$ is the number of low cardinality columns (which also includes the key column(s), whose “sub-atomic” components can be compressed), $C _ { d H C }$ is the number of high cardinality columns with respective compression factors $c o m p _ { L C }$ and comp between 0 and 1, where com $p _ { L C } { < } c o m p _ { H C } . ^ { 3 }$ The total number of columns is then $C _ { d L C } + C _ { d H C } = C _ { \mathrm { d } }$ for each dimension.

Finally, the since the fact column(s) can also be compressed (and often quite significantly so), we introduce the term comp which represents the fact column compression factor.

Before we account for the projection multiplier m, the database size in this case is

$$
M L 3 * = R _ {f} \left(\operatorname{comp} _ {f} C _ {f} + D \left(\operatorname{comp} _ {L C} C _ {d L C} + \operatorname{comp} _ {H C} C _ {d H C}\right)\right)\tag{6}
$$

Adding the projection multiplier the database size in this scenario can be expressed as

$$
M L 3 = m R _ {f} \left(\operatorname{comp} _ {f} C _ {f} + D \left(\operatorname{comp} _ {L C} C _ {d L C} + \operatorname{comp} _ {H C} C _ {d H C}\right)\right)\tag{7}
$$

with the corresponding size increase factor $S _ { M L 3 }$ expressed as

$$
S _ {M L 3} = M L 3 / M L 1 = m R _ {f} \left(\operatorname{comp} _ {f} C _ {f} + D \left(\operatorname{comp} _ {L C} C _ {d L C} + \operatorname{comp} _ {H C} C _ {d H C}\right)\right) / \left(R _ {f} (C _ {f} + D) + t D R _ {d} (C _ {d} + 1)\right)\tag{8}
$$

Which can be reduced, (after again acknowledging that $R f \gg R d$ , we assume that the size of t D Rd $( C d \neg + 1 )$ is negligible), to

$$
S _ {M L 3} \approx m \left(\operatorname{comp} _ {f} C _ {f} + D \left(\operatorname{comp} _ {L C} C _ {d L C} + \operatorname{comp} _ {H C} C _ {d H C}\right)\right) / \left(C _ {f} + D\right)\tag{9}
$$

How the size increase factor $S _ { M L 3 }$ compares to the $S _ { M L 2 }$ will depend mostly on the “strength” of the compression factors, ratio of high and low cardinality columns and the projection multiplier. As discussed above, the projection multiplier m is smaller than a total number of projections, since the marginal size requirement increase for each additional projection is not strictly linear.

In conclusion of this discussion, it is worth noting that, in many practical implementations, inclusion of all columns in all projections is not always required to successfully use our approach. In Section 6 we will illustrate this difference by showing both types of situations in two separate examples. In the first example all the columns are included in the projections because the decision analysts have a decision making process that requires doing ad-hoc analysis on the data and their analysis may require any combination of columns. In the second example, due to much more predictable analysis patterns, based on reports and dashboards, we were able to use a relatively small subset of columns in each projection, resulting in a situation where the total size requirements of our approach were significantly smaller that under the traditional approach.

## 5.2.4. Query execution time

For the purpose of analysis of the key performance aspect where our approach promises to bring about the improvement when compared to the standard model we expand our model to include the query execution time and their determinants. We introduce the following notation representing the distinct steps of the query execution under both approaches:

T: total execution time of the query is expressed as

$$
\mathrm{T} = \mathrm{T} _ {\mathrm{R}} + \mathrm{T} _ {\mathrm{J}} + \mathrm{T} _ {\mathrm{S}} + \mathrm{T} _ {\mathrm{U}},
$$

where indices $\mathbb { R } , \mathbb { J } , S$ and U represent the following query execution steps:

S: Search (sequential, binary tree, etc) for all matching data accord ing to the criteria specified in the query

R: Retrieval of all needed data from the storage medium into memory, requiring disk I/O operations

J: Joining of data from two or more tables

U: Unpacking of compressed data

This framework is a modified version of a commonly accepted framework in the area of computer science dealing with query complexity and execution time. Details of sub-steps of each portion of the query execution are abstracted out as they are not pertinent to our discussion.

Computational complexity of queries in relational databases is an extremely well researched and discussed topic in the area of computer science and an excellent overview of it is available in [8].

The key points of the accumulated knowledge, as they pertain to our analysis are as follows:

• the complexity of joins is dependent on the column count and row count of the participating tables and under the best conditions its computational complexity is directly dependent on the sum of column counts of participating tables

• the complexity of searches is dependent on the row count of the participating tables

• the complexity of data retrieval is dependent on the product of row count and column count of the participating tables

We will use subscript Std and Col for the standard and columnar approach respectively when evaluating execution times under both approaches.

The total execution time under both approaches can be expressed as summation of step execution times:

$$
\mathrm{T} _ {\text { Std }} = \mathrm{T} _ {\text { StdR }} + \mathrm{T} _ {\text { StdJ }} + \mathrm{T} _ {\text { StdS }} \quad \mathrm{T} _ {\text { Col }} = \mathrm{T} _ {\text { ColR }} + \mathrm{T} _ {\text { ColU }} + \mathrm{T} _ {\text { ColS }}\tag{10}
$$

noting that $\mathrm { T } _ { \mathrm { C o l J } } = 0$ and $\mathrm { T } _ { \mathrm { S t d U } } = 0$ respectively, due to the fact that the standard approach does not use column compression and that our approach eliminates the need for table joins.

We also note that total execution times under the standard approach can be expressed as following functions

$$
T _ {S t d} = f \left(t c _ {S t d}, c c _ {i (i = 1, \dots , t c)}, r c _ {i (i = 1, \dots , t c)}\right),
$$

where $\mathrm { t c } _ { \mathrm { S t d } } , \mathrm { c c } _ { \mathrm { i } } \ ( \mathrm { i } = 1 , . . . , \mathrm { t c } )$ and $\Gamma \mathsf { C } _ { \mathrm { i } } ( i = 1 , . . . . , \mathrm { t c } )$ are table count, each table's column count and row count respectively

Similarly, the total execution time under our proposed approach can be expressed as:

$$
\mathrm{T} _ {\text { Col }} = \mathrm{f} (\mathrm{cc}, \mathrm{rc}),
$$

where cc and rc are the total row and column count of a single denormalized table respectively, where

$$
\mathsf {c c} = \mathsf {s u m} \mathsf {c c} _ {\mathrm{i}} (\mathrm{i=1,...,tc})
$$

$$
\text { and   } \mathrm{rc} = \max _ {\mathrm{i}} (\mathrm{i} = 1, \dots , \mathrm{tc})
$$

Using the notation above, we will express the performance as the ratio of expected execution time under our approach and the standard approach

$$
\mathrm{Qr} = \mathrm{E} (\mathrm{T} _ {\text { Std }}) / \mathrm{E} (\mathrm{T} _ {\text { Col }})\tag{11}
$$

which can be further expanded to

$$
\mathrm{Qr} = \left(\mathrm{E} \left(\mathrm{T} _ {\text { StdR }}\right) + \mathrm{E} \left(\mathrm{T} _ {\text { StdJ }}\right) + \mathrm{E} \left(\mathrm{T} _ {\text { StdS }}\right)\right) / \left(\mathrm{E} \left(\mathrm{T} _ {\text { ColR }}\right) + \mathrm{E} \left(\mathrm{T} _ {\text { ColS }}\right) + \mathrm{E} \left(\mathrm{T} _ {\text { ColU }}\right)\right) \tag {12}
$$

since $\mathrm { E ( T _ { C o l U } ) \ll E ( T _ { C o l R } ) + E ( T _ { C o l S } ) }$ and $\operatorname { E } \left( \operatorname { T } _ { \mathrm { C o l S } } \right) \leq \operatorname { E } \left( \operatorname { T } _ { \mathrm { S t d S } } \right)$ our ratio can be expressed as follows: Under the best possible circumstance for the standard, star schema and row-based approach, the ratio of query execution time of standard approach an our single table columnar approach can be expressed as follows:

$$
\mathrm{Qr} \geq 1 + \left(\mathrm{E} \left(\mathrm{T} _ {\text { StdR }}\right) + \mathrm{E} \left(\mathrm{T} _ {\text { StdJ }}\right) - \mathrm{E} \left(\mathrm{T} _ {\text { ColR }}\right)\right) / \left(\mathrm{E} \left(\mathrm{T} _ {\text { ColS }}\right) + \mathrm{E} \left(\mathrm{T} _ {\text { ColR }}\right)\right)\tag{3}
$$

Observation: there exists a CCN and RCN such that for queries when

ccbCCN and rcNRCN ; QrN1;

$$
\text { due   to } \mathrm{E} (\mathrm{T} _ {\text { StdR }}) + \mathrm{E} (\mathrm{T} _ {\text { StdJ }}) \geq \mathrm{E} (\mathrm{T} _ {\text { ColR }})
$$

We will set aside the issue of $\mathrm { E ( T _ { S t d J } ) }$ even though it may (and very often does) represent very significant portion of overall query time under the standard approach and focus on the comparison of retrieval times, $\operatorname { E } ( \operatorname { T } _ { S \operatorname { t d R } } )$ and $\mathrm { E } ( \mathrm { T } _ { \mathrm { C o l R } } )$ respectively. Their dependence on column and row count can be expressed as follows:

For a fixed row count, there exists a CCN if cc b CCN, $\operatorname { E } \left( \operatorname { T } _ { \mathrm { C o l R } } \right) < \operatorname { E } \left( \operatorname { T } _ { \mathrm { S t d R } } \right) .$

Similarly, for a fixed column count, there exists a RCN if rc N RCN, $\operatorname { E } \big ( \mathrm { T } _ { \mathrm { C o l R } } \big ) < \operatorname { E } \big ( \mathrm { T } _ { \mathrm { S t d R } } \big ) .$

We know, that due to the columnar approach what retrieves only necessary columns, if cc = 1, for a fixed rc:

$$
\mathrm{E} \left(\mathrm{T} _ {\text { ColR }} (\mathbf {c c})\right) \ll \mathrm{E} \left(\mathrm{T} _ {\text { StdR }} (\mathbf {c c})\right)
$$

Also, retrieval time for row based approach is quite insensitive to the number of required columns since all rows need to be retrieved anyway, and an insignificant increase in computational resource is needed for any additional columns. This is not the case in columnar approach, where every additional column requires additional retrieval effort resulting in significant increase in retrieval time. Therefore:

$$
\frac {\partial \mathrm{T} _ {\text { ColR }}}{\partial_ {c c}} \gg \frac {\partial \mathrm{T} _ {\text { StdR }}}{\partial_ {c c}}
$$

Exactly opposite is true when it comes to row retrieval, meaning that, as we discussed in Chapter 4, retrieval time under standard approach is more sensitive to increase in row count whereby the retrieval time under our approach is more impacted by higher column count.

In order to validate this claim we conduct a series of experiments with controlled queries on synthetic data, described in the next section.

## 5.3. Model performance: experimental validation

In this section we validate our approach by conducting the series of extensive numerical simulations covering the entire spectrum of feasible scenarios with respect to the nature of fact and dimension tables, their number of columns, the ability to compress them as well as the number of needed projections. In these experiments, we focus on the key performance characteristics that we discussed above:

Size: disk (TB), memory (GB) required under each approach

Query speed: usage of the database, speed of queries against the data warehouses under both approaches

5.3.1. Validation of the size requirement of our approach with numerical simulation

Here we outline the choice of probability distributions and their parameters for our simulation experiments.

Number of projections P: we set the distribution a step function with a certain percentage of projections set at one and the reminder varving from two to five. This particular distribution choice is explained as follows: as we discussed above, the number of projections are dependent upon need to access certain data/query in a time sensitive manner. If that need/requirement does not exist, there is no incentive to further create projections. Similarly, if requirements for time sensitive analysis across multiple hierarchies exist, we will see multiple projections to match interesting hierarchies. As we discussed above, in a typical organization, a data mart (with single subject), there are usually 5 or at maximum up to 7 dimensions (higher number of dimensions indicate overzealous normalization of dimensions also known as centipede design which implies inefficient design pattern). Even though a single dimension like product can have multiple projections, in practice, time sensitive reports often use only one of the many possible hierarchies. Also, certain dimensions and respective hierarchy could already be baked in the natural architecture of a data warehouse. A good example of such dimension and hierarchy is calendar dimension because entire data is already physically sorted by time and hence will not require additional projections. Similarly, if ETL process extracts different operations of different regions in a periodic fashion, it will produce similar sorting by time and region in a naturally evolving fashion. Henceforth, we set a bimodal distribution with spikes around one and four, petering out at five, since to our knowledge, five is the widely accepted limit on number of projections accepted in practice, corresponding to the true number of distinctly projectable dimensions, after which further marginal system wide gains in query speed do not justify additional space increase.

Compression factor for fact columns comp : truncated normal distribution with the mean of 0.33, truncated at 0.2 and 1 respectively. As discussed previously, the fact tables are compressed using the zlib compression. In practice, zlib gives compression of 3:1 on average. This conforms to the documentation of zlib at http://www.zlib.net/zlib\_tech. html which states that “More typical zlib compression ratios are on the order of 2:1 to $5 { : } 1 "$ . By applying a truncated normal distribution with limits of 0.2 and 1 respectively, we make a conservative assumption that no compression below 5:1 is possible and that very low compression factors up to and including no compression (with 1:1 factor) are possible to occur.

Number of fact columns $\mathrm { C _ { f } } \mathrm { : }$ truncated normal distribution with upper bound 300, mean 160 and lower bound 1.

The lower bound of one represents the observation form practice of the existence of so called coverage or “fact less” fact tables, that simply record occurrence of certain fact as a combination of dimension values happening at a certain point in time and that are consequently tagged with a timestamp as the only fact column. However they represent a very small minority of fact tables. Usually in a well-designed data warehouse, fact tables have a large number of columns to avoid a situation where fact tables have to be joined to do cross fact analysis. The number of columns varies by user requirements but is typically around 150. The widest fact tables in practice (often data warehouses containing financial industry facts (Federal Reserve Bank as an example), can reach the column count up to 300 columns while many ERP driven data warehouse environments have fewer than 100 columns. Again, we make a conservative assumption that a greater than realistic portion of fact tables has a small number of fact columns.

Number of dimensions D: truncated normal distribution, with mean 6, upper bound 10, lower bound 3:

In a well-designed data warehouse, the dimensions are within range of 5–7 and that number very rarely goes up to 10. Any higher number of dimensions indicates the need to coalesce dimensions into smaller number. The designs that have N10 dimensions, are known as centipede design and are indication of inferior strategy [17].

The number of low and high cardinality dimension columns Cd and ${ \mathrm { C d } } _ { \mathrm { H C } } { \mathrm { : } }$ truncated normal distribution: range 2–200, with mean 100: medium sigma. Number of dimension columns and ratio of high/low cardinality columns was estimated based on various projects in financial and manufacturing environment, in which a healthy dimension usually contains approximately 100 attributes/columns and never exceeds 200 columns. In a dimension, roughly half of the columns percent tend to be categorical in nature (for example, color of product, position on shelf, organic flag, category, type etc.) and have low cardinality, with this percentage ranging from 30 to 70%. The remaining dimension columns are continuous or categorical in nature with high cardinality (for example dimension of the product, price etc.)

Compression factor for low cardinality dimension columns comp : truncated normal distribution upper bound 0.5, lower bound 0.01. Compression factor for high cardinality dimension columns comp : truncated normal distribution upper bound 0.8, lower bound 0.2.

Compression method used in dimension tables is typically RLE compression which is highly dependent upon the extent of pattern/repetition of the values in a given column and the column data type. In case of categorical, low cardinality dimensions, if a dimension hierarchy is used to sort the data, we could see tremendous reduction in space of the order of 1:00 or 1:1000. However, if dimension hierarchy is a component of another hierarchy and entire pattern of values cannot be exploited, the ratio could deteriorate almost 1:2.

For high cardinality columns the compression factor can deteriorate to the 1:1.25 ratio and will not exceed 1:4 ratio.

Having chosen our parameters as outlined above have conducted two series computational simulations of 30,000 experiment instances using the following setup, expanding on the simplified model as show in Eq. (9), based on a more realistic assumption whereby each column in the fact table and in dimension tables may have a different compression ratio, within the range specified by their respective distributions:

Size Ratio as determined by Fact Count, Dimension Count and Number of Projections (m)

<table><tr><td>m</td><td>1</td><td colspan="8"></td></tr><tr><td rowspan="2">Average Size Ratio Fact Column Count</td><td rowspan="2">Dimension Count</td><td colspan="8"></td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1-50</td><td>4.53</td><td>5.22</td><td>6.27</td><td>6.90</td><td>9.02</td><td>9.96</td><td>11.10</td><td>12.50</td><td>8.35</td></tr><tr><td>51-100</td><td>1.33</td><td>1.85</td><td>2.30</td><td>2.77</td><td>3.28</td><td>3.72</td><td>3.93</td><td>4.39</td><td>3.18</td></tr><tr><td>101-150</td><td>1.02</td><td>1.28</td><td>1.62</td><td>1.92</td><td>2.17</td><td>2.45</td><td>2.72</td><td>3.07</td><td>2.13</td></tr><tr><td>151-200</td><td>0.86</td><td>1.06</td><td>1.26</td><td>1.50</td><td>1.68</td><td>1.90</td><td>2.10</td><td>2.35</td><td>1.66</td></tr><tr><td>201-250</td><td>0.73</td><td>0.93</td><td>1.09</td><td>1.25</td><td>1.41</td><td>1.59</td><td>1.76</td><td>1.89</td><td>1.40</td></tr><tr><td>251-300</td><td>0.69</td><td>0.82</td><td>0.97</td><td>1.08</td><td>1.24</td><td>1.38</td><td>1.52</td><td>1.66</td><td>1.22</td></tr><tr><td>Grand Total</td><td>1.22</td><td>1.35</td><td>1.70</td><td>1.97</td><td>2.29</td><td>2.53</td><td>2.85</td><td>3.09</td><td>2.22</td></tr></table>

<table><tr><td rowspan="2">Average Size Ratio Fact Column Count</td><td colspan="9">Dimension Count</td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>Grand Total</td></tr><tr><td>1-50</td><td>8.80</td><td>14.36</td><td>20.09</td><td>24.31</td><td>23.40</td><td>31.45</td><td>29.87</td><td>33.50</td><td>24.87</td></tr><tr><td>51-100</td><td>4.36</td><td>5.69</td><td>7.10</td><td>8.46</td><td>9.84</td><td>10.83</td><td>12.11</td><td>13.40</td><td>9.42</td></tr><tr><td>101-150</td><td>3.16</td><td>3.82</td><td>4.80</td><td>5.58</td><td>6.57</td><td>7.33</td><td>8.15</td><td>9.02</td><td>6.38</td></tr><tr><td>151-200</td><td>2.46</td><td>3.22</td><td>3.82</td><td>4.52</td><td>5.07</td><td>5.68</td><td>6.44</td><td>6.92</td><td>4.98</td></tr><tr><td>201-250</td><td>2.24</td><td>2.80</td><td>3.32</td><td>3.74</td><td>4.31</td><td>4.69</td><td>5.23</td><td>5.83</td><td>4.24</td></tr><tr><td>251-300</td><td>2.06</td><td>2.48</td><td>2.87</td><td>3.32</td><td>3.78</td><td>4.12</td><td>4.61</td><td>4.86</td><td>3.63</td></tr><tr><td>Grand Total</td><td>3.26</td><td>4.11</td><td>5.39</td><td>6.06</td><td>6.74</td><td>7.96</td><td>8.59</td><td>9.46</td><td>6.78</td></tr></table>

<table><tr><td rowspan="2">Average Size RatioFact Column Count</td><td colspan="8">Dimension Count</td><td rowspan="2">Grand Total</td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1-50</td><td>15.87</td><td>24.97</td><td>34.61</td><td>42.65</td><td>42.32</td><td>43.19</td><td>56.39</td><td>54.29</td><td>42.22</td></tr><tr><td>51-100</td><td>6.78</td><td>9.22</td><td>11.68</td><td>14.01</td><td>15.87</td><td>18.33</td><td>20.87</td><td>22.97</td><td>15.74</td></tr><tr><td>101-150</td><td>5.01</td><td>6.45</td><td>7.96</td><td>9.37</td><td>10.77</td><td>12.29</td><td>13.60</td><td>15.07</td><td>10.62</td></tr><tr><td>151-200</td><td>4.24</td><td>5.27</td><td>6.38</td><td>7.51</td><td>8.50</td><td>9.48</td><td>10.72</td><td>11.48</td><td>8.24</td></tr><tr><td>201-250</td><td>3.58</td><td>4.60</td><td>5.37</td><td>6.29</td><td>7.14</td><td>7.98</td><td>8.73</td><td>9.53</td><td>7.04</td></tr><tr><td>251-300</td><td>3.41</td><td>4.12</td><td>4.85</td><td>5.57</td><td>6.27</td><td>7.10</td><td>7.51</td><td>8.18</td><td>6.19</td></tr><tr><td>Grand Total</td><td>4.91</td><td>6.99</td><td>8.73</td><td>10.09</td><td>11.60</td><td>13.09</td><td>14.28</td><td>15.69</td><td>11.29</td></tr></table>

$$
m \frac {\sum_ {i = 1} ^ {C _ {f}} \operatorname{compf} _ {i} \sum_ {j = 1} ^ {D} \left(\sum_ {k = 1} ^ {C d L C _ {j}} \operatorname{compLC} _ {k} + \sum_ {l = 1} ^ {C d H C _ {j}} \operatorname{compHC} _ {l}\right)}{C _ {f} + D}
$$

The pseudocode of the algorithm that generates result based on this equation is provided in the Appendix A.

Simulation results are summarized in Table 1 and Fig. 6.

Fig. 6 shows the histogram of size requirement ratios of our approach compared with standard approach based on the simulation results using a random sampling with replacement from observed compression factors for fact, low and high cardinality dimension columns from the real–life cases (to be discussed in Section 6), shown on the left hand side and the results based on simulated distributions of compression factors, shown on the right. Results are quite similar, giving confidence to the accuracy of our chosen distributions, and they show that a very large percentage of observations does not exceed our “single level of magnitude” requirement.

Table 1 shows the effect of number of projections as well as the column count of fact table as well as the number of dimensions on the feasibility of our approach, regardless of the likelihood of any certain combination occurring. Due to space considerations we show the values for scenarios including one, three and five projections respectively. Again, if we assume the “single level of magnitude” cutoff point, almost all scenarios are feasible candidate for our approach, even though including very high (9–10) number of dimensions and an unusually small number of fact columns.

Random sampling with replacement from observed compression factors  
![](/api/attachments/5QQGPTGQ/fulltext/images/fe31cadc537ff172a9d69568d4824774277f58f718dc3909947a7b067dbddef5.jpg)

![](/api/attachments/5QQGPTGQ/fulltext/images/fcd1e9f54e688d2d647fd616e58ae56ec2dbe57b65ef870b2df52fb71d716b22.jpg)

<table><tr><td>size increase</td><td>percentage of</td></tr><tr><td>ratio</td><td>observations</td></tr><tr><td>0-10</td><td>96.72%</td></tr><tr><td>10-20</td><td>2.59%</td></tr><tr><td>20-30</td><td>0.41%</td></tr><tr><td>30-40</td><td>0.16%</td></tr><tr><td>40-50</td><td>0.07%</td></tr><tr><td>50-60</td><td>0.02%</td></tr><tr><td>60-70</td><td>0.02%</td></tr><tr><td>70-80</td><td>0.02%</td></tr></table>

<table><tr><td>Size Increase Ratio</td><td>Percentage of observations</td></tr><tr><td>0-10</td><td>83.29%</td></tr><tr><td>10-20</td><td>13.44%</td></tr><tr><td>20-30</td><td>1.84%</td></tr><tr><td>30-40</td><td>0.62%</td></tr><tr><td>40-50</td><td>0.29%</td></tr><tr><td>50-60</td><td>0.18%</td></tr><tr><td>60-70</td><td>0.10%</td></tr><tr><td>70-80</td><td>0.09%</td></tr><tr><td>80-90</td><td>0.06%</td></tr><tr><td>90-100</td><td>0.02%</td></tr><tr><td>100-110</td><td>0.02%</td></tr><tr><td>110-120</td><td>0.01%</td></tr><tr><td>120-130</td><td>0.01%</td></tr><tr><td>130-140</td><td>0.02%</td></tr><tr><td>140-150</td><td>0.01%</td></tr><tr><td>150-160</td><td>0.01%</td></tr></table>

Fig. 6. Histograms of size required ratio between the proposed (single table) and standard (multiple tables) approaches

When the number of projections is at its upper practical limit (5), number of feasible scenarios is about half of all possible combinations, but it's worth mentioning that even in this case, the feasible half will occur with greater frequency, since, as discussed above, instances of data warehouses with nine or more dimensions are very rare.

The result of these scenarios represent an upper limit of ratio ranges since the real life scenarios will include some additional space reduction opportunities such as lowers space requirement for each successive projection m and smaller projections of incomplete table, focusing on a subset of columns as discussed above.

These results validate that our approach is feasible in a majority of realistic cases to be expected in practice and they also provide insight for decision makers as to what conditions and factors contribute to the attractiveness of our approach.

5.3.2. Validation of the query speed improvement of our approach with synthetic database on commodity hardware

For these experiments we use publicly available massive data set containing one year's worth of data about every taxi ride in NYC, with each being described by >50 fact columns and dimension columns in total. This data is of significant size and queries executed on commodity hardware under both approaches are in the realistic time span of expected execution time for queries of this complexity.

The row count is large, in the order of 100 million rows, consistent with real life scenarios, and we generate a set of queries where we vary the column count required, in order to validate our claim that a certain column count always leads to superior performance of our approach. In real life, the required row count may be and often is an order of magnitude greater, resulting in even greater advantage of the columnar approach

The results comparing query execution performance of both approaches are summarized in Table 2, and they show that indeed, as long as the column count does not exceed number of 20 required columns per query (which is in practical world of analytics quite unlikely), our approach will significantly outperform standard approach.

It is interesting to note that even under this extremely unlikely scenario of very large number of columns needed for a particular analysis, the level at which our approach underperforms is much smaller relative to the level it outperforms the standard approach under much more realistic scenarios where certain report, ad hoc query or analytic algorithm requirement does not require N20 parameters.

Table 2  
Comparison of Average Query Execution Times.

<table><tr><td>Column count</td><td>Average query execution time ratio</td><td>Observation count</td><td>Average query execution time (milliseconds), columnar</td><td>Average query execution time (milliseconds), row based</td></tr><tr><td>1-5</td><td>415.04</td><td>17</td><td>61,878.45</td><td>7,741,618.23</td></tr><tr><td>6-15</td><td>34.26</td><td>21</td><td>94,579.36</td><td>2,718,799.72</td></tr><tr><td>16-21</td><td>12.99</td><td>26</td><td>102,845.03</td><td>1,343,518.76</td></tr><tr><td>22-50</td><td>0.69</td><td>16</td><td>983,224.88</td><td>664,862.71</td></tr></table>

Also, for the standard approach architecture, in this set of experiments we have allowed for caching of previous query results whereby every subsequent query could take advantage of in-memory stored results of a previous query set, significantly further reducing query execution time. Since we ordered query execution roughly by the column count starting with queries requiring small number of columns and working our way up to the full table scan (with full column count), the standard approach has exhibited lower retrieval times as the column count went up, as opposed to expectation that query execution times will say roughly the same. This was the only way to achieve parity and eventually advantage of the standard approach when compared to our approach. Have we reversed the order of query execution, the execution improvement ratios would not have been as dramatic for the low column count but on the other hand they would not reach the point of parity/advantage.

Finally, we need to mention that no projections were used in this set of experiment, which if used, would have improved the query time under our approach even further. These results serve to validate our claim of advantage of our approach in terms of query execution time when compared with the standard approach over the wide range of feasible scenarios, even without the benefit of projections, indicating that a wide range of tradeoffs in size requirements and query speed exist under out approach that provide better performance when compared to the standard approach.

Here the paper continues with a general discussion about the advantages and limitations of the introduced approach.

## 5.4. Advantages and limitations of the approach

The approach based on columnar organization of the denormalized star schema we introduced here, has certain clear advantages, when compared with the traditional approach of storing all dimensions and facts as separate tables.

ETL process for the analytical databases implemented using a traditional approach of storing dimensions and facts in separate tables requires complex ETL methods to be implemented for updating dimensions with their respective surrogate keys, in the most frequent cases when Type 2 strategy is required, preserving the history of the changed dimension record. In the approach we described in this paper, the ETL process is much more direct and straightforward. Type 2 is native to the approach discussed here, and it does not require the extra effort of creating and maintaining the surrogate keys. Consequently a critical part of the ETL (ensuring preservation of the history of data) is significantly simplified and therefore faster and less laborious. Accordingly, this approach scales up better for large datasets, with frequent inputs required to append most recent data in the analytical data repository. In addition, since all the data is pre-joined most of the queries are even faster than with the common approach to storing each dimension and fact separately and having to join them as part of queries. In Section 6, we will give concrete real-world examples of actual implementations that illustrate the benefits of such simplifications and performance improvements.

In addition to the advantage of simplifying the ETL process and increasing the speed of queries, certain current and future trends that are shaping analytical databases environment provide additional motivation for the introduced approach. The following is a summary of such trends.

Disk space is cheap and getting cheaper still. In many cases, the real cost of storing data is driven by the cost of licensing proprietary software per disk space, where the increase in amount of used disk space escalates the cost of license [42]. However, open source data processing methods are rivaling the proprietary software at an increasing rate, with the effect of further liberating users from disk space restrictions [43,44]. Therefore the projections that are necessary in our proposed approach are becoming increasingly feasible both in terms of cost and efficiency.

CPUs are getting faster with each generation. However, memory bandwidth cannot keep pace with these improvements due to a gap in performance evolution between raw CPU cycles per second per dollar, which until recently has approximately followed Moore's law, and RAM access speed, which trails Moore's law significantly [45]. In addition, the disk seek time remains the bottleneck of database systems, as locating the data on the disk and moving it into the memory is the slowest part of data retrieval. Consequently it is becoming much easier to afford the CPU cycles to decompress the data than it is to transfer uncompressed data from disk to memory to CPU [40]. Our proposed method takes full advantage of this trend.

Due to the increased emphasis on analyzing ever more sources of data, including the external data and big data, the volumes of data that are being included in analytical database is growing and the ETL processes are getting more extensive. At the same time, acquisitionto-consumption time of data in analytical databases is shrinking. The idea of active data warehousing, where ETL occurs continuously and in near-real time, is becoming prominent and the need for shorter ETL cycles is becoming critical in a growing number of projects. The simplification of ETL process offered by the introduced approach can provide an attractive alternative for such projects.

At this time in industry, majority of large data applications are housed in Massively Parallel Processing (MPP) DBMS including Greenplum, IBM Netezza, Teradata, Oracle Exadata or HP Vertica. The MPP approach to data processing is based on the architecture of storing and processing the data simultaneously in slices stored across various data nodes whose actions and results are coordinated by a master node. The incoming data is split and distributed across multiple nodes/segments. In order to make sure that all data nodes are busy and performing equal load of work (which ensures maximum efficiency) the distribution should lead to uniformity in terms of size of data across all data nodes. A variability of sizes across data nodes (known as distribution skew) is detrimental to the performance of database. Another factor that can be detrimental to the performance is movement of data across nodes. Hence, joins need to perform in such a way that there is minimal movement of data across nodes. This perspective is also called “colocation” of data [46].

One MPP approach to join of two tables (joins of multiple tables could be thought of and are typically implemented as a sequence of joins of two tables) is to create multiple copies of the smaller of two tables involved in the join. These copies are then sent to each node to be joined with the slice of data of the bigger table hosted by each particular node. This is also known as “broadcasting” of data. This approach works optimally when the smaller table is small enough to be broadcasted across all segments in a timely fashion. However with large dimension tables, such as rapidly growing dimensions implementing Type 2 approach to changes in dimensions, this approach is not feasible. The dimension tables, no matter how large, are always smaller that fact tables. So when a dimension is joined with a fact table (a very common occurrence in data warehouses) these large dimensions will end up being the “small” table that have to be broadcasted. In such cases relatively slow speed of broadcasting such large tables to all nodes more than offsets the advantages in speed of actual MPP processing. This architectural aspect of MPP system is discussed in depth in [46], which also recommends various methods to overcome this problem.

Another MPP approach to join is to cut the smaller of two tables involved in the join into multiple pieces, also known as slices, and then distribute those slices to nodes. This requires that all slices of the smaller tables are matched exactly to the nodes that contain corresponding slices of the larger table. This requires another layer of data processing which adds to the time of query execution and causes the deterioration of performance. Part of the additional processing is redistributing the slices by the foreign key in order to facilitate matching of slices of the smaller table with corresponding parts of larger tables stored on separate nodes. The sum of slices of the smaller table distributed to the nodes is usually larger than the smaller table itself, because multiple parts of the larger table hosted by separate nodes may have to be joined with same data from smaller tables. This leads to similar performance issues as with broadcasting [46].

The above described issues of deteriorating performance are particularly likely to occur in dimensionally modeled data where fact tables are commonly joined with multiple dimensions. These dimensions, as we noted, are often large which renders broadcasting unfeasible. However, the alternative solution of redistributing slices of dimensions to the fact table that would be required for a join with every dimension that needs to be joined with the fact table also substantially slows down the performance.

With the approach we described in this paper, these costly MPP system bottlenecks are avoided. All tables are pre-joined and MPP processing is much more efficient as there is no longer need for either broadcasting or redistribution caused by join queries. To be noted, this approach is fully compatible with the logical viewing of any data from dimensional modeling perspective, which remains a very relevant technique for conceptually modeling and analyzing the data. The dimensions and facts can still be conceptually modeled and viewed by the end-users as separate tables in a star schema.

The proposed approach is particularly applicable to projects that are focused on fewer number of subject areas. The proposed approach is not as appropriate for projects where bus architecture [17] method results in a large number of conformed dimensions that are re-used with multiple separate fact tables forming a constellation of star schemes. In such cases, the dimensions are kept in separate tables and they are designed and developed prior to the implementation of fact tables.

Even though such approach is common when creating allencompassing comprehensive enterprise-wide data warehouses, the reality is that large majority of analytical database projects are not of such scope. For such projects, our proposed approach presents a viable option with clear advantages, as described in the previous subsection.

Also, it is worth mentioning that with the advent of large amount of data, it has become increasing difficult to do traditional analysis of taking samples from raw datasets and do distribution analysis to understand the nature of data. That implies that data mining has to be done close to data, in other words, inside the database [47,48]. The big concern that data miners often face is that some key variables are not included in the star schema modeled data warehouse, since the inclusion of new variables implies with the changes in the target schema, which leads to requirement to change of the ETL, especially the most complex ones dealing with mapping of new key values and surrogate key matching in fact tables. Our approach, using only one denormalized table, avoids complex changes to the ETL process, and is more suited to facilitating the contemporary needs of data analysts.

Finally, most enterprise-wide data warehousing projects are preceded by successful smaller scope analytical database projects. The introduced method, by facilitating quicker and more robust development of such smaller projects, can actually help organizations to ready themselves for an enterprise data warehousing project at a faster pace.

We conclude this section by acknowledging that the modeling of optimal projection methods and consequent choosing and fine tuning of compression algorithms in this context is a very important problem and is to be addressed as a topic of future research. However, as we demonstrated via our numerical analysis, this approach has a potential to outperform the standard approach across a very wide range of implementation scenarios, even when an optimal compression and projection strategies are not calculable. We intend to further strengthen this claim in the next section that discusses two examples of implementation of our algorithm in a real life setting, we demonstrate that the use of a heuristic of identifying projections based on the anticipated pattern of decision support usage, as expressed by the most frequent group queries used across reports and ad hoc inquiries, and implementing appropriate corresponding compression algorithms can result in our approach clearly outperforming the standard star-schema based approach.

## 6. Implementation examples

The following two real-world examples will serve to illustrate the details and advantages of the introduced approach. The first example discusses the implementation of an analytical database at the Federal Reserve Bank of Kansas City and the second example elaborates on an implementation in a global tool manufacturing company.

## 6.1. Example - Federal Reserve Bank of Kansas City

Federal Reserve Bank of Kansas City (FRBKC) is one of the twelve regional Reserve Banks that, along with the Board of Governors in Washington, D.C., make up central bank of the United States. FRBKC is one of the largest consumers of economic data in the United States and it continuously faces the task of making diverse datasets available to various economists and researchers who have widely varied interests in these datasets. These analytical datasets are obtained from a number of sources. One common type of a source are publicly available databases, such as Home Mortgage Disclosure Act (HMDA) which provides data about mortgage applications of all mortgage applicants in the US, or the Census Populating Survey (CPS) which provides data about monthly employment status of 100,000 U.S. individuals for the period spanning decades. Another type of source are datasets resulting from congressional mandates like Dodd Frank Act, such as Comprehensive Capital Analysis and Review (CCAR) data set containing information about banking and lending practices of major US banks. In addition, data is also acquired from commercially purchased data sets from vendors like Transunion, Equifax, and Corelogic. For example, Transunion provides a data set containing data about 5% of US consumers and their credit behavior in relation to mortgages and loans, spanning over two and a half decades.

Typical size of the analytical datasets maintained by the FRBKC varies from hundreds of gigabytes on the lower end to tens of terabytes on the high end.

The example we will discuss here involves an analytical database at the FRBKC that has an uncompressed disk size of 3.37 TB and pertains to credit and mortgage history of US consumers with 298 variables. The data for this database is sourced from the Transunion data set. The database was modeled using dimensional modeling and it contained six dimensions (CALENDAR, CUSTOMER, LOAN, LOCATION, CREDIT PROFILE and MISCELLANEOUS DIMENSION,) and two fact tables (CREDIT PER-FORMANCE, LOAN PERFORMANCE).

The system used to host and process this database was Greenplum (version 4.2 with 16 nodes on 48GB RAM, Xeon 6-core dual processor, Redhat Linux operation system, 15 K fast disk and 10 gigabit of interconnect) massively parallel processing (MPP) platform running parallel instances of PostgreSQL RBDMS and storing data in a columnar fashion. However, when used in a traditional way, i.e. storing each dimension and fact table separately, the setup still exhibited inefficiencies both from ETL and query performance perspectives, as we will describe here.

The data was uploaded in the staging area using external tables and after various transformation and cleaning procedures, various dimension and fact columns were broken down into respective staging fact and staging dimension tables. This step was followed by insertion of the data into the respective facts and dimension tables applying Type 2 strategy for slowly changing dimensions. The surrogate keys were managed by database sequences, inserting auto-increment number for each new value of a surrogate key. Because the incoming data contained a lot of duplicate information that already existed in the dimension the ETL process had to check for every incoming record whether an identical record already existed in the table or not, and then allow insertion (and subsequent creation of a new surrogate key value) only for the records that represented actual change. For example if a customer marital status changed a new record with a new surrogate key in the dimension would be created. However, if nothing changed in the customer information the customer record would still be sent from the source to and the ETL process would have to recognize that it has to be discarded. This caused lengthy execution of ETL processes, e.g. 12 h of processing for insertion of 200 GB of data.<sup>4</sup>

![](/api/attachments/5QQGPTGQ/fulltext/images/ee4726a4ab3d11280670a47fd1dd18095173599cdba6dfb153cb8eadc72c3e20.jpg)  
Fig. 7. Query performance comparison of star schema approaches Columnar denormalized vs. traditional

However, the real challenge was on the performance side. This dataset is used by economists who have wide range of motivations and hence they pick various subsets of fact variables along with almost all dimensions. This typically led to a join of fact table with all the dimensions, followed by applying the row-filtering conditions. To be noted, techniques traditionally used to improve the performance of joins, such as indexes or partitioning, were of no help due to the size of data (which made the use of indexes counterproductive) and the statistical nature of queries issued by economists looking for random samples (which renders partitioning inapplicable). These restrictions on commonly available performance improvement techniques lead to numerous queries that are doing full table scan and extensive I/O. Based on the query log of queries over the course of one month, we discovered that the mean runtime for the queries with join of facts and dimensions was close to 2,000,000 millisecond or 0.55 h during a window of 45 days. The distribution of the runtime had a left skew which further reinforced the fact that a large portion of queries are running more than half an hour. Interviews with frequent users revealed a great level of frustration with such performance. Another finding was that their research cannot be restricted to a predetermined subset of variables and hence the design approach of smaller fact table with subset of columns was not a possibility. Therefore, we proposed to apply the approach we introduced earlier in this paper and the FRBKC agreed to it. We implemented the alternative columnar approach by leveraging the same Greenplum columnar database platform used originally. As prescribed by the method we introduced in Section 5, we denormalized the schema and joined dimensions and facts to produce a wide staging table/view. The final target table was a column oriented structure with various compression algorithms based on the nature of the column (e.g. continuous fact columns used zlib compression, sorted dimensions used RLE compression). With the new approach, the compressed table structure had the disk size of only 1.98 TB (vs 3.37 TB) which left plenty of scope for us to implement 3 other projections of the dataset based on the frequently used dimensions and correlation between dimensions. Each of these projections ranged from 1.4 TB to 1.6 TB. With this, the total disk space used by the aforementioned method was approximately 6.5 TB.

Over the course of a new 45 days window, we observed that our mean runtime of similar queries (i.e. compared to equivalent queries on a dimensionally modeled dataset in the previous 45 day window) had dropped to 560,000 milliseconds (9.3 min). On one-to-one comparison, the queries received up to 10 time faster response time with the alternate columnar approach. Fig. 7 Illustrates the comparison of the runtimes using the traditional approach vs. the alternate columnar approach for the same set of queries in this environment.

Besides performance, ETL process has been reduced from splitting the data in staging area, generating sequences, and deciding on slowly changing dimensions to a simple append of the incoming transformed and cleaned data. The duration of the ETL process that used to take several hours was reduced to b30 min.

This proof-of-concept case exemplified advantages of this approach by simplifying and expediting the ETL process and increasing the speed of queries. In fact our proposed approach has proven itself so successful, that it has been now replicated for the majority of other analytical databases in the FRBKC environments.

## 6.2. Example – global tool manufacturing corporation

United States based multinational tool manufacturer maintains a global enterprise wide data warehouse that combines analytical information from operations in North America, Europe, Asia and Australia. The incoming data comes from Baan ERP system which is implemented on Oracle row-based RDBMS. The data captures information about purchases, backorders, inventory levels and other operational information. The data warehouse is traditionally modeled into dimension and facts and it is used to analyze business subjects such as sales and profits. The ETL processes are designed with tools like Oracle Warehouse Builder, Informatica and Cognos DecisionStream. Unlike in the FBRKC environment where data was loaded monthly, the ETL process in this example is required to be much faster due to the dynamic nature of the business that continuously sells its products. The ETL infrastructure reads from a replicated standby database which is at a lag of just 15 min from the production system (using replicated standby database to feed the ETL system, instead of feeding from the actual operational database, is a standard ETL procedure in order to prevent ETL processes from adversely affecting the performance of the operational systems). The traditional design has served the organization over time very well and has been the backbone of decision making process. However, during the last few years, the organization has realized that online sales constitute a significant part of their earnings. The promotion and pricing is more dynamic in online sales than in traditional retail business. In order to make a quick decision about online opportunities like black Friday sales, the organization needed a truly active (as close to real time as possible) data warehouse which reflects the operational data source almost instantaneously.

In its original setup, a usual ETL process run for about three and half hours. Despite the difference of only 15 min between production and logical standby database, the real lag in information is almost 4 h which may result in a lot of missed opportunities due to the inability to make timely promotion and pricing decisions. For example, if demand for torque wrenches suddenly increases in the online store, and there are only a few available torque wrenches in the distribution warehouses, the systems should recognize that discount should not be given in this situation. With a long ETL lag, the pricing algorithm that uses the data from the data warehouse would not be nimble enough to take advantage of profit maximizing opportunity.

Faced with these conditions, the tool manufacturing company decided to try our alternative columnar approach. We implemented it on the design of a supplemental data mart based on 4 node (48GB RAM, 15 K drives, quad core dual processor CPUs, 10GB interconnect) HP Vertica Columnar database with combined disk space of 8 TB. We denormalized the incoming data and implemented the remaining transformations using simple SQL views.

The size of the original data warehouse was approximately 15.9 TB (containing history of the last 10 fiscal years). The implementation of columnar approach has reduced the disk size to 4.23 TB with no projections included. Addition of 17 projections of different grains and across multiple facts resulted in addition of 2.87 TB of additional disk utilization. To be noted, projections in this case are not conducted on the entire table and the respective sizes of each projection varied according to the requirement of the user group. Therefore, the total data volume requirement of the data warehouse, based on our approach is 7.1 TB, which is less than half of the original required size.

Our approach eliminated the bulk of ETL process related to generation of surrogate keys, lookups related to slowly changing dimensions, splitting of data into dimensions and facts, and other ETL activities, due to full compatibility of columns in the denormalized table with the columns from the source tables.

This has virtually eliminated the delay caused by ETL processes. The appending of the data did not take N7–10 min for any ETL iteration, depending upon the frequency of the ETL process (more frequent means less time because we are processing less data at a time). The bulk of the processing time was spent in pushing the data from Oracle based systems to ETL server and reading the data into HP Vertica via external tables. We also did a one-time copy of only static dimensions from operational data warehouse to further supplement the dataset in columnar database. Since ongoing ETL processing time is very small and requires only appending of the data, this process is run continuously to keep the decision making information as reflective of operational information as possible. In addition, the various algorithms/scripts, including pricing model, are more effective because each process was able to look at the latest data, unlike in the previous setup.

Finally due elimination of joins as well as the proper use of projections, consistent with the common query patterns, the query performance of the data warehouse has greatly increased. Table 3 shows the measure of the query performance gain achieved across various queries categorized by three main reports/dashboards used by decision makers.

To summarize, the alternative approach has proven itself very successful in this environment as well, and the manufacturing company decided to permanently adopt the new setup as its production data warehouse method for its on-line sales.

## 7. Conclusion

In this paper, we focused on the growing need for fast analysis of ever-increasing amounts of data for data-driven decision-support processes. As a contribution towards supporting this paradigm of using more and more data for analysis and decision support in a timely fashion, we have introduced a method for expediting the development and use of analytical databases.

This method combines columnar database technology with an approach based on denormalizing data tables for analysis and decision support improving directly the feasibility and quality of tactical decision making by making critical information more readily available, as well as the quality of longer term strategic decision making by widening the range of feasible queries against the vast amounts of available information. We have explained the details of the introduced method and we have shown how it improves the performance of the ETL process, the most common time-consuming bottleneck in most implementations of data warehousing for quality decision support, as well as the performance of individual analytical queries. We have also demonstrated how these improvements in the critical decision support infrastructure are achievable without resulting in insurmountable storage-size increase requirements.

We have discussed the benefits of our approach, as well as its limitations in certain circumstances. Through the series of computational experiments we have outlined the range of feasible scenarios, characterized by the fact column count, row count, number of dimensions and the need for projections in which our approach shows clear advantages, providing valuable insight to managers and decision makers when considering the adoption of this approach. In addition, we have illustrated the introduced approach by showing its application in two relevant real-world cases. The approaches and discussions given in this paper offer applicable solutions for a number of scenarios taking place in the contemporary world that are dealing with performance issues in development and use of analytical databases for the support of both tactical and strategic decision making. The intention of this paper was to bring to the academic and professional community's attention the real potential of this approach and a wide range of real-life scenarios in which it outperforms the standard approach. In our future research, we intend to build on the findings of this paper by investigating how this potential can be maximized in the context of projection and compression optimization.

Table 3  
Query performance comparison of both approaches

<table><tr><td>Reports</td><td>Summary Dashboards</td><td>Mean runtime -30days (traditional) – milliseconds</td><td>Mean runtime – 30 days (new columnar approach) milliseconds</td><td>Mean Runtime Ratio (Qr)</td></tr><tr><td>COGS/TSCC/Return Rates/CCI/GMROI</td><td>Costs</td><td>207,360</td><td>8064</td><td>25.71</td></tr><tr><td>Order fulfillment lead time, late order, backorder, inventory sales ratio, order status</td><td>Fulfillment</td><td>472,494</td><td>20,732</td><td>22.79</td></tr><tr><td>Cash to cycle time, inventory on hand, asset turn</td><td>Asset utilization</td><td>380,534</td><td>46,342</td><td>8.21</td></tr></table>

## Appendix A

Step 1: Generate Cf and D from the specified distributions and their ranges

```python
Step 2: compressed column size factor, based on specified distributions and their rnages
SET compressedColumnSize = 0
FOR ff= 1,...,Cf
    Generate comp ff
    compressedColumnSize += compff
END FOR
#This generates a scenario in which each column in the fact table may have a different compression ratio
```

```txt
Step 3: compressed dimension size factor
SET compressedDimensionSize = 0
SET compressedLowCardinalitySize = 0
SET compressedHighCardinalitySize = 0

FOR d=1,..D
    Generate LC
    Generate HC
    FOR lc =1,...,LC
    Generate compLC
    compressedLowCardinalitySize += compLC
    END FOR
    FOR hc =1,...,HC
    Generate compHC
    compressedLowCardinalitySize += compHC
    END FOR
    compressedDimensionSize += compressedLowCardinalitySize
    compressedDimensionSize += compressedHighCardinalitySize
    SET compressedLowCardinalitySize = 0
    SET compressedHighCardinalitySize = 0

END FOR
```

\# This generates a scenario in which each dimension has a different number of high and low cardinality columns, anc each column in each dimension table may have a different compression ratic

## References

[1] R. Sharma, S. Mithas, Transforming decision-making processes: a research agenda for understanding the impact of business analytics on organisations, European Journal of Information Systems 23 (4) (2014) 433–441.

[2] D. Kiron, R. Shockley, N. Kruschwitz, G. Finch, M. Haydock, Analytics: the widening divide, MIT Sloan Management Review 53 (2) (2012) 1–22.

[3] M. Barlow, Real-time Big Data Analytics: Emerging Architecture, first ed. O′Reilly Media. 2013.

[4] M.W.S. Chun, C. Griffy-Brown, H. Koeppel, The new normal: fundamental shifts for 21st century organizations and for the CIOs who lead them, J. Appl. Bus. Econ. 16 (5) (2014) 27–50.

[5] R.J. Goeke, R.H. Faley, Leveraging the flexibility of your data warehouse, Communications of the ACM 50 (10) (2007) 107–111.

[6] P. Trkman, K. McCormack, M.P.V.D. Oliveira, M.B. Ladeira, The impact of business analytics on supply chain performance, Decision Support Systems 49 (3) (2010) 318–327.

[7] B. Franks, Taming the Big Data Tidal Wave, first ed. Wiley, 2012.

[8] D.J. Abadi, P. Boncz, S. Harizopoulos, Column-oriented database systems, Proc. VLDB Endowment 2 (2) (August 2009).

[9] D.J. Abadi, P. Boncz, S. Harizopoulos, S. Idreos, S. Madden, The design and implementation of modern column-oriented database systems, Found. Trends Databases 5 (3) (2012) 197–280.

[10] D.J. Abadi, S. Madden, N. Hachem, Column-stores vs. row-stores: how different are thev really? Proceedings of SIGMOD'08 ACM New York NY USA Vancouver, BC Canada June 9–12.2008.

[11] S. Idreos, F. Groffen, N. Stefan, M. Mullender, M. Kersten, MonetDB: two decades of research in column-oriented database architectures, Database Architectures Group, CWI Amsterdam The Netherlands 2012

[12] J.M. Hellerstein, M. Stonebraker, J. Hamilton, Architecture of a database system, Found. Trends Databases. 1 (2) (2007) 141–259.

[13] M. Chang, R.J. Kauffman, Y.O. Kwon, Understanding the paradigm shift to computational social science in the presence of big data, Decision Support Systems 63 (2014) 67–80.

[14] A. Thusoo, J. Sen Sarma, N. Jain, Z. Shao, P. Chakka, S. Anthony, H. Liu, P. Wyckoff, R. Murthy, Hive: a warehousing solution over a map-reduce framework Proc, VLDB Endowment 2 (2) (August 2009).

[15] A. Simitsis, P. Vassiliadis, A method for the mapping of conceptual designs to logical blueprints for ETL processes, Decision Support Systems 45 (1) (2008) 22–40.

[16] N. Jukic, S. Nestorov, Comprehensive data warehouse exploration with qualified association-rule mining, Decision Support Systems 42 (2) (2006) 859–878.

[17] R. Kimball, M. Moss, W. Thornthwaite, J. Mundy, B. Becker, The Data Warehouse Lifecycle Toolkit, second ed. Wiley, New Jersey, 2007.

[18] A. Chaudhuri, U. Dayal, An overview of data warehousing and OLAP technology, ACM SIGMOD Record 26 (1) (1997) 65–74

[19] N. Jukic, S. Vrbsky, S. Nestorov, Database Systems – Introduction to Databases and ta Warehouses, rst ed. Pearson/Prentice Hall, New Jersey, 2013.

[20] J. Rivera, R.V.D. Meulen, Gartner Says Beware of the Data Lake Fallacy, Gartner Press Release, July 28 2014 (http://www.gartner.com/newsroom/id/2809117).

[21] B. Stein, A. Morrison, The enterprise data lake: better integration and deeper analytics, PWC Technol. Forecast Rethink. Integr. (1) (2014) (http://www.pwc.com/us/en/ technology-forecast/2014/cloud-computing/features/data-lakes.html).

[22] M. Rennhackkamp, Revolt Against the Data Lake as Staging Area, Martin Insights, June 30 2014 (http://www.martinsights.com/?p=1102#sthash.Tio4Y6AC.dpuf).

[23] M. Jacobsohn, M. Delurey, How the Data Lake Works, Booz Allen White Paper, June 29 2014 (https://www boozallen com/content/dam/boozallen/documents/Data Lake.pdf).

[24] M. Assay, Why Hadoop Isn't Killing the Data Warehouse, Readwrite, April 7 2014 (http://readwrite.com/2014/04/07/hadoop-data-warehouse).

[25] D. Duckworth, Is the Data Warehouse Dead? Is Hadoop Trying to Kill It? IBM Data Warehousing, March 12 2015 (https://ibmdatawarehousing.wordpress.com/2015/ 03/12/duckworth-is-data-warehouse-dead/).

[26] C. Green, The Data Warehouse Isn't Dead: It Just Needs An Automation Overhaul, Information Age, June 4 2015 (http://www.information-age.com/technology/ inormation-management/123459596/data-warehouse-isnt-dead-it-just-needs-automation-overhaul#sthash.vEKIN0Lc.dpuf).

[27] D. Henschen, Big data debate: end near for ETL? Information Week, December 3 2012 (http://www.informationweek.com/big-data/big-data-analytics/big-data-debate-end-near-for-etl/d/d-id/1107641?).

[28] J. Kobielus, No, The Data Warehouse Is Not Dead, InfoWorld, April 13 2015 (http:// www.infoworld.com/article/2908085/big-data/no-the-data-warehouse-is-notdead.html).

[29] C. Olofson, The Rise of Hadoop: Is ETL Dead? ComputerWorld, January 3 2012 (http://www.computerworlduk.com/blogs/idc-insight/clearing-the-fog-over-thefuture-of-security-in-the-cloud-3570844/).

[30] T. King, Is ETL on life support? http://solutions-review.com/data-integration/is-etlon-life-support/.

[31] M. Rennhackkamp, Data Lake Vs Data Warehouse, Martin Insights, November 11 2014 (http://www.martinsights.com/?p=1088#sthash.dWGV2F9m.dpuf).

[32] T. Ashish, Hadoop: 5 Undeniable Truths, Information Week, October 10 2014http:// www.informationweek.com/big-data/big-data-analytics/hadoop-5-undeniable truths/a/d-id/1316832

[33] R. Elmasri, S. Navathe, Fundamentals of Database Systems, Addison-Wesley, Massachusetts, 2010.

[34] G. Held, Data Compression: Techniques and Applications, Hardware and Software Considerations, second ed. John Wiley & Sons, New York, 1987.

[35] J.A. Storer, Data Compression: Methods and Theory, Computer Science Press, Maryland. 1988

[36] T.D. Lynch, Data Compression Techniques and Applications, Lifetime Learning Publications, California, 1985.

[37] M.R. Nelson, The Data Compression Book, M&T Books, California, 1991.

[38] M. Bassiouni, Data compression in scientific and statistical databases, IEEE Transactions on Software Engineering 11 (10) (1985) 1047–1058.

[39] B. Welton, D. Kimpe, J. Cope, C. Patrick, K. Iskra, R. Ross, Improving I/O forwarding throughput with data compression, Proceedings of 2011 IEEE International Conference on Cluster Computing September 2011, pp. 438–445.

[40] A.K. Dutta, R. Hasan, How Much Does Storage Really Cost? Towards A Full Cost Accounting Model for Data Storage, Proceedings of the 10th International Conference on Economics of Grids, Clouds, Systems, and Services, vol. 8193, 2013 29–43.

[41] http://docs.oracle.com/cd/A87860\_01/doc/server.817/a76992/ch20\_io.htm#21125.

[42] D. Assuncaoa, R. Calheirosb, S. Bianchic, M. Nettoc, R. Buyya, Big data computing and clouds: trends and future directions, Journal of Parallel and Distributed Computing 79–80 (May 2015) 3–15.

[43] G.R. Gangadharan, D. Tiwari, L. Sanagavarapu, S. Mishra, A. Williams, S. Timmaraju, Open-Source Cloud Software Solutions, Encyclopedia of Cloud Computing, Wiley 2016, pp. 139–149.

[44] http://finance.yahoo.com/news/open-source-databases-set-overtake-200637854. html.

[45] D. Patterson, Latency lags bandwidth, Communications of the ACM 47 (2004) 71–75.

[46] http://gpdb.docs.pivotal.io/4380/pdf/GPDB43BestPracticesA03.pdf pp. 21

[47] J. Cohen, B. Dolan, M. Dunlap, J.M. Hellerstein, C. Welton, MAD Skills: New Analysis Practices for Big Data, Proc. VLDB Endow, Vol. 2, 2, August 2009 1481–1492.

[48] A. Cuzzocrea, I.-Y. Song, K.C. Davis, Analytics over large-scale multidimensional data: the big data revolution! Proceedings of the ACM 14th International Workshop on Data Warehousing and OLAP (DOLAP '11), ACM, New York, NY, USA 2011, pp. 101–104.

Nenad Jukic is a Professor of Information Systems at the Quinlan School of Business at Loyola University Chicago. He conducts research in various information management–related areas, including database modeling and management, data warehousing, business intelligence, data mining, business analytics, big data, e-business, and IT strategy. His work has been published in numerous information systems and computer science academic journals, conference publications, and books. In addition to his academic work, he provides expertise to database, data warehousing, business intelligence, and big data projects for corporations and organizations that vary from startups to Fortune 500 companies and U.S. government agencies

Boris Jukic is a Professor of Information Systems and the Director of The Masters of Data Analytics Program at Clarkson University School of Business. Previously he was also an Associate Dean of Graduate Programs at Clarkson University School of Business. He conducts active research in various information technology related areas including e-business, data warehousing, data analytics, computing resource pricing and management, process and applications modeling as well as IT strategy. His work has been published in a number of management information systems and computer science academic journals, conference publications, and books.

Abhishek Sharma is a database/business intelligence consultant and the founder of an IT consulting company, Awishkar, Inc. He is also a Clinical Professor of Information Systems at the Quinlan School of Business at Loyola University Chicago. He has worked at various information technology positions in fields such as information management, banking/ quantitative finance and instrumentation, process control, and statistical analysis in manufacturing environment. Parallel with his consulting work and teaching, he conducts research in a variety of fields, including database modeling and management, data warehousing, business intelligence, data mining, very large databases (VLDBs)/big data, and IT strategy.

Svetlozar Nestorov is an Assistant Professor of Information Systems at the Quinlan School of Business at Loyola University Chicago. Previously he worked at the University of Chicago as a senior research associate at the Computation Institute, an assistant professor of computer science, and a leader of the data warehouse project at the Nielsen Data Center at the Kilts Center for Marketing at the Booth School of Business. He is a co-founder of Mobissimo, a venture-backed travel search engine that was chosen as one of the 50 coolest Web sites by Time magazine in 2004. His research interests include data mining, high-performance computing, and Web technologies.

Beniamin Korallus Arnold is a data architecture/business intelligence consultant and a current Masters of Science in Analytics student at the University of Chicago. He has consulted in enterprise information management strategy, database modeling, business intelligence and data warehouse design for some of the largest global companies in the airline, retail fuels and healthcare industries. His current professional focus is on implementing complete data warehousing and analytics platforms utilizing public cloud architecture. His involvement in academic research within the database modeling and business intelligence space began early during his undergraduate coursework at the Quinlan School of Business at Loyola University Chicago.
