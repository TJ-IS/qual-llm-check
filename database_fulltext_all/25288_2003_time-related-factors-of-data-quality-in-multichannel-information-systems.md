---
otero_id: 25288
otero_key: "SN7NTVTR"
title: "Time-Related Factors of Data Quality in Multichannel Information Systems"
authors: "CINZIA CAPPIELLO; CHIARA FRANCALANCI; BARBARA PERNICI"
year: "2003"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2003.11045769"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/SN7NTVTR/fulltext/images/91d683ad880a60ba1591464032f6368fbf077f3a1fa323fa5ab05dcbf53b2d37.jpg)

## Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Time-Related Factors of Data Quality in Multichannel Information Systems

CINZIA CAPPIELLO , CHIARA FRANCALANCI <sup>a</sup> & BARBARA PERNICI b

<sup>a</sup> Politecnico di Milano

<sup>b</sup> Politecnico di Milano

Published online: 08 Dec 2014.

To cite this article: CINZIA CAPPIELLO , CHIARA FRANCALANCI & BARBARA PERNICI (2003) Time-Related Factors of Data Quality in Multichannel Information Systems, Journal of Management Information Systems, 20:3, 71-92

To link to this article: http://dx.doi.org/10.1080/07421222.2003.11045769

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http:// www.tandfonline.com/page/terms-and-conditions

# Time-Related Factors of Data Quality in Multichannel Information Systems

CINZIA CAPPIELLO, CHIARA FRANCALANCI, AND BARBARA PERNICI

CINZIA CAPPIELLO is a Ph.D. student at Politecnico di Milano, where she has also received a master’s degree in Computer Science. As part of her Ph.D. research, she is working on information quality issues and on the application of data quality techniques to the preservation of Web information.

CHIARA FRANCALANCI is Associate Professor of information systems at Politecnico di Milano. She has a master’s degree in Electronic Engineering from Politecnico di Milano, where she has also completed her Ph.D. in Computer Science. As part of her post-doctoral studies, she has worked for two years at the Harvard Business School as a Visiting Researcher. She has authored articles on the economics of information technology and on feasibility analyses of IT projects, consulted in the financial industry, both in Europe and in the United States, and is a member of the editorial board of the Journal of Information Technology.

BARBARA PERNICI is Full Professor of Computer Engineering at Politecnico di Milano. She has a doctorate in engineering from Politecnico di Milano and an M.S. in Computer Science from Stanford University. Her research interests include e-service, work flow information systems design, cooperative information systems, mobile information systems, and data quality. She has published some 40 papers in international journals. She is a member of the program committee in several international conferences, among them VLDB and SIGMOD, and is a member of the editorial boards of the Requirements Engineering Journal and Journal of Database Management. She is vice-chair of IFIP Working Group 8.1 on Design and Evaluation of Information Systems.

ABSTRACT: Modern organizations offer services through multiple channels, such as branches, ATMs, telephones, and Internet sites, and are supported by multifunctional software architectures. Different functional modules share data, which are typically stored in multiple local databases. Functional modules are usually not integrated across channels, as channels are implemented at different times within independent software projects and are subject to varying requirements of availability and performance. This lack of channel and functional integration raises data quality problems that can impact the quality of the products and services of an organization. In particular, in complex systems in which data are managed in multiple databases, timeliness is critical. This paper focuses on time-related factors of data quality and provides a model that can help companies to evaluate data currency, accuracy, and completeness in software architectures with different degrees of integration across channels and functionalities. The model is validated through simulation based on empirical data on financial information systems. Results indicate how architectural choices on the degree of data integration have a varying impact on currency, accuracy, and completeness depending on the type of financial institution and on customer profiles.

KEY WORDS AND PHRASES: data accuracy, data completeness, data currency, data quality, financial information systems.

DATA QUALITY ISSUES ARE WIDESPREAD in all economic sectors and their relevance is constantly growing. The competitiveness of organizations is increasingly based on the personalization of services, which is enabled by the availability of accurate information on individual customers for all service activities, across all distribution channels, and at all times [10, 21]. Ultimately, the quality of this information depends on the quality of the data that can be extracted from organization’s databases [22]. The data quality literature highlights multiple causes for poor data quality, ranging from dirty data in source databases, to inadequate data management procedures, software errors, and contextual uncertainty [20]. Several authors (e.g., [17, 24]) define the quality of data as their “fitness for use,” that is, the ability of a data collection to meet user requirements. Therefore, the causes for poor data quality are closely related to the applications managing data to satisfy the requirements of the portion of real world modeled by those data [20].

Organizations offering services through multiple channels, such as branches, ATMs, telephones, and Internet sites, are faced with contrasting requirements. On one hand, data management applications should guarantee that data are accurate and up to date, irrespective of the channel selected by customers to access services. On the other hand, full data integration across channels involves high investments that raise costto-quality trade-offs [16]. These contrasting requirements have originated a variety of market solutions, ranging from high-cost fully integrated software architectures, to less expensive modules managing data for a single channel and a single functionality [8, 12]. As separate modules are composed into a complex multichannel system, data integration is obtained with periodic data alignment procedures supported by integration technologies such as data warehouses [13, 18] and distributed databases providing tools for data partitioning and replication [26]. Different from classical data warehouses [1], multichannel architectures can have different refresh periods for different databases. Consequently, delays in data updates can vary across databases and corresponding channels and services. Customers can obtain different values of the same data depending on the combination of channel, service, and time of their data request. Only a subset of these data values is current, accurate, and complete.

The goal of this paper is to provide a model that can help companies analyze the impact of software architectural choices on the currency, accuracy, and completeness of data. The paper proposes a classification of software architectures based on their degree of integration across channels and functionalities. The degree of integration results in different values of currency, accuracy, and completeness delivered to customers.

Operating measures of currency, accuracy, and completeness are tested through simulation based on empirical data on financial information systems (IS). Simulations compare software architectures of financial institutions with varying characteristics of services and customer behavior. Results provide preliminary design criteria for the choice of the most appropriate integration strategy depending on service and customer characteristics of different financial institutions. Traditional and virtual financial institutions are compared to show the benefits of design criteria on the timerelated quality of customer data.

## Data Quality Dimensions in Multichannel Information Systems

DATA QUALITY CAN BE MEASURED along the following dimensions:

• Relevance, granularity, and level of detail, which are associated with data views.

• Accuracy, consistency, currency, and completeness, which are associated with data values.

• Format and ease of interpretation, which are associated with the presentation of data.

• Privacy, security, and ownership, which are general dimensions.

This paper focuses on quality dimensions associated with data values and, in particular, on currency, accuracy, and completeness. In the following, we provide a literature survey to ground the definitions presented in this paper on the previous data quality literature.

Different definitions of accuracy are provided in the data quality literature. In Wang and Strong [25], accuracy is generally defined as “the extent to which data are correct, reliable and certified.” In Redman [20], accuracy is associated with data values and is defined as a measure of the proximity of a data value v to some other value $\nu ^ { \prime }$ that is considered correct. It is simple to determine the level of accuracy of a data value if it represents a characteristic of a real-world entity, which can be used as a source of correct information [4]. If data values are the output of a complex transformation process, accuracy may be difficult to evaluate, as it involves the dynamic assessment of a process, as opposed to the static comparison of values. However, a measure of accuracy can be associated with data sources. It can be defined as the ratio between the number of correct values and the total number of values available from a given source [20]. This definition supports the mathematical measure of accuracy discussed in the “Time-Related Accuracy” section.

The incorrectness of a data value depends on multiple factors, such as syntax errors or representational ambiguities. In multichannel IS, delays in data updates represent a major cause for inaccuracy. Let us consider a data value v stored in two databases at $t _ { o }$ and changed to $\nu ^ { \prime }$ in one database at $t _ { 1 } .$ The misalignment between the two databases involves the inaccuracy of the data value v. According to the definition of accuracy presented in Redman [20], only part of the data are modified to $\nu ^ { \prime }$ and, consequently, not all data report the changes that have occurred in the real world.

The definition of data completeness is consistent across research contributions [3, 20, 25]. In Redman [20], completeness is associated with data values and is defined as the degree to which a specific database includes all the values corresponding to a complete representation of a given set of real-world events as database entities. According to this definition, it is possible to obtain an objective measure of the completeness of a data source by adding up significant data values.

In multichannel IS, a relevant aspect of completeness is the degree to which a database includes all new events within a given time interval. Databases are periodically realigned and a new event may occur between subsequent realignments. This event should be simultaneously registered in all databases to guarantee completeness, but the application generating the new event may update its local database and rely on realignments to propagate data changes to other databases. Between an event and the following realignment, databases are incomplete, as they do not include a data representation of all events.

Currency is not provided a standard definition in the literature. Currency is usually defined as a time measure. In Wang and Strong [25], currency is defined as a time point that indicates the time instant when data are stored in a database. In Ballou et al. [5], currency is defined as a time interval as opposed to a time point, obtained by merging two time intervals: the former ranges from the time when data are stored in a database to the time when data are used, whereas the latter, referred to as the age of data, indicates how old data are when they are stored in a database. Finally, in Bovee et al. [6], currency is defined as the time interval that goes from the time when data are updated to the time when data are used. Delays in propagating changes across databases are a cause for either inaccuracy or incompleteness. If new data are created in a database, other databases within the same multichannel system are incomplete until changes are propagated. If old data are updated, other databases are inaccurate until propagation. The higher the number of changes, the lower the currency, accuracy, and completeness of data. Accordingly, Redman [20] defines currency as a measure of the degree to which data are up to date. This definition of currency is used in the fourth section to provide an operating measure of currency in multichannel IS, which is then used to define corresponding time-related measures of accuracy and completeness.

Data are also associated with a time interval measuring their volatility, that is the average time length for which data remain valid [5]. Volatility is considered a static property that is independent of architectural design choices. For example, the quotation of a stock remains valid for only a few seconds irrespective of architectural choices. When data are accessed from a single source, validity is guaranteed if refresh periods are lower than volatility. However, this condition is not sufficient to satisfy time validity criteria in redundant contexts. For example, let us consider two databases, say A and B, that contain the same data. If at time t a user updates data in database A and another user reads the same data from database B at time t′ (t < t′ ), the latter will read incorrect data. If t and t′ are included within the time interval between two subsequent data realignments. The time interval between two realignments usually depends on architectural choices and related constraints, which are discussed in the next section.

![](/api/attachments/SN7NTVTR/fulltext/images/a8c9d2cd769fbb04d4df4d4d12a4923e902bd5178a2ef5266ec33e40b7ccafb9.jpg)  
Figure 1. Typical Channels and Functionalities of Multichannel Financial Systems

## Integration Strategies for Multichannel Information Systems

THIS PAPER FOCUSES ON FINANCIAL IS as a test case of multichannel systems. Data constitute a critical resource in financial IS and data quality issues are particularly relevant for the following reasons:

1. financial information is inherently critical and errors are consequential;

2. the quality of financial data has a strong economic impact;

3. customers perceive the quality of financial data as an essential component of the quality of service; and

4. multichannel software platforms extract data from a high number of databases and, thus, are more liable to inconsistencies.

Multichannel IS of financial institutions are composed by complex and heterogeneous applications [8]. At a high level, a multichannel software platform can be seen as a black box that receives elementary data extracted from multiple sources and provides an integrated view of information for different financial services and distribution channels. Figure 1 shows the channels and functionalities that are usually implemented in multichannel financial systems.

As discussed in the introduction, functional modules are seldom integrated across channels and operate on private databases that need to be periodically realigned. From a data standpoint, this lack of integration across channels and functionalities raises data quality issues. Users can access financial services from different channels at different time points. For example, a user may withdraw money from an ATM and soon afterward check his or her account balance from the Internet. As money has been withdrawn from a channel different from the Internet, the user may be returned obsolete account information. This type of data currency problems has been found to constitute a significant limit to the overall quality of service. To obviate currency problems, financial institutions should increase the degree of integration of their IS architecture [23]. However, full integration is usually considered too expensive and incremental integration strategies are preferred [11].

![](/api/attachments/SN7NTVTR/fulltext/images/7c7282afc557c9a2faafda179ff6afb7790317ecaf0fdaf31d30cb3aa6a2814a.jpg)  
Figure 2. Data Flows for a User of a Specific Functional Area and Channel (Front-End)

The following sections propose a classification of software architectures based on their degree of integration. Architectures are classified by assuming that users both read and update data from operational databases and do not access source databases directly, that is they cannot follow the dashed path in Figure 2. This assumption is a simplification with respect to practice, but it can be removed without affecting the model proposed in the fourth section. For the sake of simplicity, this paper does not consider the geographical data distribution dimension, which can also raise data replication issues and will be considered by future work.

## Goal of Integration: Fully Integrated Multichannel Architecture

Let $c _ { 1 } , c _ { 2 } , \dots , c _ { N }$ be a set of N channels and $f _ { 1 } , f _ { 2 } , \dots , f _ { M }$ a set of M functionalities. Figure 3 shows the blueprint of a fully integrated architecture where all channels share the same set of functionalities and all functionalities access the same operational database od.

This architecture represents the goal of integration, as it has no time-related problems. Users accessing any functionality from any channel will certainly read and update the same information retrieved from a common operational database.

## Starting Point of Integration: Multichannel Architecture with the Lowest Degree of Integration

The multichannel architecture with the lowest degree of integration is shown in Figure 4. A different software application serves each channel–functionality combination, and each application has access to a separate operational database $o d _ { i j } .$ . Data are periodically aligned with a given refresh period. This represents the worst-case scenario and is not a likely configuration in real financial IS. Most financial institutions have integrated their applications across functionalities for branches, which represent a traditional and consolidated channel. On the contrary, they are likely to implement more recent technology-based channels with separate applications for different functional areas, such as trading and insurance. As they add new services over time, banks may design corresponding functionalities ad hoc for different channels, without integrating them with existing functionalities.

![](/api/attachments/SN7NTVTR/fulltext/images/404c9a7bc419743cc125a6817380f561a3de9df498a227f6e3c7b9d5c9a4761f.jpg)  
Figure 3. Fully Integrated Architecture

![](/api/attachments/SN7NTVTR/fulltext/images/0db719622e306fd1020d1801dcfa58c66e8b06e2c41bca3b865d39f0073bd0da.jpg)  
Figure 4. Architecture with the Lowest Degree of Integration

![](/api/attachments/SN7NTVTR/fulltext/images/b7fcac4536f9b576da7fcd4e8b2cac2a1e5085e3be054d1e26d309a0a51c9c3a.jpg)  
Figure 5. Channel-Integrated Architecture

Although less expensive, this architecture presents data quality problems. Since the number of operational databases to be periodically aligned is potentially high, refresh is a costly activity and the affordable refresh period may be long. Therefore, within the same refresh period, customers may be returned obsolete data if they use different functionalities through the same channel or access the same functionality from different channels at different time points. In the following, this architecture will be considered as the starting point to discuss integration.

## Channel Integration

The degree of integration of the starting-point architecture (Figure 4) can be increased by integrating all functionalities provided by the same channel or by integrating corresponding functional areas across channels. Both strategies are followed in practice. The first strategy will be referred to as channel-integration strategy, the latter as functional-integration strategy. Figure 5 shows the blueprint of the architecture that is obtained by implementing the channel-integration strategy on the starting-point architecture. Note that the architecture in Figure 5 is fully channel-integrated, since the channel-integration strategy has been implemented for all channels. Intermediate degrees of integration are also possible. Users of a fully channel-integrated architecture can realize that they are returned obsolete data only if they change channel, whereas if they access different functionalities through the same channel they will be provided up-to-date data.

## Functional Integration

Figure 6 shows the blueprint of the architecture that is obtained by implementing the functional-integration strategy on the starting-point architecture (Figure 4). The architecture in Figure 6 is fully functionally integrated, since the functional-integration strategy has been implemented for all corresponding functionalities of all channels. Similar to the channel-integration strategy, this strategy allows intermediate degrees of integration. Users of a fully functionally integrated architecture can realize that they are returned obsolete data only if they access different functional areas, irrespective of the channel that is selected to interact with their financial institution.

![](/api/attachments/SN7NTVTR/fulltext/images/dfe389af947975d8a4d76388771f16b2ac02aa7b37cfbdde2e055f80c127e470.jpg)  
Figure 6. Functionally Integrated Architecture

## Time-Related Data Quality Measures

This section presents a model of time-related factors of currency, accuracy, and completeness. Table 1 summarizes the variables of the model. The model is defined for the architecture with the lowest degree of functional and channel integration, which represents the most complex case (see the third section). The definition of time-related variables for architectures with a higher degree of integration is then derived from these initial definitions.

Let us consider a multichannel IS with M functionalities and N channels. The architecture with the lowest degree of integration has $M \times N$ databases, referred to as operational databases $o d _ { i j } ,$ where i and j indicate the ith functionality and the jth channel, respectively. Two given operational databases $o d _ { i j }$ and $o d _ { m n }$ may overlap; that is,

Table 1. Model’s Variables

<table><tr><td>Variable</td><td>Symbol</td><td>Description</td></tr><tr><td>Operational database</td><td> $od_{ij}$ </td><td>Set of data supporting the  $i$ th set of functionalities on the  $j$ th channel.</td></tr><tr><td>Refresh time</td><td> $rt_{ij,mn}$ </td><td>Time interval between alignments of operational databases  $od_{ij}$  and  $od_{mn}$  ( $rt_{ij,mn} = rt_{mn,ij}$ ).</td></tr><tr><td>Operational frequency</td><td> $of_{ij}$ </td><td>Average frequency with which users of the  $i$ th functionality of the  $j$ th channel modify, delete or create one data unit of operational database  $od_{ij}$ .</td></tr><tr><td>Update frequency</td><td> $uf_{ij,.mn}$ </td><td>Average frequency with which users of the  $i$ th functionality of the  $j$ th channel modify or delete a data unit in  $od_{ij} \cap od_{mn}$ , that has already been modified or deleted in  $od_{mn}$ .</td></tr><tr><td>Creation frequency</td><td> $cf_{ij,.mn}$ </td><td>Average frequency with which users of the  $i$ th functionality of the  $j$ th channel create a data unit in  $od_{ij} \cap od_{mn}$ .</td></tr></table>

$$
o d _ {i j, m n} = o d _ {i j} \cap o d _ {m n} \neq \emptyset .
$$

An architecture can be associated with a matrix OD that reports the sets of overlapping data between pairs of operational databases. An element of OD, $o d _ { i j } , _ { m n } ,$ is null if corresponding operational databases $o d _ { i j }$ and $o d _ { m n }$ do not overlap. OD is a symmetric matrix (Figure 7).

Operational databases od of a fully channel-integrated architecture can be obtained from $o d _ { i j }$ as

$$
o d _ {j} = \bigcup_ {i = 1} ^ {M} o d _ {i j}.
$$

Conversely, operational databases $o d _ { i }$ of a fully functionally integrated architecture can be obtained from $o d _ { i j }$ as

$$
o d _ {i} = \bigcup_ {j = 1} ^ {N} o d _ {i j}.
$$

Finally, the operational database od of the $f u l l y$ integrated architecture can be obtained from $o d _ { i j }$ as

$$
o d = \bigcup_ {j = 1} ^ {N} \bigcup_ {i = 1} ^ {M} o d _ {i j}.
$$

$$
O D = \left| \begin{array}{c c c c} 1 & o d _ {1 1, 1 2} & \dots & o d _ {1 1, M N} \\ o d _ {1 2, 1 1} & 1 & \dots & \dots \\ \dots & \dots & \dots & \dots \\ o d _ {M N, 1 1} & \dots & \dots & 1 \end{array} \right| \quad \forall i, j, m, n: i = m \wedge j = n \Rightarrow o d _ {i j, m n} = 1
$$

Figure 7. Matrix of Data Overlaps Between Pairs of Operational Databases

$$
R T = \left| \begin{array}{c c c c} 0 & r t _ {1 1, 1 2} & ... & r t _ {1 1, M N} \\ r t _ {1 2, 1 1} & ... & ... & ... \\ ... & ... & ... & ... \\ r t _ {M N, 1 1} & ... & ... & 0 \end{array} \right| \quad \forall i, j, m, n: i = m \land j = n \Rightarrow r _ {i j, m n} = 0
$$

Figure 8. Matrix of Refresh Periods

Financial institutions have developed their IS architecture incrementally and they have integrated their architecture for only a subset of their channels and functionalities according to contextual criteria. In a multichannel IS that is not fully integrated, there is necessarily data redundancy among operational databases. Data redundancy raises a need for periodic realignments. Each pair of operational databases $o d _ { i j }$ and $o d _ { m n }$ is supposed to be aligned with a refresh period $r t _ { i j , m n } ,$ which represents the time interval with which data used by the mth functionality of the nth channel are updated with data created or modified by the ith functionality of the jth channel, and vice versa, as $r t _ { i j , m n }$ is supposed to be equal to $r t _ { m n , i j }$ (see Table 1).

Refresh periods $r t _ { i j , m n }$ can be represented in a matrix, called RT (Figure 8). An element of RT is not null if corresponding $o d _ { i j , m n } \not = \emptyset$ and if data in $o d _ { i j , m n }$ are actually modified, deleted, or created in $o d _ { i j }$ by users of the ith functionality and jth channel.

As a general observation, the intersection between two operational databases od storing data of the same set of functionalities for different channels can be expected to be greater than the intersection between two operational databases od managing data for different functionalities. In this respect, the channel-integration strategy would pursue the potential data quality advantages from integrating operational databases with larger intersections. However, the actual level of quality perceived by users depends on the frequency of their read and update operations on the data shared across operational databases. A large set of shared data that is only seldom accessed by customers has a limited impact on the level of quality delivered to users even if it is misaligned across different databases [9]. To describe the behavior of customers, operational databases are associated with three parameters:

• The operational frequency $o f _ { i j } ,$ defined as the average frequency with which users of the ith functionality of the jth channel modify, delete, or create a data unit of operational database $o d _ { i j } .$

• The update frequency $u f _ { i j , m n }$ , defined as the average frequency with which users of the ith functionality of the jth channel modify or delete a data unit in $o d _ { i j } \cap$ $o d _ { m n }$

• The create frequency $c f _ { i j , m n } .$ , defined as the average frequency with which users of the ith functionality of the jth channel create a data unit in $o d _ { i j } \cap o d _ { m n } .$

In order to guarantee a given level of quality, refresh periods should decrease as the update and create frequencies increase.

The average number of data units that are updated or created by users of operational database $o d _ { i j }$ and need to be aligned with $o d _ { m n }$ after the refresh period $r t _ { i j , m n }$ evaluates to

$$
d u _ {i j, m n} = \left(u f _ {i j, m n} + c f _ {i j, m n}\right) \times r t _ {i j, m n}.
$$

If $d u _ { i j , m n } < 1$ , alignments occur, on average, after each change in one data unit and users always access current data. Otherwise, users may retrieve data from an operational database that have already been changed within another operational database and are therefore obsolete. Note that since formulas include average values, even if $d u _ { i j , m n } < 1$ , data currency is not guaranteed 100 percent, but occasional out-of-date values can be generated even if the condition above is valid.

## An Operating Measure of Currency

Currency is defined as the degree to which data are up to date in a given operational database [20]. In order to provide currency with a mathematical definition, let us consider an architecture with M functionalities $f _ { i }$ and $N$ channels $c _ { j } .$ . As shown in Figure 2, each operational database is either directly updated by users, or periodically refreshed from data sources or other operational databases.

It is hypothesized that frequencies of data updates and frequencies of data accesses coincide. In financial systems, all operations are registered and, therefore, correspond to updates. Under this hypothesis, from update frequencies $u f _ { i j , m n } ,$ it is possible to calculate the frequency $e f ( t ) _ { i j , m n } ,$ with which, at time t, users of the ith functionality of the jth channel read one data unit in $o d _ { i j } \cap o d _ { m n }$ that has already been modified or deleted in $o d _ { m n } . \mathrm { ~ I f ~ } t _ { 0 }$ is the time of the most recent refresh, the portion of $o d _ { i j } \cap o d _ { m n }$ that is modified or deleted by a user of the mth functionality of the nth channel between $t _ { 0 }$ and t is

$$
\frac {\int_ {0} ^ {t} u f _ {m n , i j} d t}{\left| o d _ {i j , m n} \right|} = \frac {u f _ {m n , i j} \times (t - t _ {0})}{\left| o d _ {i j , m n} \right|} \qquad t _ {0} \leq t \leq t _ {0} + r t _ {i j, m n},
$$

where |o $l _ { i j , m n } ^ { } |$ indicates the cardinality of $o d _ { i j , m n } ,$ , which is the total number of data units in $o d _ { i j } \cap o d _ { m n } .$ . The frequency $e f ( t ) _ { i j , m }$ with which users of the ith functionality of the jth channel read one data unit in $o d _ { i j } \cap o d _ { m n }$ that has already been modified or deleted in $o d _ { m n }$ can be estimated as

$$
e f (t) _ {i j, m n} = \min \left(u f _ {i j, m n} * \frac {\int_ {0} ^ {t} u f _ {m n , i j} d t}{\left| o d _ {i j , m n} \right|}; u f _ {i j, m n}\right),
$$

where $e f ( t ) _ { i j , m n }$ evaluates to $u f _ { i j , m n }$ whenever the update frequency of users of $o d _ { m n }$ is such that data in $o d _ { i j } \cap o d _ { m n }$ are modified multiple times within the refresh period $r t _ { i j , m n } .$ Note that a user of the ith functionality of the jth channel reading an obsolete data unit does not necessarily generate an error. When $o d _ { i j }$ and $o d _ { m n }$ are refreshed, alignment operations can restore data correctness in most cases. However, users accessing obsolete data are offered a lower-quality service and, in financial systems, they typically experience functional restrictions [14, 19]. A measure of the average number of obsolete data accessed within a refresh period by all users of the ith functionality of the jth channel is

$$
\overline {{n}} _ {i j, m n} = \min \left(\int_ {t _ {0}} ^ {t _ {0} + r t _ {i j, m n}} e f (t) _ {i j, m n} d t; | o d _ {i j, m n} |\right).
$$

If $o d _ { i j , m n }$ were independent of each other, the fraction of out-of-date data units in $o d _ { i j }$ could be obtained as the summation of $\overline { { n } } _ { i j , m n }$ for all $o d _ { m n }$ that share data with $o d _ { i j }$ divided by the cardinality of $o d _ { i j } ;$ that is

$$
o u t o f d a t e _ {i j} = \frac {\sum_ {n = 1} ^ {n = N} \sum_ {m = 1} ^ {m = M} \overline {{n}} _ {i j , m n}}{\left| \mathrm{od} _ {i j} \right|}.
$$

A measure of currency of $o d _ { i j }$ could be obtained as

$$
c u r r e n c y _ {i j} = 1 - o u t o f d a t e _ {i j}.
$$

However, the intersections between $o d _ { i j , m n }$ are typically not null. Data items in the intersections change with a frequency that is the sum of the frequencies of all operational databases to which they belong. Therefore, the general expression of currency is more complex and recursively considers the intersection between operational databases $o d _ { i j , m n }$ in order not to account for the same data multiple times.

Note that currency is not affected by data creations, as, by definition, it represents a property of the data values of a specific database that were current at some point in time [20]. New data created in $o d _ { i j }$ do not belong to $o d _ { m n }$ until the next realignment and, therefore, affect $o d _ { m n } \mathrm { ' s }$ data currency only as a consequence of update operations following the first refresh. On the contrary, create operations clearly affect completeness. Based on this observation, the next sections provide a time-related definition of accuracy and completeness.

## Time-Related Accuracy

The time-related issues raised by data duplication represent one of the causes of inaccuracy. Therefore, databases $o d _ { i j }$ have a starting value of accuracy, referred to as

Local $\_ A c c u r a c y _ { i j } ,$ which is further decreased by data duplication issues. Accuracy is defined as the ratio between the number of correct values and the total number of values in a database. According to this definition, the set of inaccurate data due to time-related issues coincides with the set of noncurrent data. This observation has been generalized by Redman [20], observing that when currency is defined as the percentage of up-to-date data in a database, it represents the time-related aspect of accuracy. Accordingly, the accuracy of operational databases $o d _ { i j }$ is defined as

$$
A c c u r a c y _ {i j} = L o c a l \_ a c c u r a c y _ {i j} - o u t o f d a t e _ {i j}.
$$

With this definition, whereas currency is decreased by $o u t o f d a t e _ { i j }$ starting from one, accuracy starts from a value that can be lower than one due to causes of inaccuracy different from time.

## Time-Related Completeness

Let us refer to the completeness of an operational database $o d _ { i j }$ as Local\_Completeness , which represents the ratio between the number of data stored in database $o d _ { i j }$ and the number of data that should be stored in $o d _ { i j }$ in order for $o d _ { i j }$ to be complete. Similar to $L o c a l \_ A c c u r a c y _ { i j } ,$ Local\_Completeness<sub>ij</sub> represents the starting value of completeness that is further reduced by time-related issues. The value of local completeness is correct for $o d _ { i j }$ right after realignments, but should decrease with respect to its initial value during refresh periods as a consequence of create operations in other operational databases that share data with $o d _ { i j }$ . To account for this time dependence of Local\_Completeness , we define the outofdate\_incomplete parameter as follows.

From create frequencies $c f _ { i j , m n } ,$ it is possible to calculate the average number of data units created in $o d _ { i j } \cap o d _ { m n }$ by users of the mth functionality of the nth channel that have not been copied in $o d _ { i j } \mathbf { . }$

$$
\overline {{n}} \_ i n c o m p l e t e _ {i j, m n} = \int_ {t _ {0}} ^ {t _ {0} + r t _ {i j, m n}} c f _ {m n, i j} d t.
$$

The number of incomplete data units due to misalignment problems in $o d _ { i j }$ can be obtained as the sum of $n _ { - }$ incomplete for all $o d _ { m n }$ that share data with $o d _ { i j } .$ :

$$
\text { outofdate\_incomplete} _ {i j} = \sum_ {n = 1} ^ {n = N} \sum_ {m = 1} ^ {m = M -} \overline {{n}} \_ \text { incomplete } _ {i j, m n},
$$

by discarding data items that belong to multiple $o d _ { i j , m n } ,$ according to the recursive procedure discussed for currency in the “An Operating Measure of Currency” section. This parameter is used to define a measure of the completeness of $o d _ { i j }$ between subsequent alignments as

$$
C o m p l e t e n e s s _ {i j} = \frac {\left| o d _ {i j} \right|}{o u t o f d a t e \_ i n c o m p l e t e _ {i j} + \frac {\left| o d _ {i j} \right|}{L o c a l \_ c o m p l e t e n e s s _ {i j}}}.
$$

## Simulation Results

SIMULATIONS COMPARE THE TIME-RELATED MEASURES of accuracy and completeness defined in the previous sections for architectures with different degrees of data integration and for different types of financial institutions. Currency is not reported, as it differs from time-related accuracy by a constant value, as discussed in the “Time-Related Accuracy” section.

Simulations analyze the relationship between the architectural integration strategy and the resulting quality of data. The following types of financial institutions are considered:

• Global institutions, defined as institutions operating in multiple countries and with at least 5 million accounts.

• National institutions, defined as institutions operating in a single country and with at least 1 million accounts (and at most, 5 million accounts).

• Regional institutions, defined as institutions operating in a single country and with at least 300,000 accounts (and at most, 1 million accounts).

• Virtual institutions, defined as institutions managing at least 60 percent of their per-customer transactions through technology-based channels.

Data on customer behavior have been collected through ad hoc interviews with 1,000 customers of Italian banks. The statistical distribution of sample customers has been cross-checked for validity with average data on the age, gender, job, and education of Italian bank customers from the Italian Association of Banks [2]. Customers are classified into three categories depending on the average frequency of their financial transactions, as discussed in [15]:

• Active users, executing more than 200 transactions per year.

• Moderate users, executing more than 20, but less than 200 transactions per year.

• Sleepy users, executing less than 20 transactions per year.

In our sample, different types of financial institutions have a different mix of active, moderate, and sleepy customers, with different patterns of access to services across channels. Table 2 reports the composition of customers for the four different types of financial institutions that have been used for simulations.

Four categories of financial services are considered: home banking, trading, credit card, and insurance. Over 99 percent of each category of services is offered through four types of channels: branch, Internet, call center, and agents. The GSM (global system for mobile communications) channel is not considered for simulation due the low frequency of data accesses. Tables 3 and 4 specify the distribution of customers transactions across services and channels for different types of financial institutions. Values in Tables 3 and 4 are consistent with other empirical benchmarks in the financial literature [15].

Data on the size and redundancy of financial databases have been obtained from a previous multi-case analysis on the quality of service across European financial institutions [7]. A row in a database table has been considered as the data unit. Based on the structure of financial databases and typical services, it has been empirically estimated that each transaction corresponds on average to the modification and the creation of one data unit and to deletion of 10<sup>–3</sup> data unit. These values, combined with the frequency of transactions have allowed the calculation of the operational, update, and create frequencies (see Table 1).

Table 2. Composition of Customers for Different Types of Financial Institutions

<table><tr><td></td><td>Active(percent)</td><td>Moderate(percent)</td><td>Sleepy(percent)</td><td>Percentage ofonline users</td></tr><tr><td>Regional bank</td><td>4.2</td><td>47.4</td><td>48.4</td><td>5.9</td></tr><tr><td>National bank</td><td>11.8</td><td>30.1</td><td>58.1</td><td>2.4</td></tr><tr><td>Global bank</td><td>8.8</td><td>38.2</td><td>53.0</td><td>6.8</td></tr><tr><td>Virtual bank</td><td>50</td><td>25</td><td>25</td><td>81.8</td></tr></table>

Table 3. Distribution of Operational Frequencies Across Functionalities

<table><tr><td></td><td>Home banking (percent)</td><td>Trading (percent)</td><td>Insurance (percent)</td><td>Credit card (percent)</td></tr><tr><td>Case 1—Regional bank</td><td>97.19</td><td>2.77</td><td>0</td><td>0.04</td></tr><tr><td>Case 2—National bank</td><td>95.67</td><td>4.21</td><td>0.04</td><td>0.08</td></tr><tr><td>Case 3—Global bank</td><td>93.28</td><td>6.56</td><td>0.06</td><td>0.10</td></tr><tr><td>Case 4—Virtual bank</td><td>25.9</td><td>73.3</td><td>0.3</td><td>0.5</td></tr></table>

Table 4. Distribution of Operational Frequencies Across Channels

<table><tr><td></td><td>Branch(percent)</td><td>Online channels(percent)</td><td>Agents(percent)</td><td>Internet(percent)</td><td>Call center(percent)</td></tr><tr><td>Case 1—Regional bank</td><td>94.1</td><td>5.9</td><td>0.2</td><td>5.7</td><td>0</td></tr><tr><td>Case 2—National bank</td><td>97.6</td><td>2.4</td><td>0.4</td><td>1.66</td><td>0.34</td></tr><tr><td>Case 3—Global bank</td><td>93.2</td><td>6.8</td><td>0.51</td><td>6.1</td><td>0.19</td></tr><tr><td>Case 4—Virtual bank</td><td>18.2</td><td>81.8</td><td>3.5</td><td>77.8</td><td>0.5</td></tr></table>

Local accuracy and local completeness of operational databases are supposed to be equal to 0.8. Figure 9 reports accuracy and completeness as a function of refresh time for the fully channel- and functional-integrated architectures of a global financial institution. Figures 10, 11, and 12 report corresponding simulation results for national, regional, and virtual institutions, respectively. In all cases, both accuracy and completeness decrease as a function of refresh time. Intuitively, a high frequency of realignments reduces the impact of the level of data integration on quality.

![](/api/attachments/SN7NTVTR/fulltext/images/1b1f3a502899acf842a7725ac798b11354b6c2170f35c973482032d2a5e9a7f2.jpg)

![](/api/attachments/SN7NTVTR/fulltext/images/8bf7d14df1b29851f4b09c137275613ef52308f8ff99af6c3e9d70482b09a0f3.jpg)  
Figure 9. Accuracy and Completeness in Global Financial Institutions

![](/api/attachments/SN7NTVTR/fulltext/images/c49551715e00f9c03aedc614e18c76350c7712e201228b57b23eb769205d3062.jpg)

![](/api/attachments/SN7NTVTR/fulltext/images/f4848c7cd83f1314dbe7643a88237921c28c2bf41f57f26592e0e1920c6fcd84.jpg)  
Figure 10. Accuracy and Completeness in National Financial Institutions

![](/api/attachments/SN7NTVTR/fulltext/images/2189c7d96f68e6a6ab460b22fb7f74210bce0ef6146e77b9ad40c40b980fc409.jpg)  
Figure 11. Accuracy and Completeness in Regional Financial Institutions

![](/api/attachments/SN7NTVTR/fulltext/images/0ee6303e2cebfd822a24dce1d7d90cb4badee119f693e1d9b320711c64bcb3b7.jpg)

Global and national institutions (Figures 9 and 10) show a trade-off between accuracy and completeness. Whereas the former is maximized by channel integration, the latter increases with functional integration. As an explanation, accuracy is significantly reduced if data changes from transactions performed by customers are not updated on all channels in real time; it is less sensitive to transactions that are not performed by a customer, but add new customer data, such as an inbound payment that must be credited to a customer’s account. Customers will realize that they have received a payment simultaneously from all channels even if the architecture is not fully channel-integrated. Conversely, completeness is highly sensitive to the creation of new customer data, even if they are a consequence of inbound transactions. Therefore, from a data quality standpoint, global and national financial institutions should integrate their software architecture across channels, whereas integration across functionalities is less critical.

![](/api/attachments/SN7NTVTR/fulltext/images/be3fec1c7ca9ab7faecf23a71aabe424a8e1eed0a676fb3c7619606986e263c3.jpg)

![](/api/attachments/SN7NTVTR/fulltext/images/9f064ef44af5d6c08c85f3e4f905ed7b0443b883c5bc2861a2cfa6a56d86b598.jpg)  
Figure 12. Accuracy and Completeness in Virtual Financial Institutions

![](/api/attachments/SN7NTVTR/fulltext/images/8d6f6593cfb2f6bd15e9cd3d8edc1e2fba41852d9cae38afcaed6dbec83a2253.jpg)  
Figure 13. Accuracy as a Function of the Percentage of Online Customers

Note that the trade-off between accuracy and completeness disappears in favor of functional integration if customers are supposed to distribute evenly across channels. Figure 13 reports simulation results for the hypothetical case of a national financial institution with a growing percentage of online customers.

Figure 11 shows that both accuracy and completeness are maximized by a functional integration strategy in regional financial institutions. The low frequency of operational transactions in regional institutions is a likely reason for these trends. Results confirm, from a data quality standpoint, the advantages of functional integration that are reported to be pursued in practice by most regional banks [7].

Virtual financial institutions show a trade-off between accuracy and completeness (Figure 12), similar to global and national institutions. However, the trade-off disappears in favor of the functional integration strategy for high values of refresh time. These results indicate that virtual institutions can implement a channel-integration strategy only if their architectures support frequent realignments among channels. Conversely, if the refresh period is longer than 60 hours (three days) a functionalintegration strategy should be implemented to guarantee maximum accuracy and completeness. This seems to raise data quality issues for virtual institutions sharing branches with multiple physical institutions.

## Conclusions

THIS PAPER DEFINES A MATHEMATICAL MODEL to evaluate time-related measures of data accuracy and completeness. The model is simulated to compare data accuracy and completeness in financial institutions characterized by different size and patterns of customers’ access to services and channels. Simulation results show that no single integration strategy is optimal in all cases, whereas accuracy and completeness depend on customer behavior and corresponding perception of data quality. In particular, functional integration would be optimal only in a future scenario when accesses will be more evenly distributed across channels. From a practical standpoint, financial institutions are reported to implement architectural solutions that do not always maximize data quality according to the results of this paper. This may indicate that other contrasting factors drive the architectural choices of financial institutions. Future work will analyze these factors and use the model to identify the values of refresh time that satisfy data quality requirements and architectural constraints simultaneously.

Future work will also examine volatility requirements to obtain consistent values of refresh periods based on required levels of accuracy and completeness. Besides, it will refine the mathematical model to represent accuracy and completeness as statistical distributions around their mean value. In turn, this will allow the representation of customer behavior as a statistical distribution of read, update, and create operations over time. In this way, the degradation of data quality can be analyzed as a function of time within refresh periods of variable length. The model will be applied to compare architectures with different degrees of data integration along a continuum between the fully functional- and fully channel-integrated architectural blueprints. More general suggestions on architectural design will be derived from extended simulation results.

## REFERENCES

1. Anahory, S., and Murray, D. Data Warehousing in the Real World. Reading, MA: Addison-Wesley, 1997.

2. Associazione Bancaria Italiana. Rilevazione dello stato dell’automazione del sistema creditizi [Survey of the state of the automation in the financial industry]. White Paper 2002, Milan.

3. Ballou, D.P., and Pazer, H.L. Modeling data and process quality in multi-input, multioutput information systems. Management Science, 31, 2 (February 1985), 150–162.

4. Ballou, D.P., and Pazer, H.L. Designing data information systems to optimize the accuracy-timeliness tradeoff. Information Systems Research, 6, 1 (1995), 51–72.

5. Ballou, D.P.; Wang, R.; Pazer, H.L.; and Tayi, G.K. Modelling information manufacturing systems to determine information product quality. Management Science, 44, 4 (April 1998), 462–484.

6. Bovee, M.; Srivastava, R.P.; and Mak, B. A conceptual framework and belief-function approach to assessing overall information quality. In E.M. Pierce and R. Katz-Haas (eds.), Proceedings of the Sixth International Conference on Information Quality. Cambridge, MA: MIT Press, 2001, pp. 311–328.

7. Bracchi, G.; Francalanci, C.; and Bognetti, A. La Banca multicanale in Europa [Multichannel Banks in Europe]. Milan: Edibank, 2002.

8. Byers, R.E., and Lederer, P.J. Retail bank services strategy: A model of traditional, electronic, and mixed distribution choices. Journal of Management Information Systems, 18, 2 (Fall 2001), 133–156.

9. Cappiello, C.; Francalanci, C.; and Pernici, B. A model of data currency in multi-channel financial architectures. In C. Fisher and B.N. Davidson (eds.), Proceedings of the Seventh International Conference on Information Quality (ICIQ ’02). Cambridge, MA: MIT Press, 2002, pp. 106–118.

10. Clemons, E.K., and Weber, B.W. Segmentation, differentiation, and flexible pricing: Experiences with information technology and segment-tailored strategies. Journal of Management Information Systems, 11, 2 (Fall 1994), 9–36.

11. Escalate, Inc. Multi-channel integration, a retailer’s perspective. White Paper, Redwood Shores, CA, 2001 (available at www.escalate.com/whitepaper3.htm).

12. FirstLogic, Inc. Guide to data quality, financial institutions. White Paper, La Crosse, WI, 2000.

13. Jarke, M.; Lenzerini, M.; Vassiliou, Y.; and Vassiliadis, P. Fundamentals of Data Warehouse. Berlin: Springer-Verlag, 2000.

14. Kaplan, D.; Krishnan, R.; Padman, R.; and Peters J. Assessing data quality accounting information systems. Communications of the ACM, 41, 2 (February 1998), 72–78.

15. KPMG Consulting. Read your eFuture. White paper, London, Autumn 2000.

16. Loshin, D., and Inbar, D. Integration and the data quality imperative: The data quality monitor. White Paper, Data Junction Corporation, Austin, TX, 2001.

17. Orr, K. Data quality and systems theory. Communications of the ACM, 41, 2 (February 1998), 66–71.

18. Orr, K. Data warehousing technology. White Paper, Ken Orr Institute, Topeka, KS, 2000. 19. Paulson, L.D. Data quality: A rising e-business concern. IT Pro, 2, 4 (July–August 2000), 19. Paulson, L.D. Data quality: A rising e-business concern. IT Pro, 2, 4 (July-August 2000),

10–14.

20. Redman, T.C. Data Quality for the Information Age. Boston: Artech House, 1996.

21. Redman, T.C. The impact of poor data quality on the typical enterprise. Communications of the ACM, 41, 2 (February 1998), 79–82.

22. Redman, T.C. Data Quality: The Field Guide. Boston: Digital Press, 2001.

23. Van der Zee, J.T.M., and de Jong, B. Alignment is not enough: Integrating business and information technology management with the balanced business scorecard. Journal of Management Information Systems, 16, 2 (Fall 1999), 137–158.

24. Wang, R.Y. A product perspective on total data quality management. Communications of the ACM, 41, 2 (February 1998), 58–65.

25. Wang, R.Y., and Strong, D.M. Beyond accuracy: What data quality means to data consumers. Journal of Management Information Systems, 12, 4 (Spring 1996), 5–34.

26. Wiederhold, G.; Ceri, S.; and Pernici, B. Distributed database design methodologies. Proceedings of the IEEE, 75, 5 75, 5 (May 1988), 533–546.
