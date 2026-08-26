---
otero_id: 4112
otero_key: "EXHNPEGE"
title: "Assessing the quality of large-scale data standards: A case of XBRL GAAP Taxonomy"
authors: "Hongwei Zhu; Harris Wu"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.01.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessing the quality of large-scale data standards: A case of XBRL GAAP Taxonomy

Hongwei Zhu <sup>a,</sup>⁎, Harris Wu <sup>b</sup>

<sup>a</sup> Department of Operations and Information Systems, Manning School of Business, University of Massachusetts Lowell, Lowell, MA 01854, United States

<sup>b</sup> Department of Information Technology and Decision Sciences, College of Business and Public Administration, Old Dominion University, Norfolk, VA 23529, United States

## a r t i c l e i n f o

Article history: Received 12 May 2013 Received in revised form 8 January 2014 Accepted 17 January 2014 Available online 24 January 2014

Keywords: Information quality Data quality Data standards Quality assessment XBRL GAAP Taxonomy

## a b s t r a c t

Data standards are often used by multiple organizations to produce and exchange data. Given the high cost of developing data standards and their signi<sup>fi</sup>cant impact on the interoperability of data produced using the standards, the quality of data standards must be systematically measured. We develop a framework for systematically assessing the quality of large-scale data standards using automated tools. It consists of metrics for intrinsic and contextual quality dimensions, as well as effectual metrics that assess the extent to which a standard enables data interoperability. We evaluate the quality assessment framework using two versions of a large <sup>fi</sup>nancial reporting standard, the US GAAP Taxonomy, and public companies' <sup>fi</sup>nancial statements created using the Taxonomy. Evaluation results con<sup>fi</sup>rm the effectiveness of the framework. Findings from the evaluation also offer valuable insights to decision makers who develop and improve data standards, select and adopt data standards, or consume standards-based data.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

Data standards specify data elements to be used by multiple organizations to create data that can be exchanged and processed unambiguously. Large-scale data standards, such as those within the US Department of Defense [52] and across the real estate mortgage industry [32], include many data elements and are intended for use by a large number of organizations. Such data standards are costly to develop and can have a signi<sup>fi</sup>cant impact on organizations that use the standards. Systematic methods for measuring the quality of large-scale data standards are needed to aid the development, implementation, and evolvement of data standards.

Despite extensive work in the areas of data and information quality [18,30,54,56,66], little has been done to create automated methods for assessing the quality of data standards. We attempt to <sup>fi</sup>ll this research gap by developing a framework with metrics and automatic methods to systematically assess the quality of large-scale data standards. The framework offers methods to answer fundamental questions about a data standard, such as: Is the standard complex? Does the standard have everything I need? Do I need everything in the standard? Does the standard accomplish its primary objective? We evaluate the framework using real-world data standards and the corresponding data instances in the <sup>fi</sup>nancial domain. The standards are the United States Generally Accepted Accounting Principles (GAAP) Taxonomy released in 2009 and then revised in 2011. The two versions of the Taxonomy are speci<sup>fi</sup>ed using the eXtensible Business Markup Language (XBRL) [70]. The Securities and Exchange Commission (SEC) has adopted both the 2009 and 2011 versions of the GAAP Taxonomy and mandated the public companies to use either version to create their <sup>fi</sup>nancial statements. The data instances are of<sup>fi</sup>cial <sup>fi</sup>nancial statements encoded in XBRL, submitted to the SEC by publicly traded companies.

Our work makes four contributions to both research and practice. (1) The framework consists of a small number of quality metrics for four primary aspects of data standard quality. Thus it is not only compact and easy to implement, but also informative and relatively comprehensive. (2) The contextual and effectual metrics of the framework are novel. The contextual metrics measure how well a data standard <sup>fi</sup>ts users' needs. The effectual metrics objectively measure how well a standard has accomplished its primary objective of achieving semantic data interoperability. We are not aware of the same standard quality metrics elsewhere in extant literature. (3) For each metric we implement an automated method to obtain the measurement. Evaluation shows that the metrics are effective for large-scale automated measurements. We evaluate the framework using XBRL taxonomies and data instances. The methods are applicable to any data standards speci<sup>fi</sup>ed using a formal language such as XML. (4) The framework and the evaluation also directly answer the call for increased professional relevance in decision support systems research [14]. The SEC has tasked the Financial Accounting Standards Board (FASB) to continuously “improve” the GAAP Taxonomy. The methods and <sup>fi</sup>ndings of this research are apparently useful to decision makers such as those at FASB and other standards development organizations.

The rest of the paper is organized as follows. Section 2 reviews related research to justify the need for effective measurement of data standard quality. Section 3 describes the metrics of the framework. Section 4 presents the evaluation method and brie<sup>fl</sup>y describes the data standards and the corresponding data used for the evaluation. Section 5 presents the evaluation results. Section 6 discusses the characteristics of this research. Section 7 concludes the paper and points out directions of future research.

## 2. Related work

Our work is closely related to three bodies of literature: (1) data quality, (2) quality of schema, ontology, and other forms of metadata, and (3) quality of XBRL data and XBRL taxonomies.

Data standards are a form of metadata, thus certain theories and concepts of data quality can be adapted to examine the quality of data standards. Most data quality research has focused on data, not the standards used to create and organize the data. The extant data quality research has identi<sup>fi</sup>ed useful quality dimensions and developed assessment methods that use objective metrics or survey instruments [9,13,26,40,59,67]. The dimensions, whether discovered using the survey method or based on theories, can be grouped into categories such as intrinsic, contextual, and representational [59,67]. Although the methods and results of data quality research are useful to this study, they must be adapted to consider the unique characteristics and purposes of data standards. Furthermore, many data quality metrics in extant research rely on subjective, human assessment that can be biased, labor intensive, and costly to implement in practice.

Quality of database schemas and data integration schemas is discussed in [2,19,49]. Among the quality aspects introduced, completeness and minimality (i.e., no redundancy) are most relevant to data standards. Because of the differences in use contexts, we need to develop metrics and measurement methods suitable for data standards.

Metadata in digital libraries and library information systems plays an important role in organizing and searching information items. Metadata quality has been studied in the library and information science community [9,40,44,58,60]. Most of their work examines the metadata values. For example, completeness is often determined by whether values for metadata such as author and title are supplied for each information item [68]. This line of research concerns issues in standardsbased data, which is relevant, but it does not address the key questions regarding the quality of data standards.

Ontology is often used for sharing knowledge, developing intelligent systems, and enabling semantic integration of data [18,31,39,63]. With the growth of the Semantic Web [3,53], ontology engineering has emerged as a research stream, with a number of studies focusing on ontology quality [10,21,23,42,57,62]. This line of research has been in<sup>fl</sup>uenced by earlier work on the quality of conceptual modeling [27], which is extended in subsequent studies [25,35–37]. Existing approaches often rely on intuition or theories such as semiotic theory to identify the dimensions of ontology quality, and most evaluations have used relatively small “toy ontologies” [10,55]. Studies on the complexity of ontology have used graph theoretic or entropy-based metrics adapted from software complexity [24,33,69,72]. Other quality metrics, such as cohesion and coupledness, are speci<sup>fi</sup>c to ontology implementation and application [28,41,71]. Thus not all ontology metrics are applicable to data standards. Ontology quality metrics do not examine how ontology is being used, and yet, how users use data standards is a crucial component of measuring the standards' quality.

Numerous papers have been written on the topic of XBRL [50], however, only a few studies focus on the quality of XBRL data and XBRL taxonomies. In an earlier study [7], a manual inspection of line items in <sup>fi</sup>nancial statements of 69 companies was used to examine whether a preliminary taxonomy met the reporting needs of most companies. Manual inspection continued to be used in studies to examine if companies properly used XBRL taxonomies [1,5,6]. While the manual approach can reveal deep issues such as violation of reporting convention and inconsistency between XBRL version and non-XBRL version of <sup>fi</sup>nancial statements, it is labor intensive and not applicable at a large scale. Commercial software tools were used in [12] on approximately 100 XBRL <sup>fi</sup>nancial statements, then manual efforts were used to examine error and warning messages generated by the tools. It was still a manual approach and its results depend on the particular implementation of the software tools. Automated tools have been suggested to perform large-scale analysis [7,8], which holds great potential to advance both research and practice of standard quality management as demonstrated in recent studies that examined only one or two aspects of quality [74,75].

A recent study identi<sup>fi</sup>es dozens of aspects for quality data standards in terms of the end product, the development process, and the implementation and use of data standards [22]. The measurement of these aspects relies on the use of an instrument that requires human input. Thus it is labor intensive to obtain a measurement and the results are subjective.

Clearly, there is a need for systematic methods to ef<sup>fi</sup>ciently and ob jectively measure the quality of large-scale data standards. This work aims to address such a need.

## 3. Framework for quality of data standards

We develop the framework with three underlying design principles. First, quality is based on the notion of “<sup>fi</sup>tness for use”. Thus the framework must examine not only a data standard itself, but also whether the standard meets users' needs as well as how well the standard leads to interoperable data. Second, the framework must consist of metrics that can be algorithmically measured so that they are applicable to large-scale data standards. There are two aspects of “large-scale”: the standard itself is large, and the number of its users is large. Third, the framework must be compact and informative. The framework does not need to cover every aspect of data standard quality. Rather, the framework should be <sup>fi</sup>t for use by practitioners who prefer a small number of dimensions for quality assessment [46].

## 3.1. Quality dimensions

We de<sup>fi</sup>ne the quality of a data standard as the standard's <sup>fi</sup>tness for multiple users to produce interoperable data. Following this de<sup>fi</sup>nition and the design principles discussed earlier, we identify four “usecentric” dimensions that indicate the quality of data standards from intrinsic, contextual, and effectual aspects, as summarized in Table 1.

Complexity of a data standard affects the correct understanding and appropriate use of the standard due to limitations of users' cognitive capacity [34,61]. Risks of unintended consequences also increase with increasing complexity of information systems [11,29,38,45], of which data standards are often an important part. A number of factors impact standards complexity, such as the complexity of the underlying domain, the amount of the information needing to be captured, and the diverse needs and preferences of various stakeholders. A standard should be kept as simple as possible. But certain stakeholders may prefer high complexity (e.g., technology suppliers may prefer high complexity as it will increase the demand of their products). Thus it is important to measure and manage standards complexity to minimize misunderstanding and misuse of data standards. Aside from complexity, misuse can be exacerbated when users of a standard are not provided with suf<sup>fi</sup>cient incentives for producing standards-based data [51]. Although the perceived complexity of a data standard may differ among users with differing levels of expertise, complexity is generally intrinsic to a given standard and we will develop metrics to measure this intrinsic dimension.

Completeness of a data standard indicates whether the standard contains the speci<sup>fi</sup>cations of all data elements and relationships needed by the user. Relevancy of a data standard indicates whether the standard contains the speci<sup>fi</sup>cations of only the data elements and the relationships needed by the user. Apparently, these two dimensions depend on the speci<sup>fi</sup>c usage contexts of various users. In practice, a data standard sometimes lacks the necessary completeness and relevancy because differing stakeholder interests and insuf<sup>fi</sup>cient incentives often result in a standard that either contains “infrequently reused” data elements [52] or is a “least common denominator” [4], limiting the standard's <sup>fi</sup>tness for use (i.e., quality). Thus completeness and relevancy are important quality dimensions of data standards.

Table 1  
Dimensions of quality of data standards.

<table><tr><td>Dimension</td><td>Aspect</td><td>Explanation</td></tr><tr><td>Complexity</td><td>Intrinsic</td><td>Number of data elements and number of various relationships among the data elements specified in the data</td></tr><tr><td>Completeness</td><td>Contextual</td><td>Extent to which a data standard specifies all the data elements and relationships needed by users of the standard</td></tr><tr><td>Relevancy</td><td>Contextual</td><td>Extent to which a data standard specifies only the data elements and relationships needed by users of the standard</td></tr><tr><td>Interoperability</td><td>Effectual</td><td>Extent to which a data standard achieves of its primary objective of ensuring interoperability of data created using the standard</td></tr></table>

Interoperability of data from multiple users of a data standard assesses the effect of the standard on the primary objective of achieving interoperability of standards-based data.

Although additional dimensions may be added, the four dimensions provide a concise indication of quality from intrinsic, contextual, and effectual aspects concerning a data standard's <sup>fi</sup>tness for use. Furthermore, as we will see next, metrics for these dimensions can be measured with automated methods, making these dimensions suitable for evaluating large-scale data standards.

## 3.2. Metrics for quality dimensions

For each dimension, we identify and de<sup>fi</sup>ne a set of metrics that can be measured using automatic computational methods.

## 3.2.1. Metrics for complexity

A data standard usually speci<sup>fi</sup>es data types (for physical implementation), data elements (corresponding to concepts in application domains), and relationships among data types (e.g., composite and derived data types) and data elements (e.g., is\_a and part\_of relationships). Since there are often more data elements than data types, we focus on metrics for data elements in the rest of the discussion.

Data elements and their relationships can be represented using a graph where nodes correspond to data elements de<sup>fi</sup>ned in a standard and directed edges correspond to the relationships between data elements. Then we can use the various characteristics of a directed graph to de<sup>fi</sup>ne complexity metrics. Let S be the set of the nodes and E be the set of labeled directed edges. The following metrics indicate certain aspects of a data standard's complexity:

• Number of data elements (i.e., nodes), |S|, re<sup>fl</sup>ects the size of the standard.

• Number of edges, |E|, re<sup>fl</sup>ects the size of the standard.

• Edge–node ratio, |E|/|S|, indicates the complexity of relationships among data elements

• Entropy, $e = - \Sigma _ { i } p ( i ) \log _ { 2 } p ( i )$ , where p(i) is the probability of any given node having a degree i (i.e., having i edges). Entropy indicates the uncertainty and therefore complexity in relationships among data elements. The minimum entropy is 0, when all nodes have the same number of edges. The maximum is log k, where k is the number of all possible degrees that a node can have and a node has an equal probability of having any of the k degrees.

Intuitively, the number of elements (concepts) measures complexity in terms of size. The number of edges and the edge/node ratio measure complexity in terms of relationships among concepts. The entropy measures complexity in terms of variance, or the uncertainty, of the relationships in which a concept is involved. These metrics are directly related to user tasks of understanding a given data standard, choosing the appropriate data elements to represent the user's data, and making appropriate extensions to the standard when extensions are allowed.

Note that as an intrinsic dimension, complexity is measured by evaluating the standard itself but not against the data instances based on the standard. In contrast, data instances are needed for the metrics of contextual and effectual dimensions, which will be described next.

## 3.2.2. Metrics for completeness and relevancy

Completeness and relevancy of the same data standard can be different to different users. They evolve with the user's needs even for the same user. Further, they are different between an individual user and the user community. When a data element is needed, chances are that all the relationships associated with it are also needed. Thus it is likely that relationship-based measurements for completeness and relevancy are proportional to element-based measurements. For simplicity, in this paper we limit the metrics to data elements and leave the relationships among data elements for future research.

Let U be the set of data elements required by the user i. From the user i's perspective, the metrics for completeness and relevancy can be de<sup>fi</sup>ned as

$$
\text { completeness } _ {\mathrm{i}} = \frac {| U _ {\mathrm{i}} \cap S |}{| U _ {\mathrm{i}} |}, \text { and   relevancy } _ {\mathrm{i}} = \frac {| U _ {\mathrm{i}} \cap S |}{| S |}.
$$

From the user community's perspective, the metrics can be de<sup>fi</sup>ned as

$$
\text { completeness } _ {c} = \frac {| \cup_ {i} U _ {i} \cap S |}{| \cup_ {i} U _ {i} |}, \text { and   relevancy } _ {c} = \frac {| \cup_ {i} U _ {i} \cap S |}{| S |}.
$$

A standard can be complete by specifying every possible data elements, but it suffers from low relevancy because many of the speci<sup>fi</sup>ed data elements may not be needed by most users. Conversely, a standard can be highly relevant by specifying only crucial data elements that are absolutely needed by all users, but it is incomplete because it does not specify the data elements needed by a variety of users. Analogously, with more than 230,000 entries, the Oxford English Dictionary is perceived to have high quality by adult users. But for an elementary school student, most of the words in the dictionary are not relevant. To the student, a children's or junior dictionary (typically with several thousands of entries) has a higher quality even though occasionally the student cannot <sup>fi</sup>nd a certain word in the dictionary.

## 3.2.3. Metrics for interoperability

A standard often adopts a uniform syntax for data representation. Thus it is relatively trivial to achieve syntactic interoperability when data is produced in conformance with the standard. A standard also de-<sup>fi</sup>nes a set of data elements with their semantics agreed upon by all users, aiming to attain semantic interoperability. However, semantic heterogeneity problems will arise when the standard allows for multiple representations of the same data [51] or when users are allowed to choose among different elements in the standard or to extend the standard with custom elements. Certain semantic heterogeneity problems can be resolved when semantic mappings are available [18,31]. However, there are no automatic methods to reliably induce such mappings. Manual creation of such mappings is not scalable for standards with a large number of users.

In this paper, we focus on the comparability aspect of semantic interoperability. A set of data instances is comparable if the instances use the same set of data elements de<sup>fi</sup>ned in a data standard. Interoperability measures the extent to which the data instances have overlapping data elements de<sup>fi</sup>ned in a standard. This de<sup>fi</sup>nition allows us to measure interoperability directly without relying on unreliable semantic matching techniques [47,48]. It is possible that pervasive misuse of an otherwise high quality data standard will result in data with low interoperability. The metrics can be adapted by including only the data of well-intentioned users if such users can be identi<sup>fi</sup>ed. Here we do not intend to distinguish abusers from well-intentioned users. Thus the metrics re<sup>fl</sup>ect the actual effect of all users.

The interoperability between a pair of data instances is based on the common data elements used. The interoperability between users i and j, $\mathbf { I _ { i , j } } ,$ can be de<sup>fi</sup>ned as

$$
\mathrm{i} _ {\mathrm{i}, \mathrm{j}} = \frac {\left| \mathrm{U} _ {\mathrm{i}} \cap \mathrm{U} _ {\mathrm{j}} \right|}{\sqrt {\left| \mathrm{U} _ {\mathrm{i}} \right| \left| \mathrm{U} _ {\mathrm{j}} \right|}}.\tag{1}
$$

Clearly, $\mathrm { I _ { i , j } = I _ { j , i \cdot } }$ The pair-wise interoperability for all users, $\mathbf { I } _ { 2 } ,$ is de-<sup>fi</sup>ned as the arithmetic mean of pair-wise interoperability among all pairs. This de<sup>fi</sup>nition can be extended to interoperability of any ktuple (with k ≥ 2) as

$$
\mathrm{I} _ {\mathrm{i} _ {1}, \dots , \mathrm{i} _ {\mathrm{k}}} = \frac {\left| \mathrm{U} _ {\mathrm{i} _ {1}} \cap \cdots \cap \mathrm{U} _ {\mathrm{i} _ {\mathrm{k}}} \right|}{\sqrt [ k ]{\left| \mathrm{U} _ {\mathrm{i} _ {1}} \right| \cdots \left| \mathrm{U} _ {\mathrm{i} _ {\mathrm{k}}} \right|}}.\tag{2}
$$

The k-interoperability of all users, $\mathbf { I _ { k } } ,$ can be de<sup>fi</sup>ned as the arithmetic mean of the k-interoperability among all k-tuples. We will limit our discussion to $\mathrm { I } _ { 2 }$ and $\mathrm { I } _ { 3 }$ because interoperability calculation is computationally expensive. For $\mathrm { I } _ { \mathrm { k } } ,$ there are ${ \mathsf { O } } ( { \mathsf { n } } ^ { \mathrm { k } } )$ k-tuples that need to be computed; here n is the number of users of a given data standard.

When a user is allowed to extend the standard, $\mathrm { U _ { i } }$ can be partitioned into two sets: U<sup>s</sup> (elements from the standard) and U<sup>c</sup> (elements custom-made by the user). One may argue that custom elements tend to be speci<sup>fi</sup>c to the user and people are largely interested in comparing the data de<sup>fi</sup>ned in the standard. Thus it is reasonable to measure interoperability by just considering standard data elements in the denominator of the formulas. For this purpose, we de<sup>fi</sup>ne $\mathrm { I _ { i , j } } ^ { \prime }$ and $\mathrm { I _ { i , j , k } } ^ { \prime }$ by replacing all occurrences of U with U<sup>s</sup> in Eqs. (1) and $( 2 ) .$ Similarly, I ′ and ${ \mathrm { I } } _ { 3 } { } ^ { \prime }$ are the arithmetic means of the pairs and triples.

## 4. XBRL GAAP Taxonomy and data collection

We use XBRL GAAP Taxonomy and data instances created using the Taxonomy to empirically evaluate the framework for data standard quality. In this section, we provide background information about XBRL and GAAP Taxonomy, followed by a description of the data collection and analysis methods.

## 4.1. XBRL and the GAAP Taxonomy

XBRL is a technology based on XML Schema and XML Linking. It de-<sup>fi</sup>nes a business reporting language by specifying a set of data types, XML elements, and attributes for each element. For example, XBRL de-<sup>fi</sup>nes data types such as monetaryItemType and sharesItemType that are often used in business reporting. Using XBRL, any jurisdiction can develop its own reporting taxonomy as a data standard for companies to exchange business data.

An XBRL-based business reporting taxonomy consists of taxonomy schemas that de<sup>fi</sup>ne data elements and linkbases that specify various relationships between data elements or between a data element and other resources. For example, below is the GAAP Taxonomy speci<sup>fi</sup>cation of the Assets data element:

```txt
<xs:element id = 'us-gaap_Assets' name = 'Assets'  
nillable = 'true' substitutionGroup = 'xbrli:item' type = 'xbrli:monetaryItemType' xbrli:balance = 'debit'  
xbrli:periodType = 'instant' />
```

The name attribute speci<sup>fi</sup>es what is generally known as the “tag” for users to tag their Assets data. The type attribute speci<sup>fi</sup>es the data type of the element, which is a monetaryItemType data type de<sup>fi</sup>ned in XBRL. The element also has several attributes that specify XBRL-speci<sup>fi</sup>c properties of the element. Below is an example of how the Assets element is used by a company to report its total assets (\$176 billion):

```xml
<us-gaap:Assets contextRef = "eol_PE2035—1210-K0010_STD_0_20120929_0" decimals = "-6" id = "id_401409_472EB522-A942-4262-B21B-5925B6A7DA2D_1_16" unitRef = "iso4217_USD">176064000000</us-gaap:Assets>
```

There are two types of elements: concrete (by default) and abstract (speci<sup>fi</sup>ed using the abstract attribute). A concrete element such as Assets can be used in data instances (<sup>fi</sup>nancial statements) with actual values. An abstract element is used by the Taxonomy only to conceptually group other elements that usually have a part-of or is-a relationship with the abstract element.

An XBRL taxonomy has <sup>fi</sup>ve types of linkbases, each specifying a kind of relationship: de<sup>fi</sup>nition, label, reference, calculation, and presentation. A de<sup>fi</sup>nition linkbase speci<sup>fi</sup>es the conceptual relationships between elements such as generalization–specialization or parent–child relationship. A label linkbase provides humanreadable descriptions for the elements de<sup>fi</sup>ned in the taxonomy schema. A reference linkbase provides further explanations to the elements by linking them to authoritative references (e.g., SEC regulations or certain accounting standards) that de<sup>fi</sup>ne the meaning of the elements.

A calculation linkbase speci<sup>fi</sup>es the numeric relationships between concrete elements. For example, the following fragments in the GAAP Taxonomy specify that Assets is the sum of Current Assets and Noncurrent Assets:

```txt
<calculationArc order = '10' use = 'optional' weight = '1.0' xlink:arcrole = 'http://www.xbrl.org/2003/arcrole/summation-item' xlink:from = 'loc_Assets' xlink:to = 'loc_AssetsCurrent' xlink:type = 'arc' />
```

```txt
<calculationArc order = '20' use = 'optional' weight = '1.0' xlink:arcrole = 'http://www.xbrl.org/2003/arcrole/summation-item' xlink:from = 'loc_Assets' xlink:to = 'loc_AssetsNoncurrent' xlink:type = 'arc' />
```

When this relationship is represented using a graph, each data element, identi<sup>fi</sup>ed by an ID using either xlink:from or xlink:to attribute, corresponds to a node in the graph. Each link, speci<sup>fi</sup>ed by both xlink: arcrole and xlink:type attributes, corresponds to a directed edge in the graph. Thus the above calculation linkbase can be represented with three nodes and two directed edges in the graph corresponding to the calculation linkbase.

A presentation linkbase speci<sup>fi</sup>es the hierarchical grouping (mainly the parent–child relationship) and the order in which the elements are presented in a report. For example, the GAAP Taxonomy's presentation linkbase uses an AssetsAbstract element as the parent of a variety of assets (including the Assets element) organized into different levels for rendering a human-readable <sup>fi</sup>nancial report.

The SEC adopted the GAAP Taxonomy and mandated that all public companies must use the Taxonomy to produce <sup>fi</sup>nancial statements in XBRL format, beginning on June 15, 2009 with a phased-in schedule based on company size. By October 31, 2014, all public companies must use the Taxonomy to submit their <sup>fi</sup>nancial statements to the SEC. Each company needs to submit <sup>fi</sup>nancial statements with additional details (so-called “detailed tagging”) starting its second year of XBRL <sup>fi</sup>ling. The 2009 GAAP Taxonomy had 13,452 elements and 41,651 presentation and calculation links among these elements. In March 2011 SEC adopted a revised Taxonomy, the 2011 GAAP Taxonomy, with 15,967 elements and 54,823 presentation and calculation links among these elements. Since then, a new version is scheduled to release on an annual basis. Companies are recommended to use the latest version of the Taxonomy and are allowed to extend the taxonomy by introducing additional data elements and relationships.

## 4.2. Data acquisition and analysis

The methods to support data acquisition and analysis are depicted in Fig. 1.

A data acquisition agent monitors the RSS Feed from the SEC (feed:// www.sec.gov/Archives/edgar/usgaap.rss.xml) to obtain company <sup>fi</sup>lings submitted to the SEC. The acquisition agent downloads the <sup>fi</sup>nancial statements and the accompanying taxonomy extensions into a local repository. An ETL (Extract/Transform/Load) program parses the <sup>fi</sup>les downloaded and loads the extracted data into a relational database. The GAAP Taxonomy is also parsed and loaded into the relational database. Stored SQL procedures and other programs are used to analyze the data in the relational database.

We collected all second quarter (with an of<sup>fi</sup>cial <sup>fi</sup>ling date of June 30, 2011) <sup>fi</sup>nancial statements submitted to SEC in XBRL format as of August 15, 2011. Each statement is from a different public company or so-called <sup>fi</sup>ler. The data is partitioned according to the version of the GAAP Taxonomy used and whether the company is in its <sup>fi</sup>rst year or second year of using the GAAP Taxonomy (see Table 2). A majority of the statements are from companies who are in their <sup>fi</sup>rst year using the GAAP Taxonomy and most of them used the 2011 version.

## 5. Results of empirical evaluation

In this section, we present the results of evaluating the framework using two versions of the US GAAP Taxonomy and <sup>fi</sup>nancial statements created using the taxonomies.

## 5.1. Complexity of GAAP Taxonomy

The complexity metrics for 2009 and 2011 GAAP taxonomies are presented in Table 3. The last column shows the percentage change from the 2009 to the 2011 version of the Taxonomy. For illustration purposes, we only consider calculation and presentation links.

![](/api/attachments/EXHNPEGE/fulltext/images/4ddf5c548564592dac9a8122fa51d1af398f0a6301868f28b782d3047c5721c1.jpg)  
Fig. 1. Methods for data acquisition and analysis.

Table 2  
Datasets used for evaluation

<table><tr><td></td><td>1st year filer</td><td>2nd year filer</td><td>Total</td></tr><tr><td>2009 Taxonomy</td><td>60</td><td>61</td><td>121</td></tr><tr><td>2011 Taxonomy</td><td>1189</td><td>223</td><td>1412</td></tr><tr><td>Total</td><td>1249</td><td>284</td><td>1533</td></tr></table>

## 5.1.1. Number of elements and number of edges

Both taxonomies de<sup>fi</sup>ne a large number of data elements that are either concrete or abstract. We use $\pmb { S _ { \mathbf { c } } }$ to denote the set of all concrete elements. The 2011 Taxonomy has 18.70% more elements; most of the new additions are abstract elements to organize the Taxonomy. The 2011 Taxonomy also has substantially more edges in graphs corresponding to calculation and presentation links. The increase of presentation links (41.74%) is greater than the increase of calculation links (14.57%), which indicates that the effort of creating the 2011 Taxonomy had focused on better organizing data in human-readable <sup>fi</sup>nancial reports rendered using presentation links.

## 5.1.2. Edge–Node ratio

Not all data elements have edges de<sup>fi</sup>ned in calculation or presentation linkbases. Only concrete, numeric elements can have calculation links. In the 2009 Taxonomy, 4713 elements have calculation links; in the 2011 Taxonomy, 5250 elements have calculation links. We use ${ \pmb S } _ { \mathbf { c } } ^ { + }$ to denote elements that have a calculation link. For the graphs corresponding to calculation linkbases, we present two edge–node ratios, one considering all concrete elements in $\mathbf { s _ { c } } ,$ and the other considering only the concrete elements in S<sup>+</sup>. Both ratios are higher for the 2011 Taxonomy.

All elements of the 2009 Taxonomy have presentation links. Out of 15,967 elements of the 2011 Taxonomy, 244 (1.5%) do not have a presentation link. Given the small percentage of elements that do not have a presentation link, we use the number of all elements when calculating the edge–node ratio for the graphs corresponding to presentation linkbases. The 2011 Taxonomy has a 19.59% increase in the edge–node ratio, which is greater than the ratios of the calculation graph. Again, this indicates that the focus of the 2011 Taxonomy had been on improving the organization of data in human-readable reports.

The fact that edge–node ratios of both versions of the GAAP Taxonomy are greater than 1 indicates that the data elements are well connected. We have considered only two out of <sup>fi</sup>ve types of linkbases. A taxonomy user, i.e. a <sup>fi</sup>ling company, must consider all linkbases. Thus the GAAP Taxonomy is quite complex in terms of relationships among data elements.

## 5.1.3. Entropy

Both versions of the GAAP Taxonomy have high entropy and the 2011 version has higher entropy. This means that for a randomly given data element, there are many probable numbers of calculation or presentation links. In fact, both the number of child nodes and the number of edges (i.e., degrees) per node have a long-tail distribution. That ${ \mathrm { i } } s ,$ most nodes only have a small number of direct links to other nodes, but a few nodes have a large number direct links to other nodes. For example, the median and maximum degrees in the presentation graph corresponding to the 2011 Taxonomy are 1 and 391, respectively. Fig. 2 shows the number of links versus the occurrence frequency on a log–log scale.

Complexity metrics of the 2009 and 2011 GAAP Taxonomies.

<table><tr><td></td><td>2009</td><td>2011</td><td>% Change</td></tr><tr><td> $|S|$ , number of elements</td><td>13,452</td><td>15,967</td><td>18.70%</td></tr><tr><td> $|S_c|$ , number of concrete elements</td><td>10,799</td><td>11,159</td><td>3.33%</td></tr><tr><td> $|E_c|$ , number of calculation links</td><td>15,566</td><td>17,849</td><td>14.67%</td></tr><tr><td> $|E_p|$ , number of presentation links</td><td>26,085</td><td>36,974</td><td>41.74%</td></tr><tr><td> $|E_c|/|S_c|$ </td><td>1.44</td><td>1.60</td><td>11.11%</td></tr><tr><td> $|E_c|/|S_c^+|$ </td><td>3.30</td><td>3.40</td><td>3.03%</td></tr><tr><td> $|E_p|/|S|$ </td><td>1.94</td><td>2.32</td><td>19.59%</td></tr><tr><td> $e_c$ , entropy of calculation graph</td><td>2.48</td><td>2.64</td><td>6.45%</td></tr><tr><td> $e_p$ , entropy of presentation graph</td><td>2.69</td><td>2.98</td><td>10.78%</td></tr></table>

Table 4  
![](/api/attachments/EXHNPEGE/fulltext/images/da8fadcd5f836ada53b9c3b16b86016a91f6145eaeb85352ca80005054277b49.jpg)

![](/api/attachments/EXHNPEGE/fulltext/images/9bd1ed243d3226cb87baa1785b45fb0fd34965559f2db760929ae6d97e894e79.jpg)

![](/api/attachments/EXHNPEGE/fulltext/images/1f7537fe248bfab12eb50ec041f5c12224f3996b6058ed6e296973e5cd1f2986.jpg)

![](/api/attachments/EXHNPEGE/fulltext/images/0f99c30b1b274ca462b44903135bfd053d76d672bb2c84e0deb5f98d72746190.jpg)  
Fig. 2. Distribution of the number of links.

In summary, both versions the GAAP taxonomies are complex. The 2011 Taxonomy is more complex, but its elements are better organized than the 2009 Taxonomy.

## 5.2. Completeness and relevancy of GAAP taxonomies

Completeness (C) and relevancy (R) of the two versions of the Taxonomy from a user's perspective are measured using the datasets. Their average values and standard deviations (in parentheses) from an individual user's perspective are provided in Table 4.

On average, both versions of the GAAP Taxonomy have high completeness and low relevancy. This is because most of the data elements used by a user are from the GAAP Taxonomy, hence the high completeness. However, the number of GAAP elements used by a user is very small compared to the total number of elements de<sup>fi</sup>ned in the GAAP Taxonomy, hence the low relevancy. As shown in Table 5, when a user (i.e., a <sup>fi</sup>ling company) uses the 2011 GAAP Taxonomy, on average a <sup>fi</sup>- nancial statement contains less than 150 data elements and nearly 110 of the elements are from the GAAP Taxonomy. The proportions for the 2009 Taxonomy users are similar. The large variances indicate signi<sup>fi</sup>- cant heterogeneity of Taxonomy users in terms of the number of standard or custom elements used.

Another observation from Tables 4 and 5 is that the average completeness, relevancy and the number of standard elements used differ among different groups of users. Table 6 presents the p-values to test the statistical signi<sup>fi</sup>cance of the differences in completeness and relevancy. A p-value less than 0.05 indicates that the difference is signi<sup>fi</sup>cant.

Completeness and relevancy of the GAAP Taxonomies from individual user's perspective.

<table><tr><td rowspan="2"></td><td colspan="2">1st year filer</td><td colspan="2">2nd year filer</td><td colspan="2">Both user types</td></tr><tr><td>C</td><td>R</td><td>C</td><td>R</td><td>C</td><td>R</td></tr><tr><td>2009 Taxonomy</td><td>0.8660(0.1101)</td><td>0.0098(0.0041)</td><td>0.6980(0.1273)</td><td>0.0175(0.0050)</td><td>0.7813(0.1458)</td><td>0.0137(0.0060)</td></tr><tr><td>2011 Taxonomy</td><td>0.9190(0.0864)</td><td>0.0082(0.0034)</td><td>0.7806(0.1093)</td><td>0.0182(0.0050)</td><td>0.8972(0.1035)</td><td>0.0098(0.0052)</td></tr><tr><td>Both versions</td><td>0.9165(0.0883)</td><td>0.0083(0.0035)</td><td>0.7628(0.1182)</td><td>0.0181(0.0050)</td><td>0.8880(0.1118)</td><td>0.0101(0.0054)</td></tr></table>

Completeness and relevancy for <sup>fi</sup>rst year and second year taxonomy users are statistically different. In fact, to second year users, both taxonomies are less complete and more relevant. The main reason is that second year <sup>fi</sup>lers are required by the SEC to annotate their <sup>fi</sup>nancial statements with more details (so-called “detailed tagging”), therefore they typically expand their usage of both standard and custom elements. An increased use of GAAP elements results in a higher relevancy of the data standard. When the increase of custom elements outnumbers the increased use of GAAP elements, completeness decreases.

The measured values are also different for the two versions of the GAAP Taxonomy. Except for second year <sup>fi</sup>lers' relevancy, all other differences are statistically signi<sup>fi</sup>cant between the two taxonomy versions. The 2011 Taxonomy has higher completeness and lower relevancy than those of the 2009 Taxonomy. We observe that in the dataset a majority of <sup>fi</sup>nancial statements are from <sup>fi</sup>rst year <sup>fi</sup>lers who used the 2011 Taxonomy. Without detailed tagging, they use a smaller number of data elements, among which the proportion of GAAP elements are larger than that of the 2009 Taxonomy users. Thus the 2011 Taxonomy has a higher completeness from these users' perspective. Similarly, the 2011 Taxonomy users in the dataset used a smaller number of GAAP elements (in absolute value, see Table 5), and at the same time, the 2011 Taxonomy has 3.33% more concrete elements. Thus the measured completeness is lower.

From a user community's perspective, both versions of the GAAP Taxonomy have substantially lower completeness and higher relevancy in comparison to the measurements for individual users (see Table 7).

Table 5  
The numbers of elements used in <sup>fi</sup>nancial statements.

<table><tr><td></td><td>Standard</td><td>Custom</td><td>Both</td><td>Standard</td><td>Custom</td><td>Both</td></tr><tr><td></td><td colspan="3">2009 Taxonomy (N = 121)</td><td colspan="3">2011 Taxonomy (N = 1412)</td></tr><tr><td>Min</td><td>46</td><td>0</td><td>86</td><td>6</td><td>0</td><td>30</td></tr><tr><td>Max</td><td>322</td><td>348</td><td>657</td><td>377</td><td>302</td><td>638</td></tr><tr><td>Mean</td><td>148.09</td><td>59.33</td><td>229.63</td><td>108.91</td><td>18.6</td><td>147.88</td></tr><tr><td>Std dev</td><td>64.18</td><td>64.84</td><td>123.52</td><td>58.23</td><td>32.47</td><td>85.86</td></tr><tr><td></td><td colspan="3">1st year filers (N = 1249)</td><td colspan="3">2nd year filers (N = 284)</td></tr><tr><td>Min</td><td>6</td><td>0</td><td>30</td><td>23</td><td>0</td><td>83</td></tr><tr><td>Max</td><td>355</td><td>348</td><td>638</td><td>377</td><td>348</td><td>657</td></tr><tr><td>Mean</td><td>91.92</td><td>59.33</td><td>122.40</td><td>200.32</td><td>71.52</td><td>294.78</td></tr><tr><td>Std dev</td><td>38.61</td><td>64.84</td><td>52.75</td><td>55.54</td><td>55.42</td><td>96.59</td></tr></table>

Table 7  
Table 6  
p-Values of two-tailed t-test with equal mean as null hypothesis

<table><tr><td rowspan="2"></td><td colspan="2">1st year vs. 2nd year</td><td rowspan="2"></td><td colspan="2">2009 vs. 2011</td></tr><tr><td>C</td><td>R</td><td>C</td><td>R</td></tr><tr><td>2009 Taxonomy</td><td>0.0000</td><td>0.0000</td><td>1st year</td><td>0.0005</td><td>0.0030</td></tr><tr><td>2011 Taxonomy</td><td>0.0000</td><td>0.0000</td><td>2nd year</td><td>0.0000</td><td>0.1687</td></tr><tr><td>Both versions</td><td>0.0000</td><td>0.0000</td><td>Both filers</td><td>0.0000</td><td>0.0000</td></tr></table>

Even though an individual user may use only a couple hundred elements from the GAAP Taxonomy, these elements do not always overlap between users. Thus collectively, more Taxonomy elements are used by the user community, hence a higher relevancy. Meanwhile, the users collectively introduce a large number of custom elements. When the increase of custom elements outpaces the increased use of Taxonomy elements, completeness decreases. For example, the 121 companies who used the 2009 Taxonomy collectively used 2736 elements from the Taxonomy and introduced 7179 custom elements. The 1412 companies who used the 2011 Taxonomy together used 5244 GAAP elements and introduced 26,269 custom elements.

We shall point out that the measurements for a community change with the size and characteristics of the community. Relevancy semimonotonically increases with the size of the community because any additional elements from a standard used by the community increases the standard's relevancy to the community. Completeness depends not only on standards elements used, but also on the custom elements introduced. Within the dataset, we can only have a fair comparison between <sup>fi</sup>rst year <sup>fi</sup>lers and second year <sup>fi</sup>lers who used the 2009 Taxonomy (60 <sup>fi</sup>lers vs. 61 <sup>fi</sup>lers). To second year <sup>fi</sup>lers, the Taxonomy has lower completeness and higher relevancy. As explained earlier for individual users, this is largely due to the SEC requirements on detailed tagging.

## 5.3. Interoperability of data created using GAAP Taxonomy

Out of the 121 <sup>fi</sup>nancial statements based on the GAAP 2009 Taxonomy, we have computed the interoperability of 7260 pairs. The summary statistics of the interoperability scores $\mathbf { I _ { i , j } } , \mathbf { I _ { i , j } } ^ { \prime } , \mathbf { I _ { i , j , k } } ,$ and $\mathbf { I _ { i , j , k } } ^ { \prime }$ are reported in Table 8.

As shown in the <sup>fi</sup>rst column of Table 8, the average pair-wise interoperability score is only 0.2031. That is, investors can conveniently compare only about 20.31% of the <sup>fi</sup>nancial information from two companies' statements.

While allowing <sup>fl</sup>exibility, the usage of non-standard elements certainly affects interoperability. Many custom elements extend the GAAP elements to allow for more detailed, company-speci<sup>fi</sup>c reporting. If investors do not consider company-speci<sup>fi</sup>c elements when comparing companies' <sup>fi</sup>nancial statements, the interoperability can be computed based on GAAP elements only. The results for this scenario are reported in the second column of Table 8. The interoperability score for the dataset is 29.52%.

The interoperability of the <sup>fi</sup>nancial statements from three companies is expected to be lower than that of two companies (see the third and fourth columns in Table 8). On average, 11.92% of the <sup>fi</sup>nancial information from three companies' XBRL statements is comparable. If only GAAP elements are considered, 17.35% of the <sup>fi</sup>nancial information is comparable.

Table 8  
Interoperability among 121 <sup>fi</sup>nancial statements based on GAAP 2009.

<table><tr><td></td><td> $I_{i,j}$ </td><td> $I_{i,j}'$ </td><td> $I_{i,j,k}$ </td><td> $I_{i,j,k}'$ </td></tr><tr><td>Min</td><td>0.0494</td><td>0.0791</td><td>0.0200</td><td>0.0300</td></tr><tr><td>Max</td><td>0.7168</td><td>0.9217</td><td>0.4416</td><td>0.7991</td></tr><tr><td>Mean</td><td>0.2031</td><td>0.2952</td><td>0.1192</td><td>0.1735</td></tr><tr><td>Standard deviation</td><td>0.0748</td><td>0.0878</td><td>0.0463</td><td>0.0576</td></tr></table>

The 2011 GAAP Taxonomy leads to higher interoperability among the <sup>fi</sup>nancial statements, as shown in Table 9. The interoperability among second-year <sup>fi</sup>lings is lower than that among the <sup>fi</sup>rst year <sup>fi</sup>lings. Second year <sup>fi</sup>lers use more custom elements due to detailed tagging, resulting in lower interoperability. The differences among all datasets are statistically signi<sup>fi</sup>cant $\left( \mathsf { p } < 0 . 0 1 \right)$ using a two-tailed test except for the difference between the 2009 and 2011 taxonomies measured by $\mathrm { I } _ { 2 } { ' }$ among second year <sup>fi</sup>lers

Since comparisons are usually performed for companies in the same industry, we classi<sup>fi</sup>ed the companies into industries according to the <sup>fi</sup>rst two digits of the NAICS (North American Industry Classi<sup>fi</sup>cation System) code and calculated the interoperability of <sup>fi</sup>rms within the same industry. The interoperability between <sup>fi</sup>nancial statements varies by industry (Table 10). For example, the manufacturing industry has higher interoperability among its <sup>fi</sup>nancial statements, likely due to its established <sup>fi</sup>nancial accounting structure. The <sup>fi</sup>nance and insurance industry, on the other hand, has the lowest interoperability likely due to its intrinsic accounting complexity and the diversity of <sup>fi</sup>nancial structures within the industry. Except for the <sup>fi</sup>nance and insurance industry, <sup>fi</sup>nancial statements within a given industry have higher interoperability than <sup>fi</sup>nancial statements from all industries. For most industries the interoperability among the <sup>fi</sup>nancial statements based on the 2011 GAAP Taxonomy is higher than that of the <sup>fi</sup>nancial statements based on the 2009 GAAP Taxonomy.

It is interesting to observe that the 2011 GAAP Taxonomy is more complex, yet <sup>fi</sup>nancial statements based on it generally have a higher pair-wise interoperability score. Why? Recall that to most individual users, the 2011 Taxonomy is more complete but less relevant, which means that these users use a smaller number of elements from the Taxonomy (low relevancy) but these elements represent a larger fraction of all the data elements needed by the users (high completeness). As a user community, the Taxonomy elements being used tend to overlap more, thus together the number of Taxonomy elements used is actually smaller compared to 2009 Taxonomy users. As a result, the communitywise relevancy is higher for the 2011 users (see Table 7). When companies use more common data elements in the Taxonomy, the interoperability among their <sup>fi</sup>nancial statements increases.

As companies start to report more details in their second year <sup>fi</sup>lings, the interoperability of second year <sup>fi</sup>lers within the same industry is also lower than that of the <sup>fi</sup>nancial statements from the <sup>fi</sup>rst year <sup>fi</sup>lers. Table 11 shows the interoperability among <sup>fi</sup>rst year and second year <sup>fi</sup>lers using the 2009 GAAP Taxonomy, for several major industries.

## 6. Discussion

We have presented a use-centric framework with metrics that can be measured using automated methods to assess the multiple dimensions of data standard quality. The evaluation employs a large realworld dataset and produces measurements that are corroborated by evidence in practice in terms of differing user requirements and evolving data standards.

Completeness (C) and Relevancy (R) of the GAAP Taxonomy from a user community's perspective.

<table><tr><td rowspan="2"></td><td colspan="3">1st year filers</td><td colspan="3">2nd year filers</td><td colspan="3">All filers</td></tr><tr><td>#</td><td>C</td><td>R</td><td>#</td><td>C</td><td>R</td><td>#</td><td>C</td><td>R</td></tr><tr><td>2009 Taxonomy</td><td>60</td><td>0.5317</td><td>0.1384</td><td>61</td><td>0.2851</td><td>0.2165</td><td>121</td><td>0.2759</td><td>0.2533</td></tr><tr><td>2011 Taxonomy</td><td>1189</td><td>0.2733</td><td>0.3748</td><td>223</td><td>0.2197</td><td>0.3646</td><td>1412</td><td>0.1664</td><td>0.4699</td></tr></table>

Table 9  
Interoperability of <sup>fi</sup>nancial statements based on Taxonomy version and <sup>fi</sup>ling status

<table><tr><td rowspan="2"></td><td colspan="2">1st Year Filers</td><td colspan="2">2nd Year Filers</td><td colspan="2">All Filers</td></tr><tr><td> $I_2$ </td><td> $I_2'$ </td><td> $I_2$ </td><td> $I_2'$ </td><td> $I_2$ </td><td> $I_2'$ </td></tr><tr><td>2009 Taxonomy</td><td>0.2363</td><td>0.3154</td><td>0.1985</td><td>0.3053</td><td>0.2031</td><td>0.2952</td></tr><tr><td>2011 Taxonomy</td><td>0.2450</td><td>0.3695</td><td>0.2208</td><td>0.3074</td><td>0.2306</td><td>0.3084</td></tr></table>

The evaluation indicates that the metrics and automated methods are effective in measuring the multiple aspects of data standard quality. Complexity metrics used in our framework have been used elsewhere to measure complexity of artifacts such as ontology and software [23,33,72]. The other metrics are novel contributions of our work. As mentioned in Section 2, completeness in most metadata quality studies examines whether the values for certain metadata elements are supplied in the instances. This de<sup>fi</sup>nition does not examine whether the data standard (i.e., the metadata schema and vocabulary) has everything that a user requires. The notion of completeness in an XBRL usability study is similar to ours [7], but their method is completely manual. Relevancy is clearly task speci<sup>fi</sup>c. Our metric is use-centric and allows for a direct measurement. We are not aware of a similar metric in literature. For example, to measure an ontology's relevancy, the method in [10] selects the information search task and uses the count of subclass–superclass relationship as a proxy. This is at best an indirect measurement. We have not seen any use of effectual metrics such as interoperability among data instances in the literature.

The framework is useful to decision makers in both standards development organizations and user communities of data standards (including data producers as well as data consumers). Standards developers can use the framework and the measurement methods to continuously monitor and improve their data standards. For standards users who need to select from multiple competing data standards, the framework provides useful tools for them to make comparisons. The framework is also useful to consumers of standards-based data as they also need to be aware of the quality of both the standard and the data.

It is tempting to provide guidelines for deciding whether a data standard has a high or a low quality based on the measurements using the framework. Unfortunately, this cannot be done without considering application context. For example, without knowing context speci<sup>fi</sup>cs, one cannot (and should not) answer questions such as “a standard is 80% complete, is it good or bad” and “a standard is 75% relevant to all users collectively, is it good or bad”. The measurements, however, can help standards makers and standards users in their decision making. For example, the team at FASB who maintains the GAAP Taxonomy has been identifying frequent custom data elements and selectively adding the most common ones to the next iteration of the Taxonomy. The team is aware of the trade-offs between completeness and relevancy and does not attempt to make the Taxonomy 100% complete. In fact, FASB would like to allow data producers to design custom elements outside the standard to encourage voluntary report of detailed <sup>fi</sup>nancial information. By examining the metrics from our proposed quality measurement framework, the FASB taxonomy team can optimize the Taxonomy to achieve the balance between uniformity and <sup>fl</sup>exibility.

Mean interoperability by industry.

<table><tr><td rowspan="2">Industry</td><td colspan="3">2009 Taxonomy</td><td colspan="3">2011 Taxonomy</td></tr><tr><td>N</td><td> $I_2$ </td><td> $I_2'$ </td><td>N</td><td> $I_2$ </td><td> $I_2'$ </td></tr><tr><td>Finance and Insurance</td><td>30</td><td>0.2023</td><td>0.2921</td><td>316</td><td>0.2285</td><td>0.3028</td></tr><tr><td>Information</td><td>7</td><td>0.2739</td><td>0.3838</td><td>45</td><td>0.2639</td><td>0.3614</td></tr><tr><td>Manufacturing</td><td>27</td><td>0.2709</td><td>0.3725</td><td>385</td><td>0.3055</td><td>0.3998</td></tr><tr><td>Mining</td><td>10</td><td>0.2119</td><td>0.3366</td><td>75</td><td>0.2416</td><td>0.3289</td></tr><tr><td>Professional</td><td>3</td><td>0.3002</td><td>0.4117</td><td>47</td><td>0.2959</td><td>0.3861</td></tr><tr><td>Transport and warehousing</td><td>7</td><td>0.2051</td><td>0.3218</td><td>26</td><td>0.2772</td><td>0.3645</td></tr><tr><td>Utilities</td><td>9</td><td>0.2306</td><td>0.3734</td><td>32</td><td>0.2481</td><td>0.3370</td></tr><tr><td>Wholesale trade</td><td>3</td><td>0.3570</td><td>0.4611</td><td>20</td><td>0.3286</td><td>0.4158</td></tr><tr><td>Other</td><td>25</td><td>0.2136</td><td>0.3155</td><td>466</td><td>0.2307</td><td>0.3159</td></tr><tr><td>All</td><td>121</td><td>0.2031</td><td>0.2952</td><td>1412</td><td>0.2306</td><td>0.3084</td></tr></table>

Mean interoperability by industry for 1st year and 2nd year <sup>fi</sup>lings based on 2009 Taxonomy.

<table><tr><td rowspan="2">Industry</td><td colspan="3">1st year filings</td><td colspan="3">2nd year filings</td></tr><tr><td>N</td><td> $I_2$ </td><td> $I_2'$ </td><td>N</td><td> $I_2$ </td><td> $I_2'$ </td></tr><tr><td>Finance and Insurance</td><td>21</td><td>0.2389</td><td>0.3203</td><td>9</td><td>0.1613</td><td>0.2858</td></tr><tr><td>Information</td><td>6</td><td>0.3830</td><td>0.4911</td><td>3</td><td>0.2251</td><td>0.3669</td></tr><tr><td>Manufacturing</td><td>12</td><td>0.3755</td><td>0.4711</td><td>15</td><td>0.2516</td><td>0.3711</td></tr><tr><td>All industries</td><td>60</td><td>0.2363</td><td>0.3154</td><td>61</td><td>0.1985</td><td>0.3153</td></tr></table>

It is also tempting to combine metrics to obtain a single measurement. However, we do not think that there is a universal formula for combining the metrics because the relative importance of quality dimensions varies by application context. A standard can be good in certain aspects but not so good in certain other aspects. Additionally, different metrics are more valuable at different stages of a data standard's life cycle. For example, intrinsic metrics can be used at the development stage, contextual and effectual metrics are suitable in the pilot and production stage when users have begun to use the standard. However, if a single measure is absolutely necessary, one can use methods such as weighted harmonic mean to combine multiple measurements. The usefulness of such weighted measures may be an interesting topic for future research.

The framework has several limitations. Additional dimensions can be added. We have purposely left out syntax-based metrics because with the increasing use of software that comes with robust syntactic validation functions, syntactic errors can be largely avoided. However, additional dimensions based on semantics are desirable. For example, a large data standard is likely to contain semantically equivalent data elements. Redundancy, or minimality, is a good metric that can be potentially measured semi-automatically by adapting the techniques developed for schema and ontology matching and mapping [15–17]. It would be also interesting to study the impact of redundancy on completeness and relevancy. There is a trade-off between adding redundancy to the standard to promote its perceived completeness and <sup>fi</sup>tness for use, and the resulting decrease in relevancy because of the enlarged standard. The methods for measuring the interoperability of standards-based data can be further enhanced. As shown in [18], ontology-based semantic mappings (when available) can be utilized to improve interoperability, especially interoperability of data instances created under different standards. Accuracy, as de<sup>fi</sup>ned ontologically in [64], is also an important dimension. However, there is no known automatic method to measure accuracy. This is partially because there is no de<sup>fi</sup>nitive relationship between signs (e.g., element names) and meanings [65].

Another limitation of the framework is that its contextual and effectual quality metrics rely on the availability of observations on how users use a data standard. When such observations are unavailable, surveys may be used as an alternative. For example, surveys have been used to assess the user-perceived quality of metadata for digital content [43,73]. Perception gaps between different stakeholders can be useful for solving problems in quality management [26]. Although the survey method involves humans in the loop and can identify issues not discoverable using automated methods, it can also introduce bias.

## 7. Conclusion and future research

We have developed a framework for assessing the quality of largescale data standards and empirically evaluated this framework using a real-world data standard. The results show that the quality dimensions and metrics can be used to effectively assess several important aspects of data standard quality. Furthermore, our analysis of XBRL GAAP Taxonomy and XBRL data provides timely insights for the <sup>fi</sup>nancial reporting practice. For example, through our dissemination effort and active engagement with the XBRL community, Taxonomy designers have learned more about the trade-off between completeness and relevancy. They realize that they should not expect to totally eliminate custom elements by exhaustively expanding the Taxonomy. Instead, they selectively add commonly created custom elements to the next version of the Taxonomy. This approach can increase data interoperability with a minimum adverse impact on the Taxonomy's complexity and relevancy. They have also begun to designate certain standard elements as industry-speci<sup>fi</sup>c and add industry-speci<sup>fi</sup>c standard elements, as these data elements are commonly used by a particular industry. Such industry speci<sup>fi</sup>cations will increase both completeness and relevancy of the standard.

For future research, we will enhance the framework for data standard quality and expand the evaluation. All limitations discussed earlier will be addressed. For example, we will develop methods for identifying redundancy in data standards and assessing its impacts on interoperability of data instances. In addition, we will analyze the revision notes of the new XBRL taxonomy to infer the design objectives of the Taxonomy revisions, and empirically validate whether the design objectives have been achieved and whether the revisions have contributed to higher standards quality. We will develop mathematical models on how the complexity of a standard and other factors such as decision making process and user requirement affect the interoperability of data produced by different data producers. We will also explore the feasibility of developing utility functions [20] and use them to provide guidelines for decision makers of different standards stakeholders. Due to limited computing resources, we did not perform any kinteroperability analysis for k N 3 in this study. We will use cloud computing resources to analyze k-interoperability among data created by different standard users. The results will allow us to understand the impact of standard quality on the interoperability of data as k increases. We will also evaluate our quality assessment framework using data standards other than XBRL such as HL7 in the healthcare domain.

In summary, we believe that we have made an important step towards developing systematic methods for assessing data standard quality. With the exponential growth of data, standards play an increasingly important role in improving data usability and the effectiveness of data intensive systems. Further efforts are needed so that we can effectively assess and improve the quality of large-scale data standards.

## Acknowledgments

This research is supported in part by the National Science Foundation under grant #1355683. The authors gratefully acknowledge helpful comments from Arnon Rosenthal and the review team on earlier versions of the paper.

## References

[1] J.W. Bartley, Y.A. Chen, E.Z. Taylor, A Comparison of XBRL Filings to Corporate 10-Ks — Evidence From the Voluntary Filing Program, SSRN, 2010. (http://papers.ssrn.com sol3/papers.cfm?abstract\_id=1397658).

[2] M.d.C.A.O.M. Batista, A.C. Salgado, Information quality measurement in data integration schemas, VLDB'07 Workshop on Quality in Databases, VLDB Endowment and ACM, Vienna, Austria, 2007, pp. 61–72.

[3] T. Berners-Lee, J. Hendler, O. Lassila, The Semantic Web, Scienti<sup>fi</sup>c American, 2001. 34–43.

[4] P.A. Bernstein L.M. Haas Information integration in the enterprise Communications of the ACM 51 (9) (2008) 72-79

[5] E.J. Boritz, W.G. No, Auditing an XBRL Instance Document: The Case of United Technologies Corporation University of Waterloo 2008

[6] E.J. Boritz, W.G. No, SEC's XBRL Voluntary Program on Edgar: The Case for Quality Assurance, SSRN, 2008, (http://ssrn.com/abstract=1163254).

[7] M. Bovee, M.L. Ettredge, R.P. Srivastava, M.A. Vasarhelyi, Does the year 2000 XBRL Taxonomy accommodate current business <sup>fi</sup>nancial-reporting practice? Journal of Information Systems 16 (2) (2002) 165–182.

[8] M. Bovee, A. Kogan, K. Nelson, R.P. Srivastava, M.A. Vasarhelyi, Financial Reporting and Auditing Agent with Net Knowledge (FRAANK) and eXtensible Business Reporting Language (XBRL), Journal of Information Systems 19 (1) (2005) 19–41.

[9] T.R. Bruce, D. Hillmann, The continuum of metadata quality: de<sup>fi</sup>ning, expressing, exploiting, in: D. Hillmann, E.L. Westbrooks (Eds.), Metadata in Practice, American Library Association, Chicago, 2004, pp. 238–256.

[10] A. Burton-Jones, V.C. Storey, V. Sugumaran, P. Ahluwalia, A semiotic metrics suite for assessing the quality of ontologies, Data & Knowledge Engineering 55 (1) (2005) 84–102.

[11] L. Cao, H. Zhu, Normal accidents: data quality problems in ERP-enabled manufacturing, ACM Journal of Data and Information Quality 4 (3) (2013) 11:11–11:26.

[12] K.H. Chou, How valid are they? An examination of XBRL voluntary <sup>fi</sup>ling documents with the SEC EDGAR system, 14th International XBRL Conference, Philadelphia, USA, 2006.

[13] H. Crawford, Encyclopedias, in: R. Bopp, L.C. Smith (Eds.), Reference and Information Services: An Introduction Libraries Unlimited Englewood 2001 pp. 433–459

[14] A. David, P. Graham, Eight key issues for the decision support systems discipline, Decision Support Systems 44 (3) (2008) 657–672.

[15] H.-H. Do, E. Rahm, Matching large schemas: approaches and evaluation, Information Systems 32 (6) (2006) 857–885.

[16] A. Doan, A.Y. Halevy, Semantic integration research in the database community: a brief survey, AI Magazine 26 (1) (2005) 83–94.

[17] A. Doan, J. Madhavan, P. Domingos, A.Y. Halery, Learning to map between ontologies on the semantic web, The 11th International World Wide Web Conference (WWW), 2002.

[18] J. Du, L. Zhou, Improving <sup>fi</sup>nancial data quality using ontologies, Decision Support Systems 54 (2012) 76–86.

[19] F. Duchateau, Z. Bellahsene, Measuring the quality of an integrated schema, Conceptual Modeling — ER 2010, Springer, Vancouver, BC, Canada, 2010, pp. 261–273.

[20] A. Even, G. Shankaranarayanan, P.D. Berger, Evaluating a model for cost-effective data quality management in a real-world CRM setting, Decision Support Systems 50 (1) (2010) 152–163.

[21] M. Fernández, C. Overbeeke, M. Sabou, E. Motta, What makes a good ontology? A case-study in <sup>fi</sup>ne-grained knowledge reuse, Proceedings of the 4th Asian Conference on the Semantic Web, Springer-Verlag, Shanghai, China, 2009, pp. 61–75.

[22] E. Folmer, Quality of Semantic Standards, Ph.D. Thesis University of Twente, 2012.

[23] A. Gangemi, C. Catenacci, M. Giaramita, J. Lehmann, R. Gil, F. Bolici, O. Strignana, Ontology Evaluation and Validation, Laboratory for Applied Ontology, ISTC-CNR, Trento, Italy, 2005.

[24] W. Harrison, An entropy-based measure of software complexity, IEEE Transactions on Software Engineering 18 (11) (1992) 1025–1029.

[25] J. Krogstie, G. Sindre, H. Jørgensen, Process models representing knowledge for action: a revised quality framework, European Journal of Information Systems 15 (1) (2006) 91–102.

[26] Y.W. Lee, D. Strong, B. Kahn, R.Y. Wang, AIMQ: A Methodology for Information Quality Assessment, Information and Management 40 (2) (2002) 133–146.

[27] O.I. Lindland, G. Sindre, A. Sølvberg, Understanding quality in conceptual modeling, IEEE Software 11 (2) (1994) 42–49.

[28] Y. Ma, B. Jin, Y. Feng, Semantic oriented ontology cohesion metrics for ontology-based systems, Journal of Systems and Software 83 (1) (2010) 143–152.

[29] D. MacKenzie, Computer-related accidental death: an empirical exploration, Science and Public Policy 21 (4) (1994) 233–248

[30] S.E. Madnick, R.Y. Wang, Y.W. Lee, H. Zhu, Overview and framework for data and information quality research, ACM Journal of Data and Information Quality 1 (1) (2009)(Article #2).

[31] S.E. Madnick, H. Zhu, Improving data quality with effective use of data semantics, Data and Knowledge Engineering 59 (2) (2006) 460–475.

[32] M.L. Markus, C.W. Stein<sup>fi</sup>eld, R.T. Wigand, G. Minton, Industry-wide information systems standardization as collective action: the case of the U.S. residential mortgage industry, MIS Quarterly 30 (Special Issue) (2006) 439–465.

[33] T.J. McCabe, A complexity measure, Proceedings of the 2nd International Conference on Software Engineering, IEEE Computer Society Press, San Francisco, California, United States, 1976, p. 407.

[34] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review 63 (2) (1956) 81–97.

[35] D.L. Moody, Theoretical and practical issues in evaluating the quality of conceptual models: current state and future directions, Data & Knowledge Engineering 55 (3) (2005) 243–276.

[36] D.L. Moody, G. Sindre, T. Brasethvik, A. Sølvberg, Evaluating the quality of information models: empirical testing of a conceptual model quality framework, Proceedings of the 25th International Conference on Software Engineering, IEEE Computer Society, Portland, Oregon, 2003, pp. 295–305.

[37] H.J. Nelson, G. Poels, M. Genero, M. Piattini, A conceptual modeling quality framework, Software Quality Journal 20 (1) (2012) 201–228.

[38] P.G.A.P. Neumann, Computer Related Risks, ACM Press/Addison Wesley Publishing Co., New York, 1995.

[39] N.F. Noy, A. Doan, A.Y. Halevy, Semantic Integration, AI Magazine 26 (1) (2005) 7–9.

[40] X. Ochoa, E. Duval, Automatic evaluation of metadata quality in digital repositories, International Journal on Digital Libraries 10 (2/3) (2009) 67–91.

[41] A.M. Orme, H. Yao, L.H. Etzkorn, Coupling metrics for ontology-based systems, IEEE Software 23 (2) (2006) 102-108

[42] J. Pak, L. Zhou, A framework for ontology evaluation, in: R. Sharman, H.R. Rao, T.S. Raghu (Eds.), Exploring the Grand Challenges for Next Generation E-business, Springer, Berlin Heidelberg, 2011, pp. 10–18.

[43] N. Palavitsinis, N. Manouselis, S.S. Alonso, Evaluation of a metadata application pro-<sup>fi</sup>le for learning resources on organic agriculture, in: F. Sartori, M.A. Sicilia, N. Manouselis (Eds.), MSTR 2009, CCIS 46, Springer-Verlag, Berlin, 2009, pp. 270–281.

[44] J.-R. Park, Metadata quality in digital repositories: a survey of the current state of the art, Cataloging and Classi<sup>fi</sup>cation Quarterly 47 (3/4) (2009) 213–228.

[45] C. Perrow, Normal Accidents: Living With High-risk Technologies, Princeton University Press, Princeton, NJ, 1999.

[46] Personal Communication, Discussion with participants of MIT Information Quality Industrial Symposium in past <sup>fi</sup>ve years, 2011.

[47] E. Rahm, P.A. Bernstein, A survey of approaches to automatic schema matching, VLDB Journal 10 (4) (2001) 334–350.

[48] E. Rahm, H.-H. Do, S. Maßmann, Matching large XML schemas, ACM SIGMOD Record 33 (4) (2004) 26–31.

[49] T.C. Redman, Data Quality for the Information Age, Artech House, Boston, MA, 1996.

[50] S. Roohani, X. Zhao, E.A. Capozzoli, B. Lamberton, Analysis of XBRL literature: a decade of progress and puzzle, The International Journal of Digital Accounting Research 10 (2010) 131–147.

[51] A. Rosenthal, L. Seligman, M.D. Allen, A. Chapman, Fit for purpose: toward an engineering basis for data exchange standards, International IFIP Working Conference on Enterprise Interoperability Information, Services and Processes for the Interoperable Economy and Society, Springer, Enschede, The Netherlands, 2013, pp. 91–103.

[52] A. Rosenthal, L. Seligman, S. Renner, From semantic integration to semantics management: case studies and a way forward, ACM SIGMOD Record 33 (4) (2004) 44–50.

[53] N. Shadbolt, T. Berners-Lee, W. Hall, The semantic web revisited, IEEE Intelligent Systems 21 (3) (2006) 96–101.

[54] G. Shankaranarayanan, Y. Cai, Supporting data quality management in decision-making, Decision Support Systems 42 (1) (2005) 302–317.

[55] E.P.B. Simperl, C. Tempich, Ontology engineering: a reality check, in: M. Robert, T. Zahir (Eds.), OTM Conferences, Springer, 2006, pp. 836–854.

[56] V.C. Storey, R.M. Dewan, M. Freimer, Data quality: setting organizational policies, Decision Support Systems 54 (1) (2012) 434–442.

[57] B. Stvilia, A model for ontology quality evaluation, First Monday 12 (12) (2007).

[58] B. Stvilia, L. Gasser, Value based metadata quality assessment, Library and Information Science Research 30 (1) (2008) 67–74.

[59] B. Stvilia, L. Gasser, M.B. Twidale, L.C. Smith, A framework for information quality assessment, Journal of the American Society for Information Science and Technology 58 (12) (2007) 1720–1733.

[60] S.A. Sutton, Metadata quality, utility and the semantic web: the case of learning resources and achievement standards, Cataloging and Classi<sup>fi</sup>cation Quarterly 46 (1) (2010) 81–107.

[61] J. Sweller, Cognitive load during problem solving: effects on learning, Cognitive Science 12 (2)(1988) 257–285

[62] S. Tartir, I.B. Arpinar, M. Moore, A.P. Sheth, OntoQA: metric-based ontology quality analysis, IEEE International Conference on Semantic Computing, 2005.

[63] H. Wache, T. Vögele, U. Visser, H. Stuckenschmidt, G. Schuster, H. Neumann, S. Hübner, Ontology-based integration of information — a survey of existing approaches, IJCAI-01 Workshop: Ontologies and Information Sharing, Seattle, WA, 2001, pp. 108–117.

[64] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11) (1996) 86–95.

[65] Y. Wand, R. Weber, On the deep structure of information systems, Information Sys tems Journal 5 (3) (1995) 203–223.

[66] R.Y. Wang, M.P. Reddy, H.B. Kon, Toward quality data: an attribute-based approach, Decision Support Systems 13 (3–4) (1995) 349–372

[67] R.Y. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–33.

[68] J. Weagley, E. Gelches, J.-R. Park, Interoperability and metadata quality in digital video repositories: a study of Dublin Core, Journal of Library Metadata 10 (1) (2010) 37–57.

[69] E.J. Weyuker, Evaluating Software complexity measures, IEEE Transactions on Software Engineering 14 (9) (1988) 1357–1365.

[70] XBRL International, Extensible Business Reporting Language (XBRL) 2.1, XBRL International, 2006.

[71] H. Yao, A.M. Orme, L. Etzkorn, Cohesion metrics for ontology design and application, Journal of Computer Science 1 (1) (2005) 107–113.

[72] H. Zhang, Y.-F. Li, H.B.K. Tan, Measuring design complexity of semantic web ontologies, Journal of Systems and Software 83 (5) (2010) 803–814.

[73] Y. Zhang, Y. Li, A user-centered functional metadata evaluation of moving image collections, Journal of the American Society for Information Science and Technology 59 (8) (2008) 1331–1346.

[74] H. Zhu, L. Fu, Towards quality of data standards: empirical <sup>fi</sup>ndings from XBRL, The 30th International Conference on Information Systems (ICIS'09), Phoenix, AZ, USA, 2009.

[75] H. Zhu, H. Wu, Interoperability of XBRL <sup>fi</sup>nancial statements in the U.S. International Journal of E-Business Research 7 (2) (2011) 18–33.

Hongwei Zhu holds a Ph.D. from MIT and is an associate professor of Information Systems at the University of Massachusetts Lowell. His research aims to improve the quality of data standards and standards-based data. He is a member of AIS and the Best Practices Committee of XBRL US.

Harris Wu received his Ph.D. in Business Administration from the University of Michigan at Ann Arbor. He is an associate professor of Information Technology at the Old Dominion University. His research interests include social computing, data quality, complex systems and inter-organizational collaboration. He is a member of AIS and XBRL US.
