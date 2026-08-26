---
otero_id: 2112
otero_key: "AYT8GH4Z"
title: "Improving financial data quality using ontologies"
authors: "Jie Du; Lina Zhou"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving <sup>fi</sup>nancial data quality using ontologies

Jie Du, Lina Zhou ⁎

Department of Information Systems, University of Maryland Baltimore County, Baltimore, MD 21250, United States

## a r t i c l e i n f o

Article history: Received 15 March 2011 Received in revised form 27 January 2012 Accepted 15 April 2012 Available online 12 June 2012

Keywords: Data quality Financial decision-making Ontology Ontology mapping Portfolio management

## a b s t r a c t

The performance of <sup>fi</sup>nancial decision-making directly concerns both businesses and individuals. Data quality is a key factor for decision performance. As the availability of online <sup>fi</sup>nancial data increases, it also heightens the problem of data quality. In this paper, a taxonomy is created for data quality problems. More importantly, an ontology-based framework is proposed to improve the quality of online <sup>fi</sup>nancial data. An empirical evaluation of the framework with the <sup>fi</sup>nancial data of real-world <sup>fi</sup>rms provides preliminary evidence for the effectiveness of the framework. The framework is expected to support decision-making in <sup>fi</sup>nance and in other domains where data is spread across multiple sources with overlap but complementary in content.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Today's widespread <sup>fi</sup>nancial problems and the economic downturn highlight the importance of <sup>fi</sup>nancial decision-making to individuals, businesses, and organizations. Intelligence gathering is the <sup>fi</sup>rst stage of decision making [57], and data quality is a key factor for decision performance [29]. It is reported [63] that 20% of asset managers, investment bankers and hedge fund professionals spend between 25% and 50% of their time in validating data, which prevents them from focusing on tasks that contribute to the bottom line. According to a recent study of the costs and other consequences of dirty or inconsistent data in the secondary mortgage market in the U.S. [22], inaccurate data results in slow and expensive loan processing, weak underwriting, incorrect portfolio management, and other costs to lenders and mortgage investors. Given that <sup>fi</sup>nancial data including <sup>fi</sup>nancial statements, market data, and business news are being used increasingly by investors in stock market predictions [16,53], data quality has become an important and widespread issue in <sup>fi</sup>nancial decision-making.

The problems with <sup>fi</sup>nancial data come in a variety of forms. The main problems of <sup>fi</sup>nancial data include ambiguity, inconsistency, missing values, inaccuracy, misrepresentation, incompletion, and so on [40]. For instance, missing values are not uncommon in Standard & Poor's Compustat North America dataset. Such problems can directly impact the performance of <sup>fi</sup>nancial decision-making. Under this backdrop, this study aims to answer the following research question:

How should one address the quality problems of financial data so as to improve the performance of financial decision-making?

Both qualitative and quantitative approaches have been proposed to address various types of data quality problems [42]. For example, missing values can be replaced with global means or the most probable values [15]. Nevertheless, validating data quality is a challenging and time-consuming task [59]. This is especially true for <sup>fi</sup>nancial data as an increasing amount of it becomes available on the Internet. The characteristics of the high frequency [25], high diversity and dependency of <sup>fi</sup>nancial data render the conventional static approaches ineffective. Therefore, <sup>fi</sup>nancial data calls for a synergic semantic alignment of various resources to improve <sup>fi</sup>nancial data quality.

This study proposes a framework for addressing and identifying data quality problems following the design science research framework [28]. There are three types of artifacts created in our study. First, this study proposes an ontology-based framework to address the quality problems associated with online <sup>fi</sup>nancial data. The framework is motivated by one unique feature of <sup>fi</sup>nancial data, namely redundancy. Speci<sup>fi</sup>cally, <sup>fi</sup>nancial data about a <sup>fi</sup>rm is duplicated across multiple yet complementary online sources such as Yahoo!Finance, Google Finance, MSN Money Central, and Compustat. Yet the data are heterogeneous across different sources, even within the highly regulated <sup>fi</sup>nancial domain. Our ontology is expected to address the above problem by enabling the mapping of data across different sources.

Second, this study creates a taxonomy and formalization of quality problems associated with <sup>fi</sup>nancial data. The taxonomy, comprised of six types of quality problems such as missing values, is organized along two dimensions: the foundation and the abstraction level of ontology. Third, this study introduces a baseline method for evaluating the performance of <sup>fi</sup>nancial decision-making that is based on fuzzy theories. In view of the uncertainty involved in <sup>fi</sup>nancial decisionmaking, the neuro-fuzzy approach is expected to be more robust when faced with data quality problems. The results of this study demonstrate that the proposed framework is effective for improving the quality of <sup>fi</sup>nancial decision-making.

The remainder of this paper is organized as follows. Section 2 provides background information on <sup>fi</sup>nancial decision-making, <sup>fi</sup>nancial data quality, and ontology. Section 3 presents a taxonomy of problems associated with online <sup>fi</sup>nancial data. Section 4 introduces the ontology-based framework for improving data quality in <sup>fi</sup>nancial decision-making. The framework is evaluated in Section 5 and the results are presented and discussed in Section 6. Section 7 concludes the paper.

## 2. Background

## 2.1. Data quality to financial decision-making

Financial decision-making applications can be classi<sup>fi</sup>ed into <sup>fi</sup>ve major categories, including stock forecasting, portfolio management, bankruptcy prediction, foreign exchange market, and fraud detection [69]. All of these applications require the collection of data whose quality is of great importance to their success. According to IBM Business Consulting's 2008 CFO Survey, data management remained a high priority for integrated <sup>fi</sup>nance organization. Issues around data consistency, data accuracy, and data integrity are primary concerns. Poor data quality can have substantially negative, social and economic impacts [55,65]. Since the <sup>fi</sup>nancial data is highly time-variant, nonlinear, and noisy, data quality especially impacts <sup>fi</sup>nancial decisionmaking [4].

## 2.2. Data quality dimensions

Traditionally, data quality is measured from multiple dimensions, including accuracy, consistency, completeness, and so on [51,54]. Based on the framework of Madnick et al. [42], data quality research can be characterized by two dimensions: topics and methods. Data quality covers a wide range of topics, which include data quality impact [21,39], database-related technical solutions for data quality [13,19], data quality in the context of computer science and information technology [38,50], and data quality in curation [9]. The quality of internal <sup>fi</sup>nancial data can be managed by enhancing internal controls and reporting processes, which may be supported by application software such as Oracle Hyperion Financial Management (FDQM) [49]. Much research on <sup>fi</sup>nancial decision-making has focused on improving the performance/ outcome by developing and enhancing algorithms and decision models [5,62]. However, little research has focused on addressing the quality of <sup>fi</sup>nancial data.

There are two types of methods that have been used to address data quality problems: the quantitative method and the qualitative method. The quantitative method is dominant. For example, Madnick and Zhu [41] improve data quality with context interchange technology. Thatcher and Pingry [60] present an econometric model to formalize the complex relationships among IT investments, product quality, and economic performance. Ballou et al. [3] use a mathematical model to analyze how data quality dimensions change within an information manufacturing system. Other studies deal with data quality problems using qualitative methods. For example, Davidson et al. [14] explore how the information maps can be used to improve data quality using a longitudinal case study. Kerr [33] adopts an ethnography method to study the data quality problems in the health sector. This study aims to improve the <sup>fi</sup>nancial data quality by combining both quantitative and qualitative methods.

## 2.3. Ontology application in finance domain

Ontology is de<sup>fi</sup>ned as an explicit speci<sup>fi</sup>cation of conceptualization [26]. Conceptualization refers to an abstract model of a particular domain of knowledge. Explicit speci<sup>fi</sup>cation means the concepts, their attributes and the relationship between concepts. Classes and instances are common components of ontologies [26]. Classes, also known as concepts, are used to model the domain structure. Instances belong to classes and are used to model the “ground level” objects. Ontology research centers on two issues: ontology building and ontology mapping [17,18]. The building process could be manual, semi-automated, or fully automated. As more and more ontologies are being generated, how to reuse these existing ontologies becomes essential. Ontology mapping expands and combines existing ontologies in support of communication between existing and new domains. An evaluation of existing ontology mapping techniques is given by Kaza and Chen [32].

Based on a shared and common understanding of a speci<sup>fi</sup>c domain, ontology plays a key role in improving information consistency, reusability, systems interoperability, and knowledge sharing. Additionally, ontology has a huge potential to improve information organization, management, and understanding [20]. Some <sup>fi</sup>nancial applications have bene<sup>fi</sup>ted from ontology. For instance, an ontology is proposed to facilitate the communication among agents in a multi-agent <sup>fi</sup>nancial investment system [58,70]; and ontologies are used to facilitate the predictions of <sup>fi</sup>rms which will have fraudulent <sup>fi</sup>nancial statements [31], and to support investigators in the detection of fraudulent <sup>fi</sup>nancial sites [36,71]. Nevertheless, applying ontology to address the problems of <sup>fi</sup>nancial data has not been explored.

## 2.4. Schematic and data heterogeneity

Schematic and data heterogeneity makes communication among heterogeneous sources dif<sup>fi</sup>cult and may cause many issues about data quality [34]. Database schema matching has received a long standing research attention. According to Kim and Seo [34], schema con<sup>fl</sup>icts result from the use of different schema de<sup>fi</sup>nitions from different sources. In other words, it is caused by the use of different concepts for semantically equivalent information. Data con<sup>fl</sup>icts, on the other hand, are due to inconsistent data in the absence of schema con<sup>fl</sup>icts [34]. There are many types of inconsistent data. Different representations might be used for the same data while the same representation might be used for different data. Computing errors or incorrect entry is another cause of data quality problems. Both types of heterogeneity are signi<sup>fi</sup>cant to online <sup>fi</sup>nancial data. For instance, one data source represents a company's revenue as ‘sales’, while another represents it as ‘revenue’. The unit for dollar amount is a thousand in Yahoo!Finance and a million in Compustat.

## 3. An ontology-anchored classi<sup>fi</sup>cation schema for data quality problems

The <sup>fi</sup>nancial market is characterized by noisy, nonlinear data [66]. The noise of <sup>fi</sup>nancial data includes dynamic noise, which disturbs the information obtained, and observation noise, which negatively impacts the accuracy of measurement. From the information system's perspective, data quality problems can be treated as representation de<sup>fi</sup>ciencies, which are de<sup>fi</sup>ned in terms of the difference between the view of the real-world system as inferred from the information system, and the view that is obtained by directly observing the realworld system [64].

Data quality is a multidimensional concept that concerns both objective aspects that are intrinsic to the data (e.g., completeness) and contextual aspects that vary across tasks and users (e.g., ambiguity). It is important to address both aspects of the data quality for improved support of decision-making [56,67]. Therefore, this study aims to address the quality problem of <sup>fi</sup>nancial data from both the objective and the contextual aspects. Moreover, this study focuses on utilizing ontology to improve <sup>fi</sup>nancial data quality. Thus, the selection of quality variables is directly tied to the conceptualization of the <sup>fi</sup>nance domain.

We propose a two-dimensional ontology-based classi<sup>fi</sup>cation schema for data quality problems. The <sup>fi</sup>rst dimension is anchored in ontological foundations, including completeness, unambiguity, correctness and meaningfulness [64]. Speci<sup>fi</sup>cally, completeness refers to the ability of an information system to represent every meaningful state of the represented real-world system; unambiguity indicates that the information system state corresponds to exact one state of the real world; correctness indicates whether the data conveys the right information; meaningfulness refers to whether the data generated by an information system can be interpreted in a meaningful way [64]. Finance is an established domain, and online <sup>fi</sup>nancial data are expected to be meaningful to its prospect users. Therefore, ‘meaningfulness’ is not so relevant to <sup>fi</sup>nancial data quality and thus is disregarded.

The second dimension is based on the abstraction level of ontology, which consists of concept and instance. The concepts refer to the classes used in a speci<sup>fi</sup>c domain and the ways in which classes and properties can be related to one another. The instances, belonging to classes, are used to model “ground level” objects [26].

Based on these two dimensions, we classify data quality problems into six categories: terminological ambiguity, conceptual inaccuracy, missing data, unreliable data, inconsistent representation, and incomplete domain, as shown in Table 1.

## 3.1. Terminological ambiguity

Terminological ambiguity is a common phenomenon when the data sources are heterogeneous and diverse [17]. According to a systematic classi<sup>fi</sup>cation of multi-database system con<sup>fl</sup>icts [34], there are two types of con<sup>fl</sup>icts: schema con<sup>fl</sup>icts resulting from using different structures for the same information; and data con<sup>fl</sup>icts resulting from inconsistent data in the absence of schema con<sup>fl</sup>icts. Despite the <sup>fi</sup>nancial domain being highly structured, con<sup>fl</sup>icts in terminology usage still exist between different online resources of <sup>fi</sup>nancial data. For example, <sup>fi</sup>nancial terms such as sales, cost of goods sold, accounts payable, other assets, and retained earnings have different interpretations across different online data sources. Viewing the <sup>fi</sup>nancial domain as a whole, the ambiguity problems associated with interpreting <sup>fi</sup>nancial terms come in two forms: many-to-one and one-to-many.

• one-to-many: the same term is used to refer to different concepts:

$$
\exists t; \quad t \stackrel {{\text { def }}} {{=}} C _ {1}, \quad t \stackrel {{\text { def }}} {{=}} C _ {2}, \quad C _ {1} \neq C _ {2}
$$

where t is a term, and concepts $C _ { 1 } \in T _ { A }$ and $C _ { 2 } { \in } T _ { B } , C _ { 1 }$ and $C _ { 2 }$ belong to concept spaces A and B, respectively. For example, accounts payable from Yahoo!Finance means differently than that from Google Finance and MSN Money Central in that the former is also composed of taxes payable and notes payable.

An ontology-anchored classi<sup>fi</sup>cation schema of data quality problems.

<table><tr><td></td><td>Completeness</td><td>Unambiguity</td><td>Correctness</td></tr><tr><td>Concept</td><td>Incomplete domain</td><td>Terminological ambiguity, inconsistent representation</td><td>Conceptual inaccuracy</td></tr><tr><td>Instance</td><td>Missing data</td><td>Inconsistent representation</td><td>Unreliable data</td></tr></table>

• many-to-one: different terms $t _ { 1 }$ and $t _ { 2 }$ are used to refer to the same concept:

$$
\exists t _ {1}, t _ {2}; t _ {1} \neq t _ {2}, t _ {1} \stackrel {\text { def }} {=} C _ {1}, t _ {2} \stackrel {\text { def }} {=} C _ {2}, C _ {1} = C _ {2}
$$

where $t _ { 1 }$ and $t _ { 2 }$ are two different terms, and concepts $C _ { 1 } \in T _ { A }$ and $C _ { 2 } { \in } T _ { B } , C _ { 1 }$ and $C _ { 2 }$ belong to two concept spaces A and B, respectively. For example, in<sup>fl</sup>ows of resources resulting from providing goods or services to customers is conceptualized as sales in Compustat, and as revenue in Google Finance. On a related note, out<sup>fl</sup>ows of resources incurred while generating revenue is conceptualized as cost of goods sold in Compustat and as cost of revenue in Google Finance.

## 3.2. Conceptual inaccuracy

Conceptual inaccuracy is caused by the lack of precision in concept de<sup>fi</sup>nitions, which has many types of manifestation. One common type is called part-whole mapping, where the term t is mapped to a combination of another two terms $t _ { 1 }$ and $t _ { 2 } .$

$$
\exists t, t _ {1}, t _ {2}; t \stackrel {{\text { def }}} {{=}} C _ {1}, t _ {1} \stackrel {{\text { def }}} {{=}} C _ {2}, t _ {2} \stackrel {{\text { def }}} {{=}} C _ {3}, C _ {1} = C _ {2} \sqcup C _ {3}
$$

where $C _ { 1 } \in T _ { A }$ and $C _ { 2 } , C _ { 3 } \in T _ { B } .$ For example, revenue is a common term from the Income Statement, which comprises revenue of goods and revenue of service. Hence, conceptually, revenue in Google Finance can be interpreted as revenue of goods, revenue of service, or a combination of both when there is a lack of suf<sup>fi</sup>cient information for veri<sup>fi</sup>cation. This problem is particularly pronounced in mapping heterogeneous data sources.

Another common type is called sub-super type mapping, in which term $t _ { 1 }$ subsumes term $t _ { 2 } .$

$$
\exists t _ {1}, t _ {2}; \quad t _ {1} \stackrel {\text { def }} {=} C _ {1}, t _ {2} \stackrel {\text { def }} {=} C _ {2}, C _ {1} \sqsubset C _ {2}
$$

where concepts $C _ { 1 } \in T _ { A }$ and $C _ { 2 } \in T _ { B } ,$ and $C _ { 1 }$ is a subclass of $C _ { 2 } .$ For example, investments at equity from Compustat is subsumed by long term investments from Yahoo!Finance.

## 3.3. Missing data

The problem of missing data occurs at the instance level, which violates the principle of data completeness. Missing data is a common problem with online <sup>fi</sup>nancial data. Moreover, it is generally dif<sup>fi</sup>cult to distinguish missing values from null values unless explicit labels are provided to mark missing values as Standard & Poor's Compustat does (see Appendix 1).

There are many conventional solutions to addressing the missing data problem [15], which include:

• trying to <sup>fi</sup>nd the missing data potentially from other sources,

• interpolating or using average values,

• <sup>fi</sup>lling in values that would minimally disturb the patterns, or

• dropping the record in question.

The <sup>fi</sup>rst approach is the most desired compared with other alternatives because they are prone to data integrity violation. Nevertheless, this method has rarely been used because the missing data problem is usually complicated by other types of data problems such as conceptual inaccuracy and terminological ambiguity. How to <sup>fi</sup>nd the right data in the right place requires a synergetic approach that can successfully solve all the related data quality problems. This study provides a theoretical framework for addressing data quality problems in <sup>fi</sup>nancial data, such as missing data, by leveraging multiple data sources.

## 3.4. Unreliable data

Unreliable data problems reside at the intersection of the correctness dimension and the instance level. There are standard rules governing the relationships between different items in <sup>fi</sup>nancial statements such as Generally Accepted Accounting Principles (GAAP). According to Statements of Financial Accounting Standards (SFAS) No. 6, there are ten key elements in <sup>fi</sup>nancial statements, including assets, liabilities, equity, investments by owners, distributions to owners, revenues, expenses, gains, losses, and comprehensive income. Each of these elements is in turn derived from a set of basic items. For instance, total current assets in the Balance Sheet is composed of <sup>fi</sup>ve basic items, including cash and equivalents, short term investments, net receivables, inventory, and other current assets.

However, the derivation of item values sometimes does not strictly follow standard accounting principles. For example, gross profit is de<sup>fi</sup>ned as the difference between total revenue and cost of revenue in GAAP, and such principle is not followed in the data of some <sup>fi</sup>rms from MSN Money Central. One possible way to address this problem is to model the <sup>fi</sup>nancial principle as an axiom and to detect and correct unreliable data by making inferences.

## 3.5. Inconsistent representation

Consistency refers to several aspects of data, such as values of data and the representation of data [64]. This study focuses on the representation aspect, which means that two or more representations of the same concept (or instance) exist. At the concept level, for instance, the same data may be represented in units of millions or thousands of USD by different <sup>fi</sup>nancial data sources. Additionally, there are slight differences across different data sources in the representations of ticker symbol extensions [1], which are additional letters added to a publicly-traded stock in a market to uniquely identify it [11]. For instance, Google Finance and MSN Money Central use the “behind the dot” codes for shares traded on the NYSE (e.g., BRK.A and BRK.B) while Yahoo!Finance and Compustat use slightly different formats (e.g., BRK-A and BRK-B, BRKa and BRKb), respectively. Resolutions of such inconsistencies could be aided by de<sup>fi</sup>ning rules for mapping different ontologies. Inconsistent representation may also occur at the instance level. For instance, for those stocks having two share classes, MSN money central and Yahoo!Finance only report the <sup>fi</sup>nancial statement for one class instead of reporting both classes as does Google Finance. No publicly available rules are available for guiding the report of stock issues.

## 3.6. Incomplete domain

Incomplete domain refers to the lack of complete knowledge about a certain domain [64]. For instance, some concepts in the Balance Sheet such as inventory are not applicable to <sup>fi</sup>nancial <sup>fi</sup>rms. According to SFAS, inventory refers to the amount or value of a <sup>fi</sup>rm's current assets that consist of raw materials, work in progress, and <sup>fi</sup>nished good. According to the Global Industry Classi<sup>fi</sup>- cation Standard, the industry sector ‘<sup>fi</sup>nancial’ contains banks, insurance companies, real estate companies and <sup>fi</sup>nancial service companies. One of the common characteristics of <sup>fi</sup>nancial <sup>fi</sup>rms is that they do not have inventory, which is distinct from zero inventory. However, when retrieving <sup>fi</sup>nancial data from online sources, it is sometimes hard to distinguish the null value and zero value, leading to the problem of incomplete domain. This problem may be solved with aid of ontology by creating a concept hierarchy.

## 4. An ontology-based framework for improving <sup>fi</sup>nancial data quality

We propose an ontology-based framework to improve the quality of <sup>fi</sup>nancial data. Ontology has been used to solve data quality problems [10,23,64]. For example, Frank [23] presents an ontology for imperfect data in GIS and views data quality problems from the decision-making perspective. Choi et al. [10] use a quality evaluation ontology to improve data quality in Service Oriented Architecture and real-time enterprise environments. Ontology mapping is one of the most used technologies to address the schematic and data heterogeneity problem and thus facilitates interoperability [18]. However, it should be noted that these applications of ontologies in the area of data quality focus on the issue of assessing data quality, but largely ignore handling data quality problems. The latter issue is important because it realizes the ultimate goal of data quality research. To <sup>fi</sup>ll in the gap, this study addresses the quality problems associated with online <sup>fi</sup>nancial data using ontologies.

There is abundant <sup>fi</sup>nancial information about publicly-traded companies in various online sources such as Yahoo!Finance, Google Finance, and MSN Money Central. The easy access to online <sup>fi</sup>nancial data further heightens the importance of <sup>fi</sup>nancial data quality. Additionally, making these heterogeneous sources interoperable becomes increasingly important to the performance of decisionmaking. Thus, the ontology-based framework aims to improve the quality of <sup>fi</sup>nancial data by leveraging rich and diverse online resources.

An ontology-based framework for <sup>fi</sup>nancial decision-making (OFFDM) consists of three components: Financial Ontology (FinO), online <sup>fi</sup>nancial data resources, and <sup>fi</sup>nancial decision-making, as shown in Fig. 1. The decision-making process contains four key phases: intelligence, design, choice and implementation [44]. The intelligence phase outlines the goal and outcome and gathers data to support the following phases. The design phase develops possible solutions via brainstorming and then lists the pros and cons of each solution. One solution is chosen in the choice phase and implemented in the implementation phase. Therefore, gathering data is indispensable to decision-making [44], such as asset valuation in portfolio management. Nevertheless, the collection of online <sup>fi</sup>nancial data is infused with data quality problems. FinO not only directly facilitates ontology mapping between heterogeneous data sources but also indirectly supports <sup>fi</sup>nancial decisionmaking by addressing data quality problems. Given the pivotal role of FinO in the framework, we introduce how to generate FinO and how to use the ontology to improve <sup>fi</sup>nancial decision-making in detail.

An ontology can be generated using one of the three methods: bottom-up, top-down, and hybrid [72]. Bottom-up strategy starts with text documents and gradually moves from speci<sup>fi</sup>cation to generalization. Top-down strategy begins with top-level concepts and then gradually moves from generalization to speci<sup>fi</sup>cation. Hybrid or middle-out strategy is a combination of the <sup>fi</sup>rst two, which starts with the most important concepts and then moves to generalization and speci<sup>fi</sup>cation. Given that <sup>fi</sup>nance is a well-established domain, the top-down or the hybrid approach is appropriate for developing FinO [72]. Our survey identi<sup>fi</sup>ed some promising candidates in support of the development of FinO.

• SUMO<sup>1</sup> (Suggested Upper Merged Ontology) is a general upperlevel ontology. It is the only formal ontology that has been mapped to the WordNet lexicon [48]. SUMO represents high-level concepts and the relationship between concepts in the <sup>fi</sup>nance domain and thus can easily support the ontology development process from generation to speci<sup>fi</sup>cation. SUMO has been extended in the

![](/api/attachments/AYT8GH4Z/fulltext/images/4faa1ea7f3245a8cd7b5f933bf70046dffe4ac0abf547c4892e31cc25b770af5.jpg)  
Fig. 1. An ontology-based framework in support of <sup>fi</sup>nancial decision-making

LSDIS<sup>2</sup> (Large Scale Distributed Information Systems) Finance Ontology.

• Finance Ontology<sup>3</sup> represents knowledge in the <sup>fi</sup>nancial services domain including <sup>fi</sup>nancial statements. It is written in OWL.

• XBRL US GAAP Taxonomies v1.0<sup>4</sup> provide comprehensive, complete concepts and relationships between concepts from <sup>fi</sup>nancial statements, which is particularly useful for developing <sup>fi</sup>nance ontology. In the taxonomies, each term is de<sup>fi</sup>ned with speci<sup>fi</sup>c attributes that include label, de<sup>fi</sup>nition, and potential references.

Drawing knowledge from the above ontologies and other online <sup>fi</sup>- nancial resources such as Google Finance,<sup>5</sup> Yahoo!Finance,<sup>6</sup> and MSN Money Central,<sup>7</sup> we developed an ontology of Income Statement, which is represented with UML class diagram (see Appendix 2).

In the framework, the FinO interoperates diverse <sup>fi</sup>nancial data sources via ontology mapping. Ontology mapping provides a common layer from which several ontologies could be accessed and hence could exchange information in semantically sound manners [30]. The approaches to ontology mapping can be summarized into three categories [18]: 1) one-to-one approach, where each ontology communicates with another ontology based on a set of translating functions; 2) single-shared ontology, where a common ontology is developed to which every speci<sup>fi</sup>c ontology is mapped; and 3) ontology clustering, where ontology sources are clustered based on their similarity. The FinO is designed as a single-shared ontology.

The semantic heterogeneity between two ontologies occurs in at least two levels: concepts and instances, as discussed in Section 2. At the concept level, mapping can be created between the concepts of FinO and ontologies used by individual online <sup>fi</sup>nancial resources. As a result, the data from different sources such as Google Finance and Compustat can be mapped to each other. OFFDM aims to address data quality problems associated with online <sup>fi</sup>nancial data, which helps to improve the performance of <sup>fi</sup>nancial decision-making. This is demonstrated with a case study in Section 5.

## 5. A case study — portfolio management

We select portfolio management, a typical case of intelligent <sup>fi</sup>- nancial decision-making to demonstrate how OFFDM is used to detect and address related data quality problems.

## 5.1. Portfolio management

Portfolio management concerns how individuals decide which securities to hold in investment portfolios and how funds should be allocated among broader asset classes, such as stocks versus bonds. Its primary goal is to choose a set of risk assets that could maximize the return under certain risk condition or minimize the risk for obtaining a speci<sup>fi</sup>c return.

The process of portfolio management (see Fig. 2) can be divided into three phases: data collection, asset valuation, and portfolio optimization [6,35]. Data collection identi<sup>fi</sup>es what data might be used to predict an asset's value. Asset valuation is the process of estimating the potential market value of a <sup>fi</sup>nancial asset, which is in<sup>fl</sup>uenced by many factors. Portfolio optimization starts with a set of assets and generates a weight combination for the optimal risky portfolio that lies on the ef<sup>fi</sup>cient frontier [45]. Additionally, the data collection phase provides inputs for the asset valuation phase, and asset valuation in turn provides the prediction of assets which will guide portfolio optimization. Further, portfolio management is an iterative process where a later stage can provide feedback to an earlier stage.

## 5.2. Detecting data quality problems

Without losing the generality of <sup>fi</sup>nancial data, Income Statement was selected to illustrate how to apply the OFFDM. Fig. 3 shows the mapping between a subset of the concepts of the Income Statements from Google Finance and Compustat via FinO. Based on the mapping, the OFFDM can be used to address data quality problems. The process of detecting and handling <sup>fi</sup>nancial data quality problems, particularly missing values, is illustrated in Fig. 4. Once a missing value in the data extracted from source Si is identi<sup>fi</sup>ed, another data source Sj (j≠i) will be checked against to retrieve the value that is FinO-mapped to the missing value. If the search is successful, the retrieved value would be validated and used to <sup>fi</sup>ll in the missing value. Otherwise, the missing value would be estimated using weighted K-nearest neighbors [61]. The detail of how to address data quality problems is introduced in the next section.

![](/api/attachments/AYT8GH4Z/fulltext/images/6968ca573c69d8d4d569da621eec2c94d4f5df89f3a7e618cab1f7f3a38549dd.jpg)  
Fig. 2. Processes of portfolio management.

![](/api/attachments/AYT8GH4Z/fulltext/images/69fc2e9e2bcdf585d2199ac223dc9a2655fe5e0adc064d20aa9723e1439f15da.jpg)  
Fig. 3. FinO-supported mapping of Income Statement concepts between Google Finance and Compustat.

## 5.3. Addressing data quality problems

We illustrate how to apply OFFDM to address all of the six types of data quality problems listed in Table 1 in detail. Description logic [2] is used to formalize the problems for conciseness, and additional symbols may be introduced to express the logic as needed.

## 5.3.1. Missing data

Suppose that the value of sales for <sup>fi</sup>rm A is missing from Compustat. Based on the proposed framework, the concept of sales in Compustat is equivalent to the concept of sales revenue in FinO, and the latter is equivalent to the concept of total revenue in Google

![](/api/attachments/AYT8GH4Z/fulltext/images/9771362b9734e2028cb5bfbc796173c106f7c75fe9aea44dcd5ea02c71f2075f.jpg)  
Fig. 4. Process <sup>fl</sup>ow for handling missing values.

Finance. Thus, it can be inferred that sales in Compustat is equivalent to total revenue in Google Finance. Thus, if the value of total revenue for <sup>fi</sup>rm A is available from Google Finance, it can be used to <sup>fi</sup>ll in the missing value. The inference process is formally described as follows:

Compustat : Sales≡FinO : Sales Revenue Google Finance : Total Revenue≡FinO : Sales Revenue ⇒Compustat : Sales≡Google Finance : Total Revenue:

## 5.3.2. Terminological ambiguity

The terminological ambiguity problem is also manifested in the previous example. Take accounts payable as another example. The de<sup>fi</sup>nition of the term from Yahoo!Finance is broader than that from Google Finance in that the former is composed of accrued expenses and other current liabilities, total in addition to accounts payable from Google Finance. According to the proposed framework, it can be inferred that the concept of accounts payable from Yahoo!Finance is equivalent to the union of the concepts of accounts payable, accrued expenses and other current liabilities, total from Google Finance.

Yahoo!Finance : Accounts Payable≡FinO : Accounts Payable

add Google Finance : Accounts Payable; Google Finance:

Accrued Expenses; Google Finance :Other Current Liabilities Total ≡FinO : Accounts Payable

⇒Yahoo!Finance : Accounts Payable≡add Google Finance:

Accounts Payable; Google Finance :Accrued Expenses;

Google Finance : Other Current Liabilities Total :

## 5.3.3. Conceptual inaccuracy

One example of conceptual inaccuracy, in particular the partwhole mapping, is the lack of precision in the de<sup>fi</sup>nition of total revenue. Conceptually, total revenue from Google Finance can be used to reference revenue of goods, revenue of service, or a combination of both. To address the lack of suf<sup>fi</sup>cient information for accurate interpretation of the concept, a mapping rule can be de<sup>fi</sup>ned between the related concepts from FinO and an online <sup>fi</sup>nancial data source. Given that total revenue from Google Finance is de<sup>fi</sup>ned as the sum of revenue of goods and revenue of service from FinO, the following inference can be made.

add EDGAR : Revenue of Goods; EDGAR : Revenue of Services ≡FinO : Sales Revenue Google Finance : Total Revenue ≡FinO : Sales Revenue

⇒Google Finance : Total Revenue≡add EDGAR : Revenue of Goods; EDGAR : Revenue of Services :

## 5.3.4. Unreliable data

Unreliable data can be detected by making inferences using the axioms encoded in the FinO. For example, Gross profit from the FinO is computed as the difference between sales revenue and cost of goods sold, where minus represents the corresponding arithmetic operatio'n:

Google Finance : Gross Profit≡FinO: Gross Profit

FinO: Gross Profit≡minus FinO: Sales Revenue; FinO: Cost of Goods Sold Google Finance: Total Revenue≡FinO: Sales Revenue

Google Finance : Cost of Revenue Total≡FinO : Cost of Goods Sold

⇒Google Finance : Gross Profit≡minus Google Finance : Total Revenue; Google Finance : Cost of Revenue Total :

According to the above inference result, the original value of gross profit for NBR from Google Finance (i.e., \$2195.90), as shown in Table 2, should be replaced with \$2318.45.

## 5.3.5. Inconsistent representation

As discussed in Section 3.5, ticker symbols manifest inconsistent representation in that the representation of the extensions of the ticker symbols for some stocks may differ between different data sources [11]. For example, Berkshire Hathaway trades both class A and class B on the NYSE. Their ticker symbols are BRK.A and BRK.B in Google Finance and MSN Money Central, which are different from BRK-A and BRK-B in Yahoo!Finance. Such extensions only apply to a subset of stocks, such as capital stocks having more than one issue or preferred stocks, which may be resolved by de<sup>fi</sup>ning mapping rules between ontologies. The inference process is formally described as follows, where replace represents a replacement function:

Google Finance: Symbol Extension≡FinO: Symbol Extension

FinO : Symbol Extension≡replace

Yahoo!Finance: Symbol Extension; ‘ ’; ‘ :’

Google Finance: Symbol Extension≡replace

Yahoo!Finance: Symbol Extension; ‘  ’; ‘:’ :

## 5.3.6. Incomplete domain

FinO contains a concept hierarchy of industry sectors such as Financial. In the hierarchy, a super-class contains properties that are generic to all of its sub-classes while a sub-class may contain some properties that are unique to it. When retrieving the value of a property for a <sup>fi</sup>rm, the concept associated with the <sup>fi</sup>rm is checked against to see whether the requested property is applicable. If the result is negative, a null value would be returned. For instance, the value of inventory for the ticker AXP is null based on the following inference.

AXP∈financial; inventory:financial≡⊥ ⇒inventory:AXP≡⊥:

## 6. Evaluation

Our general hypothesis suggests that the OFFDM is more effective than other traditional methods for addressing data quality problems in <sup>fi</sup>nancial decision-making. We conducted an experiment with real-world data to evaluate the effectiveness of the proposed framework for asset valuation in portfolio management.

FinO is the core of the framework. There are two primary approaches to evaluating an ontology: its internal content and structure, and its role in facilitating certain applications [27]. Typically, an ontology will be used in some kinds of application or task. The outputs of the application, or its performance on the given task, might be better or worse depending partly on the ontology used in it. Therefore, a potentially effective approach to ontology evaluation would be focusing on how effective a particular ontology is in the context of an application [8]. This is elegant in the sense that the output of the application might be something for which a relatively straightforward and non-problematic evaluation approach already exists [7]. We adopted the latter approach in this study. Moreover, the missing values were selected as the focus of the evaluation because the problem is more commonplace with real-world <sup>fi</sup>nancial data.

Table 2  
A segment of 2006 income statement for NBR from Google Finance.

<table><tr><td>Revenue</td><td>4707.29</td></tr><tr><td>Other revenue, total</td><td>122.55</td></tr><tr><td>Total revenue</td><td>4829.84</td></tr><tr><td>Cost of revenue, total</td><td>2511.39</td></tr><tr><td>Gross profit</td><td>2195.90</td></tr></table>

Table 3  
Financial ratios (input features) and their groupings.

<table><tr><td>Grouping</td><td>Financial ratio</td></tr><tr><td>Profitability ratios</td><td>Earnings before interests and taxes/total assetsNet income/net worthGross profit/total assetsNet income/gross profit</td></tr><tr><td>Solvency ratios</td><td>Current liabilities/total assetsTotal liabilities/total assetsLong term debt/total equityCurrent assets/current liabilitiesInventories/current liabilities</td></tr><tr><td>Managerial performance ratios</td><td>Interest expenses/salesSelling, general, &amp; administrative expenses/salesAccounts receivable/salesAccounts payable/inventoriesAccounts payable/sales</td></tr></table>

## 6.1. Datasets

We selected the <sup>fi</sup>nancial data of S&P 500 companies from Standard & Poor's Compustat North America dataset. The data were extracted for both the fourth quarter of 2009 and the <sup>fi</sup>rst quarter of 2010, and the data for the <sup>fi</sup>rst time period was used to predict the trend of stock earnings for the second time period. According to an earlier study on <sup>fi</sup>nancial decision-making [43], 14 <sup>fi</sup>nancial ratios were computed for each of the companies to support asset valuation. These <sup>fi</sup>nancial ratios are clustered into three groups [12]: pro<sup>fi</sup>tability ratios, solvency ratios, and managerial performance ratios (see Table 3).

Among the selected <sup>fi</sup>nancial ratios, eight involves <sup>fi</sup>nancial attributes that contain missing values to varying degree such as total equity, inventories, interest expenses, selling, general, & administrative expenses, accounts receivable, and accounts payable (see the last column of Table 4), which lead to missing values for these <sup>fi</sup>nancial ratios, as shown in Table 4. It is noted from Table 4 that the occurrence frequency of missing values is highest for Accounts payable/Inventories. A detailed investigation of individual cases reveals that 98 out of 101 cases were caused by having zero as the value of their inventories. In order to avoid confusing missing values with null (not available), we removed those 98 <sup>fi</sup>rms from the dataset. The <sup>fi</sup>nancial ratio that has the second highest frequency of missing values is Selling, general, & administrative expenses/Sales, which was selected as the focus of evaluation in this study. In other words, missing values of other <sup>fi</sup>nancial ratios are ignored by being replaced with their actual values in the dataset, following the procedure for handling missing values, as introduced in Fig. 4. This helps keep the evaluation focus on the impact of missing values for an individual input feature.

Frequency of missing values.

<table><tr><td>Financial ratio</td><td># of firms</td><td>Missing items</td></tr><tr><td>Net income/net equity</td><td>2</td><td>Total equity</td></tr><tr><td>Long term debt/total equity</td><td>3</td><td>Total equity</td></tr><tr><td>Inventories/current liabilities</td><td>2</td><td>Inventories</td></tr><tr><td>Interest expenses/sales</td><td>34</td><td>Interest expenses</td></tr><tr><td>Selling, general, &amp; administrative expenses/sales</td><td>96</td><td>Selling, general, &amp; administrative expenses</td></tr><tr><td>Accounts receivable/sales</td><td>1</td><td>Accounts receivable</td></tr><tr><td>Accounts payable/inventories</td><td> $101^a$ </td><td>Inventories</td></tr><tr><td>Accounts payable/sales</td><td>1</td><td>Accounts payable</td></tr></table>

<sup>a</sup> 98 out of the 101 cases do not have missing value problems but null (no inventory).

## 6.2. Classification problem and techniques

Considering the cost of trading stocks, the goal of asset valuation is to predict relative change instead of absolute value. Thus, the target variable is relative change in stock earning (RCSE), as de<sup>fi</sup>ned in Formula (1).

$$
\mathrm{RCSE} _ {j} (t + 1) = \left[ P _ {i} (t + 1) + D _ {i} (t + 1)\right) - \left(P _ {i} (t) + D _ {i} (t)\right) ] / \left(P _ {i} (t) + D _ {i} (t)\right)\tag{1}
$$

where $P _ { i } ( t )$ represents the price of ith stock during time period t, and $D _ { \mathrm { i } } ( t )$ represents the dividend of ith stock during time period t. RCSE is a continuous variable, which is transformed into three-valued class labels using the equal-width method: DOWN (≤.011), NOCHG (No Change) (≤.104), and UP (>.105). Arti<sup>fi</sup>cial Neural Network (ANN) was used to build prediction models for asset valuation because of its popularity in <sup>fi</sup>nancial decision making [37,69]. ANN can be de-<sup>fi</sup>ned as a computer model to emulate human pattern recognition function through a parallel processing structure. A neural network usually consists of three layers, which are input, hidden, and output. A set of input features is <sup>fi</sup>rst entered into a neural network. After each neuron in a hidden layer receives the entry from the input layer, the input values are converted to an output value by applying the weights on edges between the two layers. Then the output is passed to all neurons in the next layer. The weights between two neurons are automatically adjusted through an iterative process by testing the training sample in the neural network.

Neuro-fuzzy System (NFS) employs a supervised learning algorithm to train fuzzy sets and linguistic rules by modifying the structure and parameters of a neuro-fuzzy model [46], and was thus also selected to build prediction models. Speci<sup>fi</sup>cally, Weka [68] and NEFCLASS-J [47] were selected as the tools that implement ANN and NFS, respectively. In addition to handling missing values, NEFCLASS-J is also featured with automatic cross validation, automatic determination of the rule base size, and automatic pruning of a classi<sup>fi</sup>er to reduce its size and to increase its interpretability.

All of the ANN models were trained and tested using the same con<sup>fi</sup>gurations and parameter settings (e.g., learning rate=0.1, #nodes in the hidden layer=half of the total of inputs and outputs). The same principle applies to creating and testing NFS models, where the adjustment of parameters such as the maximum number of rules and re-learning of rule base were made only when they are of interest. Ten-fold cross validations were used to test the generality of all the prediction models.

## 6.3. Baselines and evaluation metrics

The transformed RCSE was the target class label, and the 14 <sup>fi</sup>nancial ratios were used as input features. The experiment considered four different strategies for handling missing values.

• Address it using OFFDM (OFF)

• Replace with the mean of available observations (AVG)

• Ignore missing values (IGN)

• Set the membership degree to ‘one’ for all fuzzy sets of the attribute (FUZ)

Among them, OFF is based on the proposed framework OFFDM in this study, AVG and IGN re<sup>fl</sup>ect common strategies for dealing with missing values in the literature as well as existing tools, thereby serving as the baseline method, and FUZ is featured with its ability to handle missing values using the concept of fuzzy sets [46].

The four strategies for handling missing values led to four versions of the dataset. All datasets share the same values for all the input features (<sup>fi</sup>nancial ratios) except for missing values of selling, general, & administrative expenses/sales, which were handled according to individual strategies. The sizes of all versions are the same (402 instances) except for IGN, and the size for IGN is 341 after <sup>fi</sup>ltering those items with missing values.

Table 5  
Accuracy and RMSE for asset valuation.

<table><tr><td>Datasets</td><td>Accuracies</td><td>Root mean squared error</td><td># of instances</td></tr><tr><td>OFF</td><td>44.8</td><td>0.464</td><td>402</td></tr><tr><td>AVG</td><td>39.1</td><td>0.468</td><td>402</td></tr><tr><td>IGN</td><td>38.7</td><td>0.473</td><td>341</td></tr><tr><td>FUZ</td><td>48.0</td><td>0.505</td><td>402</td></tr></table>

Three metrics were adopted to evaluate the prediction models fully, including accuracy, Root Mean Squared Error (RMSE), and F-measure. Accuracy is de<sup>fi</sup>ned as the percentage of <sup>fi</sup>rms whose trends of stock earnings are correctly predicted. RMSE is de<sup>fi</sup>ned as the square root of mean squared error. F-measure is de<sup>fi</sup>ned as the harmonic mean of precision and recall, where precision is de<sup>fi</sup>ned as the percentage of correct results in all predicted results, and recall is de<sup>fi</sup>ned as the percentage of correctly predicted results in all predicted results.

## 6.4. Results

The performance of prediction models is reported in Tables 5 and 6.

Given that the three target labels are equally distributed, the accuracy for random selection is 33%. It is shown from Table 5 that all the accuracies are higher than that of random selection. Compared with other methods, FUZ performed the best achieving an accuracy of 48%, OFF the second best achieving an accuracy of 44.8%, and IGN the worst with the accuracy below 40%. It is also noted that the reported results of FUZ were based on the number of rules selected by the system, which was 57 in this case. The problems with having so many rules in relation to the size of the dataset are discussed in Section 7. It is shown from Table 6 that, among the three predicted trends, F-measures are consistently higher for UP and DOWN categories than the NOCHG category. This is not surprising because the NOCHG category is conceptually close to both UP and DOWN categories.

## 7. Discussion

The experimental results show that the proposed framework OFFDM outperformed the two baseline methods for handling missing value, including AVG and IGN. The results demonstrate that the ontology-based method for addressing the missing-value problem is more effective for asset valuation than the traditional methods such as replacement with mean values and ignoring the missing values.

The neuro-fuzzy approach performed the best, suggesting that the approach could be an effective alternative to the OFFDM for handling missing values. Nevertheless, both the number of rules (i.e., 57) and the ratio of the number of rules created by the system to the data size (about 1:6.5) are very high. As a result, not only would it be dif<sup>fi</sup>cult for human users to differentiate and select the rules but also the rules would be less generalizable. To improve the utility of the learned rules, pruning was followed by limiting the maximum number of rules. In addition, given that the NEFCLASS-J is capable of relearning the rule base based on an existing rule base, we considered both settings when the option of ‘relearn the rule base’ is either enabled or disabled. The accuracies of FUZ for varying number of rules are reported in Fig. 5.

F-measures for each of the target labels.

<table><tr><td>Datasets</td><td>UP</td><td>NOCHG</td><td>DOWN</td></tr><tr><td>OFF</td><td>0.48</td><td>0.355</td><td>0.51</td></tr><tr><td>AVG</td><td>0.45</td><td>0.28</td><td>0.43</td></tr><tr><td>IGN</td><td>0.44</td><td>0.34</td><td>0.38</td></tr><tr><td>FUZ</td><td>0.51</td><td>0.41</td><td>0.53</td></tr></table>

It is shown from Fig. 5 that the accuracy of neuro-fuzzy models degrades quickly as the number of rules reduces. For example, when the number of rules is pruned by half to 30, the accuracy is reduced to 18.9% for the setting of “with a rule base”, and to 31.3% for the setting “without a rule base”. When the number of rules is pruned to 8, which would be manageable by human users, the accuracy is reduced to 4.7% and 6.7% for the same two settings, respectively. These results clearly show that the performance of neuro-fuzzy models on datasets with missing values is gained at the expense of usability and generality.

From a theoretical standpoint, to the best of our knowledge, this is the <sup>fi</sup>rst study that utilizes ontology mapping to improve the quality of online <sup>fi</sup>nancial data. The proposed framework OFFDM interoperates <sup>fi</sup>nancial data from various online sources, which ultimately helps improve the performance of <sup>fi</sup>nancial decision-making. In addition, the ontology-anchored taxonomy of quality problems with online <sup>fi</sup>nancial data proposed in this study is instrumental to data quality research and practice in general. Second, by extending the applications of ontology in data quality research from dealing with quality assessment to addressing quality improvement issues, the OFFDM provides a holistic view and a complete solution to data quality problems. Last but not the least, this study demonstrates how to improve <sup>fi</sup>nancial decision-making, particularly asset valuation, by handling data quality problems.

The <sup>fi</sup>ndings of this study also provide several practical guidelines for <sup>fi</sup>nancial decision-making. First, <sup>fi</sup>nance, as a well-established domain, has had its data quality problems largely ignored. This study, however, clearly identi<sup>fi</sup>es several major categories of quality problems associated with online <sup>fi</sup>nancial data. The taxonomy of data quality problems provides <sup>fi</sup>nancial experts with awareness of and guidance on what types of data quality problems they might face in their own areas. Second, effective guidance on portfolio management has long been an interest for practitioners including business, organizations, and individuals. This study shows that improving data quality is one promising way of boosting the performance of <sup>fi</sup>nancial decisionmaking. It enriches the literature by showing that poor data quality can have substantially negative social and economic impacts. Third, as the use of online <sup>fi</sup>nancial data and information resources increases, the proposed OFFDM framework would have more signi<sup>fi</sup>cant implica tions for the development of <sup>fi</sup>nancial decision support. For those who cannot afford professional <sup>fi</sup>nancial data sources such as Compustat, the framework proposed in this study enhances their abilities to utilize online <sup>fi</sup>nancial data effectively.

The proposed framework can be applied to other application domains where relevant information about an entity/object is often not only spread across multiple systems with overlap in content, but also different in data formats and naming schemes such as life science [52]. For instance, there are thousands of life science databases and billions of database records [24]. As a result, <sup>fi</sup>nding reliable and complete information about an entity is a challenging task. The proposed ontology-based framework helps mitigate the data problem by exploiting existing domain knowledge about the relationship across entities in different databases.

![](/api/attachments/AYT8GH4Z/fulltext/images/db5b353e972960f98c662268e6198475c595da6613c1c6cc43ba3651ca80450f.jpg)  
Fig. 5. Accuracies of FUZ for varying number of rules.

This study exposes several limitations. First, since the primary objective of this study is to address data quality problems, feature selection was outside the scope of this study and thus was not implemented. Employing feature selection could improve the performance of asset valuation models. Second, although missing values were the focal problem in our experimental evaluation, the proposed framework can be used to address other types of data quality problems such as inconsistent representation and unreliable data. Further, missing values were con<sup>fi</sup>ned to one single input feature in the study. When a dataset involves missing values in two or more input features, as shown in our dataset, it should gain more bene<sup>fi</sup>t from the proposed framework. Thus, the effectiveness of the framework should be fully explored in future research. Similarly, we expect that in addition to <sup>fi</sup>nancial statements, the proposed framework will be generally applicable to other types of <sup>fi</sup>nancial data and <sup>fi</sup>nancial decision-making problems, which warrants future research.

## 8. Conclusions

An ontology-based framework is proposed in this research to improve <sup>fi</sup>nancial data quality. The framework can be used to address various types of problems associated with online <sup>fi</sup>nancial data. The positive impact of the framework on the performance of <sup>fi</sup>nancial decision-making is empirically demonstrated with asset valuation.

Improving quality of <sup>fi</sup>nancial data is just the <sup>fi</sup>rst step toward effective <sup>fi</sup>nancial decision-making. In view that the <sup>fi</sup>nancial market is dynamic, the domain knowledge modeled in FinO (Financial Ontology) should evolve accordingly.

## Appendix 1

The notation of missing data in Compustat.

<table><tr><td colspan="2">Markers in Compustat</td></tr><tr><td>Code</td><td>Description</td></tr><tr><td>@Af</td><td>Annual figure (only annual data is available for quarterly items)</td></tr><tr><td>@CF</td><td>Combined figure (the figure is combined in another item)</td></tr><tr><td>@IF</td><td>Insignificant figure (the number is immaterial)</td></tr><tr><td>@NA</td><td>Not available (company does not disclose information about the item)</td></tr><tr><td>@NC</td><td>Not calculable (rules for calculation were not met)</td></tr><tr><td>@NM</td><td>Not meaningful (item is not meaningful for a company)</td></tr><tr><td>@SF</td><td>Semi-annual figure (only semi-annual data is available for quarterly items)</td></tr></table>

## Appendix 2

An ontology of income statement.

![](/api/attachments/AYT8GH4Z/fulltext/images/7889d1a9479402cd0d7d2640a2ad9d0efd307b77bc94872501632e4e93c95640.jpg)  
Note: the links between concepts denote composition relationships.

## References

[1] Anonymous, Preferred Ticker Symbols & Security NamesRetrieved on January 15, 2012 from, http://www.quantumonline.com/PfdSymbolsNames.cfm

[2] F. Baader, D. Calvanese, D. McGuinness, D. Nardi, P. Patel-Schneider, The Description Logic Handbook: Theory, Implementation, Applications, Cambridge University Press, Cambridge, UK, 2003.

[3] D. Ballou, R. Wang, H. Pazer, G. Kumar Tayi, Modeling information manufacturing systems to determine information product quality, Management Science 44 (4) (1998) 462–484.

[4] A. Bansal, R.J. Kauffman, R.R. Weitz, Comparing the modeling performance of regression and neural networks as data quality varies: a business value approach, Journal of Management Information Systems 10 (1) (1993) 11–32.

[5] S. Bhattacharyya, O.V. Pictet, G. Zumbach, Knowledge-intensive genetic discovery in foreign exchange markets, IEEE Transactions on Evolutionary Computation 6 (2) (2002) 169–181.

[6] Z. Bodie, R.C. Merton, Finance, Preliminary ed. Prentice Hall, Upper Saddle River, NJ, 1998.

[7] J. Brank, M. Grobelnik, D. Mladenic, A survey of ontology evaluation techniques, Conference on Data Mining and Data Warehouses (SiKDD 2005), Ljubljana, Slovenia, 2005.

[8] C. Brewster, H. Alani, S. Dasmahapatra, Y. Wilks, Data driven ontology evaluation, International Conference on Language Resources and Evaluation, Lisbon, Portugal, 2004.

[9] P. Buneman, A. Chapman, J. Cheney, Provenance management in curated databases, Proceedings of the 2006 International Conference on Management of Data, ACM, Chicago, IL, USA, 2006, pp. 539–550.

[10] O.H. Choi, L. Jun-Eun, N. Hong-Seok, B. Doo-Kwon, An ef<sup>fi</sup>cient method of data quality using quality evaluation ontology, Proceedings of the Third International Conference on Convergence and Hybrid Information Technology, IEEE Computer Society, Busan, Korea, 2008, pp. 1058–1061.

[11] S.P. Corporation, The Ticker Symbol Book, McGraw-Hill, New York, 1998.

[12] J.K. Courtis, Modelling a <sup>fi</sup>nancial ratios categoric framework, Journal of Business Finance & Accounting 5 (4) (1978) 371–386.

[13] N. Dalvi, D. Suciu, Management of probabilistic data: foundations and challenges, Proceedings of the Twenty-sixth ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems. ACM. Bejjing, China. 2007.

[14] B. Davidson, Y.W. Lee, R. Wang, Developing data production maps: meeting patient discharge data submission requirements, International Journal of Healthcare Technology and Management 6 (2) (2004) 223–240.

[15] G.J. Deboeck, M. Cader, Pre- and Postprocessing of Financial Data, in: Trading on the Edge: Neural, Genetic, and Fuzzy Systems for Chaotic Financial Markets, John Wiley & Sons, New York, 1994.

[16] D. Deller, M. Stubenrath, C. Weber, A survey on the use of the Internet for investor relations in the USA, the UK and Germany, The European Accounting Review 8 (2) (1999) 351–364.

[17] Y. Ding, S. Foo, Ontology research and development. Part 1 — a review of ontology generation, Journal of Information Science 28 (2) (2002) 123–136.

[18] Y. Ding, S. Foo, Ontology research and development. Part 2 — a review of ontology mapping and evolving, Journal of Information Science 28 (5) (2002) 375–388.

[19] W. Fan, H. Lu, S.E. Madnick, D. Cheung, Discovering and reconciling value con<sup>fl</sup>icts for numerical data integration, Information Systems 26 (2001) 635–656

[21] C.W. Fisher, B.R. Kingma, Criticality of data quality as exempli<sup>fi</sup>ed in two disasters, Information Management 39 (2) (2001) 109–116.

[22] C. Focardi, Data quality: the cost of dirty data in the decondary market, Mortgage Banking 68 (5) (2008) 88–89.

[23] A. Frank, Data quality ontology: an ontology for imperfect knowledge, Spatial Informa tion Theory, 2007, pp. 406–420.

[24] M.Y. Galperin, G.R. Cochrane, The 2011 Nucleic Acids Research Database Issue and the online Molecular Biology Database Collection, Nucleic Acids Research 39 (Suppl. 1) (2011) D1–D6.

[25] C.A.E. Goodharta, M. O'Hara, High frequency data in <sup>fi</sup>nancial markets: issues and applications, Journal of Empirical Finance 4 (2–3) (1997) 73–114.

[26] T. Gruber, A transitional approach to portable ontology speci<sup>fi</sup>cations, Knowledge Acquisition 5 (2) (1993) 39–41.

[27] J. Hartman, P. Spyns, A. Giboin, D. Maynard, R. Cuel, M.C. Suárez-Figueroa, Y. Sure, D1.2.3 methods for ontology evaluation, Deliverable for Knowledge Web Consortium.2005.

[28] A. Hevner, S.T. March, J. Park, S. Ram, Design science research in information systems, MIS Quarterly 28 (1) (2004) 75–105.

[29] W. Jung, A review of research: an investigation of the impact of data quality on decision performance, Proceedings of the 2004 International Symposium on Information and Communication Technologies, Las Vegas, Nevada, 2004.

[30] Y. Kalfoglou, M. Schorlemmer, Ontology mapping: the state of the art, The Knowledge Engineering Review 18 (01) (2003) 1–31.

[31] D. Kanellopoulos, S. Kotsiantis, V. Tampakas, Towards an ontology-based system for intelligent prediction of <sup>fi</sup>rms with fraudulent <sup>fi</sup>nancial statements, IEEE Conference on Emerging Technologies and Factory Automation, Patras, 2007.

[32] S. Kaza, H. Chen, Evaluating ontology mapping techniques: an experiment in public safety information sharing, Decision Support Systems 45 (4) (2008) 714–728.

[33] K. Kerr, The Institutionalization of Data Quality in the New Zealand Health Sector, The University of Auckland, New Zealand, 2004.

[34] W. Kim, J. Seo, Classifying schematic and data heterogeneity in multidatabase systems, Computer 24 (12) (1991) 12–18.

[35] J. Kingdon, Intelligent Systems and Financial Forecasting, Springer-Verlag, London, 1997.

[36] J. Kingston, B. Schafer, W. Vandenberghe, Towards a <sup>fi</sup>nancial fraud ontology: a legal modelling approach, Arti<sup>fi</sup>cal Intelligence and Law 12 (4) (2006) 419–446.

[37] M. Lam, Neural network techniques for <sup>fi</sup>nancial performance prediction: integrating fundamental and technical analysis, Decision Support Systems 37 (4) (2004) 567–581.

[38] Y.W. Lee, Crafting rules: context-re<sup>fl</sup>ective data quality problem solving, Journal of Management Information Systems 20 (3) (2003) 93–119.

[39] Y.W. Lee, D.M. Strong, Knowing-why about data processes and data quality, Journal of Management Information Systems 20 (3) (2003) 13–39.

[40] D. Loshin, Monitoring data quality performance using data quality metrics [white paper] Retrieved on January 19, 2012 from, it.ojp.gov/docdownloader.aspx?ddid=9992006.

[41] S. Madnick, H. Zhu, Improving data quality through effective use of data semantics, Data & Knowledge Engineering 59 (2) (2006) 460–475

[42] S.E. Madnick, R.Y. Wang, Y.W. Lee, H. Zhu, Overview and framework for data and information quality research, Journal of Data and Information Quality 1 (1) (2009) 1–22.

[43] N.F. Matsatsinis, M. Doumpos, C. Zopounidis, Knowledge acquisition and representation for expert systems in the <sup>fi</sup>eld of <sup>fi</sup>nancial analysis, Expert Systems with Applications 12 (2) (1997) 247–262.

[44] M. McMahon, Career Coach: Decision Making, Pulse, United Kingdom, 2007.

[45] R.C. Merton, An analytic derivation of the ef<sup>fi</sup>cient portfolio frontier, Journal of Financial and Quantitative Analysis 7 (4) (1972) 1851–1872.

[46] D. Nauck, R. Kruse, Obtaining interpretable fuzzy classi<sup>fi</sup>cation rules from medical data, Arti<sup>fi</sup>cial Intelligence in Medicine 16 (2) (1999) 149–169.

[47] D. Nauck, U. Nauck, R. Kruse, NEFCLASS for Java—new learning algorithms, 18th International Conference of the North American Fuzzy Information Processing Society, New York, NY, USA, 1999.

[48] I. Niles, A. Pease, Towards a standard upper ontology, Proceedings of the 2nd International Conference on Formal Ontology in Information Systems, ACM, Ogunquit, Maine, 2001, pp. 2–9.

[49] Oracle, The emerging <sup>fi</sup>eld of <sup>fi</sup>nancial data quality management [white paper]Retrieved on January 19, 2012 from, http://www.oracle.com/us/products/middleware/ bus-int/064080.pdf2008.

[50] E.M. Pierce, Assessing data quality with control matrices, Communications of the ACM 47 (2) (2004) 82–86.

[51] L.L. Pipino, Y.W. Lee, R.Y. Wang, Data quality assessment, Communications of the ACM 45 (4) (2002) 211–218.

[52] D. Quan, Improving life sciences information retrieval using semantic web technology, Brie<sup>fi</sup>ngs in Bioinformatics 8 (3) (2007) 172–182.

[53] A. Raeder, Financial and investment sources on the Web, Search 5 (4) (1997) 44–49.

[54] T.C. Redman, Data Quality for the Information Age, Artech House, Boston, MA, 1996.

[55] T.C. Redman, The impact of poor data quality on the typical enterprise, Commu nications of the ACM 41 (2) (1998) 79–82.

[56] G. Shankaranarayanan, Y. Cai, Supporting data quality management in decisionmaking, Decision Support Systems 42 (1) (2006) 302–317.

[57] H. Simon, Administrative Behavior, 3rd ed. The Free Press, New York, 1976.

[58] A. Sujanani, P. Ray, N. Paramesh, R. Bhar, The development of ontology driven multi-agent systems: a case study in the <sup>fi</sup>nancial services domain, Proceedings of the IEEE International Workshop on Business Services Networks, IEEE Press, Hong Kong, 2005, 1-1pp.

[59] G.K. Tayi, D.P. Ballou, Examining data quality, Communications of the ACM 41 (2) (1998) 54–57.

[60] M.E. Thatcher, D.E. Pingry, An economic model of product quality and IT value, Information Systems Research 15 (3) (2004) 268–286.

[61] O. Troyanskaya, M. Cantor, G. Sherlock, P. Brown, T. Hastie, R. Tibshirani, D. Botstein, R.B. Altman, Missing value estimation methods for DNA microarrays, Bioinformatics 17 (6) (2001) 520–525.

[62] A. Tsakonas, G. Dounias, M. Doumpos, C. Zopounidis, Bankruptcy prediction with neural logic networks by means of grammar-guided genetic programming, Expert Systems with Applications 30 (3) (2006) 449–461.

[63] D. Valiante, Survey <sup>fi</sup>nds <sup>fi</sup>nancial professionals dissatis<sup>fi</sup>ed with market data quality, Wall Street & Technology, 2008 Retrieved on Mar.1 2011 from http:// www.wallstreetandtech.com/articles/208801964.

[64] Y. Wand, R.Y. Wang, Anchoring data quality dimensions in ontological foundations, Communications of the ACM 39 (11) (1996) 86–95.

[65] R.W. Wang, D.M. Strong, Beyond accuracy: what data quality means to data consumers, Journal of Management Information Systems 12 (4) (1996) 5–25.

[66] R.Y. Wang, V.C. Storey, C.P. Firth, A framework for analysis of data quality research, IEEE Transactions on Knowledge and Data Engineering 7 (4) (1995) 623–640.

[67] S. Watts, G. Shankaranarayanan, A. Even, Data quality assessment in context: a cognitive perspective, Decision Support Systems 48 (1) (2009) 202–211.

[68] I.H. Witten, E. Frank, Data Mining: Practical Machine Learning Tools and Techniques, 2nd edition Morgan Kaufmann, San Francisco, 2005.

[69] D. Zhang, L. Zhou, Discovering golden nuggets: data mining in <sup>fi</sup>nancial application, IEEE Transactions on Systems, Man, and Cybernetics Part C: Applications and Reviews 34 (4) (2004) 513–522.

[70] Z. Zhang, C. Zhang, S.S. Ong, Building an ontology for <sup>fi</sup>nancial investment, Proceedings of the 2nd International Conference on Intelligent Data Engineering and Automated Learning, Data Mining, Financial Engineering, and Intelligent Agents, Springer-Verlag, 2000.

[71] G. Zhao, J. Kingston, K. Kerremans, F. Coppens, R. Verlinden, R. Temmerman, R. Meersman, Engineering an ontology of <sup>fi</sup>nancial securities fraud, On the Move to Meaningful Internet Systems Workshops, 2004.

[72] L. Zhou, Ontology learning: state of the art and open issues, Information Technology and Management 8 (3) (2007) 241–252.

Jie Du received her B.S. degree in information systems from Southwest Jiaotong University, China, in 2001, M.S. degree in management science from Beijing Jiaotong University, China, in 2004, and M.S. degree in information systems from the University of Maryland, Baltimore County, in 2009. Currently, she is pursuing her Ph.D. degree in information systems department at UMBC. Her research interests include intelligent <sup>fi</sup>nancial investing systems.

Lina Zhou is an Associate Professor of Information Systems, University of Maryland, Baltimore County. Her research aims to improve knowledge management and human decision making by designing and developing intelligent technologies. Dr. Zhou has authored or co-authored over 30 referred papers in journals such as Journal of Management Information Systems, IEEE Transactions, Decision Support Systems, Information & Management, and MIS Quarterly. She is a member of the editorial board of <sup>fi</sup>ve international journals.
