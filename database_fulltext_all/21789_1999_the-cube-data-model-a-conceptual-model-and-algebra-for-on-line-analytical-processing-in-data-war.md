---
otero_id: 21789
otero_key: "8X76HN93"
title: "The cube data model: a conceptual model and algebra for on-line analytical processing in data warehouses"
authors: "Anindya Datta; Helen Thomas"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00052-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The cube data model: a conceptual model and algebra for on-line analytical processing in data warehouses

Anindya Datta <sup>)</sup>, Helen Thomas 2

MIS Department, UniÕersity of Arizona, Tucson, AZ 85721, USA

## Abstract

Data warehousing and On-Line Analytical Processing OLAP are two of the most significant new technologies in theŽ . business data processing arena. A data warehouse can be defined as a ‘‘very large’’ repository of historical data pertaining to an organization. OLAP refers to the technique of performing complex analysis over the information stored in a data warehouse. The complexity of queries required to support OLAP applications makes it difficult to implement using standard relational database technology. Moreover, there is currently no standard conceptual model for OLAP. There is clearly a need for such a model and an algebra as evidenced by the numerous SQL extensions offered by many vendors of OLAP products. In this paper, we address this issue by proposing a model of a data cube and an algebra to support OLAP operations on this cube. The model we present is simple and intuitive, and the algebra provides a means to concisely express complex OLAP queries. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Data warehouse; On-line analytical processing OLAP ; Relational OLAP ROLAP ; Conceptual data models; Algebra;Ž . Ž . Multidimensional databases; Decision support databases; Data cube model

## 1. Introduction

The dual but related notions of data warehousing and On-Line Analytical Processing OLAP are,Ž .

clearly, two of the most significant new technologies in the business data processing arena. They are used in a multitude of industries such as retail sales Ž . supermarkets, department stores, etc. , telecommunications, financial services organizations and realestate firms 5 . Perhaps the most telling testimonial<sup>w</sup> <sup>x</sup> of the widespread acceptance of these technologies is the fact that the sales of data warehousing and OLAP products totalled US\$9 billion in 1997, up 350% since 1995 3,4 . Loosely speaking, a data warehouse <sup>w</sup> <sup>x</sup> is a ‘‘ very large’’ repository of historical data pertaining to an organization see Refs. 17,18 for Ž <sup>w</sup> <sup>x</sup> excellent treatment of data warehousing . The notion. of OLAP, introduced by Codd in his seminal paper in 1993 9 , refers to the technique of performing <sup>w</sup> <sup>x</sup> complex analysis over the information stored in a data warehouse. In general, OLAP applications are characterized by the rendering of enterprise data into multidimensional perspectives. This is achieved through complex, ad hoc queries that frequently aggregate and consolidate data, often using statistical formulae 9 . For example, a retail organization is<sup>w</sup> <sup>x</sup> often interested in comparing the total sales for thi year with the total sales for last year, or identifying sequences of 5 years or more when sales have increased or decreased within a 50-year envelope.Ž . It has been conjectured that relational database tech nology is well suited to fulfilling the needs of OLAP. However, the major use of relational technology so far has been in transaction management and ad-hoc querying for traditional On-line Transaction Processing OLTP systems. Conversely, OLAP calls for Ž . sophisticated on-line analytical support, for which the relational model is ill equipped 13 . Readers can easily gauge the limitation of the relational model by trying to answer the queries mentioned above in a relational language such as SQL. As a result, several vendors have developed specialized OLAP products such as Arbor Software’s Essbase, Oracle’s Expres and Sybase’s IQ. Most of these products however suffer from the following drawbacks 2,13 : a they<sup>w</sup> <sup>x</sup> Ž . suggest SQL extensions piece meal, rather than a comprehensive query language, b the user interac-Ž . tion is often limited to one operation at a time, which is inconsistent with the objectives of OLAP, cŽ . multidimensional rendering of data involves identify ing certain attributes as dimensional parameters and other attributes as metrics or measures Žthis is explained in detail later in the paper . Most OLAP. products in the market exclusively view metrics as functions of dimensions; that is, dimension and metric sets are static. However,this prevents users from making queries based on metric restrictions. It has been shown that this is inadequate as often users like to query dimensions by restricting metric values 20 .<sup>w</sup> <sup>x</sup> Thus, there is clearly a need for symmetric treatment of dimensions and measures.

One reason for the failure of existing OLAP products to provide a ‘‘good’’ framework is the fact that, unlike the relational model, there does not exist a precise, commonly agreed upon conceptual model for OLAP. Though the notion of the data cube Ž . explained below has been widely accepted as the underlying logical construct of data warehouses i.e.,Ž multidimensional databases , there does not exist a. precise model for a data cube and, therefore, it has not been possible to define accurately a model of operations on a data cube.

In response to this need, there is significant current interest in work that attempts to explore operations on multidimensional databases. An influential paper in this field appeared in 1995, written by Gray et al. 12 . In this paper the authors define the ‘‘data<sup>w</sup> <sup>x</sup> cube’’ operator by extending SQL to include new types of grouping and aggregating functionalities. Since the appearance of this paper, much work has been devoted to designing efficient data cube algorithms 1,16 . However, this work, while interesting,<sup>w</sup> <sup>x</sup> still makes very little headway in orchestrating a ‘‘big picture’’ for OLAP. The work remains at a level of suggesting piecemeal extensions to SQL, which, while perhaps providing a specific OLAP functionality, cannot lay an integrated framework upon which generic OLAP functionalities can be constructed. This is somewhat analogous to the situation in the mid-1970s, when data processing experts would suggest special purpose algorithms to perform operations such as selections, projections and join. However, because of the lack of a common data and operations model which would later come in theŽ form of the relational model, relational algebra and calculus such solutions failed to provide general. frameworks and eventually led to the development of relational database technology. Similarly, unless a common data and operations model of multidimensional databases i.e., data warehouses is advocated,Ž . a general purpose OLAP framework will be hard to realize. In this paper, we propose a simple but generic model of a data cube and attempt to design a simple algebra to support OLAP operations on this cube. To the best of our knowledge, this is the first comprehensive model proposed for data warehousing and OLAP.

The remainder of the paper is organized as follows. In Section 2, we discuss related work and provide a brief overview of OLAP and data warehousing and in Section 3, we present the contributions of this work. In Section 4, we present the proposed data model and operators, in Section 5 we demonstrate the capabilities of the operators, and in Section 6 we conclude the paper.

## 2. Related work

We now provide a compendium of related work, including the early work in data and operations modeling and more recent work in OLAP and data warehousing.

## 2.1. Data and operations models

Early work in data modeling began with the hierarchical, network, and relational models. Although there is no early documentation for the hierarchical model, it is known that this model evolved from the Information Management System IMSŽ . DBMS, which was developed in the late 1960s 11 .<sup>w</sup> <sup>x</sup> The network model was developed in the early 1970s and is the underlying model for the Integrated Database Management System IDMS DBMS 10 . Ž . <sup>w</sup> <sup>x</sup> The relational model was also developed in the early 1970s 6 . This model has gained widespread accep- <sup>w</sup> <sup>x</sup> tance and is the underlying data model for many commercial DBMSs. In addition, operations models have been developed for the relational data model. These models include the relational algebra 6 , which<sup>w</sup> <sup>x</sup> is a procedural language, and the tuple relational calculus 7,8 and the domain relational calculus<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 23,20 , which are declarative languages.

There is very little work in creating data and operations models for multidimensional databases. We are aware of three papers in the published literature which tackle this issue. All of these are quite recent, the earliest one appearing in 1996 21 and<sup>w</sup> <sup>x</sup> the two most recent ones in 1997 2,15 . All of these<sup>w</sup> <sup>x</sup> papers deal with multi-dimensional databases, designed around the basic underlying construct of a data cube, containing dimensions, attributes and measures. These papers are important as they chart the initial footsteps in an important research topic, namely modeling data warehouses. However, unrealistic restrictions are placed in these models, e.g., restrictions are imposed on either the number of attributes per dimension or the number of total measures representable in the cube. Moreover, dimensions and measures are treated asymmetrically, leading to the inability of these models to answer particular types of queries without requiring expensive redesign. In this paper, we propose a simple and intuitive model of a data cube, and attempt to design a clear and concise algebra to support OLAP operations on this cube. As already mentioned, this paper is one of the first to deal with these issues.

We now discuss more recent work by providing an overview of OLAP and data warehousing.

## 2.2. OÕerÕiew of OLAP and data warehousing

A data warehouse can be defined as a repository of historical data used to support decision-making <sup>w</sup> <sup>x</sup> 17 . OLAP refers to the technology that allows the user to efficiently retrieve data from the data warehouse. The characteristics of OLAP applications are quite different than those of operational or OLTP systems. OLTP systems are designed to perform repetitive, structured tasks where detailed records are updated e.g., order entry, account updates following Ž a bank transaction . The emphasis in these systems is. on maximizing transaction throughput and maintaining consistency. Typically, OLTP systems are on the order of hundreds of megabytes to gigabytes in size.

In contrast to OLTP systems, data warehouses are designed for decision support purposes and contain long periods of historical data. For this reason, data warehouses tend to be much larger than OLTP systems, often by orders of magnitude. It is quite possible for a data warehouse to be hundreds of gigabytes to terabytes in size 5 . In this environment, aggre-<sup>w</sup> <sup>x</sup> gated and summarized data are much more important than detailed records. The emphasis in data warehousing is on query processing and response times rather than transaction processing. Queries tend to be complex and ad hoc, often requiring computationally expensive operations such as joins and aggregation. Further complicating this situation is the fact that such queries must be performed on tables having potentially millions of records. Moreover, the results have to be delivered interactively to the business analyst using the system.

The differing requirements of OLTP and OLAP systems dictate different data models and implementation methods for each type of system. The entity– relationship ER model is commonly used to repre- Ž . sent an OLTP application at the conceptual level. However, this model is not capable of sufficiently representing multidimensional data 19 . For this rea- <sup>w</sup> <sup>x</sup> son, an alternative conceptual model is required for OLAP systems. The multidimensional data model or data cube is a popular model used to conceptualize the data in a data warehouse 5 . The data cube<sup>w</sup> <sup>x</sup> contains points or ‘‘cells’’ that are measures or values based on a set of dimensions. For example, consider a retail sales application where the dimensions of interest may include CUSTOMER, PROD-UCT, LOCATION, and TIME. If the measure of interest in this application is sales amount, then a point represents the sales measure corresponding to the CUSTOMER, PRODUCT, LOCATION, and TIME dimensions. In Fig. 1, a data cube is provided which shows the PRODUCT, LOCATION, and TIME dimensions. A cell corresponds to the sales value for the corresponding PRODUCT, LOCA-TION, and TIME. For example, the shaded cell corresponds to sales for PRODUCT ‘P1’ in ‘Seattle for 1994.

Dimensions often form a hierarchy. For instance, the TIME dimension may form a day–month– year hierarchy and the LOCATION dimension may form a city–state–region hierarchy. Dimensions allow different levels of granularity in the warehouse. For example, region corresponds to a high level of granularity whereas city corresponds to a low level of granularity.

Given the data cube representation of a multidimensional database, several decision support operations have been proposed as part of OLAP. These constructs include slice, dice, drill-down, roll-up. and piÕot. Slice and dice are roughly analogous toŽ . the relational algebra operators selection and projection. Slicing refers to selecting the dimensions used to view the cube. In Fig. 1, the dimensional view provided is PRODUCT by LOCATION with TIME in the background. This view can easily be changed using the slice operation. Dice refers to selecting actual positions or values on a dimension. Selecting ‘‘Dallas’’ as the LOCATION is an example of dicing. Slice and dice together have the effect of reducing the dimensionality of the cube. Drill-down refers to decreasing the level of aggregation along one or more dimensional hierarchies, whereas roll-up refers to increasing the level of aggregation. For example, in a drill-down, the user may first examine sales at the regional level. If more detail is required, the user may then examine sales at the more detailed state level.

![](/api/attachments/8X76HN93/fulltext/images/9943bc1c7b5a2dd0363f142de7094678ba6f0d229ca029f393c62ab7df3aa6e3.jpg)  
Fig. 1. Data cube for sales application.

Pivot refers to aggregating over one or more dimensions and producing a new cube having an attribute for each dimension and an additional attribute for the aggregated measure 5 . Consider a<sup>w</sup> <sup>x</sup> simple two-dimensional example where the selected dimensions are PRODUCT and TIME and the desired aggregate measure is total sales. The result of a pivot would be a new two-dimensional cube having product, time, and total sales as its attributes. The significance of pivot is that it allows the measures in a cube to become attributes in the resulting cube.

Having discussed data modeling in OLAP systems, we now briefly discuss implementation and design. There are two main implementation methods to support OLAP applications: multidimensional OLAP MOLAP servers and relational OLAPŽ . Ž . ROLAP servers. The MOLAP approach physically stores the data in array-like structures that are similar to the data cube presented in Fig. 1. In the ROLAP approach, the data is stored in a relational database using a special schema instead of the traditional relational schema. The highly normalized form of the relational model is inappropriate in an OLAP environment for performance reasons. A high degree of normalization requires more joins, which greatly affects response time, especially given the size of most data warehouses. For this reason, a special schema known as the star schema is often used. A star schema usually consists of a single fact table and a dimension table for each dimension. The fact table contains foreign keys to each dimension table, along with the actual measured data e.g., sales amount .Ž .

![](/api/attachments/8X76HN93/fulltext/images/6f4a0cd6afe391a34a67bac9c17f04cd2eced53877c864ea2951a3312e40ccbd.jpg)  
Fig. 2. Snowflake schema for sales application.

An extended version of the star schema, the snowflake schema, is often used to represent the dimensional hierarchies in normalized form. A possible snowflake schema is presented in Fig. 2 for the sales application. This figure displays the day– month–year and city–state–region hierarchies in their respective normal forms.

There are several research issues in data warehousing including data loading, view materialization, and access methods. Since the data in a data warehouse often originates from multiple production systems, a cleaning process is usually employed, which checks for and removes integrity problems. The timing and method of loading is also critical, since the volume of data tends to be high. To improve query response time, some data is often pre-aggregated in a data warehouse, an approach known as Õiew materialization. However, there is a tradeoff in response time and the storage required for pre-aggregated data. Determining how much data to pre-aggregate is an issue that has been addressed in Refs. 14,16 .<sup>w</sup> <sup>x</sup> Access methods in data warehouses are also being examined to improve query response times. Indexing strategies such as bitmapped indexes have been proposed in Ref. 22 . Having provided an overview of<sup>w</sup> <sup>x</sup> OLAP and data warehousing, we now discuss the contributions of our work.

## 3. Contributions of this paper

The contributions of the research presented in this paper are twofold.

Ž . 1 We stipulate a detailed data model for the data cube — the underlying logical level construct used to conceptualize multidimensional data. Again this is the first such comprehensive formal model proposed.

Ž . 2 We stipulate a detailed operations model for the data cube — a powerful yet simple algebra that operates on the data cube. Our proposed algebra allows complex OLAP queries to be expressed in a concise manner.

Having stated our contributions, we now turn our attention to our proposed model and algebra. We use the terms multidimensional database Ž . MDDB and data warehouse synonymously throughout this paper.

## 4. Proposed operators

In this section, we present a model of a multidimensional database<sup>r</sup>datawarehouse and an algebra for OLAP based on this model. We reiterate our goals: 1 to allow symmetric treatment of dimen-Ž . sions and measures and 2 to provide comprehen-Ž . sive OLAP functionality. This functionality includes aggregation e.g., roll-ups and comparisons of aggre-Ž gate values , transformations converting dimensions. Ž to measures and vice versa , partitioning grouping . Ž of data for aggregating purposes , and other analyti- . cal queries e.g., drill-downs, joins of fact and di-Ž mension tables ..

As mentioned previously, the data cube is almost universally accepted as the underlying logical level construct to describe a multidimensional database Ž . just as the ‘‘relation’’ is for a relational database . This mandates that all the operators we define asŽ well as their algebra must operate on the cube. structure just as the relational algebra operators Ž operate on the relation structure . The first step . therefore, is to define a data cube.

Definition 1 A data cube, to be referred toŽ simply as a cube from this point on is the funda-. mental underlying construct of the multidimensional database and serves as the basic unit of input and output for all operators defined on a multidimensional database. It is defined as a 4-tuple, $\langle D , M , A , f \rangle$ where the four components indicate the characteristics of the cube. These characteristics are:

1. A set of n dimensions $D = \{ d _ { 1 } , d _ { 2 } , \dots , d _ { n } \}$ where each $d _ { i }$ is a dimension name, extracted from a domain dom . <sub>dimŽi.</sub>

2. a set of k measures $M = \left\{ m _ { 1 } , m _ { 2 } , \dots , m _ { k } \right\}$ where each $m _ { i }$ is a measure name, extracted from a domain dom . <sub>measureŽi.</sub>

3. The set of dimension names and measure names are disjoint; i.e., D <sup>l</sup> M <sup>s</sup> 0.

4. A set of t attributes $A = \{ a _ { 1 } , a _ { 2 } , \ldots , a _ { t } \}$ where each $a _ { i }$ is an attribute name, extracted from a domain dom . <sub>attrŽ i.</sub>

5. A one-to-many mapping f: D A, i.e., there exists, corresponding to each dimension, a set of attributes. The mapping is such that attribute sets corresponding to dimensions are pairwise disjoint, $\mathrm { i . e . , } \forall i , j , i \neq j , f ( d _ { i } ) \cap f ( d _ { i } ) = 0 .$

We now provide an example to clarify this definition. Subsequently, this will be used as a running example for the rest of the paper. Consider a cube Sales which represents a multidimensional database of sales figures of certain products. The Sales cube has the following features note the correspondence Ž of the example to the definition above ..

<sup>Ø</sup> The users are interested in the sales and quantity metrics. Thus for the Sales cube M <sup>s</sup>  sales, quantity4

<sup>Ø</sup> The users are interested in analyzing sales figures along three dimensions, namely TIME, PRODUCT, and LOCATION. In other words users are interested in asking questions such as ‘‘what was the total sales of product $P _ { 1 }$ in a certain location’’ Ž . querying along the product and location dimension , or ‘‘what was the total sales of $P _ { 1 }$ in a certain location during a specific time interval’’ querying Ž along all three dimensions . Therefore for the. Sales cube, D<sup>s</sup> 4TIME, PRODUCT, LOCATION

<sup>Ø</sup> The TIME dimension is described by the attributes day, month and year. The PRODUCT dimension is described by product\_name, weight and color, whereas the LOCATION dimension is described by the store\_name, city, state and region attributes. Thus, for the Sales cube, A<sup>s</sup>day, month, year, product name, weight, color, store name, city, state, region4.

<sup>Ø</sup> Each of the dimensions, as explained in the previous item, are described by specific attributes. In other words, for the Sales cube, the mapping f works as follows:

$$
\begin{array}{l} f (\text {TIME}) = \{\text {day, month, year} \} \\ f (\text {PRODUCT}) = \{\text {product\_name, weight, color} \} \\ f (\text {LOCATION}) = \{\text {store\_name, city, state, region} \} \end{array}
$$

Also note that the three attribute sets shown above are mutually disjoint.

It is easily seen that the characteristics of the Sales cube satisfy the definition given above. Note that a cube, as defined above, is an abstract structure. In order to materialize a cube, one must ascribe values to the various measures along all dimensions. Such a materialized cube is known as a cube-instance. It is easily seen that a cube-instance is defined by a 6-tuple $\langle D , M , A , f , V , g \rangle$ where the elements D, M, A and f are inherited from its ‘‘parent’’ cube whereas V represents a set of values that have been used to materialize a cube. Note that every element $v _ { i } \in V$ is a k-tuple $\langle \mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { k } \rangle$ where each $\mu _ { i }$ is an instantiation of the ith measure $m _ { i }$ . Finally, g represents a mapping $g \colon \mathsf { d o m } _ { \mathsf { d i m } ( 1 ) } \times$ dom $\mathsf { \mathsf { 1 } } _ { \dim ( 2 ) } \times \ldots \times \mathsf { d o m } _ { \dim ( n ) } \to V .$ . Intuitively, the g mapping indicates which values are associated with which specific ‘‘cells’’ of the cube-instance. In other words, two cube-instances corresponding to the same cube will differ only in the 2-tuple $\langle V , g \rangle$

Henceforth, we will work with cube-instances in the development of theory in this paper. For ease of expression we shall simply refer to cube-instances as cubes without any loss of generality much asŽ entity-sets and entities are referred to simply as entities in the Entity–Relationship model ..

The Sales cube more correctly a cube-instanceŽ . is shown below pictorially in Fig. 3.

We now define an OLAP algebra, and use the cube shown above as a running example to illustrate the operators. As is the norm, our algebra consists of a set of operators. These are defined below.

Restriction Ž . . The restriction operator restricts the values on one or more dimensions. Let an atomic predicate, denoted by p, be a logical expression Ž . possibly including negated literals involving a single dimension. Let a compound predicate, denoted by P be an expression involving a set of atomic predicates $\{ p _ { 1 } , p _ { 2 } , . . . , p _ { 1 } \} , l \geq 1$ , of the form:

$$
P = p _ {1} \langle \mathrm{op} \rangle p _ {2} \langle \mathrm{op} \rangle \dots \langle \mathrm{op} \rangle p _ {l}
$$

where op represents a logical operator² : $\left( \mathrm { e . g . , \ } \wedge \right.$ Ž . Ž .. and , <sup>k</sup> or . Then, the algebra of the restriction operator is defined as follows.

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I } } = \langle D , M , A , f , V , g \rangle$ and a compound predicate P.

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } = D ; M _ { 0 } = M ; A _ { 0 } = A ; f _ { 0 } = f ; V _ { 0 } \subseteq V ;$ and $g _ { 0 } = g _ { 0 }$ where every element of $g _ { p } ^ { - 1 } ( V _ { P } )$ satisfies P.

<sup>Ø</sup> Mathematical notation: $\sigma _ { P } ( C _ { \mathrm { I } } ) = C _ { 0 }$

<sup>Ø</sup> A simple example: Assume the user would like to know the sales values for all products in all cities during 1994. Such a query can be answered by the following operation from the Sales cube shown above: $\sigma _ { ( { \mathrm { y e a r } } = 1 9 9 4 } ( \mathbf { S a l e s } )$ . More complex examples are shown in Section 5.

We now make a few remarks. First, note that the input to and output of the restriction operator are both instances of the same parent cube, i.e., the dimension, measure, attribute and mapping characteristics are identical. Secondly, the restriction operator realizes the important OLAP operation of dicing by restricting the values contained inside to a subset of their original values. Thirdly, if there are no values satisfying P, the result is an empty cube. Finally, we note that one feature of the restrict operator appears to be in violation of one of our earlier stated goals that we wanted to treat dimensions and measures similarly. The careful reader will note that the input predicate to the restrict operator is defined on the basis of dimensions only. However, if we were truly treating dimensions and measures identically, P should be defined on measures as well. This apparent anomaly is explained by the following statement: although restriction is defined to operate on dimensions, it can be applied to measures by first ‘transforming’ a measure into a dimension. This is a key feature of our model and we will discuss how this ‘transformation’ is done later in this section. Finally, in the examples shown in Section 5, it will be shown how the restriction operator is used uniformly towards both dimensions and measures.

![](/api/attachments/8X76HN93/fulltext/images/fc7656f8bc10dc33abb55ee5b49e015e5222bfc1b99941c8e652d65dd3f40a0e.jpg)  
Fig. 3. Data cube example with notation.

Aggregation Ž .  . The aggregation operator performs aggregation on one or more dimensions. This operator is roughly based on the relational aggre- Ž . gate functions e.g., Ž . SUM, AVG, MAX and allows these functions to be applied to cubes with one or more dimensions specified as grouping attributes. For example, referring to the Sales cube in Fig. 3, if the user would like to know the average sales amount for each year, then year would be the grouping attribute; hence, the aggregation occurs over the remaining dimension attributes Žcity, product\_name.. This operator is especially useful in roll-ups, where multiple aggregations usually occur. Let h be an aggregate function defined on a single measure $m _ { i }$ and let S be a set of grouping dimension attributes $\{ a _ { 1 } , a _ { 2 } , \ldots , a _ { \mathrm { q } } \}$ such that $S \subseteq A$ . For expository convenience, we define an additional oneto-one mapping $\delta \colon \ A \to D$ , where  represents a mapping of an attribute $a _ { i }$ to a dimension name $d _ { i } .$ Then, the algebra of the aggregation operator is defined as follows.

<sup>Ø</sup> Input: A Cube $C _ { \mathrm { I } } = \langle D , M , A , f , V , g \rangle$ , a measure to aggregate $m _ { i }$ , and a set of grouping dimension attributes S.

<sup>Ø</sup> Output: A Cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } = \{ d _ { 1 } , d _ { 2 } , \ldots , d _ { 9 } \} , \ q = | S |$ and $\forall a _ { i } \in S , \ d _ { i }$ $= \delta ( { a } _ { i } )$ . Furthermore, $\tilde { M _ { 0 } } = \{ m _ { i } \} ; A _ { 0 } = \cup _ { \forall d _ { i } \in D _ { 0 } }$ $f ( d _ { i } ) ;$ and $f _ { 0 } = f . \ V _ { 0 }$ represents the values obtained by applying the aggregate function h to the elements of V, and $g _ { 0 }$ represents a mapping $g _ { 0 } \colon \mathrm { d o m } _ { \mathrm { d i m } ( 1 ) } \times$ dom $_ { \cdot \mathrm { d i m } ( 2 ) } \times \ldots \times \mathrm { d o m } _ { \mathrm { d i m } ( q ) } \to V _ { 0 } .$

<sup>Ø</sup> Mathematical notation: $\alpha _ { h , m _ { i } , S } ~ ( C _ { \mathrm { I } } ) = C _ { 0 }$

<sup>Ø</sup> A simple example: Suppose the user would like to display annual sales for each product regardless of city. This query can be answered using the following operation on the Sales cube:

Ž . Sales <sub>wSUMŽamount.,product\_name , year4x</sub>

Cartesian Product Ž . <sup>=</sup> : The Cartesian Product operator is a binary operator that can be used to relate any two cubes. The algebra of the Cartesian Product operator is defined as follows:

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I 1 } } = \langle D _ { 1 } , M _ { 1 } , A _ { 1 } , f _ { 1 } , V _ { 1 } , g _ { 1 } \rangle$ and a cube $C _ { 1 2 } = D _ { 2 } , M _ { 2 } , A _ { 2 } , f _ { 2 } , V _ { 2 } , g _ { 2 } \rangle$

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } = D _ { 1 } \cup D _ { 2 } ; ~ M _ { 0 } = M _ { 1 } \cup M _ { 2 } ; ~ A _ { 0 } = A _ { 1 } \cup$ $A _ { 2 } ; \ V _ { 0 } = V _ { 1 } \times V _ { 2 }$ , and $\begin{array} { r } { | V _ { 0 } | = | V _ { 1 } | \times | V _ { 2 } | . } \end{array}$ . It can be easily shown that $f _ { 0 }$ can be derived from $f _ { 1 }$ and $f _ { 2 }$ Ž . discussion omitted due to space considerations . Again $g _ { 0 }$ represents a mapping $g _ { 0 } \colon { \mathrm { \ d o m } } _ { \mathrm { \ d i m ( 1 ) } } \times$ $\mathrm { d o m } _ { \mathrm { d i m } ( 2 ) } \times \ldots \times \mathrm { d o m } _ { \mathrm { d i m } ( q ) } \to V _ { 0 }$ where $q = | D _ { 0 } | .$

<sup>Ø</sup> Mathematical notation: $C _ { \mathrm { I 1 } } \times C _ { \mathrm { I 2 } } = C _ { 0 }$

<sup>Ø</sup> A simple example: Consider another cube, Discount, containing discount amounts for various combinations of product and city. More formally, the Discount cube has dimensions $D = \{ \mathrm { P R O D U C T } . $ LOCATION ; measure4 $M = \left\{ d i s c o u n t \right\}$ , and $A =$ $\{ \mathtt { p r o d u c t \_ n a m e } , \quad \mathtt { c i t y \_ I D } \}$ w h e re product\_name maps to the PRODUCT dimension and city\_ID maps to the LOCATION dimension. Suppose the user would like to know which discount amounts apply to the various cities in the Sales cube. To answer this query, the user may first apply the Cartesian Product operation to the Sales and Discount cubes as follows: Sales<sup>=</sup>Discount. Note that the result of this operation is a superset of the desired information. Further operations are required to extract the actual answer. Also note that the Cartesian Product operator places no restrictions on the domains of the dimension attributes. A special case of the Cartesian Product operator is the join operator, which can be used to express the above query more concisely by imposing certain restrictions, as we will demonstrate next.

Join Ž . <sup>j</sup> : The join operator is a special case of Cartesian Product operator that is used to relate two cubes having one or more dimensions in common, and having identical mappings from the common dimensions to the respective attribute sets of these dimensions. In other words two cubes $C _ { 1 } = \langle D _ { 1 }$ $\_ , \_ f _ { 1 } , \_ , \_ \rangle$ and $C _ { 2 } = \langle D _ { 2 } , \ldots , f _ { 2 } , \ldots \rangle$ are candidates for join iff $D _ { 1 } \cap D _ { 2 } \neq 0$ and $\forall d _ { i } \in ( D _ { 1 } \cap D _ { 2 } )$

$f _ { 1 } ( d _ { i } ) = f _ { 2 } ( d _ { i } )$ . Furthermore, let the dimensions in $D _ { 1 } \cap D _ { 2 }$ be referred to as the Common Dimensions Ž . cd and let $D _ { 1 } \cap D _ { 2 } = \{ { \mathrm { c d } } _ { 1 } , { \mathrm { c d } } _ { 2 } , \dots , { \mathrm { c d } } _ { l } \}$ . The algebra of join may be succinctly expressed through the following identity:

$$
C _ {1} \bowtie C _ {2} = \sigma_ {P} (C _ {1} \times C _ {2})
$$

where P is a predicate of the form $P = [ ( C _ { 1 } \mathsf { c d } _ { 1 } = C _ { 2 } -$ $\mathbf { c d } _ { 1 } ) \wedge ( C _ { 1 } \mathbf { c d } _ { 2 } = C _ { 2 } \mathbf { c d } _ { 2 } ) \wedge \ldots \wedge ( C _ { 1 } \mathbf { c d } _ { 1 } = \overline { { { C _ { 2 } } \mathbf { c d } _ { 1 } } } ) ] .$

A simple example: Consider the query in the previous example: the user would like to know which discount amounts apply to the various cities in the Sales cube. The answer to this query can be obtained easily by joining the Sales and Discount cubes as follows: Ž . Sales <sup>j</sup> Discount .

The next two operators are binary operators which require as input two union-compatible cubes. Loosely speaking, two cubes are union-compatible if they have an identical number of dimensions and measures and there is a 1-to-1 correspondence between dimensions and measures across the two cubes. A very informal way of putting it is that the cubes have the same structure. A more formal way of stating this is as follows: Cube $C _ { \mathrm { I 1 } } = \langle D _ { 1 } , M _ { 1 }$ $A _ { 1 } , f _ { 1 } , V _ { 1 } , g _ { 1 } \rangle$ and cube $C _ { 1 2 } = \langle D _ { 2 } , M _ { 2 } , A _ { 2 }$ $f _ { 2 } , V _ { 2 } , g _ { 2 } \rangle$ are union-compatible iff the following conditions simultaneously hold: i DimensionsŽ . must have the same cardinality; i.e., $| D _ { 1 } | = | D _ { 2 } |$ Ž . ii let $D _ { 1 } = \{ d _ { 1 1 } , d _ { 1 2 } , . . . , d _ { 1 n } \}$ and let $D _ { 2 } =$ $\{ d _ { 2 1 } , d _ { 2 2 } , \ldots , d _ { 2 n } \}$ . Then, ;i, domŽ . Žd <sup>s</sup>dom $d _ { 2 i } ) ;$ Ž .iii $f _ { 1 } ( D _ { 1 } ) = f _ { 2 } ( D _ { 2 } )$ . Note that this implies $A _ { 1 } = A _ { 2 } ;$ Ž . iv Measures must have the same cardinality, i.e., $\vert M _ { 1 } \vert = \vert M _ { 2 } \vert ; \mathrm { ( v ) }$ let $M _ { 1 } = \{ m _ { 1 1 } , m _ { 1 2 } , . . . , m _ { 1 k } \}$ and let $M _ { 2 } = \left\{ \begin{array} { c } { { m _ { 2 1 } , m _ { 2 2 } , . . . , m _ { 2 k } } } \end{array} \right\}$ . Then, ;i, domŽ $m _ { 1 i } ) =$ domŽ ${ \bf \nabla } _ { m _ { 2 i } } ) .$

Union Ž . <sup>j</sup> : The union operator finds the union of two cubes. The algebra of the union operator is defined as follows.

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I 1 } } = \langle D _ { 1 } , M _ { 1 } , A _ { 1 } , f _ { 1 } , V _ { 1 } , g _ { 1 } \rangle$ and a cube $C _ { 1 2 } = \langle D _ { 2 } , M _ { 2 } , A _ { 2 } , f _ { 2 } , V _ { 2 } , g _ { 2 } \rangle$ such that $C _ { \mathrm { I 1 } }$ and $C _ { 1 2 }$ are union-compatible.

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } / M _ { 0 } / A _ { 0 } = D _ { 1 } / M _ { 1 } / A _ { 1 } = D _ { 2 } / M _ { 2 } / A _ { 2 }$ and $V _ { 0 } = V _ { 1 } \cup V _ { 2 }$ . It is easily seen that the new mapping f is very easily derivable from $f _ { 1 }$ and $f _ { 2 }$ . Again $g _ { 0 }$ represents a mapping as previously defined. We doŽ not include this definition again due to space considerations..

<sup>Ø</sup> Mathematical notation: $C _ { \mathrm { I 1 } } \cup C _ { \mathrm { I 2 } } = C _ { 0 }$

<sup>Ø</sup> A simple example: consider two cubes, Sales\_East and Sales\_West, both having the same cube-instance as defined for the Sales cube, where Sales\_East contains sales data corresponding to the Eastern region and Sales\_West contains sales data corresponding to the Western region. <sup>3</sup> Suppose the user would like to consolidate the data for the two regions into a single cube. This consolidation can be accomplished using the following union operation: Sales\_East<sup>j</sup>Sales\_West, which results in a single cube containing sales data that appear in either or both regions if the latter case is possible .Ž .

Difference Ž . <sup>y</sup> . The difference operator finds the difference of two cubes. The algebra of the difference operator is defined as follows.

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I 1 } } = \langle D _ { 1 } , M _ { 1 } , A _ { 1 } , f _ { 1 } , V _ { 1 } , g _ { 1 } \rangle$ and a cube $C _ { 1 2 } = \langle D _ { 2 } , M _ { 2 } , A _ { 2 } , f _ { 2 } , V _ { 2 } , g _ { 2 } \rangle$ such that $C _ { \mathrm { I 1 } }$ and $C _ { 1 2 }$ are union-compatible.

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } / M _ { 0 } / A _ { 0 } = D _ { 1 } / M _ { 1 } / A _ { 1 } = D _ { 2 } / M _ { 2 } / A _ { 2 } , ~ f _ { 0 }$ $= f ,$ and $V _ { 0 } = V _ { 1 } - V _ { 2 }$ . The difference operator essentially removes the portion of cube $C _ { \mathrm { I 1 } }$ that is common to both cubes.

<sup>Ø</sup> Mathematical notation: $C _ { \mathrm { I 1 } } - C _ { \mathrm { I 2 } } = C _ { 0 }$

<sup>Ø</sup> A simple example: consider again the Sales\_West cube and also a cube Sales\_CA, having the same cube-instance as defined for the Sales cube, where Sales\_CA contains sales data corresponding to California, which belongs to the Western region. Suppose the user would like to remove the California data from the Sales\_West cube. This operation can be accomplished using the difference operator as follows: Sales\_West<sup>y</sup>Sales\_CA.

Remarks: An additional operation, intersection Ž . <sup>l</sup> , can be expressed in terms of the difference operator as follows: $C _ { \mathrm { I } 1 } - ( C _ { \mathrm { I } 1 } - C _ { \mathrm { I } 2 } ) = C _ { 0 }$ . Note that intersection is not a fundamental operator since it can be expressed in terms of other operators. For convenience, intersection may also be expressed as: $C _ { \mathrm { I 1 } } \cap C _ { \mathrm { I 2 } } = C _ { 0 }$

The next two operators can be categorized as transformation operators. OLAP queries often require that measures be treated as dimensions and vice versa. For example, in the Sales cube, the user may wish to restrict the cube based on the sales amount measure e.g., sales amountŽ $> 1 0 0 )$ . Since the restriction operator and other operators as wellŽ . applies to dimensions, a transformation operation is required to convert the measure to a dimension in order to answer this type of query. Conversely, dimensions often must be treated as measures and therefore, an operation is also required to transform dimensions to measures. The pull and push operators, which we now describe, perform such transformations and thus allow the uniform treatment of dimensions and measures.

Pull Ž . . The pull operator converts measures to dimensions. Let $D _ { R }$ be a set of dimension names, $D _ { R } = \{ d _ { R 1 } , d _ { R 2 } , \ldots , d _ { R q } \}$ . Let R be a set of measures to transform such that $R \subseteq M$ . We define an additional one-to-one mapping : $R \to D _ { R }$ , where represents a mapping of a measure $m _ { i } \in R$ to a dimension name $d _ { i } \in D _ { R }$ . The algebra of the pull operator is defined as follows.

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I } } = \langle D , M , A , f , V , g \rangle$ , a set of measures to transform R, a set of dimension names $D _ { R }$ , and a dimension name mapping .

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } = D \cup \kappa ( d _ { R i } ) ; ~ M _ { 0 } = M - R ; ~ A _ { 0 } = A \cup$ $f _ { 0 } ( \kappa ( d _ { R i } ) ) ;$ it is clear that $f _ { 0 }$ is easily derivable from f , in particular $f _ { 0 }$ , in addition to encapsulating all the mappings in f, must also contain the additional mapping $\forall m _ { i } \in R , \ f _ { 0 } ( m _ { i } ) \to d _ { R i }$ . Also note that the domain of $V _ { 0 }$ changes as all the values in $C _ { 0 }$ no longer include the components of R.

<sup>Ø</sup> Mathematical notation: $\phi _ { [ R , D _ { R . \kappa } ] } ( C _ { \mathrm { I } } ) = C _ { 0 } .$

A simple example: suppose the user would like to find those products having sales amount greater than 100. Since amount is a measure, we cannot perform the necessary restriction operation. We must first pull the measure as follows:

$$
\phi_ {[ \{\text { amount } \}, \{\text { SALES } \}, \kappa (\text { amount }) = \text { SALES } ]} (\text { Sales }).
$$

This operation creates a new dimension name, SALES, and a new dimension attribute, amount. The restriction operation can then be performed as follows: $\sigma _ { \mathrm { ( a m o u n t ) } } = \mathrm { { } } _ { 1 0 0 } \mathrm { { ( S a l e s ) } }$ .

Push Ž . . The push operator converts dimensions to measures. The algebra of the push operator is defined as follows:

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I } } = \langle D , M , A , f , V , g \rangle$ and a dimension name to transform $d _ { i }$

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } = D - d _ { i } ; M _ { 0 } = M \cup f ( d _ { i } ) ; A _ { 0 } = A$ $\textstyle - f ( d _ { i } ) ;$ and $f _ { 0 } = f .$ For $V _ { 0 }$ , dom $_ { V _ { 0 } } = \mathrm { d o m } _ { V } \times$ ${ \mathrm { d o m } } _ { \mu _ { 1 } } \times \ldots \times { \mathrm { d o m } } _ { \mu _ { p } }$ such that $\textstyle f ( d _ { i } ) =$ $\{ \mu _ { 1 } , \dotsc , \mu _ { p } \}$ and $| V _ { 0 } | \stackrel {  } { = } | V |$

<sup>Ø</sup> Mathematical notation: $\psi _ { d _ { i } } ( C _ { \mathrm { I } } ) = C _ { 0 }$

<sup>Ø</sup> A simple example: Continuing with the above example, suppose the user would now like to push amount back into the cube cell as a measure. We use the push operation as follows: $\psi _ { \mathrm { S A L E S } } ( \mathbf { S a l e s } )$

Partition $( \gamma )$ . The partition operator maps the points of a cube into meaningful groups. Such partitioning is required for certain types of aggregation. The standard SQL aggregate functions perform aggregation over the entire range of values. Recall thatŽ our aggregation operator is based on the SQL aggregate functions. OLAP queries often require that. aggregation be performed over specifically defined groups. For example, a moving average requires that the aggregate function AVG be applied to groups having size n where n is the window size. Therefore, an operation is required to group the cube values so that aggregation can be performed. Let t represent a mapping $\begin{array} { r l } { t \colon } & { { } \mathrm { d o m } _ { \mathrm { d i m } ( 1 ) } \times \mathrm { d o m } _ { \mathrm { d i m } ( 2 ) } } \end{array}$ $\times \ldots \times \mathrm { d o m } _ { \mathrm { d i m } ( n ) } \to V _ { \mathrm { G } }$ where $V _ { \mathrm { G } }$ represents a set of groups consisting of values. There is no requirement that the groups in $V _ { \mathrm { G } }$ be disjoint. Let R be a set of partitioning dimension attributes $\{ a _ { 1 } , a _ { 2 }$ $\ldots , a _ { q } \}$ such that $R \subseteq A$ . The algebra of the partition operator is defined as follows.

<sup>Ø</sup> Input: A cube $C _ { \mathrm { I } } = \langle D , M , A , f , V , g \rangle$ , a set of partitioning dimension attributes R, and a partitioning function t.

<sup>Ø</sup> Output: A cube $C _ { 0 } = \langle D _ { 0 } , M _ { 0 } , A _ { 0 } , f _ { 0 } , V _ { 0 } , g _ { 0 } \rangle$ where $D _ { 0 } = D ; M _ { 0 } = M ; \forall a _ { i } \epsilon R , A _ { 0 } = A \cup t ( a _ { i } ) ;$ and $f _ { 0 } = f .$ For $V _ { 0 } , \vert V _ { 0 } \vert = \vert V \vert .$

<sup>Ø</sup> Mathematical notation: $\gamma _ { t , R } ( C _ { \mathrm { I } } ) = C _ { 0 }$

<sup>Ø</sup> A simple example: Suppose the user would like to find the 3-year moving average of sales values over the entire period of record. The first step in answering this query is to partition the values into groups of three consecutive years, which can be done using the partition operator as follows: $\gamma _ { t , \{ \mathrm { y e a r } \} } ( \mathbf { S a l e s } )$ where t is a function mapping the points into the 3-year groups. Specifically, $t ( \mathrm { y e a r } ) = \{ \mathrm { y e a r } ^ { \prime } | ( \mathrm { y e a r } ^ { \prime }$ $= \operatorname { y e a r } ) \operatorname { v } ( \operatorname { y e a r } ^ { \prime } = \operatorname { y e a r } - 1 ) \operatorname { v } ( \operatorname { y e a r } ^ { \prime } = \operatorname { y e a r } - 2 ) \}$ . The result of this operation is a cube having the same dimensions and measures, and an additional attribute Ž Ž .. t year identifying the group to which the value belongs. This identifying attribute is then used in the aggregation part of the query, which we include in Section 5.

## 5. Examples

In this section, we demonstrate the capabilities of our proposed algebra by applying the algebra to example queries. Several complex queries are presented which we believe to be representative of typical OLAP queries. These queries are difficult to express using standard SQL. All examples apply to the Sales cube unless stated otherwise.

Query 1: Find the 3-year moÕing aÕerage of sales Õalues for the period 1950 to 1990. This query is a modified version of the example used in the previous section. It requires a partitioning of the cube into groups, aggregation over these groups, and dicing to select the appropriate values on the TIME dimension. This query is expressed in our algebra as follows

$$
\begin{array}{l} \sigma_ {(t (\text { year }) \geq 1 9 5 0 \land t (\text { year }) \leq 1 9 9 0)} \\ \left(\alpha_ {[ \text { AVG(amount), } \{t (\text { year }) \} ]} \big (\gamma_ {t, \{\text { year } \}} (\text { Sales }) \big)\right) = C _ {\text { Result }} \\ \text { where } t (\text { year }) = \{\text { year } ^ {\prime} | (\text { year } ^ {\prime} = \text { year }) \text { v } (\text { year } ^ {\prime} = \text { year } - 1) \text { v } (\text { year } ^ {\prime} = \text { year } - 2) \}. \end{array}
$$

Query 2: For each city, find the maximum sales for each year. Display the city, product name, year, and amount for the corresponding sale. This query requires transformation and aggregation and can be expressed in our algebra as follows:

$$
\begin{array}{l} \phi_ {[ \{\text {product\_name}, \{\text {PRODUCT} \}, \kappa ]} \big (\alpha_ {[ \text {MAX(amount),} \{\text {city,year} \} ]} \\ \qquad \Big (\phi_ {[ \{\text {weight,color}, \{\text {PRODUCT} \}, \kappa ]} \big (\psi_ {\text {PRODUCT}} (\text {Sales}) \big) \Big) \\ = C _ {\text {Result}} \\ \text {where} \forall m _ {i} \in R, \kappa (m _ {i}) = \text {PRODUCT}. \end{array}
$$

Query 3: i Find the total sales for each region; Ž . ( ) ii then find the corresponding totals for each city. In this example, i is a roll-up and ii is a drill-down.Ž . Ž . A drill-down is quite complex by nature, requiring several transformation operations and a join. These queries can be expressed in our algebra as follows:

$$
\begin{array}{l} \text {(i)} \alpha_ {[ \text {SUM(amount),\{region\}} ]} \big (\alpha_ {[ \text {SUM(amount),\{city\}} ]} (\text {Sales}) \big) \\ = C _ {\text {Region}} \\ \text {(iia)} \phi_ {[ \{\text {region}, \{\text {LOCATION}, \kappa \} ]} \big (\alpha_ {[ \text {SUM(amount),\{city\}} ]} \\ \big (\phi_ {[ \{\text {city,state}, \{\text {LOCATION}, \kappa \} ]} \big (\psi_ {\text {LOCATION}} (\text {Sales})) \big) \big) \\ = C _ {\text {City}} \end{array}
$$

where $\forall m _ { i } \in R , \kappa ( m _ { i } ) = \mathrm { L O C A T I O N } .$

$$
\left(\mathrm{iib}\right) \left(C _ {\text { Region }}\right) \bowtie \left(C _ {\text { City }}\right) = C _ {\text { Result }}
$$

Query 4: Find those products haÕing total sales during the summer June, July, August greater than( ) one-third of their sales for the entire year for 1996. This query requires first aggregating sales for the entire year and for the summer as shown below:

$$
\begin{array}{r l} & \alpha_ {[ \text { SUM(amount),   } \{\text { product\_name } \} ]} \\ & \quad \left(\sigma_ {\text { year } = 1 9 9 6} (\text { Sales })\right) = C _ {\text { A }} \\ & \alpha_ {[ \text { SUM(amount),   } \{\text { product\_name } \} ]} \\ & \quad \left(\sigma_ {[ \text { year } = 1 9 9 6 \land (\text { month } = \text { June } \lor \text { month } = \text { July } \lor \text { month } = \text { August }) ]} \\ & \quad (\text { Sales })\right) = C _ {\text { S }} \end{array}
$$

Next, we pull the amount attribute, i.e., convert it from a measure to a dimension. This operation is necessary for the subsequent restriction and must be done for both cubes.

$$
\begin{array}{l} \phi_ {[ \{\text {amount}, \{\text {SALES} \}, \kappa (\text {amount}) = \text {SALES} ]} (C _ {\mathrm{A}}) = C _ {\text {Annual}} \\ \phi_ {[ \{\text {amount}, \{\text {SALES} \}, \kappa (\text {amount}) = \text {SALES} ]} (C _ {\mathrm{S}}) = C _ {\text {Summer}} \end{array}
$$

We can then join the resulting two cubes and restrict the result to those values satisfying the predicate below, which requires that summer sales totals be greater than one-third of the annual sales totals:

$$
\begin{array}{r l} & \sigma_ {(C _ {\text { Summer } \cdot \text { amount }} > 1 / 3 C _ {\text { Annual } \cdot \text { amount }})} (C _ {\text { Annual }} \bowtie C _ {\text { Summer }}) \\ & = C _ {\text { Result }} \end{array}
$$

## 6. Conclusion

In this paper, we have addressed an important issue within the realm of decision support databases: the lack of a precise, commonly agreed upon conceptual model for OLAP. The need for such a model is clear as evidenced by the numerous OLAP products currently offered. The development of such products, however, has largely been piece-meal, where existing database technology is modified to solve a specific problem. This situation has resulted in not only a lack of a data model for multidimensional databases, but also a lack of an operations model. Such an operations model is critical in implementing relational query languages as it allows for query optimization.

To address this problem, we have made two significant contributions. First, we have presented a detailed data model for the data cube. Secondly, we have presented a detailed operations model for the data cube in the form of a powerful yet simple algebra that operates on the data cube. Our proposed model and algebra meets one of the key requirements of OLAP by allowing uniform treatment of dimensions and measures. We have also demonstrated the capabilities of the proposed algebra by providing examples of typical OLAP queries expressed in our algebra. We emphasize again that this work is one of the first to formally define a data and operations model for OLAP.

In addition, our work opens up several areas for future work. First, the properties of the operators must be examined to show the expressive power and completeness of the operators. Secondly, there are several outstanding issues related to the implementation of the algebra. These issues include how optimization will be handled and if and how the algebra can be implemented on top of a relational database engine.

## References

<sup>w</sup> <sup>x</sup> 1 S. Agarwal, R. Agrawal, P.M. Deshpande, A. Gupta, J.F. Naughton, R. Ramakrishnan, S. Sarawagi, On the computation of multidimensional aggregates, in: Proc. 22nd VLDB Conf., Mumbai, 1996.

<sup>w</sup> <sup>x</sup> 2 R. Agrawal, A. Gupta, S. Sarawagi, Modeling multidimensional databases, in: Proc. Thirteenth Intl. Conf. on Data Engineering, Birmingham, UK, April 7–11 1997, IEEE, pp. 232–243.

<sup>w</sup> <sup>x</sup> 3 Butler Group, Business case for data warehousing: strategies and technologies, White Paper, October 1996.

<sup>w</sup> <sup>x</sup> 4 J. Byard, D. Schneider, The ins and outs and everything in Ž between of data warehousing, Tutorial in ACM SIGMOD. Intl. Conf. on Management of Data, Montreal, Quebec, Canada, June 4–6 1996.

<sup>w</sup> <sup>x</sup> 5 S. Chauduri, U. Dayal, An overview of data warehousing and OLAP technology, SIGMOD Record 26 1 1997 65–74.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 E. Codd, A relational model for large shared data banks, Communications with the ACM 13 6 1970 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 E. Codd, A data base sublanguage founded on the relational calculus, in: Proc. ACM SIGFIDET Workshop on Data Description, Access, and Control, November 1971.

<sup>w</sup> <sup>x</sup> 8 E. Codd, Relational completeness of data base sublanguages, Data Base Systems, 1972.

<sup>w</sup> <sup>x</sup> 9 E.F. Codd, S.B. Codd, C.T. Salley, Providing OLAP on-lineŽ analytical processing to user-analysts: an IT mandate. Tech-. nical report, E.F. Codd and Associates, 1993.

<sup>w</sup> <sup>x</sup> 10 DBTG, Report of the codasyl data base task group, April 1971.

<sup>w</sup> <sup>x</sup> 11 R. Elmasri, S. Navathe, Fundamentals of Database Systems, Benjamin Cummings, 1994.

<sup>w</sup> <sup>x</sup> 12 J. Gray, A. Bosworth, A. Layman, H. Pirahesh, Data cube: a relational aggregation operator generalizing group-by, crosstab, and sub-totals, Technical Report MSR-TR-95-22, Microsoft, Redmond, WA, July 1995.

<sup>w</sup> <sup>x</sup> 13 J. Gray, S. Chaudhuri, A. Bosworth, A. Layman, D. Reichart, M. Venkatrao, Data cube: a relational aggregation operator generalizing group-by, cross-tab, and sub-totals, Data Mining and Knowledge Discovery 1 1 1997 29–53.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 A. Gupta, V. Harinarayan, D. Quass, Aggregate-query processing in data warehousing environments, in: Proc. 21st VLDB Conf., Zurich, Switzerland, 1995.

<sup>w</sup> <sup>x</sup> 15 M. Gyssens, L.V.S. Lakshmanan, A foundation for multi-dimensional databases, in: Proc. 23rd VLDB Conf., Athens, Greece, September 1997.

<sup>w</sup> <sup>x</sup> 16 V. Harinarayan, A. Rajaraman, J.D. Ullman, Implementing data cubes efficiently, in: Proc. ACM SIGMOD, Montreal, Canada, June 4–6 1996, pp. 205–216.

<sup>w</sup> <sup>x</sup> 17 W.H. Inmon, Building the Data Warehouse, 2nd edn., Wiley, New York, 1996.

<sup>w</sup> <sup>x</sup> 18 R. Kimball, The Data Warehouse Toolkit, 1st edn., Wiley, New York, 1996.

<sup>w</sup> <sup>x</sup> 19 R. Kimball, K. Strehlo, Why decision support fails and how to fix it, SIGMOD Record 24 3 1995 92–97.Ž . Ž .

<sup>w</sup> <sup>x</sup>20 M. Lacroix, A. Pirotte, Domain-oriented relational languages, in: Proc. Intl. Conf. on Very Large Databases, Tokyo, Japan, 1977.

<sup>w</sup> <sup>x</sup> 21 C. Li, X.S. Wang, A data model for supporting on-line analytical processing, in: Proc. Conf. on Information and Knowledge Management, Baltimore, MD, 81–88, November 1996.

<sup>w</sup> <sup>x</sup> 22 P. O’Neil, D. Quass, Improved query performance with variant indexes, in: Proc. ACM SIGMOD Intl. Conf. on Management of Data, Tucson, AZ, May 13–15 1997, pp. 38–49.

<sup>w</sup> <sup>x</sup> 23 M. Zloof, Query by example, in: Proc. of the National Computer Conference, Vol. 4, 1975.

Anindya Datta is an Associate Professor in the DuPree School of Management at the Georgia Institute of Technology. Previously he was an Assistant Professor of MIS at the University of Arizona, after finishing his doctoral studies at the University of Maryland, College Park. Dr. Datta’s undergraduate education was completed at the Indian Institute of Technology, Kharagpur. His primary research interests lie in studying technologies that have the potential to significantly impact the automated processing of organizational information. Examples of such technologies include Data Warehousing<sup>r</sup>OLAP and Workflow Systems. He has published more than 15 papers in refereed journals such as ACM Transactions on Database Systems, IEEE Transactions on Knowledge and Data Engineering, INFORMS Journal of Computing, Information Systems and IEEE Transactions on Systems, Man and Cybernetics. He has also published over 35 conference papers and has chaired as well as served on the program committees of reputed international conferences and workshops.

Helen Thomas is a doctoral student in the DuPree College of Management at the Georgia Institute of Technology. Helen was previously a doctoral student in the Management and Information Systems program at the University of Arizona. She has an MSE in Operations Research and Industrial Engineering from the University of Texas at Austin and a BS in Decision and Information Sciences from the University of Maryland at College Park. In addition, she has more than 5 years experience in the software consulting industry. Her primary research interests are in decision support databases, which include efficient OLAP query processing and data modeling for data warehouses<sup>r</sup>multidimensional databases.
