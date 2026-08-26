---
otero_id: 8460
otero_key: "QXEDAA39"
title: "Exploring Attribute Correspondences Across Heterogeneous Databases by Mutual Information"
authors: "HUIMIN ZHAO; EHSAN S. SOOFI"
year: "2006"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222220411"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring Attribute Correspondences Across Heterogeneous Databases by Mutual Information

HUIMIN ZHAO & EHSAN S. SOOFI

To cite this article: HUIMIN ZHAO & EHSAN S. SOOFI (2006) Exploring Attribute Correspondences Across Heterogeneous Databases by Mutual Information, Journal of Management Information Systems, 22:4, 305-336

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222220411

![](/api/attachments/QXEDAA39/fulltext/images/5180098895e99d44254d8233f2e6c839bd9905c9659bd38a0cbf8c7e7114b531.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/QXEDAA39/fulltext/images/f8da225d43911df7d33a86e0022f64fae67d9e8472837ad43b54288f099eccb5.jpg)

Submit your article to this journal

![](/api/attachments/QXEDAA39/fulltext/images/eec7b0f791a06269e358d077ec2ee6c9f285fa84229d5e3c785e07a7d7d58eb7.jpg)

Article views: 2

![](/api/attachments/QXEDAA39/fulltext/images/ab435f521884430a93c77d8bdea2c4bbf4d01b5250ce550e09885de78fe312b4.jpg)

View related articles

# Exploring Attribute Correspondences Across Heterogeneous Databases by Mutual Information

HUIMIN ZHAO AND EHSAN S. SOOFI

HUIMIN ZHAO is an Assistant Professor of MIS at the School of Business Administration, University of Wisconsin–Milwaukee. He earned his Ph.D. in MIS from the University of Arizona. His current research interests are in the areas of data integration, data mining, and Web services. His research has been published in several journals, including IEEE Transactions on Knowledge and Data Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems, Journal of Database Management, Journal of Information Systems and e-Business Management, and International Journal of Web Services Research. He is a member of the Institute of Electrical and Electronics Engineers (IEEE), Association for Information Systems (AIS), and Information Resources Management Association (IRMA).

EHSAN S. SOOFI is a Professor of Management Science and Statistics at the School of Business Administration, University of Wisconsin–Milwaukee. He is a Fellow of the American Statistical Association. His research focuses on measures that quantify informational value of data and developing statistical models. He has published in several journals, including the Journal of the American Statistical Association, Journal of the Royal Statistical Society, Biometrika, Journal of Econometrics, Operations Research, European Journal of Operational Research, IEEE Transactions on Information Theory, Journal of Applied Probability, Decision Sciences, and Marketing Science. He served as an Associate Editor of the Journal of the American Statistical Association (1990–2005), and is an Associate Editor of ENTROPY, An International Journal of Entropy and Information Studies (1999–present). He was a vice president of the International Association for Statistical Computing for 1999–2001 and the chair of Evaluation and Managing Committees of the highly prestigious Leonard J. Savage Thesis Awards 1992–2002.

ABSTRACT: Identifying attribute correspondences across heterogeneous databases is a critical and time-consuming step in integrating the databases. Past research has applied correlation analysis techniques to explore correspondences between attributes. These techniques, however, are appropriate for numeric attributes that are linearly related. This paper proposes an information-theoretic approach to exploring correspondences between attributes in heterogeneous databases. The proposed approach is applicable to character attributes, as well as to numeric attributes, regardless whether or not they are linearly related. It overcomes some serious shortcomings of previous approaches based on correlation analysis and has much broader applicability. The proposed procedure samples both matching and nonmatching pairs of records from the databases under consideration, applies matching functions to compare pairs of attributes, and then uses the mutual information to measure the dependency between a matching function as applied to a pair of attributes and the class (i.e., matching or nonmatching) of a pair of records. A high mutual information index implies a potential attribute correspondence, which is presented to the analyst for further evaluation. The paper also presents some empirical results demonstrating the utility of the proposed approach.

KEY WORDS AND PHRASES: attribute correspondence, attribute matching, composite information systems, database interoperability, heterogeneous databases, information theory, interorganizational systems, mutual information.

AS WE ARE CONTINUALLY BUILDING MORE DATABASES, there is accordingly a growing need for integrating these databases. Databases owned by different companies need to be integrated following mergers and acquisitions. Organizations that have developed a variety of operational databases in different sections over time need to integrate the isolated “data islands” into composite information systems (CIS) [34, 43] for strategic applications. Business partners within a value chain and other cooperating organizations need to exchange data across their system boundaries, resulting in interorganizational systems [2, 3, 18, 20, 56]. As an example, there are currently emergent needs in the United States for nationwide collaboration of massively distributed, autonomous, heterogeneous databases in the health-care and the homeland security domains [5, 26].

While modern organizations are increasingly facing challenges to integrate and effectively use the data scattered in various local systems, a recent research commentary called upon information systems (IS) researchers for more research of distributed and heterogeneous computing environments [38]. The demand for such research is also reflected in a survey of key issues in IS management [7]; a majority of the identified top issues directly relates to distributed and heterogeneous computing environments.

Determining semantic correspondences across heterogeneous databases is a prerequisite for successfully integrating the databases [46, 51], either physically (e.g., by consolidating local data sources into a data warehouse [42]) or logically (e.g., by building a wrapper/mediator system such as the context interchange system (COIN) [35]). Semantic correspondences exist on both the schema level and the instance level. Schemalevel correspondences consist of tables that represent the same real-world entity type and attributes that represent the same property about some entity type. Instance-level correspondences consist of records that represent the same entity in the real world. Understanding schema-level correspondences is especially critical for the local databases to effectively communicate with each other, just as users must understand the metadata [37] describing the schema of a database before they can appropriately interpret the instance data in the database [36]. Determining schema correspondences is also an important step in the view integration process [45] during database design, where multiple local schemas reflecting the perspectives of different user groups need to be integrated into a global schema [45]. In this paper, we propose a procedure for detecting attribute correspondences from heterogeneous databases. Much of the research in the IS discipline is characterized by two paradigms—behavioral science and design science [23]. This work falls into the design science paradigm.

It is well known that manually determining attribute correspondences across databases is very complex and time-consuming in large real-world database integration projects due to various kinds of semantic heterogeneities (e.g., synonyms and homonyms) among different databases [46]. For example, the MITRE Corporation integrated four heterogeneous databases for the U.S. Air Force over a period of several years [11]. The number of attributes in these databases ranged between 884 and 2,578. MITRE used two matching tools. An information retrieval tool, called DELTA, was used to compare the textual descriptions of the attributes. A clustering tool, called SemInt, was used to cluster the attributes based on several metadata (properties of the attributes, such as data types, length of the attribute, and univariate summary statistics for numeric attributes and string length for textual attributes). A tremendous amount of time and effort was consumed in determining semantically corresponding attributes across databases. But using these tools consumed less time than reviewing their results manually. However, since neither of these tools utilized actual attribute values, their results were very rough. Automated procedures that utilize actual attribute values and can make more specific recommendations are therefore desirable to further reduce the time and efforts for heterogeneous database integration.

Some researchers have proposed the use of correlation and regression analysis for exploring correspondences between numerical attributes of the same real-world entities in various databases [16, 17, 31]. It is well known that the correlation and regression analysis do not apply when some or all of the attributes under consideration are character type, and these methods perform best when the numerical variables are normally distributed. Consequently, the problem of exploring correspondence between character attributes, which prevail in real-world databases, has not yet been addressed. The objective of this paper is to propose a more general methodology, which is applicable to numerical and character attributes alike, and for the case of normally distributed variables corresponding to the correlation analysis.

More specifically, we propose a procedure that uses mutual information for exploring correspondences between attributes in heterogeneous databases. The mutual information between two (or more) variables measures the extent of dependency between them. Kang and Naughton [25] have used mutual information to measure the dependency between attributes within a database. We use mutual information to measure the dependency between record matching and the similarity of attributes across databases. Mutual information is invariant under any one-to-one transformations, including nonlinear transformations of numeric attributes and different coding schemes of categorical attributes (e.g., gender coded as “Male/Female” or “1/0”). The proposed approach poses no limitation in terms of the types (e.g., numeric and character) of attributes or the functional forms (e.g., linear) of the relationships among attributes. Therefore, it has a broader applicability than the correlation analysis and, for normally distributed variables, is a function of correlation only.

We assume that the databases under investigation share some corresponding records and that a set of matching and nonmatching record pairs can be obtained based on a common key, provided by domain experts, or identified during a record matching process [47]. The proposed procedure consists of three steps:

1. a set of matching and nonmatching pairs of records from two corresponding tables in two heterogeneous databases are sampled;

2. for each pair of attributes across the two tables, use an exact or approximate matching function to quantify the similarity of attribute values for each record pair in the sample; and

3. compute the mutual information between the class of record pairs (i.e., matching or nonmatching) and the attribute matching function value for each attribute pair.

A high mutual information index implies a potential attribute correspondence. Potential attribute correspondences are presented to the analyst for further evaluation. Detecting correspondences between numeric attributes or categorical attributes (i.e., attributes with just a few distinct values) can be simplified by directly computing the mutual information between the attributes using just matching record pairs in the sample, without using an attribute matching function.

## Related Work

SEVERAL APPROACHES TO DETECTING SCHEMA correspondences across heterogeneous databases have been proposed in the past. We classify these approaches into two categories—those comparing metadata and those comparing instance data.

The metadata approaches determine the degree of similarity between schema elements (i.e., tables and attributes) based on metadata, including names, textual descriptions, schematic specifications, statistics, and usage patterns, without investigating the actually stored data [57]. These approaches assume that the semantics of schema elements are adequately described by metadata. Linguistic techniques, such as fuzzy thesaurus [40], semantic dictionary, taxonomy [8, 52], conceptual graph, case grammar [1], and speech act theory [24], have been used to measure the naming similarity between schema elements. Heuristic formulae have been designed to compute the degree of similarity between schema elements, based on the names and schematic specifications of the elements [22, 33, 39, 44, 50]. Information retrieval techniques have been used to measure the degree of similarity between text documents of schema elements [6]. Clustering and classification techniques have also been used to group similar schema elements [14, 29, 54, 57] based on metadata.

The instance data approaches determine the degree of similarity between schema elements by investigating the data actually stored in the databases. These approaches assume that some corresponding records (i.e., records about the same real-world entities) can be extracted from the underlying databases and apply statistical analysis techniques such as correlation analysis to analyze the relationships among attributes based on the sample of corresponding records [16, 17, 31]. The corresponding records may be generated based on a common key, provided by domain experts, or identified during a record matching process [47].

In general, the approaches that rely on comparing metadata (attribute names, textual descriptions, schema specifications, data patterns, usage patterns, etc.) produce less accurate results due to various problems associated with the metadata [57]. Schema element names usually cannot completely capture the semantics of the elements. There are often opaque element names in database schemas [25]; ad hoc phrases and acronyms rather than single words are more commonly used to name schema elements. The meaning of a schema element changes as the associated business processes evolve; the current meaning of a schema element may be different from the originally intended meaning. Design documents are often outdated, incomplete, incorrect, ambiguous, or simply missing. Schematic specifications are correlated more with structures than with semantics; semantically similar concepts could often be modeled using different schematic specifications, whereas semantically different concepts could have similar schematic specifications. Usage data may not be maintained in legacy systems.

While approaches that compare instance data can potentially produce more accurate results, they are difficult to apply directly if a common key across the databases does not exist. In such situations, both techniques for comparing metadata and techniques for comparing instance data as well as techniques for identifying corresponding records [58] need to be combined in an iterative procedure to gradually improve the accuracy of the results [47]. Metadata can be investigated first to identify an initial set of corresponding schema elements, which is used as a basis for comparing records. Corresponding records identified using record matching techniques can then be used to evaluate attribute correspondences more rigorously. Improvement on one level (schema level or instance level) triggers further evaluation on the other level.

In a closely related work, Kang and Naughton [25] use mutual information to measure the attribute dependencies within each database and then identify potential corresponding attributes based on similarity of the entropy or dependency patterns across the databases using graph similarity measures. Such dependency graphs do not distinguish variables as corresponding and noncorresponding when entropies of the attributes are approximately equal and dependencies between the attributes are approximately the same. An extreme example of such cases would be the situation when the attributes are all unique based on the sample data, thus each variable is uniformly distributed, and the joint distribution of each pair of variables is also uniformly distributed. Then the entropies and mutual information are the same, irrespective of whether or not attributes being corresponding. In our proposed technique, we use the mutual information to measure the dependency between record matching and attribute matching functions applied to attributes across databases to identify potential corresponding attributes. This approach identifies corresponding attribute pairs as the ones that their matching functions have higher mutual information indices with the record matching function than that for noncorresponding pairs. The two procedures may be viewed as complementary in that Kang and Naughton’s is an information-theoretic clustering approach and ours is an information-theoretic discriminant analysis approach.

## University Property Example

WE WILL USE A REAL-WORLD CASE of heterogeneous databases for both illustrative and empirical evaluation purposes. In a large public university, two departments—the property management department and the surplus property office—have independently developed two databases for different operational purposes. The property management department manages all property assets owned by various departments of the university. When some department wants to dispose of an item, the item is delivered to the surplus property office, where the item is sold to another department or a public customer. Data about a property item are entered into the property management database (referred to as FFX) when the item is purchased and independently entered into the surplus database when the item is disposed.

The two databases partially overlap. There are nine tables in FFX and three tables in surplus. One of the tables in surplus, named INVMSTR, corresponds closely with one of the tables in FFX, named FFX\_ASSET; both tables store one record for each property item. Three additional tables in FFX, FFX\_ACCOUNT, FFX\_CLASS\_ CODE, and FFX\_MFG\_CODE, also contain data that correspond with data in INVMSTR. FFX\_ACCOUNT contains additional financial information about every property item. FFX\_CLASS\_CODE and FFX\_MFG\_CODE are reference tables, providing the class description and the manufacturer name of every property item. Therefore, INVMSTR corresponds with the join of FFX\_ASSET, FFX\_ACCOUNT, FFX\_CLASS\_CODE, and FFX\_MFG\_CODE. In the rest of the paper, we refer to the INVMSTR table of surplus as INV and the join of the four FFX tables as FFX.

The task is to identify the attributes in the two tables that represent the same realworld concept. There are 32 attributes in table INV and 115 attributes in table FFX. According to the domain experts of the two departments, 11 attributes in table INV correspond with 14 attributes in table FFX. An attribute in one table may correspond with multiple attributes in another table. For example, DESC in table INV corresponds with DESCN1, DESCN2, CLASS\_DESCN1, CLASS\_DESCN2, and CLASS\_DESCN3 in table FFX, although most of the values are missing for DESCN2, CLASS\_DESCN2, and CLASS\_DESCN3.

Tables 1 and 2 show some sample data of the two tables INV and FFX. Note that there are various inconsistencies across the two tables. Since correlation analysis used in the past research can adequately detect correspondences between numeric attributes (e.g., acquisition cost [INV.ACQCOST and FFX.TOTAL\_COST]), we focus on correspondences between character attributes in this paper. To save space, we present just the corresponding character attributes, excluding DESCN2, CLASS\_DESCN2, and CLASS\_DESCN3, which contain too many missing values.

Since the two databases have been independently designed by different people at different times for different purposes, not surprisingly, the metadata (name, description, schema specification, usage patterns, etc.) of the two databases are very different and hard to compare. Almost all attributes are named using abbreviations of phrases, and the abbreviations are very different between the two databases. FFX has an online dictionary that contains a text description of several lines for each attribute. However, there is no counterpart on the surplus side. A single person, the expert in the surplus office, is regarded as the authority in interpreting the meaning of every attribute. Although this expert has fortunately stayed in the surplus office throughout the history of the database, her own interpretation of the attributes has inevitably changed as the operational requirements change from time to time. Schema specifications in IBM IDMS (the system underlying the property management database) and Foxpro (the system underlying the surplus database) are very different. The data types are incompatible between the two systems. Keys or any other types of constraints are not specified on either database declaratively but, rather, are embedded in application programs or even manually enforced. The lengths of attributes usually have been designed to be much longer in surplus than in FFX, probably because Foxpro supports variable-length character strings. Neither of the two databases maintains an active audit trial.

<sub>.</sub> <sub>Exa</sub>m<sup>ples</sup> <sup>of</sup> <sup>Entries</sup> <sup>in</sup> <sup>Tab</sup>

<table><tr><td>A_TAG</td><td>SER</td><td>DESC</td><td>MODEL</td><td>MFG</td></tr><tr><td>A4494</td><td>111DF66</td><td>LAPTOP COMPUTER</td><td>ZWL286</td><td>ZENITH</td></tr><tr><td>A254</td><td>M11285QRDT</td><td>COMPUTER</td><td>B83LLB</td><td>APPLE</td></tr><tr><td>A9925</td><td>1GNGC26K2P</td><td>TRUCK, SUBURBAN</td><td>1993</td><td>CHEVROLET</td></tr><tr><td>A16538</td><td>321479</td><td>PHOTOCOPIER</td><td>227</td><td>SHARP</td></tr><tr><td>A137971</td><td>1FBJS31H8M</td><td>TABLE, TYPEWRITER</td><td>1991</td><td>FORD 1991</td></tr></table>

<table><tr><td>ASSET_NO</td><td>SERIAL_NO</td><td>CLASS_DESCN1</td><td>DESCN1</td><td>MFG_MODEL_NO</td><td>MFG_NAME</td></tr><tr><td>A4494</td><td>11DF665</td><td>COMPUTER/ DESKTOP-PC</td><td>MICRO-COMPUTER LAPTOP</td><td>WL2864</td><td>ZENITH RADIO CORP</td></tr><tr><td>A254</td><td>?</td><td>COMPUTER/ DESKTOP-PC</td><td>MICRO-COMPUTER</td><td>B83LLB</td><td>APPLE COMPUTER INC</td></tr><tr><td>A9925</td><td>1GNGC26 K2PJ35636</td><td>TRUCK/&lt; 1, GVW</td><td>UA497/G842AH-1993-GA</td><td>1993 SUBURBAN</td><td>CHEVROLET MOTOR GMC</td></tr><tr><td>A16538</td><td>321479</td><td>PHOTOCOPIER</td><td>COPIER W/PLATEN COVE</td><td>SF227</td><td>SHARP ELECTRONICS CORP</td></tr><tr><td>A137971</td><td>1FBJS31H8 MHA49494</td><td>TRUCK/&lt; 1, GVW</td><td>UA242/G785AB-1991-G</td><td>1991 S31</td><td>FORD MOTOR CO</td></tr><tr><td colspan="6">“?” indicates a missing value.</td></tr></table>

While it is difficult to compare the metadata of the two databases, there is a common key attribute, called A\_TAG in surplus and ASSET\_NO in FFX, which can determine the correspondences between records. Every property item owned by the university is tagged with such a unique identifier. Two records about the same property item should have the same tag number, whereas records about different items should have different tag numbers. At the time we took snapshots of the two databases, there were 13,365 records in table INV and 77,966 records in table FFX. There are 3,624 matching records across the two snapshot tables. The data are very “dirty,” especially in table INV, where even the tag number can be wrong for some records.

## Mutual Information

CONSIDER TWO SEMANTICALLY CORRESPONDING TABLES such as $T _ { \mathrm { 1 } } = \mathrm { I N V }$ and $T _ { 2 } =$ FFX, in two heterogeneous databases that contain some semantically matching records (i.e., records that represent the same real-world entities). There are often various types of data discrepancies across databases [32, 48]. There are incorrect data, phonetic errors, typographical errors, and different abbreviations in most operational databases. The degree of similarity (or distance) between the values of two attributes from heterogeneous databases can be measured by an attribute matching function.

More specifically, let $S = S ( X _ { 1 } , X _ { 2 } )$ denote an attribute matching function for comparing two values of two attributes in two tables. Attribute matching functions such as the simple equality comparison that are binary $( s \in \{ 0 , 1 \} )$ ) are referred to as exact. Attribute matching functions that map a pair of attribute values into the unit interval $( s \in [ 0 , 1 ] )$ are referred to as approximate. In this case, 1 indicates a perfect match between two attribute values and 0 indicates a complete mismatch.

For any pair of records drawn from $T _ { 1 }$ and $T _ { 2 } ,$ let Y denote the binary variable,

$$
Y = \left\{ \begin{array}{l l} 1 & \text { if   a   pair   of   records   in } T _ {1} \text { and } T _ {2} \text { is   matching }, \\ 0 & \text { otherwise }. \end{array} \right.
$$

Given a pair of attributes $X _ { 1 }$ and $X _ { 2 }$ from two heterogeneous databases, if the degree of similarity between the attributes has information about the class $Y$ (matching or nonmatching) of a record pair, it is likely that the two attributes $X _ { 1 }$ and $X _ { 2 }$ semantically correspond with the same real-world concept.

Comparison of the overall distribution of an attribute matching function with distribution of the attribute matching function for matching and nonmatching record pairs provides some information about the relationship between the attribute matching function and the record matching variable. The mutual information serves this purpose.

## Exact Attribute Matching

The overall distribution of an exact attribute matching function $( s \in \{ 0 , 1 \} )$ is the marginal distribution denoted by $p ( s )$ , and the conditional distributions of the attribute, given the values of $Y ,$ denoted by $p ( s \vert Y = 0 )$ and $p ( s | Y = 1 )$ ).

We measure the discrepancy between the distributions $p ( s )$ and $p ( s | Y = y ) , y = 0 ,$ , 1 by the Kullback–Leibler discrimination information function [28], given by

$$
K \left[ p (s | y), p (s) \right] = \sum_ {s} p (s | y) \log \frac {p (s | y)}{p (s)}.\tag{1}
$$

This measure is also known as the cross-entropy and relative entropy. It is a nonnegative function $K [ p ( s \vert y ) , p ( s ) ] \ge 0 ;$ ; equality holds if and only i $\mathrm { f } p ( s | y ) = p ( s )$ for all values of s; for properties and interpretations, see Kullback [27] and Soofi and Retzer [53].

The mutual information between the attribute matching function and the record matching variable is given by the average of $K [ f ( s | y ) , f ( s ) ]$ taken with respect to distribution of Y. A useful formula for the mutual information is

$$
. M (S; Y) = K \left[ p (s, y): p (s) p (y) \right] = \sum_ {y} \sum_ {s} p (s, y) \log \frac {p (s , y)}{p (s) p (y)}.\tag{2}
$$

It is well known that $M ( S ; Y ) \ge 0$ and the equality holds if and only if S and $Y$ are independent random variables.

We may construct a mutual information index as

$$
I (S; Y) = 1 - \frac {H (S | Y)}{H (Y)} = \frac {M (S ; Y)}{H (Y)},\tag{3}
$$

where $H ( Y )$ is the entropy. This index ranges from zero to one: $I ( S ; Y ) = 0$ if and only if the two variables are independent, and $I ( S ; Y ) = 1$ if and only if the two variables are functionally related in some form.

## Approximate Attribute Matching

Due to various types of data errors frequently found in real-world databases, exact matching may not be appropriate in comparing attribute values. Approximate comparisons should then be used to measure the degree of similarity between attribute values. Let an approximate attribute matching function map the degree of similarity between $X _ { 1 }$ and $X _ { 2 }$ to a number in the unit interval [0, 1], where $S ( X _ { 1 } , X _ { 2 } ) = 0$ indicates a complete mismatch and $S ( X _ { 1 } , X _ { 2 } ) = 1$ indicates a perfect match. For such case of approximate attribute matching function, S is a continuous variable having a probability density function $f ( s )$ and conditional probability density functions f(s|y), $y =$ 0,1. In this case, the information quantities are defined using Equations (1) and (2) with the probability functions $p ( s )$ and $p ( s \vert y )$ replaced with density functions $f ( s )$ and $f ( s \vert y )$ , and the summations over s replaced with integrals. The information quantities may also be computed for a pair of approximate attribute matching functions $S _ { 1 }$ and $S _ { 2 } .$ . In this case, all summations are replaced with integrals and all probability functions are replaced with density functions.

The interpretations and properties of the mutual information are the same for discrete and continuous random variables. However, the entropy of a continuous distribution can be negative. For this and some other technical reasons, the mutual information index for two continuous random variables $S _ { 1 }$ and $S _ { 2 }$ is computed by the following exponential transformation:

$$
I \left(S _ {1}; S _ {2}\right) = 1 - e ^ {- 2 M \left(S _ {1}; S _ {2}\right)}.\tag{4}
$$

As in the discrete case, $I ( S _ { 1 } ; S _ { 2 } ) = 0$ if and only if the two variables are independent. Also, $I ( S _ { 1 } ; S _ { 2 } ) = 1$ if and only if the two variables are functionally related, linearly or nonlinearly.

## Computation

For the discrete case, computation of all information quantities is simple. When the probability distributions $p ( y ) , p ( s | y ) , y = 0 , 1$ , and $p ( s )$ are known, the information quantities are at hand. When the probability distributions are not known, they may be easily estimated by the sample proportions. For example, let the numbers of matching and nonmatching records and attributes be as shown in Table 3. Then the estimates of probabilities are $p ( s , y ) = n _ { s y } / n , p ( s ) = n _ { s + } / n$ , and $p ( y ) = n _ { + y } / n$ , which can be used in Equation (2).

For the continuous case, the information quantities can be computed when the density functions are known. However, computing the mutual information may not always be easy. An easy case for computing mutual information is when two random variables, $S _ { 1 }$ and $S _ { 2 } ,$ have a bivariate normal distribution and correlation coefficient $\rho ( S _ { 1 } ; S _ { 2 } )$ . Then

$$
M \left(S _ {1}; S _ {2}\right) = - 0. 5 \log \left[ 1 - \rho^ {2} \left(S _ {1}; S _ {2}\right) \right]\tag{5}
$$

$$
I \left(S _ {1}; S _ {2}\right) = \rho^ {2} \left(S _ {1}; S _ {2}\right).\tag{6}
$$

Thus, for the bivariate normal case, the mutual information is a function of the correlation and the mutual information index is the same as the squared correlation due to the fact that the form of the functional relationship can only be linear.

Table 3. Numbers of Matching and Nonmatching Records and Attributes

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Y</td><td rowspan="2">Total</td></tr><tr><td>0</td><td>1</td></tr><tr><td rowspan="2">S</td><td>0</td><td> $n_{00}$ </td><td> $n_{01}$ </td><td> $n_{0+}$ </td></tr><tr><td>1</td><td> $n_{10}$ </td><td> $n_{11}$ </td><td> $n_{1+}$ </td></tr><tr><td>Total</td><td></td><td> $n_{+0}$ </td><td> $n_{+1}$ </td><td>n</td></tr></table>

Computing mutual information is also easy when the variables $S _ { 1 }$ and $S _ { 2 }$ are not normally distributed, but some transformations to normality are possible. An important property of the mutual information measures is invariance under one-to-one transformations of the variables. For example, when $S _ { 1 }$ and $S _ { 2 }$ are not bivariate normal variables, but $Z _ { 1 } = { \sqrt { S } } _ { 1 }$ and $Z _ { 2 } = \log { \cal S } _ { 2 }$ are normally distributed, then the invariance property implies that

$$
M \left(S _ {1}; S _ {2}\right) = M \left(Z _ {1}; Z _ {2}\right) = - 0. 5 \log \left[ 1 - \rho^ {2} \left(Z _ {1}; Z _ {2}\right) \right]\tag{7}
$$

$$
I \left(S _ {1}; S _ {2}\right) = I \left(Z _ {1}; Z _ {2}\right) = \rho^ {2} \left(Z _ {1}; Z _ {2}\right).\tag{8}
$$

However, the correlation coefficient is not invariant under nonlinear transformations, thus $\rho ( Z _ { 1 } ; Z _ { 2 } ) \neq \rho ( S _ { 1 } ; S _ { 2 } )$ . Usually the relationship between the record matching indicator and attribute matching function is not linear. Hence, the correlation coefficient is not useful, but the mutual information is an appropriate measure.

The mutual information between the record matching indicator Y and an approximate attribute matching function S may be computed using a histogram entropy estimate [19]. This procedure leads to a cross-tabulation and formula (2) where the variable s has several applicable categories.

## Mutual Information Between Attribute Matching Functions

Consider two attribute matching functions $S _ { 1 }$ and $S _ { 2 }$ . In general, $S _ { 1 }$ and $S _ { 2 }$ may be two different functions applied to the same attribute pair or the same function applied to two different attribute pairs. In the first case, $M ( S _ { 1 } ; S _ { 2 } )$ provides a measure of shared information about two attribute matching functions. In the second case, $M ( S _ { 1 } ; S _ { 2 } )$ 1 provides additional evidence for potential attribute correspondences.

When both $S _ { 1 }$ and $S _ { 2 }$ are exact attribute matching functions, formula (2) is directly applicable for computation of $M ( S _ { 1 } ; S _ { 2 } )$ . When one of $S _ { 1 }$ and $S _ { 2 }$ is an exact and the other is an approximate attribute matching function or when both $S _ { 1 }$ and $S _ { 2 }$ are approximate attribute matching functions, the histogram entropy estimate of Hall and Morton [19] leads to formula (2) where one or both variables have several categories, respectively.

## Application to the University Property Example

WE HAVE APPLIED THE PROPOSED METHODOLOGY in detecting attribute correspondences in the university property example. We estimate the mutual information between the degree of similarity (or distance) between two attributes and whether or not a pair of records matches. For this purpose, we need data from both matching and nonmatching record pairs. Such a sample of record pairs may be generated based on a common key, provided by domain experts, or identified during a record matching process.

We use four simple attribute matching functions, two exact and two approximate, for illustration and not for comparison of different matching functions. First, two attributes $X _ { 1 }$ and $X _ { 2 }$ in different databases can be compared by a simple equality,

$$
E Q \big (x _ {1}, x _ {2} \big) = \left\{ \begin{array}{l l} 1 & \text { if } x _ {1} = x _ {2}, \\ 0 & \text { otherwise }, \end{array} \right.\tag{9}
$$

where $x _ { 1 }$ and $x _ { 2 }$ are particular attribute values of two variables. For semantically corresponding records, $E Q ( x _ { 1 } , x _ { 2 } )$ will be 1 if the two databases share the same format and store accurate consistent data on semantically corresponding attributes.

If an attribute in a database is frequently recorded as a substring of a corresponding attribute in another database, we can compare the attributes using

$$
S U B \left(x _ {1}, x _ {2}\right) = \left\{ \begin{array}{l l} 1 & \text { if } x _ {1} \text { is   a   substring   of } x _ {2} \text { or } x _ {2} \text { is   a   substring   of } x _ {1}, \\ 0 & \text { otherwise. } \end{array} \right.\tag{10}
$$

Many string distance measures have been developed to account for spelling errors, such as insertion, deletion, transposition, and substitution of characters. One example is Levenshtein’s edit distance, which is defined as the minimum number of characters that need to be inserted into or deleted from one string to transform it into another string divided by the total number of characters in the two strings. More examples of string distance measures include Hamming distance, longest common substring, q-grams, and Soundex, to name a few [10, 55]. There are special algorithms that can match various types of abbreviations [41]. There are also semantic similarity measures for comparing words in standard taxonomy, thesauri, or ontology that can take synonyms, hyponyms/hypernyms, and acronyms into account [30, 33, 49]. However, note that the focus of this paper is not on developing or evaluating attribute matching functions. We therefore use only several simple attribute matching functions in this paper for illustration purposes.

We can define attribute matching functions based on such similarity measures. For example,

$$
E D I T \left(x _ {1}, x _ {2}\right) = 1 - \text { Levinshtein's   edit   distance   between } x _ {1} \text { and } x _ {2}.\tag{11}
$$

It is also possible to construct matching functions by combining multiple matching functions. For example,

$$
C O M B \left(x _ {1}, x _ {2}\right) = \left\{ \begin{array}{l l} 1 & \text { if } S U B \left(x _ {1}, x _ {2}\right) = 1, \\ E D I T \left(x _ {1}, x _ {2}\right) & \text { otherwise } \end{array} \right.\tag{12}
$$

is a simple combination. More complex combinations can be constructed as well.

Table 4 shows a portion of the data for the university property example. In this example, the common key across the two tables are INV.A\_TAG and FFX.ASSET\_ NO. We use all 3,624 matching record pairs and randomly sample an equal number of nonmatching record pairs. Our total sample size is therefore 7,248. The constructed record matching variable Y indicates whether a record pair is a matching (Y = 1) or nonmatching (Y = 0) pair.

In the university property example, there are many types of errors and discrepancies across the two databases. For example, as seen in Table 4, the serial number of the property item $\mathrm { ^ { 6 6 } A 4 4 9 4 ^ { , 3 } }$ is recorded as $ { ^ { \circ } } 1 1 1  { \mathrm { D F } } 6 6 ^ { \circ }$ in table INV and as “11DF665” in table FFX. Also, as was seen in Tables 1 and 2, for this item, the description is recorded as “LAPTOP COMPUTER” in table INV and as “COMPUTER/DESK-TOP-PC” in table FFX, the model is recoded as “ZWL286” in table INV and as “WL2864” in table FFX, and the manufacturer is recoded as “ZENITH” in table INV and as “ZENITH RADIO CORP” in table FFX.

Table 4 also shows the values of attribute matching functions EQ, SUB, EDIT, and COMB for the pair (SER, SERIAL\_NO), where the first attribute is from table INV and the second is from table FFX. As before, missing attribute values are shown by “?” We note that the values of the exact attribute matching functions EQ and SUB are all zero for the nonmatching pairs. In fact, this is the case for the entire data set of nonmatching pairs in the sample. However, not all values of these matching functions for the matching pairs are one. In this case, $p ( 1 | Y = 1 ) = 0 . 7 0$ for EQ(SER, SERIAL\_NO) and $p ( 1 | Y = 1 ) = 0 . 7 2$ for SUB(SER, SERIAL\_NO). For these attribute matching functions, the mutual information M(S; Y) can be easily computed using formula (2). For EQ(SER, SERIAL\_NO), we have M(S; $Y ) = 0 . 3 4$ , and formula (3) gives a mutual information index $I ( S ; Y ) = 0 . 4 9$ . For SUB(SER, SERIAL\_NO), the mutual information is slightly higher. These results indicate that the attribute pair (SER, SERIAL\_NO) is informative about record matching.

As can be seen in Table 4, the values of the approximate matching functions EDIT and COMB are much higher for the matching record pairs than for the nonmatching record pairs. Figure 1 shows the entire distributions of EDIT(SER, SERIAL\_NO) for the matching (solid) and nonmatching (dashed) record pairs. We note that the distribution for the matching record pairs is highly concentrated near 1 and the distribution for nonmatching record pairs is concentrated near 0. This configuration indicates that the attribute pair (SER, $\mathrm { S E R I A L \_ N O ) }$ is informative about the record matching. Since Figure 1 does not suggest any parametric distribution for the data, we compute an estimate of the mutual information between EDIT(SER, SERIAL\_NO) and the record matching variable using formula (2) with ten categories for s. This procedure gives an estimate $M ( S ; Y ) = 0 . 5 8$ . Then formula (4) gives mutual information index $I ( S ; Y ) =$ 0.68, which is relatively high. The distributions of COMB(SER, SERIAL\_NO) for the matching and nonmatching record pairs are also shown in Figure 1. These distributions are very similar to those for EDIT(SER, SERIAL\_NO) and yield similar mutual information index. Furthermore, the mutual information index between $S _ { 1 } =$ EDIT(SER, SERIAL\_NO) and $S _ { 2 } = C O M B ( S E R$ , SERIAL\_NO) is $I ( S _ { 1 } ; S _ { 2 } ) = 0 . 9 4$ which indicates the two attribute matching functions are quite similar. Since the results of COMB and EDIT were very similar in all cases, henceforth the results of COMB will not be reported.

<sub>bute</sub> M<sup>atching</sup> <sup>Functions</sup> <sup>Applied</sup> <sup>on</sup> <sup>the</sup> <sup>Sample</sup> <sup>of</sup>

<table><tr><td colspan="2">INV</td><td colspan="2">FFX</td><td colspan="5">Matching functions</td></tr><tr><td>A_TAG</td><td>SER</td><td>ASSET_NO</td><td>SERIAL_NO</td><td>Y</td><td>EQ</td><td>SUB</td><td>EDIT</td><td>COMB</td></tr><tr><td>A4494</td><td>111DF66</td><td>A4494</td><td>11DF665</td><td>1</td><td>0</td><td>0</td><td>0.71</td><td>0.71</td></tr><tr><td>A254</td><td>M11285QRDT</td><td>A254</td><td>?</td><td>1</td><td>F ?</td><td>F ?</td><td>F ?</td><td>F ?</td></tr><tr><td>A9925</td><td>1GNGC26K2P</td><td>A9925</td><td>1GNGC26K2PJ35636</td><td>1</td><td>0</td><td>1</td><td>0.83</td><td>1.00</td></tr><tr><td>A16538</td><td>321479</td><td>A16538</td><td>321479</td><td>1</td><td>1</td><td>1</td><td>1.00</td><td>1.00</td></tr><tr><td>A137971</td><td>1FBJS31H8M</td><td>A137971</td><td>1FBJS31H8MHA49494</td><td>1</td><td>0</td><td>1</td><td>0.83</td><td>1.00</td></tr><tr><td>A16538</td><td>321479</td><td>A137971</td><td>1FBJS31H8MHA49494</td><td>0</td><td>0</td><td>0</td><td>0.08</td><td>0.08</td></tr><tr><td>A254</td><td>M11285QRDT</td><td>A4494</td><td>11DF665</td><td>0</td><td>0</td><td>0</td><td>0.20</td><td>0.20</td></tr><tr><td>A254</td><td>M11285QRDT</td><td>A16538</td><td>321479</td><td>0</td><td>0</td><td>0</td><td>0.10</td><td>0.10</td></tr><tr><td>A4494</td><td>111DF66</td><td>A9925</td><td>1GNGC26K2PJ35636</td><td>0</td><td>0</td><td>0</td><td>0.17</td><td>0.17</td></tr><tr><td>A254</td><td>M11285QRDT</td><td>A4494</td><td>11DF665</td><td>0</td><td>0</td><td>0</td><td>0.20</td><td>0.20</td></tr><tr><td colspan="9">“?” indicates a missing value.</td></tr></table>

![](/api/attachments/QXEDAA39/fulltext/images/7010701cafd69098643148dc3a9ec179157c25bce1e90ae57a04ac86b903b930.jpg)  
a. EDIT(SER, SERIAL\_NO)

![](/api/attachments/QXEDAA39/fulltext/images/a76b978af258b79c8e46a19d78445be18e34403a61b8a14429107437d309a00b.jpg)  
b. COMB(SER, SERIAL\_NO)  
Figure 1. Distributions of EDIT(SER, SERIAL\_NO) and COMB(SER, SERIAL\_NO) for Matching (Solid) and Nonmatching (Dashed) Record Pairs

There are four other corresponding attribute pairs, (MODEL, MFG\_MODEL\_NO), (MFG, MFG\_NAME), (DESC, CLASS\_DESCN1), and (DESC, DESCN1), not shown in Table 4. Both MODEL and MFG\_MODEL\_NO describe the manufacturing model name of an item. Both MFG and MFG\_NAME are the manufacturer name of an item. DESC, DESCN1, and CLASS\_DESCN1 are all descriptions about a property item. Usually CLASS\_DESCN1 is more general than DESCN1. For example, the CLASS\_DESCN1 of an item is “COMPUTER/DESKTOP-PC” while the DESCN1 of the item is “486DX/2–50 CPU W/8MB.” For some items, however, these two attributes have identical values.

Figure 2 shows the graphs of distributions of EDIT for the aforementioned four corresponding attribute pairs for the matching (solid) and nonmatching (dashed) record pairs. As seen in the graphs, the distributions of EDIT(MODEL, MFG\_MODEL\_NO) and EDIT(MFG, MFG\_NAME) concentrate differently for the matching and nonmatching record pairs. Thus, these pairs of attributes are informative about the record matching. But the distributions of EDIT(DESC, CLASS\_DESCN1) and EDIT(DESC, DESCN1) are concentrated similarly for the matching and nonmatching record pairs. Thus, these pairs of attributes are not so informative about the record matching. Again, these graphs do not suggest any parametric distribution for the data, so the mutual information is estimated using formula (2) with ten categories for s.

Figure 3 shows the mutual information indices for all the attribute pairs, sorted by the magnitude of the indices for EDIT. From the figure, we can see that the five semantically corresponding attribute pairs confirmed by the domain experts, (SER,

![](/api/attachments/QXEDAA39/fulltext/images/ab372fb2949ff436687d8ff8b6b57f7fdcaffe98c00463a4e6c75e2de27acdc7.jpg)  
a. EDIT(MODEL, MFG\_MODEL\_NO)

![](/api/attachments/QXEDAA39/fulltext/images/0de8b03875589e19b2151e27cf34bbdc5e8acbb8913893b0276f325f760ee2ea.jpg)  
b. EDIT(MFG, MFG\_NAME)

![](/api/attachments/QXEDAA39/fulltext/images/b6be3215be4df729cf9bacff844fbe69d7d7d781b98f51d478018229a3d26063.jpg)  
c. EDIT(DESC, CLASS\_DESCN1)

![](/api/attachments/QXEDAA39/fulltext/images/9734c43958cb2878ac1d33d8e746ad341a807eebbf4723119312a938658a3011.jpg)  
d. EDIT(DESC, DESCN1)  
Figure 2. Distributions of EDIT for Four Corresponding Attribute Pairs for Matching (Solid) and Nonmatching (Dashed) Record Pairs

SERIAL\_NO), (MODEL, MFG\_MODEL\_NO), (MFG, MFG\_NAME), (DESC, CLASS\_DESCN1) and (DESC, DESCN1), are relatively more informative about record matching than all other pairs of attributes. The first three attribute pairs are much more informative than the other two pairs because the description attributes DESC, CLASS\_DESCN1, and DESCN1 are free texts for which the operators of the two databases can enter the values using their own words, resulting in large discrepancies. These results show that the proposed approach can identify attribute correspondences even in such “dirty” situations as this example. There are many data discrepancies across the two databases and many data errors. Even worse, the class of the sample also has errors because some of the tag numbers are wrong in the surplus database. Nevertheless, the approach still effectively ranks the five corresponding attribute pairs as the most likely corresponding ones.

As shown in Figure 3, the approximate attribute matching functions are more effective than exact matching functions in such “dirty” situations. While all four attribute matching functions correctly rank the five matching pairs at the top, the approximate attribute matching functions EDIT and COMB discriminate corresponding pairs from the rest better than the exact attribute matching functions, especially EQ. In such “dirty” situations, it is important to apply approximate matching methods to account for various types of data errors. The simple attribute matching function based on Levenshtein’s edit distance effectively reveals the attribute correspondences in this example. In a more complex and even dirtier situation, more sophisticated attribute matching functions that take into account synonyms, hyponyms/hypernyms, acronyms, abbreviations, similarly sounding names, nicknames, and even words from different languages can be used.

![](/api/attachments/QXEDAA39/fulltext/images/38494eb883318eabb42c49ae0a0bbb7f8ce95d943301bb0a50407ef82b15bb45.jpg)  
Figure 3. Mutual Information Indices Sorted for the Function EDIT

The type of figures like Figure 3 is useful for the analyst in the attribute correspondence identification process during large database integration projects. Instead of evaluating all 32 (INV) × 115 (FFX) attribute pairs simultaneously, the analyst can evaluate the most informative attribute pairs first and gradually evaluate less informative ones, until the mutual information index becomes very small, indicating that there are unlikely to be any more corresponding attribute pairs. In this case, only the first several (less than ten) attribute pairs are worth further evaluation. The proposed approach can thus assist the analyst in identifying potential attribute correspondences and reduce the amount of interaction among the analyst, the local database administrators, and the local experts needed to determine the correspondences. To reduce the sensitivity of the results to the attribute matching function S, multiple functions can be used and results cross-validated. In this case, the two approximate attribute matching functions EDIT and COMB yield very similar results.

Table 5 gives the mutual information indices between five attribute pairs with the attribute matching function $S = E D I T$ . The first column shows the mutual information indices between the record matching indicator Y and the attribute matching functions of each of the five pairs of attributes. The results show relatively large mutual information indices between the first three attribute pairs, which are also highly informative about record matching, thus providing more evidence that these attribute pairs are potentially corresponding ones. It is also interesting to note that there is high mutual information between two attribute pairs, (DESC, CLASS\_DESCN1) and (DESC, DESCN1), which are not so informative about record matching. This type of information analysis is especially useful for identifying such corresponding attribute pairs for which I(S;Y) is relatively small but the mutual information between them is large. The mutual information indices between the highly informative attribute pairs and those that are not so informative are relatively small.

## Further Analyses

THIS SECTION PRESENTS THE MUTUAL INFORMATION between the record matching variable and multiple attribute matching functions, and an approach for taking missing values into account in computation of mutual information. These quantities provide additional indication of potential attribute correspondences and are useful if the basic mutual information and mutual information index quantities we have described in the previous section do not provide the analyst with sufficient evidence. However, note that these quantities are computationally more expensive and should be selected with the trade-off between accuracy and efficiency in consideration.

## Multiple Mutual Information

The multiple mutual information between the record matching indicator Y and a set of attribute matching functions $( S _ { 1 } , S _ { 2 } , . . . . , S _ { p } )$ quantifies the amount of information about Y provided by $( S _ { 1 } , S _ { 2 } , . . . . , S _ { p } )$ jointly. This measure can be computed using the following chain rule formula:

$$
M \left(Y; S _ {1}, S _ {2},..., S _ {p}\right) = M \left(Y; S _ {1}\right) + M \left(Y; S _ {2} \mid S _ {1}\right) +... + M \left(Y; S _ {p} \mid S _ {1}, S _ {2},..., S _ {p - 1}\right),\tag{13}
$$

where $M ( Y ; ~ S _ { h } | S _ { 1 } , ~ S _ { 2 } , ~ . ~ . ~ . , ~ S _ { h - 1 } ) , ~ h = 1 , 2 , ~ . ~ . ~ . , p ,$ is the partial mutual information between Y and $S _ { h }$ beyond $S _ { 1 } , S _ { 2 } , . . . . , S _ { h - 1 }$

Table 6 summarizes the results of the mutual information functions $M ( Y ; S _ { i } )$ , where i is shown in a column; $M ( Y ; S _ { k } , S _ { i } )$ , where k is shown as a column label; and $M ( Y ; S _ { k }$

Table 5. Mutual Information Indices Between Five Attribute Pairs with $S = E D I T$

<table><tr><td rowspan="2">Attribute pair</td><td rowspan="2">i</td><td rowspan="2"> $I(Y; S_i)$ </td><td colspan="4"> $I(S_i; S_k)$ k</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>SER, SERIAL_NO</td><td>1</td><td>0.68</td><td></td><td></td><td></td><td></td></tr><tr><td>MODEL, MFG_MODEL_NO</td><td>2</td><td>0.60</td><td>0.62</td><td></td><td></td><td></td></tr><tr><td>MFG, MFG_NAME</td><td>3</td><td>0.51</td><td>0.52</td><td>0.48</td><td></td><td></td></tr><tr><td>DESC, CLASS_DESCN1</td><td>4</td><td>0.18</td><td>0.20</td><td>0.20</td><td>0.19</td><td></td></tr><tr><td>DESC, DESCN1</td><td>5</td><td>0.08</td><td>0.10</td><td>0.11</td><td>0.11</td><td>0.51</td></tr></table>

$S _ { j } , S _ { i } )$ , where $k , j$ is shown as a column label. The attribute matching function is $S =$ $E D I T .$ These quantities are computed based on the listwise deletion of cases for missing values of the attributes. Thus the estimated mutual information between the record matching variable and attribute pairs can be slightly different from those seen before. Table 6 shows the multiple mutual information quantities that involve the five semantically corresponding attribute pairs, that is, (SER, SERIAL\_NO), (MODEL, MFG\_MODEL\_NO), (MFG, MFG\_NAME), (DESC, CLASS\_DESCN1), and (DESC, DESCN1); these values were relatively higher than all other attribute pairs considered in this study. As can be seen from Table $^ { 6 , }$ the values of multiple mutual information $M ( Y ; S _ { k } , S _ { i } )$ are high when one of the first three attribute pairs is considered, but not so high otherwise, that is, $M ( Y ; S _ { 4 } , S _ { 5 } ) = 0 . 1 2$ . The values of $M ( Y ; S _ { k } , S _ { j }$ i6 S ) are all high because at least one of the first three attribute pairs are involved.

The quantities shown in Table 6 are sufficient for computing partial mutual information measures defined in Equation (13). The difference between the entries in column k and M(Y; S ) gives the partial mutual information $M ( Y ; S _ { k } | S _ { i } )$ . For example, M(Y; $S _ { 1 } | S _ { i } ) = 0 . 1 5 , 0 . 2 5 , 0 . 4 9 , 0 . 5 4 \mathrm { f o r } i = 2 , 3 , 4 , 5 .$ respectively. Thus, (SER, SERIAL\_NO) provides additional information about the record matching, and the additional amounts of information to the fourth and fifth attribute pairs are substantial. Noting that M(Y; $S _ { 1 } , S _ { 2 } ) = M ( Y ; S _ { 2 } , S _ { 1 } ) = 0 . 6 1$ , the partial mutual information $M ( Y ; S _ { 2 } | S _ { 1 } ) = 0 . 0 3$ . That is, the additional information about the record matching provided by (MODEL, MFG\_MODEL\_NO) is negligible. However, from the column $k = 2 .$ , we obtain M(Y; $S _ { 2 } | S _ { i } \rangle = 0 . 1 8 , 0 . 3 8 , 0 . 4 3 \mathrm { f o r } i = 3 , 4 , 5 ,$ which are not negligible amounts particularly for the last two pairs. Similarly, from the column $k = 3 .$ , we note that (MFG, MFG\_NAME) provides a substantial amount of information about the record matching in addition to the last two attribute pairs, (DESC, CLASS\_DESCN1) and (DESC, DESCN1). We also note that M(Y; $S _ { 4 } , \ S _ { 5 } ) = 0 . 1 2$ , which indicates (DESC, CLASS\_DESCN1) and (DESC, DESCN1) are neither singly nor jointly very informative about the record matching. Finally, the difference between the entries in column $k , j$ and $M ( Y ; S _ { k } , S _ { j } , S _ { i } )$ gives the partial mutual information for a third variable given the other two variables. For example, $M ( Y ; S _ { 3 } | S _ { 1 } , S _ { 2 } ) = 0 . 6 3 - 0 . 6 1 = 0 . 0 2 ;$ thus (MFG, MFG\_NAME) does not provide much information about the record matching over and above (SER, SERIAL\_NO) and (MODEL, MFG\_MODEL\_NO). However,

<sub>Multi</sub><sup>ple</sup> <sup>Mutual</sup> <sup>Information</sup> <sup>with</sup> <sup>S</sup>

<table><tr><td rowspan="2">Attribute pair</td><td rowspan="2">i</td><td rowspan="2"> $M(Y; S_i)$ </td><td colspan="4"> $M(Y; S_k, S_i)$  $k$ </td><td colspan="6"> $M(Y; S_k, S_j, S_i)$  $k, j$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>1, 2</td><td>1, 3</td><td>1, 4</td><td>2, 3</td><td>2, 4</td><td>3, 4</td></tr><tr><td>SER, SERIAL_NO</td><td>1</td><td>0.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MODEL, MFG_MODEL_NO</td><td>2</td><td>0.46</td><td>0.61</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MFG, MFG_NAME</td><td>3</td><td>0.36</td><td>0.61</td><td>0.54</td><td></td><td></td><td>0.63</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DESC, CLASS_DESCN1</td><td>4</td><td>0.11</td><td>0.60</td><td>0.49</td><td>0.41</td><td></td><td>0.63</td><td>0.63</td><td></td><td>0.58</td><td></td><td></td></tr><tr><td>DESC, DESCN1</td><td>5</td><td>0.05</td><td>0.59</td><td>0.48</td><td>0.39</td><td>0.12</td><td>0.63</td><td>0.63</td><td>0.61</td><td>0.57</td><td>0.51</td><td>0.43</td></tr></table>

$M ( Y ; S _ { 1 } | S _ { 4 } , S _ { 5 } ) = 0 . 6 1 - 0 . 1 2 = 0 . 4 9 $ that is, (SER, SERIAL\_NO) provides substantial contribution to information about the record matching over and above the last two attribute pairs (DESC, CLASS\_DESCN1) and (DESC, DESCN1). Multiple mutual information between the record matching indicator and more than three attribute pairs does not provide significant further evidence and thus is not presented.

## Missing Values

Real-world databases often contain missing values for some attributes for a variety of reasons, random or systematic. Systematically missing values may convey significant information. For example, in a medical database, whether a patient is recommended to take some tests has important information—may be as important as the actual results of the tests—about a doctor’s diagnosis.

An attribute may be missing in one or both tables under consideration. For the exact attribute matching case, the mutual information formula (2) can be extended to take missing values into account by treating different types of missing values (i.e., missing in one or both tables) as additional categories. A drawback of such an aggregated measure is that the effects of actual attribute matching values may be masked by missing values. For the approximate attribute matching case, such an aggregation creates technical difficulties associated with handling distributions that have continuous (actual attribute matching) and categorical (missing values) components.

A more elaborate procedure, which is applicable to both the exact and approximate attribute matching cases, can be developed using the additive decomposition property of entropy. Let V be the missing/nonmissing indicator,

$$
V = \left\{ \begin{array}{l l} 1 & \text { if   the   attribute   values   under   comparison   are   not   missing, } \\ 0 & \text { otherwise. } \end{array} \right.
$$

Let S be the regular nonmissing attribute matching value. Let W be an indicator of the events when an attribute is missing in one or both tables under consideration. W is a categorical variable with three possible values, indicating that neither of the two attribute values under comparison is missing, exactly one of them is missing, and both of them are missing, respectively. Let $S ^ { \prime }$ be the overall attribute matching function, missing or nonmissing,

$$
S ^ {\prime} = \left\{ \begin{array}{l l} S & \text { if } V = 1, \\ W & \text { otherwise }. \end{array} \right.
$$

Then, by the additive decomposition property of entropy, we have,

$$
M \left(S ^ {\prime}; Y\right) = M (V; Y) + P (V = 1) M (S; Y | V = 1) + P (V = 0) M (W; Y | V = 0),\tag{14}
$$

where $M ( V ; Y )$ is the mutual information between the missing/nonmissing indicator and the record matching indicator; $M ( S ; \thinspace Y | V = 1 )$ is the mutual information between the regular nonmissing attribute matching value and the record matching indicator, given that the attribute values are not missing; and M(W; $Y V = 0 )$ is the mutual information between the type of missing value and the record matching indicator, given that one or both of the attribute values are missing. $M ( V ; Y ) , M ( S ; Y | V = 1 )$ , and (W; Y|V = 0) can be computed using formula (2).

A small value of $M ( V ; Y )$ indicates that record matching is independent of whether attribute values are missing or not. In such cases, $M ( S ^ { \prime } ; Y )$ is approximately the mean value of $M ( S ; Y | V = 1 )$ and $M ( W ; Y | V = 0 )$ , weighted by the distribution of V. If some attribute values are missing randomly, the type of missing value has no information on record matching and $M ( W ; Y | V = 0 )$ will be small. For a pair of semantically corresponding attributes, $M ( S ; Y | V = 1 )$ may be large but masked by the small $M ( W ; Y | V =$ 0) in the aggregated measure $M ( S ^ { \prime } ; Y )$ . In such cases, discarding missing values provides better indication of potential attribute correspondences than using the aggregated measure $M ( S ^ { \prime } ; Y )$ . On the other hand, if there are many missing values and the missing values are due to systematic reasons, $M ( W ; Y | V = 0 )$ will be large—maybe even larger than M(S; $Y V = 1 )$ —and thus analyzing the effects of missing values becomes important. When it is unknown whether attribute values are missing due to random or systematic reasons, all three quantities, $M ( S ^ { \prime } ; Y ) , M ( S ; Y | V = 1 )$ , and $M ( W ;$ $Y V = 0 )$ , should be considered. A large value for any of the three measures indicates a potential attribute correspondence and should be reported to the analyst for further evaluation.

Table 7 summarizes the results for the three attribute pairs that are informative about record matching: (SER, SERIAL\_NO), (MODEL, MFD\_MODEL\_NO), and (MFG, MFG\_NAME). The percentages of missing values $P ( V = 0 )$ are substantial particularly for (SER, $\mathrm { S E R I A L \_ N O ) }$ and (MODEL, MFD\_MODEL\_NO). However, the values of M(V; Y) are close to zero for all three attribute pairs, indicating that missing cases are almost independent of the record matching. The values of $M ( W ;$ $Y V = 0 )$ are also very small, indicating that the type of missing cases (missing in one or both databases) are almost independent of the record matching, that is, the missing values are mainly due to random reasons. Also shown in Table 7 are the values of mutual information for nonmissing cases $M ( S ; Y | V = 1 )$ and for missing and nonmissing cases combined $M ( S ^ { \prime } ; Y )$ , with S = EQ, SUB, EDIT. The results indicate that nonmissing cases are more informative about record matching than the combined cases. The highest differences are seen when the percentages of missing values are large and for the approximate attribute matching function EDIT. Overall, since the random patterns of missing values mask the information content of the attribute pairs, discarding missing values (i.e., using $M ( S ; Y V = 1 )$ instead of M(S′; Y)) provides a more accurate picture of the potential dependencies between the corresponding attribute pairs and the record matching in this case.

## Empirical Evaluation

THIS SECTION REPORTS THE RESULTS of an empirical evaluation of the proposed technique using the entire two databases in the university property example. The two tables contain 77,966 and 13,365 records, of which 3,624 are matching. The two tables contain 115 and 32 attributes, of which 32 and 11 are character attributes. Among the 352 pairs of character attributes, there are eight corresponding pairs, including (SER, SERIAL\_NO), (MODEL, MFG\_MODEL\_NO), (MFG, MFG\_NAME), (DESC, CLASS\_DESCN1), (DESC, CLASS\_DESCN2), (DESC, DESCN1), (DESC, DESCN2), and (DESC, DESCN3).

Table 7. Mutual Information With and Without Considering Missing Values

<table><tr><td></td><td>SER, SERIAL_NO</td><td>MODEL, MFD_MODEL_NO</td><td>MFG, MFG_NAME</td></tr><tr><td> $P(V=0)$ </td><td>0.29</td><td>0.38</td><td>0.10</td></tr><tr><td> $M(V;Y)$ </td><td>0.00</td><td>0.01</td><td>0.00</td></tr><tr><td> $M(W;Y|V=0)$ </td><td>0.07</td><td>0.07</td><td>0.03</td></tr><tr><td colspan="4">EQ</td></tr><tr><td> $M(S;Y|V=1)$ </td><td>0.34</td><td>0.19</td><td>0.03</td></tr><tr><td> $M(S';Y)$ </td><td>0.26</td><td>0.15</td><td>0.03</td></tr><tr><td colspan="4">SUB</td></tr><tr><td> $M(S;Y|V=1)$ </td><td>0.35</td><td>0.24</td><td>0.24</td></tr><tr><td> $M(S';Y)$ </td><td>0.27</td><td>0.18</td><td>0.22</td></tr><tr><td colspan="4">EDIT</td></tr><tr><td> $M(S;Y|V=1)$ </td><td>0.58</td><td>0.45</td><td>0.35</td></tr><tr><td> $M(S';Y)$ </td><td>0.44</td><td>0.32</td><td>0.32</td></tr></table>

For the performance measure, we use average precision, defined as the average of the precision scores (i.e., proportion of the attribute pairs evaluated by a user that are indeed corresponding pairs) for all the corresponding attribute pairs. This measure has been widely used to report the accuracy of information retrieval systems [15, 21]. Average precision is considered as an overall composite measure that reflects a pair of measures, precision and recall [9], simultaneously [15, 21].

We report the results for attribute matching functions SUB and EDIT and for sample sizes n = 500, 1,000, . . ., 7,000. In each case, a balanced sample (an equal number of matching and nonmatching record pairs) was randomly generated. For each sample size, the process was replicated 500 times in order to examine the variation of the performance measure. For computing the average precision index, the attribute pairs are sorted based on the mutual information index between their attribute matching function values and the record matching indicator, and the attribute pairs with larger scores are considered more likely to be corresponding pairs.

Figure 4 shows the box plots of the distributions of the average precision for SUB and EDIT under various sample sizes. Average precision tends to increase as the sample size increases. The amount of improvement gradually reduces and becomes very small after the sample size reaches 3,000. The median of average precision for SUB approaches 72 percent, whereas that for EDIT approaches 78 percent.

Most of the errors are due to three attribute pairs that are extremely difficult to detect, including (DESC, CLASS\_DESCN2), (DESC, DESCN2), and (DESC,

<sub>lots</sub> <sub>of</sub> <sub>Distributions</sub> <sub>of</sub> <sub>Precision</sub> <sub>for</sub> <sub>SUB</sub> <sub>a</sub>n<sup>d</sup> <sup>EDIT</sup> <sup>for</sup> <sup>Variou</sup>  
![](/api/attachments/QXEDAA39/fulltext/images/0e4eebd0510833e24f3ce953db44654c7174f2829df25a9edfbe440b1cc166a4.jpg)

![](/api/attachments/QXEDAA39/fulltext/images/321449aa3bf9e5f5a7799d29cd94cdc0c95bfcc65f6d82d99ade577d3684f957.jpg)

DESCN3). While there is a single attribute (DESC) in INVMST that describes a property item, there are five attributes (CLASS\_DESCN1, CLASS\_DESCN2, DESCN1, DESCN2, and DESCN3) in FFX that describe a property item. However, large portions (95 percent, 24 percent, and 60 percent, respectively) of CLASS\_ DESCN2, DESCN2, and DESCN3 are missing. In addition, these attributes are used only as auxiliary attributes for CLASS\_DESCN1 and DESCN1; they are largely dissimilar to DESC. The three attribute pairs, (DESC, CLASS\_DESCN2), (DESC, DESCN2), and (DESC, DESCN3), are, at the best, very weak corresponding pairs.

We also measure the average precision for SUB and EDIT under various sample sizes, with the three attribute pairs, (DESC, CLASS\_DESCN2), (DESC, DESCN2), and (DESC, DESCN3), excluded. The average precision is largely improved and has much smaller variations. The average precision measures for SUB and EDIT both approach 100 percent.

To evaluate the efficiency and scalability of the proposed technique, we also record the running time. Most of the running time is spent on computing the attribute matching function values. The time spent on other steps, such as sampling and estimating the mutual information values, appears to be relatively negligible. We load the two tables into an Oracle database. The database server is a Dell PE1650 configured with a 1.26 GHz Pentium III CPU and 1 GB of RAM. The storage system is RAID5 with 3 SCSI 33.98 GB hard drives for a total capacity of 67.8 GB. The database management system (DBMS) is Oracle 10g. The client is a Dell Optiplex/GX260 workstation configured with a 2.27 GHz Pentium IV CPU and 512 MB of RAM. Both the server and the client run the Windows XP operating system. The network connecting the server and the client has a speed of 100 Mb/second. The evaluation procedure is written in Visual C++ .NET, accessing the Oracle database through ADO.NET. The EDIT function is implemented using the Wagner–Fischer algorithm [55].

Figure 5 shows the plots of median time for SUB and EDIT against the sample size. The running time is approximately linear with regard to the sample size. The running time for EDIT is about 2.8 times of that for SUB. The running time for EDIT is less than 5 seconds when the sample size is 3,000, which results in reasonably accurate results. We feel that the procedure is reasonably efficient.

## Conclusion and Future Research

WE HAVE PROPOSED AN INFORMATION-THEORETIC approach to exploring attribute correspondences across heterogeneous databases, which is a critical step during database integration. The step is very time-consuming in large database integration projects because the number of possible attribute pairs can be huge and a tremendous amount of time and effort are needed from the analysts, database administrators, and domain experts to determine the semantically corresponding attribute pairs.

We sampled both matching and nonmatching record pairs from two real-world databases, applied exact and approximate matching functions to compare attributes, and then used the mutual information to measure the amount of information provided by the degree of similarity between two attributes about record matching. Attribute pairs with high mutual information quantities have been suggested to the analyst as potential corresponding pairs for further evaluation. Our results enable the analyst to begin with very likely corresponding pairs and gradually evaluate less likely ones, and stop when the likelihood becomes negligible. Consequently, only a small number of the possible attribute pairs need to be evaluated, and thus the amount of needed interaction among the analysts, database administrators, and domain experts can be significantly reduced. We have also presented some further analyses such as multiple mutual information and methods for taking missing values into account, which enhance the basic procedure in extremely “dirty” situations.

![](/api/attachments/QXEDAA39/fulltext/images/1b24dc6a578fcac6ecd2c81b4eaca19ff11c82cee4fc03e9c5578e4e7a18e019.jpg)  
Figure 5. Plots of Median Time for SUB and EDIT Against Sample Size

Our preliminary empirical evaluation of heterogeneous databases shows that the approach can effectively reveal potential attribute correspondences, with no limitation in terms of the types (e.g., numeric and character) of attributes or the functional forms (e.g., linear) of the relationships among attributes, in “dirty” real-world situations. Our approach has therefore overcome some serious shortcomings of previous approaches based on correlation analysis and has much broader applicability. Our proposed methodologies are simple to implement and thus can be easily applied and validated in real-world database integration projects. This research has therefore made an important contribution by providing a more general approach to detecting attribute correspondences across heterogeneous data sources.

Although we have focused on character attributes in two databases in this paper, the extension of the proposed approach to deal with other types of attributes in more than two databases is straightforward. Different matching functions can be defined to compare other types of attributes. Numeric attributes can be directly evaluated using mutual information in a sample of only matching record pairs. The past research has evaluated correspondences between numeric attributes using correlation analysis in a sample of only matching record pairs [16, 17, 31]. Note that the proposed approach should be superior to the previous approach based on correlation analysis even for numeric attributes because the previous approach is applicable only when the attributes are linearly related. For example, correlation analysis can adequately detect correspondences between numeric attributes (e.g., acquisition cost [INV.ACQCOST and FFX.TOTAL\_COST]) in the university property example. Correlation analysis is invariant under linear transformations (e.g., change of measurement scales) but not under nonlinear transformations. As a more general measure of dependence (the mutual information index is the same as the squared correlation when the two attributes under comparison follow a bivariate normal distribution), mutual information can perform as well as correlation in detecting linearly related attributes and better than correlation in detecting nonlinearly related attributes.

Similarly, mutual information can also be used to detect correspondences between categorical attributes (attributes with only a small set of distinct values) that may be coded using different coding schemes. For example, an attribute named gender in one database is coded as (Male/Female), while a corresponding attribute named sex in another database is coded as (0/1). Mutual information is invariant with regard to different coding schemes and can effectively reveal the correspondence between the two coded categorical attributes. However, correlation analysis is not applicable in this case.

When there are more than two databases, the multiple databases can be compared in a pairwise fashion. In addition, a transitive closure can be computed because attribute correspondence is transitive. When there are many databases that need to be compared, a machine learning approach [12, 13] can be used along with the proposed method to improve efficiency and scalability. The proposed method can be used first to identify attribute correspondences across several databases. These identified correspondences can then be used as training examples to train various classifiers, which are then applied on the remaining databases. However, while such a machine learning approach helps to improve efficiency and scalability, we remind the user of the potential risk of losing the correspondences that may exist in the remaining databases but are not covered by the correspondences used during training. The user should also keep in mind that the accuracy of this machine learning approach on some reported testing cases was in the range of 71–92 percent [13].

Despite its projected usefulness, the proposed approach is subject to limitations and is not meant to be a panacea to the semantic correspondence identification problem. Indeed, we believe that there will never be a panacea. The proposed approach may be useful in a very specific task of the overall data integration project and is not intended to solve all the problems. It has several limitations. First, the proposed approach is applicable to heterogeneous databases that share both some semantically corresponding schema elements and some semantically corresponding records. It is not intended for databases that do not have any schema elements or records in common (e.g., distributed databases resulting from vertical or horizontal partitioning of a single database, multiple human resource databases resulting from corporate mergers that do not share any common records).

Second, the proposed approach also assumes the availability of a sample of matching and nonmatching record pairs. When there is no common key across the databases to easily generate such a sample, the proposed technique can be combined with techniques for comparing metadata about schema elements as well as techniques for matching semantically corresponding records in an overall procedure [47]. Metadata can be investigated first to identify an initial set of corresponding schema elements, which is used as a basis for comparing records. Corresponding records identified using record matching techniques can then be used to evaluate attribute correspondences more closely using the technique described in this paper. Any new findings can trigger another iteration of analysis, resulting in an iterative procedure that allows incremental improvement on results. While we have focused on the proposed technique alone in this paper, its application in such an overall procedure can be further evaluated in future research.

The main vehicle in the proposed approach is an estimate of the mutual information function. Estimation of mutual information for the exact attribute matching functions is straightforward. However, for the approximate attribute matching functions, several methods are available for the estimation. In this paper, we used the histogram entropy method, which can be easily implemented. It would be worthwhile to use other entropy estimation procedures [4] and compare the results of various procedures.

Finally, the two university property databases used in the empirical evaluation experiment are the largest real-world heterogeneous databases we currently have. While we have proposed a general methodology, more elaborate engineering effort may be devoted to optimizing the efficiency and scalability of the modules in the procedure to develop practical tools in the future. Such tools may then be applied in real-world large-scale database integration projects to further validate the real utility of the proposed technique.

## REFERENCES

1. Ambrosio, A.P.; Métais, E.; and Meunier, J. The linguistic level: Contribution for conceptual design, view integration, reuse and documentation. Data & Knowledge Engineering, 21, 2 (1997), 111–129.

2. Bakos, J.Y. Information links and electronic marketplaces: The role of interorganizational information systems in vertical markets. Journal of Management Information Systems, 8, 2 (Fall 1991), 31–52.

3. Barrett, S.S. Strategic alternatives and inter-organizational system implementations: An overview. Journal of Management Information Systems, 3, 3 (Winter 1986–1987), 5–16.

4. Beirlant, J.; Dudewicz, E.J.; Gyorfi, L.; and van der Meulen, E.C. Non-parametric entropy estimation: An overview. International Journal of Mathematical and Statistical Sciences, 6, 1 (1997), 17–39.

5. Bell, G.B., and Sethi, A. Matching records in a national medical patient index. Communications of the ACM, 44, 9 (2001), 83–88.

6. Benkley, S.S.; Fandozzi, J.F.; Housman, E.M.; and Woodhouse, G.M. Data element toolbased analysis (DELTA). Technical Report MTR 95B0000147, MITRE Corporation, Bedford, MA, 1995.

7. Brancheau, J.; Janz, B.; and Wetherbe, J. Key issues in information systems management: 1994–95 SIM Delphi results. MIS Quarterly, 20, 2 (1996), 225–242.

8. Bright, M.W.; Hurson, A.R.; and Pakzad, S.H. Automated resolution of semantic heterogeneity in multidatabases. ACM Transactions on Database Systems, 19, 2 (1994), 212–253.

9. Buckland, M., and Gey, F. The relationship between recall and precision. Journal of the American Society for Information Science, 45, 1 (1994), 12–19.

10. Budzinsky, C.D. Automated spelling correction. Statistics Canada, Ottawa, 1991.

11. Clifton, C.; Housman, E.; and Rosenthal, A. Experience with a combined approach to attribute-matching across heterogeneous databases. In S. Spaccapietra and F.J. Maryanski (eds.), Data Mining and Reverse Engineering—Searching for Semantics: Proceedings of the IFIP TC2/WG2.6 Seventh Conference on Database Semantics. London: Chapman and Hall, 1997, pp. 429–451.

12. Dhamanka, R.; Lee, Y.; Doan, A.; Halevy, A.; and Domingos, P. iMAP: Discovering complex semantic matches between database schemas. In G. Weikum, A.C. Konig, and S. Dessloch (eds.), Proceedings of the 2004 ACM SIGMOD International Conference on Management of Data. New York: ACM Press, 2004, pp. 383–394.

13. Doan, A.; Domingos, P.; and Halevy, A. Learning to match the schemas of databases: A multistrategy approach. Machine Learning, 50, 3 (2003), 279–301.

14. Ellmer, E.; Huemer, C.; Merkl, D.; and Pernul, G. Automatic classification of semantic concepts in view specifications. In R. Wagner and H. Thoma (eds.), Proceedings of the Seventh International Conference on Database and Expert Systems Applications. New York: Springer-Verlag, 1996, pp. 824–833.

15. Fan, W.; Gordon, M.D.; and Pathak, P. Effective profiling of consumer information retrieval needs: A unified framework and empirical comparison. Decision Support Systems, 40, 2 (2005), 213–233.

16. Fan, W.; Lu, H.; Madnick, S.E.; and Cheung, D.W. Discovering and reconciling value conflicts for numerical data integration. Information Systems, 26, 8 (2001), 635–656.

17. Fan, W.; Lu, H.; Madnick, S.E.; and Cheung, D.W. DIRECT: A system for mining data value conversion rules from disparate sources. Decision Support Systems, 34, 1 (2002), 19–39.

18. Gosain, S.; Malhotra, A.; and El Sawy, O.A. Coordinating for flexibility in e-business supply chains. Journal of Management Information Systems, 21, 3 (Winter 2004–2005), 7–46.

19. Hall, P., and Morton, S.C. On the estimation of entropy. Annals of Institute of Mathematical Statistics, 45, 1 (1993), 69–88.

20. Han, K.; Kauffman, R.J.; and Nault, B.R. Information exploitation and interorganizational systems ownership. Journal of Management Information Systems, 21, 2 (Fall 2004), 109–135.

21. Harman, D. Overview of the second text retrieval conference (TREC-2). Information Processing & Management, 31, 3 (1995), 271–289.

22. Hayne, S., and Ram, S. Multi-user view integration system (MUVIS): An expert system for view integration. In Proceedings of the Sixth International Conference on Data Engineering. Los Alamitos, CA: IEEE Computer Society Press, 1990, pp. 402–410.

23. Hevner, A.R.; March, S.T.; Park, J.; and Ram, S. Design science in information systems research. MIS Quarterly, 28, 1 (2004), 75–105.

24. Johannesson, P. Supporting schema integration by linguistic instruments. Data & Knowledge Engineering, 21, 2 (1997), 165–182.

25. Kang, J., and Naughton, J.F. On schema matching with opaque column names and data values. In A.Y. Halevy, Z.G. Ives, and A. Doan (eds.), Proceedings of the 2003 ACM SIGMOD International Conference on Management of Data. New York: ACM Press, 2003, pp. 205–216.

26. Kim, W. On database technology for U.S. homeland security. Journal of Object Technology, 1, 5 (2002), 43–49.

27. Kullback, S. Information Theory and Statistics. New York: Wiley, 1959. [Reprinted in 1968.]

28. Kullback, S., and Leibler, R.A. On information and sufficiency. Annals of Mathematical Statistics, 22, 1 (1951), 79–86.

29. Li, W.S., and Clifton, C. SEMINT: A tool for identifying attribute correspondences in heterogeneous databases using neural networks. Data & Knowledge Engineering, 33, 1 (2000), 49–84.

30. Li, Y.; Bandar, Z.A.; and McLean, D. An approach for measuring semantic similarity between words: Using multiple information sources. IEEE Transactions on Knowledge and Data Engineering, 15, 4 (2003), 871–882.

31. Lu, H.; Fan, W.; Goh, C.H.; Madnick, S.E.; and Cheng, D.W. Discovering and reconciling semantic conflicts: A data mining perspective. In S. Spaccapietra and F.J. Maryanski (eds.),

Data Mining and Reverse Engineering—Searching for Semantics: Proceedings of the IFIP TC2/WG2.6 Seventh Conference on Database Semantics. London: Chapman and Hall, 1997, pp. 410–427.

32. Luján-Mora, S., and Palomar, M. Reducing inconsistency in integrating data from different sources. In Proceedings of the 2001 International Database Engineering and Applications Symposium. Los Alamitos, CA: IEEE Computer Society Press, 2001, pp. 209–218.

33. Madhavan, J.; Bernstein, P.A.; and Rahm, E. Generic schema matching with cupid. In P.M.G. Apers, P. Atzeni, S. Ceri, S. Paraboschi, K. Ramamohanarao, and R.T. Snodgrass (eds.), Proceedings of the Twenty-Seventh International Conference on Very Large Databases. San Francisco: Morgan Kaufmann, 2001, pp. 49–58.

34. Madnick, S.E., and Wang, Y.R. Evolution towards strategic applications of databases through composite information systems. Journal of Management Information Systems, 5, 2 (Fall 1988), 5–22.

35. Madnick, S.E.; Wang, Y.R.; and Xian, X. The design and implementation of a corporate householding knowledge processor to improve data quality. Journal of Management Information Systems, 20, 3 (Winter 2003–2004), 41–69.

36. Maier, D. Capturing more meaning in databases. Journal of Management Information Systems, 1, 1 (Summer 1984), 33–49.

37. March, S.T., and Kim, Y. Information resource management: A metadata perspective. Journal of Management Information Systems, 5, 3 (Winter 1988–1989), 5–18.

38. March, S.T.; Hevner, A.; and Ram, S. Research commentary: An agenda for information technology research in heterogeneous and distributed environments. Information Systems Research, 11, 4 (2000), 327–341.

39. Masood, N., and Eaglestone, B. Semantics based schema analysis. In G. Quirchmayr, E. Schweighofer, and T.J.M. Bench-Capon (eds.), Proceedings of the Ninth International Conference on Database and Expert Systems Applications. London: Springer-Verlag, 1998, pp. 80–89.

40. Mirbel, I. Semantic integration of conceptual schemas. Data & Knowledge Engineering, 21, 2 (1997), 183–195.

41. Monge, A.E., and Elkan, C.P. An efficient domain-independent algorithm for detecting approximately duplicate database records. In R. Ng (ed.), Proceedings of the 1997 SIGMOD Workshop on Research Issues on Data Mining and Knowledge Discovery. New York: ACM, 1997, pp. 23–29.

42. Nelson, R.R.; Todd, P.A.; and Wixom, B.H. Antecedents of information and system quality: An empirical examination within the context of data warehousing. Journal of Management Information Systems, 21, 4 (Spring 2005), 199–235.

43. Osborn, C.S.; Madnick, S.E.; and Wang, Y.R. Motivating strategic alliance for composite information systems: The case of a major regional hospital. Journal of Management Information Systems, 6, 3 (Winter 1989–1990), 99–118.

44. Palopoli, L.; Pontieri, L.; Terracina, G.; and Ursino, D. Intensional and extensional integration and abstraction of heterogeneous databases. Data & Knowledge Engineering, 35, 3 (2000), 201–237.

45. Parsons, J. Effects of local versus global schema diagrams on verification and communication in conceptual data modeling. Journal of Management Information Systems, 19, 3 (Winter 2002–2003), 155–183.

46. Ram, S., and Venkataraman, R. Schema integration: Past, present and future. In A. Elmagarmid, M. Rusinkiewicz, and A. Sheth (eds.), Management of Heterogeneous and Autonomous Database System. San Mateo, CA: Morgan Kaufmann, 1999, pp. 119–156.

47. Ram, S., and Zhao, H. Detecting both schema-level and instance-level correspondences for the integration of e-catalogs. In J. Parsons and O. Sheng (eds.), Proceedings of the Eleventh Annual Workshop on Information Technology and Systems. Atlanta: AIS, 2001, pp. 193–198.

48. Ram, S.; Park, J.; Kim, K.; and Hwang, Y. A comprehensive framework for classifying data- and schema-level semantic conflicts in geographic and non-geographic databases. In S. Narasimhan and R. Kumar (eds.), Proceedings of the Ninth Annual Workshop on Information Technologies and Systems. Atlanta: AIS, 1999, pp. 185–190.

49. Resnik, P. Using information content to evaluate semantic similarity in a taxonomy. In C. Mellish (ed.), Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence. San Francisco: Morgan Kaufmann, 1995, pp. 448–453.

50. Rodríguez, M.A.; Egenhofer, M.J.; and Rugg, R.D. Assessing semantic similarities among geospatial feature class definitions. In A. Vckovski, K.E. Brassel, and H.-J. Schek (eds.), Proceedings of the Second International Conference on Interoperating Geographic Information Systems. New York: Springer-Verlag, 1999, pp. 189–202.

51. Seligman, L.; Rosenthal, A.; Lehner, P.; and Smith, A. Data integration: Where does the time go? IEEE Data Engineering Bulletin, 25, 3, 2002, 3–10.

52. Song, W.W.; Johannesson, P.; and Bubenko, J.A. Semantic similarity relations and computation in schema integration. Data & Knowledge Engineering, 19, 1 (1996), 65–97.

53. Soofi, E.S., and Retzer, J.J. Information indices: Unification and applications. Journal of Econometrics, 107, 1–2 (2002), 17–40.

54. Srinivasan, U.; Ngu, A.H.H.; and Gedeon, T. Managing heterogeneous information systems through discovery and retrieval of generic concepts. Journal of American Society for Information Science, 51, 8 (2000), 707–723.

55. Stephen, G.A. String Searching Algorithms. River Edge, NJ: World Scientific Publishing, 1994.

56. Truman, G.E. Integration in electronic exchange environments. Journal of Management Information Systems, 17, 1 (Summer 2000), 209–245.

57. Zhao, H., and Ram, S. Clustering schema elements for semantic integration of heterogeneous data sources. Journal of Database Management, 15, 4 (2004), 88–106.

58. Zhao, H., and Ram, S. Entity identification for heterogeneous database integration—A multiple classifier system approach and empirical evaluation. Information Systems, 30, 2 (2005), 119–132.
