---
otero_id: 14422
otero_key: "FPC89A2X"
title: "Protecting Privacy Against Record Linkage Disclosure: A Bounded Swapping Approach for Numeric Data"
authors: "Xiao-Bai Li; Sumit Sarkar"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0289"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/FPC89A2X/fulltext/images/66cb6e2ba6ab458bb9322f82341a4400a8c84e6690b9961d7974511471d1745b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Protecting Privacy Against Record Linkage Disclosure: A Bounded Swapping Approach for Numeric Data

Xiao-Bai Li, Sumit Sarkar,

## To cite this article:

Xiao-Bai Li, Sumit Sarkar, (2011) Protecting Privacy Against Record Linkage Disclosure: A Bounded Swapping Approach for Numeric Data. Information Systems Research 22(4):774-789. http://dx.doi.org/10.1287/isre.1100.0289

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/FPC89A2X/fulltext/images/f0d1a9807eaf55cae030178fcbdaf6c7c8b9a776cd29c7b682c4ffb6a5291141.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Protecting Privacy Against Record Linkage Disclosure: A Bounded Swapping Approach for Numeric Data

Xiao-Bai Li

Department of Operations and Information Systems, University of Massachusetts Lowell, Lowell, Massachusetts 01854, xiaobai\_li@uml.edu

Sumit Sarkar

School of Management, University of Texas at Dallas, Richardson, Texas 75080, sumit@utdallas.edu

ecord linkage techniques have been widely used in areas such as antiterrorism, crime analysis, epidemi used for identity matching that leads to the disclosure of private information. These techniques can be used to effectively reidentify records even in deidentified data. Consequently, the use of such techniques can lead to individual privacy being severely eroded. Our study addresses this important issue and provides a solution to resolve the conflict between privacy protection and data utility. We propose a data-masking method for protecting private information against record linkage disclosure that preserves the statistical properties of the data for legitimate analysis. Our method recursively partitions a data set into smaller subsets such that data records within each subset are more homogeneous after each partition. The partition is made orthogonal to the maximum variance dimension represented by the first principal component in each partitioned set. The attribute values of a record in a subset are then masked using a double-bounded swapping method. The proposed method, which we call multivariate swapping trees, is nonparametric in nature and does not require any assumptions about statistical distributions of the original data. Experiments conducted on real-world data sets demonstrate that the proposed approach significantly outperforms existing methods in terms of both preventing identity disclosure and preserving data quality.

Key words: privacy; record linkage; data partitioning; data swapping

History: Sudha Ram, Senior Editor; Balaji Padmanadhan, Associate Editor. This paper was received on July 10, 2008, and was with the authors 4 months for 2 revisions. Published online in Articles in Advance June 14, 2010.

## 1. Introduction

Record linkage is a valuable technique for data analysis. Since its introduction by Newcombe et al. (1959, 1962) and Fellegi and Sunter (1969), the technique has been widely used in a variety of application areas such as information retrieval, data fusion, database marketing, epidemiologic research, crime analysis, and terrorism detection. As record linkage and other data-mining techniques become increasingly popular, there are growing concerns about their threats to individual privacy, as reported by the U.S. General Accounting Office (2001). Over the last few years, the U.S. federal and state governments developed counterterrorism programs that are based on record linkage and data-mining technologies, including the Terrorism Information Awareness (TIA) program, the Computer-Assisted Passenger Prescreening System (CAPPS II), and the Multistate Anti-Terrorism Information Exchange (MATRIX) system. These programs were recently terminated because of strong opposition by public and privacy advocates (Seifert 2006). The public’s concern about privacy is further exemplified by the recent case of U.S. Justice Department v. Google, Inc. A poll conducted by KDnuggets (2006) revealed that 51% of respondents, most of them presumably data-mining professionals, believed Google should not release search data to the Justice Department (43% thought otherwise). Concerns about privacy threats have caused data quality and integrity to deteriorate. According to Teltzrow and Kobsa (2004), 82% of online users have refused to give personal information and 34% have lied when asked about their personal habits and preferences.

Prior research has attempted to address the privacy concerns that arise from the use of record linkage and data-mining techniques. Public policy-related issues have been discussed in Cox and Boruch (1988), Fellegi (1997), and Sweeney (2005), among others. Pagliuca and Seri (1999) proposed a privacy disclosure measure for record linkage attacks based on the distance between a record shown on an original data file and that shown on a released file. A popular technique for protecting against record linkage attack is recoding (including global recoding, grouped recoding, and top and bottom recoding), which collapses the individual values of identifying or sensitive attributes into less-detailed values (Hundepool and Willenborg 1996, Boruch et al. 2000, and Garfinkel et al. 2007). Another widely used technique is value suppression (including global and local suppression), which replaces the values of identifying or sensitive attributes with semanticless symbols (Cox 1995, Samarati 2001, and Sweeney 2002). There are also a number of studies that used encryption techniques for protecting identity and confidentiality disclosure using record linkage and other data-snooping techniques (Lindell and Pinkas 2002, Churches and Christen 2004, O’Keefe et al. 2004, and Al-Lawati et al. 2005).

A common practice to protect against identity disclosure is to remove identity-related attributes from released data (called deidentification), in the belief that deidentification is adequate for protecting individual privacy. The fact is, however, that an intruder can often identify a target subject based on the values of the nonconfidential attributes in the deidentified data, and thus discover the confidential values of the subject. Sweeney (2002) pointed out that 87% of the population in the United States can be uniquely identified using deterministic record linkage with three attributes (gender, date of birth, and five-digit zip code), which are accessible from voter registration records available to the public. Li and Sarkar (2006b) investigated the effect of the deidentification practice and analyzed disclosure risk of the individuals in the deidentified data. That study, however, focuses on privacy issues arising in data that are of categorical type.

The reidentification risk may be significantly higher when numeric attributes are present in the data because it is more likely that numeric values are unique, not to mention the combination of multiple numeric values. This study focuses on disclosure protection against record linkage attacks in deidentified numeric data, an area that has not been adequately addressed in prior literature particularly when the statistical distribution of the data is unknown. We examine a situation where an organization releases microdata to enable statistical analysis or data-mining applications. The released data consist of confidential attributes and nonconfidential attributes that can potentially be used to identify individual records. We present a method to mask attribute values to prevent identity disclosure that also adequately preserves the relationships between masked and unmasked attributes. By preventing identity disclosure, the method also effectively protects the confidential information of individuals. The proposed method recursively splits a data set into smaller subsets such that data records within each subset are more homogeneous after each partition. The partition is made orthogonal to the maximum variance dimension represented by the first principal component in each partitioned set. The attribute values of a record in a subset are then masked using a double-bounded swapping method. The proposed method, which we call multivariate swapping trees, is nonparametric in nature and does not require any assumptions about statistical distributions of the original data. Experiments conducted on real-world and simulated data sets demonstrate that the proposed approach significantly outperforms some well-known existing methods in terms of both preventing identity disclosure and preserving data quality.

The main contributions of this research are as follows:

• The novelty and performance advantage of the methodology. The proposed approach integrates a multivariate tree-based data-partitioning method and a rank-based bounded data-swapping method in an innovative manner. Multivariate data partitioning effectively preserves the properties of the data set as a whole when the data are later masked within partitions; bounded swapping ensures that the masked attribute values are at least a certain distance away from the original values, thereby adequately preventing privacy disclosure. Both the multivariate tree-based partitioning and the bounded swapping methods are novel to the literature. The proposed approach leads to superior performance over existing techniques.

• Theoretical justification of our methodology. Many of the existing data privacy methods are parametric, depending on assumptions about the properties of the data such as normality or monotonicity. Current nonparametric approaches lack theoretical results to justify their validity. We show that, for our methodology, the covariance matrix and linear regression parameters of the masked data converge in probability to the original covariance matrix and regression parameters. These results are useful not only for the proposed methodology but also potentially for other nonparametric methods that are similar in nature.

• Computational efficiency. The proposed algorithm is computationally more efficient than well-known data-masking algorithms such as microaggregation. It is therefore well-suited for large-scale data-mining problems.

The rest of the paper is organized as follows. We discuss related prior research in §2. The proposed approach, which includes a multivariate datapartitioning method followed by a bounded swapping method, is presented in §3. Experiments conducted on real and simulated data are described in §4. We conclude the paper and provide directions for future research in §5.

## 2. Related Work

From a privacy viewpoint, the attributes of data can be classified into three categories: (i) identifying attributes, which can be used to directly identify an individual (name, social security number, credit card number, phone number, and address); (ii) confidential attributes, which contain private information that an individual typically does not want revealed (salary, medical test results, sexual orientation, and academic transcripts); and (iii) nonconfidential attributes, which are normally not considered as confidential by individuals (gender, occupation, and zip code). However, the values of some nonconfidential attributes for individuals included in the data can be obtained from different sources that also contain identifying attributes (for example, age, gender, and zip code are accessible from voter registration records). These nonconfidential attributes can be used by an intruder to reidentify the individuals in the deidentified data, which can result in eventual disclosure of confidential values of these individuals. We term these pseudokey attributes for convenience.

There has been extensive research in the area of statistical databases (SDBs) on how to protect individuals’ confidential data when providing summary statistical information (Adam and Wortmann 1989). The privacy issue arises in SDBs when summary statistics are derived using data on very few individuals. In this case, releasing the summary statistics may result in disclosing sensitive data. The methods for preventing such disclosure can be broadly classified into two categories (Duncan and Mukherjee 2000): (i) query restriction, which prohibits queries that would reveal sensitive data, and (ii) data masking, which alters individual data in such a way that the summary statistics remain approximately the same. For a predictive or multivariate data analysis such as regression and correlation analysis, it is typically required that a data set containing individual records (called microdata) be released to the user. As a result, query restriction methods are not applicable and data masking becomes the primary approach for privacy protection in this situation.

This study focuses on microdata where the identifying attributes are removed (deidentified) and pseudokey and confidential attributes are numeric. In this situation, there are two basic strategies for masking data. The first is to mask the pseudokey attributes to prevent reidentification disclosure; the second is to mask the confidential attributes to prevent confidential value disclosure. When both pseudokey and confidential attributes are numeric, techniques originally designed to mask confidential attributes can be easily applied to masking pseudokey attributes and vice versa. Therefore, we consider techniques that attempt to mask either pseudokey or confidential attributes in the following discussion.

One of the popular data-masking methods is noisebased perturbation (Traub et al. 1984, Liew et al. 1985). The basic idea behind this approach is to add noise to either the pseudokey or the confidential data to disguise their true values while preserving the statistical properties of the data as a whole. This approach is easy to implement and works well in some situations. One limitation is that the perturbation mechanisms typically depend on some assumptions about the properties of the data such as normality or monotonicity. This can cause data utility to deteriorate when the assumptions are violated. Another limitation is that the perturbed values may be unreasonable (for example, a negative age or body weight).

For business applications, the data being analyzed such as customer and transaction data typically have very complex characteristics. Their distributions are often unknown and difficult to estimate. Therefore, it is desirable to have a data-masking method that does not require any prior knowledge about the distributions. One such approach is microaggregation, which masks data by aggregating confidential values instead of adding noise. Univariate microaggregation (Defays and Nanopoulos 1993) involves sorting records by each attribute to be masked, clustering adjacent records into groups of small sizes, and replacing the individual values in each group with the group average. Hansen and Mukherjee (2003) provide a microaggregation algorithm that minimizes univariate information loss. Univariate microaggregation does not consider the relationships between attributes so the masked data might not be appropriate for data mining. Multivariate microaggregation groups data using a clustering technique that is based on a multidimensional distance measure (Domingo-Ferrer and Mateo-Sanz 2002, Laszlo and Mukherjee 2005). As a result, the relationships between attributes are expected to be better preserved. However, this benefit comes with a higher computational cost, which could be inefficient for large data sets (Li and Sarkar 2006a). Because of its nonparametric nature, another criticism leveled against microaggregation is that it lacks analytical justification for preserving statistical properties of the data (Winkler 2007).

A method for privacy protection in the deidentified data called k-anonymity (Samarati 2001, Sweeney 2002) has recently gained increasing popularity. The basic idea behind k-anonymity is to mask the values for the pseudokey attributes (called quasi identifier in their papers) such that the values of the pseudokey attributes for any individual match those of at least k − 1 other individuals in the same data set. In this way, the identity of an individual is expected to be better protected. However, it is still possible for an intruder to discover the confidential information of individuals in the k-anonymized data (Machanavajjhala et al. 2006). The problem is that k-anonymity protects identity disclosure by generalizing different but similar pseudokey attribute values into the same value. The new values produced by the generalization operation are still correct with respect to the generalized categories. Because confidential attribute values remain unchanged in k-anonymity, individuals in a group with the same pseudokey attribute values are subject to disclosure if their confidential values in the group are the same. Further, k-anonymity focuses primarily on categorical data. When an attribute is initially numeric, the technique converts its values into intervals and then treats the intervals as categorical values. In this study, we focus on masking data within a numeric domain.

Li and Sarkar (2006a) proposed a tree-based datamasking method. Their basic idea is to use a kd-tree technique (Friedman and Bentley 1977) to recursively divide a data set into smaller subsets such that data points within each subset are more homogeneous after each partition. A kd-tree algorithm typically selects the attribute with the largest variance and splits the data into two subsets at the median or midrange of the attribute. After this data-partitioning process is completed, the values of confidential or pseudokey attributes at a leaf are then replaced with the average value at the leaf. This method has two limitations as noted by Li and Sarkar (2006a). First, because kd-trees are univariate $( \mathrm { i . e . , }$ each split uses only one attribute), when the boundaries between data clusters are not approximately axis parallel, they could create groups within which data points are quite dissimilar, which could cause poor data quality for the masked data. Second, because of the use of average value for a leaf to replace the original values, the variance of the masked data is always smaller than that of the original data. This is undesirable in terms of preserving statistical properties of the data.

The method presented in this paper overcomes both limitations in Li and Sarkar (2006a). It uses oblique splits to handle data clusters whose boundaries are not axis parallel. The data partition is made orthogonal to the maximum variance dimension represented by the first principal component in each partitioned set. This partitioning method is in the same spirit as the well-known k-means clustering with $k = 2$ and equal cluster size, as discussed in $\ S 3 .$ To remove the negative bias in variance because of using leaf average, the proposed method adopts a novel swapping method that not only completely preserves the variance of the data but also results in significantly smaller deviations in correlations as compared to microaggregation and the kd-tree-based method. Our analysis indicates that, with this method, the covariance matrix and linear regression parameters of the masked data converge in probability to the original covariance matrix and regression parameters.

## 3. The Tree-Based Bounded Swapping Approach

The proposed approach is composed of two steps. Step 1 consists of a tree-based data-partitioning method that recursively partitions a data set into smaller subsets, where data items are more similar. The purpose of data partitioning is to preserve the properties of the data set as a whole so that the results of data analysis on the masked data are similar to those on the original data. Step 2 consists of a bounded data-swapping method that is applied to the data within each subset obtained in Step 1 to protect against identity disclosure.

## 3.1. Multivariate Trees Using Principal Components

To illustrate the idea of multivariate trees, consider an example data set containing 14 records with 2 attributes $X _ { 1 }$ and $X _ { 2 }$ as plotted in Figure 1. We contrast the proposed approach to the univariate trees proposed in Li and Sarkar (2006a). The univariate tree algorithm first selects the attribute with maximum variance, which is $( X _ { 1 } )$ , and partitions the data at the midrange of the attribute, which results in a split represented by the vertical dashed line. The splitting process continues on the partitioned sets until each subset contains no more than a prespecified number (e.g., four in this example). The procedure results in axis-parallel partitions as shown by the dashed lines. The data set is eventually divided into four subsets: 811 21 31 89, 841 51 69, 891 101 119, and 871 121 131 149. The values of the confidential or pseudokey attribute (say, $X _ { 1 } )$ are then replaced with the subset-average value of that attribute. It can be seen from Figure 1 that some data points are not included in their natural groupings because of the restriction of axis-parallel partitions. For instance, Record 7 is closer to Records

Figure 1 An Illustrative Example  
![](/api/attachments/FPC89A2X/fulltext/images/7bb76abf32cc7d38fa5c715feb5bd42ee97e1e9b9d93b553f606d846ce721cfa.jpg)

4, 5, and 6 than to Records 12, 13, and 14. Similarly, Record 8 is included in an inappropriate group.

The method we present attempts to partition the data along their natural boundaries using linear combinations of multiple attributes as shown by the oblique solid lines in Figure 1. The linear combinations are constructed using principal components. Given a set of data with M attributes, $\mathbf { X } =$ $[ X _ { 1 } , \dots , X _ { M } ] ^ { \prime }$ , let $\mathbf { e } _ { 1 } , \ldots , \mathbf { e } _ { { \scriptscriptstyle M } }$ be the eigenvectors of the covariance matrix, ranked in descending order by their corresponding eigenvalues. The jth principal component is given by

$$
V _ {j} = \mathbf {e ^ {\prime}} _ {j} \mathbf {X} = e _ {j 1} X _ {1} + \dots + e _ {j M} X _ {M}, j = 1, \ldots , M.\tag{1}
$$

Geometrically, principal components are formed by rotating and shifting the original coordinate system such that each new axis passes through the data points in the direction of maximum variance. Our method draws upon this idea for partitioning the data. It computes the first principal component for each partitioned subset, which represents the direction of the maximum variance for the subset. Each of the n records in the subset is then projected onto this first principal component as

$$
v _ {i 1} = \mathbf {e ^ {\prime}} _ {1} \mathbf {x} _ {i} = e _ {1 1} x _ {i 1} + \dots + e _ {1 M} x _ {i M}, i = 1, \ldots , n.\tag{2}
$$

The subset is then partitioned at the median of the projection list $v _ { 1 1 } , v _ { 2 1 } , \ldots , v _ { n 1 }$ . The process continues until each subset contains no more than a prespecified number of records. The entire recursive partitioning process can be illustrated by a tree structure, with each split involving multiple attributes (variables).

The objective of multivariate data partitioning is to preserve the joint distribution of the data. Because data partitions are obtained based on all of the attributes, the records within a subset are more similar to each other in terms of all the attributes and they are less similar between subsets. If we view each partitioned subset geometrically as a data mass in the relevant space, then the joint distribution of these data masses remains the same before and after data masking because masking is performed within each mass. As a result, the joint distribution of the individual data points is reasonably preserved (we provide analytical results on this in §3.3). This is achieved without assuming any knowledge about statistical distributions of the original data.

We should also point out that the multivariate partitioning approach does not need the assumption of monotonic relationships between attributes. Our method effectively handles nonmonotonic relationships between the attributes by recursively partitioning the data into subsets within which data items become increasingly similar. If there are nonmonotonic between the attributes in the original data, such relationships are segmented into monotonic relationships within the subsets. The relationships across different subsets will remain nonmonotonic because masking is performed within each subset.

The multivariate tree algorithm is computationally quite efficient as formally described in Lemma 1.

<sup>Lemma</sup> <sup>1.</sup> The computational time complexity of the multivariate tree algorithm is of order O4N log N 5, where N is the number of records in the data set.

The proofs of Lemma 1 and all other lemmas and theorems are provided in the appendix. As mentioned earlier, microaggregation techniques usually employ a clustering algorithm to group the data into subsets. For example, Domingo-Ferrer and Mateo-Sanz (2002) use the Ward clustering method while Laszlo and Mukherjee (2005) adopt a clustering method based on minimum spanning trees. Because a clustering algorithm is typically designed to minimize some withingroup distance measures, it may have an advantage over the kd-tree-based partitioning method in this aspect. However, for a data set with N records, such clustering algorithms normally require a computing time of at least O4N <sup>2</sup>5, which can be expensive for large data sets. Lemma 1 shows that the proposed algorithm is computationally more efficient than a traditional clustering algorithm. Furthermore, as we discuss later in §3.3, this principal component-based partitioning follows the same principle as a recursive k-means equal-size clustering with $\bar { k } = 2$ . Therefore, this method can be very effective in terms of grouping similar records.

## 3.2. Double-Bounded Swapping

In most microaggregation methods as well as in the kd-tree approach (Li and Sarkar 2006a), data masking is achieved by replacing the values of a confidential attribute in a subset with the subset-average value of the corresponding attribute. Taking the average, however, results in a reduction in variance in the masked data. In addition, the subset average may be very close to some original values and thus may not provide sufficient protection against record linkage attacks. To overcome these problems, we propose a bounded swapping method that not only maintains exactly the variance of the data but also ensures that the masked values are at least a certain distance away from the original values.

The idea behind bounded swapping is derived from the rank-based swapping method in Moore (1996). Moore’s method, originally intended for application to the entire data set, first sorts the values of an attribute to be masked. Each value is then randomly swapped with another value such that the distance in rank between the two values is smaller than a prespecified value. This procedure is repeated independently for each attribute to be masked. By specifying an upper-bound distance for swapping, some statistical properties of the data are expected to be reasonably preserved. However, if there are nonmonotonic relationships between the attributes, then multivariate statistical properties are less likely to be adequately preserved because the ranking and swapping are done for each attribute independently. Moreover, because there is no lower-bound distance for swapping, an attribute value could be swapped with a very close value. Therefore, disclosure risk associated with the rank-based swapping method can be high.

In our proposed method, rank-based swapping is made within each subset partitioned by a multivariate swapping tree. With partitioned data, the upper bound of the distance is naturally set by the range of each partition, which can be controlled by the subset size ã. To limit disclosure risk, we impose a lower bound  on the distance in rank (as opposed to an upper bound in the original rank-based swapping). It is in this sense that we call the proposed method “double-bounded” swapping.

In general, the lower bound  and upper bound ã are related to both disclosure risk and data quality. Larger  and ã values will lead to larger distances between the original and masked values and thus better protection against disclosure, but this will likely reduce data utility in that the statistical distribution of the masked data will be further away from that of the original data. In our algorithm, the lower bound  essentially serves as a disclosure protection parameter by setting the minimum distance between the original and masked values. The upper bound ã, on the other hand, is primarily used for preserving data utility in that it sets the maximum distance between the original and masked values. As such, it will be most effective to set  as large as possible and ã as small as possible. However, to ensure that the distance in rank between two swapped values is at least $\delta ,$ the parameters  and ã should be set such that $\Delta \ge 2 \delta$ . Usually, we choose $\Delta$ to be somewhat larger than 2 to make the implementation of the swapping procedure easier.

The complete algorithm for this multivariate treebased swapping approach is provided in Figure 2. Overall, this algorithm is computationally very efficient as stated in Lemma 2.

<sup>Lemma</sup> <sup>2.</sup> The computational time complexity of the entire tree-based double-bounded swapping algorithm is of order O4N log N 50

As described in Step 5 of the algorithm, for a given attribute value, the value to be swapped is selected at random as long as the distance in rank between the two values is greater than . In general, we assume

## Figure 2 Multivariate Swapping Tree Algorithm

1. Let X be the data set at the current node, with n records. Compute the first principal component $V _ { 1 }$ using Equation (1).

2. For each record i, compute its projection on $V _ { 1 }$ using Equation (2). Partition X into two subsets (child nodes) at the median of the projection list $\left[ v _ { 1 1 } , v _ { 2 1 } , \ldots , v _ { n 1 } \right]$

3. Repeat Steps 1 and 2 for each of the two child nodes. Stop the process when each node contains fewer than a prespecified number of records ã.

4. Within each leaf (subset), sort the values of each attribute to be masked.

5. Let $X _ { j }$ be an attribute to be masked. Sequentially swap all $X _ { j }$ values in the subset as follows: For an unswapped value $x _ { i j } ,$ randomly select another unswapped value $x _ { r j }$ such that $| i - r | \geq \delta ,$ where  is a prespecified lower bound for distance in rank and $\delta < \Delta / 2 .$ . Swap $x _ { i j }$ with $x _ { r j } .$ Repeat this procedure for each attribute to be masked.

6. Repeat Steps 4 and 5 for each leaf in the tree built in Step 3.

that parameters  and ã are not revealed when the masked data are released. If an intruder somehow knew the parameters, the randomness in swapping would still prevent reverse unmasking of the data. Note that swaps are made separately for individual attributes; therefore, the values of different attributes for a masked record are usually taken from those of different records. This makes reverse unmasking extremely difficult.

Pagliuca and Seri (1999) proposed a deterministic record linkage measure for evaluating reidentification risk. The measure uses the Euclidean distance between a record shown on an original data file and that shown on the corresponding masked file. A record in the masked file is said to be “linked” if the record closest to it in the original file is indeed the corresponding unmasked record. A record in the masked file is “second closely linked” if the second closest record in the original file is the corresponding one. The record linkage measure is defined as the percentage of records that are either “linked” or “second closely linked.” Obviously, the measure can be extended to cover a closely linked record for any order. The parameter  in our approach is a good approximation for the order of closeness in measuring reidentification risk. Therefore, by suitably choosing its value, the method is expected to be effective in preventing or limiting identity disclosure by record linkage.

3.3. Analytical Properties of the Proposed Method A strong advantage of the proposed method is that it is nonparametric in nature and does not require any assumptions about statistical distributions of the original data. As a result, the statistical properties discussed in this section also do not depend on any distributional assumptions.

To describe the analytical properties formally, we first define some terms. Let N be the number of records in the data set, $T$ be the number of leaves in the masking tree, and $n _ { t }$ be the number of records in leaf t. Let $X _ { i } \ ( j = 1 , \ldots , M )$ be an attribute to be masked, $x _ { i j } \ ( i = 1 , \ldots , N )$ be the value of $X _ { j }$ in the ith record, and ${ \overline { { X } } } _ { i }$ be the overall mean of the $X _ { j }$ values. Let $x _ { i j | t } \ ( i = \dot { 1 } , \ldots , n _ { t } )$ be the value of $X _ { j }$ in the ith record in leaf $t ,$ and $\bar { x } _ { j \vert t }$ be the mean of the $X _ { j }$ values in leaf t. Let $X _ { k } \ ( k = 1 , \ldots , M ; k \neq j )$ be another attribute, which may or may not be subject to masking. Denote $x _ { i k } , X _ { k } , x _ { i k | t }$ and $\bar { x } _ { k \mid t }$ similarly.

<sup>Definition</sup> <sup>1.</sup> The total sum of cross-products between $X _ { j }$ and $X _ { k }$ is defined as

$$
T S C P (X _ {j}, X _ {k}) = \sum_ {i = 1} ^ {N} (x _ {i j} - \overline {{X}} _ {j}) (x _ {i k} - \overline {{X}} _ {k}).\tag{3}
$$

The within-group sum of cross-products between $X _ { j }$ and $X _ { k }$ is defined as

$$
W S C P (X _ {j}, X _ {k}) = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (x _ {i j | t} - \bar {x} _ {j | t}) (x _ {i k | t} - \bar {x} _ {k | t}).\tag{4}
$$

The between-group sum of cross-products between $X _ { j }$ and $X _ { k }$ is defined as

$$
B S C P (X _ {j}, X _ {k}) = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (\bar {x} _ {j | t} - \overline {{X}} _ {j}) (\bar {x} _ {k | t} - \overline {{X}} _ {k}).\tag{5}
$$

The within-group sum of cross-products measures the covariance relationships within a data mass partitioned by the tree while the between-group sum of cross-products measures the covariance relationships between the different data masses. Lemma 3 specifies the relationship among the total sum of cross-products, between-group sum of cross-products, and within-group sum of cross-products.

<sup>Lemma</sup> <sup>3.</sup> The total sum of cross-products between $X _ { j }$ and $X _ { k }$ can be decomposed into two components—the between-group sum of cross-products and the within-group sum of cross-products—as follows:

$$
T S C P (X _ {j}, X _ {k}) = B S C P (X _ {j}, X _ {k}) + W S C P (X _ {j}, X _ {k}).\tag{6}
$$

Next, we discuss the connection between the principal component-based partitioning method and the well-known k-means clustering method. Let ${ \bf x } _ { i } ~ ( i =$ $1 , \ldots , N )$ be the values of the ith record, $\begin{array} { r l } { \mathbf { x } _ { i t } } & { { } ( i = } \end{array}$ $1 , \ldots , n _ { t } )$ be the values of the ith record in leaf t, $\overline { { \mathbf { x } } } _ { t }$ be the mean vector in leaf $t ,$ and X<sup>±</sup> be the overall mean vector.

<sup>Definition</sup> <sup>2.</sup> The total sum of squares is defined as

$$
T S S = \sum_ {i = 1} ^ {N} (\mathbf {x} _ {i} - \overline {{\mathbf {X}}}) ^ {\prime} (\mathbf {x} _ {i} - \overline {{\mathbf {X}}}).\tag{7}
$$

The within-group sum of squares is defined as

$$
W S S = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (\mathbf {x} _ {i t} - \overline {{\mathbf {x}}} _ {t}) ^ {\prime} (\mathbf {x} _ {i t} - \overline {{\mathbf {x}}} _ {t}).\tag{8}
$$

The between-group sum of squares is defined as

$$
B S S = \sum_ {t = 1} ^ {T} n _ {t} (\overline {{\mathbf {x}}} _ {t} - \overline {{\mathbf {X}}}) ^ {\prime} (\overline {{\mathbf {x}}} _ {t} - \overline {{\mathbf {X}}}).\tag{9}
$$

<sup>Observation</sup> <sup>1.</sup> The principal component-based partitioning method based on Equations (1) and (2) at each node follows the same principle as a 2- means clustering method with an equal cluster size constraint.

This observation can be justified as follows. The objective of the k-means clustering method (MacQueen 1967) is to group the data into k clusters such that the within-cluster sum of squares is minimized. With $k = 2 .$ , the problem can be formulated as follows (Bradley et al. 1999):

$$
\min \sum_ {g = 1} ^ {2} \sum_ {i = 1} ^ {N} u _ {i g} (\mathbf {x} _ {i} - \overline {{\mathbf {x}}} _ {g}) ^ {\prime} (\mathbf {x} _ {i} - \overline {{\mathbf {x}}} _ {g})\tag{10a}
$$

$$
\mathrm{s.t.} u _ {i 1} + u _ {i 2} = 1, i = 1, \ldots , N,\tag{10b}
$$

$$
\begin{array}{c} u _ {i g} = \begin{array}{l} 1, \text {if} \mathbf {x} _ {i} \in \text {cluster} g, \\ 0, \text {if} \mathbf {x} _ {i} \notin \text {cluster} g, \end{array} \\ i = 1, \ldots , N;   g = 1,   2. \end{array}\tag{10c}
$$

Note that (10a) is equivalent to WSS in (8) with $T = 2$ It follows from Lemma 3 that

$$
T S S = W S S + B S S.\tag{11}
$$

Because TSS is a constant for a given data set, minimizing WSS is equivalent to maximizing BSS. Thus, objective (10a) can be written, in terms of maximizing BSS, as

$$
\max \sum_ {g = 1} ^ {2} n _ {g} (\overline {{\mathbf {x}}} _ {g} - \overline {{\mathbf {X}}}) ^ {\prime} (\overline {{\mathbf {x}}} _ {g} - \overline {{\mathbf {X}}}),\tag{12}
$$

where $\begin{array} { r } { n _ { g } = \sum _ { i = 1 } ^ { N } u _ { i g } } \end{array}$ is the number of data points in cluster $\bar { g } \ ( g = 1 , 2 )$ . It follows from the equal cluster size constraint that $n _ { 1 } = n _ { 2 }$ and both of them are a constant for a given data set. Thus, they can be taken out of the optimization objective and (12) is equivalent to

$$
\max \sum_ {g = 1} ^ {2} (\overline {{\mathbf {x}}} _ {g} - \overline {{\mathbf {X}}}) ^ {\prime} (\overline {{\mathbf {x}}} _ {g} - \overline {{\mathbf {X}}}).\tag{13}
$$

Hence, the 2-means equal-size clustering problem is to group the data such that the distance between the two cluster centers is maximized. Various algorithms that use iterative approaches have been proposed to solve this problem. Unlike (supervised) classification problems, there does not exist a single-cut solution using a functional form partition for this optimization problem (otherwise, we would use it). Because the first principal component represents the maximum variance direction, it becomes an ideal candidate to represent the direction that maximizes the distance between two cluster centers. The partition at the median of the projections along this direction leads to equal group size.

Observation 1 indicates that the proposed multivariate swapping tree approach is similar to a recursive two-group clustering approach. However, as mentioned earlier, the proposed algorithm has a clear advantage over traditional clustering algorithms in computational cost. We demonstrate this experimentally in §4.

We now discuss statistical properties related to the proposed bounded swapping method. We first present a straightforward property below, which is a direct result of the swapping method.

<sup>Theorem</sup> <sup>1.</sup> The marginal distribution of each attribute masked by the proposed swapping method is completely preserved both within each subset and for the entire data set; this implies that parameters such as means and variances are completely preserved both within each subset and for the entire data set.

It follows from Lemma 3 and Theorem 1 that, using tree-based partitioning, the difference in total sum of cross-products before and after masking is independent of the between-group sum of cross-products. To describe this property, let $Y _ { j }$ be the masked value of $X _ { j }$ and $Y _ { k }$ be the masked value of $X _ { k } ~ ( Y _ { k }$ and $X _ { k }$ are the same if $X _ { k }$ is not masked).

<sup>Lemma</sup> <sup>4.</sup> The difference in total sum of cross-products caused by masking depends only on the within-group sum of cross-products; i.e.,

$$
\begin{array}{c} T S C P (Y _ {j}, Y _ {k}) - T S C P (X _ {j}, X _ {k}) \\ = W S C P (Y _ {j}, Y _ {k}) - W S C P (X _ {j}, X _ {k}). \end{array}\tag{14}
$$

Next, we discuss the asymptotic behavior of the covariances and linear regression parameters associated with the double-bounded swapping method. Let $Z _ { N }$ be a random variable indexed by its sample size N . In asymptotic theory, $Z _ { N }$ is said to converge in probability to a finite quantity C if lim $_ { \cdot \ / N  \infty } \operatorname* { P r } ( | Z _ { N } - C | > \bar { \varepsilon } ) = 0$ for any positive . This is written as follows (Greene 1993, p. 99):

$$
\operatorname{plim} Z _ {N} = C.\tag{15}
$$

<sup>Theorem</sup> <sup>2.</sup> For a fixed leaf size ã, the covariance matrix of the masked data S<sup>˜</sup> converges in probability to the original covariance matrix S; i.e.,

$$
\operatorname{plim} \tilde {\mathbf {S}} = \mathbf {S}.\tag{16}
$$

Theorem 2 provides an important property about the proposed approach. We note that this property does not hold for all masking approaches that use swapping. For instance, a simple random swapping method (without data partitioning) clearly does not have this “large sample” property because there is a high probability that an attribute value will be swapped with another fairly distant value, and this probability does not decrease as the size of the data set increases. As a result, the covariances of the masked data will not converge in probability to the original covariances. This convergence property also does not hold for rank-based swapping (Moore 1996) because this method sorts and swaps the data values within each attribute independently over the entire range of the attribute. If there are nonmonotonic relationships between different attributes, then the covariances between these attributes will not be adequately preserved regardless of the data set size.

Next, we consider linear regression parameters. Given a set of data $\pmb { X } = [ X _ { 0 } \mid \mathbf { X } _ { 1 } ]$ , where $X _ { 0 }$ is called the dependent variable and $\mathbf { X } _ { 1 }$ is a set of independent variables, a linear regression model can be written as follows (Graybill 1976):

$$
E (X _ {0} \mid \mathbf {X} _ {1}) = a + \mathbf {b} ^ {\prime} \mathbf {X} _ {1},\tag{17}
$$

where a and b are the intercept and slope parameters, respectively. Let a˜ and b<sup>˜</sup> be the corresponding parameters based on the masked data.

<sup>Theorem</sup> <sup>3.</sup> For a fixed leaf size ã, the linear regression parameters of the masked data converges in probability to the original parameters; i.e.,

$$
\operatorname{plim} \tilde {a} = a, \quad a n d \quad \operatorname{plim} \tilde {\mathbf {b}} = \mathbf {b}.\tag{18}
$$

Again, this property does not hold for masking methods like simple random swapping and rankbased swapping. As mentioned earlier, the lowerbound parameter for swapping  is constrained by the upper-bound parameter ã. We have also explained in §3.2 that  is a good approximation for the record linkage measure. Given fixed ã and  values, the percentage of the linked records should decrease as the data set size N increases. At the same time, Theorems 2 and 3 indicate that the quality of the masked data improves as N becomes large. As a result, the proposed bounded swapping method will perform better in both data utility and disclosure protection aspects when the size of the data set is large.

## 4. Experimental Evaluation

## 4.1. Data

We conducted experiments on three real-world data sets and a series of simulated data sets to evaluate the proposed method. The Association for Information Systems has a website that conducts annual surveys of MIS faculty salary offers (Galletta 2004). Our first real-world data set was taken from this site, where the offer data from 1999 to 2002 inclusive were selected (attributes are consistent for these four years and somewhat different for other years). The data set consists of 443 records of faculty members who received offers during the period. There are 13 attributes, including salary offered, position, course load, number of years teaching, region, and year indicator. They are of numeric, ordinal, or binary type and thus can be easily handled by the algorithms used in the experiment. Salary offered was considered as the confidential attribute.

The second real-world data set includes 1080 individual records extracted from the U.S. Census Bureau’s data website (Brand et al. 2002). It has 13 numeric attributes originally, including various categories of income, taxes, interests, and health insurance. During experiments, we found that, for each record, the value of one attribute (total person earnings) exactly equals the sum of two other attribute values. This attribute was removed from the data set, which resulted in a total of 12 attributes. The attribute net earnings was assumed confidential.

The third real-world data set was initially collected by Torgo (1996) using census data. It consists of 22,784 house records and includes 9 demographicand housing-related attributes, all of them numeric. All attributes except house price were given symbolic names and thus their actual meanings are not available to us. House price was considered as the confidential attribute. The original data set has seven decimal places for all numeric attribute values. The values of the first and last attributes are about 1,000 to 10,000 times larger than the values of the other attributes. To make the scale of all attribute values comparable, the values of these two attributes were divided by 1,000 and subsequently rounded to 7 decimal places.

A series of simulated data sets were generated based on a multivariate normal distribution (named MVN) with the following mean vector and covariance matrix:

$$
\boldsymbol {\mu} = [ 4. 3 2 \quad 1 4. 0 1 \quad 1. 9 5 \quad 2. 1 7 \quad 2. 4 5 ] ^ {\prime},
$$

$$
\boldsymbol {\Sigma} = \left[ \begin{array}{l l l l l} 4. 3 0 8 & 1. 6 8 3 & 1. 8 0 3 & 2. 1 5 5 & - 0. 2 5 3 \\ 1. 6 8 3 & 1. 7 6 8 & 0. 5 8 8 & 0. 1 7 7 & 0. 1 7 6 \\ 1. 8 0 3 & 0. 5 8 8 & 0. 8 0 1 & 1. 0 6 5 & - 0. 1 5 8 \\ 2. 1 5 5 & 0. 1 7 7 & 1. 0 6 5 & 1. 9 7 0 & - 0. 3 5 7 \\ - 0. 2 5 3 & 0. 1 7 6 & - 0. 1 5 8 & - 0. 3 5 7 & 0. 5 0 4 \end{array} \right]
$$

These parameters were taken from an example in Johnson and Wichern (2002, p. 439), that is, in fact, derived from real-world socioeconomic data. Based on the context of these attributes, the last attribute was assumed confidential. The purpose of using simulated data is to examine how different methods perform under controlled conditions. Four data sets were generated using the above parameters, with the number of records being 5,000, 10,000, 15,000, and 20,000. Obviously, given a fixed number of pseudokey attributes, when the data set size is large it becomes more difficult to reidentify a record in the data set and is thus easier to protect against record linkage attacks (this is indeed verified by the results of the experiment described later). Therefore, it is not very interesting to experiment with data sets of overly large size.

## 4.2. Experimental Setup

Three masking methods were used in the experiments: microaggregation (Domingo-Ferrer and Mateo-Sanz 2002), univariate perturbation trees (Li and Sarkar 2006a), and the proposed multivariate swapping trees. The identity disclosure risk measure used in the experiment is the record linkage measure (Pagliuca and Seri 1999) discussed earlier, which is defined as the percentage of records that are either linked or second closely linked.

All three methods preserve the original means in the masked data. Thus, univariate information loss because of data masking is measured using average bias in standard deviation (ABISD) (Adam and Wortmann 1989, Domingo-Ferrer and Torra 2001), defined as

$$
\mathrm{ABISD} = \frac {1}{m} \sum_ {j = 1} ^ {m} \left(\frac {S D (Y _ {j}) - S D (X _ {j})}{S D (X _ {j})}\right),\tag{19}
$$

where m is the number of masked attributes and $S D ( X _ { j } )$ and $S D ( Y _ { j } )$ are standard deviations calculated on the original and masked data, respectively. A small ABISD value indicates that the standard deviations for the masked data are, on average, close to those for the original data. Clearly, the smaller the ABISD values, the smaller the information loss in standard deviation.

To measure multivariate information loss, we use average bias in correlation (ABICO), which is defined as follows (Domingo-Ferrer and Torra 2001):

$$
\mathrm{ABICO} = \frac {1}{C} \sum \left| \frac {\operatorname{Corr} \left(Y _ {j} , Y _ {k}\right) - \operatorname{Corr} \left(X _ {j} , X _ {k}\right)}{\operatorname{Corr} \left(X _ {j} , X _ {k}\right)} \right|,\tag{20}
$$

where $\operatorname { C o r r } ( X _ { i } , X _ { k } )$ is the correlation between attributes j and k computed on the original data set and $\operatorname { C o r r } ( Y _ { j } , Y _ { k } )$ is the same correlation computed on the masked data set. The summation is run over all the correlations related to the masked attributes. The number of such correlations is $C = m ( m - 1 ) / 2 + m ( M - m )$ , where M is the total number of attributes. The absolute values are taken in the above definitions to prevent positive and negative biases over different attributes from canceling out (absolute values are not needed for ABISD because the directions of the biases in standard deviation for the three methods are known with certainty). Again, a smaller ABICO value is desirable because it indicates a smaller information loss in correlation.

In addition, regression and neural network analyses were performed to examine how well the relationships between nonconfidential and confidential attributes are maintained in predictive data analysis. We used the Weka implementation of regression and neural network models (Witten and Frank 2005) with default parameters in our experiments.<sup>1</sup> The confidential attribute in each data set served as the dependent (output) variable while all the other attributes were used as independent (input) variables. We applied a fivefold cross-validation procedure in the experiments. A data set was first randomly partitioned into five equally sized blocks. All masking algorithms were run five times. Each time, one block was used as the test set while the remaining four blocks together were the training set. The training set served as the “original” set for masking (and subsequently for building regression and neural network models) while the test set was not masked. This process was repeated five times, each time with different training and test sets.

Information loss is measured by the mean absolute percentage error (MAPE), defined as

$$
\mathrm{MAPE} = \frac {1}{L} \sum_ {i = 1} ^ {L} \left| \frac {x _ {i} - \hat {x} _ {i}}{x _ {i}} \right|,\tag{21}
$$

where L is the number of records in the test set, $x _ { i }$ is the confidential value of the ith record in the test set, and $\hat { x } _ { i }$ is the estimate of $x _ { i }$ based on the regression or neural network model. Because a fivefold crossvalidation procedure was used, we report the average results over five runs for MAPE as well as for all other performance metrics. As MAPE measures the distance between the predictions of the model built from the masked data and the values in the unmasked test data, a smaller MAPE value is desirable. In the experiments, the MAPE values were computed on the unmasked training and testing sets for comparison.

Because this study focuses on masking potentially identifying attributes, we kept the confidential attribute unmasked while the nonconfidential attributes were subject to masking. To do this, it is necessary to specify the pseudokey attributes to be masked. In general, pseudokey attributes are those that may be accessible to a potential intruder. Identifying such attributes in our experiment requires more background information about the data than what we had available. Therefore, instead of selecting the pseudokey attributes subjectively, we used two criteria to determine pseudokey attributes. The first is to simply mask all nonconfidential attributes assuming they are all pseudokey attributes. The second is to select one half of the nonconfidential attributes as the pseudokey attributes based on the statistical significance of the attributes with respect to the confidential attribute. To identify these attributes, for each data set a linear regression was run on the original data using the confidential attribute as the dependent variable. The nonconfidential attributes that were most statistically significant in the regression model were selected for masking.

Comparisons of different masking methods should be made in terms of both disclosure risk and data utility measures. As described above, there is one disclosure risk measure (record linkage) and three information loss measures. Ideally, if the methods under comparison can be adjusted such that the masked data produced by them all result in the same record linkage value, then it will be easier to compare the performances based on the information loss measures. This is very difficult to achieve given the fivefold cross-validation procedure. Because the purpose of this experiment is to evaluate the performance of the multivariate swapping tree method, we adjusted the leaf size ã and the rank-distance size  in this method as well as the group sizes for the other two methods to produce masked data such that the record linkage values computed from the multivariate swapping tree method were the smallest among all the methods. The performance of the proposed method was then examined on the information loss measures.

## 4.3. Performance Evaluation

The results of the experiments on the real-world data are shown in Table 1. In addition to the measures described in the previous section, times to generate masked data by each method are also reported. There are a total of six settings (three data sets × two attribute selection methods). The multivariate swapping tree method clearly outperforms the other two methods in all settings. It is the best in all information loss measures. Upon applying a paired t-test (Mitchell 1997) to each setting, we find that the differences in the information loss measures between the multivariate swapping tree method and the other two methods are all statistically significant at $\alpha =$ 0005 level, except in one case: In testing the Census data with one half of the nonconfidential attributes masked, the difference in regression MAPE results between microaggregation and the multivariate swapping trees is statistically insignificant. The record linkage values associated with the multivariate swapping trees are considerably smaller than those with the other two methods, which indicates that the proposed method is the best in preventing or limiting reidentification risk while leading to the least amount of information loss.

Table 1 Results of Primary Experiments on Real-World Data

<table><tr><td>Data</td><td>Method</td><td>Time (seconds)</td><td>Linkage (%)</td><td>ABISD (%)</td><td>ABICO (%)</td><td>Reg-MAPEa (%)</td><td>NN-MAPEb (%)</td></tr><tr><td>Offer</td><td>Original</td><td></td><td></td><td></td><td></td><td>10.46</td><td>10.66</td></tr><tr><td rowspan="3">All attsc</td><td>Microaggregation</td><td>0.2</td><td>8.24</td><td>-37.11</td><td>797.41</td><td>13.44</td><td>23.36</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>8.30</td><td>-28.43</td><td>330.01</td><td>14.30</td><td>20.61</td></tr><tr><td>Multivariate tree</td><td>0.1</td><td>3.16</td><td>0</td><td>279.59</td><td>10.52</td><td>12.53</td></tr><tr><td rowspan="3">Half attsd</td><td>Microaggregation</td><td>0.2</td><td>3.84</td><td>-30.96</td><td>272.55</td><td>11.61</td><td>19.77</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>3.89</td><td>-30.85</td><td>271.57</td><td>13.36</td><td>17.99</td></tr><tr><td>Multivariate tree</td><td>0.1</td><td>2.37</td><td>0</td><td>253.29</td><td>10.48</td><td>13.10</td></tr><tr><td>Census</td><td>Original</td><td></td><td></td><td></td><td></td><td>17.68</td><td>36.29</td></tr><tr><td rowspan="3">All atts.</td><td>Microaggregation</td><td>0.4</td><td>3.57</td><td>-20.59</td><td>236.02</td><td>37.54</td><td>125.03</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>3.57</td><td>-23.28</td><td>82.74</td><td>26.83</td><td>100.54</td></tr><tr><td>Multivariate tree</td><td>0.2</td><td>1.40</td><td>0</td><td>27.68</td><td>21.75</td><td>41.70</td></tr><tr><td rowspan="3">Half atts.</td><td>Microaggregation</td><td>0.4</td><td>2.92</td><td>-10.30</td><td>55.30</td><td>24.59</td><td>52.94</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>2.92</td><td>-16.27</td><td>52.52</td><td>29.04</td><td>59.66</td></tr><tr><td>Multivariate tree</td><td>0.2</td><td>1.00</td><td>0</td><td>28.32</td><td>24.11</td><td>47.45</td></tr><tr><td>Housing</td><td>Original</td><td></td><td></td><td></td><td></td><td>60.94</td><td>38.00</td></tr><tr><td rowspan="3">All atts.</td><td>Microaggregation</td><td>239.4</td><td>0.60</td><td>-29.16</td><td>231.73</td><td>77.56</td><td>71.07</td></tr><tr><td>Univariate tree</td><td>0.3</td><td>0.58</td><td>-29.87</td><td>250.32</td><td>64.74</td><td>86.48</td></tr><tr><td>Multivariate tree</td><td>4.3</td><td>0.10</td><td>0</td><td>34.57</td><td>61.88</td><td>46.78</td></tr><tr><td rowspan="3">Half atts.</td><td>Microaggregation</td><td>229.3</td><td>0.18</td><td>-29.34</td><td>90.40</td><td>75.15</td><td>82.03</td></tr><tr><td>Univariate tree</td><td>0.3</td><td>0.17</td><td>-22.89</td><td>88.32</td><td>68.65</td><td>50.15</td></tr><tr><td>Multivariate tree</td><td>4.2</td><td>0.05</td><td>0</td><td>29.62</td><td>61.81</td><td>43.47</td></tr></table>

Notes. <sup>a</sup>Average MAPE for regression. <sup>b</sup>Average MAPE for neural networks. <sup>c</sup>All nonconfidential attributes are masked. <sup>d</sup>One half of the nonconfidential attributes that are statistically most significant to the confidential attribute are masked.

Performance comparisons between microaggregation and univariate trees are mixed in terms of record linkage and information loss. However, it is clear that microaggregation requires longer running time than univariate trees (as well as multivariate trees). Therefore, univariate trees are a better choice than microaggregation when dealing with large data sets. A serious weakness with both microaggregation and univariate trees is the reduction in variance of the masked data. The proposed method, on the other hand, is unbiased in variance.

We observe that regression preserved the relationships between the masked and unmasked attributes better than neural networks for the Offer and Census data, particularly when microaggregation and univariate tree techniques are used. A possible explanation is that neural networks would require parameter tuning to improve their performance. We did not attempt to tune parameters because that would render the results less objective. Of course, the parameters used for neural networks are the same for all three techniques and, as mentioned earlier, the multivariate swapping tree approach outperforms the other two approaches regardless of whether regression or neural networks are used.

The results of the experiments on the simulated data, with eight different settings, are given in Table 2. In all settings, the record linkage values with the proposed method are significantly smaller than those with the other two methods, which indicates that our method is clearly superior to the other two methods in protecting identity disclosure. In terms of information loss measures, the proposed method still significantly outperforms the other two methods when all of the nonconfidential attributes are masked. However, when only one half of the nonconfidential attributes are masked, the advantages of the proposed method are not statistically significant in most regression and neural network cases. It appears that all three methods perform very well in these cases. This is likely because of the nature of the data—reasonably large data sets with multivariate normal distribution. The excellent performances in regression and neural networks are achieved even when the record linkage percentages appear to be very low for all methods. However, because these are relatively large data sets, the absolute numbers of linked records are not necessarily small.

Again, there is no clear evidence to indicate whether the microaggregation or the univariate trees method is better in terms of disclosure risk and information loss. However, the disadvantage of microaggregation regarding runtime is quite noticeable. The proposed algorithm runs very fast and clearly can be applied to much larger data sets.

Table 2 Results of Primary Experiments on Simulated Data

<table><tr><td>Data</td><td>Method</td><td>Time (seconds)</td><td>Linkage (%)</td><td>ABISD (%)</td><td>ABICO (%)</td><td>Reg-MAPE (%)</td><td>NN-MAPE (%)</td></tr><tr><td>MVN-5K</td><td>Original</td><td></td><td></td><td></td><td></td><td>26.38</td><td>25.89</td></tr><tr><td rowspan="3">All atts.</td><td>Microaggregation</td><td>5.8</td><td>1.14</td><td>-6.18</td><td>22.23</td><td>96.75</td><td>91.43</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>1.14</td><td>-7.14</td><td>16.17</td><td>83.98</td><td>65.88</td></tr><tr><td>Multivariate tree</td><td>0.5</td><td>0.30</td><td>0</td><td>2.45</td><td>26.49</td><td>26.57</td></tr><tr><td rowspan="3">Half atts.</td><td>Microaggregation</td><td>5.7</td><td>0.91</td><td>-6.51</td><td>19.96</td><td>26.42</td><td>32.45</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>0.69</td><td>-6.97</td><td>14.04</td><td>26.38</td><td>30.51</td></tr><tr><td>Multivariate tree</td><td>0.5</td><td>0.20</td><td>0</td><td>1.34</td><td> $26.38^a$ </td><td>26.68</td></tr><tr><td>MVN-10K</td><td>Original</td><td></td><td></td><td></td><td></td><td>27.75</td><td>28.19</td></tr><tr><td rowspan="3">All atts.</td><td>Microaggregation</td><td>29.8</td><td>0.81</td><td>-5.13</td><td>20.67</td><td>103.37</td><td>86.85</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>0.74</td><td>-5.76</td><td>14.02</td><td>81.04</td><td>65.21</td></tr><tr><td>Multivariate tree</td><td>1.0</td><td>0.18</td><td>0</td><td>1.52</td><td>27.78</td><td>28.60</td></tr><tr><td rowspan="3">Half atts.</td><td>Microaggregation</td><td>28.4</td><td>0.67</td><td>-5.45</td><td>19.24</td><td>27.76</td><td>28.55</td></tr><tr><td>Univariate tree</td><td>0.1</td><td>0.51</td><td>-5.45</td><td>11.27</td><td>27.86</td><td>29.22</td></tr><tr><td>Multivariate tree</td><td>1.0</td><td>0.15</td><td>0</td><td>0.90</td><td> $27.76^a$ </td><td> $28.27^a$ </td></tr><tr><td>MVN-15K</td><td>Original</td><td></td><td></td><td></td><td></td><td>27.21</td><td>34.37</td></tr><tr><td rowspan="3">All atts.</td><td>Microaggregation</td><td>73.0</td><td>0.64</td><td>-4.79</td><td>17.71</td><td>103.33</td><td>85.63</td></tr><tr><td>Univariate tree</td><td>0.2</td><td>0.52</td><td>-5.73</td><td>13.58</td><td>92.45</td><td>70.88</td></tr><tr><td>Multivariate tree</td><td>1.5</td><td>0.13</td><td>0</td><td>1.15</td><td>27.25</td><td>35.31</td></tr><tr><td rowspan="3">Half atts.</td><td>Microaggregation</td><td>71.1</td><td>0.46</td><td>-4.86</td><td>15.79</td><td>27.23</td><td>34.55</td></tr><tr><td>Univariate tree</td><td>0.2</td><td>0.38</td><td>-5.41</td><td>10.94</td><td>27.24</td><td>34.95</td></tr><tr><td>Multivariate tree</td><td>1.5</td><td>0.12</td><td>0</td><td>0.68</td><td> $27.22^a$ </td><td> $34.52^a$ </td></tr><tr><td>MVN-20K</td><td>Original</td><td></td><td></td><td></td><td></td><td>27.19</td><td>27.14</td></tr><tr><td rowspan="3">All atts.</td><td>Microaggregation</td><td>130.6</td><td>0.53</td><td>-4.62</td><td>15.79</td><td>117.00</td><td>111.08</td></tr><tr><td>Univariate tree</td><td>0.2</td><td>0.43</td><td>-5.58</td><td>12.56</td><td>107.20</td><td>83.78</td></tr><tr><td>Multivariate tree</td><td>2.1</td><td>0.11</td><td>0</td><td>1.12</td><td>27.22</td><td>27.66</td></tr><tr><td rowspan="3">Half atts.</td><td>Microaggregation</td><td>125.1</td><td>0.34</td><td>-4.54</td><td>12.85</td><td>27.20</td><td>27.36</td></tr><tr><td>Univariate tree</td><td>0.2</td><td>0.29</td><td>-5.36</td><td>9.87</td><td>27.21</td><td>27.59</td></tr><tr><td>Multivariate tree</td><td>2.0</td><td>0.10</td><td>0</td><td>0.49</td><td> $27.20^a$ </td><td> $27.21^a$ </td></tr></table>

<sup>a</sup>The result of the multivariate trees is not statistically significantly different from that of at least one of the methods for comparison (microaggregation and univariate trees).

There is an observable pattern that, as the data size increases, the average bias in correlation (ABICO) values produced by the proposed method decreases (for both the “all attributes” and the “half attributes” settings). This is consistent with Theorem 2. A similar behavior can also be observed from the results of microaggregation and univariate trees (although their ABICO values are much larger). For all three methods, the ABISD and ABICO values are significantly smaller on these simulated data sets than those on real-world data sets. This is likely because of the ideal setting of a multivariate normal distribution.

The proposed approach includes two new component methods: a multivariate tree-based datapartitioning method and a bounded swapping method. To examine the contributions from each component, we created two alternative methods for experimental comparisons. The first uses univariate trees for data partitioning but bounded swapping for data masking (labeled “Univar. tree − Swap” in Tables 3 and 4). The second uses multivariate trees for data partitioning but group average substitution for data masking (labeled “Multivar. tree − Avg.” in Tables 3 and 4). We ran the same cross-validation procedure as before for these two alternatives. The results are shown in Tables 3 and 4 for the real-world and simulated data, respectively. The results for the proposed combined method are also listed for comparison (labeled “Multivar. tree − Swap” in Tables 3 and 4 and as “Multivariate tree” in Tables 1 and 2).

Both alternative methods perform better overall than the existing microaggregation and univariate tree methods. It appears that using multivariate trees with group average is slightly better than using univariate trees with bounded swapping for the smaller data sets such as Offer and Census, while the latter is better for larger data sets such as Housing. The proposed combined method is able to take advantage of each component method and outperforms them in general. The only exception is in the Housing data, where univariate trees with bounded swapping perform as well as (if not better than) the proposed combined method as far as data utility is concerned (it is inferior in terms of privacy protection). Note that Theorems 2 and 3 are stated and derived based on the bounded swapping method. Therefore, when the data set is

Table 3 Results of Additional Experiments on Real-World Data

<table><tr><td>Data</td><td>Method</td><td>Time (seconds)</td><td>Linkage (%)</td><td>ABISD (%)</td><td>ABICO (%)</td><td>Reg-MAPE (%)</td><td>NN-MAPE (%)</td></tr><tr><td>Offer</td><td>Univar. tree – Swap</td><td>0.1</td><td>5.19</td><td>0</td><td>281.13</td><td>10.62</td><td>20.35</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree – Avg.</td><td>0.1</td><td>3.50</td><td>-21.40</td><td>280.11</td><td>10.96</td><td>16.78</td></tr><tr><td>Multivar. tree – Swap</td><td>0.1</td><td>3.16</td><td>0</td><td>279.59</td><td>10.52</td><td>12.53</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree – Swap</td><td>0.1</td><td>2.99</td><td>0</td><td>280.37</td><td>10.55</td><td>15.23</td></tr><tr><td>Multivar. tree – Avg.</td><td>0.1</td><td>2.48</td><td>-18.38</td><td>270.93</td><td>10.73</td><td>13.99</td></tr><tr><td>Multivar. tree – Swap</td><td>0.1</td><td>2.37</td><td>0</td><td>253.29</td><td>10.48</td><td>13.10</td></tr><tr><td>Census</td><td>Univar. tree – Swap</td><td>0.1</td><td>2.96</td><td>0</td><td>57.10</td><td>34.55</td><td>99.26</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree – Avg.</td><td>0.2</td><td>3.01</td><td>-14.86</td><td>72.87</td><td>33.67</td><td>84.06</td></tr><tr><td>Multivar. tree – Swap</td><td>0.2</td><td>1.40</td><td>0</td><td>27.68</td><td>21.75</td><td>41.70</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree – Swap</td><td>0.1</td><td>2.64</td><td>0</td><td>45.78</td><td>35.08</td><td>46.91</td></tr><tr><td>Multivar. tree – Avg.</td><td>0.2</td><td>2.43</td><td>-6.58</td><td>47.87</td><td>22.79</td><td>38.57</td></tr><tr><td>Multivar. tree – Swap</td><td>0.2</td><td>1.00</td><td>0</td><td>28.32</td><td>24.11</td><td>47.45</td></tr><tr><td>Housing</td><td>Univar. tree – Swap</td><td>0.4</td><td>0.29</td><td>0</td><td>39.30</td><td>60.94</td><td>43.71</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree – Avg.</td><td>3.5</td><td>0.40</td><td>-17.33</td><td>89.58</td><td>66.12</td><td>48.82</td></tr><tr><td>Multivar. tree – Swap</td><td>4.3</td><td>0.10</td><td>0</td><td>34.57</td><td>61.88</td><td>46.78</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree – Swap</td><td>0.4</td><td>0.10</td><td>0</td><td>24.88</td><td>61.25</td><td>41.01</td></tr><tr><td>Multivar. tree – Avg.</td><td>2.9</td><td>0.14</td><td>-12.95</td><td>41.60</td><td>66.70</td><td>43.71</td></tr><tr><td>Multivar. tree – Swap</td><td>4.2</td><td>0.05</td><td>0</td><td>29.62</td><td>61.81</td><td>43.47</td></tr></table>

large, the benefit of bounded swapping is expected to be more significant while multivariate partitioning might not be as important. For the simulated data, both alternative methods perform very well particularly for regression and neural networks. Again, this is most likely because of the ideal setting of a multivariate normal distribution. Note that although the ABICO values from univariate trees with bounded swapping are somewhat larger for smaller data sets when all nonconfidential attributes are masked, they are still much better than those of the two existing methods.

## 5. Conclusions and Future Work

We have presented a tree-based bounded swapping method for protecting privacy against reidentification by record linkage. We have shown analytically that the proposed method possesses some highly desirable statistical properties that do not depend on any assumptions about the distributions of the data. Our empirical study has demonstrated that the method is very effective in handling data with different characteristics. The proposed approach has significant management and policy implications. As record linkage and related data-mining techniques are increasingly used in areas such as antiterrorism, crime analysis, epidemiologic research, database marketing, and information retrieval, there is a rising public sentiment that individual privacy is being severely eroded. Our proposed approach addresses this important issue and provides a solution to resolve the conflict between data sharing and dissemination and privacy protection.

Table 4 Results of Additional Experiments on Simulated Data

<table><tr><td>Data</td><td>Method</td><td>Time (seconds)</td><td>Linkage (%)</td><td>ABISD (%)</td><td>ABICO (%)</td><td>Reg-MAPE (%)</td><td>NN-MAPE (%)</td></tr><tr><td>MVN-5K</td><td>Univar. tree - Swap</td><td>0.1</td><td>0.79</td><td>0</td><td>8.69</td><td>26.55</td><td>26.78</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree - Avg.</td><td>0.4</td><td>0.79</td><td>-2.90</td><td>3.22</td><td>26.84</td><td>26.93</td></tr><tr><td>Multivar. tree - Swap</td><td>0.5</td><td>0.30</td><td>0</td><td>2.45</td><td>26.49</td><td>26.57</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree - Swap</td><td>0.1</td><td>0.69</td><td>0</td><td>2.42</td><td>26.50</td><td>26.70</td></tr><tr><td>Multivar. tree - Avg.</td><td>0.4</td><td>0.74</td><td>-2.40</td><td>2.50</td><td>26.39</td><td>26.34</td></tr><tr><td>Multivar. tree - Swap</td><td>0.5</td><td>0.20</td><td>0</td><td>1.34</td><td>26.42</td><td>26.68</td></tr><tr><td>MVN-10K</td><td>Univar. tree - Swap</td><td>0.1</td><td>0.31</td><td>0</td><td>6.27</td><td>27.85</td><td>28.67</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree - Avg.</td><td>0.9</td><td>0.38</td><td>-2.82</td><td>3.92</td><td>27.89</td><td>28.61</td></tr><tr><td>Multivar. tree - Swap</td><td>1.0</td><td>0.18</td><td>0</td><td>1.52</td><td>27.78</td><td>28.60</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree - Swap</td><td>0.1</td><td>0.37</td><td>0</td><td>1.86</td><td>27.82</td><td>28.64</td></tr><tr><td>Multivar. tree - Avg.</td><td>0.9</td><td>0.36</td><td>-2.30</td><td>2.86</td><td>27.75</td><td>28.76</td></tr><tr><td>Multivar. tree - Swap</td><td>1.0</td><td>0.15</td><td>0</td><td>0.90</td><td>27.76</td><td>28.27</td></tr><tr><td>MVN-15K</td><td>Univar. tree - Swap</td><td>0.2</td><td>0.22</td><td>0</td><td>4.59</td><td>27.38</td><td>35.04</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree - Avg.</td><td>1.4</td><td>0.32</td><td>-2.00</td><td>3.18</td><td>27.75</td><td>36.93</td></tr><tr><td>Multivar. tree - Swap</td><td>1.5</td><td>0.13</td><td>0</td><td>1.15</td><td>27.25</td><td>35.31</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree - Swap</td><td>0.2</td><td>0.22</td><td>0</td><td>1.92</td><td>27.34</td><td>34.61</td></tr><tr><td>Multivar. tree - Avg.</td><td>1.4</td><td>0.28</td><td>-1.78</td><td>2.93</td><td>27.28</td><td>35.40</td></tr><tr><td>Multivar. tree - Swap</td><td>1.5</td><td>0.12</td><td>0</td><td>0.68</td><td>27.22</td><td>34.52</td></tr><tr><td>MVN-20K</td><td>Univar. tree - Swap</td><td>0.2</td><td>0.15</td><td>0</td><td>2.80</td><td>27.32</td><td>27.73</td></tr><tr><td rowspan="2">All atts.</td><td>Multivar. tree - Avg.</td><td>2.0</td><td>0.29</td><td>-1.90</td><td>2.09</td><td>27.24</td><td>27.97</td></tr><tr><td>Multivar. tree - Swap</td><td>2.1</td><td>0.11</td><td>0</td><td>1.12</td><td>27.22</td><td>27.66</td></tr><tr><td rowspan="3">Half atts.</td><td>Univar. tree - Swap</td><td>0.2</td><td>0.24</td><td>0</td><td>1.15</td><td>27.27</td><td>27.69</td></tr><tr><td>Multivar. tree - Avg.</td><td>1.9</td><td>0.23</td><td>-1.60</td><td>2.43</td><td>27.27</td><td>27.76</td></tr><tr><td>Multivar. tree - Swap</td><td>2.0</td><td>0.10</td><td>0</td><td>0.49</td><td>27.20</td><td>27.21</td></tr></table>

The basic idea behind the proposed method in terms of data utility is to preserve the original joint distribution via multivariate partitioning of the data. For predictive data analysis such as regression, it may be more effective to preserve the conditional distribution (i.e., conditioning the dependent variable on the independent variables). One approach to this problem, along the same direction as in this research, is to use regression trees for data partitioning. An additional advantage of a regression tree is that it can easily handle categorical dependent variables. An interesting area of future research is to develop a regression tree-based approach for the purposes of regression and other predictive data analyses.

## Acknowledgments

The authors thank the associate editor and three anonymous reviewers for their insightful comments and suggestions that improved the paper considerably.

## Appendix. Proofs of Lemmas and Theorems in §3

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>1.</sup> The data structure of the multivariate tree is the same as a kd-tree. It is well-known that the time to build a kd-tree is of order O4N log N 5 (Friedman and Bentley 1977). Briefly, the depth of the kd-tree is log N because it is a balanced binary tree. At each level of the tree, it takes O4MN 5 time to find the attribute with maximum variance for splitting the data, where M is the total number of attributes. Thus, the total time complexity is of O4MN log N 5, which simplifies to O4N log N 5 because N is typically several orders of magnitude larger than M. The multivariate tree differs from the kd-tree in that it uses the first principal component instead of the maximum-variance attribute for splitting the data. At each level, the time to compute the first principal component is of order O4M<sup>2</sup>N 5 (Sharma and Paliwal 2007). Therefore, the total time complexity still reduces to O4N log N 5 because N is normally also much larger than M<sup>2</sup>. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>2.</sup> We have shown in Lemma 1 that the multivariate data-partitioning part of the algorithm takes O4N log N 5 time. The bounded swapping part of the algorithm involves sorting attribute values within each partition and then making swaps. At each leaf, it takes O4mã log ã5 time for sorting and O4mã5 time for swapping, where m is the number of masked attributes. Thus, for a tree with T leaves, the total operation takes O4Tmã4log ã + 155 ≈ O4mN log ã5 time, which simplifies to O4N log ã5 because m is typically much smaller than N . Because O4N log ã5 < O4N log N 5, the time complexity of the entire procedure is still of O4N log N 5. <sup></sup>

Proof of Lemma 3. <sub>Consider</sub>

$$
x _ {i j \mid t} - \overline {{X}} _ {j} = (\bar {x} _ {j \mid t} - \overline {{X}} _ {j}) + (x _ {i j \mid t} - \bar {x} _ {j \mid t})
$$

and

$$
x _ {i k \mid t} - \overline {{X}} _ {k} = (\bar {x} _ {k \mid t} - \overline {{X}} _ {k}) + (x _ {i k \mid t} - \bar {x} _ {k \mid t}).
$$

Multiplying the left- and right-hand sides of the above two equations, respectively, we have

$$
\begin{array}{r l} & (x _ {i j \mid t} - \overline {{X}} _ {j}) (x _ {i k \mid t} - \overline {{X}} _ {k}) \\ & \quad = (\bar {x} _ {j \mid t} - \overline {{X}} _ {j}) (\bar {x} _ {k \mid t} - \overline {{X}} _ {k}) + (\bar {x} _ {j \mid t} - \overline {{X}} _ {j}) (x _ {i k \mid t} - \bar {x} _ {k \mid t}) \\ & \quad + (x _ {i j \mid t} - \bar {x} _ {j \mid t}) (\bar {x} _ {k \mid t} - \overline {{X}} _ {k}) + (x _ {i j \mid t} - \bar {x} _ {j \mid t}) (x _ {i k \mid t} - \bar {x} _ {k \mid t}). \end{array}\tag{22}
$$

Summing over all the records and noting that the summations for the middle two terms in the right-hand side of (22) equal zero, we get

$$
\begin{array}{l} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (x _ {i j | t} - \overline {{X}} _ {j}) (x _ {i k | t} - \overline {{X}} _ {k}) \\ \qquad = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (\bar {x} _ {j | t} - \overline {{X}} _ {j}) (\bar {x} _ {k | t} - \overline {{X}} _ {k}) \\ \qquad + \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (x _ {i j | t} - \bar {x} _ {j | t}) (x _ {i k | t} - \bar {x} _ {k | t}). \end{array}\tag{23}
$$

Equation (23) is equivalent to Equation (6). <sup></sup>

Proof of Lemma 4. <sub>Let</sub> $y _ { i j \mid t }$ be the value of $Y _ { j }$ in the ith record in leaf t, and let $\bar { y } _ { j \mid t }$ be the mean of the $Y _ { i }$ values in leaf t. It follows from Theorem 1 that ${ \bar { Y } } _ { i } = { \bar { X } } _ { i } , \ { \bar { Y } } _ { k } = { \bar { X } } _ { k } ,$ $\bar { y } _ { j \mid t } = \bar { x } _ { j \mid t } ,$ and $\bar { y } _ { k \mid t } = \bar { x } _ { k \mid t } , \forall t .$ . Applying these relationships to Equation (23), the between-group sum of cross products terms cancel out, which results in Equation (14). <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Theorem</sup> <sup>2.</sup> Given Theorem 1, it suffices to prove that

$$
\operatorname{plim} \operatorname{Cov} (Y _ {j}, Y _ {k}) = \operatorname{Cov} (X _ {j}, X _ {k}), \quad \forall j, k.\tag{24}
$$

It follows from Equations (14) and (4) that

$$
\begin{array}{l} T S C P (Y _ {j}, Y _ {k}) - T S C P (X _ {j}, X _ {k}) \\ = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} [ (y _ {i j | t} - \bar {y} _ {j | t}) (y _ {i k | t} - \bar {y} _ {k | t}) - (x _ {i j | t} - \bar {x} _ {j | t}) (x _ {i k | t} - \bar {x} _ {k | t}) ] \\ = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} (y _ {i j | t} y _ {i k | t} - x _ {i j | t} x _ {i k | t}). \end{array} \tag {25}
$$

Let $d _ { i j | t } = y _ { i j | t } - x _ { i j | t }$ and $d _ { i k \mid t } = y _ { i k \mid t } - x _ { i k \mid t }$ . It is clear that $d _ { i j | t }$ and $d _ { i k \mid t }$ are inversely proportional to N for a fixed ã. This is because (given a fixed ã) the larger the value of $N ,$ the more densely the data points are distributed (because all data are taken from the same population) and thus the smaller the ranges of the partitioned subsets. Therefore, $| d _ { i j | t } | \propto 1 / N$ and $| d _ { i k | t } | \propto 1 / N$ . It follows from (25) that for every $j , k ,$

$$
\begin{array}{l} \operatorname{plim} [ T S C P (Y _ {j}, Y _ {k}) - T S C P (X _ {j}, X _ {k}) ] \\ = \operatorname{plim} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} [ (x _ {i j | t} + d _ {i j | t}) (x _ {i k | t} + d _ {i k | t}) - x _ {i j | t} x _ {i k | t} ] \\ = \operatorname{plim} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} [ x _ {i j | t} d _ {i k | t} + x _ {i k | t} d _ {i j | t} + d _ {i j | t} d _ {i k | t} ] \\ \propto \operatorname{plim} \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {n _ {t}} \left[ \frac {x _ {i j | t}}{N} + \frac {x _ {i k | t}}{N} + \frac {1}{N ^ {2}} \right] = \overline {{X}} _ {j} + \overline {{X}} _ {k}. \end{array}\tag{26}
$$

That is, the difference in total sum of cross-products converges in probability to a finite quantity. Dividing TSCP4 · 5 in (26) by N (or a “degree of freedom” quantity that is in the same scale as N 5, we have

$$
\operatorname{plim} \left[ \operatorname{Cov} (Y _ {j}, Y _ {k}) - \operatorname{Cov} (X _ {j}, X _ {k}) \right] = 0, \quad \forall j, k. \quad \square
$$

<sup>Proof</sup> <sup>of</sup> <sup>Theorem</sup> <sup>3.</sup> Let x° and S be the sample mean vector and covariance matrix of $\mathbf { X } = \left[ X _ { 0 } \mid \mathbf { X } _ { 1 } \right]$ , where $X _ { 0 }$ is the dependent variable. Let S<sup>˜</sup> be the covariance matrix based on the mask data. Partition these parameters as follows:

$$
\bar {\mathbf {x}} = \left[ \begin{array}{c} \bar {x} _ {0} \\ \bar {\mathbf {x}} _ {1} \end{array} \right], \quad \mathbf {S} = \left[ \begin{array}{c c} s _ {0 0} & \mathbf {s} _ {0 1} \\ \mathbf {s} _ {1 0} & \mathbf {S} _ {1 1} \end{array} \right] \quad \text {and} \tilde {\mathbf {S}} = \left[ \begin{array}{c c} \tilde {s} _ {0 0} & \tilde {\mathbf {s}} _ {0 1} \\ \tilde {\mathbf {s}} _ {1 0} & \tilde {\mathbf {S}} _ {1 1} \end{array} \right].
$$

Note that x° remains exactly the same after masking, so it is not necessary to use another symbol for the masked version of x°.

The regression intercept and slope parameters can be computed using the sample mean vector and the covariance matrix as follows:

$$
a = \bar {x} _ {0} - \mathbf {s} _ {0 1} \mathbf {S} _ {1 1} ^ {- 1} \bar {\mathbf {x}} _ {1}, \quad \text { and } \quad \mathbf {b} = \mathbf {S} _ {1 1} ^ {- 1} \mathbf {s} _ {1 0}.
$$

From the Slutsky theorem (Greene 1993, pp. 101–102) and Theorem $^ { 2 , }$ we have

$$
\mathrm{plim} \tilde {a} = \mathrm{plim} (\bar {x} _ {0} - \tilde {\mathbf {s}} _ {0 1} \tilde {\mathbf {S}} _ {1 1} ^ {- 1} \overline {{\mathbf {x}}} _ {1}) = \bar {x} _ {0} - \mathbf {s} _ {0 1} \mathbf {S} _ {1 1} ^ {- 1} \overline {{\mathbf {x}}} _ {1} = a
$$

and

$$
\operatorname{plim} \tilde {\mathbf {b}} = \operatorname{plim} (\tilde {\mathbf {S}} _ {1 1} ^ {- 1} \tilde {\mathbf {s}} _ {1 0}) = \mathbf {S} _ {1 1} ^ {- 1} \mathbf {s} _ {1 0} = \mathbf {b}. \quad \square
$$

## References

Adam, N. R., J. C. Wortmann. 1989. Security-control methods for statistical databases: A comparative study. ACM Comput. Surveys 21(4) 515–556.

Al-Lawati, A., D. Lee, P. McDaniel. 2005. Blocking-aware private record linkage. Proc. 2nd Internat. Workshop on Information Quality in Information Systems (IQIS), ACM Press, New York, 59–68.

Boruch, R. F., T. Victor, J. S. Cecil. 2000. Resolving ethical and legal problems in randomized experiments. Crime Delinquency 46(3) 330–353.

Bradley, P. S., U. M. Fayyad, O. L. Mangasarian. 1999. Mathematical programming for data mining: Formulations and challenges. INFORMS J. Comput. 11(3) 217–238.

Brand, R., J. Domingo-Ferrer, J. M. Mateo-Sanz. 2002. Reference data sets to test and compare SDC methods for protection of numerical microdata. Retrieved July 1, 2006, http://neon.vb.cbs.nl/casc/.

Churches, T., P. Christen. 2004. Some methods for blindfolded record linkage. BMC Medical Informatics Decision Making 4(9) 17.

Cox, L. H. 1995. Network models for complementary cell suppression. J. Amer. Statist. Assoc. 90(432) 1453–1462.

Cox, L. H., R. F. Boruch. 1988. Record linkage, privacy and statistical policy. J. Official Statist. 4(1) 3–16.

Defays, D., P. Nanopoulos. 1993. Panels of enterprises and confidentiality: The small aggregates method. Proc. Statist. Canada Sympos. 1992 Design Anal. Longitudinal Surveys, Ottawa, ON, Canada, 195–204.

Domingo-Ferrer, J., J. M. Mateo-Sanz. 2002. Practical data-oriented microaggregation for statistical disclosure control. IEEE Trans. Knowledge Data Engrg. 14(1) 189–201.

Domingo-Ferrer, J., V. Torra. 2001. A quantitative comparison of disclosure control methods for microdata. P. Doyle, J. Lane, J. Theeuwes, L. Zayatz, eds. Confidentiality, Disclosure and Data Access: Theory and Practical Applications for Statistical Agencies. North-Holland, Amsterdam, 111–134.

Duncan, G. T., S. Mukherjee. 2000. Optimal disclosure limitation strategy in statistical databases: Deterring tracker attacks through additive noise. J. Amer. Statist. Assoc. 95(451) 720–729.

Fellegi, I. P. 1997. Record linkage and public policy—A dynamic evolution. W. Alvey, B. Jamerson, eds. Record Linkage Techniques—1997. Proc. Internat. Workshop Exposition, Federal Committee, Washington, DC, 3–12.

Fellegi, I. P., A. B. Sunter. 1969. A theory for record linkage. J. Amer. Statist. Assoc. 64(328) 1183–1210.

Friedman, J. H., J. L. Bentley. 1977. An algorithm for finding best matches in logarithmic expected time. ACM Trans. Math. Software 3(3) 209–226.

Galletta, D. 2004. MIS faculty salary survey results. Retrieved March 1, http://www.pitt.edu/∼galletta/salsurv.html.

Garfinkel, R., R. Gopal, S. Thompson. 2007. Releasing individually identifiable microdata with privacy protection against stochastic threat: An application to health information. Inform. Systems Res. 18(1) 23–41.

Graybill, F. A. 1976. Theory and Application of the Linear Model. Wadsworth, Pacific Grove, CA.

Greene, W. H. 1993. Econometric Analysis. Macmillan, New York.

Hansen, S. L., S. Mukherjee. 2003. A polynomial algorithm for optimal univariate microaggregation. IEEE Trans. Knowledge Data Engrg. 15(4) 1043–1044.

Hundepool, A., L. Willenborg. 1996. - and -ARGUS: Software for statistical disclosure control. Proc. 3rd Internat. Seminar Statist. Confidentiality, Bled, Slovenia.

Johnson, R. A., D. W. Wichern. 2002. Applied Multivariate Statistical Analysis. Prentice Hall, Upper Saddle River, NJ.

KDnuggets. 2006. Google subpoena: Child protection vs. privacy. Retrieved July 1, http://www.kdnuggets.com/polls/ 2006/google\_subpoena.htm.

Laszlo, M., S. Mukherjee. 2005. Minimum spanning tree partitioning algorithm for microaggregation. IEEE Trans. Knowledge Data Engrg. 17(7) 902–911.

Li, X.-B., S. Sarkar. 2006a. A tree-based data perturbation approach for privacy-preserving data mining. IEEE Trans. Knowledge Data Engrg. 18(9) 1278–1283.

Li, X.-B., S. Sarkar. 2006b. Privacy protection in data mining: A perturbation approach for categorical data. Inform. Systems Res. 17(3) 254–270.

Liew, C. K., U. J. Choi, C. J. Liew. 1985. A data distortion by probability distribution. ACM Trans. Database Systems 10(3) 395–411.

Lindell, Y., B. Pinkas. 2002. Privacy preserving data mining. J. Cryptology 15(3) 177–206.

Machanavajjhala, A., J. Gehrke, D. Kifer, M. Venkitasubramaniam. 2006. l-diversity: Privacy beyond k-anonymity. Proc. 22nd IEEE Internat. Conf. Data Engrg. (ICDE 2006), IEEE Computer Science Society, Washington, DC, 24–35.

MacQueen, J. B. 1967. Some methods for classification and analysis of multivariate observations. Proc. 5th Berkeley Sympos. Math. Statist. Probab. Berkeley, CA, 281–297.

Mitchell, T. M. 1997. Machine Learning. McGraw-Hill, New York.

Moore, R. A. 1996. Controlled data swapping for masking public use microdata sets. Statistical Research Division Report, Series RR96/04, U.S. Census Bureau, Washington, DC.

Newcombe, H. B., J. M. Kennedy. 1962. Record linkage: Making maximum use of the discriminating power of identifying information. Comm. ACM 5(13) 563–566.

Newcombe, H. B., J. M. Kennedy, S. J. Axford, A. P. James. 1959. Automatic linkage of vital records. Science 130(3389) 954–959.

O’Keefe, C. M., M. Yung, L. Gu, R. Baxter. 2004. Privacy-preserving data linkage protocols. Proc. 2004 ACM Workshop Privacy Electronic Soc., ACM Press, New York, 94–102.

Pagliuca, D., G. Seri. 1999. Some results of individual ranking method on the system of enterprise accounts annual survey, Esprit SDC Project, Deliverable MI-3/D2.

Samarati, P. 2001. Protecting respondents’ identities in microdata release. IEEE Trans. Knowledge Data Engrg. 13(6) 1010–1027.

Seifert, J. W. 2006. Data mining and homeland security: An overview. CRS Report for Congress, January 27. Retrieved July 1, http://www.fas.org/sgp/crs/intel/RL31798.pdf.

Sharma, A., K. K. Paliwal. 2007. Fast principal component analysis using fixed-point algorithm. Pattern Recognition Lett. 28(10) 1151–1155.

Sweeney, L. 2002. k-Anonymity: A model for protecting privacy. Internat. J. Uncertainty Fuzziness Knowledge-Based Systems 10(5) 557–570.

Sweeney, L. 2005. Privacy-enhanced linking. SIGKDD Explorations 7(2) 72–75.

Teltzrow, M., A. Kobsa. 2004. Impacts of user privacy preferences on personalized systems: A comparative study. Designing Personalized User Experiences in eCommerce. Kluwer Academic Publishers, Dordrecht, The Netherlands, 315–332.

Torgo, L. 1996. Housing data. Retrieved January 1, http:// www.cs.waikato.ac.nz/ml/weka/.

Traub, J. F., Y. Yemini, H. Wozniakowski. 1984. The statistical security of a statistical database. ACM Trans. Database Systems 9(4) 672–679.

U.S. General Accounting Office. 2001. Record linkage and privacy: Issues in creating new federal research and statistical information. Report GAO-01-126SP, GAO, Washington, DC. Retrieved July 1, http://www.gao.gov/new.items/ d01126sp.pdf.

Winkler, W. E. 2007. Examples of easy-to-implement, widely used methods of masking for which analytic properties are not justified. Census Bureau Research Report Series (Statistics #2007-21). Retrieved March 1, http://www.census .gov/srd/papers/pdf/rrs2007-21.pdf.

Witten, I. H., E. Frank. 2005. Data Mining: Practical Machine Learning Tools and Techniques. Morgan Kaufmann, San Francisco.
