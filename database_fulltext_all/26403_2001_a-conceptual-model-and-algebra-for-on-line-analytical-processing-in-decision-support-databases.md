---
otero_id: 26403
otero_key: "GKBV48ZY"
title: "A Conceptual Model and Algebra for On-Line Analytical Processing in Decision Support Databases"
authors: "Helen Thomas; Anindya Datta"
year: "2001"
journal: "Information Systems Research"
doi: "10.1287/isre.12.1.83.9715"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/GKBV48ZY/fulltext/images/cf4338ee55e1f1010d72616750656777c679ab7ca35959efbb4a9cb917644341.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## A Conceptual Model and Algebra for On-Line Analytical Processing in Decision Support Databases

Helen Thomas, Anindya Datta,

## To cite this article:

Helen Thomas, Anindya Datta, (2001) A Conceptual Model and Algebra for On-Line Analytical Processing in Decision Support Databases. Information Systems Research 12(1):83-102. http://dx.doi.org/10.1287/isre.12.1.83.9715

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2001 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GKBV48ZY/fulltext/images/ad2a1370acf9e07faefee1c939d6f50ce59b28f0d79fef6141637030d6e283c8.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Conceptual Model and Algebra for On-Line Analytical Processing in Decision Support Databases

Helen Thomas • Anindya Datta

DuPree College of Management, Georgia Institute of Technology, Atlanta, Georgia 30318-0520 helen@loochi.mgt.gatech.edu • adatta@loochi.mgt.gatech.edu

D <sup>ata</sup> <sup>warehousing</sup> <sup>and</sup> <sup>On-Line</sup> <sup>Analytical</sup> <sup>Processing</sup> <sup>(OLAP)</sup> <sup>are</sup> <sup>two</sup> <sup>of</sup> <sup>the</sup> <sup>most</sup> <sup>signifi-</sup>cant new technologies in the business data processing arena. A data warehouse, or de- cant new technologies in the business data processing arena. A data warehouse, or decision support database, can be defined as a “very large” repository of historical data pertaining to an organization. OLAP refers to the technique of performing complex analysis over the information stored in a data warehouse. The complexity of queries required to support OLAP applications makes it difficult to implement using standard relational database technology. Moreover, currently there is no standard conceptual model for OLAP. There clearly is a need for such a model and an algebra as evidenced by the numerous SQL extensions offered by many vendors of OLAP products. In this paper we address this issue by proposing a model of a data cube and an algebra to support OLAP operations on this cube. The model we present is simple and intuitive, and the algebra provides a means to concisely express complex OLAP queries.

(Data Warehouse; On-Line Analytical Processing (OLAP); Data Models; Algebra; Multidimensional Databases; Decision Support Databases)

## 1. Introduction

The dual but related notions of data warehousing and On-Line Analytical Processing (OLAP) are, clearly, two of the most significant new technologies in the business data processing arena. They are used in a multitude of industries such as retail sales (supermarkets, department stores, etc.), telecommunications, financial services, and real-estate (Chauduri and Dayal 1997). Perhaps the most telling testimonial of the widespread acceptance of these technologies is the fact that data warehousing and OLAP products sales totaled \$9 billion in 1997, up 350% since 1995 (Butler Group 1996, Byard and Schneider 1996). Loosely speaking, a data warehouse is a “very large” repository of historical data pertaining to an organization (see Inmon 1996 and Kimball 1996 for excellent treatment of data warehousing). The notion of OLAP, introduced by Codd in his seminal paper in 1993 (Codd et al. 1993), refers to the technique of performing complex analysis over the information stored in a data warehouse.

In general, OLAP applications are characterized by the rendering of enterprise data into multidimensional perspectives. This is achieved through complex, adhoc queries that frequently aggregate and consolidate data, often using statistical formulae (Codd et al. 1993). For example, a retail organization is often interested in comparing the total sales for the current year with the total sales for the previous year, or identifying sequences of 5 years or more when sales have increased (or decreased) within a 50-year envelope. It has been conjectured that relational database technology is well suited to fulfilling the needs of OLAP. However, the major use of relational technology so far has been in transaction management and ad-hoc querying for traditional On-Line Transaction Processing (OLTP) systems. Conversely, OLAP calls for sophisticated online analytical support, for which the traditional normalized relational model is ill equipped (Kimball and Strehlo 1995). Readers can easily gauge the limitation of the relational model by trying to answer the queries mentioned above in a relational language such as SQL.<sup>1</sup> As a result, several vendors have developed specialized OLAP products such as Hyperion’s Essbase, Oracle’s Express, and Sybase’s IQ. Most of these products, however, suffer from the following drawbacks (Gray et al. 1997, Agrawal et al. 1997): (a) They suggest SQL extensions piecemeal, rather than a comprehensive query language; (b) the user interaction is often limited to one operation at a time, which is inconsistent with the objectives of OLAP; and (c) multidimensional rendering of data involves identifying certain attributes as dimensional parameters and other attributes as metrics or measures (this is explained in detail later in the paper). Most OLAP products in the market exclusively view metrics as functions of dimensions; that is, dimension and metric sets are static. However, this prevents users from making queries based on metric restrictions. It has been shown that this is inadequate as often users like to query dimensions by restricting metric values (Agrawal et al. 1997). For example, in a retail sales application where sales amount is a metric, an analyst may wish to list those products having total monthly sales greater than \$500. With many of the current OLAP products, this query would not be possible because the query imposes a restriction on a metric attribute. Thus there is clearly a need for symmetric treatment of dimensions and measures.

One reason for the failure of existing OLAP products to provide a “good” framework is the fact that, unlike the relational model, there does not exist a precise, commonly agreed upon conceptual model for OLAP. Though the notion of the data cube (explained below) has been widely accepted as the underlying logical construct of data warehouses (i.e., multidimensional databases), there does not exist a precise model for a data cube, and therefore it has not been possible to define accurately a model of operations on a data cube.

In response to this need there is significant current interest in work that attempts to explore operations on multidimensional databases. An influential paper in this field appeared in 1995, written by Gray et al. (1995). In this paper the authors define the CUBE operator by extending SQL to include new types of grouping and aggregating functionalities. Since the appearance of this paper, much work has been devoted to designing efficient CUBE algorithms (Harinarayan et al. 1996, Agarwal et al. 1996). However, this work, while interesting, still makes very little headway in orchestrating a “big picture” for OLAP. The work remains at a level of suggesting piecemeal extensions to SQL, which, while perhaps satisfying a specific OLAP requirement, cannot lay an integrated framework on which generic OLAP functionalities can be constructed. This situation is somewhat analogous to the situation in the mid 1970s, when data processing experts would suggest special purpose algorithms to perform operations such as selection, projection, and join. However, because of the lack of a common data and operations model (which would later come in the form of the relational model, relational algebra, and calculus), such solutions failed to provide general frameworks and eventually led to the development of relational database technology. Similarly, unless a common data and operations model of multidimensional databases (i.e., data warehouses) is advocated, a general purpose OLAP framework will be hard to realize.

In this paper we propose a simple but generic model of a data cube and attempt to design a simple algebra to support OLAP operations on this cube. To the best of our knowledge, this is the first formal model proposed for data warehousing and OLAP that attempts to encompass current OLAP functionality requirements. We stress that our proposal, like all data and operations models, is intended to serve as a foundation on which query languages can be designed efficiently. It is our intention to keep the model similar to the relational model, primarily for ease of implementation. We emphasize that our model is intended to be independent of implementation, and thus we do not consider implementation issues in this paper. We do, however, believe implementation to be a crucial subject and, therefore, the work of future papers.

The remainder of the paper is organized as follows. In §2 we describe the context of our research, in §3 we discuss related work and provide a brief overview of OLAP and data warehousing, and in §4 we present the contributions of this paper. In §5 we discuss the goals of a data and operations model for OLAP. In §6 we present the data model, and in §7 we present the proposed operators. We present example queries using the algebra in §8, and we discuss properties of the model in §9. We conclude the paper in §10.

## 2. Research Context

We now explicitly state the background upon which this paper rests. Data warehousing and OLAP are established fields of study as well as established technologies. A peculiar feature of this market is its rapid evolution in the marketplace without an adequate formal foundation. This is usually not the case in the significant paradigm shifts one observes in the software industry. For instance, the development of relational database systems (arguably the RDBMS defines the software paradigm that has, perhaps, had the greatest impact on business data processing) in the early 1980s followed fairly intensive R&D in the relational model and algebra from the early 1970s. Similarly, the development of the “object-oriented” software paradigm, resulting in tools such as SMALLTALK, C--, and finally JAVA, was preceded by years of study on the properties of such systems. The data warehousing/ OLAP market (although we think data warehousing is less “profound” than either of the two software classes mentioned above), on the other hand, has developed in a completely opposite fashion—not much foundation building but a great deal of product offerings. This has had, as we see it, two distinct impacts:

1. A large degree of variability in the functionalities of the product offerings. This is what we (and others) have referred to as “ad-hoc” and is a key motivation for this paper.

2. In spite of the variability of the product offerings, industry is, after all, driven by market needs. Thus, given the fact that OLAP systems are in considerable use in organizations today, it stands to reason that across the different products, market needs are being satisfied.

Based on the above considerations, one of the aims of this paper is to consider the various functionalities being offered today in the OLAP market and provide a list that is “comprehensive” with respect to the marketplace as it currently stands. Given the second item listed above, it appears that the OLAP market has matured to a point where the rate of introduction of new features will slow significantly. This phenomenon is reinforced by industry and analyst reports (Forrester Research, Inc. 1997, Business Intelligence, Inc. 1998). The main competitive “play” will be consolidation, i.e., integration of various features and functionalities into single products. This, however, is very difficult owing to the lack of a “common” foundational model on which to perform such consolidation. In fact, the underlying models of existing products differ so widely that it is often infeasible to integrate their features. This is the backdrop of this paper: It proposes such a common foundation.

## 3. Related Work

We now provide a compendium of related work, including the early work in data and operations modeling and more recent work in OLAP and data warehousing.

## 3.1. Data and Operations Models

Early work in data modeling began with the hierarchical, network, and relational models. Although there is no early documentation for the hierarchical model, it is known that this model evolved from the Information Management System (IMS) DBMS, which was developed in the late 1960s (Elmasri and Navathe 2000). The network model was developed in the early 1970s and is the underlying model for the Integrated Database Management System (IDMS) DBMS (DBTE 1971). The relational model was also developed in the early 1970s (Codd 1970). This model has gained widespread acceptance and is the underlying data model for many commercial DBMSs. In addition, operations models have been developed for the relational data model. These models include the relational algebra (Codd 1970), which is a procedural language, and the tuple relational calculus (Codd 1971, 1972) and the domain relational calculus (Zloof 1975, Lacroix and Pirotte 1977), which are declarative languages.

There is very little work in creating data and operations models for multidimensional databases. We are aware of three papers in the published literature which tackle this issue. All of these are quite recent, the earliest one appearing in 1996 (Li and Wang 1996) and the two most recent ones in 1997 (Agrawal et al. 1997, Glysseus and Lakshmanan 1997). All of these papers deal with multidimensional databases, designed around the basic underlying construct of a data cube, containing dimensions, attributes, and measures. These papers are important as they chart the initial footsteps in an important research topic, namely modeling data warehouses. However, unrealistic restrictions are placed in these models, e.g., restrictions are imposed on either the number of attributes per dimension or the number of total measures representable in the cube. Moreover dimensions and measures are treated asymmetrically, leading to the inability of these models to answer particular types of queries without requiring expensive redesign. In this paper we propose a simple but generic model of a data cube and attempt to design a simple algebra to support OLAP operations on this cube. As already mentioned, this paper is one of the first to deal with these issues.

We now discuss more recent work by providing an overview of OLAP and data warehousing.

## 3.2. Overview of OLAP and Data Warehousing

A data warehouse can be defined as a repository of historical data used to support decision making (Inmon 1996). OLAP refers to the technology that allows the user to efficiently retrieve data from the data warehouse. The characteristics of OLAP applications are quite different from those of operational or OLTP systems. OLTP systems are designed to perform repetitive, structured tasks where detailed records are updated (e.g., order entry, account updates following a bank transaction). The emphasis in these systems is on maximizing transaction throughput and maintaining consistency. Typically OLTP systems are on the order of hundreds of megabytes to gigabytes in size.

In contrast to OLTP systems, data warehouses are designed for decision support purposes and contain long periods of historical data. For this reason, data warehouses tend to be much larger than OLTP systems, often by orders of magnitude. It is quite possible for a data warehouse to be hundreds of gigabytes to terabytes in size (Chauduri and Dayal 1997). In this environment, aggregated and summarized data are much more important than detailed records. The emphasis in data warehousing is on query processing and response times rather than transaction processing. Queries tend to be complex and ad-hoc, often requiring computationally expensive operations such as joins and aggregation. Further complicating this situation is the fact that such queries must be performed on tables having potentially millions of records. Moreover, the results have to be delivered interactively to the business analyst using the system.

The differing requirements of OLTP and OLAP systems dictate different data models and implementation methods for each type of system. The entityrelationship (ER) model is commonly used to represent an OLTP application at the conceptual level. However, this model is not well suited to the representation and efficient analysis of multidimensional data (Kimball and Strehlo 1995). For this reason, an alternative conceptual model is required for OLAP systems. The multidimensional data model or data cube is a popular model used to conceptualize the data in a data warehouse (Chauduri and Dayal 1997). We emphasize that the data cube that we are referring to here is a data model, and is not to be confused with the well-known CUBE operator, which performs extended grouping and aggregation of the data.

The data cube contains points or “cells” that are measures or values based on a set of dimensions. For example, consider a retail sales application where the dimensions of interest may include, CUSTOMER, PRODUCT, LOCATION, and TIME. If the measure of interest in this application is sales amount, then a point represents the sales measure corresponding to the CUSTOMER, PRODUCT, LOCATION, and TIME dimensions. In Figure 1, a data cube is provided which shows the PRODUCT, LOCATION, and TIME dimensions. A cell corresponds to the sales value for the corresponding PRODUCT, LOCATION, and TIME. For example, the upper rightmost cell of the cube corresponds to sales for PRODUCT “P1” in “Seattle” for 1994. This representation is similar to the data model used for statistical databases, where the dimensions are actually categories and the measures are summaries (Shoshani 1997).

Figure 1 Data Cube for Sales Application  
![](/api/attachments/GKBV48ZY/fulltext/images/8c5ba3f49adb7a48f0fb1b8814c103c1e272366c32e45449d4c52af44d4f4d07.jpg)

Figure 2 Snowflake Schema for Sales Application  
![](/api/attachments/GKBV48ZY/fulltext/images/6cbc5b4c26ab408355dcaa1bd02f81a792783e2131a1eb4c04fca3f5b6972a4f.jpg)

Dimensions often form a hierarchy. For instance, the TIME dimension may form a day-month-year hierarchy and the LOCATION dimension may form a city-state-region hierarchy. Dimensions allow different levels of granularity in the warehouse. For example, region corresponds to a high level of granularity whereas city corresponds to a low level of granularity.

Having discussed data modeling in OLAP systems, we now briefly discuss implementation and design. There are two main implementation methods to support OLAP applications: multidimensional OLAP (MOLAP) servers and relational OLAP (ROLAP) servers. The MOLAP approach physically stores the data in array-like structures that are similar to the data cube presented in Figure 1. In the ROLAP approach, the data is stored in a relational database using a special schema instead of a traditional relational design. The highly normalized form of conventional design methodologies is inappropriate in an OLAP environment for performance reasons. A high degree of normalization entails a large number of joins, which greatly increases response times, especially given the size of most data warehouses. For this reason, a special schema known as the star schema (or its variants the snowflake and the constellation schema) is often used. A star schema usually consists of a single fact table and a dimension table for each dimension. The fact table contains foreign keys to each dimension table, along with the actual metric data (e.g., sales amount). An extended version of the star schema, the snowflake schema, is often used to represent the dimensional hierarchies in normalized form. A possible snowflake schema is presented in Figure 2 for the sales application. This figure displays the day-month-year and citystate-region hierarchies as somewhat normalized.

There are several research issues in data warehousing including data loading, view materialization, and access methods. Since the data in a data warehouse often originates from multiple production systems, a cleaning process is usually employed, which checks for and removes integrity problems. The timing and method of loading is also critical, since the volume of data tends to be high. To improve query response times, some data is often preaggregated in a data warehouse, an approach known as view materialization. However, there is a trade-off between response times and the storage requirements of preaggregated data. Determining how much data to preaggregate is an issue that has been addressed in Gupta et al. (1995) and Harinarayan et al. (1996). Access methods in data warehouses are also being examined to improve query response times. Specialized indexing strategies have been proposed and evaluated in O’Neil and Quass (1997). Having provided an overview of data warehousing, we now discuss the contributions of our work.

## 4. Contributions of This Paper

The contributions of the research presented in this paper are threefold:

1. We provide a detailed description of the requirements of a “good” OLAP engine. Numerous OLAP functionalities have been suggested in various papers (Gray et al. 1997, Gyssens and Lakshmanan 1997, Agrawal et al. 1997), and most of these functionalities have been incorporated in commercial warehousing products. For instance, Red Brick Warehouse (1994) offers extensions to SQL that perform ranking, percentiles, and cumulative aggregates. The need to express these types of queries in SQL has been recognized. For instance, SQL extensions have been suggested in Kimball and Strehlo (1995) to handle ranking, percentiles, aggregate comparisons, and attribute-based grouping. In addition, in Chatziantoniou and Ross (1996), a relational algebra operator and SQL extensions have been proposed to allow aggregate comparisons to be expressed concisely. While these needs have been identified by various sources, we are aware of no single source that provides an integrated list of these functionalities. Thus we combine these requirements from the various sources and provide an integrative list of OLAP functionalities. Our intention is to provide a “fairly comprehensive” list in the sense that it satisfies the OLAP requirements that are known as of today. We believe such a list to be a nontrivial contribution—this description should serve as a guide to OLAP designers and as a basis for future research efforts.

2. We stipulate a detailed data model for the data cube—the underlying logical-level construct used to conceptualize multidimensional data. Again, this is the first such formal model proposed that attempts to encompass current OLAP functionality requirements.

3. We stipulate a detailed operations model for the data cube—a powerful yet simple algebra that operates on the data cube. Our proposed algebra allows complex OLAP queries to be expressed in a concise manner.

We now address the first contribution by presenting an integrative list of required OLAP functionalities.

## 5. Goals of a Data and Operations Model for OLAP

The first step in constructing any model is to examine carefully the various characteristics of the environment being modeled. Such an examination can then aid model validation; i.e., one can check that the proposed model possesses the same characteristics as the modeled reality. In our case the modeled environment is a multidimensional database and its associated operations. In keeping with the above-mentioned philosophy, we start out by providing an extensive examination of the required functionalities of such a system. The most important characteristic is the multidimensionality of the data. To model this characteristic, the notion of a data cube has been proposed (Chauduri and Dayal 1997) and widely accepted. In this paper we follow this lead and adopt the data cube as the fundamental underlying modeling construct to capture multidimensionality. Now we proceed to enumerate current OLAP functionality requirements in terms of operations on the data cube.

## 5.1. Data Cube Operations

Data cube operations refer to several decision support operations that have been coined in the literature based on the data cube representation of a multidimensional database, as presented in §3. Included in this class of operations are slice, dice, drill-down, roll-up, and pivot, which are further described below:

Slicing refers to selecting the dimensions used to view the cube. Referring back to Figure 1, the dimensional view provided is PRODUCT by LOCATION with TIME in the background. With this view, for instance, an analyst may see all products for all locations for 1994. This view can easily be changed using the slice operation. For example, a slice operation can change the view to PRODUCT by TIME with LOCA-TION in the background. With the resulting view, an analyst may then see all products for all years for Boston.

Dicing refers to selecting actual positions or values on a dimension. Selecting “Dallas” as the LOCATION is an example of dicing. Note that slice and dice together are (roughly) analogous to the relational algebra operators selection and projection, and have the effect of reducing the dimensionality of the cube.

Roll-up refers to increasing the level of granularity along one or more dimensional hierarchies. For example, consider again the sales cube of Figure 1, where the LOCATION dimension forms a city-stateregion hierarchy. A typical analyst in an OLAP environment may wish to see the total sales at the state level, or at an even higher level, such as the region level.

Drill-down refers to decreasing the level of granularity and is the converse of roll-up. Drill-down is essential because an analyst often examines data first at an aggregated level and then selectively examines data in more detail. For example, suppose an analyst has total sales at the region level, but would like to see the corresponding totals for each state. In other words, the analyst would like to drill-down or move down the dimensional hierarchy. Again the analyst may desire even more detail and drill-down to the city level.

Pivot refers to aggregating using two or more grouping dimensions and producing a new multidimensional view of the data having an attribute for each grouping dimension and an additional attribute for the aggregated measure (Chauduri and Dayal 1997). This operation is commonly found in multidimensional spreadsheet applications. Consider a simple example using the sales cube in Figure 1 where the dimensions are PRODUCT, LOCATION, and TIME and the desired aggregate measure is total sales by LOCATION and TIME. Hence, LOCATION and TIME are the grouping dimensions. Assuming the data values displayed in Table 1, the result of such a pivot would be a new view of the cube having LOCATION and TIME as dimensions, and total sales as a measure. A pivoted view is often displayed in a cross-tab format, as shown in Table 2. A result of the pivot operation is that values in the original cube become column headers (e.g., 1994) in the pivoted view.

Table 1 Sales Data for Pivot Example

<table><tr><td>Product</td><td>Location</td><td>Time</td><td>Sales Amount</td></tr><tr><td>P1</td><td>Boston</td><td>1994</td><td>100</td></tr><tr><td>P2</td><td>Boston</td><td>1994</td><td>200</td></tr><tr><td>P2</td><td>Boston</td><td>1995</td><td>200</td></tr><tr><td>P1</td><td>Dallas</td><td>1995</td><td>150</td></tr><tr><td>P2</td><td>Dallas</td><td>1995</td><td>150</td></tr></table>

Information Systems Research Vol. 12, No. 1, March 2001

Aside from the “data cube operations” described above, another class of operations that have been mandated for data warehousing and OLAP are aggregation operations.

## 5.2. Aggregation

In the RDBMS environment, we often view aggregation as the ability to group and summarize data using the standard SQL aggregate operators (e.g., MIN, MAX, SUM, AVG, COUNT). However, decision support systems require more complex user-defined functions. This category encompasses several types of functionalities listed below along with examples:

Ranking. An example of ranking would be to find the top five products based on sales.

Percentiles. An example of a percentile query would be to find the products in the top 5% based on sales.

Comparisons of aggregates. The most common type of query in this category is the ratio-to-total query. For example, find the ratio of each month’s sales to annual sales.

Attribute-based grouping. This type of query includes moving sums and averages. For example, find the 3- year moving average of sales values.

Trends. An example of a trend would be to find the products having sales values that have increased during each of the last six months.

The third and final class of operations required for OLAP processing are transformation operations.

## 5.3. Transformation

This class of operations provides the ability to convert dimensions to measures and vice versa, thus allowing uniform treatment of dimensions and measures. This concept allows analysis based on a variety of perspectives and is accomplished through the following operations:

Table 2 Result of Total Sales by LOCATION and TIME Pivot

<table><tr><td>Location</td><td>1994</td><td>1995</td></tr><tr><td>Boston</td><td>300</td><td>200</td></tr><tr><td>Dallas</td><td>0</td><td>300</td></tr></table>

Force refers to converting a dimension to a measure. Extract refers to converting a measure to a dimension.

These operations are best explained through examples. Consider the case where an analyst would like to see the maximum sales value for each city and year. However, along with the city and year, the analyst would also like to see the product name associated with the sale. Finding the maximum sales value for each city and year requires an aggregation over the PRODUCT dimension; hence the product\_name attribute is essentially “lost” in the aggregation process. To prevent this loss of detail, we can force the product\_name attribute into the cube cell; i.e., convert it from a dimension to a measure. Conversely, once the aggregation is complete, we can then extract product\_name from the cube cell; i.e., convert it from a measure to a dimension. The problem of expressing this type of query has been identified in Gray et al. (1995). Without transformations, this type of query must be formulated using a join operation, which is an expensive operator in the OLAP context given the size of the underlying database.

Having expressed the goals of an OLAP engine and the dire need for such capabilities, we now turn our attention to our proposed model and algebra. To accommodate the above goals requires a solid model and a rigorous algebra, such as the model and algebra that we now propose.

## 6. The Data Model

In this section we present a data model of a multidimensional database/data warehouse. Note that we use the terms multidimensional database (MDDB) and data warehouse synonymously throughout this paper. We reiterate our goals: to allow symmetric treatment of dimensions and measures and to provide the required OLAP functionality as described in the previous section.

As mentioned previously, the data cube is almost universally accepted as the underlying logical level construct to describe a multidimensional database (just as the “relation” is for a relational database). This mandates that all the operators we define (as well as their algebra) must operate on the cube structure (just as the relational algebra operators operate on the relation structure). The first step, therefore, is to define a data cube.

Definition 1 Cube. A cube is a generalized, abstract structure that serves as the foundation for the multidimensional data cube model. A cube C is defined as a six-tuple $\langle C , A , f , d , O , L \rangle$ where:

• C is a set of m characteristics $\{ c _ { 1 } , c _ { 2 } , \ldots , c _ { m } \}$ where each $c _ { i }$ is a characteristic having domain (dom) C.

• A is a set of t attributes $\{ a _ { 1 } , a _ { 2 } , \ldots , a _ { t } \}$ where each $a _ { i }$ is an attribute name having domain dom A. We assume that there exists an arbitrary total order on A, $\leq _ { A }$ . Thus, the attributes in A (and any subset of A) can be listed according to $\leq _ { A } .$ Moreover we say that each $a _ { i } \in A$ is recognizable to the cube C.

• f is a one-to-one mapping, $f \colon C \to 2 ^ { A } .$ , which maps a set of attributes to each characteristic. The mapping is such that attribute sets corresponding to characteristics are pairwise disjoint, i.e., $\forall i , j , i \neq j , f ( c _ { i } ) \cap f ( c _ { j } )$ $= \emptyset$ . Also, all attributes are mapped to characteristics $( { \mathrm { i . e . , ~ } } \forall x , x \in A , \exists c , c \in C , x \in f ( c ) )$ . Hence, f partitions the set of attributes among the characteristics. We refer to f(c) as the schema of c.

• d is a boolean-valued function that partitions C into a set of dimensions $D$ and a set of measures M. Thus, $C \ = \ D \cup \ M$ where $D \cap M = \emptyset$ . The function d is defined as follows:

$$
\forall x \in C, d (x) = \left\{ \begin{array}{l l} 1 & \text { if } x \in D, \\ 0 & \text { otherwise }. \end{array} \right.
$$

• O is a set of partial orders such that each $o _ { i } \in O$ is a partial order defined on $f ( c _ { i } )$ and $| O | ~ = ~ | C |$ . In other words, the schema for each characteristic $c _ { i } ,$ has a partial order $o _ { i }$ associated with it.

• L is a set of cube cells. A cube cell is represented as an address, content- pair.

—The address in this pair is an n-tuple, $\langle \alpha _ { 1 } , \alpha _ { 2 } , \ldots ,$ $\alpha _ { n } \rangle _ { - }$ , where n is the number of dimensional attributes in the cube, i.e., $n \ = \ \vert { \cal A } _ { d } \vert$ , where $A _ { d }$ represents the set of all dimensional attributes; i.e., $A _ { d }$ $= \cup _ { d _ { i } \in D } f ( d _ { i } )$ . Each address component, $\alpha _ { i } ,$ represents a position along the “axis” of a dimensional attribute. $\alpha _ { i }$ corresponds to the ith dimensional attribute in A based on $\leq _ { A } ( \mathrm { e . g . }$ , the third component of the address, $\alpha _ { 3 } ,$ corresponds to the third dimensional attribute in A in $\leq _ { A } .$ -order).

—The content of a cube cell is defined similarly. It is a k-tuple, $\langle \chi _ { 1 } , \chi _ { 2 } , \ldots , \chi _ { k } \rangle .$ , where k is the number of metric attributes in the cube; i.e., $k ~ = ~ \vert A _ { m } \vert$ 7 where $A _ { m }$ represents the set of all metric attributes; i.e., $A _ { m } = \cup _ { m _ { i } \in M } f ( m _ { i } )$ . Each content component, $\chi _ { i } ,$ represents the element of the content that corresponds to a particular metric attribute. $\chi _ { i }$ corresponds to the ith metric attribute in A in <sub>A</sub>-order.

Remarks. For notational convenience, we define g to be a mapping g: $A  C ,$ , such that $g ( a ) = c { \mathrm { ~ i f f ~ } } a \in f ( c )$ Hence, if the schema of a characteristic c contains attribute a, then g maps a to c. Also for notational convenience, we denote the structural address component of L as L.AC and the structural content component as L.CC. We denote the ith address value component of cube cell l as l.AC[i] and the ith content value component as l.CC[i].

We now provide an example to clarify this definition. Subsequently, this will be used as a running example for the rest of the paper. Consider a cube Sales which represents a multidimensional database of sales figures of certain products. The Sales cube has the following features (note the correspondence of the example to the definition above).

• The data are described by the characteristics time, product, location, and sales. Hence, the cube has a characteristics set C  {time, product, location, sales} (m  4).

• The time characteristic is described by the attributes day, week, month, and year; th e product characteristic is described by the product\_name, weight and color attributes; the location characteristic is described by the store\_name, city, state, and region attributes. The sales characteristic is described by the amount and quantity attributes. Thus, for the Sales cube, A  {day, week, month, year, product\_name, weight, color, store\_name, city, state, region, amount, quantity} (t  13).

• Each of the characteristics, as explained in the previous item, are described by specific attributes. In other words, for the Sales cube, the mapping f is as follows:

Also note that the attribute sets shown above are mutually disjoint.

• The users are interested in analyzing sales figures along three dimensions, namely time, product, and location. In other words users are interested in asking questions such as “what was the total sales of product $P _ { l }$ in a certain location” (querying along the product and location dimension), or “what was the total sales of $P _ { l }$ in a certain location during a specific time interval” (querying along all three dimensions). Hence, the metric of interest is sales and the dimensions are time, product, and location. The function d then evaluates to true for the time, product, and location characteristics (.e.g, d(time)  1) and to false for the sales characteristic. Thus d partitions the Sales cube into a set of dimensions D  {time, product, location} and a set of measures M  {sales}.

• An example of a partial order in O on the Sales cube is given by the following:

$$
\begin{array}{r l} O _ {t i m e} & = \{\langle d a y, w e e k \rangle , \langle d a y, m o n t h \rangle , \langle d a y, y e a r \rangle , \\ & \quad \langle m o n t h, y e a r \rangle \}, \\ O _ {p r o d u c t} & = \{\langle p r o d u c t \_ n a m e, w e i g h t \rangle , \\ & \quad \langle p r o d u c t \_ n a m e, c o l o r \rangle \}, \\ O _ {l o c a t i o n} & = \{\langle s t o r e \_ n a m e, c i t y \rangle , \langle c i t y, s t a t e \rangle , \\ & \quad \langle s t a t e, r e g i o n \rangle \}, \\ O _ {s a l e s} & = \{\}. \end{array}
$$

• To present a simple example of L, we assume the following attributes and corresponding domains for the Sales cube data:

$$
\begin{array}{r l} A & = \{\text { year }, \text { product\_name }, \text { city }, \\ & \quad \text { amount }, \text { quantity } \}, \end{array}
$$

$$
\text { dom   year } = \{1 9 9 4, 1 9 9 5, 1 9 9 6 \},
$$

dom product\_name  {P1, P2, P3},

$$
\text {   dom   city   } = \{\text { Boston, Dallas, Seattle } \},
$$

$$
\text { dom   amount } = \{0, 1, 2, \dots \},
$$

$$
\text { dom   quantity } = \{0, 1, 2, \dots \}.
$$

• Then an element l  L may be expressed as follows:

$$
l = \langle l. A C, l. C C \rangle \text {   where:   }
$$

$$
\begin{array}{l} l. A C = \langle 1 9 9 4, P 1, B o s t o n \rangle , \text { corresponding   to } \\ \text { the   structural   components: } \end{array}
$$

$$
l. A C = \langle \text { year }, \text { product\_name }, \text { city } \rangle
$$

$$
l. C C = \langle 1 0 0, 1 0 \rangle , \text {   corresponding   to   the   }
$$

$$
l. C C = \langle \text { amount }, \text { quantity } \rangle .
$$

![](/api/attachments/GKBV48ZY/fulltext/images/b799736344cb95b42557d4fa8e87aef3d82f3edddccc0f459a60e492930926e0.jpg)  
Figure 3 Data Cube Example with Notation

A possible cube using the data from above is shown below pictorially in Figure 3. Henceforth, we will work with cubes in the development of theory in this paper.

## 7. The Proposed Operators

In this section we present an algebra for OLAP based on the cube model defined in the previous section. We use the cube shown in Figure 3 as a running example to illustrate the operators. As is the norm, our algebra consists of a set of operators. We will use simple logical formulas to state our operator definitions. At the outset we present the notation (refer to Table 3) and some preliminary definitions. We then present each operator using the following format: the operator name, symbol, a textual description, input, output, mathematical notation, and a simple example of the operator. More complex examples are given in §8.

Definition 2 Predicate. We define a predicate as a well-formed formula in first-order predicate logic. A predicate $P ,$ may be:

(i) an atomic predicate where P is a restriction on the domain of a single variable.

(ii) a compound predicate of the form:

$$
P = p _ {1} \langle o p \rangle p _ {2} \langle o p \rangle \dots \langle o p \rangle p _ {1},
$$

where each $p _ { i }$ refers to an atomic predicate and oprepresents a logical connector, which may include <sup>#</sup> (and), $\lor ( \mathrm { o r } ) , \neg ( \mathrm { n o t } ) ,  ( \mathrm { i m p l i e s } ) .$ , and ↔ (equivalent to).

A Simple Example. Referring to the Sales cube in §6, an example of a predicate would be (year  1994) $\wedge ( \mathrm { c i t y } = " { \mathrm { S e a t t l e } } ^ { \prime \prime } )$

Definition 3: l Satisfies P. Let l be a cell of a cube C with address component l.AC and content component l.CC. Let P be a predicate comprised of variables which are attribute names recognizable to C. l satisfies P if and only if the following hold:

Case 1. P is atomic (assume attribute a appears in P).

(a) if $a \in f ( d _ { i } ) , d _ { i } \in D _ { \cdot }$ , then $P ( l . A C [ a ] ) \colon = \mathrm { T R U E }$

(b) if $a \in f ( m _ { i } ) , m _ { i } \in M$ , then $P ( l . C C [ a ] ) \colon = \mathrm { T R U E }$

Case 2. P is compound, $P = p _ { 1 } \langle o p \rangle p _ { 2 } \langle o p \rangle \cdots \langle o p \rangle p _ { n } .$

(a) $\forall p _ { i } \in P ,$ let $Q _ { i }$ denote the truth value of $p _ { i }$ evaluated on l.

$$
(b) Q _ {1} \langle o p \rangle Q _ {2} \langle o p \rangle \dots \langle o p \rangle Q _ {n} := \text { TRUE }.
$$

A Simple Example. Referring once again to the Sales cube, the upper rightmost cell in the cube satisfies the predicate $( \mathrm { y e a r } = 1 9 9 4 ) \wedge ( \mathrm { c i t y } = { } ^ { \prime \prime } \mathrm { S e a t t l e } ^ { \prime \prime } ) \wedge$ (product $\mathrm { n a m e } = \mathit { ^ { \prime \prime } P 1 ^ { \prime \prime } } )$

Table 3 Table of Notation

<table><tr><td>Symbol</td><td>Description</td></tr><tr><td> $C$ </td><td>set of characteristics</td></tr><tr><td> $A$ </td><td>set of attribute names</td></tr><tr><td> $f$ </td><td>a mapping that yields schemas of characteristics</td></tr><tr><td> $D$ </td><td>set of dimensions,  $D \subseteq C$ </td></tr><tr><td> $M$ </td><td>set of measures,  $M \subseteq C$ </td></tr><tr><td> $d$ </td><td>boolean-valued function partitioning  $C$  into  $D$  and  $M$ </td></tr><tr><td> $A_{d}$ </td><td>set of dimensional attributes</td></tr><tr><td> $A_{m}$ </td><td>set of metric attributes</td></tr><tr><td> $O$ </td><td>set of partial orders</td></tr><tr><td> $L$ </td><td>set of cube cells</td></tr><tr><td> $L.AC$ </td><td>structural address component of cube cell</td></tr><tr><td> $L.CC$ </td><td>structural content component of cube cell</td></tr><tr><td> $I.AC[i]$ </td><td> $i$ th address value component</td></tr><tr><td> $I.CC[i]$ </td><td> $i$ th content value component</td></tr><tr><td> $g$ </td><td>a mapping  $g:A \to C$ </td></tr><tr><td> $p$ </td><td>atomic predicate</td></tr><tr><td> $P$ </td><td>compound predicate</td></tr><tr><td> $\circ$ </td><td>concatenation operator</td></tr><tr><td> $\Sigma$ </td><td>restriction operator</td></tr><tr><td> $\Pi^{M}$ </td><td>metric projection operator</td></tr><tr><td> $S$ </td><td>set of projection attributes</td></tr><tr><td> $\Lambda$ </td><td>rename operator</td></tr><tr><td> $\otimes$ </td><td>cubic product operator</td></tr><tr><td> $\Theta$ </td><td>join operator</td></tr><tr><td> $\cup$ </td><td>union operator</td></tr><tr><td> $\theta$ </td><td>difference operator</td></tr><tr><td> $\cap$ </td><td>intersection operator</td></tr><tr><td> $G$ </td><td>set of grouping attributes</td></tr><tr><td> $F$ </td><td>aggregate function  $F: 2^{\Pi_{\forall g \in G^{dom_{w}}}} \to \text{dom}_{agg}$ </td></tr><tr><td> $\Psi$ </td><td>force operator</td></tr><tr><td> $\Phi$ </td><td>extract operator</td></tr></table>

Restriction (R). The restriction operator restricts the values on one or more attributes based on specified conditions, where a given condition is in the form of a predicate. Thus, a set of predicates is evaluated on selected attributes, and cube cells are retrieved only if they satisfy a given predicate. If there are no cube cells that satisfy P, the result is an empty cube. The algebra of the restriction operator is then defined as follows:

$$
C _ {I} = \langle C, A, f, d, O, L \rangle
$$

• Output: A cube $\mathrm { C } _ { O } = \langle C , A , f , d , O , L _ { O } \rangle$ where $L _ { O } \subseteq L$ and $L _ { O } = \{ l | ( l \in L ) \land ( l$ satisfies P)}.

• Mathematical Notation: $\Sigma _ { P } ( C _ { I } ) = C _ { O } .$

• A Simple Example: Assume the user would like to know the sales values for all products in all cities during 1994. Such a query can be answered by the following operation on the Sales cube: $\Sigma _ { \mathrm { ( y e a r = 1 9 9 4 ) } } \ ( \bf { S a l e s } ) =$ $\mathbf { C _ { R e s u l t } } .$

Metric Projection $( I I ^ { \mathrm { M } } )$ . The metric projection operator restricts the output of a cube to include only a subset of the original set of measures. Let S be a set of projection attributes such that $S \subseteq A _ { \mathrm { m } } .$ Then the output of the resulting cube includes only those measures in S. The algebra of metric projection is defined as follows:

• Input: A cube $C _ { I } = \langle C , A , f , d , O , L \rangle$ and a set of projection attributes S.

• Output: A cube $C _ { O } ~ = ~ \langle C , A _ { O } , f _ { O } , d , O , L _ { O } \rangle$ where ${ \cal A } _ { \cal O } = { \cal S } \cup { \cal A } _ { d } , f _ { \cal O } : { \cal C }  2 _ { \phantom { A } \rho } ^ { A } , \mathrm { s u c h } \mathrm { t h a t } f _ { \cal O } ( c ) = f ( c ) \cup { \cal A } _ { \cal O } ,$ and $\begin{array} { r } { L _ { O } = \{ l _ { O } | \exists l \in L , l _ { O } . \bar { A C } = l , A C , l _ { O } . C C = \langle l . C C [ s _ { 1 } ] , } \end{array}$ $l . C C [ s _ { 2 } ] , \ldots , l . C C [ s _ { n } ] \rangle \}$ , where $\{ s _ { 1 } , s _ { 2 } , \ldots , s _ { n } \} = S .$

• Mathematical Notation: $I I _ { S } ^ { \mathrm { M } } \left( C _ { I } \right) = C _ { O } .$

• A Simple Example: Referring to the previous example, suppose the user is only interested in the amount metric. The query in the previous example can be modified to project only the amount metric using the following operation:

$$
\Pi_ {\text {amount}} ^ {\mathrm{M}} (\Sigma_ {\text {year} = 1 9 9 4} (\text {Sales})) = C _ {R e s u l t}.
$$

Rename (K). The rename operator is a set operator similar to the rename used in standard relational query languages. This operator is used in subsequent operator definitions and is not one of our basic cube operators. We define rename as follows: Let $S _ { I }$ be some set of elements $\{ s _ { 1 1 } , \ s _ { 1 2 } , \ldots , \ s _ { I n } \}$ . Then, $\Lambda _ { S } ~ ( S _ { I } ) ~ = ~ \{ S . s _ { 1 1 } ,$ $S . s _ { 1 2 } , \ldots , s . s _ { I n } \}$ . Thus, rename can be applied to any set. For example, it is often useful to rename attributes when performing certain binary operations on cubes to ensure that duplicate attribute names do not exist in the resulting cube. Renaming the attributes corresponding to the time dimension of the Sales cube can be expressed as follows: $\begin{array} { l c l } { { \Lambda _ { S a l e s } } } & { { ( A ) } } & { { = } } & { { \{ S a l e s . d a y _ { , } } }  \end{array}$ Sales.week, Sales.month, Sales.year}

Cubic Product (). The Cubic Product operator is a binary operator that can be used to relate any two cubes. Often it is useful to combine the information in two cubes to answer certain queries (which we will illustrate with an example). The algebra of the Cubic Product operator is defined as follows:

• Input: A cube $\boldsymbol { C } _ { 1 } = \langle \boldsymbol { C } _ { 1 } , \boldsymbol { A } _ { 1 } , \boldsymbol { f } _ { 1 } , \boldsymbol { d } _ { 1 } , \boldsymbol { O } _ { 1 } , \boldsymbol { L } _ { 1 } \rangle$ and a cube $C _ { 2 } = \langle C _ { 2 } , A _ { 2 } , f _ { 2 } , d _ { 2 } , O _ { 2 } , L _ { 2 } \rangle .$

• Output: A cube $C _ { O } = \langle C _ { O } , A _ { O } , f _ { O } , d _ { O } , O _ { O } , L _ { O } \rangle _ { \mathrm { t } }$ , where $C _ { O } = \ A _ { c 1 } \left( C _ { 1 } \right) \cup \ A _ { c 2 } \left( C _ { 2 } \right) ; A _ { O } = \ A _ { c 1 } \left( A _ { 1 } \right) \cup A _ { c 2 } \left( A _ { 2 } \right) ; L _ { O }$ $= \{ l _ { O } | \exists l _ { 1 } , \exists l _ { 2 } , l _ { 1 } \in L _ { 1 } , l _ { 2 } \in L _ { 2 } , l _ { O } . A C = l _ { 1 } . A C \cdot l _ { 2 } . A C ,$ $l _ { O } . C C = l _ { 1 } . C C \cdot l _ { 2 } . C C \}$ , where $a \cdot b$ denotes the concatenation of a and b. In addition:

$$
\begin{array}{l} \forall c _ {i} \in (C _ {1} \cup C _ {2}), \\ f _ {O} = \left\{ \begin{array}{l l} f _ {1} & \text {when applied to c_{i} \in C_{1}.c_{i}}, \\ f _ {2} & \text {when applied to c_{j} \in C_{2}.c_{i}}, \end{array} \right. \end{array}
$$

$$
\forall c _ {i} \in (C _ {1} \cup C _ {2}),
$$

$$
d _ {O} = \left\{ \begin{array}{l l} d _ {1} & \text { when   applied   to } c _ {i} \in C _ {1}. c _ {i}, \\ d _ {2} & \text { when   applied   to } c _ {j} \in C _ {2}. c _ {i}, \end{array} \right.
$$

$$
\forall a _ {i} \in (f (C _ {1}) \cup f (C _ {2})),
$$

$$
\mathrm{O} _ {O} = \left\{ \begin{array}{l l} O _ {1} & \text { when   applied   to } a _ {i} \in f (C _ {1}), \\ O _ {2} & \text { when   applied   to } a _ {j} \in f (C _ {2}). \end{array} \right.
$$

• Mathematical Notation: $c _ { 1 } \otimes c _ { 2 } = c _ { O } .$

• A Simple Example. Consider another cube, Discount, containing discount amounts for various combinations of product and city. More formally, the Discount cube has characteristics $C \ = \ \{ p r o d u c t .$ , location discount}, measure M  {discount}, dimensions $D =$ {product, location} and A  {product\_name, $\mathtt { c i t y \_ I D }$ amount}, where product\_name maps to the productcharacteristic, city\_ID maps to location, and amount maps to discount. Suppose the user would like to know which discount amounts apply to the various cities and products in the Sales cube. To answer this query, the user may first apply the Cubic Product operation to the Sales and Discount cubes as follows: Sales  $\mathbf { D i s c o u n t } = \mathbf { c } _ { \mathrm { R e s u l t } } .$ Note that the result of this operation is a superset of the desired information. Further operations are required to extract the actual answer. Also note that the Cubic Product operator places no restrictions on the domains of the attributes.

Remarks. The join (H) operator is based on the cubic product operator. Join is used to relate two cubes having one or more dimensions in common, and having identical mappings from the common dimensions to the respective attribute sets of these dimensions. In other words, two cubes $C _ { 1 } = \langle C _ { 1 } , A _ { 1 } , f _ { 1 } , d _ { 1 } , O _ { 1 } , L _ { 1 } \rangle$ and $C _ { 2 } = \langle C _ { 2 } , A _ { 2 } , f _ { 2 } , d _ { 2 } , O _ { 2 } , L _ { 2 } \rangle$ are join-compatible if $D _ { 1 } \cap$ $D _ { 2 } \neq { \cal O } ,$ , and ∀ $c _ { i } \in D _ { 1 } \cup D _ { 2 } , f _ { 1 } ( c _ { i } ) = f _ { 2 } ( c _ { i } )$ . Furthermore, let cd be the set of common dimensions such that $c d =$ $D _ { 1 } \cap D _ { 2 } = \{ c d _ { 1 } , c d _ { 2 } , . . . , c d _ { 1 } \}$ and $A _ { c d } = \{ a _ { c d 1 } , a _ { c d 2 } , . . . ,$ $a _ { c d m } \}$ denote the set of common dimensional attributes corresponding to cd. Hence, $A _ { c d } = \cup _ { \forall c d _ { i } \in c d } f ( c d _ { i } )$ and $A _ { c d } \subseteq A _ { d } .$ . The algebra of join may be succinctly expressed through the following identity: ${ \cal C } _ { 1 } \Theta { \cal C } _ { 2 } =$ $\Sigma _ { P } ( C _ { 1 } \otimes C _ { 2 } )$ where P is a predicate of the form $\operatorname { I } ( C _ { 1 } { \cdot } a _ { \mathrm { c d l } }$ $ = C _ { 2 } \cdot a _ { \mathrm { c d l } } ) \wedge ( C _ { 1 } \cdot a _ { \mathrm { c d 2 } } = C _ { 2 } \cdot a _ { \mathrm { c d 2 } } ) \wedge , \ldots , \wedge ( C _ { 1 } \cdot a _ { \mathrm { c d m } } =$ $C _ { 2 } { \cdot } a _ { \mathrm { c d m } } ) ]$

A Simple Example. Consider the query in the previous example: the user would like to know which discount amounts apply to the various cities and products in the Sales cube. The answer to this query can be obtained easily by joining the Sales and Discount cubes as follows: Sales H Discount $\begin{array} { r } { \mathbf { \Phi } = \mathbf { c _ { \mathrm { R e s u l t } } } . } \end{array}$

The next two operators are binary operators<sup>2</sup> which require as input two union-compatible cubes. Intuitively, two cubes are union-chcompatible if they have the same structure. More formally, two cubes $C _ { 1 } =$ $\langle C _ { 1 } , A _ { 1 } , f _ { 1 } , d _ { 1 } , O _ { 1 } , L _ { 1 } \rangle$ and $\begin{array} { c c l } { C _ { 2 } } & { = } & { \langle C _ { 2 } , A _ { 2 } , f _ { 2 } , d _ { 2 } , O _ { 2 } , L _ { 2 } \rangle } \end{array}$ are union-compatible if $C _ { 1 } = C _ { 2 } , A _ { 1 } = A _ { 2 } , f _ { 1 } = f _ { 2 } , d _ { 1 } = d _ { 2 } ,$ and $O _ { 1 } = O _ { 2 } .$

Union (). The union operator is a binary operator that finds the union of two cubes. The algebra of the union operator is defined as follows:

• Input: A cube $\boldsymbol { C } _ { 1 } = \langle \boldsymbol { C } _ { 1 } , \boldsymbol { A } _ { 1 } , \boldsymbol { f } _ { 1 } , \boldsymbol { d } _ { 1 } , \boldsymbol { O } _ { 1 } , \boldsymbol { L } _ { 1 } \rangle$ and a cube $C _ { 2 } = \left. C _ { 2 } , A _ { 2 } , f _ { 2 } , d _ { 2 } , O _ { 2 } , L _ { 2 } \right.$ such that $C _ { 1 }$ and $C _ { 2 }$ are unioncompatible.

• Output: A cube $\begin{array} { r } { C _ { O } = \langle C _ { O } , A _ { O } , f _ { O } , d _ { O } , O _ { O } , L _ { O } \rangle } \end{array}$ where $C _ { O } = C _ { 1 } = C _ { 2 } ; A _ { O } = A _ { 1 } = A _ { 2 } ; f _ { O } = f _ { 1 } = f _ { 2 } ; d _ { O } = d _ { 1 }$ $\quad = d _ { 2 } ; O _ { O } = O _ { 1 } = O _ { 2 } ; L _ { O } = L _ { 1 } \cup L _ { 2 } .$

• Mathematical Notation: $C _ { 1 } \cup C _ { 2 } = C _ { O } .$

• A Simple Example: Consider two cubes, Sales\_ East and Sales\_West, both having the same cube structure as defined for the Sales cube, where Sales\_East contains sales data corresponding to the Eastern region and Sales\_West contains sales data corresponding to the Western region.<sup>3</sup> Suppose the user would like to combine the data for the two regions into a single cube. This operation can be accomplished using the union operator as follows: Sales\_East  Sales\_West  $\mathbf { C _ { R e s u l t } }$ , which results in a single cube containing sales data that appear in either or both regions (if the latter case is possible).

Difference (h). The difference operator is a binary operator that finds the difference of two cubes. The algebra of the difference operator is defined as follows: • Input: A cube $\boldsymbol { C } _ { 1 } = \langle \boldsymbol { C } _ { 1 } , \boldsymbol { A } _ { 1 } , \boldsymbol { f } _ { 1 } , \boldsymbol { d } _ { 1 } , \boldsymbol { O } _ { 1 } , \boldsymbol { L } _ { 1 } \rangle$ and a cube $C _ { 2 } = \langle C _ { 2 } , A _ { 2 } , f _ { 2 } , d _ { 2 } , O _ { 2 } , L _ { 2 } \rangle$ such that $C _ { 1 }$ and $C _ { 2 }$ are unioncompatible.

• Output: A cube $\begin{array} { r } { C _ { O } = \langle C _ { O } , A _ { O } , f _ { O } , d _ { O } , O _ { O } , L _ { O } \rangle } \end{array}$ where $C _ { O } = C _ { 1 } = C _ { 2 } ; A _ { O } = A _ { 1 } = A _ { 2 } ; f _ { O } = f _ { 1 } = f _ { 2 } ; d _ { O } = d _ { 1 }$ ${ \bf \Gamma } = d _ { 2 } ; O _ { O } = O _ { 1 } = O _ { 2 } ; L _ { O } = L _ { 1 } - L _ { 2 } .$

• Mathematical Notation: ${ \cal C } _ { 1 } \theta { \cal C } _ { 2 } = { \cal C } _ { O } .$

• A Simple Example: Consider again the Sales\_West cube and also a cube Sales\_CA, having the same cube structure as defined for the Sales cube, where Sales\_CA contains sales data corresponding to California, which belongs to the Western region. Suppose the user would like to find sales information for customers in the Western region who are not in California. This operation can be accomplished using the difference operator as follows: Sales\_West h Sales $\begin{array} { r } { { \bf \nabla } _ { - } { \bf C } { \bf A } = } \end{array}$ $\mathbf { C _ { R e s u l t } } .$

Remarks. The difference operator essentially removes the portion of cube $C _ { 1 }$ that is common to both cubes $C _ { 1 }$ and $C _ { 2 } .$ An additional operation, intersection, can be expressed in terms of the difference operator as follows: $C _ { 1 } \theta ( C _ { 1 } \theta C _ { 2 } ) = C _ { O }$ . Note that intersection is not a fundamental operator since it can be expressed in terms of other operators. For convenience, intersection may also be expressed as: ${ \cal C } _ { 1 } \cap { \cal C } _ { 2 } = { \cal C } _ { O } .$

Aggregation (C). The aggregation operator performs aggregation on one or more dimensional attributes. This operator encompasses not only the standard SQL aggregate functions $( \mathrm { e . g . }$ , MIN, MAX, SUM, AVG, COUNT), but also repeated additions and multiplications over a set of items, thus allowing more complex computations (e.g., n-tiles, roll-ups).

Let G be a set of grouping attributes such that $G \subseteq A _ { \mathrm { d } } .$ Let met be a metric attribute to aggregate where met $\in A _ { m } .$ Let F be an aggregate function having the following mapping: F: $2 ^ { \Pi _ { \mathrm { v g i } } \in \mathrm { \check { G } } ^ { \mathrm { d o m _ { \mathrm { g i } } } } } \to d o m _ { a g g } ,$ where agg represents some user-specified attribute name given to the result, which is extracted from domain dom agg. We assume that F is a first-order definable function including the standard arithmetic operations $+ , - , \times .$ , and , the standard SQL aggregate functions, and a RANK function, which we now define. The RANK function can be used to answer queries that require the ordering of cube cells. RANK takes as input a group of cube cells and returns an attribute agg corresponding to the ordinal number of the cell. An example of a query using RANK is included in $\ S \ 8 .$ The algebra of the aggregation operator is defined as follows:

• Input: A cube $C _ { I } = \langle C , A , f , d , O , L \rangle$ , a set of grouping attributes G, a metric attribute met, and an aggregate function F.

• Output: A cube $\begin{array} { r } { C _ { O } = \langle C _ { O } , A _ { O } , f _ { O } , d _ { O } , O _ { O } , L _ { O } \rangle } \end{array}$ where $c _ { O } = \{ c | c \in C , \exists x , x \in G , x \in f ( c ) \} \cup \{ A G G \}$ and {AGG} is the characteristic name defined specifically for aggregated metrics; $A _ { O } = G \cup$ {agg} and {agg} represents the computed aggregate attribute; $L _ { O } = \{ l _ { O } | \exists l \in L ,$ $1 _ { O } . A C ~ = ~ \langle l . A C [ g _ { 1 } ] , ~ l . A C [ g _ { 2 } ] , \ldots , ~ l . A C [ g _ { \mathrm { n } } ] \rangle , ~ l _ { O } . C C ~ =$ $\langle l . C C [ a g g ] \rangle { \mathrm { ! } }$ . In addition:

$$
f _ {O} = \left\{ \begin{array}{l} \{\langle x, y \rangle |   x \in C _ {O}, \langle \exists \langle x, z \rangle \in f, x \neq \{A G G \}, \\ \quad y; = \{a   |   a \in (z \cap A _ {O}) \}) \\ \quad \lor (\exists \langle x, z \rangle \in f, x = \{A G G \}, y = \{a   |   a \in (z \cap A _ {O}) \cup \{a g g \} \}) \} \\ \quad \text {if} \exists \langle \{A G G \}, z \rangle \in f, \\ \{\langle x, y \rangle |   x \in C _ {O}, (\exists \langle x, z \rangle \in f, \\ \quad y = \{a   |   a \in (z \cap A _ {O}) \}) \} \cup \{\langle \{A G G \}, \{a g g \} \rangle \} \\ \quad \text {otherwise.} \end{array} \right.
$$

$$
\forall x \in C, d _ {O} (x) = \left\{ \begin{array}{l} d (x) \quad \text { if } \{A G G \} \in C, \\ d (x) \cup \langle A G G, 0 \rangle \quad \text { otherwise }. \end{array} \right.
$$

• Mathematical Notation: ${ \cal T } _ { \mathrm { F } , G , m e t } ( { \bf C } _ { 1 } ) = { \cal C } _ { O } .$

• A Simple Example: Suppose the user would like to display total annual sales for each product regardless of location. Hence, the user wants to sum over the location dimension, and group the result using the product\_name and year attributes. Thus, $\mathtt { F } = \mathtt { S U M }$ (the standard SQL operator) and G  {product \_name, year}. This query can be answered using the following operation on the Sales cube:

• C <sub>[SUM,{product\_name,year},</sub> <sub>amount]</sub> $( S \mathbf { a l e s } ) = \mathbf { C } _ { \mathrm { R e s u l t } } .$

The next two operators can be categorized as transformation operators. OLAP queries often require that measures be treated as dimensions and vice versa. At times, it may be necessary to perform join or aggregation operations based on metric attributes. However, both the join and aggregation operators are based on dimensional attributes, and so a metric attribute must first be converted to a dimensional attribute to answer such queries. For example, consider the following query on the Sales cube: For each product, find the maximum quantity sold and the name of the store where the sale was made. To answer this query requires that the store\_name attribute, a dimensional attribute, be retained with the resulting grouping attributes even though it is not itself a grouping attribute. This can be accomplished by forcing store\_name into the content portion of the cube cell, and hence, converting it from a dimension to a measure. Conversely, dimensions often must be treated as measures and therefore, an operation is also required to transform dimensions to measures. The force and extract operators perform such transformations and thus allow the uniform treatment of dimensions and measures. We will provide the complete formulation for the above query in a later section. For now, we proceed to describe the force and extract operators.

Force (W ). The force operator converts dimensions to measures. Let $a _ { t }$ be a dimensional attribute to transform such that $g ( a _ { t } ) \in D$ . Let $c _ { t }$ be the corresponding characteristic name for $a _ { t }$ such that $c _ { t } \notin D$ and either $c _ { t }$  M or $c _ { t }$ is a new characteristic name. The algebra of the force operator is defined as follows:

• Input: A cube $C _ { I } \ = \ \langle C , A , f , d , O , L \rangle$ , a dimensional attribute to transform $a _ { t } ,$ and a corresponding characteristic name $c _ { t } .$

• Output: A cube $\mathsf { C } _ { O } = \langle C _ { O } , A _ { O } , f _ { O } , d _ { O } , O _ { O } , L _ { O } \rangle$ where $C _ { O } = C \cup \{ c _ { t } \} ; f _ { O } = f - f ( g ( a _ { t } ) ) + [ g ( a _ { t } ) \to f ( g ( a _ { t } ) - a _ { t } ) ]$ $+ ~ [ c _ { t } \to a _ { t } ] ^ { 4 } ; O _ { O } = O _ { p r e v } \cup O _ { n e w }$ where $O _ { p r e v }$ is obtained by removing from O those ordered pairs containing $a _ { t } ,$ and $O _ { n e w }$ represents a user specified set of ordering relations between $a _ { t }$ and the elements of $f ( c _ { t } ) { \mathrm { ~ i f ~ } } c _ { t } \in M ;$ ${ \cal L } _ { \cal O } = \{ l _ { \cal O } | \exists l \in { \cal L } , l _ { \cal O } . A C = l . A C - \langle l . A C [ a _ { t } ] \rangle , l _ { \cal O } . C C =$ $l . C C \circ \langle l . A C [ a _ { t } ] \rangle \}$ }. In addition:

$$
\forall c _ {i} \in C, d _ {0} (c _ {i}) = \left\{ \begin{array}{l l} d (c _ {i}) & \text {if c_{i} \neq c_{t}}, \\ 0 & \text {otherwise}. \end{array} \right.
$$

• Mathematical Notation: $\begin{array} { r } { { \pmb { { \mathscr { V } } } } _ { a t , c t } ( C _ { I } ) = C _ { O } . } \end{array}$

• A Simple Example: Convert store\_name from a dimension to a measure. This operation can be expressed as follows: $\boldsymbol { \varPsi } _ { s t o r e \_ n a m e , s a l e s } ( \mathbf { S } \mathbf { a l e s } ) = \mathbf { C } _ { \mathrm { R e s u l t } } .$

Extract (U ). The extract operator converts measures to dimensions. Let $a _ { t }$ be a metric attribute to transform such that $g ( a _ { t } ) \in M . \operatorname { L e t } c _ { t }$ be the corresponding characteristic name for $a _ { t }$ such that $c _ { t } \notin M$ and either $c _ { t } \in D \ \mathrm { o r } \ c _ { t }$ is a new characteristic name. The algebra of the extract operator is defined as follows:

• Input: A cube $\mathsf { C } _ { I } = \langle C , A , f , d , O , L \rangle$ , a metric attribute to transform $a _ { t } ,$ and a corresponding characteristic name $c _ { t } .$

• Output: A cube $\mathsf { C } _ { O } = \langle C _ { O } , A _ { O } , f _ { O } , d _ { O } , O _ { O } , L _ { O } \rangle$ where $C _ { O } = C \cup \{ c _ { t } \} ; f _ { O } = f - f ( g ( a _ { t } ) ) + [ g ( a _ { t } ) \to f ( g ( a _ { t } ) - a _ { t } ) ]$ $~ + ~ [ c _ { t }  a _ { t } ] ; O _ { O } = O _ { p r e v } \cup O _ { n e w }$ where $O _ { p r e v }$ is obtained by removing from O those ordered pairs containing $a _ { t } ,$ and $O _ { n e w }$ represents a user specified set of ordering relations between $a _ { t }$ and the elements of $f ( c _ { t } ) { \mathrm { ~ i f ~ } } c _ { t } \in D ;$ $L _ { O } = \{ l _ { O } | \exists l \in L , l _ { O } . A C = l . A C \circ \langle l . C C [ a _ { t } ] \rangle , l _ { O } . C C =$ $l . C C \mathrm { ~ - ~ } \langle l . C C [ a _ { t } ] \rangle \}$ . In addition:

$$
\forall c _ {i} \in C, d _ {O} (c _ {i}) = \left\{ \begin{array}{l l} d (c _ {i}) & \text { if } c _ {i} \neq c _ {t}, \\ 0 & \text { otherwise }. \end{array} \right.
$$

• Mathematical Notation: $\Phi _ { a t , c t } ( { \bf C } _ { I } ) = { \bf C } _ { O } .$

• A Simple Example: Convert store\_name from a measure to a dimensional attribute. This operation can be expressed as follows: $\phi _ { s t o r e \_ n a m e , l o c a t i o n } ( S { \bf a l e s } ) =$ $\mathbf { C _ { R e s u l t } } .$

In addition to the above defined operators, we also allow the standard arithmetic operators $( + , - , \times$ , and $\div )$ to be applied to either: (i) one or more metric attributes of a cube, or (ii) a metric attribute from one cube and a metric attribute from another cube. We illustrate these operations with the following examples:

• For the Sales cube, suppose the user wants to see the amount divided by the quantity. This query can be expressed as follows: Sales $\begin{array} { r } { { \bf \nabla } _ { \cdot a m o u n t } \div \bf { S a l e s } . _ { q u a n t i t y } = } \end{array}$ $\mathbf { C _ { R e s u l t } } .$

• (ii) Consider two cubes, Sales $\mathbf { 1 9 9 5 }$ and Sales<sub>1996</sub>, which each contain the total sales amounts for each product for 1995 and 1996, respectively. Both cubes have the same structure: $D = \{ p r o d u c t \} , \ : M =$ {sales}, f(product)  {product\_name}, and f(sales)  {amount}. Suppose the user would like to see the ratio of the sales amounts for the two years. This query can be expressed as follows: $\mathbf { S a l e s _ { 1 9 9 5 \cdot a m o u n t } } \quad \div$ $\mathbf { S } a \mathbf { l e s } _ { 1 9 9 6 \cdot a m o u n t } = \mathbf { C } _ { \mathrm { R e s u l t } } .$

## 8. Examples of Queries in the Model

In this section, we provide a feel for the power of our algebra by providing examples of OLAP queries that are extremely difficult, if not impossible, to express using the relational algebra or SQL. The examples apply to the Sales cube. For comparison purposes, we also provide the corresponding SQL expressions, assuming a non-normalized version of the schema shown in Figure 2.

Query 1: For each product, find the maximum quantity sold and the name of the store where the sale was made. This query was presented in the previous section, and provides a good illustration of the use of transformation operations. The query is conceptually simple, yet is quite complicated when expressed using SQL, as we will soon show. The reason for this is that, due to the nature of the way that aggregations are performed, two passes are required through the joined relations: one to actually find the maximum value, and the other to get the associated store name. The query can be expressed in our algebra as follows:

$$
\begin{array}{c} \Phi_ {s t o r e \_ n a m e, l o c a t i o n} (\varGamma_ {[ M A X, \{p r o d u c t \_ n a m e \}, q u a n t i t y ]} \\ (\Psi_ {s t o r e \_ n a m e, s a l e s} (\mathbf {S a l e s}))) = \mathbf {C} _ {\text { Result }}. \end{array}
$$

We explain the expression working from the innermost to the outermost sub-expression (i.e., right to left). The first step transforms store\_name to a measure so that it is retained for the answer set. The next step is the aggregation, which finds the maximum Quantity for each Product\_name. Finally, store\_name is transformed or extracted back into the location dimension. The resulting cube, ${ \bf C } _ { \bf R e s u l t } ,$ has the following structure: C  {location,product,sales}, D  {location,product}, M  {sales}, f(location)  {store\_name}, f(product)  {product\_name}, f(sales)  {quantity}.

In SQL, this query can be expressed as follows:

```sql
CREATE VIEW MaxView AS
SELECT P.Product_name, MaxQ = MAX(S.Quantity)
FROM SALES S, PRODUCT P, CUSTOMER C, TIME T,
LOCATION L
WHERE S.TimeID = T.TimeID AND S.LocID = L.LocID
AND S.CustID = C.CustID AND S.ProdID = P.ProdID
GROUP BY P.Product_name
SELECT L.Store_name, P.Product_name, MV.MaxQ
FROM MaxView MV, SALES S, PRODUCT P, LOCATION L
WHERE MV.Product_name = P.Product_name AND
S.LocID = L.LocID
AND S.ProdID = P.ProdID
```

In the above formulation, the first query creates a view containing the maximum Quantity for each product, and the second query joins this view with the appropriate tables to get the corresponding store\_name.

Query 2: Find those products having total sales during the summer (June, July, August) greater than one-third of their sales for the entire year for 1996. This query provides an example of a comparison of aggregates as described in § 5. This particular example is a variation of the ratio to total type of query. This query requires aggregating sales for the entire year and for the summer as shown below:

$$
\begin{array}{l} \Gamma_ {[ S U M, \{\text {product\_name} \}, a m o u n t ]} (\Sigma_ {\text {year} = 1 9 9 6} (\mathbf {S a l e s})) = \mathbf {C} _ {\text {Annual}}, \\ \Gamma_ {[ S U M, \{\text {product\_name} \}, a m o u n t ]} \\ (\Sigma_ {\text {year} = 1 9 9 6 \wedge (\text {month} = \text {June} \vee \text {month} = \text {July} \vee \text {month} = \text {August})} (\mathbf {S a l e s})) \\ = \mathbf {C} _ {\text {Summer}}. \end{array}
$$

We can then join the resulting two cubes and restrict the result to those values satisfying the predicate below, which requires that summer sales totals be greater than one-third of the annual sales totals:

$$
\begin{array}{l} \Sigma_ {(C S u m m e r. a m o u n t > 1 / 3 C A n n u a l. a m o u n t)} (\mathbf {C} _ {\text { Annual }} \Theta \mathbf {C} _ {\text { Summer }}) \\ = \mathbf {C} _ {\text { Result }}. \end{array}
$$

In SQL, this query can be expressed as follows:

```sql
CREATE VIEW AnnualSales AS
SELECT P.Product_name, SumA = SUM(S.Amount)
FROM SALES S, PRODUCT P, CUSTOMER C, TIME T, LOCATION L
WHERE S.TimeID = T.TimeID AND S.LocID = L.LocID
AND S.CustID = C.CustID AND S.ProdID = P.ProdID
AND T.Year = 1996
GROUP BY P.Product_name
CREATE VIEW SummerSales AS
SELECT P.Product_name, SumS = SUM(S.Amount)
FROM SALES S, PRODUCT P, CUSTOMER C, TIME T, LOCATION L
WHERE S.TimeID = T.TimeID AND S.LocID = L.LocID
AND S.CustID = C.CustID AND S.ProdID = P.ProdID
AND T.Year = 1996 AND T.Month IN
{June, July, August}
GROUP BY P.Product_name
SELECT AS.Product_name
FROM AnnualSales AS, SummerSales SS
WHERE SS.Product_name = AS.Product_name
AND SS.SumS > 1/3 * AS.SumA
```

In the above formulation, the first two queries create views for annual sales and summer sales, respectively. The last query joins the two views to determine which tuples satisfy the restriction condition.

Query 3: Find the top five products for each city in 1996 based on total sales. This query provides another example of aggregation, this time using ranking as discussed in § 5. To express this query, we illustrate the RANK function defined in the previous section. The first step in answering this query is to perform a restriction to select only those values corresponding to the year “1996.” Note that the restriction operation realizes dicing of the cube. An aggregation is then performed to sum the amount metric using the grouping attributes city and product\_name. Another aggregation is then performed on this result to rank the cube cells by total sales (which we still refer to as the amount metric even though it represents an aggregate value). Recall that the RANK function adds an attribute to the cube containing the ordinal number of the cube cell. These operations are provided below in a nested expression:

$$
\begin{array}{c} \Sigma_ {[ R A N K, \{\}, a m o u n t ]} (\Gamma_ {[ S U M, \{c i t y p r o d u c t \_ n a m e \}, a m o u n t ]} \\ (\Sigma_ {y e a r = 1 9 9 6} (\mathbf {S a l e s}))) = \mathbf {C} _ {\text {Ranked}}. \end{array}
$$

The resulting cube, $\mathbf { C } _ { \mathrm { R a n k e d } } ,$ has the following cube structure: C  {location, product, sales, rank}, $D ~ = ~ \{ l o \cdot$ cation, product}, $M = \{ s a l e s , r a n k \} , f ( l o c a t i o n ) = \{ c i t y ,$ , state}, f(product)  {product\_name}, f(sales)  {amount}, and f(rank)  {rank}. To produce the final answer to the query, a restriction is performed on $\mathbf { C } _ { \mathrm { R a n k e d } }$ so that only those values having a rank value in the top five are included. Note the symmetric treatment of dimensions and measures here: the rank measure appears in the restriction predicate.

$$
\Sigma_ {(r a n k \geq 1 \land r a n k \leq 5)} (\mathbf {C} _ {\text { Ranked }}) = \mathbf {C} _ {\text { Result }}.
$$

For this query, we are not able to provide an equivalent SQL expression since it is not possible to perform ranking in SQL.

Query 4: Find products having total sales that have increased in each of the last five years. This query provides an example of an aggregation involving a user-defined function. Let INC represent a function that sets a boolean variable inc to one if the total sales values for a particular record are increasing in each of the five years. Then this query can be expressed as:

$$
\begin{array}{l} \Sigma_ {i n c = T R U E} (\Gamma_ {[ I N C, \{\}, i n c ]} (\Gamma_ {[ S U M, \{p r o d u c t \_ n a m e \}, a m o u n t ]} \\ (\Sigma_ {\text { year } \geq 1 9 9 5} (\mathbf {S a l e s})))) = \mathbf {C} _ {\text { Ranked }}. \end{array}
$$

This query first restricts the cube to the last five years. Next an aggregation is performed to find the total sales by product\_name. Then another aggregation is performed that determines which records have increasing sales values. Finally, the records are restricted to those having increasing sales values. This query provides another example of a query that is not expressible in SQL.

## 9. Properties of the Model

In this section we discuss the properties of our model in an attempt to show the “goodness” of our proposal.

We start off by demonstrating the advantages of our model over other proposed models.

## 9.1. Comparison to Other Work

The model we present has several advantages over the models presented in previous work. First of all, our model incorporates dimensional hierarchies and allows these hierarchies to be modified through ordering relations. In Agrawal et al. (1997), functions are used for this purpose, which results in complicated operator definitions. In Gyssens and Lakshmanan (1997), hierarchies are not explicitly mentioned. Incorporating hierarchies in their model is accomplished by defining summarization functions. For instance, a summarization function can be defined to perform a roll-up, where the appropriate hierarchies must be established.

Secondly, our model and algebra are based on the widely accepted data cube construct presented in $\ S 3 ,$ resulting in a model that is intuitive and familiar. In Gyssens and Lakshmanan (1997), the underlying data structure is an n-dimensional table, where an instance is a set of relations, one for each dimension and one for the dimension keys along with their corresponding measures. While relations may be familiar to work with, they are more difficult to conceptualize with multidimensional data. In addition, the authors claim that using relations removes the structure of the cube, thereby resulting in a separation of structure and content. They argue that this separation allows the algebra to be defined in a simple, transparent manner. While this may be the case for the basic algebraic operations they define (e.g., selection, projection, union, difference, Cartesian Product), it is not the case for other important OLAP operations $\scriptstyle ( \mathrm { e . g . } ,$ transformation, summarization), as we will soon show. In short, the authors have not shown any real benefit to separating structure and content. In fact, this separation may add some unnecessary complexity to their model by incorporating implementation issues. Our algebra, on the other hand, operates on one or more cubes and produces as output a new cube. The structure present in our model does not in any way limit the capabilities of the model, but rather strengthens the conceptual foundations of the model.

Finally, our model provides simple algebraic operator definitions, where each operator performs a unique function. In Agrawal et al. (1997), one of the primary goals is to keep the number of operators small. However, as mentioned, the operators are quite complex. In Gyssens and Lakshmanan (1997), the authors claim to have defined a concise algebra. However, this claim is questionable when one considers expressing the cube operator using their algebra. We refer the reader to Gyssens and Lakshmanan (1997) for a detailed discussion of how this operator can be expressed using their algebra. We now present the cube operator expressed in our algebra, which is a much more clear and concise set of algebraic expressions.

The CUBE operator is proposed as an extension to the SQL GROUP BY clause (Gray et al. 1997). It aggregates over all possible combinations of the attributes in the GROUP BY clause and then unions in each superaggregate, substituting all for the aggregation columns. In our algebra, this operator can be expressed as a combination of aggregation and union operations. In general, we must derive an aggregate cube for: (i) each of the grouping attributes, (ii) each combination of the grouping attributes, and (iii) the overall aggregate. Each of these aggregate cubes is unioned with the original sales cube so that the resulting cube contains all possible aggregations along with the original data. Each aggregate cube is created by performing two aggregations, one summing the amount and the other inserting ALL into the cube cells, which we will demonstrate shortly using an example. These two cubes are then unioned together to form the aggregate cube.

Consider the following example, where it is desired to perform the CUBE operation using city and year as the grouping attributes and total sales amount as the aggregated metric. We first derive the aggregate cube for sales by city. This requires performing the following two aggregations:

$$
\begin{array}{c} \Sigma_ {[ S U I M, \{c i t y \}, a m o u n t ]} (\mathbf {S a l e s}) = \mathbf {C} _ {\text { City\_amount}}, \\ \Sigma_ {[ A l l, \{c i t y \} ]} (\mathbf {S a l e s}) = \mathbf {C} _ {\text { City\_all }}, \end{array}
$$

where we define all as a constant-valued function that inserts the literal ALL into each cube cell.

We then union the above two cubes to obtain the aggregate cube by city:

$$
\mathbf {C} _ {\text { City\_amount }} \cup \mathbf {C} _ {\text { City\_all }} = \mathbf {C} _ {\text { City }},
$$

Next we union the aggregate cube with the original Sales cube:

$$
\mathbf {C} _ {\text { City }} \cup \text { Sales } = \mathbf {C} _ {\text { Result }}.
$$

Note that the resulting cube is an intermediate result. Similar steps are required for amount by year, amount by city and year, and the overall aggregate. It should be emphasized that the operations required to express CUBE in our algebra are quite simplistic and intuitive, involving only a combination of aggregation and union operations.

Another common OLAP operation is the roll-up, which is closely related to the CUBE operation, but performs only a subset of the aggregation. For instance, using the above example, a roll-up would be to find the total sales amount for each city. This operation can be expressed concisely in our algebra as follows:

$$
\Sigma_ {[ S U M, \{c i t y \}, a m o u n t ]} (\mathbf {S a l e s}) = \mathbf {C} _ {\text { Result }}.
$$

To roll-up to a higher level, State, for instance, we must consider the partial orders defined on the hierarchy. Recall from the partial orders on the location dimension that store\_name rolls up to city and city rolls up to state. Thus this query requires two aggregations: (1) store\_name to city and (2) city to state. For the first aggregation, we must transform state to a measure so that it is retained for the second aggregation. For the second aggregation, we must transform state back into a dimension. This query can be expressed as follows:

$$
\begin{array}{l} \Gamma_ {[ S U M, \{s t a t e \}, a m o u n t ]} (\varPhi_ {s t a t e \_ l o c a t i o n} (\varGamma_ {[ S U M, \{c i t y \}, a m o u n t ]} \varPsi_ {s t a t e, s a l e s} \\ (\mathbf {S a l e s}))))) = \mathbf {C} _ {\text {Result}}. \end{array}
$$

This example also illustrates a slight efficiency advantage in our transformation operators over the fold and unfold operators defined in Gyssens and Lakshamanan (1997), which serve to convert dimensions to measures and measures to dimensions, respectively. The fold operator takes a dimension as its argument. Hence, there is no way to convert a single-dimensional attribute to a measure using this algebra. Instead one must fold the entire dimension and then subsequently unfold those dimensional attributes that are not desired as measures. Thus, each transformation operation may require an additional operation when expressed using the fold and unfold operators defined in Gyssens and Lakshamanan (1997).

## 9.2. Closure and Expressivity of Our Model

So far in this paper, we have described a new model for data cubes and an algebra of operations on this cube. Additionally, we have also attempted to illustrate, through argumentation and examples, why our model is useful. Finally, in this section we endeavor to discuss a few “formal” properties of our proposal. In particular, we will discuss two well-known properties in the context of our model and algebra, namely closure and expressivity. Closure (Aho et al. 1988) refers to how well a language can interpret the results of the application of its operations—a language is closed if the results of any allowable operation is a legal construct in the language. Expressivity is self-explanatory and is well known as notoriously difficult to analyze. An often adopted approach is to compare how expressive a new language is in comparison to a well-known expressive language. We will adopt this approach—in particular we will demonstrate that our algebra circumscribes the semantics of relational algebra, a wellknown language. This is achieved by the two theorems stated below.

Theorem 1. Our algebra is closed.

We now turn our attention to showing that the semantics of our algebra circumscribe those of the relational algebra. Since the underlying data models are different (i.e., the relational algebra operates on relations, whereas our algebra operates on cubes), we must first demonstrate that these two constructs are contentwise equivalent. This is shown through the notion of data equivalence defined below.

## 9.3. Data Equivalence

A relation instance is a set of n-tuples. Each tuple can easily be seen to correspond to the content of an individual cell in a cube. With this in mind, one can easily define an equivalence relationship, $\cong _ { \mathfrak { N } } ,$ between relation instances and zero dimensional cubes. Intuitively, the relationship $r \cong _ { \mathfrak { R } }$ C indicates that both the relation instance r and the cube C represent the same underlying base data set. We thus refer to this as data equivalence. More formally, we define $\cong _ { \mathfrak { N } }$ as follows:

Data Equivalence. An instance r of a relation R and a cube C are data equivalent, denoted $r \cong _ { \mathrm { { \scriptscriptstyle \mathscr { R } } } } c , i f f C$ $= \langle C , A , f , d , O , L \rangle$ such that

$C = \{ M \} .$ , where M is an arbitrary characteristic;

${ \bf \nabla } \cdot { \cal A } = { \cal R } , \mathrm { i . e . }$ ., the relation and the cube have the same set of attributes;

$\bullet f = \{ \{ M , A \} \} , \ : \mathrm { i . e . } , f$ maps all attributes to the arbitrary characteristic M;

• d  {{M, 0}}, i.e., characteristic M is a measure;

$O = O , { \mathrm { i . e . , } }$ no partial ordering is present; and

$\bullet L = \{ l | \exists t \in r , l . C C = t , l . A C = O \} ,$ , i.e., for every tuple t in $r ,$ there exists a single cell l in C which has the tuple as its content component and no address component.

Having formally defined the concept of data equivalence, we now turn to showing that our algebra is at least as expressive as relational algebra. In doing so, we effectively prove the “relational completeness” of our algebra, even though the underlying data models differ. To show this, we examine each of the five basic relational operators $( \sigma , \pi \times , \cup , - )$ in turn.

## 9.4. Expressivity

Theorem 2. Our algebra is at least as expressive as the relational algebra.

Proof. Every relational algebra operator can be expressed in our algebra. Below we show that all five basic operators can be expressed in our algebra. Consequently, the derived operators (join, division, etc.) can be expressed as well.

• Restriction. Given relation instance r and a cube C such that $r \cong _ { \mathfrak { R } } \mathrm { C } , \sigma _ { P } ( r ) \cong _ { \mathfrak { R } } \itSigma _ { P } ( C )$

This claim holds since $\sigma _ { P } ( r )$ returns relation instance $r ^ { \prime }$ containing tuples of r that satisfy P and $\Sigma _ { P } ( \mathrm { C } )$ returns cube C containing cells of C that satisfy P.

A similar argument holds for the following three operators.

• Metric Projection. Given relation instance r and a cube C such that $r \cong _ { \mathfrak { R } } \mathrm { C } , \pi _ { S } ( r ) \cong _ { \mathfrak { R } } \varPi _ { S } ^ { \mathrm { M } }$ (C).

• Union. Given relation instances r and r and cubes $\mathrm { C _ { 1 } }$ and ${ \mathrm { C } } _ { 2 }$ such that $r _ { 1 } \cong _ { \mathfrak { A } } \mathrm { C } _ { 1 }$ and $r _ { 2 } \cong _ { \Re } \mathrm { C } _ { 2 } , r _ { 1 } \cup r _ { 2 } \cong _ { \Re }$ $\mathrm { C } _ { 1 } \cup \mathrm { C } _ { 2 } .$

• Difference. Given relation instances $r _ { 1 }$ and $r _ { 2 }$ and cubes $\mathrm { C _ { 1 } }$ and ${ \mathrm { C } } _ { 2 }$ such that $r _ { 1 } \cong _ { \mathfrak { A } } \mathrm { C } _ { 1 }$ and $r _ { 2 } \cong _ { \mathfrak { R } } \mathrm { C } _ { 2 } , r _ { 1 } \mathrm { ~ - ~ }$ $r _ { 2 } \cong _ { \mathfrak { N } } \mathrm { C } _ { 1 } \theta \mathrm { C } _ { 2 } .$

• Cubic Product. Given relation instances $r _ { 1 }$ and $r _ { 2 }$ and cubes $\mathrm { C _ { 1 } }$ and ${ \mathrm { C } } _ { 2 }$ such that $r _ { 1 } \cong _ { \mathfrak { N } } { \mathrm { C } } _ { 1 }$ and $r _ { 2 } \cong _ { \mathfrak { N } } \mathrm { C } _ { 2 } , r _ { 1 }$ $\times \ r _ { 2 } \cong _ { \mathfrak { N } } \mathsf { C } _ { 1 } \otimes \mathsf { C } _ { 2 } .$

This claim holds since $\left( \mathrm { i } \right) r _ { 1 } \times r _ { 2 }$ returns a relation r having n - m attributes where n represents the number of attributes in $R _ { 1 }$ and m the number of attributes in $R _ { 2 } ,$ and $r$ contains a tuple for each combination of tuples from $r _ { 1 }$ and $r _ { 2 } ,$ and (ii) $\mathrm { C } _ { 1 } \otimes \mathrm { C } _ { 2 }$ returns a cube C having all characteristics and attributes of both $\mathrm { C _ { 1 } }$ and ${ \mathrm { C } } _ { 2 }$ and cells representing all possible combinations of the cells of both cubes.

Because we have shown that every relational operator can be expressed in our algebra, it follows that any relational algebra expression can be expressed using our algebra. Therefore, our algebra is at least as expressive as the relational algebra; intuitively, our algebra is relationally complete.

We conclude this section by noting that both our data model and algebra contain semantics that are clearly absent from the relational approach. For instance, our model allows dimensional hierarchies to be expressed in the cube itself and the algebra allows for very advanced aggregate computations to be performed (e.g., rank). Hence, it is possible that our proposed model and algebra are in fact more expressive than the relational model and algebra.

## 10. Conclusion

In this paper we have made an attempt to specify a rigorous conceptual model for decision support databases. This was motivated by the failure of existing OLAP products in providing a “good” framework for performing decision support queries. The main reason for this is the rather “helter-skelter” development of OLAP technology. Essentially, both practitioners and researchers have targeted problems piece-meal, i.e., once a specific problem is identified there has been a rush to provide a solution to this problem by modifying existing database technology. However unlike the relational model, there does not exist a precise, commonly agreed upon conceptual model for OLAP. Though the notion of the data cube has been widely accepted as the underlying logical construct of data warehouses $( \mathrm { i . e . , }$ , multidimensional databases), there does not exist a precise model for a data cube, and therefore it has not been possible to define accurately a model of operations on a data cube.

In response to this need we have postulated a model and algebra for data warehousing and OLAP. Our work is one of the first to provide an integrative list of the required functionalities of an OLAP data and operations model. We have proposed the cube data model, which is based on the intuitive and widely accepted data cube construct. We have also proposed an algebra for the cube model, which is capable of expressing the required OLAP functionalities in a concise manner. We have shown several examples of complex OLAP queries expressed elegantly in our algebra. It would be extremely difficult, if not entirely impossible, to formulate such queries using relational languages. We also discuss how our model and algebra satisfies certain “goodness” properties. In particular, we prove that our algebra is closed and at least as expressive as relational algebra. Finally, we also show that our proposed model has several advantages over the models presented in previous work, such as simplistic operator definitions and an intuitive underlying data structure.

## References

Agrawal, R., A. Gupta, S. Sarawagi. 1997. Modeling multidimensional databases. Proc. 13th ICDE Conf., IEEE, Birmingham, U.K.

Agarwal, S., R. Agrawal, P. Deshpande, A. Gupta, J. Naughton, R. Ramakrishnan, S. Sarawagi. 1996. On the computation of multidimensional aggregates. VLDB 506–521.

Aho, A., R. Sethi, J. Ullman. 1988. Compilers Principles, Techniques, and Tools. Addison-Wesley Publishing Company, Reading, Massachusetts.

Business Intelligence Ltd. 1998. The OLAP Report: Market Share Analysis. Business Intelligence Ltd., London, U.K.

Butler Group. 1996. Business Case for Data Warehousing: Strategies and Technologies. Butler Group, London, U.K.

Byard, J., D. Schneider. 1996. The ins and outs (and everything in between) of data warehousing. Proc. ACM SIGMOD. Montreal, Quebec, Canada.

Chatziantoniou, D., K. Ross. 1996. Querying multiple features of groups in relational databases. Proc. 22nd VLDB Conf., Mumbai, India.

Chauduri, S., U. Dayal. 1997. An overview of data warehousing and OLAP technology. SIGMOD Rec., 26(1) 65–74.

Codd, E. 1970. A relational model for large shared data banks. Comm. ACM 13(6) 377–387.

——. 1971. A data base sublanguage founded on the relational calculus. Proc. ACM SIGFIDET Workshop on Data Description, Access, and Control. San Diego, CA.

——. 1972. Relational Completeness of Data Base Sublanguages. Data Base Systems, Prentice Hall, Englewood Cliffs, NJ.

——, S. B. Codd, and C. T. Salley. 1993. Providing OLAP (On-Line

Analytical Processing) to User-Analysts: An IT Mandate. E. F. Codd & Associates http://www.arborsoft.com/papers/codd TOC.html-.

DBTG. 1971. Report of the CODASYL Data Base Task Group.

Elmasri, R., S. Navathe. 2000. Fundamentals of Database Systems. 3rd ed. Addison-Wesley Publishing Company.

Forrester Research Inc. 1997. Software Strategies. Forrester Research Inc.

Gray, J., S. Chaudhuri, A. Bosworth, A. Layman, D. Reichart, M. Venkatrao, F. Pellow, H. Pirahesh. 1997. Data cube: A relational aggregation operator generalizing group-by, cross-tab, and sub totals. Data Mining and Knowledge Discovery 1(1) 29–53.

Gupta, A., V. Harinarayan, D. Quass. 1995. Aggregate-query processing in data warehousing environments. Proc. 21st VLDB Conf., Zurich, Switzerland.

Gyssens, M., L. V. S. Lakshmanan. 1997. A foundation for multidimensional databases. Proc. 23rd VLDB Conf., Athens, Greece.

Harinarayan, V., A. Rajaraman, J. D. Ullman. 1996. Implementing Data Cubes Efficiently. Proc. ACM SIGMOD Conf., Montreal, Canada.

Inmon, W. H. 1996. Building the Data Warehouse, 2nd ed. J. Wiley & Sons, Inc., New York.

International Standards Organization. 1992. IS 9075 International Standard for Database Language SQL, Document ISO/IEC 9075, New York.

Kimball, R. 1996. The Data Warehouse Toolkit. J. Wiley & Sons, Inc. ——, A. Strehlo. 1995. Why decision support fails and how to fix it. SIGMOD Rec. 24(3). 92–97.

Lacroix, M., A. Pirotte. 1977. Domain-oriented relational languages. Proc. 3rd VLDB Conf., Tokyo, Japan.

Li, C., X. S. Wang. 1996. A data model for supporting on-line analytical processing. Proc. Conf. Inform. Knowledge Management Baltimore, MD.

O’Neil, P., D. Quass. 1997. Improved query performance with vari ant indexes. Proc. ACM SIGMOD Conf., Tucson, AZ.

Red Brick Systems. 1994. RISQL Reference Guide, Red Brick Warehouse VPT Version 3. Los Gatos, CA.

Shoshani, A. 1997. OLAP and statistical databases: Similarities and differences. ACM TODS. 22 185–196.

Zloof, M. 1975. Query by example. Proc. of the National Comput. Conf. Anaheim, CA.

Steven O. Kimbrough, Associate Editor. This paper was received on February 6, 1998, and was with the authors $6 \frac 1 2$ months for 1 revision.
