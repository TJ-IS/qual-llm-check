---
otero_id: 9666
otero_key: "XHFDVZ5Q"
title: "Managerial decision support with knowledge of accuracy and completeness of the relational aggregate functions"
authors: "Amir Parssian"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.12.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managerial decision support with knowledge of accuracy and completeness of the relational aggregate functions

Amir Parssian

University of Illinois at Springfield, One University Plaza, Springfield 62703, United States

Received 31 March 2005; received in revised form 25 September 2005; accepted 22 December 2005 Available online 13 February 2006

## Abstract

Aggregate data produced by decision support systems is utilized by managers in their decision making process to run or improve their firm's operations. Often, data residing in corporate databases and data warehouses are far from being perfect, and their imperfections have an impact on decision quality and outcome. Therefore, having knowledge about the effect of data errors on aggregate data could lead to more informed decisions, reduced risks, and competitive advantage. In this paper, we present a methodology to estimate the effects of data accuracy and completeness, as two important data quality dimensions, on the relational aggregate functions Count, Sum, Average, Max, and Min. Our methodology defines a set of attribute value types and deploys sampling strategies to determine the maximum likelihood estimates of each value type. We show the effect of data error rates on the scalar values returned by the aggregate functions and demonstrate the efficiency of our estimates by Monte Carlo simulations.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Information quality; Relational aggregate functions; Sampling strategies

## 1. Introduction

Managers use aggregated data (summary information) retrieved from their companies' databases and data warehouses to make tactical or strategic decisions to run and improve their firms' operations. Most databases and data warehouses contain data errors that are created either by people [11] or caused by systems failure [15]. The existence of data errors directly impacts the decision quality [4,26] as the eroded data quality accumulates and propagates through the aggregation process. Without having proper knowledge about the quality of information at hand, managers either trust or are forced to accept the available information at its face value and base their decisions upon that. While detecting and correcting data errors could be expensive, resource-intensive, and often impractical, the need for error-free data may be replaced by knowledge gained from assessment of information quality. A manager may not be able to obtain perfect information, but knowledge about the imperfection rate may be helpful to compose or change business scenarios or undertake appropriate actions. Therefore, from the perspectives of increasing profits and minimizing risks, assessment of information quality seems imperative to support informed decisions.

To illustrate the effect of quality of aggregated data on business decisions, consider two major consumer electronic product manufacturers, company A and B. Both companies sell a particular product in two versions of large and small through their proprietary and franchised stores. The stores report their sales data to their parent companies which are then recorded in corporate data warehouses as part of decision support systems that help the management to analyze the sales trend. Both companies want to decide which product version to keep and which one to discontinue. They would be better off if both choose the same product type (say the large one) as it leads to a standard and it boosts their sales. If company A moves first by choosing one of the two product types, then company B adopts that choice too. In case that the aggregated sales data used by company A's management suffer from sufficient inaccuracy and incompleteness, company A may choose to keep the small version of the product instead of the large one. This choice, followed by company B, will then lead to a lesser payoff for both companies affecting their profits.

In another scenario, a manager uses the total count of active customers, who have placed orders for certain products in the past, for forecasting the demand and subsequently for planning of production, inventory, and distribution of those products. The accuracy and completeness of the customer count directly impacts the manager's decisions on forecasting and planning activities that could lead to over- or under-production and in-stock levels of inventory. Therefore, knowledge about the accuracy and completeness of such count would help the manager to adjust the planning accordingly.

The term data quality is a subjective notion and depends on the context and goals of the information consumers. Often, subjective qualitative measures, such as low, medium, and high, are used to indicate the quality of data. However, users may not share the same perceptions as to what low or high quality data pertains to. The above examples show that quantitative metrics to measure the information quality would lead to more objective judgments and decisions. Hence, the main goal of this work is to provide a framework where quality characteristics of aggregate data could be measured quantitatively.

The organization of this paper is as follows. In Section 2, we discuss the prior research related to data quality dimensions, handling of incomplete data, and relational aggregate functions. Section 3 covers the ontological foundations and basic definitions of our work. We derive the quality estimations for the relational aggregate functions in Section 4 and give numeric examples of our estimations in Section 5. Our concluding remarks are given in Section 6.

## 2. Related work

Prior researches relevant to different aspects of our work are summarized below.

## 2.1. Data quality dimensions and metrics

Data quality dimensions that are potentially of interest to end users (information consumers) have been enlisted in numerous studies [6,28]. Although no study provides a set of standard data quality dimensions, four dimensions of accuracy, completeness, consistency, and timeliness have been widely cited in the literature as the most important data quality dimensions to the information consumers. Since metrics to measure timeliness were derived in an information product manufacturing model [1], and consistency is more related to data semantics and metadata, in this work we focus on accuracy and completeness of data.

Within relational data model, some studies have defined a set of four tuple types (i.e., accurate, inaccurate, mismember, and incomplete) for a base relation [12,22,24] and developed metrics to measure the propagation of data errors from base relations throughout the output (i.e., query result). Their metrics measure accuracy and completeness of relational algebra operations at tuple level. For our purpose, we also adopt these types, but at cell (attribute value) level rather than the tuple level, since the relational aggregate functions operate on attributes.

In other study, an attribute-based model has been introduced where quality indicators are tagged to each cell [29]. This model has practical limitations in terms of data validation, storage, and processing when the numbers of tuples and attributes (and thus cells) are very large. Our framework is based on statistical sampling of quality profiles for each attribute and, therefore, does not have such limitations.

## 2.2. Nulls and incompleteness

Nulls or missing values have been extensively studied in the context of information completeness within relational databases [5,9,16,17,19,23]. In some studies, nulls were treated as inaccurate values at tuple levels [22,24] but in this study we treat nulls as incomplete values and use the following two main interpretations of nulls under the Closed World Assumption: “a) the value exists, but it is not known, and b) the value does not exist” ([7], p. 51). The first null type, referred to as existential null, represents an attribute value within database domain that is unknown and thus missing from the database. An example of existential null is the phone extension of an employee that has not been entered in the database. The second null type, referred to as non-existential null, represents an attribute value that does not exist in the real world.

<table><tr><td>Store_No</td><td>Prod_ID</td><td>Sales_Date</td><td>QTY</td><td>Sales_Amt</td></tr><tr><td>S1</td><td>P1</td><td>03-jan-04</td><td>10</td><td>2000</td></tr><tr><td>S1</td><td>P1</td><td>15-apr-04</td><td>40</td><td>8000</td></tr><tr><td>S2</td><td>P2</td><td>22-apr-04</td><td>45</td><td>9000</td></tr><tr><td>S3</td><td>P1</td><td>06-may-04</td><td>15</td><td>3000</td></tr><tr><td>S3</td><td>P2</td><td>12-jun-04</td><td>25</td><td>5000</td></tr><tr><td>S4</td><td>P1</td><td>14-aug-04</td><td>20</td><td>4000</td></tr><tr><td>S1</td><td>P2</td><td>15-sep-04</td><td>25</td><td>5000</td></tr><tr><td>S5</td><td>P1</td><td>01-oct-04</td><td>40</td><td>8000</td></tr></table>

Fig. 1. Conceptual relation for Sales data.

An example of non-existential null is the value for attribute Spouse for a single employee.

## 2.3. Relational aggregate functions

Evaluation and estimation of relational aggregate functions over incomplete data has been addressed by several studies in the past. One study involved a framework for evaluating the aggregate functions over imprecise data where nulls may take a partial value from a set of possible values in which exactly one is the true value [3]. Theoretical frameworks included one for setvalued aggregate functions where attributes take their values from a set of values but did not present a formal treatment of nulls [21]. Algorithms for statistical estimation of COUNT function based on sampling were presented in [8] and assumed that the relations do not contain incomplete information (i.e., nulls). Our study differs from these previous works in the sense that we consider an atomic value for nulls in the relation and study their effect on the accuracy and completeness of scalar values returned by aggregate functions.

## 3. Ontological foundations and basic definitions

We consider relations that have a properly defined identifier within the relational data model. By identifier, we mean a single attribute or a composite set of attributes that uniquely identifies a tuple within a relation. Further, we use the Open World Assumption, which declares that there may be relevant tuples belonging to a relation that are not present in that relation [25], to introduce our definitions.

<table><tr><td>Store_No</td><td>Prod_ID</td><td>Sales_Date</td><td>QTY</td><td>Sales_Amt</td></tr><tr><td>S1</td><td>P2</td><td>15-sep-04</td><td>25</td><td>5000</td></tr><tr><td>S5</td><td>P1</td><td>01-oct-04</td><td>40</td><td>8000</td></tr></table>

Fig. 3. Incomplete data set for the Sales table.

Let T be a conceptual relation that contains all instances of a real-world entity. All attribute values in T are by definition accurate and complete. Instances of T are captured into a physically stored relation S where due to some possible error-generating mechanisms some data values in S become inaccurate, become existential nulls or some data even not being captured into S. If an inaccuracy occurs in any of the identifier attributes, then the non-identifier attribute values no longer represent a valid fact about that particular identifier. In such cases, we have mismember values which do not belong to S but are present. Those instances of T that have not been captured into S form the incomplete data set denoted by S . To illustrate these relations, consider a conceptual sales transactions relation as shown in Fig. 1.

The instances of T are captured into relation S where some attribute values have become erroneous as shown in Fig. 2. Some instances of T that are not captured in S form the incomplete data set $S _ { C }$ as shown in Fig. 3. The set of identifier attributes is {Store\_No, Prod\_ID, Sales\_Date} and the set of non-identifier attributes is {QTY, Sales\_Amt}. In Fig. 2, the inaccurate and existential null values are shown by a grey background and the ‘Sales\_Amt Status’ column is shown for illustrative purposes and is not actually stored in S.

Let $K = \{ k _ { 1 } , k _ { 2 } , . . . , k _ { m } \}$ and $Q { = } \{ q _ { 1 } , q _ { 2 } , . . . , q _ { n } \}$ be the sets of identifier and non-identifier attributes of S, respectively. We denote an identifier attribute value by $\nu _ { k }$ and a non-identifier attribute value by $\nu _ { q } .$ Further, we use the letters A, I, N, M, and C to assign an accurate, inaccurate, existential null, mismember, or incomplete status to any attribute value. We will use ‘←’ for status assignment. Let t be an arbitrary tuple in S (Fig. 2) for which we define the following attribute value types:

<table><tr><td>Store_No</td><td>Prod_ID</td><td>Sales_Date</td><td>QTY</td><td>Sales_Amt</td><td>Sales_Amt Status</td></tr><tr><td>S1</td><td>P1</td><td>03-jan-04</td><td>10</td><td>2000</td><td>A</td></tr><tr><td>S1</td><td>P1</td><td>15-apr-04</td><td>40</td><td>8000</td><td>A</td></tr><tr><td>S2</td><td>P2</td><td>22-apr-04</td><td>40</td><td>7500</td><td>I</td></tr><tr><td>S3</td><td>P1</td><td>06-may-04</td><td></td><td></td><td>C</td></tr><tr><td>S3</td><td>P2</td><td>12-jun-04</td><td>25</td><td>5000</td><td>A</td></tr><tr><td>S4</td><td>P1</td><td>14-aug-04</td><td>20</td><td>4000</td><td>A</td></tr><tr><td>S5</td><td>P2</td><td>10-sep-04</td><td>30</td><td>6000</td><td>M</td></tr></table>

Fig. 2. Stored Sales table.

i) Accurate identifier: an attribute value in the identifier set is defined as accurate if, and only if, all attribute values that compose the identifier are accurate. Formally stated: $[ ( \nu _ { k i }  \mathbf { A } ) \land ( \forall $ $\nu _ { k j }  \mathrm { A } ) ] \Rightarrow ( \nu _ { k i }  \mathrm { A } ) , \ i , j \in \{ 1 , \ 2 , \ \dotsc \ , \ m \} , \ i \neq j .$ An example of accurate identifier attribute value is {Store $\mathrm { \Delta N o = ^ { \circ } S 1 ^ { \circ } }$ , Prod $\mathrm { J D } { = } { } ^ { 6 } \mathrm { P } 1 ^ { \circ }$ , Sales\_Date = $^ { \cdot } 0 3 \ – \mathrm { j a n } – 0 4 ^ { \cdot } \}$ . The values for all attributes composing the identifier are accurate.

ii) Mismember identifier: an attribute value in the identifier set is defined as mismember if, and only if, the attribute value itself is inaccurate or at least one of the other attribute values composing the identifier is inaccurate: (∃ $\nu _ { k i } \longleftarrow \mathrm { I } ) \Longrightarrow ( \forall \nu _ { k i } \longleftarrow \mathrm { M } )$ $i { \in } \{ 1 , ~ 2 , ~ { \ldots } ~ , ~ m \}$ . An example of mismember identifier attribute value is {Store $\mathrm { N o } = \mathrm { \bar { S } } 5 ^ { \circ }$ Prod $\mathrm { \Delta I D } { } = { } ^ { 6 } \mathrm { P } { } 2 { } ^ { \circ }$ , Sales\_ $\mathrm { D a t e } { = } ^ { \cdot } 1 0 { \cdot } \mathrm { s e p } { - } 0 4 ^ { \circ } \}$ The $\cdot \mathrm { P } 2 ^ { \bullet }$ value for Prod\_ID is inaccurate, causing misidentification of the facts represented by this tuple. In other words, the sales transaction of 6000 for 30 quantity of this product in store ‘S5’ on sales date $\cdot _ { 1 0 - \mathrm { S e p } - 0 4 } ,$ has not occurred. This tuple does not belong to the relation.

iii) Accurate non-identifier: a non-identifier attribute value is defined as accurate if, and only if, the attribute value itself along with all the attribute values composing the identifier are accurate: $[ ( \nu _ { q j }  \mathrm { A } ) \land ( \forall \nu _ { k i }  \mathrm { A } ) ] { \Rightarrow } ( \nu _ { q j }  \mathrm { A } ) , i \in \{ 1 , \ 2$ $. . . , m \} , j \in \{ 1 , 2 , . . . , n \}$ . Examples of accurate nonidentifier attribute values are Sales\_Amt = $\{ 2 0 0 0 , 5 0 0 0 , 8 0 0 0 \}$ that have accurate values for all their identifier values.

iv) Inaccurate non-identifier: a non-identifier attribute value is defined as inaccurate if, and only if, the attribute value itself is inaccurate and all the attribute values composing the identifier are accurate: $[ ( \nu _ { q j }  \mathrm { I } ) \land ( \forall \nu _ { k i }  \mathrm { A } ) ] { \Rightarrow } ( \nu _ { q j }  \mathrm { I } )$ , $i \in \{ 1 , 2 , . . . , m \} , j \in \{ 1 , 2 , . . . , n \}$ . An example of inaccurate non-identifier attribute value is Sales\_- Amt = 7500 that has an inaccurate value (i.e., the actual value has been 9000 but has been erroneously recorded as 7500) and all its identifier values are accurate.

v) Mismember non-identifier: a non-identifier attribute value is defined as mismember if, and only if, at least one of the attribute values composing the identifier is inaccurate. Note that this applies regardless of the accurate, inaccurate, or null value of the non-identifier attribute: $[ ( \nu _ { q j }  \{ \mathrm { A } , \mathrm { I } , $ $\mathbf { N } \mathfrak { Y } ) \wedge ( \exists \ \nu _ { k i }  \mathrm { I } ) ] \Rightarrow ( \nu _ { q j }  \mathbf { M } ) , i \in \{ 1 , 2 , \dotsc , m \}$ $j \in \left\{ 1 , 2 , \ldots , n \right\}$ . An example of mismember nonidentifier attribute value is Sales\_Amt = 6000 that one of its identifier values (i.e., Prod\_ID = ‘P2’) is inaccurate. The sales amount, although accurate, has been for another product but was erroneously recorded for $\cdot \mathrm { P } 2 ^ { \bullet }$ . Since product $\cdot \mathrm { P } 2 ^ { \bullet }$ did not have a 6000 sales in store $^ { \cdot } \mathrm { S } 5 ^ { \prime } \mathrm { o n } ^ { \cdot } 1 0 \mathrm { - s e p - } 0 4 ^ { \cdot }$ , the entire tuple does not belong to the relation, and, therefore, all the attribute values are mismembers.

vi) Incomplete non-identifier: a non-identifier attribute value is defined as incomplete if, and only if, the attribute value is an existential null and all the attribute values composing the identifier are accurate: $[ ( \nu _ { q j }  \mathrm { N } ) \land ( \forall \nu _ { k i }  \mathrm { A } ) ] { \Rightarrow } ( \nu _ { q j }  \mathrm { C } )$ 2 $i = \{ 1 , 2 , . . . , m \} , j \in \{ 1 , 2 , . . . , n \}$

An example of incomplete non-identifier attribute value is Sales\_Amt = NULL that has an existential null value (i.e., its actual value of 3000 exists but has not been recorded making it unavailable at the time of query execution) and all its identifier values are accurate.

Further, all attribute values (identifier and nonidentifier) in the incomplete data set $S _ { C }$ are by definition incomplete but accurate (e.g., Sales\_Amt = 5000 in Fig. 3).

Note that the above definitions are meaningful only for non-empty S. When S is empty $( \mathrm { i . e . , } | S | = 0 )$ , we have to only consider attributes and their values in $S _ { C }$ for our estimations. The estimation processes are given in the next section.

## 4. Estimations

It is easily seen that the existence of inaccurate, null, mismember, and incomplete attribute values have a direct impact on the aggregate values. For instance, consider the following query on the Sales table (Fig. 2):

SELECT SUM Sales Amt

FROM Sales

WHERE Prod ID <sup>d</sup>P1<sup>T</sup>:

The query returns 32 000 for the aggregate sum value. This, however, is not the true value because a) the inaccurate value 7500 deviates from the actual value of 9000; b) the mismember value 6000 contributes to this aggregate while it should not; c) the existential null value does not contribute to the sum while its true value of 3000 should; d) the values of 5000 and 8000 in the incomplete data set do not contribute to the sum while they should. Accounting for all the errors, the true aggregate sum value for this query is 43 500 which deviates about 27% from the query result.

It is, therefore, essential that the number of inaccurate, existential null, mismember, and incomplete values for each attribute be obtained in order to adjust the query result for the errors caused by these values. Auditing every single value in a database or data warehouse table that typically contain very large numbers of rows and attributes is expensive and impractical. Instead, sampling strategies can be used to estimate these errors as described next.

## 4.1. Sampling strategies

We differentiate between sampling schemes for the identifier and non-identifier attributes and explicitly assume that the sampled data can be verified for their actual values. Note that in a relational model, identifiers cannot take null values, and all sampling schemes are defined for non-empty S.

Further, in this study, we will focus on the point estimates that simplify our analysis. At the same time, we acknowledge that interval estimates could be very valuable in decision-making processes, but we leave them for future research.

## 4.1.1. Identifier attribute sampling

In order to estimate the number of mismembers, we draw a random sample without replacement from the set of identifier attributes of S and verify the number of accurate and inaccurate values; denoted by $n _ { k ; \mathrm { A } }$ and $n _ { k : \mathrm { I } } .$ respectively; in the sample as shown in Fig. 4.

Simple random sampling [20] is the most appropriate for our purpose because we have no a priori knowledge about the status of attribute values. Let |S| denote the cardinality of $S ;$ let $n _ { k }$ be the sample size; and let $s _ { k ; \mathrm { A } }$ be the total number of accurate identifiers in S that must be estimated. The maximum likelihood estimator (MLE) of

$$
\begin{array}{c} n _ {k} \\ \hline K (k _ {1},.., k _ {m}) \\ \hline \forall v _ {k i} \leftarrow A i \in \{1,..., m \} \\ \hline \exists v _ {k i} \leftarrow I i \in \{1,..., m \} \\ \hline \end{array} \text {   mismembers   }
$$

Fig. 4. Identifier sampling.

<table><tr><td> $K(k_1,..,k_m)$ </td><td> $q_i \quad i \in \{1,...,n\}$ </td></tr><tr><td rowspan="3"> $\forall v_{ki} \leftarrow A \quad i \in \{1,...,m\}$ </td><td> $v_{qi} \leftarrow A$  $\left. \begin{array}{l} \} n_{q:A} \\ \} n_{q:I} \\ \} n_{q:N} \end{array} \right.$ </td></tr><tr><td> $v_{qi} \leftarrow I$ </td></tr><tr><td> $v_{qi} \leftarrow N$ </td></tr><tr><td rowspan="3"> $\exists v_{ki} \leftarrow I \quad i \in \{1,...,m\}$ </td><td> $v_{qi} \leftarrow A$ </td></tr><tr><td> $v_{qi} \leftarrow I$ </td></tr><tr><td> $v_{qi} \leftarrow N$ </td></tr></table>

Fig. 5. Non-identifier sampling.

$s _ { k : \mathrm { A } } ,$ denoted by $\hat { s } _ { k : \mathrm { A } } ,$ is an integer that maximizes the probability distribution of the accurate identifiers in S. This probability follows a hypergeometric distribution given by:

$$
p (n _ {k: \mathrm{A}} = x) = \frac {\binom{s _ {k : \mathrm{A}}}{x} \binom{| S | - s _ {k : \mathrm{A}}}{n _ {k} - x}}{\binom{| S |}{n _ {k}}}\tag{1}
$$

Using the closed form expression ([10], p. 262) we have:

$$
\hat {s} _ {k: \mathrm{A}} = \left\lceil \frac {n _ {k : \mathrm{A}} (| S | + 1)}{n _ {k}} \right\rceil\tag{2}
$$

where ⌈·⌉ is the ceiling for any given number. The MLE for the inaccurate identifiers in S (i.e., mismembers), denoted by $\hat { s } _ { k : \mathrm { M } }$ is then given by:

$$
\hat {s} _ {k: \mathrm{M}} = | S | - \hat {s} _ {k: \mathrm{A}} = | S | - \left\lceil \frac {n _ {k : \mathrm{A}} (| S | + 1)}{n _ {k}} \right\rceil .\tag{3}
$$

## 4.1.2. Non-identifier attribute sampling

We separately sample each non-identifier attribute of interest that the aggregate functions operate on. In this sampling scheme, as shown in Fig. 5, the corresponding identifier values are also retrieved since the nonidentifier attribute values find their meaning only in conjunction with their corresponding identifiers.

The total number of mismembers for each nonidentifier attribute would be equal to $\hat { s } _ { k : \mathrm { M } } .$ Let $n _ { \mathrm { q } }$ be the sample size taken from the values of a non-identifier attribute $q _ { i } \in \mathcal { Q } .$ . Let $n _ { q : \mathrm { A } } , n _ { q : \mathrm { I } }$ , and $n _ { q : \mathrm { N } }$ be the verified numbers of accurate, inaccurate, and existential null values in the sample, respectively. Let $s _ { q : \mathrm { A } } , s _ { q : \mathrm { I } } .$ , and $s _ { q : \mathrm { N } }$ be the total numbers of accurate, inaccurate, and existential null values in $q _ { \mathrm { i } }$ with an accurate identifier that need to be estimated. Their MLEs, denoted by $\hat { s } _ { q : \mathrm { A } } ,$ $\hat { s } _ { q : \mathrm { I } } ,$ , and $\hat { s } _ { q : \mathrm { N } } ,$ are integers that maximize the probability distribution of these attribute value types in q . This probability function follows a multivariate hypergeometric distribution given by

$$
p \big (n _ {q: \mathrm{A}} = x, n _ {q: \mathrm{I}} = y, n _ {q: \mathrm{N}} = z \big) = \frac {\binom {S _ {q : \mathrm{A}}} {x} \binom {S _ {q : \mathrm{I}}} {y} \binom {S _ {q : \mathrm{N}}} {z}}{\binom {\hat {S} _ {k : \mathrm{A}}} {n _ {q}}}\tag{4}
$$

There are no closed form expressions for $\hat { s } _ { q : \mathrm { A } } , \hat { s } _ { q : \mathrm { I } } .$ , and $\hat { s } _ { q : \mathrm { N } }$ . They can be evaluated iteratively by substituting the values of $n _ { q : \mathrm { A } } , n _ { q : \mathrm { I } }$ , and $n _ { q : \mathrm { N } }$ within their respective ranges, in expression (4) and determining which combination produces the largest value for the probability. The iterative process could be inefficient when these numbers are large. A good approximation of MLEs can be obtained by assuming that $s _ { q : \mathrm { A } } , s _ { q : \mathrm { I } }$ , and $s _ { q : \mathrm { N } }$ are integral multiples of $n _ { \mathrm { q } } \left[ 2 \right]$ . Their estimates are then given by

$$
\begin{array}{l}\hat {s} _ {q: \mathrm{A}} = \left\lceil \frac {n _ {q : \mathrm{A}} (\hat {s} _ {k : \mathrm{A}} + 1)}{n _ {q}} \right\rceil ;\\\hat {s} _ {q: \mathrm{I}} = \left\lceil \frac {n _ {q : \mathrm{I}} (\hat {s} _ {k : \mathrm{A}} + 1)}{n _ {q}} \right\rceil ; \quad \hat {s} _ {q: \mathrm{N}} = \left\lceil \frac {n _ {q : \mathrm{N}} (\hat {s} _ {k : \mathrm{A}} + 1)}{n _ {q}} \right\rceil .\end{array}\tag{5}
$$

## 4.1.3. Incomplete data sampling and adjustments

Unlike the stored data, the incomplete data set is not directly available for sampling purposes. Therefore, obtaining a close estimation for the incomplete data could be a challenging and non-trivial task. One suggested method is to obtain a data sample of the real world entity (i.e., T) and determine what percentage of it has been captured into S [16,18]. This method may not be practical if access to data outside the database is limited. We propose using the Simple-Recapture sampling method ([27], p. 234) to obtain an estimation for the size of the incomplete data set $S _ { \mathrm { { C } } } .$ . For this purpose, we assume that |S| tuples have been sampled from T and $\hat { s } _ { k : \mathrm { A } }$ is obtained and this sampling has been done twice. The MLE estimates for |T| and $| S _ { C } |$ are then given by:

$$
| \hat {T} | = \frac {| S | ^ {2}}{\hat {s} _ {k : \mathrm{A}}}; \quad | \hat {S} _ {\mathrm{C}} | = | \hat {T} | - | S | - \hat {s} _ {k: \mathrm{M}} = \frac {| S | ^ {2}}{\hat {s} _ {k : \mathrm{A}}} - \hat {s} _ {k: \mathrm{A}}\tag{6}
$$

For instance, if $\vert { \cal S } \vert { = } 1 0 0 0 0$ and $\hat { s } _ { k : \mathrm { A } } = 9 5 0 0$ , then $| \hat { S } _ { \bf C } | =$ 1026. Further, note that the inaccurate, existential null, and mismember values found in the samples can be corrected. This correction will affect the estimated likelihoods in the entire data set. Standard procedures exist to make such adjustments ([13], p. 691). With the estimated values of attribute types, we now can estimate the quality profiles (accuracy and completeness) of the aggregate functions as described in next sections.

## 4.2. COUNT

The COUNT function gives the number of tuples in S or the number of not-null values in a single attribute. Without considering the mismembers and the incomplete data set; the COUNT function gives |S|. When COUNT is used to retrieve the cardinality of S or it functions on one of the identifier attributes, the true COUNT, denoted by $\mathrm { C O U N T } ^ { T } ,$ , is the number of tuples with accurate identifiers plus the cardinality of the incomplete set:

$$
\mathrm{COUNT} ^ {T} (k _ {i}) = \hat {s} _ {k: \mathrm{A}} + | \hat {S} _ {\mathrm{C}} |\tag{7}
$$

When COUNT operates on one of the non-identifier attributes, the true count is the sum of accurate, inaccurate, and incomplete (i.e., existential nulls and incomplete data set) values:

$$
\mathbf {C O U N T} ^ {T} (q _ {i}) = \hat {s} _ {q: \mathrm{A}} + \hat {s} _ {q: \mathrm{I}} + \hat {s} _ {q: \mathrm{N}} + | \hat {S} _ {\mathrm{C}} |.\tag{8}
$$

## 4.3. MAX and MIN

The MAX function operates on a single attribute or a substring. When MAX operates on one of the identifier attributes, then the probability that the returned value is accurate is given by

$$
p (\operatorname{MAX} (k _ {i}) \leftarrow A) = \left\{ \begin{array}{l l} \frac {\hat {s} _ {k : \mathrm{A}}}{| S |} & \text { for } | S | \neq 0 \\ 0 & \text { for } | S | = 0 \end{array} \right.\tag{9}
$$

The probability that the true MAX value is in the incomplete data set is given by

$$
\begin{array}{l l} p (\text { MAX } (k _ {i}) \in S _ {\text { C }}) \\ = \left\{ \begin{array}{l l} \frac {| \hat {S} _ {\text { C }} |}{| \hat {S} _ {\text { C }} | + \hat {s} _ {k : \text { A }}} & \text { for   } | S | \neq 0 \\ 1 & \text { for   } | S | = 0 \end{array} \right. \end{array}\tag{10}
$$

When MAX function operates on a non-identifier attribute, the probability of an accurate returned value is

$$
p (\operatorname{MAX} (q _ {i}) \leftarrow A) = \left\{ \begin{array}{l l} \frac {\hat {s} _ {q : \mathrm{A}}}{| S |} & \text { for } | S | \neq 0 \\ 0 & \text { for } | S | = 0 \end{array} \right.\tag{11}
$$

and the probability that the true MAX value is replaced by an existential null or is in the incomplete data set is given by

$$
\begin{array}{l} p ((\operatorname{MAX} (q _ {i}) \leftarrow N) \lor (\operatorname{MAX} (q _ {i}) \in S _ {\mathrm{C}})) \\ = \left\{ \begin{array}{l l} \frac {| \hat {S} _ {\mathrm{C}} | + \hat {s} _ {q : \mathrm{N}}}{| \hat {S} _ {\mathrm{C}} | + \hat {s} _ {k : \mathrm{A}}} & \text { for } | S | \neq 0 \\ 1 & \text { for } | S | = 0 \end{array} \right. \end{array}\tag{12}
$$

Analogously, all the expressions (9)–(12) apply for the MIN function.

## 4.4. SUM

The distributions of attribute value types within their underlying domains affect the estimation of the true SUM value. The attribute value types could have a uniform or skewed distribution depending on the errorgenerating processes. We make the following assumptions about the error-generating processes:

Assumption 1. The error-generating processes that cause errors in values of each attribute are not systematic. This assumption implies that we do not have a priori knowledge about causes that produce errors in data because if we had such knowledge then we would simply eliminate them.

Assumption 2. On average, the data loads, updates, and refreshing cycles do not affect the proportions of value types in attributes. We mean that the errorgenerating processes would produce the same proportions of errors each time data are captured in the relation. In other words, we do not expect the error proportions to become different unless we have specific knowledge about change or elimination of the error-generating processes.

Next, we discuss the estimation of the true SUM for both uniform and skewed distributions of the attribute value type.

## 4.4.1. Uniform attribute value distribution

In order to estimate the true sum value on a particular attribute (either identifier or non-identifier), we obtain a representative sample of attribute values and verify the average of accurate values. This average will vary each time we repeat the sampling. Therefore, we repeat the sampling enough times so that the average values will have a Normal distribution according to the central limit theorem. Then, the average of all averages will be a converged value to be used as the average of accurate values. We denote the converged average accurate values for the identifier and non-identifier attributes by $\overline { { \lambda } } _ { k : \mathrm { A } }$ and $\overline { { \lambda } } _ { q : \mathrm { A } } ,$ , respectively.

When SUM operates on an identifier attribute, the values in the incomplete data set are not directly available and not contributing to the sum as they should. Therefore, we use $\overline { { \lambda } } _ { k : \mathrm { A } }$ for each value in the incomplete data set and the estimated true sum will be given by

$$
\operatorname{SUM} ^ {T} \left(k _ {i}\right) = \bar {\lambda} _ {k: \mathrm{A}} \left(\hat {s} _ {k: \mathrm{A}} + | \hat {S} _ {\mathrm{C}} |\right).\tag{13}
$$

Similarly, when SUM operates on a non-identifier attribute, the estimate for the true SUM value can be obtained by substituting the inaccurate, existential nulls and incomplete values with $\overline { { \lambda } } _ { q : \mathrm { A } }$ which is given by

$$
\mathrm{SUM} ^ {T} (q _ {i}) = \bar {\lambda} _ {q: \mathrm{A}} \big (\hat {s} _ {q: \mathrm{A}} + \hat {s} _ {q: \mathrm{I}} + \hat {s} _ {q: \mathrm{N}} + | \hat {S} _ {\mathrm{C}} | \big).\tag{14}
$$

## 4.4.2. Skewed attribute value distribution

In cases that sampling and verification of data confirms a skewed distribution of the attribute value types, the Zipf general law [14] can be applied to estimate the average of accurate values in the sample. The occurrence probability of ith ranked value is given by $\scriptstyle { p _ { i } = \alpha / ( i ^ { z } ) }$ , where α is a constant factor and Z is the distribution skew. Let the frequencies of the first and second ranked accurate values in the sample be $\phi _ { 1 }$ and $\phi _ { 2 } ,$ respectively. Then, α and Z are imputed [14] as $\scriptstyle { \alpha = \phi _ { 1 } / n }$ where n is the sample size and $Z { = } \log _ { 2 } ( \phi _ { 1 } / \phi _ { 2 } )$ Values with $p _ { i } \ge \theta$ , where θ is a predefined threshold, are considered to calculate $\overline { { \lambda } } _ { k : \mathrm { A } }$ and $\overline { { \lambda } } _ { q : \mathrm { A } }$

## 4.5. AVERAGE

The estimated true value returned by the AVERAGE function on an identifier (non-identifier) attribute is given by the ratio of the estimated true SUM and true COUNT:

$$
\text { AVERAGE } ^ {T} (k _ {i}) = \frac {\text { SUM } ^ {T} (k _ {i})}{\text { COUNT } ^ {T} (k _ {i})} = \bar {\lambda} _ {k: \text { A }}\tag{15}
$$

$$
\text { AVERAGE } ^ {T} (q _ {i}) = \frac {\text { SUM } ^ {T} (q _ {i})}{\text { COUNT } ^ {T} (q _ {i})} = \bar {\lambda} _ {q: \text { A }}.\tag{16}
$$

## 5. Numeric examples with Monte Carlo simulation

We demonstrate our methodology by an example using Monte Carlo simulation. We consider a conceptual relation T and its stored and incomplete data sets to be similar to those shown in Figs. 1–3. We populated T with 5000 tuples and S with 5150 tuples (implying 250 mismembers), and included 500 tuples in $S _ { \mathrm { C } }$ . The values of Sales\_Amt for $\cdot _ { \mathrm { P l } } ,$ were generated using a random number generator and took their values uniformly from a range of [1000,10 000].

We ran the following query, SELECT SUM(Sales\_- Amt) FROM Sales WHERE Prod\_ID =‘P1’, on T where the returned actual sum was 29,926,754. Next, we randomly selected and altered 500 values of Sales\_Amt in S and labeled them as inaccurate, randomly selected 250 values and marked them as mismembers, and converted 100 values to existential nulls. The size of random sample of values to be taken from S was calculated to be 462 ([27], p. 44) but we chose to sample a round number of 500 values and repeated the sampling 100 times. The average number of values with accurate identifiers in the sample was 473. The converged averages of accurate, inaccurate, and existential nulls for Sales\_Amt values in the samples were found to be 424, 40, and 10, respectively. Their maximum likelihood estimates were calculated to be 4123, 467, and 87 which correspond to 0.96, 0.93, and 0.87 of the actual numbers of these value types in S. The averages of accurate values were found to be in the range of [5064,6050] and the converged average over this range was 5540. Fig. 6 shows the sample averages.

Using 5540 for the inaccurate, existential nulls, and incompletes and excluding the mismembers, the estimated sum value was 28,680,580 which is about 0.96 of the actual value. The mismembers and incomplete data set have the greatest impact on the sum value and, therefore, on the efficiency of the estimation. The greater the number of mismembers and incomplete data set, the more useful the estimated true value of the sum becomes because the returned sum by query does not reflect the impact of mismember and incomplete values, but the estimated value does.

We also simulated a skewed distribution of values for Sales\_Amt. The numbers of tuples in $S , S _ { \mathrm { C } } ,$ the sample size and number of samplings, and randomly altered inaccurate, mismember, and existential null values were the same as the previous simulation. We used a patterned random number generator which gave us control on producing a skewed distribution for the data values in the range of [1000, 10000]. The numbers in the pattern range [4000,6000] were generated 10 times more than other numbers to simulate the skew. The actual sum returned by the query was 32,745,242.

![](/api/attachments/XHFDVZ5Q/fulltext/images/d823fbeb2caa7cfe58e671de261b6ebee419aed4a9403cd824a6f3f3e45a6f90.jpg)  
Fig. 6. Sample averages over accurate values.

<table><tr><td> $i^{th}$  Rank</td><td> $p_i$ </td><td>Average Values</td></tr><tr><td>1</td><td>0.37</td><td>6541</td></tr><tr><td>2</td><td>0.27</td><td>5589</td></tr><tr><td>3</td><td>0.22</td><td>4337</td></tr><tr><td>4</td><td>0.19</td><td>5229</td></tr><tr><td>5</td><td>0.18</td><td>5667</td></tr><tr><td>6</td><td>0.16</td><td>6103</td></tr><tr><td>7</td><td>0.15</td><td>4814</td></tr><tr><td>8</td><td>0.14</td><td>5362</td></tr><tr><td>9</td><td>0.13</td><td>6875</td></tr><tr><td>10</td><td>0.12</td><td>4771</td></tr><tr><td colspan="3"> $p_i \geq 0.20 \rightarrow \overline{\lambda}_{q:A} = 5489$  $p_i \geq 0.15 \rightarrow \overline{\lambda}_{q:A} = 5569$ </td></tr></table>

Fig. 7. The Zipf ranks and their corresponding average values.

The average frequencies of the top 2 rankings of accurate values in the sample were $\bar { \phi } _ { 1 } = 1 8 3$ and $\bar { \phi } _ { 2 } = 1 1 6$ which gave $\overline { { \alpha } } = 1 8 3 / 5 0 0 = 0 . 3 7$ and $\scriptstyle { \overline { { Z } } } = \log _ { 2 }$ $( 1 8 3 / 1 1 6 ) { = } 0 . 4 6$ . The first 10 ranked average values are given in Fig. 7.

Further we set a threshold of 0.20 (i.e., $p _ { i } { \ge } 0 . 2 0 )$ that led to selection of top 3 values with probabilities of occurrence greater than the threshold. The average of these values was $\overline { { \lambda } } _ { q : \mathrm { A } } = 5 4 8 9$

Substituting 5489 for the inaccurate, nulls, and incompletes, the estimated sum was 28,416,553 which is about 0.87 of the actual value. With $p _ { i } 2 0 . 1 5 $ , the estimated sum was 28,828,494 which is 0.88 of the actual sum implying that lower $p _ { i }$ does not lead to more drastically efficient estimations. The estimations in case of the skewed distribution of data values seemed to be less efficient than those for the uniform distribution but still acceptable for all practical purposes demonstrating the usefulness of our metrics.

## 6. Conclusions and future research

In this work, we have argued that aggregated information used by managers in their decision making processes could suffer from data errors which make an impact on decision quality. We have provided a framework for formal definitions of attribute value types (i.e., accurate, inaccurate, mismember, and incomplete) within the relational data model. Then, we presented sampling strategies to determine the maximum likelihood estimates of these value types in the entire data population residing in databases or data warehouses. The maximum likelihoods estimates were used in our metrics to estimate the true values of scalars returned by the relational aggregate functions. Finally, we demonstrated our methodology with numerical examples using Monte Carlo simulations. The simulation results show that our estimations of the true values are efficient enough for most practical purposes.

Our study considered unbiased point estimates to derive the quality metrics but it would also be interesting to use interval estimates that provide the standard deviation for the sampled averages and investigate their effects on the returned scalar values. This study can further be extended to estimate the aggregations returned by the widely used Group By clause, partial sum, and the OLAP functions such as Roll Up and Drill Down.

## References

[1] D.P. Ballou, H.L. Pazer, R.Y. Wang, G.K. Tayi, Modeling information manufacturing systems to determine information product quality, Management Science 44 (4) (1998) 462–484.

[2] P.J. Boland, F. Proschan, Schur convexity of the maximum likelihood function for the multivariate hypergeometric and multinomial distributions, Statistics & Probability Letters 5 (1987) 317–322.

[3] A.L.P. Chen, J. Chiu, F.S.C. Tseng, Evaluating aggregate operations over imprecise data, IEEE Transactions on Knowledge and Data Engineering 8 (2) (1996) 273–284.

[4] I.N. Chengalur-Smith, D.P. Ballou, H.L. Pazer, The impact of data quality information on decision making: an exploratory analysis, IEEE Transactions on Knowledge and Data Engineer ing 11 (6) (1999) 853–864.

[5] E.F. Codd, Missing information (applicable and inapplicable) in relational databases, SIGMOD Record 15 (4) (1986) 53–78.

[6] M.J. Eppler, Managing Information Quality, Springer Verlag, Berlin, 2003.

[7] G. Gottlob, R. Zicari, Closed world databases opened through null values. Proceedings of the 14th VLDB Conference, Los Angeles, California (1988) 50–61.

[8] W.C. Hou, G. Ozsoyoglu, Statistical estimators for aggregate relational algebra queries, ACM Transactions on Database Systems 16 (4) (1991) 600–654.

[9] T. Imielinski, W. Lipski, Incomplete information in relational databases, Journal of ACM 31 (4) (1984) 761–791.

[10] N.L. Johnson, S. Kotz, A.W. Kemp, Univariate Discrete Distributions, Wiley Interscience, 1993.

[11] B.D. Klein, D.L. Goodhue, G.B. Davis, Can humans detect errors in data? Impact of base rates, incentives, and goals, MIS Quarterly (1997 (June)) 169–194.

[12] H. Kon, S. Madnick, M.D. Seigel, Good answers from bad data: a data management strategy. Proceedings of Workshop on Information Technologies and Systems, Amsterdam, The Nether lands, 1995.

[13] D.C. Montgomery, Introduction to Statistical Quality Control, 4th ed., Wiley, 2001.

[14] A.Y. Montgomery, D.J. D'Souza, S.B. Lee, The Cost of Relational Algebraic Operations on Skewed Data: Estimates and Experiments, Information Processing, 1983, pp. 235–241.

[15] R.C. Morey, Estimating and improving the quality of information in the MIS, Communications of the ACM 25 (5) (1982) 337–342.

[16] A. Motro, Completeness information and its application to query processing. Proceedings of the 12th VLDB Conference, Kyoto, Japan (1986) 170–178.

[17] A. Motro, Integrity = Validity + Completeness, ACM Transactions on Database Systems 14 (4) (1989) 480–502.

[18] A. Motro, I. Rakov, Estimating the quality of databases. Proceedings of the Third International Conference on Flexible Query Answering Systems, Roskilde, Denmark (1998) 298–307.

[19] A. Ola, G. Ozsoyoglu, A family of incomplete relational database models. Proceedings of the 15th VLDB Conference, Amsterdam, Holland (1989) 23–31.

[20] F. Olken, D. Rotemt, Simple random sampling from relational databases. Proceedings of the 12th VLDB Conference, Kyoto, Japan (1986) 160–169.

[21] G. Ozsoyoglu, Z.M. Ozsoyoglu, V. Matos, Extending relational algebra and relational calculus with set-valued attributes and aggregate functions, ACM Transactions on Database Systems 12 (4) (1987) 566–592.

[22] A. Parssian, S. Sarkar, V.S. Jacob, Assessing data quality for information products: impact of selection, projection, and Cartesian product, Management Science 50 (7) (2004) 967–982.

[23] H. Prade, C. Testemale, Generalizing database relational algebra for the treatment of incomplete or uncertain information and vague queries, Information Sciences 34 (1984) 115–143.

[24] M. Reddy, R.Y. Wang, Estimating Data Accuracy in a Federated Database Environment. Proceedings of 6th International Conference on Information Systems and Management of Data, Bombay, India, (1995) 115–134.

[25] R. Reiter, On closed world databases, in: H. Gallaire, J. Minker (Eds.), Logic and Databases, Plenum Press, 1978, pp. 55–76.

[26] G. Shankaranarayan, M. Ziad, R.Y. Wang, Managing data quality in dynamic decision environments: an information product approach, Journal of Database Management 14 (4) (2003) 14–32.

[27] S.K. Thomson, Sampling, 2nd ed., Wiley Interscience, New York, 2002.

[28] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11) (1996) 86–95.

[29] R.Y. Wang, M.P. Reddy, H.B. Kon, Toward quality data: an attribute-based approach, Decision Support Systems 13 (1995) 349–372.

![](/api/attachments/XHFDVZ5Q/fulltext/images/5619981fb57d11c7800b0481ba84d7decc8ddbb69520d653e1e3393b45e25c0a.jpg)

Amir Parssian is an Assistant Professor of Information Systems in University of Illinois Springfield. He received his Ph.D. in Management Science and Information Systems from University of Texas at Dallas in 2002. His research interests are in Information Quality Assessment, Temporal Knowledge Management, Dynamics of Virtual Teams, Data Mining, and Health Informatics. He has also worked as an IT systems architect at various corporations. His publications have appeared

in Management Science, International Journal of Operations Management and Information Systems Education, as well as international conferences such as ICIS, IRMA, and ICIQ.
