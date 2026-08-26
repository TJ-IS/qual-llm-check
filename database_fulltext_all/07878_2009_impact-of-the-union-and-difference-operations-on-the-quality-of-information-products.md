---
otero_id: 7878
otero_key: "WUZKVXN9"
title: "Impact of the Union and Difference Operations on the Quality of Information Products"
authors: "Amir Parssian; Sumit Sarkar; Varghese S. Jacob"
year: "2009"
journal: "Information Systems Research"
doi: "10.1287/isre.1070.0161"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/WUZKVXN9/fulltext/images/69c57f5a2dcf25cbb29a8da3bd21d05b0d964214ea44518301fac08cc0f1748a.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Impact of the Union and Difference Operations on the Quality of Information Products

Amir Parssian, Sumit Sarkar, Varghese S. Jacob,

## To cite this article:

Amir Parssian, Sumit Sarkar, Varghese S. Jacob, (2009) Impact of the Union and Difference Operations on the Quality of Information Products. Information Systems Research 20(1):99-120. http://dx.doi.org/10.1287/isre.1070.0161

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2009, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/WUZKVXN9/fulltext/images/f8b6a90c47b7195b2e339731b396985fc8bacf73e39f9cf062e5e9e92a8833fc.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Impact of the Union and Difference Operations on the Quality of Information Products

Amir Parssian

Department of Information Systems, Instituto de Empresa Business School, Madrid 28006, Spain, amir.parssian@ie.edu

Sumit Sarkar, Varghese S. Jacob

School of Management, University of Texas at Dallas, Richardson, Texas 75080 {sumit@utd.edu, vjacob@utd.edu}

nformation derived from relational databases is routinely used for decision making. However, little thought Iis usually given to the quality of the source data, its impact on the quality of the derived information, and how this in turn affects decisions. To assess quality, one needs a framework that defines relevant metrics that constitute the quality profile of a relation, and provides mechanisms for their evaluation. We build on a quality framework proposed in prior work, and develop quality profiles for the result of the primitive relational oper ations Difference and Union. These operations have nuances that make both the classification of the resulting records as well as the estimation of the different classes quite difficult to address, and very different from that for other operations. We first determine how tuples appearing in the results of these operations should be clas sified as accurate, inaccurate or mismember, and when tuples that should appear do not (called incomplete) in the result. Although estimating the cardinalities of these subsets directly is difficult, we resolve this by decom posing the problem into a sequence of drawing processes, each of which follows a hyper-geometric distribution. Finally, we discuss how decisions would be influenced based on the resulting quality profiles.

Key words: information quality framework; relational data model; probability calculus; hyper-geometric distributions; database marketing

History: Paulo Goes, Senior Editor; J. Leon Zhao, Associate Editor. This paper was received on February 28, 2006, and was with the authors 1 year for 2 revisions. Published online in Articles in Advance June 20, 2008.

## 1. Introduction

The importance of managing the quality of data, and the quality of information derived from the data, is well recognized. Nevertheless, poor data quality is a pervasive problem. A recent survey conducted by CNNMoney (2004) found that 25% of credit reports contain errors that are serious enough to deny consumers credits, loans, or even a job, and 79% of the credit reports sampled contained errors of some kind. Another national survey observed significant misreporting of patient data across the United States (Lorence 2003). Scientists have raised concerns about errors in Environmental Protection Agency data and other governmental databases (Cohn 2001). Industry experts put the cost of poor data quality to be around 15%–20% of an organization’s operating revenue (IDMA 2003), and the Data Warehousing Institute recently estimated that poor data quality costs businesses over \$600 billion each year (Ziff Davis 2006).

Errors in data occur for a variety of reasons. Obvious factors include intrinsic system errors, transaction errors, and data entry errors (Morey 1982). Some types of data are volatile, and therefore their quality can deteriorate with time if not frequently updated (Ballou et al. 1998). In other environments, the data is provided by end-users who may deliberately falsify their information (Jiang et al. 2005). To complicate matters, data are repeatedly reused, affecting many decisions over time (Wang et al. 1995). Consequently, identifying and eliminating all the factors that lead to poor data quality is nontrivial, and in many cases, economically unjustifiable. In response to these issues, data cleansing has emerged as an industry in its own right—however, such efforts usually cannot remove all quality deficiencies (Ballou and Tayi 1999).

The data quality problem has grown dramatically over the last few years as firms are increasingly adopting data-driven approaches to business decision making. Extant research on data quality has addressed a variety of issues. Wang et al. (1995) provide a framework that categorizes different streams of data quality research where they summarize the main issues studied, and list unexplored issues worthy of research efforts. An important phenomenon that has emerged is that businesses are treating information as a product to be delivered to end-users (Ballou et al. 1998, Wang et al. 1998). As a result, these researchers propose that the quality of data be managed analogous to that of physical products. In a related context, Fisher et al. (2003) demonstrate that knowledge of the quality of information products influences decisions by managers, and recommend that this quality information (i.e., quality metadata) be provided to management along with the data itself.

While viewing quality issues in terms of information products is now well accepted, implementing a quality management process remains a challenging task. An important contributing factor is that firms are usually unable to directly measure the quality of information products because the number of such products can be very large (Ballou et al. 2006). This makes it difficult for firms to estimate the cost of poorquality data. On the other hand, the problems encountered in assessing the quality of derived information based on the inherent quality of the source databases have been largely ignored. While Ballou et al. (1998) provide a framework to evaluate the quality of information products based on the operations performed on the source data, they assume that the impact of each processing activity can be determined in some manner. An important requirement to operationalize such a framework is the ability to derive the quality of information products based on the operations performed on the source data. Our work addresses important aspects of this problem in the context of relational databases.

Four prior works are particularly relevant in that regard. The first, by Kon et al. (1995), presented an error representation schema consisting of three error types, inaccuracy, incompleteness, and mismembership, and showed these error types to be closed under relational algebra operations. In their framework, a tuple is inaccurate if it correctly identifies a relevant real-world entity but has inaccurately recorded one or more of its nonidentifier attributes; it is a mismember if it does not belong in the relation; and, it is incomplete if it corresponds to an entity instance in the real world that should be captured in the relation but is not. In the same vein, a tuple is accurate if it accurately represents all attributes of an entity in the real world. This work does not provide a methodology for deriving quality metrics for the output of relational operations. Reddy and Wang (1995) have provided an analysis of the error propagation process, but when only inaccuracies and mismembers are present. Incompleteness is a critical data quality attribute, particularly for applications that draw on multiple internal and external data sources. Further, that work does not explicitly recognize the impact of identifiers on the quality metrics of input and output relations, which leads to ambiguity in classifying tuples in the output. Ballou et al. (2006) determine the quality of information products using a single quality metric for each relation that is based on an acceptability criteria defined for relations based on user perceptions that the relation is fit for use. Finally, and most relevant to this work, Parssian et al. (2004) derived the quality profile (constituting the metrics for accuracy, inaccuracy, mismembership, and incompleteness as formally defined in §2) of the relations resulting from the operations Selection, Projection, and Cartesian Product, considering all the three types of errors. That work does not address the two other primitive relational algebra operations, Difference and Union. Our research focuses on these two operations.

Both the Difference and Union operations are widely used and are intuitively easy to understand. However, estimating the quality profiles of their results is nontrivial, and very different from such estimations for the other three primitive operations considered in Parssian et al. (2004). Importantly, the quality profile of the resulting relation can significantly affect the decisions being made. For instance, it could have a severe impact on the return on investment (ROI) of projects that use the data. Consider, for example, a firm that is planning a marketing campaign to obtain new customers and purchases a data set (called Prospect) for which the mismembership is known to be 10%. To exclude existing customers in the campaign, a Difference operation could be performed on Prospect with the existing customer data set (called Current). When estimating the ROI for the promotion based on the resultant data, a question that arises is what quality profile should be used for this calculation. Should the mismembership rate of 10% be used for the resultant data? We show that mismembership (and the other quality dimensions) could change substantially as a result of the operation, and is closely tied to the size of the set of eliminated tuples. If the mismembership turns out to be significantly higher, then the ROI on the marketing campaign would be correspondingly lower, and may even lead to a decision to not run the campaign using that data set.

Another interesting decision problem in this context arises from the fact that tuples in two data sets that correspond to the same entity instance may not match exactly because of inaccuracies in their nonidentifying attributes. Although the Difference and Union operations do not automatically eliminate such tuples from the result, based on identifying attributes such tuples can be easily isolated and removed from the resulting relation. It is then possible to examine the quality implications of augmenting the Difference and Union operations in this manner, and compare them to the result of the pure Difference and Union operations. Under what situations should one use the augmented approaches as opposed to the pure operations? We demonstrate how the quality profiles of the results differ in these two scenarios, and discuss circumstances under which one or the other approach would be preferred.

The primary contribution of this research is the development of techniques to derive the quality profiles for the results of the operations Union and Difference. To accomplish this, we first determine how to classify tuples appearing in the relations resulting from these operations, as well as tuples that should have appeared in the resulting relations but do not because of inaccurate or missing data. We assume that the errors occur independently in the relations participating in such operations (i.e., the participating relations are not drawn from the same underlying base relation). The classification of tuples allows us to determine when tuples from each subset (i.e., accurates, inaccurates, mismembers, and incompletes) of the participating relations will appear in a specific subset of the resulting relation. We find that, although directly estimating the sizes of the subsets in the resulting relation is a difficult problem, it can be resolved by appropriately decomposing the problem into a series of simpler subproblems. We show that the sizes of these subsets can be viewed as the outcome of a combination of drawing processes implied by our decomposition method, and these processes follow univariate or multivariate hypergeometric distributions. Using properties of these distributions, we can obtain estimates of the quality metrics that constitute the quality profiles of the relations resulting from these two operations.

The techniques developed in this research can be directly used to make a variety of business decisions. In addition to the marketing campaign example already discussed, these techniques could be used to determine if data derived from the Difference or Union operations meet desired quality levels for their intended task, and whether data cleansing activities are needed. These techniques, which complement our previous analyses for the other primitive operations, can serve as the basic building blocks for deriving the quality profile for information produced using queries involving sequences of the primitive operations.

The next section gives the formal error definitions and base metrics used to define the quality profile of a relation. In §3 we show how tuples should be classified in a relation resulting from the Difference operation and from the Union operation, respectively. In §4, we derive expressions for the quality metrics of the result in terms of the quality metrics of the two data sets and the cardinality of the set of common tuples. Section 5 shows how our analyses can impact decisions in several scenarios, including the impact of varying levels of data quality. Section 6 concludes the paper, and provides directions for future research.

## 2. Definitions and Base Metrics

We use the quality metrics proposed by Parssian et al. (2004) to operationalize the three error types discussed in §1. The error types and associated metrics are briefly described next. Consider a relation (denoted by S) that contains the collection of all tuples captured for a predefined real-world entity type. The attribute(s) of the entity that uniquely identifies each entity instance is (are) called its identifying attribute(s), or identifier. We denote the set of accurate, inaccurate, and mismember tuples by $S _ { \mathrm { { A } } } , S _ { \mathrm { { I } } } ,$ and $S _ { \mathrm { { M } } } ,$ respectively. Tuples with inaccurate identifying attribute values are classified as mismembers. While some mismember tuples have accurate values for all nonidentifying attributes, others may have one or more inaccurate values for such attributes. This distinction is important for our analysis, as we show later. We denote the subset of mismember tuples that have accurate values for all their nonidentifying attributes by $\hat { S } _ { \mathrm { { M } } } ;$ the rest are denoted by $\tilde { S } _ { \mathrm { M } } . \mathrm { A }$ fourth category of data associated with S corresponds to entity instances that are missing in S. A tuple belongs to the incomplete set if it should have been captured into S but it is not. The set of incomplete tuples of S is denoted by $S _ { \mathrm { { C } } } .$ . The cardinalities of the different sets are denoted by . The metrics that constitute the quality profile for a relation S are as follows:

Accuracy. Accuracy of S is the probability that a tuple in S accurately represents an entity in the real world. It is measured by $\alpha _ { S } = | S _ { \mathrm { A } } | / | S |$

Inaccuracy. Inaccuracy of S is the probability that a tuple in S is inaccurate. It is measured by $\beta _ { S } = | S _ { \mathrm { I } } | / | S |$

Mismembership. Mismembership of S is the probability that a tuple in S is a mismember. It is measured by $\mu _ { S } = | S _ { \mathrm { { M } } } | / | S |$

Incompleteness. Incompleteness of S is the probability that an entity instance in the real world is not captured in S. It is measured by $\chi _ { S } = \vert S _ { \mathrm { C } } \vert / ( \vert S \vert -$ $| S _ { \mathrm { M } } | + | S _ { \mathrm { C } } | )$ . With $| T | = | S | - | S _ { \mathrm { M } } | + | S _ { \mathrm { C } } |$ and $| S _ { C } | \leq | T |$ we have $0 \leq \chi _ { S } \leq 1$

To determine the values of these metrics, each tuple in S could be individually examined for its error status and all incomplete tuples identified. This, however, would be a hard and costly task when the number of tuples involved is large. Appropriate statistical sampling methods are typically deployed to estimate these metrics (Morey 1982). The estimates for $\alpha _ { S } , \beta _ { S } ,$ , and $\mu _ { S }$ can usually be obtained in a straightforward manner by determining an appropriate sample size for a given relation, selecting a randomly identified set of tuples, and then manually verifying the data recorded in these sample tuples. If necessary, estimates at the attribute level can be used to derive the quality profiles of the participating relations (Parssian et al. 2004); we should point out that the estimates of the sizes of the different subsets of the relations resulting from the Union and Difference operations are not impacted by the quality of individual attributes in the participating relations, but by the overall quality of these relations. To estimate $\chi _ { S } ,$ it is necessary to obtain a sample of the real-world entity instances, and then verify what proportion is represented in the database (Motro and Rakov 1998).

Since $S _ { \mathrm { { A } } } , S _ { \mathrm { { I } } }$ , and $S _ { \mathrm { { M } } }$ constitute $S ,$ we have $0 \leq \alpha _ { S } ,$ $\beta _ { S } , \mu _ { S } \leq 1$ , and $\alpha _ { S } + \beta _ { S } + \mu _ { S } = 1$ . We also have $\left. S _ { \mathrm { M } } \right. =$ $| \hat { S } _ { \mathrm { M } } | + | \tilde { S } _ { \mathrm { M } } |$ . These two terms can be estimated from accuracies of the attributes in S (Parssian et al. 2004). If attribute-level accuracies are not available, then $| \hat { S } _ { \mathrm { M } } |$ can be estimated from the table-level parameters as $| \hat { S } _ { \mathrm { M } } | = | S _ { \mathrm { M } } | \cdot \alpha _ { s } / ( \alpha _ { s } + \beta _ { s } )$ , with $| \tilde { S } _ { \mathrm { M } } |$ constituting the rest of $| S _ { \mathrm { M } } |$

## 3. Tuple Categorizations

To derive the quality profiles of the results of the Difference and Union operations, it is important to understand the interaction between records in the participating relations and how to categorize each tuple that appears in the result. Consider, for example, the Difference operation performed over two relations $S _ { 1 }$ and $S _ { 2 } ,$ i.e., $R = S _ { 1 } - S _ { 2 }$ . Let a record $t _ { 1 } \in S _ { 1 }$ match a record $t _ { 2 } \in S _ { 2 }$ . Then $t _ { 1 }$ does not appear in the result R. Nevertheless, it could play a role in the quality metrics of R depending on the quality of $t _ { 1 }$ and $t _ { 2 } .$ . For example, if both $t _ { 1 }$ and $t _ { 2 }$ are accurate, then the quality of R is not directly affected. However, if $t _ { 1 }$ is accurate in $S _ { 1 }$ and $t _ { 2 }$ is a mismember in $S _ { 2 } ,$ then $t _ { 1 }$ should appear in R but does not. Therefore, it now belongs to the incomplete set and contributes to the incompleteness measure for R. On the other hand, if $t _ { 1 }$ is a mismember and $t _ { 2 }$ is accurate, then $t _ { 1 } ^ { \prime } { \bf s }$ absence in R is desirable, as otherwise it would have contributed to the set of mismembers in the result. A factor that further complicates the analysis is the impact of incompleteness. Continuing with the above example, if $t _ { 1 }$ is accurate in $S _ { 1 }$ and $t _ { 2 }$ is missing in $S _ { 2 }$ when it should have been included, then $t _ { 1 }$ will show up in R when it should not. Therefore, it is now a mismember in R. We elaborate in this section how tuples should be classified in a relation resulting from the Difference operation and from the Union operation, respectively.

3.1. Categorizations for the Difference Operation We discuss tuple categorization for the Difference operation with an example. Let $T _ { 1 }$ and $T _ { 2 }$ be two conceptual (true) relations for the two real-world entities, Prospect and Current, of our example company. Let $S _ { 1 }$ and $S _ { 2 }$ be their stored (imperfect) relations, with $S _ { \mathrm { 1 C } }$ and $S _ { 2 C }$ being the corresponding incomplete data sets. The attribute CUST\_ID is the identifier for both relations, and attributes NAME and DOB (Date of Birth) are nonidentifiers. These relations are shown in $\mathrm { F i g \mathrm { - } }$ ures 1, 2, and 3. In Figure $^ { 2 , }$ the Tuple Status column is for illustrative purposes and is not available for storing. The symbols $\bar { \mathbf { A } } , \bar { \mathbf { I } } , \widehat { \mathbf { M } }$ , and $\widetilde { \mathrm { M } }$ stand for tuples that are accurate, inaccurate, mismember with all accurate values for the nonidentifier attributes, and mismember with some inaccurate values for the nonidentifier attributes, respectively. Inaccurate attribute values are identified by a grey background. The Difference T of $T _ { 1 }$ and ${ T _ { 2 } } \left( { \mathrm { i . e . , ~ } } T = { T _ { 1 } } - { T _ { 2 } } \right)$ and the Difference R of $S _ { 1 }$ and $S _ { 2 } ( \mathrm { i . e . , ~ } R = S _ { 1 } - S _ { 2 } )$ are shown in Figures 4 and 5, respectively. The incomplete data set $R _ { \mathrm { { C } } }$ includes those instances in T that do not appear in $R .$ Note that this is not the same as $T - R$ since the inaccurate tuples in R could have corresponding instances in $T \left( \mathrm { e . g . } \right.$ , the customer identified by C8). $R _ { \mathrm { { C } } }$ is shown in Figure 6.

Tuples in $S _ { 1 }$ that have a matching counterpart in $S _ { 2 }$ are removed from $S _ { 1 }$ to obtain R. Tuples that remain in R continue to have the same status as in $S _ { 1 }$ for some instances, while in other instances the status changes. To determine the quality profile for $R ,$ it is necessary to correctly recognize the status for tuples that remain in the result as well as for tuples that are eliminated. To conduct our analysis, we need to differentiate between two types of matches, perfect and imperfect. Perfect matches occur between tuples in $S _ { 1 }$ and $S _ { 2 }$ that have identical values for all their corresponding attributes, and are removed as a result of the Difference operation $( \mathrm { e . g . } ,$ tuples with identifiers $^ { \prime \prime } { \bf O } { \bf r } \ ^ { \prime \prime } { \bf C } 1 8 ^ { \prime \prime }$ in Figure 2). Imperfect matches occur between tuples in $S _ { 1 }$ and $S _ { 2 }$ that have identical values for their identifiers and differ in one or more values of their nonidentifier attributes (e.g., tuples with identifiers $^ { \prime \prime } C 2 ^ { \prime \prime }$ or $^ { \prime \prime } { \mathsf { C } } 2 4 ^ { \prime \prime }$ in Figure 2). These tuples remain in the result, although they can be easily identified. The numbers of perfect and imperfect matches are easily available in practice. The number of perfect matches is equal to the difference in the cardinality of $S _ { 1 }$ and $R .$ The number of imperfect matches can be obtained by determining how many tuples in $S _ { 1 }$ and $S _ { 2 }$ have identical values for their identifiers, and then subtracting from this the number of perfect matches.

Perfect matches can only occur between a tuple in $S _ { \mathrm { 1 A } } \cup \hat { S } _ { \mathrm { 1 M } }$ and a tuple in $\dot { S _ { 2 \mathrm { A } } } \cup \hat { S } _ { 2 \mathrm { M } }$ . We disregard perfect matches between $S _ { \mathrm { 1 I } } \cup \tilde { S } _ { \mathrm { 1 M } }$ and $S _ { \mathrm { 2 I } } \cup \tilde { S } _ { \mathrm { 2 M } }$ since the probability that an entity instance appearing in both data sets will have exactly the same inaccurate values for their corresponding attributes is very low (because errors in the two data sets are assumed to occur independently). This is particularly true when attributes take their values from large domains, or when there are a large number of inaccurate attribute values in a tuple. Therefore, tuples in $S _ { 1 }$ with inaccurate attribute-values are assumed to not have perfectly matching tuples in $S _ { 2 } .$ . Similar arguments hold for other components.

Figure 1 The Conceptual Relations $T _ { 1 }$ and $T _ { 2 }$

<table><tr><td colspan="3"> $T_1$ </td><td colspan="3"> $T_2$ </td></tr><tr><td>CUST_ID</td><td>NAME</td><td>DOB</td><td>CUST_ID</td><td>NAME</td><td>DOB</td></tr><tr><td>C1</td><td>Eric Brown</td><td>01-05-1978</td><td>C1</td><td>Eric Brown</td><td>01-05-1978</td></tr><tr><td>C2</td><td>Sue Carter</td><td>14-09-1979</td><td>C2</td><td>Sue Carter</td><td>14-09-1979</td></tr><tr><td>C3</td><td>Denis Shaw</td><td>12-08-1965</td><td>C5</td><td>Cindy Owen</td><td>22-10-1972</td></tr><tr><td>C4</td><td>Andre Green</td><td>03-07-1969</td><td>C6</td><td>George Lynn</td><td>15-02-1970</td></tr><tr><td>C5</td><td>Cindy Owen</td><td>22-10-1972</td><td>C7</td><td>Steven Turner</td><td>06-06-1966</td></tr><tr><td>C6</td><td>George Lynn</td><td>15-02-1970</td><td>C10</td><td>Randy Rider</td><td>23-09-1976</td></tr><tr><td>C7</td><td>Steven Turner</td><td>06-06-1966</td><td>C11</td><td>Mark Randall</td><td>07-08-1968</td></tr><tr><td>C8</td><td>Andrew Flint</td><td>17-11-1977</td><td>C12</td><td>Andy Jackson</td><td>04-07-1969</td></tr><tr><td>C9</td><td>Ellen Sawyer</td><td>25-01-1971</td><td>C15</td><td>Sherry Cassidy</td><td>16-05-1967</td></tr><tr><td>C10</td><td>Randy Rider</td><td>23-09-1976</td><td>C16</td><td>Brian Shultz</td><td>14-10-1971</td></tr><tr><td>C11</td><td>Mark Randall</td><td>07-08-1968</td><td>C17</td><td>Angie Gunter</td><td>12-12-1970</td></tr><tr><td>C12</td><td>Andy Jackson</td><td>04-07-1969</td><td>C20</td><td>Todd Ingram</td><td>07-11-1974</td></tr><tr><td>C13</td><td>Laura Marsh</td><td>28-12-1975</td><td>C21</td><td>Debbie Arnold</td><td>03-02-1972</td></tr><tr><td>C14</td><td>David Duval</td><td>19-11-1973</td><td>C22</td><td>Linda Larson</td><td>19-07-1975</td></tr><tr><td>C15</td><td>Sherry Cassidy</td><td>16-05-1967</td><td>C25</td><td>Nancy Fort</td><td>08-06-1967</td></tr></table>

Figure 2 The Stored Relations

<table><tr><td colspan="4"> $S_1$ </td><td colspan="4"> $S_2$ </td></tr><tr><td>CUST_ID</td><td>NAME</td><td>DOB</td><td>Tuple status</td><td>CUST_ID</td><td>NAME</td><td>DOB</td><td>Tuple status</td></tr><tr><td>C1</td><td>Eric Brown</td><td>01-05-1978</td><td>A</td><td>C1</td><td>Eric Brown</td><td>01-05-1978</td><td>A</td></tr><tr><td>C2</td><td>Sue Carter</td><td>14-09-1979</td><td>A</td><td>C2</td><td>Sue Carter</td><td>14-09-1975</td><td>I</td></tr><tr><td>C3</td><td>Denis Shaw</td><td>12-08-1965</td><td>A</td><td>C3</td><td>Denis Shaw</td><td>12-08-1965</td><td> $\widehat{M}$ </td></tr><tr><td>C4</td><td>Andre Green</td><td>03-07-1969</td><td>A</td><td>C4</td><td>Andrew Johnson</td><td>03-07-1969</td><td> $\widetilde{M}$ </td></tr><tr><td>C5</td><td>Cindy Owen</td><td>22-10-1972</td><td>A</td><td>C6</td><td>George Lynn</td><td>15-02-1970</td><td>A</td></tr><tr><td>C6</td><td>George Lynn</td><td>15-02-1972</td><td>I</td><td>C7</td><td>Steven Turner</td><td>06-06-1976</td><td>I</td></tr><tr><td>C7</td><td>Steve Turner</td><td>06-06-1966</td><td>I</td><td>C8</td><td>Andrew Flint</td><td>17-11-1977</td><td> $\widehat{M}$ </td></tr><tr><td>C8</td><td>Andrew Flint</td><td>17-11-1979</td><td>I</td><td>C9</td><td>Ellen Sayer</td><td>25-01-1971</td><td> $\widetilde{M}$ </td></tr><tr><td>C9</td><td>Elen Sawyer</td><td>25-01-1971</td><td>I</td><td>C11</td><td>Mark Randall</td><td>07-08-1968</td><td>A</td></tr><tr><td>C10</td><td>Randy Rider</td><td>23-09-1967</td><td>I</td><td>C12</td><td>Amy Jackson</td><td>04-07-1969</td><td>I</td></tr><tr><td>C16</td><td>Brian Shultz</td><td>14-10-1971</td><td> $\widehat{M}$ </td><td>C13</td><td>Laura Marsh</td><td>28-12-1975</td><td> $\widehat{M}$ </td></tr><tr><td>C17</td><td>Angie Gunter</td><td>12-12-1970</td><td> $\widehat{M}$ </td><td>C14</td><td>David Duval</td><td>19-11-1975</td><td> $\widetilde{M}$ </td></tr><tr><td>C18</td><td>Janice Walker</td><td>04-07-1977</td><td> $\widehat{M}$ </td><td>C16</td><td>Brian Shultz</td><td>14-10-1971</td><td>A</td></tr><tr><td>C19</td><td>Sandra Willis</td><td>10-09-1968</td><td> $\widehat{M}$ </td><td>C17</td><td>Angie Hunter</td><td>12-12-1970</td><td>I</td></tr><tr><td>C20</td><td>Todd Ingram</td><td>07-11-1974</td><td> $\widehat{M}$ </td><td>C18</td><td>Janice Walker</td><td>04-07-1977</td><td> $\widehat{M}$ </td></tr><tr><td>C21</td><td>Jack Smith</td><td>03-02-1972</td><td> $\widetilde{M}$ </td><td>C19</td><td>Sandra Willis</td><td>10-09-1965</td><td> $\widetilde{M}$ </td></tr><tr><td>C22</td><td>Linda Larson</td><td>19-07-1976</td><td> $\widetilde{M}$ </td><td>C21</td><td>Debbie Arnold</td><td>03-02-1972</td><td>A</td></tr><tr><td>C23</td><td>Cathy Edwards</td><td>21-05-1966</td><td> $\widetilde{M}$ </td><td>C22</td><td>Linda Larson</td><td>19-07-1971</td><td>I</td></tr><tr><td>C24</td><td>Mary Klein</td><td>27-09-1972</td><td> $\widetilde{M}$ </td><td>C23</td><td>John Miller</td><td>21-05-1966</td><td> $\widehat{M}$ </td></tr><tr><td>C25</td><td>Nancy Ford</td><td>08-06-1967</td><td> $\widetilde{M}$ </td><td>C24</td><td>Mary Kalvin</td><td>27-09-1972</td><td> $\widetilde{M}$ </td></tr></table>

In addition to the observed perfect and imperfect matches between $S _ { 1 }$ and $S _ { 2 } ,$ we also need to consider matches that would have occurred if tuples in the incomplete sets for the two tables had been accurately captured. Such unobserved potential matches are also of two types, perfect and imperfect. Matches that occur for entity instances that have accurate values for all the nonidentifier attributes in one stored table and have not been captured in the other table, are unobserved potential perfect matches (e.g., C5). This type of an unobserved match also includes those instances which are part of the incomplete set for both tables. The other type of unobserved potential matches occurs for entity instances which are not captured in one table and have one or more inaccurate nonidentifier attribute-values stored in the other table. Examples of such unobserved potential imperfect matches are C12 and C25.

Figure 3 The Incomplete Data Sets

<table><tr><td colspan="3"> $S_{1C}$ </td><td colspan="3"> $S_{2C}$ </td></tr><tr><td>CUST_ID</td><td>NAME</td><td>DOB</td><td>CUST_ID</td><td>NAME</td><td>DOB</td></tr><tr><td>C11</td><td>Mark Randall</td><td>07-08-1968</td><td>C5</td><td>Cindy Owen</td><td>22-10-1972</td></tr><tr><td>C12</td><td>Andy Jackson</td><td>04-07-1969</td><td>C10</td><td>Randy Rider</td><td>23-09-1976</td></tr><tr><td>C13</td><td>Laura Marsh</td><td>28-12-1975</td><td>C15</td><td>Sherry Cassidy</td><td>16-05-1967</td></tr><tr><td>C14</td><td>David Duval</td><td>19-11-1973</td><td>C20</td><td>Todd Ingram</td><td>07-11-1974</td></tr><tr><td>C15</td><td>Sherry Cassidy</td><td>16-05-1967</td><td>C25</td><td>Nancy Fort</td><td>08-06-1967</td></tr></table>

Figure 4 $\tau = T _ { 1 } - T _ { 2 }$

<table><tr><td colspan="3">T</td></tr><tr><td>CUST_ID</td><td>NAME</td><td>DOB</td></tr><tr><td>C3</td><td>Denis Shaw</td><td>12-08-1965</td></tr><tr><td>C4</td><td>Andre Green</td><td>03-07-1969</td></tr><tr><td>C8</td><td>Andrew Flint</td><td>17-11-1977</td></tr><tr><td>C9</td><td>Ellen Sawyer</td><td>25-01-1971</td></tr><tr><td>C13</td><td>Laura Marsh</td><td>28-12-1975</td></tr><tr><td>C14</td><td>David Duval</td><td>19-11-1973</td></tr></table>

Figure 5 $R = S _ { 1 } - S _ { 2 }$

<table><tr><td colspan="4">R</td></tr><tr><td>CUST_ID</td><td>NAME</td><td>DOB</td><td>Tuple status</td></tr><tr><td>C2</td><td>Sue Carter</td><td>14-09-1979</td><td> $\widehat{M}$ </td></tr><tr><td>C4</td><td>Andre Green</td><td>03-07-1969</td><td>A</td></tr><tr><td>C5</td><td>Cindy Owen</td><td>22-10-1972</td><td> $\widehat{M}$ </td></tr><tr><td>C6</td><td>George Lynn</td><td>15-02-1972</td><td> $\widetilde{M}$ </td></tr><tr><td>C7</td><td>Steve Turner</td><td>06-06-1966</td><td> $\widetilde{M}$ </td></tr><tr><td>C8</td><td>Andrew Flint</td><td>17-11-1979</td><td>I</td></tr><tr><td>C9</td><td>Elen Sawyer</td><td>25-01-1971</td><td>I</td></tr><tr><td>C10</td><td>Randy Rider</td><td>23-09-1967</td><td> $\widetilde{M}$ </td></tr><tr><td>C17</td><td>Angie Gunter</td><td>12-12-1970</td><td> $\widehat{M}$ </td></tr><tr><td>C19</td><td>Sandra Willis</td><td>10-09-1968</td><td> $\widehat{M}$ </td></tr><tr><td>C20</td><td>Todd Ingram</td><td>07-11-1974</td><td> $\widehat{M}$ </td></tr><tr><td>C21</td><td>Jack Smith</td><td>03-02-1972</td><td> $\widetilde{M}$ </td></tr><tr><td>C22</td><td>Linda Larson</td><td>19-07-1976</td><td> $\widetilde{M}$ </td></tr><tr><td>C23</td><td>Cathy Edwards</td><td>21-05-1966</td><td> $\widetilde{M}$ </td></tr><tr><td>C24</td><td>Mary Klein</td><td>27-09-1972</td><td> $\widetilde{M}$ </td></tr><tr><td>C25</td><td>Nancy Ford</td><td>08-06-1967</td><td> $\widetilde{M}$ </td></tr></table>

The following examples demonstrate how tuples in the result should be characterized. We first analyze the effect of perfect matches considering both observed and unobserved types. Consider an entity instance that is perfectly recorded in $S _ { 1 }$ and does not have a corresponding tuple (accurate or inaccurate) in $S _ { 2 }$ . The tuple in $S _ { 1 }$ will show up in the result, and will be accurate in R if the entity instance is not part of $S _ { 2 C } ,$ the incomplete set of $S _ { 2 }$ . If it is part of $S _ { 2 C } ,$ then the tuple becomes a mismember in R. On the other hand, if a tuple $t _ { 1 }$ is part of $\hat { S } _ { 1 \mathrm { M } } ,$ and it does not have a matching tuple (perfect or imperfect) in $S _ { 2 } ,$ then it continues to be a mismember in R regardless of whether the entity instance is a part of $S _ { 2 C }$ . Similarly, tuples that are eliminated could become part of the incomplete set of R. If $t _ { 1 } \in S _ { \mathrm { 1 A } }$ has a matching tuple in $S _ { 2 \mathrm { A } } ,$ it is correctly eliminated and contributes to neither R nor $R _ { C } .$ . However, if $t _ { 1 } \in S _ { \mathrm { 1 A } }$ has a matching tuple in $\hat { S } _ { 2 \mathrm { M } } ,$ , then it will not appear in R when it should have, thereby becoming part of $R _ { \mathrm { C } } . \mathrm { A }$ tuple in $S _ { \mathrm { 1 C } }$ becomes part of $R _ { \mathrm { { C } } }$ if it does not have a matching tuple in $S _ { 2 \mathrm { A } }$ or $S _ { 2 C } ;$ if such a match exists, then it no longer belongs to $R _ { \mathrm { C } } . \mathrm { ~ A ~ }$ tuple in $S _ { \mathrm { 1 C } }$ that has a matching tuple in $\bar { S } _ { 2 \mathrm { M } }$ also becomes part of $R _ { \mathrm { { C } } }$ . Figure 7 summarizes all the feasible tuple categorizations when a tuple $t _ { 1 } \in \{ S _ { 1 } \cup S _ { \mathrm { 1 C } } \}$ perfectly matches a tuple $t _ { 2 } \in \{ S _ { 2 } \cup S _ { 2 \mathrm C } \}$ , along with examples from the relations shown in Figures 2 and 3.

Figure 6 Incomplete Data Set for R

<table><tr><td colspan="3"> $R_{C}$ </td></tr><tr><td>CUST_ID</td><td>NAME</td><td>DOB</td></tr><tr><td>C3</td><td>Denis Shaw</td><td>12-08-1965</td></tr><tr><td>C13</td><td>Laura Marsh</td><td>28-12-1975</td></tr><tr><td>C14</td><td>David Duval</td><td>19-11-1973</td></tr></table>

Next, we consider the role of imperfect matches on tuple categorization. Recall that in imperfect matches the tuples have the same values for the identifier, and at least one of the tuples has inaccurate nonidentifier attribute values. When a tuple $t _ { 1 }$ in $S _ { 1 }$ is accurate (i.e., $t _ { 1 } \in S _ { \mathrm { 1 A } } )$ and matches an inaccurate tuple in $S _ { 2 }$ (i.e., $t _ { 2 } \in S _ { \mathrm { 2 I } } )$ , then it appears in R when it should not and thus becomes a mismember in $R ;$ had all the attribute values for $t _ { 2 }$ been correctly recorded, then $t _ { 1 }$ would not have appeared in R. Similarly, when $t _ { 1 } \in S _ { \mathrm { 1 I } }$ imperfectly matches $t _ { 2 } \in \{ S _ { 2 \mathrm { A } }$ or $S _ { 2 \mathrm { I } } \} , ~ t _ { 1 }$ shows up as a mismember in R.

Interestingly, if an accurate (inaccurate) tuple in $S _ { 1 }$ imperfectly matches a mismember tuple in $S _ { 2 } ,$ it appears in R as accurate (inaccurate). When an inaccurate tuple in $S _ { 1 }$ imperfectly matches a tuple in $S _ { 2 C } ,$ it appears in R as a mismember. A mismember tuple in $S _ { 1 }$ that imperfectly matches an accurate or inaccurate tuple in $S _ { 2 }$ also appears in R as a mismember. Figure 8 summarizes the categorizations for tuples involved in imperfect matches. Note that the blank cells correspond to perfect matches already summarized in Figure 7.

Figure 7 Tuple Categorization in R for Perfect Matches Between S<sub>1</sub> and S<sub>2</sub>

<table><tr><td> $R = S_1 - S_2$ </td><td> $t_2 \in S_{2A}$ </td><td> $t_2 \in \hat{S}_{2M}$ </td><td> $t_2 \in S_{2C}$ </td></tr><tr><td> $t_1 \in S_{1A}$ </td><td> $t_1 \notin R$  $t_1 \notin R_C$ (e.g., C1)</td><td> $t_1 \in R_C$ (e.g., C3)</td><td> $t_1 \in R_M$ (e.g., C5)</td></tr><tr><td> $t_1 \in \hat{S}_{1M}$ </td><td> $t_1 \notin R$  $t_1 \notin R_C$ (e.g., C16)</td><td> $t_1 \notin R$  $t_1 \notin R_C$ (e.g., C18)</td><td> $t_1 \in R_M$ (e.g., C20)</td></tr><tr><td> $t_1 \in S_{1C}$ </td><td> $t_1 \notin R_C$ (e.g., C11)</td><td> $t_1 \in R_C$ (e.g., C13)</td><td> $t_1 \notin R_C$ (e.g., C15)</td></tr></table>

Figure 8 Tuple Categorization in R for Imperfect Matches for the Difference Operation

<table><tr><td> $R = S_{1} - S_{2}$ </td><td> $t_{2} \in S_{2\text{A}}$ </td><td> $t_{2} \in S_{2\text{I}}$ </td><td> $t_{2} \in \hat{S}_{2\text{M}}$ </td><td> $t_{2} \in \tilde{S}_{2\text{M}}$ </td><td> $t_{2} \in S_{2\text{C}}$ </td></tr><tr><td> $t_{1} \in S_{1\text{A}}$ </td><td></td><td> $t_{1} \in R_{\text{M}}$ (e.g., C2)</td><td></td><td> $t_{1} \in R_{\text{A}}$ (e.g., C4)</td><td></td></tr><tr><td> $t_{1} \in S_{1\text{I}}$ </td><td> $t_{1} \in R_{\text{M}}$ (e.g., C6)</td><td> $t_{1} \in R_{\text{M}}$ (e.g., C7)</td><td> $t_{1} \in R_{\text{I}}$ (e.g., C8)</td><td> $t_{1} \in R_{\text{I}}$ (e.g., C9)</td><td> $t_{1} \in R_{\text{M}}$ (e.g., C10)</td></tr><tr><td> $t_{1} \in \hat{S}_{1\text{M}}$ </td><td></td><td> $t_{1} \in R_{\text{M}}$ (e.g., C17)</td><td></td><td> $t_{1} \in R_{\text{M}}$ (e.g., C19)</td><td></td></tr><tr><td> $t_{1} \in \tilde{S}_{1\text{M}}$ </td><td> $t_{1} \in R_{\text{M}}$ (e.g., C21)</td><td> $t_{1} \in R_{\text{M}}$ (e.g., C22)</td><td> $t_{1} \in R_{\text{M}}$ (e.g., C23)</td><td> $t_{1} \in R_{\text{M}}$ (e.g., C24)</td><td> $t_{1} \in R_{\text{M}}$ (e.g., C25)</td></tr><tr><td> $t_{1} \in S_{1\text{C}}$ </td><td></td><td> $t_{1} \notin R_{\text{C}}$ (e.g., C12)</td><td></td><td> $t_{1} \in R_{\text{C}}$ (e.g., C14)</td><td></td></tr></table>

Figure 9 Tuple Categorization in R for Perfect Matches for the Union Operation

## 3.2. Categorizations for the Union Operation

Tuple categorizations for the result of the Union operation are analyzed analogously. When a tuple $t _ { 1 } \in S _ { 1 }$ or $t _ { 1 } \in S _ { \mathrm { 1 C } }$ does not have a matching counterpart in either $S _ { 2 }$ or $S _ { 2 C }$ , its status remains unchanged in $R .$ The tuple status, however, can change if such matches do exist. Here, too, we need to consider perfect and imperfect matches. Unlike the Difference operation, the Union operation is symmetric and, therefore, the tuple categorizations are symmetric as well.

First, we consider perfect matches. When a tuple $t _ { 1 } \in S _ { \mathrm { 1 A } }$ perfectly matches a tuple in either $S _ { 2 }$ or $S _ { 2 C } ,$ it retains its accurate status in R. By symmetry, the same is true when $t _ { 2 } \in S _ { 2 \mathrm { A } }$ has a perfectly matching tuple in either $\hat { S } _ { 1 \mathrm { M } }$ or $S _ { \mathrm { 1 C } }$ . Interestingly, if a tuple in $\hat { S } _ { 1 \mathrm { M } }$ perfectly matches a tuple in $S _ { 2 C } ,$ its status becomes accurate in the result; the mismember in the first table compensates for the incomplete tuple in the second table, and becomes a legitimate member of the union. When both tuples in a matching pair are accurate, mismembers, or incompletes, then exactly one copy appears in R with its status unchanged. A summary of the analysis is presented in Figure 9.

When a tuple $t _ { 1 } \in S _ { \mathrm { 1 A } }$ imperfectly matches a tuple $t _ { 2 } \in \{ S _ { 2 \mathrm { I } } \cup \tilde { S } _ { 2 \mathrm { M } } \}$ , then $t _ { 1 }$ appears in R as accurate and

$$
R = S _ {1} \cup S _ {2}
$$

$$
t _ {2} \in S _ {\mathrm{2A}}
$$

$$
t _ {2} \in \widehat {S} _ {\mathrm{2M}}
$$

$$
t _ {2} \in S _ {2 C}
$$

$$
t _ {1} \in S _ {\mathrm{1A}}
$$

$$
t _ {1} \in R _ {\mathrm{A}}
$$

$$
t _ {1} \in R _ {\mathrm{A}}
$$

$$
t _ {1} \in R _ {\mathrm{A}}
$$

$$
t _ {2} \notin R \cup R _ {\mathrm{C}}
$$

$$
t _ {2} \notin R \cup R _ {\mathrm{C}}
$$

$$
(\mathrm{e.g.,C1})
$$

$$
t _ {2} \notin R _ {\mathrm{C}}
$$

$$
(\mathrm{e.g.,C3})
$$

$$
t _ {1} \in \widehat {S} _ {\mathrm{1M}}
$$

$$
t _ {1} \notin R \cup R _ {\mathrm{C}}
$$

$$
t _ {1} \in R _ {\mathrm{M}}
$$

$$
(\mathrm{e.g.,C5})
$$

$$
t _ {2} \in R _ {\mathrm{A}}
$$

$$
(\mathrm{e.g.,C16})
$$

$$
t _ {2} \notin R \cup R _ {\mathrm{C}}
$$

$$
t _ {1} \in R _ {\mathrm{A}}
$$

$$
(\mathrm{e.g.,C18})
$$

$$
t _ {1} \in S _ {\mathrm{1C}}
$$

$$
t _ {1} \notin R _ {\mathrm{C}}
$$

$$
t _ {2} \notin R _ {\mathrm{C}}
$$

$$
t _ {2} \in R _ {\mathrm{A}}
$$

$$
t _ {1} \notin R _ {\mathrm{C}}
$$

$$
(\mathrm{e.g.,C20})
$$

$$
t _ {2} \in R _ {\mathrm{A}}
$$

$$
t _ {1} \in R _ {\mathrm{C}}
$$

$$
(\mathrm{e.g.,C11})
$$

$$
(\mathrm{e.g.,C13})
$$

$$
t _ {2} \notin R _ {\mathrm{C}}
$$

$$
(\mathrm{e.g.,C15})
$$

Figure 10 Tuple Categorization in R for Imperfect Matches for the Union Operation

<table><tr><td> $R = S_1 \cup S_2$ </td><td> $t_2 \in S_{2A}$ </td><td> $t_2 \in S_{2I}$ </td><td> $t_2 \in \hat{S}_{2M}$ </td><td> $t_2 \in \tilde{S}_{2M}$ </td><td> $t_2 \in S_{2C}$ </td></tr><tr><td> $t_1 \in S_{1A}$ </td><td></td><td> $t_1 \in R_A$  $t_2 \in R_M$ (e.g., C2)</td><td></td><td> $t_1 \in R_A$  $t_2 \in R_M$ (e.g., C4)</td><td></td></tr><tr><td> $t_1 \in S_{1I}$ </td><td> $t_1 \in R_M$  $t_2 \in R_A$ (e.g., C6)</td><td> $t_1 \in R_I$  $t_2 \in R_M$ (e.g., C7)</td><td> $t_1 \in R_I$  $t_2 \in R_M$ (e.g., C8)</td><td> $t_1 \in R_I$  $t_2 \in R_M$ (e.g., C9)</td><td> $t_1 \in R_I$  $t_2 \notin R_C$ (e.g., C10)</td></tr><tr><td> $t_1 \in \hat{S}_{1M}$ </td><td></td><td> $t_1 \in R_M$  $t_2 \in R_I$ (e.g., C17)</td><td></td><td> $t_1 \in R_M$  $t_2 \in R_M$ (e.g., C19)</td><td></td></tr><tr><td> $t_1 \in \tilde{S}_{1M}$ </td><td> $t_1 \in R_M$  $t_2 \in R_A$ (e.g., C21)</td><td> $t_1 \in R_M$  $t_2 \in R_I$ (e.g., C22)</td><td> $t_1 \in R_M$  $t_2 \in R_M$ (e.g., C23)</td><td> $t_1 \in R_M$  $t_2 \in R_M$ (e.g., C24)</td><td> $t_1 \in R_I$  $t_2 \notin R_C$ (e.g., C25)</td></tr><tr><td> $t_1 \in S_{1C}$ </td><td></td><td> $t_1 \notin R_C$  $t_2 \in R_I$ (e.g., C12)</td><td></td><td> $t_1 \notin R_C$  $t_2 \in R_I$ (e.g., C14)</td><td></td></tr></table>

$t _ { 2 }$ becomes a mismember, since the presence of $t _ { 2 }$ in R is redundant. When a tuple $t _ { 1 } \in S _ { \mathrm { 1 I } }$ imperfectly matches a tuple $t _ { 2 } \in \{ S _ { 2 \mathrm { I } } \cup \hat { S } _ { 2 \mathrm { M } } \bar { \cup } \tilde { S } _ { 2 \mathrm { M } } \}$ , then $t _ { 1 }$ appears in R as inaccurate and $t _ { 2 }$ becomes a mismember.<sup>1</sup> However, if $t _ { 1 }$ in $S _ { \mathrm { 1 I } }$ imperfectly matches a tuple $t _ { 2 }$ in $S _ { 2 C }$ , then $t _ { 1 }$ appears in R as inaccurate but $t _ { 2 }$ is no longer part of $R _ { C } .$ . When $t _ { 1 } \in \{ \widehat { S } _ { \scriptscriptstyle { 1 \mathrm { M } } } \cup \widetilde { S } _ { \scriptscriptstyle { 1 \mathrm { M } } } \}$ imperfectly matches $t _ { 2 } \in \tilde { S } _ { 2 \mathrm { M } } .$ , both $t _ { 1 }$ and $t _ { 2 }$ are mismembers in R. When $t _ { 1 } \in \tilde { S } _ { \scriptscriptstyle { 1 \mathrm { M } } }$ imperfectly matches $t _ { 2 } \in S _ { 2 C } ,$ $t _ { 1 }$ becomes inaccurate in $R ;$ at the same time, $t _ { 2 }$ no longer appears in $R _ { C } .$ . The remaining tuple categorizations follow by symmetry, and are summarized in Figure 10.

<sup>1</sup> When $t _ { 1 } \in S _ { \mathrm { 1 I } }$ imperfectly matches $t _ { 2 } \in S _ { \mathrm { 2 I } } ,$ , we could classify either tuple as inaccurate in R, and the other one as a mismember in R. The analysis remains unchanged.

## 4. Estimating the Number of Matching Tuples

To determine the quality profiles for the results of the Difference and Union operations, we need to estimate the number of tuples that match between the tuple subsets of $S _ { 1 } \cup S _ { \mathrm { 1 C } }$ and $S _ { 2 } \cup S _ { 2 C }$ . As mentioned in $\ S 3 ,$ such matches could be perfect or imperfect. The following parameters are used in our analyses (how they are obtained has been discussed in $\ S \ S 2$ and 3):

(1) The quality metrics for the base relations $S _ { 1 }$ and $S _ { 2 }$ (denoted by $\alpha _ { i } , \beta _ { i } , \mu _ { i }$ , and $\chi _ { i } , i \in \{ 1 , 2 \} )$ .

(2) The cardinalities of the sets $S _ { 1 } , S _ { 2 } ,$ and $R .$ .

(3) The count of perfect and imperfect matches between $S _ { 1 }$ and $S _ { 2 } ,$ denoted by $\delta$ and $\delta ^ { \prime } ,$ , respectively. We denote the sets of such tuples by $S _ { \delta }$ and $S _ { \delta ^ { \prime } }$ .

We need to estimate the components of $\delta$ and $\delta ^ { \prime }$ that appear in the various subsets of the two tables. In addition, we also need to estimate the number of unobserved potential perfect matches and potential imperfect matches. The total number of potential perfect matches, which includes those between $S _ { 1 }$ and $S _ { 2 C } ,$ between $S _ { 2 }$ and $S _ { \mathrm { 1 C } } ,$ and between $S _ { \mathrm { 1 C } }$ and $S _ { 2 C }$ is denoted by $\eta .$ The total number of potential imperfect matches (which can occur between $S _ { 1 }$ and $S _ { 2 C }$ and between $S _ { 2 }$ and $S _ { \mathrm { 1 C } } )$ is denoted by $\eta ^ { \prime } .$ Since $\eta$ and $\eta ^ { \prime }$ are not directly observable, we estimate them before determining how they are distributed across the various components of $S _ { 1 }$ and $S _ { 2 }$

For notational convenience, we denote the number of observed matching tuples between any two subsets $S _ { 1 i }$ and $S _ { 2 j }$ by $\delta _ { i j }$ or $\delta _ { i j } ^ { \prime } , i , j \in \{ \mathrm { A } , \mathrm { I } , \widehat { \mathrm { M } } , \widetilde { \mathrm { M } } \}$ , depending on whether they are part of $\delta$ or $\delta ^ { \prime }$ , respectively. Similarly, the components of potential matches $\eta$ and $\eta ^ { \prime }$ are denoted by $\eta _ { i j }$ and $\eta _ { i j } ^ { \prime }$ . For example, the number of matching tuples between $S _ { \mathrm { 1 A } }$ and $S _ { 2 \mathrm { A } }$ is denoted by $\delta _ { \mathrm { A A } } ,$ while that between $S _ { \mathrm { 1 A } }$ and $S _ { 2 \mathrm { I } }$ is denoted by $\delta _ { \mathrm { A I } } ^ { \prime }$ . The number of potential matches between $S _ { \mathrm { 1 A } }$ and $S _ { 2 C }$ is denoted by $\eta _ { \mathrm { A C } } ,$ while that between $S _ { \mathrm { 1 I } }$ and $S _ { 2 C }$ is denoted by $\eta _ { \mathrm { I C } } ^ { \prime }$

The fully matching tuple subsets (including both the observed and the potential ones) are shown in Figure 11. Shaded areas refer to tuples that do not have a match. The imperfectly matching tuple subsets are shown in Figure 12.

Figure 11 Components of  and   
![](/api/attachments/WUZKVXN9/fulltext/images/0cf33dd99b636c707e5aeeca8266989f9a12d3f2ea4efbcaef9e14b1811bf5cf.jpg)

Figure 12 Components of  and $\eta ^ { \prime }$  
![](/api/attachments/WUZKVXN9/fulltext/images/aed07dfde01d417454d742463362bbeaaaa58ff2bef9cea2ded46b760523eead.jpg)

From Figures 11 and 12, it is easy to see the following identities:

$$
\begin{array}{r l r} & & {\delta = \delta_ {\mathrm{AA}} + \delta_ {\mathrm{AM}} + \delta_ {\mathrm{MA}} + \delta_ {\mathrm{MM}},} \\ & & {\delta^ {\prime} = \delta_ {\mathrm{IA}} ^ {\prime} + \delta_ {\mathrm{AI}} ^ {\prime} + \delta_ {\mathrm{II}} ^ {\prime} + \delta_ {\mathrm{AM}} ^ {\prime} + \delta_ {\mathrm{MA}} ^ {\prime} + \delta_ {\mathrm{IM}} ^ {\prime} + \delta_ {\mathrm{MI}} ^ {\prime}} \\ & & {+ \delta_ {\mathrm{IM}} ^ {\prime} + \delta_ {\mathrm{MI}} ^ {\prime} + \delta_ {\mathrm{MM}} ^ {\prime} + \delta_ {\mathrm{MM}} ^ {\prime} + \delta_ {\mathrm{MM}} ^ {\prime},} \\ & & {\eta = \eta_ {\mathrm{AC}} + \eta_ {\mathrm{CA}} + \eta_ {\mathrm{MC}} + \eta_ {\mathrm{CM}} + \eta_ {\mathrm{CC}}, \quad \mathrm{and}} \\ & & {\eta^ {\prime} = \eta_ {\mathrm{IC}} ^ {\prime} + \eta_ {\mathrm{CI}} ^ {\prime} + \eta_ {\mathrm{MC}} ^ {\prime} + \eta_ {\mathrm{CM}} ^ {\prime}.} \end{array}
$$

To determine the quality profile for the result $R ,$ we need to estimate the sizes of its accurate, inaccurate, mismember, and incomplete sets $( \mathrm { i . e . , }$ the quantities $| R _ { \mathrm { A } } | , | R _ { \mathrm { I } } | , | R _ { \mathrm { M } } | .$ , and $| R _ { \mathrm { C } } | )$ . For the Difference operation, they are derived as follows:

$$
| R _ {\mathrm{A}} | = | S _ {1 \mathrm{A}} | - \delta_ {\mathrm{AA}} - \delta_ {\mathrm{AM}} - \delta_ {\mathrm{AI}} ^ {\prime} - \eta_ {\mathrm{AC}},\tag{1}
$$

$$
| R _ {\mathrm{I}} | = | S _ {\mathrm{II}} | - \delta_ {\mathrm{IA}} ^ {\prime} - \delta_ {\mathrm{II}} ^ {\prime} - \eta_ {\mathrm{IC}} ^ {\prime},\tag{2}
$$

$$
| R _ {\mathrm{M}} | = | S _ {\mathrm{1M}} | - \delta_ {\widehat {\mathrm{MA}}} - \delta_ {\widehat {\mathrm{MM}}} + \delta_ {\mathrm{AI}} ^ {\prime}
$$

$$
+ \delta_ {\mathrm{IA}} ^ {\prime} + \delta_ {\mathrm{II}} ^ {\prime} + \eta_ {\mathrm{AC}} + \eta_ {\mathrm{IC}} ^ {\prime}, \quad \text { and }\tag{3}
$$

$$
| R _ {\mathrm{C}} | = | S _ {1 \mathrm{C}} | + \delta_ {\mathrm{AM}} - \eta_ {\mathrm{CA}} - \eta_ {\mathrm{CC}} - \eta_ {\mathrm{CI}} ^ {\prime}.\tag{4}
$$

In estimating $| R _ { \mathrm { A } } |$ , Equation (1) accounts for the following occurrences. Tuples in $S _ { \mathrm { 1 A } }$ that perfectly match tuples in $S _ { 2 \mathrm { A } }$ or $\hat { S } _ { 2 \bf M }$ will be eliminated as a result of the difference operation $( \delta _ { \mathrm { A A } }$ and $\delta _ { \mathrm { A } \widehat { \mathrm { M } } } .$ , respectively). Tuples in $S _ { \mathrm { 1 A } }$ that imperfectly match tuples in $S _ { 2 \mathrm { I } }$ will remain in the result, but as mismembers $( \mathrm { i . e . , ~ } \delta _ { \mathrm { A I } } ^ { \prime } )$ On the other hand, tuples in $S _ { \mathrm { 1 A } }$ that imperfectly match tuples in $\tilde { S } _ { 2 \mathrm { M } }$ continue to remain as accurate in the result; therefore, no adjustments are needed stemming from such matches. Finally, we account for those tuples that would have found a match in $S _ { 2 C }$ $( \mathrm { i . e . } , \ \eta _ { \mathrm { A C } } )$ . Expressions for $| R _ { \mathrm { I } } | , \ | R _ { \mathrm { M } } | ,$ and $| R _ { C } |$ are obtained in an analogous manner.

Similarly, for the Union operation, we have

$$
| R _ {\mathrm{A}} | = | S _ {\mathrm{1A}} | + | S _ {\mathrm{2A}} | - \delta_ {\mathrm{AA}} + \eta_ {\widehat {\mathrm{MC}}} + \eta_ {\mathrm{C} \widehat {\mathrm{M}}},\tag{5}
$$

$$
| R _ {\mathrm{I}} | = | S _ {\mathrm{1I}} | + | S _ {\mathrm{2I}} | - \delta_ {\mathrm{AI}} ^ {\prime} - \delta_ {\mathrm{IA}} ^ {\prime} - \delta_ {\mathrm{II}} ^ {\prime} + \eta_ {\widetilde {\mathrm{MC}}} ^ {\prime} + \eta_ {\mathrm{CM}} ^ {\prime},\tag{6}
$$

$$
| R _ {\mathrm{M}} | = | S _ {\mathrm{1M}} | + | S _ {\mathrm{2M}} | - \delta_ {\mathrm{A} \widehat {\mathrm{M}}} - \delta_ {\widehat {\mathrm{M}} \mathrm{A}} - \delta_ {\widehat {\mathrm{M}} \widehat {\mathrm{M}}} + \delta_ {\mathrm{AI}} ^ {\prime} + \delta_ {\mathrm{IA}} ^ {\prime}
$$

$$
+ \delta_ {\mathrm{II}} ^ {\prime} - \eta_ {\widehat {\mathrm{MC}}} - \eta_ {\mathrm{CM}} - \eta_ {\widetilde {\mathrm{MC}}} ^ {\prime} - \eta_ {\mathrm{CM}} ^ {\prime}, \quad \text { and }\tag{7}
$$

$$
\begin{array}{c} | R _ {\mathrm{C}} | = | S _ {1 \mathrm{C}} | + | S _ {2 \mathrm{C}} | - \eta_ {\mathrm{AC}} - \eta_ {\mathrm{CA}} - \eta_ {\widehat {\mathrm{MC}}} - \eta_ {\mathrm{CM}} \\ - \eta_ {\mathrm{CC}} - \eta_ {\mathrm{IC}} ^ {\prime} - \eta_ {\mathrm{CI}} ^ {\prime} - \eta_ {\widetilde {\mathrm{MC}}} ^ {\prime} - \eta_ {\mathrm{CM}} ^ {\prime}. \end{array}\tag{8}
$$

We show in §4.1 how the size of the components of  and $\delta ^ { \prime }$ can be estimated, followed by estimation procedures for the components of  and $\eta ^ { \prime }$ in §4.2.

## 4.1. Components of Perfect Matches  and Imperfect Matches 

Estimating the sizes of the components of  and $\delta ^ { \prime }$ is complicated by the fact that different subsets of each table have potential matches with different collections of subsets of the other table. This is important, as it leads to different likelihoods of matches for tuples across different subsets. For example, if a tuple in $S _ { \mathrm { 1 A } }$ perfectly matches a tuple in $S _ { 2 \mathrm { A } }$ it contributes to $\delta _ { \mathrm { A A } } ,$ which is a part of . On the other hand, if a tuple in $S _ { \mathrm { 1 A } }$ imperfectly matches a tuple in $S _ { 2 \mathrm { I } }$ it contributes to $\delta _ { \mathrm { A I } } ^ { \prime } ,$ which is a part of . Since the values of  and $\delta ^ { \prime }$ could be very different, the likelihood of a tuple in $S _ { \mathrm { 1 A } }$ being part of $\delta _ { \mathrm { A A } }$ could be quite different from its likelihood of being part of $\delta _ { \mathrm { A I } } ^ { \prime }$ . We show how the overall problem of estimating the various components can be solved by decomposing the larger problem into several simpler subproblems.

4.1.1. Decomposing Imperfect Matches. In the decomposition approach, we view the imperfectly matching tuples in $S _ { \delta ^ { \prime } }$ as comprising of three parts characterized as follows: (i) the matching tuple from $S _ { 1 }$ has accurate nonkey attribute values while the tuple from $S _ { 2 }$ has some inaccurate nonkey attribute value(s) (this part is denoted by $\delta _ { 1 } ^ { \prime } ) ;$ ; (ii) the matching tuple from $S _ { 1 }$ has some inaccurate nonkey attribute value(s) while the tuple from $S _ { 2 }$ has accurate nonkey attribute values (denoted by $\delta _ { 2 } ^ { \prime } ) ;$ and (iii) the matching tuples from both $S _ { 1 }$ and $S _ { 2 }$ have inaccurate nonkey attribute values (denoted by  ). Clearly, $\delta ^ { \prime } = \delta _ { 1 } ^ { \prime } + \delta _ { 2 } ^ { \prime } + \delta _ { 3 } ^ { \prime } ,$ , where

$$
\begin{array}{r} \delta_ {1} ^ {\prime} = \delta_ {\mathrm{AI}} ^ {\prime} + \delta_ {\widetilde {\mathrm{AM}}} ^ {\prime} + \delta_ {\widetilde {\mathrm{MI}}} ^ {\prime} + \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime}, \\ \delta_ {2} ^ {\prime} = \delta_ {\mathrm{IA}} ^ {\prime} + \delta_ {\widetilde {\mathrm{MA}}} ^ {\prime} + \delta_ {\mathrm{IM}} ^ {\prime} + \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime}, \quad \text {and} \\ \delta_ {3} ^ {\prime} = \delta_ {\mathrm{II}} ^ {\prime} + \delta_ {\mathrm{IM}} ^ {\prime} + \delta_ {\widetilde {\mathrm{MI}}} ^ {\prime} + \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime}. \end{array}
$$

Figure 13 illustrates  and the three parts of $\delta ^ { \prime }$ across the two relations. Before we estimate sizes of the finer components of $\delta ^ { \prime }$ , we estimate the sizes of $\delta _ { 1 } ^ { \prime } ,$ $\delta _ { 2 } ^ { \prime } ,$ and $\delta _ { 3 } ^ { \prime }$ . We use the following notation to simplify our discussion: $V _ { 1 } = \{ S _ { \mathrm { 1 A } } \cup \hat { S } _ { \mathrm { 1 M } } \} - S _ { \delta } ; ~ V _ { 2 } = S _ { \mathrm { 1 I } } \cup \tilde { S } _ { \mathrm { 1 M } } ;$ $V _ { 3 } = \{ S _ { 2 \mathrm { A } } \cup \hat { S } _ { 2 \mathrm { M } } \} - S _ { \delta } ;$ and $V _ { 4 } = S _ { 2 \mathrm { I } } \cup \tilde { S } _ { 2 \mathrm { M } }$ We know that  tuples in $S _ { \mathrm { 1 A } } \cup \hat { S } _ { \mathrm { 1 M } }$ have matches in $S _ { 2 \mathrm { A } } \cup \hat { S } _ { 2 \mathrm { M } }$ . Tuples in $S _ { 1 } - S _ { \delta }$ (i.e., $V _ { 1 } \cup V _ { 2 } )$ that match

Figure 13 ,  ,  , and $\delta _ { 3 } ^ { \prime }$ Across $S _ { \uparrow }$ and $S _ { 2 }$

![](/api/attachments/WUZKVXN9/fulltext/images/21a4f72be405eac1827602507e192a2898f6b709ee7c7a5d99121e9da14b4ffc.jpg)

tuples in $S _ { 2 } - S _ { \delta } ~ ( \mathrm { i . e . , } ~ V _ { 3 } \cup V _ { 4 } )$ belong to $\delta ^ { \prime } .$ . Let $\delta _ { 1 3 } ^ { \prime } =$ $\delta _ { 1 } ^ { \prime } + \delta _ { 3 } ^ { \prime }$ be the number of tuples from $S _ { \delta ^ { \prime } }$ that belong to $V _ { 4 }$ and let $\delta _ { 2 3 } ^ { \prime } = \delta _ { 2 } ^ { \prime } + \delta _ { 3 } ^ { \prime }$ be the number of tuples from $S _ { \delta ^ { \prime } }$ that belong to $V _ { 2 } \mathrm { ~  ~ { ~ \left( S _ { \delta _ { 1 3 } ^ { \prime } } \right. } ~ }$ and $S _ { \delta _ { 7 3 } ^ { \prime } }$ denote the <sub>13</sub> corresponding sets of tuples). By definition,  tuples from $S _ { 1 } - V _ { 2 }$ match $S _ { 2 } - V _ { 4 }$ and $\delta _ { 1 } ^ { \prime }$ tuples from $S _ { 1 } - V _ { 2 }$ match $V _ { 4 } ;$ therefore, a tuple in $S _ { \delta _ { 2 3 } ^ { \prime } }$ could match a tuple either in $V _ { 3 }$ or in $V _ { 4 } - S _ { \delta _ { 1 } ^ { \prime } }$ . Matches occur on the identifying attributes, and thus such a tuple in $S _ { \delta _ { 2 3 } ^ { \prime } }$ is equally likely to match a specific tuple in $V _ { 3 }$ as it is to match a tuple in $V _ { 4 } - S _ { \delta _ { 1 } ^ { \prime } }$ . Consequently, the set $V _ { 3 }$ can be viewed as being constructed from $\{ V _ { 3 } \cup V _ { 4 } \} - S _ { \delta _ { 1 } ^ { \prime } }$ by drawing $\delta _ { 2 } ^ { \prime }$ tuples from $\delta _ { 2 3 } ^ { \prime } ,$ and $\left| V _ { 3 } \right| - \delta _ { 2 } ^ { \prime }$ from $\{ V _ { 3 } \cup V _ { 4 } \} - S _ { \delta ^ { \prime } }$ . Then, the probability that $\delta _ { 2 } ^ { \prime } = c$ follows the hypergeometric distribution and is given by

$$
P (\delta_ {2} ^ {\prime} = c) = \frac {\binom{\delta_ {2 3} ^ {\prime}}{c} \cdot \binom{| V _ {3} | + | V _ {4} | - \delta^ {\prime}}{| V _ {3} | - c}}{\binom{| V _ {3} | + | V _ {4} | - \delta_ {1} ^ {\prime}}{| V _ {3} |}}.
$$

The expected value for $\delta _ { 2 } ^ { \prime }$ is given by

$$
E (\delta_ {2} ^ {\prime}) = \frac {\delta_ {2 3} ^ {\prime} | V _ {3} |}{| V _ {3} | + | V _ {4} | - \delta_ {1} ^ {\prime}}.
$$

Similarly, the set $V _ { 1 }$ can be constructed from $\{ V _ { 1 } \cup V _ { 2 } \} - S _ { \delta _ { 2 } ^ { \prime } }$ , and the expected value for $\delta _ { 1 } ^ { \prime }$ is

$$
E (\delta_ {1} ^ {\prime}) = \frac {\delta_ {1 3} ^ {\prime} | V _ {1} |}{| V _ {1} | + | V _ {2} | - \delta_ {2} ^ {\prime}}.
$$

Since $\delta _ { 2 3 } ^ { \prime } = \delta - \delta _ { 1 } ^ { \prime }$ and $\delta _ { 1 3 } ^ { \prime } = \delta - \delta _ { 2 } ^ { \prime } ,$ the estimate for $\delta _ { 1 } ^ { \prime }$ depends on the value for $\delta _ { 2 } ^ { \prime } ,$ , and vice versa. Thus, we have two equations in two unknown variables, as shown below:

$$
E (\delta_ {2} ^ {\prime}) = \frac {(\delta^ {\prime} - E (\delta_ {1} ^ {\prime})) | V _ {3} |}{| V _ {3} | + | V _ {4} | - E (\delta_ {1} ^ {\prime})}, \quad \text { and }\tag{9}
$$

$$
E (\delta_ {1} ^ {\prime}) = \frac {(\delta^ {\prime} - E (\delta_ {2} ^ {\prime})) | V _ {1} |}{| V _ {1} | + | V _ {2} | - E (\delta_ {2} ^ {\prime})}.\tag{10}
$$

Algebraically manipulating Equations (9) and (10), we obtain the following quadratic equation in $E ( \delta _ { 1 } ^ { \prime } )$

$$
\begin{array}{c} (| V _ {3} | - | V _ {1} | - | V _ {2} |) (E (\delta_ {1} ^ {\prime})) ^ {2} + \big (\delta^ {\prime} (| V _ {1} | - | V _ {3} |) + | V _ {1} | \cdot | V _ {4} | \\ + | V _ {2} | (| V _ {3} | + | V _ {4} |) \big) E (\delta_ {1} ^ {\prime}) - (\delta^ {\prime} | V _ {1} | \cdot | V _ {4} |) = 0. \end{array}
$$

Solving this quadratic equation gives two solutions for $E ( \delta _ { 1 } ^ { \prime } )$ , both of which are positive. In most cases, one of the solutions is infeasible, either because it is negative or it exceeds $\delta ^ { \prime }$ . When both solutions are feasible, we select the one with the higher likelihood (Feller 1968, p. 46). $E ( \delta _ { 2 } ^ { \prime } )$ is then obtained using Equation (9), and $E ( \delta _ { 3 } ^ { \prime } ) = \delta ^ { \prime } - E ( \delta _ { 1 } ^ { \prime } ) - E ( \delta _ { 2 } ^ { \prime } )$ .

4.1.2. Estimating the Sizes of the Components of $\delta , \delta _ { 1 } ^ { \prime } , \delta _ { 2 } ^ { \prime } ,$ and $\delta _ { 3 } ^ { \prime } .$ . We consider next how tuples in $S _ { \delta }$ and in $S _ { \delta _ { 1 } ^ { \prime } }$ are expected to be distributed in $S _ { 1 }$ . Tuples in $S _ { \delta }$ and $S _ { \delta _ { 1 } ^ { \prime } }$ appear only in the subsets $S _ { \mathrm { 1 A } }$ and $\hat { S } _ { 1 \mathrm { M } }$ and not in $S _ { \mathrm { 1 I } }$ or ${ \tilde { S } } _ { 1 \mathrm { M } } ,$ and none of the remaining tuples that contribute to $\delta ^ { \prime }$ appear in $S _ { \mathrm { 1 A } }$ and $\hat { S } _ { 1 \mathrm { M } }$ . The complete set of matches across $S _ { \mathrm { 1 A } } \cup \widehat { S } _ { \mathrm { 1 M } }$ and $S _ { 2 }$ are shown in Figure 14.

$S _ { \mathrm { 1 A } }$ can be constructed by drawing $| S _ { \mathrm { 1 A } } |$ tuples from $S _ { \mathrm { 1 A } } \cup \hat { S } _ { \mathrm { 1 M } }$ as shown in Figure 15; the remaining tuples naturally constitute $\hat { S } _ { 1 \mathrm { M } } .$ . Let x be the number of tuples from $S _ { \delta }$ that are part of $S _ { \mathrm { 1 A } } ~ ( \mathrm { i . e . , } ~ x = \delta _ { \mathrm { A A } } + \delta _ { \mathrm { A \widehat { M } } } )$ , and let z be the number of tuples from $S _ { \delta _ { 1 } ^ { \prime } }$ that are part

Figure 14 Matches Across $S _ { 1 \mathsf { A } } \cup \hat { S } _ { 1 \mathsf { M } }$ and $S _ { 2 }$

![](/api/attachments/WUZKVXN9/fulltext/images/a0b8a6460abfbd24e0eeee4c7ab3b3835535f76f7f822e712d26fe61270a4d45.jpg)

of $S _ { 1 \mathrm { A } } ~ ( \mathrm { i . e . , } ~ z = \delta _ { \mathrm { A I } } ^ { \prime } + \delta _ { \mathrm { A \widetilde { M } } } ^ { \prime } )$ . Then, the probability distribution function of x and $z$ follows a multivariate hypergeometric distribution, i.e.,

$$
\begin{array}{l} P (\delta_ {\mathrm{AA}} + \delta_ {\mathrm{AM}} = x;   \delta_ {\mathrm{AI}} ^ {\prime} + \delta_ {\mathrm{AM}} ^ {\prime} = z) \\ = \frac {\binom{\delta}{x} \cdot \binom{\delta_ {1} ^ {\prime}}{z} \cdot \binom{| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} | - \delta - \delta_ {1} ^ {\prime}}{| S _ {1 \mathrm{A}} | - x - z}}{\binom{| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |}{| S _ {1 \mathrm{A}} |}}. \end{array}
$$

The expected values for x and z are given by (Johnson et al. 1993, p. 238)

$$
\begin{array}{c} E (x) = E (\delta_ {\mathrm{AA}} + \delta_ {\mathrm{AM}}) = \delta \cdot | S _ {1 \mathrm{A}} | / (| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |), \quad \text {and} \\ E (z) = E (\delta_ {\mathrm{AI}} ^ {\prime} + \delta_ {\mathrm{AM}} ^ {\prime}) = \delta_ {1} ^ {\prime} \cdot | S _ {1 \mathrm{A}} | / (| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |). \end{array}
$$

Now consider the components of $x ,$ namely $\delta _ { \mathrm { A A } }$ and $\delta _ { \mathrm { A \widehat { M } } }$ . To estimate their sizes, we construct $S _ { 2 \mathrm { A } }$ from $S _ { 2 \mathrm { A } } \cup \hat { S } _ { 2 \mathrm { M } }$ by drawing $y ~ ( = \delta _ { \mathrm { A A } } )$ tuples from the set $S _ { x }$ $( \mathrm { i . e . , }$ the set of $x$ tuples in $\delta ) _ { \cdot }$ , w $( = \delta _ { \widehat { \mathrm { M A } } } )$ tuples from the set $S _ { \delta } - S _ { x } ,$ and the remaining $| S _ { 2 \mathrm { A } } | - y - w$ tuples from $\{ \{ S _ { 2 \mathrm { A } } \cup \widehat { S } _ { 2 \mathrm { M } } \} - S _ { \delta } \} - S _ { x }$ , as shown in Figure 16. The joint probability distribution function for y and w given x follows a multivariate hypergeometric distribution given by

$$
\begin{array}{l} P (\delta_ {\mathrm{AA}} = y, \delta_ {\widehat {\mathrm{MA}}} = w \mid x) \\ = \frac {\binom {x} {y} \cdot \binom {\delta - x} {w} \cdot \binom {| S _ {2 \mathrm{A}} | + | \widehat {S} _ {2 \mathrm{M}} | - \delta} {| S _ {2 \mathrm{A}} | - y - w}}{\binom {| S _ {2 \mathrm{A}} | + | \widehat {S} _ {2 \mathrm{M}} |} {| S _ {2 \mathrm{A}} |}}. \end{array}
$$

Figure 15 Construction of $S _ { 1 A }$

![](/api/attachments/WUZKVXN9/fulltext/images/39790150d0a5c3a5cbc72a5452866956ca6178a09aafc95bc621bb110d38faf8.jpg)

Figure 16 Construction of $S _ { 2 \mathsf { A } }$  
![](/api/attachments/WUZKVXN9/fulltext/images/5a1ee99cabbcacd7b79528bca2a578a60f0b36c6415a27e75cbd4af3ea5b6196.jpg)

The expected values of $y$ and w are as follows:

$$
\begin{array}{l} E (y) = E (\delta_ {\mathrm{AA}}) = \frac {E (x) \cdot | S _ {2 \mathrm{A}} |}{(| S _ {2 \mathrm{A}} | + | \hat {S} _ {2 \mathrm{M}} |)} \\ \qquad = \frac {\delta \cdot | S _ {1 \mathrm{A}} | \cdot | S _ {2 \mathrm{A}} |}{(| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |) (| S _ {2 \mathrm{A}} | + | \hat {S} _ {2 \mathrm{M}} |)}, \quad \text {and} \\ E (w) = E (\delta_ {\widehat {\mathrm{MA}}}) = \frac {(\delta - E (x)) \cdot | S _ {2 \mathrm{A}} |}{| S _ {2 \mathrm{A}} | + | \hat {S} _ {2 \mathrm{M}} |} \\ \qquad = \frac {\delta \cdot | \hat {S} _ {1 \mathrm{M}} | \cdot | S _ {2 \mathrm{A}} |}{(| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |) (| S _ {2 \mathrm{A}} | + | \hat {S} _ {2 \mathrm{M}} |)}. \end{array}
$$

Similarly, we have

$$
\begin{array}{c} E (\delta_ {\mathrm{AM}}) = \frac {\delta \cdot | S _ {1 \mathrm{A}} | \cdot | \hat {S} _ {2 \mathrm{M}} |}{(| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |) (| S _ {2 \mathrm{A}} | + | \hat {S} _ {2 \mathrm{M}} |)}, \quad \text {and} \\ E (\delta_ {\hat {\mathrm{MM}}}) = \frac {\delta \cdot | \hat {S} _ {1 \mathrm{M}} | \cdot | \hat {S} _ {2 \mathrm{M}} |}{(| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |) (| S _ {2 \mathrm{A}} | + | \hat {S} _ {2 \mathrm{M}} |)}. \end{array}
$$

The sizes of the individual components of $\delta _ { 1 } ^ { \prime }$ are estimated by using z in a manner similar to how x was used for estimating the sizes of the components of $\delta .$

To estimate the sizes of the components of $\delta _ { 2 } ^ { \prime }$ and $\delta _ { 3 } ^ { \prime } ,$ we observe that $S _ { \delta _ { 2 } ^ { \prime } }$ and $S _ { \delta _ { 3 } ^ { \prime } }$ appear only in the subsets $S _ { \mathrm { 1 I } }$ and ${ \tilde { S } } _ { 1 \mathrm { M } } ,$ , and not in $S _ { \mathrm { 1 A } }$ or $\hat { S } _ { 1 \mathrm { M } } .$ . Therefore, the complete set of matches across $S _ { \mathrm { 1 I } } \cup \tilde { S } _ { \mathrm { 1 M } }$ and $S _ { 2 }$ are as shown in Figure 17. This construction is identical to that obtained in Figure 14 when determining the sizes of the components of $\delta$ and $\delta _ { 1 } ^ { \prime }$ . Consequently, a procedure analogous to the one described earlier enables us to estimate the sizes of the various components of $\delta _ { 2 } ^ { \prime }$ and $\delta _ { 3 } ^ { \prime }$

The derivations for the estimated sizes of the components of $\delta ^ { \prime }$ are analogous to that for the components of . The sizes of the components of $\delta ^ { \prime }$ are summarized in Figure 18.

## 4.2. Components of Potential Perfect and Imperfect Matches ( and )

We must first estimate the sizes of $\eta$ and $\eta ^ { \prime }$ before we estimate the sizes of their components. The size $\eta + \eta ^ { \prime }$ corresponds to the total number of unobserved potential matches, while $\delta { + } \delta ^ { \prime }$ corresponds to the total number of observed matches. We denote the total number of potential matches (observed plus unobserved) by ; i.e., $\Delta = \delta + \delta ^ { \prime } + \eta + \eta ^ { \prime }$ . To facilitate our analysis, we denote the total number of unobserved perfectly matching and imperfectly matching tuples between $S _ { 1 }$ and $S _ { 2 C }$ by $\eta _ { 1 2 } ,$ and the total number of unobserved perfectly matching and imperfectly matching tuples between $S _ { 2 }$ and $S _ { \mathrm { 1 C } }$ by $\eta _ { 2 1 }$ . As noted earlier, the number of unobserved potential matches between $S _ { \mathrm { 1 C } }$ and $S _ { 2 C }$ is denoted by $\eta _ { \scriptscriptstyle \mathrm { C C } }$ . It follows that $\eta + \eta ^ { \prime } = \eta _ { 1 2 } + \eta _ { 2 1 } + \eta _ { \mathrm { C C } } .$ , and therefore $\Delta = \delta + \delta ^ { \prime } + \eta _ { 1 2 } +$ $\eta _ { 2 1 } + \eta _ { \mathrm { C C } }$ . Figure 19 illustrates the observed and unobserved overlapping entity instances between $S _ { 1 } \cup S _ { \mathrm { 1 C } }$ and $S _ { 2 } \cup S _ { 2 C }$

Interestingly, the problem of estimating the size of $\Delta$ is related to the well-known problem of estimating the population of fish from recapture data (Feller 1968,

Figure 17 Tuple Subsets for Estimation of $\delta _ { 2 } ^ { \prime }$ and $\delta _ { 3 } ^ { \prime }$ Components  
![](/api/attachments/WUZKVXN9/fulltext/images/9e2b034e446f8bbaf7b7387cc410b18edccf2f72b98606a87625c0a8183be396.jpg)

Figure 18 Components of $\delta _ { 1 } ^ { \prime } , \delta _ { 2 } ^ { \prime }$ , and $\delta _ { 3 } ^ { \prime }$

$$
E (\delta_ {\mathrm{AI}} ^ {\prime}) = \frac {| S _ {\mathrm{1A}} | \cdot | S _ {\mathrm{2I}} |}{(| S _ {\mathrm{1A}} | + | \hat {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \tilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {\mathrm{1}} ^ {\prime}
$$

$$
E (\delta_ {\mathrm{AM}} ^ {\prime}) = \frac {| S _ {1 \mathrm{A}} | \cdot | \tilde {S} _ {2 \mathrm{M}} |}{(| S _ {1 \mathrm{A}} | + | \hat {S} _ {1 \mathrm{M}} |) (| S _ {2 \mathrm{I}} | + | \tilde {S} _ {2 \mathrm{M}} |)} \cdot \delta_ {1} ^ {\prime}
$$

$$
E (\delta_ {\widehat {\mathrm{MI}}} ^ {\prime}) = \frac {| \widehat {S} _ {\mathrm{1M}} | \cdot | S _ {\mathrm{2I}} |}{(| S _ {\mathrm{1A}} | + | \widehat {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \widetilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {\mathrm{1}} ^ {\prime}
$$

$$
E (\delta_ {\widehat {\mathrm{M}} \widetilde {\mathrm{M}}} ^ {\prime}) = \frac {| \widehat {S} _ {\mathrm{1M}} | \cdot | \widetilde {S} _ {\mathrm{2M}} |}{(| S _ {\mathrm{1A}} | + | \widehat {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \widetilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {1} ^ {\prime}
$$

$$
E (\delta_ {\mathrm{IA}} ^ {\prime}) = \frac {| S _ {\mathrm{1I}} | \cdot | S _ {\mathrm{2A}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2A}} | + | \hat {S} _ {\mathrm{2M}} |)} \cdot \delta_ {2} ^ {\prime}
$$

$$
E (\delta_ {\mathrm{IM}} ^ {\prime}) = \frac {| S _ {\mathrm{1I}} | \cdot | \hat {S} _ {\mathrm{2M}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2A}} | + | \hat {S} _ {\mathrm{2M}} |)} \cdot \delta_ {2} ^ {\prime}
$$

p. 45). The tuples that appear in $S _ { 1 }$ and $S _ { 2 }$ can be viewed as random draws from $S _ { 1 } \cup S _ { \mathrm { 1 C } }$ and ${ \cal S } _ { 2 } \cup { \cal S } _ { 2 C } ,$ respectively. Given the sizes for $S _ { \mathrm { 1 C } }$ and $S _ { 2 C } ,$ we can infer the value of $\Delta$ that is most likely to have led to observing $\delta { + \delta } ^ { \prime }$ matches between $S _ { 1 }$ and $S _ { 2 }$ . The exact procedure is described below.

The drawing process is illustrated in Figure 20. We consider a hypothetical table H comprising of all entity instances in $S _ { 1 } , \ S _ { 1 C } , \ S _ { 2 } ,$ and $S _ { 2 C }$ . Both $S _ { 1 } \cup S _ { \mathrm { 1 C } }$ and $S _ { 2 } \cup S _ { 2 C }$ are drawn from H. When drawing $S _ { 1 } \cup S _ { \mathrm { 1 C } }$ (steps 1 and 2 in Figure 20) we are interested in determining how many instances that contribute to $\Delta$ will appear in $S _ { 1 } ;$ this is equal to $\delta + \delta ^ { \prime } + \eta _ { 1 2 }$ . The remainder of  (i.e., $\eta _ { 2 1 } + \eta _ { \mathrm { C C } } )$ will appear in $S _ { \mathrm { 1 C } }$ . Further, of those instances in $S _ { \Delta }$ that appear in $S _ { 1 } .$ , we are interested in knowing how many would be expected to appear in $S _ { 2 }$ when $S _ { 2 } \cup S _ { 2 C }$ is drawn from H (steps 3 and 4 in Figure 20).

Figure 19 Overlapping Entity Instances Between $S _ { \mathfrak { 1 } } \cup S _ { \mathfrak { 1 } \mathfrak { C } }$ and $S _ { z } \cup S _ { z \mathrm { c } }$  
![](/api/attachments/WUZKVXN9/fulltext/images/fc9e692c98866872becf39656ad00e1bf7cff41eb5c30f0ee6e02f549231e4f2.jpg)

$$
E (\delta_ {\widetilde {\mathrm{MA}}} ^ {\prime}) = \frac {| \tilde {S} _ {\mathrm{1M}} | \cdot | S _ {\mathrm{2A}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2A}} | + | \hat {S} _ {\mathrm{2M}} |)} \cdot \delta_ {2} ^ {\prime}
$$

$$
E (\delta_ {\widetilde {\mathrm{MM}}} ^ {\prime}) = \frac {| \tilde {S} _ {\mathrm{1M}} | \cdot | \hat {S} _ {\mathrm{2M}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2A}} | + | \hat {S} _ {\mathrm{2M}} |)} \cdot \delta_ {2} ^ {\prime}
$$

$$
E (\delta_ {\mathrm{II}} ^ {\prime}) = \frac {| S _ {\mathrm{1I}} | \cdot | S _ {\mathrm{2I}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \tilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {3} ^ {\prime}
$$

$$
E (\delta_ {\mathrm{IM}} ^ {\prime}) = \frac {| S _ {\mathrm{1I}} | \cdot | \tilde {S} _ {\mathrm{2M}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \tilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {3} ^ {\prime}
$$

$$
E (\delta_ {\widetilde {\mathrm{MI}}} ^ {\prime}) = \frac {| \tilde {S} _ {\mathrm{1M}} | \cdot | S _ {\mathrm{2I}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \tilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {3} ^ {\prime}
$$

$$
E (\delta_ {\widetilde {\mathrm{MM}}} ^ {\prime}) = \frac {| \tilde {S} _ {\mathrm{1M}} | \cdot | \tilde {S} _ {\mathrm{2M}} |}{(| S _ {\mathrm{1I}} | + | \tilde {S} _ {\mathrm{1M}} |) (| S _ {\mathrm{2I}} | + | \tilde {S} _ {\mathrm{2M}} |)} \cdot \delta_ {3} ^ {\prime}
$$

From our drawing process, it follows that for a given value of $\Delta _ { \prime }$ , the distribution for $\delta + \delta ^ { \prime } +$ $\eta _ { 1 2 } = x$ follows a univariate hypergeometric function given by

$$
P (\delta + \delta^ {\prime} + \eta_ {1 2} = x) = \frac {\binom{\Delta}{x} \cdot \binom{| S _ {1} | + | S _ {1 C} | - \Delta}{| S _ {1} | - x}}{\binom{| S _ {1} | + | S _ {1 C} |}{| S _ {1} |}}.\tag{11}
$$

Similarly, given $x , \ \delta + \delta ^ { \prime } = y$ follows a univariate hypergeometric distribution, i.e.,

$$
P (\delta + \delta^ {\prime} = y \mid x) = \frac {\binom{x}{y} \cdot \binom{| S _ {2} | + | S _ {2 C} | - x}{| S _ {2} | - y}}{\binom{| S _ {2} | + | S _ {2 C} |}{| S _ {2} |}}.\tag{12}
$$

The value for $y$ is known, and we wish to find the most likely value for x from Equation (12). When x is unbounded, this is given by the following expression (Johnson et al. 1993 $\mathrm { \bar { p } } . 2 6 2 \mathrm { \bar { \cdot } } ^ { 2 }$

$$
\hat {x} = \lceil (\delta + \delta^ {\prime}) (| S _ {2} | + | S _ {2 C} | + 1) / | S _ {2} | \rceil .
$$

We see from Figure 20 that the value of x is bounded by $| S _ { 1 } |$ . Since the probability distribution for y is unimodal with respect to x (Johnson et al. 1993), it follows that the most likely value for x, if $| S _ { 1 } | <$ $\lceil ( \delta + \delta ^ { \prime } ) ( | S _ { 2 } | + | S _ { 2 C } | + 1 ) / | S _ { 2 } | \rceil$ , must be $| S _ { 1 } |$ . Thus, we have

Figure 20 Drawing Process for Construction of $S _ { \uparrow }$ and $S _ { 2 }$  
![](/api/attachments/WUZKVXN9/fulltext/images/09e1572e55177f28317eed357d0ba7641af0b37396e38d3b1ed1ea3f9f37631d.jpg)

$$
\hat {x} = \min \{\lceil (\delta + \delta^ {\prime}) (| S _ {2} | + | S _ {2 C} | + 1) / | S _ {2} | \rceil , | S _ {1} | \}.
$$

The value $\lvert S _ { 1 } \rvert$ is binding when $| S _ { 1 } |$ is relatively small compared to $| S _ { 2 C } | ,$ , and $\delta + \delta ^ { \prime }$ constitutes a significant proportion of $| S _ { 2 } |$ . For example, if $| S _ { 1 } | = | S _ { 2 } | = 2 , 0 0 0 ,$ $| S _ { 2 C } | = 5 , 0 0 0$ , and $\delta + \delta ^ { \prime } = 1 , 0 0 0$ , then the estimate for unbounded x is 3,500, which is clearly infeasible given the cardinality of <sub></sub>S <sub></sub>. In this situation, the most likely estimate for x is 2,000.

Once x has been estimated,  can be determined from the distribution shown in Equation (11) using a similar procedure. For unbounded , we have

$$
\hat {\Delta} = \lceil \hat {x} \cdot (| S _ {1} | + | S _ {1 C} | + 1) / | S _ {1} | \rceil .
$$

From Figure 20, it is easy to see that $\eta _ { 1 2 } + \eta _ { 2 1 } + \eta _ { \mathrm { C C } }$ is bounded by $| S _ { \mathrm { 1 C } } | + | S _ { 2 C } | ,$ , and therefore  is bounded by $| S _ { 1 \mathrm C } | + | S _ { 2 \mathrm C } | + \delta + \delta ^ { \prime }$ . From the unimodality of the distribution of x with respect to $\Delta ,$ it follows that

$$
\hat {\Delta} = \min \{\lceil \hat {x} \cdot (| S _ {1} | + | S _ {1 C} | + 1) / | S _ {1} | \rceil , | S _ {1 C} | + | S _ {2 C} | + \delta + \delta^ {\prime} \}.
$$

We estimate $\delta + \delta ^ { \prime } + \eta _ { 2 1 } ~ ( = z )$ in a manner analogous to the procedure for estimating $x = \delta + \delta ^ { \prime } + \eta _ { 1 2 }$ shown above. Since the probability distribution for z is also univariate hypergeometric, the most likely value of $z$ is given by min $\{ \lceil ( ( | S _ { 1 } | + | S _ { \mathrm { 1 C } } | + 1 ) / | S _ { 1 } | ) \cdot ( \delta + \delta ^ { \prime } ) \rceil , | S _ { 2 } | \}$ Since $\delta { + } \delta ^ { \prime }$ is observed, once $x , z ,$ and  are estimated, we can determine $\eta _ { 1 2 } , \eta _ { 2 1 }$ , and  , respectively.

4.2.1. Estimating the Sizes of the Components of $\eta _ { 1 2 }$ and $\eta _ { 2 1 }$ . What remains is the estimation of the sizes of the individual components that add up to $\eta _ { 1 2 }$ and to $\eta _ { 2 1 } ,$ respectively. The components of $\eta _ { 1 2 }$ are $\eta _ { \mathrm { A C } } , \ \eta _ { \mathrm { \widehat { M C } } } , \ \eta _ { \mathrm { I C } } .$ and $\eta _ { \widetilde { \mathrm { M C } } } ,$ and are counts of tuples that belong to the four subsets of $S _ { 1 } .$ . The distributions for these counts are multivariate hypergeometric, and are estimated based on the sizes of the subsets of $S _ { 1 }$ . The following adjustment must be made to the sizes of these subsets when estimating the components of $\eta _ { 1 2 }$ . Since estimates have been obtained for the components of  and $\delta ^ { \prime }$ that appear in these subsets, and tuples that constitute those components cannot appear in components of $\widehat { \eta } _ { 1 2 } ,$ they are excluded from $S _ { 1 }$ as shown in Figure 21.

The estimates for the components of $\eta _ { 1 2 }$ and $\eta _ { 2 1 }$ are summarized in Figure 22. Once estimates for all the components of $\delta , \delta ^ { \prime } , \eta _ { 1 2 } , \eta _ { 2 1 } .$ , and $\eta _ { \mathrm { C C } }$ are obtained, the

Figure 21 Distribution of Components of $\widehat { \eta } _ { 1 2 }$  
![](/api/attachments/WUZKVXN9/fulltext/images/227385ccf7662d090aa87a08420eda94c71acdd6d2d7524fcb66287658885426.jpg)

Figure 22 Components of $\eta _ { 1 2 }$ and $\eta _ { 2 1 }$

$$
\widehat {\eta} _ {\mathrm{AC}} = \frac {| S _ {1 \mathrm{A}} | - \delta_ {\mathrm{AA}} - \delta_ {\mathrm{AM}} - \delta_ {\mathrm{AI}} ^ {\prime} - \delta_ {\mathrm{AM}} ^ {\prime}}{| S _ {1} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {1 2}
$$

$$
\widehat {\eta} _ {\widehat {\mathrm{MC}}} = \frac {| \widehat {S} _ {\mathrm{1M}} | - \delta_ {\widehat {\mathrm{MA}}} - \delta_ {\widehat {\mathrm{MM}}} - \delta_ {\widehat {\mathrm{MI}}} ^ {\prime} - \delta_ {\widehat {\mathrm{MM}}} ^ {\prime}}{| S _ {1} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {1 2}
$$

$$
\widehat {\eta} _ {\mathrm{IC}} = \frac {| S _ {\mathrm{II}} | - \delta_ {\mathrm{IA}} ^ {\prime} - \delta_ {\mathrm{II}} ^ {\prime} - \delta_ {\mathrm{IM}} ^ {\prime} - \delta_ {\mathrm{IM}} ^ {\prime}}{| S _ {1} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {1 2}
$$

$$
\widehat {\eta} _ {\widetilde {\mathrm{MC}}} = \frac {| \widetilde {S} _ {\mathrm{1M}} | - \delta_ {\widetilde {\mathrm{MA}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{MI}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime}}{| S _ {1} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {1 2}
$$

sizes for the various subsets of R can be determined for the Difference operation using Equations (1)–(4), and for the Union operation using Equations (5)–(8). The quality profiles are obtained from these estimates.

## 5. Managerial Implications

Using numerical examples for the Difference operation, we illustrate the impact of our methodology in several scenarios. First, we illustrate how our analysis can impact decision making under varying levels of data quality. Next, we demonstrate how the quality parameters change as the number of matches between the two relations increase. Third, we show that estimating the quality profile of the result using a naïve approach could lead to quality metrics that are very misleading. Finally, we illustrate how one could trade off between the mismembership and incompleteness in the result by removing or retaining imperfect matches.

Table 1 provides the important symbols reused in this section. Table 2 provides the cardinalities and

Table 1 Important Symbols Used in This Section

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td> $\alpha_{i}, \beta_{i}, \mu_{i}, \chi_{i}$ </td><td>Accuracy, inaccuracy, mismembership, and incompleteness of a relation  $S_{i}, i \in \{1, 2\}$ .</td></tr><tr><td> $S_{ij}$ </td><td>The set of tuples in  $S_{i}$  associated with subset  $S_{ij}, j \in \{A, I, \widehat{M}, \widetilde{M}, C\}$ .</td></tr><tr><td> $R_{i}$ </td><td>The set of tuples in  $R$  associated with subset  $R_{i}, i \in \{A, I, M, C\}$ .</td></tr><tr><td> $\delta, \delta'$ </td><td>Number of perfectly/imperfectly matching tuples between relations  $S_{1}$  and  $S_{2}$ .</td></tr><tr><td> $\delta_{ij}, \delta'_{ij}$ </td><td>Number of perfectly/imperfectly matching tuples between  $S_{1i}$  and  $S_{2j}, i, j \in \{A, I, \widehat{M}, \widetilde{M}\}$ .</td></tr><tr><td> $\eta, \eta'$ </td><td>Number of potential perfect/imperfect matches</td></tr><tr><td> $\eta_{ij}, \eta'_{ij}$ </td><td>Number of potential perfect/imperfect matches between  $S_{1i}$  and  $S_{2j}, i, j \in \{A, I, \widehat{M}, \widetilde{M}, C\}$ .</td></tr></table>

$$
\widehat {\eta} _ {\mathrm{CA}} = \frac {| S _ {\mathrm{2A}} | - \delta_ {\mathrm{AA}} - \delta_ {\mathrm {\widehat {MA}}} - \delta_ {\mathrm{IA}} ^ {\prime} - \delta_ {\mathrm {\widetilde {MA}}} ^ {\prime}}{| S _ {2} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {2 1}
$$

$$
\widehat {\eta} _ {\mathrm{C} \widehat {\mathrm{M}}} = \frac {| \widehat {S} _ {\mathrm{2M}} | - \delta_ {\mathrm{A} \widehat {\mathrm{M}}} - \delta_ {\widehat {\mathrm{M}} \widehat {\mathrm{M}}} - \delta_ {\mathrm{IM}} ^ {\prime} - \delta_ {\widetilde {\mathrm{M}} \widehat {\mathrm{M}}} ^ {\prime}}{| S _ {2} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {2 1}
$$

$$
\widehat {\eta} _ {\mathrm{CI}} = \frac {| S _ {2 \mathrm{I}} | - \delta_ {\mathrm{AI}} ^ {\prime} - \delta_ {\mathrm{II}} ^ {\prime} - \delta_ {\mathrm {\widetilde {MI}}} ^ {\prime} - \delta_ {\mathrm {\widetilde {MI}}} ^ {\prime}}{| S _ {2} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {2 1}
$$

$$
\widehat {\eta} _ {\mathrm{C} \widetilde {\mathrm{M}}} = \frac {| \widetilde {S} _ {\mathrm{2M}} | - \delta_ {\mathrm{A} \widetilde {\mathrm{M}}} ^ {\prime} - \delta_ {\mathrm{I} \widetilde {\mathrm{M}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{M}} \widetilde {\mathrm{M}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{M}} \widetilde {\mathrm{M}}} ^ {\prime}}{| S _ {2} | - \delta - \delta^ {\prime}} \cdot \widehat {\eta} _ {2 1}
$$

quality profiles of the example relations for the Difference operation.

## 5.1. Impact of Varying Levels of Data Quality

We illustrate using two simple scenarios how business decisions would change based on the quality of the result. We vary the levels of accuracy for relation $S _ { 1 }$ (e.g., the Prospect data for the marketing campaign example discussed in the introduction) in these scenarios, keeping mismembership and incompleteness fixed at 0.1 and 0.2, respectively (therefore, $\beta _ { 1 } = 0 . 9 - \alpha _ { 1 } )$ . We assume $\delta = 0 . 5 | S _ { \mathrm { 1 A } } |$ and $\delta ^ { \prime } = 0 . 5 | S _ { \mathrm { 1 I } } |$ in these examples, which implies $| R | = | S _ { 1 } | - 0 . 5 | S _ { \mathrm { 1 A } } |$ The quality profile for $S _ { 2 }$ is as shown in Table 2. Table 3 provides the quality profile of R with varying levels of $\alpha _ { 1 }$

Continuing with the marketing campaign example, consider a decision maker wishing to determine if the campaign will be profitable $( \mathrm { i . e . , }$ the expected ROI is positive). Assume the ROI for the campaign becomes negative when the mismembership of the resulting table exceeds 0.3 because of the large proportion of ineffective mailings. In that case, as long as the Prospect data has an accuracy of 0.7 or higher (resulting in R having a mismembership of 0.29 or less), the decision would be to go ahead with the campaign. If $\alpha _ { 1 }$ was lower, the decision would be to not proceed with the campaign.

Next, consider another scenario where a decision maker is planning to use the customer records in the resulting table to conduct a survey. The decision maker must receive at least 500 responses for the findings to be meaningful, and would like to know how many questionnaires to mail out (say n). Let us assume that the decision maker knows from prior experience that about 20% of the people on whom they have accurate information respond to their surveys. Then, depending on the accuracy of $S _ { 1 }$ , she can estimate $\scriptstyle \alpha _ { R } ,$ , and in turn determine n. For example, if $\alpha _ { 1 } = 0 . 9 ,$ , then $\alpha _ { R } = 0 . 8 3$ and n is 3,012. If $\alpha _ { 1 } = 0 . 6 ,$ then $\alpha _ { R } = 0 . 3 9$ , and she should mail out $^ { 6 , 4 1 0 }$ questionnaires. On the other hand, if $\alpha _ { 1 } = 0 . 5 ,$ then $\alpha _ { R } = 0 . 3 ,$ and using the entire R $( | R | = 7 , 5 0 0 )$ will still not be enough to get 500 responses. Thus, if $S _ { 1 }$ has an accuracy of 0.5 or less, it will not be adequate for the survey.

Table 2 Quality Profiles for $S _ { \uparrow }$ and $S _ { 2 }$

<table><tr><td></td><td> $|\cdot|$ </td><td> $\alpha$ </td><td> $\beta$ </td><td> $\mu$ </td><td> $\chi$ </td></tr><tr><td> $S_1$ </td><td>10,000</td><td>0.60</td><td>0.30</td><td>0.10</td><td>0.20</td></tr><tr><td> $S_2$ </td><td>8,000</td><td>0.70</td><td>0.20</td><td>0.10</td><td>0.10</td></tr></table>

Table 3 Quality Profile of R with Varying Levels of Accuracy of $S _ { \uparrow }$

<table><tr><td> $\alpha_{1}$ </td><td>0.1</td><td>0.2</td><td>0.3</td><td>0.4</td><td>0.5</td><td>0.6</td><td>0.7</td><td>0.8</td><td>0.9</td></tr><tr><td> $\alpha_{R}$ </td><td>0.05</td><td>0.10</td><td>0.16</td><td>0.22</td><td>0.30</td><td>0.39</td><td>0.49</td><td>0.63</td><td>0.83</td></tr><tr><td> $\beta_{R}$ </td><td>0.47</td><td>0.44</td><td>0.41</td><td>0.37</td><td>0.33</td><td>0.28</td><td>0.22</td><td>0.13</td><td>0.00</td></tr><tr><td> $\mu_{R}$ </td><td>0.48</td><td>0.46</td><td>0.43</td><td>0.40</td><td>0.37</td><td>0.33</td><td>0.29</td><td>0.24</td><td>0.17</td></tr><tr><td> $\chi_{R}$ </td><td>0.21</td><td>0.21</td><td>0.22</td><td>0.23</td><td>0.24</td><td>0.24</td><td>0.25</td><td>0.26</td><td>0.27</td></tr></table>

These examples illustrate both how the data quality affects decisions as well as the role different parameters may have on the decision. Further, what is to be accomplished with the data also plays a pivotal role in determining the acceptable level of data quality for the decision problem.

## 5.2. Impact of  and $\delta ^ { \prime }$

We have already seen that  and $\delta ^ { \prime }$ play an integral role in determining the quality profile of the resulting relations. How much does the quality profile of the result R change with these parameters? To illustrate, we first fix $\delta ^ { \prime }$ at 2,000 and vary  in the range of "0 5 000# with increments of 1,000. Subsequently, we repeat the experiments by fixing  at 2,000 and varying $\delta ^ { \prime }$ in the same manner.

The results from varying  are shown in Figure 23. Considering the quality profile of $S _ { 1 }$ as the benchmark, we find that the metrics for mismembership and incompleteness increase with an increase in $\delta ,$ primarily at the expense of accuracy. The accuracy of R drops from about 0.5 when 1,000 records match to only about 0.2 when 5,000 records match.

Figure 23 Impact of  on the Quality Profile for $R = S _ { 1 } - S _ { 2 }$  
![](/api/attachments/WUZKVXN9/fulltext/images/588a39fb811a15e3c0713a47548a86d3ab965c2c4a92dd7723dff6dccf9761fd.jpg)

By the same token, mismembership goes up from approximately 0.3 when 1,000 records match to over 0.5 when 5,000 records match. Consider again the marketing campaign example. Although the original data set with a mismembership of 10% may have appeared reasonable, once the Difference operation is performed, the mismembership increases to 30% with a match of just 1,000 records. If 5,000 records matched, the mismembership would be over 50% and the ROI using R would be negative.

The results from varying $\delta ^ { \prime }$ are shown in Figure 24. In this case, sharp decreases in both accuracy and inaccuracy of R result in a dramatic increase in mismembership of R as $\delta ^ { \prime }$ increases; the mismembership is close to 0.7 when $\delta ^ { \prime } = 5 , 0 0 0 .$ . On the other hand, the incompleteness of R shows little change. Like the previous case, the drastic increase in mismembership of R would impact the ROI and demands careful consideration by decision makers.

Figure 24 Impact of  on the Quality Profile for $R = S _ { 1 } - S _ { 2 }$  
![](/api/attachments/WUZKVXN9/fulltext/images/1751827bb3992ccc216d512053b055434e93b1dd04d4abdf063ee3a8303aaf06.jpg)

## 5.3. Comparison Between the Naïve and the Proposed Approach

It may be easy to estimate the quality profile for R using a naïve approach that ignores the impact of imperfect matches, and further, assumes that tuples are equally likely to match across all subsets of the relations. Using the naïve approach, the cardinalities of the different subsets in the result are as shown below. Since these expressions are derived ignoring imperfect matches, components of $\delta ^ { \prime }$ do not appear in them. The terms $\delta _ { i j }$ in these expressions refer to the estimated number of matches between subset i in $S _ { 1 }$ and subset j in $S _ { 2 }$ . For example, $\delta _ { \mathrm { A M } }$ refers to the number of matches between $S _ { \mathrm { 1 A } }$ and $S _ { 2 \mathrm { M } }$ in this approach (this approach does not distinguish between $\hat { \cal S } _ { 2 \mathrm { M } }$ and $\tilde { S } _ { 2 \mathrm { M } }$ , and only considers the aggregate set $S _ { 2 \mathrm { M } } )$

$$
\begin{array}{r} | R _ {\mathrm{A}} | = | S _ {\mathrm{1A}} | - \delta_ {\mathrm{AA}} - \delta_ {\mathrm{AM}} - \delta_ {\mathrm{AI}} - \eta_ {\mathrm{AC}}, \\ | R _ {\mathrm{I}} | = | S _ {\mathrm{1I}} | - \delta_ {\mathrm{IA}} - \delta_ {\mathrm{II}} - \delta_ {\mathrm{IM}} - \eta_ {\mathrm{IC}}, \\ | R _ {\mathrm{M}} | = | S _ {\mathrm{1M}} | - \delta_ {\mathrm{MA}} - \delta_ {\mathrm{MI}} - \delta_ {\mathrm{MM}} + \eta_ {\mathrm{AC}} + \eta_ {\mathrm{IC}}, \quad \text {and} \\ | R _ {\mathrm{C}} | = | S _ {\mathrm{1C}} | + \delta_ {\mathrm{AM}} + \delta_ {\mathrm{IM}} - \eta_ {\mathrm{CA}} - \eta_ {\mathrm{CI}} - \eta_ {\mathrm{CC}}. \end{array}
$$

Assuming that the number of matches across different subsets is proportional to the products of the sizes of the subsets (which ignores the fact that accurate tuples cannot perfectly match inaccurate ones), we can estimate the various components of  needed above. Figure 25 shows the implications of not considering the $\delta ^ { \prime }$ components and their effects on quality profiles, as well as not carefully recognizing which matches are truly possible (the quality profile for the naïve approach is denoted by the subscript NR).

As is apparent from the figure, the quality profile for R in the naïve case is quite similar to that of $S _ { 1 }$ . While the general trends for accuracy and for mismembership are similar to that of the proposed approach, i.e., accuracy drops while mismembership increases with increasing $\delta ,$ the impact is minimal in the naïve case. It is only for higher values of  that the effect becomes noticeable. One may make erroneous decisions using the naïve approach since even at $\delta = 5 , 0 0 0 _ { \cdot }$ , this approach predicts accuracy to be as high as 0.55 and mismembership at 0.15, when they are about 0.2 and 0.55, respectively.

Figure 25 Comparing the Proposed Approach with a Naïve Approach for Varying  Values  
![](/api/attachments/WUZKVXN9/fulltext/images/3d0e30262c45f5525b7d785dfd8c47c344c9aab2bb5c1603a435c5de371ed38f.jpg)

We repeat the above experiment for different values of $\delta ^ { \prime }$ (keeping  fixed). The results are shown in Figure 26. As shown, the naïve case grossly overestimates the accuracy of R (0.68 versus 0.27) as $\delta ^ { \prime }$ increases to $5 { , } 0 0 0 ,$ while underestimating its mismembership (0.31 versus 0.68). Again, these severe differences would lead to poor decisions.

## 5.4. Imperfect Matches to Keep or Not

An interesting decision problem that arises is whether to keep the imperfect matches or remove them from R, the result of the Difference operation. In other words, should the tuples that constitute $\delta ^ { \prime }$ be removed, and if so what impact would it have on the quality of the result. Equations (1)–(4) have to be modified to account for the removal of the components of $\delta ^ { \prime }$ from R. On one hand, many of the components that contributed to mismembership in R (such as the $\delta _ { \mathrm { A I } } ^ { \prime }$ and the $ { \delta _ { \mathrm { L A } } } ^ { \prime }$ components in $R _ { \mathrm { M } } )$ will be removed, and Equation (3) will be modified accordingly. On the other hand, the primary change for $R _ { \mathrm { A } }$ will be the removal of the $\delta _ { _ \mathrm { A \widetilde { M } } } ^ { \prime }$ component. This is a match between accurate tuples in $S _ { 1 }$ and mismember tuples in $S _ { 2 } ,$ which should ideally not be removed. However, because they are, this component will now contribute to the incomplete set. Similarly, for $R _ { \mathrm { I } } ,$ we see that $\delta _ { \widehat { \mathrm { I M } } } ^ { \prime }$ and $\delta _ { \widetilde { \mathrm { I M } } } ^ { \prime }$ are removed when they should not; this also contributes to incompleteness. Thus, we expect to see an increase in incompleteness and a decrease in mismembership by removing imperfect matches. The counterparts for Equations (1)–(4) are obtained as

Figure 26 Comparing the Proposed Approach with a Naïve Approach for Varying  Values  
![](/api/attachments/WUZKVXN9/fulltext/images/44a631438e18d4ea2a71a3146897aae6617c7327a25033f21e4910148e22a852.jpg)

$$
| R _ {\mathrm{A}} | = | S _ {1 \mathrm{A}} | - \delta_ {\mathrm{AA}} - \delta_ {\mathrm{A} \widehat {\mathrm{M}}} - \delta_ {\mathrm{AI}} ^ {\prime} - \delta_ {\mathrm{A} \widetilde {\mathrm{M}}} ^ {\prime} - \eta_ {\mathrm{AC}},
$$

$$
| R _ {\mathrm{I}} | = | S _ {\mathrm{1I}} | - \delta_ {\mathrm{IA}} ^ {\prime} - \delta_ {\mathrm{II}} ^ {\prime} - \delta_ {\mathrm{IM}} ^ {\prime} - \delta_ {\mathrm{IM}} ^ {\prime} - \eta_ {\mathrm{IC}} ^ {\prime},
$$

$$
\begin{array}{r} | R _ {\mathrm{M}} | = | S _ {1 \mathrm{M}} | - \delta_ {\widehat {\mathrm{MA}}} - \delta_ {\widehat {\mathrm{MI}}} ^ {\prime} - \delta_ {\widehat {\mathrm{MM}}} - \delta_ {\widehat {\mathrm{MM}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{MA}}} ^ {\prime} \\ - \delta_ {\widetilde {\mathrm{MI}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime} - \delta_ {\widetilde {\mathrm{MM}}} ^ {\prime} + \eta_ {\mathrm{AC}} + \eta_ {\mathrm{IC}} ^ {\prime}, \quad \text {and} \end{array}
$$

$$
| R _ {\mathrm{C}} | = | S _ {1 \mathrm{C}} | + \delta_ {\mathrm{A} \widehat {\mathrm{M}}} + \delta_ {\mathrm{A} \widetilde {\mathrm{M}}} ^ {\prime} + \delta_ {\mathrm{I} \widehat {\mathrm{M}}} ^ {\prime} + \delta_ {\mathrm{I} \widetilde {\mathrm{M}}} ^ {\prime} - \eta_ {\mathrm{CA}} - \eta_ {\mathrm{CC}} - \eta_ {\mathrm{CI}} ^ {\prime}.
$$

To better understand the effect of removing or retaining the imperfect matches from R, we performed a numerical analysis where we fixed $\delta =$ 2 000, and varied $\delta ^ { \prime }$ in the range "0 5 000# with increments of 1,000. The results for mismembership and incompleteness are shown in Figure 27, where $( \mu _ { e x } , \chi _ { e x } )$ and $( \mu _ { R } , \chi _ { R } )$ denote the mismembership and incompleteness for the removal and retention scenarios, respectively.

As expected, retaining imperfect matches in R leads to substantially higher mismembership while their removal leads to higher incompleteness. A related question, then, is when should imperfect matches be retained (or removed). The answer depends on the cost of missing a relevant entity instance versus including an entity instance incorrectly $( \mathrm { i . e . , }$ the costs of type-I and type-II errors). Thus, in our marketing campaign example, sending an expensive promotion to a large number of people incorrectly could be a significant unjustified cost, and it may be preferable to exclude the imperfect matches. On the other hand, if one were to consider a social welfare scenario where information is being mailed to people who are dependant on the information, missing an individual could have a high cost and it would make sense to keep the imperfect matches.

## 6. Contributions, Discussions, and Directions for Future Research

This paper, in conjunction with our previous work (Parssian et al. 2004), provides the necessary tools for analyzing the quality of the results when performing any of the primitive operations on a relational database. $\mathrm { A s }$ this work illustrates, determining the quality profiles of the results of the Difference and Union operations are quite complex, and very different from the other primitive relational operations. Furthermore, we show that just the knowledge of the quality profile of the participating tables is not sufficient to infer the quality profile of the result; in fact, the quality of the result is also dependent on the interaction between the two tables (i.e.,  and ). For example, in our ROI example, superficially it would appear that a low mismembership of $S _ { 1 }$ would be sufficient to have a low mismembership in the result of the Difference operation. However, a large $\delta ^ { \prime }$ and a relatively high inaccuracy could result in high mismembership (as evident from Equation (3)).

An important aspect of our analysis is that it does not require that the data be static. What is assumed is that the error-generating processes for the source data do not keep changing, and hence the error rates are stable. Consequently, data manipulation operations like updates, insertions, and deletions would not significantly change the error proportions within the base relations. Because our analysis uses the sizes of the participating relations, it explicitly accounts for such data manipulation operations.

Figure 27 Comparing the Removal of Imperfect Matches to Retaining Them  
![](/api/attachments/WUZKVXN9/fulltext/images/137dba7457423c42acb2aad099c89e541725dc9f6532ee037aa983916f808f34.jpg)

Our work fills an important gap in the extant research on information quality. While prior research has recognized that the quality of information products should be derived based on processing operations and the quality of data inputs, the actual derivations had been treated as black box operations (Ballou et al. 1998). Several methodologies, such as the Information Product Map (IP-Map) (Shankaranarayanan et al. 2000, Shankaranarayanan and Cai 2006) and the control matrix approach (Pierce 2004), have been developed that enable data quality professionals to diagram and analyze how information products are manufactured. Our techniques can be used to enhance such existing methodologies (perhaps as CASE tools) such that they can be used to estimate the projected quality of intermediate and final information products. Such tools can also be used in a decision-support mode to examine the potential impact of data-cleansing operations on information products. In situations where resources for data quality enhancement are constrained (Ballou and Tayi 1999), our analyses can help decide which data sources should be cleaned to be most beneficial for the organization.

In practice, many queries require the execution of a sequence of primitive operations. An interesting question, then, is how to obtain the quality profile of the result of such queries. When composite operations are executed, the analyses provided in this work and our prior research could be used to determine the quality profile of the result provided our assumptions about the independence of error-generating processes are not violated. The quality of the result would be obtained by evaluating the quality profile of each intermediate relation using the quality algebra associated with the corresponding operation. For instance, a query may require the union of the result of two selection operations, one on a base relation $S _ { 1 }$ and another on a base relation $S _ { 2 }$ . The quality of the intermediate results of the two selection operations (say, $R _ { 1 }$ and $R _ { 2 } )$ can be derived using the quality algebra for the selection operation (Parssian et al. 2004). If the error-generating processes for $S _ { 1 }$ and $S _ { 2 }$ are independent, then the quality analysis for the union operation can be applied based on the sizes and quality profiles of $R _ { 1 }$ and $R _ { 2 } ,$ along with the count of perfect and imperfect matches that result from the union of

$R _ { 1 }$ and $R _ { 2 } .$ On the other hand, if $S _ { 1 }$ and $S _ { 2 }$ are not base relations, and are instead results of some operations on a common base relation $S ,$ then our analyses cannot be used directly. In such a situation, it would be necessary to determine how the various operations impact the underlying base tables, and alternate procedures would have to be developed.

Our analyses provide the core functions needed to build a quality profile engine that can interface directly with a relational database engine. Adding these functionalities to relational engines will enable the provisioning of quality metadata in addition to the information itself to decision makers. The quality metadata will enable managers and users to make better decisions about whether the information they receive is of acceptable quality for their specific needs. Our approach is quite efficient, as it requires storing and manipulating the quality metadata at the relation level. This overcomes the storage and estimation expenses associated with tagging quality metadata for individual records and attributes, as considered in extant research (Fisher et al. 2003).

An interesting observation is that while the result of a query can sometimes be obtained by different sequences of primitive operations, the correct quality profile may be obtained by following a particular sequence and not others. For instance, the result of the following two sequences of operations, A<sub>∩</sub>B <sub>∪</sub>C and A <sub>∩</sub> B <sub>∪</sub> A <sub>∩</sub> C, lead to the same query result. However, to determine the correct quality profile of the resulting relation, the first sequence must be considered, regardless of the sequence used for the query execution itself. Using the second sequence for estimating the quality profile violates the requirement that the occurrences of errors in relations participating in a union operation should be independent. It is, therefore, necessary to determine how the quality profiles for the results of other queries such as the one illustrated above should be derived to develop a comprehensive quality engine.

As is apparent from the above discussion, a limitation of this work is that if the error-generating processes for participating relations are not independent, our analyses will not hold. If these processes are dependent, this dependence would need to be parameterized, and an analysis that incorporates this dependence parameter would be needed. Of course, if the dependence is because the participating relations are drawn from the same underlying base table, then alternative query plans could be considered. For example, our analysis for the Difference operation will not apply for a query of the form (S Where C1 holds) <sub>−</sub> (S Where C2 holds). However, the quality profile of the result could be obtained by considering the result as the outcome of the conjunction of two selection operations, one of which includes a negation. Consequently, the impacts of such logical operators are of considerable research interest. While some research has been conducted in this regard (Parssian et al. 2002), more work remains to be done.

Our work opens up several other interesting avenues for future research as well. In some applications, new attributes are derived from existing ones (e.g., an attribute Amount may be created as the product of two attributes Quantity and Sale\_Price). The quality of such derived attributes would be useful for users of such data. Considering interval estimates for quality metrics is also an important exercise for future research. It is possible that in some environments the error generating processes are constantly changing over time, and the number of modification operations (i.e., updates, deletions, and insertions) in a short amount of time constitutes a significant fraction of the source relations. In such environments, it might be necessary to estimate the quality profiles for base relations frequently. Determining the frequency of such sampling is another interesting research question.

## Acknowledgments

This paper has greatly benefited from the many discussions on hyper-geometric drawing processes the authors had with R. Chandrasekharan and Shun Chen Niu from the University of Texas at Dallas. The authors would also like to thank the senior editor, the associate editor, and the reviewers for their detailed comments and suggestions that have considerably improved the paper. The reviewers suggested the examples discussed in §6.

## References

Ballou, D., G. Tayi. 1999. Enhancing data quality in data warehouse environments. Comm. ACM 42(1) 73–78.

Ballou, D., I. N. Chengalur-Smith, R. Wang. 2006. Samplebased quality estimation of query results in relational database environments. IEEE Trans. Know. Data Engrg. 18(5) 639–650.

Ballou, D., R. Wang, H. Pazer, G. Tayi. 1998. Modeling information manufacturing systems to determine information product quality. Management Sci. 44(4) 462–484.

CNNMoney. 2004. (June 17) http://money.cnn.com/2004/06/17/ pf/debt/credit\_report/index.htm?cnn <sub>=</sub> yes.

Cohn, J. P. 2001. Scientists concerned about proposed data quality guidelines. BioScience 51(10) 806.

Feller, W. 1968. An Introduction to Probability Theory and Its Applications, Vol. 1, 3rd ed. John Wiley & Sons, New York.

Fisher, C. W., I. N. Chengalur-Smith, D. Ballou. 2003. The impact of experience and time on the use of data quality information in decision making. Inform. Systems Res. 14(2) 170–188.

IDMA (Insurance Data Management Association) News Letter. 2003. Feb. 27, http://www.idma.org/valuePropositionGeneral. pdf.

Jiang, Z., V. S. Mookerjee, S. Sarkar. 2005. Lying on the web: Implications for cost effective information gathering. Inform. Systems Res. 16(2) 131–148.

Johnson, N. L., S. Kotz, A. W. Kemp. 1993. Univariate Discrete Distributions, 2nd ed. John Wiley & Sons, New York.

Kon, H., S. Madnick, M. Siegel. 1995. Good answers from bad data: A data management strategy. Proc. 5th Annual Workshop Inform. Tech. Systems, Amsterdam, 77–86.

Lorence, D. P. 2003. The perils of data misreporting. Comm. ACM 46(11) 85–88.

Morey, R. C. 1982. Estimating and improving the quality of information in a MIS. Comm. ACM 25(5) 337–342.

Motro, A., I. Rakov. 1998. Estimating the quality of databases. Proc. 3rd Int’l Conf. Flexible QueryAnswering Systems, Roskilde, Denmark, 298–307.

Parssian, A. 2002. Assessing information quality for relational databases. Unpublished doctoral dissertation, School of Management, University of Texas at Dallas.

Parssian, A. 2006. Managerial decision support with knowledge of accuracy and completeness of the relational aggregate func tions. Decision Support Systems 42(3) 1494–1502.

Parssian, A., S. Sarkar, V. S. Jacob. 2002. Assessing information quality for the composite relational operation join. C. Fisher, B. Davidson, eds. Proc. Seventh Internat. Conf. Inform. Quality, November 8–10. MIT, Cambridge, Massachusetts, 225–237.

Parssian, A., S. Sarkar, V. S. Jacob. 2004. Assessing data quality for information product: Impact of selection, projection, and Cartesian product. Management Sci. 50(7) 967–982.

Pierce, E. M. 2004. Assessing data quality with control matrices. Comm. ACM 47(2) 82–86.

Reddy, M., R. Wang. 1995. Estimating data accuracy in a federated database. Proc. 6th Int’l Conf. Inform. Systems and Data Management, Bombay, India, 115–134.

Shankaranarayanan, G., Y. Cai. 2006. Supporting data quality management in decision-making. Decision Support Systems 42(1) 302–317.

Shankaranarayanan, G., R. Y. Wang, M. Ziad. 2000. IP-map: Representing the manufacture of an information product. Proc. 2000 Conf. Inform. Quality, MIT, Cambridge, MA, 1–16.

Wang, R., V. Storey, C. Firth. 1995. A framework for analysis of data quality research. IEEE Trans. Know. Data Engrg. 7(4) 623–639.

Wang, R., Y. W. Lee, L. L. Pipino, D. Strong. 1998. Manage your information as a product. Sloan Management Rev. 29(4) 95–105.

Ziff Davis. 2006. Data Management Dynamics—The ROI from Data Quality. Ziff Davis Media Custom Publishing, New York.
